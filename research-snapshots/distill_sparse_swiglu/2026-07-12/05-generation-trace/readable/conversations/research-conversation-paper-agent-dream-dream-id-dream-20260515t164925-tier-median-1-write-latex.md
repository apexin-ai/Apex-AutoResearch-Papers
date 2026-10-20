# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/e4efbda2-19e3-49b7-bacb-45a8e0db6a48.jsonl`
- **Structured JSON:** [`747eef7090dfbade81d4.json`](../../sessions/74/747eef7090dfbade81d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T17:30:29.444Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T17:30:29.444Z",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 从\"KL categorically better\"调整为\"KL eliminates compensation overhead at quality parity\"—— KL-only (PPL ~9.5) 击败 BCE+comp (~11.6)，核心贡献变为效率：同等或更好质量下省掉256MB compensation参数， 推理pipeline更简单。Claim 2 弱化为\"empirically observed partial additivity\"，interaction residual ~22% 需要honest characterization而非clean decomposition。Claim 3 降级为appendix-level\"consistent empirical trend\"， R²~0.88不足以声称precise quantitative law。Paper重心转向taxonomy + systematic ablation的方法论贡献。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T17:30:29.450Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T17:30:29.450Z",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-15T17:30:29.512Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 从"KL categorically better"调整为"KL eliminates compensation overhead at quality parity"—— KL-only (PPL ~9.5) 击败 BCE+comp (~11.6)，核心贡献变为效率：同等或更好质量下省掉256MB compensation参数， 推理pipeline更简单。Claim 2 弱化为"empirically observed partial additivity"，interaction residual ~22% 需要honest characterization而非clean decomposition。Claim 3 降级为appendix-level"consistent empirical trend"， R²~0.88不足以声称precise quantitative law。Paper重心转向taxonomy + systematic ablation的方法论贡献。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "1c1cf360-59ce-4829-a22e-8303483b1757",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T17:30:29.507Z_

```json
{
  "parentUuid": "1c1cf360-59ce-4829-a22e-8303483b1757",
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
  "uuid": "2b35c76e-6d22-44c8-b6a3-9170f0017539",
  "timestamp": "2026-05-15T17:30:29.507Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T17:30:29.507Z_

```json
{
  "parentUuid": "2b35c76e-6d22-44c8-b6a3-9170f0017539",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "28939a02-a3cf-4b6b-a31a-69e011efe630",
  "timestamp": "2026-05-15T17:30:29.507Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
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
  "aiTitle": "Generate simulated research paper for dream_20260515T164925",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Assistant

_source line 7 · 2026-05-15T17:30:31.977Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28939a02-a3cf-4b6b-a31a-69e011efe630",
  "isSidechain": false,
  "requestId": "req_011Cb4kZ3JKFS1ng2tYnXtyX",
  "type": "assistant",
  "uuid": "028da8d2-7ac3-4180-8fcc-c5e534d5685d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRcQBtJJzBQ8oW3F6PYHvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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

_source line 8 · 2026-05-15T17:30:32.950Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KqaTEi6b4e4nmPBRTqiGtN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "028da8d2-7ac3-4180-8fcc-c5e534d5685d",
  "isSidechain": false,
  "requestId": "req_011Cb4kZ3JKFS1ng2tYnXtyX",
  "type": "assistant",
  "uuid": "7da3a816-073f-4a79-a281-5c08b21b5f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRcQBtJJzBQ8oW3F6PYHvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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

_source line 9 · 2026-05-15T17:30:33.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rn2pQr1fo4YBuDZkDYfcVW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7da3a816-073f-4a79-a281-5c08b21b5f8f",
  "isSidechain": false,
  "requestId": "req_011Cb4kZ3JKFS1ng2tYnXtyX",
  "type": "assistant",
  "uuid": "8eac7291-5dab-4502-820f-fdb0f91e99b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NRcQBtJJzBQ8oW3F6PYHvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11243,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11243
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

_source line 10 · 2026-05-15T17:30:33.284Z_

<details><summary>↩ Tool result · `toolu_01Rn2pQr1fo4YBuDZkDYfcVW`</summary>

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
  "parentUuid": "8eac7291-5dab-4502-820f-fdb0f91e99b4",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "926090bf-0e2c-4ecc-a7ef-0ccd2263ac85",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating ~256MB of inference-time compensation weights and per-layer GEMV overhead. (Headline claim)\n\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\n\n3. **KL advantage scales quadratically with sparsity**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). Testable prediction: KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] — demonstrating that output-distribution distillation subsumes error compensation and enabling a simpler, lighter inference pipeline.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "8eac7291-5dab-4502-820f-fdb0f91e99b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T17:30:33.322Z_

<details><summary>↩ Tool result · `toolu_01KqaTEi6b4e4nmPBRTqiGtN`</summary>

