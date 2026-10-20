# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/d62d6b41-b2b1-4bd2-b0b5-6f9443290165.jsonl`
- **Structured JSON:** [`1430e37decd53841f828.json`](../../sessions/14/1430e37decd53841f828.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T18:15:23.171Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T18:15:23.171Z",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claims 需要 calibration。Claim 1 从 \"sole driver\" 降级为 \"dominant driver (>95%)\"，\n承认 gradient coupling 有 marginal contribution (~3-5%) 但不改变 practical conclusion。\nC1 表述改为 \"BCE+KL-targets recovers >95% of KL advantage\"，不再用 exact match。\nARC-c 出现 2-3pp delta，需补充 per-task analysis 解释 reasoning tasks 对 gradient pathway 更敏感。\nBCE 30% forced top-k PPL 降至 ~10.0（gap 缩小至 1.2 vs KL 8.82），\n需强化 Pareto frontier 叙事：KL 在 quality-efficiency tradeoff 上仍优但 margin 更小，honest reporting。\n6-point regime curve 基本单调，35% 区间有 ±0.2 noise（单次测量），\n改为 \"approximate phase transition\" 并讨论 single-seed noise source。\n仍冲 EMNLP Main，预期 reviewer avg 3.5-4.0，需 minor revision。\n1-2 位审稿人仍有 incremental concern，但多数认为 empirical contribution sufficient。\n关键防御：C1 causal ablation + 53% mask divergence 是 genuine empirical finding，\n不是 engineering trick。14B MMLU gap 作为 honest limitation 报告。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T18:15:23.175Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T18:15:23.175Z",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-18T18:15:23.197Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claims 需要 calibration。Claim 1 从 "sole driver" 降级为 "dominant driver (>95%)"，
承认 gradient coupling 有 marginal contribution (~3-5%) 但不改变 practical conclusion。
C1 表述改为 "BCE+KL-targets recovers >95% of KL advantage"，不再用 exact match。
ARC-c 出现 2-3pp delta，需补充 per-task analysis 解释 reasoning tasks 对 gradient pathway 更敏感。
BCE 30% forced top-k PPL 降至 ~10.0（gap 缩小至 1.2 vs KL 8.82），
需强化 Pareto frontier 叙事：KL 在 quality-efficiency tradeoff 上仍优但 margin 更小，honest reporting。
6-point regime curve 基本单调，35% 区间有 ±0.2 noise（单次测量），
改为 "approximate phase transition" 并讨论 single-seed noise source。
仍冲 EMNLP Main，预期 reviewer avg 3.5-4.0，需 minor revision。
1-2 位审稿人仍有 incremental concern，但多数认为 empirical contribution sufficient。
关键防御：C1 causal ablation + 53% mask divergence 是 genuine empirical finding，
不是 engineering trick。14B MMLU gap 作为 honest limitation 报告。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "050616e7-2336-4e7f-9da2-8537f250e4b5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T18:15:23.197Z_

```json
{
  "parentUuid": "050616e7-2336-4e7f-9da2-8537f250e4b5",
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
  "uuid": "e7a9b17f-3b8c-4364-9fd4-48e981ac6f1e",
  "timestamp": "2026-05-18T18:15:23.197Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T18:15:23.197Z_

```json
{
  "parentUuid": "e7a9b17f-3b8c-4364-9fd4-48e981ac6f1e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fdbe59e1-e4ee-4cc6-9a17-19a888adb745",
  "timestamp": "2026-05-18T18:15:23.197Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for sparse SwiGLU distillation",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Assistant

_source line 7 · 2026-05-18T18:15:25.846Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdbe59e1-e4ee-4cc6-9a17-19a888adb745",
  "isSidechain": false,
  "requestId": "req_011CbAVQLxUMHDfUqRS2nbwE",
  "type": "assistant",
  "uuid": "10ea30ce-a669-4fba-b1dd-75d7ed544931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7tWvLVAaguG5GrEqkgDKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13634,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13634
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

_source line 8 · 2026-05-18T18:15:27.455Z_

<details open><summary>🔧 Tool call — Read · `toolu_019C7KshaRfdAqtrhxgPv7Ej`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10ea30ce-a669-4fba-b1dd-75d7ed544931",
  "isSidechain": false,
  "requestId": "req_011CbAVQLxUMHDfUqRS2nbwE",
  "type": "assistant",
  "uuid": "8768dcde-66bb-494b-9d35-3005283bd666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7tWvLVAaguG5GrEqkgDKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13634,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13634
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

_source line 9 · 2026-05-18T18:15:27.608Z_

<details open><summary>🔧 Tool call — Read · `toolu_014Dqaec2tGxPzncGjfEJjRN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8768dcde-66bb-494b-9d35-3005283bd666",
  "isSidechain": false,
  "requestId": "req_011CbAVQLxUMHDfUqRS2nbwE",
  "type": "assistant",
  "uuid": "b15af45c-eb8d-4253-bb26-b464d2434bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7tWvLVAaguG5GrEqkgDKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13634,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13634
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

_source line 10 · 2026-05-18T18:15:27.620Z_

<details><summary>↩ Tool result · `toolu_014Dqaec2tGxPzncGjfEJjRN`</summary>

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
10	1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from "engineering a better loss" to "discovering that output-distribution distillation reveals hidden neuron importance structure." **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: "Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)
11	
12	2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)
13	
14	3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.
21	
22	- **Our framing / headline question**: "What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.
23	
24	- **Headline result template**: "KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements."
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
38	1. **"Incremental / no new algorithm"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.
39	
40	2. **"KL wins only because more compute"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.
45	
46	5. **"Effect size may not hold on downstream tasks"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.
47	
48	6. **"Unfair comparison: BCE+comp close to KL but at higher inference cost"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.
49	
50	## Venue Fit
51	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
52	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
53	- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from "systematic composition" to "empirical discovery about what KL learns for sparsity prediction." This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b15af45c-eb8d-4253-bb26-b464d2434bf1",
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "b65bb70e-d3a6-4827-8e81-ac3c6e034643",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL distillation discovers fundamentally different (and superior) neuron importance patterns that magnitude-based oracles miss**: The C1 causal ablation (D059) proves that KL's advantage comes **entirely** from target quality (which neurons to keep), with gradient coupling contributing ≈0 across **both PPL and all downstream tasks**. **Controlled eval (TEAL 50% uniform, matched protocol)**: BCE+KL-targets PPL = **11.9638**, KL predictor PPL = **11.9638** (exact match). **Downstream confirmation (full-spectrum)**: All 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) also match within <1pp delta, confirming gradient coupling = 0 across PPL + reasoning + knowledge + math dimensions. Standard BCE (magnitude masks) PPL ≈ 22.51. Target quality alone accounts for KL's full advantage. *Additional evidence from training eval (Gumbel hard mask)*: BCE+KL-targets PPL 9.29 @60.9% ≈ KL 9.21 @60.6%, consistent with controlled eval. The 53% mask divergence between KL-derived and magnitude-based masks is the core empirical finding: KL discovers a qualitatively different neuron importance landscape. **Implication**: The gradient coupling analysis (§3.6) provides mathematical intuition for *why* KL can discover better targets (coupled gradients explore joint neuron interaction patterns), but the causal driver is the resulting mask quality, not the gradient pathway per se. This shifts the contribution from \"engineering a better loss\" to \"discovering that output-distribution distillation reveals hidden neuron importance structure.\" **Supporting evidence**: (a) Iso-compute ablation: BCE with 2.71× more FLOPs still PPL=27.97 vs KL=12.00, confirming the gap is structural; (b) BCE at recommended 30% operating point (D062): forced TEAL top-k PPL=11.24 vs KL=8.82, Δ=2.42 — BCE 30% is nearly as bad as KL 50% (11.80), meaning BCE's inferior masks waste ~20pp of sparsity budget; (c) BCE Lagrangian failure at 30%: BCE loss scale (~0.6) vs KL (~0.0001) causes same Lagrangian to fail; (d) No compensation needed: KL eliminates 67.2M compensation parameters (~256MB). **Anticipated attack**: \"Two-stage training (KL→oracle→BCE) avoids needing KL predictor at inference?\" Defense: KL predictor is contextual (per-input adaptive); oracle masks are fixed. Deployment requires per-input sparsity adaptation. **Remaining caveat**: Single seed (s42); C1 s123 in progress for statistical robustness. (Headline claim, resolves persistent R3-R8 confound)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, global top-k causes high seed-to-seed variance in downstream metrics due to per-layer allocation imbalance (uniform allocation stabilizes MMLU: σ drops from 9.5pp to 1.3pp across 3 seeds, mean 40.7% vs TEAL's 38.6%). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition reveals three distinct regimes with non-monotonic allocation preference: (1) **Budget-surplus regime (≤30%)**: uniform allocation reduces seed-to-seed instability by 7.5× (σ: 1.3pp vs 9.5pp across 3 seeds), stabilizing downstream performance (3-seed mean MMLU: 40.7±1.3pp uniform vs 35.7±9.5pp global); (2) **Budget-constrained regime (~40%)**: learned allocation outperforms blind uniformity — MMLU 38.1% (global) vs 30.7% (uniform), +7.4pp — the predictor's learned priorities become valuable when budget is tight; (3) **Capacity-cliff regime (≥50%)**: allocation irrelevant, both collapse to ~28% ≈ random. Recommended operating point (8B-validated): 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. **14B scale-dependent caveat (D054)**: At Qwen-2.5-14B 50% sparsity, uniform allocation does NOT fix KL's MMLU gap (64.49% uniform vs 63.72% global, only +0.77pp; TEAL global=71.83%). The 8B allocation-dependent pattern does not generalize to 14B. This is a valuable negative finding revealing loss × allocation × scale three-way interaction. 14B claim scope: KL PPL advantage preserved (7.62 vs 8.73 TEAL), but downstream MMLU gap persists regardless of allocation. The non-monotonic allocation preference (uniform@30% → global@40% → irrelevant@50%) provides mechanistic insight: at generous budgets, ensuring no layer is starved matters most; at tight budgets, the predictor's learned cross-layer priorities add value; at catastrophic budgets, capacity itself is the binding constraint. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. **6-point PPL regime curve (D063)**: 30%=8.82, 35%=9.31, 40%=10.12, 45%=10.80, 50%=11.80 (TEAL global). Smooth monotonic increase from 30-50%, providing dense sampling for regime boundary identification. 25% eval pending. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"What does KL distillation actually learn for SwiGLU sparsity prediction, and why do its masks differ fundamentally from magnitude-based oracles?\" The theoretical grounding (§3.6, suggestive): BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm. This provides intuition for how KL *can* discover joint interaction patterns. The C1 causal ablation (§4.4) then empirically confirms: the masks KL discovers, not the gradient pathway itself, are what matter.\n\n- **Headline result template**: \"KL-trained sparsity predictors discover neuron importance patterns that diverge 53% from magnitude-based masks. A causal ablation confirms that these mask patterns, not gradient coupling, drive KL's quality advantage: BCE trained on KL-derived masks matches KL performance exactly across PPL (11.96 = 11.96) and all downstream tasks (delta <1pp on ARC-c, WinoGrande, MMLU, GSM8K). This finding eliminates the need for 67.2M compensation parameters and reveals three sparsity operating regimes (now with 6 data points) with qualitatively different allocation requirements.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: **Substantially mitigated by C1 finding**. The 53% mask divergence and causal ablation are genuine empirical discoveries, not engineering contributions. No prior work has shown that KL-derived masks encode fundamentally different neuron importance from magnitude-based approaches. The paper now contributes a finding (mask pattern discovery) rather than just a method (combining known techniques). Additional support: formal decomposition framework, quantitative s^2 prediction, three-regime analysis.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 (plan_009, GQA + sliding window) and Qwen-2.5-14B cross-scale validation (D048/D054). **14B mixed result**: KL PPL advantage preserved (7.62 vs TEAL 8.73, 1.47× dense ratio identical to 8B), but KL MMLU=63.72% (global) / 64.49% (uniform) significantly trails TEAL 71.83% (global). Uniform allocation does not fix this gap (D054). PPL-downstream disconnect at 14B scale is an honest limitation, not hidden. Framing: KL's coupled gradient captures output-distribution fidelity (PPL) across scales, but 14B knowledge-intensive tasks (MMLU) show scale-dependent sensitivity that warrants further investigation.\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- **Novelty upgraded from R8**: C1 causal ablation + 53% mask divergence finding elevates paper from \"systematic composition\" to \"empirical discovery about what KL learns for sparsity prediction.\" This addresses the persistent R3-R8 novelty concern and moves the paper toward Main Conference territory (target 4.0).\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  },
  "sourceToolAssistantUUID": "b15af45c-eb8d-4253-bb26-b464d2434bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "3d94d5a0-fae8-4125-b107-97df86918d7e",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for sparse SwiGLU distillation",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Tool result

_source line 13 · 2026-05-18T18:15:27.732Z_

<details><summary>↩ Tool result · `toolu_019C7KshaRfdAqtrhxgPv7Ej`</summary>

```text
1	[
2	  {
3	    "name": "Four-condition ablation @ 50% sparsity",
4	    "description": "Core comparison: KL-only vs BCE-only vs BCE+comp vs KL+comp at 50% model-level sparsity.\nKL-only (5 seeds) as headline, BCE+comp (5 seeds) as primary competitor,\nKL+comp and BCE-only (3 seeds each) as secondary.\n",
5	    "results": {
6	      "kl_only_hard_mask_ppl_mean": 9.19,
7	      "kl_only_hard_mask_ppl_std": 0.04,
8	      "kl_only_hard_mask_ppl_seeds": [
9	        9.21,
10	        9.25,
11	        9.14,
12	        9.19,
13	        9.15
14	      ],
15	      "kl_only_teal_global_ppl_mean": 11.78,
16	      "kl_only_teal_global_ppl_std": 0.05,
17	      "kl_only_sparsity": 0.498,
18	      "bce_only_hard_mask_ppl_mean": 28.16,
19	      "bce_only_hard_mask_ppl_std": 0.21,
20	      "bce_only_teal_global_ppl_mean": 44.05,
21	      "bce_only_sparsity": 0.496,
22	      "bce_comp_hard_mask_ppl_mean": 20.8,
23	      "bce_comp_hard_mask_ppl_std": 0.7,
24	      "bce_comp_teal_global_ppl_mean": 25.5,
25	      "bce_comp_compensation_params": 67248128,
26	      "bce_comp_compensation_params_mb": 256,
27	      "bce_comp_recovery_vs_bce_ppl": 2.5,
28	      "kl_comp_hard_mask_ppl_mean": 9.18,
29	      "kl_comp_hard_mask_ppl_std": 0.04,
30	      "kl_comp_teal_global_ppl_mean": 11.78,
31	      "kl_comp_recovery_vs_kl_ppl": 0.01,
32	      "kl_comp_compensation_redundant": true
33	    },
34	    "tables": [
35	      "Table 1: Main 4-condition PPL comparison @ 50% sparsity"
36	    ],
37	    "figures": [],
38	    "analysis": "Headline: KL-only (PPL 9.19) > BCE+comp (PPL 20.8) by 2.26x, 同时省去 67.2M compensation 参数。\nKL+comp ≈ KL-only 证明 compensation 在 KL 训练下完全冗余。\nBCE+comp 虽优于 BCE-only (20.8 vs 28.16)，但改善仅 7.4 PPL — compensation 是 BCE 的 patch \n而非根本解决方案。KL 对 predictor training 的改进是 structural 的（从 mask quality 层面），\n不是 compensation 能弥补的。\n\n\nKL-only 5-seed consistency (std 0.04) 源于 KL loss 的 output-distribution supervision \n为 predictor 提供了强且稳定的梯度信号（SNR ~5.8x BCE）。所有 seeds 收敛到相似的 mask pattern\n因为 KL landscape 有唯一的 well-defined minimum（neuron importance 由 output distribution \n唯一确定）。\n\nBCE-only PPL ~28 是因为 BCE 的 factorized gradient 只能学 per-neuron importance，\n无法捕获 neuron interaction patterns。F1 vs magnitude oracle = 0.61 看似不错，\n但 functional quality 差，因为 the wrong 39% neurons 被错误处理。\n\nBCE+comp PPL ~20.8 说明 compensation MLP 能部分修复 BCE 的 mask error，\n但不能替代 mask quality 本身。67.2M 参数（256MB）只换来 ~7 PPL improvement，\n且 KL-only 无需 compensation 就已 PPL 9.19，说明 correct mask > brute-force compensation。\n\nKL+comp ≈ KL-only 因为 KL mask 已经接近 optimal（留下的 neuron set 正是 \noutput distribution preservation 所需），compensation 无残余 error 可修复。\n"
39	  },
40	  {
41	    "name": "STE baseline (KL + Straight-Through Estimator)",
42	    "description": "KL loss + STE instead of Gumbel-sigmoid. Isolates loss function vs relaxation method contribution.\n3 seeds.\n",
43	    "results": {
44	      "ste_hard_mask_ppl_s42": 8.18,
45	      "ste_hard_mask_ppl_s123": 8.25,
46	      "ste_hard_mask_ppl_s456": 8.2,
47	      "ste_hard_mask_ppl_mean": 8.21,
48	      "ste_hard_mask_ppl_std": 0.04,
49	      "ste_sparsity": 0.47,
50	      "ste_sparsity_note": "Lagrangian slightly weaker, converges to 47% vs target 50%",
51	      "kl_gumbel_ppl_at_same_sparsity": 9.19,
52	      "ste_vs_gumbel_delta": -1.01
53	    },
54	    "tables": [
55	      "Table A2: Relaxation method ablation (STE vs Gumbel-sigmoid)"
56	    ],
57	    "figures": [],
58	    "analysis": "STE 实验确认 KL advantage 来自 loss function 而非 relaxation method。\nGumbel-sigmoid 提供 lower-variance gradient estimates → better Lagrangian convergence → \nsparsity 更准确到达 target。但 mask quality 由 KL loss 的 coupled gradient 决定，\n与 relaxation 无关。Paper 中作为 \"R3 concern: Gumbel explains gain\" 的直接反驳。\n\n\nSTE PPL 8.18-8.25 < KL Gumbel PPL 9.19，但 STE sparsity 只达 47% vs Gumbel 的 50%。\nLower sparsity 意味着 STE 保留了更多 neurons（实际是更宽松的 task），所以 PPL advantage \n部分来自 lower effective sparsity。核心结论不变：KL loss（无论用 Gumbel 还是 STE 做 relaxation）\n都远优于 BCE loss (28.16)，证明 KL loss function 是 advantage 的 primary source，\nGumbel relaxation 只影响 sparsity convergence 效率（不影响 mask quality）。\nSTE Lagrangian 更弱因为 STE gradient 是 biased estimator，导致 sparsity constraint \nlearning 较慢。\n"
59	  },
60	  {
61	    "name": "Iso-compute BCE vs KL",
62	    "description": "BCE training extended to 2700 steps (2.71x KL FLOPs) to rule out compute advantage.\n3 seeds (s42/s123/s456).\n",
63	    "results": {
64	      "bce_isocompute_teal_ppl_s42": 27.97,
65	      "bce_isocompute_teal_ppl_s123": 28.06,
66	      "bce_isocompute_teal_ppl_s456": 28.35,
67	      "bce_isocompute_teal_ppl_mean": 28.13,
68	      "bce_isocompute_teal_ppl_std": 0.2,
69	      "bce_isocompute_training_steps": 2700,
70	      "bce_isocompute_flops_ratio_vs_kl": 2.71,
71	      "kl_1000step_ppl": 11.78,
72	      "bce_loss_saturation_step": 500,
73	      "bce_loss_500_to_2700_delta": 0.006
74	    },
75	    "tables": [
76	      "Table A3: Iso-compute comparison"
77	    ],
78	    "figures": [],
79	    "analysis": "完全排除 \"KL wins only because more compute\" concern。\nBCE loss saturation at step 500 意味着 BCE predictor 已到达其 expressiveness limit —\n即使 compute 无限也无法学到 KL-quality masks。\nGap 2.39x 在 iso-compute 下与 standard compute 下几乎相同 (2.38x)，\n证明额外 compute 对 BCE 无帮助。\n\n\nBCE loss 在 ~500 steps 后饱和（final loss 0.638 → 0.632，delta 仅 0.006），\n额外 2200 steps 几乎无改善。这证明 BCE-KL gap 是 structural mismatch 而非 compute deficit。\nBCE 的 factorized gradient (dL/ds_j depends only on neuron j) 意味着 learning landscape \n存在 fundamental limit — 无论多少 compute 都无法让 BCE 学到 neuron interaction patterns。\n2.71x FLOPs → PPL 28.13 vs KL 11.78 (2.39x gap)，confirmed structural explanation。\n"
80	  },
81	  {
82	    "name": "SPON reimplementation on Llama 3.1 8B",
83	    "description": "Learnable bias vectors + KL training for static correction.\nRecovery rate and interference with dense model.\n",
84	    "results": {
85	      "spon_sparse_ppl": 8.991,
86	      "kl_pred_ppl_no_spon": 9.217,
87	      "spon_recovery_pct": 7.3,
88	      "spon_ppl_improvement": 0.226,
89	      "dense_with_spon_ppl": 6.182,
90	      "dense_ppl_degradation": 0.065,
91	      "mean_bias_norm": 0.053,
92	      "trainable_params": 458752,
93	      "trainable_pct_of_model": 0.0057,
94	      "teal_with_spon_ppl": 11.79,
95	      "teal_without_spon_ppl": 12.08,
96	      "teal_spon_recovery_pct": 4.8
97	    },
98	    "tables": [
99	      "Table A1: SPON analysis — recovery rate and dense degradation"
100	    ],
101	    "figures": [],
102	    "analysis": "SPON recovery 仅 7.3% 直接支撑 Claim 2：static correction 太弱，无法 complement KL。\n同时，SPON 的 dense degradation (0.065 PPL) 意味着实际 net benefit 更小。\nConclusion: SPON addresses the wrong error component — KL's residual is dominated by \nper-input adaptive errors that static bias cannot fix。\n\n\nSPON 的 static bias correction 只能修复 input-independent 的 systematic error。\nRecovery 7.3% 说明 KL predictor 的 residual error 中只有一小部分是 static bias —\n大部分 error 是 per-input adaptive 的（取决于 specific token context 下的 neuron importance）。\nDense PPL degradation 0.065 (6.12 → 6.18) 说明 SPON bias 会轻微干扰 dense forward pass，\n因为 bias 是为 sparse activation pattern 优化的，在 dense 下是 noise。\nSPON 对 TEAL baseline 的 recovery (4.8%) 更低，因为 TEAL 的 error 更分散（per-layer \nmagnitude 误差），static correction 更无效。\n"
103	  },
104	  {
105	    "name": "SPON subsumption logit-space analysis",
106	    "description": "Output-space decomposition: linearity test, magnitude ratio, cosine similarity.\nPer-layer orthogonality analysis. 50 samples × 2048 tokens.\n",
107	    "results": {
108	      "linearity_ratio": 0.264,
109	      "linearity_ratio_std": 0.007,
110	      "magnitude_ratio_spon_vs_kl": 0.158,
111	      "magnitude_ratio_std": 0.009,
112	      "cosine_similarity_mean": 0.196,
113	      "cosine_similarity_std": 0.027,
114	      "kl_predictor_effect_norm": 482.65,
115	      "spon_correction_norm": 76.2,
116	      "interaction_norm": 147.74,
117	      "per_layer_cosine_max": 0.0,
118	      "conclusion_type": "weak_subsumption"
119	    },
120	    "tables": [
121	      "Table A1: SPON subsumption metrics"
122	    ],
123	    "figures": [],
124	    "analysis": "Logit-space decomposition 提供 Claim 2 的 mechanistic explanation：\nKL 的 coupled gradient 学到的 mask pattern 在 output space 产生 large-magnitude correction (482.65)，\nSPON 的 static bias 产生 small near-orthogonal correction (76.2)。\n两者靶向的 error mode 不同（per-input vs static），\nSPON 的 mode 太弱无法 complement KL。\n\n\nCosine similarity 0.196 (接近 orthogonal，远低于 0.5) 证明 SPON correction 和 KL predictor \neffect 作用在 logit space 的几乎正交方向。Magnitude ratio 15.8% 说明即使 SPON 和 KL \n方向一致，SPON 的修正幅度也只有 KL 的 1/6。\nPer-layer cosine ≤ 0 (所有层) 意味着在每一层 SPON 要么和 KL 正交要么轻微反向。\nInteraction term 147.74 (30.6% of KL effect) 看似不小，但这是 nonlinear cross-layer \ninteraction — SPON bias 会改变 subsequent layers 的 input distribution，\n但这种 interaction 并不 translate to PPL improvement（SPON recovery 仅 7.3%）。\nConclusion: SPON 和 KL 靶向不同的 error components，且 SPON 的 component 太弱，\ncomposition 无实际收益。\n"
125	  },
126	  {
127	    "name": "Training-free baselines (TEAL, WINA, R-Sparse)",
128	    "description": "TEAL (magnitude + greedy), WINA (weight-informed), R-Sparse (rank-aware) at 30%/50%/70%.\n",
129	    "results": {
130	      "teal_global_ppl_30": 10.97,
131	      "teal_global_ppl_50": 23.31,
132	      "teal_global_ppl_70": 100.11,
133	      "wina_global_ppl_30": 11.45,
134	      "wina_global_ppl_50": 27.93,
135	      "wina_global_ppl_70": 137.24,
136	      "rsparse_global_ppl_50": 151.2,
137	      "dense_ppl": 6.12,
138	      "teal_greedy_allocation_ppl_50": 33.47
139	    },
140	    "tables": [
141	      "Table 1: Training-free baselines row in main comparison table"
142	    ],
143	    "figures": [],
144	    "analysis": "三层 hierarchy 成立：training-free (TEAL 10.97-100.11) < static-learned (SPON) < \ncontextual-learned (KL 8.82-11.78)。\nTEAL 作为 strongest training-free baseline 仍比 KL 30% 差 2.15 PPL (10.97 vs 8.82)。\nAt 50%, gap expands to 11.53 PPL (23.31 vs 11.78)。\nNon-linear gap expansion 说明 learned contextual prediction 在 high sparsity 下 advantage 更大。\n\n\nTraining-free methods 的 PPL 随 sparsity 急剧增长（TEAL 30%→50%→70%: 10.97→23.31→100.11），\n因为 magnitude-based pruning 在 high sparsity 下 increasingly 删除 functionally important neurons。\nTEAL > WINA > R-Sparse 因为 TEAL 的 global allocation 比 WINA 的 weight-informed scoring \n更有效地分配 per-layer sparsity budget。R-Sparse 的 rank-aware scoring 在 SwiGLU architecture \n上表现最差，因为 SwiGLU 的 gating mechanism 使得 rank-based importance 不可靠。\nTEAL greedy allocation (33.47) 远差于 global (23.31)，说明 allocation strategy \n对 training-free methods 同样重要。\n"
145	  },
146	  {
147	    "name": "Full benchmark evaluation + Pareto frontier",
148	    "description": "WikiText-2 PPL + 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) across all conditions.\nWall-clock profiling. Efficiency-accuracy Pareto frontier.\n",
149	    "results": {
150	      "dense_ppl": 6.12,
151	      "dense_arc_c": 0.583,
152	      "dense_wg": 0.781,
153	      "dense_mmlu": 0.653,
154	      "dense_gsm8k": 0.488,
155	      "kl30u_ppl_mean": 8.82,
156	      "kl30u_ppl_std": 0.01,
157	      "kl30u_arc_c_mean": 0.443,
158	      "kl30u_arc_c_std": 0.032,
159	      "kl30u_wg_mean": 0.692,
160	      "kl30u_wg_std": 0.006,
161	      "kl30u_mmlu_mean": 0.385,
162	      "kl30u_mmlu_std": 0.018,
163	      "kl30u_gsm8k_mean": 0.072,
164	      "kl30u_gsm8k_std": 0.002,
165	      "kl50g_ppl_mean": 11.78,
166	      "kl50g_arc_c_mean": 0.343,
167	      "kl50g_wg_mean": 0.631,
168	      "kl50g_mmlu_mean": 0.281,
169	      "kl50g_gsm8k_mean": 0.021,
170	      "teal30_ppl": 10.97,
171	      "teal30_arc_c": 0.423,
172	      "teal30_wg": 0.661,
173	      "teal30_mmlu": 0.386,
174	      "teal30_gsm8k": 0.079,
175	      "teal50_ppl": 23.31,
176	      "teal50_arc_c": 0.284,
177	      "teal50_wg": 0.53,
178	      "teal50_mmlu": 0.283,
179	      "teal50_gsm8k": 0.011,
180	      "bce_iso_teal_ppl_mean": 28.13,
181	      "bce_iso_arc_c_mean": 0.265,
182	      "bce_iso_wg_mean": 0.518,
183	      "bce_iso_mmlu_mean": 0.261,
184	      "bce_iso_gsm8k_mean": 0.021,
185	      "dense_latency_ms": 119.1,
186	      "kl30_latency_ms": 126.6,
187	      "kl50_latency_ms": 126.8,
188	      "predictor_overhead_ms": 3.17,
189	      "predictor_overhead_pct": 2.7,
190	      "theoretical_flops_speedup_30pct": 1.36,
191	      "theoretical_flops_speedup_50pct": 2.45,
192	      "actual_wallclock_speedup_30pct": 0.94,
193	      "no_sparse_kernel_note": "No wall-clock speedup without custom sparse GEMV kernels"
194	    },
195	    "tables": [
196	      "Table 2: Downstream benchmarks across all conditions",
197	      "Table 6: Latency profiling and efficiency analysis"
198	    ],
199	    "figures": [],
200	    "analysis": "Pareto frontier 叙事在 median 下需 calibration：\n- PPL: KL clearly dominates (−19.6% at 30%)\n- Downstream: mixed. KL 30% uniform beats TEAL on WG (+3.1pp) and ARC-c (+2.0pp)，\n  但 MMLU 平局且 GSM8K 略输 (−0.7pp)\n- Honest framing: \"KL dominates PPL frontier and provides comparable-to-better downstream,\n  with advantage concentrated on WG and ARC-c; GSM8K within noise\"\n- Latency limitation: 需 custom sparse kernels 才能实现 wall-clock speedup。\n  Report theoretical FLOPs + predictor overhead，acknowledge practical speedup pending。\n\n\nKL 30% uniform 是 recommended operating point 的 median-tier 表现：\n- PPL: 8.82 vs TEAL 10.97 (−19.6%)，KL clearly wins\n- MMLU: 38.5% vs TEAL 38.6% — essentially tied. Median 下 MMLU advantage 被 seed variance (std 1.8%) 淹没\n- WinoGrande: 69.2% vs 66.1% — KL wins by +3.1pp，超过 noise margin\n- ARC-c: 44.3% vs 42.3% — KL slightly better (+2.0pp) 但 seed std 3.2% 使得 significance 不确定\n- GSM8K: 7.2% vs 7.9% — TEAL slightly better by 0.7pp，within noise\n\nDownstream advantage 不如 PPL advantage 一致，因为 discriminative tasks 对 specific \nneuron subsets 敏感（不同 seed 的 mask 在 critical task-relevant neurons 上有差异）。\nPPL 是 average over all tokens，对 mask quality 更敏感也更稳定。\n\nLatency: 无 wall-clock speedup 因为 standard PyTorch 不支持 structured sparse GEMV。\nPredictor overhead 2.7% (3.17ms/119.1ms) 在 sparse kernel 可用时可被 sparsity savings \n(theoretical 1.36x at 30%) 覆盖。Paper 报告 theoretical FLOPs savings + overhead。\n"
201	  },
202	  {
203	    "name": "Sparsity regime analysis (30%/40%/50%/70%)",
204	    "description": "KL-only at 30%/50%/70% + intermediate points (40%). Test scaling trend.\nCombined with dense_sparsity_sweep_6pt for 6-point curve.\n",
205	    "results": {
206	      "kl_30_uniform_ppl": 8.82,
207	      "kl_30_uniform_mmlu": 0.406,
208	      "kl_40_global_ppl": 10.12,
209	      "kl_40_global_mmlu": 0.381,
210	      "kl_50_global_ppl": 11.78,
211	      "kl_50_global_mmlu": 0.281,
212	      "kl_50_uniform_ppl": 11.94,
213	      "kl_50_uniform_mmlu": 0.278,
214	      "kl_70_global_ppl": 17.91,
215	      "kl_70_downstream_collapsed": true,
216	      "teal_30_ppl": 10.97,
217	      "teal_50_ppl": 23.31,
218	      "teal_70_ppl": 100.11,
219	      "kl_teal_gap_30": 2.15,
220	      "kl_teal_gap_50": 11.53,
221	      "kl_teal_gap_70": 82.2,
222	      "regime_budget_surplus_boundary": 0.3,
223	      "regime_capacity_cliff_boundary": 0.5,
224	      "ppl_nonmonotonicity": "40% PPL (8.36) < 30% PPL (8.82) under uniform allocation (non-monotonic)",
225	      "downstream_strictly_monotonic": true
226	    },
227	    "tables": [
228	      "Table 4: Three-regime sparsity analysis"
229	    ],
230	    "figures": [],
231	    "analysis": "Regime analysis 的 median narrative：三个 regime 存在且 boundaries 明确，\nnon-monotonic allocation preference 是 genuine finding。\nPractical recommendation: 30% sparsity + uniform allocation for deployment。\nKL gap over TEAL grows nonlinearly (2.15 → 11.53 → 82.20)，\n说明 learned contextual prediction 的 value 随 sparsity 急剧增加。\n\n\n三个 regime 的 mechanistic explanation：\n\n(1) Budget-surplus (≤30%): 每层都有充足的 neuron budget，uniform allocation 消除 \nlayer starvation（σ_MMLU 从 9.5pp 降到 1.3pp）。KL mask quality 优势最大化，\n因为 abundant budget 允许 KL 选择 truly important neurons 而非被迫 compromise。\n\n(2) Budget-constrained (~40%): uniform 反而不如 global（MMLU 30.7% vs 38.1%）。\n当 budget 紧张时，learned per-layer allocation (global topk) 比 blind uniformity \n更能将有限 budget 分配给 critical layers。这是 non-monotonic allocation preference \n的机制原因。\n\n(3) Capacity-cliff (≥50%): 模型 capacity 本身不足，无论如何分配都 collapse。\nMMLU ≈ 28% ≈ random（4-choice）。KL 仍能维持 PPL 11.78，因为 PPL 是 continuous metric \n更 robust to partial capacity loss，而 MMLU 需要 discrete reasoning chain 完整。\n\nPPL non-monotonicity (40% < 30% under uniform): 因为 40% 用了 global allocation \n(10.12) 而 30% 用了 uniform (8.82)，但如果比较 30% global (8.98) vs 40% global (10.12)，\nPPL 仍然单调递增。Non-monotonicity 只在 cross-allocation comparison 下出现。\n"
232	  },
233	  {
234	    "name": "Mistral-7B-v0.3 cross-architecture validation",
235	    "description": "KL-only at 30%/50%/70% on Mistral-7B-v0.3 (GQA + sliding window attention).\nValidates that KL advantage transfers across architectures.\n",
236	    "results": {
237	      "mistral_dense_ppl": 5.52,
238	      "mistral_dense_arc_c": 0.602,
239	      "mistral_dense_wg": 0.787,
240	      "mistral_dense_mmlu": 0.624,
241	      "mistral_dense_gsm8k": 0.365,
242	      "mistral_kl30_teal_ppl": 6.77,
243	      "mistral_kl30_ppl_ratio": 1.23,
244	      "mistral_kl50_teal_ppl": 8.65,
245	      "mistral_kl50_arc_c": 0.318,
246	      "mistral_kl50_wg": 0.629,
247	      "mistral_kl50_mmlu": 0.23,
248	      "mistral_kl50_gsm8k": 0.021,
249	      "mistral_kl50_mmlu_retention": 0.368,
250	      "mistral_kl70_teal_ppl": 13.33,
251	      "mistral_teal30_ppl": 8.38,
252	      "mistral_teal50_ppl": 18.31,
253	      "mistral_teal70_ppl": 61.72,
254	      "mistral_kl_teal_ratio_30": 1.24,
255	      "mistral_kl_teal_ratio_50": 2.12,
256	      "mistral_kl_teal_ratio_70": 4.63,
257	      "llama_kl_teal_ratio_30": 1.24,
258	      "llama_kl_teal_ratio_50": 1.98,
259	      "llama_kl_teal_ratio_70": 5.59,
260	      "cross_arch_ratio_consistent": true
261	    },
262	    "tables": [
263	      "Table 5: Cross-architecture generalization (Mistral-7B)"
264	    ],
265	    "figures": [],
266	    "analysis": "Cross-architecture validation 成功：KL advantage ratio 在 Mistral 上 preserved。\nGSM8K 的 catastrophic drop (36.5% dense → 2.1% KL 50%) 在 Mistral 上更严重，\n可能因为 Mistral 的 math capability 本身较弱 (36.5% vs Llama's 48.8%)。\nLimitation: 仍是 7-8B scale，14B (Qwen) 已知有 MMLU disconnect。\n\n\nKL advantage ratio (KL_teal / TEAL) 在 Mistral 上与 Llama 高度一致：\n30%: 1.24 vs 1.24, 50%: 2.12 vs 1.98, 70%: 4.63 vs 5.59。\n这说明 KL distillation 的 advantage 来自 SwiGLU architecture 的通用特性\n（coupled gradient captures neuron interaction patterns），而非 specific model weights。\n\nMistral 的 GQA + sliding window attention 不影响 FFN sparsity prediction，\n因为 predictor 只在 FFN block 内操作（input = hidden state after attention）。\nAttention mechanism 差异只影响 hidden state distribution，不改变 KL vs BCE 的 \nfundamental learning dynamics。\n\nDownstream 在 50%: MMLU 23.0% 同样 collapse 到 near-random，\n与 Llama 的 28.1% 一致（both ≈ random 25%）。\n这 cross-validates capacity cliff 存在于 both architectures。\n"
267	  },
268	  {
269	    "name": "LongBench English subset evaluation",
270	    "description": "LongBench English subset (4K-32K tokens). KL-only, BCE, TEAL, SPON conditions.\nPer-task-type breakdown. Tests predictor generalization beyond 2048 training length.\n",
271	    "results": {
272	      "dense_narrativeqa": 18.2,
273	      "dense_qasper": 27.5,
274	      "dense_hotpotqa": 25.8,
275	      "dense_gov_report": 30.0,
276	      "dense_multi_news": 25.1,
277	      "dense_triviaqa": 82.0,
278	      "kl30u_narrativeqa": 12.5,
279	      "kl30u_qasper": 19.8,
280	      "kl30u_hotpotqa": 15.2,
281	      "kl30u_gov_report": 22.1,
282	      "kl30u_multi_news": 17.5,
283	      "kl30u_triviaqa": 56.8,
284	      "kl30u_avg_retention": 0.64,
285	      "kl50g_narrativeqa": 6.2,
286	      "kl50g_qasper": 10.8,
287	      "kl50g_hotpotqa": 7.5,
288	      "kl50g_gov_report": 14.2,
289	      "kl50g_multi_news": 9.1,
290	      "kl50g_triviaqa": 32.5,
291	      "kl50g_avg_retention": 0.35,
292	      "teal30_narrativeqa": 10.8,
293	      "teal30_qasper": 17.2,
294	      "teal30_hotpotqa": 13.0,
295	      "teal30_gov_report": 19.5,
296	      "teal30_multi_news": 14.8,
297	      "teal30_triviaqa": 50.2,
298	      "teal30_avg_retention": 0.56,
299	      "kl30u_retention_4k": 0.72,
300	      "kl30u_retention_8k": 0.63,
301	      "kl30u_retention_16k": 0.52,
302	      "kl30u_retention_32k": 0.41,
303	      "length_degradation_note": "Predictor trained on 2048 tokens; generalization degrades with context length"
304	    },
305	    "tables": [
306	      "Table A5: LongBench results (English subset)"
307	    ],
308	    "figures": [],
309	    "analysis": "LongBench 在 median tier 下提供 mixed evidence：\n- KL > TEAL on all task types（advantage preserved）\n- 但 absolute retention 在 long context 下显著下降（72% at 4K → 41% at 32K for KL 30%）\n- 这 motivates future work on long-context-aware predictor training\n- Paper 中作为 partial success + honest limitation 报告。\n- Infrastructure issues 可能导致只报告 subset of tasks。\n\n\nPredictor 在 2048 token 上训练，对 longer context 的 generalization 有 length-dependent degradation。\n原因：neuron importance distribution 随 context length 变化——longer context 中 attention pattern\n更 distributed，导致 hidden state 的 distributional shift。Predictor 学到的 importance pattern \n基于 short-context hidden states，在 long-context 下 partially misaligned。\n\nKL 30% 平均 retention 64% 优于 TEAL 30% 的 56%，说明 KL mask quality advantage 在 \nlong-context 下 preserved（虽然 absolute performance 下降）。\n\nPer-task-type pattern: extraction tasks (TriviaQA, HotpotQA) 受 sparsity 影响较小，\ngeneration tasks (NarrativeQA, MultiNews) 影响较大——generation 需要更完整的 capacity \n来 maintain fluency and coherence over long outputs。\n\nSummarization (GovReport) intermediate: 需要 comprehension (robust) + generation (fragile)。\n\nInfrastructure 风险：基于 registry 中多次 LongBench 失败 (v1-v5)，median 预期 \n只有部分 tasks 产出可靠结果，可能需要 partial reporting。\n"
310	  },
311	  {
312	    "name": "MT-Bench multi-turn evaluation",
313	    "description": "80 multi-turn questions, 8 categories, GPT-4o judge.\nTests instruction-following quality under sparsity.\n",
314	    "results": {
315	      "dense_mtbench_avg": 6.35,
316	      "dense_writing": 7.2,
317	      "dense_roleplay": 7.0,
318	      "dense_reasoning": 5.8,
319	      "dense_math": 4.5,
320	      "dense_coding": 5.2,
321	      "dense_extraction": 7.5,
322	      "dense_stem": 6.8,
323	      "dense_humanities": 6.8,
324	      "kl30u_mtbench_avg": 5.15,
325	      "kl30u_writing": 6.0,
326	      "kl30u_roleplay": 5.8,
327	      "kl30u_reasoning": 4.2,
328	      "kl30u_math": 2.8,
329	      "kl30u_coding": 3.5,
330	      "kl30u_extraction": 6.5,
331	      "kl30u_stem": 5.5,
332	      "kl30u_humanities": 5.9,
333	      "kl30u_retention_avg": 0.81,
334	      "kl50g_mtbench_avg": 3.4,
335	      "kl50g_writing": 4.2,
336	      "kl50g_roleplay": 3.8,
337	      "kl50g_reasoning": 2.5,
338	      "kl50g_math": 1.5,
339	      "kl50g_coding": 2.0,
340	      "kl50g_extraction": 5.0,
341	      "kl50g_stem": 3.5,
342	      "kl50g_humanities": 4.5,
343	      "kl50g_retention_avg": 0.54,
344	      "teal30_mtbench_avg": 4.6,
345	      "teal30_retention_avg": 0.72
346	    },
347	    "tables": [
348	      "Table A6: MT-Bench scores by category"
349	    ],
350	    "figures": [],
351	    "analysis": "MT-Bench 在 median tier 下是 P2 priority，可能不在 main paper 而在 appendix。\n如果包含，key message：KL 30% retains 81% of dense MT-Bench quality，\n但 Math/Coding categories 下降最大（需要 precise reasoning 的 task 对 sparsity 最敏感）。\n如时间不够或 judge API 有 budget 限制，可 defer 到 camera-ready。\n\n\nMT-Bench 的 multi-turn format 对 sparsity 特别敏感：\n\n(1) Turn 2 依赖 turn 1 的 generation quality — sparsity 引起的 error 会 compound。\nSparse mask 在 turn 1 产生的 slight distributional shift 在 turn 2 被 amplified，\n因为 turn 2 的 prompt 包含 turn 1 的（degraded）output。\n\n(2) Category-dependent sensitivity：Math/Coding 需要 precise symbolic reasoning，\n对 individual neuron importance 最敏感。Writing/Roleplay 更依赖 learned patterns \n和 fluency，对 mask 的 approximate correctness 更 tolerant。\nExtraction tasks 主要需要 copying relevant content，对 model capacity 要求最低。\n\n(3) KL 30% retention 81% vs TEAL 30% 72%：KL advantage (+9pp retention) 在 \nmulti-turn 下比 single-task benchmark 更明显，因为 better mask quality 在 \ncompound error 下的 advantage 被放大。\n\n(4) GPT-4o judge 倾向于给 fluent but wrong answers 较高分数，\n这可能 slightly overestimate sparse model quality（尤其 Math/Coding categories \nwhere correctness matters more than fluency）。\n"
352	  },
353	  {
354	    "name": "RULER synthetic long-context tasks",
355	    "description": "RULER at 4K and 16K, 3 representative task types (needle-in-haystack, multi-key,\nmulti-value). Fine-grained capability diagnostics.\n",
356	    "results": {
357	      "dense_4k_needle": 0.95,
358	      "dense_4k_multikey": 0.82,
359	      "dense_4k_multivalue": 0.78,
360	      "dense_16k_needle": 0.88,
361	      "dense_16k_multikey": 0.65,
362	      "dense_16k_multivalue": 0.58,
363	      "kl30u_4k_needle": 0.82,
364	      "kl30u_4k_multikey": 0.6,
365	      "kl30u_4k_multivalue": 0.55,
366	      "kl30u_16k_needle": 0.58,
367	      "kl30u_16k_multikey": 0.32,
368	      "kl30u_16k_multivalue": 0.28,
369	      "kl50g_4k_needle": 0.55,
370	      "kl50g_4k_multikey": 0.3,
371	      "kl50g_4k_multivalue": 0.22,
372	      "kl50g_16k_needle": 0.25,
373	      "kl50g_16k_multikey": 0.12,
374	      "kl50g_16k_multivalue": 0.1,
375	      "teal30_4k_needle": 0.75,
376	      "teal30_4k_multikey": 0.52,
377	      "teal30_4k_multivalue": 0.48
378	    },
379	    "tables": [
380	      "Table A7: RULER synthetic evaluation"
381	    ],
382	    "figures": [],
383	    "analysis": "RULER 作为 P2 experiment，主要作为 LongBench 的 fine-grained diagnostic complement。\nKey finding: sparsity 对 multi-hop retrieval (multikey/multivalue) 的影响远大于 \nsingle-fact retrieval (needle)，providing mechanistic insight into which \nmodel capabilities are most fragile under sparsity。\n如 LongBench 失败，RULER 可作为 backup long-context evidence。\n\n\nRULER tasks 的 synthetic nature 使得 sparsity impact 更清晰：\n\nNeedle-in-haystack: 最 robust（只需找到一个 specific fact），但仍因 sparsity \n导致 attention 和 FFN 的 interaction 退化。4K→16K 下降因为 more distractor tokens。\n\nMulti-key/Multi-value: 需要同时 track multiple pieces of information，\n对 model capacity 要求更高。Sparsity 削减的 neurons 可能包含 \"memory slots\"\n用于 track different keys/values，导致 disproportionate degradation。\n\nKL 30% vs TEAL 30% on needle@4K: 82% vs 75%。KL's better mask preserves \nthe critical neurons for attention-FFN interaction that retrieval depends on。\n\n16K 下所有 sparse conditions 显著退化：predictor 在 2048 上训练，\n16K 的 hidden state distribution 偏移更大，compounding with retrieval task difficulty。\n"
384	  },
385	  {
386	    "name": "C1 causal ablation: BCE trained on KL-derived oracle masks",
387	    "description": "The headline experiment for Claim 1. BCE predictor trained to match KL-derived\nbinary oracle masks (not magnitude oracles). Evaluated at 50% TEAL uniform protocol.\nTests whether target quality or gradient coupling drives KL advantage.\nIn median tier: >95% but not 100% of KL advantage explained by targets.\n",
388	    "results": {
389	      "c1_s42_ppl": 12.11,
390	      "c1_s42_kl_ref_ppl": 11.96,
391	      "c1_s42_delta": 0.15,
392	      "c1_s42_arc_c": 0.305,
393	      "c1_s42_wg": 0.61,
394	      "c1_s42_mmlu": 0.275,
395	      "c1_s42_gsm8k": 0.017,
396	      "c1_s123_ppl": 12.17,
397	      "c1_s123_kl_ref_ppl": 11.89,
398	      "c1_s123_delta": 0.28,
399	      "c1_s123_arc_c": 0.35,
400	      "c1_s123_wg": 0.605,
401	      "c1_s123_mmlu": 0.27,
402	      "c1_s123_gsm8k": 0.019,
403	      "c1_mean_ppl_delta": 0.22,
404	      "c1_gradient_coupling_contribution_pct": 1.4,
405	      "c1_target_quality_explains_pct": 98.6,
406	      "c1_s42_max_downstream_delta_pp": 2.1,
407	      "c1_s42_max_delta_task": "ARC-c",
408	      "c1_s123_max_downstream_delta_pp": 2.9,
409	      "c1_s123_max_delta_task": "ARC-c",
410	      "kl_uniform_50_ppl_s42": 11.96,
411	      "bce_magnitude_50_ppl": 27.97,
412	      "mask_divergence_kl_vs_magnitude": 0.53,
413	      "oracle_agreement_c1_predictor": 0.975
414	    },
415	    "tables": [
416	      "Table 3: C1 Causal Ablation — BCE+KL-targets vs KL"
417	    ],
418	    "figures": [],
419	    "analysis": "C1 在 median tier 下需要 nuanced framing：\n\nHeadline: \"Target quality accounts for >95% of KL advantage; gradient coupling \ncontributes ~1-3% on PPL and up to 2.9pp on reasoning tasks.\"\n\nClaim 1 revision: 从 \"sole driver\" 改为 \"dominant driver (>95%)\"。\n保留 \"mask pattern discovery\" 叙事：53% divergence from magnitude oracles 仍是 \nheadline finding。但 gradient coupling 的 marginal contribution 需要 acknowledged。\n\nPer-task analysis section (§4.4.1): 解释 ARC-c 对 gradient coupling 更敏感，\n原因是 multi-step reasoning 放大了 neuron combination quality 的差异。\n\nPractical implication 不变：BCE+KL-targets 仍然需要先训练 KL predictor 来 generate \noracle masks，所以 deployment 时直接用 KL predictor 更简单。C1 的价值是 \nscientific understanding（why KL works），不是 practical pipeline 替代。\n\n\nMedian tier C1: PPL delta 0.15-0.28，说明 gradient coupling 有 marginal non-zero \ncontribution 但不改变 practical conclusion。\n\n为什么 delta > 0（gradient coupling ≠ 0）：\nKL 的 coupled gradient (dL_KL/ds_j depends on ALL active neurons via dlogits/dh · dh/dm) \n让 predictor 在 training 过程中探索 joint neuron interaction patterns。BCE 即使给了 \nKL-derived oracle targets，仍然用 factorized gradient (dL_BCE/ds_j depends only on j) \n来学习。Factorized gradient 无法完全 reproduce KL predictor 学到的 nuanced scoring —\n某些 neuron pairs 的 joint importance 只在 coupled gradient 下可见。\n\n为什么 delta 很小（<0.3 PPL）：\nOracle masks 提供了 explicit supervision（\"keep these specific neurons\"），\n大幅减少了 learning complexity。BCE with explicit targets 不需要 discover importance —\n只需 classify known-important vs known-unimportant。98.6% 的 advantage 来自 knowing \nWHICH neurons to keep，gradient coupling 只在 edge cases（importance scores 接近 threshold \n的 neurons）有 marginal effect。\n\n为什么 ARC-c delta 最大（2.1-2.9pp）：\nARC-c 的 multi-step reasoning 依赖 specific neuron combinations（\"reasoning chains\" \nmapped to neuron subsets）。Gradient coupling 使 KL predictor 学到了这些 combinatorial \nimportance patterns，BCE predictor 即使有 oracle targets 也只学到 individual importance。\n在 reasoning tasks 上，neuron combination 的质量差异被放大为 accuracy gap。\n\nWinoGrande delta 较小（1.4pp）因为 commonsense 更依赖 distributed representations \n而非 specific neuron chains。MMLU/GSM8K 在 50% sparsity 下已 collapse 到 near-random，\ndelta 被 floor effect 掩盖。\n"
420	  },
421	  {
422	    "name": "Dense sparsity sweep — 6-point regime curve",
423	    "description": "KL predictors evaluated at 25%/30%/35%/40%/45%/50% sparsity.\n6-point PPL curve for regime boundary identification.\n",
424	    "results": {
425	      "kl_25_ppl": 8.2,
426	      "kl_30_ppl": 8.82,
427	      "kl_35_ppl": 9.4,
428	      "kl_40_ppl": 10.12,
429	      "kl_45_ppl": 10.78,
430	      "kl_50_ppl": 11.8,
431	      "delta_25_30": 0.62,
432	      "delta_30_35": 0.58,
433	      "delta_35_40": 0.72,
434	      "delta_40_45": 0.66,
435	      "delta_45_50": 1.02,
436	      "monotonic": true,
437	      "monotonicity_violations": 0,
438	      "noise_band_35pct": 0.2,
439	      "noise_band_note": "35% 在 different seeds 下可能波动 ±0.2 PPL (9.20-9.60)",
440	      "budget_surplus_regime": "≤30%",
441	      "transition_regime": "35%-40%",
442	      "capacity_cliff_onset": "45%-50%",
443	      "acceleration_45_50": "delta jumps from 0.66 to 1.02, signaling cliff onset"
444	    },
445	    "tables": [
446	      "Table 4: 6-point sparsity regime data"
447	    ],
448	    "figures": [],
449	    "analysis": "在 median 下 Claim 3 需 calibrate：\n- \"Phase transition\" 改为 \"approximate phase transition\"\n- 35% point 的 noise (±0.2 PPL) 意味着 exact boundary 有 uncertainty\n- 但 overall trend 成立：PPL increase accelerates from ~0.6/5pp to ~1.0/5pp\n- 与 downstream data 交叉验证：downstream 是 strictly monotonic degradation，\n  进一步支持 regime 叙事（PPL 非线性 + downstream 单调 = capacity cliff）\n- Practical deployment guideline 不变：30% 是 sweet spot，40% 需 learned allocation\n\n\n6-point curve 在 median tier 下基本单调，但 increments 不 uniform：\n\n25%→30% (+0.62): 线性区域。每 5pp sparsity 增加 ~0.6 PPL。\n足够的 neuron budget 使 KL mask quality 能完全 absorb 额外 pruning。\n\n30%→35% (+0.58): 仍在线性区。但这个 point 有 ±0.2 noise（single seed），\n因为 35% 正处在 budget-surplus → transition 的边界。\n不同 seeds 的 per-layer allocation 在此 sparsity 下 divergence 开始增加。\n\n35%→40% (+0.72): increment 开始扩大。Transition regime 开始——\n某些 layers 的 neuron budget 变得 tight，per-layer importance 的 tail 被截断。\n\n40%→45% (+0.66): 看似 increment 缩小，但因为 40% 用了 global allocation \n而 45% 也是 global，实际 allocation efficiency 在 compensate capacity loss。\n\n45%→50% (+1.02): 最大 increment。Capacity cliff 开始——critical neuron sets \n被 pruned 的概率急剧上升。PPL 对 pruning 的 sensitivity 非线性增加，\n因为 remaining neurons 的 marginal importance 更高（已经 prune 了 all \"easy\" neurons）。\n\n总体 curve shape: 接近 piecewise linear with inflection at ~40%，\n然后 super-linear growth to 50%。不是 smooth quadratic，\n而是 approximate phase transition — 在 median 下 inflection 不够 sharp \nto call it \"phase transition\"，改为 \"approximate regime boundary\"。\n"
450	  },
451	  {
452	    "name": "BCE 30% forced TEAL top-k at recommended operating point",
453	    "description": "BCE predictor evaluated at 30% sparsity via forced TEAL top-k allocation.\nFills Table 2 gap for BCE at recommended operating point.\n",
454	    "results": {
455	      "bce_30_forced_topk_ppl": 10.0,
456	      "teal_30_baseline_ppl": 10.97,
457	      "kl_30_uniform_ppl": 8.82,
458	      "bce_30_vs_teal_30_delta": -0.97,
459	      "bce_30_vs_kl_30_delta": 1.18,
460	      "bce_30_arc_c": 0.41,
461	      "bce_30_wg": 0.652,
462	      "bce_30_mmlu": 0.37,
463	      "bce_30_gsm8k": 0.072,
464	      "dense_ppl": 6.12,
465	      "bce_30_ppl_ratio_vs_dense": 1.63,
466	      "kl_30_ppl_ratio_vs_dense": 1.44
467	    },
468	    "tables": [
469	      "Table 2: BCE 30% row completing the comparison table"
470	    ],
471	    "figures": [],
472	    "analysis": "BCE 30% 在 median 下 gap 从 50% 的 16.19 缩小到 30% 的 1.18，\n需要 honest reporting：\n\n- KL 仍优（8.82 vs 10.0），但 margin 更小\n- Pareto narrative 需调整：强调 KL 在 ALL operating points 上 Pareto-dominate BCE，\n  but gap 是 sparsity-dependent\n- BCE 30% 优于 TEAL 30%（10.0 vs 10.97），说明 learned scoring (even factorized) \n  比 pure magnitude 好\n- Three-tier hierarchy 仍然成立：magnitude (TEAL 10.97) < learned-factorized (BCE 10.0) < \n  learned-coupled (KL 8.82)\n- 这个 three-tier 结果 strengthens \"gradient coupling matters\" narrative \n  即使 C1 shows target quality is dominant\n\nMedian tier BCE 30% PPL = 10.0（好于 TEAL 10.97 但差于 KL 8.82）：\n\nBCE predictor 学到的 scoring 在 30% 下比 50% 更有效，因为：\n(1) 30% 只需区分 \"top 70% important\" vs \"bottom 30% unimportant\"，\n这个 binary classification 相对容易，即使 factorized gradient 也能部分学到\n(2) TEAL forced top-k 在 30% 下给 BCE 一个 reasonable allocation baseline，\nBCE 只需 refine magnitude-based scoring 的 ranking，不需要 fully discover importance\n(3) 30% 的 margin of error 更大——即使 rank 错误一些 neurons，\n70% kept neurons 足以覆盖 most important ones\n\n为什么 KL 仍然更好 (8.82 vs 10.0, gap 1.18)：\nKL 的 coupled gradient 在 30% 下仍然比 BCE 学到更好的 neuron ranking，\n特别是在 borderline neurons (importance rank 65-75 percentile) 上。\n这些 borderline neurons 的正确 inclusion/exclusion 对 PPL 有 measurable impact。\n\nGap 缩小（1.18 at 30% vs 16.19 at 50%）因为 30% 是 \"easier\" problem —\nless pruning → less room for mask quality to matter → less KL advantage。\n这与 sparsity sweep 的 finding 一致：KL advantage grows with sparsity。\n\nDownstream at 30%: BCE 表现 intermediate between TEAL and KL on most tasks，\nMMLU 37.0% slightly below TEAL 38.6%（因为 BCE mask 对 knowledge-relevant \nneurons 的 coverage 不如 TEAL's pure magnitude approach at 30%）。\n"
473	  }
474	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8768dcde-66bb-494b-9d35-3005283bd666",
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "3d94d5a0-fae8-4125-b107-97df86918d7e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Four-condition ablation @ 50% sparsity\",\n    \"description\": \"Core comparison: KL-only vs BCE-only vs BCE+comp vs KL+comp at 50% model-level sparsity.\\nKL-only (5 seeds) as headline, BCE+comp (5 seeds) as primary competitor,\\nKL+comp and BCE-only (3 seeds each) as secondary.\\n\",\n    \"results\": {\n      \"kl_only_hard_mask_ppl_mean\": 9.19,\n      \"kl_only_hard_mask_ppl_std\": 0.04,\n      \"kl_only_hard_mask_ppl_seeds\": [\n        9.21,\n        9.25,\n        9.14,\n        9.19,\n        9.15\n      ],\n      \"kl_only_teal_global_ppl_mean\": 11.78,\n      \"kl_only_teal_global_ppl_std\": 0.05,\n      \"kl_only_sparsity\": 0.498,\n      \"bce_only_hard_mask_ppl_mean\": 28.16,\n      \"bce_only_hard_mask_ppl_std\": 0.21,\n      \"bce_only_teal_global_ppl_mean\": 44.05,\n      \"bce_only_sparsity\": 0.496,\n      \"bce_comp_hard_mask_ppl_mean\": 20.8,\n      \"bce_comp_hard_mask_ppl_std\": 0.7,\n      \"bce_comp_teal_global_ppl_mean\": 25.5,\n      \"bce_comp_compensation_params\": 67248128,\n      \"bce_comp_compensation_params_mb\": 256,\n      \"bce_comp_recovery_vs_bce_ppl\": 2.5,\n      \"kl_comp_hard_mask_ppl_mean\": 9.18,\n      \"kl_comp_hard_mask_ppl_std\": 0.04,\n      \"kl_comp_teal_global_ppl_mean\": 11.78,\n      \"kl_comp_recovery_vs_kl_ppl\": 0.01,\n      \"kl_comp_compensation_redundant\": true\n    },\n    \"tables\": [\n      \"Table 1: Main 4-condition PPL comparison @ 50% sparsity\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Headline: KL-only (PPL 9.19) > BCE+comp (PPL 20.8) by 2.26x, 同时省去 67.2M compensation 参数。\\nKL+comp ≈ KL-only 证明 compensation 在 KL 训练下完全冗余。\\nBCE+comp 虽优于 BCE-only (20.8 vs 28.16)，但改善仅 7.4 PPL — compensation 是 BCE 的 patch \\n而非根本解决方案。KL 对 predictor training 的改进是 structural 的（从 mask quality 层面），\\n不是 compensation 能弥补的。\\n\\n\\nKL-only 5-seed consistency (std 0.04) 源于 KL loss 的 output-distribution supervision \\n为 predictor 提供了强且稳定的梯度信号（SNR ~5.8x BCE）。所有 seeds 收敛到相似的 mask pattern\\n因为 KL landscape 有唯一的 well-defined minimum（neuron importance 由 output distribution \\n唯一确定）。\\n\\nBCE-only PPL ~28 是因为 BCE 的 factorized gradient 只能学 per-neuron importance，\\n无法捕获 neuron interaction patterns。F1 vs magnitude oracle = 0.61 看似不错，\\n但 functional quality 差，因为 the wrong 39% neurons 被错误处理。\\n\\nBCE+comp PPL ~20.8 说明 compensation MLP 能部分修复 BCE 的 mask error，\\n但不能替代 mask quality 本身。67.2M 参数（256MB）只换来 ~7 PPL improvement，\\n且 KL-only 无需 compensation 就已 PPL 9.19，说明 correct mask > brute-force compensation。\\n\\nKL+comp ≈ KL-only 因为 KL mask 已经接近 optimal（留下的 neuron set 正是 \\noutput distribution preservation 所需），compensation 无残余 error 可修复。\\n\"\n  },\n  {\n    \"name\": \"STE baseline (KL + Straight-Through Estimator)\",\n    \"description\": \"KL loss + STE instead of Gumbel-sigmoid. Isolates loss function vs relaxation method contribution.\\n3 seeds.\\n\",\n    \"results\": {\n      \"ste_hard_mask_ppl_s42\": 8.18,\n      \"ste_hard_mask_ppl_s123\": 8.25,\n      \"ste_hard_mask_ppl_s456\": 8.2,\n      \"ste_hard_mask_ppl_mean\": 8.21,\n      \"ste_hard_mask_ppl_std\": 0.04,\n      \"ste_sparsity\": 0.47,\n      \"ste_sparsity_note\": \"Lagrangian slightly weaker, converges to 47% vs target 50%\",\n      \"kl_gumbel_ppl_at_same_sparsity\": 9.19,\n      \"ste_vs_gumbel_delta\": -1.01\n    },\n    \"tables\": [\n      \"Table A2: Relaxation method ablation (STE vs Gumbel-sigmoid)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"STE 实验确认 KL advantage 来自 loss function 而非 relaxation method。\\nGumbel-sigmoid 提供 lower-variance gradient estimates → better Lagrangian convergence → \\nsparsity 更准确到达 target。但 mask quality 由 KL loss 的 coupled gradient 决定，\\n与 relaxation 无关。Paper 中作为 \\\"R3 concern: Gumbel explains gain\\\" 的直接反驳。\\n\\n\\nSTE PPL 8.18-8.25 < KL Gumbel PPL 9.19，但 STE sparsity 只达 47% vs Gumbel 的 50%。\\nLower sparsity 意味着 STE 保留了更多 neurons（实际是更宽松的 task），所以 PPL advantage \\n部分来自 lower effective sparsity。核心结论不变：KL loss（无论用 Gumbel 还是 STE 做 relaxation）\\n都远优于 BCE loss (28.16)，证明 KL loss function 是 advantage 的 primary source，\\nGumbel relaxation 只影响 sparsity convergence 效率（不影响 mask quality）。\\nSTE Lagrangian 更弱因为 STE gradient 是 biased estimator，导致 sparsity constraint \\nlearning 较慢。\\n\"\n  },\n  {\n    \"name\": \"Iso-compute BCE vs KL\",\n    \"description\": \"BCE training extended to 2700 steps (2.71x KL FLOPs) to rule out compute advantage.\\n3 seeds (s42/s123/s456).\\n\",\n    \"results\": {\n      \"bce_isocompute_teal_ppl_s42\": 27.97,\n      \"bce_isocompute_teal_ppl_s123\": 28.06,\n      \"bce_isocompute_teal_ppl_s456\": 28.35,\n      \"bce_isocompute_teal_ppl_mean\": 28.13,\n      \"bce_isocompute_teal_ppl_std\": 0.2,\n      \"bce_isocompute_training_steps\": 2700,\n      \"bce_isocompute_flops_ratio_vs_kl\": 2.71,\n      \"kl_1000step_ppl\": 11.78,\n      \"bce_loss_saturation_step\": 500,\n      \"bce_loss_500_to_2700_delta\": 0.006\n    },\n    \"tables\": [\n      \"Table A3: Iso-compute comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"完全排除 \\\"KL wins only because more compute\\\" concern。\\nBCE loss saturation at step 500 意味着 BCE predictor 已到达其 expressiveness limit —\\n即使 compute 无限也无法学到 KL-quality masks。\\nGap 2.39x 在 iso-compute 下与 standard compute 下几乎相同 (2.38x)，\\n证明额外 compute 对 BCE 无帮助。\\n\\n\\nBCE loss 在 ~500 steps 后饱和（final loss 0.638 → 0.632，delta 仅 0.006），\\n额外 2200 steps 几乎无改善。这证明 BCE-KL gap 是 structural mismatch 而非 compute deficit。\\nBCE 的 factorized gradient (dL/ds_j depends only on neuron j) 意味着 learning landscape \\n存在 fundamental limit — 无论多少 compute 都无法让 BCE 学到 neuron interaction patterns。\\n2.71x FLOPs → PPL 28.13 vs KL 11.78 (2.39x gap)，confirmed structural explanation。\\n\"\n  },\n  {\n    \"name\": \"SPON reimplementation on Llama 3.1 8B\",\n    \"description\": \"Learnable bias vectors + KL training for static correction.\\nRecovery rate and interference with dense model.\\n\",\n    \"results\": {\n      \"spon_sparse_ppl\": 8.991,\n      \"kl_pred_ppl_no_spon\": 9.217,\n      \"spon_recovery_pct\": 7.3,\n      \"spon_ppl_improvement\": 0.226,\n      \"dense_with_spon_ppl\": 6.182,\n      \"dense_ppl_degradation\": 0.065,\n      \"mean_bias_norm\": 0.053,\n      \"trainable_params\": 458752,\n      \"trainable_pct_of_model\": 0.0057,\n      \"teal_with_spon_ppl\": 11.79,\n      \"teal_without_spon_ppl\": 12.08,\n      \"teal_spon_recovery_pct\": 4.8\n    },\n    \"tables\": [\n      \"Table A1: SPON analysis — recovery rate and dense degradation\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"SPON recovery 仅 7.3% 直接支撑 Claim 2：static correction 太弱，无法 complement KL。\\n同时，SPON 的 dense degradation (0.065 PPL) 意味着实际 net benefit 更小。\\nConclusion: SPON addresses the wrong error component — KL's residual is dominated by \\nper-input adaptive errors that static bias cannot fix。\\n\\n\\nSPON 的 static bias correction 只能修复 input-independent 的 systematic error。\\nRecovery 7.3% 说明 KL predictor 的 residual error 中只有一小部分是 static bias —\\n大部分 error 是 per-input adaptive 的（取决于 specific token context 下的 neuron importance）。\\nDense PPL degradation 0.065 (6.12 → 6.18) 说明 SPON bias 会轻微干扰 dense forward pass，\\n因为 bias 是为 sparse activation pattern 优化的，在 dense 下是 noise。\\nSPON 对 TEAL baseline 的 recovery (4.8%) 更低，因为 TEAL 的 error 更分散（per-layer \\nmagnitude 误差），static correction 更无效。\\n\"\n  },\n  {\n    \"name\": \"SPON subsumption logit-space analysis\",\n    \"description\": \"Output-space decomposition: linearity test, magnitude ratio, cosine similarity.\\nPer-layer orthogonality analysis. 50 samples × 2048 tokens.\\n\",\n    \"results\": {\n      \"linearity_ratio\": 0.264,\n      \"linearity_ratio_std\": 0.007,\n      \"magnitude_ratio_spon_vs_kl\": 0.158,\n      \"magnitude_ratio_std\": 0.009,\n      \"cosine_similarity_mean\": 0.196,\n      \"cosine_similarity_std\": 0.027,\n      \"kl_predictor_effect_norm\": 482.65,\n      \"spon_correction_norm\": 76.2,\n      \"interaction_norm\": 147.74,\n      \"per_layer_cosine_max\": 0.0,\n      \"conclusion_type\": \"weak_subsumption\"\n    },\n    \"tables\": [\n      \"Table A1: SPON subsumption metrics\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Logit-space decomposition 提供 Claim 2 的 mechanistic explanation：\\nKL 的 coupled gradient 学到的 mask pattern 在 output space 产生 large-magnitude correction (482.65)，\\nSPON 的 static bias 产生 small near-orthogonal correction (76.2)。\\n两者靶向的 error mode 不同（per-input vs static），\\nSPON 的 mode 太弱无法 complement KL。\\n\\n\\nCosine similarity 0.196 (接近 orthogonal，远低于 0.5) 证明 SPON correction 和 KL predictor \\neffect 作用在 logit space 的几乎正交方向。Magnitude ratio 15.8% 说明即使 SPON 和 KL \\n方向一致，SPON 的修正幅度也只有 KL 的 1/6。\\nPer-layer cosine ≤ 0 (所有层) 意味着在每一层 SPON 要么和 KL 正交要么轻微反向。\\nInteraction term 147.74 (30.6% of KL effect) 看似不小，但这是 nonlinear cross-layer \\ninteraction — SPON bias 会改变 subsequent layers 的 input distribution，\\n但这种 interaction 并不 translate to PPL improvement（SPON recovery 仅 7.3%）。\\nConclusion: SPON 和 KL 靶向不同的 error components，且 SPON 的 component 太弱，\\ncomposition 无实际收益。\\n\"\n  },\n  {\n    \"name\": \"Training-free baselines (TEAL, WINA, R-Sparse)\",\n    \"description\": \"TEAL (magnitude + greedy), WINA (weight-informed), R-Sparse (rank-aware) at 30%/50%/70%.\\n\",\n    \"results\": {\n      \"teal_global_ppl_30\": 10.97,\n      \"teal_global_ppl_50\": 23.31,\n      \"teal_global_ppl_70\": 100.11,\n      \"wina_global_ppl_30\": 11.45,\n      \"wina_global_ppl_50\": 27.93,\n      \"wina_global_ppl_70\": 137.24,\n      \"rsparse_global_ppl_50\": 151.2,\n      \"dense_ppl\": 6.12,\n      \"teal_greedy_allocation_ppl_50\": 33.47\n    },\n    \"tables\": [\n      \"Table 1: Training-free baselines row in main comparison table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"三层 hierarchy 成立：training-free (TEAL 10.97-100.11) < static-learned (SPON) < \\ncontextual-learned (KL 8.82-11.78)。\\nTEAL 作为 strongest training-free baseline 仍比 KL 30% 差 2.15 PPL (10.97 vs 8.82)。\\nAt 50%, gap expands to 11.53 PPL (23.31 vs 11.78)。\\nNon-linear gap expansion 说明 learned contextual prediction 在 high sparsity 下 advantage 更大。\\n\\n\\nTraining-free methods 的 PPL 随 sparsity 急剧增长（TEAL 30%→50%→70%: 10.97→23.31→100.11），\\n因为 magnitude-based pruning 在 high sparsity 下 increasingly 删除 functionally important neurons。\\nTEAL > WINA > R-Sparse 因为 TEAL 的 global allocation 比 WINA 的 weight-informed scoring \\n更有效地分配 per-layer sparsity budget。R-Sparse 的 rank-aware scoring 在 SwiGLU architecture \\n上表现最差，因为 SwiGLU 的 gating mechanism 使得 rank-based importance 不可靠。\\nTEAL greedy allocation (33.47) 远差于 global (23.31)，说明 allocation strategy \\n对 training-free methods 同样重要。\\n\"\n  },\n  {\n    \"name\": \"Full benchmark evaluation + Pareto frontier\",\n    \"description\": \"WikiText-2 PPL + 4 downstream tasks (ARC-c, WinoGrande, MMLU, GSM8K) across all conditions.\\nWall-clock profiling. Efficiency-accuracy Pareto frontier.\\n\",\n    \"results\": {\n      \"dense_ppl\": 6.12,\n      \"dense_arc_c\": 0.583,\n      \"dense_wg\": 0.781,\n      \"dense_mmlu\": 0.653,\n      \"dense_gsm8k\": 0.488,\n      \"kl30u_ppl_mean\": 8.82,\n      \"kl30u_ppl_std\": 0.01,\n      \"kl30u_arc_c_mean\": 0.443,\n      \"kl30u_arc_c_std\": 0.032,\n      \"kl30u_wg_mean\": 0.692,\n      \"kl30u_wg_std\": 0.006,\n      \"kl30u_mmlu_mean\": 0.385,\n      \"kl30u_mmlu_std\": 0.018,\n      \"kl30u_gsm8k_mean\": 0.072,\n      \"kl30u_gsm8k_std\": 0.002,\n      \"kl50g_ppl_mean\": 11.78,\n      \"kl50g_arc_c_mean\": 0.343,\n      \"kl50g_wg_mean\": 0.631,\n      \"kl50g_mmlu_mean\": 0.281,\n      \"kl50g_gsm8k_mean\": 0.021,\n      \"teal30_ppl\": 10.97,\n      \"teal30_arc_c\": 0.423,\n      \"teal30_wg\": 0.661,\n      \"teal30_mmlu\": 0.386,\n      \"teal30_gsm8k\": 0.079,\n      \"teal50_ppl\": 23.31,\n      \"teal50_arc_c\": 0.284,\n      \"teal50_wg\": 0.53,\n      \"teal50_mmlu\": 0.283,\n      \"teal50_gsm8k\": 0.011,\n      \"bce_iso_teal_ppl_mean\": 28.13,\n      \"bce_iso_arc_c_mean\": 0.265,\n      \"bce_iso_wg_mean\": 0.518,\n      \"bce_iso_mmlu_mean\": 0.261,\n      \"bce_iso_gsm8k_mean\": 0.021,\n      \"dense_latency_ms\": 119.1,\n      \"kl30_latency_ms\": 126.6,\n      \"kl50_latency_ms\": 126.8,\n      \"predictor_overhead_ms\": 3.17,\n      \"predictor_overhead_pct\": 2.7,\n      \"theoretical_flops_speedup_30pct\": 1.36,\n      \"theoretical_flops_speedup_50pct\": 2.45,\n      \"actual_wallclock_speedup_30pct\": 0.94,\n      \"no_sparse_kernel_note\": \"No wall-clock speedup without custom sparse GEMV kernels\"\n    },\n    \"tables\": [\n      \"Table 2: Downstream benchmarks across all conditions\",\n      \"Table 6: Latency profiling and efficiency analysis\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pareto frontier 叙事在 median 下需 calibration：\\n- PPL: KL clearly dominates (−19.6% at 30%)\\n- Downstream: mixed. KL 30% uniform beats TEAL on WG (+3.1pp) and ARC-c (+2.0pp)，\\n  但 MMLU 平局且 GSM8K 略输 (−0.7pp)\\n- Honest framing: \\\"KL dominates PPL frontier and provides comparable-to-better downstream,\\n  with advantage concentrated on WG and ARC-c; GSM8K within noise\\\"\\n- Latency limitation: 需 custom sparse kernels 才能实现 wall-clock speedup。\\n  Report theoretical FLOPs + predictor overhead，acknowledge practical speedup pending。\\n\\n\\nKL 30% uniform 是 recommended operating point 的 median-tier 表现：\\n- PPL: 8.82 vs TEAL 10.97 (−19.6%)，KL clearly wins\\n- MMLU: 38.5% vs TEAL 38.6% — essentially tied. Median 下 MMLU advantage 被 seed variance (std 1.8%) 淹没\\n- WinoGrande: 69.2% vs 66.1% — KL wins by +3.1pp，超过 noise margin\\n- ARC-c: 44.3% vs 42.3% — KL slightly better (+2.0pp) 但 seed std 3.2% 使得 significance 不确定\\n- GSM8K: 7.2% vs 7.9% — TEAL slightly better by 0.7pp，within noise\\n\\nDownstream advantage 不如 PPL advantage 一致，因为 discriminative tasks 对 specific \\nneuron subsets 敏感（不同 seed 的 mask 在 critical task-relevant neurons 上有差异）。\\nPPL 是 average over all tokens，对 mask quality 更敏感也更稳定。\\n\\nLatency: 无 wall-clock speedup 因为 standard PyTorch 不支持 structured sparse GEMV。\\nPredictor overhead 2.7% (3.17ms/119.1ms) 在 sparse kernel 可用时可被 sparsity savings \\n(theoretical 1.36x at 30%) 覆盖。Paper 报告 theoretical FLOPs savings + overhead。\\n\"\n  },\n  {\n    \"name\": \"Sparsity regime analysis (30%/40%/50%/70%)\",\n    \"description\": \"KL-only at 30%/50%/70% + intermediate points (40%). Test scaling trend.\\nCombined with dense_sparsity_sweep_6pt for 6-point curve.\\n\",\n    \"results\": {\n      \"kl_30_uniform_ppl\": 8.82,\n      \"kl_30_uniform_mmlu\": 0.406,\n      \"kl_40_global_ppl\": 10.12,\n      \"kl_40_global_mmlu\": 0.381,\n      \"kl_50_global_ppl\": 11.78,\n      \"kl_50_global_mmlu\": 0.281,\n      \"kl_50_uniform_ppl\": 11.94,\n      \"kl_50_uniform_mmlu\": 0.278,\n      \"kl_70_global_ppl\": 17.91,\n      \"kl_70_downstream_collapsed\": true,\n      \"teal_30_ppl\": 10.97,\n      \"teal_50_ppl\": 23.31,\n      \"teal_70_ppl\": 100.11,\n      \"kl_teal_gap_30\": 2.15,\n      \"kl_teal_gap_50\": 11.53,\n      \"kl_teal_gap_70\": 82.2,\n      \"regime_budget_surplus_boundary\": 0.3,\n      \"regime_capacity_cliff_boundary\": 0.5,\n      \"ppl_nonmonotonicity\": \"40% PPL (8.36) < 30% PPL (8.82) under uniform allocation (non-monotonic)\",\n      \"downstream_strictly_monotonic\": true\n    },\n    \"tables\": [\n      \"Table 4: Three-regime sparsity analysis\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Regime analysis 的 median narrative：三个 regime 存在且 boundaries 明确，\\nnon-monotonic allocation preference 是 genuine finding。\\nPractical recommendation: 30% sparsity + uniform allocation for deployment。\\nKL gap over TEAL grows nonlinearly (2.15 → 11.53 → 82.20)，\\n说明 learned contextual prediction 的 value 随 sparsity 急剧增加。\\n\\n\\n三个 regime 的 mechanistic explanation：\\n\\n(1) Budget-surplus (≤30%): 每层都有充足的 neuron budget，uniform allocation 消除 \\nlayer starvation（σ_MMLU 从 9.5pp 降到 1.3pp）。KL mask quality 优势最大化，\\n因为 abundant budget 允许 KL 选择 truly important neurons 而非被迫 compromise。\\n\\n(2) Budget-constrained (~40%): uniform 反而不如 global（MMLU 30.7% vs 38.1%）。\\n当 budget 紧张时，learned per-layer allocation (global topk) 比 blind uniformity \\n更能将有限 budget 分配给 critical layers。这是 non-monotonic allocation preference \\n的机制原因。\\n\\n(3) Capacity-cliff (≥50%): 模型 capacity 本身不足，无论如何分配都 collapse。\\nMMLU ≈ 28% ≈ random（4-choice）。KL 仍能维持 PPL 11.78，因为 PPL 是 continuous metric \\n更 robust to partial capacity loss，而 MMLU 需要 discrete reasoning chain 完整。\\n\\nPPL non-monotonicity (40% < 30% under uniform): 因为 40% 用了 global allocation \\n(10.12) 而 30% 用了 uniform (8.82)，但如果比较 30% global (8.98) vs 40% global (10.12)，\\nPPL 仍然单调递增。Non-monotonicity 只在 cross-allocation comparison 下出现。\\n\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 cross-architecture validation\",\n    \"description\": \"KL-only at 30%/50%/70% on Mistral-7B-v0.3 (GQA + sliding window attention).\\nValidates that KL advantage transfers across architectures.\\n\",\n    \"results\": {\n      \"mistral_dense_ppl\": 5.52,\n      \"mistral_dense_arc_c\": 0.602,\n      \"mistral_dense_wg\": 0.787,\n      \"mistral_dense_mmlu\": 0.624,\n      \"mistral_dense_gsm8k\": 0.365,\n      \"mistral_kl30_teal_ppl\": 6.77,\n      \"mistral_kl30_ppl_ratio\": 1.23,\n      \"mistral_kl50_teal_ppl\": 8.65,\n      \"mistral_kl50_arc_c\": 0.318,\n      \"mistral_kl50_wg\": 0.629,\n      \"mistral_kl50_mmlu\": 0.23,\n      \"mistral_kl50_gsm8k\": 0.021,\n      \"mistral_kl50_mmlu_retention\": 0.368,\n      \"mistral_kl70_teal_ppl\": 13.33,\n      \"mistral_teal30_ppl\": 8.38,\n      \"mistral_teal50_ppl\": 18.31,\n      \"mistral_teal70_ppl\": 61.72,\n      \"mistral_kl_teal_ratio_30\": 1.24,\n      \"mistral_kl_teal_ratio_50\": 2.12,\n      \"mistral_kl_teal_ratio_70\": 4.63,\n      \"llama_kl_teal_ratio_30\": 1.24,\n      \"llama_kl_teal_ratio_50\": 1.98,\n      \"llama_kl_teal_ratio_70\": 5.59,\n      \"cross_arch_ratio_consistent\": true\n    },\n    \"tables\": [\n      \"Table 5: Cross-architecture generalization (Mistral-7B)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-architecture validation 成功：KL advantage ratio 在 Mistral 上 preserved。\\nGSM8K 的 catastrophic drop (36.5% dense → 2.1% KL 50%) 在 Mistral 上更严重，\\n可能因为 Mistral 的 math capability 本身较弱 (36.5% vs Llama's 48.8%)。\\nLimitation: 仍是 7-8B scale，14B (Qwen) 已知有 MMLU disconnect。\\n\\n\\nKL advantage ratio (KL_teal / TEAL) 在 Mistral 上与 Llama 高度一致：\\n30%: 1.24 vs 1.24, 50%: 2.12 vs 1.98, 70%: 4.63 vs 5.59。\\n这说明 KL distillation 的 advantage 来自 SwiGLU architecture 的通用特性\\n（coupled gradient captures neuron interaction patterns），而非 specific model weights。\\n\\nMistral 的 GQA + sliding window attention 不影响 FFN sparsity prediction，\\n因为 predictor 只在 FFN block 内操作（input = hidden state after attention）。\\nAttention mechanism 差异只影响 hidden state distribution，不改变 KL vs BCE 的 \\nfundamental learning dynamics。\\n\\nDownstream 在 50%: MMLU 23.0% 同样 collapse 到 near-random，\\n与 Llama 的 28.1% 一致（both ≈ random 25%）。\\n这 cross-validates capacity cliff 存在于 both architectures。\\n\"\n  },\n  {\n    \"name\": \"LongBench English subset evaluation\",\n    \"description\": \"LongBench English subset (4K-32K tokens). KL-only, BCE, TEAL, SPON conditions.\\nPer-task-type breakdown. Tests predictor generalization beyond 2048 training length.\\n\",\n    \"results\": {\n      \"dense_narrativeqa\": 18.2,\n      \"dense_qasper\": 27.5,\n      \"dense_hotpotqa\": 25.8,\n      \"dense_gov_report\": 30.0,\n      \"dense_multi_news\": 25.1,\n      \"dense_triviaqa\": 82.0,\n      \"kl30u_narrativeqa\": 12.5,\n      \"kl30u_qasper\": 19.8,\n      \"kl30u_hotpotqa\": 15.2,\n      \"kl30u_gov_report\": 22.1,\n      \"kl30u_multi_news\": 17.5,\n      \"kl30u_triviaqa\": 56.8,\n      \"kl30u_avg_retention\": 0.64,\n      \"kl50g_narrativeqa\": 6.2,\n      \"kl50g_qasper\": 10.8,\n      \"kl50g_hotpotqa\": 7.5,\n      \"kl50g_gov_report\": 14.2,\n      \"kl50g_multi_news\": 9.1,\n      \"kl50g_triviaqa\": 32.5,\n      \"kl50g_avg_retention\": 0.35,\n      \"teal30_narrativeqa\": 10.8,\n      \"teal30_qasper\": 17.2,\n      \"teal30_hotpotqa\": 13.0,\n      \"teal30_gov_report\": 19.5,\n      \"teal30_multi_news\": 14.8,\n      \"teal30_triviaqa\": 50.2,\n      \"teal30_avg_retention\": 0.56,\n      \"kl30u_retention_4k\": 0.72,\n      \"kl30u_retention_8k\": 0.63,\n      \"kl30u_retention_16k\": 0.52,\n      \"kl30u_retention_32k\": 0.41,\n      \"length_degradation_note\": \"Predictor trained on 2048 tokens; generalization degrades with context length\"\n    },\n    \"tables\": [\n      \"Table A5: LongBench results (English subset)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LongBench 在 median tier 下提供 mixed evidence：\\n- KL > TEAL on all task types（advantage preserved）\\n- 但 absolute retention 在 long context 下显著下降（72% at 4K → 41% at 32K for KL 30%）\\n- 这 motivates future work on long-context-aware predictor training\\n- Paper 中作为 partial success + honest limitation 报告。\\n- Infrastructure issues 可能导致只报告 subset of tasks。\\n\\n\\nPredictor 在 2048 token 上训练，对 longer context 的 generalization 有 length-dependent degradation。\\n原因：neuron importance distribution 随 context length 变化——longer context 中 attention pattern\\n更 distributed，导致 hidden state 的 distributional shift。Predictor 学到的 importance pattern \\n基于 short-context hidden states，在 long-context 下 partially misaligned。\\n\\nKL 30% 平均 retention 64% 优于 TEAL 30% 的 56%，说明 KL mask quality advantage 在 \\nlong-context 下 preserved（虽然 absolute performance 下降）。\\n\\nPer-task-type pattern: extraction tasks (TriviaQA, HotpotQA) 受 sparsity 影响较小，\\ngeneration tasks (NarrativeQA, MultiNews) 影响较大——generation 需要更完整的 capacity \\n来 maintain fluency and coherence over long outputs。\\n\\nSummarization (GovReport) intermediate: 需要 comprehension (robust) + generation (fragile)。\\n\\nInfrastructure 风险：基于 registry 中多次 LongBench 失败 (v1-v5)，median 预期 \\n只有部分 tasks 产出可靠结果，可能需要 partial reporting。\\n\"\n  },\n  {\n    \"name\": \"MT-Bench multi-turn evaluation\",\n    \"description\": \"80 multi-turn questions, 8 categories, GPT-4o judge.\\nTests instruction-following quality under sparsity.\\n\",\n    \"results\": {\n      \"dense_mtbench_avg\": 6.35,\n      \"dense_writing\": 7.2,\n      \"dense_roleplay\": 7.0,\n      \"dense_reasoning\": 5.8,\n      \"dense_math\": 4.5,\n      \"dense_coding\": 5.2,\n      \"dense_extraction\": 7.5,\n      \"dense_stem\": 6.8,\n      \"dense_humanities\": 6.8,\n      \"kl30u_mtbench_avg\": 5.15,\n      \"kl30u_writing\": 6.0,\n      \"kl30u_roleplay\": 5.8,\n      \"kl30u_reasoning\": 4.2,\n      \"kl30u_math\": 2.8,\n      \"kl30u_coding\": 3.5,\n      \"kl30u_extraction\": 6.5,\n      \"kl30u_stem\": 5.5,\n      \"kl30u_humanities\": 5.9,\n      \"kl30u_retention_avg\": 0.81,\n      \"kl50g_mtbench_avg\": 3.4,\n      \"kl50g_writing\": 4.2,\n      \"kl50g_roleplay\": 3.8,\n      \"kl50g_reasoning\": 2.5,\n      \"kl50g_math\": 1.5,\n      \"kl50g_coding\": 2.0,\n      \"kl50g_extraction\": 5.0,\n      \"kl50g_stem\": 3.5,\n      \"kl50g_humanities\": 4.5,\n      \"kl50g_retention_avg\": 0.54,\n      \"teal30_mtbench_avg\": 4.6,\n      \"teal30_retention_avg\": 0.72\n    },\n    \"tables\": [\n      \"Table A6: MT-Bench scores by category\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MT-Bench 在 median tier 下是 P2 priority，可能不在 main paper 而在 appendix。\\n如果包含，key message：KL 30% retains 81% of dense MT-Bench quality，\\n但 Math/Coding categories 下降最大（需要 precise reasoning 的 task 对 sparsity 最敏感）。\\n如时间不够或 judge API 有 budget 限制，可 defer 到 camera-ready。\\n\\n\\nMT-Bench 的 multi-turn format 对 sparsity 特别敏感：\\n\\n(1) Turn 2 依赖 turn 1 的 generation quality — sparsity 引起的 error 会 compound。\\nSparse mask 在 turn 1 产生的 slight distributional shift 在 turn 2 被 amplified，\\n因为 turn 2 的 prompt 包含 turn 1 的（degraded）output。\\n\\n(2) Category-dependent sensitivity：Math/Coding 需要 precise symbolic reasoning，\\n对 individual neuron importance 最敏感。Writing/Roleplay 更依赖 learned patterns \\n和 fluency，对 mask 的 approximate correctness 更 tolerant。\\nExtraction tasks 主要需要 copying relevant content，对 model capacity 要求最低。\\n\\n(3) KL 30% retention 81% vs TEAL 30% 72%：KL advantage (+9pp retention) 在 \\nmulti-turn 下比 single-task benchmark 更明显，因为 better mask quality 在 \\ncompound error 下的 advantage 被放大。\\n\\n(4) GPT-4o judge 倾向于给 fluent but wrong answers 较高分数，\\n这可能 slightly overestimate sparse model quality（尤其 Math/Coding categories \\nwhere correctness matters more than fluency）。\\n\"\n  },\n  {\n    \"name\": \"RULER synthetic long-context tasks\",\n    \"description\": \"RULER at 4K and 16K, 3 representative task types (needle-in-haystack, multi-key,\\nmulti-value). Fine-grained capability diagnostics.\\n\",\n    \"results\": {\n      \"dense_4k_needle\": 0.95,\n      \"dense_4k_multikey\": 0.82,\n      \"dense_4k_multivalue\": 0.78,\n      \"dense_16k_needle\": 0.88,\n      \"dense_16k_multikey\": 0.65,\n      \"dense_16k_multivalue\": 0.58,\n      \"kl30u_4k_needle\": 0.82,\n      \"kl30u_4k_multikey\": 0.6,\n      \"kl30u_4k_multivalue\": 0.55,\n      \"kl30u_16k_needle\": 0.58,\n      \"kl30u_16k_multikey\": 0.32,\n      \"kl30u_16k_multivalue\": 0.28,\n      \"kl50g_4k_needle\": 0.55,\n      \"kl50g_4k_multikey\": 0.3,\n      \"kl50g_4k_multivalue\": 0.22,\n      \"kl50g_16k_needle\": 0.25,\n      \"kl50g_16k_multikey\": 0.12,\n      \"kl50g_16k_multivalue\": 0.1,\n      \"teal30_4k_needle\": 0.75,\n      \"teal30_4k_multikey\": 0.52,\n      \"teal30_4k_multivalue\": 0.48\n    },\n    \"tables\": [\n      \"Table A7: RULER synthetic evaluation\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"RULER 作为 P2 experiment，主要作为 LongBench 的 fine-grained diagnostic complement。\\nKey finding: sparsity 对 multi-hop retrieval (multikey/multivalue) 的影响远大于 \\nsingle-fact retrieval (needle)，providing mechanistic insight into which \\nmodel capabilities are most fragile under sparsity。\\n如 LongBench 失败，RULER 可作为 backup long-context evidence。\\n\\n\\nRULER tasks 的 synthetic nature 使得 sparsity impact 更清晰：\\n\\nNeedle-in-haystack: 最 robust（只需找到一个 specific fact），但仍因 sparsity \\n导致 attention 和 FFN 的 interaction 退化。4K→16K 下降因为 more distractor tokens。\\n\\nMulti-key/Multi-value: 需要同时 track multiple pieces of information，\\n对 model capacity 要求更高。Sparsity 削减的 neurons 可能包含 \\\"memory slots\\\"\\n用于 track different keys/values，导致 disproportionate degradation。\\n\\nKL 30% vs TEAL 30% on needle@4K: 82% vs 75%。KL's better mask preserves \\nthe critical neurons for attention-FFN interaction that retrieval depends on。\\n\\n16K 下所有 sparse conditions 显著退化：predictor 在 2048 上训练，\\n16K 的 hidden state distribution 偏移更大，compounding with retrieval task difficulty。\\n\"\n  },\n  {\n    \"name\": \"C1 causal ablation: BCE trained on KL-derived oracle masks\",\n    \"description\": \"The headline experiment for Claim 1. BCE predictor trained to match KL-derived\\nbinary oracle masks (not magnitude oracles). Evaluated at 50% TEAL uniform protocol.\\nTests whether target quality or gradient coupling drives KL advantage.\\nIn median tier: >95% but not 100% of KL advantage explained by targets.\\n\",\n    \"results\": {\n      \"c1_s42_ppl\": 12.11,\n      \"c1_s42_kl_ref_ppl\": 11.96,\n      \"c1_s42_delta\": 0.15,\n      \"c1_s42_arc_c\": 0.305,\n      \"c1_s42_wg\": 0.61,\n      \"c1_s42_mmlu\": 0.275,\n      \"c1_s42_gsm8k\": 0.017,\n      \"c1_s123_ppl\": 12.17,\n      \"c1_s123_kl_ref_ppl\": 11.89,\n      \"c1_s123_delta\": 0.28,\n      \"c1_s123_arc_c\": 0.35,\n      \"c1_s123_wg\": 0.605,\n      \"c1_s123_mmlu\": 0.27,\n      \"c1_s123_gsm8k\": 0.019,\n      \"c1_mean_ppl_delta\": 0.22,\n      \"c1_gradient_coupling_contribution_pct\": 1.4,\n      \"c1_target_quality_explains_pct\": 98.6,\n      \"c1_s42_max_downstream_delta_pp\": 2.1,\n      \"c1_s42_max_delta_task\": \"ARC-c\",\n      \"c1_s123_max_downstream_delta_pp\": 2.9,\n      \"c1_s123_max_delta_task\": \"ARC-c\",\n      \"kl_uniform_50_ppl_s42\": 11.96,\n      \"bce_magnitude_50_ppl\": 27.97,\n      \"mask_divergence_kl_vs_magnitude\": 0.53,\n      \"oracle_agreement_c1_predictor\": 0.975\n    },\n    \"tables\": [\n      \"Table 3: C1 Causal Ablation — BCE+KL-targets vs KL\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"C1 在 median tier 下需要 nuanced framing：\\n\\nHeadline: \\\"Target quality accounts for >95% of KL advantage; gradient coupling \\ncontributes ~1-3% on PPL and up to 2.9pp on reasoning tasks.\\\"\\n\\nClaim 1 revision: 从 \\\"sole driver\\\" 改为 \\\"dominant driver (>95%)\\\"。\\n保留 \\\"mask pattern discovery\\\" 叙事：53% divergence from magnitude oracles 仍是 \\nheadline finding。但 gradient coupling 的 marginal contribution 需要 acknowledged。\\n\\nPer-task analysis section (§4.4.1): 解释 ARC-c 对 gradient coupling 更敏感，\\n原因是 multi-step reasoning 放大了 neuron combination quality 的差异。\\n\\nPractical implication 不变：BCE+KL-targets 仍然需要先训练 KL predictor 来 generate \\noracle masks，所以 deployment 时直接用 KL predictor 更简单。C1 的价值是 \\nscientific understanding（why KL works），不是 practical pipeline 替代。\\n\\n\\nMedian tier C1: PPL delta 0.15-0.28，说明 gradient coupling 有 marginal non-zero \\ncontribution 但不改变 practical conclusion。\\n\\n为什么 delta > 0（gradient coupling ≠ 0）：\\nKL 的 coupled gradient (dL_KL/ds_j depends on ALL active neurons via dlogits/dh · dh/dm) \\n让 predictor 在 training 过程中探索 joint neuron interaction patterns。BCE 即使给了 \\nKL-derived oracle targets，仍然用 factorized gradient (dL_BCE/ds_j depends only on j) \\n来学习。Factorized gradient 无法完全 reproduce KL predictor 学到的 nuanced scoring —\\n某些 neuron pairs 的 joint importance 只在 coupled gradient 下可见。\\n\\n为什么 delta 很小（<0.3 PPL）：\\nOracle masks 提供了 explicit supervision（\\\"keep these specific neurons\\\"），\\n大幅减少了 learning complexity。BCE with explicit targets 不需要 discover importance —\\n只需 classify known-important vs known-unimportant。98.6% 的 advantage 来自 knowing \\nWHICH neurons to keep，gradient coupling 只在 edge cases（importance scores 接近 threshold \\n的 neurons）有 marginal effect。\\n\\n为什么 ARC-c delta 最大（2.1-2.9pp）：\\nARC-c 的 multi-step reasoning 依赖 specific neuron combinations（\\\"reasoning chains\\\" \\nmapped to neuron subsets）。Gradient coupling 使 KL predictor 学到了这些 combinatorial \\nimportance patterns，BCE predictor 即使有 oracle targets 也只学到 individual importance。\\n在 reasoning tasks 上，neuron combination 的质量差异被放大为 accuracy gap。\\n\\nWinoGrande delta 较小（1.4pp）因为 commonsense 更依赖 distributed representations \\n而非 specific neuron chains。MMLU/GSM8K 在 50% sparsity 下已 collapse 到 near-random，\\ndelta 被 floor effect 掩盖。\\n\"\n  },\n  {\n    \"name\": \"Dense sparsity sweep — 6-point regime curve\",\n    \"description\": \"KL predictors evaluated at 25%/30%/35%/40%/45%/50% sparsity.\\n6-point PPL curve for regime boundary identification.\\n\",\n    \"results\": {\n      \"kl_25_ppl\": 8.2,\n      \"kl_30_ppl\": 8.82,\n      \"kl_35_ppl\": 9.4,\n      \"kl_40_ppl\": 10.12,\n      \"kl_45_ppl\": 10.78,\n      \"kl_50_ppl\": 11.8,\n      \"delta_25_30\": 0.62,\n      \"delta_30_35\": 0.58,\n      \"delta_35_40\": 0.72,\n      \"delta_40_45\": 0.66,\n      \"delta_45_50\": 1.02,\n      \"monotonic\": true,\n      \"monotonicity_violations\": 0,\n      \"noise_band_35pct\": 0.2,\n      \"noise_band_note\": \"35% 在 different seeds 下可能波动 ±0.2 PPL (9.20-9.60)\",\n      \"budget_surplus_regime\": \"≤30%\",\n      \"transition_regime\": \"35%-40%\",\n      \"capacity_cliff_onset\": \"45%-50%\",\n      \"acceleration_45_50\": \"delta jumps from 0.66 to 1.02, signaling cliff onset\"\n    },\n    \"tables\": [\n      \"Table 4: 6-point sparsity regime data\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 median 下 Claim 3 需 calibrate：\\n- \\\"Phase transition\\\" 改为 \\\"approximate phase transition\\\"\\n- 35% point 的 noise (±0.2 PPL) 意味着 exact boundary 有 uncertainty\\n- 但 overall trend 成立：PPL increase accelerates from ~0.6/5pp to ~1.0/5pp\\n- 与 downstream data 交叉验证：downstream 是 strictly monotonic degradation，\\n  进一步支持 regime 叙事（PPL 非线性 + downstream 单调 = capacity cliff）\\n- Practical deployment guideline 不变：30% 是 sweet spot，40% 需 learned allocation\\n\\n\\n6-point curve 在 median tier 下基本单调，但 increments 不 uniform：\\n\\n25%→30% (+0.62): 线性区域。每 5pp sparsity 增加 ~0.6 PPL。\\n足够的 neuron budget 使 KL mask quality 能完全 absorb 额外 pruning。\\n\\n30%→35% (+0.58): 仍在线性区。但这个 point 有 ±0.2 noise（single seed），\\n因为 35% 正处在 budget-surplus → transition 的边界。\\n不同 seeds 的 per-layer allocation 在此 sparsity 下 divergence 开始增加。\\n\\n35%→40% (+0.72): increment 开始扩大。Transition regime 开始——\\n某些 layers 的 neuron budget 变得 tight，per-layer importance 的 tail 被截断。\\n\\n40%→45% (+0.66): 看似 increment 缩小，但因为 40% 用了 global allocation \\n而 45% 也是 global，实际 allocation efficiency 在 compensate capacity loss。\\n\\n45%→50% (+1.02): 最大 increment。Capacity cliff 开始——critical neuron sets \\n被 pruned 的概率急剧上升。PPL 对 pruning 的 sensitivity 非线性增加，\\n因为 remaining neurons 的 marginal importance 更高（已经 prune 了 all \\\"easy\\\" neurons）。\\n\\n总体 curve shape: 接近 piecewise linear with inflection at ~40%，\\n然后 super-linear growth to 50%。不是 smooth quadratic，\\n而是 approximate phase transition — 在 median 下 inflection 不够 sharp \\nto call it \\\"phase transition\\\"，改为 \\\"approximate regime boundary\\\"。\\n\"\n  },\n  {\n    \"name\": \"BCE 30% forced TEAL top-k at recommended operating point\",\n    \"description\": \"BCE predictor evaluated at 30% sparsity via forced TEAL top-k allocation.\\nFills Table 2 gap for BCE at recommended operating point.\\n\",\n    \"results\": {\n      \"bce_30_forced_topk_ppl\": 10.0,\n      \"teal_30_baseline_ppl\": 10.97,\n      \"kl_30_uniform_ppl\": 8.82,\n      \"bce_30_vs_teal_30_delta\": -0.97,\n      \"bce_30_vs_kl_30_delta\": 1.18,\n      \"bce_30_arc_c\": 0.41,\n      \"bce_30_wg\": 0.652,\n      \"bce_30_mmlu\": 0.37,\n      \"bce_30_gsm8k\": 0.072,\n      \"dense_ppl\": 6.12,\n      \"bce_30_ppl_ratio_vs_dense\": 1.63,\n      \"kl_30_ppl_ratio_vs_dense\": 1.44\n    },\n    \"tables\": [\n      \"Table 2: BCE 30% row completing the comparison table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"BCE 30% 在 median 下 gap 从 50% 的 16.19 缩小到 30% 的 1.18，\\n需要 honest reporting：\\n\\n- KL 仍优（8.82 vs 10.0），但 margin 更小\\n- Pareto narrative 需调整：强调 KL 在 ALL operating points 上 Pareto-dominate BCE，\\n  but gap 是 sparsity-dependent\\n- BCE 30% 优于 TEAL 30%（10.0 vs 10.97），说明 learned scoring (even factorized) \\n  比 pure magnitude 好\\n- Three-tier hierarchy 仍然成立：magnitude (TEAL 10.97) < learned-factorized (BCE 10.0) < \\n  learned-coupled (KL 8.82)\\n- 这个 three-tier 结果 strengthens \\\"gradient coupling matters\\\" narrative \\n  即使 C1 shows target quality is dominant\\n\\nMedian tier BCE 30% PPL = 10.0（好于 TEAL 10.97 但差于 KL 8.82）：\\n\\nBCE predictor 学到的 scoring 在 30% 下比 50% 更有效，因为：\\n(1) 30% 只需区分 \\\"top 70% important\\\" vs \\\"bottom 30% unimportant\\\"，\\n这个 binary classification 相对容易，即使 factorized gradient 也能部分学到\\n(2) TEAL forced top-k 在 30% 下给 BCE 一个 reasonable allocation baseline，\\nBCE 只需 refine magnitude-based scoring 的 ranking，不需要 fully discover importance\\n(3) 30% 的 margin of error 更大——即使 rank 错误一些 neurons，\\n70% kept neurons 足以覆盖 most important ones\\n\\n为什么 KL 仍然更好 (8.82 vs 10.0, gap 1.18)：\\nKL 的 coupled gradient 在 30% 下仍然比 BCE 学到更好的 neuron ranking，\\n特别是在 borderline neurons (importance rank 65-75 percentile) 上。\\n这些 borderline neurons 的正确 inclusion/exclusion 对 PPL 有 measurable impact。\\n\\nGap 缩小（1.18 at 30% vs 16.19 at 50%）因为 30% 是 \\\"easier\\\" problem —\\nless pruning → less room for mask quality to matter → less KL advantage。\\n这与 sparsity sweep 的 finding 一致：KL advantage grows with sparsity。\\n\\nDownstream at 30%: BCE 表现 intermediate between TEAL and KL on most tasks，\\nMMLU 37.0% slightly below TEAL 38.6%（因为 BCE mask 对 knowledge-relevant \\nneurons 的 coverage 不如 TEAL's pure magnitude approach at 30%）。\\n\"\n  }\n]",
      "numLines": 474,
      "startLine": 1,
      "totalLines": 474
    }
  },
  "sourceToolAssistantUUID": "8768dcde-66bb-494b-9d35-3005283bd666",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "3d94d5a0-fae8-4125-b107-97df86918d7e",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for sparse SwiGLU distillation",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Assistant

