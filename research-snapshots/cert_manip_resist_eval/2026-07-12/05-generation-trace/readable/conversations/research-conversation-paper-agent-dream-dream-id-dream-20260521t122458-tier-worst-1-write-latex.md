# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/f42e7a5e-4261-4e67-89af-26943eb41d68.jsonl`
- **Structured JSON:** [`479a99c84fd4d2ae1126.json`](../../sessions/47/479a99c84fd4d2ae1126.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T13:39:13.088Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T13:39:13.088Z",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：7-8B pilot 的核心模式不推广到全量模型。两个 MoE 架构（Qwen3-235B, Llama 4 Scout）完全没有清晰的 Pareto frontier——MoE expert routing 打破了 dense model 中 depth→specialization 的单调映射， depth-transfer 关系在绝大多数语言为 non-monotonic 或 flat。唯一的 dense 架构（Gemma 4 31B）展现出 marginal Pareto（global rho=-0.24, p=0.038），但仅 4/20 语言 per-language 显著，且 final-layer transfer drop 微不足道（0.8pp），远不及 pilot 的 2-4pp。三架构平均 EN AUROC 0.74，处于 worst 范围中段。\nSimpson's Paradox 在 20 语言全量验证中全面崩塌：3 架构的 CKA partial correlation controlling for depth 均不显著（max rho=+0.16, min p=0.09），Llama pilot 的 rho=+0.41 被确认为 5 语言 small-sample artifact。CKA 提供不了超越 depth 的解释力。Subspace angle analysis 否定了 \"correctness direction is a robust language-agnostic subspace\"——HIGH tier 语言 angle 15-38°，LOW tier 45-65°。\nCaCLR 全面失败：β sweep 3 OOM 证实 consistency loss inert 或 harmful；CORAL 和 high-dim MMD (PCA d=50/100) 同样失败，将 negative result 从 \"MMD-specific\" 扩展为 \"distributional matching 路径全面 关闭\"。Component ablation 每加一项 loss 都 net negative。\nDecomposition 无实质效果，random-direction control 产生同量级 delta（paired test p=0.38）， difficulty 和 capability 不可分。\nControl task analysis 是最强贡献：cross-lingual artifact rate 达 35%（LOW 42%，MID 31%，HIGH 15%）， 首次在跨语言 probing 场景系统性应用 selectivity 检验。Selectivity 与 ZS AUROC 强相关（rho=0.65）， 暗示文献中许多 positive transfer 结果可能是 capacity artifacts。\nLinear projection 作为唯一可行方案但需 100+ pairs（非 50），且效果反转阈值 language-specific， 无法给出单一可操作的 cutoff。\n重构为 EACL negative results + methodology paper：(1) control task 方法论警告（field-level 贡献）， (2) mean-shift 不可能性证明（理论贡献），(3) distributional matching 路径全面关闭（CaCLR + CORAL + high-dim MMD 系统性 negative result），(4) linear projection 条件性实用指导（descriptive empirical 贡献）。Drop Claim 2（decomposition）和 Claim 3（CaCLR method）作为 standalone claims。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T13:39:13.091Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T13:39:13.091Z",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-21T13:39:13.110Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：7-8B pilot 的核心模式不推广到全量模型。两个 MoE 架构（Qwen3-235B, Llama 4 Scout）完全没有清晰的 Pareto frontier——MoE expert routing 打破了 dense model 中 depth→specialization 的单调映射， depth-transfer 关系在绝大多数语言为 non-monotonic 或 flat。唯一的 dense 架构（Gemma 4 31B）展现出 marginal Pareto（global rho=-0.24, p=0.038），但仅 4/20 语言 per-language 显著，且 final-layer transfer drop 微不足道（0.8pp），远不及 pilot 的 2-4pp。三架构平均 EN AUROC 0.74，处于 worst 范围中段。
Simpson's Paradox 在 20 语言全量验证中全面崩塌：3 架构的 CKA partial correlation controlling for depth 均不显著（max rho=+0.16, min p=0.09），Llama pilot 的 rho=+0.41 被确认为 5 语言 small-sample artifact。CKA 提供不了超越 depth 的解释力。Subspace angle analysis 否定了 "correctness direction is a robust language-agnostic subspace"——HIGH tier 语言 angle 15-38°，LOW tier 45-65°。
CaCLR 全面失败：β sweep 3 OOM 证实 consistency loss inert 或 harmful；CORAL 和 high-dim MMD (PCA d=50/100) 同样失败，将 negative result 从 "MMD-specific" 扩展为 "distributional matching 路径全面 关闭"。Component ablation 每加一项 loss 都 net negative。
Decomposition 无实质效果，random-direction control 产生同量级 delta（paired test p=0.38）， difficulty 和 capability 不可分。
Control task analysis 是最强贡献：cross-lingual artifact rate 达 35%（LOW 42%，MID 31%，HIGH 15%）， 首次在跨语言 probing 场景系统性应用 selectivity 检验。Selectivity 与 ZS AUROC 强相关（rho=0.65）， 暗示文献中许多 positive transfer 结果可能是 capacity artifacts。
Linear projection 作为唯一可行方案但需 100+ pairs（非 50），且效果反转阈值 language-specific， 无法给出单一可操作的 cutoff。
重构为 EACL negative results + methodology paper：(1) control task 方法论警告（field-level 贡献）， (2) mean-shift 不可能性证明（理论贡献），(3) distributional matching 路径全面关闭（CaCLR + CORAL + high-dim MMD 系统性 negative result），(4) linear projection 条件性实用指导（descriptive empirical 贡献）。Drop Claim 2（decomposition）和 Claim 3（CaCLR method）作为 standalone claims。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "4b58596c-2632-4820-9872-9c4f8b9b3bb3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T13:39:13.110Z_

```json
{
  "parentUuid": "4b58596c-2632-4820-9872-9c4f8b9b3bb3",
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
  "uuid": "c068fd84-9c8a-490a-a905-3d0394a1a72d",
  "timestamp": "2026-05-21T13:39:13.110Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T13:39:13.110Z_

```json
{
  "parentUuid": "c068fd84-9c8a-490a-a905-3d0394a1a72d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d8dd8437-7819-4148-8dc2-2b8c05ab5c25",
  "timestamp": "2026-05-21T13:39:13.110Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
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
  "aiTitle": "Generate worst-tier simulation paper for dream_20260521T122458",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Assistant

_source line 7 · 2026-05-21T13:39:16.357Z_

I'll start by reading the input files to understand the experimental data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8dd8437-7819-4148-8dc2-2b8c05ab5c25",
  "isSidechain": false,
  "requestId": "req_011CbFomduQ6DgP7nyivb2cM",
  "type": "assistant",
  "uuid": "624454ae-45f5-49cd-bd67-84828bcb765a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiHhqiEAC6ry3sVGGLaGb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12153,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12153
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

_source line 8 · 2026-05-21T13:39:16.846Z_

<details open><summary>🔧 Tool call — Read · `toolu_019H6hSwJXVynjMs1yBToCpA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "624454ae-45f5-49cd-bd67-84828bcb765a",
  "isSidechain": false,
  "requestId": "req_011CbFomduQ6DgP7nyivb2cM",
  "type": "assistant",
  "uuid": "90497761-6843-4f88-996b-fc10a096a15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiHhqiEAC6ry3sVGGLaGb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12153,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12153
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

_source line 9 · 2026-05-21T13:39:17.173Z_

<details><summary>↩ Tool result · `toolu_019H6hSwJXVynjMs1yBToCpA`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B Full Pareto Frontier",
4	    "description": "Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th), 20 typologically diverse languages, EN correctness probes (LR + MLP), 5 transfer conditions (zero-shot, mean-shift, linear projection 200 pairs, few-shot 25/100, CaCLR).\n",
5	    "results": {
6	      "en_best_auroc": 0.741,
7	      "en_best_layer": 72,
8	      "en_auroc_range": [
9	        0.601,
10	        0.741
11	      ],
12	      "en_best_ece_raw": 0.198,
13	      "zs_pass_count_auroc_gt_058": 11,
14	      "zs_pass_rate": 0.55,
15	      "zs_fail_count": 9,
16	      "mean_zs_auroc_all_20": 0.576,
17	      "mean_zs_auroc_drop_vs_en_pp": 16.5,
18	      "best_zs_auroc": {
19	        "zh": 0.668,
20	        "es": 0.675,
21	        "fr": 0.658,
22	        "de": 0.649,
23	        "ja": 0.588,
24	        "pt": 0.662,
25	        "it": 0.645,
26	        "ar": 0.608,
27	        "hi": 0.567,
28	        "ru": 0.621,
29	        "ko": 0.591,
30	        "tr": 0.548,
31	        "vi": 0.562,
32	        "th": 0.528,
33	        "sw": 0.518,
34	        "bn": 0.524,
35	        "am": 0.486,
36	        "yo": 0.475,
37	        "te": 0.502,
38	        "my": 0.468
39	      },
40	      "best_zs_layer": {
41	        "zh": 60,
42	        "es": 56,
43	        "fr": 60,
44	        "de": 52,
45	        "ja": 48,
46	        "pt": 56,
47	        "it": 56,
48	        "ar": 52,
49	        "hi": 44,
50	        "ru": 56,
51	        "ko": 48,
52	        "tr": 40,
53	        "vi": 44,
54	        "th": 36,
55	        "sw": 36,
56	        "bn": 40,
57	        "am": 32,
58	        "yo": 28,
59	        "te": 36,
60	        "my": 32
61	      },
62	      "global_spearman_rho_depth_vs_transfer": -0.12,
63	      "global_spearman_p": 0.078,
64	      "per_lang_spearman": {
65	        "zh": {
66	          "rho": -0.31,
67	          "p": 0.14
68	        },
69	        "es": {
70	          "rho": -0.25,
71	          "p": 0.24
72	        },
73	        "fr": {
74	          "rho": -0.28,
75	          "p": 0.18
76	        },
77	        "de": {
78	          "rho": -0.19,
79	          "p": 0.38
80	        },
81	        "ja": {
82	          "rho": 0.18,
83	          "p": 0.4
84	        },
85	        "pt": {
86	          "rho": -0.22,
87	          "p": 0.3
88	        },
89	        "it": {
90	          "rho": -0.16,
91	          "p": 0.46
92	        },
93	        "ar": {
94	          "rho": 0.05,
95	          "p": 0.82
96	        },
97	        "hi": {
98	          "rho": -0.41,
99	          "p": 0.046
100	        },
101	        "ru": {
102	          "rho": -0.14,
103	          "p": 0.52
104	        },
105	        "ko": {
106	          "rho": 0.25,
107	          "p": 0.24
108	        },
109	        "tr": {
110	          "rho": -0.08,
111	          "p": 0.71
112	        },
113	        "vi": {
114	          "rho": 0.09,
115	          "p": 0.68
116	        },
117	        "th": {
118	          "rho": -0.11,
119	          "p": 0.61
120	        },
121	        "sw": {
122	          "rho": -0.35,
123	          "p": 0.09
124	        },
125	        "bn": {
126	          "rho": -0.12,
127	          "p": 0.58
128	        },
129	        "am": {
130	          "rho": 0.14,
131	          "p": 0.52
132	        },
133	        "yo": {
134	          "rho": -0.02,
135	          "p": 0.93
136	        },
137	        "te": {
138	          "rho": -0.18,
139	          "p": 0.4
140	        },
141	        "my": {
142	          "rho": 0.1,
143	          "p": 0.64
144	        }
145	      },
146	      "per_lang_significant_negative_rho_count": 1,
147	      "per_lang_significant_positive_rho_count": 0,
148	      "per_lang_nonmonotonic_count": 13,
149	      "pareto_tradeoff_prevalence": 0.08,
150	      "pareto_depth_transfer_drop_final_layers_pp": 0.6,
151	      "mean_shift_delta_auroc_all": 0.0,
152	      "transfer_conditions_summary": {
153	        "zero_shot": {
154	          "mean_auroc": 0.576,
155	          "std": 0.068,
156	          "delta_vs_zs": 0.0
157	        },
158	        "mean_shift": {
159	          "mean_auroc": 0.576,
160	          "std": 0.068,
161	          "delta_vs_zs": 0.0
162	        },
163	        "linear_proj_200": {
164	          "mean_auroc": 0.612,
165	          "std": 0.055,
166	          "delta_vs_zs": 0.036
167	        },
168	        "fewshot_25": {
169	          "mean_auroc": 0.598,
170	          "std": 0.061,
171	          "delta_vs_zs": 0.022
172	        },
173	        "fewshot_100": {
174	          "mean_auroc": 0.625,
175	          "std": 0.049,
176	          "delta_vs_zs": 0.049
177	        }
178	      }
179	    },
180	    "tables": [
181	      {
182	        "name": "Table 1a: Qwen3-235B Per-Language Pareto (Depth vs ZS-AUROC Spearman ρ)",
183	        "columns": [
184	          "lang",
185	          "tier",
186	          "best_zs_auroc",
187	          "best_zs_layer",
188	          "spearman_rho",
189	          "p_value",
190	          "pattern"
191	        ],
192	        "rows": [
193	          [
194	            "zh",
195	            "HIGH",
196	            0.668,
197	            60,
198	            -0.31,
199	            0.14,
200	            "weak negative"
201	          ],
202	          [
203	            "es",
204	            "HIGH",
205	            0.675,
206	            56,
207	            -0.25,
208	            0.24,
209	            "n.s."
210	          ],
211	          [
212	            "fr",
213	            "HIGH",
214	            0.658,
215	            60,
216	            -0.28,
217	            0.18,
218	            "n.s."
219	          ],
220	          [
221	            "de",
222	            "HIGH",
223	            0.649,
224	            52,
225	            -0.19,
226	            0.38,
227	            "n.s."
228	          ],
229	          [
230	            "ja",
231	            "HIGH",
232	            0.588,
233	            48,
234	            0.18,
235	            0.4,
236	            "non-monotonic U-shape"
237	          ],
238	          [
239	            "pt",
240	            "HIGH",
241	            0.662,
242	            56,
243	            -0.22,
244	            0.3,
245	            "n.s."
246	          ],
247	          [
248	            "it",
249	            "HIGH",
250	            0.645,
251	            56,
252	            -0.16,
253	            0.46,
254	            "n.s."
255	          ],
256	          [
257	            "ar",
258	            "MID",
259	            0.608,
260	            52,
261	            0.05,
262	            0.82,
263	            "flat"
264	          ],
265	          [
266	            "hi",
267	            "MID",
268	            0.567,
269	            44,
270	            -0.41,
271	            0.046,
272	            "significant negative"
273	          ],
274	          [
275	            "ru",
276	            "MID",
277	            0.621,
278	            56,
279	            -0.14,
280	            0.52,
281	            "n.s."
282	          ],
283	          [
284	            "ko",
285	            "MID",
286	            0.591,
287	            48,
288	            0.25,
289	            0.24,
290	            "inverted—deeper helps"
291	          ],
292	          [
293	            "tr",
294	            "MID",
295	            0.548,
296	            40,
297	            -0.08,
298	            0.71,
299	            "n.s."
300	          ],
301	          [
302	            "vi",
303	            "MID",
304	            0.562,
305	            44,
306	            0.09,
307	            0.68,
308	            "flat"
309	          ],
310	          [
311	            "th",
312	            "MID",
313	            0.528,
314	            36,
315	            -0.11,
316	            0.61,
317	            "n.s."
318	          ],
319	          [
320	            "sw",
321	            "LOW",
322	            0.518,
323	            36,
324	            -0.35,
325	            0.09,
326	            "marginal negative"
327	          ],
328	          [
329	            "bn",
330	            "LOW",
331	            0.524,
332	            40,
333	            -0.12,
334	            0.58,
335	            "n.s."
336	          ],
337	          [
338	            "am",
339	            "LOW",
340	            0.486,
341	            32,
342	            0.14,
343	            0.52,
344	            "non-monotonic"
345	          ],
346	          [
347	            "yo",
348	            "LOW",
349	            0.475,
350	            28,
351	            -0.02,
352	            0.93,
353	            "noisy flat"
354	          ],
355	          [
356	            "te",
357	            "LOW",
358	            0.502,
359	            36,
360	            -0.18,
361	            0.4,
362	            "n.s."
363	          ],
364	          [
365	            "my",
366	            "LOW",
367	            0.468,
368	            32,
369	            0.1,
370	            0.64,
371	            "non-monotonic"
372	          ]
373	        ]
374	      },
375	      {
376	        "name": "Table 1b: Qwen3-235B Transfer Conditions Summary (20 langs, EN-optimal layer)",
377	        "columns": [
378	          "condition",
379	          "mean_auroc",
380	          "std",
381	          "delta_vs_zs",
382	          "significant_improvement_count"
383	        ],
384	        "rows": [
385	          [
386	            "zero-shot",
387	            0.576,
388	            0.068,
389	            "—",
390	            "—"
391	          ],
392	          [
393	            "mean-shift",
394	            0.576,
395	            0.068,
396	            0.0,
397	            "0/20"
398	          ],
399	          [
400	            "linear_proj_200",
401	            0.612,
402	            0.055,
403	            0.036,
404	            "11/20"
405	          ],
406	          [
407	            "fewshot_25",
408	            0.598,
409	            0.061,
410	            0.022,
411	            "7/20"
412	          ],
413	          [
414	            "fewshot_100",
415	            0.625,
416	            0.049,
417	            0.049,
418	            "13/20"
419	          ]
420	        ]
421	      }
422	    ],
423	    "figures": [],
424	    "analysis": "Qwen3-235B 的 Pareto frontier 远不如 Qwen2.5-7B pilot 清晰。MoE expert routing 打破了 dense model 中 depth = specialization 的单调映射。Pilot 的 clear Pareto（L27 EN best 但 transfer drops 2-4pp vs L24）是 dense 7B model 的特殊现象。仅 1/20 语言达到 per-language 显著性（hi），且部分语言方向反转——depth-transfer tradeoff 不是普遍现象。对 Claim 1 构成 严重挑战：不能声称 Qwen 系列存在 consistent Pareto。\n\n\nEN best AUROC 0.741 在 worst 范围 [0.72, 0.78] 内——Qwen3-235B 的 22B active parameters 对 correctness signal 的编码不显著优于 7B pilot（0.754），因为 correctness direction 的信号 强度主要由 pretraining data 质量和 MCQA 格式暴露量决定，而非模型 scale。INT4 量化引入 ~1pp 额外损耗。\nZS pass 11/20 (55%) 处于 worst 范围 [8, 13] 中段。MoE routing 导致不同语言被路由到 不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱：pilot 中 Qwen2.5-7B dense 架构的 4/5 pass 不能外推，因为 dense model 的 shared representation 天然更有利于 cross-lingual alignment。低资源语言（am, yo, my）的 best ZS AUROC < 0.50，接近 random。\nGlobal Pareto rho=-0.12 (p=0.078) 仅 marginally significant：depth-transfer tradeoff 在 MoE 中不成立，因为 expert routing 在不同深度可以 \"重置\" 语言特异性——L48 的 expert allocation 可能与 L72 完全不同，打破了 \"deeper = more specialized\" 的 dense-model 假设。13/20 语言呈现 non-monotonic 模式（U形、锯齿形、plateau），这是 MoE 的结构性特征而非噪声。仅 hi 达到 per-language significant negative rho（p=0.046），ko 和 ja 方向反转（deeper helps transfer）。\nFinal-layer transfer drop 仅 0.6pp（worst 范围 [0.0, 1.5]），远低于 pilot 的 2-4pp—— 235B MoE 的最深层 expert routing 已经足够 specialized，EN probe 在这些层的 AUROC 提升本身就很小（L88 vs L72 仅 +0.3pp EN AUROC），所以 transfer drop 也被压缩。\nMean-shift ΔAUROC ≡ 0 符合已证明的 rank-invariance。Linear projection +3.6pp 和 few-shot 100 +4.9pp 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言。\n"
425	  },
426	  {
427	    "name": "Llama 4 Scout Full Pareto Frontier",
428	    "description": "Llama 4 Scout (48 layers, 17B-16E MoE, W4A16), 12 probed layers (every 4th), 20 languages, 5 transfer conditions.\n",
429	    "results": {
430	      "en_best_auroc": 0.718,
431	      "en_best_layer": 40,
432	      "en_auroc_range": [
433	        0.615,
434	        0.718
435	      ],
436	      "en_best_ece_raw": 0.215,
437	      "zs_pass_count_auroc_gt_058": 9,
438	      "zs_pass_rate": 0.45,
439	      "mean_zs_auroc_all_20": 0.562,
440	      "mean_zs_auroc_drop_vs_en_pp": 15.6,
441	      "best_zs_auroc": {
442	        "zh": 0.648,
443	        "es": 0.655,
444	        "fr": 0.642,
445	        "de": 0.635,
446	        "ja": 0.562,
447	        "pt": 0.648,
448	        "it": 0.631,
449	        "ar": 0.588,
450	        "hi": 0.548,
451	        "ru": 0.608,
452	        "ko": 0.575,
453	        "tr": 0.531,
454	        "vi": 0.558,
455	        "th": 0.515,
456	        "sw": 0.501,
457	        "bn": 0.508,
458	        "am": 0.472,
459	        "yo": 0.458,
460	        "te": 0.491,
461	        "my": 0.452
462	      },
463	      "global_spearman_rho_depth_vs_transfer": -0.06,
464	      "global_spearman_p": 0.31,
465	      "per_lang_significant_negative_rho_count": 0,
466	      "per_lang_significant_positive_rho_count": 0,
467	      "per_lang_nonmonotonic_count": 8,
468	      "pareto_tradeoff_prevalence": 0.05,
469	      "pareto_depth_transfer_drop_final_layers_pp": 0.3,
470	      "mean_shift_delta_auroc_all": 0.0,
471	      "transfer_conditions_summary": {
472	        "zero_shot": {
473	          "mean_auroc": 0.562,
474	          "std": 0.065,
475	          "delta_vs_zs": 0.0
476	        },
477	        "mean_shift": {
478	          "mean_auroc": 0.562,
479	          "std": 0.065,
480	          "delta_vs_zs": 0.0
481	        },
482	        "linear_proj_200": {
483	          "mean_auroc": 0.598,
484	          "std": 0.052,
485	          "delta_vs_zs": 0.036
486	        },
487	        "fewshot_25": {
488	          "mean_auroc": 0.584,
489	          "std": 0.058,
490	          "delta_vs_zs": 0.022
491	        },
492	        "fewshot_100": {
493	          "mean_auroc": 0.611,
494	          "std": 0.048,
495	          "delta_vs_zs": 0.049
496	        }
497	      }
498	    },
499	    "tables": [
500	      {
501	        "name": "Table 2a: Llama 4 Scout Per-Language Pareto Spearman ρ",
502	        "columns": [
503	          "lang",
504	          "tier",
505	          "best_zs_auroc",
506	          "spearman_rho",
507	          "p_value"
508	        ],
509	        "rows": [
510	          [
511	            "zh",
512	            "HIGH",
513	            0.648,
514	            -0.18,
515	            0.58
516	          ],
517	          [
518	            "es",
519	            "HIGH",
520	            0.655,
521	            -0.12,
522	            0.71
523	          ],
524	          [
525	            "fr",
526	            "HIGH",
527	            0.642,
528	            -0.22,
529	            0.49
530	          ],
531	          [
532	            "de",
533	            "HIGH",
534	            0.635,
535	            -0.08,
536	            0.81
537	          ],
538	          [
539	            "ja",
540	            "HIGH",
541	            0.562,
542	            0.32,
543	            0.31
544	          ],
545	          [
546	            "pt",
547	            "HIGH",
548	            0.648,
549	            -0.15,
550	            0.64
551	          ],
552	          [
553	            "it",
554	            "HIGH",
555	            0.631,
556	            -0.05,
557	            0.88
558	          ],
559	          [
560	            "ar",
561	            "MID",
562	            0.588,
563	            0.22,
564	            0.49
565	          ],
566	          [
567	            "hi",
568	            "MID",
569	            0.548,
570	            -0.38,
571	            0.22
572	          ],
573	          [
574	            "ru",
575	            "MID",
576	            0.608,
577	            -0.02,
578	            0.95
579	          ],
580	          [
581	            "ko",
582	            "MID",
583	            0.575,
584	            0.35,
585	            0.26
586	          ],
587	          [
588	            "tr",
589	            "MID",
590	            0.531,
591	            0.08,
592	            0.81
593	          ],
594	          [
595	            "vi",
596	            "MID",
597	            0.558,
598	            0.12,
599	            0.71
600	          ],
601	          [
602	            "th",
603	            "MID",
604	            0.515,
605	            -0.18,
606	            0.58
607	          ],
608	          [
609	            "sw",
610	            "LOW",
611	            0.501,
612	            -0.25,
613	            0.43
614	          ],
615	          [
616	            "bn",
617	            "LOW",
618	            0.508,
619	            -0.08,
620	            0.81
621	          ],
622	          [
623	            "am",
624	            "LOW",
625	            0.472,
626	            0.02,
627	            0.95
628	          ],
629	          [
630	            "yo",
631	            "LOW",
632	            0.458,
633	            -0.12,
634	            0.71
635	          ],
636	          [
637	            "te",
638	            "LOW",
639	            0.491,
640	            -0.05,
641	            0.88
642	          ],
643	          [
644	            "my",
645	            "LOW",
646	            0.452,
647	            0.15,
648	            0.64
649	          ]
650	        ]
651	      },
652	      {
653	        "name": "Table 2b: Llama 4 Scout Transfer Conditions Summary",
654	        "columns": [
655	          "condition",
656	          "mean_auroc",
657	          "delta_vs_zs",
658	          "significant_count"
659	        ],
660	        "rows": [
661	          [
662	            "zero-shot",
663	            0.562,
664	            "—",
665	            "—"
666	          ],
667	          [
668	            "mean-shift",
669	            0.562,
670	            0.0,
671	            "0/20"
672	          ],
673	          [
674	            "linear_proj_200",
675	            0.598,
676	            0.036,
677	            "10/20"
678	          ],
679	          [
680	            "fewshot_25",
681	            0.584,
682	            0.022,
683	            "6/20"
684	          ],
685	          [
686	            "fewshot_100",
687	            0.611,
688	            0.049,
689	            "12/20"
690	          ]
691	        ]
692	      }
693	    ],
694	    "figures": [],
695	    "analysis": "Llama 4 Scout 确认 MoE 架构的 Pareto 缺失。与 Qwen3 合并看：0 个 MoE 架构在 p<0.05 展现 Pareto。MVP 中 Llama-3.1-8B 的弱 Pareto 是 dense 架构特有的。两个 MoE 结合表明 expert routing 是 Pareto 缺失的结构性原因，而非偶然。\n\n\nLlama 4 Scout EN best AUROC 0.718 在 worst 范围低端——active parameters 17B 但 16 experts 的稀疏激活使得每个 token 实际使用的参数量有限，correctness signal 在 expert 间被稀释。W4A16 量化额外损耗 ~0.5-1pp。\nZS pass 9/20 (45%)，比 Qwen3 低因为：(1) Llama 4 Scout 的 multilingual pretraining 比例可能低于 Qwen3（Qwen 系列历来强调多语言）；(2) 16-expert MoE 的 expert specialization 程度更高，语言间 representation divergence 更大。MVP 中 Llama-3.1-8B dense 的 5/5 pass 不推广——8B dense → Scout MoE 的架构变化比 scale change 更根本。\nGlobal Pareto rho=-0.06 (p=0.31) 完全不显著，0/20 语言 per-language 显著。仅 12 probed layers 使 per-language Spearman 功效极低（n=12），但即使考虑 power 问题，effect sizes 也很小 （max |rho| = 0.38）。Scout 的 expert routing 比 Qwen3 更激进（16 experts vs Qwen3 的 设计），导致 depth-transfer 关系更加 noisy。\nFinal-layer drop 仅 0.3pp——transfer 在 L40-L48 区间几乎 flat，没有 tradeoff 可言。\n"
696	  },
697	  {
698	    "name": "Gemma 4 31B Dense Pareto Frontier",
699	    "description": "Gemma 4 31B Dense (60 text layers, BF16 无量化), 16 probed layers (every 4th + final), 20 languages, 5 transfer conditions. Dense vs MoE 对照。\n",
700	    "results": {
701	      "en_best_auroc": 0.755,
702	      "en_best_layer": 52,
703	      "en_auroc_range": [
704	        0.618,
705	        0.755
706	      ],
707	      "en_best_ece_raw": 0.188,
708	      "zs_pass_count_auroc_gt_058": 12,
709	      "zs_pass_rate": 0.6,
710	      "mean_zs_auroc_all_20": 0.585,
711	      "mean_zs_auroc_drop_vs_en_pp": 17.0,
712	      "best_zs_auroc": {
713	        "zh": 0.682,
714	        "es": 0.691,
715	        "fr": 0.672,
716	        "de": 0.665,
717	        "ja": 0.598,
718	        "pt": 0.678,
719	        "it": 0.658,
720	        "ar": 0.618,
721	        "hi": 0.575,
722	        "ru": 0.635,
723	        "ko": 0.602,
724	        "tr": 0.558,
725	        "vi": 0.572,
726	        "th": 0.538,
727	        "sw": 0.525,
728	        "bn": 0.531,
729	        "am": 0.492,
730	        "yo": 0.481,
731	        "te": 0.508,
732	        "my": 0.475
733	      },
734	      "global_spearman_rho_depth_vs_transfer": -0.24,
735	      "global_spearman_p": 0.038,
736	      "per_lang_significant_negative_rho_count": 4,
737	      "per_lang_significant_positive_rho_count": 0,
738	      "per_lang_nonmonotonic_count": 5,
739	      "pareto_tradeoff_prevalence": 0.22,
740	      "pareto_depth_transfer_drop_final_layers_pp": 0.8,
741	      "spearman_depth_vs_transfer_rho_positive_langs": 10,
742	      "transfer_conditions_summary": {
743	        "zero_shot": {
744	          "mean_auroc": 0.585,
745	          "std": 0.063,
746	          "delta_vs_zs": 0.0
747	        },
748	        "mean_shift": {
749	          "mean_auroc": 0.585,
750	          "std": 0.063,
751	          "delta_vs_zs": 0.0
752	        },
753	        "linear_proj_200": {
754	          "mean_auroc": 0.621,
755	          "std": 0.051,
756	          "delta_vs_zs": 0.036
757	        },
758	        "fewshot_25": {
759	          "mean_auroc": 0.607,
760	          "std": 0.057,
761	          "delta_vs_zs": 0.022
762	        },
763	        "fewshot_100": {
764	          "mean_auroc": 0.634,
765	          "std": 0.045,
766	          "delta_vs_zs": 0.049
767	        }
768	      }
769	    },
770	    "tables": [
771	      {
772	        "name": "Table 3: Gemma 4 31B Dense Pareto Summary",
773	        "columns": [
774	          "metric",
775	          "value"
776	        ],
777	        "rows": [
778	          [
779	            "en_best_auroc",
780	            0.755
781	          ],
782	          [
783	            "en_best_layer",
784	            "L52 (87% depth)"
785	          ],
786	          [
787	            "zs_pass_rate",
788	            "60% (12/20)"
789	          ],
790	          [
791	            "global_pareto_rho",
792	            "-0.24 (p=0.038)"
793	          ],
794	          [
795	            "per_lang_significant_rho",
796	            "4/20 (zh, fr, hi, sw)"
797	          ],
798	          [
799	            "final_layer_transfer_drop_pp",
800	            0.8
801	          ],
802	          [
803	            "control_artifact_rate_LOW",
804	            "38%"
805	          ],
806	          [
807	            "no_quantization_confound",
808	            "BF16 — no quantization artifact"
809	          ]
810	        ]
811	      },
812	      {
813	        "name": "Table 3b: Dense vs MoE Architecture Comparison",
814	        "columns": [
815	          "metric",
816	          "Qwen3 (MoE)",
817	          "Llama4 (MoE)",
818	          "Gemma4 (Dense)"
819	        ],
820	        "rows": [
821	          [
822	            "en_best_auroc",
823	            0.741,
824	            0.718,
825	            0.755
826	          ],
827	          [
828	            "global_pareto_rho",
829	            "-0.12 (n.s.)",
830	            "-0.06 (n.s.)",
831	            "-0.24 (p=0.038)"
832	          ],
833	          [
834	            "per_lang_sig_count",
835	            "1/20",
836	            "0/20",
837	            "4/20"
838	          ],
839	          [
840	            "non_monotonic_langs",
841	            "13/20",
842	            "8/20",
843	            "5/20"
844	          ],
845	          [
846	            "final_layer_drop_pp",
847	            0.6,
848	            0.3,
849	            0.8
850	          ],
851	          [
852	            "zs_pass_rate",
853	            "55%",
854	            "45%",
855	            "60%"
856	          ]
857	        ]
858	      }
859	    ],
860	    "figures": [],
861	    "analysis": "Dense vs MoE 对比是 Gemma 最大的贡献：dense 架构确实有 cleaner depth-transfer 关系， 但 effect size 远小于 pilot 预期。三架构综合 pareto_tradeoff_prevalence ≈ 0.12 (12% of lang-arch pairs)，在 worst 范围 [0.05, 0.25] 内。 结论：Pareto 是 architecture-conditional 的，不是 universal finding——这使得 Claim 1 从 \"discovery\" 降级为 \"architecture-dependent observational note\"。\n\n\nGemma 4 31B Dense 是唯一有 marginal Pareto 的架构。Dense 架构没有 expert routing， depth→specialization 映射更单调，因此 global rho=-0.24 (p=0.038) 达到 significance。 4/20 语言 per-language 显著（zh, fr, hi, sw）——全部是负 rho（deeper layers = worse transfer）， 符合 specialization 叙述。\n但这反而增加了叙述复杂性：Pareto 是 architecture-dependent 的（dense 有，MoE 没有）， 无法声称是普遍现象。且 final-layer drop 仅 0.8pp——远低于 pilot 的 2-4pp，因为 31B dense model 的最深层已经足够 expressive，EN probe 的边际 AUROC 提升很小（L56→L60 仅 +0.4pp）， 相应 transfer 损失也被压缩。\nEN AUROC 0.755 略高于两个 MoE（因无量化损耗 + BF16 保留更多信号精度），三架构均值 (0.741 + 0.718 + 0.755)/3 = 0.738，在 worst 范围 [0.72, 0.78] 内。\nZS pass 12/20 (60%)——三架构最高，因为 Gemma 4 的 multilingual pretraining 可能 更均衡（Apache 2.0 开源模型通常 training data 更 curated），且无量化损耗。\n"
862	  },
863	  {
864	    "name": "CaCLR Implementation and Comparative Evaluation",
865	    "description": "CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD), β sweep 3 OOM, α sweep, component ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion. vs 4 baselines, 3 models × 20 langs.\n",
866	    "results": {
867	      "caclr_mean_delta_auroc_vs_zs": -0.008,
868	      "caclr_langs_improved_of_20": 4,
869	      "caclr_best_beta": "none — all β inert or harmful",
870	      "beta_sweep": {
871	        "beta_0.001": {
872	          "mean_delta_auroc": -0.002,
873	          "std": 0.016
874	        },
875	        "beta_0.01": {
876	          "mean_delta_auroc": -0.005,
877	          "std": 0.019
878	        },
879	        "beta_0.1": {
880	          "mean_delta_auroc": -0.009,
881	          "std": 0.023
882	        },
883	        "beta_1.0": {
884	          "mean_delta_auroc": -0.016,
885	          "std": 0.028
886	        }
887	      },
888	      "alpha_sweep": {
889	        "alpha_0.01": {
890	          "delta_auroc": -0.001,
891	          "delta_ece": 0.006
892	        },
893	        "alpha_0.1": {
894	          "delta_auroc": -0.004,
895	          "delta_ece": 0.002
896	        },
897	        "alpha_1.0": {
898	          "delta_auroc": -0.01,
899	          "delta_ece": -0.001
900	        },
901	        "alpha_10.0": {
902	          "delta_auroc": -0.025,
903	          "delta_ece": -0.004
904	        }
905	      },
906	      "component_ablation": {
907	        "bce_only": {
908	          "delta_vs_zs": -0.001,
909	          "note": "≈ ZS baseline"
910	        },
911	        "bce_plus_sbece": {
912	          "delta_vs_zs": -0.005,
913	          "note": "SB-ECE hurts discrimination"
914	        },
915	        "bce_plus_mmd_1d": {
916	          "delta_vs_zs": -0.004,
917	          "note": "1-D MMD inert/harmful"
918	        },
919	        "bce_plus_mmd_pca50": {
920	          "delta_vs_zs": -0.006,
921	          "note": "50-D MMD also fails"
922	        },
923	        "bce_plus_mmd_pca100": {
924	          "delta_vs_zs": -0.008,
925	          "note": "100-D MMD worse — curse of dimensionality"
926	        },
927	        "bce_plus_coral": {
928	          "delta_vs_zs": -0.005,
929	          "note": "CORAL fails — second-order alignment insufficient"
930	        },
931	        "bce_plus_coral_pca50": {
932	          "delta_vs_zs": -0.007,
933	          "note": "high-dim CORAL also fails"
934	        },
935	        "full_caclr": {
936	          "delta_vs_zs": -0.008,
937	          "note": "compound degradation"
938	        }
939	      },
940	      "multi_seed_std": {
941	        "caclr": 0.003,
942	        "fewshot_25": 0.008,
943	        "fewshot_100": 0.005,
944	        "procrustes": 0.002
945	      },
946	      "mixed_beta_criterion_result": "β selected on zh+sw validation matches English-only selection (β=0.001). No evidence of systematic bias against cross-lingual benefit.\n",
947	      "five_way_comparison": {
948	        "zero_shot": {
949	          "mean_auroc": 0.574,
950	          "mean_ece": 0.282
951	        },
952	        "mean_shift": {
953	          "mean_auroc": 0.574,
954	          "mean_ece": 0.288
955	        },
956	        "caclr_best": {
957	          "mean_auroc": 0.566,
958	          "mean_ece": 0.275
959	        },
960	        "linear_proj_200": {
961	          "mean_auroc": 0.61,
962	          "mean_ece": 0.245
963	        },
964	        "fewshot_25": {
965	          "mean_auroc": 0.596,
966	          "mean_ece": 0.258
967	        },
968	        "fewshot_100": {
969	          "mean_auroc": 0.623,
970	          "mean_ece": 0.232
971	        }
972	      },
973	      "implementation_spec": {
974	        "mmd_kernel": "Gaussian RBF, bandwidth=median heuristic",
975	        "optimizer": "Adam, lr=1e-3, cosine schedule to 1e-5",
976	        "epochs": 50,
977	        "early_stopping": "patience=10 on held-out English BCE loss",
978	        "initialization": "from standard LR solution",
979	        "batch_size": 256,
980	        "mmd_items": "same items as BCE (probe_train 70% split)",
981	        "parallel_set_size_range": [
982	          618,
983	          2852
984	        ]
985	      }
986	    },
987	    "tables": [
988	      {
989	        "name": "Table 4a: CaCLR β Sweep (3 architectures × 20 langs, EN-optimal layer)",
990	        "columns": [
991	          "beta",
992	          "mean_auroc",
993	          "delta_vs_zs",
994	          "pct_improved",
995	          "pct_harmed"
996	        ],
997	        "rows": [
998	          [
999	            0.001,
1000	            0.572,
1001	            -0.002,
1002	            "30%",
1003	            "42%"
1004	          ],
1005	          [
1006	            0.01,
1007	            0.569,
1008	            -0.005,
1009	            "25%",
1010	            "52%"
1011	          ],
1012	          [
1013	            0.1,
1014	            0.565,
1015	            -0.009,
1016	            "18%",
1017	            "62%"
1018	          ],
1019	          [
1020	            1.0,
1021	            0.558,
1022	            -0.016,
1023	            "12%",
1024	            "75%"
1025	          ]
1026	        ]
1027	      },
1028	      {
1029	        "name": "Table 4b: Distributional Matching Comprehensive Ablation",
1030	        "columns": [
1031	          "method",
1032	          "dimensionality",
1033	          "mean_delta_auroc",
1034	          "note"
1035	        ],
1036	        "rows": [
1037	          [
1038	            "MMD (logit)",
1039	            "1-D",
1040	            -0.004,
1041	            "marginal match, no conditional alignment"
1042	          ],
1043	          [
1044	            "MMD (PCA-50)",
1045	            "50-D",
1046	            -0.006,
1047	            "underpowered MMD in 50-D"
1048	          ],
1049	          [
1050	            "MMD (PCA-100)",
1051	            "100-D",
1052	            -0.008,
1053	            "curse of dimensionality"
1054	          ],
1055	          [
1056	            "CORAL (logit)",
1057	            "1-D",
1058	            -0.005,
1059	            "second-order alignment insufficient"
1060	          ],
1061	          [
1062	            "CORAL (PCA-50)",
1063	            "50-D",
1064	            -0.007,
1065	            "covariance match fails"
1066	          ],
1067	          [
1068	            "Linear projection",
1069	            "full-D Procrustes",
1070	            0.036,
1071	            "learns subspace rotation directly"
1072	          ]
1073	        ]
1074	      },
1075	      {
1076	        "name": "Table 4c: 5-Way Transfer Comparison (3 arch × 20 langs)",
1077	        "columns": [
1078	          "condition",
1079	          "mean_auroc",
1080	          "mean_ece",
1081	          "delta_auroc_vs_zs",
1082	          "win_rate_vs_zs"
1083	        ],
1084	        "rows": [
1085	          [
1086	            "zero-shot",
1087	            0.574,
1088	            0.282,
1089	            "—",
1090	            "—"
1091	          ],
1092	          [
1093	            "mean-shift",
1094	            0.574,
1095	            0.288,
1096	            0.0,
1097	            "0%"
1098	          ],
1099	          [
1100	            "CaCLR (best)",
1101	            0.566,
1102	            0.275,
1103	            -0.008,
1104	            "20%"
1105	          ],
1106	          [
1107	            "linear_proj_200",
1108	            0.61,
1109	            0.245,
1110	            0.036,
1111	            "70%"
1112	          ],
1113	          [
1114	            "fewshot_25",
1115	            0.596,
1116	            0.258,
1117	            0.022,
1118	            "52%"
1119	          ],
1120	          [
1121	            "fewshot_100",
1122	            0.623,
1123	            0.232,
1124	            0.049,
1125	            "75%"
1126	          ]
1127	        ]
1128	      }
1129	    ],
1130	    "figures": [],
1131	    "analysis": "CaCLR 的全面 negative result 是 worst tier 的核心贡献之一。关键升级：CORAL + high-dim MMD 将 scope 从 \"MMD fails\" 扩展为 \"distributional matching path is closed\"。这比仅报告 1-D MMD 失败有力得多——reviewer 无法反驳说 \"换个 kernel/提高维度就行\"。 Distributional matching ablation table (Table 4b) 是该 claim 的 anchor evidence。 CKA subspace 解释也不成立（plan_011），所以 geometric rationalization 也失败—— 不仅方法失败，elegant 解释也失败。但完整的 implementation spec + sweep + ablation 确保 reproducibility，使 negative result 可信。\n\n\nCaCLR 失败的根本原因链：\n(1) 1-D MMD 结构性限制：probe logit 是标量，MMD 只能 match 两个 1-D 分布的 marginal。 即使 marginal 被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect) 仍然不同——Zhao et al. (2019) 的理论预测在此得到验证。β 越大，logits 被拉向无区分性的 marginal match，discrimination 下降。\n(2) High-dim MMD (PCA d=50/100) 同样失败：curse of dimensionality 使得 Gaussian RBF kernel 在 50-100 维空间的 MMD estimate 方差极大，有效样本量不足（probe_train ~2000 samples 对 100 维 MMD 来说 severely underpowered）。d=100 比 d=50 更差，证实这一解释。\n(3) CORAL 也失败：second-order alignment（match mean + covariance）比 MMD 更受 conditional distribution mismatch 的影响——对齐 marginal moments 不能修复 correctness signal 的 conditional structure 差异。CORAL 在 domain adaptation 中成功的条件是 covariate shift （P(X) changes, P(Y|X) stable），但 cross-lingual correctness probing 违反这一条件 （P(correct|representation) 在不同语言中不同）。\n(4) Component ablation 证实每个额外 loss 都是 net negative：BCE-only retrain ≈ ZS baseline（LR solution 初始化后 Adam 微调不改变 optimum），每加一项都引入额外 noise 而 无 signal。CaCLR 不是超参选择问题而是方法论层面的失败。\n(5) Multi-seed 结果稳定（std=0.003），排除了 single-seed 偶然性。Mixed β criterion 排除了 β selection 对 cross-lingual benefit 的系统性偏见。\n综合：distributional matching 路径（MMD + CORAL，low-dim + high-dim）被全面关闭。 Linear projection 和 few-shot 显著优于 CaCLR，因为它们直接利用 target-language 结构 信息而非试图间接 match distributions。\n"
1132	  },
1133	  {
1134	    "name": "Difficulty-Controlled Decomposition Ablation",
1135	    "description": "IRT difficulty probes → project out difficulty direction → retrain correctness probes on residuals → evaluate transfer. 10 representative languages × 8 representative layers × 3 models. Random-direction control.\n",
1136	    "results": {
1137	      "decomp_transfer_improvement_pp": 0.2,
1138	      "decomp_transfer_improvement_range": [
1139	        -0.8,
1140	        1.2
1141	      ],
1142	      "random_direction_control_delta_pp": -0.1,
1143	      "random_direction_control_range": [
1144	        -1.0,
1145	        0.8
1146	      ],
1147	      "decomp_vs_random_paired_test_p": 0.38,
1148	      "difficulty_probe_r2": 0.28,
1149	      "decomp_langs_showing_clean_separation": 2,
1150	      "per_tier_results": {
1151	        "HIGH": {
1152	          "mean_delta_pp": 0.3,
1153	          "significant": "0/4",
1154	          "clean_separation": 1
1155	        },
1156	        "MID": {
1157	          "mean_delta_pp": 0.1,
1158	          "significant": "0/3",
1159	          "clean_separation": 1
1160	        },
1161	        "LOW": {
1162	          "mean_delta_pp": -0.2,
1163	          "significant": "0/3",
1164	          "clean_separation": 0
1165	        }
1166	      }
1167	    },
1168	    "tables": [
1169	      {
1170	        "name": "Table 5: Difficulty Decomposition Ablation (3 models mean)",
1171	        "columns": [
1172	          "lang",
1173	          "tier",
1174	          "original_zs",
1175	          "after_proj",
1176	          "delta_pp",
1177	          "random_ctrl_delta_pp",
1178	          "paired_p"
1179	        ],
1180	        "rows": [
1181	          [
1182	            "zh",
1183	            "HIGH",
1184	            0.666,
1185	            0.67,
1186	            0.4,
1187	            0.1,
1188	            0.45
1189	          ],
1190	          [
1191	            "es",
1192	            "HIGH",
1193	            0.674,
1194	            0.676,
1195	            0.2,
1196	            -0.1,
1197	            0.58
1198	          ],
1199	          [
1200	            "fr",
1201	            "HIGH",
1202	            0.657,
1203	            0.66,
1204	            0.3,
1205	            0.2,
1206	            0.82
1207	          ],
1208	          [
1209	            "de",
1210	            "HIGH",
1211	            0.65,
1212	            0.652,
1213	            0.2,
1214	            -0.2,
1215	            0.41
1216	          ],
1217	          [
1218	            "hi",
1219	            "MID",
1220	            0.563,
1221	            0.565,
1222	            0.2,
1223	            0.3,
1224	            0.91
1225	          ],
1226	          [
1227	            "ru",
1228	            "MID",
1229	            0.621,
1230	            0.622,
1231	            0.1,
1232	            -0.2,
1233	            0.52
1234	          ],
1235	          [
1236	            "ko",
1237	            "MID",
1238	            0.589,
1239	            0.598,
1240	            0.9,
1241	            0.2,
1242	            0.08
1243	          ],
1244	          [
1245	            "tr",
1246	            "MID",
1247	            0.546,
1248	            0.54,
1249	            -0.6,
1250	            -0.4,
1251	            0.65
1252	          ],
1253	          [
1254	            "sw",
1255	            "LOW",
1256	            0.515,
1257	            0.51,
1258	            -0.5,
1259	            -0.3,
1260	            0.71
1261	          ],
1262	          [
1263	            "bn",
1264	            "LOW",
1265	            0.521,
1266	            0.519,
1267	            -0.2,
1268	            0.0,
1269	            0.68
1270	          ]
1271	        ]
1272	      }
1273	    ],
1274	    "figures": [],
1275	    "analysis": "Decomposition null result 与 random control 不可区分。Claim 2 被否定。 在 worst tier paper 中这成为另一条被关闭的路径，但不需要大篇幅—— 1 table + 1 figure 在 Section 5.2 用 1 paragraph 报告即可。\n\n\nDecomposition 在 worst tier 无实质效果，两个层面的失败：\n(1) Difficulty direction 在 LLM representation 中编码不够 linear/集中——IRT difficulty probe R²=0.28（低），意味着 linear projection 只捕获了 difficulty variance 的 28%。 剩余 72% 的 difficulty 信息分布在 correctness direction 也占据的子空间中——两者高度 纠缠，projecting out 28% 的 difficulty 同时损坏了部分 correctness signal。\n(2) Random-direction control 产生同量级效果（paired test p=0.38），这是 worst tier 的 killer finding：观察到的微小 delta 主要来自 dimensionality reduction 效应 （投影去除任意方向都会改变 probe 性能 ≈ 同量级），而非 difficulty-specific 信号去除。\n2/10 语言 \"clean separation\"（zh, ko）可能是 type-I error 在 10 次检验中的自然出现率。 LOW tier 3 语言全部 negative delta——它们的 difficulty 和 capability 信号本身就很弱， 投影去除任何方向只会损失信息。\n结论：transfer degradation 不能分解为 difficulty-shared + capability-specific 两个可操作的 component——Claim 2 被否定，decomposition 从 standalone claim 降级。\n"
1276	  },
1277	  {
1278	    "name": "Cross-Lingual Orthogonality Analysis",
1279	    "description": "Correctness-confidence cosine similarity, 20 languages × 2 architectures (Qwen3 + Llama4), resource-tier 和 language family 分析.\n",
1280	    "results": {
1281	      "mean_cosine_high": 0.035,
1282	      "mean_cosine_mid": 0.062,
1283	      "mean_cosine_low": 0.108,
1284	      "std_cosine_low": 0.078,
1285	      "cosine_range_all": [
1286	        0.012,
1287	        0.192
1288	      ],
1289	      "architecture_agreement_rate": 0.65,
1290	      "outlier_langs": [
1291	        "am",
1292	        "yo",
1293	        "my"
1294	      ]
1295	    },
1296	    "tables": [
1297	      {
1298	        "name": "Table 6: Correctness-Confidence Orthogonality by Resource Tier",
1299	        "columns": [
1300	          "tier",
1301	          "n_langs",
1302	          "mean_cosine",
1303	          "std",
1304	          "min",
1305	          "max",
1306	          "arch_agreement"
1307	        ],
1308	        "rows": [
1309	          [
1310	            "HIGH",
1311	            7,
1312	            0.035,
1313	            0.012,
1314	            0.012,
1315	            0.052,
1316	            "6/7"
1317	          ],
1318	          [
1319	            "MID",
1320	            7,
1321	            0.062,
1322	            0.025,
1323	            0.035,
1324	            0.095,
1325	            "5/7"
1326	          ],
1327	          [
1328	            "LOW",
1329	            6,
1330	            0.108,
1331	            0.078,
1332	            0.042,
1333	            0.192,
1334	            "2/6"
1335	          ],
1336	          [
1337	            "ALL",
1338	            20,
1339	            0.065,
1340	            0.055,
1341	            0.012,
1342	            0.192,
1343	            "13/20"
1344	          ]
1345	        ]
1346	      }
1347	    ],
1348	    "figures": [],
1349	    "analysis": "Orthogonality 作为 subsection 贡献有限。LOW tier 的高 cosine 可能是 probe noise 而非真 non-orthogonality（control task artifact rate 42% in LOW tier）。 简化为 1 paragraph + 1 table 在 supporting evidence 小节。\n\n\nOrthogonality 在 HIGH resource 语言成立（cosine < 0.05），复现 Miao & Ungar (2026)。 但 LOW resource 的 cosine 显著升高且方差大（mean 0.108, std 0.078）——原因不是真正的 非正交结构，而是两个 probe 都更 noisy：correctness probe selectivity 低（plan_013 控制 任务发现），confidence probe 同样缺乏区分性信号，两个 noisy direction 的 cosine 自然 偏离 0。Architecture 一致性仅 65%：7/20 语言两架构给出矛盾信号——可能反映不同 MoE routing 对 confidence 编码方式的影响。\n作为已降级的 subsection，这些结果增加复杂性但无 clean takeaway。\n"
1350	  },
1351	  {
1352	    "name": "Probe Complexity Comparison",
1353	    "description": "Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer degradation + calibration, 3 models × 20 languages.\n",
1354	    "results": {
1355	      "en_auroc_lr_mean": 0.738,
1356	      "en_auroc_mlp_mean": 0.752,
1357	      "mlp_en_advantage_pp": 1.4,
1358	      "zs_transfer_degradation_lr_pp": 15.8,
1359	      "zs_transfer_degradation_mlp_pp": 19.4,
1360	      "mlp_transfer_disadvantage_pp": 3.6,
1361	      "lr_better_for_transfer_pct": 0.72,
1362	      "ece_lr_mean": 0.238,
1363	      "ece_mlp_mean": 0.252
1364	    },
1365	    "tables": [
1366	      {
1367	        "name": "Table S2: Probe Complexity Comparison",
1368	        "columns": [
1369	          "metric",
1370	          "logistic_regression",
1371	          "mlp_2layer",
1372	          "delta",
1373	          "p_value"
1374	        ],
1375	        "rows": [
1376	          [
1377	            "EN AUROC",
1378	            0.738,
1379	            0.752,
1380	            0.014,
1381	            0.006
1382	          ],
1383	          [
1384	            "ZS degradation",
1385	            "15.8%",
1386	            "19.4%",
1387	            "+3.6pp",
1388	            0.018
1389	          ],
1390	          [
1391	            "ZS AUROC",
1392	            0.621,
1393	            0.608,
1394	            -0.013,
1395	            0.032
1396	          ],
1397	          [
1398	            "EN ECE",
1399	            0.238,
1400	            0.252,
1401	            0.014,
1402	            0.058
1403	          ],
1404	          [
1405	            "LR better for transfer",
1406	            "72%",
1407	            "28%",
1408	            "—",
1409	            "—"
1410	          ]
1411	        ]
1412	      }
1413	    ],
1414	    "figures": [],
1415	    "analysis": "方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，probe complexity 不是主要问题。保持 LR 默认，appendix 报告 MLP 对比。\n\n\nMLP 更高 capacity → EN +1.4pp，但跨语言 transfer degradation 更大（-19.4% vs -15.8%）， 符合 \"linear probes transfer better\" 假设。在 worst tier 下 effect size 中等 （Cohen's d ≈ 0.35），72% 语言支持 LR。部分 HIGH resource 语言中 MLP 额外 capacity 弥补了 transfer loss。结论方向正确但不 dramatic——LR 作为默认 choice 被 confirm， MLP 结果放 appendix。\n"
1416	  },
1417	  {
1418	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
1419	    "description": "Best probes + all transfer conditions on Belebele (20 langs) and MMLU-ProX (20 langs). Cross-benchmark generalization test.\n",
1420	    "results": {
1421	      "belebele_zs_pass_rate": 0.45,
1422	      "belebele_mean_zs_auroc": 0.545,
1423	      "belebele_vs_globalmmlu_spearman": 0.71,
1424	      "belebele_mean_delta_vs_globalmmlu": -0.029,
1425	      "mmlupx_zs_pass_rate": 0.55,
1426	      "mmlupx_mean_zs_auroc": 0.565,
1427	      "mmlupx_vs_globalmmlu_spearman": 0.79,
1428	      "caclr_belebele_delta": -0.015,
1429	      "caclr_mmlupx_delta": -0.009,
1430	      "linear_proj_belebele_delta": 0.028,
1431	      "linear_proj_mmlupx_delta": 0.033
1432	    },
1433	    "tables": [
1434	      {
1435	        "name": "Table S3: Cross-Benchmark Generalization",
1436	        "columns": [
1437	          "benchmark",
1438	          "zs_pass_rate",
1439	          "mean_zs_auroc",
1440	          "caclr_Δ",
1441	          "linproj_Δ",
1442	          "corr_vs_globalmmlu"
1443	        ],
1444	        "rows": [
1445	          [
1446	            "GlobalMMLU",
1447	            "57%",
1448	            0.574,
1449	            -0.008,
1450	            0.036,
1451	            "—"
1452	          ],
1453	          [
1454	            "Belebele",
1455	            "45%",
1456	            0.545,
1457	            -0.015,
1458	            0.028,
1459	            0.71
1460	          ],
1461	          [
1462	            "MMLU-ProX",
1463	            "55%",
1464	            0.565,
1465	            -0.009,
1466	            0.033,
1467	            0.79
1468	          ]
1469	        ]
1470	      }
1471	    ],
1472	    "figures": [],
1473	    "analysis": "Cross-benchmark generalization moderate。Belebele 低 performance 暗示 correctness probing 对 task format 敏感——在 worst tier paper 中增加一层 caveat。 放 appendix 作为 generalization check。\n\n\nBelebele (reading comprehension) 与 MCQA correctness probing 的 task mismatch 导致更低 pass rate。Correctness probe 在 GlobalMMLU 上学到的 \"correct answer\" signal 部分依赖于 MCQA-specific format cues（如选项长度、academic domain structure），这些 在 Belebele 的 reading comprehension 中缺失。MMLU-ProX 与 GlobalMMLU 更接近（同为 知识 MCQA），correlation 更高。\nCaCLR 在 out-of-distribution data 上更差——distribution mismatch 被放大。 Linear projection 仍正但幅度缩小。\nWorst tier 意味着 generalization 弱化了已经微弱的 positive findings， 暗示 correctness probing 可能 MCQA-specific。\n"
1474	  },
1475	  {
1476	    "name": "Quantization Validation Ablation",
1477	    "description": "(a) W4A16 vs FP16 for Llama 4 Scout, 5 representative layers, 5% data subset; (b) INT4 vs FP16 for Qwen3-235B, 5 representative layers, 5% data subset.\n",
1478	    "results": {
1479	      "llama_w4a16_vs_fp16": {
1480	        "mean_delta_auroc": 0.008,
1481	        "max_delta_auroc": 0.016,
1482	        "rank_preservation": 0.92
1483	      },
1484	      "qwen_int4_vs_fp16": {
1485	        "mean_delta_auroc": 0.011,
1486	        "max_delta_auroc": 0.021,
1487	        "rank_preservation": 0.89
1488	      },
1489	      "problematic_layers": 2,
1490	      "gemma_note": "BF16, no quantization — serves as quantization-free control"
1491	    },
1492	    "tables": [
1493	      {
1494	        "name": "Table S4: Quantization Validation",
1495	        "columns": [
1496	          "model",
1497	          "quant",
1498	          "layer_pct",
1499	          "fp16_auroc",
1500	          "quant_auroc",
1501	          "delta",
1502	          "rank_ok"
1503	        ],
1504	        "rows": [
1505	          [
1506	            "Llama4",
1507	            "W4A16",
1508	            "20%",
1509	            0.65,
1510	            0.647,
1511	            -0.003,
1512	            "✓"
1513	          ],
1514	          [
1515	            "Llama4",
1516	            "W4A16",
1517	            "40%",
1518	            0.675,
1519	            0.668,
1520	            -0.007,
1521	            "✓"
1522	          ],
1523	          [
1524	            "Llama4",
1525	            "W4A16",
1526	            "60%",
1527	            0.698,
1528	            0.688,
1529	            -0.01,
1530	            "✓"
1531	          ],
1532	          [
1533	            "Llama4",
1534	            "W4A16",
1535	            "80%",
1536	            0.71,
1537	            0.696,
1538	            -0.014,
1539	            "✗ (2 swaps)"
1540	          ],
1541	          [
1542	            "Llama4",
1543	            "W4A16",
1544	            "95%",
1545	            0.715,
1546	            0.699,
1547	            -0.016,
1548	            "✗ (3 swaps)"
1549	          ],
1550	          [
1551	            "Qwen3",
1552	            "INT4",
1553	            "20%",
1554	            0.628,
1555	            0.623,
1556	            -0.005,
1557	            "✓"
1558	          ],
1559	          [
1560	            "Qwen3",
1561	            "INT4",
1562	            "40%",
1563	            0.672,
1564	            0.662,
1565	            -0.01,
1566	            "✓"
1567	          ],
1568	          [
1569	            "Qwen3",
1570	            "INT4",
1571	            "60%",
1572	            0.705,
1573	            0.692,
1574	            -0.013,
1575	            "✗ (1 swap)"
1576	          ],
1577	          [
1578	            "Qwen3",
1579	            "INT4",
1580	            "80%",
1581	            0.73,
1582	            0.714,
1583	            -0.016,
1584	            "✗ (3 swaps)"
1585	          ],
1586	          [
1587	            "Qwen3",
1588	            "INT4",
1589	            "95%",
1590	            0.741,
1591	            0.72,
1592	            -0.021,
1593	            "✗ (4 swaps)"
1594	          ]
1595	        ]
1596	      }
1597	    ],
1598	    "figures": [],
1599	    "analysis": "Quantization 在深层引入 1-2pp 偏差，不改变主要 negative result 结论 （negative results 不依赖精确数值），但增加 limitations 内容。 Gemma BF16 作为 quantization-free control 点使得 Gemma 的结果最可信。\n\n\nQuantization artifacts 不灾难性但 non-negligible。深层（80-95% depth）受影响最大， 因为 correctness signal 在这些层最集中，而高频/低方差的 correctness direction 对 quantization noise 更敏感。INT4 (Qwen) 比 W4A16 (Llama) 更aggressive，所以 delta 更大。Rank preservation 88-92% 意味着 per-language ranking 大体保持但不完美。\nWorst tier 下这创造一个 caveat：深层 probe 结论 potentially 受量化影响。 Gemma 4 BF16 无量化，提供了 quantization-free 的 architecture 数据点。\n"
1600	  },
1601	  {
1602	    "name": "CKA Cross-Lingual Representation Similarity Analysis",
1603	    "description": "CKA (linear kernel) EN vs target, all probed layers, 20 langs × 3 models. Simpson's Paradox full-scale validation. Partial correlation controlling for depth. Same-layer cross-language analysis. Subspace angle analysis.\n",
1604	    "results": {
1605	      "simpson_paradox_confirmed_of_3_arch": 0,
1606	      "partial_correlations": {
1607	        "qwen3": {
1608	          "rho": 0.11,
1609	          "p": 0.28,
1610	          "bootstrap_ci": [
1611	            -0.08,
1612	            0.29
1613	          ]
1614	        },
1615	        "llama4": {
1616	          "rho": 0.06,
1617	          "p": 0.45,
1618	          "bootstrap_ci": [
1619	            -0.12,
1620	            0.24
1621	          ]
1622	        },
1623	        "gemma4": {
1624	          "rho": 0.16,
1625	          "p": 0.09,
1626	          "bootstrap_ci": [
1627	            -0.02,
1628	            0.33
1629	          ]
1630	        }
1631	      },
1632	      "raw_correlations": {
1633	        "qwen3": {
1634	          "rho": -0.32,
1635	          "p": "<0.001"
1636	        },
1637	        "llama4": {
1638	          "rho": -0.38,
1639	          "p": "<0.001"
1640	        },
1641	        "gemma4": {
1642	          "rho": -0.29,
1643	          "p": "<0.001"
1644	        }
1645	      },
1646	      "same_layer_cross_lang_analysis": {
1647	        "qwen3_significant_layers": "2/24",
1648	        "llama4_significant_layers": "0/12",
1649	        "gemma4_significant_layers": "1/16",
1650	        "median_rho": 0.14
1651	      },
1652	      "subspace_angle": {
1653	        "high_tier_range_deg": [
1654	          15,
1655	          38
1656	        ],
1657	        "mid_tier_range_deg": [
1658	          28,
1659	          52
1660	        ],
1661	        "low_tier_range_deg": [
1662	          42,
1663	          65
1664	        ],
1665	        "consistency_across_layers": "low — within-language angle std 8-15° across layers"
1666	      },
1667	      "pilot_replication": {
1668	        "llama_pilot_rho": 0.41,
1669	        "llama_fullscale_rho": 0.06,
1670	        "verdict": "pilot artifact confirmed"
1671	      }
1672	    },
1673	    "tables": [
1674	      {
1675	        "name": "Table 7a: Simpson's Paradox Full-Scale Validation",
1676	        "columns": [
1677	          "model",
1678	          "raw_rho",
1679	          "raw_p",
1680	          "partial_rho",
1681	          "partial_p",
1682	          "pilot_rho",
1683	          "pilot_p",
1684	          "verdict"
1685	        ],
1686	        "rows": [
1687	          [
1688	            "Qwen3-235B",
1689	            -0.32,
1690	            "<0.001",
1691	            0.11,
1692	            0.28,
1693	            "+0.18 (n.s.)",
1694	            0.274,
1695	            "n.s. confirmed"
1696	          ],
1697	          [
1698	            "Llama4-Scout",
1699	            -0.38,
1700	            "<0.001",
1701	            0.06,
1702	            0.45,
1703	            "+0.41 (sig.)",
1704	            0.006,
1705	            "pilot artifact"
1706	          ],
1707	          [
1708	            "Gemma4-31B",
1709	            -0.29,
1710	            "<0.001",
1711	            0.16,
1712	            0.09,
1713	            "N/A",
1714	            "N/A",
1715	            "marginal, CI spans 0"
1716	          ]
1717	        ]
1718	      },
1719	      {
1720	        "name": "Table 7b: Same-Layer Cross-Language CKA-Transfer Correlation",
1721	        "columns": [
1722	          "model",
1723	          "total_layers",
1724	          "significant_layers",
1725	          "median_rho",
1726	          "best_layer_rho",
1727	          "best_p"
1728	        ],
1729	        "rows": [
1730	          [
1731	            "Qwen3",
1732	            24,
1733	            "2/24",
1734	            0.15,
1735	            0.4,
1736	            0.078
1737	          ],
1738	          [
1739	            "Llama4",
1740	            12,
1741	            "0/12",
1742	            0.08,
1743	            0.28,
1744	            0.23
1745	          ],
1746	          [
1747	            "Gemma4",
1748	            16,
1749	            "1/16",
1750	            0.18,
1751	            0.44,
1752	            0.052
1753	          ]
1754	        ]
1755	      },
1756	      {
1757	        "name": "Table 7c: Subspace Angle (Correctness Direction, EN vs Target, at ~60% depth)",
1758	        "columns": [
1759	          "lang",
1760	          "tier",
1761	          "qwen3_angle",
1762	          "llama4_angle",
1763	          "gemma4_angle"
1764	        ],
1765	        "rows": [
1766	          [
1767	            "zh",
1768	            "HIGH",
1769	            "18°",
1770	            "24°",
1771	            "16°"
1772	          ],
1773	          [
1774	            "es",
1775	            "HIGH",
1776	            "15°",
1777	            "20°",
1778	            "14°"
1779	          ],
1780	          [
1781	            "ja",
1782	            "HIGH",
1783	            "35°",
1784	            "42°",
1785	            "32°"
1786	          ],
1787	          [
1788	            "ar",
1789	            "MID",
1790	            "32°",
1791	            "40°",
1792	            "30°"
1793	          ],
1794	          [
1795	            "hi",
1796	            "MID",
1797	            "38°",
1798	            "46°",
1799	            "35°"
1800	          ],
1801	          [
1802	            "ko",
1803	            "MID",
1804	            "28°",
1805	            "36°",
1806	            "26°"
1807	          ],
1808	          [
1809	            "tr",
1810	            "MID",
1811	            "45°",
1812	            "52°",
1813	            "42°"
1814	          ],
1815	          [
1816	            "sw",
1817	            "LOW",
1818	            "52°",
1819	            "58°",
1820	            "48°"
1821	          ],
1822	          [
1823	            "bn",
1824	            "LOW",
1825	            "48°",
1826	            "55°",
1827	            "45°"
1828	          ],
1829	          [
1830	            "am",
1831	            "LOW",
1832	            "62°",
1833	            "65°",
1834	            "58°"
1835	          ]
1836	        ]
1837	      }
1838	    ],
1839	    "figures": [],
1840	    "analysis": "CKA 的全面失败从 pilot 的 Simpson's Paradox 标杆发现降级为 \"depth confound 在 raw correlation 中占主导，controlling 后无 signal\"。Subspace angle 否定了论文的 前提假设：\"correctness direction 是 robust language-agnostic subspace\" 不成立。 CKA 框架从解释性分析降级为描述性可视化——保留 heatmap 但不承载因果叙述。 3 架构 0/3 Simpson's Paradox confirmed，在 worst 范围 [0, 1] 内。\n\n\n这是 worst tier 的 defining falsification。\n5 语言 pilot 的 Simpson's Paradox 被 20 语言全量数据否定：\n(1) Llama partial rho 从 +0.41 (p=0.006) 骤降至 +0.06 (p=0.45)。原因：pilot 的 5 语言 恰好 overrepresented CKA-transfer 相关性最强的语言（zh, ar 有高 CKA + 低 degradation）， 排除了关系最弱的语言。15 种新增语言中 MID/LOW tier 的 CKA 模式与 pilot 语言截然不同—— 这些语言的 CKA 虽然也随 depth 下降，但下降斜率和 transfer degradation 之间没有一致的 within-layer 关系。\n(2) Qwen3 rho=+0.11 (p=0.28) 在 pilot 就不显著（+0.18, p=0.274），全量数据只是确认。 Gemma4 rho=+0.16 (p=0.09) 是最接近显著的，但 bootstrap CI 跨零（[-0.02, 0.33]）， 不能依赖。\n(3) Same-layer cross-language analysis（n=20 per layer，最强检验）：median rho=0.14， 仅 3/52 层 significant——CKA 在 within-layer 水平几乎无预测力。在同一层中，不同语言 的 CKA 差异巨大但 transfer AUROC 差异不 track CKA。\n(4) Subspace angle analysis 否定 \"correctness direction is a robust language-agnostic subspace\"：HIGH tier 15-38°（不是近乎平行），LOW tier 42-65°（近乎 orthogonal）。 Angle 在同一语言的不同层之间也有 8-15° 的标准差——correctness direction 不仅跨语言 不一致，在同一语言内也随 depth 漂移。\n结论：CKA 不提供超越 depth 的解释力。从 \"geometric analysis\" 降级为 \"suggestive correlation\"——仅保留 CKA heatmap 作为 descriptive visualization。\n"
1841	  },
1842	  {
1843	    "name": "Linear Projection Sensitivity Analysis",
1844	    "description": "Procrustes alignment with 10/20/50/100/200 parallel pairs. 3 models × 5 representative layers × 20 languages.\n",
1845	    "results": {
1846	      "linear_proj_delta_over_zs_low_resource_pp": 2.8,
1847	      "linear_proj_saturation_pairs_mean": 135,
1848	      "saturation_by_tier": {
1849	        "HIGH": {
1850	          "pairs_95pct": 62,
1851	          "range": [
1852	            38,
1853	            92
1854	          ]
1855	        },
1856	        "MID": {
1857	          "pairs_95pct": 118,
1858	          "range": [
1859	            72,
1860	            158
1861	          ]
1862	        },
1863	        "LOW": {
1864	          "pairs_95pct": 175,
1865	          "range": [
1866	            140,
1867	            198
1868	          ]
1869	        }
1870	      },
1871	      "sample_efficiency_curve": {
1872	        "10_pairs": {
1873	          "mean_auroc": 0.552,
1874	          "pct_of_200": "66%"
1875	        },
1876	        "20_pairs": {
1877	          "mean_auroc": 0.571,
1878	          "pct_of_200": "78%"
1879	        },
1880	        "50_pairs": {
1881	          "mean_auroc": 0.592,
1882	          "pct_of_200": "89%"
1883	        },
1884	        "100_pairs": {
1885	          "mean_auroc": 0.605,
1886	          "pct_of_200": "96%"
1887	        },
1888	        "200_pairs": {
1889	          "mean_auroc": 0.61,
1890	          "pct_of_200": "100%"
1891	        }
1892	      },
1893	      "procrustes_reversal": {
1894	        "helps_below_zs": "< 0.53 (mostly helps)",
1895	        "hurts_above_zs": "> 0.62 (mostly hurts)",
1896	        "inconsistent_zone": [
1897	          0.53,
1898	          0.62
1899	        ],
1900	        "note": "threshold varies ±0.08 across languages — no single reliable cutoff"
1901	      }
1902	    },
1903	    "tables": [
1904	      {
1905	        "name": "Table 8a: Linear Projection Sample Efficiency (3 arch × 20 langs)",
1906	        "columns": [
1907	          "n_pairs",
1908	          "mean_auroc",
1909	          "pct_of_200",
1910	          "std",
1911	          "significant_pct"
1912	        ],
1913	        "rows": [
1914	          [
1915	            10,
1916	            0.552,
1917	            "66%",
1918	            0.062,
1919	            "22%"
1920	          ],
1921	          [
1922	            20,
1923	            0.571,
1924	            "78%",
1925	            0.055,
1926	            "38%"
1927	          ],
1928	          [
1929	            50,
1930	            0.592,
1931	            "89%",
1932	            0.049,
1933	            "52%"
1934	          ],
1935	          [
1936	            100,
1937	            0.605,
1938	            "96%",
1939	            0.044,
1940	            "65%"
1941	          ],
1942	          [
1943	            200,
1944	            0.61,
1945	            "100%",
1946	            0.042,
1947	            "70%"
1948	          ]
1949	        ]
1950	      },
1951	      {
1952	        "name": "Table 8b: Pairs to 95% by Resource Tier",
1953	        "columns": [
1954	          "tier",
1955	          "mean",
1956	          "min",
1957	          "max",
1958	          "std"
1959	        ],
1960	        "rows": [
1961	          [
1962	            "HIGH",
1963	            62,
1964	            38,
1965	            92,
1966	            20
1967	          ],
1968	          [
1969	            "MID",
1970	            118,
1971	            72,
1972	            158,
1973	            32
1974	          ],
1975	          [
1976	            "LOW",
1977	            175,
1978	            140,
1979	            198,
1980	            25
1981	          ]
1982	        ]
1983	      },
1984	      {
1985	        "name": "Table 8c: Procrustes Effect Direction (200 pairs, selected languages)",
1986	        "columns": [
1987	          "lang",
1988	          "tier",
1989	          "zs_auroc",
1990	          "linproj_auroc",
1991	          "delta",
1992	          "effect"
1993	        ],
1994	        "rows": [
1995	          [
1996	            "am",
1997	            "LOW",
1998	            0.483,
1999	            0.508,
2000	            0.025,
2001	            "helps"
2002	          ],
2003	          [
2004	            "yo",
2005	            "LOW",
2006	            0.468,
2007	            0.494,
2008	            0.026,
2009	            "helps"
2010	          ],
2011	          [
2012	            "sw",
2013	            "LOW",
2014	            0.511,
2015	            0.528,
2016	            0.017,
2017	            "helps"
2018	          ],
2019	          [
2020	            "tr",
2021	            "MID",
2022	            0.544,
2023	            0.56,
2024	            0.016,
2025	            "helps"
2026	          ],
2027	          [
2028	            "hi",
2029	            "MID",
2030	            0.56,
2031	            0.568,
2032	            0.008,
2033	            "marginal"
2034	          ],
2035	          [
2036	            "vi",
2037	            "MID",
2038	            0.563,
2039	            0.562,
2040	            -0.001,
2041	            "neutral"
2042	          ],
2043	          [
2044	            "ko",
2045	            "MID",
2046	            0.589,
2047	            0.582,
2048	            -0.007,
2049	            "hurts"
2050	          ],
2051	          [
2052	            "ar",
2053	            "MID",
2054	            0.606,
2055	            0.598,
2056	            -0.008,
2057	            "hurts"
2058	          ],
2059	          [
2060	            "ru",
2061	            "MID",
2062	            0.622,
2063	            0.61,
2064	            -0.012,
2065	            "hurts"
2066	          ],
2067	          [
2068	            "es",
2069	            "HIGH",
2070	            0.674,
2071	            0.654,
2072	            -0.02,
2073	            "hurts"
2074	          ],
2075	          [
2076	            "ja",
2077	            "HIGH",
2078	            0.588,
2079	            0.596,
2080	            0.008,
2081	            "helps (despite HIGH)"
2082	          ]
2083	        ]
2084	      }
2085	    ],
2086	    "figures": [],
2087	    "analysis": "Linear projection 是唯一可行 label-free 方案但实用性弱化：需 100+ pairs（非 50）， effect reversal threshold inconsistent。Paper 给出条件性 recommendation： \"ZS < 0.50 大概率有益, > 0.65 大概率有害, 中间需 validation\"—— 比预期的 clean threshold 弱得多，但对 practitioners 仍有指导价值。\n\n\nWorst tier 下 linear projection 需 100-135 pairs 达到 95% performance（非 50）：\n(1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需更多数据 稳定 rotation matrix 估计——50 pairs 在高维空间 rank-deficient。\n(2) LOW resource 语言的 parallel pairs 翻译质量低 → activation noise → 需更多 pairs average out noise。HIGH tier 62 pairs（翻译精确，subspace angle 小）vs LOW tier 175 pairs（翻译 noisy，subspace angle 大）。\n(3) Effect reversal threshold language-specific：inconsistent zone [0.53, 0.62] 意味着同一 ZS AUROC 值下不同语言可能被帮助或伤害。例如 ja (HIGH, ZS=0.588) 被 帮助但 ko (MID, ZS=0.589) 被伤害——差异来自 subspace angle 和翻译质量的交互作用。 无法给出单一可操作阈值——practitioner recommendation 弱化为 \"ZS < 0.50 大概率有益， > 0.65 大概率有害，中间区间需 held-out validation\"。\n低资源语言 delta +2.8pp（worst 范围 [1, 4] 内），仍是唯一可行的 label-free 方案。\n"
2088	  },
2089	  {
2090	    "name": "Probing Control Tasks — Cross-Lingual Extension",
2091	    "description": "Hewitt & Liang control tasks extended to 20 languages × all probed layers × 3 models. Selectivity analysis. Multiple selectivity thresholds (0.03, 0.05, 0.10). (builds on completed plan_013 EN-only results)\n",
2092	    "results": {
2093	      "cross_lingual_artifact_rate_pct": 35,
2094	      "artifact_by_tier": {
2095	        "HIGH": {
2096	          "rate": "15%",
2097	          "selectivity_mean": 0.195
2098	        },
2099	        "MID": {
2100	          "rate": "31%",
2101	          "selectivity_mean": 0.138
2102	        },
2103	        "LOW": {
2104	          "rate": "42%",
2105	          "selectivity_mean": 0.082
2106	        }
2107	      },
2108	      "control_task_selectivity_deep_layers": 0.16,
2109	      "selectivity_vs_zs_auroc_rho": 0.65,
2110	      "threshold_sensitivity": {
2111	        "threshold_003": {
2112	          "artifact_rate": "42%"
2113	        },
2114	        "threshold_005": {
2115	          "artifact_rate": "35%"
2116	        },
2117	        "threshold_010": {
2118	          "artifact_rate": "24%"
2119	        }
2120	      },
2121	      "worst_combos": [
2122	        "am: selectivity 0.004 at EN-opt layer",
2123	        "yo: selectivity 0.005 at EN-opt layer",
2124	        "my: selectivity 0.006 at EN-opt layer",
2125	        "sw: selectivity 0.008 at EN-opt layer"
2126	      ],
2127	      "mid_resource_surprise": {
2128	        "tr": {
2129	          "selectivity_at_enopt": 0.031
2130	        },
2131	        "th": {
2132	          "selectivity_at_enopt": 0.028
2133	        },
2134	        "vi": {
2135	          "selectivity_at_enopt": 0.042
2136	        }
2137	      }
2138	    },
2139	    "tables": [
2140	      {
2141	        "name": "Table 9a: Cross-Lingual Artifact Rate by Resource Tier (3 models)",
2142	        "columns": [
2143	          "tier",
2144	          "n_langs",
2145	          "artifact_rate_thresh_005",
2146	          "selectivity_mean",
2147	          "selectivity_std"
2148	        ],
2149	        "rows": [
2150	          [
2151	            "HIGH",
2152	            7,
2153	            "15%",
2154	            0.195,
2155	            0.042
2156	          ],
2157	          [
2158	            "MID",
2159	            7,
2160	            "31%",
2161	            0.138,
2162	            0.038
2163	          ],
2164	          [
2165	            "LOW",
2166	            6,
2167	            "42%",
2168	            0.082,
2169	            0.035
2170	          ],
2171	          [
2172	            "ALL",
2173	            20,
2174	            "35%",
2175	            0.142,
2176	            0.058
2177	          ]
2178	        ]
2179	      },
2180	      {
2181	        "name": "Table 9b: Per-Language Selectivity at EN-Optimal Layer (Qwen3)",
2182	        "columns": [
2183	          "lang",
2184	          "tier",
2185	          "real_auroc",
2186	          "permuted_auroc",
2187	          "selectivity",
2188	          "flag"
2189	        ],
2190	        "rows": [
2191	          [
2192	            "en",
2193	            "—",
2194	            0.741,
2195	            0.488,
2196	            0.253,
2197	            ""
2198	          ],
2199	          [
2200	            "zh",
2201	            "HIGH",
2202	            0.668,
2203	            0.495,
2204	            0.173,
2205	            ""
2206	          ],
2207	          [
2208	            "es",
2209	            "HIGH",
2210	            0.675,
2211	            0.492,
2212	            0.183,
2213	            ""
2214	          ],
2215	          [
2216	            "fr",
2217	            "HIGH",
2218	            0.658,
2219	            0.49,
2220	            0.168,
2221	            ""
2222	          ],
2223	          [
2224	            "de",
2225	            "HIGH",
2226	            0.649,
2227	            0.486,
2228	            0.163,
2229	            ""
2230	          ],
2231	          [
2232	            "ja",
2233	            "HIGH",
2234	            0.588,
2235	            0.501,
2236	            0.087,
2237	            ""
2238	          ],
2239	          [
2240	            "pt",
2241	            "HIGH",
2242	            0.662,
2243	            0.489,
2244	            0.173,
2245	            ""
2246	          ],
2247	          [
2248	            "it",
2249	            "HIGH",
2250	            0.645,
2251	            0.492,
2252	            0.153,
2253	            ""
2254	          ],
2255	          [
2256	            "ar",
2257	            "MID",
2258	            0.608,
2259	            0.496,
2260	            0.112,
2261	            ""
2262	          ],
2263	          [
2264	            "hi",
2265	            "MID",
2266	            0.567,
2267	            0.503,
2268	            0.064,
2269	            "⚠"
2270	          ],
2271	          [
2272	            "ru",
2273	            "MID",
2274	            0.621,
2275	            0.493,
2276	            0.128,
2277	            ""
2278	          ],
2279	          [
2280	            "ko",
2281	            "MID",
2282	            0.591,
2283	            0.499,
2284	            0.092,
2285	            ""
2286	          ],
2287	          [
2288	            "tr",
2289	            "MID",
2290	            0.548,
2291	            0.517,
2292	            0.031,
2293	            "⚠"
2294	          ],
2295	          [
2296	            "vi",
2297	            "MID",
2298	            0.562,
2299	            0.52,
2300	            0.042,
2301	            "⚠"
2302	          ],
2303	          [
2304	            "th",
2305	            "MID",
2306	            0.528,
2307	            0.5,
2308	            0.028,
2309	            "⚠"
2310	          ],
2311	          [
2312	            "sw",
2313	            "LOW",
2314	            0.518,
2315	            0.51,
2316	            0.008,
2317	            "⚠⚠"
2318	          ],
2319	          [
2320	            "bn",
2321	            "LOW",
2322	            0.524,
2323	            0.505,
2324	            0.019,
2325	            "⚠⚠"
2326	          ],
2327	          [
2328	            "am",
2329	            "LOW",
2330	            0.486,
2331	            0.482,
2332	            0.004,
2333	            "⚠⚠"
2334	          ],
2335	          [
2336	            "yo",
2337	            "LOW",
2338	            0.475,
2339	            0.47,
2340	            0.005,
2341	            "⚠⚠"
2342	          ],
2343	          [
2344	            "te",
2345	            "LOW",
2346	            0.502,
2347	            0.492,
2348	            0.01,
2349	            "⚠⚠"
2350	          ],
2351	          [
2352	            "my",
2353	            "LOW",
2354	            0.468,
2355	            0.462,
2356	            0.006,
2357	            "⚠⚠"
2358	          ]
2359	        ]
2360	      },
2361	      {
2362	        "name": "Table 9c: Selectivity Threshold Sensitivity",
2363	        "columns": [
2364	          "threshold",
2365	          "overall_artifact_rate",
2366	          "LOW_rate",
2367	          "MID_rate",
2368	          "HIGH_rate"
2369	        ],
2370	        "rows": [
2371	          [
2372	            0.03,
2373	            "42%",
2374	            "52%",
2375	            "40%",
2376	            "22%"
2377	          ],
2378	          [
2379	            0.05,
2380	            "35%",
2381	            "42%",
2382	            "31%",
2383	            "15%"
2384	          ],
2385	          [
2386	            0.1,
2387	            "24%",
2388	            "35%",
2389	            "22%",
2390	            "8%"
2391	          ]
2392	        ]
2393	      }
2394	    ],
2395	    "figures": [],
2396	    "analysis": "Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate 波及中资源语言是 field-level 发现：所有跨语言 probing 研究——包括只看中/高资源的—— 都需要 selectivity 检验。Selectivity-AUROC correlation (ρ=0.65) 暗示文献中许多 positive results 可能是 artifacts。首次系统性应用 Hewitt & Liang 到 cross-lingual 场景——这个贡献独立于本文其他所有 claims，即使其他全部失败仍足以支撑 EACL findings paper。\n\n\nCross-lingual artifact rate 35% (overall) 是 worst tier 最强贡献。\nLOW tier 42% artifact rate 的原因：am, yo, my, te 等语言在 LLM pretraining 中 极度不足（估计 < 0.1% token share），这些语言的 representation 缺乏区分性结构—— probe 学到的主要是 capacity artifacts（随机 label 也能达到类似 AUROC）。 Selectivity = real_AUROC - permuted_AUROC 对这些语言仅 0.004-0.008， 几乎等于 zero information content。\nMID tier 31% artifact rate 是 worst tier 的 signature finding：不仅低资源有问题—— tr (0.031), th (0.028), vi (0.042) 等中资源语言在 shallow/mid layers 也有大量 artifacts。原因：这些语言虽然 pretraining 充足，但 correctness-specific signal （区分 \"模型答对/答错\"）在 representation 中的编码弱于语言 identity signal， probe 部分地拟合了 language-specific capacity pattern 而非 correctness。\nHIGH tier 15% artifact rate 主要出现在 shallow layers（0-30% depth）， 与 plan_013 completed results 一致（L0-L16 selectivity < 0.12）。\nSelectivity 与 ZS AUROC 的 rho=0.65 是最尖锐的发现：暗示 cross-lingual probing 文献中许多 \"positive transfer\" 结果可能是 artifacts——高 ZS AUROC 可能部分反映 capacity artifacts 而非 genuine correctness signal transfer。\n首次在 cross-lingual transfer 场景系统性应用 Hewitt & Liang selectivity—— 发现 artifact 问题远比 monolingual probing 严重。Field-level implication。\n"
2397	  },
2398	  {
2399	    "name": "Extended Language Coverage (50+ Languages)",
2400	    "description": "从 20 扩展到 50+ 语言 (camera-ready extension)。Leverages GlobalMMLU/Belebele full language sets。P2 priority。\n",
2401	    "results": {
2402	      "total_languages": 52,
2403	      "zs_pass_rate_52lang": 0.5,
2404	      "artifact_rate_low_expanded": 0.45,
2405	      "artifact_rate_mid_expanded": 0.34,
2406	      "new_significant_pareto_langs": 2,
2407	      "linear_proj_saturation_mean_expanded": 155
2408	    },
2409	    "tables": [
2410	      {
2411	        "name": "Table S5: 52-Language vs 20-Language Summary",
2412	        "columns": [
2413	          "metric",
2414	          "20_lang",
2415	          "52_lang",
2416	          "delta"
2417	        ],
2418	        "rows": [
2419	          [
2420	            "zs_pass_rate",
2421	            "57%",
2422	            "50%",
2423	            "-7pp"
2424	          ],
2425	          [
2426	            "artifact_rate_LOW",
2427	            "42%",
2428	            "45%",
2429	            "+3pp"
2430	          ],
2431	          [
2432	            "artifact_rate_MID",
2433	            "31%",
2434	            "34%",
2435	            "+3pp"
2436	          ],
2437	          [
2438	            "linear_proj_mean_pairs",
2439	            135,
2440	            155,
2441	            "+20"
2442	          ],
2443	          [
2444	            "max_partial_rho",
2445	            0.16,
2446	            0.14,
2447	            "-0.02"
2448	          ]
2449	        ]
2450	      }
2451	    ],
2452	    "figures": [],
2453	    "analysis": "52 语言扩展服务于 coverage 和 robustness。核心结论不变但 control task finding 更 impactful，linear projection guidance 更 granular（更多语言的 tier classification）。\n\n\n扩展到 52 语言后新增大部分是 MID/LOW resource，ZS pass rate 从 57% → 50% 因为新语言 skew lower resource。Control artifact rate 在扩展 LOW tier 升至 45% 因为更多极低资源语言纳入。新增语言不改变核心 negative results，主要增加 statistical power 和 coverage credibility。Linear projection saturation mean 升至 155 因为 更多 hard languages。\n扩展语言数的主要价值：(1) control task finding 的 scope 更大——\"近半数低资源跨语言 probing 结果是 artifacts\" 在 50+ 语言规模下更有说服力；(2) EACL reviewer 可能要求 更多语言的 coverage；(3) 无量化 Gemma 在 52 语言上的数据最可信。\n"
2454	  }
2455	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90497761-6843-4f88-996b-fc10a096a15d",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "1e683ec6-22f2-455a-a6af-52b51f849fcb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B Full Pareto Frontier\",\n    \"description\": \"Qwen3-235B-A22B (94 layers, MoE, INT4), 24 probed layers (every 4th), 20 typologically diverse languages, EN correctness probes (LR + MLP), 5 transfer conditions (zero-shot, mean-shift, linear projection 200 pairs, few-shot 25/100, CaCLR).\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.741,\n      \"en_best_layer\": 72,\n      \"en_auroc_range\": [\n        0.601,\n        0.741\n      ],\n      \"en_best_ece_raw\": 0.198,\n      \"zs_pass_count_auroc_gt_058\": 11,\n      \"zs_pass_rate\": 0.55,\n      \"zs_fail_count\": 9,\n      \"mean_zs_auroc_all_20\": 0.576,\n      \"mean_zs_auroc_drop_vs_en_pp\": 16.5,\n      \"best_zs_auroc\": {\n        \"zh\": 0.668,\n        \"es\": 0.675,\n        \"fr\": 0.658,\n        \"de\": 0.649,\n        \"ja\": 0.588,\n        \"pt\": 0.662,\n        \"it\": 0.645,\n        \"ar\": 0.608,\n        \"hi\": 0.567,\n        \"ru\": 0.621,\n        \"ko\": 0.591,\n        \"tr\": 0.548,\n        \"vi\": 0.562,\n        \"th\": 0.528,\n        \"sw\": 0.518,\n        \"bn\": 0.524,\n        \"am\": 0.486,\n        \"yo\": 0.475,\n        \"te\": 0.502,\n        \"my\": 0.468\n      },\n      \"best_zs_layer\": {\n        \"zh\": 60,\n        \"es\": 56,\n        \"fr\": 60,\n        \"de\": 52,\n        \"ja\": 48,\n        \"pt\": 56,\n        \"it\": 56,\n        \"ar\": 52,\n        \"hi\": 44,\n        \"ru\": 56,\n        \"ko\": 48,\n        \"tr\": 40,\n        \"vi\": 44,\n        \"th\": 36,\n        \"sw\": 36,\n        \"bn\": 40,\n        \"am\": 32,\n        \"yo\": 28,\n        \"te\": 36,\n        \"my\": 32\n      },\n      \"global_spearman_rho_depth_vs_transfer\": -0.12,\n      \"global_spearman_p\": 0.078,\n      \"per_lang_spearman\": {\n        \"zh\": {\n          \"rho\": -0.31,\n          \"p\": 0.14\n        },\n        \"es\": {\n          \"rho\": -0.25,\n          \"p\": 0.24\n        },\n        \"fr\": {\n          \"rho\": -0.28,\n          \"p\": 0.18\n        },\n        \"de\": {\n          \"rho\": -0.19,\n          \"p\": 0.38\n        },\n        \"ja\": {\n          \"rho\": 0.18,\n          \"p\": 0.4\n        },\n        \"pt\": {\n          \"rho\": -0.22,\n          \"p\": 0.3\n        },\n        \"it\": {\n          \"rho\": -0.16,\n          \"p\": 0.46\n        },\n        \"ar\": {\n          \"rho\": 0.05,\n          \"p\": 0.82\n        },\n        \"hi\": {\n          \"rho\": -0.41,\n          \"p\": 0.046\n        },\n        \"ru\": {\n          \"rho\": -0.14,\n          \"p\": 0.52\n        },\n        \"ko\": {\n          \"rho\": 0.25,\n          \"p\": 0.24\n        },\n        \"tr\": {\n          \"rho\": -0.08,\n          \"p\": 0.71\n        },\n        \"vi\": {\n          \"rho\": 0.09,\n          \"p\": 0.68\n        },\n        \"th\": {\n          \"rho\": -0.11,\n          \"p\": 0.61\n        },\n        \"sw\": {\n          \"rho\": -0.35,\n          \"p\": 0.09\n        },\n        \"bn\": {\n          \"rho\": -0.12,\n          \"p\": 0.58\n        },\n        \"am\": {\n          \"rho\": 0.14,\n          \"p\": 0.52\n        },\n        \"yo\": {\n          \"rho\": -0.02,\n          \"p\": 0.93\n        },\n        \"te\": {\n          \"rho\": -0.18,\n          \"p\": 0.4\n        },\n        \"my\": {\n          \"rho\": 0.1,\n          \"p\": 0.64\n        }\n      },\n      \"per_lang_significant_negative_rho_count\": 1,\n      \"per_lang_significant_positive_rho_count\": 0,\n      \"per_lang_nonmonotonic_count\": 13,\n      \"pareto_tradeoff_prevalence\": 0.08,\n      \"pareto_depth_transfer_drop_final_layers_pp\": 0.6,\n      \"mean_shift_delta_auroc_all\": 0.0,\n      \"transfer_conditions_summary\": {\n        \"zero_shot\": {\n          \"mean_auroc\": 0.576,\n          \"std\": 0.068,\n          \"delta_vs_zs\": 0.0\n        },\n        \"mean_shift\": {\n          \"mean_auroc\": 0.576,\n          \"std\": 0.068,\n          \"delta_vs_zs\": 0.0\n        },\n        \"linear_proj_200\": {\n          \"mean_auroc\": 0.612,\n          \"std\": 0.055,\n          \"delta_vs_zs\": 0.036\n        },\n        \"fewshot_25\": {\n          \"mean_auroc\": 0.598,\n          \"std\": 0.061,\n          \"delta_vs_zs\": 0.022\n        },\n        \"fewshot_100\": {\n          \"mean_auroc\": 0.625,\n          \"std\": 0.049,\n          \"delta_vs_zs\": 0.049\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1a: Qwen3-235B Per-Language Pareto (Depth vs ZS-AUROC Spearman ρ)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"best_zs_auroc\",\n          \"best_zs_layer\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"pattern\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.668,\n            60,\n            -0.31,\n            0.14,\n            \"weak negative\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.675,\n            56,\n            -0.25,\n            0.24,\n            \"n.s.\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.658,\n            60,\n            -0.28,\n            0.18,\n            \"n.s.\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.649,\n            52,\n            -0.19,\n            0.38,\n            \"n.s.\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.588,\n            48,\n            0.18,\n            0.4,\n            \"non-monotonic U-shape\"\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.662,\n            56,\n            -0.22,\n            0.3,\n            \"n.s.\"\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.645,\n            56,\n            -0.16,\n            0.46,\n            \"n.s.\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.608,\n            52,\n            0.05,\n            0.82,\n            \"flat\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.567,\n            44,\n            -0.41,\n            0.046,\n            \"significant negative\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.621,\n            56,\n            -0.14,\n            0.52,\n            \"n.s.\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.591,\n            48,\n            0.25,\n            0.24,\n            \"inverted—deeper helps\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.548,\n            40,\n            -0.08,\n            0.71,\n            \"n.s.\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.562,\n            44,\n            0.09,\n            0.68,\n            \"flat\"\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.528,\n            36,\n            -0.11,\n            0.61,\n            \"n.s.\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.518,\n            36,\n            -0.35,\n            0.09,\n            \"marginal negative\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.524,\n            40,\n            -0.12,\n            0.58,\n            \"n.s.\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.486,\n            32,\n            0.14,\n            0.52,\n            \"non-monotonic\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.475,\n            28,\n            -0.02,\n            0.93,\n            \"noisy flat\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.502,\n            36,\n            -0.18,\n            0.4,\n            \"n.s.\"\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.468,\n            32,\n            0.1,\n            0.64,\n            \"non-monotonic\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 1b: Qwen3-235B Transfer Conditions Summary (20 langs, EN-optimal layer)\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc\",\n          \"std\",\n          \"delta_vs_zs\",\n          \"significant_improvement_count\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.576,\n            0.068,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.576,\n            0.068,\n            0.0,\n            \"0/20\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.612,\n            0.055,\n            0.036,\n            \"11/20\"\n          ],\n          [\n            \"fewshot_25\",\n            0.598,\n            0.061,\n            0.022,\n            \"7/20\"\n          ],\n          [\n            \"fewshot_100\",\n            0.625,\n            0.049,\n            0.049,\n            \"13/20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-235B 的 Pareto frontier 远不如 Qwen2.5-7B pilot 清晰。MoE expert routing 打破了 dense model 中 depth = specialization 的单调映射。Pilot 的 clear Pareto（L27 EN best 但 transfer drops 2-4pp vs L24）是 dense 7B model 的特殊现象。仅 1/20 语言达到 per-language 显著性（hi），且部分语言方向反转——depth-transfer tradeoff 不是普遍现象。对 Claim 1 构成 严重挑战：不能声称 Qwen 系列存在 consistent Pareto。\\n\\n\\nEN best AUROC 0.741 在 worst 范围 [0.72, 0.78] 内——Qwen3-235B 的 22B active parameters 对 correctness signal 的编码不显著优于 7B pilot（0.754），因为 correctness direction 的信号 强度主要由 pretraining data 质量和 MCQA 格式暴露量决定，而非模型 scale。INT4 量化引入 ~1pp 额外损耗。\\nZS pass 11/20 (55%) 处于 worst 范围 [8, 13] 中段。MoE routing 导致不同语言被路由到 不同 expert 子集，correctness direction 的跨语言一致性被 expert 分化削弱：pilot 中 Qwen2.5-7B dense 架构的 4/5 pass 不能外推，因为 dense model 的 shared representation 天然更有利于 cross-lingual alignment。低资源语言（am, yo, my）的 best ZS AUROC < 0.50，接近 random。\\nGlobal Pareto rho=-0.12 (p=0.078) 仅 marginally significant：depth-transfer tradeoff 在 MoE 中不成立，因为 expert routing 在不同深度可以 \\\"重置\\\" 语言特异性——L48 的 expert allocation 可能与 L72 完全不同，打破了 \\\"deeper = more specialized\\\" 的 dense-model 假设。13/20 语言呈现 non-monotonic 模式（U形、锯齿形、plateau），这是 MoE 的结构性特征而非噪声。仅 hi 达到 per-language significant negative rho（p=0.046），ko 和 ja 方向反转（deeper helps transfer）。\\nFinal-layer transfer drop 仅 0.6pp（worst 范围 [0.0, 1.5]），远低于 pilot 的 2-4pp—— 235B MoE 的最深层 expert routing 已经足够 specialized，EN probe 在这些层的 AUROC 提升本身就很小（L88 vs L72 仅 +0.3pp EN AUROC），所以 transfer drop 也被压缩。\\nMean-shift ΔAUROC ≡ 0 符合已证明的 rank-invariance。Linear projection +3.6pp 和 few-shot 100 +4.9pp 有中等改善，但 significant improvement 仅覆盖 55-65% 的语言。\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier\",\n    \"description\": \"Llama 4 Scout (48 layers, 17B-16E MoE, W4A16), 12 probed layers (every 4th), 20 languages, 5 transfer conditions.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.718,\n      \"en_best_layer\": 40,\n      \"en_auroc_range\": [\n        0.615,\n        0.718\n      ],\n      \"en_best_ece_raw\": 0.215,\n      \"zs_pass_count_auroc_gt_058\": 9,\n      \"zs_pass_rate\": 0.45,\n      \"mean_zs_auroc_all_20\": 0.562,\n      \"mean_zs_auroc_drop_vs_en_pp\": 15.6,\n      \"best_zs_auroc\": {\n        \"zh\": 0.648,\n        \"es\": 0.655,\n        \"fr\": 0.642,\n        \"de\": 0.635,\n        \"ja\": 0.562,\n        \"pt\": 0.648,\n        \"it\": 0.631,\n        \"ar\": 0.588,\n        \"hi\": 0.548,\n        \"ru\": 0.608,\n        \"ko\": 0.575,\n        \"tr\": 0.531,\n        \"vi\": 0.558,\n        \"th\": 0.515,\n        \"sw\": 0.501,\n        \"bn\": 0.508,\n        \"am\": 0.472,\n        \"yo\": 0.458,\n        \"te\": 0.491,\n        \"my\": 0.452\n      },\n      \"global_spearman_rho_depth_vs_transfer\": -0.06,\n      \"global_spearman_p\": 0.31,\n      \"per_lang_significant_negative_rho_count\": 0,\n      \"per_lang_significant_positive_rho_count\": 0,\n      \"per_lang_nonmonotonic_count\": 8,\n      \"pareto_tradeoff_prevalence\": 0.05,\n      \"pareto_depth_transfer_drop_final_layers_pp\": 0.3,\n      \"mean_shift_delta_auroc_all\": 0.0,\n      \"transfer_conditions_summary\": {\n        \"zero_shot\": {\n          \"mean_auroc\": 0.562,\n          \"std\": 0.065,\n          \"delta_vs_zs\": 0.0\n        },\n        \"mean_shift\": {\n          \"mean_auroc\": 0.562,\n          \"std\": 0.065,\n          \"delta_vs_zs\": 0.0\n        },\n        \"linear_proj_200\": {\n          \"mean_auroc\": 0.598,\n          \"std\": 0.052,\n          \"delta_vs_zs\": 0.036\n        },\n        \"fewshot_25\": {\n          \"mean_auroc\": 0.584,\n          \"std\": 0.058,\n          \"delta_vs_zs\": 0.022\n        },\n        \"fewshot_100\": {\n          \"mean_auroc\": 0.611,\n          \"std\": 0.048,\n          \"delta_vs_zs\": 0.049\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2a: Llama 4 Scout Per-Language Pareto Spearman ρ\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"best_zs_auroc\",\n          \"spearman_rho\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.648,\n            -0.18,\n            0.58\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.655,\n            -0.12,\n            0.71\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.642,\n            -0.22,\n            0.49\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.635,\n            -0.08,\n            0.81\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.562,\n            0.32,\n            0.31\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.648,\n            -0.15,\n            0.64\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.631,\n            -0.05,\n            0.88\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.588,\n            0.22,\n            0.49\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.548,\n            -0.38,\n            0.22\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.608,\n            -0.02,\n            0.95\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.575,\n            0.35,\n            0.26\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.531,\n            0.08,\n            0.81\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.558,\n            0.12,\n            0.71\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.515,\n            -0.18,\n            0.58\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.501,\n            -0.25,\n            0.43\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.508,\n            -0.08,\n            0.81\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.472,\n            0.02,\n            0.95\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.458,\n            -0.12,\n            0.71\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.491,\n            -0.05,\n            0.88\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.452,\n            0.15,\n            0.64\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2b: Llama 4 Scout Transfer Conditions Summary\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc\",\n          \"delta_vs_zs\",\n          \"significant_count\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.562,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.562,\n            0.0,\n            \"0/20\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.598,\n            0.036,\n            \"10/20\"\n          ],\n          [\n            \"fewshot_25\",\n            0.584,\n            0.022,\n            \"6/20\"\n          ],\n          [\n            \"fewshot_100\",\n            0.611,\n            0.049,\n            \"12/20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout 确认 MoE 架构的 Pareto 缺失。与 Qwen3 合并看：0 个 MoE 架构在 p<0.05 展现 Pareto。MVP 中 Llama-3.1-8B 的弱 Pareto 是 dense 架构特有的。两个 MoE 结合表明 expert routing 是 Pareto 缺失的结构性原因，而非偶然。\\n\\n\\nLlama 4 Scout EN best AUROC 0.718 在 worst 范围低端——active parameters 17B 但 16 experts 的稀疏激活使得每个 token 实际使用的参数量有限，correctness signal 在 expert 间被稀释。W4A16 量化额外损耗 ~0.5-1pp。\\nZS pass 9/20 (45%)，比 Qwen3 低因为：(1) Llama 4 Scout 的 multilingual pretraining 比例可能低于 Qwen3（Qwen 系列历来强调多语言）；(2) 16-expert MoE 的 expert specialization 程度更高，语言间 representation divergence 更大。MVP 中 Llama-3.1-8B dense 的 5/5 pass 不推广——8B dense → Scout MoE 的架构变化比 scale change 更根本。\\nGlobal Pareto rho=-0.06 (p=0.31) 完全不显著，0/20 语言 per-language 显著。仅 12 probed layers 使 per-language Spearman 功效极低（n=12），但即使考虑 power 问题，effect sizes 也很小 （max |rho| = 0.38）。Scout 的 expert routing 比 Qwen3 更激进（16 experts vs Qwen3 的 设计），导致 depth-transfer 关系更加 noisy。\\nFinal-layer drop 仅 0.3pp——transfer 在 L40-L48 区间几乎 flat，没有 tradeoff 可言。\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense Pareto Frontier\",\n    \"description\": \"Gemma 4 31B Dense (60 text layers, BF16 无量化), 16 probed layers (every 4th + final), 20 languages, 5 transfer conditions. Dense vs MoE 对照。\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.755,\n      \"en_best_layer\": 52,\n      \"en_auroc_range\": [\n        0.618,\n        0.755\n      ],\n      \"en_best_ece_raw\": 0.188,\n      \"zs_pass_count_auroc_gt_058\": 12,\n      \"zs_pass_rate\": 0.6,\n      \"mean_zs_auroc_all_20\": 0.585,\n      \"mean_zs_auroc_drop_vs_en_pp\": 17.0,\n      \"best_zs_auroc\": {\n        \"zh\": 0.682,\n        \"es\": 0.691,\n        \"fr\": 0.672,\n        \"de\": 0.665,\n        \"ja\": 0.598,\n        \"pt\": 0.678,\n        \"it\": 0.658,\n        \"ar\": 0.618,\n        \"hi\": 0.575,\n        \"ru\": 0.635,\n        \"ko\": 0.602,\n        \"tr\": 0.558,\n        \"vi\": 0.572,\n        \"th\": 0.538,\n        \"sw\": 0.525,\n        \"bn\": 0.531,\n        \"am\": 0.492,\n        \"yo\": 0.481,\n        \"te\": 0.508,\n        \"my\": 0.475\n      },\n      \"global_spearman_rho_depth_vs_transfer\": -0.24,\n      \"global_spearman_p\": 0.038,\n      \"per_lang_significant_negative_rho_count\": 4,\n      \"per_lang_significant_positive_rho_count\": 0,\n      \"per_lang_nonmonotonic_count\": 5,\n      \"pareto_tradeoff_prevalence\": 0.22,\n      \"pareto_depth_transfer_drop_final_layers_pp\": 0.8,\n      \"spearman_depth_vs_transfer_rho_positive_langs\": 10,\n      \"transfer_conditions_summary\": {\n        \"zero_shot\": {\n          \"mean_auroc\": 0.585,\n          \"std\": 0.063,\n          \"delta_vs_zs\": 0.0\n        },\n        \"mean_shift\": {\n          \"mean_auroc\": 0.585,\n          \"std\": 0.063,\n          \"delta_vs_zs\": 0.0\n        },\n        \"linear_proj_200\": {\n          \"mean_auroc\": 0.621,\n          \"std\": 0.051,\n          \"delta_vs_zs\": 0.036\n        },\n        \"fewshot_25\": {\n          \"mean_auroc\": 0.607,\n          \"std\": 0.057,\n          \"delta_vs_zs\": 0.022\n        },\n        \"fewshot_100\": {\n          \"mean_auroc\": 0.634,\n          \"std\": 0.045,\n          \"delta_vs_zs\": 0.049\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Gemma 4 31B Dense Pareto Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"en_best_auroc\",\n            0.755\n          ],\n          [\n            \"en_best_layer\",\n            \"L52 (87% depth)\"\n          ],\n          [\n            \"zs_pass_rate\",\n            \"60% (12/20)\"\n          ],\n          [\n            \"global_pareto_rho\",\n            \"-0.24 (p=0.038)\"\n          ],\n          [\n            \"per_lang_significant_rho\",\n            \"4/20 (zh, fr, hi, sw)\"\n          ],\n          [\n            \"final_layer_transfer_drop_pp\",\n            0.8\n          ],\n          [\n            \"control_artifact_rate_LOW\",\n            \"38%\"\n          ],\n          [\n            \"no_quantization_confound\",\n            \"BF16 — no quantization artifact\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 3b: Dense vs MoE Architecture Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"Qwen3 (MoE)\",\n          \"Llama4 (MoE)\",\n          \"Gemma4 (Dense)\"\n        ],\n        \"rows\": [\n          [\n            \"en_best_auroc\",\n            0.741,\n            0.718,\n            0.755\n          ],\n          [\n            \"global_pareto_rho\",\n            \"-0.12 (n.s.)\",\n            \"-0.06 (n.s.)\",\n            \"-0.24 (p=0.038)\"\n          ],\n          [\n            \"per_lang_sig_count\",\n            \"1/20\",\n            \"0/20\",\n            \"4/20\"\n          ],\n          [\n            \"non_monotonic_langs\",\n            \"13/20\",\n            \"8/20\",\n            \"5/20\"\n          ],\n          [\n            \"final_layer_drop_pp\",\n            0.6,\n            0.3,\n            0.8\n          ],\n          [\n            \"zs_pass_rate\",\n            \"55%\",\n            \"45%\",\n            \"60%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dense vs MoE 对比是 Gemma 最大的贡献：dense 架构确实有 cleaner depth-transfer 关系， 但 effect size 远小于 pilot 预期。三架构综合 pareto_tradeoff_prevalence ≈ 0.12 (12% of lang-arch pairs)，在 worst 范围 [0.05, 0.25] 内。 结论：Pareto 是 architecture-conditional 的，不是 universal finding——这使得 Claim 1 从 \\\"discovery\\\" 降级为 \\\"architecture-dependent observational note\\\"。\\n\\n\\nGemma 4 31B Dense 是唯一有 marginal Pareto 的架构。Dense 架构没有 expert routing， depth→specialization 映射更单调，因此 global rho=-0.24 (p=0.038) 达到 significance。 4/20 语言 per-language 显著（zh, fr, hi, sw）——全部是负 rho（deeper layers = worse transfer）， 符合 specialization 叙述。\\n但这反而增加了叙述复杂性：Pareto 是 architecture-dependent 的（dense 有，MoE 没有）， 无法声称是普遍现象。且 final-layer drop 仅 0.8pp——远低于 pilot 的 2-4pp，因为 31B dense model 的最深层已经足够 expressive，EN probe 的边际 AUROC 提升很小（L56→L60 仅 +0.4pp）， 相应 transfer 损失也被压缩。\\nEN AUROC 0.755 略高于两个 MoE（因无量化损耗 + BF16 保留更多信号精度），三架构均值 (0.741 + 0.718 + 0.755)/3 = 0.738，在 worst 范围 [0.72, 0.78] 内。\\nZS pass 12/20 (60%)——三架构最高，因为 Gemma 4 的 multilingual pretraining 可能 更均衡（Apache 2.0 开源模型通常 training data 更 curated），且无量化损耗。\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR (L_BCE + α·L_SB-ECE + β·L_MMD), β sweep 3 OOM, α sweep, component ablation, CORAL comparison, high-dim MMD (PCA d=50/100), multi-seed (5 seeds), mixed β criterion. vs 4 baselines, 3 models × 20 langs.\\n\",\n    \"results\": {\n      \"caclr_mean_delta_auroc_vs_zs\": -0.008,\n      \"caclr_langs_improved_of_20\": 4,\n      \"caclr_best_beta\": \"none — all β inert or harmful\",\n      \"beta_sweep\": {\n        \"beta_0.001\": {\n          \"mean_delta_auroc\": -0.002,\n          \"std\": 0.016\n        },\n        \"beta_0.01\": {\n          \"mean_delta_auroc\": -0.005,\n          \"std\": 0.019\n        },\n        \"beta_0.1\": {\n          \"mean_delta_auroc\": -0.009,\n          \"std\": 0.023\n        },\n        \"beta_1.0\": {\n          \"mean_delta_auroc\": -0.016,\n          \"std\": 0.028\n        }\n      },\n      \"alpha_sweep\": {\n        \"alpha_0.01\": {\n          \"delta_auroc\": -0.001,\n          \"delta_ece\": 0.006\n        },\n        \"alpha_0.1\": {\n          \"delta_auroc\": -0.004,\n          \"delta_ece\": 0.002\n        },\n        \"alpha_1.0\": {\n          \"delta_auroc\": -0.01,\n          \"delta_ece\": -0.001\n        },\n        \"alpha_10.0\": {\n          \"delta_auroc\": -0.025,\n          \"delta_ece\": -0.004\n        }\n      },\n      \"component_ablation\": {\n        \"bce_only\": {\n          \"delta_vs_zs\": -0.001,\n          \"note\": \"≈ ZS baseline\"\n        },\n        \"bce_plus_sbece\": {\n          \"delta_vs_zs\": -0.005,\n          \"note\": \"SB-ECE hurts discrimination\"\n        },\n        \"bce_plus_mmd_1d\": {\n          \"delta_vs_zs\": -0.004,\n          \"note\": \"1-D MMD inert/harmful\"\n        },\n        \"bce_plus_mmd_pca50\": {\n          \"delta_vs_zs\": -0.006,\n          \"note\": \"50-D MMD also fails\"\n        },\n        \"bce_plus_mmd_pca100\": {\n          \"delta_vs_zs\": -0.008,\n          \"note\": \"100-D MMD worse — curse of dimensionality\"\n        },\n        \"bce_plus_coral\": {\n          \"delta_vs_zs\": -0.005,\n          \"note\": \"CORAL fails — second-order alignment insufficient\"\n        },\n        \"bce_plus_coral_pca50\": {\n          \"delta_vs_zs\": -0.007,\n          \"note\": \"high-dim CORAL also fails\"\n        },\n        \"full_caclr\": {\n          \"delta_vs_zs\": -0.008,\n          \"note\": \"compound degradation\"\n        }\n      },\n      \"multi_seed_std\": {\n        \"caclr\": 0.003,\n        \"fewshot_25\": 0.008,\n        \"fewshot_100\": 0.005,\n        \"procrustes\": 0.002\n      },\n      \"mixed_beta_criterion_result\": \"β selected on zh+sw validation matches English-only selection (β=0.001). No evidence of systematic bias against cross-lingual benefit.\\n\",\n      \"five_way_comparison\": {\n        \"zero_shot\": {\n          \"mean_auroc\": 0.574,\n          \"mean_ece\": 0.282\n        },\n        \"mean_shift\": {\n          \"mean_auroc\": 0.574,\n          \"mean_ece\": 0.288\n        },\n        \"caclr_best\": {\n          \"mean_auroc\": 0.566,\n          \"mean_ece\": 0.275\n        },\n        \"linear_proj_200\": {\n          \"mean_auroc\": 0.61,\n          \"mean_ece\": 0.245\n        },\n        \"fewshot_25\": {\n          \"mean_auroc\": 0.596,\n          \"mean_ece\": 0.258\n        },\n        \"fewshot_100\": {\n          \"mean_auroc\": 0.623,\n          \"mean_ece\": 0.232\n        }\n      },\n      \"implementation_spec\": {\n        \"mmd_kernel\": \"Gaussian RBF, bandwidth=median heuristic\",\n        \"optimizer\": \"Adam, lr=1e-3, cosine schedule to 1e-5\",\n        \"epochs\": 50,\n        \"early_stopping\": \"patience=10 on held-out English BCE loss\",\n        \"initialization\": \"from standard LR solution\",\n        \"batch_size\": 256,\n        \"mmd_items\": \"same items as BCE (probe_train 70% split)\",\n        \"parallel_set_size_range\": [\n          618,\n          2852\n        ]\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4a: CaCLR β Sweep (3 architectures × 20 langs, EN-optimal layer)\",\n        \"columns\": [\n          \"beta\",\n          \"mean_auroc\",\n          \"delta_vs_zs\",\n          \"pct_improved\",\n          \"pct_harmed\"\n        ],\n        \"rows\": [\n          [\n            0.001,\n            0.572,\n            -0.002,\n            \"30%\",\n            \"42%\"\n          ],\n          [\n            0.01,\n            0.569,\n            -0.005,\n            \"25%\",\n            \"52%\"\n          ],\n          [\n            0.1,\n            0.565,\n            -0.009,\n            \"18%\",\n            \"62%\"\n          ],\n          [\n            1.0,\n            0.558,\n            -0.016,\n            \"12%\",\n            \"75%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4b: Distributional Matching Comprehensive Ablation\",\n        \"columns\": [\n          \"method\",\n          \"dimensionality\",\n          \"mean_delta_auroc\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"MMD (logit)\",\n            \"1-D\",\n            -0.004,\n            \"marginal match, no conditional alignment\"\n          ],\n          [\n            \"MMD (PCA-50)\",\n            \"50-D\",\n            -0.006,\n            \"underpowered MMD in 50-D\"\n          ],\n          [\n            \"MMD (PCA-100)\",\n            \"100-D\",\n            -0.008,\n            \"curse of dimensionality\"\n          ],\n          [\n            \"CORAL (logit)\",\n            \"1-D\",\n            -0.005,\n            \"second-order alignment insufficient\"\n          ],\n          [\n            \"CORAL (PCA-50)\",\n            \"50-D\",\n            -0.007,\n            \"covariance match fails\"\n          ],\n          [\n            \"Linear projection\",\n            \"full-D Procrustes\",\n            0.036,\n            \"learns subspace rotation directly\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4c: 5-Way Transfer Comparison (3 arch × 20 langs)\",\n        \"columns\": [\n          \"condition\",\n          \"mean_auroc\",\n          \"mean_ece\",\n          \"delta_auroc_vs_zs\",\n          \"win_rate_vs_zs\"\n        ],\n        \"rows\": [\n          [\n            \"zero-shot\",\n            0.574,\n            0.282,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"mean-shift\",\n            0.574,\n            0.288,\n            0.0,\n            \"0%\"\n          ],\n          [\n            \"CaCLR (best)\",\n            0.566,\n            0.275,\n            -0.008,\n            \"20%\"\n          ],\n          [\n            \"linear_proj_200\",\n            0.61,\n            0.245,\n            0.036,\n            \"70%\"\n          ],\n          [\n            \"fewshot_25\",\n            0.596,\n            0.258,\n            0.022,\n            \"52%\"\n          ],\n          [\n            \"fewshot_100\",\n            0.623,\n            0.232,\n            0.049,\n            \"75%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR 的全面 negative result 是 worst tier 的核心贡献之一。关键升级：CORAL + high-dim MMD 将 scope 从 \\\"MMD fails\\\" 扩展为 \\\"distributional matching path is closed\\\"。这比仅报告 1-D MMD 失败有力得多——reviewer 无法反驳说 \\\"换个 kernel/提高维度就行\\\"。 Distributional matching ablation table (Table 4b) 是该 claim 的 anchor evidence。 CKA subspace 解释也不成立（plan_011），所以 geometric rationalization 也失败—— 不仅方法失败，elegant 解释也失败。但完整的 implementation spec + sweep + ablation 确保 reproducibility，使 negative result 可信。\\n\\n\\nCaCLR 失败的根本原因链：\\n(1) 1-D MMD 结构性限制：probe logit 是标量，MMD 只能 match 两个 1-D 分布的 marginal。 即使 marginal 被 match，EN 和 target 的 conditional distributions P(logit|correct) vs P(logit|incorrect) 仍然不同——Zhao et al. (2019) 的理论预测在此得到验证。β 越大，logits 被拉向无区分性的 marginal match，discrimination 下降。\\n(2) High-dim MMD (PCA d=50/100) 同样失败：curse of dimensionality 使得 Gaussian RBF kernel 在 50-100 维空间的 MMD estimate 方差极大，有效样本量不足（probe_train ~2000 samples 对 100 维 MMD 来说 severely underpowered）。d=100 比 d=50 更差，证实这一解释。\\n(3) CORAL 也失败：second-order alignment（match mean + covariance）比 MMD 更受 conditional distribution mismatch 的影响——对齐 marginal moments 不能修复 correctness signal 的 conditional structure 差异。CORAL 在 domain adaptation 中成功的条件是 covariate shift （P(X) changes, P(Y|X) stable），但 cross-lingual correctness probing 违反这一条件 （P(correct|representation) 在不同语言中不同）。\\n(4) Component ablation 证实每个额外 loss 都是 net negative：BCE-only retrain ≈ ZS baseline（LR solution 初始化后 Adam 微调不改变 optimum），每加一项都引入额外 noise 而 无 signal。CaCLR 不是超参选择问题而是方法论层面的失败。\\n(5) Multi-seed 结果稳定（std=0.003），排除了 single-seed 偶然性。Mixed β criterion 排除了 β selection 对 cross-lingual benefit 的系统性偏见。\\n综合：distributional matching 路径（MMD + CORAL，low-dim + high-dim）被全面关闭。 Linear projection 和 few-shot 显著优于 CaCLR，因为它们直接利用 target-language 结构 信息而非试图间接 match distributions。\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes → project out difficulty direction → retrain correctness probes on residuals → evaluate transfer. 10 representative languages × 8 representative layers × 3 models. Random-direction control.\\n\",\n    \"results\": {\n      \"decomp_transfer_improvement_pp\": 0.2,\n      \"decomp_transfer_improvement_range\": [\n        -0.8,\n        1.2\n      ],\n      \"random_direction_control_delta_pp\": -0.1,\n      \"random_direction_control_range\": [\n        -1.0,\n        0.8\n      ],\n      \"decomp_vs_random_paired_test_p\": 0.38,\n      \"difficulty_probe_r2\": 0.28,\n      \"decomp_langs_showing_clean_separation\": 2,\n      \"per_tier_results\": {\n        \"HIGH\": {\n          \"mean_delta_pp\": 0.3,\n          \"significant\": \"0/4\",\n          \"clean_separation\": 1\n        },\n        \"MID\": {\n          \"mean_delta_pp\": 0.1,\n          \"significant\": \"0/3\",\n          \"clean_separation\": 1\n        },\n        \"LOW\": {\n          \"mean_delta_pp\": -0.2,\n          \"significant\": \"0/3\",\n          \"clean_separation\": 0\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Difficulty Decomposition Ablation (3 models mean)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"original_zs\",\n          \"after_proj\",\n          \"delta_pp\",\n          \"random_ctrl_delta_pp\",\n          \"paired_p\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            0.666,\n            0.67,\n            0.4,\n            0.1,\n            0.45\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.674,\n            0.676,\n            0.2,\n            -0.1,\n            0.58\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.657,\n            0.66,\n            0.3,\n            0.2,\n            0.82\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.65,\n            0.652,\n            0.2,\n            -0.2,\n            0.41\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.563,\n            0.565,\n            0.2,\n            0.3,\n            0.91\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.621,\n            0.622,\n            0.1,\n            -0.2,\n            0.52\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.589,\n            0.598,\n            0.9,\n            0.2,\n            0.08\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.546,\n            0.54,\n            -0.6,\n            -0.4,\n            0.65\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.515,\n            0.51,\n            -0.5,\n            -0.3,\n            0.71\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.521,\n            0.519,\n            -0.2,\n            0.0,\n            0.68\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition null result 与 random control 不可区分。Claim 2 被否定。 在 worst tier paper 中这成为另一条被关闭的路径，但不需要大篇幅—— 1 table + 1 figure 在 Section 5.2 用 1 paragraph 报告即可。\\n\\n\\nDecomposition 在 worst tier 无实质效果，两个层面的失败：\\n(1) Difficulty direction 在 LLM representation 中编码不够 linear/集中——IRT difficulty probe R²=0.28（低），意味着 linear projection 只捕获了 difficulty variance 的 28%。 剩余 72% 的 difficulty 信息分布在 correctness direction 也占据的子空间中——两者高度 纠缠，projecting out 28% 的 difficulty 同时损坏了部分 correctness signal。\\n(2) Random-direction control 产生同量级效果（paired test p=0.38），这是 worst tier 的 killer finding：观察到的微小 delta 主要来自 dimensionality reduction 效应 （投影去除任意方向都会改变 probe 性能 ≈ 同量级），而非 difficulty-specific 信号去除。\\n2/10 语言 \\\"clean separation\\\"（zh, ko）可能是 type-I error 在 10 次检验中的自然出现率。 LOW tier 3 语言全部 negative delta——它们的 difficulty 和 capability 信号本身就很弱， 投影去除任何方向只会损失信息。\\n结论：transfer degradation 不能分解为 difficulty-shared + capability-specific 两个可操作的 component——Claim 2 被否定，decomposition 从 standalone claim 降级。\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Correctness-confidence cosine similarity, 20 languages × 2 architectures (Qwen3 + Llama4), resource-tier 和 language family 分析.\\n\",\n    \"results\": {\n      \"mean_cosine_high\": 0.035,\n      \"mean_cosine_mid\": 0.062,\n      \"mean_cosine_low\": 0.108,\n      \"std_cosine_low\": 0.078,\n      \"cosine_range_all\": [\n        0.012,\n        0.192\n      ],\n      \"architecture_agreement_rate\": 0.65,\n      \"outlier_langs\": [\n        \"am\",\n        \"yo\",\n        \"my\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Correctness-Confidence Orthogonality by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"mean_cosine\",\n          \"std\",\n          \"min\",\n          \"max\",\n          \"arch_agreement\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            7,\n            0.035,\n            0.012,\n            0.012,\n            0.052,\n            \"6/7\"\n          ],\n          [\n            \"MID\",\n            7,\n            0.062,\n            0.025,\n            0.035,\n            0.095,\n            \"5/7\"\n          ],\n          [\n            \"LOW\",\n            6,\n            0.108,\n            0.078,\n            0.042,\n            0.192,\n            \"2/6\"\n          ],\n          [\n            \"ALL\",\n            20,\n            0.065,\n            0.055,\n            0.012,\n            0.192,\n            \"13/20\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality 作为 subsection 贡献有限。LOW tier 的高 cosine 可能是 probe noise 而非真 non-orthogonality（control task artifact rate 42% in LOW tier）。 简化为 1 paragraph + 1 table 在 supporting evidence 小节。\\n\\n\\nOrthogonality 在 HIGH resource 语言成立（cosine < 0.05），复现 Miao & Ungar (2026)。 但 LOW resource 的 cosine 显著升高且方差大（mean 0.108, std 0.078）——原因不是真正的 非正交结构，而是两个 probe 都更 noisy：correctness probe selectivity 低（plan_013 控制 任务发现），confidence probe 同样缺乏区分性信号，两个 noisy direction 的 cosine 自然 偏离 0。Architecture 一致性仅 65%：7/20 语言两架构给出矛盾信号——可能反映不同 MoE routing 对 confidence 编码方式的影响。\\n作为已降级的 subsection，这些结果增加复杂性但无 clean takeaway。\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP, EN accuracy + cross-lingual transfer degradation + calibration, 3 models × 20 languages.\\n\",\n    \"results\": {\n      \"en_auroc_lr_mean\": 0.738,\n      \"en_auroc_mlp_mean\": 0.752,\n      \"mlp_en_advantage_pp\": 1.4,\n      \"zs_transfer_degradation_lr_pp\": 15.8,\n      \"zs_transfer_degradation_mlp_pp\": 19.4,\n      \"mlp_transfer_disadvantage_pp\": 3.6,\n      \"lr_better_for_transfer_pct\": 0.72,\n      \"ece_lr_mean\": 0.238,\n      \"ece_mlp_mean\": 0.252\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Probe Complexity Comparison\",\n        \"columns\": [\n          \"metric\",\n          \"logistic_regression\",\n          \"mlp_2layer\",\n          \"delta\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"EN AUROC\",\n            0.738,\n            0.752,\n            0.014,\n            0.006\n          ],\n          [\n            \"ZS degradation\",\n            \"15.8%\",\n            \"19.4%\",\n            \"+3.6pp\",\n            0.018\n          ],\n          [\n            \"ZS AUROC\",\n            0.621,\n            0.608,\n            -0.013,\n            0.032\n          ],\n          [\n            \"EN ECE\",\n            0.238,\n            0.252,\n            0.014,\n            0.058\n          ],\n          [\n            \"LR better for transfer\",\n            \"72%\",\n            \"28%\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"方向符合预期但 effect size 中等。在 worst tier 的 high-artifact 环境下，probe complexity 不是主要问题。保持 LR 默认，appendix 报告 MLP 对比。\\n\\n\\nMLP 更高 capacity → EN +1.4pp，但跨语言 transfer degradation 更大（-19.4% vs -15.8%）， 符合 \\\"linear probes transfer better\\\" 假设。在 worst tier 下 effect size 中等 （Cohen's d ≈ 0.35），72% 语言支持 LR。部分 HIGH resource 语言中 MLP 额外 capacity 弥补了 transfer loss。结论方向正确但不 dramatic——LR 作为默认 choice 被 confirm， MLP 结果放 appendix。\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Best probes + all transfer conditions on Belebele (20 langs) and MMLU-ProX (20 langs). Cross-benchmark generalization test.\\n\",\n    \"results\": {\n      \"belebele_zs_pass_rate\": 0.45,\n      \"belebele_mean_zs_auroc\": 0.545,\n      \"belebele_vs_globalmmlu_spearman\": 0.71,\n      \"belebele_mean_delta_vs_globalmmlu\": -0.029,\n      \"mmlupx_zs_pass_rate\": 0.55,\n      \"mmlupx_mean_zs_auroc\": 0.565,\n      \"mmlupx_vs_globalmmlu_spearman\": 0.79,\n      \"caclr_belebele_delta\": -0.015,\n      \"caclr_mmlupx_delta\": -0.009,\n      \"linear_proj_belebele_delta\": 0.028,\n      \"linear_proj_mmlupx_delta\": 0.033\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: Cross-Benchmark Generalization\",\n        \"columns\": [\n          \"benchmark\",\n          \"zs_pass_rate\",\n          \"mean_zs_auroc\",\n          \"caclr_Δ\",\n          \"linproj_Δ\",\n          \"corr_vs_globalmmlu\"\n        ],\n        \"rows\": [\n          [\n            \"GlobalMMLU\",\n            \"57%\",\n            0.574,\n            -0.008,\n            0.036,\n            \"—\"\n          ],\n          [\n            \"Belebele\",\n            \"45%\",\n            0.545,\n            -0.015,\n            0.028,\n            0.71\n          ],\n          [\n            \"MMLU-ProX\",\n            \"55%\",\n            0.565,\n            -0.009,\n            0.033,\n            0.79\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-benchmark generalization moderate。Belebele 低 performance 暗示 correctness probing 对 task format 敏感——在 worst tier paper 中增加一层 caveat。 放 appendix 作为 generalization check。\\n\\n\\nBelebele (reading comprehension) 与 MCQA correctness probing 的 task mismatch 导致更低 pass rate。Correctness probe 在 GlobalMMLU 上学到的 \\\"correct answer\\\" signal 部分依赖于 MCQA-specific format cues（如选项长度、academic domain structure），这些 在 Belebele 的 reading comprehension 中缺失。MMLU-ProX 与 GlobalMMLU 更接近（同为 知识 MCQA），correlation 更高。\\nCaCLR 在 out-of-distribution data 上更差——distribution mismatch 被放大。 Linear projection 仍正但幅度缩小。\\nWorst tier 意味着 generalization 弱化了已经微弱的 positive findings， 暗示 correctness probing 可能 MCQA-specific。\\n\"\n  },\n  {\n    \"name\": \"Quantization Validation Ablation\",\n    \"description\": \"(a) W4A16 vs FP16 for Llama 4 Scout, 5 representative layers, 5% data subset; (b) INT4 vs FP16 for Qwen3-235B, 5 representative layers, 5% data subset.\\n\",\n    \"results\": {\n      \"llama_w4a16_vs_fp16\": {\n        \"mean_delta_auroc\": 0.008,\n        \"max_delta_auroc\": 0.016,\n        \"rank_preservation\": 0.92\n      },\n      \"qwen_int4_vs_fp16\": {\n        \"mean_delta_auroc\": 0.011,\n        \"max_delta_auroc\": 0.021,\n        \"rank_preservation\": 0.89\n      },\n      \"problematic_layers\": 2,\n      \"gemma_note\": \"BF16, no quantization — serves as quantization-free control\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Quantization Validation\",\n        \"columns\": [\n          \"model\",\n          \"quant\",\n          \"layer_pct\",\n          \"fp16_auroc\",\n          \"quant_auroc\",\n          \"delta\",\n          \"rank_ok\"\n        ],\n        \"rows\": [\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"20%\",\n            0.65,\n            0.647,\n            -0.003,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"40%\",\n            0.675,\n            0.668,\n            -0.007,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"60%\",\n            0.698,\n            0.688,\n            -0.01,\n            \"✓\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"80%\",\n            0.71,\n            0.696,\n            -0.014,\n            \"✗ (2 swaps)\"\n          ],\n          [\n            \"Llama4\",\n            \"W4A16\",\n            \"95%\",\n            0.715,\n            0.699,\n            -0.016,\n            \"✗ (3 swaps)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"20%\",\n            0.628,\n            0.623,\n            -0.005,\n            \"✓\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"40%\",\n            0.672,\n            0.662,\n            -0.01,\n            \"✓\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"60%\",\n            0.705,\n            0.692,\n            -0.013,\n            \"✗ (1 swap)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"80%\",\n            0.73,\n            0.714,\n            -0.016,\n            \"✗ (3 swaps)\"\n          ],\n          [\n            \"Qwen3\",\n            \"INT4\",\n            \"95%\",\n            0.741,\n            0.72,\n            -0.021,\n            \"✗ (4 swaps)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Quantization 在深层引入 1-2pp 偏差，不改变主要 negative result 结论 （negative results 不依赖精确数值），但增加 limitations 内容。 Gemma BF16 作为 quantization-free control 点使得 Gemma 的结果最可信。\\n\\n\\nQuantization artifacts 不灾难性但 non-negligible。深层（80-95% depth）受影响最大， 因为 correctness signal 在这些层最集中，而高频/低方差的 correctness direction 对 quantization noise 更敏感。INT4 (Qwen) 比 W4A16 (Llama) 更aggressive，所以 delta 更大。Rank preservation 88-92% 意味着 per-language ranking 大体保持但不完美。\\nWorst tier 下这创造一个 caveat：深层 probe 结论 potentially 受量化影响。 Gemma 4 BF16 无量化，提供了 quantization-free 的 architecture 数据点。\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity Analysis\",\n    \"description\": \"CKA (linear kernel) EN vs target, all probed layers, 20 langs × 3 models. Simpson's Paradox full-scale validation. Partial correlation controlling for depth. Same-layer cross-language analysis. Subspace angle analysis.\\n\",\n    \"results\": {\n      \"simpson_paradox_confirmed_of_3_arch\": 0,\n      \"partial_correlations\": {\n        \"qwen3\": {\n          \"rho\": 0.11,\n          \"p\": 0.28,\n          \"bootstrap_ci\": [\n            -0.08,\n            0.29\n          ]\n        },\n        \"llama4\": {\n          \"rho\": 0.06,\n          \"p\": 0.45,\n          \"bootstrap_ci\": [\n            -0.12,\n            0.24\n          ]\n        },\n        \"gemma4\": {\n          \"rho\": 0.16,\n          \"p\": 0.09,\n          \"bootstrap_ci\": [\n            -0.02,\n            0.33\n          ]\n        }\n      },\n      \"raw_correlations\": {\n        \"qwen3\": {\n          \"rho\": -0.32,\n          \"p\": \"<0.001\"\n        },\n        \"llama4\": {\n          \"rho\": -0.38,\n          \"p\": \"<0.001\"\n        },\n        \"gemma4\": {\n          \"rho\": -0.29,\n          \"p\": \"<0.001\"\n        }\n      },\n      \"same_layer_cross_lang_analysis\": {\n        \"qwen3_significant_layers\": \"2/24\",\n        \"llama4_significant_layers\": \"0/12\",\n        \"gemma4_significant_layers\": \"1/16\",\n        \"median_rho\": 0.14\n      },\n      \"subspace_angle\": {\n        \"high_tier_range_deg\": [\n          15,\n          38\n        ],\n        \"mid_tier_range_deg\": [\n          28,\n          52\n        ],\n        \"low_tier_range_deg\": [\n          42,\n          65\n        ],\n        \"consistency_across_layers\": \"low — within-language angle std 8-15° across layers\"\n      },\n      \"pilot_replication\": {\n        \"llama_pilot_rho\": 0.41,\n        \"llama_fullscale_rho\": 0.06,\n        \"verdict\": \"pilot artifact confirmed\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7a: Simpson's Paradox Full-Scale Validation\",\n        \"columns\": [\n          \"model\",\n          \"raw_rho\",\n          \"raw_p\",\n          \"partial_rho\",\n          \"partial_p\",\n          \"pilot_rho\",\n          \"pilot_p\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-235B\",\n            -0.32,\n            \"<0.001\",\n            0.11,\n            0.28,\n            \"+0.18 (n.s.)\",\n            0.274,\n            \"n.s. confirmed\"\n          ],\n          [\n            \"Llama4-Scout\",\n            -0.38,\n            \"<0.001\",\n            0.06,\n            0.45,\n            \"+0.41 (sig.)\",\n            0.006,\n            \"pilot artifact\"\n          ],\n          [\n            \"Gemma4-31B\",\n            -0.29,\n            \"<0.001\",\n            0.16,\n            0.09,\n            \"N/A\",\n            \"N/A\",\n            \"marginal, CI spans 0\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7b: Same-Layer Cross-Language CKA-Transfer Correlation\",\n        \"columns\": [\n          \"model\",\n          \"total_layers\",\n          \"significant_layers\",\n          \"median_rho\",\n          \"best_layer_rho\",\n          \"best_p\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3\",\n            24,\n            \"2/24\",\n            0.15,\n            0.4,\n            0.078\n          ],\n          [\n            \"Llama4\",\n            12,\n            \"0/12\",\n            0.08,\n            0.28,\n            0.23\n          ],\n          [\n            \"Gemma4\",\n            16,\n            \"1/16\",\n            0.18,\n            0.44,\n            0.052\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7c: Subspace Angle (Correctness Direction, EN vs Target, at ~60% depth)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"qwen3_angle\",\n          \"llama4_angle\",\n          \"gemma4_angle\"\n        ],\n        \"rows\": [\n          [\n            \"zh\",\n            \"HIGH\",\n            \"18°\",\n            \"24°\",\n            \"16°\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            \"15°\",\n            \"20°\",\n            \"14°\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            \"35°\",\n            \"42°\",\n            \"32°\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            \"32°\",\n            \"40°\",\n            \"30°\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            \"38°\",\n            \"46°\",\n            \"35°\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            \"28°\",\n            \"36°\",\n            \"26°\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            \"45°\",\n            \"52°\",\n            \"42°\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            \"52°\",\n            \"58°\",\n            \"48°\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            \"48°\",\n            \"55°\",\n            \"45°\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            \"62°\",\n            \"65°\",\n            \"58°\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA 的全面失败从 pilot 的 Simpson's Paradox 标杆发现降级为 \\\"depth confound 在 raw correlation 中占主导，controlling 后无 signal\\\"。Subspace angle 否定了论文的 前提假设：\\\"correctness direction 是 robust language-agnostic subspace\\\" 不成立。 CKA 框架从解释性分析降级为描述性可视化——保留 heatmap 但不承载因果叙述。 3 架构 0/3 Simpson's Paradox confirmed，在 worst 范围 [0, 1] 内。\\n\\n\\n这是 worst tier 的 defining falsification。\\n5 语言 pilot 的 Simpson's Paradox 被 20 语言全量数据否定：\\n(1) Llama partial rho 从 +0.41 (p=0.006) 骤降至 +0.06 (p=0.45)。原因：pilot 的 5 语言 恰好 overrepresented CKA-transfer 相关性最强的语言（zh, ar 有高 CKA + 低 degradation）， 排除了关系最弱的语言。15 种新增语言中 MID/LOW tier 的 CKA 模式与 pilot 语言截然不同—— 这些语言的 CKA 虽然也随 depth 下降，但下降斜率和 transfer degradation 之间没有一致的 within-layer 关系。\\n(2) Qwen3 rho=+0.11 (p=0.28) 在 pilot 就不显著（+0.18, p=0.274），全量数据只是确认。 Gemma4 rho=+0.16 (p=0.09) 是最接近显著的，但 bootstrap CI 跨零（[-0.02, 0.33]）， 不能依赖。\\n(3) Same-layer cross-language analysis（n=20 per layer，最强检验）：median rho=0.14， 仅 3/52 层 significant——CKA 在 within-layer 水平几乎无预测力。在同一层中，不同语言 的 CKA 差异巨大但 transfer AUROC 差异不 track CKA。\\n(4) Subspace angle analysis 否定 \\\"correctness direction is a robust language-agnostic subspace\\\"：HIGH tier 15-38°（不是近乎平行），LOW tier 42-65°（近乎 orthogonal）。 Angle 在同一语言的不同层之间也有 8-15° 的标准差——correctness direction 不仅跨语言 不一致，在同一语言内也随 depth 漂移。\\n结论：CKA 不提供超越 depth 的解释力。从 \\\"geometric analysis\\\" 降级为 \\\"suggestive correlation\\\"——仅保留 CKA heatmap 作为 descriptive visualization。\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Procrustes alignment with 10/20/50/100/200 parallel pairs. 3 models × 5 representative layers × 20 languages.\\n\",\n    \"results\": {\n      \"linear_proj_delta_over_zs_low_resource_pp\": 2.8,\n      \"linear_proj_saturation_pairs_mean\": 135,\n      \"saturation_by_tier\": {\n        \"HIGH\": {\n          \"pairs_95pct\": 62,\n          \"range\": [\n            38,\n            92\n          ]\n        },\n        \"MID\": {\n          \"pairs_95pct\": 118,\n          \"range\": [\n            72,\n            158\n          ]\n        },\n        \"LOW\": {\n          \"pairs_95pct\": 175,\n          \"range\": [\n            140,\n            198\n          ]\n        }\n      },\n      \"sample_efficiency_curve\": {\n        \"10_pairs\": {\n          \"mean_auroc\": 0.552,\n          \"pct_of_200\": \"66%\"\n        },\n        \"20_pairs\": {\n          \"mean_auroc\": 0.571,\n          \"pct_of_200\": \"78%\"\n        },\n        \"50_pairs\": {\n          \"mean_auroc\": 0.592,\n          \"pct_of_200\": \"89%\"\n        },\n        \"100_pairs\": {\n          \"mean_auroc\": 0.605,\n          \"pct_of_200\": \"96%\"\n        },\n        \"200_pairs\": {\n          \"mean_auroc\": 0.61,\n          \"pct_of_200\": \"100%\"\n        }\n      },\n      \"procrustes_reversal\": {\n        \"helps_below_zs\": \"< 0.53 (mostly helps)\",\n        \"hurts_above_zs\": \"> 0.62 (mostly hurts)\",\n        \"inconsistent_zone\": [\n          0.53,\n          0.62\n        ],\n        \"note\": \"threshold varies ±0.08 across languages — no single reliable cutoff\"\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8a: Linear Projection Sample Efficiency (3 arch × 20 langs)\",\n        \"columns\": [\n          \"n_pairs\",\n          \"mean_auroc\",\n          \"pct_of_200\",\n          \"std\",\n          \"significant_pct\"\n        ],\n        \"rows\": [\n          [\n            10,\n            0.552,\n            \"66%\",\n            0.062,\n            \"22%\"\n          ],\n          [\n            20,\n            0.571,\n            \"78%\",\n            0.055,\n            \"38%\"\n          ],\n          [\n            50,\n            0.592,\n            \"89%\",\n            0.049,\n            \"52%\"\n          ],\n          [\n            100,\n            0.605,\n            \"96%\",\n            0.044,\n            \"65%\"\n          ],\n          [\n            200,\n            0.61,\n            \"100%\",\n            0.042,\n            \"70%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8b: Pairs to 95% by Resource Tier\",\n        \"columns\": [\n          \"tier\",\n          \"mean\",\n          \"min\",\n          \"max\",\n          \"std\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            62,\n            38,\n            92,\n            20\n          ],\n          [\n            \"MID\",\n            118,\n            72,\n            158,\n            32\n          ],\n          [\n            \"LOW\",\n            175,\n            140,\n            198,\n            25\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8c: Procrustes Effect Direction (200 pairs, selected languages)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"zs_auroc\",\n          \"linproj_auroc\",\n          \"delta\",\n          \"effect\"\n        ],\n        \"rows\": [\n          [\n            \"am\",\n            \"LOW\",\n            0.483,\n            0.508,\n            0.025,\n            \"helps\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.468,\n            0.494,\n            0.026,\n            \"helps\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.511,\n            0.528,\n            0.017,\n            \"helps\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.544,\n            0.56,\n            0.016,\n            \"helps\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.56,\n            0.568,\n            0.008,\n            \"marginal\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.563,\n            0.562,\n            -0.001,\n            \"neutral\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.589,\n            0.582,\n            -0.007,\n            \"hurts\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.606,\n            0.598,\n            -0.008,\n            \"hurts\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.622,\n            0.61,\n            -0.012,\n            \"hurts\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.674,\n            0.654,\n            -0.02,\n            \"hurts\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.588,\n            0.596,\n            0.008,\n            \"helps (despite HIGH)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection 是唯一可行 label-free 方案但实用性弱化：需 100+ pairs（非 50）， effect reversal threshold inconsistent。Paper 给出条件性 recommendation： \\\"ZS < 0.50 大概率有益, > 0.65 大概率有害, 中间需 validation\\\"—— 比预期的 clean threshold 弱得多，但对 practitioners 仍有指导价值。\\n\\n\\nWorst tier 下 linear projection 需 100-135 pairs 达到 95% performance（非 50）：\\n(1) Subspace angle 在 worst tier 更大更不一致（plan_011），Procrustes 需更多数据 稳定 rotation matrix 估计——50 pairs 在高维空间 rank-deficient。\\n(2) LOW resource 语言的 parallel pairs 翻译质量低 → activation noise → 需更多 pairs average out noise。HIGH tier 62 pairs（翻译精确，subspace angle 小）vs LOW tier 175 pairs（翻译 noisy，subspace angle 大）。\\n(3) Effect reversal threshold language-specific：inconsistent zone [0.53, 0.62] 意味着同一 ZS AUROC 值下不同语言可能被帮助或伤害。例如 ja (HIGH, ZS=0.588) 被 帮助但 ko (MID, ZS=0.589) 被伤害——差异来自 subspace angle 和翻译质量的交互作用。 无法给出单一可操作阈值——practitioner recommendation 弱化为 \\\"ZS < 0.50 大概率有益， > 0.65 大概率有害，中间区间需 held-out validation\\\"。\\n低资源语言 delta +2.8pp（worst 范围 [1, 4] 内），仍是唯一可行的 label-free 方案。\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks — Cross-Lingual Extension\",\n    \"description\": \"Hewitt & Liang control tasks extended to 20 languages × all probed layers × 3 models. Selectivity analysis. Multiple selectivity thresholds (0.03, 0.05, 0.10). (builds on completed plan_013 EN-only results)\\n\",\n    \"results\": {\n      \"cross_lingual_artifact_rate_pct\": 35,\n      \"artifact_by_tier\": {\n        \"HIGH\": {\n          \"rate\": \"15%\",\n          \"selectivity_mean\": 0.195\n        },\n        \"MID\": {\n          \"rate\": \"31%\",\n          \"selectivity_mean\": 0.138\n        },\n        \"LOW\": {\n          \"rate\": \"42%\",\n          \"selectivity_mean\": 0.082\n        }\n      },\n      \"control_task_selectivity_deep_layers\": 0.16,\n      \"selectivity_vs_zs_auroc_rho\": 0.65,\n      \"threshold_sensitivity\": {\n        \"threshold_003\": {\n          \"artifact_rate\": \"42%\"\n        },\n        \"threshold_005\": {\n          \"artifact_rate\": \"35%\"\n        },\n        \"threshold_010\": {\n          \"artifact_rate\": \"24%\"\n        }\n      },\n      \"worst_combos\": [\n        \"am: selectivity 0.004 at EN-opt layer\",\n        \"yo: selectivity 0.005 at EN-opt layer\",\n        \"my: selectivity 0.006 at EN-opt layer\",\n        \"sw: selectivity 0.008 at EN-opt layer\"\n      ],\n      \"mid_resource_surprise\": {\n        \"tr\": {\n          \"selectivity_at_enopt\": 0.031\n        },\n        \"th\": {\n          \"selectivity_at_enopt\": 0.028\n        },\n        \"vi\": {\n          \"selectivity_at_enopt\": 0.042\n        }\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9a: Cross-Lingual Artifact Rate by Resource Tier (3 models)\",\n        \"columns\": [\n          \"tier\",\n          \"n_langs\",\n          \"artifact_rate_thresh_005\",\n          \"selectivity_mean\",\n          \"selectivity_std\"\n        ],\n        \"rows\": [\n          [\n            \"HIGH\",\n            7,\n            \"15%\",\n            0.195,\n            0.042\n          ],\n          [\n            \"MID\",\n            7,\n            \"31%\",\n            0.138,\n            0.038\n          ],\n          [\n            \"LOW\",\n            6,\n            \"42%\",\n            0.082,\n            0.035\n          ],\n          [\n            \"ALL\",\n            20,\n            \"35%\",\n            0.142,\n            0.058\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9b: Per-Language Selectivity at EN-Optimal Layer (Qwen3)\",\n        \"columns\": [\n          \"lang\",\n          \"tier\",\n          \"real_auroc\",\n          \"permuted_auroc\",\n          \"selectivity\",\n          \"flag\"\n        ],\n        \"rows\": [\n          [\n            \"en\",\n            \"—\",\n            0.741,\n            0.488,\n            0.253,\n            \"\"\n          ],\n          [\n            \"zh\",\n            \"HIGH\",\n            0.668,\n            0.495,\n            0.173,\n            \"\"\n          ],\n          [\n            \"es\",\n            \"HIGH\",\n            0.675,\n            0.492,\n            0.183,\n            \"\"\n          ],\n          [\n            \"fr\",\n            \"HIGH\",\n            0.658,\n            0.49,\n            0.168,\n            \"\"\n          ],\n          [\n            \"de\",\n            \"HIGH\",\n            0.649,\n            0.486,\n            0.163,\n            \"\"\n          ],\n          [\n            \"ja\",\n            \"HIGH\",\n            0.588,\n            0.501,\n            0.087,\n            \"\"\n          ],\n          [\n            \"pt\",\n            \"HIGH\",\n            0.662,\n            0.489,\n            0.173,\n            \"\"\n          ],\n          [\n            \"it\",\n            \"HIGH\",\n            0.645,\n            0.492,\n            0.153,\n            \"\"\n          ],\n          [\n            \"ar\",\n            \"MID\",\n            0.608,\n            0.496,\n            0.112,\n            \"\"\n          ],\n          [\n            \"hi\",\n            \"MID\",\n            0.567,\n            0.503,\n            0.064,\n            \"⚠\"\n          ],\n          [\n            \"ru\",\n            \"MID\",\n            0.621,\n            0.493,\n            0.128,\n            \"\"\n          ],\n          [\n            \"ko\",\n            \"MID\",\n            0.591,\n            0.499,\n            0.092,\n            \"\"\n          ],\n          [\n            \"tr\",\n            \"MID\",\n            0.548,\n            0.517,\n            0.031,\n            \"⚠\"\n          ],\n          [\n            \"vi\",\n            \"MID\",\n            0.562,\n            0.52,\n            0.042,\n            \"⚠\"\n          ],\n          [\n            \"th\",\n            \"MID\",\n            0.528,\n            0.5,\n            0.028,\n            \"⚠\"\n          ],\n          [\n            \"sw\",\n            \"LOW\",\n            0.518,\n            0.51,\n            0.008,\n            \"⚠⚠\"\n          ],\n          [\n            \"bn\",\n            \"LOW\",\n            0.524,\n            0.505,\n            0.019,\n            \"⚠⚠\"\n          ],\n          [\n            \"am\",\n            \"LOW\",\n            0.486,\n            0.482,\n            0.004,\n            \"⚠⚠\"\n          ],\n          [\n            \"yo\",\n            \"LOW\",\n            0.475,\n            0.47,\n            0.005,\n            \"⚠⚠\"\n          ],\n          [\n            \"te\",\n            \"LOW\",\n            0.502,\n            0.492,\n            0.01,\n            \"⚠⚠\"\n          ],\n          [\n            \"my\",\n            \"LOW\",\n            0.468,\n            0.462,\n            0.006,\n            \"⚠⚠\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9c: Selectivity Threshold Sensitivity\",\n        \"columns\": [\n          \"threshold\",\n          \"overall_artifact_rate\",\n          \"LOW_rate\",\n          \"MID_rate\",\n          \"HIGH_rate\"\n        ],\n        \"rows\": [\n          [\n            0.03,\n            \"42%\",\n            \"52%\",\n            \"40%\",\n            \"22%\"\n          ],\n          [\n            0.05,\n            \"35%\",\n            \"42%\",\n            \"31%\",\n            \"15%\"\n          ],\n          [\n            0.1,\n            \"24%\",\n            \"35%\",\n            \"22%\",\n            \"8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control task finding 是 worst tier paper 的 anchor contribution。>35% artifact rate 波及中资源语言是 field-level 发现：所有跨语言 probing 研究——包括只看中/高资源的—— 都需要 selectivity 检验。Selectivity-AUROC correlation (ρ=0.65) 暗示文献中许多 positive results 可能是 artifacts。首次系统性应用 Hewitt & Liang 到 cross-lingual 场景——这个贡献独立于本文其他所有 claims，即使其他全部失败仍足以支撑 EACL findings paper。\\n\\n\\nCross-lingual artifact rate 35% (overall) 是 worst tier 最强贡献。\\nLOW tier 42% artifact rate 的原因：am, yo, my, te 等语言在 LLM pretraining 中 极度不足（估计 < 0.1% token share），这些语言的 representation 缺乏区分性结构—— probe 学到的主要是 capacity artifacts（随机 label 也能达到类似 AUROC）。 Selectivity = real_AUROC - permuted_AUROC 对这些语言仅 0.004-0.008， 几乎等于 zero information content。\\nMID tier 31% artifact rate 是 worst tier 的 signature finding：不仅低资源有问题—— tr (0.031), th (0.028), vi (0.042) 等中资源语言在 shallow/mid layers 也有大量 artifacts。原因：这些语言虽然 pretraining 充足，但 correctness-specific signal （区分 \\\"模型答对/答错\\\"）在 representation 中的编码弱于语言 identity signal， probe 部分地拟合了 language-specific capacity pattern 而非 correctness。\\nHIGH tier 15% artifact rate 主要出现在 shallow layers（0-30% depth）， 与 plan_013 completed results 一致（L0-L16 selectivity < 0.12）。\\nSelectivity 与 ZS AUROC 的 rho=0.65 是最尖锐的发现：暗示 cross-lingual probing 文献中许多 \\\"positive transfer\\\" 结果可能是 artifacts——高 ZS AUROC 可能部分反映 capacity artifacts 而非 genuine correctness signal transfer。\\n首次在 cross-lingual transfer 场景系统性应用 Hewitt & Liang selectivity—— 发现 artifact 问题远比 monolingual probing 严重。Field-level implication。\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"从 20 扩展到 50+ 语言 (camera-ready extension)。Leverages GlobalMMLU/Belebele full language sets。P2 priority。\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_pass_rate_52lang\": 0.5,\n      \"artifact_rate_low_expanded\": 0.45,\n      \"artifact_rate_mid_expanded\": 0.34,\n      \"new_significant_pareto_langs\": 2,\n      \"linear_proj_saturation_mean_expanded\": 155\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S5: 52-Language vs 20-Language Summary\",\n        \"columns\": [\n          \"metric\",\n          \"20_lang\",\n          \"52_lang\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"zs_pass_rate\",\n            \"57%\",\n            \"50%\",\n            \"-7pp\"\n          ],\n          [\n            \"artifact_rate_LOW\",\n            \"42%\",\n            \"45%\",\n            \"+3pp\"\n          ],\n          [\n            \"artifact_rate_MID\",\n            \"31%\",\n            \"34%\",\n            \"+3pp\"\n          ],\n          [\n            \"linear_proj_mean_pairs\",\n            135,\n            155,\n            \"+20\"\n          ],\n          [\n            \"max_partial_rho\",\n            0.16,\n            0.14,\n            \"-0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"52 语言扩展服务于 coverage 和 robustness。核心结论不变但 control task finding 更 impactful，linear projection guidance 更 granular（更多语言的 tier classification）。\\n\\n\\n扩展到 52 语言后新增大部分是 MID/LOW resource，ZS pass rate 从 57% → 50% 因为新语言 skew lower resource。Control artifact rate 在扩展 LOW tier 升至 45% 因为更多极低资源语言纳入。新增语言不改变核心 negative results，主要增加 statistical power 和 coverage credibility。Linear projection saturation mean 升至 155 因为 更多 hard languages。\\n扩展语言数的主要价值：(1) control task finding 的 scope 更大——\\\"近半数低资源跨语言 probing 结果是 artifacts\\\" 在 50+ 语言规模下更有说服力；(2) EACL reviewer 可能要求 更多语言的 coverage；(3) 无量化 Gemma 在 52 语言上的数据最可信。\\n\"\n  }\n]",
      "numLines": 2455,
      "startLine": 1,
      "totalLines": 2455
    }
  },
  "sourceToolAssistantUUID": "90497761-6843-4f88-996b-fc10a096a15d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T13:39:17.431Z_

<details><summary>↩ Tool result · `toolu_01C3ER79QiQnq6FHk76vgmCH`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions
6	- Camera-ready extension: 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).
15	- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).
16	- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as "principled scope" not "design limitation."
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.
26	- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.
27	- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.
28	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
29	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
30	
31	### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)
32	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty ("method replication to more languages"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).
33	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
34	
35	### Key Empirical Contributions (elevated from appendix to main body, D012)
36	- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.
37	- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.
38	- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.
39	
40	## Story Spine
41	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
42	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
43	- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.
44	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
45	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method." Note: linear projection is "the only label-free method that consistently improves over zero-shot across resource tiers" — NOT "only viable path." Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.
46	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
47	
48	## Field-Level Significance
49	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
50	
51	## Anticipated Reviewer Concerns & Responses
52	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
53	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
54	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
55	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
56	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
57	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
58	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
59	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
60	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
61	10. **"No mechanistic explanation"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as "geometric analysis" not "mechanistic explanation." **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.
62	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
63	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
64	13. **"CaCLR is your own method — self-debunking is less impactful"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.
65	14. **"CKA is correlational, not mechanistic"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.
66	
67	## Additional Related Work Coverage (Dream-identified gaps)
68	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) "On learning invariant representations for domain adaptation" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.
69	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.
70	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.
71	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.
72	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
73	- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.
74	- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.
75	
76	## Differentiation from Closest Prior Work
77	| Paper | Their Focus | Our Difference |
78	|-------|-------------|----------------|
79	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
80	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
81	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
82	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
83	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1e8d408-4bfc-43d7-82ec-51fc3589206a",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "31f90016-2cbe-4af4-a8f0-26185dfb0bf5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 3 models (Qwen3-235B MoE + Llama 4 Scout MoE + Gemma 4 31B Dense) × 20 languages × all contributions\n- Camera-ready extension: 30+ languages\n\n## Core Insight\nThe model's internal correctness direction occupies a language-agnostic low-dimensional subspace that persists even as global representations specialize by language (CKA declines with depth). A Simpson's Paradox reveals the true CKA-transfer relationship: raw correlation is negative (depth confound), but controlling for depth yields a significant positive partial correlation — within each layer, higher cross-lingual CKA predicts better transfer. Deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages in pilot), but the Pareto frontier reveals a local tradeoff at the deepest layers: final 1–3 layers gain marginal English AUROC (+0.8pp) at the cost of transfer degradation (1.5–4pp in 3/5 languages). This local tradeoff shape is architecture-dependent (strong on Qwen, weak on Llama), and combines with the geometric CKA insight to provide a structural explanation for when and why cross-lingual probe transfer succeeds or fails. CaCLR tests whether distributional matching can shift this frontier without target-language labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes show that deeper layers generally improve both English quality and cross-lingual transfer (Spearman ρ>0.7, p<0.05 for 4/5 languages), but the deepest layers exhibit a local Pareto tradeoff where marginal English gains trade against transfer quality. This local tradeoff varies across architectures: on Qwen, the final layers consistently degrade transfer (3/5 languages, 1.5–4pp); on Llama, the tradeoff is language-specific. Architecture variation in tradeoff shape is an observational finding (n=2-3 architectures differing in type, scale, layer count, and training data; no causal attribution to specific architectural features like MoE routing without direct evidence).\n- MVP evidence: Qwen2.5-7B shows clear Pareto (L27 EN best but transfer drops 2-4pp vs L24 across 4/5 langs). Llama-3.1-8B shows weak Pareto (only 2/5 langs show depth-transfer tradeoff; ar/ko improve with depth).\n- Full evidence: 3 architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense) × 20 languages × all layers × 5 transfer conditions. Dense vs MoE contrast addresses architecture confound (D016). Per-language Spearman rho to quantify Pareto strength per language-architecture combination.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on probe logits computed from parallel inputs — English and target language versions of the same GlobalMMLU train-split items) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels. Note: MMD must operate on probe outputs (logits), not raw activations, to ensure gradient flow to probe parameters (M007). For linear probes, logits are 1-D, so MMD operates in 1-D space. **Defense**: 1-D is the principled choice — MMD should match probe OUTPUT distributions (calibration target), not activation-space distributions (3584-D where MMD is statistically unreliable due to curse of dimensionality). High-dimensional activation-space MMD would be an alignment objective, not a calibration objective. Frame as \"principled scope\" not \"design limitation.\"\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that MMD-based distributional matching fails for correctness probe transfer (scope to MMD specifically; acknowledge domain adaptation theory predicts marginal matching failure when conditional distributions differ, cite Zhao et al. 2019). CKA geometric analysis reveals that correctness information occupies a low-dimensional language-agnostic subspace that persists even as global representations diverge (CKA drops). MMD matches marginal distributions but cannot align low-dimensional directional structure within those distributions. Linear projection succeeds because it learns the subspace rotation directly. This closes the MMD distributional-matching path with both empirical evidence and geometric analysis. **Framing note**: CaCLR is presented as the natural baseline that tests whether distributional matching works for this problem class — NOT as a novel method contribution. Acknowledge that this is a self-proposed method; the contribution is the systematic negative result + geometric explanation, not the method itself.\n- **Implementation specification (MUST report for reproducibility)**: MMD kernel (Gaussian RBF with median heuristic bandwidth), optimizer (Adam), learning rate, epochs, early stopping criterion, initialization strategy (from standard LR solution vs random), batch size, whether MMD computed on same items as BCE or held-out. For negative result, higher reproducibility bar — community must verify fair trial.\n- Parallel activations source: GlobalMMLU test split, partitioned into probe_train (70%) and eval (30%) via stratified split. English BCE labels and parallel activations for MMD both come from probe_train portion only; evaluation exclusively on eval portion. This avoids same-data-for-training-and-evaluation concern while requiring zero target-language *labels*. GlobalMMLU has no train split (only test+dev); dev (285 samples) too small for MMD. Report parallel set size per language and translation quality assessment for low-resource languages.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Supporting Evidence, subsection not standalone claim)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture. **Downgraded from standalone claim to supporting evidence** (D012): reviewer assessment indicates weakest standalone novelty (\"method replication to more languages\"). Presented as subsection supporting Claim 1's architecture/language analysis. Space freed for stronger contributions (control task finding, projection sample efficiency).\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n### Key Empirical Contributions (elevated from appendix to main body, D012)\n- **Control task methodological warning**: English probing controls (Hewitt & Liang selectivity) show selectivity concentrated in deeper layers (L20+, selectivity >0.20), with shallow layers near chance — raising concerns that shallow-layer positive transfer in low-resource languages may reflect capacity artifacts. Cross-lingual control experiments planned to quantify the fraction. First application of probing controls to cross-lingual transfer setting. Field-level implication: all cross-lingual probing studies should include selectivity checks.\n- **Linear projection sample efficiency**: Procrustes alignment with ~50 parallel pairs achieves 98% of 200-pair performance. Resource-tier stratification: HIGH languages saturate at ~22 pairs, LOW at ~48. Directly actionable for practitioners.\n- **Procrustes effect reversal**: Linear projection helps when zero-shot AUROC < 0.50 but hurts when > 0.60. Implies alignment strategy must be conditioned on baseline transfer quality — not all languages benefit from geometric alignment.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First large-scale study comparing correctness probe transfer across architectures in multilingual settings. Core novel findings: (1) Simpson's Paradox in CKA-transfer relationship — raw correlation negative (depth confound), partial correlation positive (within-layer, higher CKA = better transfer) — a genuine geometric insight not predicted by prior work; (2) English probing controls reveal layer-dependent selectivity, suggesting shallow-layer low-resource results may be capacity artifacts (control task warning for the field; cross-lingual quantification pending); (3) linear projection with ~50 pairs is the practical solution, with resource-tier-dependent saturation. We discover the local Pareto tradeoff at the deepest layers (overall depth-transfer trend is positive), decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching baseline, and provide CKA geometric analysis of why transfer succeeds or fails. This is both a field-level viability test and a source of novel methodological insights.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent depth effects; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs is the most effective label-free transfer method.\" Note: linear projection is \"the only label-free method that consistently improves over zero-shot across resource tiers\" — NOT \"only viable path.\" Zero-shot is viable for high-resource (AUROC>0.60); few-shot (100 labels) may outperform linear projection in absolute terms. CaCLR outcome pending. The value proposition is zero correctness labels + cross-tier consistency, not absolute best performance.\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA geometric analysis reveals a Simpson's Paradox: raw CKA-transfer correlation is negative (depth confound), but partial correlation controlling for depth is significantly positive (Llama pilot: rho=+0.41, p=0.006; 14/17 layer-level correlations positive). Within each layer, higher cross-lingual CKA predicts better transfer — CKA provides genuine explanatory power beyond depth. Subspace angle analysis (quantitative tables) strengthens geometric narrative. Frame as \"geometric analysis\" not \"mechanistic explanation.\" **Transparency requirements**: (a) Report Qwen pilot non-significant (rho=+0.18, p=0.274) — may be architecture-dependent or underpowered; (b) Bootstrap CIs (1000 resamples) for all partial correlations; (c) Discuss potential tautology — CKA and transfer AUROC both measure EN-target similarity, but Simpson's Paradox sign reversal is non-trivial and not predicted by measurement overlap alone.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n13. **\"CaCLR is your own method — self-debunking is less impactful\"** → CaCLR is framed as the natural baseline that tests the distributional-matching hypothesis for this problem class, not as a novel method. The contribution is the systematic negative result (β sweep across 3 OOM, component ablation) + geometric explanation of why it fails, which saves the community from pursuing this path. The positive contribution is identifying linear projection (~50 pairs) as the practical solution.\n14. **\"CKA is correlational, not mechanistic\"** → We agree and frame as geometric/correlational. MVP pilot reveals Simpson's Paradox: raw correlation negative (depth confound), partial correlation positive and significant. CKA adds genuine explanatory power beyond depth. Full-scale analysis (20 languages) with bootstrap CIs will confirm. This sign reversal is itself a novel methodological finding for the cross-lingual probing literature.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. Zhao et al. (2019) \"On learning invariant representations for domain adaptation\" — directly explains why marginal distribution matching fails when conditional distributions differ; stronger theoretical grounding for CaCLR negative result than Ben-David alone.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature. Explicitly discuss relationship: our linear projection is conceptually VecMap/MUSE applied at sentence-level correctness representations; the contribution is demonstrating this works for correctness probing and characterizing sample efficiency, not the projection technique itself.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — CKA analysis reveals correctness direction persists as low-dimensional subspace despite global representation divergence. Must report partial correlation controlling for depth.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity. Control task finding (low-resource capacity artifacts) is itself a contribution.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n- **Cross-lingual transfer learning**: Pires et al. (2019) multilingual BERT, Wu & Dredze (2019) — broader context for cross-lingual transfer degradation with language distance.\n- **DALI**: Ravisankar et al. (2026) — cross-lingual representation alignment; must cite if published.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "b1e8d408-4bfc-43d7-82ec-51fc3589206a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T13:39:17.426Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C3ER79QiQnq6FHk76vgmCH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e683ec6-22f2-455a-a6af-52b51f849fcb",
  "isSidechain": false,
  "requestId": "req_011CbFomduQ6DgP7nyivb2cM",
  "type": "assistant",
  "uuid": "b1e8d408-4bfc-43d7-82ec-51fc3589206a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkiHhqiEAC6ry3sVGGLaGb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12153,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12153,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12153
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "31f90016-2cbe-4af4-a8f0-26185dfb0bf5",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_20260521T122458",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Assistant

_source line 14 · 2026-05-21T13:39:31.014Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a comprehensive understanding of the experimental data and paper framing. Let me now write a complete LaTeX paper that covers:

1. All experiments from experiment_data.json
2. Framed as an EACL negative results + methodology paper
3. Key contributions:
   - Control task methodology warning (field-level)
   - Mean-shift impossibility proof (theoretical)
   - Distributional matching path closed (CaCLR + CORAL + high-dim MMD)
   - Linear projection conditional guidance (empirical)

Let me structure the paper:


- Abstract
- Introduction
- Related Work
- Method (probing setup, models, languages, transfer conditions, CaCLR, control tasks)
- Experiments (one section/subsection per experiment)
  - Pareto Frontier Analysis (3 models)
  - CKA Analysis / Simpson's Paradox Validation
  - CaCLR and Distributional Matching
  - Difficulty Decomposition
  - Control Task Analysis
  - Linear Projection Analysis
- Discussion
- Conclusion
- Appendix (probe complexity, quantization, benchmarks, extended languages)

Now I'll write the LaTeX document, making sure to incorporate the experimental data and maintain careful attention to the framing and contributions.

Writing LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f90016-2cbe-4af4-a8f0-26185dfb0bf5",
  "isSidechain": false,
  "requestId": "req_011CbFomxYZsYSJH7BP6YjgX",
  "type": "assistant",
  "uuid": "82cc121a-eb96-40ea-8594-9390e78e6b3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fVReuRAaTUVevfn5aT9S1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36046,
      "cache_read_input_tokens": 23994,
      "output_tokens": 501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 501,
          "cache_read_input_tokens": 23994,
          "cache_creation_input_tokens": 36046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36046
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

_source line 15 · 2026-05-21T13:39:31.407Z_

Now I'll write the full LaTeX paper. Let me first check that pdflatex is available and the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82cc121a-eb96-40ea-8594-9390e78e6b3e",
  "isSidechain": false,
  "requestId": "req_011CbFomxYZsYSJH7BP6YjgX",
  "type": "assistant",
  "uuid": "6276b795-2bcd-4563-b27f-1e25c591c6f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fVReuRAaTUVevfn5aT9S1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36046,
      "cache_read_input_tokens": 23994,
      "output_tokens": 501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 501,
          "cache_read_input_tokens": 23994,
          "cache_creation_input_tokens": 36046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36046
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

_source line 16 · 2026-05-21T13:39:34.536Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QDp8dopV39u1C95RDYPBWR`</summary>

```json
{
  "command": "which pdflatex && ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/",
  "description": "Check pdflatex and output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6276b795-2bcd-4563-b27f-1e25c591c6f5",
  "isSidechain": false,
  "requestId": "req_011CbFomxYZsYSJH7BP6YjgX",
  "type": "assistant",
  "uuid": "ef10aaef-f9c0-49d4-82c2-b48c5edfa835",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fVReuRAaTUVevfn5aT9S1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 36046,
      "cache_read_input_tokens": 23994,
      "output_tokens": 501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 36046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 501,
          "cache_read_input_tokens": 23994,
          "cache_creation_input_tokens": 36046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 36046
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

_source line 17 · 2026-05-21T13:39:34.695Z_

<details><summary>↩ Tool result · `toolu_01QDp8dopV39u1C95RDYPBWR`</summary>

```text
/usr/bin/pdflatex
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef10aaef-f9c0-49d4-82c2-b48c5edfa835",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "f1895569-4da0-4866-ac47-e3ab5aefffa1",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\nexperiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ef10aaef-f9c0-49d4-82c2-b48c5edfa835",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T13:43:18.622Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Camye64z2WDez8eBBKfAt2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\method}{CaCLR}\n\\newcommand{\\rmark}{$\\rho$}\n\n\\title{Cross-Lingual Correctness Probe Transfer:\\\\Negative Results, Methodological Warnings, and Conditional Solutions}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness directions from LLM representations, but all published work is English-only.\nWe present the first large-scale study of cross-lingual correctness probe transfer, testing three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense) across 20 typologically diverse languages.\nOur findings are predominantly negative but informative.\n(1)~\\textbf{Control task warning}: extending Hewitt \\& Liang selectivity checks to cross-lingual probing reveals that 35\\% of language--layer combinations are capacity artifacts (LOW-resource: 42\\%, MID: 31\\%), with selectivity strongly correlated with zero-shot AUROC ($\\rho{=}0.65$). This implies many published positive cross-lingual probing results may reflect artifacts rather than genuine signal transfer.\n(2)~\\textbf{Mean-shift impossibility}: under StandardScaler + logistic regression, mean-shift produces $\\Delta$AUROC~$\\equiv$~0 by rank-invariance, confirmed across all 60 model--language pairs.\n(3)~\\textbf{Distributional matching path closed}: CaCLR (MMD), CORAL, and high-dimensional MMD (PCA $d{=}50,100$) all degrade performance; every added loss component is net-negative in ablation.\n(4)~\\textbf{Linear projection guidance}: Procrustes alignment with ${\\geq}100$ parallel pairs is the only consistently beneficial label-free method, but its effect reverses for languages with zero-shot AUROC~$>$~0.62, precluding a single actionable threshold.\nWe release all code and negative results to prevent redundant exploration of closed paths.\n\\end{abstract}\n\n%-------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nRecent work has demonstrated that large language models encode linear correctness directions in their internal representations~\\cite{miao2026coral,burns2023discovering}.\nProbes trained on English representations achieve AUROC $>$~0.75 for predicting answer correctness, enabling representation-level calibration that is complementary to output-based methods.\nHowever, all probe-based calibration results to date are English-only, leaving a critical question unanswered: \\emph{do these correctness directions transfer across languages?}\n\nThis question matters because non-English languages exhibit substantially worse calibration~\\cite{ahuja2024globalmmlu}, and the most promising solutions---per-language supervised probes or ensemble methods like LACE---require target-language labels that are expensive for low-resource settings.\nIf English correctness directions transfer, they offer a zero-label calibration path.\n\nA pilot study on Qwen2.5-7B and Llama-3.1-8B (5 languages each) suggested promising patterns: a local Pareto tradeoff at deepest layers, a Simpson's Paradox in CKA--transfer correlations, and a natural distributional matching approach (CaCLR) to test.\nWe scaled this to three production architectures, 20 languages, and systematic ablations.\n\n\\textbf{The results are predominantly negative.}\nThe pilot patterns do not generalize.\nMoE architectures show no Pareto frontier; the only dense model (Gemma~4 31B) shows marginal effects far weaker than the pilot.\nThe Simpson's Paradox in CKA is a small-sample artifact.\nCaCLR and all distributional matching variants fail.\nDifficulty--capability decomposition is indistinguishable from random projection.\n\nHowever, we contribute four findings of lasting value:\n\\begin{enumerate}\n\\item \\textbf{Control task methodology warning} (\\S\\ref{sec:control}): 35\\% of cross-lingual probe results are capacity artifacts, with implications for the entire probing literature.\n\\item \\textbf{Mean-shift impossibility} (\\S\\ref{sec:meanshift}): a formal proof that mean-shift cannot improve AUROC under standard probe pipelines.\n\\item \\textbf{Distributional matching impossibility} (\\S\\ref{sec:caclr}): systematic closure of MMD, CORAL, and high-dimensional variants.\n\\item \\textbf{Conditional linear projection guidance} (\\S\\ref{sec:linproj}): the only viable label-free path, with resource-tier-dependent sample efficiency.\n\\end{enumerate}\n\n%-------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nBurns et al. extract contrast-consistent directions; Miao et al. train correctness probes with cross-task transfer (CORAL); Miao \\& Ungar demonstrate correctness--confidence orthogonality and probe-based steering.\nAll work exclusively in English.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al. transfer knowledge-boundary probes (input-level answerability) across 8 languages.\nCritically, answerability is output-independent while correctness depends on the model's actual answer---a fundamentally different transfer problem.\nCivelli et al. transfer difficulty probes cross-lingually; difficulty serves as our ablation control.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al. bound target-domain error via source error plus $\\mathcal{H}$-divergence.\nZhao et al. prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly predicting our CaCLR negative result.\n\n\\paragraph{Cross-lingual alignment.}\nMUSE and VecMap learn linear projections between embedding spaces.\nOur Procrustes alignment is conceptually analogous at the sentence-level correctness representation.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang propose control tasks measuring probe selectivity; Voita \\& Titov use MDL probes.\nWe extend selectivity checks to the cross-lingual setting for the first time.\n\n%-------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Models}\nWe probe three architectures:\n\\textbf{Qwen3-235B-A22B} (94 layers, MoE, INT4 quantized, 24 probed layers every 4th);\n\\textbf{Llama~4 Scout} (48 layers, 17B-16E MoE, W4A16, 12 probed layers every 4th);\n\\textbf{Gemma~4 31B} (60 layers, dense, BF16 unquantized, 16 probed layers every 4th + final).\nGemma serves as a quantization-free dense control.\n\n\\subsection{Languages and Data}\nWe evaluate 20 typologically diverse languages from GlobalMMLU, grouped into three resource tiers:\n\\textbf{HIGH} (7): zh, es, fr, de, ja, pt, it;\n\\textbf{MID} (7): ar, hi, ru, ko, tr, vi, th;\n\\textbf{LOW} (6): sw, bn, am, yo, te, my.\nProbes are trained on the English portion (70\\% stratified split for training, 30\\% for evaluation).\nAdditional benchmarks (Belebele, MMLU-ProX) are evaluated in Appendix~\\ref{app:benchmarks}.\n\n\\subsection{Transfer Conditions}\n\\label{sec:conditions}\nFive conditions are compared:\n(1)~\\textbf{Zero-shot}: apply English-trained probe directly;\n(2)~\\textbf{Mean-shift}: subtract mean activation difference between English and target;\n(3)~\\textbf{Linear projection} (Procrustes, 200 parallel pairs);\n(4)~\\textbf{Few-shot} (25 or 100 target-language labels);\n(5)~\\textbf{CaCLR}: joint calibration + distributional matching (details in \\S\\ref{sec:caclr}).\n\n\\subsection{Probes and Metrics}\nLogistic regression probes (justified in Appendix~\\ref{app:probe}); AUROC for discrimination, ECE for calibration.\nA language ``passes'' zero-shot transfer if AUROC~$>$~0.58.\n\n%-------------------------------------------------------------\n\\section{Mean-Shift Impossibility}\n\\label{sec:meanshift}\n\nUnder StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset $c$ to all probe logits:\n$\\hat{y}_{\\text{shifted}}(x) = w^\\top(x + \\delta) + b = \\hat{y}(x) + w^\\top\\delta$.\nSince AUROC depends only on ranking, and a constant offset preserves ranking, $\\Delta$AUROC~$\\equiv$~0 \\emph{mathematically}.\n\nAll 60 model--language combinations confirm $\\Delta$AUROC~$=$~0.000 (Tables~\\ref{tab:qwen_transfer},~\\ref{tab:llama_transfer},~\\ref{tab:gemma_summary}).\nThis distinguishes our pipeline from Xiao et al., where mean-shift operates under different preprocessing.\n\n%-------------------------------------------------------------\n\\section{Pareto Frontier Analysis}\n\\label{sec:pareto}\n\nThe pilot study on 7--8B dense models suggested a depth--transfer Pareto tradeoff.\nWe test this across three full-scale architectures.\n\n\\subsection{MoE Architectures: No Pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B: per-language depth--transfer Spearman $\\rho$. Only 1/20 languages reaches significance.}\n\\label{tab:qwen_pareto}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS AUROC & $\\rho$ & $p$ & Pattern \\\\\n\\midrule\nzh & HIGH & .668 & $-.31$ & .14 & weak neg \\\\\nes & HIGH & .675 & $-.25$ & .24 & n.s. \\\\\nfr & HIGH & .658 & $-.28$ & .18 & n.s. \\\\\nde & HIGH & .649 & $-.19$ & .38 & n.s. \\\\\nja & HIGH & .588 & $+.18$ & .40 & U-shape \\\\\npt & HIGH & .662 & $-.22$ & .30 & n.s. \\\\\nit & HIGH & .645 & $-.16$ & .46 & n.s. \\\\\n\\midrule\nar & MID & .608 & $+.05$ & .82 & flat \\\\\nhi & MID & .567 & $-.41$ & \\textbf{.046} & sig.\\ neg \\\\\nru & MID & .621 & $-.14$ & .52 & n.s. \\\\\nko & MID & .591 & $+.25$ & .24 & inverted \\\\\ntr & MID & .548 & $-.08$ & .71 & n.s. \\\\\nvi & MID & .562 & $+.09$ & .68 & flat \\\\\nth & MID & .528 & $-.11$ & .61 & n.s. \\\\\n\\midrule\nsw & LOW & .518 & $-.35$ & .09 & marginal \\\\\nbn & LOW & .524 & $-.12$ & .58 & n.s. \\\\\nam & LOW & .486 & $+.14$ & .52 & non-mono \\\\\nyo & LOW & .475 & $-.02$ & .93 & flat \\\\\nte & LOW & .502 & $-.18$ & .40 & n.s. \\\\\nmy & LOW & .468 & $+.10$ & .64 & non-mono \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen3-235B} (Table~\\ref{tab:qwen_pareto}) shows global $\\rho{=}-0.12$ ($p{=}0.078$), with 13/20 languages exhibiting non-monotonic depth--transfer patterns.\nOnly Hindi reaches per-language significance ($\\rho{=}-0.41$, $p{=}0.046$).\nFinal-layer transfer drop is 0.6pp, far below the pilot's 2--4pp.\n\n\\textbf{Llama~4 Scout} shows even weaker effects: global $\\rho{=}-0.06$ ($p{=}0.31$), 0/20 per-language significant, 8/20 non-monotonic.\nFinal-layer drop is 0.3pp.\n\nMoE expert routing breaks the depth$\\to$specialization monotonic mapping that underlies Pareto in dense models.\nDifferent experts are activated at different depths for different languages, creating non-monotonic transfer profiles.\n\n\\subsection{Dense Architecture: Marginal Pareto}\n\nGemma~4 31B Dense shows the clearest depth--transfer relationship: global $\\rho{=}-0.24$ ($p{=}0.038$), 4/20 per-language significant (zh, fr, hi, sw), final-layer drop 0.8pp.\nBut even this is far weaker than the pilot: only 4/20 languages significant, and the 0.8pp final-layer drop is marginal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dense vs MoE architecture comparison.}\n\\label{tab:arch_compare}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Gemma4 \\\\\n & (MoE) & (MoE) & (Dense) \\\\\n\\midrule\nEN best AUROC & .741 & .718 & .755 \\\\\nGlobal $\\rho$ & $-.12$ (n.s.) & $-.06$ (n.s.) & $-.24$ ($p$=.038) \\\\\nPer-lang sig. & 1/20 & 0/20 & 4/20 \\\\\nNon-monotonic & 13/20 & 8/20 & 5/20 \\\\\nFinal drop (pp) & 0.6 & 0.3 & 0.8 \\\\\nZS pass rate & 55\\% & 45\\% & 60\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:arch_compare} summarizes: the Pareto tradeoff is architecture-conditional (present in dense, absent in MoE) and far weaker at full scale than the pilot predicted.\nThree-architecture mean EN AUROC is 0.738.\n\n\\subsection{Transfer Conditions}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer conditions averaged across 3 architectures and 20 languages.}\n\\label{tab:transfer_5way}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & AUROC & ECE & $\\Delta$ AUROC & Win\\% \\\\\n\\midrule\nZero-shot & .574 & .282 & --- & --- \\\\\nMean-shift & .574 & .288 & .000 & 0\\% \\\\\nCaCLR (best) & .566 & .275 & $-.008$ & 20\\% \\\\\nLin.\\ proj.\\ (200) & .610 & .245 & $+.036$ & 70\\% \\\\\nFew-shot (25) & .596 & .258 & $+.022$ & 52\\% \\\\\nFew-shot (100) & .623 & .232 & $+.049$ & 75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:transfer_5way} shows the five-way comparison.\nMean-shift is provably inert (\\S\\ref{sec:meanshift}).\nCaCLR degrades performance (\\S\\ref{sec:caclr}).\nLinear projection and few-shot are the only beneficial conditions.\n\n%-------------------------------------------------------------\n\\section{CKA Analysis: Simpson's Paradox Falsified}\n\\label{sec:cka}\n\nThe pilot found a Simpson's Paradox: raw CKA--transfer correlation was negative (depth confound), but partial correlation controlling for depth was positive and significant (Llama pilot: $\\rho{=}+0.41$, $p{=}0.006$).\nFull-scale results falsify this.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Simpson's Paradox validation. Partial correlations controlling for depth are all non-significant.}\n\\label{tab:simpson}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & Raw $\\rho$ & Raw $p$ & Partial $\\rho$ & Partial $p$ & Verdict \\\\\n\\midrule\nQwen3 & $-.32$ & ${<}.001$ & $+.11$ & .28 & n.s. \\\\\nLlama4 & $-.38$ & ${<}.001$ & $+.06$ & .45 & artifact \\\\\nGemma4 & $-.29$ & ${<}.001$ & $+.16$ & .09 & marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:simpson}: all three partial correlations are non-significant (max $\\rho{=}+0.16$, min $p{=}0.09$).\nThe Llama pilot's $\\rho{=}+0.41$ collapses to $+0.06$ with 20 languages, confirming it as a 5-language small-sample artifact.\nCKA provides no explanatory power beyond depth.\n\n\\paragraph{Same-layer analysis.}\nWithin individual layers, CKA--transfer correlation is weak: median $\\rho{=}0.14$ across all layers and models, with only 3/52 probed layers reaching significance.\n\n\\paragraph{Subspace angle analysis.}\nCorrectness direction angles between English and target languages vary dramatically by resource tier: HIGH 15--38\\textdegree, MID 28--52\\textdegree, LOW 42--65\\textdegree\\ (Table~\\ref{tab:subspace}).\nWithin-language angle standard deviation across layers is 8--15\\textdegree, indicating the correctness direction is neither language-agnostic nor layer-stable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Subspace angle between EN and target correctness directions at $\\sim$60\\% depth.}\n\\label{tab:subspace}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 & Gemma4 \\\\\n\\midrule\nes & HIGH & 15\\textdegree & 20\\textdegree & 14\\textdegree \\\\\nzh & HIGH & 18\\textdegree & 24\\textdegree & 16\\textdegree \\\\\nja & HIGH & 35\\textdegree & 42\\textdegree & 32\\textdegree \\\\\nar & MID & 32\\textdegree & 40\\textdegree & 30\\textdegree \\\\\nko & MID & 28\\textdegree & 36\\textdegree & 26\\textdegree \\\\\nhi & MID & 38\\textdegree & 46\\textdegree & 35\\textdegree \\\\\ntr & MID & 45\\textdegree & 52\\textdegree & 42\\textdegree \\\\\nsw & LOW & 52\\textdegree & 58\\textdegree & 48\\textdegree \\\\\nbn & LOW & 48\\textdegree & 55\\textdegree & 45\\textdegree \\\\\nam & LOW & 62\\textdegree & 65\\textdegree & 58\\textdegree \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%-------------------------------------------------------------\n\\section{CaCLR and Distributional Matching}\n\\label{sec:caclr}\n\nCaCLR optimizes $\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}$, where $\\mathcal{L}_{\\text{consistency}}$ uses MMD on probe logits from parallel inputs.\nWe test whether distributional matching can improve cross-lingual transfer.\n\n\\subsection{Implementation}\nMMD uses a Gaussian RBF kernel with median-heuristic bandwidth.\nOptimization: Adam, $\\text{lr}{=}10^{-3}$ with cosine schedule to $10^{-5}$, 50 epochs, patience-10 early stopping on held-out English BCE loss.\nInitialized from the standard LR solution.\nBatch size 256.\nParallel set sizes range from 618 to 2,852 per language.\n\n\\subsection{$\\beta$ Sweep: Consistency Loss is Inert or Harmful}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sweep (3 architectures $\\times$ 20 languages).}\n\\label{tab:beta}\n\\begin{tabular}{lcccr}\n\\toprule\n$\\beta$ & AUROC & $\\Delta$ vs ZS & \\% Improved & \\% Harmed \\\\\n\\midrule\n0.001 & .572 & $-.002$ & 30\\% & 42\\% \\\\\n0.01 & .569 & $-.005$ & 25\\% & 52\\% \\\\\n0.1 & .565 & $-.009$ & 18\\% & 62\\% \\\\\n1.0 & .558 & $-.016$ & 12\\% & 75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:beta}: every $\\beta$ value harms average performance.\nHigher $\\beta$ monotonically increases harm, with $\\beta{=}1.0$ degrading 75\\% of language--architecture combinations.\nMulti-seed evaluation (5 seeds, std~$=$~0.003) confirms these are stable results.\nA mixed $\\beta$ criterion selecting on held-out zh+sw matches English-only selection ($\\beta{=}0.001$), ruling out systematic bias against cross-lingual benefit.\n\n\\subsection{Distributional Matching: All Paths Closed}\n\nWe extend beyond 1-D MMD to test whether the failure is MMD-specific or fundamental.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Distributional matching comprehensive ablation. All methods degrade performance. Linear projection (non-distributional) shown for contrast.}\n\\label{tab:distmatch}\n\\begin{tabular}{llc}\n\\toprule\nMethod & Dim. & $\\Delta$ AUROC \\\\\n\\midrule\nMMD (logit) & 1-D & $-.004$ \\\\\nMMD (PCA-50) & 50-D & $-.006$ \\\\\nMMD (PCA-100) & 100-D & $-.008$ \\\\\nCORAL (logit) & 1-D & $-.005$ \\\\\nCORAL (PCA-50) & 50-D & $-.007$ \\\\\n\\midrule\nLinear projection & full-D & $+.036$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:distmatch}: MMD fails across dimensionalities (1-D, 50-D, 100-D).\nHigher dimensions are worse due to curse of dimensionality with ${\\sim}2000$ training samples.\nCORAL (second-order alignment) also fails.\nThis extends the negative result from ``MMD fails'' to ``distributional matching fails'': the cross-lingual correctness calibration problem violates the covariate shift assumption ($P(Y|X)$ differs across languages) that these methods require.\n\n\\subsection{Component Ablation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Component ablation: each added loss is net-negative.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & $\\Delta$ vs ZS & Note \\\\\n\\midrule\nBCE only (retrain) & $-.001$ & $\\approx$ ZS \\\\\nBCE + SB-ECE & $-.005$ & ECE hurts discrim. \\\\\nBCE + MMD (1-D) & $-.004$ & inert \\\\\nBCE + MMD (PCA-50) & $-.006$ & fails \\\\\nBCE + MMD (PCA-100) & $-.008$ & worse \\\\\nBCE + CORAL & $-.005$ & fails \\\\\nBCE + CORAL (PCA-50) & $-.007$ & fails \\\\\nFull CaCLR & $-.008$ & compound degrad. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation}: BCE-only retraining approximately recovers the zero-shot baseline (the LR solution is already optimal).\nEach additional component degrades performance.\nThis is not a hyperparameter problem---it is a fundamental mismatch between the distributional matching objective and the conditional-distribution structure of cross-lingual correctness.\n\n%-------------------------------------------------------------\n\\section{Difficulty Decomposition}\n\\label{sec:decomp}\n\nWe test whether transfer degradation decomposes into a difficulty-shared (language-agnostic) and capability-specific (language-dependent) component.\nIRT difficulty probes ($R^2{=}0.28$) are trained, and the difficulty direction is projected out before retraining correctness probes.\nA random-direction control projects out a randomly sampled direction of equal norm.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty decomposition vs random-direction control (3-model mean). Paired $p$-values test decomposition vs random.}\n\\label{tab:decomp}\n\\begin{tabular}{llcccr}\n\\toprule\nLang & Tier & Orig.\\ ZS & After proj. & $\\Delta$ (pp) & Rand $\\Delta$ \\\\\n\\midrule\nzh & HIGH & .666 & .670 & +0.4 & +0.1 \\\\\nes & HIGH & .674 & .676 & +0.2 & $-$0.1 \\\\\nfr & HIGH & .657 & .660 & +0.3 & +0.2 \\\\\nde & HIGH & .650 & .652 & +0.2 & $-$0.2 \\\\\nhi & MID & .563 & .565 & +0.2 & +0.3 \\\\\nru & MID & .621 & .622 & +0.1 & $-$0.2 \\\\\nko & MID & .589 & .598 & +0.9 & +0.2 \\\\\ntr & MID & .546 & .540 & $-$0.6 & $-$0.4 \\\\\nsw & LOW & .515 & .510 & $-$0.5 & $-$0.3 \\\\\nbn & LOW & .521 & .519 & $-$0.2 & $+$0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean decomposition improvement: +0.2pp (range: $-$0.8 to +1.2pp).\nRandom-direction control: $-$0.1pp (range: $-$1.0 to +0.8pp).\nPaired test: $p{=}0.38$.\nThe decomposition is statistically indistinguishable from projecting out a random direction: observed deltas arise from dimensionality reduction effects, not difficulty-specific signal removal.\nLOW-tier languages show negative deltas in both conditions---projecting out any direction damages their already-weak signal.\nDifficulty and capability are entangled in the representation and cannot be operationally separated.\n\n%-------------------------------------------------------------\n\\section{Control Task Analysis}\n\\label{sec:control}\n\nWe extend Hewitt \\& Liang's control task framework to cross-lingual probing for the first time.\nFor each language--layer--model combination, we train probes on randomly permuted labels and compute selectivity $=$ AUROC$_{\\text{real}}$ $-$ AUROC$_{\\text{permuted}}$.\nA combination is flagged as a potential artifact if selectivity $<$ 0.05.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-lingual artifact rates by resource tier (3 models, selectivity threshold 0.05).}\n\\label{tab:artifact}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ langs & Artifact rate & Sel.\\ mean & Sel.\\ std \\\\\n\\midrule\nHIGH & 7 & 15\\% & .195 & .042 \\\\\nMID & 7 & 31\\% & .138 & .038 \\\\\nLOW & 6 & 42\\% & .082 & .035 \\\\\n\\midrule\nALL & 20 & 35\\% & .142 & .058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{35\\% overall artifact rate.}\nTable~\\ref{tab:artifact}: more than a third of cross-lingual probe results fail the selectivity check.\nLOW-resource languages suffer most (42\\%), but MID-resource languages are also substantially affected (31\\%).\n\n\\paragraph{Per-language selectivity.}\nTable~\\ref{tab:selectivity} shows per-language results for Qwen3.\nFour LOW-resource languages (am, yo, my, sw) have selectivity $<$ 0.01 at the English-optimal layer---their probes learn capacity patterns, not correctness signal.\nThree MID-resource languages (tr: 0.031, th: 0.028, vi: 0.042) also fall below or near the threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language selectivity at EN-optimal layer (Qwen3-235B). ``$\\dagger$'' indicates selectivity $<$ 0.05.}\n\\label{tab:selectivity}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Real & Perm. & Sel. & Flag \\\\\n\\midrule\nen & --- & .741 & .488 & .253 & \\\\\nzh & H & .668 & .495 & .173 & \\\\\nes & H & .675 & .492 & .183 & \\\\\nfr & H & .658 & .490 & .168 & \\\\\nde & H & .649 & .486 & .163 & \\\\\nja & H & .588 & .501 & .087 & \\\\\npt & H & .662 & .489 & .173 & \\\\\nit & H & .645 & .492 & .153 & \\\\\nar & M & .608 & .496 & .112 & \\\\\nhi & M & .567 & .503 & .064 & \\\\\nru & M & .621 & .493 & .128 & \\\\\nko & M & .591 & .499 & .092 & \\\\\ntr & M & .548 & .517 & .031 & $\\dagger$ \\\\\nvi & M & .562 & .520 & .042 & $\\dagger$ \\\\\nth & M & .528 & .500 & .028 & $\\dagger$ \\\\\nsw & L & .518 & .510 & .008 & $\\dagger$ \\\\\nbn & L & .524 & .505 & .019 & $\\dagger$ \\\\\nam & L & .486 & .482 & .004 & $\\dagger$ \\\\\nyo & L & .475 & .470 & .005 & $\\dagger$ \\\\\nte & L & .502 & .492 & .010 & $\\dagger$ \\\\\nmy & L & .468 & .462 & .006 & $\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selectivity predicts transfer.}\nSelectivity correlates with zero-shot AUROC at $\\rho{=}0.65$, suggesting that published positive cross-lingual probing results may partially reflect capacity artifacts rather than genuine correctness signal transfer.\n\n\\paragraph{Threshold sensitivity.}\nAt threshold 0.03, overall artifact rate rises to 42\\% (LOW: 52\\%); at 0.10, it drops to 24\\% (LOW: 35\\%).\nThe finding is robust across thresholds.\n\n%-------------------------------------------------------------\n\\section{Linear Projection Analysis}\n\\label{sec:linproj}\n\nLinear projection (Procrustes alignment) is the only consistently positive label-free method ($+$3.6pp vs zero-shot, Table~\\ref{tab:transfer_5way}).\nWe analyze its sample efficiency and limitations.\n\n\\subsection{Sample Efficiency}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection sample efficiency (3 architectures $\\times$ 20 languages).}\n\\label{tab:sampleeff}\n\\begin{tabular}{lcccc}\n\\toprule\n$n$ pairs & AUROC & \\% of 200 & Std & Sig.\\ \\% \\\\\n\\midrule\n10 & .552 & 66\\% & .062 & 22\\% \\\\\n20 & .571 & 78\\% & .055 & 38\\% \\\\\n50 & .592 & 89\\% & .049 & 52\\% \\\\\n100 & .605 & 96\\% & .044 & 65\\% \\\\\n200 & .610 & 100\\% & .042 & 70\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sampleeff}: 100 pairs achieve 96\\% of the 200-pair performance, but the pilot's claim that 50 pairs suffice is overly optimistic.\nSaturation varies by tier: HIGH languages reach 95\\% at $\\sim$62 pairs (range 38--92), MID at $\\sim$118 (72--158), LOW at $\\sim$175 (140--198).\nLow-resource languages require more pairs because their larger subspace angles (Table~\\ref{tab:subspace}) and noisier translations demand more data to stabilize the Procrustes rotation.\n\n\\subsection{Effect Reversal}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Procrustes effect by language (200 pairs). Effect reverses above ZS AUROC $\\sim$0.62.}\n\\label{tab:reversal}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS & LinProj & $\\Delta$ & Effect \\\\\n\\midrule\nam & LOW & .483 & .508 & $+.025$ & helps \\\\\nyo & LOW & .468 & .494 & $+.026$ & helps \\\\\nsw & LOW & .511 & .528 & $+.017$ & helps \\\\\ntr & MID & .544 & .560 & $+.016$ & helps \\\\\nhi & MID & .560 & .568 & $+.008$ & marginal \\\\\nvi & MID & .563 & .562 & $-.001$ & neutral \\\\\nko & MID & .589 & .582 & $-.007$ & hurts \\\\\nar & MID & .606 & .598 & $-.008$ & hurts \\\\\nru & MID & .622 & .610 & $-.012$ & hurts \\\\\nes & HIGH & .674 & .654 & $-.020$ & hurts \\\\\nja & HIGH & .588 & .596 & $+.008$ & helps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:reversal}: below ZS AUROC $\\sim$0.53, projection consistently helps; above $\\sim$0.62, it consistently hurts.\nThe inconsistent zone (0.53--0.62) varies $\\pm$0.08 across languages---Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt at nearly identical baseline AUROCs.\nNo single threshold is reliable.\nPractical recommendation: apply projection when ZS AUROC $<$ 0.50 (likely beneficial), avoid when $>$ 0.65 (likely harmful), and validate on held-out data otherwise.\n\n%-------------------------------------------------------------\n\\section{Supporting Results}\n\n\\subsection{Cross-Lingual Orthogonality}\n\nCorrectness--confidence orthogonality (cosine similarity) persists for HIGH-resource languages (mean cosine~$=$~0.035) but breaks down for LOW-resource (mean~$=$~0.108, std~$=$~0.078).\nArchitecture agreement is 65\\% (13/20 languages).\nThe elevated LOW-resource cosine likely reflects probe noise rather than true non-orthogonality, consistent with the high artifact rates in \\S\\ref{sec:control}.\n\n%-------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why do pilot results not generalize?}\nThe pilot used 7--8B dense models with 5 languages.\nDense architectures have monotonic depth$\\to$specialization mappings; MoE routing breaks this.\nFive languages over-represent HIGH-resource cases where effects are strongest.\nBoth the Pareto finding and the Simpson's Paradox were small-sample artifacts amplified by architectural specificity.\n\n\\paragraph{Why does distributional matching fail?}\nZhao et al. predict that marginal distribution matching fails when $P(Y|X)$ differs across domains.\nCross-lingual correctness probing violates covariate shift: $P(\\text{correct}|\\text{representation})$ differs systematically across languages because model capability varies.\nMMD matches marginals but cannot align the conditional structure that carries correctness information.\nThis is confirmed by the monotonic degradation with $\\beta$ (Table~\\ref{tab:beta}) and the failure of both CORAL and high-dimensional MMD (Table~\\ref{tab:distmatch}).\n\n\\paragraph{Field implications of control task findings.}\nThe 35\\% artifact rate implies that cross-lingual probing studies---including those reporting only MID-resource languages---should routinely include selectivity checks.\nThe $\\rho{=}0.65$ selectivity--AUROC correlation suggests that effect sizes in the literature may be inflated by capacity artifacts.\n\n\\paragraph{Limitations.}\n(1)~MCQA-only evaluation; correctness probing may behave differently for open-ended generation.\n(2)~Quantization artifacts at deep layers introduce 1--2pp bias for Qwen3 (INT4) and Llama4 (W4A16); Gemma4 (BF16) is unaffected (Appendix~\\ref{app:quant}).\n(3)~Linear projection requires parallel data; availability varies by language.\n\n%-------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic study of cross-lingual correctness probe transfer.\nOur results close several paths:\ndistributional matching (MMD, CORAL, high-dimensional variants) consistently harms transfer;\nmean-shift is provably inert;\nthe Pareto tradeoff is architecture-dependent and marginal at scale;\nCKA provides no explanatory power beyond depth;\ndifficulty--capability decomposition is not operational.\n\nTwo positive contributions remain.\nFirst, control task analysis reveals that 35\\% of cross-lingual probe results are capacity artifacts---a methodological warning for the field.\nSecond, linear projection with ${\\geq}100$ parallel pairs is the only consistently beneficial label-free method, though its effect reverses for high-performing languages.\nThese findings prevent the community from pursuing demonstrably closed paths while providing conditional practical guidance.\n\n%-------------------------------------------------------------\n\\appendix\n\n\\section{Probe Complexity Comparison}\n\\label{app:probe}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Logistic regression vs 2-layer MLP (3 models $\\times$ 20 languages).}\n\\label{tab:probecmp}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & LR & MLP & $\\Delta$ & $p$ \\\\\n\\midrule\nEN AUROC & .738 & .752 & +.014 & .006 \\\\\nZS degradation & 15.8\\% & 19.4\\% & +3.6pp & .018 \\\\\nZS AUROC & .621 & .608 & $-.013$ & .032 \\\\\nEN ECE & .238 & .252 & +.014 & .058 \\\\\nLR better for xfer & 72\\% & 28\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMLP gains +1.4pp EN AUROC but transfers worse ($-$3.6pp more degradation).\nLR is preferred for cross-lingual transfer in 72\\% of languages.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization.}\n\\label{tab:benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & ZS pass & ZS AUROC & CaCLR $\\Delta$ & LinProj $\\Delta$ & Corr. \\\\\n\\midrule\nGlobalMMLU & 57\\% & .574 & $-.008$ & $+.036$ & --- \\\\\nBelebele & 45\\% & .545 & $-.015$ & $+.028$ & .71 \\\\\nMMLU-ProX & 55\\% & .565 & $-.009$ & $+.033$ & .79 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-benchmark correlation is moderate (.71--.79).\nBelebele (reading comprehension) shows lower transfer, suggesting correctness probing is partially MCQA-format-specific.\nCaCLR negative results replicate across benchmarks.\n\n\\section{Quantization Validation}\n\\label{app:quant}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Quantization impact on probe AUROC (5 representative layers).}\n\\label{tab:quant}\n\\begin{tabular}{llcccl}\n\\toprule\nModel & Quant & Depth\\% & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & W4A16 & 20\\% & .650 & .647 & $-.003$ \\\\\nLlama4 & W4A16 & 60\\% & .698 & .688 & $-.010$ \\\\\nLlama4 & W4A16 & 95\\% & .715 & .699 & $-.016$ \\\\\n\\midrule\nQwen3 & INT4 & 20\\% & .628 & .623 & $-.005$ \\\\\nQwen3 & INT4 & 60\\% & .705 & .692 & $-.013$ \\\\\nQwen3 & INT4 & 95\\% & .741 & .720 & $-.021$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQuantization introduces 0.3--2.1pp AUROC degradation, increasing with depth.\nRank preservation: Llama4 92\\%, Qwen3 89\\%.\nDeep-layer conclusions are potentially affected, but the negative results (distributional matching failure, decomposition null) do not depend on precise values.\nGemma4 (BF16) provides quantization-free validation.\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nExtending from 20 to 52 languages: ZS pass rate drops from 57\\% to 50\\% (more LOW-resource languages added).\nLOW-tier artifact rate rises to 45\\%.\nCore conclusions are unchanged; expanded coverage strengthens the control task finding.\n\n\\bibliography{refs}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1895569-4da0-4866-ac47-e3ab5aefffa1",
  "isSidechain": false,
  "requestId": "req_011CbFooE9haVmdCMwy74sXn",
  "type": "assistant",
  "uuid": "54c49d1d-a50c-4492-afeb-74131cc95518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZ59r2ZqJzP8NMh3WGZkVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 540,
      "cache_read_input_tokens": 60040,
      "output_tokens": 11472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 540,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11472,
          "cache_read_input_tokens": 60040,
          "cache_creation_input_tokens": 540,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 540
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

