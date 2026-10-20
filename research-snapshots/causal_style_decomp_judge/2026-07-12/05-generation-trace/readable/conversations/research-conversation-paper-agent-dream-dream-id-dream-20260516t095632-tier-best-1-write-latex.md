# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/54959dd4-c6b2-483d-8e01-175da7151411.jsonl`
- **Structured JSON:** [`4772d7b14fa0765f934d.json`](../../sessions/47/4772d7b14fa0765f934d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T10:14:43.449Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T10:14:43.449Z",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。plan001 在 deadline 前完成 ≥24/30 runs（5 seeds × ≥5 fractions）， 1.5B 在所有核心维度复现 0.5B 发现。6-fraction Spearman ρ 跨 seed 中位数 0.97， 非 trivial n=3 的 1.0。LLaMA N=1 spot-check 10/11 信号方向一致，足够支撑 \"cross-family validated\" 定位。3B 4/4 core signals 方向一致，确认 scale trend 且 揭示 stable_rank Cohen's d 随 scale 下降（0.5B→1.5B→3B），强化 Claim 3 的 scale-dependent sensitivity 子论点。5-seed bootstrap CI 下界 > 0 对所有 Tier 1 信号。 PPL within-gen AUC 跨 1.5B 和 PubMed 均 ≤ 0.58，camera-ready 可升级 \"PPL fails\" 措辞。 论文可自信投 ARR 5/25。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T10:14:43.454Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T10:14:43.454Z",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-16T10:14:43.480Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。plan001 在 deadline 前完成 ≥24/30 runs（5 seeds × ≥5 fractions）， 1.5B 在所有核心维度复现 0.5B 发现。6-fraction Spearman ρ 跨 seed 中位数 0.97， 非 trivial n=3 的 1.0。LLaMA N=1 spot-check 10/11 信号方向一致，足够支撑 "cross-family validated" 定位。3B 4/4 core signals 方向一致，确认 scale trend 且 揭示 stable_rank Cohen's d 随 scale 下降（0.5B→1.5B→3B），强化 Claim 3 的 scale-dependent sensitivity 子论点。5-seed bootstrap CI 下界 > 0 对所有 Tier 1 信号。 PPL within-gen AUC 跨 1.5B 和 PubMed 均 ≤ 0.58，camera-ready 可升级 "PPL fails" 措辞。 论文可自信投 ARR 5/25。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "5daf50f4-9971-4e26-9239-8499b0003773",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T10:14:43.478Z_

```json
{
  "parentUuid": "5daf50f4-9971-4e26-9239-8499b0003773",
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
  "uuid": "cc054683-dfea-4425-8389-48ebac0d47d4",
  "timestamp": "2026-05-16T10:14:43.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T10:14:43.478Z_

```json
{
  "parentUuid": "cc054683-dfea-4425-8389-48ebac0d47d4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "add2096e-e6d6-45c2-8e5f-4963a4580f6d",
  "timestamp": "2026-05-16T10:14:43.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
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
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Assistant

_source line 7 · 2026-05-16T10:14:45.915Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "add2096e-e6d6-45c2-8e5f-4963a4580f6d",
  "isSidechain": false,
  "requestId": "req_011Cb658cYqNQTYmwyvBQYTB",
  "type": "assistant",
  "uuid": "f8905ed3-7e94-4ee1-819a-d2ddd195929e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UydmsgZfKuc2QxUYwU8uhf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11342,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11342
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

_source line 8 · 2026-05-16T10:14:46.403Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F4YKBMHQgMtKyJc9RRTKSD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8905ed3-7e94-4ee1-819a-d2ddd195929e",
  "isSidechain": false,
  "requestId": "req_011Cb658cYqNQTYmwyvBQYTB",
  "type": "assistant",
  "uuid": "a0525da4-3972-4e8e-be8a-1f438fb655c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UydmsgZfKuc2QxUYwU8uhf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11342,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11342
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

_source line 9 · 2026-05-16T10:14:46.725Z_

<details><summary>↩ Tool result · `toolu_01F4YKBMHQgMtKyJc9RRTKSD`</summary>

```text
1	[
2	  {
3	    "name": "1.5B WikiText 5-seed scale validation",
4	    "description": "Qwen2.5-1.5B × WikiText-2 × 6 fractions × 5 seeds × 5 gens",
5	    "results": {
6	      "runs_completed": 25,
7	      "seeds_with_full_coverage": 4,
8	      "fractions_per_seed_median": 6,
9	      "spearman_rho_6frac_per_seed": {
10	        "seed42": 0.97,
11	        "seed43": 0.94,
12	        "seed44": 0.97,
13	        "seed45": 0.97,
14	        "seed46": 1.0
15	      },
16	      "spearman_rho_median_5seed": 0.97,
17	      "spearman_rho_bootstrap_95ci": [
18	        0.93,
19	        1.0
20	      ],
21	      "gen4_ppl_frac0_mean": 12.1,
22	      "gen4_ppl_frac10_mean": 12.4,
23	      "gen4_ppl_frac25_mean": 13.0,
24	      "gen4_ppl_frac50_mean": 13.2,
25	      "gen4_ppl_frac75_mean": 18.5,
26	      "gen4_ppl_frac100_mean": 485.0,
27	      "gen4_stable_rank_frac0_mean": 28.3,
28	      "gen4_stable_rank_frac50_mean": 30.1,
29	      "gen4_stable_rank_frac100_mean": 178.5,
30	      "gen4_spectral_entropy_frac0_mean": 0.718,
31	      "gen4_spectral_entropy_frac100_mean": 0.901,
32	      "gen4_token_entropy_frac0_mean": 2.31,
33	      "gen4_token_entropy_frac100_mean": 0.85,
34	      "stable_rank_cv_across_seeds_frac50": 0.018,
35	      "stable_rank_cv_across_seeds_frac100": 0.025,
36	      "spectral_entropy_cv_across_seeds": 0.0012,
37	      "cohens_d_spectral_entropy_5seed_0v100": 28.5,
38	      "cohens_d_perplexity_5seed_0v100": 18.7,
39	      "cohens_d_stable_rank_5seed_0v100": 10.2,
40	      "cohens_d_stable_rank_5seed_0v50": 2.8,
41	      "bootstrap_ci_lower_all_tier1_gt0": true,
42	      "collapse_magnitude_100pct_ppl": "~40x",
43	      "collapse_magnitude_100pct_sr": "~6.3x",
44	      "baseline_0pct_5seed_cv_ppl": 0.02,
45	      "hellaswag_frac0_mean": 0.519,
46	      "hellaswag_frac100_mean": 0.485
47	    },
48	    "tables": [
49	      {
50	        "name": "Table 2: Cross-scale signal comparison (gen4, 0% vs 100%)",
51	        "columns": [
52	          "signal",
53	          "0.5B_d",
54	          "1.5B_d_5seed",
55	          "1.5B_d_95ci",
56	          "direction"
57	        ],
58	        "rows": [
59	          [
60	            "spectral_entropy",
61	            33.48,
62	            28.5,
63	            "[19.2, 37.8]",
64	            "↑"
65	          ],
66	          [
67	            "perplexity",
68	            20.82,
69	            18.7,
70	            "[12.4, 25.0]",
71	            "↑"
72	          ],
73	          [
74	            "stable_rank",
75	            9.43,
76	            10.2,
77	            "[6.1, 14.3]",
78	            "↑"
79	          ],
80	          [
81	            "token_entropy",
82	            -4.52,
83	            -5.8,
84	            "[-8.9, -2.7]",
85	            "↓"
86	          ],
87	          [
88	            "hellaswag",
89	            1.34,
90	            -2.1,
91	            "[-4.5, 0.3]",
92	            "↓"
93	          ]
94	        ]
95	      },
96	      {
97	        "name": "Table S1: 6-fraction Spearman ρ per seed (1.5B)",
98	        "columns": [
99	          "seed",
100	          "n_fractions",
101	          "rho_stable_rank",
102	          "rho_ppl",
103	          "rho_spectral_entropy"
104	        ],
105	        "rows": [
106	          [
107	            42,
108	            6,
109	            0.97,
110	            1.0,
111	            0.94
112	          ],
113	          [
114	            43,
115	            6,
116	            0.94,
117	            0.97,
118	            0.97
119	          ],
120	          [
121	            44,
122	            6,
123	            0.97,
124	            1.0,
125	            0.94
126	          ],
127	          [
128	            45,
129	            6,
130	            1.0,
131	            0.97,
132	            0.97
133	          ],
134	          [
135	            46,
136	            3,
137	            1.0,
138	            1.0,
139	            1.0
140	          ]
141	        ]
142	      }
143	    ],
144	    "figures": [],
145	    "analysis": "plan001 数据是全文统计基础。5-seed × 6-fraction 矩阵提供了 (1) 非 trivial ρ 证明单调性非偶然，(2) bootstrap CI 证明效应跨 seed 稳健，(3) CV 量化 seed 敏感性。 关键 takeaway：spectral_entropy 仍是 cross-seed 最稳定信号，但 stable_rank 在 5-seed 下 d 值 recover 到 10.2（3-seed 时 9.43），证明 3-seed 估计已合理。\n\n\n1.5B 模型比 0.5B 有更大参数冗余，对中等污染（≤50%）的抗性更强—— frac50 PPL 仅升 ~9%（0.5B 为 ~8%），spectral 变化同样温和。但 frac100 catastrophic collapse 仍发生（PPL ~40x），因为 5 代递归训练最终超越了 任何规模的缓冲能力。关键区别：1.5B 的 collapse 绝对幅度（PPL ~485 vs 0.5B ~839） 更低，但 stable_rank 倍数（~6.3x vs 6.6x）几乎一致——说明权重空间结构性 坍缩与 scale 无关，PPL 差异反映的是 baseline 能力差异而非 collapse 程度差异。 6-fraction 的 Spearman ρ 中位数 0.97 而非 1.0，因为 frac10 和 frac25 在 1.5B 的信号差异极小（参数冗余吸收了轻度污染），偶尔出现 rank tie 或 微小排序翻转。5-seed 的 stable_rank CV=0.018 at frac50 表明 seed 敏感性 可控但非零——seed44 类型的方差贡献者在 5 seed 中被稀释但不消失。 Cohen's d 从 2-seed 的膨胀值回落到 5-seed 合理范围，spectral_entropy 仍最稳定（d=28.5），stable_rank d=10.2（远低于 2-seed 的 61.7 但 CI 下界 > 0）。 25/30 runs 完成（seed46 仅完成 3 fractions 因 GPU 排队延迟，但 4 seeds × 6 fracs 已满足统计功效要求）。\n"
146	  },
147	  {
148	    "name": "PubMed cross-domain validation",
149	    "description": "Qwen2.5-1.5B × PubMed × 6 fractions × 3 seeds × 5 gens",
150	    "results": {
151	      "runs_completed": 72,
152	      "seeds_completed": 3,
153	      "fractions_completed_all_seeds": 5,
154	      "spearman_rho_6frac_per_seed": {
155	        "seed42": 0.94,
156	        "seed43": 0.97,
157	        "seed44": 0.94
158	      },
159	      "spearman_rho_median": 0.94,
160	      "gen4_ppl_frac0_mean": 18.5,
161	      "gen4_ppl_frac50_mean": 20.8,
162	      "gen4_ppl_frac100_mean": 312.0,
163	      "gen4_stable_rank_frac0_mean": 27.8,
164	      "gen4_stable_rank_frac100_mean": 165.2,
165	      "recovery_prevalence_50pct": 0.8,
166	      "recovery_ratio_ppl_50pct": 0.41,
167	      "recovery_ratio_sr_50pct": 0.18,
168	      "spectral_entropy_recovery_ratio": 0.15,
169	      "within_gen_auc_ppl": 0.55,
170	      "within_gen_auc_stable_rank": 0.96,
171	      "cohens_d_spectral_entropy_3seed_0v100": 25.0,
172	      "cohens_d_perplexity_3seed_0v100": 15.5,
173	      "signal_direction_consistency_vs_wikitext": "10/11"
174	    },
175	    "tables": [
176	      {
177	        "name": "Table 3: Cross-domain comparison (gen4 values, frac=100%)",
178	        "columns": [
179	          "signal",
180	          "wikitext_1.5B",
181	          "pubmed_1.5B",
182	          "direction_match"
183	        ],
184	        "rows": [
185	          [
186	            "perplexity",
187	            485,
188	            312,
189	            "✓ (↑)"
190	          ],
191	          [
192	            "stable_rank",
193	            178.5,
194	            165.2,
195	            "✓ (↑)"
196	          ],
197	          [
198	            "spectral_entropy",
199	            0.901,
200	            0.912,
201	            "✓ (↑)"
202	          ],
203	          [
204	            "token_entropy",
205	            0.85,
206	            0.91,
207	            "✓ (↓ from baseline)"
208	          ]
209	        ]
210	      }
211	    ],
212	    "figures": [],
213	    "analysis": "PubMed 数据解决 \"single domain\" 质疑。方向一致性 10/11 证明信号行为非 WikiText-specific。唯一不一致信号（gradient_norm 在 frac25）可归因于 domain-specific optimization landscape。Recovery 的 domain 差异本身是 有价值发现——strengthens Claim 3 的 \"context-dependent signal behavior\"。\n\n\nPubMed 是窄分布专业领域，baseline PPL 高于 WikiText（~18.5 vs ~12.1）因为 biomedical text 词汇多样性更低、专业术语集中。frac100 collapse 绝对 PPL 略低（~312 vs ~485）因为 PubMed 窄分布下 collapsed model 的输出更 predictable（entropy 上限更低）。但结构性 collapse（stable_rank ~165） 与 WikiText（~178）量级一致——再次证明 spectral collapse 与 domain 无关。 Recovery 更弱（RR=0.41 vs WikiText 0.52）因为 PubMed 窄分布使 synthetic corruption fingerprint 更持久——real data 代间训练难以覆盖已被 synthetic 数据重写的专业术语空间。spectral_entropy recovery ratio < 0.2 是最突出的 domain 差异——权重空间一旦被 PubMed 的 narrow synthetic 重写，结构恢复 极其困难。Within-gen PPL AUC=0.55 跨域确认 \"PPL within-gen fails\" 叙事。 ρ=0.94 中位数略低于 WikiText（0.97），因为 PubMed frac10/frac25 的信号 排序在 biomedical 域更 noisy（domain-specific tokenization 影响 low-fraction 信号粒度）。\n"
214	  },
215	  {
216	    "name": "Full FT vs QLoRA comparison",
217	    "description": "0.5B × WikiText-2 × 3 fracs × 1 seed, Full FT (已完成)",
218	    "results": {
219	      "status": "DONE — actual data",
220	      "fullft_100pct_gen4_ppl": 326.19,
221	      "fullft_100pct_gen4_sr": 153.87,
222	      "fullft_100pct_gen4_se": 0.889,
223	      "fullft_100pct_hellaswag": 0.372,
224	      "qlora_100pct_gen4_ppl": 839.2,
225	      "qlora_100pct_gen4_sr": 155.64,
226	      "qlora_100pct_hellaswag": 0.43,
227	      "direction_consistent": "4/4 core signals",
228	      "onset_ratio_fullft": 15.3,
229	      "onset_ratio_qlora": 8.7,
230	      "structural_convergence_sr_gap": 1.7
231	    },
232	    "tables": [
233	      {
234	        "name": "Table 4: Full FT vs QLoRA (actual data)",
235	        "note": "已在 analysis/fullft_vs_qlora_comparison.json"
236	      }
237	    ],
238	    "figures": [],
239	    "analysis": "N=1 限制已知。plan_012 (3-seed Full FT) 在 best 档中完成，将 N=1 升级到 N=3。 当前数据足以支撑 Claim 3 的 method-dependence 叙事，但 Limitations 必须标注。\n\n\n已完成实验。Full FT 15.3x gen1 PPL jump 后饱和（gen1→4 仅 +1.11x），因为 full parameter access 导致 gen1 即完全过拟合到 corrupted distribution，后续 代没有\"新的破坏空间\"。QLoRA 8.7x 初始跳后持续增长（gen1→4: 6.13x），因为 adapter-only 限制了每代过拟合程度，damage 分散到多代累积。终态 spectral convergence（SR ~154 vs ~156）说明两种方法的权重空间最终达到相似的结构性 坍缩程度——路径不同但终点一致。PPL-downstream dissociation（QLoRA PPL 839 > Full FT 326，但 HellaSwag QLoRA 0.43 > Full FT 0.372）因为 QLoRA 的 adapter 冻结了 base model 大部分能力，PPL 反映 adapter 的分布漂移但 base model 的 downstream 能力被隐式保护。\n"
240	  },
241	  {
242	    "name": "1.5B within-gen early warning analysis",
243	    "description": "Pure analysis on plan_001 data: signal divergence at step 50/100/200/500",
244	    "results": {
245	      "stable_rank_step50_rel_div_1.5B_mean": 0.21,
246	      "stable_rank_step50_rel_div_1.5B_std": 0.04,
247	      "training_loss_step50_auc_1.5B": 0.87,
248	      "perplexity_step100_auc_1.5B": 0.93,
249	      "perplexity_step50_auc_1.5B": 0.56,
250	      "spectral_entropy_step50_rel_div": 0.03,
251	      "earliest_reliable_step_sr": 50,
252	      "earliest_reliable_step_training_loss": 50,
253	      "earliest_reliable_step_ppl": 150,
254	      "detection_power_improvement_5seed_vs_1seed": "CI width ~45% narrower"
255	    },
256	    "tables": [
257	      {
258	        "name": "Table 5: Early warning detection power (1.5B, 5-seed mean ± std)",
259	        "columns": [
260	          "signal",
261	          "step50_AUC",
262	          "step100_AUC",
263	          "step200_AUC",
264	          "step500_AUC"
265	        ],
266	        "rows": [
267	          [
268	            "stable_rank",
269	            "0.82±0.06",
270	            "0.91±0.04",
271	            "0.95±0.02",
272	            "0.97±0.01"
273	          ],
274	          [
275	            "training_loss",
276	            "0.87±0.03",
277	            "0.92±0.02",
278	            "0.94±0.02",
279	            "0.93±0.02"
280	          ],
281	          [
282	            "perplexity",
283	            "0.56±0.05",
284	            "0.93±0.03",
285	            "0.95±0.02",
286	            "0.96±0.01"
287	          ],
288	          [
289	            "spectral_entropy",
290	            "0.52±0.04",
291	            "0.55±0.06",
292	            "0.61±0.08",
293	            "0.72±0.10"
294	          ],
295	          [
296	            "token_entropy",
297	            "0.58±0.07",
298	            "0.64±0.06",
299	            "0.71±0.05",
300	            "0.78±0.04"
301	          ]
302	        ]
303	      }
304	    ],
305	    "figures": [],
306	    "analysis": "1.5B 数据确认 within-gen early warning 泛化到更大 scale，但检测阈值需 scale-specific calibration（1.5B 的 step50 幅度是 0.5B 的 ~60%）。 这本身加强 Claim 3 的 \"scale-dependent sensitivity\" 论点。\n\n\n1.5B 的 within-gen 信号幅度预期低于 0.5B（stable_rank step50 rel_div 0.21 vs 0.34），因为更大模型的参数冗余\"吸收\"了早期训练步的 corruption 影响—— adapter 修改占总参数比例更小。但 5-seed 平均后仍可靠检出（std=0.04 意味着 最差 seed 也有 ~0.13 偏差，远超 baseline noise ~0.02）。training_loss 是 1.5B 上的最强 early signal（AUC=0.87），因为 CE loss 直接反映训练数据 分布变化，不受 model capacity 稀释。perplexity within-gen 延迟到 step100 才有效（AUC=0.93），step50 仍无效（AUC=0.56）——held-out PPL 需要模型 充分更新后 eval 分布才显现偏移。spectral_entropy step50 几乎无信号（0.03） 因为它是 late detector，需要累积到 training 后期。\n"
307	  },
308	  {
309	    "name": "ROC analysis with clustered bootstrap",
310	    "description": "Within-gen + cross-gen AUROC, clustered bootstrap by seed × fraction",
311	    "results": {
312	      "within_gen_auc_stable_rank_1.5B": 0.97,
313	      "within_gen_auc_stable_rank_1.5B_ci": [
314	        0.94,
315	        0.99
316	      ],
317	      "within_gen_auc_training_loss_1.5B": 0.91,
318	      "within_gen_auc_training_loss_1.5B_ci": [
319	        0.87,
320	        0.94
321	      ],
322	      "within_gen_auc_ppl_1.5B": 0.55,
323	      "within_gen_auc_ppl_1.5B_ci": [
324	        0.48,
325	        0.62
326	      ],
327	      "within_gen_auc_spectral_entropy_1.5B": 0.63,
328	      "within_gen_auc_ppl_pubmed": 0.53,
329	      "within_gen_auc_stable_rank_pubmed": 0.95,
330	      "cross_gen_auc_ppl": 0.99,
331	      "cross_gen_auc_spectral_entropy": 0.97,
332	      "cross_gen_auc_stable_rank": 0.94,
333	      "clustered_bootstrap_n_clusters": 30,
334	      "sensitivity_at_10pct_progress_sr": 0.82,
335	      "specificity_at_10pct_progress_sr": 0.98
336	    },
337	    "tables": [
338	      {
339	        "name": "Table 6: Within-gen vs Cross-gen AUROC comparison",
340	        "columns": [
341	          "signal",
342	          "within_gen_AUC_0.5B",
343	          "within_gen_AUC_1.5B",
344	          "within_gen_AUC_PubMed",
345	          "cross_gen_AUC"
346	        ],
347	        "rows": [
348	          [
349	            "stable_rank",
350	            0.984,
351	            "0.97 [0.94,0.99]",
352	            0.95,
353	            0.94
354	          ],
355	          [
356	            "training_loss",
357	            0.923,
358	            "0.91 [0.87,0.94]",
359	            0.89,
360	            0.88
361	          ],
362	          [
363	            "perplexity",
364	            0.534,
365	            "0.55 [0.48,0.62]",
366	            0.53,
367	            0.99
368	          ],
369	          [
370	            "spectral_entropy",
371	            0.58,
372	            "0.63 [0.55,0.71]",
373	            0.6,
374	            0.97
375	          ],
376	          [
377	            "token_entropy",
378	            0.478,
379	            "0.51 [0.44,0.58]",
380	            0.49,
381	            0.92
382	          ]
383	        ]
384	      }
385	    ],
386	    "figures": [],
387	    "analysis": "ROC 分析是 Claim 2 的核心证据。三维分层叙事（within-gen → stable_rank, cross-gen → PPL, severity discrimination → spectral_entropy）在多配置 下一致成立。PPL within-gen AUC ≤ 0.6 跨三个独立配置是 camera-ready 升级的充分条件。\n\n\nClustered bootstrap（一个 observation = 一个 seed×fraction 的信号轨迹） 比 naive pooling 更保守——AUC 从 0.5B N=1 的 0.984 降到 1.5B 5-seed clustered 的 0.97，因为 (1) 1.5B amplitude 更小，(2) clustered bootstrap 正确计入了 seed 间变异。但 CI 下界 0.94 仍远超 random（0.5），统计显著。 PPL within-gen AUC 跨 1.5B（0.55）和 PubMed（0.53）均 ≤ 0.6——两配置 独立确认 \"held-out PPL within-gen fails\"，camera-ready 可将措辞从 \"our data suggests\" 升级为 \"consistently observed across scales and domains\"。 Cross-gen 方向完全翻转：PPL 是最强 cross-gen detector（AUC=0.99）， stable_rank 反而最弱（0.94）——因为 cross-gen PPL 累积效应巨大（100x+）， 而 stable_rank 的 cross-gen 变化有 ceiling（structural collapse 有上限）。 sensitivity at 10% progress 从 0.5B 的 0.78 提升到 0.82，因为 5-seed averaging 减少了 false negatives。\n"
388	  },
389	  {
390	    "name": "Signal taxonomy 5-seed full reanalysis",
391	    "description": "Cohen's d ranking across 5 seeds × 6 fractions, full taxonomy table",
392	    "results": {
393	      "top_signal_by_d_5seed": "spectral_entropy",
394	      "cohens_d_spectral_entropy_5seed": 28.5,
395	      "cohens_d_perplexity_5seed": 18.7,
396	      "cohens_d_stable_rank_5seed": 10.2,
397	      "cohens_d_token_entropy_5seed": -5.8,
398	      "cohens_d_gradient_norm_5seed": -3.1,
399	      "cohens_d_hellaswag_5seed": -2.1,
400	      "tier1_count": 4,
401	      "stable_rank_rank_5seed": 3,
402	      "spectral_entropy_cv_5seed": 0.0011,
403	      "stable_rank_cv_5seed": 0.019,
404	      "perplexity_cv_5seed": 0.008,
405	      "bootstrap_ci_lower_gt0_tier1": "4/4",
406	      "bootstrap_ci_crossing0": "hellaswag, gradient_norm",
407	      "frac50_detectable_signals": [
408	        "stable_rank",
409	        "perplexity",
410	        "training_loss"
411	      ],
412	      "frac100_only_signals": [
413	        "spectral_entropy"
414	      ],
415	      "method_dependence_column": {
416	        "hellaswag": "method-dependent (Full FT ✓, QLoRA ✗)",
417	        "gradient_norm": "method-dependent (Full FT monotonic, QLoRA non-monotonic)",
418	        "stable_rank": "method-invariant",
419	        "perplexity": "method-invariant",
420	        "spectral_entropy": "method-invariant"
421	      }
422	    },
423	    "tables": [
424	      {
425	        "name": "Table 7: Signal Taxonomy (5-seed, 1.5B)",
426	        "columns": [
427	          "signal",
428	          "family",
429	          "d_0v100",
430	          "d_95ci",
431	          "CV",
432	          "early_detect",
433	          "cross_gen",
434	          "method_dep"
435	        ],
436	        "rows": [
437	          [
438	            "spectral_entropy",
439	            "spectral",
440	            28.5,
441	            "[19.2,37.8]",
442	            0.0011,
443	            "late (100% only)",
444	            "strong",
445	            "invariant"
446	          ],
447	          [
448	            "perplexity",
449	            "output",
450	            18.7,
451	            "[12.4,25.0]",
452	            0.008,
453	            "cross-gen only",
454	            "strongest",
455	            "invariant"
456	          ],
457	          [
458	            "stable_rank",
459	            "spectral",
460	            10.2,
461	            "[6.1,14.3]",
462	            0.019,
463	            "earliest within-gen",
464	            "moderate",
465	            "invariant"
466	          ],
467	          [
468	            "token_entropy",
469	            "output",
470	            -5.8,
471	            "[-8.9,-2.7]",
472	            0.015,
473	            "moderate",
474	            "moderate",
475	            "invariant"
476	          ],
477	          [
478	            "training_loss",
479	            "output",
480	            7.5,
481	            "[4.2,10.8]",
482	            0.012,
483	            "strong within-gen",
484	            "weak",
485	            "invariant"
486	          ],
487	          [
488	            "gradient_norm",
489	            "gradient",
490	            -3.1,
491	            "[-6.2,0.0]",
492	            0.045,
493	            "unreliable",
494	            "weak",
495	            "dependent"
496	          ],
497	          [
498	            "hellaswag",
499	            "downstream",
500	            -2.1,
501	            "[-4.5,0.3]",
502	            0.031,
503	            "none",
504	            "weak",
505	            "dependent"
506	          ]
507	        ]
508	      }
509	    ],
510	    "figures": [],
511	    "analysis": "Taxonomy table 是 Claim 3 核心 artifact。method-dependence 列是最大升级—— 将 \"signals respond differently\" 升级为 \"same signal can be informative or misleading depending on method\"。5-seed 数据使所有 Tier 1 信号 CI 下界 > 0， 统计结论可靠。\n\n\n5-seed 的 Cohen's d 比 3-seed 更可靠——spectral_entropy 仍居首（d=28.5， 3-seed 时 33.48），因为它 cross-seed 变异最小（CV=0.0011）使得 pooled SD 极低。stable_rank 从 rank 4 回升到 rank 3（d=10.2 vs 3-seed 的 9.43）， 因为第 4、5 seed 稀释了 seed44 的异常方差。perplexity 稳定在 rank 2。 hellaswag 的 CI 跨 0 是因为 0.5B QLoRA 下 downstream 效应极小（仅 -2.5%）， 5 seed 的方差不足以 resolve 这个微小效应——但 Full FT 下效应显著（-12.5%）， 故 taxonomy 标注为 \"method-dependent\" 而非 \"uninformative\"。 frac50 可检出信号仅 3 个（SR, PPL, training_loss）而 spectral_entropy 仅在 frac100 显著（Δ+25.7%）——这是分层策略的核心证据： no single signal covers all severity levels。\n"
512	  },
513	  {
514	    "name": "Per-layer collapse propagation (1.5B)",
515	    "description": "Forward-pass SVD on 1.5B checkpoints, per-layer stable_rank and spectral_entropy",
516	    "results": {
517	      "n_layers_analyzed": 28,
518	      "v_proj_avg_sr_increase_1.5B": "+1.8 across all layers",
519	      "down_proj_local_collapse_layers": [
520	        22,
521	        23,
522	        24
523	      ],
524	      "most_sensitive_submodule": "v_proj",
525	      "layer_propagation_pattern": "v_proj diffuses uniformly; down_proj collapses in final 3 layers",
526	      "scale_comparison_vs_0.5B": {
527	        "v_proj_pattern": "consistent (diffuse across all layers)",
528	        "down_proj_collapse_onset": "later layer (L22 vs L11 in 0.5B, proportionally similar ~80% depth)",
529	        "magnitude": "ΔSR per layer ~1.8 vs 0.5B ~1.5 (slightly larger due to wider layers)"
530	      }
531	    },
532	    "tables": [
533	      {
534	        "name": "Table S3: Per-sub-module ΔSR summary (0.5B vs 1.5B)",
535	        "columns": [
536	          "submodule",
537	          "0.5B_mean_ΔSR",
538	          "1.5B_mean_ΔSR",
539	          "pattern"
540	        ],
541	        "rows": [
542	          [
543	            "v_proj",
544	            "+1.5",
545	            "+1.8",
546	            "uniform diffusion"
547	          ],
548	          [
549	            "k_proj",
550	            "+0.7",
551	            "+0.9",
552	            "mild diffusion"
553	          ],
554	          [
555	            "q_proj",
556	            "+0.5",
557	            "+0.6",
558	            "mild diffusion"
559	          ],
560	          [
561	            "down_proj",
562	            "-2.1 (L11-12)",
563	            "-2.5 (L22-24)",
564	            "local collapse"
565	          ],
566	          [
567	            "up_proj",
568	            "+0.3",
569	            "+0.4",
570	            "minimal change"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "Per-layer 分析是 Supplementary 的 anchor figure。v_proj 作为 within-run 最敏感 indicator 的发现跨 scale 复现。Practitioner takeaway 不变： 优先监控 v_proj stable rank。\n\n\n1.5B 有 28 层 vs 0.5B 的 24 层。v_proj 的 uniform diffusion 是 scale-invariant pattern——每层 v_proj 接收 attention output 并投影到 value space，synthetic data 的 low-diversity attention pattern 导致 v_proj 权重分散化（ΔSR +1~+3） 在任何规模下都发生。down_proj local collapse 出现在 ~80% depth（0.5B: L11-12/24, 1.5B: L22-24/28）——这是 feed-forward network 的 final processing layers 承受最大 gradient 压力的已知现象。ΔSR 幅度略大（1.8 vs 1.5）因为 1.5B hidden dimension 更大，权重矩阵有更多\"维度\"可以 diffuse。这个 scale comparison 加强了 sub-module-centric 叙事的泛化性。\n"
577	  },
578	  {
579	    "name": "Self-recovery deep dive (5-seed + cross-domain)",
580	    "description": "50% contamination recovery analysis with full 6-fraction × 5-seed data",
581	    "results": {
582	      "recovery_prevalence_50pct_wikitext_5seed": "95% (19/20)",
583	      "recovery_prevalence_50pct_pubmed_3seed": "80% (12/15)",
584	      "recovery_ratio_ppl_wikitext_5seed": "0.52 ± 0.025",
585	      "recovery_ratio_ppl_pubmed_3seed": "0.40 ± 0.010",
586	      "recovery_ratio_sr_wikitext": "0.33 ± 0.045",
587	      "recovery_ratio_sr_pubmed": "0.18 ± 0.095",
588	      "frac25_classification": "mild degradation, not recovery",
589	      "frac75_recovery": "absent — monotonic worsening",
590	      "recovery_window": "frac=50% only (25% too mild to recover from, 75% too severe)",
591	      "weight_vs_output_gap": {
592	        "wikitext": "output RR 0.52, weight RR 0.33 → Δ0.19",
593	        "pubmed": "output RR 0.40, weight RR 0.18 → Δ0.22"
594	      },
595	      "cross_domain_delta_significant": true
596	    },
597	    "tables": [
598	      {
599	        "name": "Table S4: Recovery ratio by domain × signal family (5-seed WikiText, 3-seed PubMed)",
600	        "columns": [
601	          "signal",
602	          "wikitext_RR_mean",
603	          "wikitext_RR_std",
604	          "pubmed_RR_mean",
605	          "pubmed_RR_std"
606	        ],
607	        "rows": [
608	          [
609	            "perplexity",
610	            0.52,
611	            0.025,
612	            0.4,
613	            0.01
614	          ],
615	          [
616	            "stable_rank",
617	            0.33,
618	            0.045,
619	            0.18,
620	            0.095
621	          ],
622	          [
623	            "spectral_entropy",
624	            0.31,
625	            0.018,
626	            0.15,
627	            0.038
628	          ],
629	          [
630	            "token_entropy",
631	            0.59,
632	            0.11,
633	            0.44,
634	            0.015
635	          ]
636	        ]
637	      }
638	    ],
639	    "figures": [],
640	    "analysis": "Self-recovery 定位为 observation consistent with Gerstgrasser et al. 2024 data mixing effects。Domain-dependent recovery 是新发现——PubMed 权重空间 恢复显著弱于 WikiText。这强化 Claim 3 但不独立成 claim。\n\n\n5-seed WikiText recovery prevalence 从 3-seed 的 100% 降到 95%——因为 第 4/5 seed 中 gradient_norm 在 frac50 偶尔不 recover（non-monotonic behavior documented in Note 9），但核心信号（PPL, SR, SE）仍 100% recover。 PubMed 80% 一致于已有 2-seed 数据。Recovery 仅发生在 frac=50%——frac25 degradation 太轻（PPL 仅 +8%）所以不存在\"恢复\"概念（从未显著偏离）， frac75 corruption 已足够严重使模型无法在代间 self-correct。 Weight-vs-output gap（output 恢复更快）跨域一致，且 PubMed 更极端 （Δ0.22 vs 0.19），因为窄分布域的 weight-space corruption 更持久。 Recovery ratio 的 std 在 5-seed 下收窄（PPL: ±0.025 vs 3-seed 的 ±0.027）， 表明 3-seed 估计已接近收敛。禁止跨不同信号集比较 prevalence（Note 15）。\n"
641	  },
642	  {
643	    "name": "SIGMA head-to-head",
644	    "description": "SIGMA metrics collected alongside plan_001 signals (killed — insufficient data)",
645	    "results": {
646	      "status": "killed — SIGMA signals integrated into signals.py but plan001 only 10/30 complete",
647	      "usable_sigma_data_points": "~8 runs (those started after SIGMA integration)",
648	      "effective_rank_direction_at_collapse": "+1 (increases, consistent with 0.5B N=2)",
649	      "log_det_correlation_with_sr": ">0.95",
650	      "analysis_feasibility": "insufficient for formal head-to-head; mention in Discussion as preliminary"
651	    },
652	    "tables": [],
653	    "figures": [],
654	    "analysis": "SIGMA head-to-head 在 best 档中是 Discussion 论点而非独立结果。足以回应 \"SIGMA differentiation thin\" 质疑——我们的信号在 training checkpoints 实时 可用，SIGMA 需要 clean reference，这是 operational 而非 fundamental 优势。\n\n\nSIGMA 被集成到 signals.py 后随 plan001 被动收集，但 plan001 仅完成 10/30 runs 时 SIGMA 数据点不足以做正式 head-to-head。有效数据（post-integration runs）约 8 个，足以确认 effective_rank 方向（+1，与 SR 一致——collapse 时 能量分散导致有效秩上升），但不足以比较 detection power。论文中降级为 Discussion 段落的 preliminary observation，不作为正式发现。\n"
655	  },
656	  {
657	    "name": "3B scale spot-check",
658	    "description": "Qwen2.5-3B × WikiText-2 × 3 fracs (0/50/100%) × 1 seed × 5 gens",
659	    "results": {
660	      "runs_completed": 15,
661	      "gen4_values_frac0": {
662	        "ppl": 10.8,
663	        "stable_rank": 31.5,
664	        "spectral_entropy": 0.725,
665	        "token_entropy": 2.38
666	      },
667	      "gen4_values_frac50": {
668	        "ppl": 11.5,
669	        "stable_rank": 33.2,
670	        "spectral_entropy": 0.738,
671	        "token_entropy": 2.32
672	      },
673	      "gen4_values_frac100": {
674	        "ppl": 310.0,
675	        "stable_rank": 195.0,
676	        "spectral_entropy": 0.915,
677	        "token_entropy": 0.78
678	      },
679	      "core_direction_match": "4/4 (SR↑, SE↑, TE↓, PPL↑)",
680	      "scale_trend_cohens_d_sr": {
681	        "0.5B": 9.43,
682	        "1.5B": 10.2,
683	        "3B": 7.8
684	      },
685	      "scale_trend_observation": "stable_rank d decreases at 3B — scale-dependent sensitivity",
686	      "collapse_magnitude_ppl_3B": "~29x (vs 0.5B ~53x, 1.5B ~40x)",
687	      "frac50_ppl_elevation_3B": "~6.5% (vs 0.5B ~8%, 1.5B ~9%)"
688	    },
689	    "tables": [
690	      {
691	        "name": "Table 8: Cross-scale comparison (gen4, frac=100%, N=1 for 3B)",
692	        "columns": [
693	          "metric",
694	          "0.5B",
695	          "1.5B",
696	          "3B",
697	          "direction"
698	        ],
699	        "rows": [
700	          [
701	            "ppl",
702	            839.2,
703	            485,
704	            310,
705	            "↑ (decreasing magnitude)"
706	          ],
707	          [
708	            "stable_rank",
709	            155.6,
710	            178.5,
711	            195.0,
712	            "↑ (increasing magnitude)"
713	          ],
714	          [
715	            "spectral_entropy",
716	            0.884,
717	            0.901,
718	            0.915,
719	            "↑ (converging to ceiling)"
720	          ],
721	          [
722	            "token_entropy",
723	            0.782,
724	            0.85,
725	            0.78,
726	            "↓ (similar floor)"
727	          ],
728	          [
729	            "collapse_ratio_ppl",
730	            "53x",
731	            "40x",
732	            "29x",
733	            "decreasing with scale"
734	          ],
735	          [
736	            "cohens_d_sr",
737	            9.43,
738	            10.2,
739	            7.8,
740	            "non-monotonic"
741	          ]
742	        ]
743	      }
744	    ],
745	    "figures": [],
746	    "analysis": "3B spot-check（N=1）不支撑独立 claim，但作为 third data point 确认 scale trend。 stable_rank d 下降是 Claim 3 的加强项——告知 practitioners 在更大模型上 需要更敏感的 threshold。Limitations 标注 N=1。\n\n\n3B 的 4/4 core direction match 是几乎确定的——collapse 的 spectral 和 output 方向在理论上是 scale-invariant（能量分散、分布坍缩）。关键数值： (1) baseline PPL 更低（10.8 vs 12.1 vs 15.7）——更大模型更好的语言建模能力； (2) frac100 PPL 绝对值更低（310 vs 485 vs 839）但仍 catastrophic（~29x）； (3) stable_rank collapse 幅度更大（195 vs 178 vs 156）——3B 的更大权重矩阵 在 collapse 时有更多\"空间\"分散；(4) Cohen's d for stable_rank 下降到 7.8 因为 baseline SR 更高（31.5 vs 28.3 vs 23.4）使 relative change 更小。 这个 d 下降趋势（9.43 → 10.2 → 7.8，1.5B 略回升是因为 5-seed averaging） 证明 \"even the best within-gen signal has scale-dependent sensitivity\"—— 直接支撑 Claim 3 的 scale-dependent sub-finding。frac50 仅 +6.5% PPL elevation 说明 3B 对中度污染的 resilience 更强（参数冗余更大）。\n"
747	  },
748	  {
749	    "name": "LLaMA cross-family validation",
750	    "description": "LLaMA-3.2-1B × WikiText-2 × 3 fracs (0/50/100%) × 1 seed × 5 gens",
751	    "results": {
752	      "runs_completed": 15,
753	      "gen4_values_frac0": {
754	        "ppl": 14.2,
755	        "stable_rank": 25.8,
756	        "spectral_entropy": 0.71,
757	        "token_entropy": 2.18
758	      },
759	      "gen4_values_frac50": {
760	        "ppl": 16.1,
761	        "stable_rank": 28.0,
762	        "spectral_entropy": 0.724,
763	        "token_entropy": 2.08
764	      },
765	      "gen4_values_frac100": {
766	        "ppl": 620.0,
767	        "stable_rank": 142.0,
768	        "spectral_entropy": 0.875,
769	        "token_entropy": 0.88
770	      },
771	      "signal_direction_consistency": "10/11",
772	      "inconsistent_signal": "gradient_norm (direction flipped at frac=50%)",
773	      "core_4_signal_match": "4/4",
774	      "collapse_ratio_ppl": "~44x",
775	      "frac50_ppl_elevation": "~13%",
776	      "architecture_differences": {
777	        "baseline_sr": "25.8 (vs Qwen 0.5B 23.4, 1.5B 28.3)",
778	        "collapse_sr": "142 (vs Qwen 0.5B 156, 1.5B 178)",
779	        "collapse_se": "0.875 (vs Qwen 0.5B 0.884, 1.5B 0.901)"
780	      }
781	    },
782	    "tables": [
783	      {
784	        "name": "Table 9: Cross-family signal direction comparison",
785	        "columns": [
786	          "signal",
787	          "qwen_direction",
788	          "llama_direction",
789	          "match"
790	        ],
791	        "rows": [
792	          [
793	            "stable_rank",
794	            "↑",
795	            "↑",
796	            "✓"
797	          ],
798	          [
799	            "spectral_entropy",
800	            "↑",
801	            "↑",
802	            "✓"
803	          ],
804	          [
805	            "perplexity",
806	            "↑",
807	            "↑",
808	            "✓"
809	          ],
810	          [
811	            "token_entropy",
812	            "↓",
813	            "↓",
814	            "✓"
815	          ],
816	          [
817	            "training_loss",
818	            "↑",
819	            "↑",
820	            "✓"
821	          ],
822	          [
823	            "gradient_norm",
824	            "↓ (QLoRA)",
825	            "↑ (frac50)",
826	            "✗"
827	          ],
828	          [
829	            "hellaswag",
830	            "↓",
831	            "↓",
832	            "✓"
833	          ],
834	          [
835	            "self_bleu",
836	            "→",
837	            "→",
838	            "✓"
839	          ],
840	          [
841	            "distinct_1",
842	            "↓",
843	            "↓",
844	            "✓"
845	          ],
846	          [
847	            "distinct_2",
848	            "↓",
849	            "↓",
850	            "✓"
851	          ],
852	          [
853	            "distinct_3",
854	            "↓",
855	            "↓",
856	            "✓"
857	          ]
858	        ]
859	      }
860	    ],
861	    "figures": [],
862	    "analysis": "10/11 direction consistency 足以支撑 \"cross-family validated\" 定位（论文 措辞为 validated 而非 proven）。gradient_norm 不一致加强 Claim 3 —— gradient 是 architecture-dependent 信号。N=1 在 Limitations 标注。\n\n\nLLaMA-3.2-1B（1.24B params）与 Qwen2.5-1.5B 规模接近，便于 cross-family 比较。10/11 方向一致因为 collapse 的物理机制（分布坍缩 → spectral 分散 → output entropy 下降）与 architecture 无关——无论 Qwen 的 grouped-query attention 还是 LLaMA 的 standard MHA，synthetic data 递归训练都导致相同的 权重空间退化。唯一不一致的 gradient_norm 在 frac50 方向翻转是因为 LLaMA 的 optimizer landscape 不同（LLaMA 使用 RMSNorm vs Qwen 的 LayerNorm 变体）， 导致 intermediate severity 下的 gradient 行为不同——但这恰好支撑 Claim 3 的 \"gradient signals are architecture-dependent\" 论点。 Collapse ratio（PPL ~44x）介于 Qwen 0.5B（53x）和 1.5B（40x）之间， 与参数量一致（LLaMA 1.24B）。absolute SR collapse 值更低（142 vs 156/178） 因为 LLaMA hidden dimension 更小（2048 vs Qwen-1.5B 的 1536）——wait， 实际上 LLaMA-3.2-1B hidden=2048 > Qwen-0.5B hidden=896，所以 baseline SR 25.8 合理。Collapse SR 142 略低因为 LLaMA 的 16-layer 结构比 Qwen-0.5B 的 24-layer 更 shallow，每层承受更多 corruption 但总累积 diffusion 更小。\n"
863	  },
864	  {
865	    "name": "Full FT 3-seed expansion",
866	    "description": "0.5B × WikiText-2 × 3 fracs × 2 additional seeds, Full FT",
867	    "results": {
868	      "new_seeds": [
869	        43,
870	        44
871	      ],
872	      "total_seeds": 3,
873	      "fullft_100pct_gen4_ppl_mean": 335.0,
874	      "fullft_100pct_gen4_ppl_std": 28.0,
875	      "fullft_100pct_gen4_sr_mean": 155.2,
876	      "fullft_100pct_gen4_sr_std": 3.5,
877	      "fullft_100pct_hellaswag_mean": 0.368,
878	      "fullft_100pct_hellaswag_std": 0.012,
879	      "onset_ratio_mean": 15.8,
880	      "onset_ratio_std": 1.2,
881	      "fullft_vs_qlora_direction_3seed": "4/4 consistent across all 3 seeds",
882	      "ppl_downstream_dissociation_confirmed": true,
883	      "collapse_morphology_consistent": "3/3 seeds show fast-onset-saturation"
884	    },
885	    "tables": [
886	      {
887	        "name": "Table S5: Full FT 3-seed results (gen4)",
888	        "columns": [
889	          "seed",
890	          "frac",
891	          "ppl",
892	          "stable_rank",
893	          "hellaswag"
894	        ],
895	        "rows": [
896	          [
897	            42,
898	            "100%",
899	            326.2,
900	            153.9,
901	            0.372
902	          ],
903	          [
904	            43,
905	            "100%",
906	            352.1,
907	            157.8,
908	            0.358
909	          ],
910	          [
911	            44,
912	            "100%",
913	            328.5,
914	            153.8,
915	            0.374
916	          ]
917	        ]
918	      }
919	    ],
920	    "figures": [],
921	    "analysis": "N=3 Full FT 将 Claim 3 method-dependence 从 \"observed\" 升级到 \"confirmed with variance estimation\"。Limitations 中的 \"N=1 Full FT\" 可移除。\n\n\n3-seed Full FT 确认 N=1 发现不是 seed 偶然。PPL mean 335（±28）vs N=1 的 326——seed 间变异约 8%，说明 Full FT collapse 的终态比 QLoRA 更确定性 （QLoRA PPL seed 变异更大，因为 adapter 随机初始化引入更多 stochasticity）。 Onset ratio 15.8±1.2 证明 Full FT 的 \"gen1 catastrophic jump\" 是 robust 现象而非 seed-specific。HellaSwag 0.368±0.012 确认 Full FT 下 downstream degrade 是 real effect（vs QLoRA 0.43 稳定）——3-seed CI 不跨 0.43， method-dependence 结论 statistically supported。PPL-downstream dissociation 跨 3 seeds 一致是 Claim 3 featured sub-result 的必要条件。\n"
922	  },
923	  {
924	    "name": "MMLU-mini downstream evaluation",
925	    "description": "MMLU-mini on all plan001 checkpoints (1.5B, 5 seeds × 6 fracs × 5 gens)",
926	    "results": {
927	      "baseline_accuracy_frac0": "36.1% ± 0.8%",
928	      "accuracy_frac50_gen4": "35.2% ± 1.0%",
929	      "accuracy_frac100_gen4": "30.5% ± 1.5%",
930	      "accuracy_drop_frac100": "-5.6 pp",
931	      "hellaswag_vs_mmlu_correlation": "r=0.82 (moderate-strong)",
932	      "mmlu_method_dependence": {
933	        "qlora": "mild decline (-5.6 pp at frac100)",
934	        "fullft": "larger decline (~-8 pp, extrapolated)"
935	      },
936	      "mmlu_sensitivity_vs_hellaswag": "more sensitive (larger pp drop)",
937	      "cross_gen_mmlu_trajectory": "monotonic decline at frac=100%, stable at frac≤50%"
938	    },
939	    "tables": [
940	      {
941	        "name": "Table 10: MMLU-mini accuracy across fractions (1.5B, 5-seed mean)",
942	        "columns": [
943	          "fraction",
944	          "gen0",
945	          "gen1",
946	          "gen2",
947	          "gen3",
948	          "gen4"
949	        ],
950	        "rows": [
951	          [
952	            "0%",
953	            36.1,
954	            36.0,
955	            35.9,
956	            36.2,
957	            36.1
958	          ],
959	          [
960	            "50%",
961	            36.0,
962	            35.8,
963	            35.5,
964	            35.4,
965	            35.2
966	          ],
967	          [
968	            "100%",
969	            35.8,
970	            34.2,
971	            32.8,
972	            31.5,
973	            30.5
974	          ]
975	        ]
976	      }
977	    ],
978	    "figures": [],
979	    "analysis": "MMLU-mini 作为第二 downstream benchmark 解决 reviewer concern。关键 insight： downstream 退化是 gradual（不像 PPL 的 sudden jump），这支撑 Claim 2 的 \"PPL and downstream metrics operate on different timescales\" 叙事。\n\n\nMMLU-mini baseline ~36%（与 dry-run 的 36.06% 一致）。frac100 gen4 下降 ~5.6 pp 因为 model collapse 降低了 general reasoning capability—— 但比 HellaSwag（仅 -2.5 pp for QLoRA）更敏感，因为 MMLU 要求 broader knowledge 而 HellaSwag 主要测试 commonsense reasoning 这个更 robust 的 能力。frac50 仅 -0.9 pp 与 HellaSwag 的 frac50 stability 一致——中等 污染不足以损害 downstream capability。这解决了 \"single downstream benchmark\" 质疑，且 MMLU-HellaSwag correlation r=0.82 说明两者捕捉 collapse 的不同 维度（不完全冗余）。Cross-gen 轨迹的 monotonic decline at frac100 证明 downstream 退化是持续累积的，不像 PPL 那样 gen1 就 catastrophic jump。\n"
980	  },
981	  {
982	    "name": "Within-gen AUROC 1.5B 5-seed (formal Claim 2)",
983	    "description": "Recompute within-gen AUROC on plan001 data with clustered bootstrap",
984	    "results": {
985	      "within_gen_auc_stable_rank_1.5B_5seed": 0.97,
986	      "within_gen_auc_stable_rank_ci": [
987	        0.94,
988	        0.99
989	      ],
990	      "within_gen_auc_training_loss_1.5B_5seed": 0.91,
991	      "within_gen_auc_training_loss_ci": [
992	        0.87,
993	        0.94
994	      ],
995	      "within_gen_auc_ppl_1.5B_5seed": 0.55,
996	      "within_gen_auc_ppl_ci": [
997	        0.48,
998	        0.62
999	      ],
1000	      "within_gen_auc_spectral_entropy": 0.63,
1001	      "sensitivity_at_10pct_progress": 0.82,
1002	      "specificity_at_10pct_progress": 0.97,
1003	      "clustered_bootstrap_method": "one observation per fraction×seed pair",
1004	      "n_bootstrap_iterations": 10000,
1005	      "n_clusters": 30,
1006	      "comparison_vs_0.5B_n1": {
1007	        "auc_sr": "0.97 vs 0.984 — lower but CI overlaps",
1008	        "auc_ppl": "0.55 vs 0.534 — consistent near-random"
1009	      }
1010	    },
1011	    "tables": [
1012	      {
1013	        "name": "Table 1 (Main): Within-gen Early Warning AUROC",
1014	        "columns": [
1015	          "signal",
1016	          "AUC_0.5B_N1",
1017	          "AUC_1.5B_5seed",
1018	          "AUC_1.5B_95CI",
1019	          "verdict"
1020	        ],
1021	        "rows": [
1022	          [
1023	            "stable_rank",
1024	            0.984,
1025	            0.97,
1026	            "[0.94, 0.99]",
1027	            "✓ early detector"
1028	          ],
1029	          [
1030	            "training_loss",
1031	            0.923,
1032	            0.91,
1033	            "[0.87, 0.94]",
1034	            "✓ early detector"
1035	          ],
1036	          [
1037	            "perplexity",
1038	            0.534,
1039	            0.55,
1040	            "[0.48, 0.62]",
1041	            "✗ within-gen fails"
1042	          ],
1043	          [
1044	            "spectral_entropy",
1045	            0.58,
1046	            0.63,
1047	            "[0.55, 0.71]",
1048	            "✗ late/non-monotonic"
1049	          ],
1050	          [
1051	            "token_entropy",
1052	            0.478,
1053	            0.51,
1054	            "[0.44, 0.58]",
1055	            "✗ within-gen fails"
1056	          ]
1057	        ]
1058	      }
1059	    ],
1060	    "figures": [],
1061	    "analysis": "plan014 是论文 Claim 2 的 definitive evidence。1.5B 5-seed clustered AUC 替代 0.5B N=1 成为 primary reported number。PPL within-gen failure 跨 3 configurations（0.5B, 1.5B, PubMed）一致确认，camera-ready 可用 strong language：\"held-out evaluation perplexity consistently fails at within-generation detection across model scales and domains.\"\n\n5-seed clustered bootstrap 是 Claim 2 的 gold-standard evidence。AUC 从 0.5B N=1 的 0.984 降到 0.97 有两个原因：(1) 1.5B within-gen 信号幅度更小 （参数冗余稀释），(2) clustered bootstrap 比 naive pooling 更保守。 但 CI 下界 0.94 远超 random 0.5，结论 robust。PPL within-gen AUC=0.55 跨 1.5B 5-seed 确认——CI [0.48, 0.62] 包含 0.5 但偏高是因为 100% contamination 的 late-training steps PPL 终于开始偏移（但太晚无法做 early warning）。sensitivity at 10% progress 从 0.78 提升到 0.82 因为 5-seed averaging 降低了 false negative rate（个别 seed 的 noise 被平滑）。 这些数字直接进入 Abstract 和 Claim 2 Results 段。\n"
1062	  }
1063	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0525da4-3972-4e8e-be8a-1f438fb655c7",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "839ed705-c855-49ab-a78b-c6da3bee16d9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"1.5B WikiText 5-seed scale validation\",\n    \"description\": \"Qwen2.5-1.5B × WikiText-2 × 6 fractions × 5 seeds × 5 gens\",\n    \"results\": {\n      \"runs_completed\": 25,\n      \"seeds_with_full_coverage\": 4,\n      \"fractions_per_seed_median\": 6,\n      \"spearman_rho_6frac_per_seed\": {\n        \"seed42\": 0.97,\n        \"seed43\": 0.94,\n        \"seed44\": 0.97,\n        \"seed45\": 0.97,\n        \"seed46\": 1.0\n      },\n      \"spearman_rho_median_5seed\": 0.97,\n      \"spearman_rho_bootstrap_95ci\": [\n        0.93,\n        1.0\n      ],\n      \"gen4_ppl_frac0_mean\": 12.1,\n      \"gen4_ppl_frac10_mean\": 12.4,\n      \"gen4_ppl_frac25_mean\": 13.0,\n      \"gen4_ppl_frac50_mean\": 13.2,\n      \"gen4_ppl_frac75_mean\": 18.5,\n      \"gen4_ppl_frac100_mean\": 485.0,\n      \"gen4_stable_rank_frac0_mean\": 28.3,\n      \"gen4_stable_rank_frac50_mean\": 30.1,\n      \"gen4_stable_rank_frac100_mean\": 178.5,\n      \"gen4_spectral_entropy_frac0_mean\": 0.718,\n      \"gen4_spectral_entropy_frac100_mean\": 0.901,\n      \"gen4_token_entropy_frac0_mean\": 2.31,\n      \"gen4_token_entropy_frac100_mean\": 0.85,\n      \"stable_rank_cv_across_seeds_frac50\": 0.018,\n      \"stable_rank_cv_across_seeds_frac100\": 0.025,\n      \"spectral_entropy_cv_across_seeds\": 0.0012,\n      \"cohens_d_spectral_entropy_5seed_0v100\": 28.5,\n      \"cohens_d_perplexity_5seed_0v100\": 18.7,\n      \"cohens_d_stable_rank_5seed_0v100\": 10.2,\n      \"cohens_d_stable_rank_5seed_0v50\": 2.8,\n      \"bootstrap_ci_lower_all_tier1_gt0\": true,\n      \"collapse_magnitude_100pct_ppl\": \"~40x\",\n      \"collapse_magnitude_100pct_sr\": \"~6.3x\",\n      \"baseline_0pct_5seed_cv_ppl\": 0.02,\n      \"hellaswag_frac0_mean\": 0.519,\n      \"hellaswag_frac100_mean\": 0.485\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Cross-scale signal comparison (gen4, 0% vs 100%)\",\n        \"columns\": [\n          \"signal\",\n          \"0.5B_d\",\n          \"1.5B_d_5seed\",\n          \"1.5B_d_95ci\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"spectral_entropy\",\n            33.48,\n            28.5,\n            \"[19.2, 37.8]\",\n            \"↑\"\n          ],\n          [\n            \"perplexity\",\n            20.82,\n            18.7,\n            \"[12.4, 25.0]\",\n            \"↑\"\n          ],\n          [\n            \"stable_rank\",\n            9.43,\n            10.2,\n            \"[6.1, 14.3]\",\n            \"↑\"\n          ],\n          [\n            \"token_entropy\",\n            -4.52,\n            -5.8,\n            \"[-8.9, -2.7]\",\n            \"↓\"\n          ],\n          [\n            \"hellaswag\",\n            1.34,\n            -2.1,\n            \"[-4.5, 0.3]\",\n            \"↓\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table S1: 6-fraction Spearman ρ per seed (1.5B)\",\n        \"columns\": [\n          \"seed\",\n          \"n_fractions\",\n          \"rho_stable_rank\",\n          \"rho_ppl\",\n          \"rho_spectral_entropy\"\n        ],\n        \"rows\": [\n          [\n            42,\n            6,\n            0.97,\n            1.0,\n            0.94\n          ],\n          [\n            43,\n            6,\n            0.94,\n            0.97,\n            0.97\n          ],\n          [\n            44,\n            6,\n            0.97,\n            1.0,\n            0.94\n          ],\n          [\n            45,\n            6,\n            1.0,\n            0.97,\n            0.97\n          ],\n          [\n            46,\n            3,\n            1.0,\n            1.0,\n            1.0\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"plan001 数据是全文统计基础。5-seed × 6-fraction 矩阵提供了 (1) 非 trivial ρ 证明单调性非偶然，(2) bootstrap CI 证明效应跨 seed 稳健，(3) CV 量化 seed 敏感性。 关键 takeaway：spectral_entropy 仍是 cross-seed 最稳定信号，但 stable_rank 在 5-seed 下 d 值 recover 到 10.2（3-seed 时 9.43），证明 3-seed 估计已合理。\\n\\n\\n1.5B 模型比 0.5B 有更大参数冗余，对中等污染（≤50%）的抗性更强—— frac50 PPL 仅升 ~9%（0.5B 为 ~8%），spectral 变化同样温和。但 frac100 catastrophic collapse 仍发生（PPL ~40x），因为 5 代递归训练最终超越了 任何规模的缓冲能力。关键区别：1.5B 的 collapse 绝对幅度（PPL ~485 vs 0.5B ~839） 更低，但 stable_rank 倍数（~6.3x vs 6.6x）几乎一致——说明权重空间结构性 坍缩与 scale 无关，PPL 差异反映的是 baseline 能力差异而非 collapse 程度差异。 6-fraction 的 Spearman ρ 中位数 0.97 而非 1.0，因为 frac10 和 frac25 在 1.5B 的信号差异极小（参数冗余吸收了轻度污染），偶尔出现 rank tie 或 微小排序翻转。5-seed 的 stable_rank CV=0.018 at frac50 表明 seed 敏感性 可控但非零——seed44 类型的方差贡献者在 5 seed 中被稀释但不消失。 Cohen's d 从 2-seed 的膨胀值回落到 5-seed 合理范围，spectral_entropy 仍最稳定（d=28.5），stable_rank d=10.2（远低于 2-seed 的 61.7 但 CI 下界 > 0）。 25/30 runs 完成（seed46 仅完成 3 fractions 因 GPU 排队延迟，但 4 seeds × 6 fracs 已满足统计功效要求）。\\n\"\n  },\n  {\n    \"name\": \"PubMed cross-domain validation\",\n    \"description\": \"Qwen2.5-1.5B × PubMed × 6 fractions × 3 seeds × 5 gens\",\n    \"results\": {\n      \"runs_completed\": 72,\n      \"seeds_completed\": 3,\n      \"fractions_completed_all_seeds\": 5,\n      \"spearman_rho_6frac_per_seed\": {\n        \"seed42\": 0.94,\n        \"seed43\": 0.97,\n        \"seed44\": 0.94\n      },\n      \"spearman_rho_median\": 0.94,\n      \"gen4_ppl_frac0_mean\": 18.5,\n      \"gen4_ppl_frac50_mean\": 20.8,\n      \"gen4_ppl_frac100_mean\": 312.0,\n      \"gen4_stable_rank_frac0_mean\": 27.8,\n      \"gen4_stable_rank_frac100_mean\": 165.2,\n      \"recovery_prevalence_50pct\": 0.8,\n      \"recovery_ratio_ppl_50pct\": 0.41,\n      \"recovery_ratio_sr_50pct\": 0.18,\n      \"spectral_entropy_recovery_ratio\": 0.15,\n      \"within_gen_auc_ppl\": 0.55,\n      \"within_gen_auc_stable_rank\": 0.96,\n      \"cohens_d_spectral_entropy_3seed_0v100\": 25.0,\n      \"cohens_d_perplexity_3seed_0v100\": 15.5,\n      \"signal_direction_consistency_vs_wikitext\": \"10/11\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Cross-domain comparison (gen4 values, frac=100%)\",\n        \"columns\": [\n          \"signal\",\n          \"wikitext_1.5B\",\n          \"pubmed_1.5B\",\n          \"direction_match\"\n        ],\n        \"rows\": [\n          [\n            \"perplexity\",\n            485,\n            312,\n            \"✓ (↑)\"\n          ],\n          [\n            \"stable_rank\",\n            178.5,\n            165.2,\n            \"✓ (↑)\"\n          ],\n          [\n            \"spectral_entropy\",\n            0.901,\n            0.912,\n            \"✓ (↑)\"\n          ],\n          [\n            \"token_entropy\",\n            0.85,\n            0.91,\n            \"✓ (↓ from baseline)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PubMed 数据解决 \\\"single domain\\\" 质疑。方向一致性 10/11 证明信号行为非 WikiText-specific。唯一不一致信号（gradient_norm 在 frac25）可归因于 domain-specific optimization landscape。Recovery 的 domain 差异本身是 有价值发现——strengthens Claim 3 的 \\\"context-dependent signal behavior\\\"。\\n\\n\\nPubMed 是窄分布专业领域，baseline PPL 高于 WikiText（~18.5 vs ~12.1）因为 biomedical text 词汇多样性更低、专业术语集中。frac100 collapse 绝对 PPL 略低（~312 vs ~485）因为 PubMed 窄分布下 collapsed model 的输出更 predictable（entropy 上限更低）。但结构性 collapse（stable_rank ~165） 与 WikiText（~178）量级一致——再次证明 spectral collapse 与 domain 无关。 Recovery 更弱（RR=0.41 vs WikiText 0.52）因为 PubMed 窄分布使 synthetic corruption fingerprint 更持久——real data 代间训练难以覆盖已被 synthetic 数据重写的专业术语空间。spectral_entropy recovery ratio < 0.2 是最突出的 domain 差异——权重空间一旦被 PubMed 的 narrow synthetic 重写，结构恢复 极其困难。Within-gen PPL AUC=0.55 跨域确认 \\\"PPL within-gen fails\\\" 叙事。 ρ=0.94 中位数略低于 WikiText（0.97），因为 PubMed frac10/frac25 的信号 排序在 biomedical 域更 noisy（domain-specific tokenization 影响 low-fraction 信号粒度）。\\n\"\n  },\n  {\n    \"name\": \"Full FT vs QLoRA comparison\",\n    \"description\": \"0.5B × WikiText-2 × 3 fracs × 1 seed, Full FT (已完成)\",\n    \"results\": {\n      \"status\": \"DONE — actual data\",\n      \"fullft_100pct_gen4_ppl\": 326.19,\n      \"fullft_100pct_gen4_sr\": 153.87,\n      \"fullft_100pct_gen4_se\": 0.889,\n      \"fullft_100pct_hellaswag\": 0.372,\n      \"qlora_100pct_gen4_ppl\": 839.2,\n      \"qlora_100pct_gen4_sr\": 155.64,\n      \"qlora_100pct_hellaswag\": 0.43,\n      \"direction_consistent\": \"4/4 core signals\",\n      \"onset_ratio_fullft\": 15.3,\n      \"onset_ratio_qlora\": 8.7,\n      \"structural_convergence_sr_gap\": 1.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Full FT vs QLoRA (actual data)\",\n        \"note\": \"已在 analysis/fullft_vs_qlora_comparison.json\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"N=1 限制已知。plan_012 (3-seed Full FT) 在 best 档中完成，将 N=1 升级到 N=3。 当前数据足以支撑 Claim 3 的 method-dependence 叙事，但 Limitations 必须标注。\\n\\n\\n已完成实验。Full FT 15.3x gen1 PPL jump 后饱和（gen1→4 仅 +1.11x），因为 full parameter access 导致 gen1 即完全过拟合到 corrupted distribution，后续 代没有\\\"新的破坏空间\\\"。QLoRA 8.7x 初始跳后持续增长（gen1→4: 6.13x），因为 adapter-only 限制了每代过拟合程度，damage 分散到多代累积。终态 spectral convergence（SR ~154 vs ~156）说明两种方法的权重空间最终达到相似的结构性 坍缩程度——路径不同但终点一致。PPL-downstream dissociation（QLoRA PPL 839 > Full FT 326，但 HellaSwag QLoRA 0.43 > Full FT 0.372）因为 QLoRA 的 adapter 冻结了 base model 大部分能力，PPL 反映 adapter 的分布漂移但 base model 的 downstream 能力被隐式保护。\\n\"\n  },\n  {\n    \"name\": \"1.5B within-gen early warning analysis\",\n    \"description\": \"Pure analysis on plan_001 data: signal divergence at step 50/100/200/500\",\n    \"results\": {\n      \"stable_rank_step50_rel_div_1.5B_mean\": 0.21,\n      \"stable_rank_step50_rel_div_1.5B_std\": 0.04,\n      \"training_loss_step50_auc_1.5B\": 0.87,\n      \"perplexity_step100_auc_1.5B\": 0.93,\n      \"perplexity_step50_auc_1.5B\": 0.56,\n      \"spectral_entropy_step50_rel_div\": 0.03,\n      \"earliest_reliable_step_sr\": 50,\n      \"earliest_reliable_step_training_loss\": 50,\n      \"earliest_reliable_step_ppl\": 150,\n      \"detection_power_improvement_5seed_vs_1seed\": \"CI width ~45% narrower\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Early warning detection power (1.5B, 5-seed mean ± std)\",\n        \"columns\": [\n          \"signal\",\n          \"step50_AUC\",\n          \"step100_AUC\",\n          \"step200_AUC\",\n          \"step500_AUC\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            \"0.82±0.06\",\n            \"0.91±0.04\",\n            \"0.95±0.02\",\n            \"0.97±0.01\"\n          ],\n          [\n            \"training_loss\",\n            \"0.87±0.03\",\n            \"0.92±0.02\",\n            \"0.94±0.02\",\n            \"0.93±0.02\"\n          ],\n          [\n            \"perplexity\",\n            \"0.56±0.05\",\n            \"0.93±0.03\",\n            \"0.95±0.02\",\n            \"0.96±0.01\"\n          ],\n          [\n            \"spectral_entropy\",\n            \"0.52±0.04\",\n            \"0.55±0.06\",\n            \"0.61±0.08\",\n            \"0.72±0.10\"\n          ],\n          [\n            \"token_entropy\",\n            \"0.58±0.07\",\n            \"0.64±0.06\",\n            \"0.71±0.05\",\n            \"0.78±0.04\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"1.5B 数据确认 within-gen early warning 泛化到更大 scale，但检测阈值需 scale-specific calibration（1.5B 的 step50 幅度是 0.5B 的 ~60%）。 这本身加强 Claim 3 的 \\\"scale-dependent sensitivity\\\" 论点。\\n\\n\\n1.5B 的 within-gen 信号幅度预期低于 0.5B（stable_rank step50 rel_div 0.21 vs 0.34），因为更大模型的参数冗余\\\"吸收\\\"了早期训练步的 corruption 影响—— adapter 修改占总参数比例更小。但 5-seed 平均后仍可靠检出（std=0.04 意味着 最差 seed 也有 ~0.13 偏差，远超 baseline noise ~0.02）。training_loss 是 1.5B 上的最强 early signal（AUC=0.87），因为 CE loss 直接反映训练数据 分布变化，不受 model capacity 稀释。perplexity within-gen 延迟到 step100 才有效（AUC=0.93），step50 仍无效（AUC=0.56）——held-out PPL 需要模型 充分更新后 eval 分布才显现偏移。spectral_entropy step50 几乎无信号（0.03） 因为它是 late detector，需要累积到 training 后期。\\n\"\n  },\n  {\n    \"name\": \"ROC analysis with clustered bootstrap\",\n    \"description\": \"Within-gen + cross-gen AUROC, clustered bootstrap by seed × fraction\",\n    \"results\": {\n      \"within_gen_auc_stable_rank_1.5B\": 0.97,\n      \"within_gen_auc_stable_rank_1.5B_ci\": [\n        0.94,\n        0.99\n      ],\n      \"within_gen_auc_training_loss_1.5B\": 0.91,\n      \"within_gen_auc_training_loss_1.5B_ci\": [\n        0.87,\n        0.94\n      ],\n      \"within_gen_auc_ppl_1.5B\": 0.55,\n      \"within_gen_auc_ppl_1.5B_ci\": [\n        0.48,\n        0.62\n      ],\n      \"within_gen_auc_spectral_entropy_1.5B\": 0.63,\n      \"within_gen_auc_ppl_pubmed\": 0.53,\n      \"within_gen_auc_stable_rank_pubmed\": 0.95,\n      \"cross_gen_auc_ppl\": 0.99,\n      \"cross_gen_auc_spectral_entropy\": 0.97,\n      \"cross_gen_auc_stable_rank\": 0.94,\n      \"clustered_bootstrap_n_clusters\": 30,\n      \"sensitivity_at_10pct_progress_sr\": 0.82,\n      \"specificity_at_10pct_progress_sr\": 0.98\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Within-gen vs Cross-gen AUROC comparison\",\n        \"columns\": [\n          \"signal\",\n          \"within_gen_AUC_0.5B\",\n          \"within_gen_AUC_1.5B\",\n          \"within_gen_AUC_PubMed\",\n          \"cross_gen_AUC\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.984,\n            \"0.97 [0.94,0.99]\",\n            0.95,\n            0.94\n          ],\n          [\n            \"training_loss\",\n            0.923,\n            \"0.91 [0.87,0.94]\",\n            0.89,\n            0.88\n          ],\n          [\n            \"perplexity\",\n            0.534,\n            \"0.55 [0.48,0.62]\",\n            0.53,\n            0.99\n          ],\n          [\n            \"spectral_entropy\",\n            0.58,\n            \"0.63 [0.55,0.71]\",\n            0.6,\n            0.97\n          ],\n          [\n            \"token_entropy\",\n            0.478,\n            \"0.51 [0.44,0.58]\",\n            0.49,\n            0.92\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ROC 分析是 Claim 2 的核心证据。三维分层叙事（within-gen → stable_rank, cross-gen → PPL, severity discrimination → spectral_entropy）在多配置 下一致成立。PPL within-gen AUC ≤ 0.6 跨三个独立配置是 camera-ready 升级的充分条件。\\n\\n\\nClustered bootstrap（一个 observation = 一个 seed×fraction 的信号轨迹） 比 naive pooling 更保守——AUC 从 0.5B N=1 的 0.984 降到 1.5B 5-seed clustered 的 0.97，因为 (1) 1.5B amplitude 更小，(2) clustered bootstrap 正确计入了 seed 间变异。但 CI 下界 0.94 仍远超 random（0.5），统计显著。 PPL within-gen AUC 跨 1.5B（0.55）和 PubMed（0.53）均 ≤ 0.6——两配置 独立确认 \\\"held-out PPL within-gen fails\\\"，camera-ready 可将措辞从 \\\"our data suggests\\\" 升级为 \\\"consistently observed across scales and domains\\\"。 Cross-gen 方向完全翻转：PPL 是最强 cross-gen detector（AUC=0.99）， stable_rank 反而最弱（0.94）——因为 cross-gen PPL 累积效应巨大（100x+）， 而 stable_rank 的 cross-gen 变化有 ceiling（structural collapse 有上限）。 sensitivity at 10% progress 从 0.5B 的 0.78 提升到 0.82，因为 5-seed averaging 减少了 false negatives。\\n\"\n  },\n  {\n    \"name\": \"Signal taxonomy 5-seed full reanalysis\",\n    \"description\": \"Cohen's d ranking across 5 seeds × 6 fractions, full taxonomy table\",\n    \"results\": {\n      \"top_signal_by_d_5seed\": \"spectral_entropy\",\n      \"cohens_d_spectral_entropy_5seed\": 28.5,\n      \"cohens_d_perplexity_5seed\": 18.7,\n      \"cohens_d_stable_rank_5seed\": 10.2,\n      \"cohens_d_token_entropy_5seed\": -5.8,\n      \"cohens_d_gradient_norm_5seed\": -3.1,\n      \"cohens_d_hellaswag_5seed\": -2.1,\n      \"tier1_count\": 4,\n      \"stable_rank_rank_5seed\": 3,\n      \"spectral_entropy_cv_5seed\": 0.0011,\n      \"stable_rank_cv_5seed\": 0.019,\n      \"perplexity_cv_5seed\": 0.008,\n      \"bootstrap_ci_lower_gt0_tier1\": \"4/4\",\n      \"bootstrap_ci_crossing0\": \"hellaswag, gradient_norm\",\n      \"frac50_detectable_signals\": [\n        \"stable_rank\",\n        \"perplexity\",\n        \"training_loss\"\n      ],\n      \"frac100_only_signals\": [\n        \"spectral_entropy\"\n      ],\n      \"method_dependence_column\": {\n        \"hellaswag\": \"method-dependent (Full FT ✓, QLoRA ✗)\",\n        \"gradient_norm\": \"method-dependent (Full FT monotonic, QLoRA non-monotonic)\",\n        \"stable_rank\": \"method-invariant\",\n        \"perplexity\": \"method-invariant\",\n        \"spectral_entropy\": \"method-invariant\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Signal Taxonomy (5-seed, 1.5B)\",\n        \"columns\": [\n          \"signal\",\n          \"family\",\n          \"d_0v100\",\n          \"d_95ci\",\n          \"CV\",\n          \"early_detect\",\n          \"cross_gen\",\n          \"method_dep\"\n        ],\n        \"rows\": [\n          [\n            \"spectral_entropy\",\n            \"spectral\",\n            28.5,\n            \"[19.2,37.8]\",\n            0.0011,\n            \"late (100% only)\",\n            \"strong\",\n            \"invariant\"\n          ],\n          [\n            \"perplexity\",\n            \"output\",\n            18.7,\n            \"[12.4,25.0]\",\n            0.008,\n            \"cross-gen only\",\n            \"strongest\",\n            \"invariant\"\n          ],\n          [\n            \"stable_rank\",\n            \"spectral\",\n            10.2,\n            \"[6.1,14.3]\",\n            0.019,\n            \"earliest within-gen\",\n            \"moderate\",\n            \"invariant\"\n          ],\n          [\n            \"token_entropy\",\n            \"output\",\n            -5.8,\n            \"[-8.9,-2.7]\",\n            0.015,\n            \"moderate\",\n            \"moderate\",\n            \"invariant\"\n          ],\n          [\n            \"training_loss\",\n            \"output\",\n            7.5,\n            \"[4.2,10.8]\",\n            0.012,\n            \"strong within-gen\",\n            \"weak\",\n            \"invariant\"\n          ],\n          [\n            \"gradient_norm\",\n            \"gradient\",\n            -3.1,\n            \"[-6.2,0.0]\",\n            0.045,\n            \"unreliable\",\n            \"weak\",\n            \"dependent\"\n          ],\n          [\n            \"hellaswag\",\n            \"downstream\",\n            -2.1,\n            \"[-4.5,0.3]\",\n            0.031,\n            \"none\",\n            \"weak\",\n            \"dependent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Taxonomy table 是 Claim 3 核心 artifact。method-dependence 列是最大升级—— 将 \\\"signals respond differently\\\" 升级为 \\\"same signal can be informative or misleading depending on method\\\"。5-seed 数据使所有 Tier 1 信号 CI 下界 > 0， 统计结论可靠。\\n\\n\\n5-seed 的 Cohen's d 比 3-seed 更可靠——spectral_entropy 仍居首（d=28.5， 3-seed 时 33.48），因为它 cross-seed 变异最小（CV=0.0011）使得 pooled SD 极低。stable_rank 从 rank 4 回升到 rank 3（d=10.2 vs 3-seed 的 9.43）， 因为第 4、5 seed 稀释了 seed44 的异常方差。perplexity 稳定在 rank 2。 hellaswag 的 CI 跨 0 是因为 0.5B QLoRA 下 downstream 效应极小（仅 -2.5%）， 5 seed 的方差不足以 resolve 这个微小效应——但 Full FT 下效应显著（-12.5%）， 故 taxonomy 标注为 \\\"method-dependent\\\" 而非 \\\"uninformative\\\"。 frac50 可检出信号仅 3 个（SR, PPL, training_loss）而 spectral_entropy 仅在 frac100 显著（Δ+25.7%）——这是分层策略的核心证据： no single signal covers all severity levels。\\n\"\n  },\n  {\n    \"name\": \"Per-layer collapse propagation (1.5B)\",\n    \"description\": \"Forward-pass SVD on 1.5B checkpoints, per-layer stable_rank and spectral_entropy\",\n    \"results\": {\n      \"n_layers_analyzed\": 28,\n      \"v_proj_avg_sr_increase_1.5B\": \"+1.8 across all layers\",\n      \"down_proj_local_collapse_layers\": [\n        22,\n        23,\n        24\n      ],\n      \"most_sensitive_submodule\": \"v_proj\",\n      \"layer_propagation_pattern\": \"v_proj diffuses uniformly; down_proj collapses in final 3 layers\",\n      \"scale_comparison_vs_0.5B\": {\n        \"v_proj_pattern\": \"consistent (diffuse across all layers)\",\n        \"down_proj_collapse_onset\": \"later layer (L22 vs L11 in 0.5B, proportionally similar ~80% depth)\",\n        \"magnitude\": \"ΔSR per layer ~1.8 vs 0.5B ~1.5 (slightly larger due to wider layers)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Per-sub-module ΔSR summary (0.5B vs 1.5B)\",\n        \"columns\": [\n          \"submodule\",\n          \"0.5B_mean_ΔSR\",\n          \"1.5B_mean_ΔSR\",\n          \"pattern\"\n        ],\n        \"rows\": [\n          [\n            \"v_proj\",\n            \"+1.5\",\n            \"+1.8\",\n            \"uniform diffusion\"\n          ],\n          [\n            \"k_proj\",\n            \"+0.7\",\n            \"+0.9\",\n            \"mild diffusion\"\n          ],\n          [\n            \"q_proj\",\n            \"+0.5\",\n            \"+0.6\",\n            \"mild diffusion\"\n          ],\n          [\n            \"down_proj\",\n            \"-2.1 (L11-12)\",\n            \"-2.5 (L22-24)\",\n            \"local collapse\"\n          ],\n          [\n            \"up_proj\",\n            \"+0.3\",\n            \"+0.4\",\n            \"minimal change\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-layer 分析是 Supplementary 的 anchor figure。v_proj 作为 within-run 最敏感 indicator 的发现跨 scale 复现。Practitioner takeaway 不变： 优先监控 v_proj stable rank。\\n\\n\\n1.5B 有 28 层 vs 0.5B 的 24 层。v_proj 的 uniform diffusion 是 scale-invariant pattern——每层 v_proj 接收 attention output 并投影到 value space，synthetic data 的 low-diversity attention pattern 导致 v_proj 权重分散化（ΔSR +1~+3） 在任何规模下都发生。down_proj local collapse 出现在 ~80% depth（0.5B: L11-12/24, 1.5B: L22-24/28）——这是 feed-forward network 的 final processing layers 承受最大 gradient 压力的已知现象。ΔSR 幅度略大（1.8 vs 1.5）因为 1.5B hidden dimension 更大，权重矩阵有更多\\\"维度\\\"可以 diffuse。这个 scale comparison 加强了 sub-module-centric 叙事的泛化性。\\n\"\n  },\n  {\n    \"name\": \"Self-recovery deep dive (5-seed + cross-domain)\",\n    \"description\": \"50% contamination recovery analysis with full 6-fraction × 5-seed data\",\n    \"results\": {\n      \"recovery_prevalence_50pct_wikitext_5seed\": \"95% (19/20)\",\n      \"recovery_prevalence_50pct_pubmed_3seed\": \"80% (12/15)\",\n      \"recovery_ratio_ppl_wikitext_5seed\": \"0.52 ± 0.025\",\n      \"recovery_ratio_ppl_pubmed_3seed\": \"0.40 ± 0.010\",\n      \"recovery_ratio_sr_wikitext\": \"0.33 ± 0.045\",\n      \"recovery_ratio_sr_pubmed\": \"0.18 ± 0.095\",\n      \"frac25_classification\": \"mild degradation, not recovery\",\n      \"frac75_recovery\": \"absent — monotonic worsening\",\n      \"recovery_window\": \"frac=50% only (25% too mild to recover from, 75% too severe)\",\n      \"weight_vs_output_gap\": {\n        \"wikitext\": \"output RR 0.52, weight RR 0.33 → Δ0.19\",\n        \"pubmed\": \"output RR 0.40, weight RR 0.18 → Δ0.22\"\n      },\n      \"cross_domain_delta_significant\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Recovery ratio by domain × signal family (5-seed WikiText, 3-seed PubMed)\",\n        \"columns\": [\n          \"signal\",\n          \"wikitext_RR_mean\",\n          \"wikitext_RR_std\",\n          \"pubmed_RR_mean\",\n          \"pubmed_RR_std\"\n        ],\n        \"rows\": [\n          [\n            \"perplexity\",\n            0.52,\n            0.025,\n            0.4,\n            0.01\n          ],\n          [\n            \"stable_rank\",\n            0.33,\n            0.045,\n            0.18,\n            0.095\n          ],\n          [\n            \"spectral_entropy\",\n            0.31,\n            0.018,\n            0.15,\n            0.038\n          ],\n          [\n            \"token_entropy\",\n            0.59,\n            0.11,\n            0.44,\n            0.015\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Self-recovery 定位为 observation consistent with Gerstgrasser et al. 2024 data mixing effects。Domain-dependent recovery 是新发现——PubMed 权重空间 恢复显著弱于 WikiText。这强化 Claim 3 但不独立成 claim。\\n\\n\\n5-seed WikiText recovery prevalence 从 3-seed 的 100% 降到 95%——因为 第 4/5 seed 中 gradient_norm 在 frac50 偶尔不 recover（non-monotonic behavior documented in Note 9），但核心信号（PPL, SR, SE）仍 100% recover。 PubMed 80% 一致于已有 2-seed 数据。Recovery 仅发生在 frac=50%——frac25 degradation 太轻（PPL 仅 +8%）所以不存在\\\"恢复\\\"概念（从未显著偏离）， frac75 corruption 已足够严重使模型无法在代间 self-correct。 Weight-vs-output gap（output 恢复更快）跨域一致，且 PubMed 更极端 （Δ0.22 vs 0.19），因为窄分布域的 weight-space corruption 更持久。 Recovery ratio 的 std 在 5-seed 下收窄（PPL: ±0.025 vs 3-seed 的 ±0.027）， 表明 3-seed 估计已接近收敛。禁止跨不同信号集比较 prevalence（Note 15）。\\n\"\n  },\n  {\n    \"name\": \"SIGMA head-to-head\",\n    \"description\": \"SIGMA metrics collected alongside plan_001 signals (killed — insufficient data)\",\n    \"results\": {\n      \"status\": \"killed — SIGMA signals integrated into signals.py but plan001 only 10/30 complete\",\n      \"usable_sigma_data_points\": \"~8 runs (those started after SIGMA integration)\",\n      \"effective_rank_direction_at_collapse\": \"+1 (increases, consistent with 0.5B N=2)\",\n      \"log_det_correlation_with_sr\": \">0.95\",\n      \"analysis_feasibility\": \"insufficient for formal head-to-head; mention in Discussion as preliminary\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"SIGMA head-to-head 在 best 档中是 Discussion 论点而非独立结果。足以回应 \\\"SIGMA differentiation thin\\\" 质疑——我们的信号在 training checkpoints 实时 可用，SIGMA 需要 clean reference，这是 operational 而非 fundamental 优势。\\n\\n\\nSIGMA 被集成到 signals.py 后随 plan001 被动收集，但 plan001 仅完成 10/30 runs 时 SIGMA 数据点不足以做正式 head-to-head。有效数据（post-integration runs）约 8 个，足以确认 effective_rank 方向（+1，与 SR 一致——collapse 时 能量分散导致有效秩上升），但不足以比较 detection power。论文中降级为 Discussion 段落的 preliminary observation，不作为正式发现。\\n\"\n  },\n  {\n    \"name\": \"3B scale spot-check\",\n    \"description\": \"Qwen2.5-3B × WikiText-2 × 3 fracs (0/50/100%) × 1 seed × 5 gens\",\n    \"results\": {\n      \"runs_completed\": 15,\n      \"gen4_values_frac0\": {\n        \"ppl\": 10.8,\n        \"stable_rank\": 31.5,\n        \"spectral_entropy\": 0.725,\n        \"token_entropy\": 2.38\n      },\n      \"gen4_values_frac50\": {\n        \"ppl\": 11.5,\n        \"stable_rank\": 33.2,\n        \"spectral_entropy\": 0.738,\n        \"token_entropy\": 2.32\n      },\n      \"gen4_values_frac100\": {\n        \"ppl\": 310.0,\n        \"stable_rank\": 195.0,\n        \"spectral_entropy\": 0.915,\n        \"token_entropy\": 0.78\n      },\n      \"core_direction_match\": \"4/4 (SR↑, SE↑, TE↓, PPL↑)\",\n      \"scale_trend_cohens_d_sr\": {\n        \"0.5B\": 9.43,\n        \"1.5B\": 10.2,\n        \"3B\": 7.8\n      },\n      \"scale_trend_observation\": \"stable_rank d decreases at 3B — scale-dependent sensitivity\",\n      \"collapse_magnitude_ppl_3B\": \"~29x (vs 0.5B ~53x, 1.5B ~40x)\",\n      \"frac50_ppl_elevation_3B\": \"~6.5% (vs 0.5B ~8%, 1.5B ~9%)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Cross-scale comparison (gen4, frac=100%, N=1 for 3B)\",\n        \"columns\": [\n          \"metric\",\n          \"0.5B\",\n          \"1.5B\",\n          \"3B\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"ppl\",\n            839.2,\n            485,\n            310,\n            \"↑ (decreasing magnitude)\"\n          ],\n          [\n            \"stable_rank\",\n            155.6,\n            178.5,\n            195.0,\n            \"↑ (increasing magnitude)\"\n          ],\n          [\n            \"spectral_entropy\",\n            0.884,\n            0.901,\n            0.915,\n            \"↑ (converging to ceiling)\"\n          ],\n          [\n            \"token_entropy\",\n            0.782,\n            0.85,\n            0.78,\n            \"↓ (similar floor)\"\n          ],\n          [\n            \"collapse_ratio_ppl\",\n            \"53x\",\n            \"40x\",\n            \"29x\",\n            \"decreasing with scale\"\n          ],\n          [\n            \"cohens_d_sr\",\n            9.43,\n            10.2,\n            7.8,\n            \"non-monotonic\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3B spot-check（N=1）不支撑独立 claim，但作为 third data point 确认 scale trend。 stable_rank d 下降是 Claim 3 的加强项——告知 practitioners 在更大模型上 需要更敏感的 threshold。Limitations 标注 N=1。\\n\\n\\n3B 的 4/4 core direction match 是几乎确定的——collapse 的 spectral 和 output 方向在理论上是 scale-invariant（能量分散、分布坍缩）。关键数值： (1) baseline PPL 更低（10.8 vs 12.1 vs 15.7）——更大模型更好的语言建模能力； (2) frac100 PPL 绝对值更低（310 vs 485 vs 839）但仍 catastrophic（~29x）； (3) stable_rank collapse 幅度更大（195 vs 178 vs 156）——3B 的更大权重矩阵 在 collapse 时有更多\\\"空间\\\"分散；(4) Cohen's d for stable_rank 下降到 7.8 因为 baseline SR 更高（31.5 vs 28.3 vs 23.4）使 relative change 更小。 这个 d 下降趋势（9.43 → 10.2 → 7.8，1.5B 略回升是因为 5-seed averaging） 证明 \\\"even the best within-gen signal has scale-dependent sensitivity\\\"—— 直接支撑 Claim 3 的 scale-dependent sub-finding。frac50 仅 +6.5% PPL elevation 说明 3B 对中度污染的 resilience 更强（参数冗余更大）。\\n\"\n  },\n  {\n    \"name\": \"LLaMA cross-family validation\",\n    \"description\": \"LLaMA-3.2-1B × WikiText-2 × 3 fracs (0/50/100%) × 1 seed × 5 gens\",\n    \"results\": {\n      \"runs_completed\": 15,\n      \"gen4_values_frac0\": {\n        \"ppl\": 14.2,\n        \"stable_rank\": 25.8,\n        \"spectral_entropy\": 0.71,\n        \"token_entropy\": 2.18\n      },\n      \"gen4_values_frac50\": {\n        \"ppl\": 16.1,\n        \"stable_rank\": 28.0,\n        \"spectral_entropy\": 0.724,\n        \"token_entropy\": 2.08\n      },\n      \"gen4_values_frac100\": {\n        \"ppl\": 620.0,\n        \"stable_rank\": 142.0,\n        \"spectral_entropy\": 0.875,\n        \"token_entropy\": 0.88\n      },\n      \"signal_direction_consistency\": \"10/11\",\n      \"inconsistent_signal\": \"gradient_norm (direction flipped at frac=50%)\",\n      \"core_4_signal_match\": \"4/4\",\n      \"collapse_ratio_ppl\": \"~44x\",\n      \"frac50_ppl_elevation\": \"~13%\",\n      \"architecture_differences\": {\n        \"baseline_sr\": \"25.8 (vs Qwen 0.5B 23.4, 1.5B 28.3)\",\n        \"collapse_sr\": \"142 (vs Qwen 0.5B 156, 1.5B 178)\",\n        \"collapse_se\": \"0.875 (vs Qwen 0.5B 0.884, 1.5B 0.901)\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Cross-family signal direction comparison\",\n        \"columns\": [\n          \"signal\",\n          \"qwen_direction\",\n          \"llama_direction\",\n          \"match\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"spectral_entropy\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"perplexity\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"token_entropy\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"training_loss\",\n            \"↑\",\n            \"↑\",\n            \"✓\"\n          ],\n          [\n            \"gradient_norm\",\n            \"↓ (QLoRA)\",\n            \"↑ (frac50)\",\n            \"✗\"\n          ],\n          [\n            \"hellaswag\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"self_bleu\",\n            \"→\",\n            \"→\",\n            \"✓\"\n          ],\n          [\n            \"distinct_1\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"distinct_2\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ],\n          [\n            \"distinct_3\",\n            \"↓\",\n            \"↓\",\n            \"✓\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"10/11 direction consistency 足以支撑 \\\"cross-family validated\\\" 定位（论文 措辞为 validated 而非 proven）。gradient_norm 不一致加强 Claim 3 —— gradient 是 architecture-dependent 信号。N=1 在 Limitations 标注。\\n\\n\\nLLaMA-3.2-1B（1.24B params）与 Qwen2.5-1.5B 规模接近，便于 cross-family 比较。10/11 方向一致因为 collapse 的物理机制（分布坍缩 → spectral 分散 → output entropy 下降）与 architecture 无关——无论 Qwen 的 grouped-query attention 还是 LLaMA 的 standard MHA，synthetic data 递归训练都导致相同的 权重空间退化。唯一不一致的 gradient_norm 在 frac50 方向翻转是因为 LLaMA 的 optimizer landscape 不同（LLaMA 使用 RMSNorm vs Qwen 的 LayerNorm 变体）， 导致 intermediate severity 下的 gradient 行为不同——但这恰好支撑 Claim 3 的 \\\"gradient signals are architecture-dependent\\\" 论点。 Collapse ratio（PPL ~44x）介于 Qwen 0.5B（53x）和 1.5B（40x）之间， 与参数量一致（LLaMA 1.24B）。absolute SR collapse 值更低（142 vs 156/178） 因为 LLaMA hidden dimension 更小（2048 vs Qwen-1.5B 的 1536）——wait， 实际上 LLaMA-3.2-1B hidden=2048 > Qwen-0.5B hidden=896，所以 baseline SR 25.8 合理。Collapse SR 142 略低因为 LLaMA 的 16-layer 结构比 Qwen-0.5B 的 24-layer 更 shallow，每层承受更多 corruption 但总累积 diffusion 更小。\\n\"\n  },\n  {\n    \"name\": \"Full FT 3-seed expansion\",\n    \"description\": \"0.5B × WikiText-2 × 3 fracs × 2 additional seeds, Full FT\",\n    \"results\": {\n      \"new_seeds\": [\n        43,\n        44\n      ],\n      \"total_seeds\": 3,\n      \"fullft_100pct_gen4_ppl_mean\": 335.0,\n      \"fullft_100pct_gen4_ppl_std\": 28.0,\n      \"fullft_100pct_gen4_sr_mean\": 155.2,\n      \"fullft_100pct_gen4_sr_std\": 3.5,\n      \"fullft_100pct_hellaswag_mean\": 0.368,\n      \"fullft_100pct_hellaswag_std\": 0.012,\n      \"onset_ratio_mean\": 15.8,\n      \"onset_ratio_std\": 1.2,\n      \"fullft_vs_qlora_direction_3seed\": \"4/4 consistent across all 3 seeds\",\n      \"ppl_downstream_dissociation_confirmed\": true,\n      \"collapse_morphology_consistent\": \"3/3 seeds show fast-onset-saturation\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S5: Full FT 3-seed results (gen4)\",\n        \"columns\": [\n          \"seed\",\n          \"frac\",\n          \"ppl\",\n          \"stable_rank\",\n          \"hellaswag\"\n        ],\n        \"rows\": [\n          [\n            42,\n            \"100%\",\n            326.2,\n            153.9,\n            0.372\n          ],\n          [\n            43,\n            \"100%\",\n            352.1,\n            157.8,\n            0.358\n          ],\n          [\n            44,\n            \"100%\",\n            328.5,\n            153.8,\n            0.374\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"N=3 Full FT 将 Claim 3 method-dependence 从 \\\"observed\\\" 升级到 \\\"confirmed with variance estimation\\\"。Limitations 中的 \\\"N=1 Full FT\\\" 可移除。\\n\\n\\n3-seed Full FT 确认 N=1 发现不是 seed 偶然。PPL mean 335（±28）vs N=1 的 326——seed 间变异约 8%，说明 Full FT collapse 的终态比 QLoRA 更确定性 （QLoRA PPL seed 变异更大，因为 adapter 随机初始化引入更多 stochasticity）。 Onset ratio 15.8±1.2 证明 Full FT 的 \\\"gen1 catastrophic jump\\\" 是 robust 现象而非 seed-specific。HellaSwag 0.368±0.012 确认 Full FT 下 downstream degrade 是 real effect（vs QLoRA 0.43 稳定）——3-seed CI 不跨 0.43， method-dependence 结论 statistically supported。PPL-downstream dissociation 跨 3 seeds 一致是 Claim 3 featured sub-result 的必要条件。\\n\"\n  },\n  {\n    \"name\": \"MMLU-mini downstream evaluation\",\n    \"description\": \"MMLU-mini on all plan001 checkpoints (1.5B, 5 seeds × 6 fracs × 5 gens)\",\n    \"results\": {\n      \"baseline_accuracy_frac0\": \"36.1% ± 0.8%\",\n      \"accuracy_frac50_gen4\": \"35.2% ± 1.0%\",\n      \"accuracy_frac100_gen4\": \"30.5% ± 1.5%\",\n      \"accuracy_drop_frac100\": \"-5.6 pp\",\n      \"hellaswag_vs_mmlu_correlation\": \"r=0.82 (moderate-strong)\",\n      \"mmlu_method_dependence\": {\n        \"qlora\": \"mild decline (-5.6 pp at frac100)\",\n        \"fullft\": \"larger decline (~-8 pp, extrapolated)\"\n      },\n      \"mmlu_sensitivity_vs_hellaswag\": \"more sensitive (larger pp drop)\",\n      \"cross_gen_mmlu_trajectory\": \"monotonic decline at frac=100%, stable at frac≤50%\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: MMLU-mini accuracy across fractions (1.5B, 5-seed mean)\",\n        \"columns\": [\n          \"fraction\",\n          \"gen0\",\n          \"gen1\",\n          \"gen2\",\n          \"gen3\",\n          \"gen4\"\n        ],\n        \"rows\": [\n          [\n            \"0%\",\n            36.1,\n            36.0,\n            35.9,\n            36.2,\n            36.1\n          ],\n          [\n            \"50%\",\n            36.0,\n            35.8,\n            35.5,\n            35.4,\n            35.2\n          ],\n          [\n            \"100%\",\n            35.8,\n            34.2,\n            32.8,\n            31.5,\n            30.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MMLU-mini 作为第二 downstream benchmark 解决 reviewer concern。关键 insight： downstream 退化是 gradual（不像 PPL 的 sudden jump），这支撑 Claim 2 的 \\\"PPL and downstream metrics operate on different timescales\\\" 叙事。\\n\\n\\nMMLU-mini baseline ~36%（与 dry-run 的 36.06% 一致）。frac100 gen4 下降 ~5.6 pp 因为 model collapse 降低了 general reasoning capability—— 但比 HellaSwag（仅 -2.5 pp for QLoRA）更敏感，因为 MMLU 要求 broader knowledge 而 HellaSwag 主要测试 commonsense reasoning 这个更 robust 的 能力。frac50 仅 -0.9 pp 与 HellaSwag 的 frac50 stability 一致——中等 污染不足以损害 downstream capability。这解决了 \\\"single downstream benchmark\\\" 质疑，且 MMLU-HellaSwag correlation r=0.82 说明两者捕捉 collapse 的不同 维度（不完全冗余）。Cross-gen 轨迹的 monotonic decline at frac100 证明 downstream 退化是持续累积的，不像 PPL 那样 gen1 就 catastrophic jump。\\n\"\n  },\n  {\n    \"name\": \"Within-gen AUROC 1.5B 5-seed (formal Claim 2)\",\n    \"description\": \"Recompute within-gen AUROC on plan001 data with clustered bootstrap\",\n    \"results\": {\n      \"within_gen_auc_stable_rank_1.5B_5seed\": 0.97,\n      \"within_gen_auc_stable_rank_ci\": [\n        0.94,\n        0.99\n      ],\n      \"within_gen_auc_training_loss_1.5B_5seed\": 0.91,\n      \"within_gen_auc_training_loss_ci\": [\n        0.87,\n        0.94\n      ],\n      \"within_gen_auc_ppl_1.5B_5seed\": 0.55,\n      \"within_gen_auc_ppl_ci\": [\n        0.48,\n        0.62\n      ],\n      \"within_gen_auc_spectral_entropy\": 0.63,\n      \"sensitivity_at_10pct_progress\": 0.82,\n      \"specificity_at_10pct_progress\": 0.97,\n      \"clustered_bootstrap_method\": \"one observation per fraction×seed pair\",\n      \"n_bootstrap_iterations\": 10000,\n      \"n_clusters\": 30,\n      \"comparison_vs_0.5B_n1\": {\n        \"auc_sr\": \"0.97 vs 0.984 — lower but CI overlaps\",\n        \"auc_ppl\": \"0.55 vs 0.534 — consistent near-random\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1 (Main): Within-gen Early Warning AUROC\",\n        \"columns\": [\n          \"signal\",\n          \"AUC_0.5B_N1\",\n          \"AUC_1.5B_5seed\",\n          \"AUC_1.5B_95CI\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"stable_rank\",\n            0.984,\n            0.97,\n            \"[0.94, 0.99]\",\n            \"✓ early detector\"\n          ],\n          [\n            \"training_loss\",\n            0.923,\n            0.91,\n            \"[0.87, 0.94]\",\n            \"✓ early detector\"\n          ],\n          [\n            \"perplexity\",\n            0.534,\n            0.55,\n            \"[0.48, 0.62]\",\n            \"✗ within-gen fails\"\n          ],\n          [\n            \"spectral_entropy\",\n            0.58,\n            0.63,\n            \"[0.55, 0.71]\",\n            \"✗ late/non-monotonic\"\n          ],\n          [\n            \"token_entropy\",\n            0.478,\n            0.51,\n            \"[0.44, 0.58]\",\n            \"✗ within-gen fails\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"plan014 是论文 Claim 2 的 definitive evidence。1.5B 5-seed clustered AUC 替代 0.5B N=1 成为 primary reported number。PPL within-gen failure 跨 3 configurations（0.5B, 1.5B, PubMed）一致确认，camera-ready 可用 strong language：\\\"held-out evaluation perplexity consistently fails at within-generation detection across model scales and domains.\\\"\\n\\n5-seed clustered bootstrap 是 Claim 2 的 gold-standard evidence。AUC 从 0.5B N=1 的 0.984 降到 0.97 有两个原因：(1) 1.5B within-gen 信号幅度更小 （参数冗余稀释），(2) clustered bootstrap 比 naive pooling 更保守。 但 CI 下界 0.94 远超 random 0.5，结论 robust。PPL within-gen AUC=0.55 跨 1.5B 5-seed 确认——CI [0.48, 0.62] 包含 0.5 但偏高是因为 100% contamination 的 late-training steps PPL 终于开始偏移（但太晚无法做 early warning）。sensitivity at 10% progress 从 0.78 提升到 0.82 因为 5-seed averaging 降低了 false negative rate（个别 seed 的 noise 被平滑）。 这些数字直接进入 Abstract 和 Claim 2 Results 段。\\n\"\n  }\n]",
      "numLines": 1063,
      "startLine": 1,
      "totalLines": 1063
    }
  },
  "sourceToolAssistantUUID": "a0525da4-3972-4e8e-be8a-1f438fb655c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:14:46.798Z_

<details><summary>↩ Tool result · `toolu_01HCfkvpYhyqdaEzqSgZ8Csa`</summary>

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
  "parentUuid": "a4e9105b-98e9-4314-8783-94fec16ce822",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "00337bbb-634d-42f1-b551-514309e2e559",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper_framing.md",
      "content": "# Paper Framing — collapse_severity_monitor\n\n## Target Venue\n- Primary: EMNLP 2026 via ACL Rolling Review (ARR)\n- Deadline: ARR submission 2026-05-25\n- Backup: ARR June cycle (2026-06-15) if 5/25 not feasible\n\n## Core Claims (3 条)\n\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, maintaining monotonic ordering across tested fractions and generations. (MVP: ρ=1.0 with n=3; to be validated with n=6 fractions × 5 seeds in plan_001. Primary evidence: Spearman ρ with bootstrap CIs; effect sizes elevated as primary evidence, ρ as supporting.)\n\n2. **Early Warning Capability**: Collapse can be detected at moderate contamination (50%) within a single training run: stable rank achieves AUC=0.984 [0.978, 0.989] for within-gen collapse detection, reaching AUC=0.94 (sens=0.78, spec=1.00) at just 10% training progress. Training loss is the second-best within-gen detector (AUC=0.923). ROC analysis must use clustered bootstrap (one observation per fraction×seed) to avoid inflating AUC from serial generation dependence. **Featured sub-result: held-out evaluation perplexity — the metric practitioners most commonly check at eval checkpoints — provides no within-generation early warning (AUC=0.534 ≈ random).** This is because held-out PPL requires multi-generation accumulation before collapse manifests; in contrast, train-set loss (AUC=0.923) detects earlier because it directly measures learning dynamics on the contaminated distribution. Claim 2 Results 段落结构：(a) stable_rank early detection 正面证据, (b) 专门 1 段讨论 PPL within-gen 失效 + 原理解释 + AUC 对比, (c) ROC curves 图。Abstract 加半句：\"notably, held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.53)\"。(Note: stable_rank is seed-sensitive but early-detecting; spectral_entropy is seed-robust but late-detecting (only at 100%). Practitioner recommendation: use stable_rank for within-gen early warning, perplexity for cross-gen severity comparison, spectral_entropy for severity discrimination. Cross-validation needed: plan001 5-seed + plan002 PubMed within-gen ROC, 如果多配置 PPL AUC 一致 ~0.5，camera-ready 可升级措辞。See writing notes 17, 18, 19.)\n\n3. **Non-Uniform Signal Behavior**: The same monitoring signal can be informative under one training method and misleading under another. Spectral signals saturate at extreme severity; gradient norm is non-monotonic under QLoRA but monotonic under Full FT; downstream metrics (HellaSwag) track collapse under Full FT but remain stable under QLoRA. Both methods show large gen1 PPL jumps (Full FT 15.3x, QLoRA 8.7x) but diverge in subsequent evolution: Full FT saturates (gen1→4: 1.11x), QLoRA decelerates but continues (gen1→4: 6.13x). Featured sub-result: PPL-downstream dissociation — QLoRA PPL=839 but hellaswag=0.430 vs Full FT PPL=326 but hellaswag=0.372, meaning PPL-based monitoring overestimates damage under QLoRA and practitioners must consider training method when selecting collapse signals. Terminal spectral convergence (SR ~154-156) noted as observation, not claimed as finding (N=1). Signal taxonomy table should include \"method-dependence\" column.\n\n## Story Spine\n\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\n\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution (plan_009 adds head-to-head to clarify operational vs fundamental advantage). Kalinowski (2024) uses topological analysis but is computationally expensive. Data mixing strategies (Gerstgrasser et al. 2024, Kazdan et al. 2024) study prevention rather than detection. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\n\n- **Our framing**: We conduct a systematic empirical analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × 6 contamination levels × 2 model scales × 2 domains × 2 fine-tuning methods, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: stable rank provides the earliest within-gen warning (AUC=0.94 at 10% training progress) while perplexity provides the most reliable cross-generation severity tracking — but these roles are non-interchangeable. We document a partial self-recovery phenomenon at moderate contamination consistent with known data mixing effects (Gerstgrasser et al. 2024), and characterize where standard monitoring signals mislead practitioners.\n\n- **Headline result template**: \"Stable rank detects within-generation collapse with AUC=0.984, reaching actionable sensitivity (AUC=0.94) at 10% training progress. Across generations, spectral entropy provides the most robust severity discrimination (CV=0.0015) but is a late detector (only at 100% contamination). Held-out evaluation perplexity — often the go-to metric at eval checkpoints — is nearly ineffective for within-generation detection (AUC=0.534), while train-set loss detects data distribution shift (AUC=0.923) but not model quality degradation; evaluation perplexity remains the strongest cross-generation severity tracker. Different signals have complementary operating ranges; no single signal suffices across all detection contexts.\" (Note: ρ ≥ 0.94 是 plan001 验证目标，非当前实际数值，到手前用 effect size 表述。分层信号策略替代单一 headline signal。ROC 数据来自 plan005 within-gen 分析，N=1 seed。)\n\n## Anticipated Reviewer Concerns & Mitigation\n\n| Concern | Severity | Mitigation |\n|---------|----------|------------|\n| Statistical power (seeds) | CRITICAL | 5 seeds WikiText, 3 seeds PubMed; bootstrap CIs for all claims |\n| n=3 fractions → trivial ρ=1.0 | HIGH | 6 fractions (0/10/25/50/75/100%) |\n| Single model scale | HIGH | 0.5B + 1.5B (+ 3B spot-check if GPU permits) |\n| Single dataset | HIGH | WikiText-2 + PubMed (3 seeds each) |\n| QLoRA only | MEDIUM | Full FT comparison on 1 config (plan_003) |\n| ROC pools non-independent observations | HIGH | Clustered bootstrap or one-gen-per-run restriction (plan_005) |\n| Stable rank direction under collapse | MEDIUM | Clarify: ‖W‖_F² grows faster than σ₁² → SR increases = energy dispersal, not concentration. Fix text |\n| No theoretical grounding | MEDIUM | Informal argument: 75% phase transition ↔ distributional shift theory; when spectral monitoring fails (capacity redundancy) |\n| \"First\" claims overclaimed | MEDIUM | Qualify: \"first systematic multi-axis comparison in iterative fine-tuning setting.\" Self-recovery → cite Gerstgrasser et al. |\n| SIGMA differentiation thin | MEDIUM | Head-to-head (plan_009): run SIGMA at training checkpoints |\n| Related work too thin | HIGH | ≥20 refs: Briesch 2023, Hataya 2023, Gerstgrasser 2024, Seddik 2024, Dohmatob \"Tale of Tails\" 2024, Pennington & Worah 2017 |\n| Missing synthetic data gen params | LOW | Document temperature, top-p/k, max length, prompt format in Methods |\n| No code/data release | MEDIUM | Release monitoring toolkit + signal trajectories + generation scripts |\n| \"Not a monitoring system\" | LOW | Frame as analysis paper; taxonomy + early warning = practical value |\n| No intervention/mitigation | LOW | Explicit non-goal; future work |\n\n## Core Insight (一句话)\n\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\n\n## Novelty Statement\n\nWe provide the first systematic multi-axis comparison of training-time signal families as collapse severity monitors, spanning contamination levels, model scales, text domains, and fine-tuning methods. The within-generation early warning capability (stable rank AUC=0.94 at 10% training progress), the signal operating-range taxonomy, and the documentation of where standard monitoring signals actively mislead practitioners are the primary empirical contributions. The self-recovery observation at moderate contamination is consistent with known data mixing effects and is positioned as a finding rather than a novel phenomenon.\n\n## Key Writing Notes (from Dream review, 2026-05-14)\n\n1. **Effect sizes > ρ**: Elevate effect size tables as primary evidence; ρ as supporting.\n2. **Stable rank direction**: SR increases under collapse = energy dispersal (Frobenius norm grows faster than spectral norm), not concentration. Fix text.\n3. **25% contamination**: \"mild degradation / near-stability\", NOT \"strong recovery\" (PPL monotonically increases).\n4. **Figures required**: Severity curves, ROC curves, heatmaps, per-layer propagation. Analysis paper without figures is a major gap.\n5. **Reproducibility**: Code release, signal trajectories, generation scripts for D&B track.\n6. **Collapse protocol**: Explicitly state whether fine-tuning from M₀ or M_{g-1} and discuss implications.\n7. **Per-layer 叙事修正 (D011, 2026-05-15)**: 废弃\"三区结构\"（boundary/middle-neutral/late-bifurcation），改为 sub-module-centric 分析。真实数据显示 v_proj 在几乎所有层 diffuse（ΔSR +1~+3），down_proj 在 L11-L12 局部 collapse，其余子模块温和。Practitioner takeaway: 优先监控 v_proj stable rank 作为最敏感的 within-run collapse indicator。（注：cross-seed 稳定性另论，参见写作笔记 16。within-run 灵敏度与 cross-seed 排名是不同维度。）\n8. **SIGMA 方向 provisional (C001/D014, 2026-05-15)**: expected_direction=+1（effective_rank 在 collapse 时上升）是 N=2 观测，非已验证结论。禁止在论文中当发现写。验证条件：plan_001 seed43-46 全量数据 + plan_003 Full FT SIGMA 数据。如果 Full FT 方向一致(+1)可排除 QLoRA confound；如果不一致需重写分析。\"Within-gen corruption vs recursive collapse 方向差异\"作为 discussion 论点需要等验证后才能使用。\n9. **Non-monotonic claim scope (plan008/plan003, 2026-05-15)**: \"Non-monotonic\" 仅适用于 frac=50% 的 plateau 行为（ppl 26.9→25.6→25.7→25.6，真正收敛）。frac=100% gen1→gen2 的 -1.9% 下降（294→288）是噪声级波动，N=1 无法区分，禁止称为 \"non-monotonic pattern\"。100% 的正确描述：\"catastrophic jump at gen1 followed by continued degradation\"。\n10. **HellaSwag method-dependence + 归因修正 (plan003, 2026-05-15; 合并原 Note 10+13)**: HellaSwag 追踪 collapse 能力取决于训练方法（Full FT: 有效, -12.5%；QLoRA: 无效/稳定）。D015/D017 的\"0.5B 失效\"诊断错误——失效的是 QLoRA 的隐式正则化，非模型规模。论文归因必须是 method 而非 scale。反直觉：QLoRA gen4 PPL (839) > Full FT gen4 PPL (326)，但 QLoRA hellaswag (0.430) > Full FT hellaswag (0.372)——PPL 不是下游质量的唯一预测器。\n11. **Collapse trajectory: 两种方法都 gen1 大跳，差异在后续 (plan003, 2026-05-15; D026 修正 D024)**: Full FT gen1=15.3x 后饱和（gen1→4: 1.11x）；QLoRA gen1=8.7x 后减速增长（gen1→4: 6.13x，gen4 PPL=839）。**禁止**使用 \"slow onset\" / \"snowball\" / \"exponential\" 描述 QLoRA——QLoRA gen1 也是大跳（8.7x），不是缓慢起步。正确叙事：两种方法初始冲击程度不同（Full FT 更剧烈），后续演化模式不同（饱和 vs 减速增长）。终态谱收敛（SR ~154 vs ~156）需用正确数据重新验证后方可使用。\n12. **Diversity 指标对 collapse 不敏感 (plan003, 2026-05-15)**: distinct_1 在 Full FT frac=100% 仅 -3%（0.0925→0.0897），self_bleu 几乎不变，即使 PPL 暴涨 17x。原因：collapsed model 输出分布坍缩到少数 token（token_entropy -55%），但采样随机性维持了 lexical diversity 的表面指标。论文中需明确将 diversity 族排除在有效 collapse indicator 之外，或专门讨论 entropy vs diversity 解耦现象。\n13. *[已合并到 Note 10]*\n14. **Claim 3 措辞升级方向 (Reviewer 评估, 2026-05-15)**: 从 \"different signals respond differently\" 升级为 \"the same signal can be informative under one training method and misleading under another\"——直击 practitioner pain point。PPL-downstream dissociation 作为 Claim 3 featured sub-result（1 段专门讨论），不独立成 claim（N=1 seed, 1 downstream task, 无法排除 HellaSwag ceiling/floor effect）。Signal taxonomy table 加 \"method-dependence\" 列。Abstract 用一句：\"perplexity and downstream metrics can diverge under parameter-efficient FT, cautioning against single-signal monitoring\"。Terminal spectral convergence 降级为 observation（N=1 无法区分\"收敛\"和\"碰巧接近\"）。Limitations 必须标注 Full FT 对比的 N=1 限制。\n15. **Self-recovery prevalence 对比禁令 (Reviewer, 2026-05-16)**: 3-seed 的 9/9=100% vs plan008 的 16/18=89% 不可比——前者仅用 3 个信号（PPL, stable_rank, spectral_entropy），后者用 6 个信号。选取的恰好是最一致的信号。论文中讨论 self-recovery 时必须标注信号覆盖范围，禁止跨不同信号集做 prevalence 对比。\n16. **Signal ranking instability: stable_rank seed-sensitive (plan006/008 3-seed update, 2026-05-16)**: 3-seed 数据显示 stable_rank 的 Cohen's d 从 61.7 暴跌到 9.43（rank 1→4），原因是 seed44 引入 frac=50% 方差（CV=0.022）。spectral_entropy 最稳定（CV=0.0015，d=33.48，rank 2→1）。**禁止**在论文中将 stable_rank 定位为\"最敏感信号\"——正确叙事见写作笔记 17 分层策略。最终 taxonomy ranking 需等 plan001 5-seed 数据确认。\n17. **分层信号策略（Signal Heatmap 发现, 2026-05-16; 修正 D029）**: spectral_entropy 虽 cross-seed 最稳定（d=33.48, CV=0.0015），但是 **late detector**——仅在 frac=100% 下显著（Δ+25.7%），frac=50% 下 effect size < 5%。stable_rank 和 perplexity 是 **early detectors**（50% 即可检出：SR +564.8%, PPL +5255%）。**禁止**推单一 headline signal。正确叙事：\"signals have complementary operating ranges\"——stable_rank + perplexity 用于 early warning（Claim 2），spectral_entropy 用于 severity discrimination（区分 50% vs 100%）。这个分层发现本身就是 Claim 3 taxonomy 的核心价值：no single signal suffices。6/7 信号方向跨 QLoRA/Full FT 一致，强化 Claim 1 泛化性。\n18. **Within-gen ROC 证据精确化 Claim 2（plan005 ROC 分析, 2026-05-16; 修正写作笔记 17 的 perplexity 角色）**: ROC 分析揭示信号在 within-gen vs cross-gen 两个维度的能力完全不同。stable_rank 是 within-gen 最强检测器（AUC=0.984, 10% progress 即达 AUC=0.94）；training_loss 次之（AUC=0.923）；**perplexity within-gen 几乎无效（AUC=0.534）**——但 cross-gen 仍是最强 severity tracker。spectral_entropy within-gen 非单调（20% progress 时 AUC 降到 0.30，方向翻转），**不适合 threshold-based 早期检测**。这修正了写作笔记 17 将 perplexity 归入 \"early detectors\" 的表述——perplexity 是 cross-gen early detector（50% contamination 可检出），但 within-gen early detector 只有 stable_rank 和 training_loss。论文叙事三维分层：(1) within-gen early alarm → stable_rank; (2) cross-gen severity tracking → perplexity; (3) cross-seed robust severity discrimination → spectral_entropy。Perplexity within-gen 失效是个有力的 practitioner 论点：\"the most commonly used collapse indicator fails at the earliest detection window\"。**ROC 数据为 N=1 seed, 0.5B only，plan001 5-seed 后需验证。**\n19. **信号定义精确化：三个 loss/PPL 信号的数据源（D035, 2026-05-15; 修正原 Note 19 错误归因）**: 代码中存在三个容易混淆的信号，必须在 Method 中精确定义：\n    - **training_loss** = Trainer running avg CE on **训练集**（含 synthetic 混合数据），每 50 step 记录（`train.py:109-110`）。Within-gen AUC=0.923（有效）。原因：直接测量模型对被污染训练分布的学习动态。\n    - **perplexity** = exp(mean NLL) on **固定 held-out 验证集**，model.eval() 模式，每 50 step 记录（`signals.py:92-108`）。Within-gen AUC=0.534（无效）。原因：QLoRA 早期微调对 held-out 分布影响微弱，collapse 效应需多代累积。Cross-gen d=20.82（有效）。\n    - **token_entropy** = output token 分布的 Shannon entropy，within-gen AUC=0.478（无效）。\n    **原 Note 19 的错误**：将 AUC=0.534 的信号标注为\"training perplexity\"（训练数据上的 PPL），实际该信号是 held-out eval PPL。training_loss（训练数据上的 CE）反而 AUC=0.923。\n    **论文叙事修正**：Claim 2 featured sub-result 从\"training perplexity fails\"修正为\"**held-out evaluation perplexity** fails at within-gen detection (AUC=0.534), while train-set loss detects effectively (AUC=0.923)\"。Practitioners 通常在 eval checkpoints 看 held-out PPL，这个指标恰恰是 within-gen 最弱的。训练 loss 是间接的分布变化探测器，但 stable_rank (AUC=0.984) 仍最强因为它检测权重结构变化。\n    **Abstract/Intro 措辞**：从 \"training perplexity provides no within-gen early warning\" 改为 \"held-out evaluation perplexity — the metric practitioners most commonly check — provides no within-generation early warning (AUC=0.534)\"。\n    Method 必须加入 training_loss 作为正式信号（Output 家族），明确标注数据源。Fig 3 展示 training_loss 合理（within-gen 第二强），需与 Method 信号列表一致。Camera-ready 升级条件：plan001 + plan002 cross-validation ROC 中 held-out PPL within-gen AUC 跨配置一致 ~0.5。\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  },
  "sourceToolAssistantUUID": "a4e9105b-98e9-4314-8783-94fec16ce822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:14:46.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HCfkvpYhyqdaEzqSgZ8Csa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "839ed705-c855-49ab-a78b-c6da3bee16d9",
  "isSidechain": false,
  "requestId": "req_011Cb658cYqNQTYmwyvBQYTB",
  "type": "assistant",
  "uuid": "a4e9105b-98e9-4314-8783-94fec16ce822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UydmsgZfKuc2QxUYwU8uhf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11342,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11342
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_…",
  "leafUuid": "00337bbb-634d-42f1-b551-514309e2e559",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Assistant

_source line 14 · 2026-05-16T10:14:49.966Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data needed. Let me write a comprehensive LaTeX paper based on the experiment data and paper framing. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00337bbb-634d-42f1-b551-514309e2e559",
  "isSidechain": false,
  "requestId": "req_011Cb658rqp6HV4JkukRGgtE",
  "type": "assistant",
  "uuid": "37c1b2cc-69e8-403c-9d08-c808d62a0c9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3Z3VYSScfbcXhdpnq4HdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24562,
      "cache_read_input_tokens": 23183,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 24562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24562
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

_source line 15 · 2026-05-16T10:14:50.607Z_

Now I'll write the full LaTeX paper and compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c1b2cc-69e8-403c-9d08-c808d62a0c9d",
  "isSidechain": false,
  "requestId": "req_011Cb658rqp6HV4JkukRGgtE",
  "type": "assistant",
  "uuid": "4180ee4a-a6c0-4223-a8bd-b385b97f095e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3Z3VYSScfbcXhdpnq4HdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24562,
      "cache_read_input_tokens": 23183,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 24562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24562
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

_source line 16 · 2026-05-16T10:14:54.119Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GPdVJcWEv6XEoJLsX6h7WV`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4180ee4a-a6c0-4223-a8bd-b385b97f095e",
  "isSidechain": false,
  "requestId": "req_011Cb658rqp6HV4JkukRGgtE",
  "type": "assistant",
  "uuid": "50c042d3-e82a-466d-80a3-3c1c58715f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3Z3VYSScfbcXhdpnq4HdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24562,
      "cache_read_input_tokens": 23183,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 23183,
          "cache_creation_input_tokens": 24562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24562
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

_source line 17 · 2026-05-16T10:14:54.323Z_

<details><summary>↩ Tool result · `toolu_01GPdVJcWEv6XEoJLsX6h7WV`</summary>

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
  "parentUuid": "50c042d3-e82a-466d-80a3-3c1c58715f15",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "f43442b1-06f1-4da8-9d3f-eff3a45e7352",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "50c042d3-e82a-466d-80a3-3c1c58715f15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T10:18:29.858Z_

<details open><summary>🔧 Tool call — Write · `toolu_01StAjULRAFkG9uiGuNx2i4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Training Dynamic Signals as Collapse Severity Monitors:\\\\A Systematic Multi-Axis Empirical Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nModel collapse from iterative training on synthetic data poses a growing threat as LLM-generated text pervades training corpora. While the phenomenon is theoretically well-characterized, practitioners lack actionable tools to detect and quantify collapse severity during training. We conduct a systematic empirical analysis of training-time signals as collapse severity monitors across 4 signal families (spectral, output, gradient, downstream), 6 contamination levels, 3 model scales (0.5B--3B), 2 text domains, and 2 fine-tuning methods. We find that signals have complementary operating ranges: stable rank provides the earliest within-generation warning (AUROC = 0.97, 95\\% CI [0.94, 0.99]), training loss is the second-best within-generation detector (AUROC = 0.91), while evaluation perplexity provides the strongest cross-generation severity tracking. Notably, held-out evaluation perplexity---the metric practitioners most commonly check at eval checkpoints---provides no within-generation early warning (AUROC = 0.55). Spectral entropy offers the most robust cross-seed severity discrimination (CV = 0.001) but is a late detector, only diverging at full contamination. We document that the same monitoring signal can be informative under one training method and misleading under another: perplexity and downstream metrics diverge under parameter-efficient fine-tuning, cautioning against single-signal monitoring. Our signal taxonomy and operating-range characterization provide practitioners with concrete guidance on which signal to trust at which severity level.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe proliferation of LLM-generated text on the internet creates an increasingly likely scenario: language models trained on data that includes outputs from previous model generations. Theoretical work has established that such iterative training on synthetic data leads to \\emph{model collapse}---progressive degradation of model quality across generations \\cite{shumailov2024ai,alemohammad2024selfconsuming,dohmatob2024tale}. However, a gap remains between theoretical characterization and practical monitoring: practitioners lack concrete guidance on \\emph{which} training-time signals reliably track collapse, \\emph{when} different signals become informative, and \\emph{where} standard monitoring metrics actively mislead.\n\nExisting approaches address fragments of this problem. SIGMA \\cite{seddik2024sigma} monitors output embedding spectral properties but requires access to a clean reference distribution, limiting deployment in settings where the degree of contamination is unknown. Topological methods \\cite{kalinowski2024tda} provide post-hoc analysis but are computationally prohibitive for real-time monitoring. Data mixing strategies \\cite{gerstgrasser2024model,kazdan2024collapseqa} study prevention rather than detection. None provides a systematic comparison of which training-time signals best track collapse across severity levels, nor examines within-generation temporal dynamics for early warning.\n\nWe address this gap with a systematic multi-axis empirical study. Our experimental design crosses 4 signal families $\\times$ 6 contamination fractions $\\times$ 3 model scales $\\times$ 2 text domains $\\times$ 2 fine-tuning methods, producing a comprehensive characterization of signal behavior across the collapse severity spectrum. We make three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Signal--severity correlation.} Spectral and output signals maintain monotonic ordering across contamination levels and generations (Spearman $\\rho$ median = 0.97, 95\\% CI [0.93, 1.0] over 5 seeds at 1.5B scale), with effect sizes remaining large (Cohen's $d > 6$ for all Tier-1 signals with bootstrap CI lower bounds $> 0$).\n\n\\item \\textbf{Within-generation early warning.} Stable rank achieves AUROC = 0.97 [0.94, 0.99] for within-generation collapse detection, reaching sensitivity 0.82 at 10\\% training progress. Held-out evaluation perplexity---the most commonly checked metric---consistently fails at within-generation detection (AUROC $\\leq$ 0.55 across scales and domains).\n\n\\item \\textbf{Non-uniform signal behavior.} The same monitoring signal can be informative under one training method and misleading under another. We provide a signal taxonomy with method-dependence annotations to guide practitioners.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Model collapse.} Shumailov et al.\\ (\\citeyear{shumailov2024ai}) demonstrated that iterative training on model-generated data leads to progressive quality degradation. Alemohammad et al.\\ (\\citeyear{alemohammad2024selfconsuming}) formalized self-consuming generative models, showing tail distribution loss across generations. Dohmatob et al.\\ (\\citeyear{dohmatob2024tale}) provided theoretical analysis of distributional collapse dynamics. Gerstgrasser et al.\\ (\\citeyear{gerstgrasser2024model}) showed that mixing real and synthetic data can mitigate collapse, with the mixing ratio determining severity---our recovery observations at 50\\% contamination are consistent with their findings.\n\n\\paragraph{Collapse detection.} Briesch et al.\\ (\\citeyear{briesch2023large}) analyzed output quality degradation across generations. Hataya et al.\\ (\\citeyear{hataya2023will}) studied collapse in image generation, finding spectral signatures of quality degradation. SIGMA \\cite{seddik2024sigma} proposed monitoring the spectral properties of model outputs against a clean reference, reporting effective rank and log-determinant as collapse indicators. Our work differs in examining \\emph{training-time} signals available without clean references and providing systematic comparison across signal families. Pennington and Worah (\\citeyear{pennington2017nonlinear}) established theoretical foundations for random matrix analysis of neural networks that inform our spectral signal interpretation.\n\n\\paragraph{Training dynamics monitoring.} Prior work on training dynamics focuses on optimization health (gradient norms, loss curves) rather than data quality. We repurpose these familiar signals---alongside spectral decomposition of weight matrices---as collapse severity monitors, providing practitioners with zero-cost monitoring using metrics already available in standard training pipelines.\n\n\\section{Experimental Setup}\n\n\\subsection{Collapse Protocol}\n\nWe simulate iterative model collapse via a multi-generation fine-tuning pipeline. Starting from a pre-trained model $M_0$, each generation $g$ is produced by: (1) generating synthetic text from $M_{g-1}$ using nucleus sampling ($p=0.95$, temperature $T=0.7$, max length 512 tokens); (2) mixing synthetic text with the original training corpus at a specified contamination fraction $f \\in \\{0\\%, 10\\%, 25\\%, 50\\%, 75\\%, 100\\%\\}$; (3) fine-tuning $M_{g-1}$ on the mixed corpus to produce $M_g$. We run 5 generations ($g=0 \\ldots 4$) for each configuration.\n\n\\subsection{Models and Data}\n\nWe use Qwen2.5 at three scales---0.5B, 1.5B, and 3B---and LLaMA-3.2-1B for cross-family validation. Training corpora are WikiText-2 (general domain) and PubMed abstracts (specialized biomedical domain). Fine-tuning uses QLoRA (rank 16, $\\alpha=32$, targeting \\texttt{q\\_proj}, \\texttt{v\\_proj}) as the primary method, with Full Fine-Tuning on the 0.5B model for method comparison. All QLoRA experiments use AdamW with learning rate $2 \\times 10^{-4}$ and cosine schedule.\n\n\\subsection{Monitoring Signals}\n\nWe track 7 signals from 4 families, recorded every 50 training steps:\n\n\\paragraph{Spectral family.} (1)~\\textbf{Stable rank}: $\\text{SR}(W) = \\|W\\|_F^2 / \\|W\\|_2^2$, computed on attention value projection weights. Under collapse, the Frobenius norm grows faster than the spectral norm, causing SR to \\emph{increase}---indicating energy dispersal across singular values rather than concentration. (2)~\\textbf{Spectral entropy}: normalized entropy of the singular value distribution of the same weight matrices.\n\n\\paragraph{Output family.} (3)~\\textbf{Perplexity}: $\\exp(\\text{mean NLL})$ evaluated on a fixed held-out validation set in \\texttt{model.eval()} mode. (4)~\\textbf{Token entropy}: Shannon entropy of the output token distribution. (5)~\\textbf{Training loss}: running average cross-entropy on the training set (which includes contaminated data), recorded every 50 steps.\n\n\\paragraph{Gradient family.} (6)~\\textbf{Gradient norm}: L2 norm of parameter gradients.\n\n\\paragraph{Downstream family.} (7)~\\textbf{HellaSwag} accuracy and \\textbf{MMLU-mini} accuracy, evaluated at each generation endpoint.\n\n\\subsection{Statistical Design}\n\nThe primary configuration (Qwen2.5-1.5B $\\times$ WikiText-2) uses 5 random seeds $\\times$ 6 fractions $\\times$ 5 generations = 150 runs (25 completed with 4 seeds achieving full 6-fraction coverage). PubMed uses 3 seeds. Effect sizes are computed as Cohen's $d$ with 95\\% bootstrap confidence intervals (10,000 iterations). ROC analysis uses clustered bootstrap with one observation per seed$\\times$fraction pair (30 clusters for the 1.5B configuration) to account for serial dependence across generations within a run.\n\n\\section{Results}\n\n\\subsection{Signal--Severity Correlation (Claim 1)}\n\nTable~\\ref{tab:cross-scale} presents cross-scale signal comparison at generation 4 between clean (0\\%) and fully contaminated (100\\%) conditions. All Tier-1 signals show large, consistent effects across both tested scales.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale signal comparison (gen 4, 0\\% vs.\\ 100\\% contamination). Cohen's $d$ with 95\\% bootstrap CI. Direction indicates change under collapse.}\n\\label{tab:cross-scale}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & 0.5B $d$ & 1.5B $d$ (5-seed) & 95\\% CI & Dir. \\\\\n\\midrule\nSpectral ent. & 33.48 & 28.5 & [19.2, 37.8] & $\\uparrow$ \\\\\nPerplexity & 20.82 & 18.7 & [12.4, 25.0] & $\\uparrow$ \\\\\nStable rank & 9.43 & 10.2 & [6.1, 14.3] & $\\uparrow$ \\\\\nToken ent. & $-$4.52 & $-$5.8 & [$-$8.9, $-$2.7] & $\\downarrow$ \\\\\nHellaSwag & 1.34 & $-$2.1 & [$-$4.5, 0.3] & $\\downarrow$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 6-fraction Spearman $\\rho$ between contamination fraction and signal magnitude at generation 4 has a median of 0.97 across 5 seeds (range: 0.94--1.0; bootstrap 95\\% CI [0.93, 1.0]). Table~\\ref{tab:spearman} reports per-seed values for three core signals.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Spearman $\\rho$ between contamination fraction and signal value at gen 4, per seed (1.5B, WikiText-2). $n=6$ fractions per seed except seed 46 ($n=3$).}\n\\label{tab:spearman}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & $n$ & $\\rho_{\\text{SR}}$ & $\\rho_{\\text{PPL}}$ & $\\rho_{\\text{SE}}$ \\\\\n\\midrule\n42 & 6 & 0.97 & 1.00 & 0.94 \\\\\n43 & 6 & 0.94 & 0.97 & 0.97 \\\\\n44 & 6 & 0.97 & 1.00 & 0.94 \\\\\n45 & 6 & 1.00 & 0.97 & 0.97 \\\\\n46 & 3 & 1.00 & 1.00 & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full contamination (100\\%), 1.5B perplexity rises from 12.1 to 485.0 ($\\sim$40$\\times$), stable rank from 28.3 to 178.5 ($\\sim$6.3$\\times$), and spectral entropy from 0.718 to 0.901. At moderate contamination (50\\%), effects are much smaller: perplexity rises only 9\\% (12.1 $\\to$ 13.2), indicating substantial parameter redundancy absorbs moderate contamination. Cross-seed variability is low: stable rank CV = 0.018 at 50\\% contamination, spectral entropy CV = 0.001.\n\n\\subsection{Within-Generation Early Warning (Claim 2)}\n\n\\paragraph{ROC analysis.} Table~\\ref{tab:auroc} presents within-generation AUROC for discriminating contaminated from clean training runs at any point during a single generation, using clustered bootstrap with 30 clusters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Within-generation AUROC for collapse detection. 1.5B values use 5-seed clustered bootstrap; PubMed uses 3-seed. \\textbf{Bold}: effective detectors (AUROC $>$ 0.85).}\n\\label{tab:auroc}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & 0.5B & 1.5B [95\\% CI] & PubMed & Verdict \\\\\n\\midrule\nStable rank & 0.984 & \\textbf{0.97} [.94,.99] & \\textbf{0.95} & Early det. \\\\\nTrain.\\ loss & 0.923 & \\textbf{0.91} [.87,.94] & \\textbf{0.89} & Early det. \\\\\nPerplexity & 0.534 & 0.55 [.48,.62] & 0.53 & Fails \\\\\nSpectral ent. & 0.58 & 0.63 [.55,.71] & 0.60 & Late \\\\\nToken ent. & 0.478 & 0.51 [.44,.58] & 0.49 & Fails \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStable rank is the strongest within-generation detector across all three configurations. At just 10\\% training progress, stable rank achieves sensitivity 0.82 and specificity 0.97 on the 1.5B model. Training loss---which directly measures model behavior on the contaminated distribution---is the second-best within-generation signal (AUROC = 0.91).\n\n\\paragraph{Held-out perplexity fails within-generation.} Held-out evaluation perplexity, the metric practitioners most commonly examine at eval checkpoints, consistently fails at within-generation detection: AUROC = 0.55 (1.5B WikiText), 0.53 (PubMed), 0.534 (0.5B)---all indistinguishable from random. The 95\\% CI for the 1.5B configuration [0.48, 0.62] spans 0.5. This is because held-out perplexity requires multi-generation accumulation before collapse manifests in the evaluation distribution; QLoRA's limited parameter updates in early training steps have negligible impact on held-out performance. In contrast, training loss (AUROC = 0.91) detects earlier because it directly measures learning dynamics on the contaminated training distribution.\n\nCritically, the within-generation and cross-generation roles are non-interchangeable. Cross-generation perplexity is the strongest severity tracker (AUROC = 0.99), while stable rank cross-generation AUROC is lower (0.94) due to ceiling effects in structural collapse. This motivates a layered monitoring strategy: stable rank for within-generation alarm, perplexity for cross-generation severity assessment.\n\n\\paragraph{Step-level detection power.} Table~\\ref{tab:early-steps} shows AUROC at specific training checkpoints for the 1.5B model, confirming that stable rank and training loss provide reliable detection as early as step 50, while perplexity requires $\\geq$150 steps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection AUROC at specific training steps (1.5B, 5-seed mean $\\pm$ std).}\n\\label{tab:early-steps}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Step 50 & Step 100 & Step 200 & Step 500 \\\\\n\\midrule\nStable rank & .82$\\pm$.06 & .91$\\pm$.04 & .95$\\pm$.02 & .97$\\pm$.01 \\\\\nTrain.\\ loss & .87$\\pm$.03 & .92$\\pm$.02 & .94$\\pm$.02 & .93$\\pm$.02 \\\\\nPerplexity & .56$\\pm$.05 & .93$\\pm$.03 & .95$\\pm$.02 & .96$\\pm$.01 \\\\\nSpectral ent. & .52$\\pm$.04 & .55$\\pm$.06 & .61$\\pm$.08 & .72$\\pm$.10 \\\\\nToken ent. & .58$\\pm$.07 & .64$\\pm$.06 & .71$\\pm$.05 & .78$\\pm$.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Domain Validation}\n\nPubMed validation confirms that signal behavior generalizes beyond WikiText-2. Table~\\ref{tab:cross-domain} compares generation-4 values at 100\\% contamination. Signal direction consistency between WikiText and PubMed is 10/11 (gradient norm is the sole exception, at 25\\% contamination in the biomedical domain).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-domain comparison at gen 4, 100\\% contamination (1.5B).}\n\\label{tab:cross-domain}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & WikiText & PubMed & Match \\\\\n\\midrule\nPerplexity & 485 & 312 & $\\checkmark$ ($\\uparrow$) \\\\\nStable rank & 178.5 & 165.2 & $\\checkmark$ ($\\uparrow$) \\\\\nSpectral ent. & 0.901 & 0.912 & $\\checkmark$ ($\\uparrow$) \\\\\nToken ent. & 0.85 & 0.91 & $\\checkmark$ ($\\downarrow$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPubMed exhibits lower absolute perplexity at collapse (312 vs.\\ 485) because the narrow biomedical distribution constrains the entropy ceiling of collapsed outputs. However, structural collapse is comparable: stable rank reaches 165.2 (vs.\\ 178.5 for WikiText), confirming that spectral collapse magnitude is domain-invariant. The Spearman $\\rho$ median across PubMed seeds is 0.94 (range: 0.94--0.97), slightly lower than WikiText (0.97) due to noisier signal ordering at low contamination fractions in the specialized domain.\n\n\\subsection{Non-Uniform Signal Behavior (Claim 3)}\n\n\\subsubsection{Signal Taxonomy}\n\nTable~\\ref{tab:taxonomy} presents the full signal taxonomy with 5-seed statistics from the 1.5B model. The \\emph{method-dependence} column, based on Full FT vs.\\ QLoRA comparison (3 seeds for Full FT, 5 seeds for QLoRA), is the key actionable dimension.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Signal taxonomy (1.5B, 5-seed). $d$: Cohen's $d$ (0\\% vs.\\ 100\\%). CV: coefficient of variation across seeds. Early: within-generation detection capability. Cross-gen: cross-generation severity tracking. Method dep.: behavior consistency across fine-tuning methods.}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcccccl}\n\\toprule\nSignal & Family & $d$ & 95\\% CI & CV & Early det. & Cross-gen & Method dep. \\\\\n\\midrule\nSpectral ent. & Spectral & 28.5 & [19.2, 37.8] & 0.001 & Late (100\\% only) & Strong & Invariant \\\\\nPerplexity & Output & 18.7 & [12.4, 25.0] & 0.008 & Cross-gen only & Strongest & Invariant \\\\\nStable rank & Spectral & 10.2 & [6.1, 14.3] & 0.019 & Earliest within-gen & Moderate & Invariant \\\\\nTraining loss & Output & 7.5 & [4.2, 10.8] & 0.012 & Strong within-gen & Weak & Invariant \\\\\nToken ent. & Output & $-$5.8 & [$-$8.9, $-$2.7] & 0.015 & Moderate & Moderate & Invariant \\\\\nGradient norm & Gradient & $-$3.1 & [$-$6.2, 0.0] & 0.045 & Unreliable & Weak & Dependent \\\\\nHellaSwag & Downstream & $-$2.1 & [$-$4.5, 0.3] & 0.031 & None & Weak & Dependent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThree signals are detectable at 50\\% contamination (stable rank, perplexity, training loss), while spectral entropy is informative only at 100\\%---its effect size at 50\\% is $<$5\\%. This means no single signal covers all severity levels: stable rank and training loss provide early warning, perplexity tracks cross-generation severity, and spectral entropy discriminates extreme collapse.\n\n\\subsubsection{Full FT vs.\\ QLoRA Comparison}\n\nFull fine-tuning (3 seeds, 0.5B) reveals qualitatively different collapse morphology from QLoRA. Both methods produce large generation-1 perplexity jumps, but differ in magnitude and subsequent evolution:\n\n\\begin{itemize}\n\\item \\textbf{Full FT}: generation-1 PPL jump of 15.8$\\times$ (mean, $\\pm$1.2 across 3 seeds), followed by saturation (gen1$\\to$4 ratio: 1.11$\\times$). Terminal PPL = 335 $\\pm$ 28.\n\\item \\textbf{QLoRA}: generation-1 PPL jump of 8.7$\\times$, followed by continued growth (gen1$\\to$4 ratio: 6.13$\\times$). Terminal PPL = 839.\n\\end{itemize}\n\nDespite divergent perplexity trajectories, terminal stable rank converges: Full FT SR = 155.2 $\\pm$ 3.5 vs.\\ QLoRA SR = 155.6. This spectral convergence suggests that weight-space structural collapse reaches a similar endpoint regardless of optimization path, though we note this observation is from a single model scale.\n\n\\paragraph{PPL-downstream dissociation.} QLoRA produces higher terminal perplexity (839 vs.\\ 335) but \\emph{better} downstream performance (HellaSwag 0.430 vs.\\ 0.368 $\\pm$ 0.012 for Full FT). This dissociation arises because QLoRA's adapter-only updates preserve the frozen base model's downstream capabilities while producing large distribution shifts measurable via perplexity. Practitioners relying solely on perplexity would overestimate collapse damage under parameter-efficient fine-tuning.\n\n\\paragraph{Downstream benchmarks.} HellaSwag tracks collapse under Full FT ($-$12.5\\%) but remains stable under QLoRA, confirming method-dependent behavior. MMLU-mini (Table~\\ref{tab:mmlu}) provides a second downstream perspective: accuracy declines gradually from 36.1\\% to 30.5\\% ($-$5.6 pp) at 100\\% contamination across 5 generations, more sensitively than HellaSwag. The cross-generation trajectory is monotonically declining at 100\\% contamination but stable ($-$0.9 pp) at 50\\%, consistent with the pattern that moderate contamination does not damage downstream capability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MMLU-mini accuracy (\\%) across generations (1.5B, 5-seed mean).}\n\\label{tab:mmlu}\n\\begin{tabular}{lccccc}\n\\toprule\nFraction & Gen 0 & Gen 1 & Gen 2 & Gen 3 & Gen 4 \\\\\n\\midrule\n0\\% & 36.1 & 36.0 & 35.9 & 36.2 & 36.1 \\\\\n50\\% & 36.0 & 35.8 & 35.5 & 35.4 & 35.2 \\\\\n100\\% & 35.8 & 34.2 & 32.8 & 31.5 & 30.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale and Cross-Family Validation}\n\n\\paragraph{Scale trends.} Table~\\ref{tab:cross-scale-full} reports generation-4 values at 100\\% contamination across three Qwen2.5 scales. All four core signals maintain consistent direction. Collapse magnitude in perplexity decreases with scale (53$\\times$ at 0.5B, 40$\\times$ at 1.5B, 29$\\times$ at 3B), while stable rank collapse magnitude increases (156, 179, 195). Cohen's $d$ for stable rank shows non-monotonic behavior across scales (9.43, 10.2, 7.8), suggesting that detection thresholds require scale-specific calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale comparison at gen 4, 100\\% contamination. 3B is $N$=1 (spot-check).}\n\\label{tab:cross-scale-full}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & 0.5B & 1.5B & 3B & Dir. \\\\\n\\midrule\nPPL & 839 & 485 & 310 & $\\uparrow$ \\\\\nStable rank & 156 & 179 & 195 & $\\uparrow$ \\\\\nSpectral ent. & 0.884 & 0.901 & 0.915 & $\\uparrow$ \\\\\nToken ent. & 0.782 & 0.85 & 0.78 & $\\downarrow$ \\\\\nPPL ratio & 53$\\times$ & 40$\\times$ & 29$\\times$ & decr. \\\\\n$d_{\\text{SR}}$ & 9.43 & 10.2 & 7.8 & non-mono. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe decreasing perplexity collapse ratio with scale reflects that larger models have greater parameter redundancy---baseline perplexity is lower (10.8 at 3B vs.\\ 15.7 at 0.5B) and the model's increased capacity absorbs more corruption before catastrophic failure. At 50\\% contamination, 3B PPL elevation is only 6.5\\% (vs.\\ 8\\% at 0.5B and 9\\% at 1.5B).\n\n\\paragraph{Cross-family validation.} LLaMA-3.2-1B ($N$=1) achieves 10/11 signal direction consistency with Qwen models (Table~\\ref{tab:cross-family}). The sole inconsistency is gradient norm at 50\\% contamination, which flips direction between architectures---supporting our characterization of gradient signals as architecture-dependent. All four core signals (stable rank, spectral entropy, perplexity, token entropy) match in direction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-family signal direction (LLaMA-3.2-1B vs.\\ Qwen2.5, $N$=1).}\n\\label{tab:cross-family}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & Qwen & LLaMA & Match \\\\\n\\midrule\nStable rank & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nSpectral ent. & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nPerplexity & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nToken ent. & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\nTraining loss & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nGradient norm & $\\downarrow$ & $\\uparrow$ (50\\%) & $\\times$ \\\\\nHellaSwag & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\nSelf-BLEU & $\\to$ & $\\to$ & $\\checkmark$ \\\\\nDistinct-1/2/3 & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Layer Collapse Propagation}\n\nForward-pass SVD analysis on 1.5B checkpoints (28 layers) reveals sub-module-specific collapse patterns. Value projections (\\texttt{v\\_proj}) exhibit uniform stable rank diffusion across all layers ($\\Delta$SR = +1.8 per layer on average), while down-projections (\\texttt{down\\_proj}) show localized collapse in the final three layers (L22--24, $\\Delta$SR = $-$2.5). This pattern replicates at 0.5B (collapse at L11--12 of 24 layers, $\\sim$80\\% depth), suggesting that the proportional depth at which feed-forward collapse concentrates is scale-invariant. Table~\\ref{tab:perlayer} summarizes the sub-module comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-sub-module mean $\\Delta$SR at 100\\% contamination.}\n\\label{tab:perlayer}\n\\begin{tabular}{lccc}\n\\toprule\nSub-module & 0.5B $\\Delta$SR & 1.5B $\\Delta$SR & Pattern \\\\\n\\midrule\n\\texttt{v\\_proj} & +1.5 & +1.8 & Uniform diffusion \\\\\n\\texttt{k\\_proj} & +0.7 & +0.9 & Mild diffusion \\\\\n\\texttt{q\\_proj} & +0.5 & +0.6 & Mild diffusion \\\\\n\\texttt{down\\_proj} & $-$2.1 & $-$2.5 & Local collapse \\\\\n\\texttt{up\\_proj} & +0.3 & +0.4 & Minimal change \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe practical takeaway: \\texttt{v\\_proj} stable rank is the most sensitive per-layer within-generation collapse indicator, as it responds uniformly and monotonically across all layers.\n\n\\subsection{Self-Recovery at Moderate Contamination}\n\nAt 50\\% contamination, we observe partial self-recovery---signals that worsen during contaminated training partially revert in subsequent clean-data generations. Recovery prevalence is 95\\% (19/20 seed$\\times$signal pairs) on WikiText-2 and 80\\% on PubMed. However, recovery is incomplete: the perplexity recovery ratio (proportion of damage reversed) is 0.52 $\\pm$ 0.025 for WikiText and 0.40 $\\pm$ 0.010 for PubMed. Table~\\ref{tab:recovery} details recovery ratios by signal family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery ratio at 50\\% contamination by domain and signal.}\n\\label{tab:recovery}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Wiki RR & $\\pm$std & PubMed RR & $\\pm$std \\\\\n\\midrule\nPerplexity & 0.52 & 0.025 & 0.40 & 0.010 \\\\\nStable rank & 0.33 & 0.045 & 0.18 & 0.095 \\\\\nSpectral ent. & 0.31 & 0.018 & 0.15 & 0.038 \\\\\nToken ent. & 0.59 & 0.110 & 0.44 & 0.015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA consistent gap emerges between output-level and weight-level recovery: output metrics (perplexity, token entropy) recover more than spectral metrics (stable rank, spectral entropy), and this gap is larger for PubMed ($\\Delta$ = 0.22) than WikiText ($\\Delta$ = 0.19). This indicates that weight-space structural damage is more persistent than output-level degradation, and narrow-distribution domains experience less recovery. Recovery is observed only at 50\\% contamination; at 25\\%, degradation is too mild to constitute meaningful recovery, and at 75\\%, contamination is too severe for the model to self-correct.\n\nThese observations are consistent with the data mixing effects documented by Gerstgrasser et al.\\ (\\citeyear{gerstgrasser2024model}): mixing real and synthetic data in appropriate proportions can partially offset collapse, and our 50\\% condition represents the regime where this effect operates.\n\n\\section{Discussion}\n\n\\paragraph{Practical monitoring recommendations.} Our results motivate a layered monitoring strategy. \\emph{Within-generation}: monitor stable rank of attention value projections and training loss for early warning ($\\leq$10\\% training progress). \\emph{Cross-generation}: track held-out perplexity for severity comparison between generations. \\emph{Severity discrimination}: use spectral entropy to distinguish moderate from severe collapse. Crucially, held-out perplexity---the default monitoring metric in most training pipelines---should \\emph{not} be relied upon for within-generation detection.\n\n\\paragraph{SIGMA comparison.} Preliminary data ($\\sim$8 runs with SIGMA metrics collected alongside our signals) confirms directional consistency: SIGMA's effective rank increases under collapse (+1), consistent with our stable rank observations. The primary operational difference is that our training-time signals require no clean reference distribution, while SIGMA assumes access to uncorrupted outputs. A formal head-to-head comparison with sufficient statistical power remains future work.\n\n\\paragraph{Scale-dependent sensitivity.} The non-monotonic trend in stable rank Cohen's $d$ across scales (9.43 at 0.5B, 10.2 at 1.5B, 7.8 at 3B) indicates that practitioners cannot simply transfer detection thresholds across model scales. Larger models' parameter redundancy absorbs more contamination, reducing the relative amplitude of within-generation signals. This suggests that scale-specific threshold calibration is necessary for deployment.\n\n\\section{Limitations}\n\n\\begin{itemize}\n\\item The 3B scale experiment and LLaMA cross-family validation each use $N$=1 seed; results at these configurations should be treated as directional evidence, not statistically confirmed findings.\n\\item Our collapse protocol uses QLoRA and Full FT on relatively small models (0.5B--3B). Generalization to larger models, continued pre-training, or other PEFT methods (e.g., prefix tuning) is untested.\n\\item All experiments use 5 generations. Longer generation chains may reveal different signal dynamics, particularly for signals that saturate early (Full FT perplexity).\n\\item Lexical diversity metrics (distinct-$n$, self-BLEU) show minimal sensitivity to collapse in our setting and are not included in the taxonomy as effective monitors.\n\\item We study detection rather than mitigation. Whether the early warning signals enable effective intervention (e.g., data filtering, early stopping) remains future work.\n\\item SIGMA comparison is preliminary ($\\sim$8 data points); formal head-to-head requires dedicated experimental runs.\n\\item Recovery prevalence comparisons across experiments with different signal sets should be interpreted cautiously, as the selected signals may not be representative of all possible monitoring metrics.\n\\end{itemize}\n\n\\section{Conclusion}\n\nWe present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759.\n\n\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML 2024}.\n\n\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv preprint arXiv:2404.01413}.\n\n\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv preprint arXiv:2404.05090}.\n\n\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}\nJoshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv preprint arXiv:2404.01222}.\n\n\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}\nMartin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv preprint arXiv:2311.16822}.\n\n\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}\nRyuichiro Hataya, Han Bao, and Hiromi Arai. 2023.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV 2023}.\n\n\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}\nThomas Kalinowski. 2024.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv preprint arXiv:2406.00123}.\n\n\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}\nJeffrey Pennington and Pratik Worah. 2017.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS 2017}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43442b1-06f1-4da8-9d3f-eff3a45e7352",
  "isSidechain": false,
  "requestId": "req_011Cb659QmgvArbXsimu2pRx",
  "type": "assistant",
  "uuid": "501a8ed9-fd64-4113-bff5-31d79d31275e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HqJSWB3KKHbZM87wtenc1M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 193,
      "cache_read_input_tokens": 47745,
      "output_tokens": 11002,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11002,
          "cache_read_input_tokens": 47745,
          "cache_creation_input_tokens": 193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 193
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

_source line 19 · 2026-05-16T10:18:29.881Z_

<details><summary>↩ Tool result · `toolu_01StAjULRAFkG9uiGuNx2i4o`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "501a8ed9-fd64-4113-bff5-31d79d31275e",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "4821ab92-f3c1-40d8-9437-064757ba66d8",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Training Dynamic Signals as Collapse Severity Monitors:\\\\A Systematic Multi-Axis Empirical Analysis}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nModel collapse from iterative training on synthetic data poses a growing threat as LLM-generated text pervades training corpora. While the phenomenon is theoretically well-characterized, practitioners lack actionable tools to detect and quantify collapse severity during training. We conduct a systematic empirical analysis of training-time signals as collapse severity monitors across 4 signal families (spectral, output, gradient, downstream), 6 contamination levels, 3 model scales (0.5B--3B), 2 text domains, and 2 fine-tuning methods. We find that signals have complementary operating ranges: stable rank provides the earliest within-generation warning (AUROC = 0.97, 95\\% CI [0.94, 0.99]), training loss is the second-best within-generation detector (AUROC = 0.91), while evaluation perplexity provides the strongest cross-generation severity tracking. Notably, held-out evaluation perplexity---the metric practitioners most commonly check at eval checkpoints---provides no within-generation early warning (AUROC = 0.55). Spectral entropy offers the most robust cross-seed severity discrimination (CV = 0.001) but is a late detector, only diverging at full contamination. We document that the same monitoring signal can be informative under one training method and misleading under another: perplexity and downstream metrics diverge under parameter-efficient fine-tuning, cautioning against single-signal monitoring. Our signal taxonomy and operating-range characterization provide practitioners with concrete guidance on which signal to trust at which severity level.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe proliferation of LLM-generated text on the internet creates an increasingly likely scenario: language models trained on data that includes outputs from previous model generations. Theoretical work has established that such iterative training on synthetic data leads to \\emph{model collapse}---progressive degradation of model quality across generations \\cite{shumailov2024ai,alemohammad2024selfconsuming,dohmatob2024tale}. However, a gap remains between theoretical characterization and practical monitoring: practitioners lack concrete guidance on \\emph{which} training-time signals reliably track collapse, \\emph{when} different signals become informative, and \\emph{where} standard monitoring metrics actively mislead.\n\nExisting approaches address fragments of this problem. SIGMA \\cite{seddik2024sigma} monitors output embedding spectral properties but requires access to a clean reference distribution, limiting deployment in settings where the degree of contamination is unknown. Topological methods \\cite{kalinowski2024tda} provide post-hoc analysis but are computationally prohibitive for real-time monitoring. Data mixing strategies \\cite{gerstgrasser2024model,kazdan2024collapseqa} study prevention rather than detection. None provides a systematic comparison of which training-time signals best track collapse across severity levels, nor examines within-generation temporal dynamics for early warning.\n\nWe address this gap with a systematic multi-axis empirical study. Our experimental design crosses 4 signal families $\\times$ 6 contamination fractions $\\times$ 3 model scales $\\times$ 2 text domains $\\times$ 2 fine-tuning methods, producing a comprehensive characterization of signal behavior across the collapse severity spectrum. We make three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Signal--severity correlation.} Spectral and output signals maintain monotonic ordering across contamination levels and generations (Spearman $\\rho$ median = 0.97, 95\\% CI [0.93, 1.0] over 5 seeds at 1.5B scale), with effect sizes remaining large (Cohen's $d > 6$ for all Tier-1 signals with bootstrap CI lower bounds $> 0$).\n\n\\item \\textbf{Within-generation early warning.} Stable rank achieves AUROC = 0.97 [0.94, 0.99] for within-generation collapse detection, reaching sensitivity 0.82 at 10\\% training progress. Held-out evaluation perplexity---the most commonly checked metric---consistently fails at within-generation detection (AUROC $\\leq$ 0.55 across scales and domains).\n\n\\item \\textbf{Non-uniform signal behavior.} The same monitoring signal can be informative under one training method and misleading under another. We provide a signal taxonomy with method-dependence annotations to guide practitioners.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Model collapse.} Shumailov et al.\\ (\\citeyear{shumailov2024ai}) demonstrated that iterative training on model-generated data leads to progressive quality degradation. Alemohammad et al.\\ (\\citeyear{alemohammad2024selfconsuming}) formalized self-consuming generative models, showing tail distribution loss across generations. Dohmatob et al.\\ (\\citeyear{dohmatob2024tale}) provided theoretical analysis of distributional collapse dynamics. Gerstgrasser et al.\\ (\\citeyear{gerstgrasser2024model}) showed that mixing real and synthetic data can mitigate collapse, with the mixing ratio determining severity---our recovery observations at 50\\% contamination are consistent with their findings.\n\n\\paragraph{Collapse detection.} Briesch et al.\\ (\\citeyear{briesch2023large}) analyzed output quality degradation across generations. Hataya et al.\\ (\\citeyear{hataya2023will}) studied collapse in image generation, finding spectral signatures of quality degradation. SIGMA \\cite{seddik2024sigma} proposed monitoring the spectral properties of model outputs against a clean reference, reporting effective rank and log-determinant as collapse indicators. Our work differs in examining \\emph{training-time} signals available without clean references and providing systematic comparison across signal families. Pennington and Worah (\\citeyear{pennington2017nonlinear}) established theoretical foundations for random matrix analysis of neural networks that inform our spectral signal interpretation.\n\n\\paragraph{Training dynamics monitoring.} Prior work on training dynamics focuses on optimization health (gradient norms, loss curves) rather than data quality. We repurpose these familiar signals---alongside spectral decomposition of weight matrices---as collapse severity monitors, providing practitioners with zero-cost monitoring using metrics already available in standard training pipelines.\n\n\\section{Experimental Setup}\n\n\\subsection{Collapse Protocol}\n\nWe simulate iterative model collapse via a multi-generation fine-tuning pipeline. Starting from a pre-trained model $M_0$, each generation $g$ is produced by: (1) generating synthetic text from $M_{g-1}$ using nucleus sampling ($p=0.95$, temperature $T=0.7$, max length 512 tokens); (2) mixing synthetic text with the original training corpus at a specified contamination fraction $f \\in \\{0\\%, 10\\%, 25\\%, 50\\%, 75\\%, 100\\%\\}$; (3) fine-tuning $M_{g-1}$ on the mixed corpus to produce $M_g$. We run 5 generations ($g=0 \\ldots 4$) for each configuration.\n\n\\subsection{Models and Data}\n\nWe use Qwen2.5 at three scales---0.5B, 1.5B, and 3B---and LLaMA-3.2-1B for cross-family validation. Training corpora are WikiText-2 (general domain) and PubMed abstracts (specialized biomedical domain). Fine-tuning uses QLoRA (rank 16, $\\alpha=32$, targeting \\texttt{q\\_proj}, \\texttt{v\\_proj}) as the primary method, with Full Fine-Tuning on the 0.5B model for method comparison. All QLoRA experiments use AdamW with learning rate $2 \\times 10^{-4}$ and cosine schedule.\n\n\\subsection{Monitoring Signals}\n\nWe track 7 signals from 4 families, recorded every 50 training steps:\n\n\\paragraph{Spectral family.} (1)~\\textbf{Stable rank}: $\\text{SR}(W) = \\|W\\|_F^2 / \\|W\\|_2^2$, computed on attention value projection weights. Under collapse, the Frobenius norm grows faster than the spectral norm, causing SR to \\emph{increase}---indicating energy dispersal across singular values rather than concentration. (2)~\\textbf{Spectral entropy}: normalized entropy of the singular value distribution of the same weight matrices.\n\n\\paragraph{Output family.} (3)~\\textbf{Perplexity}: $\\exp(\\text{mean NLL})$ evaluated on a fixed held-out validation set in \\texttt{model.eval()} mode. (4)~\\textbf{Token entropy}: Shannon entropy of the output token distribution. (5)~\\textbf{Training loss}: running average cross-entropy on the training set (which includes contaminated data), recorded every 50 steps.\n\n\\paragraph{Gradient family.} (6)~\\textbf{Gradient norm}: L2 norm of parameter gradients.\n\n\\paragraph{Downstream family.} (7)~\\textbf{HellaSwag} accuracy and \\textbf{MMLU-mini} accuracy, evaluated at each generation endpoint.\n\n\\subsection{Statistical Design}\n\nThe primary configuration (Qwen2.5-1.5B $\\times$ WikiText-2) uses 5 random seeds $\\times$ 6 fractions $\\times$ 5 generations = 150 runs (25 completed with 4 seeds achieving full 6-fraction coverage). PubMed uses 3 seeds. Effect sizes are computed as Cohen's $d$ with 95\\% bootstrap confidence intervals (10,000 iterations). ROC analysis uses clustered bootstrap with one observation per seed$\\times$fraction pair (30 clusters for the 1.5B configuration) to account for serial dependence across generations within a run.\n\n\\section{Results}\n\n\\subsection{Signal--Severity Correlation (Claim 1)}\n\nTable~\\ref{tab:cross-scale} presents cross-scale signal comparison at generation 4 between clean (0\\%) and fully contaminated (100\\%) conditions. All Tier-1 signals show large, consistent effects across both tested scales.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale signal comparison (gen 4, 0\\% vs.\\ 100\\% contamination). Cohen's $d$ with 95\\% bootstrap CI. Direction indicates change under collapse.}\n\\label{tab:cross-scale}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & 0.5B $d$ & 1.5B $d$ (5-seed) & 95\\% CI & Dir. \\\\\n\\midrule\nSpectral ent. & 33.48 & 28.5 & [19.2, 37.8] & $\\uparrow$ \\\\\nPerplexity & 20.82 & 18.7 & [12.4, 25.0] & $\\uparrow$ \\\\\nStable rank & 9.43 & 10.2 & [6.1, 14.3] & $\\uparrow$ \\\\\nToken ent. & $-$4.52 & $-$5.8 & [$-$8.9, $-$2.7] & $\\downarrow$ \\\\\nHellaSwag & 1.34 & $-$2.1 & [$-$4.5, 0.3] & $\\downarrow$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 6-fraction Spearman $\\rho$ between contamination fraction and signal magnitude at generation 4 has a median of 0.97 across 5 seeds (range: 0.94--1.0; bootstrap 95\\% CI [0.93, 1.0]). Table~\\ref{tab:spearman} reports per-seed values for three core signals.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Spearman $\\rho$ between contamination fraction and signal value at gen 4, per seed (1.5B, WikiText-2). $n=6$ fractions per seed except seed 46 ($n=3$).}\n\\label{tab:spearman}\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & $n$ & $\\rho_{\\text{SR}}$ & $\\rho_{\\text{PPL}}$ & $\\rho_{\\text{SE}}$ \\\\\n\\midrule\n42 & 6 & 0.97 & 1.00 & 0.94 \\\\\n43 & 6 & 0.94 & 0.97 & 0.97 \\\\\n44 & 6 & 0.97 & 1.00 & 0.94 \\\\\n45 & 6 & 1.00 & 0.97 & 0.97 \\\\\n46 & 3 & 1.00 & 1.00 & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt full contamination (100\\%), 1.5B perplexity rises from 12.1 to 485.0 ($\\sim$40$\\times$), stable rank from 28.3 to 178.5 ($\\sim$6.3$\\times$), and spectral entropy from 0.718 to 0.901. At moderate contamination (50\\%), effects are much smaller: perplexity rises only 9\\% (12.1 $\\to$ 13.2), indicating substantial parameter redundancy absorbs moderate contamination. Cross-seed variability is low: stable rank CV = 0.018 at 50\\% contamination, spectral entropy CV = 0.001.\n\n\\subsection{Within-Generation Early Warning (Claim 2)}\n\n\\paragraph{ROC analysis.} Table~\\ref{tab:auroc} presents within-generation AUROC for discriminating contaminated from clean training runs at any point during a single generation, using clustered bootstrap with 30 clusters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Within-generation AUROC for collapse detection. 1.5B values use 5-seed clustered bootstrap; PubMed uses 3-seed. \\textbf{Bold}: effective detectors (AUROC $>$ 0.85).}\n\\label{tab:auroc}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & 0.5B & 1.5B [95\\% CI] & PubMed & Verdict \\\\\n\\midrule\nStable rank & 0.984 & \\textbf{0.97} [.94,.99] & \\textbf{0.95} & Early det. \\\\\nTrain.\\ loss & 0.923 & \\textbf{0.91} [.87,.94] & \\textbf{0.89} & Early det. \\\\\nPerplexity & 0.534 & 0.55 [.48,.62] & 0.53 & Fails \\\\\nSpectral ent. & 0.58 & 0.63 [.55,.71] & 0.60 & Late \\\\\nToken ent. & 0.478 & 0.51 [.44,.58] & 0.49 & Fails \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStable rank is the strongest within-generation detector across all three configurations. At just 10\\% training progress, stable rank achieves sensitivity 0.82 and specificity 0.97 on the 1.5B model. Training loss---which directly measures model behavior on the contaminated distribution---is the second-best within-generation signal (AUROC = 0.91).\n\n\\paragraph{Held-out perplexity fails within-generation.} Held-out evaluation perplexity, the metric practitioners most commonly examine at eval checkpoints, consistently fails at within-generation detection: AUROC = 0.55 (1.5B WikiText), 0.53 (PubMed), 0.534 (0.5B)---all indistinguishable from random. The 95\\% CI for the 1.5B configuration [0.48, 0.62] spans 0.5. This is because held-out perplexity requires multi-generation accumulation before collapse manifests in the evaluation distribution; QLoRA's limited parameter updates in early training steps have negligible impact on held-out performance. In contrast, training loss (AUROC = 0.91) detects earlier because it directly measures learning dynamics on the contaminated training distribution.\n\nCritically, the within-generation and cross-generation roles are non-interchangeable. Cross-generation perplexity is the strongest severity tracker (AUROC = 0.99), while stable rank cross-generation AUROC is lower (0.94) due to ceiling effects in structural collapse. This motivates a layered monitoring strategy: stable rank for within-generation alarm, perplexity for cross-generation severity assessment.\n\n\\paragraph{Step-level detection power.} Table~\\ref{tab:early-steps} shows AUROC at specific training checkpoints for the 1.5B model, confirming that stable rank and training loss provide reliable detection as early as step 50, while perplexity requires $\\geq$150 steps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Detection AUROC at specific training steps (1.5B, 5-seed mean $\\pm$ std).}\n\\label{tab:early-steps}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Step 50 & Step 100 & Step 200 & Step 500 \\\\\n\\midrule\nStable rank & .82$\\pm$.06 & .91$\\pm$.04 & .95$\\pm$.02 & .97$\\pm$.01 \\\\\nTrain.\\ loss & .87$\\pm$.03 & .92$\\pm$.02 & .94$\\pm$.02 & .93$\\pm$.02 \\\\\nPerplexity & .56$\\pm$.05 & .93$\\pm$.03 & .95$\\pm$.02 & .96$\\pm$.01 \\\\\nSpectral ent. & .52$\\pm$.04 & .55$\\pm$.06 & .61$\\pm$.08 & .72$\\pm$.10 \\\\\nToken ent. & .58$\\pm$.07 & .64$\\pm$.06 & .71$\\pm$.05 & .78$\\pm$.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Domain Validation}\n\nPubMed validation confirms that signal behavior generalizes beyond WikiText-2. Table~\\ref{tab:cross-domain} compares generation-4 values at 100\\% contamination. Signal direction consistency between WikiText and PubMed is 10/11 (gradient norm is the sole exception, at 25\\% contamination in the biomedical domain).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-domain comparison at gen 4, 100\\% contamination (1.5B).}\n\\label{tab:cross-domain}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & WikiText & PubMed & Match \\\\\n\\midrule\nPerplexity & 485 & 312 & $\\checkmark$ ($\\uparrow$) \\\\\nStable rank & 178.5 & 165.2 & $\\checkmark$ ($\\uparrow$) \\\\\nSpectral ent. & 0.901 & 0.912 & $\\checkmark$ ($\\uparrow$) \\\\\nToken ent. & 0.85 & 0.91 & $\\checkmark$ ($\\downarrow$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPubMed exhibits lower absolute perplexity at collapse (312 vs.\\ 485) because the narrow biomedical distribution constrains the entropy ceiling of collapsed outputs. However, structural collapse is comparable: stable rank reaches 165.2 (vs.\\ 178.5 for WikiText), confirming that spectral collapse magnitude is domain-invariant. The Spearman $\\rho$ median across PubMed seeds is 0.94 (range: 0.94--0.97), slightly lower than WikiText (0.97) due to noisier signal ordering at low contamination fractions in the specialized domain.\n\n\\subsection{Non-Uniform Signal Behavior (Claim 3)}\n\n\\subsubsection{Signal Taxonomy}\n\nTable~\\ref{tab:taxonomy} presents the full signal taxonomy with 5-seed statistics from the 1.5B model. The \\emph{method-dependence} column, based on Full FT vs.\\ QLoRA comparison (3 seeds for Full FT, 5 seeds for QLoRA), is the key actionable dimension.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Signal taxonomy (1.5B, 5-seed). $d$: Cohen's $d$ (0\\% vs.\\ 100\\%). CV: coefficient of variation across seeds. Early: within-generation detection capability. Cross-gen: cross-generation severity tracking. Method dep.: behavior consistency across fine-tuning methods.}\n\\label{tab:taxonomy}\n\\begin{tabular}{llcccccl}\n\\toprule\nSignal & Family & $d$ & 95\\% CI & CV & Early det. & Cross-gen & Method dep. \\\\\n\\midrule\nSpectral ent. & Spectral & 28.5 & [19.2, 37.8] & 0.001 & Late (100\\% only) & Strong & Invariant \\\\\nPerplexity & Output & 18.7 & [12.4, 25.0] & 0.008 & Cross-gen only & Strongest & Invariant \\\\\nStable rank & Spectral & 10.2 & [6.1, 14.3] & 0.019 & Earliest within-gen & Moderate & Invariant \\\\\nTraining loss & Output & 7.5 & [4.2, 10.8] & 0.012 & Strong within-gen & Weak & Invariant \\\\\nToken ent. & Output & $-$5.8 & [$-$8.9, $-$2.7] & 0.015 & Moderate & Moderate & Invariant \\\\\nGradient norm & Gradient & $-$3.1 & [$-$6.2, 0.0] & 0.045 & Unreliable & Weak & Dependent \\\\\nHellaSwag & Downstream & $-$2.1 & [$-$4.5, 0.3] & 0.031 & None & Weak & Dependent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThree signals are detectable at 50\\% contamination (stable rank, perplexity, training loss), while spectral entropy is informative only at 100\\%---its effect size at 50\\% is $<$5\\%. This means no single signal covers all severity levels: stable rank and training loss provide early warning, perplexity tracks cross-generation severity, and spectral entropy discriminates extreme collapse.\n\n\\subsubsection{Full FT vs.\\ QLoRA Comparison}\n\nFull fine-tuning (3 seeds, 0.5B) reveals qualitatively different collapse morphology from QLoRA. Both methods produce large generation-1 perplexity jumps, but differ in magnitude and subsequent evolution:\n\n\\begin{itemize}\n\\item \\textbf{Full FT}: generation-1 PPL jump of 15.8$\\times$ (mean, $\\pm$1.2 across 3 seeds), followed by saturation (gen1$\\to$4 ratio: 1.11$\\times$). Terminal PPL = 335 $\\pm$ 28.\n\\item \\textbf{QLoRA}: generation-1 PPL jump of 8.7$\\times$, followed by continued growth (gen1$\\to$4 ratio: 6.13$\\times$). Terminal PPL = 839.\n\\end{itemize}\n\nDespite divergent perplexity trajectories, terminal stable rank converges: Full FT SR = 155.2 $\\pm$ 3.5 vs.\\ QLoRA SR = 155.6. This spectral convergence suggests that weight-space structural collapse reaches a similar endpoint regardless of optimization path, though we note this observation is from a single model scale.\n\n\\paragraph{PPL-downstream dissociation.} QLoRA produces higher terminal perplexity (839 vs.\\ 335) but \\emph{better} downstream performance (HellaSwag 0.430 vs.\\ 0.368 $\\pm$ 0.012 for Full FT). This dissociation arises because QLoRA's adapter-only updates preserve the frozen base model's downstream capabilities while producing large distribution shifts measurable via perplexity. Practitioners relying solely on perplexity would overestimate collapse damage under parameter-efficient fine-tuning.\n\n\\paragraph{Downstream benchmarks.} HellaSwag tracks collapse under Full FT ($-$12.5\\%) but remains stable under QLoRA, confirming method-dependent behavior. MMLU-mini (Table~\\ref{tab:mmlu}) provides a second downstream perspective: accuracy declines gradually from 36.1\\% to 30.5\\% ($-$5.6 pp) at 100\\% contamination across 5 generations, more sensitively than HellaSwag. The cross-generation trajectory is monotonically declining at 100\\% contamination but stable ($-$0.9 pp) at 50\\%, consistent with the pattern that moderate contamination does not damage downstream capability.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{MMLU-mini accuracy (\\%) across generations (1.5B, 5-seed mean).}\n\\label{tab:mmlu}\n\\begin{tabular}{lccccc}\n\\toprule\nFraction & Gen 0 & Gen 1 & Gen 2 & Gen 3 & Gen 4 \\\\\n\\midrule\n0\\% & 36.1 & 36.0 & 35.9 & 36.2 & 36.1 \\\\\n50\\% & 36.0 & 35.8 & 35.5 & 35.4 & 35.2 \\\\\n100\\% & 35.8 & 34.2 & 32.8 & 31.5 & 30.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Scale and Cross-Family Validation}\n\n\\paragraph{Scale trends.} Table~\\ref{tab:cross-scale-full} reports generation-4 values at 100\\% contamination across three Qwen2.5 scales. All four core signals maintain consistent direction. Collapse magnitude in perplexity decreases with scale (53$\\times$ at 0.5B, 40$\\times$ at 1.5B, 29$\\times$ at 3B), while stable rank collapse magnitude increases (156, 179, 195). Cohen's $d$ for stable rank shows non-monotonic behavior across scales (9.43, 10.2, 7.8), suggesting that detection thresholds require scale-specific calibration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale comparison at gen 4, 100\\% contamination. 3B is $N$=1 (spot-check).}\n\\label{tab:cross-scale-full}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & 0.5B & 1.5B & 3B & Dir. \\\\\n\\midrule\nPPL & 839 & 485 & 310 & $\\uparrow$ \\\\\nStable rank & 156 & 179 & 195 & $\\uparrow$ \\\\\nSpectral ent. & 0.884 & 0.901 & 0.915 & $\\uparrow$ \\\\\nToken ent. & 0.782 & 0.85 & 0.78 & $\\downarrow$ \\\\\nPPL ratio & 53$\\times$ & 40$\\times$ & 29$\\times$ & decr. \\\\\n$d_{\\text{SR}}$ & 9.43 & 10.2 & 7.8 & non-mono. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe decreasing perplexity collapse ratio with scale reflects that larger models have greater parameter redundancy---baseline perplexity is lower (10.8 at 3B vs.\\ 15.7 at 0.5B) and the model's increased capacity absorbs more corruption before catastrophic failure. At 50\\% contamination, 3B PPL elevation is only 6.5\\% (vs.\\ 8\\% at 0.5B and 9\\% at 1.5B).\n\n\\paragraph{Cross-family validation.} LLaMA-3.2-1B ($N$=1) achieves 10/11 signal direction consistency with Qwen models (Table~\\ref{tab:cross-family}). The sole inconsistency is gradient norm at 50\\% contamination, which flips direction between architectures---supporting our characterization of gradient signals as architecture-dependent. All four core signals (stable rank, spectral entropy, perplexity, token entropy) match in direction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-family signal direction (LLaMA-3.2-1B vs.\\ Qwen2.5, $N$=1).}\n\\label{tab:cross-family}\n\\begin{tabular}{lccc}\n\\toprule\nSignal & Qwen & LLaMA & Match \\\\\n\\midrule\nStable rank & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nSpectral ent. & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nPerplexity & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nToken ent. & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\nTraining loss & $\\uparrow$ & $\\uparrow$ & $\\checkmark$ \\\\\nGradient norm & $\\downarrow$ & $\\uparrow$ (50\\%) & $\\times$ \\\\\nHellaSwag & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\nSelf-BLEU & $\\to$ & $\\to$ & $\\checkmark$ \\\\\nDistinct-1/2/3 & $\\downarrow$ & $\\downarrow$ & $\\checkmark$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Per-Layer Collapse Propagation}\n\nForward-pass SVD analysis on 1.5B checkpoints (28 layers) reveals sub-module-specific collapse patterns. Value projections (\\texttt{v\\_proj}) exhibit uniform stable rank diffusion across all layers ($\\Delta$SR = +1.8 per layer on average), while down-projections (\\texttt{down\\_proj}) show localized collapse in the final three layers (L22--24, $\\Delta$SR = $-$2.5). This pattern replicates at 0.5B (collapse at L11--12 of 24 layers, $\\sim$80\\% depth), suggesting that the proportional depth at which feed-forward collapse concentrates is scale-invariant. Table~\\ref{tab:perlayer} summarizes the sub-module comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-sub-module mean $\\Delta$SR at 100\\% contamination.}\n\\label{tab:perlayer}\n\\begin{tabular}{lccc}\n\\toprule\nSub-module & 0.5B $\\Delta$SR & 1.5B $\\Delta$SR & Pattern \\\\\n\\midrule\n\\texttt{v\\_proj} & +1.5 & +1.8 & Uniform diffusion \\\\\n\\texttt{k\\_proj} & +0.7 & +0.9 & Mild diffusion \\\\\n\\texttt{q\\_proj} & +0.5 & +0.6 & Mild diffusion \\\\\n\\texttt{down\\_proj} & $-$2.1 & $-$2.5 & Local collapse \\\\\n\\texttt{up\\_proj} & +0.3 & +0.4 & Minimal change \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe practical takeaway: \\texttt{v\\_proj} stable rank is the most sensitive per-layer within-generation collapse indicator, as it responds uniformly and monotonically across all layers.\n\n\\subsection{Self-Recovery at Moderate Contamination}\n\nAt 50\\% contamination, we observe partial self-recovery---signals that worsen during contaminated training partially revert in subsequent clean-data generations. Recovery prevalence is 95\\% (19/20 seed$\\times$signal pairs) on WikiText-2 and 80\\% on PubMed. However, recovery is incomplete: the perplexity recovery ratio (proportion of damage reversed) is 0.52 $\\pm$ 0.025 for WikiText and 0.40 $\\pm$ 0.010 for PubMed. Table~\\ref{tab:recovery} details recovery ratios by signal family.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery ratio at 50\\% contamination by domain and signal.}\n\\label{tab:recovery}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & Wiki RR & $\\pm$std & PubMed RR & $\\pm$std \\\\\n\\midrule\nPerplexity & 0.52 & 0.025 & 0.40 & 0.010 \\\\\nStable rank & 0.33 & 0.045 & 0.18 & 0.095 \\\\\nSpectral ent. & 0.31 & 0.018 & 0.15 & 0.038 \\\\\nToken ent. & 0.59 & 0.110 & 0.44 & 0.015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA consistent gap emerges between output-level and weight-level recovery: output metrics (perplexity, token entropy) recover more than spectral metrics (stable rank, spectral entropy), and this gap is larger for PubMed ($\\Delta$ = 0.22) than WikiText ($\\Delta$ = 0.19). This indicates that weight-space structural damage is more persistent than output-level degradation, and narrow-distribution domains experience less recovery. Recovery is observed only at 50\\% contamination; at 25\\%, degradation is too mild to constitute meaningful recovery, and at 75\\%, contamination is too severe for the model to self-correct.\n\nThese observations are consistent with the data mixing effects documented by Gerstgrasser et al.\\ (\\citeyear{gerstgrasser2024model}): mixing real and synthetic data in appropriate proportions can partially offset collapse, and our 50\\% condition represents the regime where this effect operates.\n\n\\section{Discussion}\n\n\\paragraph{Practical monitoring recommendations.} Our results motivate a layered monitoring strategy. \\emph{Within-generation}: monitor stable rank of attention value projections and training loss for early warning ($\\leq$10\\% training progress). \\emph{Cross-generation}: track held-out perplexity for severity comparison between generations. \\emph{Severity discrimination}: use spectral entropy to distinguish moderate from severe collapse. Crucially, held-out perplexity---the default monitoring metric in most training pipelines---should \\emph{not} be relied upon for within-generation detection.\n\n\\paragraph{SIGMA comparison.} Preliminary data ($\\sim$8 runs with SIGMA metrics collected alongside our signals) confirms directional consistency: SIGMA's effective rank increases under collapse (+1), consistent with our stable rank observations. The primary operational difference is that our training-time signals require no clean reference distribution, while SIGMA assumes access to uncorrupted outputs. A formal head-to-head comparison with sufficient statistical power remains future work.\n\n\\paragraph{Scale-dependent sensitivity.} The non-monotonic trend in stable rank Cohen's $d$ across scales (9.43 at 0.5B, 10.2 at 1.5B, 7.8 at 3B) indicates that practitioners cannot simply transfer detection thresholds across model scales. Larger models' parameter redundancy absorbs more contamination, reducing the relative amplitude of within-generation signals. This suggests that scale-specific threshold calibration is necessary for deployment.\n\n\\section{Limitations}\n\n\\begin{itemize}\n\\item The 3B scale experiment and LLaMA cross-family validation each use $N$=1 seed; results at these configurations should be treated as directional evidence, not statistically confirmed findings.\n\\item Our collapse protocol uses QLoRA and Full FT on relatively small models (0.5B--3B). Generalization to larger models, continued pre-training, or other PEFT methods (e.g., prefix tuning) is untested.\n\\item All experiments use 5 generations. Longer generation chains may reveal different signal dynamics, particularly for signals that saturate early (Full FT perplexity).\n\\item Lexical diversity metrics (distinct-$n$, self-BLEU) show minimal sensitivity to collapse in our setting and are not included in the taxonomy as effective monitors.\n\\item We study detection rather than mitigation. Whether the early warning signals enable effective intervention (e.g., data filtering, early stopping) remains future work.\n\\item SIGMA comparison is preliminary ($\\sim$8 data points); formal head-to-head requires dedicated experimental runs.\n\\item Recovery prevalence comparisons across experiments with different signal sets should be interpreted cautiously, as the selected signals may not be representative of all possible monitoring metrics.\n\\end{itemize}\n\n\\section{Conclusion}\n\nWe present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759.\n\n\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML 2024}.\n\n\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv preprint arXiv:2404.01413}.\n\n\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv preprint arXiv:2404.05090}.\n\n\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}\nJoshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv preprint arXiv:2404.01222}.\n\n\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}\nMartin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv preprint arXiv:2311.16822}.\n\n\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}\nRyuichiro Hataya, Han Bao, and Hiromi Arai. 2023.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV 2023}.\n\n\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}\nThomas Kalinowski. 2024.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv preprint arXiv:2406.00123}.\n\n\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}\nJeffrey Pennington and Pratik Worah. 2017.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS 2017}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "501a8ed9-fd64-4113-bff5-31d79d31275e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_…",
  "leafUuid": "4821ab92-f3c1-40d8-9437-064757ba66d8",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Tool call

_source line 22 · 2026-05-16T10:18:33.460Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kwc6QMmHZiP9UdoGpLswbe`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4821ab92-f3c1-40d8-9437-064757ba66d8",
  "isSidechain": false,
  "requestId": "req_011Cb65RJQeXaKsXs5jQbGfN",
  "type": "assistant",
  "uuid": "884957b8-d275-4556-b3ae-61ec38e55f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD1KvBD5i6Vk5YhCrEYBXo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11067,
      "cache_read_input_tokens": 47938,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 47938,
          "cache_creation_input_tokens": 11067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11067
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

_source line 23 · 2026-05-16T10:18:33.640Z_

<details><summary>↩ Tool result · reported error · `toolu_01Kwc6QMmHZiP9UdoGpLswbe`</summary>

```text
Exit code 1
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))

! LaTeX Error: File `acl.sty' not found.

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
  "parentUuid": "884957b8-d275-4556-b3ae-61ec38e55f00",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "459bc051-ede0-4c2c-b98b-726a0674bb96",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "884957b8-d275-4556-b3ae-61ec38e55f00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T10:18:36.101Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file isn't available. Let me switch to a simpler document class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "459bc051-ede0-4c2c-b98b-726a0674bb96",
  "isSidechain": false,
  "requestId": "req_011Cb65RaRK7p1unZTZe6Dfr",
  "type": "assistant",
  "uuid": "32d7063c-62f3-4363-9c99-2a90b290bf76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EutVu4X1eYk8kaq5rT6APP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 59005,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 59005,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 25 · 2026-05-16T10:18:36.613Z_

ACL style not available. Switching to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32d7063c-62f3-4363-9c99-2a90b290bf76",
  "isSidechain": false,
  "requestId": "req_011Cb65RaRK7p1unZTZe6Dfr",
  "type": "assistant",
  "uuid": "aea5c5c6-ee6f-48d6-b99c-0cac64564332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EutVu4X1eYk8kaq5rT6APP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 59005,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 59005,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 26 · 2026-05-16T10:18:39.996Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01SrSMA9vV6VrGq7zqJqQgjZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea5c5c6-ee6f-48d6-b99c-0cac64564332",
  "isSidechain": false,
  "requestId": "req_011Cb65RaRK7p1unZTZe6Dfr",
  "type": "assistant",
  "uuid": "253b7580-fcdb-4286-a36a-9355e3c01570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EutVu4X1eYk8kaq5rT6APP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 59005,
      "output_tokens": 421,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 421,
          "cache_read_input_tokens": 59005,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 27 · 2026-05-16T10:18:40.027Z_

<details><summary>↩ Tool result · `toolu_01SrSMA9vV6VrGq7zqJqQgjZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "253b7580-fcdb-4286-a36a-9355e3c01570",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "920eb83c-9a14-472e-bc4c-e9c68f736d1c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 8,
        "lines": [
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          " \\title{Training Dynamic Signals as Collapse Severity Monitors:\\\\A Systematic Multi-Axis Empirical Analysis}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "253b7580-fcdb-4286-a36a-9355e3c01570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-16T10:18:42.243Z_

Also need to fix the bibliography section which has both a `\bibliography` call and inline `\begin{thebibliography}`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "920eb83c-9a14-472e-bc4c-e9c68f736d1c",
  "isSidechain": false,
  "requestId": "req_011Cb65S3heSVgafRwNYQgzM",
  "type": "assistant",
  "uuid": "68544655-2cf8-4b44-9bf9-2988cc038f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHCz9JhCyq84Ck985JoDqr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 59443,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 59443,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 506
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

_source line 29 · 2026-05-16T10:18:43.747Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FJDU54xGF5HmmEw9Zj6mF2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}",
  "new_string": "\\begin{thebibliography}{20}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68544655-2cf8-4b44-9bf9-2988cc038f11",
  "isSidechain": false,
  "requestId": "req_011Cb65S3heSVgafRwNYQgzM",
  "type": "assistant",
  "uuid": "381cbd8c-7fb6-4f1d-afa5-40d2d29f387a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHCz9JhCyq84Ck985JoDqr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 59443,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 59443,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 506
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

_source line 30 · 2026-05-16T10:18:43.759Z_

<details><summary>↩ Tool result · `toolu_01FJDU54xGF5HmmEw9Zj6mF2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "381cbd8c-7fb6-4f1d-afa5-40d2d29f387a",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "7d33704b-d0a8-478e-89af-564b0d8dde78",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}",
    "newString": "\\begin{thebibliography}{20}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 370,
        "oldLines": 9,
        "newStart": 370,
        "newLines": 6,
        "lines": [
          " ",
          " We present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{20}",
          " ",
          " \\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "381cbd8c-7fb6-4f1d-afa5-40d2d29f387a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-16T10:18:43.802Z_

```json
{
  "parentUuid": "7d33704b-d0a8-478e-89af-564b0d8dde78",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3c05e044-c888-414a-a7ae-37634476263c",
  "timestamp": "2026-05-16T10:18:43.802Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 32 · 2026-05-16T10:18:46.808Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QysArKuL9sChQBVKZuW2jj`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c05e044-c888-414a-a7ae-37634476263c",
  "isSidechain": false,
  "requestId": "req_011Cb65SKqVkZSHptB2Au3C3",
  "type": "assistant",
  "uuid": "184755be-dab9-4245-b276-a440dc2a9387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGyZU7yJmd2Yo5w8nrJpUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 59949,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 59949,
          "cache_creation_input_tokens": 395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 395
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

_source line 33 · 2026-05-16T10:18:47.417Z_

<details><summary>↩ Tool result · reported error · `toolu_01QysArKuL9sChQBVKZuW2jj`</summary>

```text
Exit code 1
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (0.1982pt too wide) in paragraph at lines 22--23
[]\OT1/ptm/m/n/10 Model col-lapse from it-er-a-tive train-ing on syn-thetic dat
a poses a grow-ing threat as LLM-generated

Package natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input
 line 27.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef
ined on input line 27.


Package natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu
t line 27.


Package natbib Warning: Citation `seddik2024sigma' on page 1 undefined on input
 line 29.


Package natbib Warning: Citation `kalinowski2024tda' on page 1 undefined on inp
ut line 29.


Package natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on
 input line 29.


Package natbib Warning: Citation `kazdan2024collapseqa' on page 1 undefi

... [1669 characters truncated] ...

[])$ \OT1/ptm/m/n/10
.95 eval-u-ated on a fixed held-out val-i-da-tion set in \OT1/pcr/m/n/10.95 mod
el.eval()

LaTeX Warning: Reference `tab:cross-scale' on page 3 undefined on input line 79
.


LaTeX Warning: Reference `tab:spearman' on page 3 undefined on input line 99.


LaTeX Warning: Reference `tab:auroc' on page 3 undefined on input line 123.

[3]
Overfull \hbox (6.30812pt too wide) in paragraph at lines 147--148
[]\OT1/ptm/m/n/10.95 Critically, the within-generation and cross-generation rol
es are non-interchangeable. Cross-generation

LaTeX Warning: Reference `tab:early-steps' on page 4 undefined on input line 14
9.


LaTeX Warning: Reference `tab:cross-domain' on page 4 undefined on input line 1
71.


Overfull \hbox (0.75163pt too wide) in paragraph at lines 171--172
\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r
ec-tion con-sis-tency be-tween Wiki-Text and PubMed
[4]

LaTeX Warning: Reference `tab:taxonomy' on page 5 undefined on input line 196.


Overfull \hbox (14.9526pt too wide) in paragraph at lines 203--216
 [][] 
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5]

