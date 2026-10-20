# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae.jsonl`
- **Structured JSON:** [`e173aaa5f9df3dbf2fb7.json`](../../sessions/e1/e173aaa5f9df3dbf2fb7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:36:46.173Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:36:46.173Z",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/experiment_data.json`（先 Read 此文件）\n- Venue：Insights from Negative Results in NLP @ EMNLP 2026\n- Narrative guidance：核心叙事从三个 crisp findings 收缩为层级式 claims：(1) 方差梯度作为 primary finding（最 robust， 跨实验一致），(2) taxonomy label 作为 amplifier of instability（方向性 claim，penalty 存在 但幅度跨 seed 漂移 3-9pp，不再称 \"remarkably stable\"），(3) 剂量-响应作为 exploratory evidence with caveats（大致形状成立但阈值位置漂移）。论文仍成立为 cautionary negative result，但 contribution 从精确定量边界条件转向 \"error injection 不应被默认迁移到 embodied planning\" 的方向性警告。 Priority 2 实验中 qualitative failure analysis 变得关键——需要定性证据弥补定量统计力不足。 新增实验的结果均在 marginal significance 区间，强化了 \"suggestive but inconclusive\" 的叙事基调。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:36:46.176Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:36:46.176Z",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-15T02:36:46.196Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/experiment_data.json`（先 Read 此文件）
- Venue：Insights from Negative Results in NLP @ EMNLP 2026
- Narrative guidance：核心叙事从三个 crisp findings 收缩为层级式 claims：(1) 方差梯度作为 primary finding（最 robust， 跨实验一致），(2) taxonomy label 作为 amplifier of instability（方向性 claim，penalty 存在 但幅度跨 seed 漂移 3-9pp，不再称 "remarkably stable"），(3) 剂量-响应作为 exploratory evidence with caveats（大致形状成立但阈值位置漂移）。论文仍成立为 cautionary negative result，但 contribution 从精确定量边界条件转向 "error injection 不应被默认迁移到 embodied planning" 的方向性警告。 Priority 2 实验中 qualitative failure analysis 变得关键——需要定性证据弥补定量统计力不足。 新增实验的结果均在 marginal significance 区间，强化了 "suggestive but inconclusive" 的叙事基调。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "3bf1c563-9cda-485b-90bb-a0c50bf78650",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:36:46.195Z_

```json
{
  "parentUuid": "3bf1c563-9cda-485b-90bb-a0c50bf78650",
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
  "uuid": "80f5b7ca-3498-4dc7-b2fc-75d25cd76f9d",
  "timestamp": "2026-05-15T02:36:46.195Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:36:46.196Z_

```json
{
  "parentUuid": "80f5b7ca-3498-4dc7-b2fc-75d25cd76f9d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "69b11a0f-e980-4fb0-a4a8-27ef8a3f1de3",
  "timestamp": "2026-05-15T02:36:46.196Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
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
  "aiTitle": "Generate simulated research paper for error injection study",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Assistant

_source line 7 · 2026-05-15T02:36:50.282Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b11a0f-e980-4fb0-a4a8-27ef8a3f1de3",
  "isSidechain": false,
  "requestId": "req_011Cb3aQF8YPz65A7g8VEKo6",
  "type": "assistant",
  "uuid": "04e53f6c-28ea-44a9-9611-a0bcbc43aa50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoAAe3dR6p5SfB1iM8btD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11345
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

_source line 8 · 2026-05-15T02:36:51.493Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S4cRGVGUmpWGrUKk5qnXDo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04e53f6c-28ea-44a9-9611-a0bcbc43aa50",
  "isSidechain": false,
  "requestId": "req_011Cb3aQF8YPz65A7g8VEKo6",
  "type": "assistant",
  "uuid": "bdbf7a5a-c06e-4569-980d-b5410e4d285d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoAAe3dR6p5SfB1iM8btD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11345
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

_source line 9 · 2026-05-15T02:36:51.647Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NfobfCYkfHjicVAgkjoR9Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdbf7a5a-c06e-4569-980d-b5410e4d285d",
  "isSidechain": false,
  "requestId": "req_011Cb3aQF8YPz65A7g8VEKo6",
  "type": "assistant",
  "uuid": "8bb2bd7e-7c3d-473c-9756-f950592cfe96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnoAAe3dR6p5SfB1iM8btD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11345,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11345,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11345
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

_source line 10 · 2026-05-15T02:36:51.655Z_

<details><summary>↩ Tool result · `toolu_01NfobfCYkfHjicVAgkjoR9Y`</summary>

```text
1	# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training
2	
3	## Target Venue
4	**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.
5	**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).
6	
7	## Core Question
8	Under what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?
9	
10	## Thesis Statement
11	Taxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.
12	
13	## Story Arc
14	
15	### 1. Motivation: Why error injection should work
16	Error injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?
17	
18	### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning
19	We designed a 4-operator error taxonomy for ALFWorld embodied planning:
20	- **P1** (step_order_swap): permute action ordering
21	- **P2** (sub_goal_deletion): remove sub-goals
22	- **C1** (context_truncation): truncate environmental context
23	- **C4** (observation_masking): mask observation feedback
24	
25	We injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.
26	
27	### 3. Finding: No benefit, high instability
28	**Clean task performance (3-seed, all methods complete)**:
29	- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable
30	- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**
31	- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**
32	
33	**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.
34	
35	**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.
36	
37	**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:
38	| Dose | TaxEI | Random | Δ(R−T) |
39	|------|-------|--------|---------|
40	| 0% (vanilla) | 61.7% | 61.7% | 0 |
41	| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |
42	| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |
43	| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |
44	
45	**Two separable effects**:
46	1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.
47	2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.
48	
49	Note: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.
50	
51	**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:
52	- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%
53	
54	**Detection Rate**: 0% for all methods.
55	
56	**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).
57	
58	### 4. Analysis: Why it fails in embodied planning but works in tool-use
59	
60	**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.
61	| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |
62	|-----------|----------------------|------------------------------|
63	| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |
64	| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |
65	| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |
66	| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |
67	| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |
68	| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |
69	| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |
70	
71	**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.
72	
73	**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.
74	
75	### 5. Contribution: What this negative result gives the community
76	1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.
77	2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.
78	3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.
79	4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.
80	
81	## Core Claims (each backed by experimental evidence)
82	
83	- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.
84	  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.
85	
86	- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.
87	  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.
88	
89	- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.
90	  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.
91	
92	- **Claim 4**: Injection-trained models do not improve error recovery.
93	  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).
94	
95	- **Claim 5**: Detection training via error injection is completely ineffective in this setup.
96	  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).
97	
98	- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.
99	  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.
100	
101	## Anticipated Reviewer Concerns
102	
103	1. **"Statistical power with 3 seeds is limited."**
104	   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.
105	
106	2. **"ALFWorld has only 47 test tasks — too small for reliable conclusions."**
107	   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.
108	
109	3. **"Maybe the taxonomy itself is poorly designed."**
110	   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.
111	
112	4. **"The training recipe might be suboptimal for injection data."**
113	   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.
114	
115	5. **"50% injection ratio is too high — you're drowning the signal."**
116	   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.
117	
118	6. **"Why is detection rate 0%? Evaluation might be flawed."**
119	   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.
120	
121	7. **"Why not compare directly on ToolBench?"**
122	   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.
123	
124	## Key Differentiators vs PALADIN
125	
126	PALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:
127	
128	1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., "go to countertop 2" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.
129	
130	2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.
131	
132	3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making "what to do after an error" fundamentally harder to learn from examples.
133	
134	4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.
135	
136	**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.
137	
138	## Note on v3→v4 Vanilla Discrepancy
139	v3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.
140	
141	## Supplementary Experiments Needed
142	
143	### Priority 1 (required for submission)
144	- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.
145	- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.
146	- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?
147	
148	### Priority 2 (strengthens paper significantly)
149	- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.
150	- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the "noise vs. wrong learning" distinction.
151	
152	### Priority 3 (nice to have)
153	- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?
154	- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.
155	- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bb2bd7e-7c3d-473c-9756-f950592cfe96",
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "19d055ad-96d9-4dfd-a6cf-ed72914bf7d0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper_framing.md",
      "content": "# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  },
  "sourceToolAssistantUUID": "8bb2bd7e-7c3d-473c-9756-f950592cfe96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject…",
  "leafUuid": "19d055ad-96d9-4dfd-a6cf-ed72914bf7d0",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for error injection study",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Tool result

_source line 13 · 2026-05-15T02:36:52.113Z_

<details><summary>↩ Tool result · `toolu_01S4cRGVGUmpWGrUKk5qnXDo`</summary>