```text
1	[
2	  {
3	    "name": "Four-condition ablation @ 50% sparsity",
4	    "description": "补充KL-only 2 seeds (s0, s1) 达到5-seed headline；新增BCE+comp 5 seeds； 新增KL+comp 3 seeds。与已有BCE-only 3 seeds和KL-only 3 seeds组合。\n",
5	    "results": {
6	      "kl_only_wikitext2_ppl_mean": 9.53,
7	      "kl_only_wikitext2_ppl_std": 0.41,
8	      "kl_only_wikitext2_ppl_seeds": [
9	        9.21,
10	        9.25,
11	        9.14,
12	        9.85,
13	        10.18
14	      ],
15	      "kl_only_model_sparsity": 0.498,
16	      "bce_only_wikitext2_ppl_mean": 28.16,
17	      "bce_only_wikitext2_ppl_std": 0.21,
18	      "bce_comp_wikitext2_ppl_mean": 11.56,
19	      "bce_comp_wikitext2_ppl_std": 0.61,
20	      "bce_comp_wikitext2_ppl_seeds": [
21	        11.2,
22	        11.8,
23	        12.5,
24	        10.8,
25	        11.5
26	      ],
27	      "bce_comp_param_overhead_mb": 256,
28	      "kl_comp_wikitext2_ppl_mean": 9.05,
29	      "kl_comp_wikitext2_ppl_std": 0.15,
30	      "kl_comp_wikitext2_ppl_seeds": [
31	        9.05,
32	        9.2,
33	        8.9
34	      ],
35	      "kl_only_vs_bce_comp_gap": 2.03,
36	      "kl_comp_vs_kl_only_improvement": 0.48,
37	      "dense_wikitext2_ppl": 6.12
38	    },
39	    "tables": [
40	      {
41	        "name": "Table 1: Four-condition ablation at 50% model-level sparsity (Llama 3.1 8B)",
42	        "columns": [
43	          "Condition",
44	          "WikiText-2 PPL (↓)",
45	          "Seeds",
46	          "Compensation Params",
47	          "Pipeline Complexity"
48	        ],
49	        "rows": [
50	          [
51	            "Dense (reference)",
52	            "6.12",
53	            "—",
54	            "—",
55	            "—"
56	          ],
57	          [
58	            "BCE-only",
59	            "28.16 ± 0.21",
60	            3,
61	            0,
62	            "Simple"
63	          ],
64	          [
65	            "BCE + compensation",
66	            "11.56 ± 0.61",
67	            5,
68	            "256 MB",
69	            "Complex"
70	          ],
71	          [
72	            "KL-only",
73	            "9.53 ± 0.41",
74	            5,
75	            0,
76	            "Simple"
77	          ],
78	          [
79	            "KL + compensation",
80	            "9.05 ± 0.15",
81	            3,
82	            "256 MB",
83	            "Complex"
84	          ]
85	        ]
86	      }
87	    ],
88	    "figures": [],
89	    "analysis": "Headline result支持revised Claim 1：KL-only在质量上优于BCE+comp (9.53 vs 11.56)， 同时完全省去compensation网络。KL+comp的微弱提升(0.48 PPL)表明compensation对KL是冗余的， 而对BCE是必需的(28.16→11.56)。这将论文核心message从\"KL is categorically better\" 调整为\"KL eliminates compensation overhead while achieving better quality\"—— 更nuanced但仍有明确的practical implication。 Seed方差增大(std 0.41)需要在paper中transparent报告，但5-seed mean的confidence interval 仍完全在BCE+comp之下。\n\n\nKL-only: 新增s0/s1引入方差增大（s1=10.18为较弱种子），5-seed std从0.05升至0.41。 这反映Gumbel-sigmoid采样在不同初始化下的探索路径差异——部分种子的predictor在特定层学到次优mask分布， 导致几个层的neuron selection偏差累积。均值9.53仍在9.0-10.5范围内。\nBCE+comp: compensation网络（per-layer MLP, ~256MB）有效修正BCE predictor的mask错误： BCE-only的per-neuron独立预测在高sparsity下产生大量joint interaction error， compensation网络通过residual connection学习修正sparse hidden state的drift。 PPL从28.16降至11.56，compensation确实有用（回收~16.6 PPL）。 但BCE的factorized gradient本身限制了mask质量ceiling，compensation只能修正而非预防错误。\nKL+comp: compensation对KL的提升微弱（9.53→9.05, 仅0.48 PPL）。 因为KL loss通过d_logits/dh * dh/dm的gradient coupling已经在训练时优化了joint neuron selection， 留给compensation修正的residual error很小。这证明KL在训练阶段\"preempt\"了compensation需要解决的问题。\n核心结论：KL-only (9.53) < BCE+comp (11.56)，且KL不需要256MB compensation overhead。 KL+comp的diminishing return进一步确认compensation对KL是冗余的。\n"
90	  },
91	  {
92	    "name": "STE baseline: KL loss + Straight-Through Estimator",
93	    "description": "用STE替换Gumbel-sigmoid作为gradient estimator，保持KL loss不变。 3 seeds。隔离KL优势中loss function vs relaxation method的各自贡献。\n",
94	    "results": {
95	      "kl_ste_wikitext2_ppl_mean": 14.7,
96	      "kl_ste_wikitext2_ppl_std": 0.6,
97	      "kl_ste_wikitext2_ppl_seeds": [
98	        14.7,
99	        15.3,
100	        14.1
101	      ],
102	      "kl_ste_model_sparsity": 0.498,
103	      "total_gain_over_bce": 18.63,
104	      "gain_from_kl_loss": 13.46,
105	      "gain_from_gumbel": 5.17,
106	      "gumbel_contribution_pct": 27.8
107	    },
108	    "tables": [
109	      {
110	        "name": "Table 2: Loss function vs relaxation method ablation",
111	        "columns": [
112	          "Condition",
113	          "Loss",
114	          "Relaxation",
115	          "WikiText-2 PPL",
116	          "Gain over BCE-only"
117	        ],
118	        "rows": [
119	          [
120	            "BCE-only",
121	            "BCE",
122	            "STE",
123	            "28.16",
124	            "—"
125	          ],
126	          [
127	            "KL + STE",
128	            "KL",
129	            "STE",
130	            "14.70 ± 0.60",
131	            "13.46 (72%)"
132	          ],
133	          [
134	            "KL + Gumbel",
135	            "KL",
136	            "Gumbel-σ",
137	            "9.53 ± 0.41",
138	            "18.63 (100%)"
139	          ]
140	        ]
141	      }
142	    ],
143	    "figures": [],
144	    "analysis": "KL loss贡献72%的improvement，Gumbel贡献28%。两者都是necessary component。 这回答reviewer concern #3: gains不是purely from Gumbel relaxation，KL loss本身是主要driver。 同时也表明gradient estimator的选择有meaningful impact，为future work （更好的relaxation methods）留下空间。\n\n\nSTE将hard threshold的gradient设为1（identity），丢失了neuron importance的magnitude信息。 Gumbel-sigmoid在forward pass中通过temperature-controlled soft sampling保留了importance ranking的连续性， 使KL gradient能够区分\"barely active\"和\"strongly active\"的neurons。\nKL+STE (14.70) 仍大幅优于BCE-only (28.16)，因为KL loss的joint coupling效应不依赖relaxation方法—— 即使用STE的biased gradient，KL的∂logits/∂mask仍传递了output-distribution level的supervision。 但STE的gradient bias导致predictor在边界neurons（importance接近threshold的neurons）上做出次优决策， 累积~5 PPL的损失。\nGumbel贡献~28%的gain，说明\"loss和relaxation都重要\"——KL loss是主要贡献者（72%）， 但Gumbel的smooth gradient对于fine-grained mask optimization不可或缺。 这防御了reviewer concern \"Gumbel relaxation, not KL, explains gains\"。\n"
145	  },
146	  {
147	    "name": "Iso-compute BCE comparison",
148	    "description": "扩展BCE训练步数以匹配KL的total FLOPs。KL需要per-step dense forward pass获取logits， BCE可用cached targets，因此BCE per-step成本远低于KL。等量计算下BCE可训练更多步。\n",
149	    "results": {
150	      "kl_per_step_tflops": 66.0,
151	      "bce_per_step_tflops": 0.8,
152	      "kl_total_training_hours": 3.8,
153	      "bce_standard_training_hours": 0.4,
154	      "bce_isocompute_training_steps": 33000,
155	      "bce_isocompute_training_hours": 3.8,
156	      "bce_standard_ppl": 28.16,
157	      "bce_isocompute_ppl_mean": 23.5,
158	      "bce_isocompute_ppl_std": 0.7,
159	      "bce_isocompute_ppl_seeds": [
160	        23.5,
161	        24.2,
162	        22.8
163	      ],
164	      "kl_only_ppl_mean": 9.53,
165	      "gap_kl_vs_bce_isocompute": 13.97
166	    },
167	    "tables": [
168	      {
169	        "name": "Table 3: Iso-compute training comparison",
170	        "columns": [
171	          "Condition",
172	          "Per-step TFLOPs",
173	          "Total Steps",
174	          "GPU-hours",
175	          "WikiText-2 PPL"
176	        ],
177	        "rows": [
178	          [
179	            "KL + Gumbel",
180	            66.0,
181	            1000,
182	            3.8,
183	            "9.53 ± 0.41"
184	          ],
185	          [
186	            "BCE (standard)",
187	            0.8,
188	            1000,
189	            0.4,
190	            "28.16 ± 0.21"
191	          ],
192	          [
193	            "BCE (iso-compute)",
194	            0.8,
195	            33000,
196	            3.8,
197	            "23.50 ± 0.70"
198	          ]
199	        ]
200	      }
201	    ],
202	    "figures": [],
203	    "analysis": "直接回答reviewer concern #2 \"KL wins only because more compute\"。 等量计算下KL仍领先14 PPL points，BCE的per-neuron independence assumption是根本瓶颈。 附带发现：BCE training cost极低（0.4 vs 3.8 GPU-hours），在不追求最优质量的场景下 BCE+comp仍有实用价值（training便宜，compensation弥补质量），但KL在quality-critical场景下 是strictly better choice。\n\n\nBCE per-step成本远低于KL（0.8 vs 66 TFLOPs），因为BCE只需predictor forward+binary target比对， 无需base model forward pass。等量计算下BCE获得~33x训练步数。\n额外训练将BCE PPL从28.16降至23.50（降低16.5%）。改善来源： (1) predictor在更多数据上泛化更好，(2) 更充分的convergence。 但改善呈sharp diminishing returns——BCE在~5000步后已接近per-neuron prediction accuracy的ceiling。\n即便给予等量计算，BCE (23.50) 仍比KL (9.53) 差14 PPL points。 这确认KL的优势不是compute artifact——BCE的factorized gradient （∂L/∂s_j仅依赖neuron j）无论训练多久都无法捕获joint neuron interactions。 Information bottleneck在loss function structure中，不在训练预算中。\n"
204	  },
205	  {
206	    "name": "SPON reimplementation on Llama 3.1 8B",
207	    "description": "实现SPON（learnable per-layer bias vectors + KL training）。 先在5个QA benchmarks上验证可复现SPON发表结果，再用于composition实验。\n",
208	    "results": {
209	      "spon_wikitext2_ppl": 11.2,
210	      "spon_ppl_increase_vs_dense_pct": 83.0,
211	      "spon_arc_c": 49.5,
212	      "spon_arc_e": 75.8,
213	      "spon_boolq": 78.2,
214	      "spon_piqa": 77.5,
215	      "spon_winogrande": 69.8,
216	      "reproduction_arc_c_delta_vs_published": 1.2,
217	      "reproduction_boolq_delta_vs_published": 0.8,
218	      "spon_training_hours": 0.3,
219	      "spon_param_count_mb": 0.5,
220	      "spon_inference_overhead_ms": 0.0
221	    },
222	    "tables": [
223	      {
224	        "name": "Table 4: SPON reproduction — QA benchmark comparison",
225	        "columns": [
226	          "Benchmark",
227	          "Dense",
228	          "SPON (ours)",
229	          "Δ vs published SPON"
230	        ],
231	        "rows": [
232	          [
233	            "ARC-c",
234	            "53.4%",
235	            "49.5%",
236	            "+1.2%"
237	          ],
238	          [
239	            "ARC-e",
240	            "81.2%",
241	            "75.8%",
242	            "-0.5%"
243	          ],
244	          [
245	            "BoolQ",
246	            "83.5%",
247	            "78.2%",
248	            "+0.8%"
249	          ],
250	          [
251	            "PIQA",
252	            "81.0%",
253	            "77.5%",
254	            "-1.0%"
255	          ],
256	          [
257	            "WinoGrande",
258	            "74.2%",
259	            "69.8%",
260	            "+0.6%"
261	          ]
262	        ]
263	      }
264	    ],
265	    "figures": [],
266	    "analysis": "SPON成功复现，PPL 11.20接近BCE+comp (11.56) 但zero overhead。 这为composition实验(plan_005)建立baseline。 有趣的observation：SPON (static KL-trained) ≈ BCE+comp (contextual BCE-trained)， 说明KL loss signal的quality甚至在static correction场景下也有value， 与BCE需要contextual compensation才能达到同等水平形成对比。\n\n\nSPON的per-layer bias vector捕获average-case activation drift——当50%的neurons被pruned时， 每层hidden state的均值会systematically shift，bias correction直接补偿这个first-order偏差。 KL loss训练确保bias correction在output distribution level是optimal的（而非仅在hidden space level）。\nPPL 11.20优于TEAL (~12.5)，因为static bias correction addresses the mean drift that magnitude-based pruning cannot handle。但远不如contextual KL (9.53)，因为 input-independent correction无法适应per-token的neuron importance variation—— 不同输入的optimal pruning pattern差异很大，static bias只是average correction。\nQA benchmarks应在published results的±2%内，偏差来源： (1) Llama 3.1 8B vs SPON原文可能用不同base model，(2) sparsity target可能略有差异。 零inference overhead是SPON的关键优势——bias只是per-layer addition，fused into existing computation。\n"
267	  },
268	  {
269	    "name": "SPON + KL predictor composition",
270	    "description": "同时应用SPON bias correction + KL contextual predictor。 Additivity test: 测量output-space interaction residual。Per-layer orthogonality分析。\n",
271	    "results": {
272	      "spon_kl_wikitext2_ppl_mean": 8.91,
273	      "spon_kl_wikitext2_ppl_std": 0.14,
274	      "spon_kl_wikitext2_ppl_seeds": [
275	        8.75,
276	        9.02,
277	        8.95
278	      ],
279	      "spon_only_ppl": 11.2,
280	      "kl_only_ppl": 9.53,
281	      "interaction_residual_norm_ratio": 0.22,
282	      "per_layer_orthogonality_mean_cosine": 0.18,
283	      "hypothetical_fully_additive_ppl": 8.23,
284	      "actual_vs_additive_gap": 0.68,
285	      "interaction_residual_pct": 22.0
286	    },
287	    "tables": [
288	      {
289	        "name": "Table 5: Composition additivity analysis",
290	        "columns": [
291	          "Condition",
292	          "WikiText-2 PPL",
293	          "Δ from TEAL baseline"
294	        ],
295	        "rows": [
296	          [
297	            "TEAL (no learned correction)",
298	            12.5,
299	            "—"
300	          ],
301	          [
302	            "SPON only",
303	            11.2,
304	            "-1.30"
305	          ],
306	          [
307	            "KL-only",
308	            9.53,
309	            "-2.97"
310	          ],
311	          [
312	            "SPON + KL (if fully additive)",
313	            8.23,
314	            "-4.27"
315	          ],
316	          [
317	            "SPON + KL (actual)",
318	            "8.91 ± 0.14",
319	            "-3.59"
320	          ],
321	          [
322	            "Interaction residual",
323	            "—",
324	            "0.68 (22%)"
325	          ]
326	        ]
327	      }
328	    ],
329	    "figures": [],
330	    "analysis": "Composition有效但not clean：22% interaction residual意味着不能声称perfect additivity。 Claim 2需要弱化为\"empirically observed partial additivity\"。 Paper中需要supplementary analysis展示interaction term的per-layer breakdown， honest地characterize哪些层composition是near-additive的，哪些有significant overlap。 但SPON+KL (8.91) 作为best overall result仍然有value—— 证明static和contextual corrections可以有意义地组合，即使不是mathematically clean的。\n\n\nSPON corrects average drift (first-order bias)，KL predictor adapts per-token neuron importance (conditional correction)。两者address partially orthogonal error sources： SPON修正\"平均而言哪些neurons被drop后hidden state往哪个方向drift\"， KL修正\"对这个specific input应该keep哪些neurons\"。\nInteraction residual ~22%表明non-trivial overlap：KL predictor在训练时部分学到了 SPON负责的mean drift correction（因为KL loss本身会push predictor去修正所有可修正的error， 包括systematic bias）。因此组合收益存在但不perfectly additive。\nPPL从KL-only (9.53) 提升到SPON+KL (8.91)，gain = 0.62 PPL。 如果fully additive（TEAL baseline 12.5为reference）： SPON improvement = 12.5 - 11.2 = 1.3, KL improvement = 12.5 - 9.53 = 2.97 Additive prediction: 12.5 - 1.3 - 2.97 = 8.23。Actual 8.91 vs 8.23 → 22% interaction residual。\nOutput-space linearity test: ||Δ_logits(s+c) - Δ_logits(s) - Δ_logits(c)|| / ||Δ_logits(s+c)|| ≈ 0.22。 Per-layer分析：attention-heavy layers (early layers) 的correction更orthogonal (cosine ~0.1)， FFN-heavy layers (middle layers) 的overlap更大 (cosine ~0.25)。\n"
331	  },
332	  {
333	    "name": "Training-free baselines @ 50% sparsity",
334	    "description": "TEAL (magnitude + greedy allocation), WINA (weight-informed scoring), R-Sparse (rank-aware scoring) 在Llama 3.1 8B上的controlled evaluation。\n",
335	    "results": {
336	      "teal_wikitext2_ppl": 12.5,
337	      "teal_ppl_increase_vs_dense_pct": 104.2,
338	      "wina_wikitext2_ppl": 14.2,
339	      "wina_ppl_increase_vs_dense_pct": 132.1,
340	      "rsparse_wikitext2_ppl": 13.5,
341	      "rsparse_ppl_increase_vs_dense_pct": 120.7,
342	      "teal_training_hours": 0,
343	      "wina_training_hours": 0,
344	      "rsparse_training_hours": 0
345	    },
346	    "tables": [
347	      {
348	        "name": "Table 6: Training-free baselines at 50% model-level sparsity",
349	        "columns": [
350	          "Method",
351	          "WikiText-2 PPL",
352	          "Δ vs Dense",
353	          "Training Cost"
354	        ],
355	        "rows": [
356	          [
357	            "Dense",
358	            6.12,
359	            "—",
360	            "—"
361	          ],
362	          [
363	            "TEAL",
364	            12.5,
365	            "+6.38",
366	            "0"
367	          ],
368	          [
369	            "R-Sparse",
370	            13.5,
371	            "+7.38",
372	            "0"
373	          ],
374	          [
375	            "WINA",
376	            14.2,
377	            "+8.08",
378	            "0"
379	          ],
380	          [
381	            "KL-only (reference)",
382	            9.53,
383	            "+3.41",
384	            "3.8 h"
385	          ]
386	        ]
387	      }
388	    ],
389	    "figures": [],
390	    "analysis": "Training-free方法在50% sparsity下留下6-8 PPL gap，验证了paper framing中 \"training-free heuristics leave a 6+ point quality gap\"的claim。 TEAL是最强baseline (12.50)，将作为所有learned methods的primary comparison point。 三层hierarchy清晰：training-free (12.5-14.2) → static-learned/SPON (11.2) → contextual-learned/KL (9.5)。\n\n\nTEAL最强：magnitude pruning + greedy per-layer allocation在SwiGLU上效果好， 因为gate activation magnitude直接反映neuron importance（gate值接近0的neuron贡献小）。 Greedy allocation在layers间智能分配sparsity budget（让important layers保留更多neurons）。\nWINA次之（14.20）：weight-informed scoring考虑weight magnitude × activation， 但在50% high sparsity下，weight和activation的interaction是non-monotonic的 （large weight × small activation vs small weight × large activation的trade-off不清晰）， 导致pruning决策noisier。\nR-Sparse居中（13.50）：rank-aware approach比pure magnitude好 （考虑了neurons之间的redundancy），但不如TEAL的greedy allocation adaptive。\n三个training-free方法都比learned approaches差3-5 PPL以上， 确立了\"training-free < learned\"的hierarchy，justifying学习predictor的必要性。\n"
391	  },
392	  {
393	    "name": "Full benchmark evaluation + wall-clock profiling",
394	    "description": "所有conditions在WikiText-2, C4, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval上的完整评估。 Wall-clock latency profiling + memory overhead。Pareto frontier。\n",
395	    "results": {
396	      "dense_wikitext2_ppl": 6.12,
397	      "dense_c4_ppl": 8.88,
398	      "dense_arc_c": 53.4,
399	      "dense_winogrande": 74.2,
400	      "dense_mmlu": 65.3,
401	      "dense_gsm8k": 48.2,
402	      "dense_humaneval": 33.5,
403	      "kl_only_wikitext2_ppl": 9.53,
404	      "kl_only_c4_ppl": 12.8,
405	      "kl_only_arc_c": 51.5,
406	      "kl_only_winogrande": 72.0,
407	      "kl_only_mmlu": 63.0,
408	      "kl_only_gsm8k": 46.2,
409	      "kl_only_humaneval": 31.5,
410	      "kl_only_avg_acc_drop_vs_dense_pct": 3.4,
411	      "bce_comp_wikitext2_ppl": 11.56,
412	      "bce_comp_c4_ppl": 15.2,
413	      "bce_comp_arc_c": 50.2,
414	      "bce_comp_winogrande": 70.5,
415	      "bce_comp_mmlu": 61.8,
416	      "bce_comp_gsm8k": 44.8,
417	      "bce_comp_humaneval": 30.5,
418	      "bce_comp_avg_acc_drop_vs_dense_pct": 5.2,
419	      "spon_kl_wikitext2_ppl": 8.91,
420	      "spon_kl_c4_ppl": 11.9,
421	      "spon_kl_arc_c": 52.1,
422	      "spon_kl_winogrande": 72.8,
423	      "spon_kl_mmlu": 63.8,
424	      "spon_kl_gsm8k": 47.0,
425	      "spon_kl_humaneval": 32.0,
426	      "spon_kl_avg_acc_drop_vs_dense_pct": 2.3,
427	      "teal_wikitext2_ppl": 12.5,
428	      "teal_arc_c": 47.8,
429	      "teal_mmlu": 58.5,
430	      "teal_avg_acc_drop_vs_dense_pct": 9.8,
431	      "dense_latency_ms_b1": 18.0,
432	      "kl_only_latency_ms_b1": 16.5,
433	      "bce_comp_latency_ms_b1": 17.8,
434	      "spon_kl_latency_ms_b1": 16.5,
435	      "kl_only_speedup_b1": 1.09,
436	      "bce_comp_speedup_b1": 1.01,
437	      "dense_latency_ms_b32": 3.2,
438	      "kl_only_latency_ms_b32": 2.15,
439	      "bce_comp_latency_ms_b32": 2.72,
440	      "spon_kl_latency_ms_b32": 2.15,
441	      "kl_only_speedup_b32": 1.49,
442	      "bce_comp_speedup_b32": 1.18,
443	      "kl_only_extra_params_mb": 8,
444	      "bce_comp_extra_params_mb": 264,
445	      "spon_kl_extra_params_mb": 8.5
446	    },
447	    "tables": [
448	      {
449	        "name": "Table 7: Full benchmark comparison (Llama 3.1 8B, 50% sparsity)",
450	        "columns": [
451	          "Method",
452	          "Wiki PPL↓",
453	          "C4 PPL↓",
454	          "ARC-c↑",
455	          "WG↑",
456	          "MMLU↑",
457	          "GSM8K↑",
458	          "HE↑",
459	          "Avg Acc Drop"
460	        ],
461	        "rows": [
462	          [
463	            "Dense",
464	            6.12,
465	            8.88,
466	            53.4,
467	            74.2,
468	            65.3,
469	            48.2,
470	            33.5,
471	            "—"
472	          ],
473	          [
474	            "TEAL",
475	            12.5,
476	            17.1,
477	            47.8,
478	            67.2,
479	            58.5,
480	            40.5,
481	            27.0,
482	            "9.8%"
483	          ],
484	          [
485	            "SPON",
486	            11.2,
487	            15.5,
488	            49.5,
489	            69.8,
490	            60.5,
491	            43.0,
492	            28.5,
493	            "7.0%"
494	          ],
495	          [
496	            "BCE+comp",
497	            11.56,
498	            15.2,
499	            50.2,
500	            70.5,
501	            61.8,
502	            44.8,
503	            30.5,
504	            "5.2%"
505	          ],
506	          [
507	            "KL-only",
508	            9.53,
509	            12.8,
510	            51.5,
511	            72.0,
512	            63.0,
513	            46.2,
514	            31.5,
515	            "3.4%"
516	          ],
517	          [
518	            "SPON+KL",
519	            8.91,
520	            11.9,
521	            52.1,
522	            72.8,
523	            63.8,
524	            47.0,
525	            32.0,
526	            "2.3%"
527	          ]
528	        ]
529	      },
530	      {
531	        "name": "Table 8: Inference efficiency (A100 GPU)",
532	        "columns": [
533	          "Method",
534	          "Latency b=1 (ms)",
535	          "Speedup b=1",
536	          "Latency b=32 (ms)",
537	          "Speedup b=32",
538	          "Extra Params"
539	        ],
540	        "rows": [
541	          [
542	            "Dense",
543	            18.0,
544	            "1.00×",
545	            3.2,
546	            "1.00×",
547	            "—"
548	          ],
549	          [
550	            "KL-only",
551	            16.5,
552	            "1.09×",
553	            2.15,
554	            "1.49×",
555	            "8 MB"
556	          ],
557	          [
558	            "SPON+KL",
559	            16.5,
560	            "1.09×",
561	            2.15,
562	            "1.49×",
563	            "8.5 MB"
564	          ],
565	          [
566	            "BCE+comp",
567	            17.8,
568	            "1.01×",
569	            2.72,
570	            "1.18×",
571	            "264 MB"
572	          ]
573	        ]
574	      }
575	    ],
576	    "figures": [],
577	    "analysis": "Main paper table确认KL-only在quality和efficiency两个维度上都dominate BCE+comp。 Quality: 9.53 vs 11.56 PPL, 3.4% vs 5.2% downstream drop。 Efficiency: 1.49x vs 1.18x at b=32, 8MB vs 264MB extra params。 SPON+KL是quality-optimal (8.91, 2.3% drop) 且efficiency与KL-only相同。 This is the paper's main result table, supporting the \"simpler pipeline, better quality\" narrative。\n\n\nDownstream accuracy: KL-only的2-5% relative drop反映PPL degradation在discriminative tasks上的衰减： PPL从6.12升至9.53 (+56%)，但downstream accuracy仅降3.4%，因为discriminative tasks 主要依赖representation quality而非exact next-token prediction，而50% sparsity下 KL predictor保留了most important neurons，representation受损有限。\nBCE+comp的downstream drop更大(5.2%)因为compensation网络修正的是hidden state drift而非 representation quality——补偿了数值偏差但未恢复pruning导致的information loss。\nSPON+KL最佳(2.3% drop)因为static bias correction + contextual prediction覆盖了 both systematic和input-specific errors，leaving minimal residual representation damage。\nLatency: batch=1时memory-bandwidth bound，sparsity的compute reduction被parameter loading开销稀释， KL仅1.09x speedup。Batch=32时compute-bound，50% FFN sparsity的savings充分显现： KL 1.49x vs BCE+comp 1.18x——compensation网络的256MB参数和per-layer GEMV 吃掉了batch场景下1/3的sparsity savings。这是KL的practical efficiency论点的核心。\n"
578	  },
579	  {
580	    "name": "7-level sparsity sweep: KL vs BCE scaling",
581	    "description": "30/35/40/45/50/55/60% sparsity下KL-only vs BCE-only。 Test: KL-BCE PPL delta ~ s²。1 seed per level。50%复用plan_001数据。\n",
582	    "results": {
583	      "sparsity_levels": [
584	        0.3,
585	        0.35,
586	        0.4,
587	        0.45,
588	        0.5,
589	        0.55,
590	        0.6
591	      ],
592	      "kl_only_ppls": [
593	        6.82,
594	        7.28,
595	        7.95,
596	        8.58,
597	        9.53,
598	        11.2,
599	        14.05
600	      ],
601	      "bce_only_ppls": [
602	        11.32,
603	        14.48,
604	        18.95,
605	        23.38,
606	        28.16,
607	        36.7,
608	        49.05
609	      ],
610	      "kl_bce_deltas": [
611	        4.5,
612	        7.2,
613	        11.0,
614	        14.8,
615	        18.63,
616	        25.5,
617	        35.0
618	      ],
619	      "quadratic_fit_a": 97.2,
620	      "quadratic_fit_r2": 0.88,
621	      "residual_at_030": -2.17,
622	      "residual_at_060": 8.17
623	    },
624	    "tables": [
625	      {
626	        "name": "Table 9: Sparsity sweep — KL vs BCE PPL",
627	        "columns": [
628	          "Sparsity",
629	          "KL PPL",
630	          "BCE PPL",
631	          "Δ(BCE-KL)",
632	          "Quadratic prediction",
633	          "Residual"
634	        ],
635	        "rows": [
636	          [
637	            "30%",
638	            6.82,
639	            11.32,
640	            4.5,
641	            6.67,
642	            -2.17
643	          ],
644	          [
645	            "35%",
646	            7.28,
647	            14.48,
648	            7.2,
649	            9.07,
650	            -1.87
651	          ],
652	          [
653	            "40%",
654	            7.95,
655	            18.95,
656	            11.0,
657	            11.9,
658	            -0.9
659	          ],
660	          [
661	            "45%",
662	            8.58,
663	            23.38,
664	            14.8,
665	            15.08,
666	            -0.28
667	          ],
668	          [
669	            "50%",
670	            9.53,
671	            28.16,
672	            18.63,
673	            18.71,
674	            -0.08
675	          ],
676	          [
677	            "55%",
678	            11.2,
679	            36.7,
680	            25.5,
681	            22.79,
682	            2.71
683	          ],
684	          [
685	            "60%",
686	            14.05,
687	            49.05,
688	            35.0,
689	            27.31,
690	            7.69
691	          ]
692	        ]
693	      }
694	    ],
695	    "figures": [],
696	    "analysis": "Claim 3降级为\"consistent empirical trend\"而非\"precise quadratic law\"。 R²=0.88表明quadratic model解释了88%的variance，但systematic residual pattern (low-s sub-quadratic, high-s super-quadratic) 表明真实关系比s²更complex。 在paper中放appendix展示完整fit，main text仅claim \"KL advantage grows super-linearly with sparsity, consistent with the theoretical prediction that joint interaction effects scale with the number of pruned neurons\"。\n\n\nKL-BCE delta随sparsity单调递增：低sparsity时BCE的per-neuron独立假设damage较小 （pruning少量neurons时joint interaction effect有限），高sparsity时damage急剧增大 （每个pruning决策影响更多remaining neurons的joint output）。\nQuadratic fit R²=0.88：存在clear上升趋势，但不是clean quadratic。 Deviation pattern: 低sparsity处delta低于quadratic prediction（此时neuron interactions是sparse的， BCE的independence assumption伤害有限）；高sparsity处delta高于quadratic prediction （此时interaction density超过O(s²)的简化模型，higher-order terms变得significant）。\n这支持\"KL gradient captures joint interactions that scale with sparsity\"的intuition， 但fit noise和systematic residual pattern意味着precise s² law不成立。 R² 0.88在0.80-0.95范围内，支持\"consistent empirical trend\"但不支持\"precise quantitative law\"。\n"
697	  },
698	  {
699	    "name": "Mistral-7B-v0.3 generalization validation",
700	    "description": "KL-only vs BCE+comp @ 50% sparsity on Mistral-7B-v0.3。 Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。\n",
701	    "results": {
702	      "mistral_dense_wikitext2_ppl": 5.52,
703	      "mistral_kl_wikitext2_ppl_mean": 9.38,
704	      "mistral_kl_wikitext2_ppl_std": 0.35,
705	      "mistral_kl_wikitext2_ppl_seeds": [
706	        9.15,
707	        9.35,
708	        9.65
709	      ],
710	      "mistral_kl_ppl_increase_vs_dense_pct": 69.9,
711	      "mistral_kl_arc_c": 52.8,
712	      "mistral_kl_mmlu": 61.5,
713	      "mistral_bce_comp_wikitext2_ppl_mean": 10.45,
714	      "mistral_bce_comp_wikitext2_ppl_std": 0.48,
715	      "mistral_bce_comp_wikitext2_ppl_seeds": [
716	        10.1,
717	        10.3,
718	        10.95
719	      ],
720	      "mistral_bce_comp_ppl_increase_vs_dense_pct": 89.3,
721	      "mistral_bce_comp_arc_c": 51.5,
722	      "mistral_bce_comp_mmlu": 60.2,
723	      "mistral_kl_vs_bce_comp_gap": 1.07,
724	      "llama_kl_vs_bce_comp_gap": 2.03
725	    },
726	    "tables": [
727	      {
728	        "name": "Table 10: Cross-model validation (50% sparsity)",
729	        "columns": [
730	          "Model",
731	          "Condition",
732	          "Wiki PPL↓",
733	          "ARC-c↑",
734	          "MMLU↑",
735	          "KL-BCE gap"
736	        ],
737	        "rows": [
738	          [
739	            "Llama 3.1 8B",
740	            "Dense",
741	            6.12,
742	            53.4,
743	            65.3,
744	            "—"
745	          ],
746	          [
747	            "Llama 3.1 8B",
748	            "KL-only",
749	            9.53,
750	            51.5,
751	            63.0,
752	            "2.03"
753	          ],
754	          [
755	            "Llama 3.1 8B",
756	            "BCE+comp",
757	            11.56,
758	            50.2,
759	            61.8,
760	            "—"
761	          ],
762	          [
763	            "Mistral 7B v0.3",
764	            "Dense",
765	            5.52,
766	            55.0,
767	            63.5,
768	            "—"
769	          ],
770	          [
771	            "Mistral 7B v0.3",
772	            "KL-only",
773	            9.38,
774	            52.8,
775	            61.5,
776	            "1.07"
777	          ],
778	          [
779	            "Mistral 7B v0.3",
780	            "BCE+comp",
781	            10.45,
782	            51.5,
783	            60.2,
784	            "—"
785	          ]
786	        ]
787	      }
788	    ],
789	    "figures": [],
790	    "analysis": "回答reviewer concern #4 \"single model / limited generalization\"。 Mistral验证KL advantage的方向一致性，但smaller gap是honest finding—— 不同架构下advantage magnitude varies。Paper中报告为\"consistent across architectures\" 而非\"universal with fixed effect size\"。Mistral的GQA/sliding window解释 为gap缩小提供architectural intuition。\n\n\nMistral同方向但relative gap更小 (1.07 vs Llama's 2.03 PPL)。原因： (1) Mistral的GQA (grouped-query attention) 产生更structured的activation pattern， SwiGLU层的neuron importance分布more concentrated (fewer \"ambiguous\" neurons near threshold)， 使得BCE的per-neuron独立预测在Mistral上less harmful。 (2) Mistral的sliding window attention导致信息更local，每个token的neuron importance 变化更平滑，减少了KL的contextual adaptation advantage。\nKL PPL increase 70% vs dense (5.52→9.38) 在median tier的50-90%范围内。 BCE+comp PPL increase 89% (5.52→10.45) 表明compensation在Mistral上也有效。\nGap缩小但方向一致：KL-only仍优于BCE+comp on all metrics， 证明KL advantage不是Llama-specific artifact，generalize across architectures。\n"
791	  },
792	  {
793	    "name": "LongBench English subset evaluation (4K-32K tokens)",
794	    "description": "所有conditions在LongBench English subset上的评估： single-doc QA, multi-doc QA, summarization, few-shot, code。 测试predictor在超出训练序列长度时的generalization。\n",
795	    "results": {
796	      "dense_single_doc_qa": 42.5,
797	      "dense_multi_doc_qa": 36.0,
798	      "dense_summarization": 27.2,
799	      "dense_few_shot": 60.0,
800	      "dense_code": 34.0,
801	      "dense_avg": 39.9,
802	      "kl_single_doc_qa": 38.8,
803	      "kl_multi_doc_qa": 32.2,
804	      "kl_summarization": 25.5,
805	      "kl_few_shot": 55.8,
806	      "kl_code": 30.2,
807	      "kl_avg": 36.5,
808	      "kl_avg_drop_pct": 8.5,
809	      "bce_comp_single_doc_qa": 36.5,
810	      "bce_comp_multi_doc_qa": 30.0,
811	      "bce_comp_summarization": 24.2,
812	      "bce_comp_few_shot": 53.5,
813	      "bce_comp_code": 28.5,
814	      "bce_comp_avg": 34.5,
815	      "bce_comp_avg_drop_pct": 13.5,
816	      "spon_kl_single_doc_qa": 39.5,
817	      "spon_kl_multi_doc_qa": 33.0,
818	      "spon_kl_summarization": 25.8,
819	      "spon_kl_few_shot": 56.5,
820	      "spon_kl_code": 31.0,
821	      "spon_kl_avg": 37.2,
822	      "spon_kl_avg_drop_pct": 6.8,
823	      "teal_avg": 31.5,
824	      "teal_avg_drop_pct": 21.1
825	    },
826	    "tables": [
827	      {
828	        "name": "Table 11: LongBench performance (English subset)",
829	        "columns": [
830	          "Method",
831	          "Single-doc QA",
832	          "Multi-doc QA",
833	          "Summ.",
834	          "Few-shot",
835	          "Code",
836	          "Avg",
837	          "Avg Drop"
838	        ],
839	        "rows": [
840	          [
841	            "Dense",
842	            42.5,
843	            36.0,
844	            27.2,
845	            60.0,
846	            34.0,
847	            39.9,
848	            "—"
849	          ],
850	          [
851	            "TEAL",
852	            34.0,
853	            27.5,
854	            23.0,
855	            48.5,
856	            24.5,
857	            31.5,
858	            "21.1%"
859	          ],
860	          [
861	            "BCE+comp",
862	            36.5,
863	            30.0,
864	            24.2,
865	            53.5,
866	            28.5,
867	            34.5,
868	            "13.5%"
869	          ],
870	          [
871	            "KL-only",
872	            38.8,
873	            32.2,
874	            25.5,
875	            55.8,
876	            30.2,
877	            36.5,
878	            "8.5%"
879	          ],
880	          [
881	            "SPON+KL",
882	            39.5,
883	            33.0,
884	            25.8,
885	            56.5,
886	            31.0,
887	            37.2,
888	            "6.8%"
889	          ]
890	        ]
891	      }
892	    ],
893	    "figures": [],
894	    "analysis": "Long-context generalization是KL approach的非trivial validation： predictor trained on short sequences仍在long context下保持8.5% average drop。 KL vs BCE+comp gap在long context下expand (8.5% vs 13.5%)，suggesting KL's distributional supervision provides better OOD robustness。 SPON+KL进一步improve (6.8%)，supporting the composition claim's practical value。\n\n\nLong-context evaluation drop (KL avg 8.5%) 大于short-context downstream (3.4%)， 因为predictor在2048-token序列上训练，推广到4K-32K时neuron importance distribution shifts： 长文本中attention pattern更diffuse，neuron activation的long-range dependency增加， predictor需要在unseen的activation regime下做决策。\nKL仍优于BCE+comp (8.5% vs 13.5% drop)：KL的output-distribution supervision在 distributional shift下更robust，因为即使在OOD inputs上，KL梯度仍push predictor 去最小化logit divergence，而BCE的target masks在OOD时可能fundamentally错误 （训练时的\"correct\" mask对长文本不适用）。\nPer-task pattern: multi-doc QA和code drop最大（需要跨document/long-range reasoning， 对neuron selection错误最敏感）；summarization drop最小（更tolerant of approximate representation， 核心信息在early tokens中已被captured）。\nSPON+KL最佳 (6.8% drop)：SPON的static bias correction在长文本中仍然valid （average drift不依赖sequence length），提供stable baseline correction。\n"
895	  },
896	  {
897	    "name": "MT-Bench evaluation with GPT-4o judge",
898	    "description": "80 multi-turn questions, 8 categories。All conditions。 Tests instruction-following quality under sparsity。\n",
899	    "results": {
900	      "dense_mt_bench_avg": 7.25,
901	      "kl_only_mt_bench_avg": 6.72,
902	      "bce_comp_mt_bench_avg": 6.38,
903	      "spon_kl_mt_bench_avg": 6.85,
904	      "teal_mt_bench_avg": 5.8,
905	      "kl_mt_writing": 7.1,
906	      "kl_mt_roleplay": 6.9,
907	      "kl_mt_reasoning": 6.2,
908	      "kl_mt_math": 5.8,
909	      "kl_mt_coding": 6.5,
910	      "kl_mt_extraction": 7.3,
911	      "kl_mt_stem": 6.8,
912	      "kl_mt_humanities": 7.2
913	    },
914	    "tables": [
915	      {
916	        "name": "Table 12: MT-Bench scores by category (GPT-4o judge)",
917	        "columns": [
918	          "Category",
919	          "Dense",
920	          "KL-only",
921	          "BCE+comp",
922	          "SPON+KL"
923	        ],
924	        "rows": [
925	          [
926	            "Writing",
927	            7.5,
928	            7.1,
929	            6.8,
930	            7.2
931	          ],
932	          [
933	            "Roleplay",
934	            7.3,
935	            6.9,
936	            6.5,
937	            7.0
938	          ],
939	          [
940	            "Reasoning",
941	            6.8,
942	            6.2,
943	            5.8,
944	            6.4
945	          ],
946	          [
947	            "Math",
948	            6.5,
949	            5.8,
950	            5.3,
951	            6.0
952	          ],
953	          [
954	            "Coding",
955	            7.0,
956	            6.5,
957	            6.1,
958	            6.7
959	          ],
960	          [
961	            "Extraction",
962	            7.8,
963	            7.3,
964	            7.0,
965	            7.5
966	          ],
967	          [
968	            "STEM",
969	            7.2,
970	            6.8,
971	            6.4,
972	            6.9
973	          ],
974	          [
975	            "Humanities",
976	            7.9,
977	            7.2,
978	            7.2,
979	            7.3
980	          ],
981	          [
982	            "Average",
983	            7.25,
984	            6.72,
985	            6.38,
986	            6.85
987	          ]
988	        ]
989	      }
990	    ],
991	    "figures": [],
992	    "analysis": "MT-Bench验证KL approach在instruction-following场景下的质量保持。 Average drop 0.53 for KL vs 0.87 for BCE+comp, consistent with PPL results。 Category-level breakdown provides actionable insight: math/reasoning是sparsity的weak spot， 可作为future work的optimization target。EMNLP reviewers重视NLP-specific evaluation， MT-Bench作为multi-turn generation quality metric补充了discriminative benchmarks。\n\n\nMT-Bench average drop: KL -0.53, BCE+comp -0.87。Multi-turn instruction following 对model quality less sensitive than PPL would suggest：MT-Bench更多测试format compliance 和high-level reasoning，而非exact token probability。但math和reasoning categories 受sparsity影响最大（6.2, 5.8 for KL），因为这些需要precise computation chains where even small representation errors accumulate across reasoning steps。\nWriting和extraction受影响最小（7.1, 7.3），因为这些依赖pattern matching和formatting rather than deep logical reasoning。\nKL显著优于BCE+comp in multi-turn setting：multi-turn对话中error accumulation更严重， KL的lower per-step error导致multi-turn quality degradation更小。\n"
993	  },
994	  {
995	    "name": "RULER synthetic long-context evaluation",
996	    "description": "RULER @ 4K和16K context，3 representative task types。 Fine-grained capability diagnostics complementing LongBench。\n",
997	    "results": {
998	      "dense_ruler_4k_avg": 92.0,
999	      "kl_only_ruler_4k_avg": 85.5,
1000	      "bce_comp_ruler_4k_avg": 81.0,
1001	      "spon_kl_ruler_4k_avg": 87.0,
1002	      "dense_ruler_16k_avg": 85.0,
1003	      "kl_only_ruler_16k_avg": 73.5,
1004	      "bce_comp_ruler_16k_avg": 67.0,
1005	      "spon_kl_ruler_16k_avg": 75.5,
1006	      "kl_ruler_16k_needle_retrieval": 78.0,
1007	      "kl_ruler_16k_multi_key": 70.5,
1008	      "kl_ruler_16k_aggregation": 72.0
1009	    },
1010	    "tables": [
1011	      {
1012	        "name": "Table 13: RULER evaluation at 4K and 16K context",
1013	        "columns": [
1014	          "Method",
1015	          "4K Avg",
1016	          "16K Avg",
1017	          "4K→16K Δ"
1018	        ],
1019	        "rows": [
1020	          [
1021	            "Dense",
1022	            92.0,
1023	            85.0,
1024	            "-7.0"
1025	          ],
1026	          [
1027	            "KL-only",
1028	            85.5,
1029	            73.5,
1030	            "-12.0"
1031	          ],
1032	          [
1033	            "SPON+KL",
1034	            87.0,
1035	            75.5,
1036	            "-11.5"
1037	          ],
1038	          [
1039	            "BCE+comp",
1040	            81.0,
1041	            67.0,
1042	            "-14.0"
1043	          ]
1044	        ]
1045	      }
1046	    ],
1047	    "figures": [],
1048	    "analysis": "RULER确认LongBench的findings: KL在long context下更robust than BCE+comp， 且degradation rate (slope) 更小。作为appendix-level diagnostic complement LongBench的 naturalistic evaluation。4K→16K的degradation pattern suggest training on longer sequences could improve predictor robustness（future work direction）。\n\nRULER的synthetic tasks提供controlled diagnostics： 4K时KL drop 7% (85.5 vs 92.0)，与LongBench consistent但more controlled。 16K时KL drop增大到13.5% (73.5 vs 85.0)，表明predictor的generalization 随context length增加而degrade——在超出训练distribution的长context中， predictor对late-position tokens的neuron importance估计less accurate （attention pattern在long context中more diffuse，activation statistics shift）。\nNeedle retrieval (78.0 at 16K) 相对较好因为retrieval主要依赖attention mechanism 而非FFN computation。Multi-key (70.5) 和aggregation (72.0) 更差因为 需要跨position的information integration，FFN computation的precision更重要。\nBCE+comp在16K时drop更严重 (67.0, 21.2% drop)：compensation网络在OOD context下 不仅没帮助，反而可能introduce noise（compensation trained on short context的correction pattern在long context下不适用）。\n"
1049	  }
1050	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7da3a816-073f-4a79-a281-5c08b21b5f8f",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "ab1f0b6a-baf9-4110-a628-7375b55aa5d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Four-condition ablation @ 50% sparsity\",\n    \"description\": \"补充KL-only 2 seeds (s0, s1) 达到5-seed headline；新增BCE+comp 5 seeds； 新增KL+comp 3 seeds。与已有BCE-only 3 seeds和KL-only 3 seeds组合。\\n\",\n    \"results\": {\n      \"kl_only_wikitext2_ppl_mean\": 9.53,\n      \"kl_only_wikitext2_ppl_std\": 0.41,\n      \"kl_only_wikitext2_ppl_seeds\": [\n        9.21,\n        9.25,\n        9.14,\n        9.85,\n        10.18\n      ],\n      \"kl_only_model_sparsity\": 0.498,\n      \"bce_only_wikitext2_ppl_mean\": 28.16,\n      \"bce_only_wikitext2_ppl_std\": 0.21,\n      \"bce_comp_wikitext2_ppl_mean\": 11.56,\n      \"bce_comp_wikitext2_ppl_std\": 0.61,\n      \"bce_comp_wikitext2_ppl_seeds\": [\n        11.2,\n        11.8,\n        12.5,\n        10.8,\n        11.5\n      ],\n      \"bce_comp_param_overhead_mb\": 256,\n      \"kl_comp_wikitext2_ppl_mean\": 9.05,\n      \"kl_comp_wikitext2_ppl_std\": 0.15,\n      \"kl_comp_wikitext2_ppl_seeds\": [\n        9.05,\n        9.2,\n        8.9\n      ],\n      \"kl_only_vs_bce_comp_gap\": 2.03,\n      \"kl_comp_vs_kl_only_improvement\": 0.48,\n      \"dense_wikitext2_ppl\": 6.12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Four-condition ablation at 50% model-level sparsity (Llama 3.1 8B)\",\n        \"columns\": [\n          \"Condition\",\n          \"WikiText-2 PPL (↓)\",\n          \"Seeds\",\n          \"Compensation Params\",\n          \"Pipeline Complexity\"\n        ],\n        \"rows\": [\n          [\n            \"Dense (reference)\",\n            \"6.12\",\n            \"—\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"BCE-only\",\n            \"28.16 ± 0.21\",\n            3,\n            0,\n            \"Simple\"\n          ],\n          [\n            \"BCE + compensation\",\n            \"11.56 ± 0.61\",\n            5,\n            \"256 MB\",\n            \"Complex\"\n          ],\n          [\n            \"KL-only\",\n            \"9.53 ± 0.41\",\n            5,\n            0,\n            \"Simple\"\n          ],\n          [\n            \"KL + compensation\",\n            \"9.05 ± 0.15\",\n            3,\n            \"256 MB\",\n            \"Complex\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Headline result支持revised Claim 1：KL-only在质量上优于BCE+comp (9.53 vs 11.56)， 同时完全省去compensation网络。KL+comp的微弱提升(0.48 PPL)表明compensation对KL是冗余的， 而对BCE是必需的(28.16→11.56)。这将论文核心message从\\\"KL is categorically better\\\" 调整为\\\"KL eliminates compensation overhead while achieving better quality\\\"—— 更nuanced但仍有明确的practical implication。 Seed方差增大(std 0.41)需要在paper中transparent报告，但5-seed mean的confidence interval 仍完全在BCE+comp之下。\\n\\n\\nKL-only: 新增s0/s1引入方差增大（s1=10.18为较弱种子），5-seed std从0.05升至0.41。 这反映Gumbel-sigmoid采样在不同初始化下的探索路径差异——部分种子的predictor在特定层学到次优mask分布， 导致几个层的neuron selection偏差累积。均值9.53仍在9.0-10.5范围内。\\nBCE+comp: compensation网络（per-layer MLP, ~256MB）有效修正BCE predictor的mask错误： BCE-only的per-neuron独立预测在高sparsity下产生大量joint interaction error， compensation网络通过residual connection学习修正sparse hidden state的drift。 PPL从28.16降至11.56，compensation确实有用（回收~16.6 PPL）。 但BCE的factorized gradient本身限制了mask质量ceiling，compensation只能修正而非预防错误。\\nKL+comp: compensation对KL的提升微弱（9.53→9.05, 仅0.48 PPL）。 因为KL loss通过d_logits/dh * dh/dm的gradient coupling已经在训练时优化了joint neuron selection， 留给compensation修正的residual error很小。这证明KL在训练阶段\\\"preempt\\\"了compensation需要解决的问题。\\n核心结论：KL-only (9.53) < BCE+comp (11.56)，且KL不需要256MB compensation overhead。 KL+comp的diminishing return进一步确认compensation对KL是冗余的。\\n\"\n  },\n  {\n    \"name\": \"STE baseline: KL loss + Straight-Through Estimator\",\n    \"description\": \"用STE替换Gumbel-sigmoid作为gradient estimator，保持KL loss不变。 3 seeds。隔离KL优势中loss function vs relaxation method的各自贡献。\\n\",\n    \"results\": {\n      \"kl_ste_wikitext2_ppl_mean\": 14.7,\n      \"kl_ste_wikitext2_ppl_std\": 0.6,\n      \"kl_ste_wikitext2_ppl_seeds\": [\n        14.7,\n        15.3,\n        14.1\n      ],\n      \"kl_ste_model_sparsity\": 0.498,\n      \"total_gain_over_bce\": 18.63,\n      \"gain_from_kl_loss\": 13.46,\n      \"gain_from_gumbel\": 5.17,\n      \"gumbel_contribution_pct\": 27.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Loss function vs relaxation method ablation\",\n        \"columns\": [\n          \"Condition\",\n          \"Loss\",\n          \"Relaxation\",\n          \"WikiText-2 PPL\",\n          \"Gain over BCE-only\"\n        ],\n        \"rows\": [\n          [\n            \"BCE-only\",\n            \"BCE\",\n            \"STE\",\n            \"28.16\",\n            \"—\"\n          ],\n          [\n            \"KL + STE\",\n            \"KL\",\n            \"STE\",\n            \"14.70 ± 0.60\",\n            \"13.46 (72%)\"\n          ],\n          [\n            \"KL + Gumbel\",\n            \"KL\",\n            \"Gumbel-σ\",\n            \"9.53 ± 0.41\",\n            \"18.63 (100%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"KL loss贡献72%的improvement，Gumbel贡献28%。两者都是necessary component。 这回答reviewer concern #3: gains不是purely from Gumbel relaxation，KL loss本身是主要driver。 同时也表明gradient estimator的选择有meaningful impact，为future work （更好的relaxation methods）留下空间。\\n\\n\\nSTE将hard threshold的gradient设为1（identity），丢失了neuron importance的magnitude信息。 Gumbel-sigmoid在forward pass中通过temperature-controlled soft sampling保留了importance ranking的连续性， 使KL gradient能够区分\\\"barely active\\\"和\\\"strongly active\\\"的neurons。\\nKL+STE (14.70) 仍大幅优于BCE-only (28.16)，因为KL loss的joint coupling效应不依赖relaxation方法—— 即使用STE的biased gradient，KL的∂logits/∂mask仍传递了output-distribution level的supervision。 但STE的gradient bias导致predictor在边界neurons（importance接近threshold的neurons）上做出次优决策， 累积~5 PPL的损失。\\nGumbel贡献~28%的gain，说明\\\"loss和relaxation都重要\\\"——KL loss是主要贡献者（72%）， 但Gumbel的smooth gradient对于fine-grained mask optimization不可或缺。 这防御了reviewer concern \\\"Gumbel relaxation, not KL, explains gains\\\"。\\n\"\n  },\n  {\n    \"name\": \"Iso-compute BCE comparison\",\n    \"description\": \"扩展BCE训练步数以匹配KL的total FLOPs。KL需要per-step dense forward pass获取logits， BCE可用cached targets，因此BCE per-step成本远低于KL。等量计算下BCE可训练更多步。\\n\",\n    \"results\": {\n      \"kl_per_step_tflops\": 66.0,\n      \"bce_per_step_tflops\": 0.8,\n      \"kl_total_training_hours\": 3.8,\n      \"bce_standard_training_hours\": 0.4,\n      \"bce_isocompute_training_steps\": 33000,\n      \"bce_isocompute_training_hours\": 3.8,\n      \"bce_standard_ppl\": 28.16,\n      \"bce_isocompute_ppl_mean\": 23.5,\n      \"bce_isocompute_ppl_std\": 0.7,\n      \"bce_isocompute_ppl_seeds\": [\n        23.5,\n        24.2,\n        22.8\n      ],\n      \"kl_only_ppl_mean\": 9.53,\n      \"gap_kl_vs_bce_isocompute\": 13.97\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Iso-compute training comparison\",\n        \"columns\": [\n          \"Condition\",\n          \"Per-step TFLOPs\",\n          \"Total Steps\",\n          \"GPU-hours\",\n          \"WikiText-2 PPL\"\n        ],\n        \"rows\": [\n          [\n            \"KL + Gumbel\",\n            66.0,\n            1000,\n            3.8,\n            \"9.53 ± 0.41\"\n          ],\n          [\n            \"BCE (standard)\",\n            0.8,\n            1000,\n            0.4,\n            \"28.16 ± 0.21\"\n          ],\n          [\n            \"BCE (iso-compute)\",\n            0.8,\n            33000,\n            3.8,\n            \"23.50 ± 0.70\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"直接回答reviewer concern #2 \\\"KL wins only because more compute\\\"。 等量计算下KL仍领先14 PPL points，BCE的per-neuron independence assumption是根本瓶颈。 附带发现：BCE training cost极低（0.4 vs 3.8 GPU-hours），在不追求最优质量的场景下 BCE+comp仍有实用价值（training便宜，compensation弥补质量），但KL在quality-critical场景下 是strictly better choice。\\n\\n\\nBCE per-step成本远低于KL（0.8 vs 66 TFLOPs），因为BCE只需predictor forward+binary target比对， 无需base model forward pass。等量计算下BCE获得~33x训练步数。\\n额外训练将BCE PPL从28.16降至23.50（降低16.5%）。改善来源： (1) predictor在更多数据上泛化更好，(2) 更充分的convergence。 但改善呈sharp diminishing returns——BCE在~5000步后已接近per-neuron prediction accuracy的ceiling。\\n即便给予等量计算，BCE (23.50) 仍比KL (9.53) 差14 PPL points。 这确认KL的优势不是compute artifact——BCE的factorized gradient （∂L/∂s_j仅依赖neuron j）无论训练多久都无法捕获joint neuron interactions。 Information bottleneck在loss function structure中，不在训练预算中。\\n\"\n  },\n  {\n    \"name\": \"SPON reimplementation on Llama 3.1 8B\",\n    \"description\": \"实现SPON（learnable per-layer bias vectors + KL training）。 先在5个QA benchmarks上验证可复现SPON发表结果，再用于composition实验。\\n\",\n    \"results\": {\n      \"spon_wikitext2_ppl\": 11.2,\n      \"spon_ppl_increase_vs_dense_pct\": 83.0,\n      \"spon_arc_c\": 49.5,\n      \"spon_arc_e\": 75.8,\n      \"spon_boolq\": 78.2,\n      \"spon_piqa\": 77.5,\n      \"spon_winogrande\": 69.8,\n      \"reproduction_arc_c_delta_vs_published\": 1.2,\n      \"reproduction_boolq_delta_vs_published\": 0.8,\n      \"spon_training_hours\": 0.3,\n      \"spon_param_count_mb\": 0.5,\n      \"spon_inference_overhead_ms\": 0.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: SPON reproduction — QA benchmark comparison\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Dense\",\n          \"SPON (ours)\",\n          \"Δ vs published SPON\"\n        ],\n        \"rows\": [\n          [\n            \"ARC-c\",\n            \"53.4%\",\n            \"49.5%\",\n            \"+1.2%\"\n          ],\n          [\n            \"ARC-e\",\n            \"81.2%\",\n            \"75.8%\",\n            \"-0.5%\"\n          ],\n          [\n            \"BoolQ\",\n            \"83.5%\",\n            \"78.2%\",\n            \"+0.8%\"\n          ],\n          [\n            \"PIQA\",\n            \"81.0%\",\n            \"77.5%\",\n            \"-1.0%\"\n          ],\n          [\n            \"WinoGrande\",\n            \"74.2%\",\n            \"69.8%\",\n            \"+0.6%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON成功复现，PPL 11.20接近BCE+comp (11.56) 但zero overhead。 这为composition实验(plan_005)建立baseline。 有趣的observation：SPON (static KL-trained) ≈ BCE+comp (contextual BCE-trained)， 说明KL loss signal的quality甚至在static correction场景下也有value， 与BCE需要contextual compensation才能达到同等水平形成对比。\\n\\n\\nSPON的per-layer bias vector捕获average-case activation drift——当50%的neurons被pruned时， 每层hidden state的均值会systematically shift，bias correction直接补偿这个first-order偏差。 KL loss训练确保bias correction在output distribution level是optimal的（而非仅在hidden space level）。\\nPPL 11.20优于TEAL (~12.5)，因为static bias correction addresses the mean drift that magnitude-based pruning cannot handle。但远不如contextual KL (9.53)，因为 input-independent correction无法适应per-token的neuron importance variation—— 不同输入的optimal pruning pattern差异很大，static bias只是average correction。\\nQA benchmarks应在published results的±2%内，偏差来源： (1) Llama 3.1 8B vs SPON原文可能用不同base model，(2) sparsity target可能略有差异。 零inference overhead是SPON的关键优势——bias只是per-layer addition，fused into existing computation。\\n\"\n  },\n  {\n    \"name\": \"SPON + KL predictor composition\",\n    \"description\": \"同时应用SPON bias correction + KL contextual predictor。 Additivity test: 测量output-space interaction residual。Per-layer orthogonality分析。\\n\",\n    \"results\": {\n      \"spon_kl_wikitext2_ppl_mean\": 8.91,\n      \"spon_kl_wikitext2_ppl_std\": 0.14,\n      \"spon_kl_wikitext2_ppl_seeds\": [\n        8.75,\n        9.02,\n        8.95\n      ],\n      \"spon_only_ppl\": 11.2,\n      \"kl_only_ppl\": 9.53,\n      \"interaction_residual_norm_ratio\": 0.22,\n      \"per_layer_orthogonality_mean_cosine\": 0.18,\n      \"hypothetical_fully_additive_ppl\": 8.23,\n      \"actual_vs_additive_gap\": 0.68,\n      \"interaction_residual_pct\": 22.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Composition additivity analysis\",\n        \"columns\": [\n          \"Condition\",\n          \"WikiText-2 PPL\",\n          \"Δ from TEAL baseline\"\n        ],\n        \"rows\": [\n          [\n            \"TEAL (no learned correction)\",\n            12.5,\n            \"—\"\n          ],\n          [\n            \"SPON only\",\n            11.2,\n            \"-1.30\"\n          ],\n          [\n            \"KL-only\",\n            9.53,\n            \"-2.97\"\n          ],\n          [\n            \"SPON + KL (if fully additive)\",\n            8.23,\n            \"-4.27\"\n          ],\n          [\n            \"SPON + KL (actual)\",\n            \"8.91 ± 0.14\",\n            \"-3.59\"\n          ],\n          [\n            \"Interaction residual\",\n            \"—\",\n            \"0.68 (22%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Composition有效但not clean：22% interaction residual意味着不能声称perfect additivity。 Claim 2需要弱化为\\\"empirically observed partial additivity\\\"。 Paper中需要supplementary analysis展示interaction term的per-layer breakdown， honest地characterize哪些层composition是near-additive的，哪些有significant overlap。 但SPON+KL (8.91) 作为best overall result仍然有value—— 证明static和contextual corrections可以有意义地组合，即使不是mathematically clean的。\\n\\n\\nSPON corrects average drift (first-order bias)，KL predictor adapts per-token neuron importance (conditional correction)。两者address partially orthogonal error sources： SPON修正\\\"平均而言哪些neurons被drop后hidden state往哪个方向drift\\\"， KL修正\\\"对这个specific input应该keep哪些neurons\\\"。\\nInteraction residual ~22%表明non-trivial overlap：KL predictor在训练时部分学到了 SPON负责的mean drift correction（因为KL loss本身会push predictor去修正所有可修正的error， 包括systematic bias）。因此组合收益存在但不perfectly additive。\\nPPL从KL-only (9.53) 提升到SPON+KL (8.91)，gain = 0.62 PPL。 如果fully additive（TEAL baseline 12.5为reference）： SPON improvement = 12.5 - 11.2 = 1.3, KL improvement = 12.5 - 9.53 = 2.97 Additive prediction: 12.5 - 1.3 - 2.97 = 8.23。Actual 8.91 vs 8.23 → 22% interaction residual。\\nOutput-space linearity test: ||Δ_logits(s+c) - Δ_logits(s) - Δ_logits(c)|| / ||Δ_logits(s+c)|| ≈ 0.22。 Per-layer分析：attention-heavy layers (early layers) 的correction更orthogonal (cosine ~0.1)， FFN-heavy layers (middle layers) 的overlap更大 (cosine ~0.25)。\\n\"\n  },\n  {\n    \"name\": \"Training-free baselines @ 50% sparsity\",\n    \"description\": \"TEAL (magnitude + greedy allocation), WINA (weight-informed scoring), R-Sparse (rank-aware scoring) 在Llama 3.1 8B上的controlled evaluation。\\n\",\n    \"results\": {\n      \"teal_wikitext2_ppl\": 12.5,\n      \"teal_ppl_increase_vs_dense_pct\": 104.2,\n      \"wina_wikitext2_ppl\": 14.2,\n      \"wina_ppl_increase_vs_dense_pct\": 132.1,\n      \"rsparse_wikitext2_ppl\": 13.5,\n      \"rsparse_ppl_increase_vs_dense_pct\": 120.7,\n      \"teal_training_hours\": 0,\n      \"wina_training_hours\": 0,\n      \"rsparse_training_hours\": 0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Training-free baselines at 50% model-level sparsity\",\n        \"columns\": [\n          \"Method\",\n          \"WikiText-2 PPL\",\n          \"Δ vs Dense\",\n          \"Training Cost\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            6.12,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"TEAL\",\n            12.5,\n            \"+6.38\",\n            \"0\"\n          ],\n          [\n            \"R-Sparse\",\n            13.5,\n            \"+7.38\",\n            \"0\"\n          ],\n          [\n            \"WINA\",\n            14.2,\n            \"+8.08\",\n            \"0\"\n          ],\n          [\n            \"KL-only (reference)\",\n            9.53,\n            \"+3.41\",\n            \"3.8 h\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Training-free方法在50% sparsity下留下6-8 PPL gap，验证了paper framing中 \\\"training-free heuristics leave a 6+ point quality gap\\\"的claim。 TEAL是最强baseline (12.50)，将作为所有learned methods的primary comparison point。 三层hierarchy清晰：training-free (12.5-14.2) → static-learned/SPON (11.2) → contextual-learned/KL (9.5)。\\n\\n\\nTEAL最强：magnitude pruning + greedy per-layer allocation在SwiGLU上效果好， 因为gate activation magnitude直接反映neuron importance（gate值接近0的neuron贡献小）。 Greedy allocation在layers间智能分配sparsity budget（让important layers保留更多neurons）。\\nWINA次之（14.20）：weight-informed scoring考虑weight magnitude × activation， 但在50% high sparsity下，weight和activation的interaction是non-monotonic的 （large weight × small activation vs small weight × large activation的trade-off不清晰）， 导致pruning决策noisier。\\nR-Sparse居中（13.50）：rank-aware approach比pure magnitude好 （考虑了neurons之间的redundancy），但不如TEAL的greedy allocation adaptive。\\n三个training-free方法都比learned approaches差3-5 PPL以上， 确立了\\\"training-free < learned\\\"的hierarchy，justifying学习predictor的必要性。\\n\"\n  },\n  {\n    \"name\": \"Full benchmark evaluation + wall-clock profiling\",\n    \"description\": \"所有conditions在WikiText-2, C4, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval上的完整评估。 Wall-clock latency profiling + memory overhead。Pareto frontier。\\n\",\n    \"results\": {\n      \"dense_wikitext2_ppl\": 6.12,\n      \"dense_c4_ppl\": 8.88,\n      \"dense_arc_c\": 53.4,\n      \"dense_winogrande\": 74.2,\n      \"dense_mmlu\": 65.3,\n      \"dense_gsm8k\": 48.2,\n      \"dense_humaneval\": 33.5,\n      \"kl_only_wikitext2_ppl\": 9.53,\n      \"kl_only_c4_ppl\": 12.8,\n      \"kl_only_arc_c\": 51.5,\n      \"kl_only_winogrande\": 72.0,\n      \"kl_only_mmlu\": 63.0,\n      \"kl_only_gsm8k\": 46.2,\n      \"kl_only_humaneval\": 31.5,\n      \"kl_only_avg_acc_drop_vs_dense_pct\": 3.4,\n      \"bce_comp_wikitext2_ppl\": 11.56,\n      \"bce_comp_c4_ppl\": 15.2,\n      \"bce_comp_arc_c\": 50.2,\n      \"bce_comp_winogrande\": 70.5,\n      \"bce_comp_mmlu\": 61.8,\n      \"bce_comp_gsm8k\": 44.8,\n      \"bce_comp_humaneval\": 30.5,\n      \"bce_comp_avg_acc_drop_vs_dense_pct\": 5.2,\n      \"spon_kl_wikitext2_ppl\": 8.91,\n      \"spon_kl_c4_ppl\": 11.9,\n      \"spon_kl_arc_c\": 52.1,\n      \"spon_kl_winogrande\": 72.8,\n      \"spon_kl_mmlu\": 63.8,\n      \"spon_kl_gsm8k\": 47.0,\n      \"spon_kl_humaneval\": 32.0,\n      \"spon_kl_avg_acc_drop_vs_dense_pct\": 2.3,\n      \"teal_wikitext2_ppl\": 12.5,\n      \"teal_arc_c\": 47.8,\n      \"teal_mmlu\": 58.5,\n      \"teal_avg_acc_drop_vs_dense_pct\": 9.8,\n      \"dense_latency_ms_b1\": 18.0,\n      \"kl_only_latency_ms_b1\": 16.5,\n      \"bce_comp_latency_ms_b1\": 17.8,\n      \"spon_kl_latency_ms_b1\": 16.5,\n      \"kl_only_speedup_b1\": 1.09,\n      \"bce_comp_speedup_b1\": 1.01,\n      \"dense_latency_ms_b32\": 3.2,\n      \"kl_only_latency_ms_b32\": 2.15,\n      \"bce_comp_latency_ms_b32\": 2.72,\n      \"spon_kl_latency_ms_b32\": 2.15,\n      \"kl_only_speedup_b32\": 1.49,\n      \"bce_comp_speedup_b32\": 1.18,\n      \"kl_only_extra_params_mb\": 8,\n      \"bce_comp_extra_params_mb\": 264,\n      \"spon_kl_extra_params_mb\": 8.5\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Full benchmark comparison (Llama 3.1 8B, 50% sparsity)\",\n        \"columns\": [\n          \"Method\",\n          \"Wiki PPL↓\",\n          \"C4 PPL↓\",\n          \"ARC-c↑\",\n          \"WG↑\",\n          \"MMLU↑\",\n          \"GSM8K↑\",\n          \"HE↑\",\n          \"Avg Acc Drop\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            6.12,\n            8.88,\n            53.4,\n            74.2,\n            65.3,\n            48.2,\n            33.5,\n            \"—\"\n          ],\n          [\n            \"TEAL\",\n            12.5,\n            17.1,\n            47.8,\n            67.2,\n            58.5,\n            40.5,\n            27.0,\n            \"9.8%\"\n          ],\n          [\n            \"SPON\",\n            11.2,\n            15.5,\n            49.5,\n            69.8,\n            60.5,\n            43.0,\n            28.5,\n            \"7.0%\"\n          ],\n          [\n            \"BCE+comp\",\n            11.56,\n            15.2,\n            50.2,\n            70.5,\n            61.8,\n            44.8,\n            30.5,\n            \"5.2%\"\n          ],\n          [\n            \"KL-only\",\n            9.53,\n            12.8,\n            51.5,\n            72.0,\n            63.0,\n            46.2,\n            31.5,\n            \"3.4%\"\n          ],\n          [\n            \"SPON+KL\",\n            8.91,\n            11.9,\n            52.1,\n            72.8,\n            63.8,\n            47.0,\n            32.0,\n            \"2.3%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Inference efficiency (A100 GPU)\",\n        \"columns\": [\n          \"Method\",\n          \"Latency b=1 (ms)\",\n          \"Speedup b=1\",\n          \"Latency b=32 (ms)\",\n          \"Speedup b=32\",\n          \"Extra Params\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            18.0,\n            \"1.00×\",\n            3.2,\n            \"1.00×\",\n            \"—\"\n          ],\n          [\n            \"KL-only\",\n            16.5,\n            \"1.09×\",\n            2.15,\n            \"1.49×\",\n            \"8 MB\"\n          ],\n          [\n            \"SPON+KL\",\n            16.5,\n            \"1.09×\",\n            2.15,\n            \"1.49×\",\n            \"8.5 MB\"\n          ],\n          [\n            \"BCE+comp\",\n            17.8,\n            \"1.01×\",\n            2.72,\n            \"1.18×\",\n            \"264 MB\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Main paper table确认KL-only在quality和efficiency两个维度上都dominate BCE+comp。 Quality: 9.53 vs 11.56 PPL, 3.4% vs 5.2% downstream drop。 Efficiency: 1.49x vs 1.18x at b=32, 8MB vs 264MB extra params。 SPON+KL是quality-optimal (8.91, 2.3% drop) 且efficiency与KL-only相同。 This is the paper's main result table, supporting the \\\"simpler pipeline, better quality\\\" narrative。\\n\\n\\nDownstream accuracy: KL-only的2-5% relative drop反映PPL degradation在discriminative tasks上的衰减： PPL从6.12升至9.53 (+56%)，但downstream accuracy仅降3.4%，因为discriminative tasks 主要依赖representation quality而非exact next-token prediction，而50% sparsity下 KL predictor保留了most important neurons，representation受损有限。\\nBCE+comp的downstream drop更大(5.2%)因为compensation网络修正的是hidden state drift而非 representation quality——补偿了数值偏差但未恢复pruning导致的information loss。\\nSPON+KL最佳(2.3% drop)因为static bias correction + contextual prediction覆盖了 both systematic和input-specific errors，leaving minimal residual representation damage。\\nLatency: batch=1时memory-bandwidth bound，sparsity的compute reduction被parameter loading开销稀释， KL仅1.09x speedup。Batch=32时compute-bound，50% FFN sparsity的savings充分显现： KL 1.49x vs BCE+comp 1.18x——compensation网络的256MB参数和per-layer GEMV 吃掉了batch场景下1/3的sparsity savings。这是KL的practical efficiency论点的核心。\\n\"\n  },\n  {\n    \"name\": \"7-level sparsity sweep: KL vs BCE scaling\",\n    \"description\": \"30/35/40/45/50/55/60% sparsity下KL-only vs BCE-only。 Test: KL-BCE PPL delta ~ s²。1 seed per level。50%复用plan_001数据。\\n\",\n    \"results\": {\n      \"sparsity_levels\": [\n        0.3,\n        0.35,\n        0.4,\n        0.45,\n        0.5,\n        0.55,\n        0.6\n      ],\n      \"kl_only_ppls\": [\n        6.82,\n        7.28,\n        7.95,\n        8.58,\n        9.53,\n        11.2,\n        14.05\n      ],\n      \"bce_only_ppls\": [\n        11.32,\n        14.48,\n        18.95,\n        23.38,\n        28.16,\n        36.7,\n        49.05\n      ],\n      \"kl_bce_deltas\": [\n        4.5,\n        7.2,\n        11.0,\n        14.8,\n        18.63,\n        25.5,\n        35.0\n      ],\n      \"quadratic_fit_a\": 97.2,\n      \"quadratic_fit_r2\": 0.88,\n      \"residual_at_030\": -2.17,\n      \"residual_at_060\": 8.17\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Sparsity sweep — KL vs BCE PPL\",\n        \"columns\": [\n          \"Sparsity\",\n          \"KL PPL\",\n          \"BCE PPL\",\n          \"Δ(BCE-KL)\",\n          \"Quadratic prediction\",\n          \"Residual\"\n        ],\n        \"rows\": [\n          [\n            \"30%\",\n            6.82,\n            11.32,\n            4.5,\n            6.67,\n            -2.17\n          ],\n          [\n            \"35%\",\n            7.28,\n            14.48,\n            7.2,\n            9.07,\n            -1.87\n          ],\n          [\n            \"40%\",\n            7.95,\n            18.95,\n            11.0,\n            11.9,\n            -0.9\n          ],\n          [\n            \"45%\",\n            8.58,\n            23.38,\n            14.8,\n            15.08,\n            -0.28\n          ],\n          [\n            \"50%\",\n            9.53,\n            28.16,\n            18.63,\n            18.71,\n            -0.08\n          ],\n          [\n            \"55%\",\n            11.2,\n            36.7,\n            25.5,\n            22.79,\n            2.71\n          ],\n          [\n            \"60%\",\n            14.05,\n            49.05,\n            35.0,\n            27.31,\n            7.69\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3降级为\\\"consistent empirical trend\\\"而非\\\"precise quadratic law\\\"。 R²=0.88表明quadratic model解释了88%的variance，但systematic residual pattern (low-s sub-quadratic, high-s super-quadratic) 表明真实关系比s²更complex。 在paper中放appendix展示完整fit，main text仅claim \\\"KL advantage grows super-linearly with sparsity, consistent with the theoretical prediction that joint interaction effects scale with the number of pruned neurons\\\"。\\n\\n\\nKL-BCE delta随sparsity单调递增：低sparsity时BCE的per-neuron独立假设damage较小 （pruning少量neurons时joint interaction effect有限），高sparsity时damage急剧增大 （每个pruning决策影响更多remaining neurons的joint output）。\\nQuadratic fit R²=0.88：存在clear上升趋势，但不是clean quadratic。 Deviation pattern: 低sparsity处delta低于quadratic prediction（此时neuron interactions是sparse的， BCE的independence assumption伤害有限）；高sparsity处delta高于quadratic prediction （此时interaction density超过O(s²)的简化模型，higher-order terms变得significant）。\\n这支持\\\"KL gradient captures joint interactions that scale with sparsity\\\"的intuition， 但fit noise和systematic residual pattern意味着precise s² law不成立。 R² 0.88在0.80-0.95范围内，支持\\\"consistent empirical trend\\\"但不支持\\\"precise quantitative law\\\"。\\n\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 generalization validation\",\n    \"description\": \"KL-only vs BCE+comp @ 50% sparsity on Mistral-7B-v0.3。 Core benchmarks: WikiText-2, ARC-c, MMLU。3 seeds each。\\n\",\n    \"results\": {\n      \"mistral_dense_wikitext2_ppl\": 5.52,\n      \"mistral_kl_wikitext2_ppl_mean\": 9.38,\n      \"mistral_kl_wikitext2_ppl_std\": 0.35,\n      \"mistral_kl_wikitext2_ppl_seeds\": [\n        9.15,\n        9.35,\n        9.65\n      ],\n      \"mistral_kl_ppl_increase_vs_dense_pct\": 69.9,\n      \"mistral_kl_arc_c\": 52.8,\n      \"mistral_kl_mmlu\": 61.5,\n      \"mistral_bce_comp_wikitext2_ppl_mean\": 10.45,\n      \"mistral_bce_comp_wikitext2_ppl_std\": 0.48,\n      \"mistral_bce_comp_wikitext2_ppl_seeds\": [\n        10.1,\n        10.3,\n        10.95\n      ],\n      \"mistral_bce_comp_ppl_increase_vs_dense_pct\": 89.3,\n      \"mistral_bce_comp_arc_c\": 51.5,\n      \"mistral_bce_comp_mmlu\": 60.2,\n      \"mistral_kl_vs_bce_comp_gap\": 1.07,\n      \"llama_kl_vs_bce_comp_gap\": 2.03\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Cross-model validation (50% sparsity)\",\n        \"columns\": [\n          \"Model\",\n          \"Condition\",\n          \"Wiki PPL↓\",\n          \"ARC-c↑\",\n          \"MMLU↑\",\n          \"KL-BCE gap\"\n        ],\n        \"rows\": [\n          [\n            \"Llama 3.1 8B\",\n            \"Dense\",\n            6.12,\n            53.4,\n            65.3,\n            \"—\"\n          ],\n          [\n            \"Llama 3.1 8B\",\n            \"KL-only\",\n            9.53,\n            51.5,\n            63.0,\n            \"2.03\"\n          ],\n          [\n            \"Llama 3.1 8B\",\n            \"BCE+comp\",\n            11.56,\n            50.2,\n            61.8,\n            \"—\"\n          ],\n          [\n            \"Mistral 7B v0.3\",\n            \"Dense\",\n            5.52,\n            55.0,\n            63.5,\n            \"—\"\n          ],\n          [\n            \"Mistral 7B v0.3\",\n            \"KL-only\",\n            9.38,\n            52.8,\n            61.5,\n            \"1.07\"\n          ],\n          [\n            \"Mistral 7B v0.3\",\n            \"BCE+comp\",\n            10.45,\n            51.5,\n            60.2,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"回答reviewer concern #4 \\\"single model / limited generalization\\\"。 Mistral验证KL advantage的方向一致性，但smaller gap是honest finding—— 不同架构下advantage magnitude varies。Paper中报告为\\\"consistent across architectures\\\" 而非\\\"universal with fixed effect size\\\"。Mistral的GQA/sliding window解释 为gap缩小提供architectural intuition。\\n\\n\\nMistral同方向但relative gap更小 (1.07 vs Llama's 2.03 PPL)。原因： (1) Mistral的GQA (grouped-query attention) 产生更structured的activation pattern， SwiGLU层的neuron importance分布more concentrated (fewer \\\"ambiguous\\\" neurons near threshold)， 使得BCE的per-neuron独立预测在Mistral上less harmful。 (2) Mistral的sliding window attention导致信息更local，每个token的neuron importance 变化更平滑，减少了KL的contextual adaptation advantage。\\nKL PPL increase 70% vs dense (5.52→9.38) 在median tier的50-90%范围内。 BCE+comp PPL increase 89% (5.52→10.45) 表明compensation在Mistral上也有效。\\nGap缩小但方向一致：KL-only仍优于BCE+comp on all metrics， 证明KL advantage不是Llama-specific artifact，generalize across architectures。\\n\"\n  },\n  {\n    \"name\": \"LongBench English subset evaluation (4K-32K tokens)\",\n    \"description\": \"所有conditions在LongBench English subset上的评估： single-doc QA, multi-doc QA, summarization, few-shot, code。 测试predictor在超出训练序列长度时的generalization。\\n\",\n    \"results\": {\n      \"dense_single_doc_qa\": 42.5,\n      \"dense_multi_doc_qa\": 36.0,\n      \"dense_summarization\": 27.2,\n      \"dense_few_shot\": 60.0,\n      \"dense_code\": 34.0,\n      \"dense_avg\": 39.9,\n      \"kl_single_doc_qa\": 38.8,\n      \"kl_multi_doc_qa\": 32.2,\n      \"kl_summarization\": 25.5,\n      \"kl_few_shot\": 55.8,\n      \"kl_code\": 30.2,\n      \"kl_avg\": 36.5,\n      \"kl_avg_drop_pct\": 8.5,\n      \"bce_comp_single_doc_qa\": 36.5,\n      \"bce_comp_multi_doc_qa\": 30.0,\n      \"bce_comp_summarization\": 24.2,\n      \"bce_comp_few_shot\": 53.5,\n      \"bce_comp_code\": 28.5,\n      \"bce_comp_avg\": 34.5,\n      \"bce_comp_avg_drop_pct\": 13.5,\n      \"spon_kl_single_doc_qa\": 39.5,\n      \"spon_kl_multi_doc_qa\": 33.0,\n      \"spon_kl_summarization\": 25.8,\n      \"spon_kl_few_shot\": 56.5,\n      \"spon_kl_code\": 31.0,\n      \"spon_kl_avg\": 37.2,\n      \"spon_kl_avg_drop_pct\": 6.8,\n      \"teal_avg\": 31.5,\n      \"teal_avg_drop_pct\": 21.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: LongBench performance (English subset)\",\n        \"columns\": [\n          \"Method\",\n          \"Single-doc QA\",\n          \"Multi-doc QA\",\n          \"Summ.\",\n          \"Few-shot\",\n          \"Code\",\n          \"Avg\",\n          \"Avg Drop\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            42.5,\n            36.0,\n            27.2,\n            60.0,\n            34.0,\n            39.9,\n            \"—\"\n          ],\n          [\n            \"TEAL\",\n            34.0,\n            27.5,\n            23.0,\n            48.5,\n            24.5,\n            31.5,\n            \"21.1%\"\n          ],\n          [\n            \"BCE+comp\",\n            36.5,\n            30.0,\n            24.2,\n            53.5,\n            28.5,\n            34.5,\n            \"13.5%\"\n          ],\n          [\n            \"KL-only\",\n            38.8,\n            32.2,\n            25.5,\n            55.8,\n            30.2,\n            36.5,\n            \"8.5%\"\n          ],\n          [\n            \"SPON+KL\",\n            39.5,\n            33.0,\n            25.8,\n            56.5,\n            31.0,\n            37.2,\n            \"6.8%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Long-context generalization是KL approach的非trivial validation： predictor trained on short sequences仍在long context下保持8.5% average drop。 KL vs BCE+comp gap在long context下expand (8.5% vs 13.5%)，suggesting KL's distributional supervision provides better OOD robustness。 SPON+KL进一步improve (6.8%)，supporting the composition claim's practical value。\\n\\n\\nLong-context evaluation drop (KL avg 8.5%) 大于short-context downstream (3.4%)， 因为predictor在2048-token序列上训练，推广到4K-32K时neuron importance distribution shifts： 长文本中attention pattern更diffuse，neuron activation的long-range dependency增加， predictor需要在unseen的activation regime下做决策。\\nKL仍优于BCE+comp (8.5% vs 13.5% drop)：KL的output-distribution supervision在 distributional shift下更robust，因为即使在OOD inputs上，KL梯度仍push predictor 去最小化logit divergence，而BCE的target masks在OOD时可能fundamentally错误 （训练时的\\\"correct\\\" mask对长文本不适用）。\\nPer-task pattern: multi-doc QA和code drop最大（需要跨document/long-range reasoning， 对neuron selection错误最敏感）；summarization drop最小（更tolerant of approximate representation， 核心信息在early tokens中已被captured）。\\nSPON+KL最佳 (6.8% drop)：SPON的static bias correction在长文本中仍然valid （average drift不依赖sequence length），提供stable baseline correction。\\n\"\n  },\n  {\n    \"name\": \"MT-Bench evaluation with GPT-4o judge\",\n    \"description\": \"80 multi-turn questions, 8 categories。All conditions。 Tests instruction-following quality under sparsity。\\n\",\n    \"results\": {\n      \"dense_mt_bench_avg\": 7.25,\n      \"kl_only_mt_bench_avg\": 6.72,\n      \"bce_comp_mt_bench_avg\": 6.38,\n      \"spon_kl_mt_bench_avg\": 6.85,\n      \"teal_mt_bench_avg\": 5.8,\n      \"kl_mt_writing\": 7.1,\n      \"kl_mt_roleplay\": 6.9,\n      \"kl_mt_reasoning\": 6.2,\n      \"kl_mt_math\": 5.8,\n      \"kl_mt_coding\": 6.5,\n      \"kl_mt_extraction\": 7.3,\n      \"kl_mt_stem\": 6.8,\n      \"kl_mt_humanities\": 7.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: MT-Bench scores by category (GPT-4o judge)\",\n        \"columns\": [\n          \"Category\",\n          \"Dense\",\n          \"KL-only\",\n          \"BCE+comp\",\n          \"SPON+KL\"\n        ],\n        \"rows\": [\n          [\n            \"Writing\",\n            7.5,\n            7.1,\n            6.8,\n            7.2\n          ],\n          [\n            \"Roleplay\",\n            7.3,\n            6.9,\n            6.5,\n            7.0\n          ],\n          [\n            \"Reasoning\",\n            6.8,\n            6.2,\n            5.8,\n            6.4\n          ],\n          [\n            \"Math\",\n            6.5,\n            5.8,\n            5.3,\n            6.0\n          ],\n          [\n            \"Coding\",\n            7.0,\n            6.5,\n            6.1,\n            6.7\n          ],\n          [\n            \"Extraction\",\n            7.8,\n            7.3,\n            7.0,\n            7.5\n          ],\n          [\n            \"STEM\",\n            7.2,\n            6.8,\n            6.4,\n            6.9\n          ],\n          [\n            \"Humanities\",\n            7.9,\n            7.2,\n            7.2,\n            7.3\n          ],\n          [\n            \"Average\",\n            7.25,\n            6.72,\n            6.38,\n            6.85\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MT-Bench验证KL approach在instruction-following场景下的质量保持。 Average drop 0.53 for KL vs 0.87 for BCE+comp, consistent with PPL results。 Category-level breakdown provides actionable insight: math/reasoning是sparsity的weak spot， 可作为future work的optimization target。EMNLP reviewers重视NLP-specific evaluation， MT-Bench作为multi-turn generation quality metric补充了discriminative benchmarks。\\n\\n\\nMT-Bench average drop: KL -0.53, BCE+comp -0.87。Multi-turn instruction following 对model quality less sensitive than PPL would suggest：MT-Bench更多测试format compliance 和high-level reasoning，而非exact token probability。但math和reasoning categories 受sparsity影响最大（6.2, 5.8 for KL），因为这些需要precise computation chains where even small representation errors accumulate across reasoning steps。\\nWriting和extraction受影响最小（7.1, 7.3），因为这些依赖pattern matching和formatting rather than deep logical reasoning。\\nKL显著优于BCE+comp in multi-turn setting：multi-turn对话中error accumulation更严重， KL的lower per-step error导致multi-turn quality degradation更小。\\n\"\n  },\n  {\n    \"name\": \"RULER synthetic long-context evaluation\",\n    \"description\": \"RULER @ 4K和16K context，3 representative task types。 Fine-grained capability diagnostics complementing LongBench。\\n\",\n    \"results\": {\n      \"dense_ruler_4k_avg\": 92.0,\n      \"kl_only_ruler_4k_avg\": 85.5,\n      \"bce_comp_ruler_4k_avg\": 81.0,\n      \"spon_kl_ruler_4k_avg\": 87.0,\n      \"dense_ruler_16k_avg\": 85.0,\n      \"kl_only_ruler_16k_avg\": 73.5,\n      \"bce_comp_ruler_16k_avg\": 67.0,\n      \"spon_kl_ruler_16k_avg\": 75.5,\n      \"kl_ruler_16k_needle_retrieval\": 78.0,\n      \"kl_ruler_16k_multi_key\": 70.5,\n      \"kl_ruler_16k_aggregation\": 72.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: RULER evaluation at 4K and 16K context\",\n        \"columns\": [\n          \"Method\",\n          \"4K Avg\",\n          \"16K Avg\",\n          \"4K→16K Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Dense\",\n            92.0,\n            85.0,\n            \"-7.0\"\n          ],\n          [\n            \"KL-only\",\n            85.5,\n            73.5,\n            \"-12.0\"\n          ],\n          [\n            \"SPON+KL\",\n            87.0,\n            75.5,\n            \"-11.5\"\n          ],\n          [\n            \"BCE+comp\",\n            81.0,\n            67.0,\n            \"-14.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RULER确认LongBench的findings: KL在long context下更robust than BCE+comp， 且degradation rate (slope) 更小。作为appendix-level diagnostic complement LongBench的 naturalistic evaluation。4K→16K的degradation pattern suggest training on longer sequences could improve predictor robustness（future work direction）。\\n\\nRULER的synthetic tasks提供controlled diagnostics： 4K时KL drop 7% (85.5 vs 92.0)，与LongBench consistent但more controlled。 16K时KL drop增大到13.5% (73.5 vs 85.0)，表明predictor的generalization 随context length增加而degrade——在超出训练distribution的长context中， predictor对late-position tokens的neuron importance估计less accurate （attention pattern在long context中more diffuse，activation statistics shift）。\\nNeedle retrieval (78.0 at 16K) 相对较好因为retrieval主要依赖attention mechanism 而非FFN computation。Multi-key (70.5) 和aggregation (72.0) 更差因为 需要跨position的information integration，FFN computation的precision更重要。\\nBCE+comp在16K时drop更严重 (67.0, 21.2% drop)：compensation网络在OOD context下 不仅没帮助，反而可能introduce noise（compensation trained on short context的correction pattern在long context下不适用）。\\n\"\n  }\n]",
      "numLines": 1050,
      "startLine": 1,
      "totalLines": 1050
    }
  },
  "sourceToolAssistantUUID": "7da3a816-073f-4a79-a281-5c08b21b5f8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "ab1f0b6a-baf9-4110-a628-7375b55aa5d6",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260515T164925",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Assistant

_source line 14 · 2026-05-15T17:30:36.779Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write the LaTeX paper. Let me first check that the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab1f0b6a-baf9-4110-a628-7375b55aa5d6",
  "isSidechain": false,
  "requestId": "req_011Cb4kZKrUSLLmXrbKDfeHZ",
  "type": "assistant",
  "uuid": "7bceb37b-8091-49b2-af32-014007b178aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4eEosafoCdVVqKdhTjrpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 16974,
      "cache_read_input_tokens": 23084,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 185,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 16974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16974
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

_source line 15 · 2026-05-15T17:30:37.201Z_

Now I have all the data. Let me write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bceb37b-8091-49b2-af32-014007b178aa",
  "isSidechain": false,
  "requestId": "req_011Cb4kZKrUSLLmXrbKDfeHZ",
  "type": "assistant",
  "uuid": "8a09218e-3b4a-489b-a0eb-3e305a8eee35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4eEosafoCdVVqKdhTjrpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 16974,
      "cache_read_input_tokens": 23084,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 185,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 16974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16974
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

_source line 16 · 2026-05-15T17:30:39.600Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Vwf98JPX1hkKQBELqJsY53`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/",
  "description": "Check output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a09218e-3b4a-489b-a0eb-3e305a8eee35",
  "isSidechain": false,
  "requestId": "req_011Cb4kZKrUSLLmXrbKDfeHZ",
  "type": "assistant",
  "uuid": "44637c6b-2a04-4b7b-a6a6-de2328b861b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4eEosafoCdVVqKdhTjrpc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1367,
      "cache_creation_input_tokens": 16974,
      "cache_read_input_tokens": 23084,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1367,
          "output_tokens": 185,
          "cache_read_input_tokens": 23084,
          "cache_creation_input_tokens": 16974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16974
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

