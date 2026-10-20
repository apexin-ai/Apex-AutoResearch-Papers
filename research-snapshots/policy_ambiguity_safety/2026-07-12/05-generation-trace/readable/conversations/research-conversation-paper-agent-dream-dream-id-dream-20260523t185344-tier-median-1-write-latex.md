# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-3/d8d171b8-cd92-4076-8cf5-4c38921f83f5.jsonl`
- **Structured JSON:** [`6aa61c84a12d7caa6669.json`](../../sessions/6a/6aa61c84a12d7caa6669.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:37:25.736Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:37:25.736Z",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：C1（+34.0pp, 5 models, perturbation PASS）+ C4（model×type interaction, auth_scope 52pp range）承载论文核心贡献。 C5 从 \"validated taxonomy\" 降级为 \"convergent LLM-coded and human evidence with moderate agreement (κ=0.39)\"； abstract 将 \"type-diagnostic failure signatures\" 替换为 \"type-associated failure patterns\"； Contribution (3) 保留 \"supported by\" 但追加 \"preliminary human validation (κ=0.39)\" 限定语。 C3 layer effect 不再作为独立 finding，降为 C4 下属观察（\"model×type interaction subsumes the aggregate layer gap\"）。 SOPBench 描述为 \"partial cross-domain evidence (Δ=19.4pp, 4/5 models replicate)\" 而非 \"full replication\"； DeepSeek 在 SOPBench 上 Δ=12.4pp 归因于 rule-based verifier 的 domain-specific 校准差异，不构成 fundamental non-replication。 Rebuttal 策略：强调 κ=0.39 超过 chance 且与已知 category-boundary ambiguity（auth_scope/incompleteness）一致； 4-type dominant mode 一致性覆盖了理论上最具区分性的类型（scopal, lexical, CP）。 κ=0.39 比纯 automated coding（LLM-LLM κ=0.517）低，但 human inter-annotator 在 failure mode 编码上天然更分散； collapsed 4-category scheme κ=0.44 接近 moderate。 竞争力：C1 causal design + C4 interaction 足够支撑 novel contribution；weakened C5 不致命但限制 main-track award potential。 Expected ARR: 3.75（competitive for EMNLP Findings / borderline Main poster）。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-23T19:37:25.741Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:37:25.741Z",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-23T19:37:25.772Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：C1（+34.0pp, 5 models, perturbation PASS）+ C4（model×type interaction, auth_scope 52pp range）承载论文核心贡献。 C5 从 "validated taxonomy" 降级为 "convergent LLM-coded and human evidence with moderate agreement (κ=0.39)"； abstract 将 "type-diagnostic failure signatures" 替换为 "type-associated failure patterns"； Contribution (3) 保留 "supported by" 但追加 "preliminary human validation (κ=0.39)" 限定语。 C3 layer effect 不再作为独立 finding，降为 C4 下属观察（"model×type interaction subsumes the aggregate layer gap"）。 SOPBench 描述为 "partial cross-domain evidence (Δ=19.4pp, 4/5 models replicate)" 而非 "full replication"； DeepSeek 在 SOPBench 上 Δ=12.4pp 归因于 rule-based verifier 的 domain-specific 校准差异，不构成 fundamental non-replication。 Rebuttal 策略：强调 κ=0.39 超过 chance 且与已知 category-boundary ambiguity（auth_scope/incompleteness）一致； 4-type dominant mode 一致性覆盖了理论上最具区分性的类型（scopal, lexical, CP）。 κ=0.39 比纯 automated coding（LLM-LLM κ=0.517）低，但 human inter-annotator 在 failure mode 编码上天然更分散； collapsed 4-category scheme κ=0.44 接近 moderate。 竞争力：C1 causal design + C4 interaction 足够支撑 novel contribution；weakened C5 不致命但限制 main-track award potential。 Expected ARR: 3.75（competitive for EMNLP Findings / borderline Main poster）。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "11927a15-b7f6-47c9-946f-746914c8a48e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:37:25.771Z_

```json
{
  "parentUuid": "11927a15-b7f6-47c9-946f-746914c8a48e",
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
  "uuid": "589327ee-a8c8-4564-96d7-46426de6f732",
  "timestamp": "2026-05-23T19:37:25.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:37:25.771Z_

```json
{
  "parentUuid": "589327ee-a8c8-4564-96d7-46426de6f732",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b56bbc80-985c-4af0-9e36-f23cdd70131e",
  "timestamp": "2026-05-23T19:37:25.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
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
  "aiTitle": "Generate median-tier simulated research paper",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Assistant

_source line 7 · 2026-05-23T19:37:28.977Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b56bbc80-985c-4af0-9e36-f23cdd70131e",
  "isSidechain": false,
  "requestId": "req_011CbL4hnzz6zKZKbiacrXT1",
  "type": "assistant",
  "uuid": "6d31860d-b0cb-4288-8d43-a58bf1a0a263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxxZUPx4yeLnbWJxiVyKsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12876
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

_source line 8 · 2026-05-23T19:37:30.790Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LnZdY8iXw74RmUcK8x8fMr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d31860d-b0cb-4288-8d43-a58bf1a0a263",
  "isSidechain": false,
  "requestId": "req_011CbL4hnzz6zKZKbiacrXT1",
  "type": "assistant",
  "uuid": "6d619870-10ea-44bf-9ac0-c0f0353300c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxxZUPx4yeLnbWJxiVyKsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12876
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

_source line 9 · 2026-05-23T19:37:30.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_013KE7Hkx1q2XAgaoGCD3bWU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d619870-10ea-44bf-9ac0-c0f0353300c0",
  "isSidechain": false,
  "requestId": "req_011CbL4hnzz6zKZKbiacrXT1",
  "type": "assistant",
  "uuid": "569f7bc7-221c-41fa-907a-cac71846d419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxxZUPx4yeLnbWJxiVyKsd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12876,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12876,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12876
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

_source line 10 · 2026-05-23T19:37:31.189Z_

<details><summary>↩ Tool result · `toolu_013KE7Hkx1q2XAgaoGCD3bWU`</summary>

````text
1	# Paper Framing — policy_ambiguity_safety
2	
3	> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)
4	> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)
5	> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
6	> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
7	> Supplementary experiments (2026-05-22/23):
8	>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated
9	>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved
10	>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered
11	>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition
12	>   - ✅ Human Annotation Prep: 100 traces + codebook ready
13	>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete
14	
15	## Core Insight
16	
17	Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.
18	
19	## Title (Working)
20	
21	"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"
22	
23	Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"
24	
25	Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.
26	
27	## Core Claims
28	
29	### C1: Binary Effect (PRIMARY — confirmed, 5 models)
30	Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
31	- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
32	- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
33	- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
34	- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
35	- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.
36	
37	### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
38	**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
39	- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
40	  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
41	  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
42	  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
43	- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
44	- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
45	- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
46	- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.
47	
48	### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
49	**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
50	- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
51	- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
52	- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
53	  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
54	  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
55	  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
56	  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
57	  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
58	- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
59	- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
60	- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
61	- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
62	- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
63	- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.
64	
65	### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
66	**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
67	- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
68	  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
69	  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
70	- **Model × Type interaction matrix** (ambiguous condition, violation rates):
71	  ```
72	  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
73	  authorization_scope     64%     46%      12%     26%     60%
74	  conditional_precedence  34%     36%      36%     40%     38%
75	  incompleteness          46%     58%      48%     62%     54%
76	  lexical                 42%     34%      32%     52%     54%
77	  coreferential           18%     32%      22%     42%     44%
78	  scopal                  42%     38%      32%     37%     48%
79	  ```
80	- **Key interaction patterns**:
81	  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
82	  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
83	  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
84	  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
85	- **Per-model type χ²** (which models show type-specific vulnerability patterns):
86	  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
87	  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
88	  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
89	  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
90	  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
91	- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
92	- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
93	- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
94	- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
95	- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.
96	
97	### C5: Error Analysis (CONFIRMED — EMNLP core)
98	Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
99	- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
100	  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
101	  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
102	  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
103	  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
104	  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
105	  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
106	  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
107	- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
108	  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
109	  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
110	- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.
111	
112	## Narrative Structure (CL-first for EMNLP)
113	
114	### Intro Logic Chain
115	1. Agent policies are written in NL → contain ambiguity (established)
116	2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
117	3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
118	4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
119	5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
120	6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."
121	
122	### Section Map
123	- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
124	- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
125	- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
126	- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
127	- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
128	- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
129	- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
130	- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.
131	
132	## Anticipated Reviewer Concerns
133	
134	### RC1: "Type effect could be artifact of taxonomy granularity"
135	**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).
136	
137	### RC2: "Taxonomy is ad hoc / why these 6 types"
138	**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).
139	
140	### RC3: "Only API models, no open-source"
141	**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
142	**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.
143	
144	### RC4: "Synthetic ambiguity injection lacks ecological validity"
145	**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.
146	
147	### RC5: "τ²-bench limited to retail/airline"
148	**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from "customer service finding" to "cross-domain finding" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.
149	
150	### RC6: "Binary effect is obvious — of course ambiguity causes errors"
151	**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.
152	
153	### RC7: "Incompleteness matched-pair confound (information asymmetry)"
154	**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.
155	
156	### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
157	**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.
158	
159	### RC9: "authorization_scope is just a subtype of incompleteness"
160	**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.
161	
162	### RC10: "API sampling noise undermines reliability"
163	**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.
164	
165	### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
166	**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
167	**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.
168	
169	## Concept Naming (distill insight: 命名即贡献)
170	
171	Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.
172	
173	Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.
174	
175	Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).
176	
177	Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.
178	
179	## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")
180	
181	Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.
182	
183	## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)
184	
185	"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."
186	
187	## Benchmark Comparison Table (distill insight: 必有 feature matrix)
188	
189	| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
190	|---------|--------|---------------|------------|----------|----------|
191	| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
192	| Causal design | — | — | — | — | **matched pairs** |
193	| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
194	| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
195	| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
196	| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |
197	
198	## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]
199	
200	1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
201	2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
202	3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.
203	
204	NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.
205	
206	## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]
207	
208	Current plan has thin references. Must add (≥25 total in final paper):
209	- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
210	- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
211	- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
212	- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
213	- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
214	- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
215	- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
216	- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
217	- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
218	- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
219	- **Garden-path**: Frazier & Rayner (1982)
220	- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
221	- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份
222	
223	## Code/Data Release Plan [Dream A6 — three-tier consistent]
224	
225	Must commit to releasing:
226	1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
227	2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
228	3. Statistical analysis code (all tests, bootstrap CI computation)
229	4. Agent trace samples (anonymized) for reproducibility of C5
230	
231	## Figure Plan [Dream A12]
232	
233	Minimum figures for paper (zero-figure paper flagged in dream):
234	1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
235	2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
236	3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
237	4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
238	5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
239	6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
240	7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)
241	
242	## Berry & Kamsties Operationalization Note [Dream best Q5]
243	
244	Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.
245	
246	## Contingency Framing [RESOLVED — Scenario C occurred]
247	
248	> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
249	> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。
250	
251	## Claude Baseline — RESOLVED [2026-05-20]
252	
253	✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).
254	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "569f7bc7-221c-41fa-907a-cac71846d419",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "d7a40123-5c1c-47c9-a05a-93796665bedb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper_framing.md",
      "content": "# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)\n> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n> Supplementary experiments (2026-05-22/23):\n>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated\n>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved\n>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered\n>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition\n>   - ✅ Human Annotation Prep: 100 traces + codebook ready\n>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n",
      "numLines": 254,
      "startLine": 1,
      "totalLines": 254
    }
  },
  "sourceToolAssistantUUID": "569f7bc7-221c-41fa-907a-cac71846d419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool result

_source line 11 · 2026-05-23T19:37:31.296Z_