_source line 16 · 2026-05-18T18:15:40.390Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me compose a complete LaTeX paper. I need to:

1. Create a well-structured paper with Abstract, Introduction, Method, Experiments, and Conclusion
2. Include tables for all experiments from experiment_data.json
3. Follow the narrative guidance (median tier calibration)
4. Use honest framing (>95% not 100%, approximate phase transition, etc.)

Let me organize the paper structure:

- Abstract
- Introduction (5-paragraph structure per writing norms)
- Related Work


- Method (KL distillation framework, predictor architecture, training)
- Experiments with the main ablation comparison, downstream benchmarks, causal ablation, sparsity regime analysis, cross-architecture results, and latency measurements
- Analysis and Discussion
- Conclusion
- Appendix with additional benchmark tables

Now I'll write the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d94d5a0-fae8-4125-b107-97df86918d7e",
  "isSidechain": false,
  "requestId": "req_011CbAVQgDrLL62sj2cgTknD",
  "type": "assistant",
  "uuid": "bf60e396-5e63-4bea-b56e-d434deeed807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ2yN5JcrKJBLgyNJETwrV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3603,
      "cache_creation_input_tokens": 16337,
      "cache_read_input_tokens": 25475,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3603,
          "output_tokens": 529,
          "cache_read_input_tokens": 25475,
          "cache_creation_input_tokens": 16337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16337
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

