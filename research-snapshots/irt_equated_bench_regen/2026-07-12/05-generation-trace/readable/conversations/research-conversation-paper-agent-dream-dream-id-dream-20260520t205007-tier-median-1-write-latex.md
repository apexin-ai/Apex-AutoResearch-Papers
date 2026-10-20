# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/3be65274-1c7a-4df1-b2f9-03f667310cd1.jsonl`
- **Structured JSON:** [`041593a802d90c439a1e.json`](../../sessions/04/041593a802d90c439a1e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T21:13:11.757Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T21:13:11.757Z",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：论文重心从\"端到端污染检测管线\"转向\"检测方法论贡献+心理测量诊断洞察\"。 Claim 1降级为条件性陈述（架构同质+大效应）；Claim 2从三信号退化为DIF+ConStat双信号； Claim 3加\"pilot-scale\"限定。新增贡献：首个大规模LLM群体IRT拟合诊断、semi-synthetic验证框架。 仍可投ICLR但需在framing上诚实呈现限制条件，以方法论严谨性取胜而非系统完整性。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T21:13:11.761Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T21:13:11.761Z",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-20T21:13:11.785Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：论文重心从"端到端污染检测管线"转向"检测方法论贡献+心理测量诊断洞察"。 Claim 1降级为条件性陈述（架构同质+大效应）；Claim 2从三信号退化为DIF+ConStat双信号； Claim 3加"pilot-scale"限定。新增贡献：首个大规模LLM群体IRT拟合诊断、semi-synthetic验证框架。 仍可投ICLR但需在framing上诚实呈现限制条件，以方法论严谨性取胜而非系统完整性。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "7642636c-2bd8-437f-9e08-ec6ce4e26f9d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T21:13:11.784Z_

```json
{
  "parentUuid": "7642636c-2bd8-437f-9e08-ec6ce4e26f9d",
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
  "uuid": "44c0ecb4-e948-47a0-8f73-ebe907357a34",
  "timestamp": "2026-05-20T21:13:11.784Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T21:13:11.784Z_

```json
{
  "parentUuid": "44c0ecb4-e948-47a0-8f73-ebe907357a34",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bc125ca3-f230-4361-87e5-3bdaa1240dd3",
  "timestamp": "2026-05-20T21:13:11.784Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
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
  "aiTitle": "Generate simulated research paper with IRT methodology",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Assistant

_source line 7 · 2026-05-20T21:15:16.696Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc125ca3-f230-4361-87e5-3bdaa1240dd3",
  "isSidechain": false,
  "requestId": "req_011CbEWac2VbWYaTDFt3AjB5",
  "type": "assistant",
  "uuid": "2c1fe667-cbe2-4d39-a710-65fbabd71b2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU6TuxXP4papV6jrFTigYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11368,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11368
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

_source line 8 · 2026-05-20T21:15:17.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UUb6kjHWnEoRLagRCvD9tj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c1fe667-cbe2-4d39-a710-65fbabd71b2a",
  "isSidechain": false,
  "requestId": "req_011CbEWac2VbWYaTDFt3AjB5",
  "type": "assistant",
  "uuid": "bd7dfa61-42c8-4620-b9be-785461d1aa48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU6TuxXP4papV6jrFTigYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11368,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11368
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

_source line 9 · 2026-05-20T21:15:17.942Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mf1vMdBPywVksiMr8Hj9xh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd7dfa61-42c8-4620-b9be-785461d1aa48",
  "isSidechain": false,
  "requestId": "req_011CbEWac2VbWYaTDFt3AjB5",
  "type": "assistant",
  "uuid": "47e6c8c3-299b-46aa-88a0-a940d3a63aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EU6TuxXP4papV6jrFTigYZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11368,
      "cache_read_input_tokens": 11841,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11368,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11368
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

_source line 10 · 2026-05-20T21:15:17.950Z_

<details><summary>↩ Tool result · `toolu_01Mf1vMdBPywVksiMr8Hj9xh`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)
5	- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)
6	- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)
7	
8	## Core Claims (3 条, 可证伪)
9	
10	**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.
11	
12	**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.
13	
14	**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.
15	
16	## Story Spine
17	
18	**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.
19	
20	**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.
21	
22	**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.
23	
24	**Headline result template**: "On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature."
25	
26	## Venue Fit Risks
27	
28	- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ "fairness testing for items").
29	- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: "examinees" → "models", "test items" → "benchmark questions", "DIF" → "item-level contamination signal", "equating" → "score comparability across benchmark versions".
30	- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as "bringing mature psychometric tools to solve an urgent ML problem" rather than "inventing new statistics."
31	
32	## Anticipated Reviewer Concerns
33	
34	1. **"DIF power is only sufficient for large effects (δ≥1.4)"**
35	   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.
36	   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)
37	
38	2. **"Model cohort sample sizes are too small for classical DIF"**
39	   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.
40	   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)
41	
42	3. **"Only validated in simulation"**
43	   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.
44	   - Evidence needed: plan_001, plan_004
45	
46	4. **"Item regeneration quality — how do you ensure replacements measure the same construct?"**
47	   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.
48	   - Evidence needed: plan_005, plan_006
49	
50	5. **"RL robustness is only theoretical — where's the empirical evidence?"**
51	   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.
52	   - Evidence needed: plan_002
53	
54	6. **"Computational cost of the full pipeline"**
55	   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.
56	
57	7. **"DIF flags may reflect capability improvement, not contamination"**
58	   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.
59	   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)
60	
61	8. **"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random"**
62	   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.
63	   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)
64	
65	9. **"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items"**
66	   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.
67	   - Evidence needed: plan_002 (partial exploitation analysis)
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47e6c8c3-299b-46aa-88a0-a940d3a63aa0",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "586d8f9e-13fa-49a0-8993-d6a700515ac5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026; 5 months for full pipeline experiments)\n- Backup: AAAI 2027 (abstract July 21, paper July 28, 2026 — tight, 2 months)\n- Backup 2: EACL 2027 via ARR August 2026 cycle (August 3, 2026)\n\n## Core Claims (3 条, 可证伪)\n\n**Claim 1 (Detection)**: DIF analysis across model release cohorts detects benchmark contamination with practical power (ETS C: TPR 0.72-0.85, FPR <0.05 at N≥80, δ≥1.4) and is robust to RL training — because it operates on group-level behavioral response patterns (correct/incorrect conditional on ability), not within-model output distributions that GRPO/PPO smoothing affects.\n\n**Claim 2 (Ensemble Coverage)**: A multi-signal contamination sentinel combining DIF (large effects, RL-robust), ConStat-style perturbation testing (non-RL models), and DVD generation variance (variant contamination) achieves detection coverage across the full effect-size spectrum and model-type landscape, with each signal covering the blind spots of the others.\n\n**Claim 3 (Regeneration)**: Bifactor IRT equating with anchor items enables psychometrically equivalent benchmark regeneration — flagged items can be replaced with empirically calibrated alternatives that preserve construct validity, difficulty, and discrimination, maintaining benchmark comparability through a formal graceful-degradation framework.\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent ability. Contamination systematically erodes this validity. Critically, RL training (GRPO/PPO) conceals contamination signals: Wang et al. (ICLR 2026) show 14-20pp AUROC degradation for all reference-free detectors after ~156 GRPO steps, reducing most to near-random (~50% AUROC). The model ecosystem is shifting toward RL-trained reasoning models (o1, o3, DeepSeek-R1), making this a growing threat.\n\n**Existing approaches & gaps**: LiveBench updates monthly from recent sources but applies no psychometric calibration across updates. ConStat provides FDR-controlled performance-based detection but relies on perturbation sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains (arXiv 2026) uses multidimensional IRT for extensible evaluation but addresses score comparability, not contamination. No existing work closes the full loop from RL-robust detection through construct-constrained generation to psychometrically equated regeneration.\n\n**Our framing**: Contamination is fundamentally a psychometric problem — it creates Differential Item Functioning (DIF), where contaminated items become differentially easier for exposed model cohorts beyond what general ability gains predict. DIF operates on group-level Item Characteristic Curves conditional on ability, making it orthogonal to within-model output distribution smoothing. This is the one contamination signal RL cannot conceal without negating the purpose of contamination itself: if a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level. A nuance: partial exploitation (model memorizes but answers correctly only p<1 of the time) shrinks DIF effect size proportionally — we formally characterize detection power as a function of exploitation rate. Combined with a multi-signal ensemble for full effect-size coverage and bifactor IRT equating for calibrated item regeneration, this creates a psychometric monitoring and regeneration framework — applying mature, validated psychometric tools to solve an urgent ML evaluation problem.\n\n**Headline result template**: \"On MMLU with 5,000+ models spanning a capability range from near-random (46% accuracy) to near-saturation (60%), DIF-based ETS C detection achieves 73-85% TPR with <5% FPR for large contamination effects (δ≥1.4), maintaining power where 10 existing detection methods degrade to near-random under RL training (Wang et al., ICLR 2026). Leveraging the unprecedented scale of METABENCH (5,219 models), we conduct the largest DIF analysis in LLM evaluation literature.\"\n\n## Venue Fit Risks\n\n- **ICLR**: Strong fit — evaluation methodology, robustness to RL, psychometric theory applied to ML. Risk: reviewers may not be familiar with IRT/DIF methodology. Mitigation: provide self-contained DIF tutorial in appendix, reproducible code, and connection to ML-familiar concepts (DIF ≈ \"fairness testing for items\").\n- **Cross-discipline bridge**: IRT/psychometrics vocabulary needs translation for ML audience. Key mappings: \"examinees\" → \"models\", \"test items\" → \"benchmark questions\", \"DIF\" → \"item-level contamination signal\", \"equating\" → \"score comparability across benchmark versions\".\n- **Novelty concern**: DIF itself is not new (1988). Our contribution is the novel application to LLM benchmark contamination + the RL-robustness argument + the integration with regeneration. Need to frame as \"bringing mature psychometric tools to solve an urgent ML problem\" rather than \"inventing new statistics.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"DIF power is only sufficient for large effects (δ≥1.4)\"**\n   - Response: Large effects are precisely what threaten benchmark validity most (GSM1K: 10-13% average accuracy drop). Small effects (δ<0.6) have minimal impact on rankings. For medium effects, the ensemble's other signals provide coverage.\n   - Evidence needed: plan_001 (real-data validation), plan_003 (ensemble)\n\n2. **\"Model cohort sample sizes are too small for classical DIF\"**\n   - Response: (a) ETS C uses effect-size thresholds, not p-values, reducing sample-size dependence; (b) annual cohorts now reach N=80-100; (c) Cumulative Bayesian priors accumulate power over time; (d) Item-Focused Trees treat release date as continuous covariate.\n   - Evidence needed: plan_001 (real cohort sizes), plan_008 (Bayesian DIF, P2)\n\n3. **\"Only validated in simulation\"**\n   - Response: plan_001 uses METABENCH real data (5,055 models). plan_004 cross-validates on GSM8K with GSM1K ground truth.\n   - Evidence needed: plan_001, plan_004\n\n4. **\"Item regeneration quality — how do you ensure replacements measure the same construct?\"**\n   - Response: Bifactor IRT equating with anchor items + empirical calibration via student simulation (not prompt-based difficulty targeting). Construct validity verified through factor loading analysis.\n   - Evidence needed: plan_005, plan_006\n\n5. **\"RL robustness is only theoretical — where's the empirical evidence?\"**\n   - Response: plan_002 directly evaluates DIF on cohorts including RL-trained models.\n   - Evidence needed: plan_002\n\n6. **\"Computational cost of the full pipeline\"**\n   - Response: DIF analysis is lightweight (minutes, CPU only). Main cost is one-time calibration panel. Once calibrated, ongoing monitoring is cheap.\n\n7. **\"DIF flags may reflect capability improvement, not contamination\"**\n   - Response: Post-2024 models are both more capable and more contaminated. We control for this via (a) within-family DIF analysis (same architecture at different training stages, e.g., Llama-2→3→3.1), where capability trajectory is known, isolating contamination-specific DIF; (b) domain-specificity analysis of DIF flags vs known capability trajectories; (c) bifactor model's subject-specific factors as covariates to absorb domain-specific capability gains.\n   - Evidence needed: plan_001 (within-family sub-analysis), plan_005 (bifactor covariates)\n\n8. **\"Ground truth is too noisy to validate DIF — MMLU-CF κ=0.14 is near-random\"**\n   - Response: (a) We supplement MMLU-CF with semi-synthetic validation: inject known contamination signals into the real METABENCH response matrix and measure DIF detection power under controlled conditions. (b) GSM8K/GSM1K provides independent cross-benchmark ground truth. (c) We explicitly characterize MMLU-CF's own reliability limitations before using it as validation.\n   - Evidence needed: plan_011 (semi-synthetic validation), plan_004 (GSM8K cross-validation)\n\n9. **\"Partial exploitation defeats DIF — RL models may only exploit p<1 of memorized items\"**\n   - Response: Formal power analysis as function of exploitation rate p shows: at p=1.0 DIF detects with TPR=0.72-0.85; at p=0.6 effect size shrinks ~0.6×, falling to medium range where ensemble's ConStat signal provides coverage. DIF + ensemble jointly cover p≥0.4. Below p=0.4, contamination impact on rankings is minimal.\n   - Evidence needed: plan_002 (partial exploitation analysis)\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  },
  "sourceToolAssistantUUID": "47e6c8c3-299b-46aa-88a0-a940d3a63aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T21:15:18.059Z_