```text
1	[
2	  {
3	    "name": "Training Dynamics Analysis",
4	    "description": "分离 TaxEI/Random/Vanilla 训练过程中 clean 样本与 injected 样本的 loss 曲线，检验注入样本是否腐蚀 clean 学习信号",
5	    "results": {
6	      "vanilla_clean_loss_epoch1": 0.44,
7	      "vanilla_clean_loss_epoch2": 0.33,
8	      "vanilla_clean_loss_epoch3": 0.29,
9	      "taxei_clean_loss_epoch1": 0.46,
10	      "taxei_clean_loss_epoch2": 0.35,
11	      "taxei_clean_loss_epoch3": 0.31,
12	      "taxei_injected_loss_epoch1": 0.63,
13	      "taxei_injected_loss_epoch2": 0.49,
14	      "taxei_injected_loss_epoch3": 0.42,
15	      "random_clean_loss_epoch1": 0.45,
16	      "random_clean_loss_epoch2": 0.34,
17	      "random_clean_loss_epoch3": 0.3,
18	      "random_injected_loss_epoch1": 0.61,
19	      "random_injected_loss_epoch2": 0.47,
20	      "random_injected_loss_epoch3": 0.4,
21	      "taxei_clean_vs_vanilla_clean_gap_epoch3": 0.02,
22	      "injected_vs_clean_gap_taxei_epoch3": 0.11,
23	      "injected_vs_clean_gap_random_epoch3": 0.1,
24	      "taxei_clean_loss_epoch3_seed_sd": 0.015,
25	      "vanilla_clean_loss_epoch3_seed_sd": 0.008
26	    },
27	    "tables": [
28	      {
29	        "name": "Training Loss Decomposition by Sample Type",
30	        "description": "3 methods × 3 epochs × 2 sample types (clean/injected), 报告 mean loss ± cross-seed SD",
31	        "columns": [
32	          "method",
33	          "sample_type",
34	          "epoch1",
35	          "epoch2",
36	          "epoch3"
37	        ],
38	        "rows": [
39	          [
40	            "Vanilla",
41	            "clean",
42	            "0.44 ± 0.01",
43	            "0.33 ± 0.01",
44	            "0.29 ± 0.01"
45	          ],
46	          [
47	            "TaxEI",
48	            "clean",
49	            "0.46 ± 0.02",
50	            "0.35 ± 0.02",
51	            "0.31 ± 0.02"
52	          ],
53	          [
54	            "TaxEI",
55	            "injected",
56	            "0.63 ± 0.03",
57	            "0.49 ± 0.02",
58	            "0.42 ± 0.02"
59	          ],
60	          [
61	            "Random",
62	            "clean",
63	            "0.45 ± 0.01",
64	            "0.34 ± 0.01",
65	            "0.30 ± 0.01"
66	          ],
67	          [
68	            "Random",
69	            "injected",
70	            "0.61 ± 0.02",
71	            "0.47 ± 0.02",
72	            "0.40 ± 0.02"
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "训练动态证据在 median 档下是 supportive but inconclusive：注入样本确实是\"更难学的数据\" （loss 持续高出 ~25-35%），但这本身不构成 harm——问题是这些难学的样本是否干扰了 clean 样本的学习。0.02 的 clean loss gap 方向正确但统计不可靠。 该结果可以在论文中作为 supplementary evidence 呈现，用\"consistent with the hypothesis that injection introduces noise without providing learnable recovery signal\"的措辞， 避免称其为 definitive evidence of corruption。 方差梯度在训练动态层面也有所体现（TaxEI clean loss 的跨 seed SD 更大），这加强了 Claim 3 (training instability) 的叙事。\n\n\nMedian 档下，注入样本 loss 始终高于 clean 样本（~0.10-0.11 gap at epoch 3），这是直接预期： 注入样本包含刻意错误的轨迹，模型难以完美拟合。关键问题是 clean 样本是否被\"传染\"—— TaxEI 训练中 clean 子集的 epoch 3 loss (0.31) 比 Vanilla 的 (0.29) 高约 0.02， 但这个差异仅约 1 个 seed SD (0.015)，在统计上不显著。这解释了 median 档的核心特征： 注入样本 loss 更高是明确的（clean 和 injected 两条曲线清晰分离），但对 clean 样本 的 corruption 效应淹没在训练噪声中——你能看到趋势但无法声称 significant corruption。 TaxEI injected loss 略高于 Random injected loss (0.42 vs 0.40) 反映 taxonomy-tagged 错误模式更难学（结构化标签引入了额外的模式复杂性），但差异同样 marginal。 跨 seed 看，TaxEI clean loss 的 SD (0.015) 几乎是 Vanilla (0.008) 的 2 倍， 与 eval 端观察到的方差梯度一致——训练过程本身就更不稳定。\n"
79	  },
80	  {
81	    "name": "Second Environment Replication (WebShop)",
82	    "description": "在 WebShop 环境复制 Vanilla/TaxEI/Random 三条件对比，测试 negative result 是否跨环境泛化",
83	    "results": {
84	      "vanilla_3seed_mean_reward": 0.53,
85	      "vanilla_3seed_sd": 0.025,
86	      "taxei_3seed_mean_reward": 0.48,
87	      "taxei_3seed_sd": 0.055,
88	      "random_3seed_mean_reward": 0.5,
89	      "random_3seed_sd": 0.04,
90	      "taxei_vs_vanilla_gap_pp": -5.0,
91	      "taxonomy_penalty_pp": -2.0,
92	      "variance_ratio_taxei_vs_vanilla": 2.2,
93	      "paired_t_taxei_vs_vanilla_p": 0.18,
94	      "paired_t_taxei_vs_random_p": 0.12,
95	      "vanilla_seed42": 0.55,
96	      "vanilla_seed0": 0.51,
97	      "vanilla_seed123": 0.53,
98	      "taxei_seed42": 0.52,
99	      "taxei_seed0": 0.42,
100	      "taxei_seed123": 0.5,
101	      "random_seed42": 0.53,
102	      "random_seed0": 0.46,
103	      "random_seed123": 0.51
104	    },
105	    "tables": [
106	      {
107	        "name": "Cross-Environment Comparison",
108	        "description": "ALFWorld vs WebShop, 三个方法的 3-seed mean ± SD 并列",
109	        "columns": [
110	          "method",
111	          "ALFWorld acc% (±SD)",
112	          "WebShop reward (±SD)",
113	          "ALFWorld Δ vs Vanilla",
114	          "WebShop Δ vs Vanilla"
115	        ],
116	        "rows": [
117	          [
118	            "Vanilla",
119	            "65.3 ± 3.3",
120	            "0.53 ± 0.025",
121	            "—",
122	            "—"
123	          ],
124	          [
125	            "TaxEI",
126	            "56.7 ± 8.6",
127	            "0.48 ± 0.055",
128	            "-8.6pp",
129	            "-5.0pp"
130	          ],
131	          [
132	            "Random",
133	            "63.1 ± 7.0",
134	            "0.50 ± 0.040",
135	            "-2.2pp",
136	            "-3.0pp"
137	          ]
138	        ]
139	      },
140	      {
141	        "name": "WebShop Per-Seed Results",
142	        "description": "3 methods × 3 seeds",
143	        "columns": [
144	          "method",
145	          "seed=42",
146	          "seed=0",
147	          "seed=123",
148	          "mean",
149	          "SD"
150	        ],
151	        "rows": [
152	          [
153	            "Vanilla",
154	            "0.55",
155	            "0.51",
156	            "0.53",
157	            "0.53",
158	            "0.020"
159	          ],
160	          [
161	            "TaxEI",
162	            "0.52",
163	            "0.42",
164	            "0.50",
165	            "0.48",
166	            "0.053"
167	          ],
168	          [
169	            "Random",
170	            "0.53",
171	            "0.46",
172	            "0.51",
173	            "0.50",
174	            "0.036"
175	          ]
176	        ]
177	      }
178	    ],
179	    "figures": [],
180	    "analysis": "WebShop 复制确认了 negative result 的方向性泛化，但效应量衰减（-5pp vs ALFWorld 的 -8.6pp， taxonomy penalty 2pp vs 5-7pp）。这实际上 *加强* 了论文的核心 contribution： boundary condition 不是 binary (works / doesn't work) 而是 gradient——随着 task structure 向更 observable、更 locally recoverable 方向移动，error injection 的 harm 递减。 论文可以将三个环境 (ToolBench +57pp / WebShop -5pp / ALFWorld -8.6pp) 排列在 task-structure spectrum 上，这比单环境 negative result 更有说服力。 但统计检验仍然 marginal（p ∈ [0.10, 0.20]），limitation section 需要坦承 underpowered。\n\n\nWebShop 与 ALFWorld 的结构差异导致效应减弱但方向一致。WebShop 的 action space 更结构化 （search → click → buy 的固定流程），错误可观察性比 ALFWorld 高（搜索返回相关度可见的结果）， 但仍然弱于 tool-use（没有显式 error code）。Median 档预测： (1) 方差梯度依然成立 (Vanilla SD 0.025 < Random 0.040 < TaxEI 0.055)，但倍率从 ALFWorld 的 2.6× 降至 2.2×——WebShop 更结构化的 action space 部分吸收了注入带来的不稳定性。 (2) Taxonomy penalty 缩小到 ~2pp（ALFWorld 是 ~5-7pp），因为 WebShop 的错误模式 更接近 tool-use 端的\"局部可恢复\"属性，taxonomy label 的 harm 减弱。 (3) TaxEI seed=0 再次出现 collapse (0.42 vs mean 0.48)，但幅度比 ALFWorld 小—— 这支持\"TaxEI 训练是 lottery\"的叙事。 (4) p 值全在 0.10-0.20 区间，与 ALFWorld 一样无法突破 α=0.05。 总体：方向性复制成功，但效应量更小，加强了\"task structure matters\"的论点—— WebShop 介于 tool-use (PALADIN ✓) 和 embodied planning (ALFWorld ✗) 之间。\n"
181	  },
182	  {
183	    "name": "Qualitative Failure Analysis",
184	    "description": "人工检查 25 个 TaxEI 失败案例（重点来自 seed=0 的 collapse），分类失败模式，区分 noise corruption 与 wrong learning",
185	    "results": {
186	      "total_cases_examined": 25,
187	      "cases_from_seed0": 15,
188	      "cases_from_seed42_seed123": 10,
189	      "type_a_incoherent_planning_count": 11,
190	      "type_a_pct": 44,
191	      "type_b_systematic_wrong_action_count": 8,
192	      "type_b_pct": 32,
193	      "type_c_premature_termination_count": 4,
194	      "type_c_pct": 16,
195	      "type_d_correct_plan_execution_error_count": 2,
196	      "type_d_pct": 8,
197	      "seed0_type_a_pct": 53,
198	      "seed42_123_type_a_pct": 30,
199	      "seed0_type_b_pct": 27,
200	      "seed42_123_type_b_pct": 40,
201	      "random_type_a_pct": 30,
202	      "random_type_b_pct": 20,
203	      "random_type_c_pct": 30,
204	      "random_type_d_pct": 20,
205	      "p1_echo_cases": 3,
206	      "p2_echo_cases": 2,
207	      "recovery_behavior_in_wrong_context": 4
208	    },
209	    "tables": [
210	      {
211	        "name": "Failure Type Distribution",
212	        "description": "TaxEI 失败案例分类，按 seed 分组",
213	        "columns": [
214	          "failure_type",
215	          "seed=0 (n=15)",
216	          "seed=42/123 (n=10)",
217	          "total (n=25)",
218	          "Random ref (n=10)"
219	        ],
220	        "rows": [
221	          [
222	            "A: Incoherent planning",
223	            "8 (53%)",
224	            "3 (30%)",
225	            "11 (44%)",
226	            "3 (30%)"
227	          ],
228	          [
229	            "B: Systematic wrong action",
230	            "4 (27%)",
231	            "4 (40%)",
232	            "8 (32%)",
233	            "2 (20%)"
234	          ],
235	          [
236	            "C: Premature termination",
237	            "2 (13%)",
238	            "2 (20%)",
239	            "4 (16%)",
240	            "3 (30%)"
241	          ],
242	          [
243	            "D: Correct plan, exec error",
244	            "1 (7%)",
245	            "1 (10%)",
246	            "2 (8%)",
247	            "2 (20%)"
248	          ]
249	        ]
250	      },
251	      {
252	        "name": "Error Echo Examples",
253	        "description": "TaxEI 失败中与注入 operator 直接对应的错误模式",
254	        "columns": [
255	          "case_id",
256	          "task_type",
257	          "injected_operator_echo",
258	          "description"
259	        ],
260	        "rows": [
261	          [
262	            "F-s0-07",
263	            "pick_heat_then_place",
264	            "P1_step_order_swap",
265	            "先 put 再 heat，与 P1 注入的 swap 模式一致"
266	          ],
267	          [
268	            "F-s0-12",
269	            "pick_clean_then_place",
270	            "P1_step_order_swap",
271	            "clean 和 place 顺序颠倒"
272	          ],
273	          [
274	            "F-s0-19",
275	            "pick_two_obj",
276	            "P2_sub_goal_deletion",
277	            "只完成了第一个 object 就终止，跳过第二个 sub-goal"
278	          ],
279	          [
280	            "F-s42-03",
281	            "pick_cool_then_place",
282	            "P2_sub_goal_deletion",
283	            "跳过 cool 步骤直接 place"
284	          ],
285	          [
286	            "F-s123-08",
287	            "look_at_obj_in_light",
288	            "—",
289	            "反复在 desklamp 前检查对象（recovery-like behavior in normal context）"
290	          ]
291	        ]
292	      }
293	    ],
294	    "figures": [],
295	    "analysis": "定性分析是 median 档下最有价值的补充实验。定量证据受限于 n=47 和 3 seeds， p 值卡在 0.05-0.15，无法做 strong quantitative claims。但定性证据提供了 mechanistic insight：(1) seed=0 collapse 主要由 incoherent planning 驱动（noise corruption）， (2) 即使在\"正常\"seed 中，TaxEI 的失败模式也包含可识别的 error echoes（wrong learning）， (3) TaxEI vs Random 的失败模式分布差异（Type B 32% vs 20%）为 taxonomy penalty 的 mechanistic 解释提供了初步证据。论文应将此作为 Section 5 的核心分析，用具体案例 支撑定量发现的方向性 claims。措辞建议：\"Manual inspection reveals two co-occurring failure mechanisms — noise-induced incoherence and taxonomy-specific error echoes — suggesting that structured error injection both corrupts and misdirects the learning signal.\"\n\n\nMedian 档下，failure analysis 揭示混合机制——既有 noise corruption 也有 wrong learning， 不能简单归因于单一原因。 Type A (incoherent planning, 44%) 代表 noise corruption：模型产生的动作序列虽然句法合法 但逻辑矛盾（先 heat 再 pick up，或导航到不相关位置）。这在 seed=0 中特别突出 (53%)， 与 seed=0 的 catastrophic collapse (46.8%) 一致——这个 seed 的训练过程中 noise 占了上风。 Type B (systematic wrong action, 32%) 代表 wrong learning：模型一致性地选择错误对象或 位置，暗示它从注入样本中学到了特定的错误关联。值得注意的是 Type B 在 seed42/123 中 比例更高 (40%)——这些 seed 整体表现尚可 (61.7%)，但失败案例中 wrong learning 占主导。 在 3 个案例中发现了明确的 \"error echo\"——模型的错误模式直接镜像了 P1 (step_order_swap) 注入的动作排列错误。4 个案例显示模型在不需要恢复的正常任务中执行了类似恢复的行为 （如反复检查已确认的对象），说明注入训练 taught the model to be cautious in wrong contexts。 与 Random 失败案例的对比显示 TaxEI 的 Type B 比例更高 (32% vs 20%)，支持 \"taxonomy labels teach specific wrong behaviors\" 的 claim，但样本量太小 (25 vs 10) 无法做统计检验。\n"
296	  },
297	  {
298	    "name": "Scale Ablation (25K/50K trajectories)",
299	    "description": "将训练数据扩展到 25K 和 50K 轨迹，测试 PALADIN 级别数据量是否改善 TaxEI 表现",
300	    "results": {
301	      "collection_25k_attempts": 36000,
302	      "collection_25k_successes": 25200,
303	      "collection_25k_cost_usd": 445,
304	      "collection_50k_attempts": 72000,
305	      "collection_50k_successes": 50400,
306	      "collection_50k_cost_usd": 890,
307	      "vanilla_25k_mean_pct": 66.8,
308	      "vanilla_25k_sd_pp": 2.8,
309	      "taxei_25k_mean_pct": 60.3,
310	      "taxei_25k_sd_pp": 5.2,
311	      "random_25k_mean_pct": 62.5,
312	      "random_25k_sd_pp": 4.1,
313	      "taxei_vs_vanilla_25k_gap_pp": -6.5,
314	      "taxonomy_penalty_25k_pp": -2.2,
315	      "variance_ratio_25k": 1.86,
316	      "vanilla_50k_mean_pct": 67.5,
317	      "vanilla_50k_sd_pp": 2.5,
318	      "taxei_50k_mean_pct": 62.1,
319	      "taxei_50k_sd_pp": 4.5,
320	      "random_50k_mean_pct": 64.0,
321	      "random_50k_sd_pp": 3.8,
322	      "taxei_vs_vanilla_50k_gap_pp": -5.4,
323	      "taxonomy_penalty_50k_pp": -1.9,
324	      "variance_ratio_50k": 1.8,
325	      "paired_t_taxei_vs_vanilla_25k_p": 0.12,
326	      "paired_t_taxei_vs_vanilla_50k_p": 0.09,
327	      "train_time_25k_hours": 18,
328	      "train_time_50k_hours": 36,
329	      "total_gpu_hours": 162
330	    },
331	    "tables": [
332	      {
333	        "name": "Scale Ablation Results",
334	        "description": "三个 data scale 下三方法的性能对比",
335	        "columns": [
336	          "scale",
337	          "Vanilla (±SD)",
338	          "TaxEI (±SD)",
339	          "Random (±SD)",
340	          "TaxEI-Vanilla gap",
341	          "Taxonomy penalty",
342	          "Variance ratio"
343	        ],
344	        "rows": [
345	          [
346	            "9K (current)",
347	            "65.3 ± 3.3",
348	            "56.7 ± 8.6",
349	            "63.1 ± 7.0",
350	            "-8.6pp",
351	            "-6.4pp",
352	            "2.6×"
353	          ],
354	          [
355	            "25K",
356	            "66.8 ± 2.8",
357	            "60.3 ± 5.2",
358	            "62.5 ± 4.1",
359	            "-6.5pp",
360	            "-2.2pp",
361	            "1.86×"
362	          ],
363	          [
364	            "50K",
365	            "67.5 ± 2.5",
366	            "62.1 ± 4.5",
367	            "64.0 ± 3.8",
368	            "-5.4pp",
369	            "-1.9pp",
370	            "1.80×"
371	          ]
372	        ]
373	      },
374	      {
375	        "name": "Cost-Benefit Analysis",
376	        "description": "数据规模扩展的成本与收益",
377	        "columns": [
378	          "scale",
379	          "collection_cost",
380	          "gpu_hours",
381	          "taxei_improvement_vs_9k",
382	          "still_worse_than_vanilla"
383	        ],
384	        "rows": [
385	          [
386	            "9K",
387	            "$8.86",
388	            "~6h",
389	            "baseline",
390	            "yes (-8.6pp)"
391	          ],
392	          [
393	            "25K",
394	            "~$445",
395	            "~54h",
396	            "+3.6pp",
397	            "yes (-6.5pp)"
398	          ],
399	          [
400	            "50K",
401	            "~$890",
402	            "~108h",
403	            "+5.4pp",
404	            "yes (-5.4pp)"
405	          ]
406	        ]
407	      }
408	    ],
409	    "figures": [],
410	    "analysis": "Scale ablation 在 median 档下产生 mixed 信号：scale 确实 helps（方差降低、gap 收窄）， 但 50K 数据仍无法消除 TaxEI 的劣势。这使得论文的 PALADIN 对比更加 nuanced—— PALADIN 的成功不仅是 scale（50K+ 轨迹），更是 task structure + retrieval augmentation 的组合。建议在 Discussion 中加入 scaling analysis 作为 \"data scale as partial mitigant\"， 但明确 \"structural mismatch persists even at PALADIN scale\"。 成本分析 ($890 for 50K, 108 GPU-hours) 进一步强化了 negative result 的实践价值： 追求 error injection 在 embodied planning 中的效果需要极高成本且收效甚微。\n\n\nMedian 档预测 scale helps but doesn't close the gap。理由： (1) 更多 clean 数据直接受益所有方法——Vanilla 从 65.3% 提升到 67.5%（+2.2pp）， 因为 ALFWorld 的 47 task 的最优表现大约在 70-75% 区间（v3 vanilla 就达到 74.5%）。 (2) TaxEI 在 25K 时提升到 60.3%（vs 9K 的 56.7%，+3.6pp），50K 时 62.1%（+5.4pp）。 提升来自两个效应：更多 clean 样本提供更强基础信号，更大数据量让模型有更多容量 分离 error 模式和 correct 模式。但 gap 仅从 -8.6pp 收窄到 -5.4pp，说明结构性 mismatch 不是纯 scale 问题。 (3) 方差梯度依然成立但倍率递减：9K 2.6× → 25K 1.86× → 50K 1.80×。 更多数据 stabilize 训练，但 TaxEI 的方差始终高于 Vanilla。 (4) Taxonomy penalty 从 ~6.4pp 降至 ~1.9pp——大数据量下模型更能 tolerate taxonomy labels 的干扰，但 penalty 方向始终为负。 (5) p 值从 0.32 改善到 0.09，接近但仍未突破 α=0.05——median 档的标志性特征。 关键结论：即使在 PALADIN 级别的 50K scale，TaxEI 在 embodied planning 上仍然 inferior， 且需要 5.5× 的数据收集成本（$890 vs $8.86）才能部分弥合差距。 这强化了 \"task structure > data scale\" 的论点。\n"
411	  },
412	  {
413	    "name": "Recovery Prompting (Few-Shot In-Context)",
414	    "description": "用 5-shot 恢复示例替代 SFT，测试 error recovery 知识在 inference-time 提供是否比训练时注入更有效",
415	    "results": {
416	      "vanilla_zeroshot_pct": 65.3,
417	      "vanilla_5shot_recovery_pct": 67.4,
418	      "vanilla_5shot_gain_pp": 2.1,
419	      "taxei_zeroshot_pct": 56.7,
420	      "taxei_5shot_recovery_pct": 60.8,
421	      "taxei_5shot_gain_pp": 4.1,
422	      "random_zeroshot_pct": 63.1,
423	      "random_5shot_recovery_pct": 65.0,
424	      "random_5shot_gain_pp": 1.9,
425	      "vanilla_recovery_zeroshot_pct": 61.7,
426	      "vanilla_recovery_5shot_pct": 66.0,
427	      "vanilla_recovery_5shot_gain_pp": 4.3,
428	      "taxei_recovery_zeroshot_pct": 59.6,
429	      "taxei_recovery_5shot_pct": 64.9,
430	      "taxei_recovery_5shot_gain_pp": 5.3,
431	      "random_recovery_zeroshot_pct": 63.8,
432	      "random_recovery_5shot_pct": 66.7,
433	      "random_recovery_5shot_gain_pp": 2.9,
434	      "paired_t_5shot_vs_zeroshot_vanilla_p": 0.14,
435	      "paired_t_5shot_vs_zeroshot_taxei_p": 0.08,
436	      "paladin_retrieval_gain_pp": 30.0,
437	      "our_5shot_recovery_gain_pp_max": 5.3
438	    },
439	    "tables": [
440	      {
441	        "name": "Zero-Shot vs Few-Shot Recovery Comparison",
442	        "description": "3 methods × 2 eval settings (clean / recovery) × 2 conditions (zero-shot / 5-shot)",
443	        "columns": [
444	          "method",
445	          "clean_0shot",
446	          "clean_5shot",
447	          "Δ",
448	          "recovery_0shot",
449	          "recovery_5shot",
450	          "Δ"
451	        ],
452	        "rows": [
453	          [
454	            "Vanilla",
455	            "65.3%",
456	            "67.4%",
457	            "+2.1",
458	            "61.7%",
459	            "66.0%",
460	            "+4.3"
461	          ],
462	          [
463	            "TaxEI",
464	            "56.7%",
465	            "60.8%",
466	            "+4.1",
467	            "59.6%",
468	            "64.9%",
469	            "+5.3"
470	          ],
471	          [
472	            "Random",
473	            "63.1%",
474	            "65.0%",
475	            "+1.9",
476	            "63.8%",
477	            "66.7%",
478	            "+2.9"
479	          ]
480	        ]
481	      }
482	    ],
483	    "figures": [],
484	    "analysis": "Few-shot recovery 实验的价值在于 mechanistic decomposition：它证明 recovery knowledge 本身是有用的（inference-time 提供可以 improve），但 SFT 不是正确的 delivery mechanism for embodied planning。这与 EEF 的成功形成对比——EEF 从 failures 中 extract positive signal（what to do right），而 TaxEI inject negative signal（what goes wrong）。 论文可以在 Discussion 中构建一个 2×2 框架：training vs inference × positive vs negative signal，argue that embodied planning 需要 inference-time positive signal (EEF-like) 而非 training-time negative signal (TaxEI-like)。\n\n\nMedian 档预测 few-shot recovery 提供 modest improvement（2-5pp），远低于 PALADIN 的 30pp retrieval 增益。理由： (1) 5 个恢复示例为模型提供了\"如何从错误中恢复\"的 in-context knowledge， 这对 clean tasks 有轻微帮助（模型变得更 cautious/systematic），对 recovery tasks 有更明显帮助（直接相关的示例）。 (2) TaxEI + 5-shot 的 gain (+4.1pp clean, +5.3pp recovery) 高于 Vanilla + 5-shot (+2.1pp, +4.3pp)，显示 TaxEI 训练虽然 hurt overall，但可能让模型对 recovery cues 更 receptive——它学会了\"关注错误\"但没学会\"如何正确恢复\"，few-shot 补充了后者。 这构成了一个有趣的 complementarity story。 (3) 5-shot 的 gain 远低于 PALADIN 的 retrieval gain (30pp)，因为 5 个示例覆盖率 极低（PALADIN 用 55+ exemplars），且 ALFWorld 的 unbounded action space 使得 少量示例的迁移性有限。 (4) 所有 gain 的 p 值在 0.08-0.15，再次停留在 marginal 区间——median 档特征。 关键 insight：recovery knowledge 在 inference-time 提供比在 training-time 注入 更安全（无 variance increase），但在 embodied planning 中效果均有限。 这进一步隔离了问题：不是 \"knowledge of recovery is useless\"， 而是 \"embodied planning 的 action space 太大，局部恢复示例难以泛化\"。\n"
485	  },
486	  {
487	    "name": "Per-Operator Recovery Deep Dive",
488	    "description": "扩展 recovery eval 到 3 seeds，验证单 seed 观察到的 per-operator patterns（特别是 C4 +9.1pp 优势）是否稳定",
489	    "results": {
490	      "taxei_C1_mean_pct": 60.4,
491	      "taxei_C1_sd_pp": 8.3,
492	      "taxei_C4_mean_pct": 58.7,
493	      "taxei_C4_sd_pp": 7.1,
494	      "taxei_P1_mean_pct": 55.6,
495	      "taxei_P1_sd_pp": 11.2,
496	      "taxei_P2_mean_pct": 48.6,
497	      "taxei_P2_sd_pp": 6.8,
498	      "vanilla_C1_mean_pct": 62.5,
499	      "vanilla_C1_sd_pp": 4.2,
500	      "vanilla_C4_mean_pct": 55.6,
501	      "vanilla_C4_sd_pp": 5.0,
502	      "vanilla_P1_mean_pct": 61.1,
503	      "vanilla_P1_sd_pp": 6.3,
504	      "vanilla_P2_mean_pct": 56.9,
505	      "vanilla_P2_sd_pp": 4.8,
506	      "gap_C1_pp": -2.1,
507	      "gap_C4_pp": 3.1,
508	      "gap_P1_pp": -5.5,
509	      "gap_P2_pp": -8.3,
510	      "single_seed_gap_C1_pp": -8.3,
511	      "single_seed_gap_C4_pp": 9.1,
512	      "single_seed_gap_P1_pp": -3.4,
513	      "single_seed_gap_P2_pp": -8.3,
514	      "paired_t_C4_p": 0.22,
515	      "paired_t_P2_p": 0.06,
516	      "paired_t_P1_p": 0.15,
517	      "paired_t_C1_p": 0.35
518	    },
519	    "tables": [
520	      {
521	        "name": "Per-Operator Recovery Rate (3-Seed)",
522	        "description": "TaxEI vs Vanilla per-operator, 3-seed mean ± SD，附单 seed 对比",
523	        "columns": [
524	          "operator",
525	          "TaxEI (±SD)",
526	          "Vanilla (±SD)",
527	          "Δ (3-seed)",
528	          "Δ (single-seed)",
529	          "p-value"
530	        ],
531	        "rows": [
532	          [
533	            "C1_context_truncation",
534	            "60.4 ± 8.3%",
535	            "62.5 ± 4.2%",
536	            "-2.1pp",
537	            "-8.3pp",
538	            "0.35"
539	          ],
540	          [
541	            "C4_observation_masking",
542	            "58.7 ± 7.1%",
543	            "55.6 ± 5.0%",
544	            "+3.1pp",
545	            "+9.1pp",
546	            "0.22"
547	          ],
548	          [
549	            "P1_step_order_swap",
550	            "55.6 ± 11.2%",
551	            "61.1 ± 6.3%",
552	            "-5.5pp",
553	            "-3.4pp",
554	            "0.15"
555	          ],
556	          [
557	            "P2_sub_goal_deletion",
558	            "48.6 ± 6.8%",
559	            "56.9 ± 4.8%",
560	            "-8.3pp",
561	            "-8.3pp",
562	            "0.06"
563	          ]
564	        ]
565	      },
566	      {
567	        "name": "Operator Structural Properties",
568	        "description": "将 per-operator 结果与 operator 的结构属性联系",
569	        "columns": [
570	          "operator",
571	          "error_locality",
572	          "recovery_feasibility",
573	          "TaxEI effect direction"
574	        ],
575	        "rows": [
576	          [
577	            "C4_observation_masking",
578	            "local (single obs)",
579	            "high (act conservatively)",
580	            "positive (+3.1pp)"
581	          ],
582	          [
583	            "C1_context_truncation",
584	            "partial (context window)",
585	            "medium (infer from partial)",
586	            "neutral (-2.1pp)"
587	          ],
588	          [
589	            "P1_step_order_swap",
590	            "moderate (multi-step)",
591	            "medium (re-sequence)",
592	            "negative (-5.5pp)"
593	          ],
594	          [
595	            "P2_sub_goal_deletion",
596	            "global (cascading)",
597	            "low (requires re-planning)",
598	            "negative (-8.3pp)"
599	          ]
600	        ]
601	      }
602	    ],
603	    "figures": [],
604	    "analysis": "Per-operator deep dive 是论文 mechanistic argument 的关键支撑。结果揭示了一个 清晰的 gradient：error locality 越 local、recovery 越 feasible 的 operator， TaxEI 效果越好（C4 +3.1pp → C1 -2.1pp → P1 -5.5pp → P2 -8.3pp）。 这个 micro-level gradient 完美镜像了 macro-level 的 tool-use vs planning 对比： 在 operator 层面也是\"局部可恢复的错误可以被学习，全局 cascading 的错误只引入噪声\"。 P2 的 robust negative effect (p≈0.06) 是最接近 significant 的 per-operator finding， 可以在论文中重点讨论。C4 的 positive direction 虽然 NS，但提供了 \"error injection CAN work even in planning, IF the error is locally recoverable\" 的 suggestive evidence， 这是比纯 negative result 更 nuanced 的 contribution。 建议将此结果与 Table 3 (ToolBench vs ALFWorld structural comparison) 合并讨论， 论证 error locality 是 THE key moderating variable。\n\nMedian 档下，multi-seed recovery 揭示单 seed per-operator 数据的不可靠性。 (1) C4 (observation_masking)：单 seed 显示 +9.1pp 优势，3-seed 均值缩水到 +3.1pp。 原因：C4 注入 masks observations，而 ALFWorld 任务中 observation 的重要性因 task instance 而异——有些任务即使 masked 也能靠 prior knowledge 解决，造成高 cross-seed 方差。 单 seed 的 +9.1pp 大概率是有利 task sampling 的结果。但方向仍然正确（唯一 positive gap）， 说明 observation masking 可能是最接近 \"locally recoverable\" 的 operator—— 模型可以学会在信息不足时更 conservative 地行动。 (2) P2 (sub_goal_deletion)：3-seed 均值 -8.3pp，与单 seed 完全一致，SD 仅 6.8pp。 这是最 robust 的 per-operator finding。理由：sub-goal deletion 造成的 cascading failure 最严重——跳过一个 sub-goal 直接导致后续所有步骤无效，这正是 embodied planning 中 error injection 失败的典型机制。TaxEI 不但没学会避免这类错误，反而在某些 instances 中复制了 deletion 模式（与 qualitative analysis 的 error echo 发现一致）。 (3) P1 (step_order_swap)：SD 最高 (11.2pp)，说明 step ordering 的影响高度 task-dependent。 有些任务的 step 可以部分重排而不影响结果，有些则不行。 (4) C1 (context_truncation)：从 -8.3pp 缓和到 -2.1pp，说明单 seed 高估了 harm。 总结：只有 P2 的 negative effect 是 robust 的（p≈0.06），C4 的 positive effect 是 real but small，P1 和 C1 的 patterns 是 noise。\n"
605	  }
606	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdbf7a5a-c06e-4569-980d-b5410e4d285d",
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "22e1693b-264e-46cf-b720-5aa13bacc86f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Training Dynamics Analysis\",\n    \"description\": \"分离 TaxEI/Random/Vanilla 训练过程中 clean 样本与 injected 样本的 loss 曲线，检验注入样本是否腐蚀 clean 学习信号\",\n    \"results\": {\n      \"vanilla_clean_loss_epoch1\": 0.44,\n      \"vanilla_clean_loss_epoch2\": 0.33,\n      \"vanilla_clean_loss_epoch3\": 0.29,\n      \"taxei_clean_loss_epoch1\": 0.46,\n      \"taxei_clean_loss_epoch2\": 0.35,\n      \"taxei_clean_loss_epoch3\": 0.31,\n      \"taxei_injected_loss_epoch1\": 0.63,\n      \"taxei_injected_loss_epoch2\": 0.49,\n      \"taxei_injected_loss_epoch3\": 0.42,\n      \"random_clean_loss_epoch1\": 0.45,\n      \"random_clean_loss_epoch2\": 0.34,\n      \"random_clean_loss_epoch3\": 0.3,\n      \"random_injected_loss_epoch1\": 0.61,\n      \"random_injected_loss_epoch2\": 0.47,\n      \"random_injected_loss_epoch3\": 0.4,\n      \"taxei_clean_vs_vanilla_clean_gap_epoch3\": 0.02,\n      \"injected_vs_clean_gap_taxei_epoch3\": 0.11,\n      \"injected_vs_clean_gap_random_epoch3\": 0.1,\n      \"taxei_clean_loss_epoch3_seed_sd\": 0.015,\n      \"vanilla_clean_loss_epoch3_seed_sd\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Training Loss Decomposition by Sample Type\",\n        \"description\": \"3 methods × 3 epochs × 2 sample types (clean/injected), 报告 mean loss ± cross-seed SD\",\n        \"columns\": [\n          \"method\",\n          \"sample_type\",\n          \"epoch1\",\n          \"epoch2\",\n          \"epoch3\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"clean\",\n            \"0.44 ± 0.01\",\n            \"0.33 ± 0.01\",\n            \"0.29 ± 0.01\"\n          ],\n          [\n            \"TaxEI\",\n            \"clean\",\n            \"0.46 ± 0.02\",\n            \"0.35 ± 0.02\",\n            \"0.31 ± 0.02\"\n          ],\n          [\n            \"TaxEI\",\n            \"injected\",\n            \"0.63 ± 0.03\",\n            \"0.49 ± 0.02\",\n            \"0.42 ± 0.02\"\n          ],\n          [\n            \"Random\",\n            \"clean\",\n            \"0.45 ± 0.01\",\n            \"0.34 ± 0.01\",\n            \"0.30 ± 0.01\"\n          ],\n          [\n            \"Random\",\n            \"injected\",\n            \"0.61 ± 0.02\",\n            \"0.47 ± 0.02\",\n            \"0.40 ± 0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"训练动态证据在 median 档下是 supportive but inconclusive：注入样本确实是\\\"更难学的数据\\\" （loss 持续高出 ~25-35%），但这本身不构成 harm——问题是这些难学的样本是否干扰了 clean 样本的学习。0.02 的 clean loss gap 方向正确但统计不可靠。 该结果可以在论文中作为 supplementary evidence 呈现，用\\\"consistent with the hypothesis that injection introduces noise without providing learnable recovery signal\\\"的措辞， 避免称其为 definitive evidence of corruption。 方差梯度在训练动态层面也有所体现（TaxEI clean loss 的跨 seed SD 更大），这加强了 Claim 3 (training instability) 的叙事。\\n\\n\\nMedian 档下，注入样本 loss 始终高于 clean 样本（~0.10-0.11 gap at epoch 3），这是直接预期： 注入样本包含刻意错误的轨迹，模型难以完美拟合。关键问题是 clean 样本是否被\\\"传染\\\"—— TaxEI 训练中 clean 子集的 epoch 3 loss (0.31) 比 Vanilla 的 (0.29) 高约 0.02， 但这个差异仅约 1 个 seed SD (0.015)，在统计上不显著。这解释了 median 档的核心特征： 注入样本 loss 更高是明确的（clean 和 injected 两条曲线清晰分离），但对 clean 样本 的 corruption 效应淹没在训练噪声中——你能看到趋势但无法声称 significant corruption。 TaxEI injected loss 略高于 Random injected loss (0.42 vs 0.40) 反映 taxonomy-tagged 错误模式更难学（结构化标签引入了额外的模式复杂性），但差异同样 marginal。 跨 seed 看，TaxEI clean loss 的 SD (0.015) 几乎是 Vanilla (0.008) 的 2 倍， 与 eval 端观察到的方差梯度一致——训练过程本身就更不稳定。\\n\"\n  },\n  {\n    \"name\": \"Second Environment Replication (WebShop)\",\n    \"description\": \"在 WebShop 环境复制 Vanilla/TaxEI/Random 三条件对比，测试 negative result 是否跨环境泛化\",\n    \"results\": {\n      \"vanilla_3seed_mean_reward\": 0.53,\n      \"vanilla_3seed_sd\": 0.025,\n      \"taxei_3seed_mean_reward\": 0.48,\n      \"taxei_3seed_sd\": 0.055,\n      \"random_3seed_mean_reward\": 0.5,\n      \"random_3seed_sd\": 0.04,\n      \"taxei_vs_vanilla_gap_pp\": -5.0,\n      \"taxonomy_penalty_pp\": -2.0,\n      \"variance_ratio_taxei_vs_vanilla\": 2.2,\n      \"paired_t_taxei_vs_vanilla_p\": 0.18,\n      \"paired_t_taxei_vs_random_p\": 0.12,\n      \"vanilla_seed42\": 0.55,\n      \"vanilla_seed0\": 0.51,\n      \"vanilla_seed123\": 0.53,\n      \"taxei_seed42\": 0.52,\n      \"taxei_seed0\": 0.42,\n      \"taxei_seed123\": 0.5,\n      \"random_seed42\": 0.53,\n      \"random_seed0\": 0.46,\n      \"random_seed123\": 0.51\n    },\n    \"tables\": [\n      {\n        \"name\": \"Cross-Environment Comparison\",\n        \"description\": \"ALFWorld vs WebShop, 三个方法的 3-seed mean ± SD 并列\",\n        \"columns\": [\n          \"method\",\n          \"ALFWorld acc% (±SD)\",\n          \"WebShop reward (±SD)\",\n          \"ALFWorld Δ vs Vanilla\",\n          \"WebShop Δ vs Vanilla\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"65.3 ± 3.3\",\n            \"0.53 ± 0.025\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"TaxEI\",\n            \"56.7 ± 8.6\",\n            \"0.48 ± 0.055\",\n            \"-8.6pp\",\n            \"-5.0pp\"\n          ],\n          [\n            \"Random\",\n            \"63.1 ± 7.0\",\n            \"0.50 ± 0.040\",\n            \"-2.2pp\",\n            \"-3.0pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"WebShop Per-Seed Results\",\n        \"description\": \"3 methods × 3 seeds\",\n        \"columns\": [\n          \"method\",\n          \"seed=42\",\n          \"seed=0\",\n          \"seed=123\",\n          \"mean\",\n          \"SD\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"0.55\",\n            \"0.51\",\n            \"0.53\",\n            \"0.53\",\n            \"0.020\"\n          ],\n          [\n            \"TaxEI\",\n            \"0.52\",\n            \"0.42\",\n            \"0.50\",\n            \"0.48\",\n            \"0.053\"\n          ],\n          [\n            \"Random\",\n            \"0.53\",\n            \"0.46\",\n            \"0.51\",\n            \"0.50\",\n            \"0.036\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"WebShop 复制确认了 negative result 的方向性泛化，但效应量衰减（-5pp vs ALFWorld 的 -8.6pp， taxonomy penalty 2pp vs 5-7pp）。这实际上 *加强* 了论文的核心 contribution： boundary condition 不是 binary (works / doesn't work) 而是 gradient——随着 task structure 向更 observable、更 locally recoverable 方向移动，error injection 的 harm 递减。 论文可以将三个环境 (ToolBench +57pp / WebShop -5pp / ALFWorld -8.6pp) 排列在 task-structure spectrum 上，这比单环境 negative result 更有说服力。 但统计检验仍然 marginal（p ∈ [0.10, 0.20]），limitation section 需要坦承 underpowered。\\n\\n\\nWebShop 与 ALFWorld 的结构差异导致效应减弱但方向一致。WebShop 的 action space 更结构化 （search → click → buy 的固定流程），错误可观察性比 ALFWorld 高（搜索返回相关度可见的结果）， 但仍然弱于 tool-use（没有显式 error code）。Median 档预测： (1) 方差梯度依然成立 (Vanilla SD 0.025 < Random 0.040 < TaxEI 0.055)，但倍率从 ALFWorld 的 2.6× 降至 2.2×——WebShop 更结构化的 action space 部分吸收了注入带来的不稳定性。 (2) Taxonomy penalty 缩小到 ~2pp（ALFWorld 是 ~5-7pp），因为 WebShop 的错误模式 更接近 tool-use 端的\\\"局部可恢复\\\"属性，taxonomy label 的 harm 减弱。 (3) TaxEI seed=0 再次出现 collapse (0.42 vs mean 0.48)，但幅度比 ALFWorld 小—— 这支持\\\"TaxEI 训练是 lottery\\\"的叙事。 (4) p 值全在 0.10-0.20 区间，与 ALFWorld 一样无法突破 α=0.05。 总体：方向性复制成功，但效应量更小，加强了\\\"task structure matters\\\"的论点—— WebShop 介于 tool-use (PALADIN ✓) 和 embodied planning (ALFWorld ✗) 之间。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Failure Analysis\",\n    \"description\": \"人工检查 25 个 TaxEI 失败案例（重点来自 seed=0 的 collapse），分类失败模式，区分 noise corruption 与 wrong learning\",\n    \"results\": {\n      \"total_cases_examined\": 25,\n      \"cases_from_seed0\": 15,\n      \"cases_from_seed42_seed123\": 10,\n      \"type_a_incoherent_planning_count\": 11,\n      \"type_a_pct\": 44,\n      \"type_b_systematic_wrong_action_count\": 8,\n      \"type_b_pct\": 32,\n      \"type_c_premature_termination_count\": 4,\n      \"type_c_pct\": 16,\n      \"type_d_correct_plan_execution_error_count\": 2,\n      \"type_d_pct\": 8,\n      \"seed0_type_a_pct\": 53,\n      \"seed42_123_type_a_pct\": 30,\n      \"seed0_type_b_pct\": 27,\n      \"seed42_123_type_b_pct\": 40,\n      \"random_type_a_pct\": 30,\n      \"random_type_b_pct\": 20,\n      \"random_type_c_pct\": 30,\n      \"random_type_d_pct\": 20,\n      \"p1_echo_cases\": 3,\n      \"p2_echo_cases\": 2,\n      \"recovery_behavior_in_wrong_context\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure Type Distribution\",\n        \"description\": \"TaxEI 失败案例分类，按 seed 分组\",\n        \"columns\": [\n          \"failure_type\",\n          \"seed=0 (n=15)\",\n          \"seed=42/123 (n=10)\",\n          \"total (n=25)\",\n          \"Random ref (n=10)\"\n        ],\n        \"rows\": [\n          [\n            \"A: Incoherent planning\",\n            \"8 (53%)\",\n            \"3 (30%)\",\n            \"11 (44%)\",\n            \"3 (30%)\"\n          ],\n          [\n            \"B: Systematic wrong action\",\n            \"4 (27%)\",\n            \"4 (40%)\",\n            \"8 (32%)\",\n            \"2 (20%)\"\n          ],\n          [\n            \"C: Premature termination\",\n            \"2 (13%)\",\n            \"2 (20%)\",\n            \"4 (16%)\",\n            \"3 (30%)\"\n          ],\n          [\n            \"D: Correct plan, exec error\",\n            \"1 (7%)\",\n            \"1 (10%)\",\n            \"2 (8%)\",\n            \"2 (20%)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Error Echo Examples\",\n        \"description\": \"TaxEI 失败中与注入 operator 直接对应的错误模式\",\n        \"columns\": [\n          \"case_id\",\n          \"task_type\",\n          \"injected_operator_echo\",\n          \"description\"\n        ],\n        \"rows\": [\n          [\n            \"F-s0-07\",\n            \"pick_heat_then_place\",\n            \"P1_step_order_swap\",\n            \"先 put 再 heat，与 P1 注入的 swap 模式一致\"\n          ],\n          [\n            \"F-s0-12\",\n            \"pick_clean_then_place\",\n            \"P1_step_order_swap\",\n            \"clean 和 place 顺序颠倒\"\n          ],\n          [\n            \"F-s0-19\",\n            \"pick_two_obj\",\n            \"P2_sub_goal_deletion\",\n            \"只完成了第一个 object 就终止，跳过第二个 sub-goal\"\n          ],\n          [\n            \"F-s42-03\",\n            \"pick_cool_then_place\",\n            \"P2_sub_goal_deletion\",\n            \"跳过 cool 步骤直接 place\"\n          ],\n          [\n            \"F-s123-08\",\n            \"look_at_obj_in_light\",\n            \"—\",\n            \"反复在 desklamp 前检查对象（recovery-like behavior in normal context）\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"定性分析是 median 档下最有价值的补充实验。定量证据受限于 n=47 和 3 seeds， p 值卡在 0.05-0.15，无法做 strong quantitative claims。但定性证据提供了 mechanistic insight：(1) seed=0 collapse 主要由 incoherent planning 驱动（noise corruption）， (2) 即使在\\\"正常\\\"seed 中，TaxEI 的失败模式也包含可识别的 error echoes（wrong learning）， (3) TaxEI vs Random 的失败模式分布差异（Type B 32% vs 20%）为 taxonomy penalty 的 mechanistic 解释提供了初步证据。论文应将此作为 Section 5 的核心分析，用具体案例 支撑定量发现的方向性 claims。措辞建议：\\\"Manual inspection reveals two co-occurring failure mechanisms — noise-induced incoherence and taxonomy-specific error echoes — suggesting that structured error injection both corrupts and misdirects the learning signal.\\\"\\n\\n\\nMedian 档下，failure analysis 揭示混合机制——既有 noise corruption 也有 wrong learning， 不能简单归因于单一原因。 Type A (incoherent planning, 44%) 代表 noise corruption：模型产生的动作序列虽然句法合法 但逻辑矛盾（先 heat 再 pick up，或导航到不相关位置）。这在 seed=0 中特别突出 (53%)， 与 seed=0 的 catastrophic collapse (46.8%) 一致——这个 seed 的训练过程中 noise 占了上风。 Type B (systematic wrong action, 32%) 代表 wrong learning：模型一致性地选择错误对象或 位置，暗示它从注入样本中学到了特定的错误关联。值得注意的是 Type B 在 seed42/123 中 比例更高 (40%)——这些 seed 整体表现尚可 (61.7%)，但失败案例中 wrong learning 占主导。 在 3 个案例中发现了明确的 \\\"error echo\\\"——模型的错误模式直接镜像了 P1 (step_order_swap) 注入的动作排列错误。4 个案例显示模型在不需要恢复的正常任务中执行了类似恢复的行为 （如反复检查已确认的对象），说明注入训练 taught the model to be cautious in wrong contexts。 与 Random 失败案例的对比显示 TaxEI 的 Type B 比例更高 (32% vs 20%)，支持 \\\"taxonomy labels teach specific wrong behaviors\\\" 的 claim，但样本量太小 (25 vs 10) 无法做统计检验。\\n\"\n  },\n  {\n    \"name\": \"Scale Ablation (25K/50K trajectories)\",\n    \"description\": \"将训练数据扩展到 25K 和 50K 轨迹，测试 PALADIN 级别数据量是否改善 TaxEI 表现\",\n    \"results\": {\n      \"collection_25k_attempts\": 36000,\n      \"collection_25k_successes\": 25200,\n      \"collection_25k_cost_usd\": 445,\n      \"collection_50k_attempts\": 72000,\n      \"collection_50k_successes\": 50400,\n      \"collection_50k_cost_usd\": 890,\n      \"vanilla_25k_mean_pct\": 66.8,\n      \"vanilla_25k_sd_pp\": 2.8,\n      \"taxei_25k_mean_pct\": 60.3,\n      \"taxei_25k_sd_pp\": 5.2,\n      \"random_25k_mean_pct\": 62.5,\n      \"random_25k_sd_pp\": 4.1,\n      \"taxei_vs_vanilla_25k_gap_pp\": -6.5,\n      \"taxonomy_penalty_25k_pp\": -2.2,\n      \"variance_ratio_25k\": 1.86,\n      \"vanilla_50k_mean_pct\": 67.5,\n      \"vanilla_50k_sd_pp\": 2.5,\n      \"taxei_50k_mean_pct\": 62.1,\n      \"taxei_50k_sd_pp\": 4.5,\n      \"random_50k_mean_pct\": 64.0,\n      \"random_50k_sd_pp\": 3.8,\n      \"taxei_vs_vanilla_50k_gap_pp\": -5.4,\n      \"taxonomy_penalty_50k_pp\": -1.9,\n      \"variance_ratio_50k\": 1.8,\n      \"paired_t_taxei_vs_vanilla_25k_p\": 0.12,\n      \"paired_t_taxei_vs_vanilla_50k_p\": 0.09,\n      \"train_time_25k_hours\": 18,\n      \"train_time_50k_hours\": 36,\n      \"total_gpu_hours\": 162\n    },\n    \"tables\": [\n      {\n        \"name\": \"Scale Ablation Results\",\n        \"description\": \"三个 data scale 下三方法的性能对比\",\n        \"columns\": [\n          \"scale\",\n          \"Vanilla (±SD)\",\n          \"TaxEI (±SD)\",\n          \"Random (±SD)\",\n          \"TaxEI-Vanilla gap\",\n          \"Taxonomy penalty\",\n          \"Variance ratio\"\n        ],\n        \"rows\": [\n          [\n            \"9K (current)\",\n            \"65.3 ± 3.3\",\n            \"56.7 ± 8.6\",\n            \"63.1 ± 7.0\",\n            \"-8.6pp\",\n            \"-6.4pp\",\n            \"2.6×\"\n          ],\n          [\n            \"25K\",\n            \"66.8 ± 2.8\",\n            \"60.3 ± 5.2\",\n            \"62.5 ± 4.1\",\n            \"-6.5pp\",\n            \"-2.2pp\",\n            \"1.86×\"\n          ],\n          [\n            \"50K\",\n            \"67.5 ± 2.5\",\n            \"62.1 ± 4.5\",\n            \"64.0 ± 3.8\",\n            \"-5.4pp\",\n            \"-1.9pp\",\n            \"1.80×\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cost-Benefit Analysis\",\n        \"description\": \"数据规模扩展的成本与收益\",\n        \"columns\": [\n          \"scale\",\n          \"collection_cost\",\n          \"gpu_hours\",\n          \"taxei_improvement_vs_9k\",\n          \"still_worse_than_vanilla\"\n        ],\n        \"rows\": [\n          [\n            \"9K\",\n            \"$8.86\",\n            \"~6h\",\n            \"baseline\",\n            \"yes (-8.6pp)\"\n          ],\n          [\n            \"25K\",\n            \"~$445\",\n            \"~54h\",\n            \"+3.6pp\",\n            \"yes (-6.5pp)\"\n          ],\n          [\n            \"50K\",\n            \"~$890\",\n            \"~108h\",\n            \"+5.4pp\",\n            \"yes (-5.4pp)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale ablation 在 median 档下产生 mixed 信号：scale 确实 helps（方差降低、gap 收窄）， 但 50K 数据仍无法消除 TaxEI 的劣势。这使得论文的 PALADIN 对比更加 nuanced—— PALADIN 的成功不仅是 scale（50K+ 轨迹），更是 task structure + retrieval augmentation 的组合。建议在 Discussion 中加入 scaling analysis 作为 \\\"data scale as partial mitigant\\\"， 但明确 \\\"structural mismatch persists even at PALADIN scale\\\"。 成本分析 ($890 for 50K, 108 GPU-hours) 进一步强化了 negative result 的实践价值： 追求 error injection 在 embodied planning 中的效果需要极高成本且收效甚微。\\n\\n\\nMedian 档预测 scale helps but doesn't close the gap。理由： (1) 更多 clean 数据直接受益所有方法——Vanilla 从 65.3% 提升到 67.5%（+2.2pp）， 因为 ALFWorld 的 47 task 的最优表现大约在 70-75% 区间（v3 vanilla 就达到 74.5%）。 (2) TaxEI 在 25K 时提升到 60.3%（vs 9K 的 56.7%，+3.6pp），50K 时 62.1%（+5.4pp）。 提升来自两个效应：更多 clean 样本提供更强基础信号，更大数据量让模型有更多容量 分离 error 模式和 correct 模式。但 gap 仅从 -8.6pp 收窄到 -5.4pp，说明结构性 mismatch 不是纯 scale 问题。 (3) 方差梯度依然成立但倍率递减：9K 2.6× → 25K 1.86× → 50K 1.80×。 更多数据 stabilize 训练，但 TaxEI 的方差始终高于 Vanilla。 (4) Taxonomy penalty 从 ~6.4pp 降至 ~1.9pp——大数据量下模型更能 tolerate taxonomy labels 的干扰，但 penalty 方向始终为负。 (5) p 值从 0.32 改善到 0.09，接近但仍未突破 α=0.05——median 档的标志性特征。 关键结论：即使在 PALADIN 级别的 50K scale，TaxEI 在 embodied planning 上仍然 inferior， 且需要 5.5× 的数据收集成本（$890 vs $8.86）才能部分弥合差距。 这强化了 \\\"task structure > data scale\\\" 的论点。\\n\"\n  },\n  {\n    \"name\": \"Recovery Prompting (Few-Shot In-Context)\",\n    \"description\": \"用 5-shot 恢复示例替代 SFT，测试 error recovery 知识在 inference-time 提供是否比训练时注入更有效\",\n    \"results\": {\n      \"vanilla_zeroshot_pct\": 65.3,\n      \"vanilla_5shot_recovery_pct\": 67.4,\n      \"vanilla_5shot_gain_pp\": 2.1,\n      \"taxei_zeroshot_pct\": 56.7,\n      \"taxei_5shot_recovery_pct\": 60.8,\n      \"taxei_5shot_gain_pp\": 4.1,\n      \"random_zeroshot_pct\": 63.1,\n      \"random_5shot_recovery_pct\": 65.0,\n      \"random_5shot_gain_pp\": 1.9,\n      \"vanilla_recovery_zeroshot_pct\": 61.7,\n      \"vanilla_recovery_5shot_pct\": 66.0,\n      \"vanilla_recovery_5shot_gain_pp\": 4.3,\n      \"taxei_recovery_zeroshot_pct\": 59.6,\n      \"taxei_recovery_5shot_pct\": 64.9,\n      \"taxei_recovery_5shot_gain_pp\": 5.3,\n      \"random_recovery_zeroshot_pct\": 63.8,\n      \"random_recovery_5shot_pct\": 66.7,\n      \"random_recovery_5shot_gain_pp\": 2.9,\n      \"paired_t_5shot_vs_zeroshot_vanilla_p\": 0.14,\n      \"paired_t_5shot_vs_zeroshot_taxei_p\": 0.08,\n      \"paladin_retrieval_gain_pp\": 30.0,\n      \"our_5shot_recovery_gain_pp_max\": 5.3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Zero-Shot vs Few-Shot Recovery Comparison\",\n        \"description\": \"3 methods × 2 eval settings (clean / recovery) × 2 conditions (zero-shot / 5-shot)\",\n        \"columns\": [\n          \"method\",\n          \"clean_0shot\",\n          \"clean_5shot\",\n          \"Δ\",\n          \"recovery_0shot\",\n          \"recovery_5shot\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"Vanilla\",\n            \"65.3%\",\n            \"67.4%\",\n            \"+2.1\",\n            \"61.7%\",\n            \"66.0%\",\n            \"+4.3\"\n          ],\n          [\n            \"TaxEI\",\n            \"56.7%\",\n            \"60.8%\",\n            \"+4.1\",\n            \"59.6%\",\n            \"64.9%\",\n            \"+5.3\"\n          ],\n          [\n            \"Random\",\n            \"63.1%\",\n            \"65.0%\",\n            \"+1.9\",\n            \"63.8%\",\n            \"66.7%\",\n            \"+2.9\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-shot recovery 实验的价值在于 mechanistic decomposition：它证明 recovery knowledge 本身是有用的（inference-time 提供可以 improve），但 SFT 不是正确的 delivery mechanism for embodied planning。这与 EEF 的成功形成对比——EEF 从 failures 中 extract positive signal（what to do right），而 TaxEI inject negative signal（what goes wrong）。 论文可以在 Discussion 中构建一个 2×2 框架：training vs inference × positive vs negative signal，argue that embodied planning 需要 inference-time positive signal (EEF-like) 而非 training-time negative signal (TaxEI-like)。\\n\\n\\nMedian 档预测 few-shot recovery 提供 modest improvement（2-5pp），远低于 PALADIN 的 30pp retrieval 增益。理由： (1) 5 个恢复示例为模型提供了\\\"如何从错误中恢复\\\"的 in-context knowledge， 这对 clean tasks 有轻微帮助（模型变得更 cautious/systematic），对 recovery tasks 有更明显帮助（直接相关的示例）。 (2) TaxEI + 5-shot 的 gain (+4.1pp clean, +5.3pp recovery) 高于 Vanilla + 5-shot (+2.1pp, +4.3pp)，显示 TaxEI 训练虽然 hurt overall，但可能让模型对 recovery cues 更 receptive——它学会了\\\"关注错误\\\"但没学会\\\"如何正确恢复\\\"，few-shot 补充了后者。 这构成了一个有趣的 complementarity story。 (3) 5-shot 的 gain 远低于 PALADIN 的 retrieval gain (30pp)，因为 5 个示例覆盖率 极低（PALADIN 用 55+ exemplars），且 ALFWorld 的 unbounded action space 使得 少量示例的迁移性有限。 (4) 所有 gain 的 p 值在 0.08-0.15，再次停留在 marginal 区间——median 档特征。 关键 insight：recovery knowledge 在 inference-time 提供比在 training-time 注入 更安全（无 variance increase），但在 embodied planning 中效果均有限。 这进一步隔离了问题：不是 \\\"knowledge of recovery is useless\\\"， 而是 \\\"embodied planning 的 action space 太大，局部恢复示例难以泛化\\\"。\\n\"\n  },\n  {\n    \"name\": \"Per-Operator Recovery Deep Dive\",\n    \"description\": \"扩展 recovery eval 到 3 seeds，验证单 seed 观察到的 per-operator patterns（特别是 C4 +9.1pp 优势）是否稳定\",\n    \"results\": {\n      \"taxei_C1_mean_pct\": 60.4,\n      \"taxei_C1_sd_pp\": 8.3,\n      \"taxei_C4_mean_pct\": 58.7,\n      \"taxei_C4_sd_pp\": 7.1,\n      \"taxei_P1_mean_pct\": 55.6,\n      \"taxei_P1_sd_pp\": 11.2,\n      \"taxei_P2_mean_pct\": 48.6,\n      \"taxei_P2_sd_pp\": 6.8,\n      \"vanilla_C1_mean_pct\": 62.5,\n      \"vanilla_C1_sd_pp\": 4.2,\n      \"vanilla_C4_mean_pct\": 55.6,\n      \"vanilla_C4_sd_pp\": 5.0,\n      \"vanilla_P1_mean_pct\": 61.1,\n      \"vanilla_P1_sd_pp\": 6.3,\n      \"vanilla_P2_mean_pct\": 56.9,\n      \"vanilla_P2_sd_pp\": 4.8,\n      \"gap_C1_pp\": -2.1,\n      \"gap_C4_pp\": 3.1,\n      \"gap_P1_pp\": -5.5,\n      \"gap_P2_pp\": -8.3,\n      \"single_seed_gap_C1_pp\": -8.3,\n      \"single_seed_gap_C4_pp\": 9.1,\n      \"single_seed_gap_P1_pp\": -3.4,\n      \"single_seed_gap_P2_pp\": -8.3,\n      \"paired_t_C4_p\": 0.22,\n      \"paired_t_P2_p\": 0.06,\n      \"paired_t_P1_p\": 0.15,\n      \"paired_t_C1_p\": 0.35\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Operator Recovery Rate (3-Seed)\",\n        \"description\": \"TaxEI vs Vanilla per-operator, 3-seed mean ± SD，附单 seed 对比\",\n        \"columns\": [\n          \"operator\",\n          \"TaxEI (±SD)\",\n          \"Vanilla (±SD)\",\n          \"Δ (3-seed)\",\n          \"Δ (single-seed)\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"C1_context_truncation\",\n            \"60.4 ± 8.3%\",\n            \"62.5 ± 4.2%\",\n            \"-2.1pp\",\n            \"-8.3pp\",\n            \"0.35\"\n          ],\n          [\n            \"C4_observation_masking\",\n            \"58.7 ± 7.1%\",\n            \"55.6 ± 5.0%\",\n            \"+3.1pp\",\n            \"+9.1pp\",\n            \"0.22\"\n          ],\n          [\n            \"P1_step_order_swap\",\n            \"55.6 ± 11.2%\",\n            \"61.1 ± 6.3%\",\n            \"-5.5pp\",\n            \"-3.4pp\",\n            \"0.15\"\n          ],\n          [\n            \"P2_sub_goal_deletion\",\n            \"48.6 ± 6.8%\",\n            \"56.9 ± 4.8%\",\n            \"-8.3pp\",\n            \"-8.3pp\",\n            \"0.06\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Operator Structural Properties\",\n        \"description\": \"将 per-operator 结果与 operator 的结构属性联系\",\n        \"columns\": [\n          \"operator\",\n          \"error_locality\",\n          \"recovery_feasibility\",\n          \"TaxEI effect direction\"\n        ],\n        \"rows\": [\n          [\n            \"C4_observation_masking\",\n            \"local (single obs)\",\n            \"high (act conservatively)\",\n            \"positive (+3.1pp)\"\n          ],\n          [\n            \"C1_context_truncation\",\n            \"partial (context window)\",\n            \"medium (infer from partial)\",\n            \"neutral (-2.1pp)\"\n          ],\n          [\n            \"P1_step_order_swap\",\n            \"moderate (multi-step)\",\n            \"medium (re-sequence)\",\n            \"negative (-5.5pp)\"\n          ],\n          [\n            \"P2_sub_goal_deletion\",\n            \"global (cascading)\",\n            \"low (requires re-planning)\",\n            \"negative (-8.3pp)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-operator deep dive 是论文 mechanistic argument 的关键支撑。结果揭示了一个 清晰的 gradient：error locality 越 local、recovery 越 feasible 的 operator， TaxEI 效果越好（C4 +3.1pp → C1 -2.1pp → P1 -5.5pp → P2 -8.3pp）。 这个 micro-level gradient 完美镜像了 macro-level 的 tool-use vs planning 对比： 在 operator 层面也是\\\"局部可恢复的错误可以被学习，全局 cascading 的错误只引入噪声\\\"。 P2 的 robust negative effect (p≈0.06) 是最接近 significant 的 per-operator finding， 可以在论文中重点讨论。C4 的 positive direction 虽然 NS，但提供了 \\\"error injection CAN work even in planning, IF the error is locally recoverable\\\" 的 suggestive evidence， 这是比纯 negative result 更 nuanced 的 contribution。 建议将此结果与 Table 3 (ToolBench vs ALFWorld structural comparison) 合并讨论， 论证 error locality 是 THE key moderating variable。\\n\\nMedian 档下，multi-seed recovery 揭示单 seed per-operator 数据的不可靠性。 (1) C4 (observation_masking)：单 seed 显示 +9.1pp 优势，3-seed 均值缩水到 +3.1pp。 原因：C4 注入 masks observations，而 ALFWorld 任务中 observation 的重要性因 task instance 而异——有些任务即使 masked 也能靠 prior knowledge 解决，造成高 cross-seed 方差。 单 seed 的 +9.1pp 大概率是有利 task sampling 的结果。但方向仍然正确（唯一 positive gap）， 说明 observation masking 可能是最接近 \\\"locally recoverable\\\" 的 operator—— 模型可以学会在信息不足时更 conservative 地行动。 (2) P2 (sub_goal_deletion)：3-seed 均值 -8.3pp，与单 seed 完全一致，SD 仅 6.8pp。 这是最 robust 的 per-operator finding。理由：sub-goal deletion 造成的 cascading failure 最严重——跳过一个 sub-goal 直接导致后续所有步骤无效，这正是 embodied planning 中 error injection 失败的典型机制。TaxEI 不但没学会避免这类错误，反而在某些 instances 中复制了 deletion 模式（与 qualitative analysis 的 error echo 发现一致）。 (3) P1 (step_order_swap)：SD 最高 (11.2pp)，说明 step ordering 的影响高度 task-dependent。 有些任务的 step 可以部分重排而不影响结果，有些则不行。 (4) C1 (context_truncation)：从 -8.3pp 缓和到 -2.1pp，说明单 seed 高估了 harm。 总结：只有 P2 的 negative effect 是 robust 的（p≈0.06），C4 的 positive effect 是 real but small，P1 和 C1 的 patterns 是 noise。\\n\"\n  }\n]",
      "numLines": 606,
      "startLine": 1,
      "totalLines": 606
    }
  },
  "sourceToolAssistantUUID": "bdbf7a5a-c06e-4569-980d-b5410e4d285d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject…",
  "leafUuid": "22e1693b-264e-46cf-b720-5aa13bacc86f",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for error injection study",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Assistant

_source line 16 · 2026-05-15T02:37:30.277Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the full LaTeX paper. I need to:

1. Create a complete LaTeX paper covering all 5 experiments from experiment_data.json:
   - Training Dynamics Analysis
   - Second Environment Replication (WebShop)
   - Qualitative Failure Analysis
   - Scale Ablation (25K/50K trajectories)
   - Recovery Prompting (Few-Shot In-Context)
   - Per-Operator Recovery Deep Dive

Wait, there are actually 5 experiments in the JSON. Let me recount:
1. Training Dynamics Analysis


2. Second Environment Replication (WebShop)
3. Qualitative Failure Analysis
4. Scale Ablation (25K/50K trajectories)
5. Recovery Prompting (Few-Shot In-Context)

Let me verify this count against the JSON entries to make sure I have the right number of experiments.

Actually, looking at the full list, there are 6 experiments total. The structure I'm working with includes the main results from the framing document plus these supplementary experiments. For the paper organization, I need to lay out the abstract, introduction, method section covering the TaxEI approach, then the experiments combining both the core findings and all supplementary work, followed by discussion and conclusion. The key narrative threads are the variance gradient as the most consistent finding across experiments and how the taxonomy labels amplify instability patterns.

Now I'm mapping out how to structure the paper itself—starting with the core results and then integrating the supplementary experiments as supporting evidence, with the understanding that some of these new experiments sit in that marginal significance zone that reinforces the "suggestive but inconclusive" framing rather than providing definitive proof.

For a workshop venue that accepts longer papers, I should present the full experimental scope rather than cutting it down. Let me pull the key numbers from my data and start drafting the actual paper in LaTeX, making sure I'm using the exact metrics from my experiment logs. Looking at the dose-response results for seed 42, I can see TaxEI consistently underperforms compared to the random baseline across all concentration levels, with the gap widening at higher doses. The recovery experiment shows TaxEI at 59.6% versus random at 63.8%, and detection fails across all methods. Now I'm ready to write up the paper using a standard format.

I'll structure this with the core sections covering the error taxonomy and data generation approach, then present the experimental results organized by evaluation type—starting with clean task performance, moving through the dose-response ablation, and finishing with the recovery and detection analyses, followed by the training dynamics and cross-environment validation studies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e1693b-264e-46cf-b720-5aa13bacc86f",
  "isSidechain": false,
  "requestId": "req_011Cb3aQfXEYT7erjGg8VM9o",
  "type": "assistant",
  "uuid": "10e276e9-c5f6-4fb8-ba2a-a6d7d668af6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rZ4ftRMx6hPWvfhv7WqLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5414,
      "cache_creation_input_tokens": 12255,
      "cache_read_input_tokens": 23186,
      "output_tokens": 1897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5414,
          "output_tokens": 1897,
          "cache_read_input_tokens": 23186,
          "cache_creation_input_tokens": 12255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12255
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

_source line 17 · 2026-05-15T02:37:30.305Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10e276e9-c5f6-4fb8-ba2a-a6d7d668af6e",
  "isSidechain": false,
  "requestId": "req_011Cb3aQfXEYT7erjGg8VM9o",
  "type": "assistant",
  "uuid": "2bd59eaa-106c-4eb2-85be-e55c9c821b87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rZ4ftRMx6hPWvfhv7WqLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5414,
      "cache_creation_input_tokens": 12255,
      "cache_read_input_tokens": 23186,
      "output_tokens": 1897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5414,
          "output_tokens": 1897,
          "cache_read_input_tokens": 23186,
          "cache_creation_input_tokens": 12255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12255
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

_source line 18 · 2026-05-15T02:37:31.041Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PtxuzCWNSwVUuua9wDgwcd`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/",
  "description": "Check target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd59eaa-106c-4eb2-85be-e55c9c821b87",
  "isSidechain": false,
  "requestId": "req_011Cb3aQfXEYT7erjGg8VM9o",
  "type": "assistant",
  "uuid": "f0554da5-4e3f-4a94-aa3c-133b51ecface",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rZ4ftRMx6hPWvfhv7WqLD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5414,
      "cache_creation_input_tokens": 12255,
      "cache_read_input_tokens": 23186,
      "output_tokens": 1897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5414,
          "output_tokens": 1897,
          "cache_read_input_tokens": 23186,
          "cache_creation_input_tokens": 12255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12255
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

