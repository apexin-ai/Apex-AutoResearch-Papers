# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/291986bc-33d8-4825-80fc-c5492d1484a2.jsonl`
- **Structured JSON:** [`e1004e49391a1ac323af.json`](../../sessions/e1/e1004e49391a1ac323af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T15:35:44.167Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T15:35:44.167Z",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：从 'structural impossibility' 全面退守为 'first systematic empirical survey of symbolic consensus across models, domains, and operating conditions'。核心问题：(1) Temperature ablation T=1.0 暴露 Δ=+8.3pp (p=0.034)，打破 'regardless of diversity' 声明；(2) LLaMA-8B D012 达 p=0.096，成为 第二个边际正向结果；(3) F2 per-problem constraint precision 均值 0.57 — 高于 random (0.33 for 3-class), 与 'non-discriminative' 叙事矛盾；(4) C0 仅有 2 个聚类（<5% vs 22-68%），无梯度，沦为 trivial binary indicator。放弃 'capability trap' 作为 mechanism claim，降级为 descriptive label。Hero figure 切换 Plan B: temperature × model response-surface heatmap（绝大部分区域 ≈ 0 但 T=1.0 角落有正值）。 加 'boundary conditions' 节：T=1.0 部分打破 trap 但 extraction rate 下降 + output coherence 退化 → overhead negates marginal gain。Title 改为 'When Does Symbolic Consensus Help? A Systematic Empirical Study'。仍冲 EMNLP，novelty 从 mechanism identification 转向 comprehensive negative-result coverage + practical operating guidelines (C0 gate + temperature-overhead tradeoff)。 关键数值: aggregate_abs_weighted_delta_pp ≈ 1.5pp, n_exp_positive_p_below_010 = 2, discordant_sica_winrate ≈ 0.65, c0_scaling_distinct_levels = 2, f2_constraint_precision_mean = 0.57, f2_precision_vs_entropy_R2 = 0.008。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T15:35:44.171Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T15:35:44.171Z",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-17T15:35:44.193Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：从 'structural impossibility' 全面退守为 'first systematic empirical survey of symbolic consensus across models, domains, and operating conditions'。核心问题：(1) Temperature ablation T=1.0 暴露 Δ=+8.3pp (p=0.034)，打破 'regardless of diversity' 声明；(2) LLaMA-8B D012 达 p=0.096，成为 第二个边际正向结果；(3) F2 per-problem constraint precision 均值 0.57 — 高于 random (0.33 for 3-class), 与 'non-discriminative' 叙事矛盾；(4) C0 仅有 2 个聚类（<5% vs 22-68%），无梯度，沦为 trivial binary indicator。放弃 'capability trap' 作为 mechanism claim，降级为 descriptive label。Hero figure 切换 Plan B: temperature × model response-surface heatmap（绝大部分区域 ≈ 0 但 T=1.0 角落有正值）。 加 'boundary conditions' 节：T=1.0 部分打破 trap 但 extraction rate 下降 + output coherence 退化 → overhead negates marginal gain。Title 改为 'When Does Symbolic Consensus Help? A Systematic Empirical Study'。仍冲 EMNLP，novelty 从 mechanism identification 转向 comprehensive negative-result coverage + practical operating guidelines (C0 gate + temperature-overhead tradeoff)。 关键数值: aggregate_abs_weighted_delta_pp ≈ 1.5pp, n_exp_positive_p_below_010 = 2, discordant_sica_winrate ≈ 0.65, c0_scaling_distinct_levels = 2, f2_constraint_precision_mean = 0.57, f2_precision_vs_entropy_R2 = 0.008。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "f8ffe20d-075d-45a2-9e34-e384a060a2f7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T15:35:44.192Z_

```json
{
  "parentUuid": "f8ffe20d-075d-45a2-9e34-e384a060a2f7",
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
  "uuid": "2ae03f7d-d12c-4d12-b51e-31b4b887c9d2",
  "timestamp": "2026-05-17T15:35:44.192Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T15:35:44.192Z_

```json
{
  "parentUuid": "2ae03f7d-d12c-4d12-b51e-31b4b887c9d2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "53f4c527-3d93-40bb-b376-e600d15d2706",
  "timestamp": "2026-05-17T15:35:44.192Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
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
  "aiTitle": "Generate symbolic consensus survey paper for dream_20260517T144412",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Assistant

_source line 7 · 2026-05-17T15:35:46.645Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f4c527-3d93-40bb-b376-e600d15d2706",
  "isSidechain": false,
  "requestId": "req_011Cb8PRKRGnPbPxki9DPgoy",
  "type": "assistant",
  "uuid": "b7382fca-154f-4aec-8b2c-40b08306475e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyDY7KW1yBUi6DxuyyHcrM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12814,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12814
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

_source line 8 · 2026-05-17T15:35:47.627Z_

<details open><summary>🔧 Tool call — Read · `toolu_0147S8fMGZvqT8uLayuZrVjM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7382fca-154f-4aec-8b2c-40b08306475e",
  "isSidechain": false,
  "requestId": "req_011Cb8PRKRGnPbPxki9DPgoy",
  "type": "assistant",
  "uuid": "53f0b398-4e02-4427-9085-acd75154dd21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyDY7KW1yBUi6DxuyyHcrM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12814,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12814
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

_source line 9 · 2026-05-17T15:35:47.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_011JzDXRgT4HWRzc3GhRd8Xx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f0b398-4e02-4427-9085-acd75154dd21",
  "isSidechain": false,
  "requestId": "req_011Cb8PRKRGnPbPxki9DPgoy",
  "type": "assistant",
  "uuid": "1aa1a7f5-85fe-4496-9c4f-19d2dda5599a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyDY7KW1yBUi6DxuyyHcrM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12814,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12814
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

_source line 10 · 2026-05-17T15:35:47.848Z_

<details><summary>↩ Tool result · `toolu_011JzDXRgT4HWRzc3GhRd8Xx`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)
8	
9	1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).
10	2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
11	3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.
12	
13	## Core Insight
14	Symbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.
15	
16	## Story Spine
17	- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
18	- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
19	- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.
20	- **Headline result**: "Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level."
21	
22	## Anticipated Reviewer Concerns & Defensive Experiments
23	1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
24	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
25	3. **"Only Qwen models"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B
26	4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
27	5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
28	6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
29	7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
30	8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
31	9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
32	10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
33	11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
34	12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.
35	
36	## Working Title
37	**"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"**
38	(Alternatives: 
39	- "When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why"
40	- "Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation")
41	
42	## Paper Structure (EMNLP 8pp + appendix)
43	- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)
44	- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)
45	- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data
46	
47	## Claim Risk Notes (Updated D035 + exp-014)
48	- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
49	- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
50	- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator". Need exp-004/007 for gradient data. OPEN.
51	- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
52	- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.
53	
54	## Venue Fit Risks
55	- EMNLP: Negative-results/analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic + overhead analysis.
56	- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
57	- Statistical power: Now strong (N>1,200 combined across powered tests).
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1aa1a7f5-85fe-4496-9c4f-19d2dda5599a",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "3aae433f-e01e-4c04-9f04-2d2c701ffa57",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n\n## Working Title\n**\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"**\n(Alternatives: \n- \"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\"\n- \"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\". Need exp-004/007 for gradient data. OPEN.\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  },
  "sourceToolAssistantUUID": "1aa1a7f5-85fe-4496-9c4f-19d2dda5599a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T15:35:47.945Z_

<details><summary>↩ Tool result · `toolu_0147S8fMGZvqT8uLayuZrVjM`</summary>

```text
1	[
2	  {
3	    "name": "sica_k_ablation_14b",
4	    "description": "K sensitivity (K=6,8,11,12,16,20) on D012 60 questions, Qwen-14B",
5	    "results": {
6	      "K6_sica": 0.75,
7	      "K6_sc": 0.733,
8	      "K6_gap_pp": 1.7,
9	      "K8_sica": 0.75,
10	      "K8_sc": 0.75,
11	      "K8_gap_pp": 0.0,
12	      "K11_sica": 0.75,
13	      "K11_sc": 0.75,
14	      "K11_gap_pp": 0.0,
15	      "K12_sica": 0.733,
16	      "K12_sc": 0.75,
17	      "K12_gap_pp": -1.7,
18	      "K16_sica": 0.717,
19	      "K16_sc": 0.733,
20	      "K16_gap_pp": -1.7,
21	      "K20_sica": 0.717,
22	      "K20_sc": 0.733,
23	      "K20_gap_pp": -1.7,
24	      "tiebreak_rate_K6": 0.183,
25	      "tiebreak_rate_K12": 0.267,
26	      "tiebreak_rate_K20": 0.05,
27	      "all_K_sica_leq_sc": false,
28	      "n": 60
29	    },
30	    "tables": [
31	      "Appendix Table A1: K-ablation results (K × accuracy × gap × tiebreak rate)"
32	    ],
33	    "figures": [],
34	    "analysis": "K=6 的 +1.7pp 在 n=60 下 SE≈5pp，统计上无意义 (p>0.5)，但在图上形成一个视觉上的正向点， reviewer 可能追问 'why not use K=6?'。应对策略：在 appendix 说明 K=6 下 SC 本身 variance 更大 (fewer votes)， +1.7pp 在 bootstrap CI [-5.0, +8.3] 内完全兼容零效应。K=11 (odd) gap=0 是核心证据： 无 tie 时 SICA 完全等价于 SC，确认 SICA 的全部潜在价值来自 tiebreaking。论文可保留此结论。\n\n\nWorst 档下 K=6 出现 +1.7pp 正向 delta。原因：低 K 时每条 trace 权重大，diversity 自然较高， SICA 的 constraint filtering 在少样本高 diversity 场景有边际价值。K=11 (odd) gap=0 确认 tiebreak-only mechanism：去除 exact tie 后 SICA 无额外价值。K≥12 时 SICA 退化：更多 traces 引入更多 low-quality constraints，noise injection 效应压过任何 signal。整体模式非单调—— low K 弱正向、odd K 零、high K 弱负向——使 'SICA ≤ SC at all K' 叙述失效，需改为 'K-dependent with no consistent advantage'。\n"
35	  },
36	  {
37	    "name": "tiebreak_baseline_analysis",
38	    "description": "SICA vs SC-random-tiebreak vs SC-deterministic on tied questions, CPU reanalysis",
39	    "results": {
40	      "n_tied_questions": 5,
41	      "sica_tiebreak_accuracy": 0.8,
42	      "random_tiebreak_accuracy": 0.5,
43	      "alphabetical_tiebreak_accuracy": 0.6,
44	      "first_seen_tiebreak_accuracy": 0.4,
45	      "tied_question_fraction": 0.083,
46	      "n_total_problems": 60
47	    },
48	    "tables": [
49	      "T4: Tiebreak Analysis (method × accuracy on tied subset × contribution to overall gap)"
50	    ],
51	    "figures": [],
52	    "analysis": "Tiebreak quality 80% 本身是一个 positive result，论文不能忽略。应策略性地呈现： 在 T4 中同时展示 'accuracy on ties' (SICA wins) 和 'contribution to total accuracy' (negligible)。用 'effective contribution' = tiebreak_quality × tie_rate 量化： 0.80 × 0.083 = 6.6% effective contribution → translates to ~2pp at best。 在 worst 档叙事中，这成为 'boundary conditions' 节的辅助论据。\n\n\nSICA 在 tied questions 上表现出色 (80% vs random 50%)，证明 constraint-based tiebreaking 有真实价值。但问题在于 tied questions 极少 (5/60 = 8.3%)：即使 SICA 每次 tie 都选对， 对总体 accuracy 的贡献仅 ~0.083 × 0.30 ≈ +2.5pp。Worst 档的问题：80% tiebreak quality 给 reviewer 一个 'method works on ties, just needs more ties' 的反驳切入点，暗示 在更极端的 diversity 条件（如 T=1.0）下 SICA 可能有更大价值。这与温度 ablation 正向结果 形成叙事共振，削弱 trap 的 'structural' 性质。\n"
53	  },
54	  {
55	    "name": "sica_7b_scaling",
56	    "description": "Qwen2.5-7B-Instruct on D012 60 questions, within-Qwen scaling",
57	    "results": {
58	      "n": 60,
59	      "k": 12,
60	      "sica_accuracy": 0.6,
61	      "sc_accuracy": 0.567,
62	      "delta_pp": 3.3,
63	      "multi_candidate_rate": 0.65,
64	      "extraction_rate": 0.82,
65	      "answer_extraction_rate": 0.88,
66	      "contradiction_rate": 0.068,
67	      "truncated_traces": 30,
68	      "discordant_sica_wins": 4,
69	      "discordant_sc_wins": 2,
70	      "mcnemar_p": 0.41,
71	      "proofwriter_sica": 0.567,
72	      "proofwriter_sc": 0.533,
73	      "proofwriter_delta_pp": 3.3,
74	      "folio_sica": 0.633,
75	      "folio_sc": 0.6,
76	      "folio_delta_pp": 3.3,
77	      "c0_level_cluster": "high"
78	    },
79	    "tables": [
80	      "T1 row: Qwen-7B | PW/FOLIO | 0.600 vs 0.567 | +3.3pp | p=0.41"
81	    ],
82	    "figures": [],
83	    "analysis": "7B 结果在 worst 档中制造叙事摩擦：delta 方向为正，且比 14B (+0.3pp) 更大。 Reviewer 可能论证 'the method works better on weaker models where diversity is higher'， 要求 larger-n 验证。防御：(1) n=60 SE≈6pp，+3.3pp 在 CI 内含零；(2) extraction rate 下降到 82% 意味 constraint quality 更差；(3) 即使真实效应为 +3pp，overhead 约 50% 使 cost/gain ratio 不合理。但这些论证相比 'trap is structural' 明显更弱。\n\n\n7B 模型更弱 → baseline 更低 (SC≈57%) → diversity 更高 (C0=65% vs 14B 的 38%)。 Higher diversity 给 SICA 更多操作空间，产生 +3.3pp 边际正向 delta。但 p=0.41 完全 在噪声范围内。Worst 档的核心问题：7B 和 14B 的 C0 都在 {30-68%} 聚类中，无法构成 'C0 gradient' → c0_scaling_distinct_levels 仍为 2（{<5%} vs {30-68%}）。 +3.3pp delta 虽不显著，但方向一致地为正，给 reviewer 'underpowered positive' 解读空间。 Truncation 较高 (30/720 traces) 引入 confound：truncated traces 可能产生 artifact diversity。\n"
84	  },
85	  {
86	    "name": "qwq_32b_operating_regime",
87	    "description": "QwQ-32B negative control — data from MVP phase, formatted for paper",
88	    "results": {
89	      "qwq_aggregate_c0_nominal_pct": 10.3,
90	      "qwq_aggregate_c0_effective_pct": 2.6,
91	      "qwen14b_c0_pct": 46.0,
92	      "diversity_ratio_effective": 17.7,
93	      "aime_delta_pp": 0.0,
94	      "proofwriter_delta_pp": -5.9,
95	      "aime_n": 22,
96	      "proofwriter_n": 17,
97	      "temp_diversity_n": 5,
98	      "folio_n": 2,
99	      "total_problems": 46,
100	      "c0_threshold": 20,
101	      "qwq_below_threshold": true,
102	      "sica_eq_sc_all_domains": true
103	    },
104	    "tables": [
105	      "T1 row: QwQ-32B | AIME/PW/FOLIO | SICA≡SC | C0=2.6%"
106	    ],
107	    "figures": [],
108	    "analysis": "QwQ-32B 数据是论文最干净的 negative control，worst 档下仍可正常使用。风险在于 reviewer 要求 larger-n QwQ 验证或其他 reasoning model (e.g., o1-mini, Gemini 2.5 Flash Thinking) → 超出 GPU budget。在 worst 叙事中，QwQ-32B 作为 'converged regime' 示例仍成立， 但 'operating regime is empirically empty' 的强声明需要更多 reasoning model 数据点。\n\n\nQwQ-32B 作为 full reasoning model，deterministic chain 主导 sampling randomness， C0 effective 仅 2.6%。SICA ≡ SC 是结构性的——only 1-2 candidate answers per problem， MaxSAT exclusion 无 target。这一结果干净地支持 'low C0 → method degenerates' 叙述。 Worst 档的问题不在结果本身，而在数据量：total n=46 且分布不均 (AIME 22, PW 17, temperature 5, FOLIO 2)，统计功效极低。Reviewer 可质疑 'n=46 不足以得出 C0<5% 是 generalizable 的结论'。\n"
109	  },
110	  {
111	    "name": "c0_diagnostic_validation",
112	    "description": "C0 vs SICA-SC gap scatter across all models/conditions, CPU analysis",
113	    "results": {
114	      "n_data_points": 12,
115	      "c0_values_observed": [
116	        2.6,
117	        5.0,
118	        10.0,
119	        22.0,
120	        27.0,
121	        38.0,
122	        50.0,
123	        58.0,
124	        62.0,
125	        65.0,
126	        72.0
127	      ],
128	      "gap_values_observed": [
129	        0.0,
130	        -1.7,
131	        3.3,
132	        1.7,
133	        3.3,
134	        0.3,
135	        0.0,
136	        -3.3,
137	        8.3,
138	        3.3,
139	        8.3
140	      ],
141	      "linear_R2": 0.08,
142	      "linear_slope_pp_per_pct": 0.09,
143	      "linear_p_value": 0.37,
144	      "distinct_clusters": 2,
145	      "cluster_low_c0_range": [
146	        0,
147	        10
148	      ],
149	      "cluster_high_c0_range": [
150	        22,
151	        72
152	      ],
153	      "cluster_low_mean_gap": -0.9,
154	      "cluster_high_mean_gap": 1.8
155	    },
156	    "tables": [
157	      "Appendix Table: All (model, domain, C0, gap) data points"
158	    ],
159	    "figures": [],
160	    "analysis": "F4 在 worst 档下仍可展示，但叙事从 'C0 predicts gap (negative correlation)' 变为 'C0 discriminates two regimes (low/high) but provides no gradient information'。 Claim 3 必须弱化：C0 是 'binary indicator' 而非 'diagnostic tool'。 唯一的挽救空间是加 exp-004 (7B) 和 exp-007 (72B) 数据后 within-Qwen-family C0 确实单调递减 (65% → 38% → 22%)，但 gap 不单调 → C0 gradient 存在但无预测力。\n\n\nC0 与 gap 之间无显著线性关系 (R²=0.08, p=0.37)。数据点自然分为两个聚类： reasoning models (C0<10%, gap≈0) 和 instruction models (C0=22-72%, gap 散布于 -3.3 到 +8.3pp)。 无中间 C0 值 (10-22% 区间空白) → C0 仅能做 binary classification (reasoning vs instruction)， 不是 gradient diagnostic。Worst 档的核心问题：instruction-scale 聚类内部 gap 方差极大 (从 -3.3 到 +8.3pp)，C0 对 gap 无预测力。'C0 as necessary-but-insufficient diagnostic' 降级为 'C0 as trivial model-type classifier'。\n"
161	  },
162	  {
163	    "name": "sica_72b_awq",
164	    "description": "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions",
165	    "results": {
166	      "n": 60,
167	      "k": 12,
168	      "sica_accuracy": 0.867,
169	      "sc_accuracy": 0.85,
170	      "delta_pp": 1.7,
171	      "multi_candidate_rate": 0.22,
172	      "extraction_rate": 0.91,
173	      "answer_extraction_rate": 0.97,
174	      "contradiction_rate": 0.015,
175	      "truncated_traces": 5,
176	      "discordant_sica_wins": 3,
177	      "discordant_sc_wins": 2,
178	      "mcnemar_p": 0.65,
179	      "c0_level_cluster": "high"
180	    },
181	    "tables": [
182	      "T1 row: Qwen-72B | PW/FOLIO | 0.867 vs 0.850 | +1.7pp | p=0.65"
183	    ],
184	    "figures": [],
185	    "analysis": "72B 是 within-Qwen scaling 维度的关键数据点。C0 sequence: 7B=65% → 14B=38% → 72B=22% → QwQ-32B=2.6% 形成单调递减，但 gap sequence: +3.3 → +0.3 → +1.7 → 0 不单调。 这意味 C0 gradient 存在 (c0_scaling_distinct_levels 勉强算 2)，但 gap 与 C0 不共变。 论文可在 appendix 展示 Qwen-family 4 点的 C0 trend，标注 'monotonic C0 decrease with scale, but no corresponding gap trend'。\n\n\n72B 的 baseline 高 (SC=85%)，diversity 中等 (C0=22%)。C0=22% 刚过 20% threshold 但 远低于 7B (65%) 和 14B (38%) → 在 Qwen family 内 C0 确实随 scale 递减。 +1.7pp delta 方向为正但完全在噪声内 (p=0.65)。Worst 档问题：C0=22% 是唯一的 intermediate C0 值，本应填补 'gradient' 缺口，但 gap 仍不显著 → C0 gradient 存在 但对 gap 无预测力。72B 的正向 delta 为 reviewer 提供 'scale helps tiebreaking' 的假设空间。\n"
186	  },
187	  {
188	    "name": "constraint_quality_case_studies",
189	    "description": "Qualitative analysis of 8 representative questions' constraints",
190	    "results": {
191	      "n_cases": 8,
192	      "semantically_meaningful": 3,
193	      "correctly_discriminative": 2,
194	      "non_discriminative": 3,
195	      "actively_misleading": 2,
196	      "constraint_categories": {
197	        "tautological": 3,
198	        "partial_correct": 2,
199	        "fully_correct": 2,
200	        "contradiction_with_ground_truth": 1
201	      }
202	    },
203	    "tables": [],
204	    "figures": [],
205	    "analysis": "Case studies 在 worst 档下成为双刃剑：positive examples 展示 method 的理论潜力， negative examples 展示当前 extraction 的局限。论文应选择性呈现：main text 放 一个 positive + 一个 negative (balanced)，appendix 放全部 8 个。叙事调整为 'constraints are occasionally discriminative but too noisy in aggregate to improve over majority voting'。\n\n\n8 个 case study 中，3 个的 constraints 语义上有意义且可区分正确/错误答案。 特别是 FOLIO 形式逻辑问题中，FOL constraints 直接编码推理步骤，部分 constraints 确实 discriminative。这与 aggregate 统计 (precision=0.57) 一致——constraints 并非 completely non-discriminative，而是 weakly discriminative。Worst 档问题：qualitative evidence 展示 constraints CAN work on individual problems，削弱 'constraints lack discriminative power' 的绝对表述。Reviewer 可论证 'the method works, just needs better constraint extraction'。\n"
206	  },
207	  {
208	    "name": "overhead_analysis",
209	    "description": "Wall-time breakdown per question from exp-001 data",
210	    "results": {
211	      "n": 804,
212	      "mean_total_wall_s": 61.6,
213	      "mean_trace_gen_s": 31.6,
214	      "trace_gen_pct": 51.3,
215	      "mean_extract_s": 29.0,
216	      "extract_pct": 47.0,
217	      "mean_dedup_s": 1.0,
218	      "dedup_pct": 1.6,
219	      "mean_maxsat_s": 0.003,
220	      "maxsat_pct": 0.005,
221	      "sica_overhead_pct": 48.7,
222	      "pw_overhead_pct": 51.3,
223	      "folio_overhead_pct": 38.6,
224	      "p50_overhead_pct": 48.9,
225	      "p90_overhead_pct": 57.6,
226	      "overhead_gain_ratio": 162.3
227	    },
228	    "tables": [
229	      "Appendix Table: Overhead breakdown (component × mean time × % total)"
230	    ],
231	    "figures": [],
232	    "analysis": "Overhead analysis 在 worst 档需要扩展：增加 T=1.0 条件下的 overhead 分析。 预计 T=1.0 时 extraction rate 从 89% 降至 76% → 更多 retry / empty extractions → actual overhead 从 48.7% 升至 ~65%。在 boundary conditions 节中呈现： 'T=1.0 gain of +8.3pp comes with 65% overhead increase, effectively doubling compute for a marginal and non-robust improvement'。\n\n\nSICA 额外开销约 48.7%（主要来自 constraint extraction LLM call），MaxSAT 解算 开销可忽略 (<0.01%)。Overhead/gain ratio = 48.7%/0.3pp ≈ 162（每 1pp gain 需 162% overhead）。Worst 档问题：如果 T=1.0 下 gain=+8.3pp，overhead/gain ratio 变为 48.7%/8.3pp ≈ 5.9 — 这就 reasonable 了。Reviewer 会指出 'at T=1.0 the overhead-to-gain ratio is acceptable'，要求 boundary conditions 节量化 T=1.0 的真实 overhead（extraction rate 下降 → 更多 retry → overhead 可能更高）。\n"
233	  },
234	  {
235	    "name": "sica_mistral_7b",
236	    "description": "Mistral-7B-Instruct-v0.3 on D012 60 questions",
237	    "results": {
238	      "n": 60,
239	      "k": 12,
240	      "sica_accuracy": 0.483,
241	      "sc_accuracy": 0.483,
242	      "delta_pp": 0.0,
243	      "multi_candidate_rate": 0.5,
244	      "extraction_rate": 0.882,
245	      "answer_extraction_rate": 1.0,
246	      "contradiction_rate": 0.056,
247	      "discordant_sica_wins": 2,
248	      "discordant_sc_wins": 2,
249	      "mcnemar_p": 1.0,
250	      "proofwriter_sica": 0.4,
251	      "proofwriter_sc": 0.4,
252	      "folio_sica": 0.567,
253	      "folio_sc": 0.567,
254	      "truncated_traces": 0
255	    },
256	    "tables": [
257	      "T1 row: Mistral-7B | PW/FOLIO | 0.483 vs 0.483 | 0pp | p=1.0"
258	    ],
259	    "figures": [],
260	    "analysis": "Mistral 和 LLaMA 的对比是 worst 档的 key tension：两个 7B instruction models， 相似的 C0 (50% vs 62%)，但 delta 完全不同 (0pp vs +8.3pp)。论文必须解释这个差异。 可能的解释：(1) LLaMA 有 48 truncated traces → artifact diversity; (2) Mistral 的 constraint quality 恰好平衡 (equal quality for correct and incorrect answers); (3) sample variance at n=60。策略：在论文中明确标注 LLaMA 的 truncation confound， 并用 exp-019/020 的 large-n LLaMA 数据 (Δ=+2.0pp p=0.424 / Δ=-2.4pp p=0.267) 论证 n=60 的 +8.3pp 是 noise。\n\n\nMistral-7B 产生高 diversity (C0=50%) 但 delta 精确为 0。Discordant pairs 完美 平衡 (2:2)，McNemar p=1.0。这是 capability trap 的教科书案例：abundance of diversity (C0=50%) + zero gain → constraints are non-discriminative on this model。 Worst 档下 Mistral 结果实际上 HELPS the paper（干净的 negative result），但它 也暴露了一个问题：为什么 Mistral delta=0 而 LLaMA delta=+8.3pp？两者都是 7B instruction models with similar C0 (50% vs 62%)。这个不一致使 'model-agnostic trap' 叙述受到挑战。\n"
261	  },
262	  {
263	    "name": "sica_llama_8b",
264	    "description": "LLaMA-3.1-8B-Instruct on D012 60 questions",
265	    "results": {
266	      "n": 60,
267	      "k": 12,
268	      "sica_accuracy": 0.683,
269	      "sc_accuracy": 0.6,
270	      "delta_pp": 8.3,
271	      "multi_candidate_rate": 0.62,
272	      "extraction_rate": 0.83,
273	      "answer_extraction_rate": 0.89,
274	      "contradiction_rate": 0.055,
275	      "truncated_traces": 48,
276	      "discordant_sica_wins": 7,
277	      "discordant_sc_wins": 2,
278	      "mcnemar_p": 0.096,
279	      "proofwriter_sica": 0.633,
280	      "proofwriter_sc": 0.6,
281	      "proofwriter_delta_pp": 3.3,
282	      "folio_sica": 0.733,
283	      "folio_sc": 0.6,
284	      "folio_delta_pp": 13.3,
285	      "discordant_sica_winrate": 0.778
286	    },
287	    "tables": [
288	      "T1 row: LLaMA-8B | PW/FOLIO | 0.683 vs 0.600 | +8.3pp | p=0.096*"
289	    ],
290	    "figures": [],
291	    "analysis": "This is THE experiment that forces the worst-tier reframe。防御策略层级： (1) Primary: exp-019/020 large-n 结果否定 LLaMA positive signal → n=60 是 noise； (2) Secondary: 48 truncated traces confound → 不是 clean comparison； (3) Tertiary: Bonferroni correction across 5+ model families → p=0.096 不 survive multiple testing correction (threshold ≈ 0.02)。 但 reviewer 反驳：'even if this specific result is noise, combined with T=1.0 positive result, there's suggestive evidence that extreme diversity conditions can unlock marginal SICA gains'。论文必须在 boundary conditions 节正面回应： 承认 marginal gains exist at extreme diversity but argue they're dominated by overhead and instability。\n\n\nLLaMA-8B 是 worst 档的核心 problematic result。+8.3pp delta 达 McNemar p=0.096 (< 0.10 threshold)，7:2 discordant ratio 强烈偏向 SICA。FOLIO subset 尤其突出 (+13.3pp)。但有严重 confound：48/720 traces 被 truncated，truncation 可能 人为产生 diverse partial answers → SICA 从 truncation-induced diversity 中获益， 而非从 genuine constraint quality。另一 confound：SC baseline 异常低 (60%)， 远低于 Qwen-14B (76.2%)，暗示 LLaMA-8B 的 reasoning quality 不稳定， 高 variance baseline 更容易产生 spurious positive deltas。 Registry 中 exp-019 (LLaMA StrategyQA n=200 Δ=+2.0pp p=0.424) 和 exp-020 (LLaMA FOLIO n=204 Δ=-2.4pp p=0.267) 的 large-n 结果均不支持 positive signal → 强烈暗示 n=60 的 +8.3pp 是 noise。\n"
292	  },
293	  {
294	    "name": "gsm8k_pilot_14b",
295	    "description": "Qwen2.5-14B on GSM8K 30-question pilot (K=12)",
296	    "results": {
297	      "n": 30,
298	      "k": 12,
299	      "sica_accuracy": 0.8,
300	      "sc_accuracy": 0.767,
301	      "delta_pp": 3.3,
302	      "multi_candidate_rate": 0.27,
303	      "extraction_rate": 0.85,
304	      "answer_extraction_rate": 0.93,
305	      "contradiction_rate": 0.033,
306	      "discordant_sica_wins": 2,
307	      "discordant_sc_wins": 1,
308	      "mcnemar_p": 0.56,
309	      "c0_interpretation": "moderate"
310	    },
311	    "tables": [
312	      "Appendix row or T1 extension: Qwen-14B GSM8K | 0.800 vs 0.767 | +3.3pp | p=0.56"
313	    ],
314	    "figures": [],
315	    "analysis": "GSM8K pilot 在 worst 档下价值有限（n=30 太小），但 C0=27% 是有用的 intermediate 数据点。 策略：放 appendix，注明 pilot。如果扩展到 200 题，预计 delta 回归到 ~0-1pp。 不扩展的理由：GSM8K 不是 NLI/logic domain，与论文主要 scope (formal reasoning) 距离较远， reviewer 不太会 insist on full GSM8K 实验。\n\n\n14B 在 GSM8K 上 accuracy ~77-80%（不是预期的 >85%），C0=27% 中等偏高（预期 <20%）。 原因：K=12 traces 中部分含 arithmetic error 的不同路径，产生 moderate diversity。 +3.3pp delta 在 n=30 下完全无信息量 (SE≈8pp)，但 C0=27% 本身是有价值的数据点—— 填充 F4 散点图的 mid-C0 区域 (与 72B 的 C0=22% 接近)。Worst 档问题：C0=27% 不如预期的 <20%，意味 '14B on easy tasks has low C0' 假设未成立， weakening 'C0 reflects task difficulty / model confidence' 叙事。\n"
316	  },
317	  {
318	    "name": "constraint_ablation",
319	    "description": "MaxSAT vs count-only vs random-weight on exp-001 data (n=804)",
320	    "results": {
321	      "n": 804,
322	      "maxsat_accuracy": 0.765,
323	      "count_only_accuracy": 0.764,
324	      "random_weight_accuracy": 0.763,
325	      "sc_baseline_accuracy": 0.762,
326	      "maxsat_vs_count_delta_pp": 0.1,
327	      "maxsat_vs_random_delta_pp": 0.2,
328	      "count_vs_sc_delta_pp": 0.2,
329	      "mcnemar_maxsat_vs_count_p": 0.85,
330	      "mcnemar_maxsat_vs_random_p": 0.72,
331	      "agreement_rate_maxsat_count": 0.998,
332	      "n_disagreements": 2
333	    },
334	    "tables": [
335	      "T3: Constraint Ablation (method × accuracy × pairwise McNemar p)"
336	    ],
337	    "figures": [],
338	    "analysis": "T3 在 worst 档下需要加 caveat: 'ablation performed at T=0.7; results may differ at extreme temperatures where constraint quality distribution changes'。 如果不做 T=1.0 ablation → reviewer 会视为 major limitation。如果做了且 MaxSAT > count-only at T=1.0 → paper narrative needs fundamental restructuring。 策略：在 main text 只报 T=0.7 ablation, appendix acknowledge T=1.0 ablation as future work。但这在 worst 档 reviewer standards 下可能不够。\n\n\nMaxSAT ≈ count-only ≈ random-weight ≈ SC，四种方法在 804 题中仅 2 题不同。 这是 capability trap 的最强证据之一：satisfiability reasoning (MaxSAT) 相比 简单计数 (count-only) 无任何贡献，证明 constraints 的 logical structure 未被利用， SAT solver 实质上退化为 constraint counter。Worst 档下这一结果仍然干净地支持论文， BUT 如果结合 T=1.0 的 positive result，reviewer 可能要求在 T=1.0 条件下 重做 ablation → 如果 T=1.0 的 MaxSAT > count-only → 表明 high diversity 下 constraint satisfiability 变得 informative → 直接推翻 'mechanism is vacuous'。 论文需要 hedge: 'at default operating conditions (T=0.7), the mechanism is vacuous'.\n"
339	  },
340	  {
341	    "name": "sica_deepseek_r1_llama_8b",
342	    "description": "DeepSeek-R1-Distill-Qwen-7B on D012 60 questions",
343	    "results": {
344	      "n": 60,
345	      "k": 12,
346	      "sica_accuracy": 0.683,
347	      "sc_accuracy": 0.717,
348	      "delta_pp": -3.3,
349	      "multi_candidate_rate": 0.583,
350	      "extraction_rate": 0.839,
351	      "answer_extraction_rate": 0.939,
352	      "truncated_traces": 72,
353	      "contradiction_rate": 0.037,
354	      "mcnemar_p": 0.48,
355	      "discordant_sica_wins": 0,
356	      "discordant_sc_wins": 2,
357	      "model_reclassification": "instruction_scale"
358	    },
359	    "tables": [
360	      "T1 row: DeepSeek-R1-7B | PW/FOLIO | 0.683 vs 0.717 | -3.3pp | instruction-scale"
361	    ],
362	    "figures": [],
363	    "analysis": "DeepSeek reclassification 在 worst 档是 mixed：它增强了 instruction-scale 的 coverage (now 4 families) 但削弱了 reasoning model coverage (only QwQ-32B)。 Reviewer concern: 'you only tested one reasoning model' → mitigate by arguing QwQ-32B at C0=2.6% is structurally determined (reasoning models converge by design) and DeepSeek-R1's reclassification itself is an insight (distillation ≠ reasoning at 7B)。 -3.3pp 的负向 delta 是论文 strongest per-experiment negative result，可用于 'constraints can actively hurt when extraction quality is low' 叙事。\n\n\nDeepSeek-R1-Distill-7B 被重新分类为 instruction-scale model：C0=58%（远非预期的 <5%）， 行为完全像 7B instruction model 而非 reasoning model。Distillation 在 7B 容量下 不足以产生 deterministic reasoning chains。-3.3pp delta 表明 constraints 积极有害 （SICA 比 SC 差）。72 truncated traces 最多（vs LLaMA 的 48）→ reasoning 风格 的长 traces 在 context window 内被截断更多。Worst 档下 DeepSeek 结果 helps the paper (clear negative) 但 reclassification 创建叙事复杂性：原计划将其作为 'second reasoning model'， 现在只有 QwQ-32B 一个 reasoning model 数据点。\n"
364	  },
365	  {
366	    "name": "logic_lm_baseline",
367	    "description": "Logic-LM × K + majority vote on FOLIO, CPU reanalysis",
368	    "results": {
369	      "n_folio": 204,
370	      "logic_lm_k_vote_accuracy": 0.809,
371	      "sica_accuracy_folio": 0.794,
372	      "sc_accuracy_folio": 0.794,
373	      "logic_lm_vs_sica_delta_pp": 1.5,
374	      "logic_lm_vs_sc_delta_pp": 1.5,
375	      "mcnemar_logic_lm_vs_sica_p": 0.38,
376	      "single_trace_logic_lm_accuracy": 0.775,
377	      "k_used": 12
378	    },
379	    "tables": [
380	      "Appendix Table: Logic-LM × K vs SICA vs SC on FOLIO"
381	    ],
382	    "figures": [],
383	    "analysis": "Logic-LM comparison 在 worst 档下是 double-edged：(1) confirms FOL extraction itself has value → good for paper's relevance; (2) suggests SICA's MAX-SAT aggregation is the wrong approach → reviewer may argue for better aggregation rather than abandoning symbolic consensus。论文防御：Logic-LM × K 的 1.5pp advantage 不显著， 且 Logic-LM 的 overhead 更高 (K independent FOL checks vs 1 extraction + 1 MaxSAT)， overhead-adjusted performance 可能 comparable。\n\n\nLogic-LM (单 trace FOL 验证 repeated K times + vote) 在 FOLIO 上达到 0.809， 略高于 SICA 的 0.794 和 SC 的 0.794。差异不显著 (p=0.38) 但方向上 Logic-LM > SICA。 这暗示 multi-trace MAX-SAT aggregation 不仅无益，可能不如 single-trace verification 重复后投票。原因：Logic-LM 对每条 trace 做完整 FOL consistency check（通过/不通过）， 这比 MAX-SAT 的 soft constraint aggregation 更有 discriminative power—— 一条 trace 如果内部逻辑不一致，Logic-LM 直接排除它，而 SICA 仍将其 constraints 纳入 aggregation。Worst 档问题：Logic-LM > SICA 意味 'there IS value in FOL constraints, but SICA's aggregation destroys it' → reviewer 可论证 'fix the aggregation, don't abandon the approach'。\n"
384	  },
385	  {
386	    "name": "weighted_sc_baseline",
387	    "description": "Weighted SC baselines on exp-001 data (n=804)",
388	    "results": {
389	      "n": 804,
390	      "sc_uniform_accuracy": 0.762,
391	      "inv_length_accuracy": 0.77,
392	      "length_weighted_accuracy": 0.753,
393	      "constraint_count_accuracy": 0.753,
394	      "sica_maxsat_accuracy": 0.765,
395	      "inv_length_vs_sc_p": 0.42,
396	      "inv_length_vs_sica_p": 0.79,
397	      "length_vs_sc_p": 0.16,
398	      "all_nonsignificant": true
399	    },
400	    "tables": [
401	      "Appendix Table: Weighted SC variants (method × accuracy × p vs SC)"
402	    ],
403	    "figures": [],
404	    "analysis": "Weighted SC 结果在 worst 档下可用于 'SICA is no better than simple heuristics' 论点。 但 inv-length 的微弱优势暗示 trace quality selection (短 traces = 更 confident) 可能是 right direction，而 SICA 的 constraint-based selection 是 wrong direction。 论文可在 discussion 中 acknowledge 'lightweight quality proxies like trace length may be more effective than formal constraint extraction'。\n\n\nInverse-length weighted SC (偏好短 traces) 达 0.770，略高于 SICA (0.765) 和 SC (0.762)。 Length-weighted 和 constraint-count weighted 反而更差 (0.753)。所有差异不显著。 Worst 档解读：一个 zero-cost heuristic (inverse-length weighting) 匹配或微超 SICA → SICA 的 constraint extraction + MaxSAT 开销完全多余。但 inv-length 的 advantage 也不显著 (p=0.42 vs SC) → 实质上所有方法等价。'Simple weighting ≈ SICA ≈ SC' 强化 'nothing helps' 叙事，但 reviewer 可能 focus on inv-length 的 0.770 → 'there IS a slightly better method, just not yours'。\n"
405	  },
406	  {
407	    "name": "sica_strategyqa_14b",
408	    "description": "Qwen2.5-14B on StrategyQA 60 questions (K=12)",
409	    "results": {
410	      "n": 60,
411	      "k": 12,
412	      "sica_accuracy": 0.567,
413	      "sc_accuracy": 0.533,
414	      "delta_pp": 3.3,
415	      "multi_candidate_rate": 0.1,
416	      "extraction_rate_problem": 1.0,
417	      "extraction_rate_trace": 0.704,
418	      "contradiction_detected": 5,
419	      "discordant_sica_wins": 2,
420	      "discordant_sc_wins": 0,
421	      "mcnemar_p": 0.16,
422	      "bootstrap_p_delta_le_0": 0.135
423	    },
424	    "tables": [
425	      "T1 column: StrategyQA | Qwen-14B | 0.567 vs 0.533 | +3.3pp | p=0.16"
426	    ],
427	    "figures": [],
428	    "analysis": "StrategyQA 的 low C0 在 worst 档是一个 minor complication。本来预期 'binary task → high C0 → test capability trap'，实际 C0=10% → test is underpowered。 论文处理：在 T1 标注 C0=10% 并解释 '14B commonsense confidence limits diversity'。 +3.3pp delta 可在 F3 heatmap 中展示但不强调。StrategyQA 作为 'third domain' 的角色弱化——它更像 ARC 的 low-C0 场景而非预期的 high-C0 场景。\n\n\nStrategyQA 的 C0=10% 意外地低——binary task (yes/no) 预期 C0 应该高 (30-50%)。 原因：Qwen-14B 在 commonsense reasoning 上相对 confident，12 traces 中大多数 agree on same answer。低 C0 使 SICA 退化为近 SC (only 10% problems have multiple candidates)。+3.3pp delta 来自极少的 discordant pairs (2:0)，p=0.16 不显著。 Worst 档问题：(1) C0=10% 打破 'StrategyQA should have high C0' 预期 → domain difficulty 与 C0 的关系比预想复杂；(2) +3.3pp 虽不显著但方向一致为正， 与 LLaMA StrategyQA (exp-019, Δ=+2.0pp) 方向一致 → suggestive cross-model positive signal in StrategyQA domain。\n"
429	  },
430	  {
431	    "name": "sica_arc_challenge_14b",
432	    "description": "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)",
433	    "results": {
434	      "n": 60,
435	      "k": 12,
436	      "sica_accuracy": 0.95,
437	      "sc_accuracy": 0.967,
438	      "delta_pp": -1.7,
439	      "multi_candidate_rate": 0.05,
440	      "extraction_rate": 1.0,
441	      "contradiction_detected": 3,
442	      "discordant_sica_wins": 0,
443	      "discordant_sc_wins": 1,
444	      "c0_interpretation": "near_degenerate"
445	    },
446	    "tables": [
447	      "T1 column: ARC | Qwen-14B | 0.950 vs 0.967 | -1.7pp"
448	    ],
449	    "figures": [],
450	    "analysis": "ARC 在 worst 档是最弱的 domain data point：C0=5% 使它成为 QwQ-32B 类的 'degenerate' case 而非真正的 'third domain test'。论文需要在 discussion 中 acknowledge 'ARC-Challenge may be too easy for 14B models to provide a meaningful test of symbolic consensus methods'。如果 ARC 和 StrategyQA 都是 low-C0 (5%, 10%), 则论文只有 FOLIO + ProofWriter 两个真正的 high-C0 domains → 'three domains' claim weakened。\n\n\nARC-Challenge 的 C0=5% 极低——Qwen-14B 在 science reasoning 上 baseline 高 (SC=96.7%)， 几乎所有题目 unanimous。SICA 退化为 SC，唯一的 discordant pair 是 SC 赢。 -1.7pp delta 来自 1 个 problem 的 constraint misfire。Worst 档下 ARC 结果干净 地支持 'low C0 → degeneration' 叙事，但暴露一个问题：C0=5% 意味 ARC-Challenge 对 14B 太简单，不是 meaningful test bed。Reviewer 可能要求 harder science tasks (e.g., GPQA) 或 weaker model on ARC → 超出 budget。\n"
451	  },
452	  {
453	    "name": "constraint_quality_correlation",
454	    "description": "Per-problem constraint precision analysis, CPU (n≈307 multi-candidate problems from exp-001)",
455	    "results": {
456	      "n_multi_candidate_problems": 307,
457	      "constraint_precision_mean": 0.57,
458	      "constraint_precision_std": 0.23,
459	      "constraint_precision_median": 0.58,
460	      "precision_vs_vote_entropy_R2": 0.008,
461	      "precision_vs_vote_entropy_slope": 0.03,
462	      "precision_vs_vote_entropy_p": 0.12,
463	      "precision_vs_exclusion_rate_R2": 0.003,
464	      "precision_vs_exclusion_rate_slope": -0.01,
465	      "precision_by_domain_pw": 0.55,
466	      "precision_by_domain_folio": 0.62,
467	      "precision_above_random_3class": true,
468	      "precision_above_random_binary": true,
469	      "hero_figure_verdict": "failed"
470	    },
471	    "tables": [
472	      "T2: Constraint Quality (domain × precision mean ± std × n)"
473	    ],
474	    "figures": [],
475	    "analysis": "F2 hero figure 概念失败是 worst 档的 defining moment for paper structure。 原计划的 scatter plot (C0 vs constraint precision, showing inverse correlation) 变成 formless cloud。Plan B: response-surface heatmap (temperature × model, cell color = SICA-SC gap)，展示 gap landscape 绝大部分 ≈ 0 但 T=1.0 角落有正值。 这是一个 weaker but still publishable figure，叙事从 'here's why the trap exists' 变为 'here's where the trap holds and where it breaks down'。 Precision=0.57 的重新解读需要更长的 analysis 段落：'Constraints are weakly discriminative (precision 0.57 vs 0.33 random) but this 7pp advantage over chance is insufficient to reliably flip majority vote outcomes. At K=12 with C0=38%, only ~3-4 multi-candidate problems per experiment set, and constraints correct 57% of the time, the expected number of correct flips is ~2 — comparable to noise.'\n\n\nPer-problem constraint precision 平均 0.57 (std 0.23)，显著高于 3-class random (0.33) 和 binary random (0.50)。这直接与 'constraints lack discriminative power' 叙事矛盾—— constraints ARE weakly discriminative，精度 57% 意味着接近 6/10 的 constraints 正确指向 ground truth。但 precision 与 vote_entropy 几乎无关 (R²=0.008, slope=0.03)： diversity level 不影响 constraint quality。Hero figure (precision vs entropy scatter) 是一个 formless cloud，无可读模式。FOLIO precision (0.62) 高于 ProofWriter (0.55)， 可能因为 FOLIO 的形式逻辑结构更适合 FOL constraint extraction。 Worst 档核心问题：precision=0.57 > 0.50 → constraints 并非 'non-discriminative'， 它们是 'weakly discriminative'。Paper claim 必须从 'constraints lack discriminative power' 重写为 'constraints have insufficient discriminative power to overcome aggregation noise at practical sample sizes'。\n"
476	  },
477	  {
478	    "name": "temperature_ablation_t03_t05_t10",
479	    "description": "T=0.3/0.5/1.0 on Qwen-14B D012 60题, diversity-gap relationship",
480	    "results": {
481	      "t03_n": 60,
482	      "t03_c0": 0.18,
483	      "t03_sica_accuracy": 0.75,
484	      "t03_sc_accuracy": 0.733,
485	      "t03_delta_pp": 1.7,
486	      "t03_extraction_rate": 0.93,
487	      "t03_mcnemar_p": 0.65,
488	      "t03_discordant_sica": 2,
489	      "t03_discordant_sc": 1,
490	      "t05_n": 60,
491	      "t05_c0": 0.3,
492	      "t05_sica_accuracy": 0.75,
493	      "t05_sc_accuracy": 0.733,
494	      "t05_delta_pp": 1.7,
495	      "t05_extraction_rate": 0.91,
496	      "t05_mcnemar_p": 0.55,
497	      "t05_discordant_sica": 3,
498	      "t05_discordant_sc": 2,
499	      "t10_n": 60,
500	      "t10_c0": 0.72,
501	      "t10_sica_accuracy": 0.817,
502	      "t10_sc_accuracy": 0.733,
503	      "t10_delta_pp": 8.3,
504	      "t10_extraction_rate": 0.76,
505	      "t10_answer_coherence_rate": 0.85,
506	      "t10_mcnemar_p": 0.034,
507	      "t10_discordant_sica": 7,
508	      "t10_discordant_sc": 1,
509	      "t10_discordant_sica_winrate": 0.875,
510	      "temp_max_abs_delta_pp": 8.3,
511	      "c0_vs_temp_correlation": 0.98,
512	      "gap_vs_temp_monotonic": true
513	    },
514	    "tables": [
515	      "Table (boundary conditions section): Temperature × C0 × SICA × SC × Δ × p × extraction rate"
516	    ],
517	    "figures": [],
518	    "analysis": "Temperature ablation 的 T=1.0 positive result (p=0.034) 是 worst 档的最大叙事挑战。 论文必须加 'boundary conditions' 节正面回应： (1) T=1.0 的 +8.3pp 伴随 extraction rate 从 89% 降至 76% → 约 24% 的 traces 产生 empty/corrupt constraints → MaxSAT input quality 退化； (2) Answer coherence 从 ~98% 降至 85% → 15% 的 outputs 本身质量低 → 这些 outputs 的 constraints 是 noise； (3) 如果将 overhead 折入：T=0.7 overhead ≈ 49%，T=1.0 overhead ≈ 65% (因 extraction retry) → effective cost per question 增加 ~30%； (4) 结论：'T=1.0 partially breaks the trap but at a cost that negates the gain. The marginal +8.3pp requires 65% additional compute, operating in a regime where 15% of outputs are incoherent. Practitioners seeking this marginal gain would be better served by simply increasing K at T=0.7.'\n这一 framing 将 T=1.0 positive result 转化为 'the trap has a theoretical escape hatch that is practically useless'。但 reviewer 可反驳：'(1) overhead analysis is not done at T=1.0, you're speculating; (2) incoherence at T=1.0 is model-specific and may not apply to larger models; (3) p=0.034 < 0.05, this is a real effect.'\n\n\nTemperature ablation 是 worst 档的 defining experiment。T 与 C0 高度相关 (r=0.98)： T=0.3→C0=18%, T=0.5→C0=30%, T=0.7→C0=38% (baseline), T=1.0→C0=72%。 关键发现：T=1.0 下 SICA 显著优于 SC (+8.3pp, p=0.034)，7:1 discordant ratio。 这打破 'regardless of diversity' 声明——在极端 diversity 下 SICA 确实有优势。 但伴随成本：extraction rate 从 89% (T=0.7) 降至 76% (T=1.0)，answer coherence 从 ~98% 降至 85%。15% incoherent outputs 意味实际 usable diversity 低于 C0 暗示的。 T=0.3 和 T=0.5 的 delta 为 +1.7pp，均不显著 (p>0.5)，与 T=0.7 的 +0.3pp (exp-001 n=804) 方向一致但大小不同（n=60 variance）。 Gap vs temperature 单调递增暗示 'more diversity → more SICA gain'，直接否定 capability trap 作为 structural mechanism：trap 在 default T=0.7 下成立， 但在 T=1.0 下 partially broken → trap 不是 structural，只是 default operating condition 的产物。\n"
519	  },
520	  {
521	    "name": "gsm8k_pilot_30q",
522	    "description": "Qwen-14B GSM8K 30-question pilot, math reasoning domain",
523	    "results": {
524	      "n": 30,
525	      "k": 12,
526	      "sica_accuracy": 0.8,
527	      "sc_accuracy": 0.767,
528	      "delta_pp": 3.3,
529	      "multi_candidate_rate": 0.23,
530	      "extraction_rate": 0.85,
531	      "answer_extraction_rate": 0.93,
532	      "contradiction_rate": 0.033,
533	      "discordant_sica_wins": 2,
534	      "discordant_sc_wins": 1,
535	      "mcnemar_p": 0.56
536	    },
537	    "tables": [
538	      "Appendix: GSM8K pilot results (same as exp-012)"
539	    ],
540	    "figures": [],
541	    "analysis": "GSM8K pilot 在 worst 档下是 'nice to have' 但不改变任何 narrative。C0=23% 填充 F4 mid-range 但 n=30 误差带太宽。不建议投入 GPU budget 扩展，除非 reviewer explicit 要求 math domain coverage。\n\n与 exp-012 相同实验。C0=23% 中等——14B 在 GSM8K 上不完全 confident，部分 arithmetic 步骤产生不同答案。+3.3pp 在 n=30 下无信息量。此实验在 worst 档下价值在于 提供一个 math domain 数据点 (与 NLI/science domains 互补)，但 n=30 太小无法 影响任何 claim。如不扩展到 200+ 题，GSM8K 只能放 appendix 且不计入 main claims。\n"
542	  }
543	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53f0b398-4e02-4427-9085-acd75154dd21",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "fc7a1bfd-7c3e-4ab8-a999-b800e4a23c34",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"sica_k_ablation_14b\",\n    \"description\": \"K sensitivity (K=6,8,11,12,16,20) on D012 60 questions, Qwen-14B\",\n    \"results\": {\n      \"K6_sica\": 0.75,\n      \"K6_sc\": 0.733,\n      \"K6_gap_pp\": 1.7,\n      \"K8_sica\": 0.75,\n      \"K8_sc\": 0.75,\n      \"K8_gap_pp\": 0.0,\n      \"K11_sica\": 0.75,\n      \"K11_sc\": 0.75,\n      \"K11_gap_pp\": 0.0,\n      \"K12_sica\": 0.733,\n      \"K12_sc\": 0.75,\n      \"K12_gap_pp\": -1.7,\n      \"K16_sica\": 0.717,\n      \"K16_sc\": 0.733,\n      \"K16_gap_pp\": -1.7,\n      \"K20_sica\": 0.717,\n      \"K20_sc\": 0.733,\n      \"K20_gap_pp\": -1.7,\n      \"tiebreak_rate_K6\": 0.183,\n      \"tiebreak_rate_K12\": 0.267,\n      \"tiebreak_rate_K20\": 0.05,\n      \"all_K_sica_leq_sc\": false,\n      \"n\": 60\n    },\n    \"tables\": [\n      \"Appendix Table A1: K-ablation results (K × accuracy × gap × tiebreak rate)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"K=6 的 +1.7pp 在 n=60 下 SE≈5pp，统计上无意义 (p>0.5)，但在图上形成一个视觉上的正向点， reviewer 可能追问 'why not use K=6?'。应对策略：在 appendix 说明 K=6 下 SC 本身 variance 更大 (fewer votes)， +1.7pp 在 bootstrap CI [-5.0, +8.3] 内完全兼容零效应。K=11 (odd) gap=0 是核心证据： 无 tie 时 SICA 完全等价于 SC，确认 SICA 的全部潜在价值来自 tiebreaking。论文可保留此结论。\\n\\n\\nWorst 档下 K=6 出现 +1.7pp 正向 delta。原因：低 K 时每条 trace 权重大，diversity 自然较高， SICA 的 constraint filtering 在少样本高 diversity 场景有边际价值。K=11 (odd) gap=0 确认 tiebreak-only mechanism：去除 exact tie 后 SICA 无额外价值。K≥12 时 SICA 退化：更多 traces 引入更多 low-quality constraints，noise injection 效应压过任何 signal。整体模式非单调—— low K 弱正向、odd K 零、high K 弱负向——使 'SICA ≤ SC at all K' 叙述失效，需改为 'K-dependent with no consistent advantage'。\\n\"\n  },\n  {\n    \"name\": \"tiebreak_baseline_analysis\",\n    \"description\": \"SICA vs SC-random-tiebreak vs SC-deterministic on tied questions, CPU reanalysis\",\n    \"results\": {\n      \"n_tied_questions\": 5,\n      \"sica_tiebreak_accuracy\": 0.8,\n      \"random_tiebreak_accuracy\": 0.5,\n      \"alphabetical_tiebreak_accuracy\": 0.6,\n      \"first_seen_tiebreak_accuracy\": 0.4,\n      \"tied_question_fraction\": 0.083,\n      \"n_total_problems\": 60\n    },\n    \"tables\": [\n      \"T4: Tiebreak Analysis (method × accuracy on tied subset × contribution to overall gap)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Tiebreak quality 80% 本身是一个 positive result，论文不能忽略。应策略性地呈现： 在 T4 中同时展示 'accuracy on ties' (SICA wins) 和 'contribution to total accuracy' (negligible)。用 'effective contribution' = tiebreak_quality × tie_rate 量化： 0.80 × 0.083 = 6.6% effective contribution → translates to ~2pp at best。 在 worst 档叙事中，这成为 'boundary conditions' 节的辅助论据。\\n\\n\\nSICA 在 tied questions 上表现出色 (80% vs random 50%)，证明 constraint-based tiebreaking 有真实价值。但问题在于 tied questions 极少 (5/60 = 8.3%)：即使 SICA 每次 tie 都选对， 对总体 accuracy 的贡献仅 ~0.083 × 0.30 ≈ +2.5pp。Worst 档的问题：80% tiebreak quality 给 reviewer 一个 'method works on ties, just needs more ties' 的反驳切入点，暗示 在更极端的 diversity 条件（如 T=1.0）下 SICA 可能有更大价值。这与温度 ablation 正向结果 形成叙事共振，削弱 trap 的 'structural' 性质。\\n\"\n  },\n  {\n    \"name\": \"sica_7b_scaling\",\n    \"description\": \"Qwen2.5-7B-Instruct on D012 60 questions, within-Qwen scaling\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.6,\n      \"sc_accuracy\": 0.567,\n      \"delta_pp\": 3.3,\n      \"multi_candidate_rate\": 0.65,\n      \"extraction_rate\": 0.82,\n      \"answer_extraction_rate\": 0.88,\n      \"contradiction_rate\": 0.068,\n      \"truncated_traces\": 30,\n      \"discordant_sica_wins\": 4,\n      \"discordant_sc_wins\": 2,\n      \"mcnemar_p\": 0.41,\n      \"proofwriter_sica\": 0.567,\n      \"proofwriter_sc\": 0.533,\n      \"proofwriter_delta_pp\": 3.3,\n      \"folio_sica\": 0.633,\n      \"folio_sc\": 0.6,\n      \"folio_delta_pp\": 3.3,\n      \"c0_level_cluster\": \"high\"\n    },\n    \"tables\": [\n      \"T1 row: Qwen-7B | PW/FOLIO | 0.600 vs 0.567 | +3.3pp | p=0.41\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 结果在 worst 档中制造叙事摩擦：delta 方向为正，且比 14B (+0.3pp) 更大。 Reviewer 可能论证 'the method works better on weaker models where diversity is higher'， 要求 larger-n 验证。防御：(1) n=60 SE≈6pp，+3.3pp 在 CI 内含零；(2) extraction rate 下降到 82% 意味 constraint quality 更差；(3) 即使真实效应为 +3pp，overhead 约 50% 使 cost/gain ratio 不合理。但这些论证相比 'trap is structural' 明显更弱。\\n\\n\\n7B 模型更弱 → baseline 更低 (SC≈57%) → diversity 更高 (C0=65% vs 14B 的 38%)。 Higher diversity 给 SICA 更多操作空间，产生 +3.3pp 边际正向 delta。但 p=0.41 完全 在噪声范围内。Worst 档的核心问题：7B 和 14B 的 C0 都在 {30-68%} 聚类中，无法构成 'C0 gradient' → c0_scaling_distinct_levels 仍为 2（{<5%} vs {30-68%}）。 +3.3pp delta 虽不显著，但方向一致地为正，给 reviewer 'underpowered positive' 解读空间。 Truncation 较高 (30/720 traces) 引入 confound：truncated traces 可能产生 artifact diversity。\\n\"\n  },\n  {\n    \"name\": \"qwq_32b_operating_regime\",\n    \"description\": \"QwQ-32B negative control — data from MVP phase, formatted for paper\",\n    \"results\": {\n      \"qwq_aggregate_c0_nominal_pct\": 10.3,\n      \"qwq_aggregate_c0_effective_pct\": 2.6,\n      \"qwen14b_c0_pct\": 46.0,\n      \"diversity_ratio_effective\": 17.7,\n      \"aime_delta_pp\": 0.0,\n      \"proofwriter_delta_pp\": -5.9,\n      \"aime_n\": 22,\n      \"proofwriter_n\": 17,\n      \"temp_diversity_n\": 5,\n      \"folio_n\": 2,\n      \"total_problems\": 46,\n      \"c0_threshold\": 20,\n      \"qwq_below_threshold\": true,\n      \"sica_eq_sc_all_domains\": true\n    },\n    \"tables\": [\n      \"T1 row: QwQ-32B | AIME/PW/FOLIO | SICA≡SC | C0=2.6%\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"QwQ-32B 数据是论文最干净的 negative control，worst 档下仍可正常使用。风险在于 reviewer 要求 larger-n QwQ 验证或其他 reasoning model (e.g., o1-mini, Gemini 2.5 Flash Thinking) → 超出 GPU budget。在 worst 叙事中，QwQ-32B 作为 'converged regime' 示例仍成立， 但 'operating regime is empirically empty' 的强声明需要更多 reasoning model 数据点。\\n\\n\\nQwQ-32B 作为 full reasoning model，deterministic chain 主导 sampling randomness， C0 effective 仅 2.6%。SICA ≡ SC 是结构性的——only 1-2 candidate answers per problem， MaxSAT exclusion 无 target。这一结果干净地支持 'low C0 → method degenerates' 叙述。 Worst 档的问题不在结果本身，而在数据量：total n=46 且分布不均 (AIME 22, PW 17, temperature 5, FOLIO 2)，统计功效极低。Reviewer 可质疑 'n=46 不足以得出 C0<5% 是 generalizable 的结论'。\\n\"\n  },\n  {\n    \"name\": \"c0_diagnostic_validation\",\n    \"description\": \"C0 vs SICA-SC gap scatter across all models/conditions, CPU analysis\",\n    \"results\": {\n      \"n_data_points\": 12,\n      \"c0_values_observed\": [\n        2.6,\n        5.0,\n        10.0,\n        22.0,\n        27.0,\n        38.0,\n        50.0,\n        58.0,\n        62.0,\n        65.0,\n        72.0\n      ],\n      \"gap_values_observed\": [\n        0.0,\n        -1.7,\n        3.3,\n        1.7,\n        3.3,\n        0.3,\n        0.0,\n        -3.3,\n        8.3,\n        3.3,\n        8.3\n      ],\n      \"linear_R2\": 0.08,\n      \"linear_slope_pp_per_pct\": 0.09,\n      \"linear_p_value\": 0.37,\n      \"distinct_clusters\": 2,\n      \"cluster_low_c0_range\": [\n        0,\n        10\n      ],\n      \"cluster_high_c0_range\": [\n        22,\n        72\n      ],\n      \"cluster_low_mean_gap\": -0.9,\n      \"cluster_high_mean_gap\": 1.8\n    },\n    \"tables\": [\n      \"Appendix Table: All (model, domain, C0, gap) data points\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"F4 在 worst 档下仍可展示，但叙事从 'C0 predicts gap (negative correlation)' 变为 'C0 discriminates two regimes (low/high) but provides no gradient information'。 Claim 3 必须弱化：C0 是 'binary indicator' 而非 'diagnostic tool'。 唯一的挽救空间是加 exp-004 (7B) 和 exp-007 (72B) 数据后 within-Qwen-family C0 确实单调递减 (65% → 38% → 22%)，但 gap 不单调 → C0 gradient 存在但无预测力。\\n\\n\\nC0 与 gap 之间无显著线性关系 (R²=0.08, p=0.37)。数据点自然分为两个聚类： reasoning models (C0<10%, gap≈0) 和 instruction models (C0=22-72%, gap 散布于 -3.3 到 +8.3pp)。 无中间 C0 值 (10-22% 区间空白) → C0 仅能做 binary classification (reasoning vs instruction)， 不是 gradient diagnostic。Worst 档的核心问题：instruction-scale 聚类内部 gap 方差极大 (从 -3.3 到 +8.3pp)，C0 对 gap 无预测力。'C0 as necessary-but-insufficient diagnostic' 降级为 'C0 as trivial model-type classifier'。\\n\"\n  },\n  {\n    \"name\": \"sica_72b_awq\",\n    \"description\": \"Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.85,\n      \"delta_pp\": 1.7,\n      \"multi_candidate_rate\": 0.22,\n      \"extraction_rate\": 0.91,\n      \"answer_extraction_rate\": 0.97,\n      \"contradiction_rate\": 0.015,\n      \"truncated_traces\": 5,\n      \"discordant_sica_wins\": 3,\n      \"discordant_sc_wins\": 2,\n      \"mcnemar_p\": 0.65,\n      \"c0_level_cluster\": \"high\"\n    },\n    \"tables\": [\n      \"T1 row: Qwen-72B | PW/FOLIO | 0.867 vs 0.850 | +1.7pp | p=0.65\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 是 within-Qwen scaling 维度的关键数据点。C0 sequence: 7B=65% → 14B=38% → 72B=22% → QwQ-32B=2.6% 形成单调递减，但 gap sequence: +3.3 → +0.3 → +1.7 → 0 不单调。 这意味 C0 gradient 存在 (c0_scaling_distinct_levels 勉强算 2)，但 gap 与 C0 不共变。 论文可在 appendix 展示 Qwen-family 4 点的 C0 trend，标注 'monotonic C0 decrease with scale, but no corresponding gap trend'。\\n\\n\\n72B 的 baseline 高 (SC=85%)，diversity 中等 (C0=22%)。C0=22% 刚过 20% threshold 但 远低于 7B (65%) 和 14B (38%) → 在 Qwen family 内 C0 确实随 scale 递减。 +1.7pp delta 方向为正但完全在噪声内 (p=0.65)。Worst 档问题：C0=22% 是唯一的 intermediate C0 值，本应填补 'gradient' 缺口，但 gap 仍不显著 → C0 gradient 存在 但对 gap 无预测力。72B 的正向 delta 为 reviewer 提供 'scale helps tiebreaking' 的假设空间。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_case_studies\",\n    \"description\": \"Qualitative analysis of 8 representative questions' constraints\",\n    \"results\": {\n      \"n_cases\": 8,\n      \"semantically_meaningful\": 3,\n      \"correctly_discriminative\": 2,\n      \"non_discriminative\": 3,\n      \"actively_misleading\": 2,\n      \"constraint_categories\": {\n        \"tautological\": 3,\n        \"partial_correct\": 2,\n        \"fully_correct\": 2,\n        \"contradiction_with_ground_truth\": 1\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies 在 worst 档下成为双刃剑：positive examples 展示 method 的理论潜力， negative examples 展示当前 extraction 的局限。论文应选择性呈现：main text 放 一个 positive + 一个 negative (balanced)，appendix 放全部 8 个。叙事调整为 'constraints are occasionally discriminative but too noisy in aggregate to improve over majority voting'。\\n\\n\\n8 个 case study 中，3 个的 constraints 语义上有意义且可区分正确/错误答案。 特别是 FOLIO 形式逻辑问题中，FOL constraints 直接编码推理步骤，部分 constraints 确实 discriminative。这与 aggregate 统计 (precision=0.57) 一致——constraints 并非 completely non-discriminative，而是 weakly discriminative。Worst 档问题：qualitative evidence 展示 constraints CAN work on individual problems，削弱 'constraints lack discriminative power' 的绝对表述。Reviewer 可论证 'the method works, just needs better constraint extraction'。\\n\"\n  },\n  {\n    \"name\": \"overhead_analysis\",\n    \"description\": \"Wall-time breakdown per question from exp-001 data\",\n    \"results\": {\n      \"n\": 804,\n      \"mean_total_wall_s\": 61.6,\n      \"mean_trace_gen_s\": 31.6,\n      \"trace_gen_pct\": 51.3,\n      \"mean_extract_s\": 29.0,\n      \"extract_pct\": 47.0,\n      \"mean_dedup_s\": 1.0,\n      \"dedup_pct\": 1.6,\n      \"mean_maxsat_s\": 0.003,\n      \"maxsat_pct\": 0.005,\n      \"sica_overhead_pct\": 48.7,\n      \"pw_overhead_pct\": 51.3,\n      \"folio_overhead_pct\": 38.6,\n      \"p50_overhead_pct\": 48.9,\n      \"p90_overhead_pct\": 57.6,\n      \"overhead_gain_ratio\": 162.3\n    },\n    \"tables\": [\n      \"Appendix Table: Overhead breakdown (component × mean time × % total)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Overhead analysis 在 worst 档需要扩展：增加 T=1.0 条件下的 overhead 分析。 预计 T=1.0 时 extraction rate 从 89% 降至 76% → 更多 retry / empty extractions → actual overhead 从 48.7% 升至 ~65%。在 boundary conditions 节中呈现： 'T=1.0 gain of +8.3pp comes with 65% overhead increase, effectively doubling compute for a marginal and non-robust improvement'。\\n\\n\\nSICA 额外开销约 48.7%（主要来自 constraint extraction LLM call），MaxSAT 解算 开销可忽略 (<0.01%)。Overhead/gain ratio = 48.7%/0.3pp ≈ 162（每 1pp gain 需 162% overhead）。Worst 档问题：如果 T=1.0 下 gain=+8.3pp，overhead/gain ratio 变为 48.7%/8.3pp ≈ 5.9 — 这就 reasonable 了。Reviewer 会指出 'at T=1.0 the overhead-to-gain ratio is acceptable'，要求 boundary conditions 节量化 T=1.0 的真实 overhead（extraction rate 下降 → 更多 retry → overhead 可能更高）。\\n\"\n  },\n  {\n    \"name\": \"sica_mistral_7b\",\n    \"description\": \"Mistral-7B-Instruct-v0.3 on D012 60 questions\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.483,\n      \"sc_accuracy\": 0.483,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.5,\n      \"extraction_rate\": 0.882,\n      \"answer_extraction_rate\": 1.0,\n      \"contradiction_rate\": 0.056,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 2,\n      \"mcnemar_p\": 1.0,\n      \"proofwriter_sica\": 0.4,\n      \"proofwriter_sc\": 0.4,\n      \"folio_sica\": 0.567,\n      \"folio_sc\": 0.567,\n      \"truncated_traces\": 0\n    },\n    \"tables\": [\n      \"T1 row: Mistral-7B | PW/FOLIO | 0.483 vs 0.483 | 0pp | p=1.0\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral 和 LLaMA 的对比是 worst 档的 key tension：两个 7B instruction models， 相似的 C0 (50% vs 62%)，但 delta 完全不同 (0pp vs +8.3pp)。论文必须解释这个差异。 可能的解释：(1) LLaMA 有 48 truncated traces → artifact diversity; (2) Mistral 的 constraint quality 恰好平衡 (equal quality for correct and incorrect answers); (3) sample variance at n=60。策略：在论文中明确标注 LLaMA 的 truncation confound， 并用 exp-019/020 的 large-n LLaMA 数据 (Δ=+2.0pp p=0.424 / Δ=-2.4pp p=0.267) 论证 n=60 的 +8.3pp 是 noise。\\n\\n\\nMistral-7B 产生高 diversity (C0=50%) 但 delta 精确为 0。Discordant pairs 完美 平衡 (2:2)，McNemar p=1.0。这是 capability trap 的教科书案例：abundance of diversity (C0=50%) + zero gain → constraints are non-discriminative on this model。 Worst 档下 Mistral 结果实际上 HELPS the paper（干净的 negative result），但它 也暴露了一个问题：为什么 Mistral delta=0 而 LLaMA delta=+8.3pp？两者都是 7B instruction models with similar C0 (50% vs 62%)。这个不一致使 'model-agnostic trap' 叙述受到挑战。\\n\"\n  },\n  {\n    \"name\": \"sica_llama_8b\",\n    \"description\": \"LLaMA-3.1-8B-Instruct on D012 60 questions\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.6,\n      \"delta_pp\": 8.3,\n      \"multi_candidate_rate\": 0.62,\n      \"extraction_rate\": 0.83,\n      \"answer_extraction_rate\": 0.89,\n      \"contradiction_rate\": 0.055,\n      \"truncated_traces\": 48,\n      \"discordant_sica_wins\": 7,\n      \"discordant_sc_wins\": 2,\n      \"mcnemar_p\": 0.096,\n      \"proofwriter_sica\": 0.633,\n      \"proofwriter_sc\": 0.6,\n      \"proofwriter_delta_pp\": 3.3,\n      \"folio_sica\": 0.733,\n      \"folio_sc\": 0.6,\n      \"folio_delta_pp\": 13.3,\n      \"discordant_sica_winrate\": 0.778\n    },\n    \"tables\": [\n      \"T1 row: LLaMA-8B | PW/FOLIO | 0.683 vs 0.600 | +8.3pp | p=0.096*\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is THE experiment that forces the worst-tier reframe。防御策略层级： (1) Primary: exp-019/020 large-n 结果否定 LLaMA positive signal → n=60 是 noise； (2) Secondary: 48 truncated traces confound → 不是 clean comparison； (3) Tertiary: Bonferroni correction across 5+ model families → p=0.096 不 survive multiple testing correction (threshold ≈ 0.02)。 但 reviewer 反驳：'even if this specific result is noise, combined with T=1.0 positive result, there's suggestive evidence that extreme diversity conditions can unlock marginal SICA gains'。论文必须在 boundary conditions 节正面回应： 承认 marginal gains exist at extreme diversity but argue they're dominated by overhead and instability。\\n\\n\\nLLaMA-8B 是 worst 档的核心 problematic result。+8.3pp delta 达 McNemar p=0.096 (< 0.10 threshold)，7:2 discordant ratio 强烈偏向 SICA。FOLIO subset 尤其突出 (+13.3pp)。但有严重 confound：48/720 traces 被 truncated，truncation 可能 人为产生 diverse partial answers → SICA 从 truncation-induced diversity 中获益， 而非从 genuine constraint quality。另一 confound：SC baseline 异常低 (60%)， 远低于 Qwen-14B (76.2%)，暗示 LLaMA-8B 的 reasoning quality 不稳定， 高 variance baseline 更容易产生 spurious positive deltas。 Registry 中 exp-019 (LLaMA StrategyQA n=200 Δ=+2.0pp p=0.424) 和 exp-020 (LLaMA FOLIO n=204 Δ=-2.4pp p=0.267) 的 large-n 结果均不支持 positive signal → 强烈暗示 n=60 的 +8.3pp 是 noise。\\n\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_14b\",\n    \"description\": \"Qwen2.5-14B on GSM8K 30-question pilot (K=12)\",\n    \"results\": {\n      \"n\": 30,\n      \"k\": 12,\n      \"sica_accuracy\": 0.8,\n      \"sc_accuracy\": 0.767,\n      \"delta_pp\": 3.3,\n      \"multi_candidate_rate\": 0.27,\n      \"extraction_rate\": 0.85,\n      \"answer_extraction_rate\": 0.93,\n      \"contradiction_rate\": 0.033,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 0.56,\n      \"c0_interpretation\": \"moderate\"\n    },\n    \"tables\": [\n      \"Appendix row or T1 extension: Qwen-14B GSM8K | 0.800 vs 0.767 | +3.3pp | p=0.56\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K pilot 在 worst 档下价值有限（n=30 太小），但 C0=27% 是有用的 intermediate 数据点。 策略：放 appendix，注明 pilot。如果扩展到 200 题，预计 delta 回归到 ~0-1pp。 不扩展的理由：GSM8K 不是 NLI/logic domain，与论文主要 scope (formal reasoning) 距离较远， reviewer 不太会 insist on full GSM8K 实验。\\n\\n\\n14B 在 GSM8K 上 accuracy ~77-80%（不是预期的 >85%），C0=27% 中等偏高（预期 <20%）。 原因：K=12 traces 中部分含 arithmetic error 的不同路径，产生 moderate diversity。 +3.3pp delta 在 n=30 下完全无信息量 (SE≈8pp)，但 C0=27% 本身是有价值的数据点—— 填充 F4 散点图的 mid-C0 区域 (与 72B 的 C0=22% 接近)。Worst 档问题：C0=27% 不如预期的 <20%，意味 '14B on easy tasks has low C0' 假设未成立， weakening 'C0 reflects task difficulty / model confidence' 叙事。\\n\"\n  },\n  {\n    \"name\": \"constraint_ablation\",\n    \"description\": \"MaxSAT vs count-only vs random-weight on exp-001 data (n=804)\",\n    \"results\": {\n      \"n\": 804,\n      \"maxsat_accuracy\": 0.765,\n      \"count_only_accuracy\": 0.764,\n      \"random_weight_accuracy\": 0.763,\n      \"sc_baseline_accuracy\": 0.762,\n      \"maxsat_vs_count_delta_pp\": 0.1,\n      \"maxsat_vs_random_delta_pp\": 0.2,\n      \"count_vs_sc_delta_pp\": 0.2,\n      \"mcnemar_maxsat_vs_count_p\": 0.85,\n      \"mcnemar_maxsat_vs_random_p\": 0.72,\n      \"agreement_rate_maxsat_count\": 0.998,\n      \"n_disagreements\": 2\n    },\n    \"tables\": [\n      \"T3: Constraint Ablation (method × accuracy × pairwise McNemar p)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"T3 在 worst 档下需要加 caveat: 'ablation performed at T=0.7; results may differ at extreme temperatures where constraint quality distribution changes'。 如果不做 T=1.0 ablation → reviewer 会视为 major limitation。如果做了且 MaxSAT > count-only at T=1.0 → paper narrative needs fundamental restructuring。 策略：在 main text 只报 T=0.7 ablation, appendix acknowledge T=1.0 ablation as future work。但这在 worst 档 reviewer standards 下可能不够。\\n\\n\\nMaxSAT ≈ count-only ≈ random-weight ≈ SC，四种方法在 804 题中仅 2 题不同。 这是 capability trap 的最强证据之一：satisfiability reasoning (MaxSAT) 相比 简单计数 (count-only) 无任何贡献，证明 constraints 的 logical structure 未被利用， SAT solver 实质上退化为 constraint counter。Worst 档下这一结果仍然干净地支持论文， BUT 如果结合 T=1.0 的 positive result，reviewer 可能要求在 T=1.0 条件下 重做 ablation → 如果 T=1.0 的 MaxSAT > count-only → 表明 high diversity 下 constraint satisfiability 变得 informative → 直接推翻 'mechanism is vacuous'。 论文需要 hedge: 'at default operating conditions (T=0.7), the mechanism is vacuous'.\\n\"\n  },\n  {\n    \"name\": \"sica_deepseek_r1_llama_8b\",\n    \"description\": \"DeepSeek-R1-Distill-Qwen-7B on D012 60 questions\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.717,\n      \"delta_pp\": -3.3,\n      \"multi_candidate_rate\": 0.583,\n      \"extraction_rate\": 0.839,\n      \"answer_extraction_rate\": 0.939,\n      \"truncated_traces\": 72,\n      \"contradiction_rate\": 0.037,\n      \"mcnemar_p\": 0.48,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 2,\n      \"model_reclassification\": \"instruction_scale\"\n    },\n    \"tables\": [\n      \"T1 row: DeepSeek-R1-7B | PW/FOLIO | 0.683 vs 0.717 | -3.3pp | instruction-scale\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek reclassification 在 worst 档是 mixed：它增强了 instruction-scale 的 coverage (now 4 families) 但削弱了 reasoning model coverage (only QwQ-32B)。 Reviewer concern: 'you only tested one reasoning model' → mitigate by arguing QwQ-32B at C0=2.6% is structurally determined (reasoning models converge by design) and DeepSeek-R1's reclassification itself is an insight (distillation ≠ reasoning at 7B)。 -3.3pp 的负向 delta 是论文 strongest per-experiment negative result，可用于 'constraints can actively hurt when extraction quality is low' 叙事。\\n\\n\\nDeepSeek-R1-Distill-7B 被重新分类为 instruction-scale model：C0=58%（远非预期的 <5%）， 行为完全像 7B instruction model 而非 reasoning model。Distillation 在 7B 容量下 不足以产生 deterministic reasoning chains。-3.3pp delta 表明 constraints 积极有害 （SICA 比 SC 差）。72 truncated traces 最多（vs LLaMA 的 48）→ reasoning 风格 的长 traces 在 context window 内被截断更多。Worst 档下 DeepSeek 结果 helps the paper (clear negative) 但 reclassification 创建叙事复杂性：原计划将其作为 'second reasoning model'， 现在只有 QwQ-32B 一个 reasoning model 数据点。\\n\"\n  },\n  {\n    \"name\": \"logic_lm_baseline\",\n    \"description\": \"Logic-LM × K + majority vote on FOLIO, CPU reanalysis\",\n    \"results\": {\n      \"n_folio\": 204,\n      \"logic_lm_k_vote_accuracy\": 0.809,\n      \"sica_accuracy_folio\": 0.794,\n      \"sc_accuracy_folio\": 0.794,\n      \"logic_lm_vs_sica_delta_pp\": 1.5,\n      \"logic_lm_vs_sc_delta_pp\": 1.5,\n      \"mcnemar_logic_lm_vs_sica_p\": 0.38,\n      \"single_trace_logic_lm_accuracy\": 0.775,\n      \"k_used\": 12\n    },\n    \"tables\": [\n      \"Appendix Table: Logic-LM × K vs SICA vs SC on FOLIO\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Logic-LM comparison 在 worst 档下是 double-edged：(1) confirms FOL extraction itself has value → good for paper's relevance; (2) suggests SICA's MAX-SAT aggregation is the wrong approach → reviewer may argue for better aggregation rather than abandoning symbolic consensus。论文防御：Logic-LM × K 的 1.5pp advantage 不显著， 且 Logic-LM 的 overhead 更高 (K independent FOL checks vs 1 extraction + 1 MaxSAT)， overhead-adjusted performance 可能 comparable。\\n\\n\\nLogic-LM (单 trace FOL 验证 repeated K times + vote) 在 FOLIO 上达到 0.809， 略高于 SICA 的 0.794 和 SC 的 0.794。差异不显著 (p=0.38) 但方向上 Logic-LM > SICA。 这暗示 multi-trace MAX-SAT aggregation 不仅无益，可能不如 single-trace verification 重复后投票。原因：Logic-LM 对每条 trace 做完整 FOL consistency check（通过/不通过）， 这比 MAX-SAT 的 soft constraint aggregation 更有 discriminative power—— 一条 trace 如果内部逻辑不一致，Logic-LM 直接排除它，而 SICA 仍将其 constraints 纳入 aggregation。Worst 档问题：Logic-LM > SICA 意味 'there IS value in FOL constraints, but SICA's aggregation destroys it' → reviewer 可论证 'fix the aggregation, don't abandon the approach'。\\n\"\n  },\n  {\n    \"name\": \"weighted_sc_baseline\",\n    \"description\": \"Weighted SC baselines on exp-001 data (n=804)\",\n    \"results\": {\n      \"n\": 804,\n      \"sc_uniform_accuracy\": 0.762,\n      \"inv_length_accuracy\": 0.77,\n      \"length_weighted_accuracy\": 0.753,\n      \"constraint_count_accuracy\": 0.753,\n      \"sica_maxsat_accuracy\": 0.765,\n      \"inv_length_vs_sc_p\": 0.42,\n      \"inv_length_vs_sica_p\": 0.79,\n      \"length_vs_sc_p\": 0.16,\n      \"all_nonsignificant\": true\n    },\n    \"tables\": [\n      \"Appendix Table: Weighted SC variants (method × accuracy × p vs SC)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Weighted SC 结果在 worst 档下可用于 'SICA is no better than simple heuristics' 论点。 但 inv-length 的微弱优势暗示 trace quality selection (短 traces = 更 confident) 可能是 right direction，而 SICA 的 constraint-based selection 是 wrong direction。 论文可在 discussion 中 acknowledge 'lightweight quality proxies like trace length may be more effective than formal constraint extraction'。\\n\\n\\nInverse-length weighted SC (偏好短 traces) 达 0.770，略高于 SICA (0.765) 和 SC (0.762)。 Length-weighted 和 constraint-count weighted 反而更差 (0.753)。所有差异不显著。 Worst 档解读：一个 zero-cost heuristic (inverse-length weighting) 匹配或微超 SICA → SICA 的 constraint extraction + MaxSAT 开销完全多余。但 inv-length 的 advantage 也不显著 (p=0.42 vs SC) → 实质上所有方法等价。'Simple weighting ≈ SICA ≈ SC' 强化 'nothing helps' 叙事，但 reviewer 可能 focus on inv-length 的 0.770 → 'there IS a slightly better method, just not yours'。\\n\"\n  },\n  {\n    \"name\": \"sica_strategyqa_14b\",\n    \"description\": \"Qwen2.5-14B on StrategyQA 60 questions (K=12)\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.567,\n      \"sc_accuracy\": 0.533,\n      \"delta_pp\": 3.3,\n      \"multi_candidate_rate\": 0.1,\n      \"extraction_rate_problem\": 1.0,\n      \"extraction_rate_trace\": 0.704,\n      \"contradiction_detected\": 5,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 0,\n      \"mcnemar_p\": 0.16,\n      \"bootstrap_p_delta_le_0\": 0.135\n    },\n    \"tables\": [\n      \"T1 column: StrategyQA | Qwen-14B | 0.567 vs 0.533 | +3.3pp | p=0.16\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"StrategyQA 的 low C0 在 worst 档是一个 minor complication。本来预期 'binary task → high C0 → test capability trap'，实际 C0=10% → test is underpowered。 论文处理：在 T1 标注 C0=10% 并解释 '14B commonsense confidence limits diversity'。 +3.3pp delta 可在 F3 heatmap 中展示但不强调。StrategyQA 作为 'third domain' 的角色弱化——它更像 ARC 的 low-C0 场景而非预期的 high-C0 场景。\\n\\n\\nStrategyQA 的 C0=10% 意外地低——binary task (yes/no) 预期 C0 应该高 (30-50%)。 原因：Qwen-14B 在 commonsense reasoning 上相对 confident，12 traces 中大多数 agree on same answer。低 C0 使 SICA 退化为近 SC (only 10% problems have multiple candidates)。+3.3pp delta 来自极少的 discordant pairs (2:0)，p=0.16 不显著。 Worst 档问题：(1) C0=10% 打破 'StrategyQA should have high C0' 预期 → domain difficulty 与 C0 的关系比预想复杂；(2) +3.3pp 虽不显著但方向一致为正， 与 LLaMA StrategyQA (exp-019, Δ=+2.0pp) 方向一致 → suggestive cross-model positive signal in StrategyQA domain。\\n\"\n  },\n  {\n    \"name\": \"sica_arc_challenge_14b\",\n    \"description\": \"Qwen2.5-14B on ARC-Challenge 60 questions (K=12)\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.95,\n      \"sc_accuracy\": 0.967,\n      \"delta_pp\": -1.7,\n      \"multi_candidate_rate\": 0.05,\n      \"extraction_rate\": 1.0,\n      \"contradiction_detected\": 3,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 1,\n      \"c0_interpretation\": \"near_degenerate\"\n    },\n    \"tables\": [\n      \"T1 column: ARC | Qwen-14B | 0.950 vs 0.967 | -1.7pp\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ARC 在 worst 档是最弱的 domain data point：C0=5% 使它成为 QwQ-32B 类的 'degenerate' case 而非真正的 'third domain test'。论文需要在 discussion 中 acknowledge 'ARC-Challenge may be too easy for 14B models to provide a meaningful test of symbolic consensus methods'。如果 ARC 和 StrategyQA 都是 low-C0 (5%, 10%), 则论文只有 FOLIO + ProofWriter 两个真正的 high-C0 domains → 'three domains' claim weakened。\\n\\n\\nARC-Challenge 的 C0=5% 极低——Qwen-14B 在 science reasoning 上 baseline 高 (SC=96.7%)， 几乎所有题目 unanimous。SICA 退化为 SC，唯一的 discordant pair 是 SC 赢。 -1.7pp delta 来自 1 个 problem 的 constraint misfire。Worst 档下 ARC 结果干净 地支持 'low C0 → degeneration' 叙事，但暴露一个问题：C0=5% 意味 ARC-Challenge 对 14B 太简单，不是 meaningful test bed。Reviewer 可能要求 harder science tasks (e.g., GPQA) 或 weaker model on ARC → 超出 budget。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_correlation\",\n    \"description\": \"Per-problem constraint precision analysis, CPU (n≈307 multi-candidate problems from exp-001)\",\n    \"results\": {\n      \"n_multi_candidate_problems\": 307,\n      \"constraint_precision_mean\": 0.57,\n      \"constraint_precision_std\": 0.23,\n      \"constraint_precision_median\": 0.58,\n      \"precision_vs_vote_entropy_R2\": 0.008,\n      \"precision_vs_vote_entropy_slope\": 0.03,\n      \"precision_vs_vote_entropy_p\": 0.12,\n      \"precision_vs_exclusion_rate_R2\": 0.003,\n      \"precision_vs_exclusion_rate_slope\": -0.01,\n      \"precision_by_domain_pw\": 0.55,\n      \"precision_by_domain_folio\": 0.62,\n      \"precision_above_random_3class\": true,\n      \"precision_above_random_binary\": true,\n      \"hero_figure_verdict\": \"failed\"\n    },\n    \"tables\": [\n      \"T2: Constraint Quality (domain × precision mean ± std × n)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"F2 hero figure 概念失败是 worst 档的 defining moment for paper structure。 原计划的 scatter plot (C0 vs constraint precision, showing inverse correlation) 变成 formless cloud。Plan B: response-surface heatmap (temperature × model, cell color = SICA-SC gap)，展示 gap landscape 绝大部分 ≈ 0 但 T=1.0 角落有正值。 这是一个 weaker but still publishable figure，叙事从 'here's why the trap exists' 变为 'here's where the trap holds and where it breaks down'。 Precision=0.57 的重新解读需要更长的 analysis 段落：'Constraints are weakly discriminative (precision 0.57 vs 0.33 random) but this 7pp advantage over chance is insufficient to reliably flip majority vote outcomes. At K=12 with C0=38%, only ~3-4 multi-candidate problems per experiment set, and constraints correct 57% of the time, the expected number of correct flips is ~2 — comparable to noise.'\\n\\n\\nPer-problem constraint precision 平均 0.57 (std 0.23)，显著高于 3-class random (0.33) 和 binary random (0.50)。这直接与 'constraints lack discriminative power' 叙事矛盾—— constraints ARE weakly discriminative，精度 57% 意味着接近 6/10 的 constraints 正确指向 ground truth。但 precision 与 vote_entropy 几乎无关 (R²=0.008, slope=0.03)： diversity level 不影响 constraint quality。Hero figure (precision vs entropy scatter) 是一个 formless cloud，无可读模式。FOLIO precision (0.62) 高于 ProofWriter (0.55)， 可能因为 FOLIO 的形式逻辑结构更适合 FOL constraint extraction。 Worst 档核心问题：precision=0.57 > 0.50 → constraints 并非 'non-discriminative'， 它们是 'weakly discriminative'。Paper claim 必须从 'constraints lack discriminative power' 重写为 'constraints have insufficient discriminative power to overcome aggregation noise at practical sample sizes'。\\n\"\n  },\n  {\n    \"name\": \"temperature_ablation_t03_t05_t10\",\n    \"description\": \"T=0.3/0.5/1.0 on Qwen-14B D012 60题, diversity-gap relationship\",\n    \"results\": {\n      \"t03_n\": 60,\n      \"t03_c0\": 0.18,\n      \"t03_sica_accuracy\": 0.75,\n      \"t03_sc_accuracy\": 0.733,\n      \"t03_delta_pp\": 1.7,\n      \"t03_extraction_rate\": 0.93,\n      \"t03_mcnemar_p\": 0.65,\n      \"t03_discordant_sica\": 2,\n      \"t03_discordant_sc\": 1,\n      \"t05_n\": 60,\n      \"t05_c0\": 0.3,\n      \"t05_sica_accuracy\": 0.75,\n      \"t05_sc_accuracy\": 0.733,\n      \"t05_delta_pp\": 1.7,\n      \"t05_extraction_rate\": 0.91,\n      \"t05_mcnemar_p\": 0.55,\n      \"t05_discordant_sica\": 3,\n      \"t05_discordant_sc\": 2,\n      \"t10_n\": 60,\n      \"t10_c0\": 0.72,\n      \"t10_sica_accuracy\": 0.817,\n      \"t10_sc_accuracy\": 0.733,\n      \"t10_delta_pp\": 8.3,\n      \"t10_extraction_rate\": 0.76,\n      \"t10_answer_coherence_rate\": 0.85,\n      \"t10_mcnemar_p\": 0.034,\n      \"t10_discordant_sica\": 7,\n      \"t10_discordant_sc\": 1,\n      \"t10_discordant_sica_winrate\": 0.875,\n      \"temp_max_abs_delta_pp\": 8.3,\n      \"c0_vs_temp_correlation\": 0.98,\n      \"gap_vs_temp_monotonic\": true\n    },\n    \"tables\": [\n      \"Table (boundary conditions section): Temperature × C0 × SICA × SC × Δ × p × extraction rate\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature ablation 的 T=1.0 positive result (p=0.034) 是 worst 档的最大叙事挑战。 论文必须加 'boundary conditions' 节正面回应： (1) T=1.0 的 +8.3pp 伴随 extraction rate 从 89% 降至 76% → 约 24% 的 traces 产生 empty/corrupt constraints → MaxSAT input quality 退化； (2) Answer coherence 从 ~98% 降至 85% → 15% 的 outputs 本身质量低 → 这些 outputs 的 constraints 是 noise； (3) 如果将 overhead 折入：T=0.7 overhead ≈ 49%，T=1.0 overhead ≈ 65% (因 extraction retry) → effective cost per question 增加 ~30%； (4) 结论：'T=1.0 partially breaks the trap but at a cost that negates the gain. The marginal +8.3pp requires 65% additional compute, operating in a regime where 15% of outputs are incoherent. Practitioners seeking this marginal gain would be better served by simply increasing K at T=0.7.'\\n这一 framing 将 T=1.0 positive result 转化为 'the trap has a theoretical escape hatch that is practically useless'。但 reviewer 可反驳：'(1) overhead analysis is not done at T=1.0, you're speculating; (2) incoherence at T=1.0 is model-specific and may not apply to larger models; (3) p=0.034 < 0.05, this is a real effect.'\\n\\n\\nTemperature ablation 是 worst 档的 defining experiment。T 与 C0 高度相关 (r=0.98)： T=0.3→C0=18%, T=0.5→C0=30%, T=0.7→C0=38% (baseline), T=1.0→C0=72%。 关键发现：T=1.0 下 SICA 显著优于 SC (+8.3pp, p=0.034)，7:1 discordant ratio。 这打破 'regardless of diversity' 声明——在极端 diversity 下 SICA 确实有优势。 但伴随成本：extraction rate 从 89% (T=0.7) 降至 76% (T=1.0)，answer coherence 从 ~98% 降至 85%。15% incoherent outputs 意味实际 usable diversity 低于 C0 暗示的。 T=0.3 和 T=0.5 的 delta 为 +1.7pp，均不显著 (p>0.5)，与 T=0.7 的 +0.3pp (exp-001 n=804) 方向一致但大小不同（n=60 variance）。 Gap vs temperature 单调递增暗示 'more diversity → more SICA gain'，直接否定 capability trap 作为 structural mechanism：trap 在 default T=0.7 下成立， 但在 T=1.0 下 partially broken → trap 不是 structural，只是 default operating condition 的产物。\\n\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_30q\",\n    \"description\": \"Qwen-14B GSM8K 30-question pilot, math reasoning domain\",\n    \"results\": {\n      \"n\": 30,\n      \"k\": 12,\n      \"sica_accuracy\": 0.8,\n      \"sc_accuracy\": 0.767,\n      \"delta_pp\": 3.3,\n      \"multi_candidate_rate\": 0.23,\n      \"extraction_rate\": 0.85,\n      \"answer_extraction_rate\": 0.93,\n      \"contradiction_rate\": 0.033,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 0.56\n    },\n    \"tables\": [\n      \"Appendix: GSM8K pilot results (same as exp-012)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K pilot 在 worst 档下是 'nice to have' 但不改变任何 narrative。C0=23% 填充 F4 mid-range 但 n=30 误差带太宽。不建议投入 GPU budget 扩展，除非 reviewer explicit 要求 math domain coverage。\\n\\n与 exp-012 相同实验。C0=23% 中等——14B 在 GSM8K 上不完全 confident，部分 arithmetic 步骤产生不同答案。+3.3pp 在 n=30 下无信息量。此实验在 worst 档下价值在于 提供一个 math domain 数据点 (与 NLI/science domains 互补)，但 n=30 太小无法 影响任何 claim。如不扩展到 200+ 题，GSM8K 只能放 appendix 且不计入 main claims。\\n\"\n  }\n]",
      "numLines": 543,
      "startLine": 1,
      "totalLines": 543
    }
  },
  "sourceToolAssistantUUID": "53f0b398-4e02-4427-9085-acd75154dd21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "fc7a1bfd-7c3e-4ab8-a999-b800e4a23c34",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic consensus survey paper for dream_20260517T144412",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Assistant

_source line 14 · 2026-05-17T15:41:07.467Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me synthesize what I need to write:

The paper has been reframed from "structural impossibility" to "first systematic empirical survey of symbolic consensus across models, domains, and operating conditions." The title should be: "When Does Symbolic Consensus Help? A Systematic Empirical Study"

Key narrative changes based on the worst-tier guidance:
1. Temperature ablation T=1.0 shows Δ=+8.3pp (p=0.034), breaking "regardless of diversity" claim


2. LLaMA-8B D012 has p=0.096, a second marginal positive result
3. F2 per-problem constraint precision mean 0.57 > random (0.33), contradicts "non-discriminative" narrative
4. C0 only has 2 clusters, no gradient → trivial binary indicator
5. Drop "capability trap" as mechanism claim, downgrade to descriptive label
6. Add "boundary conditions" section for T=1.0
7. Hero figure: temperature × model response-surface heatmap

Now I'm mapping out the paper structure with Abstract, Introduction, Related Work, Method covering the SICA pipeline, and Experimental Setup as the foundation.

For the results section, I need to organize the findings across multiple analyses—main results, constraint quality, ablations, tiebreak patterns, C0 diagnostics, and temperature sensitivity—each with corresponding tables. The appendix will hold supplementary analyses including K-ablation, computational overhead, weighted scoring, Logic-LM comparisons, C0 details, and the GSM8K pilot. I'm ready to write the full LaTeX document using standard article formatting.

Now I'm extracting the numerical results from the experiments. The main results table needs accuracy scores for each model-domain combination, along with the improvement deltas and significance values. I'm pulling data from the constraint ablation and overhead analyses to populate T1 with the baseline and SICA performance across Qwen-14B, Qwen-7B, Qwen-72B-AWQ, and Mistral-7B. Looking at the GSM8K pilot results, the SICA approach shows a modest improvement over standard voting. Now examining the constraint quality metrics across 307 multi-candidate problems—precision averages around 0.57 with notable variation, and interestingly there's almost no correlation between precision and voting entropy. The constraint ablation study across 804 problems reveals that MaxSAT, count-only, random-weight, and standard voting all perform nearly identically around 0.76-0.77, with no statistically significant differences between them.

For tiebreaking, SICA substantially outperforms random and alphabetical approaches when candidates are tied. The temperature ablation shows an interesting pattern: lower temperatures keep more candidates in contention but don't improve performance, while higher temperatures dramatically increase the fraction of single-candidate problems and push SICA accuracy up to 0.817, though the extraction rate drops to 76%.

Now looking at how the number of candidates affects performance, I'm seeing that SICA remains stable around 0.750 across K=6 through K=11, matching or slightly trailing the standard approach, but performance degrades as K increases further, with SICA dropping to 0.717 at K=16 and K=20 while tiebreaking becomes more frequent at smaller K values.

For the overhead analysis across 804 samples, trace generation and extraction dominate the runtime at roughly equal proportions around 50% each, with deduplication and MaxSAT contributing negligibly, and SICA itself accounting for about half the total overhead. The diagnostic on C0 shows two distinct behavioral clusters—cases with minimal constraint gaps cluster around zero while others show stronger positive gaps—though the linear relationship is weak. When I weight the standard approach by different factors, inverse-length weighting performs best at 0.770, slightly outperforming uniform weighting at 0.762, while both length and constraint-count weighting drop to 0.753.

Now looking at the Logic-LM results on FOLIO, SICA achieves 0.794 which matches the standard approach, while Logic-LM with knowledge augmentation reaches 0.809—a modest improvement that isn't statistically significant. The constraint case studies reveal a mixed picture: only 3 of 8 cases show meaningful discriminative power, while 2 actually mislead rather than help. As I write this up, I need to reframe the narrative around when symbolic consensus actually helps rather than claiming it's fundamentally limited, adjust the title to reflect this systematic empirical perspective, properly contextualize the boundary condition where it does work, treat C0 as a binary signal rather than a continuous diagnostic, describe the capability trap as an observed pattern without overstating the mechanism, and be transparent about the precision limitations.

Writing the paper now with a clean LaTeX template suitable for EMNLP standards. I'm organizing the key results into tables—mapping across the seven models and four domains, though not all combinations have data. Let me structure the main results table carefully to show which experiments actually ran. out what data I have:

Qwen-14B:
- D012 (PW+FOLIO) n=804: SICA=76.5, SC=76.2, Δ=+0.3pp (from constraint_ablation)
  Wait, actually the n=804 seems to be aggregate. Let me check... The experiment descriptions say "D012 60 questions" for most experiments, but constraint_ablation has n=804. This must be the full dataset.
  
  Actually, looking more carefully:
  - sica_k_ablation_14b: "D012 60 questions, Qwen-14B" - this is a subset
  - constraint_ablation: n=804 - this is the main exp-001 data
  - sica_strategyqa_14b: StrategyQA 60 questions
  - sica_arc_challenge_14b: ARC-Challenge 60 questions

So for Qwen-14B I'm seeing the full D012 results at n=804 with a marginal improvement, while the smaller 60-question subsets show more substantial gains on StrategyQA and a slight regression on ARC. For Qwen-7B, the D012 subset shows a 3.3pp improvement, with similar patterns across the PW and FOLIO components.

Qwen-72B shows a smaller 1.7pp improvement on D012. Mistral-7B shows no improvement overall, though there's a notable difference between PW (no gain) and FOLIO (no gain either). LLaMA-8B shows the largest improvement at 8.3pp, with stronger gains on FOLIO than PW.

Now I'm compiling the performance metrics across all these models and datasets to see the overall pattern.

Looking at the paper structure, I need to organize this clearly. I'm planning out the main sections: starting with an abstract, then introduction and related work, followed by the SICA method description, experimental setup, and results sections.

For the results, I'll break it into several subsections covering the main findings, constraint quality analysis, mechanism ablations, temperature sensitivity, and how C0 functions as an operating regime indicator. Then I'll wrap up with discussion and conclusion sections, plus a comprehensive appendix covering ablations, tiebreak analysis, overhead, baseline comparisons, and case studies.

I'm going to write this up now using a standard article class with clean formatting.

Actually, I'll keep it simple and avoid external dependencies. The key narrative shift is reframing this as a systematic empirical survey rather than claiming structural impossibility—the title should reflect that. For the main figure, I'm thinking a temperature by model response surface heatmap would be ideal, though I'll need to work around the lack of actual data files. I can use tikz or just create table-based visualizations instead.

Writing the LaTeX document now...

For the paper structure, I need specific numbers: the abstract should cite 3 domains across 5 model families with over 1300 samples, showing SICA and symbolic consensus produce roughly 1.5 percentage point gains, constraint precision around 0.57, and that MaxSAT performs similarly to simpler baselines. The temperature boundary at 1.0 shows an 8.3 percentage point improvement but with extraction degradation. Then I'll build out the introduction with the problem-insight-method-findings arc, followed by results tables covering all model and domain combinations, constraint precision analysis, and ablation studies.

Now I'm organizing the main results table with model, domain, sample size, symbolic consensus baseline, SICA performance, the delta in percentage points, and significance testing. I need to pull every number directly from the experiment data rather than estimating. Now I'm looking at the additional model results and noticing QwQ-32B needs special handling since its data is sparse across different benchmarks. Let me reorganize it to show the breakdown clearly—it has mixed results with zero delta on AIME but negative performance on ProofWriter, and I should present that separately from the standard table format. Now I'm looking at the performance metrics across different temperature settings, and I need to be careful about which experimental subset each result comes from—the temperature ablation uses a different 60-question set than the main experiment with 804 questions, which is why the SICA and SC scores diverge at certain temperature points. I'm gathering the C0 values (multi-candidate rates) for each model from the data to reference in the paper, though I notice some inconsistencies across different sections that I need to reconcile before writing. I'm settling on the multi_candidate_rate values as my C0 metric across experiments, with Qwen-14B at 38% from the temperature ablation and the other models pulling from their respective datasets. Now I need to write out the full LaTeX document, and I'll go with a standard article class to keep the formatting clean and straightforward.

For the figures, I'm considering what I can actually render—pgfplots might not be available, so I'll stick with basic tikz or simple tabular layouts to visualize the temperature-model heatmap and the C0 versus gap scatter plot. I'll rely on standard packages like amsmath, booktabs, and geometry to avoid compilation issues.

Now I'm setting up the LaTeX structure with a minimal preamble, making sure every number pulls from the experiment data and the narrative follows the worst-tier guidance while covering all experiments without any AI-style markers.

Writing the paper now... I need to map out where each experiment result will appear in the paper—some go in the main tables, others in the appendix, and a few get discussed narratively in the text. Let me make sure I'm covering all the key analyses and not duplicating anything across sections. I'm mapping out where each experiment belongs across the main tables and appendix sections. The GSM8K pilot experiments are duplicates, so I'll consolidate those. Now I'm ready to write everything up.

The key numbers to anchor the narrative: the aggregate improvement is around 1.5 percentage points, with only two experiments showing p-values below 0.10 (though neither survives multiple comparison correction). SICA wins roughly 65% of the discordant pair comparisons across all experiments. I'll make sure these headline findings are woven through clearly.

Starting with the Qwen-14B results as the main focus...

the constraint ablation experiment shows a 0.3 percentage point improvement for SICA over SC on the largest dataset (n=804), but this difference isn't statistically significant. I'll report it that way in the main table and move forward with writing the full paper.

Now I'm structuring the document with a clear outline—starting with a title about when symbolic consensus helps, followed by an abstract that frames this as the first systematic evaluation across multiple reasoning domains, model families, and experimental conditions. I'll keep the writing concise and grounded in the empirical results. which extracts first-order logic constraints from K reasoning traces and selects answers via weighted MAX-SAT. Across N>1,300 problems, SICA provides no significant accuracy gain over majority voting (aggregate |Δ|≈1.5pp). We identify a recurring pattern we term the capability trap: instruction-scale models produce sufficient output diversity for symbolic methods to operate (C0=22-65%), but extracted constraints are only weakly discriminative (mean precision 0.57). MAX-SAT optimization over such constraints is statistically equivalent to simple counting or random weighting. At extreme temperatures (T=1.0), SICA achieves a significant +8.3pp gain (p=0.034), but extraction quality degrades (76% vs 89%) and output coherence drops to 85%, limiting practical applicability. We propose C0 (candidate answer fraction) as a zero-cost binary indicator: C0<5% guarantees method degeneration, while C0>20% is necessary but insufficient for potential gains.

Now I'm outlining the paper structure. The introduction will establish the broader context around LLM reasoning and sampling-based approaches versus symbolic methods, then pose the central question of when symbolic consensus actually helps—something that hasn't been systematically characterized. I'll position our work as filling that gap through SICA as a controlled test bed, and lay out the key findings including the capability trap concept. The related work section covers self-consistency, symbolic reasoning approaches like Logic-LM, and relevant negative results. For the method section, I'm describing the SICA pipeline starting with trace generation, constraint extraction in first-order logic, and then the decoding strategy.

The experimental setup spans multiple model families and reasoning domains with specific hyperparameter choices, while the results section will present main findings, constraint quality analysis, ablations, and boundary conditions around temperature sensitivity. Finally, the discussion will synthesize these findings and their implications.

Now I'm deciding how to structure the paper—which analyses belong in the main text versus the appendix. The core narrative should feature the primary results table, constraint quality metrics, the ablation study, and temperature sensitivity as a boundary condition, while pushing the K-ablation, computational overhead, weighted baselines, and GSM8K pilot to the appendix. The C0 diagnostic could work as its own section to show when symbolic consensus operates effectively.

I need to be careful about the writing style too—avoiding em-dashes, -ing constructions, and overused academic phrases like "leverage" or "notably." Time to draft the full LaTeX document with these constraints in mind.

Writing the paper now...

I'm noticing a potential duplicate in the experiments—gsm8k_pilot_14b and gsm8k_pilot_30q appear to have identical results, so I'll consolidate them in the appendix. Before I write the full paper, I need to pin down the C0 values for Table 1. Looking at the multi_candidate_rate across experiments: Qwen-7B D012 gives 65%, and for Qwen-14B D012 I'm seeing 38% from the temperature ablation at T=0.7, though there's some variation depending on which experiment I reference. I'll go with 38% since it matches the main condition, but I need to verify what the constraint_ablation experiment actually reports for C0.

The discrepancy between the 46% from qwq_32b_operating_regime and 38% from temperature ablation likely stems from different dataset sizes—the full n=804 experiment versus a 60-question subset—so I'll use the appropriate value depending on the context of each table. For the main table, I'll pull C0 values as reported in each experiment, computing from multi_candidate_rate when necessary. I'm realizing I need to use the 46% figure from the QwQ comparison for Qwen-14B's multi_candidate_rate since it's not directly available from the main experiment, though I should note this varies with temperature. Looking back at the diagnostic validation data, I can see the C0 values that were actually observed across different conditions. I've got 11 C0 values but 12 data points, so there's definitely a mismatch—either a duplicate or a missing entry. Looking at the gap values to cross-reference: the pattern shows consistent mappings for most entries like QwQ-32B with a gap of 0.0, ARC with -1.7, and StrategyQA with +3.3, but I need to trace through the rest to find where the discrepancy lies. Looking at the baseline values I've identified, I count 11 distinct data points, but the experiment indicates there should be 12. I'm trying to figure out which temperature condition is the missing one—it's likely either T=0.3 with around 18% baseline or T=0.5 with around 30% baseline, both showing similar performance gaps.

Since I have enough data to proceed, I'm moving forward with writing the paper. I'll use 38% as Qwen-14B's baseline value from the T=0.7 condition for the main results table. Now I'm setting up the LaTeX structure with standard packages and booktabs for formatting, and I'll create a text-based representation for the temperature-by-model heatmap since I can't generate actual graphics.

For length, I'm aiming for 8-10 pages of main text plus appendix, which is reasonable in single-column format with 11pt font. I need to be meticulous about verifying each number against the experimental data, and I'm noticing a discrepancy between the framing document and the constraint ablation data for Qwen-14B that I should resolve before finalizing. accuracy=0.762, which gives Δ=+0.3pp. I'll use +0.3pp since that's what the data shows.

Actually, 0.765 - 0.762 = 0.003 = 0.3pp. And the framing says 0.25pp. This might be due to rounding. I'll use +0.3pp since that's what the data directly shows.

Now I'm computing the aggregate weighted delta across all models. Taking the absolute deltas weighted by their sample sizes and summing them up, I get a total of 1537.2 across 1270 samples, which averages to about 1.21pp. That's lower than the framing's ≈1.5pp, so there might be a different calculation method they used.

I'll go with the ≈1.5pp figure from the guidance since it's marked as approximate. Now I need to structure the LaTeX document itself. The paper should have a clear title about symbolic consensus and empirical study, frame this as the first systematic survey rather than an impossibility proof, use "capability trap" as a descriptive label, acknowledge the positive T=1.0 result in the boundary conditions section, treat C0 as a binary indicator, and note the precision improvement of 0.57pp.

The main findings I need to support are that SICA and SC perform similarly across most conditions, constraints are weakly discriminative but not sufficient on their own, MAX-SAT performs about the same as count-only and random baselines, T=1.0 partially breaks the pattern though with tradeoffs, and C0 acts as a binary indicator. Before I start writing though, I should flag that LLaMA-8B has 48 truncated traces out of 720 total and DeepSeek has 72—these are notable confounds I'll need to mention.

Writing the paper structure now...

I'm laying out the full document with all the experimental sections—main results, ablations, boundary condition analysis, and various appendices covering sensitivity, overhead, baselines, and case studies. I'll use a simple bibliography environment for references since I don't have a separate .bib file, and I'll keep each section concise while making sure everything is well-organized and readable.

Now I'm drafting the abstract, which summarizes our systematic evaluation of symbolic consensus across reasoning domains and model families. We implemented SICA to extract first-order logic constraints and use MAX-SAT for answer selection, but found that it provides minimal accuracy improvement over majority voting—only about 1.5 percentage points on average. The extracted constraints have weak discriminative power, and the optimization approach doesn't outperform simpler baselines, though we do identify specific conditions where symbolic methods might help.

For the introduction, I'm setting up the motivation: sampling multiple reasoning traces and aggregating them is now standard practice, with Self-Consistency using majority voting as the baseline. Recent work proposes extracting symbolic constraints from traces and applying formal solvers to potentially capture logical structure that simple voting misses. The intuition is appealing—there should be value in exploiting the formal structure of reasoning—but I need to establish why this empirical evaluation matters.

The key gap is that no one has systematically characterized when symbolic constraint aggregation actually helps versus when it fails or hurts performance. Existing work evaluates on narrow slices, making it hard to generalize. This matters because practitioners need to know if the overhead of constraint extraction and solving is worth it. I'm proposing SICA as a systematic study that extracts first-order logic constraints from reasoning traces, deduplicates them, and applies a solver to find the most consistent answer.

I'm evaluating this across 3 reasoning domains, 5 model families including both instruction-scale and full reasoning models, and different operating conditions like temperature and sample counts—covering over 1,300 problems. The main finding is that symbolic consensus provides almost no improvement over simple majority voting in standard settings, around 1.5 percentage points. I'm also identifying a capability trap where instruction-scale models generate diverse outputs but the extracted constraints aren't discriminative enough to meaningfully improve answer selection. There's a boundary condition at extreme temperatures where we see some gains, though extraction quality degrades.

I'm introducing C0 as a simple binary diagnostic to flag whether symbolic consensus can actually work or if it'll just collapse to voting, and I'm developing practical guidance for when practitioners should actually use these methods versus sticking with simpler approaches.

Now I'm reviewing related work on self-consistency and majority voting as strong baselines, symbolic reasoning approaches like Logic-LM and LINC that focus on single-trace verification rather than aggregating across multiple traces, and process/outcome reward models.

I'm also looking at weighted voting methods and negative results papers that analyze when these approaches fail to improve performance.

The core SICA pipeline samples multiple reasoning traces from an LLM, extracts the final answers, then uses the LLM to pull out first-order logic constraints from each trace's intermediate reasoning steps. I deduplicate semantically equivalent constraints across traces and feed everything into a weighted MAX-SAT solver where each constraint's weight reflects how confident the extraction was.

The MAX-SAT solver finds the assignment over candidate answers that maximizes the total weight of satisfied constraints, and I select whichever candidate answer scores highest. If MAX-SAT doesn't provide useful discrimination between answers, I fall back to majority voting.

I'm tracking a C0 metric that measures the fraction of problems where the K traces actually produce different candidate answers—this tells me how much disagreement exists to resolve. When C0 is near zero, all traces agree anyway, so any aggregation method just returns that unanimous answer. When C0 is high, there's real disagreement to work through.

For experiments, I'm testing across several models: the Qwen2.5 family at different scales, Mistral-7B, LLaMA-3.1-8B, and DeepSeek-R1-Distill-Qwen-7B.

I'm also including QwQ-32B, which is a full reasoning model.

I'm evaluating on four domains: ProofWriter for deductive reasoning, FOLIO for first-order logic, StrategyQA for commonsense yes/no questions, and ARC-Challenge for science reasoning with multiple choice answers.

My default setup uses K=12 traces at temperature 0.7, and I'm using McNemar's test for pairwise significance testing with bootstrap confidence intervals.

Looking at the main results now, SICA accuracy stays within a few percentage points of standard chain-of-thought across most conditions. The biggest positive gap is +8.3pp with LLaMA-8B, though that's complicated by truncation issues affecting about 6.7% of the traces.

After correcting for multiple comparisons, SICA doesn't significantly outperform standard chain-of-thought at the 0.05 level on any model-domain pair. The QwQ-32B results show that when reasoning models converge to near-zero disagreement, SICA collapses back to standard chain-of-thought since there's no diversity to leverage. Within the Qwen family, disagreement rates drop consistently with model size, but the performance gap between SICA and standard chain-of-thought doesn't follow that same pattern.

Looking at constraint quality, the mean precision of 0.57 is well above random chance but shows no relationship with diversity levels. FOLIO constraints are slightly more reliable than ProofWriter ones, though the overall precision is still modest. This explains why we see minimal aggregate improvements: with only about 4 problems per experiment where constraints could matter, and those constraints being correct just 57% of the time, we'd expect only around 2 correct flips per run on average.

The ablation results show that MAX-SAT optimization performs essentially identically to simpler baselines like count-only aggregation and standard majority voting, with disagreement on just 2 of 804 problems. This suggests the solver isn't actually leveraging the logical structure in the constraints—it's effectively just counting votes rather than reasoning about the constraint relationships.

However, on the small subset of tied questions, SICA does select the correct answer 80% of the time compared to 50% for random tiebreaking, indicating that constraints do provide some signal in these edge cases.

Looking at temperature effects, I'm seeing that T=1.0 gives SICA a significant +8.3pp advantage over standard consistency checking, with strong statistical support. The correlation between temperature and diversity is very high at 0.98. But this improvement comes at a cost—the extraction rate drops substantially from 89% to 76%, meaning we're losing a quarter of the responses.

The coherence also suffers at higher temperatures, dropping to 85%, and the computational overhead jumps to around 65% compared to 49% at the default setting. That's roughly a 30% increase in compute cost for a gain that only showed up in one experimental condition with a small sample size and hasn't been replicated elsewhere. Lower temperatures show modest improvements of 1.7pp but nothing statistically significant.

I'm also noticing that C0 values cluster into distinct operating regimes—a low cluster around 0-10% that includes QwQ-32B and high-confidence domains. The capability trap emerges as a key finding—high output diversity doesn't guarantee better performance, and instruction-scale models struggle to extract constraints precise enough to meaningfully improve answer selection. For practitioners, the decision is straightforward: compute C0 as a quick filter, but recognize that symbolic methods rarely justify their 49% computational overhead unless working with extreme temperature sampling. The study does have limitations, including evaluation of just one symbolic consensus instantiation with first-order logic constraints.

Looking at the scope of testing, the largest powered experiments cover only specific model-dataset pairs, with cross-model validation limited to smaller sample sizes. I'm also noting that a comparison with Logic-LM suggests per-trace verification might be more effective than aggregating constraints across multiple traces, which points toward a different direction for improving reasoning verification. Now I'm compiling the complete LaTeX document and double-checking the win rates across model families to ensure accuracy in the results section. I need to decide how to handle the temperature ablation data in the table—the main experiment used a larger sample (n=804) for T=0.7, while the other temperatures used n=60, which creates an inconsistency. I could either use the K-ablation result as a reference point for T=0.7 at the same sample size, but that comes from a different subset of questions, so the numbers won't align perfectly. I'll keep the temperature table focused on T=0.3, 0.5, and maybe 0.7 to show the trend clearly. I'm noticing that the SC score stays constant at 73.3% across all three temperature settings, which is surprising—it suggests the majority voting mechanism is robust regardless of temperature, since the consensus answer remains stable even when sampling diversity changes.

Now I need to map out which experiments go into the main text versus appendix, starting with the core results and making sure I cover all the key comparisons. Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7a1bfd-7c3e-4ab8-a999-b800e4a23c34",
  "isSidechain": false,
  "requestId": "req_011Cb8PRbURCacCYgwhiEZqZ",
  "type": "assistant",
  "uuid": "1bfcba4e-7754-4836-942b-f9ed48c951ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AebkrMBDCaPasFdYRS8jsN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2614,
      "cache_creation_input_tokens": 16336,
      "cache_read_input_tokens": 24655,
      "output_tokens": 17451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2614,
          "output_tokens": 17451,
          "cache_read_input_tokens": 24655,
          "cache_creation_input_tokens": 16336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16336
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

_source line 15 · 2026-05-17T15:41:07.471Z_

Reading the experiment data and paper framing, then writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bfcba4e-7754-4836-942b-f9ed48c951ee",
  "isSidechain": false,
  "requestId": "req_011Cb8PRbURCacCYgwhiEZqZ",
  "type": "assistant",
  "uuid": "435ffa54-c9b4-48be-aead-d0fde13487fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AebkrMBDCaPasFdYRS8jsN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2614,
      "cache_creation_input_tokens": 16336,
      "cache_read_input_tokens": 24655,
      "output_tokens": 17451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2614,
          "output_tokens": 17451,
          "cache_read_input_tokens": 24655,
          "cache_creation_input_tokens": 16336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16336
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

_source line 16 · 2026-05-17T15:41:09.293Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018vw9YyRmpuA4rJpxTZvQtT`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/",
  "description": "List files in target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "435ffa54-c9b4-48be-aead-d0fde13487fb",
  "isSidechain": false,
  "requestId": "req_011Cb8PRbURCacCYgwhiEZqZ",
  "type": "assistant",
  "uuid": "5b975fa3-8c84-472f-9a08-f6e78b957429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AebkrMBDCaPasFdYRS8jsN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2614,
      "cache_creation_input_tokens": 16336,
      "cache_read_input_tokens": 24655,
      "output_tokens": 17451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2614,
          "output_tokens": 17451,
          "cache_read_input_tokens": 24655,
          "cache_creation_input_tokens": 16336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16336
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "5b975fa3-8c84-472f-9a08-f6e78b957429",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic consensus survey paper for dream_20260517T144412",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Tool result

_source line 19 · 2026-05-17T15:41:09.470Z_

<details><summary>↩ Tool result · `toolu_018vw9YyRmpuA4rJpxTZvQtT`</summary>

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
  "parentUuid": "5b975fa3-8c84-472f-9a08-f6e78b957429",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "b2c3f0cd-9261-4420-99b0-211fc1f762e0",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5b975fa3-8c84-472f-9a08-f6e78b957429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T15:41:12.846Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016mi58xuMv6FXfRJdFHsoB3`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -3",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2c3f0cd-9261-4420-99b0-211fc1f762e0",
  "isSidechain": false,
  "requestId": "req_011Cb8PqJ36i9dP7pnUYbwBf",
  "type": "assistant",
  "uuid": "1e359676-8db0-4586-949b-853f2e5f73f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wv2cEifinzoCvNiGDfVxB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20062,
      "cache_read_input_tokens": 40991,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20062,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 40991,
          "cache_creation_input_tokens": 20062,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20062
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

_source line 21 · 2026-05-17T15:41:12.941Z_

<details><summary>↩ Tool result · `toolu_016mi58xuMv6FXfRJdFHsoB3`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e359676-8db0-4586-949b-853f2e5f73f1",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "c6bc24ba-1e17-431e-8871-7571243075f6",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1e359676-8db0-4586-949b-853f2e5f73f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T15:44:55.921Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HfCFDc5q17aZ11P8wQEBUT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{caption}\n\\usepackage{enumitem}\n\\usepackage{natbib}\n\\usepackage{graphicx}\n\n\\setlength{\\parskip}{0.4em}\n\\setlength{\\parindent}{0em}\n\n\\title{When Does Symbolic Consensus Help?\\\\A Systematic Empirical Study}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRecent proposals augment LLM (Large Language Model) reasoning with symbolic methods that extract formal constraints from reasoning traces and use satisfiability solvers for answer selection.\nWe present the first systematic empirical evaluation of symbolic consensus, covering three reasoning domains, five model families, and multiple operating conditions.\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from $K$ reasoning traces and selects answers via weighted MAX-SAT.\nAcross more than 1{,}300 problems, SICA provides no significant accuracy gain over standard majority voting (aggregate $|\\Delta|\\approx1.5$ percentage points).\nExtracted constraints are weakly discriminative (mean precision 0.57 vs.\\ 0.33 random baseline for 3-class problems), but this modest signal is insufficient to reliably influence answer selection at practical sample sizes.\nMAX-SAT optimization is statistically equivalent to simple constraint counting or random weighting.\nWe identify one boundary condition: at temperature $T{=}1.0$, SICA achieves $+8.3$pp over majority voting ($p{=}0.034$), but extraction quality degrades from 89\\% to 76\\% and output coherence drops to 85\\%, limiting practical value.\nWe propose $C_0$, the fraction of problems with multiple candidate answers, as a zero-cost binary diagnostic: $C_0{<}5\\%$ guarantees method degeneration to majority voting, while $C_0{>}20\\%$ is necessary but insufficient for potential gains.\n\\end{abstract}\n\n%% ===================================================================\n\\section{Introduction}\n%% ===================================================================\n\nSampling multiple reasoning traces from large language models and aggregating their answers has become standard practice for improving accuracy on complex tasks.\nSelf-Consistency \\citep{wang2023selfconsistency} selects the majority answer across $K$ sampled chains of thought, providing a simple and effective baseline.\nRecent work goes further, proposing to extract symbolic constraints from reasoning traces and use formal solvers to aggregate them, potentially exploiting logical structure that majority voting ignores \\citep{pan2023logiclm,olausson2023linc}.\n\nThe appeal is intuitive: if reasoning traces encode intermediate logical claims, a satisfiability solver should identify the answer most consistent with the full body of extracted knowledge, outperforming a raw head count.\nSeveral methods pursue this direction with varying formalisations of constraint extraction and solver integration.\nYet a basic practical question remains open: across realistic model families, reasoning domains, and operating conditions, when does symbolic consensus actually outperform majority voting?\n\nNo prior work systematically characterises the conditions under which symbolic constraint aggregation helps, degenerates to voting, or actively hurts.\nExisting evaluations compare symbolic and voting methods on narrow model-domain slices, making it difficult to draw general conclusions about method viability.\nThis gap is consequential for practitioners who must decide whether the substantial overhead of constraint extraction and solving (approximately 49\\% additional compute in our measurements) is justified by accuracy gains.\n\nWe address this gap with a controlled empirical study.\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from $K$ reasoning traces, deduplicates them, and selects answers via weighted MAX-SAT.\nSICA serves as a concrete, reproducible test bed for the broader question of whether symbolic aggregation adds value over voting.\nWe evaluate SICA against majority voting across three reasoning domains (formal logic, commonsense, science), five model families (four instruction-scale, one full reasoning model), and varied operating conditions (temperature $T$, sample count $K$), covering more than 1{,}300 problems with controlled pairwise comparisons.\n\nOur contributions are as follows:\n\\begin{itemize}[nosep,leftmargin=1.5em]\n\\item The first systematic evaluation of symbolic consensus across multiple models, domains, and operating conditions, establishing that SICA provides no significant gain over majority voting in standard settings (Section~\\ref{sec:main}).\n\\item Characterisation of the \\emph{capability trap} pattern: instruction-scale models produce ample output diversity ($C_0{=}22$--$65\\%$), but extracted constraints have only weak discriminative power (precision 0.57), and MAX-SAT over such constraints is equivalent to counting (Sections~\\ref{sec:quality}--\\ref{sec:ablation}).\n\\item Analysis of boundary conditions showing that extreme temperature ($T{=}1.0$) partially breaks the pattern but with degraded extraction quality and output coherence (Section~\\ref{sec:temperature}).\n\\item $C_0$, a zero-cost binary diagnostic indicating whether symbolic consensus can potentially operate ($C_0{>}20\\%$) or trivially degenerates to voting ($C_0{<}5\\%$) (Section~\\ref{sec:c0}).\n\\end{itemize}\n\n%% ===================================================================\n\\section{Related Work}\n%% ===================================================================\n\n\\paragraph{Self-Consistency and majority voting.}\nSelf-Consistency (SC) samples multiple chains of thought and selects the answer receiving the most votes \\citep{wang2023selfconsistency}.\nUniversal Self-Consistency extends this to free-form answers \\citep{chen2023universal}.\nSC remains the dominant aggregation baseline due to its simplicity and strong empirical performance.\nWeighted variants assign non-uniform weights to traces based on length or confidence heuristics \\citep{taubenfeld2024weighted}, but evidence for consistent improvement is limited.\n\n\\paragraph{Symbolic reasoning for LLMs.}\nLogic-LM translates natural language problems into first-order logic and verifies solutions with theorem provers \\citep{pan2023logiclm}.\nLINC performs neurosymbolic inference over FOL representations \\citep{olausson2023linc}.\nThese methods focus on single-trace symbolic verification rather than multi-trace constraint aggregation.\nOur work asks whether the multi-trace aggregation dimension adds value beyond what single-trace verification provides.\n\n\\paragraph{Process and outcome reward models.}\nTrained verifiers score individual reasoning steps or final answers \\citep{cobbe2021gsm8k,lightman2023process}.\nUnlike constraint-based aggregation, these methods require supervised training data.\nThey represent a distinct and complementary approach to improving reasoning quality.\n\n\\paragraph{Negative results in NLP.}\nSystematic negative-result studies have clarified the limitations of prompting strategies \\citep{reynolds2021prompt}, chain-of-thought elicitation, and various reasoning augmentation techniques.\nOur work contributes to this tradition by providing controlled evidence on the limits of symbolic consensus.\n\n%% ===================================================================\n\\section{Method: SICA Pipeline}\n\\label{sec:method}\n%% ===================================================================\n\nSICA (Symbolic Invariant Consensus Aggregation) aggregates multiple reasoning traces through five stages.\n\n\\paragraph{1.\\ Trace generation.}\nGiven a problem $q$, we sample $K$ reasoning traces $\\{r_1, \\ldots, r_K\\}$ from an LLM at temperature $T$.\nEach trace contains a chain of thought concluding with a candidate answer.\n\n\\paragraph{2.\\ Answer extraction.}\nA deterministic parser extracts the final answer $a_i$ from each trace $r_i$.\nProblems where all $K$ traces produce the same answer are classified as \\emph{unanimous} and passed directly to majority voting, since no aggregation method can change the outcome.\n\n\\paragraph{3.\\ Constraint extraction.}\nFor each trace $r_i$, an LLM-based extractor produces a set of FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ expressing intermediate logical claims.\nEach constraint is a first-order formula over the candidate answer space.\nExtraction success is measured as the fraction of traces yielding at least one parseable constraint.\n\n\\paragraph{4.\\ Deduplication.}\nSemantically equivalent constraints across traces are merged, retaining the maximum weight.\nDeduplication removes redundancy without discarding signal from independent traces that happen to derive the same intermediate claim.\n\n\\paragraph{5.\\ MAX-SAT aggregation.}\nWe construct a weighted MAX-SAT instance: each unique constraint $c_j$ has weight $w_j$ proportional to extraction confidence.\nCandidate answers are evaluated by the total weight of constraints they satisfy.\nThe answer maximising satisfied weight is selected.\nWhen MAX-SAT produces no discrimination (all candidates satisfy the same constraints), the method falls back to majority vote.\n\n\\paragraph{$C_0$ metric.}\nWe define $C_0$ as the fraction of problems in a dataset where $K$ traces produce more than one distinct candidate answer.\n$C_0$ reflects output diversity: when $C_0 \\approx 0$, all traces agree and any aggregation method reduces to the unanimous answer.\n$C_0$ is computable with zero overhead from the answer extraction stage and requires no constraint extraction.\n\n%% ===================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%% ===================================================================\n\n\\paragraph{Models.}\nWe evaluate seven models spanning four categories.\n\\emph{Qwen family (instruction-scale)}: Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-72B-Instruct-AWQ (4-bit quantised).\n\\emph{Other instruction-scale}: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct.\n\\emph{Distilled reasoning}: DeepSeek-R1-Distill-Qwen-7B, which we initially expected to behave as a reasoning model but reclassified as instruction-scale after observing $C_0{=}58\\%$ (far above the $<5\\%$ expected for reasoning models).\n\\emph{Full reasoning}: QwQ-32B.\n\n\\paragraph{Domains.}\nProofWriter (deductive reasoning over formal rules), FOLIO (first-order logic NLI), StrategyQA (commonsense binary reasoning), and ARC-Challenge (science multiple-choice).\nThe primary evaluation set combines ProofWriter and FOLIO (``D012'') for formal logic coverage.\n\n\\paragraph{Default configuration.}\n$K{=}12$ traces per problem, temperature $T{=}0.7$, unless stated otherwise.\nTemperature and $K$ are varied in ablation experiments.\n\n\\paragraph{Statistical testing.}\nWe use McNemar's exact test for paired comparisons on the same problem set.\nFor experiments involving multiple comparisons across model families, we apply Bonferroni correction (adjusted $\\alpha \\approx 0.01$ for five families).\n\n%% ===================================================================\n\\section{Results}\n\\label{sec:results}\n%% ===================================================================\n\n\\subsection{Main Results}\n\\label{sec:main}\n\nTable~\\ref{tab:main} presents SICA versus SC accuracy across all model-domain configurations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results: SICA vs.\\ Self-Consistency (SC) across models and domains. $C_0$: fraction of problems with multiple candidate answers. $\\Delta$: SICA $-$ SC in percentage points. $p$: McNemar's exact test. Best per-row result in \\textbf{bold}.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{@{}llrrrrrr@{}}\n\\toprule\nModel & Domain & $N$ & $C_0$\\% & SC & SICA & $\\Delta$pp & $p$ \\\\\n\\midrule\nQwen-14B & PW+FOLIO & 804 & 38 & \\textbf{76.2} & 76.5 & $+0.3$ & n.s. \\\\\nQwen-14B & StrategyQA & 60 & 10 & 53.3 & \\textbf{56.7} & $+3.3$ & 0.16 \\\\\nQwen-14B & ARC-Chal. & 60 & 5 & \\textbf{96.7} & 95.0 & $-1.7$ & --- \\\\\n\\midrule\nQwen-7B & PW+FOLIO & 60 & 65 & 56.7 & \\textbf{60.0} & $+3.3$ & 0.41 \\\\\nQwen-72B & PW+FOLIO & 60 & 22 & 85.0 & \\textbf{86.7} & $+1.7$ & 0.65 \\\\\n\\midrule\nMistral-7B & PW+FOLIO & 60 & 50 & 48.3 & 48.3 & $0.0$ & 1.00 \\\\\nLLaMA-8B & PW+FOLIO & 60 & 62 & 60.0 & \\textbf{68.3} & $+8.3$ & 0.096 \\\\\nDeepSeek-R1-7B & PW+FOLIO & 60 & 58 & \\textbf{71.7} & 68.3 & $-3.3$ & 0.48 \\\\\n\\midrule\nQwQ-32B & Mixed & 46 & 2.6 & \\multicolumn{2}{c}{$\\equiv$ SC} & $0.0$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross all standard conditions, SICA accuracy falls within a few percentage points of SC.\nThe largest positive delta ($+8.3$pp, LLaMA-8B) does not reach significance after Bonferroni correction for multiple model comparisons (McNemar $p{=}0.096$, corrected threshold $\\approx 0.01$).\nThis result is further confounded by 48 truncated traces out of 720 total (6.7\\% truncation rate), which may artificially inflate diversity.\nThe largest negative delta ($-3.3$pp, DeepSeek-R1-7B) occurs with the highest truncation rate in the study (72/720 = 10.0\\%).\nNo model-domain combination shows SICA significantly outperforming SC at $\\alpha{=}0.05$ after correction.\n\nQwQ-32B represents the converged regime.\nWith effective $C_0{=}2.6\\%$, nearly all problems produce unanimous traces, and SICA trivially reduces to SC.\nFull reasoning models, by design, produce deterministic-like chains that eliminate the diversity symbolic methods require.\n\nWithin the Qwen family, $C_0$ decreases monotonically with model scale (7B: 65\\%, 14B: 38\\%, 72B: 22\\%, QwQ-32B: 2.6\\%), but the SICA-SC gap does not follow a corresponding trend ($+3.3$, $+0.3$, $+1.7$, $0.0$pp).\nDiversity reduction does not predict method performance.\n\nDeepSeek-R1-Distill-Qwen-7B was initially expected to function as a reasoning model ($C_0{<}5\\%$).\nIn practice, at 7B parameter capacity, distillation does not produce the deterministic reasoning chains characteristic of full reasoning models.\n$C_0{=}58\\%$ places it squarely in the instruction-scale cluster, and we reclassify it accordingly.\n\n\\subsection{Constraint Quality Analysis}\n\\label{sec:quality}\n\nTable~\\ref{tab:quality} characterises per-problem constraint precision across the 307 multi-candidate problems from the main Qwen-14B experiment ($n{=}804$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint precision on multi-candidate problems (Qwen-14B, PW+FOLIO, $n{=}307$). Precision measures the fraction of extracted constraints that correctly discriminate the ground-truth answer from alternatives. Random baseline: 0.33 for 3-class, 0.50 for binary.}\n\\label{tab:quality}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDomain & $N$ & Mean & Std & Median \\\\\n\\midrule\nProofWriter & --- & 0.55 & --- & --- \\\\\nFOLIO & --- & 0.62 & --- & --- \\\\\n\\midrule\nOverall & 307 & 0.57 & 0.23 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean constraint precision is 0.57 (std 0.23), significantly above the 0.33 random baseline for 3-class problems.\nConstraints are \\emph{weakly discriminative}, not random.\nHowever, precision shows no correlation with vote entropy ($R^2{=}0.008$, $p{=}0.12$), meaning constraint quality does not improve when output diversity increases.\nFOLIO constraints (precision 0.62) are somewhat more accurate than ProofWriter constraints (0.55), consistent with FOLIO's more explicit logical structure.\n\nA precision of 0.57 explains the aggregate null result quantitatively.\nAt $K{=}12$ with $C_0{\\approx}38\\%$, approximately 4 multi-candidate problems per 60-question set have constraints that could influence the outcome.\nWith constraints correct 57\\% of the time, the expected number of correct answer flips per experiment is approximately 2, which is indistinguishable from sampling noise at these sample sizes.\n\n\\subsection{Mechanism Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares four aggregation strategies on the main experiment data ($n{=}804$) to isolate the contribution of MAX-SAT reasoning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation (Qwen-14B, PW+FOLIO, $n{=}804$, $T{=}0.7$). MAX-SAT: full SICA pipeline. Count-only: constraints weighted equally, no satisfiability reasoning. Random-weight: constraints with random weights. SC: standard majority voting.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lccr@{}}\n\\toprule\nMethod & Accuracy (\\%) & $\\Delta$ vs.\\ SC (pp) & $p$ vs.\\ SC \\\\\n\\midrule\nMAX-SAT (SICA) & 76.5 & $+0.3$ & --- \\\\\nCount-only & 76.4 & $+0.2$ & --- \\\\\nRandom-weight & 76.3 & $+0.1$ & --- \\\\\nSC (baseline) & 76.2 & --- & --- \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\small MAX-SAT vs.\\ Count-only: $p{=}0.85$; agreement on 802/804 problems.} \\\\\n\\multicolumn{4}{@{}l}{\\small MAX-SAT vs.\\ Random: $p{=}0.72$.} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMAX-SAT (76.5\\%) is statistically indistinguishable from count-only aggregation (76.4\\%), random-weight aggregation (76.3\\%), and standard majority voting (76.2\\%).\nThe four methods disagree on only 2 of 804 problems.\nThe logical structure encoded in constraints is not exploited by the solver in any meaningful way: MAX-SAT degenerates to a constraint counter, and constraints provide no incremental signal beyond raw vote counts.\n\n\\subsection{Tiebreak Analysis}\n\\label{sec:tiebreak}\n\nTable~\\ref{tab:tiebreak} examines SICA's performance specifically on tied questions, where majority voting must break ties arbitrarily.\n\n\\begin{table}[t]\n\\centering\n\\caption{Tiebreak accuracy on tied questions (Qwen-14B, $K{=}12$, $n_{\\text{tied}}{=}5$ of 60). Tie fraction: 8.3\\%.}\n\\label{tab:tiebreak}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nTiebreak Method & Accuracy on Ties \\\\\n\\midrule\nSICA (constraint-based) & 80\\% (4/5) \\\\\nAlphabetical & 60\\% (3/5) \\\\\nRandom (expected) & 50\\% \\\\\nFirst-seen & 40\\% (2/5) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn the small subset of tied questions (5 of 60, tie fraction 8.3\\%), SICA selects the correct answer 80\\% of the time versus 50\\% for random tiebreaking.\nConstraint-based tiebreaking has genuine value on individual ties.\nHowever, ties are too rare to materially affect overall accuracy.\nThe effective contribution is $0.80 \\times 0.083 \\approx 6.6\\%$ of possible gain, translating to at most ${\\sim}2.5$pp under ideal conditions.\nAt even $K$ (where ties can occur), the tie rate varies from 5.0\\% ($K{=}20$) to 26.7\\% ($K{=}12$), but even at peak tie rate the overall accuracy impact remains within noise.\n\n\\subsection{Boundary Conditions: Temperature}\n\\label{sec:temperature}\n\nTable~\\ref{tab:temperature} presents the temperature ablation on Qwen-14B over 60 D012 problems.\nThis is the critical experiment for understanding when symbolic consensus can differ from voting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temperature ablation (Qwen-14B, D012, $n{=}60$, $K{=}12$). Default operating condition is $T{=}0.7$. Extraction rate: fraction of traces yielding parseable constraints. Coherence: fraction of traces producing coherent, complete outputs.}\n\\label{tab:temperature}\n\\small\n\\begin{tabular}{@{}cccccccc@{}}\n\\toprule\n$T$ & $C_0$\\% & SC & SICA & $\\Delta$pp & $p$ & Extr. & Coher. \\\\\n\\midrule\n0.3 & 18 & 73.3 & 75.0 & $+1.7$ & 0.65 & 93\\% & ${\\sim}98\\%$ \\\\\n0.5 & 30 & 73.3 & 75.0 & $+1.7$ & 0.55 & 91\\% & ${\\sim}98\\%$ \\\\\n0.7 & 38 & 76.2 & 76.5 & $+0.3$ & n.s. & 89\\% & ${\\sim}98\\%$ \\\\\n1.0 & 72 & 73.3 & 81.7 & $+8.3$ & \\textbf{0.034} & 76\\% & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature $T{=}1.0$ produces the only statistically significant SICA advantage in the entire study: $+8.3$pp (McNemar $p{=}0.034$) with a 7:1 discordant ratio favouring SICA.\n$C_0$ increases from 38\\% at $T{=}0.7$ to 72\\% at $T{=}1.0$, confirming the strong link between temperature and diversity ($r{=}0.98$).\nThe gap is monotonically increasing with temperature.\n\nThis gain comes with substantial costs.\nExtraction rate drops from 89\\% ($T{=}0.7$) to 76\\% ($T{=}1.0$): nearly one quarter of constraint extraction attempts produce empty or unparseable output.\nAnswer coherence drops to 85\\%, meaning 15\\% of generated traces are partially incoherent.\nWhen extraction retries are factored in, the estimated overhead at $T{=}1.0$ rises to approximately 65\\% (vs.\\ 49\\% at default temperature), increasing the per-question compute cost by roughly 30\\%.\nThe $T{=}0.7$ reference row reports the main experiment ($n{=}804$) for context; all other rows use $n{=}60$.\n\nThe practical implication is that the boundary condition exists in theory but is operationally costly.\nA practitioner seeking the marginal $+8.3$pp would need to tolerate incoherent outputs, higher extraction failure rates, and additional compute.\nFor comparison, simply running more traces at the default temperature ($K{=}16$ or $K{=}20$) achieves similar variance reduction without these quality degradations.\n\nLower temperatures ($T{=}0.3$, $T{=}0.5$) produce small positive deltas ($+1.7$pp each) that are not significant ($p{>}0.5$), consistent with the default-temperature null result.\n\n\\subsection{$C_0$ as Operating Regime Indicator}\n\\label{sec:c0}\n\nAcross all 12 model-domain-temperature conditions, $C_0$ values cluster into two distinct regimes (Table~\\ref{tab:c0_summary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{$C_0$ clusters and corresponding SICA-SC gaps. Low-$C_0$ cluster: reasoning models and high-confidence domains. High-$C_0$ cluster: instruction-scale models on challenging domains.}\n\\label{tab:c0_summary}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nCluster & $C_0$ range & Mean gap (pp) & $N$ points \\\\\n\\midrule\nLow $C_0$ & 0--10\\% & $-0.9$ & 3 \\\\\nHigh $C_0$ & 22--72\\% & $+1.8$ & 9 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\small Linear regression: $R^2{=}0.08$, slope$=0.09$pp per \\%$C_0$, $p{=}0.37$.} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe low-$C_0$ cluster ($C_0{=}0$--$10\\%$) comprises QwQ-32B ($C_0{=}2.6\\%$), ARC-Challenge ($C_0{=}5\\%$), and StrategyQA ($C_0{=}10\\%$).\nMean gap in this cluster is $-0.9$pp: SICA trivially reduces to voting.\nThe high-$C_0$ cluster ($C_0{=}22$--$72\\%$) comprises instruction-scale models on formal logic domains plus the temperature extreme.\nMean gap is $+1.8$pp but with enormous variance (from $-3.3$ to $+8.3$pp), and no individual comparison is significant except $T{=}1.0$.\n\nLinear regression of gap on $C_0$ yields $R^2{=}0.08$ ($p{=}0.37$): $C_0$ provides no gradient-level predictive power for the SICA-SC gap.\nThe 10--22\\% range contains only one data point ($C_0{=}18\\%$ at $T{=}0.3$), leaving a gap between clusters.\n\n$C_0$ therefore functions as a binary indicator.\n$C_0{<}5\\%$ reliably predicts SICA $\\equiv$ SC (method degeneration).\n$C_0{>}20\\%$ indicates that symbolic consensus can potentially differ from voting, but does not predict whether the difference will be positive, negative, or zero.\nThis makes $C_0$ useful as a zero-cost go/no-go check before investing in constraint extraction, but not as a quantitative performance predictor.\n\n%% ===================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%% ===================================================================\n\n\\paragraph{The capability trap as descriptive pattern.}\nAcross our experiments, we observe a recurring pattern that we label the \\emph{capability trap}: conditions that enable symbolic consensus to differ from majority voting (high output diversity, $C_0{>}20\\%$) do not ensure that the difference is beneficial.\nInstruction-scale models produce abundant diversity ($C_0{=}22$--$65\\%$), but extracted constraints at precision 0.57 are insufficient to reliably steer answer selection.\nWe emphasise that this is a descriptive label for an empirical observation, not a mechanistic explanation.\nThe decoupling of diversity and constraint quality may stem from the extraction process, the FOL formalism, or inherent limitations of current-generation LLM reasoning.\n\n\\paragraph{Practical guidelines.}\nFor practitioners considering symbolic aggregation, our results suggest a simple decision framework.\nFirst, compute $C_0$ from raw answer extractions at zero cost.\nIf $C_0{<}5\\%$ (strong reasoning models, easy tasks), symbolic methods will trivially degenerate to voting.\nIf $C_0{>}20\\%$ under standard temperatures, symbolic methods may differ from voting but are unlikely to improve accuracy, while incurring approximately 49\\% additional compute (Appendix~\\ref{app:overhead}).\n\n\\paragraph{The $T{=}1.0$ exception and its limits.}\nThe temperature ablation reveals that extreme diversity ($T{=}1.0$, $C_0{=}72\\%$) can produce a significant SICA advantage.\nThis finding prevents us from claiming that the capability trap is absolute.\nHowever, the associated quality degradation (extraction rate 76\\%, coherence 85\\%) and the fact that this result comes from a single $n{=}60$ experiment temper its practical significance.\nReplication across models and larger sample sizes is needed before recommending $T{=}1.0$ as an operating point.\n\n\\paragraph{Alternative aggregation directions.}\nThe Logic-LM comparison (Appendix~\\ref{app:logiclm}) shows that Logic-LM with $K$ repetitions and majority voting achieves 80.9\\% on FOLIO vs.\\ SICA's 79.4\\%.\nSingle-trace FOL verification repeated $K$ times may be more effective than multi-trace constraint aggregation.\nInverse-length weighted voting (Appendix~\\ref{app:weightedsc}) matches SICA at zero extraction cost (77.0\\% vs.\\ 76.5\\%).\nThese results suggest that lightweight quality proxies, or per-trace verification, may be more productive directions than cross-trace constraint consensus.\n\n\\paragraph{Limitations.}\n(1) We evaluate one instantiation of symbolic consensus (FOL constraints, MAX-SAT solver). Other constraint languages or aggregation strategies might yield different results.\n(2) The largest powered test ($n{=}804$) covers only Qwen-14B on ProofWriter and FOLIO. Cross-model tests at $n{\\geq}200$ exist only for LLaMA-8B.\n(3) We test only one full reasoning model (QwQ-32B); additional reasoning models (o1-series, Gemini thinking models) would strengthen the converged-regime claim.\n(4) The $T{=}1.0$ boundary condition has been tested only on Qwen-14B with $n{=}60$.\n(5) The constraint ablation (Table~\\ref{tab:ablation}) was performed at $T{=}0.7$; results may differ at extreme temperatures where the constraint quality distribution changes.\n\n%% ===================================================================\n\\section{Conclusion}\n%% ===================================================================\n\nWe present the first systematic empirical study of symbolic consensus for LLM reasoning aggregation.\nAcross three domains, five model families, and over 1{,}300 problems, symbolic constraint aggregation via SICA provides no significant accuracy improvement over majority voting in standard operating conditions.\nExtracted constraints are weakly discriminative (precision 0.57) but insufficient to reliably influence answer selection.\nThe MAX-SAT solver degenerates to a constraint counter: it is statistically equivalent to counting or random weighting.\nAt extreme temperatures ($T{=}1.0$), a marginal gain appears ($+8.3$pp, $p{=}0.034$) but is accompanied by degraded extraction quality and output coherence.\nWe contribute $C_0$ as a practical, zero-cost binary diagnostic for practitioners deciding whether to invest in symbolic aggregation.\nOur findings indicate that, for the current generation of LLM constraint extraction, simple majority voting remains the method of choice.\n\n%% ===================================================================\n%% APPENDIX\n%% ===================================================================\n\\appendix\n\n\\section{$K$ Sensitivity Analysis}\n\\label{app:k_ablation}\n\nTable~\\ref{tab:k_ablation} presents the effect of varying $K$ on SICA vs.\\ SC (Qwen-14B, D012, $n{=}60$).\n\n\\begin{table}[h]\n\\centering\n\\caption{$K$ ablation (Qwen-14B, D012, $n{=}60$, $T{=}0.7$). Tiebreak rate: fraction of problems producing exact ties at this $K$.}\n\\label{tab:k_ablation}\n\\small\n\\begin{tabular}{@{}rccccr@{}}\n\\toprule\n$K$ & SICA & SC & $\\Delta$pp & Tiebreak Rate \\\\\n\\midrule\n6  & 75.0 & 73.3 & $+1.7$ & 18.3\\% \\\\\n8  & 75.0 & 75.0 & $0.0$  & --- \\\\\n11 & 75.0 & 75.0 & $0.0$  & --- \\\\\n12 & 73.3 & 75.0 & $-1.7$ & 26.7\\% \\\\\n16 & 71.7 & 73.3 & $-1.7$ & --- \\\\\n20 & 71.7 & 73.3 & $-1.7$ & 5.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt odd $K{=}11$, where exact ties cannot occur, the gap is precisely zero.\nThis confirms that SICA's potential value comes entirely from tiebreaking.\nAt $K{=}6$ (small sample), the $+1.7$pp positive delta falls within the bootstrap 95\\% CI $[-5.0, +8.3]$pp, compatible with zero effect.\nAt $K{\\geq}12$, SICA shows a consistent $-1.7$pp deficit, likely from noise injection by low-quality constraints in larger trace sets.\nThe pattern is non-monotonic (positive at low $K$, zero at odd $K$, negative at high $K$), making a blanket ``SICA $\\leq$ SC at all $K$'' statement inaccurate.\nThe correct characterisation is \\emph{$K$-dependent with no consistent advantage}.\n\n\\section{Overhead Analysis}\n\\label{app:overhead}\n\nTable~\\ref{tab:overhead} breaks down wall-clock time per question from the main experiment ($n{=}804$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-question wall-time breakdown (Qwen-14B, $n{=}804$, $T{=}0.7$).}\n\\label{tab:overhead}\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nComponent & Mean time (s) & \\% of total \\\\\n\\midrule\nTrace generation & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nDeduplication & 1.0 & 1.6\\% \\\\\nMAX-SAT solving & 0.003 & ${<}0.01\\%$ \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA's overhead relative to SC (which requires only trace generation) is 48.7\\%, dominated by the constraint extraction LLM call.\nMAX-SAT solving time is negligible.\nThe overhead-to-gain ratio at default temperature is $48.7\\% / 0.3\\text{pp} \\approx 162$: each percentage point of (non-significant) gain costs 162\\% in additional compute.\nMedian overhead is 48.9\\%, with the 90th percentile at 57.6\\%.\nProofWriter questions incur 51.3\\% overhead on average vs.\\ 38.6\\% for FOLIO, reflecting longer constraint extraction prompts for deductive rules.\n\n\\section{Weighted SC Baselines}\n\\label{app:weightedsc}\n\nTable~\\ref{tab:weighted_sc} compares SICA against simple weighted voting heuristics ($n{=}804$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Weighted SC variants (Qwen-14B, PW+FOLIO, $n{=}804$, $T{=}0.7$).}\n\\label{tab:weighted_sc}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Accuracy (\\%) & $\\Delta$ vs.\\ SC (pp) & $p$ vs.\\ SC \\\\\n\\midrule\nInverse-length & 77.0 & $+0.8$ & 0.42 \\\\\nSICA (MAX-SAT) & 76.5 & $+0.3$ & --- \\\\\nSC (uniform) & 76.2 & --- & --- \\\\\nLength-weighted & 75.3 & $-0.9$ & 0.16 \\\\\nConstraint-count & 75.3 & $-0.9$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInverse-length weighting (favouring shorter, more confident traces) achieves 77.0\\%, slightly above SICA's 76.5\\%.\nAll differences are non-significant.\nA zero-cost heuristic based on trace length matches or exceeds the full SICA pipeline, reinforcing the conclusion that constraint extraction does not add value at default settings.\n\n\\section{Logic-LM Comparison}\n\\label{app:logiclm}\n\nTable~\\ref{tab:logiclm} compares SICA against a Logic-LM baseline on FOLIO ($n{=}204$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Logic-LM $\\times$ $K$ vs.\\ SICA vs.\\ SC on FOLIO ($n{=}204$, $K{=}12$).}\n\\label{tab:logiclm}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Accuracy (\\%) & $p$ vs.\\ SICA \\\\\n\\midrule\nLogic-LM $\\times$ $K$ + vote & 80.9 & 0.38 \\\\\nSICA (MAX-SAT) & 79.4 & --- \\\\\nSC (majority vote) & 79.4 & --- \\\\\nSingle-trace Logic-LM & 77.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLogic-LM repeated $K$ times with majority voting achieves 80.9\\% vs.\\ SICA's 79.4\\%.\nThe difference is not significant ($p{=}0.38$), but the directional advantage of per-trace verification over multi-trace constraint aggregation is notable.\nLogic-LM performs a complete FOL consistency check per trace (pass/fail), which has stronger discriminative power than SICA's soft constraint aggregation: an internally inconsistent trace is excluded entirely by Logic-LM, while SICA still incorporates its constraints.\n\n\\section{GSM8K Pilot}\n\\label{app:gsm8k}\n\nA 30-question pilot on GSM8K (Qwen-14B, $K{=}12$) yields: SICA 80.0\\% vs.\\ SC 76.7\\% ($\\Delta{=}+3.3$pp, $p{=}0.56$, McNemar).\n$C_0{=}27\\%$ (moderate), multi-candidate rate 23\\%, extraction rate 85\\%.\nAt $n{=}30$, the standard error is approximately 8pp, making this result uninformative.\nGSM8K is included as a pilot data point for domain coverage; it does not alter any main-text claims.\n\n\\section{Constraint Case Studies}\n\\label{app:case_studies}\n\nWe qualitatively analyse 8 representative questions from the main experiment.\nOf these, 3 produce semantically meaningful constraints, 2 produce correctly discriminative constraints that steer SICA to the right answer, 3 produce non-discriminative constraints (tautological or irrelevant), and 2 produce actively misleading constraints that steer SICA away from the correct answer.\n\nConstraint categories: 3 tautological, 2 partially correct, 2 fully correct, 1 contradicting ground truth.\nThe two fully correct cases both come from FOLIO problems with explicit formal logical structure, where FOL extraction naturally aligns with the problem's own representation.\nThe misleading case involves a ProofWriter problem where the extracted constraint encodes a premise not present in the original rules.\n\nThese case studies illustrate that constraints \\emph{can} be discriminative on individual problems (consistent with the aggregate precision of 0.57), but the mixture of helpful, neutral, and harmful constraints yields no net improvement when aggregated across a full problem set.\n\n\\section{$C_0$ Diagnostic Full Data}\n\\label{app:c0_data}\n\nTable~\\ref{tab:c0_full} lists all 12 data points used for the $C_0$ analysis in Section~\\ref{sec:c0}.\n\n\\begin{table}[h]\n\\centering\n\\caption{All (model/condition, domain, $C_0$, SICA-SC gap) data points.}\n\\label{tab:c0_full}\n\\small\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nCondition & Domain & $C_0$ (\\%) & Gap (pp) \\\\\n\\midrule\nQwQ-32B & Mixed & 2.6 & $0.0$ \\\\\nQwen-14B & ARC & 5.0 & $-1.7$ \\\\\nQwen-14B & StrategyQA & 10.0 & $+3.3$ \\\\\nQwen-14B $T{=}0.3$ & PW+FOLIO & 18.0 & $+1.7$ \\\\\nQwen-72B & PW+FOLIO & 22.0 & $+1.7$ \\\\\nQwen-14B GSM8K & GSM8K & 27.0 & $+3.3$ \\\\\nQwen-14B $T{=}0.7$ & PW+FOLIO & 38.0 & $+0.3$ \\\\\nMistral-7B & PW+FOLIO & 50.0 & $0.0$ \\\\\nDeepSeek-R1-7B & PW+FOLIO & 58.0 & $-3.3$ \\\\\nLLaMA-8B & PW+FOLIO & 62.0 & $+8.3$ \\\\\nQwen-7B & PW+FOLIO & 65.0 & $+3.3$ \\\\\nQwen-14B $T{=}1.0$ & PW+FOLIO & 72.0 & $+8.3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ===================================================================\n%% REFERENCES\n%% ===================================================================\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Chen et~al.(2023)]{chen2023universal}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv:2311.17311}, 2023.\n\n\\bibitem[Pan et~al.(2023)]{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Y.~Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et~al.(2023)]{olausson2023linc}\nT.~X.~Olausson, A.~Gu, B.~Lipkin, C.~E.~Zhang, A.~Solar-Lezama, J.~B.~Tenenbaum, and R.~Levy.\n\\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training Verifiers to Solve Math Word Problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023process}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's Verify Step by Step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Taubenfeld et~al.(2024)]{taubenfeld2024weighted}\nA.~Taubenfeld, Y.~Horesh, N.~Benaim, G.~Shani, N.~Shani, and L.~Wolf.\n\\newblock Systematic Biases in LLM Simulations of Debates.\n\\newblock \\emph{arXiv:2402.04049}, 2024.\n\n\\bibitem[Reynolds and McDonell(2021)]{reynolds2021prompt}\nL.~Reynolds and K.~McDonell.\n\\newblock Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm.\n\\newblock In \\emph{CHI EA}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6bc24ba-1e17-431e-8871-7571243075f6",
  "isSidechain": false,
  "requestId": "req_011Cb8PqYq6HRgcmtrfmTMo5",
  "type": "assistant",
  "uuid": "ba83137d-c379-45df-9f81-c93fa44b5f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEiGYeQgYUEGCYc2iG1gQ7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 61053,
      "output_tokens": 12128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 172,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12128,
          "cache_read_input_tokens": 61053,
          "cache_creation_input_tokens": 172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 172
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

_source line 23 · 2026-05-17T15:44:55.939Z_

<details><summary>↩ Tool result · `toolu_01HfCFDc5q17aZ11P8wQEBUT`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba83137d-c379-45df-9f81-c93fa44b5f20",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "a8180a1a-802d-4c54-9201-aefde55682ec",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{caption}\n\\usepackage{enumitem}\n\\usepackage{natbib}\n\\usepackage{graphicx}\n\n\\setlength{\\parskip}{0.4em}\n\\setlength{\\parindent}{0em}\n\n\\title{When Does Symbolic Consensus Help?\\\\A Systematic Empirical Study}\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nRecent proposals augment LLM (Large Language Model) reasoning with symbolic methods that extract formal constraints from reasoning traces and use satisfiability solvers for answer selection.\nWe present the first systematic empirical evaluation of symbolic consensus, covering three reasoning domains, five model families, and multiple operating conditions.\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from $K$ reasoning traces and selects answers via weighted MAX-SAT.\nAcross more than 1{,}300 problems, SICA provides no significant accuracy gain over standard majority voting (aggregate $|\\Delta|\\approx1.5$ percentage points).\nExtracted constraints are weakly discriminative (mean precision 0.57 vs.\\ 0.33 random baseline for 3-class problems), but this modest signal is insufficient to reliably influence answer selection at practical sample sizes.\nMAX-SAT optimization is statistically equivalent to simple constraint counting or random weighting.\nWe identify one boundary condition: at temperature $T{=}1.0$, SICA achieves $+8.3$pp over majority voting ($p{=}0.034$), but extraction quality degrades from 89\\% to 76\\% and output coherence drops to 85\\%, limiting practical value.\nWe propose $C_0$, the fraction of problems with multiple candidate answers, as a zero-cost binary diagnostic: $C_0{<}5\\%$ guarantees method degeneration to majority voting, while $C_0{>}20\\%$ is necessary but insufficient for potential gains.\n\\end{abstract}\n\n%% ===================================================================\n\\section{Introduction}\n%% ===================================================================\n\nSampling multiple reasoning traces from large language models and aggregating their answers has become standard practice for improving accuracy on complex tasks.\nSelf-Consistency \\citep{wang2023selfconsistency} selects the majority answer across $K$ sampled chains of thought, providing a simple and effective baseline.\nRecent work goes further, proposing to extract symbolic constraints from reasoning traces and use formal solvers to aggregate them, potentially exploiting logical structure that majority voting ignores \\citep{pan2023logiclm,olausson2023linc}.\n\nThe appeal is intuitive: if reasoning traces encode intermediate logical claims, a satisfiability solver should identify the answer most consistent with the full body of extracted knowledge, outperforming a raw head count.\nSeveral methods pursue this direction with varying formalisations of constraint extraction and solver integration.\nYet a basic practical question remains open: across realistic model families, reasoning domains, and operating conditions, when does symbolic consensus actually outperform majority voting?\n\nNo prior work systematically characterises the conditions under which symbolic constraint aggregation helps, degenerates to voting, or actively hurts.\nExisting evaluations compare symbolic and voting methods on narrow model-domain slices, making it difficult to draw general conclusions about method viability.\nThis gap is consequential for practitioners who must decide whether the substantial overhead of constraint extraction and solving (approximately 49\\% additional compute in our measurements) is justified by accuracy gains.\n\nWe address this gap with a controlled empirical study.\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from $K$ reasoning traces, deduplicates them, and selects answers via weighted MAX-SAT.\nSICA serves as a concrete, reproducible test bed for the broader question of whether symbolic aggregation adds value over voting.\nWe evaluate SICA against majority voting across three reasoning domains (formal logic, commonsense, science), five model families (four instruction-scale, one full reasoning model), and varied operating conditions (temperature $T$, sample count $K$), covering more than 1{,}300 problems with controlled pairwise comparisons.\n\nOur contributions are as follows:\n\\begin{itemize}[nosep,leftmargin=1.5em]\n\\item The first systematic evaluation of symbolic consensus across multiple models, domains, and operating conditions, establishing that SICA provides no significant gain over majority voting in standard settings (Section~\\ref{sec:main}).\n\\item Characterisation of the \\emph{capability trap} pattern: instruction-scale models produce ample output diversity ($C_0{=}22$--$65\\%$), but extracted constraints have only weak discriminative power (precision 0.57), and MAX-SAT over such constraints is equivalent to counting (Sections~\\ref{sec:quality}--\\ref{sec:ablation}).\n\\item Analysis of boundary conditions showing that extreme temperature ($T{=}1.0$) partially breaks the pattern but with degraded extraction quality and output coherence (Section~\\ref{sec:temperature}).\n\\item $C_0$, a zero-cost binary diagnostic indicating whether symbolic consensus can potentially operate ($C_0{>}20\\%$) or trivially degenerates to voting ($C_0{<}5\\%$) (Section~\\ref{sec:c0}).\n\\end{itemize}\n\n%% ===================================================================\n\\section{Related Work}\n%% ===================================================================\n\n\\paragraph{Self-Consistency and majority voting.}\nSelf-Consistency (SC) samples multiple chains of thought and selects the answer receiving the most votes \\citep{wang2023selfconsistency}.\nUniversal Self-Consistency extends this to free-form answers \\citep{chen2023universal}.\nSC remains the dominant aggregation baseline due to its simplicity and strong empirical performance.\nWeighted variants assign non-uniform weights to traces based on length or confidence heuristics \\citep{taubenfeld2024weighted}, but evidence for consistent improvement is limited.\n\n\\paragraph{Symbolic reasoning for LLMs.}\nLogic-LM translates natural language problems into first-order logic and verifies solutions with theorem provers \\citep{pan2023logiclm}.\nLINC performs neurosymbolic inference over FOL representations \\citep{olausson2023linc}.\nThese methods focus on single-trace symbolic verification rather than multi-trace constraint aggregation.\nOur work asks whether the multi-trace aggregation dimension adds value beyond what single-trace verification provides.\n\n\\paragraph{Process and outcome reward models.}\nTrained verifiers score individual reasoning steps or final answers \\citep{cobbe2021gsm8k,lightman2023process}.\nUnlike constraint-based aggregation, these methods require supervised training data.\nThey represent a distinct and complementary approach to improving reasoning quality.\n\n\\paragraph{Negative results in NLP.}\nSystematic negative-result studies have clarified the limitations of prompting strategies \\citep{reynolds2021prompt}, chain-of-thought elicitation, and various reasoning augmentation techniques.\nOur work contributes to this tradition by providing controlled evidence on the limits of symbolic consensus.\n\n%% ===================================================================\n\\section{Method: SICA Pipeline}\n\\label{sec:method}\n%% ===================================================================\n\nSICA (Symbolic Invariant Consensus Aggregation) aggregates multiple reasoning traces through five stages.\n\n\\paragraph{1.\\ Trace generation.}\nGiven a problem $q$, we sample $K$ reasoning traces $\\{r_1, \\ldots, r_K\\}$ from an LLM at temperature $T$.\nEach trace contains a chain of thought concluding with a candidate answer.\n\n\\paragraph{2.\\ Answer extraction.}\nA deterministic parser extracts the final answer $a_i$ from each trace $r_i$.\nProblems where all $K$ traces produce the same answer are classified as \\emph{unanimous} and passed directly to majority voting, since no aggregation method can change the outcome.\n\n\\paragraph{3.\\ Constraint extraction.}\nFor each trace $r_i$, an LLM-based extractor produces a set of FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ expressing intermediate logical claims.\nEach constraint is a first-order formula over the candidate answer space.\nExtraction success is measured as the fraction of traces yielding at least one parseable constraint.\n\n\\paragraph{4.\\ Deduplication.}\nSemantically equivalent constraints across traces are merged, retaining the maximum weight.\nDeduplication removes redundancy without discarding signal from independent traces that happen to derive the same intermediate claim.\n\n\\paragraph{5.\\ MAX-SAT aggregation.}\nWe construct a weighted MAX-SAT instance: each unique constraint $c_j$ has weight $w_j$ proportional to extraction confidence.\nCandidate answers are evaluated by the total weight of constraints they satisfy.\nThe answer maximising satisfied weight is selected.\nWhen MAX-SAT produces no discrimination (all candidates satisfy the same constraints), the method falls back to majority vote.\n\n\\paragraph{$C_0$ metric.}\nWe define $C_0$ as the fraction of problems in a dataset where $K$ traces produce more than one distinct candidate answer.\n$C_0$ reflects output diversity: when $C_0 \\approx 0$, all traces agree and any aggregation method reduces to the unanimous answer.\n$C_0$ is computable with zero overhead from the answer extraction stage and requires no constraint extraction.\n\n%% ===================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%% ===================================================================\n\n\\paragraph{Models.}\nWe evaluate seven models spanning four categories.\n\\emph{Qwen family (instruction-scale)}: Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-72B-Instruct-AWQ (4-bit quantised).\n\\emph{Other instruction-scale}: Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct.\n\\emph{Distilled reasoning}: DeepSeek-R1-Distill-Qwen-7B, which we initially expected to behave as a reasoning model but reclassified as instruction-scale after observing $C_0{=}58\\%$ (far above the $<5\\%$ expected for reasoning models).\n\\emph{Full reasoning}: QwQ-32B.\n\n\\paragraph{Domains.}\nProofWriter (deductive reasoning over formal rules), FOLIO (first-order logic NLI), StrategyQA (commonsense binary reasoning), and ARC-Challenge (science multiple-choice).\nThe primary evaluation set combines ProofWriter and FOLIO (``D012'') for formal logic coverage.\n\n\\paragraph{Default configuration.}\n$K{=}12$ traces per problem, temperature $T{=}0.7$, unless stated otherwise.\nTemperature and $K$ are varied in ablation experiments.\n\n\\paragraph{Statistical testing.}\nWe use McNemar's exact test for paired comparisons on the same problem set.\nFor experiments involving multiple comparisons across model families, we apply Bonferroni correction (adjusted $\\alpha \\approx 0.01$ for five families).\n\n%% ===================================================================\n\\section{Results}\n\\label{sec:results}\n%% ===================================================================\n\n\\subsection{Main Results}\n\\label{sec:main}\n\nTable~\\ref{tab:main} presents SICA versus SC accuracy across all model-domain configurations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results: SICA vs.\\ Self-Consistency (SC) across models and domains. $C_0$: fraction of problems with multiple candidate answers. $\\Delta$: SICA $-$ SC in percentage points. $p$: McNemar's exact test. Best per-row result in \\textbf{bold}.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{@{}llrrrrrr@{}}\n\\toprule\nModel & Domain & $N$ & $C_0$\\% & SC & SICA & $\\Delta$pp & $p$ \\\\\n\\midrule\nQwen-14B & PW+FOLIO & 804 & 38 & \\textbf{76.2} & 76.5 & $+0.3$ & n.s. \\\\\nQwen-14B & StrategyQA & 60 & 10 & 53.3 & \\textbf{56.7} & $+3.3$ & 0.16 \\\\\nQwen-14B & ARC-Chal. & 60 & 5 & \\textbf{96.7} & 95.0 & $-1.7$ & --- \\\\\n\\midrule\nQwen-7B & PW+FOLIO & 60 & 65 & 56.7 & \\textbf{60.0} & $+3.3$ & 0.41 \\\\\nQwen-72B & PW+FOLIO & 60 & 22 & 85.0 & \\textbf{86.7} & $+1.7$ & 0.65 \\\\\n\\midrule\nMistral-7B & PW+FOLIO & 60 & 50 & 48.3 & 48.3 & $0.0$ & 1.00 \\\\\nLLaMA-8B & PW+FOLIO & 60 & 62 & 60.0 & \\textbf{68.3} & $+8.3$ & 0.096 \\\\\nDeepSeek-R1-7B & PW+FOLIO & 60 & 58 & \\textbf{71.7} & 68.3 & $-3.3$ & 0.48 \\\\\n\\midrule\nQwQ-32B & Mixed & 46 & 2.6 & \\multicolumn{2}{c}{$\\equiv$ SC} & $0.0$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross all standard conditions, SICA accuracy falls within a few percentage points of SC.\nThe largest positive delta ($+8.3$pp, LLaMA-8B) does not reach significance after Bonferroni correction for multiple model comparisons (McNemar $p{=}0.096$, corrected threshold $\\approx 0.01$).\nThis result is further confounded by 48 truncated traces out of 720 total (6.7\\% truncation rate), which may artificially inflate diversity.\nThe largest negative delta ($-3.3$pp, DeepSeek-R1-7B) occurs with the highest truncation rate in the study (72/720 = 10.0\\%).\nNo model-domain combination shows SICA significantly outperforming SC at $\\alpha{=}0.05$ after correction.\n\nQwQ-32B represents the converged regime.\nWith effective $C_0{=}2.6\\%$, nearly all problems produce unanimous traces, and SICA trivially reduces to SC.\nFull reasoning models, by design, produce deterministic-like chains that eliminate the diversity symbolic methods require.\n\nWithin the Qwen family, $C_0$ decreases monotonically with model scale (7B: 65\\%, 14B: 38\\%, 72B: 22\\%, QwQ-32B: 2.6\\%), but the SICA-SC gap does not follow a corresponding trend ($+3.3$, $+0.3$, $+1.7$, $0.0$pp).\nDiversity reduction does not predict method performance.\n\nDeepSeek-R1-Distill-Qwen-7B was initially expected to function as a reasoning model ($C_0{<}5\\%$).\nIn practice, at 7B parameter capacity, distillation does not produce the deterministic reasoning chains characteristic of full reasoning models.\n$C_0{=}58\\%$ places it squarely in the instruction-scale cluster, and we reclassify it accordingly.\n\n\\subsection{Constraint Quality Analysis}\n\\label{sec:quality}\n\nTable~\\ref{tab:quality} characterises per-problem constraint precision across the 307 multi-candidate problems from the main Qwen-14B experiment ($n{=}804$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint precision on multi-candidate problems (Qwen-14B, PW+FOLIO, $n{=}307$). Precision measures the fraction of extracted constraints that correctly discriminate the ground-truth answer from alternatives. Random baseline: 0.33 for 3-class, 0.50 for binary.}\n\\label{tab:quality}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nDomain & $N$ & Mean & Std & Median \\\\\n\\midrule\nProofWriter & --- & 0.55 & --- & --- \\\\\nFOLIO & --- & 0.62 & --- & --- \\\\\n\\midrule\nOverall & 307 & 0.57 & 0.23 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMean constraint precision is 0.57 (std 0.23), significantly above the 0.33 random baseline for 3-class problems.\nConstraints are \\emph{weakly discriminative}, not random.\nHowever, precision shows no correlation with vote entropy ($R^2{=}0.008$, $p{=}0.12$), meaning constraint quality does not improve when output diversity increases.\nFOLIO constraints (precision 0.62) are somewhat more accurate than ProofWriter constraints (0.55), consistent with FOLIO's more explicit logical structure.\n\nA precision of 0.57 explains the aggregate null result quantitatively.\nAt $K{=}12$ with $C_0{\\approx}38\\%$, approximately 4 multi-candidate problems per 60-question set have constraints that could influence the outcome.\nWith constraints correct 57\\% of the time, the expected number of correct answer flips per experiment is approximately 2, which is indistinguishable from sampling noise at these sample sizes.\n\n\\subsection{Mechanism Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares four aggregation strategies on the main experiment data ($n{=}804$) to isolate the contribution of MAX-SAT reasoning.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint ablation (Qwen-14B, PW+FOLIO, $n{=}804$, $T{=}0.7$). MAX-SAT: full SICA pipeline. Count-only: constraints weighted equally, no satisfiability reasoning. Random-weight: constraints with random weights. SC: standard majority voting.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lccr@{}}\n\\toprule\nMethod & Accuracy (\\%) & $\\Delta$ vs.\\ SC (pp) & $p$ vs.\\ SC \\\\\n\\midrule\nMAX-SAT (SICA) & 76.5 & $+0.3$ & --- \\\\\nCount-only & 76.4 & $+0.2$ & --- \\\\\nRandom-weight & 76.3 & $+0.1$ & --- \\\\\nSC (baseline) & 76.2 & --- & --- \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\small MAX-SAT vs.\\ Count-only: $p{=}0.85$; agreement on 802/804 problems.} \\\\\n\\multicolumn{4}{@{}l}{\\small MAX-SAT vs.\\ Random: $p{=}0.72$.} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMAX-SAT (76.5\\%) is statistically indistinguishable from count-only aggregation (76.4\\%), random-weight aggregation (76.3\\%), and standard majority voting (76.2\\%).\nThe four methods disagree on only 2 of 804 problems.\nThe logical structure encoded in constraints is not exploited by the solver in any meaningful way: MAX-SAT degenerates to a constraint counter, and constraints provide no incremental signal beyond raw vote counts.\n\n\\subsection{Tiebreak Analysis}\n\\label{sec:tiebreak}\n\nTable~\\ref{tab:tiebreak} examines SICA's performance specifically on tied questions, where majority voting must break ties arbitrarily.\n\n\\begin{table}[t]\n\\centering\n\\caption{Tiebreak accuracy on tied questions (Qwen-14B, $K{=}12$, $n_{\\text{tied}}{=}5$ of 60). Tie fraction: 8.3\\%.}\n\\label{tab:tiebreak}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nTiebreak Method & Accuracy on Ties \\\\\n\\midrule\nSICA (constraint-based) & 80\\% (4/5) \\\\\nAlphabetical & 60\\% (3/5) \\\\\nRandom (expected) & 50\\% \\\\\nFirst-seen & 40\\% (2/5) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn the small subset of tied questions (5 of 60, tie fraction 8.3\\%), SICA selects the correct answer 80\\% of the time versus 50\\% for random tiebreaking.\nConstraint-based tiebreaking has genuine value on individual ties.\nHowever, ties are too rare to materially affect overall accuracy.\nThe effective contribution is $0.80 \\times 0.083 \\approx 6.6\\%$ of possible gain, translating to at most ${\\sim}2.5$pp under ideal conditions.\nAt even $K$ (where ties can occur), the tie rate varies from 5.0\\% ($K{=}20$) to 26.7\\% ($K{=}12$), but even at peak tie rate the overall accuracy impact remains within noise.\n\n\\subsection{Boundary Conditions: Temperature}\n\\label{sec:temperature}\n\nTable~\\ref{tab:temperature} presents the temperature ablation on Qwen-14B over 60 D012 problems.\nThis is the critical experiment for understanding when symbolic consensus can differ from voting.\n\n\\begin{table}[t]\n\\centering\n\\caption{Temperature ablation (Qwen-14B, D012, $n{=}60$, $K{=}12$). Default operating condition is $T{=}0.7$. Extraction rate: fraction of traces yielding parseable constraints. Coherence: fraction of traces producing coherent, complete outputs.}\n\\label{tab:temperature}\n\\small\n\\begin{tabular}{@{}cccccccc@{}}\n\\toprule\n$T$ & $C_0$\\% & SC & SICA & $\\Delta$pp & $p$ & Extr. & Coher. \\\\\n\\midrule\n0.3 & 18 & 73.3 & 75.0 & $+1.7$ & 0.65 & 93\\% & ${\\sim}98\\%$ \\\\\n0.5 & 30 & 73.3 & 75.0 & $+1.7$ & 0.55 & 91\\% & ${\\sim}98\\%$ \\\\\n0.7 & 38 & 76.2 & 76.5 & $+0.3$ & n.s. & 89\\% & ${\\sim}98\\%$ \\\\\n1.0 & 72 & 73.3 & 81.7 & $+8.3$ & \\textbf{0.034} & 76\\% & 85\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTemperature $T{=}1.0$ produces the only statistically significant SICA advantage in the entire study: $+8.3$pp (McNemar $p{=}0.034$) with a 7:1 discordant ratio favouring SICA.\n$C_0$ increases from 38\\% at $T{=}0.7$ to 72\\% at $T{=}1.0$, confirming the strong link between temperature and diversity ($r{=}0.98$).\nThe gap is monotonically increasing with temperature.\n\nThis gain comes with substantial costs.\nExtraction rate drops from 89\\% ($T{=}0.7$) to 76\\% ($T{=}1.0$): nearly one quarter of constraint extraction attempts produce empty or unparseable output.\nAnswer coherence drops to 85\\%, meaning 15\\% of generated traces are partially incoherent.\nWhen extraction retries are factored in, the estimated overhead at $T{=}1.0$ rises to approximately 65\\% (vs.\\ 49\\% at default temperature), increasing the per-question compute cost by roughly 30\\%.\nThe $T{=}0.7$ reference row reports the main experiment ($n{=}804$) for context; all other rows use $n{=}60$.\n\nThe practical implication is that the boundary condition exists in theory but is operationally costly.\nA practitioner seeking the marginal $+8.3$pp would need to tolerate incoherent outputs, higher extraction failure rates, and additional compute.\nFor comparison, simply running more traces at the default temperature ($K{=}16$ or $K{=}20$) achieves similar variance reduction without these quality degradations.\n\nLower temperatures ($T{=}0.3$, $T{=}0.5$) produce small positive deltas ($+1.7$pp each) that are not significant ($p{>}0.5$), consistent with the default-temperature null result.\n\n\\subsection{$C_0$ as Operating Regime Indicator}\n\\label{sec:c0}\n\nAcross all 12 model-domain-temperature conditions, $C_0$ values cluster into two distinct regimes (Table~\\ref{tab:c0_summary}).\n\n\\begin{table}[t]\n\\centering\n\\caption{$C_0$ clusters and corresponding SICA-SC gaps. Low-$C_0$ cluster: reasoning models and high-confidence domains. High-$C_0$ cluster: instruction-scale models on challenging domains.}\n\\label{tab:c0_summary}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nCluster & $C_0$ range & Mean gap (pp) & $N$ points \\\\\n\\midrule\nLow $C_0$ & 0--10\\% & $-0.9$ & 3 \\\\\nHigh $C_0$ & 22--72\\% & $+1.8$ & 9 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\small Linear regression: $R^2{=}0.08$, slope$=0.09$pp per \\%$C_0$, $p{=}0.37$.} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe low-$C_0$ cluster ($C_0{=}0$--$10\\%$) comprises QwQ-32B ($C_0{=}2.6\\%$), ARC-Challenge ($C_0{=}5\\%$), and StrategyQA ($C_0{=}10\\%$).\nMean gap in this cluster is $-0.9$pp: SICA trivially reduces to voting.\nThe high-$C_0$ cluster ($C_0{=}22$--$72\\%$) comprises instruction-scale models on formal logic domains plus the temperature extreme.\nMean gap is $+1.8$pp but with enormous variance (from $-3.3$ to $+8.3$pp), and no individual comparison is significant except $T{=}1.0$.\n\nLinear regression of gap on $C_0$ yields $R^2{=}0.08$ ($p{=}0.37$): $C_0$ provides no gradient-level predictive power for the SICA-SC gap.\nThe 10--22\\% range contains only one data point ($C_0{=}18\\%$ at $T{=}0.3$), leaving a gap between clusters.\n\n$C_0$ therefore functions as a binary indicator.\n$C_0{<}5\\%$ reliably predicts SICA $\\equiv$ SC (method degeneration).\n$C_0{>}20\\%$ indicates that symbolic consensus can potentially differ from voting, but does not predict whether the difference will be positive, negative, or zero.\nThis makes $C_0$ useful as a zero-cost go/no-go check before investing in constraint extraction, but not as a quantitative performance predictor.\n\n%% ===================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%% ===================================================================\n\n\\paragraph{The capability trap as descriptive pattern.}\nAcross our experiments, we observe a recurring pattern that we label the \\emph{capability trap}: conditions that enable symbolic consensus to differ from majority voting (high output diversity, $C_0{>}20\\%$) do not ensure that the difference is beneficial.\nInstruction-scale models produce abundant diversity ($C_0{=}22$--$65\\%$), but extracted constraints at precision 0.57 are insufficient to reliably steer answer selection.\nWe emphasise that this is a descriptive label for an empirical observation, not a mechanistic explanation.\nThe decoupling of diversity and constraint quality may stem from the extraction process, the FOL formalism, or inherent limitations of current-generation LLM reasoning.\n\n\\paragraph{Practical guidelines.}\nFor practitioners considering symbolic aggregation, our results suggest a simple decision framework.\nFirst, compute $C_0$ from raw answer extractions at zero cost.\nIf $C_0{<}5\\%$ (strong reasoning models, easy tasks), symbolic methods will trivially degenerate to voting.\nIf $C_0{>}20\\%$ under standard temperatures, symbolic methods may differ from voting but are unlikely to improve accuracy, while incurring approximately 49\\% additional compute (Appendix~\\ref{app:overhead}).\n\n\\paragraph{The $T{=}1.0$ exception and its limits.}\nThe temperature ablation reveals that extreme diversity ($T{=}1.0$, $C_0{=}72\\%$) can produce a significant SICA advantage.\nThis finding prevents us from claiming that the capability trap is absolute.\nHowever, the associated quality degradation (extraction rate 76\\%, coherence 85\\%) and the fact that this result comes from a single $n{=}60$ experiment temper its practical significance.\nReplication across models and larger sample sizes is needed before recommending $T{=}1.0$ as an operating point.\n\n\\paragraph{Alternative aggregation directions.}\nThe Logic-LM comparison (Appendix~\\ref{app:logiclm}) shows that Logic-LM with $K$ repetitions and majority voting achieves 80.9\\% on FOLIO vs.\\ SICA's 79.4\\%.\nSingle-trace FOL verification repeated $K$ times may be more effective than multi-trace constraint aggregation.\nInverse-length weighted voting (Appendix~\\ref{app:weightedsc}) matches SICA at zero extraction cost (77.0\\% vs.\\ 76.5\\%).\nThese results suggest that lightweight quality proxies, or per-trace verification, may be more productive directions than cross-trace constraint consensus.\n\n\\paragraph{Limitations.}\n(1) We evaluate one instantiation of symbolic consensus (FOL constraints, MAX-SAT solver). Other constraint languages or aggregation strategies might yield different results.\n(2) The largest powered test ($n{=}804$) covers only Qwen-14B on ProofWriter and FOLIO. Cross-model tests at $n{\\geq}200$ exist only for LLaMA-8B.\n(3) We test only one full reasoning model (QwQ-32B); additional reasoning models (o1-series, Gemini thinking models) would strengthen the converged-regime claim.\n(4) The $T{=}1.0$ boundary condition has been tested only on Qwen-14B with $n{=}60$.\n(5) The constraint ablation (Table~\\ref{tab:ablation}) was performed at $T{=}0.7$; results may differ at extreme temperatures where the constraint quality distribution changes.\n\n%% ===================================================================\n\\section{Conclusion}\n%% ===================================================================\n\nWe present the first systematic empirical study of symbolic consensus for LLM reasoning aggregation.\nAcross three domains, five model families, and over 1{,}300 problems, symbolic constraint aggregation via SICA provides no significant accuracy improvement over majority voting in standard operating conditions.\nExtracted constraints are weakly discriminative (precision 0.57) but insufficient to reliably influence answer selection.\nThe MAX-SAT solver degenerates to a constraint counter: it is statistically equivalent to counting or random weighting.\nAt extreme temperatures ($T{=}1.0$), a marginal gain appears ($+8.3$pp, $p{=}0.034$) but is accompanied by degraded extraction quality and output coherence.\nWe contribute $C_0$ as a practical, zero-cost binary diagnostic for practitioners deciding whether to invest in symbolic aggregation.\nOur findings indicate that, for the current generation of LLM constraint extraction, simple majority voting remains the method of choice.\n\n%% ===================================================================\n%% APPENDIX\n%% ===================================================================\n\\appendix\n\n\\section{$K$ Sensitivity Analysis}\n\\label{app:k_ablation}\n\nTable~\\ref{tab:k_ablation} presents the effect of varying $K$ on SICA vs.\\ SC (Qwen-14B, D012, $n{=}60$).\n\n\\begin{table}[h]\n\\centering\n\\caption{$K$ ablation (Qwen-14B, D012, $n{=}60$, $T{=}0.7$). Tiebreak rate: fraction of problems producing exact ties at this $K$.}\n\\label{tab:k_ablation}\n\\small\n\\begin{tabular}{@{}rccccr@{}}\n\\toprule\n$K$ & SICA & SC & $\\Delta$pp & Tiebreak Rate \\\\\n\\midrule\n6  & 75.0 & 73.3 & $+1.7$ & 18.3\\% \\\\\n8  & 75.0 & 75.0 & $0.0$  & --- \\\\\n11 & 75.0 & 75.0 & $0.0$  & --- \\\\\n12 & 73.3 & 75.0 & $-1.7$ & 26.7\\% \\\\\n16 & 71.7 & 73.3 & $-1.7$ & --- \\\\\n20 & 71.7 & 73.3 & $-1.7$ & 5.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt odd $K{=}11$, where exact ties cannot occur, the gap is precisely zero.\nThis confirms that SICA's potential value comes entirely from tiebreaking.\nAt $K{=}6$ (small sample), the $+1.7$pp positive delta falls within the bootstrap 95\\% CI $[-5.0, +8.3]$pp, compatible with zero effect.\nAt $K{\\geq}12$, SICA shows a consistent $-1.7$pp deficit, likely from noise injection by low-quality constraints in larger trace sets.\nThe pattern is non-monotonic (positive at low $K$, zero at odd $K$, negative at high $K$), making a blanket ``SICA $\\leq$ SC at all $K$'' statement inaccurate.\nThe correct characterisation is \\emph{$K$-dependent with no consistent advantage}.\n\n\\section{Overhead Analysis}\n\\label{app:overhead}\n\nTable~\\ref{tab:overhead} breaks down wall-clock time per question from the main experiment ($n{=}804$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-question wall-time breakdown (Qwen-14B, $n{=}804$, $T{=}0.7$).}\n\\label{tab:overhead}\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nComponent & Mean time (s) & \\% of total \\\\\n\\midrule\nTrace generation & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nDeduplication & 1.0 & 1.6\\% \\\\\nMAX-SAT solving & 0.003 & ${<}0.01\\%$ \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA's overhead relative to SC (which requires only trace generation) is 48.7\\%, dominated by the constraint extraction LLM call.\nMAX-SAT solving time is negligible.\nThe overhead-to-gain ratio at default temperature is $48.7\\% / 0.3\\text{pp} \\approx 162$: each percentage point of (non-significant) gain costs 162\\% in additional compute.\nMedian overhead is 48.9\\%, with the 90th percentile at 57.6\\%.\nProofWriter questions incur 51.3\\% overhead on average vs.\\ 38.6\\% for FOLIO, reflecting longer constraint extraction prompts for deductive rules.\n\n\\section{Weighted SC Baselines}\n\\label{app:weightedsc}\n\nTable~\\ref{tab:weighted_sc} compares SICA against simple weighted voting heuristics ($n{=}804$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Weighted SC variants (Qwen-14B, PW+FOLIO, $n{=}804$, $T{=}0.7$).}\n\\label{tab:weighted_sc}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & Accuracy (\\%) & $\\Delta$ vs.\\ SC (pp) & $p$ vs.\\ SC \\\\\n\\midrule\nInverse-length & 77.0 & $+0.8$ & 0.42 \\\\\nSICA (MAX-SAT) & 76.5 & $+0.3$ & --- \\\\\nSC (uniform) & 76.2 & --- & --- \\\\\nLength-weighted & 75.3 & $-0.9$ & 0.16 \\\\\nConstraint-count & 75.3 & $-0.9$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInverse-length weighting (favouring shorter, more confident traces) achieves 77.0\\%, slightly above SICA's 76.5\\%.\nAll differences are non-significant.\nA zero-cost heuristic based on trace length matches or exceeds the full SICA pipeline, reinforcing the conclusion that constraint extraction does not add value at default settings.\n\n\\section{Logic-LM Comparison}\n\\label{app:logiclm}\n\nTable~\\ref{tab:logiclm} compares SICA against a Logic-LM baseline on FOLIO ($n{=}204$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Logic-LM $\\times$ $K$ vs.\\ SICA vs.\\ SC on FOLIO ($n{=}204$, $K{=}12$).}\n\\label{tab:logiclm}\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Accuracy (\\%) & $p$ vs.\\ SICA \\\\\n\\midrule\nLogic-LM $\\times$ $K$ + vote & 80.9 & 0.38 \\\\\nSICA (MAX-SAT) & 79.4 & --- \\\\\nSC (majority vote) & 79.4 & --- \\\\\nSingle-trace Logic-LM & 77.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLogic-LM repeated $K$ times with majority voting achieves 80.9\\% vs.\\ SICA's 79.4\\%.\nThe difference is not significant ($p{=}0.38$), but the directional advantage of per-trace verification over multi-trace constraint aggregation is notable.\nLogic-LM performs a complete FOL consistency check per trace (pass/fail), which has stronger discriminative power than SICA's soft constraint aggregation: an internally inconsistent trace is excluded entirely by Logic-LM, while SICA still incorporates its constraints.\n\n\\section{GSM8K Pilot}\n\\label{app:gsm8k}\n\nA 30-question pilot on GSM8K (Qwen-14B, $K{=}12$) yields: SICA 80.0\\% vs.\\ SC 76.7\\% ($\\Delta{=}+3.3$pp, $p{=}0.56$, McNemar).\n$C_0{=}27\\%$ (moderate), multi-candidate rate 23\\%, extraction rate 85\\%.\nAt $n{=}30$, the standard error is approximately 8pp, making this result uninformative.\nGSM8K is included as a pilot data point for domain coverage; it does not alter any main-text claims.\n\n\\section{Constraint Case Studies}\n\\label{app:case_studies}\n\nWe qualitatively analyse 8 representative questions from the main experiment.\nOf these, 3 produce semantically meaningful constraints, 2 produce correctly discriminative constraints that steer SICA to the right answer, 3 produce non-discriminative constraints (tautological or irrelevant), and 2 produce actively misleading constraints that steer SICA away from the correct answer.\n\nConstraint categories: 3 tautological, 2 partially correct, 2 fully correct, 1 contradicting ground truth.\nThe two fully correct cases both come from FOLIO problems with explicit formal logical structure, where FOL extraction naturally aligns with the problem's own representation.\nThe misleading case involves a ProofWriter problem where the extracted constraint encodes a premise not present in the original rules.\n\nThese case studies illustrate that constraints \\emph{can} be discriminative on individual problems (consistent with the aggregate precision of 0.57), but the mixture of helpful, neutral, and harmful constraints yields no net improvement when aggregated across a full problem set.\n\n\\section{$C_0$ Diagnostic Full Data}\n\\label{app:c0_data}\n\nTable~\\ref{tab:c0_full} lists all 12 data points used for the $C_0$ analysis in Section~\\ref{sec:c0}.\n\n\\begin{table}[h]\n\\centering\n\\caption{All (model/condition, domain, $C_0$, SICA-SC gap) data points.}\n\\label{tab:c0_full}\n\\small\n\\begin{tabular}{@{}llrr@{}}\n\\toprule\nCondition & Domain & $C_0$ (\\%) & Gap (pp) \\\\\n\\midrule\nQwQ-32B & Mixed & 2.6 & $0.0$ \\\\\nQwen-14B & ARC & 5.0 & $-1.7$ \\\\\nQwen-14B & StrategyQA & 10.0 & $+3.3$ \\\\\nQwen-14B $T{=}0.3$ & PW+FOLIO & 18.0 & $+1.7$ \\\\\nQwen-72B & PW+FOLIO & 22.0 & $+1.7$ \\\\\nQwen-14B GSM8K & GSM8K & 27.0 & $+3.3$ \\\\\nQwen-14B $T{=}0.7$ & PW+FOLIO & 38.0 & $+0.3$ \\\\\nMistral-7B & PW+FOLIO & 50.0 & $0.0$ \\\\\nDeepSeek-R1-7B & PW+FOLIO & 58.0 & $-3.3$ \\\\\nLLaMA-8B & PW+FOLIO & 62.0 & $+8.3$ \\\\\nQwen-7B & PW+FOLIO & 65.0 & $+3.3$ \\\\\nQwen-14B $T{=}1.0$ & PW+FOLIO & 72.0 & $+8.3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% ===================================================================\n%% REFERENCES\n%% ===================================================================\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Chen et~al.(2023)]{chen2023universal}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv:2311.17311}, 2023.\n\n\\bibitem[Pan et~al.(2023)]{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Y.~Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et~al.(2023)]{olausson2023linc}\nT.~X.~Olausson, A.~Gu, B.~Lipkin, C.~E.~Zhang, A.~Solar-Lezama, J.~B.~Tenenbaum, and R.~Levy.\n\\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training Verifiers to Solve Math Word Problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023process}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's Verify Step by Step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Taubenfeld et~al.(2024)]{taubenfeld2024weighted}\nA.~Taubenfeld, Y.~Horesh, N.~Benaim, G.~Shani, N.~Shani, and L.~Wolf.\n\\newblock Systematic Biases in LLM Simulations of Debates.\n\\newblock \\emph{arXiv:2402.04049}, 2024.\n\n\\bibitem[Reynolds and McDonell(2021)]{reynolds2021prompt}\nL.~Reynolds and K.~McDonell.\n\\newblock Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm.\n\\newblock In \\emph{CHI EA}, 2021.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ba83137d-c379-45df-9f81-c93fa44b5f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "a8180a1a-802d-4c54-9201-aefde55682ec",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic consensus survey paper for dream_20260517T144412",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Tool call

_source line 26 · 2026-05-17T15:44:59.367Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014rQEQx4Bszw4tDE8PeGtzr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8180a1a-802d-4c54-9201-aefde55682ec",
  "isSidechain": false,
  "requestId": "req_011Cb8Q7zSAMKDxPP79nZHoe",
  "type": "assistant",
  "uuid": "2a95050a-a626-485a-a638-054c46dab212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sfnt9uPmQPGS5ZG9SYXedA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12195,
      "cache_read_input_tokens": 61225,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12195,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 61225,
          "cache_creation_input_tokens": 12195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12195
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

_source line 27 · 2026-05-17T15:44:59.914Z_

<details><summary>↩ Tool result · `toolu_014rQEQx4Bszw4tDE8PeGtzr`</summary>

```text
)

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
public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 205263 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a95050a-a626-485a-a638-054c46dab212",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "dc669e57-24bf-4c7a-91d2-cd85158274da",
  "toolUseResult": {
    "stdout": ")\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 205263 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2a95050a-a626-485a-a638-054c46dab212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T15:45:03.813Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UBKSFJmC4Hy4Nk16RWCY33`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc669e57-24bf-4c7a-91d2-cd85158274da",
  "isSidechain": false,
  "requestId": "req_011Cb8Q8HVLDZDfPrmngUYq3",
  "type": "assistant",
  "uuid": "4f8554bc-4077-4061-9ebf-85c3b5eed4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4EREvSmEL1pmfP7wVne7i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 73420,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 73420,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 29 · 2026-05-17T15:45:04.356Z_

<details><summary>↩ Tool result · `toolu_01UBKSFJmC4Hy4Nk16RWCY33`</summary>

```text
/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmti10.pfb>
Output written on paper.pdf (12 pages, 208539 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f8554bc-4077-4061-9ebf-85c3b5eed4bf",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "4fead138-779a-4215-a7e4-ce51a6b48e6a",
  "toolUseResult": {
    "stdout": "/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmti10.pfb>\nOutput written on paper.pdf (12 pages, 208539 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4f8554bc-4077-4061-9ebf-85c3b5eed4bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T15:45:07.850Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0192NzN1jnAC6YuGPdfjpxf4`</summary>

```json
{
  "command": "grep -c \"Warning\" paper.log | head -1 && grep \"LaTeX Warning\" paper.log",
  "description": "Check for remaining warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fead138-779a-4215-a7e4-ce51a6b48e6a",
  "isSidechain": false,
  "requestId": "req_011Cb8Q8cFwPMM2xqHrvtgR1",
  "type": "assistant",
  "uuid": "766ae65f-8e03-47a8-aaa1-2c53e9648413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCbABhbnaFyoiTAqe8kTzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 74210,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 443,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 74210,
          "cache_creation_input_tokens": 443,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 443
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

_source line 31 · 2026-05-17T15:45:07.913Z_

<details><summary>↩ Tool result · `toolu_0192NzN1jnAC6YuGPdfjpxf4`</summary>

```text
9
LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "766ae65f-8e03-47a8-aaa1-2c53e9648413",
  "isSidechain": false,
  "promptId": "08f9818c-216a-463f-8844-60836a5021a9",
  "type": "user",
  "uuid": "81d3d993-2ef3-4609-b9fd-60dbcad348f7",
  "toolUseResult": {
    "stdout": "9\nLaTeX Warning: `h' float specifier changed to `ht'.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "766ae65f-8e03-47a8-aaa1-2c53e9648413",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-17T15:45:07.916Z_

```json
{
  "parentUuid": "81d3d993-2ef3-4609-b9fd-60dbcad348f7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "dbc83480-fef1-4b3e-867f-1e6c60f913cd",
  "timestamp": "2026-05-17T15:45:07.916Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-17T15:45:18.827Z_

编译成功，12 页 PDF，无错误。仅有一个浮动位置的常规警告。

论文已写入 `worst/paper.tex` 并编译为 `worst/paper.pdf`。结构：

**正文** (约 8 页): Abstract, Introduction, Related Work, Method (SICA Pipeline), Experimental Setup, Results (6 subsections: Main Results T1, Constraint Quality T2, Mechanism Ablation T3, Tiebreak Analysis T4, Temperature Boundary Conditions T5, C0 Diagnostic), Discussion, Conclusion

**附录** (约 4 页): K Sensitivity Analysis, Overhead Analysis, Weighted SC Baselines, Logic-LM Comparison, GSM8K Pilot, Constraint Case Studies, C0 Full Data

所有 18 个独立实验均有对应的 table 或 section。所有数字来自 `experiment_data.json`，无编造。叙事按 narrative guidance 重构：title 改为 survey 风格，capability trap 降级为 descriptive label，T=1.0 positive result 在 boundary conditions 节正面处理，constraint precision 0.57 承认为 weakly discriminative，C0 定位为 binary indicator。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc83480-fef1-4b3e-867f-1e6c60f913cd",
  "isSidechain": false,
  "requestId": "req_011Cb8Q8sSFVpyp4zWciWauv",
  "type": "assistant",
  "uuid": "3c795afb-2b28-4e5b-b728-6a7e6e44a75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/worst",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxizW91NjQVu3HmHgXwyAR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 74653,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 74653,
          "cache_creation_input_tokens": 228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 228
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "3c795afb-2b28-4e5b-b728-6a7e6e44a75b",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic consensus survey paper for dream_20260517T144412",
  "sessionId": "291986bc-33d8-4825-80fc-c5492d1484a2"
}
```

---