<details><summary>↩ Tool result · `toolu_01UUb6kjHWnEoRLagRCvD9tj`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU全量DIF分析（5219模型×12508题），含时序/能力分组、负区分度敏感性、族内混淆控制、领域特异性分析",
5	    "results": {
6	      "full_pop_rmsea": 0.105,
7	      "full_pop_cfi": 0.82,
8	      "full_pop_tli": 0.79,
9	      "decoder_only_rmsea": 0.068,
10	      "temporal_dif_flags_ets_c_count": 485,
11	      "temporal_dif_flags_ets_b_count": 1120,
12	      "accuracy_quintile_dif_flags_ets_c_count": 390,
13	      "cohort_overlap_jaccard_c": 0.55,
14	      "mmlu_cf_validation_kappa": 0.14,
15	      "mmlu_cf_partial_correlation_with_dif": 0.18,
16	      "neg_disc_sensitivity_flag_change_pct": 12.3,
17	      "within_family_confound_overlap": 0.42,
18	      "within_family_llama_dif_flags": 68,
19	      "within_family_qwen_dif_flags": 52,
20	      "domain_specificity_chi2_p": 0.003,
21	      "stem_vs_humanities_dif_ratio": 1.45
22	    },
23	    "tables": [
24	      {
25	        "title": "Table 1: IRT Model Fit Diagnostics by Population",
26	        "columns": [
27	          "population",
28	          "N_models",
29	          "N_items",
30	          "RMSEA",
31	          "CFI",
32	          "TLI",
33	          "SRMR"
34	        ],
35	        "rows": [
36	          [
37	            "full_population",
38	            5219,
39	            12508,
40	            0.105,
41	            0.82,
42	            0.79,
43	            0.091
44	          ],
45	          [
46	            "decoder_only",
47	            3842,
48	            12508,
49	            0.068,
50	            0.92,
51	            0.9,
52	            0.054
53	          ],
54	          [
55	            "post_2023_decoder_only",
56	            1856,
57	            12508,
58	            0.072,
59	            0.91,
60	            0.89,
61	            0.058
62	          ]
63	        ]
64	      },
65	      {
66	        "title": "Table 2: DIF Detection Results by Cohort Definition",
67	        "columns": [
68	          "cohort_def",
69	          "N_focal",
70	          "N_ref",
71	          "ETS_C_flags",
72	          "ETS_B_flags",
73	          "ETS_A_pct"
74	        ],
75	        "rows": [
76	          [
77	            "temporal_2023v2024",
78	            656,
79	            1253,
80	            485,
81	            1120,
82	            87.2
83	          ],
84	          [
85	            "accuracy_quintile_Q5vQ1",
86	            1044,
87	            1044,
88	            390,
89	            980,
90	            89.1
91	          ],
92	          [
93	            "temporal_no_neg_disc",
94	            656,
95	            1253,
96	            427,
97	            985,
98	            88.5
99	          ]
100	        ]
101	      },
102	      {
103	        "title": "Table 3: Within-Family Confound Analysis",
104	        "columns": [
105	          "family",
106	          "N_models",
107	          "DIF_C_flags",
108	          "overlap_with_cross_cohort_pct"
109	        ],
110	        "rows": [
111	          [
112	            "Llama_2_to_3.1",
113	            38,
114	            68,
115	            44
116	          ],
117	          [
118	            "Qwen_1.5_to_2.5",
119	            29,
120	            52,
121	            39
122	          ],
123	          [
124	            "Mistral_Mixtral",
125	            22,
126	            41,
127	            43
128	          ],
129	          [
130	            "pooled_within_family",
131	            89,
132	            161,
133	            42
134	          ]
135	        ]
136	      }
137	    ],
138	    "figures": [],
139	    "analysis": "核心发现：DIF在真实数据上可检出大效应污染信号，但全群体IRT拟合不佳（RMSEA>0.08）迫使 结论限定于decoder-only子群体。Within-family混淆分析是本实验最关键的新贡献——42%重叠率 意味着近半数DIF标记可能是能力增长而非污染。这直接支持Claim 1降级为条件性陈述。 领域特异性分析提供了间接证据（STEM集中）但无法单独区分污染vs能力。 MMLU-CF验证基本失败（κ=0.14），需要plan_011的semi-synthetic验证来补救。 关键方法论贡献：首次报告大规模LLM群体IRT拟合诊断，揭示架构异质性是IRT应用于LLM评估的核心障碍。\n\n\n全群体IRT拟合边缘（RMSEA~0.105）因架构异质性（encoder-decoder、MoE混入decoder-only群体）违反单维性假设。 CFI/TLI低于0.90阈值确认模型误拟合。时序DIF标记约485个ETS-C级（3.9%题目），与模拟阶段预期的 大效应检测力一致。但within-family分析揭示42%标记在族内也出现，表明这些DIF可能反映 Llama-2→3的架构跃迁带来的能力增长而非污染。MMLU-CF验证受限于其自身低信度（κ=0.14）， 偏相关仅0.18，无法作为强验证。领域特异性显示STEM科目DIF比例高于人文1.45倍， 与已知的数学/代码领域污染重灾区一致，但也与这些领域能力增长更快的事实混淆。 负区分度题目移除后标记变化12.3%——非忽略不计但也未颠覆主结论。\n"
140	  },
141	  {
142	    "name": "rl_robustness_validation",
143	    "description": "DIF的RL鲁棒性实证验证：alignment-RL（DPO/ORPO）充分验证+reasoning-RL（GRPO/PPO）初步验证+部分利用功率分析",
144	    "results": {
145	      "sft_cohort_n": 1842,
146	      "alignment_rl_cohort_n": 477,
147	      "reasoning_rl_models_n": 13,
148	      "dif_retention_ratio_alignment_rl": 0.88,
149	      "dif_retention_ratio_reasoning_rl_mixed": 0.82,
150	      "dif_flag_jaccard_sft_vs_alignment": 0.76,
151	      "dif_flag_jaccard_sft_vs_sft_plus_rl": 0.71,
152	      "constat_auroc_non_rl": 0.62,
153	      "constat_auroc_alignment_rl": 0.58,
154	      "constat_auroc_reasoning_rl": 0.51,
155	      "mink_auroc_non_rl": 0.68,
156	      "mink_auroc_reasoning_rl": 0.49,
157	      "delong_dif_vs_constat_p": 0.008,
158	      "tost_dif_retention_equivalence_p": 0.03,
159	      "bootstrap_ci_dif_auroc_95": [
160	        0.74,
161	        0.86
162	      ],
163	      "partial_exploit_tpr_p1_0": 0.73,
164	      "partial_exploit_tpr_p0_8": 0.61,
165	      "partial_exploit_tpr_p0_6": 0.44,
166	      "partial_exploit_tpr_p0_4": 0.28,
167	      "partial_exploit_ensemble_handoff_p": 0.55
168	    },
169	    "tables": [
170	      {
171	        "title": "Table 4: DIF Robustness Across Training Paradigms",
172	        "columns": [
173	          "cohort_composition",
174	          "N_focal",
175	          "DIF_C_flags",
176	          "retention_ratio",
177	          "jaccard_vs_sft_baseline"
178	        ],
179	        "rows": [
180	          [
181	            "SFT_only_temporal",
182	            1842,
183	            485,
184	            1.0,
185	            1.0
186	          ],
187	          [
188	            "SFT_plus_alignment_RL",
189	            2319,
190	            452,
191	            0.88,
192	            0.76
193	          ],
194	          [
195	            "SFT_plus_all_RL",
196	            2332,
197	            438,
198	            0.82,
199	            0.71
200	          ]
201	        ]
202	      },
203	      {
204	        "title": "Table 5: Per-Model Detector AUROC Comparison",
205	        "columns": [
206	          "detector",
207	          "non_RL",
208	          "alignment_RL",
209	          "reasoning_RL",
210	          "delta_RL"
211	        ],
212	        "rows": [
213	          [
214	            "DIF_group_level",
215	            0.81,
216	            0.79,
217	            "N/A (group)",
218	            "—"
219	          ],
220	          [
221	            "ConStat",
222	            0.62,
223	            0.58,
224	            0.51,
225	            -0.11
226	          ],
227	          [
228	            "Min-K_pct",
229	            0.68,
230	            0.63,
231	            0.49,
232	            -0.19
233	          ],
234	          [
235	            "Perplexity",
236	            0.61,
237	            0.55,
238	            0.47,
239	            -0.14
240	          ]
241	        ]
242	      },
243	      {
244	        "title": "Table 6: Partial Exploitation Power Curve",
245	        "columns": [
246	          "exploitation_rate_p",
247	          "effective_delta",
248	          "dif_tpr",
249	          "constat_tpr",
250	          "ensemble_tpr"
251	        ],
252	        "rows": [
253	          [
254	            1.0,
255	            1.6,
256	            0.73,
257	            0.54,
258	            0.79
259	          ],
260	          [
261	            0.8,
262	            1.28,
263	            0.61,
264	            0.48,
265	            0.68
266	          ],
267	          [
268	            0.6,
269	            0.96,
270	            0.44,
271	            0.42,
272	            0.55
273	          ],
274	          [
275	            0.4,
276	            0.64,
277	            0.28,
278	            0.35,
279	            0.41
280	          ]
281	        ]
282	      }
283	    ],
284	    "figures": [],
285	    "analysis": "Alignment-RL鲁棒性结论扎实（大样本+统计显著）。Reasoning-RL结论只能写为\"初步实证支持\"—— 13个模型混入大cohort后检测力保持，但这更多反映群体统计的稀释效应而非真正的机制鲁棒性验证。 论文需诚实区分两种RL并承认reasoning-RL验证的样本局限。 部分利用分析提供了实用的检测边界图：p≥0.6时DIF主导，p∈[0.4,0.6]时需ensemble覆盖， p<0.4时检测力不足但污染对排名影响也可忽略——这个论证链条完整且可信。 对比实验清晰展示传统检测器在reasoning-RL下降至随机水平，而DIF保持—— 即使是有限样本下的这一对比也是有价值的实证贡献。\n\n\nAlignment-RL验证充分（N=477）：DIF保留率0.88表明DPO/ORPO不干扰群体级行为模式，因为 离线偏好优化不产生NLL gap收缩。标记Jaccard 0.76说明添加alignment-RL模型后DIF标记高度稳定。 ConStat和Min-K%在alignment-RL上仅轻微下降（非目标机制），但在reasoning-RL上ConStat降至0.51（接近随机）， Min-K%降至0.49，复现Wang et al.发现。\nReasoning-RL验证受限于样本量（仅13个模型）：DIF保留率0.82看似不错，但将13个模型混入 已有cohort后，它们对群体DIF的影响被稀释——这既是方法论优势（群体级统计天然鲁棒）， 也是验证的局限（无法确认在reasoning-RL占多数时DIF是否仍稳健）。Bootstrap CI较宽。 TOST等价性检验p=0.03勉强通过（α=0.05），但统计力不足以强声明。\n部分利用分析显示清晰的检测力衰减曲线：p=1.0时TPR=0.73与模拟一致， p=0.6时降至0.44（中等效应范围），p≈0.55处DIF与ConStat检测力交叉—— 这是ensemble handoff点，但因ConStat自身在RL下降质，实际coverage gap存在于 reasoning-RL+中等利用率区间。\n"
286	  },
287	  {
288	    "name": "constat_perturbation_eval",
289	    "description": "ConStat风格扰动检测独立评估：200+题目改写、FDR控制检测、按效应量和训练范式分层",
290	    "results": {
291	      "items_reformulated": 220,
292	      "reformulation_quality_human_eval": 0.87,
293	      "constat_auroc_all_models": 0.63,
294	      "constat_auroc_non_rl": 0.67,
295	      "constat_auroc_alignment_rl": 0.61,
296	      "constat_auroc_reasoning_rl": 0.52,
297	      "constat_fdr_controlled_flags": 145,
298	      "constat_fdr_level": 0.1,
299	      "constat_tpr_delta_ge_1_4": 0.48,
300	      "constat_tpr_delta_0_6_to_1_4": 0.35,
301	      "constat_fpr": 0.08,
302	      "constat_dif_flag_overlap_pct": 38
303	    },
304	    "tables": [
305	      {
306	        "title": "Table 7: ConStat Detection Performance by Model Type",
307	        "columns": [
308	          "model_type",
309	          "N_models",
310	          "AUROC",
311	          "TPR_at_FDR_0.10",
312	          "FPR"
313	        ],
314	        "rows": [
315	          [
316	            "all_models",
317	            5219,
318	            0.63,
319	            0.38,
320	            0.08
321	          ],
322	          [
323	            "non_RL",
324	            4742,
325	            0.67,
326	            0.44,
327	            0.07
328	          ],
329	          [
330	            "alignment_RL",
331	            477,
332	            0.61,
333	            0.36,
334	            0.09
335	          ],
336	          [
337	            "reasoning_RL",
338	            13,
339	            0.52,
340	            0.22,
341	            0.11
342	          ]
343	        ]
344	      }
345	    ],
346	    "figures": [],
347	    "analysis": "ConStat作为独立信号价值中等——对non-RL模型提供DIF的互补视角（per-model粒度）， 但在RL模型上失效。与DIF低重叠率（38%）证实两个信号正交性，为ensemble fusion提供基础。 结果质量足以支撑双信号ensemble叙事，但不足以单独支撑一个独立claim。\n\n\nConStat在non-RL模型上表现中等（AUROC 0.67），因为扰动敏感性在未经RL平滑的模型上 确实能捕捉到记忆痕迹——对原始问题正确但对语义等价改写错误。但AUROC远未达到 原论文报告的水平，因为：(1) MMLU是4选1MCQ，扰动空间有限（改写选项文本可能 改变难度而非仅测试记忆）；(2) 大规模改写的质量不均匀（人工评估87%可接受意味着 13%改写引入了构念偏移）。\nReasoning-RL模型上AUROC降至0.52（接近随机），复现Wang et al.的发现—— GRPO训练平滑了对扰动的敏感性差异。这正是ConStat的已知弱点，也是ensemble中 ConStat覆盖non-RL、DIF覆盖RL的分工基础。\nConStat与DIF标记仅38%重叠，说明两者捕捉不同信号维度——ConStat侧重per-model 扰动敏感性，DIF侧重group-level行为模式差异。这为ensemble互补性提供了实证基础。\n"
348	  },
349	  {
350	    "name": "dvd_generation_variance_eval",
351	    "description": "DVD生成方差检测独立评估：10-15个开放权重模型、50次采样/题、变体污染检测",
352	    "results": {
353	      "models_evaluated": 12,
354	      "items_evaluated": 500,
355	      "dvd_auroc_overall": 0.56,
356	      "dvd_auroc_verbatim_contamination": 0.53,
357	      "dvd_auroc_variant_contamination": 0.61,
358	      "dvd_tpr_variant_delta_ge_1_0": 0.42,
359	      "dvd_fpr": 0.14,
360	      "dvd_bimodal_detection_rate": 0.18,
361	      "dvd_dif_overlap_pct": 22,
362	      "dvd_constat_overlap_pct": 28
363	    },
364	    "tables": [
365	      {
366	        "title": "Table 8: DVD Detection Performance",
367	        "columns": [
368	          "contamination_type",
369	          "AUROC",
370	          "TPR_at_FPR_0.10",
371	          "FPR_at_TPR_0.50"
372	        ],
373	        "rows": [
374	          [
375	            "overall",
376	            0.56,
377	            0.31,
378	            0.35
379	          ],
380	          [
381	            "verbatim",
382	            0.53,
383	            0.24,
384	            0.41
385	          ],
386	          [
387	            "variant",
388	            0.61,
389	            0.42,
390	            0.22
391	          ]
392	        ]
393	      }
394	    ],
395	    "figures": [],
396	    "analysis": "DVD在MCQ场景下信号过弱，不足以作为ensemble的正式组件。AUROC 0.56和FPR 0.14 使其在任何实用阈值下都无法提供可靠检测。此结果应诚实报告并放入appendix， 作为\"DVD在MCQ场景下的局限性\"的实证贡献——这本身对社区有信息价值。 ensemble叙事需从三信号退化为双信号（DIF+ConStat）。\n\n\nDVD信号在median档显著弱于预期。根本原因：(1) 4选1 MCQ的生成方差信号本质微弱—— 模型输出是4个logit的softmax，即使记忆了答案，temperature sampling下的方差差异 远小于开放生成任务；(2) 仅12个模型的per-model方差估计噪声大；(3) 变体污染 （model见过问题变体而非原题）在MMLU上难以量化——没有ground truth标注哪些模型 见过哪些变体。\nAUROC 0.56整体上仅略优于随机。对变体污染略好（0.61）但FPR高达0.14， 实用价值有限。双峰分布检测率仅18%——大多数题目的生成方差分布是单峰的， 无法区分记忆vs非记忆。与DIF仅22%重叠表明DVD捕捉的是不同（但更弱）的信号。\n这一结果直接支持median叙事：DVD从ensemble的正式组成部分退化为appendix中的 探索性分析，ensemble从三信号简化为DIF+ConStat双信号。\n"
397	  },
398	  {
399	    "name": "ensemble_fusion",
400	    "description": "多信号ensemble融合：因DVD弱于预期，退化为DIF+ConStat双信号融合+DVD作为可选探索性第三信号",
401	    "results": {
402	      "ensemble_2signal_tpr_delta_ge_0_8": 0.58,
403	      "ensemble_2signal_fpr": 0.09,
404	      "ensemble_3signal_tpr_delta_ge_0_8": 0.55,
405	      "ensemble_3signal_fpr": 0.11,
406	      "dif_only_tpr_delta_ge_1_4": 0.73,
407	      "constat_only_tpr_delta_ge_0_6": 0.35,
408	      "ensemble_2signal_tpr_delta_ge_1_4": 0.78,
409	      "coverage_union_non_rl": 0.71,
410	      "coverage_union_all": 0.62,
411	      "majority_vote_2of2_tpr": 0.42,
412	      "weighted_fusion_auroc": 0.72,
413	      "uniform_weight_auroc": 0.69,
414	      "cv_5fold_auroc_std": 0.04
415	    },
416	    "tables": [
417	      {
418	        "title": "Table 9: Ensemble Detection Performance",
419	        "columns": [
420	          "ensemble_config",
421	          "TPR_delta_ge_0.8",
422	          "TPR_delta_ge_1.4",
423	          "FPR",
424	          "AUROC"
425	        ],
426	        "rows": [
427	          [
428	            "DIF_only",
429	            0.45,
430	            0.73,
431	            0.04,
432	            0.76
433	          ],
434	          [
435	            "ConStat_only",
436	            0.35,
437	            0.48,
438	            0.08,
439	            0.63
440	          ],
441	          [
442	            "DVD_only",
443	            0.22,
444	            0.31,
445	            0.14,
446	            0.56
447	          ],
448	          [
449	            "DIF_plus_ConStat_union",
450	            0.58,
451	            0.78,
452	            0.09,
453	            0.72
454	          ],
455	          [
456	            "DIF_plus_ConStat_plus_DVD",
457	            0.55,
458	            0.76,
459	            0.11,
460	            0.7
461	          ],
462	          [
463	            "DIF_plus_ConStat_intersection",
464	            0.42,
465	            0.52,
466	            0.03,
467	            "—"
468	          ]
469	        ]
470	      },
471	      {
472	        "title": "Table 10: Fusion Weight Analysis (5-fold CV)",
473	        "columns": [
474	          "method",
475	          "mean_AUROC",
476	          "std_AUROC",
477	          "DIF_weight",
478	          "ConStat_weight"
479	        ],
480	        "rows": [
481	          [
482	            "uniform",
483	            0.69,
484	            0.05,
485	            0.5,
486	            0.5
487	          ],
488	          [
489	            "optimized",
490	            0.72,
491	            0.04,
492	            0.62,
493	            0.38
494	          ]
495	        ]
496	      }
497	    ],
498	    "figures": [],
499	    "analysis": "Ensemble叙事需务实调整：不是\"三信号系统性覆盖全谱\"，而是\"DIF+ConStat双信号在各自优势区间互补， DIF主攻大效应+RL鲁棒，ConStat补充non-RL中效应检测\"。Coverage gap在reasoning-RL+中等效应区间 客观存在，需在论文中诚实标注。AUROC 0.72的双信号ensemble作为baseline有发表价值， 但不足以支撑\"全覆盖\"的强claim。Claim 2需相应弱化。\n\n\n双信号ensemble（DIF+ConStat）的核心价值在于coverage互补而非精度提升：DIF覆盖大效应+RL场景， ConStat覆盖中效应+non-RL场景。union coverage在non-RL模型上达0.71，但在含RL模型的 全群体上降至0.62（因ConStat在RL上失效，DIF对中效应力不足）。\n加入DVD第三信号后ensemble实际略微恶化（TPR持平但FPR从0.09升至0.11）， 因为DVD的高FPR稀释了ensemble精度。这进一步支持将DVD排除出正式ensemble。\n加权融合（AUROC 0.72）优于均匀权重（0.69）约3个点，但5-fold CV显示 标准差0.04，说明改善在噪声范围内——不足以支撑\"需要学习融合权重\"的claim， 应报告均匀权重为主结果。\n2-of-2多数投票TPR仅0.42——两个信号同时标记的题目太少，说明它们确实在 检测不同类型的污染，但intersection策略过于保守。\n"
500	  },
501	  {
502	    "name": "cross_benchmark_gsm8k",
503	    "description": "GSM8K跨benchmark DIF复现，以GSM1K为独立ground truth验证DIF标记的污染相关性",
504	    "results": {
505	      "gsm8k_models_collected": 62,
506	      "gsm8k_items": 1319,
507	      "gsm8k_dif_c_flags": 78,
508	      "gsm8k_dif_b_flags": 195,
509	      "gsm8k_gsm1k_gap_mean": 8.2,
510	      "gsm8k_gsm1k_gap_std": 11.4,
511	      "dif_gap_correlation_r": 0.36,
512	      "dif_gap_correlation_p": 0.004,
513	      "dif_flag_enrichment_in_high_gap_models": 1.8,
514	      "gsm8k_irt_rmsea": 0.075,
515	      "gsm8k_temporal_cohort_n_focal": 28,
516	      "gsm8k_temporal_cohort_n_ref": 34
517	    },
518	    "tables": [
519	      {
520	        "title": "Table 11: GSM8K DIF Analysis Summary",
521	        "columns": [
522	          "metric",
523	          "value"
524	        ],
525	        "rows": [
526	          [
527	            "models",
528	            62
529	          ],
530	          [
531	            "items",
532	            1319
533	          ],
534	          [
535	            "ETS_C_flags",
536	            78
537	          ],
538	          [
539	            "IRT_RMSEA",
540	            0.075
541	          ],
542	          [
543	            "DIF_gap_correlation_r",
544	            0.36
545	          ],
546	          [
547	            "DIF_gap_correlation_p",
548	            0.004
549	          ],
550	          [
551	            "flag_enrichment_ratio",
552	            1.8
553	          ]
554	        ]
555	      }
556	    ],
557	    "figures": [],
558	    "analysis": "跨benchmark验证达到\"有意义但不强\"的水平。r=0.36支持DIF捕捉与污染相关的信号， 但无法排除混淆因素（数学推理能力增长也会产生类似pattern）。模型数量限制是主要瓶颈。 论文中应作为corroborating evidence而非primary validation呈现。\n\n\nGSM8K验证提供了MMLU之外的独立实证但效果中等。DIF-gap相关r=0.36（p=0.004）统计显著 但效应量中等——远非完美验证。原因：(1) GSM8K模型数仅62个，cohort分组后每组不足35， 低于plan_001的80+阈值，DIF检测力受损；(2) GSM1K accuracy gap本身是model-level指标， 而DIF是item-level指标，粒度不匹配——需要通过模型级聚合（\"高DIF标记模型是否也是高gap模型\"） 间接关联，enrichment ratio 1.8说明存在关联但不强；(3) GSM8K的IRT拟合更好（RMSEA 0.075）， 因为数学推理在LLM群体中更接近单维构念，但模型数少削弱了统计力。\n此结果支撑\"DIF在多个benchmark上可复现\"的claim，但跨benchmark验证力度有限。 作为supplementary evidence足够，不应作为主要验证手段。\n"
559	  },
560	  {
561	    "name": "bifactor_irt_equating_pilot",
562	    "description": "MMLU bifactor IRT拟合+锚题选取+固定参数校准替换题等价性pilot验证",
563	    "results": {
564	      "bifactor_converged": true,
565	      "bifactor_general_factor_variance_explained": 0.58,
566	      "bifactor_n_subjects_with_strong_specific_factor": 38,
567	      "bifactor_n_subjects_with_weak_specific_factor": 19,
568	      "bifactor_rmsea": 0.062,
569	      "anchor_items_selected": 620,
570	      "anchor_items_pct": 5.0,
571	      "anchor_stability_across_cohorts_icc": 0.94,
572	      "equated_score_spearman_rho": 0.93,
573	      "equated_vs_unequated_rank_shift_median": 2.1,
574	      "equated_vs_unequated_rank_shift_95pct": 8.4,
575	      "weak_factor_subjects": [
576	        "abstract_algebra",
577	        "formal_logic",
578	        "jurisprudence",
579	        "moral_scenarios"
580	      ]
581	    },
582	    "tables": [
583	      {
584	        "title": "Table 12: Bifactor Model Fit",
585	        "columns": [
586	          "model",
587	          "population",
588	          "RMSEA",
589	          "CFI",
590	          "TLI",
591	          "variance_general"
592	        ],
593	        "rows": [
594	          [
595	            "unidimensional",
596	            "full_pop",
597	            0.105,
598	            0.82,
599	            0.79,
600	            "—"
601	          ],
602	          [
603	            "unidimensional",
604	            "decoder_only",
605	            0.068,
606	            0.92,
607	            0.9,
608	            "—"
609	          ],
610	          [
611	            "bifactor",
612	            "decoder_only",
613	            0.062,
614	            0.94,
615	            0.92,
616	            0.58
617	          ]
618	        ]
619	      },
620	      {
621	        "title": "Table 13: Equating Results",
622	        "columns": [
623	          "metric",
624	          "value"
625	        ],
626	        "rows": [
627	          [
628	            "anchor_items",
629	            620
630	          ],
631	          [
632	            "equated_spearman_rho",
633	            0.93
634	          ],
635	          [
636	            "median_rank_shift",
637	            2.1
638	          ],
639	          [
640	            "95pct_rank_shift",
641	            8.4
642	          ],
643	          [
644	            "weak_factor_subjects_count",
645	            19
646	          ]
647	        ]
648	      }
649	    ],
650	    "figures": [],
651	    "analysis": "Bifactor equating在pilot规模上\"基本可行但有结构性限制\"。rho=0.93对pilot而言合理， 但弱因子科目是系统性瓶颈——这些科目需要额外的构念验证或更大的校准样本。 论文中Claim 3需加\"pilot-scale\"限定，并诚实报告弱因子科目的局限。 方法论贡献：首次对MMLU进行bifactor IRT分析，揭示其多维结构特征。\n\n\nBifactor模型收敛但部分科目因子载荷弱——这是MMLU固有结构问题。MMLU的57个科目中， 38个（67%）有强特定因子（标准化载荷>0.3），说明确实存在学科特异性维度。 但19个科目（33%）特定因子弱（载荷<0.2），这些科目的题目本质上只加载在一般因子上， 意味着它们的替换题校准可能不稳定（缺乏学科维度锚定）。\n锚题池620个（5%）看似充足，但因为弱因子科目的题目不适合做锚题， 实际可用锚题在这些科目上稀疏。整体等价Spearman rho=0.93接近但未达到0.95目标—— 差距来源于弱因子科目的替换题校准误差。中位排名位移2.1位可接受， 但95百分位8.4位意味着5%的模型排名变动超过8位——在竞争性leaderboard上非trivial。\nRMSEA 0.062（bifactor on decoder-only subpop）比单因子0.105大幅改善， 确认多维IRT建模的必要性和可行性。\n"
652	  },
653	  {
654	    "name": "item_generation_calibration",
655	    "description": "DIF标记题替换生成+student simulation校准+与prompt-based难度定向对比",
656	    "results": {
657	      "items_generated": 150,
658	      "items_passing_construct_filter": 112,
659	      "student_sim_difficulty_correlation_rho": 0.78,
660	      "prompt_based_difficulty_correlation_rho": 0.28,
661	      "holdout_panel_n_models": 50,
662	      "holdout_equated_rho": 0.91,
663	      "difficulty_mse_student_sim": 0.34,
664	      "difficulty_mse_prompt_based": 1.85,
665	      "construct_validity_factor_loading_mean": 0.41,
666	      "generation_failure_rate": 0.25
667	    },
668	    "tables": [
669	      {
670	        "title": "Table 14: Item Generation & Calibration",
671	        "columns": [
672	          "method",
673	          "difficulty_rho",
674	          "difficulty_MSE",
675	          "N_items"
676	        ],
677	        "rows": [
678	          [
679	            "student_simulation",
680	            0.78,
681	            0.34,
682	            112
683	          ],
684	          [
685	            "prompt_based_targeting",
686	            0.28,
687	            1.85,
688	            112
689	          ],
690	          [
691	            "random_same_subject",
692	            0.11,
693	            2.4,
694	            112
695	          ]
696	        ]
697	      },
698	      {
699	        "title": "Table 15: Holdout Validation",
700	        "columns": [
701	          "metric",
702	          "original_items",
703	          "replaced_items"
704	        ],
705	        "rows": [
706	          [
707	            "spearman_rho_vs_full",
708	            "—",
709	            0.91
710	          ],
711	          [
712	            "mean_factor_loading",
713	            0.5,
714	            0.41
715	          ],
716	          [
717	            "difficulty_mean",
718	            0.52,
719	            0.49
720	          ],
721	          [
722	            "discrimination_mean",
723	            1.18,
724	            0.95
725	          ]
726	        ]
727	      }
728	    ],
729	    "figures": [],
730	    "analysis": "Student simulation校准是可发表的方法论贡献。但替换题整体质量（因子载荷0.41、区分度0.95） 系统性低于原题，说明LLM生成的MCQ在构念纯度上仍有差距。Claim 3应定位为 \"方法论框架+pilot验证\"而非\"可部署的再生系统\"。\n\n\nStudent simulation校准（rho=0.78）显著优于prompt-based难度定向（rho=0.28）， 复现并扩展arXiv 2601.09953的发现。这是因为student simulation直接模拟目标群体 （LLM）的应答行为来估计难度，而prompt-based方法依赖LLM对自身难度的元认知—— 已知LLM的自我难度评估与实际表现弱相关。\n但holdout验证的equated rho仅0.91，低于plan_005的0.93——因为替换题引入了 额外的构念偏移（生成质量不完美）。25%的生成失败率（不满足构念约束）说明 自动化替换仍需人工审核。通过构念filter的112题平均因子载荷0.41（vs原题~0.50）， 表明替换题的构念对齐性有系统性衰减。\n核心方法论贡献是student simulation vs prompt-based的对比实验—— 这在现有文献中缺乏大规模实证。但端到端质量（rho 0.91）不足以支撑\"自动化再生\"的强claim。\n"
731	  },
732	  {
733	    "name": "cumulative_bayesian_dif",
734	    "description": "累积贝叶斯DIF先验模拟：4次连续benchmark施测的功率累积",
735	    "results": {
736	      "single_admin_power_delta_1_0": 0.38,
737	      "cumulative_2_admin_power": 0.52,
738	      "cumulative_3_admin_power": 0.65,
739	      "cumulative_4_admin_power": 0.72,
740	      "power_improvement_per_admin": [
741	        0.14,
742	        0.13,
743	        0.07
744	      ],
745	      "bayes_factor_threshold": 3.0,
746	      "false_positive_rate_cumulative": 0.06
747	    },
748	    "tables": [
749	      {
750	        "title": "Table S1: Cumulative Bayesian DIF Power",
751	        "columns": [
752	          "n_administrations",
753	          "power_delta_1_0",
754	          "power_delta_1_4",
755	          "fpr"
756	        ],
757	        "rows": [
758	          [
759	            1,
760	            0.38,
761	            0.73,
762	            0.04
763	          ],
764	          [
765	            2,
766	            0.52,
767	            0.82,
768	            0.05
769	          ],
770	          [
771	            3,
772	            0.65,
773	            0.88,
774	            0.05
775	          ],
776	          [
777	            4,
778	            0.72,
779	            0.91,
780	            0.06
781	          ]
782	        ]
783	      }
784	    ],
785	    "figures": [],
786	    "analysis": "累积贝叶斯DIF提供了优雅的理论框架但实证验证仅为模拟。作为supplementary结果 支持\"DIF监控随时间增强\"的叙事足够，但不应作为主文核心贡献。\n\n\n单次施测对中等效应（δ=1.0）功率仅0.38，反映classical DIF对中等效应的固有局限。 累积贝叶斯先验通过将前次分析的后验作为下次先验，逐步积累证据。3次后功率从0.38升至0.65—— 显著提升但未达0.70目标。第4次边际收益递减（+0.07），因为先验已较informative。\nFPR从单次的0.04小幅上升至累积的0.06——贝叶斯累积也累积了假阳性证据， 但受BF阈值控制仍在可接受范围。\n此结果支持\"DIF作为持续监控工具\"的叙事——单次快照检测力有限， 但随时间累积可覆盖中等效应。纯模拟结果，P2优先级，放supplementary materials。\n"
787	  },
788	  {
789	    "name": "graceful_degradation_analysis",
790	    "description": "渐进替换下benchmark效度衰退分析：5%-50%替换率的排名稳定性/信度/构念覆盖",
791	    "results": {
792	      "rho_5pct_replaced": 0.98,
793	      "rho_10pct_replaced": 0.96,
794	      "rho_20pct_replaced": 0.93,
795	      "rho_50pct_replaced": 0.85,
796	      "reliability_alpha_original": 0.94,
797	      "reliability_alpha_20pct_replaced": 0.91,
798	      "construct_coverage_original": 1.0,
799	      "construct_coverage_20pct_replaced": 0.89,
800	      "theoretical_bound_validity_loss_rate": 0.003,
801	      "critical_replacement_threshold": 0.28
802	    },
803	    "tables": [
804	      {
805	        "title": "Table S2: Graceful Degradation Metrics",
806	        "columns": [
807	          "replacement_pct",
808	          "spearman_rho",
809	          "cronbach_alpha",
810	          "construct_coverage"
811	        ],
812	        "rows": [
813	          [
814	            0,
815	            1.0,
816	            0.94,
817	            1.0
818	          ],
819	          [
820	            5,
821	            0.98,
822	            0.93,
823	            0.97
824	          ],
825	          [
826	            10,
827	            0.96,
828	            0.93,
829	            0.94
830	          ],
831	          [
832	            20,
833	            0.93,
834	            0.91,
835	            0.89
836	          ],
837	          [
838	            50,
839	            0.85,
840	            0.86,
841	            0.74
842	          ]
843	        ]
844	      }
845	    ],
846	    "figures": [],
847	    "analysis": "提供了实用的替换预算指导：20%以内替换是安全区间，28%是临界点。 但这依赖于plan_006的替换题质量——如果替换题质量提升，曲线会更平缓。 P2优先级结果，支持Claim 3的\"有限替换下等价性可维持\"子论点。\n\n\n渐进替换的效度衰退遵循近似线性规律：每替换10%题目，Spearman rho下降约0.03-0.04。 这比理论最优（完美替换题下rho应保持0.99+）差，因为plan_006已显示替换题的 构念纯度系统性低于原题（因子载荷0.41 vs 0.50）。\n20%替换时rho=0.93、信度0.91，勉强可接受。50%时rho降至0.85——排名变动过大， 不再算\"等价benchmark\"。临界替换率约28%——超过此点效度加速下降。\n构念覆盖在20%替换时降至0.89，因为弱因子科目的替换题无法维持原有的 学科维度覆盖。这与plan_005识别的19个弱因子科目一致。\n"
848	  },
849	  {
850	    "name": "item_focused_trees",
851	    "description": "Item-Focused Trees：将发布日期作为连续协变量的DIF检测替代方法",
852	    "results": {
853	      "ift_n_items_flagged": 520,
854	      "ift_overlap_with_ets_c": 0.62,
855	      "ift_auc": 0.78,
856	      "ift_tpr_delta_ge_1_4": 0.69,
857	      "ift_fpr": 0.07,
858	      "ift_split_point_date": "2023-09",
859	      "ift_advantage_no_arbitrary_cohort": true,
860	      "ift_computational_cost_minutes": 45
861	    },
862	    "tables": [
863	      {
864	        "title": "Table S3: IFT vs ETS-C DIF Comparison",
865	        "columns": [
866	          "method",
867	          "flags",
868	          "TPR_ge_1.4",
869	          "FPR",
870	          "AUC",
871	          "overlap"
872	        ],
873	        "rows": [
874	          [
875	            "ETS_C",
876	            485,
877	            0.73,
878	            0.04,
879	            0.76,
880	            "—"
881	          ],
882	          [
883	            "IFT",
884	            520,
885	            0.69,
886	            0.07,
887	            0.78,
888	            0.62
889	          ]
890	        ]
891	      }
892	    ],
893	    "figures": [],
894	    "analysis": "IFT作为methodological alternative有价值——避免任意cohort分割，提供连续视角。 与ETS-C互补（不同false positive/negative tradeoff）。P2优先级， 适合放supplementary作为robustness check。\n\n\nIFT将发布日期作为连续协变量，避免了plan_001中任意时序cohort分割的问题。 AUC 0.78略高于ETS-C categorical DIF（因为连续建模不丢失信息），但TPR 0.69 略低于ETS-C的0.73（因为树分割不如参数化DIF统计效率高）。\n自动学到的分割点2023-09与直觉一致——这大约是LLM训练数据中benchmark泄露 开始加速的时间点。与ETS-C标记62%重叠说明两种方法捕捉相似但不完全相同的信号—— IFT额外标记的题目可能反映了渐进式污染（而非二元的污染/未污染）。\nFPR 0.07略高于ETS-C的0.04——树方法的灵活性代价。计算成本45分钟可接受。\n"
895	  },
896	  {
897	    "name": "architecture_stratified_dif",
898	    "description": "架构分层DIF：decoder-only子群体IRT拟合诊断+DIF检测对比全群体",
899	    "results": {
900	      "decoder_only_n": 3842,
901	      "decoder_only_rmsea": 0.068,
902	      "decoder_only_cfi": 0.92,
903	      "decoder_only_tli": 0.9,
904	      "decoder_only_srmr": 0.054,
905	      "full_pop_rmsea": 0.105,
906	      "rmsea_improvement": 0.037,
907	      "decoder_only_dif_c_flags": 410,
908	      "decoder_only_dif_fpr": 0.035,
909	      "decoder_only_dif_tpr_est": 0.71,
910	      "full_pop_dif_c_flags": 485,
911	      "spurious_dif_reduction_pct": 18,
912	      "flag_overlap_jaccard": 0.72
913	    },
914	    "tables": [
915	      {
916	        "title": "Table 16: Architecture Stratification Effect on IRT Fit",
917	        "columns": [
918	          "population",
919	          "N",
920	          "RMSEA",
921	          "CFI",
922	          "TLI",
923	          "SRMR",
924	          "DIF_C_flags"
925	        ],
926	        "rows": [
927	          [
928	            "full_population",
929	            5219,
930	            0.105,
931	            0.82,
932	            0.79,
933	            0.091,
934	            485
935	          ],
936	          [
937	            "decoder_only",
938	            3842,
939	            0.068,
940	            0.92,
941	            0.9,
942	            0.054,
943	            410
944	          ],
945	          [
946	            "encoder_decoder",
947	            312,
948	            0.088,
949	            0.87,
950	            0.85,
951	            0.072,
952	            "—"
953	          ],
954	          [
955	            "MoE",
956	            198,
957	            0.095,
958	            0.84,
959	            0.82,
960	            0.081,
961	            "—"
962	          ]
963	        ]
964	      },
965	      {
966	        "title": "Table 17: Spurious DIF Analysis",
967	        "columns": [
968	          "metric",
969	          "full_pop",
970	          "decoder_only",
971	          "delta"
972	        ],
973	        "rows": [
974	          [
975	            "ETS_C_flags",
976	            485,
977	            410,
978	            -75
979	          ],
980	          [
981	            "FPR",
982	            0.04,
983	            0.035,
984	            -0.005
985	          ],
986	          [
987	            "spurious_flag_pct",
988	            "—",
989	            "—",
990	            15.5
991	          ]
992	        ]
993	      }
994	    ],
995	    "figures": [],
996	    "analysis": "这是median档最关键的实验之一。结论清晰：DIF需要架构同质子群体才能获得可靠的IRT拟合， 这是一个可操作的约束（实践中只需筛选decoder-only模型）而非根本性缺陷。 RMSEA从0.105降至0.068的改善幅度为Claim 1的条件性陈述提供了直接实证支持。 作为首个大规模LLM群体IRT拟合诊断，本身具有独立发表价值。\n\n\n架构分层后IRT拟合显著改善：RMSEA从0.105降至0.068（跨过0.08阈值进入\"可接受\"区间）， CFI/TLI达到0.90+。这确认了架构异质性是全群体IRT误拟合的主要来源——不同架构 （encoder-decoder、MoE、dense decoder-only）的应答模式存在系统性差异， 违反单维性假设。\nDIF标记从485减至410（减少15%），FPR从0.04降至0.035，说明约75个全群体DIF标记 是架构差异引起的spurious DIF而非真实污染信号。Spurious DIF减少18% 是非忽略不计的改善。标记重叠Jaccard 0.72说明核心污染信号在分层后保持稳定。\n这一结果直接支持median叙事的核心约束：DIF需在架构同质子群体上运行。 同时提供了首个大规模LLM群体IRT拟合诊断分析——揭示架构异质性对心理测量建模的影响， 这本身是独立的方法论贡献。\n"
997	  },
998	  {
999	    "name": "semi_synthetic_contamination_validation",
1000	    "description": "半合成污染注入验证：在真实METABENCH矩阵上注入已知污染信号，测量DIF检测力",
1001	    "results": {
1002	      "clean_items_selected": 500,
1003	      "injection_items": 150,
1004	      "semi_synthetic_tpr_delta_ge_1_4": 0.58,
1005	      "semi_synthetic_tpr_delta_ge_1_0": 0.41,
1006	      "semi_synthetic_tpr_delta_ge_0_6": 0.25,
1007	      "semi_synthetic_fpr": 0.07,
1008	      "tpr_by_prevalence_5pct": 0.52,
1009	      "tpr_by_prevalence_15pct": 0.58,
1010	      "tpr_by_prevalence_30pct": 0.63,
1011	      "tpr_by_exploitation_rate_1_0": 0.65,
1012	      "tpr_by_exploitation_rate_0_8": 0.54,
1013	      "tpr_by_exploitation_rate_0_6": 0.38,
1014	      "tpr_by_exploitation_rate_0_4": 0.22,
1015	      "tpr_by_focal_n_40": 0.44,
1016	      "tpr_by_focal_n_80": 0.58,
1017	      "tpr_by_focal_n_200": 0.68,
1018	      "power_surface_r2": 0.89
1019	    },
1020	    "tables": [
1021	      {
1022	        "title": "Table 18: Semi-Synthetic Validation — TPR by Effect Size",
1023	        "columns": [
1024	          "delta_threshold",
1025	          "TPR",
1026	          "FPR",
1027	          "n_injected"
1028	        ],
1029	        "rows": [
1030	          [
1031	            "≥1.4",
1032	            0.58,
1033	            0.07,
1034	            45
1035	          ],
1036	          [
1037	            "≥1.0",
1038	            0.41,
1039	            0.07,
1040	            85
1041	          ],
1042	          [
1043	            "≥0.6",
1044	            0.25,
1045	            0.07,
1046	            150
1047	          ]
1048	        ]
1049	      },
1050	      {
1051	        "title": "Table 19: Semi-Synthetic Power Surface",
1052	        "columns": [
1053	          "parameter",
1054	          "low",
1055	          "mid",
1056	          "high",
1057	          "tpr_low",
1058	          "tpr_mid",
1059	          "tpr_high"
1060	        ],
1061	        "rows": [
1062	          [
1063	            "exploitation_rate",
1064	            0.4,
1065	            0.7,
1066	            1.0,
1067	            0.22,
1068	            0.45,
1069	            0.65
1070	          ],
1071	          [
1072	            "focal_n",
1073	            40,
1074	            80,
1075	            200,
1076	            0.44,
1077	            0.58,
1078	            0.68
1079	          ],
1080	          [
1081	            "prevalence",
1082	            0.05,
1083	            0.15,
1084	            0.3,
1085	            0.52,
1086	            0.58,
1087	            0.63
1088	          ]
1089	        ]
1090	      },
1091	      {
1092	        "title": "Table 20: Simulation vs Semi-Synthetic Gap",
1093	        "columns": [
1094	          "metric",
1095	          "simulation",
1096	          "semi_synthetic",
1097	          "gap"
1098	        ],
1099	        "rows": [
1100	          [
1101	            "TPR_delta_ge_1.4",
1102	            0.73,
1103	            0.58,
1104	            -0.15
1105	          ],
1106	          [
1107	            "FPR",
1108	            0.04,
1109	            0.07,
1110	            0.03
1111	          ],
1112	          [
1113	            "AUC",
1114	            0.94,
1115	            0.82,
1116	            -0.12
1117	          ]
1118	        ]
1119	      }
1120	    ],
1121	    "figures": [],
1122	    "analysis": "Semi-synthetic验证提供了最可靠的ground truth评估，同时揭示了模拟-真实gap（TPR差距0.15）。 这个gap本身是重要发现——说明纯模拟评估高估了DIF在真实数据上的检测力。 功率曲面提供了实用的操作指南（需要多大N、什么效应量范围可检测）。 方法论贡献：semi-synthetic验证框架本身作为污染检测器评估的通用工具， 可推广到评估任何item-level检测方法，独立于DIF的具体结果。 此实验是Claim 1降级为条件性陈述的直接实证基础——\"实用检测力\"而非\"高检测力\"。\n\nSemi-synthetic验证是解决ground truth困境的核心实验。TPR=0.58（δ≥1.4）低于 纯模拟的0.72-0.73——这个差距是median档的关键特征，原因是真实METABENCH矩阵 包含模拟中不存在的噪声源：(1) 真实IRT参数分布比模拟假设的更偏斜（负区分度15%题目）； (2) 真实群体能力分布非正态（双峰，低能力模型集中在45-50%准确率）； (3) 注入污染叠加在可能已有的真实污染之上，导致clean baseline不完全干净。\nFPR 0.07（在0.05-0.10范围内）——略高于模拟的0.04，因为真实数据中存在 plan_001揭示的background DIF（能力增长、架构差异引起的non-contamination DIF）。\n参数扫描揭示了清晰的检测力依赖关系：exploitation rate是最强决定因素（从p=1.0到p=0.4， TPR从0.65降至0.22），focal group size次之（N=40时TPR=0.44，N=200时0.68）， 污染prevalence影响最小（5%→30%仅+0.11 TPR）。功率曲面R²=0.89说明检测力 可被这三个参数well-characterized。\n真实数据效应量分布偏向中等（δ 1.0-1.4）而非模拟中均匀分布的大效应， 这是检测力下降的另一来源——在实际污染场景中，多数污染的效应量在medium range， 正好是DIF检测力最敏感的衰减区间。\n"
1123	  }
1124	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd7dfa61-42c8-4620-b9be-785461d1aa48",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "97f0cdaf-b53d-481e-bb33-53e068590c82",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU全量DIF分析（5219模型×12508题），含时序/能力分组、负区分度敏感性、族内混淆控制、领域特异性分析\",\n    \"results\": {\n      \"full_pop_rmsea\": 0.105,\n      \"full_pop_cfi\": 0.82,\n      \"full_pop_tli\": 0.79,\n      \"decoder_only_rmsea\": 0.068,\n      \"temporal_dif_flags_ets_c_count\": 485,\n      \"temporal_dif_flags_ets_b_count\": 1120,\n      \"accuracy_quintile_dif_flags_ets_c_count\": 390,\n      \"cohort_overlap_jaccard_c\": 0.55,\n      \"mmlu_cf_validation_kappa\": 0.14,\n      \"mmlu_cf_partial_correlation_with_dif\": 0.18,\n      \"neg_disc_sensitivity_flag_change_pct\": 12.3,\n      \"within_family_confound_overlap\": 0.42,\n      \"within_family_llama_dif_flags\": 68,\n      \"within_family_qwen_dif_flags\": 52,\n      \"domain_specificity_chi2_p\": 0.003,\n      \"stem_vs_humanities_dif_ratio\": 1.45\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 1: IRT Model Fit Diagnostics by Population\",\n        \"columns\": [\n          \"population\",\n          \"N_models\",\n          \"N_items\",\n          \"RMSEA\",\n          \"CFI\",\n          \"TLI\",\n          \"SRMR\"\n        ],\n        \"rows\": [\n          [\n            \"full_population\",\n            5219,\n            12508,\n            0.105,\n            0.82,\n            0.79,\n            0.091\n          ],\n          [\n            \"decoder_only\",\n            3842,\n            12508,\n            0.068,\n            0.92,\n            0.9,\n            0.054\n          ],\n          [\n            \"post_2023_decoder_only\",\n            1856,\n            12508,\n            0.072,\n            0.91,\n            0.89,\n            0.058\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 2: DIF Detection Results by Cohort Definition\",\n        \"columns\": [\n          \"cohort_def\",\n          \"N_focal\",\n          \"N_ref\",\n          \"ETS_C_flags\",\n          \"ETS_B_flags\",\n          \"ETS_A_pct\"\n        ],\n        \"rows\": [\n          [\n            \"temporal_2023v2024\",\n            656,\n            1253,\n            485,\n            1120,\n            87.2\n          ],\n          [\n            \"accuracy_quintile_Q5vQ1\",\n            1044,\n            1044,\n            390,\n            980,\n            89.1\n          ],\n          [\n            \"temporal_no_neg_disc\",\n            656,\n            1253,\n            427,\n            985,\n            88.5\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 3: Within-Family Confound Analysis\",\n        \"columns\": [\n          \"family\",\n          \"N_models\",\n          \"DIF_C_flags\",\n          \"overlap_with_cross_cohort_pct\"\n        ],\n        \"rows\": [\n          [\n            \"Llama_2_to_3.1\",\n            38,\n            68,\n            44\n          ],\n          [\n            \"Qwen_1.5_to_2.5\",\n            29,\n            52,\n            39\n          ],\n          [\n            \"Mistral_Mixtral\",\n            22,\n            41,\n            43\n          ],\n          [\n            \"pooled_within_family\",\n            89,\n            161,\n            42\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：DIF在真实数据上可检出大效应污染信号，但全群体IRT拟合不佳（RMSEA>0.08）迫使 结论限定于decoder-only子群体。Within-family混淆分析是本实验最关键的新贡献——42%重叠率 意味着近半数DIF标记可能是能力增长而非污染。这直接支持Claim 1降级为条件性陈述。 领域特异性分析提供了间接证据（STEM集中）但无法单独区分污染vs能力。 MMLU-CF验证基本失败（κ=0.14），需要plan_011的semi-synthetic验证来补救。 关键方法论贡献：首次报告大规模LLM群体IRT拟合诊断，揭示架构异质性是IRT应用于LLM评估的核心障碍。\\n\\n\\n全群体IRT拟合边缘（RMSEA~0.105）因架构异质性（encoder-decoder、MoE混入decoder-only群体）违反单维性假设。 CFI/TLI低于0.90阈值确认模型误拟合。时序DIF标记约485个ETS-C级（3.9%题目），与模拟阶段预期的 大效应检测力一致。但within-family分析揭示42%标记在族内也出现，表明这些DIF可能反映 Llama-2→3的架构跃迁带来的能力增长而非污染。MMLU-CF验证受限于其自身低信度（κ=0.14）， 偏相关仅0.18，无法作为强验证。领域特异性显示STEM科目DIF比例高于人文1.45倍， 与已知的数学/代码领域污染重灾区一致，但也与这些领域能力增长更快的事实混淆。 负区分度题目移除后标记变化12.3%——非忽略不计但也未颠覆主结论。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"DIF的RL鲁棒性实证验证：alignment-RL（DPO/ORPO）充分验证+reasoning-RL（GRPO/PPO）初步验证+部分利用功率分析\",\n    \"results\": {\n      \"sft_cohort_n\": 1842,\n      \"alignment_rl_cohort_n\": 477,\n      \"reasoning_rl_models_n\": 13,\n      \"dif_retention_ratio_alignment_rl\": 0.88,\n      \"dif_retention_ratio_reasoning_rl_mixed\": 0.82,\n      \"dif_flag_jaccard_sft_vs_alignment\": 0.76,\n      \"dif_flag_jaccard_sft_vs_sft_plus_rl\": 0.71,\n      \"constat_auroc_non_rl\": 0.62,\n      \"constat_auroc_alignment_rl\": 0.58,\n      \"constat_auroc_reasoning_rl\": 0.51,\n      \"mink_auroc_non_rl\": 0.68,\n      \"mink_auroc_reasoning_rl\": 0.49,\n      \"delong_dif_vs_constat_p\": 0.008,\n      \"tost_dif_retention_equivalence_p\": 0.03,\n      \"bootstrap_ci_dif_auroc_95\": [\n        0.74,\n        0.86\n      ],\n      \"partial_exploit_tpr_p1_0\": 0.73,\n      \"partial_exploit_tpr_p0_8\": 0.61,\n      \"partial_exploit_tpr_p0_6\": 0.44,\n      \"partial_exploit_tpr_p0_4\": 0.28,\n      \"partial_exploit_ensemble_handoff_p\": 0.55\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 4: DIF Robustness Across Training Paradigms\",\n        \"columns\": [\n          \"cohort_composition\",\n          \"N_focal\",\n          \"DIF_C_flags\",\n          \"retention_ratio\",\n          \"jaccard_vs_sft_baseline\"\n        ],\n        \"rows\": [\n          [\n            \"SFT_only_temporal\",\n            1842,\n            485,\n            1.0,\n            1.0\n          ],\n          [\n            \"SFT_plus_alignment_RL\",\n            2319,\n            452,\n            0.88,\n            0.76\n          ],\n          [\n            \"SFT_plus_all_RL\",\n            2332,\n            438,\n            0.82,\n            0.71\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 5: Per-Model Detector AUROC Comparison\",\n        \"columns\": [\n          \"detector\",\n          \"non_RL\",\n          \"alignment_RL\",\n          \"reasoning_RL\",\n          \"delta_RL\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_group_level\",\n            0.81,\n            0.79,\n            \"N/A (group)\",\n            \"—\"\n          ],\n          [\n            \"ConStat\",\n            0.62,\n            0.58,\n            0.51,\n            -0.11\n          ],\n          [\n            \"Min-K_pct\",\n            0.68,\n            0.63,\n            0.49,\n            -0.19\n          ],\n          [\n            \"Perplexity\",\n            0.61,\n            0.55,\n            0.47,\n            -0.14\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 6: Partial Exploitation Power Curve\",\n        \"columns\": [\n          \"exploitation_rate_p\",\n          \"effective_delta\",\n          \"dif_tpr\",\n          \"constat_tpr\",\n          \"ensemble_tpr\"\n        ],\n        \"rows\": [\n          [\n            1.0,\n            1.6,\n            0.73,\n            0.54,\n            0.79\n          ],\n          [\n            0.8,\n            1.28,\n            0.61,\n            0.48,\n            0.68\n          ],\n          [\n            0.6,\n            0.96,\n            0.44,\n            0.42,\n            0.55\n          ],\n          [\n            0.4,\n            0.64,\n            0.28,\n            0.35,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Alignment-RL鲁棒性结论扎实（大样本+统计显著）。Reasoning-RL结论只能写为\\\"初步实证支持\\\"—— 13个模型混入大cohort后检测力保持，但这更多反映群体统计的稀释效应而非真正的机制鲁棒性验证。 论文需诚实区分两种RL并承认reasoning-RL验证的样本局限。 部分利用分析提供了实用的检测边界图：p≥0.6时DIF主导，p∈[0.4,0.6]时需ensemble覆盖， p<0.4时检测力不足但污染对排名影响也可忽略——这个论证链条完整且可信。 对比实验清晰展示传统检测器在reasoning-RL下降至随机水平，而DIF保持—— 即使是有限样本下的这一对比也是有价值的实证贡献。\\n\\n\\nAlignment-RL验证充分（N=477）：DIF保留率0.88表明DPO/ORPO不干扰群体级行为模式，因为 离线偏好优化不产生NLL gap收缩。标记Jaccard 0.76说明添加alignment-RL模型后DIF标记高度稳定。 ConStat和Min-K%在alignment-RL上仅轻微下降（非目标机制），但在reasoning-RL上ConStat降至0.51（接近随机）， Min-K%降至0.49，复现Wang et al.发现。\\nReasoning-RL验证受限于样本量（仅13个模型）：DIF保留率0.82看似不错，但将13个模型混入 已有cohort后，它们对群体DIF的影响被稀释——这既是方法论优势（群体级统计天然鲁棒）， 也是验证的局限（无法确认在reasoning-RL占多数时DIF是否仍稳健）。Bootstrap CI较宽。 TOST等价性检验p=0.03勉强通过（α=0.05），但统计力不足以强声明。\\n部分利用分析显示清晰的检测力衰减曲线：p=1.0时TPR=0.73与模拟一致， p=0.6时降至0.44（中等效应范围），p≈0.55处DIF与ConStat检测力交叉—— 这是ensemble handoff点，但因ConStat自身在RL下降质，实际coverage gap存在于 reasoning-RL+中等利用率区间。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat风格扰动检测独立评估：200+题目改写、FDR控制检测、按效应量和训练范式分层\",\n    \"results\": {\n      \"items_reformulated\": 220,\n      \"reformulation_quality_human_eval\": 0.87,\n      \"constat_auroc_all_models\": 0.63,\n      \"constat_auroc_non_rl\": 0.67,\n      \"constat_auroc_alignment_rl\": 0.61,\n      \"constat_auroc_reasoning_rl\": 0.52,\n      \"constat_fdr_controlled_flags\": 145,\n      \"constat_fdr_level\": 0.1,\n      \"constat_tpr_delta_ge_1_4\": 0.48,\n      \"constat_tpr_delta_0_6_to_1_4\": 0.35,\n      \"constat_fpr\": 0.08,\n      \"constat_dif_flag_overlap_pct\": 38\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 7: ConStat Detection Performance by Model Type\",\n        \"columns\": [\n          \"model_type\",\n          \"N_models\",\n          \"AUROC\",\n          \"TPR_at_FDR_0.10\",\n          \"FPR\"\n        ],\n        \"rows\": [\n          [\n            \"all_models\",\n            5219,\n            0.63,\n            0.38,\n            0.08\n          ],\n          [\n            \"non_RL\",\n            4742,\n            0.67,\n            0.44,\n            0.07\n          ],\n          [\n            \"alignment_RL\",\n            477,\n            0.61,\n            0.36,\n            0.09\n          ],\n          [\n            \"reasoning_RL\",\n            13,\n            0.52,\n            0.22,\n            0.11\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat作为独立信号价值中等——对non-RL模型提供DIF的互补视角（per-model粒度）， 但在RL模型上失效。与DIF低重叠率（38%）证实两个信号正交性，为ensemble fusion提供基础。 结果质量足以支撑双信号ensemble叙事，但不足以单独支撑一个独立claim。\\n\\n\\nConStat在non-RL模型上表现中等（AUROC 0.67），因为扰动敏感性在未经RL平滑的模型上 确实能捕捉到记忆痕迹——对原始问题正确但对语义等价改写错误。但AUROC远未达到 原论文报告的水平，因为：(1) MMLU是4选1MCQ，扰动空间有限（改写选项文本可能 改变难度而非仅测试记忆）；(2) 大规模改写的质量不均匀（人工评估87%可接受意味着 13%改写引入了构念偏移）。\\nReasoning-RL模型上AUROC降至0.52（接近随机），复现Wang et al.的发现—— GRPO训练平滑了对扰动的敏感性差异。这正是ConStat的已知弱点，也是ensemble中 ConStat覆盖non-RL、DIF覆盖RL的分工基础。\\nConStat与DIF标记仅38%重叠，说明两者捕捉不同信号维度——ConStat侧重per-model 扰动敏感性，DIF侧重group-level行为模式差异。这为ensemble互补性提供了实证基础。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD生成方差检测独立评估：10-15个开放权重模型、50次采样/题、变体污染检测\",\n    \"results\": {\n      \"models_evaluated\": 12,\n      \"items_evaluated\": 500,\n      \"dvd_auroc_overall\": 0.56,\n      \"dvd_auroc_verbatim_contamination\": 0.53,\n      \"dvd_auroc_variant_contamination\": 0.61,\n      \"dvd_tpr_variant_delta_ge_1_0\": 0.42,\n      \"dvd_fpr\": 0.14,\n      \"dvd_bimodal_detection_rate\": 0.18,\n      \"dvd_dif_overlap_pct\": 22,\n      \"dvd_constat_overlap_pct\": 28\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 8: DVD Detection Performance\",\n        \"columns\": [\n          \"contamination_type\",\n          \"AUROC\",\n          \"TPR_at_FPR_0.10\",\n          \"FPR_at_TPR_0.50\"\n        ],\n        \"rows\": [\n          [\n            \"overall\",\n            0.56,\n            0.31,\n            0.35\n          ],\n          [\n            \"verbatim\",\n            0.53,\n            0.24,\n            0.41\n          ],\n          [\n            \"variant\",\n            0.61,\n            0.42,\n            0.22\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD在MCQ场景下信号过弱，不足以作为ensemble的正式组件。AUROC 0.56和FPR 0.14 使其在任何实用阈值下都无法提供可靠检测。此结果应诚实报告并放入appendix， 作为\\\"DVD在MCQ场景下的局限性\\\"的实证贡献——这本身对社区有信息价值。 ensemble叙事需从三信号退化为双信号（DIF+ConStat）。\\n\\n\\nDVD信号在median档显著弱于预期。根本原因：(1) 4选1 MCQ的生成方差信号本质微弱—— 模型输出是4个logit的softmax，即使记忆了答案，temperature sampling下的方差差异 远小于开放生成任务；(2) 仅12个模型的per-model方差估计噪声大；(3) 变体污染 （model见过问题变体而非原题）在MMLU上难以量化——没有ground truth标注哪些模型 见过哪些变体。\\nAUROC 0.56整体上仅略优于随机。对变体污染略好（0.61）但FPR高达0.14， 实用价值有限。双峰分布检测率仅18%——大多数题目的生成方差分布是单峰的， 无法区分记忆vs非记忆。与DIF仅22%重叠表明DVD捕捉的是不同（但更弱）的信号。\\n这一结果直接支持median叙事：DVD从ensemble的正式组成部分退化为appendix中的 探索性分析，ensemble从三信号简化为DIF+ConStat双信号。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"多信号ensemble融合：因DVD弱于预期，退化为DIF+ConStat双信号融合+DVD作为可选探索性第三信号\",\n    \"results\": {\n      \"ensemble_2signal_tpr_delta_ge_0_8\": 0.58,\n      \"ensemble_2signal_fpr\": 0.09,\n      \"ensemble_3signal_tpr_delta_ge_0_8\": 0.55,\n      \"ensemble_3signal_fpr\": 0.11,\n      \"dif_only_tpr_delta_ge_1_4\": 0.73,\n      \"constat_only_tpr_delta_ge_0_6\": 0.35,\n      \"ensemble_2signal_tpr_delta_ge_1_4\": 0.78,\n      \"coverage_union_non_rl\": 0.71,\n      \"coverage_union_all\": 0.62,\n      \"majority_vote_2of2_tpr\": 0.42,\n      \"weighted_fusion_auroc\": 0.72,\n      \"uniform_weight_auroc\": 0.69,\n      \"cv_5fold_auroc_std\": 0.04\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 9: Ensemble Detection Performance\",\n        \"columns\": [\n          \"ensemble_config\",\n          \"TPR_delta_ge_0.8\",\n          \"TPR_delta_ge_1.4\",\n          \"FPR\",\n          \"AUROC\"\n        ],\n        \"rows\": [\n          [\n            \"DIF_only\",\n            0.45,\n            0.73,\n            0.04,\n            0.76\n          ],\n          [\n            \"ConStat_only\",\n            0.35,\n            0.48,\n            0.08,\n            0.63\n          ],\n          [\n            \"DVD_only\",\n            0.22,\n            0.31,\n            0.14,\n            0.56\n          ],\n          [\n            \"DIF_plus_ConStat_union\",\n            0.58,\n            0.78,\n            0.09,\n            0.72\n          ],\n          [\n            \"DIF_plus_ConStat_plus_DVD\",\n            0.55,\n            0.76,\n            0.11,\n            0.7\n          ],\n          [\n            \"DIF_plus_ConStat_intersection\",\n            0.42,\n            0.52,\n            0.03,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 10: Fusion Weight Analysis (5-fold CV)\",\n        \"columns\": [\n          \"method\",\n          \"mean_AUROC\",\n          \"std_AUROC\",\n          \"DIF_weight\",\n          \"ConStat_weight\"\n        ],\n        \"rows\": [\n          [\n            \"uniform\",\n            0.69,\n            0.05,\n            0.5,\n            0.5\n          ],\n          [\n            \"optimized\",\n            0.72,\n            0.04,\n            0.62,\n            0.38\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble叙事需务实调整：不是\\\"三信号系统性覆盖全谱\\\"，而是\\\"DIF+ConStat双信号在各自优势区间互补， DIF主攻大效应+RL鲁棒，ConStat补充non-RL中效应检测\\\"。Coverage gap在reasoning-RL+中等效应区间 客观存在，需在论文中诚实标注。AUROC 0.72的双信号ensemble作为baseline有发表价值， 但不足以支撑\\\"全覆盖\\\"的强claim。Claim 2需相应弱化。\\n\\n\\n双信号ensemble（DIF+ConStat）的核心价值在于coverage互补而非精度提升：DIF覆盖大效应+RL场景， ConStat覆盖中效应+non-RL场景。union coverage在non-RL模型上达0.71，但在含RL模型的 全群体上降至0.62（因ConStat在RL上失效，DIF对中效应力不足）。\\n加入DVD第三信号后ensemble实际略微恶化（TPR持平但FPR从0.09升至0.11）， 因为DVD的高FPR稀释了ensemble精度。这进一步支持将DVD排除出正式ensemble。\\n加权融合（AUROC 0.72）优于均匀权重（0.69）约3个点，但5-fold CV显示 标准差0.04，说明改善在噪声范围内——不足以支撑\\\"需要学习融合权重\\\"的claim， 应报告均匀权重为主结果。\\n2-of-2多数投票TPR仅0.42——两个信号同时标记的题目太少，说明它们确实在 检测不同类型的污染，但intersection策略过于保守。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K跨benchmark DIF复现，以GSM1K为独立ground truth验证DIF标记的污染相关性\",\n    \"results\": {\n      \"gsm8k_models_collected\": 62,\n      \"gsm8k_items\": 1319,\n      \"gsm8k_dif_c_flags\": 78,\n      \"gsm8k_dif_b_flags\": 195,\n      \"gsm8k_gsm1k_gap_mean\": 8.2,\n      \"gsm8k_gsm1k_gap_std\": 11.4,\n      \"dif_gap_correlation_r\": 0.36,\n      \"dif_gap_correlation_p\": 0.004,\n      \"dif_flag_enrichment_in_high_gap_models\": 1.8,\n      \"gsm8k_irt_rmsea\": 0.075,\n      \"gsm8k_temporal_cohort_n_focal\": 28,\n      \"gsm8k_temporal_cohort_n_ref\": 34\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 11: GSM8K DIF Analysis Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"models\",\n            62\n          ],\n          [\n            \"items\",\n            1319\n          ],\n          [\n            \"ETS_C_flags\",\n            78\n          ],\n          [\n            \"IRT_RMSEA\",\n            0.075\n          ],\n          [\n            \"DIF_gap_correlation_r\",\n            0.36\n          ],\n          [\n            \"DIF_gap_correlation_p\",\n            0.004\n          ],\n          [\n            \"flag_enrichment_ratio\",\n            1.8\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"跨benchmark验证达到\\\"有意义但不强\\\"的水平。r=0.36支持DIF捕捉与污染相关的信号， 但无法排除混淆因素（数学推理能力增长也会产生类似pattern）。模型数量限制是主要瓶颈。 论文中应作为corroborating evidence而非primary validation呈现。\\n\\n\\nGSM8K验证提供了MMLU之外的独立实证但效果中等。DIF-gap相关r=0.36（p=0.004）统计显著 但效应量中等——远非完美验证。原因：(1) GSM8K模型数仅62个，cohort分组后每组不足35， 低于plan_001的80+阈值，DIF检测力受损；(2) GSM1K accuracy gap本身是model-level指标， 而DIF是item-level指标，粒度不匹配——需要通过模型级聚合（\\\"高DIF标记模型是否也是高gap模型\\\"） 间接关联，enrichment ratio 1.8说明存在关联但不强；(3) GSM8K的IRT拟合更好（RMSEA 0.075）， 因为数学推理在LLM群体中更接近单维构念，但模型数少削弱了统计力。\\n此结果支撑\\\"DIF在多个benchmark上可复现\\\"的claim，但跨benchmark验证力度有限。 作为supplementary evidence足够，不应作为主要验证手段。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"MMLU bifactor IRT拟合+锚题选取+固定参数校准替换题等价性pilot验证\",\n    \"results\": {\n      \"bifactor_converged\": true,\n      \"bifactor_general_factor_variance_explained\": 0.58,\n      \"bifactor_n_subjects_with_strong_specific_factor\": 38,\n      \"bifactor_n_subjects_with_weak_specific_factor\": 19,\n      \"bifactor_rmsea\": 0.062,\n      \"anchor_items_selected\": 620,\n      \"anchor_items_pct\": 5.0,\n      \"anchor_stability_across_cohorts_icc\": 0.94,\n      \"equated_score_spearman_rho\": 0.93,\n      \"equated_vs_unequated_rank_shift_median\": 2.1,\n      \"equated_vs_unequated_rank_shift_95pct\": 8.4,\n      \"weak_factor_subjects\": [\n        \"abstract_algebra\",\n        \"formal_logic\",\n        \"jurisprudence\",\n        \"moral_scenarios\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 12: Bifactor Model Fit\",\n        \"columns\": [\n          \"model\",\n          \"population\",\n          \"RMSEA\",\n          \"CFI\",\n          \"TLI\",\n          \"variance_general\"\n        ],\n        \"rows\": [\n          [\n            \"unidimensional\",\n            \"full_pop\",\n            0.105,\n            0.82,\n            0.79,\n            \"—\"\n          ],\n          [\n            \"unidimensional\",\n            \"decoder_only\",\n            0.068,\n            0.92,\n            0.9,\n            \"—\"\n          ],\n          [\n            \"bifactor\",\n            \"decoder_only\",\n            0.062,\n            0.94,\n            0.92,\n            0.58\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 13: Equating Results\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"anchor_items\",\n            620\n          ],\n          [\n            \"equated_spearman_rho\",\n            0.93\n          ],\n          [\n            \"median_rank_shift\",\n            2.1\n          ],\n          [\n            \"95pct_rank_shift\",\n            8.4\n          ],\n          [\n            \"weak_factor_subjects_count\",\n            19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor equating在pilot规模上\\\"基本可行但有结构性限制\\\"。rho=0.93对pilot而言合理， 但弱因子科目是系统性瓶颈——这些科目需要额外的构念验证或更大的校准样本。 论文中Claim 3需加\\\"pilot-scale\\\"限定，并诚实报告弱因子科目的局限。 方法论贡献：首次对MMLU进行bifactor IRT分析，揭示其多维结构特征。\\n\\n\\nBifactor模型收敛但部分科目因子载荷弱——这是MMLU固有结构问题。MMLU的57个科目中， 38个（67%）有强特定因子（标准化载荷>0.3），说明确实存在学科特异性维度。 但19个科目（33%）特定因子弱（载荷<0.2），这些科目的题目本质上只加载在一般因子上， 意味着它们的替换题校准可能不稳定（缺乏学科维度锚定）。\\n锚题池620个（5%）看似充足，但因为弱因子科目的题目不适合做锚题， 实际可用锚题在这些科目上稀疏。整体等价Spearman rho=0.93接近但未达到0.95目标—— 差距来源于弱因子科目的替换题校准误差。中位排名位移2.1位可接受， 但95百分位8.4位意味着5%的模型排名变动超过8位——在竞争性leaderboard上非trivial。\\nRMSEA 0.062（bifactor on decoder-only subpop）比单因子0.105大幅改善， 确认多维IRT建模的必要性和可行性。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"DIF标记题替换生成+student simulation校准+与prompt-based难度定向对比\",\n    \"results\": {\n      \"items_generated\": 150,\n      \"items_passing_construct_filter\": 112,\n      \"student_sim_difficulty_correlation_rho\": 0.78,\n      \"prompt_based_difficulty_correlation_rho\": 0.28,\n      \"holdout_panel_n_models\": 50,\n      \"holdout_equated_rho\": 0.91,\n      \"difficulty_mse_student_sim\": 0.34,\n      \"difficulty_mse_prompt_based\": 1.85,\n      \"construct_validity_factor_loading_mean\": 0.41,\n      \"generation_failure_rate\": 0.25\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 14: Item Generation & Calibration\",\n        \"columns\": [\n          \"method\",\n          \"difficulty_rho\",\n          \"difficulty_MSE\",\n          \"N_items\"\n        ],\n        \"rows\": [\n          [\n            \"student_simulation\",\n            0.78,\n            0.34,\n            112\n          ],\n          [\n            \"prompt_based_targeting\",\n            0.28,\n            1.85,\n            112\n          ],\n          [\n            \"random_same_subject\",\n            0.11,\n            2.4,\n            112\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 15: Holdout Validation\",\n        \"columns\": [\n          \"metric\",\n          \"original_items\",\n          \"replaced_items\"\n        ],\n        \"rows\": [\n          [\n            \"spearman_rho_vs_full\",\n            \"—\",\n            0.91\n          ],\n          [\n            \"mean_factor_loading\",\n            0.5,\n            0.41\n          ],\n          [\n            \"difficulty_mean\",\n            0.52,\n            0.49\n          ],\n          [\n            \"discrimination_mean\",\n            1.18,\n            0.95\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Student simulation校准是可发表的方法论贡献。但替换题整体质量（因子载荷0.41、区分度0.95） 系统性低于原题，说明LLM生成的MCQ在构念纯度上仍有差距。Claim 3应定位为 \\\"方法论框架+pilot验证\\\"而非\\\"可部署的再生系统\\\"。\\n\\n\\nStudent simulation校准（rho=0.78）显著优于prompt-based难度定向（rho=0.28）， 复现并扩展arXiv 2601.09953的发现。这是因为student simulation直接模拟目标群体 （LLM）的应答行为来估计难度，而prompt-based方法依赖LLM对自身难度的元认知—— 已知LLM的自我难度评估与实际表现弱相关。\\n但holdout验证的equated rho仅0.91，低于plan_005的0.93——因为替换题引入了 额外的构念偏移（生成质量不完美）。25%的生成失败率（不满足构念约束）说明 自动化替换仍需人工审核。通过构念filter的112题平均因子载荷0.41（vs原题~0.50）， 表明替换题的构念对齐性有系统性衰减。\\n核心方法论贡献是student simulation vs prompt-based的对比实验—— 这在现有文献中缺乏大规模实证。但端到端质量（rho 0.91）不足以支撑\\\"自动化再生\\\"的强claim。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"累积贝叶斯DIF先验模拟：4次连续benchmark施测的功率累积\",\n    \"results\": {\n      \"single_admin_power_delta_1_0\": 0.38,\n      \"cumulative_2_admin_power\": 0.52,\n      \"cumulative_3_admin_power\": 0.65,\n      \"cumulative_4_admin_power\": 0.72,\n      \"power_improvement_per_admin\": [\n        0.14,\n        0.13,\n        0.07\n      ],\n      \"bayes_factor_threshold\": 3.0,\n      \"false_positive_rate_cumulative\": 0.06\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table S1: Cumulative Bayesian DIF Power\",\n        \"columns\": [\n          \"n_administrations\",\n          \"power_delta_1_0\",\n          \"power_delta_1_4\",\n          \"fpr\"\n        ],\n        \"rows\": [\n          [\n            1,\n            0.38,\n            0.73,\n            0.04\n          ],\n          [\n            2,\n            0.52,\n            0.82,\n            0.05\n          ],\n          [\n            3,\n            0.65,\n            0.88,\n            0.05\n          ],\n          [\n            4,\n            0.72,\n            0.91,\n            0.06\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"累积贝叶斯DIF提供了优雅的理论框架但实证验证仅为模拟。作为supplementary结果 支持\\\"DIF监控随时间增强\\\"的叙事足够，但不应作为主文核心贡献。\\n\\n\\n单次施测对中等效应（δ=1.0）功率仅0.38，反映classical DIF对中等效应的固有局限。 累积贝叶斯先验通过将前次分析的后验作为下次先验，逐步积累证据。3次后功率从0.38升至0.65—— 显著提升但未达0.70目标。第4次边际收益递减（+0.07），因为先验已较informative。\\nFPR从单次的0.04小幅上升至累积的0.06——贝叶斯累积也累积了假阳性证据， 但受BF阈值控制仍在可接受范围。\\n此结果支持\\\"DIF作为持续监控工具\\\"的叙事——单次快照检测力有限， 但随时间累积可覆盖中等效应。纯模拟结果，P2优先级，放supplementary materials。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"渐进替换下benchmark效度衰退分析：5%-50%替换率的排名稳定性/信度/构念覆盖\",\n    \"results\": {\n      \"rho_5pct_replaced\": 0.98,\n      \"rho_10pct_replaced\": 0.96,\n      \"rho_20pct_replaced\": 0.93,\n      \"rho_50pct_replaced\": 0.85,\n      \"reliability_alpha_original\": 0.94,\n      \"reliability_alpha_20pct_replaced\": 0.91,\n      \"construct_coverage_original\": 1.0,\n      \"construct_coverage_20pct_replaced\": 0.89,\n      \"theoretical_bound_validity_loss_rate\": 0.003,\n      \"critical_replacement_threshold\": 0.28\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table S2: Graceful Degradation Metrics\",\n        \"columns\": [\n          \"replacement_pct\",\n          \"spearman_rho\",\n          \"cronbach_alpha\",\n          \"construct_coverage\"\n        ],\n        \"rows\": [\n          [\n            0,\n            1.0,\n            0.94,\n            1.0\n          ],\n          [\n            5,\n            0.98,\n            0.93,\n            0.97\n          ],\n          [\n            10,\n            0.96,\n            0.93,\n            0.94\n          ],\n          [\n            20,\n            0.93,\n            0.91,\n            0.89\n          ],\n          [\n            50,\n            0.85,\n            0.86,\n            0.74\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"提供了实用的替换预算指导：20%以内替换是安全区间，28%是临界点。 但这依赖于plan_006的替换题质量——如果替换题质量提升，曲线会更平缓。 P2优先级结果，支持Claim 3的\\\"有限替换下等价性可维持\\\"子论点。\\n\\n\\n渐进替换的效度衰退遵循近似线性规律：每替换10%题目，Spearman rho下降约0.03-0.04。 这比理论最优（完美替换题下rho应保持0.99+）差，因为plan_006已显示替换题的 构念纯度系统性低于原题（因子载荷0.41 vs 0.50）。\\n20%替换时rho=0.93、信度0.91，勉强可接受。50%时rho降至0.85——排名变动过大， 不再算\\\"等价benchmark\\\"。临界替换率约28%——超过此点效度加速下降。\\n构念覆盖在20%替换时降至0.89，因为弱因子科目的替换题无法维持原有的 学科维度覆盖。这与plan_005识别的19个弱因子科目一致。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees：将发布日期作为连续协变量的DIF检测替代方法\",\n    \"results\": {\n      \"ift_n_items_flagged\": 520,\n      \"ift_overlap_with_ets_c\": 0.62,\n      \"ift_auc\": 0.78,\n      \"ift_tpr_delta_ge_1_4\": 0.69,\n      \"ift_fpr\": 0.07,\n      \"ift_split_point_date\": \"2023-09\",\n      \"ift_advantage_no_arbitrary_cohort\": true,\n      \"ift_computational_cost_minutes\": 45\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table S3: IFT vs ETS-C DIF Comparison\",\n        \"columns\": [\n          \"method\",\n          \"flags\",\n          \"TPR_ge_1.4\",\n          \"FPR\",\n          \"AUC\",\n          \"overlap\"\n        ],\n        \"rows\": [\n          [\n            \"ETS_C\",\n            485,\n            0.73,\n            0.04,\n            0.76,\n            \"—\"\n          ],\n          [\n            \"IFT\",\n            520,\n            0.69,\n            0.07,\n            0.78,\n            0.62\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT作为methodological alternative有价值——避免任意cohort分割，提供连续视角。 与ETS-C互补（不同false positive/negative tradeoff）。P2优先级， 适合放supplementary作为robustness check。\\n\\n\\nIFT将发布日期作为连续协变量，避免了plan_001中任意时序cohort分割的问题。 AUC 0.78略高于ETS-C categorical DIF（因为连续建模不丢失信息），但TPR 0.69 略低于ETS-C的0.73（因为树分割不如参数化DIF统计效率高）。\\n自动学到的分割点2023-09与直觉一致——这大约是LLM训练数据中benchmark泄露 开始加速的时间点。与ETS-C标记62%重叠说明两种方法捕捉相似但不完全相同的信号—— IFT额外标记的题目可能反映了渐进式污染（而非二元的污染/未污染）。\\nFPR 0.07略高于ETS-C的0.04——树方法的灵活性代价。计算成本45分钟可接受。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"架构分层DIF：decoder-only子群体IRT拟合诊断+DIF检测对比全群体\",\n    \"results\": {\n      \"decoder_only_n\": 3842,\n      \"decoder_only_rmsea\": 0.068,\n      \"decoder_only_cfi\": 0.92,\n      \"decoder_only_tli\": 0.9,\n      \"decoder_only_srmr\": 0.054,\n      \"full_pop_rmsea\": 0.105,\n      \"rmsea_improvement\": 0.037,\n      \"decoder_only_dif_c_flags\": 410,\n      \"decoder_only_dif_fpr\": 0.035,\n      \"decoder_only_dif_tpr_est\": 0.71,\n      \"full_pop_dif_c_flags\": 485,\n      \"spurious_dif_reduction_pct\": 18,\n      \"flag_overlap_jaccard\": 0.72\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 16: Architecture Stratification Effect on IRT Fit\",\n        \"columns\": [\n          \"population\",\n          \"N\",\n          \"RMSEA\",\n          \"CFI\",\n          \"TLI\",\n          \"SRMR\",\n          \"DIF_C_flags\"\n        ],\n        \"rows\": [\n          [\n            \"full_population\",\n            5219,\n            0.105,\n            0.82,\n            0.79,\n            0.091,\n            485\n          ],\n          [\n            \"decoder_only\",\n            3842,\n            0.068,\n            0.92,\n            0.9,\n            0.054,\n            410\n          ],\n          [\n            \"encoder_decoder\",\n            312,\n            0.088,\n            0.87,\n            0.85,\n            0.072,\n            \"—\"\n          ],\n          [\n            \"MoE\",\n            198,\n            0.095,\n            0.84,\n            0.82,\n            0.081,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 17: Spurious DIF Analysis\",\n        \"columns\": [\n          \"metric\",\n          \"full_pop\",\n          \"decoder_only\",\n          \"delta\"\n        ],\n        \"rows\": [\n          [\n            \"ETS_C_flags\",\n            485,\n            410,\n            -75\n          ],\n          [\n            \"FPR\",\n            0.04,\n            0.035,\n            -0.005\n          ],\n          [\n            \"spurious_flag_pct\",\n            \"—\",\n            \"—\",\n            15.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是median档最关键的实验之一。结论清晰：DIF需要架构同质子群体才能获得可靠的IRT拟合， 这是一个可操作的约束（实践中只需筛选decoder-only模型）而非根本性缺陷。 RMSEA从0.105降至0.068的改善幅度为Claim 1的条件性陈述提供了直接实证支持。 作为首个大规模LLM群体IRT拟合诊断，本身具有独立发表价值。\\n\\n\\n架构分层后IRT拟合显著改善：RMSEA从0.105降至0.068（跨过0.08阈值进入\\\"可接受\\\"区间）， CFI/TLI达到0.90+。这确认了架构异质性是全群体IRT误拟合的主要来源——不同架构 （encoder-decoder、MoE、dense decoder-only）的应答模式存在系统性差异， 违反单维性假设。\\nDIF标记从485减至410（减少15%），FPR从0.04降至0.035，说明约75个全群体DIF标记 是架构差异引起的spurious DIF而非真实污染信号。Spurious DIF减少18% 是非忽略不计的改善。标记重叠Jaccard 0.72说明核心污染信号在分层后保持稳定。\\n这一结果直接支持median叙事的核心约束：DIF需在架构同质子群体上运行。 同时提供了首个大规模LLM群体IRT拟合诊断分析——揭示架构异质性对心理测量建模的影响， 这本身是独立的方法论贡献。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"半合成污染注入验证：在真实METABENCH矩阵上注入已知污染信号，测量DIF检测力\",\n    \"results\": {\n      \"clean_items_selected\": 500,\n      \"injection_items\": 150,\n      \"semi_synthetic_tpr_delta_ge_1_4\": 0.58,\n      \"semi_synthetic_tpr_delta_ge_1_0\": 0.41,\n      \"semi_synthetic_tpr_delta_ge_0_6\": 0.25,\n      \"semi_synthetic_fpr\": 0.07,\n      \"tpr_by_prevalence_5pct\": 0.52,\n      \"tpr_by_prevalence_15pct\": 0.58,\n      \"tpr_by_prevalence_30pct\": 0.63,\n      \"tpr_by_exploitation_rate_1_0\": 0.65,\n      \"tpr_by_exploitation_rate_0_8\": 0.54,\n      \"tpr_by_exploitation_rate_0_6\": 0.38,\n      \"tpr_by_exploitation_rate_0_4\": 0.22,\n      \"tpr_by_focal_n_40\": 0.44,\n      \"tpr_by_focal_n_80\": 0.58,\n      \"tpr_by_focal_n_200\": 0.68,\n      \"power_surface_r2\": 0.89\n    },\n    \"tables\": [\n      {\n        \"title\": \"Table 18: Semi-Synthetic Validation — TPR by Effect Size\",\n        \"columns\": [\n          \"delta_threshold\",\n          \"TPR\",\n          \"FPR\",\n          \"n_injected\"\n        ],\n        \"rows\": [\n          [\n            \"≥1.4\",\n            0.58,\n            0.07,\n            45\n          ],\n          [\n            \"≥1.0\",\n            0.41,\n            0.07,\n            85\n          ],\n          [\n            \"≥0.6\",\n            0.25,\n            0.07,\n            150\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 19: Semi-Synthetic Power Surface\",\n        \"columns\": [\n          \"parameter\",\n          \"low\",\n          \"mid\",\n          \"high\",\n          \"tpr_low\",\n          \"tpr_mid\",\n          \"tpr_high\"\n        ],\n        \"rows\": [\n          [\n            \"exploitation_rate\",\n            0.4,\n            0.7,\n            1.0,\n            0.22,\n            0.45,\n            0.65\n          ],\n          [\n            \"focal_n\",\n            40,\n            80,\n            200,\n            0.44,\n            0.58,\n            0.68\n          ],\n          [\n            \"prevalence\",\n            0.05,\n            0.15,\n            0.3,\n            0.52,\n            0.58,\n            0.63\n          ]\n        ]\n      },\n      {\n        \"title\": \"Table 20: Simulation vs Semi-Synthetic Gap\",\n        \"columns\": [\n          \"metric\",\n          \"simulation\",\n          \"semi_synthetic\",\n          \"gap\"\n        ],\n        \"rows\": [\n          [\n            \"TPR_delta_ge_1.4\",\n            0.73,\n            0.58,\n            -0.15\n          ],\n          [\n            \"FPR\",\n            0.04,\n            0.07,\n            0.03\n          ],\n          [\n            \"AUC\",\n            0.94,\n            0.82,\n            -0.12\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic验证提供了最可靠的ground truth评估，同时揭示了模拟-真实gap（TPR差距0.15）。 这个gap本身是重要发现——说明纯模拟评估高估了DIF在真实数据上的检测力。 功率曲面提供了实用的操作指南（需要多大N、什么效应量范围可检测）。 方法论贡献：semi-synthetic验证框架本身作为污染检测器评估的通用工具， 可推广到评估任何item-level检测方法，独立于DIF的具体结果。 此实验是Claim 1降级为条件性陈述的直接实证基础——\\\"实用检测力\\\"而非\\\"高检测力\\\"。\\n\\nSemi-synthetic验证是解决ground truth困境的核心实验。TPR=0.58（δ≥1.4）低于 纯模拟的0.72-0.73——这个差距是median档的关键特征，原因是真实METABENCH矩阵 包含模拟中不存在的噪声源：(1) 真实IRT参数分布比模拟假设的更偏斜（负区分度15%题目）； (2) 真实群体能力分布非正态（双峰，低能力模型集中在45-50%准确率）； (3) 注入污染叠加在可能已有的真实污染之上，导致clean baseline不完全干净。\\nFPR 0.07（在0.05-0.10范围内）——略高于模拟的0.04，因为真实数据中存在 plan_001揭示的background DIF（能力增长、架构差异引起的non-contamination DIF）。\\n参数扫描揭示了清晰的检测力依赖关系：exploitation rate是最强决定因素（从p=1.0到p=0.4， TPR从0.65降至0.22），focal group size次之（N=40时TPR=0.44，N=200时0.68）， 污染prevalence影响最小（5%→30%仅+0.11 TPR）。功率曲面R²=0.89说明检测力 可被这三个参数well-characterized。\\n真实数据效应量分布偏向中等（δ 1.0-1.4）而非模拟中均匀分布的大效应， 这是检测力下降的另一来源——在实际污染场景中，多数污染的效应量在medium range， 正好是DIF检测力最敏感的衰减区间。\\n\"\n  }\n]",
      "numLines": 1124,
      "startLine": 1,
      "totalLines": 1124
    }
  },
  "sourceToolAssistantUUID": "bd7dfa61-42c8-4620-b9be-785461d1aa48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "97f0cdaf-b53d-481e-bb33-53e068590c82",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT methodology",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Assistant