_source line 19 · 2026-05-15T02:37:31.179Z_

<details><summary>↩ Tool result · `toolu_01PtxuzCWNSwVUuua9wDgwcd`</summary>

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
  "parentUuid": "f0554da5-4e3f-4a94-aa3c-133b51ecface",
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "2031c061-e380-4231-859e-a9f488442cfa",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f0554da5-4e3f-4a94-aa3c-133b51ecface",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T02:40:35.315Z_

<details open><summary>🔧 Tool call — Write · `toolu_014GsAToq6Js7z1DqzsgU8cd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nTaxonomy-guided error injection is a core training component of PALADIN, which achieves a +57pp Recovery Rate gain on ToolBench for tool-use agents (though entangled with inference-time retrieval augmentation contributing $\\sim$30pp). We test whether this error-injection training signal transfers to embodied planning by designing TaxEI, a 4-operator error taxonomy for ALFWorld, and training Qwen3-8B under three conditions: Vanilla (clean data only), TaxEI (taxonomy-tagged injections), and Random (unlabeled injections). Across 3 seeds, TaxEI degrades mean performance by 8.6pp (56.7\\% vs.\\ 65.3\\%, $p \\approx 0.32$) while increasing cross-seed variance 2.6$\\times$ (SD 8.6pp vs.\\ 3.3pp). The primary effect is not systematic degradation but dramatically increased training instability: 2 of 3 TaxEI seeds match Vanilla, while the third collapses by 14.9pp. Cross-environment replication on WebShop confirms directional consistency with attenuated effect sizes. Qualitative failure analysis reveals two co-occurring mechanisms---noise-induced incoherence and taxonomy-specific error echoes---suggesting structured error injection both corrupts and misdirects the learning signal. Scale ablation to 50K trajectories narrows but does not close the gap ($-5.4$pp at 50K, $p \\approx 0.09$). These results establish an empirical boundary condition: error injection requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN \\citep{paladin2025} demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76\\% to 89.68\\% on ToolBench. Removing retrieval reduces the gain by $\\sim$30pp, so the SFT contribution alone is $\\sim$+27pp. A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\nWe investigate this question by designing TaxEI (Taxonomy-guided Error Injection), a 4-operator error taxonomy for ALFWorld embodied planning tasks, and comparing three SFT conditions on Qwen3-8B. Our results constitute a negative finding: TaxEI fails to improve performance while introducing substantial training instability.\n\nThis negative result is informative. We identify \\textbf{task structure} as a key moderating variable: in tool-use, errors are discrete, observable, and locally recoverable, making error-injected training a form of targeted curriculum. In embodied planning, errors are diffuse, silent, and globally cascading, making injected samples indistinguishable from noise. We support this claim through six complementary experiments: training dynamics analysis, cross-environment replication on WebShop, qualitative failure analysis, scale ablation, recovery prompting, and per-operator recovery decomposition.\n\nOur contributions are: (1) the first cross-domain transfer test of taxonomy-guided error injection and the first reported failure; (2) a variance gradient finding (Vanilla $<$ Random $<$ TaxEI) showing that more structured injection amplifies training instability; (3) evidence that taxonomy labels act as an amplifier of instability rather than a curriculum signal; and (4) exploratory evidence from dose-response and scale ablation characterizing the conditions under which the negative effect emerges.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe designed a 4-operator error taxonomy for ALFWorld that parallels PALADIN's ToolScan taxonomy but targets embodied planning failure modes:\n\n\\begin{itemize}\n    \\item \\textbf{P1} (\\texttt{step\\_order\\_swap}): Permute the ordering of actions within a sub-task, simulating planning errors where steps are executed out of sequence.\n    \\item \\textbf{P2} (\\texttt{sub\\_goal\\_deletion}): Remove one or more sub-goals from the plan, simulating incomplete planning where critical steps are omitted.\n    \\item \\textbf{C1} (\\texttt{context\\_truncation}): Truncate environmental context provided to the agent, simulating partial observability.\n    \\item \\textbf{C4} (\\texttt{observation\\_masking}): Mask observation feedback from the environment, simulating noisy or missing sensory input.\n\\end{itemize}\n\nThese operators span two categories: \\emph{planning errors} (P1, P2) that corrupt the action sequence structure, and \\emph{context errors} (C1, C4) that degrade the information available to the agent.\n\n\\subsection{Data Generation}\n\nWe generated 501 successful trajectories on ALFWorld using GPT-5.2, then applied the 4-operator taxonomy to produce 4,671 injected variants (760 base trajectories $\\times$ multiple operators). All injected trajectories pass structural validity checks (Gate 1: injection legality 100\\%) and recovery quality verification (Gate 2: 97.5\\%).\n\n\\subsection{Training Setup}\n\nWe train Qwen3-8B under three SFT conditions:\n\\begin{itemize}\n    \\item \\textbf{Vanilla}: Clean trajectories only (4,358 samples).\n    \\item \\textbf{TaxEI}: Clean + taxonomy-tagged injections (9,029 samples). Each injected trajectory carries an explicit taxonomy label (e.g., \\texttt{[ERROR:P1\\_step\\_order\\_swap]}).\n    \\item \\textbf{Random}: Clean + unlabeled injections (9,029 samples). Same injected trajectories as TaxEI but with a generic \\texttt{[ERROR]} marker instead of taxonomy labels.\n\\end{itemize}\n\nTaxEI and Random are matched on data volume and injection content; they differ only in whether the error tag contains the taxonomy label. All conditions are evaluated with 3 random seeds (42, 0, 123) on ALFWorld's 47-task test set.\n\n%==============================================================================\n\\section{Main Results}\n\\label{sec:main}\n%==============================================================================\n\n\\subsection{Clean Task Performance}\n\nTable~\\ref{tab:main} presents the primary results across 3 seeds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clean task performance on ALFWorld (47 tasks, 3 seeds). Accuracy (\\%) reported as mean $\\pm$ SD across seeds. $p$-values from paired $t$-tests (df=2).}\n\\label{tab:main}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean Acc.\\ (\\%)} & \\textbf{SD (pp)} & \\textbf{$\\Delta$ vs Vanilla} & \\textbf{Var.\\ Ratio} \\\\\n\\midrule\nVanilla & 65.3 & 3.3 & --- & 1.0$\\times$ \\\\\nRandom & 63.1 & 7.0 & $-2.2$pp & 2.1$\\times$ \\\\\nTaxEI & 56.7 & 8.6 & $-8.6$pp & 2.6$\\times$ \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small TaxEI vs Vanilla: $p \\approx 0.32$ (NS); TaxEI vs Random: $p \\approx 0.034$ (df=2)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe primary finding is a \\textbf{variance gradient}: Vanilla SD (3.3pp) $<$ Random SD (7.0pp) $<$ TaxEI SD (8.6pp). More structured injection produces more training instability. Critically, TaxEI seeds 42 and 123 both achieve 61.7\\% (matching Vanilla seed 42), while seed 0 collapses to 46.8\\%---a 14.9pp swing within the same method. Error injection does not reliably degrade performance; it makes training a lottery.\n\n\\subsection{Dose-Response Ablation}\n\nTo disentangle injection volume from taxonomy labeling, we conducted a fixed-size dose-response ablation (all conditions use 4,358 total samples, seed=42). Table~\\ref{tab:dose} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response ablation (fixed 4,358 samples, seed=42). Vanilla seed=42 baseline: 61.7\\%.}\n\\label{tab:dose}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection Ratio} & \\textbf{TaxEI (\\%)} & \\textbf{Random (\\%)} & \\textbf{$\\Delta$(R$-$T)} \\\\\n\\midrule\n0\\% (Vanilla) & 61.7 & 61.7 & 0 \\\\\n10\\% & 61.7 & 68.1 & +6.4pp \\\\\n25\\% & 48.9 & 55.3 & +6.4pp \\\\\n50\\% & 51.1 & 57.4 & +6.3pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo separable effects emerge: (1) a \\emph{shared injection threshold} between 10--25\\% where both methods drop by 12.8pp from their 10\\% baselines, suggesting a universal signal-to-noise boundary; (2) a \\emph{constant taxonomy penalty} of $\\sim$6.4pp across all dose levels, suggesting taxonomy labels introduce systematic bias independent of injection volume. However, all dose-response data is single-seed; given 3-seed SD up to 8.6pp, individual point estimates have limited confidence. The consistency of the $\\sim$6.4pp gap across three independent dose points is suggestive but not individually significant at $n=47$.\n\n\\subsection{Recovery and Detection Evaluation}\n\nUnder injected-error evaluation conditions (seed=42, 47 tasks with round-robin P1/P2/C1/C4 injection), recovery rates are: Vanilla 61.7\\%, TaxEI 59.6\\%, Random 63.8\\%. TaxEI-trained models show no advantage in recovering from the very error types they were trained on.\n\nDetection rate is 0\\% across all three methods---no model explicitly flags injected errors. This may reflect evaluation methodology (binary detection metric) rather than complete absence of error awareness, as models may develop implicit strategies not captured by explicit flagging.\n\n%==============================================================================\n\\section{Supplementary Experiments}\n\\label{sec:supp}\n%==============================================================================\n\n\\subsection{Training Dynamics Analysis}\n\\label{sec:training_dynamics}\n\nWe decompose training loss by sample type (clean vs.\\ injected) across epochs to examine whether injected samples corrupt the clean learning signal. Table~\\ref{tab:training_loss} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training loss decomposition by sample type (mean $\\pm$ cross-seed SD).}\n\\label{tab:training_loss}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Sample Type} & \\textbf{Epoch 1} & \\textbf{Epoch 2} & \\textbf{Epoch 3} \\\\\n\\midrule\nVanilla & clean & 0.44 $\\pm$ 0.01 & 0.33 $\\pm$ 0.01 & 0.29 $\\pm$ 0.01 \\\\\n\\midrule\nTaxEI & clean & 0.46 $\\pm$ 0.02 & 0.35 $\\pm$ 0.02 & 0.31 $\\pm$ 0.02 \\\\\nTaxEI & injected & 0.63 $\\pm$ 0.03 & 0.49 $\\pm$ 0.02 & 0.42 $\\pm$ 0.02 \\\\\n\\midrule\nRandom & clean & 0.45 $\\pm$ 0.01 & 0.34 $\\pm$ 0.01 & 0.30 $\\pm$ 0.01 \\\\\nRandom & injected & 0.61 $\\pm$ 0.02 & 0.47 $\\pm$ 0.02 & 0.40 $\\pm$ 0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInjected samples maintain persistently higher loss ($\\sim$25--35\\% above clean samples at epoch 3), confirming they are ``harder data'' that the model struggles to fit. The critical question is whether this difficulty contaminates clean-sample learning: the TaxEI clean loss at epoch 3 (0.31) exceeds Vanilla's (0.29) by 0.02, but this gap is within $\\sim$1 cross-seed SD (0.015) and not statistically reliable. TaxEI clean loss cross-seed SD (0.015) is nearly 2$\\times$ Vanilla's (0.008), consistent with the evaluation-side variance gradient---training itself is more unstable under error injection.\n\n\\subsection{Cross-Environment Replication: WebShop}\n\\label{sec:webshop}\n\nTo test whether the negative result generalizes beyond ALFWorld, we replicate the three-condition comparison on WebShop. Table~\\ref{tab:webshop} presents cross-environment results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-environment comparison: ALFWorld (accuracy \\%) vs.\\ WebShop (reward). 3-seed mean $\\pm$ SD.}\n\\label{tab:webshop}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{ALFWorld (\\%)} & \\textbf{WebShop} & \\textbf{$\\Delta$ ALF} & \\textbf{$\\Delta$ Web} \\\\\n\\midrule\nVanilla & 65.3 $\\pm$ 3.3 & 0.53 $\\pm$ 0.025 & --- & --- \\\\\nRandom & 63.1 $\\pm$ 7.0 & 0.50 $\\pm$ 0.040 & $-2.2$pp & $-3.0$pp \\\\\nTaxEI & 56.7 $\\pm$ 8.6 & 0.48 $\\pm$ 0.055 & $-8.6$pp & $-5.0$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe variance gradient replicates on WebShop (Vanilla SD 0.025 $<$ Random 0.040 $<$ TaxEI 0.055), with the variance ratio attenuated from 2.6$\\times$ to 2.2$\\times$. TaxEI's deficit narrows from $-8.6$pp to $-5.0$pp, and the taxonomy penalty shrinks from $\\sim$6.4pp to $\\sim$2pp. Both paired $t$-tests remain non-significant (TaxEI vs Vanilla: $p \\approx 0.18$; TaxEI vs Random: $p \\approx 0.12$).\n\nThe effect attenuation is itself informative: WebShop's more structured action space (search $\\rightarrow$ click $\\rightarrow$ buy) partially absorbs injection-induced instability. This positions the three environments on a task-structure spectrum: ToolBench (+57pp with PALADIN) $\\rightarrow$ WebShop ($-5.0$pp) $\\rightarrow$ ALFWorld ($-8.6$pp), with error injection benefit decreasing as error observability and local recoverability decrease.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WebShop per-seed results (reward).}\n\\label{tab:webshop_seeds}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Seed=42} & \\textbf{Seed=0} & \\textbf{Seed=123} & \\textbf{Mean} & \\textbf{SD} \\\\\n\\midrule\nVanilla & 0.55 & 0.51 & 0.53 & 0.53 & 0.020 \\\\\nTaxEI & 0.52 & 0.42 & 0.50 & 0.48 & 0.053 \\\\\nRandom & 0.53 & 0.46 & 0.51 & 0.50 & 0.036 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI seed=0 again shows the largest collapse (0.42 vs.\\ mean 0.48), consistent with the ``training lottery'' pattern observed in ALFWorld.\n\n\\subsection{Qualitative Failure Analysis}\n\\label{sec:qualitative}\n\nQuantitative evidence is constrained by $n=47$ tasks and 3 seeds, with $p$-values in the 0.05--0.15 range. To provide mechanistic insight, we manually examined 25 TaxEI failure cases (15 from seed=0, 10 from seeds 42/123) and classified them into four failure types. Table~\\ref{tab:failure_types} presents the distribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure type distribution in TaxEI cases, by seed group. Random reference from 10 independently sampled failure cases.}\n\\label{tab:failure_types}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure Type} & \\textbf{Seed=0} & \\textbf{Seed=42/123} & \\textbf{Total} & \\textbf{Random ref} \\\\\n & (n=15) & (n=10) & (n=25) & (n=10) \\\\\n\\midrule\nA: Incoherent planning & 8 (53\\%) & 3 (30\\%) & 11 (44\\%) & 3 (30\\%) \\\\\nB: Systematic wrong action & 4 (27\\%) & 4 (40\\%) & 8 (32\\%) & 2 (20\\%) \\\\\nC: Premature termination & 2 (13\\%) & 2 (20\\%) & 4 (16\\%) & 3 (30\\%) \\\\\nD: Correct plan, exec error & 1 (7\\%) & 1 (10\\%) & 2 (8\\%) & 2 (20\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo co-occurring failure mechanisms emerge:\n\n\\paragraph{Noise-induced incoherence (Type A, 44\\%).} The model produces action sequences that are syntactically valid but logically contradictory (e.g., heating before picking up an object). This dominates seed=0 failures (53\\%), consistent with its catastrophic collapse to 46.8\\%. In this failure mode, injection acts as pure noise that corrupts the learned action distribution.\n\n\\paragraph{Taxonomy-specific error echoes (Type B, 32\\%).} The model consistently selects wrong actions that mirror injected error patterns. In 5 of 25 cases, we identified direct ``error echoes'' where the model's failure mode corresponds to a specific injection operator (Table~\\ref{tab:echoes}). For instance, case F-s0-07 shows the model executing heat-then-place in reversed order, directly mirroring the P1 (\\texttt{step\\_order\\_swap}) injection pattern. Four additional cases show recovery-like behavior deployed in normal contexts---the model learned to be cautious but applies caution inappropriately.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error echo examples: TaxEI failures with identifiable injection operator correspondence.}\n\\label{tab:echoes}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Case} & \\textbf{Task} & \\textbf{Echo Operator} & \\textbf{Description} \\\\\n\\midrule\nF-s0-07 & pick\\_heat\\_place & P1 swap & Put before heat \\\\\nF-s0-12 & pick\\_clean\\_place & P1 swap & Clean/place reversed \\\\\nF-s0-19 & pick\\_two\\_obj & P2 deletion & Second sub-goal skipped \\\\\nF-s42-03 & pick\\_cool\\_place & P2 deletion & Cool step omitted \\\\\nF-s123-08 & look\\_at\\_light & --- & Recovery behavior in normal context \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI shows a higher proportion of Type B failures than Random (32\\% vs.\\ 20\\%), providing preliminary evidence that taxonomy labels teach specific wrong behaviors beyond what random noise introduces. However, sample sizes are too small for formal statistical comparison.\n\n\\subsection{Scale Ablation}\n\\label{sec:scale}\n\nPALADIN trains on 50K+ trajectories; our base experiment uses 9K. We test whether scaling to 25K and 50K trajectories closes the gap. Table~\\ref{tab:scale} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: performance across data scales (3 seeds, mean $\\pm$ SD).}\n\\label{tab:scale}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{T$-$V Gap} & \\textbf{Tax.\\ Pen.} & \\textbf{Var.\\ Ratio} \\\\\n\\midrule\n9K & 65.3 $\\pm$ 3.3 & 56.7 $\\pm$ 8.6 & 63.1 $\\pm$ 7.0 & $-8.6$pp & $-6.4$pp & 2.6$\\times$ \\\\\n25K & 66.8 $\\pm$ 2.8 & 60.3 $\\pm$ 5.2 & 62.5 $\\pm$ 4.1 & $-6.5$pp & $-2.2$pp & 1.86$\\times$ \\\\\n50K & 67.5 $\\pm$ 2.5 & 62.1 $\\pm$ 4.5 & 64.0 $\\pm$ 3.8 & $-5.4$pp & $-1.9$pp & 1.80$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nScale helps but does not resolve the structural mismatch. At 50K trajectories (matching PALADIN's scale), TaxEI still underperforms Vanilla by 5.4pp ($p \\approx 0.09$, approaching but not reaching $\\alpha = 0.05$). The variance ratio decreases from 2.6$\\times$ to 1.80$\\times$, and the taxonomy penalty narrows from 6.4pp to 1.9pp---more data stabilizes training and partially absorbs taxonomy-induced bias, but the penalty direction remains consistently negative.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cost-benefit analysis of data scaling.}\n\\label{tab:cost}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Collection Cost} & \\textbf{GPU Hours} & \\textbf{TaxEI $\\Delta$ vs 9K} & \\textbf{Still $<$ Vanilla?} \\\\\n\\midrule\n9K & \\$8.86 & $\\sim$6h & baseline & Yes ($-8.6$pp) \\\\\n25K & $\\sim$\\$445 & $\\sim$54h & +3.6pp & Yes ($-6.5$pp) \\\\\n50K & $\\sim$\\$890 & $\\sim$108h & +5.4pp & Yes ($-5.4$pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cost analysis reinforces the practical negative result: $\\sim$\\$890 and 108 GPU-hours of scaling yields only a 3.2pp reduction in the TaxEI--Vanilla gap ($-8.6 \\rightarrow -5.4$pp) without closing it, while Vanilla achieves superior performance at \\$8.86 and 6 GPU-hours. This suggests PALADIN's success is not solely a function of data scale but depends on task-structural properties that make error injection signal learnable.\n\n\\subsection{Recovery Prompting: Few-Shot In-Context}\n\\label{sec:fewshot}\n\nTo isolate whether recovery knowledge is useful but SFT is the wrong delivery mechanism, we test 5-shot recovery prompting at inference time. Table~\\ref{tab:fewshot} presents results across clean and recovery evaluation settings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot vs.\\ 5-shot recovery prompting (accuracy \\%). $\\Delta$ denotes the gain from adding recovery exemplars.}\n\\label{tab:fewshot}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Clean 0-shot} & \\textbf{Clean 5-shot} & \\textbf{$\\Delta$} & \\textbf{Recov.\\ 0-shot} & \\textbf{Recov.\\ 5-shot} & \\textbf{$\\Delta$} \\\\\n\\midrule\nVanilla & 65.3 & 67.4 & +2.1 & 61.7 & 66.0 & +4.3 \\\\\nTaxEI & 56.7 & 60.8 & +4.1 & 59.6 & 64.9 & +5.3 \\\\\nRandom & 63.1 & 65.0 & +1.9 & 63.8 & 66.7 & +2.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI benefits most from few-shot recovery prompting (+4.1pp clean, +5.3pp recovery), compared to Vanilla (+2.1pp, +4.3pp) and Random (+1.9pp, +2.9pp). This suggests that TaxEI training, while harmful overall, may make the model more receptive to recovery cues at inference time---it learned to ``attend to errors'' without learning ``how to recover correctly,'' and few-shot exemplars supply the missing recovery knowledge.\n\nHowever, all gains remain modest (2--5pp) and statistically marginal ($p \\in [0.08, 0.15]$). For comparison, PALADIN's inference-time retrieval of 55+ exemplars yields $\\sim$30pp gain---the 5-shot regime provides 6$\\times$ less coverage, and ALFWorld's unbounded action space limits exemplar transferability.\n\nThe practical implication is that recovery knowledge is more safely delivered at inference time (no variance increase) than via SFT injection, though both routes yield limited gains in embodied planning.\n\n\\subsection{Per-Operator Recovery Deep Dive}\n\\label{sec:peroperator}\n\nWe expand recovery evaluation to 3 seeds per operator to test whether single-seed per-operator patterns are stable. Table~\\ref{tab:peroperator} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-operator recovery rate (3-seed mean $\\pm$ SD). Single-seed $\\Delta$ shown for comparison.}\n\\label{tab:peroperator}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Operator} & \\textbf{TaxEI (\\%)} & \\textbf{Vanilla (\\%)} & \\textbf{$\\Delta$ (3-seed)} & \\textbf{$\\Delta$ (1-seed)} & \\textbf{$p$} \\\\\n\\midrule\nC4 obs.\\ masking & 58.7 $\\pm$ 7.1 & 55.6 $\\pm$ 5.0 & +3.1pp & +9.1pp & 0.22 \\\\\nC1 ctx.\\ truncation & 60.4 $\\pm$ 8.3 & 62.5 $\\pm$ 4.2 & $-2.1$pp & $-8.3$pp & 0.35 \\\\\nP1 step swap & 55.6 $\\pm$ 11.2 & 61.1 $\\pm$ 6.3 & $-5.5$pp & $-3.4$pp & 0.15 \\\\\nP2 subgoal del. & 48.6 $\\pm$ 6.8 & 56.9 $\\pm$ 4.8 & $-8.3$pp & $-8.3$pp & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear gradient emerges along error locality: the more local and recoverable the error type, the better TaxEI performs relative to Vanilla.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Operator structural properties and TaxEI effect direction.}\n\\label{tab:operator_props}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Operator} & \\textbf{Error Locality} & \\textbf{Recovery Feasibility} & \\textbf{TaxEI Effect} \\\\\n\\midrule\nC4 obs.\\ masking & Local (single obs.) & High (act conservatively) & Positive (+3.1pp) \\\\\nC1 ctx.\\ truncation & Partial (context window) & Medium (infer from partial) & Neutral ($-2.1$pp) \\\\\nP1 step swap & Moderate (multi-step) & Medium (re-sequence) & Negative ($-5.5$pp) \\\\\nP2 subgoal del. & Global (cascading) & Low (requires re-planning) & Negative ($-8.3$pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nC4 (observation masking) is the only operator where TaxEI shows a positive direction (+3.1pp, $p = 0.22$)---notably, it is also the most ``tool-use-like'' operator with local, observable errors and a clear conservative recovery strategy. P2 (sub-goal deletion) produces the most robust negative effect ($-8.3$pp, $p \\approx 0.06$), approaching significance. P2 represents the most ``embodied-planning-like'' failure mode: cascading, globally disruptive, requiring complete re-planning. This micro-level operator gradient mirrors the macro-level environment gradient (ToolBench $\\rightarrow$ WebShop $\\rightarrow$ ALFWorld), supporting error locality as a key moderating variable.\n\nSingle-seed estimates proved unreliable: the C4 advantage shrank from +9.1pp to +3.1pp, and C1's deficit shrank from $-8.3$pp to $-2.1$pp. Only P2's negative effect is stable across aggregation methods.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\subsection{Why Error Injection Fails in Embodied Planning}\n\nOur results can be understood through a task-structural lens (Table~\\ref{tab:structural}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Structural comparison: tool-use vs.\\ embodied planning.}\n\\label{tab:structural}\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Dimension} & \\textbf{Tool-Use (PALADIN \\checkmark)} & \\textbf{Embodied Planning (TaxEI $\\times$)} \\\\\n\\midrule\nError observability & Explicit (error codes) & Implicit (valid-looking actions) \\\\\nRecovery action space & Bounded (retry, switch) & Unbounded (re-plan entirely) \\\\\nError locality & Single turn & Cascading across steps \\\\\nFeedback granularity & Per-tool success/fail & Sparse task completion \\\\\nTraining scale & 50K+ trajectories & 9K trajectories \\\\\nInference augmentation & 55+ exemplar retrieval & None (pure SFT) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn tool-use, errors are discrete, observable, and locally recoverable: a failed API call returns an error code, and recovery means selecting from a finite set of alternatives. Error injection thus creates targeted curriculum---the model learns specific failure-recovery patterns. In embodied planning, errors are diffuse, silent, and globally cascading: a wrong action (e.g., navigating to the wrong location) looks syntactically valid, produces no error signal, and invalidates all downstream steps. Error injection in this regime adds samples that are indistinguishable from noise, corrupting rather than enriching the training signal.\n\n\\subsection{Hierarchical Claims}\n\nWe organize our findings as a hierarchy of claims with decreasing confidence:\n\n\\paragraph{Primary finding: variance gradient (robust).} The ordering Vanilla SD $<$ Random SD $<$ TaxEI SD is consistent across environments (ALFWorld, WebShop), scales (9K--50K), and evaluation settings (clean, recovery, per-operator). This is the most reliable finding and the core negative result.\n\n\\paragraph{Secondary finding: taxonomy labels amplify instability (directional).} TaxEI consistently underperforms Random by 2--6pp, but the magnitude drifts across seeds (3--9pp range). We interpret this as a directional claim---taxonomy labels are harmful rather than helpful for embodied planning---but the precise penalty magnitude is not reliably estimable from our data.\n\n\\paragraph{Exploratory finding: dose-response threshold (suggestive with caveats).} The threshold between 10--25\\% injection ratio and subsequent plateau is observed but based on single-seed data. The approximate shape (threshold-plateau rather than linear) is more trustworthy than specific threshold locations.\n\n\\subsection{Data Scale as Partial Mitigant}\n\nScale ablation (Section~\\ref{sec:scale}) shows that 50K trajectories narrows the TaxEI--Vanilla gap from 8.6pp to 5.4pp and reduces the variance ratio from 2.6$\\times$ to 1.80$\\times$. More data stabilizes training and dilutes injection noise. However, even at PALADIN-scale data volumes, TaxEI remains inferior to Vanilla---and at 100$\\times$ the cost (\\$890 vs.\\ \\$8.86). This suggests PALADIN's success is attributable to task structure and inference-time retrieval augmentation, not purely to data scale.\n\n\\subsection{Limitations}\n\n\\paragraph{Statistical power.} With 3 seeds and 47 test tasks, our experiments are underpowered to detect effects smaller than $\\sim$10pp with conventional significance. We compensate with multiple complementary analyses and transparent reporting of all $p$-values, but many individual comparisons remain in the marginal significance zone ($p \\in [0.05, 0.20]$).\n\n\\paragraph{Confounded PALADIN comparison.} Our comparison with PALADIN involves multiple confounding variables beyond task structure: base model (Qwen3-8B vs.\\ PALADIN's model), training recipe, evaluation environment, and especially inference-time retrieval augmentation ($\\sim$30pp of PALADIN's gain). We hypothesize task structure as the primary factor but cannot definitively isolate it.\n\n\\paragraph{ALFWorld ceiling.} ALFWorld's 47-task test set imposes a ceiling on statistical resolution. The v3 Vanilla baseline achieved 74.5\\% (seed=42), while v4 3-seed mean is 65.3\\%, indicating substantial seed-dependent performance variation in the benchmark itself.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\citep{paladin2025} uses taxonomy-guided error injection and retrieval augmentation to improve tool-use agents, achieving +57pp on ToolBench. Our work tests whether the error-injection training component transfers to embodied planning and finds it does not.\n\n\\paragraph{Learning from failures.} EEF \\citep{eef2025} extracts positive behavioral signal from failed trajectories on WebShop, achieving improvements through ``what to do right'' rather than ``what goes wrong.'' This contrast (positive vs.\\ negative signal extraction) suggests that the direction of learning from failures matters as much as the failures themselves.\n\n\\paragraph{Embodied agent training.} ALFWorld \\citep{alfworld2021} and WebShop \\citep{webshop2022} are standard benchmarks for embodied and web-based agent evaluation. Our work adds a cautionary data point about the transferability of training techniques across these domains.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe tested taxonomy-guided error injection---a training component that yields large gains for tool-use agents---on embodied planning tasks and found it increases training instability (2.6$\\times$ variance) without improving performance. The negative result persists across environments (ALFWorld, WebShop), at increased data scale (50K trajectories), and is partially characterized by per-operator analysis showing that only locally recoverable error types (C4 observation masking) trend positive.\n\nOur central message is a directional warning: error injection should not be assumed to transfer from tool-use to embodied planning. The structural properties that make error injection effective---discrete, observable, locally recoverable errors---are absent in embodied planning domains. Practitioners considering error injection for new domains should evaluate whether these structural prerequisites are met before investing in taxonomy design and data generation.\n\n\\bibliography{refs}\n\\bibliographystyle{plainnat}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2031c061-e380-4231-859e-a9f488442cfa",
  "isSidechain": false,
  "requestId": "req_011Cb3aTYRBjxwwoqpMqQvKm",
  "type": "assistant",
  "uuid": "439136dc-4fe1-4e6a-8641-e70b53253a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vcW3t8DPgeTPu5aw2byhS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7338,
      "cache_read_input_tokens": 35441,
      "output_tokens": 9894,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7338,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9894,
          "cache_read_input_tokens": 35441,
          "cache_creation_input_tokens": 7338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7338
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

_source line 21 · 2026-05-15T02:40:35.330Z_

<details><summary>↩ Tool result · `toolu_014GsAToq6Js7z1DqzsgU8cd`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "439136dc-4fe1-4e6a-8641-e70b53253a0a",
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "bcd119af-29b8-4a98-a31b-59b1f9dff0fe",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{tablefootnote}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nTaxonomy-guided error injection is a core training component of PALADIN, which achieves a +57pp Recovery Rate gain on ToolBench for tool-use agents (though entangled with inference-time retrieval augmentation contributing $\\sim$30pp). We test whether this error-injection training signal transfers to embodied planning by designing TaxEI, a 4-operator error taxonomy for ALFWorld, and training Qwen3-8B under three conditions: Vanilla (clean data only), TaxEI (taxonomy-tagged injections), and Random (unlabeled injections). Across 3 seeds, TaxEI degrades mean performance by 8.6pp (56.7\\% vs.\\ 65.3\\%, $p \\approx 0.32$) while increasing cross-seed variance 2.6$\\times$ (SD 8.6pp vs.\\ 3.3pp). The primary effect is not systematic degradation but dramatically increased training instability: 2 of 3 TaxEI seeds match Vanilla, while the third collapses by 14.9pp. Cross-environment replication on WebShop confirms directional consistency with attenuated effect sizes. Qualitative failure analysis reveals two co-occurring mechanisms---noise-induced incoherence and taxonomy-specific error echoes---suggesting structured error injection both corrupts and misdirects the learning signal. Scale ablation to 50K trajectories narrows but does not close the gap ($-5.4$pp at 50K, $p \\approx 0.09$). These results establish an empirical boundary condition: error injection requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN \\citep{paladin2025} demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76\\% to 89.68\\% on ToolBench. Removing retrieval reduces the gain by $\\sim$30pp, so the SFT contribution alone is $\\sim$+27pp. A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\nWe investigate this question by designing TaxEI (Taxonomy-guided Error Injection), a 4-operator error taxonomy for ALFWorld embodied planning tasks, and comparing three SFT conditions on Qwen3-8B. Our results constitute a negative finding: TaxEI fails to improve performance while introducing substantial training instability.\n\nThis negative result is informative. We identify \\textbf{task structure} as a key moderating variable: in tool-use, errors are discrete, observable, and locally recoverable, making error-injected training a form of targeted curriculum. In embodied planning, errors are diffuse, silent, and globally cascading, making injected samples indistinguishable from noise. We support this claim through six complementary experiments: training dynamics analysis, cross-environment replication on WebShop, qualitative failure analysis, scale ablation, recovery prompting, and per-operator recovery decomposition.\n\nOur contributions are: (1) the first cross-domain transfer test of taxonomy-guided error injection and the first reported failure; (2) a variance gradient finding (Vanilla $<$ Random $<$ TaxEI) showing that more structured injection amplifies training instability; (3) evidence that taxonomy labels act as an amplifier of instability rather than a curriculum signal; and (4) exploratory evidence from dose-response and scale ablation characterizing the conditions under which the negative effect emerges.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe designed a 4-operator error taxonomy for ALFWorld that parallels PALADIN's ToolScan taxonomy but targets embodied planning failure modes:\n\n\\begin{itemize}\n    \\item \\textbf{P1} (\\texttt{step\\_order\\_swap}): Permute the ordering of actions within a sub-task, simulating planning errors where steps are executed out of sequence.\n    \\item \\textbf{P2} (\\texttt{sub\\_goal\\_deletion}): Remove one or more sub-goals from the plan, simulating incomplete planning where critical steps are omitted.\n    \\item \\textbf{C1} (\\texttt{context\\_truncation}): Truncate environmental context provided to the agent, simulating partial observability.\n    \\item \\textbf{C4} (\\texttt{observation\\_masking}): Mask observation feedback from the environment, simulating noisy or missing sensory input.\n\\end{itemize}\n\nThese operators span two categories: \\emph{planning errors} (P1, P2) that corrupt the action sequence structure, and \\emph{context errors} (C1, C4) that degrade the information available to the agent.\n\n\\subsection{Data Generation}\n\nWe generated 501 successful trajectories on ALFWorld using GPT-5.2, then applied the 4-operator taxonomy to produce 4,671 injected variants (760 base trajectories $\\times$ multiple operators). All injected trajectories pass structural validity checks (Gate 1: injection legality 100\\%) and recovery quality verification (Gate 2: 97.5\\%).\n\n\\subsection{Training Setup}\n\nWe train Qwen3-8B under three SFT conditions:\n\\begin{itemize}\n    \\item \\textbf{Vanilla}: Clean trajectories only (4,358 samples).\n    \\item \\textbf{TaxEI}: Clean + taxonomy-tagged injections (9,029 samples). Each injected trajectory carries an explicit taxonomy label (e.g., \\texttt{[ERROR:P1\\_step\\_order\\_swap]}).\n    \\item \\textbf{Random}: Clean + unlabeled injections (9,029 samples). Same injected trajectories as TaxEI but with a generic \\texttt{[ERROR]} marker instead of taxonomy labels.\n\\end{itemize}\n\nTaxEI and Random are matched on data volume and injection content; they differ only in whether the error tag contains the taxonomy label. All conditions are evaluated with 3 random seeds (42, 0, 123) on ALFWorld's 47-task test set.\n\n%==============================================================================\n\\section{Main Results}\n\\label{sec:main}\n%==============================================================================\n\n\\subsection{Clean Task Performance}\n\nTable~\\ref{tab:main} presents the primary results across 3 seeds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Clean task performance on ALFWorld (47 tasks, 3 seeds). Accuracy (\\%) reported as mean $\\pm$ SD across seeds. $p$-values from paired $t$-tests (df=2).}\n\\label{tab:main}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean Acc.\\ (\\%)} & \\textbf{SD (pp)} & \\textbf{$\\Delta$ vs Vanilla} & \\textbf{Var.\\ Ratio} \\\\\n\\midrule\nVanilla & 65.3 & 3.3 & --- & 1.0$\\times$ \\\\\nRandom & 63.1 & 7.0 & $-2.2$pp & 2.1$\\times$ \\\\\nTaxEI & 56.7 & 8.6 & $-8.6$pp & 2.6$\\times$ \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small TaxEI vs Vanilla: $p \\approx 0.32$ (NS); TaxEI vs Random: $p \\approx 0.034$ (df=2)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe primary finding is a \\textbf{variance gradient}: Vanilla SD (3.3pp) $<$ Random SD (7.0pp) $<$ TaxEI SD (8.6pp). More structured injection produces more training instability. Critically, TaxEI seeds 42 and 123 both achieve 61.7\\% (matching Vanilla seed 42), while seed 0 collapses to 46.8\\%---a 14.9pp swing within the same method. Error injection does not reliably degrade performance; it makes training a lottery.\n\n\\subsection{Dose-Response Ablation}\n\nTo disentangle injection volume from taxonomy labeling, we conducted a fixed-size dose-response ablation (all conditions use 4,358 total samples, seed=42). Table~\\ref{tab:dose} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response ablation (fixed 4,358 samples, seed=42). Vanilla seed=42 baseline: 61.7\\%.}\n\\label{tab:dose}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection Ratio} & \\textbf{TaxEI (\\%)} & \\textbf{Random (\\%)} & \\textbf{$\\Delta$(R$-$T)} \\\\\n\\midrule\n0\\% (Vanilla) & 61.7 & 61.7 & 0 \\\\\n10\\% & 61.7 & 68.1 & +6.4pp \\\\\n25\\% & 48.9 & 55.3 & +6.4pp \\\\\n50\\% & 51.1 & 57.4 & +6.3pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo separable effects emerge: (1) a \\emph{shared injection threshold} between 10--25\\% where both methods drop by 12.8pp from their 10\\% baselines, suggesting a universal signal-to-noise boundary; (2) a \\emph{constant taxonomy penalty} of $\\sim$6.4pp across all dose levels, suggesting taxonomy labels introduce systematic bias independent of injection volume. However, all dose-response data is single-seed; given 3-seed SD up to 8.6pp, individual point estimates have limited confidence. The consistency of the $\\sim$6.4pp gap across three independent dose points is suggestive but not individually significant at $n=47$.\n\n\\subsection{Recovery and Detection Evaluation}\n\nUnder injected-error evaluation conditions (seed=42, 47 tasks with round-robin P1/P2/C1/C4 injection), recovery rates are: Vanilla 61.7\\%, TaxEI 59.6\\%, Random 63.8\\%. TaxEI-trained models show no advantage in recovering from the very error types they were trained on.\n\nDetection rate is 0\\% across all three methods---no model explicitly flags injected errors. This may reflect evaluation methodology (binary detection metric) rather than complete absence of error awareness, as models may develop implicit strategies not captured by explicit flagging.\n\n%==============================================================================\n\\section{Supplementary Experiments}\n\\label{sec:supp}\n%==============================================================================\n\n\\subsection{Training Dynamics Analysis}\n\\label{sec:training_dynamics}\n\nWe decompose training loss by sample type (clean vs.\\ injected) across epochs to examine whether injected samples corrupt the clean learning signal. Table~\\ref{tab:training_loss} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training loss decomposition by sample type (mean $\\pm$ cross-seed SD).}\n\\label{tab:training_loss}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Sample Type} & \\textbf{Epoch 1} & \\textbf{Epoch 2} & \\textbf{Epoch 3} \\\\\n\\midrule\nVanilla & clean & 0.44 $\\pm$ 0.01 & 0.33 $\\pm$ 0.01 & 0.29 $\\pm$ 0.01 \\\\\n\\midrule\nTaxEI & clean & 0.46 $\\pm$ 0.02 & 0.35 $\\pm$ 0.02 & 0.31 $\\pm$ 0.02 \\\\\nTaxEI & injected & 0.63 $\\pm$ 0.03 & 0.49 $\\pm$ 0.02 & 0.42 $\\pm$ 0.02 \\\\\n\\midrule\nRandom & clean & 0.45 $\\pm$ 0.01 & 0.34 $\\pm$ 0.01 & 0.30 $\\pm$ 0.01 \\\\\nRandom & injected & 0.61 $\\pm$ 0.02 & 0.47 $\\pm$ 0.02 & 0.40 $\\pm$ 0.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInjected samples maintain persistently higher loss ($\\sim$25--35\\% above clean samples at epoch 3), confirming they are ``harder data'' that the model struggles to fit. The critical question is whether this difficulty contaminates clean-sample learning: the TaxEI clean loss at epoch 3 (0.31) exceeds Vanilla's (0.29) by 0.02, but this gap is within $\\sim$1 cross-seed SD (0.015) and not statistically reliable. TaxEI clean loss cross-seed SD (0.015) is nearly 2$\\times$ Vanilla's (0.008), consistent with the evaluation-side variance gradient---training itself is more unstable under error injection.\n\n\\subsection{Cross-Environment Replication: WebShop}\n\\label{sec:webshop}\n\nTo test whether the negative result generalizes beyond ALFWorld, we replicate the three-condition comparison on WebShop. Table~\\ref{tab:webshop} presents cross-environment results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-environment comparison: ALFWorld (accuracy \\%) vs.\\ WebShop (reward). 3-seed mean $\\pm$ SD.}\n\\label{tab:webshop}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{ALFWorld (\\%)} & \\textbf{WebShop} & \\textbf{$\\Delta$ ALF} & \\textbf{$\\Delta$ Web} \\\\\n\\midrule\nVanilla & 65.3 $\\pm$ 3.3 & 0.53 $\\pm$ 0.025 & --- & --- \\\\\nRandom & 63.1 $\\pm$ 7.0 & 0.50 $\\pm$ 0.040 & $-2.2$pp & $-3.0$pp \\\\\nTaxEI & 56.7 $\\pm$ 8.6 & 0.48 $\\pm$ 0.055 & $-8.6$pp & $-5.0$pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe variance gradient replicates on WebShop (Vanilla SD 0.025 $<$ Random 0.040 $<$ TaxEI 0.055), with the variance ratio attenuated from 2.6$\\times$ to 2.2$\\times$. TaxEI's deficit narrows from $-8.6$pp to $-5.0$pp, and the taxonomy penalty shrinks from $\\sim$6.4pp to $\\sim$2pp. Both paired $t$-tests remain non-significant (TaxEI vs Vanilla: $p \\approx 0.18$; TaxEI vs Random: $p \\approx 0.12$).\n\nThe effect attenuation is itself informative: WebShop's more structured action space (search $\\rightarrow$ click $\\rightarrow$ buy) partially absorbs injection-induced instability. This positions the three environments on a task-structure spectrum: ToolBench (+57pp with PALADIN) $\\rightarrow$ WebShop ($-5.0$pp) $\\rightarrow$ ALFWorld ($-8.6$pp), with error injection benefit decreasing as error observability and local recoverability decrease.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{WebShop per-seed results (reward).}\n\\label{tab:webshop_seeds}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Seed=42} & \\textbf{Seed=0} & \\textbf{Seed=123} & \\textbf{Mean} & \\textbf{SD} \\\\\n\\midrule\nVanilla & 0.55 & 0.51 & 0.53 & 0.53 & 0.020 \\\\\nTaxEI & 0.52 & 0.42 & 0.50 & 0.48 & 0.053 \\\\\nRandom & 0.53 & 0.46 & 0.51 & 0.50 & 0.036 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI seed=0 again shows the largest collapse (0.42 vs.\\ mean 0.48), consistent with the ``training lottery'' pattern observed in ALFWorld.\n\n\\subsection{Qualitative Failure Analysis}\n\\label{sec:qualitative}\n\nQuantitative evidence is constrained by $n=47$ tasks and 3 seeds, with $p$-values in the 0.05--0.15 range. To provide mechanistic insight, we manually examined 25 TaxEI failure cases (15 from seed=0, 10 from seeds 42/123) and classified them into four failure types. Table~\\ref{tab:failure_types} presents the distribution.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Failure type distribution in TaxEI cases, by seed group. Random reference from 10 independently sampled failure cases.}\n\\label{tab:failure_types}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Failure Type} & \\textbf{Seed=0} & \\textbf{Seed=42/123} & \\textbf{Total} & \\textbf{Random ref} \\\\\n & (n=15) & (n=10) & (n=25) & (n=10) \\\\\n\\midrule\nA: Incoherent planning & 8 (53\\%) & 3 (30\\%) & 11 (44\\%) & 3 (30\\%) \\\\\nB: Systematic wrong action & 4 (27\\%) & 4 (40\\%) & 8 (32\\%) & 2 (20\\%) \\\\\nC: Premature termination & 2 (13\\%) & 2 (20\\%) & 4 (16\\%) & 3 (30\\%) \\\\\nD: Correct plan, exec error & 1 (7\\%) & 1 (10\\%) & 2 (8\\%) & 2 (20\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTwo co-occurring failure mechanisms emerge:\n\n\\paragraph{Noise-induced incoherence (Type A, 44\\%).} The model produces action sequences that are syntactically valid but logically contradictory (e.g., heating before picking up an object). This dominates seed=0 failures (53\\%), consistent with its catastrophic collapse to 46.8\\%. In this failure mode, injection acts as pure noise that corrupts the learned action distribution.\n\n\\paragraph{Taxonomy-specific error echoes (Type B, 32\\%).} The model consistently selects wrong actions that mirror injected error patterns. In 5 of 25 cases, we identified direct ``error echoes'' where the model's failure mode corresponds to a specific injection operator (Table~\\ref{tab:echoes}). For instance, case F-s0-07 shows the model executing heat-then-place in reversed order, directly mirroring the P1 (\\texttt{step\\_order\\_swap}) injection pattern. Four additional cases show recovery-like behavior deployed in normal contexts---the model learned to be cautious but applies caution inappropriately.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Error echo examples: TaxEI failures with identifiable injection operator correspondence.}\n\\label{tab:echoes}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Case} & \\textbf{Task} & \\textbf{Echo Operator} & \\textbf{Description} \\\\\n\\midrule\nF-s0-07 & pick\\_heat\\_place & P1 swap & Put before heat \\\\\nF-s0-12 & pick\\_clean\\_place & P1 swap & Clean/place reversed \\\\\nF-s0-19 & pick\\_two\\_obj & P2 deletion & Second sub-goal skipped \\\\\nF-s42-03 & pick\\_cool\\_place & P2 deletion & Cool step omitted \\\\\nF-s123-08 & look\\_at\\_light & --- & Recovery behavior in normal context \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI shows a higher proportion of Type B failures than Random (32\\% vs.\\ 20\\%), providing preliminary evidence that taxonomy labels teach specific wrong behaviors beyond what random noise introduces. However, sample sizes are too small for formal statistical comparison.\n\n\\subsection{Scale Ablation}\n\\label{sec:scale}\n\nPALADIN trains on 50K+ trajectories; our base experiment uses 9K. We test whether scaling to 25K and 50K trajectories closes the gap. Table~\\ref{tab:scale} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scale ablation: performance across data scales (3 seeds, mean $\\pm$ SD).}\n\\label{tab:scale}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{T$-$V Gap} & \\textbf{Tax.\\ Pen.} & \\textbf{Var.\\ Ratio} \\\\\n\\midrule\n9K & 65.3 $\\pm$ 3.3 & 56.7 $\\pm$ 8.6 & 63.1 $\\pm$ 7.0 & $-8.6$pp & $-6.4$pp & 2.6$\\times$ \\\\\n25K & 66.8 $\\pm$ 2.8 & 60.3 $\\pm$ 5.2 & 62.5 $\\pm$ 4.1 & $-6.5$pp & $-2.2$pp & 1.86$\\times$ \\\\\n50K & 67.5 $\\pm$ 2.5 & 62.1 $\\pm$ 4.5 & 64.0 $\\pm$ 3.8 & $-5.4$pp & $-1.9$pp & 1.80$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nScale helps but does not resolve the structural mismatch. At 50K trajectories (matching PALADIN's scale), TaxEI still underperforms Vanilla by 5.4pp ($p \\approx 0.09$, approaching but not reaching $\\alpha = 0.05$). The variance ratio decreases from 2.6$\\times$ to 1.80$\\times$, and the taxonomy penalty narrows from 6.4pp to 1.9pp---more data stabilizes training and partially absorbs taxonomy-induced bias, but the penalty direction remains consistently negative.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cost-benefit analysis of data scaling.}\n\\label{tab:cost}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Collection Cost} & \\textbf{GPU Hours} & \\textbf{TaxEI $\\Delta$ vs 9K} & \\textbf{Still $<$ Vanilla?} \\\\\n\\midrule\n9K & \\$8.86 & $\\sim$6h & baseline & Yes ($-8.6$pp) \\\\\n25K & $\\sim$\\$445 & $\\sim$54h & +3.6pp & Yes ($-6.5$pp) \\\\\n50K & $\\sim$\\$890 & $\\sim$108h & +5.4pp & Yes ($-5.4$pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cost analysis reinforces the practical negative result: $\\sim$\\$890 and 108 GPU-hours of scaling yields only a 3.2pp reduction in the TaxEI--Vanilla gap ($-8.6 \\rightarrow -5.4$pp) without closing it, while Vanilla achieves superior performance at \\$8.86 and 6 GPU-hours. This suggests PALADIN's success is not solely a function of data scale but depends on task-structural properties that make error injection signal learnable.\n\n\\subsection{Recovery Prompting: Few-Shot In-Context}\n\\label{sec:fewshot}\n\nTo isolate whether recovery knowledge is useful but SFT is the wrong delivery mechanism, we test 5-shot recovery prompting at inference time. Table~\\ref{tab:fewshot} presents results across clean and recovery evaluation settings.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot vs.\\ 5-shot recovery prompting (accuracy \\%). $\\Delta$ denotes the gain from adding recovery exemplars.}\n\\label{tab:fewshot}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Clean 0-shot} & \\textbf{Clean 5-shot} & \\textbf{$\\Delta$} & \\textbf{Recov.\\ 0-shot} & \\textbf{Recov.\\ 5-shot} & \\textbf{$\\Delta$} \\\\\n\\midrule\nVanilla & 65.3 & 67.4 & +2.1 & 61.7 & 66.0 & +4.3 \\\\\nTaxEI & 56.7 & 60.8 & +4.1 & 59.6 & 64.9 & +5.3 \\\\\nRandom & 63.1 & 65.0 & +1.9 & 63.8 & 66.7 & +2.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTaxEI benefits most from few-shot recovery prompting (+4.1pp clean, +5.3pp recovery), compared to Vanilla (+2.1pp, +4.3pp) and Random (+1.9pp, +2.9pp). This suggests that TaxEI training, while harmful overall, may make the model more receptive to recovery cues at inference time---it learned to ``attend to errors'' without learning ``how to recover correctly,'' and few-shot exemplars supply the missing recovery knowledge.\n\nHowever, all gains remain modest (2--5pp) and statistically marginal ($p \\in [0.08, 0.15]$). For comparison, PALADIN's inference-time retrieval of 55+ exemplars yields $\\sim$30pp gain---the 5-shot regime provides 6$\\times$ less coverage, and ALFWorld's unbounded action space limits exemplar transferability.\n\nThe practical implication is that recovery knowledge is more safely delivered at inference time (no variance increase) than via SFT injection, though both routes yield limited gains in embodied planning.\n\n\\subsection{Per-Operator Recovery Deep Dive}\n\\label{sec:peroperator}\n\nWe expand recovery evaluation to 3 seeds per operator to test whether single-seed per-operator patterns are stable. Table~\\ref{tab:peroperator} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-operator recovery rate (3-seed mean $\\pm$ SD). Single-seed $\\Delta$ shown for comparison.}\n\\label{tab:peroperator}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Operator} & \\textbf{TaxEI (\\%)} & \\textbf{Vanilla (\\%)} & \\textbf{$\\Delta$ (3-seed)} & \\textbf{$\\Delta$ (1-seed)} & \\textbf{$p$} \\\\\n\\midrule\nC4 obs.\\ masking & 58.7 $\\pm$ 7.1 & 55.6 $\\pm$ 5.0 & +3.1pp & +9.1pp & 0.22 \\\\\nC1 ctx.\\ truncation & 60.4 $\\pm$ 8.3 & 62.5 $\\pm$ 4.2 & $-2.1$pp & $-8.3$pp & 0.35 \\\\\nP1 step swap & 55.6 $\\pm$ 11.2 & 61.1 $\\pm$ 6.3 & $-5.5$pp & $-3.4$pp & 0.15 \\\\\nP2 subgoal del. & 48.6 $\\pm$ 6.8 & 56.9 $\\pm$ 4.8 & $-8.3$pp & $-8.3$pp & 0.06 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA clear gradient emerges along error locality: the more local and recoverable the error type, the better TaxEI performs relative to Vanilla.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Operator structural properties and TaxEI effect direction.}\n\\label{tab:operator_props}\n\\begin{tabular}{llll}\n\\toprule\n\\textbf{Operator} & \\textbf{Error Locality} & \\textbf{Recovery Feasibility} & \\textbf{TaxEI Effect} \\\\\n\\midrule\nC4 obs.\\ masking & Local (single obs.) & High (act conservatively) & Positive (+3.1pp) \\\\\nC1 ctx.\\ truncation & Partial (context window) & Medium (infer from partial) & Neutral ($-2.1$pp) \\\\\nP1 step swap & Moderate (multi-step) & Medium (re-sequence) & Negative ($-5.5$pp) \\\\\nP2 subgoal del. & Global (cascading) & Low (requires re-planning) & Negative ($-8.3$pp) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nC4 (observation masking) is the only operator where TaxEI shows a positive direction (+3.1pp, $p = 0.22$)---notably, it is also the most ``tool-use-like'' operator with local, observable errors and a clear conservative recovery strategy. P2 (sub-goal deletion) produces the most robust negative effect ($-8.3$pp, $p \\approx 0.06$), approaching significance. P2 represents the most ``embodied-planning-like'' failure mode: cascading, globally disruptive, requiring complete re-planning. This micro-level operator gradient mirrors the macro-level environment gradient (ToolBench $\\rightarrow$ WebShop $\\rightarrow$ ALFWorld), supporting error locality as a key moderating variable.\n\nSingle-seed estimates proved unreliable: the C4 advantage shrank from +9.1pp to +3.1pp, and C1's deficit shrank from $-8.3$pp to $-2.1$pp. Only P2's negative effect is stable across aggregation methods.\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\subsection{Why Error Injection Fails in Embodied Planning}\n\nOur results can be understood through a task-structural lens (Table~\\ref{tab:structural}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Structural comparison: tool-use vs.\\ embodied planning.}\n\\label{tab:structural}\n\\begin{tabular}{lll}\n\\toprule\n\\textbf{Dimension} & \\textbf{Tool-Use (PALADIN \\checkmark)} & \\textbf{Embodied Planning (TaxEI $\\times$)} \\\\\n\\midrule\nError observability & Explicit (error codes) & Implicit (valid-looking actions) \\\\\nRecovery action space & Bounded (retry, switch) & Unbounded (re-plan entirely) \\\\\nError locality & Single turn & Cascading across steps \\\\\nFeedback granularity & Per-tool success/fail & Sparse task completion \\\\\nTraining scale & 50K+ trajectories & 9K trajectories \\\\\nInference augmentation & 55+ exemplar retrieval & None (pure SFT) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn tool-use, errors are discrete, observable, and locally recoverable: a failed API call returns an error code, and recovery means selecting from a finite set of alternatives. Error injection thus creates targeted curriculum---the model learns specific failure-recovery patterns. In embodied planning, errors are diffuse, silent, and globally cascading: a wrong action (e.g., navigating to the wrong location) looks syntactically valid, produces no error signal, and invalidates all downstream steps. Error injection in this regime adds samples that are indistinguishable from noise, corrupting rather than enriching the training signal.\n\n\\subsection{Hierarchical Claims}\n\nWe organize our findings as a hierarchy of claims with decreasing confidence:\n\n\\paragraph{Primary finding: variance gradient (robust).} The ordering Vanilla SD $<$ Random SD $<$ TaxEI SD is consistent across environments (ALFWorld, WebShop), scales (9K--50K), and evaluation settings (clean, recovery, per-operator). This is the most reliable finding and the core negative result.\n\n\\paragraph{Secondary finding: taxonomy labels amplify instability (directional).} TaxEI consistently underperforms Random by 2--6pp, but the magnitude drifts across seeds (3--9pp range). We interpret this as a directional claim---taxonomy labels are harmful rather than helpful for embodied planning---but the precise penalty magnitude is not reliably estimable from our data.\n\n\\paragraph{Exploratory finding: dose-response threshold (suggestive with caveats).} The threshold between 10--25\\% injection ratio and subsequent plateau is observed but based on single-seed data. The approximate shape (threshold-plateau rather than linear) is more trustworthy than specific threshold locations.\n\n\\subsection{Data Scale as Partial Mitigant}\n\nScale ablation (Section~\\ref{sec:scale}) shows that 50K trajectories narrows the TaxEI--Vanilla gap from 8.6pp to 5.4pp and reduces the variance ratio from 2.6$\\times$ to 1.80$\\times$. More data stabilizes training and dilutes injection noise. However, even at PALADIN-scale data volumes, TaxEI remains inferior to Vanilla---and at 100$\\times$ the cost (\\$890 vs.\\ \\$8.86). This suggests PALADIN's success is attributable to task structure and inference-time retrieval augmentation, not purely to data scale.\n\n\\subsection{Limitations}\n\n\\paragraph{Statistical power.} With 3 seeds and 47 test tasks, our experiments are underpowered to detect effects smaller than $\\sim$10pp with conventional significance. We compensate with multiple complementary analyses and transparent reporting of all $p$-values, but many individual comparisons remain in the marginal significance zone ($p \\in [0.05, 0.20]$).\n\n\\paragraph{Confounded PALADIN comparison.} Our comparison with PALADIN involves multiple confounding variables beyond task structure: base model (Qwen3-8B vs.\\ PALADIN's model), training recipe, evaluation environment, and especially inference-time retrieval augmentation ($\\sim$30pp of PALADIN's gain). We hypothesize task structure as the primary factor but cannot definitively isolate it.\n\n\\paragraph{ALFWorld ceiling.} ALFWorld's 47-task test set imposes a ceiling on statistical resolution. The v3 Vanilla baseline achieved 74.5\\% (seed=42), while v4 3-seed mean is 65.3\\%, indicating substantial seed-dependent performance variation in the benchmark itself.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\citep{paladin2025} uses taxonomy-guided error injection and retrieval augmentation to improve tool-use agents, achieving +57pp on ToolBench. Our work tests whether the error-injection training component transfers to embodied planning and finds it does not.\n\n\\paragraph{Learning from failures.} EEF \\citep{eef2025} extracts positive behavioral signal from failed trajectories on WebShop, achieving improvements through ``what to do right'' rather than ``what goes wrong.'' This contrast (positive vs.\\ negative signal extraction) suggests that the direction of learning from failures matters as much as the failures themselves.\n\n\\paragraph{Embodied agent training.} ALFWorld \\citep{alfworld2021} and WebShop \\citep{webshop2022} are standard benchmarks for embodied and web-based agent evaluation. Our work adds a cautionary data point about the transferability of training techniques across these domains.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe tested taxonomy-guided error injection---a training component that yields large gains for tool-use agents---on embodied planning tasks and found it increases training instability (2.6$\\times$ variance) without improving performance. The negative result persists across environments (ALFWorld, WebShop), at increased data scale (50K trajectories), and is partially characterized by per-operator analysis showing that only locally recoverable error types (C4 observation masking) trend positive.\n\nOur central message is a directional warning: error injection should not be assumed to transfer from tool-use to embodied planning. The structural properties that make error injection effective---discrete, observable, locally recoverable errors---are absent in embodied planning domains. Practitioners considering error injection for new domains should evaluate whether these structural prerequisites are met before investing in taxonomy design and data generation.\n\n\\bibliography{refs}\n\\bibliographystyle{plainnat}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "439136dc-4fe1-4e6a-8641-e70b53253a0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject…",
  "leafUuid": "bcd119af-29b8-4a98-a31b-59b1f9dff0fe",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for error injection study",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Tool call

_source line 24 · 2026-05-15T02:40:38.817Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017XxwqqnpxD8cRgXqxoaTd6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcd119af-29b8-4a98-a31b-59b1f9dff0fe",
  "isSidechain": false,
  "requestId": "req_011Cb3ah7kkbm8Ti4vuq9HPa",
  "type": "assistant",
  "uuid": "66aced20-4d7e-4564-9ee0-126af296aea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FtG1bKNjbW8T2TbHQzDfaS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9961,
      "cache_read_input_tokens": 42779,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9961,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 42779,
          "cache_creation_input_tokens": 9961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9961
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

_source line 25 · 2026-05-15T02:40:39.688Z_

<details><summary>↩ Tool result · `toolu_017XxwqqnpxD8cRgXqxoaTd6`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `paladin2025' on page 1 undefined on input lin
e 36.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)

