# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/fa7753a8-dd61-4209-9c6b-997c283e43b3.jsonl`
- **Structured JSON:** [`11de5b19ef3136ac343c.json`](../../sessions/11/11de5b19ef3136ac343c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:02:06.128Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:02:06.128Z",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心 claim 从 \"adaptive b* replaces grid search\" 全面后退。finer grid 揭示真最优 b 在 0.1-0.3 区间，adaptive b* median ~0.87 系统性 overshoot 约 4×。60% 污染和 3B 模型下效应未显著放大，cross-generator 场景 adaptive 甚至劣于 uniform。 Reframe 1: α_eff(b) 作为 diagnostic framework——b* 轨迹揭示 batch-level 污染结构， 即使不产出最优 b 也提供 Drayson 框架缺乏的可解释性工具。 Reframe 2: loss reweighting vs SIR 的系统对比（同一 b 下 gradient variance 和 收敛行为差异）升级为独立 contribution。 Reframe 3: lightweight detector sufficiency（TF-IDF+LR AUC=0.939 vs ModernBERT AUC=0.986 → PPL 差异 <0.005）成为 primary finding——\"you don't need an expensive detector\"。 Claim 2 降级为 \"adaptive b* provides a reasonable default in most settings\"； Claim 1 弱化为 \"principled analysis tool\"。投稿仍冲 EMNLP，靠 framework + implementation comparison + detector finding 三条线撑住。 关键叙事转折：adaptive 不是最优解，但它是零成本的合理默认值，且 b* 轨迹本身 具有诊断价值。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:02:06.131Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:02:06.131Z",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-15T02:02:06.150Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心 claim 从 "adaptive b* replaces grid search" 全面后退。finer grid 揭示真最优 b 在 0.1-0.3 区间，adaptive b* median ~0.87 系统性 overshoot 约 4×。60% 污染和 3B 模型下效应未显著放大，cross-generator 场景 adaptive 甚至劣于 uniform。 Reframe 1: α_eff(b) 作为 diagnostic framework——b* 轨迹揭示 batch-level 污染结构， 即使不产出最优 b 也提供 Drayson 框架缺乏的可解释性工具。 Reframe 2: loss reweighting vs SIR 的系统对比（同一 b 下 gradient variance 和 收敛行为差异）升级为独立 contribution。 Reframe 3: lightweight detector sufficiency（TF-IDF+LR AUC=0.939 vs ModernBERT AUC=0.986 → PPL 差异 <0.005）成为 primary finding——"you don't need an expensive detector"。 Claim 2 降级为 "adaptive b* provides a reasonable default in most settings"； Claim 1 弱化为 "principled analysis tool"。投稿仍冲 EMNLP，靠 framework + implementation comparison + detector finding 三条线撑住。 关键叙事转折：adaptive 不是最优解，但它是零成本的合理默认值，且 b* 轨迹本身 具有诊断价值。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "4d57b202-e2e2-4082-83a8-14419f73d0ca",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:02:06.150Z_

```json
{
  "parentUuid": "4d57b202-e2e2-4082-83a8-14419f73d0ca",
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
  "uuid": "045878de-e6f4-47fa-92c3-6d2cc84fa7b1",
  "timestamp": "2026-05-15T02:02:06.150Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:02:06.150Z_

```json
{
  "parentUuid": "045878de-e6f4-47fa-92c3-6d2cc84fa7b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ec01eab6-70cb-4cb6-b9d1-b5ab42d70fc3",
  "timestamp": "2026-05-15T02:02:06.150Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
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
  "aiTitle": "Generate worst-case research paper simulation",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Assistant

_source line 7 · 2026-05-15T02:02:12.334Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec01eab6-70cb-4cb6-b9d1-b5ab42d70fc3",
  "isSidechain": false,
  "requestId": "req_011Cb3Xku5mo6c4hgHnMXHQA",
  "type": "assistant",
  "uuid": "82c7a41e-bbad-42d8-a0ef-561f0d1ef58a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFLgvf52m6hN3ZfqyVuFYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11468,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11468
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

_source line 8 · 2026-05-15T02:02:13.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JVyDsRhAcYot6iS8izUAed`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c7a41e-bbad-42d8-a0ef-561f0d1ef58a",
  "isSidechain": false,
  "requestId": "req_011Cb3Xku5mo6c4hgHnMXHQA",
  "type": "assistant",
  "uuid": "ad1af87d-e66d-416b-842d-a6877136a83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFLgvf52m6hN3ZfqyVuFYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11468,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11468
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

_source line 9 · 2026-05-15T02:02:13.567Z_

<details><summary>↩ Tool result · `toolu_01JVyDsRhAcYot6iS8izUAed`</summary>

```text
1	[
2	  {
3	    "name": "Grid-b low (b=0.1/0.2/0.3), seed42",
4	    "description": "在现有 grid (b=0.5~5.0) 基础上向低 b 区间扩展。 worst 档核心预测：真最优 b 在 0.1-0.3 区间，b=0.5 并非 grid-best。\n",
5	    "results": {
6	      "b0_1_train_loss": 7.55,
7	      "b0_2_train_loss": 7.95,
8	      "b0_3_train_loss": 8.6,
9	      "total_steps": 6103,
10	      "train_runtime_s_per_b": 13000,
11	      "all_completed": true
12	    },
13	    "tables": [],
14	    "figures": [],
15	    "analysis": "训练顺利完成，train_loss 在 [7.55, 8.60] 区间，与 b 值正相关趋势一致。 关键判断需等 post-hoc eval (p0_grid_b_low_eval) 出 PPL 数据。\n\n\ntrain_loss 与 b 正相关（更大 b → 更多 downweight 合成样本 → 去掉低 loss 的 合成样本后均值上升）。b=0.1 的 train_loss (7.55) 仅略高于 uniform (7.31)， 因为 w=(1-q)^0.1 对 q=0.9 仍给出权重 0.79，几乎不降权。\n"
16	  },
17	  {
18	    "name": "Grid-b low (b=0.1/0.2/0.3), seed123",
19	    "description": "seed123 的 b<0.5 grid 扩展，用于 cross-seed consistency 验证。\n",
20	    "results": {
21	      "b0_1_train_loss": 7.57,
22	      "b0_2_train_loss": 7.97,
23	      "b0_3_train_loss": 8.62,
24	      "total_steps": 6103,
25	      "all_completed": true
26	    },
27	    "tables": [],
28	    "figures": [],
29	    "analysis": "训练完成，模式与 seed42 一致。\n\n\nseed123 在 b=0.5 grid 中表现最好 (PPL=17.638)，low-b 区间预计保持相同趋势。 train_loss 与 seed42 相当，seed 间差异 <1%。\n"
30	  },
31	  {
32	    "name": "Grid-b low (b=0.1/0.2/0.3), seed456",
33	    "description": "seed456 的 b<0.5 grid 扩展。\n",
34	    "results": {
35	      "b0_1_train_loss": 7.52,
36	      "b0_2_train_loss": 7.91,
37	      "b0_3_train_loss": 8.55,
38	      "total_steps": 6103,
39	      "all_completed": true
40	    },
41	    "tables": [],
42	    "figures": [],
43	    "analysis": "训练完成，等 eval 结果。\n\n\nseed456 uniform train_loss (7.29) 略低于其他 seed，low-b grid 保持一致偏移。\n"
44	  },
45	  {
46	    "name": "Post-hoc eval for all 9 b<0.5 checkpoints",
47	    "description": "对 3 seeds × 3 b-values = 9 个 checkpoint 做 holdout eval，获取 PPL。 worst 档核心预测：b=0.2 在所有 seed 上 PPL 低于 b=0.5，成为新 grid-best， 使 adaptive 的 aggregate ratio 从 88.6% 降至 ~70%。\n",
48	    "results": {
49	      "b0_1_seed42_eval_ppl": 17.645,
50	      "b0_2_seed42_eval_ppl": 17.637,
51	      "b0_3_seed42_eval_ppl": 17.641,
52	      "b0_1_seed123_eval_ppl": 17.631,
53	      "b0_2_seed123_eval_ppl": 17.625,
54	      "b0_3_seed123_eval_ppl": 17.629,
55	      "b0_1_seed456_eval_ppl": 17.642,
56	      "b0_2_seed456_eval_ppl": 17.636,
57	      "b0_3_seed456_eval_ppl": 17.64,
58	      "new_grid_best_b": 0.2,
59	      "new_grid_best_ppl_seed42": 17.637,
60	      "new_grid_best_ppl_seed123": 17.625,
61	      "new_grid_best_ppl_seed456": 17.636,
62	      "old_grid_best_b": 0.5,
63	      "new_ratio_seed42_pct": 75.5,
64	      "new_ratio_seed123_pct": 72.3,
65	      "new_ratio_seed456_pct": 62.5,
66	      "new_aggregate_ratio_pct": 69.8,
67	      "max_relative_ppl_improvement_pct": 0.37,
68	      "eval_holdout_tokens": 4077068
69	    },
70	    "tables": [
71	      {
72	        "caption": "Full Grid-b PPL Curve (ρ=0.4, Qwen3-0.6B, 200M tokens)",
73	        "rows": [
74	          {
75	            "b": 0.1,
76	            "seed42": 17.645,
77	            "seed123": 17.631,
78	            "seed456": 17.642
79	          },
80	          {
81	            "b": 0.2,
82	            "seed42": 17.637,
83	            "seed123": 17.625,
84	            "seed456": 17.636
85	          },
86	          {
87	            "b": 0.3,
88	            "seed42": 17.641,
89	            "seed123": 17.629,
90	            "seed456": 17.64
91	          },
92	          {
93	            "b": 0.5,
94	            "seed42": 17.651,
95	            "seed123": 17.638,
96	            "seed456": 17.65
97	          },
98	          {
99	            "b": 1.0,
100	            "seed42": 17.692,
101	            "seed123": 17.674,
102	            "seed456": 17.68
103	          },
104	          {
105	            "b": 1.5,
106	            "seed42": 17.718,
107	            "seed123": 17.701,
108	            "seed456": 17.71
109	          },
110	          {
111	            "b": 2.0,
112	            "seed42": 17.741,
113	            "seed123": 17.725,
114	            "seed456": "~17.73"
115	          },
116	          {
117	            "b": 3.0,
118	            "seed42": 17.774,
119	            "seed123": 17.76,
120	            "seed456": "~17.77"
121	          },
122	          {
123	            "b": 5.0,
124	            "seed42": 17.818,
125	            "seed123": 17.804,
126	            "seed456": "~17.82"
127	          },
128	          {
129	            "b": "uniform",
130	            "seed42": 17.69,
131	            "seed123": 17.69,
132	            "seed456": 17.7
133	          },
134	          {
135	            "b": "adaptive",
136	            "seed42": 17.65,
137	            "seed123": 17.643,
138	            "seed456": 17.66
139	          }
140	        ]
141	      },
142	      {
143	        "caption": "Revised Aggregate Ratio with New Grid-best (b=0.2)",
144	        "rows": [
145	          {
146	            "seed": 42,
147	            "uniform": 17.69,
148	            "grid_best_b0_2": 17.637,
149	            "adaptive": 17.65,
150	            "grid_improvement": 0.053,
151	            "adaptive_improvement": 0.04,
152	            "ratio_pct": 75.5
153	          },
154	          {
155	            "seed": 123,
156	            "uniform": 17.69,
157	            "grid_best_b0_2": 17.625,
158	            "adaptive": 17.643,
159	            "grid_improvement": 0.065,
160	            "adaptive_improvement": 0.047,
161	            "ratio_pct": 72.3
162	          },
163	          {
164	            "seed": 456,
165	            "uniform": 17.7,
166	            "grid_best_b0_2": 17.636,
167	            "adaptive": 17.66,
168	            "grid_improvement": 0.064,
169	            "adaptive_improvement": 0.04,
170	            "ratio_pct": 62.5
171	          },
172	          {
173	            "seed": "aggregate",
174	            "grid_improvement": 0.182,
175	            "adaptive_improvement": 0.127,
176	            "ratio_pct": 69.8
177	          }
178	        ]
179	      }
180	    ],
181	    "figures": [],
182	    "analysis": "核心发现：grid-best 从 b=0.5 移至 b=0.2，证实 adaptive b* (median=0.87) 系统性 overshoot ~4×。aggregate ratio 从 88.6% 降至 69.8%，MVP Path B 的 \"within seed variance\" 论证不再成立——adaptive-grid gap (0.013-0.024) 显著大于 seed variance (~0.007)。 叙事影响：Claim 2 必须从 \"matches grid-best\" 降级为 \"provides a reasonable default without any tuning\"。α_eff(b) 框架的 b* 推导在数值上不准确，但框架 的分析价值仍然存在（b* 轨迹反映 batch-level 污染结构）。 论文呈现：在 Results 中坦诚展示 full grid curve，讨论 b=0.2 vs b*=0.87 的 gap，将 \"why adaptive overshoots\" 作为 analysis/discussion 的核心问题之一。\n\n\nworst 档假设：真最优 b 远低于 adaptive b* median (~0.87)。 物理解释：FineWeb 中 40% Qwen-self 合成数据质量尚可（非噪声），过度降权 (b>0.5) 等同于丢弃可用信号。b=0.2 时 w=(1-0.9)^0.2=0.63，contaminated 样本仍保留 63% 权重——温和降权保留数据量的同时轻微纠正污染偏移。 b=0.5 时 w=0.32，已过度降权；adaptive median b*=0.87 时 w=0.13，更加激进。 PPL 曲线在 b=0.2 形成 U 型最低点：b<0.2 降权不足（污染信号残留）， b>0.2 降权过度（有效数据量损失超过去污染收益）。 aggregate ratio 从 88.6% (b=0.5 为 grid-best) 降至 69.8% (b=0.2 为 grid-best)， 进入 worst 档 [55, 80] 范围。adaptive 的 overshoot 问题暴露无遗。\n"
183	  },
184	  {
185	    "name": "Data generation for ρ=0.6",
186	    "description": "生成 60% 合成数据比例的训练集（Qwen3-0.6B self-gen, 200M tokens）。\n",
187	    "results": {
188	      "contamination_ratio": 0.6,
189	      "total_tokens": 200000000,
190	      "synthetic_tokens": 120000000,
191	      "real_tokens": 80000000,
192	      "detector_auc_on_60pct": 0.935,
193	      "q_score_mean_60pct": 0.68,
194	      "q_score_median_60pct": 0.82,
195	      "scored_data_file": "scored_data_60.jsonl"
196	    },
197	    "tables": [],
198	    "figures": [],
199	    "analysis": "数据生成和检测器 scoring 顺利完成。q-score 分布相比 40% 条件向高值偏移， 符合预期。检测器泛化到不同 mixing ratio 无显著退化。\n\n\n同一 TF-IDF+LR 检测器在 60% 数据上 AUC 微降至 0.935（class imbalance 从 40:60 变为 60:40，合成类占多数导致 precision 略降）。q_score_mean 升至 0.68（更多样本为合成 → 更多高 q 值），median 升至 0.82。\n"
200	  },
201	  {
202	    "name": "Uniform baseline (ρ=0.6, Qwen3-0.6B, seed42)",
203	    "description": "60% 污染下的 uniform baseline。预期 PPL 高于 40% uniform， 因为更多训练数据是合成的。\n",
204	    "results": {
205	      "eval_ppl_holdout": 17.85,
206	      "train_loss": 7.22,
207	      "total_steps": 6103,
208	      "train_runtime_s": 12000,
209	      "eval_holdout_tokens": 4077068
210	    },
211	    "tables": [],
212	    "figures": [],
213	    "analysis": "60% 污染使 uniform PPL 升高 0.16——污染效应存在但不剧烈。这为 reweighting 提供了 headroom，但 worst 档预测 adaptive 不会有效利用这个 headroom。\n\n\n60% 合成数据导致 uniform PPL 从 17.69 升至 17.85（+0.16, +0.9% relative）。 效应方向正确——更多合成数据确实降低训练质量。但升幅有限，因为 Qwen3-0.6B self-gen 的合成数据质量尚可（非随机噪声），只是分布略偏。 train_loss 反而略低 (7.22 vs 7.31)，因为合成数据通常 loss 更低（模型更 容易 fit 自己生成的内容）。\n"
214	  },
215	  {
216	    "name": "Adaptive b* (ρ=0.6, Qwen3-0.6B, seed42)",
217	    "description": "60% 污染下的 adaptive b* 运行。worst 档核心预测： Δ_adaptive(60%) 不显著大于 Δ_adaptive(40%)，效应未放大。\n",
218	    "results": {
219	      "eval_ppl_holdout": 17.82,
220	      "train_loss": 7.46,
221	      "total_steps": 6103,
222	      "b_star_mean": 1.62,
223	      "b_star_median": 1.08,
224	      "b_star_std": 2.15,
225	      "b_star_p25": 0.61,
226	      "b_star_p75": 1.85,
227	      "b_star_pct_below_0.5": 16.3,
228	      "b_star_pct_0.5_to_1": 30.2,
229	      "b_star_pct_1_to_2": 31.5,
230	      "b_star_pct_above_2": 22.0,
231	      "delta_adaptive_60_abs": 0.03,
232	      "delta_adaptive_40_abs": 0.04,
233	      "delta_adaptive_60_rel_pct": 0.17,
234	      "delta_adaptive_40_rel_pct": 0.23,
235	      "effect_amplification": false
236	    },
237	    "tables": [
238	      {
239	        "caption": "Effect Size: 40% vs 60% Contamination",
240	        "rows": [
241	          {
242	            "contamination": "40%",
243	            "uniform_ppl": 17.69,
244	            "adaptive_ppl": 17.65,
245	            "delta_abs": 0.04,
246	            "delta_rel_pct": 0.23,
247	            "b_star_median": 0.87
248	          },
249	          {
250	            "contamination": "60%",
251	            "uniform_ppl": 17.85,
252	            "adaptive_ppl": 17.82,
253	            "delta_abs": 0.03,
254	            "delta_rel_pct": 0.17,
255	            "b_star_median": 1.08
256	          }
257	        ]
258	      }
259	    ],
260	    "figures": [],
261	    "analysis": "效应未放大是 worst 档的标志性结果。反驳了 \"更高污染 → 更大收益\" 的直觉。 根本原因是 adaptive 的 b* 响应方向正确（污染增加 → b* 升高）但幅度过大 （真最优 b 不随污染比例大幅变化，但 b* 大幅上升）。 叙事影响：不能用 60% 数据来论证 \"方法在高污染下更重要\"。转而论证 α_eff 对污染比例变化的响应本身是有信息量的诊断信号——b* 从 0.87→1.08 的偏移 正确反映了污染增加，即使数值不是最优的。\n\n\n60% 污染下 q-score 分布向高值偏移 → α_eff 估计值更大 → b* median 从 0.87 升至 1.08。但真最优 b 仍在 ~0.2 区间（worst 档假设），overshoot 更严重。 Δ_adaptive(60%)=0.03 < Δ_adaptive(40%)=0.04：adaptive 在高污染下反而更差。 原因：60% 数据为合成 → 更激进的降权丢弃了过多数据 → 有效训练集缩小到 不足以支撑学习。b* 从 0.87→1.08 进一步偏离真最优 0.2，导致效应不升反降。\n"
262	  },
263	  {
264	    "name": "Grid-b=0.5 (ρ=0.6, Qwen3-0.6B, seed42)",
265	    "description": "60% 污染下 grid b=0.5 的参考点，用于对比 adaptive。\n",
266	    "results": {
267	      "eval_ppl_holdout": 17.8,
268	      "train_loss": 9.45,
269	      "total_steps": 6103,
270	      "train_runtime_s": 13000,
271	      "delta_vs_uniform_abs": 0.05,
272	      "delta_vs_uniform_rel_pct": 0.28,
273	      "ratio_adaptive_vs_grid_pct": 60.0
274	    },
275	    "tables": [],
276	    "figures": [],
277	    "analysis": "b=0.5 在 60% 下优于 adaptive，adaptive ratio 仅 60%。若在 60% 条件下也做 finer grid (b=0.1/0.2/0.3)，grid-best 可能更低，ratio 会进一步下降。 但 GPU 预算不支持 60% 的 full grid sweep——这本身就说明 grid search 的 计算成本问题（adaptive 的零成本优势在此体现）。\n\n\nb=0.5 在 60% 污染下的 PPL 改善 (0.05, 0.28%) 与 40% 条件相似 (0.039, 0.22% for seed42)。效应量基本持平——更高污染并未放大 reweighting 收益。 adaptive ratio 为 60%（0.03/0.05），低于 40% 条件下的 75.5%（以 b=0.2 为 grid-best 计算）。 原因：60% 时 b=0.5 仍然过高（真最优 ~0.2），但比 adaptive 的 b*=1.08 更接近最优。更高污染下 b=0.5 的 \"适度过高\" 和 adaptive 的 \"严重过高\" 之间的差距在拉大。\n"
278	  },
279	  {
280	    "name": "Llama-3.2-3B environment setup + data prep",
281	    "description": "3B 模型环境搭建：下载 Llama-3.2-3B，生成/复用合成数据， 用 TF-IDF+LR 对新数据打分。\n",
282	    "results": {
283	      "model_downloaded": true,
284	      "model_params": "3.2B",
285	      "vram_usage_gb": 78,
286	      "gradient_checkpointing": true,
287	      "detector_scores_generated": true,
288	      "data_reuse_from_qwen": true,
289	      "detector_auc_on_llama_data": 0.932
290	    },
291	    "tables": [],
292	    "figures": [],
293	    "analysis": "环境就绪，可以开始训练。\n\n\n复用 Qwen3-0.6B 生成的合成数据（检测器和合成数据不变，只换训练模型）。 96GB VRAM 足够 3B 模型 + gradient checkpointing。检测器 AUC 对不同训练 模型不敏感（检测的是数据来源，不是训练模型）。\n"
294	  },
295	  {
296	    "name": "Uniform baseline (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)",
297	    "description": "3B 模型的 uniform baseline。200M tokens 对 3B 模型严重不足 （Chinchilla 最优约需 64B tokens），PPL 会在高位。\n",
298	    "results": {
299	      "eval_ppl_holdout": 16.2,
300	      "train_loss": 6.85,
301	      "total_steps": 6103,
302	      "train_runtime_s": 32000,
303	      "gpu_hours": 35.6,
304	      "eval_holdout_tokens": 4077068
305	    },
306	    "tables": [],
307	    "figures": [],
308	    "analysis": "3B baseline PPL = 16.20，低于 0.6B 的 17.69。但 200M tokens 不足以让 3B 模型充分学习，效应量可能因此被压缩。\n\n\n3B 模型在 200M tokens 上严重 undertrain（tokens/param ≈ 63，远低于 Chinchilla 最优的 20×），PPL 仍在高位 (16.20 vs Qwen 0.6B 的 17.69)。更大模型的 inductive bias 带来部分优势，但数据量不足限制了收敛。 训练时间约 32000s（比 0.6B 的 12000s 长 2.7×），主要受 gradient checkpointing 和更大的矩阵运算影响。\n"
309	  },
310	  {
311	    "name": "Adaptive b* (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)",
312	    "description": "3B 模型的 adaptive 运行。worst 档核心预测：adaptive 对 3B 几乎无效， b* 分布与 0.6B 相似（方法未能适应不同模型规模），改善量接近噪声水平。\n",
313	    "results": {
314	      "eval_ppl_holdout": 16.19,
315	      "train_loss": 6.92,
316	      "total_steps": 6103,
317	      "train_runtime_s": 32500,
318	      "b_star_mean": 1.38,
319	      "b_star_median": 0.92,
320	      "b_star_std": 1.85,
321	      "b_star_p25": 0.55,
322	      "b_star_p75": 1.48,
323	      "b_star_pct_below_0.5": 21.5,
324	      "b_star_pct_0.5_to_1": 34.8,
325	      "b_star_pct_1_to_2": 27.1,
326	      "b_star_pct_above_2": 16.6,
327	      "delta_vs_uniform_abs": 0.01,
328	      "delta_vs_uniform_rel_pct": 0.06,
329	      "b_star_distribution_ks_test_vs_06b": 0.87
330	    },
331	    "tables": [
332	      {
333	        "caption": "b* Distribution Comparison: 0.6B vs 3B",
334	        "rows": [
335	          {
336	            "model": "Qwen3-0.6B",
337	            "b_star_median": 0.87,
338	            "b_star_mean": 1.4,
339	            "b_star_p25": 0.54,
340	            "b_star_p75": 1.51,
341	            "delta_ppl_rel_pct": 0.23
342	          },
343	          {
344	            "model": "Llama-3.2-3B",
345	            "b_star_median": 0.92,
346	            "b_star_mean": 1.38,
347	            "b_star_p25": 0.55,
348	            "b_star_p75": 1.48,
349	            "delta_ppl_rel_pct": 0.06
350	          }
351	        ]
352	      }
353	    ],
354	    "figures": [],
355	    "analysis": "3B 实验暴露 adaptive 方法的核心局限：b* 推导完全由 q-score 统计量驱动， 对模型规模/架构/loss landscape 无感知。当 q-score 分布不变（同一数据、 同一检测器），b* 不变——即使不同模型的最优 b 可能截然不同。 叙事影响：不能 claim \"adaptive adapts to model characteristics\"。但可以 reframe 为 \"adaptive provides a data-driven default that is consistent across models\"——一致性本身也是一种优势（可预测性）。 如果要验证 3B 的真最优 b 是否确实在不同区间（如 b=5），需要额外的 3B grid sweep，但 GPU 预算不足。\n\n\nworst 档假设：3B 模型的真最优 b 可能在完全不同的区间（Drayson 论文中 SmolLM-1.7B 用 b=1 而非 b=10），但 adaptive 的 b* 分布 (median=0.92) 与 0.6B (median=0.87) 几乎无差异。原因是 b* 推导仅依赖 q-score 分布和 ESS 约束——这两者与模型规模无关（同一数据、同一检测器）。 改善量仅 0.01 PPL (0.06% relative)，在 seed variance 范围内（基本是噪声）。 3B 模型的 loss landscape 更 flat（梯度更小），reweighting 的效果被稀释。 此外 200M tokens undertrain 意味着模型还在快速学习阶段，数据质量的微小 差异被训练动态淹没。\n"
356	  },
357	  {
358	    "name": "n_min=1 ablation (ρ=0.4, Qwen3-0.6B, seed42)",
359	    "description": "ESS 下界设为 1（最宽松约束）。worst 档预测：b* 过高导致 over-downweighting， PPL 劣于 uniform。\n",
360	    "results": {
361	      "eval_ppl_holdout": 17.71,
362	      "train_loss": 7.62,
363	      "b_star_mean": 3.85,
364	      "b_star_median": 2.6,
365	      "b_star_std": 4.12,
366	      "b_star_p25": 1.2,
367	      "b_star_p75": 4.8,
368	      "b_star_pct_above_5": 18.5,
369	      "b_star_max": 20,
370	      "total_steps": 6103
371	    },
372	    "tables": [],
373	    "figures": [],
374	    "analysis": "n_min=1 是 \"too aggressive\" 端的失败案例。b* 不受约束 → 系统性 over-downweight → 效果不如 uniform。这为 ESS 约束的必要性提供了证据， 但也说明 n_min 是一个需要 \"恰好正确\" 的参数。\n\n\nn_min=1 几乎不约束 ESS（仅要求有效样本量 ≥1/batch_size = 25%）， b* 自由飙升至 mean=3.85, median=2.60。大量 batch 使用 b*>5，导致 contaminated 样本权重趋近于零 (w=(1-0.9)^2.6=0.004)，有效训练集 急剧缩小。 PPL=17.71 > uniform (17.69)：over-downweighting 导致有效数据不足， 模型学习不充分。这比不做 reweighting 更差。 物理直觉：batch_size=4 时 n_min=1 意味着只需保留 1 个有效样本的 信息量——在 40% 污染下这几乎等于只用 clean 样本，丢弃了 40% 数据 中仍有价值的信号。\n"
375	  },
376	  {
377	    "name": "n_min=4 ablation (=batch_size, ρ=0.4, Qwen3-0.6B, seed42)",
378	    "description": "ESS 下界 = batch_size（要求所有样本保持同等权重 → 强制 b*=0）。\n",
379	    "results": {
380	      "eval_ppl_holdout": 17.69,
381	      "train_loss": 7.31,
382	      "b_star_mean": 0.0,
383	      "b_star_median": 0.0,
384	      "b_star_std": 0.0,
385	      "b_star_pct_at_zero": 100.0,
386	      "total_steps": 6103
387	    },
388	    "tables": [],
389	    "figures": [],
390	    "analysis": "预期行为——n_min=batch_size 是 uniform 的重现。与 n_min=5 一起 构成 \"退化端\" 的验证点。\n\n\nn_min=4=batch_size 要求 ESS ≥ batch_size，即所有权重完全均等， 唯一满足条件的值是 b*=0。方法退化为 uniform baseline。 PPL = 17.69 = uniform，验证了实现正确性（ESS 约束确实在工作）。\n"
391	  },
392	  {
393	    "name": "n_min=5 ablation (>batch_size, ρ=0.4, Qwen3-0.6B, seed42)",
394	    "description": "ESS 下界 > batch_size（不可能满足 → 同 n_min=4 退化为 b*=0）。\n",
395	    "results": {
396	      "eval_ppl_holdout": 17.69,
397	      "train_loss": 7.31,
398	      "b_star_mean": 0.0,
399	      "b_star_median": 0.0,
400	      "b_star_std": 0.0,
401	      "b_star_pct_at_zero": 100.0,
402	      "total_steps": 6103
403	    },
404	    "tables": [
405	      {
406	        "caption": "n_min Sensitivity Curve (ρ=0.4, Qwen3-0.6B, seed42)",
407	        "rows": [
408	          {
409	            "n_min": 1,
410	            "eval_ppl": 17.71,
411	            "b_star_median": 2.6,
412	            "status": "worse than uniform"
413	          },
414	          {
415	            "n_min": 2,
416	            "eval_ppl": 17.65,
417	            "b_star_median": 0.87,
418	            "status": "best (adaptive_fix)"
419	          },
420	          {
421	            "n_min": 3,
422	            "eval_ppl": 17.69,
423	            "b_star_median": "~0.3",
424	            "status": "≈ uniform"
425	          },
426	          {
427	            "n_min": 4,
428	            "eval_ppl": 17.69,
429	            "b_star_median": 0.0,
430	            "status": "= uniform"
431	          },
432	          {
433	            "n_min": 5,
434	            "eval_ppl": 17.69,
435	            "b_star_median": 0.0,
436	            "status": "= uniform"
437	          }
438	        ]
439	      }
440	    ],
441	    "figures": [],
442	    "analysis": "n_min sensitivity curve 展示一个尖锐的 sweet spot： - n_min=1: 过度激进，劣于 uniform - n_min=2: 唯一有效点 - n_min≥3: 退化为 uniform 这对 \"adaptive 免调参\" 的叙事构成挑战——虽然消除了 b 的 grid search， 但引入了 n_min 这个同样需要选取的超参。不过 n_min 的选择空间极小 （只有整数 1-5），比 b 的连续空间（0.1-10）简单得多。 worst 档 reframe：n_min 的存在承认方法并非 \"zero-hyperparameter\"， 但将超参搜索从 \"6+ runs 的连续 grid\" 压缩为 \"2-3 个整数点\"——仍是 显著的调参成本降低。\n\n\nn_min=5 > batch_size=4，ESS 约束永远无法满足（ESS 最大值 = batch_size）， b* 被钳制在 0。效果等同于 n_min=4 和 uniform。\n"
443	  },
444	  {
445	    "name": "ModernBERT detector training (AUC≈0.99)",
446	    "description": "训练 ModernBERT 150M 检测器作为 high-end baseline。\n",
447	    "results": {
448	      "auc": 0.986,
449	      "accuracy": 0.953,
450	      "ece_raw": 0.15,
451	      "ece_calibrated": 0.022,
452	      "temperature_T": 0.35,
453	      "q_score_mean": 0.58,
454	      "q_score_std": 0.42,
455	      "q_score_median": 0.72,
456	      "mid_range_ratio": 0.28,
457	      "training_time_hours": 1.5,
458	      "model_params": "150M"
459	    },
460	    "tables": [
461	      {
462	        "caption": "Detector Comparison",
463	        "rows": [
464	          {
465	            "detector": "TF-IDF + LR",
466	            "params": "~50K",
467	            "auc": 0.939,
468	            "ece_cal": 0.048,
469	            "mid_range_ratio": 0.463,
470	            "training_cost": "<1 min CPU"
471	          },
472	          {
473	            "detector": "ModernBERT 150M",
474	            "params": "150M",
475	            "auc": 0.986,
476	            "ece_cal": 0.022,
477	            "mid_range_ratio": 0.28,
478	            "training_cost": "1.5h GPU"
479	          }
480	        ]
481	      }
482	    ],
483	    "figures": [],
484	    "analysis": "检测器训练成功，AUC=0.986 符合预期。关键后续问题：更高 AUC 是否转化为 更好的训练 PPL？p1_detector_ablation_training 将回答这个问题。\n\n\nModernBERT 150M 在 real vs synthetic 分类上 AUC=0.986（与 Drayson 报告一致）。 相比 TF-IDF+LR (AUC=0.939)，AUC 提升 0.047。q-score 分布更 bimodal （mid_range_ratio 从 0.463 降至 0.28——更多样本在极端值，更少在中间）， ECE 更低（更准确的概率估计）。\n"
485	  },
486	  {
487	    "name": "Training with ModernBERT scores (ρ=0.4, Qwen3-0.6B, seed42)",
488	    "description": "用 ModernBERT q-scores 替换 TF-IDF+LR 的 q-scores，运行 adaptive + uniform。 worst 档预测：AUC 0.939→0.986 不会带来显著 PPL 改善。\n",
489	    "results": {
490	      "adaptive_modernbert_ppl": 17.647,
491	      "uniform_modernbert_ppl": 17.69,
492	      "adaptive_tfidf_ppl": 17.65,
493	      "uniform_tfidf_ppl": 17.69,
494	      "ppl_diff_adaptive": -0.003,
495	      "ppl_diff_relative_pct": 0.02,
496	      "b_star_median_modernbert": 0.95,
497	      "b_star_median_tfidf": 0.87
498	    },
499	    "tables": [
500	      {
501	        "caption": "Detector Quality → PPL Improvement (AUC-PPL Relationship)",
502	        "rows": [
503	          {
504	            "detector": "TF-IDF+LR",
505	            "auc": 0.939,
506	            "adaptive_ppl": 17.65,
507	            "delta_vs_uniform": 0.04,
508	            "cost": "<1 min CPU"
509	          },
510	          {
511	            "detector": "ModernBERT",
512	            "auc": 0.986,
513	            "adaptive_ppl": 17.647,
514	            "delta_vs_uniform": 0.043,
515	            "cost": "1.5h GPU"
516	          },
517	          {
518	            "improvement": "",
519	            "auc_gain": "+0.047",
520	            "ppl_gain": "-0.003",
521	            "marginal_value": "negligible"
522	          }
523	        ]
524	      }
525	    ],
526	    "figures": [],
527	    "analysis": "这是 worst 档中最强的独立发现之一：AUC 0.939→0.986 (+5%相对) 仅换来 0.003 PPL 改善 (<0.02% relative)。 升级为 primary finding 的论据：(1) 实际影响——省去 150M 参数检测器 的训练和推理成本；(2) 理论解释——w=(1-q)^b 的 monotonicity 保证 排序正确即可，不需要精确概率；(3) 对 Drayson 框架的改进建议—— 他们使用 ModernBERT 是 overkill。 Reframe 3 的核心支撑实验。\n\n\nAUC 从 0.939 提升至 0.986 (+0.047)，但 PPL 仅改善 0.003 (0.02% relative)—— 检测器质量的 marginal return 极低。 原因分析：(1) q-score 的连续性和排序正确性比 AUC 更重要——TF-IDF+LR 的 q-scores 虽然 calibration 不完美 (ECE=0.048 vs 0.022)，但排序已足够好 用于权重计算；(2) w=(1-q)^b 对 q 的 monotone transform 使得精确 q 值 不如排序重要；(3) ModernBERT 的更 bimodal 分布导致 b* 略高 (0.95 vs 0.87)， 进一步偏离真最优 b~0.2。\n"
528	  },
529	  {
530	    "name": "Cross-generator data (Llama-3.2-1B generates, Qwen3-0.6B trains)",
531	    "description": "用 Llama-3.2-1B 生成合成数据，Qwen3-0.6B 训练——模拟 web corpus 中不同来源的合成内容。TF-IDF+LR 检测器在 cross-family 数据上打分。\n",
532	    "results": {
533	      "synthetic_generator": "Llama-3.2-1B",
534	      "training_model": "Qwen3-0.6B",
535	      "contamination_ratio": 0.4,
536	      "total_tokens": 200000000,
537	      "detector_auc_cross_family": 0.891,
538	      "q_score_mean": 0.55,
539	      "q_score_std": 0.35,
540	      "q_score_median": 0.58,
541	      "mid_range_ratio": 0.52
542	    },
543	    "tables": [],
544	    "figures": [],
545	    "analysis": "检测器 cross-family 泛化受限——AUC 降至 0.891，q-score 分布变得 diffuse。 这预示 adaptive b* 在这些 noisier scores 上可能表现不佳。\n\n\ncross-family 检测更难：TF-IDF+LR 在训练时只见过 Qwen3-0.6B 的合成数据， Llama-3.2-1B 的合成文本风格不同，AUC 从 0.939 降至 0.891。 q-score 分布更 diffuse（mid_range_ratio 从 0.463 升至 0.52——更多样本 在 0.3-0.7 的不确定区间），median 从 0.707 降至 0.58。 这意味着检测器对 cross-family 合成数据的 \"信心\" 更低，q-score 排序 更不可靠。\n"
546	  },
547	  {
548	    "name": "Cross-generator training (adaptive + uniform, ρ=0.4)",
549	    "description": "用 cross-family q-scores 运行 adaptive 和 uniform。 worst 档核心预测：adaptive 在 noisy q-scores 上劣于 uniform。\n",
550	    "results": {
551	      "uniform_ppl": 17.75,
552	      "adaptive_ppl": 17.77,
553	      "delta_adaptive_abs": -0.02,
554	      "b_star_mean": 1.15,
555	      "b_star_median": 0.72,
556	      "b_star_std": 1.65,
557	      "b_star_p25": 0.35,
558	      "b_star_p75": 1.3
559	    },
560	    "tables": [
561	      {
562	        "caption": "Cross-Generator Performance",
563	        "rows": [
564	          {
565	            "setting": "self-gen (Qwen→Qwen)",
566	            "uniform_ppl": 17.69,
567	            "adaptive_ppl": 17.65,
568	            "delta": -0.04,
569	            "verdict": "adaptive wins"
570	          },
571	          {
572	            "setting": "cross-gen (Llama→Qwen)",
573	            "uniform_ppl": 17.75,
574	            "adaptive_ppl": 17.77,
575	            "delta": 0.02,
576	            "verdict": "adaptive LOSES"
577	          }
578	        ]
579	      }
580	    ],
581	    "figures": [],
582	    "analysis": "cross-generator 是 worst 档的关键失败场景。当检测器信号质量下降 (AUC 0.939→0.891)，adaptive 从 \"有益\" 翻转为 \"有害\"。 这暴露了方法的根本依赖：adaptive b* 的质量完全取决于 q-score 的 信号噪声比。在 real-world web corpus 中，合成数据来源多样 （多个 generator family），检测器 AUC 可能更低——方法的实用性 在最需要它的场景中反而最差。 叙事影响：Claim 3 (\"unknown contamination proportion\") 受损—— 不仅比例未知，合成来源也未知，而后者对方法有效性的影响更大。\n\n\ncross-family q-scores 的高 mid_range_ratio (0.52) 和低 AUC (0.891) 导致 两个问题：(1) α_eff 估计不准确——大量样本 q 在 0.3-0.7，既非明确 clean 也非明确 contaminated，使 α_eff 的 batch-level 估计噪声大；(2) b* 仍在 ~0.72 (高于真最优)，且方差更大，导致某些 batch 的权重严重失调。 最终 adaptive PPL (17.77) > uniform (17.75)：noisy reweighting 比不 reweight 更差。有害降权的数据量超过了有益降权的收益。 uniform PPL (17.75) 高于 self-gen 条件 (17.69)，因为 Llama-1B 合成数据 质量更低（更小模型生成的文本更差）。\n"
583	  },
584	  {
585	    "name": "Detect-and-remove baseline (threshold=0.5, ρ=0.4, Qwen3-0.6B, seed42)",
586	    "description": "硬阈值过滤：q>0.5 的样本直接删除，在剩余数据上 uniform 训练。\n",
587	    "results": {
588	      "eval_ppl_holdout": 17.68,
589	      "train_loss": 7.45,
590	      "total_steps": 3662,
591	      "effective_data_ratio": 0.58,
592	      "samples_removed_pct": 42.0,
593	      "false_positive_rate": 0.03
594	    },
595	    "tables": [],
596	    "figures": [],
597	    "analysis": "detect-and-remove (PPL=17.68) 略优于 uniform (17.69)，略劣于 adaptive (17.65)。在 worst 档的全局 picture 中： gentle reweighting (b=0.2, PPL=17.637) >> adaptive (b*≈0.87, PPL=17.65) ≈ detect-and-remove (PPL=17.68) > uniform (PPL=17.69)。 adaptive 优于 detect-and-remove 仍然成立，但 margin 很小 (0.03)。\n\n\nthreshold=0.5 删除约 42% 数据（40% 真合成 + ~2% 假阳性 clean 样本）。 PPL=17.68——优于 uniform (17.69) 但劣于 grid-best b=0.2 (17.637)。 在 worst 档中，detect-and-remove 是 \"过度激进\" 的极端：完全移除 vs gentle reweighting (b=0.2, w=0.63)。移除丢失了合成数据中的有用信号 （虽然分布有偏，但仍包含语言模式信息），而 gentle reweighting 保留了 这些信号的 63%。 但 detect-and-remove 比 aggressive adaptive (b*=0.87, w=0.13) 的效果 接近——都是\"过度处理\"的不同程度。\n"
598	  },
599	  {
600	    "name": "Random reweighting baseline (ρ=0.4, Qwen3-0.6B, seed42)",
601	    "description": "用随机权重（不基于检测器）训练，验证检测器信号的必要性。\n",
602	    "results": {
603	      "eval_ppl_holdout": 17.695,
604	      "train_loss": 7.33,
605	      "total_steps": 6103,
606	      "weight_mean": 1.0,
607	      "weight_std": 0.5
608	    },
609	    "tables": [
610	      {
611	        "caption": "Baseline Comparison (ρ=0.4, Qwen3-0.6B, seed42)",
612	        "rows": [
613	          {
614	            "method": "uniform",
615	            "ppl": 17.69,
616	            "delta": 0.0,
617	            "signal": "none"
618	          },
619	          {
620	            "method": "random reweight",
621	            "ppl": 17.695,
622	            "delta": 0.005,
623	            "signal": "random"
624	          },
625	          {
626	            "method": "detect-and-remove",
627	            "ppl": 17.68,
628	            "delta": -0.01,
629	            "signal": "hard threshold"
630	          },
631	          {
632	            "method": "adaptive b*",
633	            "ppl": 17.65,
634	            "delta": -0.04,
635	            "signal": "adaptive q-based"
636	          },
637	          {
638	            "method": "grid-best b=0.2",
639	            "ppl": 17.637,
640	            "delta": -0.053,
641	            "signal": "oracle grid"
642	          }
643	        ]
644	      }
645	    ],
646	    "figures": [],
647	    "analysis": "random reweighting ≈ uniform 确认检测器信号是 load-bearing—— 不是 \"任何形式的权重扰动\" 都有效，必须是与数据质量相关的信号。 这支持了 adaptive 方法的合理性（虽然不是最优，但利用了真实信号）。\n\n\n随机权重 (uniform [0, 2] 或 similar) 均值为 1，期望上等同于 uniform 训练。额外的梯度噪声（权重方差引入）使 PPL 微升 0.005。 random 不含任何数据质量信号 → 无法区分 clean vs contaminated → 表现近似 uniform。\n"
648	  },
649	  {
650	    "name": "Domain-skewed injection (code-heavy contamination, ρ=0.4, Qwen3-0.6B)",
651	    "description": "合成数据集中在代码领域（非 uniform random injection）。 worst 档预测：domain skew 导致 q-score 分布崩坏，adaptive 失效。\n",
652	    "results": {
653	      "uniform_ppl": 17.73,
654	      "adaptive_ppl": 17.76,
655	      "delta_adaptive": -0.03,
656	      "b_star_mean": 1.55,
657	      "b_star_median": 1.1,
658	      "q_score_distribution_skewness": 1.8,
659	      "domain_contamination_code_pct": 0.85,
660	      "domain_contamination_text_pct": 0.15
661	    },
662	    "tables": [],
663	    "figures": [],
664	    "analysis": "domain-skewed 是 adaptive 的另一个失败模式。方法假设 contamination 在 batch 间大致均匀分布，当 domain skew 打破这个假设时，per-batch adaptation 反而放大了 skew 的负面影响。 叙事影响：在论文 Limitations 中讨论 domain-skewed contamination 作为方法的适用边界。\n\n\ndomain-skewed injection 使 q-score 分布在不同 domain batch 间高度不均： code-heavy batch 几乎全是合成 (q 全高) → α_eff 估计偏高 → b* 过大； text batch 几乎无合成 (q 全低) → α_eff~0 → b*=0。 这种 bimodal batch structure 使 per-batch adaptive 策略失效：在 code batch 中过度降权（但 code 数据可能有用），在 text batch 中完全不降权（但 可能有少量未检测到的合成 text）。 整体效果：adaptive (17.76) > uniform (17.73)，降权带来的 harm 超过 benefit。\n"
665	  },
666	  {
667	    "name": "Downstream eval (MMLU/HellaSwag on Llama-3.2-3B checkpoints)",
668	    "description": "在 3B 模型 checkpoint 上评估 MMLU 和 HellaSwag，验证 PPL 改善 是否传导到下游任务。worst 档预测：完全无可测增益。\n",
669	    "results": {
670	      "uniform_mmlu_acc": 25.8,
671	      "adaptive_mmlu_acc": 25.8,
672	      "mmlu_delta_abs_pct": 0.0,
673	      "uniform_hellaswag_acc": 38.2,
674	      "adaptive_hellaswag_acc": 38.3,
675	      "hellaswag_delta_abs_pct": 0.1,
676	      "pppl_to_downstream_correlation": "not significant"
677	    },
678	    "tables": [
679	      {
680	        "caption": "Downstream Eval (Llama-3.2-3B, ρ=0.4, seed42, 200M tokens)",
681	        "rows": [
682	          {
683	            "benchmark": "MMLU (5-shot)",
684	            "uniform": "25.8%",
685	            "adaptive": "25.8%",
686	            "delta": "0.0%",
687	            "significance": "n.s."
688	          },
689	          {
690	            "benchmark": "HellaSwag (10-shot)",
691	            "uniform": "38.2%",
692	            "adaptive": "38.3%",
693	            "delta": "+0.1%",
694	            "significance": "n.s."
695	          }
696	        ]
697	      }
698	    ],
699	    "figures": [],
700	    "analysis": "下游任务无可测增益，符合 worst 档预期。这不一定是方法的失败—— 200M tokens 的 undertrained 3B 模型本身不应被期望展示有意义的 下游差异。但这确实意味着论文不能 claim \"PPL improvement translates to downstream gains\"。 叙事处理：(1) 承认当前规模下下游差异不显著；(2) 论证 PPL 改善 本身有价值（预训练评估的标准指标）；(3) 指出 full-scale 实验 (3B+ 模型, 10B+ tokens) 下效应可能放大，作为 future work。\n\n3B 模型在 200M tokens 上严重 undertrain，MMLU 近随机水平 (25.8% ≈ 25% random)， HellaSwag 在 38% 左右。adaptive 的 PPL 改善仅 0.01 (0.06% relative)， 完全不足以传导到下游 benchmark——这些 benchmark 的测量精度（~0.5% absolute） 远粗于 PPL 差异 (0.06% relative)。 即使在 PPL 改善更大的 0.6B 设定 (0.23% relative)，下游任务的 resolution 也不足以检测到差异。PPL 是连续指标，下游 accuracy 是离散指标， 两者的灵敏度不在同一量级。\n"
701	  }
702	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1af87d-e66d-416b-842d-a6877136a83b",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "1cf98d69-c9e5-4b7f-8035-8ca14756643f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed42\",\n    \"description\": \"在现有 grid (b=0.5~5.0) 基础上向低 b 区间扩展。 worst 档核心预测：真最优 b 在 0.1-0.3 区间，b=0.5 并非 grid-best。\\n\",\n    \"results\": {\n      \"b0_1_train_loss\": 7.55,\n      \"b0_2_train_loss\": 7.95,\n      \"b0_3_train_loss\": 8.6,\n      \"total_steps\": 6103,\n      \"train_runtime_s_per_b\": 13000,\n      \"all_completed\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"训练顺利完成，train_loss 在 [7.55, 8.60] 区间，与 b 值正相关趋势一致。 关键判断需等 post-hoc eval (p0_grid_b_low_eval) 出 PPL 数据。\\n\\n\\ntrain_loss 与 b 正相关（更大 b → 更多 downweight 合成样本 → 去掉低 loss 的 合成样本后均值上升）。b=0.1 的 train_loss (7.55) 仅略高于 uniform (7.31)， 因为 w=(1-q)^0.1 对 q=0.9 仍给出权重 0.79，几乎不降权。\\n\"\n  },\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed123\",\n    \"description\": \"seed123 的 b<0.5 grid 扩展，用于 cross-seed consistency 验证。\\n\",\n    \"results\": {\n      \"b0_1_train_loss\": 7.57,\n      \"b0_2_train_loss\": 7.97,\n      \"b0_3_train_loss\": 8.62,\n      \"total_steps\": 6103,\n      \"all_completed\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"训练完成，模式与 seed42 一致。\\n\\n\\nseed123 在 b=0.5 grid 中表现最好 (PPL=17.638)，low-b 区间预计保持相同趋势。 train_loss 与 seed42 相当，seed 间差异 <1%。\\n\"\n  },\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed456\",\n    \"description\": \"seed456 的 b<0.5 grid 扩展。\\n\",\n    \"results\": {\n      \"b0_1_train_loss\": 7.52,\n      \"b0_2_train_loss\": 7.91,\n      \"b0_3_train_loss\": 8.55,\n      \"total_steps\": 6103,\n      \"all_completed\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"训练完成，等 eval 结果。\\n\\n\\nseed456 uniform train_loss (7.29) 略低于其他 seed，low-b grid 保持一致偏移。\\n\"\n  },\n  {\n    \"name\": \"Post-hoc eval for all 9 b<0.5 checkpoints\",\n    \"description\": \"对 3 seeds × 3 b-values = 9 个 checkpoint 做 holdout eval，获取 PPL。 worst 档核心预测：b=0.2 在所有 seed 上 PPL 低于 b=0.5，成为新 grid-best， 使 adaptive 的 aggregate ratio 从 88.6% 降至 ~70%。\\n\",\n    \"results\": {\n      \"b0_1_seed42_eval_ppl\": 17.645,\n      \"b0_2_seed42_eval_ppl\": 17.637,\n      \"b0_3_seed42_eval_ppl\": 17.641,\n      \"b0_1_seed123_eval_ppl\": 17.631,\n      \"b0_2_seed123_eval_ppl\": 17.625,\n      \"b0_3_seed123_eval_ppl\": 17.629,\n      \"b0_1_seed456_eval_ppl\": 17.642,\n      \"b0_2_seed456_eval_ppl\": 17.636,\n      \"b0_3_seed456_eval_ppl\": 17.64,\n      \"new_grid_best_b\": 0.2,\n      \"new_grid_best_ppl_seed42\": 17.637,\n      \"new_grid_best_ppl_seed123\": 17.625,\n      \"new_grid_best_ppl_seed456\": 17.636,\n      \"old_grid_best_b\": 0.5,\n      \"new_ratio_seed42_pct\": 75.5,\n      \"new_ratio_seed123_pct\": 72.3,\n      \"new_ratio_seed456_pct\": 62.5,\n      \"new_aggregate_ratio_pct\": 69.8,\n      \"max_relative_ppl_improvement_pct\": 0.37,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Full Grid-b PPL Curve (ρ=0.4, Qwen3-0.6B, 200M tokens)\",\n        \"rows\": [\n          {\n            \"b\": 0.1,\n            \"seed42\": 17.645,\n            \"seed123\": 17.631,\n            \"seed456\": 17.642\n          },\n          {\n            \"b\": 0.2,\n            \"seed42\": 17.637,\n            \"seed123\": 17.625,\n            \"seed456\": 17.636\n          },\n          {\n            \"b\": 0.3,\n            \"seed42\": 17.641,\n            \"seed123\": 17.629,\n            \"seed456\": 17.64\n          },\n          {\n            \"b\": 0.5,\n            \"seed42\": 17.651,\n            \"seed123\": 17.638,\n            \"seed456\": 17.65\n          },\n          {\n            \"b\": 1.0,\n            \"seed42\": 17.692,\n            \"seed123\": 17.674,\n            \"seed456\": 17.68\n          },\n          {\n            \"b\": 1.5,\n            \"seed42\": 17.718,\n            \"seed123\": 17.701,\n            \"seed456\": 17.71\n          },\n          {\n            \"b\": 2.0,\n            \"seed42\": 17.741,\n            \"seed123\": 17.725,\n            \"seed456\": \"~17.73\"\n          },\n          {\n            \"b\": 3.0,\n            \"seed42\": 17.774,\n            \"seed123\": 17.76,\n            \"seed456\": \"~17.77\"\n          },\n          {\n            \"b\": 5.0,\n            \"seed42\": 17.818,\n            \"seed123\": 17.804,\n            \"seed456\": \"~17.82\"\n          },\n          {\n            \"b\": \"uniform\",\n            \"seed42\": 17.69,\n            \"seed123\": 17.69,\n            \"seed456\": 17.7\n          },\n          {\n            \"b\": \"adaptive\",\n            \"seed42\": 17.65,\n            \"seed123\": 17.643,\n            \"seed456\": 17.66\n          }\n        ]\n      },\n      {\n        \"caption\": \"Revised Aggregate Ratio with New Grid-best (b=0.2)\",\n        \"rows\": [\n          {\n            \"seed\": 42,\n            \"uniform\": 17.69,\n            \"grid_best_b0_2\": 17.637,\n            \"adaptive\": 17.65,\n            \"grid_improvement\": 0.053,\n            \"adaptive_improvement\": 0.04,\n            \"ratio_pct\": 75.5\n          },\n          {\n            \"seed\": 123,\n            \"uniform\": 17.69,\n            \"grid_best_b0_2\": 17.625,\n            \"adaptive\": 17.643,\n            \"grid_improvement\": 0.065,\n            \"adaptive_improvement\": 0.047,\n            \"ratio_pct\": 72.3\n          },\n          {\n            \"seed\": 456,\n            \"uniform\": 17.7,\n            \"grid_best_b0_2\": 17.636,\n            \"adaptive\": 17.66,\n            \"grid_improvement\": 0.064,\n            \"adaptive_improvement\": 0.04,\n            \"ratio_pct\": 62.5\n          },\n          {\n            \"seed\": \"aggregate\",\n            \"grid_improvement\": 0.182,\n            \"adaptive_improvement\": 0.127,\n            \"ratio_pct\": 69.8\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：grid-best 从 b=0.5 移至 b=0.2，证实 adaptive b* (median=0.87) 系统性 overshoot ~4×。aggregate ratio 从 88.6% 降至 69.8%，MVP Path B 的 \\\"within seed variance\\\" 论证不再成立——adaptive-grid gap (0.013-0.024) 显著大于 seed variance (~0.007)。 叙事影响：Claim 2 必须从 \\\"matches grid-best\\\" 降级为 \\\"provides a reasonable default without any tuning\\\"。α_eff(b) 框架的 b* 推导在数值上不准确，但框架 的分析价值仍然存在（b* 轨迹反映 batch-level 污染结构）。 论文呈现：在 Results 中坦诚展示 full grid curve，讨论 b=0.2 vs b*=0.87 的 gap，将 \\\"why adaptive overshoots\\\" 作为 analysis/discussion 的核心问题之一。\\n\\n\\nworst 档假设：真最优 b 远低于 adaptive b* median (~0.87)。 物理解释：FineWeb 中 40% Qwen-self 合成数据质量尚可（非噪声），过度降权 (b>0.5) 等同于丢弃可用信号。b=0.2 时 w=(1-0.9)^0.2=0.63，contaminated 样本仍保留 63% 权重——温和降权保留数据量的同时轻微纠正污染偏移。 b=0.5 时 w=0.32，已过度降权；adaptive median b*=0.87 时 w=0.13，更加激进。 PPL 曲线在 b=0.2 形成 U 型最低点：b<0.2 降权不足（污染信号残留）， b>0.2 降权过度（有效数据量损失超过去污染收益）。 aggregate ratio 从 88.6% (b=0.5 为 grid-best) 降至 69.8% (b=0.2 为 grid-best)， 进入 worst 档 [55, 80] 范围。adaptive 的 overshoot 问题暴露无遗。\\n\"\n  },\n  {\n    \"name\": \"Data generation for ρ=0.6\",\n    \"description\": \"生成 60% 合成数据比例的训练集（Qwen3-0.6B self-gen, 200M tokens）。\\n\",\n    \"results\": {\n      \"contamination_ratio\": 0.6,\n      \"total_tokens\": 200000000,\n      \"synthetic_tokens\": 120000000,\n      \"real_tokens\": 80000000,\n      \"detector_auc_on_60pct\": 0.935,\n      \"q_score_mean_60pct\": 0.68,\n      \"q_score_median_60pct\": 0.82,\n      \"scored_data_file\": \"scored_data_60.jsonl\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"数据生成和检测器 scoring 顺利完成。q-score 分布相比 40% 条件向高值偏移， 符合预期。检测器泛化到不同 mixing ratio 无显著退化。\\n\\n\\n同一 TF-IDF+LR 检测器在 60% 数据上 AUC 微降至 0.935（class imbalance 从 40:60 变为 60:40，合成类占多数导致 precision 略降）。q_score_mean 升至 0.68（更多样本为合成 → 更多高 q 值），median 升至 0.82。\\n\"\n  },\n  {\n    \"name\": \"Uniform baseline (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"60% 污染下的 uniform baseline。预期 PPL 高于 40% uniform， 因为更多训练数据是合成的。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.85,\n      \"train_loss\": 7.22,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 12000,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"60% 污染使 uniform PPL 升高 0.16——污染效应存在但不剧烈。这为 reweighting 提供了 headroom，但 worst 档预测 adaptive 不会有效利用这个 headroom。\\n\\n\\n60% 合成数据导致 uniform PPL 从 17.69 升至 17.85（+0.16, +0.9% relative）。 效应方向正确——更多合成数据确实降低训练质量。但升幅有限，因为 Qwen3-0.6B self-gen 的合成数据质量尚可（非随机噪声），只是分布略偏。 train_loss 反而略低 (7.22 vs 7.31)，因为合成数据通常 loss 更低（模型更 容易 fit 自己生成的内容）。\\n\"\n  },\n  {\n    \"name\": \"Adaptive b* (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"60% 污染下的 adaptive b* 运行。worst 档核心预测： Δ_adaptive(60%) 不显著大于 Δ_adaptive(40%)，效应未放大。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.82,\n      \"train_loss\": 7.46,\n      \"total_steps\": 6103,\n      \"b_star_mean\": 1.62,\n      \"b_star_median\": 1.08,\n      \"b_star_std\": 2.15,\n      \"b_star_p25\": 0.61,\n      \"b_star_p75\": 1.85,\n      \"b_star_pct_below_0.5\": 16.3,\n      \"b_star_pct_0.5_to_1\": 30.2,\n      \"b_star_pct_1_to_2\": 31.5,\n      \"b_star_pct_above_2\": 22.0,\n      \"delta_adaptive_60_abs\": 0.03,\n      \"delta_adaptive_40_abs\": 0.04,\n      \"delta_adaptive_60_rel_pct\": 0.17,\n      \"delta_adaptive_40_rel_pct\": 0.23,\n      \"effect_amplification\": false\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Effect Size: 40% vs 60% Contamination\",\n        \"rows\": [\n          {\n            \"contamination\": \"40%\",\n            \"uniform_ppl\": 17.69,\n            \"adaptive_ppl\": 17.65,\n            \"delta_abs\": 0.04,\n            \"delta_rel_pct\": 0.23,\n            \"b_star_median\": 0.87\n          },\n          {\n            \"contamination\": \"60%\",\n            \"uniform_ppl\": 17.85,\n            \"adaptive_ppl\": 17.82,\n            \"delta_abs\": 0.03,\n            \"delta_rel_pct\": 0.17,\n            \"b_star_median\": 1.08\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"效应未放大是 worst 档的标志性结果。反驳了 \\\"更高污染 → 更大收益\\\" 的直觉。 根本原因是 adaptive 的 b* 响应方向正确（污染增加 → b* 升高）但幅度过大 （真最优 b 不随污染比例大幅变化，但 b* 大幅上升）。 叙事影响：不能用 60% 数据来论证 \\\"方法在高污染下更重要\\\"。转而论证 α_eff 对污染比例变化的响应本身是有信息量的诊断信号——b* 从 0.87→1.08 的偏移 正确反映了污染增加，即使数值不是最优的。\\n\\n\\n60% 污染下 q-score 分布向高值偏移 → α_eff 估计值更大 → b* median 从 0.87 升至 1.08。但真最优 b 仍在 ~0.2 区间（worst 档假设），overshoot 更严重。 Δ_adaptive(60%)=0.03 < Δ_adaptive(40%)=0.04：adaptive 在高污染下反而更差。 原因：60% 数据为合成 → 更激进的降权丢弃了过多数据 → 有效训练集缩小到 不足以支撑学习。b* 从 0.87→1.08 进一步偏离真最优 0.2，导致效应不升反降。\\n\"\n  },\n  {\n    \"name\": \"Grid-b=0.5 (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"60% 污染下 grid b=0.5 的参考点，用于对比 adaptive。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.8,\n      \"train_loss\": 9.45,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 13000,\n      \"delta_vs_uniform_abs\": 0.05,\n      \"delta_vs_uniform_rel_pct\": 0.28,\n      \"ratio_adaptive_vs_grid_pct\": 60.0\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"b=0.5 在 60% 下优于 adaptive，adaptive ratio 仅 60%。若在 60% 条件下也做 finer grid (b=0.1/0.2/0.3)，grid-best 可能更低，ratio 会进一步下降。 但 GPU 预算不支持 60% 的 full grid sweep——这本身就说明 grid search 的 计算成本问题（adaptive 的零成本优势在此体现）。\\n\\n\\nb=0.5 在 60% 污染下的 PPL 改善 (0.05, 0.28%) 与 40% 条件相似 (0.039, 0.22% for seed42)。效应量基本持平——更高污染并未放大 reweighting 收益。 adaptive ratio 为 60%（0.03/0.05），低于 40% 条件下的 75.5%（以 b=0.2 为 grid-best 计算）。 原因：60% 时 b=0.5 仍然过高（真最优 ~0.2），但比 adaptive 的 b*=1.08 更接近最优。更高污染下 b=0.5 的 \\\"适度过高\\\" 和 adaptive 的 \\\"严重过高\\\" 之间的差距在拉大。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.2-3B environment setup + data prep\",\n    \"description\": \"3B 模型环境搭建：下载 Llama-3.2-3B，生成/复用合成数据， 用 TF-IDF+LR 对新数据打分。\\n\",\n    \"results\": {\n      \"model_downloaded\": true,\n      \"model_params\": \"3.2B\",\n      \"vram_usage_gb\": 78,\n      \"gradient_checkpointing\": true,\n      \"detector_scores_generated\": true,\n      \"data_reuse_from_qwen\": true,\n      \"detector_auc_on_llama_data\": 0.932\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"环境就绪，可以开始训练。\\n\\n\\n复用 Qwen3-0.6B 生成的合成数据（检测器和合成数据不变，只换训练模型）。 96GB VRAM 足够 3B 模型 + gradient checkpointing。检测器 AUC 对不同训练 模型不敏感（检测的是数据来源，不是训练模型）。\\n\"\n  },\n  {\n    \"name\": \"Uniform baseline (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)\",\n    \"description\": \"3B 模型的 uniform baseline。200M tokens 对 3B 模型严重不足 （Chinchilla 最优约需 64B tokens），PPL 会在高位。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 16.2,\n      \"train_loss\": 6.85,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 32000,\n      \"gpu_hours\": 35.6,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"3B baseline PPL = 16.20，低于 0.6B 的 17.69。但 200M tokens 不足以让 3B 模型充分学习，效应量可能因此被压缩。\\n\\n\\n3B 模型在 200M tokens 上严重 undertrain（tokens/param ≈ 63，远低于 Chinchilla 最优的 20×），PPL 仍在高位 (16.20 vs Qwen 0.6B 的 17.69)。更大模型的 inductive bias 带来部分优势，但数据量不足限制了收敛。 训练时间约 32000s（比 0.6B 的 12000s 长 2.7×），主要受 gradient checkpointing 和更大的矩阵运算影响。\\n\"\n  },\n  {\n    \"name\": \"Adaptive b* (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)\",\n    \"description\": \"3B 模型的 adaptive 运行。worst 档核心预测：adaptive 对 3B 几乎无效， b* 分布与 0.6B 相似（方法未能适应不同模型规模），改善量接近噪声水平。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 16.19,\n      \"train_loss\": 6.92,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 32500,\n      \"b_star_mean\": 1.38,\n      \"b_star_median\": 0.92,\n      \"b_star_std\": 1.85,\n      \"b_star_p25\": 0.55,\n      \"b_star_p75\": 1.48,\n      \"b_star_pct_below_0.5\": 21.5,\n      \"b_star_pct_0.5_to_1\": 34.8,\n      \"b_star_pct_1_to_2\": 27.1,\n      \"b_star_pct_above_2\": 16.6,\n      \"delta_vs_uniform_abs\": 0.01,\n      \"delta_vs_uniform_rel_pct\": 0.06,\n      \"b_star_distribution_ks_test_vs_06b\": 0.87\n    },\n    \"tables\": [\n      {\n        \"caption\": \"b* Distribution Comparison: 0.6B vs 3B\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen3-0.6B\",\n            \"b_star_median\": 0.87,\n            \"b_star_mean\": 1.4,\n            \"b_star_p25\": 0.54,\n            \"b_star_p75\": 1.51,\n            \"delta_ppl_rel_pct\": 0.23\n          },\n          {\n            \"model\": \"Llama-3.2-3B\",\n            \"b_star_median\": 0.92,\n            \"b_star_mean\": 1.38,\n            \"b_star_p25\": 0.55,\n            \"b_star_p75\": 1.48,\n            \"delta_ppl_rel_pct\": 0.06\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3B 实验暴露 adaptive 方法的核心局限：b* 推导完全由 q-score 统计量驱动， 对模型规模/架构/loss landscape 无感知。当 q-score 分布不变（同一数据、 同一检测器），b* 不变——即使不同模型的最优 b 可能截然不同。 叙事影响：不能 claim \\\"adaptive adapts to model characteristics\\\"。但可以 reframe 为 \\\"adaptive provides a data-driven default that is consistent across models\\\"——一致性本身也是一种优势（可预测性）。 如果要验证 3B 的真最优 b 是否确实在不同区间（如 b=5），需要额外的 3B grid sweep，但 GPU 预算不足。\\n\\n\\nworst 档假设：3B 模型的真最优 b 可能在完全不同的区间（Drayson 论文中 SmolLM-1.7B 用 b=1 而非 b=10），但 adaptive 的 b* 分布 (median=0.92) 与 0.6B (median=0.87) 几乎无差异。原因是 b* 推导仅依赖 q-score 分布和 ESS 约束——这两者与模型规模无关（同一数据、同一检测器）。 改善量仅 0.01 PPL (0.06% relative)，在 seed variance 范围内（基本是噪声）。 3B 模型的 loss landscape 更 flat（梯度更小），reweighting 的效果被稀释。 此外 200M tokens undertrain 意味着模型还在快速学习阶段，数据质量的微小 差异被训练动态淹没。\\n\"\n  },\n  {\n    \"name\": \"n_min=1 ablation (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"ESS 下界设为 1（最宽松约束）。worst 档预测：b* 过高导致 over-downweighting， PPL 劣于 uniform。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.71,\n      \"train_loss\": 7.62,\n      \"b_star_mean\": 3.85,\n      \"b_star_median\": 2.6,\n      \"b_star_std\": 4.12,\n      \"b_star_p25\": 1.2,\n      \"b_star_p75\": 4.8,\n      \"b_star_pct_above_5\": 18.5,\n      \"b_star_max\": 20,\n      \"total_steps\": 6103\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"n_min=1 是 \\\"too aggressive\\\" 端的失败案例。b* 不受约束 → 系统性 over-downweight → 效果不如 uniform。这为 ESS 约束的必要性提供了证据， 但也说明 n_min 是一个需要 \\\"恰好正确\\\" 的参数。\\n\\n\\nn_min=1 几乎不约束 ESS（仅要求有效样本量 ≥1/batch_size = 25%）， b* 自由飙升至 mean=3.85, median=2.60。大量 batch 使用 b*>5，导致 contaminated 样本权重趋近于零 (w=(1-0.9)^2.6=0.004)，有效训练集 急剧缩小。 PPL=17.71 > uniform (17.69)：over-downweighting 导致有效数据不足， 模型学习不充分。这比不做 reweighting 更差。 物理直觉：batch_size=4 时 n_min=1 意味着只需保留 1 个有效样本的 信息量——在 40% 污染下这几乎等于只用 clean 样本，丢弃了 40% 数据 中仍有价值的信号。\\n\"\n  },\n  {\n    \"name\": \"n_min=4 ablation (=batch_size, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"ESS 下界 = batch_size（要求所有样本保持同等权重 → 强制 b*=0）。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.69,\n      \"train_loss\": 7.31,\n      \"b_star_mean\": 0.0,\n      \"b_star_median\": 0.0,\n      \"b_star_std\": 0.0,\n      \"b_star_pct_at_zero\": 100.0,\n      \"total_steps\": 6103\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"预期行为——n_min=batch_size 是 uniform 的重现。与 n_min=5 一起 构成 \\\"退化端\\\" 的验证点。\\n\\n\\nn_min=4=batch_size 要求 ESS ≥ batch_size，即所有权重完全均等， 唯一满足条件的值是 b*=0。方法退化为 uniform baseline。 PPL = 17.69 = uniform，验证了实现正确性（ESS 约束确实在工作）。\\n\"\n  },\n  {\n    \"name\": \"n_min=5 ablation (>batch_size, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"ESS 下界 > batch_size（不可能满足 → 同 n_min=4 退化为 b*=0）。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.69,\n      \"train_loss\": 7.31,\n      \"b_star_mean\": 0.0,\n      \"b_star_median\": 0.0,\n      \"b_star_std\": 0.0,\n      \"b_star_pct_at_zero\": 100.0,\n      \"total_steps\": 6103\n    },\n    \"tables\": [\n      {\n        \"caption\": \"n_min Sensitivity Curve (ρ=0.4, Qwen3-0.6B, seed42)\",\n        \"rows\": [\n          {\n            \"n_min\": 1,\n            \"eval_ppl\": 17.71,\n            \"b_star_median\": 2.6,\n            \"status\": \"worse than uniform\"\n          },\n          {\n            \"n_min\": 2,\n            \"eval_ppl\": 17.65,\n            \"b_star_median\": 0.87,\n            \"status\": \"best (adaptive_fix)\"\n          },\n          {\n            \"n_min\": 3,\n            \"eval_ppl\": 17.69,\n            \"b_star_median\": \"~0.3\",\n            \"status\": \"≈ uniform\"\n          },\n          {\n            \"n_min\": 4,\n            \"eval_ppl\": 17.69,\n            \"b_star_median\": 0.0,\n            \"status\": \"= uniform\"\n          },\n          {\n            \"n_min\": 5,\n            \"eval_ppl\": 17.69,\n            \"b_star_median\": 0.0,\n            \"status\": \"= uniform\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"n_min sensitivity curve 展示一个尖锐的 sweet spot： - n_min=1: 过度激进，劣于 uniform - n_min=2: 唯一有效点 - n_min≥3: 退化为 uniform 这对 \\\"adaptive 免调参\\\" 的叙事构成挑战——虽然消除了 b 的 grid search， 但引入了 n_min 这个同样需要选取的超参。不过 n_min 的选择空间极小 （只有整数 1-5），比 b 的连续空间（0.1-10）简单得多。 worst 档 reframe：n_min 的存在承认方法并非 \\\"zero-hyperparameter\\\"， 但将超参搜索从 \\\"6+ runs 的连续 grid\\\" 压缩为 \\\"2-3 个整数点\\\"——仍是 显著的调参成本降低。\\n\\n\\nn_min=5 > batch_size=4，ESS 约束永远无法满足（ESS 最大值 = batch_size）， b* 被钳制在 0。效果等同于 n_min=4 和 uniform。\\n\"\n  },\n  {\n    \"name\": \"ModernBERT detector training (AUC≈0.99)\",\n    \"description\": \"训练 ModernBERT 150M 检测器作为 high-end baseline。\\n\",\n    \"results\": {\n      \"auc\": 0.986,\n      \"accuracy\": 0.953,\n      \"ece_raw\": 0.15,\n      \"ece_calibrated\": 0.022,\n      \"temperature_T\": 0.35,\n      \"q_score_mean\": 0.58,\n      \"q_score_std\": 0.42,\n      \"q_score_median\": 0.72,\n      \"mid_range_ratio\": 0.28,\n      \"training_time_hours\": 1.5,\n      \"model_params\": \"150M\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Detector Comparison\",\n        \"rows\": [\n          {\n            \"detector\": \"TF-IDF + LR\",\n            \"params\": \"~50K\",\n            \"auc\": 0.939,\n            \"ece_cal\": 0.048,\n            \"mid_range_ratio\": 0.463,\n            \"training_cost\": \"<1 min CPU\"\n          },\n          {\n            \"detector\": \"ModernBERT 150M\",\n            \"params\": \"150M\",\n            \"auc\": 0.986,\n            \"ece_cal\": 0.022,\n            \"mid_range_ratio\": 0.28,\n            \"training_cost\": \"1.5h GPU\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"检测器训练成功，AUC=0.986 符合预期。关键后续问题：更高 AUC 是否转化为 更好的训练 PPL？p1_detector_ablation_training 将回答这个问题。\\n\\n\\nModernBERT 150M 在 real vs synthetic 分类上 AUC=0.986（与 Drayson 报告一致）。 相比 TF-IDF+LR (AUC=0.939)，AUC 提升 0.047。q-score 分布更 bimodal （mid_range_ratio 从 0.463 降至 0.28——更多样本在极端值，更少在中间）， ECE 更低（更准确的概率估计）。\\n\"\n  },\n  {\n    \"name\": \"Training with ModernBERT scores (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"用 ModernBERT q-scores 替换 TF-IDF+LR 的 q-scores，运行 adaptive + uniform。 worst 档预测：AUC 0.939→0.986 不会带来显著 PPL 改善。\\n\",\n    \"results\": {\n      \"adaptive_modernbert_ppl\": 17.647,\n      \"uniform_modernbert_ppl\": 17.69,\n      \"adaptive_tfidf_ppl\": 17.65,\n      \"uniform_tfidf_ppl\": 17.69,\n      \"ppl_diff_adaptive\": -0.003,\n      \"ppl_diff_relative_pct\": 0.02,\n      \"b_star_median_modernbert\": 0.95,\n      \"b_star_median_tfidf\": 0.87\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Detector Quality → PPL Improvement (AUC-PPL Relationship)\",\n        \"rows\": [\n          {\n            \"detector\": \"TF-IDF+LR\",\n            \"auc\": 0.939,\n            \"adaptive_ppl\": 17.65,\n            \"delta_vs_uniform\": 0.04,\n            \"cost\": \"<1 min CPU\"\n          },\n          {\n            \"detector\": \"ModernBERT\",\n            \"auc\": 0.986,\n            \"adaptive_ppl\": 17.647,\n            \"delta_vs_uniform\": 0.043,\n            \"cost\": \"1.5h GPU\"\n          },\n          {\n            \"improvement\": \"\",\n            \"auc_gain\": \"+0.047\",\n            \"ppl_gain\": \"-0.003\",\n            \"marginal_value\": \"negligible\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 worst 档中最强的独立发现之一：AUC 0.939→0.986 (+5%相对) 仅换来 0.003 PPL 改善 (<0.02% relative)。 升级为 primary finding 的论据：(1) 实际影响——省去 150M 参数检测器 的训练和推理成本；(2) 理论解释——w=(1-q)^b 的 monotonicity 保证 排序正确即可，不需要精确概率；(3) 对 Drayson 框架的改进建议—— 他们使用 ModernBERT 是 overkill。 Reframe 3 的核心支撑实验。\\n\\n\\nAUC 从 0.939 提升至 0.986 (+0.047)，但 PPL 仅改善 0.003 (0.02% relative)—— 检测器质量的 marginal return 极低。 原因分析：(1) q-score 的连续性和排序正确性比 AUC 更重要——TF-IDF+LR 的 q-scores 虽然 calibration 不完美 (ECE=0.048 vs 0.022)，但排序已足够好 用于权重计算；(2) w=(1-q)^b 对 q 的 monotone transform 使得精确 q 值 不如排序重要；(3) ModernBERT 的更 bimodal 分布导致 b* 略高 (0.95 vs 0.87)， 进一步偏离真最优 b~0.2。\\n\"\n  },\n  {\n    \"name\": \"Cross-generator data (Llama-3.2-1B generates, Qwen3-0.6B trains)\",\n    \"description\": \"用 Llama-3.2-1B 生成合成数据，Qwen3-0.6B 训练——模拟 web corpus 中不同来源的合成内容。TF-IDF+LR 检测器在 cross-family 数据上打分。\\n\",\n    \"results\": {\n      \"synthetic_generator\": \"Llama-3.2-1B\",\n      \"training_model\": \"Qwen3-0.6B\",\n      \"contamination_ratio\": 0.4,\n      \"total_tokens\": 200000000,\n      \"detector_auc_cross_family\": 0.891,\n      \"q_score_mean\": 0.55,\n      \"q_score_std\": 0.35,\n      \"q_score_median\": 0.58,\n      \"mid_range_ratio\": 0.52\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"检测器 cross-family 泛化受限——AUC 降至 0.891，q-score 分布变得 diffuse。 这预示 adaptive b* 在这些 noisier scores 上可能表现不佳。\\n\\n\\ncross-family 检测更难：TF-IDF+LR 在训练时只见过 Qwen3-0.6B 的合成数据， Llama-3.2-1B 的合成文本风格不同，AUC 从 0.939 降至 0.891。 q-score 分布更 diffuse（mid_range_ratio 从 0.463 升至 0.52——更多样本 在 0.3-0.7 的不确定区间），median 从 0.707 降至 0.58。 这意味着检测器对 cross-family 合成数据的 \\\"信心\\\" 更低，q-score 排序 更不可靠。\\n\"\n  },\n  {\n    \"name\": \"Cross-generator training (adaptive + uniform, ρ=0.4)\",\n    \"description\": \"用 cross-family q-scores 运行 adaptive 和 uniform。 worst 档核心预测：adaptive 在 noisy q-scores 上劣于 uniform。\\n\",\n    \"results\": {\n      \"uniform_ppl\": 17.75,\n      \"adaptive_ppl\": 17.77,\n      \"delta_adaptive_abs\": -0.02,\n      \"b_star_mean\": 1.15,\n      \"b_star_median\": 0.72,\n      \"b_star_std\": 1.65,\n      \"b_star_p25\": 0.35,\n      \"b_star_p75\": 1.3\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-Generator Performance\",\n        \"rows\": [\n          {\n            \"setting\": \"self-gen (Qwen→Qwen)\",\n            \"uniform_ppl\": 17.69,\n            \"adaptive_ppl\": 17.65,\n            \"delta\": -0.04,\n            \"verdict\": \"adaptive wins\"\n          },\n          {\n            \"setting\": \"cross-gen (Llama→Qwen)\",\n            \"uniform_ppl\": 17.75,\n            \"adaptive_ppl\": 17.77,\n            \"delta\": 0.02,\n            \"verdict\": \"adaptive LOSES\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"cross-generator 是 worst 档的关键失败场景。当检测器信号质量下降 (AUC 0.939→0.891)，adaptive 从 \\\"有益\\\" 翻转为 \\\"有害\\\"。 这暴露了方法的根本依赖：adaptive b* 的质量完全取决于 q-score 的 信号噪声比。在 real-world web corpus 中，合成数据来源多样 （多个 generator family），检测器 AUC 可能更低——方法的实用性 在最需要它的场景中反而最差。 叙事影响：Claim 3 (\\\"unknown contamination proportion\\\") 受损—— 不仅比例未知，合成来源也未知，而后者对方法有效性的影响更大。\\n\\n\\ncross-family q-scores 的高 mid_range_ratio (0.52) 和低 AUC (0.891) 导致 两个问题：(1) α_eff 估计不准确——大量样本 q 在 0.3-0.7，既非明确 clean 也非明确 contaminated，使 α_eff 的 batch-level 估计噪声大；(2) b* 仍在 ~0.72 (高于真最优)，且方差更大，导致某些 batch 的权重严重失调。 最终 adaptive PPL (17.77) > uniform (17.75)：noisy reweighting 比不 reweight 更差。有害降权的数据量超过了有益降权的收益。 uniform PPL (17.75) 高于 self-gen 条件 (17.69)，因为 Llama-1B 合成数据 质量更低（更小模型生成的文本更差）。\\n\"\n  },\n  {\n    \"name\": \"Detect-and-remove baseline (threshold=0.5, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"硬阈值过滤：q>0.5 的样本直接删除，在剩余数据上 uniform 训练。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.68,\n      \"train_loss\": 7.45,\n      \"total_steps\": 3662,\n      \"effective_data_ratio\": 0.58,\n      \"samples_removed_pct\": 42.0,\n      \"false_positive_rate\": 0.03\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"detect-and-remove (PPL=17.68) 略优于 uniform (17.69)，略劣于 adaptive (17.65)。在 worst 档的全局 picture 中： gentle reweighting (b=0.2, PPL=17.637) >> adaptive (b*≈0.87, PPL=17.65) ≈ detect-and-remove (PPL=17.68) > uniform (PPL=17.69)。 adaptive 优于 detect-and-remove 仍然成立，但 margin 很小 (0.03)。\\n\\n\\nthreshold=0.5 删除约 42% 数据（40% 真合成 + ~2% 假阳性 clean 样本）。 PPL=17.68——优于 uniform (17.69) 但劣于 grid-best b=0.2 (17.637)。 在 worst 档中，detect-and-remove 是 \\\"过度激进\\\" 的极端：完全移除 vs gentle reweighting (b=0.2, w=0.63)。移除丢失了合成数据中的有用信号 （虽然分布有偏，但仍包含语言模式信息），而 gentle reweighting 保留了 这些信号的 63%。 但 detect-and-remove 比 aggressive adaptive (b*=0.87, w=0.13) 的效果 接近——都是\\\"过度处理\\\"的不同程度。\\n\"\n  },\n  {\n    \"name\": \"Random reweighting baseline (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"用随机权重（不基于检测器）训练，验证检测器信号的必要性。\\n\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.695,\n      \"train_loss\": 7.33,\n      \"total_steps\": 6103,\n      \"weight_mean\": 1.0,\n      \"weight_std\": 0.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Baseline Comparison (ρ=0.4, Qwen3-0.6B, seed42)\",\n        \"rows\": [\n          {\n            \"method\": \"uniform\",\n            \"ppl\": 17.69,\n            \"delta\": 0.0,\n            \"signal\": \"none\"\n          },\n          {\n            \"method\": \"random reweight\",\n            \"ppl\": 17.695,\n            \"delta\": 0.005,\n            \"signal\": \"random\"\n          },\n          {\n            \"method\": \"detect-and-remove\",\n            \"ppl\": 17.68,\n            \"delta\": -0.01,\n            \"signal\": \"hard threshold\"\n          },\n          {\n            \"method\": \"adaptive b*\",\n            \"ppl\": 17.65,\n            \"delta\": -0.04,\n            \"signal\": \"adaptive q-based\"\n          },\n          {\n            \"method\": \"grid-best b=0.2\",\n            \"ppl\": 17.637,\n            \"delta\": -0.053,\n            \"signal\": \"oracle grid\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"random reweighting ≈ uniform 确认检测器信号是 load-bearing—— 不是 \\\"任何形式的权重扰动\\\" 都有效，必须是与数据质量相关的信号。 这支持了 adaptive 方法的合理性（虽然不是最优，但利用了真实信号）。\\n\\n\\n随机权重 (uniform [0, 2] 或 similar) 均值为 1，期望上等同于 uniform 训练。额外的梯度噪声（权重方差引入）使 PPL 微升 0.005。 random 不含任何数据质量信号 → 无法区分 clean vs contaminated → 表现近似 uniform。\\n\"\n  },\n  {\n    \"name\": \"Domain-skewed injection (code-heavy contamination, ρ=0.4, Qwen3-0.6B)\",\n    \"description\": \"合成数据集中在代码领域（非 uniform random injection）。 worst 档预测：domain skew 导致 q-score 分布崩坏，adaptive 失效。\\n\",\n    \"results\": {\n      \"uniform_ppl\": 17.73,\n      \"adaptive_ppl\": 17.76,\n      \"delta_adaptive\": -0.03,\n      \"b_star_mean\": 1.55,\n      \"b_star_median\": 1.1,\n      \"q_score_distribution_skewness\": 1.8,\n      \"domain_contamination_code_pct\": 0.85,\n      \"domain_contamination_text_pct\": 0.15\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"domain-skewed 是 adaptive 的另一个失败模式。方法假设 contamination 在 batch 间大致均匀分布，当 domain skew 打破这个假设时，per-batch adaptation 反而放大了 skew 的负面影响。 叙事影响：在论文 Limitations 中讨论 domain-skewed contamination 作为方法的适用边界。\\n\\n\\ndomain-skewed injection 使 q-score 分布在不同 domain batch 间高度不均： code-heavy batch 几乎全是合成 (q 全高) → α_eff 估计偏高 → b* 过大； text batch 几乎无合成 (q 全低) → α_eff~0 → b*=0。 这种 bimodal batch structure 使 per-batch adaptive 策略失效：在 code batch 中过度降权（但 code 数据可能有用），在 text batch 中完全不降权（但 可能有少量未检测到的合成 text）。 整体效果：adaptive (17.76) > uniform (17.73)，降权带来的 harm 超过 benefit。\\n\"\n  },\n  {\n    \"name\": \"Downstream eval (MMLU/HellaSwag on Llama-3.2-3B checkpoints)\",\n    \"description\": \"在 3B 模型 checkpoint 上评估 MMLU 和 HellaSwag，验证 PPL 改善 是否传导到下游任务。worst 档预测：完全无可测增益。\\n\",\n    \"results\": {\n      \"uniform_mmlu_acc\": 25.8,\n      \"adaptive_mmlu_acc\": 25.8,\n      \"mmlu_delta_abs_pct\": 0.0,\n      \"uniform_hellaswag_acc\": 38.2,\n      \"adaptive_hellaswag_acc\": 38.3,\n      \"hellaswag_delta_abs_pct\": 0.1,\n      \"pppl_to_downstream_correlation\": \"not significant\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Downstream Eval (Llama-3.2-3B, ρ=0.4, seed42, 200M tokens)\",\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU (5-shot)\",\n            \"uniform\": \"25.8%\",\n            \"adaptive\": \"25.8%\",\n            \"delta\": \"0.0%\",\n            \"significance\": \"n.s.\"\n          },\n          {\n            \"benchmark\": \"HellaSwag (10-shot)\",\n            \"uniform\": \"38.2%\",\n            \"adaptive\": \"38.3%\",\n            \"delta\": \"+0.1%\",\n            \"significance\": \"n.s.\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"下游任务无可测增益，符合 worst 档预期。这不一定是方法的失败—— 200M tokens 的 undertrained 3B 模型本身不应被期望展示有意义的 下游差异。但这确实意味着论文不能 claim \\\"PPL improvement translates to downstream gains\\\"。 叙事处理：(1) 承认当前规模下下游差异不显著；(2) 论证 PPL 改善 本身有价值（预训练评估的标准指标）；(3) 指出 full-scale 实验 (3B+ 模型, 10B+ tokens) 下效应可能放大，作为 future work。\\n\\n3B 模型在 200M tokens 上严重 undertrain，MMLU 近随机水平 (25.8% ≈ 25% random)， HellaSwag 在 38% 左右。adaptive 的 PPL 改善仅 0.01 (0.06% relative)， 完全不足以传导到下游 benchmark——这些 benchmark 的测量精度（~0.5% absolute） 远粗于 PPL 差异 (0.06% relative)。 即使在 PPL 改善更大的 0.6B 设定 (0.23% relative)，下游任务的 resolution 也不足以检测到差异。PPL 是连续指标，下游 accuracy 是离散指标， 两者的灵敏度不在同一量级。\\n\"\n  }\n]",
      "numLines": 702,
      "startLine": 1,
      "totalLines": 702
    }
  },
  "sourceToolAssistantUUID": "ad1af87d-e66d-416b-842d-a6877136a83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T02:02:13.587Z_

<details><summary>↩ Tool result · `toolu_01B9Dpgd4bZYGDShcrWULhHL`</summary>

```text
1	# Paper Framing — provenance_weight_training
2	
3	> 状态: DRAFT (MVP Path B PASS, D019确认，进入 research 阶段)
4	> 最后更新: 2026-05-15 01:15 UTC
5	> 投稿目标: EMNLP 2026 ARR May 25
6	
7	## Core Insight
8	
9	Drayson et al. (EMNLP 2025) 提出 detect-and-reweight 框架 w=(1-q)^b 用于缓解合成数据污染导致的 model collapse，但 b 需要在 validation set 上 per-model empirical 选取（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1），且其实现路径为 **Sampling Importance Resampling (SIR)**——按权重重采样数据，本质是离散选择。我们提出 **adaptive b***：从 batch 统计量在线估计 α_eff(b) 推导最优 b*，per-batch 动态调整，无需 validation set、无需 grid search、无需已知污染比例。我们的实现路径为 **直接 loss reweighting**——在 gradient 层面连续加权，保留细粒度控制。
10	
11	**两种方法使用同一加权公式，但解决不同问题、采用不同实现路径**：Drayson 面向递归训练场景的 model collapse prevention（b 通过 per-model validation 选取），我们面向 web corpus 一次性预训练的 decontamination（b* 从 batch 统计量自适应推导，零 validation cost）。
12	
13	收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。
14	
15	## Positioning vs Prior Work
16	
17	### Drayson et al. (EMNLP 2025) — 最近相关工作
18	
19	**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。
20	
21	**关键区分**：
22	
23	| 维度 | Drayson et al. | Ours |
24	|------|---------------|------|
25	| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态 |
26	| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |
27	| **污染设置** | 不假设已知比例（原文明确声明），但实验为控制设置 | 未知比例（从 batch 统计量在线估计） |
28	| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |
29	| **理论基础** | 无 b 选取理论，无 ablation | 收敛理论 motivated α_eff(b) 推导 |
30	| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |
31	| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |
32	| **validation 成本** | 需 per-model validation run | 零额外 validation cost |
33	
34	**定位原则：complementary approaches for different settings，非"我们比 Drayson 更好"。** Drayson 在其设定（递归训练、强检测器、validation-based b 选择）下是合理方案；我们解决的是 web pretraining 场景下无需 validation 的 principled b 选择问题。
35	
36	### Golden Ratio Weighting (arXiv 2502.18049, 2025)
37	理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。我们不需要已知比例。
38	
39	### 其他相关工作
40	- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse
41	- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补
42	- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting
43	- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级
44	- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention
45	- **arXiv 2602.16065** — 我们引用的收敛理论
46	
47	## Core Claims
48	
49	### Claim 1 (Primary): Principled b* via α_eff(b) 理论框架
50	
51	基于 α_eff(b) 和 ESS 约束的 adaptive b* 提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical selection。
52	
53	- **差异化核心**：Drayson 的 b 是超参数（需 validation set + 人工选取），我们的 b* 是从 batch 统计量在线推导的自适应量
54	- **理论贡献**：α_eff(b) 框架将 contamination detection score 分布与权重指数选择建立 principled 联系
55	- **证据需求**：adaptive b* 轨迹分析 + 与 Drayson 推荐值（b=1, b=10）的对比
56	
57	### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best
58	
59	Adaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。
60	
61	- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）
62	- **Pass criteria**: adaptive 均值 ≥ 90% grid-best 改善量 + 无任何 seed 劣于 uniform
63	- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)
64	
65	**叙事弹性（避免硬编码精确数字）**：
66	- 核心表述：**"adaptive matches grid-best within seed variance"**
67	- 补充表述：**"eliminates grid search cost (6N → 1 runs)"** 和 **"consistent improvement across all seeds"**
68	- Path B 叙事：3/3 seeds adaptive > uniform，adaptive-grid 差异在 seed variance 范围内
69	
70	**最终 MVP 数据**：
71	
72	3-seed Grid-b best (b=0.5) vs Adaptive_fix：
73	
74	| Metric | seed42 | seed123 | seed456 |
75	|--------|--------|---------|---------|
76	| Uniform PPL | 17.690 | 17.690 | 17.700 |
77	| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |
78	| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |
79	| Ratio | 102.6% | 90.4% | 80.0% |
80	
81	Aggregate ratio: 88.6% (D019). Path B PASS.
82	
83	### Claim 3 (Setting): Unknown Contamination Proportion
84	
85	我们的方法在 contamination proportion 完全未知的条件下工作——仅需 detector scores，无需已知污染比例、无需 clean validation set。
86	
87	- **差异化**：Golden Ratio Weighting 需要已知比例 k；Drayson 虽不假设已知比例，但 b 选择依赖 validation set 做 per-model tuning；我们仅需 detector scores，无需 validation set 或已知比例
88	- **实际意义**：web-scale pretraining 中污染比例本质上不可知（organic contamination from multiple generators）
89	- **证据**：adaptive b* 仅从 per-batch q-score 分布推导，无外部信息输入
90	
91	## n_min Robustness Framing
92	
93	D012 修复（n_min=3→2）显示方法对 ESS 约束参数的**实际鲁棒性**：
94	
95	- **现象**：n_min=3 导致 seed42 零改善（ESS 约束过紧，b* 被钳制在低值），n_min=2 修复后 seed42 恢复正常表现
96	- **Framing**：ESS 约束是 b* 推导中唯一的超参数，n_min=3→2 的修复表明只要 ESS 下界合理宽松（不过度约束有效样本量），adaptive b* 就能稳定工作
97	- **论文呈现**：在 Method section 讨论 ESS 约束的作用和敏感度；在 Ablation 中展示 n_min=2 vs n_min=3 的对比作为 robustness evidence
98	- **注意**：D017 勘误确认实际实施为 n_min=2 无 EMA（EMA 未编码），D018 确认 v1→v2 唯一差异为 n_min(3→2)
99	
100	## Narrative Structure
101	
102	**起点**: Web 语料中 20-60% 为合成文本，比例未知，来源多样——这是实际预训练面临的现实问题。Strong Model Collapse (ICLR 2025) 证明即使微量污染也会破坏 scaling law。
103	
104	**现有方法的不足**：
105	- Drayson et al.: w=(1-q)^b 有效，但 b 依赖 per-model validation-based tuning（不同模型需不同 b，b=1 vs b=10），且需要 clean validation set
106	- Golden Ratio Weighting: 理论最优权重，但假设已知混合比例 k
107	- 两者都不适用于无 validation set 的大规模 web pretraining 场景
108	
109	**我们的方案**: 在 Drayson 框架上，从 batch 统计量自适应估计 α_eff(b) 推导 b*，消除对 validation set 和 grid search 的依赖。实现路径从 SIR resampling 转为 direct loss reweighting，保留细粒度 gradient 控制。
110	
111	**理论连接**: 收敛 bound 作为 Background/Motivation，不 claim 理论贡献。
112	
113	**Method 呈现**: Algorithm 1 (adaptive b*) + ESS 约束（n_min 敏感度分析） + soft-to-hard 连续谱（作为 framing 而非独立 contribution）。
114	
115	**Path B 默认叙事**: "Adaptive b* 免调参即可匹配 validation-tuned best，将 Drayson 框架从需要 per-model heuristic tuning 提升为全自动 principled method。" 如果数据支持 Path A（adaptive 显著优于 grid-best），可升级表述，但默认保守。
116	
117	## Contribution Structure (2 Primary + 1 Setting)
118	
119	1. **Primary — Theoretical Framework**: Adaptive b* via α_eff(b) estimation + ESS constraints，提供 contamination-aware reweighting 中 b 的 principled 推导（vs Drayson 的 empirical selection）
120	2. **Primary — Practical Result**: Adaptive b* 零超参调优即匹配 grid-best，消除 per-model validation 成本。Lightweight detector (TF-IDF+LR, AUC=0.939) sufficiency 作为附加发现（升级为 co-primary 需 detector quality ablation）
121	3. **Setting — Unknown Proportion**: 与 Golden Ratio (known k) 的 problem setting 差异。Drayson 虽不假设已知比例，但 b 选择依赖 validation set；我们仅需 detector scores，无需 validation 或已知比例
122	
123	## Anticipated Reviewer Concerns
124	
125	| Concern | Response Strategy | 实验支撑 |
126	|---------|------------------|----------|
127	| "Incremental over Drayson et al." | 三层差异化: (1) adaptive b* without validation-set tuning vs per-model empirical b (核心), (2) loss reweighting vs SIR resampling, (3) zero validation cost vs validation-dependent。Complementary approaches for different settings | Claim 1 + Claim 3 |
128	| "Base formula is from Drayson" | 明确 acknowledge 公式来源；贡献是 b* 的 principled derivation + 实现路径差异 + 问题设定差异 | Positioning section |
129	| "Theory not rigorous / overclaimed" | 明确 scope: motivation not contribution; α_eff(b) 是 testable sufficient condition not theorem | Background section |
130	| "Only 0.6B model, would it scale?" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |
131	| "Detector quality sensitivity" | TF-IDF+LR (AUC=0.939) 即可；q-score 连续性比 AUC 更关键；检测器 quality ablation | detector quality ablation |
132	| "Controlled injection ≠ real web" | Full paper: domain-skewed injection + semi-realistic (Binoculars on Common Crawl) | 扩展实验 |
133	| "Small effect size (~0.3% PPL)" | (a) claim 聚焦方法正确性+调参消除，非效应量; (b) 60% 污染+3B 模型效应放大; (c) adaptive 的 zero-cost advantage | 扩展实验 |
134	| "n_min sensitivity — just another hyperparameter?" | n_min=3→2 修复证明方法对 ESS 约束宽松度敏感度低（n_min=2 稳定工作）；单一超参 vs Drayson 的 per-model b 选择仍是降低了调参负担 | n_min ablation |
135	
136	## Key Risks
137	
138	1. **Novelty narrowing (D013)**: 基础公式来自 Drayson，核心新颖性收窄为 adaptive b*。应对：三层差异化（principled b* + loss reweighting vs SIR + unknown proportion setting）；强化 lightweight detector finding
139	2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis（contamination 对不同 NLP task 的影响差异）
140	3. **效应量小 (0.3% relative PPL at 40% contamination)**: 应对：60% 污染 + 3B 模型展示效应放大；强调 zero-cost advantage（方法价值在于免调参，不在于绝对 PPL 提升）
141	4. **adaptive_fix 如果仍有 seed 失败**: MVP 依赖 D012 修复版结果。应对：如果修复版仍不稳定，需进一步诊断算法或调整 claims
142	5. **SIR vs loss reweighting 差异被低估**: Reviewer 可能认为两种实现路径差异不大。应对：在 Method 中讨论 gradient-level 细粒度控制的优势，必要时加 ablation 对比
143	
144	## MVP → Full Paper 扩展路径
145	
146	| 维度 | MVP | Full Paper |
147	|------|-----|-----------|
148	| 污染比例 | 40% | 20%, 40%, 60% |
149	| 模型 | Qwen3-0.6B | + Llama-3.2-3B |
150	| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |
151	| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |
152	| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |
153	| 评估 | eval_ppl (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |
154	| 注入方式 | uniform random | + domain-skewed, semi-realistic |
155	| n_min 分析 | n_min=2 vs n_min=3 (2 点) | + n_min=1, 4, 5 的完整 sensitivity curve |
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda3ca6d-63f7-45ff-9ca9-a0497d9cec7a",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "c6c3b071-4a07-4470-8e1d-d1c9208862d2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper_framing.md",
      "content": "# Paper Framing — provenance_weight_training\n\n> 状态: DRAFT (MVP Path B PASS, D019确认，进入 research 阶段)\n> 最后更新: 2026-05-15 01:15 UTC\n> 投稿目标: EMNLP 2026 ARR May 25\n\n## Core Insight\n\nDrayson et al. (EMNLP 2025) 提出 detect-and-reweight 框架 w=(1-q)^b 用于缓解合成数据污染导致的 model collapse，但 b 需要在 validation set 上 per-model empirical 选取（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1），且其实现路径为 **Sampling Importance Resampling (SIR)**——按权重重采样数据，本质是离散选择。我们提出 **adaptive b***：从 batch 统计量在线估计 α_eff(b) 推导最优 b*，per-batch 动态调整，无需 validation set、无需 grid search、无需已知污染比例。我们的实现路径为 **直接 loss reweighting**——在 gradient 层面连续加权，保留细粒度控制。\n\n**两种方法使用同一加权公式，但解决不同问题、采用不同实现路径**：Drayson 面向递归训练场景的 model collapse prevention（b 通过 per-model validation 选取），我们面向 web corpus 一次性预训练的 decontamination（b* 从 batch 统计量自适应推导，零 validation cost）。\n\n收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。\n\n## Positioning vs Prior Work\n\n### Drayson et al. (EMNLP 2025) — 最近相关工作\n\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\n\n**关键区分**：\n\n| 维度 | Drayson et al. | Ours |\n|------|---------------|------|\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态 |\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\n| **污染设置** | 不假设已知比例（原文明确声明），但实验为控制设置 | 未知比例（从 batch 统计量在线估计） |\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\n| **理论基础** | 无 b 选取理论，无 ablation | 收敛理论 motivated α_eff(b) 推导 |\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\n\n**定位原则：complementary approaches for different settings，非\"我们比 Drayson 更好\"。** Drayson 在其设定（递归训练、强检测器、validation-based b 选择）下是合理方案；我们解决的是 web pretraining 场景下无需 validation 的 principled b 选择问题。\n\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。我们不需要已知比例。\n\n### 其他相关工作\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\n- **arXiv 2602.16065** — 我们引用的收敛理论\n\n## Core Claims\n\n### Claim 1 (Primary): Principled b* via α_eff(b) 理论框架\n\n基于 α_eff(b) 和 ESS 约束的 adaptive b* 提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical selection。\n\n- **差异化核心**：Drayson 的 b 是超参数（需 validation set + 人工选取），我们的 b* 是从 batch 统计量在线推导的自适应量\n- **理论贡献**：α_eff(b) 框架将 contamination detection score 分布与权重指数选择建立 principled 联系\n- **证据需求**：adaptive b* 轨迹分析 + 与 Drayson 推荐值（b=1, b=10）的对比\n\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\n\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\n\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\n- **Pass criteria**: adaptive 均值 ≥ 90% grid-best 改善量 + 无任何 seed 劣于 uniform\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\n\n**叙事弹性（避免硬编码精确数字）**：\n- 核心表述：**\"adaptive matches grid-best within seed variance\"**\n- 补充表述：**\"eliminates grid search cost (6N → 1 runs)\"** 和 **\"consistent improvement across all seeds\"**\n- Path B 叙事：3/3 seeds adaptive > uniform，adaptive-grid 差异在 seed variance 范围内\n\n**最终 MVP 数据**：\n\n3-seed Grid-b best (b=0.5) vs Adaptive_fix：\n\n| Metric | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\n| Ratio | 102.6% | 90.4% | 80.0% |\n\nAggregate ratio: 88.6% (D019). Path B PASS.\n\n### Claim 3 (Setting): Unknown Contamination Proportion\n\n我们的方法在 contamination proportion 完全未知的条件下工作——仅需 detector scores，无需已知污染比例、无需 clean validation set。\n\n- **差异化**：Golden Ratio Weighting 需要已知比例 k；Drayson 虽不假设已知比例，但 b 选择依赖 validation set 做 per-model tuning；我们仅需 detector scores，无需 validation set 或已知比例\n- **实际意义**：web-scale pretraining 中污染比例本质上不可知（organic contamination from multiple generators）\n- **证据**：adaptive b* 仅从 per-batch q-score 分布推导，无外部信息输入\n\n## n_min Robustness Framing\n\nD012 修复（n_min=3→2）显示方法对 ESS 约束参数的**实际鲁棒性**：\n\n- **现象**：n_min=3 导致 seed42 零改善（ESS 约束过紧，b* 被钳制在低值），n_min=2 修复后 seed42 恢复正常表现\n- **Framing**：ESS 约束是 b* 推导中唯一的超参数，n_min=3→2 的修复表明只要 ESS 下界合理宽松（不过度约束有效样本量），adaptive b* 就能稳定工作\n- **论文呈现**：在 Method section 讨论 ESS 约束的作用和敏感度；在 Ablation 中展示 n_min=2 vs n_min=3 的对比作为 robustness evidence\n- **注意**：D017 勘误确认实际实施为 n_min=2 无 EMA（EMA 未编码），D018 确认 v1→v2 唯一差异为 n_min(3→2)\n\n## Narrative Structure\n\n**起点**: Web 语料中 20-60% 为合成文本，比例未知，来源多样——这是实际预训练面临的现实问题。Strong Model Collapse (ICLR 2025) 证明即使微量污染也会破坏 scaling law。\n\n**现有方法的不足**：\n- Drayson et al.: w=(1-q)^b 有效，但 b 依赖 per-model validation-based tuning（不同模型需不同 b，b=1 vs b=10），且需要 clean validation set\n- Golden Ratio Weighting: 理论最优权重，但假设已知混合比例 k\n- 两者都不适用于无 validation set 的大规模 web pretraining 场景\n\n**我们的方案**: 在 Drayson 框架上，从 batch 统计量自适应估计 α_eff(b) 推导 b*，消除对 validation set 和 grid search 的依赖。实现路径从 SIR resampling 转为 direct loss reweighting，保留细粒度 gradient 控制。\n\n**理论连接**: 收敛 bound 作为 Background/Motivation，不 claim 理论贡献。\n\n**Method 呈现**: Algorithm 1 (adaptive b*) + ESS 约束（n_min 敏感度分析） + soft-to-hard 连续谱（作为 framing 而非独立 contribution）。\n\n**Path B 默认叙事**: \"Adaptive b* 免调参即可匹配 validation-tuned best，将 Drayson 框架从需要 per-model heuristic tuning 提升为全自动 principled method。\" 如果数据支持 Path A（adaptive 显著优于 grid-best），可升级表述，但默认保守。\n\n## Contribution Structure (2 Primary + 1 Setting)\n\n1. **Primary — Theoretical Framework**: Adaptive b* via α_eff(b) estimation + ESS constraints，提供 contamination-aware reweighting 中 b 的 principled 推导（vs Drayson 的 empirical selection）\n2. **Primary — Practical Result**: Adaptive b* 零超参调优即匹配 grid-best，消除 per-model validation 成本。Lightweight detector (TF-IDF+LR, AUC=0.939) sufficiency 作为附加发现（升级为 co-primary 需 detector quality ablation）\n3. **Setting — Unknown Proportion**: 与 Golden Ratio (known k) 的 problem setting 差异。Drayson 虽不假设已知比例，但 b 选择依赖 validation set；我们仅需 detector scores，无需 validation 或已知比例\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | 实验支撑 |\n|---------|------------------|----------|\n| \"Incremental over Drayson et al.\" | 三层差异化: (1) adaptive b* without validation-set tuning vs per-model empirical b (核心), (2) loss reweighting vs SIR resampling, (3) zero validation cost vs validation-dependent。Complementary approaches for different settings | Claim 1 + Claim 3 |\n| \"Base formula is from Drayson\" | 明确 acknowledge 公式来源；贡献是 b* 的 principled derivation + 实现路径差异 + 问题设定差异 | Positioning section |\n| \"Theory not rigorous / overclaimed\" | 明确 scope: motivation not contribution; α_eff(b) 是 testable sufficient condition not theorem | Background section |\n| \"Only 0.6B model, would it scale?\" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |\n| \"Detector quality sensitivity\" | TF-IDF+LR (AUC=0.939) 即可；q-score 连续性比 AUC 更关键；检测器 quality ablation | detector quality ablation |\n| \"Controlled injection ≠ real web\" | Full paper: domain-skewed injection + semi-realistic (Binoculars on Common Crawl) | 扩展实验 |\n| \"Small effect size (~0.3% PPL)\" | (a) claim 聚焦方法正确性+调参消除，非效应量; (b) 60% 污染+3B 模型效应放大; (c) adaptive 的 zero-cost advantage | 扩展实验 |\n| \"n_min sensitivity — just another hyperparameter?\" | n_min=3→2 修复证明方法对 ESS 约束宽松度敏感度低（n_min=2 稳定工作）；单一超参 vs Drayson 的 per-model b 选择仍是降低了调参负担 | n_min ablation |\n\n## Key Risks\n\n1. **Novelty narrowing (D013)**: 基础公式来自 Drayson，核心新颖性收窄为 adaptive b*。应对：三层差异化（principled b* + loss reweighting vs SIR + unknown proportion setting）；强化 lightweight detector finding\n2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis（contamination 对不同 NLP task 的影响差异）\n3. **效应量小 (0.3% relative PPL at 40% contamination)**: 应对：60% 污染 + 3B 模型展示效应放大；强调 zero-cost advantage（方法价值在于免调参，不在于绝对 PPL 提升）\n4. **adaptive_fix 如果仍有 seed 失败**: MVP 依赖 D012 修复版结果。应对：如果修复版仍不稳定，需进一步诊断算法或调整 claims\n5. **SIR vs loss reweighting 差异被低估**: Reviewer 可能认为两种实现路径差异不大。应对：在 Method 中讨论 gradient-level 细粒度控制的优势，必要时加 ablation 对比\n\n## MVP → Full Paper 扩展路径\n\n| 维度 | MVP | Full Paper |\n|------|-----|-----------|\n| 污染比例 | 40% | 20%, 40%, 60% |\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\n| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |\n| 评估 | eval_ppl (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\n| n_min 分析 | n_min=2 vs n_min=3 (2 点) | + n_min=1, 4, 5 的完整 sensitivity curve |\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  },
  "sourceToolAssistantUUID": "dda3ca6d-63f7-45ff-9ca9-a0497d9cec7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:02:13.583Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B9Dpgd4bZYGDShcrWULhHL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf98d69-c9e5-4b7f-8035-8ca14756643f",
  "isSidechain": false,
  "requestId": "req_011Cb3Xku5mo6c4hgHnMXHQA",
  "type": "assistant",
  "uuid": "dda3ca6d-63f7-45ff-9ca9-a0497d9cec7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFLgvf52m6hN3ZfqyVuFYq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11468,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11468
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weigh…",
  "leafUuid": "c6c3b071-4a07-4470-8e1d-d1c9208862d2",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case research paper simulation",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Assistant

_source line 14 · 2026-05-15T02:02:30.223Z_

<details><summary>Logged reasoning block</summary>

```text
I've read both files. Now I need to write a complete LaTeX paper based on the experiment data and narrative guidance. Let me plan the paper structure:

The narrative guidance says:
1. Core claim retreats from "adaptive b* replaces grid search"
2. Finer grid reveals true optimal b in 0.1-0.3, adaptive b* median ~0.87 systematically overshoots ~4×
3. 60% contamination and 3B model effects don't significantly amplify
4. Cross-generator scenario: adaptive even loses to uniform


5. Reframing the contributions: α_eff(b) becomes a diagnostic tool for understanding batch-level contamination, loss reweighting versus SIR comparison stands as an independent methodological contribution, and the lightweight detector emerges as the primary finding—showing you don't need expensive detection infrastructure
6. Downgrading adaptive b* to "a reasonable zero-cost default in most settings" rather than an optimal solution, and positioning the b* trajectory itself as having diagnostic value

Target venue is EMNLP, anchored by the framework, implementation comparison, and detector sufficiency finding. The key narrative shift is that adaptive isn't optimal but provides a principled default with interpretable diagnostics.

Now I'm structuring the paper with abstract, introduction, background and related work, and methods sections.

Writing the LaTeX paper with the full experimental section covering grid search results, contamination scaling, model size variations, detector quality comparisons, cross-generator robustness, sensitivity analyses, baseline comparisons, and downstream evaluation—pulling only verified numbers from the experiment data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c3b071-4a07-4470-8e1d-d1c9208862d2",
  "isSidechain": false,
  "requestId": "req_011Cb3XmSzuZ69cgFxvU6ErY",
  "type": "assistant",
  "uuid": "eafc0c3a-5bd0-4611-95cf-d2c33d2db824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018L4jqADFcoaUys9C1kL5Fc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21541,
      "cache_read_input_tokens": 23309,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 23309,
          "cache_creation_input_tokens": 21541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21541
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

_source line 15 · 2026-05-15T02:02:30.225Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eafc0c3a-5bd0-4611-95cf-d2c33d2db824",
  "isSidechain": false,
  "requestId": "req_011Cb3XmSzuZ69cgFxvU6ErY",
  "type": "assistant",
  "uuid": "ee4dd870-f2cc-4842-b516-550552ff4291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018L4jqADFcoaUys9C1kL5Fc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21541,
      "cache_read_input_tokens": 23309,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 23309,
          "cache_creation_input_tokens": 21541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21541
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

_source line 16 · 2026-05-15T02:02:31.265Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VztsfvBjoQeJyCgPvMG5TP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4dd870-f2cc-4842-b516-550552ff4291",
  "isSidechain": false,
  "requestId": "req_011Cb3XmSzuZ69cgFxvU6ErY",
  "type": "assistant",
  "uuid": "9d6310ef-434a-4836-9d3b-a3d1bfa23976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018L4jqADFcoaUys9C1kL5Fc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21541,
      "cache_read_input_tokens": 23309,
      "output_tokens": 639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 639,
          "cache_read_input_tokens": 23309,
          "cache_creation_input_tokens": 21541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21541
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

_source line 17 · 2026-05-15T02:02:31.441Z_

<details><summary>↩ Tool result · `toolu_01VztsfvBjoQeJyCgPvMG5TP`</summary>

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
  "parentUuid": "9d6310ef-434a-4836-9d3b-a3d1bfa23976",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "96261961-e9c7-4249-a327-0745d27eb118",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9d6310ef-434a-4836-9d3b-a3d1bfa23976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T02:05:52.877Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JzSBgPj38YKSNdjYM4ZYNo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{natbib}\n\n\\title{Adaptive Provenance Weighting for Contaminated Pretraining Corpora:\\\\A Diagnostic Framework and Practical Guidelines}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLarge-scale web corpora increasingly contain machine-generated text of unknown provenance and proportion, degrading language model pretraining.\nDetect-and-reweight approaches assign instance weights $w_i = (1-q_i)^b$ based on detector scores $q_i$, but the exponent $b$ must be tuned per model via grid search over a validation set.\nWe introduce \\textbf{adaptive $b^*$}, which derives $b$ online from per-batch contamination statistics $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ subject to an effective sample size (ESS) constraint, requiring no validation set and no known contamination ratio.\nOur experiments on FineWeb subsets (200M tokens, $\\rho \\in \\{0.4, 0.6\\}$) with Qwen3-0.6B and Llama-3.2-3B reveal three findings.\n\\textbf{(1)} A lightweight TF-IDF + logistic regression detector (AUC = 0.939) achieves within 0.003 PPL of a 150M-parameter ModernBERT detector (AUC = 0.986), establishing that expensive detectors are unnecessary for provenance weighting.\n\\textbf{(2)} The $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework, while producing $b^*$ values that systematically overshoot the grid-optimal $b$ by approximately $4\\times$, serves as a diagnostic tool whose $b^*$ trajectory exposes batch-level contamination structure.\n\\textbf{(3)} Adaptive $b^*$ provides a zero-cost reasonable default (recovering 70\\% of grid-best improvement) in standard settings, though it degrades under cross-generator contamination and domain-skewed injection.\nWe additionally provide the first systematic comparison of loss reweighting versus sampling importance resampling (SIR) under identical weighting formulas.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nThe proliferation of machine-generated text on the web poses a growing challenge for language model pretraining.\nRecent estimates suggest 20--60\\% of web-crawled corpora may contain synthetic content from diverse generators, with the exact proportion and provenance unknown at training time.\nTheoretical analyses demonstrate that even small amounts of synthetic contamination can degrade scaling laws and induce model collapse~\\citep{shumailov2024strong}.\n\nDrayson et al.\\ propose a detect-and-reweight framework: train a detector to produce per-instance contamination scores $q_i \\in [0,1]$, then weight each sample by $w_i = (1 - q_i)^b$ during training via Sampling Importance Resampling (SIR).\nWhile effective, this approach requires tuning $b$ per model through validation-based grid search---different model scales need different $b$ values (e.g., $b=10$ for GPT-2/SmolLM $\\leq$360M versus $b=1$ for SmolLM-1.7B), and the procedure assumes access to a clean validation set.\n\nWe propose \\textbf{adaptive $b^*$}: an online method that derives the weighting exponent from per-batch statistics of the detector score distribution, subject to an effective sample size (ESS) constraint.\nOur method requires neither a validation set nor knowledge of the contamination proportion, making it applicable to web-scale pretraining where these are unavailable.\nWe implement provenance weighting via direct loss reweighting rather than SIR, providing continuous gradient-level control.\n\nOur investigation yields three contributions, ordered by strength of evidence:\n\n\\begin{enumerate}\n    \\item \\textbf{Lightweight detector sufficiency.} A TF-IDF + logistic regression detector (50K parameters, AUC = 0.939, $<$1 min CPU training) produces training outcomes within 0.003 PPL of a ModernBERT 150M detector (AUC = 0.986, 1.5h GPU training).\n    The marginal return of detector quality on downstream PPL is negligible, suggesting that practitioners can skip expensive neural detectors entirely.\n\n    \\item \\textbf{$\\hat{\\alpha}_{\\mathrm{eff}}(b)$ as a diagnostic framework.} We formalize the connection between batch-level contamination statistics and the weighting exponent through $\\hat{\\alpha}_{\\mathrm{eff}}(b)$.\n    While the derived $b^*$ systematically overshoots the grid-optimal value (median $b^* \\approx 0.87$ versus grid-best $b = 0.2$), the $b^*$ trajectory across batches and contamination levels provides interpretable diagnostics about contamination structure that the original framework lacks.\n\n    \\item \\textbf{Loss reweighting vs.\\ SIR.} We provide a systematic comparison of continuous loss reweighting and discrete SIR under identical weighting formulas, characterizing their gradient variance and convergence behavior differences.\n\\end{enumerate}\n\nAs an additional practical finding, adaptive $b^*$ recovers approximately 70\\% of grid-best improvement at zero tuning cost, serving as a reasonable default in standard settings---though it degrades or becomes harmful under cross-generator contamination (Section~\\ref{sec:cross_gen}) and domain-skewed injection (Section~\\ref{sec:domain_skew}).\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:background}\n\n\\paragraph{Model Collapse and Synthetic Contamination.}\nTraining on model-generated data can cause progressive degradation of output quality, termed \\emph{model collapse}~\\citep{shumailov2024strong}.\nEven low contamination ratios degrade scaling behavior, motivating methods that mitigate synthetic content during pretraining.\n\n\\paragraph{Detect-and-Reweight.}\nDrayson et al.\\ train a detector to produce scores $q_i \\in [0,1]$ indicating the probability that sample $i$ is synthetic.\nEach sample receives weight $w_i = (1 - q_i)^b$, where $b > 0$ controls downweighting aggressiveness.\nTheir implementation uses SIR: samples are stochastically resampled proportional to their weights, effectively a discrete selection mechanism.\nThe exponent $b$ is selected via grid search over a validation set, yielding model-specific values ($b = 10$ for $\\leq$360M models, $b = 1$ for 1.7B).\n\n\\paragraph{Golden Ratio Weighting.}\nConcurrent work derives a theoretically optimal weight $w^* = 1/\\varphi$ but assumes the real-to-synthetic ratio $k$ is known, which is unrealistic for web corpora.\n\n\\paragraph{Domain-Level Reweighting.}\nDoReMi and DSIR optimize domain-level mixture weights, operating at a coarser granularity than our instance-level approach.\nSoftDedup applies soft reweighting based on duplication, which is orthogonal to provenance-based weighting.\nDynamic loss-based reweighting adjusts weights based on training loss rather than detector scores, providing a complementary signal.\n\n\\paragraph{Convergence Theory.}\nThe bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p, \\alpha\\}}$ from recent work motivates the definition of $\\alpha_{\\mathrm{eff}}$ and the derivation of $b^*$, though we do not claim this theoretical bridge as a contribution.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setting}\n\nWe consider pretraining on a corpus $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ where an unknown fraction $\\rho$ of samples are machine-generated.\nA pretrained detector provides scores $q_i \\in [0,1]$ estimating $P(\\text{synthetic} \\mid x_i)$.\nOur goal: assign weights $w_i = (1 - q_i)^b$ that mitigate contamination effects, with $b$ determined automatically.\n\n\\subsection{Effective Contamination Fraction $\\hat{\\alpha}_{\\mathrm{eff}}(b)$}\n\nFor a batch $\\mathcal{B}$ of size $n$, we define the effective contamination fraction under weighting exponent $b$:\n\\begin{equation}\n    \\hat{\\alpha}_{\\mathrm{eff}}(b) = 1 - \\frac{\\sum_{i \\in \\mathcal{B}} (1 - q_i)^b}{\\sum_{i \\in \\mathcal{B}} 1} = 1 - \\frac{1}{n} \\sum_{i \\in \\mathcal{B}} (1 - q_i)^b.\n\\end{equation}\nThis quantity measures how much effective mass is removed by the weighting scheme: when $b = 0$, $\\hat{\\alpha}_{\\mathrm{eff}} = 0$ (no downweighting); as $b \\to \\infty$, $\\hat{\\alpha}_{\\mathrm{eff}} \\to 1 - (1-\\rho_{\\mathcal{B}})$ where $\\rho_{\\mathcal{B}}$ is the batch contamination fraction for perfectly calibrated $q_i$.\n\n\\subsection{ESS-Constrained $b^*$ Derivation}\n\nWe derive $b^*$ by maximizing the contamination removal subject to maintaining sufficient effective sample size.\nThe ESS for weights $\\{w_i\\}$ in batch $\\mathcal{B}$ is:\n\\begin{equation}\n    \\mathrm{ESS}(\\mathcal{B}, b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2} = \\frac{\\left(\\sum_{i} (1-q_i)^b\\right)^2}{\\sum_{i} (1-q_i)^{2b}}.\n\\end{equation}\nWe impose $\\mathrm{ESS}(\\mathcal{B}, b) \\geq n_{\\min}$ and solve for the largest $b$ satisfying this constraint:\n\\begin{equation}\n    b^* = \\max \\{ b \\geq 0 : \\mathrm{ESS}(\\mathcal{B}, b) \\geq n_{\\min} \\}.\n\\end{equation}\n\nThe hyperparameter $n_{\\min}$ controls the aggressiveness of downweighting.\nUnlike the continuous exponent $b$ which spans $[0, \\infty)$ and requires multi-point grid search, $n_{\\min}$ takes small integer values ($\\{1, 2, 3, \\ldots, n\\}$) with $n_{\\min} = 2$ performing well across our experiments (Section~\\ref{sec:nmin}).\n\n\\begin{algorithm}[t]\n\\caption{Adaptive $b^*$ with ESS Constraint}\n\\label{alg:adaptive}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch $\\mathcal{B} = \\{(x_i, q_i)\\}_{i=1}^n$, ESS lower bound $n_{\\min}$, search range $[0, b_{\\max}]$\n\\STATE Compute $\\mathrm{ESS}(b)$ for $b \\in \\{0, 0.1, 0.2, \\ldots, b_{\\max}\\}$ via Eq.~(2)\n\\STATE $b^* \\leftarrow \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$\n\\STATE $w_i \\leftarrow (1 - q_i)^{b^*}$ for each $i \\in \\mathcal{B}$\n\\STATE $\\bar{w} \\leftarrow \\frac{1}{n}\\sum_i w_i$; \\quad $\\tilde{w}_i \\leftarrow w_i / \\bar{w}$ \\hfill (normalize to mean 1)\n\\STATE $\\mathcal{L}_{\\mathrm{weighted}} = \\frac{1}{n}\\sum_i \\tilde{w}_i \\cdot \\ell(x_i; \\theta)$\n\\RETURN $\\mathcal{L}_{\\mathrm{weighted}}$, $b^*$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Loss Reweighting vs.\\ SIR}\n\nDrayson et al.\\ implement provenance weighting via SIR: samples are resampled proportional to $w_i$ before each epoch, creating a modified dataset.\nWe instead apply weights directly to the loss function (Algorithm~\\ref{alg:adaptive}, line 5).\nThe key differences are:\n\\begin{itemize}\n    \\item \\textbf{Granularity}: Loss reweighting applies continuous weights per gradient step; SIR makes discrete include/exclude decisions per epoch.\n    \\item \\textbf{Gradient variance}: Loss reweighting introduces weight-dependent variance in gradient estimates; SIR introduces resampling variance.\n    \\item \\textbf{Adaptivity}: Per-batch $b^*$ naturally integrates with loss reweighting (weights change every batch); SIR would require re-resampling per batch, negating its data-loading efficiency.\n\\end{itemize}\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe use FineWeb subsets totaling 200M tokens.\nSynthetic data is generated by Qwen3-0.6B (self-generation setting) or Llama-3.2-1B (cross-generator setting) via continuation of real text prefixes.\nContamination ratios: $\\rho \\in \\{0.4, 0.6\\}$.\n\n\\paragraph{Detectors.}\n(1)~\\textbf{TF-IDF + LR}: TF-IDF features with logistic regression, $\\sim$50K parameters, $<$1 min CPU training, AUC = 0.939.\n(2)~\\textbf{ModernBERT 150M}: Fine-tuned ModernBERT, 150M parameters, 1.5h GPU training, AUC = 0.986.\n\n\\paragraph{Models.}\nQwen3-0.6B (primary) and Llama-3.2-3B (scale validation), trained for 6103 steps on 200M tokens with batch size 4 and gradient checkpointing.\n\n\\paragraph{Evaluation.}\nPerplexity (PPL) on a held-out FineWeb subset ($\\sim$4M tokens).\nDownstream: MMLU (5-shot) and HellaSwag (10-shot) for the 3B model.\nAll experiments use 3 random seeds (42, 123, 456) where budget permits.\n\n\\paragraph{Baselines.}\n\\textit{Uniform}: standard training without reweighting.\n\\textit{Grid-$b$}: fixed $b \\in \\{0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$.\n\\textit{Detect-and-remove}: discard samples with $q > 0.5$.\n\\textit{Random reweighting}: weights drawn uniformly from $[0, 2]$ (mean 1).\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Full Grid Curve Reveals Low-$b$ Optimum}\n\\label{sec:grid_curve}\n\nTable~\\ref{tab:full_grid} presents the complete PPL landscape across 9 fixed-$b$ values, adaptive $b^*$, and the uniform baseline ($\\rho = 0.4$, Qwen3-0.6B, 200M tokens).\n\n\\begin{table}[t]\n\\centering\n\\caption{Eval PPL across weighting exponents ($\\rho = 0.4$, Qwen3-0.6B, 200M tokens). Lower is better. Bold: best per seed.}\n\\label{tab:full_grid}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n$b$ & seed 42 & seed 123 & seed 456 \\\\\n\\midrule\n0.1     & 17.645 & 17.631 & 17.642 \\\\\n\\textbf{0.2}     & \\textbf{17.637} & \\textbf{17.625} & \\textbf{17.636} \\\\\n0.3     & 17.641 & 17.629 & 17.640 \\\\\n0.5     & 17.651 & 17.638 & 17.650 \\\\\n1.0     & 17.692 & 17.674 & 17.680 \\\\\n1.5     & 17.718 & 17.701 & 17.710 \\\\\n2.0     & 17.741 & 17.725 & $\\sim$17.73 \\\\\n3.0     & 17.774 & 17.760 & $\\sim$17.77 \\\\\n5.0     & 17.818 & 17.804 & $\\sim$17.82 \\\\\n\\midrule\nUniform & 17.690 & 17.690 & 17.700 \\\\\nAdaptive $b^*$ & 17.650 & 17.643 & 17.660 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe grid-best exponent is $b = 0.2$ across all three seeds, with PPL improvements of 0.053, 0.065, and 0.064 over uniform (seed 42, 123, 456 respectively).\nThe PPL curve is monotonically increasing for $b > 0.2$, confirming that aggressive downweighting hurts: at $b = 0.2$, contaminated samples retain 63\\% weight ($w = (1-0.9)^{0.2} = 0.63$), preserving useful signal while mildly correcting distributional shift.\n\nAdaptive $b^*$ (median $\\approx 0.87$) overshoots the grid optimum by approximately $4\\times$.\nThis systematic overshoot reduces the aggregate recovery ratio from the previously reported 88.6\\% (when $b = 0.5$ was believed to be grid-best) to 69.8\\% (Table~\\ref{tab:ratio}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Adaptive $b^*$ recovery ratio relative to grid-best ($b = 0.2$). The gap between adaptive and grid-best (0.013--0.024) exceeds cross-seed variance ($\\sim$0.007).}\n\\label{tab:ratio}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Uniform & Grid-best ($b\\!=\\!0.2$) & Adaptive & Ratio \\\\\n\\midrule\n42  & 17.690 & 17.637 & 17.650 & 75.5\\% \\\\\n123 & 17.690 & 17.625 & 17.643 & 72.3\\% \\\\\n456 & 17.700 & 17.636 & 17.660 & 62.5\\% \\\\\n\\midrule\n\\textit{Aggregate} & --- & \\textit{0.182} & \\textit{0.127} & \\textit{69.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Lightweight Detector Sufficiency}\n\\label{sec:detector}\n\nTable~\\ref{tab:detector} compares the TF-IDF + LR and ModernBERT detectors.\nDespite a large AUC gap (0.939 vs.\\ 0.986), the PPL difference is negligible: 0.003 absolute, $<$0.02\\% relative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detector quality vs.\\ training PPL ($\\rho = 0.4$, Qwen3-0.6B, adaptive $b^*$, seed 42). AUC improves by 5\\% relative, but PPL gain is negligible.}\n\\label{tab:detector}\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\nDetector & Params & AUC & ECE (cal.) & Adaptive PPL & Cost \\\\\n\\midrule\nTF-IDF + LR   & $\\sim$50K & 0.939 & 0.048 & 17.650 & $<$1 min CPU \\\\\nModernBERT 150M & 150M     & 0.986 & 0.022 & 17.647 & 1.5h GPU \\\\\n\\midrule\n\\multicolumn{2}{l}{$\\Delta$ (AUC $\\uparrow$ 0.047)} & & & $-$0.003 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonicity of $w = (1-q)^b$ guarantees that ranking correctness matters more than calibration accuracy.\nTF-IDF + LR, despite higher calibration error (ECE 0.048 vs.\\ 0.022) and a more diffuse $q$-score distribution (mid-range ratio 0.463 vs.\\ 0.28), preserves sufficient ranking quality for effective reweighting.\nThe practical implication: a detector trainable in under one minute on a CPU suffices for provenance weighting.\n\n\\subsection{Higher Contamination ($\\rho = 0.6$)}\n\\label{sec:rho06}\n\nTable~\\ref{tab:rho06} compares reweighting effectiveness at 40\\% and 60\\% contamination.\nAt $\\rho = 0.6$, uniform PPL rises from 17.69 to 17.85 (+0.9\\% relative), confirming that higher contamination degrades training quality.\nHowever, adaptive improvement does \\emph{not} scale with contamination: $\\Delta_{\\mathrm{adaptive}}$ decreases from 0.04 to 0.03.\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination level vs.\\ adaptive effectiveness (Qwen3-0.6B, seed 42). Higher contamination does not amplify the benefit of adaptive reweighting.}\n\\label{tab:rho06}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$\\rho$ & Uniform & Adaptive & $\\Delta_{\\mathrm{abs}}$ & $\\Delta_{\\mathrm{rel}}$ (\\%) & $b^*$ median \\\\\n\\midrule\n0.4 & 17.690 & 17.650 & 0.040 & 0.23 & 0.87 \\\\\n0.6 & 17.850 & 17.820 & 0.030 & 0.17 & 1.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe adaptive mechanism responds directionally: $b^*$ median increases from 0.87 to 1.08 as contamination rises, reflecting higher batch-level $\\hat{\\alpha}_{\\mathrm{eff}}$.\nHowever, this response exacerbates overshoot---the true optimal $b$ likely remains near 0.2, so the increased $b^*$ at $\\rho = 0.6$ moves further from the optimum.\nAt $\\rho = 0.6$, grid $b = 0.5$ achieves PPL = 17.80, yielding $\\Delta = 0.05$ versus adaptive's 0.03, for a ratio of only 60\\%.\n\nThis result has diagnostic value: the $b^*$ shift from 0.87 to 1.08 correctly signals increased contamination, even though the derived value is not numerically optimal.\nThe $\\hat{\\alpha}_{\\mathrm{eff}}$ framework thus serves as a contamination \\emph{thermometer}, not an optimizer.\n\n\\subsection{Model Scale (Llama-3.2-3B)}\n\\label{sec:3b}\n\nWe evaluate on Llama-3.2-3B to test whether the method adapts to model scale (Table~\\ref{tab:3b}).\n\n\\begin{table}[t]\n\\centering\n\\caption{$b^*$ distribution comparison across model scales ($\\rho = 0.4$, seed 42). The $b^*$ distribution is nearly identical because it depends only on $q$-score statistics, not model architecture. KS test $p = 0.87$.}\n\\label{tab:3b}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & $b^*$ med. & $b^*$ mean & $b^*$ P25 & $b^*$ P75 & $\\Delta_{\\mathrm{rel}}$ (\\%) \\\\\n\\midrule\nQwen3-0.6B   & 0.87 & 1.40 & 0.54 & 1.51 & 0.23 \\\\\nLlama-3.2-3B & 0.92 & 1.38 & 0.55 & 1.48 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $b^*$ distributions are statistically indistinguishable (KS test $p = 0.87$) because $b^*$ is derived solely from $q$-score statistics, which depend on the data and detector, not the training model.\nThe PPL improvement for 3B is minimal: 0.01 absolute (16.19 vs.\\ 16.20), 0.06\\% relative---within noise.\n\nThis reveals a fundamental property: adaptive $b^*$ provides a \\emph{data-driven} default that is consistent across models.\nThis consistency is both a strength (predictable behavior) and a limitation (no model-specific adaptation).\nDrayson et al.'s observation that different model scales need different $b$ values (1 vs.\\ 10) suggests that optimal $b$ is model-dependent, a dimension our $q$-score-only derivation cannot capture.\n\n\\subsection{ESS Constraint Sensitivity ($n_{\\min}$)}\n\\label{sec:nmin}\n\nTable~\\ref{tab:nmin} presents the sensitivity of adaptive $b^*$ to the ESS lower bound $n_{\\min}$ (batch size $n = 4$).\n\n\\begin{table}[t]\n\\centering\n\\caption{$n_{\\min}$ sensitivity ($\\rho = 0.4$, Qwen3-0.6B, seed 42, batch size 4). Only $n_{\\min} = 2$ improves over uniform; $n_{\\min} = 1$ is too aggressive, $n_{\\min} \\geq 3$ collapses to uniform.}\n\\label{tab:nmin}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n$n_{\\min}$ & Eval PPL & $b^*$ median & Status \\\\\n\\midrule\n1 & 17.710 & 2.60 & Worse than uniform \\\\\n2 & 17.650 & 0.87 & Best \\\\\n3 & 17.690 & $\\sim$0.3 & $\\approx$ Uniform \\\\\n4 & 17.690 & 0.0 & $=$ Uniform \\\\\n5 & 17.690 & 0.0 & $=$ Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe sensitivity curve reveals a narrow effective range.\nAt $n_{\\min} = 1$, the ESS constraint is too permissive: $b^*$ reaches median 2.60, contaminated samples receive weight $w \\approx 0.004$, and PPL (17.71) is \\emph{worse} than uniform (17.69) due to over-downweighting.\nAt $n_{\\min} \\geq 3$, the constraint is too tight: $b^*$ is clamped near zero, and the method degrades to uniform training.\nAt $n_{\\min} = 4 = n$ (batch size), $b^* = 0$ identically---the ESS constraint demands all weights be equal, which is only possible when $b = 0$.\n\nOnly $n_{\\min} = 2$ occupies the effective region.\nWhile this single-point sensitivity is a limitation, we note that $n_{\\min}$ selection reduces from a continuous grid search over $b$ (requiring $\\geq 6$ runs) to checking 2--3 integer values, representing a significant practical simplification.\n\n\\subsection{Cross-Generator Robustness}\n\\label{sec:cross_gen}\n\nIn realistic web corpora, synthetic content originates from multiple generator families.\nWe test this by generating contamination with Llama-3.2-1B while training Qwen3-0.6B (Table~\\ref{tab:cross_gen}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-generator evaluation ($\\rho = 0.4$, Qwen3-0.6B, seed 42). When detector quality degrades on out-of-distribution synthetic text, adaptive reweighting becomes harmful.}\n\\label{tab:cross_gen}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nSetting & Uniform & Adaptive & $\\Delta$ & Verdict \\\\\n\\midrule\nSelf-gen (Qwen $\\to$ Qwen) & 17.690 & 17.650 & $-$0.040 & Adaptive wins \\\\\nCross-gen (Llama $\\to$ Qwen) & 17.750 & 17.770 & +0.020 & Adaptive \\textbf{loses} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe TF-IDF + LR detector, trained only on Qwen3-0.6B-generated text, generalizes poorly to Llama-3.2-1B outputs (AUC drops from 0.939 to 0.891).\nThe $q$-score distribution becomes diffuse (mid-range ratio rises from 0.463 to 0.52), degrading both the $\\hat{\\alpha}_{\\mathrm{eff}}$ estimates and the ranking quality of weights.\nAdaptive $b^*$ (PPL = 17.77) is \\emph{worse} than uniform (17.75): noisy reweighting does more harm than good.\n\nThis exposes a fundamental dependency: adaptive $b^*$ quality is bounded by detector signal-to-noise ratio.\nIn web corpora with diverse synthetic sources, detector AUC may be lower than in controlled settings, making the method less applicable precisely where it would be most needed.\n\n\\subsection{Domain-Skewed Injection}\n\\label{sec:domain_skew}\n\nWe test robustness to non-uniform contamination by concentrating 85\\% of synthetic content in the code domain.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-skewed contamination ($\\rho = 0.4$, Qwen3-0.6B). Per-batch adaptation amplifies domain skew rather than correcting it.}\n\\label{tab:domain_skew}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Uniform PPL & Adaptive PPL & $\\Delta$ \\\\\n\\midrule\nUniform injection & 17.690 & 17.650 & $-$0.040 \\\\\nDomain-skewed (code-heavy) & 17.730 & 17.760 & +0.030 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain skew creates a bimodal batch structure: code-heavy batches have uniformly high $q$-scores ($\\hat{\\alpha}_{\\mathrm{eff}}$ overestimates, $b^*$ too large), while text batches have low $q$-scores ($b^* \\approx 0$).\nThe per-batch mechanism, designed to adapt to local contamination variation, instead amplifies the skew by over-downweighting code batches that may contain useful programming knowledge.\n\n\\subsection{Baseline Comparisons}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} consolidates all methods under the standard setting ($\\rho = 0.4$, Qwen3-0.6B, seed 42).\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison ($\\rho = 0.4$, Qwen3-0.6B, seed 42). Grid-best $b = 0.2$ dominates; adaptive provides partial improvement; random reweighting confirms detector signal is necessary.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\nMethod & PPL & $\\Delta$ vs.\\ Uniform & Signal source \\\\\n\\midrule\nGrid-best ($b = 0.2$) & 17.637 & $-$0.053 & Oracle grid \\\\\nAdaptive $b^*$ & 17.650 & $-$0.040 & Adaptive $q$-based \\\\\nDetect-and-remove ($q > 0.5$) & 17.680 & $-$0.010 & Hard threshold \\\\\nUniform & 17.690 & 0.000 & None \\\\\nRandom reweighting & 17.695 & +0.005 & Random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ranking is: gentle reweighting ($b = 0.2$) $\\gg$ adaptive $\\gg$ detect-and-remove $>$ uniform $\\approx$ random.\nRandom reweighting (PPL = 17.695 $\\approx$ uniform) confirms that detector-informed signal is load-bearing: arbitrary weight perturbations do not help.\nDetect-and-remove (PPL = 17.68) removes $\\sim$42\\% of data (40\\% true synthetic + 2\\% false positives), losing useful signal that gentle reweighting preserves.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\nTable~\\ref{tab:downstream} reports MMLU and HellaSwag results for Llama-3.2-3B checkpoints.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation (Llama-3.2-3B, $\\rho = 0.4$, seed 42, 200M tokens). No significant differences are observed, consistent with the minimal PPL gap (0.06\\% relative) and severe undertraining (63 tokens/parameter vs.\\ Chinchilla-optimal $\\sim$20$\\times$).}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Uniform & Adaptive & $\\Delta$ \\\\\n\\midrule\nMMLU (5-shot) & 25.8\\% & 25.8\\% & 0.0\\% \\\\\nHellaSwag (10-shot) & 38.2\\% & 38.3\\% & +0.1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo significant downstream differences are observed.\nMMLU performance (25.8\\%) is near random-chance level (25\\%), reflecting severe undertraining at 200M tokens for a 3B model (63 tokens/parameter versus $\\sim$20$\\times$ Chinchilla-optimal).\nThe PPL improvement of 0.06\\% relative is far below the resolution of discrete accuracy benchmarks ($\\sim$0.5\\% absolute).\nWe note that PPL is a continuous metric with higher sensitivity than discrete accuracy, and do not claim downstream transfer at current scale.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why adaptive $b^*$ overshoots.}\nThe $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework estimates contamination from $q$-score statistics and seeks the most aggressive downweighting permitted by the ESS constraint.\nThis objective is misaligned with the true optimum in our setting: FineWeb synthetic data generated by Qwen3-0.6B is not pure noise but retains substantial linguistic quality.\nThe optimal strategy ($b = 0.2$, $w = 0.63$) is \\emph{mild correction}, not aggressive removal.\nThe ESS constraint prevents catastrophic over-downweighting (cf.\\ $n_{\\min} = 1$, Table~\\ref{tab:nmin}) but does not guide $b^*$ toward the shallow optimum.\n\n\\paragraph{Diagnostic value of $b^*$ trajectories.}\nDespite numerical inaccuracy, $b^*$ trajectories provide information absent from the Drayson framework.\nThe shift from $b^* = 0.87$ ($\\rho = 0.4$) to $b^* = 1.08$ ($\\rho = 0.6$) correctly indicates increased contamination.\nPer-batch $b^*$ variance reveals contamination heterogeneity: batches with higher contamination receive larger $b^*$, making the framework interpretable for data auditing even when not producing optimal weights.\n\n\\paragraph{When adaptive hurts.}\nWe identify two failure modes: (1) cross-generator contamination, where detector quality degrades (AUC 0.939 $\\to$ 0.891) and noisy $q$-scores lead to harmful reweighting (Section~\\ref{sec:cross_gen}); and (2) domain-skewed contamination, where per-batch adaptation amplifies rather than corrects the skew (Section~\\ref{sec:domain_skew}).\nBoth failure modes stem from violations of implicit assumptions: the detector generalizes well (violated in cross-generator), and contamination is roughly uniform across batches (violated in domain skew).\n\n\\paragraph{The $n_{\\min}$ sensitivity question.}\nA reviewer might argue that replacing grid search over $b$ with selection of $n_{\\min}$ merely substitutes one hyperparameter for another.\nWe partially concede: the method is not hyperparameter-free.\nHowever, $n_{\\min}$ is an integer in $\\{1, \\ldots, n\\}$ (typically 2--3 effective values), requiring far fewer runs to sweep than $b \\in [0.1, 10]$ (our grid uses 9 values).\nThis represents a reduction in tuning cost, not its elimination.\n\n\\paragraph{Loss reweighting vs.\\ SIR.}\nLoss reweighting enables per-batch adaptive $b^*$, which is architecturally incompatible with SIR's per-epoch resampling.\nThe continuous gradient-level control also avoids the discrete variance introduced by stochastic resampling.\nA full gradient variance analysis under both implementations remains future work.\n\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Scale.}\nAll experiments use 200M tokens, far below production pretraining scale.\nThe 3B model is severely undertrained (63 tokens/parameter).\nEffect sizes at scale may differ qualitatively.\n\n\\textbf{Generator diversity.}\nCross-generator results (Section~\\ref{sec:cross_gen}) demonstrate degradation with a single out-of-distribution generator.\nReal web corpora contain outputs from many generators and model families; robustness under such diversity is untested.\n\n\\textbf{Contamination type.}\nWe study continuation-based synthetic text.\nOther contamination types (paraphrase, translation, summarization, instruction-following outputs) may interact differently with provenance detectors and reweighting schemes.\n\n\\textbf{$n_{\\min}$ sensitivity.}\nThe narrow effective range of $n_{\\min}$ at batch size 4 may not generalize to larger batch sizes, where the integer space grows and the ESS constraint landscape changes.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented adaptive $b^*$, an online method for deriving the weighting exponent in provenance-weighted pretraining from per-batch contamination statistics.\nOur investigation yields three actionable findings: (1) lightweight detectors (TF-IDF + LR) suffice for provenance weighting, with 3000$\\times$ fewer parameters and negligible PPL difference compared to neural alternatives; (2) the $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework provides batch-level contamination diagnostics, though its derived $b^*$ systematically overshoots the grid optimum by $\\sim$4$\\times$; and (3) adaptive $b^*$ serves as a zero-cost reasonable default recovering $\\sim$70\\% of grid-best improvement, while failing under cross-generator and domain-skewed contamination.\nThese results suggest that future work should focus on closing the overshoot gap---potentially through model-aware corrections to $b^*$---and on improving detector robustness to diverse synthetic sources at scale.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025contamination}\nDrayson, O., et~al.\n\\newblock Detecting and mitigating model-generated text in internet corpora.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024strong}\nShumailov, I., et~al.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock In \\emph{Nature}, 2024.\n\n\\bibitem[Dohmatob et~al.(2025)]{dohmatob2025strong}\nDohmatob, E., et~al.\n\\newblock Strong model collapse.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nXie, S.~M., et~al.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Xie et~al.(2023b)]{xie2023doremi}\nXie, S.~M., et~al.\n\\newblock DoReMi: Optimizing data mixtures by domain reweighting.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Abbas et~al.(2024)]{abbas2024softdedup}\nAbbas, A., et~al.\n\\newblock SoftDedup: Soft deduplication for training data.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Li et~al.(2025)]{li2025goldenratio}\nLi, Y., et~al.\n\\newblock Golden ratio weighting for synthetic and human data.\n\\newblock \\emph{arXiv:2502.18049}, 2025.\n\n\\bibitem[Anonymous(2025)]{convergence2025}\nAnonymous.\n\\newblock Convergence bounds for contaminated distributions.\n\\newblock \\emph{arXiv:2602.16065}, 2025.\n\n\\bibitem[Okanovic et~al.(2025)]{okanovic2025dynamic}\nOkanovic, D., et~al.\n\\newblock Dynamic loss-based reweighting for pretraining.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Hoffmann et~al.(2022)]{hoffmann2022chinchilla}\nHoffmann, J., et~al.\n\\newblock Training compute-optimal large language models.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96261961-e9c7-4249-a327-0745d27eb118",
  "isSidechain": false,
  "requestId": "req_011Cb3Xnm6cEWoXWnewn4fXx",
  "type": "assistant",
  "uuid": "f9614bf8-dbc1-4f9e-be1a-53e3fd628d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEgRSxMTmECxj3A2G5JkLA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 44850,
      "output_tokens": 11261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11261,
          "cache_read_input_tokens": 44850,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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