_source line 14 · 2026-05-20T21:15:21.550Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both files. Let me also check if the output directory exists and if pdflatex is available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97f0cdaf-b53d-481e-bb33-53e068590c82",
  "isSidechain": false,
  "requestId": "req_011CbEWjui8ByuqnncuhgYz9",
  "type": "assistant",
  "uuid": "4fddb7d4-1e77-439e-9ff4-7c2c5654f660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vdH7VhWDgQWbZrqbcVfzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2421,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 23209,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2421,
          "output_tokens": 185,
          "cache_read_input_tokens": 23209,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

_source line 15 · 2026-05-20T21:15:22.005Z_

Let me check the output directory and pdflatex availability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fddb7d4-1e77-439e-9ff4-7c2c5654f660",
  "isSidechain": false,
  "requestId": "req_011CbEWjui8ByuqnncuhgYz9",
  "type": "assistant",
  "uuid": "7f5cc2bd-b618-44ce-899e-96d487c81c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vdH7VhWDgQWbZrqbcVfzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2421,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 23209,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2421,
          "output_tokens": 185,
          "cache_read_input_tokens": 23209,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

_source line 16 · 2026-05-20T21:15:23.990Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015wt2q8ySfzVdNip3vdoNBP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/ && which pdflatex",
  "description": "Check output directory and pdflatex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f5cc2bd-b618-44ce-899e-96d487c81c22",
  "isSidechain": false,
  "requestId": "req_011CbEWjui8ByuqnncuhgYz9",
  "type": "assistant",
  "uuid": "c2e389c2-9484-4407-9043-a4ea6b886403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vdH7VhWDgQWbZrqbcVfzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2421,
      "cache_creation_input_tokens": 17933,
      "cache_read_input_tokens": 23209,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2421,
          "output_tokens": 185,
          "cache_read_input_tokens": 23209,
          "cache_creation_input_tokens": 17933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17933
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

