# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/4f83ae47-14e0-4308-9a87-39cf36bef00d.jsonl`
- **Structured JSON:** [`4d35e6818c88dfe502fb.json`](../../sessions/4d/4d35e6818c88dfe502fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:34:28.443Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:34:28.443Z",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：KL优势是假象。BCE的核心瓶颈不是loss function而是缺少compensation mechanism。 加上FastForward风格的compensation MLP后，BCE+comp在PPL和downstream tasks上追平甚至反超KL-only。 KL-only训练不稳定（5-seed std > 0.8，2个新seed PPL > 10.5），稳定性劣于BCE+comp。 s²scaling理论不成立（R² < 0.7），linear fit同样好。SPON+KL非可加，Mistral结果方向反转。 Paper重心从\"KL eliminates compensation\"转向\"首个系统性taxonomy of training signals × correction granularity for activation sparsity\"，以characterization study投EMNLP Efficient Methods track。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T17:34:28.447Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:34:28.447Z",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-15T17:34:28.467Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：KL优势是假象。BCE的核心瓶颈不是loss function而是缺少compensation mechanism。 加上FastForward风格的compensation MLP后，BCE+comp在PPL和downstream tasks上追平甚至反超KL-only。 KL-only训练不稳定（5-seed std > 0.8，2个新seed PPL > 10.5），稳定性劣于BCE+comp。 s²scaling理论不成立（R² < 0.7），linear fit同样好。SPON+KL非可加，Mistral结果方向反转。 Paper重心从"KL eliminates compensation"转向"首个系统性taxonomy of training signals × correction granularity for activation sparsity"，以characterization study投EMNLP Efficient Methods track。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "d3ca91d7-af2a-4a8d-b0b3-966c35f6df81",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:34:28.467Z_

```json
{
  "parentUuid": "d3ca91d7-af2a-4a8d-b0b3-966c35f6df81",
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
  "uuid": "e220620b-5c9b-40ea-9636-2ffa26e12189",
  "timestamp": "2026-05-15T17:34:28.467Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:34:28.467Z_

```json
{
  "parentUuid": "e220620b-5c9b-40ea-9636-2ffa26e12189",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ca683b58-6674-41c2-a8cc-f6e13eae08d6",
  "timestamp": "2026-05-15T17:34:28.467Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
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
  "aiTitle": "Generate worst-tier research paper",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Assistant

_source line 7 · 2026-05-15T17:34:30.326Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca683b58-6674-41c2-a8cc-f6e13eae08d6",
  "isSidechain": false,
  "requestId": "req_011Cb4kreXrH7Yq1JPhuuV8W",
  "type": "assistant",
  "uuid": "b765c3ce-4b76-478e-9b61-605796566272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x3kn5dtJqcZR26GDxSHeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11269,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11269
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

_source line 8 · 2026-05-15T17:34:31.550Z_

<details open><summary>🔧 Tool call — Read · `toolu_019aHjwJFxLqFaWtNg3M5Whi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b765c3ce-4b76-478e-9b61-605796566272",
  "isSidechain": false,
  "requestId": "req_011Cb4kreXrH7Yq1JPhuuV8W",
  "type": "assistant",
  "uuid": "ceb0ce63-4bf8-440d-a0f2-eee9c1396141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x3kn5dtJqcZR26GDxSHeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11269,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11269
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

_source line 9 · 2026-05-15T17:34:31.675Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EY8YfH7jd4kpb6Ne12ExbA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceb0ce63-4bf8-440d-a0f2-eee9c1396141",
  "isSidechain": false,
  "requestId": "req_011Cb4kreXrH7Yq1JPhuuV8W",
  "type": "assistant",
  "uuid": "3b645bea-63ac-4d5c-84ae-0253cc879746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019x3kn5dtJqcZR26GDxSHeK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11269,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11269
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

_source line 10 · 2026-05-15T17:34:31.686Z_

<details><summary>↩ Tool result · `toolu_01EY8YfH7jd4kpb6Ne12ExbA`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)
11	
12	2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.
13	
14	3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.
47	
48	## Venue Fit
49	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
50	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
51	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b645bea-63ac-4d5c-84ae-0253cc879746",
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "b093e988-d8a6-4776-a9ef-46c17a009357",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "3b645bea-63ac-4d5c-84ae-0253cc879746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T17:34:31.822Z_

<details><summary>↩ Tool result · `toolu_019aHjwJFxLqFaWtNg3M5Whi`</summary>

```text
1	[
2	  {
3	    "name": "Four-condition ablation @ 50% sparsity",
4	    "description": "四条件消融：(a) BCE-only 3 seeds existing, (b) BCE+comp 5 seeds new, (c) KL-only 5 seeds (3 existing + 2 new), (d) KL+comp 3 seeds new。 Headline对比KL-only vs BCE+comp各5 seeds。",
5	    "results": {
6	      "kl_only_s42_ppl": 9.21,
7	      "kl_only_s123_ppl": 9.25,
8	      "kl_only_s456_ppl": 9.14,
9	      "kl_only_s0_ppl": 10.31,
10	      "kl_only_s1_ppl": 11.08,
11	      "kl_only_mean_ppl": 9.8,
12	      "kl_only_std_ppl": 0.87,
13	      "kl_only_model_sparsity": 0.498,
14	      "bce_comp_s42_ppl": 9.18,
15	      "bce_comp_s123_ppl": 9.35,
16	      "bce_comp_s456_ppl": 9.52,
17	      "bce_comp_s0_ppl": 9.28,
18	      "bce_comp_s1_ppl": 9.68,
19	      "bce_comp_mean_ppl": 9.4,
20	      "bce_comp_std_ppl": 0.19,
21	      "bce_comp_model_sparsity": 0.496,
22	      "kl_comp_s42_ppl": 8.82,
23	      "kl_comp_s123_ppl": 8.95,
24	      "kl_comp_s456_ppl": 9.08,
25	      "kl_comp_mean_ppl": 8.95,
26	      "kl_comp_std_ppl": 0.13,
27	      "bce_only_mean_ppl": 28.16,
28	      "kl_vs_bce_comp_gap": 0.4,
29	      "kl_comp_vs_bce_comp_gap": -0.45,
30	      "dense_ppl": 6.12
31	    },
32	    "tables": [
33	      {
34	        "title": "Table 1: Four-condition WikiText-2 PPL @ 50% sparsity (Llama 3.1 8B)",
35	        "rows": [
36	          "Condition | Seeds | Mean PPL | Std | Δ vs Dense (%)",
37	          "Dense (no sparsity) | — | 6.12 | — | —",
38	          "BCE-only | 3 | 28.16 | 0.22 | +360.1%",
39	          "BCE+compensation | 5 | 9.40 | 0.19 | +53.6%",
40	          "KL-only | 5 | 9.80 | 0.87 | +60.1%",
41	          "KL+compensation | 3 | 8.95 | 0.13 | +46.2%"
42	        ]
43	      },
44	      {
45	        "title": "Table 1b: Per-seed breakdown",
46	        "rows": [
47	          "Seed | BCE-only | BCE+comp | KL-only | KL+comp",
48	          "s42  | 27.96    | 9.18     | 9.21    | 8.82",
49	          "s123 | 28.38    | 9.35     | 9.25    | 8.95",
50	          "s456 | 28.14    | 9.52     | 9.14    | 9.08",
51	          "s0   | —        | 9.28     | 10.31   | —",
52	          "s1   | —        | 9.68     | 11.08   | —"
53	        ]
54	      }
55	    ],
56	    "figures": [],
57	    "analysis": "headline claim \"KL eliminates compensation\"不成立。BCE+comp (9.40) < KL-only (9.80)， 且KL-only的高方差使其在deployment中不可靠。 KL+comp是全局最佳（8.95），但这反证了compensation的通用价值， 而非KL的独特优势。Narrative需从\"KL beats BCE+comp\"转向 \"characterization: 不同training signal × compensation的交互效应\"。 唯一保留的KL叙事：KL-only在不使用compensation时确实优于BCE-only（9.80 vs 28.16）， 但这个\"免compensation\"优势在BCE+comp面前消失。\n\ns0和s1两个新seed暴露了KL训练的Lagrangian不稳定性。 Lagrangian乘子在这两个seed下出现λ震荡（未收敛到稳定平衡点）， 导致sparsity在0.47-0.52间振荡，predictor未充分优化。 s456的teal异常（13.58 vs 12.08/11.91）已经暗示了seed敏感性， 新seed进一步确认：KL+Lagrangian在某些初始化下不稳定， std=0.87远高于BCE+comp的0.19。 BCE+comp通过compensation MLP有效纠正了BCE predictor的per-neuron误差， 从28.16降至9.40——compensation消除了~67%的BCE quality gap。 KL+comp是最佳条件（8.95），说明compensation对KL也有帮助， 而非KL已经\"不需要\"compensation。核心发现：compensation是通用质量提升手段， KL的\"优势\"仅是在不公平对比（有comp vs 无comp）下的假象。"
58	  },
59	  {
60	    "name": "STE baseline (KL + Straight-Through Estimator)",
61	    "description": "用STE替换Gumbel-sigmoid作为梯度通路，保留KL loss不变。 隔离KL优势来源：loss function还是relaxation method。3 seeds。",
62	    "results": {
63	      "ste_kl_s42_ppl": 9.85,
64	      "ste_kl_s123_ppl": 10.1,
65	      "ste_kl_s456_ppl": 9.72,
66	      "ste_kl_mean_ppl": 9.89,
67	      "ste_kl_std_ppl": 0.19,
68	      "ste_kl_model_sparsity": 0.497,
69	      "ste_kl_vs_gumbel_kl_gap": 0.09,
70	      "ste_kl_training_steps_to_converge": 950
71	    },
72	    "tables": [
73	      {
74	        "title": "Table 2: Gradient estimator ablation (KL loss fixed)",
75	        "rows": [
76	          "Method | Mean PPL | Std | Sparsity",
77	          "Gumbel-sigmoid + KL | 9.80 | 0.87 | 0.498",
78	          "STE + KL | 9.89 | 0.19 | 0.497",
79	          "BCE-only (ref) | 28.16 | 0.22 | 0.496"
80	        ]
81	      }
82	    ],
83	    "figures": [],
84	    "analysis": "STE≈Gumbel确认relaxation method不是KL优势的来源。 但结合BCE+comp追平KL的结果，因果归因链断裂： KL的优势不来自relaxation，也不来自\"独特的loss function\"—— 因为compensation可以弥补BCE的不足。 论文无法claim \"our Gumbel-KL combination is uniquely effective\"。 可作为honest ablation报告，支持characterization study叙事。 额外发现：STE+KL的std=0.19远低于Gumbel+KL的0.87， 说明Gumbel温度退火引入了额外的seed sensitivity（进一步削弱Gumbel的必要性）。\n\nSTE+KL (9.89) ≈ Gumbel+KL (9.80)，差距仅0.09 PPL，在KL-only自身方差（std=0.87） 内可忽略。这说明Gumbel-sigmoid relaxation对最终质量贡献极小， KL loss gradient本身才是驱动因素。 表面上这支持\"KL是关键\"——但结合plan_001的结论（BCE+comp追平KL）， 更准确的解读是：任何能传递端到端output-distribution信息的training signal （无论STE还是Gumbel路径）都能达到~9.8 PPL，而BCE+comp通过不同路径达到了9.4。 relaxation method不重要这一事实削弱了论文的technical novelty—— \"Gumbel + KL\"不是一个不可替代的组合，STE+KL同样有效。"
85	  },
86	  {
87	    "name": "Iso-compute BCE vs KL",
88	    "description": "KL每步需full forward pass计算output logits（~2x FLOPs per step vs BCE用cached targets）。 给BCE等量total FLOPs（extended training），评估compute-normalized比较。3 seeds。",
89	    "results": {
90	      "kl_flops_per_step": "4.2e14",
91	      "bce_flops_per_step": "1.8e14",
92	      "kl_total_training_flops": "4.2e17",
93	      "bce_extended_steps": 2333,
94	      "bce_extended_s42_ppl": 24.5,
95	      "bce_extended_s123_ppl": 25.1,
96	      "bce_extended_s456_ppl": 24.8,
97	      "bce_extended_mean_ppl": 24.8,
98	      "bce_extended_std_ppl": 0.3,
99	      "bce_1000step_mean_ppl": 28.16,
100	      "bce_improvement_from_extended": -3.36,
101	      "kl_training_time_min": 42,
102	      "bce_extended_training_time_min": 58
103	    },
104	    "tables": [
105	      {
106	        "title": "Table 3: Iso-compute comparison",
107	        "rows": [
108	          "Condition | Steps | Total FLOPs | Mean PPL | Wall Time",
109	          "KL-only (1000 steps) | 1000 | 4.2e17 | 9.80 | 42 min",
110	          "BCE-only (1000 steps) | 1000 | 1.8e17 | 28.16 | 25 min",
111	          "BCE-only (extended, iso-FLOP) | 2333 | 4.2e17 | 24.80 | 58 min",
112	          "BCE+comp (1000+500 steps) | 1500 | 3.5e17 | 9.40 | 50 min"
113	        ]
114	      }
115	    ],
116	    "figures": [],
117	    "analysis": "Iso-compute消除了\"KL wins because more compute\"的reviewer concern。 但同时也表明：BCE的瓶颈不是compute，而是loss function的结构性局限。 当compensation弥补了这个局限后（BCE+comp），以更少compute达到更好结果。 论文中可诚实报告：KL确实compute-efficient（fewer total FLOPs to reach good quality）， 但\"KL eliminates compensation\"的claim仍然不成立。\n\nBCE extended training从28.16降至24.80——额外1333步仅带来3.36 PPL改善。 BCE的收敛曲线在~800步后进入plateau，更多步数的边际收益递减。 这是因为BCE的per-neuron factorized gradient本身信息不足： 无论训练多久，BCE无法学到neuron间的joint interaction。 但这个结果不支持\"KL需要更多compute所以不公平\"的reviewer concern—— 即使给BCE等量compute，差距仍然巨大（24.80 vs 9.80）。 然而结合plan_001，真正的解决方案不是更多BCE training， 而是加compensation（9.40）——这才是compute的正确使用方式。"
118	  },
119	  {
120	    "name": "SPON reimplementation & reproduction",
121	    "description": "在Llama 3.1 8B上重现SPON（static learnable bias + KL training）。 5个QA benchmarks验证reproduction质量。",
122	    "results": {
123	      "spon_wikitext2_ppl": 10.82,
124	      "spon_model_sparsity": 0.5,
125	      "spon_params_per_layer": 4096,
126	      "spon_total_params": 131072,
127	      "spon_training_time_min": 15,
128	      "spon_arc_c": 50.2,
129	      "spon_arc_e": 77.5,
130	      "spon_boolq": 79.8,
131	      "spon_piqa": 78.1,
132	      "spon_winogrande": 73.6,
133	      "published_arc_c": 50.8,
134	      "published_arc_e": 78.2,
135	      "published_boolq": 80.5,
136	      "published_piqa": 78.8,
137	      "published_winogrande": 74.2,
138	      "reproduction_max_gap": 1.0
139	    },
140	    "tables": [
141	      {
142	        "title": "Table 4: SPON reproduction on 5 QA benchmarks",
143	        "rows": [
144	          "Benchmark | Published | Ours | Δ",
145	          "ARC-c | 50.8 | 50.2 | -0.6",
146	          "ARC-e | 78.2 | 77.5 | -0.7",
147	          "BoolQ | 80.5 | 79.8 | -0.7",
148	          "PIQA | 78.8 | 78.1 | -0.7",
149	          "WinoGrande | 74.2 | 73.6 | -0.6"
150	        ]
151	      }
152	    ],
153	    "figures": [],
154	    "analysis": "SPON reproduction成功，5个benchmark最大偏差0.7 points。 PPL=10.82介于KL-only (9.80)和training-free (~12.5)之间， 符合static correction的预期能力范围。\n\nSPON方法简单（每层仅hidden_dim个learnable参数），超参数空间小， reproduction误差主要来自KL训练的随机性和calibration data差异。 所有5个benchmark与published results差距 < 1 point，reproduction合格。 PPL=10.82确认static correction的天花板：input-independent bias只能修正 average-case drift，无法适应per-input neuron importance变化。 这为plan_005的composition实验提供了valid SPON baseline。"
155	  },
156	  {
157	    "name": "SPON + KL predictor composition & additivity test",
158	    "description": "同时应用SPON bias correction + KL contextual prediction。 Output-space linearity测试和per-layer正交性分析。3 seeds。",
159	    "results": {
160	      "spon_kl_s42_ppl": 9.55,
161	      "spon_kl_s123_ppl": 9.78,
162	      "spon_kl_s456_ppl": 10.05,
163	      "spon_kl_mean_ppl": 9.79,
164	      "spon_kl_std_ppl": 0.25,
165	      "spon_only_ppl": 10.82,
166	      "kl_only_mean_ppl": 9.8,
167	      "teal_baseline_ppl": 12.5,
168	      "spon_improvement_over_teal": 1.68,
169	      "kl_improvement_over_teal": 2.7,
170	      "predicted_additive_ppl": 8.12,
171	      "actual_combined_ppl": 9.79,
172	      "additivity_residual_ppl": 1.67,
173	      "additivity_ratio": 0.62,
174	      "logit_residual_norm_ratio": 0.38,
175	      "mean_cos_similarity": 0.34,
176	      "layers_with_cos_gt_03": 20,
177	      "max_cos_similarity_layer": 0.62
178	    },
179	    "tables": [
180	      {
181	        "title": "Table 5: SPON + KL composition results",
182	        "rows": [
183	          "Condition | PPL | Improvement over TEAL",
184	          "TEAL baseline | 12.50 | —",
185	          "SPON only | 10.82 | 1.68",
186	          "KL only | 9.80 | 2.70",
187	          "SPON+KL (actual) | 9.79 | 2.71",
188	          "SPON+KL (additive prediction) | 8.12 | 4.38"
189	        ]
190	      },
191	      {
192	        "title": "Table 5b: Additivity metrics",
193	        "rows": [
194	          "Metric | Value",
195	          "Additivity ratio | 0.62",
196	          "Logit residual norm ratio | 0.38",
197	          "Mean cos(c_s, c_θ) | 0.34",
198	          "Layers with cos > 0.3 | 20/32"
199	        ]
200	      }
201	    ],
202	    "figures": [],
203	    "analysis": "SPON+KL composition不满足可加性假设（Claim 2不成立）。 但这本身是一个有价值的empirical finding—— \"static和contextual corrections的overlap分析\"可作为standalone贡献。 论文中不再claim可加性，改为report interaction structure： \"static和contextual corrections在中间层高度相关， suggesting both target the same error mode (average-case neuron importance drift)\"。 这支持characterization study的叙事方向。\n\nSPON+KL (9.79) ≈ KL-only (9.80)——组合几乎没有额外收益。 predicted additive PPL=8.12 vs actual=9.79，additivity ratio仅0.62。 原因：SPON的static bias和KL predictor的contextual correction在output space 高度相关——两者都在修正同一组\"容易误杀\"的neurons的drift。 cos similarity分析确认：在中间层（layer 12-20），两种correction方向高度一致 （cos > 0.4），说明它们修正的是同一类误差而非互补的不同误差源。 Claim 2（可加性）在worst tier下彻底不成立。 logit_residual_norm_ratio=0.38 >> 0（如果可加应接近0）， interaction term不可忽略。"
204	  },
205	  {
206	    "name": "Training-free baselines @ 50% sparsity",
207	    "description": "TEAL (activation magnitude + greedy allocation), WINA (weight-informed scoring), R-Sparse (rank-aware scoring)。建立三层比较：training-free < static-learned < contextual-learned。",
208	    "results": {
209	      "teal_vanilla_ppl": 12.48,
210	      "wina_ppl": 15.8,
211	      "rsparse_ppl": 14.2,
212	      "dense_ppl": 6.12,
213	      "teal_vanilla_sparsity": 0.5,
214	      "wina_sparsity": 0.5,
215	      "rsparse_sparsity": 0.5,
216	      "teal_vs_dense_pct": 103.9,
217	      "wina_vs_dense_pct": 158.2,
218	      "rsparse_vs_dense_pct": 132.0
219	    },
220	    "tables": [
221	      {
222	        "title": "Table 6: Training-free baselines @ 50% sparsity",
223	        "rows": [
224	          "Method | WikiText-2 PPL | Δ vs Dense (%)",
225	          "Dense | 6.12 | —",
226	          "TEAL (activation magnitude) | 12.48 | +103.9%",
227	          "R-Sparse | 14.20 | +132.0%",
228	          "WINA | 15.80 | +158.2%",
229	          "SPON (static learned) | 10.82 | +76.8%",
230	          "KL-only (contextual) | 9.80 | +60.1%",
231	          "BCE+comp (contextual) | 9.40 | +53.6%"
232	        ]
233	      }
234	    ],
235	    "figures": [],
236	    "analysis": "三层层级结构清晰，training-free到contextual有6-7 PPL points的gap。 这验证了learned prediction的价值。在worst tier下， KL-only和BCE+comp处于同一tier（contextual），彼此差距不显著。 paper的taxonomy贡献成立：不同training signal在不同granularity下的表现分布 本身就是有价值的empirical map。\n\nTEAL表现最好（12.48），因为activation magnitude是neuron importance的直接proxy， 加上greedy per-layer allocation自适应地保护关键层。 R-Sparse (14.20)次之——rank-aware scoring考虑了相对重要性但无跨层allocation。 WINA最差（15.80）——weight-informed scoring在SwiGLU gate×up结构下信号较弱， weight magnitude与activation importance的相关性不如直接用activation。 这建立了清晰的tier结构：training-free（12-16）<< SPON（10.8）<< contextual（9.4-9.8）。 注意这里的TEAL使用vanilla activation magnitude（非predictor scores）， 与registry中基于predictor scores的\"teal_sparse_ppl\"不同。"
237	  },
238	  {
239	    "name": "Full benchmark suite + wall-clock profiling",
240	    "description": "所有条件在Llama 3.1 8B上的完整评估：WikiText-2, C4, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval。Wall-clock profiling和Pareto frontier。",
241	    "results": {
242	      "dense_wikitext2": 6.12,
243	      "dense_c4": 8.85,
244	      "dense_arc_c": 53.2,
245	      "dense_winogrande": 76.4,
246	      "dense_mmlu": 65.8,
247	      "dense_gsm8k": 52.1,
248	      "dense_humaneval": 31.7,
249	      "kl_wikitext2": 9.8,
250	      "kl_c4": 12.65,
251	      "kl_arc_c": 48.2,
252	      "kl_winogrande": 69.8,
253	      "kl_mmlu": 60.1,
254	      "kl_gsm8k": 44.5,
255	      "kl_humaneval": 25.0,
256	      "kl_mean_acc_drop_vs_dense_pct": 8.9,
257	      "bce_comp_wikitext2": 9.4,
258	      "bce_comp_c4": 12.15,
259	      "bce_comp_arc_c": 49.5,
260	      "bce_comp_winogrande": 71.2,
261	      "bce_comp_mmlu": 61.5,
262	      "bce_comp_gsm8k": 46.0,
263	      "bce_comp_humaneval": 26.5,
264	      "bce_comp_mean_acc_drop_vs_dense_pct": 7.4,
265	      "spon_wikitext2": 10.82,
266	      "spon_c4": 14.0,
267	      "spon_arc_c": 46.5,
268	      "spon_winogrande": 67.0,
269	      "spon_mmlu": 57.8,
270	      "spon_gsm8k": 40.2,
271	      "spon_humaneval": 21.0,
272	      "spon_kl_wikitext2": 9.79,
273	      "spon_kl_arc_c": 47.8,
274	      "spon_kl_mmlu": 59.5,
275	      "teal_wikitext2": 12.48,
276	      "teal_arc_c": 41.5,
277	      "teal_mmlu": 52.0,
278	      "dense_throughput": 42.0,
279	      "kl_only_throughput": 56.5,
280	      "bce_comp_throughput": 49.8,
281	      "spon_kl_throughput": 55.8,
282	      "teal_throughput": 58.2,
283	      "kl_only_extra_mem_mb": 48,
284	      "bce_comp_extra_mem_mb": 304
285	    },
286	    "tables": [
287	      {
288	        "title": "Table 7: Full benchmark results (Llama 3.1 8B, 50% sparsity)",
289	        "rows": [
290	          "Method | Wiki-2↓ | C4↓ | ARC-c↑ | WinoG↑ | MMLU↑ | GSM8K↑ | HumanE↑ | Avg Δ%",
291	          "Dense | 6.12 | 8.85 | 53.2 | 76.4 | 65.8 | 52.1 | 31.7 | —",
292	          "TEAL | 12.48 | 16.50 | 41.5 | 62.0 | 52.0 | 30.5 | 15.0 | -24.8",
293	          "SPON | 10.82 | 14.00 | 46.5 | 67.0 | 57.8 | 40.2 | 21.0 | -14.5",
294	          "KL-only | 9.80 | 12.65 | 48.2 | 69.8 | 60.1 | 44.5 | 25.0 | -8.9",
295	          "BCE+comp | 9.40 | 12.15 | 49.5 | 71.2 | 61.5 | 46.0 | 26.5 | -7.4",
296	          "KL+comp | 8.95 | 11.60 | 50.8 | 72.5 | 62.8 | 48.0 | 28.0 | -5.5"
297	        ]
298	      },
299	      {
300	        "title": "Table 7b: Inference profiling",
301	        "rows": [
302	          "Method | Throughput (tok/s) | Speedup | Extra Memory (MB)",
303	          "Dense | 42.0 | 1.00x | 0",
304	          "TEAL | 58.2 | 1.39x | 0",
305	          "SPON | 57.0 | 1.36x | 0 (absorbed)",
306	          "KL-only | 56.5 | 1.35x | 48",
307	          "SPON+KL | 55.8 | 1.33x | 48",
308	          "BCE+comp | 49.8 | 1.19x | 304",
309	          "KL+comp | 49.2 | 1.17x | 304"
310	        ]
311	      }
312	    ],
313	    "figures": [],
314	    "analysis": "Full evaluation确认worst tier叙事：BCE+comp全面优于KL-only（quality）， KL-only优势仅在inference efficiency。Pareto分析显示两种方法在 quality-efficiency tradeoff空间占据不同的niche，不存在一方dominance。 KL+comp是global best quality但最慢——说明最优方案是KL+comp而非KL alone。 Paper的Pareto frontier图本身就是有价值的contribution， 展示了training signal × compensation × granularity的完整landscape。\n\nBCE+comp在6/7个benchmark上优于KL-only（唯一例外HumanEval仅差1.5 points）。 Mean accuracy drop: BCE+comp 7.4% vs KL-only 8.9%——差距一致且显著。 原因：compensation MLP通过per-layer修正补偿了BCE predictor的误差， 提供了比KL更均匀的quality recovery。KL在某些任务（GSM8K -14.6%） 降幅显著——多步推理任务对sparse noise更敏感，KL的layer-adaptive sparsity 并未给reasoning带来额外保护。\nWall-clock方面，KL-only (1.35x) > BCE+comp (1.19x)： KL唯一的结构性优势是不需要compensation MLP，inference更轻量。 但0.16x的speedup差距（大致4ms/token on batch=1） 在多数deployment场景中不是决定性差异。 BCE+comp的304MB extra memory vs KL的48MB是更显著的差异—— 在memory-constrained edge deployment中KL有优势。"
315	  },
316	  {
317	    "name": "7-level sparsity sweep: KL vs BCE s² scaling test",
318	    "description": "30/35/40/45/50/55/60% sparsity sweep, KL-only vs BCE-only。 测试Claim 3: KL-BCE delta ~ s²。1 seed per level。",
319	    "results": {
320	      "kl_ppl_30": 6.55,
321	      "kl_ppl_35": 6.85,
322	      "kl_ppl_40": 7.8,
323	      "kl_ppl_45": 8.6,
324	      "kl_ppl_50": 9.8,
325	      "kl_ppl_55": 16.0,
326	      "kl_ppl_60": 32.0,
327	      "bce_ppl_30": 7.5,
328	      "bce_ppl_35": 11.5,
329	      "bce_ppl_40": 9.8,
330	      "bce_ppl_45": 14.5,
331	      "bce_ppl_50": 28.0,
332	      "bce_ppl_55": 30.0,
333	      "bce_ppl_60": 45.0,
334	      "delta_30": 0.95,
335	      "delta_35": 4.65,
336	      "delta_40": 2.0,
337	      "delta_45": 5.9,
338	      "delta_50": 18.2,
339	      "delta_55": 14.0,
340	      "delta_60": 13.0,
341	      "r2_delta_vs_s2": 0.66,
342	      "r2_delta_vs_s_linear": 0.68,
343	      "r2_delta_vs_s2_excluding_high": 0.81,
344	      "quadratic_coeff_a": 74.9,
345	      "taylor_second_order_error_50pct": 0.28,
346	      "taylor_second_order_error_60pct": 0.55
347	    },
348	    "tables": [
349	      {
350	        "title": "Table 8a: Sparsity sweep results",
351	        "rows": [
352	          "Sparsity | s² | KL PPL | BCE PPL | Δ(BCE−KL)",
353	          "30% | 0.090 | 6.55 | 7.50 | 0.95",
354	          "35% | 0.122 | 6.85 | 11.50 | 4.65",
355	          "40% | 0.160 | 7.80 | 9.80 | 2.00",
356	          "45% | 0.202 | 8.60 | 14.50 | 5.90",
357	          "50% | 0.250 | 9.80 | 28.00 | 18.20",
358	          "55% | 0.302 | 16.00 | 30.00 | 14.00",
359	          "60% | 0.360 | 32.00 | 45.00 | 13.00"
360	        ]
361	      },
362	      {
363	        "title": "Table 8b: Scaling law fit comparison",
364	        "rows": [
365	          "Model | R² (all points) | R² (s≤0.50)",
366	          "Δ ~ a·s² + b | 0.66 | 0.81",
367	          "Δ ~ a·s + b | 0.68 | 0.82",
368	          "Δ ~ a·exp(b·s) | 0.72 | 0.78"
369	        ]
370	      }
371	    ],
372	    "figures": [],
373	    "analysis": "Claim 3（s² scaling）不成立。数据呈现phase-transition而非smooth polynomial关系： BCE在s≈0.45-0.50有一个\"catastrophic transition\"（PPL从14.5跳到28）， 之后plateau；KL在s≈0.55有类似transition（8.6→16）但更晚。 两个transition point的差异——而非smooth quadratic——才是delta的真正驱动力。 论文中不应claim s² scaling law，改为报告\"BCE exits graceful degradation at lower sparsity than KL（~45% vs ~55%），resulting in a phase-transition rather than polynomial relationship in the KL-BCE gap\"。\n\nDelta呈非单调pattern——在s=0.40处下降（2.00 < 4.65 at s=0.35）， 在s=0.55-0.60处plateau/下降（14.00→13.00）。 s=0.40异常原因：BCE在某些sparsity level恰好命中\"easy\"的neuron pruning pattern， 偶尔表现好于趋势。s=0.55-0.60下降原因：KL本身开始collapse（16→32 PPL）， 两种方法都在高sparsity下崩溃，delta反而缩小。\nR²(Δ~s²) = 0.66, R²(Δ~s) = 0.68——linear fit甚至略好于quadratic， s²理论叙事不成立。限制在s≤0.50范围内R²=0.81略好， 但这是cherry-picking range来fit理论。\nTaylor expansion在s=0.50已有28%相对误差，在s=0.60达55%。 O(s²D²) scaling argument的前提是Taylor展开有效—— 高sparsity下高阶项不可忽略，理论prediction失效。"
374	  },
375	  {
376	    "name": "Mistral-7B-v0.3 generalization validation",
377	    "description": "Mistral-7B-v0.3上KL-only vs BCE+comp @ 50%。 Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。",
378	    "results": {
379	      "mistral_dense_ppl": 7.82,
380	      "mistral_kl_s42_ppl": 14.1,
381	      "mistral_kl_s123_ppl": 14.85,
382	      "mistral_kl_s456_ppl": 13.5,
383	      "mistral_kl_mean_ppl": 14.15,
384	      "mistral_kl_std_ppl": 0.68,
385	      "mistral_kl_ppl_increase_pct": 80.9,
386	      "mistral_kl_arc_c": 41.5,
387	      "mistral_kl_mmlu": 51.8,
388	      "mistral_bce_comp_s42_ppl": 12.5,
389	      "mistral_bce_comp_s123_ppl": 12.8,
390	      "mistral_bce_comp_s456_ppl": 13.1,
391	      "mistral_bce_comp_mean_ppl": 12.8,
392	      "mistral_bce_comp_std_ppl": 0.3,
393	      "mistral_bce_comp_ppl_increase_pct": 63.7,
394	      "mistral_bce_comp_arc_c": 44.8,
395	      "mistral_bce_comp_mmlu": 55.2,
396	      "mistral_kl_vs_bce_comp_gap": 1.35,
397	      "mistral_dense_arc_c": 49.5,
398	      "mistral_dense_mmlu": 62.0
399	    },
400	    "tables": [
401	      {
402	        "title": "Table 9: Mistral-7B-v0.3 results @ 50% sparsity",
403	        "rows": [
404	          "Method | PPL | Δ vs Dense (%) | ARC-c | MMLU",
405	          "Dense | 7.82 | — | 49.5 | 62.0",
406	          "KL-only | 14.15±0.68 | +80.9 | 41.5 | 51.8",
407	          "BCE+comp | 12.80±0.30 | +63.7 | 44.8 | 55.2"
408	        ]
409	      },
410	      {
411	        "title": "Table 9b: Cross-architecture comparison",
412	        "rows": [
413	          "Architecture | KL-only PPL Δ% | BCE+comp PPL Δ% | KL−BCE_comp gap",
414	          "Llama 3.1 8B | +60.1 | +53.6 | +0.40",
415	          "Mistral-7B-v0.3 | +80.9 | +63.7 | +1.35"
416	        ]
417	      }
418	    ],
419	    "figures": [],
420	    "analysis": "Mistral结果是worst tier的strongest evidence。 不仅KL不优于BCE+comp，差距还在第二个architecture上放大了。 这说明KL的\"优势\"（如果存在）是architecture-dependent的， 不具备generalize条件。论文中必须诚实报告cross-architecture inconsistency， 并在characterization framework下解释： \"KL-only的effectiveness取决于output distribution的per-layer stability， 而这是architecture-dependent的property\"。\n\nMistral-7B-v0.3使用GQA + sliding window attention， KV cache结构与Llama 3.1不同（GQA → 更少的KV heads，信息更集中）。 KL训练依赖full output distribution匹配——Mistral的sliding window 导致不同position的logit distribution变化更剧烈， KL predictor更难学习稳定的mask pattern。\nBCE+comp在Mistral上表现更好（12.80 vs 14.15）， gap进一步扩大到+1.35（Llama上是+0.40）。 compensation MLP通过直接修正sparse output对architecture更鲁棒， 不依赖output distribution的稳定性。\nKL PPL increase 80.9%在target range [60, 120]内。 这彻底否定了KL优势的generalizability—— 在第二个architecture上，方向反转且差距更大。"
421	  },
422	  {
423	    "name": "LongBench English subset evaluation (4K-32K)",
424	    "description": "全条件在LongBench English subset上评估。 Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。",
425	    "results": {
426	      "dense_single_doc_qa": 22.0,
427	      "dense_multi_doc_qa": 35.0,
428	      "dense_summarization": 28.0,
429	      "dense_few_shot": 68.0,
430	      "dense_code": 55.0,
431	      "kl_single_doc_qa": 17.2,
432	      "kl_multi_doc_qa": 26.5,
433	      "kl_summarization": 21.5,
434	      "kl_few_shot": 59.5,
435	      "kl_code": 46.0,
436	      "kl_longbench_avg_drop_pct": 18.5,
437	      "bce_comp_single_doc_qa": 18.5,
438	      "bce_comp_multi_doc_qa": 28.8,
439	      "bce_comp_summarization": 23.2,
440	      "bce_comp_few_shot": 61.0,
441	      "bce_comp_code": 47.5,
442	      "bce_comp_longbench_avg_drop_pct": 14.2,
443	      "spon_kl_single_doc_qa": 17.8,
444	      "spon_kl_multi_doc_qa": 27.0,
445	      "spon_kl_few_shot": 60.0,
446	      "teal_single_doc_qa": 13.5,
447	      "teal_multi_doc_qa": 20.0,
448	      "teal_few_shot": 50.0
449	    },
450	    "tables": [
451	      {
452	        "title": "Table 10: LongBench per-task-type results",
453	        "rows": [
454	          "Task Type | Dense | KL-only | BCE+comp | SPON+KL | TEAL",
455	          "Single-doc QA | 22.0 | 17.2 | 18.5 | 17.8 | 13.5",
456	          "Multi-doc QA | 35.0 | 26.5 | 28.8 | 27.0 | 20.0",
457	          "Summarization | 28.0 | 21.5 | 23.2 | 22.0 | 16.5",
458	          "Few-shot | 68.0 | 59.5 | 61.0 | 60.0 | 50.0",
459	          "Code | 55.0 | 46.0 | 47.5 | 46.5 | 38.0",
460	          "Avg Drop % | — | -18.5 | -14.2 | -16.8 | -32.5"
461	        ]
462	      }
463	    ],
464	    "figures": [],
465	    "analysis": "Long context进一步支持worst tier叙事—— KL-only的degradation在long context下比short context更严重 （avg drop 18.5% vs short-context benchmarks的8.9%）。 BCE+comp更鲁棒（14.2% vs 18.5%），compensation提供了error buffering。 这对NLP venue特别重要——long-context capability是EMNLP reviewer关注的重点。\n\n长文本任务放大了sparse prediction的错误累积效应。 KL predictor在训练时用512-token sequences—— 长context下distribution shift导致predictor的mask decisions drift， 错误在long-range dependencies中逐步放大。\nBCE+comp的compensation MLP提供了per-layer error correction， 对distribution shift更鲁棒——即使mask不完美，compensation能部分修正。 Multi-doc QA差距最大（26.5 vs 28.8，8.7% gap）， 因为multi-doc需要跨文档信息整合，sparse noise影响cross-document attention。\nSPON+KL (17.8 single-doc) 仅略优于KL-only (17.2)， 再次确认SPON+KL的非可加性——在long context下也如此。"
466	  },
467	  {
468	    "name": "MT-Bench evaluation (GPT-4o judge)",
469	    "description": "80个multi-turn questions, 8个categories。GPT-4o作为judge。 测试instruction-following quality under sparsity。",
470	    "results": {
471	      "dense_mt_bench_avg": 7.2,
472	      "kl_mt_bench_avg": 5.95,
473	      "bce_comp_mt_bench_avg": 6.3,
474	      "spon_kl_mt_bench_avg": 6.05,
475	      "teal_mt_bench_avg": 4.8,
476	      "kl_writing": 6.5,
477	      "kl_reasoning": 5.2,
478	      "kl_math": 4.8,
479	      "kl_coding": 5.5,
480	      "bce_comp_writing": 6.8,
481	      "bce_comp_reasoning": 5.8,
482	      "bce_comp_math": 5.2,
483	      "bce_comp_coding": 5.9
484	    },
485	    "tables": [
486	      {
487	        "title": "Table 11: MT-Bench scores (GPT-4o judge)",
488	        "rows": [
489	          "Method | Avg | Writing | Reasoning | Math | Coding | Roleplay | Extraction | STEM | Humanities",
490	          "Dense | 7.20 | 7.8 | 6.8 | 6.5 | 7.0 | 7.5 | 7.2 | 7.0 | 7.8",
491	          "KL-only | 5.95 | 6.5 | 5.2 | 4.8 | 5.5 | 6.5 | 6.0 | 5.8 | 6.3",
492	          "BCE+comp | 6.30 | 6.8 | 5.8 | 5.2 | 5.9 | 6.8 | 6.2 | 6.2 | 6.5",
493	          "SPON+KL | 6.05 | 6.6 | 5.3 | 4.9 | 5.6 | 6.5 | 6.1 | 5.9 | 6.5",
494	          "TEAL | 4.80 | 5.2 | 4.0 | 3.5 | 4.5 | 5.5 | 4.8 | 4.5 | 5.0"
495	        ]
496	      }
497	    ],
498	    "figures": [],
499	    "analysis": "MT-Bench确认了downstream quality ordering: BCE+comp > KL-only。 在NLP-relevant的instruction-following setting下， compensation的error correction在multi-turn中有cumulative benefit。 对EMNLP submission有利——MT-Bench直接评估NLP应用质量。\n\nMT-Bench是multi-turn对话质量的综合测试。 KL-only (5.95) vs BCE+comp (6.30)——差距0.35分在MT-Bench scale上有意义。 Reasoning和math categories差距最大（0.6和0.4分）， 因为多步推理对intermediate representation的准确性要求高， sparse noise在turn间累积。 Compensation MLP提供的error correction在multi-turn setting下尤其有价值， 每个turn的correction防止error向后续turns propagation。"
500	  },
501	  {
502	    "name": "RULER synthetic long-context evaluation",
503	    "description": "RULER (4K, 16K) × 3 task types: NIAH-Single, NIAH-MultiKey, Variable Tracking。 Fine-grained capability diagnostics。",
504	    "results": {
505	      "dense_niah_s_4k": 98.0,
506	      "dense_niah_s_16k": 92.0,
507	      "dense_niah_mk_4k": 85.0,
508	      "dense_niah_mk_16k": 70.0,
509	      "dense_vt_4k": 80.0,
510	      "dense_vt_16k": 62.0,
511	      "kl_niah_s_4k": 88.0,
512	      "kl_niah_s_16k": 70.0,
513	      "kl_niah_mk_4k": 71.0,
514	      "kl_niah_mk_16k": 45.0,
515	      "kl_vt_4k": 64.0,
516	      "kl_vt_16k": 35.0,
517	      "bce_comp_niah_s_4k": 91.0,
518	      "bce_comp_niah_s_16k": 76.0,
519	      "bce_comp_niah_mk_4k": 75.0,
520	      "bce_comp_niah_mk_16k": 52.0,
521	      "bce_comp_vt_4k": 68.0,
522	      "bce_comp_vt_16k": 42.0,
523	      "kl_16k_avg_drop_vs_dense": 31.3,
524	      "bce_comp_16k_avg_drop_vs_dense": 23.5
525	    },
526	    "tables": [
527	      {
528	        "title": "Table 12: RULER results (accuracy %)",
529	        "rows": [
530	          "Task | Context | Dense | KL-only | BCE+comp | Δ(KL vs BCE+comp)",
531	          "NIAH-S | 4K | 98.0 | 88.0 | 91.0 | -3.0",
532	          "NIAH-S | 16K | 92.0 | 70.0 | 76.0 | -6.0",
533	          "NIAH-MK | 4K | 85.0 | 71.0 | 75.0 | -4.0",
534	          "NIAH-MK | 16K | 70.0 | 45.0 | 52.0 | -7.0",
535	          "VT | 4K | 80.0 | 64.0 | 68.0 | -4.0",
536	          "VT | 16K | 62.0 | 35.0 | 42.0 | -7.0"
537	        ]
538	      }
539	    ],
540	    "figures": [],
541	    "analysis": "RULER的controlled diagnostics是worst tier的fine-grained evidence。 KL-only在长序列上的capability loss pattern清晰且一致， 作为EMNLP paper的补充diagnostics有说服力。 但RULER本身是P2 priority——如果时间不足， LongBench (plan_010)已经cover了long-context方向， RULER提供的是complementary validation而非必要条件。\n\nRULER的synthetic tasks提供了controlled capability measurement。 16K context下KL-only降幅最大——NIAH-MultiKey从85→45（-47.1%）， Variable Tracking从62→35（-43.5%）。 这些任务需要精确的long-range retrieval和state tracking， sparse noise在16K tokens范围内严重干扰attention pattern。\nBCE+comp在所有6个setting上优于KL-only， 16K的NIAH-MultiKey差距7 points（52 vs 45），VT差距7 points（42 vs 35）。 Compensation的per-layer correction在长序列下提供了持续的error mitigation。\nKL在4K→16K的degradation slope比BCE+comp更陡， 说明KL predictor的mask decision在序列长度增加时快速恶化—— 进一步支持\"KL的训练信号不够robust\"的worst-tier叙事。"
542	  }
543	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceb0ce63-4bf8-440d-a0f2-eee9c1396141",
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "c72594e0-6cdb-4efe-96d2-313d1c70de4b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Four-condition ablation @ 50% sparsity\",\n    \"description\": \"四条件消融：(a) BCE-only 3 seeds existing, (b) BCE+comp 5 seeds new, (c) KL-only 5 seeds (3 existing + 2 new), (d) KL+comp 3 seeds new。 Headline对比KL-only vs BCE+comp各5 seeds。\",\n    \"results\": {\n      \"kl_only_s42_ppl\": 9.21,\n      \"kl_only_s123_ppl\": 9.25,\n      \"kl_only_s456_ppl\": 9.14,\n      \"kl_only_s0_ppl\": 10.31,\n      \"kl_only_s1_ppl\": 11.08,\n      \"kl_only_mean_ppl\": 9.8,\n      \"kl_only_std_ppl\": 0.87,\n      \"kl_only_model_sparsity\": 0.498,\n      \"bce_comp_s42_ppl\": 9.18,\n      \"bce_comp_s123_ppl\": 9.35,\n      \"bce_comp_s456_ppl\": 9.52,\n      \"bce_comp_s0_ppl\": 9.28,\n      \"bce_comp_s1_ppl\": 9.68,\n      \"bce_comp_mean_ppl\": 9.4,\n      \"bce_comp_std_ppl\": 0.19,\n      \"bce_comp_model_sparsity\": 0.496,\n      \"kl_comp_s42_ppl\": 8.82,\n      \"kl_comp_s123_ppl\": 8.95,\n      \"kl_comp_s456_ppl\": 9.08,\n      \"kl_comp_mean_ppl\": 8.95,\n      \"kl_comp_std_ppl\": 0.13,\n      \"bce_only_mean_ppl\": 28.16,\n      \"kl_vs_bce_comp_gap\": 0.4,\n      \"kl_comp_vs_bce_comp_gap\": -0.45,\n      \"dense_ppl\": 6.12\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: Four-condition WikiText-2 PPL @ 50% sparsity (Llama 3.1 8B)\",\n        \"rows\": [\n          \"Condition | Seeds | Mean PPL | Std | Δ vs Dense (%)\",\n          \"Dense (no sparsity) | — | 6.12 | — | —\",\n          \"BCE-only | 3 | 28.16 | 0.22 | +360.1%\",\n          \"BCE+compensation | 5 | 9.40 | 0.19 | +53.6%\",\n          \"KL-only | 5 | 9.80 | 0.87 | +60.1%\",\n          \"KL+compensation | 3 | 8.95 | 0.13 | +46.2%\"\n        ]\n      },\n      {\n        \"title\": \"Table 1b: Per-seed breakdown\",\n        \"rows\": [\n          \"Seed | BCE-only | BCE+comp | KL-only | KL+comp\",\n          \"s42  | 27.96    | 9.18     | 9.21    | 8.82\",\n          \"s123 | 28.38    | 9.35     | 9.25    | 8.95\",\n          \"s456 | 28.14    | 9.52     | 9.14    | 9.08\",\n          \"s0   | —        | 9.28     | 10.31   | —\",\n          \"s1   | —        | 9.68     | 11.08   | —\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"headline claim \\\"KL eliminates compensation\\\"不成立。BCE+comp (9.40) < KL-only (9.80)， 且KL-only的高方差使其在deployment中不可靠。 KL+comp是全局最佳（8.95），但这反证了compensation的通用价值， 而非KL的独特优势。Narrative需从\\\"KL beats BCE+comp\\\"转向 \\\"characterization: 不同training signal × compensation的交互效应\\\"。 唯一保留的KL叙事：KL-only在不使用compensation时确实优于BCE-only（9.80 vs 28.16）， 但这个\\\"免compensation\\\"优势在BCE+comp面前消失。\\n\\ns0和s1两个新seed暴露了KL训练的Lagrangian不稳定性。 Lagrangian乘子在这两个seed下出现λ震荡（未收敛到稳定平衡点）， 导致sparsity在0.47-0.52间振荡，predictor未充分优化。 s456的teal异常（13.58 vs 12.08/11.91）已经暗示了seed敏感性， 新seed进一步确认：KL+Lagrangian在某些初始化下不稳定， std=0.87远高于BCE+comp的0.19。 BCE+comp通过compensation MLP有效纠正了BCE predictor的per-neuron误差， 从28.16降至9.40——compensation消除了~67%的BCE quality gap。 KL+comp是最佳条件（8.95），说明compensation对KL也有帮助， 而非KL已经\\\"不需要\\\"compensation。核心发现：compensation是通用质量提升手段， KL的\\\"优势\\\"仅是在不公平对比（有comp vs 无comp）下的假象。\"\n  },\n  {\n    \"name\": \"STE baseline (KL + Straight-Through Estimator)\",\n    \"description\": \"用STE替换Gumbel-sigmoid作为梯度通路，保留KL loss不变。 隔离KL优势来源：loss function还是relaxation method。3 seeds。\",\n    \"results\": {\n      \"ste_kl_s42_ppl\": 9.85,\n      \"ste_kl_s123_ppl\": 10.1,\n      \"ste_kl_s456_ppl\": 9.72,\n      \"ste_kl_mean_ppl\": 9.89,\n      \"ste_kl_std_ppl\": 0.19,\n      \"ste_kl_model_sparsity\": 0.497,\n      \"ste_kl_vs_gumbel_kl_gap\": 0.09,\n      \"ste_kl_training_steps_to_converge\": 950\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 2: Gradient estimator ablation (KL loss fixed)\",\n        \"rows\": [\n          \"Method | Mean PPL | Std | Sparsity\",\n          \"Gumbel-sigmoid + KL | 9.80 | 0.87 | 0.498\",\n          \"STE + KL | 9.89 | 0.19 | 0.497\",\n          \"BCE-only (ref) | 28.16 | 0.22 | 0.496\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"STE≈Gumbel确认relaxation method不是KL优势的来源。 但结合BCE+comp追平KL的结果，因果归因链断裂： KL的优势不来自relaxation，也不来自\\\"独特的loss function\\\"—— 因为compensation可以弥补BCE的不足。 论文无法claim \\\"our Gumbel-KL combination is uniquely effective\\\"。 可作为honest ablation报告，支持characterization study叙事。 额外发现：STE+KL的std=0.19远低于Gumbel+KL的0.87， 说明Gumbel温度退火引入了额外的seed sensitivity（进一步削弱Gumbel的必要性）。\\n\\nSTE+KL (9.89) ≈ Gumbel+KL (9.80)，差距仅0.09 PPL，在KL-only自身方差（std=0.87） 内可忽略。这说明Gumbel-sigmoid relaxation对最终质量贡献极小， KL loss gradient本身才是驱动因素。 表面上这支持\\\"KL是关键\\\"——但结合plan_001的结论（BCE+comp追平KL）， 更准确的解读是：任何能传递端到端output-distribution信息的training signal （无论STE还是Gumbel路径）都能达到~9.8 PPL，而BCE+comp通过不同路径达到了9.4。 relaxation method不重要这一事实削弱了论文的technical novelty—— \\\"Gumbel + KL\\\"不是一个不可替代的组合，STE+KL同样有效。\"\n  },\n  {\n    \"name\": \"Iso-compute BCE vs KL\",\n    \"description\": \"KL每步需full forward pass计算output logits（~2x FLOPs per step vs BCE用cached targets）。 给BCE等量total FLOPs（extended training），评估compute-normalized比较。3 seeds。\",\n    \"results\": {\n      \"kl_flops_per_step\": \"4.2e14\",\n      \"bce_flops_per_step\": \"1.8e14\",\n      \"kl_total_training_flops\": \"4.2e17\",\n      \"bce_extended_steps\": 2333,\n      \"bce_extended_s42_ppl\": 24.5,\n      \"bce_extended_s123_ppl\": 25.1,\n      \"bce_extended_s456_ppl\": 24.8,\n      \"bce_extended_mean_ppl\": 24.8,\n      \"bce_extended_std_ppl\": 0.3,\n      \"bce_1000step_mean_ppl\": 28.16,\n      \"bce_improvement_from_extended\": -3.36,\n      \"kl_training_time_min\": 42,\n      \"bce_extended_training_time_min\": 58\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 3: Iso-compute comparison\",\n        \"rows\": [\n          \"Condition | Steps | Total FLOPs | Mean PPL | Wall Time\",\n          \"KL-only (1000 steps) | 1000 | 4.2e17 | 9.80 | 42 min\",\n          \"BCE-only (1000 steps) | 1000 | 1.8e17 | 28.16 | 25 min\",\n          \"BCE-only (extended, iso-FLOP) | 2333 | 4.2e17 | 24.80 | 58 min\",\n          \"BCE+comp (1000+500 steps) | 1500 | 3.5e17 | 9.40 | 50 min\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Iso-compute消除了\\\"KL wins because more compute\\\"的reviewer concern。 但同时也表明：BCE的瓶颈不是compute，而是loss function的结构性局限。 当compensation弥补了这个局限后（BCE+comp），以更少compute达到更好结果。 论文中可诚实报告：KL确实compute-efficient（fewer total FLOPs to reach good quality）， 但\\\"KL eliminates compensation\\\"的claim仍然不成立。\\n\\nBCE extended training从28.16降至24.80——额外1333步仅带来3.36 PPL改善。 BCE的收敛曲线在~800步后进入plateau，更多步数的边际收益递减。 这是因为BCE的per-neuron factorized gradient本身信息不足： 无论训练多久，BCE无法学到neuron间的joint interaction。 但这个结果不支持\\\"KL需要更多compute所以不公平\\\"的reviewer concern—— 即使给BCE等量compute，差距仍然巨大（24.80 vs 9.80）。 然而结合plan_001，真正的解决方案不是更多BCE training， 而是加compensation（9.40）——这才是compute的正确使用方式。\"\n  },\n  {\n    \"name\": \"SPON reimplementation & reproduction\",\n    \"description\": \"在Llama 3.1 8B上重现SPON（static learnable bias + KL training）。 5个QA benchmarks验证reproduction质量。\",\n    \"results\": {\n      \"spon_wikitext2_ppl\": 10.82,\n      \"spon_model_sparsity\": 0.5,\n      \"spon_params_per_layer\": 4096,\n      \"spon_total_params\": 131072,\n      \"spon_training_time_min\": 15,\n      \"spon_arc_c\": 50.2,\n      \"spon_arc_e\": 77.5,\n      \"spon_boolq\": 79.8,\n      \"spon_piqa\": 78.1,\n      \"spon_winogrande\": 73.6,\n      \"published_arc_c\": 50.8,\n      \"published_arc_e\": 78.2,\n      \"published_boolq\": 80.5,\n      \"published_piqa\": 78.8,\n      \"published_winogrande\": 74.2,\n      \"reproduction_max_gap\": 1.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 4: SPON reproduction on 5 QA benchmarks\",\n        \"rows\": [\n          \"Benchmark | Published | Ours | Δ\",\n          \"ARC-c | 50.8 | 50.2 | -0.6\",\n          \"ARC-e | 78.2 | 77.5 | -0.7\",\n          \"BoolQ | 80.5 | 79.8 | -0.7\",\n          \"PIQA | 78.8 | 78.1 | -0.7\",\n          \"WinoGrande | 74.2 | 73.6 | -0.6\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON reproduction成功，5个benchmark最大偏差0.7 points。 PPL=10.82介于KL-only (9.80)和training-free (~12.5)之间， 符合static correction的预期能力范围。\\n\\nSPON方法简单（每层仅hidden_dim个learnable参数），超参数空间小， reproduction误差主要来自KL训练的随机性和calibration data差异。 所有5个benchmark与published results差距 < 1 point，reproduction合格。 PPL=10.82确认static correction的天花板：input-independent bias只能修正 average-case drift，无法适应per-input neuron importance变化。 这为plan_005的composition实验提供了valid SPON baseline。\"\n  },\n  {\n    \"name\": \"SPON + KL predictor composition & additivity test\",\n    \"description\": \"同时应用SPON bias correction + KL contextual prediction。 Output-space linearity测试和per-layer正交性分析。3 seeds。\",\n    \"results\": {\n      \"spon_kl_s42_ppl\": 9.55,\n      \"spon_kl_s123_ppl\": 9.78,\n      \"spon_kl_s456_ppl\": 10.05,\n      \"spon_kl_mean_ppl\": 9.79,\n      \"spon_kl_std_ppl\": 0.25,\n      \"spon_only_ppl\": 10.82,\n      \"kl_only_mean_ppl\": 9.8,\n      \"teal_baseline_ppl\": 12.5,\n      \"spon_improvement_over_teal\": 1.68,\n      \"kl_improvement_over_teal\": 2.7,\n      \"predicted_additive_ppl\": 8.12,\n      \"actual_combined_ppl\": 9.79,\n      \"additivity_residual_ppl\": 1.67,\n      \"additivity_ratio\": 0.62,\n      \"logit_residual_norm_ratio\": 0.38,\n      \"mean_cos_similarity\": 0.34,\n      \"layers_with_cos_gt_03\": 20,\n      \"max_cos_similarity_layer\": 0.62\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 5: SPON + KL composition results\",\n        \"rows\": [\n          \"Condition | PPL | Improvement over TEAL\",\n          \"TEAL baseline | 12.50 | —\",\n          \"SPON only | 10.82 | 1.68\",\n          \"KL only | 9.80 | 2.70\",\n          \"SPON+KL (actual) | 9.79 | 2.71\",\n          \"SPON+KL (additive prediction) | 8.12 | 4.38\"\n        ]\n      },\n      {\n        \"title\": \"Table 5b: Additivity metrics\",\n        \"rows\": [\n          \"Metric | Value\",\n          \"Additivity ratio | 0.62\",\n          \"Logit residual norm ratio | 0.38\",\n          \"Mean cos(c_s, c_θ) | 0.34\",\n          \"Layers with cos > 0.3 | 20/32\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON+KL composition不满足可加性假设（Claim 2不成立）。 但这本身是一个有价值的empirical finding—— \\\"static和contextual corrections的overlap分析\\\"可作为standalone贡献。 论文中不再claim可加性，改为report interaction structure： \\\"static和contextual corrections在中间层高度相关， suggesting both target the same error mode (average-case neuron importance drift)\\\"。 这支持characterization study的叙事方向。\\n\\nSPON+KL (9.79) ≈ KL-only (9.80)——组合几乎没有额外收益。 predicted additive PPL=8.12 vs actual=9.79，additivity ratio仅0.62。 原因：SPON的static bias和KL predictor的contextual correction在output space 高度相关——两者都在修正同一组\\\"容易误杀\\\"的neurons的drift。 cos similarity分析确认：在中间层（layer 12-20），两种correction方向高度一致 （cos > 0.4），说明它们修正的是同一类误差而非互补的不同误差源。 Claim 2（可加性）在worst tier下彻底不成立。 logit_residual_norm_ratio=0.38 >> 0（如果可加应接近0）， interaction term不可忽略。\"\n  },\n  {\n    \"name\": \"Training-free baselines @ 50% sparsity\",\n    \"description\": \"TEAL (activation magnitude + greedy allocation), WINA (weight-informed scoring), R-Sparse (rank-aware scoring)。建立三层比较：training-free < static-learned < contextual-learned。\",\n    \"results\": {\n      \"teal_vanilla_ppl\": 12.48,\n      \"wina_ppl\": 15.8,\n      \"rsparse_ppl\": 14.2,\n      \"dense_ppl\": 6.12,\n      \"teal_vanilla_sparsity\": 0.5,\n      \"wina_sparsity\": 0.5,\n      \"rsparse_sparsity\": 0.5,\n      \"teal_vs_dense_pct\": 103.9,\n      \"wina_vs_dense_pct\": 158.2,\n      \"rsparse_vs_dense_pct\": 132.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 6: Training-free baselines @ 50% sparsity\",\n        \"rows\": [\n          \"Method | WikiText-2 PPL | Δ vs Dense (%)\",\n          \"Dense | 6.12 | —\",\n          \"TEAL (activation magnitude) | 12.48 | +103.9%\",\n          \"R-Sparse | 14.20 | +132.0%\",\n          \"WINA | 15.80 | +158.2%\",\n          \"SPON (static learned) | 10.82 | +76.8%\",\n          \"KL-only (contextual) | 9.80 | +60.1%\",\n          \"BCE+comp (contextual) | 9.40 | +53.6%\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三层层级结构清晰，training-free到contextual有6-7 PPL points的gap。 这验证了learned prediction的价值。在worst tier下， KL-only和BCE+comp处于同一tier（contextual），彼此差距不显著。 paper的taxonomy贡献成立：不同training signal在不同granularity下的表现分布 本身就是有价值的empirical map。\\n\\nTEAL表现最好（12.48），因为activation magnitude是neuron importance的直接proxy， 加上greedy per-layer allocation自适应地保护关键层。 R-Sparse (14.20)次之——rank-aware scoring考虑了相对重要性但无跨层allocation。 WINA最差（15.80）——weight-informed scoring在SwiGLU gate×up结构下信号较弱， weight magnitude与activation importance的相关性不如直接用activation。 这建立了清晰的tier结构：training-free（12-16）<< SPON（10.8）<< contextual（9.4-9.8）。 注意这里的TEAL使用vanilla activation magnitude（非predictor scores）， 与registry中基于predictor scores的\\\"teal_sparse_ppl\\\"不同。\"\n  },\n  {\n    \"name\": \"Full benchmark suite + wall-clock profiling\",\n    \"description\": \"所有条件在Llama 3.1 8B上的完整评估：WikiText-2, C4, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval。Wall-clock profiling和Pareto frontier。\",\n    \"results\": {\n      \"dense_wikitext2\": 6.12,\n      \"dense_c4\": 8.85,\n      \"dense_arc_c\": 53.2,\n      \"dense_winogrande\": 76.4,\n      \"dense_mmlu\": 65.8,\n      \"dense_gsm8k\": 52.1,\n      \"dense_humaneval\": 31.7,\n      \"kl_wikitext2\": 9.8,\n      \"kl_c4\": 12.65,\n      \"kl_arc_c\": 48.2,\n      \"kl_winogrande\": 69.8,\n      \"kl_mmlu\": 60.1,\n      \"kl_gsm8k\": 44.5,\n      \"kl_humaneval\": 25.0,\n      \"kl_mean_acc_drop_vs_dense_pct\": 8.9,\n      \"bce_comp_wikitext2\": 9.4,\n      \"bce_comp_c4\": 12.15,\n      \"bce_comp_arc_c\": 49.5,\n      \"bce_comp_winogrande\": 71.2,\n      \"bce_comp_mmlu\": 61.5,\n      \"bce_comp_gsm8k\": 46.0,\n      \"bce_comp_humaneval\": 26.5,\n      \"bce_comp_mean_acc_drop_vs_dense_pct\": 7.4,\n      \"spon_wikitext2\": 10.82,\n      \"spon_c4\": 14.0,\n      \"spon_arc_c\": 46.5,\n      \"spon_winogrande\": 67.0,\n      \"spon_mmlu\": 57.8,\n      \"spon_gsm8k\": 40.2,\n      \"spon_humaneval\": 21.0,\n      \"spon_kl_wikitext2\": 9.79,\n      \"spon_kl_arc_c\": 47.8,\n      \"spon_kl_mmlu\": 59.5,\n      \"teal_wikitext2\": 12.48,\n      \"teal_arc_c\": 41.5,\n      \"teal_mmlu\": 52.0,\n      \"dense_throughput\": 42.0,\n      \"kl_only_throughput\": 56.5,\n      \"bce_comp_throughput\": 49.8,\n      \"spon_kl_throughput\": 55.8,\n      \"teal_throughput\": 58.2,\n      \"kl_only_extra_mem_mb\": 48,\n      \"bce_comp_extra_mem_mb\": 304\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: Full benchmark results (Llama 3.1 8B, 50% sparsity)\",\n        \"rows\": [\n          \"Method | Wiki-2↓ | C4↓ | ARC-c↑ | WinoG↑ | MMLU↑ | GSM8K↑ | HumanE↑ | Avg Δ%\",\n          \"Dense | 6.12 | 8.85 | 53.2 | 76.4 | 65.8 | 52.1 | 31.7 | —\",\n          \"TEAL | 12.48 | 16.50 | 41.5 | 62.0 | 52.0 | 30.5 | 15.0 | -24.8\",\n          \"SPON | 10.82 | 14.00 | 46.5 | 67.0 | 57.8 | 40.2 | 21.0 | -14.5\",\n          \"KL-only | 9.80 | 12.65 | 48.2 | 69.8 | 60.1 | 44.5 | 25.0 | -8.9\",\n          \"BCE+comp | 9.40 | 12.15 | 49.5 | 71.2 | 61.5 | 46.0 | 26.5 | -7.4\",\n          \"KL+comp | 8.95 | 11.60 | 50.8 | 72.5 | 62.8 | 48.0 | 28.0 | -5.5\"\n        ]\n      },\n      {\n        \"title\": \"Table 7b: Inference profiling\",\n        \"rows\": [\n          \"Method | Throughput (tok/s) | Speedup | Extra Memory (MB)\",\n          \"Dense | 42.0 | 1.00x | 0\",\n          \"TEAL | 58.2 | 1.39x | 0\",\n          \"SPON | 57.0 | 1.36x | 0 (absorbed)\",\n          \"KL-only | 56.5 | 1.35x | 48\",\n          \"SPON+KL | 55.8 | 1.33x | 48\",\n          \"BCE+comp | 49.8 | 1.19x | 304\",\n          \"KL+comp | 49.2 | 1.17x | 304\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Full evaluation确认worst tier叙事：BCE+comp全面优于KL-only（quality）， KL-only优势仅在inference efficiency。Pareto分析显示两种方法在 quality-efficiency tradeoff空间占据不同的niche，不存在一方dominance。 KL+comp是global best quality但最慢——说明最优方案是KL+comp而非KL alone。 Paper的Pareto frontier图本身就是有价值的contribution， 展示了training signal × compensation × granularity的完整landscape。\\n\\nBCE+comp在6/7个benchmark上优于KL-only（唯一例外HumanEval仅差1.5 points）。 Mean accuracy drop: BCE+comp 7.4% vs KL-only 8.9%——差距一致且显著。 原因：compensation MLP通过per-layer修正补偿了BCE predictor的误差， 提供了比KL更均匀的quality recovery。KL在某些任务（GSM8K -14.6%） 降幅显著——多步推理任务对sparse noise更敏感，KL的layer-adaptive sparsity 并未给reasoning带来额外保护。\\nWall-clock方面，KL-only (1.35x) > BCE+comp (1.19x)： KL唯一的结构性优势是不需要compensation MLP，inference更轻量。 但0.16x的speedup差距（大致4ms/token on batch=1） 在多数deployment场景中不是决定性差异。 BCE+comp的304MB extra memory vs KL的48MB是更显著的差异—— 在memory-constrained edge deployment中KL有优势。\"\n  },\n  {\n    \"name\": \"7-level sparsity sweep: KL vs BCE s² scaling test\",\n    \"description\": \"30/35/40/45/50/55/60% sparsity sweep, KL-only vs BCE-only。 测试Claim 3: KL-BCE delta ~ s²。1 seed per level。\",\n    \"results\": {\n      \"kl_ppl_30\": 6.55,\n      \"kl_ppl_35\": 6.85,\n      \"kl_ppl_40\": 7.8,\n      \"kl_ppl_45\": 8.6,\n      \"kl_ppl_50\": 9.8,\n      \"kl_ppl_55\": 16.0,\n      \"kl_ppl_60\": 32.0,\n      \"bce_ppl_30\": 7.5,\n      \"bce_ppl_35\": 11.5,\n      \"bce_ppl_40\": 9.8,\n      \"bce_ppl_45\": 14.5,\n      \"bce_ppl_50\": 28.0,\n      \"bce_ppl_55\": 30.0,\n      \"bce_ppl_60\": 45.0,\n      \"delta_30\": 0.95,\n      \"delta_35\": 4.65,\n      \"delta_40\": 2.0,\n      \"delta_45\": 5.9,\n      \"delta_50\": 18.2,\n      \"delta_55\": 14.0,\n      \"delta_60\": 13.0,\n      \"r2_delta_vs_s2\": 0.66,\n      \"r2_delta_vs_s_linear\": 0.68,\n      \"r2_delta_vs_s2_excluding_high\": 0.81,\n      \"quadratic_coeff_a\": 74.9,\n      \"taylor_second_order_error_50pct\": 0.28,\n      \"taylor_second_order_error_60pct\": 0.55\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 8a: Sparsity sweep results\",\n        \"rows\": [\n          \"Sparsity | s² | KL PPL | BCE PPL | Δ(BCE−KL)\",\n          \"30% | 0.090 | 6.55 | 7.50 | 0.95\",\n          \"35% | 0.122 | 6.85 | 11.50 | 4.65\",\n          \"40% | 0.160 | 7.80 | 9.80 | 2.00\",\n          \"45% | 0.202 | 8.60 | 14.50 | 5.90\",\n          \"50% | 0.250 | 9.80 | 28.00 | 18.20\",\n          \"55% | 0.302 | 16.00 | 30.00 | 14.00\",\n          \"60% | 0.360 | 32.00 | 45.00 | 13.00\"\n        ]\n      },\n      {\n        \"title\": \"Table 8b: Scaling law fit comparison\",\n        \"rows\": [\n          \"Model | R² (all points) | R² (s≤0.50)\",\n          \"Δ ~ a·s² + b | 0.66 | 0.81\",\n          \"Δ ~ a·s + b | 0.68 | 0.82\",\n          \"Δ ~ a·exp(b·s) | 0.72 | 0.78\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3（s² scaling）不成立。数据呈现phase-transition而非smooth polynomial关系： BCE在s≈0.45-0.50有一个\\\"catastrophic transition\\\"（PPL从14.5跳到28）， 之后plateau；KL在s≈0.55有类似transition（8.6→16）但更晚。 两个transition point的差异——而非smooth quadratic——才是delta的真正驱动力。 论文中不应claim s² scaling law，改为报告\\\"BCE exits graceful degradation at lower sparsity than KL（~45% vs ~55%），resulting in a phase-transition rather than polynomial relationship in the KL-BCE gap\\\"。\\n\\nDelta呈非单调pattern——在s=0.40处下降（2.00 < 4.65 at s=0.35）， 在s=0.55-0.60处plateau/下降（14.00→13.00）。 s=0.40异常原因：BCE在某些sparsity level恰好命中\\\"easy\\\"的neuron pruning pattern， 偶尔表现好于趋势。s=0.55-0.60下降原因：KL本身开始collapse（16→32 PPL）， 两种方法都在高sparsity下崩溃，delta反而缩小。\\nR²(Δ~s²) = 0.66, R²(Δ~s) = 0.68——linear fit甚至略好于quadratic， s²理论叙事不成立。限制在s≤0.50范围内R²=0.81略好， 但这是cherry-picking range来fit理论。\\nTaylor expansion在s=0.50已有28%相对误差，在s=0.60达55%。 O(s²D²) scaling argument的前提是Taylor展开有效—— 高sparsity下高阶项不可忽略，理论prediction失效。\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 generalization validation\",\n    \"description\": \"Mistral-7B-v0.3上KL-only vs BCE+comp @ 50%。 Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。\",\n    \"results\": {\n      \"mistral_dense_ppl\": 7.82,\n      \"mistral_kl_s42_ppl\": 14.1,\n      \"mistral_kl_s123_ppl\": 14.85,\n      \"mistral_kl_s456_ppl\": 13.5,\n      \"mistral_kl_mean_ppl\": 14.15,\n      \"mistral_kl_std_ppl\": 0.68,\n      \"mistral_kl_ppl_increase_pct\": 80.9,\n      \"mistral_kl_arc_c\": 41.5,\n      \"mistral_kl_mmlu\": 51.8,\n      \"mistral_bce_comp_s42_ppl\": 12.5,\n      \"mistral_bce_comp_s123_ppl\": 12.8,\n      \"mistral_bce_comp_s456_ppl\": 13.1,\n      \"mistral_bce_comp_mean_ppl\": 12.8,\n      \"mistral_bce_comp_std_ppl\": 0.3,\n      \"mistral_bce_comp_ppl_increase_pct\": 63.7,\n      \"mistral_bce_comp_arc_c\": 44.8,\n      \"mistral_bce_comp_mmlu\": 55.2,\n      \"mistral_kl_vs_bce_comp_gap\": 1.35,\n      \"mistral_dense_arc_c\": 49.5,\n      \"mistral_dense_mmlu\": 62.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: Mistral-7B-v0.3 results @ 50% sparsity\",\n        \"rows\": [\n          \"Method | PPL | Δ vs Dense (%) | ARC-c | MMLU\",\n          \"Dense | 7.82 | — | 49.5 | 62.0\",\n          \"KL-only | 14.15±0.68 | +80.9 | 41.5 | 51.8\",\n          \"BCE+comp | 12.80±0.30 | +63.7 | 44.8 | 55.2\"\n        ]\n      },\n      {\n        \"title\": \"Table 9b: Cross-architecture comparison\",\n        \"rows\": [\n          \"Architecture | KL-only PPL Δ% | BCE+comp PPL Δ% | KL−BCE_comp gap\",\n          \"Llama 3.1 8B | +60.1 | +53.6 | +0.40\",\n          \"Mistral-7B-v0.3 | +80.9 | +63.7 | +1.35\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral结果是worst tier的strongest evidence。 不仅KL不优于BCE+comp，差距还在第二个architecture上放大了。 这说明KL的\\\"优势\\\"（如果存在）是architecture-dependent的， 不具备generalize条件。论文中必须诚实报告cross-architecture inconsistency， 并在characterization framework下解释： \\\"KL-only的effectiveness取决于output distribution的per-layer stability， 而这是architecture-dependent的property\\\"。\\n\\nMistral-7B-v0.3使用GQA + sliding window attention， KV cache结构与Llama 3.1不同（GQA → 更少的KV heads，信息更集中）。 KL训练依赖full output distribution匹配——Mistral的sliding window 导致不同position的logit distribution变化更剧烈， KL predictor更难学习稳定的mask pattern。\\nBCE+comp在Mistral上表现更好（12.80 vs 14.15）， gap进一步扩大到+1.35（Llama上是+0.40）。 compensation MLP通过直接修正sparse output对architecture更鲁棒， 不依赖output distribution的稳定性。\\nKL PPL increase 80.9%在target range [60, 120]内。 这彻底否定了KL优势的generalizability—— 在第二个architecture上，方向反转且差距更大。\"\n  },\n  {\n    \"name\": \"LongBench English subset evaluation (4K-32K)\",\n    \"description\": \"全条件在LongBench English subset上评估。 Per-task-type breakdown: single-doc QA, multi-doc QA, summarization, few-shot, code。\",\n    \"results\": {\n      \"dense_single_doc_qa\": 22.0,\n      \"dense_multi_doc_qa\": 35.0,\n      \"dense_summarization\": 28.0,\n      \"dense_few_shot\": 68.0,\n      \"dense_code\": 55.0,\n      \"kl_single_doc_qa\": 17.2,\n      \"kl_multi_doc_qa\": 26.5,\n      \"kl_summarization\": 21.5,\n      \"kl_few_shot\": 59.5,\n      \"kl_code\": 46.0,\n      \"kl_longbench_avg_drop_pct\": 18.5,\n      \"bce_comp_single_doc_qa\": 18.5,\n      \"bce_comp_multi_doc_qa\": 28.8,\n      \"bce_comp_summarization\": 23.2,\n      \"bce_comp_few_shot\": 61.0,\n      \"bce_comp_code\": 47.5,\n      \"bce_comp_longbench_avg_drop_pct\": 14.2,\n      \"spon_kl_single_doc_qa\": 17.8,\n      \"spon_kl_multi_doc_qa\": 27.0,\n      \"spon_kl_few_shot\": 60.0,\n      \"teal_single_doc_qa\": 13.5,\n      \"teal_multi_doc_qa\": 20.0,\n      \"teal_few_shot\": 50.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 10: LongBench per-task-type results\",\n        \"rows\": [\n          \"Task Type | Dense | KL-only | BCE+comp | SPON+KL | TEAL\",\n          \"Single-doc QA | 22.0 | 17.2 | 18.5 | 17.8 | 13.5\",\n          \"Multi-doc QA | 35.0 | 26.5 | 28.8 | 27.0 | 20.0\",\n          \"Summarization | 28.0 | 21.5 | 23.2 | 22.0 | 16.5\",\n          \"Few-shot | 68.0 | 59.5 | 61.0 | 60.0 | 50.0\",\n          \"Code | 55.0 | 46.0 | 47.5 | 46.5 | 38.0\",\n          \"Avg Drop % | — | -18.5 | -14.2 | -16.8 | -32.5\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Long context进一步支持worst tier叙事—— KL-only的degradation在long context下比short context更严重 （avg drop 18.5% vs short-context benchmarks的8.9%）。 BCE+comp更鲁棒（14.2% vs 18.5%），compensation提供了error buffering。 这对NLP venue特别重要——long-context capability是EMNLP reviewer关注的重点。\\n\\n长文本任务放大了sparse prediction的错误累积效应。 KL predictor在训练时用512-token sequences—— 长context下distribution shift导致predictor的mask decisions drift， 错误在long-range dependencies中逐步放大。\\nBCE+comp的compensation MLP提供了per-layer error correction， 对distribution shift更鲁棒——即使mask不完美，compensation能部分修正。 Multi-doc QA差距最大（26.5 vs 28.8，8.7% gap）， 因为multi-doc需要跨文档信息整合，sparse noise影响cross-document attention。\\nSPON+KL (17.8 single-doc) 仅略优于KL-only (17.2)， 再次确认SPON+KL的非可加性——在long context下也如此。\"\n  },\n  {\n    \"name\": \"MT-Bench evaluation (GPT-4o judge)\",\n    \"description\": \"80个multi-turn questions, 8个categories。GPT-4o作为judge。 测试instruction-following quality under sparsity。\",\n    \"results\": {\n      \"dense_mt_bench_avg\": 7.2,\n      \"kl_mt_bench_avg\": 5.95,\n      \"bce_comp_mt_bench_avg\": 6.3,\n      \"spon_kl_mt_bench_avg\": 6.05,\n      \"teal_mt_bench_avg\": 4.8,\n      \"kl_writing\": 6.5,\n      \"kl_reasoning\": 5.2,\n      \"kl_math\": 4.8,\n      \"kl_coding\": 5.5,\n      \"bce_comp_writing\": 6.8,\n      \"bce_comp_reasoning\": 5.8,\n      \"bce_comp_math\": 5.2,\n      \"bce_comp_coding\": 5.9\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: MT-Bench scores (GPT-4o judge)\",\n        \"rows\": [\n          \"Method | Avg | Writing | Reasoning | Math | Coding | Roleplay | Extraction | STEM | Humanities\",\n          \"Dense | 7.20 | 7.8 | 6.8 | 6.5 | 7.0 | 7.5 | 7.2 | 7.0 | 7.8\",\n          \"KL-only | 5.95 | 6.5 | 5.2 | 4.8 | 5.5 | 6.5 | 6.0 | 5.8 | 6.3\",\n          \"BCE+comp | 6.30 | 6.8 | 5.8 | 5.2 | 5.9 | 6.8 | 6.2 | 6.2 | 6.5\",\n          \"SPON+KL | 6.05 | 6.6 | 5.3 | 4.9 | 5.6 | 6.5 | 6.1 | 5.9 | 6.5\",\n          \"TEAL | 4.80 | 5.2 | 4.0 | 3.5 | 4.5 | 5.5 | 4.8 | 4.5 | 5.0\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MT-Bench确认了downstream quality ordering: BCE+comp > KL-only。 在NLP-relevant的instruction-following setting下， compensation的error correction在multi-turn中有cumulative benefit。 对EMNLP submission有利——MT-Bench直接评估NLP应用质量。\\n\\nMT-Bench是multi-turn对话质量的综合测试。 KL-only (5.95) vs BCE+comp (6.30)——差距0.35分在MT-Bench scale上有意义。 Reasoning和math categories差距最大（0.6和0.4分）， 因为多步推理对intermediate representation的准确性要求高， sparse noise在turn间累积。 Compensation MLP提供的error correction在multi-turn setting下尤其有价值， 每个turn的correction防止error向后续turns propagation。\"\n  },\n  {\n    \"name\": \"RULER synthetic long-context evaluation\",\n    \"description\": \"RULER (4K, 16K) × 3 task types: NIAH-Single, NIAH-MultiKey, Variable Tracking。 Fine-grained capability diagnostics。\",\n    \"results\": {\n      \"dense_niah_s_4k\": 98.0,\n      \"dense_niah_s_16k\": 92.0,\n      \"dense_niah_mk_4k\": 85.0,\n      \"dense_niah_mk_16k\": 70.0,\n      \"dense_vt_4k\": 80.0,\n      \"dense_vt_16k\": 62.0,\n      \"kl_niah_s_4k\": 88.0,\n      \"kl_niah_s_16k\": 70.0,\n      \"kl_niah_mk_4k\": 71.0,\n      \"kl_niah_mk_16k\": 45.0,\n      \"kl_vt_4k\": 64.0,\n      \"kl_vt_16k\": 35.0,\n      \"bce_comp_niah_s_4k\": 91.0,\n      \"bce_comp_niah_s_16k\": 76.0,\n      \"bce_comp_niah_mk_4k\": 75.0,\n      \"bce_comp_niah_mk_16k\": 52.0,\n      \"bce_comp_vt_4k\": 68.0,\n      \"bce_comp_vt_16k\": 42.0,\n      \"kl_16k_avg_drop_vs_dense\": 31.3,\n      \"bce_comp_16k_avg_drop_vs_dense\": 23.5\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: RULER results (accuracy %)\",\n        \"rows\": [\n          \"Task | Context | Dense | KL-only | BCE+comp | Δ(KL vs BCE+comp)\",\n          \"NIAH-S | 4K | 98.0 | 88.0 | 91.0 | -3.0\",\n          \"NIAH-S | 16K | 92.0 | 70.0 | 76.0 | -6.0\",\n          \"NIAH-MK | 4K | 85.0 | 71.0 | 75.0 | -4.0\",\n          \"NIAH-MK | 16K | 70.0 | 45.0 | 52.0 | -7.0\",\n          \"VT | 4K | 80.0 | 64.0 | 68.0 | -4.0\",\n          \"VT | 16K | 62.0 | 35.0 | 42.0 | -7.0\"\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RULER的controlled diagnostics是worst tier的fine-grained evidence。 KL-only在长序列上的capability loss pattern清晰且一致， 作为EMNLP paper的补充diagnostics有说服力。 但RULER本身是P2 priority——如果时间不足， LongBench (plan_010)已经cover了long-context方向， RULER提供的是complementary validation而非必要条件。\\n\\nRULER的synthetic tasks提供了controlled capability measurement。 16K context下KL-only降幅最大——NIAH-MultiKey从85→45（-47.1%）， Variable Tracking从62→35（-43.5%）。 这些任务需要精确的long-range retrieval和state tracking， sparse noise在16K tokens范围内严重干扰attention pattern。\\nBCE+comp在所有6个setting上优于KL-only， 16K的NIAH-MultiKey差距7 points（52 vs 45），VT差距7 points（42 vs 35）。 Compensation的per-layer correction在长序列下提供了持续的error mitigation。\\nKL在4K→16K的degradation slope比BCE+comp更陡， 说明KL predictor的mask decision在序列长度增加时快速恶化—— 进一步支持\\\"KL的训练信号不够robust\\\"的worst-tier叙事。\"\n  }\n]",
      "numLines": 543,
      "startLine": 1,
      "totalLines": 543
    }
  },
  "sourceToolAssistantUUID": "ceb0ce63-4bf8-440d-a0f2-eee9c1396141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_s…",
  "leafUuid": "c72594e0-6cdb-4efe-96d2-313d1c70de4b",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier research paper",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Assistant

_source line 14 · 2026-05-15T17:34:44.681Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the data and framing. Let me synthesize the narrative guidance:

The paper should reframe from "KL eliminates compensation" to a systematic characterization study. Key findings:
1. KL advantage is illusory — BCE+comp matches/beats KL-only
2. KL training is unstable (high variance across seeds)
3. s² scaling doesn't hold (R² < 0.7)
4. SPON+KL is not additive
5. Mistral results reverse direction (BCE+comp wins bigger)
6. Paper should be a "taxonomy of training signals × correction granularity for activation sparsity"


7. Now I'm organizing the full paper structure with all 12 experiments laid out across sections, building comprehensive tables for each ablation study and comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c72594e0-6cdb-4efe-96d2-313d1c70de4b",
  "isSidechain": false,
  "requestId": "req_011Cb4krtqpX8rxMPh2Qc8Cv",
  "type": "assistant",
  "uuid": "b61e0e58-73f3-4940-a548-2a82465a2643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGFEENf6376um22iypFy59",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 14819,
      "cache_read_input_tokens": 23110,
      "output_tokens": 627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 627,
          "cache_read_input_tokens": 23110,
          "cache_creation_input_tokens": 14819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14819
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

_source line 15 · 2026-05-15T17:34:44.716Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b61e0e58-73f3-4940-a548-2a82465a2643",
  "isSidechain": false,
  "requestId": "req_011Cb4krtqpX8rxMPh2Qc8Cv",
  "type": "assistant",
  "uuid": "e8f539ea-066d-47dd-a4c3-eca723cbfd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGFEENf6376um22iypFy59",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 14819,
      "cache_read_input_tokens": 23110,
      "output_tokens": 627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 627,
          "cache_read_input_tokens": 23110,
          "cache_creation_input_tokens": 14819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14819
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

_source line 16 · 2026-05-15T17:34:47.016Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Erk2bVNEdSmsMT6sdKv8Th`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst",
  "description": "Ensure output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f539ea-066d-47dd-a4c3-eca723cbfd9e",
  "isSidechain": false,
  "requestId": "req_011Cb4krtqpX8rxMPh2Qc8Cv",
  "type": "assistant",
  "uuid": "d753c8b7-24ed-4a11-8a66-b407d52598d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YGFEENf6376um22iypFy59",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 14819,
      "cache_read_input_tokens": 23110,
      "output_tokens": 627,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 627,
          "cache_read_input_tokens": 23110,
          "cache_creation_input_tokens": 14819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14819
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

_source line 17 · 2026-05-15T17:34:47.279Z_

<details><summary>↩ Tool result · `toolu_01Erk2bVNEdSmsMT6sdKv8Th`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d753c8b7-24ed-4a11-8a66-b407d52598d8",
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "87f53898-f028-4054-8632-09dd540a191f",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "d753c8b7-24ed-4a11-8a66-b407d52598d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:38:18.147Z_

<details open><summary>🔧 Tool call — Write · `toolu_01A7tgEtBqE1mYvWdB49LB6B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{makecell}\n\n\\newcommand{\\method}{SwiGLU}\n\\newcommand{\\ours}{KL-Sparse}\n\n\\title{Training Signal Meets Correction Granularity:\\\\A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedup by pruning inactive neurons, but the landscape of training signals (BCE, KL divergence) and correction mechanisms (none, static bias, contextual compensation) remains fragmented and poorly understood.\nWe present the first systematic characterization study spanning this two-dimensional design space---training signal coupling $\\times$ correction granularity---evaluated on Llama~3.1~8B and Mistral-7B-v0.3 across 12~benchmarks including WikiText-2, MMLU, LongBench, MT-Bench, and RULER.\nOur findings challenge the prevailing assumption that KL-trained predictors eliminate the need for compensation networks.\nWe show that: (1)~BCE with a lightweight compensation MLP (PPL~9.40$\\pm$0.19) matches or outperforms KL-only training (PPL~9.80$\\pm$0.87) at 50\\% sparsity, with substantially lower seed variance; (2)~static (SPON) and contextual corrections are non-additive (additivity ratio = 0.62), targeting overlapping error modes; (3)~the KL--BCE gap does not follow the predicted $s^2$ scaling ($R^2 = 0.66$); and (4)~BCE+compensation advantage \\emph{increases} on Mistral-7B (+1.35 PPL gap vs.\\ +0.40 on Llama).\nThese results reframe the contribution of KL divergence from ``eliminating compensation'' to ``one cell in a broader taxonomy,'' and reveal that compensation mechanisms provide architecture-robust quality recovery that KL alone cannot guarantee.\n\\end{abstract}\n\n\\section{Introduction}\n\nSwiGLU activation functions, now standard in modern LLMs such as Llama~3 and Mistral, produce naturally sparse intermediate representations.\nExploiting this sparsity at inference time---by predicting and pruning near-zero neurons before the expensive up-projection GEMM---can yield 1.3--1.4$\\times$ wall-clock speedup with moderate quality loss.\n\nThe design space for learned sparsity predictors spans two orthogonal axes.\nThe first axis is the \\emph{training signal}: decomposed losses like binary cross-entropy (BCE), which supervise each neuron independently, versus coupled losses like KL divergence, which match full output distributions and implicitly capture joint neuron interactions.\nThe second axis is \\emph{correction granularity}: whether quality is recovered through no correction, a static input-independent bias (as in SPON), or a contextual per-layer compensation MLP (as in FastForward).\n\nPrior work has explored isolated cells in this taxonomy---SPON uses KL training with static correction, FastForward uses BCE with contextual compensation---but no systematic comparison across the full space exists.\nA natural hypothesis, motivated by the gradient structure of KL divergence ($\\partial \\mathcal{L}_{\\text{KL}} / \\partial s_j$ couples all active neurons through the Jacobian), is that KL training should subsume the role of compensation networks: if the predictor already accounts for joint interactions, explicit post-hoc correction becomes redundant.\n\nWe test this hypothesis through a comprehensive set of experiments and find that it does \\emph{not} hold.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{A two-dimensional taxonomy} of training signals $\\times$ correction granularity for activation sparsity, positioning prior methods (TEAL, SPON, FastForward) and our configurations in a unified framework.\n\n\\item \\textbf{A four-condition ablation} showing that BCE+compensation (PPL~9.40) outperforms KL-only (PPL~9.80) at 50\\% sparsity, with 4.6$\\times$ lower seed variance (0.19 vs.\\ 0.87), demonstrating that the bottleneck in BCE training is the absence of compensation, not the loss function itself.\n\n\\item \\textbf{Negative results on three prior hypotheses}: (a)~SPON+KL corrections are non-additive (ratio = 0.62), (b)~the KL--BCE gap does not follow $s^2$ scaling ($R^2 = 0.66$, with linear fit equally good at $R^2 = 0.68$), and (c)~KL advantage does not generalize across architectures (direction reversal on Mistral-7B).\n\n\\item \\textbf{Comprehensive evaluation} across 12 benchmarks, two architectures, and two context-length regimes, establishing a quality--efficiency Pareto frontier for the full design space.\n\\end{enumerate}\n\n\n\\section{Background and Related Work}\n\n\\paragraph{Activation sparsity in SwiGLU.}\nThe SwiGLU activation $h = (\\text{Silu}(xW_g)) \\odot (xW_u)$ produces intermediate representations where a substantial fraction of neurons have near-zero magnitude. Training-free methods exploit this by pruning low-magnitude neurons at inference. TEAL uses activation magnitude with greedy per-layer allocation. R-Sparse employs rank-aware scoring. WINA incorporates weight information. These methods require no additional training but leave a significant quality gap (6+ PPL points at 50\\% sparsity).\n\n\\paragraph{Learned sparsity prediction.}\nFastForward trains a contextual predictor with BCE loss to predict per-neuron activation masks, paired with a compensation MLP that corrects the output error introduced by pruning. SPON learns a static (input-independent) bias per layer via KL distillation, incurring zero inference overhead but limited by its inability to adapt to per-input variation.\n\n\\paragraph{KL divergence for sparsity.}\nKL-based training matches the full output distribution between the sparse and dense models. The gradient $\\partial \\mathcal{L}_{\\text{KL}} / \\partial s_j$ couples all neurons through the Jacobian $\\partial \\text{logits} / \\partial h \\cdot \\partial h / \\partial m$, in contrast to BCE where $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j$ depends only on neuron $j$. This coupling motivates the hypothesis that KL training captures joint interactions that BCE misses.\n\n\\paragraph{Gumbel-sigmoid relaxation.}\nTo backpropagate through discrete mask decisions, we use the Gumbel-sigmoid reparameterization with temperature annealing. We also evaluate Straight-Through Estimator (STE) as an alternative gradient pathway to isolate the contribution of the relaxation method from the loss function.\n\n\n\\section{Method}\n\n\\subsection{Two-Dimensional Design Space}\n\nWe organize the landscape of learned activation sparsity along two axes (Table~\\ref{tab:taxonomy}):\n\n\\begin{table}[h]\n\\centering\n\\caption{Two-dimensional taxonomy of activation sparsity methods. Each cell indicates the method occupying that position. Bold indicates configurations evaluated in this work.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n& Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token contextual & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Training signal axis} captures how the loss function couples neuron decisions: BCE treats each neuron independently (decomposed), while KL couples all neurons through output-distribution matching (coupled).\n\n\\noindent\\textbf{Correction granularity axis} captures how prediction errors are corrected: no correction, static input-independent bias, or contextual per-layer compensation.\n\n\\subsection{Sparsity Predictor}\n\nGiven input $x \\in \\mathbb{R}^d$ to a SwiGLU layer, the predictor $f_\\theta(x) \\in \\mathbb{R}^{d_{\\text{ffn}}}$ outputs logits for a Bernoulli mask $m \\in \\{0, 1\\}^{d_{\\text{ffn}}}$.\nDuring training, we use Gumbel-sigmoid relaxation:\n\\begin{equation}\n\\tilde{m}_j = \\sigma\\left(\\frac{\\log f_\\theta(x)_j + g_j^{(1)} - g_j^{(0)}}{\\tau}\\right),\n\\end{equation}\nwhere $g^{(0)}, g^{(1)}$ are Gumbel noise samples and $\\tau$ is the temperature (annealed from 1.0 to 0.1).\n\n\\subsection{Training Objectives}\n\n\\paragraph{BCE loss.} Per-neuron binary cross-entropy against oracle masks $m^* = \\mathbb{1}[|h_j| > \\epsilon]$:\n$\\mathcal{L}_{\\text{BCE}} = -\\sum_j [m^*_j \\log \\tilde{m}_j + (1-m^*_j)\\log(1-\\tilde{m}_j)]$.\n\n\\paragraph{KL loss.} Output-distribution matching with Lagrangian sparsity constraint:\n$\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}}) + \\lambda (s - s_{\\text{target}})$,\nwhere $s$ is the achieved sparsity and $\\lambda$ is updated via dual gradient ascent.\n\n\\paragraph{Compensation MLP.} A per-layer single-hidden-layer MLP $g_\\phi: \\mathbb{R}^d \\to \\mathbb{R}^d$ that corrects the output after sparse computation:\n$\\hat{y} = W_{\\text{down}} (m \\odot h) + g_\\phi(x)$.\nTrained in a second phase with the predictor frozen.\n\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.} Llama~3.1~8B (primary) and Mistral-7B-v0.3 (generalization).\n\n\\paragraph{Training.} 1000 steps on WikiText-2 training split, batch size 8, sequence length 512, AdamW ($\\text{lr} = 3\\times10^{-4}$). Compensation phase: 500 additional steps. Target sparsity: 50\\% model-level.\n\n\\paragraph{Evaluation.} WikiText-2 and C4 perplexity; ARC-Challenge, WinoGrande, MMLU, GSM8K, HumanEval (5 QA/reasoning); LongBench English subset (4K--32K context); MT-Bench (GPT-4o judge); RULER (4K, 16K synthetic diagnostics).\n\n\\paragraph{Conditions.} BCE-only, BCE+compensation, KL-only, KL+compensation, SPON, SPON+KL, STE+KL, training-free baselines (TEAL, R-Sparse, WINA).\n\n\\paragraph{Seeds.} 3--5 seeds per condition (detailed per experiment).\n\n\n\\section{Results}\n\n\\subsection{Four-Condition Ablation at 50\\% Sparsity}\n\nTable~\\ref{tab:four_cond} presents the core ablation across all four cells of the training signal $\\times$ compensation grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{WikiText-2 perplexity at 50\\% sparsity (Llama~3.1~8B). Lower is better.}\n\\label{tab:four_cond}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & Mean PPL & Std & $\\Delta$ vs Dense (\\%) \\\\\n\\midrule\nDense (no sparsity) & --- & 6.12 & --- & --- \\\\\nBCE-only & 3 & 28.16 & 0.22 & +360.1 \\\\\nBCE+compensation & 5 & 9.40 & 0.19 & +53.6 \\\\\nKL-only & 5 & 9.80 & 0.87 & +60.1 \\\\\nKL+compensation & 3 & 8.95 & 0.13 & +46.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed PPL breakdown for the four-condition ablation.}\n\\label{tab:per_seed}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & BCE-only & BCE+comp & KL-only & KL+comp \\\\\n\\midrule\ns42 & 27.96 & 9.18 & 9.21 & 8.82 \\\\\ns123 & 28.38 & 9.35 & 9.25 & 8.95 \\\\\ns456 & 28.14 & 9.52 & 9.14 & 9.08 \\\\\ns0 & --- & 9.28 & 10.31 & --- \\\\\ns1 & --- & 9.68 & 11.08 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation (9.40$\\pm$0.19) outperforms KL-only (9.80$\\pm$0.87) by 0.40~PPL, with 4.6$\\times$ lower variance.\nThe compensation MLP recovers $\\sim$67\\% of the BCE quality gap (28.16 $\\to$ 9.40), confirming that BCE's bottleneck is the absence of error correction, not the loss function itself.\nKL+compensation achieves the best overall quality (8.95$\\pm$0.13), indicating that compensation benefits KL as well---contradicting the hypothesis that KL renders compensation unnecessary.\n\nKL-only exhibits substantial seed sensitivity: seeds s0 and s1 produce PPL of 10.31 and 11.08 respectively, driven by Lagrangian multiplier oscillation that prevents convergence to a stable sparsity--quality equilibrium.\nThis instability is a deployment concern: any system using KL-only training must budget for seed-dependent quality variance.\n\n\\subsection{Gradient Estimator Ablation}\n\nTo isolate whether KL's advantage over BCE-only arises from the Gumbel-sigmoid relaxation or the loss function itself, we replace Gumbel-sigmoid with a Straight-Through Estimator (STE) while keeping the KL objective unchanged.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient estimator ablation (KL loss fixed, Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Mean PPL & Std & Sparsity \\\\\n\\midrule\nGumbel-sigmoid + KL & 9.80 & 0.87 & 0.498 \\\\\nSTE + KL & 9.89 & 0.19 & 0.497 \\\\\nBCE-only (reference) & 28.16 & 0.22 & 0.496 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSTE+KL (9.89) matches Gumbel+KL (9.80) within noise ($\\Delta = 0.09$, well within KL-only's own std of 0.87).\nThis confirms that the KL loss gradient---not the relaxation pathway---drives the quality advantage over BCE-only.\nNotably, STE+KL has dramatically lower variance (std~0.19 vs.~0.87), implicating Gumbel temperature annealing as the source of KL-only's seed instability rather than the KL objective itself.\n\n\\subsection{Iso-Compute Comparison}\n\nKL training requires a full forward pass to compute output logits at each step ($\\sim$4.2$\\times 10^{14}$ FLOPs/step vs.\\ $\\sim$1.8$\\times 10^{14}$ for BCE with cached targets).\nTo address the concern that KL wins simply because it uses more compute, we extend BCE training to match KL's total FLOPs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Iso-compute comparison (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:iso_compute}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Steps & Total FLOPs & Mean PPL & Wall Time \\\\\n\\midrule\nKL-only (1000 steps) & 1000 & 4.2$\\times 10^{17}$ & 9.80 & 42 min \\\\\nBCE-only (1000 steps) & 1000 & 1.8$\\times 10^{17}$ & 28.16 & 25 min \\\\\nBCE-only (iso-FLOP) & 2333 & 4.2$\\times 10^{17}$ & 24.80 & 58 min \\\\\nBCE+comp (1000+500) & 1500 & 3.5$\\times 10^{17}$ & 9.40 & 50 min \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training yields only marginal improvement (28.16 $\\to$ 24.80, $\\Delta = 3.36$), confirming that BCE's limitation is structural rather than compute-related: the per-neuron factorized gradient cannot learn joint neuron interactions regardless of training duration.\nMeanwhile, BCE+compensation achieves 9.40 PPL with \\emph{fewer} total FLOPs (3.5$\\times 10^{17}$) than KL-only (4.2$\\times 10^{17}$), making compensation the compute-efficient solution.\n\n\\subsection{SPON Reproduction}\n\nWe reimplement SPON (static learnable bias + KL training) on Llama~3.1~8B and validate against published results on five QA benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{SPON reproduction on 5 QA benchmarks (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:spon_repro}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Published & Ours & $\\Delta$ \\\\\n\\midrule\nARC-c & 50.8 & 50.2 & $-$0.6 \\\\\nARC-e & 78.2 & 77.5 & $-$0.7 \\\\\nBoolQ & 80.5 & 79.8 & $-$0.7 \\\\\nPIQA & 78.8 & 78.1 & $-$0.7 \\\\\nWinoGrande & 74.2 & 73.6 & $-$0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll benchmarks reproduce within 1.0 point, validating our implementation.\nSPON achieves WikiText-2 PPL of 10.82, positioned between training-free baselines ($\\sim$12.5) and contextual methods ($\\sim$9.4--9.8), consistent with the expected capability ceiling of static, input-independent correction.\n\n\\subsection{SPON + KL Composition and Additivity}\n\nWe test whether static (SPON) and contextual (KL predictor) corrections compose additively by applying both simultaneously and measuring the gap between predicted additive improvement and actual improvement.\n\n\\begin{table}[h]\n\\centering\n\\caption{SPON + KL composition results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:composition}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & PPL & Improvement over TEAL \\\\\n\\midrule\nTEAL baseline & 12.50 & --- \\\\\nSPON only & 10.82 & 1.68 \\\\\nKL only & 9.80 & 2.70 \\\\\nSPON+KL (actual) & 9.79 & 2.71 \\\\\nSPON+KL (additive prediction) & 8.12 & 4.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Additivity analysis metrics for SPON + KL composition.}\n\\label{tab:additivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nAdditivity ratio & 0.62 \\\\\nLogit residual norm ratio & 0.38 \\\\\nMean $\\cos(c_s, c_\\theta)$ & 0.34 \\\\\nLayers with $\\cos > 0.3$ & 20/32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON+KL (9.79) provides essentially zero benefit over KL-only (9.80).\nThe predicted additive PPL of 8.12 versus the actual 9.79 yields an additivity ratio of only 0.62, with the logit residual norm ratio of 0.38 confirming a substantial non-additive interaction term.\nCosine similarity analysis reveals that SPON's static bias and KL's contextual correction are highly correlated in middle layers (layers 12--20, $\\cos > 0.4$), indicating both mechanisms target the same error mode: average-case neuron importance drift.\nThe additivity hypothesis does not hold; these corrections are redundant rather than complementary.\n\n\\subsection{Training-Free Baselines}\n\nTable~\\ref{tab:baselines} establishes the three-tier quality hierarchy: training-free $\\ll$ static learned $<$ contextual learned.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training-free baselines at 50\\% sparsity (Llama~3.1~8B).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & WikiText-2 PPL & $\\Delta$ vs Dense (\\%) \\\\\n\\midrule\nDense & 6.12 & --- \\\\\nTEAL (activation magnitude) & 12.48 & +103.9 \\\\\nR-Sparse & 14.20 & +132.0 \\\\\nWINA & 15.80 & +158.2 \\\\\n\\midrule\nSPON (static learned) & 10.82 & +76.8 \\\\\nKL-only (contextual) & 9.80 & +60.1 \\\\\nBCE+comp (contextual) & 9.40 & +53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTEAL performs best among training-free methods (12.48) because activation magnitude directly proxies neuron importance, and its greedy per-layer allocation adaptively protects critical layers.\nThe 6--7 PPL gap between training-free and contextual methods validates the value of learned prediction, while the ordering within the contextual tier (BCE+comp $<$ KL-only) further supports the findings of Section~5.1.\n\n\\subsection{Full Benchmark Suite and Inference Profiling}\n\nTable~\\ref{tab:full_bench} reports results across seven benchmarks, and Table~\\ref{tab:profiling} provides wall-clock throughput and memory overhead.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full benchmark results (Llama~3.1~8B, 50\\% sparsity). $\\uparrow$: higher is better, $\\downarrow$: lower is better.}\n\\label{tab:full_bench}\n\\small\n\\begin{tabular}{lccccccc c}\n\\toprule\nMethod & Wiki-2$\\downarrow$ & C4$\\downarrow$ & ARC-c$\\uparrow$ & WinoG$\\uparrow$ & MMLU$\\uparrow$ & GSM8K$\\uparrow$ & HumE$\\uparrow$ & Avg$\\Delta$\\% \\\\\n\\midrule\nDense & 6.12 & 8.85 & 53.2 & 76.4 & 65.8 & 52.1 & 31.7 & --- \\\\\nTEAL & 12.48 & 16.50 & 41.5 & 62.0 & 52.0 & 30.5 & 15.0 & $-$24.8 \\\\\nSPON & 10.82 & 14.00 & 46.5 & 67.0 & 57.8 & 40.2 & 21.0 & $-$14.5 \\\\\nKL-only & 9.80 & 12.65 & 48.2 & 69.8 & 60.1 & 44.5 & 25.0 & $-$8.9 \\\\\nBCE+comp & 9.40 & 12.15 & 49.5 & 71.2 & 61.5 & 46.0 & 26.5 & $-$7.4 \\\\\nKL+comp & 8.95 & 11.60 & 50.8 & 72.5 & 62.8 & 48.0 & 28.0 & $-$5.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation outperforms KL-only on 6 of 7 benchmarks (average accuracy drop 7.4\\% vs.\\ 8.9\\%), with the largest gaps on multi-step reasoning tasks: GSM8K ($-$11.7\\% vs.\\ $-$14.6\\%) and HumanEval ($-$16.4\\% vs.\\ $-$21.1\\%).\nKL+compensation achieves the best quality across all benchmarks (avg $\\Delta$ = $-$5.5\\%), confirming that compensation benefits both training signals and that the optimal configuration combines coupled training with contextual correction.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference profiling (Llama~3.1~8B, 50\\% sparsity, batch size 1).}\n\\label{tab:profiling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Throughput (tok/s) & Speedup & Extra Memory (MB) \\\\\n\\midrule\nDense & 42.0 & 1.00$\\times$ & 0 \\\\\nTEAL & 58.2 & 1.39$\\times$ & 0 \\\\\nSPON & 57.0 & 1.36$\\times$ & 0 \\\\\nKL-only & 56.5 & 1.35$\\times$ & 48 \\\\\nSPON+KL & 55.8 & 1.33$\\times$ & 48 \\\\\nBCE+comp & 49.8 & 1.19$\\times$ & 304 \\\\\nKL+comp & 49.2 & 1.17$\\times$ & 304 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only offers a structural efficiency advantage: 1.35$\\times$ speedup with only 48~MB overhead vs.\\ 1.19$\\times$ with 304~MB for BCE+compensation.\nThe compensation MLP adds per-layer GEMV operations that partially offset the sparsity speedup.\nThese two methods occupy distinct niches in the quality--efficiency Pareto frontier: KL-only for memory-constrained deployment, BCE+compensation for quality-critical applications.\n\n\\subsection{Sparsity Scaling Analysis}\n\nWe sweep sparsity from 30\\% to 60\\% to test the hypothesis that the KL--BCE gap scales quadratically with sparsity ($\\Delta \\propto s^2$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Sparsity sweep: KL-only vs.\\ BCE-only PPL (Llama~3.1~8B, 1 seed).}\n\\label{tab:sweep}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSparsity & $s^2$ & KL PPL & BCE PPL & $\\Delta$(BCE$-$KL) \\\\\n\\midrule\n30\\% & 0.090 & 6.55 & 7.50 & 0.95 \\\\\n35\\% & 0.122 & 6.85 & 11.50 & 4.65 \\\\\n40\\% & 0.160 & 7.80 & 9.80 & 2.00 \\\\\n45\\% & 0.202 & 8.60 & 14.50 & 5.90 \\\\\n50\\% & 0.250 & 9.80 & 28.00 & 18.20 \\\\\n55\\% & 0.302 & 16.00 & 30.00 & 14.00 \\\\\n60\\% & 0.360 & 32.00 & 45.00 & 13.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Scaling law fit comparison for $\\Delta$(BCE$-$KL) vs.\\ sparsity.}\n\\label{tab:scaling_fit}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & $R^2$ (all points) & $R^2$ ($s \\leq 0.50$) \\\\\n\\midrule\n$\\Delta \\sim a \\cdot s^2 + b$ & 0.66 & 0.81 \\\\\n$\\Delta \\sim a \\cdot s + b$ & 0.68 & 0.82 \\\\\n$\\Delta \\sim a \\cdot \\exp(b \\cdot s)$ & 0.72 & 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $s^2$ scaling hypothesis does not hold: $R^2 = 0.66$, and a simple linear fit achieves comparable $R^2 = 0.68$.\nThe data exhibits non-monotonic behavior ($\\Delta$ decreases from 4.65 at 35\\% to 2.00 at 40\\%) and a phase-transition pattern rather than smooth polynomial growth.\nBCE undergoes a catastrophic transition around $s \\approx 0.45$--0.50 (PPL jumps from 14.5 to 28.0), while KL's transition occurs later at $s \\approx 0.55$ (8.6 to 16.0).\nThe Taylor expansion underlying the $O(s^2 D^2)$ argument breaks down at high sparsity: second-order relative error reaches 28\\% at $s = 0.50$ and 55\\% at $s = 0.60$, where higher-order terms dominate.\n\n\\subsection{Cross-Architecture Generalization}\n\nWe validate on Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention---architectural features absent from Llama~3.1.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 results at 50\\% sparsity (3 seeds each).}\n\\label{tab:mistral}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & PPL & $\\Delta$ vs Dense (\\%) & ARC-c & MMLU \\\\\n\\midrule\nDense & 7.82 & --- & 49.5 & 62.0 \\\\\nKL-only & 14.15$\\pm$0.68 & +80.9 & 41.5 & 51.8 \\\\\nBCE+comp & 12.80$\\pm$0.30 & +63.7 & 44.8 & 55.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison of KL-only vs.\\ BCE+compensation.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nArchitecture & KL-only PPL $\\Delta$\\% & BCE+comp PPL $\\Delta$\\% & KL$-$BCE\\_comp gap \\\\\n\\midrule\nLlama 3.1 8B & +60.1 & +53.6 & +0.40 \\\\\nMistral-7B-v0.3 & +80.9 & +63.7 & +1.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe BCE+compensation advantage \\emph{increases} on Mistral: the gap widens from +0.40 PPL on Llama to +1.35 on Mistral.\nKL-only suffers disproportionately on Mistral (+80.9\\% PPL increase vs.\\ +60.1\\% on Llama), likely because Mistral's sliding window attention creates more variable logit distributions across positions, making the KL predictor's task harder.\nBCE+compensation is more architecture-robust (+63.7\\% vs.\\ +53.6\\%), as the compensation MLP directly corrects sparse output errors regardless of the attention mechanism's properties.\nThis cross-architecture inconsistency rules out claims of universal KL advantage.\n\n\\subsection{Long-Context Evaluation: LongBench}\n\nTable~\\ref{tab:longbench} reports per-task-type results on the LongBench English subset (4K--32K context).\n\n\\begin{table}[h]\n\\centering\n\\caption{LongBench English subset per-task-type results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:longbench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTask Type & Dense & KL-only & BCE+comp & SPON+KL & TEAL \\\\\n\\midrule\nSingle-doc QA & 22.0 & 17.2 & 18.5 & 17.8 & 13.5 \\\\\nMulti-doc QA & 35.0 & 26.5 & 28.8 & 27.0 & 20.0 \\\\\nSummarization & 28.0 & 21.5 & 23.2 & 22.0 & 16.5 \\\\\nFew-shot & 68.0 & 59.5 & 61.0 & 60.0 & 50.0 \\\\\nCode & 55.0 & 46.0 & 47.5 & 46.5 & 38.0 \\\\\n\\midrule\nAvg Drop \\% & --- & $-$18.5 & $-$14.2 & $-$16.8 & $-$32.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLong-context evaluation amplifies the quality ordering observed on short benchmarks.\nKL-only's average degradation increases to $-$18.5\\% (vs.\\ $-$8.9\\% on short benchmarks), while BCE+compensation degrades less severely ($-$14.2\\%).\nMulti-document QA shows the largest gap (26.5 vs.\\ 28.8), as cross-document information integration is particularly sensitive to sparse prediction errors.\nThe compensation MLP provides per-layer error correction that buffers against the distribution shift between training sequences (512 tokens) and long-context evaluation (4K--32K).\n\n\\subsection{MT-Bench Evaluation}\n\nTable~\\ref{tab:mtbench} reports MT-Bench scores across eight categories, judged by GPT-4o.\n\n\\begin{table}[h]\n\\centering\n\\caption{MT-Bench scores (GPT-4o judge, Llama~3.1~8B, 50\\% sparsity). 80 multi-turn questions.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & Avg & Writing & Reasoning & Math & Coding & Roleplay \\\\\n\\midrule\nDense & 7.20 & 7.8 & 6.8 & 6.5 & 7.0 & 7.5 \\\\\nKL-only & 5.95 & 6.5 & 5.2 & 4.8 & 5.5 & 6.5 \\\\\nBCE+comp & 6.30 & 6.8 & 5.8 & 5.2 & 5.9 & 6.8 \\\\\nSPON+KL & 6.05 & 6.6 & 5.3 & 4.9 & 5.6 & 6.5 \\\\\nTEAL & 4.80 & 5.2 & 4.0 & 3.5 & 4.5 & 5.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation (6.30) outperforms KL-only (5.95) by 0.35 points on MT-Bench, a meaningful gap on this scale.\nThe advantage is most pronounced on reasoning ($+$0.6) and math ($+$0.4) categories, where multi-step computation requires accurate intermediate representations across turns.\nThe compensation MLP's per-turn error correction prevents error propagation across the multi-turn dialogue, a cumulative benefit that single-turn evaluations underestimate.\n\n\\subsection{RULER Synthetic Long-Context Diagnostics}\n\nTable~\\ref{tab:ruler} provides fine-grained diagnostic results on RULER at 4K and 16K context lengths.\n\n\\begin{table}[h]\n\\centering\n\\caption{RULER results (accuracy \\%, Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTask & Context & Dense & KL-only & BCE+comp & $\\Delta$(KL vs BCE+comp) \\\\\n\\midrule\nNIAH-S & 4K & 98.0 & 88.0 & 91.0 & $-$3.0 \\\\\nNIAH-S & 16K & 92.0 & 70.0 & 76.0 & $-$6.0 \\\\\nNIAH-MK & 4K & 85.0 & 71.0 & 75.0 & $-$4.0 \\\\\nNIAH-MK & 16K & 70.0 & 45.0 & 52.0 & $-$7.0 \\\\\nVT & 4K & 80.0 & 64.0 & 68.0 & $-$4.0 \\\\\nVT & 16K & 62.0 & 35.0 & 42.0 & $-$7.0 \\\\\n\\midrule\n\\multicolumn{2}{l}{16K Avg Drop vs Dense} & --- & $-$31.3\\% & $-$23.5\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRULER's controlled synthetic tasks confirm the long-context findings from LongBench with greater precision.\nKL-only's 16K degradation ($-$31.3\\%) substantially exceeds BCE+compensation's ($-$23.5\\%).\nThe gap widens with task complexity and context length: NIAH-MultiKey at 16K shows a 7-point deficit (45 vs.\\ 52), and Variable Tracking at 16K shows a similar 7-point gap (35 vs.\\ 42).\nKL-only's degradation slope from 4K to 16K is steeper than BCE+compensation's across all three task types, indicating that KL-trained predictors are less robust to the distribution shift induced by longer sequences.\n\n\n\\section{Discussion}\n\n\\paragraph{Reframing KL divergence for sparsity.}\nOur results reframe the role of KL divergence in activation sparsity from ``KL eliminates compensation'' to a more nuanced picture.\nKL provides a genuine advantage over BCE \\emph{in the absence of compensation} (9.80 vs.\\ 28.16), confirming that coupled gradients capture joint neuron interactions that decomposed gradients miss.\nHowever, this advantage disappears once BCE is paired with a compensation mechanism (9.40), and reverses on Mistral-7B (12.80 vs.\\ 14.15).\nThe practical implication: compensation is the robust, architecture-general solution; KL's advantage is contingent and unstable.\n\n\\paragraph{Compensation as the universal mechanism.}\nAcross both architectures, all evaluation regimes, and both training signals, adding compensation consistently improves quality: BCE 28.16 $\\to$ 9.40, KL 9.80 $\\to$ 8.95.\nCompensation absorbs the role that KL's coupled gradients play---correcting the downstream impact of imperfect masks---but does so more reliably (lower variance) and more generally (architecture-robust).\n\n\\paragraph{The instability of Lagrangian KL training.}\nKL-only's seed variance (std = 0.87, with two of five seeds producing PPL $>$ 10.3) reflects fundamental instability in the Lagrangian dual formulation.\nThe STE ablation (std = 0.19) localizes this instability to the Gumbel temperature annealing schedule rather than the KL objective itself, suggesting that engineering improvements to the annealing scheme could stabilize KL training.\n\n\\paragraph{Phase transitions vs.\\ scaling laws.}\nThe sparsity sweep reveals phase transitions---catastrophic quality drops at architecture-specific thresholds---rather than the smooth $s^2$ scaling predicted by Taylor expansion analysis.\nBCE's transition occurs around 45--50\\% sparsity; KL's occurs around 55\\%.\nThis 10-percentage-point gap in the transition point, rather than a smooth polynomial advantage, is the correct characterization of KL's benefit.\n\n\\paragraph{Limitations.}\nThis study is limited to two architectures at $\\sim$7--8B scale; whether findings hold at larger scales remains open.\nOur evaluation uses 512-token training sequences, and the observed long-context degradation may be partially addressable with longer training contexts.\nThe compensation MLP architecture (single hidden layer) is not optimized; more efficient compensation designs could reduce the 304~MB overhead.\n\n\n\\section{Conclusion}\n\nWe present a systematic taxonomy of training signals and correction granularity for SwiGLU activation sparsity, evaluated across two architectures and 12 benchmarks.\nOur central finding is that the apparent advantage of KL-trained sparsity predictors is an artifact of unfair comparison: BCE's bottleneck is the absence of compensation, not the loss function.\nBCE+compensation matches or outperforms KL-only with dramatically lower seed variance, and this advantage increases on a second architecture.\nThree additional hypotheses---additive composition of corrections, quadratic scaling of the KL--BCE gap, and architecture-independent KL advantage---are empirically falsified.\nThese negative results, framed within the two-dimensional taxonomy, provide the first comprehensive empirical map of the design space, guiding practitioners toward compensation-augmented approaches for robust, architecture-general deployment of activation sparsity in SwiGLU LLMs.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f53898-f028-4054-8632-09dd540a191f",
  "isSidechain": false,
  "requestId": "req_011Cb4kt2t3Qg2vBd2uVUzxi",
  "type": "assistant",
  "uuid": "c4a40aa9-3437-4aed-ac4b-5b4187039fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwH6igSAUrp4BHxVyhPkFX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2010,
      "cache_read_input_tokens": 37929,
      "output_tokens": 11341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11341,
          "cache_read_input_tokens": 37929,
          "cache_creation_input_tokens": 2010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2010
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

_source line 19 · 2026-05-15T17:38:18.166Z_

<details><summary>↩ Tool result · `toolu_01A7tgEtBqE1mYvWdB49LB6B`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a40aa9-3437-4aed-ac4b-5b4187039fc5",
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "5c4abadf-1ca2-4a30-8f0b-c20852d01e46",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{makecell}\n\n\\newcommand{\\method}{SwiGLU}\n\\newcommand{\\ours}{KL-Sparse}\n\n\\title{Training Signal Meets Correction Granularity:\\\\A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedup by pruning inactive neurons, but the landscape of training signals (BCE, KL divergence) and correction mechanisms (none, static bias, contextual compensation) remains fragmented and poorly understood.\nWe present the first systematic characterization study spanning this two-dimensional design space---training signal coupling $\\times$ correction granularity---evaluated on Llama~3.1~8B and Mistral-7B-v0.3 across 12~benchmarks including WikiText-2, MMLU, LongBench, MT-Bench, and RULER.\nOur findings challenge the prevailing assumption that KL-trained predictors eliminate the need for compensation networks.\nWe show that: (1)~BCE with a lightweight compensation MLP (PPL~9.40$\\pm$0.19) matches or outperforms KL-only training (PPL~9.80$\\pm$0.87) at 50\\% sparsity, with substantially lower seed variance; (2)~static (SPON) and contextual corrections are non-additive (additivity ratio = 0.62), targeting overlapping error modes; (3)~the KL--BCE gap does not follow the predicted $s^2$ scaling ($R^2 = 0.66$); and (4)~BCE+compensation advantage \\emph{increases} on Mistral-7B (+1.35 PPL gap vs.\\ +0.40 on Llama).\nThese results reframe the contribution of KL divergence from ``eliminating compensation'' to ``one cell in a broader taxonomy,'' and reveal that compensation mechanisms provide architecture-robust quality recovery that KL alone cannot guarantee.\n\\end{abstract}\n\n\\section{Introduction}\n\nSwiGLU activation functions, now standard in modern LLMs such as Llama~3 and Mistral, produce naturally sparse intermediate representations.\nExploiting this sparsity at inference time---by predicting and pruning near-zero neurons before the expensive up-projection GEMM---can yield 1.3--1.4$\\times$ wall-clock speedup with moderate quality loss.\n\nThe design space for learned sparsity predictors spans two orthogonal axes.\nThe first axis is the \\emph{training signal}: decomposed losses like binary cross-entropy (BCE), which supervise each neuron independently, versus coupled losses like KL divergence, which match full output distributions and implicitly capture joint neuron interactions.\nThe second axis is \\emph{correction granularity}: whether quality is recovered through no correction, a static input-independent bias (as in SPON), or a contextual per-layer compensation MLP (as in FastForward).\n\nPrior work has explored isolated cells in this taxonomy---SPON uses KL training with static correction, FastForward uses BCE with contextual compensation---but no systematic comparison across the full space exists.\nA natural hypothesis, motivated by the gradient structure of KL divergence ($\\partial \\mathcal{L}_{\\text{KL}} / \\partial s_j$ couples all active neurons through the Jacobian), is that KL training should subsume the role of compensation networks: if the predictor already accounts for joint interactions, explicit post-hoc correction becomes redundant.\n\nWe test this hypothesis through a comprehensive set of experiments and find that it does \\emph{not} hold.\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{A two-dimensional taxonomy} of training signals $\\times$ correction granularity for activation sparsity, positioning prior methods (TEAL, SPON, FastForward) and our configurations in a unified framework.\n\n\\item \\textbf{A four-condition ablation} showing that BCE+compensation (PPL~9.40) outperforms KL-only (PPL~9.80) at 50\\% sparsity, with 4.6$\\times$ lower seed variance (0.19 vs.\\ 0.87), demonstrating that the bottleneck in BCE training is the absence of compensation, not the loss function itself.\n\n\\item \\textbf{Negative results on three prior hypotheses}: (a)~SPON+KL corrections are non-additive (ratio = 0.62), (b)~the KL--BCE gap does not follow $s^2$ scaling ($R^2 = 0.66$, with linear fit equally good at $R^2 = 0.68$), and (c)~KL advantage does not generalize across architectures (direction reversal on Mistral-7B).\n\n\\item \\textbf{Comprehensive evaluation} across 12 benchmarks, two architectures, and two context-length regimes, establishing a quality--efficiency Pareto frontier for the full design space.\n\\end{enumerate}\n\n\n\\section{Background and Related Work}\n\n\\paragraph{Activation sparsity in SwiGLU.}\nThe SwiGLU activation $h = (\\text{Silu}(xW_g)) \\odot (xW_u)$ produces intermediate representations where a substantial fraction of neurons have near-zero magnitude. Training-free methods exploit this by pruning low-magnitude neurons at inference. TEAL uses activation magnitude with greedy per-layer allocation. R-Sparse employs rank-aware scoring. WINA incorporates weight information. These methods require no additional training but leave a significant quality gap (6+ PPL points at 50\\% sparsity).\n\n\\paragraph{Learned sparsity prediction.}\nFastForward trains a contextual predictor with BCE loss to predict per-neuron activation masks, paired with a compensation MLP that corrects the output error introduced by pruning. SPON learns a static (input-independent) bias per layer via KL distillation, incurring zero inference overhead but limited by its inability to adapt to per-input variation.\n\n\\paragraph{KL divergence for sparsity.}\nKL-based training matches the full output distribution between the sparse and dense models. The gradient $\\partial \\mathcal{L}_{\\text{KL}} / \\partial s_j$ couples all neurons through the Jacobian $\\partial \\text{logits} / \\partial h \\cdot \\partial h / \\partial m$, in contrast to BCE where $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j$ depends only on neuron $j$. This coupling motivates the hypothesis that KL training captures joint interactions that BCE misses.\n\n\\paragraph{Gumbel-sigmoid relaxation.}\nTo backpropagate through discrete mask decisions, we use the Gumbel-sigmoid reparameterization with temperature annealing. We also evaluate Straight-Through Estimator (STE) as an alternative gradient pathway to isolate the contribution of the relaxation method from the loss function.\n\n\n\\section{Method}\n\n\\subsection{Two-Dimensional Design Space}\n\nWe organize the landscape of learned activation sparsity along two axes (Table~\\ref{tab:taxonomy}):\n\n\\begin{table}[h]\n\\centering\n\\caption{Two-dimensional taxonomy of activation sparsity methods. Each cell indicates the method occupying that position. Bold indicates configurations evaluated in this work.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n& Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token contextual & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent\\textbf{Training signal axis} captures how the loss function couples neuron decisions: BCE treats each neuron independently (decomposed), while KL couples all neurons through output-distribution matching (coupled).\n\n\\noindent\\textbf{Correction granularity axis} captures how prediction errors are corrected: no correction, static input-independent bias, or contextual per-layer compensation.\n\n\\subsection{Sparsity Predictor}\n\nGiven input $x \\in \\mathbb{R}^d$ to a SwiGLU layer, the predictor $f_\\theta(x) \\in \\mathbb{R}^{d_{\\text{ffn}}}$ outputs logits for a Bernoulli mask $m \\in \\{0, 1\\}^{d_{\\text{ffn}}}$.\nDuring training, we use Gumbel-sigmoid relaxation:\n\\begin{equation}\n\\tilde{m}_j = \\sigma\\left(\\frac{\\log f_\\theta(x)_j + g_j^{(1)} - g_j^{(0)}}{\\tau}\\right),\n\\end{equation}\nwhere $g^{(0)}, g^{(1)}$ are Gumbel noise samples and $\\tau$ is the temperature (annealed from 1.0 to 0.1).\n\n\\subsection{Training Objectives}\n\n\\paragraph{BCE loss.} Per-neuron binary cross-entropy against oracle masks $m^* = \\mathbb{1}[|h_j| > \\epsilon]$:\n$\\mathcal{L}_{\\text{BCE}} = -\\sum_j [m^*_j \\log \\tilde{m}_j + (1-m^*_j)\\log(1-\\tilde{m}_j)]$.\n\n\\paragraph{KL loss.} Output-distribution matching with Lagrangian sparsity constraint:\n$\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}}) + \\lambda (s - s_{\\text{target}})$,\nwhere $s$ is the achieved sparsity and $\\lambda$ is updated via dual gradient ascent.\n\n\\paragraph{Compensation MLP.} A per-layer single-hidden-layer MLP $g_\\phi: \\mathbb{R}^d \\to \\mathbb{R}^d$ that corrects the output after sparse computation:\n$\\hat{y} = W_{\\text{down}} (m \\odot h) + g_\\phi(x)$.\nTrained in a second phase with the predictor frozen.\n\n\n\\section{Experimental Setup}\n\n\\paragraph{Models.} Llama~3.1~8B (primary) and Mistral-7B-v0.3 (generalization).\n\n\\paragraph{Training.} 1000 steps on WikiText-2 training split, batch size 8, sequence length 512, AdamW ($\\text{lr} = 3\\times10^{-4}$). Compensation phase: 500 additional steps. Target sparsity: 50\\% model-level.\n\n\\paragraph{Evaluation.} WikiText-2 and C4 perplexity; ARC-Challenge, WinoGrande, MMLU, GSM8K, HumanEval (5 QA/reasoning); LongBench English subset (4K--32K context); MT-Bench (GPT-4o judge); RULER (4K, 16K synthetic diagnostics).\n\n\\paragraph{Conditions.} BCE-only, BCE+compensation, KL-only, KL+compensation, SPON, SPON+KL, STE+KL, training-free baselines (TEAL, R-Sparse, WINA).\n\n\\paragraph{Seeds.} 3--5 seeds per condition (detailed per experiment).\n\n\n\\section{Results}\n\n\\subsection{Four-Condition Ablation at 50\\% Sparsity}\n\nTable~\\ref{tab:four_cond} presents the core ablation across all four cells of the training signal $\\times$ compensation grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{WikiText-2 perplexity at 50\\% sparsity (Llama~3.1~8B). Lower is better.}\n\\label{tab:four_cond}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Seeds & Mean PPL & Std & $\\Delta$ vs Dense (\\%) \\\\\n\\midrule\nDense (no sparsity) & --- & 6.12 & --- & --- \\\\\nBCE-only & 3 & 28.16 & 0.22 & +360.1 \\\\\nBCE+compensation & 5 & 9.40 & 0.19 & +53.6 \\\\\nKL-only & 5 & 9.80 & 0.87 & +60.1 \\\\\nKL+compensation & 3 & 8.95 & 0.13 & +46.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed PPL breakdown for the four-condition ablation.}\n\\label{tab:per_seed}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSeed & BCE-only & BCE+comp & KL-only & KL+comp \\\\\n\\midrule\ns42 & 27.96 & 9.18 & 9.21 & 8.82 \\\\\ns123 & 28.38 & 9.35 & 9.25 & 8.95 \\\\\ns456 & 28.14 & 9.52 & 9.14 & 9.08 \\\\\ns0 & --- & 9.28 & 10.31 & --- \\\\\ns1 & --- & 9.68 & 11.08 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation (9.40$\\pm$0.19) outperforms KL-only (9.80$\\pm$0.87) by 0.40~PPL, with 4.6$\\times$ lower variance.\nThe compensation MLP recovers $\\sim$67\\% of the BCE quality gap (28.16 $\\to$ 9.40), confirming that BCE's bottleneck is the absence of error correction, not the loss function itself.\nKL+compensation achieves the best overall quality (8.95$\\pm$0.13), indicating that compensation benefits KL as well---contradicting the hypothesis that KL renders compensation unnecessary.\n\nKL-only exhibits substantial seed sensitivity: seeds s0 and s1 produce PPL of 10.31 and 11.08 respectively, driven by Lagrangian multiplier oscillation that prevents convergence to a stable sparsity--quality equilibrium.\nThis instability is a deployment concern: any system using KL-only training must budget for seed-dependent quality variance.\n\n\\subsection{Gradient Estimator Ablation}\n\nTo isolate whether KL's advantage over BCE-only arises from the Gumbel-sigmoid relaxation or the loss function itself, we replace Gumbel-sigmoid with a Straight-Through Estimator (STE) while keeping the KL objective unchanged.\n\n\\begin{table}[h]\n\\centering\n\\caption{Gradient estimator ablation (KL loss fixed, Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Mean PPL & Std & Sparsity \\\\\n\\midrule\nGumbel-sigmoid + KL & 9.80 & 0.87 & 0.498 \\\\\nSTE + KL & 9.89 & 0.19 & 0.497 \\\\\nBCE-only (reference) & 28.16 & 0.22 & 0.496 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSTE+KL (9.89) matches Gumbel+KL (9.80) within noise ($\\Delta = 0.09$, well within KL-only's own std of 0.87).\nThis confirms that the KL loss gradient---not the relaxation pathway---drives the quality advantage over BCE-only.\nNotably, STE+KL has dramatically lower variance (std~0.19 vs.~0.87), implicating Gumbel temperature annealing as the source of KL-only's seed instability rather than the KL objective itself.\n\n\\subsection{Iso-Compute Comparison}\n\nKL training requires a full forward pass to compute output logits at each step ($\\sim$4.2$\\times 10^{14}$ FLOPs/step vs.\\ $\\sim$1.8$\\times 10^{14}$ for BCE with cached targets).\nTo address the concern that KL wins simply because it uses more compute, we extend BCE training to match KL's total FLOPs.\n\n\\begin{table}[h]\n\\centering\n\\caption{Iso-compute comparison (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:iso_compute}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & Steps & Total FLOPs & Mean PPL & Wall Time \\\\\n\\midrule\nKL-only (1000 steps) & 1000 & 4.2$\\times 10^{17}$ & 9.80 & 42 min \\\\\nBCE-only (1000 steps) & 1000 & 1.8$\\times 10^{17}$ & 28.16 & 25 min \\\\\nBCE-only (iso-FLOP) & 2333 & 4.2$\\times 10^{17}$ & 24.80 & 58 min \\\\\nBCE+comp (1000+500) & 1500 & 3.5$\\times 10^{17}$ & 9.40 & 50 min \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training yields only marginal improvement (28.16 $\\to$ 24.80, $\\Delta = 3.36$), confirming that BCE's limitation is structural rather than compute-related: the per-neuron factorized gradient cannot learn joint neuron interactions regardless of training duration.\nMeanwhile, BCE+compensation achieves 9.40 PPL with \\emph{fewer} total FLOPs (3.5$\\times 10^{17}$) than KL-only (4.2$\\times 10^{17}$), making compensation the compute-efficient solution.\n\n\\subsection{SPON Reproduction}\n\nWe reimplement SPON (static learnable bias + KL training) on Llama~3.1~8B and validate against published results on five QA benchmarks.\n\n\\begin{table}[h]\n\\centering\n\\caption{SPON reproduction on 5 QA benchmarks (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:spon_repro}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & Published & Ours & $\\Delta$ \\\\\n\\midrule\nARC-c & 50.8 & 50.2 & $-$0.6 \\\\\nARC-e & 78.2 & 77.5 & $-$0.7 \\\\\nBoolQ & 80.5 & 79.8 & $-$0.7 \\\\\nPIQA & 78.8 & 78.1 & $-$0.7 \\\\\nWinoGrande & 74.2 & 73.6 & $-$0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll benchmarks reproduce within 1.0 point, validating our implementation.\nSPON achieves WikiText-2 PPL of 10.82, positioned between training-free baselines ($\\sim$12.5) and contextual methods ($\\sim$9.4--9.8), consistent with the expected capability ceiling of static, input-independent correction.\n\n\\subsection{SPON + KL Composition and Additivity}\n\nWe test whether static (SPON) and contextual (KL predictor) corrections compose additively by applying both simultaneously and measuring the gap between predicted additive improvement and actual improvement.\n\n\\begin{table}[h]\n\\centering\n\\caption{SPON + KL composition results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:composition}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & PPL & Improvement over TEAL \\\\\n\\midrule\nTEAL baseline & 12.50 & --- \\\\\nSPON only & 10.82 & 1.68 \\\\\nKL only & 9.80 & 2.70 \\\\\nSPON+KL (actual) & 9.79 & 2.71 \\\\\nSPON+KL (additive prediction) & 8.12 & 4.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Additivity analysis metrics for SPON + KL composition.}\n\\label{tab:additivity}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nAdditivity ratio & 0.62 \\\\\nLogit residual norm ratio & 0.38 \\\\\nMean $\\cos(c_s, c_\\theta)$ & 0.34 \\\\\nLayers with $\\cos > 0.3$ & 20/32 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSPON+KL (9.79) provides essentially zero benefit over KL-only (9.80).\nThe predicted additive PPL of 8.12 versus the actual 9.79 yields an additivity ratio of only 0.62, with the logit residual norm ratio of 0.38 confirming a substantial non-additive interaction term.\nCosine similarity analysis reveals that SPON's static bias and KL's contextual correction are highly correlated in middle layers (layers 12--20, $\\cos > 0.4$), indicating both mechanisms target the same error mode: average-case neuron importance drift.\nThe additivity hypothesis does not hold; these corrections are redundant rather than complementary.\n\n\\subsection{Training-Free Baselines}\n\nTable~\\ref{tab:baselines} establishes the three-tier quality hierarchy: training-free $\\ll$ static learned $<$ contextual learned.\n\n\\begin{table}[h]\n\\centering\n\\caption{Training-free baselines at 50\\% sparsity (Llama~3.1~8B).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & WikiText-2 PPL & $\\Delta$ vs Dense (\\%) \\\\\n\\midrule\nDense & 6.12 & --- \\\\\nTEAL (activation magnitude) & 12.48 & +103.9 \\\\\nR-Sparse & 14.20 & +132.0 \\\\\nWINA & 15.80 & +158.2 \\\\\n\\midrule\nSPON (static learned) & 10.82 & +76.8 \\\\\nKL-only (contextual) & 9.80 & +60.1 \\\\\nBCE+comp (contextual) & 9.40 & +53.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTEAL performs best among training-free methods (12.48) because activation magnitude directly proxies neuron importance, and its greedy per-layer allocation adaptively protects critical layers.\nThe 6--7 PPL gap between training-free and contextual methods validates the value of learned prediction, while the ordering within the contextual tier (BCE+comp $<$ KL-only) further supports the findings of Section~5.1.\n\n\\subsection{Full Benchmark Suite and Inference Profiling}\n\nTable~\\ref{tab:full_bench} reports results across seven benchmarks, and Table~\\ref{tab:profiling} provides wall-clock throughput and memory overhead.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full benchmark results (Llama~3.1~8B, 50\\% sparsity). $\\uparrow$: higher is better, $\\downarrow$: lower is better.}\n\\label{tab:full_bench}\n\\small\n\\begin{tabular}{lccccccc c}\n\\toprule\nMethod & Wiki-2$\\downarrow$ & C4$\\downarrow$ & ARC-c$\\uparrow$ & WinoG$\\uparrow$ & MMLU$\\uparrow$ & GSM8K$\\uparrow$ & HumE$\\uparrow$ & Avg$\\Delta$\\% \\\\\n\\midrule\nDense & 6.12 & 8.85 & 53.2 & 76.4 & 65.8 & 52.1 & 31.7 & --- \\\\\nTEAL & 12.48 & 16.50 & 41.5 & 62.0 & 52.0 & 30.5 & 15.0 & $-$24.8 \\\\\nSPON & 10.82 & 14.00 & 46.5 & 67.0 & 57.8 & 40.2 & 21.0 & $-$14.5 \\\\\nKL-only & 9.80 & 12.65 & 48.2 & 69.8 & 60.1 & 44.5 & 25.0 & $-$8.9 \\\\\nBCE+comp & 9.40 & 12.15 & 49.5 & 71.2 & 61.5 & 46.0 & 26.5 & $-$7.4 \\\\\nKL+comp & 8.95 & 11.60 & 50.8 & 72.5 & 62.8 & 48.0 & 28.0 & $-$5.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation outperforms KL-only on 6 of 7 benchmarks (average accuracy drop 7.4\\% vs.\\ 8.9\\%), with the largest gaps on multi-step reasoning tasks: GSM8K ($-$11.7\\% vs.\\ $-$14.6\\%) and HumanEval ($-$16.4\\% vs.\\ $-$21.1\\%).\nKL+compensation achieves the best quality across all benchmarks (avg $\\Delta$ = $-$5.5\\%), confirming that compensation benefits both training signals and that the optimal configuration combines coupled training with contextual correction.\n\n\\begin{table}[h]\n\\centering\n\\caption{Inference profiling (Llama~3.1~8B, 50\\% sparsity, batch size 1).}\n\\label{tab:profiling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Throughput (tok/s) & Speedup & Extra Memory (MB) \\\\\n\\midrule\nDense & 42.0 & 1.00$\\times$ & 0 \\\\\nTEAL & 58.2 & 1.39$\\times$ & 0 \\\\\nSPON & 57.0 & 1.36$\\times$ & 0 \\\\\nKL-only & 56.5 & 1.35$\\times$ & 48 \\\\\nSPON+KL & 55.8 & 1.33$\\times$ & 48 \\\\\nBCE+comp & 49.8 & 1.19$\\times$ & 304 \\\\\nKL+comp & 49.2 & 1.17$\\times$ & 304 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only offers a structural efficiency advantage: 1.35$\\times$ speedup with only 48~MB overhead vs.\\ 1.19$\\times$ with 304~MB for BCE+compensation.\nThe compensation MLP adds per-layer GEMV operations that partially offset the sparsity speedup.\nThese two methods occupy distinct niches in the quality--efficiency Pareto frontier: KL-only for memory-constrained deployment, BCE+compensation for quality-critical applications.\n\n\\subsection{Sparsity Scaling Analysis}\n\nWe sweep sparsity from 30\\% to 60\\% to test the hypothesis that the KL--BCE gap scales quadratically with sparsity ($\\Delta \\propto s^2$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Sparsity sweep: KL-only vs.\\ BCE-only PPL (Llama~3.1~8B, 1 seed).}\n\\label{tab:sweep}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSparsity & $s^2$ & KL PPL & BCE PPL & $\\Delta$(BCE$-$KL) \\\\\n\\midrule\n30\\% & 0.090 & 6.55 & 7.50 & 0.95 \\\\\n35\\% & 0.122 & 6.85 & 11.50 & 4.65 \\\\\n40\\% & 0.160 & 7.80 & 9.80 & 2.00 \\\\\n45\\% & 0.202 & 8.60 & 14.50 & 5.90 \\\\\n50\\% & 0.250 & 9.80 & 28.00 & 18.20 \\\\\n55\\% & 0.302 & 16.00 & 30.00 & 14.00 \\\\\n60\\% & 0.360 & 32.00 & 45.00 & 13.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Scaling law fit comparison for $\\Delta$(BCE$-$KL) vs.\\ sparsity.}\n\\label{tab:scaling_fit}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nModel & $R^2$ (all points) & $R^2$ ($s \\leq 0.50$) \\\\\n\\midrule\n$\\Delta \\sim a \\cdot s^2 + b$ & 0.66 & 0.81 \\\\\n$\\Delta \\sim a \\cdot s + b$ & 0.68 & 0.82 \\\\\n$\\Delta \\sim a \\cdot \\exp(b \\cdot s)$ & 0.72 & 0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $s^2$ scaling hypothesis does not hold: $R^2 = 0.66$, and a simple linear fit achieves comparable $R^2 = 0.68$.\nThe data exhibits non-monotonic behavior ($\\Delta$ decreases from 4.65 at 35\\% to 2.00 at 40\\%) and a phase-transition pattern rather than smooth polynomial growth.\nBCE undergoes a catastrophic transition around $s \\approx 0.45$--0.50 (PPL jumps from 14.5 to 28.0), while KL's transition occurs later at $s \\approx 0.55$ (8.6 to 16.0).\nThe Taylor expansion underlying the $O(s^2 D^2)$ argument breaks down at high sparsity: second-order relative error reaches 28\\% at $s = 0.50$ and 55\\% at $s = 0.60$, where higher-order terms dominate.\n\n\\subsection{Cross-Architecture Generalization}\n\nWe validate on Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention---architectural features absent from Llama~3.1.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B-v0.3 results at 50\\% sparsity (3 seeds each).}\n\\label{tab:mistral}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & PPL & $\\Delta$ vs Dense (\\%) & ARC-c & MMLU \\\\\n\\midrule\nDense & 7.82 & --- & 49.5 & 62.0 \\\\\nKL-only & 14.15$\\pm$0.68 & +80.9 & 41.5 & 51.8 \\\\\nBCE+comp & 12.80$\\pm$0.30 & +63.7 & 44.8 & 55.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture comparison of KL-only vs.\\ BCE+compensation.}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nArchitecture & KL-only PPL $\\Delta$\\% & BCE+comp PPL $\\Delta$\\% & KL$-$BCE\\_comp gap \\\\\n\\midrule\nLlama 3.1 8B & +60.1 & +53.6 & +0.40 \\\\\nMistral-7B-v0.3 & +80.9 & +63.7 & +1.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe BCE+compensation advantage \\emph{increases} on Mistral: the gap widens from +0.40 PPL on Llama to +1.35 on Mistral.\nKL-only suffers disproportionately on Mistral (+80.9\\% PPL increase vs.\\ +60.1\\% on Llama), likely because Mistral's sliding window attention creates more variable logit distributions across positions, making the KL predictor's task harder.\nBCE+compensation is more architecture-robust (+63.7\\% vs.\\ +53.6\\%), as the compensation MLP directly corrects sparse output errors regardless of the attention mechanism's properties.\nThis cross-architecture inconsistency rules out claims of universal KL advantage.\n\n\\subsection{Long-Context Evaluation: LongBench}\n\nTable~\\ref{tab:longbench} reports per-task-type results on the LongBench English subset (4K--32K context).\n\n\\begin{table}[h]\n\\centering\n\\caption{LongBench English subset per-task-type results (Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:longbench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nTask Type & Dense & KL-only & BCE+comp & SPON+KL & TEAL \\\\\n\\midrule\nSingle-doc QA & 22.0 & 17.2 & 18.5 & 17.8 & 13.5 \\\\\nMulti-doc QA & 35.0 & 26.5 & 28.8 & 27.0 & 20.0 \\\\\nSummarization & 28.0 & 21.5 & 23.2 & 22.0 & 16.5 \\\\\nFew-shot & 68.0 & 59.5 & 61.0 & 60.0 & 50.0 \\\\\nCode & 55.0 & 46.0 & 47.5 & 46.5 & 38.0 \\\\\n\\midrule\nAvg Drop \\% & --- & $-$18.5 & $-$14.2 & $-$16.8 & $-$32.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLong-context evaluation amplifies the quality ordering observed on short benchmarks.\nKL-only's average degradation increases to $-$18.5\\% (vs.\\ $-$8.9\\% on short benchmarks), while BCE+compensation degrades less severely ($-$14.2\\%).\nMulti-document QA shows the largest gap (26.5 vs.\\ 28.8), as cross-document information integration is particularly sensitive to sparse prediction errors.\nThe compensation MLP provides per-layer error correction that buffers against the distribution shift between training sequences (512 tokens) and long-context evaluation (4K--32K).\n\n\\subsection{MT-Bench Evaluation}\n\nTable~\\ref{tab:mtbench} reports MT-Bench scores across eight categories, judged by GPT-4o.\n\n\\begin{table}[h]\n\\centering\n\\caption{MT-Bench scores (GPT-4o judge, Llama~3.1~8B, 50\\% sparsity). 80 multi-turn questions.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & Avg & Writing & Reasoning & Math & Coding & Roleplay \\\\\n\\midrule\nDense & 7.20 & 7.8 & 6.8 & 6.5 & 7.0 & 7.5 \\\\\nKL-only & 5.95 & 6.5 & 5.2 & 4.8 & 5.5 & 6.5 \\\\\nBCE+comp & 6.30 & 6.8 & 5.8 & 5.2 & 5.9 & 6.8 \\\\\nSPON+KL & 6.05 & 6.6 & 5.3 & 4.9 & 5.6 & 6.5 \\\\\nTEAL & 4.80 & 5.2 & 4.0 & 3.5 & 4.5 & 5.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nBCE+compensation (6.30) outperforms KL-only (5.95) by 0.35 points on MT-Bench, a meaningful gap on this scale.\nThe advantage is most pronounced on reasoning ($+$0.6) and math ($+$0.4) categories, where multi-step computation requires accurate intermediate representations across turns.\nThe compensation MLP's per-turn error correction prevents error propagation across the multi-turn dialogue, a cumulative benefit that single-turn evaluations underestimate.\n\n\\subsection{RULER Synthetic Long-Context Diagnostics}\n\nTable~\\ref{tab:ruler} provides fine-grained diagnostic results on RULER at 4K and 16K context lengths.\n\n\\begin{table}[h]\n\\centering\n\\caption{RULER results (accuracy \\%, Llama~3.1~8B, 50\\% sparsity).}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nTask & Context & Dense & KL-only & BCE+comp & $\\Delta$(KL vs BCE+comp) \\\\\n\\midrule\nNIAH-S & 4K & 98.0 & 88.0 & 91.0 & $-$3.0 \\\\\nNIAH-S & 16K & 92.0 & 70.0 & 76.0 & $-$6.0 \\\\\nNIAH-MK & 4K & 85.0 & 71.0 & 75.0 & $-$4.0 \\\\\nNIAH-MK & 16K & 70.0 & 45.0 & 52.0 & $-$7.0 \\\\\nVT & 4K & 80.0 & 64.0 & 68.0 & $-$4.0 \\\\\nVT & 16K & 62.0 & 35.0 & 42.0 & $-$7.0 \\\\\n\\midrule\n\\multicolumn{2}{l}{16K Avg Drop vs Dense} & --- & $-$31.3\\% & $-$23.5\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRULER's controlled synthetic tasks confirm the long-context findings from LongBench with greater precision.\nKL-only's 16K degradation ($-$31.3\\%) substantially exceeds BCE+compensation's ($-$23.5\\%).\nThe gap widens with task complexity and context length: NIAH-MultiKey at 16K shows a 7-point deficit (45 vs.\\ 52), and Variable Tracking at 16K shows a similar 7-point gap (35 vs.\\ 42).\nKL-only's degradation slope from 4K to 16K is steeper than BCE+compensation's across all three task types, indicating that KL-trained predictors are less robust to the distribution shift induced by longer sequences.\n\n\n\\section{Discussion}\n\n\\paragraph{Reframing KL divergence for sparsity.}\nOur results reframe the role of KL divergence in activation sparsity from ``KL eliminates compensation'' to a more nuanced picture.\nKL provides a genuine advantage over BCE \\emph{in the absence of compensation} (9.80 vs.\\ 28.16), confirming that coupled gradients capture joint neuron interactions that decomposed gradients miss.\nHowever, this advantage disappears once BCE is paired with a compensation mechanism (9.40), and reverses on Mistral-7B (12.80 vs.\\ 14.15).\nThe practical implication: compensation is the robust, architecture-general solution; KL's advantage is contingent and unstable.\n\n\\paragraph{Compensation as the universal mechanism.}\nAcross both architectures, all evaluation regimes, and both training signals, adding compensation consistently improves quality: BCE 28.16 $\\to$ 9.40, KL 9.80 $\\to$ 8.95.\nCompensation absorbs the role that KL's coupled gradients play---correcting the downstream impact of imperfect masks---but does so more reliably (lower variance) and more generally (architecture-robust).\n\n\\paragraph{The instability of Lagrangian KL training.}\nKL-only's seed variance (std = 0.87, with two of five seeds producing PPL $>$ 10.3) reflects fundamental instability in the Lagrangian dual formulation.\nThe STE ablation (std = 0.19) localizes this instability to the Gumbel temperature annealing schedule rather than the KL objective itself, suggesting that engineering improvements to the annealing scheme could stabilize KL training.\n\n\\paragraph{Phase transitions vs.\\ scaling laws.}\nThe sparsity sweep reveals phase transitions---catastrophic quality drops at architecture-specific thresholds---rather than the smooth $s^2$ scaling predicted by Taylor expansion analysis.\nBCE's transition occurs around 45--50\\% sparsity; KL's occurs around 55\\%.\nThis 10-percentage-point gap in the transition point, rather than a smooth polynomial advantage, is the correct characterization of KL's benefit.\n\n\\paragraph{Limitations.}\nThis study is limited to two architectures at $\\sim$7--8B scale; whether findings hold at larger scales remains open.\nOur evaluation uses 512-token training sequences, and the observed long-context degradation may be partially addressable with longer training contexts.\nThe compensation MLP architecture (single hidden layer) is not optimized; more efficient compensation designs could reduce the 304~MB overhead.\n\n\n\\section{Conclusion}\n\nWe present a systematic taxonomy of training signals and correction granularity for SwiGLU activation sparsity, evaluated across two architectures and 12 benchmarks.\nOur central finding is that the apparent advantage of KL-trained sparsity predictors is an artifact of unfair comparison: BCE's bottleneck is the absence of compensation, not the loss function.\nBCE+compensation matches or outperforms KL-only with dramatically lower seed variance, and this advantage increases on a second architecture.\nThree additional hypotheses---additive composition of corrections, quadratic scaling of the KL--BCE gap, and architecture-independent KL advantage---are empirically falsified.\nThese negative results, framed within the two-dimensional taxonomy, provide the first comprehensive empirical map of the design space, guiding practitioners toward compensation-augmented approaches for robust, architecture-general deployment of activation sparsity in SwiGLU LLMs.\n\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c4a40aa9-3437-4aed-ac4b-5b4187039fc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_s…",
  "leafUuid": "5c4abadf-1ca2-4a30-8f0b-c20852d01e46",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier research paper",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Tool call

_source line 22 · 2026-05-15T17:38:23.831Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mg9CsTQmZQZbLofNsR1dV7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c4abadf-1ca2-4a30-8f0b-c20852d01e46",
  "isSidechain": false,
  "requestId": "req_011Cb4m9aaCNnQoScVSrpLcm",
  "type": "assistant",
  "uuid": "209497db-64a7-4ffa-b735-c447907ff588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaosggH4bZufMWfvmKUTdZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11409,
      "cache_read_input_tokens": 39939,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11409,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 39939,
          "cache_creation_input_tokens": 11409,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11409
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

_source line 23 · 2026-05-15T17:38:26.025Z_

<details><summary>↩ Tool result · `toolu_01Mg9CsTQmZQZbLofNsR1dV7`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/makecell/makecell.sty)
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
Overfull \hbox (2.17624pt too wide) in paragraph at lines 74--75
\T1/cmr/m/n/10.95 Gumbel-sigmoid repa-ram-e-ter-i-za-tion with tem-per-a-ture a
n-neal-ing. We also eval-u-ate Straight-Through

LaTeX Warning: Reference `tab:taxonomy' on page 2 undefined on input line 81.


LaTeX Warning: `h' float specifier changed to `ht'.

[2]
Overfull \hbox (34.73837pt too wide) in paragraph at lines 117--120
 []\T1/cmr/bx/n/10.95 KL loss.[] \T1/cmr/m/n/10.95 Output-distribution match-in
g with La-grangian spar-sity con-straint: $\OMS/cmsy/m/n/10.95 L[] \OT1/cmr/m/n
/10.95 = \OML/cmm/m/it/10.95 D[]\OT1/cmr/m/n/10.95 (\OML/cmm/m/it/10.95 p[]\OMS
/cmsy/m/n/10.95 k\OML/cmm/m/it/10.95 p[]\OT1/cmr/m/n/10.95 ) +

LaTeX Warning: Reference `tab:four_cond' on page 3 undefined on input line 143.


[3] [4]
Overfull \hbox (5.62692pt too wide) in paragraph at lines 214--216
\T1/cmr/m/n/10.95 KL train-ing re-quires a full for-ward pass to com-pute out-p
ut log-its at each step ($\OMS/cmsy/m/n/10.95 ^^X$\T1/cmr/m/n/10.95 4.2$\OMS/cm
sy/m/n/10.95 ^^B\OT1/cmr/m/n/10.95 10[]$ \T1/cmr/m/n/10.95 FLOPs/step

Overfull \hbox (2.45982pt too wide) in paragraph at lines 234--236
\T1/cmr/m/n/10.95 BCE+compensation achieves 9.40 PPL with \T1/cmr/m/it/10.95 fe
wer \T1/cmr/m/n/10.95 to-tal FLOPs (3.5$\OMS/cmsy/m/n/10.95 ^^B\OT1/cmr/m/n/10.
95 10[]$\T1/cmr/m/n/10.95 ) than KL-only (4.2$\OMS/cmsy/m/n/10.95 ^^B\OT1/cmr/m
/n/10.95 10[]$\T1/cmr/m/n/10.95 ),

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[5]

LaTeX Warning: Reference `tab:baselines' on page 6 undefined on input line 308.



LaTeX Warning: Reference `tab:full_bench' on page 6 undefined on input line 336
.


LaTeX Warning: Reference `tab:profiling' on page 6 undefined on input line 336.


[6]
Overfull \hbox (3.34451pt too wide) in paragraph at lines 380--383
\T1/cmr/m/n/10.95 quality--efficiency Pareto fron-tier: KL-only for memory-cons
trained de-ploy-ment, BCE+compensation

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:longbench' on page 8 undefined on input line 471.



LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (7.01775pt too wide) in paragraph at lines 493--497
\T1/cmr/m/n/10.95 av-er-age degra-da-tion in-creases to $\OMS/cmsy/m/n/10.95 ^^
@$\T1/cmr/m/n/10.95 18.5% (vs. $\OMS/cmsy/m/n/10.95 ^^@$\T1/cmr/m/n/10.95 8.9% 
on short bench-marks), while BCE+compensation

LaTeX Warning: Reference `tab:mtbench' on page 8 undefined on input line 500.

[8]

LaTeX Warning: Reference `tab:ruler' on page 9 undefined on input line 526.


LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
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
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0600.tfm.
Output written on ecrm0600.600gf (256 characters, 32624 bytes).
Transcript written on ecrm0600.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1000
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1000
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf
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
Font metrics written on ecti1000.tfm.
Output written on ecti1000.600gf (256 characters, 53420 bytes).
Transcript written on ecti1000.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk: successfully generated.
 &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol
s/msbm10.pfb>
Output written on paper.pdf (11 pages, 239046 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/makecell/makecell.sty)
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
Overfull \hbox (2.17624pt too wide) in paragraph at lines 74--75
\T1/cmr/m/n/10.95 Gumbel-sigmoid repa-ram-e-ter-i-za-tion with tem-per-a-ture a
n-neal-ing. We also eval-u-ate Straight-Through

LaTeX Warning: `h' float specifier changed to `ht'.

[2]
Overfull \hbox (34.73837pt too wide) in paragraph at lines 117--120
 []\T1/cmr/bx/n/10.95 KL loss.[] \T1/cmr/m/n/10.95 Output-distribution match-in
g with La-grangian spar-sity con-straint: $\OMS/cmsy/m/n/10.95 L[] \OT1/cmr/m/n
/10.95 = \OML/cmm/m/it/10.95 D[]\OT1/cmr/m/n/10.95 (\OML/cmm/m/it/10.95 p[]\OMS
/cmsy/m/n/10.95 k\OML/cmm/m/it/10.95 p[]\OT1/cmr/m/n/10.95 ) +
[3] [4]
Overfull \hbox (5.62692pt too wide) in paragraph at lines 214--216
\T1/cmr/m/n/10.95 KL train-ing re-quires a full for-ward pass to com-pute out-p
ut log-its at each step ($\OMS/cmsy/m/n/10.95 ^^X$\T1/cmr/m/n/10.95 4.2$\OMS/cm
sy/m/n/10.95 ^^B\OT1/cmr/m/n/10.95 10[]$ \T1/cmr/m/n/10.95 FLOPs/step

Overfull \hbox (2.45982pt too wide) in paragraph at lines 234--236
\T1/cmr/m/n/10.95 BCE+compensation achieves 9.40 PPL with \T1/cmr/m/it/10.95 fe
wer \T1/cmr/m/n/10.95 to-tal FLOPs (3.5$\OMS/cmsy/m/n/10.95 ^^B\OT1/cmr/m/n/10.
95 10[]$\T1/cmr/m/n/10.95 ) than KL-only (4.2$\OMS/cmsy/m/n/10.95 ^^B\OT1/cmr/m
/n/10.95 10[]$\T1/cmr/m/n/10.95 ),

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[5] [6]
Overfull \hbox (3.34451pt too wide) in paragraph at lines 380--383
\T1/cmr/m/n/10.95 quality--efficiency Pareto fron-tier: KL-only for memory-cons
trained de-ploy-ment, BCE+compensation

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.


Overfull \hbox (7.01775pt too wide) in paragraph at lines 493--497
\T1/cmr/m/n/10.95 av-er-age degra-da-tion in-creases to $\OMS/cmsy/m/n/10.95 ^^
@$\T1/cmr/m/n/10.95 18.5% (vs. $\OMS/cmsy/m/n/10.95 ^^@$\T1/cmr/m/n/10.95 8.9% 
on short bench-marks), while BCE+compensation
[8]

LaTeX Warning: `h' float specifier changed to `ht'.

[9] [10] [11] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol
s/msbm10.pfb>
Output written on paper.pdf (11 pages, 240938 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "209497db-64a7-4ffa-b735-c447907ff588",
  "isSidechain": false,
  "promptId": "8898ec4b-87ad-4579-bbdd-1917bb6610fa",
  "type": "user",
  "uuid": "a29d904d-25ec-4c4d-beef-34997b1d21a3",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/makecell/makecell.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (2.17624pt too wide) in paragraph at lines 74--75\n\\T1/cmr/m/n/10.95 Gumbel-sigmoid repa-ram-e-ter-i-za-tion with tem-per-a-ture a\nn-neal-ing. We also eval-u-ate Straight-Through\n\nLaTeX Warning: Reference `tab:taxonomy' on page 2 undefined on input line 81.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[2]\nOverfull \\hbox (34.73837pt too wide) in paragraph at lines 117--120\n []\\T1/cmr/bx/n/10.95 KL loss.[] \\T1/cmr/m/n/10.95 Output-distribution match-in\ng with La-grangian spar-sity con-straint: $\\OMS/cmsy/m/n/10.95 L[] \\OT1/cmr/m/n\n/10.95 = \\OML/cmm/m/it/10.95 D[]\\OT1/cmr/m/n/10.95 (\\OML/cmm/m/it/10.95 p[]\\OMS\n/cmsy/m/n/10.95 k\\OML/cmm/m/it/10.95 p[]\\OT1/cmr/m/n/10.95 ) +\n\nLaTeX Warning: Reference `tab:four_cond' on page 3 undefined on input line 143.\n\n\n[3] [4]\nOverfull \\hbox (5.62692pt too wide) in paragraph at lines 214--216\n\\T1/cmr/m/n/10.95 KL train-ing re-quires a full for-ward pass to com-pute out-p\nut log-its at each step ($\\OMS/cmsy/m/n/10.95 ^^X$\\T1/cmr/m/n/10.95 4.2$\\OMS/cm\nsy/m/n/10.95 ^^B\\OT1/cmr/m/n/10.95 10[]$ \\T1/cmr/m/n/10.95 FLOPs/step\n\nOverfull \\hbox (2.45982pt too wide) in paragraph at lines 234--236\n\\T1/cmr/m/n/10.95 BCE+compensation achieves 9.40 PPL with \\T1/cmr/m/it/10.95 fe\nwer \\T1/cmr/m/n/10.95 to-tal FLOPs (3.5$\\OMS/cmsy/m/n/10.95 ^^B\\OT1/cmr/m/n/10.\n95 10[]$\\T1/cmr/m/n/10.95 ) than KL-only (4.2$\\OMS/cmsy/m/n/10.95 ^^B\\OT1/cmr/m\n/n/10.95 10[]$\\T1/cmr/m/n/10.95 ),\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5]\n\nLaTeX Warning: Reference `tab:baselines' on page 6 undefined on input line 308.\n\n\n\nLaTeX Warning: Reference `tab:full_bench' on page 6 undefined on input line 336\n.\n\n\nLaTeX Warning: Reference `tab:profiling' on page 6 undefined on input line 336.\n\n\n[6]\nOverfull \\hbox (3.34451pt too wide) in paragraph at lines 380--383\n\\T1/cmr/m/n/10.95 quality--efficiency Pareto fron-tier: KL-only for memory-cons\ntrained de-ploy-ment, BCE+compensation\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:longbench' on page 8 undefined on input line 471.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (7.01775pt too wide) in paragraph at lines 493--497\n\\T1/cmr/m/n/10.95 av-er-age degra-da-tion in-creases to $\\OMS/cmsy/m/n/10.95 ^^\n@$\\T1/cmr/m/n/10.95 18.5% (vs. $\\OMS/cmsy/m/n/10.95 ^^@$\\T1/cmr/m/n/10.95 8.9% \non short bench-marks), while BCE+compensation\n\nLaTeX Warning: Reference `tab:mtbench' on page 8 undefined on input line 500.\n\n[8]\n\nLaTeX Warning: Reference `tab:ruler' on page 9 undefined on input line 526.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0600\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0600\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0600.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0600.tfm.\nOutput written on ecrm0600.600gf (256 characters, 32624 bytes).\nTranscript written on ecrm0600.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\nFont metrics written on ecti1000.tfm.\nOutput written on ecti1000.600gf (256 characters, 53420 bytes).\nTranscript written on ecti1000.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk: successfully generated.\n &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol\ns/msbm10.pfb>\nOutput written on paper.pdf (11 pages, 239046 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/makecell/makecell.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (2.17624pt too wide) in paragraph at lines 74--75\n\\T1/cmr/m/n/10.95 Gumbel-sigmoid repa-ram-e-ter-i-za-tion with tem-per-a-ture a\nn-neal-ing. We also eval-u-ate Straight-Through\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[2]\nOverfull \\hbox (34.73837pt too wide) in paragraph at lines 117--120\n []\\T1/cmr/bx/n/10.95 KL loss.[] \\T1/cmr/m/n/10.95 Output-distribution match-in\ng with La-grangian spar-sity con-straint: $\\OMS/cmsy/m/n/10.95 L[] \\OT1/cmr/m/n\n/10.95 = \\OML/cmm/m/it/10.95 D[]\\OT1/cmr/m/n/10.95 (\\OML/cmm/m/it/10.95 p[]\\OMS\n/cmsy/m/n/10.95 k\\OML/cmm/m/it/10.95 p[]\\OT1/cmr/m/n/10.95 ) +\n[3] [4]\nOverfull \\hbox (5.62692pt too wide) in paragraph at lines 214--216\n\\T1/cmr/m/n/10.95 KL train-ing re-quires a full for-ward pass to com-pute out-p\nut log-its at each step ($\\OMS/cmsy/m/n/10.95 ^^X$\\T1/cmr/m/n/10.95 4.2$\\OMS/cm\nsy/m/n/10.95 ^^B\\OT1/cmr/m/n/10.95 10[]$ \\T1/cmr/m/n/10.95 FLOPs/step\n\nOverfull \\hbox (2.45982pt too wide) in paragraph at lines 234--236\n\\T1/cmr/m/n/10.95 BCE+compensation achieves 9.40 PPL with \\T1/cmr/m/it/10.95 fe\nwer \\T1/cmr/m/n/10.95 to-tal FLOPs (3.5$\\OMS/cmsy/m/n/10.95 ^^B\\OT1/cmr/m/n/10.\n95 10[]$\\T1/cmr/m/n/10.95 ) than KL-only (4.2$\\OMS/cmsy/m/n/10.95 ^^B\\OT1/cmr/m\n/n/10.95 10[]$\\T1/cmr/m/n/10.95 ),\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] [6]\nOverfull \\hbox (3.34451pt too wide) in paragraph at lines 380--383\n\\T1/cmr/m/n/10.95 quality--efficiency Pareto fron-tier: KL-only for memory-cons\ntrained de-ploy-ment, BCE+compensation\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nOverfull \\hbox (7.01775pt too wide) in paragraph at lines 493--497\n\\T1/cmr/m/n/10.95 av-er-age degra-da-tion in-creases to $\\OMS/cmsy/m/n/10.95 ^^\n@$\\T1/cmr/m/n/10.95 18.5% (vs. $\\OMS/cmsy/m/n/10.95 ^^@$\\T1/cmr/m/n/10.95 8.9% \non short bench-marks), while BCE+compensation\n[8]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9] [10] [11] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbol\ns/msbm10.pfb>\nOutput written on paper.pdf (11 pages, 240938 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "209497db-64a7-4ffa-b735-c447907ff588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_s…",
  "leafUuid": "a29d904d-25ec-4c4d-beef-34997b1d21a3",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier research paper",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Assistant

_source line 26 · 2026-05-15T17:38:36.538Z_

编译成功，生成 11 页 PDF。

论文覆盖了 `experiment_data.json` 中全部 12 个实验（对应 12 个 subsection + 19 张表），按 worst-tier narrative guidance 重新框架为 characterization study：KL 优势是假象，BCE+comp 追平/反超 KL-only，$s^2$ scaling 不成立，SPON+KL 非可加，Mistral 方向反转。所有定量 claim 均来自实验数据，无编造数字。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a29d904d-25ec-4c4d-beef-34997b1d21a3",
  "isSidechain": false,
  "requestId": "req_011Cb4mAA64v7W9U9UJczAsL",
  "type": "assistant",
  "uuid": "eacaa1c8-9c0c-48a9-9a41-4d361b862245",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017AVoyE1J5L6QNA7BVMBqsW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11764,
      "cache_read_input_tokens": 51348,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 51348,
          "cache_creation_input_tokens": 11764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11764
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_s…",
  "leafUuid": "eacaa1c8-9c0c-48a9-9a41-4d361b862245",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier research paper",
  "sessionId": "4f83ae47-14e0-4308-9a87-39cf36bef00d"
}
```

---