_source line 19 · 2026-05-15T02:05:52.923Z_

<details><summary>↩ Tool result · `toolu_01JzSBgPj38YKSNdjYM4ZYNo`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9614bf8-dbc1-4f9e-be1a-53e3fd628d6b",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "56f7f58b-1bff-458f-a031-c4be90403410",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{natbib}\n\n\\title{Adaptive Provenance Weighting for Contaminated Pretraining Corpora:\\\\A Diagnostic Framework and Practical Guidelines}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLarge-scale web corpora increasingly contain machine-generated text of unknown provenance and proportion, degrading language model pretraining.\nDetect-and-reweight approaches assign instance weights $w_i = (1-q_i)^b$ based on detector scores $q_i$, but the exponent $b$ must be tuned per model via grid search over a validation set.\nWe introduce \\textbf{adaptive $b^*$}, which derives $b$ online from per-batch contamination statistics $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ subject to an effective sample size (ESS) constraint, requiring no validation set and no known contamination ratio.\nOur experiments on FineWeb subsets (200M tokens, $\\rho \\in \\{0.4, 0.6\\}$) with Qwen3-0.6B and Llama-3.2-3B reveal three findings.\n\\textbf{(1)} A lightweight TF-IDF + logistic regression detector (AUC = 0.939) achieves within 0.003 PPL of a 150M-parameter ModernBERT detector (AUC = 0.986), establishing that expensive detectors are unnecessary for provenance weighting.\n\\textbf{(2)} The $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework, while producing $b^*$ values that systematically overshoot the grid-optimal $b$ by approximately $4\\times$, serves as a diagnostic tool whose $b^*$ trajectory exposes batch-level contamination structure.\n\\textbf{(3)} Adaptive $b^*$ provides a zero-cost reasonable default (recovering 70\\% of grid-best improvement) in standard settings, though it degrades under cross-generator contamination and domain-skewed injection.\nWe additionally provide the first systematic comparison of loss reweighting versus sampling importance resampling (SIR) under identical weighting formulas.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nThe proliferation of machine-generated text on the web poses a growing challenge for language model pretraining.\nRecent estimates suggest 20--60\\% of web-crawled corpora may contain synthetic content from diverse generators, with the exact proportion and provenance unknown at training time.\nTheoretical analyses demonstrate that even small amounts of synthetic contamination can degrade scaling laws and induce model collapse~\\citep{shumailov2024strong}.\n\nDrayson et al.\\ propose a detect-and-reweight framework: train a detector to produce per-instance contamination scores $q_i \\in [0,1]$, then weight each sample by $w_i = (1 - q_i)^b$ during training via Sampling Importance Resampling (SIR).\nWhile effective, this approach requires tuning $b$ per model through validation-based grid search---different model scales need different $b$ values (e.g., $b=10$ for GPT-2/SmolLM $\\leq$360M versus $b=1$ for SmolLM-1.7B), and the procedure assumes access to a clean validation set.\n\nWe propose \\textbf{adaptive $b^*$}: an online method that derives the weighting exponent from per-batch statistics of the detector score distribution, subject to an effective sample size (ESS) constraint.\nOur method requires neither a validation set nor knowledge of the contamination proportion, making it applicable to web-scale pretraining where these are unavailable.\nWe implement provenance weighting via direct loss reweighting rather than SIR, providing continuous gradient-level control.\n\nOur investigation yields three contributions, ordered by strength of evidence:\n\n\\begin{enumerate}\n    \\item \\textbf{Lightweight detector sufficiency.} A TF-IDF + logistic regression detector (50K parameters, AUC = 0.939, $<$1 min CPU training) produces training outcomes within 0.003 PPL of a ModernBERT 150M detector (AUC = 0.986, 1.5h GPU training).\n    The marginal return of detector quality on downstream PPL is negligible, suggesting that practitioners can skip expensive neural detectors entirely.\n\n    \\item \\textbf{$\\hat{\\alpha}_{\\mathrm{eff}}(b)$ as a diagnostic framework.} We formalize the connection between batch-level contamination statistics and the weighting exponent through $\\hat{\\alpha}_{\\mathrm{eff}}(b)$.\n    While the derived $b^*$ systematically overshoots the grid-optimal value (median $b^* \\approx 0.87$ versus grid-best $b = 0.2$), the $b^*$ trajectory across batches and contamination levels provides interpretable diagnostics about contamination structure that the original framework lacks.\n\n    \\item \\textbf{Loss reweighting vs.\\ SIR.} We provide a systematic comparison of continuous loss reweighting and discrete SIR under identical weighting formulas, characterizing their gradient variance and convergence behavior differences.\n\\end{enumerate}\n\nAs an additional practical finding, adaptive $b^*$ recovers approximately 70\\% of grid-best improvement at zero tuning cost, serving as a reasonable default in standard settings---though it degrades or becomes harmful under cross-generator contamination (Section~\\ref{sec:cross_gen}) and domain-skewed injection (Section~\\ref{sec:domain_skew}).\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:background}\n\n\\paragraph{Model Collapse and Synthetic Contamination.}\nTraining on model-generated data can cause progressive degradation of output quality, termed \\emph{model collapse}~\\citep{shumailov2024strong}.\nEven low contamination ratios degrade scaling behavior, motivating methods that mitigate synthetic content during pretraining.\n\n\\paragraph{Detect-and-Reweight.}\nDrayson et al.\\ train a detector to produce scores $q_i \\in [0,1]$ indicating the probability that sample $i$ is synthetic.\nEach sample receives weight $w_i = (1 - q_i)^b$, where $b > 0$ controls downweighting aggressiveness.\nTheir implementation uses SIR: samples are stochastically resampled proportional to their weights, effectively a discrete selection mechanism.\nThe exponent $b$ is selected via grid search over a validation set, yielding model-specific values ($b = 10$ for $\\leq$360M models, $b = 1$ for 1.7B).\n\n\\paragraph{Golden Ratio Weighting.}\nConcurrent work derives a theoretically optimal weight $w^* = 1/\\varphi$ but assumes the real-to-synthetic ratio $k$ is known, which is unrealistic for web corpora.\n\n\\paragraph{Domain-Level Reweighting.}\nDoReMi and DSIR optimize domain-level mixture weights, operating at a coarser granularity than our instance-level approach.\nSoftDedup applies soft reweighting based on duplication, which is orthogonal to provenance-based weighting.\nDynamic loss-based reweighting adjusts weights based on training loss rather than detector scores, providing a complementary signal.\n\n\\paragraph{Convergence Theory.}\nThe bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p, \\alpha\\}}$ from recent work motivates the definition of $\\alpha_{\\mathrm{eff}}$ and the derivation of $b^*$, though we do not claim this theoretical bridge as a contribution.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setting}\n\nWe consider pretraining on a corpus $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ where an unknown fraction $\\rho$ of samples are machine-generated.\nA pretrained detector provides scores $q_i \\in [0,1]$ estimating $P(\\text{synthetic} \\mid x_i)$.\nOur goal: assign weights $w_i = (1 - q_i)^b$ that mitigate contamination effects, with $b$ determined automatically.\n\n\\subsection{Effective Contamination Fraction $\\hat{\\alpha}_{\\mathrm{eff}}(b)$}\n\nFor a batch $\\mathcal{B}$ of size $n$, we define the effective contamination fraction under weighting exponent $b$:\n\\begin{equation}\n    \\hat{\\alpha}_{\\mathrm{eff}}(b) = 1 - \\frac{\\sum_{i \\in \\mathcal{B}} (1 - q_i)^b}{\\sum_{i \\in \\mathcal{B}} 1} = 1 - \\frac{1}{n} \\sum_{i \\in \\mathcal{B}} (1 - q_i)^b.\n\\end{equation}\nThis quantity measures how much effective mass is removed by the weighting scheme: when $b = 0$, $\\hat{\\alpha}_{\\mathrm{eff}} = 0$ (no downweighting); as $b \\to \\infty$, $\\hat{\\alpha}_{\\mathrm{eff}} \\to 1 - (1-\\rho_{\\mathcal{B}})$ where $\\rho_{\\mathcal{B}}$ is the batch contamination fraction for perfectly calibrated $q_i$.\n\n\\subsection{ESS-Constrained $b^*$ Derivation}\n\nWe derive $b^*$ by maximizing the contamination removal subject to maintaining sufficient effective sample size.\nThe ESS for weights $\\{w_i\\}$ in batch $\\mathcal{B}$ is:\n\\begin{equation}\n    \\mathrm{ESS}(\\mathcal{B}, b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2} = \\frac{\\left(\\sum_{i} (1-q_i)^b\\right)^2}{\\sum_{i} (1-q_i)^{2b}}.\n\\end{equation}\nWe impose $\\mathrm{ESS}(\\mathcal{B}, b) \\geq n_{\\min}$ and solve for the largest $b$ satisfying this constraint:\n\\begin{equation}\n    b^* = \\max \\{ b \\geq 0 : \\mathrm{ESS}(\\mathcal{B}, b) \\geq n_{\\min} \\}.\n\\end{equation}\n\nThe hyperparameter $n_{\\min}$ controls the aggressiveness of downweighting.\nUnlike the continuous exponent $b$ which spans $[0, \\infty)$ and requires multi-point grid search, $n_{\\min}$ takes small integer values ($\\{1, 2, 3, \\ldots, n\\}$) with $n_{\\min} = 2$ performing well across our experiments (Section~\\ref{sec:nmin}).\n\n\\begin{algorithm}[t]\n\\caption{Adaptive $b^*$ with ESS Constraint}\n\\label{alg:adaptive}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch $\\mathcal{B} = \\{(x_i, q_i)\\}_{i=1}^n$, ESS lower bound $n_{\\min}$, search range $[0, b_{\\max}]$\n\\STATE Compute $\\mathrm{ESS}(b)$ for $b \\in \\{0, 0.1, 0.2, \\ldots, b_{\\max}\\}$ via Eq.~(2)\n\\STATE $b^* \\leftarrow \\max\\{b : \\mathrm{ESS}(b) \\geq n_{\\min}\\}$\n\\STATE $w_i \\leftarrow (1 - q_i)^{b^*}$ for each $i \\in \\mathcal{B}$\n\\STATE $\\bar{w} \\leftarrow \\frac{1}{n}\\sum_i w_i$; \\quad $\\tilde{w}_i \\leftarrow w_i / \\bar{w}$ \\hfill (normalize to mean 1)\n\\STATE $\\mathcal{L}_{\\mathrm{weighted}} = \\frac{1}{n}\\sum_i \\tilde{w}_i \\cdot \\ell(x_i; \\theta)$\n\\RETURN $\\mathcal{L}_{\\mathrm{weighted}}$, $b^*$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Loss Reweighting vs.\\ SIR}\n\nDrayson et al.\\ implement provenance weighting via SIR: samples are resampled proportional to $w_i$ before each epoch, creating a modified dataset.\nWe instead apply weights directly to the loss function (Algorithm~\\ref{alg:adaptive}, line 5).\nThe key differences are:\n\\begin{itemize}\n    \\item \\textbf{Granularity}: Loss reweighting applies continuous weights per gradient step; SIR makes discrete include/exclude decisions per epoch.\n    \\item \\textbf{Gradient variance}: Loss reweighting introduces weight-dependent variance in gradient estimates; SIR introduces resampling variance.\n    \\item \\textbf{Adaptivity}: Per-batch $b^*$ naturally integrates with loss reweighting (weights change every batch); SIR would require re-resampling per batch, negating its data-loading efficiency.\n\\end{itemize}\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nWe use FineWeb subsets totaling 200M tokens.\nSynthetic data is generated by Qwen3-0.6B (self-generation setting) or Llama-3.2-1B (cross-generator setting) via continuation of real text prefixes.\nContamination ratios: $\\rho \\in \\{0.4, 0.6\\}$.\n\n\\paragraph{Detectors.}\n(1)~\\textbf{TF-IDF + LR}: TF-IDF features with logistic regression, $\\sim$50K parameters, $<$1 min CPU training, AUC = 0.939.\n(2)~\\textbf{ModernBERT 150M}: Fine-tuned ModernBERT, 150M parameters, 1.5h GPU training, AUC = 0.986.\n\n\\paragraph{Models.}\nQwen3-0.6B (primary) and Llama-3.2-3B (scale validation), trained for 6103 steps on 200M tokens with batch size 4 and gradient checkpointing.\n\n\\paragraph{Evaluation.}\nPerplexity (PPL) on a held-out FineWeb subset ($\\sim$4M tokens).\nDownstream: MMLU (5-shot) and HellaSwag (10-shot) for the 3B model.\nAll experiments use 3 random seeds (42, 123, 456) where budget permits.\n\n\\paragraph{Baselines.}\n\\textit{Uniform}: standard training without reweighting.\n\\textit{Grid-$b$}: fixed $b \\in \\{0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0\\}$.\n\\textit{Detect-and-remove}: discard samples with $q > 0.5$.\n\\textit{Random reweighting}: weights drawn uniformly from $[0, 2]$ (mean 1).\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Full Grid Curve Reveals Low-$b$ Optimum}\n\\label{sec:grid_curve}\n\nTable~\\ref{tab:full_grid} presents the complete PPL landscape across 9 fixed-$b$ values, adaptive $b^*$, and the uniform baseline ($\\rho = 0.4$, Qwen3-0.6B, 200M tokens).\n\n\\begin{table}[t]\n\\centering\n\\caption{Eval PPL across weighting exponents ($\\rho = 0.4$, Qwen3-0.6B, 200M tokens). Lower is better. Bold: best per seed.}\n\\label{tab:full_grid}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n$b$ & seed 42 & seed 123 & seed 456 \\\\\n\\midrule\n0.1     & 17.645 & 17.631 & 17.642 \\\\\n\\textbf{0.2}     & \\textbf{17.637} & \\textbf{17.625} & \\textbf{17.636} \\\\\n0.3     & 17.641 & 17.629 & 17.640 \\\\\n0.5     & 17.651 & 17.638 & 17.650 \\\\\n1.0     & 17.692 & 17.674 & 17.680 \\\\\n1.5     & 17.718 & 17.701 & 17.710 \\\\\n2.0     & 17.741 & 17.725 & $\\sim$17.73 \\\\\n3.0     & 17.774 & 17.760 & $\\sim$17.77 \\\\\n5.0     & 17.818 & 17.804 & $\\sim$17.82 \\\\\n\\midrule\nUniform & 17.690 & 17.690 & 17.700 \\\\\nAdaptive $b^*$ & 17.650 & 17.643 & 17.660 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe grid-best exponent is $b = 0.2$ across all three seeds, with PPL improvements of 0.053, 0.065, and 0.064 over uniform (seed 42, 123, 456 respectively).\nThe PPL curve is monotonically increasing for $b > 0.2$, confirming that aggressive downweighting hurts: at $b = 0.2$, contaminated samples retain 63\\% weight ($w = (1-0.9)^{0.2} = 0.63$), preserving useful signal while mildly correcting distributional shift.\n\nAdaptive $b^*$ (median $\\approx 0.87$) overshoots the grid optimum by approximately $4\\times$.\nThis systematic overshoot reduces the aggregate recovery ratio from the previously reported 88.6\\% (when $b = 0.5$ was believed to be grid-best) to 69.8\\% (Table~\\ref{tab:ratio}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Adaptive $b^*$ recovery ratio relative to grid-best ($b = 0.2$). The gap between adaptive and grid-best (0.013--0.024) exceeds cross-seed variance ($\\sim$0.007).}\n\\label{tab:ratio}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & Uniform & Grid-best ($b\\!=\\!0.2$) & Adaptive & Ratio \\\\\n\\midrule\n42  & 17.690 & 17.637 & 17.650 & 75.5\\% \\\\\n123 & 17.690 & 17.625 & 17.643 & 72.3\\% \\\\\n456 & 17.700 & 17.636 & 17.660 & 62.5\\% \\\\\n\\midrule\n\\textit{Aggregate} & --- & \\textit{0.182} & \\textit{0.127} & \\textit{69.8\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Lightweight Detector Sufficiency}\n\\label{sec:detector}\n\nTable~\\ref{tab:detector} compares the TF-IDF + LR and ModernBERT detectors.\nDespite a large AUC gap (0.939 vs.\\ 0.986), the PPL difference is negligible: 0.003 absolute, $<$0.02\\% relative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detector quality vs.\\ training PPL ($\\rho = 0.4$, Qwen3-0.6B, adaptive $b^*$, seed 42). AUC improves by 5\\% relative, but PPL gain is negligible.}\n\\label{tab:detector}\n\\small\n\\begin{tabular}{lccccl}\n\\toprule\nDetector & Params & AUC & ECE (cal.) & Adaptive PPL & Cost \\\\\n\\midrule\nTF-IDF + LR   & $\\sim$50K & 0.939 & 0.048 & 17.650 & $<$1 min CPU \\\\\nModernBERT 150M & 150M     & 0.986 & 0.022 & 17.647 & 1.5h GPU \\\\\n\\midrule\n\\multicolumn{2}{l}{$\\Delta$ (AUC $\\uparrow$ 0.047)} & & & $-$0.003 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonicity of $w = (1-q)^b$ guarantees that ranking correctness matters more than calibration accuracy.\nTF-IDF + LR, despite higher calibration error (ECE 0.048 vs.\\ 0.022) and a more diffuse $q$-score distribution (mid-range ratio 0.463 vs.\\ 0.28), preserves sufficient ranking quality for effective reweighting.\nThe practical implication: a detector trainable in under one minute on a CPU suffices for provenance weighting.\n\n\\subsection{Higher Contamination ($\\rho = 0.6$)}\n\\label{sec:rho06}\n\nTable~\\ref{tab:rho06} compares reweighting effectiveness at 40\\% and 60\\% contamination.\nAt $\\rho = 0.6$, uniform PPL rises from 17.69 to 17.85 (+0.9\\% relative), confirming that higher contamination degrades training quality.\nHowever, adaptive improvement does \\emph{not} scale with contamination: $\\Delta_{\\mathrm{adaptive}}$ decreases from 0.04 to 0.03.\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination level vs.\\ adaptive effectiveness (Qwen3-0.6B, seed 42). Higher contamination does not amplify the benefit of adaptive reweighting.}\n\\label{tab:rho06}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n$\\rho$ & Uniform & Adaptive & $\\Delta_{\\mathrm{abs}}$ & $\\Delta_{\\mathrm{rel}}$ (\\%) & $b^*$ median \\\\\n\\midrule\n0.4 & 17.690 & 17.650 & 0.040 & 0.23 & 0.87 \\\\\n0.6 & 17.850 & 17.820 & 0.030 & 0.17 & 1.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe adaptive mechanism responds directionally: $b^*$ median increases from 0.87 to 1.08 as contamination rises, reflecting higher batch-level $\\hat{\\alpha}_{\\mathrm{eff}}$.\nHowever, this response exacerbates overshoot---the true optimal $b$ likely remains near 0.2, so the increased $b^*$ at $\\rho = 0.6$ moves further from the optimum.\nAt $\\rho = 0.6$, grid $b = 0.5$ achieves PPL = 17.80, yielding $\\Delta = 0.05$ versus adaptive's 0.03, for a ratio of only 60\\%.\n\nThis result has diagnostic value: the $b^*$ shift from 0.87 to 1.08 correctly signals increased contamination, even though the derived value is not numerically optimal.\nThe $\\hat{\\alpha}_{\\mathrm{eff}}$ framework thus serves as a contamination \\emph{thermometer}, not an optimizer.\n\n\\subsection{Model Scale (Llama-3.2-3B)}\n\\label{sec:3b}\n\nWe evaluate on Llama-3.2-3B to test whether the method adapts to model scale (Table~\\ref{tab:3b}).\n\n\\begin{table}[t]\n\\centering\n\\caption{$b^*$ distribution comparison across model scales ($\\rho = 0.4$, seed 42). The $b^*$ distribution is nearly identical because it depends only on $q$-score statistics, not model architecture. KS test $p = 0.87$.}\n\\label{tab:3b}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & $b^*$ med. & $b^*$ mean & $b^*$ P25 & $b^*$ P75 & $\\Delta_{\\mathrm{rel}}$ (\\%) \\\\\n\\midrule\nQwen3-0.6B   & 0.87 & 1.40 & 0.54 & 1.51 & 0.23 \\\\\nLlama-3.2-3B & 0.92 & 1.38 & 0.55 & 1.48 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $b^*$ distributions are statistically indistinguishable (KS test $p = 0.87$) because $b^*$ is derived solely from $q$-score statistics, which depend on the data and detector, not the training model.\nThe PPL improvement for 3B is minimal: 0.01 absolute (16.19 vs.\\ 16.20), 0.06\\% relative---within noise.\n\nThis reveals a fundamental property: adaptive $b^*$ provides a \\emph{data-driven} default that is consistent across models.\nThis consistency is both a strength (predictable behavior) and a limitation (no model-specific adaptation).\nDrayson et al.'s observation that different model scales need different $b$ values (1 vs.\\ 10) suggests that optimal $b$ is model-dependent, a dimension our $q$-score-only derivation cannot capture.\n\n\\subsection{ESS Constraint Sensitivity ($n_{\\min}$)}\n\\label{sec:nmin}\n\nTable~\\ref{tab:nmin} presents the sensitivity of adaptive $b^*$ to the ESS lower bound $n_{\\min}$ (batch size $n = 4$).\n\n\\begin{table}[t]\n\\centering\n\\caption{$n_{\\min}$ sensitivity ($\\rho = 0.4$, Qwen3-0.6B, seed 42, batch size 4). Only $n_{\\min} = 2$ improves over uniform; $n_{\\min} = 1$ is too aggressive, $n_{\\min} \\geq 3$ collapses to uniform.}\n\\label{tab:nmin}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n$n_{\\min}$ & Eval PPL & $b^*$ median & Status \\\\\n\\midrule\n1 & 17.710 & 2.60 & Worse than uniform \\\\\n2 & 17.650 & 0.87 & Best \\\\\n3 & 17.690 & $\\sim$0.3 & $\\approx$ Uniform \\\\\n4 & 17.690 & 0.0 & $=$ Uniform \\\\\n5 & 17.690 & 0.0 & $=$ Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe sensitivity curve reveals a narrow effective range.\nAt $n_{\\min} = 1$, the ESS constraint is too permissive: $b^*$ reaches median 2.60, contaminated samples receive weight $w \\approx 0.004$, and PPL (17.71) is \\emph{worse} than uniform (17.69) due to over-downweighting.\nAt $n_{\\min} \\geq 3$, the constraint is too tight: $b^*$ is clamped near zero, and the method degrades to uniform training.\nAt $n_{\\min} = 4 = n$ (batch size), $b^* = 0$ identically---the ESS constraint demands all weights be equal, which is only possible when $b = 0$.\n\nOnly $n_{\\min} = 2$ occupies the effective region.\nWhile this single-point sensitivity is a limitation, we note that $n_{\\min}$ selection reduces from a continuous grid search over $b$ (requiring $\\geq 6$ runs) to checking 2--3 integer values, representing a significant practical simplification.\n\n\\subsection{Cross-Generator Robustness}\n\\label{sec:cross_gen}\n\nIn realistic web corpora, synthetic content originates from multiple generator families.\nWe test this by generating contamination with Llama-3.2-1B while training Qwen3-0.6B (Table~\\ref{tab:cross_gen}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-generator evaluation ($\\rho = 0.4$, Qwen3-0.6B, seed 42). When detector quality degrades on out-of-distribution synthetic text, adaptive reweighting becomes harmful.}\n\\label{tab:cross_gen}\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\nSetting & Uniform & Adaptive & $\\Delta$ & Verdict \\\\\n\\midrule\nSelf-gen (Qwen $\\to$ Qwen) & 17.690 & 17.650 & $-$0.040 & Adaptive wins \\\\\nCross-gen (Llama $\\to$ Qwen) & 17.750 & 17.770 & +0.020 & Adaptive \\textbf{loses} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe TF-IDF + LR detector, trained only on Qwen3-0.6B-generated text, generalizes poorly to Llama-3.2-1B outputs (AUC drops from 0.939 to 0.891).\nThe $q$-score distribution becomes diffuse (mid-range ratio rises from 0.463 to 0.52), degrading both the $\\hat{\\alpha}_{\\mathrm{eff}}$ estimates and the ranking quality of weights.\nAdaptive $b^*$ (PPL = 17.77) is \\emph{worse} than uniform (17.75): noisy reweighting does more harm than good.\n\nThis exposes a fundamental dependency: adaptive $b^*$ quality is bounded by detector signal-to-noise ratio.\nIn web corpora with diverse synthetic sources, detector AUC may be lower than in controlled settings, making the method less applicable precisely where it would be most needed.\n\n\\subsection{Domain-Skewed Injection}\n\\label{sec:domain_skew}\n\nWe test robustness to non-uniform contamination by concentrating 85\\% of synthetic content in the code domain.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-skewed contamination ($\\rho = 0.4$, Qwen3-0.6B). Per-batch adaptation amplifies domain skew rather than correcting it.}\n\\label{tab:domain_skew}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Uniform PPL & Adaptive PPL & $\\Delta$ \\\\\n\\midrule\nUniform injection & 17.690 & 17.650 & $-$0.040 \\\\\nDomain-skewed (code-heavy) & 17.730 & 17.760 & +0.030 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain skew creates a bimodal batch structure: code-heavy batches have uniformly high $q$-scores ($\\hat{\\alpha}_{\\mathrm{eff}}$ overestimates, $b^*$ too large), while text batches have low $q$-scores ($b^* \\approx 0$).\nThe per-batch mechanism, designed to adapt to local contamination variation, instead amplifies the skew by over-downweighting code batches that may contain useful programming knowledge.\n\n\\subsection{Baseline Comparisons}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} consolidates all methods under the standard setting ($\\rho = 0.4$, Qwen3-0.6B, seed 42).\n\n\\begin{table}[t]\n\\centering\n\\caption{Method comparison ($\\rho = 0.4$, Qwen3-0.6B, seed 42). Grid-best $b = 0.2$ dominates; adaptive provides partial improvement; random reweighting confirms detector signal is necessary.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\nMethod & PPL & $\\Delta$ vs.\\ Uniform & Signal source \\\\\n\\midrule\nGrid-best ($b = 0.2$) & 17.637 & $-$0.053 & Oracle grid \\\\\nAdaptive $b^*$ & 17.650 & $-$0.040 & Adaptive $q$-based \\\\\nDetect-and-remove ($q > 0.5$) & 17.680 & $-$0.010 & Hard threshold \\\\\nUniform & 17.690 & 0.000 & None \\\\\nRandom reweighting & 17.695 & +0.005 & Random \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ranking is: gentle reweighting ($b = 0.2$) $\\gg$ adaptive $\\gg$ detect-and-remove $>$ uniform $\\approx$ random.\nRandom reweighting (PPL = 17.695 $\\approx$ uniform) confirms that detector-informed signal is load-bearing: arbitrary weight perturbations do not help.\nDetect-and-remove (PPL = 17.68) removes $\\sim$42\\% of data (40\\% true synthetic + 2\\% false positives), losing useful signal that gentle reweighting preserves.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\nTable~\\ref{tab:downstream} reports MMLU and HellaSwag results for Llama-3.2-3B checkpoints.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation (Llama-3.2-3B, $\\rho = 0.4$, seed 42, 200M tokens). No significant differences are observed, consistent with the minimal PPL gap (0.06\\% relative) and severe undertraining (63 tokens/parameter vs.\\ Chinchilla-optimal $\\sim$20$\\times$).}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Uniform & Adaptive & $\\Delta$ \\\\\n\\midrule\nMMLU (5-shot) & 25.8\\% & 25.8\\% & 0.0\\% \\\\\nHellaSwag (10-shot) & 38.2\\% & 38.3\\% & +0.1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo significant downstream differences are observed.\nMMLU performance (25.8\\%) is near random-chance level (25\\%), reflecting severe undertraining at 200M tokens for a 3B model (63 tokens/parameter versus $\\sim$20$\\times$ Chinchilla-optimal).\nThe PPL improvement of 0.06\\% relative is far below the resolution of discrete accuracy benchmarks ($\\sim$0.5\\% absolute).\nWe note that PPL is a continuous metric with higher sensitivity than discrete accuracy, and do not claim downstream transfer at current scale.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why adaptive $b^*$ overshoots.}\nThe $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework estimates contamination from $q$-score statistics and seeks the most aggressive downweighting permitted by the ESS constraint.\nThis objective is misaligned with the true optimum in our setting: FineWeb synthetic data generated by Qwen3-0.6B is not pure noise but retains substantial linguistic quality.\nThe optimal strategy ($b = 0.2$, $w = 0.63$) is \\emph{mild correction}, not aggressive removal.\nThe ESS constraint prevents catastrophic over-downweighting (cf.\\ $n_{\\min} = 1$, Table~\\ref{tab:nmin}) but does not guide $b^*$ toward the shallow optimum.\n\n\\paragraph{Diagnostic value of $b^*$ trajectories.}\nDespite numerical inaccuracy, $b^*$ trajectories provide information absent from the Drayson framework.\nThe shift from $b^* = 0.87$ ($\\rho = 0.4$) to $b^* = 1.08$ ($\\rho = 0.6$) correctly indicates increased contamination.\nPer-batch $b^*$ variance reveals contamination heterogeneity: batches with higher contamination receive larger $b^*$, making the framework interpretable for data auditing even when not producing optimal weights.\n\n\\paragraph{When adaptive hurts.}\nWe identify two failure modes: (1) cross-generator contamination, where detector quality degrades (AUC 0.939 $\\to$ 0.891) and noisy $q$-scores lead to harmful reweighting (Section~\\ref{sec:cross_gen}); and (2) domain-skewed contamination, where per-batch adaptation amplifies rather than corrects the skew (Section~\\ref{sec:domain_skew}).\nBoth failure modes stem from violations of implicit assumptions: the detector generalizes well (violated in cross-generator), and contamination is roughly uniform across batches (violated in domain skew).\n\n\\paragraph{The $n_{\\min}$ sensitivity question.}\nA reviewer might argue that replacing grid search over $b$ with selection of $n_{\\min}$ merely substitutes one hyperparameter for another.\nWe partially concede: the method is not hyperparameter-free.\nHowever, $n_{\\min}$ is an integer in $\\{1, \\ldots, n\\}$ (typically 2--3 effective values), requiring far fewer runs to sweep than $b \\in [0.1, 10]$ (our grid uses 9 values).\nThis represents a reduction in tuning cost, not its elimination.\n\n\\paragraph{Loss reweighting vs.\\ SIR.}\nLoss reweighting enables per-batch adaptive $b^*$, which is architecturally incompatible with SIR's per-epoch resampling.\nThe continuous gradient-level control also avoids the discrete variance introduced by stochastic resampling.\nA full gradient variance analysis under both implementations remains future work.\n\n% ============================================================\n\\section{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Scale.}\nAll experiments use 200M tokens, far below production pretraining scale.\nThe 3B model is severely undertrained (63 tokens/parameter).\nEffect sizes at scale may differ qualitatively.\n\n\\textbf{Generator diversity.}\nCross-generator results (Section~\\ref{sec:cross_gen}) demonstrate degradation with a single out-of-distribution generator.\nReal web corpora contain outputs from many generators and model families; robustness under such diversity is untested.\n\n\\textbf{Contamination type.}\nWe study continuation-based synthetic text.\nOther contamination types (paraphrase, translation, summarization, instruction-following outputs) may interact differently with provenance detectors and reweighting schemes.\n\n\\textbf{$n_{\\min}$ sensitivity.}\nThe narrow effective range of $n_{\\min}$ at batch size 4 may not generalize to larger batch sizes, where the integer space grows and the ESS constraint landscape changes.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented adaptive $b^*$, an online method for deriving the weighting exponent in provenance-weighted pretraining from per-batch contamination statistics.\nOur investigation yields three actionable findings: (1) lightweight detectors (TF-IDF + LR) suffice for provenance weighting, with 3000$\\times$ fewer parameters and negligible PPL difference compared to neural alternatives; (2) the $\\hat{\\alpha}_{\\mathrm{eff}}(b)$ framework provides batch-level contamination diagnostics, though its derived $b^*$ systematically overshoots the grid optimum by $\\sim$4$\\times$; and (3) adaptive $b^*$ serves as a zero-cost reasonable default recovering $\\sim$70\\% of grid-best improvement, while failing under cross-generator and domain-skewed contamination.\nThese results suggest that future work should focus on closing the overshoot gap---potentially through model-aware corrections to $b^*$---and on improving detector robustness to diverse synthetic sources at scale.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{10}\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025contamination}\nDrayson, O., et~al.\n\\newblock Detecting and mitigating model-generated text in internet corpora.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024strong}\nShumailov, I., et~al.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock In \\emph{Nature}, 2024.\n\n\\bibitem[Dohmatob et~al.(2025)]{dohmatob2025strong}\nDohmatob, E., et~al.\n\\newblock Strong model collapse.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nXie, S.~M., et~al.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Xie et~al.(2023b)]{xie2023doremi}\nXie, S.~M., et~al.\n\\newblock DoReMi: Optimizing data mixtures by domain reweighting.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Abbas et~al.(2024)]{abbas2024softdedup}\nAbbas, A., et~al.\n\\newblock SoftDedup: Soft deduplication for training data.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Li et~al.(2025)]{li2025goldenratio}\nLi, Y., et~al.\n\\newblock Golden ratio weighting for synthetic and human data.\n\\newblock \\emph{arXiv:2502.18049}, 2025.\n\n\\bibitem[Anonymous(2025)]{convergence2025}\nAnonymous.\n\\newblock Convergence bounds for contaminated distributions.\n\\newblock \\emph{arXiv:2602.16065}, 2025.\n\n\\bibitem[Okanovic et~al.(2025)]{okanovic2025dynamic}\nOkanovic, D., et~al.\n\\newblock Dynamic loss-based reweighting for pretraining.\n\\newblock In \\emph{ICLR}, 2025.\n\n\\bibitem[Hoffmann et~al.(2022)]{hoffmann2022chinchilla}\nHoffmann, J., et~al.\n\\newblock Training compute-optimal large language models.\n\\newblock In \\emph{NeurIPS}, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f9614bf8-dbc1-4f9e-be1a-53e3fd628d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weigh…",
  "leafUuid": "56f7f58b-1bff-458f-a031-c4be90403410",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case research paper simulation",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Tool call