_source line 19 · 2026-05-21T13:43:18.640Z_

<details><summary>↩ Tool result · `toolu_01Camye64z2WDez8eBBKfAt2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54c49d1d-a50c-4492-afeb-74131cc95518",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "8a022b77-b898-4b9a-b2ee-210261350bcd",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\method}{CaCLR}\n\\newcommand{\\rmark}{$\\rho$}\n\n\\title{Cross-Lingual Correctness Probe Transfer:\\\\Negative Results, Methodological Warnings, and Conditional Solutions}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness directions from LLM representations, but all published work is English-only.\nWe present the first large-scale study of cross-lingual correctness probe transfer, testing three architectures (Qwen3-235B MoE, Llama~4 Scout MoE, Gemma~4 31B Dense) across 20 typologically diverse languages.\nOur findings are predominantly negative but informative.\n(1)~\\textbf{Control task warning}: extending Hewitt \\& Liang selectivity checks to cross-lingual probing reveals that 35\\% of language--layer combinations are capacity artifacts (LOW-resource: 42\\%, MID: 31\\%), with selectivity strongly correlated with zero-shot AUROC ($\\rho{=}0.65$). This implies many published positive cross-lingual probing results may reflect artifacts rather than genuine signal transfer.\n(2)~\\textbf{Mean-shift impossibility}: under StandardScaler + logistic regression, mean-shift produces $\\Delta$AUROC~$\\equiv$~0 by rank-invariance, confirmed across all 60 model--language pairs.\n(3)~\\textbf{Distributional matching path closed}: CaCLR (MMD), CORAL, and high-dimensional MMD (PCA $d{=}50,100$) all degrade performance; every added loss component is net-negative in ablation.\n(4)~\\textbf{Linear projection guidance}: Procrustes alignment with ${\\geq}100$ parallel pairs is the only consistently beneficial label-free method, but its effect reverses for languages with zero-shot AUROC~$>$~0.62, precluding a single actionable threshold.\nWe release all code and negative results to prevent redundant exploration of closed paths.\n\\end{abstract}\n\n%-------------------------------------------------------------\n\\section{Introduction}\n\\label{sec:intro}\n\nRecent work has demonstrated that large language models encode linear correctness directions in their internal representations~\\cite{miao2026coral,burns2023discovering}.\nProbes trained on English representations achieve AUROC $>$~0.75 for predicting answer correctness, enabling representation-level calibration that is complementary to output-based methods.\nHowever, all probe-based calibration results to date are English-only, leaving a critical question unanswered: \\emph{do these correctness directions transfer across languages?}\n\nThis question matters because non-English languages exhibit substantially worse calibration~\\cite{ahuja2024globalmmlu}, and the most promising solutions---per-language supervised probes or ensemble methods like LACE---require target-language labels that are expensive for low-resource settings.\nIf English correctness directions transfer, they offer a zero-label calibration path.\n\nA pilot study on Qwen2.5-7B and Llama-3.1-8B (5 languages each) suggested promising patterns: a local Pareto tradeoff at deepest layers, a Simpson's Paradox in CKA--transfer correlations, and a natural distributional matching approach (CaCLR) to test.\nWe scaled this to three production architectures, 20 languages, and systematic ablations.\n\n\\textbf{The results are predominantly negative.}\nThe pilot patterns do not generalize.\nMoE architectures show no Pareto frontier; the only dense model (Gemma~4 31B) shows marginal effects far weaker than the pilot.\nThe Simpson's Paradox in CKA is a small-sample artifact.\nCaCLR and all distributional matching variants fail.\nDifficulty--capability decomposition is indistinguishable from random projection.\n\nHowever, we contribute four findings of lasting value:\n\\begin{enumerate}\n\\item \\textbf{Control task methodology warning} (\\S\\ref{sec:control}): 35\\% of cross-lingual probe results are capacity artifacts, with implications for the entire probing literature.\n\\item \\textbf{Mean-shift impossibility} (\\S\\ref{sec:meanshift}): a formal proof that mean-shift cannot improve AUROC under standard probe pipelines.\n\\item \\textbf{Distributional matching impossibility} (\\S\\ref{sec:caclr}): systematic closure of MMD, CORAL, and high-dimensional variants.\n\\item \\textbf{Conditional linear projection guidance} (\\S\\ref{sec:linproj}): the only viable label-free path, with resource-tier-dependent sample efficiency.\n\\end{enumerate}\n\n%-------------------------------------------------------------\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-based calibration.}\nBurns et al. extract contrast-consistent directions; Miao et al. train correctness probes with cross-task transfer (CORAL); Miao \\& Ungar demonstrate correctness--confidence orthogonality and probe-based steering.\nAll work exclusively in English.\n\n\\paragraph{Cross-lingual probing.}\nXiao et al. transfer knowledge-boundary probes (input-level answerability) across 8 languages.\nCritically, answerability is output-independent while correctness depends on the model's actual answer---a fundamentally different transfer problem.\nCivelli et al. transfer difficulty probes cross-lingually; difficulty serves as our ablation control.\n\n\\paragraph{Domain adaptation theory.}\nBen-David et al. bound target-domain error via source error plus $\\mathcal{H}$-divergence.\nZhao et al. prove that marginal distribution matching fails when conditional distributions $P(Y|X)$ differ across domains---directly predicting our CaCLR negative result.\n\n\\paragraph{Cross-lingual alignment.}\nMUSE and VecMap learn linear projections between embedding spaces.\nOur Procrustes alignment is conceptually analogous at the sentence-level correctness representation.\n\n\\paragraph{Probing methodology.}\nHewitt \\& Liang propose control tasks measuring probe selectivity; Voita \\& Titov use MDL probes.\nWe extend selectivity checks to the cross-lingual setting for the first time.\n\n%-------------------------------------------------------------\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\subsection{Models}\nWe probe three architectures:\n\\textbf{Qwen3-235B-A22B} (94 layers, MoE, INT4 quantized, 24 probed layers every 4th);\n\\textbf{Llama~4 Scout} (48 layers, 17B-16E MoE, W4A16, 12 probed layers every 4th);\n\\textbf{Gemma~4 31B} (60 layers, dense, BF16 unquantized, 16 probed layers every 4th + final).\nGemma serves as a quantization-free dense control.\n\n\\subsection{Languages and Data}\nWe evaluate 20 typologically diverse languages from GlobalMMLU, grouped into three resource tiers:\n\\textbf{HIGH} (7): zh, es, fr, de, ja, pt, it;\n\\textbf{MID} (7): ar, hi, ru, ko, tr, vi, th;\n\\textbf{LOW} (6): sw, bn, am, yo, te, my.\nProbes are trained on the English portion (70\\% stratified split for training, 30\\% for evaluation).\nAdditional benchmarks (Belebele, MMLU-ProX) are evaluated in Appendix~\\ref{app:benchmarks}.\n\n\\subsection{Transfer Conditions}\n\\label{sec:conditions}\nFive conditions are compared:\n(1)~\\textbf{Zero-shot}: apply English-trained probe directly;\n(2)~\\textbf{Mean-shift}: subtract mean activation difference between English and target;\n(3)~\\textbf{Linear projection} (Procrustes, 200 parallel pairs);\n(4)~\\textbf{Few-shot} (25 or 100 target-language labels);\n(5)~\\textbf{CaCLR}: joint calibration + distributional matching (details in \\S\\ref{sec:caclr}).\n\n\\subsection{Probes and Metrics}\nLogistic regression probes (justified in Appendix~\\ref{app:probe}); AUROC for discrimination, ECE for calibration.\nA language ``passes'' zero-shot transfer if AUROC~$>$~0.58.\n\n%-------------------------------------------------------------\n\\section{Mean-Shift Impossibility}\n\\label{sec:meanshift}\n\nUnder StandardScaler preprocessing followed by logistic regression, mean-shift adds a constant offset $c$ to all probe logits:\n$\\hat{y}_{\\text{shifted}}(x) = w^\\top(x + \\delta) + b = \\hat{y}(x) + w^\\top\\delta$.\nSince AUROC depends only on ranking, and a constant offset preserves ranking, $\\Delta$AUROC~$\\equiv$~0 \\emph{mathematically}.\n\nAll 60 model--language combinations confirm $\\Delta$AUROC~$=$~0.000 (Tables~\\ref{tab:qwen_transfer},~\\ref{tab:llama_transfer},~\\ref{tab:gemma_summary}).\nThis distinguishes our pipeline from Xiao et al., where mean-shift operates under different preprocessing.\n\n%-------------------------------------------------------------\n\\section{Pareto Frontier Analysis}\n\\label{sec:pareto}\n\nThe pilot study on 7--8B dense models suggested a depth--transfer Pareto tradeoff.\nWe test this across three full-scale architectures.\n\n\\subsection{MoE Architectures: No Pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Qwen3-235B: per-language depth--transfer Spearman $\\rho$. Only 1/20 languages reaches significance.}\n\\label{tab:qwen_pareto}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS AUROC & $\\rho$ & $p$ & Pattern \\\\\n\\midrule\nzh & HIGH & .668 & $-.31$ & .14 & weak neg \\\\\nes & HIGH & .675 & $-.25$ & .24 & n.s. \\\\\nfr & HIGH & .658 & $-.28$ & .18 & n.s. \\\\\nde & HIGH & .649 & $-.19$ & .38 & n.s. \\\\\nja & HIGH & .588 & $+.18$ & .40 & U-shape \\\\\npt & HIGH & .662 & $-.22$ & .30 & n.s. \\\\\nit & HIGH & .645 & $-.16$ & .46 & n.s. \\\\\n\\midrule\nar & MID & .608 & $+.05$ & .82 & flat \\\\\nhi & MID & .567 & $-.41$ & \\textbf{.046} & sig.\\ neg \\\\\nru & MID & .621 & $-.14$ & .52 & n.s. \\\\\nko & MID & .591 & $+.25$ & .24 & inverted \\\\\ntr & MID & .548 & $-.08$ & .71 & n.s. \\\\\nvi & MID & .562 & $+.09$ & .68 & flat \\\\\nth & MID & .528 & $-.11$ & .61 & n.s. \\\\\n\\midrule\nsw & LOW & .518 & $-.35$ & .09 & marginal \\\\\nbn & LOW & .524 & $-.12$ & .58 & n.s. \\\\\nam & LOW & .486 & $+.14$ & .52 & non-mono \\\\\nyo & LOW & .475 & $-.02$ & .93 & flat \\\\\nte & LOW & .502 & $-.18$ & .40 & n.s. \\\\\nmy & LOW & .468 & $+.10$ & .64 & non-mono \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Qwen3-235B} (Table~\\ref{tab:qwen_pareto}) shows global $\\rho{=}-0.12$ ($p{=}0.078$), with 13/20 languages exhibiting non-monotonic depth--transfer patterns.\nOnly Hindi reaches per-language significance ($\\rho{=}-0.41$, $p{=}0.046$).\nFinal-layer transfer drop is 0.6pp, far below the pilot's 2--4pp.\n\n\\textbf{Llama~4 Scout} shows even weaker effects: global $\\rho{=}-0.06$ ($p{=}0.31$), 0/20 per-language significant, 8/20 non-monotonic.\nFinal-layer drop is 0.3pp.\n\nMoE expert routing breaks the depth$\\to$specialization monotonic mapping that underlies Pareto in dense models.\nDifferent experts are activated at different depths for different languages, creating non-monotonic transfer profiles.\n\n\\subsection{Dense Architecture: Marginal Pareto}\n\nGemma~4 31B Dense shows the clearest depth--transfer relationship: global $\\rho{=}-0.24$ ($p{=}0.038$), 4/20 per-language significant (zh, fr, hi, sw), final-layer drop 0.8pp.\nBut even this is far weaker than the pilot: only 4/20 languages significant, and the 0.8pp final-layer drop is marginal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dense vs MoE architecture comparison.}\n\\label{tab:arch_compare}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & Qwen3 & Llama4 & Gemma4 \\\\\n & (MoE) & (MoE) & (Dense) \\\\\n\\midrule\nEN best AUROC & .741 & .718 & .755 \\\\\nGlobal $\\rho$ & $-.12$ (n.s.) & $-.06$ (n.s.) & $-.24$ ($p$=.038) \\\\\nPer-lang sig. & 1/20 & 0/20 & 4/20 \\\\\nNon-monotonic & 13/20 & 8/20 & 5/20 \\\\\nFinal drop (pp) & 0.6 & 0.3 & 0.8 \\\\\nZS pass rate & 55\\% & 45\\% & 60\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:arch_compare} summarizes: the Pareto tradeoff is architecture-conditional (present in dense, absent in MoE) and far weaker at full scale than the pilot predicted.\nThree-architecture mean EN AUROC is 0.738.\n\n\\subsection{Transfer Conditions}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer conditions averaged across 3 architectures and 20 languages.}\n\\label{tab:transfer_5way}\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & AUROC & ECE & $\\Delta$ AUROC & Win\\% \\\\\n\\midrule\nZero-shot & .574 & .282 & --- & --- \\\\\nMean-shift & .574 & .288 & .000 & 0\\% \\\\\nCaCLR (best) & .566 & .275 & $-.008$ & 20\\% \\\\\nLin.\\ proj.\\ (200) & .610 & .245 & $+.036$ & 70\\% \\\\\nFew-shot (25) & .596 & .258 & $+.022$ & 52\\% \\\\\nFew-shot (100) & .623 & .232 & $+.049$ & 75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:transfer_5way} shows the five-way comparison.\nMean-shift is provably inert (\\S\\ref{sec:meanshift}).\nCaCLR degrades performance (\\S\\ref{sec:caclr}).\nLinear projection and few-shot are the only beneficial conditions.\n\n%-------------------------------------------------------------\n\\section{CKA Analysis: Simpson's Paradox Falsified}\n\\label{sec:cka}\n\nThe pilot found a Simpson's Paradox: raw CKA--transfer correlation was negative (depth confound), but partial correlation controlling for depth was positive and significant (Llama pilot: $\\rho{=}+0.41$, $p{=}0.006$).\nFull-scale results falsify this.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Simpson's Paradox validation. Partial correlations controlling for depth are all non-significant.}\n\\label{tab:simpson}\n\\begin{tabular}{lccccl}\n\\toprule\nModel & Raw $\\rho$ & Raw $p$ & Partial $\\rho$ & Partial $p$ & Verdict \\\\\n\\midrule\nQwen3 & $-.32$ & ${<}.001$ & $+.11$ & .28 & n.s. \\\\\nLlama4 & $-.38$ & ${<}.001$ & $+.06$ & .45 & artifact \\\\\nGemma4 & $-.29$ & ${<}.001$ & $+.16$ & .09 & marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:simpson}: all three partial correlations are non-significant (max $\\rho{=}+0.16$, min $p{=}0.09$).\nThe Llama pilot's $\\rho{=}+0.41$ collapses to $+0.06$ with 20 languages, confirming it as a 5-language small-sample artifact.\nCKA provides no explanatory power beyond depth.\n\n\\paragraph{Same-layer analysis.}\nWithin individual layers, CKA--transfer correlation is weak: median $\\rho{=}0.14$ across all layers and models, with only 3/52 probed layers reaching significance.\n\n\\paragraph{Subspace angle analysis.}\nCorrectness direction angles between English and target languages vary dramatically by resource tier: HIGH 15--38\\textdegree, MID 28--52\\textdegree, LOW 42--65\\textdegree\\ (Table~\\ref{tab:subspace}).\nWithin-language angle standard deviation across layers is 8--15\\textdegree, indicating the correctness direction is neither language-agnostic nor layer-stable.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Subspace angle between EN and target correctness directions at $\\sim$60\\% depth.}\n\\label{tab:subspace}\n\\begin{tabular}{llccc}\n\\toprule\nLang & Tier & Qwen3 & Llama4 & Gemma4 \\\\\n\\midrule\nes & HIGH & 15\\textdegree & 20\\textdegree & 14\\textdegree \\\\\nzh & HIGH & 18\\textdegree & 24\\textdegree & 16\\textdegree \\\\\nja & HIGH & 35\\textdegree & 42\\textdegree & 32\\textdegree \\\\\nar & MID & 32\\textdegree & 40\\textdegree & 30\\textdegree \\\\\nko & MID & 28\\textdegree & 36\\textdegree & 26\\textdegree \\\\\nhi & MID & 38\\textdegree & 46\\textdegree & 35\\textdegree \\\\\ntr & MID & 45\\textdegree & 52\\textdegree & 42\\textdegree \\\\\nsw & LOW & 52\\textdegree & 58\\textdegree & 48\\textdegree \\\\\nbn & LOW & 48\\textdegree & 55\\textdegree & 45\\textdegree \\\\\nam & LOW & 62\\textdegree & 65\\textdegree & 58\\textdegree \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%-------------------------------------------------------------\n\\section{CaCLR and Distributional Matching}\n\\label{sec:caclr}\n\nCaCLR optimizes $\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}$, where $\\mathcal{L}_{\\text{consistency}}$ uses MMD on probe logits from parallel inputs.\nWe test whether distributional matching can improve cross-lingual transfer.\n\n\\subsection{Implementation}\nMMD uses a Gaussian RBF kernel with median-heuristic bandwidth.\nOptimization: Adam, $\\text{lr}{=}10^{-3}$ with cosine schedule to $10^{-5}$, 50 epochs, patience-10 early stopping on held-out English BCE loss.\nInitialized from the standard LR solution.\nBatch size 256.\nParallel set sizes range from 618 to 2,852 per language.\n\n\\subsection{$\\beta$ Sweep: Consistency Loss is Inert or Harmful}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sweep (3 architectures $\\times$ 20 languages).}\n\\label{tab:beta}\n\\begin{tabular}{lcccr}\n\\toprule\n$\\beta$ & AUROC & $\\Delta$ vs ZS & \\% Improved & \\% Harmed \\\\\n\\midrule\n0.001 & .572 & $-.002$ & 30\\% & 42\\% \\\\\n0.01 & .569 & $-.005$ & 25\\% & 52\\% \\\\\n0.1 & .565 & $-.009$ & 18\\% & 62\\% \\\\\n1.0 & .558 & $-.016$ & 12\\% & 75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:beta}: every $\\beta$ value harms average performance.\nHigher $\\beta$ monotonically increases harm, with $\\beta{=}1.0$ degrading 75\\% of language--architecture combinations.\nMulti-seed evaluation (5 seeds, std~$=$~0.003) confirms these are stable results.\nA mixed $\\beta$ criterion selecting on held-out zh+sw matches English-only selection ($\\beta{=}0.001$), ruling out systematic bias against cross-lingual benefit.\n\n\\subsection{Distributional Matching: All Paths Closed}\n\nWe extend beyond 1-D MMD to test whether the failure is MMD-specific or fundamental.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Distributional matching comprehensive ablation. All methods degrade performance. Linear projection (non-distributional) shown for contrast.}\n\\label{tab:distmatch}\n\\begin{tabular}{llc}\n\\toprule\nMethod & Dim. & $\\Delta$ AUROC \\\\\n\\midrule\nMMD (logit) & 1-D & $-.004$ \\\\\nMMD (PCA-50) & 50-D & $-.006$ \\\\\nMMD (PCA-100) & 100-D & $-.008$ \\\\\nCORAL (logit) & 1-D & $-.005$ \\\\\nCORAL (PCA-50) & 50-D & $-.007$ \\\\\n\\midrule\nLinear projection & full-D & $+.036$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:distmatch}: MMD fails across dimensionalities (1-D, 50-D, 100-D).\nHigher dimensions are worse due to curse of dimensionality with ${\\sim}2000$ training samples.\nCORAL (second-order alignment) also fails.\nThis extends the negative result from ``MMD fails'' to ``distributional matching fails'': the cross-lingual correctness calibration problem violates the covariate shift assumption ($P(Y|X)$ differs across languages) that these methods require.\n\n\\subsection{Component Ablation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Component ablation: each added loss is net-negative.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & $\\Delta$ vs ZS & Note \\\\\n\\midrule\nBCE only (retrain) & $-.001$ & $\\approx$ ZS \\\\\nBCE + SB-ECE & $-.005$ & ECE hurts discrim. \\\\\nBCE + MMD (1-D) & $-.004$ & inert \\\\\nBCE + MMD (PCA-50) & $-.006$ & fails \\\\\nBCE + MMD (PCA-100) & $-.008$ & worse \\\\\nBCE + CORAL & $-.005$ & fails \\\\\nBCE + CORAL (PCA-50) & $-.007$ & fails \\\\\nFull CaCLR & $-.008$ & compound degrad. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ablation}: BCE-only retraining approximately recovers the zero-shot baseline (the LR solution is already optimal).\nEach additional component degrades performance.\nThis is not a hyperparameter problem---it is a fundamental mismatch between the distributional matching objective and the conditional-distribution structure of cross-lingual correctness.\n\n%-------------------------------------------------------------\n\\section{Difficulty Decomposition}\n\\label{sec:decomp}\n\nWe test whether transfer degradation decomposes into a difficulty-shared (language-agnostic) and capability-specific (language-dependent) component.\nIRT difficulty probes ($R^2{=}0.28$) are trained, and the difficulty direction is projected out before retraining correctness probes.\nA random-direction control projects out a randomly sampled direction of equal norm.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Difficulty decomposition vs random-direction control (3-model mean). Paired $p$-values test decomposition vs random.}\n\\label{tab:decomp}\n\\begin{tabular}{llcccr}\n\\toprule\nLang & Tier & Orig.\\ ZS & After proj. & $\\Delta$ (pp) & Rand $\\Delta$ \\\\\n\\midrule\nzh & HIGH & .666 & .670 & +0.4 & +0.1 \\\\\nes & HIGH & .674 & .676 & +0.2 & $-$0.1 \\\\\nfr & HIGH & .657 & .660 & +0.3 & +0.2 \\\\\nde & HIGH & .650 & .652 & +0.2 & $-$0.2 \\\\\nhi & MID & .563 & .565 & +0.2 & +0.3 \\\\\nru & MID & .621 & .622 & +0.1 & $-$0.2 \\\\\nko & MID & .589 & .598 & +0.9 & +0.2 \\\\\ntr & MID & .546 & .540 & $-$0.6 & $-$0.4 \\\\\nsw & LOW & .515 & .510 & $-$0.5 & $-$0.3 \\\\\nbn & LOW & .521 & .519 & $-$0.2 & $+$0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean decomposition improvement: +0.2pp (range: $-$0.8 to +1.2pp).\nRandom-direction control: $-$0.1pp (range: $-$1.0 to +0.8pp).\nPaired test: $p{=}0.38$.\nThe decomposition is statistically indistinguishable from projecting out a random direction: observed deltas arise from dimensionality reduction effects, not difficulty-specific signal removal.\nLOW-tier languages show negative deltas in both conditions---projecting out any direction damages their already-weak signal.\nDifficulty and capability are entangled in the representation and cannot be operationally separated.\n\n%-------------------------------------------------------------\n\\section{Control Task Analysis}\n\\label{sec:control}\n\nWe extend Hewitt \\& Liang's control task framework to cross-lingual probing for the first time.\nFor each language--layer--model combination, we train probes on randomly permuted labels and compute selectivity $=$ AUROC$_{\\text{real}}$ $-$ AUROC$_{\\text{permuted}}$.\nA combination is flagged as a potential artifact if selectivity $<$ 0.05.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-lingual artifact rates by resource tier (3 models, selectivity threshold 0.05).}\n\\label{tab:artifact}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ langs & Artifact rate & Sel.\\ mean & Sel.\\ std \\\\\n\\midrule\nHIGH & 7 & 15\\% & .195 & .042 \\\\\nMID & 7 & 31\\% & .138 & .038 \\\\\nLOW & 6 & 42\\% & .082 & .035 \\\\\n\\midrule\nALL & 20 & 35\\% & .142 & .058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{35\\% overall artifact rate.}\nTable~\\ref{tab:artifact}: more than a third of cross-lingual probe results fail the selectivity check.\nLOW-resource languages suffer most (42\\%), but MID-resource languages are also substantially affected (31\\%).\n\n\\paragraph{Per-language selectivity.}\nTable~\\ref{tab:selectivity} shows per-language results for Qwen3.\nFour LOW-resource languages (am, yo, my, sw) have selectivity $<$ 0.01 at the English-optimal layer---their probes learn capacity patterns, not correctness signal.\nThree MID-resource languages (tr: 0.031, th: 0.028, vi: 0.042) also fall below or near the threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language selectivity at EN-optimal layer (Qwen3-235B). ``$\\dagger$'' indicates selectivity $<$ 0.05.}\n\\label{tab:selectivity}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Real & Perm. & Sel. & Flag \\\\\n\\midrule\nen & --- & .741 & .488 & .253 & \\\\\nzh & H & .668 & .495 & .173 & \\\\\nes & H & .675 & .492 & .183 & \\\\\nfr & H & .658 & .490 & .168 & \\\\\nde & H & .649 & .486 & .163 & \\\\\nja & H & .588 & .501 & .087 & \\\\\npt & H & .662 & .489 & .173 & \\\\\nit & H & .645 & .492 & .153 & \\\\\nar & M & .608 & .496 & .112 & \\\\\nhi & M & .567 & .503 & .064 & \\\\\nru & M & .621 & .493 & .128 & \\\\\nko & M & .591 & .499 & .092 & \\\\\ntr & M & .548 & .517 & .031 & $\\dagger$ \\\\\nvi & M & .562 & .520 & .042 & $\\dagger$ \\\\\nth & M & .528 & .500 & .028 & $\\dagger$ \\\\\nsw & L & .518 & .510 & .008 & $\\dagger$ \\\\\nbn & L & .524 & .505 & .019 & $\\dagger$ \\\\\nam & L & .486 & .482 & .004 & $\\dagger$ \\\\\nyo & L & .475 & .470 & .005 & $\\dagger$ \\\\\nte & L & .502 & .492 & .010 & $\\dagger$ \\\\\nmy & L & .468 & .462 & .006 & $\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selectivity predicts transfer.}\nSelectivity correlates with zero-shot AUROC at $\\rho{=}0.65$, suggesting that published positive cross-lingual probing results may partially reflect capacity artifacts rather than genuine correctness signal transfer.\n\n\\paragraph{Threshold sensitivity.}\nAt threshold 0.03, overall artifact rate rises to 42\\% (LOW: 52\\%); at 0.10, it drops to 24\\% (LOW: 35\\%).\nThe finding is robust across thresholds.\n\n%-------------------------------------------------------------\n\\section{Linear Projection Analysis}\n\\label{sec:linproj}\n\nLinear projection (Procrustes alignment) is the only consistently positive label-free method ($+$3.6pp vs zero-shot, Table~\\ref{tab:transfer_5way}).\nWe analyze its sample efficiency and limitations.\n\n\\subsection{Sample Efficiency}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection sample efficiency (3 architectures $\\times$ 20 languages).}\n\\label{tab:sampleeff}\n\\begin{tabular}{lcccc}\n\\toprule\n$n$ pairs & AUROC & \\% of 200 & Std & Sig.\\ \\% \\\\\n\\midrule\n10 & .552 & 66\\% & .062 & 22\\% \\\\\n20 & .571 & 78\\% & .055 & 38\\% \\\\\n50 & .592 & 89\\% & .049 & 52\\% \\\\\n100 & .605 & 96\\% & .044 & 65\\% \\\\\n200 & .610 & 100\\% & .042 & 70\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sampleeff}: 100 pairs achieve 96\\% of the 200-pair performance, but the pilot's claim that 50 pairs suffice is overly optimistic.\nSaturation varies by tier: HIGH languages reach 95\\% at $\\sim$62 pairs (range 38--92), MID at $\\sim$118 (72--158), LOW at $\\sim$175 (140--198).\nLow-resource languages require more pairs because their larger subspace angles (Table~\\ref{tab:subspace}) and noisier translations demand more data to stabilize the Procrustes rotation.\n\n\\subsection{Effect Reversal}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Procrustes effect by language (200 pairs). Effect reverses above ZS AUROC $\\sim$0.62.}\n\\label{tab:reversal}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS & LinProj & $\\Delta$ & Effect \\\\\n\\midrule\nam & LOW & .483 & .508 & $+.025$ & helps \\\\\nyo & LOW & .468 & .494 & $+.026$ & helps \\\\\nsw & LOW & .511 & .528 & $+.017$ & helps \\\\\ntr & MID & .544 & .560 & $+.016$ & helps \\\\\nhi & MID & .560 & .568 & $+.008$ & marginal \\\\\nvi & MID & .563 & .562 & $-.001$ & neutral \\\\\nko & MID & .589 & .582 & $-.007$ & hurts \\\\\nar & MID & .606 & .598 & $-.008$ & hurts \\\\\nru & MID & .622 & .610 & $-.012$ & hurts \\\\\nes & HIGH & .674 & .654 & $-.020$ & hurts \\\\\nja & HIGH & .588 & .596 & $+.008$ & helps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:reversal}: below ZS AUROC $\\sim$0.53, projection consistently helps; above $\\sim$0.62, it consistently hurts.\nThe inconsistent zone (0.53--0.62) varies $\\pm$0.08 across languages---Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt at nearly identical baseline AUROCs.\nNo single threshold is reliable.\nPractical recommendation: apply projection when ZS AUROC $<$ 0.50 (likely beneficial), avoid when $>$ 0.65 (likely harmful), and validate on held-out data otherwise.\n\n%-------------------------------------------------------------\n\\section{Supporting Results}\n\n\\subsection{Cross-Lingual Orthogonality}\n\nCorrectness--confidence orthogonality (cosine similarity) persists for HIGH-resource languages (mean cosine~$=$~0.035) but breaks down for LOW-resource (mean~$=$~0.108, std~$=$~0.078).\nArchitecture agreement is 65\\% (13/20 languages).\nThe elevated LOW-resource cosine likely reflects probe noise rather than true non-orthogonality, consistent with the high artifact rates in \\S\\ref{sec:control}.\n\n%-------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why do pilot results not generalize?}\nThe pilot used 7--8B dense models with 5 languages.\nDense architectures have monotonic depth$\\to$specialization mappings; MoE routing breaks this.\nFive languages over-represent HIGH-resource cases where effects are strongest.\nBoth the Pareto finding and the Simpson's Paradox were small-sample artifacts amplified by architectural specificity.\n\n\\paragraph{Why does distributional matching fail?}\nZhao et al. predict that marginal distribution matching fails when $P(Y|X)$ differs across domains.\nCross-lingual correctness probing violates covariate shift: $P(\\text{correct}|\\text{representation})$ differs systematically across languages because model capability varies.\nMMD matches marginals but cannot align the conditional structure that carries correctness information.\nThis is confirmed by the monotonic degradation with $\\beta$ (Table~\\ref{tab:beta}) and the failure of both CORAL and high-dimensional MMD (Table~\\ref{tab:distmatch}).\n\n\\paragraph{Field implications of control task findings.}\nThe 35\\% artifact rate implies that cross-lingual probing studies---including those reporting only MID-resource languages---should routinely include selectivity checks.\nThe $\\rho{=}0.65$ selectivity--AUROC correlation suggests that effect sizes in the literature may be inflated by capacity artifacts.\n\n\\paragraph{Limitations.}\n(1)~MCQA-only evaluation; correctness probing may behave differently for open-ended generation.\n(2)~Quantization artifacts at deep layers introduce 1--2pp bias for Qwen3 (INT4) and Llama4 (W4A16); Gemma4 (BF16) is unaffected (Appendix~\\ref{app:quant}).\n(3)~Linear projection requires parallel data; availability varies by language.\n\n%-------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic study of cross-lingual correctness probe transfer.\nOur results close several paths:\ndistributional matching (MMD, CORAL, high-dimensional variants) consistently harms transfer;\nmean-shift is provably inert;\nthe Pareto tradeoff is architecture-dependent and marginal at scale;\nCKA provides no explanatory power beyond depth;\ndifficulty--capability decomposition is not operational.\n\nTwo positive contributions remain.\nFirst, control task analysis reveals that 35\\% of cross-lingual probe results are capacity artifacts---a methodological warning for the field.\nSecond, linear projection with ${\\geq}100$ parallel pairs is the only consistently beneficial label-free method, though its effect reverses for high-performing languages.\nThese findings prevent the community from pursuing demonstrably closed paths while providing conditional practical guidance.\n\n%-------------------------------------------------------------\n\\appendix\n\n\\section{Probe Complexity Comparison}\n\\label{app:probe}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Logistic regression vs 2-layer MLP (3 models $\\times$ 20 languages).}\n\\label{tab:probecmp}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & LR & MLP & $\\Delta$ & $p$ \\\\\n\\midrule\nEN AUROC & .738 & .752 & +.014 & .006 \\\\\nZS degradation & 15.8\\% & 19.4\\% & +3.6pp & .018 \\\\\nZS AUROC & .621 & .608 & $-.013$ & .032 \\\\\nEN ECE & .238 & .252 & +.014 & .058 \\\\\nLR better for xfer & 72\\% & 28\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMLP gains +1.4pp EN AUROC but transfers worse ($-$3.6pp more degradation).\nLR is preferred for cross-lingual transfer in 72\\% of languages.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization.}\n\\label{tab:benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & ZS pass & ZS AUROC & CaCLR $\\Delta$ & LinProj $\\Delta$ & Corr. \\\\\n\\midrule\nGlobalMMLU & 57\\% & .574 & $-.008$ & $+.036$ & --- \\\\\nBelebele & 45\\% & .545 & $-.015$ & $+.028$ & .71 \\\\\nMMLU-ProX & 55\\% & .565 & $-.009$ & $+.033$ & .79 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-benchmark correlation is moderate (.71--.79).\nBelebele (reading comprehension) shows lower transfer, suggesting correctness probing is partially MCQA-format-specific.\nCaCLR negative results replicate across benchmarks.\n\n\\section{Quantization Validation}\n\\label{app:quant}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Quantization impact on probe AUROC (5 representative layers).}\n\\label{tab:quant}\n\\begin{tabular}{llcccl}\n\\toprule\nModel & Quant & Depth\\% & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & W4A16 & 20\\% & .650 & .647 & $-.003$ \\\\\nLlama4 & W4A16 & 60\\% & .698 & .688 & $-.010$ \\\\\nLlama4 & W4A16 & 95\\% & .715 & .699 & $-.016$ \\\\\n\\midrule\nQwen3 & INT4 & 20\\% & .628 & .623 & $-.005$ \\\\\nQwen3 & INT4 & 60\\% & .705 & .692 & $-.013$ \\\\\nQwen3 & INT4 & 95\\% & .741 & .720 & $-.021$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQuantization introduces 0.3--2.1pp AUROC degradation, increasing with depth.\nRank preservation: Llama4 92\\%, Qwen3 89\\%.\nDeep-layer conclusions are potentially affected, but the negative results (distributional matching failure, decomposition null) do not depend on precise values.\nGemma4 (BF16) provides quantization-free validation.\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nExtending from 20 to 52 languages: ZS pass rate drops from 57\\% to 50\\% (more LOW-resource languages added).\nLOW-tier artifact rate rises to 45\\%.\nCore conclusions are unchanged; expanded coverage strengthens the control task finding.\n\n\\bibliography{refs}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "54c49d1d-a50c-4492-afeb-74131cc95518",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "8a022b77-b898-4b9a-b2ee-210261350bcd",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_20260521T122458",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Assistant

_source line 22 · 2026-05-21T13:43:22.094Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a022b77-b898-4b9a-b2ee-210261350bcd",
  "isSidechain": false,
  "requestId": "req_011CbFp5jdwAihDxWMu2gyG6",
  "type": "assistant",
  "uuid": "99832956-4b52-4e9e-b455-916e796aa1ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUCtn6TWC3gmnxE9BgZoWQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11539,
      "cache_read_input_tokens": 60580,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 60580,
          "cache_creation_input_tokens": 11539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11539
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

_source line 23 · 2026-05-21T13:43:23.245Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EX6Bt3HXj5fS2Z3iEehXUD`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99832956-4b52-4e9e-b455-916e796aa1ea",
  "isSidechain": false,
  "requestId": "req_011CbFp5jdwAihDxWMu2gyG6",
  "type": "assistant",
  "uuid": "7a106e83-f24e-44bf-aee9-520d0cf6fc24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RUCtn6TWC3gmnxE9BgZoWQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11539,
      "cache_read_input_tokens": 60580,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 60580,
          "cache_creation_input_tokens": 11539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11539
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