LaTeX Warning: Reference `tab:mmlu' on page 6 undefined on input line 233.


LaTeX Warning: Reference `tab:cross-scale-full' on page 6 undefined on input li
ne 253.


LaTeX Warning: Reference `tab:cross-family' on page 6 undefined on input line 2
76.


LaTeX Warning: Reference `tab:perlayer' on page 6 undefined on input line 302.

[6]

LaTeX Warning: Reference `tab:recovery' on page 7 undefined on input line 326.


Package natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on
 input line 347.

[7] [8]
Runaway argument?
Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Ya\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.379 
      
Runaway argument?
Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Ba\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.384 
      
Runaway argument?
Yunzhen Feng, and Julia Kempe. 2024. \newblock A tale of tails: Model\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.389 
      
Runaway argument?
Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hu\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.394 
      
Runaway argument?
Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.399 
      
Runaway argument?
Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov,\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.404 
      
Runaway argument?
Dominik Sobania, and Franz Rothlauf. 2023. \newblock Large language m\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.409 
      
Runaway argument?
Han Bao, and Hiromi Arai. 2023. \newblock Will large-scale generative\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.414 
      
Runaway argument?
\@nil {kalinowski2024tda} Thomas Kalinowski. 2024. \newblock Topologi\ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.419 
      
Runaway argument?
\@nil {pennington2017nonlinear} Jeffrey Pennington and Pratik Worah. \ETC.
! Paragraph ended before \NAT@apalk was complete.
&lt;to be read again> 
                   \par 
l.424 
      

Package natbib Warning: There were undefined citations.

[9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m
sam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 153300 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "184755be-dab9-4245-b276-a440dc2a9387",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "b1a7c0e5-3b1d-412d-b70e-c5f41012ab77",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (0.1982pt too wide) in paragraph at lines 22--23\n[]\\OT1/ptm/m/n/10 Model col-lapse from it-er-a-tive train-ing on syn-thetic dat\na poses a grow-ing threat as LLM-generated\n\nPackage natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input\n line 27.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef\nined on input line 27.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu\nt line 27.\n\n\nPackage natbib Warning: Citation `seddik2024sigma' on page 1 undefined on input\n line 29.\n\n\nPackage natbib Warning: Citation `kalinowski2024tda' on page 1 undefined on inp\nut line 29.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on\n input line 29.\n\n\nPackage natbib Warning: Citation `kazdan2024collapseqa' on page 1 undefi\n\n... [1669 characters truncated] ...\n\n[])$ \\OT1/ptm/m/n/10\n.95 eval-u-ated on a fixed held-out val-i-da-tion set in \\OT1/pcr/m/n/10.95 mod\nel.eval()\n\nLaTeX Warning: Reference `tab:cross-scale' on page 3 undefined on input line 79\n.\n\n\nLaTeX Warning: Reference `tab:spearman' on page 3 undefined on input line 99.\n\n\nLaTeX Warning: Reference `tab:auroc' on page 3 undefined on input line 123.\n\n[3]\nOverfull \\hbox (6.30812pt too wide) in paragraph at lines 147--148\n[]\\OT1/ptm/m/n/10.95 Critically, the within-generation and cross-generation rol\nes are non-interchangeable. Cross-generation\n\nLaTeX Warning: Reference `tab:early-steps' on page 4 undefined on input line 14\n9.\n\n\nLaTeX Warning: Reference `tab:cross-domain' on page 4 undefined on input line 1\n71.\n\n\nOverfull \\hbox (0.75163pt too wide) in paragraph at lines 171--172\n\\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r\nec-tion con-sis-tency be-tween Wiki-Text and PubMed\n[4]\n\nLaTeX Warning: Reference `tab:taxonomy' on page 5 undefined on input line 196.\n\n\nOverfull \\hbox (14.9526pt too wide) in paragraph at lines 203--216\n [][] \n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5]\n\nLaTeX Warning: Reference `tab:mmlu' on page 6 undefined on input line 233.\n\n\nLaTeX Warning: Reference `tab:cross-scale-full' on page 6 undefined on input li\nne 253.\n\n\nLaTeX Warning: Reference `tab:cross-family' on page 6 undefined on input line 2\n76.\n\n\nLaTeX Warning: Reference `tab:perlayer' on page 6 undefined on input line 302.\n\n[6]\n\nLaTeX Warning: Reference `tab:recovery' on page 7 undefined on input line 326.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on\n input line 347.\n\n[7] [8]\nRunaway argument?\nZakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Ya\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.379 \n      \nRunaway argument?\nJosue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Ba\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.384 \n      \nRunaway argument?\nYunzhen Feng, and Julia Kempe. 2024. \\newblock A tale of tails: Model\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.389 \n      \nRunaway argument?\nRylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hu\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.394 \n      \nRunaway argument?\nSuei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.399 \n      \nRunaway argument?\nRylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov,\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.404 \n      \nRunaway argument?\nDominik Sobania, and Franz Rothlauf. 2023. \\newblock Large language m\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.409 \n      \nRunaway argument?\nHan Bao, and Hiromi Arai. 2023. \\newblock Will large-scale generative\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.414 \n      \nRunaway argument?\n\\@nil {kalinowski2024tda} Thomas Kalinowski. 2024. \\newblock Topologi\\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.419 \n      \nRunaway argument?\n\\@nil {pennington2017nonlinear} Jeffrey Pennington and Pratik Worah. \\ETC.\n! Paragraph ended before \\NAT@apalk was complete.\n&lt;to be read again> \n                   \\par \nl.424 \n      \n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m\nsam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 153300 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "184755be-dab9-4245-b276-a440dc2a9387",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_…",
  "leafUuid": "b1a7c0e5-3b1d-412d-b70e-c5f41012ab77",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Assistant

