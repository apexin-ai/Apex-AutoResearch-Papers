# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/eab7f882-a47b-4142-9d99-cf7021352d31.jsonl`
- **Structured JSON:** [`cca212935cb0a76dc153.json`](../../sessions/cc/cca212935cb0a76dc153.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T22:42:01.707Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T22:42:01.707Z",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Depth discriminability holds within-generator (F1 0.82) but cross-generator generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated on out-of-family holdouts. Dual dynamics is real but reference-model-modulated: entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the paper to present the H1/H2 split as 'reference-model-modulated dual dynamics' rather than a universal law. Length confound is partial — surface feature F1 drops ~0.05 after length control, but residual signal confirms depth is not reducible to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on scale-robust features. Downstream filtering offers complementary signal but CIs overlap with best binary baseline on some metrics. Paper reframed: 'depth estimation is feasible and useful, with initial evidence for dual dynamics' rather than 'dual dynamics as general principle.' Still viable for AAAI/EMNLP as empirical contribution with honest limitations.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-14T22:42:01.710Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T22:42:01.710Z",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-14T22:42:01.726Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Depth discriminability holds within-generator (F1 0.82) but cross-generator generalization is moderate (LOGO F1 ~0.64), with performance drops concentrated on out-of-family holdouts. Dual dynamics is real but reference-model-modulated: entropy_mean drift attenuates to |ρ|~0.4 with non-Pythia references, requiring the paper to present the H1/H2 split as 'reference-model-modulated dual dynamics' rather than a universal law. Length confound is partial — surface feature F1 drops ~0.05 after length control, but residual signal confirms depth is not reducible to length. 7B+ signal weakens (F1 ~0.57) but persists, motivating future work on scale-robust features. Downstream filtering offers complementary signal but CIs overlap with best binary baseline on some metrics. Paper reframed: 'depth estimation is feasible and useful, with initial evidence for dual dynamics' rather than 'dual dynamics as general principle.' Still viable for AAAI/EMNLP as empirical contribution with honest limitations.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "db0b056b-68c9-48a5-9a53-2f5b3ea97c3e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T22:42:01.725Z_

```json
{
  "parentUuid": "db0b056b-68c9-48a5-9a53-2f5b3ea97c3e",
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
  "uuid": "fba05c59-58b3-4246-98b5-5dbbcefe7c50",
  "timestamp": "2026-05-14T22:42:01.725Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T22:42:01.725Z_

```json
{
  "parentUuid": "fba05c59-58b3-4246-98b5-5dbbcefe7c50",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2859dc28-83c7-4a62-983d-2ec777e059da",
  "timestamp": "2026-05-14T22:42:01.725Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
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
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Assistant

_source line 7 · 2026-05-14T22:42:04.288Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2859dc28-83c7-4a62-983d-2ec777e059da",
  "isSidechain": false,
  "requestId": "req_011Cb3GVzz4HdM9r3fYpPjBP",
  "type": "assistant",
  "uuid": "f6350859-8fde-43ca-a1d2-7ada16452768",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jEHWaDY3fGqX9qwnCvp6Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11293
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

_source line 8 · 2026-05-14T22:42:05.378Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MiMrCNSMsuYpV4kDyps8GG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6350859-8fde-43ca-a1d2-7ada16452768",
  "isSidechain": false,
  "requestId": "req_011Cb3GVzz4HdM9r3fYpPjBP",
  "type": "assistant",
  "uuid": "b67790c2-fc31-4130-a695-85a30a1b4f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jEHWaDY3fGqX9qwnCvp6Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11293
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

_source line 9 · 2026-05-14T22:42:05.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_012xQJyySAXxqEhFyncKoygG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b67790c2-fc31-4130-a695-85a30a1b4f8c",
  "isSidechain": false,
  "requestId": "req_011Cb3GVzz4HdM9r3fYpPjBP",
  "type": "assistant",
  "uuid": "8c2584c4-d200-4fac-b09f-ec12b9fc049b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jEHWaDY3fGqX9qwnCvp6Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11293,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11293,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11293
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

_source line 10 · 2026-05-14T22:42:05.448Z_

<details><summary>↩ Tool result · `toolu_012xQJyySAXxqEhFyncKoygG`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- Primary: AAAI 2027 (deadline: August 2, 2026)
5	- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).
14	
15	**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.
16	
17	**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.
18	
19	## Story Spine
20	
21	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).
22	
23	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.
24	
25	**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that "reference-model features = robust, surface features = fragile." The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.
26	
27	**Headline result template**: "On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines."
28	
29	## Anticipated Reviewer Concerns
30	
31	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are "better" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: "fingerprint" in the paper refers to the full feature vector's combination, not just reference-model features.
32	
33	**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.
34	
35	**RC2 — "Does this generalize beyond Pythia?"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).
36	
37	**RC3 — "Is 3-class sufficient? Why not finer-grained?"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.
38	
39	**RC4 — "How realistic are single-model chains?"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).
40	
41	**RC5 — "What about human editing / post-processing?"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).
42	
43	**RC6 — "Ecological validity — continuation vs real web content"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).
44	
45	**RC8 — "Aren't these just OOD detection features?"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.
46	
47	**RC9 — "Only ≤2.8B generators — does this transfer to frontier scale?"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.
48	
49	**RC10 — "Text length confound"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.
50	
51	**RC11 — "Downstream utility — single run, no CIs"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).
52	
53	## Contribution Positioning (Dream D006 insight)
54	The contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:
55	1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection
56	2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary
57	3. **Practical application**: Risk-stratified data curation outperforming binary filtering
58	
59	Do NOT overclaim "distributional fingerprinting" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.
60	
61	Related work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).
62	
63	## Venue Fit
64	- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.
65	- EMNLP 2026: Excellent fit — directly addresses special theme "New Missions for NLP Research" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c2584c4-d200-4fac-b09f-ec12b9fc049b",
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "825092e1-9eb0-4c36-9cb8-8a957dd25e6c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- Primary: AAAI 2027 (deadline: August 2, 2026)\n- Stretch: EMNLP 2026 ARR (deadline: May 25, 2026) — minimal scope RQ1+RQ4\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **dual depth dynamics** that cross-cuts the surface/reference distinction: **level/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth (H₂), while **distributional shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁). Notably, entropy_mean is a reference-model feature that drifts (ρ=-0.68), showing the H₁/H₂ split is about what the feature measures (central tendency vs shape), not where it comes from (surface vs reference). This dual pattern creates a complementary feature space: drifting features provide ordinal depth signal, while stable shape features provide noise-robust class boundaries. The combination significantly outperforms either alone (macro-F1 0.82 vs 0.76/0.72).\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: Distributional features computed under a held-out reference model can classify text generation depth (gen-0 / gen-1 / gen-2+) with macro-F1 significantly above chance, generalizing across unseen generators (leave-one-generator-out evaluation).\n\n**Claim 2 — Dual Dynamics (Level vs Shape)**: Depth-dependent features split into two families by **what they measure**, not by their source (surface vs reference): (a) **level/diversity features** (entropy_mean, TTR, hapax_ratio) drift monotonically with depth (H₂ — vocabulary impoverishment + entropy compression); (b) **shape features** (entropy_std, entropy_max, tail_decay) remain near-stationary (H₁ — distributional shape is robust to recursive generation). This split cross-cuts the surface/reference boundary (entropy_mean is reference-derived but drifts). Full feature set (0.82) significantly outperforms surface-only (0.76) and reference-only (0.72) — the two dynamics are complementary for classification.\n\n**Claim 3 — Downstream Utility**: Predicted generation depth correlates with fine-tuning quality degradation (Spearman ρ), and depth-aware filtering outperforms binary detection baselines (FastDetectGPT, LD-Score threshold) for preserving downstream model quality.\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth. Current detection methods offer only binary real-vs-synthetic classification, forcing all-or-nothing filtering: discard everything flagged as synthetic (losing useful gen-1 content) or keep everything (admitting high-risk deep-generation text with compounding distributional drift).\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, SynthID-Text, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) proves paraphrasing chains converge to 2-period cycles, bounding depth signal to ~3 classes — but this result depends on the semantic-preservation constraint of paraphrasing. No existing work attempts generation depth estimation.\n\n**Our framing**: We characterize distributional drift in recursive non-paraphrastic LLM generation, revealing **dual dynamics**: level/diversity features (including reference-model entropy_mean) drift monotonically with depth (H₂), while distributional shape features (entropy variance, tail decay) remain near-stationary (H₁). This split is about **what the feature measures** (central tendency vs shape), not where it comes from — overturning the naive expectation that \"reference-model features = robust, surface features = fragile.\" The dual pattern has practical value: drifting features provide ordinal depth signal, stable shape features provide noise-robust decision boundaries, and their combination yields the best depth estimation for risk-stratified data curation.\n\n**Headline result template**: \"On multi-generator continuation chains across 4 domains, our distributional fingerprint features achieve macro-F1 of X for 3-class depth estimation (gen-0/gen-1/gen-2+), with leave-one-generator-out generalization at Y. Depth-aware filtering preserves Z% more downstream task performance compared to binary filtering baselines.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.76 macro-F1, but full features achieve 0.82 (p<0.001). We don't claim reference features are \"better\" — we show they capture a **different, complementary** signal (stationary distributional shape vs drifting level/diversity). The dual dynamics finding is itself a scientific contribution. Note: \"fingerprint\" in the paper refers to the full feature vector's combination, not just reference-model features.\n\n**RC7 — Pre-registered prediction (LD-Score)**: LD-Score (character-distribution signature) measures character-level distributional properties. We predict it is a **level feature** (sensitive to vocabulary/character frequency shifts) and should exhibit **H₂ drift** with depth. This prediction is registered before plan_011 execution as an out-of-sample test of the level/shape framework.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: MVP used same-family models (Pythia-2.8B generator + Pythia-410M reference). → Cross-family experiments: Qwen/OLMo generators + non-Pythia reference models (RQ1 cross-generator evaluation).\n\n**RC3 — \"Is 3-class sufficient? Why not finer-grained?\"**: Attractor theory bounds paraphrasing to ~3 classes. → Secondary analysis: finer-grained ordinal classification (gen-0 through gen-4) on non-paraphrastic chains to test if more depth signal exists.\n\n**RC4 — \"How realistic are single-model chains?\"**: Real web contamination involves diverse generators. → Cross-model chains (different generator per depth step) as primary evaluation setting (RQ3).\n\n**RC5 — \"What about human editing / post-processing?\"**: Real-world synthetic text is often edited. → Robustness test with simulated human edits (random word replacement as lower-bound + LLM-simulated editing).\n\n**RC6 — \"Ecological validity — continuation vs real web content\"**: Lab-constructed chains may not match wild distribution. → Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, inspired rewriting).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Reference-model entropy statistics are functionally NLL-based OOD scores (same signal backbone as DetectGPT/GLTR/Binoculars). Our contribution is NOT the features themselves but: (a) the problem formulation (ordinal depth estimation, not binary detection), (b) the empirical discovery that these features exhibit dual dynamics (level drift vs shape stationarity) under recursive generation, and (c) the practical application to risk-stratified data curation. Paper must explicitly connect to OOD detection + perplexity-based detection literature and position the contribution as primarily empirical/conceptual rather than methodological.\n\n**RC9 — \"Only ≤2.8B generators — does this transfer to frontier scale?\"**: All 5 current generators ≤2.8B. Frontier models (7B+) produce more fluent text that may compress depth signal. → Add at least one 7B+ generator (plan_014). If depth signal significantly weaker at scale → honest limitation with analysis of why; if comparable → strong generalization evidence.\n\n**RC10 — \"Text length confound\"**: Hapax ratio and TTR are mechanically length-dependent. If generation chains produce texts of systematically different lengths, surface features may track length artifacts rather than distributional drift. → Length distribution analysis + length-normalized features + length-matched comparison (plan_013). Critical confound control.\n\n**RC11 — \"Downstream utility — single run, no CIs\"**: Depth-aware filtering advantage must be validated with multiple seeds + bootstrap CIs + sample-count-matched comparison (to control for data size confound). Must use non-Pythia model for downstream fine-tuning (OLMo-1B) to avoid reference model circularity (Pythia-410M as both feature extractor and eval model).\n\n## Contribution Positioning (Dream D006 insight)\nThe contribution is **primarily empirical and conceptual**, not methodological. The features (NLL summary statistics) and classifier (XGBoost) are standard — the novelty lies in:\n1. **Problem formulation**: Ordinal depth estimation as a new task beyond binary detection\n2. **Empirical discovery**: Dual dynamics (level/diversity drift vs shape stationarity) cross-cutting surface/reference boundary\n3. **Practical application**: Risk-stratified data curation outperforming binary filtering\n\nDo NOT overclaim \"distributional fingerprinting\" as a new method. Position the paper as empirical science with a novel task formulation and a surprising empirical finding. The H1/H2 framework is an empirical validation extending attractor cycle theory to non-paraphrastic chains, not a major theoretical contribution.\n\nRelated work must expand to 30+ references covering: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory (Alemohammad et al., Dohmatob et al., Gerstgrasser et al., Guo et al.), OOD detection (Hendrycks & Gimpel), data quality scoring (DSIR, QuRating, CCNet), watermarking (Kirchenbauer et al.), vocabulary diversity (Guo et al. 2024, Padmakumar & He 2024, Holtzman et al. 2020).\n\n## Venue Fit\n- AAAI 2027: Fit as empirical + conceptual contribution — novel task formulation (depth estimation) + surprising empirical finding (dual dynamics) + practical application (data curation). Must position as empirical science, not methodology paper.\n- EMNLP 2026: Excellent fit — directly addresses special theme \"New Missions for NLP Research\" (data contamination, synthetic data feedback loops, data governance). NLP-native venue for text-focused work. Empirical/conceptual contributions better received here than AAAI.\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  },
  "sourceToolAssistantUUID": "8c2584c4-d200-4fac-b09f-ec12b9fc049b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "825092e1-9eb0-4c36-9cb8-8a957dd25e6c",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Tool result

_source line 13 · 2026-05-14T22:42:05.669Z_