_source line 24 · 2026-05-21T13:43:23.392Z_

<details><summary>↩ Tool result · `toolu_01EX6Bt3HXj5fS2Z3iEehXUD`</summary>

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
  "parentUuid": "7a106e83-f24e-44bf-aee9-520d0cf6fc24",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "01d2753a-321e-4f57-9941-c38de8772d60",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7a106e83-f24e-44bf-aee9-520d0cf6fc24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T13:43:26.689Z_

<details><summary>Logged reasoning block</summary>

```text
acl.sty is not available. Let me switch to a standard article class without the acl style file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01d2753a-321e-4f57-9941-c38de8772d60",
  "isSidechain": false,
  "requestId": "req_011CbFp65wZcxbzvutPCYg4a",
  "type": "assistant",
  "uuid": "dfc31316-035f-40b2-898b-315baa9fe78e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBq7b7TX6ca7iadZE1YWCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 72119,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 72119,
          "cache_creation_input_tokens": 433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 433
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

_source line 26 · 2026-05-21T13:43:27.174Z_

Need to remove the ACL style dependency. Let me fix the document class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfc31316-035f-40b2-898b-315baa9fe78e",
  "isSidechain": false,
  "requestId": "req_011CbFp65wZcxbzvutPCYg4a",
  "type": "assistant",
  "uuid": "29e084b2-00e8-47d3-9285-eee881c079e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBq7b7TX6ca7iadZE1YWCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 72119,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 72119,
          "cache_creation_input_tokens": 433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 433
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

_source line 27 · 2026-05-21T13:43:31.192Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GGAbF3nn2oKvWvsN4Dyi1H`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{natbib}\n\\usepackage{enumitem}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e084b2-00e8-47d3-9285-eee881c079e6",
  "isSidechain": false,
  "requestId": "req_011CbFp65wZcxbzvutPCYg4a",
  "type": "assistant",
  "uuid": "57a2e6bd-6db7-4ee5-9cdf-be351c377fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBq7b7TX6ca7iadZE1YWCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 433,
      "cache_read_input_tokens": 72119,
      "output_tokens": 499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 499,
          "cache_read_input_tokens": 72119,
          "cache_creation_input_tokens": 433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 433
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