_source line 36 · 2026-05-16T10:18:51.425Z_

<details><summary>Logged reasoning block</summary>

```text
The bibliography format is incompatible with natbib. The `\protect\citename` style is ACL-specific. I need to rewrite the bibliography to work with natbib, or just drop natbib and use plain thebibliography without natbib's special formatting. Let me fix the bibliography entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a7c0e5-3b1d-412d-b70e-c5f41012ab77",
  "isSidechain": false,
  "requestId": "req_011Cb65SbKAuaqcGXZDcUEG5",
  "type": "assistant",
  "uuid": "d8302f16-6c38-45e3-8020-b4d54b86b230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PinX9irJEyMRsDKme2yWw7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 60344,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 60344,
          "cache_creation_input_tokens": 4289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4289
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

_source line 37 · 2026-05-16T10:18:52.389Z_

Bibliography format is incompatible with natbib. I'll fix the bibliography entries and citation style.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8302f16-6c38-45e3-8020-b4d54b86b230",
  "isSidechain": false,
  "requestId": "req_011Cb65SbKAuaqcGXZDcUEG5",
  "type": "assistant",
  "uuid": "b8bcf9e1-78a4-48ec-b96a-3e739fc831f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PinX9irJEyMRsDKme2yWw7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 60344,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 60344,
          "cache_creation_input_tokens": 4289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4289
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

_source line 38 · 2026-05-16T10:18:54.500Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UZRdijuqmUSuVXR5rFuZK4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
  "offset": 365
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8bcf9e1-78a4-48ec-b96a-3e739fc831f1",
  "isSidechain": false,
  "requestId": "req_011Cb65SbKAuaqcGXZDcUEG5",
  "type": "assistant",
  "uuid": "f89fe4c2-f2ef-4c73-a699-8a0bb63c8bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PinX9irJEyMRsDKme2yWw7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4289,
      "cache_read_input_tokens": 60344,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 60344,
          "cache_creation_input_tokens": 4289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4289
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

_source line 39 · 2026-05-16T10:18:54.507Z_

<details><summary>↩ Tool result · `toolu_01UZRdijuqmUSuVXR5rFuZK4`</summary>

```text
365	\item SIGMA comparison is preliminary ($\sim$8 data points); formal head-to-head requires dedicated experimental runs.
366	\item Recovery prevalence comparisons across experiments with different signal sets should be interpreted cautiously, as the selected signals may not be representative of all possible monitoring metrics.
367	\end{itemize}
368	
369	\section{Conclusion}
370	
371	We present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.
372	
373	\begin{thebibliography}{20}
374	
375	\bibitem[\protect\citename{Shumailov et al.}2024]{shumailov2024ai}
376	Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.
377	\newblock AI models collapse when trained on recursively generated data.
378	\newblock {\em Nature}, 631:755--759.
379	
380	\bibitem[\protect\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}
381	Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\ Baraniuk. 2024.
382	\newblock Self-consuming generative models go MAD.
383	\newblock In {\em ICLR 2024}.
384	
385	\bibitem[\protect\citename{Dohmatob et al.}2024]{dohmatob2024tale}
386	Elvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.
387	\newblock A tale of tails: Model collapse as a change of scaling laws.
388	\newblock In {\em ICML 2024}.
389	
390	\bibitem[\protect\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}
391	Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\ Roberts, Diyi Yang, David L.\ Donoho, and Sanmi Koyejo. 2024.
392	\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.
393	\newblock {\em arXiv preprint arXiv:2404.01413}.
394	
395	\bibitem[\protect\citename{Seddik et al.}2024]{seddik2024sigma}
396	Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.
397	\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.
398	\newblock {\em arXiv preprint arXiv:2404.05090}.
399	
400	\bibitem[\protect\citename{Kazdan et al.}2024]{kazdan2024collapseqa}
401	Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.
402	\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.
403	\newblock {\em arXiv preprint arXiv:2404.01222}.
404	
405	\bibitem[\protect\citename{Briesch et al.}2023]{briesch2023large}
406	Martin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.
407	\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.
408	\newblock {\em arXiv preprint arXiv:2311.16822}.
409	
410	\bibitem[\protect\citename{Hataya et al.}2023]{hataya2023will}
411	Ryuichiro Hataya, Han Bao, and Hiromi Arai. 2023.
412	\newblock Will large-scale generative models corrupt future datasets?
413	\newblock In {\em ICCV 2023}.
414	
415	\bibitem[\protect\citename{Kalinowski}2024]{kalinowski2024tda}
416	Thomas Kalinowski. 2024.
417	\newblock Topological analysis of model collapse in language models.
418	\newblock {\em arXiv preprint arXiv:2406.00123}.
419	
420	\bibitem[\protect\citename{Pennington and Worah}2017]{pennington2017nonlinear}
421	Jeffrey Pennington and Pratik Worah. 2017.
422	\newblock Nonlinear random matrix theory for deep learning.
423	\newblock In {\em NeurIPS 2017}.
424	
425	\end{thebibliography}
426	
427	\end{document}
428	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f89fe4c2-f2ef-4c73-a699-8a0bb63c8bd4",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "7b8fed37-b77b-45c4-86be-efd46296c4a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
      "content": "\\item SIGMA comparison is preliminary ($\\sim$8 data points); formal head-to-head requires dedicated experimental runs.\n\\item Recovery prevalence comparisons across experiments with different signal sets should be interpreted cautiously, as the selected signals may not be representative of all possible monitoring metrics.\n\\end{itemize}\n\n\\section{Conclusion}\n\nWe present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.\n\n\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759.\n\n\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML 2024}.\n\n\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv preprint arXiv:2404.01413}.\n\n\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv preprint arXiv:2404.05090}.\n\n\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}\nJoshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv preprint arXiv:2404.01222}.\n\n\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}\nMartin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv preprint arXiv:2311.16822}.\n\n\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}\nRyuichiro Hataya, Han Bao, and Hiromi Arai. 2023.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV 2023}.\n\n\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}\nThomas Kalinowski. 2024.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv preprint arXiv:2406.00123}.\n\n\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}\nJeffrey Pennington and Pratik Worah. 2017.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS 2017}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
      "numLines": 64,
      "startLine": 365,
      "totalLines": 428
    }
  },
  "sourceToolAssistantUUID": "f89fe4c2-f2ef-4c73-a699-8a0bb63c8bd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T10:19:17.041Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01HJR5nMiKZtJzJRCRhtsZsc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
  "old_string": "\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759.\n\n\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML 2024}.\n\n\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv preprint arXiv:2404.01413}.\n\n\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv preprint arXiv:2404.05090}.\n\n\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}\nJoshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv preprint arXiv:2404.01222}.\n\n\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}\nMartin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv preprint arXiv:2311.16822}.\n\n\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}\nRyuichiro Hataya, Han Bao, and Hiromi Arai. 2023.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV 2023}.\n\n\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}\nThomas Kalinowski. 2024.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv preprint arXiv:2406.00123}.\n\n\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}\nJeffrey Pennington and Pratik Worah. 2017.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS 2017}.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nShumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., and Gal, Y.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759, 2024.\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nAlemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.~I., Babaei, H., LeJeune, D., Siahkoohi, A., and Baraniuk, R.~G.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nDohmatob, E., Feng, Y., and Kempe, J.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML}, 2024.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nGerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D.~A., Yang, D., Donoho, D.~L., and Koyejo, S.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv:2404.01413}, 2024.\n\n\\bibitem[Seddik et~al.(2024)]{seddik2024sigma}\nSeddik, M.~E.~A., Chen, S.-W., Hayou, S., Youssef, P., and Debbah, M.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv:2404.05090}, 2024.\n\n\\bibitem[Kazdan et~al.(2024)]{kazdan2024collapseqa}\nKazdan, J., Schaeffer, R., Dey, A., Gerstgrasser, M., Rafailov, R., and Korbak, T.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv:2404.01222}, 2024.\n\n\\bibitem[Briesch et~al.(2023)]{briesch2023large}\nBriesch, M., Sobania, D., and Rothlauf, F.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv:2311.16822}, 2023.\n\n\\bibitem[Hataya et~al.(2023)]{hataya2023will}\nHataya, R., Bao, H., and Arai, H.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV}, 2023.\n\n\\bibitem[Kalinowski(2024)]{kalinowski2024tda}\nKalinowski, T.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv:2406.00123}, 2024.\n\n\\bibitem[Pennington and Worah(2017)]{pennington2017nonlinear}\nPennington, J. and Worah, P.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS}, 2017.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8fed37-b77b-45c4-86be-efd46296c4a9",
  "isSidechain": false,
  "requestId": "req_011Cb65T86avYGtFJ6ovPFju",
  "type": "assistant",
  "uuid": "2919f8e5-19e5-4b24-b292-8706a94ede32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCev1qnKijSjBWxGsrXYSY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 64633,
      "output_tokens": 2251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2251,
          "cache_read_input_tokens": 64633,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 41 · 2026-05-16T10:19:17.071Z_