<details><summary>↩ Tool result · `toolu_01MiMrCNSMsuYpV4kDyps8GG`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "Feature ablation (full / surface-only / reference-only) + H1/H2 trend analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity pre-validation for Claim 3.\n",
5	    "results": {
6	      "full_macro_f1": 0.82,
7	      "surface_only_f1": 0.76,
8	      "reference_only_f1": 0.72,
9	      "full_vs_surface_gap": 0.06,
10	      "full_vs_reference_gap": 0.1,
11	      "bootstrap_ci_full": "[0.804, 0.836]",
12	      "bootstrap_ci_surface": "[0.747, 0.774]",
13	      "bootstrap_ci_reference": "[0.706, 0.733]",
14	      "h2_entropy_mean_slope": -0.148,
15	      "h2_entropy_mean_r2": 0.93,
16	      "h2_ttr_slope": -0.071,
17	      "h2_ttr_r2": 0.87,
18	      "h2_hapax_ratio_slope": -0.054,
19	      "h2_hapax_ratio_r2": 0.81,
20	      "h1_entropy_std_slope": 0.003,
21	      "h1_entropy_std_r2": 0.02,
22	      "h1_entropy_max_slope": -0.009,
23	      "h1_entropy_max_r2": 0.04,
24	      "h1_tail_decay_slope": 0.005,
25	      "h1_tail_decay_r2": 0.03,
26	      "h1_entropy_min_slope": -0.012,
27	      "h1_entropy_min_r2": 0.06,
28	      "median_ppl_by_depth": [
29	        13.5,
30	        4.96,
31	        3.0,
32	        2.07,
33	        1.72
34	      ],
35	      "ppl_kruskal_wallis_p": "<0.001"
36	    },
37	    "tables": [
38	      {
39	        "name": "Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)",
40	        "columns": [
41	          "feature_set",
42	          "macro_f1",
43	          "95% CI",
44	          "gen0_f1",
45	          "gen1_f1",
46	          "gen2plus_f1"
47	        ],
48	        "rows": [
49	          [
50	            "Full (7 features)",
51	            0.82,
52	            "[0.804, 0.836]",
53	            0.94,
54	            0.77,
55	            0.79
56	          ],
57	          [
58	            "Surface only (TTR + hapax)",
59	            0.76,
60	            "[0.747, 0.774]",
61	            0.91,
62	            0.7,
63	            0.72
64	          ],
65	          [
66	            "Reference only (5 NLL)",
67	            0.72,
68	            "[0.706, 0.733]",
69	            0.88,
70	            0.65,
71	            0.67
72	          ],
73	          [
74	            "Chance baseline",
75	            0.33,
76	            "—",
77	            0.33,
78	            0.33,
79	            0.33
80	          ]
81	        ]
82	      },
83	      {
84	        "name": "Table 2: H1/H2 Trend Regression per Feature",
85	        "columns": [
86	          "feature",
87	          "slope",
88	          "R²",
89	          "p_value",
90	          "classification"
91	        ],
92	        "rows": [
93	          [
94	            "entropy_mean",
95	            -0.148,
96	            0.93,
97	            "<0.001",
98	            "H2 (drift)"
99	          ],
100	          [
101	            "TTR",
102	            -0.071,
103	            0.87,
104	            "<0.001",
105	            "H2 (drift)"
106	          ],
107	          [
108	            "hapax_ratio",
109	            -0.054,
110	            0.81,
111	            "<0.001",
112	            "H2 (drift)"
113	          ],
114	          [
115	            "entropy_std",
116	            0.003,
117	            0.02,
118	            0.41,
119	            "H1 (stationary)"
120	          ],
121	          [
122	            "entropy_max",
123	            -0.009,
124	            0.04,
125	            0.28,
126	            "H1 (stationary)"
127	          ],
128	          [
129	            "tail_decay",
130	            0.005,
131	            0.03,
132	            0.33,
133	            "H1 (stationary)"
134	          ],
135	          [
136	            "entropy_min",
137	            -0.012,
138	            0.06,
139	            0.19,
140	            "H1 (stationary)"
141	          ]
142	        ]
143	      }
144	    ],
145	    "figures": [],
146	    "analysis": "Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface gap is statistically significant (bootstrap CIs non-overlapping), establishing that reference features capture complementary signal. However, this is within-generator with same-family reference model — the gap's robustness must be tested cross-generator (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates Claim 3's premise: depth correlates with distributional properties detectable by a reference model.\n\n\nWithin-generator results remain strong because Pythia-410M reference model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL feature sensitivity. The 0.06 full-surface gap confirms reference features add independent value — entropy_mean captures distributional compression that surface statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive generation compounds vocabulary impoverishment and entropy compression — each step feeds an increasingly constrained output distribution back as input. H1 features (shape statistics like entropy_std, tail_decay) remain stable because distributional shape is determined by the generator's softmax geometry, not the input content — recursive generation shifts the location (mean) of the NLL distribution but not its spread or tail behavior. Perplexity shows steep monotonic decline because deeper generations become more predictable to the reference model as they converge toward the generator's mode.\n"
147	  },
148	  {
149	    "name": "cross_generator_evaluation",
150	    "description": "5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out CV.\n",
151	    "results": {
152	      "logo_mean_macro_f1": 0.64,
153	      "logo_holdout_pythia28b_f1": 0.71,
154	      "logo_holdout_pythia1b_f1": 0.72,
155	      "logo_holdout_olmo2_f1": 0.6,
156	      "logo_holdout_qwen17b_f1": 0.62,
157	      "logo_holdout_qwen06b_f1": 0.59,
158	      "lofo_holdout_pythia_family_f1": 0.58,
159	      "lofo_holdout_olmo_family_f1": 0.61,
160	      "lofo_holdout_qwen_family_f1": 0.59,
161	      "lofo_mean_f1": 0.593,
162	      "within_generator_pooled_5fold_f1": 0.78,
163	      "logo_full_feature_f1": 0.64,
164	      "logo_surface_only_f1": 0.61,
165	      "logo_reference_only_f1": 0.58,
166	      "logo_full_vs_surface_gap": 0.03,
167	      "logo_full_vs_reference_gap": 0.06,
168	      "total_chains_generated": 23847,
169	      "total_chains_after_attrition": 21503
170	    },
171	    "tables": [
172	      {
173	        "name": "Table 3: Leave-One-Generator-Out Results (Full Features)",
174	        "columns": [
175	          "held_out_generator",
176	          "family",
177	          "macro_f1",
178	          "gen0_f1",
179	          "gen1_f1",
180	          "gen2plus_f1"
181	        ],
182	        "rows": [
183	          [
184	            "Pythia-2.8B",
185	            "Pythia",
186	            0.71,
187	            0.87,
188	            0.64,
189	            0.66
190	          ],
191	          [
192	            "Pythia-1B",
193	            "Pythia",
194	            0.72,
195	            0.88,
196	            0.66,
197	            0.67
198	          ],
199	          [
200	            "OLMo-2-1B",
201	            "OLMo",
202	            0.6,
203	            0.79,
204	            0.51,
205	            0.53
206	          ],
207	          [
208	            "Qwen3-1.7B",
209	            "Qwen",
210	            0.62,
211	            0.82,
212	            0.53,
213	            0.55
214	          ],
215	          [
216	            "Qwen3-0.6B",
217	            "Qwen",
218	            0.59,
219	            0.78,
220	            0.5,
221	            0.51
222	          ],
223	          [
224	            "Mean LOGO",
225	            "—",
226	            0.64,
227	            0.83,
228	            0.57,
229	            0.58
230	          ]
231	        ]
232	      },
233	      {
234	        "name": "Table 4: Leave-One-Family-Out Results",
235	        "columns": [
236	          "held_out_family",
237	          "generators_in_family",
238	          "macro_f1",
239	          "95% CI"
240	        ],
241	        "rows": [
242	          [
243	            "Pythia",
244	            "2.8B + 1B",
245	            0.58,
246	            "[0.55, 0.61]"
247	          ],
248	          [
249	            "OLMo",
250	            "OLMo-2-1B",
251	            0.61,
252	            "[0.57, 0.64]"
253	          ],
254	          [
255	            "Qwen",
256	            "1.7B + 0.6B",
257	            0.59,
258	            "[0.56, 0.62]"
259	          ]
260	        ]
261	      },
262	      {
263	        "name": "Table 5: Feature Ablation in Cross-Generator Setting (LOGO)",
264	        "columns": [
265	          "feature_set",
266	          "logo_macro_f1",
267	          "gap_vs_full"
268	        ],
269	        "rows": [
270	          [
271	            "Full",
272	            0.64,
273	            "—"
274	          ],
275	          [
276	            "Surface only",
277	            0.61,
278	            -0.03
279	          ],
280	          [
281	            "Reference only",
282	            0.58,
283	            -0.06
284	          ]
285	        ]
286	      }
287	    ],
288	    "figures": [],
289	    "analysis": "LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate cross-generator generalization. The within-family vs cross-family gap (~0.12) reveals that distributional features partially encode generator identity, not just depth. This constrains Claim 1 to 'depth discriminability generalizes within model family; cross-family generalization is moderate and requires further work.' The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference features lose their relative advantage in the cross-generator setting — likely because the Pythia-410M reference model is better calibrated for Pythia-family generators. This motivates plan_003 to test non-Pythia reference models.\n\n\nCross-generator F1 drops from 0.82 (within-generator) to 0.64 (LOGO) because each generator family imprints family-specific distributional signatures beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining data overlap) — when one is held out, the other provides a close proxy in the training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent genuinely out-of-distribution generator families with different tokenizers and pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because reference features (computed with Pythia-410M) are partially Pythia-biased: they extract richer signal from Pythia-generated text than from OLMo/Qwen-generated text, eroding their cross-family advantage. Leave-one-family-out results (mean 0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators remaining in training. The within-generator pooled F1 (0.78) is lower than MVP's 0.82 because pooling heterogeneous generators introduces inter-generator variance that the classifier must absorb.\n"
290	  },
291	  {
292	    "name": "cross_family_reference_model",
293	    "description": "Recompute NLL features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and shape feature H1 stationarity persist. Key falsification test for Claim 2.\n",
294	    "results": {
295	      "pythia410m_ref_entropy_mean_rho": -0.68,
296	      "olmo2_ref_entropy_mean_rho": -0.42,
297	      "qwen06b_ref_entropy_mean_rho": -0.36,
298	      "pythia410m_ref_full_f1": 0.82,
299	      "olmo2_ref_full_f1": 0.78,
300	      "qwen06b_ref_full_f1": 0.76,
301	      "olmo2_ref_shape_max_abs_rho": 0.11,
302	      "qwen06b_ref_shape_max_abs_rho": 0.09,
303	      "pythia410m_ref_shape_max_abs_rho": 0.08,
304	      "olmo2_ref_entropy_std_rho": 0.06,
305	      "olmo2_ref_tail_decay_rho": -0.11,
306	      "qwen06b_ref_entropy_std_rho": -0.04,
307	      "qwen06b_ref_tail_decay_rho": 0.09,
308	      "cross_ref_logo_f1_olmo_ref": 0.61,
309	      "cross_ref_logo_f1_qwen_ref": 0.58
310	    },
311	    "tables": [
312	      {
313	        "name": "Table 6: Entropy_mean Drift (ρ) by Reference Model",
314	        "columns": [
315	          "reference_model",
316	          "entropy_mean_rho",
317	          "p-value",
318	          "classification_full_f1"
319	        ],
320	        "rows": [
321	          [
322	            "Pythia-410M",
323	            -0.68,
324	            "<0.001",
325	            0.82
326	          ],
327	          [
328	            "OLMo-2-1B",
329	            -0.42,
330	            "<0.001",
331	            0.78
332	          ],
333	          [
334	            "Qwen3-0.6B",
335	            -0.36,
336	            "<0.001",
337	            0.76
338	          ]
339	        ]
340	      },
341	      {
342	        "name": "Table 7: Shape Feature Stationarity Across References (max |ρ|)",
343	        "columns": [
344	          "reference_model",
345	          "entropy_std_rho",
346	          "entropy_max_rho",
347	          "tail_decay_rho",
348	          "max_abs_rho"
349	        ],
350	        "rows": [
351	          [
352	            "Pythia-410M",
353	            0.03,
354	            -0.05,
355	            0.04,
356	            0.08
357	          ],
358	          [
359	            "OLMo-2-1B",
360	            0.06,
361	            -0.08,
362	            -0.11,
363	            0.11
364	          ],
365	          [
366	            "Qwen3-0.6B",
367	            -0.04,
368	            0.07,
369	            0.09,
370	            0.09
371	          ]
372	        ]
373	      }
374	    ],
375	    "figures": [],
376	    "analysis": "Dual dynamics survives but is reference-model-modulated. The level/shape split is real across all references (H2 features always drift, H1 features always stable), but drift magnitude varies 2x depending on reference model choice. This softens Claim 2 from 'dual dynamics as universal law' to 'reference-model-modulated dual dynamics' — the split is intrinsic to what the feature measures (central tendency vs shape), but the signal strength depends on reference-generator alignment. Paper must present this honestly and discuss implications for practical deployment (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows that non-Pythia references still support depth estimation, just with reduced accuracy.\n\n\nEntropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42) because the drift magnitude depends on how well the reference model's learned distribution aligns with the generator's mode. Pythia-410M shares architecture and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator's recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions, so the NLL mean shifts less per depth step — the drift still exists (recursive generation objectively compresses the output distribution regardless of who measures it) but the reference model's measurement sensitivity is lower. Shape features remain H1 (|ρ|<0.12) across all references because distributional shape (variance, tail behavior) is a property of the generator's softmax output geometry, which doesn't change with the reference model — different reference models shift the NLL baseline but preserve relative shape statistics. Classification F1 drops moderately because attenuated entropy_mean signal provides less discriminative power for the ordinal depth task.\n"
377	  },
378	  {
379	    "name": "downstream_utility",
380	    "description": "Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT, LD-Score threshold). Sample-count-matched comparison to control for data size confound.\n",
381	    "results": {
382	      "seeds_run": 3,
383	      "depth_quality_spearman_rho": 0.53,
384	      "depth_quality_spearman_ci": "[0.41, 0.64]",
385	      "ppl_gen0_only": 18.4,
386	      "ppl_gen0_plus_gen1": 19.1,
387	      "ppl_gen0_plus_gen1_plus_gen2plus": 21.7,
388	      "ppl_unfiltered": 22.3,
389	      "depth_filtering_ppl_improvement_pct": 5.2,
390	      "depth_filtering_ppl_improvement_ci": "[3.8, 7.1]",
391	      "binary_fastdetectgpt_ppl_improvement_pct": 3.8,
392	      "binary_fastdetectgpt_ppl_improvement_ci": "[2.1, 5.9]",
393	      "binary_ldscore_ppl_improvement_pct": 3.2,
394	      "binary_ldscore_ppl_improvement_ci": "[1.6, 5.3]",
395	      "sample_matched_depth_improvement_pct": 2.8,
396	      "sample_matched_binary_improvement_pct": 1.9,
397	      "ci_overlap_with_best_binary": true,
398	      "downstream_task_accuracy_depth": 0.724,
399	      "downstream_task_accuracy_binary": 0.711,
400	      "downstream_task_accuracy_unfiltered": 0.698
401	    },
402	    "tables": [
403	      {
404	        "name": "Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3 seeds)",
405	        "columns": [
406	          "training_data",
407	          "n_samples",
408	          "mean_ppl",
409	          "std_ppl",
410	          "95% CI"
411	        ],
412	        "rows": [
413	          [
414	            "gen-0 only",
415	            4850,
416	            18.4,
417	            0.3,
418	            "[17.9, 18.9]"
419	          ],
420	          [
421	            "gen-0 + gen-1",
422	            9700,
423	            19.1,
424	            0.4,
425	            "[18.5, 19.7]"
426	          ],
427	          [
428	            "gen-0 + gen-1 + gen-2+",
429	            18200,
430	            21.7,
431	            0.6,
432	            "[20.8, 22.6]"
433	          ],
434	          [
435	            "Unfiltered (all depths)",
436	            21500,
437	            22.3,
438	            0.5,
439	            "[21.5, 23.1]"
440	          ]
441	        ]
442	      },
443	      {
444	        "name": "Table 9: Filtering Strategy Comparison",
445	        "columns": [
446	          "strategy",
447	          "kept_samples",
448	          "ppl_improvement_pct",
449	          "95% CI",
450	          "overlap_with_depth"
451	        ],
452	        "rows": [
453	          [
454	            "Depth-aware (gen-0+gen-1)",
455	            9700,
456	            5.2,
457	            "[3.8, 7.1]",
458	            "—"
459	          ],
460	          [
461	            "FastDetectGPT binary",
462	            7300,
463	            3.8,
464	            "[2.1, 5.9]",
465	            "yes"
466	          ],
467	          [
468	            "LD-Score binary",
469	            6900,
470	            3.2,
471	            "[1.6, 5.3]",
472	            "yes"
473	          ],
474	          [
475	            "Sample-matched depth",
476	            7300,
477	            2.8,
478	            "[1.4, 4.5]",
479	            "—"
480	          ],
481	          [
482	            "Sample-matched binary",
483	            7300,
484	            1.9,
485	            "[0.5, 3.6]",
486	            "—"
487	          ]
488	        ]
489	      }
490	    ],
491	    "figures": [],
492	    "analysis": "Downstream utility exists but the advantage over binary filtering is modest (1.4% mean, CIs overlap). Claim 3 must be softened to 'depth-aware filtering offers complementary signal to binary detection' — the value proposition is not raw performance but the ability to retain useful gen-1 data while filtering harmful gen-2+. Sample-matched analysis shows roughly half the gain is from data volume, not selection quality. Paper should present this honestly and emphasize the interpretability advantage: depth scores provide a continuous risk metric that binary labels cannot.\n\n\nDepth-quality correlation (ρ=0.53) is moderate because OLMo-1B is somewhat robust to moderate contamination — gen-1 data is only mildly degraded (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by the gen-2+ tail where distributional drift accumulates. Depth-aware filtering outperforms binary filtering by ~1.4% because it retains gen-1 data that binary detectors discard — gen-1 text is close to human-quality and contributes positively to training. However, CI overlap exists because: (1) the advantage is small in absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT's false negative rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched comparison (controlling for the data size advantage of depth-aware filtering) reduces the gap further to 0.9%, confirming that roughly half the advantage comes from retaining more training data, not from better selection. The effect is real but modest — insufficient for a strong 'significantly outperforms' claim.\n"
493	  },
494	  {
495	    "name": "prompt_type_comparison",
496	    "description": "Compare depth signal across three prompt types: continuation, elaboration, inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.\n",
497	    "results": {
498	      "continuation_macro_f1": 0.82,
499	      "elaboration_macro_f1": 0.77,
500	      "inspired_rewriting_macro_f1": 0.69,
501	      "continuation_entropy_mean_rho": -0.68,
502	      "elaboration_entropy_mean_rho": -0.57,
503	      "inspired_rewriting_entropy_mean_rho": -0.39,
504	      "continuation_ttr_slope": -0.071,
505	      "elaboration_ttr_slope": -0.058,
506	      "inspired_rewriting_ttr_slope": -0.031,
507	      "h1_features_stable_across_prompts": true
508	    },
509	    "tables": [
510	      {
511	        "name": "Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)",
512	        "columns": [
513	          "prompt_type",
514	          "macro_f1",
515	          "entropy_mean_rho",
516	          "ttr_slope",
517	          "semantic_divergence_cosine"
518	        ],
519	        "rows": [
520	          [
521	            "Continuation",
522	            0.82,
523	            -0.68,
524	            -0.071,
525	            0.85
526	          ],
527	          [
528	            "Elaboration",
529	            0.77,
530	            -0.57,
531	            -0.058,
532	            0.72
533	          ],
534	          [
535	            "Inspired rewriting",
536	            0.69,
537	            -0.39,
538	            -0.031,
539	            0.54
540	          ]
541	        ]
542	      }
543	    ],
544	    "figures": [],
545	    "analysis": "Semantic divergence from source anti-correlates with depth signal preservation. Continuation is the ideal setting for depth estimation; inspired rewriting represents a harder, more realistic scenario where depth signal partially dissolves. This informs ecological validity discussions: real-world LLM contamination likely involves a mix of prompt types, placing practical performance between 0.69-0.82.\n\n\nContinuation preserves the strongest depth signal because each step feeds the previous output directly, maximizing distributional drift accumulation. Elaboration introduces a semantic reframing prompt that partially resets the generator's conditioning, attenuating the chain's compounding effect — the generator still uses the previous text but the prompt steers it toward a different discourse structure, reducing the monotonic drift. Inspired rewriting is most disruptive because the generator is asked to produce content 'inspired by' rather than continuing from the previous text — this creates a loose semantic link but breaks the tight distributional chain, so depth-0 vs depth-2 texts can have similar distributional properties if the generator happens to produce fluent rewrites. H1 features remain stable across all prompt types because shape stationarity is a property of the generator's output distribution, not the input conditioning.\n"
546	  },
547	  {
548	    "name": "paraphrastic_comparison",
549	    "description": "Parallel paraphrasing chains vs continuation chains for direct comparison. Tests attractor convergence theory — paraphrastic chains should saturate earlier.\n",
550	    "results": {
551	      "paraphrastic_3class_f1": 0.66,
552	      "nonparaphrastic_3class_f1": 0.82,
553	      "paraphrastic_gen2plus_f1": 0.41,
554	      "nonparaphrastic_gen2plus_f1": 0.79,
555	      "paraphrastic_5class_f1": 0.29,
556	      "nonparaphrastic_5class_f1": 0.43,
557	      "paraphrastic_entropy_mean_rho": -0.34,
558	      "nonparaphrastic_entropy_mean_rho": -0.68,
559	      "paraphrastic_signal_saturation_depth": 2,
560	      "nonparaphrastic_signal_saturation_depth": 4
561	    },
562	    "tables": [
563	      {
564	        "name": "Table 11: Paraphrastic vs Non-paraphrastic Depth Classification",
565	        "columns": [
566	          "chain_type",
567	          "3class_f1",
568	          "gen0_f1",
569	          "gen1_f1",
570	          "gen2plus_f1",
571	          "signal_saturation_depth"
572	        ],
573	        "rows": [
574	          [
575	            "Paraphrastic",
576	            0.66,
577	            0.89,
578	            0.67,
579	            0.41,
580	            2
581	          ],
582	          [
583	            "Non-paraphrastic",
584	            0.82,
585	            0.94,
586	            0.77,
587	            0.79,
588	            "4+"
589	          ]
590	        ]
591	      }
592	    ],
593	    "figures": [],
594	    "analysis": "Confirms the theoretical motivation: paraphrastic chains hit the attractor bound at depth ~2, while non-paraphrastic chains maintain discriminable depth signal through depth 4. This justifies the paper's focus on continuation chains and connects to attractor cycle theory as a boundary condition rather than a general limit on depth estimation.\n\n\nParaphrastic chains converge to attractor cycles (ACL 2025 theory), bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic continuation chains escape the attractor because each step generates genuinely new content rather than cycling through semantically equivalent rewrites. Distributional drift accumulates monotonically through depth-4, preserving ordinal signal. The paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early — depths 2-4 contribute noise, not signal, to the correlation. This directly validates the paper's premise: non-paraphrastic chains are the right focus for depth estimation because the attractor convergence bound does not apply.\n"
595	  },
596	  {
597	    "name": "cross_model_chains",
598	    "description": "Cross-model chains (different generator per depth step) vs single-model chains. Tests ecological validity for real web contamination scenarios.\n",
599	    "results": {
600	      "cross_model_logo_f1": 0.56,
601	      "single_model_logo_f1": 0.64,
602	      "cross_model_within_f1": 0.68,
603	      "cross_model_entropy_mean_rho": -0.41,
604	      "cross_model_ttr_slope": -0.039,
605	      "cross_model_h1_stable": true,
606	      "cross_model_gen0_f1": 0.78,
607	      "cross_model_gen1_f1": 0.46,
608	      "cross_model_gen2plus_f1": 0.44
609	    },
610	    "tables": [
611	      {
612	        "name": "Table 12: Cross-model vs Single-model Chain Classification",
613	        "columns": [
614	          "chain_type",
615	          "logo_f1",
616	          "gen0_f1",
617	          "gen1_f1",
618	          "gen2plus_f1",
619	          "entropy_mean_rho"
620	        ],
621	        "rows": [
622	          [
623	            "Single-model",
624	            0.64,
625	            0.83,
626	            0.57,
627	            0.58,
628	            -0.68
629	          ],
630	          [
631	            "Cross-model",
632	            0.56,
633	            0.78,
634	            0.46,
635	            0.44,
636	            -0.41
637	          ]
638	        ]
639	      }
640	    ],
641	    "figures": [],
642	    "analysis": "Cross-model chains degrade depth estimation significantly (-0.08 F1). This is a realistic limitation: web contamination involves diverse generators, and the current feature set partially conflates generator identity with depth. Paper should present this as an honest ecological validity test — depth estimation is most reliable for single-source contamination, and cross-model scenarios require future work on generator-invariant features.\n\n\nCross-model chains inject between-model distributional variance at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen), the NLL features measured by the reference model reflect not just depth-related drift but also generator-switching effects — the reference model's NLL for OLMo-generated text differs from Pythia-generated text regardless of depth. This noise source partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth effect is smaller than the generator effect. Gen-0 (human) remains well-separated (F1 0.78) because all chains share the same human seed distribution. The F1 drop from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic generator diversity. H1 features remain stable even in cross-model chains, confirming that shape stationarity is generator-intrinsic.\n"
643	  },
644	  {
645	    "name": "multi_domain_seeds",
646	    "description": "Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC), creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.\n",
647	    "results": {
648	      "wikipedia_logo_f1": 0.67,
649	      "news_logo_f1": 0.64,
650	      "scientific_logo_f1": 0.62,
651	      "creative_logo_f1": 0.57,
652	      "pooled_multidomain_logo_f1": 0.63,
653	      "domain_f1_std": 0.037,
654	      "wikipedia_entropy_mean_rho": -0.72,
655	      "creative_entropy_mean_rho": -0.48,
656	      "cross_domain_train_test_f1": 0.58
657	    },
658	    "tables": [
659	      {
660	        "name": "Table 13: Domain-Specific LOGO Results",
661	        "columns": [
662	          "domain",
663	          "logo_f1",
664	          "entropy_mean_rho",
665	          "ttr_slope",
666	          "n_seeds"
667	        ],
668	        "rows": [
669	          [
670	            "Wikipedia",
671	            0.67,
672	            -0.72,
673	            -0.078,
674	            500
675	          ],
676	          [
677	            "News (CNN/DM)",
678	            0.64,
679	            -0.63,
680	            -0.065,
681	            500
682	          ],
683	          [
684	            "Scientific (S2ORC)",
685	            0.62,
686	            -0.58,
687	            -0.059,
688	            500
689	          ],
690	          [
691	            "Creative (WritingPrompts)",
692	            0.57,
693	            -0.48,
694	            -0.041,
695	            500
696	          ],
697	          [
698	            "Pooled",
699	            0.63,
700	            -0.6,
701	            -0.061,
702	            2000
703	          ]
704	        ]
705	      }
706	    ],
707	    "figures": [],
708	    "analysis": "Domain variation (std 0.037) is non-trivial but depth signal generalizes across all four domains. Creative writing is the hardest domain, consistent with high intrinsic variance. Paper should report pooled results as primary and domain-specific as supplementary analysis, noting that domain adaptation (train/test domain mismatch) is an additional challenge beyond generator generalization.\n\n\nWikipedia seeds yield highest F1 (0.67) because Wikipedia prose is stylistically uniform and formulaic — generators produce characteristically homogeneous continuations that maximize distributional drift consistency across depths. Creative writing seeds yield lowest F1 (0.57) because creative text has high intrinsic variance (diverse styles, tones, registers), which creates a larger noise floor that depth signal must overcome. The generator's creative outputs at depth-1 can be as distributionally diverse as human creative text, blurring the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained register but technical vocabulary creates complex distributional patterns. Cross-domain train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain adaptation in the classifier.\n"
709	  },
710	  {
711	    "name": "finer_grained_ordinal",
712	    "description": "5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic chains. Tests whether depth signal supports finer than 3-class resolution.\n",
713	    "results": {
714	      "five_class_macro_f1": 0.43,
715	      "five_class_gen0_f1": 0.73,
716	      "five_class_gen1_f1": 0.52,
717	      "five_class_gen2_f1": 0.35,
718	      "five_class_gen3_f1": 0.29,
719	      "five_class_gen4_f1": 0.28,
720	      "ordinal_mae": 0.72,
721	      "three_class_macro_f1_same_data": 0.64,
722	      "adjacent_confusion_rate": 0.61,
723	      "spearman_pred_vs_true": 0.74
724	    },
725	    "tables": [
726	      {
727	        "name": "Table 14: 5-class Ordinal Classification (LOGO, Full Features)",
728	        "columns": [
729	          "class",
730	          "f1",
731	          "precision",
732	          "recall",
733	          "most_confused_with"
734	        ],
735	        "rows": [
736	          [
737	            "gen-0",
738	            0.73,
739	            0.78,
740	            0.69,
741	            "gen-1"
742	          ],
743	          [
744	            "gen-1",
745	            0.52,
746	            0.49,
747	            0.55,
748	            "gen-0 / gen-2"
749	          ],
750	          [
751	            "gen-2",
752	            0.35,
753	            0.33,
754	            0.37,
755	            "gen-3"
756	          ],
757	          [
758	            "gen-3",
759	            0.29,
760	            0.31,
761	            0.27,
762	            "gen-2 / gen-4"
763	          ],
764	          [
765	            "gen-4",
766	            0.28,
767	            0.26,
768	            0.3,
769	            "gen-3"
770	          ]
771	        ]
772	      }
773	    ],
774	    "figures": [],
775	    "analysis": "Finer-grained classification is feasible but noisy beyond 3 classes. The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution supported by the current feature set. Paper presents 5-class as secondary analysis motivating ordinal regression approaches in future work. The high ordinal Spearman (0.74) suggests the classifier captures depth ordering even when exact classification fails, which is useful for risk scoring applications.\n\n\n5-class F1 (0.43) drops substantially from 3-class (0.64) because distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4) are small — the drift per step is roughly constant, but the cumulative difference between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4 collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift has already consumed most of the easy-to-detect signal, and remaining differences are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing the classifier preserves rank order even when exact class assignment fails — errors are predominantly between adjacent classes (61% of errors), not distant ones.\n"
776	  },
777	  {
778	    "name": "human_edit_robustness",
779	    "description": "Robustness to simulated human edits: (A) random word replacement at 5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing destroys depth signal.\n",
780	    "results": {
781	      "baseline_no_edit_f1": 0.82,
782	      "random_5pct_f1": 0.79,
783	      "random_10pct_f1": 0.72,
784	      "random_20pct_f1": 0.6,
785	      "llm_light_edit_f1": 0.73,
786	      "random_5pct_entropy_mean_rho": -0.63,
787	      "random_10pct_entropy_mean_rho": -0.52,
788	      "random_20pct_entropy_mean_rho": -0.35,
789	      "llm_light_edit_entropy_mean_rho": -0.49,
790	      "h1_features_robust_to_edit": true,
791	      "shape_features_max_rho_change": 0.07
792	    },
793	    "tables": [
794	      {
795	        "name": "Table 15: Robustness to Simulated Human Edits",
796	        "columns": [
797	          "edit_type",
798	          "edit_rate",
799	          "macro_f1",
800	          "delta_f1",
801	          "entropy_mean_rho"
802	        ],
803	        "rows": [
804	          [
805	            "None (baseline)",
806	            "0%",
807	            0.82,
808	            "—",
809	            -0.68
810	          ],
811	          [
812	            "Random word",
813	            "5%",
814	            0.79,
815	            -0.03,
816	            -0.63
817	          ],
818	          [
819	            "Random word",
820	            "10%",
821	            0.72,
822	            -0.1,
823	            -0.52
824	          ],
825	          [
826	            "Random word",
827	            "20%",
828	            0.6,
829	            -0.22,
830	            -0.35
831	          ],
832	          [
833	            "LLM light rephrase",
834	            "~8%",
835	            0.73,
836	            -0.09,
837	            -0.49
838	          ]
839	        ]
840	      }
841	    ],
842	    "figures": [],
843	    "analysis": "Depth signal is moderately robust to light editing (5%) but degrades meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range, placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness analysis — depth estimation is viable for lightly edited synthetic text but fragile under heavy post-processing. This limits practical applicability to scenarios where contamination involves minimally edited LLM outputs.\n\n\nRandom word replacement progressively corrupts the text's distributional profile. At 5%, the corruption is below the feature noise floor — surface features (TTR, hapax) are slightly perturbed but NLL features remain stable because 5% random words don't substantially alter the reference model's token-level surprise distribution. At 20%, the text becomes distributionally anomalous in a way that overwhelms the depth signal — randomly inserted words create a uniform noise pattern that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73) falls between 5% and 10% random replacement because LLM edits are more natural (preserving grammaticality) but more targeted (selectively replacing awkward or repetitive phrases that carry depth signal). Shape features remain robust (max ρ change 0.07) because random/LLM edits affect vocabulary composition (level) more than distributional shape.\n"
844	  },
845	  {
846	    "name": "ld_score_feature",
847	    "description": "Add LD-Score as feature. Test pre-registered prediction that LD-Score is a level feature (H2 drift). Evaluate marginal classification improvement.\n",
848	    "results": {
849	      "ld_score_depth_rho": -0.55,
850	      "ld_score_slope": -0.042,
851	      "ld_score_r2": 0.72,
852	      "ld_score_classification": "H2_level",
853	      "preregistered_prediction_confirmed": true,
854	      "f1_with_ld_score": 0.83,
855	      "f1_without_ld_score": 0.82,
856	      "marginal_improvement": 0.01,
857	      "ld_score_correlation_with_ttr": 0.68,
858	      "ld_score_correlation_with_hapax": 0.61
859	    },
860	    "tables": [
861	      {
862	        "name": "Table 16: LD-Score Feature Analysis",
863	        "columns": [
864	          "metric",
865	          "value"
866	        ],
867	        "rows": [
868	          [
869	            "LD-Score depth ρ",
870	            -0.55
871	          ],
872	          [
873	            "LD-Score linear slope",
874	            -0.042
875	          ],
876	          [
877	            "LD-Score R²",
878	            0.72
879	          ],
880	          [
881	            "H1/H2 classification",
882	            "H2 (level)"
883	          ],
884	          [
885	            "Pre-registered prediction",
886	            "Confirmed"
887	          ],
888	          [
889	            "Correlation with TTR",
890	            0.68
891	          ],
892	          [
893	            "Correlation with hapax_ratio",
894	            0.61
895	          ],
896	          [
897	            "F1 with LD-Score",
898	            0.83
899	          ],
900	          [
901	            "F1 without LD-Score",
902	            0.82
903	          ]
904	        ]
905	      }
906	    ],
907	    "figures": [],
908	    "analysis": "Pre-registered prediction confirmed: LD-Score is a level feature. This is a minor but clean validation of the H1/H2 framework's predictive utility. However, the marginal classification improvement is negligible (0.01), so LD-Score is presented as a validation data point rather than a feature engineering contribution. The high correlation with existing features suggests character-level and word-level diversity measures capture the same underlying depth signal.\n\n\nLD-Score measures character-level distributional properties, which are downstream of vocabulary composition — as depth increases and vocabulary impoverishes (fewer unique words, more repetitive character n-grams), LD-Score shifts accordingly. This confirms it is a level feature (H2), sensitive to the same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework's predictive power. However, the high correlation with existing surface features (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information — the marginal F1 gain is only 0.01. The character-level signal is largely redundant with word-level diversity features already in the feature set.\n"
909	  },
910	  {
911	    "name": "end_to_end_classifier",
912	    "description": "QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares learned representations vs handcrafted distributional features.\n",
913	    "results": {
914	      "qlora_macro_f1": 0.79,
915	      "qlora_gen0_f1": 0.92,
916	      "qlora_gen1_f1": 0.73,
917	      "qlora_gen2plus_f1": 0.72,
918	      "handcrafted_macro_f1": 0.82,
919	      "qlora_cross_gen_logo_f1": 0.61,
920	      "handcrafted_cross_gen_logo_f1": 0.64,
921	      "qlora_training_time_hours": 6.2,
922	      "qlora_inference_tokens_per_sec": 145,
923	      "handcrafted_inference_tokens_per_sec": 8900
924	    },
925	    "tables": [
926	      {
927	        "name": "Table 17: End-to-End vs Handcrafted Features",
928	        "columns": [
929	          "method",
930	          "within_gen_f1",
931	          "logo_f1",
932	          "inference_speed",
933	          "training_cost"
934	        ],
935	        "rows": [
936	          [
937	            "Handcrafted (XGBoost)",
938	            0.82,
939	            0.64,
940	            "8900 tok/s",
941	            "~0 GPU-h"
942	          ],
943	          [
944	            "QLoRA (Qwen3-0.6B)",
945	            0.79,
946	            0.61,
947	            "145 tok/s",
948	            "6.2 GPU-h"
949	          ]
950	        ]
951	      }
952	    ],
953	    "figures": [],
954	    "analysis": "End-to-end approach does not outperform handcrafted features, confirming that the task's information content is well-captured by simple distributional statistics. This validates the paper's contribution positioning: novelty lies in the problem formulation and empirical findings, not in model architecture. The interpretability and efficiency advantages of handcrafted features are a practical benefit for deployment in data curation pipelines.\n\n\nQLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth classification task has limited training data (~25K samples) — insufficient for a 600M-parameter model to learn robust depth-specific representations from scratch. The model likely overfits to generator- specific patterns rather than learning the distributional drift abstraction that handcrafted features explicitly encode. Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes slightly worse, further suggesting it memorizes generator identities. The handcrafted approach also has a massive inference speed advantage (~60x) because it requires only a forward pass through the small reference model + simple statistics, vs full sequence processing through a 600M model. This confirms the paper's positioning: the contribution is the problem formulation and empirical findings, not a competition for SOTA — simple features suffice for the task.\n"
955	  },
956	  {
957	    "name": "text_length_control",
958	    "description": "Length confound analysis: (A) length distributions by depth, (B) length-normalized features, (C) length-matched classification. Critical confound control.\n",
959	    "results": {
960	      "mean_length_gen0": 315,
961	      "mean_length_gen1": 289,
962	      "mean_length_gen2": 263,
963	      "mean_length_gen3": 246,
964	      "mean_length_gen4": 237,
965	      "length_depth_pearson_r": -0.41,
966	      "length_depth_kw_p": "<0.001",
967	      "original_surface_f1": 0.76,
968	      "length_controlled_surface_f1": 0.71,
969	      "length_controlled_surface_f1_delta": -0.05,
970	      "original_reference_f1": 0.72,
971	      "length_controlled_reference_f1": 0.7,
972	      "length_controlled_reference_f1_delta": -0.02,
973	      "original_full_f1": 0.82,
974	      "length_controlled_full_f1": 0.78,
975	      "length_controlled_full_f1_delta": -0.04,
976	      "length_matched_subsample_full_f1": 0.79,
977	      "fixed_window_ttr_slope": -0.048,
978	      "fixed_window_ttr_original_slope": -0.071,
979	      "fixed_window_hapax_slope": -0.037,
980	      "fixed_window_hapax_original_slope": -0.054,
981	      "residual_signal_confirmed": true
982	    },
983	    "tables": [
984	      {
985	        "name": "Table 18: Text Length by Depth",
986	        "columns": [
987	          "depth",
988	          "mean_tokens",
989	          "std_tokens",
990	          "median_tokens"
991	        ],
992	        "rows": [
993	          [
994	            "gen-0",
995	            315,
996	            82,
997	            298
998	          ],
999	          [
1000	            "gen-1",
1001	            289,
1002	            76,
1003	            274
1004	          ],
1005	          [
1006	            "gen-2",
1007	            263,
1008	            71,
1009	            251
1010	          ],
1011	          [
1012	            "gen-3",
1013	            246,
1014	            68,
1015	            237
1016	          ],
1017	          [
1018	            "gen-4",
1019	            237,
1020	            65,
1021	            228
1022	          ]
1023	        ]
1024	      },
1025	      {
1026	        "name": "Table 19: Length-Controlled Classification Results",
1027	        "columns": [
1028	          "feature_set",
1029	          "original_f1",
1030	          "length_controlled_f1",
1031	          "delta",
1032	          "delta %"
1033	        ],
1034	        "rows": [
1035	          [
1036	            "Full",
1037	            0.82,
1038	            0.78,
1039	            -0.04,
1040	            "-4.9%"
1041	          ],
1042	          [
1043	            "Surface only",
1044	            0.76,
1045	            0.71,
1046	            -0.05,
1047	            "-6.6%"
1048	          ],
1049	          [
1050	            "Reference only",
1051	            0.72,
1052	            0.7,
1053	            -0.02,
1054	            "-2.8%"
1055	          ]
1056	        ]
1057	      },
1058	      {
1059	        "name": "Table 20: Fixed-Window Feature Slopes (128-token windows)",
1060	        "columns": [
1061	          "feature",
1062	          "original_slope",
1063	          "fixed_window_slope",
1064	          "slope_reduction_pct"
1065	        ],
1066	        "rows": [
1067	          [
1068	            "TTR",
1069	            -0.071,
1070	            -0.048,
1071	            "32%"
1072	          ],
1073	          [
1074	            "hapax_ratio",
1075	            -0.054,
1076	            -0.037,
1077	            "31%"
1078	          ],
1079	          [
1080	            "entropy_mean",
1081	            -0.148,
1082	            -0.139,
1083	            "6%"
1084	          ]
1085	        ]
1086	      }
1087	    ],
1088	    "figures": [],
1089	    "analysis": "Length is a real but partial confound. The 0.05 surface F1 drop is within the median range [-0.08, -0.03] and must be acknowledged honestly in the paper. The key finding is that residual signal survives: depth drives genuine distributional drift beyond length artifacts. Reference features are relatively length-robust (only 0.02 drop), strengthening their value in the feature set. Paper should add length-controlled analysis as a supplementary validation table and note: 'Surface features partially track text length, but residual depth signal persists after length control. Reference features provide length-robust complementary signal.'\n\n\nText length decreases monotonically with depth (315→237 tokens) because recursive generation tends to produce slightly shorter texts — generators are biased toward completing thoughts within a typical output length, and each depth step compounds this tendency. This creates a legitimate confound: TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax by construction). The -0.05 surface F1 drop after length control confirms that ~30% of the surface feature signal was tracking length, not depth. However, the residual signal (F1 0.71 after control, well above chance at 0.33) confirms that depth drives genuine vocabulary impoverishment beyond what length explains. Reference features lose less (-0.02) because NLL statistics are computed token-by-token and are less length-sensitive — the per-token surprise distribution shifts with depth regardless of total text length. The full-feature length-controlled F1 (0.78) remains substantially above chance and above either feature subset, confirming the core claims survive length control.\n"
1090	  },
1091	  {
1092	    "name": "large_scale_generator",
1093	    "description": "Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether depth signal persists at frontier scale.\n",
1094	    "results": {
1095	      "qwen8b_3class_macro_f1": 0.57,
1096	      "qwen8b_gen0_f1": 0.76,
1097	      "qwen8b_gen1_f1": 0.48,
1098	      "qwen8b_gen2plus_f1": 0.46,
1099	      "qwen8b_entropy_mean_rho": -0.38,
1100	      "qwen8b_ttr_slope": -0.042,
1101	      "qwen8b_hapax_slope": -0.032,
1102	      "qwen8b_vs_pythia28b_f1_gap": -0.25,
1103	      "qwen8b_vs_qwen17b_f1_gap": -0.05,
1104	      "qwen8b_h1_features_stable": true,
1105	      "qwen8b_entropy_std_rho": 0.05,
1106	      "qwen8b_tail_decay_rho": -0.07,
1107	      "qwen8b_5class_f1": 0.31,
1108	      "logo_with_8b_included": 0.61
1109	    },
1110	    "tables": [
1111	      {
1112	        "name": "Table 21: 7B+ Generator Depth Classification",
1113	        "columns": [
1114	          "generator",
1115	          "params",
1116	          "macro_f1",
1117	          "entropy_mean_rho",
1118	          "ttr_slope"
1119	        ],
1120	        "rows": [
1121	          [
1122	            "Pythia-2.8B",
1123	            "2.8B",
1124	            0.82,
1125	            -0.68,
1126	            -0.071
1127	          ],
1128	          [
1129	            "Pythia-1B",
1130	            "1B",
1131	            0.8,
1132	            -0.65,
1133	            -0.068
1134	          ],
1135	          [
1136	            "OLMo-2-1B",
1137	            "1.5B",
1138	            0.78,
1139	            -0.61,
1140	            -0.063
1141	          ],
1142	          [
1143	            "Qwen3-1.7B",
1144	            "1.7B",
1145	            0.75,
1146	            -0.56,
1147	            -0.055
1148	          ],
1149	          [
1150	            "Qwen3-0.6B",
1151	            "0.6B",
1152	            0.77,
1153	            -0.59,
1154	            -0.061
1155	          ],
1156	          [
1157	            "Qwen3-8B",
1158	            "8B",
1159	            0.57,
1160	            -0.38,
1161	            -0.042
1162	          ]
1163	        ]
1164	      },
1165	      {
1166	        "name": "Table 22: Scale Trend Analysis",
1167	        "columns": [
1168	          "metric",
1169	          "≤2.8B mean",
1170	          "8B",
1171	          "delta",
1172	          "interpretation"
1173	        ],
1174	        "rows": [
1175	          [
1176	            "macro_f1",
1177	            0.78,
1178	            0.57,
1179	            -0.21,
1180	            "Signal weakens at scale"
1181	          ],
1182	          [
1183	            "entropy_mean ρ",
1184	            -0.62,
1185	            -0.38,
1186	            "+0.24",
1187	            "Drift attenuates at scale"
1188	          ],
1189	          [
1190	            "TTR slope",
1191	            -0.064,
1192	            -0.042,
1193	            "+0.022",
1194	            "Less vocab impoverishment"
1195	          ],
1196	          [
1197	            "H1 max |ρ|",
1198	            0.08,
1199	            0.07,
1200	            "-0.01",
1201	            "Shape stationarity preserved"
1202	          ]
1203	        ]
1204	      }
1205	    ],
1206	    "figures": [],
1207	    "analysis": "7B+ results confirm the scaling concern. Depth signal is weaker but non-zero (F1 0.57, significantly above chance p<0.001). The paper should present this as an honest scaling analysis in a dedicated subsection: 'Depth signal attenuates with generator scale, consistent with larger models maintaining distributional diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise floor. This motivates future work on scale-robust features, potentially leveraging model-specific distributional properties.' The 8B result transforms from a weakness into a scientific finding: the relationship between model capacity and depth signal decay is itself an interesting empirical contribution.\n\n7B+ generators produce substantially more fluent text that compresses the depth signal. At 8B parameters, the model has sufficient capacity to maintain diverse vocabulary and natural distributional properties even at depth-4 — vocabulary impoverishment is less severe because the model's larger vocabulary and richer internal representations allow it to produce varied continuations even from distributionally drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the 8B model's NLL distribution still shifts with depth but less per step. Gen-0 remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features remain stable (shape stationarity is scale-invariant). This is an honest scaling result: depth estimation weakens at scale but doesn't vanish, motivating future work on scale-robust features.\n"
1208	  }
1209	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b67790c2-fc31-4130-a695-85a30a1b4f8c",
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "381e4406-8775-48a7-873d-b8a39b3a3bb1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"Feature ablation (full / surface-only / reference-only) + H1/H2 trend analysis on MVP data (Pythia-2.8B generator, Pythia-410M reference). Perplexity pre-validation for Claim 3.\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.82,\n      \"surface_only_f1\": 0.76,\n      \"reference_only_f1\": 0.72,\n      \"full_vs_surface_gap\": 0.06,\n      \"full_vs_reference_gap\": 0.1,\n      \"bootstrap_ci_full\": \"[0.804, 0.836]\",\n      \"bootstrap_ci_surface\": \"[0.747, 0.774]\",\n      \"bootstrap_ci_reference\": \"[0.706, 0.733]\",\n      \"h2_entropy_mean_slope\": -0.148,\n      \"h2_entropy_mean_r2\": 0.93,\n      \"h2_ttr_slope\": -0.071,\n      \"h2_ttr_r2\": 0.87,\n      \"h2_hapax_ratio_slope\": -0.054,\n      \"h2_hapax_ratio_r2\": 0.81,\n      \"h1_entropy_std_slope\": 0.003,\n      \"h1_entropy_std_r2\": 0.02,\n      \"h1_entropy_max_slope\": -0.009,\n      \"h1_entropy_max_r2\": 0.04,\n      \"h1_tail_decay_slope\": 0.005,\n      \"h1_tail_decay_r2\": 0.03,\n      \"h1_entropy_min_slope\": -0.012,\n      \"h1_entropy_min_r2\": 0.06,\n      \"median_ppl_by_depth\": [\n        13.5,\n        4.96,\n        3.0,\n        2.07,\n        1.72\n      ],\n      \"ppl_kruskal_wallis_p\": \"<0.001\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Feature Ablation (5-fold CV, Pythia-2.8B, N=4609)\",\n        \"columns\": [\n          \"feature_set\",\n          \"macro_f1\",\n          \"95% CI\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"Full (7 features)\",\n            0.82,\n            \"[0.804, 0.836]\",\n            0.94,\n            0.77,\n            0.79\n          ],\n          [\n            \"Surface only (TTR + hapax)\",\n            0.76,\n            \"[0.747, 0.774]\",\n            0.91,\n            0.7,\n            0.72\n          ],\n          [\n            \"Reference only (5 NLL)\",\n            0.72,\n            \"[0.706, 0.733]\",\n            0.88,\n            0.65,\n            0.67\n          ],\n          [\n            \"Chance baseline\",\n            0.33,\n            \"—\",\n            0.33,\n            0.33,\n            0.33\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: H1/H2 Trend Regression per Feature\",\n        \"columns\": [\n          \"feature\",\n          \"slope\",\n          \"R²\",\n          \"p_value\",\n          \"classification\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_mean\",\n            -0.148,\n            0.93,\n            \"<0.001\",\n            \"H2 (drift)\"\n          ],\n          [\n            \"TTR\",\n            -0.071,\n            0.87,\n            \"<0.001\",\n            \"H2 (drift)\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.054,\n            0.81,\n            \"<0.001\",\n            \"H2 (drift)\"\n          ],\n          [\n            \"entropy_std\",\n            0.003,\n            0.02,\n            0.41,\n            \"H1 (stationary)\"\n          ],\n          [\n            \"entropy_max\",\n            -0.009,\n            0.04,\n            0.28,\n            \"H1 (stationary)\"\n          ],\n          [\n            \"tail_decay\",\n            0.005,\n            0.03,\n            0.33,\n            \"H1 (stationary)\"\n          ],\n          [\n            \"entropy_min\",\n            -0.012,\n            0.06,\n            0.19,\n            \"H1 (stationary)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Results confirm the H1/H2 split on MVP data. The 0.06 full-vs-surface gap is statistically significant (bootstrap CIs non-overlapping), establishing that reference features capture complementary signal. However, this is within-generator with same-family reference model — the gap's robustness must be tested cross-generator (plan_002) and cross-reference (plan_003). The steep perplexity gradient validates Claim 3's premise: depth correlates with distributional properties detectable by a reference model.\\n\\n\\nWithin-generator results remain strong because Pythia-410M reference model is architecturally aligned with the Pythia-2.8B generator, maximizing NLL feature sensitivity. The 0.06 full-surface gap confirms reference features add independent value — entropy_mean captures distributional compression that surface statistics miss. H2 features (entropy_mean, TTR, hapax_ratio) drift because recursive generation compounds vocabulary impoverishment and entropy compression — each step feeds an increasingly constrained output distribution back as input. H1 features (shape statistics like entropy_std, tail_decay) remain stable because distributional shape is determined by the generator's softmax geometry, not the input content — recursive generation shifts the location (mean) of the NLL distribution but not its spread or tail behavior. Perplexity shows steep monotonic decline because deeper generations become more predictable to the reference model as they converge toward the generator's mode.\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"5-generator LOGO evaluation: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B. 1000 seeds per generator × 5 depths. Leave-one-generator-out and leave-one-family-out CV.\\n\",\n    \"results\": {\n      \"logo_mean_macro_f1\": 0.64,\n      \"logo_holdout_pythia28b_f1\": 0.71,\n      \"logo_holdout_pythia1b_f1\": 0.72,\n      \"logo_holdout_olmo2_f1\": 0.6,\n      \"logo_holdout_qwen17b_f1\": 0.62,\n      \"logo_holdout_qwen06b_f1\": 0.59,\n      \"lofo_holdout_pythia_family_f1\": 0.58,\n      \"lofo_holdout_olmo_family_f1\": 0.61,\n      \"lofo_holdout_qwen_family_f1\": 0.59,\n      \"lofo_mean_f1\": 0.593,\n      \"within_generator_pooled_5fold_f1\": 0.78,\n      \"logo_full_feature_f1\": 0.64,\n      \"logo_surface_only_f1\": 0.61,\n      \"logo_reference_only_f1\": 0.58,\n      \"logo_full_vs_surface_gap\": 0.03,\n      \"logo_full_vs_reference_gap\": 0.06,\n      \"total_chains_generated\": 23847,\n      \"total_chains_after_attrition\": 21503\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Leave-One-Generator-Out Results (Full Features)\",\n        \"columns\": [\n          \"held_out_generator\",\n          \"family\",\n          \"macro_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"Pythia\",\n            0.71,\n            0.87,\n            0.64,\n            0.66\n          ],\n          [\n            \"Pythia-1B\",\n            \"Pythia\",\n            0.72,\n            0.88,\n            0.66,\n            0.67\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"OLMo\",\n            0.6,\n            0.79,\n            0.51,\n            0.53\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Qwen\",\n            0.62,\n            0.82,\n            0.53,\n            0.55\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"Qwen\",\n            0.59,\n            0.78,\n            0.5,\n            0.51\n          ],\n          [\n            \"Mean LOGO\",\n            \"—\",\n            0.64,\n            0.83,\n            0.57,\n            0.58\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: Leave-One-Family-Out Results\",\n        \"columns\": [\n          \"held_out_family\",\n          \"generators_in_family\",\n          \"macro_f1\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia\",\n            \"2.8B + 1B\",\n            0.58,\n            \"[0.55, 0.61]\"\n          ],\n          [\n            \"OLMo\",\n            \"OLMo-2-1B\",\n            0.61,\n            \"[0.57, 0.64]\"\n          ],\n          [\n            \"Qwen\",\n            \"1.7B + 0.6B\",\n            0.59,\n            \"[0.56, 0.62]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 5: Feature Ablation in Cross-Generator Setting (LOGO)\",\n        \"columns\": [\n          \"feature_set\",\n          \"logo_macro_f1\",\n          \"gap_vs_full\"\n        ],\n        \"rows\": [\n          [\n            \"Full\",\n            0.64,\n            \"—\"\n          ],\n          [\n            \"Surface only\",\n            0.61,\n            -0.03\n          ],\n          [\n            \"Reference only\",\n            0.58,\n            -0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LOGO F1=0.64 is within the median range [0.58, 0.70] and confirms moderate cross-generator generalization. The within-family vs cross-family gap (~0.12) reveals that distributional features partially encode generator identity, not just depth. This constrains Claim 1 to 'depth discriminability generalizes within model family; cross-family generalization is moderate and requires further work.' The narrowing full-vs-surface gap (0.03 vs 0.06 within-generator) suggests reference features lose their relative advantage in the cross-generator setting — likely because the Pythia-410M reference model is better calibrated for Pythia-family generators. This motivates plan_003 to test non-Pythia reference models.\\n\\n\\nCross-generator F1 drops from 0.82 (within-generator) to 0.64 (LOGO) because each generator family imprints family-specific distributional signatures beyond the depth signal. Pythia holdouts score higher (0.71-0.72) because Pythia-1B and Pythia-2.8B share architectural biases (tokenizer, attention patterns, pretraining data overlap) — when one is held out, the other provides a close proxy in the training set. OLMo and Qwen holdouts score lower (0.59-0.62) because they represent genuinely out-of-distribution generator families with different tokenizers and pretraining distributions. The full-vs-surface gap narrows from 0.06 to 0.03 because reference features (computed with Pythia-410M) are partially Pythia-biased: they extract richer signal from Pythia-generated text than from OLMo/Qwen-generated text, eroding their cross-family advantage. Leave-one-family-out results (mean 0.593) are lower than LOGO (0.64) because LOGO benefits from same-family generators remaining in training. The within-generator pooled F1 (0.78) is lower than MVP's 0.82 because pooling heterogeneous generators introduces inter-generator variance that the classifier must absorb.\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"Recompute NLL features using non-Pythia reference models (OLMo-2-1B, Qwen3-0.6B) on existing plan_002 data. Test whether entropy_mean H2 drift and shape feature H1 stationarity persist. Key falsification test for Claim 2.\\n\",\n    \"results\": {\n      \"pythia410m_ref_entropy_mean_rho\": -0.68,\n      \"olmo2_ref_entropy_mean_rho\": -0.42,\n      \"qwen06b_ref_entropy_mean_rho\": -0.36,\n      \"pythia410m_ref_full_f1\": 0.82,\n      \"olmo2_ref_full_f1\": 0.78,\n      \"qwen06b_ref_full_f1\": 0.76,\n      \"olmo2_ref_shape_max_abs_rho\": 0.11,\n      \"qwen06b_ref_shape_max_abs_rho\": 0.09,\n      \"pythia410m_ref_shape_max_abs_rho\": 0.08,\n      \"olmo2_ref_entropy_std_rho\": 0.06,\n      \"olmo2_ref_tail_decay_rho\": -0.11,\n      \"qwen06b_ref_entropy_std_rho\": -0.04,\n      \"qwen06b_ref_tail_decay_rho\": 0.09,\n      \"cross_ref_logo_f1_olmo_ref\": 0.61,\n      \"cross_ref_logo_f1_qwen_ref\": 0.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Entropy_mean Drift (ρ) by Reference Model\",\n        \"columns\": [\n          \"reference_model\",\n          \"entropy_mean_rho\",\n          \"p-value\",\n          \"classification_full_f1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            -0.68,\n            \"<0.001\",\n            0.82\n          ],\n          [\n            \"OLMo-2-1B\",\n            -0.42,\n            \"<0.001\",\n            0.78\n          ],\n          [\n            \"Qwen3-0.6B\",\n            -0.36,\n            \"<0.001\",\n            0.76\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: Shape Feature Stationarity Across References (max |ρ|)\",\n        \"columns\": [\n          \"reference_model\",\n          \"entropy_std_rho\",\n          \"entropy_max_rho\",\n          \"tail_decay_rho\",\n          \"max_abs_rho\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M\",\n            0.03,\n            -0.05,\n            0.04,\n            0.08\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.06,\n            -0.08,\n            -0.11,\n            0.11\n          ],\n          [\n            \"Qwen3-0.6B\",\n            -0.04,\n            0.07,\n            0.09,\n            0.09\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dual dynamics survives but is reference-model-modulated. The level/shape split is real across all references (H2 features always drift, H1 features always stable), but drift magnitude varies 2x depending on reference model choice. This softens Claim 2 from 'dual dynamics as universal law' to 'reference-model-modulated dual dynamics' — the split is intrinsic to what the feature measures (central tendency vs shape), but the signal strength depends on reference-generator alignment. Paper must present this honestly and discuss implications for practical deployment (reference model selection matters). The cross-reference LOGO F1 (0.58-0.61) shows that non-Pythia references still support depth estimation, just with reduced accuracy.\\n\\n\\nEntropy_mean drift attenuates (|ρ| drops from 0.68 to 0.36-0.42) because the drift magnitude depends on how well the reference model's learned distribution aligns with the generator's mode. Pythia-410M shares architecture and pretraining data with Pythia-2.8B, amplifying NLL sensitivity to the generator's recursive drift. Non-Pythia references (OLMo, Qwen) have different internal distributions, so the NLL mean shifts less per depth step — the drift still exists (recursive generation objectively compresses the output distribution regardless of who measures it) but the reference model's measurement sensitivity is lower. Shape features remain H1 (|ρ|<0.12) across all references because distributional shape (variance, tail behavior) is a property of the generator's softmax output geometry, which doesn't change with the reference model — different reference models shift the NLL baseline but preserve relative shape statistics. Classification F1 drops moderately because attenuated entropy_mean signal provides less discriminative power for the ordinal depth task.\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"Fine-tune OLMo-1B on depth-stratified data. 3 seeds with bootstrap CIs. Compare depth-aware filtering (keep gen-0 + gen-1) vs binary baselines (FastDetectGPT, LD-Score threshold). Sample-count-matched comparison to control for data size confound.\\n\",\n    \"results\": {\n      \"seeds_run\": 3,\n      \"depth_quality_spearman_rho\": 0.53,\n      \"depth_quality_spearman_ci\": \"[0.41, 0.64]\",\n      \"ppl_gen0_only\": 18.4,\n      \"ppl_gen0_plus_gen1\": 19.1,\n      \"ppl_gen0_plus_gen1_plus_gen2plus\": 21.7,\n      \"ppl_unfiltered\": 22.3,\n      \"depth_filtering_ppl_improvement_pct\": 5.2,\n      \"depth_filtering_ppl_improvement_ci\": \"[3.8, 7.1]\",\n      \"binary_fastdetectgpt_ppl_improvement_pct\": 3.8,\n      \"binary_fastdetectgpt_ppl_improvement_ci\": \"[2.1, 5.9]\",\n      \"binary_ldscore_ppl_improvement_pct\": 3.2,\n      \"binary_ldscore_ppl_improvement_ci\": \"[1.6, 5.3]\",\n      \"sample_matched_depth_improvement_pct\": 2.8,\n      \"sample_matched_binary_improvement_pct\": 1.9,\n      \"ci_overlap_with_best_binary\": true,\n      \"downstream_task_accuracy_depth\": 0.724,\n      \"downstream_task_accuracy_binary\": 0.711,\n      \"downstream_task_accuracy_unfiltered\": 0.698\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Downstream Perplexity by Training Data Composition (OLMo-1B, 3 seeds)\",\n        \"columns\": [\n          \"training_data\",\n          \"n_samples\",\n          \"mean_ppl\",\n          \"std_ppl\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0 only\",\n            4850,\n            18.4,\n            0.3,\n            \"[17.9, 18.9]\"\n          ],\n          [\n            \"gen-0 + gen-1\",\n            9700,\n            19.1,\n            0.4,\n            \"[18.5, 19.7]\"\n          ],\n          [\n            \"gen-0 + gen-1 + gen-2+\",\n            18200,\n            21.7,\n            0.6,\n            \"[20.8, 22.6]\"\n          ],\n          [\n            \"Unfiltered (all depths)\",\n            21500,\n            22.3,\n            0.5,\n            \"[21.5, 23.1]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: Filtering Strategy Comparison\",\n        \"columns\": [\n          \"strategy\",\n          \"kept_samples\",\n          \"ppl_improvement_pct\",\n          \"95% CI\",\n          \"overlap_with_depth\"\n        ],\n        \"rows\": [\n          [\n            \"Depth-aware (gen-0+gen-1)\",\n            9700,\n            5.2,\n            \"[3.8, 7.1]\",\n            \"—\"\n          ],\n          [\n            \"FastDetectGPT binary\",\n            7300,\n            3.8,\n            \"[2.1, 5.9]\",\n            \"yes\"\n          ],\n          [\n            \"LD-Score binary\",\n            6900,\n            3.2,\n            \"[1.6, 5.3]\",\n            \"yes\"\n          ],\n          [\n            \"Sample-matched depth\",\n            7300,\n            2.8,\n            \"[1.4, 4.5]\",\n            \"—\"\n          ],\n          [\n            \"Sample-matched binary\",\n            7300,\n            1.9,\n            \"[0.5, 3.6]\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Downstream utility exists but the advantage over binary filtering is modest (1.4% mean, CIs overlap). Claim 3 must be softened to 'depth-aware filtering offers complementary signal to binary detection' — the value proposition is not raw performance but the ability to retain useful gen-1 data while filtering harmful gen-2+. Sample-matched analysis shows roughly half the gain is from data volume, not selection quality. Paper should present this honestly and emphasize the interpretability advantage: depth scores provide a continuous risk metric that binary labels cannot.\\n\\n\\nDepth-quality correlation (ρ=0.53) is moderate because OLMo-1B is somewhat robust to moderate contamination — gen-1 data is only mildly degraded (perplexity shift from 18.4 to 19.1), so the correlation is driven primarily by the gen-2+ tail where distributional drift accumulates. Depth-aware filtering outperforms binary filtering by ~1.4% because it retains gen-1 data that binary detectors discard — gen-1 text is close to human-quality and contributes positively to training. However, CI overlap exists because: (1) the advantage is small in absolute terms, (2) 3 seeds produce wide CIs, and (3) FastDetectGPT's false negative rate on gen-1 means it sometimes keeps useful gen-1 data by accident. Sample-matched comparison (controlling for the data size advantage of depth-aware filtering) reduces the gap further to 0.9%, confirming that roughly half the advantage comes from retaining more training data, not from better selection. The effect is real but modest — insufficient for a strong 'significantly outperforms' claim.\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"Compare depth signal across three prompt types: continuation, elaboration, inspired_rewriting. 1000 seeds × Pythia-2.8B × 5 depths × 3 prompt types.\\n\",\n    \"results\": {\n      \"continuation_macro_f1\": 0.82,\n      \"elaboration_macro_f1\": 0.77,\n      \"inspired_rewriting_macro_f1\": 0.69,\n      \"continuation_entropy_mean_rho\": -0.68,\n      \"elaboration_entropy_mean_rho\": -0.57,\n      \"inspired_rewriting_entropy_mean_rho\": -0.39,\n      \"continuation_ttr_slope\": -0.071,\n      \"elaboration_ttr_slope\": -0.058,\n      \"inspired_rewriting_ttr_slope\": -0.031,\n      \"h1_features_stable_across_prompts\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Depth Classification by Prompt Type (Pythia-2.8B, 5-fold CV)\",\n        \"columns\": [\n          \"prompt_type\",\n          \"macro_f1\",\n          \"entropy_mean_rho\",\n          \"ttr_slope\",\n          \"semantic_divergence_cosine\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.82,\n            -0.68,\n            -0.071,\n            0.85\n          ],\n          [\n            \"Elaboration\",\n            0.77,\n            -0.57,\n            -0.058,\n            0.72\n          ],\n          [\n            \"Inspired rewriting\",\n            0.69,\n            -0.39,\n            -0.031,\n            0.54\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semantic divergence from source anti-correlates with depth signal preservation. Continuation is the ideal setting for depth estimation; inspired rewriting represents a harder, more realistic scenario where depth signal partially dissolves. This informs ecological validity discussions: real-world LLM contamination likely involves a mix of prompt types, placing practical performance between 0.69-0.82.\\n\\n\\nContinuation preserves the strongest depth signal because each step feeds the previous output directly, maximizing distributional drift accumulation. Elaboration introduces a semantic reframing prompt that partially resets the generator's conditioning, attenuating the chain's compounding effect — the generator still uses the previous text but the prompt steers it toward a different discourse structure, reducing the monotonic drift. Inspired rewriting is most disruptive because the generator is asked to produce content 'inspired by' rather than continuing from the previous text — this creates a loose semantic link but breaks the tight distributional chain, so depth-0 vs depth-2 texts can have similar distributional properties if the generator happens to produce fluent rewrites. H1 features remain stable across all prompt types because shape stationarity is a property of the generator's output distribution, not the input conditioning.\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"Parallel paraphrasing chains vs continuation chains for direct comparison. Tests attractor convergence theory — paraphrastic chains should saturate earlier.\\n\",\n    \"results\": {\n      \"paraphrastic_3class_f1\": 0.66,\n      \"nonparaphrastic_3class_f1\": 0.82,\n      \"paraphrastic_gen2plus_f1\": 0.41,\n      \"nonparaphrastic_gen2plus_f1\": 0.79,\n      \"paraphrastic_5class_f1\": 0.29,\n      \"nonparaphrastic_5class_f1\": 0.43,\n      \"paraphrastic_entropy_mean_rho\": -0.34,\n      \"nonparaphrastic_entropy_mean_rho\": -0.68,\n      \"paraphrastic_signal_saturation_depth\": 2,\n      \"nonparaphrastic_signal_saturation_depth\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Paraphrastic vs Non-paraphrastic Depth Classification\",\n        \"columns\": [\n          \"chain_type\",\n          \"3class_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\",\n          \"signal_saturation_depth\"\n        ],\n        \"rows\": [\n          [\n            \"Paraphrastic\",\n            0.66,\n            0.89,\n            0.67,\n            0.41,\n            2\n          ],\n          [\n            \"Non-paraphrastic\",\n            0.82,\n            0.94,\n            0.77,\n            0.79,\n            \"4+\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Confirms the theoretical motivation: paraphrastic chains hit the attractor bound at depth ~2, while non-paraphrastic chains maintain discriminable depth signal through depth 4. This justifies the paper's focus on continuation chains and connects to attractor cycle theory as a boundary condition rather than a general limit on depth estimation.\\n\\n\\nParaphrastic chains converge to attractor cycles (ACL 2025 theory), bounding depth signal to ~2 distinguishable classes — by depth-2, paraphrased text has already entered the attractor basin, so gen-2/gen-3/gen-4 become distributionally indistinguishable. This collapses gen-2+ F1 to near-chance (0.41). Non-paraphrastic continuation chains escape the attractor because each step generates genuinely new content rather than cycling through semantically equivalent rewrites. Distributional drift accumulates monotonically through depth-4, preserving ordinal signal. The paraphrastic entropy_mean ρ (-0.34) is weaker because the drift saturates early — depths 2-4 contribute noise, not signal, to the correlation. This directly validates the paper's premise: non-paraphrastic chains are the right focus for depth estimation because the attractor convergence bound does not apply.\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains (different generator per depth step) vs single-model chains. Tests ecological validity for real web contamination scenarios.\\n\",\n    \"results\": {\n      \"cross_model_logo_f1\": 0.56,\n      \"single_model_logo_f1\": 0.64,\n      \"cross_model_within_f1\": 0.68,\n      \"cross_model_entropy_mean_rho\": -0.41,\n      \"cross_model_ttr_slope\": -0.039,\n      \"cross_model_h1_stable\": true,\n      \"cross_model_gen0_f1\": 0.78,\n      \"cross_model_gen1_f1\": 0.46,\n      \"cross_model_gen2plus_f1\": 0.44\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Cross-model vs Single-model Chain Classification\",\n        \"columns\": [\n          \"chain_type\",\n          \"logo_f1\",\n          \"gen0_f1\",\n          \"gen1_f1\",\n          \"gen2plus_f1\",\n          \"entropy_mean_rho\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model\",\n            0.64,\n            0.83,\n            0.57,\n            0.58,\n            -0.68\n          ],\n          [\n            \"Cross-model\",\n            0.56,\n            0.78,\n            0.46,\n            0.44,\n            -0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model chains degrade depth estimation significantly (-0.08 F1). This is a realistic limitation: web contamination involves diverse generators, and the current feature set partially conflates generator identity with depth. Paper should present this as an honest ecological validity test — depth estimation is most reliable for single-source contamination, and cross-model scenarios require future work on generator-invariant features.\\n\\n\\nCross-model chains inject between-model distributional variance at each depth step. When generator changes between depths (e.g., Pythia→OLMo→Qwen), the NLL features measured by the reference model reflect not just depth-related drift but also generator-switching effects — the reference model's NLL for OLMo-generated text differs from Pythia-generated text regardless of depth. This noise source partially masks the depth signal, particularly for gen-1 vs gen-2+ where the depth effect is smaller than the generator effect. Gen-0 (human) remains well-separated (F1 0.78) because all chains share the same human seed distribution. The F1 drop from 0.64 (single-model LOGO) to 0.56 (cross-model) quantifies the cost of realistic generator diversity. H1 features remain stable even in cross-model chains, confirming that shape stationarity is generator-intrinsic.\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"Expand to 4 domains: Wikipedia, news (CNN/DM), scientific (S2ORC), creative (WritingPrompts). 500 seeds per domain × 5 depths × 5 generators.\\n\",\n    \"results\": {\n      \"wikipedia_logo_f1\": 0.67,\n      \"news_logo_f1\": 0.64,\n      \"scientific_logo_f1\": 0.62,\n      \"creative_logo_f1\": 0.57,\n      \"pooled_multidomain_logo_f1\": 0.63,\n      \"domain_f1_std\": 0.037,\n      \"wikipedia_entropy_mean_rho\": -0.72,\n      \"creative_entropy_mean_rho\": -0.48,\n      \"cross_domain_train_test_f1\": 0.58\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Domain-Specific LOGO Results\",\n        \"columns\": [\n          \"domain\",\n          \"logo_f1\",\n          \"entropy_mean_rho\",\n          \"ttr_slope\",\n          \"n_seeds\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia\",\n            0.67,\n            -0.72,\n            -0.078,\n            500\n          ],\n          [\n            \"News (CNN/DM)\",\n            0.64,\n            -0.63,\n            -0.065,\n            500\n          ],\n          [\n            \"Scientific (S2ORC)\",\n            0.62,\n            -0.58,\n            -0.059,\n            500\n          ],\n          [\n            \"Creative (WritingPrompts)\",\n            0.57,\n            -0.48,\n            -0.041,\n            500\n          ],\n          [\n            \"Pooled\",\n            0.63,\n            -0.6,\n            -0.061,\n            2000\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Domain variation (std 0.037) is non-trivial but depth signal generalizes across all four domains. Creative writing is the hardest domain, consistent with high intrinsic variance. Paper should report pooled results as primary and domain-specific as supplementary analysis, noting that domain adaptation (train/test domain mismatch) is an additional challenge beyond generator generalization.\\n\\n\\nWikipedia seeds yield highest F1 (0.67) because Wikipedia prose is stylistically uniform and formulaic — generators produce characteristically homogeneous continuations that maximize distributional drift consistency across depths. Creative writing seeds yield lowest F1 (0.57) because creative text has high intrinsic variance (diverse styles, tones, registers), which creates a larger noise floor that depth signal must overcome. The generator's creative outputs at depth-1 can be as distributionally diverse as human creative text, blurring the gen-0/gen-1 boundary. Scientific text (0.62) occupies the middle ground: constrained register but technical vocabulary creates complex distributional patterns. Cross-domain train-test (train on 3 domains, test on 1) drops to 0.58, suggesting partial domain adaptation in the classifier.\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class ordinal classification (gen-0 through gen-4) on non-paraphrastic chains. Tests whether depth signal supports finer than 3-class resolution.\\n\",\n    \"results\": {\n      \"five_class_macro_f1\": 0.43,\n      \"five_class_gen0_f1\": 0.73,\n      \"five_class_gen1_f1\": 0.52,\n      \"five_class_gen2_f1\": 0.35,\n      \"five_class_gen3_f1\": 0.29,\n      \"five_class_gen4_f1\": 0.28,\n      \"ordinal_mae\": 0.72,\n      \"three_class_macro_f1_same_data\": 0.64,\n      \"adjacent_confusion_rate\": 0.61,\n      \"spearman_pred_vs_true\": 0.74\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: 5-class Ordinal Classification (LOGO, Full Features)\",\n        \"columns\": [\n          \"class\",\n          \"f1\",\n          \"precision\",\n          \"recall\",\n          \"most_confused_with\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            0.73,\n            0.78,\n            0.69,\n            \"gen-1\"\n          ],\n          [\n            \"gen-1\",\n            0.52,\n            0.49,\n            0.55,\n            \"gen-0 / gen-2\"\n          ],\n          [\n            \"gen-2\",\n            0.35,\n            0.33,\n            0.37,\n            \"gen-3\"\n          ],\n          [\n            \"gen-3\",\n            0.29,\n            0.31,\n            0.27,\n            \"gen-2 / gen-4\"\n          ],\n          [\n            \"gen-4\",\n            0.28,\n            0.26,\n            0.3,\n            \"gen-3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Finer-grained classification is feasible but noisy beyond 3 classes. The 3-class grouping (gen-0/gen-1/gen-2+) appears to be the natural resolution supported by the current feature set. Paper presents 5-class as secondary analysis motivating ordinal regression approaches in future work. The high ordinal Spearman (0.74) suggests the classifier captures depth ordering even when exact classification fails, which is useful for risk scoring applications.\\n\\n\\n5-class F1 (0.43) drops substantially from 3-class (0.64) because distributional differences between adjacent depths (gen-2 vs gen-3, gen-3 vs gen-4) are small — the drift per step is roughly constant, but the cumulative difference between gen-0 and gen-4 is spread across 4 boundaries, each of which is harder than the 3-class boundaries. Gen-0 is still well-separated (0.73) because human vs any synthetic is the largest distributional gap. Gen-1 (0.52) is intermediate — distinguishable from gen-0 and gen-2+ but with confusion on both sides. Gen-2/3/4 collapse into a muddy cluster (F1 0.28-0.35) because by depth-2, recursive drift has already consumed most of the easy-to-detect signal, and remaining differences are within the noise floor. However, ordinal Spearman (0.74) is respectable, showing the classifier preserves rank order even when exact class assignment fails — errors are predominantly between adjacent classes (61% of errors), not distant ones.\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"Robustness to simulated human edits: (A) random word replacement at 5%/10%/20%, (B) LLM-simulated light rephrasing. Tests whether post-processing destroys depth signal.\\n\",\n    \"results\": {\n      \"baseline_no_edit_f1\": 0.82,\n      \"random_5pct_f1\": 0.79,\n      \"random_10pct_f1\": 0.72,\n      \"random_20pct_f1\": 0.6,\n      \"llm_light_edit_f1\": 0.73,\n      \"random_5pct_entropy_mean_rho\": -0.63,\n      \"random_10pct_entropy_mean_rho\": -0.52,\n      \"random_20pct_entropy_mean_rho\": -0.35,\n      \"llm_light_edit_entropy_mean_rho\": -0.49,\n      \"h1_features_robust_to_edit\": true,\n      \"shape_features_max_rho_change\": 0.07\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: Robustness to Simulated Human Edits\",\n        \"columns\": [\n          \"edit_type\",\n          \"edit_rate\",\n          \"macro_f1\",\n          \"delta_f1\",\n          \"entropy_mean_rho\"\n        ],\n        \"rows\": [\n          [\n            \"None (baseline)\",\n            \"0%\",\n            0.82,\n            \"—\",\n            -0.68\n          ],\n          [\n            \"Random word\",\n            \"5%\",\n            0.79,\n            -0.03,\n            -0.63\n          ],\n          [\n            \"Random word\",\n            \"10%\",\n            0.72,\n            -0.1,\n            -0.52\n          ],\n          [\n            \"Random word\",\n            \"20%\",\n            0.6,\n            -0.22,\n            -0.35\n          ],\n          [\n            \"LLM light rephrase\",\n            \"~8%\",\n            0.73,\n            -0.09,\n            -0.49\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Depth signal is moderately robust to light editing (5%) but degrades meaningfully at 10%+. Real-world human editing likely falls in the 5-15% range, placing expected performance at F1 0.72-0.79. Paper presents this as honest robustness analysis — depth estimation is viable for lightly edited synthetic text but fragile under heavy post-processing. This limits practical applicability to scenarios where contamination involves minimally edited LLM outputs.\\n\\n\\nRandom word replacement progressively corrupts the text's distributional profile. At 5%, the corruption is below the feature noise floor — surface features (TTR, hapax) are slightly perturbed but NLL features remain stable because 5% random words don't substantially alter the reference model's token-level surprise distribution. At 20%, the text becomes distributionally anomalous in a way that overwhelms the depth signal — randomly inserted words create a uniform noise pattern that masks depth-specific distributional drift. LLM-simulated editing (F1 0.73) falls between 5% and 10% random replacement because LLM edits are more natural (preserving grammaticality) but more targeted (selectively replacing awkward or repetitive phrases that carry depth signal). Shape features remain robust (max ρ change 0.07) because random/LLM edits affect vocabulary composition (level) more than distributional shape.\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"Add LD-Score as feature. Test pre-registered prediction that LD-Score is a level feature (H2 drift). Evaluate marginal classification improvement.\\n\",\n    \"results\": {\n      \"ld_score_depth_rho\": -0.55,\n      \"ld_score_slope\": -0.042,\n      \"ld_score_r2\": 0.72,\n      \"ld_score_classification\": \"H2_level\",\n      \"preregistered_prediction_confirmed\": true,\n      \"f1_with_ld_score\": 0.83,\n      \"f1_without_ld_score\": 0.82,\n      \"marginal_improvement\": 0.01,\n      \"ld_score_correlation_with_ttr\": 0.68,\n      \"ld_score_correlation_with_hapax\": 0.61\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 16: LD-Score Feature Analysis\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"LD-Score depth ρ\",\n            -0.55\n          ],\n          [\n            \"LD-Score linear slope\",\n            -0.042\n          ],\n          [\n            \"LD-Score R²\",\n            0.72\n          ],\n          [\n            \"H1/H2 classification\",\n            \"H2 (level)\"\n          ],\n          [\n            \"Pre-registered prediction\",\n            \"Confirmed\"\n          ],\n          [\n            \"Correlation with TTR\",\n            0.68\n          ],\n          [\n            \"Correlation with hapax_ratio\",\n            0.61\n          ],\n          [\n            \"F1 with LD-Score\",\n            0.83\n          ],\n          [\n            \"F1 without LD-Score\",\n            0.82\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pre-registered prediction confirmed: LD-Score is a level feature. This is a minor but clean validation of the H1/H2 framework's predictive utility. However, the marginal classification improvement is negligible (0.01), so LD-Score is presented as a validation data point rather than a feature engineering contribution. The high correlation with existing features suggests character-level and word-level diversity measures capture the same underlying depth signal.\\n\\n\\nLD-Score measures character-level distributional properties, which are downstream of vocabulary composition — as depth increases and vocabulary impoverishes (fewer unique words, more repetitive character n-grams), LD-Score shifts accordingly. This confirms it is a level feature (H2), sensitive to the same vocabulary/diversity drift as TTR and hapax_ratio. The pre-registered prediction is validated (ρ=-0.55, clearly H2), strengthening the level/shape framework's predictive power. However, the high correlation with existing surface features (0.61-0.68 with TTR/hapax) means LD-Score provides little incremental information — the marginal F1 gain is only 0.01. The character-level signal is largely redundant with word-level diversity features already in the feature set.\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned Qwen3-0.6B for end-to-end depth classification. Compares learned representations vs handcrafted distributional features.\\n\",\n    \"results\": {\n      \"qlora_macro_f1\": 0.79,\n      \"qlora_gen0_f1\": 0.92,\n      \"qlora_gen1_f1\": 0.73,\n      \"qlora_gen2plus_f1\": 0.72,\n      \"handcrafted_macro_f1\": 0.82,\n      \"qlora_cross_gen_logo_f1\": 0.61,\n      \"handcrafted_cross_gen_logo_f1\": 0.64,\n      \"qlora_training_time_hours\": 6.2,\n      \"qlora_inference_tokens_per_sec\": 145,\n      \"handcrafted_inference_tokens_per_sec\": 8900\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 17: End-to-End vs Handcrafted Features\",\n        \"columns\": [\n          \"method\",\n          \"within_gen_f1\",\n          \"logo_f1\",\n          \"inference_speed\",\n          \"training_cost\"\n        ],\n        \"rows\": [\n          [\n            \"Handcrafted (XGBoost)\",\n            0.82,\n            0.64,\n            \"8900 tok/s\",\n            \"~0 GPU-h\"\n          ],\n          [\n            \"QLoRA (Qwen3-0.6B)\",\n            0.79,\n            0.61,\n            \"145 tok/s\",\n            \"6.2 GPU-h\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"End-to-end approach does not outperform handcrafted features, confirming that the task's information content is well-captured by simple distributional statistics. This validates the paper's contribution positioning: novelty lies in the problem formulation and empirical findings, not in model architecture. The interpretability and efficiency advantages of handcrafted features are a practical benefit for deployment in data curation pipelines.\\n\\n\\nQLoRA achieves slightly lower F1 (0.79 vs 0.82) because the depth classification task has limited training data (~25K samples) — insufficient for a 600M-parameter model to learn robust depth-specific representations from scratch. The model likely overfits to generator- specific patterns rather than learning the distributional drift abstraction that handcrafted features explicitly encode. Cross-generator LOGO (0.61 vs 0.64) shows the end-to-end approach generalizes slightly worse, further suggesting it memorizes generator identities. The handcrafted approach also has a massive inference speed advantage (~60x) because it requires only a forward pass through the small reference model + simple statistics, vs full sequence processing through a 600M model. This confirms the paper's positioning: the contribution is the problem formulation and empirical findings, not a competition for SOTA — simple features suffice for the task.\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"Length confound analysis: (A) length distributions by depth, (B) length-normalized features, (C) length-matched classification. Critical confound control.\\n\",\n    \"results\": {\n      \"mean_length_gen0\": 315,\n      \"mean_length_gen1\": 289,\n      \"mean_length_gen2\": 263,\n      \"mean_length_gen3\": 246,\n      \"mean_length_gen4\": 237,\n      \"length_depth_pearson_r\": -0.41,\n      \"length_depth_kw_p\": \"<0.001\",\n      \"original_surface_f1\": 0.76,\n      \"length_controlled_surface_f1\": 0.71,\n      \"length_controlled_surface_f1_delta\": -0.05,\n      \"original_reference_f1\": 0.72,\n      \"length_controlled_reference_f1\": 0.7,\n      \"length_controlled_reference_f1_delta\": -0.02,\n      \"original_full_f1\": 0.82,\n      \"length_controlled_full_f1\": 0.78,\n      \"length_controlled_full_f1_delta\": -0.04,\n      \"length_matched_subsample_full_f1\": 0.79,\n      \"fixed_window_ttr_slope\": -0.048,\n      \"fixed_window_ttr_original_slope\": -0.071,\n      \"fixed_window_hapax_slope\": -0.037,\n      \"fixed_window_hapax_original_slope\": -0.054,\n      \"residual_signal_confirmed\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 18: Text Length by Depth\",\n        \"columns\": [\n          \"depth\",\n          \"mean_tokens\",\n          \"std_tokens\",\n          \"median_tokens\"\n        ],\n        \"rows\": [\n          [\n            \"gen-0\",\n            315,\n            82,\n            298\n          ],\n          [\n            \"gen-1\",\n            289,\n            76,\n            274\n          ],\n          [\n            \"gen-2\",\n            263,\n            71,\n            251\n          ],\n          [\n            \"gen-3\",\n            246,\n            68,\n            237\n          ],\n          [\n            \"gen-4\",\n            237,\n            65,\n            228\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 19: Length-Controlled Classification Results\",\n        \"columns\": [\n          \"feature_set\",\n          \"original_f1\",\n          \"length_controlled_f1\",\n          \"delta\",\n          \"delta %\"\n        ],\n        \"rows\": [\n          [\n            \"Full\",\n            0.82,\n            0.78,\n            -0.04,\n            \"-4.9%\"\n          ],\n          [\n            \"Surface only\",\n            0.76,\n            0.71,\n            -0.05,\n            \"-6.6%\"\n          ],\n          [\n            \"Reference only\",\n            0.72,\n            0.7,\n            -0.02,\n            \"-2.8%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 20: Fixed-Window Feature Slopes (128-token windows)\",\n        \"columns\": [\n          \"feature\",\n          \"original_slope\",\n          \"fixed_window_slope\",\n          \"slope_reduction_pct\"\n        ],\n        \"rows\": [\n          [\n            \"TTR\",\n            -0.071,\n            -0.048,\n            \"32%\"\n          ],\n          [\n            \"hapax_ratio\",\n            -0.054,\n            -0.037,\n            \"31%\"\n          ],\n          [\n            \"entropy_mean\",\n            -0.148,\n            -0.139,\n            \"6%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length is a real but partial confound. The 0.05 surface F1 drop is within the median range [-0.08, -0.03] and must be acknowledged honestly in the paper. The key finding is that residual signal survives: depth drives genuine distributional drift beyond length artifacts. Reference features are relatively length-robust (only 0.02 drop), strengthening their value in the feature set. Paper should add length-controlled analysis as a supplementary validation table and note: 'Surface features partially track text length, but residual depth signal persists after length control. Reference features provide length-robust complementary signal.'\\n\\n\\nText length decreases monotonically with depth (315→237 tokens) because recursive generation tends to produce slightly shorter texts — generators are biased toward completing thoughts within a typical output length, and each depth step compounds this tendency. This creates a legitimate confound: TTR and hapax_ratio are mechanically length-dependent (shorter texts have higher TTR/hapax by construction). The -0.05 surface F1 drop after length control confirms that ~30% of the surface feature signal was tracking length, not depth. However, the residual signal (F1 0.71 after control, well above chance at 0.33) confirms that depth drives genuine vocabulary impoverishment beyond what length explains. Reference features lose less (-0.02) because NLL statistics are computed token-by-token and are less length-sensitive — the per-token surprise distribution shifts with depth regardless of total text length. The full-feature length-controlled F1 (0.78) remains substantially above chance and above either feature subset, confirming the core claims survive length control.\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"Add Qwen3-8B-Base as 7B+ generator. 1000 seeds × 5 depths. Tests whether depth signal persists at frontier scale.\\n\",\n    \"results\": {\n      \"qwen8b_3class_macro_f1\": 0.57,\n      \"qwen8b_gen0_f1\": 0.76,\n      \"qwen8b_gen1_f1\": 0.48,\n      \"qwen8b_gen2plus_f1\": 0.46,\n      \"qwen8b_entropy_mean_rho\": -0.38,\n      \"qwen8b_ttr_slope\": -0.042,\n      \"qwen8b_hapax_slope\": -0.032,\n      \"qwen8b_vs_pythia28b_f1_gap\": -0.25,\n      \"qwen8b_vs_qwen17b_f1_gap\": -0.05,\n      \"qwen8b_h1_features_stable\": true,\n      \"qwen8b_entropy_std_rho\": 0.05,\n      \"qwen8b_tail_decay_rho\": -0.07,\n      \"qwen8b_5class_f1\": 0.31,\n      \"logo_with_8b_included\": 0.61\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 21: 7B+ Generator Depth Classification\",\n        \"columns\": [\n          \"generator\",\n          \"params\",\n          \"macro_f1\",\n          \"entropy_mean_rho\",\n          \"ttr_slope\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-2.8B\",\n            \"2.8B\",\n            0.82,\n            -0.68,\n            -0.071\n          ],\n          [\n            \"Pythia-1B\",\n            \"1B\",\n            0.8,\n            -0.65,\n            -0.068\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"1.5B\",\n            0.78,\n            -0.61,\n            -0.063\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"1.7B\",\n            0.75,\n            -0.56,\n            -0.055\n          ],\n          [\n            \"Qwen3-0.6B\",\n            \"0.6B\",\n            0.77,\n            -0.59,\n            -0.061\n          ],\n          [\n            \"Qwen3-8B\",\n            \"8B\",\n            0.57,\n            -0.38,\n            -0.042\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 22: Scale Trend Analysis\",\n        \"columns\": [\n          \"metric\",\n          \"≤2.8B mean\",\n          \"8B\",\n          \"delta\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"macro_f1\",\n            0.78,\n            0.57,\n            -0.21,\n            \"Signal weakens at scale\"\n          ],\n          [\n            \"entropy_mean ρ\",\n            -0.62,\n            -0.38,\n            \"+0.24\",\n            \"Drift attenuates at scale\"\n          ],\n          [\n            \"TTR slope\",\n            -0.064,\n            -0.042,\n            \"+0.022\",\n            \"Less vocab impoverishment\"\n          ],\n          [\n            \"H1 max |ρ|\",\n            0.08,\n            0.07,\n            \"-0.01\",\n            \"Shape stationarity preserved\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B+ results confirm the scaling concern. Depth signal is weaker but non-zero (F1 0.57, significantly above chance p<0.001). The paper should present this as an honest scaling analysis in a dedicated subsection: 'Depth signal attenuates with generator scale, consistent with larger models maintaining distributional diversity under recursive generation. At 8B parameters, gen-0 vs synthetic remains detectable, but fine-grained depth estimation (gen-1 vs gen-2+) approaches noise floor. This motivates future work on scale-robust features, potentially leveraging model-specific distributional properties.' The 8B result transforms from a weakness into a scientific finding: the relationship between model capacity and depth signal decay is itself an interesting empirical contribution.\\n\\n7B+ generators produce substantially more fluent text that compresses the depth signal. At 8B parameters, the model has sufficient capacity to maintain diverse vocabulary and natural distributional properties even at depth-4 — vocabulary impoverishment is less severe because the model's larger vocabulary and richer internal representations allow it to produce varied continuations even from distributionally drifted inputs. The F1 drop from 0.82 (Pythia-2.8B) to 0.57 (Qwen3-8B) is large but the signal remains non-trivial (well above chance at 0.33). Entropy_mean ρ attenuates from -0.68 to -0.38, consistent with weaker but non-zero drift — the 8B model's NLL distribution still shifts with depth but less per step. Gen-0 remains distinguishable (F1 0.76) because the human-vs-any-synthetic gap is robust to model scale, but gen-1 vs gen-2+ becomes very noisy (0.46-0.48). H1 features remain stable (shape stationarity is scale-invariant). This is an honest scaling result: depth estimation weakens at scale but doesn't vanish, motivating future work on scale-robust features.\\n\"\n  }\n]",
      "numLines": 1209,
      "startLine": 1,
      "totalLines": 1209
    }
  },
  "sourceToolAssistantUUID": "b67790c2-fc31-4130-a695-85a30a1b4f8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "381e4406-8775-48a7-873d-b8a39b3a3bb1",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Assistant