_source line 17 · 2026-05-20T21:15:24.213Z_

<details><summary>↩ Tool result · `toolu_015wt2q8ySfzVdNip3vdoNBP`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2e389c2-9484-4407-9043-a4ea6b886403",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "a8db59b4-4e2e-4df5-9912-d6e060d69dee",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c2e389c2-9484-4407-9043-a4ea6b886403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T21:17:27.220Z_

Now I'll write the full LaTeX paper. This is a substantial document covering all 11 experiments from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8db59b4-4e2e-4df5-9912-d6e060d69dee",
  "isSidechain": false,
  "requestId": "req_011CbEWkMxByVzc5wkvGEwM1",
  "type": "assistant",
  "uuid": "494e1db8-3026-4931-8cb5-68db89a060e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Harvz8LatDa8WWhEPEufku",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2646,
      "cache_read_input_tokens": 41142,
      "output_tokens": 12414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12414,
          "cache_read_input_tokens": 41142,
          "cache_creation_input_tokens": 2646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2646
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

_source line 19 · 2026-05-20T21:21:03.630Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GZJN6HvZqFEtAX7MTWKQAJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\title{Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items:\\\\\nDifferential Item Functioning at Scale}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLLM benchmark scores implicitly assume temporal comparability---that a given score reflects the same latent ability regardless of when a model was trained. Benchmark contamination systematically violates this assumption, and recent RL training paradigms (GRPO, PPO) conceal contamination signals from existing per-model detectors by smoothing output distributions. We reframe contamination as a \\emph{psychometric} problem: contaminated items exhibit Differential Item Functioning (DIF), becoming differentially easier for exposed model cohorts beyond what ability gains predict. Because DIF operates on group-level behavioral patterns conditional on ability---not within-model output distributions---it is structurally robust to RL smoothing. Analyzing the METABENCH repository (5,219 models $\\times$ 12,508 MMLU items), we report the largest DIF analysis in LLM evaluation to date. Our contributions are: (1)~the first large-scale IRT fit diagnostic for LLM populations, revealing that architecture heterogeneity is the primary obstacle to psychometric modeling and that restricting to decoder-only subpopulations yields acceptable fit (RMSEA 0.068); (2)~a DIF+ConStat dual-signal ensemble achieving AUROC 0.72 with complementary coverage across training paradigms; (3)~a semi-synthetic validation framework providing controlled ground-truth evaluation of contamination detectors on real response matrices; and (4)~a pilot-scale bifactor IRT equating pipeline for benchmark regeneration ($\\rho=0.91$ on holdout). We characterize detection power as a function of effect size, exploitation rate, and cohort size via a three-parameter power surface ($R^2=0.89$), providing practitioners with actionable operating guidelines. All claims are qualified by empirically identified boundary conditions: DIF requires architecturally homogeneous subpopulations and large contamination effects ($\\delta \\geq 1.4$) for reliable detection; the ensemble has a coverage gap for reasoning-RL models at medium effect sizes; and benchmark regeneration quality systematically degrades beyond 28\\% item replacement.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we assert that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent ability measured under comparable conditions. Benchmark contamination---the inclusion of evaluation items in training data---systematically erodes this assumption. The problem is compounded by the shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1): Wang et al.\\ show 14--20 percentage-point AUROC degradation for all reference-free detectors after GRPO training, reducing most to near-random performance ($\\sim$50\\% AUROC).\n\nExisting approaches address pieces of this problem. LiveBench updates from recent sources but applies no psychometric calibration. ConStat provides FDR-controlled perturbation-based detection but relies on output sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains uses multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination.\n\nWe reframe contamination as a psychometric phenomenon. Contaminated items exhibit \\emph{Differential Item Functioning} (DIF): they become differentially easier for exposed model cohorts \\emph{beyond what general ability gains predict}. DIF operates on group-level Item Characteristic Curves conditional on ability, making it structurally orthogonal to within-model output smoothing. If a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level---the one signal RL cannot conceal without negating the purpose of contamination itself.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{Large-scale IRT fit diagnostics for LLM populations.} We report the first systematic analysis of IRT model fit across 5,219 models, revealing that architecture heterogeneity is the primary obstacle (full-population RMSEA = 0.105) and that decoder-only stratification resolves it (RMSEA = 0.068).\n\\item \\textbf{DIF-based contamination detection with RL robustness.} Under the condition of architecturally homogeneous subpopulations and large contamination effects ($\\delta \\geq 1.4$), DIF achieves TPR = 0.73 with FPR $<$ 0.05, maintaining detection power where existing methods degrade under RL training.\n\\item \\textbf{Dual-signal ensemble with complementary coverage.} DIF + ConStat achieve AUROC 0.72, with DIF covering large effects and RL-trained models while ConStat covers medium effects in non-RL models.\n\\item \\textbf{Semi-synthetic validation framework.} We inject known contamination signals into the real METABENCH response matrix, providing controlled ground-truth evaluation that reveals a simulation-to-real gap (TPR drops 0.15), establishing the framework as a general-purpose tool for contamination detector evaluation.\n\\item \\textbf{Pilot-scale bifactor IRT equating for benchmark regeneration.} Bifactor modeling improves fit (RMSEA 0.062), enables anchor-item selection, and supports item replacement with student-simulation calibration ($\\rho = 0.78$ difficulty correlation), though with systematic quality degradation relative to original items.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\\label{sec:background}\n\n\\paragraph{Item Response Theory (IRT).}\nIRT models the probability of a correct response as a function of latent ability $\\theta$ and item parameters. Under the two-parameter logistic (2PL) model, $P(X_{ij}=1 \\mid \\theta_j) = \\sigma(a_i(\\theta_j - b_i))$, where $a_i$ is discrimination and $b_i$ is difficulty. Model fit is assessed via RMSEA ($<$0.08 acceptable), CFI/TLI ($>$0.90), and SRMR ($<$0.08).\n\n\\paragraph{Differential Item Functioning.}\nAn item exhibits DIF when examinees of equal ability from different groups have unequal probabilities of a correct response. In our setting, groups are defined by model release cohorts (e.g., pre-2024 vs.\\ post-2024). We use the Mantel-Haenszel procedure with ETS classification: $|\\Delta_{\\text{MH}}| < 1.0$ (A, negligible), $1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$ (B, moderate), $|\\Delta_{\\text{MH}}| \\geq 1.5$ (C, large).\n\n\\paragraph{Bifactor IRT.}\nMMLU spans 57 subjects with varying dimensionality. A bifactor model posits a general factor $g$ plus subject-specific factors $s_k$: $P(X_{ij}=1 \\mid \\theta) = \\sigma(a_{ig}\\theta_{gj} + a_{ik}\\theta_{kj} - d_i)$. This captures both cross-domain ability and domain-specific knowledge, enabling principled anchor-item selection for equating.\n\n\\paragraph{ConStat.}\nConStat detects contamination by comparing model performance on original items vs.\\ semantically equivalent reformulations. Contaminated models show anomalous sensitivity to surface perturbations. The method operates per-model and provides FDR-controlled detection.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Data}\nWe use the METABENCH repository containing binary response matrices for 5,219 models on 12,508 MMLU items. Models span encoder-decoder, mixture-of-experts (MoE), and dense decoder-only architectures, with release dates from 2022 to 2025.\n\n\\subsection{Architecture-Stratified IRT Fitting}\n\\label{sec:strat-irt}\nFull-population IRT fitting yields poor fit (RMSEA = 0.105, CFI = 0.82) due to systematic response-pattern differences across architectures. We stratify by architecture, restricting primary analyses to the decoder-only subpopulation ($N=3{,}842$), which achieves acceptable fit (RMSEA = 0.068, CFI = 0.92). We further fit a bifactor model on this subpopulation (RMSEA = 0.062, CFI = 0.94), identifying 38 subjects with strong specific factors and 19 with weak specific factors.\n\n\\subsection{DIF Detection Pipeline}\n\\label{sec:dif-pipeline}\nWe define temporal cohorts (pre-2024 reference, post-2024 focal) and apply Mantel-Haenszel DIF detection within the decoder-only subpopulation. Sensitivity analyses include: (1)~accuracy-quintile cohort definition (highest vs.\\ lowest quintile); (2)~removal of negatively discriminating items; (3)~within-family analysis (e.g., Llama-2 $\\to$ 3.1) to disentangle capability growth from contamination.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:ensemble}\nWe combine DIF (group-level, RL-robust) with ConStat (per-model, perturbation-based) via union fusion. DIF covers large effects across all training paradigms; ConStat covers medium effects in non-RL models. We evaluate both uniform and optimized weighting via 5-fold cross-validation.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi-synth}\nTo address the ground-truth problem, we select 500 empirically clean items and inject contamination signals of known magnitude ($\\delta \\in \\{0.6, 1.0, 1.4\\}$) into the real response matrix. We vary exploitation rate ($p \\in [0.4, 1.0]$), focal group size ($N \\in \\{40, 80, 200\\}$), and contamination prevalence (5\\%--30\\%) to characterize a three-parameter detection power surface.\n\n\\subsection{Bifactor Equating and Item Regeneration}\n\\label{sec:equating}\nAnchor items (620, 5\\% of total) are selected from DIF-free items with high stability across cohorts (ICC = 0.94). Replacement items are generated via LLM with construct constraints and calibrated using student simulation---where surrogate LLMs estimate difficulty by mimicking the target population's response behavior. We compare against prompt-based difficulty targeting and random same-subject baselines.\n\n% ============================================================\n\\section{Experiments and Results}\n\\label{sec:experiments}\n\n\\subsection{IRT Fit Diagnostics Across Populations}\n\\label{sec:exp-irt-fit}\n\nTable~\\ref{tab:irt-fit} reports IRT model fit across population definitions. The full population violates unidimensionality assumptions (RMSEA = 0.105, CFI = 0.82), with encoder-decoder (RMSEA = 0.088) and MoE (RMSEA = 0.095) subpopulations also showing marginal fit. Only the decoder-only subpopulation achieves acceptable fit (RMSEA = 0.068, CFI = 0.92). The bifactor model further improves fit (RMSEA = 0.062, CFI = 0.94), with the general factor explaining 58\\% of variance.\n\n\\begin{table}[ht]\n\\centering\n\\caption{IRT model fit by population and model type. Decoder-only stratification resolves the architecture heterogeneity problem.}\n\\label{tab:irt-fit}\n\\begin{tabular}{lrcccc}\n\\toprule\nPopulation & $N$ & RMSEA & CFI & TLI & SRMR \\\\\n\\midrule\nFull population & 5,219 & 0.105 & 0.82 & 0.79 & 0.091 \\\\\nDecoder-only & 3,842 & 0.068 & 0.92 & 0.90 & 0.054 \\\\\nEncoder-decoder & 312 & 0.088 & 0.87 & 0.85 & 0.072 \\\\\nMoE & 198 & 0.095 & 0.84 & 0.82 & 0.081 \\\\\nPost-2023 decoder-only & 1,856 & 0.072 & 0.91 & 0.89 & 0.058 \\\\\n\\midrule\nBifactor (decoder-only) & 3,842 & 0.062 & 0.94 & 0.92 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification reduces spurious DIF flags by 15.5\\%: ETS-C flags drop from 485 (full population) to 410 (decoder-only), with FPR decreasing from 0.04 to 0.035 (Table~\\ref{tab:spurious-dif}). The 75 eliminated flags represent architecture-induced DIF---items that function differently across architectures for structural reasons unrelated to contamination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Spurious DIF reduction through architecture stratification.}\n\\label{tab:spurious-dif}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Full population & Decoder-only & $\\Delta$ \\\\\n\\midrule\nETS-C flags & 485 & 410 & $-$75 \\\\\nFPR & 0.04 & 0.035 & $-$0.005 \\\\\nSpurious flag \\% & --- & --- & 15.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DIF Detection on Real Data}\n\\label{sec:exp-dif-real}\n\nTable~\\ref{tab:dif-cohort} reports DIF detection results under different cohort definitions within the decoder-only subpopulation. Temporal cohorts (2023 vs.\\ 2024) yield 485 ETS-C flags (3.9\\% of items). Removing negatively discriminating items reduces flags by 12.3\\% (to 427), indicating modest sensitivity to item quality but not a qualitative change.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DIF detection by cohort definition (decoder-only subpopulation, 12,508 items).}\n\\label{tab:dif-cohort}\n\\begin{tabular}{lrrrrr}\n\\toprule\nCohort definition & $N_\\text{focal}$ & $N_\\text{ref}$ & ETS-C & ETS-B & ETS-A (\\%) \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 656 & 1,253 & 485 & 1,120 & 87.2 \\\\\nAccuracy quintile (Q5 vs.\\ Q1) & 1,044 & 1,044 & 390 & 980 & 89.1 \\\\\nTemporal (no neg.\\ disc.) & 656 & 1,253 & 427 & 985 & 88.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Within-family confound analysis.}\nA critical concern is whether temporal DIF flags reflect capability growth rather than contamination. Table~\\ref{tab:within-family} shows within-family DIF analysis for model families with known training lineages. Pooled across families, 42\\% of within-family DIF flags overlap with cross-cohort flags, indicating that a substantial fraction of temporal DIF may reflect genuine capability improvement rather than contamination. This directly motivates our conditional framing of Claim 1.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Within-family DIF confound analysis. Overlap indicates the fraction of within-family DIF flags that coincide with cross-cohort temporal flags.}\n\\label{tab:within-family}\n\\begin{tabular}{lrrr}\n\\toprule\nFamily & $N_\\text{models}$ & DIF-C flags & Overlap (\\%) \\\\\n\\midrule\nLlama 2 $\\to$ 3.1 & 38 & 68 & 44 \\\\\nQwen 1.5 $\\to$ 2.5 & 29 & 52 & 39 \\\\\nMistral / Mixtral & 22 & 41 & 43 \\\\\n\\midrule\nPooled & 89 & 161 & 42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain specificity.}\nDIF flags are non-uniformly distributed across MMLU subjects ($\\chi^2$ test, $p = 0.003$), with STEM subjects showing 1.45$\\times$ the DIF rate of humanities. This is consistent with known contamination hotspots (mathematics, coding) but also confounded with faster capability growth in these domains.\n\n\\paragraph{MMLU-CF validation.}\nCross-validation against MMLU-CF yields $\\kappa = 0.14$ and partial correlation $r = 0.18$---near-random agreement. MMLU-CF's own low reliability limits its utility as ground truth, motivating our semi-synthetic validation framework (\\S\\ref{sec:exp-semi-synth}).\n\n\\subsection{RL Robustness}\n\\label{sec:exp-rl}\n\nTable~\\ref{tab:rl-robust} reports DIF robustness across training paradigms. Adding alignment-RL models (DPO/ORPO, $N=477$) preserves 88\\% of DIF flags with Jaccard similarity 0.76 to the SFT-only baseline. Adding all RL models (including 13 reasoning-RL) maintains 82\\% retention with Jaccard 0.71.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DIF robustness across training paradigms. Retention ratio and Jaccard similarity measure stability relative to SFT-only baseline.}\n\\label{tab:rl-robust}\n\\begin{tabular}{lrrcc}\n\\toprule\nCohort composition & $N_\\text{focal}$ & DIF-C flags & Retention & Jaccard \\\\\n\\midrule\nSFT only (temporal) & 1,842 & 485 & 1.00 & 1.00 \\\\\nSFT + alignment RL & 2,319 & 452 & 0.88 & 0.76 \\\\\nSFT + all RL & 2,332 & 438 & 0.82 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:detector-comp} compares per-model detector performance. DIF maintains group-level AUROC 0.81 (non-RL) and 0.79 (alignment-RL). In contrast, ConStat drops from 0.62 to 0.51, and Min-K\\% drops from 0.68 to 0.49 under reasoning-RL---consistent with Wang et al.'s findings.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-model detector AUROC by training paradigm. DIF is group-level and thus not directly comparable at the per-model grain, but we report it for reference.}\n\\label{tab:detector-comp}\n\\begin{tabular}{lcccc}\n\\toprule\nDetector & Non-RL & Alignment-RL & Reasoning-RL & $\\Delta_\\text{RL}$ \\\\\n\\midrule\nDIF (group-level) & 0.81 & 0.79 & N/A (group) & --- \\\\\nConStat & 0.62 & 0.58 & 0.51 & $-$0.11 \\\\\nMin-K\\% & 0.68 & 0.63 & 0.49 & $-$0.19 \\\\\nPerplexity & 0.61 & 0.55 & 0.47 & $-$0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Alignment-RL robustness.}\nThe alignment-RL result ($N=477$) is statistically robust: DeLong test confirms DIF significantly outperforms ConStat ($p = 0.008$), and TOST equivalence testing ($p = 0.03$) supports DIF retention across paradigms. Bootstrap 95\\% CI for DIF AUROC is [0.74, 0.86].\n\n\\paragraph{Reasoning-RL: preliminary evidence.}\nWith only 13 reasoning-RL models in the cohort, the apparent retention (0.82) reflects dilution within a large group rather than mechanistic robustness. We report this as preliminary evidence requiring validation at larger scale.\n\n\\paragraph{Partial exploitation.}\nTable~\\ref{tab:partial} characterizes detection power as a function of exploitation rate $p$. At $p = 1.0$, DIF achieves TPR = 0.73. Power degrades to 0.44 at $p = 0.6$ and 0.28 at $p = 0.4$. The ensemble handoff point occurs near $p = 0.55$, where DIF and ConStat TPR converge. Below $p = 0.4$, contamination effects on rankings become negligible.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Detection power by exploitation rate. Ensemble TPR combines DIF and ConStat via union.}\n\\label{tab:partial}\n\\begin{tabular}{ccccc}\n\\toprule\n$p$ & Effective $\\delta$ & DIF TPR & ConStat TPR & Ensemble TPR \\\\\n\\midrule\n1.0 & 1.60 & 0.73 & 0.54 & 0.79 \\\\\n0.8 & 1.28 & 0.61 & 0.48 & 0.68 \\\\\n0.6 & 0.96 & 0.44 & 0.42 & 0.55 \\\\\n0.4 & 0.64 & 0.28 & 0.35 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{ConStat Independent Evaluation}\n\\label{sec:exp-constat}\n\nWe independently evaluate ConStat on 220 reformulated items. Table~\\ref{tab:constat-type} reports performance stratified by model type. ConStat achieves AUROC 0.67 on non-RL models but degrades to 0.52 (near-random) on reasoning-RL models, confirming its known vulnerability to RL-induced smoothing.\n\n\\begin{table}[ht]\n\\centering\n\\caption{ConStat detection by model type (FDR = 0.10, 220 reformulated items).}\n\\label{tab:constat-type}\n\\begin{tabular}{lrccc}\n\\toprule\nModel type & $N$ & AUROC & TPR & FPR \\\\\n\\midrule\nAll models & 5,219 & 0.63 & 0.38 & 0.08 \\\\\nNon-RL & 4,742 & 0.67 & 0.44 & 0.07 \\\\\nAlignment-RL & 477 & 0.61 & 0.36 & 0.09 \\\\\nReasoning-RL & 13 & 0.52 & 0.22 & 0.11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverlap between ConStat and DIF flags is 38\\%, confirming signal orthogonality: ConStat captures per-model perturbation sensitivity while DIF captures group-level behavioral anomalies. This low overlap provides the empirical basis for ensemble complementarity.\n\n\\subsection{DVD Generation Variance Evaluation}\n\\label{sec:exp-dvd}\n\nDVD detection on 12 open-weight models across 500 items yields overall AUROC = 0.56 (Table~\\ref{tab:dvd}). Performance is marginally better for variant contamination (AUROC = 0.61) than verbatim (0.53), but FPR = 0.14 limits practical utility. The bimodal detection rate (18\\%) is too low to distinguish memorization from non-memorization via generation variance in the MCQ setting.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DVD detection performance. The MCQ format inherently limits generation variance signal strength.}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\nContamination type & AUROC & TPR @ FPR=0.10 & FPR @ TPR=0.50 \\\\\n\\midrule\nOverall & 0.56 & 0.31 & 0.35 \\\\\nVerbatim & 0.53 & 0.24 & 0.41 \\\\\nVariant & 0.61 & 0.42 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD's weak performance in the MCQ setting is attributable to the constrained output space: 4-way softmax distributions yield minimal variance differences between memorized and non-memorized items. Overlap with DIF (22\\%) and ConStat (28\\%) is low, indicating DVD captures a different but weaker signal. We exclude DVD from the primary ensemble and report it as an exploratory analysis.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:exp-ensemble}\n\nTable~\\ref{tab:ensemble} reports ensemble performance. The DIF + ConStat union achieves the best AUROC (0.72) and highest TPR at $\\delta \\geq 0.8$ (0.58) while maintaining FPR = 0.09. Adding DVD marginally degrades performance (AUROC 0.70, FPR 0.11) due to DVD's high false-positive rate.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Ensemble detection performance across configurations.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\nConfiguration & TPR ($\\delta \\geq 0.8$) & TPR ($\\delta \\geq 1.4$) & FPR & AUROC \\\\\n\\midrule\nDIF only & 0.45 & 0.73 & 0.04 & 0.76 \\\\\nConStat only & 0.35 & 0.48 & 0.08 & 0.63 \\\\\nDVD only & 0.22 & 0.31 & 0.14 & 0.56 \\\\\nDIF + ConStat (union) & 0.58 & 0.78 & 0.09 & 0.72 \\\\\nDIF + ConStat + DVD & 0.55 & 0.76 & 0.11 & 0.70 \\\\\nDIF + ConStat (intersection) & 0.42 & 0.52 & 0.03 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFusion weight analysis (Table~\\ref{tab:fusion}) shows optimized weighting (DIF: 0.62, ConStat: 0.38) improves AUROC by 0.03 over uniform weights, but the improvement is within CV noise ($\\sigma = 0.04$--$0.05$). We report uniform weights as the primary result.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Fusion weight analysis (5-fold CV).}\n\\label{tab:fusion}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Mean AUROC & Std AUROC & DIF weight & ConStat weight \\\\\n\\midrule\nUniform & 0.69 & 0.05 & 0.50 & 0.50 \\\\\nOptimized & 0.72 & 0.04 & 0.62 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCoverage analysis reveals a structural gap: on non-RL models, union coverage reaches 71\\%, but on the full population (including RL models), it drops to 62\\%. The gap originates from ConStat's failure on reasoning-RL models combined with DIF's limited power for medium effect sizes---a region neither signal adequately covers for RL-trained models.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:exp-gsm8k}\n\nWe replicate DIF analysis on GSM8K (62 models, 1,319 items) using GSM1K as independent ground truth. IRT fit is acceptable (RMSEA = 0.075), better than MMLU due to GSM8K's more unidimensional construct (mathematical reasoning). DIF detects 78 ETS-C flags. The correlation between DIF flag density and GSM8K$-$GSM1K accuracy gap is $r = 0.36$ ($p = 0.004$), with 1.8$\\times$ enrichment of DIF flags among high-gap models. The moderate correlation provides corroborating---but not conclusive---evidence that DIF captures contamination-related signals.\n\n\\begin{table}[ht]\n\\centering\n\\caption{GSM8K DIF analysis with GSM1K ground truth.}\n\\label{tab:gsm8k}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nModels & 62 \\\\\nItems & 1,319 \\\\\nETS-C flags & 78 \\\\\nIRT RMSEA & 0.075 \\\\\nDIF--gap correlation ($r$) & 0.36 \\\\\nDIF--gap correlation ($p$) & 0.004 \\\\\nFlag enrichment ratio & 1.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:exp-semi-synth}\n\nTable~\\ref{tab:semi-synth-tpr} reports semi-synthetic validation results. TPR = 0.58 at $\\delta \\geq 1.4$ is substantially lower than the 0.73 observed in pure simulation, revealing a simulation-to-real gap of 0.15 in TPR and 0.12 in AUC (Table~\\ref{tab:sim-gap}). This gap arises from noise sources absent in simulation: non-normal ability distributions, negatively discriminating items (15\\% of MMLU), and pre-existing background contamination in the ``clean'' baseline.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Semi-synthetic validation: TPR by effect size (150 injected items, 500 clean items).}\n\\label{tab:semi-synth-tpr}\n\\begin{tabular}{cccc}\n\\toprule\n$\\delta$ threshold & TPR & FPR & $N_\\text{injected}$ \\\\\n\\midrule\n$\\geq 1.4$ & 0.58 & 0.07 & 45 \\\\\n$\\geq 1.0$ & 0.41 & 0.07 & 85 \\\\\n$\\geq 0.6$ & 0.25 & 0.07 & 150 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Simulation vs.\\ semi-synthetic gap.}\n\\label{tab:sim-gap}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Simulation & Semi-synthetic & Gap \\\\\n\\midrule\nTPR ($\\delta \\geq 1.4$) & 0.73 & 0.58 & $-$0.15 \\\\\nFPR & 0.04 & 0.07 & +0.03 \\\\\nAUC & 0.94 & 0.82 & $-$0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-parameter power surface (Table~\\ref{tab:power-surface}) characterizes detection power as a function of exploitation rate, focal group size, and contamination prevalence ($R^2 = 0.89$). Exploitation rate is the strongest determinant (TPR drops from 0.65 at $p=1.0$ to 0.22 at $p=0.4$), followed by focal group size (TPR 0.44 at $N=40$ vs.\\ 0.68 at $N=200$). Prevalence has the weakest effect (0.52 at 5\\% vs.\\ 0.63 at 30\\%).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Semi-synthetic power surface. Each parameter is varied while others are held at mid-level.}\n\\label{tab:power-surface}\n\\begin{tabular}{lcccccc}\n\\toprule\nParameter & Low & Mid & High & TPR (low) & TPR (mid) & TPR (high) \\\\\n\\midrule\nExploitation rate & 0.4 & 0.7 & 1.0 & 0.22 & 0.45 & 0.65 \\\\\nFocal $N$ & 40 & 80 & 200 & 0.44 & 0.58 & 0.68 \\\\\nPrevalence & 0.05 & 0.15 & 0.30 & 0.52 & 0.58 & 0.63 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Bifactor Equating and Item Regeneration}\n\\label{sec:exp-equating}\n\n\\paragraph{Bifactor model.}\nThe bifactor model converges on the decoder-only subpopulation with RMSEA = 0.062 (Table~\\ref{tab:irt-fit}). The general factor explains 58\\% of variance; 38 of 57 subjects have strong specific factors (standardized loading $> 0.3$), while 19 have weak specific factors (loading $< 0.2$), including abstract algebra, formal logic, jurisprudence, and moral scenarios. Weak-factor subjects pose a structural bottleneck for equating: their items load primarily on the general factor, making anchor-item selection and replacement calibration less stable.\n\n\\paragraph{Anchor items.}\n620 items (5\\%) are selected as anchors based on DIF-free status and cross-cohort stability (ICC = 0.94). Anchor coverage is adequate for strong-factor subjects but sparse for weak-factor subjects.\n\n\\paragraph{Item generation and calibration.}\nTable~\\ref{tab:item-gen} compares calibration methods. Student simulation achieves difficulty correlation $\\rho = 0.78$ and MSE = 0.34, substantially outperforming prompt-based targeting ($\\rho = 0.28$, MSE = 1.85) and random same-subject selection ($\\rho = 0.11$, MSE = 2.40). The 25\\% generation failure rate (items not passing construct filters) indicates that automated replacement still requires quality control.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Item calibration: difficulty correlation and MSE against empirical parameters.}\n\\label{tab:item-gen}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Difficulty MSE & $N_\\text{items}$ \\\\\n\\midrule\nStudent simulation & 0.78 & 0.34 & 112 \\\\\nPrompt-based targeting & 0.28 & 1.85 & 112 \\\\\nRandom same-subject & 0.11 & 2.40 & 112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Holdout validation.}\nOn a 50-model holdout panel, replaced items achieve equated $\\rho = 0.91$ (vs.\\ the full original benchmark), with systematic quality degradation: mean factor loading drops from 0.50 to 0.41 and discrimination from 1.18 to 0.95 (Table~\\ref{tab:holdout}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Holdout validation of replacement items (50-model panel).}\n\\label{tab:holdout}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Original items & Replaced items \\\\\n\\midrule\nSpearman $\\rho$ vs.\\ full & --- & 0.91 \\\\\nMean factor loading & 0.50 & 0.41 \\\\\nMean difficulty & 0.52 & 0.49 \\\\\nMean discrimination & 1.18 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:exp-degradation}\n\nTable~\\ref{tab:degradation} characterizes benchmark validity as a function of replacement rate. At 20\\% replacement, Spearman $\\rho = 0.93$, Cronbach's $\\alpha = 0.91$, and construct coverage = 0.89---marginally acceptable. Beyond the critical threshold of 28\\%, validity accelerates its decline. At 50\\%, $\\rho = 0.85$---ranking shifts become too large for meaningful comparison.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Graceful degradation: benchmark validity vs.\\ item replacement rate.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\nReplacement (\\%) & Spearman $\\rho$ & Cronbach's $\\alpha$ & Construct coverage \\\\\n\\midrule\n0 & 1.00 & 0.94 & 1.00 \\\\\n5 & 0.98 & 0.93 & 0.97 \\\\\n10 & 0.96 & 0.93 & 0.94 \\\\\n20 & 0.93 & 0.91 & 0.89 \\\\\n50 & 0.85 & 0.86 & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical validity loss rate is approximately 0.003 per percentage point of replacement, with acceleration beyond 28\\%. The degradation is driven by weak-factor subjects (\\S\\ref{sec:exp-equating}), where replacement items cannot maintain the original subject-specific factor structure.\n\n% ============================================================\n\\section{Supplementary Analyses}\n\\label{sec:supplementary}\n\n\\subsection{Item-Focused Trees}\n\\label{sec:exp-ift}\n\nAs a methodological alternative to categorical DIF, Item-Focused Trees (IFT) treat release date as a continuous covariate. IFT flags 520 items with AUC = 0.78, slightly higher than ETS-C (AUC = 0.76), but with higher FPR (0.07 vs.\\ 0.04). The automatically learned split point (September 2023) aligns with the estimated onset of accelerated benchmark leakage. Overlap with ETS-C is 62\\%, suggesting IFT captures gradual contamination patterns that binary cohort splits miss.\n\n\\begin{table}[ht]\n\\centering\n\\caption{IFT vs.\\ ETS-C DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lrcccc}\n\\toprule\nMethod & Flags & TPR ($\\delta \\geq 1.4$) & FPR & AUC & Overlap \\\\\n\\midrule\nETS-C & 485 & 0.73 & 0.04 & 0.76 & --- \\\\\nIFT & 520 & 0.69 & 0.07 & 0.78 & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:exp-bayes}\n\nCumulative Bayesian DIF uses the posterior from each administration as the prior for the next. Table~\\ref{tab:bayes} shows power accumulation: from 0.38 (single administration, $\\delta = 1.0$) to 0.72 after four administrations, with diminishing marginal returns. FPR remains controlled at 0.06. This supports DIF as a longitudinal monitoring tool rather than a one-shot detector.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cumulative Bayesian DIF power (simulated, $\\delta = 1.0$).}\n\\label{tab:bayes}\n\\begin{tabular}{cccc}\n\\toprule\nAdministrations & Power ($\\delta = 1.0$) & Power ($\\delta = 1.4$) & FPR \\\\\n\\midrule\n1 & 0.38 & 0.73 & 0.04 \\\\\n2 & 0.52 & 0.82 & 0.05 \\\\\n3 & 0.65 & 0.88 & 0.05 \\\\\n4 & 0.72 & 0.91 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Methodological contributions.}\nOur primary contributions are methodological rather than systemic. First, we provide the first large-scale IRT fit diagnostic for LLM populations, establishing that architecture heterogeneity---not item quality or sample size---is the primary obstacle to psychometric modeling of LLM evaluation data. The practical prescription is straightforward: restrict IRT-based analyses to architecturally homogeneous subpopulations.\n\nSecond, the semi-synthetic validation framework provides a general-purpose tool for evaluating any item-level contamination detector under controlled conditions on real response data. The revealed simulation-to-real gap (TPR $-$0.15, AUC $-$0.12) cautions against relying solely on simulation for detector evaluation.\n\nThird, the student-simulation calibration method ($\\rho = 0.78$) significantly outperforms prompt-based targeting ($\\rho = 0.28$) for replacement item difficulty estimation, establishing a viable calibration strategy for benchmark regeneration.\n\n\\paragraph{Boundary conditions.}\nOur claims carry explicit boundary conditions:\n\\begin{itemize}\n\\item DIF detection requires architecturally homogeneous subpopulations (decoder-only) and is practical only for large effects ($\\delta \\geq 1.4$). At medium effects ($\\delta \\in [0.6, 1.4]$), detection power is insufficient without ensemble support.\n\\item The dual-signal ensemble has a coverage gap: reasoning-RL models at medium effect sizes are inadequately covered by either DIF (insufficient power) or ConStat (RL-degraded).\n\\item Within-family analysis reveals 42\\% overlap between temporal DIF and within-family DIF, meaning nearly half of flagged items may reflect capability growth rather than contamination.\n\\item Benchmark regeneration quality systematically degrades: replacement items have lower factor loadings (0.41 vs.\\ 0.50) and discrimination (0.95 vs.\\ 1.18), with a critical replacement threshold at 28\\%.\n\\end{itemize}\n\n\\paragraph{DVD negative result.}\nDVD generation variance detection achieves AUROC = 0.56 in the MCQ setting---marginally above random. The 4-way MCQ output space provides insufficient variance signal, and the bimodal detection rate (18\\%) is too low for practical use. We report this as a methodologically informative negative result: generation variance approaches may be better suited to open-ended generation tasks than constrained MCQ formats.\n\n\\paragraph{Reasoning-RL coverage gap.}\nThe most significant limitation is the reasoning-RL validation gap. With only 13 reasoning-RL models available, our DIF retention results (0.82) reflect statistical dilution rather than mechanistic verification. As reasoning-RL models become more prevalent, the decoder-only subpopulation will increasingly contain RL-trained models, potentially changing DIF dynamics. Longitudinal monitoring will be needed to validate DIF stability in this evolving landscape.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present a psychometric approach to benchmark contamination detection and regeneration, demonstrating that DIF analysis provides a structurally RL-robust contamination signal when applied to architecturally homogeneous LLM subpopulations. Our contributions center on detection methodology and psychometric diagnostics rather than a complete end-to-end system: (1)~the first large-scale IRT fit analysis revealing architecture heterogeneity as the primary obstacle; (2)~a dual-signal DIF+ConStat ensemble with complementary coverage (AUROC 0.72); (3)~a semi-synthetic validation framework that quantifies detector performance under controlled conditions; and (4)~pilot-scale bifactor equating for item regeneration ($\\rho = 0.91$). All claims are qualified by empirically established boundary conditions---architecture homogeneity, large effect sizes, and limited replacement budgets---and we transparently report both the reasoning-RL coverage gap and the DVD negative result. The three-parameter power surface ($R^2 = 0.89$) provides practitioners with actionable guidelines for deploying DIF-based monitoring in their evaluation pipelines.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem{wang2026rl}\nWang, Z., et al. (2026).\n\\newblock Contamination signals vanish after reinforcement learning: A systematic evaluation.\n\\newblock In \\emph{Proceedings of ICLR 2026}.\n\n\\bibitem{livebench2024}\nWhite, C., et al. (2024).\n\\newblock LiveBench: A challenging, contamination-free LLM benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem{constat2024}\nOren, Y., et al. (2024).\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proceedings of NeurIPS 2024}.\n\n\\bibitem{growingpains2026}\nZhang, L., et al. (2026).\n\\newblock Growing pains: Multidimensional IRT for extensible LLM evaluation.\n\\newblock \\emph{arXiv preprint arXiv:2601.xxxxx}.\n\n\\bibitem{metabench2025}\nPerlitz, Y., et al. (2025).\n\\newblock METABENCH: A large-scale repository of LLM evaluation results.\n\\newblock In \\emph{Proceedings of ICLR 2025}.\n\n\\bibitem{holland1988dif}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock In \\emph{Test Validity}, pages 129--145.\n\n\\bibitem{studentsim2025}\nLi, R., et al. (2025).\n\\newblock Student simulation for item difficulty estimation.\n\\newblock \\emph{arXiv preprint arXiv:2601.09953}.\n\n\\bibitem{gsm1k2024}\nZhang, H., et al. (2024).\n\\newblock Careful examination of large language model performance on {GSM8K}.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem{mmlucf2024}\nWiegreffe, S., et al. (2024).\n\\newblock {MMLU-CF}: A contamination-free multi-task benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2412.15194}.\n\n\\bibitem{dvd2024}\nDunn, A., et al. (2024).\n\\newblock Detecting pretraining data from large language models via generation variance.\n\\newblock \\emph{arXiv preprint arXiv:2407.14985}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "494e1db8-3026-4931-8cb5-68db89a060e3",
  "isSidechain": false,
  "requestId": "req_011CbEWkMxByVzc5wkvGEwM1",
  "type": "assistant",
  "uuid": "7846f432-073d-4529-bebd-fc1f2889ef55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Harvz8LatDa8WWhEPEufku",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2646,
      "cache_read_input_tokens": 41142,
      "output_tokens": 12414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2646,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12414,
          "cache_read_input_tokens": 41142,
          "cache_creation_input_tokens": 2646,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2646
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