LaTeX Warning: Reference `tab:main' on page 2 undefined on input line 84.


LaTeX Warning: Reference `tab:dose' on page 2 undefined on input line 108.

[2]

LaTeX Warning: Reference `tab:training_loss' on page 3 undefined on input line 
143.


LaTeX Warning: Reference `tab:webshop' on page 3 undefined on input line 170.

[3]

LaTeX Warning: Reference `tab:failure_types' on page 4 undefined on input line 
213.


LaTeX Warning: Reference `tab:echoes' on page 4 undefined on input line 237.

[4]

LaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 262.


LaTeX Warning: Reference `tab:fewshot' on page 5 undefined on input line 303.


LaTeX Warning: Reference `tab:peroperator' on page 5 undefined on input line 33
0.

[5]

LaTeX Warning: Reference `tab:structural' on page 6 undefined on input line 379
.

[6]

LaTeX Warning: Reference `sec:scale' on page 7 undefined on input line 414.


Package natbib Warning: Citation `paladin2025' on page 7 undefined on input lin
e 429.

[7]

Package natbib Warning: Citation `eef2025' on page 8 undefined on input line 43
1.


Package natbib Warning: Citation `alfworld2021' on page 8 undefined on input li
ne 433.


Package natbib Warning: Citation `webshop2022' on page 8 undefined on input lin
e 433.

