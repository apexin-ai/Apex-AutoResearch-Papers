# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/12403ebc-9514-4215-82a8-4a9860541744.jsonl`
- **Structured JSON:** [`526792360c5fc1be972b.json`](../../sessions/52/526792360c5fc1be972b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T10:27:33.518Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T10:27:33.518Z",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：原始 framing 完全成立。三个 Claims 强度不变：Claim 1 以 LOGO binary F1=0.694 作为 headline， cross-model 0.830 和 LOFO 0.686 作为 generalization 佐证；Claim 2 的 DDR 分离经 causality analysis（6/7 Granger sig, 5.5× permutation gap）和 TOST bootstrap 确认，被审稿人接受为 genuine empirical contribution 而非 vocabulary impoverishment 的重新包装；Claim 3 的 negative finding 被认可为 honest science。论文定位 Findings-level empirical+conceptual paper， reviewer 平均分 3.5–4.0，spread 3–4。9 generators / 5 families / 3 prompt types / 4 domains / causality analysis / robustness tests 的体量被视为 thorough。Instruct 退化的诚实报告是 strength。 33 页论文组织未被 reviewer 视为问题。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T10:27:33.521Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T10:27:33.521Z",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-20T10:27:33.539Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：原始 framing 完全成立。三个 Claims 强度不变：Claim 1 以 LOGO binary F1=0.694 作为 headline， cross-model 0.830 和 LOFO 0.686 作为 generalization 佐证；Claim 2 的 DDR 分离经 causality analysis（6/7 Granger sig, 5.5× permutation gap）和 TOST bootstrap 确认，被审稿人接受为 genuine empirical contribution 而非 vocabulary impoverishment 的重新包装；Claim 3 的 negative finding 被认可为 honest science。论文定位 Findings-level empirical+conceptual paper， reviewer 平均分 3.5–4.0，spread 3–4。9 generators / 5 families / 3 prompt types / 4 domains / causality analysis / robustness tests 的体量被视为 thorough。Instruct 退化的诚实报告是 strength。 33 页论文组织未被 reviewer 视为问题。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "3cbbdca3-0c80-416c-bb69-8d4818051bc8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T10:27:33.538Z_

```json
{
  "parentUuid": "3cbbdca3-0c80-416c-bb69-8d4818051bc8",
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
  "uuid": "71c620b9-cfba-4a97-b901-cad76d531da5",
  "timestamp": "2026-05-20T10:27:33.538Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T10:27:33.538Z_

```json
{
  "parentUuid": "71c620b9-cfba-4a97-b901-cad76d531da5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0931baa5-194d-4fb7-9ab7-4b1268b546fc",
  "timestamp": "2026-05-20T10:27:33.538Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
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
  "aiTitle": "Generate complete simulated research paper from dream data",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Assistant

_source line 7 · 2026-05-20T10:27:35.950Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0931baa5-194d-4fb7-9ab7-4b1268b546fc",
  "isSidechain": false,
  "requestId": "req_011CbDfM3ExfxWsuyUDxhfzQ",
  "type": "assistant",
  "uuid": "2484f24b-19fe-4154-9129-4780f7a1afa5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9QKrhrDTDZCyrkAmDRmTy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12886,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12886
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

_source line 8 · 2026-05-20T10:27:37.055Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9JLQky3h8agbzCku6XhYg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2484f24b-19fe-4154-9129-4780f7a1afa5",
  "isSidechain": false,
  "requestId": "req_011CbDfM3ExfxWsuyUDxhfzQ",
  "type": "assistant",
  "uuid": "2a62018f-1eb1-41ae-9d06-cf9d78b0cfa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9QKrhrDTDZCyrkAmDRmTy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12886,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12886
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

_source line 9 · 2026-05-20T10:27:37.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J3hcSXW941sspPniXdmQPi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a62018f-1eb1-41ae-9d06-cf9d78b0cfa1",
  "isSidechain": false,
  "requestId": "req_011CbDfM3ExfxWsuyUDxhfzQ",
  "type": "assistant",
  "uuid": "b6015340-97d5-40a5-b677-162736805e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9QKrhrDTDZCyrkAmDRmTy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12886,
      "cache_read_input_tokens": 11841,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12886
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

_source line 10 · 2026-05-20T10:27:37.215Z_

<details><summary>↩ Tool result · `toolu_01J3hcSXW941sspPniXdmQPi`</summary>

```text
1	# Paper Framing — gen-depth-fingerprint
2	
3	## Target Venue
4	- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标
5	- Positioning: **Findings paper**（非 main conference long paper）
6	- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)
7	
8	## Core Insight
9	Non-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.
10	
11	## Core Claims (3 条，均可证伪)
12	
13	**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.
14	
15	**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.
16	
17	**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.
18	
19	## Headline Metrics Summary
20	
21	| Metric | Value | Context |
22	|--------|-------|---------|
23	| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |
24	| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |
25	| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |
26	| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |
27	| LOFO binary F1 | 0.686 | Leave-one-family-out |
28	| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |
29	| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |
30	| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |
31	| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |
32	| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |
33	
34	## Scope & Limitations (必须在论文中突出)
35	
36	1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.
37	2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).
38	3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.
39	4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).
40	5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.
41	6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).
42	
43	## Story Spine
44	
45	**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.
46	
47	**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.
48	
49	**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.
50	
51	**Headline result template**: "On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization."
52	
53	## Anticipated Reviewer Concerns
54	
55	**RC1 — "Is this just vocabulary impoverishment?"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.
56	
57	**RC2 — "Does this generalize beyond Pythia?"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.
58	
59	**RC3 — "Is 3-class sufficient?"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.
60	
61	**RC4 — "How realistic are single-model chains?"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.
62	
63	**RC5 — "What about human editing?"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.
64	
65	**RC6 — "Ecological validity?"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).
66	
67	**RC8 — "Aren't these just OOD detection features?"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.
68	
69	**RC9 — "Only base models — what about instruct?"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.
70	
71	**RC10 — "Text length confound"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.
72	
73	**RC11 — "Downstream — limited evidence"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.
74	
75	## Contribution Positioning (Findings Level)
76	The contribution is **empirical and conceptual**, appropriate for Findings:
77	1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)
78	2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).
79	3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.
80	
81	**Framing discipline:**
82	- Do NOT call the drift/stationarity split a "discovery" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.
83	- Do NOT use H1/H2 terminology. Use "drifting" vs "stationary" or "differential response."
84	- Do NOT overclaim "dual dynamics." Use "differential depth response" (DDR).
85	- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.
86	- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).
87	- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.
88	
89	Related work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.
90	
91	## Venue Fit
92	- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.
93	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6015340-97d5-40a5-b677-162736805e62",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "ef7d0931-a681-4d6a-a2f2-62db39bbf1ea",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper_framing.md",
      "content": "# Paper Framing — gen-depth-fingerprint\n\n## Target Venue\n- **Primary: EMNLP 2026 Findings (ARR deadline: May 25, 2026)** — D012: 恢复为主投稿目标\n- Positioning: **Findings paper**（非 main conference long paper）\n- Fallback venues: ICLR 2027 (Sep 24), NAACL 2027 ARR (Oct 16)\n\n## Core Insight\nNon-paraphrastic LLM generation chains exhibit **differential depth response** (DDR): **central-tendency/diversity features** (entropy_mean, TTR, hapax ratio) drift monotonically with depth, while **shape features** (entropy_max, tail_decay) remain near-stationary. This is consistent with recursive generation inducing a **location shift** in the NLL distribution while approximately preserving distributional shape. The contribution is: (a) the **task formulation** (generation depth classification beyond binary detection), (b) **empirical validation** across 8 generators / 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B–8B) showing DDR is robust, (c) a lightweight 7-feature ensemble achieving leak-free binary F1 = 0.694 under 8-gen LOGO. Depth signal degrades substantially under instruction tuning, restricting current scope to base models.\n\n## Core Claims (3 条，均可证伪)\n\n**Claim 1 — Depth Discriminability**: A 7-feature distributional ensemble can classify generation depth (gen-0 / gen-1 / gen-2+) with leak-free binary F1 = 0.694 (95% CI [0.688, 0.700]) under 8-generator LOGO evaluation, generalizing across unseen generators and model families (LOFO binary F1 = 0.686). Cross-model chains yield binary F1 = 0.830 under generator-level LOGO (5-gen subset). Primary metric is leak-free binary F1 (gen-1 vs gen-2+), excluding gen-0 to avoid seed-sharing leakage.\n\n**Claim 2 — Differential Depth Response & Feature Complementarity**: Features exhibit DDR: drifting features show |ρ| > 0.60 (hapax −0.63, TTR −0.61, entropy_mean −0.60), while shape features show |ρ| < 0.10 (tail_decay 0.04). KS statistics confirm: drifting 0.516–0.537 vs shape 0.043–0.052 (~10× gap). Full 7-feature set (10-fold CV F1 = 0.773) outperforms surface-only (0.688) and reference-only (0.713; McNemar p ≈ 0). Reference-only yields higher binary F1 (0.833 vs 0.695) but surface features are essential for 3-class gen-0 discrimination.\n\n**Claim 3 — Downstream Utility (Negative Finding)**: Depth-aware data curation does NOT improve downstream CLM quality. At equal sample count (n=3,951): random subsampling (ppl=2.367) outperforms depth 0–1 (2.387) and binary-filtered (2.389). TOST confirms equivalence at ±2% margin (p = 1.1×10⁻⁴). Full dataset (n=12,299, ppl=2.335) vs depth-filtered requires ±3% margin for equivalence. Depth fingerprinting is a **diagnostic** tool for provenance characterization, not a **curative** tool for data selection.\n\n## Headline Metrics Summary\n\n| Metric | Value | Context |\n|--------|-------|---------|\n| **Primary: LOGO binary F1** | **0.694** [0.688, 0.700] | 8-gen LOGO, gen-1 vs gen-2+, leak-free |\n| LOGO 3-class F1 | 0.762 [0.758, 0.766] | Inflated by gen-0 seed sharing |\n| Cross-model binary F1 | 0.830 | 5-gen subset, generator-level LOGO |\n| Cross-model 3-class F1 | 0.789 | 5-gen subset, generator-level LOGO |\n| LOFO binary F1 | 0.686 | Leave-one-family-out |\n| Per-gen binary F1 range | 0.633–0.724 | Mistral-7B lowest, Pythia-2.8B highest |\n| 9-gen LOGO 3-class F1 | 0.751 | +Gemma-2-2B; Gemma gen-1 F1=0.036 anomaly |\n| DDR causality | 6/7 Granger sig, 5.5× perm imp gap | Drifting dominance confirmed |\n| Feature ablation (10-fold CV) | Full 0.773, Surface 0.688, Ref 0.713 | McNemar p ≈ 0 |\n| Length-matched binary F1 | 0.724 vs 0.770 unmatched | Deconfounding, not sample-size effect |\n\n## Scope & Limitations (必须在论文中突出)\n\n1. **Base models only**: Instruct-tuned models show substantially degraded signal (OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base). Alignment-imposed length regulation and format constraints compress the distributional variation DDR exploits. This is the **primary scope limitation**.\n2. **Temperature sensitivity**: Reliable within t ∈ [0.5, 0.9] (≤1 pp degradation from default t=0.7). At t = 1.0: −6 pp degradation; entropy_mean ρ drops from −0.60 to −0.002. Cross-temperature transfer degrades severely (t=0.7 → t=1.0: Qwen3-1.7B F1 drops 0.789 → 0.418).\n3. **7-feature ensemble is not optimal**: Multi-detector ensembles (4-det + surface) achieve 3-class 0.795 vs 0.774 (+2.1 pp) and binary 0.708 vs 0.705 (+0.3 pp), but at 2.4× inference cost and 3.2× GPU memory. 7-feature positioned on **efficiency advantage**, not absolute performance.\n4. **3-class resolution ceiling**: 5-class F1 drops to ~0.50; ordinal methods (CORAL, Frank-Hall) yield no improvement over standard XGBoost. Gen-1/gen-2+ boundary is the bottleneck (concentrates 86% of binary errors as FNs).\n5. **Scale effect**: Larger generators show moderate degradation (Mistral-7B: 0.633, Qwen3-8B: 0.692 vs average 0.694). Higher-capacity models compress feature margins.\n6. **Prompt-type dependence**: Continuation chains show stronger drift (F1 = 0.781) than elaboration (0.730).\n\n## Story Spine\n\n**Problem**: Web-scraped training data increasingly contains LLM-generated text of unknown provenance depth (7–17% of recent scientific papers). Current detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material: gen-1 retains much of the source distribution's lexical properties, while deeper text exhibits measurably reduced vocabulary diversity and compressed perplexity.\n\n**Existing approaches & gaps**: Binary detectors (FastDetectGPT, Binoculars, LD-Score) cannot distinguish gen-1 from gen-2+. Attractor cycle theory (ACL 2025) bounds paraphrasing chains to ~3 classes but depends on semantic-preservation constraints. No existing method addresses generation depth estimation in non-paraphrastic continuation chains. When repurposed as ordinal depth predictors, single detector scores show moderate signal but high cross-generator variance.\n\n**Our framing**: We formulate generation depth classification (gen-0/gen-1/gen-2+) and characterize DDR across 8 base-model generators from 5 families (0.6B–8B). Central-tendency features drift monotonically while shape features remain near-stationary, consistent with recursive generation inducing a location shift in the NLL distribution. A 7-feature ensemble achieves leak-free binary F1 = 0.694 under 8-gen LOGO with a single 410M reference model. Multi-detector ensembles achieve marginally higher F1 at 2.4× cost. The signal degrades under instruction tuning and high temperature, restricting current scope to base models at moderate temperatures.\n\n**Headline result template**: \"On 8 base-model generators from 5 families (0.6B–8B), our 7-feature ensemble achieves leak-free binary F1 = 0.694 under LOGO evaluation and 0.830 on cross-model chains, using a single 410M reference model. Depth-aware curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2% margin), establishing depth fingerprinting as a diagnostic tool for provenance characterization.\"\n\n## Anticipated Reviewer Concerns\n\n**RC1 — \"Is this just vocabulary impoverishment?\"**: Surface features alone achieve 0.688, but full features achieve 0.773 (McNemar p ≈ 0). Reference features capture different, complementary signal. Reference-only yields higher binary F1 (0.833) but misses gen-0 discrimination. The complementarity itself is a finding.\n\n**RC2 — \"Does this generalize beyond Pythia?\"**: 8 generators from 5 families (Pythia, OLMo, Qwen, Llama, Mistral). LOFO binary F1 = 0.686 confirms cross-family transfer. Cross-model chains (heterogeneous generators per depth step) yield binary F1 = 0.764.\n\n**RC3 — \"Is 3-class sufficient?\"**: 5-class F1 drops to ~0.50. Ordinal methods (CORAL, Frank-Hall) yield no improvement. Gen-1/gen-2+ boundary is the resolution bottleneck. 3 classes represent practical ceiling.\n\n**RC4 — \"How realistic are single-model chains?\"**: Cross-model chains (different generator per step) are evaluated and yield higher F1 (0.764 binary), suggesting generator heterogeneity amplifies distributional shifts.\n\n**RC5 — \"What about human editing?\"**: Robustness test with simulated human edits (random word replacement + LLM-simulated editing). Reported in appendix.\n\n**RC6 — \"Ecological validity?\"**: Multi-domain seeds (news, Wikipedia, scientific, creative) + multiple prompt types (continuation, elaboration, rewriting). Prompt-type dependence reported transparently (continuation 0.781 vs elaboration 0.730).\n\n**RC8 — \"Aren't these just OOD detection features?\"**: Contribution is NOT the features but: (a) ordinal depth estimation formulation, (b) empirical DDR discovery (drifting vs stationary), (c) Findings-level empirical characterization. Paper explicitly connects to OOD/perplexity-based detection literature.\n\n**RC9 — \"Only base models — what about instruct?\"**: Acknowledged as primary limitation. OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base. Instruction tuning compresses the distributional variation DDR exploits. Reported transparently; defines scope boundary.\n\n**RC10 — \"Text length confound\"**: Length-matched subsampling: binary F1 = 0.724 (vs 0.770 unmatched). Random-subsample control confirms drop reflects deconfounding, not sample-size reduction.\n\n**RC11 — \"Downstream — limited evidence\"**: Three seeds, single perplexity metric. TOST equivalence confirmed at ±2% margin for equal-count comparison. Margin sensitivity analysis across ±1%–5% reported. Cohen's d inflated by low seed-level variance; TOST is the appropriate test.\n\n## Contribution Positioning (Findings Level)\nThe contribution is **empirical and conceptual**, appropriate for Findings:\n1. **Problem formulation**: Generation depth classification as a new task beyond binary detection (no prior work addresses this in non-paraphrastic chains)\n2. **Empirical characterization**: DDR across 8 generators / 5 families (0.6B–8B), with cross-generator generalization (LOGO binary F1 = 0.694, LOFO 0.686, cross-model 0.764). Honest reporting of scope boundaries (instruct degradation, temperature sensitivity, scale effect).\n3. **Negative finding**: Depth-aware curation ≡ random subsampling for downstream quality (TOST confirmed). Depth fingerprinting is diagnostic, not curative.\n\n**Framing discipline:**\n- Do NOT call the drift/stationarity split a \"discovery\" — it follows from location-shift properties of the NLL distribution. Acknowledge explicitly.\n- Do NOT use H1/H2 terminology. Use \"drifting\" vs \"stationary\" or \"differential response.\"\n- Do NOT overclaim \"dual dynamics.\" Use \"differential depth response\" (DDR).\n- Report **realistic performance range** (binary F1 0.633–0.724 per-generator, 0.694 LOGO average) in abstract/conclusion, not best-case.\n- Primary metric is leak-free binary F1 (not 3-class, which is inflated by gen-0 seed sharing).\n- 7-feature ensemble is positioned on efficiency, not absolute superiority over multi-detector ensembles.\n\nRelated work must cover: perplexity-based detection (DetectGPT, GLTR, DNA-GPT, Binoculars), model collapse theory, OOD detection, data quality scoring, watermarking, vocabulary diversity, stylometry/authorship attribution, iterative generation (LLM as Broken Telephone ACL 2025), membership inference.\n\n## Venue Fit\n- EMNLP 2026 Findings: Excellent fit — directly addresses data contamination, synthetic data feedback loops, data governance. Empirical/conceptual contribution with honest scope boundaries. Findings-appropriate ambition level: novel task formulation + solid characterization, not a state-of-the-art methodology claim.\n",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  },
  "sourceToolAssistantUUID": "b6015340-97d5-40a5-b677-162736805e62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "ef7d0931-a681-4d6a-a2f2-62db39bbf1ea",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from dream data",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Tool result

_source line 13 · 2026-05-20T10:27:37.395Z_

<details><summary>↩ Tool result · `toolu_01Y9JLQky3h8agbzCku6XhYg`</summary>

```text
1	[
2	  {
3	    "name": "feature_ablation_and_trend",
4	    "description": "三部分分析：(A) Feature ablation — full vs reference-only vs surface-only； (B) DDR trend analysis — 每个 feature 的 depth-wise 趋势 + Spearman ρ； (C) Perplexity pre-validation for Claim 3\n",
5	    "results": {
6	      "full_macro_f1": 0.82,
7	      "reference_only_f1": 0.719,
8	      "surface_only_f1": 0.763,
9	      "ref_vs_surf_bootstrap_ci": "[0.706, 0.733] vs [0.747, 0.774]",
10	      "drifting_features": "entropy_mean (ρ≈−0.60), TTR (ρ≈−0.61), hapax_ratio (ρ≈−0.63)",
11	      "stationary_features": "tail_decay (ρ≈0.04), entropy_std (ρ≈−0.12), entropy_max (ρ≈0.05)",
12	      "median_ppl_by_depth": "13.50 → 4.96 → 3.00 → 2.07 → 1.72",
13	      "ppl_depth_monotonic": true
14	    },
15	    "tables": [
16	      {
17	        "caption": "Table 2: Feature ablation results (5-fold CV, Pythia-2.8B)",
18	        "columns": [
19	          "Feature Set",
20	          "N Features",
21	          "Macro F1",
22	          "95% CI"
23	        ],
24	        "rows": [
25	          [
26	            "Full",
27	            7,
28	            0.82,
29	            "[0.807, 0.833]"
30	          ],
31	          [
32	            "Surface-only",
33	            2,
34	            0.763,
35	            "[0.747, 0.774]"
36	          ],
37	          [
38	            "Reference-only",
39	            5,
40	            0.719,
41	            "[0.706, 0.733]"
42	          ]
43	        ]
44	      },
45	      {
46	        "caption": "Table 3: Feature-depth Spearman correlations",
47	        "columns": [
48	          "Feature",
49	          "ρ",
50	          "Category",
51	          "Trend"
52	        ],
53	        "rows": [
54	          [
55	            "hapax_ratio",
56	            "−0.63",
57	            "Drifting",
58	            "Monotonic decrease"
59	          ],
60	          [
61	            "TTR",
62	            "−0.61",
63	            "Drifting",
64	            "Monotonic decrease"
65	          ],
66	          [
67	            "entropy_mean",
68	            "−0.60",
69	            "Drifting",
70	            "Monotonic decrease"
71	          ],
72	          [
73	            "entropy_min",
74	            "−0.39",
75	            "Intermediate",
76	            "Moderate decrease"
77	          ],
78	          [
79	            "entropy_std",
80	            "−0.12",
81	            "Stationary",
82	            "Near-flat"
83	          ],
84	          [
85	            "entropy_max",
86	            0.05,
87	            "Stationary",
88	            "Near-flat"
89	          ],
90	          [
91	            "tail_decay",
92	            0.04,
93	            "Stationary",
94	            "Near-flat"
95	          ]
96	        ]
97	      }
98	    ],
99	    "figures": [],
100	    "analysis": "Full > Surface > Reference 的排序表明 surface 特征（TTR, hapax）捕获了最强的单维信号， 但 reference 特征提供了不可替代的互补信息。Surface-only 虽然绝对值更高，但 reference-only 在 binary task（gen-1 vs gen-2+）上表现更优（binary F1=0.833 vs 0.695），这是因为 reference 特征在排除 gen-0 后捕获了更 fine-grained 的 NLL 分布位移。 DDR 分离的物理解释：递归生成诱导 NLL 分布的 location shift，central-tendency 指标（mean, TTR, hapax）跟踪这一 shift 因而漂移，shape 指标（max, tail_decay）反映分布形态因而稳定。\n\n\n在 best 档下，full 7-feature 以 0.820 显著高于两个 subset（McNemar p≈0）， surface-only 以 0.763 高于 reference-only 0.719，但两者都显著低于 full， 证明互补性而非冗余性。审稿人接受这一 4.4 pp gap 作为 complementarity 证据。 DDR 趋势清晰：drifting 三特征 |ρ|>0.60 呈单调下降，shape 特征 |ρ|<0.12 近乎水平。Perplexity 随 depth 单调下降（13.50→1.72）预验证 Claim 3 信号存在。 这组结果为后续所有实验奠定特征空间基础。\n"
101	  },
102	  {
103	    "name": "cross_generator_evaluation",
104	    "description": "扩展至 5 generators（Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）， LOGO 交叉验证评估跨生成器泛化性\n",
105	    "results": {
106	      "total_records": 18423,
107	      "generators": 5,
108	      "logo_avg_macro_f1": 0.804,
109	      "logo_best_held_out": {
110	        "model": "pythia-1b",
111	        "f1": 0.851
112	      },
113	      "logo_worst_held_out": {
114	        "model": "olmo-2-1b",
115	        "f1": 0.752
116	      },
117	      "lofo_delta": 0.011,
118	      "ablation_full_f1": 0.804,
119	      "ablation_reference_only_f1": 0.754,
120	      "ablation_surface_only_f1": 0.747,
121	      "mcnemar_p": 0.0,
122	      "top3_features": [
123	        "hapax_ratio (0.289)",
124	        "ttr (0.168)",
125	        "entropy_mean (0.160)"
126	      ]
127	    },
128	    "tables": [
129	      {
130	        "caption": "Table 4: LOGO cross-generator evaluation",
131	        "columns": [
132	          "Held-out Generator",
133	          "Macro F1",
134	          "Binary F1",
135	          "Gen-1 F1"
136	        ],
137	        "rows": [
138	          [
139	            "Pythia-1B",
140	            0.851,
141	            0.724,
142	            0.689
143	          ],
144	          [
145	            "Qwen3-0.6B",
146	            0.824,
147	            0.71,
148	            0.652
149	          ],
150	          [
151	            "Qwen3-1.7B",
152	            0.805,
153	            0.698,
154	            0.641
155	          ],
156	          [
157	            "Pythia-2.8B",
158	            0.804,
159	            0.694,
160	            0.638
161	          ],
162	          [
163	            "OLMo-2-1B",
164	            0.752,
165	            0.663,
166	            0.585
167	          ],
168	          [
169	            "Average",
170	            0.804,
171	            0.694,
172	            0.641
173	          ]
174	        ]
175	      }
176	    ],
177	    "figures": [],
178	    "analysis": "5-gen LOGO 为后续 8-gen/9-gen 扩展奠定基线。OLMo 的相对弱势来自其 tokenizer 和 训练数据分布与 Pythia/Qwen 的差异——这本身验证了 DDR 在不同预训练配方下的鲁棒性（仍 >0.75）。 LOFO delta 仅 0.011 说明 Pythia 家族重叠未严重膨胀 LOGO 指标。\n\n\n在 best 档下，5-gen LOGO 均值 0.804 显示强跨生成器泛化。Pythia-1B held-out 最高（0.851） 因为 Pythia-2.8B 在训练集中提供了同家族信号；OLMo held-out 最低（0.752）因为 OLMo 的生成分布与 Pythia/Qwen 家族差异最大。Family-out delta 仅 0.011 pp，审稿人接受为 cross-family generalization 证据。Feature importance 排序（hapax > ttr > entropy_mean） 与 plan_001 一致，确认 surface drifting 特征是主驱动力，但 McNemar p≈0 证明 reference 特征对 full 集的贡献统计显著。\n"
179	  },
180	  {
181	    "name": "cross_family_reference_model",
182	    "description": "测试非 Pythia reference model（OLMo-2-1B, Qwen3-0.6B）提取特征， 验证 DDR 是否为 generation-intrinsic 而非 reference-model artifact\n",
183	    "results": {
184	      "logo_f1_pythia_ref": 0.803,
185	      "logo_f1_olmo_ref": 0.807,
186	      "logo_f1_qwen_ref": 0.816,
187	      "entropy_drift_all_refs_negative": true,
188	      "pythia_ref_drift_range": "[−1.19, −1.40]",
189	      "olmo_ref_drift_range": "[−0.61, −0.91]",
190	      "qwen_ref_drift_range": "[−0.96, −1.35]",
191	      "dual_dynamics_is_pythia_artifact": false
192	    },
193	    "tables": [
194	      {
195	        "caption": "Table 5: Cross-reference-model DDR validation",
196	        "columns": [
197	          "Reference Model",
198	          "LOGO F1",
199	          "entropy_mean drift range",
200	          "DDR preserved"
201	        ],
202	        "rows": [
203	          [
204	            "Pythia-410M (default)",
205	            0.803,
206	            "[−1.19, −1.40]",
207	            "✓"
208	          ],
209	          [
210	            "OLMo-2-1B",
211	            0.807,
212	            "[−0.61, −0.91]",
213	            "✓"
214	          ],
215	          [
216	            "Qwen3-0.6B",
217	            0.816,
218	            "[−0.96, −1.35]",
219	            "✓"
220	          ]
221	        ]
222	      }
223	    ],
224	    "figures": [],
225	    "analysis": "漂移幅度的差异（Pythia > Qwen > OLMo）反映了 reference model 自身 perplexity scale 的差异， 但方向一致性是关键。这排除了 \"DDR 只是 Pythia tokenizer 的 artifact\" 这一最致命的替代解释。\n\n\n在 best 档下，三个 reference model 均产生负向 entropy drift（所有 range 为负）， LOGO F1 跨 reference 差异 <1.5 pp（0.803–0.816），关键性地证明 DDR 是 generation-intrinsic 现象而非 Pythia-410M 特有 artifact。Qwen reference 略优 可能因其 tokenizer 粒度更细，捕获了更丰富的 NLL 分布信息。这是 Claim 2 的核心 falsification test 通过：如果 DDR 消失于非 Pythia reference，整个 dual dynamics 叙事将崩塌。审稿人在 best 档下接受这一 3-reference 交叉验证为充分证据。\n"
226	  },
227	  {
228	    "name": "downstream_utility",
229	    "description": "OLMo-1B fine-tune on depth-stratified subsets，3 seeds with bootstrap CIs， sample-count-matched comparison。验证 Claim 3（negative finding）。\n",
230	    "results": {
231	      "total_runs": 15,
232	      "variants": {
233	        "all": {
234	          "ppl_mean": 2.335,
235	          "ppl_std": 0.0003
236	        },
237	        "size_matched": {
238	          "ppl_mean": 2.367,
239	          "ppl_std": 0.0002
240	        },
241	        "depth01": {
242	          "ppl_mean": 2.387,
243	          "ppl_std": 0.0005
244	        },
245	        "binary_filtered": {
246	          "ppl_mean": 2.389,
247	          "ppl_std": 0.0004
248	        },
249	        "depth0_only": {
250	          "ppl_mean": 2.681,
251	          "ppl_std": 0.0012
252	        }
253	      },
254	      "ranking": "all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)",
255	      "tost_equivalence_p": 0.00011,
256	      "tost_margin": "±2%",
257	      "seed_variance": "<0.002 ppl across seeds within same variant",
258	      "cohens_d_sizeMatched_vs_depth01": "inflated by low variance"
259	    },
260	    "tables": [
261	      {
262	        "caption": "Table 7: Downstream CLM perplexity by training data composition (3 seeds)",
263	        "columns": [
264	          "Variant",
265	          "N train",
266	          "Ppl (mean±std)",
267	          "Δ vs size_matched"
268	        ],
269	        "rows": [
270	          [
271	            "All data",
272	            12299,
273	            "2.335 ± 0.0003",
274	            "−0.032"
275	          ],
276	          [
277	            "Size-matched random",
278	            3951,
279	            "2.367 ± 0.0002",
280	            "— (baseline)"
281	          ],
282	          [
283	            "Depth 0+1 only",
284	            3951,
285	            "2.387 ± 0.0005",
286	            0.02
287	          ],
288	          [
289	            "Binary-filtered",
290	            3951,
291	            "2.389 ± 0.0004",
292	            0.022
293	          ],
294	          [
295	            "Depth 0 only",
296	            797,
297	            "2.681 ± 0.0012",
298	            0.314
299	          ]
300	        ]
301	      }
302	    ],
303	    "figures": [],
304	    "analysis": "Negative finding 的关键价值在于终止了一个看似合理但无效的研究方向：既然 depth 信息存在且可检测， 自然会假设可用于数据筛选。实验证明这一假设不成立。More data > better data 在 3951 samples 的低数据量下尤为明显。TOST equivalence 而非 NHST 是正确的统计框架选择。\n\n\n在 best 档下，negative finding 清晰：depth-aware filtering 不优于 random subsampling（size_matched 2.367 vs depth01 2.387，差 0.020 ppl）。TOST 在 ±2% margin 下 p=1.1×10⁻⁴ 确认统计等价。 depth0_only 的显著劣势（2.681）是预期的——纯人类文本量太少（797 samples）。关键是 size_matched vs depth01 的差异方向反直觉：random subsample 比 depth-curated 还好 0.020 ppl， 说明 depth 信息对下游 CLM 质量无 curative 价值。审稿人在 best 档下将此认可为 \"valuable honest science\" 而非 \"method doesn't work\"——论文诚实地将 depth fingerprinting 定位为 diagnostic tool（provenance characterization）而非 curative tool（data selection）。 三 seed 极低方差（<0.002）既增强结论可靠性，也意味着 Cohen's d 被人为放大，论文正确选择 TOST 而非 effect size 作为主检验。\n"
305	  },
306	  {
307	    "name": "prompt_type_comparison",
308	    "description": "比较 continuation / elaboration / inspired_rewriting 三种 prompt type 的 depth signal\n",
309	    "results": {
310	      "cv_f1": {
311	        "continuation": 0.781,
312	        "inspired_rewriting": 0.737,
313	        "elaboration": 0.73
314	      },
315	      "lopto_f1": {
316	        "held_out_continuation": 0.762,
317	        "held_out_elaboration": 0.762,
318	        "held_out_rewriting": 0.733,
319	        "average": 0.753
320	      },
321	      "depth_retention_d4_d0": {
322	        "continuation": 0.831,
323	        "inspired_rewriting": 0.939,
324	        "elaboration": 0.986
325	      },
326	      "drift_hapax": {
327	        "continuation": "−0.74",
328	        "elaboration": "−0.83",
329	        "rewriting": "−0.80"
330	      },
331	      "drift_ttr": {
332	        "continuation": "−0.607",
333	        "elaboration": "−0.641",
334	        "rewriting": "−0.618"
335	      }
336	    },
337	    "tables": [
338	      {
339	        "caption": "Table 8: Prompt-type comparison (Pythia-2.8B)",
340	        "columns": [
341	          "Prompt Type",
342	          "CV F1",
343	          "LOPTO F1",
344	          "Depth Retention",
345	          "hapax ρ"
346	        ],
347	        "rows": [
348	          [
349	            "Continuation",
350	            0.781,
351	            0.762,
352	            0.831,
353	            "−0.74"
354	          ],
355	          [
356	            "Inspired rewriting",
357	            0.737,
358	            0.733,
359	            0.939,
360	            "−0.80"
361	          ],
362	          [
363	            "Elaboration",
364	            0.73,
365	            0.762,
366	            0.986,
367	            "−0.83"
368	          ]
369	        ]
370	      }
371	    ],
372	    "figures": [],
373	    "analysis": "Prompt-type 差异本身是有趣发现：语义约束越强（elaboration > rewriting > continuation）， chain 越稳定但 depth discriminability 越低。这与 DDR 的 location-shift 解释一致—— 约束越强，模型输出分布被锚定在更窄的范围内，location shift 幅度减小。\n\n\n在 best 档下，三种 prompt type 均保留 DDR 信号但强度不同。Continuation 的 within-type CV F1 最高（0.781）但 depth retention 最低（83.1%），因为 continuation 给予模型最大自由度， 导致更多 chain dropout 但也产生更强的 distributional shift。Elaboration retention 最高 （98.6%）但 CV F1 最低（0.730），因为 elaboration 约束模型围绕原文展开，压缩了 cross-depth 变异。Rewriting 居中。Leave-one-prompt-type-out 交叉验证（avg 0.753） 低于 within-type（avg 0.749）仅 ~0.4 pp，表明 prompt type 间的 DDR 信号高度可迁移。 审稿人接受 prompt-type dependence 的透明报告为 ecological validity 证据。\n"
374	  },
375	  {
376	    "name": "paraphrastic_comparison",
377	    "description": "构建平行 paraphrasing chains 与 continuation chains 直接比较， 测试 attractor convergence theory\n",
378	    "results": {
379	      "paraphrase_cv_f1": 0.62,
380	      "continuation_cv_f1": 0.781,
381	      "paraphrase_depth_retention": 0.97,
382	      "paraphrase_hapax_rho": "−0.25",
383	      "paraphrase_entropy_mean_rho": "−0.18",
384	      "attractor_convergence_depth": 2,
385	      "delta_cv_f1": "−0.161"
386	    },
387	    "tables": [
388	      {
389	        "caption": "Table 9: Paraphrastic vs non-paraphrastic chains",
390	        "columns": [
391	          "Chain Type",
392	          "CV F1",
393	          "hapax ρ",
394	          "entropy_mean ρ",
395	          "Retention d4/d0"
396	        ],
397	        "rows": [
398	          [
399	            "Continuation",
400	            0.781,
401	            "−0.74",
402	            "−0.56",
403	            0.831
404	          ],
405	          [
406	            "Paraphrasing",
407	            0.62,
408	            "−0.25",
409	            "−0.18",
410	            0.97
411	          ],
412	          [
413	            "Δ",
414	            "−0.161",
415	            0.49,
416	            0.38,
417	            0.139
418	          ]
419	        ]
420	      }
421	    ],
422	    "figures": [],
423	    "analysis": "这是论文与 ACL 2025 attractor cycle 理论的关键联系点。Non-paraphrastic chains 不受 semantic-preservation attractor 约束，因此 distributional drift 可以持续到更深层， 为 depth estimation 提供更丰富的信号空间。\n\n\n在 best 档下，paraphrasing chains 的 depth signal 显著弱于 continuation（CV F1 0.62 vs 0.781，−16.1 pp）。Paraphrasing 由于语义保持约束，每步输出被 attractor basin 拉回， depth 间差异在 depth 2 后趋于收敛（与 ACL 2025 \"LLM as Broken Telephone\" 的 ~3 class ceiling 一致）。DDR drifting 特征在 paraphrase 中 ρ 幅度大幅缩小（hapax −0.25 vs −0.63）， 因为 paraphrase 保持语义→保持词汇多样性→TTR/hapax drift 被抑制。这验证了论文核心定位： DDR 是 non-paraphrastic chain 特有的现象，paraphrastic chain 走向 attractor convergence。 审稿人在 best 档下接受这一对比作为 task formulation 的 motivation——深度估计在 continuation/elaboration chain 中才有 meaningful signal。\n"
424	  },
425	  {
426	    "name": "cross_model_chains",
427	    "description": "Cross-model chains（每步使用不同 generator）vs single-model chains， 模拟真实 web contamination 场景\n",
428	    "results": {
429	      "cross_model_binary_f1": 0.83,
430	      "cross_model_3class_f1": 0.789,
431	      "single_model_binary_f1": 0.694,
432	      "single_model_3class_f1": 0.762,
433	      "cross_model_logo_binary": 0.83,
434	      "delta_binary_vs_single": 0.136,
435	      "n_generators_in_cross": 5
436	    },
437	    "tables": [
438	      {
439	        "caption": "Table 6: Cross-model vs single-model chain evaluation",
440	        "columns": [
441	          "Setting",
442	          "Binary F1",
443	          "3-class F1",
444	          "N Generators"
445	        ],
446	        "rows": [
447	          [
448	            "Single-model LOGO",
449	            0.694,
450	            0.762,
451	            "8 (homogeneous)"
452	          ],
453	          [
454	            "Cross-model LOGO",
455	            0.83,
456	            0.789,
457	            "5 (heterogeneous)"
458	          ],
459	          [
460	            "Δ",
461	            0.136,
462	            0.027,
463	            "—"
464	          ]
465	        ]
466	      }
467	    ],
468	    "figures": [],
469	    "analysis": "Cross-model 的优势来自 generator heterogeneity amplifying distributional shifts。 在单模型 chain 中，depth-wise drift 是同一模型 bias 的累积；在 cross-model chain 中， 每步引入新模型 bias，产生更大的 inter-depth 特征差异。这是 ecological validity 的 正面证据：真实世界的 contamination 更可能涉及多个 generator。\n\n\n在 best 档下，cross-model chains 的 binary F1 0.830 显著高于 single-model 0.694 （+13.6 pp），这一 counterintuitive 结果的原因是：不同 generator 在每步引入额外的 distributional discontinuity（不同 tokenizer bias, 不同 perplexity scale）， 放大了 depth 间的特征差异。这对审稿人而言是 strength——说明在更 realistic 的 heterogeneous contamination 场景下，depth signal 反而更强。0.830 cross-model binary F1 被 highlight 为 generalization evidence，审稿人接受 5-gen subset LOGO 作为评估方法。 3-class F1 同样提升（0.789 vs 0.762），但提升幅度小于 binary，因为 gen-0 identification 的 seed-sharing advantage 在两种设定下相当。\n"
470	  },
471	  {
472	    "name": "multi_domain_seeds",
473	    "description": "扩展至 4 domains（Wikipedia, news, scientific, creative/code）， 500 seeds/domain × 5 depths\n",
474	    "results": {
475	      "news_binary_f1": 0.746,
476	      "news_binary_ci": [
477	        0.726,
478	        0.764
479	      ],
480	      "academic_binary_f1": 0.739,
481	      "academic_binary_ci": [
482	        0.72,
483	        0.757
484	      ],
485	      "code_binary_f1": 0.754,
486	      "code_binary_ci": [
487	        0.737,
488	        0.77
489	      ],
490	      "wikipedia_baseline_binary_f1": 0.815,
491	      "max_gap_vs_wiki_pp": 7.62,
492	      "worst_domain": "academic",
493	      "best_domain": "code",
494	      "conclusion_label": "domain_independent"
495	    },
496	    "tables": [
497	      {
498	        "caption": "Table 10: Multi-domain evaluation",
499	        "columns": [
500	          "Domain",
501	          "Binary F1",
502	          "95% CI",
503	          "3-class F1"
504	        ],
505	        "rows": [
506	          [
507	            "Wikipedia (baseline)",
508	            0.815,
509	            "[0.799, 0.831]",
510	            0.863
511	          ],
512	          [
513	            "Code",
514	            0.754,
515	            "[0.737, 0.770]",
516	            0.634
517	          ],
518	          [
519	            "News",
520	            0.746,
521	            "[0.726, 0.764]",
522	            0.652
523	          ],
524	          [
525	            "Academic",
526	            0.739,
527	            "[0.720, 0.757]",
528	            0.622
529	          ]
530	        ]
531	      }
532	    ],
533	    "figures": [],
534	    "analysis": "Multi-domain 结果直接回应 RC6（ecological validity）。DDR 在 news/academic/code 上的 一致性说明 depth signal 不依赖于特定文本类型的 vocabulary 特征。3-class F1 的 domain 差异更大（0.622–0.863），因为 gen-0 vs gen-1 区分依赖 seed-specific 线索，这在 不同 domain 中差异更大。\n\n\n在 best 档下，所有 domain 的 binary F1 均在 0.739–0.754 范围内（排除 Wikipedia 基线）， domain 间 max gap 仅 1.5 pp，审稿人接受 DDR 为 domain-independent 现象。Wikipedia 基线（0.815）高出 ~7 pp 是预期的——Wikipedia 种子文本结构化程度更高、长度更稳定， 减少了 confounding variation。Academic domain 最低（0.739）因为学术文本的词汇多样性 本身就高且 depth 间变化小（base model 生成学术文本时更依赖 template phrasing）。 Code domain 意外地最高（0.754），因为 code-like 文本的 entropy 分布更 bimodal， DDR drifting 在 entropy_mean 上更明显。所有 CI 均不包含 0.5（random baseline）， 确认 depth signal 在所有 domain 中统计显著。\n"
535	  },
536	  {
537	    "name": "finer_grained_ordinal",
538	    "description": "5-class 序数分类（gen-0 至 gen-4），测试更细粒度 depth resolution 的可行性\n",
539	    "results": {
540	      "five_class_f1": 0.5,
541	      "three_class_f1_reference": 0.762,
542	      "ordinal_coral_f1": 0.49,
543	      "ordinal_frank_hall_f1": 0.5,
544	      "xgboost_standard_f1": 0.5,
545	      "bottleneck": "gen-1/gen-2 boundary, 86% binary FNs concentrated here",
546	      "gen3_vs_gen4_f1": 0.35
547	    },
548	    "tables": [
549	      {
550	        "caption": "Table A.3: Ordinal classification results",
551	        "columns": [
552	          "Method",
553	          "3-class F1",
554	          "5-class F1",
555	          "Δ"
556	        ],
557	        "rows": [
558	          [
559	            "XGBoost (standard)",
560	            0.762,
561	            0.5,
562	            "−0.262"
563	          ],
564	          [
565	            "CORAL",
566	            0.758,
567	            0.49,
568	            "−0.268"
569	          ],
570	          [
571	            "Frank-Hall",
572	            0.76,
573	            0.5,
574	            "−0.260"
575	          ]
576	        ]
577	      }
578	    ],
579	    "figures": [],
580	    "analysis": "5-class 的 ceiling 与 DDR 的物理解释一致：location shift 在前几步（0→1→2）幅度最大， 之后递减。Gen-3 和 gen-4 的 NLL 分布差异已小于 feature extraction noise floor。\n\n\n在 best 档下，5-class F1 降至 ~0.50，相比 3-class 的 0.762 大幅下降。Ordinal methods （CORAL, Frank-Hall）未能改善——这说明 depth signal 的 resolution ceiling 在 3 class， 不是分类方法的选择问题而是 feature space 的固有限制。Gen-1/gen-2 boundary 贡献了 86% 的 binary errors（作为 FN），因为 gen-1 和 gen-2 在 feature space 中高度重叠。 Gen-3 vs gen-4 几乎不可分（F1≈0.35）。审稿人在 best 档下接受 3-class 为 practical ceiling，论文诚实报告这一限制为 strength。5-class 负面结果排除了 \"只要用更好方法就能 区分更多 depth\" 的替代假说。\n"
581	  },
582	  {
583	    "name": "human_edit_robustness",
584	    "description": "鲁棒性测试：(A) Random word replacement (5/10/20%)，(B) LLM-simulated editing\n",
585	    "results": {
586	      "baseline_binary_f1": 0.695,
587	      "random_5pct_f1": 0.65,
588	      "random_10pct_f1": 0.614,
589	      "random_20pct_f1": 0.591,
590	      "llm_rephrase_binary_f1": 0.647,
591	      "llm_rephrase_multiclass_f1": 0.667,
592	      "llm_edit_distance_ratio": 0.507,
593	      "llm_avg_sentences_replaced": 1.69,
594	      "drop_5pct": "−0.046",
595	      "drop_10pct": "−0.081",
596	      "drop_20pct": "−0.104",
597	      "drop_llm": "−0.045"
598	    },
599	    "tables": [
600	      {
601	        "caption": "Table A.5: Robustness to text editing",
602	        "columns": [
603	          "Condition",
604	          "Binary F1",
605	          "Δ vs baseline"
606	        ],
607	        "rows": [
608	          [
609	            "No editing (baseline)",
610	            0.695,
611	            "—"
612	          ],
613	          [
614	            "5% random replacement",
615	            0.65,
616	            "−0.046"
617	          ],
618	          [
619	            "10% random replacement",
620	            0.614,
621	            "−0.081"
622	          ],
623	          [
624	            "20% random replacement",
625	            0.591,
626	            "−0.104"
627	          ],
628	          [
629	            "LLM rephrase (avg 1.69 sent)",
630	            0.647,
631	            "−0.045"
632	          ]
633	        ]
634	      }
635	    ],
636	    "figures": [],
637	    "analysis": "LLM rephrase 与 5% random 的 drop 相近这一发现本身有价值：LLM editing 的特征空间扰动 并不比 naive random replacement 更具破坏性，可能因为 LLM editing 保持了文本的局部统计 一致性（不引入 out-of-distribution tokens）。\n\n\n在 best 档下，depth signal 对 human editing 展现 graceful degradation。5% random noise 仅降 4.6 pp，LLM rephrase（平均替换 1.69 句，编辑距离 50.7%）降 4.5 pp——两者接近， 因为 LLM rephrase 虽然更自然但实际修改幅度（50.7% edit distance）与 5% random 在 feature 空间的扰动量级相当。20% random 的 10.4 pp drop 仍保持 F1>0.59（>random baseline）， 说明 depth signal 不完全依赖逐字保真。审稿人在 best 档下将 graceful degradation 视为 positive——完全抵抗 editing 是不现实的，important 是 degradation curve 平滑且 在 realistic editing level（5–10%）下性能损失可控。LLM rephrase 结果直接回应 RC5。\n"
638	  },
639	  {
640	    "name": "ld_score_feature",
641	    "description": "添加 LD-Score（character-level distributional signature）作为额外特征\n",
642	    "results": {
643	      "seven_feature_f1": 0.798,
644	      "eight_feature_with_ld_f1": 0.803,
645	      "ld_score_only_f1": 0.721,
646	      "ld_score_spearman_depth": "−0.794",
647	      "delta_with_ld": 0.005,
648	      "ld_feature_importance_rank": 4
649	    },
650	    "tables": [
651	      {
652	        "caption": "Table A.6: LD-Score augmentation",
653	        "columns": [
654	          "Feature Set",
655	          "LOGO F1",
656	          "Δ"
657	        ],
658	        "rows": [
659	          [
660	            "7-feature (default)",
661	            0.798,
662	            "—"
663	          ],
664	          [
665	            "7-feature + LD-Score",
666	            0.803,
667	            0.005
668	          ],
669	          [
670	            "LD-Score only",
671	            0.721,
672	            "−0.077"
673	          ]
674	        ]
675	      }
676	    ],
677	    "figures": [],
678	    "analysis": "LD-Score 的 marginal contribution 较小（+0.5 pp），确认 7-feature set 已捕获大部分 depth signal。Character-level 信息主要通过 character frequency distribution 的 shift 反映 vocabulary impoverishment，与 TTR/hapax 高度相关。\n\n\n在 best 档下，LD-Score 作为 character-level 特征与 token-level reference 特征部分互补， 加入后 LOGO F1 提升 0.5 pp（0.798→0.803），统计上显著但 practical 提升有限。 LD-Score 单独的 F1=0.721 介于 surface-only（0.688）和 reference-only（0.713）之间， Spearman ρ=−0.794 表明其与 depth 有强负相关。Feature importance 排第 4（在 hapax, ttr, entropy_mean 之后），说明 LD-Score 捕获的信号与 reference 特征高度 correlated 但非完全冗余。审稿人在 best 档下接受将 LD-Score 作为 supplementary evidence， 论文在 appendix 中报告此结果。7-feature 仍为 primary model 以保持简洁性。\n"
679	  },
680	  {
681	    "name": "end_to_end_classifier",
682	    "description": "QLoRA fine-tuned model 进行端到端 depth classification， 比较 learned representations vs handcrafted features\n",
683	    "results": {
684	      "qlora_olmo_instruct_3class_f1": 0.888,
685	      "qlora_qwen_instruct_3class_f1": 0.907,
686	      "qlora_olmo_base_3class_f1": 0.859,
687	      "qlora_qwen_base_3class_f1": 0.904,
688	      "qlora_olmo_instruct_binary_f1": 0.836,
689	      "qlora_qwen_instruct_binary_f1": 0.867,
690	      "qlora_olmo_base_binary_f1": 0.793,
691	      "qlora_qwen_base_binary_f1": 0.86,
692	      "qlora_5class_best_f1": 0.597,
693	      "seven_feature_3class_f1": 0.762,
694	      "delta_3class": "+12.6–14.5 pp",
695	      "inference_cost_ratio": "~15×"
696	    },
697	    "tables": [
698	      {
699	        "caption": "Table A.7: End-to-end QLoRA vs 7-feature ensemble",
700	        "columns": [
701	          "Model",
702	          "Type",
703	          "3-class F1",
704	          "Binary F1",
705	          "5-class F1"
706	        ],
707	        "rows": [
708	          [
709	            "Qwen3-1.7B (instruct)",
710	            "QLoRA",
711	            0.907,
712	            0.867,
713	            0.551
714	          ],
715	          [
716	            "OLMo-1B (instruct)",
717	            "QLoRA",
718	            0.888,
719	            0.836,
720	            0.598
721	          ],
722	          [
723	            "Qwen3-1.7B (base)",
724	            "QLoRA",
725	            0.904,
726	            0.86,
727	            0.554
728	          ],
729	          [
730	            "OLMo-1B (base)",
731	            "QLoRA",
732	            0.859,
733	            0.793,
734	            0.54
735	          ],
736	          [
737	            "7-feature ensemble",
738	            "XGBoost",
739	            0.762,
740	            0.694,
741	            0.5
742	          ]
743	        ]
744	      }
745	    ],
746	    "figures": [],
747	    "analysis": "QLoRA 的成功并不削弱 7-feature 的贡献：(1) 7-feature 提供了可解释的 DDR 框架，QLoRA 是 black box；(2) 7-feature 的 reference model 仅 410M，QLoRA 需 1.7B+；(3) QLoRA 同样 受 5-class ceiling 限制，确认这是 task boundary 而非 method limitation。\n\n\n在 best 档下，QLoRA fine-tuned models 以 3-class F1 0.859–0.907 大幅超越 7-feature ensemble 的 0.762（+10–15 pp），证明 learned representations 能捕获 handcrafted features 遗漏的深层信号。但 5-class F1 仍仅 ~0.60，说明 resolution ceiling 是 task-intrinsic 而非 feature engineering 限制。Binary F1 提升较小（0.793–0.867 vs 0.694）， 因为 binary task 的 bottleneck 在 gen-1/gen-2+ 边界，learned features 也难以完全突破。 Instruct model 意外地与 base model 表现接近甚至略优（OLMo instruct 0.888 vs base 0.859）， 因为 QLoRA 的端到端学习可以 bypass DDR degradation，直接从 raw text 学习 depth pattern。 审稿人在 best 档下接受 7-feature 的定位转换：不追求绝对最优，而是 efficiency advantage（单次 Pythia-410M forward pass vs QLoRA 推理的 ~15× 成本差距）。\n"
748	  },
749	  {
750	    "name": "text_length_control",
751	    "description": "文本长度 confound 控制：分析长度分布、length-normalized features、length-matched evaluation\n",
752	    "results": {
753	      "length_depth_spearman_range": "[−0.066, +0.134]",
754	      "length_is_confound": false,
755	      "normalized_ttr_trend_preserved": true,
756	      "normalized_hapax_trend_preserved": true,
757	      "normalized_rho_stronger": true,
758	      "length_matched_f1": 0.724,
759	      "unmatched_f1": 0.77,
760	      "length_matched_delta": "−0.046",
761	      "dropout_short_text_bias": true
762	    },
763	    "tables": [
764	      {
765	        "caption": "Table A.8: Length confound analysis",
766	        "columns": [
767	          "Condition",
768	          "Binary F1",
769	          "Δ vs unmatched"
770	        ],
771	        "rows": [
772	          [
773	            "Unmatched (full)",
774	            0.77,
775	            "—"
776	          ],
777	          [
778	            "Length-matched",
779	            0.724,
780	            "−0.046"
781	          ],
782	          [
783	            "Random subsample control",
784	            0.724,
785	            "−0.046"
786	          ]
787	        ]
788	      }
789	    ],
790	    "figures": [],
791	    "analysis": "Length confound 是 reviewer 高频关注点（RC10）。−4.6 pp drop 的来源是 deconfounding 而非信息损失，这通过 random subsample control 证实。Length-matched F1=0.724 可作为 conservative lower bound 报告在 abstract 中。\n\n\n在 best 档下，text length 与 depth 的 Spearman ρ 在 [−0.066, +0.134] 范围内（弱相关）， 排除 length 作为主要 confound。Length-normalized features（TTR, hapax 在 fixed-length window 上计算）保持甚至增强了 depth 趋势（normalized ρ stronger），说明 DDR drift 不是 length artifact。Length-matched 后 F1 从 0.770 降至 0.724（−4.6 pp），但对照实验确认 这一 drop 来自 deconfounding 而非 sample size reduction（random subsample control 也降 相同幅度）。Depth 增加→更多短文本 dropout 的 bias 被确认，但通过 length matching 控制后 signal 仍然显著（0.724 >> 0.5）。审稿人在 best 档下接受 length-matched 0.724 作为 conservative 的 deconfounded 估计。\n"
792	  },
793	  {
794	    "name": "large_scale_generator",
795	    "description": "添加 7B+ generator（Qwen3-8B-Base）测试 frontier scale 下的 depth signal\n",
796	    "results": {
797	      "total_records": 4497,
798	      "unique_seeds": 995,
799	      "depth_dist": {
800	        "0": 995,
801	        "1": 979,
802	        "2": 937,
803	        "3": 831,
804	        "4": 755
805	      },
806	      "logo_6gen_avg_f1": 0.789,
807	      "qwen3_8b_held_out_f1": 0.683,
808	      "logo_5gen_baseline_f1": 0.8,
809	      "spearman_hapax": "−0.558",
810	      "spearman_ttr": "−0.542",
811	      "spearman_entropy_mean": "−0.475",
812	      "spearman_tail_decay": "−0.089",
813	      "feature_importance_top3": [
814	        "hapax_ratio (0.269)",
815	        "entropy_mean (0.164)",
816	        "ttr (0.159)"
817	      ]
818	    },
819	    "tables": [
820	      {
821	        "caption": "Table 11: 6-generator LOGO with Qwen3-8B",
822	        "columns": [
823	          "Generator",
824	          "LOGO F1",
825	          "hapax ρ",
826	          "Scale"
827	        ],
828	        "rows": [
829	          [
830	            "Pythia-1B",
831	            0.856,
832	            "−0.65",
833	            "1.0B"
834	          ],
835	          [
836	            "Qwen3-0.6B",
837	            0.824,
838	            "−0.63",
839	            "0.6B"
840	          ],
841	          [
842	            "Qwen3-1.7B",
843	            0.805,
844	            "−0.61",
845	            "1.7B"
846	          ],
847	          [
848	            "Pythia-2.8B",
849	            0.804,
850	            "−0.63",
851	            "2.8B"
852	          ],
853	          [
854	            "OLMo-2-1B",
855	            0.764,
856	            "−0.60",
857	            "1.5B"
858	          ],
859	          [
860	            "Qwen3-8B",
861	            0.683,
862	            "−0.56",
863	            "8.0B"
864	          ]
865	        ]
866	      }
867	    ],
868	    "figures": [],
869	    "analysis": "Scale degradation 是最重要的 scope limitation 之一。6-gen LOGO 加入 8B 后均值从 0.800 降至 0.789，Qwen3-8B 拉低了整体。但 DDR pattern（drifting vs stationary）在 8B 下完全 保持，说明这是 amplitude reduction 而非 qualitative change。Feature importance 排序 不变（hapax > entropy_mean > ttr），confirmed DDR 的 cross-scale robustness。\n\n\n在 best 档下，Qwen3-8B held-out F1=0.683 低于 6-gen 平均 0.789（−10.6 pp）， 证实 larger models 产生更弱的 depth signal。物理解释：8B 模型的更高容量压缩了 depth-wise feature margins——更强的 language model 在每步生成中保持了更接近 source distribution 的输出，DDR location shift 幅度减小。但 0.683 仍显著高于 random（0.5）， 且 DDR 方向一致（hapax ρ=−0.558, tail_decay ρ=−0.089 仍为 stationary）。 审稿人在 best 档下接受 scale effect 作为 honest limitation with analysis， 而非 fatal flaw——0.683 在 8B scale 下仍为 non-trivial signal。Depth retention 从 d0 到 d4 降至 0.759（995→755），高 dropout 率部分解释了 F1 下降。\n"
870	  },
871	  {
872	    "name": "ordinal_baseline_comparison",
873	    "description": "关键 baseline：测试现有 detector（FastDetectGPT, Binoculars, LD-Score）的连续分数 是否已提供 ordinal depth signal\n",
874	    "results": {
875	      "seven_feature_logo_f1": 0.798,
876	      "seven_feature_ci": [
877	        0.786,
878	        0.799
879	      ],
880	      "avg_logprob_logo_f1": 0.765,
881	      "avg_logprob_ci": [
882	        0.616,
883	        0.82
884	      ],
885	      "ld_score_logo_f1": 0.721,
886	      "ld_score_ci": [
887	        0.588,
888	        0.77
889	      ],
890	      "fast_detect_gpt_logo_f1": 0.627,
891	      "fast_detect_gpt_ci": [
892	        0.511,
893	        0.762
894	      ],
895	      "binoculars_logo_f1": 0.579,
896	      "binoculars_ci": [
897	        0.405,
898	        0.664
899	      ],
900	      "bootstrap_7feat_vs_avglogprob": {
901	        "delta": 0.039,
902	        "p": 0.0,
903	        "significant": true
904	      },
905	      "bootstrap_7feat_vs_fdgpt": {
906	        "delta": 0.067,
907	        "p": 0.0,
908	        "significant": true
909	      },
910	      "best_single_detector": "Avg-LogProb (0.765)",
911	      "seven_feature_advantage_pp": 3.3
912	    },
913	    "tables": [
914	      {
915	        "caption": "Table 5: Ordinal baseline comparison (LOGO)",
916	        "columns": [
917	          "Method",
918	          "LOGO F1",
919	          "95% CI",
920	          "Spearman ρ",
921	          "Δ vs 7-feature"
922	        ],
923	        "rows": [
924	          [
925	            "7-feature ensemble",
926	            0.798,
927	            "[0.786, 0.799]",
928	            "—",
929	            "—"
930	          ],
931	          [
932	            "Avg-LogProb",
933	            0.765,
934	            "[0.616, 0.820]",
935	            0.788,
936	            "−0.033"
937	          ],
938	          [
939	            "LD-Score",
940	            0.721,
941	            "[0.588, 0.770]",
942	            0.794,
943	            "−0.077"
944	          ],
945	          [
946	            "FastDetectGPT",
947	            0.627,
948	            "[0.511, 0.762]",
949	            0.433,
950	            "−0.171"
951	          ],
952	          [
953	            "Binoculars",
954	            0.579,
955	            "[0.405, 0.664]",
956	            0.199,
957	            "−0.219"
958	          ]
959	        ]
960	      }
961	    ],
962	    "figures": [],
963	    "analysis": "这是论文中最关键的 baseline comparison——如果 Avg-LogProb alone 达到 0.80+，7-feature 的 contribution 就会被严重削弱。0.765 vs 0.798 的差距虽小但真实：7-feature 的优势 集中在 cross-generator 泛化（更窄 CI）和 gen-0 discrimination（surface features 必需）。 Binoculars 的 bug fix（denominator 从 CE(performer, obs_argmax) 改为 CE(performer, shifted_ids)）确保了公平比较。\n\n\n在 best 档下，7-feature ensemble（0.798）显著优于所有 single-detector baselines （bootstrap p=0 for all pairwise comparisons）。最强 baseline Avg-LogProb（0.765） 差 3.3 pp，这一差距虽不大但统计显著——关键在于 7-feature 的 CI [0.786, 0.799] 与 Avg-LogProb 的 CI [0.616, 0.820] 不重叠于下界。Avg-LogProb 的强表现说明 ordinal depth signal 部分可被简单的 log-probability 特征捕获（Spearman ρ=0.788），但 7-feature 通过 组合 drifting + stationary 特征实现了更稳定的跨生成器泛化（更窄的 CI）。 FastDetectGPT（0.627）和 Binoculars（0.579）表现较差，因为它们设计为 binary detectors， 连续分数的 ordinal sensitivity 有限。LD-Score（0.721）居中，character-level 信息 提供了中等 ordinal signal。审稿人在 best 档下接受 7-feature 的优势为 \"modest but consistent\"——贡献不在于绝对性能碾压，而在于 DDR 框架的可解释性和互补性。\n"
964	  },
965	  {
966	    "name": "9gen_scale_evaluation",
967	    "description": "扩展至 9 generators（+Gemma-2-2B, Llama-3.2-3B, Mistral-7B-v0.3）， 验证 8→9 gen 的 scaling behavior\n",
968	    "results": {
969	      "9gen_logo_3class_f1": 0.751,
970	      "9gen_logo_binary_f1": 0.666,
971	      "8gen_baseline_3class_f1": 0.77,
972	      "delta_9gen_vs_8gen": "−0.019",
973	      "gemma_held_out_3class_f1": 0.628,
974	      "gemma_held_out_binary_f1": 0.44,
975	      "mistral_held_out_3class_f1": 0.605,
976	      "mistral_held_out_binary_f1": 0.633,
977	      "n_generators": 9,
978	      "n_total_rows": 42015
979	    },
980	    "tables": [
981	      {
982	        "caption": "Table A.9: 9-generator per-generator LOGO F1",
983	        "columns": [
984	          "Generator",
985	          "3-class F1",
986	          "Binary F1",
987	          "Family"
988	        ],
989	        "rows": [
990	          [
991	            "Pythia-1B",
992	            0.857,
993	            0.724,
994	            "Pythia"
995	          ],
996	          [
997	            "Qwen3-0.6B",
998	            0.819,
999	            0.71,
1000	            "Qwen"
1001	          ],
1002	          [
1003	            "Pythia-2.8B",
1004	            0.812,
1005	            0.7,
1006	            "Pythia"
1007	          ],
1008	          [
1009	            "Qwen3-1.7B",
1010	            0.811,
1011	            0.698,
1012	            "Qwen"
1013	          ],
1014	          [
1015	            "OLMo-2-1B",
1016	            0.773,
1017	            0.663,
1018	            "OLMo"
1019	          ],
1020	          [
1021	            "Llama-3.2-3B",
1022	            0.759,
1023	            0.68,
1024	            "Llama"
1025	          ],
1026	          [
1027	            "Qwen3-8B",
1028	            0.696,
1029	            0.647,
1030	            "Qwen"
1031	          ],
1032	          [
1033	            "Gemma-2-2B",
1034	            0.628,
1035	            0.44,
1036	            "Gemma"
1037	          ],
1038	          [
1039	            "Mistral-7B-v0.3",
1040	            0.605,
1041	            0.633,
1042	            "Mistral"
1043	          ]
1044	        ]
1045	      }
1046	    ],
1047	    "figures": [],
1048	    "analysis": "9-gen 是 thoroughness 的体现。Gemma anomaly 提供了 negative case study：当 tokenizer 差异过大时，cross-model reference 特征的假设被违反。这实际上深化了 DDR 的理解—— DDR 依赖于 reference model 与 generator 之间的 tokenizer compatibility。\n\n\n在 best 档下，9-gen LOGO 3-class F1=0.751 较 8-gen 的 0.770 降 1.9 pp，主要由 Gemma-2-2B 的异常表现拉低（gen-1 F1=0.036）。Gemma 的异常来自其独特的 tokenizer （SentencePiece vs BPE）导致 reference model 特征提取偏移。Mistral-7B 的 0.605 反映了 7B scale 的 signal compression（与 plan_014 Qwen3-8B 的 0.696 一致）。 审稿人在 best 档下接受 Gemma anomaly 作为 honest outlier analysis（appendix 中详细 讨论 tokenizer mismatch），8-gen 结果作为 primary metric，9-gen 作为 robustness check。 Binary F1 0.666 是 conservative lower bound——Gemma 的 binary F1=0.440 接近 random。\n"
1049	  },
1050	  {
1051	    "name": "ddr_causality_analysis",
1052	    "description": "DDR causality analysis: permutation importance + Granger causality + feature intervention\n",
1053	    "results": {
1054	      "permutation_baseline_f1": 0.771,
1055	      "drifting_avg_importance": 0.158,
1056	      "stationary_avg_importance": 0.03,
1057	      "drifting_stationary_ratio": 5.31,
1058	      "granger_significant_features": "6/7",
1059	      "granger_nonsig_feature": "entropy_min",
1060	      "granger_max_delta_r2": 0.031,
1061	      "granger_panel_n": 29095,
1062	      "intervention_max_f1_drop": 0.02
1063	    },
1064	    "tables": [
1065	      {
1066	        "caption": "Table 6: DDR causality analysis",
1067	        "columns": [
1068	          "Feature",
1069	          "Perm Importance",
1070	          "Granger sig",
1071	          "Category"
1072	        ],
1073	        "rows": [
1074	          [
1075	            "hapax_ratio",
1076	            0.289,
1077	            "✓ (p<0.001)",
1078	            "Drifting"
1079	          ],
1080	          [
1081	            "ttr",
1082	            0.168,
1083	            "✓ (p<0.001)",
1084	            "Drifting"
1085	          ],
1086	          [
1087	            "entropy_mean",
1088	            0.16,
1089	            "✓ (p<0.001)",
1090	            "Drifting"
1091	          ],
1092	          [
1093	            "entropy_std",
1094	            0.046,
1095	            "✓ (p<0.05)",
1096	            "Stationary"
1097	          ],
1098	          [
1099	            "entropy_max",
1100	            0.063,
1101	            "✓ (p<0.01)",
1102	            "Stationary"
1103	          ],
1104	          [
1105	            "entropy_min",
1106	            0.015,
1107	            "✗ (p=0.12)",
1108	            "Stationary"
1109	          ],
1110	          [
1111	            "tail_decay",
1112	            0.012,
1113	            "✓ (p<0.05)",
1114	            "Stationary"
1115	          ]
1116	        ]
1117	      }
1118	    ],
1119	    "figures": [],
1120	    "analysis": "Causality analysis 是论文从 \"observation\" 升级到 \"empirical contribution\" 的关键。 仅报告 DDR correlation 会被审稿人视为 descriptive；加入 Granger + permutation + intervention 三角验证后，DDR 的 causal status 被充分支撑。entropy_min 的 Granger 不显著实际上增强了可信度——不是所有特征都需要 causal relationship。\n\n\n在 best 档下，drifting/stationary 分离经三重 causality test 验证：(1) Permutation importance 5.3× gap（drifting 0.158 vs stationary 0.030）确认 drifting 特征对分类的 贡献远超 stationary；(2) 6/7 Granger 显著（仅 entropy_min 不显著）确认 depth→feature 的 temporal causality；(3) Feature intervention 的最大 F1 drop 仅 0.020 pp 表明 单特征 intervention 不足以破坏分类——signal 分布在 drifting 特征组合中。 审稿人在 best 档下将这组 causality evidence 视为 \"sufficient\" 而非 \"mere correlation\"， 认可 DDR 作为 genuine empirical contribution 而非 vocabulary impoverishment 的重新包装。 5.5× permutation gap + 6/7 Granger 的组合在 Findings 级别属于 strong evidence。\n"
1121	  },
1122	  {
1123	    "name": "tost_bootstrap_stability",
1124	    "description": "TOST bootstrap 验证 stationary 特征的稳定性\n",
1125	    "results": {
1126	      "n_bootstrap": 1000,
1127	      "margin_d": 0.2,
1128	      "entropy_max": {
1129	        "median_p": 0.0,
1130	        "rejection_rate": 1.0,
1131	        "median_d": 0.062
1132	      },
1133	      "entropy_min": {
1134	        "median_p": 0.0,
1135	        "rejection_rate": 1.0,
1136	        "median_d": "−0.016"
1137	      },
1138	      "tail_decay": {
1139	        "median_p": 0.0,
1140	        "rejection_rate": 1.0,
1141	        "median_d": 0.088
1142	      },
1143	      "entropy_std": {
1144	        "median_p": 1.0,
1145	        "rejection_rate": 0.0,
1146	        "median_d": 0.458
1147	      },
1148	      "stationary_features_robust": true
1149	    },
1150	    "tables": [
1151	      {
1152	        "caption": "Table A.10: TOST bootstrap stationarity test",
1153	        "columns": [
1154	          "Feature",
1155	          "Median d",
1156	          "TOST p",
1157	          "Rejection Rate",
1158	          "Status"
1159	        ],
1160	        "rows": [
1161	          [
1162	            "entropy_max",
1163	            0.062,
1164	            0.0,
1165	            1.0,
1166	            "Stationary ✓"
1167	          ],
1168	          [
1169	            "entropy_min",
1170	            "−0.016",
1171	            0.0,
1172	            1.0,
1173	            "Stationary ✓"
1174	          ],
1175	          [
1176	            "tail_decay",
1177	            0.088,
1178	            0.0,
1179	            1.0,
1180	            "Stationary ✓"
1181	          ],
1182	          [
1183	            "entropy_std",
1184	            0.458,
1185	            1.0,
1186	            0.0,
1187	            "Intermediate (rejected)"
1188	          ]
1189	        ]
1190	      }
1191	    ],
1192	    "figures": [],
1193	    "analysis": "TOST bootstrap 为 DDR 分离提供了比 Spearman ρ 更严格的统计基础。entropy_std 的 intermediate status 实际上加强了论文的 nuance——不是简单的二分法，而是一个连续谱， 论文选择在 practical level 上维持 drifting/stationary 二分以保持 clarity。\n\n\n在 best 档下，TOST bootstrap 确认 3/4 stationary-candidate 特征在 d=0.2 margin 下 统计等价于 depth-invariant（rejection rate=100%, median d<0.1）。entropy_std 被拒绝 （median d=0.458, rejection rate=0%），因为它虽然 Spearman ρ 低（−0.12）但 effect size 超出 equivalence margin——entropy_std 是 \"weak drifter\" 而非 true stationary。 这一发现精细化了 DDR 分类：3 strong drifters (hapax, TTR, entropy_mean) + 3 true stationary (entropy_max, entropy_min, tail_decay) + 1 intermediate (entropy_std)。 审稿人在 best 档下接受 TOST 作为比 ρ 更严格的 stationarity test，entropy_std 的 intermediate status 被视为 nuanced finding 而非 inconsistency。\n"
1194	  },
1195	  {
1196	    "name": "instruct_model_degradation",
1197	    "description": "三个 instruct model（Qwen3-1.7B, OLMo-2-1B, Llama-3.2-3B）的 DDR 退化分析\n",
1198	    "results": {
1199	      "qwen_instruct_logo_binary": 0.658,
1200	      "olmo_instruct_within_3class": 0.575,
1201	      "llama_instruct_3class": 0.544,
1202	      "qwen_base_logo_binary": 0.821,
1203	      "delta_logo_binary_qwen": "−0.163",
1204	      "features_reversed_olmo": "6/7",
1205	      "features_reversed_llama": "3/7 (entropy_mean, entropy_std, tail_decay)",
1206	      "spearman_direction_reversal": true
1207	    },
1208	    "tables": [
1209	      {
1210	        "caption": "Table 12: Instruct vs base model comparison",
1211	        "columns": [
1212	          "Model",
1213	          "Type",
1214	          "LOGO Binary F1",
1215	          "3-class F1",
1216	          "Features Reversed"
1217	        ],
1218	        "rows": [
1219	          [
1220	            "Qwen3-1.7B",
1221	            "Base",
1222	            0.821,
1223	            0.769,
1224	            0
1225	          ],
1226	          [
1227	            "Qwen3-1.7B",
1228	            "Instruct",
1229	            0.658,
1230	            0.543,
1231	            "ρ direction"
1232	          ],
1233	          [
1234	            "OLMo-2-1B",
1235	            "Base",
1236	            0.845,
1237	            0.754,
1238	            0
1239	          ],
1240	          [
1241	            "OLMo-2-1B",
1242	            "Instruct",
1243	            0.813,
1244	            0.575,
1245	            "6/7"
1246	          ],
1247	          [
1248	            "Llama-3.2-3B",
1249	            "Base",
1250	            0.849,
1251	            0.742,
1252	            0
1253	          ],
1254	          [
1255	            "Llama-3.2-3B",
1256	            "Instruct",
1257	            0.838,
1258	            0.544,
1259	            "3/7"
1260	          ]
1261	        ]
1262	      }
1263	    ],
1264	    "figures": [],
1265	    "analysis": "Instruct 退化的 mechanism analysis（feature reversal, not just signal weakening）是 超越简单 \"instruct doesn't work\" 报告的 value-add。Format compliance hypothesis 可 在 future work 中通过 constrained decoding 实验验证。\n\n\n在 best 档下，instruct model 的 DDR 退化被系统性确认：LOGO binary F1 从 base 0.821 降至 instruct 0.658（Qwen, −16.3 pp），OLMo instruct 的 6/7 features Spearman 方向 反转（ρ 从负变正），说明 instruction tuning 的 length regulation 和 format constraints 根本性地改变了 depth-feature relationship。物理解释：alignment 训练强制模型在所有 depth 上产生相似的 token distribution（format compliance），压缩了 DDR 依赖的 distributional variation。这是 base-model-only scope 的核心证据。审稿人在 best 档下 将诚实报告视为 strength：不隐藏 limitation，反而深入分析其 mechanism（feature reversal + format compression hypothesis）。0 instruct scope penalty。\n"
1266	  },
1267	  {
1268	    "name": "temperature_sensitivity",
1269	    "description": "Temperature sensitivity curve (t=0.5, 0.7, 0.9, 1.0) + cross-temperature transfer\n",
1270	    "results": {
1271	      "t05_logo_binary_f1": 0.814,
1272	      "t07_logo_binary_f1": 0.694,
1273	      "t09_logo_binary_f1": 0.48,
1274	      "within_t07_binary": 0.947,
1275	      "cross_t07_to_t10_binary": 0.9,
1276	      "cross_t07_to_t10_qwen_only_binary": 0.757,
1277	      "cross_t07_to_t10_qwen_only_3class": 0.458,
1278	      "entropy_mean_rho_t05": "−0.584",
1279	      "entropy_mean_rho_t07": "−0.600",
1280	      "entropy_mean_rho_t09": "−0.302"
1281	    },
1282	    "tables": [
1283	      {
1284	        "caption": "Table A.4: Temperature sensitivity",
1285	        "columns": [
1286	          "Temperature",
1287	          "Within-CV Binary F1",
1288	          "LOGO Binary F1",
1289	          "entropy_mean ρ"
1290	        ],
1291	        "rows": [
1292	          [
1293	            0.5,
1294	            0.843,
1295	            0.814,
1296	            "−0.584"
1297	          ],
1298	          [
1299	            "0.7 (default)",
1300	            0.947,
1301	            0.694,
1302	            "−0.600"
1303	          ],
1304	          [
1305	            0.9,
1306	            0.582,
1307	            0.48,
1308	            "−0.302"
1309	          ]
1310	        ]
1311	      }
1312	    ],
1313	    "figures": [],
1314	    "analysis": "Temperature sensitivity 直接关联 DDR 的 location-shift 解释：高温增大了每步采样的 distributional noise，削弱了 deterministic drift component。t=0.5 下 signal 更强 因为低温采样更 deterministic，location shift 更 clean。\n\n\n在 best 档下，DDR 在 t∈[0.5, 0.7] 范围内稳定（≤1 pp degradation from default）， t=0.9 大幅退化（−21.4 pp），t=1.0 进一步恶化。Cross-temperature transfer 严重不对称： t=0.7→t=1.0 降 16.9 pp（Qwen-only binary），t=1.0→t=0.7 仅降微弱。物理解释： 高温增大 sampling noise，entropy_mean 的 depth-wise drift 被 within-depth variance 淹没（ρ 从 −0.60 降至 −0.002 at t=1.0）。审稿人在 best 档下接受 t∈[0.5, 0.9] 为 reliable range，t=1.0 degradation 作为 transparent limitation。\n"
1315	  },
1316	  {
1317	    "name": "independent_seed_validation",
1318	    "description": "Independent seed validation：不同生成器使用完全独立的 seed 集\n",
1319	    "results": {
1320	      "pythia_to_olmo_binary_f1": 0.695,
1321	      "olmo_to_pythia_binary_f1": 0.666,
1322	      "avg_binary_f1": 0.68,
1323	      "shared_seed_logo_ref": 0.694,
1324	      "delta_vs_shared": "−0.014"
1325	    },
1326	    "tables": [
1327	      {
1328	        "caption": "Table A.11: Independent vs shared seed evaluation",
1329	        "columns": [
1330	          "Condition",
1331	          "Binary F1",
1332	          "Δ"
1333	        ],
1334	        "rows": [
1335	          [
1336	            "Shared seed LOGO",
1337	            0.694,
1338	            "—"
1339	          ],
1340	          [
1341	            "Independent seed (Pythia→OLMo)",
1342	            0.695,
1343	            0.001
1344	          ],
1345	          [
1346	            "Independent seed (OLMo→Pythia)",
1347	            0.666,
1348	            "−0.028"
1349	          ],
1350	          [
1351	            "Independent seed avg",
1352	            0.68,
1353	            "−0.014"
1354	          ]
1355	        ]
1356	      }
1357	    ],
1358	    "figures": [],
1359	    "analysis": "Independent seed validation 关闭了 seed sharing leakage 的替代假说。 1.4 pp 差异可归因于 generator-specific difficulty 差异而非 leakage。\n\n\n在 best 档下，independent seed 的 avg binary F1=0.680 vs shared seed LOGO 0.694 仅差 1.4 pp，确认 shared seed 不构成显著 leakage。这排除了 \"performance inflated by seed sharing\" 的 critique。1.4 pp 差异在 bootstrap CI 内，不具统计显著性。 方向不对称（Pythia→OLMo 0.695 vs OLMo→Pythia 0.666）反映了 OLMo 作为 test set 更难分类（与 LOGO 结果一致）。\n"
1360	  },
1361	  {
1362	    "name": "topic_drift_control",
1363	    "description": "Semantic similarity analysis：控制 topic drift 作为 depth signal 的 confound\n",
1364	    "results": {
1365	      "sim_0_to_1": 0.622,
1366	      "sim_1_to_2": 0.683,
1367	      "sim_2_to_3": 0.801,
1368	      "sim_3_to_4": 0.859,
1369	      "shape_entropy_std_rho": "−0.164",
1370	      "shape_tail_decay_rho": 0.068,
1371	      "drifting_entropy_mean_rho": "−0.286"
1372	    },
1373	    "tables": [
1374	      {
1375	        "caption": "Table A.12: Semantic similarity by depth transition",
1376	        "columns": [
1377	          "Transition",
1378	          "Mean Sim",
1379	          "Std"
1380	        ],
1381	        "rows": [
1382	          [
1383	            "depth 0→1",
1384	            0.622,
1385	            0.165
1386	          ],
1387	          [
1388	            "depth 1→2",
1389	            0.683,
1390	            0.184
1391	          ],
1392	          [
1393	            "depth 2→3",
1394	            0.801,
1395	            0.201
1396	          ],
1397	          [
1398	            "depth 3→4",
1399	            0.859,
1400	            0.19
1401	          ]
1402	        ]
1403	      }
1404	    ],
1405	    "figures": [],
1406	    "analysis": "Semantic convergence 与 vocabulary impoverishment 是相关但不同的现象：text 变得 semantically more similar（topic narrowing）但 statistically less diverse（DDR drift）。 两者的解耦证明 DDR 不是 topic drift 的简单 proxy。\n\n\n在 best 档下，semantic similarity 随 depth 递增（0.622→0.859），表明 deeper generation 趋向 semantic convergence（repetition/narrowing）。但 DDR feature-depth correlations 在控制 semantic similarity 后仍保持方向和显著性，说明 DDR 不仅仅是 topic drift 的 proxy。Shape features 与 semantic similarity 的 correlation 极弱（|ρ|<0.17）， 进一步确认 shape stationarity 独立于 topic dynamics。审稿人在 best 档下接受 topic drift 分析为 adequate confound control。\n"
1407	  },
1408	  {
1409	    "name": "multi_detector_ensemble",
1410	    "description": "Multi-detector ensemble（4 detectors + surface features）vs 7-feature baseline\n",
1411	    "results": {
1412	      "four_det_surface_3class_f1": 0.795,
1413	      "four_det_surface_binary_f1": 0.708,
1414	      "seven_feature_3class_f1": 0.774,
1415	      "seven_feature_binary_f1": 0.705,
1416	      "delta_3class": 0.021,
1417	      "delta_binary": 0.003,
1418	      "inference_cost_ratio": 2.4,
1419	      "gpu_memory_ratio": 3.2
1420	    },
1421	    "tables": [
1422	      {
1423	        "caption": "Table A.1: Multi-detector ensemble comparison",
1424	        "columns": [
1425	          "Model",
1426	          "3-class F1",
1427	          "Binary F1",
1428	          "Cost Ratio"
1429	        ],
1430	        "rows": [
1431	          [
1432	            "7-feature ensemble",
1433	            0.774,
1434	            0.705,
1435	            "1.0×"
1436	          ],
1437	          [
1438	            "4-det + surface",
1439	            0.795,
1440	            0.708,
1441	            "2.4×"
1442	          ]
1443	        ]
1444	      }
1445	    ],
1446	    "figures": [],
1447	    "analysis": "Multi-detector ensemble 的 marginal gains 进一步验证了 7-feature 的 cost-effectiveness。 3-class 差距 2.1 pp 大于 binary 0.3 pp，因为额外 detector features 主要帮助 gen-0/gen-1 区分（通过 detector-specific calibration），对 gen-1/gen-2+ boundary 几乎无效。\n\n在 best 档下，multi-detector ensemble 以 +2.1 pp (3-class) 和 +0.3 pp (binary) 微弱优于 7-feature，但代价是 2.4× inference cost 和 3.2× GPU memory。Binary F1 差距仅 0.3 pp（essentially equivalent），因为 binary task 的 gen-1/gen-2+ 边界是 intrinsic bottleneck，更多 features 无法突破。7-feature 的 efficiency advantage 在 best 档下被审稿人接受为合理的 positioning：not absolute best, but best cost-performance tradeoff。\n"
1448	  }
1449	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a62018f-1eb1-41ae-9d06-cf9d78b0cfa1",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "02219d42-269b-4bc0-a033-0453a9e0d717",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"feature_ablation_and_trend\",\n    \"description\": \"三部分分析：(A) Feature ablation — full vs reference-only vs surface-only； (B) DDR trend analysis — 每个 feature 的 depth-wise 趋势 + Spearman ρ； (C) Perplexity pre-validation for Claim 3\\n\",\n    \"results\": {\n      \"full_macro_f1\": 0.82,\n      \"reference_only_f1\": 0.719,\n      \"surface_only_f1\": 0.763,\n      \"ref_vs_surf_bootstrap_ci\": \"[0.706, 0.733] vs [0.747, 0.774]\",\n      \"drifting_features\": \"entropy_mean (ρ≈−0.60), TTR (ρ≈−0.61), hapax_ratio (ρ≈−0.63)\",\n      \"stationary_features\": \"tail_decay (ρ≈0.04), entropy_std (ρ≈−0.12), entropy_max (ρ≈0.05)\",\n      \"median_ppl_by_depth\": \"13.50 → 4.96 → 3.00 → 2.07 → 1.72\",\n      \"ppl_depth_monotonic\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 2: Feature ablation results (5-fold CV, Pythia-2.8B)\",\n        \"columns\": [\n          \"Feature Set\",\n          \"N Features\",\n          \"Macro F1\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"Full\",\n            7,\n            0.82,\n            \"[0.807, 0.833]\"\n          ],\n          [\n            \"Surface-only\",\n            2,\n            0.763,\n            \"[0.747, 0.774]\"\n          ],\n          [\n            \"Reference-only\",\n            5,\n            0.719,\n            \"[0.706, 0.733]\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 3: Feature-depth Spearman correlations\",\n        \"columns\": [\n          \"Feature\",\n          \"ρ\",\n          \"Category\",\n          \"Trend\"\n        ],\n        \"rows\": [\n          [\n            \"hapax_ratio\",\n            \"−0.63\",\n            \"Drifting\",\n            \"Monotonic decrease\"\n          ],\n          [\n            \"TTR\",\n            \"−0.61\",\n            \"Drifting\",\n            \"Monotonic decrease\"\n          ],\n          [\n            \"entropy_mean\",\n            \"−0.60\",\n            \"Drifting\",\n            \"Monotonic decrease\"\n          ],\n          [\n            \"entropy_min\",\n            \"−0.39\",\n            \"Intermediate\",\n            \"Moderate decrease\"\n          ],\n          [\n            \"entropy_std\",\n            \"−0.12\",\n            \"Stationary\",\n            \"Near-flat\"\n          ],\n          [\n            \"entropy_max\",\n            0.05,\n            \"Stationary\",\n            \"Near-flat\"\n          ],\n          [\n            \"tail_decay\",\n            0.04,\n            \"Stationary\",\n            \"Near-flat\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Full > Surface > Reference 的排序表明 surface 特征（TTR, hapax）捕获了最强的单维信号， 但 reference 特征提供了不可替代的互补信息。Surface-only 虽然绝对值更高，但 reference-only 在 binary task（gen-1 vs gen-2+）上表现更优（binary F1=0.833 vs 0.695），这是因为 reference 特征在排除 gen-0 后捕获了更 fine-grained 的 NLL 分布位移。 DDR 分离的物理解释：递归生成诱导 NLL 分布的 location shift，central-tendency 指标（mean, TTR, hapax）跟踪这一 shift 因而漂移，shape 指标（max, tail_decay）反映分布形态因而稳定。\\n\\n\\n在 best 档下，full 7-feature 以 0.820 显著高于两个 subset（McNemar p≈0）， surface-only 以 0.763 高于 reference-only 0.719，但两者都显著低于 full， 证明互补性而非冗余性。审稿人接受这一 4.4 pp gap 作为 complementarity 证据。 DDR 趋势清晰：drifting 三特征 |ρ|>0.60 呈单调下降，shape 特征 |ρ|<0.12 近乎水平。Perplexity 随 depth 单调下降（13.50→1.72）预验证 Claim 3 信号存在。 这组结果为后续所有实验奠定特征空间基础。\\n\"\n  },\n  {\n    \"name\": \"cross_generator_evaluation\",\n    \"description\": \"扩展至 5 generators（Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B）， LOGO 交叉验证评估跨生成器泛化性\\n\",\n    \"results\": {\n      \"total_records\": 18423,\n      \"generators\": 5,\n      \"logo_avg_macro_f1\": 0.804,\n      \"logo_best_held_out\": {\n        \"model\": \"pythia-1b\",\n        \"f1\": 0.851\n      },\n      \"logo_worst_held_out\": {\n        \"model\": \"olmo-2-1b\",\n        \"f1\": 0.752\n      },\n      \"lofo_delta\": 0.011,\n      \"ablation_full_f1\": 0.804,\n      \"ablation_reference_only_f1\": 0.754,\n      \"ablation_surface_only_f1\": 0.747,\n      \"mcnemar_p\": 0.0,\n      \"top3_features\": [\n        \"hapax_ratio (0.289)\",\n        \"ttr (0.168)\",\n        \"entropy_mean (0.160)\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 4: LOGO cross-generator evaluation\",\n        \"columns\": [\n          \"Held-out Generator\",\n          \"Macro F1\",\n          \"Binary F1\",\n          \"Gen-1 F1\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            0.851,\n            0.724,\n            0.689\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.824,\n            0.71,\n            0.652\n          ],\n          [\n            \"Qwen3-1.7B\",\n            0.805,\n            0.698,\n            0.641\n          ],\n          [\n            \"Pythia-2.8B\",\n            0.804,\n            0.694,\n            0.638\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.752,\n            0.663,\n            0.585\n          ],\n          [\n            \"Average\",\n            0.804,\n            0.694,\n            0.641\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-gen LOGO 为后续 8-gen/9-gen 扩展奠定基线。OLMo 的相对弱势来自其 tokenizer 和 训练数据分布与 Pythia/Qwen 的差异——这本身验证了 DDR 在不同预训练配方下的鲁棒性（仍 >0.75）。 LOFO delta 仅 0.011 说明 Pythia 家族重叠未严重膨胀 LOGO 指标。\\n\\n\\n在 best 档下，5-gen LOGO 均值 0.804 显示强跨生成器泛化。Pythia-1B held-out 最高（0.851） 因为 Pythia-2.8B 在训练集中提供了同家族信号；OLMo held-out 最低（0.752）因为 OLMo 的生成分布与 Pythia/Qwen 家族差异最大。Family-out delta 仅 0.011 pp，审稿人接受为 cross-family generalization 证据。Feature importance 排序（hapax > ttr > entropy_mean） 与 plan_001 一致，确认 surface drifting 特征是主驱动力，但 McNemar p≈0 证明 reference 特征对 full 集的贡献统计显著。\\n\"\n  },\n  {\n    \"name\": \"cross_family_reference_model\",\n    \"description\": \"测试非 Pythia reference model（OLMo-2-1B, Qwen3-0.6B）提取特征， 验证 DDR 是否为 generation-intrinsic 而非 reference-model artifact\\n\",\n    \"results\": {\n      \"logo_f1_pythia_ref\": 0.803,\n      \"logo_f1_olmo_ref\": 0.807,\n      \"logo_f1_qwen_ref\": 0.816,\n      \"entropy_drift_all_refs_negative\": true,\n      \"pythia_ref_drift_range\": \"[−1.19, −1.40]\",\n      \"olmo_ref_drift_range\": \"[−0.61, −0.91]\",\n      \"qwen_ref_drift_range\": \"[−0.96, −1.35]\",\n      \"dual_dynamics_is_pythia_artifact\": false\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 5: Cross-reference-model DDR validation\",\n        \"columns\": [\n          \"Reference Model\",\n          \"LOGO F1\",\n          \"entropy_mean drift range\",\n          \"DDR preserved\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-410M (default)\",\n            0.803,\n            \"[−1.19, −1.40]\",\n            \"✓\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.807,\n            \"[−0.61, −0.91]\",\n            \"✓\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.816,\n            \"[−0.96, −1.35]\",\n            \"✓\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"漂移幅度的差异（Pythia > Qwen > OLMo）反映了 reference model 自身 perplexity scale 的差异， 但方向一致性是关键。这排除了 \\\"DDR 只是 Pythia tokenizer 的 artifact\\\" 这一最致命的替代解释。\\n\\n\\n在 best 档下，三个 reference model 均产生负向 entropy drift（所有 range 为负）， LOGO F1 跨 reference 差异 <1.5 pp（0.803–0.816），关键性地证明 DDR 是 generation-intrinsic 现象而非 Pythia-410M 特有 artifact。Qwen reference 略优 可能因其 tokenizer 粒度更细，捕获了更丰富的 NLL 分布信息。这是 Claim 2 的核心 falsification test 通过：如果 DDR 消失于非 Pythia reference，整个 dual dynamics 叙事将崩塌。审稿人在 best 档下接受这一 3-reference 交叉验证为充分证据。\\n\"\n  },\n  {\n    \"name\": \"downstream_utility\",\n    \"description\": \"OLMo-1B fine-tune on depth-stratified subsets，3 seeds with bootstrap CIs， sample-count-matched comparison。验证 Claim 3（negative finding）。\\n\",\n    \"results\": {\n      \"total_runs\": 15,\n      \"variants\": {\n        \"all\": {\n          \"ppl_mean\": 2.335,\n          \"ppl_std\": 0.0003\n        },\n        \"size_matched\": {\n          \"ppl_mean\": 2.367,\n          \"ppl_std\": 0.0002\n        },\n        \"depth01\": {\n          \"ppl_mean\": 2.387,\n          \"ppl_std\": 0.0005\n        },\n        \"binary_filtered\": {\n          \"ppl_mean\": 2.389,\n          \"ppl_std\": 0.0004\n        },\n        \"depth0_only\": {\n          \"ppl_mean\": 2.681,\n          \"ppl_std\": 0.0012\n        }\n      },\n      \"ranking\": \"all(2.335) < size_matched(2.367) < depth01(2.387) ≈ binary_filtered(2.389) << depth0_only(2.681)\",\n      \"tost_equivalence_p\": 0.00011,\n      \"tost_margin\": \"±2%\",\n      \"seed_variance\": \"<0.002 ppl across seeds within same variant\",\n      \"cohens_d_sizeMatched_vs_depth01\": \"inflated by low variance\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 7: Downstream CLM perplexity by training data composition (3 seeds)\",\n        \"columns\": [\n          \"Variant\",\n          \"N train\",\n          \"Ppl (mean±std)\",\n          \"Δ vs size_matched\"\n        ],\n        \"rows\": [\n          [\n            \"All data\",\n            12299,\n            \"2.335 ± 0.0003\",\n            \"−0.032\"\n          ],\n          [\n            \"Size-matched random\",\n            3951,\n            \"2.367 ± 0.0002\",\n            \"— (baseline)\"\n          ],\n          [\n            \"Depth 0+1 only\",\n            3951,\n            \"2.387 ± 0.0005\",\n            0.02\n          ],\n          [\n            \"Binary-filtered\",\n            3951,\n            \"2.389 ± 0.0004\",\n            0.022\n          ],\n          [\n            \"Depth 0 only\",\n            797,\n            \"2.681 ± 0.0012\",\n            0.314\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative finding 的关键价值在于终止了一个看似合理但无效的研究方向：既然 depth 信息存在且可检测， 自然会假设可用于数据筛选。实验证明这一假设不成立。More data > better data 在 3951 samples 的低数据量下尤为明显。TOST equivalence 而非 NHST 是正确的统计框架选择。\\n\\n\\n在 best 档下，negative finding 清晰：depth-aware filtering 不优于 random subsampling（size_matched 2.367 vs depth01 2.387，差 0.020 ppl）。TOST 在 ±2% margin 下 p=1.1×10⁻⁴ 确认统计等价。 depth0_only 的显著劣势（2.681）是预期的——纯人类文本量太少（797 samples）。关键是 size_matched vs depth01 的差异方向反直觉：random subsample 比 depth-curated 还好 0.020 ppl， 说明 depth 信息对下游 CLM 质量无 curative 价值。审稿人在 best 档下将此认可为 \\\"valuable honest science\\\" 而非 \\\"method doesn't work\\\"——论文诚实地将 depth fingerprinting 定位为 diagnostic tool（provenance characterization）而非 curative tool（data selection）。 三 seed 极低方差（<0.002）既增强结论可靠性，也意味着 Cohen's d 被人为放大，论文正确选择 TOST 而非 effect size 作为主检验。\\n\"\n  },\n  {\n    \"name\": \"prompt_type_comparison\",\n    \"description\": \"比较 continuation / elaboration / inspired_rewriting 三种 prompt type 的 depth signal\\n\",\n    \"results\": {\n      \"cv_f1\": {\n        \"continuation\": 0.781,\n        \"inspired_rewriting\": 0.737,\n        \"elaboration\": 0.73\n      },\n      \"lopto_f1\": {\n        \"held_out_continuation\": 0.762,\n        \"held_out_elaboration\": 0.762,\n        \"held_out_rewriting\": 0.733,\n        \"average\": 0.753\n      },\n      \"depth_retention_d4_d0\": {\n        \"continuation\": 0.831,\n        \"inspired_rewriting\": 0.939,\n        \"elaboration\": 0.986\n      },\n      \"drift_hapax\": {\n        \"continuation\": \"−0.74\",\n        \"elaboration\": \"−0.83\",\n        \"rewriting\": \"−0.80\"\n      },\n      \"drift_ttr\": {\n        \"continuation\": \"−0.607\",\n        \"elaboration\": \"−0.641\",\n        \"rewriting\": \"−0.618\"\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 8: Prompt-type comparison (Pythia-2.8B)\",\n        \"columns\": [\n          \"Prompt Type\",\n          \"CV F1\",\n          \"LOPTO F1\",\n          \"Depth Retention\",\n          \"hapax ρ\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.781,\n            0.762,\n            0.831,\n            \"−0.74\"\n          ],\n          [\n            \"Inspired rewriting\",\n            0.737,\n            0.733,\n            0.939,\n            \"−0.80\"\n          ],\n          [\n            \"Elaboration\",\n            0.73,\n            0.762,\n            0.986,\n            \"−0.83\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Prompt-type 差异本身是有趣发现：语义约束越强（elaboration > rewriting > continuation）， chain 越稳定但 depth discriminability 越低。这与 DDR 的 location-shift 解释一致—— 约束越强，模型输出分布被锚定在更窄的范围内，location shift 幅度减小。\\n\\n\\n在 best 档下，三种 prompt type 均保留 DDR 信号但强度不同。Continuation 的 within-type CV F1 最高（0.781）但 depth retention 最低（83.1%），因为 continuation 给予模型最大自由度， 导致更多 chain dropout 但也产生更强的 distributional shift。Elaboration retention 最高 （98.6%）但 CV F1 最低（0.730），因为 elaboration 约束模型围绕原文展开，压缩了 cross-depth 变异。Rewriting 居中。Leave-one-prompt-type-out 交叉验证（avg 0.753） 低于 within-type（avg 0.749）仅 ~0.4 pp，表明 prompt type 间的 DDR 信号高度可迁移。 审稿人接受 prompt-type dependence 的透明报告为 ecological validity 证据。\\n\"\n  },\n  {\n    \"name\": \"paraphrastic_comparison\",\n    \"description\": \"构建平行 paraphrasing chains 与 continuation chains 直接比较， 测试 attractor convergence theory\\n\",\n    \"results\": {\n      \"paraphrase_cv_f1\": 0.62,\n      \"continuation_cv_f1\": 0.781,\n      \"paraphrase_depth_retention\": 0.97,\n      \"paraphrase_hapax_rho\": \"−0.25\",\n      \"paraphrase_entropy_mean_rho\": \"−0.18\",\n      \"attractor_convergence_depth\": 2,\n      \"delta_cv_f1\": \"−0.161\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 9: Paraphrastic vs non-paraphrastic chains\",\n        \"columns\": [\n          \"Chain Type\",\n          \"CV F1\",\n          \"hapax ρ\",\n          \"entropy_mean ρ\",\n          \"Retention d4/d0\"\n        ],\n        \"rows\": [\n          [\n            \"Continuation\",\n            0.781,\n            \"−0.74\",\n            \"−0.56\",\n            0.831\n          ],\n          [\n            \"Paraphrasing\",\n            0.62,\n            \"−0.25\",\n            \"−0.18\",\n            0.97\n          ],\n          [\n            \"Δ\",\n            \"−0.161\",\n            0.49,\n            0.38,\n            0.139\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文与 ACL 2025 attractor cycle 理论的关键联系点。Non-paraphrastic chains 不受 semantic-preservation attractor 约束，因此 distributional drift 可以持续到更深层， 为 depth estimation 提供更丰富的信号空间。\\n\\n\\n在 best 档下，paraphrasing chains 的 depth signal 显著弱于 continuation（CV F1 0.62 vs 0.781，−16.1 pp）。Paraphrasing 由于语义保持约束，每步输出被 attractor basin 拉回， depth 间差异在 depth 2 后趋于收敛（与 ACL 2025 \\\"LLM as Broken Telephone\\\" 的 ~3 class ceiling 一致）。DDR drifting 特征在 paraphrase 中 ρ 幅度大幅缩小（hapax −0.25 vs −0.63）， 因为 paraphrase 保持语义→保持词汇多样性→TTR/hapax drift 被抑制。这验证了论文核心定位： DDR 是 non-paraphrastic chain 特有的现象，paraphrastic chain 走向 attractor convergence。 审稿人在 best 档下接受这一对比作为 task formulation 的 motivation——深度估计在 continuation/elaboration chain 中才有 meaningful signal。\\n\"\n  },\n  {\n    \"name\": \"cross_model_chains\",\n    \"description\": \"Cross-model chains（每步使用不同 generator）vs single-model chains， 模拟真实 web contamination 场景\\n\",\n    \"results\": {\n      \"cross_model_binary_f1\": 0.83,\n      \"cross_model_3class_f1\": 0.789,\n      \"single_model_binary_f1\": 0.694,\n      \"single_model_3class_f1\": 0.762,\n      \"cross_model_logo_binary\": 0.83,\n      \"delta_binary_vs_single\": 0.136,\n      \"n_generators_in_cross\": 5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 6: Cross-model vs single-model chain evaluation\",\n        \"columns\": [\n          \"Setting\",\n          \"Binary F1\",\n          \"3-class F1\",\n          \"N Generators\"\n        ],\n        \"rows\": [\n          [\n            \"Single-model LOGO\",\n            0.694,\n            0.762,\n            \"8 (homogeneous)\"\n          ],\n          [\n            \"Cross-model LOGO\",\n            0.83,\n            0.789,\n            \"5 (heterogeneous)\"\n          ],\n          [\n            \"Δ\",\n            0.136,\n            0.027,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model 的优势来自 generator heterogeneity amplifying distributional shifts。 在单模型 chain 中，depth-wise drift 是同一模型 bias 的累积；在 cross-model chain 中， 每步引入新模型 bias，产生更大的 inter-depth 特征差异。这是 ecological validity 的 正面证据：真实世界的 contamination 更可能涉及多个 generator。\\n\\n\\n在 best 档下，cross-model chains 的 binary F1 0.830 显著高于 single-model 0.694 （+13.6 pp），这一 counterintuitive 结果的原因是：不同 generator 在每步引入额外的 distributional discontinuity（不同 tokenizer bias, 不同 perplexity scale）， 放大了 depth 间的特征差异。这对审稿人而言是 strength——说明在更 realistic 的 heterogeneous contamination 场景下，depth signal 反而更强。0.830 cross-model binary F1 被 highlight 为 generalization evidence，审稿人接受 5-gen subset LOGO 作为评估方法。 3-class F1 同样提升（0.789 vs 0.762），但提升幅度小于 binary，因为 gen-0 identification 的 seed-sharing advantage 在两种设定下相当。\\n\"\n  },\n  {\n    \"name\": \"multi_domain_seeds\",\n    \"description\": \"扩展至 4 domains（Wikipedia, news, scientific, creative/code）， 500 seeds/domain × 5 depths\\n\",\n    \"results\": {\n      \"news_binary_f1\": 0.746,\n      \"news_binary_ci\": [\n        0.726,\n        0.764\n      ],\n      \"academic_binary_f1\": 0.739,\n      \"academic_binary_ci\": [\n        0.72,\n        0.757\n      ],\n      \"code_binary_f1\": 0.754,\n      \"code_binary_ci\": [\n        0.737,\n        0.77\n      ],\n      \"wikipedia_baseline_binary_f1\": 0.815,\n      \"max_gap_vs_wiki_pp\": 7.62,\n      \"worst_domain\": \"academic\",\n      \"best_domain\": \"code\",\n      \"conclusion_label\": \"domain_independent\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 10: Multi-domain evaluation\",\n        \"columns\": [\n          \"Domain\",\n          \"Binary F1\",\n          \"95% CI\",\n          \"3-class F1\"\n        ],\n        \"rows\": [\n          [\n            \"Wikipedia (baseline)\",\n            0.815,\n            \"[0.799, 0.831]\",\n            0.863\n          ],\n          [\n            \"Code\",\n            0.754,\n            \"[0.737, 0.770]\",\n            0.634\n          ],\n          [\n            \"News\",\n            0.746,\n            \"[0.726, 0.764]\",\n            0.652\n          ],\n          [\n            \"Academic\",\n            0.739,\n            \"[0.720, 0.757]\",\n            0.622\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-domain 结果直接回应 RC6（ecological validity）。DDR 在 news/academic/code 上的 一致性说明 depth signal 不依赖于特定文本类型的 vocabulary 特征。3-class F1 的 domain 差异更大（0.622–0.863），因为 gen-0 vs gen-1 区分依赖 seed-specific 线索，这在 不同 domain 中差异更大。\\n\\n\\n在 best 档下，所有 domain 的 binary F1 均在 0.739–0.754 范围内（排除 Wikipedia 基线）， domain 间 max gap 仅 1.5 pp，审稿人接受 DDR 为 domain-independent 现象。Wikipedia 基线（0.815）高出 ~7 pp 是预期的——Wikipedia 种子文本结构化程度更高、长度更稳定， 减少了 confounding variation。Academic domain 最低（0.739）因为学术文本的词汇多样性 本身就高且 depth 间变化小（base model 生成学术文本时更依赖 template phrasing）。 Code domain 意外地最高（0.754），因为 code-like 文本的 entropy 分布更 bimodal， DDR drifting 在 entropy_mean 上更明显。所有 CI 均不包含 0.5（random baseline）， 确认 depth signal 在所有 domain 中统计显著。\\n\"\n  },\n  {\n    \"name\": \"finer_grained_ordinal\",\n    \"description\": \"5-class 序数分类（gen-0 至 gen-4），测试更细粒度 depth resolution 的可行性\\n\",\n    \"results\": {\n      \"five_class_f1\": 0.5,\n      \"three_class_f1_reference\": 0.762,\n      \"ordinal_coral_f1\": 0.49,\n      \"ordinal_frank_hall_f1\": 0.5,\n      \"xgboost_standard_f1\": 0.5,\n      \"bottleneck\": \"gen-1/gen-2 boundary, 86% binary FNs concentrated here\",\n      \"gen3_vs_gen4_f1\": 0.35\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.3: Ordinal classification results\",\n        \"columns\": [\n          \"Method\",\n          \"3-class F1\",\n          \"5-class F1\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"XGBoost (standard)\",\n            0.762,\n            0.5,\n            \"−0.262\"\n          ],\n          [\n            \"CORAL\",\n            0.758,\n            0.49,\n            \"−0.268\"\n          ],\n          [\n            \"Frank-Hall\",\n            0.76,\n            0.5,\n            \"−0.260\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"5-class 的 ceiling 与 DDR 的物理解释一致：location shift 在前几步（0→1→2）幅度最大， 之后递减。Gen-3 和 gen-4 的 NLL 分布差异已小于 feature extraction noise floor。\\n\\n\\n在 best 档下，5-class F1 降至 ~0.50，相比 3-class 的 0.762 大幅下降。Ordinal methods （CORAL, Frank-Hall）未能改善——这说明 depth signal 的 resolution ceiling 在 3 class， 不是分类方法的选择问题而是 feature space 的固有限制。Gen-1/gen-2 boundary 贡献了 86% 的 binary errors（作为 FN），因为 gen-1 和 gen-2 在 feature space 中高度重叠。 Gen-3 vs gen-4 几乎不可分（F1≈0.35）。审稿人在 best 档下接受 3-class 为 practical ceiling，论文诚实报告这一限制为 strength。5-class 负面结果排除了 \\\"只要用更好方法就能 区分更多 depth\\\" 的替代假说。\\n\"\n  },\n  {\n    \"name\": \"human_edit_robustness\",\n    \"description\": \"鲁棒性测试：(A) Random word replacement (5/10/20%)，(B) LLM-simulated editing\\n\",\n    \"results\": {\n      \"baseline_binary_f1\": 0.695,\n      \"random_5pct_f1\": 0.65,\n      \"random_10pct_f1\": 0.614,\n      \"random_20pct_f1\": 0.591,\n      \"llm_rephrase_binary_f1\": 0.647,\n      \"llm_rephrase_multiclass_f1\": 0.667,\n      \"llm_edit_distance_ratio\": 0.507,\n      \"llm_avg_sentences_replaced\": 1.69,\n      \"drop_5pct\": \"−0.046\",\n      \"drop_10pct\": \"−0.081\",\n      \"drop_20pct\": \"−0.104\",\n      \"drop_llm\": \"−0.045\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.5: Robustness to text editing\",\n        \"columns\": [\n          \"Condition\",\n          \"Binary F1\",\n          \"Δ vs baseline\"\n        ],\n        \"rows\": [\n          [\n            \"No editing (baseline)\",\n            0.695,\n            \"—\"\n          ],\n          [\n            \"5% random replacement\",\n            0.65,\n            \"−0.046\"\n          ],\n          [\n            \"10% random replacement\",\n            0.614,\n            \"−0.081\"\n          ],\n          [\n            \"20% random replacement\",\n            0.591,\n            \"−0.104\"\n          ],\n          [\n            \"LLM rephrase (avg 1.69 sent)\",\n            0.647,\n            \"−0.045\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLM rephrase 与 5% random 的 drop 相近这一发现本身有价值：LLM editing 的特征空间扰动 并不比 naive random replacement 更具破坏性，可能因为 LLM editing 保持了文本的局部统计 一致性（不引入 out-of-distribution tokens）。\\n\\n\\n在 best 档下，depth signal 对 human editing 展现 graceful degradation。5% random noise 仅降 4.6 pp，LLM rephrase（平均替换 1.69 句，编辑距离 50.7%）降 4.5 pp——两者接近， 因为 LLM rephrase 虽然更自然但实际修改幅度（50.7% edit distance）与 5% random 在 feature 空间的扰动量级相当。20% random 的 10.4 pp drop 仍保持 F1>0.59（>random baseline）， 说明 depth signal 不完全依赖逐字保真。审稿人在 best 档下将 graceful degradation 视为 positive——完全抵抗 editing 是不现实的，important 是 degradation curve 平滑且 在 realistic editing level（5–10%）下性能损失可控。LLM rephrase 结果直接回应 RC5。\\n\"\n  },\n  {\n    \"name\": \"ld_score_feature\",\n    \"description\": \"添加 LD-Score（character-level distributional signature）作为额外特征\\n\",\n    \"results\": {\n      \"seven_feature_f1\": 0.798,\n      \"eight_feature_with_ld_f1\": 0.803,\n      \"ld_score_only_f1\": 0.721,\n      \"ld_score_spearman_depth\": \"−0.794\",\n      \"delta_with_ld\": 0.005,\n      \"ld_feature_importance_rank\": 4\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.6: LD-Score augmentation\",\n        \"columns\": [\n          \"Feature Set\",\n          \"LOGO F1\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature (default)\",\n            0.798,\n            \"—\"\n          ],\n          [\n            \"7-feature + LD-Score\",\n            0.803,\n            0.005\n          ],\n          [\n            \"LD-Score only\",\n            0.721,\n            \"−0.077\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LD-Score 的 marginal contribution 较小（+0.5 pp），确认 7-feature set 已捕获大部分 depth signal。Character-level 信息主要通过 character frequency distribution 的 shift 反映 vocabulary impoverishment，与 TTR/hapax 高度相关。\\n\\n\\n在 best 档下，LD-Score 作为 character-level 特征与 token-level reference 特征部分互补， 加入后 LOGO F1 提升 0.5 pp（0.798→0.803），统计上显著但 practical 提升有限。 LD-Score 单独的 F1=0.721 介于 surface-only（0.688）和 reference-only（0.713）之间， Spearman ρ=−0.794 表明其与 depth 有强负相关。Feature importance 排第 4（在 hapax, ttr, entropy_mean 之后），说明 LD-Score 捕获的信号与 reference 特征高度 correlated 但非完全冗余。审稿人在 best 档下接受将 LD-Score 作为 supplementary evidence， 论文在 appendix 中报告此结果。7-feature 仍为 primary model 以保持简洁性。\\n\"\n  },\n  {\n    \"name\": \"end_to_end_classifier\",\n    \"description\": \"QLoRA fine-tuned model 进行端到端 depth classification， 比较 learned representations vs handcrafted features\\n\",\n    \"results\": {\n      \"qlora_olmo_instruct_3class_f1\": 0.888,\n      \"qlora_qwen_instruct_3class_f1\": 0.907,\n      \"qlora_olmo_base_3class_f1\": 0.859,\n      \"qlora_qwen_base_3class_f1\": 0.904,\n      \"qlora_olmo_instruct_binary_f1\": 0.836,\n      \"qlora_qwen_instruct_binary_f1\": 0.867,\n      \"qlora_olmo_base_binary_f1\": 0.793,\n      \"qlora_qwen_base_binary_f1\": 0.86,\n      \"qlora_5class_best_f1\": 0.597,\n      \"seven_feature_3class_f1\": 0.762,\n      \"delta_3class\": \"+12.6–14.5 pp\",\n      \"inference_cost_ratio\": \"~15×\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.7: End-to-end QLoRA vs 7-feature ensemble\",\n        \"columns\": [\n          \"Model\",\n          \"Type\",\n          \"3-class F1\",\n          \"Binary F1\",\n          \"5-class F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-1.7B (instruct)\",\n            \"QLoRA\",\n            0.907,\n            0.867,\n            0.551\n          ],\n          [\n            \"OLMo-1B (instruct)\",\n            \"QLoRA\",\n            0.888,\n            0.836,\n            0.598\n          ],\n          [\n            \"Qwen3-1.7B (base)\",\n            \"QLoRA\",\n            0.904,\n            0.86,\n            0.554\n          ],\n          [\n            \"OLMo-1B (base)\",\n            \"QLoRA\",\n            0.859,\n            0.793,\n            0.54\n          ],\n          [\n            \"7-feature ensemble\",\n            \"XGBoost\",\n            0.762,\n            0.694,\n            0.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"QLoRA 的成功并不削弱 7-feature 的贡献：(1) 7-feature 提供了可解释的 DDR 框架，QLoRA 是 black box；(2) 7-feature 的 reference model 仅 410M，QLoRA 需 1.7B+；(3) QLoRA 同样 受 5-class ceiling 限制，确认这是 task boundary 而非 method limitation。\\n\\n\\n在 best 档下，QLoRA fine-tuned models 以 3-class F1 0.859–0.907 大幅超越 7-feature ensemble 的 0.762（+10–15 pp），证明 learned representations 能捕获 handcrafted features 遗漏的深层信号。但 5-class F1 仍仅 ~0.60，说明 resolution ceiling 是 task-intrinsic 而非 feature engineering 限制。Binary F1 提升较小（0.793–0.867 vs 0.694）， 因为 binary task 的 bottleneck 在 gen-1/gen-2+ 边界，learned features 也难以完全突破。 Instruct model 意外地与 base model 表现接近甚至略优（OLMo instruct 0.888 vs base 0.859）， 因为 QLoRA 的端到端学习可以 bypass DDR degradation，直接从 raw text 学习 depth pattern。 审稿人在 best 档下接受 7-feature 的定位转换：不追求绝对最优，而是 efficiency advantage（单次 Pythia-410M forward pass vs QLoRA 推理的 ~15× 成本差距）。\\n\"\n  },\n  {\n    \"name\": \"text_length_control\",\n    \"description\": \"文本长度 confound 控制：分析长度分布、length-normalized features、length-matched evaluation\\n\",\n    \"results\": {\n      \"length_depth_spearman_range\": \"[−0.066, +0.134]\",\n      \"length_is_confound\": false,\n      \"normalized_ttr_trend_preserved\": true,\n      \"normalized_hapax_trend_preserved\": true,\n      \"normalized_rho_stronger\": true,\n      \"length_matched_f1\": 0.724,\n      \"unmatched_f1\": 0.77,\n      \"length_matched_delta\": \"−0.046\",\n      \"dropout_short_text_bias\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.8: Length confound analysis\",\n        \"columns\": [\n          \"Condition\",\n          \"Binary F1\",\n          \"Δ vs unmatched\"\n        ],\n        \"rows\": [\n          [\n            \"Unmatched (full)\",\n            0.77,\n            \"—\"\n          ],\n          [\n            \"Length-matched\",\n            0.724,\n            \"−0.046\"\n          ],\n          [\n            \"Random subsample control\",\n            0.724,\n            \"−0.046\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Length confound 是 reviewer 高频关注点（RC10）。−4.6 pp drop 的来源是 deconfounding 而非信息损失，这通过 random subsample control 证实。Length-matched F1=0.724 可作为 conservative lower bound 报告在 abstract 中。\\n\\n\\n在 best 档下，text length 与 depth 的 Spearman ρ 在 [−0.066, +0.134] 范围内（弱相关）， 排除 length 作为主要 confound。Length-normalized features（TTR, hapax 在 fixed-length window 上计算）保持甚至增强了 depth 趋势（normalized ρ stronger），说明 DDR drift 不是 length artifact。Length-matched 后 F1 从 0.770 降至 0.724（−4.6 pp），但对照实验确认 这一 drop 来自 deconfounding 而非 sample size reduction（random subsample control 也降 相同幅度）。Depth 增加→更多短文本 dropout 的 bias 被确认，但通过 length matching 控制后 signal 仍然显著（0.724 >> 0.5）。审稿人在 best 档下接受 length-matched 0.724 作为 conservative 的 deconfounded 估计。\\n\"\n  },\n  {\n    \"name\": \"large_scale_generator\",\n    \"description\": \"添加 7B+ generator（Qwen3-8B-Base）测试 frontier scale 下的 depth signal\\n\",\n    \"results\": {\n      \"total_records\": 4497,\n      \"unique_seeds\": 995,\n      \"depth_dist\": {\n        \"0\": 995,\n        \"1\": 979,\n        \"2\": 937,\n        \"3\": 831,\n        \"4\": 755\n      },\n      \"logo_6gen_avg_f1\": 0.789,\n      \"qwen3_8b_held_out_f1\": 0.683,\n      \"logo_5gen_baseline_f1\": 0.8,\n      \"spearman_hapax\": \"−0.558\",\n      \"spearman_ttr\": \"−0.542\",\n      \"spearman_entropy_mean\": \"−0.475\",\n      \"spearman_tail_decay\": \"−0.089\",\n      \"feature_importance_top3\": [\n        \"hapax_ratio (0.269)\",\n        \"entropy_mean (0.164)\",\n        \"ttr (0.159)\"\n      ]\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 11: 6-generator LOGO with Qwen3-8B\",\n        \"columns\": [\n          \"Generator\",\n          \"LOGO F1\",\n          \"hapax ρ\",\n          \"Scale\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            0.856,\n            \"−0.65\",\n            \"1.0B\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.824,\n            \"−0.63\",\n            \"0.6B\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            0.805,\n            \"−0.61\",\n            \"1.7B\"\n          ],\n          [\n            \"Pythia-2.8B\",\n            0.804,\n            \"−0.63\",\n            \"2.8B\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.764,\n            \"−0.60\",\n            \"1.5B\"\n          ],\n          [\n            \"Qwen3-8B\",\n            0.683,\n            \"−0.56\",\n            \"8.0B\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale degradation 是最重要的 scope limitation 之一。6-gen LOGO 加入 8B 后均值从 0.800 降至 0.789，Qwen3-8B 拉低了整体。但 DDR pattern（drifting vs stationary）在 8B 下完全 保持，说明这是 amplitude reduction 而非 qualitative change。Feature importance 排序 不变（hapax > entropy_mean > ttr），confirmed DDR 的 cross-scale robustness。\\n\\n\\n在 best 档下，Qwen3-8B held-out F1=0.683 低于 6-gen 平均 0.789（−10.6 pp）， 证实 larger models 产生更弱的 depth signal。物理解释：8B 模型的更高容量压缩了 depth-wise feature margins——更强的 language model 在每步生成中保持了更接近 source distribution 的输出，DDR location shift 幅度减小。但 0.683 仍显著高于 random（0.5）， 且 DDR 方向一致（hapax ρ=−0.558, tail_decay ρ=−0.089 仍为 stationary）。 审稿人在 best 档下接受 scale effect 作为 honest limitation with analysis， 而非 fatal flaw——0.683 在 8B scale 下仍为 non-trivial signal。Depth retention 从 d0 到 d4 降至 0.759（995→755），高 dropout 率部分解释了 F1 下降。\\n\"\n  },\n  {\n    \"name\": \"ordinal_baseline_comparison\",\n    \"description\": \"关键 baseline：测试现有 detector（FastDetectGPT, Binoculars, LD-Score）的连续分数 是否已提供 ordinal depth signal\\n\",\n    \"results\": {\n      \"seven_feature_logo_f1\": 0.798,\n      \"seven_feature_ci\": [\n        0.786,\n        0.799\n      ],\n      \"avg_logprob_logo_f1\": 0.765,\n      \"avg_logprob_ci\": [\n        0.616,\n        0.82\n      ],\n      \"ld_score_logo_f1\": 0.721,\n      \"ld_score_ci\": [\n        0.588,\n        0.77\n      ],\n      \"fast_detect_gpt_logo_f1\": 0.627,\n      \"fast_detect_gpt_ci\": [\n        0.511,\n        0.762\n      ],\n      \"binoculars_logo_f1\": 0.579,\n      \"binoculars_ci\": [\n        0.405,\n        0.664\n      ],\n      \"bootstrap_7feat_vs_avglogprob\": {\n        \"delta\": 0.039,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"bootstrap_7feat_vs_fdgpt\": {\n        \"delta\": 0.067,\n        \"p\": 0.0,\n        \"significant\": true\n      },\n      \"best_single_detector\": \"Avg-LogProb (0.765)\",\n      \"seven_feature_advantage_pp\": 3.3\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 5: Ordinal baseline comparison (LOGO)\",\n        \"columns\": [\n          \"Method\",\n          \"LOGO F1\",\n          \"95% CI\",\n          \"Spearman ρ\",\n          \"Δ vs 7-feature\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature ensemble\",\n            0.798,\n            \"[0.786, 0.799]\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Avg-LogProb\",\n            0.765,\n            \"[0.616, 0.820]\",\n            0.788,\n            \"−0.033\"\n          ],\n          [\n            \"LD-Score\",\n            0.721,\n            \"[0.588, 0.770]\",\n            0.794,\n            \"−0.077\"\n          ],\n          [\n            \"FastDetectGPT\",\n            0.627,\n            \"[0.511, 0.762]\",\n            0.433,\n            \"−0.171\"\n          ],\n          [\n            \"Binoculars\",\n            0.579,\n            \"[0.405, 0.664]\",\n            0.199,\n            \"−0.219\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文中最关键的 baseline comparison——如果 Avg-LogProb alone 达到 0.80+，7-feature 的 contribution 就会被严重削弱。0.765 vs 0.798 的差距虽小但真实：7-feature 的优势 集中在 cross-generator 泛化（更窄 CI）和 gen-0 discrimination（surface features 必需）。 Binoculars 的 bug fix（denominator 从 CE(performer, obs_argmax) 改为 CE(performer, shifted_ids)）确保了公平比较。\\n\\n\\n在 best 档下，7-feature ensemble（0.798）显著优于所有 single-detector baselines （bootstrap p=0 for all pairwise comparisons）。最强 baseline Avg-LogProb（0.765） 差 3.3 pp，这一差距虽不大但统计显著——关键在于 7-feature 的 CI [0.786, 0.799] 与 Avg-LogProb 的 CI [0.616, 0.820] 不重叠于下界。Avg-LogProb 的强表现说明 ordinal depth signal 部分可被简单的 log-probability 特征捕获（Spearman ρ=0.788），但 7-feature 通过 组合 drifting + stationary 特征实现了更稳定的跨生成器泛化（更窄的 CI）。 FastDetectGPT（0.627）和 Binoculars（0.579）表现较差，因为它们设计为 binary detectors， 连续分数的 ordinal sensitivity 有限。LD-Score（0.721）居中，character-level 信息 提供了中等 ordinal signal。审稿人在 best 档下接受 7-feature 的优势为 \\\"modest but consistent\\\"——贡献不在于绝对性能碾压，而在于 DDR 框架的可解释性和互补性。\\n\"\n  },\n  {\n    \"name\": \"9gen_scale_evaluation\",\n    \"description\": \"扩展至 9 generators（+Gemma-2-2B, Llama-3.2-3B, Mistral-7B-v0.3）， 验证 8→9 gen 的 scaling behavior\\n\",\n    \"results\": {\n      \"9gen_logo_3class_f1\": 0.751,\n      \"9gen_logo_binary_f1\": 0.666,\n      \"8gen_baseline_3class_f1\": 0.77,\n      \"delta_9gen_vs_8gen\": \"−0.019\",\n      \"gemma_held_out_3class_f1\": 0.628,\n      \"gemma_held_out_binary_f1\": 0.44,\n      \"mistral_held_out_3class_f1\": 0.605,\n      \"mistral_held_out_binary_f1\": 0.633,\n      \"n_generators\": 9,\n      \"n_total_rows\": 42015\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.9: 9-generator per-generator LOGO F1\",\n        \"columns\": [\n          \"Generator\",\n          \"3-class F1\",\n          \"Binary F1\",\n          \"Family\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia-1B\",\n            0.857,\n            0.724,\n            \"Pythia\"\n          ],\n          [\n            \"Qwen3-0.6B\",\n            0.819,\n            0.71,\n            \"Qwen\"\n          ],\n          [\n            \"Pythia-2.8B\",\n            0.812,\n            0.7,\n            \"Pythia\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            0.811,\n            0.698,\n            \"Qwen\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            0.773,\n            0.663,\n            \"OLMo\"\n          ],\n          [\n            \"Llama-3.2-3B\",\n            0.759,\n            0.68,\n            \"Llama\"\n          ],\n          [\n            \"Qwen3-8B\",\n            0.696,\n            0.647,\n            \"Qwen\"\n          ],\n          [\n            \"Gemma-2-2B\",\n            0.628,\n            0.44,\n            \"Gemma\"\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.605,\n            0.633,\n            \"Mistral\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"9-gen 是 thoroughness 的体现。Gemma anomaly 提供了 negative case study：当 tokenizer 差异过大时，cross-model reference 特征的假设被违反。这实际上深化了 DDR 的理解—— DDR 依赖于 reference model 与 generator 之间的 tokenizer compatibility。\\n\\n\\n在 best 档下，9-gen LOGO 3-class F1=0.751 较 8-gen 的 0.770 降 1.9 pp，主要由 Gemma-2-2B 的异常表现拉低（gen-1 F1=0.036）。Gemma 的异常来自其独特的 tokenizer （SentencePiece vs BPE）导致 reference model 特征提取偏移。Mistral-7B 的 0.605 反映了 7B scale 的 signal compression（与 plan_014 Qwen3-8B 的 0.696 一致）。 审稿人在 best 档下接受 Gemma anomaly 作为 honest outlier analysis（appendix 中详细 讨论 tokenizer mismatch），8-gen 结果作为 primary metric，9-gen 作为 robustness check。 Binary F1 0.666 是 conservative lower bound——Gemma 的 binary F1=0.440 接近 random。\\n\"\n  },\n  {\n    \"name\": \"ddr_causality_analysis\",\n    \"description\": \"DDR causality analysis: permutation importance + Granger causality + feature intervention\\n\",\n    \"results\": {\n      \"permutation_baseline_f1\": 0.771,\n      \"drifting_avg_importance\": 0.158,\n      \"stationary_avg_importance\": 0.03,\n      \"drifting_stationary_ratio\": 5.31,\n      \"granger_significant_features\": \"6/7\",\n      \"granger_nonsig_feature\": \"entropy_min\",\n      \"granger_max_delta_r2\": 0.031,\n      \"granger_panel_n\": 29095,\n      \"intervention_max_f1_drop\": 0.02\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 6: DDR causality analysis\",\n        \"columns\": [\n          \"Feature\",\n          \"Perm Importance\",\n          \"Granger sig\",\n          \"Category\"\n        ],\n        \"rows\": [\n          [\n            \"hapax_ratio\",\n            0.289,\n            \"✓ (p<0.001)\",\n            \"Drifting\"\n          ],\n          [\n            \"ttr\",\n            0.168,\n            \"✓ (p<0.001)\",\n            \"Drifting\"\n          ],\n          [\n            \"entropy_mean\",\n            0.16,\n            \"✓ (p<0.001)\",\n            \"Drifting\"\n          ],\n          [\n            \"entropy_std\",\n            0.046,\n            \"✓ (p<0.05)\",\n            \"Stationary\"\n          ],\n          [\n            \"entropy_max\",\n            0.063,\n            \"✓ (p<0.01)\",\n            \"Stationary\"\n          ],\n          [\n            \"entropy_min\",\n            0.015,\n            \"✗ (p=0.12)\",\n            \"Stationary\"\n          ],\n          [\n            \"tail_decay\",\n            0.012,\n            \"✓ (p<0.05)\",\n            \"Stationary\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Causality analysis 是论文从 \\\"observation\\\" 升级到 \\\"empirical contribution\\\" 的关键。 仅报告 DDR correlation 会被审稿人视为 descriptive；加入 Granger + permutation + intervention 三角验证后，DDR 的 causal status 被充分支撑。entropy_min 的 Granger 不显著实际上增强了可信度——不是所有特征都需要 causal relationship。\\n\\n\\n在 best 档下，drifting/stationary 分离经三重 causality test 验证：(1) Permutation importance 5.3× gap（drifting 0.158 vs stationary 0.030）确认 drifting 特征对分类的 贡献远超 stationary；(2) 6/7 Granger 显著（仅 entropy_min 不显著）确认 depth→feature 的 temporal causality；(3) Feature intervention 的最大 F1 drop 仅 0.020 pp 表明 单特征 intervention 不足以破坏分类——signal 分布在 drifting 特征组合中。 审稿人在 best 档下将这组 causality evidence 视为 \\\"sufficient\\\" 而非 \\\"mere correlation\\\"， 认可 DDR 作为 genuine empirical contribution 而非 vocabulary impoverishment 的重新包装。 5.5× permutation gap + 6/7 Granger 的组合在 Findings 级别属于 strong evidence。\\n\"\n  },\n  {\n    \"name\": \"tost_bootstrap_stability\",\n    \"description\": \"TOST bootstrap 验证 stationary 特征的稳定性\\n\",\n    \"results\": {\n      \"n_bootstrap\": 1000,\n      \"margin_d\": 0.2,\n      \"entropy_max\": {\n        \"median_p\": 0.0,\n        \"rejection_rate\": 1.0,\n        \"median_d\": 0.062\n      },\n      \"entropy_min\": {\n        \"median_p\": 0.0,\n        \"rejection_rate\": 1.0,\n        \"median_d\": \"−0.016\"\n      },\n      \"tail_decay\": {\n        \"median_p\": 0.0,\n        \"rejection_rate\": 1.0,\n        \"median_d\": 0.088\n      },\n      \"entropy_std\": {\n        \"median_p\": 1.0,\n        \"rejection_rate\": 0.0,\n        \"median_d\": 0.458\n      },\n      \"stationary_features_robust\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.10: TOST bootstrap stationarity test\",\n        \"columns\": [\n          \"Feature\",\n          \"Median d\",\n          \"TOST p\",\n          \"Rejection Rate\",\n          \"Status\"\n        ],\n        \"rows\": [\n          [\n            \"entropy_max\",\n            0.062,\n            0.0,\n            1.0,\n            \"Stationary ✓\"\n          ],\n          [\n            \"entropy_min\",\n            \"−0.016\",\n            0.0,\n            1.0,\n            \"Stationary ✓\"\n          ],\n          [\n            \"tail_decay\",\n            0.088,\n            0.0,\n            1.0,\n            \"Stationary ✓\"\n          ],\n          [\n            \"entropy_std\",\n            0.458,\n            1.0,\n            0.0,\n            \"Intermediate (rejected)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"TOST bootstrap 为 DDR 分离提供了比 Spearman ρ 更严格的统计基础。entropy_std 的 intermediate status 实际上加强了论文的 nuance——不是简单的二分法，而是一个连续谱， 论文选择在 practical level 上维持 drifting/stationary 二分以保持 clarity。\\n\\n\\n在 best 档下，TOST bootstrap 确认 3/4 stationary-candidate 特征在 d=0.2 margin 下 统计等价于 depth-invariant（rejection rate=100%, median d<0.1）。entropy_std 被拒绝 （median d=0.458, rejection rate=0%），因为它虽然 Spearman ρ 低（−0.12）但 effect size 超出 equivalence margin——entropy_std 是 \\\"weak drifter\\\" 而非 true stationary。 这一发现精细化了 DDR 分类：3 strong drifters (hapax, TTR, entropy_mean) + 3 true stationary (entropy_max, entropy_min, tail_decay) + 1 intermediate (entropy_std)。 审稿人在 best 档下接受 TOST 作为比 ρ 更严格的 stationarity test，entropy_std 的 intermediate status 被视为 nuanced finding 而非 inconsistency。\\n\"\n  },\n  {\n    \"name\": \"instruct_model_degradation\",\n    \"description\": \"三个 instruct model（Qwen3-1.7B, OLMo-2-1B, Llama-3.2-3B）的 DDR 退化分析\\n\",\n    \"results\": {\n      \"qwen_instruct_logo_binary\": 0.658,\n      \"olmo_instruct_within_3class\": 0.575,\n      \"llama_instruct_3class\": 0.544,\n      \"qwen_base_logo_binary\": 0.821,\n      \"delta_logo_binary_qwen\": \"−0.163\",\n      \"features_reversed_olmo\": \"6/7\",\n      \"features_reversed_llama\": \"3/7 (entropy_mean, entropy_std, tail_decay)\",\n      \"spearman_direction_reversal\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 12: Instruct vs base model comparison\",\n        \"columns\": [\n          \"Model\",\n          \"Type\",\n          \"LOGO Binary F1\",\n          \"3-class F1\",\n          \"Features Reversed\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-1.7B\",\n            \"Base\",\n            0.821,\n            0.769,\n            0\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"Instruct\",\n            0.658,\n            0.543,\n            \"ρ direction\"\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"Base\",\n            0.845,\n            0.754,\n            0\n          ],\n          [\n            \"OLMo-2-1B\",\n            \"Instruct\",\n            0.813,\n            0.575,\n            \"6/7\"\n          ],\n          [\n            \"Llama-3.2-3B\",\n            \"Base\",\n            0.849,\n            0.742,\n            0\n          ],\n          [\n            \"Llama-3.2-3B\",\n            \"Instruct\",\n            0.838,\n            0.544,\n            \"3/7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Instruct 退化的 mechanism analysis（feature reversal, not just signal weakening）是 超越简单 \\\"instruct doesn't work\\\" 报告的 value-add。Format compliance hypothesis 可 在 future work 中通过 constrained decoding 实验验证。\\n\\n\\n在 best 档下，instruct model 的 DDR 退化被系统性确认：LOGO binary F1 从 base 0.821 降至 instruct 0.658（Qwen, −16.3 pp），OLMo instruct 的 6/7 features Spearman 方向 反转（ρ 从负变正），说明 instruction tuning 的 length regulation 和 format constraints 根本性地改变了 depth-feature relationship。物理解释：alignment 训练强制模型在所有 depth 上产生相似的 token distribution（format compliance），压缩了 DDR 依赖的 distributional variation。这是 base-model-only scope 的核心证据。审稿人在 best 档下 将诚实报告视为 strength：不隐藏 limitation，反而深入分析其 mechanism（feature reversal + format compression hypothesis）。0 instruct scope penalty。\\n\"\n  },\n  {\n    \"name\": \"temperature_sensitivity\",\n    \"description\": \"Temperature sensitivity curve (t=0.5, 0.7, 0.9, 1.0) + cross-temperature transfer\\n\",\n    \"results\": {\n      \"t05_logo_binary_f1\": 0.814,\n      \"t07_logo_binary_f1\": 0.694,\n      \"t09_logo_binary_f1\": 0.48,\n      \"within_t07_binary\": 0.947,\n      \"cross_t07_to_t10_binary\": 0.9,\n      \"cross_t07_to_t10_qwen_only_binary\": 0.757,\n      \"cross_t07_to_t10_qwen_only_3class\": 0.458,\n      \"entropy_mean_rho_t05\": \"−0.584\",\n      \"entropy_mean_rho_t07\": \"−0.600\",\n      \"entropy_mean_rho_t09\": \"−0.302\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.4: Temperature sensitivity\",\n        \"columns\": [\n          \"Temperature\",\n          \"Within-CV Binary F1\",\n          \"LOGO Binary F1\",\n          \"entropy_mean ρ\"\n        ],\n        \"rows\": [\n          [\n            0.5,\n            0.843,\n            0.814,\n            \"−0.584\"\n          ],\n          [\n            \"0.7 (default)\",\n            0.947,\n            0.694,\n            \"−0.600\"\n          ],\n          [\n            0.9,\n            0.582,\n            0.48,\n            \"−0.302\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature sensitivity 直接关联 DDR 的 location-shift 解释：高温增大了每步采样的 distributional noise，削弱了 deterministic drift component。t=0.5 下 signal 更强 因为低温采样更 deterministic，location shift 更 clean。\\n\\n\\n在 best 档下，DDR 在 t∈[0.5, 0.7] 范围内稳定（≤1 pp degradation from default）， t=0.9 大幅退化（−21.4 pp），t=1.0 进一步恶化。Cross-temperature transfer 严重不对称： t=0.7→t=1.0 降 16.9 pp（Qwen-only binary），t=1.0→t=0.7 仅降微弱。物理解释： 高温增大 sampling noise，entropy_mean 的 depth-wise drift 被 within-depth variance 淹没（ρ 从 −0.60 降至 −0.002 at t=1.0）。审稿人在 best 档下接受 t∈[0.5, 0.9] 为 reliable range，t=1.0 degradation 作为 transparent limitation。\\n\"\n  },\n  {\n    \"name\": \"independent_seed_validation\",\n    \"description\": \"Independent seed validation：不同生成器使用完全独立的 seed 集\\n\",\n    \"results\": {\n      \"pythia_to_olmo_binary_f1\": 0.695,\n      \"olmo_to_pythia_binary_f1\": 0.666,\n      \"avg_binary_f1\": 0.68,\n      \"shared_seed_logo_ref\": 0.694,\n      \"delta_vs_shared\": \"−0.014\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.11: Independent vs shared seed evaluation\",\n        \"columns\": [\n          \"Condition\",\n          \"Binary F1\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Shared seed LOGO\",\n            0.694,\n            \"—\"\n          ],\n          [\n            \"Independent seed (Pythia→OLMo)\",\n            0.695,\n            0.001\n          ],\n          [\n            \"Independent seed (OLMo→Pythia)\",\n            0.666,\n            \"−0.028\"\n          ],\n          [\n            \"Independent seed avg\",\n            0.68,\n            \"−0.014\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Independent seed validation 关闭了 seed sharing leakage 的替代假说。 1.4 pp 差异可归因于 generator-specific difficulty 差异而非 leakage。\\n\\n\\n在 best 档下，independent seed 的 avg binary F1=0.680 vs shared seed LOGO 0.694 仅差 1.4 pp，确认 shared seed 不构成显著 leakage。这排除了 \\\"performance inflated by seed sharing\\\" 的 critique。1.4 pp 差异在 bootstrap CI 内，不具统计显著性。 方向不对称（Pythia→OLMo 0.695 vs OLMo→Pythia 0.666）反映了 OLMo 作为 test set 更难分类（与 LOGO 结果一致）。\\n\"\n  },\n  {\n    \"name\": \"topic_drift_control\",\n    \"description\": \"Semantic similarity analysis：控制 topic drift 作为 depth signal 的 confound\\n\",\n    \"results\": {\n      \"sim_0_to_1\": 0.622,\n      \"sim_1_to_2\": 0.683,\n      \"sim_2_to_3\": 0.801,\n      \"sim_3_to_4\": 0.859,\n      \"shape_entropy_std_rho\": \"−0.164\",\n      \"shape_tail_decay_rho\": 0.068,\n      \"drifting_entropy_mean_rho\": \"−0.286\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.12: Semantic similarity by depth transition\",\n        \"columns\": [\n          \"Transition\",\n          \"Mean Sim\",\n          \"Std\"\n        ],\n        \"rows\": [\n          [\n            \"depth 0→1\",\n            0.622,\n            0.165\n          ],\n          [\n            \"depth 1→2\",\n            0.683,\n            0.184\n          ],\n          [\n            \"depth 2→3\",\n            0.801,\n            0.201\n          ],\n          [\n            \"depth 3→4\",\n            0.859,\n            0.19\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semantic convergence 与 vocabulary impoverishment 是相关但不同的现象：text 变得 semantically more similar（topic narrowing）但 statistically less diverse（DDR drift）。 两者的解耦证明 DDR 不是 topic drift 的简单 proxy。\\n\\n\\n在 best 档下，semantic similarity 随 depth 递增（0.622→0.859），表明 deeper generation 趋向 semantic convergence（repetition/narrowing）。但 DDR feature-depth correlations 在控制 semantic similarity 后仍保持方向和显著性，说明 DDR 不仅仅是 topic drift 的 proxy。Shape features 与 semantic similarity 的 correlation 极弱（|ρ|<0.17）， 进一步确认 shape stationarity 独立于 topic dynamics。审稿人在 best 档下接受 topic drift 分析为 adequate confound control。\\n\"\n  },\n  {\n    \"name\": \"multi_detector_ensemble\",\n    \"description\": \"Multi-detector ensemble（4 detectors + surface features）vs 7-feature baseline\\n\",\n    \"results\": {\n      \"four_det_surface_3class_f1\": 0.795,\n      \"four_det_surface_binary_f1\": 0.708,\n      \"seven_feature_3class_f1\": 0.774,\n      \"seven_feature_binary_f1\": 0.705,\n      \"delta_3class\": 0.021,\n      \"delta_binary\": 0.003,\n      \"inference_cost_ratio\": 2.4,\n      \"gpu_memory_ratio\": 3.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table A.1: Multi-detector ensemble comparison\",\n        \"columns\": [\n          \"Model\",\n          \"3-class F1\",\n          \"Binary F1\",\n          \"Cost Ratio\"\n        ],\n        \"rows\": [\n          [\n            \"7-feature ensemble\",\n            0.774,\n            0.705,\n            \"1.0×\"\n          ],\n          [\n            \"4-det + surface\",\n            0.795,\n            0.708,\n            \"2.4×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-detector ensemble 的 marginal gains 进一步验证了 7-feature 的 cost-effectiveness。 3-class 差距 2.1 pp 大于 binary 0.3 pp，因为额外 detector features 主要帮助 gen-0/gen-1 区分（通过 detector-specific calibration），对 gen-1/gen-2+ boundary 几乎无效。\\n\\n在 best 档下，multi-detector ensemble 以 +2.1 pp (3-class) 和 +0.3 pp (binary) 微弱优于 7-feature，但代价是 2.4× inference cost 和 3.2× GPU memory。Binary F1 差距仅 0.3 pp（essentially equivalent），因为 binary task 的 gen-1/gen-2+ 边界是 intrinsic bottleneck，更多 features 无法突破。7-feature 的 efficiency advantage 在 best 档下被审稿人接受为合理的 positioning：not absolute best, but best cost-performance tradeoff。\\n\"\n  }\n]",
      "numLines": 1449,
      "startLine": 1,
      "totalLines": 1449
    }
  },
  "sourceToolAssistantUUID": "2a62018f-1eb1-41ae-9d06-cf9d78b0cfa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "02219d42-269b-4bc0-a033-0453a9e0d717",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from dream data",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Assistant

_source line 16 · 2026-05-20T10:27:41.326Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02219d42-269b-4bc0-a033-0453a9e0d717",
  "isSidechain": false,
  "requestId": "req_011CbDfMKm8Qzc2QQn8ro4zg",
  "type": "assistant",
  "uuid": "700a8d83-9327-4636-a267-e12958165350",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKLkdCksnc4HAi1PQrcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3764,
      "cache_creation_input_tokens": 24194,
      "cache_read_input_tokens": 24727,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3764,
          "output_tokens": 248,
          "cache_read_input_tokens": 24727,
          "cache_creation_input_tokens": 24194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24194
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

_source line 17 · 2026-05-20T10:27:42.061Z_

Now let me check the output directory and load the paper-writing-norms skill for style guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700a8d83-9327-4636-a267-e12958165350",
  "isSidechain": false,
  "requestId": "req_011CbDfMKm8Qzc2QQn8ro4zg",
  "type": "assistant",
  "uuid": "47e3939f-746c-474d-ba9f-e6126abcffd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKLkdCksnc4HAi1PQrcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3764,
      "cache_creation_input_tokens": 24194,
      "cache_read_input_tokens": 24727,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3764,
          "output_tokens": 248,
          "cache_read_input_tokens": 24727,
          "cache_creation_input_tokens": 24194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24194
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

_source line 18 · 2026-05-20T10:27:44.147Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AXTwmE1dcsJohhjfs6bVzQ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47e3939f-746c-474d-ba9f-e6126abcffd3",
  "isSidechain": false,
  "requestId": "req_011CbDfMKm8Qzc2QQn8ro4zg",
  "type": "assistant",
  "uuid": "56e89ee7-c9cd-420c-bc79-b55658ef4a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKLkdCksnc4HAi1PQrcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3764,
      "cache_creation_input_tokens": 24194,
      "cache_read_input_tokens": 24727,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3764,
          "output_tokens": 248,
          "cache_read_input_tokens": 24727,
          "cache_creation_input_tokens": 24194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24194
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

_source line 19 · 2026-05-20T10:27:44.296Z_

<details><summary>↩ Tool result · `toolu_01AXTwmE1dcsJohhjfs6bVzQ`</summary>

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
  "parentUuid": "56e89ee7-c9cd-420c-bc79-b55658ef4a9b",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "d19c7f63-3f77-445a-9aad-d189f023189e",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "56e89ee7-c9cd-420c-bc79-b55658ef4a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T10:27:45.021Z_

<details open><summary>🔧 Tool call — Read · `toolu_01No3WrReJ1Vi8i6CpkJUXMK`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d19c7f63-3f77-445a-9aad-d189f023189e",
  "isSidechain": false,
  "requestId": "req_011CbDfMKm8Qzc2QQn8ro4zg",
  "type": "assistant",
  "uuid": "7e4e3904-d5e5-48af-9c90-610b1b3b13ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3vKLkdCksnc4HAi1PQrcu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3764,
      "cache_creation_input_tokens": 24194,
      "cache_read_input_tokens": 24727,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3764,
          "output_tokens": 248,
          "cache_read_input_tokens": 24727,
          "cache_creation_input_tokens": 24194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24194
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

_source line 21 · 2026-05-20T10:27:45.030Z_

<details><summary>↩ Tool result · `toolu_01No3WrReJ1Vi8i6CpkJUXMK`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e4e3904-d5e5-48af-9c90-610b1b3b13ed",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "d12919ae-2662-4869-a6c8-759693b86251",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  },
  "sourceToolAssistantUUID": "7e4e3904-d5e5-48af-9c90-610b1b3b13ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-20T10:28:22.466Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me write the full LaTeX paper. This is a "够审" (reviewable) level paper about generation depth fingerprinting. Let me organize the content from the experiment data and paper framing into a coherent paper.

Key structure:
1. Abstract
2. Introduction (with Story Spine)
3. Related Work
4. Method (Feature extraction, DDR framework, classification setup)
5. Experiments (organized by the experiments in experiment_data.json)
6. Discussion & Limitations
7. Conclusion
8. Appendix sections for supplementary experiments


9. Main body experiments: feature ablation and DDR trends, baseline comparisons, cross-generator evaluation, cross-model chains, DDR causality analysis, cross-family reference models, downstream utility findings, and instruct model degradation patterns, with additional experiments in the appendix. I'm reconsidering the paper structure—with 33 pages already and no reviewer objections, I should prioritize the most critical experiments for the main body and move the rest to the appendix. Let me cross-reference the table numbering from the experiment data to figure out which results are essential versus supplementary.

Now I'm mapping out the remaining tables—downstream perplexity results, prompt-type comparisons, paraphrastic variations, multi-domain validation, and various robustness checks like temperature sensitivity and text editing effects all need to be organized across the main tables and appendix sections. similarity

There are some numbering conflicts (Table 5 appears twice, Table 6 appears twice). I'll renumber them cleanly.

Let me organize the main body sections logically:

**§3 Method**: Feature extraction (7 features), DDR framework, classification setup, evaluation protocol (LOGO, LOFO, binary vs 3-class)

**§4 Main Results**:
- §4.1 Feature Ablation and DDR Characterization → Table 1 (ablation), Table 2 (Spearman)
- §4.2 Cross-Generator Generalization → Table 3 (LOGO)
- §4.3 Baseline Comparison → Table 4 (ordinal baseline)
- §4.4 Cross-Model Chains → Table 5
- §4.5 DDR Causality Analysis → Table 6 (causality)
- §4.6 Cross-Reference Model Validation → Table 7
- §4.7 Instruct Model Degradation → Table 8
- §4.8 Downstream Utility (Negative Finding) → Table 9

**§5 Additional Experiments** will go in the appendix with the remaining analyses. For the title, I'm settling on "Generation Depth Fingerprinting via Differential Depth Response in Non-Paraphrastic LLM Chains" to capture the core contribution. Now I'll write out the full LaTeX document with all experiments integrated comprehensively. I'm settling on a generic article class for flexibility since this is a conceptual paper. Now I need to write carefully—pulling exact numbers from the experiment data, maintaining the DDR framing throughout, structuring around three core claims, and being transparent about limitations while keeping the primary metric as leak-free binary F1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d12919ae-2662-4869-a6c8-759693b86251",
  "isSidechain": false,
  "requestId": "req_011CbDfMtGjcR2tKk8LwahMd",
  "type": "assistant",
  "uuid": "2f6caeb5-a18d-4d0a-b365-8098adc837ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8kDum9Wf5memJEKwmStXy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6067,
      "cache_read_input_tokens": 48921,
      "output_tokens": 17656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17656,
          "cache_read_input_tokens": 48921,
          "cache_creation_input_tokens": 6067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6067
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

_source line 23 · 2026-05-20T10:28:22.468Z_

Now I'll write the full paper. This is a comprehensive LaTeX document covering all 20 experiments from the data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f6caeb5-a18d-4d0a-b365-8098adc837ae",
  "isSidechain": false,
  "requestId": "req_011CbDfMtGjcR2tKk8LwahMd",
  "type": "assistant",
  "uuid": "f9be6289-f2ad-4a02-88fe-8a924f95d855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8kDum9Wf5memJEKwmStXy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6067,
      "cache_read_input_tokens": 48921,
      "output_tokens": 17656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17656,
          "cache_read_input_tokens": 48921,
          "cache_creation_input_tokens": 6067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6067
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

_source line 24 · 2026-05-20T10:32:44.688Z_

<details open><summary>🔧 Tool call — Write · `toolu_0135mD7ySDYZiPqepZ6kMxUG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pval}{\\textit{p}}\n\\newcommand{\\rhosp}{\\rho}\n\n\\title{Generation Depth Fingerprinting via Differential Depth Response\\\\in Non-Paraphrastic LLM Chains}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth.\nCurrent detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material:\nfirst-generation text retains much of the source distribution's lexical properties, while deeper recursive generations exhibit measurably reduced vocabulary diversity and compressed perplexity.\nWe formulate \\textbf{generation depth classification} (gen-0 / gen-1 / gen-2+) as a new task beyond binary detection\nand characterize \\textbf{Differential Depth Response} (DDR):\ncentral-tendency features (entropy mean, type--token ratio, hapax ratio) drift monotonically with depth,\nwhile shape features (entropy max, tail decay) remain near-stationary---consistent with recursive generation inducing a location shift in the NLL distribution while approximately preserving distributional shape.\nOn 8 base-model generators from 5 families (0.6B--8B), a lightweight 7-feature ensemble achieves\nleak-free binary \\fone{} = 0.694 under leave-one-generator-out (LOGO) evaluation\nand 0.830 on cross-model chains, using a single 410M reference model.\nCausality analysis confirms DDR with 6/7 Granger-significant features and a 5.3$\\times$ permutation importance gap between drifting and stationary features.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language model quality\n(TOST \\pval{} = 1.1$\\times$10$^{-4}$ at $\\pm$2\\% margin),\nestablishing depth fingerprinting as a \\emph{diagnostic} tool for provenance characterization, not a curative tool for data selection.\nThe signal degrades substantially under instruction tuning, restricting current scope to base models.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) now generate text that is increasingly difficult to distinguish from human-written content.\nAs LLM-generated text proliferates on the web---estimates suggest 7--17\\% of recent scientific papers contain substantial AI-generated content---it inevitably re-enters training corpora for subsequent models.\nThis creates recursive generation chains: a human writes a seed text (generation depth 0),\nan LLM produces a continuation (depth 1), another LLM may further elaborate on that output (depth 2), and so on.\nUnderstanding where a given text sits along this chain---its \\emph{generation depth}---is crucial for data governance,\ntraining corpus curation, and understanding the feedback loops that drive model collapse.\n\nExisting AI-text detectors frame the problem as binary classification: human vs.\\ machine.\nMethods such as DetectGPT \\citep{mitchell2023detectgpt}, FastDetectGPT \\citep{bao2024fastdetectgpt}, Binoculars \\citep{hans2024binoculars}, and LD-Score \\citep{tulchinskii2024ldscore}\nachieve strong binary discrimination but cannot distinguish first-generation text from deeper recursive generations.\nThis conflation matters: gen-1 text retains substantial distributional similarity to its human source,\nwhile gen-2+ text exhibits measurably compressed vocabulary diversity and perplexity---qualitatively different material that may differentially affect downstream model quality.\nSeparately, work on paraphrastic chains \\citep{briesch2025llmbrokenphone} has shown attractor convergence behavior limiting depth discriminability to approximately 3 classes,\nbut this depends on semantic-preservation constraints absent in non-paraphrastic continuation chains.\n\nIn this paper, we formulate \\textbf{generation depth classification} as a new task and characterize the distributional signatures that enable it.\nWe introduce the concept of \\textbf{Differential Depth Response} (DDR):\nwhen text is recursively generated through non-paraphrastic chains,\ncentral-tendency and diversity features of the token-level negative log-likelihood (NLL) distribution\n(entropy mean, type--token ratio, hapax ratio) \\emph{drift} monotonically with depth,\nwhile shape features (entropy max, tail decay) remain \\emph{near-stationary}.\nThis is consistent with recursive generation inducing a location shift in the NLL distribution while approximately preserving distributional shape.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Task formulation.} We define generation depth classification (gen-0/gen-1/gen-2+) as a tractable ordinal classification problem beyond binary detection. No prior work addresses depth estimation in non-paraphrastic continuation chains.\n\n\\item \\textbf{Empirical characterization of DDR.} We validate DDR across 8 base-model generators from 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B scale), 3 prompt types, and 4 text domains. A 7-feature ensemble achieves leak-free binary \\fone{} = 0.694 under LOGO and 0.830 on cross-model chains. Causality analysis (6/7 Granger-significant features, 5.3$\\times$ permutation importance gap) confirms DDR as a genuine empirical phenomenon beyond vocabulary impoverishment.\n\n\\item \\textbf{Negative finding on downstream utility.} Depth-aware data curation does not improve downstream CLM quality compared to random subsampling (TOST equivalence confirmed at $\\pm$2\\% margin). Depth fingerprinting is a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{enumerate}\n\nWe transparently report scope limitations: the signal degrades substantially under instruction tuning and high sampling temperatures ($t > 0.9$), and 5-class ordinal resolution is not achievable with current features (ceiling at 3 classes).\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Perplexity-based AI-text detection.}\nStatistical detection methods leverage the observation that LLM-generated text occupies lower-perplexity regions of the model's output distribution.\nDetectGPT \\citep{mitchell2023detectgpt} uses perturbation-based log-probability curvature;\nFastDetectGPT \\citep{bao2024fastdetectgpt} replaces perturbations with conditional probability sampling for efficiency.\nBinoculars \\citep{hans2024binoculars} compares cross-entropy ratios between two models.\nGLTR \\citep{gehrmann2019gltr} visualizes token-level statistics.\nDNA-GPT \\citep{yang2024dnagpt} employs divergent continuation comparison.\nAll operate as binary classifiers; none address ordinal depth estimation.\n\n\\paragraph{Distributional signatures and LD-Score.}\n\\citet{tulchinskii2024ldscore} propose character-level distributional signatures (LD-Score) for authorship verification and AI detection, demonstrating that distributional divergence at the character level captures stylistic fingerprints. We incorporate LD-Score as both a baseline and an augmentation feature (Appendix~\\ref{app:ld}).\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical work on model collapse \\citep{shumailov2024modelcollapse} predicts that recursive training on synthetic data leads to distributional narrowing and eventual mode collapse.\n\\citet{dohmatob2024collapse} formalize the rate of distributional degradation.\nOur work complements this line by providing an empirical method to \\emph{detect} the depth signature of recursive generation in individual texts, rather than studying the aggregate distributional consequences for model training.\n\n\\paragraph{Iterative generation chains.}\n\\citet{briesch2025llmbrokenphone} study paraphrastic LLM chains and find attractor convergence limiting depth discriminability to approximately 3 semantic clusters. Our work studies non-paraphrastic chains (continuation, elaboration), where the absence of semantic-preservation constraints allows distributional drift to persist to deeper levels.\n\n\\paragraph{Vocabulary diversity and stylometry.}\nType--token ratio (TTR), hapax legomena ratio, and entropy-based measures have a long history in computational stylometry and authorship attribution \\citep{tweedie1998variable}. We repurpose these as depth-discriminative features and show they capture the ``drifting'' component of DDR.\n\n\\paragraph{Data quality and curation.}\nPerplexity-based filtering \\citep{wenzek2019ccnet} and quality classifiers are standard in training data pipelines. Our Claim~3 (negative finding) directly tests whether depth information adds value to such curation, finding it does not.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\nGiven a text $x$, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$,\nwhere $d=0$ denotes human-written seed text, $d=1$ denotes first-generation LLM output from a human seed,\nand $d=2+$ denotes text produced at depth $\\geq 2$ in a recursive generation chain.\nThe primary evaluation metric is \\textbf{leak-free binary \\fone{}}: the \\fone{} for discriminating gen-1 from gen-2+,\nexcluding gen-0 samples to avoid inflated performance from seed-sharing cues.\n\n\\subsection{Chain Construction}\n\\label{sec:chains}\nWe construct recursive generation chains of depth 0--4 using base-model LLMs.\nGiven a human-written seed text $x_0$ (depth 0), we prompt a generator $G$ to produce $x_1 = G(x_0)$ (depth 1),\nthen $x_2 = G(x_1)$ (depth 2), and so on up to $x_4$.\nWe evaluate three prompt types: \\emph{continuation} (unconstrained generation),\n\\emph{elaboration} (expand on the input), and \\emph{inspired rewriting} (write new text inspired by the input).\nSeed texts are drawn from four domains: Wikipedia, news, academic, and code.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\nWe extract 7 features from each text using a reference language model (Pythia-410M by default).\nFor each token $t_i$ in the text, we compute its negative log-likelihood (NLL) under the reference model,\nyielding an NLL sequence. The 7 features are:\n\n\\begin{itemize}[leftmargin=*,nosep]\n\\item \\textbf{Surface features} (2): type--token ratio (TTR) and hapax legomena ratio (hapax\\_ratio)---lexical diversity measures computed directly from the token sequence.\n\\item \\textbf{Reference features} (5): entropy mean, entropy standard deviation, entropy minimum, entropy maximum, and tail decay---summary statistics of the NLL distribution extracted via the reference model.\n\\end{itemize}\n\n\\subsection{Differential Depth Response (DDR)}\n\\label{sec:ddr}\nWe observe that features partition into two behavioral categories as generation depth increases:\n\\begin{itemize}[leftmargin=*,nosep]\n\\item \\textbf{Drifting features}: hapax ratio ($\\rhosp \\approx -0.63$), TTR ($\\rhosp \\approx -0.61$), and entropy mean ($\\rhosp \\approx -0.60$) exhibit strong monotonic decrease with depth.\n\\item \\textbf{Stationary features}: tail decay ($\\rhosp \\approx 0.04$), entropy max ($\\rhosp \\approx 0.05$), and entropy std ($\\rhosp \\approx -0.12$) remain approximately constant.\n\\end{itemize}\nThis differential response is consistent with recursive generation inducing a \\emph{location shift} in the NLL distribution:\ncentral-tendency indicators track this shift and therefore drift,\nwhile shape indicators reflect distributional form and remain stable.\n\n\\subsection{Classification}\n\\label{sec:classification}\nWe train an XGBoost gradient-boosted ensemble on the 7-feature representation.\nFor evaluation, we use leave-one-generator-out (LOGO) cross-validation:\nfor each fold, one generator's data is held out as the test set and the remaining generators form the training set.\nThis ensures no information about the test generator leaks into training.\nWe additionally report leave-one-family-out (LOFO) results,\nwhere all generators from the same model family are held out simultaneously.\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Feature Ablation and DDR Characterization}\n\\label{sec:ablation}\n\nWe first characterize DDR on Pythia-2.8B chains with 5-fold cross-validation.\nTable~\\ref{tab:ablation} shows feature ablation results.\nThe full 7-feature set achieves macro \\fone{} = 0.820 (95\\% CI [0.807, 0.833]),\nsignificantly outperforming both surface-only (0.763; [0.747, 0.774]) and reference-only (0.719; [0.706, 0.733]) subsets.\nSurface features capture stronger individual signals, but reference features provide complementary information\n(McNemar $p \\approx 0$ for full vs.\\ each subset), confirming feature complementarity rather than redundancy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B).}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{N} & \\textbf{Macro \\fone{}} & \\textbf{95\\% CI} \\\\\n\\midrule\nFull & 7 & 0.820 & {[0.807, 0.833]} \\\\\nSurface-only & 2 & 0.763 & {[0.747, 0.774]} \\\\\nReference-only & 5 & 0.719 & {[0.706, 0.733]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:spearman} quantifies DDR with Spearman correlations between each feature and generation depth.\nDrifting features show $|\\rhosp| > 0.60$ with monotonic decrease, while stationary features show $|\\rhosp| < 0.12$.\nPerplexity decreases monotonically with depth (median: 13.50 $\\to$ 4.96 $\\to$ 3.00 $\\to$ 2.07 $\\to$ 1.72),\npre-validating that the reference model captures a progressively more ``expected'' signal at deeper generations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature--depth Spearman correlations (Pythia-2.8B).}\n\\label{tab:spearman}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & $\\rhosp$ & \\textbf{Category} & \\textbf{Trend} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & Drifting & Monotonic decrease \\\\\nTTR & $-0.61$ & Drifting & Monotonic decrease \\\\\nentropy\\_mean & $-0.60$ & Drifting & Monotonic decrease \\\\\nentropy\\_min & $-0.39$ & Intermediate & Moderate decrease \\\\\nentropy\\_std & $-0.12$ & Stationary & Near-flat \\\\\nentropy\\_max & $+0.05$ & Stationary & Near-flat \\\\\ntail\\_decay & $+0.04$ & Stationary & Near-flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate on 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; 18,423 total records)\nunder LOGO cross-validation.\nTable~\\ref{tab:logo} reports per-generator results.\nThe average LOGO macro \\fone{} is 0.804 and the average binary \\fone{} is 0.694,\nwith Pythia-1B held-out highest (binary 0.724) and OLMo-2-1B lowest (binary 0.663).\nThe family-out (LOFO) delta is only 0.011 pp, confirming cross-family generalization.\nFeature importance ranks hapax\\_ratio (0.289) $>$ TTR (0.168) $>$ entropy\\_mean (0.160),\nconsistent with surface drifting features as the primary drivers.\n\n\\begin{table}[t]\n\\centering\n\\caption{LOGO cross-generator evaluation (5 generators).}\n\\label{tab:logo}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Held-out Generator} & \\textbf{Macro \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Gen-1 \\fone{}} \\\\\n\\midrule\nPythia-1B & 0.851 & 0.724 & 0.689 \\\\\nQwen3-0.6B & 0.824 & 0.710 & 0.652 \\\\\nQwen3-1.7B & 0.805 & 0.698 & 0.641 \\\\\nPythia-2.8B & 0.804 & 0.694 & 0.638 \\\\\nOLMo-2-1B & 0.752 & 0.663 & 0.585 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.804} & \\textbf{0.694} & \\textbf{0.641} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare the 7-feature ensemble against existing detection methods repurposed as ordinal depth predictors\n(Table~\\ref{tab:baseline}).\nThe 7-feature ensemble (LOGO \\fone{} = 0.798; 95\\% CI [0.786, 0.799]) significantly outperforms all single-detector baselines\n(bootstrap $p = 0$ for all pairwise comparisons).\nThe strongest baseline, Avg-LogProb (\\fone{} = 0.765), confirms that ordinal depth signal is partially capturable by simple log-probability statistics.\nHowever, the 7-feature ensemble achieves a narrower confidence interval, reflecting more stable cross-generator generalization.\nFastDetectGPT (0.627) and Binoculars (0.579) perform poorly as ordinal predictors because they were designed for binary discrimination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ordinal baseline comparison under LOGO.}\n\\label{tab:baseline}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO \\fone{}} & \\textbf{95\\% CI} & $\\rhosp$ & \\textbf{$\\Delta$ vs 7-feat} \\\\\n\\midrule\n7-feature ensemble & 0.798 & {[0.786, 0.799]} & --- & --- \\\\\nAvg-LogProb & 0.765 & {[0.616, 0.820]} & 0.788 & $-0.033$ \\\\\nLD-Score & 0.721 & {[0.588, 0.770]} & 0.794 & $-0.077$ \\\\\nFastDetectGPT & 0.627 & {[0.511, 0.762]} & 0.433 & $-0.171$ \\\\\nBinoculars & 0.579 & {[0.405, 0.664]} & 0.199 & $-0.219$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Chains and Cross-Reference Validation}\n\\label{sec:cross}\n\n\\paragraph{Cross-model chains.}\nReal-world contamination likely involves heterogeneous generators at each depth step.\nWe construct cross-model chains where different generators produce each successive depth level.\nTable~\\ref{tab:crossmodel} shows that cross-model chains yield \\emph{higher} binary \\fone{} (0.830) than single-model chains (0.694),\na $+$13.6 pp improvement.\nGenerator heterogeneity amplifies distributional discontinuities between depth levels, making depth more discriminable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model vs.\\ single-model chain evaluation.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Binary \\fone{}} & \\textbf{3-class \\fone{}} & \\textbf{N Gen.} \\\\\n\\midrule\nSingle-model LOGO & 0.694 & 0.762 & 8 (homogeneous) \\\\\nCross-model LOGO & 0.830 & 0.789 & 5 (heterogeneous) \\\\\n\\midrule\n$\\Delta$ & $+0.136$ & $+0.027$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-reference model validation.}\nA key concern is whether DDR is an artifact of the Pythia-410M reference model.\nWe extract features using three different reference models (Table~\\ref{tab:crossref}).\nAll three produce negative entropy drift and comparable LOGO \\fone{} (0.803--0.816, $<$1.5 pp range),\nconfirming that DDR is a generation-intrinsic phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-reference-model DDR validation.}\n\\label{tab:crossref}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Reference Model} & \\textbf{LOGO \\fone{}} & \\textbf{entropy\\_mean drift} & \\textbf{DDR} \\\\\n\\midrule\nPythia-410M (default) & 0.803 & {[$-1.19$, $-1.40$]} & \\checkmark \\\\\nOLMo-2-1B & 0.807 & {[$-0.61$, $-0.91$]} & \\checkmark \\\\\nQwen3-0.6B & 0.816 & {[$-0.96$, $-1.35$]} & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DDR Causality Analysis}\n\\label{sec:causality}\n\nTo establish DDR as more than correlational, we conduct three causality tests (Table~\\ref{tab:causality}).\n\n\\paragraph{Permutation importance.} Drifting features have 5.3$\\times$ higher average importance (0.158) than stationary features (0.030),\nconfirming their dominant role in classification.\n\n\\paragraph{Granger causality.} Panel Granger tests ($n = 29{,}095$) show 6/7 features are Granger-significant for depth prediction.\nThe single non-significant feature is entropy\\_min ($p = 0.12$), consistent with its intermediate status.\n\n\\paragraph{Feature intervention.} Single-feature interventions produce a maximum \\fone{} drop of only 0.020,\nindicating that the depth signal is distributed across the drifting feature group rather than concentrated in any single feature.\n\n\\begin{table}[t]\n\\centering\n\\caption{DDR causality analysis.}\n\\label{tab:causality}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Perm.\\ Imp.} & \\textbf{Granger sig.} & \\textbf{Category} \\\\\n\\midrule\nhapax\\_ratio & 0.289 & \\checkmark~($p < 0.001$) & Drifting \\\\\nTTR & 0.168 & \\checkmark~($p < 0.001$) & Drifting \\\\\nentropy\\_mean & 0.160 & \\checkmark~($p < 0.001$) & Drifting \\\\\nentropy\\_max & 0.063 & \\checkmark~($p < 0.01$) & Stationary \\\\\nentropy\\_std & 0.046 & \\checkmark~($p < 0.05$) & Stationary \\\\\nentropy\\_min & 0.015 & $\\times$~($p = 0.12$) & Stationary \\\\\ntail\\_decay & 0.012 & \\checkmark~($p < 0.05$) & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth information can improve downstream training data curation\nby fine-tuning OLMo-1B on depth-stratified subsets (3 seeds each; Table~\\ref{tab:downstream}).\nSize-matched random subsampling (ppl = 2.367) \\emph{outperforms} depth 0--1 filtering (2.387) and binary filtering (2.389).\nTOST equivalence testing confirms statistical equivalence at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$).\nOnly the depth-0-only variant (ppl = 2.681) shows meaningful degradation, attributable to the small sample size (797 vs.\\ 3,951).\nAcross seeds, variance is negligible ($<$0.002 ppl), strengthening the conclusion.\n\nThis negative finding terminates a seemingly plausible research direction:\nalthough depth information is detectable, it has no curative value for data selection.\nDepth fingerprinting is positioned as a \\textbf{diagnostic} tool for provenance characterization.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream CLM perplexity by training data composition (3 seeds, OLMo-1B).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{N train} & \\textbf{Ppl (mean $\\pm$ std)} & \\textbf{$\\Delta$ vs size-matched} \\\\\n\\midrule\nAll data & 12,299 & 2.335 $\\pm$ 0.0003 & $-0.032$ \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.0002 & --- (baseline) \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.0005 & $+0.020$ \\\\\nBinary-filtered & 3,951 & 2.389 $\\pm$ 0.0004 & $+0.022$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.0012 & $+0.314$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruct Model Degradation}\n\\label{sec:instruct}\n\nThe DDR framework is developed and evaluated on base models.\nWe systematically test three instruct-tuned models (Table~\\ref{tab:instruct}).\nPerformance degrades substantially: Qwen3-1.7B LOGO binary \\fone{} drops from 0.821 (base) to 0.658 (instruct), a $-$16.3 pp gap.\nOLMo-2-1B instruct shows 6/7 features with Spearman direction reversal,\nand Llama-3.2-3B instruct reverses 3/7 features.\nInstruction tuning imposes length regulation and format constraints that compress the distributional variation DDR exploits.\nThis is the primary scope limitation: our method currently applies to base models only.\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruct vs.\\ base model DDR comparison.}\n\\label{tab:instruct}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{LOGO Bin.\\ \\fone{}} & \\textbf{3-class \\fone{}} & \\textbf{Feat.\\ Rev.} \\\\\n\\midrule\nQwen3-1.7B & Base & 0.821 & 0.769 & 0 \\\\\nQwen3-1.7B & Instruct & 0.658 & 0.543 & $\\rhosp$ direction \\\\\nOLMo-2-1B & Base & 0.845 & 0.754 & 0 \\\\\nOLMo-2-1B & Instruct & 0.813 & 0.575 & 6/7 \\\\\nLlama-3.2-3B & Base & 0.849 & 0.742 & 0 \\\\\nLlama-3.2-3B & Instruct & 0.838 & 0.544 & 3/7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domains}\n\nTo assess ecological validity, we evaluate on seeds from 4 domains (500 seeds/domain $\\times$ 5 depths; Table~\\ref{tab:domains}).\nAll non-Wikipedia domains achieve binary \\fone{} in the range 0.739--0.754,\nwith a maximum inter-domain gap of only 1.5 pp (excluding the Wikipedia baseline at 0.815).\nAcademic text is hardest (0.739) due to higher intrinsic vocabulary diversity;\ncode is easiest (0.754) due to bimodal entropy distributions that amplify DDR.\nAll confidence intervals exclude 0.5, confirming significant depth signal across all domains.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain evaluation.}\n\\label{tab:domains}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary \\fone{}} & \\textbf{95\\% CI} & \\textbf{3-class \\fone{}} \\\\\n\\midrule\nWikipedia (baseline) & 0.815 & {[0.799, 0.831]} & 0.863 \\\\\nCode & 0.754 & {[0.737, 0.770]} & 0.634 \\\\\nNews & 0.746 & {[0.726, 0.764]} & 0.652 \\\\\nAcademic & 0.739 & {[0.720, 0.757]} & 0.622 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Large-Scale Generator}\n\\label{sec:large_scale}\n\nWe add Qwen3-8B-Base to test DDR at frontier scale (Table~\\ref{tab:largescale}).\nWith 6 generators, the average LOGO \\fone{} is 0.789 ($-$1.1 pp vs.\\ 5-gen baseline of 0.800).\nQwen3-8B held-out \\fone{} is 0.683---lower than average but still well above chance.\nHigher-capacity models compress feature margins (hapax $\\rhosp = -0.558$ vs.\\ $-0.63$ for smaller models)\nbut the DDR pattern (drifting vs.\\ stationary) is fully preserved.\n\n\\begin{table}[t]\n\\centering\n\\caption{6-generator LOGO with Qwen3-8B.}\n\\label{tab:largescale}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{LOGO \\fone{}} & \\textbf{hapax $\\rhosp$} & \\textbf{Scale} \\\\\n\\midrule\nPythia-1B & 0.856 & $-0.65$ & 1.0B \\\\\nQwen3-0.6B & 0.824 & $-0.63$ & 0.6B \\\\\nQwen3-1.7B & 0.805 & $-0.61$ & 1.7B \\\\\nPythia-2.8B & 0.804 & $-0.63$ & 2.8B \\\\\nOLMo-2-1B & 0.764 & $-0.60$ & 1.5B \\\\\nQwen3-8B & 0.683 & $-0.56$ & 8.0B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{DDR as location shift.}\nThe differential behavior of drifting vs.\\ stationary features is consistent with a location-shift model:\nrecursive generation shifts the NLL distribution's central tendency (lower perplexity, reduced diversity)\nwhile approximately preserving its shape (tail behavior, maximum entropy).\nThis is not a new theoretical contribution---it follows from known properties of recursive distributional transformation---but\nthe empirical validation across 8 generators, 5 families, 4 domains, and 3 prompt types is novel.\n\n\\paragraph{Practical implications.}\nThe cross-model chain result (binary \\fone{} = 0.830) is encouraging for real-world deployment,\nwhere contamination chains likely involve heterogeneous generators.\nThe 7-feature ensemble requires only a single 410M reference model forward pass,\nmaking it substantially cheaper than QLoRA-based classifiers ($\\sim$15$\\times$ inference cost advantage; Appendix~\\ref{app:qlora}).\n\n\\paragraph{Limitations.}\n(1) \\textbf{Base models only}: instruct-tuned models show $-$16.3 pp degradation (Qwen) with feature direction reversal.\n(2) \\textbf{Temperature sensitivity}: signal degrades at $t > 0.9$ (Appendix~\\ref{app:temp}).\n(3) \\textbf{3-class resolution ceiling}: 5-class \\fone{} drops to $\\sim$0.50; ordinal methods offer no improvement (Appendix~\\ref{app:ordinal}).\n(4) \\textbf{Scale effect}: larger generators (8B) show moderate degradation (held-out \\fone{} = 0.683).\n(5) \\textbf{Prompt-type dependence}: continuation chains show stronger drift (\\fone{} = 0.781) than elaboration (0.730; Appendix~\\ref{app:prompt}).\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formulated generation depth classification as a new task beyond binary AI-text detection\nand characterized Differential Depth Response (DDR) in non-paraphrastic LLM generation chains.\nA lightweight 7-feature ensemble achieves leak-free binary \\fone{} = 0.694 under 8-generator LOGO evaluation\n(per-generator range: 0.633--0.724) and 0.830 on cross-model chains.\nDDR is validated as a genuine empirical phenomenon through causality analysis (6/7 Granger-significant features, 5.3$\\times$ permutation importance gap)\nand cross-reference model validation (3 reference models, $<$1.5 pp variance).\nDepth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality,\nestablishing depth fingerprinting as a diagnostic tool for provenance characterization.\nThe signal degrades under instruction tuning and high sampling temperatures,\ndefining clear scope boundaries for future work on extending DDR to broader generation settings.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Briesch et~al.(2025)]{briesch2025llmbrokenphone}\nBriesch, M., Sobania, D., and Rothlauf, F.\n\\newblock Large language models as broken telephone: Paraphrastic chains and attractor convergence.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024collapse}\nDohmatob, E., Feng, Y., and Recht, B.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock \\emph{arXiv preprint arXiv:2402.07043}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nHans, A., Schwarzschild, A., Cherepanova, V., Kazemi, H., Saha, A., Goldblum, M., Geiping, J., and Goldstein, T.\n\\newblock Spotting {LLM}s with {B}inoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock {D}etect{GPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024modelcollapse}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nTulchinskii, E., Kuznetsov, K., Kushnareva, L., Cherniavskii, D., Barannikov, S., Piontkovskaya, I., Nikolenko, S., and Burnaev, E.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Tweedie and Baayen(1998)]{tweedie1998variable}\nTweedie, F.~J. and Baayen, R.~H.\n\\newblock How variable may a constant be? {M}easures of lexical richness in perspective.\n\\newblock \\emph{Computers and the Humanities}, 32(5):323--352, 1998.\n\n\\bibitem[Wenzek et~al.(2019)]{wenzek2019ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock {CCN}et: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2019.\n\n\\bibitem[Yang et~al.(2024)]{yang2024dnagpt}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock {DNA-GPT}: Divergent {N}-gram analysis with {LLM} probability curvature for machine-generated text detection.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\clearpage\n\\appendix\n\n\\section{Multi-Detector Ensemble}\n\\label{app:ensemble}\n\nWe compare the 7-feature ensemble against a multi-detector ensemble combining 4 detectors (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) plus surface features (Table~\\ref{tab:ensemble}).\nThe multi-detector ensemble achieves a marginal improvement of $+$2.1 pp (3-class) and $+$0.3 pp (binary) at 2.4$\\times$ inference cost and 3.2$\\times$ GPU memory.\nThe binary \\fone{} gap (0.3 pp) is essentially negligible, confirming that the gen-1/gen-2+ boundary is an intrinsic bottleneck that additional features cannot overcome.\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-detector ensemble comparison.}\n\\label{tab:ensemble}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Cost Ratio} \\\\\n\\midrule\n7-feature ensemble & 0.774 & 0.705 & 1.0$\\times$ \\\\\n4-det + surface & 0.795 & 0.708 & 2.4$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{app:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4; Table~\\ref{tab:ordinal}).\nAll methods---standard XGBoost, CORAL, and Frank-Hall---achieve only $\\sim$0.50 \\fone{}, a $-$26 pp drop from 3-class.\nThe bottleneck is the gen-1/gen-2 boundary, which concentrates 86\\% of binary false negatives.\nGen-3 vs.\\ gen-4 is nearly indistinguishable (\\fone{} $\\approx$ 0.35).\nOrdinal methods provide no improvement over standard classification, confirming that the resolution ceiling is at 3 classes---a feature-space limitation, not a methodological one.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ordinal classification results.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-class \\fone{}} & \\textbf{5-class \\fone{}} & $\\Delta$ \\\\\n\\midrule\nXGBoost (standard) & 0.762 & 0.500 & $-0.262$ \\\\\nCORAL & 0.758 & 0.490 & $-0.268$ \\\\\nFrank-Hall & 0.760 & 0.500 & $-0.260$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Temperature Sensitivity}\n\\label{app:temp}\n\nTable~\\ref{tab:temp} shows that DDR is reliable within $t \\in [0.5, 0.7]$ but degrades substantially at $t = 0.9$.\nThe entropy\\_mean Spearman $\\rhosp$ drops from $-0.600$ (at $t = 0.7$) to $-0.302$ (at $t = 0.9$):\nhigh-temperature sampling noise drowns out the deterministic depth-wise drift component.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature sensitivity.}\n\\label{tab:temp}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Temperature} & \\textbf{Within-CV Bin.\\ \\fone{}} & \\textbf{LOGO Bin.\\ \\fone{}} & \\textbf{entropy\\_mean $\\rhosp$} \\\\\n\\midrule\n0.5 & 0.843 & 0.814 & $-0.584$ \\\\\n0.7 (default) & 0.947 & 0.694 & $-0.600$ \\\\\n0.9 & 0.582 & 0.480 & $-0.302$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Human Edit Robustness}\n\\label{app:edit}\n\nTable~\\ref{tab:edit} shows graceful degradation under simulated human editing.\nAt 5\\% random word replacement, binary \\fone{} drops only 4.6 pp.\nLLM rephrasing (average 1.69 sentences replaced, 50.7\\% edit distance) produces a comparable drop ($-$4.5 pp),\nsuggesting that LLM editing does not introduce out-of-distribution perturbations in feature space.\nEven at 20\\% replacement, performance remains above random (\\fone{} = 0.591).\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to text editing.}\n\\label{tab:edit}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\textbf{vs baseline} \\\\\n\\midrule\nNo editing (baseline) & 0.695 & --- \\\\\n5\\% random replacement & 0.650 & $-0.046$ \\\\\n10\\% random replacement & 0.614 & $-0.081$ \\\\\n20\\% random replacement & 0.591 & $-0.104$ \\\\\nLLM rephrase (avg 1.69 sent) & 0.647 & $-0.045$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{LD-Score Augmentation}\n\\label{app:ld}\n\nAdding LD-Score as an 8th feature yields a marginal improvement of $+$0.5 pp (Table~\\ref{tab:ld}).\nLD-Score alone achieves LOGO \\fone{} = 0.721 (Spearman $\\rhosp = -0.794$ with depth),\nconfirming character-level information partially captures depth signal but is highly correlated with existing reference features.\nWe retain the 7-feature set as the primary model for simplicity.\n\n\\begin{table}[h]\n\\centering\n\\caption{LD-Score augmentation.}\n\\label{tab:ld}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{LOGO \\fone{}} & $\\Delta$ \\\\\n\\midrule\n7-feature (default) & 0.798 & --- \\\\\n7-feature + LD-Score & 0.803 & $+0.005$ \\\\\nLD-Score only & 0.721 & $-0.077$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{End-to-End QLoRA Classifier}\n\\label{app:qlora}\n\nTable~\\ref{tab:qlora} compares QLoRA fine-tuned models against the 7-feature ensemble.\nQLoRA models achieve 3-class \\fone{} of 0.859--0.907, surpassing the 7-feature ensemble by 10--15 pp.\nHowever, the 5-class ceiling persists (\\fone{} $\\approx$ 0.60), confirming that the resolution limit is task-intrinsic rather than feature-engineering-specific.\nQLoRA inference costs $\\sim$15$\\times$ more than the 7-feature pipeline (which requires only a single 410M forward pass),\npositioning the 7-feature ensemble on efficiency advantage.\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end QLoRA vs.\\ 7-feature ensemble.}\n\\label{tab:qlora}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{5-class \\fone{}} \\\\\n\\midrule\nQwen3-1.7B (instruct) & QLoRA & 0.907 & 0.867 & 0.551 \\\\\nOLMo-1B (instruct) & QLoRA & 0.888 & 0.836 & 0.598 \\\\\nQwen3-1.7B (base) & QLoRA & 0.904 & 0.860 & 0.554 \\\\\nOLMo-1B (base) & QLoRA & 0.859 & 0.793 & 0.540 \\\\\n\\midrule\n7-feature ensemble & XGBoost & 0.762 & 0.694 & 0.500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Text Length Confound Control}\n\\label{app:length}\n\nText length shows weak correlation with depth (Spearman $\\rhosp \\in [-0.066, +0.134]$), ruling it out as a primary confound.\nLength-normalized features (TTR, hapax computed on fixed-length windows) preserve and even strengthen DDR trends.\nLength-matched evaluation (Table~\\ref{tab:length}) shows a $-$4.6 pp drop (0.770 $\\to$ 0.724), but a random subsample control drops by the same amount,\nconfirming this reflects deconfounding rather than information loss.\n\n\\begin{table}[h]\n\\centering\n\\caption{Length confound analysis.}\n\\label{tab:length}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\textbf{vs unmatched} \\\\\n\\midrule\nUnmatched (full) & 0.770 & --- \\\\\nLength-matched & 0.724 & $-0.046$ \\\\\nRandom subsample control & 0.724 & $-0.046$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{9-Generator Scale Evaluation}\n\\label{app:9gen}\n\nExtending to 9 generators (adding Gemma-2-2B, Llama-3.2-3B, Mistral-7B-v0.3; 42,015 total records),\nLOGO 3-class \\fone{} is 0.751 ($-$1.9 pp vs.\\ 8-gen; Table~\\ref{tab:9gen}).\nGemma-2-2B is a notable outlier (3-class 0.628, binary 0.440) due to SentencePiece tokenizer mismatch with the BPE-based reference model.\nMistral-7B (3-class 0.605) reflects 7B-scale signal compression.\nExcluding the Gemma anomaly, all generators exceed \\fone{} = 0.60.\n\n\\begin{table}[h]\n\\centering\n\\caption{9-generator per-generator LOGO \\fone{}.}\n\\label{tab:9gen}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Family} \\\\\n\\midrule\nPythia-1B & 0.857 & 0.724 & Pythia \\\\\nQwen3-0.6B & 0.819 & 0.710 & Qwen \\\\\nPythia-2.8B & 0.812 & 0.700 & Pythia \\\\\nQwen3-1.7B & 0.811 & 0.698 & Qwen \\\\\nOLMo-2-1B & 0.773 & 0.663 & OLMo \\\\\nLlama-3.2-3B & 0.759 & 0.680 & Llama \\\\\nQwen3-8B & 0.696 & 0.647 & Qwen \\\\\nGemma-2-2B & 0.628 & 0.440 & Gemma \\\\\nMistral-7B-v0.3 & 0.605 & 0.633 & Mistral \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prompt Type and Chain Type Comparison}\n\\label{app:prompt}\n\n\\paragraph{Prompt types.}\nTable~\\ref{tab:prompt} compares three prompt types on Pythia-2.8B.\nContinuation shows the strongest within-type signal (CV \\fone{} = 0.781) but lowest depth retention (83.1\\%),\nwhile elaboration has the highest retention (98.6\\%) but weakest signal (0.730).\nThis is consistent with the DDR location-shift interpretation: stronger semantic constraints narrow the output distribution, reducing cross-depth variation.\nLeave-one-prompt-type-out (LOPTO) average \\fone{} is 0.753, only 0.4 pp below within-type average, indicating high cross-prompt-type transferability.\n\n\\begin{table}[h]\n\\centering\n\\caption{Prompt-type comparison (Pythia-2.8B).}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt Type} & \\textbf{CV \\fone{}} & \\textbf{LOPTO \\fone{}} & \\textbf{Retention} & \\textbf{hapax $\\rhosp$} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.74$ \\\\\nInspired rewriting & 0.737 & 0.733 & 0.939 & $-0.80$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.83$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs.\\ non-paraphrastic chains.}\nTable~\\ref{tab:para} compares continuation and paraphrasing chains.\nParaphrasing chains show substantially weaker depth signal (CV \\fone{} = 0.62 vs.\\ 0.781, $-$16.1 pp)\nbecause semantic-preservation constraints induce attractor convergence by depth 2,\nsuppressing the distributional drift that DDR exploits.\nThis validates the task formulation: depth estimation is meaningful specifically for non-paraphrastic chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ non-paraphrastic chains.}\n\\label{tab:para}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{CV \\fone{}} & \\textbf{hapax $\\rhosp$} & \\textbf{entropy\\_mean $\\rhosp$} & \\textbf{Retention} \\\\\n\\midrule\nContinuation & 0.781 & $-0.74$ & $-0.56$ & 0.831 \\\\\nParaphrasing & 0.620 & $-0.25$ & $-0.18$ & 0.970 \\\\\n\\midrule\n$\\Delta$ & $-0.161$ & $+0.49$ & $+0.38$ & $+0.139$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{TOST Bootstrap Stationarity Test}\n\\label{app:tost}\n\nWe use Two One-Sided Tests (TOST) with 1,000 bootstrap iterations and equivalence margin $d = 0.2$\nto formally test feature stationarity (Table~\\ref{tab:tost}).\nThree features (entropy\\_max, entropy\\_min, tail\\_decay) are confirmed stationary (100\\% rejection rate, median $|d| < 0.1$).\nentropy\\_std is rejected (median $d = 0.458$, 0\\% rejection rate), classifying it as an intermediate ``weak drifter''\ndespite its low Spearman $\\rhosp$ ($-0.12$).\nThis refines the DDR taxonomy: 3 strong drifters + 3 true stationary + 1 intermediate.\n\n\\begin{table}[h]\n\\centering\n\\caption{TOST bootstrap stationarity test.}\n\\label{tab:tost}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Median $d$} & \\textbf{TOST $p$} & \\textbf{Rej.\\ Rate} & \\textbf{Status} \\\\\n\\midrule\nentropy\\_max & 0.062 & 0.000 & 1.000 & Stationary \\checkmark \\\\\nentropy\\_min & $-0.016$ & 0.000 & 1.000 & Stationary \\checkmark \\\\\ntail\\_decay & 0.088 & 0.000 & 1.000 & Stationary \\checkmark \\\\\nentropy\\_std & 0.458 & 1.000 & 0.000 & Intermediate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Independent Seed Validation}\n\\label{app:seed}\n\nTo rule out seed-sharing leakage, we evaluate with independent seed sets per generator (Table~\\ref{tab:seed}).\nThe average binary \\fone{} (0.680) differs from shared-seed LOGO (0.694) by only 1.4 pp,\nwithin bootstrap confidence intervals, confirming that shared seeds do not inflate performance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Independent vs.\\ shared seed evaluation.}\n\\label{tab:seed}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\\\\n\\midrule\nShared seed LOGO & 0.694 & --- \\\\\nIndependent seed (Pythia$\\to$OLMo) & 0.695 & $+0.001$ \\\\\nIndependent seed (OLMo$\\to$Pythia) & 0.666 & $-0.028$ \\\\\nIndependent seed avg & 0.680 & $-0.014$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Topic Drift Control}\n\\label{app:topic}\n\nSemantic similarity (cosine) increases monotonically with depth (0.622 $\\to$ 0.683 $\\to$ 0.801 $\\to$ 0.859; Table~\\ref{tab:topic}),\nindicating that deeper generations converge semantically.\nHowever, DDR feature--depth correlations remain significant after controlling for semantic similarity,\nand shape features show near-zero correlation with similarity ($|\\rhosp| < 0.17$),\nconfirming that DDR is not merely a proxy for topic drift.\n\n\\begin{table}[h]\n\\centering\n\\caption{Semantic similarity by depth transition.}\n\\label{tab:topic}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Transition} & \\textbf{Mean Similarity} & \\textbf{Std} \\\\\n\\midrule\ndepth 0 $\\to$ 1 & 0.622 & 0.165 \\\\\ndepth 1 $\\to$ 2 & 0.683 & 0.184 \\\\\ndepth 2 $\\to$ 3 & 0.801 & 0.201 \\\\\ndepth 3 $\\to$ 4 & 0.859 & 0.190 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9be6289-f2ad-4a02-88fe-8a924f95d855",
  "isSidechain": false,
  "requestId": "req_011CbDfMtGjcR2tKk8LwahMd",
  "type": "assistant",
  "uuid": "8d9a2862-1e8f-4d49-af3f-0da1f888a31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T8kDum9Wf5memJEKwmStXy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6067,
      "cache_read_input_tokens": 48921,
      "output_tokens": 17656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17656,
          "cache_read_input_tokens": 48921,
          "cache_creation_input_tokens": 6067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6067
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

_source line 25 · 2026-05-20T10:32:44.744Z_

<details><summary>↩ Tool result · `toolu_0135mD7ySDYZiPqepZ6kMxUG`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d9a2862-1e8f-4d49-af3f-0da1f888a31d",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "346d9b0a-f9f5-4328-a824-6ef49c1071d6",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{enumitem}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\newcommand{\\fone}{F\\textsubscript{1}}\n\\newcommand{\\pval}{\\textit{p}}\n\\newcommand{\\rhosp}{\\rho}\n\n\\title{Generation Depth Fingerprinting via Differential Depth Response\\\\in Non-Paraphrastic LLM Chains}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain LLM-generated text of unknown provenance depth.\nCurrent detection methods offer only binary real-vs-synthetic classification, conflating qualitatively different material:\nfirst-generation text retains much of the source distribution's lexical properties, while deeper recursive generations exhibit measurably reduced vocabulary diversity and compressed perplexity.\nWe formulate \\textbf{generation depth classification} (gen-0 / gen-1 / gen-2+) as a new task beyond binary detection\nand characterize \\textbf{Differential Depth Response} (DDR):\ncentral-tendency features (entropy mean, type--token ratio, hapax ratio) drift monotonically with depth,\nwhile shape features (entropy max, tail decay) remain near-stationary---consistent with recursive generation inducing a location shift in the NLL distribution while approximately preserving distributional shape.\nOn 8 base-model generators from 5 families (0.6B--8B), a lightweight 7-feature ensemble achieves\nleak-free binary \\fone{} = 0.694 under leave-one-generator-out (LOGO) evaluation\nand 0.830 on cross-model chains, using a single 410M reference model.\nCausality analysis confirms DDR with 6/7 Granger-significant features and a 5.3$\\times$ permutation importance gap between drifting and stationary features.\nDepth-aware data curation is statistically equivalent to random subsampling for downstream causal language model quality\n(TOST \\pval{} = 1.1$\\times$10$^{-4}$ at $\\pm$2\\% margin),\nestablishing depth fingerprinting as a \\emph{diagnostic} tool for provenance characterization, not a curative tool for data selection.\nThe signal degrades substantially under instruction tuning, restricting current scope to base models.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models (LLMs) now generate text that is increasingly difficult to distinguish from human-written content.\nAs LLM-generated text proliferates on the web---estimates suggest 7--17\\% of recent scientific papers contain substantial AI-generated content---it inevitably re-enters training corpora for subsequent models.\nThis creates recursive generation chains: a human writes a seed text (generation depth 0),\nan LLM produces a continuation (depth 1), another LLM may further elaborate on that output (depth 2), and so on.\nUnderstanding where a given text sits along this chain---its \\emph{generation depth}---is crucial for data governance,\ntraining corpus curation, and understanding the feedback loops that drive model collapse.\n\nExisting AI-text detectors frame the problem as binary classification: human vs.\\ machine.\nMethods such as DetectGPT \\citep{mitchell2023detectgpt}, FastDetectGPT \\citep{bao2024fastdetectgpt}, Binoculars \\citep{hans2024binoculars}, and LD-Score \\citep{tulchinskii2024ldscore}\nachieve strong binary discrimination but cannot distinguish first-generation text from deeper recursive generations.\nThis conflation matters: gen-1 text retains substantial distributional similarity to its human source,\nwhile gen-2+ text exhibits measurably compressed vocabulary diversity and perplexity---qualitatively different material that may differentially affect downstream model quality.\nSeparately, work on paraphrastic chains \\citep{briesch2025llmbrokenphone} has shown attractor convergence behavior limiting depth discriminability to approximately 3 classes,\nbut this depends on semantic-preservation constraints absent in non-paraphrastic continuation chains.\n\nIn this paper, we formulate \\textbf{generation depth classification} as a new task and characterize the distributional signatures that enable it.\nWe introduce the concept of \\textbf{Differential Depth Response} (DDR):\nwhen text is recursively generated through non-paraphrastic chains,\ncentral-tendency and diversity features of the token-level negative log-likelihood (NLL) distribution\n(entropy mean, type--token ratio, hapax ratio) \\emph{drift} monotonically with depth,\nwhile shape features (entropy max, tail decay) remain \\emph{near-stationary}.\nThis is consistent with recursive generation inducing a location shift in the NLL distribution while approximately preserving distributional shape.\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n\\item \\textbf{Task formulation.} We define generation depth classification (gen-0/gen-1/gen-2+) as a tractable ordinal classification problem beyond binary detection. No prior work addresses depth estimation in non-paraphrastic continuation chains.\n\n\\item \\textbf{Empirical characterization of DDR.} We validate DDR across 8 base-model generators from 5 model families (Pythia, OLMo, Qwen, Llama, Mistral; 0.6B--8B scale), 3 prompt types, and 4 text domains. A 7-feature ensemble achieves leak-free binary \\fone{} = 0.694 under LOGO and 0.830 on cross-model chains. Causality analysis (6/7 Granger-significant features, 5.3$\\times$ permutation importance gap) confirms DDR as a genuine empirical phenomenon beyond vocabulary impoverishment.\n\n\\item \\textbf{Negative finding on downstream utility.} Depth-aware data curation does not improve downstream CLM quality compared to random subsampling (TOST equivalence confirmed at $\\pm$2\\% margin). Depth fingerprinting is a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{enumerate}\n\nWe transparently report scope limitations: the signal degrades substantially under instruction tuning and high sampling temperatures ($t > 0.9$), and 5-class ordinal resolution is not achievable with current features (ceiling at 3 classes).\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Perplexity-based AI-text detection.}\nStatistical detection methods leverage the observation that LLM-generated text occupies lower-perplexity regions of the model's output distribution.\nDetectGPT \\citep{mitchell2023detectgpt} uses perturbation-based log-probability curvature;\nFastDetectGPT \\citep{bao2024fastdetectgpt} replaces perturbations with conditional probability sampling for efficiency.\nBinoculars \\citep{hans2024binoculars} compares cross-entropy ratios between two models.\nGLTR \\citep{gehrmann2019gltr} visualizes token-level statistics.\nDNA-GPT \\citep{yang2024dnagpt} employs divergent continuation comparison.\nAll operate as binary classifiers; none address ordinal depth estimation.\n\n\\paragraph{Distributional signatures and LD-Score.}\n\\citet{tulchinskii2024ldscore} propose character-level distributional signatures (LD-Score) for authorship verification and AI detection, demonstrating that distributional divergence at the character level captures stylistic fingerprints. We incorporate LD-Score as both a baseline and an augmentation feature (Appendix~\\ref{app:ld}).\n\n\\paragraph{Model collapse and recursive generation.}\nTheoretical work on model collapse \\citep{shumailov2024modelcollapse} predicts that recursive training on synthetic data leads to distributional narrowing and eventual mode collapse.\n\\citet{dohmatob2024collapse} formalize the rate of distributional degradation.\nOur work complements this line by providing an empirical method to \\emph{detect} the depth signature of recursive generation in individual texts, rather than studying the aggregate distributional consequences for model training.\n\n\\paragraph{Iterative generation chains.}\n\\citet{briesch2025llmbrokenphone} study paraphrastic LLM chains and find attractor convergence limiting depth discriminability to approximately 3 semantic clusters. Our work studies non-paraphrastic chains (continuation, elaboration), where the absence of semantic-preservation constraints allows distributional drift to persist to deeper levels.\n\n\\paragraph{Vocabulary diversity and stylometry.}\nType--token ratio (TTR), hapax legomena ratio, and entropy-based measures have a long history in computational stylometry and authorship attribution \\citep{tweedie1998variable}. We repurpose these as depth-discriminative features and show they capture the ``drifting'' component of DDR.\n\n\\paragraph{Data quality and curation.}\nPerplexity-based filtering \\citep{wenzek2019ccnet} and quality classifiers are standard in training data pipelines. Our Claim~3 (negative finding) directly tests whether depth information adds value to such curation, finding it does not.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\nGiven a text $x$, we aim to predict its \\emph{generation depth} $d \\in \\{0, 1, 2+\\}$,\nwhere $d=0$ denotes human-written seed text, $d=1$ denotes first-generation LLM output from a human seed,\nand $d=2+$ denotes text produced at depth $\\geq 2$ in a recursive generation chain.\nThe primary evaluation metric is \\textbf{leak-free binary \\fone{}}: the \\fone{} for discriminating gen-1 from gen-2+,\nexcluding gen-0 samples to avoid inflated performance from seed-sharing cues.\n\n\\subsection{Chain Construction}\n\\label{sec:chains}\nWe construct recursive generation chains of depth 0--4 using base-model LLMs.\nGiven a human-written seed text $x_0$ (depth 0), we prompt a generator $G$ to produce $x_1 = G(x_0)$ (depth 1),\nthen $x_2 = G(x_1)$ (depth 2), and so on up to $x_4$.\nWe evaluate three prompt types: \\emph{continuation} (unconstrained generation),\n\\emph{elaboration} (expand on the input), and \\emph{inspired rewriting} (write new text inspired by the input).\nSeed texts are drawn from four domains: Wikipedia, news, academic, and code.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\nWe extract 7 features from each text using a reference language model (Pythia-410M by default).\nFor each token $t_i$ in the text, we compute its negative log-likelihood (NLL) under the reference model,\nyielding an NLL sequence. The 7 features are:\n\n\\begin{itemize}[leftmargin=*,nosep]\n\\item \\textbf{Surface features} (2): type--token ratio (TTR) and hapax legomena ratio (hapax\\_ratio)---lexical diversity measures computed directly from the token sequence.\n\\item \\textbf{Reference features} (5): entropy mean, entropy standard deviation, entropy minimum, entropy maximum, and tail decay---summary statistics of the NLL distribution extracted via the reference model.\n\\end{itemize}\n\n\\subsection{Differential Depth Response (DDR)}\n\\label{sec:ddr}\nWe observe that features partition into two behavioral categories as generation depth increases:\n\\begin{itemize}[leftmargin=*,nosep]\n\\item \\textbf{Drifting features}: hapax ratio ($\\rhosp \\approx -0.63$), TTR ($\\rhosp \\approx -0.61$), and entropy mean ($\\rhosp \\approx -0.60$) exhibit strong monotonic decrease with depth.\n\\item \\textbf{Stationary features}: tail decay ($\\rhosp \\approx 0.04$), entropy max ($\\rhosp \\approx 0.05$), and entropy std ($\\rhosp \\approx -0.12$) remain approximately constant.\n\\end{itemize}\nThis differential response is consistent with recursive generation inducing a \\emph{location shift} in the NLL distribution:\ncentral-tendency indicators track this shift and therefore drift,\nwhile shape indicators reflect distributional form and remain stable.\n\n\\subsection{Classification}\n\\label{sec:classification}\nWe train an XGBoost gradient-boosted ensemble on the 7-feature representation.\nFor evaluation, we use leave-one-generator-out (LOGO) cross-validation:\nfor each fold, one generator's data is held out as the test set and the remaining generators form the training set.\nThis ensures no information about the test generator leaks into training.\nWe additionally report leave-one-family-out (LOFO) results,\nwhere all generators from the same model family are held out simultaneously.\n\n% ============================================================\n% 4. EXPERIMENTS\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Feature Ablation and DDR Characterization}\n\\label{sec:ablation}\n\nWe first characterize DDR on Pythia-2.8B chains with 5-fold cross-validation.\nTable~\\ref{tab:ablation} shows feature ablation results.\nThe full 7-feature set achieves macro \\fone{} = 0.820 (95\\% CI [0.807, 0.833]),\nsignificantly outperforming both surface-only (0.763; [0.747, 0.774]) and reference-only (0.719; [0.706, 0.733]) subsets.\nSurface features capture stronger individual signals, but reference features provide complementary information\n(McNemar $p \\approx 0$ for full vs.\\ each subset), confirming feature complementarity rather than redundancy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature ablation (5-fold CV, Pythia-2.8B).}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{N} & \\textbf{Macro \\fone{}} & \\textbf{95\\% CI} \\\\\n\\midrule\nFull & 7 & 0.820 & {[0.807, 0.833]} \\\\\nSurface-only & 2 & 0.763 & {[0.747, 0.774]} \\\\\nReference-only & 5 & 0.719 & {[0.706, 0.733]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:spearman} quantifies DDR with Spearman correlations between each feature and generation depth.\nDrifting features show $|\\rhosp| > 0.60$ with monotonic decrease, while stationary features show $|\\rhosp| < 0.12$.\nPerplexity decreases monotonically with depth (median: 13.50 $\\to$ 4.96 $\\to$ 3.00 $\\to$ 2.07 $\\to$ 1.72),\npre-validating that the reference model captures a progressively more ``expected'' signal at deeper generations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Feature--depth Spearman correlations (Pythia-2.8B).}\n\\label{tab:spearman}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & $\\rhosp$ & \\textbf{Category} & \\textbf{Trend} \\\\\n\\midrule\nhapax\\_ratio & $-0.63$ & Drifting & Monotonic decrease \\\\\nTTR & $-0.61$ & Drifting & Monotonic decrease \\\\\nentropy\\_mean & $-0.60$ & Drifting & Monotonic decrease \\\\\nentropy\\_min & $-0.39$ & Intermediate & Moderate decrease \\\\\nentropy\\_std & $-0.12$ & Stationary & Near-flat \\\\\nentropy\\_max & $+0.05$ & Stationary & Near-flat \\\\\ntail\\_decay & $+0.04$ & Stationary & Near-flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Generator Generalization}\n\\label{sec:cross_gen}\n\nWe evaluate on 5 generators (Pythia-2.8B, Pythia-1B, OLMo-2-1B, Qwen3-1.7B, Qwen3-0.6B; 18,423 total records)\nunder LOGO cross-validation.\nTable~\\ref{tab:logo} reports per-generator results.\nThe average LOGO macro \\fone{} is 0.804 and the average binary \\fone{} is 0.694,\nwith Pythia-1B held-out highest (binary 0.724) and OLMo-2-1B lowest (binary 0.663).\nThe family-out (LOFO) delta is only 0.011 pp, confirming cross-family generalization.\nFeature importance ranks hapax\\_ratio (0.289) $>$ TTR (0.168) $>$ entropy\\_mean (0.160),\nconsistent with surface drifting features as the primary drivers.\n\n\\begin{table}[t]\n\\centering\n\\caption{LOGO cross-generator evaluation (5 generators).}\n\\label{tab:logo}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Held-out Generator} & \\textbf{Macro \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Gen-1 \\fone{}} \\\\\n\\midrule\nPythia-1B & 0.851 & 0.724 & 0.689 \\\\\nQwen3-0.6B & 0.824 & 0.710 & 0.652 \\\\\nQwen3-1.7B & 0.805 & 0.698 & 0.641 \\\\\nPythia-2.8B & 0.804 & 0.694 & 0.638 \\\\\nOLMo-2-1B & 0.752 & 0.663 & 0.585 \\\\\n\\midrule\n\\textbf{Average} & \\textbf{0.804} & \\textbf{0.694} & \\textbf{0.641} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Baseline Comparison}\n\\label{sec:baselines}\n\nWe compare the 7-feature ensemble against existing detection methods repurposed as ordinal depth predictors\n(Table~\\ref{tab:baseline}).\nThe 7-feature ensemble (LOGO \\fone{} = 0.798; 95\\% CI [0.786, 0.799]) significantly outperforms all single-detector baselines\n(bootstrap $p = 0$ for all pairwise comparisons).\nThe strongest baseline, Avg-LogProb (\\fone{} = 0.765), confirms that ordinal depth signal is partially capturable by simple log-probability statistics.\nHowever, the 7-feature ensemble achieves a narrower confidence interval, reflecting more stable cross-generator generalization.\nFastDetectGPT (0.627) and Binoculars (0.579) perform poorly as ordinal predictors because they were designed for binary discrimination.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ordinal baseline comparison under LOGO.}\n\\label{tab:baseline}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO \\fone{}} & \\textbf{95\\% CI} & $\\rhosp$ & \\textbf{$\\Delta$ vs 7-feat} \\\\\n\\midrule\n7-feature ensemble & 0.798 & {[0.786, 0.799]} & --- & --- \\\\\nAvg-LogProb & 0.765 & {[0.616, 0.820]} & 0.788 & $-0.033$ \\\\\nLD-Score & 0.721 & {[0.588, 0.770]} & 0.794 & $-0.077$ \\\\\nFastDetectGPT & 0.627 & {[0.511, 0.762]} & 0.433 & $-0.171$ \\\\\nBinoculars & 0.579 & {[0.405, 0.664]} & 0.199 & $-0.219$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Chains and Cross-Reference Validation}\n\\label{sec:cross}\n\n\\paragraph{Cross-model chains.}\nReal-world contamination likely involves heterogeneous generators at each depth step.\nWe construct cross-model chains where different generators produce each successive depth level.\nTable~\\ref{tab:crossmodel} shows that cross-model chains yield \\emph{higher} binary \\fone{} (0.830) than single-model chains (0.694),\na $+$13.6 pp improvement.\nGenerator heterogeneity amplifies distributional discontinuities between depth levels, making depth more discriminable.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model vs.\\ single-model chain evaluation.}\n\\label{tab:crossmodel}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Binary \\fone{}} & \\textbf{3-class \\fone{}} & \\textbf{N Gen.} \\\\\n\\midrule\nSingle-model LOGO & 0.694 & 0.762 & 8 (homogeneous) \\\\\nCross-model LOGO & 0.830 & 0.789 & 5 (heterogeneous) \\\\\n\\midrule\n$\\Delta$ & $+0.136$ & $+0.027$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-reference model validation.}\nA key concern is whether DDR is an artifact of the Pythia-410M reference model.\nWe extract features using three different reference models (Table~\\ref{tab:crossref}).\nAll three produce negative entropy drift and comparable LOGO \\fone{} (0.803--0.816, $<$1.5 pp range),\nconfirming that DDR is a generation-intrinsic phenomenon.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-reference-model DDR validation.}\n\\label{tab:crossref}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Reference Model} & \\textbf{LOGO \\fone{}} & \\textbf{entropy\\_mean drift} & \\textbf{DDR} \\\\\n\\midrule\nPythia-410M (default) & 0.803 & {[$-1.19$, $-1.40$]} & \\checkmark \\\\\nOLMo-2-1B & 0.807 & {[$-0.61$, $-0.91$]} & \\checkmark \\\\\nQwen3-0.6B & 0.816 & {[$-0.96$, $-1.35$]} & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{DDR Causality Analysis}\n\\label{sec:causality}\n\nTo establish DDR as more than correlational, we conduct three causality tests (Table~\\ref{tab:causality}).\n\n\\paragraph{Permutation importance.} Drifting features have 5.3$\\times$ higher average importance (0.158) than stationary features (0.030),\nconfirming their dominant role in classification.\n\n\\paragraph{Granger causality.} Panel Granger tests ($n = 29{,}095$) show 6/7 features are Granger-significant for depth prediction.\nThe single non-significant feature is entropy\\_min ($p = 0.12$), consistent with its intermediate status.\n\n\\paragraph{Feature intervention.} Single-feature interventions produce a maximum \\fone{} drop of only 0.020,\nindicating that the depth signal is distributed across the drifting feature group rather than concentrated in any single feature.\n\n\\begin{table}[t]\n\\centering\n\\caption{DDR causality analysis.}\n\\label{tab:causality}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Perm.\\ Imp.} & \\textbf{Granger sig.} & \\textbf{Category} \\\\\n\\midrule\nhapax\\_ratio & 0.289 & \\checkmark~($p < 0.001$) & Drifting \\\\\nTTR & 0.168 & \\checkmark~($p < 0.001$) & Drifting \\\\\nentropy\\_mean & 0.160 & \\checkmark~($p < 0.001$) & Drifting \\\\\nentropy\\_max & 0.063 & \\checkmark~($p < 0.01$) & Stationary \\\\\nentropy\\_std & 0.046 & \\checkmark~($p < 0.05$) & Stationary \\\\\nentropy\\_min & 0.015 & $\\times$~($p = 0.12$) & Stationary \\\\\ntail\\_decay & 0.012 & \\checkmark~($p < 0.05$) & Stationary \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:downstream}\n\nWe test whether depth information can improve downstream training data curation\nby fine-tuning OLMo-1B on depth-stratified subsets (3 seeds each; Table~\\ref{tab:downstream}).\nSize-matched random subsampling (ppl = 2.367) \\emph{outperforms} depth 0--1 filtering (2.387) and binary filtering (2.389).\nTOST equivalence testing confirms statistical equivalence at $\\pm$2\\% margin ($p = 1.1 \\times 10^{-4}$).\nOnly the depth-0-only variant (ppl = 2.681) shows meaningful degradation, attributable to the small sample size (797 vs.\\ 3,951).\nAcross seeds, variance is negligible ($<$0.002 ppl), strengthening the conclusion.\n\nThis negative finding terminates a seemingly plausible research direction:\nalthough depth information is detectable, it has no curative value for data selection.\nDepth fingerprinting is positioned as a \\textbf{diagnostic} tool for provenance characterization.\n\n\\begin{table}[t]\n\\centering\n\\caption{Downstream CLM perplexity by training data composition (3 seeds, OLMo-1B).}\n\\label{tab:downstream}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{N train} & \\textbf{Ppl (mean $\\pm$ std)} & \\textbf{$\\Delta$ vs size-matched} \\\\\n\\midrule\nAll data & 12,299 & 2.335 $\\pm$ 0.0003 & $-0.032$ \\\\\nSize-matched random & 3,951 & 2.367 $\\pm$ 0.0002 & --- (baseline) \\\\\nDepth 0+1 only & 3,951 & 2.387 $\\pm$ 0.0005 & $+0.020$ \\\\\nBinary-filtered & 3,951 & 2.389 $\\pm$ 0.0004 & $+0.022$ \\\\\nDepth 0 only & 797 & 2.681 $\\pm$ 0.0012 & $+0.314$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Instruct Model Degradation}\n\\label{sec:instruct}\n\nThe DDR framework is developed and evaluated on base models.\nWe systematically test three instruct-tuned models (Table~\\ref{tab:instruct}).\nPerformance degrades substantially: Qwen3-1.7B LOGO binary \\fone{} drops from 0.821 (base) to 0.658 (instruct), a $-$16.3 pp gap.\nOLMo-2-1B instruct shows 6/7 features with Spearman direction reversal,\nand Llama-3.2-3B instruct reverses 3/7 features.\nInstruction tuning imposes length regulation and format constraints that compress the distributional variation DDR exploits.\nThis is the primary scope limitation: our method currently applies to base models only.\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruct vs.\\ base model DDR comparison.}\n\\label{tab:instruct}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{LOGO Bin.\\ \\fone{}} & \\textbf{3-class \\fone{}} & \\textbf{Feat.\\ Rev.} \\\\\n\\midrule\nQwen3-1.7B & Base & 0.821 & 0.769 & 0 \\\\\nQwen3-1.7B & Instruct & 0.658 & 0.543 & $\\rhosp$ direction \\\\\nOLMo-2-1B & Base & 0.845 & 0.754 & 0 \\\\\nOLMo-2-1B & Instruct & 0.813 & 0.575 & 6/7 \\\\\nLlama-3.2-3B & Base & 0.849 & 0.742 & 0 \\\\\nLlama-3.2-3B & Instruct & 0.838 & 0.544 & 3/7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Domain Evaluation}\n\\label{sec:domains}\n\nTo assess ecological validity, we evaluate on seeds from 4 domains (500 seeds/domain $\\times$ 5 depths; Table~\\ref{tab:domains}).\nAll non-Wikipedia domains achieve binary \\fone{} in the range 0.739--0.754,\nwith a maximum inter-domain gap of only 1.5 pp (excluding the Wikipedia baseline at 0.815).\nAcademic text is hardest (0.739) due to higher intrinsic vocabulary diversity;\ncode is easiest (0.754) due to bimodal entropy distributions that amplify DDR.\nAll confidence intervals exclude 0.5, confirming significant depth signal across all domains.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-domain evaluation.}\n\\label{tab:domains}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Binary \\fone{}} & \\textbf{95\\% CI} & \\textbf{3-class \\fone{}} \\\\\n\\midrule\nWikipedia (baseline) & 0.815 & {[0.799, 0.831]} & 0.863 \\\\\nCode & 0.754 & {[0.737, 0.770]} & 0.634 \\\\\nNews & 0.746 & {[0.726, 0.764]} & 0.652 \\\\\nAcademic & 0.739 & {[0.720, 0.757]} & 0.622 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Large-Scale Generator}\n\\label{sec:large_scale}\n\nWe add Qwen3-8B-Base to test DDR at frontier scale (Table~\\ref{tab:largescale}).\nWith 6 generators, the average LOGO \\fone{} is 0.789 ($-$1.1 pp vs.\\ 5-gen baseline of 0.800).\nQwen3-8B held-out \\fone{} is 0.683---lower than average but still well above chance.\nHigher-capacity models compress feature margins (hapax $\\rhosp = -0.558$ vs.\\ $-0.63$ for smaller models)\nbut the DDR pattern (drifting vs.\\ stationary) is fully preserved.\n\n\\begin{table}[t]\n\\centering\n\\caption{6-generator LOGO with Qwen3-8B.}\n\\label{tab:largescale}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{LOGO \\fone{}} & \\textbf{hapax $\\rhosp$} & \\textbf{Scale} \\\\\n\\midrule\nPythia-1B & 0.856 & $-0.65$ & 1.0B \\\\\nQwen3-0.6B & 0.824 & $-0.63$ & 0.6B \\\\\nQwen3-1.7B & 0.805 & $-0.61$ & 1.7B \\\\\nPythia-2.8B & 0.804 & $-0.63$ & 2.8B \\\\\nOLMo-2-1B & 0.764 & $-0.60$ & 1.5B \\\\\nQwen3-8B & 0.683 & $-0.56$ & 8.0B \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{DDR as location shift.}\nThe differential behavior of drifting vs.\\ stationary features is consistent with a location-shift model:\nrecursive generation shifts the NLL distribution's central tendency (lower perplexity, reduced diversity)\nwhile approximately preserving its shape (tail behavior, maximum entropy).\nThis is not a new theoretical contribution---it follows from known properties of recursive distributional transformation---but\nthe empirical validation across 8 generators, 5 families, 4 domains, and 3 prompt types is novel.\n\n\\paragraph{Practical implications.}\nThe cross-model chain result (binary \\fone{} = 0.830) is encouraging for real-world deployment,\nwhere contamination chains likely involve heterogeneous generators.\nThe 7-feature ensemble requires only a single 410M reference model forward pass,\nmaking it substantially cheaper than QLoRA-based classifiers ($\\sim$15$\\times$ inference cost advantage; Appendix~\\ref{app:qlora}).\n\n\\paragraph{Limitations.}\n(1) \\textbf{Base models only}: instruct-tuned models show $-$16.3 pp degradation (Qwen) with feature direction reversal.\n(2) \\textbf{Temperature sensitivity}: signal degrades at $t > 0.9$ (Appendix~\\ref{app:temp}).\n(3) \\textbf{3-class resolution ceiling}: 5-class \\fone{} drops to $\\sim$0.50; ordinal methods offer no improvement (Appendix~\\ref{app:ordinal}).\n(4) \\textbf{Scale effect}: larger generators (8B) show moderate degradation (held-out \\fone{} = 0.683).\n(5) \\textbf{Prompt-type dependence}: continuation chains show stronger drift (\\fone{} = 0.781) than elaboration (0.730; Appendix~\\ref{app:prompt}).\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe formulated generation depth classification as a new task beyond binary AI-text detection\nand characterized Differential Depth Response (DDR) in non-paraphrastic LLM generation chains.\nA lightweight 7-feature ensemble achieves leak-free binary \\fone{} = 0.694 under 8-generator LOGO evaluation\n(per-generator range: 0.633--0.724) and 0.830 on cross-model chains.\nDDR is validated as a genuine empirical phenomenon through causality analysis (6/7 Granger-significant features, 5.3$\\times$ permutation importance gap)\nand cross-reference model validation (3 reference models, $<$1.5 pp variance).\nDepth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality,\nestablishing depth fingerprinting as a diagnostic tool for provenance characterization.\nThe signal degrades under instruction tuning and high sampling temperatures,\ndefining clear scope boundaries for future work on extending DDR to broader generation settings.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nBao, G., Zhao, Y., Teng, Z., Yang, L., and Zhang, Y.\n\\newblock Fast-{D}etect{GPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Briesch et~al.(2025)]{briesch2025llmbrokenphone}\nBriesch, M., Sobania, D., and Rothlauf, F.\n\\newblock Large language models as broken telephone: Paraphrastic chains and attractor convergence.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024collapse}\nDohmatob, E., Feng, Y., and Recht, B.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock \\emph{arXiv preprint arXiv:2402.07043}, 2024.\n\n\\bibitem[Gehrmann et~al.(2019)]{gehrmann2019gltr}\nGehrmann, S., Strobelt, H., and Rush, A.\n\\newblock {GLTR}: Statistical detection and visualization of generated text.\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nHans, A., Schwarzschild, A., Cherepanova, V., Kazemi, H., Saha, A., Goldblum, M., Geiping, J., and Goldstein, T.\n\\newblock Spotting {LLM}s with {B}inoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nMitchell, E., Lee, Y., Khazatsky, A., Manning, C.~D., and Finn, C.\n\\newblock {D}etect{GPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024modelcollapse}\nShumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., and Anderson, R.\n\\newblock The curse of recursion: Training on generated data makes models forget.\n\\newblock \\emph{Nature}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024ldscore}\nTulchinskii, E., Kuznetsov, K., Kushnareva, L., Cherniavskii, D., Barannikov, S., Piontkovskaya, I., Nikolenko, S., and Burnaev, E.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Tweedie and Baayen(1998)]{tweedie1998variable}\nTweedie, F.~J. and Baayen, R.~H.\n\\newblock How variable may a constant be? {M}easures of lexical richness in perspective.\n\\newblock \\emph{Computers and the Humanities}, 32(5):323--352, 1998.\n\n\\bibitem[Wenzek et~al.(2019)]{wenzek2019ccnet}\nWenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm{\\'a}n, F., Joulin, A., and Grave, E.\n\\newblock {CCN}et: Extracting high quality monolingual datasets from web crawl data.\n\\newblock In \\emph{LREC}, 2019.\n\n\\bibitem[Yang et~al.(2024)]{yang2024dnagpt}\nYang, X., Cheng, W., Petzold, L., Wang, W.~Y., and Chen, H.\n\\newblock {DNA-GPT}: Divergent {N}-gram analysis with {LLM} probability curvature for machine-generated text detection.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\clearpage\n\\appendix\n\n\\section{Multi-Detector Ensemble}\n\\label{app:ensemble}\n\nWe compare the 7-feature ensemble against a multi-detector ensemble combining 4 detectors (FastDetectGPT, Binoculars, LD-Score, Avg-LogProb) plus surface features (Table~\\ref{tab:ensemble}).\nThe multi-detector ensemble achieves a marginal improvement of $+$2.1 pp (3-class) and $+$0.3 pp (binary) at 2.4$\\times$ inference cost and 3.2$\\times$ GPU memory.\nThe binary \\fone{} gap (0.3 pp) is essentially negligible, confirming that the gen-1/gen-2+ boundary is an intrinsic bottleneck that additional features cannot overcome.\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-detector ensemble comparison.}\n\\label{tab:ensemble}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Cost Ratio} \\\\\n\\midrule\n7-feature ensemble & 0.774 & 0.705 & 1.0$\\times$ \\\\\n4-det + surface & 0.795 & 0.708 & 2.4$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Finer-Grained Ordinal Classification}\n\\label{app:ordinal}\n\nWe test 5-class ordinal classification (gen-0 through gen-4; Table~\\ref{tab:ordinal}).\nAll methods---standard XGBoost, CORAL, and Frank-Hall---achieve only $\\sim$0.50 \\fone{}, a $-$26 pp drop from 3-class.\nThe bottleneck is the gen-1/gen-2 boundary, which concentrates 86\\% of binary false negatives.\nGen-3 vs.\\ gen-4 is nearly indistinguishable (\\fone{} $\\approx$ 0.35).\nOrdinal methods provide no improvement over standard classification, confirming that the resolution ceiling is at 3 classes---a feature-space limitation, not a methodological one.\n\n\\begin{table}[h]\n\\centering\n\\caption{Ordinal classification results.}\n\\label{tab:ordinal}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{3-class \\fone{}} & \\textbf{5-class \\fone{}} & $\\Delta$ \\\\\n\\midrule\nXGBoost (standard) & 0.762 & 0.500 & $-0.262$ \\\\\nCORAL & 0.758 & 0.490 & $-0.268$ \\\\\nFrank-Hall & 0.760 & 0.500 & $-0.260$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Temperature Sensitivity}\n\\label{app:temp}\n\nTable~\\ref{tab:temp} shows that DDR is reliable within $t \\in [0.5, 0.7]$ but degrades substantially at $t = 0.9$.\nThe entropy\\_mean Spearman $\\rhosp$ drops from $-0.600$ (at $t = 0.7$) to $-0.302$ (at $t = 0.9$):\nhigh-temperature sampling noise drowns out the deterministic depth-wise drift component.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temperature sensitivity.}\n\\label{tab:temp}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Temperature} & \\textbf{Within-CV Bin.\\ \\fone{}} & \\textbf{LOGO Bin.\\ \\fone{}} & \\textbf{entropy\\_mean $\\rhosp$} \\\\\n\\midrule\n0.5 & 0.843 & 0.814 & $-0.584$ \\\\\n0.7 (default) & 0.947 & 0.694 & $-0.600$ \\\\\n0.9 & 0.582 & 0.480 & $-0.302$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Human Edit Robustness}\n\\label{app:edit}\n\nTable~\\ref{tab:edit} shows graceful degradation under simulated human editing.\nAt 5\\% random word replacement, binary \\fone{} drops only 4.6 pp.\nLLM rephrasing (average 1.69 sentences replaced, 50.7\\% edit distance) produces a comparable drop ($-$4.5 pp),\nsuggesting that LLM editing does not introduce out-of-distribution perturbations in feature space.\nEven at 20\\% replacement, performance remains above random (\\fone{} = 0.591).\n\n\\begin{table}[h]\n\\centering\n\\caption{Robustness to text editing.}\n\\label{tab:edit}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\textbf{vs baseline} \\\\\n\\midrule\nNo editing (baseline) & 0.695 & --- \\\\\n5\\% random replacement & 0.650 & $-0.046$ \\\\\n10\\% random replacement & 0.614 & $-0.081$ \\\\\n20\\% random replacement & 0.591 & $-0.104$ \\\\\nLLM rephrase (avg 1.69 sent) & 0.647 & $-0.045$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{LD-Score Augmentation}\n\\label{app:ld}\n\nAdding LD-Score as an 8th feature yields a marginal improvement of $+$0.5 pp (Table~\\ref{tab:ld}).\nLD-Score alone achieves LOGO \\fone{} = 0.721 (Spearman $\\rhosp = -0.794$ with depth),\nconfirming character-level information partially captures depth signal but is highly correlated with existing reference features.\nWe retain the 7-feature set as the primary model for simplicity.\n\n\\begin{table}[h]\n\\centering\n\\caption{LD-Score augmentation.}\n\\label{tab:ld}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{LOGO \\fone{}} & $\\Delta$ \\\\\n\\midrule\n7-feature (default) & 0.798 & --- \\\\\n7-feature + LD-Score & 0.803 & $+0.005$ \\\\\nLD-Score only & 0.721 & $-0.077$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{End-to-End QLoRA Classifier}\n\\label{app:qlora}\n\nTable~\\ref{tab:qlora} compares QLoRA fine-tuned models against the 7-feature ensemble.\nQLoRA models achieve 3-class \\fone{} of 0.859--0.907, surpassing the 7-feature ensemble by 10--15 pp.\nHowever, the 5-class ceiling persists (\\fone{} $\\approx$ 0.60), confirming that the resolution limit is task-intrinsic rather than feature-engineering-specific.\nQLoRA inference costs $\\sim$15$\\times$ more than the 7-feature pipeline (which requires only a single 410M forward pass),\npositioning the 7-feature ensemble on efficiency advantage.\n\n\\begin{table}[h]\n\\centering\n\\caption{End-to-end QLoRA vs.\\ 7-feature ensemble.}\n\\label{tab:qlora}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Type} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{5-class \\fone{}} \\\\\n\\midrule\nQwen3-1.7B (instruct) & QLoRA & 0.907 & 0.867 & 0.551 \\\\\nOLMo-1B (instruct) & QLoRA & 0.888 & 0.836 & 0.598 \\\\\nQwen3-1.7B (base) & QLoRA & 0.904 & 0.860 & 0.554 \\\\\nOLMo-1B (base) & QLoRA & 0.859 & 0.793 & 0.540 \\\\\n\\midrule\n7-feature ensemble & XGBoost & 0.762 & 0.694 & 0.500 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Text Length Confound Control}\n\\label{app:length}\n\nText length shows weak correlation with depth (Spearman $\\rhosp \\in [-0.066, +0.134]$), ruling it out as a primary confound.\nLength-normalized features (TTR, hapax computed on fixed-length windows) preserve and even strengthen DDR trends.\nLength-matched evaluation (Table~\\ref{tab:length}) shows a $-$4.6 pp drop (0.770 $\\to$ 0.724), but a random subsample control drops by the same amount,\nconfirming this reflects deconfounding rather than information loss.\n\n\\begin{table}[h]\n\\centering\n\\caption{Length confound analysis.}\n\\label{tab:length}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\textbf{vs unmatched} \\\\\n\\midrule\nUnmatched (full) & 0.770 & --- \\\\\nLength-matched & 0.724 & $-0.046$ \\\\\nRandom subsample control & 0.724 & $-0.046$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{9-Generator Scale Evaluation}\n\\label{app:9gen}\n\nExtending to 9 generators (adding Gemma-2-2B, Llama-3.2-3B, Mistral-7B-v0.3; 42,015 total records),\nLOGO 3-class \\fone{} is 0.751 ($-$1.9 pp vs.\\ 8-gen; Table~\\ref{tab:9gen}).\nGemma-2-2B is a notable outlier (3-class 0.628, binary 0.440) due to SentencePiece tokenizer mismatch with the BPE-based reference model.\nMistral-7B (3-class 0.605) reflects 7B-scale signal compression.\nExcluding the Gemma anomaly, all generators exceed \\fone{} = 0.60.\n\n\\begin{table}[h]\n\\centering\n\\caption{9-generator per-generator LOGO \\fone{}.}\n\\label{tab:9gen}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{3-class \\fone{}} & \\textbf{Binary \\fone{}} & \\textbf{Family} \\\\\n\\midrule\nPythia-1B & 0.857 & 0.724 & Pythia \\\\\nQwen3-0.6B & 0.819 & 0.710 & Qwen \\\\\nPythia-2.8B & 0.812 & 0.700 & Pythia \\\\\nQwen3-1.7B & 0.811 & 0.698 & Qwen \\\\\nOLMo-2-1B & 0.773 & 0.663 & OLMo \\\\\nLlama-3.2-3B & 0.759 & 0.680 & Llama \\\\\nQwen3-8B & 0.696 & 0.647 & Qwen \\\\\nGemma-2-2B & 0.628 & 0.440 & Gemma \\\\\nMistral-7B-v0.3 & 0.605 & 0.633 & Mistral \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prompt Type and Chain Type Comparison}\n\\label{app:prompt}\n\n\\paragraph{Prompt types.}\nTable~\\ref{tab:prompt} compares three prompt types on Pythia-2.8B.\nContinuation shows the strongest within-type signal (CV \\fone{} = 0.781) but lowest depth retention (83.1\\%),\nwhile elaboration has the highest retention (98.6\\%) but weakest signal (0.730).\nThis is consistent with the DDR location-shift interpretation: stronger semantic constraints narrow the output distribution, reducing cross-depth variation.\nLeave-one-prompt-type-out (LOPTO) average \\fone{} is 0.753, only 0.4 pp below within-type average, indicating high cross-prompt-type transferability.\n\n\\begin{table}[h]\n\\centering\n\\caption{Prompt-type comparison (Pythia-2.8B).}\n\\label{tab:prompt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Prompt Type} & \\textbf{CV \\fone{}} & \\textbf{LOPTO \\fone{}} & \\textbf{Retention} & \\textbf{hapax $\\rhosp$} \\\\\n\\midrule\nContinuation & 0.781 & 0.762 & 0.831 & $-0.74$ \\\\\nInspired rewriting & 0.737 & 0.733 & 0.939 & $-0.80$ \\\\\nElaboration & 0.730 & 0.762 & 0.986 & $-0.83$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Paraphrastic vs.\\ non-paraphrastic chains.}\nTable~\\ref{tab:para} compares continuation and paraphrasing chains.\nParaphrasing chains show substantially weaker depth signal (CV \\fone{} = 0.62 vs.\\ 0.781, $-$16.1 pp)\nbecause semantic-preservation constraints induce attractor convergence by depth 2,\nsuppressing the distributional drift that DDR exploits.\nThis validates the task formulation: depth estimation is meaningful specifically for non-paraphrastic chains.\n\n\\begin{table}[h]\n\\centering\n\\caption{Paraphrastic vs.\\ non-paraphrastic chains.}\n\\label{tab:para}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{CV \\fone{}} & \\textbf{hapax $\\rhosp$} & \\textbf{entropy\\_mean $\\rhosp$} & \\textbf{Retention} \\\\\n\\midrule\nContinuation & 0.781 & $-0.74$ & $-0.56$ & 0.831 \\\\\nParaphrasing & 0.620 & $-0.25$ & $-0.18$ & 0.970 \\\\\n\\midrule\n$\\Delta$ & $-0.161$ & $+0.49$ & $+0.38$ & $+0.139$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{TOST Bootstrap Stationarity Test}\n\\label{app:tost}\n\nWe use Two One-Sided Tests (TOST) with 1,000 bootstrap iterations and equivalence margin $d = 0.2$\nto formally test feature stationarity (Table~\\ref{tab:tost}).\nThree features (entropy\\_max, entropy\\_min, tail\\_decay) are confirmed stationary (100\\% rejection rate, median $|d| < 0.1$).\nentropy\\_std is rejected (median $d = 0.458$, 0\\% rejection rate), classifying it as an intermediate ``weak drifter''\ndespite its low Spearman $\\rhosp$ ($-0.12$).\nThis refines the DDR taxonomy: 3 strong drifters + 3 true stationary + 1 intermediate.\n\n\\begin{table}[h]\n\\centering\n\\caption{TOST bootstrap stationarity test.}\n\\label{tab:tost}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature} & \\textbf{Median $d$} & \\textbf{TOST $p$} & \\textbf{Rej.\\ Rate} & \\textbf{Status} \\\\\n\\midrule\nentropy\\_max & 0.062 & 0.000 & 1.000 & Stationary \\checkmark \\\\\nentropy\\_min & $-0.016$ & 0.000 & 1.000 & Stationary \\checkmark \\\\\ntail\\_decay & 0.088 & 0.000 & 1.000 & Stationary \\checkmark \\\\\nentropy\\_std & 0.458 & 1.000 & 0.000 & Intermediate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Independent Seed Validation}\n\\label{app:seed}\n\nTo rule out seed-sharing leakage, we evaluate with independent seed sets per generator (Table~\\ref{tab:seed}).\nThe average binary \\fone{} (0.680) differs from shared-seed LOGO (0.694) by only 1.4 pp,\nwithin bootstrap confidence intervals, confirming that shared seeds do not inflate performance.\n\n\\begin{table}[h]\n\\centering\n\\caption{Independent vs.\\ shared seed evaluation.}\n\\label{tab:seed}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Binary \\fone{}} & $\\Delta$ \\\\\n\\midrule\nShared seed LOGO & 0.694 & --- \\\\\nIndependent seed (Pythia$\\to$OLMo) & 0.695 & $+0.001$ \\\\\nIndependent seed (OLMo$\\to$Pythia) & 0.666 & $-0.028$ \\\\\nIndependent seed avg & 0.680 & $-0.014$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Topic Drift Control}\n\\label{app:topic}\n\nSemantic similarity (cosine) increases monotonically with depth (0.622 $\\to$ 0.683 $\\to$ 0.801 $\\to$ 0.859; Table~\\ref{tab:topic}),\nindicating that deeper generations converge semantically.\nHowever, DDR feature--depth correlations remain significant after controlling for semantic similarity,\nand shape features show near-zero correlation with similarity ($|\\rhosp| < 0.17$),\nconfirming that DDR is not merely a proxy for topic drift.\n\n\\begin{table}[h]\n\\centering\n\\caption{Semantic similarity by depth transition.}\n\\label{tab:topic}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Transition} & \\textbf{Mean Similarity} & \\textbf{Std} \\\\\n\\midrule\ndepth 0 $\\to$ 1 & 0.622 & 0.165 \\\\\ndepth 1 $\\to$ 2 & 0.683 & 0.184 \\\\\ndepth 2 $\\to$ 3 & 0.801 & 0.201 \\\\\ndepth 3 $\\to$ 4 & 0.859 & 0.190 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d9a2862-1e8f-4d49-af3f-0da1f888a31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "346d9b0a-f9f5-4328-a824-6ef49c1071d6",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from dream data",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Assistant

_source line 28 · 2026-05-20T10:32:48.715Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "346d9b0a-f9f5-4328-a824-6ef49c1071d6",
  "isSidechain": false,
  "requestId": "req_011CbDfjynyz81844cktZ461",
  "type": "assistant",
  "uuid": "d21d9083-e8e9-41b3-85aa-9075ca664d6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jNmxe5qo5MJm34yRncgyU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17723,
      "cache_read_input_tokens": 54988,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 54988,
          "cache_creation_input_tokens": 17723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17723
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

_source line 29 · 2026-05-20T10:32:49.968Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WmYPxskan8MjLT2Q4xyvNB`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d21d9083-e8e9-41b3-85aa-9075ca664d6d",
  "isSidechain": false,
  "requestId": "req_011CbDfjynyz81844cktZ461",
  "type": "assistant",
  "uuid": "7b3ff367-12d0-44d3-972b-973e8e1e17d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jNmxe5qo5MJm34yRncgyU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17723,
      "cache_read_input_tokens": 54988,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 54988,
          "cache_creation_input_tokens": 17723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17723
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

_source line 30 · 2026-05-20T10:32:50.970Z_

<details><summary>↩ Tool result · `toolu_01WmYPxskan8MjLT2Q4xyvNB`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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

Package natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on
 input line 64.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on 
input line 64.


Package natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in
put line 64.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o
n input line 64.


Package natbib Warning: Citation `briesch2025llmbrokenphone' on page 1 undefine
d on input line 68.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 98.


Package natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on 
input line 99.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 100.


Package natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu
t line 101.


Package natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input 
line 102.


Package natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o
n input line 106.


LaTeX Warning: Reference `app:ld' on page 2 undefined on input line 106.


Package natbib Warning: Citation `shumailov2024modelcollapse' on page 2 undefin
ed on input line 109.


Package natbib Warning: Citation `dohmatob2024collapse' on page 2 undefined on 
input line 110.


Package natbib Warning: Citation `briesch2025llmbrokenphone' on page 2 undefine
d on input line 114.


Package natbib Warning: Citation `tweedie1998variable' on page 2 undefined on i
nput line 117.


Package natbib Warning: Citation `wenzek2019ccnet' on page 2 undefined on input
 line 120.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 185.

[3]

LaTeX Warning: Reference `tab:spearman' on page 4 undefined on input line 206.


LaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 235.


LaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 265.

[4]

LaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 295
.


LaTeX Warning: Reference `tab:crossref' on page 5 undefined on input line 317.


LaTeX Warning: Reference `tab:causality' on page 5 undefined on input line 339.



LaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 373
.

[5]

LaTeX Warning: Reference `tab:instruct' on page 6 undefined on input line 404.


LaTeX Warning: Reference `tab:domains' on page 6 undefined on input line 432.


LaTeX Warning: Reference `tab:largescale' on page 6 undefined on input line 458
.

[6]

LaTeX Warning: Reference `app:qlora' on page 7 undefined on input line 499.


LaTeX Warning: Reference `app:temp' on page 7 undefined on input line 503.


LaTeX Warning: Reference `app:ordinal' on page 7 undefined on input line 504.


LaTeX Warning: Reference `app:prompt' on page 7 undefined on input line 506.

[7] [8] [9]

LaTeX Warning: Reference `tab:ensemble' on page 10 undefined on input line 598.



LaTeX Warning: Reference `tab:ordinal' on page 10 undefined on input line 619.


LaTeX Warning: Reference `tab:temp' on page 10 undefined on input line 643.


LaTeX Warning: Reference `tab:edit' on page 10 undefined on input line 665.

[10]

LaTeX Warning: Reference `tab:ld' on page 11 undefined on input line 691.


LaTeX Warning: Reference `tab:qlora' on page 11 undefined on input line 714.


LaTeX Warning: Reference `tab:length' on page 11 undefined on input line 743.

[11]

LaTeX Warning: Reference `tab:9gen' on page 12 undefined on input line 765.


LaTeX Warning: Reference `tab:prompt' on page 12 undefined on input line 796.


Overfull \hbox (0.55602pt too wide) in paragraph at lines 796--801
 []\T1/ptm/b/n/10.95 Prompt types.[] \T1/ptm/m/n/10.95 Ta-ble [] com-pares thre
e prompt types on Pythia-2.8B. Con-tin-u-a-tion shows the strongest

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:para' on page 12 undefined on input line 818.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:tost' on page 12 undefined on input line 844.

[12]

LaTeX Warning: Reference `tab:seed' on page 13 undefined on input line 869.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:topic' on page 13 undefined on input line 892.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[13] [14] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 172672 bytes).
Transcript written on paper.log.
LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[13] [14] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (14 pages, 177452 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b3ff367-12d0-44d3-972b-973e8e1e17d5",
  "isSidechain": false,
  "promptId": "d06b0b55-9496-4158-b925-b3d3a1da1086",
  "type": "user",
  "uuid": "3f5b6c7a-623d-448a-adf0-de67cd7c4c88",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on\n input line 64.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on \ninput line 64.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in\nput line 64.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 1 undefined o\nn input line 64.\n\n\nPackage natbib Warning: Citation `briesch2025llmbrokenphone' on page 1 undefine\nd on input line 68.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 98.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on \ninput line 99.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 100.\n\n\nPackage natbib Warning: Citation `gehrmann2019gltr' on page 2 undefined on inpu\nt line 101.\n\n\nPackage natbib Warning: Citation `yang2024dnagpt' on page 2 undefined on input \nline 102.\n\n\nPackage natbib Warning: Citation `tulchinskii2024ldscore' on page 2 undefined o\nn input line 106.\n\n\nLaTeX Warning: Reference `app:ld' on page 2 undefined on input line 106.\n\n\nPackage natbib Warning: Citation `shumailov2024modelcollapse' on page 2 undefin\ned on input line 109.\n\n\nPackage natbib Warning: Citation `dohmatob2024collapse' on page 2 undefined on \ninput line 110.\n\n\nPackage natbib Warning: Citation `briesch2025llmbrokenphone' on page 2 undefine\nd on input line 114.\n\n\nPackage natbib Warning: Citation `tweedie1998variable' on page 2 undefined on i\nnput line 117.\n\n\nPackage natbib Warning: Citation `wenzek2019ccnet' on page 2 undefined on input\n line 120.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:ablation' on page 3 undefined on input line 185.\n\n[3]\n\nLaTeX Warning: Reference `tab:spearman' on page 4 undefined on input line 206.\n\n\nLaTeX Warning: Reference `tab:logo' on page 4 undefined on input line 235.\n\n\nLaTeX Warning: Reference `tab:baseline' on page 4 undefined on input line 265.\n\n[4]\n\nLaTeX Warning: Reference `tab:crossmodel' on page 5 undefined on input line 295\n.\n\n\nLaTeX Warning: Reference `tab:crossref' on page 5 undefined on input line 317.\n\n\nLaTeX Warning: Reference `tab:causality' on page 5 undefined on input line 339.\n\n\n\nLaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 373\n.\n\n[5]\n\nLaTeX Warning: Reference `tab:instruct' on page 6 undefined on input line 404.\n\n\nLaTeX Warning: Reference `tab:domains' on page 6 undefined on input line 432.\n\n\nLaTeX Warning: Reference `tab:largescale' on page 6 undefined on input line 458\n.\n\n[6]\n\nLaTeX Warning: Reference `app:qlora' on page 7 undefined on input line 499.\n\n\nLaTeX Warning: Reference `app:temp' on page 7 undefined on input line 503.\n\n\nLaTeX Warning: Reference `app:ordinal' on page 7 undefined on input line 504.\n\n\nLaTeX Warning: Reference `app:prompt' on page 7 undefined on input line 506.\n\n[7] [8] [9]\n\nLaTeX Warning: Reference `tab:ensemble' on page 10 undefined on input line 598.\n\n\n\nLaTeX Warning: Reference `tab:ordinal' on page 10 undefined on input line 619.\n\n\nLaTeX Warning: Reference `tab:temp' on page 10 undefined on input line 643.\n\n\nLaTeX Warning: Reference `tab:edit' on page 10 undefined on input line 665.\n\n[10]\n\nLaTeX Warning: Reference `tab:ld' on page 11 undefined on input line 691.\n\n\nLaTeX Warning: Reference `tab:qlora' on page 11 undefined on input line 714.\n\n\nLaTeX Warning: Reference `tab:length' on page 11 undefined on input line 743.\n\n[11]\n\nLaTeX Warning: Reference `tab:9gen' on page 12 undefined on input line 765.\n\n\nLaTeX Warning: Reference `tab:prompt' on page 12 undefined on input line 796.\n\n\nOverfull \\hbox (0.55602pt too wide) in paragraph at lines 796--801\n []\\T1/ptm/b/n/10.95 Prompt types.[] \\T1/ptm/m/n/10.95 Ta-ble [] com-pares thre\ne prompt types on Pythia-2.8B. Con-tin-u-a-tion shows the strongest\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:para' on page 12 undefined on input line 818.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:tost' on page 12 undefined on input line 844.\n\n[12]\n\nLaTeX Warning: Reference `tab:seed' on page 13 undefined on input line 869.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:topic' on page 13 undefined on input line 892.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[13] [14] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 172672 bytes).\nTranscript written on paper.log.\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[13] [14] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (14 pages, 177452 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7b3ff367-12d0-44d3-972b-973e8e1e17d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T10:32:50.973Z_

```json
{
  "parentUuid": "3f5b6c7a-623d-448a-adf0-de67cd7c4c88",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1d4b84ce-8150-4a93-9d1b-8dddfcbf83b3",
  "timestamp": "2026-05-20T10:32:50.973Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 32 · 2026-05-20T10:33:04.811Z_

Compilation successful — 14-page PDF with no errors. All references and citations resolved on the second pass.

The paper is at `artifacts/dream_reports/dream_20260520T100349/best/paper.tex` (and `paper.pdf`). It covers all 20 experiments from `experiment_data.json`:

**Main body (8 sections):** feature ablation & DDR characterization, cross-generator generalization (5-gen LOGO), baseline comparison (vs FastDetectGPT/Binoculars/LD-Score/Avg-LogProb), cross-model chains + cross-reference validation, DDR causality analysis, downstream utility (negative finding), instruct model degradation, multi-domain evaluation, and large-scale generator (8B).

**Appendix (13 sections):** multi-detector ensemble, finer-grained ordinal (5-class), temperature sensitivity, human edit robustness, LD-Score augmentation, end-to-end QLoRA classifier, text length confound control, 9-generator scale evaluation, prompt type & chain type comparison (incl. paraphrastic), TOST bootstrap stationarity, independent seed validation, and topic drift control.

All numbers come directly from `experiment_data.json`. The three claims (depth discriminability, DDR, negative downstream finding) are structured per the framing guidance, with binary F1 = 0.694 as headline metric.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4b84ce-8150-4a93-9d1b-8dddfcbf83b3",
  "isSidechain": false,
  "requestId": "req_011CbDfkSJRS2TviWgQs5Avh",
  "type": "assistant",
  "uuid": "1b51b2d5-22af-44a5-89b6-8b1e1c2bed4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260520T100349/best",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvcrctTyrMpiLFKCEn4r8g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4981,
      "cache_read_input_tokens": 72711,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4981,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 328,
          "cache_read_input_tokens": 72711,
          "cache_creation_input_tokens": 4981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4981
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T100349 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerpr…",
  "leafUuid": "1b51b2d5-22af-44a5-89b6-8b1e1c2bed4d",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete simulated research paper from dream data",
  "sessionId": "12403ebc-9514-4215-82a8-4a9860541744"
}
```

---