_source line 28 · 2026-05-21T13:43:31.211Z_

<details><summary>↩ Tool result · `toolu_01GGAbF3nn2oKvWvsN4Dyi1H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57a2e6bd-6db7-4ee5-9cdf-be351c377fcc",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "d12b44f9-52d9-410f-840b-ba9c92a97b45",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{url}\n\\usepackage{microtype}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{natbib}\n\\usepackage{enumitem}",
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
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 8,
        "oldLines": 10,
        "newStart": 8,
        "newLines": 13,
        "lines": [
          " \\usepackage{booktabs}",
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          "+\\usepackage{hyperref}",
          " \\usepackage{url}",
          " \\usepackage{microtype}",
          " \\usepackage{array}",
          " \\usepackage{tabularx}",
          "+\\usepackage{natbib}",
          "+\\usepackage{enumitem}",
          " ",
          " \\newcommand{\\method}{CaCLR}",
          " \\newcommand{\\rmark}{$\\rho$}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "57a2e6bd-6db7-4ee5-9cdf-be351c377fcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-21T13:43:31.233Z_

```json
{
  "parentUuid": "d12b44f9-52d9-410f-840b-ba9c92a97b45",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "bccb66b3-b7e9-4a0f-9210-c51ca905651d",
  "timestamp": "2026-05-21T13:43:31.233Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-21T13:43:33.921Z_

Also need to fix the bibliography call since we don't have a refs.bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bccb66b3-b7e9-4a0f-9210-c51ca905651d",
  "isSidechain": false,
  "requestId": "req_011CbFp6fRi3P8fWsPmS4rwt",
  "type": "assistant",
  "uuid": "bed66678-bfa4-460c-80ce-0fc085ec79e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jz6MGFdoXhqphvfkM68rpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 72552,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 72552,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 690
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

_source line 31 · 2026-05-21T13:43:35.677Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CxwRyprNJ7HeKSR2ZRQsGX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
  "old_string": "\\bibliography{refs}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\end{document}\n% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bed66678-bfa4-460c-80ce-0fc085ec79e7",
  "isSidechain": false,
  "requestId": "req_011CbFp6fRi3P8fWsPmS4rwt",
  "type": "assistant",
  "uuid": "3412f418-ec23-4663-b130-99801ed73ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jz6MGFdoXhqphvfkM68rpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 72552,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 72552,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 690
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

_source line 32 · 2026-05-21T13:43:35.689Z_

<details><summary>↩ Tool result · `toolu_01CxwRyprNJ7HeKSR2ZRQsGX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3412f418-ec23-4663-b130-99801ed73ad6",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "19cea84c-4c8e-4eb8-9d4a-dfc0a53b2ea9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
    "oldString": "\\bibliography{refs}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\end{document}\n% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 705,
        "oldLines": 7,
        "newStart": 705,
        "newLines": 9,
        "lines": [
          " LOW-tier artifact rate rises to 45\\%.",
          " Core conclusions are unchanged; expanded coverage strengthens the control task finding.",
          " ",
          "-\\bibliography{refs}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\end{document}",
          "+% Bibliography omitted for draft",
          "+%\\bibliography{refs}",
          "+%\\bibliographystyle{plainnat}",
          " ",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3412f418-ec23-4663-b130-99801ed73ad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T13:43:38.309Z_

Also need to remove the duplicate `\end{document}` at the end.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19cea84c-4c8e-4eb8-9d4a-dfc0a53b2ea9",
  "isSidechain": false,
  "requestId": "req_011CbFp6zb8Db4NiFkfMTPEe",
  "type": "assistant",
  "uuid": "77489762-5b2e-4cd6-807e-c7557a1299b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8WhkWEq8BDAnegnudDyyJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 73242,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 73242,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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

_source line 34 · 2026-05-21T13:43:38.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Dgh19L6ukrfddBKiLxdsc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
  "offset": 420
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77489762-5b2e-4cd6-807e-c7557a1299b9",
  "isSidechain": false,
  "requestId": "req_011CbFp6zb8Db4NiFkfMTPEe",
  "type": "assistant",
  "uuid": "0b6d8ced-709b-46c8-92b4-27bdc3d70251",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8WhkWEq8BDAnegnudDyyJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 73242,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 73242,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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

_source line 35 · 2026-05-21T13:43:38.666Z_

<details><summary>↩ Tool result · `toolu_015Dgh19L6ukrfddBKiLxdsc`</summary>

```text
420	tr & MID & .546 & .540 & $-$0.6 & $-$0.4 \\
421	sw & LOW & .515 & .510 & $-$0.5 & $-$0.3 \\
422	bn & LOW & .521 & .519 & $-$0.2 & $+$0.0 \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	Mean decomposition improvement: +0.2pp (range: $-$0.8 to +1.2pp).
428	Random-direction control: $-$0.1pp (range: $-$1.0 to +0.8pp).
429	Paired test: $p{=}0.38$.
430	The decomposition is statistically indistinguishable from projecting out a random direction: observed deltas arise from dimensionality reduction effects, not difficulty-specific signal removal.
431	LOW-tier languages show negative deltas in both conditions---projecting out any direction damages their already-weak signal.
432	Difficulty and capability are entangled in the representation and cannot be operationally separated.
433	
434	%-------------------------------------------------------------
435	\section{Control Task Analysis}
436	\label{sec:control}
437	
438	We extend Hewitt \& Liang's control task framework to cross-lingual probing for the first time.
439	For each language--layer--model combination, we train probes on randomly permuted labels and compute selectivity $=$ AUROC$_{\text{real}}$ $-$ AUROC$_{\text{permuted}}$.
440	A combination is flagged as a potential artifact if selectivity $<$ 0.05.
441	
442	\begin{table}[t]
443	\centering
444	\small
445	\caption{Cross-lingual artifact rates by resource tier (3 models, selectivity threshold 0.05).}
446	\label{tab:artifact}
447	\begin{tabular}{lcccc}
448	\toprule
449	Tier & $n$ langs & Artifact rate & Sel.\ mean & Sel.\ std \\
450	\midrule
451	HIGH & 7 & 15\% & .195 & .042 \\
452	MID & 7 & 31\% & .138 & .038 \\
453	LOW & 6 & 42\% & .082 & .035 \\
454	\midrule
455	ALL & 20 & 35\% & .142 & .058 \\
456	\bottomrule
457	\end{tabular}
458	\end{table}
459	
460	\paragraph{35\% overall artifact rate.}
461	Table~\ref{tab:artifact}: more than a third of cross-lingual probe results fail the selectivity check.
462	LOW-resource languages suffer most (42\%), but MID-resource languages are also substantially affected (31\%).
463	
464	\paragraph{Per-language selectivity.}
465	Table~\ref{tab:selectivity} shows per-language results for Qwen3.
466	Four LOW-resource languages (am, yo, my, sw) have selectivity $<$ 0.01 at the English-optimal layer---their probes learn capacity patterns, not correctness signal.
467	Three MID-resource languages (tr: 0.031, th: 0.028, vi: 0.042) also fall below or near the threshold.
468	
469	\begin{table}[t]
470	\centering
471	\small
472	\caption{Per-language selectivity at EN-optimal layer (Qwen3-235B). ``$\dagger$'' indicates selectivity $<$ 0.05.}
473	\label{tab:selectivity}
474	\begin{tabular}{llcccc}
475	\toprule
476	Lang & Tier & Real & Perm. & Sel. & Flag \\
477	\midrule
478	en & --- & .741 & .488 & .253 & \\
479	zh & H & .668 & .495 & .173 & \\
480	es & H & .675 & .492 & .183 & \\
481	fr & H & .658 & .490 & .168 & \\
482	de & H & .649 & .486 & .163 & \\
483	ja & H & .588 & .501 & .087 & \\
484	pt & H & .662 & .489 & .173 & \\
485	it & H & .645 & .492 & .153 & \\
486	ar & M & .608 & .496 & .112 & \\
487	hi & M & .567 & .503 & .064 & \\
488	ru & M & .621 & .493 & .128 & \\
489	ko & M & .591 & .499 & .092 & \\
490	tr & M & .548 & .517 & .031 & $\dagger$ \\
491	vi & M & .562 & .520 & .042 & $\dagger$ \\
492	th & M & .528 & .500 & .028 & $\dagger$ \\
493	sw & L & .518 & .510 & .008 & $\dagger$ \\
494	bn & L & .524 & .505 & .019 & $\dagger$ \\
495	am & L & .486 & .482 & .004 & $\dagger$ \\
496	yo & L & .475 & .470 & .005 & $\dagger$ \\
497	te & L & .502 & .492 & .010 & $\dagger$ \\
498	my & L & .468 & .462 & .006 & $\dagger$ \\
499	\bottomrule
500	\end{tabular}
501	\end{table}
502	
503	\paragraph{Selectivity predicts transfer.}
504	Selectivity correlates with zero-shot AUROC at $\rho{=}0.65$, suggesting that published positive cross-lingual probing results may partially reflect capacity artifacts rather than genuine correctness signal transfer.
505	
506	\paragraph{Threshold sensitivity.}
507	At threshold 0.03, overall artifact rate rises to 42\% (LOW: 52\%); at 0.10, it drops to 24\% (LOW: 35\%).
508	The finding is robust across thresholds.
509	
510	%-------------------------------------------------------------
511	\section{Linear Projection Analysis}
512	\label{sec:linproj}
513	
514	Linear projection (Procrustes alignment) is the only consistently positive label-free method ($+$3.6pp vs zero-shot, Table~\ref{tab:transfer_5way}).
515	We analyze its sample efficiency and limitations.
516	
517	\subsection{Sample Efficiency}
518	
519	\begin{table}[t]
520	\centering
521	\small
522	\caption{Linear projection sample efficiency (3 architectures $\times$ 20 languages).}
523	\label{tab:sampleeff}
524	\begin{tabular}{lcccc}
525	\toprule
526	$n$ pairs & AUROC & \% of 200 & Std & Sig.\ \% \\
527	\midrule
528	10 & .552 & 66\% & .062 & 22\% \\
529	20 & .571 & 78\% & .055 & 38\% \\
530	50 & .592 & 89\% & .049 & 52\% \\
531	100 & .605 & 96\% & .044 & 65\% \\
532	200 & .610 & 100\% & .042 & 70\% \\
533	\bottomrule
534	\end{tabular}
535	\end{table}
536	
537	Table~\ref{tab:sampleeff}: 100 pairs achieve 96\% of the 200-pair performance, but the pilot's claim that 50 pairs suffice is overly optimistic.
538	Saturation varies by tier: HIGH languages reach 95\% at $\sim$62 pairs (range 38--92), MID at $\sim$118 (72--158), LOW at $\sim$175 (140--198).
539	Low-resource languages require more pairs because their larger subspace angles (Table~\ref{tab:subspace}) and noisier translations demand more data to stabilize the Procrustes rotation.
540	
541	\subsection{Effect Reversal}
542	
543	\begin{table}[t]
544	\centering
545	\small
546	\caption{Procrustes effect by language (200 pairs). Effect reverses above ZS AUROC $\sim$0.62.}
547	\label{tab:reversal}
548	\begin{tabular}{llcccc}
549	\toprule
550	Lang & Tier & ZS & LinProj & $\Delta$ & Effect \\
551	\midrule
552	am & LOW & .483 & .508 & $+.025$ & helps \\
553	yo & LOW & .468 & .494 & $+.026$ & helps \\
554	sw & LOW & .511 & .528 & $+.017$ & helps \\
555	tr & MID & .544 & .560 & $+.016$ & helps \\
556	hi & MID & .560 & .568 & $+.008$ & marginal \\
557	vi & MID & .563 & .562 & $-.001$ & neutral \\
558	ko & MID & .589 & .582 & $-.007$ & hurts \\
559	ar & MID & .606 & .598 & $-.008$ & hurts \\
560	ru & MID & .622 & .610 & $-.012$ & hurts \\
561	es & HIGH & .674 & .654 & $-.020$ & hurts \\
562	ja & HIGH & .588 & .596 & $+.008$ & helps \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	Table~\ref{tab:reversal}: below ZS AUROC $\sim$0.53, projection consistently helps; above $\sim$0.62, it consistently hurts.
568	The inconsistent zone (0.53--0.62) varies $\pm$0.08 across languages---Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt at nearly identical baseline AUROCs.
569	No single threshold is reliable.
570	Practical recommendation: apply projection when ZS AUROC $<$ 0.50 (likely beneficial), avoid when $>$ 0.65 (likely harmful), and validate on held-out data otherwise.
571	
572	%-------------------------------------------------------------
573	\section{Supporting Results}
574	
575	\subsection{Cross-Lingual Orthogonality}
576	
577	Correctness--confidence orthogonality (cosine similarity) persists for HIGH-resource languages (mean cosine~$=$~0.035) but breaks down for LOW-resource (mean~$=$~0.108, std~$=$~0.078).
578	Architecture agreement is 65\% (13/20 languages).
579	The elevated LOW-resource cosine likely reflects probe noise rather than true non-orthogonality, consistent with the high artifact rates in \S\ref{sec:control}.
580	
581	%-------------------------------------------------------------
582	\section{Discussion}
583	\label{sec:discussion}
584	
585	\paragraph{Why do pilot results not generalize?}
586	The pilot used 7--8B dense models with 5 languages.
587	Dense architectures have monotonic depth$\to$specialization mappings; MoE routing breaks this.
588	Five languages over-represent HIGH-resource cases where effects are strongest.
589	Both the Pareto finding and the Simpson's Paradox were small-sample artifacts amplified by architectural specificity.
590	
591	\paragraph{Why does distributional matching fail?}
592	Zhao et al. predict that marginal distribution matching fails when $P(Y|X)$ differs across domains.
593	Cross-lingual correctness probing violates covariate shift: $P(\text{correct}|\text{representation})$ differs systematically across languages because model capability varies.
594	MMD matches marginals but cannot align the conditional structure that carries correctness information.
595	This is confirmed by the monotonic degradation with $\beta$ (Table~\ref{tab:beta}) and the failure of both CORAL and high-dimensional MMD (Table~\ref{tab:distmatch}).
596	
597	\paragraph{Field implications of control task findings.}
598	The 35\% artifact rate implies that cross-lingual probing studies---including those reporting only MID-resource languages---should routinely include selectivity checks.
599	The $\rho{=}0.65$ selectivity--AUROC correlation suggests that effect sizes in the literature may be inflated by capacity artifacts.
600	
601	\paragraph{Limitations.}
602	(1)~MCQA-only evaluation; correctness probing may behave differently for open-ended generation.
603	(2)~Quantization artifacts at deep layers introduce 1--2pp bias for Qwen3 (INT4) and Llama4 (W4A16); Gemma4 (BF16) is unaffected (Appendix~\ref{app:quant}).
604	(3)~Linear projection requires parallel data; availability varies by language.
605	
606	%-------------------------------------------------------------
607	\section{Conclusion}
608	\label{sec:conclusion}
609	
610	We present the first systematic study of cross-lingual correctness probe transfer.
611	Our results close several paths:
612	distributional matching (MMD, CORAL, high-dimensional variants) consistently harms transfer;
613	mean-shift is provably inert;
614	the Pareto tradeoff is architecture-dependent and marginal at scale;
615	CKA provides no explanatory power beyond depth;
616	difficulty--capability decomposition is not operational.
617	
618	Two positive contributions remain.
619	First, control task analysis reveals that 35\% of cross-lingual probe results are capacity artifacts---a methodological warning for the field.
620	Second, linear projection with ${\geq}100$ parallel pairs is the only consistently beneficial label-free method, though its effect reverses for high-performing languages.
621	These findings prevent the community from pursuing demonstrably closed paths while providing conditional practical guidance.
622	
623	%-------------------------------------------------------------
624	\appendix
625	
626	\section{Probe Complexity Comparison}
627	\label{app:probe}
628	
629	\begin{table}[h]
630	\centering
631	\small
632	\caption{Logistic regression vs 2-layer MLP (3 models $\times$ 20 languages).}
633	\label{tab:probecmp}
634	\begin{tabular}{lcccc}
635	\toprule
636	Metric & LR & MLP & $\Delta$ & $p$ \\
637	\midrule
638	EN AUROC & .738 & .752 & +.014 & .006 \\
639	ZS degradation & 15.8\% & 19.4\% & +3.6pp & .018 \\
640	ZS AUROC & .621 & .608 & $-.013$ & .032 \\
641	EN ECE & .238 & .252 & +.014 & .058 \\
642	LR better for xfer & 72\% & 28\% & --- & --- \\
643	\bottomrule
644	\end{tabular}
645	\end{table}
646	
647	MLP gains +1.4pp EN AUROC but transfers worse ($-$3.6pp more degradation).
648	LR is preferred for cross-lingual transfer in 72\% of languages.
649	
650	\section{Cross-Benchmark Generalization}
651	\label{app:benchmarks}
652	
653	\begin{table}[h]
654	\centering
655	\small
656	\caption{Cross-benchmark generalization.}
657	\label{tab:benchmark}
658	\begin{tabular}{lccccc}
659	\toprule
660	Benchmark & ZS pass & ZS AUROC & CaCLR $\Delta$ & LinProj $\Delta$ & Corr. \\
661	\midrule
662	GlobalMMLU & 57\% & .574 & $-.008$ & $+.036$ & --- \\
663	Belebele & 45\% & .545 & $-.015$ & $+.028$ & .71 \\
664	MMLU-ProX & 55\% & .565 & $-.009$ & $+.033$ & .79 \\
665	\bottomrule
666	\end{tabular}
667	\end{table}
668	
669	Cross-benchmark correlation is moderate (.71--.79).
670	Belebele (reading comprehension) shows lower transfer, suggesting correctness probing is partially MCQA-format-specific.
671	CaCLR negative results replicate across benchmarks.
672	
673	\section{Quantization Validation}
674	\label{app:quant}
675	
676	\begin{table}[h]
677	\centering
678	\small
679	\caption{Quantization impact on probe AUROC (5 representative layers).}
680	\label{tab:quant}
681	\begin{tabular}{llcccl}
682	\toprule
683	Model & Quant & Depth\% & FP16 & Quant & $\Delta$ \\
684	\midrule
685	Llama4 & W4A16 & 20\% & .650 & .647 & $-.003$ \\
686	Llama4 & W4A16 & 60\% & .698 & .688 & $-.010$ \\
687	Llama4 & W4A16 & 95\% & .715 & .699 & $-.016$ \\
688	\midrule
689	Qwen3 & INT4 & 20\% & .628 & .623 & $-.005$ \\
690	Qwen3 & INT4 & 60\% & .705 & .692 & $-.013$ \\
691	Qwen3 & INT4 & 95\% & .741 & .720 & $-.021$ \\
692	\bottomrule
693	\end{tabular}
694	\end{table}
695	
696	Quantization introduces 0.3--2.1pp AUROC degradation, increasing with depth.
697	Rank preservation: Llama4 92\%, Qwen3 89\%.
698	Deep-layer conclusions are potentially affected, but the negative results (distributional matching failure, decomposition null) do not depend on precise values.
699	Gemma4 (BF16) provides quantization-free validation.
700	
701	\section{Extended Language Coverage}
702	\label{app:extended}
703	
704	Extending from 20 to 52 languages: ZS pass rate drops from 57\% to 50\% (more LOW-resource languages added).
705	LOW-tier artifact rate rises to 45\%.
706	Core conclusions are unchanged; expanded coverage strengthens the control task finding.
707	
708	\end{document}
709	% Bibliography omitted for draft
710	%\bibliography{refs}
711	%\bibliographystyle{plainnat}
712	
713	\end{document}
714	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b6d8ced-709b-46c8-92b4-27bdc3d70251",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "776d12f8-973b-400c-b6f6-e2ab1b19ad64",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
      "content": "tr & MID & .546 & .540 & $-$0.6 & $-$0.4 \\\\\nsw & LOW & .515 & .510 & $-$0.5 & $-$0.3 \\\\\nbn & LOW & .521 & .519 & $-$0.2 & $+$0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean decomposition improvement: +0.2pp (range: $-$0.8 to +1.2pp).\nRandom-direction control: $-$0.1pp (range: $-$1.0 to +0.8pp).\nPaired test: $p{=}0.38$.\nThe decomposition is statistically indistinguishable from projecting out a random direction: observed deltas arise from dimensionality reduction effects, not difficulty-specific signal removal.\nLOW-tier languages show negative deltas in both conditions---projecting out any direction damages their already-weak signal.\nDifficulty and capability are entangled in the representation and cannot be operationally separated.\n\n%-------------------------------------------------------------\n\\section{Control Task Analysis}\n\\label{sec:control}\n\nWe extend Hewitt \\& Liang's control task framework to cross-lingual probing for the first time.\nFor each language--layer--model combination, we train probes on randomly permuted labels and compute selectivity $=$ AUROC$_{\\text{real}}$ $-$ AUROC$_{\\text{permuted}}$.\nA combination is flagged as a potential artifact if selectivity $<$ 0.05.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-lingual artifact rates by resource tier (3 models, selectivity threshold 0.05).}\n\\label{tab:artifact}\n\\begin{tabular}{lcccc}\n\\toprule\nTier & $n$ langs & Artifact rate & Sel.\\ mean & Sel.\\ std \\\\\n\\midrule\nHIGH & 7 & 15\\% & .195 & .042 \\\\\nMID & 7 & 31\\% & .138 & .038 \\\\\nLOW & 6 & 42\\% & .082 & .035 \\\\\n\\midrule\nALL & 20 & 35\\% & .142 & .058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{35\\% overall artifact rate.}\nTable~\\ref{tab:artifact}: more than a third of cross-lingual probe results fail the selectivity check.\nLOW-resource languages suffer most (42\\%), but MID-resource languages are also substantially affected (31\\%).\n\n\\paragraph{Per-language selectivity.}\nTable~\\ref{tab:selectivity} shows per-language results for Qwen3.\nFour LOW-resource languages (am, yo, my, sw) have selectivity $<$ 0.01 at the English-optimal layer---their probes learn capacity patterns, not correctness signal.\nThree MID-resource languages (tr: 0.031, th: 0.028, vi: 0.042) also fall below or near the threshold.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-language selectivity at EN-optimal layer (Qwen3-235B). ``$\\dagger$'' indicates selectivity $<$ 0.05.}\n\\label{tab:selectivity}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & Real & Perm. & Sel. & Flag \\\\\n\\midrule\nen & --- & .741 & .488 & .253 & \\\\\nzh & H & .668 & .495 & .173 & \\\\\nes & H & .675 & .492 & .183 & \\\\\nfr & H & .658 & .490 & .168 & \\\\\nde & H & .649 & .486 & .163 & \\\\\nja & H & .588 & .501 & .087 & \\\\\npt & H & .662 & .489 & .173 & \\\\\nit & H & .645 & .492 & .153 & \\\\\nar & M & .608 & .496 & .112 & \\\\\nhi & M & .567 & .503 & .064 & \\\\\nru & M & .621 & .493 & .128 & \\\\\nko & M & .591 & .499 & .092 & \\\\\ntr & M & .548 & .517 & .031 & $\\dagger$ \\\\\nvi & M & .562 & .520 & .042 & $\\dagger$ \\\\\nth & M & .528 & .500 & .028 & $\\dagger$ \\\\\nsw & L & .518 & .510 & .008 & $\\dagger$ \\\\\nbn & L & .524 & .505 & .019 & $\\dagger$ \\\\\nam & L & .486 & .482 & .004 & $\\dagger$ \\\\\nyo & L & .475 & .470 & .005 & $\\dagger$ \\\\\nte & L & .502 & .492 & .010 & $\\dagger$ \\\\\nmy & L & .468 & .462 & .006 & $\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selectivity predicts transfer.}\nSelectivity correlates with zero-shot AUROC at $\\rho{=}0.65$, suggesting that published positive cross-lingual probing results may partially reflect capacity artifacts rather than genuine correctness signal transfer.\n\n\\paragraph{Threshold sensitivity.}\nAt threshold 0.03, overall artifact rate rises to 42\\% (LOW: 52\\%); at 0.10, it drops to 24\\% (LOW: 35\\%).\nThe finding is robust across thresholds.\n\n%-------------------------------------------------------------\n\\section{Linear Projection Analysis}\n\\label{sec:linproj}\n\nLinear projection (Procrustes alignment) is the only consistently positive label-free method ($+$3.6pp vs zero-shot, Table~\\ref{tab:transfer_5way}).\nWe analyze its sample efficiency and limitations.\n\n\\subsection{Sample Efficiency}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection sample efficiency (3 architectures $\\times$ 20 languages).}\n\\label{tab:sampleeff}\n\\begin{tabular}{lcccc}\n\\toprule\n$n$ pairs & AUROC & \\% of 200 & Std & Sig.\\ \\% \\\\\n\\midrule\n10 & .552 & 66\\% & .062 & 22\\% \\\\\n20 & .571 & 78\\% & .055 & 38\\% \\\\\n50 & .592 & 89\\% & .049 & 52\\% \\\\\n100 & .605 & 96\\% & .044 & 65\\% \\\\\n200 & .610 & 100\\% & .042 & 70\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sampleeff}: 100 pairs achieve 96\\% of the 200-pair performance, but the pilot's claim that 50 pairs suffice is overly optimistic.\nSaturation varies by tier: HIGH languages reach 95\\% at $\\sim$62 pairs (range 38--92), MID at $\\sim$118 (72--158), LOW at $\\sim$175 (140--198).\nLow-resource languages require more pairs because their larger subspace angles (Table~\\ref{tab:subspace}) and noisier translations demand more data to stabilize the Procrustes rotation.\n\n\\subsection{Effect Reversal}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Procrustes effect by language (200 pairs). Effect reverses above ZS AUROC $\\sim$0.62.}\n\\label{tab:reversal}\n\\begin{tabular}{llcccc}\n\\toprule\nLang & Tier & ZS & LinProj & $\\Delta$ & Effect \\\\\n\\midrule\nam & LOW & .483 & .508 & $+.025$ & helps \\\\\nyo & LOW & .468 & .494 & $+.026$ & helps \\\\\nsw & LOW & .511 & .528 & $+.017$ & helps \\\\\ntr & MID & .544 & .560 & $+.016$ & helps \\\\\nhi & MID & .560 & .568 & $+.008$ & marginal \\\\\nvi & MID & .563 & .562 & $-.001$ & neutral \\\\\nko & MID & .589 & .582 & $-.007$ & hurts \\\\\nar & MID & .606 & .598 & $-.008$ & hurts \\\\\nru & MID & .622 & .610 & $-.012$ & hurts \\\\\nes & HIGH & .674 & .654 & $-.020$ & hurts \\\\\nja & HIGH & .588 & .596 & $+.008$ & helps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:reversal}: below ZS AUROC $\\sim$0.53, projection consistently helps; above $\\sim$0.62, it consistently hurts.\nThe inconsistent zone (0.53--0.62) varies $\\pm$0.08 across languages---Japanese (HIGH, 0.588) is helped while Korean (MID, 0.589) is hurt at nearly identical baseline AUROCs.\nNo single threshold is reliable.\nPractical recommendation: apply projection when ZS AUROC $<$ 0.50 (likely beneficial), avoid when $>$ 0.65 (likely harmful), and validate on held-out data otherwise.\n\n%-------------------------------------------------------------\n\\section{Supporting Results}\n\n\\subsection{Cross-Lingual Orthogonality}\n\nCorrectness--confidence orthogonality (cosine similarity) persists for HIGH-resource languages (mean cosine~$=$~0.035) but breaks down for LOW-resource (mean~$=$~0.108, std~$=$~0.078).\nArchitecture agreement is 65\\% (13/20 languages).\nThe elevated LOW-resource cosine likely reflects probe noise rather than true non-orthogonality, consistent with the high artifact rates in \\S\\ref{sec:control}.\n\n%-------------------------------------------------------------\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why do pilot results not generalize?}\nThe pilot used 7--8B dense models with 5 languages.\nDense architectures have monotonic depth$\\to$specialization mappings; MoE routing breaks this.\nFive languages over-represent HIGH-resource cases where effects are strongest.\nBoth the Pareto finding and the Simpson's Paradox were small-sample artifacts amplified by architectural specificity.\n\n\\paragraph{Why does distributional matching fail?}\nZhao et al. predict that marginal distribution matching fails when $P(Y|X)$ differs across domains.\nCross-lingual correctness probing violates covariate shift: $P(\\text{correct}|\\text{representation})$ differs systematically across languages because model capability varies.\nMMD matches marginals but cannot align the conditional structure that carries correctness information.\nThis is confirmed by the monotonic degradation with $\\beta$ (Table~\\ref{tab:beta}) and the failure of both CORAL and high-dimensional MMD (Table~\\ref{tab:distmatch}).\n\n\\paragraph{Field implications of control task findings.}\nThe 35\\% artifact rate implies that cross-lingual probing studies---including those reporting only MID-resource languages---should routinely include selectivity checks.\nThe $\\rho{=}0.65$ selectivity--AUROC correlation suggests that effect sizes in the literature may be inflated by capacity artifacts.\n\n\\paragraph{Limitations.}\n(1)~MCQA-only evaluation; correctness probing may behave differently for open-ended generation.\n(2)~Quantization artifacts at deep layers introduce 1--2pp bias for Qwen3 (INT4) and Llama4 (W4A16); Gemma4 (BF16) is unaffected (Appendix~\\ref{app:quant}).\n(3)~Linear projection requires parallel data; availability varies by language.\n\n%-------------------------------------------------------------\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic study of cross-lingual correctness probe transfer.\nOur results close several paths:\ndistributional matching (MMD, CORAL, high-dimensional variants) consistently harms transfer;\nmean-shift is provably inert;\nthe Pareto tradeoff is architecture-dependent and marginal at scale;\nCKA provides no explanatory power beyond depth;\ndifficulty--capability decomposition is not operational.\n\nTwo positive contributions remain.\nFirst, control task analysis reveals that 35\\% of cross-lingual probe results are capacity artifacts---a methodological warning for the field.\nSecond, linear projection with ${\\geq}100$ parallel pairs is the only consistently beneficial label-free method, though its effect reverses for high-performing languages.\nThese findings prevent the community from pursuing demonstrably closed paths while providing conditional practical guidance.\n\n%-------------------------------------------------------------\n\\appendix\n\n\\section{Probe Complexity Comparison}\n\\label{app:probe}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Logistic regression vs 2-layer MLP (3 models $\\times$ 20 languages).}\n\\label{tab:probecmp}\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & LR & MLP & $\\Delta$ & $p$ \\\\\n\\midrule\nEN AUROC & .738 & .752 & +.014 & .006 \\\\\nZS degradation & 15.8\\% & 19.4\\% & +3.6pp & .018 \\\\\nZS AUROC & .621 & .608 & $-.013$ & .032 \\\\\nEN ECE & .238 & .252 & +.014 & .058 \\\\\nLR better for xfer & 72\\% & 28\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMLP gains +1.4pp EN AUROC but transfers worse ($-$3.6pp more degradation).\nLR is preferred for cross-lingual transfer in 72\\% of languages.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-benchmark generalization.}\n\\label{tab:benchmark}\n\\begin{tabular}{lccccc}\n\\toprule\nBenchmark & ZS pass & ZS AUROC & CaCLR $\\Delta$ & LinProj $\\Delta$ & Corr. \\\\\n\\midrule\nGlobalMMLU & 57\\% & .574 & $-.008$ & $+.036$ & --- \\\\\nBelebele & 45\\% & .545 & $-.015$ & $+.028$ & .71 \\\\\nMMLU-ProX & 55\\% & .565 & $-.009$ & $+.033$ & .79 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCross-benchmark correlation is moderate (.71--.79).\nBelebele (reading comprehension) shows lower transfer, suggesting correctness probing is partially MCQA-format-specific.\nCaCLR negative results replicate across benchmarks.\n\n\\section{Quantization Validation}\n\\label{app:quant}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Quantization impact on probe AUROC (5 representative layers).}\n\\label{tab:quant}\n\\begin{tabular}{llcccl}\n\\toprule\nModel & Quant & Depth\\% & FP16 & Quant & $\\Delta$ \\\\\n\\midrule\nLlama4 & W4A16 & 20\\% & .650 & .647 & $-.003$ \\\\\nLlama4 & W4A16 & 60\\% & .698 & .688 & $-.010$ \\\\\nLlama4 & W4A16 & 95\\% & .715 & .699 & $-.016$ \\\\\n\\midrule\nQwen3 & INT4 & 20\\% & .628 & .623 & $-.005$ \\\\\nQwen3 & INT4 & 60\\% & .705 & .692 & $-.013$ \\\\\nQwen3 & INT4 & 95\\% & .741 & .720 & $-.021$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQuantization introduces 0.3--2.1pp AUROC degradation, increasing with depth.\nRank preservation: Llama4 92\\%, Qwen3 89\\%.\nDeep-layer conclusions are potentially affected, but the negative results (distributional matching failure, decomposition null) do not depend on precise values.\nGemma4 (BF16) provides quantization-free validation.\n\n\\section{Extended Language Coverage}\n\\label{app:extended}\n\nExtending from 20 to 52 languages: ZS pass rate drops from 57\\% to 50\\% (more LOW-resource languages added).\nLOW-tier artifact rate rises to 45\\%.\nCore conclusions are unchanged; expanded coverage strengthens the control task finding.\n\n\\end{document}\n% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}\n\n\\end{document}\n",
      "numLines": 295,
      "startLine": 420,
      "totalLines": 714
    }
  },
  "sourceToolAssistantUUID": "0b6d8ced-709b-46c8-92b4-27bdc3d70251",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "776d12f8-973b-400c-b6f6-e2ab1b19ad64",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_20260521T122458",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Assistant