_source line 17 · 2026-05-15T17:30:39.780Z_

<details><summary>↩ Tool result · `toolu_01Vwf98JPX1hkKQBELqJsY53`</summary>

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
  "parentUuid": "44637c6b-2a04-4b7b-a6a6-de2328b861b5",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "ff6d26c7-cf29-492a-b982-9a2bb4e58cb4",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "44637c6b-2a04-4b7b-a6a6-de2328b861b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T17:33:55.402Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VWr2rQ8U5vrRh3w23cSLoT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\method}{KL-Sparse}\n\n\\title{Output-Distribution Distillation Eliminates Compensation Overhead\\\\for Contextual SwiGLU Sparsity Prediction}\n\n\\author{\n  Anonymous Authors\n}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedups through dynamic neuron pruning, but existing approaches face a quality--efficiency trade-off: training-free heuristics leave large quality gaps, while learned BCE-trained predictors require auxiliary compensation networks adding ${\\sim}$256\\,MB of parameters and per-layer GEMV overhead. We present a systematic study of training signal and correction granularity for contextual sparsity prediction, organized around a two-dimensional taxonomy (loss coupling $\\times$ correction granularity). Our key finding is that a KL-divergence-trained contextual predictor achieves \\textbf{9.53 perplexity} on WikiText-2 at 50\\% model-level sparsity on Llama~3.1~8B---surpassing BCE+compensation (11.56) while eliminating compensation parameters entirely. This result reframes the role of compensation: output-distribution distillation during predictor training preempts the errors that compensation networks correct post-hoc. We further show that static bias correction (SPON) and contextual KL prediction compose with partial additivity (22\\% interaction residual), and that the KL advantage over BCE grows super-linearly with sparsity. Across seven benchmarks, two model families, and long-context evaluations, KL-trained prediction achieves 1.49$\\times$ batch-32 speedup with only 3.4\\% average accuracy drop and 8\\,MB overhead.\n\\end{abstract}\n\n% ===========================================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks in modern LLMs exhibit substantial contextual activation sparsity: at any given token, 40--60\\% of intermediate neurons contribute negligibly to the output. Exploiting this sparsity at inference time promises significant speedups without architectural modification. However, realizing this promise requires solving the \\emph{sparsity prediction problem}: determining which neurons to prune for each input.\n\nExisting approaches span a spectrum. \\textbf{Training-free methods} (TEAL, WINA, R-Sparse) use magnitude-based heuristics with zero training cost, but leave a 6--8 PPL gap at 50\\% sparsity. \\textbf{Static learned corrections} (SPON) train per-layer bias vectors via KL distillation to compensate average activation drift, achieving zero inference overhead but limited by input-independence. \\textbf{Contextual learned predictors} (FastForward) train per-token predictors with BCE loss against binarized activation masks, achieving near-dense quality but requiring auxiliary compensation MLPs (${\\sim}$256\\,MB) to correct prediction errors---adding parameters and per-layer GEMV operations that partially negate sparsity benefits.\n\nA fundamental question remains unexplored: \\emph{does the choice of training signal for the contextual predictor determine whether compensation is necessary?} We observe that the gradient structures of BCE and KL losses differ qualitatively. The BCE gradient $\\partial \\mathcal{L}_{\\text{BCE}}/\\partial s_j$ depends only on neuron $j$'s activation---a factorized, per-neuron signal. In contrast, the KL gradient $\\partial \\mathcal{L}_{\\text{KL}}/\\partial s_j$ couples all active neurons through $\\partial \\text{logits}/\\partial \\mathbf{h} \\cdot \\partial \\mathbf{h}/\\partial \\mathbf{m}$, propagating output-distribution-level supervision to each masking decision. This coupling allows KL-trained predictors to optimize joint neuron selection, capturing interaction effects that BCE structurally misses.\n\nWe organize prior work and our contributions in a two-dimensional taxonomy crossing \\emph{training signal coupling} (decomposed/BCE $\\rightarrow$ coupled/KL) with \\emph{correction granularity} (static $\\rightarrow$ per-token contextual), revealing an unexplored cell: per-token contextual prediction trained with coupled KL supervision.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{KL eliminates compensation overhead at quality parity.} At 50\\% sparsity, KL-only prediction (PPL 9.53) surpasses BCE+compensation (PPL 11.56) while requiring zero compensation parameters, yielding a simpler and more efficient inference pipeline (1.49$\\times$ vs.\\ 1.18$\\times$ speedup at batch 32, 8\\,MB vs.\\ 264\\,MB overhead).\n\\item \\textbf{Empirically observed partial additivity of correction mechanisms.} SPON (static) and KL (contextual) corrections compose to achieve the best overall quality (PPL 8.91), with a 22\\% interaction residual honestly characterizing their overlap.\n\\item \\textbf{Taxonomy and systematic ablation as methodological contribution.} Our two-dimensional taxonomy, four-condition ablation, iso-compute comparison, and STE baseline provide a rigorous framework for understanding sparsity prediction design choices.\n\\end{enumerate}\n\n\n% ===========================================================================\n\\section{Background and Related Work}\n\n\\paragraph{Activation sparsity in SwiGLU LLMs.}\nThe SwiGLU activation $\\text{SwiGLU}(\\mathbf{x}) = (\\mathbf{x}\\mathbf{W}_1 \\odot \\sigma(\\mathbf{x}\\mathbf{W}_g)) \\mathbf{W}_2$ produces naturally sparse intermediate representations, as the sigmoid gate $\\sigma(\\mathbf{x}\\mathbf{W}_g)$ drives many neurons toward zero. This contextual sparsity can be exploited by skipping near-zero neurons during inference, reducing FLOPs proportionally.\n\n\\paragraph{Training-free methods.}\nTEAL combines activation magnitude with greedy per-layer sparsity allocation. WINA uses weight-informed neuron scoring. R-Sparse incorporates rank-aware redundancy information. These methods require no training but achieve suboptimal quality at high sparsity levels.\n\n\\paragraph{Static learned corrections.}\nSPON trains per-layer bias vectors using KL divergence to correct average activation drift from pruning. The bias vectors add negligible parameters (${\\sim}$0.5\\,MB) and zero inference latency (fused into existing computations), but cannot adapt to per-input neuron importance variations.\n\n\\paragraph{Contextual learned predictors.}\nFastForward trains lightweight MLPs to predict per-token neuron importance using BCE loss against binarized activation targets, augmented with compensation networks that correct residual errors in the sparse hidden states. The compensation adds ${\\sim}$256\\,MB of parameters and per-layer GEMV operations.\n\n\\paragraph{Two-dimensional taxonomy.}\nWe organize these approaches along two axes (Table~\\ref{tab:taxonomy}): \\emph{training signal coupling} (how much inter-neuron information the loss gradient carries) and \\emph{correction granularity} (whether correction is input-independent or per-token). This taxonomy reveals that no prior work combines per-token contextual prediction with coupled KL training.\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of sparsity prediction methods. Our work fills the previously empty per-token contextual + coupled KL cell.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token contextual & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ===========================================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a pretrained SwiGLU LLM, we train a lightweight predictor $f_\\theta$ that, for each input token, produces a binary mask $\\mathbf{m} \\in \\{0,1\\}^D$ selecting which of the $D$ intermediate neurons to activate. The mask is applied element-wise: $\\tilde{\\mathbf{h}} = \\mathbf{m} \\odot \\mathbf{h}$, where $\\mathbf{h}$ is the dense intermediate representation.\n\n\\subsection{Training Signal: KL Divergence}\n\nWe train the predictor by minimizing the KL divergence between the output distributions of the dense and sparse models:\n\\begin{equation}\n\\mathcal{L}_{\\text{KL}} = \\text{KL}\\!\\left(p_{\\text{dense}}(\\cdot \\mid x) \\;\\|\\; p_{\\text{sparse}}(\\cdot \\mid x; \\theta)\\right)\n\\end{equation}\nwhere $p_{\\text{sparse}}$ denotes the model's output distribution when neurons are masked according to $f_\\theta(x)$.\n\n\\paragraph{Gradient coupling.} The key property distinguishing KL from BCE training is gradient structure. For the BCE loss, $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j$ depends only on whether neuron $j$'s predicted importance matches its binarized target---a factorized signal. For the KL loss:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\text{logits}} \\cdot \\frac{\\partial \\text{logits}}{\\partial \\mathbf{h}} \\cdot \\frac{\\partial \\mathbf{h}}{\\partial m_j} \\cdot \\frac{\\partial m_j}{\\partial s_j}\n\\end{equation}\nThe chain through $\\partial \\text{logits}/\\partial \\mathbf{h}$ couples all neurons: whether neuron $j$ should be active depends on which \\emph{other} neurons are active, because their joint contribution determines the output distribution. This coupling is a mathematical property of the gradient, not an analogy.\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\nTo enable gradient-based optimization of discrete masks, we use Gumbel-sigmoid relaxation during training:\n\\begin{equation}\n\\tilde{m}_j = \\sigma\\!\\left(\\frac{s_j + g_1 - g_2}{\\tau}\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1)\n\\end{equation}\nwhere $s_j = f_\\theta(x)_j$ is the predictor's logit for neuron $j$ and $\\tau$ is the temperature. At inference, we use hard thresholding: $m_j = \\mathbf{1}[s_j > 0]$.\n\n\\subsection{Composition with Static Correction}\n\nWe also explore composing the contextual KL predictor with SPON's static bias correction. SPON learns per-layer bias vectors $\\mathbf{b}_l$ to correct average activation drift:\n\\begin{equation}\n\\tilde{\\mathbf{h}}_l = \\mathbf{m}_l \\odot \\mathbf{h}_l + \\mathbf{b}_l\n\\end{equation}\nThe composition applies both the contextual mask (from KL predictor) and the static correction (from SPON), yielding $c = c_s + c_\\theta(x)$ where $c_s$ addresses systematic drift and $c_\\theta(x)$ adapts to per-input neuron importance.\n\n\n% ===========================================================================\n\\section{Experiments}\n\nAll experiments use 50\\% model-level sparsity unless otherwise noted. Our primary model is Llama~3.1~8B; we validate on Mistral-7B-v0.3. All learned methods are trained on a calibration set of 128 sequences (2048 tokens each) from C4. We report WikiText-2 perplexity as the primary metric, supplemented by downstream benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), long-context evaluations (LongBench, RULER), and instruction-following quality (MT-Bench with GPT-4o judge).\n\n% ---------------------------------------------------------------------------\n\\subsection{Training-Free Baselines}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} establishes the performance of training-free methods, motivating the need for learned predictors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training-free baselines at 50\\% model-level sparsity (Llama 3.1 8B).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nMethod & WikiText-2 PPL ($\\downarrow$) & $\\Delta$ vs Dense & Training Cost \\\\\n\\midrule\nDense & 6.12 & --- & --- \\\\\nTEAL & 12.50 & +6.38 & 0 \\\\\nR-Sparse & 13.50 & +7.38 & 0 \\\\\nWINA & 14.20 & +8.08 & 0 \\\\\n\\midrule\nKL-only (ref.) & 9.53 & +3.41 & 3.8\\,h \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining-free heuristics leave a 6--8 PPL gap versus the dense model. TEAL is the strongest baseline (12.50) owing to its greedy per-layer allocation, but all three methods substantially underperform learned predictors, establishing a clear hierarchy: training-free (12.5--14.2) $\\rightarrow$ static-learned (11.2) $\\rightarrow$ contextual-learned (9.5).\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Four-Condition Ablation: Loss $\\times$ Compensation}\n\\label{sec:ablation}\n\nOur central experiment crosses two factors: training loss (BCE vs.\\ KL) and compensation (present vs.\\ absent), yielding four conditions (Table~\\ref{tab:four_cond}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-condition ablation at 50\\% model-level sparsity (Llama 3.1 8B). KL-only achieves better quality than BCE+compensation while requiring zero compensation parameters.}\n\\label{tab:four_cond}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & WikiText-2 PPL ($\\downarrow$) & Seeds & Comp.\\ Params & Pipeline \\\\\n\\midrule\nDense (reference) & 6.12 & --- & --- & --- \\\\\nBCE-only & 28.16 $\\pm$ 0.21 & 3 & 0 & Simple \\\\\nBCE + compensation & 11.56 $\\pm$ 0.61 & 5 & 256\\,MB & Complex \\\\\nKL-only & 9.53 $\\pm$ 0.41 & 5 & 0 & Simple \\\\\nKL + compensation & 9.05 $\\pm$ 0.15 & 3 & 256\\,MB & Complex \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (9.53) outperforms BCE+compensation (11.56) by 2.03 PPL while requiring zero compensation overhead. Adding compensation to KL yields only a marginal improvement (9.53 $\\rightarrow$ 9.05, $\\Delta$ = 0.48), indicating that KL training preemptively addresses the errors compensation is designed to correct. In contrast, compensation is essential for BCE (28.16 $\\rightarrow$ 11.56, $\\Delta$ = 16.60), confirming that BCE's factorized gradient leaves substantial joint-interaction errors that require post-hoc correction.\n\n% ---------------------------------------------------------------------------\n\\subsection{Isolating Loss vs.\\ Relaxation: STE Baseline}\n\\label{sec:ste}\n\nTo disentangle the contributions of the KL loss function and the Gumbel-sigmoid relaxation, we train a predictor with KL loss but using the Straight-Through Estimator (STE) instead of Gumbel-sigmoid (Table~\\ref{tab:ste}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Loss function vs.\\ relaxation method ablation. KL contributes 72\\% of the total gain over BCE-only; Gumbel-sigmoid contributes 28\\%.}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nCondition & Loss & Relaxation & WikiText-2 PPL & Gain over BCE-only \\\\\n\\midrule\nBCE-only & BCE & STE & 28.16 & --- \\\\\nKL + STE & KL & STE & 14.70 $\\pm$ 0.60 & 13.46 (72\\%) \\\\\nKL + Gumbel & KL & Gumbel-$\\sigma$ & 9.53 $\\pm$ 0.41 & 18.63 (100\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL + STE (14.70) already substantially outperforms BCE-only (28.16), confirming that the KL loss function---not the relaxation method---is the primary driver of improvement (72\\% of total gain). Gumbel-sigmoid contributes a meaningful additional 28\\%, as its smooth gradients enable finer-grained mask optimization at decision boundaries. Both components are necessary for optimal performance.\n\n% ---------------------------------------------------------------------------\n\\subsection{Iso-Compute Comparison}\n\\label{sec:isocompute}\n\nKL training requires a dense forward pass per step (66.0 TFLOPs/step) while BCE uses cached targets (0.8 TFLOPs/step). To ensure KL's advantage is not simply a compute artifact, we extend BCE training to 33{,}000 steps to match KL's total GPU-hours (Table~\\ref{tab:isocompute}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Iso-compute comparison. Even with equivalent total compute, BCE trails KL by ${\\sim}$14 PPL.}\n\\label{tab:isocompute}\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\nCondition & Per-step TFLOPs & Total Steps & GPU-hours & WikiText-2 PPL \\\\\n\\midrule\nKL + Gumbel & 66.0 & 1{,}000 & 3.8 & 9.53 $\\pm$ 0.41 \\\\\nBCE (standard) & 0.8 & 1{,}000 & 0.4 & 28.16 $\\pm$ 0.21 \\\\\nBCE (iso-compute) & 0.8 & 33{,}000 & 3.8 & 23.50 $\\pm$ 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training reduces PPL from 28.16 to 23.50---a meaningful but insufficient improvement. The 14 PPL gap versus KL persists, confirming that BCE's information bottleneck lies in the factorized loss structure, not the training budget. Additional BCE steps improve predictor generalization but cannot capture joint neuron interactions that the loss function structurally excludes.\n\n% ---------------------------------------------------------------------------\n\\subsection{SPON Reproduction and Composition}\n\\label{sec:composition}\n\n\\paragraph{SPON reproduction.}\nWe reimplement SPON (learnable per-layer bias vectors + KL training) on Llama~3.1~8B and verify reproduction against published results (Table~\\ref{tab:spon_repro}). Our reproduction achieves WikiText-2 PPL of 11.20, within the expected range, with QA benchmark deltas within $\\pm$1.2\\% of published values.\n\n\\begin{table}[t]\n\\centering\n\\caption{SPON reproduction on Llama 3.1 8B---QA benchmark comparison at 50\\% sparsity.}\n\\label{tab:spon_repro}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nBenchmark & Dense & SPON (ours) & $\\Delta$ vs.\\ published \\\\\n\\midrule\nARC-c & 53.4\\% & 49.5\\% & +1.2\\% \\\\\nARC-e & 81.2\\% & 75.8\\% & $-$0.5\\% \\\\\nBoolQ & 83.5\\% & 78.2\\% & +0.8\\% \\\\\nPIQA & 81.0\\% & 77.5\\% & $-$1.0\\% \\\\\nWinoGrande & 74.2\\% & 69.8\\% & +0.6\\% \\\\\n\\midrule\nWikiText-2 PPL & 6.12 & 11.20 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Composition analysis.}\nWe combine SPON's static bias correction with our KL contextual predictor (Table~\\ref{tab:composition}). The composition achieves 8.91 PPL---the best overall result---but with a 22\\% interaction residual relative to a hypothetical fully additive prediction (8.23).\n\n\\begin{table}[t]\n\\centering\n\\caption{Composition additivity analysis. SPON and KL corrections compose with partial additivity; the 22\\% interaction residual reflects overlap in what each mechanism corrects.}\n\\label{tab:composition}\n\\small\n\\begin{tabular}{lcr}\n\\toprule\nCondition & WikiText-2 PPL & $\\Delta$ from TEAL \\\\\n\\midrule\nTEAL (no learned correction) & 12.50 & --- \\\\\nSPON only & 11.20 & $-$1.30 \\\\\nKL-only & 9.53 & $-$2.97 \\\\\nSPON + KL (if fully additive) & 8.23 & $-$4.27 \\\\\nSPON + KL (actual) & 8.91 $\\pm$ 0.14 & $-$3.59 \\\\\n\\midrule\nInteraction residual & --- & 0.68 (22\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe interaction arises because KL training partially learns to correct the mean drift that SPON addresses---the KL gradient pushes the predictor to minimize all correctable errors, including systematic bias. Per-layer analysis reveals that early (attention-heavy) layers show near-orthogonal corrections (cosine similarity ${\\sim}$0.10), while middle (FFN-heavy) layers show greater overlap (cosine ${\\sim}$0.25). We characterize this as \\emph{partial additivity}: the composition provides meaningful gains but should not be interpreted as clean decomposition.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Full Benchmark Evaluation}\n\\label{sec:full_eval}\n\nTable~\\ref{tab:full_bench} presents results across seven benchmarks. KL-only achieves 3.4\\% average accuracy drop versus dense, outperforming BCE+compensation (5.2\\%) and TEAL (9.8\\%). SPON+KL achieves the best quality at 2.3\\% average drop.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full benchmark comparison (Llama 3.1 8B, 50\\% sparsity).}\n\\label{tab:full_bench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccccr}\n\\toprule\nMethod & Wiki$\\downarrow$ & C4$\\downarrow$ & ARC-c$\\uparrow$ & WG$\\uparrow$ & MMLU$\\uparrow$ & GSM8K$\\uparrow$ & HE$\\uparrow$ & Avg Drop \\\\\n\\midrule\nDense & 6.12 & 8.88 & 53.4 & 74.2 & 65.3 & 48.2 & 33.5 & --- \\\\\nTEAL & 12.50 & 17.10 & 47.8 & 67.2 & 58.5 & 40.5 & 27.0 & 9.8\\% \\\\\nSPON & 11.20 & 15.50 & 49.5 & 69.8 & 60.5 & 43.0 & 28.5 & 7.0\\% \\\\\nBCE+comp & 11.56 & 15.20 & 50.2 & 70.5 & 61.8 & 44.8 & 30.5 & 5.2\\% \\\\\nKL-only & 9.53 & 12.80 & 51.5 & 72.0 & 63.0 & 46.2 & 31.5 & 3.4\\% \\\\\nSPON+KL & 8.91 & 11.90 & 52.1 & 72.8 & 63.8 & 47.0 & 32.0 & 2.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Inference efficiency.}\nTable~\\ref{tab:efficiency} reports wall-clock latency on an A100 GPU. At batch size 32 (compute-bound regime), KL-only achieves 1.49$\\times$ speedup versus 1.18$\\times$ for BCE+compensation---the compensation network's 256\\,MB parameters and per-layer GEMV operations consume roughly one-third of the sparsity savings. At batch size 1 (memory-bandwidth-bound), sparsity benefits are smaller across all methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference efficiency (A100 GPU).}\n\\label{tab:efficiency}\n\\small\n\\begin{tabular}{lccccr}\n\\toprule\nMethod & Lat.\\ $b$=1 & Speedup $b$=1 & Lat.\\ $b$=32 & Speedup $b$=32 & Extra Params \\\\\n\\midrule\nDense & 18.0\\,ms & 1.00$\\times$ & 3.20\\,ms & 1.00$\\times$ & --- \\\\\nKL-only & 16.5\\,ms & 1.09$\\times$ & 2.15\\,ms & 1.49$\\times$ & 8\\,MB \\\\\nSPON+KL & 16.5\\,ms & 1.09$\\times$ & 2.15\\,ms & 1.49$\\times$ & 8.5\\,MB \\\\\nBCE+comp & 17.8\\,ms & 1.01$\\times$ & 2.72\\,ms & 1.18$\\times$ & 264\\,MB \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---------------------------------------------------------------------------\n\\subsection{Cross-Model Generalization}\n\\label{sec:mistral}\n\nTo verify that KL's advantage is not architecture-specific, we evaluate on Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model validation at 50\\% sparsity. KL advantage direction is consistent; magnitude varies by architecture.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Condition & Wiki PPL$\\downarrow$ & ARC-c$\\uparrow$ & MMLU$\\uparrow$ & KL--BCE gap \\\\\n\\midrule\nLlama 3.1 8B & Dense & 6.12 & 53.4 & 65.3 & --- \\\\\nLlama 3.1 8B & KL-only & 9.53 & 51.5 & 63.0 & 2.03 \\\\\nLlama 3.1 8B & BCE+comp & 11.56 & 50.2 & 61.8 & --- \\\\\n\\midrule\nMistral 7B v0.3 & Dense & 5.52 & 55.0 & 63.5 & --- \\\\\nMistral 7B v0.3 & KL-only & 9.38 & 52.8 & 61.5 & 1.07 \\\\\nMistral 7B v0.3 & BCE+comp & 10.45 & 51.5 & 60.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only consistently outperforms BCE+compensation on both architectures. The smaller gap on Mistral (1.07 vs.\\ 2.03) is expected: Mistral's GQA produces more concentrated activation patterns where BCE's per-neuron independence assumption is less harmful, and sliding window attention reduces per-token variation in neuron importance. The directional consistency across architectures supports generalizability; the magnitude variation calls for architecture-aware analysis rather than universal effect-size claims.\n\n% ---------------------------------------------------------------------------\n\\subsection{Long-Context Evaluation}\n\\label{sec:longcontext}\n\nWe evaluate on LongBench (English subset, 4K--32K tokens) and RULER (synthetic tasks at 4K and 16K) to test predictor generalization beyond training sequence length (2048 tokens).\n\n\\begin{table}[t]\n\\centering\n\\caption{LongBench performance (English subset). KL-only maintains lower degradation than BCE+compensation, with SPON+KL achieving the smallest average drop.}\n\\label{tab:longbench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccccr}\n\\toprule\nMethod & S-QA & M-QA & Summ. & Few-shot & Code & Avg & Drop \\\\\n\\midrule\nDense & 42.5 & 36.0 & 27.2 & 60.0 & 34.0 & 39.9 & --- \\\\\nTEAL & 34.0 & 27.5 & 23.0 & 48.5 & 24.5 & 31.5 & 21.1\\% \\\\\nBCE+comp & 36.5 & 30.0 & 24.2 & 53.5 & 28.5 & 34.5 & 13.5\\% \\\\\nKL-only & 38.8 & 32.2 & 25.5 & 55.8 & 30.2 & 36.5 & 8.5\\% \\\\\nSPON+KL & 39.5 & 33.0 & 25.8 & 56.5 & 31.0 & 37.2 & 6.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{RULER evaluation at 4K and 16K context lengths.}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nMethod & 4K Avg & 16K Avg & 4K$\\rightarrow$16K $\\Delta$ \\\\\n\\midrule\nDense & 92.0 & 85.0 & $-$7.0 \\\\\nKL-only & 85.5 & 73.5 & $-$12.0 \\\\\nSPON+KL & 87.0 & 75.5 & $-$11.5 \\\\\nBCE+comp & 81.0 & 67.0 & $-$14.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-trained prediction degrades more gracefully than BCE+compensation on both evaluations. On LongBench, the KL--BCE gap widens at long context (8.5\\% vs.\\ 13.5\\% average drop), suggesting that KL's distributional supervision provides better out-of-distribution robustness. On RULER, KL shows smaller 4K$\\rightarrow$16K degradation ($-$12.0 vs.\\ $-$14.0), with needle retrieval tasks (78.0 at 16K) degrading less than multi-key or aggregation tasks that require cross-position reasoning.\n\n% ---------------------------------------------------------------------------\n\\subsection{Instruction-Following Quality}\n\\label{sec:mtbench}\n\nTable~\\ref{tab:mtbench} reports MT-Bench scores (80 multi-turn questions, GPT-4o judge).\n\n\\begin{table}[t]\n\\centering\n\\caption{MT-Bench scores by category (GPT-4o judge).}\n\\label{tab:mtbench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & Dense & KL-only & BCE+comp & SPON+KL \\\\\n\\midrule\nWriting & 7.5 & 7.1 & 6.8 & 7.2 \\\\\nRoleplay & 7.3 & 6.9 & 6.5 & 7.0 \\\\\nReasoning & 6.8 & 6.2 & 5.8 & 6.4 \\\\\nMath & 6.5 & 5.8 & 5.3 & 6.0 \\\\\nCoding & 7.0 & 6.5 & 6.1 & 6.7 \\\\\nExtraction & 7.8 & 7.3 & 7.0 & 7.5 \\\\\nSTEM & 7.2 & 6.8 & 6.4 & 6.9 \\\\\nHumanities & 7.9 & 7.2 & 7.2 & 7.3 \\\\\n\\midrule\nAverage & 7.25 & 6.72 & 6.38 & 6.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (6.72) outperforms BCE+compensation (6.38) by 0.34 points on average, with SPON+KL reaching 6.85. Math and reasoning categories are most affected by sparsity (KL: 5.8 and 6.2), while writing and extraction are most robust (7.1 and 7.3)---consistent with the intuition that precise computation chains are more sensitive to neuron pruning than pattern-matching tasks.\n\n% ---------------------------------------------------------------------------\n\\subsection{Sparsity Scaling Analysis}\n\\label{sec:scaling}\n\nWe evaluate KL-only and BCE-only across seven sparsity levels (30--60\\%) to characterize how the KL advantage scales (Table~\\ref{tab:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Sparsity sweep: KL vs.\\ BCE PPL across sparsity levels (1 seed per level; 50\\% reuses 5-seed data).}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSparsity & KL PPL & BCE PPL & $\\Delta$(BCE$-$KL) & Quad.\\ pred. & Residual \\\\\n\\midrule\n30\\% & 6.82 & 11.32 & 4.50 & 6.67 & $-$2.17 \\\\\n35\\% & 7.28 & 14.48 & 7.20 & 9.07 & $-$1.87 \\\\\n40\\% & 7.95 & 18.95 & 11.00 & 11.90 & $-$0.90 \\\\\n45\\% & 8.58 & 23.38 & 14.80 & 15.08 & $-$0.28 \\\\\n50\\% & 9.53 & 28.16 & 18.63 & 18.71 & $-$0.08 \\\\\n55\\% & 11.20 & 36.70 & 25.50 & 22.79 & +2.71 \\\\\n60\\% & 14.05 & 49.05 & 35.00 & 27.31 & +7.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL--BCE gap grows monotonically with sparsity, consistent with the theoretical expectation that joint neuron interaction effects---captured by KL but missed by BCE---scale with the number of pruned neurons. A quadratic fit ($\\Delta \\approx 97.2 \\cdot s^2$) achieves $R^2 = 0.88$, explaining the majority of variance but with systematic residuals: sub-quadratic at low sparsity (where per-neuron independence is a less harmful approximation) and super-quadratic at high sparsity (where higher-order interaction terms become significant). We report this as a consistent empirical trend rather than a precise quantitative law.\n\n\n% ===========================================================================\n\\section{Discussion}\n\n\\paragraph{Why does KL eliminate compensation?}\nOur results suggest a mechanistic explanation. BCE trains the predictor to match per-neuron binary targets independently, producing masks where joint interaction errors accumulate---compensation networks then learn to correct these errors post-hoc. KL training, by propagating output-distribution gradients through the masking operation, allows the predictor to optimize neuron selection \\emph{jointly}. The marginal return of compensation on top of KL (0.48 PPL) versus on top of BCE (16.60 PPL) quantifies this: KL preemptively addresses the bulk of errors that compensation would otherwise need to correct.\n\n\\paragraph{Practical implications.}\nThe elimination of compensation networks simplifies the inference pipeline in two ways: (1)~264\\,MB fewer parameters to load and store, enabling deployment on memory-constrained devices; (2)~removal of per-layer GEMV operations that reduce the effective speedup from sparsity. At batch 32, this translates to 1.49$\\times$ vs.\\ 1.18$\\times$ speedup. The training cost increase (3.8 vs.\\ 0.4 GPU-hours) is modest and amortized over deployment.\n\n\\paragraph{Limitations.}\nOur study has several limitations. (1)~We evaluate on 7B--8B scale models; behavior at larger scales is unknown. (2)~The 22\\% interaction residual in SPON+KL composition limits the clean decomposition narrative. (3)~The sparsity scaling analysis ($R^2 = 0.88$) uses single seeds per level and shows systematic deviations from the quadratic model. (4)~Long-context evaluations show increased degradation (8.5--12\\% drop), suggesting the predictor's distributional robustness has limits. (5)~KL training requires a dense forward pass per step, making it ${\\sim}$80$\\times$ more expensive per step than BCE, though total training remains under 4 GPU-hours.\n\n\n% ===========================================================================\n\\section{Conclusion}\n\nWe present a systematic study of training signals for contextual SwiGLU sparsity prediction, organized around a taxonomy crossing loss coupling with correction granularity. Our central finding is that KL-divergence training eliminates the need for error compensation networks: a KL-trained predictor at 50\\% sparsity achieves 9.53 PPL on Llama~3.1~8B---surpassing BCE+compensation (11.56) with zero compensation overhead, enabling a simpler pipeline with 1.49$\\times$ batch-32 speedup and only 8\\,MB additional parameters. Composition with SPON's static correction achieves the best overall quality (8.91 PPL) with partial additivity. These findings hold across two model families, seven benchmarks, and long-context evaluations, establishing output-distribution distillation as a principled and practical training signal for activation sparsity prediction.\n\n\n% ===========================================================================\n\\appendix\n\\section{Sparsity Scaling: Detailed Fit Analysis}\n\\label{app:scaling}\n\nThe quadratic model $\\Delta(s) = a \\cdot s^2$ fitted to the KL--BCE PPL gap yields $a = 97.2$ with $R^2 = 0.88$. The systematic residual pattern (Table~\\ref{tab:scaling}) shows sub-quadratic behavior at $s \\leq 0.45$ and super-quadratic behavior at $s \\geq 0.55$. This suggests that the true relationship involves higher-order terms: at low sparsity, neuron interactions are sparse and well-captured by pairwise effects; at high sparsity, multi-neuron interaction cascades produce super-quadratic divergence. While the $R^2$ of 0.88 supports the general trend that KL advantage grows super-linearly with sparsity, we caution against interpreting the quadratic coefficient as a precise physical constant.\n\n\\section{SPON Reproduction Details}\n\\label{app:spon}\n\nSPON trains per-layer bias vectors (${\\sim}$0.5\\,MB total, 0.3 GPU-hours) to correct average activation drift via KL divergence. Our reproduction on Llama~3.1~8B achieves WikiText-2 PPL of 11.20, with QA benchmarks within $\\pm$1.2\\% of published values (Table~\\ref{tab:spon_repro}). SPON's PPL (11.20) is comparable to BCE+compensation (11.56) despite using static, input-independent correction---an observation suggesting that KL-quality training signal provides value even in the limited static-correction setting, while BCE requires contextual compensation to reach comparable performance.\n\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff6d26c7-cf29-492a-b982-9a2bb4e58cb4",
  "isSidechain": false,
  "requestId": "req_011Cb4kZntRJZMtDXeNcRxpS",
  "type": "assistant",
  "uuid": "501fdb6c-7aa9-475c-a354-d90064d98365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01762rX4oEFRwhmygCvTb5Fp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1582,
      "cache_read_input_tokens": 40058,
      "output_tokens": 10798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10798,
          "cache_read_input_tokens": 40058,
          "cache_creation_input_tokens": 1582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1582
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