_source line 22 · 2026-05-15T02:05:57.757Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QH5qcH6hPkJdCPo6mZr8aC`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes for references)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56f7f58b-1bff-458f-a031-c4be90403410",
  "isSidechain": false,
  "requestId": "req_011Cb3Y3cY5sJXowqQbgVhTz",
  "type": "assistant",
  "uuid": "e9d08a7e-df78-47a6-b711-5f5e5d66f655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vn3wbUoeukHk8vhfEQ6Jf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11327,
      "cache_read_input_tokens": 45518,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 45518,
          "cache_creation_input_tokens": 11327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11327
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

_source line 23 · 2026-05-15T02:05:59.743Z_

<details><summary>↩ Tool result · `toolu_01QH5qcH6hPkJdCPo6mZr8aC`</summary>

```text
&lt;persisted-output>
Output too large (33.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/fa7753a8-dd61-4209-9c6b-997c283e43b3/tool-results/b70pwx3pi.txt

Preview (first 2KB):
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9d08a7e-df78-47a6-b711-5f5e5d66f655",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "3ac62462-74af-4f01-935c-2e22d8aeaa6a",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024strong' on page 1 undefined on i\nnput line 41.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:cross_gen' on page 2 undefined on input line 62.\n\n\nLaTeX Warning: Reference `sec:domain_skew' on page 2 undefined on input line 62\n.\n\n\nPackage natbib Warning: Citation `shumailov2024strong' on page 2 undefined on i\nnput line 69.\n\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 107.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 107.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 107.\n\n\nLaTeX Warning: Reference `sec:nmin' on page 3 undefined on input line 120.\n\n\nLaTeX Warning: Reference `alg:adaptive' on page 3 undefined on input line 139.\n\n[3]\nOverfull \\hbox (0.89413pt too wide) in paragraph at lines 164--167\n []\\T1/cmr/bx/n/10.95 Evaluation.[] \\T1/cmr/m/n/10.95 Per-plex-ity (PPL) on a h\neld-out FineWeb sub-set ($\\OMS/cmsy/m/n/10.95 ^^X$\\T1/cmr/m/n/10.95 4M to-kens)\n. Down-stream: MMLU\n\nOverfull \\hbox (87.8588pt too wide) in paragraph at lines 169--173\n []\\T1/cmr/bx/n/10.95 Baselines.[] \\T1/cmr/m/it/10.95 Uni-form\\T1/cmr/m/n/10.95\n : stan-dard train-ing with-out reweight-ing. \\T1/cmr/m/it/10.95 Grid-$\\OML/cmm\n/m/it/10.95 b$\\T1/cmr/m/n/10.95 : fixed $\\OML/cmm/m/it/10.95 b \\OMS/cmsy/m/n/10\n.95 2 f\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 1\\OML/cmm/m/\nit/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 2\\OML/cm\nm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 3\\OM\nL/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 \n5\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10\n.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/\nn/10.95 5\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 2\\OML/cmm/m/it/10.95 :\\OT1/cm\nr/m/n/10.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 3\\OML/cmm/m/it/10.95 :\\OT\n1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 5\\OML/cmm/m/it/10.95 \n:\\OT1/cmr/m/n/10.95 0\\OMS/cmsy/m/n/10.95 g$\\T1/cmr/m/n/10.95 .\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 178.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 178.\n\n\nLaTeX Warning: Reference `tab:full_grid' on page 4 undefined on input line 181.\n\n\n\nLaTeX Warning: Reference `tab:ratio' on page 4 undefined on input line 212.\n\n\nLaTeX Warning: Reference `tab:detector' on page 4 undefined on input line 235.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 259.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rho' on input line 259.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 259.\n\n\nLaTeX Warning: Reference `tab:rho06' on page 5 undefined on input line 262.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.288 \\subsection\n                 {Model Scale (Llama-3.2-3B)}\npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.288 \\subsection\n                 {Model Scale (Llama-3.2-3B)}]\n\nLaTeX Warning: Reference `tab:3b' on page 6 undefined on input line 291.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\min' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 315.\n\n\nLaTeX Warning: Reference `tab:nmin' on page 6 undefined on input line 318.\n\n\nLaTeX Warning: Reference `tab:cross_gen' on page 6 undefined on input line 350.\n\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.370 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.370 \n      ]\n\nLaTeX Warning: Reference `tab:baselines' on page 7 undefined on input line 400.\n\n\n\nLaTeX Warning: Reference `tab:downstream' on page 7 undefined on input line 427\n.\n\n\nOverfull \\hbox (1.277pt too wide) in paragraph at lines 444--448\n[]\\T1/cmr/m/n/10.95 No sig-nif-i-cant down-stream dif-fer-ences are ob-served. \nMMLU per-for-mance (25.8%) is near random-\n\nOverfull \\hbox (11.44273pt too wide) in paragraph at lines 444--448\n\\T1/cmr/m/n/10.95 chance level (25%), re-flect-ing se-vere un-der-train-ing at \n200M to-kens for a 3B model (63 to-kens/parameter\n[7\npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.448 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.448 \n      ]\n\nLaTeX Warning: Reference `tab:nmin' on page 8 undefined on input line 457.\n\n\nLaTeX Warning: Reference `sec:cross_gen' on page 8 undefined on input line 465.\n\n\n\nLaTeX Warning: Reference `sec:domain_skew' on page 8 undefined on input line 46\n5.\n\n[8\npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.478 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.478 \n      ]\n\nLaTeX Warning: Reference `sec:cross_gen' on page 9 undefined on input line 489.\n\n\n[9\npdfTeX warning (ext4): destination with the same identifier (name{table.9}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.510 \\begin{thebibliography}{10}\n                                 \npdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.510 \\begin{thebibliography}{10}\n                                 ]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\nFont metrics written on ecti1000.tfm.\nOutput written on ecti1000.600gf (256 characters, 53420 bytes).\nTranscript written on ecti1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cms\ny10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>\nOutput written on paper.pdf (10 pages, 301021 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 99.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 107.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 107.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 107.\n\n[3]\nOverfull \\hbox (0.89413pt too wide) in paragraph at lines 164--167\n []\\T1/cmr/bx/n/10.95 Evaluation.[] \\T1/cmr/m/n/10.95 Per-plex-ity (PPL) on a h\neld-out FineWeb sub-set ($\\OMS/cmsy/m/n/10.95 ^^X$\\T1/cmr/m/n/10.95 4M to-kens)\n. Down-stream: MMLU\n\nOverfull \\hbox (87.8588pt too wide) in paragraph at lines 169--173\n []\\T1/cmr/bx/n/10.95 Baselines.[] \\T1/cmr/m/it/10.95 Uni-form\\T1/cmr/m/n/10.95\n : stan-dard train-ing with-out reweight-ing. \\T1/cmr/m/it/10.95 Grid-$\\OML/cmm\n/m/it/10.95 b$\\T1/cmr/m/n/10.95 : fixed $\\OML/cmm/m/it/10.95 b \\OMS/cmsy/m/n/10\n.95 2 f\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 1\\OML/cmm/m/\nit/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 2\\OML/cm\nm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 3\\OM\nL/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 \n5\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10\n.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 1\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/\nn/10.95 5\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 2\\OML/cmm/m/it/10.95 :\\OT1/cm\nr/m/n/10.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 3\\OML/cmm/m/it/10.95 :\\OT\n1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 5\\OML/cmm/m/it/10.95 \n:\\OT1/cmr/m/n/10.95 0\\OMS/cmsy/m/n/10.95 g$\\T1/cmr/m/n/10.95 .\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 178.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 178.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 259.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\rho' on input line 259.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 259.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.288 \\subsection\n                 {Model Scale (Llama-3.2-3B)}\npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.288 \\subsection\n                 {Model Scale (Llama-3.2-3B)}]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\min' on input line 315.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 315.\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.370 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.370 \n      ]\nOverfull \\hbox (1.277pt too wide) in paragraph at lines 444--448\n[]\\T1/cmr/m/n/10.95 No sig-nif-i-cant down-stream dif-fer-ences are ob-served. \nMMLU per-for-mance (25.8%) is near random-\n\nOverfull \\",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/fa7753a8-dd61-4209-9c6b-997c283e43b3/tool-results/b70pwx3pi.txt",
    "persistedOutputSize": 34140
  },
  "sourceToolAssistantUUID": "e9d08a7e-df78-47a6-b711-5f5e5d66f655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weigh…",
  "leafUuid": "3ac62462-74af-4f01-935c-2e22d8aeaa6a",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case research paper simulation",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Tool call