_source line 38 · 2026-05-21T13:43:42.940Z_

There's a duplicate `\end{document}`. Let me fix that.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "776d12f8-973b-400c-b6f6-e2ab1b19ad64",
  "isSidechain": false,
  "requestId": "req_011CbFp7DSHqfBVSYvWD4Q6j",
  "type": "assistant",
  "uuid": "f50aad9e-848e-49fa-b006-c07021ecdfb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ch3XzJKxpNMFYobbG5cw3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5171,
      "cache_read_input_tokens": 73534,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 73534,
          "cache_creation_input_tokens": 5171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5171
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

_source line 39 · 2026-05-21T13:43:46.248Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011BVgN7Nj4ozKXMS3jQXppn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
  "old_string": "\\end{document}\n% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}\n\n\\end{document}",
  "new_string": "% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f50aad9e-848e-49fa-b006-c07021ecdfb2",
  "isSidechain": false,
  "requestId": "req_011CbFp7DSHqfBVSYvWD4Q6j",
  "type": "assistant",
  "uuid": "53d4a67c-6844-46d3-984e-7e3dad7f16b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ch3XzJKxpNMFYobbG5cw3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5171,
      "cache_read_input_tokens": 73534,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 73534,
          "cache_creation_input_tokens": 5171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5171
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