_source line 19 · 2026-05-15T17:33:55.427Z_

<details><summary>↩ Tool result · `toolu_01VWr2rQ8U5vrRh3w23cSLoT`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "501fdb6c-7aa9-475c-a354-d90064d98365",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "c954211f-c589-4d1f-a2b2-2968b630ff6f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\newcommand{\\method}{KL-Sparse}\n\n\\title{Output-Distribution Distillation Eliminates Compensation Overhead\\\\for Contextual SwiGLU Sparsity Prediction}\n\n\\author{\n  Anonymous Authors\n}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based large language models enables significant inference speedups through dynamic neuron pruning, but existing approaches face a quality--efficiency trade-off: training-free heuristics leave large quality gaps, while learned BCE-trained predictors require auxiliary compensation networks adding ${\\sim}$256\\,MB of parameters and per-layer GEMV overhead. We present a systematic study of training signal and correction granularity for contextual sparsity prediction, organized around a two-dimensional taxonomy (loss coupling $\\times$ correction granularity). Our key finding is that a KL-divergence-trained contextual predictor achieves \\textbf{9.53 perplexity} on WikiText-2 at 50\\% model-level sparsity on Llama~3.1~8B---surpassing BCE+compensation (11.56) while eliminating compensation parameters entirely. This result reframes the role of compensation: output-distribution distillation during predictor training preempts the errors that compensation networks correct post-hoc. We further show that static bias correction (SPON) and contextual KL prediction compose with partial additivity (22\\% interaction residual), and that the KL advantage over BCE grows super-linearly with sparsity. Across seven benchmarks, two model families, and long-context evaluations, KL-trained prediction achieves 1.49$\\times$ batch-32 speedup with only 3.4\\% average accuracy drop and 8\\,MB overhead.\n\\end{abstract}\n\n% ===========================================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks in modern LLMs exhibit substantial contextual activation sparsity: at any given token, 40--60\\% of intermediate neurons contribute negligibly to the output. Exploiting this sparsity at inference time promises significant speedups without architectural modification. However, realizing this promise requires solving the \\emph{sparsity prediction problem}: determining which neurons to prune for each input.\n\nExisting approaches span a spectrum. \\textbf{Training-free methods} (TEAL, WINA, R-Sparse) use magnitude-based heuristics with zero training cost, but leave a 6--8 PPL gap at 50\\% sparsity. \\textbf{Static learned corrections} (SPON) train per-layer bias vectors via KL distillation to compensate average activation drift, achieving zero inference overhead but limited by input-independence. \\textbf{Contextual learned predictors} (FastForward) train per-token predictors with BCE loss against binarized activation masks, achieving near-dense quality but requiring auxiliary compensation MLPs (${\\sim}$256\\,MB) to correct prediction errors---adding parameters and per-layer GEMV operations that partially negate sparsity benefits.\n\nA fundamental question remains unexplored: \\emph{does the choice of training signal for the contextual predictor determine whether compensation is necessary?} We observe that the gradient structures of BCE and KL losses differ qualitatively. The BCE gradient $\\partial \\mathcal{L}_{\\text{BCE}}/\\partial s_j$ depends only on neuron $j$'s activation---a factorized, per-neuron signal. In contrast, the KL gradient $\\partial \\mathcal{L}_{\\text{KL}}/\\partial s_j$ couples all active neurons through $\\partial \\text{logits}/\\partial \\mathbf{h} \\cdot \\partial \\mathbf{h}/\\partial \\mathbf{m}$, propagating output-distribution-level supervision to each masking decision. This coupling allows KL-trained predictors to optimize joint neuron selection, capturing interaction effects that BCE structurally misses.\n\nWe organize prior work and our contributions in a two-dimensional taxonomy crossing \\emph{training signal coupling} (decomposed/BCE $\\rightarrow$ coupled/KL) with \\emph{correction granularity} (static $\\rightarrow$ per-token contextual), revealing an unexplored cell: per-token contextual prediction trained with coupled KL supervision.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{KL eliminates compensation overhead at quality parity.} At 50\\% sparsity, KL-only prediction (PPL 9.53) surpasses BCE+compensation (PPL 11.56) while requiring zero compensation parameters, yielding a simpler and more efficient inference pipeline (1.49$\\times$ vs.\\ 1.18$\\times$ speedup at batch 32, 8\\,MB vs.\\ 264\\,MB overhead).\n\\item \\textbf{Empirically observed partial additivity of correction mechanisms.} SPON (static) and KL (contextual) corrections compose to achieve the best overall quality (PPL 8.91), with a 22\\% interaction residual honestly characterizing their overlap.\n\\item \\textbf{Taxonomy and systematic ablation as methodological contribution.} Our two-dimensional taxonomy, four-condition ablation, iso-compute comparison, and STE baseline provide a rigorous framework for understanding sparsity prediction design choices.\n\\end{enumerate}\n\n\n% ===========================================================================\n\\section{Background and Related Work}\n\n\\paragraph{Activation sparsity in SwiGLU LLMs.}\nThe SwiGLU activation $\\text{SwiGLU}(\\mathbf{x}) = (\\mathbf{x}\\mathbf{W}_1 \\odot \\sigma(\\mathbf{x}\\mathbf{W}_g)) \\mathbf{W}_2$ produces naturally sparse intermediate representations, as the sigmoid gate $\\sigma(\\mathbf{x}\\mathbf{W}_g)$ drives many neurons toward zero. This contextual sparsity can be exploited by skipping near-zero neurons during inference, reducing FLOPs proportionally.\n\n\\paragraph{Training-free methods.}\nTEAL combines activation magnitude with greedy per-layer sparsity allocation. WINA uses weight-informed neuron scoring. R-Sparse incorporates rank-aware redundancy information. These methods require no training but achieve suboptimal quality at high sparsity levels.\n\n\\paragraph{Static learned corrections.}\nSPON trains per-layer bias vectors using KL divergence to correct average activation drift from pruning. The bias vectors add negligible parameters (${\\sim}$0.5\\,MB) and zero inference latency (fused into existing computations), but cannot adapt to per-input neuron importance variations.\n\n\\paragraph{Contextual learned predictors.}\nFastForward trains lightweight MLPs to predict per-token neuron importance using BCE loss against binarized activation targets, augmented with compensation networks that correct residual errors in the sparse hidden states. The compensation adds ${\\sim}$256\\,MB of parameters and per-layer GEMV operations.\n\n\\paragraph{Two-dimensional taxonomy.}\nWe organize these approaches along two axes (Table~\\ref{tab:taxonomy}): \\emph{training signal coupling} (how much inter-neuron information the loss gradient carries) and \\emph{correction granularity} (whether correction is input-independent or per-token). This taxonomy reveals that no prior work combines per-token contextual prediction with coupled KL training.\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of sparsity prediction methods. Our work fills the previously empty per-token contextual + coupled KL cell.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token contextual & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n% ===========================================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a pretrained SwiGLU LLM, we train a lightweight predictor $f_\\theta$ that, for each input token, produces a binary mask $\\mathbf{m} \\in \\{0,1\\}^D$ selecting which of the $D$ intermediate neurons to activate. The mask is applied element-wise: $\\tilde{\\mathbf{h}} = \\mathbf{m} \\odot \\mathbf{h}$, where $\\mathbf{h}$ is the dense intermediate representation.\n\n\\subsection{Training Signal: KL Divergence}\n\nWe train the predictor by minimizing the KL divergence between the output distributions of the dense and sparse models:\n\\begin{equation}\n\\mathcal{L}_{\\text{KL}} = \\text{KL}\\!\\left(p_{\\text{dense}}(\\cdot \\mid x) \\;\\|\\; p_{\\text{sparse}}(\\cdot \\mid x; \\theta)\\right)\n\\end{equation}\nwhere $p_{\\text{sparse}}$ denotes the model's output distribution when neurons are masked according to $f_\\theta(x)$.\n\n\\paragraph{Gradient coupling.} The key property distinguishing KL from BCE training is gradient structure. For the BCE loss, $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j$ depends only on whether neuron $j$'s predicted importance matches its binarized target---a factorized signal. For the KL loss:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\text{logits}} \\cdot \\frac{\\partial \\text{logits}}{\\partial \\mathbf{h}} \\cdot \\frac{\\partial \\mathbf{h}}{\\partial m_j} \\cdot \\frac{\\partial m_j}{\\partial s_j}\n\\end{equation}\nThe chain through $\\partial \\text{logits}/\\partial \\mathbf{h}$ couples all neurons: whether neuron $j$ should be active depends on which \\emph{other} neurons are active, because their joint contribution determines the output distribution. This coupling is a mathematical property of the gradient, not an analogy.\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\nTo enable gradient-based optimization of discrete masks, we use Gumbel-sigmoid relaxation during training:\n\\begin{equation}\n\\tilde{m}_j = \\sigma\\!\\left(\\frac{s_j + g_1 - g_2}{\\tau}\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1)\n\\end{equation}\nwhere $s_j = f_\\theta(x)_j$ is the predictor's logit for neuron $j$ and $\\tau$ is the temperature. At inference, we use hard thresholding: $m_j = \\mathbf{1}[s_j > 0]$.\n\n\\subsection{Composition with Static Correction}\n\nWe also explore composing the contextual KL predictor with SPON's static bias correction. SPON learns per-layer bias vectors $\\mathbf{b}_l$ to correct average activation drift:\n\\begin{equation}\n\\tilde{\\mathbf{h}}_l = \\mathbf{m}_l \\odot \\mathbf{h}_l + \\mathbf{b}_l\n\\end{equation}\nThe composition applies both the contextual mask (from KL predictor) and the static correction (from SPON), yielding $c = c_s + c_\\theta(x)$ where $c_s$ addresses systematic drift and $c_\\theta(x)$ adapts to per-input neuron importance.\n\n\n% ===========================================================================\n\\section{Experiments}\n\nAll experiments use 50\\% model-level sparsity unless otherwise noted. Our primary model is Llama~3.1~8B; we validate on Mistral-7B-v0.3. All learned methods are trained on a calibration set of 128 sequences (2048 tokens each) from C4. We report WikiText-2 perplexity as the primary metric, supplemented by downstream benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), long-context evaluations (LongBench, RULER), and instruction-following quality (MT-Bench with GPT-4o judge).\n\n% ---------------------------------------------------------------------------\n\\subsection{Training-Free Baselines}\n\\label{sec:baselines}\n\nTable~\\ref{tab:baselines} establishes the performance of training-free methods, motivating the need for learned predictors.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training-free baselines at 50\\% model-level sparsity (Llama 3.1 8B).}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nMethod & WikiText-2 PPL ($\\downarrow$) & $\\Delta$ vs Dense & Training Cost \\\\\n\\midrule\nDense & 6.12 & --- & --- \\\\\nTEAL & 12.50 & +6.38 & 0 \\\\\nR-Sparse & 13.50 & +7.38 & 0 \\\\\nWINA & 14.20 & +8.08 & 0 \\\\\n\\midrule\nKL-only (ref.) & 9.53 & +3.41 & 3.8\\,h \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTraining-free heuristics leave a 6--8 PPL gap versus the dense model. TEAL is the strongest baseline (12.50) owing to its greedy per-layer allocation, but all three methods substantially underperform learned predictors, establishing a clear hierarchy: training-free (12.5--14.2) $\\rightarrow$ static-learned (11.2) $\\rightarrow$ contextual-learned (9.5).\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Four-Condition Ablation: Loss $\\times$ Compensation}\n\\label{sec:ablation}\n\nOur central experiment crosses two factors: training loss (BCE vs.\\ KL) and compensation (present vs.\\ absent), yielding four conditions (Table~\\ref{tab:four_cond}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-condition ablation at 50\\% model-level sparsity (Llama 3.1 8B). KL-only achieves better quality than BCE+compensation while requiring zero compensation parameters.}\n\\label{tab:four_cond}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & WikiText-2 PPL ($\\downarrow$) & Seeds & Comp.\\ Params & Pipeline \\\\\n\\midrule\nDense (reference) & 6.12 & --- & --- & --- \\\\\nBCE-only & 28.16 $\\pm$ 0.21 & 3 & 0 & Simple \\\\\nBCE + compensation & 11.56 $\\pm$ 0.61 & 5 & 256\\,MB & Complex \\\\\nKL-only & 9.53 $\\pm$ 0.41 & 5 & 0 & Simple \\\\\nKL + compensation & 9.05 $\\pm$ 0.15 & 3 & 256\\,MB & Complex \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (9.53) outperforms BCE+compensation (11.56) by 2.03 PPL while requiring zero compensation overhead. Adding compensation to KL yields only a marginal improvement (9.53 $\\rightarrow$ 9.05, $\\Delta$ = 0.48), indicating that KL training preemptively addresses the errors compensation is designed to correct. In contrast, compensation is essential for BCE (28.16 $\\rightarrow$ 11.56, $\\Delta$ = 16.60), confirming that BCE's factorized gradient leaves substantial joint-interaction errors that require post-hoc correction.\n\n% ---------------------------------------------------------------------------\n\\subsection{Isolating Loss vs.\\ Relaxation: STE Baseline}\n\\label{sec:ste}\n\nTo disentangle the contributions of the KL loss function and the Gumbel-sigmoid relaxation, we train a predictor with KL loss but using the Straight-Through Estimator (STE) instead of Gumbel-sigmoid (Table~\\ref{tab:ste}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Loss function vs.\\ relaxation method ablation. KL contributes 72\\% of the total gain over BCE-only; Gumbel-sigmoid contributes 28\\%.}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\nCondition & Loss & Relaxation & WikiText-2 PPL & Gain over BCE-only \\\\\n\\midrule\nBCE-only & BCE & STE & 28.16 & --- \\\\\nKL + STE & KL & STE & 14.70 $\\pm$ 0.60 & 13.46 (72\\%) \\\\\nKL + Gumbel & KL & Gumbel-$\\sigma$ & 9.53 $\\pm$ 0.41 & 18.63 (100\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL + STE (14.70) already substantially outperforms BCE-only (28.16), confirming that the KL loss function---not the relaxation method---is the primary driver of improvement (72\\% of total gain). Gumbel-sigmoid contributes a meaningful additional 28\\%, as its smooth gradients enable finer-grained mask optimization at decision boundaries. Both components are necessary for optimal performance.\n\n% ---------------------------------------------------------------------------\n\\subsection{Iso-Compute Comparison}\n\\label{sec:isocompute}\n\nKL training requires a dense forward pass per step (66.0 TFLOPs/step) while BCE uses cached targets (0.8 TFLOPs/step). To ensure KL's advantage is not simply a compute artifact, we extend BCE training to 33{,}000 steps to match KL's total GPU-hours (Table~\\ref{tab:isocompute}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Iso-compute comparison. Even with equivalent total compute, BCE trails KL by ${\\sim}$14 PPL.}\n\\label{tab:isocompute}\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\nCondition & Per-step TFLOPs & Total Steps & GPU-hours & WikiText-2 PPL \\\\\n\\midrule\nKL + Gumbel & 66.0 & 1{,}000 & 3.8 & 9.53 $\\pm$ 0.41 \\\\\nBCE (standard) & 0.8 & 1{,}000 & 0.4 & 28.16 $\\pm$ 0.21 \\\\\nBCE (iso-compute) & 0.8 & 33{,}000 & 3.8 & 23.50 $\\pm$ 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nExtended BCE training reduces PPL from 28.16 to 23.50---a meaningful but insufficient improvement. The 14 PPL gap versus KL persists, confirming that BCE's information bottleneck lies in the factorized loss structure, not the training budget. Additional BCE steps improve predictor generalization but cannot capture joint neuron interactions that the loss function structurally excludes.\n\n% ---------------------------------------------------------------------------\n\\subsection{SPON Reproduction and Composition}\n\\label{sec:composition}\n\n\\paragraph{SPON reproduction.}\nWe reimplement SPON (learnable per-layer bias vectors + KL training) on Llama~3.1~8B and verify reproduction against published results (Table~\\ref{tab:spon_repro}). Our reproduction achieves WikiText-2 PPL of 11.20, within the expected range, with QA benchmark deltas within $\\pm$1.2\\% of published values.\n\n\\begin{table}[t]\n\\centering\n\\caption{SPON reproduction on Llama 3.1 8B---QA benchmark comparison at 50\\% sparsity.}\n\\label{tab:spon_repro}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nBenchmark & Dense & SPON (ours) & $\\Delta$ vs.\\ published \\\\\n\\midrule\nARC-c & 53.4\\% & 49.5\\% & +1.2\\% \\\\\nARC-e & 81.2\\% & 75.8\\% & $-$0.5\\% \\\\\nBoolQ & 83.5\\% & 78.2\\% & +0.8\\% \\\\\nPIQA & 81.0\\% & 77.5\\% & $-$1.0\\% \\\\\nWinoGrande & 74.2\\% & 69.8\\% & +0.6\\% \\\\\n\\midrule\nWikiText-2 PPL & 6.12 & 11.20 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Composition analysis.}\nWe combine SPON's static bias correction with our KL contextual predictor (Table~\\ref{tab:composition}). The composition achieves 8.91 PPL---the best overall result---but with a 22\\% interaction residual relative to a hypothetical fully additive prediction (8.23).\n\n\\begin{table}[t]\n\\centering\n\\caption{Composition additivity analysis. SPON and KL corrections compose with partial additivity; the 22\\% interaction residual reflects overlap in what each mechanism corrects.}\n\\label{tab:composition}\n\\small\n\\begin{tabular}{lcr}\n\\toprule\nCondition & WikiText-2 PPL & $\\Delta$ from TEAL \\\\\n\\midrule\nTEAL (no learned correction) & 12.50 & --- \\\\\nSPON only & 11.20 & $-$1.30 \\\\\nKL-only & 9.53 & $-$2.97 \\\\\nSPON + KL (if fully additive) & 8.23 & $-$4.27 \\\\\nSPON + KL (actual) & 8.91 $\\pm$ 0.14 & $-$3.59 \\\\\n\\midrule\nInteraction residual & --- & 0.68 (22\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe interaction arises because KL training partially learns to correct the mean drift that SPON addresses---the KL gradient pushes the predictor to minimize all correctable errors, including systematic bias. Per-layer analysis reveals that early (attention-heavy) layers show near-orthogonal corrections (cosine similarity ${\\sim}$0.10), while middle (FFN-heavy) layers show greater overlap (cosine ${\\sim}$0.25). We characterize this as \\emph{partial additivity}: the composition provides meaningful gains but should not be interpreted as clean decomposition.\n\n\n% ---------------------------------------------------------------------------\n\\subsection{Full Benchmark Evaluation}\n\\label{sec:full_eval}\n\nTable~\\ref{tab:full_bench} presents results across seven benchmarks. KL-only achieves 3.4\\% average accuracy drop versus dense, outperforming BCE+compensation (5.2\\%) and TEAL (9.8\\%). SPON+KL achieves the best quality at 2.3\\% average drop.\n\n\\begin{table}[t]\n\\centering\n\\caption{Full benchmark comparison (Llama 3.1 8B, 50\\% sparsity).}\n\\label{tab:full_bench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccccccr}\n\\toprule\nMethod & Wiki$\\downarrow$ & C4$\\downarrow$ & ARC-c$\\uparrow$ & WG$\\uparrow$ & MMLU$\\uparrow$ & GSM8K$\\uparrow$ & HE$\\uparrow$ & Avg Drop \\\\\n\\midrule\nDense & 6.12 & 8.88 & 53.4 & 74.2 & 65.3 & 48.2 & 33.5 & --- \\\\\nTEAL & 12.50 & 17.10 & 47.8 & 67.2 & 58.5 & 40.5 & 27.0 & 9.8\\% \\\\\nSPON & 11.20 & 15.50 & 49.5 & 69.8 & 60.5 & 43.0 & 28.5 & 7.0\\% \\\\\nBCE+comp & 11.56 & 15.20 & 50.2 & 70.5 & 61.8 & 44.8 & 30.5 & 5.2\\% \\\\\nKL-only & 9.53 & 12.80 & 51.5 & 72.0 & 63.0 & 46.2 & 31.5 & 3.4\\% \\\\\nSPON+KL & 8.91 & 11.90 & 52.1 & 72.8 & 63.8 & 47.0 & 32.0 & 2.3\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Inference efficiency.}\nTable~\\ref{tab:efficiency} reports wall-clock latency on an A100 GPU. At batch size 32 (compute-bound regime), KL-only achieves 1.49$\\times$ speedup versus 1.18$\\times$ for BCE+compensation---the compensation network's 256\\,MB parameters and per-layer GEMV operations consume roughly one-third of the sparsity savings. At batch size 1 (memory-bandwidth-bound), sparsity benefits are smaller across all methods.\n\n\\begin{table}[t]\n\\centering\n\\caption{Inference efficiency (A100 GPU).}\n\\label{tab:efficiency}\n\\small\n\\begin{tabular}{lccccr}\n\\toprule\nMethod & Lat.\\ $b$=1 & Speedup $b$=1 & Lat.\\ $b$=32 & Speedup $b$=32 & Extra Params \\\\\n\\midrule\nDense & 18.0\\,ms & 1.00$\\times$ & 3.20\\,ms & 1.00$\\times$ & --- \\\\\nKL-only & 16.5\\,ms & 1.09$\\times$ & 2.15\\,ms & 1.49$\\times$ & 8\\,MB \\\\\nSPON+KL & 16.5\\,ms & 1.09$\\times$ & 2.15\\,ms & 1.49$\\times$ & 8.5\\,MB \\\\\nBCE+comp & 17.8\\,ms & 1.01$\\times$ & 2.72\\,ms & 1.18$\\times$ & 264\\,MB \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ---------------------------------------------------------------------------\n\\subsection{Cross-Model Generalization}\n\\label{sec:mistral}\n\nTo verify that KL's advantage is not architecture-specific, we evaluate on Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention (Table~\\ref{tab:cross_model}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model validation at 50\\% sparsity. KL advantage direction is consistent; magnitude varies by architecture.}\n\\label{tab:cross_model}\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\nModel & Condition & Wiki PPL$\\downarrow$ & ARC-c$\\uparrow$ & MMLU$\\uparrow$ & KL--BCE gap \\\\\n\\midrule\nLlama 3.1 8B & Dense & 6.12 & 53.4 & 65.3 & --- \\\\\nLlama 3.1 8B & KL-only & 9.53 & 51.5 & 63.0 & 2.03 \\\\\nLlama 3.1 8B & BCE+comp & 11.56 & 50.2 & 61.8 & --- \\\\\n\\midrule\nMistral 7B v0.3 & Dense & 5.52 & 55.0 & 63.5 & --- \\\\\nMistral 7B v0.3 & KL-only & 9.38 & 52.8 & 61.5 & 1.07 \\\\\nMistral 7B v0.3 & BCE+comp & 10.45 & 51.5 & 60.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only consistently outperforms BCE+compensation on both architectures. The smaller gap on Mistral (1.07 vs.\\ 2.03) is expected: Mistral's GQA produces more concentrated activation patterns where BCE's per-neuron independence assumption is less harmful, and sliding window attention reduces per-token variation in neuron importance. The directional consistency across architectures supports generalizability; the magnitude variation calls for architecture-aware analysis rather than universal effect-size claims.\n\n% ---------------------------------------------------------------------------\n\\subsection{Long-Context Evaluation}\n\\label{sec:longcontext}\n\nWe evaluate on LongBench (English subset, 4K--32K tokens) and RULER (synthetic tasks at 4K and 16K) to test predictor generalization beyond training sequence length (2048 tokens).\n\n\\begin{table}[t]\n\\centering\n\\caption{LongBench performance (English subset). KL-only maintains lower degradation than BCE+compensation, with SPON+KL achieving the smallest average drop.}\n\\label{tab:longbench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccccr}\n\\toprule\nMethod & S-QA & M-QA & Summ. & Few-shot & Code & Avg & Drop \\\\\n\\midrule\nDense & 42.5 & 36.0 & 27.2 & 60.0 & 34.0 & 39.9 & --- \\\\\nTEAL & 34.0 & 27.5 & 23.0 & 48.5 & 24.5 & 31.5 & 21.1\\% \\\\\nBCE+comp & 36.5 & 30.0 & 24.2 & 53.5 & 28.5 & 34.5 & 13.5\\% \\\\\nKL-only & 38.8 & 32.2 & 25.5 & 55.8 & 30.2 & 36.5 & 8.5\\% \\\\\nSPON+KL & 39.5 & 33.0 & 25.8 & 56.5 & 31.0 & 37.2 & 6.8\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{RULER evaluation at 4K and 16K context lengths.}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{lccr}\n\\toprule\nMethod & 4K Avg & 16K Avg & 4K$\\rightarrow$16K $\\Delta$ \\\\\n\\midrule\nDense & 92.0 & 85.0 & $-$7.0 \\\\\nKL-only & 85.5 & 73.5 & $-$12.0 \\\\\nSPON+KL & 87.0 & 75.5 & $-$11.5 \\\\\nBCE+comp & 81.0 & 67.0 & $-$14.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-trained prediction degrades more gracefully than BCE+compensation on both evaluations. On LongBench, the KL--BCE gap widens at long context (8.5\\% vs.\\ 13.5\\% average drop), suggesting that KL's distributional supervision provides better out-of-distribution robustness. On RULER, KL shows smaller 4K$\\rightarrow$16K degradation ($-$12.0 vs.\\ $-$14.0), with needle retrieval tasks (78.0 at 16K) degrading less than multi-key or aggregation tasks that require cross-position reasoning.\n\n% ---------------------------------------------------------------------------\n\\subsection{Instruction-Following Quality}\n\\label{sec:mtbench}\n\nTable~\\ref{tab:mtbench} reports MT-Bench scores (80 multi-turn questions, GPT-4o judge).\n\n\\begin{table}[t]\n\\centering\n\\caption{MT-Bench scores by category (GPT-4o judge).}\n\\label{tab:mtbench}\n\\small\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lcccc}\n\\toprule\nCategory & Dense & KL-only & BCE+comp & SPON+KL \\\\\n\\midrule\nWriting & 7.5 & 7.1 & 6.8 & 7.2 \\\\\nRoleplay & 7.3 & 6.9 & 6.5 & 7.0 \\\\\nReasoning & 6.8 & 6.2 & 5.8 & 6.4 \\\\\nMath & 6.5 & 5.8 & 5.3 & 6.0 \\\\\nCoding & 7.0 & 6.5 & 6.1 & 6.7 \\\\\nExtraction & 7.8 & 7.3 & 7.0 & 7.5 \\\\\nSTEM & 7.2 & 6.8 & 6.4 & 6.9 \\\\\nHumanities & 7.9 & 7.2 & 7.2 & 7.3 \\\\\n\\midrule\nAverage & 7.25 & 6.72 & 6.38 & 6.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nKL-only (6.72) outperforms BCE+compensation (6.38) by 0.34 points on average, with SPON+KL reaching 6.85. Math and reasoning categories are most affected by sparsity (KL: 5.8 and 6.2), while writing and extraction are most robust (7.1 and 7.3)---consistent with the intuition that precise computation chains are more sensitive to neuron pruning than pattern-matching tasks.\n\n% ---------------------------------------------------------------------------\n\\subsection{Sparsity Scaling Analysis}\n\\label{sec:scaling}\n\nWe evaluate KL-only and BCE-only across seven sparsity levels (30--60\\%) to characterize how the KL advantage scales (Table~\\ref{tab:scaling}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Sparsity sweep: KL vs.\\ BCE PPL across sparsity levels (1 seed per level; 50\\% reuses 5-seed data).}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{cccccc}\n\\toprule\nSparsity & KL PPL & BCE PPL & $\\Delta$(BCE$-$KL) & Quad.\\ pred. & Residual \\\\\n\\midrule\n30\\% & 6.82 & 11.32 & 4.50 & 6.67 & $-$2.17 \\\\\n35\\% & 7.28 & 14.48 & 7.20 & 9.07 & $-$1.87 \\\\\n40\\% & 7.95 & 18.95 & 11.00 & 11.90 & $-$0.90 \\\\\n45\\% & 8.58 & 23.38 & 14.80 & 15.08 & $-$0.28 \\\\\n50\\% & 9.53 & 28.16 & 18.63 & 18.71 & $-$0.08 \\\\\n55\\% & 11.20 & 36.70 & 25.50 & 22.79 & +2.71 \\\\\n60\\% & 14.05 & 49.05 & 35.00 & 27.31 & +7.69 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL--BCE gap grows monotonically with sparsity, consistent with the theoretical expectation that joint neuron interaction effects---captured by KL but missed by BCE---scale with the number of pruned neurons. A quadratic fit ($\\Delta \\approx 97.2 \\cdot s^2$) achieves $R^2 = 0.88$, explaining the majority of variance but with systematic residuals: sub-quadratic at low sparsity (where per-neuron independence is a less harmful approximation) and super-quadratic at high sparsity (where higher-order interaction terms become significant). We report this as a consistent empirical trend rather than a precise quantitative law.\n\n\n% ===========================================================================\n\\section{Discussion}\n\n\\paragraph{Why does KL eliminate compensation?}\nOur results suggest a mechanistic explanation. BCE trains the predictor to match per-neuron binary targets independently, producing masks where joint interaction errors accumulate---compensation networks then learn to correct these errors post-hoc. KL training, by propagating output-distribution gradients through the masking operation, allows the predictor to optimize neuron selection \\emph{jointly}. The marginal return of compensation on top of KL (0.48 PPL) versus on top of BCE (16.60 PPL) quantifies this: KL preemptively addresses the bulk of errors that compensation would otherwise need to correct.\n\n\\paragraph{Practical implications.}\nThe elimination of compensation networks simplifies the inference pipeline in two ways: (1)~264\\,MB fewer parameters to load and store, enabling deployment on memory-constrained devices; (2)~removal of per-layer GEMV operations that reduce the effective speedup from sparsity. At batch 32, this translates to 1.49$\\times$ vs.\\ 1.18$\\times$ speedup. The training cost increase (3.8 vs.\\ 0.4 GPU-hours) is modest and amortized over deployment.\n\n\\paragraph{Limitations.}\nOur study has several limitations. (1)~We evaluate on 7B--8B scale models; behavior at larger scales is unknown. (2)~The 22\\% interaction residual in SPON+KL composition limits the clean decomposition narrative. (3)~The sparsity scaling analysis ($R^2 = 0.88$) uses single seeds per level and shows systematic deviations from the quadratic model. (4)~Long-context evaluations show increased degradation (8.5--12\\% drop), suggesting the predictor's distributional robustness has limits. (5)~KL training requires a dense forward pass per step, making it ${\\sim}$80$\\times$ more expensive per step than BCE, though total training remains under 4 GPU-hours.\n\n\n% ===========================================================================\n\\section{Conclusion}\n\nWe present a systematic study of training signals for contextual SwiGLU sparsity prediction, organized around a taxonomy crossing loss coupling with correction granularity. Our central finding is that KL-divergence training eliminates the need for error compensation networks: a KL-trained predictor at 50\\% sparsity achieves 9.53 PPL on Llama~3.1~8B---surpassing BCE+compensation (11.56) with zero compensation overhead, enabling a simpler pipeline with 1.49$\\times$ batch-32 speedup and only 8\\,MB additional parameters. Composition with SPON's static correction achieves the best overall quality (8.91 PPL) with partial additivity. These findings hold across two model families, seven benchmarks, and long-context evaluations, establishing output-distribution distillation as a principled and practical training signal for activation sparsity prediction.\n\n\n% ===========================================================================\n\\appendix\n\\section{Sparsity Scaling: Detailed Fit Analysis}\n\\label{app:scaling}\n\nThe quadratic model $\\Delta(s) = a \\cdot s^2$ fitted to the KL--BCE PPL gap yields $a = 97.2$ with $R^2 = 0.88$. The systematic residual pattern (Table~\\ref{tab:scaling}) shows sub-quadratic behavior at $s \\leq 0.45$ and super-quadratic behavior at $s \\geq 0.55$. This suggests that the true relationship involves higher-order terms: at low sparsity, neuron interactions are sparse and well-captured by pairwise effects; at high sparsity, multi-neuron interaction cascades produce super-quadratic divergence. While the $R^2$ of 0.88 supports the general trend that KL advantage grows super-linearly with sparsity, we caution against interpreting the quadratic coefficient as a precise physical constant.\n\n\\section{SPON Reproduction Details}\n\\label{app:spon}\n\nSPON trains per-layer bias vectors (${\\sim}$0.5\\,MB total, 0.3 GPU-hours) to correct average activation drift via KL divergence. Our reproduction on Llama~3.1~8B achieves WikiText-2 PPL of 11.20, with QA benchmarks within $\\pm$1.2\\% of published values (Table~\\ref{tab:spon_repro}). SPON's PPL (11.20) is comparable to BCE+compensation (11.56) despite using static, input-independent correction---an observation suggesting that KL-quality training signal provides value even in the limited static-correction setting, while BCE requires contextual compensation to reach comparable performance.\n\n\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "501fdb6c-7aa9-475c-a354-d90064d98365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "c954211f-c589-4d1f-a2b2-2968b630ff6f",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260515T164925",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Tool call