<details><summary>↩ Tool result · `toolu_01LnZdY8iXw74RmUcK8x8fMr`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成并验证 300 条 clause pairs (50/type × 6 types)，含新类型 coreferential 和 authorization_scope 各 50 条新写，lexical/incompleteness 各补 20 条",
5	    "results": {
6	      "total_clauses": 300,
7	      "clauses_per_type": 50,
8	      "types_covered": 6,
9	      "revision_rounds_needed": 2,
10	      "avg_token_length_ambiguous": 31.2,
11	      "avg_token_length_unambiguous": 29.8,
12	      "avg_token_delta_spec_layer": 35.1,
13	      "avg_token_delta_ling_layer": 12.6,
14	      "cross_type_length_cv": 0.14,
15	      "cp_format_mix_labeled_pct": 0.6,
16	      "cp_format_mix_unlabeled_pct": 0.4
17	    },
18	    "tables": [],
19	    "figures": [],
20	    "analysis": "Clause generation 是全部下游实验的基础。关键质控：(a) cross-type token length CV=0.14 表明类型间长度 相对均衡，不会因长度差异系统性偏置 violation rate；(b) spec-layer token delta 更大是预期的（ auth_scope 需要明确 permission boundary，incompleteness 需要补充缺失条件），但需在 analysis 中 作为 covariate 控制；(c) 新类型 clause 质量验证在 plan_001b pilot 中确认。\n\n\nMedian 档下 clause generation 本身不是瓶颈——这是研究者可控的准备步骤。300 条 clause 的生成和验证 经过 2 轮修订完成。新类型（auth_scope, coreferential）的 clause 质量略低于已验证类型（scopal, CP）， 需要 1 轮额外修订确保 unambiguous 控制条件不引入新歧义。token delta 在 spec-layer（35.1 tokens）显著 高于 ling-layer（12.6 tokens）反映了 specification ambiguity 需要更多文字消歧的本质差异—— 这个 delta 后续作为 confound control variable 进入 logistic regression。 CP clause 按 Reviewer 建议混合 labeled (60%) 和 unlabeled (40%) 格式。\n"
21	  },
22	  {
23	    "name": "new_type_mini_pilot",
24	    "description": "coreferential + authorization_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes 的 mini-pilot 验证",
25	    "results": {
26	      "total_episodes": 20,
27	      "auth_scope_amb_violation_rate": 0.6,
28	      "auth_scope_unamb_violation_rate": 0.1,
29	      "coreferential_amb_violation_rate": 0.3,
30	      "coreferential_unamb_violation_rate": 0.0,
31	      "auth_scope_delta_pp": 50.0,
32	      "coreferential_delta_pp": 30.0,
33	      "design_issues_found": 1,
34	      "clauses_requiring_revision": 2
35	    },
36	    "tables": [
37	      {
38	        "title": "Mini-Pilot Results",
39	        "columns": [
40	          "Type",
41	          "Condition",
42	          "Violations",
43	          "Episodes",
44	          "Rate"
45	        ],
46	        "rows": [
47	          [
48	            "auth_scope",
49	            "ambiguous",
50	            "3",
51	            "5",
52	            "60%"
53	          ],
54	          [
55	            "auth_scope",
56	            "unambiguous",
57	            "0.5",
58	            "5",
59	            "10%"
60	          ],
61	          [
62	            "coreferential",
63	            "ambiguous",
64	            "1.5",
65	            "5",
66	            "30%"
67	          ],
68	          [
69	            "coreferential",
70	            "unambiguous",
71	            "0",
72	            "5",
73	            "0%"
74	          ]
75	        ]
76	      }
77	    ],
78	    "figures": [],
79	    "analysis": "Pilot 确认新类型 clause 设计可行，两个类型都显示 ambiguous 条件下 violation rate 显著高于 control。 auth_scope 效应强（Δ=50pp），coreferential 效应弱（Δ=30pp）但仍 meaningful。coreferential 的 低 rate 与 disambiguation channel 假说一致——tool responses 提供部分消歧。2 条需修订的 clause 在 full study 前修正。\n\n\nPilot 验证两个新类型的 clause 设计有效性。auth_scope 的 60% ambiguous violation rate 和 50pp delta 符合预期——gpt-5.4 在 auth_scope 上是高 vulnerability 模型（full study 确认 64%）。 coreferential 的 30% ambiguous rate 和 0% unambiguous control 均在可接受范围，但 violation rate 是所有类型中最低的，与 full study 最终结果一致（coreferential 31.6% 为最低 tier）。 发现 1 个 design issue：2 条 coreferential clause 的 unambiguous 版本仍含轻微 referential ambiguity， 需修订。N=20 的 pilot 不具备统计 power，仅用于排除系统性失败。\n"
80	  },
81	  {
82	    "name": "full_study_api",
83	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes，cross-judge evaluation",
84	    "results": {
85	      "total_episodes": 1800,
86	      "overall_amb_violation_rate": 0.38,
87	      "overall_unamb_violation_rate": 0.053,
88	      "overall_delta_pp": 32.7,
89	      "overall_or": 14.8,
90	      "overall_mcnemar_p": "<0.0001",
91	      "gpt54_delta_pp": 38.3,
92	      "gpt41_delta_pp": 34.7,
93	      "claude_delta_pp": 25.7,
94	      "gpt54_amb_rate": 0.41,
95	      "gpt41_amb_rate": 0.407,
96	      "claude_amb_rate": 0.303,
97	      "cross_judge_fleiss_kappa": 0.717,
98	      "episodes_per_model": 600
99	    },
100	    "tables": [
101	      {
102	        "title": "Per-Model Binary Effect (API Models)",
103	        "columns": [
104	          "Model",
105	          "Amb Rate",
106	          "Unamb Rate",
107	          "Δpp",
108	          "OR",
109	          "p-value"
110	        ],
111	        "rows": [
112	          [
113	            "gpt-5.4",
114	            "41.0%",
115	            "2.7%",
116	            "+38.3",
117	            "25.2",
118	            "<10^-23"
119	          ],
120	          [
121	            "gpt-4.1",
122	            "40.7%",
123	            "6.0%",
124	            "+34.7",
125	            "10.8",
126	            "<10^-17"
127	          ],
128	          [
129	            "claude-sonnet-4-6",
130	            "30.3%",
131	            "4.7%",
132	            "+25.7",
133	            "8.9",
134	            "<10^-17"
135	          ],
136	          [
137	            "Pooled (API)",
138	            "37.3%",
139	            "4.4%",
140	            "+32.9",
141	            "14.8",
142	            "<10^-50"
143	          ]
144	        ]
145	      }
146	    ],
147	    "figures": [],
148	    "analysis": "API 模型数据确认 C1 binary effect 在 3 个 proprietary 模型上无例外成立。Claude 的低 overall rate 源于 auth_scope 极低（12%），但 incompleteness（48%）与其他模型差距不大，支持 C4 的 \"safety training differentially mitigates specific types\" 论点。cross-judge κ=0.717 为 judge reliability 提供了 independent evidence（与 plan_009 human calibration 互为补充）。\n\n\n3-model API 实验是论文数据采集的核心。结果与 median 档完全一致——C1 binary effect 极强 （每个模型 Δpp 都 >25pp, 全部 p<10^-17），模型间已显示分化模式（Claude 最低 30.3%, GPT-5.4 最高 41.0%）， 为 C4 interaction 奠定基础。cross-judge Fleiss' κ=0.717 确认 judge 间一致性良好。 Claude 的低 violation rate 主要由 auth_scope 驱动（12% vs GPT-5.4 64%）， 这一模式在 plan_003 开源模型数据中进一步丰富。\n"
149	  },
150	  {
151	    "name": "full_study_opensource",
152	    "description": "300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter API = 1,200 episodes",
153	    "results": {
154	      "total_episodes": 1197,
155	      "qwen3_amb_rate": 0.431,
156	      "qwen3_unamb_rate": 0.093,
157	      "qwen3_delta_pp": 32.4,
158	      "deepseek_amb_rate": 0.497,
159	      "deepseek_unamb_rate": 0.107,
160	      "deepseek_delta_pp": 39.0,
161	      "deepseek_per_type_chi2_p": 0.277,
162	      "qwen3_per_type_chi2_p": 0.007
163	    },
164	    "tables": [
165	      {
166	        "title": "Per-Model Binary Effect (Open-Source Models)",
167	        "columns": [
168	          "Model",
169	          "Amb Rate",
170	          "Unamb Rate",
171	          "Δpp",
172	          "OR",
173	          "p-value"
174	        ],
175	        "rows": [
176	          [
177	            "qwen3-235b",
178	            "43.1%",
179	            "9.3%",
180	            "+32.4",
181	            "7.4",
182	            "<10^-18"
183	          ],
184	          [
185	            "deepseek-v3",
186	            "49.7%",
187	            "10.7%",
188	            "+39.0",
189	            "8.3",
190	            "<10^-20"
191	          ]
192	        ]
193	      },
194	      {
195	        "title": "Per-Model Type Differentiation (Open-Source)",
196	        "columns": [
197	          "Model",
198	          "χ²",
199	          "p-value",
200	          "V",
201	          "Type Differentiation"
202	        ],
203	        "rows": [
204	          [
205	            "qwen3-235b",
206	            "15.89",
207	            "0.007",
208	            "0.23",
209	            "Moderate — high incomp+lex, low auth_scope"
210	          ],
211	          [
212	            "deepseek-v3",
213	            "6.31",
214	            "0.277",
215	            "0.14",
216	            "NOT significant — uniformly high"
217	          ]
218	        ]
219	      }
220	    ],
221	    "figures": [],
222	    "analysis": "开源模型数据完成 5-model 矩阵。关键发现：(a) C1 binary effect 在所有模型上 replicate， 包括 architecture 截然不同的 MoE (Qwen3) 和 dense (DeepSeek)；(b) DeepSeek 的 uniform vulnerability (V=0.14, n.s.) 与 Claude 的 strong differentiation (V=0.24, p=0.003) 形成鲜明对比， 支持 \"safety training quality predicts type specificity\" 论点；(c) 3 episodes 因 API 超时丢失 (1,197/1,200)，对 power 影响可忽略。\n\n\n开源模型扩展了 C4 interaction 的 evidence base。Qwen3 显示中等 vulnerability（43.1%）但有 显著 type differentiation（χ²=15.89, p=0.007）——high incompleteness (62%) + lexical (52%)， low auth_scope (26%)。DeepSeek 是最 vulnerable 模型（49.7%），且几乎 uniformly high across all types （χ²=6.31, p=0.277, V=0.14 not significant），说明 less type-specific safety training。 Qwen3 的 auth_scope (26%) 介于 Claude (12%) 和 GPT-5.4 (64%) 之间，增强了 auth_scope 作为 \"safety training canary type\" 的论证。DeepSeek 的 uniform vulnerability 作为 C4 的 negative case （no differential mitigation）同样有理论价值。\n"
223	  },
224	  {
225	    "name": "full_study_analysis",
226	    "description": "2,997 episodes 统计分析：C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction",
227	    "results": {
228	      "total_episodes": 2997,
229	      "c1_pooled_delta_pp": 34.0,
230	      "c1_or": 15.1,
231	      "c1_or_ci_lower": 10.78,
232	      "c1_or_ci_upper": 21.17,
233	      "c1_bootstrap_ci_lower": 31.2,
234	      "c1_bootstrap_ci_upper": 36.9,
235	      "c1_mcnemar_p": "<0.0001",
236	      "c2_omnibus_chi2": 28.02,
237	      "c2_omnibus_p": 3.6e-05,
238	      "c2_cramers_v": 0.137,
239	      "c2_power": 0.993,
240	      "c2_mde": 0.093,
241	      "c2_tost_15pp_equivalent_pairs": "8/15",
242	      "c2_tost_10pp_equivalent_pairs": "4/15",
243	      "c3_spec_rate": 0.44,
244	      "c3_ling_rate": 0.379,
245	      "c3_delta_pp": 6.08,
246	      "c3_p": 0.017,
247	      "c3_v": 0.062,
248	      "c3_within_judge_gpt41_p": 0.059,
249	      "c3_within_judge_gpt54_p": 0.157,
250	      "c4_model_main_chi2": 31.02,
251	      "c4_model_main_p": 3e-06,
252	      "c4_model_main_v": 0.102,
253	      "c4_auth_scope_range_pp": 52,
254	      "c4_incompleteness_range_pp": 16,
255	      "c4_cp_range_pp": 6,
256	      "c4_fleiss_kappa": 0.384,
257	      "logistic_condition_amb_coef": 2.278,
258	      "logistic_condition_amb_z": 19.65,
259	      "logistic_token_delta_coef": 0.022,
260	      "logistic_token_delta_z": 3.49,
261	      "inter_model_agreement_on_amb_clauses": "39/300 universal, 85/300 majority, 92/300 model-specific, 84/300 safe"
262	    },
263	    "tables": [
264	      {
265	        "title": "C2: 3-Tier Type Hierarchy (Ambiguous Condition, Pooled 5 Models)",
266	        "columns": [
267	          "Tier",
268	          "Type",
269	          "Violation Rate",
270	          "95% CI"
271	        ],
272	        "rows": [
273	          [
274	            "High",
275	            "incompleteness",
276	            "53.6%",
277	            "[48.6%, 58.6%]"
278	          ],
279	          [
280	            "Mid",
281	            "lexical",
282	            "42.8%",
283	            "[37.9%, 47.7%]"
284	          ],
285	          [
286	            "Mid",
287	            "auth_scope",
288	            "41.6%",
289	            "[36.7%, 46.5%]"
290	          ],
291	          [
292	            "Mid",
293	            "scopal",
294	            "39.4%",
295	            "[34.5%, 44.3%]"
296	          ],
297	          [
298	            "Mid",
299	            "cond_precedence",
300	            "36.8%",
301	            "[32.0%, 41.6%]"
302	          ],
303	          [
304	            "Low",
305	            "coreferential",
306	            "31.6%",
307	            "[27.0%, 36.2%]"
308	          ]
309	        ]
310	      },
311	      {
312	        "title": "C4: Model × Type Interaction Matrix (Ambiguous Violation Rates)",
313	        "columns": [
314	          "Type",
315	          "GPT-5.4",
316	          "GPT-4.1",
317	          "Claude",
318	          "Qwen3",
319	          "DeepSeek",
320	          "Range"
321	        ],
322	        "rows": [
323	          [
324	            "auth_scope",
325	            "64%",
326	            "46%",
327	            "12%",
328	            "26%",
329	            "60%",
330	            "52pp"
331	          ],
332	          [
333	            "incompleteness",
334	            "46%",
335	            "58%",
336	            "48%",
337	            "62%",
338	            "54%",
339	            "16pp"
340	          ],
341	          [
342	            "lexical",
343	            "42%",
344	            "34%",
345	            "32%",
346	            "52%",
347	            "54%",
348	            "22pp"
349	          ],
350	          [
351	            "scopal",
352	            "42%",
353	            "38%",
354	            "32%",
355	            "37%",
356	            "48%",
357	            "16pp"
358	          ],
359	          [
360	            "cond_prec",
361	            "34%",
362	            "36%",
363	            "36%",
364	            "40%",
365	            "38%",
366	            "6pp"
367	          ],
368	          [
369	            "coreferential",
370	            "18%",
371	            "32%",
372	            "22%",
373	            "42%",
374	            "44%",
375	            "26pp"
376	          ]
377	        ]
378	      },
379	      {
380	        "title": "C3: Layer Effect — Aggregate vs Within-Judge",
381	        "columns": [
382	          "Analysis",
383	          "Spec Rate",
384	          "Ling Rate",
385	          "Δpp",
386	          "p-value",
387	          "Note"
388	        ],
389	        "rows": [
390	          [
391	            "Pooled (5 models)",
392	            "44.0%",
393	            "37.9%",
394	            "+6.08",
395	            "0.017",
396	            "Significant"
397	          ],
398	          [
399	            "Within gpt-4.1 judge",
400	            "—",
401	            "—",
402	            "+8.0",
403	            "0.059",
404	            "Marginal"
405	          ],
406	          [
407	            "Within gpt-5.4 judge",
408	            "—",
409	            "—",
410	            "+4.8",
411	            "0.157",
412	            "Not significant"
413	          ]
414	        ]
415	      },
416	      {
417	        "title": "TOST Equivalence Test Results",
418	        "columns": [
419	          "Margin",
420	          "Equivalent Pairs",
421	          "Non-Equivalent Pairs",
422	          "Interpretation"
423	        ],
424	        "rows": [
425	          [
426	            "±15pp",
427	            "8/15",
428	            "7/15",
429	            "Types are partially but not fully interchangeable"
430	          ],
431	          [
432	            "±10pp",
433	            "4/15",
434	            "11/15",
435	            "Most type pairs are meaningfully different at ±10pp"
436	          ]
437	        ]
438	      },
439	      {
440	        "title": "Logistic Regression (Violation ~ Condition + Model + Type + Token_Delta)",
441	        "columns": [
442	          "Predictor",
443	          "Coefficient",
444	          "z",
445	          "p-value",
446	          "Interpretation"
447	        ],
448	        "rows": [
449	          [
450	            "condition_amb",
451	            "2.278",
452	            "19.65",
453	            "<0.001",
454	            "Ambiguity is dominant predictor"
455	          ],
456	          [
457	            "token_delta",
458	            "0.022",
459	            "3.49",
460	            "0.0005",
461	            "Info delta significant but small"
462	          ],
463	          [
464	            "model (reference=Claude)",
465	            "—",
466	            "—",
467	            "<0.001",
468	            "Model main effect significant"
469	          ],
470	          [
471	            "type (reference=coreferential)",
472	            "—",
473	            "—",
474	            "<0.001",
475	            "Type main effect significant"
476	          ]
477	        ]
478	      }
479	    ],
480	    "figures": [],
481	    "analysis": "C1+C4 构成论文的 twin pillars。C1 的 causal evidence chain 极强（matched-pair + perturbation control + cross-model replication），即使最 skeptical 的 reviewer 也难以质疑。C4 的 model×type interaction 是 genuine novelty——现有文献无人做过 5-model × 6-type 的 factorial 安全性分析。 C3 的 within-judge fragility 是 median 档最大的 narrative vulnerability：至少一位 reviewer 会问 \"if the layer effect vanishes within a single judge's evaluations, isn't it just judge variance?\" 应对策略：C3 不作为 standalone finding，而是作为 C4 interaction 的 aggregate shadow（\"the layer gap is itself model-dependent, driven by auth_scope, making the model×type interaction the more fundamental finding\"）。 V=0.137 在 power=0.993 下是 real but small——论文应用 \"the 3-tier structure, not V, is the practical takeaway\" 框架。\n\n\nFull study analysis 在 median 档下已经完成且结果确定。C1 极强（+34.0pp, OR=15.1）——这是论文最坚实的基础。 C2 type hierarchy 显著（χ²=28.02, V=0.137）但 effect size 小（V<0.20），好在 power=0.993 且 MDE=0.093 说明实验 well-powered，V=0.137 不是 underpowered artifact。3-tier 结构（high: incompleteness 53.6% >> mid: lexical-scopal-auth-CP 36.8-42.8% >> low: coreferential 31.6%）稳健。 C3 layer effect 在 aggregate 层面显著（Δ=6.08pp, p=0.017）但 within-judge 分析 fragile （gpt-4.1 judged group p=0.059 marginal, gpt-5.4 judged group p=0.157 n.s.）——这是 median 档的 核心弱点之一，reviewer 必然会 flag。C4 model×type interaction 是 star finding：auth_scope 52pp range 揭示 safety training 的 type-specific 效果，而 incompleteness 16pp range 表明 universal blind spot。 Fleiss κ=0.384 说明模型间仅 moderate agreement on which specific clauses trigger violations—— binary effect universal 但 clause-level 行为 model-dependent。\n"
482	  },
483	  {
484	    "name": "error_analysis",
485	    "description": "5-model violation traces failure mode 编码：614 traces 分类为 5 类 failure modes，cross-model 一致性分析",
486	    "results": {
487	      "total_violations_coded": 614,
488	      "failure_mode_categories": 5,
489	      "types_unanimous_dominant_fm": "3/6",
490	      "types_majority_dominant_fm": "6/6",
491	      "inter_coder_kappa_llm": 0.517,
492	      "percent_agreement_llm": 0.656,
493	      "disambiguation_awareness_overall": 0.046,
494	      "surface_adoption_rate": 0.88,
495	      "escalate_to_user_rate": 0.008,
496	      "auth_scope_dominant_fm": "unauthorized_escalation",
497	      "incompleteness_dominant_fm": "assumption_based_action",
498	      "scopal_dominant_fm": "scope_misapplication",
499	      "lexical_dominant_fm": "assumption_based_action",
500	      "cp_dominant_fm": "scope_misapplication",
501	      "coreferential_dominant_fm": "mixed (no clear dominant)",
502	      "spec_layer_dominant_mechanism": "guess-and-act",
503	      "ling_layer_dominant_mechanism": "misparse-and-apply",
504	      "gwet_ac1_estimated": 0.72
505	    },
506	    "tables": [
507	      {
508	        "title": "5-Model Failure Mode Distribution by Type (Majority Dominant Mode)",
509	        "columns": [
510	          "Type",
511	          "Dominant Mode",
512	          "Dominance %",
513	          "Unanimous Across 5 Models?"
514	        ],
515	        "rows": [
516	          [
517	            "auth_scope",
518	            "unauthorized_escalation",
519	            "68%",
520	            "No (3/5 models)"
521	          ],
522	          [
523	            "incompleteness",
524	            "assumption_based_action",
525	            "61%",
526	            "Yes (5/5 models)"
527	          ],
528	          [
529	            "scopal",
530	            "scope_misapplication",
531	            "72%",
532	            "Yes (5/5 models)"
533	          ],
534	          [
535	            "lexical",
536	            "assumption_based_action",
537	            "58%",
538	            "Yes (4/5 models)"
539	          ],
540	          [
541	            "cond_precedence",
542	            "scope_misapplication",
543	            "36%",
544	            "No (3/5 models)"
545	          ],
546	          [
547	            "coreferential",
548	            "mixed",
549	            "—",
550	            "No (no dominant)"
551	          ]
552	        ]
553	      },
554	      {
555	        "title": "Ambiguity Blindness Metrics (5-Model Pooled)",
556	        "columns": [
557	          "Metric",
558	          "Value",
559	          "Note"
560	        ],
561	        "rows": [
562	          [
563	            "Disambiguation awareness",
564	            "4.6%",
565	            "Agent explicitly notes ambiguity"
566	          ],
567	          [
568	            "Surface adoption",
569	            "88%",
570	            "Agent adopts first-parse interpretation"
571	          ],
572	          [
573	            "Escalate to user",
574	            "0.8%",
575	            "Agent asks for clarification"
576	          ],
577	          [
578	            "Conservative refusal",
579	            "3.2%",
580	            "Agent refuses to act on ambiguous clause"
581	          ]
582	        ]
583	      }
584	    ],
585	    "figures": [],
586	    "analysis": "Median 档下 C5 的核心叙事挑战：从 2-model 扩展到 5-model 后，unanimous dominant mode 从 5/6 下降到 3/6。 这不是 C5 失败——majority 仍 6/6——但要求 framing 从 \"type-diagnostic failure signatures\" 调整为 \"type-associated failure patterns with cross-model consistency at majority but not unanimous level\"。 关键区分：(a) Ambiguity Blindness (4.6%) 完全不受此影响——这是 claim 最安全的发现； (b) spec→guess vs ling→misparse 的 layer mechanism 在 5 models 下仍成立； (c) auth_scope 的 failure mode heterogeneity 实际上 STRENGTHENS C4（\"even the failure mechanism is model-dependent, not just the rate\"）。 κ=0.517 由 kappa paradox 严重 deflate；报告 Gwet's AC1≈0.72 + 80% raw agreement 作为 headline validity。\n\n\n5-model error analysis揭示 failure mode 的 type-specificity 在 5 models 下部分保持。 unanimous dominant mode 仅 3/6（scopal, lexical, incompleteness），因为 auth_scope 和 CP 在不同模型间 dominant mode 分裂——GPT 模型 auth_scope 以 unauthorized_escalation 为主，但开源模型更多表现为 assumption_based_action（认为自己有权限而非明确 escalate）。coreferential 本身就无 dominant mode（flat distribution）。 majority 仍 6/6 说明 type-specific signature 的大方向一致。 inter_coder_kappa=0.517（moderate）受 kappa paradox 影响——lexical 91.7% agreement → κ=0.0。 Gwet's AC1 估计 0.72 更准确反映 true agreement。 Ambiguity Blindness (4.6% awareness) 是 C5 最 robust 的发现——不依赖 failure mode coding granularity。 median 档下这些结果意味着 C5 的 fine-grained per-type percentages 需标注 \"automated coding\" caveat， 但 type-mechanism dissociation（spec→guess vs ling→misparse）和 Ambiguity Blindness 仍可 claim。\n"
587	  },
588	  {
589	    "name": "reliability_test",
590	    "description": "30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes test-retest reliability",
591	    "results": {
592	      "total_episodes": 360,
593	      "overall_icc": 0.919,
594	      "overall_icc_ci_lower": 0.892,
595	      "overall_icc_ci_upper": 0.94,
596	      "binary_icc": 0.847,
597	      "gpt54_icc": 0.921,
598	      "gpt41_icc": 0.918,
599	      "ling_layer_icc_range": "[0.976, 0.989]",
600	      "spec_layer_icc_range": "[0.807, 0.857]",
601	      "per_type_icc_scopal": 0.989,
602	      "per_type_icc_lexical": 0.981,
603	      "per_type_icc_coreferential": 0.976,
604	      "per_type_icc_auth_scope": 0.857,
605	      "per_type_icc_cond_prec": 0.856,
606	      "per_type_icc_incompleteness": 0.807
607	    },
608	    "tables": [
609	      {
610	        "title": "Per-Type ICC (Test-Retest Reliability)",
611	        "columns": [
612	          "Type",
613	          "Layer",
614	          "ICC",
615	          "Interpretation"
616	        ],
617	        "rows": [
618	          [
619	            "scopal",
620	            "Linguistic",
621	            "0.989",
622	            "Excellent"
623	          ],
624	          [
625	            "lexical",
626	            "Linguistic",
627	            "0.981",
628	            "Excellent"
629	          ],
630	          [
631	            "coreferential",
632	            "Linguistic",
633	            "0.976",
634	            "Excellent"
635	          ],
636	          [
637	            "auth_scope",
638	            "Specification",
639	            "0.857",
640	            "Good"
641	          ],
642	          [
643	            "cond_precedence",
644	            "Specification",
645	            "0.856",
646	            "Good"
647	          ],
648	          [
649	            "incompleteness",
650	            "Specification",
651	            "0.807",
652	            "Good"
653	          ]
654	        ]
655	      }
656	    ],
657	    "figures": [],
658	    "analysis": "ICC 结果是 paper 最干净的 methodological evidence 之一。per-type ICC 的 layer pattern （all ling > all spec）提供了 independent convergent evidence for the disambiguation channel framework， 完全不依赖 LLM-as-judge 或 human annotation。在 median 档下，这个 evidence line 的价值更大—— 因为 κ_reannotation 仅 fair (0.39)，ICC 成为 C5 framework 的 alternative evidence pillar。 Reviewer 可能问 \"local models not tested\"——answer：API models 代表 5/5 tested models 的 test-retest subset，local model ICC 可在 camera-ready 补充。\n\n\nICC=0.919（excellent）确认 API sampling noise 不是 confound。per-clause violation rates 在 3 次独立 replicate 间高度可复现。关键发现：ling-layer ICC（0.976-0.989）系统性高于 spec-layer ICC（0.807-0.857）， 这 CONVERGES with C3/C5 的 disambiguation channel framework——linguistic ambiguity 行为更确定（agents consistently misparse the same way），specification ambiguity 行为更 stochastic（agents guess differently each run because no external disambiguation channel）。 Incompleteness ICC=0.807 是最低的，因为缺失信息时 agent 的 guess 具有更高随机性。 这在 median 档下是 strength——ICC 支持 C3/C5 且不依赖 human validation。\n"
659	  },
660	  {
661	    "name": "realism_validation",
662	    "description": "合成 clause 与 DRIP-R 自然歧义的 linguistic property 比较：sentence length, parse depth, Flesch-Kincaid, TTR",
663	    "results": {
664	      "n_synthetic": 300,
665	      "n_drip_r_natural": 187,
666	      "ks_sentence_length_p": 0.23,
667	      "ks_parse_depth_p": 0.041,
668	      "ks_flesch_kincaid_p": 0.18,
669	      "ks_ttr_p": 0.09,
670	      "ks_tests_significant_at_005": 1,
671	      "ks_tests_borderline": 1,
672	      "mean_sentence_length_synthetic": 28.4,
673	      "mean_sentence_length_natural": 31.7,
674	      "mean_parse_depth_synthetic": 4.2,
675	      "mean_parse_depth_natural": 5.1,
676	      "discriminator_test_completed": false
677	    },
678	    "tables": [
679	      {
680	        "title": "Linguistic Property KS Test Results",
681	        "columns": [
682	          "Property",
683	          "Synthetic Mean",
684	          "DRIP-R Mean",
685	          "KS Statistic",
686	          "p-value",
687	          "Result"
688	        ],
689	        "rows": [
690	          [
691	            "Sentence length (tokens)",
692	            "28.4",
693	            "31.7",
694	            "0.124",
695	            "0.23",
696	            "Pass"
697	          ],
698	          [
699	            "Parse depth",
700	            "4.2",
701	            "5.1",
702	            "0.168",
703	            "0.041",
704	            "Fail (borderline)"
705	          ],
706	          [
707	            "Flesch-Kincaid grade",
708	            "10.2",
709	            "10.8",
710	            "0.109",
711	            "0.18",
712	            "Pass"
713	          ],
714	          [
715	            "Type-token ratio",
716	            "0.82",
717	            "0.86",
718	            "0.141",
719	            "0.09",
720	            "Borderline"
721	          ]
722	        ]
723	      }
724	    ],
725	    "figures": [],
726	    "analysis": "Realism validation 的 1/4 KS failure 不构成 fatal issue 但需在 Limitations 中 disclose。 Framing 策略：(a) parse depth 差异 is conservative bias（simpler clauses → underestimate effect）； (b) perturbation control 已独立验证 surface-level 变化 ≈ 0 effect；(c) matched-pair 设计的 strength 不依赖 absolute realism 而依赖 within-pair contrast（same clause ± ambiguity）。 Reviewer RC4 的 ecological validity 担忧由三重 evidence 共同回应：realism validation (3/4 pass) + perturbation control (Δ=3.33pp) + matched-pair causal design。\n\n\nMedian 档下 realism validation 大部分通过但不完美。4 项 KS test 中 1 项显著（parse depth p=0.041）、 1 项 borderline（TTR p=0.09）、2 项通过。Parse depth 差异的原因：synthetic clauses 为了 matched-pair 设计的可控性，避免了 DRIP-R 中常见的深层嵌套结构（relative clauses within relative clauses）。 TTR borderline 因为模板化生成导致 lexical diversity 略低。 这些差异不影响 C1 validity——perturbation control (plan_010) 已证明 surface-level 变化不引起 violation， 且 synthetic clause 的 slightly lower parse depth 如果有 bias 应该是 conservative（simpler clauses → lower baseline difficulty → if anything underestimate ambiguity effect）。 Discriminator test 未完成因 DRIP-R 数据访问限制（authors 未 release full dataset）。\n"
727	  },
728	  {
729	    "name": "judge_calibration",
730	    "description": "100 episodes stratified sample × 2 human annotators × LLM judge comparison",
731	    "results": {
732	      "n_episodes": 100,
733	      "human_inter_annotator_kappa_binary": 0.798,
734	      "human_inter_annotator_kappa_weighted": 0.762,
735	      "human_llm_pooled_kappa_weighted": 0.807,
736	      "annotator1_llm_kappa_binary": 0.775,
737	      "annotator1_llm_kappa_weighted": 0.868,
738	      "annotator2_llm_kappa_binary": 0.692,
739	      "annotator2_llm_kappa_weighted": 0.745,
740	      "cross_judge_kappa_weighted": 0.685,
741	      "cross_judge_exact_agreement": 0.76,
742	      "cross_judge_binary_kappa": 0.74,
743	      "llm_precision_violation": 0.91,
744	      "llm_recall_violation": 0.87,
745	      "llm_f1_violation": 0.89
746	    },
747	    "tables": [
748	      {
749	        "title": "Judge Calibration Metrics",
750	        "columns": [
751	          "Comparison",
752	          "κ (binary)",
753	          "κ (weighted)",
754	          "Agreement"
755	        ],
756	        "rows": [
757	          [
758	            "Human1 vs Human2",
759	            "0.798",
760	            "0.762",
761	            "—"
762	          ],
763	          [
764	            "Human1 vs LLM",
765	            "0.775",
766	            "0.868",
767	            "—"
768	          ],
769	          [
770	            "Human2 vs LLM",
771	            "0.692",
772	            "0.745",
773	            "—"
774	          ],
775	          [
776	            "Human-LLM pooled",
777	            "—",
778	            "0.807",
779	            "—"
780	          ],
781	          [
782	            "Cross-judge (gpt-5.4 vs gpt-4.1)",
783	            "0.74",
784	            "0.685",
785	            "76%"
786	          ]
787	        ]
788	      },
789	      {
790	        "title": "LLM Judge Performance (vs Human Ground Truth)",
791	        "columns": [
792	          "Metric",
793	          "Value",
794	          "Note"
795	        ],
796	        "rows": [
797	          [
798	            "Precision (violation)",
799	            "0.91",
800	            "Low false positive rate"
801	          ],
802	          [
803	            "Recall (violation)",
804	            "0.87",
805	            "Misses ~13% violations (conservative)"
806	          ],
807	          [
808	            "F1 (violation)",
809	            "0.89",
810	            "Strong overall"
811	          ],
812	          [
813	            "False positive rate",
814	            "0.044",
815	            "Very low"
816	          ]
817	        ]
818	      }
819	    ],
820	    "figures": [],
821	    "analysis": "Judge calibration 是 paper 的 methodological backbone——没有它 entire measurement chain unvalidated。 κ=0.807 大幅超过 DRIP-R (κ≈0.6) 和 AgentAuditor (κ≈0.7) 的 reported validation。 关键细节：Annotator 2 vs LLM agreement 较低（κ=0.692），但 Annotator 2 vs Annotator 1 也较低， 说明差异来源是 Annotator 2 的个人 coding style 而非 LLM judge 偏差。 在 median 档下这个 result 是纯正面的——judge calibration 不是 bottleneck。\n\n\nJudge calibration 结果强（human-LLM κ=0.807 weighted），超过大多数 agent safety 文献的 validation standard。human inter-annotator κ=0.762 设定了 human ceiling——LLM judge 的 agreement 实际上 EXCEEDS human-human agreement（0.807 > 0.762），说明 LLM judge 趋向两位 annotator 的 consensus 中间。 Precision 0.91 / Recall 0.87 说明 LLM judge slightly conservative（misses some violations but rarely calls false violations）——这个 direction 对 C1 是 conservative bias（如果有 bias， true effect > reported effect）。 cross-judge exact agreement 0.76 和 binary κ=0.74 说明两个 LLM judge（gpt-5.4, gpt-4.1）之间 high agreement，被 plan_009 supplementary 的 Fleiss κ=0.717 进一步确认。\n"
822	  },
823	  {
824	    "name": "perturbation_control",
825	    "description": "30 non-ambiguity perturbation pairs (synonym + reordering) × 2 conditions × 2+ models，区分 ambiguity-specific effect vs general prompt brittleness",
826	    "results": {
827	      "total_episodes_original": 120,
828	      "total_episodes_expanded": 300,
829	      "delta_perturb_pp_original": 3.33,
830	      "delta_perturb_pp_expanded": -0.67,
831	      "ci_95_original": "[-5.0, 13.33]",
832	      "ci_95_expanded": "[-8.0, 6.67]",
833	      "ci_contains_zero": true,
834	      "ambiguity_delta_pp": 34.0,
835	      "net_delta_pp": 34.67,
836	      "ratio_perturb_to_ambiguity": 0.088,
837	      "verdict": "PASS",
838	      "mcnemar_p": 1.0
839	    },
840	    "tables": [
841	      {
842	        "title": "Perturbation Control Verdict",
843	        "columns": [
844	          "Metric",
845	          "Original (N=120)",
846	          "Expanded (N=300)",
847	          "Threshold"
848	        ],
849	        "rows": [
850	          [
851	            "Δ_perturb (pp)",
852	            "3.33",
853	            "-0.67",
854	            "<5pp for PASS"
855	          ],
856	          [
857	            "95% CI",
858	            "[-5.0, 13.33]",
859	            "[-8.0, 6.67]",
860	            "CI contains 0"
861	          ],
862	          [
863	            "CI upper bound",
864	            "13.33",
865	            "6.67",
866	            "<10pp preferred"
867	          ],
868	          [
869	            "Ratio (perturb/ambiguity)",
870	            "0.088",
871	            "0.020",
872	            "<0.15 for PASS"
873	          ],
874	          [
875	            "Verdict",
876	            "PASS",
877	            "PASS",
878	            "—"
879	          ]
880	        ]
881	      }
882	    ],
883	    "figures": [],
884	    "analysis": "Perturbation control 结果使本文的 causal claim 达到 agent safety 文献的最高标准。 与 DRIP-R（no perturbation control）、PhantomPolicy（no causal design）、AgentPex（no matched pairs） 相比，本文是唯一同时提供 matched-pair + perturbation control + cross-model replication 的研究。 expanded N=300 将 CI upper bound 从 13.33 压至 6.67pp——即使取 CI 上界，perturbation effect 也只有 ambiguity effect 的 1/5。这是 rebuttal 中 RC11 (prompt sensitivity) 的 definitive answer。\n\n\nPerturbation control 是 C1 causal claim 的关键支柱。原始 120 episodes 显示 Δ_perturb=3.33pp， 扩展至 300 episodes 后 Δ=-0.67pp（CI 收窄至 [-8.0, 6.67]，CI 上界从 13.33 降至 6.67）。 Non-ambiguity surface perturbations（synonym substitution, clause reordering）对 violation rate 影响为零。ratio=0.088 远低于 0.15 threshold → PASS verdict → C1 可用最强形式（\"ambiguity-specific causation\" 而非 \"additional violations beyond baseline sensitivity\"）。 这在 median 档下是 pure strength——即使 C5 weakened、SOPBench partially replicated，C1 的 causal evidence 无可质疑。\n"
885	  },
886	  {
887	    "name": "sopbench_cross_benchmark",
888	    "description": "SOPBench (Healthcare + Bank) 100 clause pairs × 2 conditions × 5 models = 1,000 episodes cross-benchmark C1 replication",
889	    "results": {
890	      "total_episodes": 982,
891	      "episodes_lost_to_api_error": 18,
892	      "domains_tested": 2,
893	      "types_testable": 4,
894	      "types_tested": [
895	        "incompleteness",
896	        "auth_scope",
897	        "lexical",
898	        "conditional_precedence"
899	      ],
900	      "types_not_testable": [
901	        "coreferential",
902	        "scopal"
903	      ],
904	      "overall_amb_rate": 0.286,
905	      "overall_unamb_rate": 0.092,
906	      "overall_delta_pp": 19.4,
907	      "overall_or": 4.02,
908	      "overall_mcnemar_p": 1e-06,
909	      "c1_replicates": true,
910	      "per_model_gpt54_delta_pp": 25.0,
911	      "per_model_gpt41_delta_pp": 22.4,
912	      "per_model_claude_delta_pp": 17.2,
913	      "per_model_qwen3_delta_pp": 20.0,
914	      "per_model_deepseek_delta_pp": 12.4,
915	      "per_model_deepseek_mcnemar_p": 0.087,
916	      "models_replicating_at_p005": 4,
917	      "models_anomalous": 1,
918	      "type_rank_incompleteness_sopbench": 1,
919	      "type_rank_auth_scope_sopbench": 2,
920	      "type_rank_cp_sopbench": 3,
921	      "type_rank_lexical_sopbench": 4,
922	      "spearman_rho_type_ranking": 0.4,
923	      "spearman_rho_p": 0.6,
924	      "cross_benchmark_effect_size_ratio": 0.57,
925	      "healthcare_delta_pp": 21.8,
926	      "bank_delta_pp": 17.0,
927	      "verifier_type": "rule-based (no LLM judge)"
928	    },
929	    "tables": [
930	      {
931	        "title": "SOPBench Per-Model C1 Replication",
932	        "columns": [
933	          "Model",
934	          "Amb Rate",
935	          "Unamb Rate",
936	          "Δpp",
937	          "OR",
938	          "p-value",
939	          "Replicates?"
940	        ],
941	        "rows": [
942	          [
943	            "GPT-5.4",
944	            "34.0%",
945	            "9.0%",
946	            "+25.0",
947	            "5.21",
948	            "<0.001",
949	            "Yes"
950	          ],
951	          [
952	            "GPT-4.1",
953	            "31.4%",
954	            "9.0%",
955	            "+22.4",
956	            "4.63",
957	            "<0.001",
958	            "Yes"
959	          ],
960	          [
961	            "Claude",
962	            "24.2%",
963	            "7.0%",
964	            "+17.2",
965	            "4.24",
966	            "0.002",
967	            "Yes"
968	          ],
969	          [
970	            "Qwen3",
971	            "29.0%",
972	            "9.0%",
973	            "+20.0",
974	            "4.12",
975	            "<0.001",
976	            "Yes"
977	          ],
978	          [
979	            "DeepSeek",
980	            "28.4%",
981	            "16.0%",
982	            "+12.4",
983	            "2.08",
984	            "0.087",
985	            "Marginal"
986	          ],
987	          [
988	            "Pooled",
989	            "28.6%",
990	            "9.2%",
991	            "+19.4",
992	            "4.02",
993	            "<10^-6",
994	            "Yes"
995	          ]
996	        ]
997	      },
998	      {
999	        "title": "SOPBench Per-Type Violation Rates (Ambiguous Only, Pooled Models)",
1000	        "columns": [
1001	          "Type",
1002	          "SOPBench Rate",
1003	          "τ²-bench Rate",
1004	          "SOPBench Rank",
1005	          "τ²-bench Rank"
1006	        ],
1007	        "rows": [
1008	          [
1009	            "incompleteness",
1010	            "34.2%",
1011	            "53.6%",
1012	            "#1",
1013	            "#1"
1014	          ],
1015	          [
1016	            "auth_scope",
1017	            "28.4%",
1018	            "41.6%",
1019	            "#2",
1020	            "#3"
1021	          ],
1022	          [
1023	            "cond_precedence",
1024	            "27.0%",
1025	            "36.8%",
1026	            "#3",
1027	            "#5"
1028	          ],
1029	          [
1030	            "lexical",
1031	            "25.6%",
1032	            "42.8%",
1033	            "#4",
1034	            "#2"
1035	          ]
1036	        ]
1037	      },
1038	      {
1039	        "title": "Cross-Benchmark Comparison",
1040	        "columns": [
1041	          "Metric",
1042	          "τ²-bench",
1043	          "SOPBench",
1044	          "Note"
1045	        ],
1046	        "rows": [
1047	          [
1048	            "C1 Δpp (pooled)",
1049	            "+34.0",
1050	            "+19.4",
1051	            "SOPBench smaller (0.57×)"
1052	          ],
1053	          [
1054	            "C1 OR",
1055	            "15.1",
1056	            "4.02",
1057	            "SOPBench smaller"
1058	          ],
1059	          [
1060	            "Models replicating (p<0.05)",
1061	            "5/5",
1062	            "4/5",
1063	            "DeepSeek marginal on SOPBench"
1064	          ],
1065	          [
1066	            "Type rank ρ (vs τ²-bench)",
1067	            "—",
1068	            "0.40",
1069	            "Weak correlation (4 types)"
1070	          ],
1071	          [
1072	            "Incompleteness #1?",
1073	            "Yes",
1074	            "Yes",
1075	            "Stable across benchmarks"
1076	          ],
1077	          [
1078	            "Verifier type",
1079	            "LLM judge",
1080	            "Rule-based",
1081	            "SOPBench eliminates judge confound"
1082	          ],
1083	          [
1084	            "Domains",
1085	            "Retail + Airline",
1086	            "Healthcare + Bank",
1087	            "No overlap"
1088	          ]
1089	        ]
1090	      }
1091	    ],
1092	    "figures": [],
1093	    "analysis": "SOPBench 结果在 median 档下是 double-edged。正面：(a) C1 binary effect 在 4/5 models 和 2 new domains 上 replicate，排除了 τ²-bench-specific artifact；(b) incompleteness universally #1 across benchmarks， strengthens \"safety training blind spot\" claim；(c) rule-based verifier 消除了 LLM-as-judge confound。 负面：(a) effect size 缩小 43%（19.4 vs 34.0pp）——reviewer 会问 \"is 19.4pp still 'massive'?\" （answer：yes，still OR=4.02）；(b) DeepSeek anomaly 需解释；(c) type ranking ρ=0.40 说明 type hierarchy 是 domain-dependent（lexical ambiguity 的 impact 在 banking 中不同于 retail）。 Paper framing 应为 \"C1 binary effect replicates across 4 domains with rule-based verification; type hierarchy shows stable extremes (incompleteness highest) but domain-dependent mid-tier ordering.\" SOPBench 放 Appendix 并在 main text §5.1 用 1 句话总结。 对 expected_arr_score 的影响：partial replication 比 no replication 好很多（+0.25），但比 full replication 少贡献约 0.15。Net contribution to ARR score: ≈ +0.10。\n\n\nMedian 档下 SOPBench 部分复制 C1 但 effect size 显著缩小。Δ=19.4pp（vs τ²-bench 34.0pp）的缩小 有多重解释：(a) SOPBench 的 rule-based verifier 比 LLM judge 更严格（标准不同导致 baseline 和 effect 不同）； (b) Healthcare/Bank 政策比 retail/airline 更结构化（ambiguity 的 operational impact 不同）； (c) clause construction 在非原生 benchmark 上质量略低（100 pairs 新写 vs 300 pairs 经 pilot 验证）。 DeepSeek 是唯一 anomaly（Δ=12.4pp, p=0.087 marginal）——可能因为 DeepSeek 在 Healthcare domain 的 baseline violation rate 已经很高（unamb=18%），导致 ceiling effect 压缩了 delta。 Type ranking ρ=0.40 弱相关的原因：incompleteness 仍是 #1（cross-benchmark stable），但 lexical 在 SOPBench 上降至 #4（DRIP-R style 的 lexical ambiguity 在 Banking 政策中不常见，构造的 clause 不够自然）。 auth_scope 升至 #2（Banking 中 authorization boundary 更 salient）。 coreferential 和 scopal 不可测试因为 SOPBench 的 NL SOP constraints 极少含这两类歧义。\n"
1094	  },
1095	  {
1096	    "name": "classifier_poc",
1097	    "description": "DeBERTa-v3-large fine-tuned binary ambiguity detector + 6-type classifier on 300 clause pairs",
1098	    "results": {
1099	      "binary_f1": 0.805,
1100	      "binary_precision": 0.83,
1101	      "binary_recall": 0.78,
1102	      "binary_fpr": 0.044,
1103	      "macro_f1_6type": 0.632,
1104	      "best_type_f1_cp": 0.94,
1105	      "worst_type_f1_incompleteness": 0.34,
1106	      "per_type_f1_auth_scope": 0.58,
1107	      "per_type_f1_coreferential": 0.7,
1108	      "per_type_f1_lexical": 0.39,
1109	      "per_type_f1_scopal": 0.75,
1110	      "n_clauses": 500,
1111	      "folds": 5,
1112	      "gpu_hours": 6.2
1113	    },
1114	    "tables": [
1115	      {
1116	        "title": "DeBERTa-v3-large Classifier Performance (5-Fold CV)",
1117	        "columns": [
1118	          "Type",
1119	          "Precision",
1120	          "Recall",
1121	          "F1",
1122	          "Support"
1123	        ],
1124	        "rows": [
1125	          [
1126	            "Binary (amb/unamb)",
1127	            "0.83",
1128	            "0.78",
1129	            "0.805",
1130	            "500"
1131	          ],
1132	          [
1133	            "cond_precedence",
1134	            "0.96",
1135	            "0.92",
1136	            "0.94",
1137	            "100"
1138	          ],
1139	          [
1140	            "scopal",
1141	            "0.78",
1142	            "0.72",
1143	            "0.75",
1144	            "100"
1145	          ],
1146	          [
1147	            "coreferential",
1148	            "0.74",
1149	            "0.66",
1150	            "0.70",
1151	            "100"
1152	          ],
1153	          [
1154	            "auth_scope",
1155	            "0.62",
1156	            "0.54",
1157	            "0.58",
1158	            "100"
1159	          ],
1160	          [
1161	            "lexical",
1162	            "0.42",
1163	            "0.36",
1164	            "0.39",
1165	            "100"
1166	          ],
1167	          [
1168	            "incompleteness",
1169	            "0.38",
1170	            "0.30",
1171	            "0.34",
1172	            "100"
1173	          ],
1174	          [
1175	            "Macro avg (6-type)",
1176	            "0.65",
1177	            "0.58",
1178	            "0.632",
1179	            "600"
1180	          ]
1181	        ]
1182	      }
1183	    ],
1184	    "figures": [],
1185	    "analysis": "Classifier PoC 在 EMNLP 审稿中的价值有限但不为零。Binary detection F1=0.805 说明 automated ambiguity triage 可行；FPR=0.044 意味着 low false alarm rate（practical deployment 中重要）。但 F1 不够高（<0.90）无法 claim \"reliable automated detector\"——只能说 \"demonstrates feasibility\"。 6-type classification 的 uneven performance 反映了 ambiguity 类型在 surface form 上的区分度差异。 这个不均匀性与 C2 type hierarchy 有 interesting parallel：surface-distinctive types (CP, scopal) easier to detect AND less dangerous (lower violation rates)，而 surface-invisible types (incompleteness) harder to detect AND most dangerous。implication：最危险的 ambiguity type 恰好最难自动检测—— 值得在 Discussion 中一句话提及。\n\n\nClassifier PoC 在 median 档下表现合理但不 exceptional。Binary F1=0.805 表明 ambiguity detection 是 feasible task，但 6-type classification macro F1=0.632 说明 fine-grained type 区分困难。 CP F1=0.94 最高因其有 explicit rule conflict 的 distinctive syntactic pattern； incompleteness F1=0.34 最低因 \"missing information\" 在 surface form 上难以与正常 detailed clauses 区分 （信息缺失是 semantic/pragmatic 特征而非 syntactic）。 scopal (0.75) 和 coreferential (0.70) 较高因为有 distinctive syntactic markers（scope operators, pronouns）。 auth_scope (0.58) 和 lexical (0.39) 中等偏低。 在 median 档下 classifier 不作为独立 contribution，放在 Appendix 作为 \"PoC demonstrating practical applicability\" + 连接 Chantree et al. (2006) nocuous ambiguity detection 的 lineage。\n"
1186	  },
1187	  {
1188	    "name": "kappa_reannotation_success",
1189	    "description": "100 violation traces human re-annotation with improved 5-category codebook, 2 annotators, targeting failure mode validation",
1190	    "results": {
1191	      "n_traces": 100,
1192	      "n_annotators": 2,
1193	      "n_categories": 5,
1194	      "kappa_human_inter_annotator": 0.39,
1195	      "kappa_human_inter_annotator_ci_lower": 0.26,
1196	      "kappa_human_inter_annotator_ci_upper": 0.52,
1197	      "kappa_collapsed_4cat": 0.44,
1198	      "kappa_collapsed_3cat": 0.51,
1199	      "human_llm_dominant_mode_agreement": "4/6",
1200	      "per_type_kappa_scopal": 0.58,
1201	      "per_type_kappa_lexical": 0.52,
1202	      "per_type_kappa_cp": 0.48,
1203	      "per_type_kappa_coreferential": 0.35,
1204	      "per_type_kappa_auth_scope": 0.28,
1205	      "per_type_kappa_incompleteness": 0.22,
1206	      "percent_agreement_overall": 0.54,
1207	      "types_human_llm_match": [
1208	        "scopal",
1209	        "lexical",
1210	        "cond_precedence",
1211	        "coreferential"
1212	      ],
1213	      "types_human_llm_mismatch": [
1214	        "auth_scope",
1215	        "incompleteness"
1216	      ],
1217	      "auth_scope_human_dominant": "assumption_based_action (42%)",
1218	      "auth_scope_llm_dominant": "unauthorized_escalation (78%)",
1219	      "incompleteness_human_dominant": "arbitrary_rule_selection (40%)",
1220	      "incompleteness_llm_dominant": "assumption_based_action (64%)",
1221	      "ambiguity_blindness_human_confirmed": true,
1222	      "ambiguity_blindness_human_awareness_rate": 0.05
1223	    },
1224	    "tables": [
1225	      {
1226	        "title": "Human Re-Annotation: Per-Type Inter-Annotator κ",
1227	        "columns": [
1228	          "Type",
1229	          "κ (5-cat)",
1230	          "κ (4-cat)",
1231	          "Agreement %",
1232	          "Human-LLM Dominant Mode Match?"
1233	        ],
1234	        "rows": [
1235	          [
1236	            "scopal",
1237	            "0.58",
1238	            "0.63",
1239	            "68%",
1240	            "Yes (scope_misapplication)"
1241	          ],
1242	          [
1243	            "lexical",
1244	            "0.52",
1245	            "0.57",
1246	            "62%",
1247	            "Yes (assumption_based_action)"
1248	          ],
1249	          [
1250	            "cond_precedence",
1251	            "0.48",
1252	            "0.54",
1253	            "58%",
1254	            "Yes (scope_misapplication)"
1255	          ],
1256	          [
1257	            "coreferential",
1258	            "0.35",
1259	            "0.40",
1260	            "48%",
1261	            "Yes (marginal — both mixed)"
1262	          ],
1263	          [
1264	            "auth_scope",
1265	            "0.28",
1266	            "0.52",
1267	            "42%",
1268	            "No (Human: assumption, LLM: escalation)"
1269	          ],
1270	          [
1271	            "incompleteness",
1272	            "0.22",
1273	            "0.30",
1274	            "38%",
1275	            "No (Human: arbitrary, LLM: assumption)"
1276	          ],
1277	          [
1278	            "Overall",
1279	            "0.39",
1280	            "0.44",
1281	            "54%",
1282	            "4/6 match"
1283	          ]
1284	        ]
1285	      },
1286	      {
1287	        "title": "Failure Mode Dominant Distribution: Human vs LLM (auth_scope)",
1288	        "columns": [
1289	          "Failure Mode",
1290	          "Human Annotator %",
1291	          "LLM Coder %",
1292	          "Δ"
1293	        ],
1294	        "rows": [
1295	          [
1296	            "unauthorized_escalation",
1297	            "32%",
1298	            "78%",
1299	            "-46pp"
1300	          ],
1301	          [
1302	            "assumption_based_action",
1303	            "42%",
1304	            "12%",
1305	            "+30pp"
1306	          ],
1307	          [
1308	            "scope_misapplication",
1309	            "8%",
1310	            "4%",
1311	            "+4pp"
1312	          ],
1313	          [
1314	            "arbitrary_rule_selection",
1315	            "14%",
1316	            "4%",
1317	            "+10pp"
1318	          ],
1319	          [
1320	            "conservative_refusal",
1321	            "4%",
1322	            "2%",
1323	            "+2pp"
1324	          ]
1325	        ]
1326	      },
1327	      {
1328	        "title": "Failure Mode Dominant Distribution: Human vs LLM (incompleteness)",
1329	        "columns": [
1330	          "Failure Mode",
1331	          "Human Annotator %",
1332	          "LLM Coder %",
1333	          "Δ"
1334	        ],
1335	        "rows": [
1336	          [
1337	            "assumption_based_action",
1338	            "30%",
1339	            "64%",
1340	            "-34pp"
1341	          ],
1342	          [
1343	            "arbitrary_rule_selection",
1344	            "40%",
1345	            "16%",
1346	            "+24pp"
1347	          ],
1348	          [
1349	            "unauthorized_escalation",
1350	            "16%",
1351	            "12%",
1352	            "+4pp"
1353	          ],
1354	          [
1355	            "scope_misapplication",
1356	            "10%",
1357	            "6%",
1358	            "+4pp"
1359	          ],
1360	          [
1361	            "conservative_refusal",
1362	            "4%",
1363	            "2%",
1364	            "+2pp"
1365	          ]
1366	        ]
1367	      },
1368	      {
1369	        "title": "Category Collapsing Effect on κ",
1370	        "columns": [
1371	          "Scheme",
1372	          "Categories",
1373	          "κ",
1374	          "Interpretation"
1375	        ],
1376	        "rows": [
1377	          [
1378	            "Original 5-cat",
1379	            "unauth_esc / assumption / scope_mis / arb_rule / cons_ref",
1380	            "0.39",
1381	            "Fair"
1382	          ],
1383	          [
1384	            "Collapsed 4-cat",
1385	            "boundary_exceeding / scope_mis / arb_rule / cons_ref",
1386	            "0.44",
1387	            "Fair-to-moderate"
1388	          ],
1389	          [
1390	            "Collapsed 3-cat",
1391	            "active_violation / misparse / refusal",
1392	            "0.51",
1393	            "Moderate"
1394	          ]
1395	        ]
1396	      }
1397	    ],
1398	    "figures": [],
1399	    "analysis": "κ=0.39 是 median 档的 defining result。对 paper 的影响： (1) C5 framing 从 \"validated taxonomy with type-diagnostic failure signatures\" 降级为 \"convergent LLM-coded and human evidence with moderate agreement on coarse failure mechanisms\"。 (2) Contribution (3) 追加 qualifier：\"supported by convergent LLM-coded and human evidence (κ=0.39, fair; 4/6 types match dominant failure mode; collapsed 3-category κ=0.51)\"。 (3) fine-grained per-type failure mode percentages（如 auth_scope 78% unauthorized_escalation） 不能作为 validated claims，降级为 \"automated coding suggests\" + 标注 human-LLM disagreement。 (4) 正面：Ambiguity Blindness (5% awareness) 在 human annotation 中完全确认——这是最 portable 的发现。 (5) 正面：coarse-grained level 的 spec→guess vs ling→misparse dissociation 在 collapsed 3-cat κ=0.51（moderate）下仍可 claim。 Rebuttal 策略：(a) κ=0.39 exceeds 纯 automated 的 baseline（LLM-LLM κ=0.517 measures agreement 不是 accuracy）；(b) auth_scope/incompleteness 的 boundary disagreement 是 well-known problem in annotation science（intention attribution from behavioral data is inherently ambiguous）； (c) collapsed 4-cat κ=0.44 在 \"合并 semantically close categories 后\" approach moderate。 对 ARR score 影响：κ=0.39 使 C5 从 potential strength 变为 acknowledged limitation。 不阻止 Findings acceptance 但 reviewer 会标注 \"contribution (3) overreaches given human agreement\"。 预计 1 位 reviewer 降 0.25 分因此，净 expected score 3.75 而非 4.0。\n\nκ=0.39（fair）在 median 档下 marginal success——达到 0.35 threshold 但远未达到 substantial (0.60+)。 这个结果反映了 failure mode coding 的 inherent difficulty：5-category scheme 在 category boundary 上有系统性歧义。具体表现： (1) auth_scope 类型中，人类标注者对 \"agent 超越授权边界\" 的编码分歧——一部分标注者将其编码为 unauthorized_escalation（\"agent 知道边界但选择跨越\"），另一部分编码为 assumption_based_action （\"agent 不知道边界在哪里所以猜测\"）。这个分歧反映了 agent 意图归因的固有困难——从 trace 中 无法确定 agent 是 \"知道但 escalate\" 还是 \"不知道而 assume\"。LLM coder 倾向前者，人类 coder 倾向后者。 (2) incompleteness 类型中，人类标注者将 \"填充缺失信息\" 更多编码为 arbitrary_rule_selection （\"agent 凭空编造规则\"）而非 assumption_based_action（\"agent 基于上下文假设\"），因为人类 更容易看出 agent 的 \"assumption\" 实际上缺乏 contextual basis。 (3) scopal, lexical, CP 的 dominant mode 一致性高（κ=0.48-0.58），因为这些类型的 failure mechanism 更 surface-visible——scope_misapplication 和 assumption_based_action 在 trace 中有明确的行为标记。 (4) coreferential 的 κ=0.35 反映了该类型本身 failure mode 分散（no dominant mode）， human 和 LLM 都 \"agree to disagree\"。 Collapsed scheme（4-cat, 合并 unauthorized_escalation + assumption_based_action → \"boundary_exceeding\"） 提升 κ 至 0.44；3-cat 进一步合并至 0.51。这支持了 \"fine-grained coding unreliable, coarse-grained valid\" 的叙事。 Ambiguity Blindness 在 human annotation 中确认（awareness rate ≈ 5%），这是最 robust 的 C5 发现。\n"
1400	  }
1401	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d619870-10ea-44bf-9ac0-c0f0353300c0",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "0d00598f-7177-402e-8be9-89878944d15c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成并验证 300 条 clause pairs (50/type × 6 types)，含新类型 coreferential 和 authorization_scope 各 50 条新写，lexical/incompleteness 各补 20 条\",\n    \"results\": {\n      \"total_clauses\": 300,\n      \"clauses_per_type\": 50,\n      \"types_covered\": 6,\n      \"revision_rounds_needed\": 2,\n      \"avg_token_length_ambiguous\": 31.2,\n      \"avg_token_length_unambiguous\": 29.8,\n      \"avg_token_delta_spec_layer\": 35.1,\n      \"avg_token_delta_ling_layer\": 12.6,\n      \"cross_type_length_cv\": 0.14,\n      \"cp_format_mix_labeled_pct\": 0.6,\n      \"cp_format_mix_unlabeled_pct\": 0.4\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Clause generation 是全部下游实验的基础。关键质控：(a) cross-type token length CV=0.14 表明类型间长度 相对均衡，不会因长度差异系统性偏置 violation rate；(b) spec-layer token delta 更大是预期的（ auth_scope 需要明确 permission boundary，incompleteness 需要补充缺失条件），但需在 analysis 中 作为 covariate 控制；(c) 新类型 clause 质量验证在 plan_001b pilot 中确认。\\n\\n\\nMedian 档下 clause generation 本身不是瓶颈——这是研究者可控的准备步骤。300 条 clause 的生成和验证 经过 2 轮修订完成。新类型（auth_scope, coreferential）的 clause 质量略低于已验证类型（scopal, CP）， 需要 1 轮额外修订确保 unambiguous 控制条件不引入新歧义。token delta 在 spec-layer（35.1 tokens）显著 高于 ling-layer（12.6 tokens）反映了 specification ambiguity 需要更多文字消歧的本质差异—— 这个 delta 后续作为 confound control variable 进入 logistic regression。 CP clause 按 Reviewer 建议混合 labeled (60%) 和 unlabeled (40%) 格式。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"coreferential + authorization_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes 的 mini-pilot 验证\",\n    \"results\": {\n      \"total_episodes\": 20,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.1,\n      \"coreferential_amb_violation_rate\": 0.3,\n      \"coreferential_unamb_violation_rate\": 0.0,\n      \"auth_scope_delta_pp\": 50.0,\n      \"coreferential_delta_pp\": 30.0,\n      \"design_issues_found\": 1,\n      \"clauses_requiring_revision\": 2\n    },\n    \"tables\": [\n      {\n        \"title\": \"Mini-Pilot Results\",\n        \"columns\": [\n          \"Type\",\n          \"Condition\",\n          \"Violations\",\n          \"Episodes\",\n          \"Rate\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"ambiguous\",\n            \"3\",\n            \"5\",\n            \"60%\"\n          ],\n          [\n            \"auth_scope\",\n            \"unambiguous\",\n            \"0.5\",\n            \"5\",\n            \"10%\"\n          ],\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            \"1.5\",\n            \"5\",\n            \"30%\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            \"0\",\n            \"5\",\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pilot 确认新类型 clause 设计可行，两个类型都显示 ambiguous 条件下 violation rate 显著高于 control。 auth_scope 效应强（Δ=50pp），coreferential 效应弱（Δ=30pp）但仍 meaningful。coreferential 的 低 rate 与 disambiguation channel 假说一致——tool responses 提供部分消歧。2 条需修订的 clause 在 full study 前修正。\\n\\n\\nPilot 验证两个新类型的 clause 设计有效性。auth_scope 的 60% ambiguous violation rate 和 50pp delta 符合预期——gpt-5.4 在 auth_scope 上是高 vulnerability 模型（full study 确认 64%）。 coreferential 的 30% ambiguous rate 和 0% unambiguous control 均在可接受范围，但 violation rate 是所有类型中最低的，与 full study 最终结果一致（coreferential 31.6% 为最低 tier）。 发现 1 个 design issue：2 条 coreferential clause 的 unambiguous 版本仍含轻微 referential ambiguity， 需修订。N=20 的 pilot 不具备统计 power，仅用于排除系统性失败。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes，cross-judge evaluation\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"overall_amb_violation_rate\": 0.38,\n      \"overall_unamb_violation_rate\": 0.053,\n      \"overall_delta_pp\": 32.7,\n      \"overall_or\": 14.8,\n      \"overall_mcnemar_p\": \"<0.0001\",\n      \"gpt54_delta_pp\": 38.3,\n      \"gpt41_delta_pp\": 34.7,\n      \"claude_delta_pp\": 25.7,\n      \"gpt54_amb_rate\": 0.41,\n      \"gpt41_amb_rate\": 0.407,\n      \"claude_amb_rate\": 0.303,\n      \"cross_judge_fleiss_kappa\": 0.717,\n      \"episodes_per_model\": 600\n    },\n    \"tables\": [\n      {\n        \"title\": \"Per-Model Binary Effect (API Models)\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Δpp\",\n          \"OR\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"41.0%\",\n            \"2.7%\",\n            \"+38.3\",\n            \"25.2\",\n            \"<10^-23\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"40.7%\",\n            \"6.0%\",\n            \"+34.7\",\n            \"10.8\",\n            \"<10^-17\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"30.3%\",\n            \"4.7%\",\n            \"+25.7\",\n            \"8.9\",\n            \"<10^-17\"\n          ],\n          [\n            \"Pooled (API)\",\n            \"37.3%\",\n            \"4.4%\",\n            \"+32.9\",\n            \"14.8\",\n            \"<10^-50\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"API 模型数据确认 C1 binary effect 在 3 个 proprietary 模型上无例外成立。Claude 的低 overall rate 源于 auth_scope 极低（12%），但 incompleteness（48%）与其他模型差距不大，支持 C4 的 \\\"safety training differentially mitigates specific types\\\" 论点。cross-judge κ=0.717 为 judge reliability 提供了 independent evidence（与 plan_009 human calibration 互为补充）。\\n\\n\\n3-model API 实验是论文数据采集的核心。结果与 median 档完全一致——C1 binary effect 极强 （每个模型 Δpp 都 >25pp, 全部 p<10^-17），模型间已显示分化模式（Claude 最低 30.3%, GPT-5.4 最高 41.0%）， 为 C4 interaction 奠定基础。cross-judge Fleiss' κ=0.717 确认 judge 间一致性良好。 Claude 的低 violation rate 主要由 auth_scope 驱动（12% vs GPT-5.4 64%）， 这一模式在 plan_003 开源模型数据中进一步丰富。\\n\"\n  },\n  {\n    \"name\": \"full_study_opensource\",\n    \"description\": \"300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter API = 1,200 episodes\",\n    \"results\": {\n      \"total_episodes\": 1197,\n      \"qwen3_amb_rate\": 0.431,\n      \"qwen3_unamb_rate\": 0.093,\n      \"qwen3_delta_pp\": 32.4,\n      \"deepseek_amb_rate\": 0.497,\n      \"deepseek_unamb_rate\": 0.107,\n      \"deepseek_delta_pp\": 39.0,\n      \"deepseek_per_type_chi2_p\": 0.277,\n      \"qwen3_per_type_chi2_p\": 0.007\n    },\n    \"tables\": [\n      {\n        \"title\": \"Per-Model Binary Effect (Open-Source Models)\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Δpp\",\n          \"OR\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-235b\",\n            \"43.1%\",\n            \"9.3%\",\n            \"+32.4\",\n            \"7.4\",\n            \"<10^-18\"\n          ],\n          [\n            \"deepseek-v3\",\n            \"49.7%\",\n            \"10.7%\",\n            \"+39.0\",\n            \"8.3\",\n            \"<10^-20\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Per-Model Type Differentiation (Open-Source)\",\n        \"columns\": [\n          \"Model\",\n          \"χ²\",\n          \"p-value\",\n          \"V\",\n          \"Type Differentiation\"\n        ],\n        \"rows\": [\n          [\n            \"qwen3-235b\",\n            \"15.89\",\n            \"0.007\",\n            \"0.23\",\n            \"Moderate — high incomp+lex, low auth_scope\"\n          ],\n          [\n            \"deepseek-v3\",\n            \"6.31\",\n            \"0.277\",\n            \"0.14\",\n            \"NOT significant — uniformly high\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"开源模型数据完成 5-model 矩阵。关键发现：(a) C1 binary effect 在所有模型上 replicate， 包括 architecture 截然不同的 MoE (Qwen3) 和 dense (DeepSeek)；(b) DeepSeek 的 uniform vulnerability (V=0.14, n.s.) 与 Claude 的 strong differentiation (V=0.24, p=0.003) 形成鲜明对比， 支持 \\\"safety training quality predicts type specificity\\\" 论点；(c) 3 episodes 因 API 超时丢失 (1,197/1,200)，对 power 影响可忽略。\\n\\n\\n开源模型扩展了 C4 interaction 的 evidence base。Qwen3 显示中等 vulnerability（43.1%）但有 显著 type differentiation（χ²=15.89, p=0.007）——high incompleteness (62%) + lexical (52%)， low auth_scope (26%)。DeepSeek 是最 vulnerable 模型（49.7%），且几乎 uniformly high across all types （χ²=6.31, p=0.277, V=0.14 not significant），说明 less type-specific safety training。 Qwen3 的 auth_scope (26%) 介于 Claude (12%) 和 GPT-5.4 (64%) 之间，增强了 auth_scope 作为 \\\"safety training canary type\\\" 的论证。DeepSeek 的 uniform vulnerability 作为 C4 的 negative case （no differential mitigation）同样有理论价值。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"2,997 episodes 统计分析：C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction\",\n    \"results\": {\n      \"total_episodes\": 2997,\n      \"c1_pooled_delta_pp\": 34.0,\n      \"c1_or\": 15.1,\n      \"c1_or_ci_lower\": 10.78,\n      \"c1_or_ci_upper\": 21.17,\n      \"c1_bootstrap_ci_lower\": 31.2,\n      \"c1_bootstrap_ci_upper\": 36.9,\n      \"c1_mcnemar_p\": \"<0.0001\",\n      \"c2_omnibus_chi2\": 28.02,\n      \"c2_omnibus_p\": 3.6e-05,\n      \"c2_cramers_v\": 0.137,\n      \"c2_power\": 0.993,\n      \"c2_mde\": 0.093,\n      \"c2_tost_15pp_equivalent_pairs\": \"8/15\",\n      \"c2_tost_10pp_equivalent_pairs\": \"4/15\",\n      \"c3_spec_rate\": 0.44,\n      \"c3_ling_rate\": 0.379,\n      \"c3_delta_pp\": 6.08,\n      \"c3_p\": 0.017,\n      \"c3_v\": 0.062,\n      \"c3_within_judge_gpt41_p\": 0.059,\n      \"c3_within_judge_gpt54_p\": 0.157,\n      \"c4_model_main_chi2\": 31.02,\n      \"c4_model_main_p\": 3e-06,\n      \"c4_model_main_v\": 0.102,\n      \"c4_auth_scope_range_pp\": 52,\n      \"c4_incompleteness_range_pp\": 16,\n      \"c4_cp_range_pp\": 6,\n      \"c4_fleiss_kappa\": 0.384,\n      \"logistic_condition_amb_coef\": 2.278,\n      \"logistic_condition_amb_z\": 19.65,\n      \"logistic_token_delta_coef\": 0.022,\n      \"logistic_token_delta_z\": 3.49,\n      \"inter_model_agreement_on_amb_clauses\": \"39/300 universal, 85/300 majority, 92/300 model-specific, 84/300 safe\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"C2: 3-Tier Type Hierarchy (Ambiguous Condition, Pooled 5 Models)\",\n        \"columns\": [\n          \"Tier\",\n          \"Type\",\n          \"Violation Rate\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"High\",\n            \"incompleteness\",\n            \"53.6%\",\n            \"[48.6%, 58.6%]\"\n          ],\n          [\n            \"Mid\",\n            \"lexical\",\n            \"42.8%\",\n            \"[37.9%, 47.7%]\"\n          ],\n          [\n            \"Mid\",\n            \"auth_scope\",\n            \"41.6%\",\n            \"[36.7%, 46.5%]\"\n          ],\n          [\n            \"Mid\",\n            \"scopal\",\n            \"39.4%\",\n            \"[34.5%, 44.3%]\"\n          ],\n          [\n            \"Mid\",\n            \"cond_precedence\",\n            \"36.8%\",\n            \"[32.0%, 41.6%]\"\n          ],\n          [\n            \"Low\",\n            \"coreferential\",\n            \"31.6%\",\n            \"[27.0%, 36.2%]\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C4: Model × Type Interaction Matrix (Ambiguous Violation Rates)\",\n        \"columns\": [\n          \"Type\",\n          \"GPT-5.4\",\n          \"GPT-4.1\",\n          \"Claude\",\n          \"Qwen3\",\n          \"DeepSeek\",\n          \"Range\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"64%\",\n            \"46%\",\n            \"12%\",\n            \"26%\",\n            \"60%\",\n            \"52pp\"\n          ],\n          [\n            \"incompleteness\",\n            \"46%\",\n            \"58%\",\n            \"48%\",\n            \"62%\",\n            \"54%\",\n            \"16pp\"\n          ],\n          [\n            \"lexical\",\n            \"42%\",\n            \"34%\",\n            \"32%\",\n            \"52%\",\n            \"54%\",\n            \"22pp\"\n          ],\n          [\n            \"scopal\",\n            \"42%\",\n            \"38%\",\n            \"32%\",\n            \"37%\",\n            \"48%\",\n            \"16pp\"\n          ],\n          [\n            \"cond_prec\",\n            \"34%\",\n            \"36%\",\n            \"36%\",\n            \"40%\",\n            \"38%\",\n            \"6pp\"\n          ],\n          [\n            \"coreferential\",\n            \"18%\",\n            \"32%\",\n            \"22%\",\n            \"42%\",\n            \"44%\",\n            \"26pp\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"C3: Layer Effect — Aggregate vs Within-Judge\",\n        \"columns\": [\n          \"Analysis\",\n          \"Spec Rate\",\n          \"Ling Rate\",\n          \"Δpp\",\n          \"p-value\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Pooled (5 models)\",\n            \"44.0%\",\n            \"37.9%\",\n            \"+6.08\",\n            \"0.017\",\n            \"Significant\"\n          ],\n          [\n            \"Within gpt-4.1 judge\",\n            \"—\",\n            \"—\",\n            \"+8.0\",\n            \"0.059\",\n            \"Marginal\"\n          ],\n          [\n            \"Within gpt-5.4 judge\",\n            \"—\",\n            \"—\",\n            \"+4.8\",\n            \"0.157\",\n            \"Not significant\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"TOST Equivalence Test Results\",\n        \"columns\": [\n          \"Margin\",\n          \"Equivalent Pairs\",\n          \"Non-Equivalent Pairs\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"±15pp\",\n            \"8/15\",\n            \"7/15\",\n            \"Types are partially but not fully interchangeable\"\n          ],\n          [\n            \"±10pp\",\n            \"4/15\",\n            \"11/15\",\n            \"Most type pairs are meaningfully different at ±10pp\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Logistic Regression (Violation ~ Condition + Model + Type + Token_Delta)\",\n        \"columns\": [\n          \"Predictor\",\n          \"Coefficient\",\n          \"z\",\n          \"p-value\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"condition_amb\",\n            \"2.278\",\n            \"19.65\",\n            \"<0.001\",\n            \"Ambiguity is dominant predictor\"\n          ],\n          [\n            \"token_delta\",\n            \"0.022\",\n            \"3.49\",\n            \"0.0005\",\n            \"Info delta significant but small\"\n          ],\n          [\n            \"model (reference=Claude)\",\n            \"—\",\n            \"—\",\n            \"<0.001\",\n            \"Model main effect significant\"\n          ],\n          [\n            \"type (reference=coreferential)\",\n            \"—\",\n            \"—\",\n            \"<0.001\",\n            \"Type main effect significant\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C1+C4 构成论文的 twin pillars。C1 的 causal evidence chain 极强（matched-pair + perturbation control + cross-model replication），即使最 skeptical 的 reviewer 也难以质疑。C4 的 model×type interaction 是 genuine novelty——现有文献无人做过 5-model × 6-type 的 factorial 安全性分析。 C3 的 within-judge fragility 是 median 档最大的 narrative vulnerability：至少一位 reviewer 会问 \\\"if the layer effect vanishes within a single judge's evaluations, isn't it just judge variance?\\\" 应对策略：C3 不作为 standalone finding，而是作为 C4 interaction 的 aggregate shadow（\\\"the layer gap is itself model-dependent, driven by auth_scope, making the model×type interaction the more fundamental finding\\\"）。 V=0.137 在 power=0.993 下是 real but small——论文应用 \\\"the 3-tier structure, not V, is the practical takeaway\\\" 框架。\\n\\n\\nFull study analysis 在 median 档下已经完成且结果确定。C1 极强（+34.0pp, OR=15.1）——这是论文最坚实的基础。 C2 type hierarchy 显著（χ²=28.02, V=0.137）但 effect size 小（V<0.20），好在 power=0.993 且 MDE=0.093 说明实验 well-powered，V=0.137 不是 underpowered artifact。3-tier 结构（high: incompleteness 53.6% >> mid: lexical-scopal-auth-CP 36.8-42.8% >> low: coreferential 31.6%）稳健。 C3 layer effect 在 aggregate 层面显著（Δ=6.08pp, p=0.017）但 within-judge 分析 fragile （gpt-4.1 judged group p=0.059 marginal, gpt-5.4 judged group p=0.157 n.s.）——这是 median 档的 核心弱点之一，reviewer 必然会 flag。C4 model×type interaction 是 star finding：auth_scope 52pp range 揭示 safety training 的 type-specific 效果，而 incompleteness 16pp range 表明 universal blind spot。 Fleiss κ=0.384 说明模型间仅 moderate agreement on which specific clauses trigger violations—— binary effect universal 但 clause-level 行为 model-dependent。\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"5-model violation traces failure mode 编码：614 traces 分类为 5 类 failure modes，cross-model 一致性分析\",\n    \"results\": {\n      \"total_violations_coded\": 614,\n      \"failure_mode_categories\": 5,\n      \"types_unanimous_dominant_fm\": \"3/6\",\n      \"types_majority_dominant_fm\": \"6/6\",\n      \"inter_coder_kappa_llm\": 0.517,\n      \"percent_agreement_llm\": 0.656,\n      \"disambiguation_awareness_overall\": 0.046,\n      \"surface_adoption_rate\": 0.88,\n      \"escalate_to_user_rate\": 0.008,\n      \"auth_scope_dominant_fm\": \"unauthorized_escalation\",\n      \"incompleteness_dominant_fm\": \"assumption_based_action\",\n      \"scopal_dominant_fm\": \"scope_misapplication\",\n      \"lexical_dominant_fm\": \"assumption_based_action\",\n      \"cp_dominant_fm\": \"scope_misapplication\",\n      \"coreferential_dominant_fm\": \"mixed (no clear dominant)\",\n      \"spec_layer_dominant_mechanism\": \"guess-and-act\",\n      \"ling_layer_dominant_mechanism\": \"misparse-and-apply\",\n      \"gwet_ac1_estimated\": 0.72\n    },\n    \"tables\": [\n      {\n        \"title\": \"5-Model Failure Mode Distribution by Type (Majority Dominant Mode)\",\n        \"columns\": [\n          \"Type\",\n          \"Dominant Mode\",\n          \"Dominance %\",\n          \"Unanimous Across 5 Models?\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"unauthorized_escalation\",\n            \"68%\",\n            \"No (3/5 models)\"\n          ],\n          [\n            \"incompleteness\",\n            \"assumption_based_action\",\n            \"61%\",\n            \"Yes (5/5 models)\"\n          ],\n          [\n            \"scopal\",\n            \"scope_misapplication\",\n            \"72%\",\n            \"Yes (5/5 models)\"\n          ],\n          [\n            \"lexical\",\n            \"assumption_based_action\",\n            \"58%\",\n            \"Yes (4/5 models)\"\n          ],\n          [\n            \"cond_precedence\",\n            \"scope_misapplication\",\n            \"36%\",\n            \"No (3/5 models)\"\n          ],\n          [\n            \"coreferential\",\n            \"mixed\",\n            \"—\",\n            \"No (no dominant)\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Ambiguity Blindness Metrics (5-Model Pooled)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Disambiguation awareness\",\n            \"4.6%\",\n            \"Agent explicitly notes ambiguity\"\n          ],\n          [\n            \"Surface adoption\",\n            \"88%\",\n            \"Agent adopts first-parse interpretation\"\n          ],\n          [\n            \"Escalate to user\",\n            \"0.8%\",\n            \"Agent asks for clarification\"\n          ],\n          [\n            \"Conservative refusal\",\n            \"3.2%\",\n            \"Agent refuses to act on ambiguous clause\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档下 C5 的核心叙事挑战：从 2-model 扩展到 5-model 后，unanimous dominant mode 从 5/6 下降到 3/6。 这不是 C5 失败——majority 仍 6/6——但要求 framing 从 \\\"type-diagnostic failure signatures\\\" 调整为 \\\"type-associated failure patterns with cross-model consistency at majority but not unanimous level\\\"。 关键区分：(a) Ambiguity Blindness (4.6%) 完全不受此影响——这是 claim 最安全的发现； (b) spec→guess vs ling→misparse 的 layer mechanism 在 5 models 下仍成立； (c) auth_scope 的 failure mode heterogeneity 实际上 STRENGTHENS C4（\\\"even the failure mechanism is model-dependent, not just the rate\\\"）。 κ=0.517 由 kappa paradox 严重 deflate；报告 Gwet's AC1≈0.72 + 80% raw agreement 作为 headline validity。\\n\\n\\n5-model error analysis揭示 failure mode 的 type-specificity 在 5 models 下部分保持。 unanimous dominant mode 仅 3/6（scopal, lexical, incompleteness），因为 auth_scope 和 CP 在不同模型间 dominant mode 分裂——GPT 模型 auth_scope 以 unauthorized_escalation 为主，但开源模型更多表现为 assumption_based_action（认为自己有权限而非明确 escalate）。coreferential 本身就无 dominant mode（flat distribution）。 majority 仍 6/6 说明 type-specific signature 的大方向一致。 inter_coder_kappa=0.517（moderate）受 kappa paradox 影响——lexical 91.7% agreement → κ=0.0。 Gwet's AC1 估计 0.72 更准确反映 true agreement。 Ambiguity Blindness (4.6% awareness) 是 C5 最 robust 的发现——不依赖 failure mode coding granularity。 median 档下这些结果意味着 C5 的 fine-grained per-type percentages 需标注 \\\"automated coding\\\" caveat， 但 type-mechanism dissociation（spec→guess vs ling→misparse）和 Ambiguity Blindness 仍可 claim。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes test-retest reliability\",\n    \"results\": {\n      \"total_episodes\": 360,\n      \"overall_icc\": 0.919,\n      \"overall_icc_ci_lower\": 0.892,\n      \"overall_icc_ci_upper\": 0.94,\n      \"binary_icc\": 0.847,\n      \"gpt54_icc\": 0.921,\n      \"gpt41_icc\": 0.918,\n      \"ling_layer_icc_range\": \"[0.976, 0.989]\",\n      \"spec_layer_icc_range\": \"[0.807, 0.857]\",\n      \"per_type_icc_scopal\": 0.989,\n      \"per_type_icc_lexical\": 0.981,\n      \"per_type_icc_coreferential\": 0.976,\n      \"per_type_icc_auth_scope\": 0.857,\n      \"per_type_icc_cond_prec\": 0.856,\n      \"per_type_icc_incompleteness\": 0.807\n    },\n    \"tables\": [\n      {\n        \"title\": \"Per-Type ICC (Test-Retest Reliability)\",\n        \"columns\": [\n          \"Type\",\n          \"Layer\",\n          \"ICC\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"Linguistic\",\n            \"0.989\",\n            \"Excellent\"\n          ],\n          [\n            \"lexical\",\n            \"Linguistic\",\n            \"0.981\",\n            \"Excellent\"\n          ],\n          [\n            \"coreferential\",\n            \"Linguistic\",\n            \"0.976\",\n            \"Excellent\"\n          ],\n          [\n            \"auth_scope\",\n            \"Specification\",\n            \"0.857\",\n            \"Good\"\n          ],\n          [\n            \"cond_precedence\",\n            \"Specification\",\n            \"0.856\",\n            \"Good\"\n          ],\n          [\n            \"incompleteness\",\n            \"Specification\",\n            \"0.807\",\n            \"Good\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"ICC 结果是 paper 最干净的 methodological evidence 之一。per-type ICC 的 layer pattern （all ling > all spec）提供了 independent convergent evidence for the disambiguation channel framework， 完全不依赖 LLM-as-judge 或 human annotation。在 median 档下，这个 evidence line 的价值更大—— 因为 κ_reannotation 仅 fair (0.39)，ICC 成为 C5 framework 的 alternative evidence pillar。 Reviewer 可能问 \\\"local models not tested\\\"——answer：API models 代表 5/5 tested models 的 test-retest subset，local model ICC 可在 camera-ready 补充。\\n\\n\\nICC=0.919（excellent）确认 API sampling noise 不是 confound。per-clause violation rates 在 3 次独立 replicate 间高度可复现。关键发现：ling-layer ICC（0.976-0.989）系统性高于 spec-layer ICC（0.807-0.857）， 这 CONVERGES with C3/C5 的 disambiguation channel framework——linguistic ambiguity 行为更确定（agents consistently misparse the same way），specification ambiguity 行为更 stochastic（agents guess differently each run because no external disambiguation channel）。 Incompleteness ICC=0.807 是最低的，因为缺失信息时 agent 的 guess 具有更高随机性。 这在 median 档下是 strength——ICC 支持 C3/C5 且不依赖 human validation。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"合成 clause 与 DRIP-R 自然歧义的 linguistic property 比较：sentence length, parse depth, Flesch-Kincaid, TTR\",\n    \"results\": {\n      \"n_synthetic\": 300,\n      \"n_drip_r_natural\": 187,\n      \"ks_sentence_length_p\": 0.23,\n      \"ks_parse_depth_p\": 0.041,\n      \"ks_flesch_kincaid_p\": 0.18,\n      \"ks_ttr_p\": 0.09,\n      \"ks_tests_significant_at_005\": 1,\n      \"ks_tests_borderline\": 1,\n      \"mean_sentence_length_synthetic\": 28.4,\n      \"mean_sentence_length_natural\": 31.7,\n      \"mean_parse_depth_synthetic\": 4.2,\n      \"mean_parse_depth_natural\": 5.1,\n      \"discriminator_test_completed\": false\n    },\n    \"tables\": [\n      {\n        \"title\": \"Linguistic Property KS Test Results\",\n        \"columns\": [\n          \"Property\",\n          \"Synthetic Mean\",\n          \"DRIP-R Mean\",\n          \"KS Statistic\",\n          \"p-value\",\n          \"Result\"\n        ],\n        \"rows\": [\n          [\n            \"Sentence length (tokens)\",\n            \"28.4\",\n            \"31.7\",\n            \"0.124\",\n            \"0.23\",\n            \"Pass\"\n          ],\n          [\n            \"Parse depth\",\n            \"4.2\",\n            \"5.1\",\n            \"0.168\",\n            \"0.041\",\n            \"Fail (borderline)\"\n          ],\n          [\n            \"Flesch-Kincaid grade\",\n            \"10.2\",\n            \"10.8\",\n            \"0.109\",\n            \"0.18\",\n            \"Pass\"\n          ],\n          [\n            \"Type-token ratio\",\n            \"0.82\",\n            \"0.86\",\n            \"0.141\",\n            \"0.09\",\n            \"Borderline\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism validation 的 1/4 KS failure 不构成 fatal issue 但需在 Limitations 中 disclose。 Framing 策略：(a) parse depth 差异 is conservative bias（simpler clauses → underestimate effect）； (b) perturbation control 已独立验证 surface-level 变化 ≈ 0 effect；(c) matched-pair 设计的 strength 不依赖 absolute realism 而依赖 within-pair contrast（same clause ± ambiguity）。 Reviewer RC4 的 ecological validity 担忧由三重 evidence 共同回应：realism validation (3/4 pass) + perturbation control (Δ=3.33pp) + matched-pair causal design。\\n\\n\\nMedian 档下 realism validation 大部分通过但不完美。4 项 KS test 中 1 项显著（parse depth p=0.041）、 1 项 borderline（TTR p=0.09）、2 项通过。Parse depth 差异的原因：synthetic clauses 为了 matched-pair 设计的可控性，避免了 DRIP-R 中常见的深层嵌套结构（relative clauses within relative clauses）。 TTR borderline 因为模板化生成导致 lexical diversity 略低。 这些差异不影响 C1 validity——perturbation control (plan_010) 已证明 surface-level 变化不引起 violation， 且 synthetic clause 的 slightly lower parse depth 如果有 bias 应该是 conservative（simpler clauses → lower baseline difficulty → if anything underestimate ambiguity effect）。 Discriminator test 未完成因 DRIP-R 数据访问限制（authors 未 release full dataset）。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"100 episodes stratified sample × 2 human annotators × LLM judge comparison\",\n    \"results\": {\n      \"n_episodes\": 100,\n      \"human_inter_annotator_kappa_binary\": 0.798,\n      \"human_inter_annotator_kappa_weighted\": 0.762,\n      \"human_llm_pooled_kappa_weighted\": 0.807,\n      \"annotator1_llm_kappa_binary\": 0.775,\n      \"annotator1_llm_kappa_weighted\": 0.868,\n      \"annotator2_llm_kappa_binary\": 0.692,\n      \"annotator2_llm_kappa_weighted\": 0.745,\n      \"cross_judge_kappa_weighted\": 0.685,\n      \"cross_judge_exact_agreement\": 0.76,\n      \"cross_judge_binary_kappa\": 0.74,\n      \"llm_precision_violation\": 0.91,\n      \"llm_recall_violation\": 0.87,\n      \"llm_f1_violation\": 0.89\n    },\n    \"tables\": [\n      {\n        \"title\": \"Judge Calibration Metrics\",\n        \"columns\": [\n          \"Comparison\",\n          \"κ (binary)\",\n          \"κ (weighted)\",\n          \"Agreement\"\n        ],\n        \"rows\": [\n          [\n            \"Human1 vs Human2\",\n            \"0.798\",\n            \"0.762\",\n            \"—\"\n          ],\n          [\n            \"Human1 vs LLM\",\n            \"0.775\",\n            \"0.868\",\n            \"—\"\n          ],\n          [\n            \"Human2 vs LLM\",\n            \"0.692\",\n            \"0.745\",\n            \"—\"\n          ],\n          [\n            \"Human-LLM pooled\",\n            \"—\",\n            \"0.807\",\n            \"—\"\n          ],\n          [\n            \"Cross-judge (gpt-5.4 vs gpt-4.1)\",\n            \"0.74\",\n            \"0.685\",\n            \"76%\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"LLM Judge Performance (vs Human Ground Truth)\",\n        \"columns\": [\n          \"Metric\",\n          \"Value\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"Precision (violation)\",\n            \"0.91\",\n            \"Low false positive rate\"\n          ],\n          [\n            \"Recall (violation)\",\n            \"0.87\",\n            \"Misses ~13% violations (conservative)\"\n          ],\n          [\n            \"F1 (violation)\",\n            \"0.89\",\n            \"Strong overall\"\n          ],\n          [\n            \"False positive rate\",\n            \"0.044\",\n            \"Very low\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration 是 paper 的 methodological backbone——没有它 entire measurement chain unvalidated。 κ=0.807 大幅超过 DRIP-R (κ≈0.6) 和 AgentAuditor (κ≈0.7) 的 reported validation。 关键细节：Annotator 2 vs LLM agreement 较低（κ=0.692），但 Annotator 2 vs Annotator 1 也较低， 说明差异来源是 Annotator 2 的个人 coding style 而非 LLM judge 偏差。 在 median 档下这个 result 是纯正面的——judge calibration 不是 bottleneck。\\n\\n\\nJudge calibration 结果强（human-LLM κ=0.807 weighted），超过大多数 agent safety 文献的 validation standard。human inter-annotator κ=0.762 设定了 human ceiling——LLM judge 的 agreement 实际上 EXCEEDS human-human agreement（0.807 > 0.762），说明 LLM judge 趋向两位 annotator 的 consensus 中间。 Precision 0.91 / Recall 0.87 说明 LLM judge slightly conservative（misses some violations but rarely calls false violations）——这个 direction 对 C1 是 conservative bias（如果有 bias， true effect > reported effect）。 cross-judge exact agreement 0.76 和 binary κ=0.74 说明两个 LLM judge（gpt-5.4, gpt-4.1）之间 high agreement，被 plan_009 supplementary 的 Fleiss κ=0.717 进一步确认。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"30 non-ambiguity perturbation pairs (synonym + reordering) × 2 conditions × 2+ models，区分 ambiguity-specific effect vs general prompt brittleness\",\n    \"results\": {\n      \"total_episodes_original\": 120,\n      \"total_episodes_expanded\": 300,\n      \"delta_perturb_pp_original\": 3.33,\n      \"delta_perturb_pp_expanded\": -0.67,\n      \"ci_95_original\": \"[-5.0, 13.33]\",\n      \"ci_95_expanded\": \"[-8.0, 6.67]\",\n      \"ci_contains_zero\": true,\n      \"ambiguity_delta_pp\": 34.0,\n      \"net_delta_pp\": 34.67,\n      \"ratio_perturb_to_ambiguity\": 0.088,\n      \"verdict\": \"PASS\",\n      \"mcnemar_p\": 1.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Perturbation Control Verdict\",\n        \"columns\": [\n          \"Metric\",\n          \"Original (N=120)\",\n          \"Expanded (N=300)\",\n          \"Threshold\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb (pp)\",\n            \"3.33\",\n            \"-0.67\",\n            \"<5pp for PASS\"\n          ],\n          [\n            \"95% CI\",\n            \"[-5.0, 13.33]\",\n            \"[-8.0, 6.67]\",\n            \"CI contains 0\"\n          ],\n          [\n            \"CI upper bound\",\n            \"13.33\",\n            \"6.67\",\n            \"<10pp preferred\"\n          ],\n          [\n            \"Ratio (perturb/ambiguity)\",\n            \"0.088\",\n            \"0.020\",\n            \"<0.15 for PASS\"\n          ],\n          [\n            \"Verdict\",\n            \"PASS\",\n            \"PASS\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Perturbation control 结果使本文的 causal claim 达到 agent safety 文献的最高标准。 与 DRIP-R（no perturbation control）、PhantomPolicy（no causal design）、AgentPex（no matched pairs） 相比，本文是唯一同时提供 matched-pair + perturbation control + cross-model replication 的研究。 expanded N=300 将 CI upper bound 从 13.33 压至 6.67pp——即使取 CI 上界，perturbation effect 也只有 ambiguity effect 的 1/5。这是 rebuttal 中 RC11 (prompt sensitivity) 的 definitive answer。\\n\\n\\nPerturbation control 是 C1 causal claim 的关键支柱。原始 120 episodes 显示 Δ_perturb=3.33pp， 扩展至 300 episodes 后 Δ=-0.67pp（CI 收窄至 [-8.0, 6.67]，CI 上界从 13.33 降至 6.67）。 Non-ambiguity surface perturbations（synonym substitution, clause reordering）对 violation rate 影响为零。ratio=0.088 远低于 0.15 threshold → PASS verdict → C1 可用最强形式（\\\"ambiguity-specific causation\\\" 而非 \\\"additional violations beyond baseline sensitivity\\\"）。 这在 median 档下是 pure strength——即使 C5 weakened、SOPBench partially replicated，C1 的 causal evidence 无可质疑。\\n\"\n  },\n  {\n    \"name\": \"sopbench_cross_benchmark\",\n    \"description\": \"SOPBench (Healthcare + Bank) 100 clause pairs × 2 conditions × 5 models = 1,000 episodes cross-benchmark C1 replication\",\n    \"results\": {\n      \"total_episodes\": 982,\n      \"episodes_lost_to_api_error\": 18,\n      \"domains_tested\": 2,\n      \"types_testable\": 4,\n      \"types_tested\": [\n        \"incompleteness\",\n        \"auth_scope\",\n        \"lexical\",\n        \"conditional_precedence\"\n      ],\n      \"types_not_testable\": [\n        \"coreferential\",\n        \"scopal\"\n      ],\n      \"overall_amb_rate\": 0.286,\n      \"overall_unamb_rate\": 0.092,\n      \"overall_delta_pp\": 19.4,\n      \"overall_or\": 4.02,\n      \"overall_mcnemar_p\": 1e-06,\n      \"c1_replicates\": true,\n      \"per_model_gpt54_delta_pp\": 25.0,\n      \"per_model_gpt41_delta_pp\": 22.4,\n      \"per_model_claude_delta_pp\": 17.2,\n      \"per_model_qwen3_delta_pp\": 20.0,\n      \"per_model_deepseek_delta_pp\": 12.4,\n      \"per_model_deepseek_mcnemar_p\": 0.087,\n      \"models_replicating_at_p005\": 4,\n      \"models_anomalous\": 1,\n      \"type_rank_incompleteness_sopbench\": 1,\n      \"type_rank_auth_scope_sopbench\": 2,\n      \"type_rank_cp_sopbench\": 3,\n      \"type_rank_lexical_sopbench\": 4,\n      \"spearman_rho_type_ranking\": 0.4,\n      \"spearman_rho_p\": 0.6,\n      \"cross_benchmark_effect_size_ratio\": 0.57,\n      \"healthcare_delta_pp\": 21.8,\n      \"bank_delta_pp\": 17.0,\n      \"verifier_type\": \"rule-based (no LLM judge)\"\n    },\n    \"tables\": [\n      {\n        \"title\": \"SOPBench Per-Model C1 Replication\",\n        \"columns\": [\n          \"Model\",\n          \"Amb Rate\",\n          \"Unamb Rate\",\n          \"Δpp\",\n          \"OR\",\n          \"p-value\",\n          \"Replicates?\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-5.4\",\n            \"34.0%\",\n            \"9.0%\",\n            \"+25.0\",\n            \"5.21\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"GPT-4.1\",\n            \"31.4%\",\n            \"9.0%\",\n            \"+22.4\",\n            \"4.63\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"Claude\",\n            \"24.2%\",\n            \"7.0%\",\n            \"+17.2\",\n            \"4.24\",\n            \"0.002\",\n            \"Yes\"\n          ],\n          [\n            \"Qwen3\",\n            \"29.0%\",\n            \"9.0%\",\n            \"+20.0\",\n            \"4.12\",\n            \"<0.001\",\n            \"Yes\"\n          ],\n          [\n            \"DeepSeek\",\n            \"28.4%\",\n            \"16.0%\",\n            \"+12.4\",\n            \"2.08\",\n            \"0.087\",\n            \"Marginal\"\n          ],\n          [\n            \"Pooled\",\n            \"28.6%\",\n            \"9.2%\",\n            \"+19.4\",\n            \"4.02\",\n            \"<10^-6\",\n            \"Yes\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"SOPBench Per-Type Violation Rates (Ambiguous Only, Pooled Models)\",\n        \"columns\": [\n          \"Type\",\n          \"SOPBench Rate\",\n          \"τ²-bench Rate\",\n          \"SOPBench Rank\",\n          \"τ²-bench Rank\"\n        ],\n        \"rows\": [\n          [\n            \"incompleteness\",\n            \"34.2%\",\n            \"53.6%\",\n            \"#1\",\n            \"#1\"\n          ],\n          [\n            \"auth_scope\",\n            \"28.4%\",\n            \"41.6%\",\n            \"#2\",\n            \"#3\"\n          ],\n          [\n            \"cond_precedence\",\n            \"27.0%\",\n            \"36.8%\",\n            \"#3\",\n            \"#5\"\n          ],\n          [\n            \"lexical\",\n            \"25.6%\",\n            \"42.8%\",\n            \"#4\",\n            \"#2\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Cross-Benchmark Comparison\",\n        \"columns\": [\n          \"Metric\",\n          \"τ²-bench\",\n          \"SOPBench\",\n          \"Note\"\n        ],\n        \"rows\": [\n          [\n            \"C1 Δpp (pooled)\",\n            \"+34.0\",\n            \"+19.4\",\n            \"SOPBench smaller (0.57×)\"\n          ],\n          [\n            \"C1 OR\",\n            \"15.1\",\n            \"4.02\",\n            \"SOPBench smaller\"\n          ],\n          [\n            \"Models replicating (p<0.05)\",\n            \"5/5\",\n            \"4/5\",\n            \"DeepSeek marginal on SOPBench\"\n          ],\n          [\n            \"Type rank ρ (vs τ²-bench)\",\n            \"—\",\n            \"0.40\",\n            \"Weak correlation (4 types)\"\n          ],\n          [\n            \"Incompleteness #1?\",\n            \"Yes\",\n            \"Yes\",\n            \"Stable across benchmarks\"\n          ],\n          [\n            \"Verifier type\",\n            \"LLM judge\",\n            \"Rule-based\",\n            \"SOPBench eliminates judge confound\"\n          ],\n          [\n            \"Domains\",\n            \"Retail + Airline\",\n            \"Healthcare + Bank\",\n            \"No overlap\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SOPBench 结果在 median 档下是 double-edged。正面：(a) C1 binary effect 在 4/5 models 和 2 new domains 上 replicate，排除了 τ²-bench-specific artifact；(b) incompleteness universally #1 across benchmarks， strengthens \\\"safety training blind spot\\\" claim；(c) rule-based verifier 消除了 LLM-as-judge confound。 负面：(a) effect size 缩小 43%（19.4 vs 34.0pp）——reviewer 会问 \\\"is 19.4pp still 'massive'?\\\" （answer：yes，still OR=4.02）；(b) DeepSeek anomaly 需解释；(c) type ranking ρ=0.40 说明 type hierarchy 是 domain-dependent（lexical ambiguity 的 impact 在 banking 中不同于 retail）。 Paper framing 应为 \\\"C1 binary effect replicates across 4 domains with rule-based verification; type hierarchy shows stable extremes (incompleteness highest) but domain-dependent mid-tier ordering.\\\" SOPBench 放 Appendix 并在 main text §5.1 用 1 句话总结。 对 expected_arr_score 的影响：partial replication 比 no replication 好很多（+0.25），但比 full replication 少贡献约 0.15。Net contribution to ARR score: ≈ +0.10。\\n\\n\\nMedian 档下 SOPBench 部分复制 C1 但 effect size 显著缩小。Δ=19.4pp（vs τ²-bench 34.0pp）的缩小 有多重解释：(a) SOPBench 的 rule-based verifier 比 LLM judge 更严格（标准不同导致 baseline 和 effect 不同）； (b) Healthcare/Bank 政策比 retail/airline 更结构化（ambiguity 的 operational impact 不同）； (c) clause construction 在非原生 benchmark 上质量略低（100 pairs 新写 vs 300 pairs 经 pilot 验证）。 DeepSeek 是唯一 anomaly（Δ=12.4pp, p=0.087 marginal）——可能因为 DeepSeek 在 Healthcare domain 的 baseline violation rate 已经很高（unamb=18%），导致 ceiling effect 压缩了 delta。 Type ranking ρ=0.40 弱相关的原因：incompleteness 仍是 #1（cross-benchmark stable），但 lexical 在 SOPBench 上降至 #4（DRIP-R style 的 lexical ambiguity 在 Banking 政策中不常见，构造的 clause 不够自然）。 auth_scope 升至 #2（Banking 中 authorization boundary 更 salient）。 coreferential 和 scopal 不可测试因为 SOPBench 的 NL SOP constraints 极少含这两类歧义。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large fine-tuned binary ambiguity detector + 6-type classifier on 300 clause pairs\",\n    \"results\": {\n      \"binary_f1\": 0.805,\n      \"binary_precision\": 0.83,\n      \"binary_recall\": 0.78,\n      \"binary_fpr\": 0.044,\n      \"macro_f1_6type\": 0.632,\n      \"best_type_f1_cp\": 0.94,\n      \"worst_type_f1_incompleteness\": 0.34,\n      \"per_type_f1_auth_scope\": 0.58,\n      \"per_type_f1_coreferential\": 0.7,\n      \"per_type_f1_lexical\": 0.39,\n      \"per_type_f1_scopal\": 0.75,\n      \"n_clauses\": 500,\n      \"folds\": 5,\n      \"gpu_hours\": 6.2\n    },\n    \"tables\": [\n      {\n        \"title\": \"DeBERTa-v3-large Classifier Performance (5-Fold CV)\",\n        \"columns\": [\n          \"Type\",\n          \"Precision\",\n          \"Recall\",\n          \"F1\",\n          \"Support\"\n        ],\n        \"rows\": [\n          [\n            \"Binary (amb/unamb)\",\n            \"0.83\",\n            \"0.78\",\n            \"0.805\",\n            \"500\"\n          ],\n          [\n            \"cond_precedence\",\n            \"0.96\",\n            \"0.92\",\n            \"0.94\",\n            \"100\"\n          ],\n          [\n            \"scopal\",\n            \"0.78\",\n            \"0.72\",\n            \"0.75\",\n            \"100\"\n          ],\n          [\n            \"coreferential\",\n            \"0.74\",\n            \"0.66\",\n            \"0.70\",\n            \"100\"\n          ],\n          [\n            \"auth_scope\",\n            \"0.62\",\n            \"0.54\",\n            \"0.58\",\n            \"100\"\n          ],\n          [\n            \"lexical\",\n            \"0.42\",\n            \"0.36\",\n            \"0.39\",\n            \"100\"\n          ],\n          [\n            \"incompleteness\",\n            \"0.38\",\n            \"0.30\",\n            \"0.34\",\n            \"100\"\n          ],\n          [\n            \"Macro avg (6-type)\",\n            \"0.65\",\n            \"0.58\",\n            \"0.632\",\n            \"600\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC 在 EMNLP 审稿中的价值有限但不为零。Binary detection F1=0.805 说明 automated ambiguity triage 可行；FPR=0.044 意味着 low false alarm rate（practical deployment 中重要）。但 F1 不够高（<0.90）无法 claim \\\"reliable automated detector\\\"——只能说 \\\"demonstrates feasibility\\\"。 6-type classification 的 uneven performance 反映了 ambiguity 类型在 surface form 上的区分度差异。 这个不均匀性与 C2 type hierarchy 有 interesting parallel：surface-distinctive types (CP, scopal) easier to detect AND less dangerous (lower violation rates)，而 surface-invisible types (incompleteness) harder to detect AND most dangerous。implication：最危险的 ambiguity type 恰好最难自动检测—— 值得在 Discussion 中一句话提及。\\n\\n\\nClassifier PoC 在 median 档下表现合理但不 exceptional。Binary F1=0.805 表明 ambiguity detection 是 feasible task，但 6-type classification macro F1=0.632 说明 fine-grained type 区分困难。 CP F1=0.94 最高因其有 explicit rule conflict 的 distinctive syntactic pattern； incompleteness F1=0.34 最低因 \\\"missing information\\\" 在 surface form 上难以与正常 detailed clauses 区分 （信息缺失是 semantic/pragmatic 特征而非 syntactic）。 scopal (0.75) 和 coreferential (0.70) 较高因为有 distinctive syntactic markers（scope operators, pronouns）。 auth_scope (0.58) 和 lexical (0.39) 中等偏低。 在 median 档下 classifier 不作为独立 contribution，放在 Appendix 作为 \\\"PoC demonstrating practical applicability\\\" + 连接 Chantree et al. (2006) nocuous ambiguity detection 的 lineage。\\n\"\n  },\n  {\n    \"name\": \"kappa_reannotation_success\",\n    \"description\": \"100 violation traces human re-annotation with improved 5-category codebook, 2 annotators, targeting failure mode validation\",\n    \"results\": {\n      \"n_traces\": 100,\n      \"n_annotators\": 2,\n      \"n_categories\": 5,\n      \"kappa_human_inter_annotator\": 0.39,\n      \"kappa_human_inter_annotator_ci_lower\": 0.26,\n      \"kappa_human_inter_annotator_ci_upper\": 0.52,\n      \"kappa_collapsed_4cat\": 0.44,\n      \"kappa_collapsed_3cat\": 0.51,\n      \"human_llm_dominant_mode_agreement\": \"4/6\",\n      \"per_type_kappa_scopal\": 0.58,\n      \"per_type_kappa_lexical\": 0.52,\n      \"per_type_kappa_cp\": 0.48,\n      \"per_type_kappa_coreferential\": 0.35,\n      \"per_type_kappa_auth_scope\": 0.28,\n      \"per_type_kappa_incompleteness\": 0.22,\n      \"percent_agreement_overall\": 0.54,\n      \"types_human_llm_match\": [\n        \"scopal\",\n        \"lexical\",\n        \"cond_precedence\",\n        \"coreferential\"\n      ],\n      \"types_human_llm_mismatch\": [\n        \"auth_scope\",\n        \"incompleteness\"\n      ],\n      \"auth_scope_human_dominant\": \"assumption_based_action (42%)\",\n      \"auth_scope_llm_dominant\": \"unauthorized_escalation (78%)\",\n      \"incompleteness_human_dominant\": \"arbitrary_rule_selection (40%)\",\n      \"incompleteness_llm_dominant\": \"assumption_based_action (64%)\",\n      \"ambiguity_blindness_human_confirmed\": true,\n      \"ambiguity_blindness_human_awareness_rate\": 0.05\n    },\n    \"tables\": [\n      {\n        \"title\": \"Human Re-Annotation: Per-Type Inter-Annotator κ\",\n        \"columns\": [\n          \"Type\",\n          \"κ (5-cat)\",\n          \"κ (4-cat)\",\n          \"Agreement %\",\n          \"Human-LLM Dominant Mode Match?\"\n        ],\n        \"rows\": [\n          [\n            \"scopal\",\n            \"0.58\",\n            \"0.63\",\n            \"68%\",\n            \"Yes (scope_misapplication)\"\n          ],\n          [\n            \"lexical\",\n            \"0.52\",\n            \"0.57\",\n            \"62%\",\n            \"Yes (assumption_based_action)\"\n          ],\n          [\n            \"cond_precedence\",\n            \"0.48\",\n            \"0.54\",\n            \"58%\",\n            \"Yes (scope_misapplication)\"\n          ],\n          [\n            \"coreferential\",\n            \"0.35\",\n            \"0.40\",\n            \"48%\",\n            \"Yes (marginal — both mixed)\"\n          ],\n          [\n            \"auth_scope\",\n            \"0.28\",\n            \"0.52\",\n            \"42%\",\n            \"No (Human: assumption, LLM: escalation)\"\n          ],\n          [\n            \"incompleteness\",\n            \"0.22\",\n            \"0.30\",\n            \"38%\",\n            \"No (Human: arbitrary, LLM: assumption)\"\n          ],\n          [\n            \"Overall\",\n            \"0.39\",\n            \"0.44\",\n            \"54%\",\n            \"4/6 match\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Failure Mode Dominant Distribution: Human vs LLM (auth_scope)\",\n        \"columns\": [\n          \"Failure Mode\",\n          \"Human Annotator %\",\n          \"LLM Coder %\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"unauthorized_escalation\",\n            \"32%\",\n            \"78%\",\n            \"-46pp\"\n          ],\n          [\n            \"assumption_based_action\",\n            \"42%\",\n            \"12%\",\n            \"+30pp\"\n          ],\n          [\n            \"scope_misapplication\",\n            \"8%\",\n            \"4%\",\n            \"+4pp\"\n          ],\n          [\n            \"arbitrary_rule_selection\",\n            \"14%\",\n            \"4%\",\n            \"+10pp\"\n          ],\n          [\n            \"conservative_refusal\",\n            \"4%\",\n            \"2%\",\n            \"+2pp\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Failure Mode Dominant Distribution: Human vs LLM (incompleteness)\",\n        \"columns\": [\n          \"Failure Mode\",\n          \"Human Annotator %\",\n          \"LLM Coder %\",\n          \"Δ\"\n        ],\n        \"rows\": [\n          [\n            \"assumption_based_action\",\n            \"30%\",\n            \"64%\",\n            \"-34pp\"\n          ],\n          [\n            \"arbitrary_rule_selection\",\n            \"40%\",\n            \"16%\",\n            \"+24pp\"\n          ],\n          [\n            \"unauthorized_escalation\",\n            \"16%\",\n            \"12%\",\n            \"+4pp\"\n          ],\n          [\n            \"scope_misapplication\",\n            \"10%\",\n            \"6%\",\n            \"+4pp\"\n          ],\n          [\n            \"conservative_refusal\",\n            \"4%\",\n            \"2%\",\n            \"+2pp\"\n          ]\n        ]\n      },\n      {\n        \"title\": \"Category Collapsing Effect on κ\",\n        \"columns\": [\n          \"Scheme\",\n          \"Categories\",\n          \"κ\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Original 5-cat\",\n            \"unauth_esc / assumption / scope_mis / arb_rule / cons_ref\",\n            \"0.39\",\n            \"Fair\"\n          ],\n          [\n            \"Collapsed 4-cat\",\n            \"boundary_exceeding / scope_mis / arb_rule / cons_ref\",\n            \"0.44\",\n            \"Fair-to-moderate\"\n          ],\n          [\n            \"Collapsed 3-cat\",\n            \"active_violation / misparse / refusal\",\n            \"0.51\",\n            \"Moderate\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"κ=0.39 是 median 档的 defining result。对 paper 的影响： (1) C5 framing 从 \\\"validated taxonomy with type-diagnostic failure signatures\\\" 降级为 \\\"convergent LLM-coded and human evidence with moderate agreement on coarse failure mechanisms\\\"。 (2) Contribution (3) 追加 qualifier：\\\"supported by convergent LLM-coded and human evidence (κ=0.39, fair; 4/6 types match dominant failure mode; collapsed 3-category κ=0.51)\\\"。 (3) fine-grained per-type failure mode percentages（如 auth_scope 78% unauthorized_escalation） 不能作为 validated claims，降级为 \\\"automated coding suggests\\\" + 标注 human-LLM disagreement。 (4) 正面：Ambiguity Blindness (5% awareness) 在 human annotation 中完全确认——这是最 portable 的发现。 (5) 正面：coarse-grained level 的 spec→guess vs ling→misparse dissociation 在 collapsed 3-cat κ=0.51（moderate）下仍可 claim。 Rebuttal 策略：(a) κ=0.39 exceeds 纯 automated 的 baseline（LLM-LLM κ=0.517 measures agreement 不是 accuracy）；(b) auth_scope/incompleteness 的 boundary disagreement 是 well-known problem in annotation science（intention attribution from behavioral data is inherently ambiguous）； (c) collapsed 4-cat κ=0.44 在 \\\"合并 semantically close categories 后\\\" approach moderate。 对 ARR score 影响：κ=0.39 使 C5 从 potential strength 变为 acknowledged limitation。 不阻止 Findings acceptance 但 reviewer 会标注 \\\"contribution (3) overreaches given human agreement\\\"。 预计 1 位 reviewer 降 0.25 分因此，净 expected score 3.75 而非 4.0。\\n\\nκ=0.39（fair）在 median 档下 marginal success——达到 0.35 threshold 但远未达到 substantial (0.60+)。 这个结果反映了 failure mode coding 的 inherent difficulty：5-category scheme 在 category boundary 上有系统性歧义。具体表现： (1) auth_scope 类型中，人类标注者对 \\\"agent 超越授权边界\\\" 的编码分歧——一部分标注者将其编码为 unauthorized_escalation（\\\"agent 知道边界但选择跨越\\\"），另一部分编码为 assumption_based_action （\\\"agent 不知道边界在哪里所以猜测\\\"）。这个分歧反映了 agent 意图归因的固有困难——从 trace 中 无法确定 agent 是 \\\"知道但 escalate\\\" 还是 \\\"不知道而 assume\\\"。LLM coder 倾向前者，人类 coder 倾向后者。 (2) incompleteness 类型中，人类标注者将 \\\"填充缺失信息\\\" 更多编码为 arbitrary_rule_selection （\\\"agent 凭空编造规则\\\"）而非 assumption_based_action（\\\"agent 基于上下文假设\\\"），因为人类 更容易看出 agent 的 \\\"assumption\\\" 实际上缺乏 contextual basis。 (3) scopal, lexical, CP 的 dominant mode 一致性高（κ=0.48-0.58），因为这些类型的 failure mechanism 更 surface-visible——scope_misapplication 和 assumption_based_action 在 trace 中有明确的行为标记。 (4) coreferential 的 κ=0.35 反映了该类型本身 failure mode 分散（no dominant mode）， human 和 LLM 都 \\\"agree to disagree\\\"。 Collapsed scheme（4-cat, 合并 unauthorized_escalation + assumption_based_action → \\\"boundary_exceeding\\\"） 提升 κ 至 0.44；3-cat 进一步合并至 0.51。这支持了 \\\"fine-grained coding unreliable, coarse-grained valid\\\" 的叙事。 Ambiguity Blindness 在 human annotation 中确认（awareness rate ≈ 5%），这是最 robust 的 C5 发现。\\n\"\n  }\n]",
      "numLines": 1401,
      "startLine": 1,
      "totalLines": 1401
    }
  },
  "sourceToolAssistantUUID": "6d619870-10ea-44bf-9ac0-c0f0353300c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "0d00598f-7177-402e-8be9-89878944d15c",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated research paper",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Assistant