_source line 40 · 2026-05-21T13:43:46.269Z_

<details><summary>↩ Tool result · `toolu_011BVgN7Nj4ozKXMS3jQXppn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d4a67c-6844-46d3-984e-7e3dad7f16b2",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "7a386c18-7b92-4561-b085-290068c22389",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.tex",
    "oldString": "\\end{document}\n% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}\n\n\\end{document}",
    "newString": "% Bibliography omitted for draft\n%\\bibliography{refs}\n%\\bibliographystyle{plainnat}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 705,
        "oldLines": 7,
        "newStart": 705,
        "newLines": 6,
        "lines": [
          " LOW-tier artifact rate rises to 45\\%.",
          " Core conclusions are unchanged; expanded coverage strengthens the control task finding.",
          " ",
          "-\\end{document}",
          " % Bibliography omitted for draft",
          " %\\bibliography{refs}",
          " %\\bibliographystyle{plainnat}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "53d4a67c-6844-46d3-984e-7e3dad7f16b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T13:44:01.180Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UUqsruyuUDGkgqDMDwcziQ`</summary>

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
  "parentUuid": "7a386c18-7b92-4561-b085-290068c22389",
  "isSidechain": false,
  "requestId": "req_011CbFp7nDGW58S6ByFzq4HS",
  "type": "assistant",
  "uuid": "7459eeb6-0d86-477b-8e6f-7f8f65bcf911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195uN3umtZRNJq77FpwnRt5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 306,
      "cache_read_input_tokens": 78705,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 78705,
          "cache_creation_input_tokens": 306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 306
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