_source line 17 · 2026-05-18T18:15:40.406Z_

Now I have both files. Let me compose the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf60e396-5e63-4bea-b56e-d434deeed807",
  "isSidechain": false,
  "requestId": "req_011CbAVQgDrLL62sj2cgTknD",
  "type": "assistant",
  "uuid": "291d504f-4aa9-42b1-90a1-8ff25be852fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ2yN5JcrKJBLgyNJETwrV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3603,
      "cache_creation_input_tokens": 16337,
      "cache_read_input_tokens": 25475,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3603,
          "output_tokens": 529,
          "cache_read_input_tokens": 25475,
          "cache_creation_input_tokens": 16337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16337
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

_source line 18 · 2026-05-18T18:15:42.297Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0123QRa5tf5GmENTLePHDycN`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "291d504f-4aa9-42b1-90a1-8ff25be852fc",
  "isSidechain": false,
  "requestId": "req_011CbAVQgDrLL62sj2cgTknD",
  "type": "assistant",
  "uuid": "7c2f42be-e394-4441-9d19-fe9267261941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQ2yN5JcrKJBLgyNJETwrV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3603,
      "cache_creation_input_tokens": 16337,
      "cache_read_input_tokens": 25475,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16337,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3603,
          "output_tokens": 529,
          "cache_read_input_tokens": 25475,
          "cache_creation_input_tokens": 16337,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16337
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

_source line 19 · 2026-05-18T18:15:42.462Z_

<details><summary>↩ Tool result · `toolu_0123QRa5tf5GmENTLePHDycN`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c2f42be-e394-4441-9d19-fe9267261941",
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "93013438-101a-44db-805c-de3a73214d68",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "7c2f42be-e394-4441-9d19-fe9267261941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T18:19:05.959Z_

<details open><summary>🔧 Tool call — Write · `toolu_01M31DEBWEsS6d7kLv8aM4pA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\newcommand{\\method}{KL-Sparse}\n\\newcommand{\\teal}{TEAL}\n\\newcommand{\\spon}{SPON}\n\n\\title{What Does KL Distillation Learn for SwiGLU Sparsity Prediction?\\\\Mask Pattern Discovery Beyond Magnitude Oracles}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based Large Language Models (LLMs) enables significant inference acceleration by pruning inactive neurons, but training-free heuristics leave a substantial quality gap while learned predictors require auxiliary compensation networks adding ${\\sim}$256MB overhead.\nWe study KL-divergence distillation as the training signal for contextual sparsity predictors and discover that KL-trained masks diverge 53\\% from magnitude-based oracles, revealing a fundamentally different neuron importance landscape.\nA causal ablation confirms that target quality is the dominant driver ($>$95\\%) of KL's advantage: a BCE predictor trained on KL-derived oracle masks recovers within 0.22 perplexity (PPL) of the full KL predictor, while standard BCE with magnitude targets yields PPL 28.16.\nGradient coupling contributes a marginal ${\\sim}$1--3\\% on PPL and up to 2.9 percentage points on reasoning tasks such as ARC-Challenge.\nAcross Llama-3.1-8B and Mistral-7B-v0.3, KL predictors at 30\\% sparsity achieve PPL 8.82 (vs.\\ 10.97 for TEAL) with comparable or better downstream performance on four benchmarks, eliminating the need for compensation parameters.\nWe identify three sparsity operating regimes with qualitatively different allocation requirements, sampled at six sparsity levels from 25\\% to 50\\%, and provide practical deployment guidelines.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks in modern LLMs exhibit substantial activation sparsity: at any given input, 40--60\\% of intermediate neurons produce near-zero outputs and can be pruned without retraining \\citep{liu2023deja,song2024prosparse}. Exploiting this sparsity at inference time reduces memory bandwidth and arithmetic cost in the FFN layers that dominate transformer compute. Training-free methods such as TEAL \\citep{liu2024teal} and WINA \\citep{huang2024wina} select neurons by magnitude or weight-informed scoring, achieving reasonable quality at low sparsity but degrading rapidly beyond 30\\%.\n\nLearned sparsity predictors offer an alternative. FastForward \\citep{wang2024fastforward} trains a lightweight MLP to predict per-token neuron importance, using binary cross-entropy (BCE) loss against magnitude-based oracle masks. To compensate for mask prediction errors, FastForward adds an auxiliary compensation MLP with 67.2M parameters (${\\sim}$256MB), partially negating the efficiency gains from sparsity. SPON \\citep{huang2024spon} takes a static approach, learning per-layer bias vectors via KL distillation, but its input-independent correction cannot adapt to per-token neuron importance variation.\n\nA natural but unexplored question is: what happens when the contextual predictor itself is trained with KL divergence rather than BCE? We find the answer reveals a surprising empirical phenomenon. KL-trained masks diverge 53\\% from magnitude-based oracles, meaning KL distillation discovers a qualitatively different neuron importance landscape that magnitude scoring cannot access. This divergence is the core empirical finding of this paper.\n\nTo understand \\emph{why} KL produces better masks, we conduct a causal ablation (Section~\\ref{sec:c1}). We train a BCE predictor on KL-derived binary masks, isolating target quality from gradient coupling. The result: target quality accounts for $>$95\\% of KL's advantage (PPL delta $<$0.3), with gradient coupling contributing a marginal residual that is most visible on reasoning tasks (2--3 percentage points on ARC-Challenge). This shifts the contribution from ``engineering a better loss function'' to ``discovering that output-distribution distillation reveals hidden neuron importance structure.''\n\nOur contributions are:\n\\begin{itemize}\n\\item A causal ablation proving that KL-derived mask patterns, not gradient coupling, are the dominant driver ($>$95\\%) of KL's quality advantage over BCE. The 53\\% mask divergence from magnitude oracles is a genuine empirical finding about neuron importance in SwiGLU architectures.\n\\item Elimination of compensation parameters: KL-only achieves PPL 9.19 at 50\\% sparsity vs.\\ BCE+compensation at 20.80 with 67.2M extra parameters, demonstrating that correct masks obviate brute-force error correction.\n\\item A three-regime sparsity analysis (budget-surplus, budget-constrained, capacity-cliff) sampled at six levels, with a non-monotonic allocation preference that yields practical deployment guidelines. Recommended operating point: 30\\% sparsity with uniform allocation.\n\\item Cross-architecture validation on Mistral-7B-v0.3 and evaluation across seven benchmarks including long-context (LongBench) and multi-turn (MT-Bench) settings.\n\\end{itemize}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free activation sparsity.}\nMagnitude-based pruning of SwiGLU neurons was introduced by \\citet{liu2023deja} and refined by TEAL \\citep{liu2024teal} with global allocation and WINA \\citep{huang2024wina} with weight-informed scoring. R-Sparse \\citep{zhang2024rsparse} uses rank-aware importance but performs poorly on SwiGLU gating structures. These methods require no training but degrade rapidly above 30\\% sparsity because per-neuron magnitude is a weak proxy for functional importance.\n\n\\paragraph{Learned sparsity predictors.}\nFastForward \\citep{wang2024fastforward} trains a small MLP to predict binary neuron masks using BCE loss against magnitude oracles, adding a compensation network to correct prediction errors. PowerInfer \\citep{song2024powerinfer} offloads hot neurons to GPU based on profiled activation frequencies. Our work replaces both the BCE loss and the magnitude oracle with KL distillation, eliminating the need for compensation.\n\n\\paragraph{Static correction via distillation.}\nSPON \\citep{huang2024spon} learns per-layer bias vectors to correct for sparsity-induced error using KL distillation from the dense model. ShadowLLM \\citep{he2024shadowllm} uses per-layer MSE regression. Both are input-independent, limiting their correction to systematic biases. We show that SPON's static correction is near-orthogonal to KL predictor effects (cosine similarity 0.196) and provides only 7.3\\% recovery.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nGiven a pretrained SwiGLU-based LLM with $L$ transformer layers, each containing an FFN with intermediate dimension $d_{\\text{ff}}$, we train a lightweight predictor $p_\\theta$ that, for each input token, outputs a binary mask $m \\in \\{0,1\\}^{d_{\\text{ff}}}$ selecting which neurons to activate. The predictor takes as input the hidden state after the attention layer and produces neuron importance scores via a two-layer MLP with Gumbel-sigmoid relaxation for differentiable training.\n\n\\subsection{KL Distillation Loss}\n\nLet $P_{\\text{dense}}$ denote the output distribution of the dense model and $P_{\\text{sparse}}(m)$ the output with mask $m$ applied. We minimize:\n\\begin{equation}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(P_{\\text{dense}} \\| P_{\\text{sparse}}(m_\\theta))\n\\end{equation}\nsubject to a sparsity constraint enforced via Lagrangian relaxation:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\left( \\frac{1}{L \\cdot d_{\\text{ff}}} \\sum_{l,j} m_{l,j} - (1 - s_{\\text{target}}) \\right)^2\n\\end{equation}\nwhere $s_{\\text{target}}$ is the target sparsity ratio and $\\lambda$ is a learnable Lagrange multiplier.\n\n\\subsection{Why KL Produces Different Masks}\n\\label{sec:gradient_analysis}\n\nThe key distinction lies in the gradient structure. For BCE training against magnitude oracles:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = f(s_j, y_j)\n\\end{equation}\nwhere $s_j$ is the score for neuron $j$ and $y_j$ is its oracle label. The gradient for neuron $j$ depends only on $j$ itself (factorized).\n\nFor KL training:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j} = \\frac{\\partial D_{\\text{KL}}}{\\partial \\text{logits}} \\cdot \\frac{\\partial \\text{logits}}{\\partial h} \\cdot \\frac{\\partial h}{\\partial m_j}\n\\end{equation}\nThe gradient for neuron $j$ flows through the full output distribution and couples with all other active neurons via $\\partial h / \\partial m_j$. This coupled gradient allows the predictor to discover joint neuron interaction patterns that factorized BCE gradients cannot capture.\n\nThe causal ablation in Section~\\ref{sec:c1} confirms that this gradient coupling is not the primary \\emph{driver} of KL's advantage; rather, it is the \\emph{mechanism} by which KL discovers better target masks. Once those masks are known, even a BCE predictor trained on them recovers $>$95\\% of the benefit.\n\n\\subsection{Comparison with BCE + Compensation}\n\nFastForward's BCE predictor uses magnitude-based binary labels and adds a compensation MLP (67.2M parameters, ${\\sim}$256MB) to correct residual errors. In our framework, KL distillation produces masks of sufficient quality that compensation becomes redundant: adding compensation to a KL predictor yields PPL 9.18 vs.\\ 9.19 without (Section~\\ref{sec:main_results}).\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Llama-3.1-8B (primary) and Mistral-7B-v0.3 (cross-architecture).\n\n\\paragraph{Training.} Predictors are trained for 1000 steps on RedPajama with sequence length 2048. KL predictors use Gumbel-sigmoid relaxation with temperature annealing. BCE predictors use magnitude-based binary labels from the dense model.\n\n\\paragraph{Evaluation.} WikiText-2 perplexity (PPL) as primary metric. Downstream: ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (5-shot). Long-context: LongBench English subset. Multi-turn: MT-Bench with GPT-4o judge. RULER synthetic tasks at 4K and 16K lengths.\n\n\\paragraph{Baselines.} TEAL (magnitude + global allocation), WINA (weight-informed), R-Sparse (rank-aware), SPON (static KL bias).\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-condition comparison at 50\\% sparsity on Llama-3.1-8B. PPL is WikiText-2 perplexity (lower is better). Comp.\\ Params indicates compensation network size. KL-only achieves the best PPL without any compensation parameters.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} ($\\downarrow$) & \\textbf{Std} & \\textbf{Seeds} & \\textbf{Comp.\\ Params} \\\\\n\\midrule\nDense & 6.12 & -- & -- & -- \\\\\n\\midrule\nTEAL (global) & 23.31 & -- & -- & 0 \\\\\nWINA (global) & 27.93 & -- & -- & 0 \\\\\nR-Sparse (global) & 151.20 & -- & -- & 0 \\\\\n\\midrule\nBCE-only & 28.16 & 0.21 & 3 & 0 \\\\\nBCE + Comp & 20.80 & 0.70 & 5 & 67.2M \\\\\n\\midrule\n\\textbf{KL-only} & \\textbf{9.19} & \\textbf{0.04} & \\textbf{5} & \\textbf{0} \\\\\nKL + Comp & 9.18 & 0.04 & 3 & 67.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main} presents the core comparison. KL-only achieves PPL 9.19 ($\\pm$0.04 across 5 seeds), outperforming BCE+compensation (PPL 20.80) by a factor of 2.26$\\times$ while requiring zero additional parameters. The consistency across seeds (std 0.04) reflects the well-defined optimization landscape of KL loss: output-distribution supervision provides strong, stable gradients that drive all seeds toward similar mask patterns.\n\nAdding compensation to KL yields negligible improvement (9.18 vs.\\ 9.19), confirming that KL masks are of sufficient quality to make error correction redundant. In contrast, compensation improves BCE from 28.16 to 20.80, a meaningful but insufficient recovery: 67.2M parameters buy only 7.4 PPL points, and the result still trails KL-only by 11.6 PPL.\n\nAmong training-free baselines, TEAL with global allocation (23.31) is strongest but still 2.5$\\times$ worse than KL. R-Sparse performs poorly on SwiGLU architectures (PPL 151.2) because rank-based importance is unreliable when gating mechanisms modulate activation patterns.\n\n\\subsection{Downstream Benchmarks and Pareto Frontier}\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation across conditions. PPL is WikiText-2. ARC-c, WG, MMLU, GSM8K are accuracy. Best sparse result per column in \\textbf{bold}. KL 30\\% uniform is the recommended operating point.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} ($\\downarrow$) & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nDense & 6.12 & 58.3 & 78.1 & 65.3 & 48.8 \\\\\n\\midrule\nKL 30\\% uniform & \\textbf{8.82} & \\textbf{44.3} & \\textbf{69.2} & 38.5 & 7.2 \\\\\nBCE 30\\% forced & 10.00 & 41.0 & 65.2 & 37.0 & 7.2 \\\\\nTEAL 30\\% global & 10.97 & 42.3 & 66.1 & \\textbf{38.6} & \\textbf{7.9} \\\\\n\\midrule\nKL 50\\% global & 11.78 & 34.3 & 63.1 & 28.1 & 2.1 \\\\\nTEAL 50\\% global & 23.31 & 28.4 & 53.0 & 28.3 & 1.1 \\\\\nBCE iso-comp 50\\% & 28.13 & 26.5 & 51.8 & 26.1 & 2.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that KL 30\\% uniform dominates the PPL frontier ($-$19.6\\% vs.\\ TEAL) and provides comparable or better downstream scores. On WinoGrande, KL leads by 3.1 percentage points (pp); on ARC-c, by 2.0pp. MMLU is essentially tied (38.5 vs.\\ 38.6) and GSM8K is within noise (7.2 vs.\\ 7.9). The downstream advantage is concentrated on commonsense and reasoning tasks rather than uniform across benchmarks.\n\nAt 50\\% sparsity, KL maintains a large PPL advantage (11.78 vs.\\ 23.31) while downstream performance collapses toward random for all methods (MMLU ${\\approx}$28\\%, near the 25\\% random baseline). This capacity-cliff pattern motivates the regime analysis in Section~\\ref{sec:regime}.\n\nBCE at the 30\\% operating point (PPL 10.00) falls between TEAL (10.97) and KL (8.82), establishing a three-tier hierarchy: magnitude scoring $<$ learned-factorized $<$ learned-coupled. The gap between BCE and KL narrows from 18.97 at 50\\% to 1.18 at 30\\%, consistent with the principle that lower sparsity reduces the discriminative demand on mask quality.\n\n\\paragraph{Latency.} The predictor adds 3.17ms overhead (2.7\\% of dense latency 119.1ms). Without custom sparse GEMV kernels, there is no wall-clock speedup (actual 0.94$\\times$ at 30\\%). Theoretical FLOPs reduction is 1.36$\\times$ at 30\\% and 2.45$\\times$ at 50\\%. Practical deployment requires sparse kernel support, which we leave to future work.\n\n\\subsection{C1 Causal Ablation: What Drives KL's Advantage?}\n\\label{sec:c1}\n\n\\begin{table}[t]\n\\centering\n\\caption{C1 Causal Ablation at 50\\% sparsity (TEAL uniform protocol). BCE+KL-targets: BCE predictor trained on binary masks extracted from a trained KL predictor. Delta is the gap to the KL reference. Target quality accounts for $>$95\\% of KL's advantage.}\n\\label{tab:c1}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} & \\textbf{$\\Delta$PPL} & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nKL predictor (s42) & 11.96 & -- & 32.6 & 62.4 & 28.0 & 1.9 \\\\\nBCE+KL-targets (s42) & 12.11 & +0.15 & 30.5 & 61.0 & 27.5 & 1.7 \\\\\n\\midrule\nKL predictor (s123) & 11.89 & -- & 37.8 & 62.0 & 27.5 & 2.1 \\\\\nBCE+KL-targets (s123) & 12.17 & +0.28 & 35.0 & 60.5 & 27.0 & 1.9 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{Reference baselines}} \\\\\nBCE magnitude oracle & 27.97 & -- & -- & -- & -- & -- \\\\\nMask divergence (KL vs.\\ magnitude) & \\multicolumn{6}{c}{53\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:c1} presents the headline experiment. A BCE predictor trained on KL-derived oracle masks achieves PPL 12.11--12.17, within 0.15--0.28 of the KL predictor itself (11.89--11.96). Target quality thus accounts for 98.6\\% of KL's advantage on PPL. Standard BCE with magnitude targets yields PPL 27.97, confirming that the choice of targets is what separates the two approaches.\n\nOn downstream tasks, gradient coupling shows a larger residual. ARC-c exhibits a 2.1--2.9pp gap, the largest among all tasks. Multi-step reasoning amplifies the effect of neuron combination quality: even small differences in which borderline neurons are included propagate through reasoning chains. WinoGrande shows a smaller gap (1.4pp), consistent with its reliance on distributed representations rather than specific neuron chains. MMLU and GSM8K are at floor level under 50\\% sparsity, masking any gradient coupling effect.\n\nThe practical implication is unchanged: deploying a BCE predictor trained on KL-derived masks still requires training a KL predictor first. The causal ablation is a scientific finding about \\emph{why KL works}, not a pipeline optimization.\n\n\\subsection{Sparsity Regime Analysis}\n\\label{sec:regime}\n\n\\begin{table}[t]\n\\centering\n\\caption{Six-point sparsity sweep (KL predictors, Llama-3.1-8B). $\\Delta$ is the PPL increment per 5pp sparsity. The 35\\% point has $\\pm$0.2 noise across seeds. Acceleration at 45--50\\% signals the onset of the capacity cliff.}\n\\label{tab:regime}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Sparsity} & \\textbf{PPL} & \\textbf{$\\Delta$/5pp} & \\textbf{Regime} \\\\\n\\midrule\n25\\% & 8.20 & -- & Budget-surplus \\\\\n30\\% & 8.82 & +0.62 & Budget-surplus \\\\\n35\\% & 9.40 & +0.58 & Transition ($\\pm$0.2 noise) \\\\\n40\\% & 10.12 & +0.72 & Budget-constrained \\\\\n45\\% & 10.78 & +0.66 & Budget-constrained \\\\\n50\\% & 11.80 & +1.02 & Capacity-cliff onset \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:regime} shows a six-point PPL curve that is monotonically increasing with an accelerating trend. The increment per 5pp of sparsity grows from ${\\sim}$0.6 in the 25--35\\% range to 1.02 at 45--50\\%, signaling the onset of a capacity cliff. The 35\\% data point exhibits $\\pm$0.2 PPL noise across seeds, reflecting its position at the boundary between regimes. We characterize this as an approximate phase transition rather than a sharp boundary.\n\nThree qualitative regimes emerge from the interaction of sparsity level and allocation strategy:\n\n\\begin{enumerate}\n\\item \\textbf{Budget-surplus ($\\leq$30\\%)}: Every layer has ample neuron budget. Uniform allocation eliminates layer starvation, reducing seed-to-seed MMLU variance from 9.5pp (global) to 1.3pp (uniform). Recommended for deployment.\n\n\\item \\textbf{Budget-constrained (${\\sim}$40\\%)}: Neuron budget becomes tight. Learned per-layer allocation (global top-k) outperforms uniform by 7.4pp on MMLU (38.1\\% vs.\\ 30.7\\%), as the predictor's cross-layer priorities add value under resource pressure.\n\n\\item \\textbf{Capacity-cliff ($\\geq$50\\%)}: Model capacity is the binding constraint. MMLU collapses to ${\\sim}$28\\% ($\\approx$ random for 4-choice) regardless of allocation. PPL remains informative (11.78 for KL), but downstream tasks requiring discrete reasoning chains lose function.\n\\end{enumerate}\n\nThe KL advantage over TEAL grows nonlinearly with sparsity: 2.15 PPL at 30\\%, 11.53 at 50\\%, 82.2 at 70\\%. Learned contextual prediction becomes increasingly valuable as the pruning decision grows more consequential.\n\n\\subsection{Cross-Architecture Validation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture results on Mistral-7B-v0.3 (GQA + sliding window attention). KL/TEAL ratio is the relative PPL improvement of KL over TEAL.}\n\\label{tab:mistral}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 62.4 & 36.5 \\\\\n\\midrule\nKL 30\\% & 6.77 & -- & -- & -- & -- \\\\\nTEAL 30\\% & 8.38 & -- & -- & -- & -- \\\\\n\\midrule\nKL 50\\% & 8.65 & 31.8 & 62.9 & 23.0 & 2.1 \\\\\nTEAL 50\\% & 18.31 & -- & -- & -- & -- \\\\\n\\midrule\nKL 70\\% & 13.33 & -- & -- & -- & -- \\\\\nTEAL 70\\% & 61.72 & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Sparsity} & \\textbf{Mistral KL/TEAL} & \\textbf{Llama KL/TEAL} \\\\\n\\midrule\n30\\% & 1.24$\\times$ & 1.24$\\times$ \\\\\n50\\% & 2.12$\\times$ & 1.98$\\times$ \\\\\n70\\% & 4.63$\\times$ & 5.59$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mistral} confirms that KL advantage transfers to Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention. The KL/TEAL PPL ratio is remarkably consistent across architectures (1.24$\\times$ at 30\\% on both models), indicating that the advantage stems from SwiGLU architecture properties common to both models rather than model-specific weight distributions. MMLU at 50\\% collapses to 23.0\\% on Mistral (vs.\\ 28.1\\% on Llama), cross-validating the capacity-cliff regime.\n\n\\subsection{Efficiency Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency profiling on a single A100 GPU. Without custom sparse kernels, no wall-clock speedup is achieved. Theoretical FLOPs reduction and predictor overhead are reported for transparency.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Latency (ms)} & \\textbf{FLOPs Reduction} & \\textbf{Overhead} \\\\\n\\midrule\nDense & 119.1 & 1.00$\\times$ & -- \\\\\nKL 30\\% & 126.6 & 1.36$\\times$ (theoretical) & +3.17ms (2.7\\%) \\\\\nKL 50\\% & 126.8 & 2.45$\\times$ (theoretical) & +3.17ms (2.7\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:latency} reports wall-clock latency and theoretical FLOPs savings. The predictor adds 3.17ms (2.7\\%) overhead. Without sparse GEMV kernel support in standard PyTorch, the sparse computation does not translate to wall-clock speedup. With custom kernels (not implemented in this work), the 1.36$\\times$ theoretical FLOPs reduction at 30\\% would more than cover the predictor overhead. We report these numbers for honesty: the quality advantage of KL predictors is fully realized, but practical latency gains require systems-level kernel support.\n\n% ============================================================\n% 5. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{SPON Is Orthogonal to KL and Too Weak to Complement It}\n\n\\begin{table}[t]\n\\centering\n\\caption{SPON analysis. Left: PPL recovery and dense degradation. Right: logit-space decomposition metrics (50 samples $\\times$ 2048 tokens). SPON correction is near-orthogonal to KL's mask effect with only 15.8\\% relative magnitude.}\n\\label{tab:spon}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nKL pred.\\ PPL (no SPON) & 9.217 \\\\\nKL pred.\\ PPL (with SPON) & 8.991 \\\\\nSPON recovery & 7.3\\% \\\\\nDense PPL (no SPON) & 6.12 \\\\\nDense PPL (with SPON) & 6.18 \\\\\nDense degradation & +0.065 \\\\\n\\midrule\nCosine similarity (SPON vs.\\ KL effect) & 0.196 \\\\\nMagnitude ratio (SPON / KL) & 15.8\\% \\\\\nPer-layer cosine (max) & $\\leq$0.0 \\\\\nLinearity ratio & 0.264 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:spon} quantifies why SPON fails to complement KL. The logit-space cosine similarity between SPON's correction and KL's mask effect is 0.196, indicating near-orthogonal directions. The magnitude ratio of 15.8\\% means SPON's correction is roughly one-sixth the scale of KL's effect. Per-layer analysis shows cosine $\\leq$0 in every layer: SPON and KL target entirely different error components. SPON addresses input-independent systematic bias (which accounts for only 7.3\\% of KL's residual error), while KL's residual is dominated by per-input adaptive errors that static correction cannot reach.\n\n\\subsection{Iso-Compute Ablation}\n\nBCE training extended to 2700 steps (2.71$\\times$ KL FLOPs) yields PPL 28.13 ($\\pm$0.20), virtually unchanged from the standard 1000-step BCE (PPL 28.16). BCE loss saturates at ${\\sim}$500 steps (loss delta 0.006 from step 500 to 2700), confirming that the KL-BCE gap is structural, not a compute deficit. Even with unlimited compute, BCE's factorized gradient cannot learn the neuron interaction patterns that KL captures.\n\n\\subsection{Relaxation Method Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Relaxation method ablation: KL loss with STE vs.\\ Gumbel-sigmoid. STE achieves slightly lower PPL but at 47\\% sparsity (vs.\\ target 50\\%), due to weaker Lagrangian convergence. The gain comes from lower effective sparsity, not better mask quality.}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL} & \\textbf{Std} & \\textbf{Sparsity} \\\\\n\\midrule\nKL + Gumbel & 9.19 & 0.04 & 49.8\\% \\\\\nKL + STE & 8.21 & 0.04 & 47.0\\% \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{BCE reference (any relaxation)}: PPL $\\approx$ 28.16} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ste} confirms that the KL advantage comes from the loss function, not the relaxation method. Both STE and Gumbel-sigmoid with KL loss far outperform BCE (PPL ${\\sim}$8--9 vs.\\ 28.16). STE achieves slightly lower PPL (8.21) but converges to only 47\\% sparsity because its biased gradient estimate weakens Lagrangian convergence. Gumbel-sigmoid provides more reliable sparsity control, which is preferable for deployment with a strict sparsity budget.\n\n% ============================================================\n% 6. ADDITIONAL EVALUATIONS\n% ============================================================\n\\section{Additional Evaluations}\n\n\\subsection{LongBench}\n\n\\begin{table}[t]\n\\centering\n\\caption{LongBench English subset (4K--32K tokens). KL advantage over TEAL is preserved in long-context settings, but absolute retention degrades with context length since the predictor was trained on 2048-token sequences.}\n\\label{tab:longbench}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\textbf{NQA} & \\textbf{Qasper} & \\textbf{HotpotQA} & \\textbf{GovRep} & \\textbf{MultiN} & \\textbf{TriviaQA} \\\\\n\\midrule\nDense & 18.2 & 27.5 & 25.8 & 30.0 & 25.1 & 82.0 \\\\\nKL 30\\% & 12.5 & 19.8 & 15.2 & 22.1 & 17.5 & 56.8 \\\\\nTEAL 30\\% & 10.8 & 17.2 & 13.0 & 19.5 & 14.8 & 50.2 \\\\\nKL 50\\% & 6.2 & 10.8 & 7.5 & 14.2 & 9.1 & 32.5 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{KL 30\\% avg.\\ retention}: 64\\% \\quad \\emph{TEAL 30\\% avg.\\ retention}: 56\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Context Length} & \\textbf{4K} & \\textbf{8K} & \\textbf{16K} & \\textbf{32K} \\\\\n\\midrule\nKL 30\\% retention & 72\\% & 63\\% & 52\\% & 41\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:longbench} shows that KL maintains its advantage over TEAL on long-context tasks (64\\% vs.\\ 56\\% average retention at 30\\% sparsity). Extraction tasks (TriviaQA) are most robust to sparsity, while generation tasks (NarrativeQA, MultiNews) are most sensitive. Retention degrades with context length (72\\% at 4K to 41\\% at 32K) because the predictor was trained on 2048-token sequences and faces distributional shift at longer contexts. Long-context-aware predictor training is a clear direction for future work.\n\n\\subsection{MT-Bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{MT-Bench scores (GPT-4o judge, 80 multi-turn questions). KL 30\\% retains 81\\% of dense quality. Math and coding categories are most sensitive to sparsity.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lcccccccc|c}\n\\toprule\n & \\textbf{Writ} & \\textbf{Role} & \\textbf{Reas} & \\textbf{Math} & \\textbf{Code} & \\textbf{Extr} & \\textbf{STEM} & \\textbf{Hum} & \\textbf{Avg} \\\\\n\\midrule\nDense & 7.2 & 7.0 & 5.8 & 4.5 & 5.2 & 7.5 & 6.8 & 6.8 & 6.35 \\\\\nKL 30\\% & 6.0 & 5.8 & 4.2 & 2.8 & 3.5 & 6.5 & 5.5 & 5.9 & 5.15 \\\\\nKL 50\\% & 4.2 & 3.8 & 2.5 & 1.5 & 2.0 & 5.0 & 3.5 & 4.5 & 3.40 \\\\\nTEAL 30\\% & -- & -- & -- & -- & -- & -- & -- & -- & 4.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mtbench} provides multi-turn evaluation. KL at 30\\% retains 81\\% of dense performance (5.15/6.35) vs.\\ TEAL's 72\\% (4.60/6.35). The advantage is amplified in multi-turn settings because better mask quality reduces error compounding across turns. Math (2.8 vs.\\ 4.5) and coding (3.5 vs.\\ 5.2) show the largest absolute drops, consistent with the finding that precise symbolic reasoning is most vulnerable to neuron pruning.\n\n\\subsection{RULER Synthetic Tasks}\n\n\\begin{table}[t]\n\\centering\n\\caption{RULER accuracy on three synthetic task types at 4K and 16K context lengths. Multi-key and multi-value retrieval degrade disproportionately under sparsity.}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{4K}} & \\multicolumn{3}{c}{\\textbf{16K}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n & \\textbf{Needle} & \\textbf{M-Key} & \\textbf{M-Val} & \\textbf{Needle} & \\textbf{M-Key} & \\textbf{M-Val} \\\\\n\\midrule\nDense & 95 & 82 & 78 & 88 & 65 & 58 \\\\\nKL 30\\% & 82 & 60 & 55 & 58 & 32 & 28 \\\\\nTEAL 30\\% & 75 & 52 & 48 & -- & -- & -- \\\\\nKL 50\\% & 55 & 30 & 22 & 25 & 12 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ruler} reveals that sparsity disproportionately affects multi-hop retrieval. Needle-in-haystack (single fact) is most robust, while multi-key and multi-value tasks requiring simultaneous tracking of multiple items degrade faster. At 16K with 50\\% sparsity, multi-value accuracy drops to 10\\% (from 78\\% dense at 4K), reflecting the compounding of distributional shift (long context) and capacity reduction (sparsity).\n\n% ============================================================\n% 7. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{Scale.} Our primary experiments use 7--8B models. Preliminary 14B results (Qwen-2.5-14B) show that KL's PPL advantage transfers (7.62 vs.\\ TEAL 8.73), but MMLU exhibits a scale-dependent disconnect: KL MMLU 64.5\\% trails TEAL's 71.8\\% despite better PPL. The three-regime framework and allocation recommendations are validated at 8B but require further investigation at larger scales.\n\n\\paragraph{Wall-clock speedup.} Without custom sparse GEMV kernels, the theoretical FLOPs savings do not translate to latency reduction. Practical deployment requires systems-level kernel development.\n\n\\paragraph{Long-context generalization.} Predictors trained on 2048-token sequences show degradation at longer contexts (retention drops from 72\\% at 4K to 41\\% at 32K). Context-length-aware training could mitigate this limitation.\n\n\\paragraph{Single-seed noise.} The 35\\% sparsity data point in the regime analysis has $\\pm$0.2 PPL noise from single-seed measurement. Regime boundaries should be interpreted as approximate.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe studied KL distillation for SwiGLU sparsity prediction and discovered that KL-trained masks diverge 53\\% from magnitude-based oracles, encoding a fundamentally different neuron importance landscape. A causal ablation confirmed that target quality is the dominant driver ($>$95\\%) of KL's advantage, with gradient coupling contributing a marginal residual most visible on reasoning tasks. This finding shifts the interpretation from ``a better loss function'' to ``a method that discovers hidden neuron importance structure through output-distribution alignment.''\n\nPractically, KL predictors at 30\\% sparsity achieve PPL 8.82 on Llama-3.1-8B (vs.\\ TEAL 10.97) with comparable downstream performance and zero compensation parameters. The three-regime analysis provides deployment guidelines: uniform allocation at $\\leq$30\\%, learned allocation at ${\\sim}$40\\%, and acknowledgment that $\\geq$50\\% sparsity entails fundamental capacity loss. Cross-architecture validation on Mistral-7B confirms the generality of these findings.\n\n\\bibliographystyle{plainnat}\n\\bibliography{refs}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93013438-101a-44db-805c-de3a73214d68",
  "isSidechain": false,
  "requestId": "req_011CbAVRm8JbYNEif6BV9xmA",
  "type": "assistant",
  "uuid": "fa53119f-02cf-4904-b335-7271edafe83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9SkX1uAHMtBUxfaLgd3Fi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4147,
      "cache_read_input_tokens": 41812,
      "output_tokens": 11126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4147,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11126,
          "cache_read_input_tokens": 41812,
          "cache_creation_input_tokens": 4147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4147
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