_source line 20 · 2026-05-20T21:21:03.650Z_

<details><summary>↩ Tool result · `toolu_01GZJN6HvZqFEtAX7MTWKQAJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7846f432-073d-4529-bebd-fc1f2889ef55",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "e8b65109-d36a-4c90-b8d8-04ffa42225b2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\title{Psychometric Detection and Regeneration of Contaminated LLM Benchmark Items:\\\\\nDifferential Item Functioning at Scale}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nLLM benchmark scores implicitly assume temporal comparability---that a given score reflects the same latent ability regardless of when a model was trained. Benchmark contamination systematically violates this assumption, and recent RL training paradigms (GRPO, PPO) conceal contamination signals from existing per-model detectors by smoothing output distributions. We reframe contamination as a \\emph{psychometric} problem: contaminated items exhibit Differential Item Functioning (DIF), becoming differentially easier for exposed model cohorts beyond what ability gains predict. Because DIF operates on group-level behavioral patterns conditional on ability---not within-model output distributions---it is structurally robust to RL smoothing. Analyzing the METABENCH repository (5,219 models $\\times$ 12,508 MMLU items), we report the largest DIF analysis in LLM evaluation to date. Our contributions are: (1)~the first large-scale IRT fit diagnostic for LLM populations, revealing that architecture heterogeneity is the primary obstacle to psychometric modeling and that restricting to decoder-only subpopulations yields acceptable fit (RMSEA 0.068); (2)~a DIF+ConStat dual-signal ensemble achieving AUROC 0.72 with complementary coverage across training paradigms; (3)~a semi-synthetic validation framework providing controlled ground-truth evaluation of contamination detectors on real response matrices; and (4)~a pilot-scale bifactor IRT equating pipeline for benchmark regeneration ($\\rho=0.91$ on holdout). We characterize detection power as a function of effect size, exploitation rate, and cohort size via a three-parameter power surface ($R^2=0.89$), providing practitioners with actionable operating guidelines. All claims are qualified by empirically identified boundary conditions: DIF requires architecturally homogeneous subpopulations and large contamination effects ($\\delta \\geq 1.4$) for reliable detection; the ensemble has a coverage gap for reasoning-RL models at medium effect sizes; and benchmark regeneration quality systematically degrades beyond 28\\% item replacement.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nWhen we assert that ``Model B outperforms Model A on MMLU,'' we implicitly assume both scores reflect the same latent ability measured under comparable conditions. Benchmark contamination---the inclusion of evaluation items in training data---systematically erodes this assumption. The problem is compounded by the shift toward RL-trained reasoning models (o1, o3, DeepSeek-R1): Wang et al.\\ show 14--20 percentage-point AUROC degradation for all reference-free detectors after GRPO training, reducing most to near-random performance ($\\sim$50\\% AUROC).\n\nExisting approaches address pieces of this problem. LiveBench updates from recent sources but applies no psychometric calibration. ConStat provides FDR-controlled perturbation-based detection but relies on output sensitivity that RL can mask. DVD detects variant contamination via generation variance but is untested against RL. Growing Pains uses multidimensional IRT for extensible evaluation but addresses score comparability rather than contamination.\n\nWe reframe contamination as a psychometric phenomenon. Contaminated items exhibit \\emph{Differential Item Functioning} (DIF): they become differentially easier for exposed model cohorts \\emph{beyond what general ability gains predict}. DIF operates on group-level Item Characteristic Curves conditional on ability, making it structurally orthogonal to within-model output smoothing. If a model memorized an item, it must answer it correctly, creating a detectable behavioral anomaly at the population level---the one signal RL cannot conceal without negating the purpose of contamination itself.\n\n\\paragraph{Contributions.}\n\\begin{enumerate}\n\\item \\textbf{Large-scale IRT fit diagnostics for LLM populations.} We report the first systematic analysis of IRT model fit across 5,219 models, revealing that architecture heterogeneity is the primary obstacle (full-population RMSEA = 0.105) and that decoder-only stratification resolves it (RMSEA = 0.068).\n\\item \\textbf{DIF-based contamination detection with RL robustness.} Under the condition of architecturally homogeneous subpopulations and large contamination effects ($\\delta \\geq 1.4$), DIF achieves TPR = 0.73 with FPR $<$ 0.05, maintaining detection power where existing methods degrade under RL training.\n\\item \\textbf{Dual-signal ensemble with complementary coverage.} DIF + ConStat achieve AUROC 0.72, with DIF covering large effects and RL-trained models while ConStat covers medium effects in non-RL models.\n\\item \\textbf{Semi-synthetic validation framework.} We inject known contamination signals into the real METABENCH response matrix, providing controlled ground-truth evaluation that reveals a simulation-to-real gap (TPR drops 0.15), establishing the framework as a general-purpose tool for contamination detector evaluation.\n\\item \\textbf{Pilot-scale bifactor IRT equating for benchmark regeneration.} Bifactor modeling improves fit (RMSEA 0.062), enables anchor-item selection, and supports item replacement with student-simulation calibration ($\\rho = 0.78$ difficulty correlation), though with systematic quality degradation relative to original items.\n\\end{enumerate}\n\n% ============================================================\n\\section{Background}\n\\label{sec:background}\n\n\\paragraph{Item Response Theory (IRT).}\nIRT models the probability of a correct response as a function of latent ability $\\theta$ and item parameters. Under the two-parameter logistic (2PL) model, $P(X_{ij}=1 \\mid \\theta_j) = \\sigma(a_i(\\theta_j - b_i))$, where $a_i$ is discrimination and $b_i$ is difficulty. Model fit is assessed via RMSEA ($<$0.08 acceptable), CFI/TLI ($>$0.90), and SRMR ($<$0.08).\n\n\\paragraph{Differential Item Functioning.}\nAn item exhibits DIF when examinees of equal ability from different groups have unequal probabilities of a correct response. In our setting, groups are defined by model release cohorts (e.g., pre-2024 vs.\\ post-2024). We use the Mantel-Haenszel procedure with ETS classification: $|\\Delta_{\\text{MH}}| < 1.0$ (A, negligible), $1.0 \\leq |\\Delta_{\\text{MH}}| < 1.5$ (B, moderate), $|\\Delta_{\\text{MH}}| \\geq 1.5$ (C, large).\n\n\\paragraph{Bifactor IRT.}\nMMLU spans 57 subjects with varying dimensionality. A bifactor model posits a general factor $g$ plus subject-specific factors $s_k$: $P(X_{ij}=1 \\mid \\theta) = \\sigma(a_{ig}\\theta_{gj} + a_{ik}\\theta_{kj} - d_i)$. This captures both cross-domain ability and domain-specific knowledge, enabling principled anchor-item selection for equating.\n\n\\paragraph{ConStat.}\nConStat detects contamination by comparing model performance on original items vs.\\ semantically equivalent reformulations. Contaminated models show anomalous sensitivity to surface perturbations. The method operates per-model and provides FDR-controlled detection.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Data}\nWe use the METABENCH repository containing binary response matrices for 5,219 models on 12,508 MMLU items. Models span encoder-decoder, mixture-of-experts (MoE), and dense decoder-only architectures, with release dates from 2022 to 2025.\n\n\\subsection{Architecture-Stratified IRT Fitting}\n\\label{sec:strat-irt}\nFull-population IRT fitting yields poor fit (RMSEA = 0.105, CFI = 0.82) due to systematic response-pattern differences across architectures. We stratify by architecture, restricting primary analyses to the decoder-only subpopulation ($N=3{,}842$), which achieves acceptable fit (RMSEA = 0.068, CFI = 0.92). We further fit a bifactor model on this subpopulation (RMSEA = 0.062, CFI = 0.94), identifying 38 subjects with strong specific factors and 19 with weak specific factors.\n\n\\subsection{DIF Detection Pipeline}\n\\label{sec:dif-pipeline}\nWe define temporal cohorts (pre-2024 reference, post-2024 focal) and apply Mantel-Haenszel DIF detection within the decoder-only subpopulation. Sensitivity analyses include: (1)~accuracy-quintile cohort definition (highest vs.\\ lowest quintile); (2)~removal of negatively discriminating items; (3)~within-family analysis (e.g., Llama-2 $\\to$ 3.1) to disentangle capability growth from contamination.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:ensemble}\nWe combine DIF (group-level, RL-robust) with ConStat (per-model, perturbation-based) via union fusion. DIF covers large effects across all training paradigms; ConStat covers medium effects in non-RL models. We evaluate both uniform and optimized weighting via 5-fold cross-validation.\n\n\\subsection{Semi-Synthetic Validation}\n\\label{sec:semi-synth}\nTo address the ground-truth problem, we select 500 empirically clean items and inject contamination signals of known magnitude ($\\delta \\in \\{0.6, 1.0, 1.4\\}$) into the real response matrix. We vary exploitation rate ($p \\in [0.4, 1.0]$), focal group size ($N \\in \\{40, 80, 200\\}$), and contamination prevalence (5\\%--30\\%) to characterize a three-parameter detection power surface.\n\n\\subsection{Bifactor Equating and Item Regeneration}\n\\label{sec:equating}\nAnchor items (620, 5\\% of total) are selected from DIF-free items with high stability across cohorts (ICC = 0.94). Replacement items are generated via LLM with construct constraints and calibrated using student simulation---where surrogate LLMs estimate difficulty by mimicking the target population's response behavior. We compare against prompt-based difficulty targeting and random same-subject baselines.\n\n% ============================================================\n\\section{Experiments and Results}\n\\label{sec:experiments}\n\n\\subsection{IRT Fit Diagnostics Across Populations}\n\\label{sec:exp-irt-fit}\n\nTable~\\ref{tab:irt-fit} reports IRT model fit across population definitions. The full population violates unidimensionality assumptions (RMSEA = 0.105, CFI = 0.82), with encoder-decoder (RMSEA = 0.088) and MoE (RMSEA = 0.095) subpopulations also showing marginal fit. Only the decoder-only subpopulation achieves acceptable fit (RMSEA = 0.068, CFI = 0.92). The bifactor model further improves fit (RMSEA = 0.062, CFI = 0.94), with the general factor explaining 58\\% of variance.\n\n\\begin{table}[ht]\n\\centering\n\\caption{IRT model fit by population and model type. Decoder-only stratification resolves the architecture heterogeneity problem.}\n\\label{tab:irt-fit}\n\\begin{tabular}{lrcccc}\n\\toprule\nPopulation & $N$ & RMSEA & CFI & TLI & SRMR \\\\\n\\midrule\nFull population & 5,219 & 0.105 & 0.82 & 0.79 & 0.091 \\\\\nDecoder-only & 3,842 & 0.068 & 0.92 & 0.90 & 0.054 \\\\\nEncoder-decoder & 312 & 0.088 & 0.87 & 0.85 & 0.072 \\\\\nMoE & 198 & 0.095 & 0.84 & 0.82 & 0.081 \\\\\nPost-2023 decoder-only & 1,856 & 0.072 & 0.91 & 0.89 & 0.058 \\\\\n\\midrule\nBifactor (decoder-only) & 3,842 & 0.062 & 0.94 & 0.92 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture stratification reduces spurious DIF flags by 15.5\\%: ETS-C flags drop from 485 (full population) to 410 (decoder-only), with FPR decreasing from 0.04 to 0.035 (Table~\\ref{tab:spurious-dif}). The 75 eliminated flags represent architecture-induced DIF---items that function differently across architectures for structural reasons unrelated to contamination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Spurious DIF reduction through architecture stratification.}\n\\label{tab:spurious-dif}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Full population & Decoder-only & $\\Delta$ \\\\\n\\midrule\nETS-C flags & 485 & 410 & $-$75 \\\\\nFPR & 0.04 & 0.035 & $-$0.005 \\\\\nSpurious flag \\% & --- & --- & 15.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DIF Detection on Real Data}\n\\label{sec:exp-dif-real}\n\nTable~\\ref{tab:dif-cohort} reports DIF detection results under different cohort definitions within the decoder-only subpopulation. Temporal cohorts (2023 vs.\\ 2024) yield 485 ETS-C flags (3.9\\% of items). Removing negatively discriminating items reduces flags by 12.3\\% (to 427), indicating modest sensitivity to item quality but not a qualitative change.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DIF detection by cohort definition (decoder-only subpopulation, 12,508 items).}\n\\label{tab:dif-cohort}\n\\begin{tabular}{lrrrrr}\n\\toprule\nCohort definition & $N_\\text{focal}$ & $N_\\text{ref}$ & ETS-C & ETS-B & ETS-A (\\%) \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024) & 656 & 1,253 & 485 & 1,120 & 87.2 \\\\\nAccuracy quintile (Q5 vs.\\ Q1) & 1,044 & 1,044 & 390 & 980 & 89.1 \\\\\nTemporal (no neg.\\ disc.) & 656 & 1,253 & 427 & 985 & 88.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Within-family confound analysis.}\nA critical concern is whether temporal DIF flags reflect capability growth rather than contamination. Table~\\ref{tab:within-family} shows within-family DIF analysis for model families with known training lineages. Pooled across families, 42\\% of within-family DIF flags overlap with cross-cohort flags, indicating that a substantial fraction of temporal DIF may reflect genuine capability improvement rather than contamination. This directly motivates our conditional framing of Claim 1.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Within-family DIF confound analysis. Overlap indicates the fraction of within-family DIF flags that coincide with cross-cohort temporal flags.}\n\\label{tab:within-family}\n\\begin{tabular}{lrrr}\n\\toprule\nFamily & $N_\\text{models}$ & DIF-C flags & Overlap (\\%) \\\\\n\\midrule\nLlama 2 $\\to$ 3.1 & 38 & 68 & 44 \\\\\nQwen 1.5 $\\to$ 2.5 & 29 & 52 & 39 \\\\\nMistral / Mixtral & 22 & 41 & 43 \\\\\n\\midrule\nPooled & 89 & 161 & 42 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Domain specificity.}\nDIF flags are non-uniformly distributed across MMLU subjects ($\\chi^2$ test, $p = 0.003$), with STEM subjects showing 1.45$\\times$ the DIF rate of humanities. This is consistent with known contamination hotspots (mathematics, coding) but also confounded with faster capability growth in these domains.\n\n\\paragraph{MMLU-CF validation.}\nCross-validation against MMLU-CF yields $\\kappa = 0.14$ and partial correlation $r = 0.18$---near-random agreement. MMLU-CF's own low reliability limits its utility as ground truth, motivating our semi-synthetic validation framework (\\S\\ref{sec:exp-semi-synth}).\n\n\\subsection{RL Robustness}\n\\label{sec:exp-rl}\n\nTable~\\ref{tab:rl-robust} reports DIF robustness across training paradigms. Adding alignment-RL models (DPO/ORPO, $N=477$) preserves 88\\% of DIF flags with Jaccard similarity 0.76 to the SFT-only baseline. Adding all RL models (including 13 reasoning-RL) maintains 82\\% retention with Jaccard 0.71.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DIF robustness across training paradigms. Retention ratio and Jaccard similarity measure stability relative to SFT-only baseline.}\n\\label{tab:rl-robust}\n\\begin{tabular}{lrrcc}\n\\toprule\nCohort composition & $N_\\text{focal}$ & DIF-C flags & Retention & Jaccard \\\\\n\\midrule\nSFT only (temporal) & 1,842 & 485 & 1.00 & 1.00 \\\\\nSFT + alignment RL & 2,319 & 452 & 0.88 & 0.76 \\\\\nSFT + all RL & 2,332 & 438 & 0.82 & 0.71 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:detector-comp} compares per-model detector performance. DIF maintains group-level AUROC 0.81 (non-RL) and 0.79 (alignment-RL). In contrast, ConStat drops from 0.62 to 0.51, and Min-K\\% drops from 0.68 to 0.49 under reasoning-RL---consistent with Wang et al.'s findings.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-model detector AUROC by training paradigm. DIF is group-level and thus not directly comparable at the per-model grain, but we report it for reference.}\n\\label{tab:detector-comp}\n\\begin{tabular}{lcccc}\n\\toprule\nDetector & Non-RL & Alignment-RL & Reasoning-RL & $\\Delta_\\text{RL}$ \\\\\n\\midrule\nDIF (group-level) & 0.81 & 0.79 & N/A (group) & --- \\\\\nConStat & 0.62 & 0.58 & 0.51 & $-$0.11 \\\\\nMin-K\\% & 0.68 & 0.63 & 0.49 & $-$0.19 \\\\\nPerplexity & 0.61 & 0.55 & 0.47 & $-$0.14 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Alignment-RL robustness.}\nThe alignment-RL result ($N=477$) is statistically robust: DeLong test confirms DIF significantly outperforms ConStat ($p = 0.008$), and TOST equivalence testing ($p = 0.03$) supports DIF retention across paradigms. Bootstrap 95\\% CI for DIF AUROC is [0.74, 0.86].\n\n\\paragraph{Reasoning-RL: preliminary evidence.}\nWith only 13 reasoning-RL models in the cohort, the apparent retention (0.82) reflects dilution within a large group rather than mechanistic robustness. We report this as preliminary evidence requiring validation at larger scale.\n\n\\paragraph{Partial exploitation.}\nTable~\\ref{tab:partial} characterizes detection power as a function of exploitation rate $p$. At $p = 1.0$, DIF achieves TPR = 0.73. Power degrades to 0.44 at $p = 0.6$ and 0.28 at $p = 0.4$. The ensemble handoff point occurs near $p = 0.55$, where DIF and ConStat TPR converge. Below $p = 0.4$, contamination effects on rankings become negligible.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Detection power by exploitation rate. Ensemble TPR combines DIF and ConStat via union.}\n\\label{tab:partial}\n\\begin{tabular}{ccccc}\n\\toprule\n$p$ & Effective $\\delta$ & DIF TPR & ConStat TPR & Ensemble TPR \\\\\n\\midrule\n1.0 & 1.60 & 0.73 & 0.54 & 0.79 \\\\\n0.8 & 1.28 & 0.61 & 0.48 & 0.68 \\\\\n0.6 & 0.96 & 0.44 & 0.42 & 0.55 \\\\\n0.4 & 0.64 & 0.28 & 0.35 & 0.41 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{ConStat Independent Evaluation}\n\\label{sec:exp-constat}\n\nWe independently evaluate ConStat on 220 reformulated items. Table~\\ref{tab:constat-type} reports performance stratified by model type. ConStat achieves AUROC 0.67 on non-RL models but degrades to 0.52 (near-random) on reasoning-RL models, confirming its known vulnerability to RL-induced smoothing.\n\n\\begin{table}[ht]\n\\centering\n\\caption{ConStat detection by model type (FDR = 0.10, 220 reformulated items).}\n\\label{tab:constat-type}\n\\begin{tabular}{lrccc}\n\\toprule\nModel type & $N$ & AUROC & TPR & FPR \\\\\n\\midrule\nAll models & 5,219 & 0.63 & 0.38 & 0.08 \\\\\nNon-RL & 4,742 & 0.67 & 0.44 & 0.07 \\\\\nAlignment-RL & 477 & 0.61 & 0.36 & 0.09 \\\\\nReasoning-RL & 13 & 0.52 & 0.22 & 0.11 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverlap between ConStat and DIF flags is 38\\%, confirming signal orthogonality: ConStat captures per-model perturbation sensitivity while DIF captures group-level behavioral anomalies. This low overlap provides the empirical basis for ensemble complementarity.\n\n\\subsection{DVD Generation Variance Evaluation}\n\\label{sec:exp-dvd}\n\nDVD detection on 12 open-weight models across 500 items yields overall AUROC = 0.56 (Table~\\ref{tab:dvd}). Performance is marginally better for variant contamination (AUROC = 0.61) than verbatim (0.53), but FPR = 0.14 limits practical utility. The bimodal detection rate (18\\%) is too low to distinguish memorization from non-memorization via generation variance in the MCQ setting.\n\n\\begin{table}[ht]\n\\centering\n\\caption{DVD detection performance. The MCQ format inherently limits generation variance signal strength.}\n\\label{tab:dvd}\n\\begin{tabular}{lccc}\n\\toprule\nContamination type & AUROC & TPR @ FPR=0.10 & FPR @ TPR=0.50 \\\\\n\\midrule\nOverall & 0.56 & 0.31 & 0.35 \\\\\nVerbatim & 0.53 & 0.24 & 0.41 \\\\\nVariant & 0.61 & 0.42 & 0.22 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD's weak performance in the MCQ setting is attributable to the constrained output space: 4-way softmax distributions yield minimal variance differences between memorized and non-memorized items. Overlap with DIF (22\\%) and ConStat (28\\%) is low, indicating DVD captures a different but weaker signal. We exclude DVD from the primary ensemble and report it as an exploratory analysis.\n\n\\subsection{Dual-Signal Ensemble}\n\\label{sec:exp-ensemble}\n\nTable~\\ref{tab:ensemble} reports ensemble performance. The DIF + ConStat union achieves the best AUROC (0.72) and highest TPR at $\\delta \\geq 0.8$ (0.58) while maintaining FPR = 0.09. Adding DVD marginally degrades performance (AUROC 0.70, FPR 0.11) due to DVD's high false-positive rate.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Ensemble detection performance across configurations.}\n\\label{tab:ensemble}\n\\begin{tabular}{lcccc}\n\\toprule\nConfiguration & TPR ($\\delta \\geq 0.8$) & TPR ($\\delta \\geq 1.4$) & FPR & AUROC \\\\\n\\midrule\nDIF only & 0.45 & 0.73 & 0.04 & 0.76 \\\\\nConStat only & 0.35 & 0.48 & 0.08 & 0.63 \\\\\nDVD only & 0.22 & 0.31 & 0.14 & 0.56 \\\\\nDIF + ConStat (union) & 0.58 & 0.78 & 0.09 & 0.72 \\\\\nDIF + ConStat + DVD & 0.55 & 0.76 & 0.11 & 0.70 \\\\\nDIF + ConStat (intersection) & 0.42 & 0.52 & 0.03 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFusion weight analysis (Table~\\ref{tab:fusion}) shows optimized weighting (DIF: 0.62, ConStat: 0.38) improves AUROC by 0.03 over uniform weights, but the improvement is within CV noise ($\\sigma = 0.04$--$0.05$). We report uniform weights as the primary result.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Fusion weight analysis (5-fold CV).}\n\\label{tab:fusion}\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Mean AUROC & Std AUROC & DIF weight & ConStat weight \\\\\n\\midrule\nUniform & 0.69 & 0.05 & 0.50 & 0.50 \\\\\nOptimized & 0.72 & 0.04 & 0.62 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCoverage analysis reveals a structural gap: on non-RL models, union coverage reaches 71\\%, but on the full population (including RL models), it drops to 62\\%. The gap originates from ConStat's failure on reasoning-RL models combined with DIF's limited power for medium effect sizes---a region neither signal adequately covers for RL-trained models.\n\n\\subsection{Cross-Benchmark Validation: GSM8K}\n\\label{sec:exp-gsm8k}\n\nWe replicate DIF analysis on GSM8K (62 models, 1,319 items) using GSM1K as independent ground truth. IRT fit is acceptable (RMSEA = 0.075), better than MMLU due to GSM8K's more unidimensional construct (mathematical reasoning). DIF detects 78 ETS-C flags. The correlation between DIF flag density and GSM8K$-$GSM1K accuracy gap is $r = 0.36$ ($p = 0.004$), with 1.8$\\times$ enrichment of DIF flags among high-gap models. The moderate correlation provides corroborating---but not conclusive---evidence that DIF captures contamination-related signals.\n\n\\begin{table}[ht]\n\\centering\n\\caption{GSM8K DIF analysis with GSM1K ground truth.}\n\\label{tab:gsm8k}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nModels & 62 \\\\\nItems & 1,319 \\\\\nETS-C flags & 78 \\\\\nIRT RMSEA & 0.075 \\\\\nDIF--gap correlation ($r$) & 0.36 \\\\\nDIF--gap correlation ($p$) & 0.004 \\\\\nFlag enrichment ratio & 1.8$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:exp-semi-synth}\n\nTable~\\ref{tab:semi-synth-tpr} reports semi-synthetic validation results. TPR = 0.58 at $\\delta \\geq 1.4$ is substantially lower than the 0.73 observed in pure simulation, revealing a simulation-to-real gap of 0.15 in TPR and 0.12 in AUC (Table~\\ref{tab:sim-gap}). This gap arises from noise sources absent in simulation: non-normal ability distributions, negatively discriminating items (15\\% of MMLU), and pre-existing background contamination in the ``clean'' baseline.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Semi-synthetic validation: TPR by effect size (150 injected items, 500 clean items).}\n\\label{tab:semi-synth-tpr}\n\\begin{tabular}{cccc}\n\\toprule\n$\\delta$ threshold & TPR & FPR & $N_\\text{injected}$ \\\\\n\\midrule\n$\\geq 1.4$ & 0.58 & 0.07 & 45 \\\\\n$\\geq 1.0$ & 0.41 & 0.07 & 85 \\\\\n$\\geq 0.6$ & 0.25 & 0.07 & 150 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[ht]\n\\centering\n\\caption{Simulation vs.\\ semi-synthetic gap.}\n\\label{tab:sim-gap}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Simulation & Semi-synthetic & Gap \\\\\n\\midrule\nTPR ($\\delta \\geq 1.4$) & 0.73 & 0.58 & $-$0.15 \\\\\nFPR & 0.04 & 0.07 & +0.03 \\\\\nAUC & 0.94 & 0.82 & $-$0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe three-parameter power surface (Table~\\ref{tab:power-surface}) characterizes detection power as a function of exploitation rate, focal group size, and contamination prevalence ($R^2 = 0.89$). Exploitation rate is the strongest determinant (TPR drops from 0.65 at $p=1.0$ to 0.22 at $p=0.4$), followed by focal group size (TPR 0.44 at $N=40$ vs.\\ 0.68 at $N=200$). Prevalence has the weakest effect (0.52 at 5\\% vs.\\ 0.63 at 30\\%).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Semi-synthetic power surface. Each parameter is varied while others are held at mid-level.}\n\\label{tab:power-surface}\n\\begin{tabular}{lcccccc}\n\\toprule\nParameter & Low & Mid & High & TPR (low) & TPR (mid) & TPR (high) \\\\\n\\midrule\nExploitation rate & 0.4 & 0.7 & 1.0 & 0.22 & 0.45 & 0.65 \\\\\nFocal $N$ & 40 & 80 & 200 & 0.44 & 0.58 & 0.68 \\\\\nPrevalence & 0.05 & 0.15 & 0.30 & 0.52 & 0.58 & 0.63 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Bifactor Equating and Item Regeneration}\n\\label{sec:exp-equating}\n\n\\paragraph{Bifactor model.}\nThe bifactor model converges on the decoder-only subpopulation with RMSEA = 0.062 (Table~\\ref{tab:irt-fit}). The general factor explains 58\\% of variance; 38 of 57 subjects have strong specific factors (standardized loading $> 0.3$), while 19 have weak specific factors (loading $< 0.2$), including abstract algebra, formal logic, jurisprudence, and moral scenarios. Weak-factor subjects pose a structural bottleneck for equating: their items load primarily on the general factor, making anchor-item selection and replacement calibration less stable.\n\n\\paragraph{Anchor items.}\n620 items (5\\%) are selected as anchors based on DIF-free status and cross-cohort stability (ICC = 0.94). Anchor coverage is adequate for strong-factor subjects but sparse for weak-factor subjects.\n\n\\paragraph{Item generation and calibration.}\nTable~\\ref{tab:item-gen} compares calibration methods. Student simulation achieves difficulty correlation $\\rho = 0.78$ and MSE = 0.34, substantially outperforming prompt-based targeting ($\\rho = 0.28$, MSE = 1.85) and random same-subject selection ($\\rho = 0.11$, MSE = 2.40). The 25\\% generation failure rate (items not passing construct filters) indicates that automated replacement still requires quality control.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Item calibration: difficulty correlation and MSE against empirical parameters.}\n\\label{tab:item-gen}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Difficulty $\\rho$ & Difficulty MSE & $N_\\text{items}$ \\\\\n\\midrule\nStudent simulation & 0.78 & 0.34 & 112 \\\\\nPrompt-based targeting & 0.28 & 1.85 & 112 \\\\\nRandom same-subject & 0.11 & 2.40 & 112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Holdout validation.}\nOn a 50-model holdout panel, replaced items achieve equated $\\rho = 0.91$ (vs.\\ the full original benchmark), with systematic quality degradation: mean factor loading drops from 0.50 to 0.41 and discrimination from 1.18 to 0.95 (Table~\\ref{tab:holdout}).\n\n\\begin{table}[ht]\n\\centering\n\\caption{Holdout validation of replacement items (50-model panel).}\n\\label{tab:holdout}\n\\begin{tabular}{lcc}\n\\toprule\nMetric & Original items & Replaced items \\\\\n\\midrule\nSpearman $\\rho$ vs.\\ full & --- & 0.91 \\\\\nMean factor loading & 0.50 & 0.41 \\\\\nMean difficulty & 0.52 & 0.49 \\\\\nMean discrimination & 1.18 & 0.95 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graceful Degradation Analysis}\n\\label{sec:exp-degradation}\n\nTable~\\ref{tab:degradation} characterizes benchmark validity as a function of replacement rate. At 20\\% replacement, Spearman $\\rho = 0.93$, Cronbach's $\\alpha = 0.91$, and construct coverage = 0.89---marginally acceptable. Beyond the critical threshold of 28\\%, validity accelerates its decline. At 50\\%, $\\rho = 0.85$---ranking shifts become too large for meaningful comparison.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Graceful degradation: benchmark validity vs.\\ item replacement rate.}\n\\label{tab:degradation}\n\\begin{tabular}{cccc}\n\\toprule\nReplacement (\\%) & Spearman $\\rho$ & Cronbach's $\\alpha$ & Construct coverage \\\\\n\\midrule\n0 & 1.00 & 0.94 & 1.00 \\\\\n5 & 0.98 & 0.93 & 0.97 \\\\\n10 & 0.96 & 0.93 & 0.94 \\\\\n20 & 0.93 & 0.91 & 0.89 \\\\\n50 & 0.85 & 0.86 & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe theoretical validity loss rate is approximately 0.003 per percentage point of replacement, with acceleration beyond 28\\%. The degradation is driven by weak-factor subjects (\\S\\ref{sec:exp-equating}), where replacement items cannot maintain the original subject-specific factor structure.\n\n% ============================================================\n\\section{Supplementary Analyses}\n\\label{sec:supplementary}\n\n\\subsection{Item-Focused Trees}\n\\label{sec:exp-ift}\n\nAs a methodological alternative to categorical DIF, Item-Focused Trees (IFT) treat release date as a continuous covariate. IFT flags 520 items with AUC = 0.78, slightly higher than ETS-C (AUC = 0.76), but with higher FPR (0.07 vs.\\ 0.04). The automatically learned split point (September 2023) aligns with the estimated onset of accelerated benchmark leakage. Overlap with ETS-C is 62\\%, suggesting IFT captures gradual contamination patterns that binary cohort splits miss.\n\n\\begin{table}[ht]\n\\centering\n\\caption{IFT vs.\\ ETS-C DIF comparison.}\n\\label{tab:ift}\n\\begin{tabular}{lrcccc}\n\\toprule\nMethod & Flags & TPR ($\\delta \\geq 1.4$) & FPR & AUC & Overlap \\\\\n\\midrule\nETS-C & 485 & 0.73 & 0.04 & 0.76 & --- \\\\\nIFT & 520 & 0.69 & 0.07 & 0.78 & 0.62 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cumulative Bayesian DIF}\n\\label{sec:exp-bayes}\n\nCumulative Bayesian DIF uses the posterior from each administration as the prior for the next. Table~\\ref{tab:bayes} shows power accumulation: from 0.38 (single administration, $\\delta = 1.0$) to 0.72 after four administrations, with diminishing marginal returns. FPR remains controlled at 0.06. This supports DIF as a longitudinal monitoring tool rather than a one-shot detector.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Cumulative Bayesian DIF power (simulated, $\\delta = 1.0$).}\n\\label{tab:bayes}\n\\begin{tabular}{cccc}\n\\toprule\nAdministrations & Power ($\\delta = 1.0$) & Power ($\\delta = 1.4$) & FPR \\\\\n\\midrule\n1 & 0.38 & 0.73 & 0.04 \\\\\n2 & 0.52 & 0.82 & 0.05 \\\\\n3 & 0.65 & 0.88 & 0.05 \\\\\n4 & 0.72 & 0.91 & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Methodological contributions.}\nOur primary contributions are methodological rather than systemic. First, we provide the first large-scale IRT fit diagnostic for LLM populations, establishing that architecture heterogeneity---not item quality or sample size---is the primary obstacle to psychometric modeling of LLM evaluation data. The practical prescription is straightforward: restrict IRT-based analyses to architecturally homogeneous subpopulations.\n\nSecond, the semi-synthetic validation framework provides a general-purpose tool for evaluating any item-level contamination detector under controlled conditions on real response data. The revealed simulation-to-real gap (TPR $-$0.15, AUC $-$0.12) cautions against relying solely on simulation for detector evaluation.\n\nThird, the student-simulation calibration method ($\\rho = 0.78$) significantly outperforms prompt-based targeting ($\\rho = 0.28$) for replacement item difficulty estimation, establishing a viable calibration strategy for benchmark regeneration.\n\n\\paragraph{Boundary conditions.}\nOur claims carry explicit boundary conditions:\n\\begin{itemize}\n\\item DIF detection requires architecturally homogeneous subpopulations (decoder-only) and is practical only for large effects ($\\delta \\geq 1.4$). At medium effects ($\\delta \\in [0.6, 1.4]$), detection power is insufficient without ensemble support.\n\\item The dual-signal ensemble has a coverage gap: reasoning-RL models at medium effect sizes are inadequately covered by either DIF (insufficient power) or ConStat (RL-degraded).\n\\item Within-family analysis reveals 42\\% overlap between temporal DIF and within-family DIF, meaning nearly half of flagged items may reflect capability growth rather than contamination.\n\\item Benchmark regeneration quality systematically degrades: replacement items have lower factor loadings (0.41 vs.\\ 0.50) and discrimination (0.95 vs.\\ 1.18), with a critical replacement threshold at 28\\%.\n\\end{itemize}\n\n\\paragraph{DVD negative result.}\nDVD generation variance detection achieves AUROC = 0.56 in the MCQ setting---marginally above random. The 4-way MCQ output space provides insufficient variance signal, and the bimodal detection rate (18\\%) is too low for practical use. We report this as a methodologically informative negative result: generation variance approaches may be better suited to open-ended generation tasks than constrained MCQ formats.\n\n\\paragraph{Reasoning-RL coverage gap.}\nThe most significant limitation is the reasoning-RL validation gap. With only 13 reasoning-RL models available, our DIF retention results (0.82) reflect statistical dilution rather than mechanistic verification. As reasoning-RL models become more prevalent, the decoder-only subpopulation will increasingly contain RL-trained models, potentially changing DIF dynamics. Longitudinal monitoring will be needed to validate DIF stability in this evolving landscape.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present a psychometric approach to benchmark contamination detection and regeneration, demonstrating that DIF analysis provides a structurally RL-robust contamination signal when applied to architecturally homogeneous LLM subpopulations. Our contributions center on detection methodology and psychometric diagnostics rather than a complete end-to-end system: (1)~the first large-scale IRT fit analysis revealing architecture heterogeneity as the primary obstacle; (2)~a dual-signal DIF+ConStat ensemble with complementary coverage (AUROC 0.72); (3)~a semi-synthetic validation framework that quantifies detector performance under controlled conditions; and (4)~pilot-scale bifactor equating for item regeneration ($\\rho = 0.91$). All claims are qualified by empirically established boundary conditions---architecture homogeneity, large effect sizes, and limited replacement budgets---and we transparently report both the reasoning-RL coverage gap and the DVD negative result. The three-parameter power surface ($R^2 = 0.89$) provides practitioners with actionable guidelines for deploying DIF-based monitoring in their evaluation pipelines.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem{wang2026rl}\nWang, Z., et al. (2026).\n\\newblock Contamination signals vanish after reinforcement learning: A systematic evaluation.\n\\newblock In \\emph{Proceedings of ICLR 2026}.\n\n\\bibitem{livebench2024}\nWhite, C., et al. (2024).\n\\newblock LiveBench: A challenging, contamination-free LLM benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}.\n\n\\bibitem{constat2024}\nOren, Y., et al. (2024).\n\\newblock ConStat: Performance-based contamination detection in large language models.\n\\newblock In \\emph{Proceedings of NeurIPS 2024}.\n\n\\bibitem{growingpains2026}\nZhang, L., et al. (2026).\n\\newblock Growing pains: Multidimensional IRT for extensible LLM evaluation.\n\\newblock \\emph{arXiv preprint arXiv:2601.xxxxx}.\n\n\\bibitem{metabench2025}\nPerlitz, Y., et al. (2025).\n\\newblock METABENCH: A large-scale repository of LLM evaluation results.\n\\newblock In \\emph{Proceedings of ICLR 2025}.\n\n\\bibitem{holland1988dif}\nHolland, P.~W. and Thayer, D.~T. (1988).\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock In \\emph{Test Validity}, pages 129--145.\n\n\\bibitem{studentsim2025}\nLi, R., et al. (2025).\n\\newblock Student simulation for item difficulty estimation.\n\\newblock \\emph{arXiv preprint arXiv:2601.09953}.\n\n\\bibitem{gsm1k2024}\nZhang, H., et al. (2024).\n\\newblock Careful examination of large language model performance on {GSM8K}.\n\\newblock \\emph{arXiv preprint arXiv:2405.00332}.\n\n\\bibitem{mmlucf2024}\nWiegreffe, S., et al. (2024).\n\\newblock {MMLU-CF}: A contamination-free multi-task benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2412.15194}.\n\n\\bibitem{dvd2024}\nDunn, A., et al. (2024).\n\\newblock Detecting pretraining data from large language models via generation variance.\n\\newblock \\emph{arXiv preprint arXiv:2407.14985}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7846f432-073d-4529-bebd-fc1f2889ef55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "e8b65109-d36a-4c90-b8d8-04ffa42225b2",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT methodology",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Tool call

_source line 23 · 2026-05-20T21:21:07.828Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PyqyLQvDrjxNwgstPEANZB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b65109-d36a-4c90-b8d8-04ffa42225b2",
  "isSidechain": false,
  "requestId": "req_011CbEXBPzRHvYh1nGj4GysP",
  "type": "assistant",
  "uuid": "4b641f6e-9bc5-4533-9305-fb39a6bb5238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9yPgY5vt3LUGHmfHggktD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12484,
      "cache_read_input_tokens": 43788,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 43788,
          "cache_creation_input_tokens": 12484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12484
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

_source line 24 · 2026-05-20T21:21:08.414Z_

<details><summary>↩ Tool result · reported error · `toolu_01PyqyLQvDrjxNwgstPEANZB`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
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
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: Reference `tab:irt-fit' on page 3 undefined on input line 98.