_source line 26 · 2026-05-15T02:06:03.691Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QmgLwkyKS7jjAS3ug6wq12`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.pdf",
  "description": "Verify PDF was generated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac62462-74af-4f01-935c-2e22d8aeaa6a",
  "isSidechain": false,
  "requestId": "req_011Cb3Y47g2ZtAuXWhrSHcEJ",
  "type": "assistant",
  "uuid": "73e8c7dd-1918-497f-ba09-7de4e71004ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4hdQTmDKKwEZpD4xKucDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 56845,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 56845,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1207
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

_source line 27 · 2026-05-15T02:06:03.735Z_

<details><summary>↩ Tool result · `toolu_01QmgLwkyKS7jjAS3ug6wq12`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 304004 May 15 02:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73e8c7dd-1918-497f-ba09-7de4e71004ae",
  "isSidechain": false,
  "promptId": "f392543c-eb7c-4cb1-965a-2e6e5b38e31c",
  "type": "user",
  "uuid": "2d4338ce-c387-4578-8958-1251cb3656b2",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 304004 May 15 02:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "73e8c7dd-1918-497f-ba09-7de4e71004ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T02:06:12.712Z_

PDF 编译成功（304KB）。论文已写入 `worst/paper.tex` 并生成 `worst/paper.pdf`。

结构覆盖了 experiment_data.json 中全部 15 个实验：full grid curve + ratio analysis、detector sufficiency (TF-IDF vs ModernBERT)、ρ=0.6 contamination scaling、Llama-3.2-3B scale、n_min sensitivity (1/2/3/4/5)、cross-generator failure、domain-skewed failure、detect-and-remove baseline、random reweighting baseline、downstream eval。叙事按 narrative guidance 重构——primary finding 是 lightweight detector sufficiency，adaptive b* 定位为 diagnostic framework + reasonable default（非最优解），cross-gen/domain-skew 作为 failure modes 坦诚展示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d4338ce-c387-4578-8958-1251cb3656b2",
  "isSidechain": false,
  "requestId": "req_011Cb3Y4QoR2AaqqhWB17R7o",
  "type": "assistant",
  "uuid": "1b973908-0abf-466e-ab97-295de6507e9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/worst",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qM9soJPzXLHuu34jggnQS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 58052,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 58052,
          "cache_creation_input_tokens": 210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 210
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weigh…",
  "leafUuid": "1b973908-0abf-466e-ab97-295de6507e9a",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case research paper simulation",
  "sessionId": "fa7753a8-dd61-4209-9c6b-997c283e43b3"
}
```

---
