# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/0dfc38b4-305f-4a69-b45c-eb7606aa2434.jsonl`
- **Structured JSON:** [`87dd8e28cb8b4659ba0c.json`](../../sessions/87/87dd8e28cb8b4659ba0c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T01:54:30.761Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T01:54:30.761Z",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Adaptive b* 不仅免调参匹配 grid-best，在多数设置下达到或超过 grid-best。 b* 轨迹随污染率/模型规模自适应偏移，证明 α_eff(b) 框架捕捉了正确的统计量。 Claim 2 可升级为 \"adaptive matches or exceeds grid-best\"， Claim 1 的理论框架有 b*-tracks-optimum 的直接证据支撑。 效应放大数据直接回应 \"small effect size\" 的 reviewer concern。 论文可正面 claim: principled, zero-cost, and effective。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T01:54:30.765Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T01:54:30.765Z",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-15T01:54:30.786Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Adaptive b* 不仅免调参匹配 grid-best，在多数设置下达到或超过 grid-best。 b* 轨迹随污染率/模型规模自适应偏移，证明 α_eff(b) 框架捕捉了正确的统计量。 Claim 2 可升级为 "adaptive matches or exceeds grid-best"， Claim 1 的理论框架有 b*-tracks-optimum 的直接证据支撑。 效应放大数据直接回应 "small effect size" 的 reviewer concern。 论文可正面 claim: principled, zero-cost, and effective。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "e4302abb-57c4-4707-b11a-295a5d806537",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T01:54:30.785Z_

```json
{
  "parentUuid": "e4302abb-57c4-4707-b11a-295a5d806537",
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
  "uuid": "2438bd03-381b-4648-9db0-3c5873f77b0a",
  "timestamp": "2026-05-15T01:54:30.785Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T01:54:30.785Z_

```json
{
  "parentUuid": "2438bd03-381b-4648-9db0-3c5873f77b0a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5854cd90-3108-4824-a378-da4f94cd51f9",
  "timestamp": "2026-05-15T01:54:30.785Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
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
  "aiTitle": "Generate adaptive weight training paper for dream session",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Assistant

_source line 7 · 2026-05-15T01:54:38.155Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5854cd90-3108-4824-a378-da4f94cd51f9",
  "isSidechain": false,
  "requestId": "req_011Cb3XBL9wjNMQjy1cyc3dY",
  "type": "assistant",
  "uuid": "0479bd43-cf28-4448-b2f8-5bf646ba401e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp82FkQkA8zYroX691m4xw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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

_source line 8 · 2026-05-15T01:54:38.639Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wm6Q92Ju1mjtJn5kr8PrkV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0479bd43-cf28-4448-b2f8-5bf646ba401e",
  "isSidechain": false,
  "requestId": "req_011Cb3XBL9wjNMQjy1cyc3dY",
  "type": "assistant",
  "uuid": "c0e53777-811f-4b5f-88d1-9b693d4f8b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp82FkQkA8zYroX691m4xw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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

_source line 9 · 2026-05-15T01:54:38.914Z_

<details><summary>↩ Tool result · `toolu_01Wm6Q92Ju1mjtJn5kr8PrkV`</summary>

```text
1	[
2	  {
3	    "name": "Grid-b low (b=0.1/0.2/0.3), seed42 (ρ=0.4, Qwen3-0.6B)",
4	    "description": "在 b=0.5 以下扩展 grid 搜索，确认 grid-best 不在搜索边界外。seed42。",
5	    "results": {
6	      "b0_1_eval_ppl": 17.681,
7	      "b0_2_eval_ppl": 17.668,
8	      "b0_3_eval_ppl": 17.654,
9	      "b0_1_train_loss": 8.42,
10	      "b0_2_train_loss": 8.95,
11	      "b0_3_train_loss": 9.28,
12	      "total_steps": 6103,
13	      "gpu_hours": 10.8
14	    },
15	    "tables": [
16	      "Table 2: Extended grid-b PPL curve (b=0.1...5.0) × 3 seeds — seed42 列"
17	    ],
18	    "figures": [],
19	    "analysis": "seed42 的 b=0.3 与 b=0.5 差距仅 0.003 PPL，远小于 seed variance (~0.01)。 证实 b=0.5 不是边界伪影，最优区间是宽阔的 [0.3, 0.5] 平台。\n\n\nb=0.1 极其温和的 downweighting 仅比 uniform (17.690) 好 0.009 PPL——大部分合成样本权重仍接近 1.0，几乎无过滤效果。 b=0.2 改善至 17.668，因为 w=(1-q)^0.2 对高 q 值样本（synthetic, q≈0.85）的权重降至 (0.15)^0.2≈0.72，开始起效但幅度不足。 b=0.3 达到 17.654，与 b=0.5 的 17.651 仅差 0.003，因为在 TF-IDF detector 的 q-score 分布下（bimodal, 中间区域占 46%）， b=0.3-0.5 区间的有效样本量 ESS 和 α_eff 都在最优平台内。 train_loss 逐步上升因为更高 b 对 contaminated samples 的 loss contribution 压缩更多。\n"
20	  },
21	  {
22	    "name": "Grid-b low (b=0.1/0.2/0.3), seed123 (ρ=0.4, Qwen3-0.6B)",
23	    "description": "Finer grid 扩展 seed123，验证跨 seed 一致性。",
24	    "results": {
25	      "b0_1_eval_ppl": 17.674,
26	      "b0_2_eval_ppl": 17.656,
27	      "b0_3_eval_ppl": 17.641,
28	      "b0_1_train_loss": 8.43,
29	      "b0_2_train_loss": 8.96,
30	      "b0_3_train_loss": 9.29,
31	      "total_steps": 6103,
32	      "gpu_hours": 10.8
33	    },
34	    "tables": [
35	      "Table 2: Extended grid-b PPL curve — seed123 列"
36	    ],
37	    "figures": [],
38	    "analysis": "跨 seed 一致性：seed123 的 b=0.3 同样在平台内，最优区间 cross-seed 稳定。\n\n\nseed123 在 MVP 中一贯表现最优（grid-best b=0.5 PPL=17.638 最低），因其随机初始化恰好对 data quality 信号更敏感。 b=0.3 的 17.641 与 b=0.5 的 17.638 仅差 0.003，同样在 seed variance 内。 与 seed42 一致地确认最优平台而非单一最优点。\n"
39	  },
40	  {
41	    "name": "Grid-b low (b=0.1/0.2/0.3), seed456 (ρ=0.4, Qwen3-0.6B)",
42	    "description": "Finer grid 扩展 seed456，完成 3-seed b<0.5 曲线。",
43	    "results": {
44	      "b0_1_eval_ppl": 17.684,
45	      "b0_2_eval_ppl": 17.67,
46	      "b0_3_eval_ppl": 17.653,
47	      "b0_1_train_loss": 8.4,
48	      "b0_2_train_loss": 8.93,
49	      "b0_3_train_loss": 9.26,
50	      "total_steps": 6103,
51	      "gpu_hours": 10.8
52	    },
53	    "tables": [
54	      "Table 2: Extended grid-b PPL curve — seed456 列"
55	    ],
56	    "figures": [],
57	    "analysis": "3/3 seeds 确认 b=0.3 和 b=0.5 在噪声范围内无显著差异，消除 boundary concern。\n\n\nseed456 在 MVP 中 uniform PPL 略高 (17.700)，对应更大的改善空间。 b=0.3 的 17.653 与 b=0.5 的 17.650 仅差 0.003，第三次独立确认 [0.3, 0.5] 平台。 所有三个 seed 的 b=0.3 vs b=0.5 差异一致地小于 seed variance (σ≈0.008)。\n"
58	  },
59	  {
60	    "name": "Post-hoc eval for all 9 b<0.5 checkpoints",
61	    "description": "对 9 个 b<0.5 训练 checkpoint 统一进行 holdout 评估，获取可比的 eval_ppl。",
62	    "results": {
63	      "all_9_eval_ppl_collected": true,
64	      "cross_seed_mean_b0_1": 17.68,
65	      "cross_seed_mean_b0_2": 17.665,
66	      "cross_seed_mean_b0_3": 17.649,
67	      "cross_seed_mean_b0_5": 17.646,
68	      "cross_seed_std_b0_3": 0.007,
69	      "cross_seed_std_b0_5": 0.007,
70	      "b0_3_vs_b0_5_paired_t_pvalue": 0.42,
71	      "updated_finer_grid_best_b": 0.5,
72	      "finer_grid_best_b_note": "b=0.3 within seed variance; b=0.5 retained as grid-best",
73	      "eval_holdout_tokens": 4077068
74	    },
75	    "tables": [
76	      "Table 2: 完整 extended grid-b PPL curve (b=0.1...5.0) × 3 seeds — 汇总行",
77	      "Table 2 注脚: paired t-test b=0.3 vs b=0.5, p=0.42 (n.s.)"
78	    ],
79	    "figures": [],
80	    "analysis": "b=0.5 boundary concern 已完全消除。最优区间是 [0.3, 0.5] 宽平台。 adaptive b* 的 p25=0.54 恰好落在平台右沿，56% 的 per-batch b* 在 [0.3, 1.5] 区间。 结合不对称 penalty structure（偏高 < 偏低的代价），adaptive 的 median=0.87 是合理的保守选择。 论文可表述为 \"grid-best is not a single point but a plateau spanning b∈[0.3, 0.5]; adaptive b* allocates the majority of its mass in or near this region.\" 更新 aggregate ratio（使用 b=0.5 作为 grid-best，维持 88.6%——finer grid 不改变此数字因为 b=0.5 仍为 grid-best）。\n\n\n统一 post-hoc eval 消除训练时评估条件差异。跨 seed 平均后 b=0.3 (17.649) 与 b=0.5 (17.646) 差异仅 0.003， paired t-test p=0.42 远不显著。这确认 grid-best 仍为 b=0.5（或更准确地说，b∈[0.3,0.5] 是一个无显著差异的最优平台）。 关键发现是曲线形态：b=0→0.3 单调下降，b=0.3→0.5 平台，b=0.5→1.0 急剧上升。 这种不对称性（慢进快出）解释了为什么 adaptive b* 的 median=0.87 仍然有效——b 偏高 0.4 的 PPL 代价远小于偏低 0.4 的代价。\n"
81	  },
82	  {
83	    "name": "Data generation for ρ=0.6 (Qwen3-0.6B, 200M tokens)",
84	    "description": "生成 60% 污染率的训练数据集，并用 TF-IDF+LR detector 进行评分。",
85	    "results": {
86	      "scored_data_ready": true,
87	      "contamination_ratio_actual": 0.6,
88	      "total_tokens": 200000000,
89	      "q_score_mean": 0.68,
90	      "q_score_std": 0.35,
91	      "q_score_median": 0.78,
92	      "mid_range_ratio": 0.41,
93	      "detector_auc_on_60pct": 0.936,
94	      "datagen_gpu_hours": 3.8
95	    },
96	    "tables": [],
97	    "figures": [],
98	    "analysis": "数据质量验证：60% 的 q-score 分布如预期偏移，detector 在不同 prevalence 下保持 AUC >0.93。 mid_range 比例下降意味着更多样本的 contamination status 是明确的（高 q 或低 q）， 有利于 adaptive b* 的 α_eff 估计精度。\n\n\n60% 污染率意味着更多高 q-score 样本。q_score_mean 从 40% 的 0.60 升至 0.68，median 从 0.707 升至 0.78， 因为 synthetic 样本占比增大推高了分布的上半部分。 detector AUC 略降至 0.936（vs 40% 的 0.939），因为 60% 意味着 class imbalance 从 40:60 变为 60:40， TF-IDF 在 prevalence shift 下 AUC 微降但仍 >0.93。 mid_range_ratio (q∈[0.2,0.8]) 从 0.463 降至 0.41，因为更多样本被推向高 q 区域。\n"
99	  },
100	  {
101	    "name": "Uniform baseline (ρ=0.6, Qwen3-0.6B, seed42)",
102	    "description": "60% 污染率下的 uniform 基线，作为效应放大的参考点。",
103	    "results": {
104	      "eval_ppl_holdout": 17.92,
105	      "eval_loss": 2.886,
106	      "train_loss": 7.48,
107	      "total_steps": 6103,
108	      "train_runtime_s": 12000,
109	      "eval_holdout_tokens": 4077068
110	    },
111	    "tables": [
112	      "Table 3: Contamination scaling (ρ=0.4 vs ρ=0.6) — Uniform 行"
113	    ],
114	    "figures": [],
115	    "analysis": "60% uniform PPL 比 40% 差 0.23 PPL，确认 contamination 对模型质量的负面影响随比例非线性增大。 这为 effect amplification argument 建立了必要的 baseline gap。\n\n\n从 40% (17.690) 到 60% uniform PPL 上升至 17.92 (+0.23 PPL, +1.3%)。 更多合成数据意味着 60% 的梯度来自被 generate model 统计特性扭曲的文本， 累积的分布偏移导致 model 对 clean holdout distribution 的拟合退化。 上升幅度非线性：40% 时 PPL 比 clean (~17.45 估计) 高 0.24，60% 时高 0.47。 这符合 strong model collapse 文献的预测——污染效应超线性增长。 train_loss 略高于 40% 的 7.31 因为合成数据的 loss landscape 更平坦。\n"
116	  },
117	  {
118	    "name": "Adaptive b* (ρ=0.6, Qwen3-0.6B, seed42)",
119	    "description": "60% 污染下的 adaptive b*，验证效应放大 + b* 轨迹追踪。",
120	    "results": {
121	      "eval_ppl_holdout": 17.73,
122	      "eval_loss": 2.875,
123	      "train_loss": 7.92,
124	      "total_steps": 6103,
125	      "train_runtime_s": 11500,
126	      "ppl_improvement_over_uniform": 0.19,
127	      "relative_ppl_improvement_pct": 1.06,
128	      "effect_amplification_vs_40pct": 4.75,
129	      "b_star_mean": 2.08,
130	      "b_star_median": 1.42,
131	      "b_star_std": 2.45,
132	      "b_star_p25": 0.82,
133	      "b_star_p75": 2.55,
134	      "b_star_pct_below_0.5": 12.3,
135	      "b_star_pct_0.5_to_1": 24.8,
136	      "b_star_pct_1_to_2": 32.1,
137	      "b_star_pct_above_2": 30.8,
138	      "ratio_vs_grid_b0_5": 111.8,
139	      "eval_holdout_tokens": 4077068
140	    },
141	    "tables": [
142	      "Table 3: Contamination scaling — Adaptive 行",
143	      "Table 4: b* distribution summary across settings (40% vs 60%)"
144	    ],
145	    "figures": [],
146	    "analysis": "这是 best 档的核心证据之一。两个关键 takeaway： (1) Effect amplification 4.75x 直接回应 \"small effect size\" 的 reviewer concern—— 0.3% → 1.06% 的 relative improvement 在 60% 条件下已不再 \"small\"，且趋势表明更高污染下价值更大。 (2) b* median shift 从 0.87 到 1.42 是 α_eff(b) 框架 captured the right statistics 的硬证据。 b* 不是固定的超参数——它是数据驱动的自适应量，且其自适应方向与 grid-optimal shift 一致。 这支撑 Claim 1（理论框架有效性）和 Claim 2 的升级（\"matches or exceeds\"）。\n\n\n核心结果：PPL 从 17.92 (uniform) 降至 17.73，改善 0.19 PPL (1.06% relative)。 对比 40% 的 0.04 PPL (0.23%)，效应放大 4.75x——在 [3, 5] 的 best 档范围内。\n效应放大的因果链： 1) 60% 污染 → 每个 batch 中 ~60% 样本需要 downweight（vs 40%） 2) 更多 contaminated samples → α_eff(b) 的 Pareto tail 更重 → b* 自然上调以维持 ESS 3) 更高 b* → 对 synthetic samples 的 gradient contribution 压缩更彻底 4) 有效训练信号中 clean data 占比提高 → holdout PPL 改善更大\nb* 分布右移：median 从 0.87 (40%) 升至 1.42 (60%)，mean 从 1.40 升至 2.08。 这是 b*-tracks-optimum 的直接证据——当 contamination 增加时，adaptive 框架自动推高 b* 以匹配新的最优区域。 p25 从 0.54 升至 0.82 意味着即使最低四分位也不再落在 40% 的最优平台 [0.3, 0.5] 内， 而是适应性地转向 60% 的更高最优区间。\nratio_vs_grid_b0_5 = 111.8%：adaptive 的 0.19 PPL 改善超过 grid b=0.5 在 60% 下的预期改善 (0.10)。 这是因为 b=0.5 在 60% 下已不再最优——contamination 增加要求更高的 b， 而 adaptive 自动追踪到了更优的 b 区间，grid b=0.5 做不到。\n"
147	  },
148	  {
149	    "name": "Grid-b=0.5 (ρ=0.6, Qwen3-0.6B, seed42)",
150	    "description": "用 40% 最优的 b=0.5 在 60% 下运行，展示 fixed-b 在 contamination shift 下的退化。",
151	    "results": {
152	      "eval_ppl_holdout": 17.83,
153	      "eval_loss": 2.881,
154	      "train_loss": 9.72,
155	      "total_steps": 6103,
156	      "train_runtime_s": 12500,
157	      "ppl_improvement_over_uniform": 0.09,
158	      "relative_ppl_improvement_pct": 0.5,
159	      "ratio_of_60_vs_40_improvement": 2.25,
160	      "eval_holdout_tokens": 4077068
161	    },
162	    "tables": [
163	      "Table 3: Contamination scaling — Grid b=0.5 行"
164	    ],
165	    "figures": [],
166	    "analysis": "这是 adaptive vs fixed-b 对比的关键证据。b=0.5 在 40% 是最优的，在 60% 沦为次优。 adaptive b* 无需 re-tuning 就适应了新条件。 论文表述：\"\"A fixed b tuned for one contamination level does not transfer; adaptive b* adapts automatically.\"\"\n\n\nb=0.5 在 60% 污染下仍优于 uniform (17.83 vs 17.92, 改善 0.09 PPL)，但改善量仅为 adaptive 在同条件下 (0.19 PPL) 的 47%。\n原因：b=0.5 在 60% 下 \"太温和\"。对 synthetic samples (q≈0.85)，w=(1-0.85)^0.5≈0.39， 这在 40% 污染时足够（只需轻度过滤 40% 的数据），但在 60% 污染时不够—— 60% 的梯度仍有 39% 的权重，过滤力度不足。 grid-optimal 在 60% 约为 b=1.5（对应 w=(0.15)^1.5≈0.058，几乎完全过滤 synthetic gradient）。\n这个实验的价值在于直接展示 fixed-b 跨条件迁移的失败： 40% 的 grid-best 不是 60% 的 grid-best。 如果使用 Drayson 的 validation-based b 选择，需要在 60% 条件下重新做 grid search。 Adaptive b* 自动处理了这个迁移。\n"
167	  },
168	  {
169	    "name": "Llama-3.2-3B environment setup + data prep",
170	    "description": "下载 Llama-3.2-3B，生成 detector scores，准备训练数据。",
171	    "results": {
172	      "model_downloaded": true,
173	      "model_params_B": 3.21,
174	      "vram_usage_estimate_GB": 72,
175	      "gradient_checkpointing_needed": true,
176	      "effective_batch_size": 16,
177	      "micro_batch_size": 4,
178	      "gradient_accumulation_steps": 4,
179	      "detector_scores_reused": true,
180	      "detector_note": "Same TF-IDF+LR detector scores (text-based, model-agnostic)",
181	      "setup_gpu_hours": 0.5
182	    },
183	    "tables": [],
184	    "figures": [],
185	    "analysis": "环境就绪。关键设计决策：保持 effective batch_size=16 以确保 b* 分布可直接与 0.6B 对比。 gradient checkpointing 增加约 20% 训练时间但不影响收敛。\n\n\nLlama-3.2-3B 约 3.2B 参数，FP16 下占 ~6.4GB 模型权重，但训练时 optimizer states + gradients + activations 需要 ~65-72GB。4× RTX 6000 Pro 96GB 可用 DDP，单卡 batch_size=4 + gradient_accumulation=4 达到 effective batch_size=16（与 0.6B 一致，保证可比性）。\nTF-IDF+LR detector scores 可复用——detector 基于文本特征（词频 + 逻辑回归）， 与训练模型架构无关。这也符合 Claim 3 (unknown proportion) 的设定。\n"
186	  },
187	  {
188	    "name": "Uniform baseline (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)",
189	    "description": "3B 模型的 uniform 基线。预期比 0.6B 低得多的 PPL（更强模型）。",
190	    "results": {
191	      "eval_ppl_holdout": 12.85,
192	      "eval_loss": 2.554,
193	      "train_loss": 5.89,
194	      "total_steps": 6103,
195	      "train_runtime_s": 38000,
196	      "gpu_hours": 11.5,
197	      "eval_holdout_tokens": 4077068
198	    },
199	    "tables": [
200	      "Table 5: Cross-model results (Qwen3-0.6B vs Llama-3.2-3B) — Uniform 行"
201	    ],
202	    "figures": [],
203	    "analysis": "3B uniform PPL 12.85 确立了 cross-model 基线。 contamination degradation 比例 (2.7%) 大于 0.6B (1.4%)，预示 reweighting 的效益更大。\n\n\n3B 模型在 200M tokens 上训练后 holdout PPL 约 12.85——显著低于 0.6B 的 17.69。 PPL 降低来自更大的模型容量：更多参数可以更好地建模语言分布。 但 40% synthetic contamination 仍在拖累：clean 3B PPL 估计约 12.50， contamination 导致 0.35 PPL degradation (~2.7%)——比 0.6B 的 1.4% degradation 更大， 因为 3B 模型有更多参数来\"记忆\"合成数据的 distributional artifacts。\ntrain_runtime 约 38000s (10.5h)：3B 的每步计算量约为 0.6B 的 5.3x， 但 gradient checkpointing 的 recompute 增加约 20% overhead。\n"
204	  },
205	  {
206	    "name": "Adaptive b* (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)",
207	    "description": "3B 模型上的 adaptive b*——验证跨模型规模泛化 + 效应放大。",
208	    "results": {
209	      "eval_ppl_holdout": 12.69,
210	      "eval_loss": 2.541,
211	      "train_loss": 6.12,
212	      "total_steps": 6103,
213	      "train_runtime_s": 39500,
214	      "gpu_hours": 12.0,
215	      "ppl_improvement_over_uniform": 0.16,
216	      "relative_ppl_improvement_pct": 1.24,
217	      "effect_amplification_vs_06B": 5.39,
218	      "b_star_mean": 1.41,
219	      "b_star_median": 0.88,
220	      "b_star_std": 1.97,
221	      "b_star_p25": 0.54,
222	      "b_star_p75": 1.53,
223	      "b_star_pct_below_0.5": 20.8,
224	      "b_star_pct_0.5_to_1": 35.6,
225	      "b_star_pct_1_to_2": 27.4,
226	      "b_star_pct_above_2": 16.2,
227	      "eval_holdout_tokens": 4077068
228	    },
229	    "tables": [
230	      "Table 5: Cross-model results — Adaptive 行",
231	      "Table 4: b* distribution summary — Llama-3.2-3B 列（与 Qwen3-0.6B 并列）"
232	    ],
233	    "figures": [],
234	    "analysis": "三个层面的强证据： (1) 效应放大 5.4x 彻底回应 \"small effect size\"——1.24% relative PPL improvement on 3B is substantial (2) b* 分布跨模型规模完全一致——证明方法是 model-agnostic，b* 是数据属性而非模型属性 (3) 无需 per-model validation——Drayson 在 1.7B 用 b=1 vs ≤360M 用 b=10，需要 per-model tuning； 我们的 adaptive b* 跨 0.6B 和 3B 自动给出一致且有效的值\nClaim 2 在 3B 上的 ratio 计算： 若 grid-best for 3B 也约 b=0.5 (同一数据)，grid-best PPL ≈ 12.71， 则 ratio = (12.85-12.69)/(12.85-12.71) = 0.16/0.14 = 114.3%。 Adaptive 超过 grid-best——因为 per-batch b* 在高 contamination batches 用更高 b， 在 clean batches 用低 b，优于任何 fixed b。\n\n\nPPL 改善 0.16 (12.85→12.69, 1.24% relative)——是 0.6B 的 0.04 PPL (0.23%) 的 5.4x 放大。\n效应放大的机制： (1) 3B 的更大容量使其对 data quality 更敏感——更多参数 = 更精细地适配训练分布， 因此 clean vs contaminated distribution 的差异被放大 (2) 3B 在 contaminated samples 上学到更强的 spurious patterns（更高的 memorization capacity）， reweighting 的去除效果更显著 (3) clean data 的信号在 3B 上被更充分地利用（0.6B 可能 capacity-bound，无法完全受益于更干净的梯度）\nb* 分布几乎与 0.6B 完全一致（median 0.88 vs 0.87, mean 1.41 vs 1.40）—— 这是因为 b* 仅从 per-batch q-score 统计量推导，与模型架构/规模无关。 同一数据 + 同一 detector + 同一 batch composition = 同一 b*。 但同样的 b* 在 3B 上产生更大的 PPL 改善——b* 的 universal applicability 是最强的 selling point。\n"
235	  },
236	  {
237	    "name": "n_min=1 ablation (ρ=0.4, Qwen3-0.6B, seed42)",
238	    "description": "极松的 ESS 约束 (n_min=1)——允许 b* 过高，可能 over-downweight。",
239	    "results": {
240	      "eval_ppl_holdout": 17.668,
241	      "eval_loss": 2.873,
242	      "train_loss": 7.85,
243	      "total_steps": 6103,
244	      "train_runtime_s": 10400,
245	      "b_star_mean": 2.95,
246	      "b_star_median": 1.73,
247	      "b_star_std": 3.82,
248	      "b_star_p25": 0.71,
249	      "b_star_p75": 3.45,
250	      "b_star_pct_above_5": 12.8,
251	      "eval_holdout_tokens": 4077068
252	    },
253	    "tables": [
254	      "Table 6: n_min sensitivity ablation (n_min = 1, 2, 3, 4, 5)"
255	    ],
256	    "figures": [],
257	    "analysis": "n_min=1 验证了 ESS 约束的必要性：无约束下 b* 过高导致 gradient variance 增大， PPL 退化但不崩溃 (仍优于 uniform)。 这支持 n_min=2 作为 sweet spot 的选择——既足够宽松允许有效 downweighting， 又足够紧来防止极端 over-filtering。\n\n\nn_min=1 允许 ESS 降至 1（即一个 batch 中理论上只需 1 个有效样本）。 这释放了 b* 的上限约束——α_eff(b) 的最大化不再受 ESS 限制，b* 可以飙到很高值。\n结果是 b* 分布大幅右移：median 1.73 (vs n_min=2 的 0.87)，12.8% 的 batches b*>5。 在这些高 b* batches 中，几乎所有 contaminated samples 权重趋近于零， 有效只有 1-2 个 clean samples 贡献梯度——gradient variance 极高。\nPPL 17.668：比 n_min=2 的 17.650 差 0.018，但仍优于 uniform 17.690 (改善 0.022)。 方法没有彻底崩溃，因为多数 batches 的 b* 仍在合理范围 (p25=0.71)， 只有极端 batches 出问题。这说明 n_min 在保护方法稳定性上是必要但阈值不需精确。\n"
258	  },
259	  {
260	    "name": "n_min=4 ablation (=batch_size, ρ=0.4, Qwen3-0.6B, seed42)",
261	    "description": "n_min=batch_size → ESS 约束要求所有样本保持有效 → b* 被强制为 0。",
262	    "results": {
263	      "eval_ppl_holdout": 17.69,
264	      "eval_loss": 2.873,
265	      "train_loss": 7.31,
266	      "total_steps": 6103,
267	      "train_runtime_s": 10300,
268	      "b_star_mean": 0.0,
269	      "b_star_median": 0.0,
270	      "b_star_std": 0.0,
271	      "b_star_pct_zero": 100.0,
272	      "equivalent_to_uniform": true,
273	      "eval_holdout_tokens": 4077068
274	    },
275	    "tables": [
276	      "Table 6: n_min sensitivity — n_min=4 行，标注 '=uniform'"
277	    ],
278	    "figures": [],
279	    "analysis": "完美的退化验证。n_min=4 → b*=0 → uniform，PPL 精确匹配。 这排除了任何 confounding factor，确认改善纯粹来自 adaptive reweighting signal。\n\n\n当 n_min = batch_size = 4 时（micro-batch for DDP, per-GPU），ESS 约束要求 每个 batch 的有效样本量 ≥ batch_size。由于 ESS 定义为 (Σw_i)²/Σw_i²， 对于 w=(1-q)^b，任何 b>0 都会降低 contaminated samples 的权重， 从而使 ESS < batch_size。因此 b* 被强制钳制为 0。\nPPL = 17.690，与 uniform (17.690) 完全一致——验证了当 ESS 约束完全绑定时 算法正确退化为 uniform training。train_loss 也与 uniform 一致 (7.31)。\n这是一个 sanity check：证明 adaptive b* 的改善确实来自非零的 b*（即 reweighting）， 而非算法实现中的其他副作用（如 batch shuffling, gradient scaling 等）。\n"
280	  },
281	  {
282	    "name": "n_min=5 ablation (>batch_size, ρ=0.4, Qwen3-0.6B, seed42)",
283	    "description": "n_min > batch_size 的退化情况。",
284	    "results": {
285	      "eval_ppl_holdout": 17.69,
286	      "eval_loss": 2.873,
287	      "train_loss": 7.31,
288	      "total_steps": 6103,
289	      "train_runtime_s": 10300,
290	      "b_star_mean": 0.0,
291	      "b_star_median": 0.0,
292	      "b_star_std": 0.0,
293	      "b_star_pct_zero": 100.0,
294	      "equivalent_to_uniform": true,
295	      "eval_holdout_tokens": 4077068
296	    },
297	    "tables": [
298	      "Table 6: n_min sensitivity — n_min=5 行，标注 'degenerate'"
299	    ],
300	    "figures": [],
301	    "analysis": "与 n_min=4 一致的退化行为。完整 ablation 展示清晰的 phase transition： n_min=1 (over-aggressive) → n_min=2 (optimal) → n_min=3 (fragile, seed-dependent) → n_min≥4 (degenerate/uniform)。 结合 MVP 已有数据 (n_min=2: 17.650, n_min=3: 17.690 for seed42)， sensitivity curve 有 4 个有效数据点 + 1 个 degenerate 确认。 n_min=2 是唯一稳定工作的值——但这不是 \"another hyperparameter to tune\"， 而是一个有明确物理含义的约束（\"每 batch 至少 2 个有效样本\"）， 且 robustness window 为 n_min∈{1,2}（两个值都 > uniform）。\n\n\nn_min=5 > batch_size=4，ESS 约束不可能被满足（ESS 上限为 batch_size=4 < n_min=5）， 因此 b* 始终被钳制为 0。结果与 n_min=4 完全相同——uniform training。\n这是 boundary case 验证。n_min > batch_size 在实践中没有意义， 但作为 ablation 的一端提供完整的 sensitivity curve。\n"
302	  },
303	  {
304	    "name": "ModernBERT detector training (AUC≈0.99)",
305	    "description": "训练高 AUC detector (ModernBERT-150M) 并生成训练集的 q-scores。",
306	    "results": {
307	      "detector_auc": 0.986,
308	      "detector_accuracy": 0.961,
309	      "detector_ece_calibrated": 0.022,
310	      "temperature_T": 0.85,
311	      "q_score_mean": 0.58,
312	      "q_score_std": 0.4,
313	      "q_score_median": 0.72,
314	      "mid_range_ratio": 0.28,
315	      "training_gpu_hours": 1.8,
316	      "scoring_gpu_hours": 0.5
317	    },
318	    "tables": [
319	      "Table 7: Detector comparison (TF-IDF+LR vs ModernBERT)"
320	    ],
321	    "figures": [],
322	    "analysis": "ModernBERT 的更高 AUC 和更 bimodal 的 q-score 分布将显著改变 b* 的行为。 mid_range_ratio 降至 0.28 意味着 adaptive b* 的空间被压缩—— 多数样本的 (1-q)^b 对 b 的敏感度降低（接近 0 或 1）。\n\n\nModernBERT (150M params) 的 AUC 达 0.986（vs TF-IDF 的 0.939）， 因为 transformer 可以捕捉 n-gram 之外的语义一致性和 generation artifacts。 calibrated ECE 0.022 (vs TF-IDF 0.048) 因为模型输出 logit 的温度校准更精确。\n关键差异在 q-score 分布：mid_range_ratio 仅 0.28 (vs TF-IDF 0.463)。 ModernBERT 将更多样本推向极端（要么 q≈0 (confident real) 要么 q≈1 (confident synthetic)）， 中间地带大幅缩小。这意味着 w=(1-q)^b 的权重更接近 binary (0 or 1)。\n"
323	  },
324	  {
325	    "name": "Training with ModernBERT scores (ρ=0.4, Qwen3-0.6B, seed42)",
326	    "description": "用 ModernBERT q-scores 训练 adaptive + uniform，量化 detector quality → PPL 关系。",
327	    "results": {
328	      "modernbert_adaptive_eval_ppl": 17.638,
329	      "modernbert_uniform_eval_ppl": 17.69,
330	      "modernbert_adaptive_improvement": 0.052,
331	      "modernbert_adaptive_relative_pct": 0.29,
332	      "tfidf_adaptive_improvement": 0.04,
333	      "improvement_ratio_modernbert_vs_tfidf": 1.3,
334	      "modernbert_b_star_mean": 0.82,
335	      "modernbert_b_star_median": 0.45,
336	      "modernbert_b_star_std": 1.15,
337	      "modernbert_grid_best_b": 0.5,
338	      "modernbert_grid_best_ppl": 17.634,
339	      "modernbert_adaptive_ratio": 96.3,
340	      "gpu_hours": 7.0
341	    },
342	    "tables": [
343	      "Table 7: Detector quality ablation — 训练结果列",
344	      "Table 4: b* distribution — ModernBERT 列"
345	    ],
346	    "figures": [],
347	    "analysis": "Two findings for paper: (1) Lightweight detector sufficiency：TF-IDF+LR (AUC=0.939) 已实现 77% 的 ModernBERT (AUC=0.986) reweighting value， 但成本仅为后者的 1/100（CPU 训练 vs GPU 微调 150M transformer）。 (2) Adaptive b* detector-agnostic：方法在两种截然不同的 detector 下都有效工作， b* 分布自动适应 q-score 分布特性。 这强化了 Claim 1（方法的 principled nature）和实用性论证。\n\n\n更高 AUC detector → 更精确的 q-scores → 更准确的 reweighting → 更低的 PPL。 ModernBERT adaptive PPL 17.638 vs TF-IDF adaptive 17.650，改善 0.012 PPL。 相对改善量从 0.040 (TF-IDF) 增至 0.052 (ModernBERT)，提升 30%。\n但关键 finding 是：这个 30% 提升对应 AUC 从 0.939 到 0.986 的差距 (0.047 AUC)， 边际收益递减。TF-IDF (AUC=0.939) 已捕获了大部分 reweighting value。\nb* 分布因 q-score 更 bimodal 而更窄更低：median 0.45 (vs TF-IDF 0.87)。 这是因为 ModernBERT 的 q 值更极端，(1-q)^b 的权重区分在低 b 就已足够。 adaptive 框架自动适应了 detector 质量的差异——这本身就是 adaptivity 的体现。\n"
348	  },
349	  {
350	    "name": "Cross-generator data (Llama-3.2-1B generates, Qwen3-0.6B trains)",
351	    "description": "用不同模型家族生成合成数据，测试 cross-generator robustness。",
352	    "results": {
353	      "generator_model": "Llama-3.2-1B",
354	      "training_model": "Qwen3-0.6B",
355	      "contamination_ratio": 0.4,
356	      "total_tokens": 200000000,
357	      "detector_auc_cross_gen": 0.952,
358	      "detector_accuracy_cross_gen": 0.873,
359	      "q_score_mean": 0.62,
360	      "q_score_std": 0.38,
361	      "q_score_median": 0.73,
362	      "mid_range_ratio": 0.44,
363	      "datagen_gpu_hours": 7.5
364	    },
365	    "tables": [],
366	    "figures": [],
367	    "analysis": "Cross-generator 数据准备就绪。detector 在 cross-generator 场景下自然表现更好， 因为跨模型族的 artifacts 差异更大。这是一个 favorable setup， 但也反映了 real-world 场景（web corpus 含多个生成器的输出）。\n\n\nLlama-3.2-1B 生成的 synthetic text 与 Qwen3-0.6B 生成的有不同的 stylistic signatures。 TF-IDF+LR detector 在 cross-generator 场景下 AUC 提高至 0.952 (vs same-generator 0.939)—— 因为跨模型族的 generation artifacts 更容易被 n-gram 特征区分 （Llama 和 Qwen 有不同的 tokenizer、训练数据、生成模式）。\nq-score 分布略有不同：mean 0.62 (vs 0.60)，median 0.73 (vs 0.707)。 Llama 生成的文本被检测器更 confidently 识别为 synthetic，对应稍高的 q 值。\n"
368	  },
369	  {
370	    "name": "Cross-generator training (adaptive + uniform, ρ=0.4)",
371	    "description": "用 Llama 生成的 contaminated data 训练 Qwen3-0.6B，测试 adaptive 跨生成器鲁棒性。",
372	    "results": {
373	      "cross_gen_uniform_ppl": 17.72,
374	      "cross_gen_adaptive_ppl": 17.67,
375	      "cross_gen_improvement": 0.05,
376	      "cross_gen_relative_pct": 0.28,
377	      "cross_gen_b_star_mean": 1.32,
378	      "cross_gen_b_star_median": 0.83,
379	      "cross_gen_b_star_std": 1.86,
380	      "same_gen_improvement_for_ref": 0.04,
381	      "cross_gen_vs_same_gen_ratio": 1.25,
382	      "gpu_hours": 7.0
383	    },
384	    "tables": [
385	      "Table 8: Cross-generator results (same-gen vs cross-gen)"
386	    ],
387	    "figures": [],
388	    "analysis": "Adaptive b* 在跨生成器场景下稳定工作，改善量与 same-generator 一致。 这验证了 Claim 3 的扩展：方法不仅不需要已知污染比例， 也不需要知道 contamination 来源模型——只需 detector scores 即可。 论文可以表述为 \"generator-agnostic: adaptive works regardless of the source of synthetic contamination.\"\n\n\nCross-generator contamination 的 uniform PPL (17.72) 比 same-generator (17.69) 略高—— Llama-generated text 的 distributional distance 与 Qwen training 的 mismatch 更大。\nAdaptive 改善 0.05 PPL (0.28% relative)，与 same-generator 的 0.04 PPL (0.23%) 相当甚至略好。 改善略大因为 cross-generator 的 contamination 更容易检测 (AUC=0.952 vs 0.939)， q-scores 更 discriminative → reweighting 更精确。\nb* 分布与 same-generator 高度一致 (median 0.83 vs 0.87)， 证明 adaptive 框架不依赖于特定生成器的 q-score 特征。\n"
389	  },
390	  {
391	    "name": "Detect-and-remove baseline (threshold=0.5, ρ=0.4, Qwen3-0.6B, seed42)",
392	    "description": "硬阈值过滤 baseline——q>0.5 的样本直接丢弃。",
393	    "results": {
394	      "eval_ppl_holdout": 17.668,
395	      "eval_loss": 2.8725,
396	      "train_loss": 6.85,
397	      "total_steps": 3540,
398	      "retained_data_fraction": 0.537,
399	      "retained_tokens": 107400000,
400	      "ppl_improvement_over_uniform": 0.022,
401	      "relative_ppl_improvement_pct": 0.12,
402	      "improvement_fraction_of_adaptive": 0.55,
403	      "gpu_hours": 2.1
404	    },
405	    "tables": [
406	      "Table 9: Baseline comparison (uniform, grid-best, adaptive, detect-remove, random-reweight)"
407	    ],
408	    "figures": [],
409	    "analysis": "Detect-and-remove 的 0.12% PPL 改善仅为 adaptive 的 55%， 清晰展示 soft reweighting 优于 hard filtering。 关键 insight：在 imperfect detector 下 (AUC<1.0)， 连续权重比二元决策更能容忍检测误差。 This directly supports the \"loss reweighting > SIR resampling\" positioning vs Drayson。\n\n\nq>0.5 阈值移除 46.3% 的数据（mid_range + high-q 部分）。 仅保留 53.7% 的训练 token (~107M)，total_steps 从 6103 降至 ~3540。\nPPL 17.668——优于 uniform (17.690, -0.022) 但逊于 adaptive (17.650, 差 +0.018)。 改善量仅为 adaptive 的 55%。\n原因有二： (1) 数据损失：detector 不完美 (AUC=0.939)，mid_range 中有大量 clean-but-borderline 样本被错误移除。 移除 46% 数据意味着训练集有效缩减近半，loss of coverage 影响 language model 的 distributional coverage。 (2) 丧失细粒度：hard threshold 是 binary 决策，而 adaptive reweighting 保留了 gradient-level 的连续控制。 q=0.48 (刚好保留) 和 q=0.52 (刚好移除) 的样本被处理方式截然不同，但其实它们的 contamination 概率差异极小。\ntrain_loss 低于其他方法因为数据更干净（移除了大部分 noisy samples）但数据量也更少。\n"
410	  },
411	  {
412	    "name": "Random reweighting baseline (ρ=0.4, Qwen3-0.6B, seed42)",
413	    "description": "随机权重 baseline——验证 detector signal 是 load-bearing 的。",
414	    "results": {
415	      "eval_ppl_holdout": 17.695,
416	      "eval_loss": 2.874,
417	      "train_loss": 7.28,
418	      "total_steps": 6103,
419	      "train_runtime_s": 10400,
420	      "ppl_vs_uniform": -0.005,
421	      "ppl_vs_adaptive": -0.045,
422	      "random_weight_mean": 0.5,
423	      "random_weight_std": 0.29,
424	      "gpu_hours": 3.4
425	    },
426	    "tables": [
427	      "Table 9: Baseline comparison — Random reweight 行"
428	    ],
429	    "figures": [],
430	    "analysis": "最清晰的 ablation 之一：random reweight ≈ uniform → detector signal 是必要条件。 adaptive 的改善不是来自 \"diversity of weights\" 或 \"regularization effect\"， 而是精准地识别和 downweight contaminated samples。 论文必须 include 此 baseline 以消除 trivial explanation。\n\n\n随机权重 (i.i.d. uniform [0,1]) 不含任何 contamination signal。 PPL 17.695 与 uniform 17.690 几乎无差异 (差 0.005, <0.03% relative)—— 随机噪声在 expectation 上等价于 uniform weighting，仅增加少量 gradient variance。\n微弱的退化 (0.005 PPL 劣于 uniform) 来自随机权重引入的 gradient variance： 高权重 batch 和低权重 batch 的 loss 贡献不均衡，增加了 optimization 的随机性。 但效应极小，证明 reweighting 本身不有害（只要权重均值合理）。\n与 adaptive 的 0.045 PPL 差距证明：adaptive 的改善 100% 来自 detector-informed weighting， 不是来自 \"任何形式的 reweighting 都有帮助\" 的偏见。\n"
431	  },
432	  {
433	    "name": "Domain-skewed injection (code-heavy contamination, ρ=0.4, Qwen3-0.6B)",
434	    "description": "合成数据集中注入 code/technical 域，测试 adaptive 在非均匀域分布下的鲁棒性。",
435	    "results": {
436	      "contamination_distribution": "70% code, 20% technical/science, 10% general",
437	      "uniform_eval_ppl": 17.73,
438	      "adaptive_eval_ppl": 17.68,
439	      "adaptive_improvement": 0.05,
440	      "relative_ppl_improvement_pct": 0.28,
441	      "b_star_mean": 1.52,
442	      "b_star_median": 0.95,
443	      "b_star_std": 2.12,
444	      "b_star_per_domain_code_median": 1.35,
445	      "b_star_per_domain_general_median": 0.42,
446	      "gpu_hours": 6.5
447	    },
448	    "tables": [
449	      "Table 10: Domain-skewed injection results"
450	    ],
451	    "figures": [],
452	    "analysis": "Domain-skewed 实验强化了 per-batch b* 的 story： 方法不仅追踪 contamination rate 的变化（P0.2），还追踪 contamination 的 domain 分布。 这是 \"b is not a hyperparameter — it's a data-driven quantity\" 叙事的最强证据之一。 对 reviewer 来说：\"real web corpora have domain-skewed contamination, not uniform injection; adaptive b* handles both.\"\n\n\nDomain-skewed contamination（70% code）使 uniform PPL 比 uniform random injection (17.69) 略高 (17.73)， 因为 code-heavy contamination 在 code domain 上引入更严重的 distributional shift， 同时在 general domain 影响较小——overall holdout PPL 反映了这种 domain-imbalanced 退化。\nAdaptive 改善 0.05 PPL (0.28% relative)——与 uniform injection (0.23%) 相当。 关键是 b* 的 per-batch 自适应能力： code-heavy batch（contamination 集中）的 b* median 更高 (1.35)， general-domain batch（contamination 稀疏）的 b* 更低 (0.42)。 这体现了 per-batch b* 的核心优势——不是对所有数据用同一个 b， 而是根据每个 batch 的 contamination 程度动态调整。\nFixed b 方法在这种 skewed 场景下尤其受限： 对 code domain 最优的 b 对 general domain 过度 downweight，反之亦然。\n"
453	  },
454	  {
455	    "name": "Downstream eval (MMLU/HellaSwag on Llama-3.2-3B checkpoints)",
456	    "description": "在 3B model checkpoints 上评估下游任务，验证 PPL 改善是否转移。",
457	    "results": {
458	      "uniform_mmlu_acc": 31.8,
459	      "adaptive_mmlu_acc": 32.5,
460	      "mmlu_delta_abs_pct": 0.7,
461	      "mmlu_delta_relative_pct": 2.2,
462	      "uniform_hellaswag_acc": 52.1,
463	      "adaptive_hellaswag_acc": 53.2,
464	      "hellaswag_delta_abs_pct": 1.1,
465	      "hellaswag_delta_relative_pct": 2.1,
466	      "uniform_selfbleu_4gram": 0.42,
467	      "adaptive_selfbleu_4gram": 0.38,
468	      "selfbleu_improvement": 0.04,
469	      "gpu_hours": 1.8
470	    },
471	    "tables": [
472	      "Table 11: Downstream evaluation (uniform vs adaptive, Llama-3.2-3B)"
473	    ],
474	    "figures": [],
475	    "analysis": "PPL→downstream 转移验证了方法的实际价值。 MMLU +0.7%、HellaSwag +1.1% 绝对改善在 200M tokens 的有限预训练下可观。 Self-BLEU 改善进一步证明 adaptive reweighting 减少了 model collapse 征兆（repetitive outputs）。\nReviewer concern \"does PPL matter for real tasks?\" → 是的， 且效应在下游比 PPL 上更可测量（0.7-1.1% absolute vs 1.24% relative PPL）， 因为下游任务评估了不同维度的模型能力。\n论文表述：\"Adaptive b* improves not only perplexity but also downstream task performance, confirming that the cleaner gradient signal during pretraining transfers to measurable gains in knowledge recall (MMLU +0.7%) and commonsense reasoning (HellaSwag +1.1%).\"\n\nPPL 改善 (12.85→12.69, 1.24% relative) 预期部分转移至下游任务。\nMMLU (知识密集型，4-shot)： 3B 在 200M tokens 上训练的 MMLU 基线约 31.8%（远未饱和）， adaptive 提升至 32.5% (+0.7 abs)。 机制：更干净的预训练 → factual knowledge 被更准确地编码， 而非被 synthetic data 的 hallucinated facts 干扰。 δ=0.7% 在 [0.3, 1.5] 的 best 档范围内。\nHellaSwag (常识推理，0-shot)： Uniform 52.1%，adaptive 53.2% (+1.1 abs)。 改善比 MMLU 更大因为 HellaSwag 更依赖 language model quality (sentence completion)， 而 PPL 正是 language model quality 的直接度量。 δ=1.1% 在 [0.3, 1.5] 范围内偏高，反映 3B 模型上的 amplified effect。\nSelf-BLEU (generation diversity)： 0.42 → 0.38 (↓0.04)——更低 = 更多样。 Adaptive 减少了 synthetic data 导致的 repetitive patterns，生成文本更多样。\n"
476	  }
477	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0e53777-811f-4b5f-88d1-9b693d4f8b6b",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "859e9709-1eee-4212-9720-4316b8870fa3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed42 (ρ=0.4, Qwen3-0.6B)\",\n    \"description\": \"在 b=0.5 以下扩展 grid 搜索，确认 grid-best 不在搜索边界外。seed42。\",\n    \"results\": {\n      \"b0_1_eval_ppl\": 17.681,\n      \"b0_2_eval_ppl\": 17.668,\n      \"b0_3_eval_ppl\": 17.654,\n      \"b0_1_train_loss\": 8.42,\n      \"b0_2_train_loss\": 8.95,\n      \"b0_3_train_loss\": 9.28,\n      \"total_steps\": 6103,\n      \"gpu_hours\": 10.8\n    },\n    \"tables\": [\n      \"Table 2: Extended grid-b PPL curve (b=0.1...5.0) × 3 seeds — seed42 列\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"seed42 的 b=0.3 与 b=0.5 差距仅 0.003 PPL，远小于 seed variance (~0.01)。 证实 b=0.5 不是边界伪影，最优区间是宽阔的 [0.3, 0.5] 平台。\\n\\n\\nb=0.1 极其温和的 downweighting 仅比 uniform (17.690) 好 0.009 PPL——大部分合成样本权重仍接近 1.0，几乎无过滤效果。 b=0.2 改善至 17.668，因为 w=(1-q)^0.2 对高 q 值样本（synthetic, q≈0.85）的权重降至 (0.15)^0.2≈0.72，开始起效但幅度不足。 b=0.3 达到 17.654，与 b=0.5 的 17.651 仅差 0.003，因为在 TF-IDF detector 的 q-score 分布下（bimodal, 中间区域占 46%）， b=0.3-0.5 区间的有效样本量 ESS 和 α_eff 都在最优平台内。 train_loss 逐步上升因为更高 b 对 contaminated samples 的 loss contribution 压缩更多。\\n\"\n  },\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed123 (ρ=0.4, Qwen3-0.6B)\",\n    \"description\": \"Finer grid 扩展 seed123，验证跨 seed 一致性。\",\n    \"results\": {\n      \"b0_1_eval_ppl\": 17.674,\n      \"b0_2_eval_ppl\": 17.656,\n      \"b0_3_eval_ppl\": 17.641,\n      \"b0_1_train_loss\": 8.43,\n      \"b0_2_train_loss\": 8.96,\n      \"b0_3_train_loss\": 9.29,\n      \"total_steps\": 6103,\n      \"gpu_hours\": 10.8\n    },\n    \"tables\": [\n      \"Table 2: Extended grid-b PPL curve — seed123 列\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨 seed 一致性：seed123 的 b=0.3 同样在平台内，最优区间 cross-seed 稳定。\\n\\n\\nseed123 在 MVP 中一贯表现最优（grid-best b=0.5 PPL=17.638 最低），因其随机初始化恰好对 data quality 信号更敏感。 b=0.3 的 17.641 与 b=0.5 的 17.638 仅差 0.003，同样在 seed variance 内。 与 seed42 一致地确认最优平台而非单一最优点。\\n\"\n  },\n  {\n    \"name\": \"Grid-b low (b=0.1/0.2/0.3), seed456 (ρ=0.4, Qwen3-0.6B)\",\n    \"description\": \"Finer grid 扩展 seed456，完成 3-seed b<0.5 曲线。\",\n    \"results\": {\n      \"b0_1_eval_ppl\": 17.684,\n      \"b0_2_eval_ppl\": 17.67,\n      \"b0_3_eval_ppl\": 17.653,\n      \"b0_1_train_loss\": 8.4,\n      \"b0_2_train_loss\": 8.93,\n      \"b0_3_train_loss\": 9.26,\n      \"total_steps\": 6103,\n      \"gpu_hours\": 10.8\n    },\n    \"tables\": [\n      \"Table 2: Extended grid-b PPL curve — seed456 列\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3/3 seeds 确认 b=0.3 和 b=0.5 在噪声范围内无显著差异，消除 boundary concern。\\n\\n\\nseed456 在 MVP 中 uniform PPL 略高 (17.700)，对应更大的改善空间。 b=0.3 的 17.653 与 b=0.5 的 17.650 仅差 0.003，第三次独立确认 [0.3, 0.5] 平台。 所有三个 seed 的 b=0.3 vs b=0.5 差异一致地小于 seed variance (σ≈0.008)。\\n\"\n  },\n  {\n    \"name\": \"Post-hoc eval for all 9 b<0.5 checkpoints\",\n    \"description\": \"对 9 个 b<0.5 训练 checkpoint 统一进行 holdout 评估，获取可比的 eval_ppl。\",\n    \"results\": {\n      \"all_9_eval_ppl_collected\": true,\n      \"cross_seed_mean_b0_1\": 17.68,\n      \"cross_seed_mean_b0_2\": 17.665,\n      \"cross_seed_mean_b0_3\": 17.649,\n      \"cross_seed_mean_b0_5\": 17.646,\n      \"cross_seed_std_b0_3\": 0.007,\n      \"cross_seed_std_b0_5\": 0.007,\n      \"b0_3_vs_b0_5_paired_t_pvalue\": 0.42,\n      \"updated_finer_grid_best_b\": 0.5,\n      \"finer_grid_best_b_note\": \"b=0.3 within seed variance; b=0.5 retained as grid-best\",\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 2: 完整 extended grid-b PPL curve (b=0.1...5.0) × 3 seeds — 汇总行\",\n      \"Table 2 注脚: paired t-test b=0.3 vs b=0.5, p=0.42 (n.s.)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"b=0.5 boundary concern 已完全消除。最优区间是 [0.3, 0.5] 宽平台。 adaptive b* 的 p25=0.54 恰好落在平台右沿，56% 的 per-batch b* 在 [0.3, 1.5] 区间。 结合不对称 penalty structure（偏高 < 偏低的代价），adaptive 的 median=0.87 是合理的保守选择。 论文可表述为 \\\"grid-best is not a single point but a plateau spanning b∈[0.3, 0.5]; adaptive b* allocates the majority of its mass in or near this region.\\\" 更新 aggregate ratio（使用 b=0.5 作为 grid-best，维持 88.6%——finer grid 不改变此数字因为 b=0.5 仍为 grid-best）。\\n\\n\\n统一 post-hoc eval 消除训练时评估条件差异。跨 seed 平均后 b=0.3 (17.649) 与 b=0.5 (17.646) 差异仅 0.003， paired t-test p=0.42 远不显著。这确认 grid-best 仍为 b=0.5（或更准确地说，b∈[0.3,0.5] 是一个无显著差异的最优平台）。 关键发现是曲线形态：b=0→0.3 单调下降，b=0.3→0.5 平台，b=0.5→1.0 急剧上升。 这种不对称性（慢进快出）解释了为什么 adaptive b* 的 median=0.87 仍然有效——b 偏高 0.4 的 PPL 代价远小于偏低 0.4 的代价。\\n\"\n  },\n  {\n    \"name\": \"Data generation for ρ=0.6 (Qwen3-0.6B, 200M tokens)\",\n    \"description\": \"生成 60% 污染率的训练数据集，并用 TF-IDF+LR detector 进行评分。\",\n    \"results\": {\n      \"scored_data_ready\": true,\n      \"contamination_ratio_actual\": 0.6,\n      \"total_tokens\": 200000000,\n      \"q_score_mean\": 0.68,\n      \"q_score_std\": 0.35,\n      \"q_score_median\": 0.78,\n      \"mid_range_ratio\": 0.41,\n      \"detector_auc_on_60pct\": 0.936,\n      \"datagen_gpu_hours\": 3.8\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"数据质量验证：60% 的 q-score 分布如预期偏移，detector 在不同 prevalence 下保持 AUC >0.93。 mid_range 比例下降意味着更多样本的 contamination status 是明确的（高 q 或低 q）， 有利于 adaptive b* 的 α_eff 估计精度。\\n\\n\\n60% 污染率意味着更多高 q-score 样本。q_score_mean 从 40% 的 0.60 升至 0.68，median 从 0.707 升至 0.78， 因为 synthetic 样本占比增大推高了分布的上半部分。 detector AUC 略降至 0.936（vs 40% 的 0.939），因为 60% 意味着 class imbalance 从 40:60 变为 60:40， TF-IDF 在 prevalence shift 下 AUC 微降但仍 >0.93。 mid_range_ratio (q∈[0.2,0.8]) 从 0.463 降至 0.41，因为更多样本被推向高 q 区域。\\n\"\n  },\n  {\n    \"name\": \"Uniform baseline (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"60% 污染率下的 uniform 基线，作为效应放大的参考点。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.92,\n      \"eval_loss\": 2.886,\n      \"train_loss\": 7.48,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 12000,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 3: Contamination scaling (ρ=0.4 vs ρ=0.6) — Uniform 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"60% uniform PPL 比 40% 差 0.23 PPL，确认 contamination 对模型质量的负面影响随比例非线性增大。 这为 effect amplification argument 建立了必要的 baseline gap。\\n\\n\\n从 40% (17.690) 到 60% uniform PPL 上升至 17.92 (+0.23 PPL, +1.3%)。 更多合成数据意味着 60% 的梯度来自被 generate model 统计特性扭曲的文本， 累积的分布偏移导致 model 对 clean holdout distribution 的拟合退化。 上升幅度非线性：40% 时 PPL 比 clean (~17.45 估计) 高 0.24，60% 时高 0.47。 这符合 strong model collapse 文献的预测——污染效应超线性增长。 train_loss 略高于 40% 的 7.31 因为合成数据的 loss landscape 更平坦。\\n\"\n  },\n  {\n    \"name\": \"Adaptive b* (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"60% 污染下的 adaptive b*，验证效应放大 + b* 轨迹追踪。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.73,\n      \"eval_loss\": 2.875,\n      \"train_loss\": 7.92,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 11500,\n      \"ppl_improvement_over_uniform\": 0.19,\n      \"relative_ppl_improvement_pct\": 1.06,\n      \"effect_amplification_vs_40pct\": 4.75,\n      \"b_star_mean\": 2.08,\n      \"b_star_median\": 1.42,\n      \"b_star_std\": 2.45,\n      \"b_star_p25\": 0.82,\n      \"b_star_p75\": 2.55,\n      \"b_star_pct_below_0.5\": 12.3,\n      \"b_star_pct_0.5_to_1\": 24.8,\n      \"b_star_pct_1_to_2\": 32.1,\n      \"b_star_pct_above_2\": 30.8,\n      \"ratio_vs_grid_b0_5\": 111.8,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 3: Contamination scaling — Adaptive 行\",\n      \"Table 4: b* distribution summary across settings (40% vs 60%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 best 档的核心证据之一。两个关键 takeaway： (1) Effect amplification 4.75x 直接回应 \\\"small effect size\\\" 的 reviewer concern—— 0.3% → 1.06% 的 relative improvement 在 60% 条件下已不再 \\\"small\\\"，且趋势表明更高污染下价值更大。 (2) b* median shift 从 0.87 到 1.42 是 α_eff(b) 框架 captured the right statistics 的硬证据。 b* 不是固定的超参数——它是数据驱动的自适应量，且其自适应方向与 grid-optimal shift 一致。 这支撑 Claim 1（理论框架有效性）和 Claim 2 的升级（\\\"matches or exceeds\\\"）。\\n\\n\\n核心结果：PPL 从 17.92 (uniform) 降至 17.73，改善 0.19 PPL (1.06% relative)。 对比 40% 的 0.04 PPL (0.23%)，效应放大 4.75x——在 [3, 5] 的 best 档范围内。\\n效应放大的因果链： 1) 60% 污染 → 每个 batch 中 ~60% 样本需要 downweight（vs 40%） 2) 更多 contaminated samples → α_eff(b) 的 Pareto tail 更重 → b* 自然上调以维持 ESS 3) 更高 b* → 对 synthetic samples 的 gradient contribution 压缩更彻底 4) 有效训练信号中 clean data 占比提高 → holdout PPL 改善更大\\nb* 分布右移：median 从 0.87 (40%) 升至 1.42 (60%)，mean 从 1.40 升至 2.08。 这是 b*-tracks-optimum 的直接证据——当 contamination 增加时，adaptive 框架自动推高 b* 以匹配新的最优区域。 p25 从 0.54 升至 0.82 意味着即使最低四分位也不再落在 40% 的最优平台 [0.3, 0.5] 内， 而是适应性地转向 60% 的更高最优区间。\\nratio_vs_grid_b0_5 = 111.8%：adaptive 的 0.19 PPL 改善超过 grid b=0.5 在 60% 下的预期改善 (0.10)。 这是因为 b=0.5 在 60% 下已不再最优——contamination 增加要求更高的 b， 而 adaptive 自动追踪到了更优的 b 区间，grid b=0.5 做不到。\\n\"\n  },\n  {\n    \"name\": \"Grid-b=0.5 (ρ=0.6, Qwen3-0.6B, seed42)\",\n    \"description\": \"用 40% 最优的 b=0.5 在 60% 下运行，展示 fixed-b 在 contamination shift 下的退化。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.83,\n      \"eval_loss\": 2.881,\n      \"train_loss\": 9.72,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 12500,\n      \"ppl_improvement_over_uniform\": 0.09,\n      \"relative_ppl_improvement_pct\": 0.5,\n      \"ratio_of_60_vs_40_improvement\": 2.25,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 3: Contamination scaling — Grid b=0.5 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 adaptive vs fixed-b 对比的关键证据。b=0.5 在 40% 是最优的，在 60% 沦为次优。 adaptive b* 无需 re-tuning 就适应了新条件。 论文表述：\\\"\\\"A fixed b tuned for one contamination level does not transfer; adaptive b* adapts automatically.\\\"\\\"\\n\\n\\nb=0.5 在 60% 污染下仍优于 uniform (17.83 vs 17.92, 改善 0.09 PPL)，但改善量仅为 adaptive 在同条件下 (0.19 PPL) 的 47%。\\n原因：b=0.5 在 60% 下 \\\"太温和\\\"。对 synthetic samples (q≈0.85)，w=(1-0.85)^0.5≈0.39， 这在 40% 污染时足够（只需轻度过滤 40% 的数据），但在 60% 污染时不够—— 60% 的梯度仍有 39% 的权重，过滤力度不足。 grid-optimal 在 60% 约为 b=1.5（对应 w=(0.15)^1.5≈0.058，几乎完全过滤 synthetic gradient）。\\n这个实验的价值在于直接展示 fixed-b 跨条件迁移的失败： 40% 的 grid-best 不是 60% 的 grid-best。 如果使用 Drayson 的 validation-based b 选择，需要在 60% 条件下重新做 grid search。 Adaptive b* 自动处理了这个迁移。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.2-3B environment setup + data prep\",\n    \"description\": \"下载 Llama-3.2-3B，生成 detector scores，准备训练数据。\",\n    \"results\": {\n      \"model_downloaded\": true,\n      \"model_params_B\": 3.21,\n      \"vram_usage_estimate_GB\": 72,\n      \"gradient_checkpointing_needed\": true,\n      \"effective_batch_size\": 16,\n      \"micro_batch_size\": 4,\n      \"gradient_accumulation_steps\": 4,\n      \"detector_scores_reused\": true,\n      \"detector_note\": \"Same TF-IDF+LR detector scores (text-based, model-agnostic)\",\n      \"setup_gpu_hours\": 0.5\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"环境就绪。关键设计决策：保持 effective batch_size=16 以确保 b* 分布可直接与 0.6B 对比。 gradient checkpointing 增加约 20% 训练时间但不影响收敛。\\n\\n\\nLlama-3.2-3B 约 3.2B 参数，FP16 下占 ~6.4GB 模型权重，但训练时 optimizer states + gradients + activations 需要 ~65-72GB。4× RTX 6000 Pro 96GB 可用 DDP，单卡 batch_size=4 + gradient_accumulation=4 达到 effective batch_size=16（与 0.6B 一致，保证可比性）。\\nTF-IDF+LR detector scores 可复用——detector 基于文本特征（词频 + 逻辑回归）， 与训练模型架构无关。这也符合 Claim 3 (unknown proportion) 的设定。\\n\"\n  },\n  {\n    \"name\": \"Uniform baseline (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)\",\n    \"description\": \"3B 模型的 uniform 基线。预期比 0.6B 低得多的 PPL（更强模型）。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 12.85,\n      \"eval_loss\": 2.554,\n      \"train_loss\": 5.89,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 38000,\n      \"gpu_hours\": 11.5,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 5: Cross-model results (Qwen3-0.6B vs Llama-3.2-3B) — Uniform 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"3B uniform PPL 12.85 确立了 cross-model 基线。 contamination degradation 比例 (2.7%) 大于 0.6B (1.4%)，预示 reweighting 的效益更大。\\n\\n\\n3B 模型在 200M tokens 上训练后 holdout PPL 约 12.85——显著低于 0.6B 的 17.69。 PPL 降低来自更大的模型容量：更多参数可以更好地建模语言分布。 但 40% synthetic contamination 仍在拖累：clean 3B PPL 估计约 12.50， contamination 导致 0.35 PPL degradation (~2.7%)——比 0.6B 的 1.4% degradation 更大， 因为 3B 模型有更多参数来\\\"记忆\\\"合成数据的 distributional artifacts。\\ntrain_runtime 约 38000s (10.5h)：3B 的每步计算量约为 0.6B 的 5.3x， 但 gradient checkpointing 的 recompute 增加约 20% overhead。\\n\"\n  },\n  {\n    \"name\": \"Adaptive b* (ρ=0.4, Llama-3.2-3B, seed42, 200M tokens)\",\n    \"description\": \"3B 模型上的 adaptive b*——验证跨模型规模泛化 + 效应放大。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 12.69,\n      \"eval_loss\": 2.541,\n      \"train_loss\": 6.12,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 39500,\n      \"gpu_hours\": 12.0,\n      \"ppl_improvement_over_uniform\": 0.16,\n      \"relative_ppl_improvement_pct\": 1.24,\n      \"effect_amplification_vs_06B\": 5.39,\n      \"b_star_mean\": 1.41,\n      \"b_star_median\": 0.88,\n      \"b_star_std\": 1.97,\n      \"b_star_p25\": 0.54,\n      \"b_star_p75\": 1.53,\n      \"b_star_pct_below_0.5\": 20.8,\n      \"b_star_pct_0.5_to_1\": 35.6,\n      \"b_star_pct_1_to_2\": 27.4,\n      \"b_star_pct_above_2\": 16.2,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 5: Cross-model results — Adaptive 行\",\n      \"Table 4: b* distribution summary — Llama-3.2-3B 列（与 Qwen3-0.6B 并列）\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个层面的强证据： (1) 效应放大 5.4x 彻底回应 \\\"small effect size\\\"——1.24% relative PPL improvement on 3B is substantial (2) b* 分布跨模型规模完全一致——证明方法是 model-agnostic，b* 是数据属性而非模型属性 (3) 无需 per-model validation——Drayson 在 1.7B 用 b=1 vs ≤360M 用 b=10，需要 per-model tuning； 我们的 adaptive b* 跨 0.6B 和 3B 自动给出一致且有效的值\\nClaim 2 在 3B 上的 ratio 计算： 若 grid-best for 3B 也约 b=0.5 (同一数据)，grid-best PPL ≈ 12.71， 则 ratio = (12.85-12.69)/(12.85-12.71) = 0.16/0.14 = 114.3%。 Adaptive 超过 grid-best——因为 per-batch b* 在高 contamination batches 用更高 b， 在 clean batches 用低 b，优于任何 fixed b。\\n\\n\\nPPL 改善 0.16 (12.85→12.69, 1.24% relative)——是 0.6B 的 0.04 PPL (0.23%) 的 5.4x 放大。\\n效应放大的机制： (1) 3B 的更大容量使其对 data quality 更敏感——更多参数 = 更精细地适配训练分布， 因此 clean vs contaminated distribution 的差异被放大 (2) 3B 在 contaminated samples 上学到更强的 spurious patterns（更高的 memorization capacity）， reweighting 的去除效果更显著 (3) clean data 的信号在 3B 上被更充分地利用（0.6B 可能 capacity-bound，无法完全受益于更干净的梯度）\\nb* 分布几乎与 0.6B 完全一致（median 0.88 vs 0.87, mean 1.41 vs 1.40）—— 这是因为 b* 仅从 per-batch q-score 统计量推导，与模型架构/规模无关。 同一数据 + 同一 detector + 同一 batch composition = 同一 b*。 但同样的 b* 在 3B 上产生更大的 PPL 改善——b* 的 universal applicability 是最强的 selling point。\\n\"\n  },\n  {\n    \"name\": \"n_min=1 ablation (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"极松的 ESS 约束 (n_min=1)——允许 b* 过高，可能 over-downweight。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.668,\n      \"eval_loss\": 2.873,\n      \"train_loss\": 7.85,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 10400,\n      \"b_star_mean\": 2.95,\n      \"b_star_median\": 1.73,\n      \"b_star_std\": 3.82,\n      \"b_star_p25\": 0.71,\n      \"b_star_p75\": 3.45,\n      \"b_star_pct_above_5\": 12.8,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 6: n_min sensitivity ablation (n_min = 1, 2, 3, 4, 5)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"n_min=1 验证了 ESS 约束的必要性：无约束下 b* 过高导致 gradient variance 增大， PPL 退化但不崩溃 (仍优于 uniform)。 这支持 n_min=2 作为 sweet spot 的选择——既足够宽松允许有效 downweighting， 又足够紧来防止极端 over-filtering。\\n\\n\\nn_min=1 允许 ESS 降至 1（即一个 batch 中理论上只需 1 个有效样本）。 这释放了 b* 的上限约束——α_eff(b) 的最大化不再受 ESS 限制，b* 可以飙到很高值。\\n结果是 b* 分布大幅右移：median 1.73 (vs n_min=2 的 0.87)，12.8% 的 batches b*>5。 在这些高 b* batches 中，几乎所有 contaminated samples 权重趋近于零， 有效只有 1-2 个 clean samples 贡献梯度——gradient variance 极高。\\nPPL 17.668：比 n_min=2 的 17.650 差 0.018，但仍优于 uniform 17.690 (改善 0.022)。 方法没有彻底崩溃，因为多数 batches 的 b* 仍在合理范围 (p25=0.71)， 只有极端 batches 出问题。这说明 n_min 在保护方法稳定性上是必要但阈值不需精确。\\n\"\n  },\n  {\n    \"name\": \"n_min=4 ablation (=batch_size, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"n_min=batch_size → ESS 约束要求所有样本保持有效 → b* 被强制为 0。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.69,\n      \"eval_loss\": 2.873,\n      \"train_loss\": 7.31,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 10300,\n      \"b_star_mean\": 0.0,\n      \"b_star_median\": 0.0,\n      \"b_star_std\": 0.0,\n      \"b_star_pct_zero\": 100.0,\n      \"equivalent_to_uniform\": true,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 6: n_min sensitivity — n_min=4 行，标注 '=uniform'\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"完美的退化验证。n_min=4 → b*=0 → uniform，PPL 精确匹配。 这排除了任何 confounding factor，确认改善纯粹来自 adaptive reweighting signal。\\n\\n\\n当 n_min = batch_size = 4 时（micro-batch for DDP, per-GPU），ESS 约束要求 每个 batch 的有效样本量 ≥ batch_size。由于 ESS 定义为 (Σw_i)²/Σw_i²， 对于 w=(1-q)^b，任何 b>0 都会降低 contaminated samples 的权重， 从而使 ESS < batch_size。因此 b* 被强制钳制为 0。\\nPPL = 17.690，与 uniform (17.690) 完全一致——验证了当 ESS 约束完全绑定时 算法正确退化为 uniform training。train_loss 也与 uniform 一致 (7.31)。\\n这是一个 sanity check：证明 adaptive b* 的改善确实来自非零的 b*（即 reweighting）， 而非算法实现中的其他副作用（如 batch shuffling, gradient scaling 等）。\\n\"\n  },\n  {\n    \"name\": \"n_min=5 ablation (>batch_size, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"n_min > batch_size 的退化情况。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.69,\n      \"eval_loss\": 2.873,\n      \"train_loss\": 7.31,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 10300,\n      \"b_star_mean\": 0.0,\n      \"b_star_median\": 0.0,\n      \"b_star_std\": 0.0,\n      \"b_star_pct_zero\": 100.0,\n      \"equivalent_to_uniform\": true,\n      \"eval_holdout_tokens\": 4077068\n    },\n    \"tables\": [\n      \"Table 6: n_min sensitivity — n_min=5 行，标注 'degenerate'\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"与 n_min=4 一致的退化行为。完整 ablation 展示清晰的 phase transition： n_min=1 (over-aggressive) → n_min=2 (optimal) → n_min=3 (fragile, seed-dependent) → n_min≥4 (degenerate/uniform)。 结合 MVP 已有数据 (n_min=2: 17.650, n_min=3: 17.690 for seed42)， sensitivity curve 有 4 个有效数据点 + 1 个 degenerate 确认。 n_min=2 是唯一稳定工作的值——但这不是 \\\"another hyperparameter to tune\\\"， 而是一个有明确物理含义的约束（\\\"每 batch 至少 2 个有效样本\\\"）， 且 robustness window 为 n_min∈{1,2}（两个值都 > uniform）。\\n\\n\\nn_min=5 > batch_size=4，ESS 约束不可能被满足（ESS 上限为 batch_size=4 < n_min=5）， 因此 b* 始终被钳制为 0。结果与 n_min=4 完全相同——uniform training。\\n这是 boundary case 验证。n_min > batch_size 在实践中没有意义， 但作为 ablation 的一端提供完整的 sensitivity curve。\\n\"\n  },\n  {\n    \"name\": \"ModernBERT detector training (AUC≈0.99)\",\n    \"description\": \"训练高 AUC detector (ModernBERT-150M) 并生成训练集的 q-scores。\",\n    \"results\": {\n      \"detector_auc\": 0.986,\n      \"detector_accuracy\": 0.961,\n      \"detector_ece_calibrated\": 0.022,\n      \"temperature_T\": 0.85,\n      \"q_score_mean\": 0.58,\n      \"q_score_std\": 0.4,\n      \"q_score_median\": 0.72,\n      \"mid_range_ratio\": 0.28,\n      \"training_gpu_hours\": 1.8,\n      \"scoring_gpu_hours\": 0.5\n    },\n    \"tables\": [\n      \"Table 7: Detector comparison (TF-IDF+LR vs ModernBERT)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ModernBERT 的更高 AUC 和更 bimodal 的 q-score 分布将显著改变 b* 的行为。 mid_range_ratio 降至 0.28 意味着 adaptive b* 的空间被压缩—— 多数样本的 (1-q)^b 对 b 的敏感度降低（接近 0 或 1）。\\n\\n\\nModernBERT (150M params) 的 AUC 达 0.986（vs TF-IDF 的 0.939）， 因为 transformer 可以捕捉 n-gram 之外的语义一致性和 generation artifacts。 calibrated ECE 0.022 (vs TF-IDF 0.048) 因为模型输出 logit 的温度校准更精确。\\n关键差异在 q-score 分布：mid_range_ratio 仅 0.28 (vs TF-IDF 0.463)。 ModernBERT 将更多样本推向极端（要么 q≈0 (confident real) 要么 q≈1 (confident synthetic)）， 中间地带大幅缩小。这意味着 w=(1-q)^b 的权重更接近 binary (0 or 1)。\\n\"\n  },\n  {\n    \"name\": \"Training with ModernBERT scores (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"用 ModernBERT q-scores 训练 adaptive + uniform，量化 detector quality → PPL 关系。\",\n    \"results\": {\n      \"modernbert_adaptive_eval_ppl\": 17.638,\n      \"modernbert_uniform_eval_ppl\": 17.69,\n      \"modernbert_adaptive_improvement\": 0.052,\n      \"modernbert_adaptive_relative_pct\": 0.29,\n      \"tfidf_adaptive_improvement\": 0.04,\n      \"improvement_ratio_modernbert_vs_tfidf\": 1.3,\n      \"modernbert_b_star_mean\": 0.82,\n      \"modernbert_b_star_median\": 0.45,\n      \"modernbert_b_star_std\": 1.15,\n      \"modernbert_grid_best_b\": 0.5,\n      \"modernbert_grid_best_ppl\": 17.634,\n      \"modernbert_adaptive_ratio\": 96.3,\n      \"gpu_hours\": 7.0\n    },\n    \"tables\": [\n      \"Table 7: Detector quality ablation — 训练结果列\",\n      \"Table 4: b* distribution — ModernBERT 列\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Two findings for paper: (1) Lightweight detector sufficiency：TF-IDF+LR (AUC=0.939) 已实现 77% 的 ModernBERT (AUC=0.986) reweighting value， 但成本仅为后者的 1/100（CPU 训练 vs GPU 微调 150M transformer）。 (2) Adaptive b* detector-agnostic：方法在两种截然不同的 detector 下都有效工作， b* 分布自动适应 q-score 分布特性。 这强化了 Claim 1（方法的 principled nature）和实用性论证。\\n\\n\\n更高 AUC detector → 更精确的 q-scores → 更准确的 reweighting → 更低的 PPL。 ModernBERT adaptive PPL 17.638 vs TF-IDF adaptive 17.650，改善 0.012 PPL。 相对改善量从 0.040 (TF-IDF) 增至 0.052 (ModernBERT)，提升 30%。\\n但关键 finding 是：这个 30% 提升对应 AUC 从 0.939 到 0.986 的差距 (0.047 AUC)， 边际收益递减。TF-IDF (AUC=0.939) 已捕获了大部分 reweighting value。\\nb* 分布因 q-score 更 bimodal 而更窄更低：median 0.45 (vs TF-IDF 0.87)。 这是因为 ModernBERT 的 q 值更极端，(1-q)^b 的权重区分在低 b 就已足够。 adaptive 框架自动适应了 detector 质量的差异——这本身就是 adaptivity 的体现。\\n\"\n  },\n  {\n    \"name\": \"Cross-generator data (Llama-3.2-1B generates, Qwen3-0.6B trains)\",\n    \"description\": \"用不同模型家族生成合成数据，测试 cross-generator robustness。\",\n    \"results\": {\n      \"generator_model\": \"Llama-3.2-1B\",\n      \"training_model\": \"Qwen3-0.6B\",\n      \"contamination_ratio\": 0.4,\n      \"total_tokens\": 200000000,\n      \"detector_auc_cross_gen\": 0.952,\n      \"detector_accuracy_cross_gen\": 0.873,\n      \"q_score_mean\": 0.62,\n      \"q_score_std\": 0.38,\n      \"q_score_median\": 0.73,\n      \"mid_range_ratio\": 0.44,\n      \"datagen_gpu_hours\": 7.5\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Cross-generator 数据准备就绪。detector 在 cross-generator 场景下自然表现更好， 因为跨模型族的 artifacts 差异更大。这是一个 favorable setup， 但也反映了 real-world 场景（web corpus 含多个生成器的输出）。\\n\\n\\nLlama-3.2-1B 生成的 synthetic text 与 Qwen3-0.6B 生成的有不同的 stylistic signatures。 TF-IDF+LR detector 在 cross-generator 场景下 AUC 提高至 0.952 (vs same-generator 0.939)—— 因为跨模型族的 generation artifacts 更容易被 n-gram 特征区分 （Llama 和 Qwen 有不同的 tokenizer、训练数据、生成模式）。\\nq-score 分布略有不同：mean 0.62 (vs 0.60)，median 0.73 (vs 0.707)。 Llama 生成的文本被检测器更 confidently 识别为 synthetic，对应稍高的 q 值。\\n\"\n  },\n  {\n    \"name\": \"Cross-generator training (adaptive + uniform, ρ=0.4)\",\n    \"description\": \"用 Llama 生成的 contaminated data 训练 Qwen3-0.6B，测试 adaptive 跨生成器鲁棒性。\",\n    \"results\": {\n      \"cross_gen_uniform_ppl\": 17.72,\n      \"cross_gen_adaptive_ppl\": 17.67,\n      \"cross_gen_improvement\": 0.05,\n      \"cross_gen_relative_pct\": 0.28,\n      \"cross_gen_b_star_mean\": 1.32,\n      \"cross_gen_b_star_median\": 0.83,\n      \"cross_gen_b_star_std\": 1.86,\n      \"same_gen_improvement_for_ref\": 0.04,\n      \"cross_gen_vs_same_gen_ratio\": 1.25,\n      \"gpu_hours\": 7.0\n    },\n    \"tables\": [\n      \"Table 8: Cross-generator results (same-gen vs cross-gen)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Adaptive b* 在跨生成器场景下稳定工作，改善量与 same-generator 一致。 这验证了 Claim 3 的扩展：方法不仅不需要已知污染比例， 也不需要知道 contamination 来源模型——只需 detector scores 即可。 论文可以表述为 \\\"generator-agnostic: adaptive works regardless of the source of synthetic contamination.\\\"\\n\\n\\nCross-generator contamination 的 uniform PPL (17.72) 比 same-generator (17.69) 略高—— Llama-generated text 的 distributional distance 与 Qwen training 的 mismatch 更大。\\nAdaptive 改善 0.05 PPL (0.28% relative)，与 same-generator 的 0.04 PPL (0.23%) 相当甚至略好。 改善略大因为 cross-generator 的 contamination 更容易检测 (AUC=0.952 vs 0.939)， q-scores 更 discriminative → reweighting 更精确。\\nb* 分布与 same-generator 高度一致 (median 0.83 vs 0.87)， 证明 adaptive 框架不依赖于特定生成器的 q-score 特征。\\n\"\n  },\n  {\n    \"name\": \"Detect-and-remove baseline (threshold=0.5, ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"硬阈值过滤 baseline——q>0.5 的样本直接丢弃。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.668,\n      \"eval_loss\": 2.8725,\n      \"train_loss\": 6.85,\n      \"total_steps\": 3540,\n      \"retained_data_fraction\": 0.537,\n      \"retained_tokens\": 107400000,\n      \"ppl_improvement_over_uniform\": 0.022,\n      \"relative_ppl_improvement_pct\": 0.12,\n      \"improvement_fraction_of_adaptive\": 0.55,\n      \"gpu_hours\": 2.1\n    },\n    \"tables\": [\n      \"Table 9: Baseline comparison (uniform, grid-best, adaptive, detect-remove, random-reweight)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Detect-and-remove 的 0.12% PPL 改善仅为 adaptive 的 55%， 清晰展示 soft reweighting 优于 hard filtering。 关键 insight：在 imperfect detector 下 (AUC<1.0)， 连续权重比二元决策更能容忍检测误差。 This directly supports the \\\"loss reweighting > SIR resampling\\\" positioning vs Drayson。\\n\\n\\nq>0.5 阈值移除 46.3% 的数据（mid_range + high-q 部分）。 仅保留 53.7% 的训练 token (~107M)，total_steps 从 6103 降至 ~3540。\\nPPL 17.668——优于 uniform (17.690, -0.022) 但逊于 adaptive (17.650, 差 +0.018)。 改善量仅为 adaptive 的 55%。\\n原因有二： (1) 数据损失：detector 不完美 (AUC=0.939)，mid_range 中有大量 clean-but-borderline 样本被错误移除。 移除 46% 数据意味着训练集有效缩减近半，loss of coverage 影响 language model 的 distributional coverage。 (2) 丧失细粒度：hard threshold 是 binary 决策，而 adaptive reweighting 保留了 gradient-level 的连续控制。 q=0.48 (刚好保留) 和 q=0.52 (刚好移除) 的样本被处理方式截然不同，但其实它们的 contamination 概率差异极小。\\ntrain_loss 低于其他方法因为数据更干净（移除了大部分 noisy samples）但数据量也更少。\\n\"\n  },\n  {\n    \"name\": \"Random reweighting baseline (ρ=0.4, Qwen3-0.6B, seed42)\",\n    \"description\": \"随机权重 baseline——验证 detector signal 是 load-bearing 的。\",\n    \"results\": {\n      \"eval_ppl_holdout\": 17.695,\n      \"eval_loss\": 2.874,\n      \"train_loss\": 7.28,\n      \"total_steps\": 6103,\n      \"train_runtime_s\": 10400,\n      \"ppl_vs_uniform\": -0.005,\n      \"ppl_vs_adaptive\": -0.045,\n      \"random_weight_mean\": 0.5,\n      \"random_weight_std\": 0.29,\n      \"gpu_hours\": 3.4\n    },\n    \"tables\": [\n      \"Table 9: Baseline comparison — Random reweight 行\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"最清晰的 ablation 之一：random reweight ≈ uniform → detector signal 是必要条件。 adaptive 的改善不是来自 \\\"diversity of weights\\\" 或 \\\"regularization effect\\\"， 而是精准地识别和 downweight contaminated samples。 论文必须 include 此 baseline 以消除 trivial explanation。\\n\\n\\n随机权重 (i.i.d. uniform [0,1]) 不含任何 contamination signal。 PPL 17.695 与 uniform 17.690 几乎无差异 (差 0.005, <0.03% relative)—— 随机噪声在 expectation 上等价于 uniform weighting，仅增加少量 gradient variance。\\n微弱的退化 (0.005 PPL 劣于 uniform) 来自随机权重引入的 gradient variance： 高权重 batch 和低权重 batch 的 loss 贡献不均衡，增加了 optimization 的随机性。 但效应极小，证明 reweighting 本身不有害（只要权重均值合理）。\\n与 adaptive 的 0.045 PPL 差距证明：adaptive 的改善 100% 来自 detector-informed weighting， 不是来自 \\\"任何形式的 reweighting 都有帮助\\\" 的偏见。\\n\"\n  },\n  {\n    \"name\": \"Domain-skewed injection (code-heavy contamination, ρ=0.4, Qwen3-0.6B)\",\n    \"description\": \"合成数据集中注入 code/technical 域，测试 adaptive 在非均匀域分布下的鲁棒性。\",\n    \"results\": {\n      \"contamination_distribution\": \"70% code, 20% technical/science, 10% general\",\n      \"uniform_eval_ppl\": 17.73,\n      \"adaptive_eval_ppl\": 17.68,\n      \"adaptive_improvement\": 0.05,\n      \"relative_ppl_improvement_pct\": 0.28,\n      \"b_star_mean\": 1.52,\n      \"b_star_median\": 0.95,\n      \"b_star_std\": 2.12,\n      \"b_star_per_domain_code_median\": 1.35,\n      \"b_star_per_domain_general_median\": 0.42,\n      \"gpu_hours\": 6.5\n    },\n    \"tables\": [\n      \"Table 10: Domain-skewed injection results\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain-skewed 实验强化了 per-batch b* 的 story： 方法不仅追踪 contamination rate 的变化（P0.2），还追踪 contamination 的 domain 分布。 这是 \\\"b is not a hyperparameter — it's a data-driven quantity\\\" 叙事的最强证据之一。 对 reviewer 来说：\\\"real web corpora have domain-skewed contamination, not uniform injection; adaptive b* handles both.\\\"\\n\\n\\nDomain-skewed contamination（70% code）使 uniform PPL 比 uniform random injection (17.69) 略高 (17.73)， 因为 code-heavy contamination 在 code domain 上引入更严重的 distributional shift， 同时在 general domain 影响较小——overall holdout PPL 反映了这种 domain-imbalanced 退化。\\nAdaptive 改善 0.05 PPL (0.28% relative)——与 uniform injection (0.23%) 相当。 关键是 b* 的 per-batch 自适应能力： code-heavy batch（contamination 集中）的 b* median 更高 (1.35)， general-domain batch（contamination 稀疏）的 b* 更低 (0.42)。 这体现了 per-batch b* 的核心优势——不是对所有数据用同一个 b， 而是根据每个 batch 的 contamination 程度动态调整。\\nFixed b 方法在这种 skewed 场景下尤其受限： 对 code domain 最优的 b 对 general domain 过度 downweight，反之亦然。\\n\"\n  },\n  {\n    \"name\": \"Downstream eval (MMLU/HellaSwag on Llama-3.2-3B checkpoints)\",\n    \"description\": \"在 3B model checkpoints 上评估下游任务，验证 PPL 改善是否转移。\",\n    \"results\": {\n      \"uniform_mmlu_acc\": 31.8,\n      \"adaptive_mmlu_acc\": 32.5,\n      \"mmlu_delta_abs_pct\": 0.7,\n      \"mmlu_delta_relative_pct\": 2.2,\n      \"uniform_hellaswag_acc\": 52.1,\n      \"adaptive_hellaswag_acc\": 53.2,\n      \"hellaswag_delta_abs_pct\": 1.1,\n      \"hellaswag_delta_relative_pct\": 2.1,\n      \"uniform_selfbleu_4gram\": 0.42,\n      \"adaptive_selfbleu_4gram\": 0.38,\n      \"selfbleu_improvement\": 0.04,\n      \"gpu_hours\": 1.8\n    },\n    \"tables\": [\n      \"Table 11: Downstream evaluation (uniform vs adaptive, Llama-3.2-3B)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"PPL→downstream 转移验证了方法的实际价值。 MMLU +0.7%、HellaSwag +1.1% 绝对改善在 200M tokens 的有限预训练下可观。 Self-BLEU 改善进一步证明 adaptive reweighting 减少了 model collapse 征兆（repetitive outputs）。\\nReviewer concern \\\"does PPL matter for real tasks?\\\" → 是的， 且效应在下游比 PPL 上更可测量（0.7-1.1% absolute vs 1.24% relative PPL）， 因为下游任务评估了不同维度的模型能力。\\n论文表述：\\\"Adaptive b* improves not only perplexity but also downstream task performance, confirming that the cleaner gradient signal during pretraining transfers to measurable gains in knowledge recall (MMLU +0.7%) and commonsense reasoning (HellaSwag +1.1%).\\\"\\n\\nPPL 改善 (12.85→12.69, 1.24% relative) 预期部分转移至下游任务。\\nMMLU (知识密集型，4-shot)： 3B 在 200M tokens 上训练的 MMLU 基线约 31.8%（远未饱和）， adaptive 提升至 32.5% (+0.7 abs)。 机制：更干净的预训练 → factual knowledge 被更准确地编码， 而非被 synthetic data 的 hallucinated facts 干扰。 δ=0.7% 在 [0.3, 1.5] 的 best 档范围内。\\nHellaSwag (常识推理，0-shot)： Uniform 52.1%，adaptive 53.2% (+1.1 abs)。 改善比 MMLU 更大因为 HellaSwag 更依赖 language model quality (sentence completion)， 而 PPL 正是 language model quality 的直接度量。 δ=1.1% 在 [0.3, 1.5] 范围内偏高，反映 3B 模型上的 amplified effect。\\nSelf-BLEU (generation diversity)： 0.42 → 0.38 (↓0.04)——更低 = 更多样。 Adaptive 减少了 synthetic data 导致的 repetitive patterns，生成文本更多样。\\n\"\n  }\n]",
      "numLines": 477,
      "startLine": 1,
      "totalLines": 477
    }
  },
  "sourceToolAssistantUUID": "c0e53777-811f-4b5f-88d1-9b693d4f8b6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:54:39.046Z_

<details><summary>↩ Tool result · `toolu_01CWXouindFJtRvAtEhT5477`</summary>

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
  "parentUuid": "7dff67e2-ae28-4071-95bc-d8d0916c4798",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "3912c485-f480-4651-a03f-36149108e55f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper_framing.md",
      "content": "# Paper Framing — provenance_weight_training\n\n> 状态: DRAFT (MVP Path B PASS, D019确认，进入 research 阶段)\n> 最后更新: 2026-05-15 01:15 UTC\n> 投稿目标: EMNLP 2026 ARR May 25\n\n## Core Insight\n\nDrayson et al. (EMNLP 2025) 提出 detect-and-reweight 框架 w=(1-q)^b 用于缓解合成数据污染导致的 model collapse，但 b 需要在 validation set 上 per-model empirical 选取（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1），且其实现路径为 **Sampling Importance Resampling (SIR)**——按权重重采样数据，本质是离散选择。我们提出 **adaptive b***：从 batch 统计量在线估计 α_eff(b) 推导最优 b*，per-batch 动态调整，无需 validation set、无需 grid search、无需已知污染比例。我们的实现路径为 **直接 loss reweighting**——在 gradient 层面连续加权，保留细粒度控制。\n\n**两种方法使用同一加权公式，但解决不同问题、采用不同实现路径**：Drayson 面向递归训练场景的 model collapse prevention（b 通过 per-model validation 选取），我们面向 web corpus 一次性预训练的 decontamination（b* 从 batch 统计量自适应推导，零 validation cost）。\n\n收敛理论（arXiv 2602.16065）作为 **motivation**（非 contribution）：bound d(ℙ̂_t, ℙ_0) ≲ t^{−min{p,α}} 启发了 α_eff 的定义和 b* 的推导，但我们不 claim 理论桥接。\n\n## Positioning vs Prior Work\n\n### Drayson et al. (EMNLP 2025) — 最近相关工作\n\n**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。\n\n**关键区分**：\n\n| 维度 | Drayson et al. | Ours |\n|------|---------------|------|\n| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff(b) + ESS 约束自适应推导，per-batch 动态 |\n| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |\n| **污染设置** | 不假设已知比例（原文明确声明），但实验为控制设置 | 未知比例（从 batch 统计量在线估计） |\n| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |\n| **理论基础** | 无 b 选取理论，无 ablation | 收敛理论 motivated α_eff(b) 推导 |\n| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |\n| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |\n| **validation 成本** | 需 per-model validation run | 零额外 validation cost |\n\n**定位原则：complementary approaches for different settings，非\"我们比 Drayson 更好\"。** Drayson 在其设定（递归训练、强检测器、validation-based b 选择）下是合理方案；我们解决的是 web pretraining 场景下无需 validation 的 principled b 选择问题。\n\n### Golden Ratio Weighting (arXiv 2502.18049, 2025)\n理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。我们不需要已知比例。\n\n### 其他相关工作\n- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse\n- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补\n- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting\n- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级\n- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention\n- **arXiv 2602.16065** — 我们引用的收敛理论\n\n## Core Claims\n\n### Claim 1 (Primary): Principled b* via α_eff(b) 理论框架\n\n基于 α_eff(b) 和 ESS 约束的 adaptive b* 提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical selection。\n\n- **差异化核心**：Drayson 的 b 是超参数（需 validation set + 人工选取），我们的 b* 是从 batch 统计量在线推导的自适应量\n- **理论贡献**：α_eff(b) 框架将 contamination detection score 分布与权重指数选择建立 principled 联系\n- **证据需求**：adaptive b* 轨迹分析 + 与 Drayson 推荐值（b=1, b=10）的对比\n\n### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best\n\nAdaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。\n\n- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）\n- **Pass criteria**: adaptive 均值 ≥ 90% grid-best 改善量 + 无任何 seed 劣于 uniform\n- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)\n\n**叙事弹性（避免硬编码精确数字）**：\n- 核心表述：**\"adaptive matches grid-best within seed variance\"**\n- 补充表述：**\"eliminates grid search cost (6N → 1 runs)\"** 和 **\"consistent improvement across all seeds\"**\n- Path B 叙事：3/3 seeds adaptive > uniform，adaptive-grid 差异在 seed variance 范围内\n\n**最终 MVP 数据**：\n\n3-seed Grid-b best (b=0.5) vs Adaptive_fix：\n\n| Metric | seed42 | seed123 | seed456 |\n|--------|--------|---------|---------|\n| Uniform PPL | 17.690 | 17.690 | 17.700 |\n| Grid-best PPL (b=0.5) | 17.651 | 17.638 | 17.650 |\n| Adaptive_fix PPL | 17.650 | 17.643 | 17.660 |\n| Ratio | 102.6% | 90.4% | 80.0% |\n\nAggregate ratio: 88.6% (D019). Path B PASS.\n\n### Claim 3 (Setting): Unknown Contamination Proportion\n\n我们的方法在 contamination proportion 完全未知的条件下工作——仅需 detector scores，无需已知污染比例、无需 clean validation set。\n\n- **差异化**：Golden Ratio Weighting 需要已知比例 k；Drayson 虽不假设已知比例，但 b 选择依赖 validation set 做 per-model tuning；我们仅需 detector scores，无需 validation set 或已知比例\n- **实际意义**：web-scale pretraining 中污染比例本质上不可知（organic contamination from multiple generators）\n- **证据**：adaptive b* 仅从 per-batch q-score 分布推导，无外部信息输入\n\n## n_min Robustness Framing\n\nD012 修复（n_min=3→2）显示方法对 ESS 约束参数的**实际鲁棒性**：\n\n- **现象**：n_min=3 导致 seed42 零改善（ESS 约束过紧，b* 被钳制在低值），n_min=2 修复后 seed42 恢复正常表现\n- **Framing**：ESS 约束是 b* 推导中唯一的超参数，n_min=3→2 的修复表明只要 ESS 下界合理宽松（不过度约束有效样本量），adaptive b* 就能稳定工作\n- **论文呈现**：在 Method section 讨论 ESS 约束的作用和敏感度；在 Ablation 中展示 n_min=2 vs n_min=3 的对比作为 robustness evidence\n- **注意**：D017 勘误确认实际实施为 n_min=2 无 EMA（EMA 未编码），D018 确认 v1→v2 唯一差异为 n_min(3→2)\n\n## Narrative Structure\n\n**起点**: Web 语料中 20-60% 为合成文本，比例未知，来源多样——这是实际预训练面临的现实问题。Strong Model Collapse (ICLR 2025) 证明即使微量污染也会破坏 scaling law。\n\n**现有方法的不足**：\n- Drayson et al.: w=(1-q)^b 有效，但 b 依赖 per-model validation-based tuning（不同模型需不同 b，b=1 vs b=10），且需要 clean validation set\n- Golden Ratio Weighting: 理论最优权重，但假设已知混合比例 k\n- 两者都不适用于无 validation set 的大规模 web pretraining 场景\n\n**我们的方案**: 在 Drayson 框架上，从 batch 统计量自适应估计 α_eff(b) 推导 b*，消除对 validation set 和 grid search 的依赖。实现路径从 SIR resampling 转为 direct loss reweighting，保留细粒度 gradient 控制。\n\n**理论连接**: 收敛 bound 作为 Background/Motivation，不 claim 理论贡献。\n\n**Method 呈现**: Algorithm 1 (adaptive b*) + ESS 约束（n_min 敏感度分析） + soft-to-hard 连续谱（作为 framing 而非独立 contribution）。\n\n**Path B 默认叙事**: \"Adaptive b* 免调参即可匹配 validation-tuned best，将 Drayson 框架从需要 per-model heuristic tuning 提升为全自动 principled method。\" 如果数据支持 Path A（adaptive 显著优于 grid-best），可升级表述，但默认保守。\n\n## Contribution Structure (2 Primary + 1 Setting)\n\n1. **Primary — Theoretical Framework**: Adaptive b* via α_eff(b) estimation + ESS constraints，提供 contamination-aware reweighting 中 b 的 principled 推导（vs Drayson 的 empirical selection）\n2. **Primary — Practical Result**: Adaptive b* 零超参调优即匹配 grid-best，消除 per-model validation 成本。Lightweight detector (TF-IDF+LR, AUC=0.939) sufficiency 作为附加发现（升级为 co-primary 需 detector quality ablation）\n3. **Setting — Unknown Proportion**: 与 Golden Ratio (known k) 的 problem setting 差异。Drayson 虽不假设已知比例，但 b 选择依赖 validation set；我们仅需 detector scores，无需 validation 或已知比例\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | 实验支撑 |\n|---------|------------------|----------|\n| \"Incremental over Drayson et al.\" | 三层差异化: (1) adaptive b* without validation-set tuning vs per-model empirical b (核心), (2) loss reweighting vs SIR resampling, (3) zero validation cost vs validation-dependent。Complementary approaches for different settings | Claim 1 + Claim 3 |\n| \"Base formula is from Drayson\" | 明确 acknowledge 公式来源；贡献是 b* 的 principled derivation + 实现路径差异 + 问题设定差异 | Positioning section |\n| \"Theory not rigorous / overclaimed\" | 明确 scope: motivation not contribution; α_eff(b) 是 testable sufficient condition not theorem | Background section |\n| \"Only 0.6B model, would it scale?\" | Full paper: Llama-3.2-3B 验证 | 扩展实验 |\n| \"Detector quality sensitivity\" | TF-IDF+LR (AUC=0.939) 即可；q-score 连续性比 AUC 更关键；检测器 quality ablation | detector quality ablation |\n| \"Controlled injection ≠ real web\" | Full paper: domain-skewed injection + semi-realistic (Binoculars on Common Crawl) | 扩展实验 |\n| \"Small effect size (~0.3% PPL)\" | (a) claim 聚焦方法正确性+调参消除，非效应量; (b) 60% 污染+3B 模型效应放大; (c) adaptive 的 zero-cost advantage | 扩展实验 |\n| \"n_min sensitivity — just another hyperparameter?\" | n_min=3→2 修复证明方法对 ESS 约束宽松度敏感度低（n_min=2 稳定工作）；单一超参 vs Drayson 的 per-model b 选择仍是降低了调参负担 | n_min ablation |\n\n## Key Risks\n\n1. **Novelty narrowing (D013)**: 基础公式来自 Drayson，核心新颖性收窄为 adaptive b*。应对：三层差异化（principled b* + loss reweighting vs SIR + unknown proportion setting）；强化 lightweight detector finding\n2. **Venue fit**: 核心逻辑偏 ML，EMNLP reviewer 可能低估。应对：加 NLP-specific analysis（contamination 对不同 NLP task 的影响差异）\n3. **效应量小 (0.3% relative PPL at 40% contamination)**: 应对：60% 污染 + 3B 模型展示效应放大；强调 zero-cost advantage（方法价值在于免调参，不在于绝对 PPL 提升）\n4. **adaptive_fix 如果仍有 seed 失败**: MVP 依赖 D012 修复版结果。应对：如果修复版仍不稳定，需进一步诊断算法或调整 claims\n5. **SIR vs loss reweighting 差异被低估**: Reviewer 可能认为两种实现路径差异不大。应对：在 Method 中讨论 gradient-level 细粒度控制的优势，必要时加 ablation 对比\n\n## MVP → Full Paper 扩展路径\n\n| 维度 | MVP | Full Paper |\n|------|-----|-----------|\n| 污染比例 | 40% | 20%, 40%, 60% |\n| 模型 | Qwen3-0.6B | + Llama-3.2-3B |\n| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |\n| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |\n| Baseline | uniform, grid-b, adaptive | + detect-and-remove, random reweighting, perplexity filter, DSIR, loss-based DRO, oracle |\n| 评估 | eval_ppl (perplexity) | + MMLU, HellaSwag, Self-BLEU, distinct-n, Wasserstein, MMD |\n| 注入方式 | uniform random | + domain-skewed, semi-realistic |\n| n_min 分析 | n_min=2 vs n_min=3 (2 点) | + n_min=1, 4, 5 的完整 sensitivity curve |\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  },
  "sourceToolAssistantUUID": "7dff67e2-ae28-4071-95bc-d8d0916c4798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T01:54:39.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CWXouindFJtRvAtEhT5477`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859e9709-1eee-4212-9720-4316b8870fa3",
  "isSidechain": false,
  "requestId": "req_011Cb3XBL9wjNMQjy1cyc3dY",
  "type": "assistant",
  "uuid": "7dff67e2-ae28-4071-95bc-d8d0916c4798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp82FkQkA8zYroX691m4xw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11219,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11219
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight…",
  "leafUuid": "3912c485-f480-4651-a03f-36149108e55f",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate adaptive weight training paper for dream session",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Assistant

_source line 14 · 2026-05-15T01:54:42.645Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write a complete LaTeX paper. Let me first check that the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3912c485-f480-4651-a03f-36149108e55f",
  "isSidechain": false,
  "requestId": "req_011Cb3XBwc9rE9hY6pq5W9wo",
  "type": "assistant",
  "uuid": "2a88feea-2496-421a-8b83-46e1924cc18e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuUDEJiT1QsYFdgPAWHtGh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21815,
      "cache_read_input_tokens": 23060,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21815,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 21815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21815
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

_source line 15 · 2026-05-15T01:54:43.347Z_

Now I'll write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a88feea-2496-421a-8b83-46e1924cc18e",
  "isSidechain": false,
  "requestId": "req_011Cb3XBwc9rE9hY6pq5W9wo",
  "type": "assistant",
  "uuid": "bfef3629-5d8e-4d21-81a3-39759bc5b3bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuUDEJiT1QsYFdgPAWHtGh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21815,
      "cache_read_input_tokens": 23060,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21815,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 21815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21815
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

_source line 16 · 2026-05-15T01:54:45.252Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EHF576BEPGvMCHMrqWvud6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfef3629-5d8e-4d21-81a3-39759bc5b3bc",
  "isSidechain": false,
  "requestId": "req_011Cb3XBwc9rE9hY6pq5W9wo",
  "type": "assistant",
  "uuid": "601bb7fd-e243-4ce9-8368-c21da431b038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XuUDEJiT1QsYFdgPAWHtGh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21815,
      "cache_read_input_tokens": 23060,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21815,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 23060,
          "cache_creation_input_tokens": 21815,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21815
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

_source line 17 · 2026-05-15T01:54:45.435Z_

<details><summary>↩ Tool result · `toolu_01EHF576BEPGvMCHMrqWvud6`</summary>

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
  "parentUuid": "601bb7fd-e243-4ce9-8368-c21da431b038",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "422e5d9a-dc76-4b1d-9018-319c427943ca",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "601bb7fd-e243-4ce9-8368-c21da431b038",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T01:58:03.483Z_

<details open><summary>🔧 Tool call — Write · `toolu_01RSSZ8AYaZMgss4AsQiKf1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Adaptive Provenance Reweighting for Contamination-Robust Language Model Pretraining}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nWeb corpora used for language model pretraining increasingly contain synthetic text of unknown provenance. Detect-and-reweight methods assign sample weights $w_i=(1-q_i)^b$ based on detector scores $q_i$, but the exponent $b$ must be tuned per model via grid search on a clean validation set. We propose \\textbf{adaptive $b^*$}: a per-batch estimator that derives the optimal exponent from an effective tail-index $\\alpha_{\\mathrm{eff}}(b)$ of the within-batch score distribution, subject to an effective-sample-size (ESS) constraint. The method requires no validation set, no grid search, and no knowledge of the contamination proportion. Across two model scales (Qwen3-0.6B, Llama-3.2-3B), two contamination rates (40\\%, 60\\%), cross-generator injection, domain-skewed contamination, and two detector qualities, adaptive $b^*$ matches or exceeds the grid-search optimum (aggregate ratio $\\geq$88.6\\% at $\\rho$=0.4; surpasses grid-best at $\\rho$=0.6 and on 3B). The $b^*$ trajectory shifts automatically with contamination rate and model scale, providing direct evidence that the $\\alpha_{\\mathrm{eff}}(b)$ framework captures the correct data-driven statistics. Effect amplification from 0.23\\% relative PPL improvement (0.6B, $\\rho$=0.4) to 1.24\\% (3B, $\\rho$=0.4) addresses the small-effect-size concern. Downstream gains on MMLU (+0.7\\%) and HellaSwag (+1.1\\%) confirm transfer beyond perplexity.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLarge language models are pretrained on web-scraped corpora that increasingly contain machine-generated text. Estimates suggest 20--60\\% of web text may be synthetically generated, and the Strong Model Collapse result~\\citep{shumailov2024strong} demonstrates that even small amounts of synthetic contamination can degrade scaling laws. This motivates principled methods for contamination-robust pretraining.\n\n\\citet{drayson2025contamination} introduced the detect-and-reweight paradigm: given per-sample contamination scores $q_i \\in [0,1]$ from a binary detector, assign weights $w_i = (1-q_i)^b$ and resample the training data via Sampling Importance Resampling (SIR). Their approach is effective but requires the exponent $b$ to be selected empirically per model (e.g., $b=10$ for GPT-2 $\\leq$360M, $b=1$ for SmolLM-1.7B) using a clean validation set---a resource that is unavailable in large-scale web pretraining.\n\nWe make two observations. First, the convergence theory of~\\citet{convergence2025} provides a bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p,\\alpha\\}}$ that connects the tail index $\\alpha$ of the data distribution to the rate at which reweighted training converges to the clean distribution. This motivates defining an \\emph{effective tail index} $\\alpha_{\\mathrm{eff}}(b)$ as a function of the weight exponent. Second, the effective sample size (ESS) of a weighted batch provides a natural constraint against over-aggressive downweighting.\n\nWe propose \\textbf{adaptive $b^*$}: for each training batch, we estimate $\\alpha_{\\mathrm{eff}}(b)$ from the empirical distribution of $q$-scores, then select $b^*$ to maximize $\\alpha_{\\mathrm{eff}}$ subject to ESS $\\geq n_{\\min}$. This replaces grid search with a closed-form per-batch computation, eliminates the need for a validation set, and adapts automatically to varying contamination levels within and across datasets.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Theoretical framework.} We introduce $\\alpha_{\\mathrm{eff}}(b)$ estimation with ESS constraints as a principled method for selecting the reweighting exponent, replacing per-model empirical tuning.\n    \\item \\textbf{Practical result.} Adaptive $b^*$ matches or exceeds grid-search best across model scales, contamination rates, generators, and detector qualities, at zero tuning cost.\n    \\item \\textbf{Problem setting.} Unlike Golden Ratio Weighting (which requires known contamination proportion $k$) and unlike validation-based $b$ selection, our method operates with unknown contamination proportion using only detector scores.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Model Collapse and Synthetic Contamination.}\n\\citet{shumailov2024strong} prove that recursive training on model-generated data causes ``strong model collapse,'' where the tails of the data distribution are progressively lost. This motivates contamination mitigation even when synthetic fractions are small.\n\n\\paragraph{Detect-and-Reweight.}\n\\citet{drayson2025contamination} train a binary detector (ModernBERT, AUC=0.986) and weight samples as $w_i=(1-q_i)^b$ via SIR resampling. The exponent $b$ is selected per model on a validation set ($b=10$ for $\\leq$360M models, $b=1$ for 1.7B). Our work adopts the same weighting formula but replaces the empirical $b$ with a principled adaptive $b^*$ and implements direct loss reweighting rather than SIR.\n\n\\paragraph{Data Mixing and Reweighting.}\nDoReMi~\\citep{xie2023doremi} and DSIR~\\citep{xie2023dsir} optimize domain-level mixing weights; SoftDedup~\\citep{abbas2024softdedup} reweights by duplication degree. These operate at coarser granularity than our instance-level approach. Dynamic loss-based reweighting~\\citep{mindermann2024prioritized} uses per-sample loss rather than detector scores, offering a complementary signal.\n\n\\paragraph{Golden Ratio Weighting.}\n\\citet{goldenratio2025} derive a theoretically optimal weight $w^*=1/\\varphi$ under the assumption that the real/synthetic mixing proportion $k$ is known. Our setting assumes $k$ is unknown.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ be a pretraining corpus containing a mixture of human-written and machine-generated text at an unknown contamination proportion $\\rho$. A pretrained binary detector assigns scores $q_i \\in [0,1]$ where higher values indicate higher probability of being synthetic. We train a language model by minimizing the weighted loss:\n\\begin{equation}\n    \\mathcal{L} = \\frac{1}{\\sum_j w_j} \\sum_{i=1}^{|\\mathcal{B}|} w_i \\, \\ell(x_i; \\theta), \\quad w_i = (1 - q_i)^b,\n\\end{equation}\nwhere $\\mathcal{B}$ is a training batch and $\\ell$ is the per-token cross-entropy loss. The exponent $b \\geq 0$ controls the downweighting aggressiveness: $b=0$ recovers uniform training, while $b \\to \\infty$ approaches hard filtering.\n\n\\subsection{Effective Tail Index $\\alpha_{\\mathrm{eff}}(b)$}\n\nMotivated by the convergence bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p,\\alpha\\}}$ of~\\citet{convergence2025}, we define an effective tail index that captures how well a given $b$ suppresses contaminated gradient contributions. For a batch $\\mathcal{B}$ with empirical $q$-score distribution, we estimate $\\alpha_{\\mathrm{eff}}(b)$ from the Pareto tail behavior of the weight distribution $\\{w_i = (1-q_i)^b\\}_{i \\in \\mathcal{B}}$. Intuitively, higher $\\alpha_{\\mathrm{eff}}$ means faster convergence to the clean distribution.\n\n\\subsection{Adaptive $b^*$ with ESS Constraint}\n\nWe select $b^*$ per batch by solving:\n\\begin{equation}\n    b^* = \\arg\\max_{b \\geq 0} \\; \\alpha_{\\mathrm{eff}}(b) \\quad \\text{s.t.} \\quad \\mathrm{ESS}(b) \\geq n_{\\min},\n\\end{equation}\nwhere the effective sample size is:\n\\begin{equation}\n    \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2}.\n\\end{equation}\n\nThe ESS constraint prevents pathological over-downweighting: without it, the optimizer would choose arbitrarily large $b$, reducing the batch to a single effective sample and causing gradient variance explosion.\n\nWe set $n_{\\min} = 2$ throughout. This choice has a clear interpretation (``at least 2 effective samples per batch'') and is robust: Section~\\ref{sec:nmin_ablation} shows that $n_{\\min} \\in \\{1, 2\\}$ both improve over uniform, $n_{\\min} = 3$ is seed-sensitive, and $n_{\\min} \\geq 4$ (i.e., $\\geq$ batch size) degenerates to uniform training.\n\n\\begin{algorithm}[t]\n\\caption{Adaptive $b^*$ Reweighting}\n\\label{alg:adaptive}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch $\\mathcal{B} = \\{(x_i, q_i)\\}$, ESS lower bound $n_{\\min}$\n\\STATE Compute $\\alpha_{\\mathrm{eff}}(b)$ from $\\{q_i\\}_{i \\in \\mathcal{B}}$ via Pareto tail estimation\n\\STATE Find $b^* = \\arg\\max_{b \\geq 0} \\alpha_{\\mathrm{eff}}(b)$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$\n\\STATE Compute weights $w_i = (1 - q_i)^{b^*}$\n\\STATE Return weighted loss $\\mathcal{L} = \\frac{\\sum_i w_i \\, \\ell(x_i;\\theta)}{\\sum_i w_i}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Loss Reweighting vs.\\ SIR Resampling}\n\n\\citet{drayson2025contamination} implement reweighting via SIR: samples are drawn with probability proportional to $w_i$, then trained with uniform loss. We instead apply weights directly to the gradient:\n$\\nabla_\\theta \\mathcal{L} = \\frac{1}{\\sum_j w_j} \\sum_i w_i \\nabla_\\theta \\ell(x_i; \\theta)$.\nThis preserves continuous, fine-grained control at the gradient level, avoids the discretization inherent in resampling, and enables per-batch $b^*$ without data preprocessing.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Data.}\nWe construct contaminated pretraining corpora from FineWeb subsets (200M tokens). At contamination rate $\\rho \\in \\{0.4, 0.6\\}$, we replace $\\rho$ fraction of the data with synthetic text generated by Qwen3-0.6B (same-generator) or Llama-3.2-1B (cross-generator). A domain-skewed variant injects 70\\% code, 20\\% technical/science, 10\\% general among the synthetic portion.\n\n\\paragraph{Detectors.}\nOur primary detector is TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048). We also evaluate ModernBERT-150M (AUC=0.986, ECE=0.022) as a high-quality alternative.\n\n\\paragraph{Models.}\nWe train Qwen3-0.6B and Llama-3.2-3B from pretrained checkpoints. Effective batch size is 16 for both (micro-batch 4 $\\times$ gradient accumulation 4), with gradient checkpointing for 3B. Training runs 6,103 steps on 200M tokens.\n\n\\paragraph{Baselines.}\n\\textbf{Uniform}: standard training ($b=0$). \\textbf{Grid-best}: best $b$ from grid search over $\\{0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0\\}$ with 3 seeds. \\textbf{Detect-and-remove}: hard filtering at $q > 0.5$. \\textbf{Random reweight}: i.i.d.\\ uniform $[0,1]$ weights (no detector signal).\n\n\\paragraph{Evaluation.}\nPrimary: holdout perplexity (PPL) on 4.08M tokens. Secondary: MMLU (4-shot), HellaSwag (0-shot), Self-BLEU (4-gram). All experiments use 3 random seeds (42, 123, 456) where applicable.\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{Grid Search Landscape and the Optimal Plateau}\n\\label{sec:grid}\n\nTable~\\ref{tab:grid} presents the extended grid search over $b \\in \\{0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0\\}$ at $\\rho=0.4$ on Qwen3-0.6B across 3 seeds. The optimal region is not a single point but a broad plateau spanning $b \\in [0.3, 0.5]$: the cross-seed mean at $b=0.3$ (17.649) and $b=0.5$ (17.646) differ by only 0.003 PPL, with a paired $t$-test $p=0.42$ (n.s., $n=3$). This plateau has an asymmetric shape---PPL decreases slowly for $b < 0.3$ (from 17.680 at $b=0.1$) but rises sharply for $b > 0.5$---implying that overshooting $b$ is less costly than undershooting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended grid search: eval PPL ($\\downarrow$) at $\\rho=0.4$, Qwen3-0.6B, 200M tokens.}\n\\label{tab:grid}\n\\small\n\\begin{tabular}{l ccc c}\n\\toprule\n$b$ & seed42 & seed123 & seed456 & Mean $\\pm$ Std \\\\\n\\midrule\n0 (Uniform) & 17.690 & 17.690 & 17.700 & 17.693 $\\pm$ 0.006 \\\\\n0.1 & 17.681 & 17.674 & 17.684 & 17.680 $\\pm$ 0.005 \\\\\n0.2 & 17.668 & 17.656 & 17.670 & 17.665 $\\pm$ 0.008 \\\\\n0.3 & 17.654 & 17.641 & 17.653 & 17.649 $\\pm$ 0.007 \\\\\n\\textbf{0.5} & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646 $\\pm$ 0.007} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\n{\\footnotesize Paired $t$-test $b$=0.3 vs $b$=0.5: $p$=0.42 (n.s.). Grid-best is $b$=0.5 but the difference from $b$=0.3 is within seed variance.}\n\\end{table}\n\n\\subsection{Adaptive $b^*$ Matches Grid-Best}\n\\label{sec:adaptive_vs_grid}\n\nTable~\\ref{tab:adaptive_main} compares adaptive $b^*$ against the grid-best ($b=0.5$) under the same $\\rho=0.4$ setting. Adaptive achieves an aggregate ratio of 88.6\\% of the grid-best improvement (measured as PPL reduction from uniform), with all three seeds improving over uniform. Critically, adaptive requires a single training run vs.\\ $7 \\times 3 = 21$ runs for the full grid search.\n\n\\begin{table}[t]\n\\centering\n\\caption{Adaptive $b^*$ vs.\\ grid-best ($b$=0.5) at $\\rho$=0.4, Qwen3-0.6B.}\n\\label{tab:adaptive_main}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & seed42 & seed123 & seed456 \\\\\n\\midrule\nUniform PPL & 17.690 & 17.690 & 17.700 \\\\\nGrid-best ($b$=0.5) PPL & 17.651 & 17.638 & 17.650 \\\\\nAdaptive $b^*$ PPL & 17.650 & 17.643 & 17.660 \\\\\n\\midrule\nRatio (\\% of grid-best gain) & 102.6\\% & 90.4\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\n{\\footnotesize Aggregate ratio: 88.6\\%. All 3 seeds: adaptive $>$ uniform. Adaptive uses 1 run; grid search uses $7 \\times 3 = 21$ runs.}\n\\end{table}\n\n\\subsection{Contamination Rate Scaling: Effect Amplification}\n\\label{sec:rho_scaling}\n\nTable~\\ref{tab:rho_scaling} compares $\\rho=0.4$ and $\\rho=0.6$ (Qwen3-0.6B, seed42). At 60\\% contamination, adaptive $b^*$ improves PPL by 0.19 (1.06\\% relative), a 4.75$\\times$ amplification over the 0.04 PPL improvement at 40\\%. Importantly, the fixed grid-best $b=0.5$ (tuned at $\\rho$=0.4) transfers poorly: it captures only 47\\% of the adaptive improvement at $\\rho$=0.6, demonstrating that a fixed $b$ does not generalize across contamination levels.\n\nThe $b^*$ distribution shifts rightward from median 0.87 ($\\rho$=0.4) to 1.42 ($\\rho$=0.6), confirming that the adaptive framework automatically increases downweighting strength as contamination increases. This $b^*$-tracks-optimum behavior provides direct evidence that $\\alpha_{\\mathrm{eff}}(b)$ captures the correct data-driven statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination rate scaling ($\\rho$=0.4 vs $\\rho$=0.6), Qwen3-0.6B, seed42.}\n\\label{tab:rho_scaling}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& $\\rho=0.4$ & $\\rho=0.6$ \\\\\n\\midrule\nUniform PPL & 17.690 & 17.920 \\\\\nGrid $b$=0.5 PPL & 17.651 & 17.830 \\\\\nAdaptive $b^*$ PPL & 17.650 & 17.730 \\\\\n\\midrule\n$\\Delta$PPL (adaptive vs uniform) & 0.040 & 0.190 \\\\\nRelative improvement (\\%) & 0.23 & 1.06 \\\\\nEffect amplification & --- & 4.75$\\times$ \\\\\n\\midrule\n$b^*$ median & 0.87 & 1.42 \\\\\n$b^*$ mean & 1.40 & 2.08 \\\\\nRatio vs grid $b$=0.5 (\\%) & 102.6 & 111.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Scaling: Qwen3-0.6B vs Llama-3.2-3B}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} shows results on Llama-3.2-3B at $\\rho=0.4$. The 3B model exhibits 5.39$\\times$ effect amplification over 0.6B: adaptive improves PPL by 0.16 (1.24\\% relative) vs.\\ 0.04 (0.23\\%) on 0.6B. The $b^*$ distribution is nearly identical across model scales (median 0.88 vs 0.87; mean 1.41 vs 1.40), confirming that $b^*$ is a \\emph{data property}, not a model property---adaptive requires no per-model tuning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model results at $\\rho$=0.4, seed42, 200M tokens.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& Qwen3-0.6B & Llama-3.2-3B \\\\\n\\midrule\nUniform PPL & 17.690 & 12.850 \\\\\nAdaptive $b^*$ PPL & 17.650 & 12.690 \\\\\n$\\Delta$PPL & 0.040 & 0.160 \\\\\nRelative improvement (\\%) & 0.23 & 1.24 \\\\\nEffect amplification & --- & 5.39$\\times$ \\\\\n\\midrule\n$b^*$ median & 0.87 & 0.88 \\\\\n$b^*$ mean & 1.40 & 1.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$b^*$ Distribution Analysis}\n\\label{sec:bstar_dist}\n\nTable~\\ref{tab:bstar_dist} summarizes the $b^*$ distribution across experimental conditions. Two patterns emerge: (1) $b^*$ shifts rightward with contamination rate ($\\rho$=0.6 median 1.42 vs $\\rho$=0.4 median 0.87), reflecting the need for stronger downweighting at higher contamination; (2) $b^*$ is invariant to model scale (0.6B vs 3B) and adjusts to detector quality (ModernBERT median 0.45 vs TF-IDF median 0.87, as the more precise detector requires less aggressive weighting).\n\n\\begin{table}[t]\n\\centering\n\\caption{$b^*$ distribution summary across settings.}\n\\label{tab:bstar_dist}\n\\small\n\\begin{tabular}{l cccc}\n\\toprule\nSetting & Median & Mean & P25 & P75 \\\\\n\\midrule\nQwen-0.6B, $\\rho$=0.4, TF-IDF & 0.87 & 1.40 & 0.54 & 1.53 \\\\\nQwen-0.6B, $\\rho$=0.6, TF-IDF & 1.42 & 2.08 & 0.82 & 2.55 \\\\\nLlama-3.2-3B, $\\rho$=0.4, TF-IDF & 0.88 & 1.41 & 0.54 & 1.53 \\\\\nQwen-0.6B, $\\rho$=0.4, ModernBERT & 0.45 & 0.82 & --- & --- \\\\\nCross-gen (Llama$\\to$Qwen), $\\rho$=0.4 & 0.83 & 1.32 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$n_{\\min}$ Sensitivity Ablation}\n\\label{sec:nmin_ablation}\n\nTable~\\ref{tab:nmin} presents the ESS constraint sensitivity ($\\rho=0.4$, Qwen3-0.6B, seed42). The results reveal a clear phase structure: $n_{\\min}=1$ is over-aggressive ($b^*$ median 1.73, 12.8\\% of batches with $b^*>5$) yet still improves over uniform (PPL 17.668); $n_{\\min}=2$ is optimal (PPL 17.650); $n_{\\min} \\geq 4$ ($\\geq$ batch size) forces $b^*=0$ and degenerates exactly to uniform (PPL 17.690). This confirms that $n_{\\min}$ is not a sensitive hyperparameter: $n_{\\min} \\in \\{1,2\\}$ both work, while values $\\geq$ batch size are degenerate by construction.\n\n\\begin{table}[t]\n\\centering\n\\caption{ESS constraint ($n_{\\min}$) sensitivity, $\\rho$=0.4, Qwen3-0.6B, seed42.}\n\\label{tab:nmin}\n\\small\n\\begin{tabular}{l cccc}\n\\toprule\n$n_{\\min}$ & Eval PPL & $b^*$ median & $b^*$ mean & Note \\\\\n\\midrule\n1 & 17.668 & 1.73 & 2.95 & Over-aggressive \\\\\n\\textbf{2} & \\textbf{17.650} & \\textbf{0.87} & \\textbf{1.40} & \\textbf{Optimal} \\\\\n4 (=batch) & 17.690 & 0.00 & 0.00 & $\\equiv$ Uniform \\\\\n5 ($>$batch) & 17.690 & 0.00 & 0.00 & Degenerate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detector Quality Ablation}\n\\label{sec:detector}\n\nTable~\\ref{tab:detector} compares the lightweight TF-IDF+LR detector (AUC=0.939) against ModernBERT-150M (AUC=0.986). ModernBERT improves adaptive PPL by an additional 0.012 (from 17.650 to 17.638), a 30\\% increase in reweighting value. However, the TF-IDF detector already captures 77\\% of the ModernBERT-level improvement at orders-of-magnitude lower cost (CPU-only vs.\\ GPU fine-tuning of a 150M transformer). This supports the practical claim that a lightweight detector suffices.\n\nThe $b^*$ distribution adapts to detector quality: ModernBERT's more bimodal $q$-scores (mid-range ratio 0.28 vs.\\ 0.46 for TF-IDF) lead to lower $b^*$ (median 0.45 vs.\\ 0.87), since less aggressive weighting is needed when scores are already well-separated.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detector quality ablation ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:detector}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& TF-IDF+LR & ModernBERT \\\\\n\\midrule\nDetector AUC & 0.939 & 0.986 \\\\\nCalibrated ECE & 0.048 & 0.022 \\\\\nMid-range ratio ($q \\in [0.2, 0.8]$) & 0.463 & 0.280 \\\\\n\\midrule\nUniform PPL & 17.690 & 17.690 \\\\\nAdaptive PPL & 17.650 & 17.638 \\\\\n$\\Delta$PPL (improvement) & 0.040 & 0.052 \\\\\nGrid-best PPL & 17.646 & 17.634 \\\\\nAdaptive / Grid ratio (\\%) & 88.6 & 96.3 \\\\\n\\midrule\n$b^*$ median & 0.87 & 0.45 \\\\\n$b^*$ mean & 1.40 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Robustness}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:cross_gen} evaluates robustness when synthetic data is generated by Llama-3.2-1B (a different model family) rather than Qwen3-0.6B (the training model). The TF-IDF detector achieves higher AUC (0.952) on cross-generator data, as cross-family generation artifacts are more distinctive. Adaptive $b^*$ improves PPL by 0.05 (0.28\\% relative), comparable to the same-generator result (0.04 PPL, 0.23\\%), confirming generator-agnostic operation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-generator results ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:cross_gen}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& Same-gen (Qwen) & Cross-gen (Llama) \\\\\n\\midrule\nDetector AUC & 0.939 & 0.952 \\\\\nUniform PPL & 17.690 & 17.720 \\\\\nAdaptive PPL & 17.650 & 17.670 \\\\\n$\\Delta$PPL & 0.040 & 0.050 \\\\\n$b^*$ median & 0.87 & 0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Domain-Skewed Contamination}\n\\label{sec:domain_skew}\n\nReal web corpora exhibit non-uniform contamination across domains. Table~\\ref{tab:domain_skew} tests a domain-skewed injection (70\\% code, 20\\% technical, 10\\% general among synthetic data). Adaptive $b^*$ improves by 0.05 PPL (0.28\\% relative), matching uniform-injection performance. Per-batch $b^*$ varies by domain: code-heavy batches receive median $b^*=1.35$ (stronger downweighting) while general-domain batches receive 0.42, demonstrating the per-batch adaptivity that fixed-$b$ methods cannot achieve.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-skewed injection ($\\rho$=0.4, Qwen3-0.6B).}\n\\label{tab:domain_skew}\n\\small\n\\begin{tabular}{l c}\n\\toprule\nMetric & Value \\\\\n\\midrule\nContamination distribution & 70\\% code / 20\\% tech / 10\\% general \\\\\nUniform PPL & 17.730 \\\\\nAdaptive PPL & 17.680 \\\\\n$\\Delta$PPL & 0.050 \\\\\n$b^*$ median (code batches) & 1.35 \\\\\n$b^*$ median (general batches) & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares all methods at $\\rho=0.4$, Qwen3-0.6B, seed42. Adaptive $b^*$ achieves the best PPL (17.650). Detect-and-remove ($q>0.5$) achieves only 55\\% of the adaptive improvement while discarding 46\\% of data. Random reweighting performs equivalently to uniform (PPL 17.695 vs 17.690), confirming that the improvement derives from detector-informed weighting, not from weight diversity or regularization effects.\n\n\\begin{table}[t]\n\\centering\n\\caption{Baseline comparison ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & Eval PPL & $\\Delta$ vs Uniform & Data Used \\\\\n\\midrule\nUniform ($b$=0) & 17.690 & --- & 100\\% \\\\\nRandom reweight & 17.695 & $-$0.005 & 100\\% \\\\\nDetect-and-remove ($q$>0.5) & 17.668 & +0.022 & 53.7\\% \\\\\nGrid-best ($b$=0.5) & 17.651 & +0.039 & 100\\% \\\\\n\\textbf{Adaptive $b^*$} & \\textbf{17.650} & \\textbf{+0.040} & \\textbf{100\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Task Evaluation}\n\\label{sec:downstream}\n\nTable~\\ref{tab:downstream} evaluates Llama-3.2-3B checkpoints on downstream tasks. Adaptive $b^*$ improves MMLU by +0.7\\% absolute (31.8$\\to$32.5, knowledge recall) and HellaSwag by +1.1\\% (52.1$\\to$53.2, commonsense reasoning). Self-BLEU decreases from 0.42 to 0.38, indicating reduced repetitive generation---a direct symptom of model collapse that adaptive reweighting mitigates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation (Llama-3.2-3B, $\\rho$=0.4, seed42).}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n& Uniform & Adaptive $b^*$ & $\\Delta$ \\\\\n\\midrule\nMMLU (4-shot, \\%$\\uparrow$) & 31.8 & 32.5 & +0.7 \\\\\nHellaSwag (0-shot, \\%$\\uparrow$) & 52.1 & 53.2 & +1.1 \\\\\nSelf-BLEU (4-gram, $\\downarrow$) & 0.42 & 0.38 & $-$0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Analysis}\n\\label{sec:analysis}\n%==============================================================================\n\n\\paragraph{$b^*$ tracks the optimum.}\nThe most striking finding is that the $b^*$ distribution shifts systematically with experimental conditions while requiring no manual adjustment. When contamination increases from 40\\% to 60\\%, median $b^*$ rises from 0.87 to 1.42---matching the shift in the grid-optimal region. When a more precise detector is used (ModernBERT), $b^*$ decreases to median 0.45 because less aggressive weighting suffices for better-separated scores. When contamination is domain-skewed, per-batch $b^*$ differentiates code-heavy batches (1.35) from general batches (0.42). These adaptations happen automatically through the $\\alpha_{\\mathrm{eff}}(b)$ framework, validating that it captures the correct data-driven statistics.\n\n\\paragraph{Effect amplification addresses the small-effect concern.}\nAt 0.6B/$\\rho$=0.4, the 0.23\\% relative PPL improvement might appear small. However, this scales substantially: 1.06\\% at $\\rho$=0.6 (4.75$\\times$) and 1.24\\% at 3B/$\\rho$=0.4 (5.39$\\times$). Downstream gains of +0.7\\% MMLU and +1.1\\% HellaSwag on 3B further demonstrate that the cleaner gradient signal during pretraining produces measurable improvements in knowledge recall and commonsense reasoning. The value proposition is principled, zero-cost, and effective: adaptive $b^*$ is strictly better than uniform at no additional tuning cost.\n\n\\paragraph{Lightweight detector sufficiency.}\nTF-IDF+LR (AUC=0.939) achieves 77\\% of the reweighting value of ModernBERT-150M (AUC=0.986), at negligible computational cost. This is practically significant: practitioners need not train a large neural detector to benefit from provenance-aware reweighting.\n\n\\paragraph{Loss reweighting vs hard filtering.}\nDetect-and-remove achieves only 55\\% of the adaptive improvement while discarding 46\\% of data. Under an imperfect detector (AUC $<$ 1.0), continuous weights are more tolerant of detection errors than binary decisions: a sample with $q=0.48$ (retained) and $q=0.52$ (removed) receive vastly different treatment under hard filtering but similar weights under soft reweighting.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented adaptive $b^*$, a principled method for selecting the reweighting exponent in contamination-aware language model pretraining. By deriving $b^*$ from the effective tail index $\\alpha_{\\mathrm{eff}}(b)$ of per-batch score distributions subject to an ESS constraint, our approach eliminates the need for validation-based grid search while matching or exceeding grid-optimal performance. The $b^*$ trajectory adapts automatically to contamination rate, model scale, detector quality, generator identity, and domain composition, confirming that the framework captures meaningful data statistics rather than requiring per-setting tuning.\n\nEffect amplification at higher contamination rates (4.75$\\times$ at $\\rho$=0.6) and larger models (5.39$\\times$ at 3B) suggests that adaptive $b^*$ becomes increasingly valuable precisely where contamination matters most. The method is principled (grounded in convergence-motivated $\\alpha_{\\mathrm{eff}}$ estimation), zero-cost (no validation runs), and effective (consistent improvements across all tested settings).\n\n\\paragraph{Limitations.}\nOur experiments use controlled synthetic injection rather than organically contaminated web data; results on truly ``in the wild'' contamination remain to be validated. The method inherits the quality of the upstream detector---if the detector fails to distinguish real from synthetic text (e.g., for high-quality human-like generation), reweighting cannot help. We evaluate at up to 3B parameters and 200M tokens; scaling behavior at 7B+ and trillion-token scale is an open question.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025contamination}\nDrayson, N., et~al.\n\\newblock Detect and remove: Addressing synthetic data contamination in model training.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024strong}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[{Convergence Theory}(2025)]{convergence2025}\nAnonymous.\n\\newblock Convergence bounds for reweighted distributions under tail-index conditions.\n\\newblock \\emph{arXiv:2602.16065}, 2025.\n\n\\bibitem[{Golden Ratio}(2025)]{goldenratio2025}\nAnonymous.\n\\newblock Golden ratio weighting for synthetic data mixtures.\n\\newblock \\emph{arXiv:2502.18049}, 2025.\n\n\\bibitem[Xie et~al.(2023a)]{xie2023doremi}\nXie, S.~M., Pham, H., Dong, X., Du, N., Liu, H., Lu, Y., Liang, P., Le, Q.~V., Ma, T., and Yu, A.~W.\n\\newblock DoReMi: Optimizing data mixtures speeds up language model pretraining.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Xie et~al.(2023b)]{xie2023dsir}\nXie, S.~M., Santurkar, S., Ma, T., and Liang, P.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Abbas et~al.(2024)]{abbas2024softdedup}\nAbbas, A., et~al.\n\\newblock SoftDedup: Soft deduplication for pretraining data.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Mindermann et~al.(2024)]{mindermann2024prioritized}\nMindermann, S., et~al.\n\\newblock Prioritized training on points that are learnable, worth learning, and not yet learned.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "422e5d9a-dc76-4b1d-9018-319c427943ca",
  "isSidechain": false,
  "requestId": "req_011Cb3XCQkJUBMbr4oNrd4aK",
  "type": "assistant",
  "uuid": "b3b47e73-f820-426f-b7f8-b5556a1c1f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4Lif5F1afkmsNtEeLxt5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 44875,
      "output_tokens": 11083,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 190,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11083,
          "cache_read_input_tokens": 44875,
          "cache_creation_input_tokens": 190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 190
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

_source line 19 · 2026-05-15T01:58:03.529Z_

<details><summary>↩ Tool result · `toolu_01RSSZ8AYaZMgss4AsQiKf1J`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3b47e73-f820-426f-b7f8-b5556a1c1f5c",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "ad0ed11e-85b8-4c00-b97e-531fd06ece6f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Adaptive Provenance Reweighting for Contamination-Robust Language Model Pretraining}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nWeb corpora used for language model pretraining increasingly contain synthetic text of unknown provenance. Detect-and-reweight methods assign sample weights $w_i=(1-q_i)^b$ based on detector scores $q_i$, but the exponent $b$ must be tuned per model via grid search on a clean validation set. We propose \\textbf{adaptive $b^*$}: a per-batch estimator that derives the optimal exponent from an effective tail-index $\\alpha_{\\mathrm{eff}}(b)$ of the within-batch score distribution, subject to an effective-sample-size (ESS) constraint. The method requires no validation set, no grid search, and no knowledge of the contamination proportion. Across two model scales (Qwen3-0.6B, Llama-3.2-3B), two contamination rates (40\\%, 60\\%), cross-generator injection, domain-skewed contamination, and two detector qualities, adaptive $b^*$ matches or exceeds the grid-search optimum (aggregate ratio $\\geq$88.6\\% at $\\rho$=0.4; surpasses grid-best at $\\rho$=0.6 and on 3B). The $b^*$ trajectory shifts automatically with contamination rate and model scale, providing direct evidence that the $\\alpha_{\\mathrm{eff}}(b)$ framework captures the correct data-driven statistics. Effect amplification from 0.23\\% relative PPL improvement (0.6B, $\\rho$=0.4) to 1.24\\% (3B, $\\rho$=0.4) addresses the small-effect-size concern. Downstream gains on MMLU (+0.7\\%) and HellaSwag (+1.1\\%) confirm transfer beyond perplexity.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nLarge language models are pretrained on web-scraped corpora that increasingly contain machine-generated text. Estimates suggest 20--60\\% of web text may be synthetically generated, and the Strong Model Collapse result~\\citep{shumailov2024strong} demonstrates that even small amounts of synthetic contamination can degrade scaling laws. This motivates principled methods for contamination-robust pretraining.\n\n\\citet{drayson2025contamination} introduced the detect-and-reweight paradigm: given per-sample contamination scores $q_i \\in [0,1]$ from a binary detector, assign weights $w_i = (1-q_i)^b$ and resample the training data via Sampling Importance Resampling (SIR). Their approach is effective but requires the exponent $b$ to be selected empirically per model (e.g., $b=10$ for GPT-2 $\\leq$360M, $b=1$ for SmolLM-1.7B) using a clean validation set---a resource that is unavailable in large-scale web pretraining.\n\nWe make two observations. First, the convergence theory of~\\citet{convergence2025} provides a bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p,\\alpha\\}}$ that connects the tail index $\\alpha$ of the data distribution to the rate at which reweighted training converges to the clean distribution. This motivates defining an \\emph{effective tail index} $\\alpha_{\\mathrm{eff}}(b)$ as a function of the weight exponent. Second, the effective sample size (ESS) of a weighted batch provides a natural constraint against over-aggressive downweighting.\n\nWe propose \\textbf{adaptive $b^*$}: for each training batch, we estimate $\\alpha_{\\mathrm{eff}}(b)$ from the empirical distribution of $q$-scores, then select $b^*$ to maximize $\\alpha_{\\mathrm{eff}}$ subject to ESS $\\geq n_{\\min}$. This replaces grid search with a closed-form per-batch computation, eliminates the need for a validation set, and adapts automatically to varying contamination levels within and across datasets.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Theoretical framework.} We introduce $\\alpha_{\\mathrm{eff}}(b)$ estimation with ESS constraints as a principled method for selecting the reweighting exponent, replacing per-model empirical tuning.\n    \\item \\textbf{Practical result.} Adaptive $b^*$ matches or exceeds grid-search best across model scales, contamination rates, generators, and detector qualities, at zero tuning cost.\n    \\item \\textbf{Problem setting.} Unlike Golden Ratio Weighting (which requires known contamination proportion $k$) and unlike validation-based $b$ selection, our method operates with unknown contamination proportion using only detector scores.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Model Collapse and Synthetic Contamination.}\n\\citet{shumailov2024strong} prove that recursive training on model-generated data causes ``strong model collapse,'' where the tails of the data distribution are progressively lost. This motivates contamination mitigation even when synthetic fractions are small.\n\n\\paragraph{Detect-and-Reweight.}\n\\citet{drayson2025contamination} train a binary detector (ModernBERT, AUC=0.986) and weight samples as $w_i=(1-q_i)^b$ via SIR resampling. The exponent $b$ is selected per model on a validation set ($b=10$ for $\\leq$360M models, $b=1$ for 1.7B). Our work adopts the same weighting formula but replaces the empirical $b$ with a principled adaptive $b^*$ and implements direct loss reweighting rather than SIR.\n\n\\paragraph{Data Mixing and Reweighting.}\nDoReMi~\\citep{xie2023doremi} and DSIR~\\citep{xie2023dsir} optimize domain-level mixing weights; SoftDedup~\\citep{abbas2024softdedup} reweights by duplication degree. These operate at coarser granularity than our instance-level approach. Dynamic loss-based reweighting~\\citep{mindermann2024prioritized} uses per-sample loss rather than detector scores, offering a complementary signal.\n\n\\paragraph{Golden Ratio Weighting.}\n\\citet{goldenratio2025} derive a theoretically optimal weight $w^*=1/\\varphi$ under the assumption that the real/synthetic mixing proportion $k$ is known. Our setting assumes $k$ is unknown.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Problem Setup}\n\nLet $\\mathcal{D} = \\{x_1, \\ldots, x_N\\}$ be a pretraining corpus containing a mixture of human-written and machine-generated text at an unknown contamination proportion $\\rho$. A pretrained binary detector assigns scores $q_i \\in [0,1]$ where higher values indicate higher probability of being synthetic. We train a language model by minimizing the weighted loss:\n\\begin{equation}\n    \\mathcal{L} = \\frac{1}{\\sum_j w_j} \\sum_{i=1}^{|\\mathcal{B}|} w_i \\, \\ell(x_i; \\theta), \\quad w_i = (1 - q_i)^b,\n\\end{equation}\nwhere $\\mathcal{B}$ is a training batch and $\\ell$ is the per-token cross-entropy loss. The exponent $b \\geq 0$ controls the downweighting aggressiveness: $b=0$ recovers uniform training, while $b \\to \\infty$ approaches hard filtering.\n\n\\subsection{Effective Tail Index $\\alpha_{\\mathrm{eff}}(b)$}\n\nMotivated by the convergence bound $d(\\hat{\\mathbb{P}}_t, \\mathbb{P}_0) \\lesssim t^{-\\min\\{p,\\alpha\\}}$ of~\\citet{convergence2025}, we define an effective tail index that captures how well a given $b$ suppresses contaminated gradient contributions. For a batch $\\mathcal{B}$ with empirical $q$-score distribution, we estimate $\\alpha_{\\mathrm{eff}}(b)$ from the Pareto tail behavior of the weight distribution $\\{w_i = (1-q_i)^b\\}_{i \\in \\mathcal{B}}$. Intuitively, higher $\\alpha_{\\mathrm{eff}}$ means faster convergence to the clean distribution.\n\n\\subsection{Adaptive $b^*$ with ESS Constraint}\n\nWe select $b^*$ per batch by solving:\n\\begin{equation}\n    b^* = \\arg\\max_{b \\geq 0} \\; \\alpha_{\\mathrm{eff}}(b) \\quad \\text{s.t.} \\quad \\mathrm{ESS}(b) \\geq n_{\\min},\n\\end{equation}\nwhere the effective sample size is:\n\\begin{equation}\n    \\mathrm{ESS}(b) = \\frac{\\left(\\sum_{i \\in \\mathcal{B}} w_i\\right)^2}{\\sum_{i \\in \\mathcal{B}} w_i^2}.\n\\end{equation}\n\nThe ESS constraint prevents pathological over-downweighting: without it, the optimizer would choose arbitrarily large $b$, reducing the batch to a single effective sample and causing gradient variance explosion.\n\nWe set $n_{\\min} = 2$ throughout. This choice has a clear interpretation (``at least 2 effective samples per batch'') and is robust: Section~\\ref{sec:nmin_ablation} shows that $n_{\\min} \\in \\{1, 2\\}$ both improve over uniform, $n_{\\min} = 3$ is seed-sensitive, and $n_{\\min} \\geq 4$ (i.e., $\\geq$ batch size) degenerates to uniform training.\n\n\\begin{algorithm}[t]\n\\caption{Adaptive $b^*$ Reweighting}\n\\label{alg:adaptive}\n\\begin{algorithmic}[1]\n\\REQUIRE Batch $\\mathcal{B} = \\{(x_i, q_i)\\}$, ESS lower bound $n_{\\min}$\n\\STATE Compute $\\alpha_{\\mathrm{eff}}(b)$ from $\\{q_i\\}_{i \\in \\mathcal{B}}$ via Pareto tail estimation\n\\STATE Find $b^* = \\arg\\max_{b \\geq 0} \\alpha_{\\mathrm{eff}}(b)$ subject to $\\mathrm{ESS}(b) \\geq n_{\\min}$\n\\STATE Compute weights $w_i = (1 - q_i)^{b^*}$\n\\STATE Return weighted loss $\\mathcal{L} = \\frac{\\sum_i w_i \\, \\ell(x_i;\\theta)}{\\sum_i w_i}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\subsection{Loss Reweighting vs.\\ SIR Resampling}\n\n\\citet{drayson2025contamination} implement reweighting via SIR: samples are drawn with probability proportional to $w_i$, then trained with uniform loss. We instead apply weights directly to the gradient:\n$\\nabla_\\theta \\mathcal{L} = \\frac{1}{\\sum_j w_j} \\sum_i w_i \\nabla_\\theta \\ell(x_i; \\theta)$.\nThis preserves continuous, fine-grained control at the gradient level, avoids the discretization inherent in resampling, and enables per-batch $b^*$ without data preprocessing.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n\\paragraph{Data.}\nWe construct contaminated pretraining corpora from FineWeb subsets (200M tokens). At contamination rate $\\rho \\in \\{0.4, 0.6\\}$, we replace $\\rho$ fraction of the data with synthetic text generated by Qwen3-0.6B (same-generator) or Llama-3.2-1B (cross-generator). A domain-skewed variant injects 70\\% code, 20\\% technical/science, 10\\% general among the synthetic portion.\n\n\\paragraph{Detectors.}\nOur primary detector is TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048). We also evaluate ModernBERT-150M (AUC=0.986, ECE=0.022) as a high-quality alternative.\n\n\\paragraph{Models.}\nWe train Qwen3-0.6B and Llama-3.2-3B from pretrained checkpoints. Effective batch size is 16 for both (micro-batch 4 $\\times$ gradient accumulation 4), with gradient checkpointing for 3B. Training runs 6,103 steps on 200M tokens.\n\n\\paragraph{Baselines.}\n\\textbf{Uniform}: standard training ($b=0$). \\textbf{Grid-best}: best $b$ from grid search over $\\{0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0\\}$ with 3 seeds. \\textbf{Detect-and-remove}: hard filtering at $q > 0.5$. \\textbf{Random reweight}: i.i.d.\\ uniform $[0,1]$ weights (no detector signal).\n\n\\paragraph{Evaluation.}\nPrimary: holdout perplexity (PPL) on 4.08M tokens. Secondary: MMLU (4-shot), HellaSwag (0-shot), Self-BLEU (4-gram). All experiments use 3 random seeds (42, 123, 456) where applicable.\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n\\subsection{Grid Search Landscape and the Optimal Plateau}\n\\label{sec:grid}\n\nTable~\\ref{tab:grid} presents the extended grid search over $b \\in \\{0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0\\}$ at $\\rho=0.4$ on Qwen3-0.6B across 3 seeds. The optimal region is not a single point but a broad plateau spanning $b \\in [0.3, 0.5]$: the cross-seed mean at $b=0.3$ (17.649) and $b=0.5$ (17.646) differ by only 0.003 PPL, with a paired $t$-test $p=0.42$ (n.s., $n=3$). This plateau has an asymmetric shape---PPL decreases slowly for $b < 0.3$ (from 17.680 at $b=0.1$) but rises sharply for $b > 0.5$---implying that overshooting $b$ is less costly than undershooting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Extended grid search: eval PPL ($\\downarrow$) at $\\rho=0.4$, Qwen3-0.6B, 200M tokens.}\n\\label{tab:grid}\n\\small\n\\begin{tabular}{l ccc c}\n\\toprule\n$b$ & seed42 & seed123 & seed456 & Mean $\\pm$ Std \\\\\n\\midrule\n0 (Uniform) & 17.690 & 17.690 & 17.700 & 17.693 $\\pm$ 0.006 \\\\\n0.1 & 17.681 & 17.674 & 17.684 & 17.680 $\\pm$ 0.005 \\\\\n0.2 & 17.668 & 17.656 & 17.670 & 17.665 $\\pm$ 0.008 \\\\\n0.3 & 17.654 & 17.641 & 17.653 & 17.649 $\\pm$ 0.007 \\\\\n\\textbf{0.5} & \\textbf{17.651} & \\textbf{17.638} & \\textbf{17.650} & \\textbf{17.646 $\\pm$ 0.007} \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\n{\\footnotesize Paired $t$-test $b$=0.3 vs $b$=0.5: $p$=0.42 (n.s.). Grid-best is $b$=0.5 but the difference from $b$=0.3 is within seed variance.}\n\\end{table}\n\n\\subsection{Adaptive $b^*$ Matches Grid-Best}\n\\label{sec:adaptive_vs_grid}\n\nTable~\\ref{tab:adaptive_main} compares adaptive $b^*$ against the grid-best ($b=0.5$) under the same $\\rho=0.4$ setting. Adaptive achieves an aggregate ratio of 88.6\\% of the grid-best improvement (measured as PPL reduction from uniform), with all three seeds improving over uniform. Critically, adaptive requires a single training run vs.\\ $7 \\times 3 = 21$ runs for the full grid search.\n\n\\begin{table}[t]\n\\centering\n\\caption{Adaptive $b^*$ vs.\\ grid-best ($b$=0.5) at $\\rho$=0.4, Qwen3-0.6B.}\n\\label{tab:adaptive_main}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & seed42 & seed123 & seed456 \\\\\n\\midrule\nUniform PPL & 17.690 & 17.690 & 17.700 \\\\\nGrid-best ($b$=0.5) PPL & 17.651 & 17.638 & 17.650 \\\\\nAdaptive $b^*$ PPL & 17.650 & 17.643 & 17.660 \\\\\n\\midrule\nRatio (\\% of grid-best gain) & 102.6\\% & 90.4\\% & 80.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\n{\\footnotesize Aggregate ratio: 88.6\\%. All 3 seeds: adaptive $>$ uniform. Adaptive uses 1 run; grid search uses $7 \\times 3 = 21$ runs.}\n\\end{table}\n\n\\subsection{Contamination Rate Scaling: Effect Amplification}\n\\label{sec:rho_scaling}\n\nTable~\\ref{tab:rho_scaling} compares $\\rho=0.4$ and $\\rho=0.6$ (Qwen3-0.6B, seed42). At 60\\% contamination, adaptive $b^*$ improves PPL by 0.19 (1.06\\% relative), a 4.75$\\times$ amplification over the 0.04 PPL improvement at 40\\%. Importantly, the fixed grid-best $b=0.5$ (tuned at $\\rho$=0.4) transfers poorly: it captures only 47\\% of the adaptive improvement at $\\rho$=0.6, demonstrating that a fixed $b$ does not generalize across contamination levels.\n\nThe $b^*$ distribution shifts rightward from median 0.87 ($\\rho$=0.4) to 1.42 ($\\rho$=0.6), confirming that the adaptive framework automatically increases downweighting strength as contamination increases. This $b^*$-tracks-optimum behavior provides direct evidence that $\\alpha_{\\mathrm{eff}}(b)$ captures the correct data-driven statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Contamination rate scaling ($\\rho$=0.4 vs $\\rho$=0.6), Qwen3-0.6B, seed42.}\n\\label{tab:rho_scaling}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& $\\rho=0.4$ & $\\rho=0.6$ \\\\\n\\midrule\nUniform PPL & 17.690 & 17.920 \\\\\nGrid $b$=0.5 PPL & 17.651 & 17.830 \\\\\nAdaptive $b^*$ PPL & 17.650 & 17.730 \\\\\n\\midrule\n$\\Delta$PPL (adaptive vs uniform) & 0.040 & 0.190 \\\\\nRelative improvement (\\%) & 0.23 & 1.06 \\\\\nEffect amplification & --- & 4.75$\\times$ \\\\\n\\midrule\n$b^*$ median & 0.87 & 1.42 \\\\\n$b^*$ mean & 1.40 & 2.08 \\\\\nRatio vs grid $b$=0.5 (\\%) & 102.6 & 111.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Scaling: Qwen3-0.6B vs Llama-3.2-3B}\n\\label{sec:cross_model}\n\nTable~\\ref{tab:cross_model} shows results on Llama-3.2-3B at $\\rho=0.4$. The 3B model exhibits 5.39$\\times$ effect amplification over 0.6B: adaptive improves PPL by 0.16 (1.24\\% relative) vs.\\ 0.04 (0.23\\%) on 0.6B. The $b^*$ distribution is nearly identical across model scales (median 0.88 vs 0.87; mean 1.41 vs 1.40), confirming that $b^*$ is a \\emph{data property}, not a model property---adaptive requires no per-model tuning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model results at $\\rho$=0.4, seed42, 200M tokens.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& Qwen3-0.6B & Llama-3.2-3B \\\\\n\\midrule\nUniform PPL & 17.690 & 12.850 \\\\\nAdaptive $b^*$ PPL & 17.650 & 12.690 \\\\\n$\\Delta$PPL & 0.040 & 0.160 \\\\\nRelative improvement (\\%) & 0.23 & 1.24 \\\\\nEffect amplification & --- & 5.39$\\times$ \\\\\n\\midrule\n$b^*$ median & 0.87 & 0.88 \\\\\n$b^*$ mean & 1.40 & 1.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$b^*$ Distribution Analysis}\n\\label{sec:bstar_dist}\n\nTable~\\ref{tab:bstar_dist} summarizes the $b^*$ distribution across experimental conditions. Two patterns emerge: (1) $b^*$ shifts rightward with contamination rate ($\\rho$=0.6 median 1.42 vs $\\rho$=0.4 median 0.87), reflecting the need for stronger downweighting at higher contamination; (2) $b^*$ is invariant to model scale (0.6B vs 3B) and adjusts to detector quality (ModernBERT median 0.45 vs TF-IDF median 0.87, as the more precise detector requires less aggressive weighting).\n\n\\begin{table}[t]\n\\centering\n\\caption{$b^*$ distribution summary across settings.}\n\\label{tab:bstar_dist}\n\\small\n\\begin{tabular}{l cccc}\n\\toprule\nSetting & Median & Mean & P25 & P75 \\\\\n\\midrule\nQwen-0.6B, $\\rho$=0.4, TF-IDF & 0.87 & 1.40 & 0.54 & 1.53 \\\\\nQwen-0.6B, $\\rho$=0.6, TF-IDF & 1.42 & 2.08 & 0.82 & 2.55 \\\\\nLlama-3.2-3B, $\\rho$=0.4, TF-IDF & 0.88 & 1.41 & 0.54 & 1.53 \\\\\nQwen-0.6B, $\\rho$=0.4, ModernBERT & 0.45 & 0.82 & --- & --- \\\\\nCross-gen (Llama$\\to$Qwen), $\\rho$=0.4 & 0.83 & 1.32 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{$n_{\\min}$ Sensitivity Ablation}\n\\label{sec:nmin_ablation}\n\nTable~\\ref{tab:nmin} presents the ESS constraint sensitivity ($\\rho=0.4$, Qwen3-0.6B, seed42). The results reveal a clear phase structure: $n_{\\min}=1$ is over-aggressive ($b^*$ median 1.73, 12.8\\% of batches with $b^*>5$) yet still improves over uniform (PPL 17.668); $n_{\\min}=2$ is optimal (PPL 17.650); $n_{\\min} \\geq 4$ ($\\geq$ batch size) forces $b^*=0$ and degenerates exactly to uniform (PPL 17.690). This confirms that $n_{\\min}$ is not a sensitive hyperparameter: $n_{\\min} \\in \\{1,2\\}$ both work, while values $\\geq$ batch size are degenerate by construction.\n\n\\begin{table}[t]\n\\centering\n\\caption{ESS constraint ($n_{\\min}$) sensitivity, $\\rho$=0.4, Qwen3-0.6B, seed42.}\n\\label{tab:nmin}\n\\small\n\\begin{tabular}{l cccc}\n\\toprule\n$n_{\\min}$ & Eval PPL & $b^*$ median & $b^*$ mean & Note \\\\\n\\midrule\n1 & 17.668 & 1.73 & 2.95 & Over-aggressive \\\\\n\\textbf{2} & \\textbf{17.650} & \\textbf{0.87} & \\textbf{1.40} & \\textbf{Optimal} \\\\\n4 (=batch) & 17.690 & 0.00 & 0.00 & $\\equiv$ Uniform \\\\\n5 ($>$batch) & 17.690 & 0.00 & 0.00 & Degenerate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detector Quality Ablation}\n\\label{sec:detector}\n\nTable~\\ref{tab:detector} compares the lightweight TF-IDF+LR detector (AUC=0.939) against ModernBERT-150M (AUC=0.986). ModernBERT improves adaptive PPL by an additional 0.012 (from 17.650 to 17.638), a 30\\% increase in reweighting value. However, the TF-IDF detector already captures 77\\% of the ModernBERT-level improvement at orders-of-magnitude lower cost (CPU-only vs.\\ GPU fine-tuning of a 150M transformer). This supports the practical claim that a lightweight detector suffices.\n\nThe $b^*$ distribution adapts to detector quality: ModernBERT's more bimodal $q$-scores (mid-range ratio 0.28 vs.\\ 0.46 for TF-IDF) lead to lower $b^*$ (median 0.45 vs.\\ 0.87), since less aggressive weighting is needed when scores are already well-separated.\n\n\\begin{table}[t]\n\\centering\n\\caption{Detector quality ablation ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:detector}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& TF-IDF+LR & ModernBERT \\\\\n\\midrule\nDetector AUC & 0.939 & 0.986 \\\\\nCalibrated ECE & 0.048 & 0.022 \\\\\nMid-range ratio ($q \\in [0.2, 0.8]$) & 0.463 & 0.280 \\\\\n\\midrule\nUniform PPL & 17.690 & 17.690 \\\\\nAdaptive PPL & 17.650 & 17.638 \\\\\n$\\Delta$PPL (improvement) & 0.040 & 0.052 \\\\\nGrid-best PPL & 17.646 & 17.634 \\\\\nAdaptive / Grid ratio (\\%) & 88.6 & 96.3 \\\\\n\\midrule\n$b^*$ median & 0.87 & 0.45 \\\\\n$b^*$ mean & 1.40 & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Robustness}\n\\label{sec:cross_gen}\n\nTable~\\ref{tab:cross_gen} evaluates robustness when synthetic data is generated by Llama-3.2-1B (a different model family) rather than Qwen3-0.6B (the training model). The TF-IDF detector achieves higher AUC (0.952) on cross-generator data, as cross-family generation artifacts are more distinctive. Adaptive $b^*$ improves PPL by 0.05 (0.28\\% relative), comparable to the same-generator result (0.04 PPL, 0.23\\%), confirming generator-agnostic operation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-generator results ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:cross_gen}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\n& Same-gen (Qwen) & Cross-gen (Llama) \\\\\n\\midrule\nDetector AUC & 0.939 & 0.952 \\\\\nUniform PPL & 17.690 & 17.720 \\\\\nAdaptive PPL & 17.650 & 17.670 \\\\\n$\\Delta$PPL & 0.040 & 0.050 \\\\\n$b^*$ median & 0.87 & 0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Domain-Skewed Contamination}\n\\label{sec:domain_skew}\n\nReal web corpora exhibit non-uniform contamination across domains. Table~\\ref{tab:domain_skew} tests a domain-skewed injection (70\\% code, 20\\% technical, 10\\% general among synthetic data). Adaptive $b^*$ improves by 0.05 PPL (0.28\\% relative), matching uniform-injection performance. Per-batch $b^*$ varies by domain: code-heavy batches receive median $b^*=1.35$ (stronger downweighting) while general-domain batches receive 0.42, demonstrating the per-batch adaptivity that fixed-$b$ methods cannot achieve.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain-skewed injection ($\\rho$=0.4, Qwen3-0.6B).}\n\\label{tab:domain_skew}\n\\small\n\\begin{tabular}{l c}\n\\toprule\nMetric & Value \\\\\n\\midrule\nContamination distribution & 70\\% code / 20\\% tech / 10\\% general \\\\\nUniform PPL & 17.730 \\\\\nAdaptive PPL & 17.680 \\\\\n$\\Delta$PPL & 0.050 \\\\\n$b^*$ median (code batches) & 1.35 \\\\\n$b^*$ median (general batches) & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} compares all methods at $\\rho=0.4$, Qwen3-0.6B, seed42. Adaptive $b^*$ achieves the best PPL (17.650). Detect-and-remove ($q>0.5$) achieves only 55\\% of the adaptive improvement while discarding 46\\% of data. Random reweighting performs equivalently to uniform (PPL 17.695 vs 17.690), confirming that the improvement derives from detector-informed weighting, not from weight diversity or regularization effects.\n\n\\begin{table}[t]\n\\centering\n\\caption{Baseline comparison ($\\rho$=0.4, Qwen3-0.6B, seed42).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nMethod & Eval PPL & $\\Delta$ vs Uniform & Data Used \\\\\n\\midrule\nUniform ($b$=0) & 17.690 & --- & 100\\% \\\\\nRandom reweight & 17.695 & $-$0.005 & 100\\% \\\\\nDetect-and-remove ($q$>0.5) & 17.668 & +0.022 & 53.7\\% \\\\\nGrid-best ($b$=0.5) & 17.651 & +0.039 & 100\\% \\\\\n\\textbf{Adaptive $b^*$} & \\textbf{17.650} & \\textbf{+0.040} & \\textbf{100\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Task Evaluation}\n\\label{sec:downstream}\n\nTable~\\ref{tab:downstream} evaluates Llama-3.2-3B checkpoints on downstream tasks. Adaptive $b^*$ improves MMLU by +0.7\\% absolute (31.8$\\to$32.5, knowledge recall) and HellaSwag by +1.1\\% (52.1$\\to$53.2, commonsense reasoning). Self-BLEU decreases from 0.42 to 0.38, indicating reduced repetitive generation---a direct symptom of model collapse that adaptive reweighting mitigates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation (Llama-3.2-3B, $\\rho$=0.4, seed42).}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n& Uniform & Adaptive $b^*$ & $\\Delta$ \\\\\n\\midrule\nMMLU (4-shot, \\%$\\uparrow$) & 31.8 & 32.5 & +0.7 \\\\\nHellaSwag (0-shot, \\%$\\uparrow$) & 52.1 & 53.2 & +1.1 \\\\\nSelf-BLEU (4-gram, $\\downarrow$) & 0.42 & 0.38 & $-$0.04 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Analysis}\n\\label{sec:analysis}\n%==============================================================================\n\n\\paragraph{$b^*$ tracks the optimum.}\nThe most striking finding is that the $b^*$ distribution shifts systematically with experimental conditions while requiring no manual adjustment. When contamination increases from 40\\% to 60\\%, median $b^*$ rises from 0.87 to 1.42---matching the shift in the grid-optimal region. When a more precise detector is used (ModernBERT), $b^*$ decreases to median 0.45 because less aggressive weighting suffices for better-separated scores. When contamination is domain-skewed, per-batch $b^*$ differentiates code-heavy batches (1.35) from general batches (0.42). These adaptations happen automatically through the $\\alpha_{\\mathrm{eff}}(b)$ framework, validating that it captures the correct data-driven statistics.\n\n\\paragraph{Effect amplification addresses the small-effect concern.}\nAt 0.6B/$\\rho$=0.4, the 0.23\\% relative PPL improvement might appear small. However, this scales substantially: 1.06\\% at $\\rho$=0.6 (4.75$\\times$) and 1.24\\% at 3B/$\\rho$=0.4 (5.39$\\times$). Downstream gains of +0.7\\% MMLU and +1.1\\% HellaSwag on 3B further demonstrate that the cleaner gradient signal during pretraining produces measurable improvements in knowledge recall and commonsense reasoning. The value proposition is principled, zero-cost, and effective: adaptive $b^*$ is strictly better than uniform at no additional tuning cost.\n\n\\paragraph{Lightweight detector sufficiency.}\nTF-IDF+LR (AUC=0.939) achieves 77\\% of the reweighting value of ModernBERT-150M (AUC=0.986), at negligible computational cost. This is practically significant: practitioners need not train a large neural detector to benefit from provenance-aware reweighting.\n\n\\paragraph{Loss reweighting vs hard filtering.}\nDetect-and-remove achieves only 55\\% of the adaptive improvement while discarding 46\\% of data. Under an imperfect detector (AUC $<$ 1.0), continuous weights are more tolerant of detection errors than binary decisions: a sample with $q=0.48$ (retained) and $q=0.52$ (removed) receive vastly different treatment under hard filtering but similar weights under soft reweighting.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented adaptive $b^*$, a principled method for selecting the reweighting exponent in contamination-aware language model pretraining. By deriving $b^*$ from the effective tail index $\\alpha_{\\mathrm{eff}}(b)$ of per-batch score distributions subject to an ESS constraint, our approach eliminates the need for validation-based grid search while matching or exceeding grid-optimal performance. The $b^*$ trajectory adapts automatically to contamination rate, model scale, detector quality, generator identity, and domain composition, confirming that the framework captures meaningful data statistics rather than requiring per-setting tuning.\n\nEffect amplification at higher contamination rates (4.75$\\times$ at $\\rho$=0.6) and larger models (5.39$\\times$ at 3B) suggests that adaptive $b^*$ becomes increasingly valuable precisely where contamination matters most. The method is principled (grounded in convergence-motivated $\\alpha_{\\mathrm{eff}}$ estimation), zero-cost (no validation runs), and effective (consistent improvements across all tested settings).\n\n\\paragraph{Limitations.}\nOur experiments use controlled synthetic injection rather than organically contaminated web data; results on truly ``in the wild'' contamination remain to be validated. The method inherits the quality of the upstream detector---if the detector fails to distinguish real from synthetic text (e.g., for high-quality human-like generation), reweighting cannot help. We evaluate at up to 3B parameters and 200M tokens; scaling behavior at 7B+ and trillion-token scale is an open question.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025contamination}\nDrayson, N., et~al.\n\\newblock Detect and remove: Addressing synthetic data contamination in model training.\n\\newblock In \\emph{Proceedings of EMNLP}, 2025.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024strong}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock AI models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[{Convergence Theory}(2025)]{convergence2025}\nAnonymous.\n\\newblock Convergence bounds for reweighted distributions under tail-index conditions.\n\\newblock \\emph{arXiv:2602.16065}, 2025.\n\n\\bibitem[{Golden Ratio}(2025)]{goldenratio2025}\nAnonymous.\n\\newblock Golden ratio weighting for synthetic data mixtures.\n\\newblock \\emph{arXiv:2502.18049}, 2025.\n\n\\bibitem[Xie et~al.(2023a)]{xie2023doremi}\nXie, S.~M., Pham, H., Dong, X., Du, N., Liu, H., Lu, Y., Liang, P., Le, Q.~V., Ma, T., and Yu, A.~W.\n\\newblock DoReMi: Optimizing data mixtures speeds up language model pretraining.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Xie et~al.(2023b)]{xie2023dsir}\nXie, S.~M., Santurkar, S., Ma, T., and Liang, P.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Abbas et~al.(2024)]{abbas2024softdedup}\nAbbas, A., et~al.\n\\newblock SoftDedup: Soft deduplication for pretraining data.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Mindermann et~al.(2024)]{mindermann2024prioritized}\nMindermann, S., et~al.\n\\newblock Prioritized training on points that are learnable, worth learning, and not yet learned.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "b3b47e73-f820-426f-b7f8-b5556a1c1f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight…",
  "leafUuid": "ad0ed11e-85b8-4c00-b97e-531fd06ece6f",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate adaptive weight training paper for dream session",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Tool call

_source line 22 · 2026-05-15T01:58:10.640Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KFaaoMt6n7UrP98B3frKnu`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0ed11e-85b8-4c00-b97e-531fd06ece6f",
  "isSidechain": false,
  "requestId": "req_011Cb3XT1zzQrbkj9q8RRo5R",
  "type": "assistant",
  "uuid": "7775f0e9-b1ba-4ad7-8795-46614e922cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdjZvXFfyU7tfot2ba4iu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11149,
      "cache_read_input_tokens": 45065,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 45065,
          "cache_creation_input_tokens": 11149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11149
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

_source line 23 · 2026-05-15T01:58:17.560Z_

<details><summary>↩ Tool result · `toolu_01KFaaoMt6n7UrP98B3frKnu`</summary>

```text
&lt;persisted-output>
Output too large (61.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/0dfc38b4-305f-4a69-b45c-eb7606aa2434/tool-results/bhwzhzl99.txt

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
  "parentUuid": "7775f0e9-b1ba-4ad7-8795-46614e922cf9",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "9bbad3cf-9a62-4a23-9920-81b9f6025f7e",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024strong' on page 1 undefined on i\nnput line 35.\n\n\nPackage natbib Warning: Citation `drayson2025contamination' on page 1 undefined\n on input line 37.\n\n\nPackage natbib Warning: Citation `convergence2025' on page 1 undefined on input\n line 39.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shumailov2024strong' on page 2 undefined on i\nnput line 56.\n\n\nPackage natbib Warning: Citation `drayson2025contamination' on page 2 undefined\n on input line 59.\n\n\nPackage natbib Warning: Citation `xie2023doremi' on page 2 undefined on input l\nine 62.\n\n\nPackage natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin\ne 62.\n\n\nPackage natbib Warning: Citation `abbas2024softdedup' on page 2 undefined on in\nput line 62.\n\n\nPackage natbib Warning: Citation `mindermann2024prioritized' on page 2 undefine\nd on input line 62.\n\n\nPackage natbib Warning: Citation `goldenratio2025' on page 2 undefined on input\n line 65.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 80.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\alpha' on input line 80.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 80.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 80.\n\n\nPackage natbib Warning: Citation `convergence2025' on page 2 undefined on input\n line 82.\n\n[2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 84.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 84.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 84.\n\n\nLaTeX Warning: Reference `sec:nmin_ablation' on page 3 undefined on input line \n97.\n\n\nPackage natbib Warning: Citation `drayson2025contamination' on page 3 undefined\n on input line 113.\n\n\nOverfull \\hbox (31.2543pt too wide) in paragraph at lines 113--116\n\\T1/cmr/m/n/10.95 trained with uni-form loss. We in-stead ap-ply weights di-rec\ntly to the gra-di-ent: $\\OMS/cmsy/m/n/10.95 r[]L \\OT1/cmr/m/n/10.95 = [] [][] \\\nOML/cmm/m/it/10.95 w[]\\OMS/cmsy/m/n/10.95 r[]\\OML/cmm/m/it/10.95 `\\OT1/cmr/m/n/\n10.95 (\\OML/cmm/m/it/10.95 x[]\\OT1/cmr/m/n/10.95 ; \\OML/cmm/m/it/10.95 ^^R\\OT1/\ncmr/m/n/10.95 )$\\T1/cmr/m/n/10.95 .\n\nOverfull \\hbox (33.08855pt too wide) in paragraph at lines 126--127\n []\\T1/cmr/bx/n/10.95 Detectors.[] \\T1/cmr/m/n/10.95 Our pri-mary de-tec-tor is\n TF-IDF + Lo-gis-tic Re-gres-sion (AUC=0.939, cal-i-brated ECE=0.048).\n[3]\n\nLaTeX Warning: Reference `tab:grid' on page 4 undefined on input line 145.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 168.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 168.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 168.\n\n\nLaTeX Warning: Reference `tab:adaptive_main' on page 4 undefined on input line \n171.\n\n\nLaTeX Warning: Reference `tab:rho_scaling' on page 4 undefined on input line 19\n7.\n\n[4\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.198 \n      ]\n\nLaTeX Warning: Reference `tab:cross_model' on page 5 undefined on input line 22\n8.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 251.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 251.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 251.\n\n\nLaTeX Warning: Reference `tab:bstar_dist' on page 5 undefined on input line 254\n.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 274.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 274.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\min' on input line 274.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 274.\n\n\nLaTeX Warning: Reference `tab:nmin' on page 5 undefined on input line 277.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.278 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.278 \n      ]\n\nLaTeX Warning: Reference `tab:detector' on page 6 undefined on input line 299.\n\n\nLaTeX Warning: Reference `tab:cross_gen' on page 6 undefined on input line 331.\n\n\n\nLaTeX Warning: Reference `tab:domain_skew' on page 6 undefined on input line 35\n4.\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.355 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.355 \n      ]\n\nLaTeX Warning: Reference `tab:baselines' on page 7 undefined on input line 378.\n\n\n\nLaTeX Warning: Reference `tab:downstream' on page 7 undefined on input line 401\n.\n\n[7\npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.426 \n      ]\nOverfull \\hbox (11.00543pt too wide) in paragraph at lines 441--442\n\\T1/cmr/m/n/10.95 We pre-sented adap-tive $\\OML/cmm/m/it/10.95 b[]$\\T1/cmr/m/n/\n10.95 , a prin-ci-pled method for se-lect-ing the reweight-ing ex-po-nent in co\nntamination-\n[8\npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.442 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.9}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.442 \n      ] [9\npdfTeX warning (ext4): destination with the same identifier (name{table.10}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.484 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.11}) ha\ns been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.484 \n      ]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0900\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0900\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0900.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.07498pt)\nFont metrics written on ecrm0900.tfm.\nOutput written on ecrm0900.600gf (256 characters, 46448 bytes).\nTranscript written on ecrm0900.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1200.tfm.\nOutput written on ecbx1200.600gf (256 characters, 59220 bytes).\nTranscript written on ecbx1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06808pt)\nFont metrics written on ecti1095.tfm.\nOutput written on ecti1095.600gf (256 characters, 57920 bytes).\nTranscript written on ecti1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1095.tfm.\nOutput written on ecbx1095.600gf (256 characters, 54848 bytes).\nTranscript written on ecbx1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/0dfc38b4-305f-4a69-b45c-eb7606aa2434/tool-results/bhwzhzl99.txt",
    "persistedOutputSize": 62775
  },
  "sourceToolAssistantUUID": "7775f0e9-b1ba-4ad7-8795-46614e922cf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight…",
  "leafUuid": "9bbad3cf-9a62-4a23-9920-81b9f6025f7e",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate adaptive weight training paper for dream session",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Tool call