LaTeX Warning: Reference `tab:spurious-dif' on page 3 undefined on input line 1
19.


LaTeX Warning: Reference `tab:dif-cohort' on page 3 undefined on input line 139
.


LaTeX Warning: Reference `tab:within-family' on page 3 undefined on input line 
157.

[3]

LaTeX Warning: Reference `sec:exp-semi-synth' on page 4 undefined on input line
 180.


LaTeX Warning: Reference `tab:rl-robust' on page 4 undefined on input line 185.



LaTeX Warning: Reference `tab:detector-comp' on page 4 undefined on input line 
202.


LaTeX Warning: Reference `tab:partial' on page 4 undefined on input line 227.

[4]

LaTeX Warning: Reference `tab:constat-type' on page 5 undefined on input line 2
48.


LaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 271.


LaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 293.


LaTeX Warning: Reference `tab:fusion' on page 5 undefined on input line 313.

[5]

LaTeX Warning: Reference `tab:semi-synth-tpr' on page 6 undefined on input line
 358.


LaTeX Warning: Reference `tab:sim-gap' on page 6 undefined on input line 358.


LaTeX Warning: Reference `tab:power-surface' on page 6 undefined on input line 
390.


LaTeX Warning: Reference `tab:irt-fit' on page 6 undefined on input line 411.


LaTeX Warning: Reference `tab:item-gen' on page 6 undefined on input line 417.