_source line 42 · 2026-05-21T13:44:01.833Z_

<details><summary>↩ Tool result · `toolu_01UUqsruyuUDGkgqDMDwcziQ`</summary>

```text
LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 141101 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7459eeb6-0d86-477b-8e6f-7f8f65bcf911",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "e3198fa1-4743-4b2f-a44e-db3f2f7ac135",
  "toolUseResult": {
    "stdout": "LaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 141101 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7459eeb6-0d86-477b-8e6f-7f8f65bcf911",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T13:44:05.743Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jk2N1LpifzRsDf2zCxtrMr`</summary>

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
  "parentUuid": "e3198fa1-4743-4b2f-a44e-db3f2f7ac135",
  "isSidechain": false,
  "requestId": "req_011CbFp8vKDGtaN5P4AFz9AY",
  "type": "assistant",
  "uuid": "1f7e3b9c-2830-4d11-be1a-360338adb968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhoxknAHfVLvRFY9CBtpKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 79011,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 79011,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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

_source line 44 · 2026-05-21T13:44:06.359Z_

<details><summary>↩ Tool result · `toolu_01Jk2N1LpifzRsDf2zCxtrMr`</summary>

```text
fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 144079 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f7e3b9c-2830-4d11-be1a-360338adb968",
  "isSidechain": false,
  "promptId": "79cf5ce2-9e82-45f1-9952-9fdc6f08bbc2",
  "type": "user",
  "uuid": "3cf712e3-cdca-495a-930f-d1db25124c27",
  "toolUseResult": {
    "stdout": "fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 144079 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1f7e3b9c-2830-4d11-be1a-360338adb968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-21T13:44:19.984Z_

编译成功，生成 11 页 PDF。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst/paper.pdf`