_source line 16 · 2026-05-14T22:42:08.881Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write a comprehensive LaTeX paper. Let me first make sure the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "381e4406-8775-48a7-873d-b8a39b3a3bb1",
  "isSidechain": false,
  "requestId": "req_011Cb3GWHo6gia9K13ckq2bk",
  "type": "assistant",
  "uuid": "1a48fa47-8163-4abe-a765-99c855da3f1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eqtpS6qLCrqWECF2wQmrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 18114,
      "cache_read_input_tokens": 23134,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 170,
          "cache_read_input_tokens": 23134,
          "cache_creation_input_tokens": 18114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18114
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

_source line 17 · 2026-05-14T22:42:09.348Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a48fa47-8163-4abe-a765-99c855da3f1d",
  "isSidechain": false,
  "requestId": "req_011Cb3GWHo6gia9K13ckq2bk",
  "type": "assistant",
  "uuid": "7d5af0ef-b5ab-45de-bfbb-d5ee558a0f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eqtpS6qLCrqWECF2wQmrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 18114,
      "cache_read_input_tokens": 23134,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 170,
          "cache_read_input_tokens": 23134,
          "cache_creation_input_tokens": 18114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18114
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

_source line 18 · 2026-05-14T22:42:11.214Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XcRJyiGzW5DWbaJWsXFxBT`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d5af0ef-b5ab-45de-bfbb-d5ee558a0f84",
  "isSidechain": false,
  "requestId": "req_011Cb3GWHo6gia9K13ckq2bk",
  "type": "assistant",
  "uuid": "588fe8aa-ee9d-47d2-98ea-d3cbcf1f80dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eqtpS6qLCrqWECF2wQmrb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2721,
      "cache_creation_input_tokens": 18114,
      "cache_read_input_tokens": 23134,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2721,
          "output_tokens": 170,
          "cache_read_input_tokens": 23134,
          "cache_creation_input_tokens": 18114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18114
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

_source line 19 · 2026-05-14T22:42:11.336Z_

<details><summary>↩ Tool result · `toolu_01XcRJyiGzW5DWbaJWsXFxBT`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "588fe8aa-ee9d-47d2-98ea-d3cbcf1f80dc",
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "124f2f86-b0ad-4381-a37d-fdf2c6471230",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "588fe8aa-ee9d-47d2-98ea-d3cbcf1f80dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T22:45:36.635Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TocaiRuEK9Z5Tc7SQ52gU7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Distributional Fingerprinting for Generation Depth Estimation\\\\in Recursive LLM Output}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text whose \\emph{provenance depth}---how many successive generation steps separate it from the original human text---is unknown.\nCurrent detectors offer only binary real-vs-synthetic labels, forcing all-or-nothing filtering that discards useful near-human content or admits deeply degraded text.\nWe formulate \\textbf{generation depth estimation} as an ordinal classification task and propose a lightweight feature set combining surface diversity statistics with reference-model NLL summary statistics.\nOn continuation chains from six generators (0.6B--8B parameters) across four text domains, our features achieve macro-F1 0.82 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) within-generator and 0.64 under leave-one-generator-out evaluation.\nWe discover \\textbf{reference-model-modulated dual dynamics}: level/diversity features (entropy mean, TTR, hapax ratio) drift monotonically with depth while distributional shape features (entropy std, tail decay) remain near-stationary---a split determined by \\emph{what} the feature measures, not whether it derives from surface text or a reference model.\nThis dual pattern persists across reference models (though drift magnitude varies ${\\sim}2\\times$), prompt types, and text domains.\nDepth-aware data filtering improves downstream fine-tuning perplexity by 5.2\\% over unfiltered data, offering complementary signal to binary detection baselines.\nWe provide honest analysis of limitations: cross-generator generalization is moderate (LOGO F1 ${\\sim}$0.64), signal weakens at 7B+ scale (F1 0.57), and depth estimation is sensitive to heavy post-editing.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models are now prolific content generators on the open web.\nAs web-scraped corpora feed back into model training, the recursive loop produces text at varying \\emph{generation depths}: depth-0 text is human-authored, depth-1 is generated from a human seed, depth-2 is generated from depth-1 output, and so on.\nModel collapse theory demonstrates that training on such recursively generated data degrades model quality, with deeper-generation text contributing disproportionately to distributional drift.\n\nExisting detection methods---FastDetectGPT, SynthID-Text, LD-Score, Binoculars---provide binary real-vs-synthetic labels.\nThis binary view forces a coarse filtering strategy: discard all flagged text (losing useful gen-1 content that closely resembles human writing) or keep everything (admitting high-risk deep-generation text with compounding artifacts).\nA more nuanced approach would \\emph{estimate} generation depth, enabling risk-stratified data curation that retains near-human content while filtering deeply degraded text.\n\nAttractor cycle theory for paraphrasing chains shows that iterative paraphrasing converges to 2-period cycles, bounding distinguishable depth to ${\\sim}$3 classes.\nHowever, this result depends on the semantic-preservation constraint inherent to paraphrasing.\nNon-paraphrastic generation (continuation, elaboration) escapes this constraint, potentially supporting richer depth signal.\n\nWe make three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Problem formulation.} We define generation depth estimation as an ordinal classification task and construct multi-generator, multi-domain evaluation benchmarks with systematic controls.\n\n\\item \\textbf{Empirical discovery: reference-model-modulated dual dynamics.} We show that distributional features split into two families by \\emph{what they measure}---level/diversity features drift with depth (H$_2$) while shape features remain stationary (H$_1$)---a split that cross-cuts the surface/reference boundary. This dual pattern is modulated by reference model choice: entropy mean drift attenuates from $|\\rho|{=}0.68$ (same-family reference) to $|\\rho|{\\sim}0.4$ (cross-family reference), but the level-vs-shape split itself is preserved.\n\n\\item \\textbf{Practical application.} Depth-aware filtering provides complementary signal to binary detection for downstream data curation, with a 5.2\\% perplexity improvement over unfiltered training data.\n\\end{enumerate}\n\nOur contribution is primarily empirical and conceptual.\nThe features (NLL summary statistics, lexical diversity) and classifier (gradient-boosted trees) are standard; the novelty lies in the problem formulation, the empirical finding of dual dynamics, and the application to risk-stratified curation.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic text detection.}\nPerplexity-based methods detect machine-generated text via reference-model statistics: GLTR uses token-rank histograms, DetectGPT exploits log-probability curvature, Fast-DetectGPT replaces perturbation with conditional probability, Binoculars uses cross-model perplexity ratios, and DNA-GPT leverages divergent n-gram analysis.\nThese methods provide binary labels without depth information.\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical work demonstrates that training on model-generated data induces distributional collapse.\nAlemohammad et al.\\ show autophagous loops amplify bias; Dohmatob et al.\\ characterize the curse of recursion in Gaussian settings; Gerstgrasser et al.\\ extend results to LLMs; Guo et al.\\ quantify vocabulary impoverishment under recursive generation.\nThese results motivate depth estimation: not all synthetic text is equally harmful.\n\n\\paragraph{Attractor cycles.}\nRecent work proves that iterated paraphrasing converges to short-period cycles, bounding the distinguishable depth of paraphrastic chains.\nWe complement this theory by studying non-paraphrastic chains where the attractor bound does not apply (Section~\\ref{sec:paraphrastic}).\n\n\\paragraph{Data quality scoring.}\nMethods like DSIR, QuRating, and CCNet score training data quality for filtering.\nOur depth estimation provides a complementary contamination-risk signal orthogonal to topic/quality scores.\n\n\\paragraph{Lexical diversity and OOD detection.}\nOur surface features (TTR, hapax ratio) connect to vocabulary diversity metrics studied in computational linguistics.\nReference-model NLL statistics are functionally related to OOD detection scores.\nOur contribution is not the features themselves but the discovery that they exhibit dual dynamics under recursive generation and their application to ordinal depth estimation.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\nGiven a text passage $x$ of unknown provenance, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d{=}0$ denotes human-authored text and $d{=}k$ ($k{\\geq}1$) denotes text produced by the $k$-th step of a recursive LLM generation chain.\nWe frame this as ordinal classification with three ordered classes: gen-0, gen-1, and gen-2+.\n\n\\subsection{Generation Chain Construction}\n\\label{sec:chains}\nStarting from human-authored seed texts (depth-0), we construct generation chains by iteratively prompting an LLM to continue the previous output.\nEach chain produces texts at depths 0 through 4.\nWe use six generators spanning three model families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, and Qwen3-8B.\nSeed texts are drawn from four domains: Wikipedia, news (CNN/DailyMail), scientific abstracts (S2ORC), and creative writing (WritingPrompts).\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\nWe extract seven features from each text passage, organized by the dual dynamics framework:\n\n\\paragraph{H$_2$ (level/drift) features.}\nThese features measure central tendency or diversity and drift monotonically with depth:\n\\begin{itemize}\n\\item \\texttt{entropy\\_mean}: Mean per-token NLL under a reference model (Pythia-410M). Despite being a reference-model feature, it drifts because it measures the \\emph{level} (central tendency) of the NLL distribution.\n\\item \\texttt{TTR}: Type-token ratio, measuring vocabulary diversity.\n\\item \\texttt{hapax\\_ratio}: Proportion of words appearing exactly once.\n\\end{itemize}\n\n\\paragraph{H$_1$ (shape/stationary) features.}\nThese features measure distributional shape and remain near-stationary across depths:\n\\begin{itemize}\n\\item \\texttt{entropy\\_std}: Standard deviation of per-token NLL.\n\\item \\texttt{entropy\\_max}: Maximum per-token NLL.\n\\item \\texttt{tail\\_decay}: Rate of NLL distribution tail decay.\n\\item \\texttt{entropy\\_min}: Minimum per-token NLL.\n\\end{itemize}\n\n\\subsection{Classifier}\nWe use XGBoost with 5-fold stratified cross-validation.\nFor cross-generator evaluation, we employ leave-one-generator-out (LOGO) and leave-one-family-out (LOFO) protocols.\nAll reported metrics are macro-averaged F1 with bootstrap 95\\% confidence intervals from 1000 resamples.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Feature Ablation and Dual Dynamics (Within-Generator)}\n\\label{sec:ablation}\n\nWe first validate the feature set and dual dynamics hypothesis on a controlled within-generator setting: Pythia-2.8B as generator, Pythia-410M as reference model, $N{=}4{,}609$ chain samples.\n\n\\paragraph{Feature ablation.}\nTable~\\ref{tab:ablation} reports 3-class depth classification results.\nThe full 7-feature set achieves macro-F1 0.82 [0.804, 0.836], significantly outperforming both surface-only (TTR + hapax; F1 0.76 [0.747, 0.774]) and reference-only (5 NLL statistics; F1 0.72 [0.706, 0.733]).\nThe non-overlapping bootstrap CIs confirm that combining drifting and stationary features yields statistically significant improvement over either alone.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B generator, $N{=}4{,}609$).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Macro-F1 & 95\\% CI & Gen-0 & Gen-1 \\\\\n\\midrule\nFull (7 features) & 0.82 & [0.804, 0.836] & 0.94 & 0.77 \\\\\nSurface only (TTR + hapax) & 0.76 & [0.747, 0.774] & 0.91 & 0.70 \\\\\nReference only (5 NLL) & 0.72 & [0.706, 0.733] & 0.88 & 0.65 \\\\\nChance baseline & 0.33 & --- & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{H$_1$/H$_2$ trend analysis.}\nTable~\\ref{tab:trends} reports per-feature linear regression of feature values against depth.\nH$_2$ features exhibit strong monotonic drift: entropy\\_mean ($R^2{=}0.93$, slope $-0.148$), TTR ($R^2{=}0.87$, slope $-0.071$), hapax\\_ratio ($R^2{=}0.81$, slope $-0.054$), all with $p{<}0.001$.\nH$_1$ features show negligible trends: entropy\\_std ($R^2{=}0.02$), entropy\\_max ($R^2{=}0.04$), tail\\_decay ($R^2{=}0.03$), entropy\\_min ($R^2{=}0.06$), all with $p{>}0.19$.\nThis confirms the dual dynamics split.\n\n\\begin{table}[h]\n\\centering\n\\caption{H$_1$/H$_2$ trend regression per feature (Pythia-2.8B chains).}\n\\label{tab:trends}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Slope & $R^2$ & $p$-value & Class \\\\\n\\midrule\nentropy\\_mean & $-0.148$ & 0.93 & ${<}0.001$ & H$_2$ (drift) \\\\\nTTR & $-0.071$ & 0.87 & ${<}0.001$ & H$_2$ (drift) \\\\\nhapax\\_ratio & $-0.054$ & 0.81 & ${<}0.001$ & H$_2$ (drift) \\\\\n\\midrule\nentropy\\_std & $+0.003$ & 0.02 & $0.41$ & H$_1$ (stationary) \\\\\nentropy\\_max & $-0.009$ & 0.04 & $0.28$ & H$_1$ (stationary) \\\\\ntail\\_decay & $+0.005$ & 0.03 & $0.33$ & H$_1$ (stationary) \\\\\nentropy\\_min & $-0.012$ & 0.06 & $0.19$ & H$_1$ (stationary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMedian perplexity by depth (13.5, 4.96, 3.00, 2.07, 1.72 for gen-0 through gen-4; Kruskal--Wallis $p{<}0.001$) confirms that the reference model's surprise decreases monotonically with depth---deeper-generation text becomes more predictable as it converges toward the generator's mode.\n\n% ----------------------------------------------------------\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate on five generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) with 1{,}000 seeds per generator $\\times$ 5 depths, yielding 21{,}503 chains after quality-based attrition from 23{,}847 generated.\n\n\\paragraph{Leave-one-generator-out (LOGO).}\nTable~\\ref{tab:logo} reports LOGO results.\nMean LOGO F1 is 0.64, confirming moderate cross-generator generalization.\nPythia-family holdouts achieve higher F1 (0.71--0.72) because the remaining Pythia generator provides an in-family proxy; OLMo and Qwen holdouts score lower (0.59--0.62).\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-generator-out results (full features).}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-out Generator & Family & F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nPythia-2.8B & Pythia & 0.71 & 0.87 & 0.64 & 0.66 \\\\\nPythia-1B & Pythia & 0.72 & 0.88 & 0.66 & 0.67 \\\\\nOLMo-2-1B & OLMo & 0.60 & 0.79 & 0.51 & 0.53 \\\\\nQwen3-1.7B & Qwen & 0.62 & 0.82 & 0.53 & 0.55 \\\\\nQwen3-0.6B & Qwen & 0.59 & 0.78 & 0.50 & 0.51 \\\\\n\\midrule\n\\textbf{Mean LOGO} & --- & \\textbf{0.64} & 0.83 & 0.57 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-family-out (LOFO).}\nLOFO evaluates generalization when no same-family generator remains in training: Pythia family F1 0.58 [0.55, 0.61], OLMo F1 0.61 [0.57, 0.64], Qwen F1 0.59 [0.56, 0.62], mean 0.593.\nThe ${\\sim}$0.05 LOFO--LOGO gap quantifies the within-family transfer advantage.\n\n\\paragraph{Feature ablation under LOGO.}\nUnder LOGO, the full-vs-surface gap narrows from 0.06 (within-generator) to 0.03 (LOGO F1: full 0.64, surface-only 0.61, reference-only 0.58).\nThis suggests the Pythia-410M reference model's advantage is partially family-specific.\n\n% ----------------------------------------------------------\n\\subsection{Reference Model Modulation of Dual Dynamics}\n\\label{sec:cross_ref}\n\nTo test whether dual dynamics depends on reference model choice, we recompute NLL features using OLMo-2-1B and Qwen3-0.6B as alternative reference models on the same chain data.\n\n\\paragraph{Drift attenuation.}\nTable~\\ref{tab:ref_drift} shows entropy\\_mean drift across references.\nThe Spearman $\\rho$ attenuates from $-0.68$ (Pythia-410M, same-family) to $-0.42$ (OLMo-2-1B) and $-0.36$ (Qwen3-0.6B), all $p{<}0.001$.\nThe drift is real and universal---deeper text is always more predictable to \\emph{any} reference model---but the measurement sensitivity depends on reference--generator alignment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Entropy\\_mean drift ($\\rho$) by reference model.}\n\\label{tab:ref_drift}\n\\begin{tabular}{lccc}\n\\toprule\nReference Model & $\\rho$ (entropy\\_mean) & $p$-value & Full F1 \\\\\n\\midrule\nPythia-410M & $-0.68$ & ${<}0.001$ & 0.82 \\\\\nOLMo-2-1B & $-0.42$ & ${<}0.001$ & 0.78 \\\\\nQwen3-0.6B & $-0.36$ & ${<}0.001$ & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Shape stationarity preserved.}\nShape features remain H$_1$ across all reference models: max $|\\rho|$ is 0.08 (Pythia-410M), 0.11 (OLMo-2-1B), and 0.09 (Qwen3-0.6B).\nThe level-vs-shape split is intrinsic to what the feature measures, not an artifact of reference model choice.\n\nCross-reference LOGO F1 with non-Pythia references (OLMo-ref: 0.61; Qwen-ref: 0.58) shows depth estimation remains viable with any reference model, though at reduced accuracy.\n\n% ----------------------------------------------------------\n\\subsection{Text Length Confound Analysis}\n\\label{sec:length}\n\nText length decreases monotonically with depth (mean tokens: 315, 289, 263, 246, 237 for gen-0 through gen-4; Pearson $r{=}-0.41$, $p{<}0.001$), creating a potential confound for length-sensitive surface features.\n\n\\paragraph{Length-controlled classification.}\nTable~\\ref{tab:length_control} reports results after length normalization and length-matched subsampling.\nSurface-only F1 drops by 0.05 (from 0.76 to 0.71), confirming that ${\\sim}$30\\% of the surface signal tracked length.\nReference-only features are relatively robust ($-0.02$).\nCrucially, full-feature F1 after length control remains at 0.78---well above chance and above either feature subset---confirming that depth drives genuine distributional drift beyond length artifacts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Length-controlled classification results.}\n\\label{tab:length_control}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Original F1 & Controlled F1 & $\\Delta$ & $\\Delta$\\% \\\\\n\\midrule\nFull & 0.82 & 0.78 & $-0.04$ & $-4.9$\\% \\\\\nSurface only & 0.76 & 0.71 & $-0.05$ & $-6.6$\\% \\\\\nReference only & 0.72 & 0.70 & $-0.02$ & $-2.8$\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFixed-window analysis (128-token windows) reduces TTR slope by 32\\% ($-0.071 \\to -0.048$) and hapax slope by 31\\% ($-0.054 \\to -0.037$), while entropy\\_mean slope is barely affected ($-0.148 \\to -0.139$, 6\\% reduction).\nThis confirms that reference-model features provide length-robust depth signal.\n\n% ----------------------------------------------------------\n\\subsection{Prompt Type and Chain Type Variations}\n\\label{sec:prompt}\n\n\\paragraph{Prompt types.}\nTable~\\ref{tab:prompt} compares depth classification across three prompting strategies on Pythia-2.8B chains.\nContinuation yields the strongest signal (F1 0.82, $\\rho{=}-0.68$); elaboration is moderate (F1 0.77, $\\rho{=}-0.57$); inspired rewriting is weakest (F1 0.69, $\\rho{=}-0.39$).\nThe monotonic decrease tracks semantic divergence from source (cosine similarity: 0.85, 0.72, 0.54).\nH$_1$ features remain stable across all prompt types.\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by prompt type (Pythia-2.8B, 5-fold CV).}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\nPrompt Type & Macro-F1 & $\\rho$ (ent\\_mean) & TTR slope & Sem.\\ div.\\ $\\cos$ \\\\\n\\midrule\nContinuation & 0.82 & $-0.68$ & $-0.071$ & 0.85 \\\\\nElaboration & 0.77 & $-0.57$ & $-0.058$ & 0.72 \\\\\nInspired rewriting & 0.69 & $-0.39$ & $-0.031$ & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs non-paraphrastic chains.}\n\\label{sec:paraphrastic}\nParaphrastic chains hit the attractor bound at depth ${\\sim}$2, yielding 3-class F1 of only 0.66 (vs 0.82 for non-paraphrastic).\nThe gen-2+ F1 collapses to 0.41 (vs 0.79), and entropy\\_mean $\\rho$ attenuates to $-0.34$ (vs $-0.68$).\nThis validates our focus on non-paraphrastic chains: the attractor convergence bound constrains paraphrasing but not continuation.\n\n\\paragraph{Cross-model chains.}\nWhen different generators produce each depth step (mimicking realistic web contamination), LOGO F1 drops from 0.64 to 0.56.\nThe generator-switching noise partially masks depth signal, particularly for gen-1 vs gen-2+ (F1: 0.46 and 0.44).\nGen-0 identification remains robust (F1 0.78) because all chains share human seeds.\nH$_1$ features remain stable even under cross-model chains.\n\n% ----------------------------------------------------------\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domain}\n\nTable~\\ref{tab:domain} reports LOGO results across four seed domains.\nWikipedia yields the highest F1 (0.67), consistent with its stylistic uniformity; creative writing is hardest (F1 0.57) due to high intrinsic variance.\nPooled multi-domain LOGO F1 is 0.63 with moderate cross-domain variability (std 0.037).\nCross-domain train-test (train on 3 domains, test on 1) drops to 0.58, indicating partial domain adaptation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-specific LOGO results.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & LOGO F1 & $\\rho$ (ent\\_mean) & TTR slope & Seeds \\\\\n\\midrule\nWikipedia & 0.67 & $-0.72$ & $-0.078$ & 500 \\\\\nNews (CNN/DM) & 0.64 & $-0.63$ & $-0.065$ & 500 \\\\\nScientific (S2ORC) & 0.62 & $-0.58$ & $-0.059$ & 500 \\\\\nCreative (WritingPrompts) & 0.57 & $-0.48$ & $-0.041$ & 500 \\\\\n\\midrule\nPooled & 0.63 & $-0.60$ & $-0.061$ & 2000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ----------------------------------------------------------\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nExtending to 5-class ordinal classification (gen-0 through gen-4) under LOGO yields macro-F1 0.43.\nGen-0 is still well-separated (F1 0.73), gen-1 is intermediate (0.52), but gen-2/3/4 collapse into a cluster (F1: 0.35, 0.29, 0.28).\nErrors are predominantly between adjacent classes (61\\% of misclassifications).\nDespite low per-class accuracy for deep generations, ordinal Spearman correlation between predicted and true depth is 0.74, showing the classifier preserves depth ordering---useful for risk scoring even when exact classification fails.\nThe 3-class grouping (gen-0\\,/\\,gen-1\\,/\\,gen-2+) appears to be the natural resolution supported by the current feature set.\n\n% ----------------------------------------------------------\n\\subsection{Robustness to Human Editing}\n\\label{sec:robustness}\n\nTable~\\ref{tab:edit} reports robustness to simulated post-editing.\nAt 5\\% random word replacement, F1 drops only 0.03 (to 0.79).\nAt 10\\%, the drop is more substantial ($-0.10$).\nAt 20\\%, depth signal degrades significantly ($-0.22$, F1 0.60).\nLLM-simulated light rephrasing (${\\sim}$8\\% effective edit rate) produces a $-0.09$ drop (F1 0.73), falling between the 5\\% and 10\\% random replacement conditions.\nShape features remain robust across all conditions (max $|\\rho|$ change: 0.07).\nReal-world human editing likely falls in the 5--15\\% range, placing expected operational F1 at 0.72--0.79.\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to simulated human edits (Pythia-2.8B, within-generator).}\n\\label{tab:edit}\n\\begin{tabular}{llccc}\n\\toprule\nEdit Type & Rate & Macro-F1 & $\\Delta$ F1 & $\\rho$ (ent\\_mean) \\\\\n\\midrule\nNone (baseline) & 0\\% & 0.82 & --- & $-0.68$ \\\\\nRandom word & 5\\% & 0.79 & $-0.03$ & $-0.63$ \\\\\nRandom word & 10\\% & 0.72 & $-0.10$ & $-0.52$ \\\\\nRandom word & 20\\% & 0.60 & $-0.22$ & $-0.35$ \\\\\nLLM light rephrase & ${\\sim}$8\\% & 0.73 & $-0.09$ & $-0.49$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ----------------------------------------------------------\n\\subsection{LD-Score as Pre-Registered Validation}\n\\label{sec:ldscore}\n\nAs a pre-registered test of the H$_1$/H$_2$ framework's predictive utility, we predicted that LD-Score (a character-level distributional signature) would behave as an H$_2$ level feature.\nThis prediction is confirmed: LD-Score exhibits depth-correlated drift ($\\rho{=}-0.55$, slope $-0.042$, $R^2{=}0.72$).\nHowever, it is highly correlated with existing surface features (0.68 with TTR, 0.61 with hapax\\_ratio) and provides negligible marginal classification improvement (F1: 0.83 vs 0.82 without).\nThis validates the framework's predictions while confirming that character-level and word-level diversity capture the same underlying depth signal.\n\n% ----------------------------------------------------------\n\\subsection{End-to-End Neural Baseline}\n\\label{sec:e2e}\n\nA QLoRA fine-tuned Qwen3-0.6B achieves within-generator F1 0.79 and LOGO F1 0.61, slightly underperforming the handcrafted feature set (0.82 and 0.64 respectively).\nThe end-to-end approach requires 6.2 GPU-hours of training and runs at 145 tokens/sec inference, versus near-zero training cost and 8{,}900 tokens/sec for the handcrafted features (${\\sim}60\\times$ faster).\nThis confirms that the depth classification task is well-served by simple distributional statistics; the information content is captured by lightweight features without requiring learned representations.\n\n% ----------------------------------------------------------\n\\subsection{Scaling Analysis: 7B+ Generators}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} summarizes depth classification performance by generator scale.\nQwen3-8B (8B parameters) achieves only F1 0.57---substantially below the ${\\leq}$2.8B mean of 0.78.\nEntropy\\_mean drift attenuates ($\\rho{=}-0.38$ vs mean $-0.62$ for smaller models) and TTR slope weakens ($-0.042$ vs $-0.064$), consistent with larger models maintaining more diverse vocabulary under recursive generation.\nGen-0 remains distinguishable (F1 0.76), but gen-1 vs gen-2+ approaches the noise floor (F1 0.46--0.48).\nH$_1$ shape stationarity is preserved at scale (max $|\\rho|{=}0.07$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by generator scale.}\n\\label{tab:scale}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & Params & Macro-F1 & $\\rho$ (ent\\_mean) & TTR slope \\\\\n\\midrule\nPythia-2.8B & 2.8B & 0.82 & $-0.68$ & $-0.071$ \\\\\nPythia-1B & 1B & 0.80 & $-0.65$ & $-0.068$ \\\\\nOLMo-2-1B & 1.5B & 0.78 & $-0.61$ & $-0.063$ \\\\\nQwen3-1.7B & 1.7B & 0.75 & $-0.56$ & $-0.055$ \\\\\nQwen3-0.6B & 0.6B & 0.77 & $-0.59$ & $-0.061$ \\\\\n\\midrule\nQwen3-8B & 8B & 0.57 & $-0.38$ & $-0.042$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe relationship between model capacity and depth signal decay is itself informative: larger models compress distributional drift more effectively, suggesting that scale-robust depth features may require model-specific calibration.\n\n% ----------------------------------------------------------\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B on depth-stratified data (3 seeds, bootstrap CIs) and compare depth-aware filtering against binary baselines.\n\n\\paragraph{Depth-stratified training quality.}\nTable~\\ref{tab:downstream} shows mean perplexity by training data composition.\nGen-0-only training achieves the lowest perplexity (18.4), gen-0+gen-1 is close (19.1), while including gen-2+ text degrades quality (21.7), approaching unfiltered (22.3).\nDepth-quality Spearman $\\rho{=}0.53$ [0.41, 0.64].\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream perplexity by training data composition (OLMo-1B, 3 seeds).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nTraining Data & $N$ & Mean PPL & 95\\% CI \\\\\n\\midrule\nGen-0 only & 4{,}850 & 18.4 & [17.9, 18.9] \\\\\nGen-0 + gen-1 & 9{,}700 & 19.1 & [18.5, 19.7] \\\\\nGen-0 + gen-1 + gen-2+ & 18{,}200 & 21.7 & [20.8, 22.6] \\\\\nUnfiltered & 21{,}500 & 22.3 & [21.5, 23.1] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comparison with binary baselines.}\nDepth-aware filtering (keep gen-0 + gen-1) yields 5.2\\% perplexity improvement [3.8, 7.1] over unfiltered data, compared to 3.8\\% [2.1, 5.9] for FastDetectGPT and 3.2\\% [1.6, 5.3] for LD-Score thresholding.\nUnder sample-matched comparison (controlling for data volume), the depth advantage narrows: 2.8\\% [1.4, 4.5] vs 1.9\\% [0.5, 3.6] for binary filtering.\nThe CIs overlap between depth-aware and the best binary baseline, precluding a ``significantly outperforms'' claim.\nDownstream task accuracy shows a consistent but modest pattern: 0.724 (depth-filtered), 0.711 (binary-filtered), 0.698 (unfiltered).\n\nThe practical value of depth estimation is not raw performance superiority over binary detection but the ability to retain useful gen-1 data---which binary detectors discard---while filtering harmful gen-2+ text.\nDepth scores also provide a continuous risk metric that binary labels cannot.\n\n% ============================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n\n\\paragraph{Honest assessment of generalization.}\nWithin-generator depth estimation is strong (F1 0.82), but cross-generator generalization is moderate (LOGO F1 0.64, LOFO F1 0.59).\nPerformance drops concentrate on out-of-family holdouts, indicating that current features partially encode generator identity alongside depth.\n\n\\paragraph{Reference model modulation.}\nThe dual dynamics pattern is robust---level features always drift, shape features always remain stationary---but the drift magnitude varies ${\\sim}2\\times$ depending on reference model choice.\nThis makes the H$_1$/H$_2$ split a ``reference-model-modulated'' phenomenon rather than a universal law.\nPractical deployment requires reference model selection.\n\n\\paragraph{Scale limitation.}\nAt 7B+ parameters, depth signal weakens substantially (F1 0.57).\nAs frontier models grow, current features may become insufficient for fine-grained depth estimation.\nScale-robust features---potentially leveraging model-specific distributional properties or training dynamics---are needed.\n\n\\paragraph{Ecological validity.}\nCross-model chains (F1 0.56), creative writing domains (F1 0.57), and inspired rewriting prompts (F1 0.69) all degrade performance, reflecting realistic conditions where depth estimation is most challenging.\nHeavy human editing (${>}$10\\%) further erodes signal.\nDepth estimation is most reliable for lightly edited, single-source continuation chains.\n\n\\paragraph{Downstream utility caveat.}\nWhile depth-aware filtering outperforms binary baselines on average, CIs overlap with the best binary baseline on some metrics.\nRoughly half the filtering advantage comes from retaining more training data (gen-1), not from better selection quality per se.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formulate generation depth estimation as a new task beyond binary synthetic text detection and provide systematic empirical evidence across six generators, four domains, and multiple evaluation protocols.\nOur key finding is \\emph{reference-model-modulated dual dynamics}: level/diversity features drift monotonically with depth while distributional shape features remain stationary, a split determined by what the feature measures rather than its source.\nThis pattern supports 3-class depth estimation at macro-F1 0.82 within-generator and 0.64 cross-generator, with practical utility for risk-stratified data curation.\n\nDepth estimation is feasible and useful, with initial evidence for dual dynamics as an organizing principle.\nSignificant challenges remain: cross-family generalization, scaling to frontier models, and robustness to realistic post-editing.\nThese limitations define clear directions for future work on generator-invariant features, scale-adaptive reference models, and integration with existing data curation pipelines.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Alemohammad et~al.(2023)]{alemohammad2023selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk.\n\\newblock Self-consuming generative models go MAD.\n\\newblock \\emph{arXiv preprint arXiv:2307.01850}, 2023.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.\n\\newblock Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024curse}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nYanzhu Guo, Guokan Shang, Mingxue Li, Chlo{\\'e} Clavel, and Michalis Vazirgiannis.\n\\newblock On the curious decline of linguistic diversity with scale: A study on LLM-generated text.\n\\newblock In \\emph{EMNLP Findings}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nAri Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn.\n\\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nSang~Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "124f2f86-b0ad-4381-a37d-fdf2c6471230",
  "isSidechain": false,
  "requestId": "req_011Cb3GWi1dWdgpfirmbYG9z",
  "type": "assistant",
  "uuid": "c0f54843-7efd-4f2f-836f-9c278d808605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrXeCUgFDqSUiQ6WLAm8oh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 41248,
      "output_tokens": 11049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11049,
          "cache_read_input_tokens": 41248,
          "cache_creation_input_tokens": 2908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2908
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

_source line 21 · 2026-05-14T22:45:36.649Z_

<details><summary>↩ Tool result · `toolu_01TocaiRuEK9Z5Tc7SQ52gU7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f54843-7efd-4f2f-836f-9c278d808605",
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "7a19e1fe-ad3f-4154-9a6c-430528f9f17d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Distributional Fingerprinting for Generation Depth Estimation\\\\in Recursive LLM Output}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text whose \\emph{provenance depth}---how many successive generation steps separate it from the original human text---is unknown.\nCurrent detectors offer only binary real-vs-synthetic labels, forcing all-or-nothing filtering that discards useful near-human content or admits deeply degraded text.\nWe formulate \\textbf{generation depth estimation} as an ordinal classification task and propose a lightweight feature set combining surface diversity statistics with reference-model NLL summary statistics.\nOn continuation chains from six generators (0.6B--8B parameters) across four text domains, our features achieve macro-F1 0.82 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) within-generator and 0.64 under leave-one-generator-out evaluation.\nWe discover \\textbf{reference-model-modulated dual dynamics}: level/diversity features (entropy mean, TTR, hapax ratio) drift monotonically with depth while distributional shape features (entropy std, tail decay) remain near-stationary---a split determined by \\emph{what} the feature measures, not whether it derives from surface text or a reference model.\nThis dual pattern persists across reference models (though drift magnitude varies ${\\sim}2\\times$), prompt types, and text domains.\nDepth-aware data filtering improves downstream fine-tuning perplexity by 5.2\\% over unfiltered data, offering complementary signal to binary detection baselines.\nWe provide honest analysis of limitations: cross-generator generalization is moderate (LOGO F1 ${\\sim}$0.64), signal weakens at 7B+ scale (F1 0.57), and depth estimation is sensitive to heavy post-editing.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models are now prolific content generators on the open web.\nAs web-scraped corpora feed back into model training, the recursive loop produces text at varying \\emph{generation depths}: depth-0 text is human-authored, depth-1 is generated from a human seed, depth-2 is generated from depth-1 output, and so on.\nModel collapse theory demonstrates that training on such recursively generated data degrades model quality, with deeper-generation text contributing disproportionately to distributional drift.\n\nExisting detection methods---FastDetectGPT, SynthID-Text, LD-Score, Binoculars---provide binary real-vs-synthetic labels.\nThis binary view forces a coarse filtering strategy: discard all flagged text (losing useful gen-1 content that closely resembles human writing) or keep everything (admitting high-risk deep-generation text with compounding artifacts).\nA more nuanced approach would \\emph{estimate} generation depth, enabling risk-stratified data curation that retains near-human content while filtering deeply degraded text.\n\nAttractor cycle theory for paraphrasing chains shows that iterative paraphrasing converges to 2-period cycles, bounding distinguishable depth to ${\\sim}$3 classes.\nHowever, this result depends on the semantic-preservation constraint inherent to paraphrasing.\nNon-paraphrastic generation (continuation, elaboration) escapes this constraint, potentially supporting richer depth signal.\n\nWe make three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{Problem formulation.} We define generation depth estimation as an ordinal classification task and construct multi-generator, multi-domain evaluation benchmarks with systematic controls.\n\n\\item \\textbf{Empirical discovery: reference-model-modulated dual dynamics.} We show that distributional features split into two families by \\emph{what they measure}---level/diversity features drift with depth (H$_2$) while shape features remain stationary (H$_1$)---a split that cross-cuts the surface/reference boundary. This dual pattern is modulated by reference model choice: entropy mean drift attenuates from $|\\rho|{=}0.68$ (same-family reference) to $|\\rho|{\\sim}0.4$ (cross-family reference), but the level-vs-shape split itself is preserved.\n\n\\item \\textbf{Practical application.} Depth-aware filtering provides complementary signal to binary detection for downstream data curation, with a 5.2\\% perplexity improvement over unfiltered training data.\n\\end{enumerate}\n\nOur contribution is primarily empirical and conceptual.\nThe features (NLL summary statistics, lexical diversity) and classifier (gradient-boosted trees) are standard; the novelty lies in the problem formulation, the empirical finding of dual dynamics, and the application to risk-stratified curation.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic text detection.}\nPerplexity-based methods detect machine-generated text via reference-model statistics: GLTR uses token-rank histograms, DetectGPT exploits log-probability curvature, Fast-DetectGPT replaces perturbation with conditional probability, Binoculars uses cross-model perplexity ratios, and DNA-GPT leverages divergent n-gram analysis.\nThese methods provide binary labels without depth information.\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical work demonstrates that training on model-generated data induces distributional collapse.\nAlemohammad et al.\\ show autophagous loops amplify bias; Dohmatob et al.\\ characterize the curse of recursion in Gaussian settings; Gerstgrasser et al.\\ extend results to LLMs; Guo et al.\\ quantify vocabulary impoverishment under recursive generation.\nThese results motivate depth estimation: not all synthetic text is equally harmful.\n\n\\paragraph{Attractor cycles.}\nRecent work proves that iterated paraphrasing converges to short-period cycles, bounding the distinguishable depth of paraphrastic chains.\nWe complement this theory by studying non-paraphrastic chains where the attractor bound does not apply (Section~\\ref{sec:paraphrastic}).\n\n\\paragraph{Data quality scoring.}\nMethods like DSIR, QuRating, and CCNet score training data quality for filtering.\nOur depth estimation provides a complementary contamination-risk signal orthogonal to topic/quality scores.\n\n\\paragraph{Lexical diversity and OOD detection.}\nOur surface features (TTR, hapax ratio) connect to vocabulary diversity metrics studied in computational linguistics.\nReference-model NLL statistics are functionally related to OOD detection scores.\nOur contribution is not the features themselves but the discovery that they exhibit dual dynamics under recursive generation and their application to ordinal depth estimation.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\nGiven a text passage $x$ of unknown provenance, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$, where $d{=}0$ denotes human-authored text and $d{=}k$ ($k{\\geq}1$) denotes text produced by the $k$-th step of a recursive LLM generation chain.\nWe frame this as ordinal classification with three ordered classes: gen-0, gen-1, and gen-2+.\n\n\\subsection{Generation Chain Construction}\n\\label{sec:chains}\nStarting from human-authored seed texts (depth-0), we construct generation chains by iteratively prompting an LLM to continue the previous output.\nEach chain produces texts at depths 0 through 4.\nWe use six generators spanning three model families: Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B, and Qwen3-8B.\nSeed texts are drawn from four domains: Wikipedia, news (CNN/DailyMail), scientific abstracts (S2ORC), and creative writing (WritingPrompts).\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\nWe extract seven features from each text passage, organized by the dual dynamics framework:\n\n\\paragraph{H$_2$ (level/drift) features.}\nThese features measure central tendency or diversity and drift monotonically with depth:\n\\begin{itemize}\n\\item \\texttt{entropy\\_mean}: Mean per-token NLL under a reference model (Pythia-410M). Despite being a reference-model feature, it drifts because it measures the \\emph{level} (central tendency) of the NLL distribution.\n\\item \\texttt{TTR}: Type-token ratio, measuring vocabulary diversity.\n\\item \\texttt{hapax\\_ratio}: Proportion of words appearing exactly once.\n\\end{itemize}\n\n\\paragraph{H$_1$ (shape/stationary) features.}\nThese features measure distributional shape and remain near-stationary across depths:\n\\begin{itemize}\n\\item \\texttt{entropy\\_std}: Standard deviation of per-token NLL.\n\\item \\texttt{entropy\\_max}: Maximum per-token NLL.\n\\item \\texttt{tail\\_decay}: Rate of NLL distribution tail decay.\n\\item \\texttt{entropy\\_min}: Minimum per-token NLL.\n\\end{itemize}\n\n\\subsection{Classifier}\nWe use XGBoost with 5-fold stratified cross-validation.\nFor cross-generator evaluation, we employ leave-one-generator-out (LOGO) and leave-one-family-out (LOFO) protocols.\nAll reported metrics are macro-averaged F1 with bootstrap 95\\% confidence intervals from 1000 resamples.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Feature Ablation and Dual Dynamics (Within-Generator)}\n\\label{sec:ablation}\n\nWe first validate the feature set and dual dynamics hypothesis on a controlled within-generator setting: Pythia-2.8B as generator, Pythia-410M as reference model, $N{=}4{,}609$ chain samples.\n\n\\paragraph{Feature ablation.}\nTable~\\ref{tab:ablation} reports 3-class depth classification results.\nThe full 7-feature set achieves macro-F1 0.82 [0.804, 0.836], significantly outperforming both surface-only (TTR + hapax; F1 0.76 [0.747, 0.774]) and reference-only (5 NLL statistics; F1 0.72 [0.706, 0.733]).\nThe non-overlapping bootstrap CIs confirm that combining drifting and stationary features yields statistically significant improvement over either alone.\n\n\\begin{table}[h]\n\\centering\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B generator, $N{=}4{,}609$).}\n\\label{tab:ablation}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Macro-F1 & 95\\% CI & Gen-0 & Gen-1 \\\\\n\\midrule\nFull (7 features) & 0.82 & [0.804, 0.836] & 0.94 & 0.77 \\\\\nSurface only (TTR + hapax) & 0.76 & [0.747, 0.774] & 0.91 & 0.70 \\\\\nReference only (5 NLL) & 0.72 & [0.706, 0.733] & 0.88 & 0.65 \\\\\nChance baseline & 0.33 & --- & 0.33 & 0.33 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{H$_1$/H$_2$ trend analysis.}\nTable~\\ref{tab:trends} reports per-feature linear regression of feature values against depth.\nH$_2$ features exhibit strong monotonic drift: entropy\\_mean ($R^2{=}0.93$, slope $-0.148$), TTR ($R^2{=}0.87$, slope $-0.071$), hapax\\_ratio ($R^2{=}0.81$, slope $-0.054$), all with $p{<}0.001$.\nH$_1$ features show negligible trends: entropy\\_std ($R^2{=}0.02$), entropy\\_max ($R^2{=}0.04$), tail\\_decay ($R^2{=}0.03$), entropy\\_min ($R^2{=}0.06$), all with $p{>}0.19$.\nThis confirms the dual dynamics split.\n\n\\begin{table}[h]\n\\centering\n\\caption{H$_1$/H$_2$ trend regression per feature (Pythia-2.8B chains).}\n\\label{tab:trends}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature & Slope & $R^2$ & $p$-value & Class \\\\\n\\midrule\nentropy\\_mean & $-0.148$ & 0.93 & ${<}0.001$ & H$_2$ (drift) \\\\\nTTR & $-0.071$ & 0.87 & ${<}0.001$ & H$_2$ (drift) \\\\\nhapax\\_ratio & $-0.054$ & 0.81 & ${<}0.001$ & H$_2$ (drift) \\\\\n\\midrule\nentropy\\_std & $+0.003$ & 0.02 & $0.41$ & H$_1$ (stationary) \\\\\nentropy\\_max & $-0.009$ & 0.04 & $0.28$ & H$_1$ (stationary) \\\\\ntail\\_decay & $+0.005$ & 0.03 & $0.33$ & H$_1$ (stationary) \\\\\nentropy\\_min & $-0.012$ & 0.06 & $0.19$ & H$_1$ (stationary) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMedian perplexity by depth (13.5, 4.96, 3.00, 2.07, 1.72 for gen-0 through gen-4; Kruskal--Wallis $p{<}0.001$) confirms that the reference model's surprise decreases monotonically with depth---deeper-generation text becomes more predictable as it converges toward the generator's mode.\n\n% ----------------------------------------------------------\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate on five generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B) with 1{,}000 seeds per generator $\\times$ 5 depths, yielding 21{,}503 chains after quality-based attrition from 23{,}847 generated.\n\n\\paragraph{Leave-one-generator-out (LOGO).}\nTable~\\ref{tab:logo} reports LOGO results.\nMean LOGO F1 is 0.64, confirming moderate cross-generator generalization.\nPythia-family holdouts achieve higher F1 (0.71--0.72) because the remaining Pythia generator provides an in-family proxy; OLMo and Qwen holdouts score lower (0.59--0.62).\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-generator-out results (full features).}\n\\label{tab:logo}\n\\begin{tabular}{llcccc}\n\\toprule\nHeld-out Generator & Family & F1 & Gen-0 & Gen-1 & Gen-2+ \\\\\n\\midrule\nPythia-2.8B & Pythia & 0.71 & 0.87 & 0.64 & 0.66 \\\\\nPythia-1B & Pythia & 0.72 & 0.88 & 0.66 & 0.67 \\\\\nOLMo-2-1B & OLMo & 0.60 & 0.79 & 0.51 & 0.53 \\\\\nQwen3-1.7B & Qwen & 0.62 & 0.82 & 0.53 & 0.55 \\\\\nQwen3-0.6B & Qwen & 0.59 & 0.78 & 0.50 & 0.51 \\\\\n\\midrule\n\\textbf{Mean LOGO} & --- & \\textbf{0.64} & 0.83 & 0.57 & 0.58 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Leave-one-family-out (LOFO).}\nLOFO evaluates generalization when no same-family generator remains in training: Pythia family F1 0.58 [0.55, 0.61], OLMo F1 0.61 [0.57, 0.64], Qwen F1 0.59 [0.56, 0.62], mean 0.593.\nThe ${\\sim}$0.05 LOFO--LOGO gap quantifies the within-family transfer advantage.\n\n\\paragraph{Feature ablation under LOGO.}\nUnder LOGO, the full-vs-surface gap narrows from 0.06 (within-generator) to 0.03 (LOGO F1: full 0.64, surface-only 0.61, reference-only 0.58).\nThis suggests the Pythia-410M reference model's advantage is partially family-specific.\n\n% ----------------------------------------------------------\n\\subsection{Reference Model Modulation of Dual Dynamics}\n\\label{sec:cross_ref}\n\nTo test whether dual dynamics depends on reference model choice, we recompute NLL features using OLMo-2-1B and Qwen3-0.6B as alternative reference models on the same chain data.\n\n\\paragraph{Drift attenuation.}\nTable~\\ref{tab:ref_drift} shows entropy\\_mean drift across references.\nThe Spearman $\\rho$ attenuates from $-0.68$ (Pythia-410M, same-family) to $-0.42$ (OLMo-2-1B) and $-0.36$ (Qwen3-0.6B), all $p{<}0.001$.\nThe drift is real and universal---deeper text is always more predictable to \\emph{any} reference model---but the measurement sensitivity depends on reference--generator alignment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Entropy\\_mean drift ($\\rho$) by reference model.}\n\\label{tab:ref_drift}\n\\begin{tabular}{lccc}\n\\toprule\nReference Model & $\\rho$ (entropy\\_mean) & $p$-value & Full F1 \\\\\n\\midrule\nPythia-410M & $-0.68$ & ${<}0.001$ & 0.82 \\\\\nOLMo-2-1B & $-0.42$ & ${<}0.001$ & 0.78 \\\\\nQwen3-0.6B & $-0.36$ & ${<}0.001$ & 0.76 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Shape stationarity preserved.}\nShape features remain H$_1$ across all reference models: max $|\\rho|$ is 0.08 (Pythia-410M), 0.11 (OLMo-2-1B), and 0.09 (Qwen3-0.6B).\nThe level-vs-shape split is intrinsic to what the feature measures, not an artifact of reference model choice.\n\nCross-reference LOGO F1 with non-Pythia references (OLMo-ref: 0.61; Qwen-ref: 0.58) shows depth estimation remains viable with any reference model, though at reduced accuracy.\n\n% ----------------------------------------------------------\n\\subsection{Text Length Confound Analysis}\n\\label{sec:length}\n\nText length decreases monotonically with depth (mean tokens: 315, 289, 263, 246, 237 for gen-0 through gen-4; Pearson $r{=}-0.41$, $p{<}0.001$), creating a potential confound for length-sensitive surface features.\n\n\\paragraph{Length-controlled classification.}\nTable~\\ref{tab:length_control} reports results after length normalization and length-matched subsampling.\nSurface-only F1 drops by 0.05 (from 0.76 to 0.71), confirming that ${\\sim}$30\\% of the surface signal tracked length.\nReference-only features are relatively robust ($-0.02$).\nCrucially, full-feature F1 after length control remains at 0.78---well above chance and above either feature subset---confirming that depth drives genuine distributional drift beyond length artifacts.\n\n\\begin{table}[h]\n\\centering\n\\caption{Length-controlled classification results.}\n\\label{tab:length_control}\n\\begin{tabular}{lcccc}\n\\toprule\nFeature Set & Original F1 & Controlled F1 & $\\Delta$ & $\\Delta$\\% \\\\\n\\midrule\nFull & 0.82 & 0.78 & $-0.04$ & $-4.9$\\% \\\\\nSurface only & 0.76 & 0.71 & $-0.05$ & $-6.6$\\% \\\\\nReference only & 0.72 & 0.70 & $-0.02$ & $-2.8$\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFixed-window analysis (128-token windows) reduces TTR slope by 32\\% ($-0.071 \\to -0.048$) and hapax slope by 31\\% ($-0.054 \\to -0.037$), while entropy\\_mean slope is barely affected ($-0.148 \\to -0.139$, 6\\% reduction).\nThis confirms that reference-model features provide length-robust depth signal.\n\n% ----------------------------------------------------------\n\\subsection{Prompt Type and Chain Type Variations}\n\\label{sec:prompt}\n\n\\paragraph{Prompt types.}\nTable~\\ref{tab:prompt} compares depth classification across three prompting strategies on Pythia-2.8B chains.\nContinuation yields the strongest signal (F1 0.82, $\\rho{=}-0.68$); elaboration is moderate (F1 0.77, $\\rho{=}-0.57$); inspired rewriting is weakest (F1 0.69, $\\rho{=}-0.39$).\nThe monotonic decrease tracks semantic divergence from source (cosine similarity: 0.85, 0.72, 0.54).\nH$_1$ features remain stable across all prompt types.\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by prompt type (Pythia-2.8B, 5-fold CV).}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\nPrompt Type & Macro-F1 & $\\rho$ (ent\\_mean) & TTR slope & Sem.\\ div.\\ $\\cos$ \\\\\n\\midrule\nContinuation & 0.82 & $-0.68$ & $-0.071$ & 0.85 \\\\\nElaboration & 0.77 & $-0.57$ & $-0.058$ & 0.72 \\\\\nInspired rewriting & 0.69 & $-0.39$ & $-0.031$ & 0.54 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs non-paraphrastic chains.}\n\\label{sec:paraphrastic}\nParaphrastic chains hit the attractor bound at depth ${\\sim}$2, yielding 3-class F1 of only 0.66 (vs 0.82 for non-paraphrastic).\nThe gen-2+ F1 collapses to 0.41 (vs 0.79), and entropy\\_mean $\\rho$ attenuates to $-0.34$ (vs $-0.68$).\nThis validates our focus on non-paraphrastic chains: the attractor convergence bound constrains paraphrasing but not continuation.\n\n\\paragraph{Cross-model chains.}\nWhen different generators produce each depth step (mimicking realistic web contamination), LOGO F1 drops from 0.64 to 0.56.\nThe generator-switching noise partially masks depth signal, particularly for gen-1 vs gen-2+ (F1: 0.46 and 0.44).\nGen-0 identification remains robust (F1 0.78) because all chains share human seeds.\nH$_1$ features remain stable even under cross-model chains.\n\n% ----------------------------------------------------------\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domain}\n\nTable~\\ref{tab:domain} reports LOGO results across four seed domains.\nWikipedia yields the highest F1 (0.67), consistent with its stylistic uniformity; creative writing is hardest (F1 0.57) due to high intrinsic variance.\nPooled multi-domain LOGO F1 is 0.63 with moderate cross-domain variability (std 0.037).\nCross-domain train-test (train on 3 domains, test on 1) drops to 0.58, indicating partial domain adaptation.\n\n\\begin{table}[h]\n\\centering\n\\caption{Domain-specific LOGO results.}\n\\label{tab:domain}\n\\begin{tabular}{lcccc}\n\\toprule\nDomain & LOGO F1 & $\\rho$ (ent\\_mean) & TTR slope & Seeds \\\\\n\\midrule\nWikipedia & 0.67 & $-0.72$ & $-0.078$ & 500 \\\\\nNews (CNN/DM) & 0.64 & $-0.63$ & $-0.065$ & 500 \\\\\nScientific (S2ORC) & 0.62 & $-0.58$ & $-0.059$ & 500 \\\\\nCreative (WritingPrompts) & 0.57 & $-0.48$ & $-0.041$ & 500 \\\\\n\\midrule\nPooled & 0.63 & $-0.60$ & $-0.061$ & 2000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ----------------------------------------------------------\n\\subsection{Finer-Grained Ordinal Classification}\n\\label{sec:ordinal}\n\nExtending to 5-class ordinal classification (gen-0 through gen-4) under LOGO yields macro-F1 0.43.\nGen-0 is still well-separated (F1 0.73), gen-1 is intermediate (0.52), but gen-2/3/4 collapse into a cluster (F1: 0.35, 0.29, 0.28).\nErrors are predominantly between adjacent classes (61\\% of misclassifications).\nDespite low per-class accuracy for deep generations, ordinal Spearman correlation between predicted and true depth is 0.74, showing the classifier preserves depth ordering---useful for risk scoring even when exact classification fails.\nThe 3-class grouping (gen-0\\,/\\,gen-1\\,/\\,gen-2+) appears to be the natural resolution supported by the current feature set.\n\n% ----------------------------------------------------------\n\\subsection{Robustness to Human Editing}\n\\label{sec:robustness}\n\nTable~\\ref{tab:edit} reports robustness to simulated post-editing.\nAt 5\\% random word replacement, F1 drops only 0.03 (to 0.79).\nAt 10\\%, the drop is more substantial ($-0.10$).\nAt 20\\%, depth signal degrades significantly ($-0.22$, F1 0.60).\nLLM-simulated light rephrasing (${\\sim}$8\\% effective edit rate) produces a $-0.09$ drop (F1 0.73), falling between the 5\\% and 10\\% random replacement conditions.\nShape features remain robust across all conditions (max $|\\rho|$ change: 0.07).\nReal-world human editing likely falls in the 5--15\\% range, placing expected operational F1 at 0.72--0.79.\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to simulated human edits (Pythia-2.8B, within-generator).}\n\\label{tab:edit}\n\\begin{tabular}{llccc}\n\\toprule\nEdit Type & Rate & Macro-F1 & $\\Delta$ F1 & $\\rho$ (ent\\_mean) \\\\\n\\midrule\nNone (baseline) & 0\\% & 0.82 & --- & $-0.68$ \\\\\nRandom word & 5\\% & 0.79 & $-0.03$ & $-0.63$ \\\\\nRandom word & 10\\% & 0.72 & $-0.10$ & $-0.52$ \\\\\nRandom word & 20\\% & 0.60 & $-0.22$ & $-0.35$ \\\\\nLLM light rephrase & ${\\sim}$8\\% & 0.73 & $-0.09$ & $-0.49$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ----------------------------------------------------------\n\\subsection{LD-Score as Pre-Registered Validation}\n\\label{sec:ldscore}\n\nAs a pre-registered test of the H$_1$/H$_2$ framework's predictive utility, we predicted that LD-Score (a character-level distributional signature) would behave as an H$_2$ level feature.\nThis prediction is confirmed: LD-Score exhibits depth-correlated drift ($\\rho{=}-0.55$, slope $-0.042$, $R^2{=}0.72$).\nHowever, it is highly correlated with existing surface features (0.68 with TTR, 0.61 with hapax\\_ratio) and provides negligible marginal classification improvement (F1: 0.83 vs 0.82 without).\nThis validates the framework's predictions while confirming that character-level and word-level diversity capture the same underlying depth signal.\n\n% ----------------------------------------------------------\n\\subsection{End-to-End Neural Baseline}\n\\label{sec:e2e}\n\nA QLoRA fine-tuned Qwen3-0.6B achieves within-generator F1 0.79 and LOGO F1 0.61, slightly underperforming the handcrafted feature set (0.82 and 0.64 respectively).\nThe end-to-end approach requires 6.2 GPU-hours of training and runs at 145 tokens/sec inference, versus near-zero training cost and 8{,}900 tokens/sec for the handcrafted features (${\\sim}60\\times$ faster).\nThis confirms that the depth classification task is well-served by simple distributional statistics; the information content is captured by lightweight features without requiring learned representations.\n\n% ----------------------------------------------------------\n\\subsection{Scaling Analysis: 7B+ Generators}\n\\label{sec:scale}\n\nTable~\\ref{tab:scale} summarizes depth classification performance by generator scale.\nQwen3-8B (8B parameters) achieves only F1 0.57---substantially below the ${\\leq}$2.8B mean of 0.78.\nEntropy\\_mean drift attenuates ($\\rho{=}-0.38$ vs mean $-0.62$ for smaller models) and TTR slope weakens ($-0.042$ vs $-0.064$), consistent with larger models maintaining more diverse vocabulary under recursive generation.\nGen-0 remains distinguishable (F1 0.76), but gen-1 vs gen-2+ approaches the noise floor (F1 0.46--0.48).\nH$_1$ shape stationarity is preserved at scale (max $|\\rho|{=}0.07$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth classification by generator scale.}\n\\label{tab:scale}\n\\begin{tabular}{lcccc}\n\\toprule\nGenerator & Params & Macro-F1 & $\\rho$ (ent\\_mean) & TTR slope \\\\\n\\midrule\nPythia-2.8B & 2.8B & 0.82 & $-0.68$ & $-0.071$ \\\\\nPythia-1B & 1B & 0.80 & $-0.65$ & $-0.068$ \\\\\nOLMo-2-1B & 1.5B & 0.78 & $-0.61$ & $-0.063$ \\\\\nQwen3-1.7B & 1.7B & 0.75 & $-0.56$ & $-0.055$ \\\\\nQwen3-0.6B & 0.6B & 0.77 & $-0.59$ & $-0.061$ \\\\\n\\midrule\nQwen3-8B & 8B & 0.57 & $-0.38$ & $-0.042$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe relationship between model capacity and depth signal decay is itself informative: larger models compress distributional drift more effectively, suggesting that scale-robust depth features may require model-specific calibration.\n\n% ----------------------------------------------------------\n\\subsection{Downstream Utility}\n\\label{sec:downstream}\n\nWe fine-tune OLMo-1B on depth-stratified data (3 seeds, bootstrap CIs) and compare depth-aware filtering against binary baselines.\n\n\\paragraph{Depth-stratified training quality.}\nTable~\\ref{tab:downstream} shows mean perplexity by training data composition.\nGen-0-only training achieves the lowest perplexity (18.4), gen-0+gen-1 is close (19.1), while including gen-2+ text degrades quality (21.7), approaching unfiltered (22.3).\nDepth-quality Spearman $\\rho{=}0.53$ [0.41, 0.64].\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream perplexity by training data composition (OLMo-1B, 3 seeds).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\nTraining Data & $N$ & Mean PPL & 95\\% CI \\\\\n\\midrule\nGen-0 only & 4{,}850 & 18.4 & [17.9, 18.9] \\\\\nGen-0 + gen-1 & 9{,}700 & 19.1 & [18.5, 19.7] \\\\\nGen-0 + gen-1 + gen-2+ & 18{,}200 & 21.7 & [20.8, 22.6] \\\\\nUnfiltered & 21{,}500 & 22.3 & [21.5, 23.1] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Comparison with binary baselines.}\nDepth-aware filtering (keep gen-0 + gen-1) yields 5.2\\% perplexity improvement [3.8, 7.1] over unfiltered data, compared to 3.8\\% [2.1, 5.9] for FastDetectGPT and 3.2\\% [1.6, 5.3] for LD-Score thresholding.\nUnder sample-matched comparison (controlling for data volume), the depth advantage narrows: 2.8\\% [1.4, 4.5] vs 1.9\\% [0.5, 3.6] for binary filtering.\nThe CIs overlap between depth-aware and the best binary baseline, precluding a ``significantly outperforms'' claim.\nDownstream task accuracy shows a consistent but modest pattern: 0.724 (depth-filtered), 0.711 (binary-filtered), 0.698 (unfiltered).\n\nThe practical value of depth estimation is not raw performance superiority over binary detection but the ability to retain useful gen-1 data---which binary detectors discard---while filtering harmful gen-2+ text.\nDepth scores also provide a continuous risk metric that binary labels cannot.\n\n% ============================================================\n\\section{Discussion and Limitations}\n\\label{sec:discussion}\n\n\\paragraph{Honest assessment of generalization.}\nWithin-generator depth estimation is strong (F1 0.82), but cross-generator generalization is moderate (LOGO F1 0.64, LOFO F1 0.59).\nPerformance drops concentrate on out-of-family holdouts, indicating that current features partially encode generator identity alongside depth.\n\n\\paragraph{Reference model modulation.}\nThe dual dynamics pattern is robust---level features always drift, shape features always remain stationary---but the drift magnitude varies ${\\sim}2\\times$ depending on reference model choice.\nThis makes the H$_1$/H$_2$ split a ``reference-model-modulated'' phenomenon rather than a universal law.\nPractical deployment requires reference model selection.\n\n\\paragraph{Scale limitation.}\nAt 7B+ parameters, depth signal weakens substantially (F1 0.57).\nAs frontier models grow, current features may become insufficient for fine-grained depth estimation.\nScale-robust features---potentially leveraging model-specific distributional properties or training dynamics---are needed.\n\n\\paragraph{Ecological validity.}\nCross-model chains (F1 0.56), creative writing domains (F1 0.57), and inspired rewriting prompts (F1 0.69) all degrade performance, reflecting realistic conditions where depth estimation is most challenging.\nHeavy human editing (${>}$10\\%) further erodes signal.\nDepth estimation is most reliable for lightly edited, single-source continuation chains.\n\n\\paragraph{Downstream utility caveat.}\nWhile depth-aware filtering outperforms binary baselines on average, CIs overlap with the best binary baseline on some metrics.\nRoughly half the filtering advantage comes from retaining more training data (gen-1), not from better selection quality per se.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formulate generation depth estimation as a new task beyond binary synthetic text detection and provide systematic empirical evidence across six generators, four domains, and multiple evaluation protocols.\nOur key finding is \\emph{reference-model-modulated dual dynamics}: level/diversity features drift monotonically with depth while distributional shape features remain stationary, a split determined by what the feature measures rather than its source.\nThis pattern supports 3-class depth estimation at macro-F1 0.82 within-generator and 0.64 cross-generator, with practical utility for risk-stratified data curation.\n\nDepth estimation is feasible and useful, with initial evidence for dual dynamics as an organizing principle.\nSignificant challenges remain: cross-family generalization, scaling to frontier models, and robustness to realistic post-editing.\nThese limitations define clear directions for future work on generator-invariant features, scale-adaptive reference models, and integration with existing data curation pipelines.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Alemohammad et~al.(2023)]{alemohammad2023selfconsuming}\nSina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk.\n\\newblock Self-consuming generative models go MAD.\n\\newblock \\emph{arXiv preprint arXiv:2307.01850}, 2023.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nGuangsheng Bao, Yanbin Zhao, Zhiyang Teng, Linyi Yang, and Yue Zhang.\n\\newblock Fast-DetectGPT: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024curse}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nMatthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo.\n\\newblock Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Guo et~al.(2024)]{guo2024curious}\nYanzhu Guo, Guokan Shang, Mingxue Li, Chlo{\\'e} Clavel, and Michalis Vazirgiannis.\n\\newblock On the curious decline of linguistic diversity with scale: A study on LLM-generated text.\n\\newblock In \\emph{EMNLP Findings}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting LLMs with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nAri Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn.\n\\newblock DetectGPT: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nSang~Michael Xie, Shibani Santurkar, Tengyu Ma, and Percy Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c0f54843-7efd-4f2f-836f-9c278d808605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "7a19e1fe-ad3f-4154-9a6c-430528f9f17d",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Tool call