[6]

LaTeX Warning: Reference `tab:holdout' on page 7 undefined on input line 435.


LaTeX Warning: Reference `tab:degradation' on page 7 undefined on input line 45
6.


LaTeX Warning: Reference `sec:exp-equating' on page 7 undefined on input line 4
75.


LaTeX Warning: Reference `tab:bayes' on page 7 undefined on input line 503.

[7] [8] [9] [10] [11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.


! Package natbib Error: Bibliography not compatible with author-year citations.

(natbib)                Press &lt;return> to continue in numerical citation style.


See the natbib package documentation for explanation.
Type  H &lt;return>  for immediate help.
 ...                                              
                                                  
l.109 ...and\NAT@force@numbers{}\NAT@force@numbers
                                                  
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
amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (11 pages, 249994 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b641f6e-9bc5-4533-9305-fb39a6bb5238",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "b9834a4b-82c7-42f3-9173-c9fb905e09fa",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `tab:irt-fit' on page 3 undefined on input line 98.\n\n\nLaTeX Warning: Reference `tab:spurious-dif' on page 3 undefined on input line 1\n19.\n\n\nLaTeX Warning: Reference `tab:dif-cohort' on page 3 undefined on input line 139\n.\n\n\nLaTeX Warning: Reference `tab:within-family' on page 3 undefined on input line \n157.\n\n[3]\n\nLaTeX Warning: Reference `sec:exp-semi-synth' on page 4 undefined on input line\n 180.\n\n\nLaTeX Warning: Reference `tab:rl-robust' on page 4 undefined on input line 185.\n\n\n\nLaTeX Warning: Reference `tab:detector-comp' on page 4 undefined on input line \n202.\n\n\nLaTeX Warning: Reference `tab:partial' on page 4 undefined on input line 227.\n\n[4]\n\nLaTeX Warning: Reference `tab:constat-type' on page 5 undefined on input line 2\n48.\n\n\nLaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 271.\n\n\nLaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 293.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 5 undefined on input line 313.\n\n[5]\n\nLaTeX Warning: Reference `tab:semi-synth-tpr' on page 6 undefined on input line\n 358.\n\n\nLaTeX Warning: Reference `tab:sim-gap' on page 6 undefined on input line 358.\n\n\nLaTeX Warning: Reference `tab:power-surface' on page 6 undefined on input line \n390.\n\n\nLaTeX Warning: Reference `tab:irt-fit' on page 6 undefined on input line 411.\n\n\nLaTeX Warning: Reference `tab:item-gen' on page 6 undefined on input line 417.\n\n[6]\n\nLaTeX Warning: Reference `tab:holdout' on page 7 undefined on input line 435.\n\n\nLaTeX Warning: Reference `tab:degradation' on page 7 undefined on input line 45\n6.\n\n\nLaTeX Warning: Reference `sec:exp-equating' on page 7 undefined on input line 4\n75.\n\n\nLaTeX Warning: Reference `tab:bayes' on page 7 undefined on input line 503.\n\n[7] [8] [9] [10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n\n! Package natbib Error: Bibliography not compatible with author-year citations.\n\n(natbib)                Press &lt;return> to continue in numerical citation style.\n\n\nSee the natbib package documentation for explanation.\nType  H &lt;return>  for immediate help.\n ...                                              \n                                                  \nl.109 ...and\\NAT@force@numbers{}\\NAT@force@numbers\n                                                  \n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (11 pages, 249994 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "4b641f6e-9bc5-4533-9305-fb39a6bb5238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T21:21:14.025Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF was generated (11 pages, 249994 bytes) but there's a natbib compatibility issue. The error is that `plainnat` bibliography style expects author-year citations but the `thebibliography` environment doesn't provide the right format. Let me fix this by switching to a numeric citation style or fixing the bibliography.

The simplest fix is to change `\bibliographystyle{plainnat}` to just use `\usepackage[numbers]{natbib}` or switch to a plain bibliography style. Let me just change the natbib option to numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9834a4b-82c7-42f3-9173-c9fb905e09fa",
  "isSidechain": false,
  "requestId": "req_011CbEXBjdsLXReLD53gYW1R",
  "type": "assistant",
  "uuid": "a81a2e8d-2efe-4ad1-84d9-b08864c241cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2gRhdU6MvvmZBGcJ6Lei6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 56272,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 56272,
          "cache_creation_input_tokens": 3635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3635
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

_source line 26 · 2026-05-20T21:21:15.004Z_

PDF generated (11 pages) but natbib threw an error on the second pass. Let me fix the citation style compatibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a81a2e8d-2efe-4ad1-84d9-b08864c241cb",
  "isSidechain": false,
  "requestId": "req_011CbEXBjdsLXReLD53gYW1R",
  "type": "assistant",
  "uuid": "0cd9f669-d383-4736-a2e4-f31aa2c3b8f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2gRhdU6MvvmZBGcJ6Lei6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 56272,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 56272,
          "cache_creation_input_tokens": 3635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3635
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

_source line 27 · 2026-05-20T21:21:15.795Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GL37WJckHb4AEyPytZwkHA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex",
  "old_string": "\\usepackage{natbib}",
  "new_string": "\\usepackage[numbers]{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd9f669-d383-4736-a2e4-f31aa2c3b8f9",
  "isSidechain": false,
  "requestId": "req_011CbEXBjdsLXReLD53gYW1R",
  "type": "assistant",
  "uuid": "f6c3ffa3-415a-43f9-9ed3-98c97ed8f7cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2gRhdU6MvvmZBGcJ6Lei6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3635,
      "cache_read_input_tokens": 56272,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 330,
          "cache_read_input_tokens": 56272,
          "cache_creation_input_tokens": 3635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3635
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

_source line 28 · 2026-05-20T21:21:15.813Z_

<details><summary>↩ Tool result · `toolu_01GL37WJckHb4AEyPytZwkHA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6c3ffa3-415a-43f9-9ed3-98c97ed8f7cd",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "e683b5f8-c4bd-42f9-af29-d0507ef1ecdd",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.tex",
    "oldString": "\\usepackage{natbib}",
    "newString": "\\usepackage[numbers]{natbib}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " \\usepackage{booktabs}",
          " \\usepackage{graphicx}",
          " \\usepackage{hyperref}",
          "-\\usepackage{natbib}",
          "+\\usepackage[numbers]{natbib}",
          " \\usepackage{xcolor}",
          " \\usepackage{multirow}",
          " \\usepackage{tabularx}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f6c3ffa3-415a-43f9-9ed3-98c97ed8f7cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T21:21:15.884Z_

```json
{
  "parentUuid": "e683b5f8-c4bd-42f9-af29-d0507ef1ecdd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2e335894-98ff-4178-90cf-92b39a489050",
  "timestamp": "2026-05-20T21:21:15.884Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T21:21:18.922Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W4X11cz8T9biGVqtizbGHr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Recompile LaTeX with fixed natbib",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e335894-98ff-4178-90cf-92b39a489050",
  "isSidechain": false,
  "requestId": "req_011CbEXCHV2wQDxjkSgPFHZ6",
  "type": "assistant",
  "uuid": "6f05d6ce-48fb-44d0-9637-73ec6f6b0a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RH8yV3Rp6LsxmoekyUEbXT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 59907,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 59907,
          "cache_creation_input_tokens": 524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 524
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

_source line 31 · 2026-05-20T21:21:19.943Z_

<details><summary>↩ Tool result · `toolu_01W4X11cz8T9biGVqtizbGHr`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
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
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]
[11] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (11 pages, 252501 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
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
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]
[11] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>
Output written on paper.pdf (11 pages, 252501 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f05d6ce-48fb-44d0-9637-73ec6f6b0a43",
  "isSidechain": false,
  "promptId": "efecec37-8615-486c-a600-e1aa829e651b",
  "type": "user",
  "uuid": "ce353d08-4330-46e8-8be7-01adbb99651d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]\n[11] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (11 pages, 252501 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]\n[11] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb>\nOutput written on paper.pdf (11 pages, 252501 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6f05d6ce-48fb-44d0-9637-73ec6f6b0a43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "ce353d08-4330-46e8-8be7-01adbb99651d",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT methodology",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Assistant

_source line 34 · 2026-05-20T21:21:33.464Z_

编译成功，无错误。`paper.pdf` 已生成（11页，252KB），位于 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median/paper.pdf`。

论文覆盖全部11个实验（`experiment_data.json`中的每一个），结构：
- **Tables 1--3**: IRT拟合诊断 + 架构分层 + DIF检测 + within-family混淆分析
- **Tables 4--6**: RL鲁棒性 + 检测器对比 + 部分利用功率曲线
- **Table 7**: ConStat独立评估
- **Table 8**: DVD负结果（放入正文但标注为探索性）
- **Tables 9--10**: 双信号ensemble融合
- **Table 11**: GSM8K跨benchmark验证
- **Tables 18--20**: Semi-synthetic验证 + 功率曲面 + 模拟-真实gap
- **Tables 12--15**: Bifactor equating + item regeneration + holdout验证
- **Table S2**: Graceful degradation
- **Tables S1, S3**: Cumulative Bayesian DIF + IFT（补充分析）

所有数字均取自 `experiment_data.json`，Claims按narrative guidance降级处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce353d08-4330-46e8-8be7-01adbb99651d",
  "isSidechain": false,
  "requestId": "req_011CbEXCaroWry48qysw71SJ",
  "type": "assistant",
  "uuid": "f997afef-67c5-4374-9898-f6118f1f87d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260520T205007/median",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DncuzR9bb37ogbRVW6hR39",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5560,
      "cache_read_input_tokens": 60431,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5560,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 60431,
          "cache_creation_input_tokens": 5560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5560
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T205007 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "f997afef-67c5-4374-9898-f6118f1f87d8",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper with IRT methodology",
  "sessionId": "3be65274-1c7a-4df1-b2f9-03f667310cd1"
}
```

---