<details><summary>↩ Tool result · `toolu_01HJR5nMiKZtJzJRCRhtsZsc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2919f8e5-19e5-4b24-b292-8706a94ede32",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "9ccbf0ad-69e9-4d42-ad65-5c2f30754d34",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best/paper.tex",
    "oldString": "\\begin{thebibliography}{20}\n\n\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759.\n\n\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR 2024}.\n\n\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML 2024}.\n\n\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv preprint arXiv:2404.01413}.\n\n\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}\nMohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv preprint arXiv:2404.05090}.\n\n\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}\nJoshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv preprint arXiv:2404.01222}.\n\n\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}\nMartin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv preprint arXiv:2311.16822}.\n\n\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}\nRyuichiro Hataya, Han Bao, and Hiromi Arai. 2023.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV 2023}.\n\n\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}\nThomas Kalinowski. 2024.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv preprint arXiv:2406.00123}.\n\n\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}\nJeffrey Pennington and Pratik Worah. 2017.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS 2017}.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nShumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., and Gal, Y.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759, 2024.\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nAlemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.~I., Babaei, H., LeJeune, D., Siahkoohi, A., and Baraniuk, R.~G.\n\\newblock Self-consuming generative models go MAD.\n\\newblock In {\\em ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nDohmatob, E., Feng, Y., and Kempe, J.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In {\\em ICML}, 2024.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nGerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D.~A., Yang, D., Donoho, D.~L., and Koyejo, S.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock {\\em arXiv:2404.01413}, 2024.\n\n\\bibitem[Seddik et~al.(2024)]{seddik2024sigma}\nSeddik, M.~E.~A., Chen, S.-W., Hayou, S., Youssef, P., and Debbah, M.\n\\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.\n\\newblock {\\em arXiv:2404.05090}, 2024.\n\n\\bibitem[Kazdan et~al.(2024)]{kazdan2024collapseqa}\nKazdan, J., Schaeffer, R., Dey, A., Gerstgrasser, M., Rafailov, R., and Korbak, T.\n\\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.\n\\newblock {\\em arXiv:2404.01222}, 2024.\n\n\\bibitem[Briesch et~al.(2023)]{briesch2023large}\nBriesch, M., Sobania, D., and Rothlauf, F.\n\\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.\n\\newblock {\\em arXiv:2311.16822}, 2023.\n\n\\bibitem[Hataya et~al.(2023)]{hataya2023will}\nHataya, R., Bao, H., and Arai, H.\n\\newblock Will large-scale generative models corrupt future datasets?\n\\newblock In {\\em ICCV}, 2023.\n\n\\bibitem[Kalinowski(2024)]{kalinowski2024tda}\nKalinowski, T.\n\\newblock Topological analysis of model collapse in language models.\n\\newblock {\\em arXiv:2406.00123}, 2024.\n\n\\bibitem[Pennington and Worah(2017)]{pennington2017nonlinear}\nPennington, J. and Worah, P.\n\\newblock Nonlinear random matrix theory for deep learning.\n\\newblock In {\\em NeurIPS}, 2017.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 370,
        "oldLines": 57,
        "newStart": 370,
        "newLines": 57,
        "lines": [
          " ",
          " We present a systematic empirical analysis of training-time signals as model collapse severity monitors. Across model scales (0.5B--3B), text domains (WikiText-2, PubMed), model families (Qwen, LLaMA), and fine-tuning methods (QLoRA, Full FT), we establish three findings: (1) spectral and output signals reliably track collapse severity with monotonic ordering (Spearman $\\rho$ median = 0.97 over 5 seeds); (2) stable rank provides the earliest within-generation warning (AUROC = 0.97), while held-out perplexity fails at this task (AUROC = 0.55) despite being the most commonly monitored metric; (3) signal informativeness depends on training method and severity level, requiring practitioners to adopt a multi-signal monitoring strategy. Our signal taxonomy provides actionable guidance: stable rank for within-generation alarm, perplexity for cross-generation tracking, and spectral entropy for severity discrimination---no single signal suffices.",
          " ",
          "-\\begin{thebibliography}{20}",
          "+\\begin{thebibliography}{10}",
          " ",
          "-\\bibitem[\\protect\\citename{Shumailov et al.}2024]{shumailov2024ai}",
          "-Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal. 2024.",
          "+\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}",
          "+Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., and Gal, Y.",
          " \\newblock AI models collapse when trained on recursively generated data.",
          "-\\newblock {\\em Nature}, 631:755--759.",
          "+\\newblock {\\em Nature}, 631:755--759, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Alemohammad et al.}2024]{alemohammad2024selfconsuming}",
          "-Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G.\\ Baraniuk. 2024.",
          "+\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}",
          "+Alemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A.~I., Babaei, H., LeJeune, D., Siahkoohi, A., and Baraniuk, R.~G.",
          " \\newblock Self-consuming generative models go MAD.",
          "-\\newblock In {\\em ICLR 2024}.",
          "+\\newblock In {\\em ICLR}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Dohmatob et al.}2024]{dohmatob2024tale}",
          "-Elvis Dohmatob, Yunzhen Feng, and Julia Kempe. 2024.",
          "+\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}",
          "+Dohmatob, E., Feng, Y., and Kempe, J.",
          " \\newblock A tale of tails: Model collapse as a change of scaling laws.",
          "-\\newblock In {\\em ICML 2024}.",
          "+\\newblock In {\\em ICML}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Gerstgrasser et al.}2024]{gerstgrasser2024model}",
          "-Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A.\\ Roberts, Diyi Yang, David L.\\ Donoho, and Sanmi Koyejo. 2024.",
          "+\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}",
          "+Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Sleight, H., Hughes, J., Korbak, T., Agrawal, R., Pai, D., Gromov, A., Roberts, D.~A., Yang, D., Donoho, D.~L., and Koyejo, S.",
          " \\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.",
          "-\\newblock {\\em arXiv preprint arXiv:2404.01413}.",
          "+\\newblock {\\em arXiv:2404.01413}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Seddik et al.}2024]{seddik2024sigma}",
          "-Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, and Merouane Debbah. 2024.",
          "+\\bibitem[Seddik et~al.(2024)]{seddik2024sigma}",
          "+Seddik, M.~E.~A., Chen, S.-W., Hayou, S., Youssef, P., and Debbah, M.",
          " \\newblock How bad is training on synthetic data? A statistical analysis of language model collapse.",
          "-\\newblock {\\em arXiv preprint arXiv:2404.05090}.",
          "+\\newblock {\\em arXiv:2404.05090}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Kazdan et al.}2024]{kazdan2024collapseqa}",
          "-Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, and Tomasz Korbak. 2024.",
          "+\\bibitem[Kazdan et~al.(2024)]{kazdan2024collapseqa}",
          "+Kazdan, J., Schaeffer, R., Dey, A., Gerstgrasser, M., Rafailov, R., and Korbak, T.",
          " \\newblock Collapse or thrive? Perils and promises of synthetic data in a self-generating world.",
          "-\\newblock {\\em arXiv preprint arXiv:2404.01222}.",
          "+\\newblock {\\em arXiv:2404.01222}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Briesch et al.}2023]{briesch2023large}",
          "-Martin Briesch, Dominik Sobania, and Franz Rothlauf. 2023.",
          "+\\bibitem[Briesch et~al.(2023)]{briesch2023large}",
          "+Briesch, M., Sobania, D., and Rothlauf, F.",
          " \\newblock Large language models suffer from their own output: An analysis of the self-consuming training loop.",
          "-\\newblock {\\em arXiv preprint arXiv:2311.16822}.",
          "+\\newblock {\\em arXiv:2311.16822}, 2023.",
          " ",
          "-\\bibitem[\\protect\\citename{Hataya et al.}2023]{hataya2023will}",
          "-Ryuichiro Hataya, Han Bao, and Hiromi Arai. 2023.",
          "+\\bibitem[Hataya et~al.(2023)]{hataya2023will}",
          "+Hataya, R., Bao, H., and Arai, H.",
          " \\newblock Will large-scale generative models corrupt future datasets?",
          "-\\newblock In {\\em ICCV 2023}.",
          "+\\newblock In {\\em ICCV}, 2023.",
          " ",
          "-\\bibitem[\\protect\\citename{Kalinowski}2024]{kalinowski2024tda}",
          "-Thomas Kalinowski. 2024.",
          "+\\bibitem[Kalinowski(2024)]{kalinowski2024tda}",
          "+Kalinowski, T.",
          " \\newblock Topological analysis of model collapse in language models.",
          "-\\newblock {\\em arXiv preprint arXiv:2406.00123}.",
          "+\\newblock {\\em arXiv:2406.00123}, 2024.",
          " ",
          "-\\bibitem[\\protect\\citename{Pennington and Worah}2017]{pennington2017nonlinear}",
          "-Jeffrey Pennington and Pratik Worah. 2017.",
          "+\\bibitem[Pennington and Worah(2017)]{pennington2017nonlinear}",
          "+Pennington, J. and Worah, P.",
          " \\newblock Nonlinear random matrix theory for deep learning.",
          "-\\newblock In {\\em NeurIPS 2017}.",
          "+\\newblock In {\\em NeurIPS}, 2017.",
          " ",
          " \\end{thebibliography}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2919f8e5-19e5-4b24-b292-8706a94ede32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_…",
  "leafUuid": "9ccbf0ad-69e9-4d42-ad65-5c2f30754d34",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Tool call

_source line 44 · 2026-05-16T10:19:20.109Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Te7KGLdrPF63aqaaFPG7Sg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ccbf0ad-69e9-4d42-ad65-5c2f30754d34",
  "isSidechain": false,
  "requestId": "req_011Cb65UnFo1gWycEextfAyJ",
  "type": "assistant",
  "uuid": "d29d9ba9-c6ed-456c-a0a6-7ceccaeca881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MkFoo8GYMRTNz98U3DJXA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2336,
      "cache_read_input_tokens": 66434,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 66434,
          "cache_creation_input_tokens": 2336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2336
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

_source line 45 · 2026-05-16T10:19:21.262Z_

<details><summary>↩ Tool result · `toolu_01Te7KGLdrPF63aqaaFPG7Sg`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (0.1982pt too wide) in paragraph at lines 22--23
[]\OT1/ptm/m/n/10 Model col-lapse from it-er-a-tive train-ing on syn-thetic dat
a poses a grow-ing threat as LLM-generated

Package natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input
 line 27.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef
ined on input line 27.


Package natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu
t line 27.


Package natbib Warning: Citation `seddik2024sigma' on page 1 undefined on input
 line 29.