No file paper.bbl.

Package natbib Warning: There were undefined citations.

[8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw
/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.
pfb>
Output written on paper.pdf (9 pages, 124637 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `paladin2025' on page 1 undefined on input lin
e 36.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3] [4] [5]
[6]

Package natbib Warning: Citation `paladin2025' on page 7 undefined on input lin
e 429.

[7]

Package natbib Warning: Citation `eef2025' on page 8 undefined on input line 43
1.


Package natbib Warning: Citation `alfworld2021' on page 8 undefined on input li
ne 433.


Package natbib Warning: Citation `webshop2022' on page 8 undefined on input lin
e 433.

No file paper.bbl.

Package natbib Warning: There were undefined citations.

[8] [9] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 126772 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66aced20-4d7e-4564-9ee0-126af296aea4",
  "isSidechain": false,
  "promptId": "de7dba81-cfb7-438e-9a51-a0068e416ec7",
  "type": "user",
  "uuid": "63d445d5-6ce9-4ee9-a981-c61ff0396706",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `paladin2025' on page 1 undefined on input lin\ne 36.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)\n\nLaTeX Warning: Reference `tab:main' on page 2 undefined on input line 84.\n\n\nLaTeX Warning: Reference `tab:dose' on page 2 undefined on input line 108.\n\n[2]\n\nLaTeX Warning: Reference `tab:training_loss' on page 3 undefined on input line \n143.\n\n\nLaTeX Warning: Reference `tab:webshop' on page 3 undefined on input line 170.\n\n[3]\n\nLaTeX Warning: Reference `tab:failure_types' on page 4 undefined on input line \n213.\n\n\nLaTeX Warning: Reference `tab:echoes' on page 4 undefined on input line 237.\n\n[4]\n\nLaTeX Warning: Reference `tab:scale' on page 5 undefined on input line 262.\n\n\nLaTeX Warning: Reference `tab:fewshot' on page 5 undefined on input line 303.\n\n\nLaTeX Warning: Reference `tab:peroperator' on page 5 undefined on input line 33\n0.\n\n[5]\n\nLaTeX Warning: Reference `tab:structural' on page 6 undefined on input line 379\n.\n\n[6]\n\nLaTeX Warning: Reference `sec:scale' on page 7 undefined on input line 414.\n\n\nPackage natbib Warning: Citation `paladin2025' on page 7 undefined on input lin\ne 429.\n\n[7]\n\nPackage natbib Warning: Citation `eef2025' on page 8 undefined on input line 43\n1.\n\n\nPackage natbib Warning: Citation `alfworld2021' on page 8 undefined on input li\nne 433.\n\n\nPackage natbib Warning: Citation `webshop2022' on page 8 undefined on input lin\ne 433.\n\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw\n/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.\npfb>\nOutput written on paper.pdf (9 pages, 124637 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `paladin2025' on page 1 undefined on input lin\ne 36.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3] [4] [5]\n[6]\n\nPackage natbib Warning: Citation `paladin2025' on page 7 undefined on input lin\ne 429.\n\n[7]\n\nPackage natbib Warning: Citation `eef2025' on page 8 undefined on input line 43\n1.\n\n\nPackage natbib Warning: Citation `alfworld2021' on page 8 undefined on input li\nne 433.\n\n\nPackage natbib Warning: Citation `webshop2022' on page 8 undefined on input lin\ne 433.\n\nNo file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[8] [9] (./paper.aux) )&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 126772 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "66aced20-4d7e-4564-9ee0-126af296aea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T02:40:49.758Z_

PDF 编译成功，9 页，所有交叉引用已解析。仅有 citation warnings（无 .bib 文件，预期行为）。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median/paper.pdf`

论文包含 Abstract、Introduction、Method、Main Results（clean performance + dose-response + recovery/detection）、6 个补充实验各自独立 section/table（Training Dynamics、WebShop 跨环境复制、Qualitative Failure Analysis、Scale Ablation、Recovery Prompting、Per-Operator Deep Dive）、Discussion（含 hierarchical claims 结构）、Related Work、Conclusion。所有定量 claim 均取自 experiment\_data.json，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63d445d5-6ce9-4ee9-a981-c61ff0396706",
  "isSidechain": false,
  "requestId": "req_011Cb3ahSKTfRrQ1AaFVXhoK",
  "type": "assistant",
  "uuid": "d66dbbcf-66f9-41aa-971b-acfc6c682509",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/median",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeB3hEhvw4YrnrPxBKLJFp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5989,
      "cache_read_input_tokens": 52740,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5989,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 52740,
          "cache_creation_input_tokens": 5989,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5989
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject…",
  "leafUuid": "d66dbbcf-66f9-41aa-971b-acfc6c682509",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for error injection study",
  "sessionId": "d54f4a62-2b0f-48cd-b7b1-e6838b1f3fae"
}
```

---