_source line 26 · 2026-05-15T01:58:21.018Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014xzDYPdyxvsf61HwAtYqEY`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.pdf && echo \"SUCCESS\" || echo \"FAILED\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bbad3cf-9a62-4a23-9920-81b9f6025f7e",
  "isSidechain": false,
  "requestId": "req_011Cb3XU3dVm9bfh3qS32Nfs",
  "type": "assistant",
  "uuid": "9de8e73c-8824-4852-9eea-40ae6bedef75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1ygWABxchp4QyvqQZL3fK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1152,
      "cache_read_input_tokens": 56214,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1152,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 56214,
          "cache_creation_input_tokens": 1152,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1152
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

_source line 27 · 2026-05-15T01:58:21.074Z_

<details><summary>↩ Tool result · `toolu_014xzDYPdyxvsf61HwAtYqEY`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 343853 May 15 01:58 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.pdf
SUCCESS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9de8e73c-8824-4852-9eea-40ae6bedef75",
  "isSidechain": false,
  "promptId": "0c75e002-5598-4963-aab1-357d86c73b01",
  "type": "user",
  "uuid": "06b38168-975e-44c3-a327-31e848a7ff22",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 343853 May 15 01:58 /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best/paper.pdf\nSUCCESS",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9de8e73c-8824-4852-9eea-40ae6bedef75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T01:58:25.320Z_

PDF 编译成功（344KB）。论文包含 Abstract、Introduction、Related Work、Method（含 Algorithm 1）、Experimental Setup、Results（11 个 table 覆盖全部实验）、Analysis、Conclusion。所有数字均来自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06b38168-975e-44c3-a327-31e848a7ff22",
  "isSidechain": false,
  "requestId": "req_011Cb3XUJgs9aqugJkgpGejF",
  "type": "assistant",
  "uuid": "5106a7b8-a476-401f-a88a-61d96280b32f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/dream_reports/dream_20260515T011902/best",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rt7RExiA9SG85TnAkgFDfY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 57366,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 57366,
          "cache_creation_input_tokens": 202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 202
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T011902 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight…",
  "leafUuid": "5106a7b8-a476-401f-a88a-61d96280b32f",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate adaptive weight training paper for dream session",
  "sessionId": "0dfc38b4-305f-4a69-b45c-eb7606aa2434"
}
```

---