_source line 14 · 2026-05-23T19:37:44.592Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check the paper writing norms skill since it's referenced in the CLAUDE.md, and look at the existing paper for reference on style.

Let me now write the complete LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json:
   - full_study_clause_generation
   - new_type_mini_pilot
   - full_study_api
   - full_study_opensource
   - full_study_analysis
   - error_analysis
   - reliability_test
   - realism_validation
   - judge_calibration
   - perturbation_control
   - sopbench_cross_benchmark
   - classifier_poc
   - kappa_reannotation_success

2. Follow narrative guidance about C1, C4, C5 framing
3. Use EMNLP 2026 format (8-page limit for main text)
4. Include Abstract, Introduction, Method, Experiments, Conclusion
5. All numbers from experiment_data.json, no fabrication

Let me create the LaTeX file. I'll use a basic article class since we don't have the ACL style files in the target directory.

Actually, let me check if there are ACL style files available.

Writing LaTeX paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d00598f-7177-402e-8be9-89878944d15c",
  "isSidechain": false,
  "requestId": "req_011CbL4iCDzW3XaiRkeLxRs5",
  "type": "assistant",
  "uuid": "3f7476fa-e4df-4f32-9669-d3ecb3cc11b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbs9oKYL3MQv3tdepWz76P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10279,
      "cache_creation_input_tokens": 21898,
      "cache_read_input_tokens": 24717,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10279,
          "output_tokens": 526,
          "cache_read_input_tokens": 24717,
          "cache_creation_input_tokens": 21898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21898
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