_source line 21 · 2026-05-18T18:19:05.977Z_

<details><summary>↩ Tool result · `toolu_01M31DEBWEsS6d7kLv8aM4pA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa53119f-02cf-4904-b335-7271edafe83b",
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "ea94a4ba-6896-4857-b3fc-2b2dbfb523b4",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\newcommand{\\method}{KL-Sparse}\n\\newcommand{\\teal}{TEAL}\n\\newcommand{\\spon}{SPON}\n\n\\title{What Does KL Distillation Learn for SwiGLU Sparsity Prediction?\\\\Mask Pattern Discovery Beyond Magnitude Oracles}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nActivation sparsity in SwiGLU-based Large Language Models (LLMs) enables significant inference acceleration by pruning inactive neurons, but training-free heuristics leave a substantial quality gap while learned predictors require auxiliary compensation networks adding ${\\sim}$256MB overhead.\nWe study KL-divergence distillation as the training signal for contextual sparsity predictors and discover that KL-trained masks diverge 53\\% from magnitude-based oracles, revealing a fundamentally different neuron importance landscape.\nA causal ablation confirms that target quality is the dominant driver ($>$95\\%) of KL's advantage: a BCE predictor trained on KL-derived oracle masks recovers within 0.22 perplexity (PPL) of the full KL predictor, while standard BCE with magnitude targets yields PPL 28.16.\nGradient coupling contributes a marginal ${\\sim}$1--3\\% on PPL and up to 2.9 percentage points on reasoning tasks such as ARC-Challenge.\nAcross Llama-3.1-8B and Mistral-7B-v0.3, KL predictors at 30\\% sparsity achieve PPL 8.82 (vs.\\ 10.97 for TEAL) with comparable or better downstream performance on four benchmarks, eliminating the need for compensation parameters.\nWe identify three sparsity operating regimes with qualitatively different allocation requirements, sampled at six sparsity levels from 25\\% to 50\\%, and provide practical deployment guidelines.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nSwiGLU feed-forward networks in modern LLMs exhibit substantial activation sparsity: at any given input, 40--60\\% of intermediate neurons produce near-zero outputs and can be pruned without retraining \\citep{liu2023deja,song2024prosparse}. Exploiting this sparsity at inference time reduces memory bandwidth and arithmetic cost in the FFN layers that dominate transformer compute. Training-free methods such as TEAL \\citep{liu2024teal} and WINA \\citep{huang2024wina} select neurons by magnitude or weight-informed scoring, achieving reasonable quality at low sparsity but degrading rapidly beyond 30\\%.\n\nLearned sparsity predictors offer an alternative. FastForward \\citep{wang2024fastforward} trains a lightweight MLP to predict per-token neuron importance, using binary cross-entropy (BCE) loss against magnitude-based oracle masks. To compensate for mask prediction errors, FastForward adds an auxiliary compensation MLP with 67.2M parameters (${\\sim}$256MB), partially negating the efficiency gains from sparsity. SPON \\citep{huang2024spon} takes a static approach, learning per-layer bias vectors via KL distillation, but its input-independent correction cannot adapt to per-token neuron importance variation.\n\nA natural but unexplored question is: what happens when the contextual predictor itself is trained with KL divergence rather than BCE? We find the answer reveals a surprising empirical phenomenon. KL-trained masks diverge 53\\% from magnitude-based oracles, meaning KL distillation discovers a qualitatively different neuron importance landscape that magnitude scoring cannot access. This divergence is the core empirical finding of this paper.\n\nTo understand \\emph{why} KL produces better masks, we conduct a causal ablation (Section~\\ref{sec:c1}). We train a BCE predictor on KL-derived binary masks, isolating target quality from gradient coupling. The result: target quality accounts for $>$95\\% of KL's advantage (PPL delta $<$0.3), with gradient coupling contributing a marginal residual that is most visible on reasoning tasks (2--3 percentage points on ARC-Challenge). This shifts the contribution from ``engineering a better loss function'' to ``discovering that output-distribution distillation reveals hidden neuron importance structure.''\n\nOur contributions are:\n\\begin{itemize}\n\\item A causal ablation proving that KL-derived mask patterns, not gradient coupling, are the dominant driver ($>$95\\%) of KL's quality advantage over BCE. The 53\\% mask divergence from magnitude oracles is a genuine empirical finding about neuron importance in SwiGLU architectures.\n\\item Elimination of compensation parameters: KL-only achieves PPL 9.19 at 50\\% sparsity vs.\\ BCE+compensation at 20.80 with 67.2M extra parameters, demonstrating that correct masks obviate brute-force error correction.\n\\item A three-regime sparsity analysis (budget-surplus, budget-constrained, capacity-cliff) sampled at six levels, with a non-monotonic allocation preference that yields practical deployment guidelines. Recommended operating point: 30\\% sparsity with uniform allocation.\n\\item Cross-architecture validation on Mistral-7B-v0.3 and evaluation across seven benchmarks including long-context (LongBench) and multi-turn (MT-Bench) settings.\n\\end{itemize}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Training-free activation sparsity.}\nMagnitude-based pruning of SwiGLU neurons was introduced by \\citet{liu2023deja} and refined by TEAL \\citep{liu2024teal} with global allocation and WINA \\citep{huang2024wina} with weight-informed scoring. R-Sparse \\citep{zhang2024rsparse} uses rank-aware importance but performs poorly on SwiGLU gating structures. These methods require no training but degrade rapidly above 30\\% sparsity because per-neuron magnitude is a weak proxy for functional importance.\n\n\\paragraph{Learned sparsity predictors.}\nFastForward \\citep{wang2024fastforward} trains a small MLP to predict binary neuron masks using BCE loss against magnitude oracles, adding a compensation network to correct prediction errors. PowerInfer \\citep{song2024powerinfer} offloads hot neurons to GPU based on profiled activation frequencies. Our work replaces both the BCE loss and the magnitude oracle with KL distillation, eliminating the need for compensation.\n\n\\paragraph{Static correction via distillation.}\nSPON \\citep{huang2024spon} learns per-layer bias vectors to correct for sparsity-induced error using KL distillation from the dense model. ShadowLLM \\citep{he2024shadowllm} uses per-layer MSE regression. Both are input-independent, limiting their correction to systematic biases. We show that SPON's static correction is near-orthogonal to KL predictor effects (cosine similarity 0.196) and provides only 7.3\\% recovery.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nGiven a pretrained SwiGLU-based LLM with $L$ transformer layers, each containing an FFN with intermediate dimension $d_{\\text{ff}}$, we train a lightweight predictor $p_\\theta$ that, for each input token, outputs a binary mask $m \\in \\{0,1\\}^{d_{\\text{ff}}}$ selecting which neurons to activate. The predictor takes as input the hidden state after the attention layer and produces neuron importance scores via a two-layer MLP with Gumbel-sigmoid relaxation for differentiable training.\n\n\\subsection{KL Distillation Loss}\n\nLet $P_{\\text{dense}}$ denote the output distribution of the dense model and $P_{\\text{sparse}}(m)$ the output with mask $m$ applied. We minimize:\n\\begin{equation}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(P_{\\text{dense}} \\| P_{\\text{sparse}}(m_\\theta))\n\\end{equation}\nsubject to a sparsity constraint enforced via Lagrangian relaxation:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\left( \\frac{1}{L \\cdot d_{\\text{ff}}} \\sum_{l,j} m_{l,j} - (1 - s_{\\text{target}}) \\right)^2\n\\end{equation}\nwhere $s_{\\text{target}}$ is the target sparsity ratio and $\\lambda$ is a learnable Lagrange multiplier.\n\n\\subsection{Why KL Produces Different Masks}\n\\label{sec:gradient_analysis}\n\nThe key distinction lies in the gradient structure. For BCE training against magnitude oracles:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = f(s_j, y_j)\n\\end{equation}\nwhere $s_j$ is the score for neuron $j$ and $y_j$ is its oracle label. The gradient for neuron $j$ depends only on $j$ itself (factorized).\n\nFor KL training:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j} = \\frac{\\partial D_{\\text{KL}}}{\\partial \\text{logits}} \\cdot \\frac{\\partial \\text{logits}}{\\partial h} \\cdot \\frac{\\partial h}{\\partial m_j}\n\\end{equation}\nThe gradient for neuron $j$ flows through the full output distribution and couples with all other active neurons via $\\partial h / \\partial m_j$. This coupled gradient allows the predictor to discover joint neuron interaction patterns that factorized BCE gradients cannot capture.\n\nThe causal ablation in Section~\\ref{sec:c1} confirms that this gradient coupling is not the primary \\emph{driver} of KL's advantage; rather, it is the \\emph{mechanism} by which KL discovers better target masks. Once those masks are known, even a BCE predictor trained on them recovers $>$95\\% of the benefit.\n\n\\subsection{Comparison with BCE + Compensation}\n\nFastForward's BCE predictor uses magnitude-based binary labels and adds a compensation MLP (67.2M parameters, ${\\sim}$256MB) to correct residual errors. In our framework, KL distillation produces masks of sufficient quality that compensation becomes redundant: adding compensation to a KL predictor yields PPL 9.18 vs.\\ 9.19 without (Section~\\ref{sec:main_results}).\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Models.} Llama-3.1-8B (primary) and Mistral-7B-v0.3 (cross-architecture).\n\n\\paragraph{Training.} Predictors are trained for 1000 steps on RedPajama with sequence length 2048. KL predictors use Gumbel-sigmoid relaxation with temperature annealing. BCE predictors use magnitude-based binary labels from the dense model.\n\n\\paragraph{Evaluation.} WikiText-2 perplexity (PPL) as primary metric. Downstream: ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (5-shot). Long-context: LongBench English subset. Multi-turn: MT-Bench with GPT-4o judge. RULER synthetic tasks at 4K and 16K lengths.\n\n\\paragraph{Baselines.} TEAL (magnitude + global allocation), WINA (weight-informed), R-Sparse (rank-aware), SPON (static KL bias).\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-condition comparison at 50\\% sparsity on Llama-3.1-8B. PPL is WikiText-2 perplexity (lower is better). Comp.\\ Params indicates compensation network size. KL-only achieves the best PPL without any compensation parameters.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} ($\\downarrow$) & \\textbf{Std} & \\textbf{Seeds} & \\textbf{Comp.\\ Params} \\\\\n\\midrule\nDense & 6.12 & -- & -- & -- \\\\\n\\midrule\nTEAL (global) & 23.31 & -- & -- & 0 \\\\\nWINA (global) & 27.93 & -- & -- & 0 \\\\\nR-Sparse (global) & 151.20 & -- & -- & 0 \\\\\n\\midrule\nBCE-only & 28.16 & 0.21 & 3 & 0 \\\\\nBCE + Comp & 20.80 & 0.70 & 5 & 67.2M \\\\\n\\midrule\n\\textbf{KL-only} & \\textbf{9.19} & \\textbf{0.04} & \\textbf{5} & \\textbf{0} \\\\\nKL + Comp & 9.18 & 0.04 & 3 & 67.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main} presents the core comparison. KL-only achieves PPL 9.19 ($\\pm$0.04 across 5 seeds), outperforming BCE+compensation (PPL 20.80) by a factor of 2.26$\\times$ while requiring zero additional parameters. The consistency across seeds (std 0.04) reflects the well-defined optimization landscape of KL loss: output-distribution supervision provides strong, stable gradients that drive all seeds toward similar mask patterns.\n\nAdding compensation to KL yields negligible improvement (9.18 vs.\\ 9.19), confirming that KL masks are of sufficient quality to make error correction redundant. In contrast, compensation improves BCE from 28.16 to 20.80, a meaningful but insufficient recovery: 67.2M parameters buy only 7.4 PPL points, and the result still trails KL-only by 11.6 PPL.\n\nAmong training-free baselines, TEAL with global allocation (23.31) is strongest but still 2.5$\\times$ worse than KL. R-Sparse performs poorly on SwiGLU architectures (PPL 151.2) because rank-based importance is unreliable when gating mechanisms modulate activation patterns.\n\n\\subsection{Downstream Benchmarks and Pareto Frontier}\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream evaluation across conditions. PPL is WikiText-2. ARC-c, WG, MMLU, GSM8K are accuracy. Best sparse result per column in \\textbf{bold}. KL 30\\% uniform is the recommended operating point.}\n\\label{tab:downstream}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} ($\\downarrow$) & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nDense & 6.12 & 58.3 & 78.1 & 65.3 & 48.8 \\\\\n\\midrule\nKL 30\\% uniform & \\textbf{8.82} & \\textbf{44.3} & \\textbf{69.2} & 38.5 & 7.2 \\\\\nBCE 30\\% forced & 10.00 & 41.0 & 65.2 & 37.0 & 7.2 \\\\\nTEAL 30\\% global & 10.97 & 42.3 & 66.1 & \\textbf{38.6} & \\textbf{7.9} \\\\\n\\midrule\nKL 50\\% global & 11.78 & 34.3 & 63.1 & 28.1 & 2.1 \\\\\nTEAL 50\\% global & 23.31 & 28.4 & 53.0 & 28.3 & 1.1 \\\\\nBCE iso-comp 50\\% & 28.13 & 26.5 & 51.8 & 26.1 & 2.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that KL 30\\% uniform dominates the PPL frontier ($-$19.6\\% vs.\\ TEAL) and provides comparable or better downstream scores. On WinoGrande, KL leads by 3.1 percentage points (pp); on ARC-c, by 2.0pp. MMLU is essentially tied (38.5 vs.\\ 38.6) and GSM8K is within noise (7.2 vs.\\ 7.9). The downstream advantage is concentrated on commonsense and reasoning tasks rather than uniform across benchmarks.\n\nAt 50\\% sparsity, KL maintains a large PPL advantage (11.78 vs.\\ 23.31) while downstream performance collapses toward random for all methods (MMLU ${\\approx}$28\\%, near the 25\\% random baseline). This capacity-cliff pattern motivates the regime analysis in Section~\\ref{sec:regime}.\n\nBCE at the 30\\% operating point (PPL 10.00) falls between TEAL (10.97) and KL (8.82), establishing a three-tier hierarchy: magnitude scoring $<$ learned-factorized $<$ learned-coupled. The gap between BCE and KL narrows from 18.97 at 50\\% to 1.18 at 30\\%, consistent with the principle that lower sparsity reduces the discriminative demand on mask quality.\n\n\\paragraph{Latency.} The predictor adds 3.17ms overhead (2.7\\% of dense latency 119.1ms). Without custom sparse GEMV kernels, there is no wall-clock speedup (actual 0.94$\\times$ at 30\\%). Theoretical FLOPs reduction is 1.36$\\times$ at 30\\% and 2.45$\\times$ at 50\\%. Practical deployment requires sparse kernel support, which we leave to future work.\n\n\\subsection{C1 Causal Ablation: What Drives KL's Advantage?}\n\\label{sec:c1}\n\n\\begin{table}[t]\n\\centering\n\\caption{C1 Causal Ablation at 50\\% sparsity (TEAL uniform protocol). BCE+KL-targets: BCE predictor trained on binary masks extracted from a trained KL predictor. Delta is the gap to the KL reference. Target quality accounts for $>$95\\% of KL's advantage.}\n\\label{tab:c1}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} & \\textbf{$\\Delta$PPL} & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nKL predictor (s42) & 11.96 & -- & 32.6 & 62.4 & 28.0 & 1.9 \\\\\nBCE+KL-targets (s42) & 12.11 & +0.15 & 30.5 & 61.0 & 27.5 & 1.7 \\\\\n\\midrule\nKL predictor (s123) & 11.89 & -- & 37.8 & 62.0 & 27.5 & 2.1 \\\\\nBCE+KL-targets (s123) & 12.17 & +0.28 & 35.0 & 60.5 & 27.0 & 1.9 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{Reference baselines}} \\\\\nBCE magnitude oracle & 27.97 & -- & -- & -- & -- & -- \\\\\nMask divergence (KL vs.\\ magnitude) & \\multicolumn{6}{c}{53\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:c1} presents the headline experiment. A BCE predictor trained on KL-derived oracle masks achieves PPL 12.11--12.17, within 0.15--0.28 of the KL predictor itself (11.89--11.96). Target quality thus accounts for 98.6\\% of KL's advantage on PPL. Standard BCE with magnitude targets yields PPL 27.97, confirming that the choice of targets is what separates the two approaches.\n\nOn downstream tasks, gradient coupling shows a larger residual. ARC-c exhibits a 2.1--2.9pp gap, the largest among all tasks. Multi-step reasoning amplifies the effect of neuron combination quality: even small differences in which borderline neurons are included propagate through reasoning chains. WinoGrande shows a smaller gap (1.4pp), consistent with its reliance on distributed representations rather than specific neuron chains. MMLU and GSM8K are at floor level under 50\\% sparsity, masking any gradient coupling effect.\n\nThe practical implication is unchanged: deploying a BCE predictor trained on KL-derived masks still requires training a KL predictor first. The causal ablation is a scientific finding about \\emph{why KL works}, not a pipeline optimization.\n\n\\subsection{Sparsity Regime Analysis}\n\\label{sec:regime}\n\n\\begin{table}[t]\n\\centering\n\\caption{Six-point sparsity sweep (KL predictors, Llama-3.1-8B). $\\Delta$ is the PPL increment per 5pp sparsity. The 35\\% point has $\\pm$0.2 noise across seeds. Acceleration at 45--50\\% signals the onset of the capacity cliff.}\n\\label{tab:regime}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Sparsity} & \\textbf{PPL} & \\textbf{$\\Delta$/5pp} & \\textbf{Regime} \\\\\n\\midrule\n25\\% & 8.20 & -- & Budget-surplus \\\\\n30\\% & 8.82 & +0.62 & Budget-surplus \\\\\n35\\% & 9.40 & +0.58 & Transition ($\\pm$0.2 noise) \\\\\n40\\% & 10.12 & +0.72 & Budget-constrained \\\\\n45\\% & 10.78 & +0.66 & Budget-constrained \\\\\n50\\% & 11.80 & +1.02 & Capacity-cliff onset \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:regime} shows a six-point PPL curve that is monotonically increasing with an accelerating trend. The increment per 5pp of sparsity grows from ${\\sim}$0.6 in the 25--35\\% range to 1.02 at 45--50\\%, signaling the onset of a capacity cliff. The 35\\% data point exhibits $\\pm$0.2 PPL noise across seeds, reflecting its position at the boundary between regimes. We characterize this as an approximate phase transition rather than a sharp boundary.\n\nThree qualitative regimes emerge from the interaction of sparsity level and allocation strategy:\n\n\\begin{enumerate}\n\\item \\textbf{Budget-surplus ($\\leq$30\\%)}: Every layer has ample neuron budget. Uniform allocation eliminates layer starvation, reducing seed-to-seed MMLU variance from 9.5pp (global) to 1.3pp (uniform). Recommended for deployment.\n\n\\item \\textbf{Budget-constrained (${\\sim}$40\\%)}: Neuron budget becomes tight. Learned per-layer allocation (global top-k) outperforms uniform by 7.4pp on MMLU (38.1\\% vs.\\ 30.7\\%), as the predictor's cross-layer priorities add value under resource pressure.\n\n\\item \\textbf{Capacity-cliff ($\\geq$50\\%)}: Model capacity is the binding constraint. MMLU collapses to ${\\sim}$28\\% ($\\approx$ random for 4-choice) regardless of allocation. PPL remains informative (11.78 for KL), but downstream tasks requiring discrete reasoning chains lose function.\n\\end{enumerate}\n\nThe KL advantage over TEAL grows nonlinearly with sparsity: 2.15 PPL at 30\\%, 11.53 at 50\\%, 82.2 at 70\\%. Learned contextual prediction becomes increasingly valuable as the pruning decision grows more consequential.\n\n\\subsection{Cross-Architecture Validation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture results on Mistral-7B-v0.3 (GQA + sliding window attention). KL/TEAL ratio is the relative PPL improvement of KL over TEAL.}\n\\label{tab:mistral}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Condition} & \\textbf{PPL} & \\textbf{ARC-c} & \\textbf{WG} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nDense & 5.52 & 60.2 & 78.7 & 62.4 & 36.5 \\\\\n\\midrule\nKL 30\\% & 6.77 & -- & -- & -- & -- \\\\\nTEAL 30\\% & 8.38 & -- & -- & -- & -- \\\\\n\\midrule\nKL 50\\% & 8.65 & 31.8 & 62.9 & 23.0 & 2.1 \\\\\nTEAL 50\\% & 18.31 & -- & -- & -- & -- \\\\\n\\midrule\nKL 70\\% & 13.33 & -- & -- & -- & -- \\\\\nTEAL 70\\% & 61.72 & -- & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Sparsity} & \\textbf{Mistral KL/TEAL} & \\textbf{Llama KL/TEAL} \\\\\n\\midrule\n30\\% & 1.24$\\times$ & 1.24$\\times$ \\\\\n50\\% & 2.12$\\times$ & 1.98$\\times$ \\\\\n70\\% & 4.63$\\times$ & 5.59$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mistral} confirms that KL advantage transfers to Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention. The KL/TEAL PPL ratio is remarkably consistent across architectures (1.24$\\times$ at 30\\% on both models), indicating that the advantage stems from SwiGLU architecture properties common to both models rather than model-specific weight distributions. MMLU at 50\\% collapses to 23.0\\% on Mistral (vs.\\ 28.1\\% on Llama), cross-validating the capacity-cliff regime.\n\n\\subsection{Efficiency Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Latency profiling on a single A100 GPU. Without custom sparse kernels, no wall-clock speedup is achieved. Theoretical FLOPs reduction and predictor overhead are reported for transparency.}\n\\label{tab:latency}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Latency (ms)} & \\textbf{FLOPs Reduction} & \\textbf{Overhead} \\\\\n\\midrule\nDense & 119.1 & 1.00$\\times$ & -- \\\\\nKL 30\\% & 126.6 & 1.36$\\times$ (theoretical) & +3.17ms (2.7\\%) \\\\\nKL 50\\% & 126.8 & 2.45$\\times$ (theoretical) & +3.17ms (2.7\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:latency} reports wall-clock latency and theoretical FLOPs savings. The predictor adds 3.17ms (2.7\\%) overhead. Without sparse GEMV kernel support in standard PyTorch, the sparse computation does not translate to wall-clock speedup. With custom kernels (not implemented in this work), the 1.36$\\times$ theoretical FLOPs reduction at 30\\% would more than cover the predictor overhead. We report these numbers for honesty: the quality advantage of KL predictors is fully realized, but practical latency gains require systems-level kernel support.\n\n% ============================================================\n% 5. ANALYSIS\n% ============================================================\n\\section{Analysis}\n\n\\subsection{SPON Is Orthogonal to KL and Too Weak to Complement It}\n\n\\begin{table}[t]\n\\centering\n\\caption{SPON analysis. Left: PPL recovery and dense degradation. Right: logit-space decomposition metrics (50 samples $\\times$ 2048 tokens). SPON correction is near-orthogonal to KL's mask effect with only 15.8\\% relative magnitude.}\n\\label{tab:spon}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nKL pred.\\ PPL (no SPON) & 9.217 \\\\\nKL pred.\\ PPL (with SPON) & 8.991 \\\\\nSPON recovery & 7.3\\% \\\\\nDense PPL (no SPON) & 6.12 \\\\\nDense PPL (with SPON) & 6.18 \\\\\nDense degradation & +0.065 \\\\\n\\midrule\nCosine similarity (SPON vs.\\ KL effect) & 0.196 \\\\\nMagnitude ratio (SPON / KL) & 15.8\\% \\\\\nPer-layer cosine (max) & $\\leq$0.0 \\\\\nLinearity ratio & 0.264 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:spon} quantifies why SPON fails to complement KL. The logit-space cosine similarity between SPON's correction and KL's mask effect is 0.196, indicating near-orthogonal directions. The magnitude ratio of 15.8\\% means SPON's correction is roughly one-sixth the scale of KL's effect. Per-layer analysis shows cosine $\\leq$0 in every layer: SPON and KL target entirely different error components. SPON addresses input-independent systematic bias (which accounts for only 7.3\\% of KL's residual error), while KL's residual is dominated by per-input adaptive errors that static correction cannot reach.\n\n\\subsection{Iso-Compute Ablation}\n\nBCE training extended to 2700 steps (2.71$\\times$ KL FLOPs) yields PPL 28.13 ($\\pm$0.20), virtually unchanged from the standard 1000-step BCE (PPL 28.16). BCE loss saturates at ${\\sim}$500 steps (loss delta 0.006 from step 500 to 2700), confirming that the KL-BCE gap is structural, not a compute deficit. Even with unlimited compute, BCE's factorized gradient cannot learn the neuron interaction patterns that KL captures.\n\n\\subsection{Relaxation Method Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Relaxation method ablation: KL loss with STE vs.\\ Gumbel-sigmoid. STE achieves slightly lower PPL but at 47\\% sparsity (vs.\\ target 50\\%), due to weaker Lagrangian convergence. The gain comes from lower effective sparsity, not better mask quality.}\n\\label{tab:ste}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{PPL} & \\textbf{Std} & \\textbf{Sparsity} \\\\\n\\midrule\nKL + Gumbel & 9.19 & 0.04 & 49.8\\% \\\\\nKL + STE & 8.21 & 0.04 & 47.0\\% \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{BCE reference (any relaxation)}: PPL $\\approx$ 28.16} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ste} confirms that the KL advantage comes from the loss function, not the relaxation method. Both STE and Gumbel-sigmoid with KL loss far outperform BCE (PPL ${\\sim}$8--9 vs.\\ 28.16). STE achieves slightly lower PPL (8.21) but converges to only 47\\% sparsity because its biased gradient estimate weakens Lagrangian convergence. Gumbel-sigmoid provides more reliable sparsity control, which is preferable for deployment with a strict sparsity budget.\n\n% ============================================================\n% 6. ADDITIONAL EVALUATIONS\n% ============================================================\n\\section{Additional Evaluations}\n\n\\subsection{LongBench}\n\n\\begin{table}[t]\n\\centering\n\\caption{LongBench English subset (4K--32K tokens). KL advantage over TEAL is preserved in long-context settings, but absolute retention degrades with context length since the predictor was trained on 2048-token sequences.}\n\\label{tab:longbench}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\textbf{NQA} & \\textbf{Qasper} & \\textbf{HotpotQA} & \\textbf{GovRep} & \\textbf{MultiN} & \\textbf{TriviaQA} \\\\\n\\midrule\nDense & 18.2 & 27.5 & 25.8 & 30.0 & 25.1 & 82.0 \\\\\nKL 30\\% & 12.5 & 19.8 & 15.2 & 22.1 & 17.5 & 56.8 \\\\\nTEAL 30\\% & 10.8 & 17.2 & 13.0 & 19.5 & 14.8 & 50.2 \\\\\nKL 50\\% & 6.2 & 10.8 & 7.5 & 14.2 & 9.1 & 32.5 \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{KL 30\\% avg.\\ retention}: 64\\% \\quad \\emph{TEAL 30\\% avg.\\ retention}: 56\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Context Length} & \\textbf{4K} & \\textbf{8K} & \\textbf{16K} & \\textbf{32K} \\\\\n\\midrule\nKL 30\\% retention & 72\\% & 63\\% & 52\\% & 41\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:longbench} shows that KL maintains its advantage over TEAL on long-context tasks (64\\% vs.\\ 56\\% average retention at 30\\% sparsity). Extraction tasks (TriviaQA) are most robust to sparsity, while generation tasks (NarrativeQA, MultiNews) are most sensitive. Retention degrades with context length (72\\% at 4K to 41\\% at 32K) because the predictor was trained on 2048-token sequences and faces distributional shift at longer contexts. Long-context-aware predictor training is a clear direction for future work.\n\n\\subsection{MT-Bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{MT-Bench scores (GPT-4o judge, 80 multi-turn questions). KL 30\\% retains 81\\% of dense quality. Math and coding categories are most sensitive to sparsity.}\n\\label{tab:mtbench}\n\\small\n\\begin{tabular}{lcccccccc|c}\n\\toprule\n & \\textbf{Writ} & \\textbf{Role} & \\textbf{Reas} & \\textbf{Math} & \\textbf{Code} & \\textbf{Extr} & \\textbf{STEM} & \\textbf{Hum} & \\textbf{Avg} \\\\\n\\midrule\nDense & 7.2 & 7.0 & 5.8 & 4.5 & 5.2 & 7.5 & 6.8 & 6.8 & 6.35 \\\\\nKL 30\\% & 6.0 & 5.8 & 4.2 & 2.8 & 3.5 & 6.5 & 5.5 & 5.9 & 5.15 \\\\\nKL 50\\% & 4.2 & 3.8 & 2.5 & 1.5 & 2.0 & 5.0 & 3.5 & 4.5 & 3.40 \\\\\nTEAL 30\\% & -- & -- & -- & -- & -- & -- & -- & -- & 4.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:mtbench} provides multi-turn evaluation. KL at 30\\% retains 81\\% of dense performance (5.15/6.35) vs.\\ TEAL's 72\\% (4.60/6.35). The advantage is amplified in multi-turn settings because better mask quality reduces error compounding across turns. Math (2.8 vs.\\ 4.5) and coding (3.5 vs.\\ 5.2) show the largest absolute drops, consistent with the finding that precise symbolic reasoning is most vulnerable to neuron pruning.\n\n\\subsection{RULER Synthetic Tasks}\n\n\\begin{table}[t]\n\\centering\n\\caption{RULER accuracy on three synthetic task types at 4K and 16K context lengths. Multi-key and multi-value retrieval degrade disproportionately under sparsity.}\n\\label{tab:ruler}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{4K}} & \\multicolumn{3}{c}{\\textbf{16K}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n & \\textbf{Needle} & \\textbf{M-Key} & \\textbf{M-Val} & \\textbf{Needle} & \\textbf{M-Key} & \\textbf{M-Val} \\\\\n\\midrule\nDense & 95 & 82 & 78 & 88 & 65 & 58 \\\\\nKL 30\\% & 82 & 60 & 55 & 58 & 32 & 28 \\\\\nTEAL 30\\% & 75 & 52 & 48 & -- & -- & -- \\\\\nKL 50\\% & 55 & 30 & 22 & 25 & 12 & 10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ruler} reveals that sparsity disproportionately affects multi-hop retrieval. Needle-in-haystack (single fact) is most robust, while multi-key and multi-value tasks requiring simultaneous tracking of multiple items degrade faster. At 16K with 50\\% sparsity, multi-value accuracy drops to 10\\% (from 78\\% dense at 4K), reflecting the compounding of distributional shift (long context) and capacity reduction (sparsity).\n\n% ============================================================\n% 7. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\paragraph{Scale.} Our primary experiments use 7--8B models. Preliminary 14B results (Qwen-2.5-14B) show that KL's PPL advantage transfers (7.62 vs.\\ TEAL 8.73), but MMLU exhibits a scale-dependent disconnect: KL MMLU 64.5\\% trails TEAL's 71.8\\% despite better PPL. The three-regime framework and allocation recommendations are validated at 8B but require further investigation at larger scales.\n\n\\paragraph{Wall-clock speedup.} Without custom sparse GEMV kernels, the theoretical FLOPs savings do not translate to latency reduction. Practical deployment requires systems-level kernel development.\n\n\\paragraph{Long-context generalization.} Predictors trained on 2048-token sequences show degradation at longer contexts (retention drops from 72\\% at 4K to 41\\% at 32K). Context-length-aware training could mitigate this limitation.\n\n\\paragraph{Single-seed noise.} The 35\\% sparsity data point in the regime analysis has $\\pm$0.2 PPL noise from single-seed measurement. Regime boundaries should be interpreted as approximate.\n\n% ============================================================\n% 8. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe studied KL distillation for SwiGLU sparsity prediction and discovered that KL-trained masks diverge 53\\% from magnitude-based oracles, encoding a fundamentally different neuron importance landscape. A causal ablation confirmed that target quality is the dominant driver ($>$95\\%) of KL's advantage, with gradient coupling contributing a marginal residual most visible on reasoning tasks. This finding shifts the interpretation from ``a better loss function'' to ``a method that discovers hidden neuron importance structure through output-distribution alignment.''\n\nPractically, KL predictors at 30\\% sparsity achieve PPL 8.82 on Llama-3.1-8B (vs.\\ TEAL 10.97) with comparable downstream performance and zero compensation parameters. The three-regime analysis provides deployment guidelines: uniform allocation at $\\leq$30\\%, learned allocation at ${\\sim}$40\\%, and acknowledgment that $\\geq$50\\% sparsity entails fundamental capacity loss. Cross-architecture validation on Mistral-7B confirms the generality of these findings.\n\n\\bibliographystyle{plainnat}\n\\bibliography{refs}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "fa53119f-02cf-4904-b335-7271edafe83b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "ea94a4ba-6896-4857-b3fc-2b2dbfb523b4",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for sparse SwiGLU distillation",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Assistant

_source line 24 · 2026-05-18T18:19:09.038Z_

Now compile it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea94a4ba-6896-4857-b3fc-2b2dbfb523b4",
  "isSidechain": false,
  "requestId": "req_011CbAVgmJ9JheA7LgTkb5ox",
  "type": "assistant",
  "uuid": "6e641fc9-19ec-4a03-9a37-1879b7f2b0af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wxmy5gZtUzGVXwbGUrM2eq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11194,
      "cache_read_input_tokens": 45959,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 45959,
          "cache_creation_input_tokens": 11194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11194
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

_source line 25 · 2026-05-18T18:19:10.116Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012wow9zdZ1S2yp9A3MMKtus`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e641fc9-19ec-4a03-9a37-1879b7f2b0af",
  "isSidechain": false,
  "requestId": "req_011CbAVgmJ9JheA7LgTkb5ox",
  "type": "assistant",
  "uuid": "3cc9d9a0-104c-447d-9595-29a1d6ee301e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wxmy5gZtUzGVXwbGUrM2eq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11194,
      "cache_read_input_tokens": 45959,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 45959,
          "cache_creation_input_tokens": 11194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11194
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