_source line 22 · 2026-05-15T17:33:59.096Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EgTHyG2Br92yvxiWugMEPz`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c954211f-c589-4d1f-a2b2-2968b630ff6f",
  "isSidechain": false,
  "requestId": "req_011Cb4kpD94znnMAeyFDm6WD",
  "type": "assistant",
  "uuid": "c9adc9df-bcd5-4ccc-b602-d76ffd2d6c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ETFRztBnrWdHywLW2cvdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10866,
      "cache_read_input_tokens": 41640,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 41640,
          "cache_creation_input_tokens": 10866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10866
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

_source line 23 · 2026-05-15T17:34:07.229Z_

<details><summary>↩ Tool result · `toolu_01EgTHyG2Br92yvxiWugMEPz`</summary>

```text
&lt;persisted-output>
Output too large (48.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/e4efbda2-19e3-49b7-bacb-45a8e0db6a48/tool-results/bpvbrkmgq.txt

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9adc9df-bcd5-4ccc-b602-d76ffd2d6c97",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "e20dd15c-5367-4697-b577-694be9654d63",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (19.01051pt too wide) in paragraph at lines 47--48\n[]\\T1/cmr/bx/n/10.95 Taxonomy and sys-tem-atic ab-la-tion as method-olog-i-cal \ncon-tri-bu-tion. \\T1/cmr/m/n/10.95 Our two-dimensional\n\nLaTeX Warning: Reference `tab:taxonomy' on page 2 undefined on input line 67.\n\n[2] [3]\nOverfull \\hbox (21.22958pt too wide) in paragraph at lines 127--128\n\\T1/cmr/m/n/10.95 All ex-per-i-ments use 50% model-level spar-sity un-less oth-\ner-wise noted. Our pri-mary model is Llama 3.1 8B;\n\nLaTeX Warning: Reference `tab:baselines' on page 4 undefined on input line 133.\n\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 158.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 158.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 158.\n\n\nLaTeX Warning: Reference `tab:four_cond' on page 4 undefined on input line 161.\n\n\n[4]\n\nLaTeX Warning: Reference `tab:ste' on page 5 undefined on input line 187.\n\n\nLaTeX Warning: Reference `tab:isocompute' on page 5 undefined on input line 211\n.\n\n\nLaTeX Warning: Reference `tab:spon_repro' on page 5 undefined on input line 236\n.\n\n\nLaTeX Warning: Reference `tab:composition' on page 5 undefined on input line 25\n9.\n\n[5]\n\nLaTeX Warning: Reference `tab:full_bench' on page 6 undefined on input line 288\n.\n\n\nLaTeX Warning: Reference `tab:efficiency' on page 6 undefined on input line 311\n.\n\n\nLaTeX Warning: Reference `tab:cross_model' on page 6 undefined on input line 33\n4.\n\n[6]\n\nLaTeX Warning: Reference `tab:mtbench' on page 7 undefined on input line 406.\n\n\nOverfull \\hbox (7.83597pt too wide) in paragraph at lines 432--433\n[]\\T1/cmr/m/n/10.95 KL-only (6.72) out-per-forms BCE+compensation (6.38) by 0.3\n4 points on av-er-age, with SPON+KL\n\nLaTeX Warning: Reference `tab:scaling' on page 7 undefined on input line 438.\n\n[7]\nOverfull \\hbox (7.44386pt too wide) in paragraph at lines 470--471\n []\\T1/cmr/bx/n/10.95 Practical im-pli-ca-tions.[] \\T1/cmr/m/n/10.95 The elim-i\n-na-tion of com-pen-sa-tion net-works sim-pli-fies the in-fer-ence pipeline\n[8]\n\nLaTeX Warning: Reference `tab:scaling' on page 9 undefined on input line 487.\n\n\nLaTeX Warning: Reference `tab:spon_repro' on page 9 undefined on input line 492\n.\n\n[9]\nNo file paper.bbl.\n[10] (./paper.aux)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1200.tfm.\nOutput written on ecbx1200.600gf (256 characters, 59220 bytes).\nTranscript written on ecbx1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecbx1095.tfm.\nOutput written on ecbx1095.600gf (256 characters, 54848 bytes).\nTranscript written on ecbx1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06808pt)\nFont metrics written on ecti1095.tfm.\nOutput written on ecti1095.600gf (256 characters, 57920 bytes).\nTranscript written on ecti1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.07599pt)\nFont metrics written on ecrm1095.tfm.\nOutput written on ecrm1095.600gf (256 characters, 55424 bytes).\nTranscript written on ecrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecbx1440\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecbx1440\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx1440.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecbx.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.10997pt)\nFont metrics written on ecbx1440.tfm.\nOutput written on ecbx1440.600gf (256 characters, 70764 bytes).\nTranscript written on ecbx1440.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk: successfully generated.\n &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42]",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/e4efbda2-19e3-49b7-bacb-45a8e0db6a48/tool-results/bpvbrkmgq.txt",
    "persistedOutputSize": 49634
  },
  "sourceToolAssistantUUID": "c9adc9df-bcd5-4ccc-b602-d76ffd2d6c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "e20dd15c-5367-4697-b577-694be9654d63",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260515T164925",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Tool call

