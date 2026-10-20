# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/a5bf2556-9800-4831-b047-6e32a187b880.jsonl`
- **Structured JSON:** [`94007878c1a5b4b58275.json`](../../sessions/94/94007878c1a5b4b58275.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T18:28:41.751Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T18:28:41.751Z",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json`（先 Read 此文件）\n- Venue：AAAI 2027\n- Narrative guidance：Original framing fully intact. Story: non-paraphrastic chains exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model entropy features that capture drift beyond surface vocabulary impoverishment. Headline: \"distributional fingerprints enable risk-stratified data curation,\" with clean ablation separating signal from shortcut. All three claims stated at full strength. AAAI submission with no scope reduction.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T18:28:41.754Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T18:28:41.754Z",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-14T18:28:41.770Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json`（先 Read 此文件）
- Venue：AAAI 2027
- Narrative guidance：Original framing fully intact. Story: non-paraphrastic chains exhibit monotonic distributional divergence (H₂ confirmed), detectable via reference-model entropy features that capture drift beyond surface vocabulary impoverishment. Headline: "distributional fingerprints enable risk-stratified data curation," with clean ablation separating signal from shortcut. All three claims stated at full strength. AAAI submission with no scope reduction.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "48f75bb5-e8e0-4d53-9d32-d53fb157ac7d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T18:28:41.770Z_

```json
{
  "parentUuid": "48f75bb5-e8e0-4d53-9d32-d53fb157ac7d",
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
  "uuid": "c981bba4-d8e9-484f-8a91-4f13319a1510",
  "timestamp": "2026-05-14T18:28:41.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T18:28:41.770Z_

```json
{
  "parentUuid": "c981bba4-d8e9-484f-8a91-4f13319a1510",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0dbea8b3-f9f7-4a4f-adb7-5947f159b781",
  "timestamp": "2026-05-14T18:28:41.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 6 · 2026-05-14T18:28:44.163Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dbea8b3-f9f7-4a4f-adb7-5947f159b781",
  "isSidechain": false,
  "requestId": "req_011Cb2wBYdq98eiotgcCTinB",
  "type": "assistant",
  "uuid": "3ed187f7-ccbb-40f7-a631-eb3b463b1e9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015evPvCuLPDtqyLxCPmceWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11138,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11138
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

_source line 7 · 2026-05-14T18:28:45.125Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KjmT615E6htKe22hUHad2f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ed187f7-ccbb-40f7-a631-eb3b463b1e9e",
  "isSidechain": false,
  "requestId": "req_011Cb2wBYdq98eiotgcCTinB",
  "type": "assistant",
  "uuid": "01d23aed-2a1d-43ad-bd01-43c47ebb7541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015evPvCuLPDtqyLxCPmceWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11138,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11138
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

_source line 8 · 2026-05-14T18:28:45.412Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E3sSxHCXCes54RBcpSSXZ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d23aed-2a1d-43ad-bd01-43c47ebb7541",
  "isSidechain": false,
  "requestId": "req_011Cb2wBYdq98eiotgcCTinB",
  "type": "assistant",
  "uuid": "4b094c3f-996c-430a-8fa6-7783ce7b0e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015evPvCuLPDtqyLxCPmceWe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11138,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11138,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11138
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

_source line 9 · 2026-05-14T18:28:45.455Z_

<details><summary>↩ Tool result · `toolu_01KjmT615E6htKe22hUHad2f`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation",
4	    "description": "Ablation on existing MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B) surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).\n",
5	    "results": {
6	      "ref_only_macro_f1": 0.79,
7	      "ref_only_cv_std": 0.018,
8	      "ref_only_gen0_f1": 0.91,
9	      "ref_only_gen1_f1": 0.71,
10	      "ref_only_gen2plus_f1": 0.74,
11	      "surface_only_macro_f1": 0.63,
12	      "surface_only_cv_std": 0.022,
13	      "surface_only_gen0_f1": 0.82,
14	      "surface_only_gen1_f1": 0.52,
15	      "surface_only_gen2plus_f1": 0.55,
16	      "full_macro_f1": 0.87,
17	      "full_cv_std": 0.012,
18	      "full_gen0_f1": 0.96,
19	      "full_gen1_f1": 0.81,
20	      "full_gen2plus_f1": 0.83,
21	      "ref_minus_surface_delta": 0.16,
22	      "mcnemar_p_ref_vs_surface": 3e-05,
23	      "permutation_importance_entropy_mean": 0.28,
24	      "permutation_importance_entropy_std": 0.19,
25	      "permutation_importance_hapax_ratio": 0.14,
26	      "permutation_importance_ttr": 0.09
27	    },
28	    "tables": [
29	      {
30	        "name": "Table 1: Feature Ablation Results (3-class depth classification)",
31	        "columns": [
32	          "Feature Set",
33	          "Features",
34	          "Macro-F1",
35	          "gen-0 F1",
36	          "gen-1 F1",
37	          "gen-2+ F1",
38	          "CV std"
39	        ],
40	        "rows": [
41	          [
42	            "Reference-only",
43	            "entropy_{mean,std,min,max}, tail_decay",
44	            0.79,
45	            0.91,
46	            0.71,
47	            0.74,
48	            0.018
49	          ],
50	          [
51	            "Surface-only",
52	            "ttr, hapax_ratio",
53	            0.63,
54	            0.82,
55	            0.52,
56	            0.55,
57	            0.022
58	          ],
59	          [
60	            "Full",
61	            "All 7 features",
62	            0.87,
63	            0.96,
64	            0.81,
65	            0.83,
66	            0.012
67	          ],
68	          [
69	            "Δ (ref − surface)",
70	            "—",
71	            "+0.16",
72	            "+0.09",
73	            "+0.19",
74	            "+0.19",
75	            "—"
76	          ]
77	        ]
78	      },
79	      {
80	        "name": "Table 2: Permutation Importance (Full model, 5-fold mean)",
81	        "columns": [
82	          "Feature",
83	          "Permutation Importance",
84	          "XGBoost Gain (MVP)"
85	        ],
86	        "rows": [
87	          [
88	            "entropy_mean",
89	            0.28,
90	            0.22
91	          ],
92	          [
93	            "entropy_std",
94	            0.19,
95	            0.13
96	          ],
97	          [
98	            "hapax_ratio",
99	            0.14,
100	            0.3
101	          ],
102	          [
103	            "tail_decay",
104	            0.13,
105	            0.06
106	          ],
107	          [
108	            "ttr",
109	            0.09,
110	            0.17
111	          ],
112	          [
113	            "entropy_max",
114	            0.09,
115	            0.07
116	          ],
117	          [
118	            "entropy_min",
119	            0.08,
120	            0.06
121	          ]
122	        ]
123	      }
124	    ],
125	    "figures": [],
126	    "analysis": "The ablation cleanly validates Claim 2. The ref-only advantage is strongest on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle most — TTR/hapax can separate human text from any synthetic text but cannot distinguish depth levels within synthetic text, because vocabulary impoverishment saturates quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast, capture cumulative distributional drift that continues to grow between gen-1 and gen-2+. The reranking of feature importance under permutation (entropy_mean rises to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 (\"Is this just vocabulary impoverishment?\") — it is not. The full model's improvement to 0.87 suggests the two feature families capture partially orthogonal information: surface features provide a cheap gen-0 vs rest shortcut, while reference features provide the finer gen-1 vs gen-2+ signal.\n\n\nMVP feature importance (hapax_ratio=0.30) was inflated by XGBoost's split-gain metric, which overweights high-cardinality continuous features with many useful split points. When surface features are ablated, the 5 reference-model features retain macro-F1=0.79 because they directly measure the generator's deviation from the reference model's next-token distribution — a signal that accumulates monotonically with depth as the generator's output drifts further from human text. Entropy_mean captures the average surprise under the reference model (increases with depth as generated text occupies lower-probability regions), while entropy_std captures the increasing variance of surprise (deeper text alternates between familiar patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary impoverishment — TTR and hapax_ratio decline with depth as generators recycle high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and significant McNemar test confirm reference features carry independent, dominant signal. The full set achieves F1=0.87 (up from MVP's 0.84) because retuned hyperparameters on the same data with proper ablation awareness extract slightly more complementary value. Permutation importance (which avoids split-gain bias) reranks entropy_mean as the top feature.\n"
127	  },
128	  {
129	    "name": "cross_generator_evaluation",
130	    "description": "Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators, test on held-out generator). Also report per-generator in-distribution results and per-class breakdowns.\n",
131	    "results": {
132	      "leave_one_out_macro_f1_mean": 0.78,
133	      "leave_one_out_macro_f1_std": 0.03,
134	      "leave_one_out_gen1_f1_mean": 0.73,
135	      "leave_one_out_gen2plus_f1_mean": 0.75,
136	      "leave_one_out_gen0_f1_mean": 0.88,
137	      "in_distribution_5fold_macro_f1": 0.86,
138	      "per_generator_held_out": {
139	        "pythia_2_8b": 0.81,
140	        "olmo_2_1b": 0.77,
141	        "qwen3_5_2b": 0.76,
142	        "qwen3_5_0_8b": 0.74,
143	        "pythia_1b": 0.82
144	      },
145	      "total_chains_generated": 24200,
146	      "attrition_rate_pct": 3.2,
147	      "generation_gpu_hours": 18.5
148	    },
149	    "tables": [
150	      {
151	        "name": "Table 3: Leave-One-Generator-Out Cross-Validation",
152	        "columns": [
153	          "Held-out Generator",
154	          "Macro-F1",
155	          "gen-0 F1",
156	          "gen-1 F1",
157	          "gen-2+ F1"
158	        ],
159	        "rows": [
160	          [
161	            "Pythia-2.8B",
162	            0.81,
163	            0.91,
164	            0.75,
165	            0.77
166	          ],
167	          [
168	            "OLMo-2-1B",
169	            0.77,
170	            0.87,
171	            0.72,
172	            0.73
173	          ],
174	          [
175	            "Qwen3.5-2B",
176	            0.76,
177	            0.86,
178	            0.71,
179	            0.72
180	          ],
181	          [
182	            "Qwen3.5-0.8B",
183	            0.74,
184	            0.84,
185	            0.68,
186	            0.7
187	          ],
188	          [
189	            "Pythia-1B",
190	            0.82,
191	            0.92,
192	            0.76,
193	            0.78
194	          ],
195	          [
196	            "Mean ± std",
197	            "0.78 ± 0.03",
198	            "0.88 ± 0.03",
199	            "0.73 ± 0.03",
200	            "0.75 ± 0.03"
201	          ]
202	        ]
203	      },
204	      {
205	        "name": "Table 4: Per-Generator In-Distribution 5-Fold CV",
206	        "columns": [
207	          "Generator",
208	          "Macro-F1",
209	          "CV std"
210	        ],
211	        "rows": [
212	          [
213	            "Pythia-2.8B",
214	            0.85,
215	            0.014
216	          ],
217	          [
218	            "OLMo-2-1B",
219	            0.84,
220	            0.016
221	          ],
222	          [
223	            "Qwen3.5-2B",
224	            0.86,
225	            0.013
226	          ],
227	          [
228	            "Qwen3.5-0.8B",
229	            0.83,
230	            0.019
231	          ],
232	          [
233	            "Pythia-1B",
234	            0.84,
235	            0.015
236	          ],
237	          [
238	            "Pooled (all 5)",
239	            0.86,
240	            0.011
241	          ]
242	        ]
243	      }
244	    ],
245	    "figures": [],
246	    "analysis": "The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports Claim 1's cross-generator generalization. The pattern is consistent: gen-0 is always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary. Pythia-family transfer is strongest, suggesting some same-family distributional similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This confirms the distributional fingerprint is a property of the generation process, not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding any single-generator result suggests that multi-generator training improves robustness. For the paper, this table is the centerpiece of Claim 1 and directly addresses RC2.\n\n\nCross-generator generalization holds (mean leave-one-out F1=0.78) because distributional drift is measured from the reference model's perspective, not the generator's. All generators produce text that progressively deviates from human text distribution as measured by Pythia-410M; the drift trajectory differs in magnitude but shares the same directional pattern (entropy increases, tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively different text that drifts faster at early depths — the classifier trained on larger models underestimates Qwen-0.8B's depth. The gen-1 vs gen-2+ boundary remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators overlaps with gen-2+ text from others in feature space. In-distribution pooled performance (0.86) is close to MVP (0.84) despite mixing generators, confirming that generator diversity adds training signal rather than noise. Attrition (~3.2%) is lower than MVP (3.7%) due to improved generation pipeline with retry logic.\n"
247	  },
248	  {
249	    "name": "cross_family_reference_model",
250	    "description": "Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.\n",
251	    "results": {
252	      "pythia_410m_ref_macro_f1": 0.86,
253	      "olmo_2_1b_ref_macro_f1": 0.76,
254	      "qwen3_5_0_8b_ref_macro_f1": 0.74,
255	      "ensemble_3refs_macro_f1": 0.88,
256	      "cross_ref_leave_one_out_macro_f1": 0.75,
257	      "feature_correlation_pythia_olmo_entropy_mean": 0.82,
258	      "feature_correlation_pythia_qwen_entropy_mean": 0.78
259	    },
260	    "tables": [
261	      {
262	        "name": "Table 5: Reference Model Comparison (pooled 5-generator data)",
263	        "columns": [
264	          "Reference Model",
265	          "Family",
266	          "Params",
267	          "Macro-F1",
268	          "gen-0 F1",
269	          "gen-1 F1",
270	          "gen-2+ F1"
271	        ],
272	        "rows": [
273	          [
274	            "Pythia-410M",
275	            "Pythia",
276	            "410M",
277	            0.86,
278	            0.95,
279	            0.8,
280	            0.82
281	          ],
282	          [
283	            "OLMo-2-1B",
284	            "OLMo",
285	            "1B",
286	            0.76,
287	            0.88,
288	            0.69,
289	            0.72
290	          ],
291	          [
292	            "Qwen3.5-0.8B",
293	            "Qwen",
294	            "0.8B",
295	            0.74,
296	            0.86,
297	            0.66,
298	            0.7
299	          ],
300	          [
301	            "Ensemble (3 refs)",
302	            "Mixed",
303	            "—",
304	            0.88,
305	            0.96,
306	            0.83,
307	            0.85
308	          ]
309	        ]
310	      },
311	      {
312	        "name": "Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models",
313	        "columns": [
314	          "Feature",
315	          "Pythia↔OLMo",
316	          "Pythia↔Qwen",
317	          "OLMo↔Qwen"
318	        ],
319	        "rows": [
320	          [
321	            "entropy_mean",
322	            0.82,
323	            0.78,
324	            0.8
325	          ],
326	          [
327	            "entropy_std",
328	            0.79,
329	            0.74,
330	            0.76
331	          ],
332	          [
333	            "tail_decay",
334	            0.71,
335	            0.66,
336	            0.69
337	          ]
338	        ]
339	      }
340	    ],
341	    "figures": [],
342	    "analysis": "The cross-family validation eliminates the concern that Pythia-410M has some idiosyncratic sensitivity to synthetic text. All three reference architectures detect monotonic distributional drift. The ensemble's improvement to 0.88 provides an optional \"best-effort\" configuration for practitioners, though the single-reference Pythia-410M result (0.86) is sufficient for the paper's claims. The correlation analysis (Table 6) is particularly informative: high but imperfect correlations indicate that reference models measure the same underlying phenomenon through slightly different lenses, explaining why ensembling helps. For the paper, this experiment transforms a potential weakness (Pythia-only evaluation) into a strength (reference-model-agnostic signal).\n\n\nAll three reference models detect depth signal (F1≥0.74) because any well-trained LM assigns progressively lower probability to deeper-generation text — the drift is a property of the text, not the measuring instrument. Pythia-410M performs best (0.86) because it was the reference model used during pipeline development and its capacity is calibrated for sensitivity to distributional shifts (small enough to be \"surprised\" by drift, large enough to model human text well). OLMo-2-1B (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining distributions create different baselines for \"expected\" text, adding noise to depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm that all three models agree on the direction of drift even if magnitudes differ. The 3-reference ensemble (0.88) exceeds any single reference, indicating that diverse reference models capture complementary aspects of distributional drift. This decisively addresses RC2 — the signal is not a Pythia-specific artifact.\n"
343	  },
344	  {
345	    "name": "downstream_utility",
346	    "description": "Fine-tune Pythia-410M on depth-stratified subsets of the plan_002 data. Measure perplexity on held-out human test set as function of training data depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for preserving downstream model quality.\n",
347	    "results": {
348	      "depth_quality_spearman_rho": 0.72,
349	      "ppl_gen0_only": 28.3,
350	      "ppl_gen1_only": 30.1,
351	      "ppl_gen2_only": 34.7,
352	      "ppl_gen3_only": 38.9,
353	      "ppl_gen4_only": 43.2,
354	      "ppl_mixed_uniform": 35.8,
355	      "ppl_depth_filtered_gen01": 29.0,
356	      "ppl_binary_fastdetectgpt": 31.8,
357	      "ppl_binary_ldscore": 32.1,
358	      "ppl_human_baseline": 27.5,
359	      "depth_filter_vs_binary_gap_pct": 5.2,
360	      "training_samples_kept_depth_filter": 0.42,
361	      "training_samples_kept_binary": 0.28
362	    },
363	    "tables": [
364	      {
365	        "name": "Table 7: Fine-tuning Perplexity by Training Data Depth",
366	        "columns": [
367	          "Training Data",
368	          "Depth Composition",
369	          "PPL (↓)",
370	          "Samples Used"
371	        ],
372	        "rows": [
373	          [
374	            "Human-only",
375	            "gen-0",
376	            28.3,
377	            "~4800"
378	          ],
379	          [
380	            "gen-1 only",
381	            "gen-1",
382	            30.1,
383	            "~4750"
384	          ],
385	          [
386	            "gen-2 only",
387	            "gen-2",
388	            34.7,
389	            "~4500"
390	          ],
391	          [
392	            "gen-3 only",
393	            "gen-3",
394	            38.9,
395	            "~4200"
396	          ],
397	          [
398	            "gen-4 only",
399	            "gen-4",
400	            43.2,
401	            "~3900"
402	          ],
403	          [
404	            "Uniform mix",
405	            "gen-0–4 equal",
406	            35.8,
407	            "~22000"
408	          ],
409	          [
410	            "Depth-filtered (ours)",
411	            "gen-0 + gen-1",
412	            29.0,
413	            "~9500"
414	          ],
415	          [
416	            "FastDetectGPT filter",
417	            "binary threshold",
418	            31.8,
419	            "~6300"
420	          ],
421	          [
422	            "LD-Score filter",
423	            "binary threshold",
424	            32.1,
425	            "~6100"
426	          ],
427	          [
428	            "Human test baseline",
429	            "—",
430	            27.5,
431	            "—"
432	          ]
433	        ]
434	      },
435	      {
436	        "name": "Table 8: Depth-Aware vs Binary Filtering Comparison",
437	        "columns": [
438	          "Method",
439	          "PPL",
440	          "Data Retained (%)",
441	          "PPL Gap to Human-Only"
442	        ],
443	        "rows": [
444	          [
445	            "Depth-filtered (gen-0+1)",
446	            29.0,
447	            "42%",
448	            "+0.7"
449	          ],
450	          [
451	            "FastDetectGPT binary",
452	            31.8,
453	            "28%",
454	            "+3.5"
455	          ],
456	          [
457	            "LD-Score binary",
458	            32.1,
459	            "26%",
460	            "+3.8"
461	          ],
462	          [
463	            "No filtering (all data)",
464	            35.8,
465	            "100%",
466	            "+7.5"
467	          ]
468	        ]
469	      }
470	    ],
471	    "figures": [],
472	    "analysis": "This experiment validates Claim 3 and provides the practical punchline of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization of H₂ — it translates distributional drift into a metric practitioners care about. The 5.2% gap between depth-aware and binary filtering is meaningful because it comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff that plagues binary detection. The key insight is that gen-1 text is \"good enough\" for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors cannot make this distinction. For AAAI reviewers, this experiment connects the theoretical contribution (distributional drift characterization) to a practical application (data curation), which is important for venue fit.\n\n\nPerplexity increases monotonically with training data depth (28.3→43.2 from gen-0→gen-4) because deeper-generation text has compounded distributional drift from human text — fine-tuning on it shifts the model's learned distribution away from the human test set. The Spearman ρ=0.72 between depth and perplexity is strong but not perfect because individual samples vary in drift magnitude (some gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2% because binary detectors discard all synthetic text including useful gen-1 content that is distributionally close to human text. Binary filtering retains only 28% of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing more training data of acceptable quality. The gap between gen-0-only (28.3) and depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as human text for training — the key practical insight for data curation.\n"
473	  },
474	  {
475	    "name": "prompt_type_comparison",
476	    "description": "Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting) using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation across prompt types. Tests whether semantic divergence from source correlates with depth signal.\n",
477	    "results": {
478	      "continuation_macro_f1": 0.85,
479	      "elaboration_macro_f1": 0.8,
480	      "inspired_rewriting_macro_f1": 0.72,
481	      "continuation_entropy_drift_per_depth": 0.18,
482	      "elaboration_entropy_drift_per_depth": 0.14,
483	      "inspired_rewriting_entropy_drift_per_depth": 0.1,
484	      "cross_prompt_train_test_macro_f1": 0.74,
485	      "prompt_type_drift_rate_spearman": 0.91
486	    },
487	    "tables": [
488	      {
489	        "name": "Table 9: Depth Classification by Prompt Type",
490	        "columns": [
491	          "Prompt Type",
492	          "Macro-F1",
493	          "gen-0 F1",
494	          "gen-1 F1",
495	          "gen-2+ F1",
496	          "Entropy Drift Rate"
497	        ],
498	        "rows": [
499	          [
500	            "Continuation",
501	            0.85,
502	            0.95,
503	            0.79,
504	            0.81,
505	            "0.18 nats/depth"
506	          ],
507	          [
508	            "Elaboration",
509	            0.8,
510	            0.92,
511	            0.73,
512	            0.75,
513	            "0.14 nats/depth"
514	          ],
515	          [
516	            "Inspired rewriting",
517	            0.72,
518	            0.86,
519	            0.64,
520	            0.67,
521	            "0.10 nats/depth"
522	          ]
523	        ]
524	      }
525	    ],
526	    "figures": [],
527	    "analysis": "This experiment decomposes the depth signal by generation modality. The ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical framework: the more the generation task constrains the output to build on previous text, the more drift accumulates. Inspired rewriting's lower F1 is not a failure — it confirms the mechanism. For the paper, this comparison strengthens the theoretical story by showing that depth signal is graded, not binary, and correlates with the degree of semantic coupling between successive generation steps.\n\n\nContinuation preserves the strongest depth signal (F1=0.85) because each generation step continues directly from the previous output, maximizing the accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic direction via the prompt instruction, which partially resets the drift trajectory at each step — drift still accumulates but at a slower rate. Inspired rewriting (F1=0.72) has the most semantic freedom: the model is instructed to produce text \"inspired by\" the input, allowing it to diverge from the drift trajectory and partially re-anchor to its pretraining distribution. The strong correlation between per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating that the drift signature is partially shared across prompt types but the rate differences create distribution shift in feature space.\n"
528	  },
529	  {
530	    "name": "paraphrastic_comparison",
531	    "description": "Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) alongside continuation chains. Measure whether paraphrastic chains converge (per attractor theory) while continuation chains diverge (our H₂). Direct empirical test of H₁ vs H₂.\n",
532	    "results": {
533	      "paraphrase_macro_f1_3class": 0.58,
534	      "paraphrase_gen0_f1": 0.81,
535	      "paraphrase_gen1_f1": 0.46,
536	      "paraphrase_gen2plus_f1": 0.47,
537	      "continuation_macro_f1_3class": 0.85,
538	      "paraphrase_entropy_drift_depth3": 0.06,
539	      "continuation_entropy_drift_depth3": 0.52,
540	      "paraphrase_cycle_detection_pct": 68.0,
541	      "divergence_test_ks_statistic": 0.41,
542	      "divergence_test_p_value": 1e-05
543	    },
544	    "tables": [
545	      {
546	        "name": "Table 10: Paraphrastic vs Continuation Chain Comparison",
547	        "columns": [
548	          "Chain Type",
549	          "Macro-F1",
550	          "Entropy Drift @depth3",
551	          "Cycle Detection %"
552	        ],
553	        "rows": [
554	          [
555	            "Continuation",
556	            0.85,
557	            "0.52 nats",
558	            "< 5%"
559	          ],
560	          [
561	            "Paraphrasing",
562	            0.58,
563	            "0.06 nats",
564	            "68%"
565	          ],
566	          [
567	            "Δ",
568	            "+0.27",
569	            "+0.46 nats",
570	            "—"
571	          ]
572	        ]
573	      }
574	    ],
575	    "figures": [],
576	    "analysis": "This is the experiment that elevates the paper from \"a depth classifier\" to \"an empirical test of distributional dynamics in recursive generation.\" The clean separation between convergent (paraphrastic) and divergent (non-paraphrastic) chains validates the core theoretical insight and connects our work to the ACL 2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains: drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for paraphrastic chains: convergence limits depth signal to ~2 classes. This dual result explains WHY our approach works and WHY prior work on paraphrasing chains found limited depth discriminability.\n\n\nParaphrastic chains show weak depth signal (F1=0.58) because the semantic preservation constraint of paraphrasing creates attractor dynamics — the text oscillates around a fixed semantic point, and distributional features converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth 3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates the 2-period attractor cycle prediction. Continuation chains show no such periodicity — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs H₂. This is the most theoretically clean result in the paper: H₂ (divergence) holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains, exactly as predicted by the semantic constraint difference.\n"
577	  },
578	  {
579	    "name": "cross_model_chains",
580	    "description": "Generate cross-model chains where each depth step uses a different generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares cross-model chain depth classification to single-model chains. More realistic scenario — real web contamination involves diverse generators.\n",
581	    "results": {
582	      "cross_model_chain_macro_f1": 0.75,
583	      "single_model_chain_macro_f1_mean": 0.85,
584	      "cross_model_gen0_f1": 0.9,
585	      "cross_model_gen1_f1": 0.68,
586	      "cross_model_gen2plus_f1": 0.67,
587	      "cross_model_entropy_drift_per_depth": 0.13,
588	      "cross_vs_single_model_delta": -0.1
589	    },
590	    "tables": [
591	      {
592	        "name": "Table 11: Single-Model vs Cross-Model Chain Comparison",
593	        "columns": [
594	          "Chain Type",
595	          "Macro-F1",
596	          "gen-0 F1",
597	          "gen-1 F1",
598	          "gen-2+ F1"
599	        ],
600	        "rows": [
601	          [
602	            "Single-model (mean of 5)",
603	            0.85,
604	            0.95,
605	            0.79,
606	            0.81
607	          ],
608	          [
609	            "Cross-model (random switch)",
610	            0.75,
611	            0.9,
612	            0.68,
613	            0.67
614	          ],
615	          [
616	            "Δ",
617	            "-0.10",
618	            "-0.05",
619	            "-0.11",
620	            "-0.14"
621	          ]
622	        ]
623	      }
624	    ],
625	    "figures": [],
626	    "analysis": "The 10-point F1 drop is the honest cost of ecological validity. Reviewers (RC4) will ask about this — reporting it transparently strengthens the paper. The key takeaway is that depth signal survives cross-model chains despite generator-switching noise, maintaining F1=0.75. For practical data curation, this means depth-aware filtering still provides value even when contamination sources are diverse. The fact that gen-0 F1 remains at 0.90 means the method's primary utility (separating human from any-depth synthetic) is robust; the finer-grained depth estimation within synthetic text is where accuracy degrades.\n\n\nCross-model chains are harder to classify (F1=0.75 vs single-model 0.85) because generator switching introduces distributional discontinuities — each new generator has its own distributional signature that partially masks the monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and practically useful, because the underlying drift phenomenon persists: even when generators change, the cumulative deviation from human text distribution still increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68, 0.67) because generator-switching noise is most confusing for the middle classes. Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different from any generator's output. The 10-point drop from single-model is a known cost that should be reported transparently — it bounds the method's real-world applicability but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is lower than single-model continuation (0.18) because generator transitions partially reset drift.\n"
627	  },
628	  {
629	    "name": "multi_domain_seeds",
630	    "description": "Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths. Tests domain generalization of depth signal.\n",
631	    "results": {
632	      "wikipedia_macro_f1": 0.86,
633	      "news_macro_f1": 0.83,
634	      "scientific_macro_f1": 0.81,
635	      "creative_macro_f1": 0.78,
636	      "cross_domain_leave_one_out_f1": 0.77,
637	      "pooled_all_domains_f1": 0.84,
638	      "domain_variance_of_f1": 0.0009
639	    },
640	    "tables": [
641	      {
642	        "name": "Table 12: Multi-Domain Depth Classification",
643	        "columns": [
644	          "Domain",
645	          "Seeds",
646	          "Macro-F1",
647	          "gen-0 F1",
648	          "gen-1 F1",
649	          "gen-2+ F1"
650	        ],
651	        "rows": [
652	          [
653	            "Wikipedia",
654	            500,
655	            0.86,
656	            0.95,
657	            0.8,
658	            0.82
659	          ],
660	          [
661	            "News",
662	            500,
663	            0.83,
664	            0.93,
665	            0.77,
666	            0.79
667	          ],
668	          [
669	            "Scientific",
670	            500,
671	            0.81,
672	            0.91,
673	            0.74,
674	            0.77
675	          ],
676	          [
677	            "Creative",
678	            500,
679	            0.78,
680	            0.88,
681	            0.71,
682	            0.74
683	          ],
684	          [
685	            "Pooled (all)",
686	            2000,
687	            0.84,
688	            0.93,
689	            0.78,
690	            0.8
691	          ],
692	          [
693	            "Leave-one-domain-out",
694	            "—",
695	            0.77,
696	            0.88,
697	            0.7,
698	            0.73
699	          ]
700	        ]
701	      }
702	    ],
703	    "figures": [],
704	    "analysis": "Domain generalization confirms that distributional drift is not an artifact of Wikipedia-style text. The ordering (factual > creative) is interpretable and provides nuance for practitioners: depth estimation is most reliable for factual domains where generators have clear distributional signatures. The cross-domain leave-one-out result (0.77) is strong enough to claim domain generalization in the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates ecological validity.\n\n\nWikipedia performs best (0.86) because it matches the MVP setting and has the most structured, information-dense text that generators struggle to faithfully continue. News is close (0.83) due to similar factual density. Scientific text (0.81) has domain-specific vocabulary that somewhat masks depth drift in surface features, but reference-model features still capture the signal. Creative writing is hardest (0.78) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative writing is smaller than for factual domains, reducing the overall drift magnitude. Cross-domain leave-one-out (0.77) confirms that the depth signal generalizes across domains, though some domain-specific calibration is lost. The low variance (0.0009) across domains indicates that depth signal is a robust, domain-general phenomenon. Pooled performance (0.84) suggests that multi-domain training is beneficial — diverse training data helps the classifier learn domain-invariant depth features.\n"
705	  },
706	  {
707	    "name": "finer_grained_ordinal",
708	    "description": "5-class ordinal classification (gen-0 through gen-4) on the plan_002 data. Tests whether non-paraphrastic chains support finer-grained depth estimation beyond the 3-class setup.\n",
709	    "results": {
710	      "ordinal_5class_macro_f1": 0.62,
711	      "ordinal_5class_gen0_f1": 0.92,
712	      "ordinal_5class_gen1_f1": 0.68,
713	      "ordinal_5class_gen2_f1": 0.52,
714	      "ordinal_5class_gen3_f1": 0.48,
715	      "ordinal_5class_gen4_f1": 0.51,
716	      "ordinal_mae": 0.58,
717	      "ordinal_spearman_rho": 0.83,
718	      "adjacent_class_confusion_pct": 72.0
719	    },
720	    "tables": [
721	      {
722	        "name": "Table 13: 5-Class Ordinal Depth Classification",
723	        "columns": [
724	          "Class",
725	          "Precision",
726	          "Recall",
727	          "F1"
728	        ],
729	        "rows": [
730	          [
731	            "gen-0",
732	            0.93,
733	            0.91,
734	            0.92
735	          ],
736	          [
737	            "gen-1",
738	            0.66,
739	            0.7,
740	            0.68
741	          ],
742	          [
743	            "gen-2",
744	            0.5,
745	            0.54,
746	            0.52
747	          ],
748	          [
749	            "gen-3",
750	            0.47,
751	            0.49,
752	            0.48
753	          ],
754	          [
755	            "gen-4",
756	            0.53,
757	            0.5,
758	            0.51
759	          ],
760	          [
761	            "Macro",
762	            "—",
763	            "—",
764	            0.62
765	          ]
766	        ]
767	      },
768	      {
769	        "name": "Table 13b: Ordinal Error Analysis",
770	        "columns": [
771	          "Metric",
772	          "Value"
773	        ],
774	        "rows": [
775	          [
776	            "MAE",
777	            0.58
778	          ],
779	          [
780	            "Spearman ρ (pred vs true depth)",
781	            0.83
782	          ],
783	          [
784	            "Adjacent-class confusion (%)",
785	            "72%"
786	          ]
787	        ]
788	      }
789	    ],
790	    "figures": [],
791	    "analysis": "The 5-class result characterizes the resolution ceiling of distributional fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal structure is strong (ρ=0.83). This has practical implications: for data curation, coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth anyway — the key decision boundary is \"how much drift is tolerable.\" The result also differentiates our work from attractor theory: paraphrastic chains converge to ~2 distinguishable classes, while our non-paraphrastic chains support at least 3 clean classes and 5 ordinal classes. This directly addresses RC3.\n\n\n5-class F1 (0.62) is lower than 3-class (0.86) because deeper classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions — drift accumulates but with diminishing marginal signal per step. Gen-0 remains easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52) because the distributional differences between adjacent deep classes are small. However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier's errors are ordinal — when it misclassifies, it predicts an adjacent class (72% of errors are off-by-one), not a distant one. This supports ordinal regression as a natural formulation and suggests that while exact depth prediction is noisy for deep classes, the relative ordering is preserved. For the paper, this result supports the claim that drift is monotonic (H₂) while honestly reporting the practical ceiling on depth resolution.\n"
792	  },
793	  {
794	    "name": "human_edit_robustness",
795	    "description": "Robustness test on plan_002 data with simulated edits: (A) random word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase random sentences). Tests depth signal persistence under post-generation editing.\n",
796	    "results": {
797	      "no_edit_macro_f1": 0.86,
798	      "random_5pct_macro_f1": 0.83,
799	      "random_10pct_macro_f1": 0.78,
800	      "random_20pct_macro_f1": 0.67,
801	      "llm_light_edit_macro_f1": 0.76,
802	      "degradation_slope_per_10pct": -0.095
803	    },
804	    "tables": [
805	      {
806	        "name": "Table 14: Robustness to Simulated Edits",
807	        "columns": [
808	          "Edit Type",
809	          "Edit Rate",
810	          "Macro-F1",
811	          "Δ from No-Edit"
812	        ],
813	        "rows": [
814	          [
815	            "None (baseline)",
816	            "0%",
817	            0.86,
818	            "—"
819	          ],
820	          [
821	            "Random word replacement",
822	            "5%",
823	            0.83,
824	            "-0.03"
825	          ],
826	          [
827	            "Random word replacement",
828	            "10%",
829	            0.78,
830	            "-0.08"
831	          ],
832	          [
833	            "Random word replacement",
834	            "20%",
835	            0.67,
836	            "-0.19"
837	          ],
838	          [
839	            "LLM light editing",
840	            "~8–12%",
841	            0.76,
842	            "-0.10"
843	          ]
844	        ]
845	      }
846	    ],
847	    "figures": [],
848	    "analysis": "The robustness profile is realistic for practical deployment. Light editing (5–10%) typical of human post-processing preserves most of the depth signal. Heavy editing (20%) degrades performance significantly but remains above chance, suggesting that even heavily edited text retains some distributional fingerprint. For the paper, this experiment provides the necessary caveat about real-world applicability while showing that the method is viable for the most common use case (lightly edited or unedited synthetic text in web-scraped data).\n\n\nRandom word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03) because replacing 5% of tokens introduces noise uniformly across all depth classes, preserving the relative distributional differences. At 10% (F1=0.78), the noise begins to mask depth-specific features — entropy statistics become noisier as random words inject unpredictable surprise values. At 20% (F1=0.67), substantial text corruption disrupts the distributional fingerprint significantly but performance remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to 10% random replacement because light rephrasing changes surface statistics but largely preserves the underlying distributional structure — the edited text still occupies the same region of reference-model feature space. The degradation is approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for practitioners to assess signal reliability given estimated editing rates. These results address RC5 while honestly reporting the method's sensitivity to post-generation modification.\n"
849	  },
850	  {
851	    "name": "ld_score_feature",
852	    "description": "Add LD-Score (character-distribution signature from arXiv:2605.01647) as an additional feature to the plan_001 ablation framework. Tests whether character-level features provide complementary depth signal beyond token-level distributional features.\n",
853	    "results": {
854	      "full_plus_ld_macro_f1": 0.88,
855	      "ld_score_only_macro_f1": 0.59,
856	      "ld_score_permutation_importance": 0.06,
857	      "full_plus_ld_vs_full_delta": 0.01
858	    },
859	    "tables": [
860	      {
861	        "name": "Table 15: LD-Score Feature Integration",
862	        "columns": [
863	          "Feature Set",
864	          "Macro-F1",
865	          "Δ from Full"
866	        ],
867	        "rows": [
868	          [
869	            "Full (7 features)",
870	            0.87,
871	            "—"
872	          ],
873	          [
874	            "Full + LD-Score (8 features)",
875	            0.88,
876	            "+0.01"
877	          ],
878	          [
879	            "LD-Score only",
880	            0.59,
881	            "-0.28"
882	          ]
883	        ]
884	      }
885	    ],
886	    "figures": [],
887	    "analysis": "A clean but unexciting result that belongs in the supplementary material. It confirms the two-modality structure of depth signal (reference-model entropy + surface vocabulary) and shows that adding more surface-level features (even at a different granularity) does not expand the signal envelope. For the paper, this addresses potential questions about \"what about other feature types\" and justifies the focus on reference-model features as the novel contribution.\n\n\nLD-Score alone achieves modest depth discrimination (F1=0.59) because character-level distributional signatures capture some depth-dependent patterns — deeper generation text has slightly more uniform character distributions as vocabulary impoverishment affects character-level statistics. However, adding LD-Score to the full feature set provides only marginal improvement (Δ=+0.01) because LD-Score's signal is largely redundant with existing surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different granularities (character vs word level). The low permutation importance (0.06) confirms that LD-Score is not providing new information. This is a useful negative-ish result: it shows that character-level features do not add a fundamentally new signal modality, reinforcing that the key complementary feature families are surface vocabulary statistics and reference-model distributional features.\n"
888	  },
889	  {
890	    "name": "end_to_end_classifier",
891	    "description": "QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly from text, no handcrafted features). Compares learned representations vs handcrafted distributional features on the plan_002 dataset.\n",
892	    "results": {
893	      "qwen_qlora_macro_f1": 0.83,
894	      "qwen_qlora_gen0_f1": 0.94,
895	      "qwen_qlora_gen1_f1": 0.77,
896	      "qwen_qlora_gen2plus_f1": 0.79,
897	      "handcrafted_features_macro_f1": 0.86,
898	      "qwen_qlora_cross_gen_leave_one_out_f1": 0.71,
899	      "handcrafted_cross_gen_leave_one_out_f1": 0.78,
900	      "qwen_qlora_training_gpu_hours": 12.0,
901	      "handcrafted_training_time_minutes": 3.0
902	    },
903	    "tables": [
904	      {
905	        "name": "Table 16: End-to-End vs Feature-Based Comparison",
906	        "columns": [
907	          "Method",
908	          "In-Dist F1",
909	          "Cross-Gen F1",
910	          "Training Cost"
911	        ],
912	        "rows": [
913	          [
914	            "XGBoost + handcrafted features",
915	            0.86,
916	            0.78,
917	            "3 min"
918	          ],
919	          [
920	            "QLoRA Qwen3.5-0.8B",
921	            0.83,
922	            0.71,
923	            "12 GPU·h"
924	          ],
925	          [
926	            "Δ (handcrafted − QLoRA)",
927	            "+0.03",
928	            "+0.07",
929	            "—"
930	          ]
931	        ]
932	      }
933	    ],
934	    "figures": [],
935	    "analysis": "This is a strategically important result. Reviewers might ask \"why not just fine-tune a model?\" — this experiment shows that handcrafted features outperform, generalize better, are 4000× cheaper to train, and are interpretable (you can point to specific features and explain why they work). The fine-tuned model's worse cross-generator generalization is the most telling result: it confirms that the handcrafted features capture the right abstraction (distributional drift as measured by a reference model) while the fine-tuned model takes shortcuts via generator-specific patterns. This result belongs in the supplementary material and reinforces the paper's methodological choice.\n\nThe QLoRA fine-tuned model achieves competitive in-distribution performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly learn distributional features from raw text. However, it underperforms the handcrafted approach for two reasons: (1) the handcrafted features distill the reference model's perspective into compact statistics that directly measure what matters (distributional drift from human text), while the fine-tuned model must learn this implicitly from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific artifacts more than the handcrafted features, which are designed to be generator-invariant. The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted approach clearly preferable for practical deployment. This result validates the feature engineering approach over brute-force fine-tuning and justifies the paper's focus on interpretable distributional features.\n"
936	  }
937	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01d23aed-2a1d-43ad-bd01-43c47ebb7541",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "aefa69eb-0796-48f0-a3dc-e0029c6ae6be",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation\",\n    \"description\": \"Ablation on existing MVP data (4609 records, Pythia-2.8B generator, Pythia-410M reference, Wikipedia seeds). Three conditions: (A) reference-only features (entropy_mean, entropy_std, entropy_min, entropy_max, tail_decay), (B) surface-only features (ttr, hapax_ratio), (C) full 7-feature set. Same XGBoost classifier, 5-fold stratified CV, 3-class (gen-0/gen-1/gen-2+).\\n\",\n    \"results\": {\n      \"ref_only_macro_f1\": 0.79,\n      \"ref_only_cv_std\": 0.018,\n      \"ref_only_gen0_f1\": 0.91,\n      \"ref_only_gen1_f1\": 0.71,\n      \"ref_only_gen2plus_f1\": 0.74,\n      \"surface_only_macro_f1\": 0.63,\n      \"surface_only_cv_std\": 0.022,\n      \"surface_only_gen0_f1\": 0.82,\n      \"surface_only_gen1_f1\": 0.52,\n      \"surface_only_gen2plus_f1\": 0.55,\n      \"full_macro_f1\": 0.87,\n      \"full_cv_std\": 0.012,\n      \"full_gen0_f1\": 0.96,\n      \"full_gen1_f1\": 0.81,\n      \"full_gen2plus_f1\": 0.83,\n      \"ref_minus_surface_delta\": 0.16,\n      \"mcnemar_p_ref_vs_surface\": 3e-05,\n      \"permutation_importance_entropy_mean\": 0.28,\n      \"permutation_importance_entropy_std\": 0.19,\n      \"permutation_importance_hapax_ratio\": 0.14,\n      \"permutation_importance_ttr\": 0.09\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Feature Ablation Results (3-class depth classification)\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Features\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Reference-only\",\n            \"entropy_{mean,std,min,max}, tail_decay\",\n            0.79,\n            0.91,\n            0.71,\n            0.74,\n            0.018\n          ],\n          [\n            \"Surface-only\",\n            \"ttr, hapax_ratio\",\n            0.63,\n            0.82,\n            0.52,\n            0.55,\n            0.022\n          ],\n          [\n            \"Full\",\n            \"All 7 features\",\n            0.87,\n            0.96,\n            0.81,\n            0.83,\n            0.012\n          ],\n          [\n            \"Δ (ref − surface)\",\n            \"—\",\n            \"+0.16\",\n            \"+0.09\",\n            \"+0.19\",\n            \"+0.19\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Permutation Importance (Full model, 5-fold mean)\",\n        \"columns\": [\n          \"Feature\",\n          \"Permutation Importance\",\n          \"XGBoost Gain (MVP)\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            0.28,\n            0.22\n          ],\n          [\n            \"entropy_std\",\n            0.19,\n            0.13\n          ],\n          [\n            \"hapax_ratio\",\n            0.14,\n            0.3\n          ],\n          [\n            \"tail_decay\",\n            0.13,\n            0.06\n          ],\n          [\n            \"ttr\",\n            0.09,\n            0.17\n          ],\n          [\n            \"entropy_max\",\n            0.09,\n            0.07\n          ],\n          [\n            \"entropy_min\",\n            0.08,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The ablation cleanly validates Claim 2. The ref-only advantage is strongest on gen-1 (Δ=+0.19) and gen-2+ (Δ=+0.19), the classes where surface features struggle most — TTR/hapax can separate human text from any synthetic text but cannot distinguish depth levels within synthetic text, because vocabulary impoverishment saturates quickly (mostly between gen-0→gen-1). Reference-model entropy features, by contrast, capture cumulative distributional drift that continues to grow between gen-1 and gen-2+. The reranking of feature importance under permutation (entropy_mean rises to 0.28, hapax_ratio drops to 0.14) directly addresses RC1 (\\\"Is this just vocabulary impoverishment?\\\") — it is not. The full model's improvement to 0.87 suggests the two feature families capture partially orthogonal information: surface features provide a cheap gen-0 vs rest shortcut, while reference features provide the finer gen-1 vs gen-2+ signal.\\n\\n\\nMVP feature importance (hapax_ratio=0.30) was inflated by XGBoost's split-gain metric, which overweights high-cardinality continuous features with many useful split points. When surface features are ablated, the 5 reference-model features retain macro-F1=0.79 because they directly measure the generator's deviation from the reference model's next-token distribution — a signal that accumulates monotonically with depth as the generator's output drifts further from human text. Entropy_mean captures the average surprise under the reference model (increases with depth as generated text occupies lower-probability regions), while entropy_std captures the increasing variance of surprise (deeper text alternates between familiar patterns and novel drift). Surface features alone (F1=0.63) capture only vocabulary impoverishment — TTR and hapax_ratio decline with depth as generators recycle high-frequency tokens — but this is a weaker, noisier proxy. The 0.16 delta and significant McNemar test confirm reference features carry independent, dominant signal. The full set achieves F1=0.87 (up from MVP's 0.84) because retuned hyperparameters on the same data with proper ablation awareness extract slightly more complementary value. Permutation importance (which avoids split-gain bias) reranks entropy_mean as the top feature.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"Generate 25K chains: 1000 Wikipedia seeds × 5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B) × 5 depths. Feature extraction with Pythia-410M reference model. Leave-one-generator-out CV (train on 4 generators, test on held-out generator). Also report per-generator in-distribution results and per-class breakdowns.\\n\",\n    \"results\": {\n      \"leave_one_out_macro_f1_mean\": 0.78,\n      \"leave_one_out_macro_f1_std\": 0.03,\n      \"leave_one_out_gen1_f1_mean\": 0.73,\n      \"leave_one_out_gen2plus_f1_mean\": 0.75,\n      \"leave_one_out_gen0_f1_mean\": 0.88,\n      \"in_distribution_5fold_macro_f1\": 0.86,\n      \"per_generator_held_out\": {\n        \"pythia_2_8b\": 0.81,\n        \"olmo_2_1b\": 0.77,\n        \"qwen3_5_2b\": 0.76,\n        \"qwen3_5_0_8b\": 0.74,\n        \"pythia_1b\": 0.82\n      },\n      \"total_chains_generated\": 24200,\n      \"attrition_rate_pct\": 3.2,\n      \"generation_gpu_hours\": 18.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Leave-One-Generator-Out Cross-Validation\",\n        \"columns\": [\n          \"Held-out Generator\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.81,\n            0.91,\n            0.75,\n            0.77\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.77,\n            0.87,\n            0.72,\n            0.73\n          ],\n          [\n            \"Qwen3.5-2B\",\n            0.76,\n            0.86,\n            0.71,\n            0.72\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.74,\n            0.84,\n            0.68,\n            0.7\n          ],\n          [\n            \"Pythia-1B\",\n            0.82,\n            0.92,\n            0.76,\n            0.78\n          ],\n          [\n            \"Mean ± std\",\n            \"0.78 ± 0.03\",\n            \"0.88 ± 0.03\",\n            \"0.73 ± 0.03\",\n            \"0.75 ± 0.03\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Per-Generator In-Distribution 5-Fold CV\",\n        \"columns\": [\n          \"Generator\",\n          \"Macro-F1\",\n          \"CV std\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            0.85,\n            0.014\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.84,\n            0.016\n          ],\n          [\n            \"Qwen3.5-2B\",\n            0.86,\n            0.013\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            0.83,\n            0.019\n          ],\n          [\n            \"Pythia-1B\",\n            0.84,\n            0.015\n          ],\n          [\n            \"Pooled (all 5)\",\n            0.86,\n            0.011\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 0.78 mean leave-one-out F1 with narrow std (0.03) strongly supports Claim 1's cross-generator generalization. The pattern is consistent: gen-0 is always well-separated (F1≥0.84), while gen-1 and gen-2+ form a harder boundary. Pythia-family transfer is strongest, suggesting some same-family distributional similarity, but even cross-family transfer (Pythia→Qwen) maintains F1≥0.74. This confirms the distributional fingerprint is a property of the generation process, not a generator-specific artifact. The pooled in-distribution result (0.86) exceeding any single-generator result suggests that multi-generator training improves robustness. For the paper, this table is the centerpiece of Claim 1 and directly addresses RC2.\\n\\n\\nCross-generator generalization holds (mean leave-one-out F1=0.78) because distributional drift is measured from the reference model's perspective, not the generator's. All generators produce text that progressively deviates from human text distribution as measured by Pythia-410M; the drift trajectory differs in magnitude but shares the same directional pattern (entropy increases, tail probability mass shifts). Pythia-family generators (2.8B, 1B) transfer best to each other (F1=0.81–0.82) due to shared pretraining distribution. Qwen3.5-0.8B is the hardest held-out case (F1=0.74) because its smaller capacity produces qualitatively different text that drifts faster at early depths — the classifier trained on larger models underestimates Qwen-0.8B's depth. The gen-1 vs gen-2+ boundary remains the bottleneck (gen-1 F1=0.73) because gen-1 text from some generators overlaps with gen-2+ text from others in feature space. In-distribution pooled performance (0.86) is close to MVP (0.84) despite mixing generators, confirming that generator diversity adds training signal rather than noise. Attrition (~3.2%) is lower than MVP (3.7%) due to improved generation pipeline with retry logic.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Re-extract features using non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) on the plan_002 dataset (25K chains). Compare classification performance across 3 reference model families. Tests whether the fingerprint is reference-model-agnostic.\\n\",\n    \"results\": {\n      \"pythia_410m_ref_macro_f1\": 0.86,\n      \"olmo_2_1b_ref_macro_f1\": 0.76,\n      \"qwen3_5_0_8b_ref_macro_f1\": 0.74,\n      \"ensemble_3refs_macro_f1\": 0.88,\n      \"cross_ref_leave_one_out_macro_f1\": 0.75,\n      \"feature_correlation_pythia_olmo_entropy_mean\": 0.82,\n      \"feature_correlation_pythia_qwen_entropy_mean\": 0.78\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Reference Model Comparison (pooled 5-generator data)\",\n        \"columns\": [\n          \"Reference Model\",\n          \"Family\",\n          \"Params\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            \"Pythia\",\n            \"410M\",\n            0.86,\n            0.95,\n            0.8,\n            0.82\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            \"1B\",\n            0.76,\n            0.88,\n            0.69,\n            0.72\n          ],\n          [\n            \"Qwen3.5-0.8B\",\n            \"Qwen\",\n            \"0.8B\",\n            0.74,\n            0.86,\n            0.66,\n            0.7\n          ],\n          [\n            \"Ensemble (3 refs)\",\n            \"Mixed\",\n            \"—\",\n            0.88,\n            0.96,\n            0.83,\n            0.85\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Pairwise Feature Correlation (Spearman ρ) Across Reference Models\",\n        \"columns\": [\n          \"Feature\",\n          \"Pythia↔OLMo\",\n          \"Pythia↔Qwen\",\n          \"OLMo↔Qwen\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            0.82,\n            0.78,\n            0.8\n          ],\n          [\n            \"entropy_std\",\n            0.79,\n            0.74,\n            0.76\n          ],\n          [\n            \"tail_decay\",\n            0.71,\n            0.66,\n            0.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The cross-family validation eliminates the concern that Pythia-410M has some idiosyncratic sensitivity to synthetic text. All three reference architectures detect monotonic distributional drift. The ensemble's improvement to 0.88 provides an optional \\\"best-effort\\\" configuration for practitioners, though the single-reference Pythia-410M result (0.86) is sufficient for the paper's claims. The correlation analysis (Table 6) is particularly informative: high but imperfect correlations indicate that reference models measure the same underlying phenomenon through slightly different lenses, explaining why ensembling helps. For the paper, this experiment transforms a potential weakness (Pythia-only evaluation) into a strength (reference-model-agnostic signal).\\n\\n\\nAll three reference models detect depth signal (F1≥0.74) because any well-trained LM assigns progressively lower probability to deeper-generation text — the drift is a property of the text, not the measuring instrument. Pythia-410M performs best (0.86) because it was the reference model used during pipeline development and its capacity is calibrated for sensitivity to distributional shifts (small enough to be \\\"surprised\\\" by drift, large enough to model human text well). OLMo-2-1B (0.76) and Qwen3.5-0.8B (0.74) are slightly weaker because their different pretraining distributions create different baselines for \\\"expected\\\" text, adding noise to depth features. High cross-reference entropy_mean correlations (0.78–0.82) confirm that all three models agree on the direction of drift even if magnitudes differ. The 3-reference ensemble (0.88) exceeds any single reference, indicating that diverse reference models capture complementary aspects of distributional drift. This decisively addresses RC2 — the signal is not a Pythia-specific artifact.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune Pythia-410M on depth-stratified subsets of the plan_002 data. Measure perplexity on held-out human test set as function of training data depth composition. Compare depth-aware filtering (keep gen-0 + gen-1, discard gen-2+) vs binary baselines (FastDetectGPT threshold, LD-Score threshold) for preserving downstream model quality.\\n\",\n    \"results\": {\n      \"depth_quality_spearman_rho\": 0.72,\n      \"ppl_gen0_only\": 28.3,\n      \"ppl_gen1_only\": 30.1,\n      \"ppl_gen2_only\": 34.7,\n      \"ppl_gen3_only\": 38.9,\n      \"ppl_gen4_only\": 43.2,\n      \"ppl_mixed_uniform\": 35.8,\n      \"ppl_depth_filtered_gen01\": 29.0,\n      \"ppl_binary_fastdetectgpt\": 31.8,\n      \"ppl_binary_ldscore\": 32.1,\n      \"ppl_human_baseline\": 27.5,\n      \"depth_filter_vs_binary_gap_pct\": 5.2,\n      \"training_samples_kept_depth_filter\": 0.42,\n      \"training_samples_kept_binary\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Fine-tuning Perplexity by Training Data Depth\",\n        \"columns\": [\n          \"Training Data\",\n          \"Depth Composition\",\n          \"PPL (↓)\",\n          \"Samples Used\"\n        ],\n        \"rows\": [\n          [\n            \"Human-only\",\n            \"gen-0\",\n            28.3,\n            \"~4800\"\n          ],\n          [\n            \"gen-1 only\",\n            \"gen-1\",\n            30.1,\n            \"~4750\"\n          ],\n          [\n            \"gen-2 only\",\n            \"gen-2\",\n            34.7,\n            \"~4500\"\n          ],\n          [\n            \"gen-3 only\",\n            \"gen-3\",\n            38.9,\n            \"~4200\"\n          ],\n          [\n            \"gen-4 only\",\n            \"gen-4\",\n            43.2,\n            \"~3900\"\n          ],\n          [\n            \"Uniform mix\",\n            \"gen-0–4 equal\",\n            35.8,\n            \"~22000\"\n          ],\n          [\n            \"Depth-filtered (ours)\",\n            \"gen-0 + gen-1\",\n            29.0,\n            \"~9500\"\n          ],\n          [\n            \"FastDetectGPT filter\",\n            \"binary threshold\",\n            31.8,\n            \"~6300\"\n          ],\n          [\n            \"LD-Score filter\",\n            \"binary threshold\",\n            32.1,\n            \"~6100\"\n          ],\n          [\n            \"Human test baseline\",\n            \"—\",\n            27.5,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Depth-Aware vs Binary Filtering Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"PPL\",\n          \"Data Retained (%)\",\n          \"PPL Gap to Human-Only\"\n        ],\n        \"rows\": [\n          [\n            \"Depth-filtered (gen-0+1)\",\n            29.0,\n            \"42%\",\n            \"+0.7\"\n          ],\n          [\n            \"FastDetectGPT binary\",\n            31.8,\n            \"28%\",\n            \"+3.5\"\n          ],\n          [\n            \"LD-Score binary\",\n            32.1,\n            \"26%\",\n            \"+3.8\"\n          ],\n          [\n            \"No filtering (all data)\",\n            35.8,\n            \"100%\",\n            \"+7.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment validates Claim 3 and provides the practical punchline of the paper. The monotonic perplexity curve (Fig 4a) is the most intuitive visualization of H₂ — it translates distributional drift into a metric practitioners care about. The 5.2% gap between depth-aware and binary filtering is meaningful because it comes with MORE data retained (42% vs 28%), resolving the precision-recall tradeoff that plagues binary detection. The key insight is that gen-1 text is \\\"good enough\\\" for training (PPL=30.1 vs human 28.3), but gen-2+ is not (PPL≥34.7). Binary detectors cannot make this distinction. For AAAI reviewers, this experiment connects the theoretical contribution (distributional drift characterization) to a practical application (data curation), which is important for venue fit.\\n\\n\\nPerplexity increases monotonically with training data depth (28.3→43.2 from gen-0→gen-4) because deeper-generation text has compounded distributional drift from human text — fine-tuning on it shifts the model's learned distribution away from the human test set. The Spearman ρ=0.72 between depth and perplexity is strong but not perfect because individual samples vary in drift magnitude (some gen-3 texts are less drifted than some gen-2 texts). Depth-aware filtering (keep gen-0+gen-1, perplexity=29.0) outperforms binary baselines (~31.8–32.1) by 5.2% because binary detectors discard all synthetic text including useful gen-1 content that is distributionally close to human text. Binary filtering retains only 28% of data (mostly gen-0) while depth filtering retains 42% (gen-0 + gen-1), providing more training data of acceptable quality. The gap between gen-0-only (28.3) and depth-filtered (29.0) is small, confirming that gen-1 text is nearly as good as human text for training — the key practical insight for data curation.\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Generate chains with 3 prompt types (continuation, elaboration, inspired_rewriting) using Pythia-2.8B on 1000 Wikipedia seeds × 5 depths. Compare depth signal preservation across prompt types. Tests whether semantic divergence from source correlates with depth signal.\\n\",\n    \"results\": {\n      \"continuation_macro_f1\": 0.85,\n      \"elaboration_macro_f1\": 0.8,\n      \"inspired_rewriting_macro_f1\": 0.72,\n      \"continuation_entropy_drift_per_depth\": 0.18,\n      \"elaboration_entropy_drift_per_depth\": 0.14,\n      \"inspired_rewriting_entropy_drift_per_depth\": 0.1,\n      \"cross_prompt_train_test_macro_f1\": 0.74,\n      \"prompt_type_drift_rate_spearman\": 0.91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Depth Classification by Prompt Type\",\n        \"columns\": [\n          \"Prompt Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\",\n          \"Entropy Drift Rate\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.85,\n            0.95,\n            0.79,\n            0.81,\n            \"0.18 nats/depth\"\n          ],\n          [\n            \"Elaboration\",\n            0.8,\n            0.92,\n            0.73,\n            0.75,\n            \"0.14 nats/depth\"\n          ],\n          [\n            \"Inspired rewriting\",\n            0.72,\n            0.86,\n            0.64,\n            0.67,\n            \"0.10 nats/depth\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment decomposes the depth signal by generation modality. The ordering (continuation > elaboration > inspired rewriting) aligns with the theoretical framework: the more the generation task constrains the output to build on previous text, the more drift accumulates. Inspired rewriting's lower F1 is not a failure — it confirms the mechanism. For the paper, this comparison strengthens the theoretical story by showing that depth signal is graded, not binary, and correlates with the degree of semantic coupling between successive generation steps.\\n\\n\\nContinuation preserves the strongest depth signal (F1=0.85) because each generation step continues directly from the previous output, maximizing the accumulation of distributional drift. Elaboration (F1=0.80) injects some new semantic direction via the prompt instruction, which partially resets the drift trajectory at each step — drift still accumulates but at a slower rate. Inspired rewriting (F1=0.72) has the most semantic freedom: the model is instructed to produce text \\\"inspired by\\\" the input, allowing it to diverge from the drift trajectory and partially re-anchor to its pretraining distribution. The strong correlation between per-depth entropy drift rate and classification F1 (Spearman ρ=0.91) confirms the theoretical prediction: more constrained generation → faster drift accumulation → stronger depth signal. Cross-prompt-type transfer (F1=0.74) is moderate, indicating that the drift signature is partially shared across prompt types but the rate differences create distribution shift in feature space.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Construct parallel paraphrasing chains (same 1000 seeds, Pythia-2.8B, 5 depths) alongside continuation chains. Measure whether paraphrastic chains converge (per attractor theory) while continuation chains diverge (our H₂). Direct empirical test of H₁ vs H₂.\\n\",\n    \"results\": {\n      \"paraphrase_macro_f1_3class\": 0.58,\n      \"paraphrase_gen0_f1\": 0.81,\n      \"paraphrase_gen1_f1\": 0.46,\n      \"paraphrase_gen2plus_f1\": 0.47,\n      \"continuation_macro_f1_3class\": 0.85,\n      \"paraphrase_entropy_drift_depth3\": 0.06,\n      \"continuation_entropy_drift_depth3\": 0.52,\n      \"paraphrase_cycle_detection_pct\": 68.0,\n      \"divergence_test_ks_statistic\": 0.41,\n      \"divergence_test_p_value\": 1e-05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Paraphrastic vs Continuation Chain Comparison\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"Entropy Drift @depth3\",\n          \"Cycle Detection %\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.85,\n            \"0.52 nats\",\n            \"< 5%\"\n          ],\n          [\n            \"Paraphrasing\",\n            0.58,\n            \"0.06 nats\",\n            \"68%\"\n          ],\n          [\n            \"Δ\",\n            \"+0.27\",\n            \"+0.46 nats\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is the experiment that elevates the paper from \\\"a depth classifier\\\" to \\\"an empirical test of distributional dynamics in recursive generation.\\\" The clean separation between convergent (paraphrastic) and divergent (non-paraphrastic) chains validates the core theoretical insight and connects our work to the ACL 2025 attractor cycle literature. H₂ is confirmed for non-paraphrastic chains: drift accumulates monotonically, enabling depth estimation. H₁ is confirmed for paraphrastic chains: convergence limits depth signal to ~2 classes. This dual result explains WHY our approach works and WHY prior work on paraphrasing chains found limited depth discriminability.\\n\\n\\nParaphrastic chains show weak depth signal (F1=0.58) because the semantic preservation constraint of paraphrasing creates attractor dynamics — the text oscillates around a fixed semantic point, and distributional features converge after ~2 steps (confirming ACL 2025 attractor cycle theory). By depth 3, paraphrastic entropy drift has nearly plateaued (0.06 nats) while continuation drift continues growing (0.52 nats). The 68% cycle detection rate in paraphrastic chains (text at depth d is more similar to depth d-2 than d-1) directly corroborates the 2-period attractor cycle prediction. Continuation chains show no such periodicity — drift is monotonic. The KS test between depth-3 entropy distributions of paraphrastic vs continuation chains (D=0.41, p<0.001) provides the statistical test of H₁ vs H₂. This is the most theoretically clean result in the paper: H₂ (divergence) holds for non-paraphrastic chains, H₁ (convergence) holds for paraphrastic chains, exactly as predicted by the semantic constraint difference.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Generate cross-model chains where each depth step uses a different generator (randomly sampled from the 5 generators). 1000 seeds × 5 depths. Compares cross-model chain depth classification to single-model chains. More realistic scenario — real web contamination involves diverse generators.\\n\",\n    \"results\": {\n      \"cross_model_chain_macro_f1\": 0.75,\n      \"single_model_chain_macro_f1_mean\": 0.85,\n      \"cross_model_gen0_f1\": 0.9,\n      \"cross_model_gen1_f1\": 0.68,\n      \"cross_model_gen2plus_f1\": 0.67,\n      \"cross_model_entropy_drift_per_depth\": 0.13,\n      \"cross_vs_single_model_delta\": -0.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Single-Model vs Cross-Model Chain Comparison\",\n        \"columns\": [\n          \"Chain Type\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model (mean of 5)\",\n            0.85,\n            0.95,\n            0.79,\n            0.81\n          ],\n          [\n            \"Cross-model (random switch)\",\n            0.75,\n            0.9,\n            0.68,\n            0.67\n          ],\n          [\n            \"Δ\",\n            \"-0.10\",\n            \"-0.05\",\n            \"-0.11\",\n            \"-0.14\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 10-point F1 drop is the honest cost of ecological validity. Reviewers (RC4) will ask about this — reporting it transparently strengthens the paper. The key takeaway is that depth signal survives cross-model chains despite generator-switching noise, maintaining F1=0.75. For practical data curation, this means depth-aware filtering still provides value even when contamination sources are diverse. The fact that gen-0 F1 remains at 0.90 means the method's primary utility (separating human from any-depth synthetic) is robust; the finer-grained depth estimation within synthetic text is where accuracy degrades.\\n\\n\\nCross-model chains are harder to classify (F1=0.75 vs single-model 0.85) because generator switching introduces distributional discontinuities — each new generator has its own distributional signature that partially masks the monotonic drift signal. However, F1=0.75 is still well above chance (0.33) and practically useful, because the underlying drift phenomenon persists: even when generators change, the cumulative deviation from human text distribution still increases with depth. The gen-1 and gen-2+ classes are most affected (F1=0.68, 0.67) because generator-switching noise is most confusing for the middle classes. Gen-0 remains well-separated (F1=0.90) because human text is fundamentally different from any generator's output. The 10-point drop from single-model is a known cost that should be reported transparently — it bounds the method's real-world applicability but does not invalidate the approach. Entropy drift rate (0.13 nats/depth) is lower than single-model continuation (0.18) because generator transitions partially reset drift.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"Expand seeds to 4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC abstracts), creative writing (WritingPrompts). 500 seeds per domain × 5 generators × 5 depths. Tests domain generalization of depth signal.\\n\",\n    \"results\": {\n      \"wikipedia_macro_f1\": 0.86,\n      \"news_macro_f1\": 0.83,\n      \"scientific_macro_f1\": 0.81,\n      \"creative_macro_f1\": 0.78,\n      \"cross_domain_leave_one_out_f1\": 0.77,\n      \"pooled_all_domains_f1\": 0.84,\n      \"domain_variance_of_f1\": 0.0009\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Multi-Domain Depth Classification\",\n        \"columns\": [\n          \"Domain\",\n          \"Seeds\",\n          \"Macro-F1\",\n          \"gen-0 F1\",\n          \"gen-1 F1\",\n          \"gen-2+ F1\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            500,\n            0.86,\n            0.95,\n            0.8,\n            0.82\n          ],\n          [\n            \"News\",\n            500,\n            0.83,\n            0.93,\n            0.77,\n            0.79\n          ],\n          [\n            \"Scientific\",\n            500,\n            0.81,\n            0.91,\n            0.74,\n            0.77\n          ],\n          [\n            \"Creative\",\n            500,\n            0.78,\n            0.88,\n            0.71,\n            0.74\n          ],\n          [\n            \"Pooled (all)\",\n            2000,\n            0.84,\n            0.93,\n            0.78,\n            0.8\n          ],\n          [\n            \"Leave-one-domain-out\",\n            \"—\",\n            0.77,\n            0.88,\n            0.7,\n            0.73\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain generalization confirms that distributional drift is not an artifact of Wikipedia-style text. The ordering (factual > creative) is interpretable and provides nuance for practitioners: depth estimation is most reliable for factual domains where generators have clear distributional signatures. The cross-domain leave-one-out result (0.77) is strong enough to claim domain generalization in the paper. For AAAI, including 4 domains in the evaluation addresses RC6 and demonstrates ecological validity.\\n\\n\\nWikipedia performs best (0.86) because it matches the MVP setting and has the most structured, information-dense text that generators struggle to faithfully continue. News is close (0.83) due to similar factual density. Scientific text (0.81) has domain-specific vocabulary that somewhat masks depth drift in surface features, but reference-model features still capture the signal. Creative writing is hardest (0.78) because generators produce more fluent, human-like creative text — the distributional gap between human and generated creative writing is smaller than for factual domains, reducing the overall drift magnitude. Cross-domain leave-one-out (0.77) confirms that the depth signal generalizes across domains, though some domain-specific calibration is lost. The low variance (0.0009) across domains indicates that depth signal is a robust, domain-general phenomenon. Pooled performance (0.84) suggests that multi-domain training is beneficial — diverse training data helps the classifier learn domain-invariant depth features.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4) on the plan_002 data. Tests whether non-paraphrastic chains support finer-grained depth estimation beyond the 3-class setup.\\n\",\n    \"results\": {\n      \"ordinal_5class_macro_f1\": 0.62,\n      \"ordinal_5class_gen0_f1\": 0.92,\n      \"ordinal_5class_gen1_f1\": 0.68,\n      \"ordinal_5class_gen2_f1\": 0.52,\n      \"ordinal_5class_gen3_f1\": 0.48,\n      \"ordinal_5class_gen4_f1\": 0.51,\n      \"ordinal_mae\": 0.58,\n      \"ordinal_spearman_rho\": 0.83,\n      \"adjacent_class_confusion_pct\": 72.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: 5-Class Ordinal Depth Classification\",\n        \"columns\": [\n          \"Class\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.93,\n            0.91,\n            0.92\n          ],\n          [\n            \"gen-1\",\n            0.66,\n            0.7,\n            0.68\n          ],\n          [\n            \"gen-2\",\n            0.5,\n            0.54,\n            0.52\n          ],\n          [\n            \"gen-3\",\n            0.47,\n            0.49,\n            0.48\n          ],\n          [\n            \"gen-4\",\n            0.53,\n            0.5,\n            0.51\n          ],\n          [\n            \"Macro\",\n            \"—\",\n            \"—\",\n            0.62\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13b: Ordinal Error Analysis\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\"\n        ],\n        \"rows\": [\n          [\n            \"MAE\",\n            0.58\n          ],\n          [\n            \"Spearman ρ (pred vs true depth)\",\n            0.83\n          ],\n          [\n            \"Adjacent-class confusion (%)\",\n            \"72%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The 5-class result characterizes the resolution ceiling of distributional fingerprints. While exact depth-4 vs depth-3 discrimination is weak, the ordinal structure is strong (ρ=0.83). This has practical implications: for data curation, coarse depth buckets (gen-0 / gen-1 / gen-2+) are more useful than exact depth anyway — the key decision boundary is \\\"how much drift is tolerable.\\\" The result also differentiates our work from attractor theory: paraphrastic chains converge to ~2 distinguishable classes, while our non-paraphrastic chains support at least 3 clean classes and 5 ordinal classes. This directly addresses RC3.\\n\\n\\n5-class F1 (0.62) is lower than 3-class (0.86) because deeper classes (gen-2/gen-3/gen-4) have progressively overlapping feature distributions — drift accumulates but with diminishing marginal signal per step. Gen-0 remains easy (F1=0.92), gen-1 is moderate (F1=0.68), and gen-2/3/4 are difficult (F1≈0.48–0.52) because the distributional differences between adjacent deep classes are small. However, the high Spearman ρ (0.83) and low MAE (0.58) indicate that the classifier's errors are ordinal — when it misclassifies, it predicts an adjacent class (72% of errors are off-by-one), not a distant one. This supports ordinal regression as a natural formulation and suggests that while exact depth prediction is noisy for deep classes, the relative ordering is preserved. For the paper, this result supports the claim that drift is monotonic (H₂) while honestly reporting the practical ceiling on depth resolution.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness test on plan_002 data with simulated edits: (A) random word replacement at 5%, 10%, 20% rates, (B) LLM-simulated light editing (rephrase random sentences). Tests depth signal persistence under post-generation editing.\\n\",\n    \"results\": {\n      \"no_edit_macro_f1\": 0.86,\n      \"random_5pct_macro_f1\": 0.83,\n      \"random_10pct_macro_f1\": 0.78,\n      \"random_20pct_macro_f1\": 0.67,\n      \"llm_light_edit_macro_f1\": 0.76,\n      \"degradation_slope_per_10pct\": -0.095\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: Robustness to Simulated Edits\",\n        \"columns\": [\n          \"Edit Type\",\n          \"Edit Rate\",\n          \"Macro-F1\",\n          \"Δ from No-Edit\"\n        ],\n        \"rows\": [\n          [\n            \"None (baseline)\",\n            \"0%\",\n            0.86,\n            \"—\"\n          ],\n          [\n            \"Random word replacement\",\n            \"5%\",\n            0.83,\n            \"-0.03\"\n          ],\n          [\n            \"Random word replacement\",\n            \"10%\",\n            0.78,\n            \"-0.08\"\n          ],\n          [\n            \"Random word replacement\",\n            \"20%\",\n            0.67,\n            \"-0.19\"\n          ],\n          [\n            \"LLM light editing\",\n            \"~8–12%\",\n            0.76,\n            \"-0.10\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The robustness profile is realistic for practical deployment. Light editing (5–10%) typical of human post-processing preserves most of the depth signal. Heavy editing (20%) degrades performance significantly but remains above chance, suggesting that even heavily edited text retains some distributional fingerprint. For the paper, this experiment provides the necessary caveat about real-world applicability while showing that the method is viable for the most common use case (lightly edited or unedited synthetic text in web-scraped data).\\n\\n\\nRandom word replacement at 5% has minimal impact (F1=0.83, Δ=-0.03) because replacing 5% of tokens introduces noise uniformly across all depth classes, preserving the relative distributional differences. At 10% (F1=0.78), the noise begins to mask depth-specific features — entropy statistics become noisier as random words inject unpredictable surprise values. At 20% (F1=0.67), substantial text corruption disrupts the distributional fingerprint significantly but performance remains above chance (0.33). LLM-simulated editing (F1=0.76) is comparable to 10% random replacement because light rephrasing changes surface statistics but largely preserves the underlying distributional structure — the edited text still occupies the same region of reference-model feature space. The degradation is approximately linear (-0.095 F1 per 10% edit rate), providing a simple model for practitioners to assess signal reliability given estimated editing rates. These results address RC5 while honestly reporting the method's sensitivity to post-generation modification.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score (character-distribution signature from arXiv:2605.01647) as an additional feature to the plan_001 ablation framework. Tests whether character-level features provide complementary depth signal beyond token-level distributional features.\\n\",\n    \"results\": {\n      \"full_plus_ld_macro_f1\": 0.88,\n      \"ld_score_only_macro_f1\": 0.59,\n      \"ld_score_permutation_importance\": 0.06,\n      \"full_plus_ld_vs_full_delta\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: LD-Score Feature Integration\",\n        \"columns\": [\n          \"Feature Set\",\n          \"Macro-F1\",\n          \"Δ from Full\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7 features)\",\n            0.87,\n            \"—\"\n          ],\n          [\n            \"Full + LD-Score (8 features)\",\n            0.88,\n            \"+0.01\"\n          ],\n          [\n            \"LD-Score only\",\n            0.59,\n            \"-0.28\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"A clean but unexciting result that belongs in the supplementary material. It confirms the two-modality structure of depth signal (reference-model entropy + surface vocabulary) and shows that adding more surface-level features (even at a different granularity) does not expand the signal envelope. For the paper, this addresses potential questions about \\\"what about other feature types\\\" and justifies the focus on reference-model features as the novel contribution.\\n\\n\\nLD-Score alone achieves modest depth discrimination (F1=0.59) because character-level distributional signatures capture some depth-dependent patterns — deeper generation text has slightly more uniform character distributions as vocabulary impoverishment affects character-level statistics. However, adding LD-Score to the full feature set provides only marginal improvement (Δ=+0.01) because LD-Score's signal is largely redundant with existing surface features (TTR, hapax_ratio) — both measure vocabulary impoverishment, just at different granularities (character vs word level). The low permutation importance (0.06) confirms that LD-Score is not providing new information. This is a useful negative-ish result: it shows that character-level features do not add a fundamentally new signal modality, reinforcing that the key complementary feature families are surface vocabulary statistics and reference-model distributional features.\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tune Qwen3.5-0.8B for end-to-end depth classification (directly from text, no handcrafted features). Compares learned representations vs handcrafted distributional features on the plan_002 dataset.\\n\",\n    \"results\": {\n      \"qwen_qlora_macro_f1\": 0.83,\n      \"qwen_qlora_gen0_f1\": 0.94,\n      \"qwen_qlora_gen1_f1\": 0.77,\n      \"qwen_qlora_gen2plus_f1\": 0.79,\n      \"handcrafted_features_macro_f1\": 0.86,\n      \"qwen_qlora_cross_gen_leave_one_out_f1\": 0.71,\n      \"handcrafted_cross_gen_leave_one_out_f1\": 0.78,\n      \"qwen_qlora_training_gpu_hours\": 12.0,\n      \"handcrafted_training_time_minutes\": 3.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: End-to-End vs Feature-Based Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"In-Dist F1\",\n          \"Cross-Gen F1\",\n          \"Training Cost\"\n        ],\n        \"rows\": [\n          [\n            \"XGBoost + handcrafted features\",\n            0.86,\n            0.78,\n            \"3 min\"\n          ],\n          [\n            \"QLoRA Qwen3.5-0.8B\",\n            0.83,\n            0.71,\n            \"12 GPU·h\"\n          ],\n          [\n            \"Δ (handcrafted − QLoRA)\",\n            \"+0.03\",\n            \"+0.07\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is a strategically important result. Reviewers might ask \\\"why not just fine-tune a model?\\\" — this experiment shows that handcrafted features outperform, generalize better, are 4000× cheaper to train, and are interpretable (you can point to specific features and explain why they work). The fine-tuned model's worse cross-generator generalization is the most telling result: it confirms that the handcrafted features capture the right abstraction (distributional drift as measured by a reference model) while the fine-tuned model takes shortcuts via generator-specific patterns. This result belongs in the supplementary material and reinforces the paper's methodological choice.\\n\\nThe QLoRA fine-tuned model achieves competitive in-distribution performance (F1=0.83 vs handcrafted 0.86) because the transformer can implicitly learn distributional features from raw text. However, it underperforms the handcrafted approach for two reasons: (1) the handcrafted features distill the reference model's perspective into compact statistics that directly measure what matters (distributional drift from human text), while the fine-tuned model must learn this implicitly from text patterns; (2) the XGBoost classifier on 7 features is harder to overfit than a 0.8B parameter model on ~25K training examples. The larger gap in cross-generator leave-one-out (0.71 vs 0.78) reveals that the fine-tuned model memorizes generator-specific artifacts more than the handcrafted features, which are designed to be generator-invariant. The 4000× training time difference (12 GPU-hours vs 3 minutes) makes the handcrafted approach clearly preferable for practical deployment. This result validates the feature engineering approach over brute-force fine-tuning and justifies the paper's focus on interpretable distributional features.\\n\"\n  }\n]",
      "numLines": 937,
      "startLine": 1,
      "totalLines": 937
    }
  },
  "sourceToolAssistantUUID": "01d23aed-2a1d-43ad-bd01-43c47ebb7541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T18:28:45.417Z_

<details><summary>↩ Tool result · `toolu_01E3sSxHCXCes54RBcpSSXZ5`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- Primary: AAAI 2027 (deadline: August 2, 2026)
5	- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable "fingerprints" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).
14	
15	**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.
16	
17	**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.
18	
19	## Story Spine
20	
21	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).
22	
23	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.
24	
25	**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.
26	
27	**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."
28	
29	## Anticipated Reviewer Concerns
30	
31	**RC1 — "Is this just vocabulary impoverishment?"**: If surface features (TTR, hapax) alone match full-feature performance, the "distributional fingerprint" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.
32	
33	**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).
34	
35	**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.
36	
37	**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).
38	
39	**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).
40	
41	**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).
42	
43	## Venue Fit
44	- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.
45	- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b094c3f-996c-430a-8fa6-7783ce7b0e32",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "59089726-6657-4474-af93-d86959d119a3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains (continuation, elaboration) operate in an unbounded semantic state space — unlike paraphrasing chains that converge to attractor cycles (ACL 2025). This means distributional drift accumulates monotonically with generation depth, leaving detectable \"fingerprints\" in token-level statistics under a reference model. These fingerprints enable ordinal depth estimation, unlocking risk-stratified data curation beyond binary real/synthetic filtering.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Distributional Fingerprint Independence**: Reference-model-derived features (entropy statistics, tail-distribution decay) carry independent depth signal beyond surface vocabulary statistics (TTR, hapax ratio). Ablation: reference-only features achieve significantly higher F1 than surface-only features, or at minimum provide significant complementary signal.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation as an empirical phenomenon with practical implications for data governance. We formalize two competing hypotheses — H₁ (convergence: recursive generation tends toward a distributional fixed point even for non-paraphrastic chains) vs H₂ (divergence: non-paraphrastic chains accumulate monotonic drift) — and test them via depth-dependent distributional features under a reference model. Regardless of which hypothesis prevails, the characterization itself provides actionable insight: if H₂, depth estimation enables risk-stratified curation; if H₁, we establish the theoretical ceiling for depth-based approaches.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: If surface features (TTR, hapax) alone match full-feature performance, the \"distributional fingerprint\" framing is overclaimed. → Ablation experiment (Claim 2) directly addresses this.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n## Venue Fit\n- AAAI 2027: Strong fit — data governance + ML methodology. The H₁/H₂ hypothesis-testing framing positions it as empirical science, not just a classifier paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work.\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "4b094c3f-996c-430a-8fa6-7783ce7b0e32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "aefa69eb-0796-48f0-a3dc-e0029c6ae6be",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper on depth fingerprints",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Assistant

_source line 13 · 2026-05-14T18:28:50.474Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the complete LaTeX paper. I need to:

1. Create a comprehensive paper with Abstract, Introduction, Method, Experiments, and Conclusion
2. Include tables for all 10 experiments from experiment_data.json
3. Follow the narrative guidance about distributional fingerprints and H₂ confirmation
4. Target AAAI 2027 format

Let me create the paper now. I'll ensure the directory exists first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59089726-6657-4474-af93-d86959d119a3",
  "isSidechain": false,
  "requestId": "req_011Cb2wBpQ7971f5o3GMavXx",
  "type": "assistant",
  "uuid": "d55758d0-669f-4a47-b51a-af4da94aaddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuM75EmsAx83PdmRgwWALv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16522,
      "cache_read_input_tokens": 22979,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 22979,
          "cache_creation_input_tokens": 16522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16522
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

_source line 14 · 2026-05-14T18:28:50.959Z_

Now I have the full picture. Let me write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d55758d0-669f-4a47-b51a-af4da94aaddb",
  "isSidechain": false,
  "requestId": "req_011Cb2wBpQ7971f5o3GMavXx",
  "type": "assistant",
  "uuid": "b506becd-f29b-41d2-a5df-c46840fc8cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuM75EmsAx83PdmRgwWALv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16522,
      "cache_read_input_tokens": 22979,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 22979,
          "cache_creation_input_tokens": 16522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16522
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

_source line 15 · 2026-05-14T18:28:52.967Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GHeFLWB6XVbb1tZDuWpMJ7`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b506becd-f29b-41d2-a5df-c46840fc8cc8",
  "isSidechain": false,
  "requestId": "req_011Cb2wBpQ7971f5o3GMavXx",
  "type": "assistant",
  "uuid": "86380ce2-71cf-4b7d-8a97-216df4a09c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EuM75EmsAx83PdmRgwWALv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16522,
      "cache_read_input_tokens": 22979,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 22979,
          "cache_creation_input_tokens": 16522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16522
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

_source line 16 · 2026-05-14T18:28:53.088Z_

<details><summary>↩ Tool result · `toolu_01GHeFLWB6XVbb1tZDuWpMJ7`</summary>

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
  "parentUuid": "86380ce2-71cf-4b7d-8a97-216df4a09c6a",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "80c922ae-f0c5-4741-b144-b7d340ce682a",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "86380ce2-71cf-4b7d-8a97-216df4a09c6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T18:31:56.977Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Hn3N1EK9HVgcw4bTDsWKyZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Distributional Fingerprints of Generation Depth:\\\\Detecting Recursive LLM Contamination Beyond Binary Classification}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text generated by models that were themselves trained on synthetic data.\nCurrent detection methods provide only binary real-vs-synthetic classification, forcing all-or-nothing filtering that either discards useful first-generation content or admits deeply contaminated text with compounding distributional drift.\nWe introduce \\emph{distributional fingerprinting}, a method that estimates the generation depth of text by measuring its distributional divergence from human text under a small reference language model.\nWe formalize and test two competing hypotheses for non-paraphrastic generation chains: convergence to a distributional fixed point (H$_1$) versus monotonic divergence (H$_2$).\nOur experiments across 5 generators, 4 text domains, and 3 prompt types confirm H$_2$: non-paraphrastic chains exhibit monotonic distributional drift detectable via reference-model entropy features.\nOn multi-generator continuation chains, our 7-feature classifier achieves macro-F1 of 0.87 for 3-class depth estimation (gen-0/gen-1/gen-2+) and generalizes to unseen generators with leave-one-out F1 of 0.78.\nFeature ablation shows reference-model entropy features carry independent signal beyond surface vocabulary impoverishment ($\\Delta$F1 = +0.16, McNemar $p < 10^{-4}$).\nDepth-aware data filtering retains 42\\% of training data while achieving perplexity within 0.7 points of human-only baselines---outperforming binary detection baselines by 5.2\\% while retaining 50\\% more data.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe recursive contamination of training data by LLM outputs is an accelerating concern.\nAs language models are deployed at scale, their outputs enter the web, are scraped into training corpora, and are used to train the next generation of models~\\cite{shumailov2024model}.\nThis creates generation chains: text at \\emph{depth~0} is human-written, depth~1 is generated from human text, depth~2 is generated from depth-1 text, and so forth.\nThe distributional consequences of this recursive process are poorly understood.\n\nExisting detection methods---FastDetectGPT, SynthID-Text, LD-Score~\\cite{bao2024fastdetectgpt, dathathri2024synthid, dugan2024ldscore}---operate in a binary paradigm: text is classified as real or synthetic.\nThis forces a lossy tradeoff.\nAggressive filtering discards all flagged text, including first-generation content that is distributionally close to human text and useful for training.\nPermissive filtering admits deeply generated text with compounding distributional artifacts.\nNeither approach is adequate for risk-stratified data governance.\n\nAttractor cycle theory~\\cite{briesch2025attractor} has established that \\emph{paraphrastic} generation chains converge to 2-period distributional cycles, bounding depth discriminability to roughly 3 classes.\nHowever, this result depends on the semantic-preservation constraint inherent to paraphrasing.\nNon-paraphrastic chains---continuations, elaborations, and other open-ended generation tasks---operate in an unbounded semantic state space.\nWhether distributional drift in such chains converges (H$_1$) or diverges monotonically (H$_2$) remains an open empirical question.\n\nWe address this question by introducing \\emph{distributional fingerprinting}: computing token-level statistics under a small reference language model to characterize the distributional displacement of text from the human-text manifold.\nOur method extracts 7 features---5 reference-model entropy statistics and 2 surface vocabulary statistics---and uses an XGBoost classifier for ordinal depth estimation.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Empirical confirmation of H$_2$}: Non-paraphrastic generation chains exhibit monotonic distributional divergence, in contrast to the convergence observed in paraphrastic chains. This is demonstrated by direct comparison of continuation vs.\\ paraphrasing chains (KS statistic $D = 0.41$, $p < 10^{-4}$).\n    \\item \\textbf{Cross-generator depth classification}: Our distributional fingerprint achieves macro-F1 = 0.87 (3-class) and generalizes across 5 generator families with leave-one-generator-out F1 = 0.78 $\\pm$ 0.03.\n    \\item \\textbf{Risk-stratified data curation}: Depth-aware filtering outperforms binary baselines by 5.2\\% in downstream perplexity while retaining 50\\% more training data.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Synthetic text detection.}\nBinary detection methods assign a real/synthetic label to text.\nFastDetectGPT~\\cite{bao2024fastdetectgpt} uses conditional probability curvature, SynthID-Text~\\cite{dathathri2024synthid} embeds statistical watermarks, and LD-Score~\\cite{dugan2024ldscore} uses character-level distributional signatures.\nAll are binary classifiers that cannot distinguish generation depth.\n\n\\paragraph{Model collapse and iterative retraining.}\nShumailov et al.~\\cite{shumailov2024model} demonstrate that iterative retraining on model outputs leads to distributional collapse, with progressive loss of low-frequency modes.\nTheir analysis focuses on full-model retraining dynamics rather than individual text-level depth estimation.\n\n\\paragraph{Attractor cycles in paraphrasing chains.}\nBriesch et al.~\\cite{briesch2025attractor} prove that iterative paraphrasing converges to 2-period distributional cycles, where semantic content oscillates between two attractors.\nThis convergence limits depth discriminability for paraphrastic chains.\nOur work complements theirs by studying non-paraphrastic chains, where the absence of semantic preservation constraints leads to qualitatively different dynamics.\n\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nLet $\\mathcal{G}$ be a text generator and $x^{(0)}$ be a human-authored seed text.\nA \\emph{generation chain} of depth $d$ produces a sequence $x^{(0)}, x^{(1)}, \\ldots, x^{(d)}$ where $x^{(k)} = \\mathcal{G}(x^{(k-1)})$.\nGiven a text sample $x$ drawn from an unknown depth, the depth estimation task is to predict $\\hat{d} \\in \\{0, 1, 2, \\ldots\\}$.\nWe operationalize this as classification into depth classes: gen-0 (human), gen-1 (first-generation synthetic), and gen-2+ (depth $\\geq 2$).\n\n\\subsection{Distributional Fingerprint Features}\n\nWe extract features by scoring text under a \\emph{reference model} $p_{\\text{ref}}$---a small pretrained language model (Pythia-410M by default) that was never fine-tuned on synthetic data.\nFor each token $t_i$ in a text of length $n$, we compute the reference-model negative log-likelihood $\\ell_i = -\\log p_{\\text{ref}}(t_i | t_{&lt;i})$.\n\n\\paragraph{Reference-model features (5).}\nWe compute: (1) $\\texttt{entropy\\_mean} = \\frac{1}{n}\\sum_i \\ell_i$, the average surprise under the reference model; (2) $\\texttt{entropy\\_std}$, the standard deviation of per-token surprises; (3--4) $\\texttt{entropy\\_min}$, $\\texttt{entropy\\_max}$, capturing the range; and (5) $\\texttt{tail\\_decay}$, the fraction of tokens in the top-10\\% surprise quantile, measuring how much text mass falls in the distributional tail.\n\nThe intuition is that deeper-generation text progressively occupies lower-probability regions of the reference model's distribution.\nAs drift accumulates, $\\texttt{entropy\\_mean}$ increases because the reference model is increasingly ``surprised'' by text that has drifted from the human-text manifold.\nThe variance ($\\texttt{entropy\\_std}$) increases because deeper text alternates between familiar patterns and novel drift artifacts.\n\n\\paragraph{Surface features (2).}\nWe include type-token ratio ($\\texttt{ttr}$) and hapax legomenon ratio ($\\texttt{hapax\\_ratio}$) as vocabulary diversity measures.\nThese capture the well-known vocabulary impoverishment effect of language model generation but, as we show, provide weaker and less fine-grained depth signal than reference-model features.\n\n\\subsection{Classifier}\n\nWe train an XGBoost classifier on the 7-dimensional feature vector with 5-fold stratified cross-validation.\nWe chose XGBoost over neural alternatives for interpretability and computational efficiency (training in $\\sim$3 minutes vs.\\ 12 GPU-hours for a fine-tuned LLM baseline; see Section~\\ref{sec:e2e}).\n\n\\subsection{Hypotheses}\n\nWe formalize two competing hypotheses about distributional dynamics in recursive generation:\n\n\\noindent\\textbf{H$_1$ (Convergence):} Non-paraphrastic chains converge to a distributional fixed point, analogous to paraphrastic attractor cycles.\nUnder H$_1$, depth signal saturates after a few generations.\n\n\\noindent\\textbf{H$_2$ (Divergence):} Non-paraphrastic chains accumulate monotonic distributional drift from the human-text manifold.\nUnder H$_2$, depth signal grows with generation depth, enabling ordinal depth estimation.\n\n\\section{Experimental Setup}\n\n\\paragraph{Data generation.}\nWe construct generation chains from 2{,}000 seed texts spanning 4 domains (Wikipedia, CNN/DailyMail news, S2ORC scientific abstracts, WritingPrompts creative fiction), 500 seeds per domain.\nEach seed is extended to depth 5 using 5 generators: Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, and Pythia-1B.\nThree prompt types are used: continuation, elaboration, and inspired rewriting.\nThe resulting dataset contains $\\sim$24{,}200 chains after $\\sim$3.2\\% attrition from generation failures.\n\n\\paragraph{Feature extraction.}\nAll features are extracted using Pythia-410M as the default reference model.\nCross-reference experiments additionally use OLMo-2-1B and Qwen3.5-0.8B.\n\n\\paragraph{Evaluation protocol.}\nUnless otherwise stated, we report macro-F1 over 5-fold stratified cross-validation for the 3-class task (gen-0/gen-1/gen-2+).\nFor generalization experiments, we use leave-one-generator-out and leave-one-domain-out protocols.\n\n\\section{Experiments}\n\n\\subsection{Feature Ablation (Claim 2)}\n\\label{sec:ablation}\n\nWe ablate the 7-feature set into three conditions: (A) reference-only features (5 entropy statistics), (B) surface-only features (TTR, hapax ratio), and (C) the full 7-feature set.\nAll use the same XGBoost classifier with 5-fold stratified CV on the MVP dataset (4{,}609 records, Pythia-2.8B generator, Wikipedia seeds).\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation results (3-class depth classification). Reference-model features alone substantially outperform surface-only features, and the full set achieves the best performance.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nFeature Set & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nReference-only (5) & 0.79 {\\scriptsize$\\pm$0.018} & 0.91 & 0.71 & 0.74 \\\\\nSurface-only (2) & 0.63 {\\scriptsize$\\pm$0.022} & 0.82 & 0.52 & 0.55 \\\\\nFull (7) & \\textbf{0.87} {\\scriptsize$\\pm$0.012} & \\textbf{0.96} & \\textbf{0.81} & \\textbf{0.83} \\\\\n\\midrule\n$\\Delta$ (ref $-$ surface) & +0.16 & +0.09 & +0.19 & +0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation} shows that reference-only features achieve macro-F1 = 0.79, substantially outperforming surface-only features at 0.63 ($\\Delta$ = +0.16, McNemar $p = 3 \\times 10^{-5}$).\nThe advantage is largest for gen-1 and gen-2+ ($\\Delta$ = +0.19 each), precisely the classes where surface features struggle.\nThis is because vocabulary impoverishment (captured by TTR, hapax ratio) saturates between gen-0 and gen-1, while reference-model entropy features capture cumulative distributional drift that continues to grow at deeper depths.\n\nPermutation importance analysis (Table~\\ref{tab:importance}) confirms this pattern: under permutation (which avoids XGBoost's split-gain bias toward high-cardinality features), $\\texttt{entropy\\_mean}$ emerges as the dominant feature (importance = 0.28), while $\\texttt{hapax\\_ratio}$ drops from its inflated XGBoost gain rank.\n\n\\begin{table}[t]\n\\centering\n\\caption{Permutation importance vs.\\ XGBoost gain.}\n\\label{tab:importance}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFeature & Perm.\\ Importance & XGB Gain \\\\\n\\midrule\nentropy\\_mean & \\textbf{0.28} & 0.22 \\\\\nentropy\\_std & 0.19 & 0.13 \\\\\nhapax\\_ratio & 0.14 & 0.30 \\\\\ntail\\_decay & 0.13 & 0.06 \\\\\nttr & 0.09 & 0.17 \\\\\nentropy\\_max & 0.09 & 0.07 \\\\\nentropy\\_min & 0.08 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization (Claim 1)}\n\\label{sec:crossgen}\n\nTo test whether distributional fingerprints generalize beyond any single generator family, we evaluate using leave-one-generator-out cross-validation across 5 generators.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-generator-out cross-validation. The classifier trained on 4 generators generalizes to the held-out generator.}\n\\label{tab:crossgen}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nHeld-out Generator & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-2.8B & 0.81 & 0.91 & 0.75 & 0.77 \\\\\nOLMo-2-1B & 0.77 & 0.87 & 0.72 & 0.73 \\\\\nQwen3.5-2B & 0.76 & 0.86 & 0.71 & 0.72 \\\\\nQwen3.5-0.8B & 0.74 & 0.84 & 0.68 & 0.70 \\\\\nPythia-1B & 0.82 & 0.92 & 0.76 & 0.78 \\\\\n\\midrule\nMean $\\pm$ std & 0.78 $\\pm$ 0.03 & 0.88 & 0.73 & 0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:crossgen} demonstrates consistent generalization: mean leave-one-out F1 = 0.78 $\\pm$ 0.03 across all 5 generators, with gen-0 separation remaining strong ($\\geq$0.84) in all cases.\nCross-family transfer (e.g., Pythia-trained classifier tested on Qwen) maintains F1 $\\geq$ 0.74, confirming that the distributional fingerprint is a property of the generation process rather than a generator-specific artifact.\nIn-distribution pooled performance reaches 0.86, suggesting that multi-generator training improves robustness (Table~\\ref{tab:indist}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-generator in-distribution 5-fold CV.}\n\\label{tab:indist}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nGenerator & Macro-F1 & CV std \\\\\n\\midrule\nPythia-2.8B & 0.85 & 0.014 \\\\\nOLMo-2-1B & 0.84 & 0.016 \\\\\nQwen3.5-2B & 0.86 & 0.013 \\\\\nQwen3.5-0.8B & 0.83 & 0.019 \\\\\nPythia-1B & 0.84 & 0.015 \\\\\n\\midrule\nPooled (all 5) & 0.86 & 0.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Reference Models}\n\nA natural concern is whether the fingerprint depends on the choice of reference model.\nWe re-extract features using OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and compare classification performance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reference model comparison on pooled 5-generator data.}\n\\label{tab:crossref}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nReference Model & Params & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-410M & 410M & 0.86 & 0.95 & 0.80 & 0.82 \\\\\nOLMo-2-1B & 1B & 0.76 & 0.88 & 0.69 & 0.72 \\\\\nQwen3.5-0.8B & 0.8B & 0.74 & 0.86 & 0.66 & 0.70 \\\\\nEnsemble (3 refs) & --- & \\textbf{0.88} & \\textbf{0.96} & \\textbf{0.83} & \\textbf{0.85} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three reference models detect depth signal (F1 $\\geq$ 0.74; Table~\\ref{tab:crossref}), confirming that the fingerprint is not a Pythia-specific artifact.\nHigh cross-reference correlations in entropy features (Spearman $\\rho$ = 0.78--0.82 for $\\texttt{entropy\\_mean}$) indicate that different reference models measure the same underlying drift phenomenon through slightly different lenses.\nThe 3-reference ensemble achieves F1 = 0.88, suggesting that diverse reference models capture complementary drift aspects.\n\n\\subsection{Paraphrastic vs.\\ Non-Paraphrastic Chains (H$_1$ vs.\\ H$_2$)}\n\\label{sec:h1h2}\n\nWe directly test H$_1$ vs.\\ H$_2$ by constructing parallel paraphrasing and continuation chains from the same 1{,}000 seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain comparison. Continuation chains show monotonic divergence (H$_2$); paraphrastic chains converge (H$_1$).}\n\\label{tab:h1h2}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nChain Type & Macro-F1 & Entropy Drift @d3 & Cycle \\% \\\\\n\\midrule\nContinuation & 0.85 & 0.52 nats & $<5\\%$ \\\\\nParaphrasing & 0.58 & 0.06 nats & 68\\% \\\\\n\\midrule\n$\\Delta$ & +0.27 & +0.46 nats & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:h1h2} provides definitive evidence.\nContinuation chains accumulate substantial entropy drift (0.52 nats by depth 3) with strong depth classification (F1 = 0.85), while paraphrastic chains show near-zero drift (0.06 nats) and weak classification (F1 = 0.58).\nThe 68\\% cycle detection rate in paraphrastic chains---where text at depth $d$ is more similar to depth $d{-}2$ than $d{-}1$---directly corroborates the attractor cycle prediction of~\\cite{briesch2025attractor}.\nA two-sample Kolmogorov-Smirnov test on the depth-3 entropy distributions yields $D = 0.41$, $p < 10^{-4}$, confirming that the two chain types occupy distinct distributional regimes.\nH$_2$ holds for non-paraphrastic chains; H$_1$ holds for paraphrastic chains.\n\n\\subsection{Downstream Utility (Claim 3)}\n\\label{sec:downstream}\n\nWe validate the practical value of depth estimation by fine-tuning Pythia-410M on depth-stratified data subsets and measuring perplexity on a held-out human test set.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning perplexity by training data depth. Perplexity increases monotonically with depth ($\\rho = 0.72$).}\n\\label{tab:ppl}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nTraining Data & Depth & PPL ($\\downarrow$) & Samples \\\\\n\\midrule\nHuman-only & gen-0 & 28.3 & $\\sim$4{,}800 \\\\\ngen-1 only & gen-1 & 30.1 & $\\sim$4{,}750 \\\\\ngen-2 only & gen-2 & 34.7 & $\\sim$4{,}500 \\\\\ngen-3 only & gen-3 & 38.9 & $\\sim$4{,}200 \\\\\ngen-4 only & gen-4 & 43.2 & $\\sim$3{,}900 \\\\\nUniform mix & gen-0--4 & 35.8 & $\\sim$22{,}000 \\\\\n\\midrule\nDepth-filtered (ours) & gen-0+1 & \\textbf{29.0} & $\\sim$9{,}500 \\\\\nFastDetectGPT filter & binary & 31.8 & $\\sim$6{,}300 \\\\\nLD-Score filter & binary & 32.1 & $\\sim$6{,}100 \\\\\n\\midrule\nHuman test baseline & --- & 27.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ppl} demonstrates a monotonic relationship between training data depth and downstream perplexity (Spearman $\\rho = 0.72$), providing an intuitive translation of distributional drift into a metric practitioners care about.\nDepth-aware filtering (keep gen-0 + gen-1) achieves perplexity 29.0---within 0.7 points of the human-only baseline---while binary baselines achieve 31.8--32.1.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth-aware vs.\\ binary filtering. Depth-aware filtering retains more data at lower perplexity.}\n\\label{tab:filter}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & PPL & Retained & $\\Delta$ Human \\\\\n\\midrule\nDepth-filtered (gen-0+1) & \\textbf{29.0} & 42\\% & +0.7 \\\\\nFastDetectGPT binary & 31.8 & 28\\% & +3.5 \\\\\nLD-Score binary & 32.1 & 26\\% & +3.8 \\\\\nNo filtering & 35.8 & 100\\% & +7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe key practical insight (Table~\\ref{tab:filter}): gen-1 text is ``good enough'' for training (PPL = 30.1 vs.\\ human 28.3), but gen-2+ is not (PPL $\\geq$ 34.7).\nBinary detectors cannot make this distinction.\nDepth-aware filtering retains 42\\% of data (vs.\\ 28\\% for binary filtering), resolving the precision--recall tradeoff that plagues binary detection.\n\n\\subsection{Prompt Type Analysis}\n\\label{sec:prompt}\n\nWe compare depth signal across three prompt types: continuation, elaboration, and inspired rewriting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth classification by prompt type. More constrained generation produces stronger depth signal.}\n\\label{tab:prompt}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:prompt} reveals a graded relationship: the more a generation task constrains the output to build on previous text, the faster drift accumulates.\nContinuation (maximum constraint) yields the strongest signal; inspired rewriting (maximum freedom) yields the weakest.\nThe strong correlation between per-depth entropy drift rate and classification F1 (Spearman $\\rho = 0.91$) confirms the theoretical prediction that drift accumulation rate determines depth discriminability.\nCross-prompt-type transfer achieves F1 = 0.74, indicating partially shared but rate-differentiated drift signatures.\n\n\\subsection{Cross-Model Chains}\n\nReal-world contamination involves diverse generators at different depths.\nWe construct cross-model chains where each depth step uses a randomly sampled generator.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain comparison.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nChain Type & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nSingle-model (mean) & 0.85 & 0.95 & 0.79 & 0.81 \\\\\nCross-model & 0.75 & 0.90 & 0.68 & 0.67 \\\\\n\\midrule\n$\\Delta$ & $-$0.10 & $-$0.05 & $-$0.11 & $-$0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains incur a 10-point F1 drop (Table~\\ref{tab:crossmodel})---the honest cost of ecological validity.\nGenerator switching introduces distributional discontinuities that partially mask the monotonic drift signal.\nHowever, F1 = 0.75 remains well above chance (0.33), and gen-0 separation is robust (F1 = 0.90), preserving the method's primary utility for separating human from synthetic text.\n\n\\subsection{Multi-Domain Evaluation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain depth classification. Depth signal is domain-general, strongest for factual text.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nDomain & Seeds & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.86 & 0.95 & 0.80 & 0.82 \\\\\nNews & 500 & 0.83 & 0.93 & 0.77 & 0.79 \\\\\nScientific & 500 & 0.81 & 0.91 & 0.74 & 0.77 \\\\\nCreative & 500 & 0.78 & 0.88 & 0.71 & 0.74 \\\\\n\\midrule\nPooled & 2{,}000 & 0.84 & 0.93 & 0.78 & 0.80 \\\\\nLeave-one-out & --- & 0.77 & 0.88 & 0.70 & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:domain} confirms domain generalization across 4 text types.\nThe ordering (factual $>$ creative) is interpretable: generators produce more fluent creative text with smaller human--synthetic distributional gaps, reducing overall drift magnitude.\nLeave-one-domain-out F1 = 0.77 with low cross-domain variance ($\\sigma^2$ = 0.0009) demonstrates that depth signal is a robust, domain-general phenomenon.\n\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nWe test whether non-paraphrastic chains support depth resolution beyond 3 classes.\n\n\\begin{table}[t]\n\\centering\n\\caption{5-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.93 & 0.91 & 0.92 \\\\\ngen-1 & 0.66 & 0.70 & 0.68 \\\\\ngen-2 & 0.50 & 0.54 & 0.52 \\\\\ngen-3 & 0.47 & 0.49 & 0.48 \\\\\ngen-4 & 0.53 & 0.50 & 0.51 \\\\\n\\midrule\nMacro & --- & --- & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class macro-F1 is 0.62 (Table~\\ref{tab:ordinal}), lower than the 3-class result due to overlapping feature distributions at deep classes.\nHowever, the ordinal structure is preserved: Spearman $\\rho = 0.83$ between predicted and true depth, with MAE = 0.58 and 72\\% of errors being off-by-one.\nThis confirms that drift is monotonic (supporting H$_2$) while establishing a practical resolution ceiling: 3-class coarse bucketing is more reliable than exact depth prediction for data curation purposes.\n\n\\subsection{Robustness to Post-Generation Editing}\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to simulated post-generation edits.}\n\\label{tab:robust}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nEdit Type & Rate & Macro-F1 & $\\Delta$ \\\\\n\\midrule\nNone (baseline) & 0\\% & 0.86 & --- \\\\\nRandom word replacement & 5\\% & 0.83 & $-$0.03 \\\\\nRandom word replacement & 10\\% & 0.78 & $-$0.08 \\\\\nRandom word replacement & 20\\% & 0.67 & $-$0.19 \\\\\nLLM light editing & $\\sim$8--12\\% & 0.76 & $-$0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:robust} characterizes degradation under post-generation editing.\nLight editing (5\\%) typical of human post-processing preserves most depth signal ($\\Delta$ = $-$0.03).\nDegradation is approximately linear ($-$0.095 F1 per 10\\% edit rate), providing a simple model for practitioners to assess reliability.\nEven at 20\\% editing, performance (F1 = 0.67) remains well above chance.\n\n\\subsection{LD-Score Feature Integration}\n\n\\begin{table}[t]\n\\centering\n\\caption{LD-Score feature integration.}\n\\label{tab:ld}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFeature Set & Macro-F1 & $\\Delta$ from Full \\\\\n\\midrule\nFull (7 features) & 0.87 & --- \\\\\nFull + LD-Score & 0.88 & +0.01 \\\\\nLD-Score only & 0.59 & $-$0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding LD-Score~\\cite{dugan2024ldscore} as an 8th feature provides marginal improvement ($\\Delta$ = +0.01; Table~\\ref{tab:ld}).\nLD-Score alone achieves only F1 = 0.59 with low permutation importance (0.06), confirming that character-level distributional signatures are largely redundant with existing surface features---both measure vocabulary impoverishment at different granularities.\nThis reinforces that reference-model entropy features, not surface-level statistics, are the novel signal source.\n\n\\subsection{End-to-End Neural Baseline}\n\\label{sec:e2e}\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature-based vs.\\ end-to-end neural comparison.}\n\\label{tab:e2e}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & In-Dist F1 & Cross-Gen F1 & Cost \\\\\n\\midrule\nXGBoost + features & \\textbf{0.86} & \\textbf{0.78} & 3 min \\\\\nQLoRA Qwen3.5-0.8B & 0.83 & 0.71 & 12 GPU$\\cdot$h \\\\\n\\midrule\n$\\Delta$ & +0.03 & +0.07 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe compare against a QLoRA-fine-tuned Qwen3.5-0.8B as an end-to-end neural baseline (Table~\\ref{tab:e2e}).\nThe handcrafted feature approach outperforms on both in-distribution (+0.03) and cross-generator (+0.07) F1, while being $\\sim$240$\\times$ cheaper to train.\nThe larger cross-generator gap reveals that the fine-tuned model memorizes generator-specific artifacts, while handcrafted features are designed to capture generator-invariant distributional drift.\n\n\\section{Discussion}\n\n\\paragraph{Theoretical implications.}\nOur results establish a clean dichotomy in recursive generation dynamics: paraphrastic chains converge (H$_1$), non-paraphrastic chains diverge (H$_2$).\nThis distinction arises from the presence or absence of a semantic-preservation constraint: paraphrasing re-anchors to a fixed semantic target at each step, while continuation explores an unbounded state space where distributional drift accumulates.\nThe prompt type analysis (Section~\\ref{sec:prompt}) reveals this is a spectrum, not a binary---elaboration lies between continuation and paraphrasing in drift rate.\n\n\\paragraph{Practical implications for data curation.}\nDistributional fingerprints enable \\emph{risk-stratified} data governance: rather than binary accept/reject decisions, practitioners can assign depth-derived risk scores and set thresholds appropriate to their quality requirements.\nOur downstream experiments show that gen-1 text is nearly as valuable as human text for training (perplexity gap of 1.8 points), while gen-2+ text introduces meaningful quality degradation.\nDepth-aware filtering achieves the best quality--quantity tradeoff: 42\\% data retention at near-human quality, vs.\\ 28\\% retention with worse quality under binary filtering.\n\n\\paragraph{Limitations.}\nThe method's primary limitation is sensitivity to post-generation editing ($-$0.095 F1 per 10\\% edit rate).\nCross-model chains reduce accuracy by 10 points compared to single-model chains.\nFiner-grained depth estimation (5-class) has limited precision for depths $\\geq$2, though ordinal structure is preserved.\nAll experiments use models $\\leq$2.8B parameters; scaling to larger generators requires further investigation.\n\n\\section{Conclusion}\n\nWe introduced distributional fingerprinting for generation depth estimation, demonstrating that non-paraphrastic LLM generation chains exhibit monotonic distributional divergence detectable via reference-model entropy features.\nOur 7-feature classifier achieves macro-F1 = 0.87 for 3-class depth estimation, generalizes across 5 generator families (leave-one-out F1 = 0.78), and enables depth-aware data curation that outperforms binary detection baselines by 5.2\\% in downstream quality while retaining 50\\% more training data.\nThe clean separation between convergent paraphrastic chains and divergent non-paraphrastic chains provides a unified framework connecting attractor cycle theory to the distributional dynamics of recursive text generation.\n\n\\bibliographystyle{aaai26}\n\n\\begin{thebibliography}{10}\n\n\\bibitem{shumailov2024model}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759, 2024.\n\n\\bibitem{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and J.~Zhang.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In {\\em Proc.\\ ICLR}, 2024.\n\n\\bibitem{dathathri2024synthid}\nS.~Dathathri, A.~See, S.~Ghaisas, P.-S.~Huang, R.~McAdam, J.~Welbl, V.~Bachani, A.~Kaskasoli, R.~Stanforth, T.~Matejovicova, et~al.\n\\newblock Scalable watermarking for identifying large language model outputs.\n\\newblock {\\em Nature}, 634:818--823, 2024.\n\n\\bibitem{dugan2024ldscore}\nL.~Dugan, H.~Hwang, F.~Trhl{\\'\\i}k, A.~Ladhak, A.~Ippolito, and C.~Callison-Burch.\n\\newblock {LD}-Score: A character-level metric for distinguishing human from machine-generated text.\n\\newblock {\\em arXiv preprint arXiv:2605.01647}, 2025.\n\n\\bibitem{briesch2025attractor}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models are attractor cycles of iterative paraphrasing.\n\\newblock In {\\em Proc.\\ ACL}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80c922ae-f0c5-4741-b144-b7d340ce682a",
  "isSidechain": false,
  "requestId": "req_011Cb2wCNyvezsM4UunMor6V",
  "type": "assistant",
  "uuid": "4fa77b44-8748-43d1-9393-1b71ee10f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhsp67dT3zNBLJucokr8M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 39501,
      "output_tokens": 10528,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10528,
          "cache_read_input_tokens": 39501,
          "cache_creation_input_tokens": 285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 285
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

_source line 18 · 2026-05-14T18:31:56.992Z_

<details><summary>↩ Tool result · `toolu_01Hn3N1EK9HVgcw4bTDsWKyZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fa77b44-8748-43d1-9393-1b71ee10f6de",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "b746b74a-77b5-4af2-ba29-152811430497",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\setlength\\titlebox{2.5in}\n\n\\title{Distributional Fingerprints of Generation Depth:\\\\Detecting Recursive LLM Contamination Beyond Binary Classification}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth---text generated by models that were themselves trained on synthetic data.\nCurrent detection methods provide only binary real-vs-synthetic classification, forcing all-or-nothing filtering that either discards useful first-generation content or admits deeply contaminated text with compounding distributional drift.\nWe introduce \\emph{distributional fingerprinting}, a method that estimates the generation depth of text by measuring its distributional divergence from human text under a small reference language model.\nWe formalize and test two competing hypotheses for non-paraphrastic generation chains: convergence to a distributional fixed point (H$_1$) versus monotonic divergence (H$_2$).\nOur experiments across 5 generators, 4 text domains, and 3 prompt types confirm H$_2$: non-paraphrastic chains exhibit monotonic distributional drift detectable via reference-model entropy features.\nOn multi-generator continuation chains, our 7-feature classifier achieves macro-F1 of 0.87 for 3-class depth estimation (gen-0/gen-1/gen-2+) and generalizes to unseen generators with leave-one-out F1 of 0.78.\nFeature ablation shows reference-model entropy features carry independent signal beyond surface vocabulary impoverishment ($\\Delta$F1 = +0.16, McNemar $p < 10^{-4}$).\nDepth-aware data filtering retains 42\\% of training data while achieving perplexity within 0.7 points of human-only baselines---outperforming binary detection baselines by 5.2\\% while retaining 50\\% more data.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe recursive contamination of training data by LLM outputs is an accelerating concern.\nAs language models are deployed at scale, their outputs enter the web, are scraped into training corpora, and are used to train the next generation of models~\\cite{shumailov2024model}.\nThis creates generation chains: text at \\emph{depth~0} is human-written, depth~1 is generated from human text, depth~2 is generated from depth-1 text, and so forth.\nThe distributional consequences of this recursive process are poorly understood.\n\nExisting detection methods---FastDetectGPT, SynthID-Text, LD-Score~\\cite{bao2024fastdetectgpt, dathathri2024synthid, dugan2024ldscore}---operate in a binary paradigm: text is classified as real or synthetic.\nThis forces a lossy tradeoff.\nAggressive filtering discards all flagged text, including first-generation content that is distributionally close to human text and useful for training.\nPermissive filtering admits deeply generated text with compounding distributional artifacts.\nNeither approach is adequate for risk-stratified data governance.\n\nAttractor cycle theory~\\cite{briesch2025attractor} has established that \\emph{paraphrastic} generation chains converge to 2-period distributional cycles, bounding depth discriminability to roughly 3 classes.\nHowever, this result depends on the semantic-preservation constraint inherent to paraphrasing.\nNon-paraphrastic chains---continuations, elaborations, and other open-ended generation tasks---operate in an unbounded semantic state space.\nWhether distributional drift in such chains converges (H$_1$) or diverges monotonically (H$_2$) remains an open empirical question.\n\nWe address this question by introducing \\emph{distributional fingerprinting}: computing token-level statistics under a small reference language model to characterize the distributional displacement of text from the human-text manifold.\nOur method extracts 7 features---5 reference-model entropy statistics and 2 surface vocabulary statistics---and uses an XGBoost classifier for ordinal depth estimation.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Empirical confirmation of H$_2$}: Non-paraphrastic generation chains exhibit monotonic distributional divergence, in contrast to the convergence observed in paraphrastic chains. This is demonstrated by direct comparison of continuation vs.\\ paraphrasing chains (KS statistic $D = 0.41$, $p < 10^{-4}$).\n    \\item \\textbf{Cross-generator depth classification}: Our distributional fingerprint achieves macro-F1 = 0.87 (3-class) and generalizes across 5 generator families with leave-one-generator-out F1 = 0.78 $\\pm$ 0.03.\n    \\item \\textbf{Risk-stratified data curation}: Depth-aware filtering outperforms binary baselines by 5.2\\% in downstream perplexity while retaining 50\\% more training data.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Synthetic text detection.}\nBinary detection methods assign a real/synthetic label to text.\nFastDetectGPT~\\cite{bao2024fastdetectgpt} uses conditional probability curvature, SynthID-Text~\\cite{dathathri2024synthid} embeds statistical watermarks, and LD-Score~\\cite{dugan2024ldscore} uses character-level distributional signatures.\nAll are binary classifiers that cannot distinguish generation depth.\n\n\\paragraph{Model collapse and iterative retraining.}\nShumailov et al.~\\cite{shumailov2024model} demonstrate that iterative retraining on model outputs leads to distributional collapse, with progressive loss of low-frequency modes.\nTheir analysis focuses on full-model retraining dynamics rather than individual text-level depth estimation.\n\n\\paragraph{Attractor cycles in paraphrasing chains.}\nBriesch et al.~\\cite{briesch2025attractor} prove that iterative paraphrasing converges to 2-period distributional cycles, where semantic content oscillates between two attractors.\nThis convergence limits depth discriminability for paraphrastic chains.\nOur work complements theirs by studying non-paraphrastic chains, where the absence of semantic preservation constraints leads to qualitatively different dynamics.\n\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nLet $\\mathcal{G}$ be a text generator and $x^{(0)}$ be a human-authored seed text.\nA \\emph{generation chain} of depth $d$ produces a sequence $x^{(0)}, x^{(1)}, \\ldots, x^{(d)}$ where $x^{(k)} = \\mathcal{G}(x^{(k-1)})$.\nGiven a text sample $x$ drawn from an unknown depth, the depth estimation task is to predict $\\hat{d} \\in \\{0, 1, 2, \\ldots\\}$.\nWe operationalize this as classification into depth classes: gen-0 (human), gen-1 (first-generation synthetic), and gen-2+ (depth $\\geq 2$).\n\n\\subsection{Distributional Fingerprint Features}\n\nWe extract features by scoring text under a \\emph{reference model} $p_{\\text{ref}}$---a small pretrained language model (Pythia-410M by default) that was never fine-tuned on synthetic data.\nFor each token $t_i$ in a text of length $n$, we compute the reference-model negative log-likelihood $\\ell_i = -\\log p_{\\text{ref}}(t_i | t_{&lt;i})$.\n\n\\paragraph{Reference-model features (5).}\nWe compute: (1) $\\texttt{entropy\\_mean} = \\frac{1}{n}\\sum_i \\ell_i$, the average surprise under the reference model; (2) $\\texttt{entropy\\_std}$, the standard deviation of per-token surprises; (3--4) $\\texttt{entropy\\_min}$, $\\texttt{entropy\\_max}$, capturing the range; and (5) $\\texttt{tail\\_decay}$, the fraction of tokens in the top-10\\% surprise quantile, measuring how much text mass falls in the distributional tail.\n\nThe intuition is that deeper-generation text progressively occupies lower-probability regions of the reference model's distribution.\nAs drift accumulates, $\\texttt{entropy\\_mean}$ increases because the reference model is increasingly ``surprised'' by text that has drifted from the human-text manifold.\nThe variance ($\\texttt{entropy\\_std}$) increases because deeper text alternates between familiar patterns and novel drift artifacts.\n\n\\paragraph{Surface features (2).}\nWe include type-token ratio ($\\texttt{ttr}$) and hapax legomenon ratio ($\\texttt{hapax\\_ratio}$) as vocabulary diversity measures.\nThese capture the well-known vocabulary impoverishment effect of language model generation but, as we show, provide weaker and less fine-grained depth signal than reference-model features.\n\n\\subsection{Classifier}\n\nWe train an XGBoost classifier on the 7-dimensional feature vector with 5-fold stratified cross-validation.\nWe chose XGBoost over neural alternatives for interpretability and computational efficiency (training in $\\sim$3 minutes vs.\\ 12 GPU-hours for a fine-tuned LLM baseline; see Section~\\ref{sec:e2e}).\n\n\\subsection{Hypotheses}\n\nWe formalize two competing hypotheses about distributional dynamics in recursive generation:\n\n\\noindent\\textbf{H$_1$ (Convergence):} Non-paraphrastic chains converge to a distributional fixed point, analogous to paraphrastic attractor cycles.\nUnder H$_1$, depth signal saturates after a few generations.\n\n\\noindent\\textbf{H$_2$ (Divergence):} Non-paraphrastic chains accumulate monotonic distributional drift from the human-text manifold.\nUnder H$_2$, depth signal grows with generation depth, enabling ordinal depth estimation.\n\n\\section{Experimental Setup}\n\n\\paragraph{Data generation.}\nWe construct generation chains from 2{,}000 seed texts spanning 4 domains (Wikipedia, CNN/DailyMail news, S2ORC scientific abstracts, WritingPrompts creative fiction), 500 seeds per domain.\nEach seed is extended to depth 5 using 5 generators: Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, and Pythia-1B.\nThree prompt types are used: continuation, elaboration, and inspired rewriting.\nThe resulting dataset contains $\\sim$24{,}200 chains after $\\sim$3.2\\% attrition from generation failures.\n\n\\paragraph{Feature extraction.}\nAll features are extracted using Pythia-410M as the default reference model.\nCross-reference experiments additionally use OLMo-2-1B and Qwen3.5-0.8B.\n\n\\paragraph{Evaluation protocol.}\nUnless otherwise stated, we report macro-F1 over 5-fold stratified cross-validation for the 3-class task (gen-0/gen-1/gen-2+).\nFor generalization experiments, we use leave-one-generator-out and leave-one-domain-out protocols.\n\n\\section{Experiments}\n\n\\subsection{Feature Ablation (Claim 2)}\n\\label{sec:ablation}\n\nWe ablate the 7-feature set into three conditions: (A) reference-only features (5 entropy statistics), (B) surface-only features (TTR, hapax ratio), and (C) the full 7-feature set.\nAll use the same XGBoost classifier with 5-fold stratified CV on the MVP dataset (4{,}609 records, Pythia-2.8B generator, Wikipedia seeds).\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation results (3-class depth classification). Reference-model features alone substantially outperform surface-only features, and the full set achieves the best performance.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nFeature Set & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nReference-only (5) & 0.79 {\\scriptsize$\\pm$0.018} & 0.91 & 0.71 & 0.74 \\\\\nSurface-only (2) & 0.63 {\\scriptsize$\\pm$0.022} & 0.82 & 0.52 & 0.55 \\\\\nFull (7) & \\textbf{0.87} {\\scriptsize$\\pm$0.012} & \\textbf{0.96} & \\textbf{0.81} & \\textbf{0.83} \\\\\n\\midrule\n$\\Delta$ (ref $-$ surface) & +0.16 & +0.09 & +0.19 & +0.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation} shows that reference-only features achieve macro-F1 = 0.79, substantially outperforming surface-only features at 0.63 ($\\Delta$ = +0.16, McNemar $p = 3 \\times 10^{-5}$).\nThe advantage is largest for gen-1 and gen-2+ ($\\Delta$ = +0.19 each), precisely the classes where surface features struggle.\nThis is because vocabulary impoverishment (captured by TTR, hapax ratio) saturates between gen-0 and gen-1, while reference-model entropy features capture cumulative distributional drift that continues to grow at deeper depths.\n\nPermutation importance analysis (Table~\\ref{tab:importance}) confirms this pattern: under permutation (which avoids XGBoost's split-gain bias toward high-cardinality features), $\\texttt{entropy\\_mean}$ emerges as the dominant feature (importance = 0.28), while $\\texttt{hapax\\_ratio}$ drops from its inflated XGBoost gain rank.\n\n\\begin{table}[t]\n\\centering\n\\caption{Permutation importance vs.\\ XGBoost gain.}\n\\label{tab:importance}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFeature & Perm.\\ Importance & XGB Gain \\\\\n\\midrule\nentropy\\_mean & \\textbf{0.28} & 0.22 \\\\\nentropy\\_std & 0.19 & 0.13 \\\\\nhapax\\_ratio & 0.14 & 0.30 \\\\\ntail\\_decay & 0.13 & 0.06 \\\\\nttr & 0.09 & 0.17 \\\\\nentropy\\_max & 0.09 & 0.07 \\\\\nentropy\\_min & 0.08 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization (Claim 1)}\n\\label{sec:crossgen}\n\nTo test whether distributional fingerprints generalize beyond any single generator family, we evaluate using leave-one-generator-out cross-validation across 5 generators.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-generator-out cross-validation. The classifier trained on 4 generators generalizes to the held-out generator.}\n\\label{tab:crossgen}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nHeld-out Generator & Macro-F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-2.8B & 0.81 & 0.91 & 0.75 & 0.77 \\\\\nOLMo-2-1B & 0.77 & 0.87 & 0.72 & 0.73 \\\\\nQwen3.5-2B & 0.76 & 0.86 & 0.71 & 0.72 \\\\\nQwen3.5-0.8B & 0.74 & 0.84 & 0.68 & 0.70 \\\\\nPythia-1B & 0.82 & 0.92 & 0.76 & 0.78 \\\\\n\\midrule\nMean $\\pm$ std & 0.78 $\\pm$ 0.03 & 0.88 & 0.73 & 0.75 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:crossgen} demonstrates consistent generalization: mean leave-one-out F1 = 0.78 $\\pm$ 0.03 across all 5 generators, with gen-0 separation remaining strong ($\\geq$0.84) in all cases.\nCross-family transfer (e.g., Pythia-trained classifier tested on Qwen) maintains F1 $\\geq$ 0.74, confirming that the distributional fingerprint is a property of the generation process rather than a generator-specific artifact.\nIn-distribution pooled performance reaches 0.86, suggesting that multi-generator training improves robustness (Table~\\ref{tab:indist}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-generator in-distribution 5-fold CV.}\n\\label{tab:indist}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nGenerator & Macro-F1 & CV std \\\\\n\\midrule\nPythia-2.8B & 0.85 & 0.014 \\\\\nOLMo-2-1B & 0.84 & 0.016 \\\\\nQwen3.5-2B & 0.86 & 0.013 \\\\\nQwen3.5-0.8B & 0.83 & 0.019 \\\\\nPythia-1B & 0.84 & 0.015 \\\\\n\\midrule\nPooled (all 5) & 0.86 & 0.011 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Family Reference Models}\n\nA natural concern is whether the fingerprint depends on the choice of reference model.\nWe re-extract features using OLMo-2-1B and Qwen3.5-0.8B as alternative reference models, and compare classification performance.\n\n\\begin{table}[t]\n\\centering\n\\caption{Reference model comparison on pooled 5-generator data.}\n\\label{tab:crossref}\n\\small\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nReference Model & Params & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nPythia-410M & 410M & 0.86 & 0.95 & 0.80 & 0.82 \\\\\nOLMo-2-1B & 1B & 0.76 & 0.88 & 0.69 & 0.72 \\\\\nQwen3.5-0.8B & 0.8B & 0.74 & 0.86 & 0.66 & 0.70 \\\\\nEnsemble (3 refs) & --- & \\textbf{0.88} & \\textbf{0.96} & \\textbf{0.83} & \\textbf{0.85} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll three reference models detect depth signal (F1 $\\geq$ 0.74; Table~\\ref{tab:crossref}), confirming that the fingerprint is not a Pythia-specific artifact.\nHigh cross-reference correlations in entropy features (Spearman $\\rho$ = 0.78--0.82 for $\\texttt{entropy\\_mean}$) indicate that different reference models measure the same underlying drift phenomenon through slightly different lenses.\nThe 3-reference ensemble achieves F1 = 0.88, suggesting that diverse reference models capture complementary drift aspects.\n\n\\subsection{Paraphrastic vs.\\ Non-Paraphrastic Chains (H$_1$ vs.\\ H$_2$)}\n\\label{sec:h1h2}\n\nWe directly test H$_1$ vs.\\ H$_2$ by constructing parallel paraphrasing and continuation chains from the same 1{,}000 seeds.\n\n\\begin{table}[t]\n\\centering\n\\caption{Paraphrastic vs.\\ continuation chain comparison. Continuation chains show monotonic divergence (H$_2$); paraphrastic chains converge (H$_1$).}\n\\label{tab:h1h2}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nChain Type & Macro-F1 & Entropy Drift @d3 & Cycle \\% \\\\\n\\midrule\nContinuation & 0.85 & 0.52 nats & $<5\\%$ \\\\\nParaphrasing & 0.58 & 0.06 nats & 68\\% \\\\\n\\midrule\n$\\Delta$ & +0.27 & +0.46 nats & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:h1h2} provides definitive evidence.\nContinuation chains accumulate substantial entropy drift (0.52 nats by depth 3) with strong depth classification (F1 = 0.85), while paraphrastic chains show near-zero drift (0.06 nats) and weak classification (F1 = 0.58).\nThe 68\\% cycle detection rate in paraphrastic chains---where text at depth $d$ is more similar to depth $d{-}2$ than $d{-}1$---directly corroborates the attractor cycle prediction of~\\cite{briesch2025attractor}.\nA two-sample Kolmogorov-Smirnov test on the depth-3 entropy distributions yields $D = 0.41$, $p < 10^{-4}$, confirming that the two chain types occupy distinct distributional regimes.\nH$_2$ holds for non-paraphrastic chains; H$_1$ holds for paraphrastic chains.\n\n\\subsection{Downstream Utility (Claim 3)}\n\\label{sec:downstream}\n\nWe validate the practical value of depth estimation by fine-tuning Pythia-410M on depth-stratified data subsets and measuring perplexity on a held-out human test set.\n\n\\begin{table}[t]\n\\centering\n\\caption{Fine-tuning perplexity by training data depth. Perplexity increases monotonically with depth ($\\rho = 0.72$).}\n\\label{tab:ppl}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nTraining Data & Depth & PPL ($\\downarrow$) & Samples \\\\\n\\midrule\nHuman-only & gen-0 & 28.3 & $\\sim$4{,}800 \\\\\ngen-1 only & gen-1 & 30.1 & $\\sim$4{,}750 \\\\\ngen-2 only & gen-2 & 34.7 & $\\sim$4{,}500 \\\\\ngen-3 only & gen-3 & 38.9 & $\\sim$4{,}200 \\\\\ngen-4 only & gen-4 & 43.2 & $\\sim$3{,}900 \\\\\nUniform mix & gen-0--4 & 35.8 & $\\sim$22{,}000 \\\\\n\\midrule\nDepth-filtered (ours) & gen-0+1 & \\textbf{29.0} & $\\sim$9{,}500 \\\\\nFastDetectGPT filter & binary & 31.8 & $\\sim$6{,}300 \\\\\nLD-Score filter & binary & 32.1 & $\\sim$6{,}100 \\\\\n\\midrule\nHuman test baseline & --- & 27.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ppl} demonstrates a monotonic relationship between training data depth and downstream perplexity (Spearman $\\rho = 0.72$), providing an intuitive translation of distributional drift into a metric practitioners care about.\nDepth-aware filtering (keep gen-0 + gen-1) achieves perplexity 29.0---within 0.7 points of the human-only baseline---while binary baselines achieve 31.8--32.1.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth-aware vs.\\ binary filtering. Depth-aware filtering retains more data at lower perplexity.}\n\\label{tab:filter}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & PPL & Retained & $\\Delta$ Human \\\\\n\\midrule\nDepth-filtered (gen-0+1) & \\textbf{29.0} & 42\\% & +0.7 \\\\\nFastDetectGPT binary & 31.8 & 28\\% & +3.5 \\\\\nLD-Score binary & 32.1 & 26\\% & +3.8 \\\\\nNo filtering & 35.8 & 100\\% & +7.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe key practical insight (Table~\\ref{tab:filter}): gen-1 text is ``good enough'' for training (PPL = 30.1 vs.\\ human 28.3), but gen-2+ is not (PPL $\\geq$ 34.7).\nBinary detectors cannot make this distinction.\nDepth-aware filtering retains 42\\% of data (vs.\\ 28\\% for binary filtering), resolving the precision--recall tradeoff that plagues binary detection.\n\n\\subsection{Prompt Type Analysis}\n\\label{sec:prompt}\n\nWe compare depth signal across three prompt types: continuation, elaboration, and inspired rewriting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth classification by prompt type. More constrained generation produces stronger depth signal.}\n\\label{tab:prompt}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:prompt} reveals a graded relationship: the more a generation task constrains the output to build on previous text, the faster drift accumulates.\nContinuation (maximum constraint) yields the strongest signal; inspired rewriting (maximum freedom) yields the weakest.\nThe strong correlation between per-depth entropy drift rate and classification F1 (Spearman $\\rho = 0.91$) confirms the theoretical prediction that drift accumulation rate determines depth discriminability.\nCross-prompt-type transfer achieves F1 = 0.74, indicating partially shared but rate-differentiated drift signatures.\n\n\\subsection{Cross-Model Chains}\n\nReal-world contamination involves diverse generators at different depths.\nWe construct cross-model chains where each depth step uses a randomly sampled generator.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-model vs.\\ cross-model chain comparison.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nChain Type & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nSingle-model (mean) & 0.85 & 0.95 & 0.79 & 0.81 \\\\\nCross-model & 0.75 & 0.90 & 0.68 & 0.67 \\\\\n\\midrule\n$\\Delta$ & $-$0.10 & $-$0.05 & $-$0.11 & $-$0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-model chains incur a 10-point F1 drop (Table~\\ref{tab:crossmodel})---the honest cost of ecological validity.\nGenerator switching introduces distributional discontinuities that partially mask the monotonic drift signal.\nHowever, F1 = 0.75 remains well above chance (0.33), and gen-0 separation is robust (F1 = 0.90), preserving the method's primary utility for separating human from synthetic text.\n\n\\subsection{Multi-Domain Evaluation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain depth classification. Depth signal is domain-general, strongest for factual text.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nDomain & Seeds & F1 & gen-0 & gen-1 & gen-2+ \\\\\n\\midrule\nWikipedia & 500 & 0.86 & 0.95 & 0.80 & 0.82 \\\\\nNews & 500 & 0.83 & 0.93 & 0.77 & 0.79 \\\\\nScientific & 500 & 0.81 & 0.91 & 0.74 & 0.77 \\\\\nCreative & 500 & 0.78 & 0.88 & 0.71 & 0.74 \\\\\n\\midrule\nPooled & 2{,}000 & 0.84 & 0.93 & 0.78 & 0.80 \\\\\nLeave-one-out & --- & 0.77 & 0.88 & 0.70 & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:domain} confirms domain generalization across 4 text types.\nThe ordering (factual $>$ creative) is interpretable: generators produce more fluent creative text with smaller human--synthetic distributional gaps, reducing overall drift magnitude.\nLeave-one-domain-out F1 = 0.77 with low cross-domain variance ($\\sigma^2$ = 0.0009) demonstrates that depth signal is a robust, domain-general phenomenon.\n\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nWe test whether non-paraphrastic chains support depth resolution beyond 3 classes.\n\n\\begin{table}[t]\n\\centering\n\\caption{5-class ordinal depth classification.}\n\\label{tab:ordinal}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nClass & Precision & Recall & F1 \\\\\n\\midrule\ngen-0 & 0.93 & 0.91 & 0.92 \\\\\ngen-1 & 0.66 & 0.70 & 0.68 \\\\\ngen-2 & 0.50 & 0.54 & 0.52 \\\\\ngen-3 & 0.47 & 0.49 & 0.48 \\\\\ngen-4 & 0.53 & 0.50 & 0.51 \\\\\n\\midrule\nMacro & --- & --- & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n5-class macro-F1 is 0.62 (Table~\\ref{tab:ordinal}), lower than the 3-class result due to overlapping feature distributions at deep classes.\nHowever, the ordinal structure is preserved: Spearman $\\rho = 0.83$ between predicted and true depth, with MAE = 0.58 and 72\\% of errors being off-by-one.\nThis confirms that drift is monotonic (supporting H$_2$) while establishing a practical resolution ceiling: 3-class coarse bucketing is more reliable than exact depth prediction for data curation purposes.\n\n\\subsection{Robustness to Post-Generation Editing}\n\n\\begin{table}[t]\n\\centering\n\\caption{Robustness to simulated post-generation edits.}\n\\label{tab:robust}\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nEdit Type & Rate & Macro-F1 & $\\Delta$ \\\\\n\\midrule\nNone (baseline) & 0\\% & 0.86 & --- \\\\\nRandom word replacement & 5\\% & 0.83 & $-$0.03 \\\\\nRandom word replacement & 10\\% & 0.78 & $-$0.08 \\\\\nRandom word replacement & 20\\% & 0.67 & $-$0.19 \\\\\nLLM light editing & $\\sim$8--12\\% & 0.76 & $-$0.10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:robust} characterizes degradation under post-generation editing.\nLight editing (5\\%) typical of human post-processing preserves most depth signal ($\\Delta$ = $-$0.03).\nDegradation is approximately linear ($-$0.095 F1 per 10\\% edit rate), providing a simple model for practitioners to assess reliability.\nEven at 20\\% editing, performance (F1 = 0.67) remains well above chance.\n\n\\subsection{LD-Score Feature Integration}\n\n\\begin{table}[t]\n\\centering\n\\caption{LD-Score feature integration.}\n\\label{tab:ld}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nFeature Set & Macro-F1 & $\\Delta$ from Full \\\\\n\\midrule\nFull (7 features) & 0.87 & --- \\\\\nFull + LD-Score & 0.88 & +0.01 \\\\\nLD-Score only & 0.59 & $-$0.28 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding LD-Score~\\cite{dugan2024ldscore} as an 8th feature provides marginal improvement ($\\Delta$ = +0.01; Table~\\ref{tab:ld}).\nLD-Score alone achieves only F1 = 0.59 with low permutation importance (0.06), confirming that character-level distributional signatures are largely redundant with existing surface features---both measure vocabulary impoverishment at different granularities.\nThis reinforces that reference-model entropy features, not surface-level statistics, are the novel signal source.\n\n\\subsection{End-to-End Neural Baseline}\n\\label{sec:e2e}\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature-based vs.\\ end-to-end neural comparison.}\n\\label{tab:e2e}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & In-Dist F1 & Cross-Gen F1 & Cost \\\\\n\\midrule\nXGBoost + features & \\textbf{0.86} & \\textbf{0.78} & 3 min \\\\\nQLoRA Qwen3.5-0.8B & 0.83 & 0.71 & 12 GPU$\\cdot$h \\\\\n\\midrule\n$\\Delta$ & +0.03 & +0.07 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe compare against a QLoRA-fine-tuned Qwen3.5-0.8B as an end-to-end neural baseline (Table~\\ref{tab:e2e}).\nThe handcrafted feature approach outperforms on both in-distribution (+0.03) and cross-generator (+0.07) F1, while being $\\sim$240$\\times$ cheaper to train.\nThe larger cross-generator gap reveals that the fine-tuned model memorizes generator-specific artifacts, while handcrafted features are designed to capture generator-invariant distributional drift.\n\n\\section{Discussion}\n\n\\paragraph{Theoretical implications.}\nOur results establish a clean dichotomy in recursive generation dynamics: paraphrastic chains converge (H$_1$), non-paraphrastic chains diverge (H$_2$).\nThis distinction arises from the presence or absence of a semantic-preservation constraint: paraphrasing re-anchors to a fixed semantic target at each step, while continuation explores an unbounded state space where distributional drift accumulates.\nThe prompt type analysis (Section~\\ref{sec:prompt}) reveals this is a spectrum, not a binary---elaboration lies between continuation and paraphrasing in drift rate.\n\n\\paragraph{Practical implications for data curation.}\nDistributional fingerprints enable \\emph{risk-stratified} data governance: rather than binary accept/reject decisions, practitioners can assign depth-derived risk scores and set thresholds appropriate to their quality requirements.\nOur downstream experiments show that gen-1 text is nearly as valuable as human text for training (perplexity gap of 1.8 points), while gen-2+ text introduces meaningful quality degradation.\nDepth-aware filtering achieves the best quality--quantity tradeoff: 42\\% data retention at near-human quality, vs.\\ 28\\% retention with worse quality under binary filtering.\n\n\\paragraph{Limitations.}\nThe method's primary limitation is sensitivity to post-generation editing ($-$0.095 F1 per 10\\% edit rate).\nCross-model chains reduce accuracy by 10 points compared to single-model chains.\nFiner-grained depth estimation (5-class) has limited precision for depths $\\geq$2, though ordinal structure is preserved.\nAll experiments use models $\\leq$2.8B parameters; scaling to larger generators requires further investigation.\n\n\\section{Conclusion}\n\nWe introduced distributional fingerprinting for generation depth estimation, demonstrating that non-paraphrastic LLM generation chains exhibit monotonic distributional divergence detectable via reference-model entropy features.\nOur 7-feature classifier achieves macro-F1 = 0.87 for 3-class depth estimation, generalizes across 5 generator families (leave-one-out F1 = 0.78), and enables depth-aware data curation that outperforms binary detection baselines by 5.2\\% in downstream quality while retaining 50\\% more training data.\nThe clean separation between convergent paraphrastic chains and divergent non-paraphrastic chains provides a unified framework connecting attractor cycle theory to the distributional dynamics of recursive text generation.\n\n\\bibliographystyle{aaai26}\n\n\\begin{thebibliography}{10}\n\n\\bibitem{shumailov2024model}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock {\\em Nature}, 631:755--759, 2024.\n\n\\bibitem{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and J.~Zhang.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In {\\em Proc.\\ ICLR}, 2024.\n\n\\bibitem{dathathri2024synthid}\nS.~Dathathri, A.~See, S.~Ghaisas, P.-S.~Huang, R.~McAdam, J.~Welbl, V.~Bachani, A.~Kaskasoli, R.~Stanforth, T.~Matejovicova, et~al.\n\\newblock Scalable watermarking for identifying large language model outputs.\n\\newblock {\\em Nature}, 634:818--823, 2024.\n\n\\bibitem{dugan2024ldscore}\nL.~Dugan, H.~Hwang, F.~Trhl{\\'\\i}k, A.~Ladhak, A.~Ippolito, and C.~Callison-Burch.\n\\newblock {LD}-Score: A character-level metric for distinguishing human from machine-generated text.\n\\newblock {\\em arXiv preprint arXiv:2605.01647}, 2025.\n\n\\bibitem{briesch2025attractor}\nM.~Briesch, D.~Sobania, and F.~Rothlauf.\n\\newblock Large language models are attractor cycles of iterative paraphrasing.\n\\newblock In {\\em Proc.\\ ACL}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "4fa77b44-8748-43d1-9393-1b71ee10f6de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "b746b74a-77b5-4af2-ba29-152811430497",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper on depth fingerprints",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Tool call

_source line 21 · 2026-05-14T18:32:00.870Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BZa3ukZvF8QGtggfwMJs1g`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b746b74a-77b5-4af2-ba29-152811430497",
  "isSidechain": false,
  "requestId": "req_011Cb2wRwuSmQXPY7e8deQS5",
  "type": "assistant",
  "uuid": "21d1546e-5ea5-43bb-9769-6b68c7698ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KwHYdLAUy658Gnhy8Jgtrm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10594,
      "cache_read_input_tokens": 39786,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 39786,
          "cache_creation_input_tokens": 10594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10594
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

_source line 22 · 2026-05-14T18:32:01.043Z_

<details><summary>↩ Tool result · reported error · `toolu_01BZa3ukZvF8QGtggfwMJs1g`</summary>

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
  "parentUuid": "21d1546e-5ea5-43bb-9769-6b68c7698ddb",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "f86a86dd-8336-4231-bd11-03aae4a2a499",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n\n! LaTeX Error: File `aaai26.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "21d1546e-5ea5-43bb-9769-6b68c7698ddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-14T18:32:07.398Z_

<details><summary>Logged reasoning block</summary>

```text
The AAAI style file isn't available. Let me switch to a standard article class with appropriate formatting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f86a86dd-8336-4231-bd11-03aae4a2a499",
  "isSidechain": false,
  "requestId": "req_011Cb2wSEaYXYPqiaMZxXaaN",
  "type": "assistant",
  "uuid": "8cd65a4e-2038-4a3a-8569-bccc1d231c8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSNSm2yaHwZ7UtWqkDeNdS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 50380,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 463,
          "cache_read_input_tokens": 50380,
          "cache_creation_input_tokens": 467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 467
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

_source line 24 · 2026-05-14T18:32:07.856Z_

Missing AAAI style file. I'll switch to a standard article class with comparable formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cd65a4e-2038-4a3a-8569-bccc1d231c8e",
  "isSidechain": false,
  "requestId": "req_011Cb2wSEaYXYPqiaMZxXaaN",
  "type": "assistant",
  "uuid": "880d0e15-c04f-4190-8ef3-0119e919098c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSNSm2yaHwZ7UtWqkDeNdS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 50380,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 463,
          "cache_read_input_tokens": 50380,
          "cache_creation_input_tokens": 467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 467
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

_source line 25 · 2026-05-14T18:32:13.140Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QTGY24bj3PMrSarktRa7Sn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
  "old_string": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\setlength\\titlebox{2.5in}",
  "new_string": "\\documentclass[letterpaper, 10pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{enumitem}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880d0e15-c04f-4190-8ef3-0119e919098c",
  "isSidechain": false,
  "requestId": "req_011Cb2wSEaYXYPqiaMZxXaaN",
  "type": "assistant",
  "uuid": "0e84a098-c58f-43d3-ac37-1456e3df93df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JSNSm2yaHwZ7UtWqkDeNdS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 50380,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 463,
          "cache_read_input_tokens": 50380,
          "cache_creation_input_tokens": 467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 467
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

_source line 26 · 2026-05-14T18:32:13.153Z_

<details><summary>↩ Tool result · `toolu_01QTGY24bj3PMrSarktRa7Sn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e84a098-c58f-43d3-ac37-1456e3df93df",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "95c913f0-b6ca-46d6-a939-24246e63e72e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
    "oldString": "\\documentclass[letterpaper]{article}\n\\usepackage{aaai26}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\n\\setlength\\titlebox{2.5in}",
    "newString": "\\documentclass[letterpaper, 10pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{helvet}\n\\usepackage{courier}\n\\usepackage[hyphens]{url}\n\\usepackage{graphicx}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{enumitem}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[letterpaper]{article}",
          "-\\usepackage{aaai26}",
          "+\\documentclass[letterpaper, 10pt]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{helvet}",
          " \\usepackage{courier}"
        ]
      },
      {
        "oldStart": 10,
        "oldLines": 9,
        "newStart": 10,
        "newLines": 8,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{hyperref}",
          "+\\usepackage{enumitem}",
          " ",
          "-\\setlength\\titlebox{2.5in}",
          "-",
          " \\title{Distributional Fingerprints of Generation Depth:\\\\Detecting Recursive LLM Contamination Beyond Binary Classification}",
          " ",
          " \\author{Anonymous}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0e84a098-c58f-43d3-ac37-1456e3df93df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T18:32:16.513Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Kagv3VVAvg5X5964V6pG28`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
  "old_string": "\\bibliographystyle{aaai26}",
  "new_string": "\\bibliographystyle{plain}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95c913f0-b6ca-46d6-a939-24246e63e72e",
  "isSidechain": false,
  "requestId": "req_011Cb2wT8p4TcQ1AvLqDKp9o",
  "type": "assistant",
  "uuid": "b6a6eabf-75d1-4a28-90a2-d22d9d41f654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01545vsGnn9tNEXG73QbwnXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 50847,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 154,
          "cache_read_input_tokens": 50847,
          "cache_creation_input_tokens": 549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 549
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

_source line 28 · 2026-05-14T18:32:16.524Z_

<details><summary>↩ Tool result · `toolu_01Kagv3VVAvg5X5964V6pG28`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6a6eabf-75d1-4a28-90a2-d22d9d41f654",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "2dc137c4-9f7d-4496-88a2-d5e626e93ab3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
    "oldString": "\\bibliographystyle{aaai26}",
    "newString": "\\bibliographystyle{plain}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 541,
        "oldLines": 7,
        "newStart": 541,
        "newLines": 7,
        "lines": [
          " Our 7-feature classifier achieves macro-F1 = 0.87 for 3-class depth estimation, generalizes across 5 generator families (leave-one-out F1 = 0.78), and enables depth-aware data curation that outperforms binary detection baselines by 5.2\\% in downstream quality while retaining 50\\% more training data.",
          " The clean separation between convergent paraphrastic chains and divergent non-paraphrastic chains provides a unified framework connecting attractor cycle theory to the distributional dynamics of recursive text generation.",
          " ",
          "-\\bibliographystyle{aaai26}",
          "+\\bibliographystyle{plain}",
          " ",
          " \\begin{thebibliography}{10}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b6a6eabf-75d1-4a28-90a2-d22d9d41f654",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-14T18:32:16.594Z_

```json
{
  "parentUuid": "2dc137c4-9f7d-4496-88a2-d5e626e93ab3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "29fd9231-8e63-41a0-9c76-129e17aa1a4a",
  "timestamp": "2026-05-14T18:32:16.594Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-14T18:32:19.547Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018vE1jHKQoYyCVkYgVVgdr4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29fd9231-8e63-41a0-9c76-129e17aa1a4a",
  "isSidechain": false,
  "requestId": "req_011Cb2wTNzLeCMpLDXao1ZGE",
  "type": "assistant",
  "uuid": "83c13b88-5184-4b0f-89da-6539e2e488cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tna7b3cfoDX2T1UjguYky9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 51396,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 51396,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 31 · 2026-05-14T18:32:20.166Z_

<details><summary>↩ Tool result · reported error · `toolu_018vE1jHKQoYyCVkYgVVgdr4`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/helvet.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/courier.sty)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
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

LaTeX Warning: Citation `shumailov2024model' on page 1 undefined on input line 
36.


LaTeX Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on input lin
e 40.


LaTeX Warning: Citation `dathathri2024synthid' on page 1 undefined on input lin
e 40.


LaTeX Warning: Citation `dugan2024ldscore' on page 1 undefined on input line 40
.


LaTeX Warning: Citation `briesch2025attractor' on page 1 undefined on input lin
e 46.


Overfull \hbox (0.7403pt too wide) in paragraph at lines 46--50
\OT1/ptm/m/n/10 cy-cles, bound-ing depth dis-crim-inabil-ity to roughly 3 class
es. How-ever, this re-sult de-pends on the semantic-preservation
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

LaTeX Warning: Citation `bao2024fastdetectgpt' on page 2 undefine

... [666 characters truncated] ...

 from 2,000 seed texts span-ning 4 do-mains (Wikipedia, CNN/DailyMa
il

LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 159.


LaTeX Warning: Reference `tab:importance' on page 3 undefined on input line 163
.

[3]

LaTeX Warning: Reference `tab:crossgen' on page 4 undefined on input line 210.


LaTeX Warning: Reference `tab:indist' on page 4 undefined on input line 212.


LaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 256.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


LaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 282.


LaTeX Warning: Citation `briesch2025attractor' on page 4 undefined on input lin
e 284.

[4]

LaTeX Warning: Reference `tab:ppl' on page 5 undefined on input line 318.


LaTeX Warning: Reference `tab:filter' on page 5 undefined on input line 338.

! Extra alignment tab has been changed to \cr.
&lt;template> \unskip \hfil }\endtemplate 
                                       
l.354 Prompt Type & F1 & gen-0 & gen-1 & gen-2+ &
                                                  Drift Rate \\
! Extra alignment tab has been changed to \cr.
&lt;template> \unskip \hfil }\endtemplate 
                                       
l.356 Continuation & 0.85 & 0.95 & 0.79 & 0.81 &
                                                 0.18 \\
! Extra alignment tab has been changed to \cr.
&lt;template> \unskip \hfil }\endtemplate 
                                       
l.357 Elaboration & 0.80 & 0.92 & 0.73 & 0.75 &
                                                0.14 \\
! Extra alignment tab has been changed to \cr.
&lt;template> \unskip \hfil }\endtemplate 
                                       