_source line 26 · 2026-05-18T18:19:11.907Z_

<details><summary>↩ Tool result · `toolu_012wow9zdZ1S2yp9A3MMKtus`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
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

Package natbib Warning: Citation `liu2023deja' on page 1 undefined on input lin
e 43.


Package natbib Warning: Citation `song2024prosparse' on page 1 undefined on inp
ut line 43.


Package natbib Warning: Citation `liu2024teal' on page 1 undefined on input lin
e 43.


Package natbib Warning: Citation `huang2024wina' on page 1 undefined on input l
ine 43.


Package natbib Warning: Citation `wang2024fastforward' on page 1 undefined on i
nput line 45.


Package natbib Warning: Citation `huang2024spon' on page 1 undefined on input l
ine 45.


LaTeX Warning: Reference `sec:c1' on page 1 undefined on input line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `liu2023deja' on page 2 undefined on input lin
e 65.


Package natbib Warning: Citation `liu2024teal' on page 2 undefined on input lin
e 65.


Package natbib Warning: Citation `huang2024wina' on page 2 undefined on input l
ine 65.


Package natbib Warning: Citation `zhang2024rsparse' on page 2 undefined on inpu
t line 65.


Package natbib Warning: Citation `wang2024fastforward' on page 2 undefined on i
nput line 68.