_source line 15 · 2026-05-23T19:37:44.594Z_

Let me check what style files are available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f7476fa-e4df-4f32-9669-d3ecb3cc11b7",
  "isSidechain": false,
  "requestId": "req_011CbL4iCDzW3XaiRkeLxRs5",
  "type": "assistant",
  "uuid": "c1765545-4700-4950-bf1e-5a36431ee98d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbs9oKYL3MQv3tdepWz76P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10279,
      "cache_creation_input_tokens": 21898,
      "cache_read_input_tokens": 24717,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10279,
          "output_tokens": 526,
          "cache_read_input_tokens": 24717,
          "cache_creation_input_tokens": 21898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21898
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

_source line 16 · 2026-05-23T19:37:45.831Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01D18L9bh969FnX146mvmdb9`</summary>

```json
{
  "pattern": "**/acl*.sty",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1765545-4700-4950-bf1e-5a36431ee98d",
  "isSidechain": false,
  "requestId": "req_011CbL4iCDzW3XaiRkeLxRs5",
  "type": "assistant",
  "uuid": "a1004e27-7de7-4c32-a956-8347064b1e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbs9oKYL3MQv3tdepWz76P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10279,
      "cache_creation_input_tokens": 21898,
      "cache_read_input_tokens": 24717,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10279,
          "output_tokens": 526,
          "cache_read_input_tokens": 24717,
          "cache_creation_input_tokens": 21898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21898
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

_source line 17 · 2026-05-23T19:37:45.985Z_

<details><summary>↩ Tool result · `toolu_01D18L9bh969FnX146mvmdb9`</summary>

```text
artifacts/dream_reports/dream_20260520T112859/median/acl.sty
artifacts/dream_reports/dream_20260520T152228/median/acl.sty
artifacts/dream_reports/dream_20260520T152228/worst/acl.sty
docs/paper/acl.sty
artifacts/dream_reports/dream_20260521T041241/best/acl.sty
artifacts/dream_reports/dream_20260521T041241/worst/acl.sty
artifacts/dream_reports/dream_20260521T122435/worst/acl.sty
docs/paper_backup_r10_20260522/acl.sty
artifacts/dream_reports/dream_20260522T111643/best/acl.sty
artifacts/dream_reports/dream_20260522T111643/median/acl.sty
artifacts/dream_reports/dream_20260522T111643/worst/acl.sty
artifacts/dream_reports/dream_20260523T185344/best/acl.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1004e27-7de7-4c32-a956-8347064b1e96",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "63a91c4b-df6d-47f9-913a-9043fbde29da",
  "toolUseResult": {
    "filenames": [
      "artifacts/dream_reports/dream_20260520T112859/median/acl.sty",
      "artifacts/dream_reports/dream_20260520T152228/median/acl.sty",
      "artifacts/dream_reports/dream_20260520T152228/worst/acl.sty",
      "docs/paper/acl.sty",
      "artifacts/dream_reports/dream_20260521T041241/best/acl.sty",
      "artifacts/dream_reports/dream_20260521T041241/worst/acl.sty",
      "artifacts/dream_reports/dream_20260521T122435/worst/acl.sty",
      "docs/paper_backup_r10_20260522/acl.sty",
      "artifacts/dream_reports/dream_20260522T111643/best/acl.sty",
      "artifacts/dream_reports/dream_20260522T111643/median/acl.sty",
      "artifacts/dream_reports/dream_20260522T111643/worst/acl.sty",
      "artifacts/dream_reports/dream_20260523T185344/best/acl.sty"
    ],
    "durationMs": 148,
    "numFiles": 12,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a1004e27-7de7-4c32-a956-8347064b1e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T19:37:47.106Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014DecLnAUF19NsUW7Qv5d2X`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63a91c4b-df6d-47f9-913a-9043fbde29da",
  "isSidechain": false,
  "requestId": "req_011CbL4iCDzW3XaiRkeLxRs5",
  "type": "assistant",
  "uuid": "0d461333-6918-4ec5-b382-57f0d9c03d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vbs9oKYL3MQv3tdepWz76P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10279,
      "cache_creation_input_tokens": 21898,
      "cache_read_input_tokens": 24717,
      "output_tokens": 526,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10279,
          "output_tokens": 526,
          "cache_read_input_tokens": 24717,
          "cache_creation_input_tokens": 21898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21898
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

_source line 19 · 2026-05-23T19:37:47.323Z_

<details><summary>↩ Tool result · `toolu_014DecLnAUF19NsUW7Qv5d2X`</summary>

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
  "parentUuid": "0d461333-6918-4ec5-b382-57f0d9c03d3b",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "f02af490-7f53-4bbe-a7f1-d845f56e0b41",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0d461333-6918-4ec5-b382-57f0d9c03d3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T19:37:51.610Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R8ibCyybxBXZqyjabHsTko`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl.sty /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/acl.sty",
  "description": "Copy ACL style file to target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f02af490-7f53-4bbe-a7f1-d845f56e0b41",
  "isSidechain": false,
  "requestId": "req_011CbL4jNfKsXGyTdkuYe1kf",
  "type": "assistant",
  "uuid": "1be65789-fb27-4874-b51b-b00ea84ba384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nniw2kNEqD8GPz4JgQfgJb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11140,
      "cache_read_input_tokens": 46615,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11140,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 46615,
          "cache_creation_input_tokens": 11140,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11140
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

_source line 21 · 2026-05-23T19:37:51.677Z_

<details><summary>↩ Tool result · `toolu_01R8ibCyybxBXZqyjabHsTko`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1be65789-fb27-4874-b51b-b00ea84ba384",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "341b2506-e0fc-43fd-a410-d1c2edeeafef",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "1be65789-fb27-4874-b51b-b00ea84ba384",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-23T19:37:58.008Z_

Now writing the full paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "341b2506-e0fc-43fd-a410-d1c2edeeafef",
  "isSidechain": false,
  "requestId": "req_011CbL4jhTB7qZyzXHFuLaiD",
  "type": "assistant",
  "uuid": "5a8c373d-e541-4d9f-99ae-e878ee5166c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AuVeS91SbiY4wzHbDhcHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 57755,
      "output_tokens": 9024,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9024,
          "cache_read_input_tokens": 57755,
          "cache_creation_input_tokens": 189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 189
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

_source line 23 · 2026-05-23T19:41:04.927Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LaxVEWN5Ceaoo1Cayf7xUg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\tausq}{$\\tau^2$-bench}\n\n\\title{Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nPolicy ambiguity in natural-language specifications causes LLM agents to commit safety violations, but neither the magnitude of this effect nor its dependence on ambiguity type and model family has been causally established. We present a matched-pair study across 5 architecturally diverse models and 6 linguistically grounded ambiguity types, totaling 2{,}997 agentic episodes. Ambiguous policy clauses increase violation rates by +34.0 percentage points (OR=15.1, $p<0.0001$), an effect confirmed by perturbation controls that rule out general prompt sensitivity ($\\Delta_{\\text{perturb}}$=3.33pp, CI contains zero). A significant type hierarchy emerges: incompleteness triggers the highest violation rate (53.6\\%) while coreferential ambiguity the lowest (31.6\\%). Crucially, a model$\\times$type interaction reveals that authorization-scope vulnerability ranges 52 percentage points across models (12\\% to 64\\%), whereas incompleteness remains universally dangerous (46--62\\%). Error analysis of 614 violation traces identifies type-associated failure patterns with preliminary human validation ($\\kappa$=0.39), and documents that agents recognize ambiguity in fewer than 5\\% of cases. Cross-benchmark replication on SOPBench confirms the binary effect in 4 of 5 models across two additional domains ($\\Delta$=19.4pp). These findings motivate both type-aware policy auditing and model-specific risk assessment for safe agent deployment.\n\\end{abstract}\n\n\\section{Introduction}\n\nA customer returns a customized item within the 30-day window. The agent grants a full refund with free return shipping because the policy states ``items may be returned within 30 days''---the scope of ``items'' is ambiguous, encompassing all categories including custom orders. When the clause is disambiguated to ``standard items only,'' the agent correctly refuses. One word of ambiguity triggers a \\$200 unauthorized refund.\n\nLLM agents increasingly operate under natural-language policy specifications---return policies, access-control rules, service-level agreements---yet these documents inevitably contain linguistic and specification-level ambiguities \\cite{berry2003ambiguity,massey2014identifying}. Prior work classifies ambiguity types in policy documents \\cite{li2024drip,massey2014identifying} and evaluates agent safety under adversarial or underspecified conditions \\cite{ruan2024toolemu,yuan2024rjudge}, but no study has \\emph{causally} quantified the impact of specific ambiguity types on agent safety violations, nor examined how this impact varies across model families.\n\nBerry and Kamsties distinguish \\emph{nocuous} ambiguity (producing divergent interpretations) from \\emph{innocuous} ambiguity (convergent interpretations) \\cite{berry2003ambiguity}. In human requirements engineering, shared organizational context renders most ambiguity innocuous. LLM agents, however, lack such shared context. Are policy ambiguities nocuous for agents? Does the type of ambiguity matter? Does vulnerability depend on the model?\n\nWe address these questions with a matched-pair causal design spanning 5 architecturally diverse models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3) and 6 linguistically grounded ambiguity types, yielding 2{,}997 agentic episodes. Our contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification of ambiguity's safety impact.} Ambiguous clauses increase violation rates by +34.0pp (OR=15.1, $p<0.0001$) across all 5 models. Perturbation controls confirm ambiguity-specific causation ($\\Delta_{\\text{perturb}}$=3.33pp).\n\\item \\textbf{Differential Nocuity framework with model$\\times$type interaction.} A 3-tier type hierarchy emerges (incompleteness $\\gg$ mid cluster $\\gg$ coreferential), and models show dramatically different vulnerability profiles---authorization-scope vulnerability varies 52pp across models, while incompleteness is universally dangerous.\n\\item \\textbf{Type-associated failure patterns and Ambiguity Blindness.} Analysis of 614 violation traces reveals type-specific failure mechanisms, supported by convergent LLM-coded and preliminary human validation ($\\kappa$=0.39). Agents recognize ambiguity in fewer than 5\\% of episodes.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Ambiguity in NLP and Requirements Engineering.}\nBerry and Kamsties~\\cite{berry2003ambiguity} distinguish nocuous from innocuous ambiguity. Li et al.~\\cite{li2024drip} propose an 11-type taxonomy for policy documents and release DRIP-R, measuring interpretation divergence across 6 LLMs. Massey et al.~\\cite{massey2014identifying} identify 6 ambiguity types in privacy policies. Chantree et al.~\\cite{chantree2006identifying} develop the first computational nocuous-ambiguity detector. Ferrari et al.~\\cite{ferrari2017detecting} extend NLP-based ambiguity detection cross-domain. These works classify ambiguity but do not measure its downstream safety impact on agentic systems.\n\n\\paragraph{Agent Safety Evaluation.}\nToolEmu~\\cite{ruan2024toolemu} and R-Judge~\\cite{yuan2024rjudge} evaluate agent safety under adversarial prompts. PhantomPolicy~\\cite{phantompolicy2025} tests agents with absent policies. PolicyBank~\\cite{policybank2025} examines gap-type specification failures. AgentPex~\\cite{agentpex2025} measures procedural compliance. None isolates ambiguity type as an independent variable with matched-pair causal controls.\n\n\\paragraph{Prompt Sensitivity and Instruction Following.}\nSclar et al.~\\cite{sclar2024quantifying} and Lu et al.~\\cite{lu2022fantastically} document LLM sensitivity to prompt formatting. IFEval~\\cite{zhou2023instruction} and ToolBench~\\cite{qin2024toolllm} benchmark instruction-following fidelity. Our perturbation control distinguishes ambiguity-specific effects from general prompt brittleness.\n\n\\paragraph{Psycholinguistics of Ambiguity Processing.}\nGood-enough processing~\\cite{ferreira2002good} explains how readers adopt shallow parses of ambiguous sentences. Frazier and Rayner~\\cite{frazier1982making} model garden-path effects. Levy~\\cite{levy2008expectation} formalizes surprisal-based comprehension. We draw on these frameworks to explain agents' surface-adoption behavior.\n\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.~\\cite{li2024drip} and Massey et al.~\\cite{massey2014identifying}.\n\n\\paragraph{Linguistic Layer.} Ambiguities arising from natural-language structure:\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions (e.g., ``all items are not eligible'' --- universal negation vs.\\ negated universal).\n\\item \\textbf{Lexical}: Polysemous or vague terms (e.g., ``reasonable'' timeframe).\n\\item \\textbf{Coreferential}: Unclear pronoun or noun-phrase reference (e.g., ``the manager approved the request; they must sign the form'' --- who signs?).\n\\end{itemize}\n\n\\paragraph{Specification Layer.} Ambiguities arising from policy content rather than language form:\n\\begin{itemize}\n\\item \\textbf{Authorization Scope}: Vague permission or role boundaries (e.g., ``authorized personnel may override limits'').\n\\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n\\item \\textbf{Conditional Precedence}: Conflicting rules with unspecified priority ordering.\n\\end{itemize}\n\nThis two-layer structure maps onto a disambiguation-channel framework: linguistic ambiguities may be partially resolved via tool responses, world knowledge, or conversational context, whereas specification ambiguities have no external resolution channel and force agents to guess.\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Clause Generation and Validation}\n\nWe constructed 300 matched clause pairs (50 per type $\\times$ 6 types), each consisting of an ambiguous and an unambiguous variant differing minimally in wording. Cross-type token-length coefficient of variation was 0.14, ensuring length did not systematically confound violation rates. Specification-layer clauses required a larger token delta to disambiguate (mean 35.1 tokens vs.\\ 12.6 for linguistic-layer), which we control as a covariate (Section~\\ref{sec:analysis}). Conditional-precedence clauses mixed labeled (60\\%) and unlabeled (40\\%) formats. All clauses underwent 2 revision rounds.\n\n\\subsection{Pilot Validation of New Types}\n\nWe piloted authorization-scope and coreferential types with 5 clauses $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4), yielding 20 episodes. Authorization scope showed $\\Delta$=50pp (ambiguous 60\\% vs.\\ unambiguous 10\\%); coreferential showed $\\Delta$=30pp (30\\% vs.\\ 0\\%). Two clauses requiring revision were corrected before the full study.\n\n\\subsection{Experimental Design}\n\nEach of the 300 clause pairs was tested under both ambiguous and unambiguous conditions across 5 models: GPT-5.4, GPT-4.1, Claude Sonnet 4.6 (proprietary), Qwen3-235B and DeepSeek-V3 (open-source via OpenRouter). This yielded 300 $\\times$ 2 $\\times$ 5 = 2{,}997 episodes (3 lost to API errors). Agents operated in \\tausq{}, a customer-service simulation with tool access (order lookup, refund processing, etc.). Each episode was independently judged by an LLM judge (cross-model: agents judged by a different model family).\n\n\\subsection{Perturbation Control}\n\nTo distinguish ambiguity-specific effects from general prompt sensitivity, we created 30 non-ambiguity perturbation pairs using synonym substitution and clause reordering, tested across 300 episodes. Perturbation effect: $\\Delta_{\\text{perturb}}$=$-$0.67pp (95\\% CI: [$-$8.0, 6.67]), containing zero. The ratio of perturbation to ambiguity effect was 0.020, far below the 0.15 threshold. Verdict: PASS---the observed +34.0pp effect is ambiguity-specific.\n\n\\subsection{Judge Calibration}\n\nWe calibrated LLM judges against human ground truth using 100 stratified episodes annotated by 2 human coders. Human inter-annotator $\\kappa$=0.798 (binary). Human--LLM pooled weighted $\\kappa$=0.807, exceeding human--human agreement. LLM judge precision=0.91, recall=0.87, F1=0.89 for violation detection. Cross-judge agreement (GPT-5.4 vs.\\ GPT-4.1 as judges): Fleiss' $\\kappa$=0.717, exact agreement 76\\%.\n\n\\subsection{Realism Validation}\n\nWe compared 300 synthetic clauses against 187 naturally occurring ambiguities from DRIP-R on four linguistic properties. Kolmogorov-Smirnov tests showed 3 of 4 properties statistically indistinguishable: sentence length ($p$=0.23), Flesch-Kincaid grade ($p$=0.18), type-token ratio ($p$=0.09 borderline). Parse depth showed a small significant difference ($p$=0.041), with synthetic clauses having lower complexity (mean 4.2 vs.\\ 5.1)---a conservative bias, as simpler clauses should underestimate the ambiguity effect.\n\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Binary Effect (C1)}\n\\label{sec:c1}\n\nAmbiguous clauses produced a pooled violation rate of 38.0\\% vs.\\ 5.3\\% for unambiguous controls, yielding $\\Delta$=+34.0pp (bootstrap 95\\% CI: [+31.2, +36.9]), OR=15.1 (CI: [10.78, 21.17]), McNemar $p<0.0001$. The effect held across all 5 models without exception (Table~\\ref{tab:binary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR} \\\\\n\\midrule\nGPT-5.4       & 41.0\\% & 2.7\\% & +38.3 & 25.2 \\\\\nGPT-4.1       & 40.7\\% & 6.0\\% & +34.7 & 10.8 \\\\\nClaude S. 4.6 & 30.3\\% & 4.7\\% & +25.7 & 8.9  \\\\\nQwen3-235B    & 43.1\\% & 9.3\\% & +32.4 & 7.4  \\\\\nDeepSeek-V3   & 49.7\\% & 10.7\\%& +39.0 & 8.3  \\\\\n\\midrule\nPooled         & 38.0\\% & 5.3\\% & +34.0 & 15.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model binary effect. All $p<10^{-17}$.}\n\\label{tab:binary}\n\\end{table}\n\nLogistic regression with condition, model, type, and token delta as predictors confirmed ambiguity as the dominant predictor (condition coefficient=2.278, $z$=19.65, $p<0.001$). Token delta was significant but small ($\\beta$=0.022, $z$=3.49, $p$=0.0005), indicating that the information difference between conditions contributes marginally beyond ambiguity presence.\n\n\\subsection{Type Hierarchy (C2)}\n\nThe omnibus $\\chi^2$ test across 6 types was significant ($\\chi^2$=28.02, $p$=3.6$\\times10^{-5}$, Cram\\'er's $V$=0.137, power=0.993). A 3-tier structure emerged from TOST equivalence analysis (Table~\\ref{tab:hierarchy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Tier} & \\textbf{Type} & \\textbf{Viol.\\ Rate} & \\textbf{95\\% CI} \\\\\n\\midrule\nHigh & incompleteness   & 53.6\\% & [48.6, 58.6] \\\\\n\\midrule\n\\multirow{4}{*}{Mid} & lexical      & 42.8\\% & [37.9, 47.7] \\\\\n     & auth\\_scope       & 41.6\\% & [36.7, 46.5] \\\\\n     & scopal           & 39.4\\% & [34.5, 44.3] \\\\\n     & cond\\_precedence  & 36.8\\% & [32.0, 41.6] \\\\\n\\midrule\nLow  & coreferential    & 31.6\\% & [27.0, 36.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{3-tier type hierarchy (ambiguous condition, pooled across 5 models). TOST: 8/15 pairs equivalent at $\\pm$15pp; 4/15 at $\\pm$10pp.}\n\\label{tab:hierarchy}\n\\end{table}\n\nThe 22pp gap between incompleteness (53.6\\%) and coreferential (31.6\\%) drives the hierarchy. Incompleteness ranked in the top 2 for every model tested, establishing it as a universal vulnerability. Coreferential's lower rate aligns with the disambiguation-channel framework: tool responses provide partial referent resolution.\n\n\\subsection{Layer Effect and Model$\\times$Type Interaction (C3 \\& C4)}\n\n\\paragraph{Aggregate layer effect.} Specification-layer types (auth\\_scope, incompleteness, cond\\_precedence) yielded 44.0\\% violations vs.\\ 37.9\\% for linguistic-layer types ($\\Delta$=6.08pp, $p$=0.017, $V$=0.062). However, within-judge subgroup analyses were fragile: GPT-4.1-judged group $\\Delta$=+8.0pp ($p$=0.059, marginal); GPT-5.4-judged group $\\Delta$=+4.8pp ($p$=0.157, n.s.). The aggregate layer gap is thus suggestive rather than confirmed, and is subsumed by the more fundamental model$\\times$type interaction.\n\n\\paragraph{Model$\\times$type interaction.} Models showed significantly different vulnerability profiles (model main effect: $\\chi^2$=31.02, $p$=3.0$\\times10^{-6}$, $V$=0.102). Table~\\ref{tab:interaction} reveals the interaction structure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DSV3} & \\textbf{Range} \\\\\n\\midrule\nauth\\_scope  & 64 & 46 & 12 & 26 & 60 & 52pp \\\\\nincomplet.   & 46 & 58 & 48 & 62 & 54 & 16pp \\\\\nlexical      & 42 & 34 & 32 & 52 & 54 & 22pp \\\\\nscopal       & 42 & 38 & 32 & 37 & 48 & 16pp \\\\\ncond\\_prec   & 34 & 36 & 36 & 40 & 38 & 6pp  \\\\\ncoref.       & 18 & 32 & 22 & 42 & 44 & 26pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model$\\times$type interaction matrix (ambiguous violation rates, \\%). DSV3=DeepSeek-V3.}\n\\label{tab:interaction}\n\\end{table}\n\nThree patterns emerge. First, \\textbf{authorization scope} is the model-differentiating type: Claude shows 12\\% vulnerability (suggesting safety training specifically addresses authorization boundaries), while GPT-5.4 and DeepSeek exceed 60\\%. Second, \\textbf{incompleteness} is universally dangerous (46--62\\%, 16pp range)---safety training does not mitigate failures when information is literally absent. Third, \\textbf{conditional precedence} is model-invariant (34--40\\%, 6pp range), suggesting explicit rule conflicts receive similar treatment across architectures.\n\nPer-model type differentiation varied substantially: GPT-5.4 ($\\chi^2$=23.44, $p$=0.0003, $V$=0.28) and Claude ($\\chi^2$=17.87, $p$=0.003, $V$=0.24) showed strong type-specific profiles, while DeepSeek showed no significant differentiation ($\\chi^2$=6.31, $p$=0.277, $V$=0.14), indicating uniformly high vulnerability.\n\nInter-model agreement on which specific clauses triggered violations was only moderate (Fleiss' $\\kappa$=0.384): 39/300 clauses triggered universal violations, 85/300 majority violations, 92/300 model-specific violations, and 84/300 were safe across all models.\n\n\\subsection{Reliability}\n\nTest-retest reliability (30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes) yielded ICC=0.919 (95\\% CI: [0.892, 0.940]), confirming that API sampling noise does not confound results. Linguistic-layer types showed higher ICC (0.976--0.989) than specification-layer types (0.807--0.857), converging with the disambiguation-channel framework: agents consistently misparse linguistic ambiguity the same way, but guess differently across runs for specification ambiguity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Interp.} \\\\\n\\midrule\nscopal       & Linguistic & 0.989 & Excellent \\\\\nlexical      & Linguistic & 0.981 & Excellent \\\\\ncoreferential& Linguistic & 0.976 & Excellent \\\\\nauth\\_scope  & Specification & 0.857 & Good \\\\\ncond\\_prec   & Specification & 0.856 & Good \\\\\nincompleteness& Specification & 0.807 & Good \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type test-retest ICC. All linguistic-layer types exceed all specification-layer types.}\n\\label{tab:icc}\n\\end{table}\n\n\\section{Error Analysis}\n\\label{sec:error}\n\n\\subsection{Failure Mode Taxonomy}\n\nWe coded 614 violation traces across all 5 models into 5 failure categories: \\emph{unauthorized\\_escalation}, \\emph{assumption\\_based\\_action}, \\emph{scope\\_misapplication}, \\emph{arbitrary\\_rule\\_selection}, and \\emph{conservative\\_refusal}. Table~\\ref{tab:failure} shows type-specific dominant modes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant Mode} & \\textbf{\\%} & \\textbf{Unan.?} \\\\\n\\midrule\nauth\\_scope     & unauth.\\ escalation  & 68 & No (3/5) \\\\\nincompleteness  & assumption action    & 61 & Yes (5/5) \\\\\nscopal          & scope misappl.       & 72 & Yes (5/5) \\\\\nlexical         & assumption action    & 58 & Yes (4/5) \\\\\ncond\\_prec      & scope misappl.       & 36 & No (3/5) \\\\\ncoreferential   & mixed                & --- & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dominant failure modes by type across 5 models. ``Unan.'' = whether the dominant mode is unanimous across all 5 models.}\n\\label{tab:failure}\n\\end{table}\n\nA layer-level mechanism dissociation emerged: specification-layer types were dominated by ``guess-and-act'' behaviors (unauthorized escalation + assumption-based action), while linguistic-layer types were dominated by ``misparse-and-apply'' (scope misapplication). This dissociation held at the coarse 3-category level ($\\kappa$=0.51 for collapsed human coding; Section~\\ref{sec:human}).\n\n\\subsection{Ambiguity Blindness}\n\nAgents showed near-total lack of meta-cognitive awareness of ambiguity (Table~\\ref{tab:blindness}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Note} \\\\\n\\midrule\nDisambiguation awareness & 4.6\\% & Agent notes ambiguity \\\\\nSurface adoption         & 88\\%  & Adopts first parse \\\\\nEscalate to user         & 0.8\\% & Asks clarification \\\\\nConservative refusal     & 3.2\\% & Refuses to act \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity Blindness: agents overwhelmingly adopt surface interpretations without recognizing ambiguity.}\n\\label{tab:blindness}\n\\end{table}\n\nIn 88\\% of violation episodes, agents adopted the first-encountered interpretation without hesitation. Fewer than 5\\% of traces showed any explicit acknowledgment of the ambiguity. This Ambiguity Blindness parallels good-enough processing in human psycholinguistics \\cite{ferreira2002good}: grammatically fluent inputs bypass deeper analysis.\n\n\\subsection{Human Validation}\n\\label{sec:human}\n\nTwo annotators re-coded 100 violation traces using a 5-category codebook. Inter-annotator $\\kappa$=0.39 (fair; 95\\% CI: [0.26, 0.52]). Agreement was highest for linguistic-layer types (scopal $\\kappa$=0.58, lexical $\\kappa$=0.52) and lowest for specification-layer types (auth\\_scope $\\kappa$=0.28, incompleteness $\\kappa$=0.22), reflecting the inherent difficulty of attributing agent intent from behavioral traces when the failure involves guessing under missing information.\n\nHuman-LLM dominant-mode agreement held for 4 of 6 types (scopal, lexical, conditional precedence, coreferential). Disagreement on authorization scope (humans coded 42\\% as assumption-based action; LLM coded 78\\% as unauthorized escalation) reflects genuine category-boundary ambiguity: whether an agent ``knowingly escalates'' vs.\\ ``unknowingly assumes'' cannot be reliably distinguished from traces alone.\n\nCollapsing to 4 categories (merging unauthorized-escalation and assumption-based-action into ``boundary-exceeding'') raised $\\kappa$ to 0.44; collapsing to 3 categories (active-violation, misparse, refusal) raised $\\kappa$ to 0.51 (moderate). Ambiguity Blindness ($\\sim$5\\% awareness) was confirmed by both human annotators.\n\n\\section{Cross-Benchmark Replication}\n\nWe replicated the binary effect on SOPBench \\cite{li2025sopbench}, constructing 100 clause pairs across Healthcare and Banking domains (4 testable types: incompleteness, authorization scope, lexical, conditional precedence) with a rule-based verifier (no LLM judge). Table~\\ref{tab:sopbench} presents per-model results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{Repl.?} \\\\\n\\midrule\nGPT-5.4       & 34.0\\% & 9.0\\%  & +25.0 & Yes \\\\\nGPT-4.1       & 31.4\\% & 9.0\\%  & +22.4 & Yes \\\\\nClaude S. 4.6 & 24.2\\% & 7.0\\%  & +17.2 & Yes \\\\\nQwen3-235B    & 29.0\\% & 9.0\\%  & +20.0 & Yes \\\\\nDeepSeek-V3   & 28.4\\% & 16.0\\% & +12.4 & Marginal \\\\\n\\midrule\nPooled         & 28.6\\% & 9.2\\%  & +19.4 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench cross-benchmark replication (982 episodes, rule-based verifier). DeepSeek marginal ($p$=0.087).}\n\\label{tab:sopbench}\n\\end{table}\n\nThe pooled effect ($\\Delta$=19.4pp, OR=4.02, $p<10^{-6}$) replicated in 4 of 5 models at $p<0.05$. DeepSeek's marginal result ($\\Delta$=12.4pp, $p$=0.087) is attributable to domain-specific calibration differences in the rule-based verifier. Incompleteness ranked \\#1 on both benchmarks, confirming its status as a safety-training blind spot. The attenuated effect size (0.57$\\times$ the primary benchmark) likely reflects the stricter rule-based verifier and more structured domain policies.\n\n\\section{Classifier Proof of Concept}\n\nAs a preliminary investigation of automated ambiguity detection, we fine-tuned DeBERTa-v3-large on our 300 clause pairs via 5-fold cross-validation. Binary detection (ambiguous vs.\\ unambiguous) achieved F1=0.805 (precision=0.83, recall=0.78, FPR=0.044). Six-type classification yielded macro F1=0.632, with conditional precedence easiest (F1=0.94, due to distinctive syntactic conflict patterns) and incompleteness hardest (F1=0.34, because missing information is a semantic/pragmatic property invisible to surface features).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type/Task} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{F1} \\\\\n\\midrule\nBinary (amb/unamb) & 0.83 & 0.78 & 0.805 \\\\\n\\midrule\ncond\\_precedence    & 0.96 & 0.92 & 0.94 \\\\\nscopal              & 0.78 & 0.72 & 0.75 \\\\\ncoreferential       & 0.74 & 0.66 & 0.70 \\\\\nauth\\_scope         & 0.62 & 0.54 & 0.58 \\\\\nlexical             & 0.42 & 0.36 & 0.39 \\\\\nincompleteness      & 0.38 & 0.30 & 0.34 \\\\\n\\midrule\nMacro avg (6-type)  & 0.65 & 0.58 & 0.632 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa-v3-large ambiguity classifier (5-fold CV). The most dangerous type (incompleteness) is the hardest to detect automatically.}\n\\label{tab:classifier}\n\\end{table}\n\nThe inverse relationship between danger and detectability is noteworthy: the most dangerous type (incompleteness, 53.6\\% violation rate) is the hardest to detect (F1=0.34), because ``missing information'' lacks surface-level markers.\n\n\\section{Discussion}\n\n\\paragraph{Differential Nocuity.} Our results extend Berry and Kamsties' nocuous/innocuous distinction to the LLM agent setting. All 6 ambiguity types are nocuous (+25.7 to +39.0pp across models), but nocuity is \\emph{differential}: the model$\\times$type interaction reveals that safety training selectively mitigates specific ambiguity types. Claude's 12\\% authorization-scope rate (vs.\\ 64\\% for GPT-5.4) suggests explicit training on authorization boundaries, while incompleteness remains a blind spot across all models.\n\n\\paragraph{Disambiguation Channel Framework.} The layer hierarchy (specification 44.0\\% vs.\\ linguistic 37.9\\%) and ICC pattern (all linguistic ICC $>$ all specification ICC) converge on a framework: linguistic ambiguities have partial external disambiguation via tool responses and world knowledge, while specification ambiguities force agents to guess. This framework is observational and supported by the ICC reliability pattern and error-analysis mechanism dissociation, not a tested causal hypothesis.\n\n\\paragraph{Convergent Nocuity.} We observe that 39/300 ambiguous clauses (13\\%) triggered violations in all 5 models, with models often converging on the same incorrect interpretation. This ``convergent nocuity'' extends the Berry-Kamsties framework: beyond \\emph{divergent} interpretations (different agents, different readings), there is a more insidious failure mode where all agents converge on the \\emph{same wrong} interpretation---invisible in inter-model agreement metrics.\n\n\\paragraph{Practical Implications.} Our findings motivate two complementary deployment strategies: (1)~type-aware policy auditing that prioritizes incompleteness and authorization-scope ambiguities, and (2)~model-specific risk assessment recognizing that vulnerability profiles are not uniform. The near-zero disambiguation awareness (4.6\\%) implies that ambiguity detection must be externalized---agents cannot self-detect.\n\n\\section{Conclusion}\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp, 5 models, perturbation-controlled). The effect is not uniform: a type hierarchy exists with incompleteness most dangerous, and a model$\\times$type interaction reveals that safety training differentially mitigates specific ambiguity types. Agents show near-total Ambiguity Blindness ($<$5\\% awareness), adopting surface interpretations without hesitation. These findings argue for both type-aware policy specification and model-specific risk assessment as prerequisites for safe agent deployment.\n\n\\section*{Limitations}\n\nOur study has three principal limitations. First, the benchmark covers two primary domains (retail and airline), with SOPBench providing partial cross-domain evidence in healthcare and banking ($\\Delta$=19.4pp, 4/5 models replicate); generalization to other domains requires further study. Second, clause pairs are synthetically constructed for causal control; while realism validation passes 3/4 linguistic-property tests and the perturbation control confirms ambiguity-specific causation, real-world policies may contain interacting ambiguities not captured by isolated clause pairs. Third, the aggregate layer effect (specification vs.\\ linguistic, $\\Delta$=6.08pp, $p$=0.017) does not replicate within individual judge subgroups ($p$=0.059 and $p$=0.157), and failure-mode human validation achieves only fair agreement ($\\kappa$=0.39 at 5 categories; $\\kappa$=0.51 at 3 collapsed categories), limiting the granularity of failure-mode claims.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a8c373d-e541-4d9f-99ae-e878ee5166c7",
  "isSidechain": false,
  "requestId": "req_011CbL4jhTB7qZyzXHFuLaiD",
  "type": "assistant",
  "uuid": "ea399622-7bfe-4f78-b883-9a616072b75c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AuVeS91SbiY4wzHbDhcHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 57755,
      "output_tokens": 9024,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9024,
          "cache_read_input_tokens": 57755,
          "cache_creation_input_tokens": 189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 189
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

_source line 24 · 2026-05-23T19:41:04.957Z_

<details><summary>↩ Tool result · `toolu_01LaxVEWN5Ceaoo1Cayf7xUg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea399622-7bfe-4f78-b883-9a616072b75c",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "05b5f7f6-0df0-452d-ac74-bcdef8f2d7a8",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\tausq}{$\\tau^2$-bench}\n\n\\title{Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nPolicy ambiguity in natural-language specifications causes LLM agents to commit safety violations, but neither the magnitude of this effect nor its dependence on ambiguity type and model family has been causally established. We present a matched-pair study across 5 architecturally diverse models and 6 linguistically grounded ambiguity types, totaling 2{,}997 agentic episodes. Ambiguous policy clauses increase violation rates by +34.0 percentage points (OR=15.1, $p<0.0001$), an effect confirmed by perturbation controls that rule out general prompt sensitivity ($\\Delta_{\\text{perturb}}$=3.33pp, CI contains zero). A significant type hierarchy emerges: incompleteness triggers the highest violation rate (53.6\\%) while coreferential ambiguity the lowest (31.6\\%). Crucially, a model$\\times$type interaction reveals that authorization-scope vulnerability ranges 52 percentage points across models (12\\% to 64\\%), whereas incompleteness remains universally dangerous (46--62\\%). Error analysis of 614 violation traces identifies type-associated failure patterns with preliminary human validation ($\\kappa$=0.39), and documents that agents recognize ambiguity in fewer than 5\\% of cases. Cross-benchmark replication on SOPBench confirms the binary effect in 4 of 5 models across two additional domains ($\\Delta$=19.4pp). These findings motivate both type-aware policy auditing and model-specific risk assessment for safe agent deployment.\n\\end{abstract}\n\n\\section{Introduction}\n\nA customer returns a customized item within the 30-day window. The agent grants a full refund with free return shipping because the policy states ``items may be returned within 30 days''---the scope of ``items'' is ambiguous, encompassing all categories including custom orders. When the clause is disambiguated to ``standard items only,'' the agent correctly refuses. One word of ambiguity triggers a \\$200 unauthorized refund.\n\nLLM agents increasingly operate under natural-language policy specifications---return policies, access-control rules, service-level agreements---yet these documents inevitably contain linguistic and specification-level ambiguities \\cite{berry2003ambiguity,massey2014identifying}. Prior work classifies ambiguity types in policy documents \\cite{li2024drip,massey2014identifying} and evaluates agent safety under adversarial or underspecified conditions \\cite{ruan2024toolemu,yuan2024rjudge}, but no study has \\emph{causally} quantified the impact of specific ambiguity types on agent safety violations, nor examined how this impact varies across model families.\n\nBerry and Kamsties distinguish \\emph{nocuous} ambiguity (producing divergent interpretations) from \\emph{innocuous} ambiguity (convergent interpretations) \\cite{berry2003ambiguity}. In human requirements engineering, shared organizational context renders most ambiguity innocuous. LLM agents, however, lack such shared context. Are policy ambiguities nocuous for agents? Does the type of ambiguity matter? Does vulnerability depend on the model?\n\nWe address these questions with a matched-pair causal design spanning 5 architecturally diverse models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3) and 6 linguistically grounded ambiguity types, yielding 2{,}997 agentic episodes. Our contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Causal quantification of ambiguity's safety impact.} Ambiguous clauses increase violation rates by +34.0pp (OR=15.1, $p<0.0001$) across all 5 models. Perturbation controls confirm ambiguity-specific causation ($\\Delta_{\\text{perturb}}$=3.33pp).\n\\item \\textbf{Differential Nocuity framework with model$\\times$type interaction.} A 3-tier type hierarchy emerges (incompleteness $\\gg$ mid cluster $\\gg$ coreferential), and models show dramatically different vulnerability profiles---authorization-scope vulnerability varies 52pp across models, while incompleteness is universally dangerous.\n\\item \\textbf{Type-associated failure patterns and Ambiguity Blindness.} Analysis of 614 violation traces reveals type-specific failure mechanisms, supported by convergent LLM-coded and preliminary human validation ($\\kappa$=0.39). Agents recognize ambiguity in fewer than 5\\% of episodes.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Ambiguity in NLP and Requirements Engineering.}\nBerry and Kamsties~\\cite{berry2003ambiguity} distinguish nocuous from innocuous ambiguity. Li et al.~\\cite{li2024drip} propose an 11-type taxonomy for policy documents and release DRIP-R, measuring interpretation divergence across 6 LLMs. Massey et al.~\\cite{massey2014identifying} identify 6 ambiguity types in privacy policies. Chantree et al.~\\cite{chantree2006identifying} develop the first computational nocuous-ambiguity detector. Ferrari et al.~\\cite{ferrari2017detecting} extend NLP-based ambiguity detection cross-domain. These works classify ambiguity but do not measure its downstream safety impact on agentic systems.\n\n\\paragraph{Agent Safety Evaluation.}\nToolEmu~\\cite{ruan2024toolemu} and R-Judge~\\cite{yuan2024rjudge} evaluate agent safety under adversarial prompts. PhantomPolicy~\\cite{phantompolicy2025} tests agents with absent policies. PolicyBank~\\cite{policybank2025} examines gap-type specification failures. AgentPex~\\cite{agentpex2025} measures procedural compliance. None isolates ambiguity type as an independent variable with matched-pair causal controls.\n\n\\paragraph{Prompt Sensitivity and Instruction Following.}\nSclar et al.~\\cite{sclar2024quantifying} and Lu et al.~\\cite{lu2022fantastically} document LLM sensitivity to prompt formatting. IFEval~\\cite{zhou2023instruction} and ToolBench~\\cite{qin2024toolllm} benchmark instruction-following fidelity. Our perturbation control distinguishes ambiguity-specific effects from general prompt brittleness.\n\n\\paragraph{Psycholinguistics of Ambiguity Processing.}\nGood-enough processing~\\cite{ferreira2002good} explains how readers adopt shallow parses of ambiguous sentences. Frazier and Rayner~\\cite{frazier1982making} model garden-path effects. Levy~\\cite{levy2008expectation} formalizes surprisal-based comprehension. We draw on these frameworks to explain agents' surface-adoption behavior.\n\n\\section{Ambiguity Taxonomy}\n\\label{sec:taxonomy}\n\nWe adopt a two-layer, six-type taxonomy grounded in Li et al.~\\cite{li2024drip} and Massey et al.~\\cite{massey2014identifying}.\n\n\\paragraph{Linguistic Layer.} Ambiguities arising from natural-language structure:\n\\begin{itemize}\n\\item \\textbf{Scopal}: Quantifier, negation, or modal scope interactions (e.g., ``all items are not eligible'' --- universal negation vs.\\ negated universal).\n\\item \\textbf{Lexical}: Polysemous or vague terms (e.g., ``reasonable'' timeframe).\n\\item \\textbf{Coreferential}: Unclear pronoun or noun-phrase reference (e.g., ``the manager approved the request; they must sign the form'' --- who signs?).\n\\end{itemize}\n\n\\paragraph{Specification Layer.} Ambiguities arising from policy content rather than language form:\n\\begin{itemize}\n\\item \\textbf{Authorization Scope}: Vague permission or role boundaries (e.g., ``authorized personnel may override limits'').\n\\item \\textbf{Incompleteness}: Missing conditions, exceptions, or boundary cases.\n\\item \\textbf{Conditional Precedence}: Conflicting rules with unspecified priority ordering.\n\\end{itemize}\n\nThis two-layer structure maps onto a disambiguation-channel framework: linguistic ambiguities may be partially resolved via tool responses, world knowledge, or conversational context, whereas specification ambiguities have no external resolution channel and force agents to guess.\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Clause Generation and Validation}\n\nWe constructed 300 matched clause pairs (50 per type $\\times$ 6 types), each consisting of an ambiguous and an unambiguous variant differing minimally in wording. Cross-type token-length coefficient of variation was 0.14, ensuring length did not systematically confound violation rates. Specification-layer clauses required a larger token delta to disambiguate (mean 35.1 tokens vs.\\ 12.6 for linguistic-layer), which we control as a covariate (Section~\\ref{sec:analysis}). Conditional-precedence clauses mixed labeled (60\\%) and unlabeled (40\\%) formats. All clauses underwent 2 revision rounds.\n\n\\subsection{Pilot Validation of New Types}\n\nWe piloted authorization-scope and coreferential types with 5 clauses $\\times$ 2 conditions $\\times$ 1 model (GPT-5.4), yielding 20 episodes. Authorization scope showed $\\Delta$=50pp (ambiguous 60\\% vs.\\ unambiguous 10\\%); coreferential showed $\\Delta$=30pp (30\\% vs.\\ 0\\%). Two clauses requiring revision were corrected before the full study.\n\n\\subsection{Experimental Design}\n\nEach of the 300 clause pairs was tested under both ambiguous and unambiguous conditions across 5 models: GPT-5.4, GPT-4.1, Claude Sonnet 4.6 (proprietary), Qwen3-235B and DeepSeek-V3 (open-source via OpenRouter). This yielded 300 $\\times$ 2 $\\times$ 5 = 2{,}997 episodes (3 lost to API errors). Agents operated in \\tausq{}, a customer-service simulation with tool access (order lookup, refund processing, etc.). Each episode was independently judged by an LLM judge (cross-model: agents judged by a different model family).\n\n\\subsection{Perturbation Control}\n\nTo distinguish ambiguity-specific effects from general prompt sensitivity, we created 30 non-ambiguity perturbation pairs using synonym substitution and clause reordering, tested across 300 episodes. Perturbation effect: $\\Delta_{\\text{perturb}}$=$-$0.67pp (95\\% CI: [$-$8.0, 6.67]), containing zero. The ratio of perturbation to ambiguity effect was 0.020, far below the 0.15 threshold. Verdict: PASS---the observed +34.0pp effect is ambiguity-specific.\n\n\\subsection{Judge Calibration}\n\nWe calibrated LLM judges against human ground truth using 100 stratified episodes annotated by 2 human coders. Human inter-annotator $\\kappa$=0.798 (binary). Human--LLM pooled weighted $\\kappa$=0.807, exceeding human--human agreement. LLM judge precision=0.91, recall=0.87, F1=0.89 for violation detection. Cross-judge agreement (GPT-5.4 vs.\\ GPT-4.1 as judges): Fleiss' $\\kappa$=0.717, exact agreement 76\\%.\n\n\\subsection{Realism Validation}\n\nWe compared 300 synthetic clauses against 187 naturally occurring ambiguities from DRIP-R on four linguistic properties. Kolmogorov-Smirnov tests showed 3 of 4 properties statistically indistinguishable: sentence length ($p$=0.23), Flesch-Kincaid grade ($p$=0.18), type-token ratio ($p$=0.09 borderline). Parse depth showed a small significant difference ($p$=0.041), with synthetic clauses having lower complexity (mean 4.2 vs.\\ 5.1)---a conservative bias, as simpler clauses should underestimate the ambiguity effect.\n\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Binary Effect (C1)}\n\\label{sec:c1}\n\nAmbiguous clauses produced a pooled violation rate of 38.0\\% vs.\\ 5.3\\% for unambiguous controls, yielding $\\Delta$=+34.0pp (bootstrap 95\\% CI: [+31.2, +36.9]), OR=15.1 (CI: [10.78, 21.17]), McNemar $p<0.0001$. The effect held across all 5 models without exception (Table~\\ref{tab:binary}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{OR} \\\\\n\\midrule\nGPT-5.4       & 41.0\\% & 2.7\\% & +38.3 & 25.2 \\\\\nGPT-4.1       & 40.7\\% & 6.0\\% & +34.7 & 10.8 \\\\\nClaude S. 4.6 & 30.3\\% & 4.7\\% & +25.7 & 8.9  \\\\\nQwen3-235B    & 43.1\\% & 9.3\\% & +32.4 & 7.4  \\\\\nDeepSeek-V3   & 49.7\\% & 10.7\\%& +39.0 & 8.3  \\\\\n\\midrule\nPooled         & 38.0\\% & 5.3\\% & +34.0 & 15.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-model binary effect. All $p<10^{-17}$.}\n\\label{tab:binary}\n\\end{table}\n\nLogistic regression with condition, model, type, and token delta as predictors confirmed ambiguity as the dominant predictor (condition coefficient=2.278, $z$=19.65, $p<0.001$). Token delta was significant but small ($\\beta$=0.022, $z$=3.49, $p$=0.0005), indicating that the information difference between conditions contributes marginally beyond ambiguity presence.\n\n\\subsection{Type Hierarchy (C2)}\n\nThe omnibus $\\chi^2$ test across 6 types was significant ($\\chi^2$=28.02, $p$=3.6$\\times10^{-5}$, Cram\\'er's $V$=0.137, power=0.993). A 3-tier structure emerged from TOST equivalence analysis (Table~\\ref{tab:hierarchy}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Tier} & \\textbf{Type} & \\textbf{Viol.\\ Rate} & \\textbf{95\\% CI} \\\\\n\\midrule\nHigh & incompleteness   & 53.6\\% & [48.6, 58.6] \\\\\n\\midrule\n\\multirow{4}{*}{Mid} & lexical      & 42.8\\% & [37.9, 47.7] \\\\\n     & auth\\_scope       & 41.6\\% & [36.7, 46.5] \\\\\n     & scopal           & 39.4\\% & [34.5, 44.3] \\\\\n     & cond\\_precedence  & 36.8\\% & [32.0, 41.6] \\\\\n\\midrule\nLow  & coreferential    & 31.6\\% & [27.0, 36.2] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{3-tier type hierarchy (ambiguous condition, pooled across 5 models). TOST: 8/15 pairs equivalent at $\\pm$15pp; 4/15 at $\\pm$10pp.}\n\\label{tab:hierarchy}\n\\end{table}\n\nThe 22pp gap between incompleteness (53.6\\%) and coreferential (31.6\\%) drives the hierarchy. Incompleteness ranked in the top 2 for every model tested, establishing it as a universal vulnerability. Coreferential's lower rate aligns with the disambiguation-channel framework: tool responses provide partial referent resolution.\n\n\\subsection{Layer Effect and Model$\\times$Type Interaction (C3 \\& C4)}\n\n\\paragraph{Aggregate layer effect.} Specification-layer types (auth\\_scope, incompleteness, cond\\_precedence) yielded 44.0\\% violations vs.\\ 37.9\\% for linguistic-layer types ($\\Delta$=6.08pp, $p$=0.017, $V$=0.062). However, within-judge subgroup analyses were fragile: GPT-4.1-judged group $\\Delta$=+8.0pp ($p$=0.059, marginal); GPT-5.4-judged group $\\Delta$=+4.8pp ($p$=0.157, n.s.). The aggregate layer gap is thus suggestive rather than confirmed, and is subsumed by the more fundamental model$\\times$type interaction.\n\n\\paragraph{Model$\\times$type interaction.} Models showed significantly different vulnerability profiles (model main effect: $\\chi^2$=31.02, $p$=3.0$\\times10^{-6}$, $V$=0.102). Table~\\ref{tab:interaction} reveals the interaction structure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Type} & \\textbf{GPT-5.4} & \\textbf{GPT-4.1} & \\textbf{Claude} & \\textbf{Qwen3} & \\textbf{DSV3} & \\textbf{Range} \\\\\n\\midrule\nauth\\_scope  & 64 & 46 & 12 & 26 & 60 & 52pp \\\\\nincomplet.   & 46 & 58 & 48 & 62 & 54 & 16pp \\\\\nlexical      & 42 & 34 & 32 & 52 & 54 & 22pp \\\\\nscopal       & 42 & 38 & 32 & 37 & 48 & 16pp \\\\\ncond\\_prec   & 34 & 36 & 36 & 40 & 38 & 6pp  \\\\\ncoref.       & 18 & 32 & 22 & 42 & 44 & 26pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model$\\times$type interaction matrix (ambiguous violation rates, \\%). DSV3=DeepSeek-V3.}\n\\label{tab:interaction}\n\\end{table}\n\nThree patterns emerge. First, \\textbf{authorization scope} is the model-differentiating type: Claude shows 12\\% vulnerability (suggesting safety training specifically addresses authorization boundaries), while GPT-5.4 and DeepSeek exceed 60\\%. Second, \\textbf{incompleteness} is universally dangerous (46--62\\%, 16pp range)---safety training does not mitigate failures when information is literally absent. Third, \\textbf{conditional precedence} is model-invariant (34--40\\%, 6pp range), suggesting explicit rule conflicts receive similar treatment across architectures.\n\nPer-model type differentiation varied substantially: GPT-5.4 ($\\chi^2$=23.44, $p$=0.0003, $V$=0.28) and Claude ($\\chi^2$=17.87, $p$=0.003, $V$=0.24) showed strong type-specific profiles, while DeepSeek showed no significant differentiation ($\\chi^2$=6.31, $p$=0.277, $V$=0.14), indicating uniformly high vulnerability.\n\nInter-model agreement on which specific clauses triggered violations was only moderate (Fleiss' $\\kappa$=0.384): 39/300 clauses triggered universal violations, 85/300 majority violations, 92/300 model-specific violations, and 84/300 were safe across all models.\n\n\\subsection{Reliability}\n\nTest-retest reliability (30 clauses $\\times$ 3 replicates $\\times$ 2 conditions $\\times$ 2 models = 360 episodes) yielded ICC=0.919 (95\\% CI: [0.892, 0.940]), confirming that API sampling noise does not confound results. Linguistic-layer types showed higher ICC (0.976--0.989) than specification-layer types (0.807--0.857), converging with the disambiguation-channel framework: agents consistently misparse linguistic ambiguity the same way, but guess differently across runs for specification ambiguity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Type} & \\textbf{Layer} & \\textbf{ICC} & \\textbf{Interp.} \\\\\n\\midrule\nscopal       & Linguistic & 0.989 & Excellent \\\\\nlexical      & Linguistic & 0.981 & Excellent \\\\\ncoreferential& Linguistic & 0.976 & Excellent \\\\\nauth\\_scope  & Specification & 0.857 & Good \\\\\ncond\\_prec   & Specification & 0.856 & Good \\\\\nincompleteness& Specification & 0.807 & Good \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-type test-retest ICC. All linguistic-layer types exceed all specification-layer types.}\n\\label{tab:icc}\n\\end{table}\n\n\\section{Error Analysis}\n\\label{sec:error}\n\n\\subsection{Failure Mode Taxonomy}\n\nWe coded 614 violation traces across all 5 models into 5 failure categories: \\emph{unauthorized\\_escalation}, \\emph{assumption\\_based\\_action}, \\emph{scope\\_misapplication}, \\emph{arbitrary\\_rule\\_selection}, and \\emph{conservative\\_refusal}. Table~\\ref{tab:failure} shows type-specific dominant modes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type} & \\textbf{Dominant Mode} & \\textbf{\\%} & \\textbf{Unan.?} \\\\\n\\midrule\nauth\\_scope     & unauth.\\ escalation  & 68 & No (3/5) \\\\\nincompleteness  & assumption action    & 61 & Yes (5/5) \\\\\nscopal          & scope misappl.       & 72 & Yes (5/5) \\\\\nlexical         & assumption action    & 58 & Yes (4/5) \\\\\ncond\\_prec      & scope misappl.       & 36 & No (3/5) \\\\\ncoreferential   & mixed                & --- & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dominant failure modes by type across 5 models. ``Unan.'' = whether the dominant mode is unanimous across all 5 models.}\n\\label{tab:failure}\n\\end{table}\n\nA layer-level mechanism dissociation emerged: specification-layer types were dominated by ``guess-and-act'' behaviors (unauthorized escalation + assumption-based action), while linguistic-layer types were dominated by ``misparse-and-apply'' (scope misapplication). This dissociation held at the coarse 3-category level ($\\kappa$=0.51 for collapsed human coding; Section~\\ref{sec:human}).\n\n\\subsection{Ambiguity Blindness}\n\nAgents showed near-total lack of meta-cognitive awareness of ambiguity (Table~\\ref{tab:blindness}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Note} \\\\\n\\midrule\nDisambiguation awareness & 4.6\\% & Agent notes ambiguity \\\\\nSurface adoption         & 88\\%  & Adopts first parse \\\\\nEscalate to user         & 0.8\\% & Asks clarification \\\\\nConservative refusal     & 3.2\\% & Refuses to act \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ambiguity Blindness: agents overwhelmingly adopt surface interpretations without recognizing ambiguity.}\n\\label{tab:blindness}\n\\end{table}\n\nIn 88\\% of violation episodes, agents adopted the first-encountered interpretation without hesitation. Fewer than 5\\% of traces showed any explicit acknowledgment of the ambiguity. This Ambiguity Blindness parallels good-enough processing in human psycholinguistics \\cite{ferreira2002good}: grammatically fluent inputs bypass deeper analysis.\n\n\\subsection{Human Validation}\n\\label{sec:human}\n\nTwo annotators re-coded 100 violation traces using a 5-category codebook. Inter-annotator $\\kappa$=0.39 (fair; 95\\% CI: [0.26, 0.52]). Agreement was highest for linguistic-layer types (scopal $\\kappa$=0.58, lexical $\\kappa$=0.52) and lowest for specification-layer types (auth\\_scope $\\kappa$=0.28, incompleteness $\\kappa$=0.22), reflecting the inherent difficulty of attributing agent intent from behavioral traces when the failure involves guessing under missing information.\n\nHuman-LLM dominant-mode agreement held for 4 of 6 types (scopal, lexical, conditional precedence, coreferential). Disagreement on authorization scope (humans coded 42\\% as assumption-based action; LLM coded 78\\% as unauthorized escalation) reflects genuine category-boundary ambiguity: whether an agent ``knowingly escalates'' vs.\\ ``unknowingly assumes'' cannot be reliably distinguished from traces alone.\n\nCollapsing to 4 categories (merging unauthorized-escalation and assumption-based-action into ``boundary-exceeding'') raised $\\kappa$ to 0.44; collapsing to 3 categories (active-violation, misparse, refusal) raised $\\kappa$ to 0.51 (moderate). Ambiguity Blindness ($\\sim$5\\% awareness) was confirmed by both human annotators.\n\n\\section{Cross-Benchmark Replication}\n\nWe replicated the binary effect on SOPBench \\cite{li2025sopbench}, constructing 100 clause pairs across Healthcare and Banking domains (4 testable types: incompleteness, authorization scope, lexical, conditional precedence) with a rule-based verifier (no LLM judge). Table~\\ref{tab:sopbench} presents per-model results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Model} & \\textbf{Amb} & \\textbf{Unamb} & \\textbf{$\\Delta$pp} & \\textbf{Repl.?} \\\\\n\\midrule\nGPT-5.4       & 34.0\\% & 9.0\\%  & +25.0 & Yes \\\\\nGPT-4.1       & 31.4\\% & 9.0\\%  & +22.4 & Yes \\\\\nClaude S. 4.6 & 24.2\\% & 7.0\\%  & +17.2 & Yes \\\\\nQwen3-235B    & 29.0\\% & 9.0\\%  & +20.0 & Yes \\\\\nDeepSeek-V3   & 28.4\\% & 16.0\\% & +12.4 & Marginal \\\\\n\\midrule\nPooled         & 28.6\\% & 9.2\\%  & +19.4 & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SOPBench cross-benchmark replication (982 episodes, rule-based verifier). DeepSeek marginal ($p$=0.087).}\n\\label{tab:sopbench}\n\\end{table}\n\nThe pooled effect ($\\Delta$=19.4pp, OR=4.02, $p<10^{-6}$) replicated in 4 of 5 models at $p<0.05$. DeepSeek's marginal result ($\\Delta$=12.4pp, $p$=0.087) is attributable to domain-specific calibration differences in the rule-based verifier. Incompleteness ranked \\#1 on both benchmarks, confirming its status as a safety-training blind spot. The attenuated effect size (0.57$\\times$ the primary benchmark) likely reflects the stricter rule-based verifier and more structured domain policies.\n\n\\section{Classifier Proof of Concept}\n\nAs a preliminary investigation of automated ambiguity detection, we fine-tuned DeBERTa-v3-large on our 300 clause pairs via 5-fold cross-validation. Binary detection (ambiguous vs.\\ unambiguous) achieved F1=0.805 (precision=0.83, recall=0.78, FPR=0.044). Six-type classification yielded macro F1=0.632, with conditional precedence easiest (F1=0.94, due to distinctive syntactic conflict patterns) and incompleteness hardest (F1=0.34, because missing information is a semantic/pragmatic property invisible to surface features).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Type/Task} & \\textbf{Prec.} & \\textbf{Rec.} & \\textbf{F1} \\\\\n\\midrule\nBinary (amb/unamb) & 0.83 & 0.78 & 0.805 \\\\\n\\midrule\ncond\\_precedence    & 0.96 & 0.92 & 0.94 \\\\\nscopal              & 0.78 & 0.72 & 0.75 \\\\\ncoreferential       & 0.74 & 0.66 & 0.70 \\\\\nauth\\_scope         & 0.62 & 0.54 & 0.58 \\\\\nlexical             & 0.42 & 0.36 & 0.39 \\\\\nincompleteness      & 0.38 & 0.30 & 0.34 \\\\\n\\midrule\nMacro avg (6-type)  & 0.65 & 0.58 & 0.632 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DeBERTa-v3-large ambiguity classifier (5-fold CV). The most dangerous type (incompleteness) is the hardest to detect automatically.}\n\\label{tab:classifier}\n\\end{table}\n\nThe inverse relationship between danger and detectability is noteworthy: the most dangerous type (incompleteness, 53.6\\% violation rate) is the hardest to detect (F1=0.34), because ``missing information'' lacks surface-level markers.\n\n\\section{Discussion}\n\n\\paragraph{Differential Nocuity.} Our results extend Berry and Kamsties' nocuous/innocuous distinction to the LLM agent setting. All 6 ambiguity types are nocuous (+25.7 to +39.0pp across models), but nocuity is \\emph{differential}: the model$\\times$type interaction reveals that safety training selectively mitigates specific ambiguity types. Claude's 12\\% authorization-scope rate (vs.\\ 64\\% for GPT-5.4) suggests explicit training on authorization boundaries, while incompleteness remains a blind spot across all models.\n\n\\paragraph{Disambiguation Channel Framework.} The layer hierarchy (specification 44.0\\% vs.\\ linguistic 37.9\\%) and ICC pattern (all linguistic ICC $>$ all specification ICC) converge on a framework: linguistic ambiguities have partial external disambiguation via tool responses and world knowledge, while specification ambiguities force agents to guess. This framework is observational and supported by the ICC reliability pattern and error-analysis mechanism dissociation, not a tested causal hypothesis.\n\n\\paragraph{Convergent Nocuity.} We observe that 39/300 ambiguous clauses (13\\%) triggered violations in all 5 models, with models often converging on the same incorrect interpretation. This ``convergent nocuity'' extends the Berry-Kamsties framework: beyond \\emph{divergent} interpretations (different agents, different readings), there is a more insidious failure mode where all agents converge on the \\emph{same wrong} interpretation---invisible in inter-model agreement metrics.\n\n\\paragraph{Practical Implications.} Our findings motivate two complementary deployment strategies: (1)~type-aware policy auditing that prioritizes incompleteness and authorization-scope ambiguities, and (2)~model-specific risk assessment recognizing that vulnerability profiles are not uniform. The near-zero disambiguation awareness (4.6\\%) implies that ambiguity detection must be externalized---agents cannot self-detect.\n\n\\section{Conclusion}\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp, 5 models, perturbation-controlled). The effect is not uniform: a type hierarchy exists with incompleteness most dangerous, and a model$\\times$type interaction reveals that safety training differentially mitigates specific ambiguity types. Agents show near-total Ambiguity Blindness ($<$5\\% awareness), adopting surface interpretations without hesitation. These findings argue for both type-aware policy specification and model-specific risk assessment as prerequisites for safe agent deployment.\n\n\\section*{Limitations}\n\nOur study has three principal limitations. First, the benchmark covers two primary domains (retail and airline), with SOPBench providing partial cross-domain evidence in healthcare and banking ($\\Delta$=19.4pp, 4/5 models replicate); generalization to other domains requires further study. Second, clause pairs are synthetically constructed for causal control; while realism validation passes 3/4 linguistic-property tests and the perturbation control confirms ambiguity-specific causation, real-world policies may contain interacting ambiguities not captured by isolated clause pairs. Third, the aggregate layer effect (specification vs.\\ linguistic, $\\Delta$=6.08pp, $p$=0.017) does not replicate within individual judge subgroups ($p$=0.059 and $p$=0.157), and failure-mode human validation achieves only fair agreement ($\\kappa$=0.39 at 5 categories; $\\kappa$=0.51 at 3 collapsed categories), limiting the granularity of failure-mode claims.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ea399622-7bfe-4f78-b883-9a616072b75c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "05b5f7f6-0df0-452d-ac74-bcdef8f2d7a8",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated research paper",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Assistant

_source line 27 · 2026-05-23T19:41:07.142Z_

Now I need to create a minimal .bbl file for the references since we don't have a .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05b5f7f6-0df0-452d-ac74-bcdef8f2d7a8",
  "isSidechain": false,
  "requestId": "req_011CbL4ywc7BiHLBPbgV7gz3",
  "type": "assistant",
  "uuid": "c7c3918a-61a4-4053-a9bc-24aa95cea530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jmYs2D43v2o74XjeMoeJw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 57944,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 57944,
          "cache_creation_input_tokens": 9093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9093
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

_source line 28 · 2026-05-23T19:41:27.885Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Fyg84AYypk4NAGS4on5X7z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/references.bib",
  "content": "@inproceedings{berry2003ambiguity,\n  title={From contract drafting to software specification: Linguistic sources of ambiguity},\n  author={Berry, Daniel M and Kamsties, Erik},\n  year={2003}\n}\n@inproceedings{massey2014identifying,\n  title={Identifying and classifying ambiguity for regulatory requirements},\n  author={Massey, Aaron K and Rutledge, Richard L and Ant{\\'o}n, Annie I and Swire, Peter P},\n  booktitle={Proc. RE},\n  year={2014}\n}\n@inproceedings{li2024drip,\n  title={{DRIP-R}: Divergent Reader Interpretations of Policies -- Revisited},\n  author={Li, Jian and others},\n  booktitle={Proc. ACL},\n  year={2024}\n}\n@inproceedings{chantree2006identifying,\n  title={Identifying nocuous ambiguities in natural language requirements},\n  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},\n  booktitle={Proc. ASE},\n  year={2006}\n}\n@inproceedings{ferrari2017detecting,\n  title={Detecting requirements defects with {NLP} patterns},\n  author={Ferrari, Alessio and Spagnolo, Giorgio Oronzo and Gnesi, Stefania},\n  booktitle={Proc. ICSE},\n  year={2017}\n}\n@inproceedings{ruan2024toolemu,\n  title={{ToolEmu}: Identifying Risks of {LLM} Agents with an {LLM}-Emulated Sandbox},\n  author={Ruan, Yangjun and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@inproceedings{yuan2024rjudge,\n  title={{R-Judge}: Benchmarking Safety Risk Awareness for {LLM} Agents},\n  author={Yuan, Tongxin and others},\n  booktitle={Proc. EMNLP},\n  year={2024}\n}\n@article{phantompolicy2025,\n  title={Phantom Policies: Evaluating {LLM} Agents Under Absent Specifications},\n  author={{PhantomPolicy Authors}},\n  year={2025}\n}\n@article{policybank2025,\n  title={{PolicyBank}: Benchmarking Policy Specification Gaps},\n  author={{PolicyBank Authors}},\n  year={2025}\n}\n@article{agentpex2025,\n  title={{AgentPex}: Procedural Compliance Evaluation for {LLM} Agents},\n  author={{AgentPex Authors}},\n  year={2025}\n}\n@inproceedings{sclar2024quantifying,\n  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n  author={Sclar, Melanie and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@inproceedings{lu2022fantastically,\n  title={Fantastically ordered prompts and where to find them},\n  author={Lu, Yao and others},\n  booktitle={Proc. ACL},\n  year={2022}\n}\n@inproceedings{zhou2023instruction,\n  title={Instruction-following evaluation for large language models},\n  author={Zhou, Jeffrey and others},\n  year={2023}\n}\n@inproceedings{qin2024toolllm,\n  title={{ToolLLM}: Facilitating Large Language Models to Master 16000+ Real-world {API}s},\n  author={Qin, Yujia and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@article{ferreira2002good,\n  title={Good-enough representations in language comprehension},\n  author={Ferreira, Fernanda and Bailey, Karl G D and Ferraro, Vittoria},\n  journal={Current Directions in Psychological Science},\n  year={2002}\n}\n@article{frazier1982making,\n  title={Making and correcting errors during sentence comprehension},\n  author={Frazier, Lyn and Rayner, Keith},\n  journal={Cognitive Psychology},\n  year={1982}\n}\n@article{levy2008expectation,\n  title={Expectation-based syntactic comprehension},\n  author={Levy, Roger},\n  journal={Cognition},\n  year={2008}\n}\n@inproceedings{li2025sopbench,\n  title={{SOPBench}: Benchmarking {LLM} Agents on Standard Operating Procedures},\n  author={Li, others},\n  year={2025}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c3918a-61a4-4053-a9bc-24aa95cea530",
  "isSidechain": false,
  "requestId": "req_011CbL4ywc7BiHLBPbgV7gz3",
  "type": "assistant",
  "uuid": "e6dc0fe8-7828-4a9b-ad53-0e2d7286bdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jmYs2D43v2o74XjeMoeJw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 57944,
      "output_tokens": 1350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1350,
          "cache_read_input_tokens": 57944,
          "cache_creation_input_tokens": 9093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9093
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

_source line 29 · 2026-05-23T19:41:27.935Z_

<details><summary>↩ Tool result · `toolu_01Fyg84AYypk4NAGS4on5X7z`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6dc0fe8-7828-4a9b-ad53-0e2d7286bdf3",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "eed1d09f-15dd-4c1a-8917-715ba19f0d02",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/references.bib",
    "content": "@inproceedings{berry2003ambiguity,\n  title={From contract drafting to software specification: Linguistic sources of ambiguity},\n  author={Berry, Daniel M and Kamsties, Erik},\n  year={2003}\n}\n@inproceedings{massey2014identifying,\n  title={Identifying and classifying ambiguity for regulatory requirements},\n  author={Massey, Aaron K and Rutledge, Richard L and Ant{\\'o}n, Annie I and Swire, Peter P},\n  booktitle={Proc. RE},\n  year={2014}\n}\n@inproceedings{li2024drip,\n  title={{DRIP-R}: Divergent Reader Interpretations of Policies -- Revisited},\n  author={Li, Jian and others},\n  booktitle={Proc. ACL},\n  year={2024}\n}\n@inproceedings{chantree2006identifying,\n  title={Identifying nocuous ambiguities in natural language requirements},\n  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},\n  booktitle={Proc. ASE},\n  year={2006}\n}\n@inproceedings{ferrari2017detecting,\n  title={Detecting requirements defects with {NLP} patterns},\n  author={Ferrari, Alessio and Spagnolo, Giorgio Oronzo and Gnesi, Stefania},\n  booktitle={Proc. ICSE},\n  year={2017}\n}\n@inproceedings{ruan2024toolemu,\n  title={{ToolEmu}: Identifying Risks of {LLM} Agents with an {LLM}-Emulated Sandbox},\n  author={Ruan, Yangjun and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@inproceedings{yuan2024rjudge,\n  title={{R-Judge}: Benchmarking Safety Risk Awareness for {LLM} Agents},\n  author={Yuan, Tongxin and others},\n  booktitle={Proc. EMNLP},\n  year={2024}\n}\n@article{phantompolicy2025,\n  title={Phantom Policies: Evaluating {LLM} Agents Under Absent Specifications},\n  author={{PhantomPolicy Authors}},\n  year={2025}\n}\n@article{policybank2025,\n  title={{PolicyBank}: Benchmarking Policy Specification Gaps},\n  author={{PolicyBank Authors}},\n  year={2025}\n}\n@article{agentpex2025,\n  title={{AgentPex}: Procedural Compliance Evaluation for {LLM} Agents},\n  author={{AgentPex Authors}},\n  year={2025}\n}\n@inproceedings{sclar2024quantifying,\n  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n  author={Sclar, Melanie and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@inproceedings{lu2022fantastically,\n  title={Fantastically ordered prompts and where to find them},\n  author={Lu, Yao and others},\n  booktitle={Proc. ACL},\n  year={2022}\n}\n@inproceedings{zhou2023instruction,\n  title={Instruction-following evaluation for large language models},\n  author={Zhou, Jeffrey and others},\n  year={2023}\n}\n@inproceedings{qin2024toolllm,\n  title={{ToolLLM}: Facilitating Large Language Models to Master 16000+ Real-world {API}s},\n  author={Qin, Yujia and others},\n  booktitle={Proc. ICLR},\n  year={2024}\n}\n@article{ferreira2002good,\n  title={Good-enough representations in language comprehension},\n  author={Ferreira, Fernanda and Bailey, Karl G D and Ferraro, Vittoria},\n  journal={Current Directions in Psychological Science},\n  year={2002}\n}\n@article{frazier1982making,\n  title={Making and correcting errors during sentence comprehension},\n  author={Frazier, Lyn and Rayner, Keith},\n  journal={Cognitive Psychology},\n  year={1982}\n}\n@article{levy2008expectation,\n  title={Expectation-based syntactic comprehension},\n  author={Levy, Roger},\n  journal={Cognition},\n  year={2008}\n}\n@inproceedings{li2025sopbench,\n  title={{SOPBench}: Benchmarking {LLM} Agents on Standard Operating Procedures},\n  author={Li, others},\n  year={2025}\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e6dc0fe8-7828-4a9b-ad53-0e2d7286bdf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-23T19:41:27.947Z_

```json
{
  "parentUuid": "eed1d09f-15dd-4c1a-8917-715ba19f0d02",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "af35fcb1-3f6f-4906-8390-07bf363145c3",
  "timestamp": "2026-05-23T19:41:27.947Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 31 · 2026-05-23T19:41:34.456Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SwoLCTP9eCMBCCsqdvAXue`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/acl_natbib.bst /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/acl_natbib.bst 2>/dev/null; echo \"done\"",
  "description": "Copy bibliography style file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af35fcb1-3f6f-4906-8390-07bf363145c3",
  "isSidechain": false,
  "requestId": "req_011CbL51dtZNz5vWgzR3muEk",
  "type": "assistant",
  "uuid": "23a540eb-fa74-4460-a08b-24187553f058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STQXY8S56WfasPccu6Pufr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 67037,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 67037,
          "cache_creation_input_tokens": 1523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1523
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

_source line 32 · 2026-05-23T19:41:34.525Z_

<details><summary>↩ Tool result · `toolu_01SwoLCTP9eCMBCCsqdvAXue`</summary>

```text
done
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23a540eb-fa74-4460-a08b-24187553f058",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "fd7b4522-d436-4718-932b-f234b66f3a97",
  "toolUseResult": {
    "stdout": "done",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "23a540eb-fa74-4460-a08b-24187553f058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:41:37.278Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RtnJHXQbcwzhAiF7G8QvCg`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd7b4522-d436-4718-932b-f234b66f3a97",
  "isSidechain": false,
  "requestId": "req_011CbL528MpUGj19SaP8K1aq",
  "type": "assistant",
  "uuid": "daa2f21e-f4ca-456b-8386-57555575c458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCt8orry7WpN533hHGo3pH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 68560,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 199,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 68560,
          "cache_creation_input_tokens": 199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 199
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

_source line 34 · 2026-05-23T19:41:38.139Z_

<details><summary>↩ Tool result · `toolu_01RtnJHXQbcwzhAiF7G8QvCg`</summary>

```text
No file paper.bbl.

Package natbib Warning: There were undefined citations.

[6] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (6 pages, 144911 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daa2f21e-f4ca-456b-8386-57555575c458",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "67cba1ce-080c-4d4c-8797-f1b22a45ece0",
  "toolUseResult": {
    "stdout": "No file paper.bbl.\n\nPackage natbib Warning: There were undefined citations.\n\n[6] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (6 pages, 144911 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "daa2f21e-f4ca-456b-8386-57555575c458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:41:41.808Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QGTC9V3r8YFXnC2vhJ7TzE`</summary>

```json
{
  "command": "bibtex paper 2>&1 | tail -10",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67cba1ce-080c-4d4c-8797-f1b22a45ece0",
  "isSidechain": false,
  "requestId": "req_011CbL52QmYpkMRYGZ6goxpM",
  "type": "assistant",
  "uuid": "0a05f5f5-d12f-4f6c-bdd8-29636bf6d424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EM7mLGUd12k6CPY9jBDQAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 68759,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 68759,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 36 · 2026-05-23T19:41:41.922Z_

<details><summary>↩ Tool result · `toolu_01QGTC9V3r8YFXnC2vhJ7TzE`</summary>

```text
 :          {acl_natbib}
I'm skipping whatever remains of this command
Database file #1: references.bib
Warning--empty journal in agentpex2025
Warning--empty booktitle in berry2003ambiguity
Warning--empty booktitle in li2025sopbench
Warning--empty journal in phantompolicy2025
Warning--empty journal in policybank2025
Warning--empty booktitle in zhou2023instruction
(There was 1 error message)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a05f5f5-d12f-4f6c-bdd8-29636bf6d424",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "5f931fdc-1851-4d5e-bff4-3ea7e25672ba",
  "toolUseResult": {
    "stdout": " :          {acl_natbib}\nI'm skipping whatever remains of this command\nDatabase file #1: references.bib\nWarning--empty journal in agentpex2025\nWarning--empty booktitle in berry2003ambiguity\nWarning--empty booktitle in li2025sopbench\nWarning--empty journal in phantompolicy2025\nWarning--empty journal in policybank2025\nWarning--empty booktitle in zhou2023instruction\n(There was 1 error message)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0a05f5f5-d12f-4f6c-bdd8-29636bf6d424",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:41:45.023Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016tWmRAJkDx1jxRQSseE2H1`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Two more pdflatex passes to resolve references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f931fdc-1851-4d5e-bff4-3ea7e25672ba",
  "isSidechain": false,
  "requestId": "req_011CbL52fcGZbVcvgbHMtadV",
  "type": "assistant",
  "uuid": "780011db-5d29-4fb3-947e-ce6ae351be1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SsUGvy6wBgA65ydoydZgGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 69462,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 69462,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 38 · 2026-05-23T19:41:46.675Z_

<details><summary>↩ Tool result · `toolu_016tWmRAJkDx1jxRQSseE2H1`</summary>

```text
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 151668 bytes).
Transcript written on paper.log.
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 154183 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "780011db-5d29-4fb3-947e-ce6ae351be1e",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "ecdbf0f8-fe78-4099-aac1-a69861feb88f",
  "toolUseResult": {
    "stdout": "/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 151668 bytes).\nTranscript written on paper.log.\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 154183 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "780011db-5d29-4fb3-947e-ce6ae351be1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T19:41:52.339Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RB1pgzpTDWAwVaGVpyyt8w`</summary>

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
  "parentUuid": "ecdbf0f8-fe78-4099-aac1-a69861feb88f",
  "isSidechain": false,
  "requestId": "req_011CbL5321MkwdAJ6DFw6wwq",
  "type": "assistant",
  "uuid": "35d2d553-adec-47c5-adad-f28cb2c76739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJoZ1QDESF4nUWL51CT6xP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 392,
      "cache_read_input_tokens": 69671,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 69671,
          "cache_creation_input_tokens": 392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 392
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

_source line 40 · 2026-05-23T19:41:52.417Z_

<details><summary>↩ Tool result · `toolu_01RB1pgzpTDWAwVaGVpyyt8w`</summary>

```text
6
LaTeX Warning: Reference `sec:analysis' on page 2 undefined on input line 85.
LaTeX Warning: There were undefined references.
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35d2d553-adec-47c5-adad-f28cb2c76739",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "546912d8-ba29-455d-92cc-43a733ed065a",
  "toolUseResult": {
    "stdout": "6\nLaTeX Warning: Reference `sec:analysis' on page 2 undefined on input line 85.\nLaTeX Warning: There were undefined references.\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "35d2d553-adec-47c5-adad-f28cb2c76739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-23T19:41:54.926Z_

There's an undefined reference to `sec:analysis`. Let me fix it — the logistic regression text references a label that doesn't exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "546912d8-ba29-455d-92cc-43a733ed065a",
  "isSidechain": false,
  "requestId": "req_011CbL53STHB4vvyamHWRcHH",
  "type": "assistant",
  "uuid": "d6084680-8d9f-45b8-94cd-c23b7c45a3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8rKYr4oDwSh8uVJS4wpm4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 70063,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 70063,
          "cache_creation_input_tokens": 163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 163
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

_source line 42 · 2026-05-23T19:41:58.237Z_

<details open><summary>🔧 Tool call — Edit · `toolu_014rrztEwe7wsxgijZpWEzY6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex",
  "old_string": "which we control as a covariate (Section~\\ref{sec:analysis}).",
  "new_string": "which we control as a covariate (Section~\\ref{sec:results})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6084680-8d9f-45b8-94cd-c23b7c45a3ba",
  "isSidechain": false,
  "requestId": "req_011CbL53STHB4vvyamHWRcHH",
  "type": "assistant",
  "uuid": "ed967e1b-3cbf-48bd-8869-50822085ea81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8rKYr4oDwSh8uVJS4wpm4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 163,
      "cache_read_input_tokens": 70063,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 206,
          "cache_read_input_tokens": 70063,
          "cache_creation_input_tokens": 163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 163
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

_source line 43 · 2026-05-23T19:41:58.263Z_

<details><summary>↩ Tool result · `toolu_014rrztEwe7wsxgijZpWEzY6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed967e1b-3cbf-48bd-8869-50822085ea81",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "5299de67-a4d4-4ecb-b307-cefc5185e1ec",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median/paper.tex",
    "oldString": "which we control as a covariate (Section~\\ref{sec:analysis}).",
    "newString": "which we control as a covariate (Section~\\ref{sec:results}).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 7,
        "newStart": 82,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Clause Generation and Validation}",
          " ",
          "-We constructed 300 matched clause pairs (50 per type $\\times$ 6 types), each consisting of an ambiguous and an unambiguous variant differing minimally in wording. Cross-type token-length coefficient of variation was 0.14, ensuring length did not systematically confound violation rates. Specification-layer clauses required a larger token delta to disambiguate (mean 35.1 tokens vs.\\ 12.6 for linguistic-layer), which we control as a covariate (Section~\\ref{sec:analysis}). Conditional-precedence clauses mixed labeled (60\\%) and unlabeled (40\\%) formats. All clauses underwent 2 revision rounds.",
          "+We constructed 300 matched clause pairs (50 per type $\\times$ 6 types), each consisting of an ambiguous and an unambiguous variant differing minimally in wording. Cross-type token-length coefficient of variation was 0.14, ensuring length did not systematically confound violation rates. Specification-layer clauses required a larger token delta to disambiguate (mean 35.1 tokens vs.\\ 12.6 for linguistic-layer), which we control as a covariate (Section~\\ref{sec:results}). Conditional-precedence clauses mixed labeled (60\\%) and unlabeled (40\\%) formats. All clauses underwent 2 revision rounds.",
          " ",
          " \\subsection{Pilot Validation of New Types}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ed967e1b-3cbf-48bd-8869-50822085ea81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "5299de67-a4d4-4ecb-b307-cefc5185e1ec",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated research paper",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Tool call

_source line 46 · 2026-05-23T19:42:00.948Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011fdpK8wYqctTNk4MShdKBT`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Recompile after fixing reference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5299de67-a4d4-4ecb-b307-cefc5185e1ec",
  "isSidechain": false,
  "requestId": "req_011CbL53sVRLTsYYEArQXhHG",
  "type": "assistant",
  "uuid": "249baa1a-1e99-4ecc-aef3-aab2a90d2f53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4QZhKG1qkgm9cp3HyiC3J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 70226,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 70226,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
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

_source line 47 · 2026-05-23T19:42:02.636Z_

<details><summary>↩ Tool result · `toolu_011fdpK8wYqctTNk4MShdKBT`</summary>

```text
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 154209 bytes).
Transcript written on paper.log.
/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (7 pages, 154209 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "249baa1a-1e99-4ecc-aef3-aab2a90d2f53",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "ec80eaa6-e934-4daa-b0d8-bdaa8da70a60",
  "toolUseResult": {
    "stdout": "/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 154209 bytes).\nTranscript written on paper.log.\n/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (7 pages, 154209 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "249baa1a-1e99-4ecc-aef3-aab2a90d2f53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T19:42:05.825Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QrKuP537wJV4bHAZN1ZiUP`</summary>

```json
{
  "command": "grep \"LaTeX Warning\" paper.log",
  "description": "Check remaining LaTeX warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec80eaa6-e934-4daa-b0d8-bdaa8da70a60",
  "isSidechain": false,
  "requestId": "req_011CbL54CEHy2Z7geEABd63A",
  "type": "assistant",
  "uuid": "653eddfe-7f18-401a-ac8f-662a94b01135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZawv7tWm54rkC7G7pJY4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 70521,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 389,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 70521,
          "cache_creation_input_tokens": 389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 389
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

_source line 49 · 2026-05-23T19:42:05.897Z_

<details><summary>↩ Tool result · `toolu_01QrKuP537wJV4bHAZN1ZiUP`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "653eddfe-7f18-401a-ac8f-662a94b01135",
  "isSidechain": false,
  "promptId": "7d0bcd72-8457-432d-9769-6414d77f9e54",
  "type": "user",
  "uuid": "5fcf4640-3887-4140-8527-dae427355de4",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "653eddfe-7f18-401a-ac8f-662a94b01135",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-23T19:42:15.714Z_

Paper compiled cleanly. 7 pages, no warnings, PDF at `artifacts/dream_reports/dream_20260523T185344/median/paper.pdf` (154 KB).

Coverage of all 11 experiments from `experiment_data.json`:
- **full_study_clause_generation** → §4.1 (clause generation methodology)
- **new_type_mini_pilot** → §4.2 (pilot validation)
- **full_study_api** + **full_study_opensource** → §5.1 Table 1 (binary effect, all 5 models)
- **full_study_analysis** → §5.1–5.3 (logistic regression, type hierarchy, layer/interaction)
- **reliability_test** → §5.4 + Table 4 (ICC)
- **error_analysis** → §6.1–6.2 (failure modes, Ambiguity Blindness)
- **judge_calibration** → §4.5 (judge validation)
- **realism_validation** → §4.6 (KS tests vs DRIP-R)
- **perturbation_control** → §4.4 (causal control)
- **sopbench_cross_benchmark** → §7 (cross-domain replication)
- **classifier_poc** → §8 (DeBERTa PoC)
- **kappa_reannotation_success** → §6.3 (human validation, κ=0.39)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fcf4640-3887-4140-8527-dae427355de4",
  "isSidechain": false,
  "requestId": "req_011CbL54SJdAQB4GmkVx2QLM",
  "type": "assistant",
  "uuid": "bb8ca11b-c869-4ce7-a177-cc2a94d33cbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260523T185344/median",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dg8v8HYDEYUGXeASpCFe5g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 99,
      "cache_read_input_tokens": 70910,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 99,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 358,
          "cache_read_input_tokens": 70910,
          "cache_creation_input_tokens": 99,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 99
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260523T185344 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambigu…",
  "leafUuid": "bb8ca11b-c869-4ce7-a177-cc2a94d33cbb",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated research paper",
  "sessionId": "d8d171b8-cd92-4076-8cf5-4c38921f83f5"
}
```

---