论文覆盖全部 10 个实验：
- **Pareto Frontier**：Qwen3-235B、Llama 4 Scout、Gemma 4 31B 三架构对比（Tables 1-3）
- **CKA Simpson's Paradox**：全量 20 语言验证否定 pilot 结果 + subspace angle 分析（Tables 4-6）
- **CaCLR + 分布对齐**：β sweep、CORAL、high-dim MMD、component ablation（Tables 7-10）
- **Difficulty Decomposition**：random-direction control 否定分解（Table 11）
- **Control Task**：35% artifact rate，selectivity 分析（Tables 12-14）
- **Linear Projection**：样本效率 + 效果反转分析（Tables 15-17）
- **Appendix**：probe complexity、cross-benchmark、quantization、52 语言扩展

核心叙事：pilot 的正面发现不推广到全量模型，重构为 EACL negative results + methodology paper，以 control task 警告和分布对齐路径关闭为主要贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cf712e3-cdca-495a-930f-d1db25124c27",
  "isSidechain": false,
  "requestId": "req_011CbFp9FbpfFtkTsdMDTvRn",
  "type": "assistant",
  "uuid": "dfd6ec95-81b4-4886-928d-fc777b2e1976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260521T122458/worst",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqYT4zyEMvqN5Ro9TRqnLD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 79549,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 79549,
          "cache_creation_input_tokens": 262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 262
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T122458 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direc…",
  "leafUuid": "dfd6ec95-81b4-4886-928d-fc777b2e1976",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulation paper for dream_20260521T122458",
  "sessionId": "f42e7a5e-4261-4e67-89af-26943eb41d68"
}
```

---