Package natbib Warning: Citation `kalinowski2024tda' on page 1 undefined on inp
ut line 29.


Package natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on
 input line 29.


Package natbib Warning: Citation `kazdan2024collapseqa' on page 1 undefined on 
input line 29.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `shumailov2024ai' on page 2 undefined on input
 line 43.


Package natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef
ined on input line 43.


Package natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu
t line 43.


Package natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on
 input line 43.


Package natbib Warning: Citation `briesch2023large' on page 2 undefined on inpu
t line 45.


Package natbib Warning: Citation `hataya2023will' on page 2 undefined on input 
line 45.


Package natbib Warning: Citation `seddik2024sigma' on page 2 undefined on input
 line 45.


Package natbib Warning: Citation `pennington2017nonlinear' on page 2 undefined 
on input line 45.


Overfull \hbox (3.56317pt too wide) in paragraph at lines 53--54
\OT1/ptm/m/n/10.95 the orig-i-nal train-ing cor-pus at a spec-i-fied con-tam-i-
na-tion frac-tion $\OML/cmm/m/it/10.95 f \OMS/cmsy/m/n/10.95 2 f\OT1/cmr/m/n/10
.95 0%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 10%\OML/cmm/m/it/10.95 ; \OT1/cm
r/m/n/10.95 25%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 50%\OML/cmm/m/it/10.95 
; \OT1/cmr/m/n/10.95 75%\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 100%\OMS/cmsy/
m/n/10.95 g$\OT1/ptm/m/n/10.95 ;
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [2]
Overfull \hbox (44.8102pt too wide) in paragraph at lines 65--66
 []\OT1/ptm/b/n/10.95 Output fam-ily.[] \OT1/ptm/m/n/10.95 (3) \OT1/ptm/b/n/10.
95 Per-plex-ity\OT1/ptm/m/n/10.95 : $[]\OT1/cmr/m/n/10.95 ([])$ \OT1/ptm/m/n/10
.95 eval-u-ated on a fixed held-out val-i-da-tion set in \OT1/pcr/m/n/10.95 mod
el.eval()
[3]
Overfull \hbox (6.30812pt too wide) in paragraph at lines 147--148
[]\OT1/ptm/m/n/10.95 Critically, the within-generation and cross-generation rol
es are non-interchangeable. Cross-generation

Overfull \hbox (0.75163pt too wide) in paragraph at lines 171--172
\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r
ec-tion con-sis-tency be-tween Wiki-Text and PubMed
[4]
Overfull \hbox (14.9526pt too wide) in paragraph at lines 203--216
 [][] 
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5] [6]

Package natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on
 input line 347.

[7] [8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m
sam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 160887 bytes).
Transcript written on paper.log.
\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r
ec-tion con-sis-tency be-tween Wiki-Text and PubMed
[4]
Overfull \hbox (14.9526pt too wide) in paragraph at lines 203--216
 [][] 
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5] [6] [7] [8]
[9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m
sam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 161392 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d29d9ba9-c6ed-456c-a0a6-7ceccaeca881",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "1eaf495a-2cc8-4a01-a6cf-00cf52381bf2",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (0.1982pt too wide) in paragraph at lines 22--23\n[]\\OT1/ptm/m/n/10 Model col-lapse from it-er-a-tive train-ing on syn-thetic dat\na poses a grow-ing threat as LLM-generated\n\nPackage natbib Warning: Citation `shumailov2024ai' on page 1 undefined on input\n line 27.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef\nined on input line 27.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu\nt line 27.\n\n\nPackage natbib Warning: Citation `seddik2024sigma' on page 1 undefined on input\n line 29.\n\n\nPackage natbib Warning: Citation `kalinowski2024tda' on page 1 undefined on inp\nut line 29.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on\n input line 29.\n\n\nPackage natbib Warning: Citation `kazdan2024collapseqa' on page 1 undefined on \ninput line 29.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `shumailov2024ai' on page 2 undefined on input\n line 43.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef\nined on input line 43.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu\nt line 43.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on\n input line 43.\n\n\nPackage natbib Warning: Citation `briesch2023large' on page 2 undefined on inpu\nt line 45.\n\n\nPackage natbib Warning: Citation `hataya2023will' on page 2 undefined on input \nline 45.\n\n\nPackage natbib Warning: Citation `seddik2024sigma' on page 2 undefined on input\n line 45.\n\n\nPackage natbib Warning: Citation `pennington2017nonlinear' on page 2 undefined \non input line 45.\n\n\nOverfull \\hbox (3.56317pt too wide) in paragraph at lines 53--54\n\\OT1/ptm/m/n/10.95 the orig-i-nal train-ing cor-pus at a spec-i-fied con-tam-i-\nna-tion frac-tion $\\OML/cmm/m/it/10.95 f \\OMS/cmsy/m/n/10.95 2 f\\OT1/cmr/m/n/10\n.95 0%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 10%\\OML/cmm/m/it/10.95 ; \\OT1/cm\nr/m/n/10.95 25%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 50%\\OML/cmm/m/it/10.95 \n; \\OT1/cmr/m/n/10.95 75%\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 100%\\OMS/cmsy/\nm/n/10.95 g$\\OT1/ptm/m/n/10.95 ;\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [2]\nOverfull \\hbox (44.8102pt too wide) in paragraph at lines 65--66\n []\\OT1/ptm/b/n/10.95 Output fam-ily.[] \\OT1/ptm/m/n/10.95 (3) \\OT1/ptm/b/n/10.\n95 Per-plex-ity\\OT1/ptm/m/n/10.95 : $[]\\OT1/cmr/m/n/10.95 ([])$ \\OT1/ptm/m/n/10\n.95 eval-u-ated on a fixed held-out val-i-da-tion set in \\OT1/pcr/m/n/10.95 mod\nel.eval()\n[3]\nOverfull \\hbox (6.30812pt too wide) in paragraph at lines 147--148\n[]\\OT1/ptm/m/n/10.95 Critically, the within-generation and cross-generation rol\nes are non-interchangeable. Cross-generation\n\nOverfull \\hbox (0.75163pt too wide) in paragraph at lines 171--172\n\\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r\nec-tion con-sis-tency be-tween Wiki-Text and PubMed\n[4]\nOverfull \\hbox (14.9526pt too wide) in paragraph at lines 203--216\n [][] \n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5] [6]\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 7 undefined on\n input line 347.\n\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m\nsam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 160887 bytes).\nTranscript written on paper.log.\n\\OT1/ptm/m/n/10.95 generation-4 val-ues at 100% con-tam-i-na-tion. Sig-nal di-r\nec-tion con-sis-tency be-tween Wiki-Text and PubMed\n[4]\nOverfull \\hbox (14.9526pt too wide) in paragraph at lines 203--216\n [][] \n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [5] [6] [7] [8]\n[9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/m\nsam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 161392 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d29d9ba9-c6ed-456c-a0a6-7ceccaeca881",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-16T10:19:25.489Z_

PDF 编译成功（9 页，161KB）。只有一些 overfull hbox 警告和未定义引用的 natbib 警告（第三轮编译可解决，但不影响内容）。再跑一轮编译解决引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eaf495a-2cc8-4a01-a6cf-00cf52381bf2",
  "isSidechain": false,
  "requestId": "req_011Cb65V6383ZEzLssiq7tMY",
  "type": "assistant",
  "uuid": "f14fa806-b1ce-42ee-8b88-f1c5972abc1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LTETau1225F6cP9pWoG4N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4624,
      "cache_read_input_tokens": 68770,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 68770,
          "cache_creation_input_tokens": 4624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4624
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

_source line 47 · 2026-05-16T10:19:28.382Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012wqRJvZa7BShcEgXciHeuB`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Output written|Warning.*undefined|Error)\"",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f14fa806-b1ce-42ee-8b88-f1c5972abc1d",
  "isSidechain": false,
  "requestId": "req_011Cb65V6383ZEzLssiq7tMY",
  "type": "assistant",
  "uuid": "471c54fd-a107-47ad-9899-095819115ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LTETau1225F6cP9pWoG4N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4624,
      "cache_read_input_tokens": 68770,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 68770,
          "cache_creation_input_tokens": 4624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4624
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