_source line 26 · 2026-05-15T17:34:13.007Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016Xf73jTGCMKWkFT1nojLk3`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.pdf 2>/dev/null && echo \"PDF OK\" || echo \"PDF MISSING\"",
  "description": "Verify PDF was generated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e20dd15c-5367-4697-b577-694be9654d63",
  "isSidechain": false,
  "requestId": "req_011Cb4kq5o5UQCeWh53CsyjP",
  "type": "assistant",
  "uuid": "6015a580-8533-4408-867a-24a79eea1216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013y9PLKxeDNdNerPmSiY9gk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 52506,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 52506,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1189
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

_source line 27 · 2026-05-15T17:34:13.109Z_

<details><summary>↩ Tool result · `toolu_016Xf73jTGCMKWkFT1nojLk3`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 219741 May 15 17:34 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.pdf
PDF OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6015a580-8533-4408-867a-24a79eea1216",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "11ad0b7e-4e91-457d-91c4-1831f656ba0e",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 219741 May 15 17:34 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.pdf\nPDF OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6015a580-8533-4408-867a-24a79eea1216",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T17:34:16.644Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JD4SEyRyCKYUz3PRcaZKWy`</summary>

```json
{
  "command": "grep -c \"Warning\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.log | head -1; grep \"Error\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.log | head -5",
  "description": "Check for LaTeX errors/warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ad0b7e-4e91-457d-91c4-1831f656ba0e",
  "isSidechain": false,
  "requestId": "req_011Cb4kqWnjXe4br2cHKbbxr",
  "type": "assistant",
  "uuid": "3f4c191c-8aa0-4fe4-b87b-53bceeccc597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186CRAfL1gPHzdMdU7KTGzr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 53695,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 53695,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 29 · 2026-05-15T17:34:16.740Z_

<details><summary>↩ Tool result · `toolu_01JD4SEyRyCKYUz3PRcaZKWy`</summary>

```text
3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f4c191c-8aa0-4fe4-b87b-53bceeccc597",
  "isSidechain": false,
  "promptId": "c6ba93f8-5126-4fea-95a6-3bc7cba82894",
  "type": "user",
  "uuid": "5b75dbea-fe1e-4702-9525-18822e49e48e",
  "toolUseResult": {
    "stdout": "3",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3f4c191c-8aa0-4fe4-b87b-53bceeccc597",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T17:34:26.096Z_

PDF 编译成功（219KB，仅 3 个 warning，无 error）。

论文已写入 `paper.tex` 并编译为 `paper.pdf`，覆盖全部 11 个实验：

| 实验 | 对应位置 |
|---|---|
| Four-condition ablation | Table 2 (§4.2) |
| STE baseline | Table 3 (§4.3) |
| Iso-compute BCE | Table 4 (§4.4) |
| SPON reproduction | Table 5 (§4.5) |
| SPON+KL composition | Table 6 (§4.5) |
| Training-free baselines | Table 1 (§4.1) |
| Full benchmark + efficiency | Tables 7-8 (§4.6) |
| Sparsity sweep | Table 9 (§4.7) |
| Mistral generalization | Table 10 (§4.8) |
| LongBench + RULER | Tables 11-12 (§4.8) |
| MT-Bench | Table 13 (§4.9) |

核心 narrative 按 guidance 调整：Claim 1 → "KL eliminates compensation overhead at quality parity"；Claim 2 → "partial additivity" with 22% residual honest报告；Claim 3 → appendix-level empirical trend。重心放在 taxonomy + systematic ablation 的方法论贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b75dbea-fe1e-4702-9525-18822e49e48e",
  "isSidechain": false,
  "requestId": "req_011Cb4kqnU4T7CAuHWkBuVYe",
  "type": "assistant",
  "uuid": "ddf79cad-9b44-446b-87ca-9d3af36513bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jv8RbXeYCnnWB96vyAqYvb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 53931,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 208,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 53931,
          "cache_creation_input_tokens": 208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 208
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T164925 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "ddf79cad-9b44-446b-87ca-9d3af36513bf",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream_20260515T164925",
  "sessionId": "e4efbda2-19e3-49b7-bacb-45a8e0db6a48"
}
```

---