l.358 ...d rewriting & 0.72 & 0.86 & 0.64 & 0.67 &
                                                   0.10 \\

LaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 363.


LaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 390
.


LaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 416.

[5]

LaTeX Warning: Reference `tab:ordinal' on page 6 undefined on input line 445.


LaTeX Warning: Reference `tab:robust' on page 6 undefined on input line 469.


LaTeX Warning: Citation `dugan2024ldscore' on page 6 undefined on input line 49
2.


LaTeX Warning: Reference `tab:ld' on page 6 undefined on input line 492.

[6]

LaTeX Warning: Reference `tab:e2e' on page 7 undefined on input line 516.


LaTeX Warning: Reference `sec:prompt' on page 7 undefined on input line 525.

[7] [8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 206610 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83c13b88-5184-4b0f-89da-6539e2e488cb",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "581219d9-c259-4047-9839-e4fb054ff419",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/helvet.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/courier.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `shumailov2024model' on page 1 undefined on input line \n36.\n\n\nLaTeX Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on input lin\ne 40.\n\n\nLaTeX Warning: Citation `dathathri2024synthid' on page 1 undefined on input lin\ne 40.\n\n\nLaTeX Warning: Citation `dugan2024ldscore' on page 1 undefined on input line 40\n.\n\n\nLaTeX Warning: Citation `briesch2025attractor' on page 1 undefined on input lin\ne 46.\n\n\nOverfull \\hbox (0.7403pt too wide) in paragraph at lines 46--50\n\\OT1/ptm/m/n/10 cy-cles, bound-ing depth dis-crim-inabil-ity to roughly 3 class\nes. How-ever, this re-sult de-pends on the semantic-preservation\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nLaTeX Warning: Citation `bao2024fastdetectgpt' on page 2 undefine\n\n... [666 characters truncated] ...\n\n from 2,000 seed texts span-ning 4 do-mains (Wikipedia, CNN/DailyMa\nil\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 159.\n\n\nLaTeX Warning: Reference `tab:importance' on page 3 undefined on input line 163\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:crossgen' on page 4 undefined on input line 210.\n\n\nLaTeX Warning: Reference `tab:indist' on page 4 undefined on input line 212.\n\n\nLaTeX Warning: Reference `tab:crossref' on page 4 undefined on input line 256.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nLaTeX Warning: Reference `tab:h1h2' on page 4 undefined on input line 282.\n\n\nLaTeX Warning: Citation `briesch2025attractor' on page 4 undefined on input lin\ne 284.\n\n[4]\n\nLaTeX Warning: Reference `tab:ppl' on page 5 undefined on input line 318.\n\n\nLaTeX Warning: Reference `tab:filter' on page 5 undefined on input line 338.\n\n! Extra alignment tab has been changed to \\cr.\n&lt;template> \\unskip \\hfil }\\endtemplate \n                                       \nl.354 Prompt Type & F1 & gen-0 & gen-1 & gen-2+ &\n                                                  Drift Rate \\\\\n! Extra alignment tab has been changed to \\cr.\n&lt;template> \\unskip \\hfil }\\endtemplate \n                                       \nl.356 Continuation & 0.85 & 0.95 & 0.79 & 0.81 &\n                                                 0.18 \\\\\n! Extra alignment tab has been changed to \\cr.\n&lt;template> \\unskip \\hfil }\\endtemplate \n                                       \nl.357 Elaboration & 0.80 & 0.92 & 0.73 & 0.75 &\n                                                0.14 \\\\\n! Extra alignment tab has been changed to \\cr.\n&lt;template> \\unskip \\hfil }\\endtemplate \n                                       \nl.358 ...d rewriting & 0.72 & 0.86 & 0.64 & 0.67 &\n                                                   0.10 \\\\\n\nLaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 363.\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 390\n.\n\n\nLaTeX Warning: Reference `tab:domain' on page 5 undefined on input line 416.\n\n[5]\n\nLaTeX Warning: Reference `tab:ordinal' on page 6 undefined on input line 445.\n\n\nLaTeX Warning: Reference `tab:robust' on page 6 undefined on input line 469.\n\n\nLaTeX Warning: Citation `dugan2024ldscore' on page 6 undefined on input line 49\n2.\n\n\nLaTeX Warning: Reference `tab:ld' on page 6 undefined on input line 492.\n\n[6]\n\nLaTeX Warning: Reference `tab:e2e' on page 7 undefined on input line 516.\n\n\nLaTeX Warning: Reference `sec:prompt' on page 7 undefined on input line 525.\n\n[7] [8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 206610 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "83c13b88-5184-4b0f-89da-6539e2e488cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "581219d9-c259-4047-9839-e4fb054ff419",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper on depth fingerprints",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Assistant

_source line 34 · 2026-05-14T18:32:24.705Z_

<details><summary>Logged reasoning block</summary>

```text
There's an issue with the prompt type table - it has 6 columns but the tabular spec only has 5 (`{@{}lcccc@{}}`). Let me fix that. Also the first pass generated a PDF, but with errors. Let me fix the table and recompile.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "581219d9-c259-4047-9839-e4fb054ff419",
  "isSidechain": false,
  "requestId": "req_011Cb2wTeKq1ZEPw79HnyqHs",
  "type": "assistant",
  "uuid": "51571d2d-ce8d-49e1-ae3d-9d8eec0c8e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pnaysAAtnTLdcfzYRutwC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4164,
      "cache_read_input_tokens": 51740,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 567,
          "cache_read_input_tokens": 51740,
          "cache_creation_input_tokens": 4164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4164
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

_source line 35 · 2026-05-14T18:32:25.702Z_

PDF was generated (9 pages) but there's a column count mismatch in the prompt type table. Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51571d2d-ce8d-49e1-ae3d-9d8eec0c8e00",
  "isSidechain": false,
  "requestId": "req_011Cb2wTeKq1ZEPw79HnyqHs",
  "type": "assistant",
  "uuid": "dba29539-a988-47a0-a1bd-a6efa661a47a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pnaysAAtnTLdcfzYRutwC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4164,
      "cache_read_input_tokens": 51740,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 567,
          "cache_read_input_tokens": 51740,
          "cache_creation_input_tokens": 4164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4164
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

_source line 36 · 2026-05-14T18:32:30.446Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Wk8ZvT8pssHUJLXBvR74Q9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
  "old_string": "\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\",
  "new_string": "\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dba29539-a988-47a0-a1bd-a6efa661a47a",
  "isSidechain": false,
  "requestId": "req_011Cb2wTeKq1ZEPw79HnyqHs",
  "type": "assistant",
  "uuid": "5a298a83-c30b-45c1-8998-d975983f5b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014pnaysAAtnTLdcfzYRutwC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4164,
      "cache_read_input_tokens": 51740,
      "output_tokens": 567,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4164,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 567,
          "cache_read_input_tokens": 51740,
          "cache_creation_input_tokens": 4164,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4164
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

_source line 37 · 2026-05-14T18:32:30.456Z_

<details><summary>↩ Tool result · `toolu_01Wk8ZvT8pssHUJLXBvR74Q9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a298a83-c30b-45c1-8998-d975983f5b88",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "8c65dc90-db47-4cfe-b25b-2f6f6295494f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best/paper.tex",
    "oldString": "\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\",
    "newString": "\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nPrompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\\n\\midrule\nContinuation & 0.85 & 0.95 & 0.79 & 0.81 & 0.18 \\\\\nElaboration & 0.80 & 0.92 & 0.73 & 0.75 & 0.14 \\\\\nInspired rewriting & 0.72 & 0.86 & 0.64 & 0.67 & 0.10 \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 349,
        "oldLines": 7,
        "newStart": 349,
        "newLines": 7,
        "lines": [
          " \\caption{Depth classification by prompt type. More constrained generation produces stronger depth signal.}",
          " \\label{tab:prompt}",
          " \\small",
          "-\\begin{tabular}{@{}lcccc@{}}",
          "+\\begin{tabular}{@{}lccccc@{}}",
          " \\toprule",
          " Prompt Type & F1 & gen-0 & gen-1 & gen-2+ & Drift Rate \\\\",
          " \\midrule"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5a298a83-c30b-45c1-8998-d975983f5b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T18:32:33.744Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BtFfRFUrQjHnnkcb7XYopr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Recompile paper after fixing table column count",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c65dc90-db47-4cfe-b25b-2f6f6295494f",
  "isSidechain": false,
  "requestId": "req_011Cb2wUQSgKREHe79vdLkur",
  "type": "assistant",
  "uuid": "b1795451-e1b3-46c1-8d6f-0c7f223b8fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1n5ik9YoDanzJqYGsu22K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 653,
      "cache_read_input_tokens": 55904,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 653,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 55904,
          "cache_creation_input_tokens": 653,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 653
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

_source line 39 · 2026-05-14T18:32:34.607Z_

<details><summary>↩ Tool result · `toolu_01BtFfRFUrQjHnnkcb7XYopr`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/helvet.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/courier.sty)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
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
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (0.7403pt too wide) in paragraph at lines 46--50
\OT1/ptm/m/n/10 cy-cles, bound-ing depth dis-crim-inabil-ity to roughly 3 class
es. How-ever, this re-sult de-pends on the semantic-preservation
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [2]
Overfull \hbox (16.7007pt too wide) in paragraph at lines 120--124
 []\OT1/ptm/b/n/10 Data gen-er-a-tion.[] \OT1/ptm/m/n/10 We con-struct gen-er-a
-tion chains from 2,000 seed texts span-ning 4 do-mains (Wikipedia, CNN/DailyMa
il
[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 260.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 260.

[4] [5] [6] [7] [8] [9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 209113 bytes).
Transcript written on paper.log.

[4] [5] [6] [7] [8] [9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-
dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 209113 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1795451-e1b3-46c1-8d6f-0c7f223b8fe4",
  "isSidechain": false,
  "promptId": "58464941-2e05-4954-ae67-fc032f2bb3a6",
  "type": "user",
  "uuid": "ed5be735-8fd9-4460-9604-665d2e1a1001",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/helvet.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/courier.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (0.7403pt too wide) in paragraph at lines 46--50\n\\OT1/ptm/m/n/10 cy-cles, bound-ing depth dis-crim-inabil-ity to roughly 3 class\nes. How-ever, this re-sult de-pends on the semantic-preservation\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd) [2]\nOverfull \\hbox (16.7007pt too wide) in paragraph at lines 120--124\n []\\OT1/ptm/b/n/10 Data gen-er-a-tion.[] \\OT1/ptm/m/n/10 We con-struct gen-er-a\n-tion chains from 2,000 seed texts span-ning 4 do-mains (Wikipedia, CNN/DailyMa\nil\n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 260.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 260.\n\n[4] [5] [6] [7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 209113 bytes).\nTranscript written on paper.log.\n\n[4] [5] [6] [7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 209113 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b1795451-e1b3-46c1-8d6f-0c7f223b8fe4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-14T18:32:45.933Z_

编译成功，无错误。`paper.pdf` 已生成，9 页，209KB。

论文覆盖全部 10 个实验（feature_ablation → Table 1-2, cross_generator → Table 3-4, cross_family_reference → Table 5-6, paraphrastic_comparison → Table 10, downstream_utility → Table 7-8, prompt_type → Table 9, cross_model_chains → Table 11, multi_domain → Table 12, finer_grained_ordinal → Table 13, human_edit_robustness → Table 14, ld_score_feature → Table 15, end_to_end_classifier → Table 16），所有数字均来自 `experiment_data.json`，结构完整（Abstract / Introduction / Related Work / Method / Experiments / Discussion / Conclusion）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed5be735-8fd9-4460-9604-665d2e1a1001",
  "isSidechain": false,
  "requestId": "req_011Cb2wUi9nxnaLgN13JjC9n",
  "type": "assistant",
  "uuid": "082a702b-f724-48a7-8c91-04be0910bb5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/best",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SQ7HtKuvzgwfBwbsZCwwJ2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3956,
      "cache_read_input_tokens": 56557,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 56557,
          "cache_creation_input_tokens": 3956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3956
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T181213 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "082a702b-f724-48a7-8c91-04be0910bb5d",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper on depth fingerprints",
  "sessionId": "a5bf2556-9800-4831-b047-6e32a187b880"
}
```

---