Package natbib Warning: Citation `song2024powerinfer' on page 2 undefined on in
put line 68.


Package natbib Warning: Citation `huang2024spon' on page 2 undefined on input l
ine 71.


Package natbib Warning: Citation `he2024shadowllm' on page 2 undefined on input
 line 71.

[2]

LaTeX Warning: Reference `sec:c1' on page 3 undefined on input line 110.


LaTeX Warning: Reference `sec:main_results' on page 3 undefined on input line 1
14.

[3]

LaTeX Warning: Reference `tab:main' on page 4 undefined on input line 158.


LaTeX Warning: Reference `tab:downstream' on page 4 undefined on input line 188
.

[4]

LaTeX Warning: Reference `sec:regime' on page 5 undefined on input line 190.


LaTeX Warning: Reference `tab:c1' on page 5 undefined on input line 221.


LaTeX Warning: Reference `tab:regime' on page 5 undefined on input line 249.

[5]

LaTeX Warning: Reference `tab:mistral' on page 6 undefined on input line 299.

[6]

LaTeX Warning: Reference `tab:latency' on page 7 undefined on input line 319.


LaTeX Warning: Reference `tab:spon' on page 7 undefined on input line 352.

[7]

LaTeX Warning: Reference `tab:ste' on page 8 undefined on input line 377.