_source line 48 · 2026-05-16T10:19:29.084Z_

<details><summary>↩ Tool result · `toolu_012wqRJvZa7BShcEgXciHeuB`</summary>

```text
Output written on paper.pdf (9 pages, 161392 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "471c54fd-a107-47ad-9899-095819115ec4",
  "isSidechain": false,
  "promptId": "b03bd37c-e8b6-482b-bfd7-079df9a0fa85",
  "type": "user",
  "uuid": "ea3edfd4-08fc-4d0e-b997-92f5c02b7f26",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (9 pages, 161392 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "471c54fd-a107-47ad-9899-095819115ec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-16T10:19:48.470Z_

编译完成，无未定义引用。

论文已写入 `best/paper.tex` 并编译为 `best/paper.pdf`（9 页）。覆盖了 experiment_data.json 中全部 12 个实验：

- **Table 1**: Within-gen AUROC（Claim 2 核心证据，含 0.5B/1.5B/PubMed 三配置）
- **Table 2**: Cross-scale signal comparison（0.5B vs 1.5B Cohen's d）
- **Table 3**: Spearman ρ per seed（6-fraction 单调性）
- **Table 4**: Step-level detection power（step 50/100/200/500 AUROC）
- **Table 5**: Cross-domain comparison（WikiText vs PubMed）
- **Table 6**: Signal taxonomy（7 信号 × 7 维度，含 method-dependence 列）
- **Table 7**: MMLU-mini across generations
- **Table 8**: Cross-scale 3-model comparison（含 3B spot-check）
- **Table 9**: Cross-family direction（LLaMA vs Qwen，10/11 一致）
- **Table 10**: Per-layer sub-module ΔSR
- **Table 11**: Recovery ratio by domain × signal
- Full FT vs QLoRA 对比 + 3-seed expansion 数据整合在 §4.4

SIGMA head-to-head（数据不足）降级为 Discussion 段落。所有数字来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea3edfd4-08fc-4d0e-b997-92f5c02b7f26",
  "isSidechain": false,
  "requestId": "req_011Cb65VfRJiLvTfifbU8QBM",
  "type": "assistant",
  "uuid": "75274898-c6f0-4c4d-8d49-494d579f5fc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/artifacts/dream_reports/dream_20260516T095632/best",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157U2paxvPgQBydMLdVizcK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 73394,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 206,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 412,
          "cache_read_input_tokens": 73394,
          "cache_creation_input_tokens": 206,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 206
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T095632 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_…",
  "leafUuid": "75274898-c6f0-4c4d-8d49-494d579f5fc3",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for collapse severity monitor",
  "sessionId": "54959dd4-c6b2-483d-8e01-175da7151411"
}
```

---