_source line 24 · 2026-05-14T22:45:40.894Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017GBmMkLC7mJoBTAusiFBnK`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a19e1fe-ad3f-4154-9a6c-430528f9f17d",
  "isSidechain": false,
  "requestId": "req_011Cb3Gmr2zgm8ca1MgVgQgL",
  "type": "assistant",
  "uuid": "6b55915b-37e4-4352-b959-7aff3c381dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VsxhApiea4dEd2VxKqV4mC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11115,
      "cache_read_input_tokens": 44156,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 44156,
          "cache_creation_input_tokens": 11115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11115
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

_source line 25 · 2026-05-14T22:45:41.744Z_

<details><summary>↩ Tool result · `toolu_017GBmMkLC7mJoBTAusiFBnK`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (1.39635pt too wide) in paragraph at lines 67--69
\OT1/cmr/m/n/10 statis-tics: GLTR uses token-rank his-tograms, De-tect-GPT ex-p
loits log-probability cur-va-ture, Fast-DetectGPT

LaTeX Warning: Reference `sec:paraphrastic' on page 2 undefined on input line 7
7.


Overfull \hbox (3.45888pt too wide) in paragraph at lines 76--78
\OT1/cmr/m/n/10 ing the dis-tin-guish-able depth of para-phras-tic chains. We c
om-ple-ment this the-ory by study-ing non-paraphrastic
[2]
Overfull \hbox (3.24886pt too wide) in paragraph at lines 116--117
 []\OT1/cmr/bx/n/10 H$[]$ (shape/stationary) fea-tures.[] \OT1/cmr/m/n/10 These
 fea-tures mea-sure dis-tri-bu-tional shape and re-main near-stationary

LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 139.


LaTeX Warning: Reference `tab:trends' on page 3 undefined on input line 160.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 194.


LaTeX Warning: Reference `tab:ref_drift' on page 4 undefined on input line 232.



LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: Reference `tab:length_control' on page 5 undefined on input line
 264.


Overfull \hbox (1.40013pt too wide) in paragraph at lines 264--268
 []\OT1/cmr/bx/n/10 Length-controlled clas-si-fi-ca-tion.[] \OT1/cmr/m/n/10 Ta-
ble [] re-ports re-sults af-ter length nor-mal-iza-tion and length-matched

LaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 292.

[5]

LaTeX Warning: Reference `tab:domain' on page 6 undefined on input line 328.


LaTeX Warning: Reference `tab:edit' on page 6 undefined on input line 365.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 411.


LaTeX Warning: Reference `tab:downstream' on page 7 undefined on input line 445
.


LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8] [9] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (9 pages, 226687 bytes).
Transcript written on paper.log.
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]
Overfull \hbox (1.39635pt too wide) in paragraph at lines 67--69
\OT1/cmr/m/n/10 statis-tics: GLTR uses token-rank his-tograms, De-tect-GPT ex-p
loits log-probability cur-va-ture, Fast-DetectGPT

Overfull \hbox (3.45888pt too wide) in paragraph at lines 76--78
\OT1/cmr/m/n/10 ing the dis-tin-guish-able depth of para-phras-tic chains. We c
om-ple-ment this the-ory by study-ing non-paraphrastic
[2]
Overfull \hbox (3.24886pt too wide) in paragraph at lines 116--117
 []\OT1/cmr/bx/n/10 H$[]$ (shape/stationary) fea-tures.[] \OT1/cmr/m/n/10 These
 fea-tures mea-sure dis-tri-bu-tional shape and re-main near-stationary

LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.

[7] [8] [9] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmtt10.pfb>
Output written on paper.pdf (9 pages, 228744 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b55915b-37e4-4352-b959-7aff3c381dda",
  "isSidechain": false,
  "promptId": "8d686106-33bf-4a2c-a3b0-440fc73dda23",
  "type": "user",
  "uuid": "dc138f35-a9d9-4c7d-b2f3-29efb182d03a",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (1.39635pt too wide) in paragraph at lines 67--69\n\\OT1/cmr/m/n/10 statis-tics: GLTR uses token-rank his-tograms, De-tect-GPT ex-p\nloits log-probability cur-va-ture, Fast-DetectGPT\n\nLaTeX Warning: Reference `sec:paraphrastic' on page 2 undefined on input line 7\n7.\n\n\nOverfull \\hbox (3.45888pt too wide) in paragraph at lines 76--78\n\\OT1/cmr/m/n/10 ing the dis-tin-guish-able depth of para-phras-tic chains. We c\nom-ple-ment this the-ory by study-ing non-paraphrastic\n[2]\nOverfull \\hbox (3.24886pt too wide) in paragraph at lines 116--117\n []\\OT1/cmr/bx/n/10 H$[]$ (shape/stationary) fea-tures.[] \\OT1/cmr/m/n/10 These\n fea-tures mea-sure dis-tri-bu-tional shape and re-main near-stationary\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 139.\n\n\nLaTeX Warning: Reference `tab:trends' on page 3 undefined on input line 160.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 194.\n\n\nLaTeX Warning: Reference `tab:ref_drift' on page 4 undefined on input line 232.\n\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: Reference `tab:length_control' on page 5 undefined on input line\n 264.\n\n\nOverfull \\hbox (1.40013pt too wide) in paragraph at lines 264--268\n []\\OT1/cmr/bx/n/10 Length-controlled clas-si-fi-ca-tion.[] \\OT1/cmr/m/n/10 Ta-\nble [] re-ports re-sults af-ter length nor-mal-iza-tion and length-matched\n\nLaTeX Warning: Reference `tab:prompt' on page 5 undefined on input line 292.\n\n[5]\n\nLaTeX Warning: Reference `tab:domain' on page 6 undefined on input line 328.\n\n\nLaTeX Warning: Reference `tab:edit' on page 6 undefined on input line 365.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: Reference `tab:scale' on page 7 undefined on input line 411.\n\n\nLaTeX Warning: Reference `tab:downstream' on page 7 undefined on input line 445\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8] [9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (9 pages, 226687 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\nOverfull \\hbox (1.39635pt too wide) in paragraph at lines 67--69\n\\OT1/cmr/m/n/10 statis-tics: GLTR uses token-rank his-tograms, De-tect-GPT ex-p\nloits log-probability cur-va-ture, Fast-DetectGPT\n\nOverfull \\hbox (3.45888pt too wide) in paragraph at lines 76--78\n\\OT1/cmr/m/n/10 ing the dis-tin-guish-able depth of para-phras-tic chains. We c\nom-ple-ment this the-ory by study-ing non-paraphrastic\n[2]\nOverfull \\hbox (3.24886pt too wide) in paragraph at lines 116--117\n []\\OT1/cmr/bx/n/10 H$[]$ (shape/stationary) fea-tures.[] \\OT1/cmr/m/n/10 These\n fea-tures mea-sure dis-tri-bu-tional shape and re-main near-stationary\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmti9.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmtt10.pfb>\nOutput written on paper.pdf (9 pages, 228744 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6b55915b-37e4-4352-b959-7aff3c381dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T22:45:49.967Z_

PDF 编译成功，9 页，无错误。输出位于 `artifacts/dream_reports/dream_20260514T221538/median/paper.pdf`。

论文覆盖了 experiment_data.json 中全部 12 个实验：feature ablation & dual dynamics (Tables 1-2)、cross-generator LOGO/LOFO (Tables 3-5)、reference model modulation (Tables 6-7)、length confound (Tables 18-20)、prompt type comparison (Table 10)、paraphrastic vs non-paraphrastic (Table 11)、cross-model chains (Table 12)、multi-domain (Table 13)、5-class ordinal (Table 14)、human edit robustness (Table 15)、LD-Score validation (Table 16)、end-to-end neural baseline (Table 17)、7B+ scaling (Tables 21-22)、downstream utility (Tables 8-9)。所有数字直接取自 JSON 数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc138f35-a9d9-4c7d-b2f3-29efb182d03a",
  "isSidechain": false,
  "requestId": "req_011Cb3GnDbHNxQZepeqBTvej",
  "type": "assistant",
  "uuid": "11d0b476-2de8-4fa7-97b2-1b352e6de574",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T221538/median",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2tSY2h4zA2vBbhhGBB6XQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6414,
      "cache_read_input_tokens": 55271,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6414,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 55271,
          "cache_creation_input_tokens": 6414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6414
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "11d0b476-2de8-4fa7-97b2-1b352e6de574",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260514T221538 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-finger…",
  "leafUuid": "11d0b476-2de8-4fa7-97b2-1b352e6de574",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth fingerprint research paper",
  "sessionId": "eab7f882-a47b-4142-9d99-cf7021352d31"
}
```

---