LaTeX Warning: Reference `tab:longbench' on page 8 undefined on input line 414.


[8]

LaTeX Warning: Reference `tab:mtbench' on page 9 undefined on input line 435.


LaTeX Warning: Reference `tab:ruler' on page 9 undefined on input line 458.

[9]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1
200.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf
 Ok [100] [109] [98] [99] [108])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf
 Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]
[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]
[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]
[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]
[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]
[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]
[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf
 Ok [185] [178] [179] [170] [186])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf
 Ok [188] [189] [190]) ) ) )
(some charht values had to be adjusted by as much as 0.06952pt)
Font metrics written on tcrm1095.tfm.
Output written on tcrm1095.600gf (128 characters, 25592 bytes).
Transcript written on tcrm1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcr
m1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
cti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour
/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>
Output written on paper.pdf (10 pages, 218586 bytes).
Transcript written on paper.log.
Package natbib Warning: Citation `he2024shadowllm' on page 2 undefined on input
 line 71.

[2] [3] [4] [5] [6] [7] [8] [9]
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour
/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfo
ur/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/lj
four/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/
ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p
k/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts
/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fon
ts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/f
onts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var
/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-v
ar/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>
Output written on paper.pdf (10 pages, 221551 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cc9d9a0-104c-447d-9595-29a1d6ee301e",
  "isSidechain": false,
  "promptId": "39a420d6-578d-4499-8d17-88d1e455065e",
  "type": "user",
  "uuid": "d18dd854-d60d-4305-b788-187bd2db144d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `liu2023deja' on page 1 undefined on input lin\ne 43.\n\n\nPackage natbib Warning: Citation `song2024prosparse' on page 1 undefined on inp\nut line 43.\n\n\nPackage natbib Warning: Citation `liu2024teal' on page 1 undefined on input lin\ne 43.\n\n\nPackage natbib Warning: Citation `huang2024wina' on page 1 undefined on input l\nine 43.\n\n\nPackage natbib Warning: Citation `wang2024fastforward' on page 1 undefined on i\nnput line 45.\n\n\nPackage natbib Warning: Citation `huang2024spon' on page 1 undefined on input l\nine 45.\n\n\nLaTeX Warning: Reference `sec:c1' on page 1 undefined on input line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `liu2023deja' on page 2 undefined on input lin\ne 65.\n\n\nPackage natbib Warning: Citation `liu2024teal' on page 2 undefined on input lin\ne 65.\n\n\nPackage natbib Warning: Citation `huang2024wina' on page 2 undefined on input l\nine 65.\n\n\nPackage natbib Warning: Citation `zhang2024rsparse' on page 2 undefined on inpu\nt line 65.\n\n\nPackage natbib Warning: Citation `wang2024fastforward' on page 2 undefined on i\nnput line 68.\n\n\nPackage natbib Warning: Citation `song2024powerinfer' on page 2 undefined on in\nput line 68.\n\n\nPackage natbib Warning: Citation `huang2024spon' on page 2 undefined on input l\nine 71.\n\n\nPackage natbib Warning: Citation `he2024shadowllm' on page 2 undefined on input\n line 71.\n\n[2]\n\nLaTeX Warning: Reference `sec:c1' on page 3 undefined on input line 110.\n\n\nLaTeX Warning: Reference `sec:main_results' on page 3 undefined on input line 1\n14.\n\n[3]\n\nLaTeX Warning: Reference `tab:main' on page 4 undefined on input line 158.\n\n\nLaTeX Warning: Reference `tab:downstream' on page 4 undefined on input line 188\n.\n\n[4]\n\nLaTeX Warning: Reference `sec:regime' on page 5 undefined on input line 190.\n\n\nLaTeX Warning: Reference `tab:c1' on page 5 undefined on input line 221.\n\n\nLaTeX Warning: Reference `tab:regime' on page 5 undefined on input line 249.\n\n[5]\n\nLaTeX Warning: Reference `tab:mistral' on page 6 undefined on input line 299.\n\n[6]\n\nLaTeX Warning: Reference `tab:latency' on page 7 undefined on input line 319.\n\n\nLaTeX Warning: Reference `tab:spon' on page 7 undefined on input line 352.\n\n[7]\n\nLaTeX Warning: Reference `tab:ste' on page 8 undefined on input line 377.\n\n\nLaTeX Warning: Reference `tab:longbench' on page 8 undefined on input line 414.\n\n\n[8]\n\nLaTeX Warning: Reference `tab:mtbench' on page 9 undefined on input line 435.\n\n\nLaTeX Warning: Reference `tab:ruler' on page 9 undefined on input line 458.\n\n[9]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0600.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm080\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1\n200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 tcrm1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input tcrm1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/tcrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymb.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [27] [29])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txgen.mf\n Ok [100] [109] [98] [99] [108])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txsymbol.mf\n Ok [13] [18] [21] [22] [23] [24] [25] [26] [28] [31] [32] [36] [39] [44]\n[45] [46] [42] [47] [60] [61] [62] [77] [79] [87] [110] [91] [93] [94] [95]\n[96] [126] [127] [128] [129] [130] [131] [132] [133] [134] [135] [136] [137]\n[138] [139] [140] [141] [142] [143] [144] [145] [146] [147] [148] [149]\n[150] [151] [152] [153] [154] [155] [156] [157] [158] [159] [160] [161]\n[162] [163] [164] [165] [166] [167] [168] [169] [171] [172] [173] [174]\n[175] [177] [176] [180] [181] [182] [183] [184] [187] [191] [214] [246])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txromod.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrsuper.mf\n Ok [185] [178] [179] [170] [186])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txrfract.mf\n Ok [188] [189] [190]) ) ) )\n(some charht values had to be adjusted by as much as 0.06952pt)\nFont metrics written on tcrm1095.tfm.\nOutput written on tcrm1095.600gf (128 characters, 25592 bytes).\nTranscript written on tcrm1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcr\nm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour\n/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>\nOutput written on paper.pdf (10 pages, 218586 bytes).\nTranscript written on paper.log.\nPackage natbib Warning: Citation `he2024shadowllm' on page 2 undefined on input\n line 71.\n\n[2] [3] [4] [5] [6] [7] [8] [9]\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecrm0600.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour\n/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfo\nur/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/lj\nfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/\nljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p\nk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts\n/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fon\nts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/f\nonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var\n/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-v\nar/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>\nOutput written on paper.pdf (10 pages, 221551 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3cc9d9a0-104c-447d-9595-29a1d6ee301e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-18T18:19:21.705Z_

PDF 编译成功，10 页，无错误。输出位于 `artifacts/dream_reports/dream_20260518T173518/median/paper.pdf`。

论文包含：Abstract, Introduction, Related Work, Method (含梯度分析), Experiments (4-condition ablation Table 1, downstream Table 2, C1 causal ablation Table 3, 6-point regime Table 4, Mistral cross-arch Table 5, latency Table 6), Analysis (SPON/iso-compute/STE), Additional Evaluations (LongBench/MT-Bench/RULER), Limitations, Conclusion。所有定量 claim 均来自 experiment_data.json，narrative 按 median tier calibration 处理（>95% not sole driver, approximate phase transition, honest Pareto reporting）。引用未定义（无 .bib 文件）但不影响审稿可读性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d18dd854-d60d-4305-b788-187bd2db144d",
  "isSidechain": false,
  "requestId": "req_011CbAVhCbuSu99EW9ALSaEQ",
  "type": "assistant",
  "uuid": "6317b46e-4487-4881-a379-8d6f66d601a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260518T173518/median",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSGbJT7AMETdK8wnew2fxu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5784,
      "cache_read_input_tokens": 57153,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 57153,
          "cache_creation_input_tokens": 5784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5784
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T173518 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_…",
  "leafUuid": "6317b46e-4487-4881-a379-8d6f66d601a3",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier research paper for sparse SwiGLU distillation",
  "sessionId": "d62d6b41-b2b1-4bd2-b0b5-6f9443290165"
}
```

---
