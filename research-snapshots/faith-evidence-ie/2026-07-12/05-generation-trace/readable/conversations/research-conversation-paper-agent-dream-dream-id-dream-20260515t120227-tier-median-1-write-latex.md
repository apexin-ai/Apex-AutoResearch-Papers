# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/04664d5d-6490-4063-ad83-836ebb88cfce.jsonl`
- **Structured JSON:** [`651e621bf39d33048210.json`](../../sessions/65/651e621bf39d33048210.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:20:03.955Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:20:03.955Z",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main\n- Narrative guidance：核心方法有效但 CED 优势不够突出。论文叙事从 \"CED 方法论创新\" 转向 \"首个 LLM evidence-grounded DocRE 框架 + 在线/离线 RL 对比分析\" 双主线。 Claim 1 成立但弱化措辞（\"competitive with\" 而非 \"surpasses\"）；Claim 2 最危险——CED 优于 flat-NLI 但差异不 dramatic， 需将叙事调整为 \"CED 提供一致性改善，且作为可组合模块具有实用价值\"；Claim 3 升级为并列 contribution；Claim 4 补充 EDCR 局限性讨论。 补充 model size ablation 和 Re-DocRED 扩展加厚实验章节。EMNLP Main poster 可期。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T12:20:03.960Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:20:03.960Z",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-15T12:20:03.985Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main
- Narrative guidance：核心方法有效但 CED 优势不够突出。论文叙事从 "CED 方法论创新" 转向 "首个 LLM evidence-grounded DocRE 框架 + 在线/离线 RL 对比分析" 双主线。 Claim 1 成立但弱化措辞（"competitive with" 而非 "surpasses"）；Claim 2 最危险——CED 优于 flat-NLI 但差异不 dramatic， 需将叙事调整为 "CED 提供一致性改善，且作为可组合模块具有实用价值"；Claim 3 升级为并列 contribution；Claim 4 补充 EDCR 局限性讨论。 补充 model size ablation 和 Re-DocRED 扩展加厚实验章节。EMNLP Main poster 可期。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "bba1687f-d69a-4549-b728-ce6345b3c6a3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:20:03.984Z_

```json
{
  "parentUuid": "bba1687f-d69a-4549-b728-ce6345b3c6a3",
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
  "uuid": "adb6ed0e-2ef6-40c4-a634-1418dbc5bb01",
  "timestamp": "2026-05-15T12:20:03.984Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:20:03.984Z_

```json
{
  "parentUuid": "adb6ed0e-2ef6-40c4-a634-1418dbc5bb01",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "95732390-3be7-4809-bc2a-96fa8883b017",
  "timestamp": "2026-05-15T12:20:03.984Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
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
  "aiTitle": "Generate median-tier simulated paper for dream ID",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Assistant

_source line 7 · 2026-05-15T12:20:06.855Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95732390-3be7-4809-bc2a-96fa8883b017",
  "isSidechain": false,
  "requestId": "req_011Cb4Lt4kra1tXkHtvYWTj3",
  "type": "assistant",
  "uuid": "7d1df484-1fd4-4a72-8e6d-7c2f49702383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRpYno5vj8NjzTMsebArih",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11283,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11283
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

_source line 8 · 2026-05-15T12:20:07.762Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D7BLa1y7nctDXJMgcN4xCr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d1df484-1fd4-4a72-8e6d-7c2f49702383",
  "isSidechain": false,
  "requestId": "req_011Cb4Lt4kra1tXkHtvYWTj3",
  "type": "assistant",
  "uuid": "d896b2f7-612d-462e-82ab-3e0f5a5831ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRpYno5vj8NjzTMsebArih",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11283,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11283
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

_source line 9 · 2026-05-15T12:20:07.914Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PhB2bYRatjR4m51cpmDWN2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d896b2f7-612d-462e-82ab-3e0f5a5831ff",
  "isSidechain": false,
  "requestId": "req_011Cb4Lt4kra1tXkHtvYWTj3",
  "type": "assistant",
  "uuid": "7b288a89-78cf-4464-8481-4b2771397a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRpYno5vj8NjzTMsebArih",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11283,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11283,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11283
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

_source line 10 · 2026-05-15T12:20:07.920Z_

<details><summary>↩ Tool result · `toolu_01PhB2bYRatjR4m51cpmDWN2`</summary>

```text
1	# Paper Framing — FREIGE
2	
3	> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)
4	> **最后更新**: 2026-05-15
5	
6	## Target Venue
7	
8	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
9	- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)
10	- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)
11	
12	## Core Insight
13	
14	LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。
15	
16	**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从"是否蕴含"升级为"是否比最佳干扰句更蕴含"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。
17	
18	**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。
19	
20	## Story Arc
21	
22	1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）
23	2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）
24	3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）
25	4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险
26	5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + "RSFT=PPO" (ICML 2025) 等价性理论
27	6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据
28	
29	## Core Claims
30	
31	### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据
32	- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法
33	- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp
34	- **MVP-2 已验证**: 4/4 configs PASS
35	- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比
36	
37	### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT
38	- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异
39	- CED 的对比性 margin 过滤掉 distractor-heavy 候选
40	- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）
41	
42	### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget
43	- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败
44	- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力
45	- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据
46	- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功
47	
48	### Claim 4 (Evaluation): EDCR 作为独立评估指标
49	- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|
50	- Evi-F1 盲区：不惩罚 plausible-looking distractor citations
51	- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）
52	- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比
53	
54	## MVP Evidence Summary
55	
56	| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |
57	|--------|--------|----------|--------|------|------|
58	| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |
59	| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |
60	| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |
61	| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |
62	| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |
63	| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |
64	| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |
65	
66	## Anticipated Reviewer Concerns
67	
68	### RC1: NLI reward 信号质量（高概率攻击）
69	- **攻击**: "DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声"
70	- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径
71	- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比
72	
73	### RC2: Gold evidence 标注不完整导致 false distractor
74	- **攻击**: "被标为 distractor 的句子可能是 annotator 遗漏的有效证据"
75	- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱
76	- **Research 补充**: false-distractor 鲁棒性量化分析
77	
78	### RC3: 评测可比性
79	- **攻击**: "生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？"
80	- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation
81	
82	### RC4: 单数据集 + 单模型泛化性
83	- **攻击**: "只在 DocRED + Qwen3-4B 上验证"
84	- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation
85	
86	### RC5: RSFT vs GRPO 是否公平对比
87	- **攻击**: "GRPO 失败可能是超参问题而非方法论问题"
88	- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type
89	
90	### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限
91	- **攻击**: "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著"
92	- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确
93	- **Research**: CED reranker PoC（运行中），top_k ablation
94	
95	### RC7: 方法过于简单
96	- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度
97	
98	## Key Baselines (8+)
99	
100	1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL
101	2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）
102	3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法
103	4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中
104	5. **GRPO+CED**: 在线 RL with CED reward — negative baseline
105	6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)
106	7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)
107	8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)
108	9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)
109	
110	## Publishability Threshold
111	
112	- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline
113	- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整
114	- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）
115	
116	## Research Phase Priorities
117	
118	| Priority | 实验 | Claim | 预估 GPU-hours |
119	|----------|------|-------|---------------|
120	| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |
121	| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |
122	| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |
123	| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |
124	| P1 | CED-as-reranker (running) | C1 bonus | ~6h |
125	| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |
126	| P1 | Re-DocRED extension | RC4 | ~12h |
127	| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |
128	| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |
129	| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |
130	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b288a89-78cf-4464-8481-4b2771397a78",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "2697d7ad-d61b-4aec-bc32-0551a23e8a24",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md",
      "content": "# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: RSFT vs GRPO 是否公平对比\n- **攻击**: \"GRPO 失败可能是超参问题而非方法论问题\"\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim | 预估 GPU-hours |\n|----------|------|-------|---------------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\n| P1 | Re-DocRED extension | RC4 | ~12h |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\n",
      "numLines": 130,
      "startLine": 1,
      "totalLines": 130
    }
  },
  "sourceToolAssistantUUID": "7b288a89-78cf-4464-8481-4b2771397a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T12:20:08.142Z_

<details><summary>↩ Tool result · `toolu_01D7BLa1y7nctDXJMgcN4xCr`</summary>

```text
1	[
2	  {
3	    "name": "CED vs flat-NLI RSFT ablation",
4	    "description": "用 flat-NLI scoring（无 contrastive margin）筛选 RSFT 训练数据，与 CED scoring 的 RSFT 做 apple-to-apple 对比。 复用已有 candidate pool（21952 generations），仅替换 scoring function 为 max(NLI(premise=evidence, hypothesis=claim)) 而非 CED 的 margin = p_pos - max(p_neg)。flat-NLI top_k=1 筛选后训练，同超参（1ep, α=32, lr=1e-5，对齐 r2b config）。\n",
5	    "results": {
6	      "flatnli_rsft_rel_f1": 0.442,
7	      "flatnli_rsft_evi_f1": 0.7985,
8	      "flatnli_rsft_edcr": 0.685,
9	      "flatnli_rsft_evi_precision": 0.801,
10	      "flatnli_rsft_evi_recall": 0.796,
11	      "flatnli_rsft_pred_count": 14950,
12	      "flatnli_selected_samples": 2750,
13	      "flatnli_selection_rate": 0.125,
14	      "flatnli_mean_f1": 0.608,
15	      "ced_rsft_rel_f1": 0.4493,
16	      "ced_rsft_evi_f1": 0.8128,
17	      "ced_rsft_edcr": 0.6609,
18	      "delta_evi_f1_ced_minus_flatnli": 0.0143,
19	      "delta_edcr_ced_minus_flatnli": -0.0241,
20	      "delta_rel_f1_ced_minus_flatnli": 0.0073
21	    },
22	    "tables": [
23	      {
24	        "name": "Table: CED vs flat-NLI RSFT Ablation (Dev Set)",
25	        "columns": [
26	          "Method",
27	          "Scoring",
28	          "rel_f1",
29	          "evi_f1",
30	          "EDCR↓",
31	          "Δevi_f1",
32	          "ΔEDCR"
33	        ],
34	        "rows": [
35	          [
36	            "SFT baseline",
37	            "—",
38	            0.4057,
39	            0.7979,
40	            0.7118,
41	            "—",
42	            "—"
43	          ],
44	          [
45	            "RSFT",
46	            "flat-NLI",
47	            0.442,
48	            0.7985,
49	            0.685,
50	            "+0.06pp",
51	            "-2.68pp"
52	          ],
53	          [
54	            "RSFT",
55	            "CED",
56	            0.4493,
57	            0.8128,
58	            0.6609,
59	            "+1.49pp",
60	            "-5.09pp"
61	          ],
62	          [
63	            "Δ (CED − flat-NLI)",
64	            "—",
65	            "+0.73pp",
66	            "+1.43pp",
67	            "-2.41pp",
68	            "—",
69	            "—"
70	          ]
71	        ]
72	      }
73	    ],
74	    "figures": [],
75	    "analysis": "CED 优于 flat-NLI 在所有三个维度上一致，但 evi_f1 gap 1.43pp 和 EDCR gap 2.41pp 在统计上处于边缘。 需要 bootstrap confidence interval 确认显著性。若 p>0.05，Claim 2 需进一步弱化为 \"CED provides consistent directional improvement\"。关键发现：flat-NLI RSFT 的 evi_f1 几乎等于 SFT（+0.06pp）， 说明 flat-NLI scoring 在 evidence 质量维度几乎无筛选能力——它选出的 top candidate 的 evidence 质量与随机 SFT 输出相当。这一 null result 实际上 *支撑* 了 CED 的价值叙事：不是 CED 改善有限，而是 flat-NLI 在 evidence 维度几乎无效。论文中应将此 framing 为 \"flat-NLI fails to discriminate evidence quality\" 而非 \"CED marginally improves\"。\n\n\nflat-NLI scoring 能筛掉明显低质量候选（NLI 分数低的），因此 flat-NLI RSFT 仍显著优于 SFT baseline （rel_f1 +3.6pp, evi_f1 +0.06pp）。但 flat-NLI 无法区分 entity-sharing distractor 和 genuine evidence—— 两者的 NLI score 都高（因为都包含相关实体），导致筛选出的训练样本中保留了更多 distractor-heavy candidates。 CED 的 contrastive margin 恰好针对这一盲区：margin = p_pos - max(p_neg) 会惩罚那些 distractor 也获得高 NLI 分数的样本。但在 median 档位下，这种区分能力有限（discrimination_accuracy 0.815 而非 0.9+）， hard negative 有时自身也是有效 evidence（annotator 遗漏），导致 CED margin 信号有噪声。 最终 CED 相对 flat-NLI 的 evi_f1 gap 为 1.43pp，EDCR 改善 2.41pp——方向一致但不够 dramatic。 rel_f1 差异更小（0.73pp），因为关系抽取能力主要由 SFT 基础和训练数据量决定，scoring function 差异影响有限。\n"
76	  },
77	  {
78	    "name": "Test set evaluation (RSFT best config)",
79	    "description": "用 RSFT best config（r2b: 1ep, α=32, lr=1e-5）和 s44（3ep, α=128, seed=44）在 DocRED test set 上评估。 CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。\n",
80	    "results": {
81	      "rsft_ced_test_rel_f1": 0.428,
82	      "rsft_ced_test_ign_f1": 0.4195,
83	      "rsft_ced_test_evi_f1": 0.789,
84	      "rsft_ced_test_edcr": 0.638,
85	      "rsft_ced_test_precision": 0.435,
86	      "rsft_ced_test_recall": 0.4215,
87	      "rsft_ced_s44_test_rel_f1": 0.438,
88	      "rsft_ced_s44_test_ign_f1": 0.429,
89	      "rsft_ced_s44_test_evi_f1": 0.783,
90	      "rsft_ced_s44_test_edcr": 0.62,
91	      "sft_test_rel_f1": 0.386,
92	      "sft_test_ign_f1": 0.378,
93	      "sft_test_evi_f1": 0.775,
94	      "sft_test_edcr": 0.695,
95	      "flatnli_rsft_test_rel_f1": 0.42,
96	      "flatnli_rsft_test_evi_f1": 0.776,
97	      "flatnli_rsft_test_edcr": 0.668,
98	      "delta_rsft_ced_vs_sft_rel_f1": "+4.20pp",
99	      "delta_rsft_ced_vs_sft_evi_f1": "+1.40pp",
100	      "dev_to_test_rel_f1_drop": "-2.13pp",
101	      "dev_to_test_evi_f1_drop": "-2.38pp"
102	    },
103	    "tables": [
104	      {
105	        "name": "Table: Test Set Results — Main Comparison",
106	        "columns": [
107	          "Method",
108	          "rel_f1",
109	          "ign_f1",
110	          "evi_f1",
111	          "EDCR↓"
112	        ],
113	        "rows": [
114	          [
115	            "SFT baseline",
116	            0.386,
117	            0.378,
118	            0.775,
119	            0.695
120	          ],
121	          [
122	            "RSFT flat-NLI",
123	            0.42,
124	            "—",
125	            0.776,
126	            0.668
127	          ],
128	          [
129	            "RSFT CED (r2b)",
130	            0.428,
131	            0.42,
132	            0.789,
133	            0.638
134	          ],
135	          [
136	            "RSFT CED (s44)",
137	            0.438,
138	            0.429,
139	            0.783,
140	            0.62
141	          ],
142	          [
143	            "DREEAM†",
144	            "—",
145	            "—",
146	            0.5734,
147	            "—"
148	          ],
149	          [
150	            "SAIS†",
151	            "—",
152	            "—",
153	            0.5567,
154	            "—"
155	          ]
156	        ]
157	      },
158	      {
159	        "name": "Table: Dev→Test Generalization Gap",
160	        "columns": [
161	          "Config",
162	          "dev_rel_f1",
163	          "test_rel_f1",
164	          "Δrel_f1",
165	          "dev_evi_f1",
166	          "test_evi_f1",
167	          "Δevi_f1"
168	        ],
169	        "rows": [
170	          [
171	            "SFT",
172	            0.4057,
173	            0.386,
174	            "-1.97pp",
175	            0.7979,
176	            0.775,
177	            "-2.29pp"
178	          ],
179	          [
180	            "RSFT-CED r2b",
181	            0.4493,
182	            0.428,
183	            "-2.13pp",
184	            0.8128,
185	            0.789,
186	            "-2.38pp"
187	          ],
188	          [
189	            "RSFT-CED s44",
190	            0.4655,
191	            0.438,
192	            "-2.75pp",
193	            0.8087,
194	            0.783,
195	            "-2.57pp"
196	          ]
197	        ]
198	      }
199	    ],
200	    "figures": [],
201	    "analysis": "Test set 结果确认 Claim 1 成立：RSFT+CED 在 test 上 evi_f1=0.789 远超 DREEAM 0.5734（+21.6pp）， 但需在论文中明确说明评估协议差异——DREEAM 用 attention weight thresholding 提取 evidence，FREIGE 用显式 sentence index 生成。rel_f1 0.428-0.438 虽不及 encoder SOTA（ATLOP 63+），但作为同时生成 evidence 的 首个 LLM 方法，\"competitive\" 措辞合理。s44 在 test 上 rel_f1 更高但 evi_f1 更低，建议论文中报告两个 config 并讨论 rel_f1-evi_f1 trade-off。ign_f1 与 rel_f1 非常接近（差 <1pp），说明 RSFT 未过度依赖训练集中的 共现关系。EDCR 在 test 上 0.62-0.64，虽优于 SFT 的 0.695，但仍意味着 ~62-64% 的 cited non-gold sentences 是 entity-sharing distractors——论文需坦诚讨论此局限。\n\n\nDev→test 衰减是 DocRED 的已知现象：test set 的关系分布与 dev 有偏移（部分关系类型在 test 中频率不同）， 且 test set 标注由不同 annotator 完成。rel_f1 衰减约 2.1pp（从 dev 0.4493 到 test 0.4280）， 处于 median 预期的 -2~4pp 范围中段。evi_f1 衰减约 2.4pp（从 0.8128 到 0.7890）， 稍大于 rel_f1 衰减，因为 evidence 标注在 test set 中更保守（gold evidence 集合更小）。 s44 config（3ep 训练）在 dev 上 rel_f1 更高（0.4655）但 test 上衰减更大（-2.75pp）， 暗示 3ep 训练有轻微 dev set overfitting。r2b 的 1ep 训练泛化更稳定。 SFT baseline 也有 ~2pp 衰减（dev 0.4057 → test 0.3860），说明衰减是数据固有的而非方法导致。 关键指标：test_evi_f1 0.789 远高于 DREEAM 的 57.34，但需注意评估协议差异（生成式 vs attention-based）。 EDCR 在 test 上略好于 dev（0.638 vs 0.661），可能因 test set 的 entity mention 分布不同。\n"
202	  },
203	  {
204	    "name": "EDCR pipeline 验证 + cross-method diagnostic table",
205	    "description": "在所有 evidence-producing 方法上统一计算 EDCR 及其子指标，构建 cross-method diagnostic table。 包括 EDCR 的 breakdown：entity-sharing distractor rate、non-entity distractor rate、 evidence precision/recall 按关系类型分层分析。\n",
206	    "results": {
207	      "sft_edcr": 0.7118,
208	      "sft_entity_distractor_count_mean": 3.2,
209	      "sft_non_entity_distractor_count_mean": 0.4,
210	      "rsft_ced_edcr": 0.6609,
211	      "rsft_ced_entity_distractor_count_mean": 2.6,
212	      "rsft_flatnli_edcr": 0.685,
213	      "rsft_flatnli_entity_distractor_count_mean": 2.9,
214	      "ced_reranker_edcr": 0.605,
215	      "ced_reranker_entity_distractor_count_mean": 2.2,
216	      "high_edcr_relation_types": [
217	        "P17 (country)",
218	        "P131 (located in)",
219	        "P27 (citizenship)"
220	      ],
221	      "high_edcr_mean": 0.82,
222	      "low_edcr_relation_types": [
223	        "P50 (author)",
224	        "P86 (composer)",
225	        "P175 (performer)"
226	      ],
227	      "low_edcr_mean": 0.45
228	    },
229	    "tables": [
230	      {
231	        "name": "Table: Cross-Method EDCR Diagnostic",
232	        "columns": [
233	          "Method",
234	          "EDCR↓",
235	          "Evi-F1",
236	          "Mean #Distractor",
237	          "Mean #Gold Cited",
238	          "Mean #Total Cited"
239	        ],
240	        "rows": [
241	          [
242	            "SFT",
243	            0.712,
244	            0.798,
245	            3.2,
246	            2.1,
247	            5.3
248	          ],
249	          [
250	            "RSFT flat-NLI",
251	            0.685,
252	            0.799,
253	            2.9,
254	            2.0,
255	            4.9
256	          ],
257	          [
258	            "RSFT CED",
259	            0.661,
260	            0.813,
261	            2.6,
262	            2.1,
263	            4.7
264	          ],
265	          [
266	            "CED reranker",
267	            0.605,
268	            0.79,
269	            2.2,
270	            2.0,
271	            4.2
272	          ]
273	        ]
274	      },
275	      {
276	        "name": "Table: EDCR by Relation Type (Top-5 / Bottom-5)",
277	        "columns": [
278	          "Relation",
279	          "SFT EDCR",
280	          "RSFT-CED EDCR",
281	          "ΔEDCR",
282	          "#Instances"
283	        ],
284	        "rows": [
285	          [
286	            "P17 (country)",
287	            0.85,
288	            0.79,
289	            "-0.06",
290	            1205
291	          ],
292	          [
293	            "P131 (located in)",
294	            0.83,
295	            0.78,
296	            "-0.05",
297	            987
298	          ],
299	          [
300	            "P27 (citizenship)",
301	            0.8,
302	            0.74,
303	            "-0.06",
304	            654
305	          ],
306	          [
307	            "P30 (continent)",
308	            0.78,
309	            0.73,
310	            "-0.05",
311	            321
312	          ],
313	          [
314	            "P150 (contains)",
315	            0.77,
316	            0.72,
317	            "-0.05",
318	            445
319	          ],
320	          [
321	            "...",
322	            "...",
323	            "...",
324	            "...",
325	            "..."
326	          ],
327	          [
328	            "P86 (composer)",
329	            0.48,
330	            0.42,
331	            "-0.06",
332	            198
333	          ],
334	          [
335	            "P50 (author)",
336	            0.45,
337	            0.39,
338	            "-0.06",
339	            276
340	          ],
341	          [
342	            "P175 (performer)",
343	            0.42,
344	            0.37,
345	            "-0.05",
346	            312
347	          ],
348	          [
349	            "P40 (child)",
350	            0.4,
351	            0.35,
352	            "-0.05",
353	            187
354	          ],
355	          [
356	            "P26 (spouse)",
357	            0.38,
358	            0.33,
359	            "-0.05",
360	            156
361	          ]
362	        ]
363	      }
364	    ],
365	    "figures": [],
366	    "analysis": "EDCR 诊断揭示两个关键发现：(1) CED 在所有关系类型上一致降低 EDCR（~5-6pp），但高 EDCR 关系仍然很高 （P17: 0.85→0.79），说明 entity-sharing distractor 问题在地理类关系上是结构性的，单靠 CED 难以彻底解决； (2) CED reranker（推理时选择）比 RSFT-CED（训练时筛选）在 EDCR 上更优（0.605 vs 0.661）， 暗示 CED 的直接使用比间接使用更有效，但代价是推理时间增加。 论文中应将此分析作为 Claim 4 的核心内容，诚实讨论 EDCR 63-66% 的局限性， 并将关系类型分层分析作为 future work 的 motivation（relation-aware CED 设计）。\n\n\nEDCR 反映 entity-sharing distractor 在 citations 中的占比。SFT 的 EDCR 最高（0.712），因为 SFT 模型倾向于引用包含 head/tail entity mention 的所有句子而非仅支持特定关系的句子——这是 \"entity mention heuristic\" 的体现。RSFT-CED 降低 EDCR 至 0.661，因为 CED scoring 在训练数据筛选时惩罚了 distractor-heavy candidates。flat-NLI RSFT 的 EDCR 0.685 介于 SFT 和 CED 之间——flat-NLI 能过滤掉一些 evidence 完全不相关的候选，但无法区分 entity-sharing distractor。 关系类型分层分析揭示 EDCR 不均匀：地理/国籍类关系（P17, P131, P27）的 EDCR 极高（0.82），因为文档中 大量句子提到国家/地点名称但不直接支持该关系；而创作类关系（P50, P86）的 EDCR 较低（0.45），因为这类关系 通常在少数特定句子中明确表述。这一分层分析本身有诊断价值，可作为 Claim 4 的核心证据。\n"
367	  },
368	  {
369	    "name": "DREEAM baseline reproduction",
370	    "description": "在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1。使用官方代码和预训练权重， 确认 57.34 这一 test set 数字对应的 dev set 表现，作为 Claim 1 的直接对比基线。\n",
371	    "results": {
372	      "dreeam_dev_evi_f1": 0.568,
373	      "dreeam_dev_evi_precision": 0.552,
374	      "dreeam_dev_evi_recall": 0.585,
375	      "dreeam_dev_rel_f1": 0.628,
376	      "dreeam_test_evi_f1_reported": 0.5734,
377	      "reproduction_gap": "-0.0054",
378	      "sais_dev_evi_f1": 0.548
379	    },
380	    "tables": [
381	      {
382	        "name": "Table: Evidence Baseline Reproduction",
383	        "columns": [
384	          "Method",
385	          "Type",
386	          "dev_evi_f1",
387	          "test_evi_f1 (reported)",
388	          "dev_rel_f1"
389	        ],
390	        "rows": [
391	          [
392	            "DREEAM (paper)",
393	            "encoder",
394	            "—",
395	            0.5734,
396	            0.635
397	          ],
398	          [
399	            "DREEAM (reproduced)",
400	            "encoder",
401	            0.568,
402	            "—",
403	            0.628
404	          ],
405	          [
406	            "SAIS (reproduced)",
407	            "encoder",
408	            0.548,
409	            0.5567,
410	            0.618
411	          ],
412	          [
413	            "FREIGE (RSFT-CED)",
414	            "generative",
415	            0.813,
416	            "—*",
417	            0.449
418	          ]
419	        ]
420	      }
421	    ],
422	    "figures": [],
423	    "analysis": "复现结果确认 DREEAM dev Evi-F1 约 0.568（与 test 0.5734 基本一致，小幅偏差可接受）。 FREIGE 与 DREEAM 的 Evi-F1 差距巨大（0.813 vs 0.568），但这部分源于评估协议差异： DREEAM 对每个句子做 binary attention classification，threshold 选择会影响 precision-recall trade-off； FREIGE 生成显式 sentence index，模型 \"知道自己在引用什么\"。 论文中需要 (1) 明确说明评估协议差异，(2) 考虑在同一评估框架下对比（如将 FREIGE 输出转为 binary labels 后与 DREEAM 对比），(3) 承认 DREEAM 的 rel_f1 (0.628) 远高于 FREIGE (0.449)， FREIGE 的价值在于 evidence grounding 而非 extraction performance。\n\n\nDREEAM 论文报告 test Evi-F1 57.34，dev 上通常比 test 稍低或相近（DocRED dev/test 分布相似但不完全一致）。 复现偏差 -0.54pp 源于：(1) 随机种子差异导致 attention threshold 的最优值稍有不同；(2) PyTorch/CUDA 版本 差异引入的浮点不确定性；(3) 可能的预处理细节差异（sentence boundary detection）。 这个偏差幅度在合理范围内（<1pp），但需要在论文中明确报告为 \"reproduction\" 结果。 dev Evi-F1 0.568 意味着 FREIGE 的 dev evi_f1 0.813 比 DREEAM 高 24.5pp——但这个对比需要大量 caveats： DREEAM 的 evidence 是 attention-based extraction（binary classification per sentence）， FREIGE 是生成式（模型显式输出 sentence indices），评估粒度和 false positive 成因完全不同。 论文中应将此对比作为 \"reference point\" 而非 \"direct superiority claim\"。\n"
424	  },
425	  {
426	    "name": "CED-as-reranker",
427	    "description": "推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。 对 dev set 全量文档运行：SFT 生成 8 candidates per document → CED 打分 → 选最高 CED score 的候选作为最终输出。\n",
428	    "results": {
429	      "reranker_rel_f1": 0.415,
430	      "reranker_evi_f1": 0.805,
431	      "reranker_edcr": 0.605,
432	      "reranker_evi_precision": 0.82,
433	      "reranker_evi_recall": 0.791,
434	      "reranker_pred_count": 13500,
435	      "sft_baseline_rel_f1": 0.4057,
436	      "sft_baseline_evi_f1": 0.7979,
437	      "sft_baseline_edcr": 0.7118,
438	      "delta_rel_f1": "+0.93pp",
439	      "delta_evi_f1": "+0.71pp",
440	      "delta_edcr": "-10.68pp",
441	      "inference_time_multiplier": "~8x"
442	    },
443	    "tables": [
444	      {
445	        "name": "Table: CED-as-Reranker vs Training-based Methods",
446	        "columns": [
447	          "Method",
448	          "Training?",
449	          "rel_f1",
450	          "evi_f1",
451	          "EDCR↓",
452	          "Inference Cost"
453	        ],
454	        "rows": [
455	          [
456	            "SFT",
457	            "SFT only",
458	            0.4057,
459	            0.7979,
460	            0.712,
461	            "1x"
462	          ],
463	          [
464	            "CED reranker",
465	            "No (SFT + rerank)",
466	            0.415,
467	            0.805,
468	            0.605,
469	            "~8x"
470	          ],
471	          [
472	            "RSFT-CED",
473	            "SFT + RSFT",
474	            0.449,
475	            0.813,
476	            0.661,
477	            "1x"
478	          ],
479	          [
480	            "RSFT-CED + reranker",
481	            "SFT + RSFT + rerank",
482	            0.452,
483	            0.818,
484	            0.585,
485	            "~8x"
486	          ]
487	        ]
488	      }
489	    ],
490	    "figures": [],
491	    "analysis": "CED reranker 提供了最佳 EDCR（0.605），证明 CED 作为推理时 quality signal 的直接价值。 但 reranker 的 rel_f1 和 evi_f1 均不如 RSFT-CED，说明训练时改善优于推理时选择。 最有趣的是 RSFT-CED + reranker 组合：额外降低 EDCR 至 0.585（比单独 RSFT 再降 7.6pp）， 而 rel_f1/evi_f1 几乎不受影响。这支持 \"CED 作为可组合模块\" 的叙事—— RSFT 改善 generation quality，reranker 进一步过滤 distractor。 在 median 档位下，reranker 的 EDCR 降至 0.585-0.605 仍未突破 0.5 的 \"大部分 citations 不是 distractor\" 阈值，论文需承认这一局限。\n\n\nCED reranker 直接在推理时选择 CED score 最高的候选，其 EDCR 改善最显著（从 0.712 降至 0.605，-10.7pp）， 因为 CED score 直接优化了 \"相对于 distractor 的 evidence 质量\"——高 CED score 的候选天然倾向于引用 更少的 entity-sharing distractors。但 rel_f1 仅小幅提升（+0.93pp），因为 CED 打分不直接优化关系抽取质量， 高 CED score 不一定对应高 rel_f1（有些候选 evidence 好但关系抽错了）。 evi_f1 的提升（+0.71pp）小于 RSFT-CED（+1.49pp），因为 reranker 受限于 SFT 模型的 generation distribution——如果 8 个候选都引用了 distractor，reranker 也无法避免。RSFT 通过改变模型本身的 generation distribution 来从源头改善。 EDCR 改善却显著优于 RSFT，这是因为 reranker 可以在 8 个候选中做 sharp selection（选 EDCR 最低的那个）， 而 RSFT 改变的是 average generation quality（所有输出的 EDCR 平均降低）。 推理时间增加 8x 是实际部署的代价——论文中应讨论 RSFT+reranker 的组合是否值得。\n"
492	  },
493	  {
494	    "name": "Model size ablation (1.7B / 8B)",
495	    "description": "在 Qwen3-1.7B 和 Qwen3-8B 上复现完整 RSFT+CED pipeline，验证方法对模型规模的泛化性。 每个模型：SFT warmup → candidate generation → CED scoring → RSFT training → dev eval。\n",
496	    "results": {
497	      "qwen_1_7b_sft_rel_f1": 0.328,
498	      "qwen_1_7b_sft_evi_f1": 0.735,
499	      "qwen_1_7b_sft_edcr": 0.75,
500	      "qwen_1_7b_rsft_ced_rel_f1": 0.365,
501	      "qwen_1_7b_rsft_ced_evi_f1": 0.758,
502	      "qwen_1_7b_rsft_ced_edcr": 0.705,
503	      "qwen_1_7b_delta_rel_f1": "+3.70pp",
504	      "qwen_1_7b_delta_evi_f1": "+2.30pp",
505	      "qwen_1_7b_delta_edcr": "-4.50pp",
506	      "qwen_8b_sft_rel_f1": 0.445,
507	      "qwen_8b_sft_evi_f1": 0.818,
508	      "qwen_8b_sft_edcr": 0.69,
509	      "qwen_8b_rsft_ced_rel_f1": 0.482,
510	      "qwen_8b_rsft_ced_evi_f1": 0.832,
511	      "qwen_8b_rsft_ced_edcr": 0.635,
512	      "qwen_8b_delta_rel_f1": "+3.70pp",
513	      "qwen_8b_delta_evi_f1": "+1.40pp",
514	      "qwen_8b_delta_edcr": "-5.50pp"
515	    },
516	    "tables": [
517	      {
518	        "name": "Table: Model Size Ablation",
519	        "columns": [
520	          "Model",
521	          "Method",
522	          "rel_f1",
523	          "evi_f1",
524	          "EDCR↓",
525	          "Δrel_f1",
526	          "Δevi_f1"
527	        ],
528	        "rows": [
529	          [
530	            "Qwen3-1.7B",
531	            "SFT",
532	            0.328,
533	            0.735,
534	            0.75,
535	            "—",
536	            "—"
537	          ],
538	          [
539	            "Qwen3-1.7B",
540	            "RSFT-CED",
541	            0.365,
542	            0.758,
543	            0.705,
544	            "+3.7pp",
545	            "+2.3pp"
546	          ],
547	          [
548	            "Qwen3-4B",
549	            "SFT",
550	            0.406,
551	            0.798,
552	            0.712,
553	            "—",
554	            "—"
555	          ],
556	          [
557	            "Qwen3-4B",
558	            "RSFT-CED",
559	            0.449,
560	            0.813,
561	            0.661,
562	            "+4.4pp",
563	            "+1.5pp"
564	          ],
565	          [
566	            "Qwen3-8B",
567	            "SFT",
568	            0.445,
569	            0.818,
570	            0.69,
571	            "—",
572	            "—"
573	          ],
574	          [
575	            "Qwen3-8B",
576	            "RSFT-CED",
577	            0.482,
578	            0.832,
579	            0.635,
580	            "+3.7pp",
581	            "+1.4pp"
582	          ]
583	        ]
584	      }
585	    ],
586	    "figures": [],
587	    "analysis": "三个模型规模上 RSFT+CED 均一致改善所有指标，Δrel_f1 在 3.7-4.4pp 范围内稳定，Δevi_f1 在 1.4-2.3pp。 8B 的绝对数字最优但与 4B 差距不大（rel_f1 +3.3pp, evi_f1 +1.9pp），说明从 4B 到 8B 的边际收益递减。 1.7B 虽绝对性能较弱，但 RSFT-CED 的改善幅度不减，这一正面结果支撑了方法的实用性（可在资源有限场景部署）。 论文中可用一句话总结：\"RSFT+CED consistently improves over SFT across model sizes (1.7B–8B), with relative gains largely independent of model capacity.\"\n\n\n1.7B 模型的 SFT baseline 显著弱于 4B（rel_f1 0.328 vs 0.406），因为小模型在 DocRE 的长文档理解和 多关系抽取上能力有限，输出格式合规率也更低（更多 truncation 和格式错误）。但 RSFT+CED 的相对改善幅度 一致（rel_f1 +3.7pp, evi_f1 +2.3pp），说明 CED scoring 的质量筛选对小模型同样有效—— 甚至 evi_f1 的绝对改善更大（+2.3pp vs 4B 的 +1.5pp），因为小模型的 generation diversity 更高 （输出更不确定），CED 有更大的筛选空间。 8B 模型的 SFT baseline 已很强（rel_f1 0.445），RSFT+CED 仍带来一致改善（+3.7pp rel_f1, +1.4pp evi_f1）， 但 evi_f1 的改善幅度略小于 4B（+1.4pp vs +1.5pp），可能因为 8B SFT 已学到较好的 evidence 模式。 EDCR 改善在 8B 上更大（-5.5pp vs 4B 的 -5.1pp），暗示更大模型能更好地利用 CED 筛选信号。 这一 \"方法在各规模上一致有效\" 的结果足以应对 RC4，但不构成额外 novelty。\n"
588	  },
589	  {
590	    "name": "Re-DocRED extension",
591	    "description": "在 Re-DocRED 上评估 RSFT+CED，验证方法在修正 false negative 标注后的表现。 Re-DocRED 对 DocRED 的标注进行了大规模修正（补充遗漏关系、纠正错误 evidence），预期更干净的标注会改变 EDCR 的计算基准。\n",
592	    "results": {
593	      "redocred_sft_rel_f1": 0.435,
594	      "redocred_sft_evi_f1": 0.815,
595	      "redocred_sft_edcr": 0.58,
596	      "redocred_rsft_ced_rel_f1": 0.475,
597	      "redocred_rsft_ced_evi_f1": 0.835,
598	      "redocred_rsft_ced_edcr": 0.525,
599	      "redocred_delta_rel_f1": "+4.00pp",
600	      "redocred_delta_evi_f1": "+2.00pp",
601	      "redocred_delta_edcr": "-5.50pp",
602	      "docred_to_redocred_edcr_drop": "-13.6pp (SFT), -13.6pp (RSFT)"
603	    },
604	    "tables": [
605	      {
606	        "name": "Table: DocRED vs Re-DocRED",
607	        "columns": [
608	          "Dataset",
609	          "Method",
610	          "rel_f1",
611	          "evi_f1",
612	          "EDCR↓"
613	        ],
614	        "rows": [
615	          [
616	            "DocRED",
617	            "SFT",
618	            0.406,
619	            0.798,
620	            0.712
621	          ],
622	          [
623	            "DocRED",
624	            "RSFT-CED",
625	            0.449,
626	            0.813,
627	            0.661
628	          ],
629	          [
630	            "Re-DocRED",
631	            "SFT",
632	            0.435,
633	            0.815,
634	            0.58
635	          ],
636	          [
637	            "Re-DocRED",
638	            "RSFT-CED",
639	            0.475,
640	            0.835,
641	            0.525
642	          ]
643	        ]
644	      }
645	    ],
646	    "figures": [],
647	    "analysis": "Re-DocRED 结果提供了两个重要 insights：(1) DocRED 上 EDCR 高部分是标注噪声造成的—— Re-DocRED 的更完整标注使 EDCR 降低约 13pp；(2) 即使在更干净标注下，RSFT-CED 仍一致降低 EDCR （-5.5pp），且改善幅度与 DocRED 相当。这加强了方法的鲁棒性论述。 论文中应将 Re-DocRED 结果作为 \"annotation quality sensitivity\" 分析的一部分， 而非核心结果——主实验仍应基于 DocRED（更广泛使用、可与更多 baselines 对比）。\n\n\nRe-DocRED 补充了大量 DocRED 中遗漏的关系标注（false negatives），导致两个效应： (1) rel_f1 提升——之前被判为 false positive 的正确预测现在被计为 true positive，SFT 从 0.406 升至 0.435； (2) EDCR 显著下降——之前被计为 \"distractor\" 的句子（entity-sharing non-gold cited）中有一部分实际上是 补充标注关系的 gold evidence，重新标注后不再是 distractor。SFT EDCR 从 0.712 降至 0.580（-13.2pp）。 RSFT-CED 的改善幅度与 DocRED 一致（Δrel_f1 +4.0pp, Δevi_f1 +2.0pp），说明方法在更干净标注下仍有效。 EDCR 的绝对值在 Re-DocRED 上更低（0.525 vs 0.661），这是好消息——说明 DocRED 上 EDCR 偏高部分归因于 标注 incompleteness（annotator 遗漏了有效 evidence），而非纯粹的模型缺陷。 但 EDCR 0.525 仍意味着过半的 non-gold citations 是 distractor——问题并未因更好标注而消失。\n"
648	  },
649	  {
650	    "name": "top_k ablation",
651	    "description": "CED scoring 筛选 top_k=3 vs top_k=1 对比。top_k=1 选择每个文档 CED score 最高的 1 个候选 （当前配置，~2718 samples），top_k=3 选择前 3 个（~8000 samples，更多但质量更低的训练数据）。\n",
652	    "results": {
653	      "topk1_samples": 2718,
654	      "topk1_mean_ced": 0.6683,
655	      "topk1_rsft_rel_f1": 0.4493,
656	      "topk1_rsft_evi_f1": 0.8128,
657	      "topk1_rsft_edcr": 0.6609,
658	      "topk3_samples": 7950,
659	      "topk3_mean_ced": 0.548,
660	      "topk3_rsft_rel_f1": 0.455,
661	      "topk3_rsft_evi_f1": 0.802,
662	      "topk3_rsft_edcr": 0.678,
663	      "topk3_delta_rel_f1_vs_topk1": "+0.57pp",
664	      "topk3_delta_evi_f1_vs_topk1": "-1.08pp",
665	      "topk3_delta_edcr_vs_topk1": "+1.71pp"
666	    },
667	    "tables": [
668	      {
669	        "name": "Table: top_k Ablation",
670	        "columns": [
671	          "top_k",
672	          "#Samples",
673	          "Mean CED",
674	          "rel_f1",
675	          "evi_f1",
676	          "EDCR↓"
677	        ],
678	        "rows": [
679	          [
680	            1,
681	            2718,
682	            0.668,
683	            0.449,
684	            0.813,
685	            0.661
686	          ],
687	          [
688	            3,
689	            7950,
690	            0.548,
691	            0.455,
692	            0.802,
693	            0.678
694	          ]
695	        ]
696	      }
697	    ],
698	    "figures": [],
699	    "analysis": "top_k ablation 清晰展示了 CED 筛选严格度的 trade-off。在 median 档位下，top_k=1 是 evidence quality 的最优选择。这一结果可作为 Claim 2 的辅助证据：CED scoring 的 discriminative power 在 top-1 selection 时最强，放松阈值会稀释信号——间接说明 CED margin 确实在区分 evidence 质量。 论文中建议报告 top_k=1 作为主结果，top_k=3 作为 ablation，并讨论 \"quality vs quantity\" trade-off 的实践意义。\n\n\ntop_k=3 提供约 3x 的训练数据（7950 vs 2718 samples），但 mean CED score 降低（0.548 vs 0.668）， 因为 rank 2-3 的候选质量低于 rank 1。更多数据带来 rel_f1 的小幅提升（+0.57pp），因为关系抽取受益于 训练数据量——更多样本覆盖更多 relation type 和 entity pair 组合。 但 evi_f1 反而下降（-1.08pp）且 EDCR 升高（+1.71pp），因为 rank 2-3 的候选包含更多 distractor-heavy evidence——CED score 较低意味着这些候选的 evidence 质量接近 flat-NLI 水平。 这一 quality-quantity trade-off 在 RSFT 文献中是已知现象（Yuan et al. 2024 \"self-play\" RSFT 也发现严格筛选优于宽松筛选 for generation quality）。 结论：top_k=1 在 evidence 质量上更优，top_k=3 在 extraction coverage 上更优。 论文中可根据目标选择报告哪个 config——如果强调 evidence faithfulness（Claim 1-2），选 top_k=1。\n"
700	  },
701	  {
702	    "name": "GRPO forgetting 详细分析 + 可视化",
703	    "description": "整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹，绘制 forgetting dynamics 可视化。 覆盖 3 种 reward type（CED, flat-NLI, extract-only）× 多个 learning rate 的完整轨迹。\n",
704	    "results": {
705	      "grpo_ced_lr5e6_rel_f1_trajectory": [
706	        0.406,
707	        0.008,
708	        0.007,
709	        0.009,
710	        0.012,
711	        0.014
712	      ],
713	      "grpo_ced_lr5e6_evi_f1_trajectory": [
714	        0.798,
715	        0.628,
716	        0.758,
717	        0.81,
718	        0.828,
719	        0.85
720	      ],
721	      "grpo_ced_lr5e6_reward_trajectory": [
722	        0.0,
723	        0.35,
724	        0.65,
725	        0.85,
726	        1.05,
727	        1.2
728	      ],
729	      "grpo_ced_lr5e6_collapse_step": 10,
730	      "grpo_ced_kl001_rel_f1_peak": 0.211,
731	      "grpo_ced_kl001_rel_f1_peak_step": 90,
732	      "grpo_ced_kl001_evi_f1_at_peak": 0.567,
733	      "grpo_flatnli_collapse_step": 25,
734	      "grpo_flatnli_final_frac_zero_std": 0.9,
735	      "grpo_extract_rel_f1_peak": 0.015,
736	      "grpo_extract_collapse_step": 20,
737	      "forgetting_pattern": "reward ↑ monotonic, rel_f1 ↓ catastrophic within 10-25 steps, evi_f1 diverges (↑ for CED, ↓ for others)"
738	    },
739	    "tables": [
740	      {
741	        "name": "Table: GRPO Trajectory Summary",
742	        "columns": [
743	          "Reward Type",
744	          "LR",
745	          "KL",
746	          "Collapse Step",
747	          "Peak rel_f1",
748	          "Final evi_f1",
749	          "Final Reward"
750	        ],
751	        "rows": [
752	          [
753	            "CED",
754	            "5e-6",
755	            0,
756	            "~10",
757	            0.014,
758	            0.85,
759	            1.2
760	          ],
761	          [
762	            "CED",
763	            "5e-5",
764	            0.01,
765	            "~50",
766	            0.211,
767	            0.575,
768	            1.2
769	          ],
770	          [
771	            "flat-NLI",
772	            "5e-6",
773	            0,
774	            "~25",
775	            "<0.01",
776	            "<0.01",
777	            0.29
778	          ],
779	          [
780	            "extract-only",
781	            "5e-6",
782	            0,
783	            "~20",
784	            0.015,
785	            "—",
786	            0.3
787	          ]
788	        ]
789	      }
790	    ],
791	    "figures": [],
792	    "analysis": "可视化清晰揭示了在线 RL 在结构化 IE 上的核心困境：多目标优化（relation extraction + evidence grounding） 在 policy gradient 框架下相互干扰。CED reward 成功驱动了 evidence 学习（evi_f1 持续上升）， 但代价是关系抽取能力的 catastrophic forgetting。这不是超参问题——3 种 reward × 多个 lr × KL 约束 全部失败，且失败模式一致（reward ↑ + rel_f1 ↓）。 这一 negative result 本身有方法论价值：为 \"何时用在线 RL vs 离线 RL\" 提供了结构化 IE 场景下的经验指导。 论文中应将此定位为 Claim 3 的核心，与 LongRLVR 的理论框架对接。 reviewer 可能质疑 \"GRPO 超参搜索是否充分\"——覆盖 3 种 reward × 4+ LR × KL 约束的全面搜索 应能说服大部分 reviewer，但建议在 appendix 中放完整 grid 表格。\n\n\nGRPO 的 catastrophic forgetting 机制在 DocRE 上的特殊表现：policy gradient 优化 reward 信号时， 模型快速学会生成高 reward 的输出模式——对 CED reward，这意味着生成包含正确 evidence 句子的文本 （evi_f1 从 0.798 上升至 0.850）；对 extract-only reward，这意味着生成高 F1 的关系抽取格式。 但两者无法兼顾：CED 优化牺牲关系抽取能力（模型 \"遗忘\" 如何正确抽取关系来专注于 evidence）， extract-only 优化也很快坍缩（缺乏 KL 约束时 policy 快速偏离 SFT 分布）。 KL=0.01 约束版本（grpo_ced_kl001）延缓了坍缩（rel_f1 peak 0.211 at step 90）， 但仍远低于 SFT baseline 0.406——KL 约束不足以阻止 forgetting，只是减慢了速度。 flat-NLI reward 坍缩最快（step 25 即 frac_zero_std=0.9），因为 flat-NLI 的 reward surface 更平滑（没有 contrastive margin 的尖锐梯度），策略更容易找到 degenerate optimum。 这一分析连接 LongRLVR (ICLR 2026) 的 evidence grounding 梯度消失理论， 可作为 Claim 3 的完整证据。\n"
793	  },
794	  {
795	    "name": "NLI model ablation",
796	    "description": "DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer。替换 NLI 模型后重新计算全量 CED scores， 对比 discrimination accuracy 和 downstream RSFT 效果。\n",
797	    "results": {
798	      "base_discrimination_accuracy": 0.815,
799	      "base_mean_margin": 0.48,
800	      "base_pearson_r_jaccard": 0.34,
801	      "base_rsft_evi_f1": 0.8128,
802	      "base_rsft_edcr": 0.6609,
803	      "large_discrimination_accuracy": 0.845,
804	      "large_mean_margin": 0.52,
805	      "large_pearson_r_jaccard": 0.31,
806	      "large_rsft_evi_f1": 0.8165,
807	      "large_rsft_edcr": 0.652,
808	      "delta_discrimination_accuracy": "+3.0pp",
809	      "delta_mean_margin": "+0.04",
810	      "delta_rsft_evi_f1": "+0.37pp",
811	      "delta_rsft_edcr": "-0.89pp"
812	    },
813	    "tables": [
814	      {
815	        "name": "Table: NLI Model Ablation",
816	        "columns": [
817	          "NLI Model",
818	          "Disc. Acc.",
819	          "Mean Margin",
820	          "r(margin,jaccard)",
821	          "RSFT evi_f1",
822	          "RSFT EDCR↓"
823	        ],
824	        "rows": [
825	          [
826	            "DeBERTa-v3-base",
827	            0.815,
828	            0.48,
829	            0.34,
830	            0.813,
831	            0.661
832	          ],
833	          [
834	            "DeBERTa-v3-large",
835	            0.845,
836	            0.52,
837	            0.31,
838	            0.817,
839	            0.652
840	          ]
841	        ]
842	      }
843	    ],
844	    "figures": [],
845	    "analysis": "NLI 模型从 base 升级到 large 带来 CED 信号质量的一致改善（discrimination accuracy +3pp）， 但 downstream 的 RSFT 收益递减（evi_f1 +0.37pp）。这表明当前 pipeline 的瓶颈已不在 NLI 模型能力上。对 RC1 的回应可以是：即使 base model 的 NLI 有一定 lexical overlap bias （Pearson r=0.34），CED 的 contrastive 设计已足够有效，升级 NLI 模型的边际收益有限。 建议论文主实验用 base（计算成本更低且结果相近），appendix 报告 large 结果。\n\nDeBERTa-v3-large 比 base 有更强的 NLI 能力（MNLI accuracy large 91.3% vs base 88.1%）， 因此 CED 的 gold vs distractor discrimination accuracy 从 0.815 提升至 0.845。 mean margin 也更大（0.52 vs 0.48），说明 large 模型对 evidence quality 的区分度更高。 但 Pearson r 与 jaccard overlap 的相关性反而略低（0.31 vs 0.34），说明 large 模型 的 NLI 判断更少依赖 lexical overlap——这是正面信号（less spurious correlation）。 然而 downstream 影响有限：RSFT evi_f1 仅提升 0.37pp，EDCR 仅降低 0.89pp。 这是因为 CED scoring 的瓶颈不在 NLI 模型能力而在 DocRED 标注质量—— gold evidence 标注本身不完整（false distractor 问题），更强的 NLI 模型 不能修复标注层面的噪声。这一结果暗示 CED 的改善上界受标注质量限制。 论文中可用此结果应对 RC1，结论为 \"NLI model quality has limited impact, suggesting annotation completeness rather than NLI capability is the bottleneck.\"\n"
846	  }
847	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d896b2f7-612d-462e-82ab-3e0f5a5831ff",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "3d2ccc56-a537-4704-96f6-4d2a22e9dc3b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"CED vs flat-NLI RSFT ablation\",\n    \"description\": \"用 flat-NLI scoring（无 contrastive margin）筛选 RSFT 训练数据，与 CED scoring 的 RSFT 做 apple-to-apple 对比。 复用已有 candidate pool（21952 generations），仅替换 scoring function 为 max(NLI(premise=evidence, hypothesis=claim)) 而非 CED 的 margin = p_pos - max(p_neg)。flat-NLI top_k=1 筛选后训练，同超参（1ep, α=32, lr=1e-5，对齐 r2b config）。\\n\",\n    \"results\": {\n      \"flatnli_rsft_rel_f1\": 0.442,\n      \"flatnli_rsft_evi_f1\": 0.7985,\n      \"flatnli_rsft_edcr\": 0.685,\n      \"flatnli_rsft_evi_precision\": 0.801,\n      \"flatnli_rsft_evi_recall\": 0.796,\n      \"flatnli_rsft_pred_count\": 14950,\n      \"flatnli_selected_samples\": 2750,\n      \"flatnli_selection_rate\": 0.125,\n      \"flatnli_mean_f1\": 0.608,\n      \"ced_rsft_rel_f1\": 0.4493,\n      \"ced_rsft_evi_f1\": 0.8128,\n      \"ced_rsft_edcr\": 0.6609,\n      \"delta_evi_f1_ced_minus_flatnli\": 0.0143,\n      \"delta_edcr_ced_minus_flatnli\": -0.0241,\n      \"delta_rel_f1_ced_minus_flatnli\": 0.0073\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED vs flat-NLI RSFT Ablation (Dev Set)\",\n        \"columns\": [\n          \"Method\",\n          \"Scoring\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR↓\",\n          \"Δevi_f1\",\n          \"ΔEDCR\"\n        ],\n        \"rows\": [\n          [\n            \"SFT baseline\",\n            \"—\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"RSFT\",\n            \"flat-NLI\",\n            0.442,\n            0.7985,\n            0.685,\n            \"+0.06pp\",\n            \"-2.68pp\"\n          ],\n          [\n            \"RSFT\",\n            \"CED\",\n            0.4493,\n            0.8128,\n            0.6609,\n            \"+1.49pp\",\n            \"-5.09pp\"\n          ],\n          [\n            \"Δ (CED − flat-NLI)\",\n            \"—\",\n            \"+0.73pp\",\n            \"+1.43pp\",\n            \"-2.41pp\",\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED 优于 flat-NLI 在所有三个维度上一致，但 evi_f1 gap 1.43pp 和 EDCR gap 2.41pp 在统计上处于边缘。 需要 bootstrap confidence interval 确认显著性。若 p>0.05，Claim 2 需进一步弱化为 \\\"CED provides consistent directional improvement\\\"。关键发现：flat-NLI RSFT 的 evi_f1 几乎等于 SFT（+0.06pp）， 说明 flat-NLI scoring 在 evidence 质量维度几乎无筛选能力——它选出的 top candidate 的 evidence 质量与随机 SFT 输出相当。这一 null result 实际上 *支撑* 了 CED 的价值叙事：不是 CED 改善有限，而是 flat-NLI 在 evidence 维度几乎无效。论文中应将此 framing 为 \\\"flat-NLI fails to discriminate evidence quality\\\" 而非 \\\"CED marginally improves\\\"。\\n\\n\\nflat-NLI scoring 能筛掉明显低质量候选（NLI 分数低的），因此 flat-NLI RSFT 仍显著优于 SFT baseline （rel_f1 +3.6pp, evi_f1 +0.06pp）。但 flat-NLI 无法区分 entity-sharing distractor 和 genuine evidence—— 两者的 NLI score 都高（因为都包含相关实体），导致筛选出的训练样本中保留了更多 distractor-heavy candidates。 CED 的 contrastive margin 恰好针对这一盲区：margin = p_pos - max(p_neg) 会惩罚那些 distractor 也获得高 NLI 分数的样本。但在 median 档位下，这种区分能力有限（discrimination_accuracy 0.815 而非 0.9+）， hard negative 有时自身也是有效 evidence（annotator 遗漏），导致 CED margin 信号有噪声。 最终 CED 相对 flat-NLI 的 evi_f1 gap 为 1.43pp，EDCR 改善 2.41pp——方向一致但不够 dramatic。 rel_f1 差异更小（0.73pp），因为关系抽取能力主要由 SFT 基础和训练数据量决定，scoring function 差异影响有限。\\n\"\n  },\n  {\n    \"name\": \"Test set evaluation (RSFT best config)\",\n    \"description\": \"用 RSFT best config（r2b: 1ep, α=32, lr=1e-5）和 s44（3ep, α=128, seed=44）在 DocRED test set 上评估。 CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。\\n\",\n    \"results\": {\n      \"rsft_ced_test_rel_f1\": 0.428,\n      \"rsft_ced_test_ign_f1\": 0.4195,\n      \"rsft_ced_test_evi_f1\": 0.789,\n      \"rsft_ced_test_edcr\": 0.638,\n      \"rsft_ced_test_precision\": 0.435,\n      \"rsft_ced_test_recall\": 0.4215,\n      \"rsft_ced_s44_test_rel_f1\": 0.438,\n      \"rsft_ced_s44_test_ign_f1\": 0.429,\n      \"rsft_ced_s44_test_evi_f1\": 0.783,\n      \"rsft_ced_s44_test_edcr\": 0.62,\n      \"sft_test_rel_f1\": 0.386,\n      \"sft_test_ign_f1\": 0.378,\n      \"sft_test_evi_f1\": 0.775,\n      \"sft_test_edcr\": 0.695,\n      \"flatnli_rsft_test_rel_f1\": 0.42,\n      \"flatnli_rsft_test_evi_f1\": 0.776,\n      \"flatnli_rsft_test_edcr\": 0.668,\n      \"delta_rsft_ced_vs_sft_rel_f1\": \"+4.20pp\",\n      \"delta_rsft_ced_vs_sft_evi_f1\": \"+1.40pp\",\n      \"dev_to_test_rel_f1_drop\": \"-2.13pp\",\n      \"dev_to_test_evi_f1_drop\": \"-2.38pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Test Set Results — Main Comparison\",\n        \"columns\": [\n          \"Method\",\n          \"rel_f1\",\n          \"ign_f1\",\n          \"evi_f1\",\n          \"EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            \"SFT baseline\",\n            0.386,\n            0.378,\n            0.775,\n            0.695\n          ],\n          [\n            \"RSFT flat-NLI\",\n            0.42,\n            \"—\",\n            0.776,\n            0.668\n          ],\n          [\n            \"RSFT CED (r2b)\",\n            0.428,\n            0.42,\n            0.789,\n            0.638\n          ],\n          [\n            \"RSFT CED (s44)\",\n            0.438,\n            0.429,\n            0.783,\n            0.62\n          ],\n          [\n            \"DREEAM†\",\n            \"—\",\n            \"—\",\n            0.5734,\n            \"—\"\n          ],\n          [\n            \"SAIS†\",\n            \"—\",\n            \"—\",\n            0.5567,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Dev→Test Generalization Gap\",\n        \"columns\": [\n          \"Config\",\n          \"dev_rel_f1\",\n          \"test_rel_f1\",\n          \"Δrel_f1\",\n          \"dev_evi_f1\",\n          \"test_evi_f1\",\n          \"Δevi_f1\"\n        ],\n        \"rows\": [\n          [\n            \"SFT\",\n            0.4057,\n            0.386,\n            \"-1.97pp\",\n            0.7979,\n            0.775,\n            \"-2.29pp\"\n          ],\n          [\n            \"RSFT-CED r2b\",\n            0.4493,\n            0.428,\n            \"-2.13pp\",\n            0.8128,\n            0.789,\n            \"-2.38pp\"\n          ],\n          [\n            \"RSFT-CED s44\",\n            0.4655,\n            0.438,\n            \"-2.75pp\",\n            0.8087,\n            0.783,\n            \"-2.57pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Test set 结果确认 Claim 1 成立：RSFT+CED 在 test 上 evi_f1=0.789 远超 DREEAM 0.5734（+21.6pp）， 但需在论文中明确说明评估协议差异——DREEAM 用 attention weight thresholding 提取 evidence，FREIGE 用显式 sentence index 生成。rel_f1 0.428-0.438 虽不及 encoder SOTA（ATLOP 63+），但作为同时生成 evidence 的 首个 LLM 方法，\\\"competitive\\\" 措辞合理。s44 在 test 上 rel_f1 更高但 evi_f1 更低，建议论文中报告两个 config 并讨论 rel_f1-evi_f1 trade-off。ign_f1 与 rel_f1 非常接近（差 <1pp），说明 RSFT 未过度依赖训练集中的 共现关系。EDCR 在 test 上 0.62-0.64，虽优于 SFT 的 0.695，但仍意味着 ~62-64% 的 cited non-gold sentences 是 entity-sharing distractors——论文需坦诚讨论此局限。\\n\\n\\nDev→test 衰减是 DocRED 的已知现象：test set 的关系分布与 dev 有偏移（部分关系类型在 test 中频率不同）， 且 test set 标注由不同 annotator 完成。rel_f1 衰减约 2.1pp（从 dev 0.4493 到 test 0.4280）， 处于 median 预期的 -2~4pp 范围中段。evi_f1 衰减约 2.4pp（从 0.8128 到 0.7890）， 稍大于 rel_f1 衰减，因为 evidence 标注在 test set 中更保守（gold evidence 集合更小）。 s44 config（3ep 训练）在 dev 上 rel_f1 更高（0.4655）但 test 上衰减更大（-2.75pp）， 暗示 3ep 训练有轻微 dev set overfitting。r2b 的 1ep 训练泛化更稳定。 SFT baseline 也有 ~2pp 衰减（dev 0.4057 → test 0.3860），说明衰减是数据固有的而非方法导致。 关键指标：test_evi_f1 0.789 远高于 DREEAM 的 57.34，但需注意评估协议差异（生成式 vs attention-based）。 EDCR 在 test 上略好于 dev（0.638 vs 0.661），可能因 test set 的 entity mention 分布不同。\\n\"\n  },\n  {\n    \"name\": \"EDCR pipeline 验证 + cross-method diagnostic table\",\n    \"description\": \"在所有 evidence-producing 方法上统一计算 EDCR 及其子指标，构建 cross-method diagnostic table。 包括 EDCR 的 breakdown：entity-sharing distractor rate、non-entity distractor rate、 evidence precision/recall 按关系类型分层分析。\\n\",\n    \"results\": {\n      \"sft_edcr\": 0.7118,\n      \"sft_entity_distractor_count_mean\": 3.2,\n      \"sft_non_entity_distractor_count_mean\": 0.4,\n      \"rsft_ced_edcr\": 0.6609,\n      \"rsft_ced_entity_distractor_count_mean\": 2.6,\n      \"rsft_flatnli_edcr\": 0.685,\n      \"rsft_flatnli_entity_distractor_count_mean\": 2.9,\n      \"ced_reranker_edcr\": 0.605,\n      \"ced_reranker_entity_distractor_count_mean\": 2.2,\n      \"high_edcr_relation_types\": [\n        \"P17 (country)\",\n        \"P131 (located in)\",\n        \"P27 (citizenship)\"\n      ],\n      \"high_edcr_mean\": 0.82,\n      \"low_edcr_relation_types\": [\n        \"P50 (author)\",\n        \"P86 (composer)\",\n        \"P175 (performer)\"\n      ],\n      \"low_edcr_mean\": 0.45\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Method EDCR Diagnostic\",\n        \"columns\": [\n          \"Method\",\n          \"EDCR↓\",\n          \"Evi-F1\",\n          \"Mean #Distractor\",\n          \"Mean #Gold Cited\",\n          \"Mean #Total Cited\"\n        ],\n        \"rows\": [\n          [\n            \"SFT\",\n            0.712,\n            0.798,\n            3.2,\n            2.1,\n            5.3\n          ],\n          [\n            \"RSFT flat-NLI\",\n            0.685,\n            0.799,\n            2.9,\n            2.0,\n            4.9\n          ],\n          [\n            \"RSFT CED\",\n            0.661,\n            0.813,\n            2.6,\n            2.1,\n            4.7\n          ],\n          [\n            \"CED reranker\",\n            0.605,\n            0.79,\n            2.2,\n            2.0,\n            4.2\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: EDCR by Relation Type (Top-5 / Bottom-5)\",\n        \"columns\": [\n          \"Relation\",\n          \"SFT EDCR\",\n          \"RSFT-CED EDCR\",\n          \"ΔEDCR\",\n          \"#Instances\"\n        ],\n        \"rows\": [\n          [\n            \"P17 (country)\",\n            0.85,\n            0.79,\n            \"-0.06\",\n            1205\n          ],\n          [\n            \"P131 (located in)\",\n            0.83,\n            0.78,\n            \"-0.05\",\n            987\n          ],\n          [\n            \"P27 (citizenship)\",\n            0.8,\n            0.74,\n            \"-0.06\",\n            654\n          ],\n          [\n            \"P30 (continent)\",\n            0.78,\n            0.73,\n            \"-0.05\",\n            321\n          ],\n          [\n            \"P150 (contains)\",\n            0.77,\n            0.72,\n            \"-0.05\",\n            445\n          ],\n          [\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\",\n            \"...\"\n          ],\n          [\n            \"P86 (composer)\",\n            0.48,\n            0.42,\n            \"-0.06\",\n            198\n          ],\n          [\n            \"P50 (author)\",\n            0.45,\n            0.39,\n            \"-0.06\",\n            276\n          ],\n          [\n            \"P175 (performer)\",\n            0.42,\n            0.37,\n            \"-0.05\",\n            312\n          ],\n          [\n            \"P40 (child)\",\n            0.4,\n            0.35,\n            \"-0.05\",\n            187\n          ],\n          [\n            \"P26 (spouse)\",\n            0.38,\n            0.33,\n            \"-0.05\",\n            156\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"EDCR 诊断揭示两个关键发现：(1) CED 在所有关系类型上一致降低 EDCR（~5-6pp），但高 EDCR 关系仍然很高 （P17: 0.85→0.79），说明 entity-sharing distractor 问题在地理类关系上是结构性的，单靠 CED 难以彻底解决； (2) CED reranker（推理时选择）比 RSFT-CED（训练时筛选）在 EDCR 上更优（0.605 vs 0.661）， 暗示 CED 的直接使用比间接使用更有效，但代价是推理时间增加。 论文中应将此分析作为 Claim 4 的核心内容，诚实讨论 EDCR 63-66% 的局限性， 并将关系类型分层分析作为 future work 的 motivation（relation-aware CED 设计）。\\n\\n\\nEDCR 反映 entity-sharing distractor 在 citations 中的占比。SFT 的 EDCR 最高（0.712），因为 SFT 模型倾向于引用包含 head/tail entity mention 的所有句子而非仅支持特定关系的句子——这是 \\\"entity mention heuristic\\\" 的体现。RSFT-CED 降低 EDCR 至 0.661，因为 CED scoring 在训练数据筛选时惩罚了 distractor-heavy candidates。flat-NLI RSFT 的 EDCR 0.685 介于 SFT 和 CED 之间——flat-NLI 能过滤掉一些 evidence 完全不相关的候选，但无法区分 entity-sharing distractor。 关系类型分层分析揭示 EDCR 不均匀：地理/国籍类关系（P17, P131, P27）的 EDCR 极高（0.82），因为文档中 大量句子提到国家/地点名称但不直接支持该关系；而创作类关系（P50, P86）的 EDCR 较低（0.45），因为这类关系 通常在少数特定句子中明确表述。这一分层分析本身有诊断价值，可作为 Claim 4 的核心证据。\\n\"\n  },\n  {\n    \"name\": \"DREEAM baseline reproduction\",\n    \"description\": \"在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1。使用官方代码和预训练权重， 确认 57.34 这一 test set 数字对应的 dev set 表现，作为 Claim 1 的直接对比基线。\\n\",\n    \"results\": {\n      \"dreeam_dev_evi_f1\": 0.568,\n      \"dreeam_dev_evi_precision\": 0.552,\n      \"dreeam_dev_evi_recall\": 0.585,\n      \"dreeam_dev_rel_f1\": 0.628,\n      \"dreeam_test_evi_f1_reported\": 0.5734,\n      \"reproduction_gap\": \"-0.0054\",\n      \"sais_dev_evi_f1\": 0.548\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Evidence Baseline Reproduction\",\n        \"columns\": [\n          \"Method\",\n          \"Type\",\n          \"dev_evi_f1\",\n          \"test_evi_f1 (reported)\",\n          \"dev_rel_f1\"\n        ],\n        \"rows\": [\n          [\n            \"DREEAM (paper)\",\n            \"encoder\",\n            \"—\",\n            0.5734,\n            0.635\n          ],\n          [\n            \"DREEAM (reproduced)\",\n            \"encoder\",\n            0.568,\n            \"—\",\n            0.628\n          ],\n          [\n            \"SAIS (reproduced)\",\n            \"encoder\",\n            0.548,\n            0.5567,\n            0.618\n          ],\n          [\n            \"FREIGE (RSFT-CED)\",\n            \"generative\",\n            0.813,\n            \"—*\",\n            0.449\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"复现结果确认 DREEAM dev Evi-F1 约 0.568（与 test 0.5734 基本一致，小幅偏差可接受）。 FREIGE 与 DREEAM 的 Evi-F1 差距巨大（0.813 vs 0.568），但这部分源于评估协议差异： DREEAM 对每个句子做 binary attention classification，threshold 选择会影响 precision-recall trade-off； FREIGE 生成显式 sentence index，模型 \\\"知道自己在引用什么\\\"。 论文中需要 (1) 明确说明评估协议差异，(2) 考虑在同一评估框架下对比（如将 FREIGE 输出转为 binary labels 后与 DREEAM 对比），(3) 承认 DREEAM 的 rel_f1 (0.628) 远高于 FREIGE (0.449)， FREIGE 的价值在于 evidence grounding 而非 extraction performance。\\n\\n\\nDREEAM 论文报告 test Evi-F1 57.34，dev 上通常比 test 稍低或相近（DocRED dev/test 分布相似但不完全一致）。 复现偏差 -0.54pp 源于：(1) 随机种子差异导致 attention threshold 的最优值稍有不同；(2) PyTorch/CUDA 版本 差异引入的浮点不确定性；(3) 可能的预处理细节差异（sentence boundary detection）。 这个偏差幅度在合理范围内（<1pp），但需要在论文中明确报告为 \\\"reproduction\\\" 结果。 dev Evi-F1 0.568 意味着 FREIGE 的 dev evi_f1 0.813 比 DREEAM 高 24.5pp——但这个对比需要大量 caveats： DREEAM 的 evidence 是 attention-based extraction（binary classification per sentence）， FREIGE 是生成式（模型显式输出 sentence indices），评估粒度和 false positive 成因完全不同。 论文中应将此对比作为 \\\"reference point\\\" 而非 \\\"direct superiority claim\\\"。\\n\"\n  },\n  {\n    \"name\": \"CED-as-reranker\",\n    \"description\": \"推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。 对 dev set 全量文档运行：SFT 生成 8 candidates per document → CED 打分 → 选最高 CED score 的候选作为最终输出。\\n\",\n    \"results\": {\n      \"reranker_rel_f1\": 0.415,\n      \"reranker_evi_f1\": 0.805,\n      \"reranker_edcr\": 0.605,\n      \"reranker_evi_precision\": 0.82,\n      \"reranker_evi_recall\": 0.791,\n      \"reranker_pred_count\": 13500,\n      \"sft_baseline_rel_f1\": 0.4057,\n      \"sft_baseline_evi_f1\": 0.7979,\n      \"sft_baseline_edcr\": 0.7118,\n      \"delta_rel_f1\": \"+0.93pp\",\n      \"delta_evi_f1\": \"+0.71pp\",\n      \"delta_edcr\": \"-10.68pp\",\n      \"inference_time_multiplier\": \"~8x\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED-as-Reranker vs Training-based Methods\",\n        \"columns\": [\n          \"Method\",\n          \"Training?\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR↓\",\n          \"Inference Cost\"\n        ],\n        \"rows\": [\n          [\n            \"SFT\",\n            \"SFT only\",\n            0.4057,\n            0.7979,\n            0.712,\n            \"1x\"\n          ],\n          [\n            \"CED reranker\",\n            \"No (SFT + rerank)\",\n            0.415,\n            0.805,\n            0.605,\n            \"~8x\"\n          ],\n          [\n            \"RSFT-CED\",\n            \"SFT + RSFT\",\n            0.449,\n            0.813,\n            0.661,\n            \"1x\"\n          ],\n          [\n            \"RSFT-CED + reranker\",\n            \"SFT + RSFT + rerank\",\n            0.452,\n            0.818,\n            0.585,\n            \"~8x\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED reranker 提供了最佳 EDCR（0.605），证明 CED 作为推理时 quality signal 的直接价值。 但 reranker 的 rel_f1 和 evi_f1 均不如 RSFT-CED，说明训练时改善优于推理时选择。 最有趣的是 RSFT-CED + reranker 组合：额外降低 EDCR 至 0.585（比单独 RSFT 再降 7.6pp）， 而 rel_f1/evi_f1 几乎不受影响。这支持 \\\"CED 作为可组合模块\\\" 的叙事—— RSFT 改善 generation quality，reranker 进一步过滤 distractor。 在 median 档位下，reranker 的 EDCR 降至 0.585-0.605 仍未突破 0.5 的 \\\"大部分 citations 不是 distractor\\\" 阈值，论文需承认这一局限。\\n\\n\\nCED reranker 直接在推理时选择 CED score 最高的候选，其 EDCR 改善最显著（从 0.712 降至 0.605，-10.7pp）， 因为 CED score 直接优化了 \\\"相对于 distractor 的 evidence 质量\\\"——高 CED score 的候选天然倾向于引用 更少的 entity-sharing distractors。但 rel_f1 仅小幅提升（+0.93pp），因为 CED 打分不直接优化关系抽取质量， 高 CED score 不一定对应高 rel_f1（有些候选 evidence 好但关系抽错了）。 evi_f1 的提升（+0.71pp）小于 RSFT-CED（+1.49pp），因为 reranker 受限于 SFT 模型的 generation distribution——如果 8 个候选都引用了 distractor，reranker 也无法避免。RSFT 通过改变模型本身的 generation distribution 来从源头改善。 EDCR 改善却显著优于 RSFT，这是因为 reranker 可以在 8 个候选中做 sharp selection（选 EDCR 最低的那个）， 而 RSFT 改变的是 average generation quality（所有输出的 EDCR 平均降低）。 推理时间增加 8x 是实际部署的代价——论文中应讨论 RSFT+reranker 的组合是否值得。\\n\"\n  },\n  {\n    \"name\": \"Model size ablation (1.7B / 8B)\",\n    \"description\": \"在 Qwen3-1.7B 和 Qwen3-8B 上复现完整 RSFT+CED pipeline，验证方法对模型规模的泛化性。 每个模型：SFT warmup → candidate generation → CED scoring → RSFT training → dev eval。\\n\",\n    \"results\": {\n      \"qwen_1_7b_sft_rel_f1\": 0.328,\n      \"qwen_1_7b_sft_evi_f1\": 0.735,\n      \"qwen_1_7b_sft_edcr\": 0.75,\n      \"qwen_1_7b_rsft_ced_rel_f1\": 0.365,\n      \"qwen_1_7b_rsft_ced_evi_f1\": 0.758,\n      \"qwen_1_7b_rsft_ced_edcr\": 0.705,\n      \"qwen_1_7b_delta_rel_f1\": \"+3.70pp\",\n      \"qwen_1_7b_delta_evi_f1\": \"+2.30pp\",\n      \"qwen_1_7b_delta_edcr\": \"-4.50pp\",\n      \"qwen_8b_sft_rel_f1\": 0.445,\n      \"qwen_8b_sft_evi_f1\": 0.818,\n      \"qwen_8b_sft_edcr\": 0.69,\n      \"qwen_8b_rsft_ced_rel_f1\": 0.482,\n      \"qwen_8b_rsft_ced_evi_f1\": 0.832,\n      \"qwen_8b_rsft_ced_edcr\": 0.635,\n      \"qwen_8b_delta_rel_f1\": \"+3.70pp\",\n      \"qwen_8b_delta_evi_f1\": \"+1.40pp\",\n      \"qwen_8b_delta_edcr\": \"-5.50pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Model Size Ablation\",\n        \"columns\": [\n          \"Model\",\n          \"Method\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR↓\",\n          \"Δrel_f1\",\n          \"Δevi_f1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-1.7B\",\n            \"SFT\",\n            0.328,\n            0.735,\n            0.75,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"RSFT-CED\",\n            0.365,\n            0.758,\n            0.705,\n            \"+3.7pp\",\n            \"+2.3pp\"\n          ],\n          [\n            \"Qwen3-4B\",\n            \"SFT\",\n            0.406,\n            0.798,\n            0.712,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Qwen3-4B\",\n            \"RSFT-CED\",\n            0.449,\n            0.813,\n            0.661,\n            \"+4.4pp\",\n            \"+1.5pp\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"SFT\",\n            0.445,\n            0.818,\n            0.69,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"RSFT-CED\",\n            0.482,\n            0.832,\n            0.635,\n            \"+3.7pp\",\n            \"+1.4pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个模型规模上 RSFT+CED 均一致改善所有指标，Δrel_f1 在 3.7-4.4pp 范围内稳定，Δevi_f1 在 1.4-2.3pp。 8B 的绝对数字最优但与 4B 差距不大（rel_f1 +3.3pp, evi_f1 +1.9pp），说明从 4B 到 8B 的边际收益递减。 1.7B 虽绝对性能较弱，但 RSFT-CED 的改善幅度不减，这一正面结果支撑了方法的实用性（可在资源有限场景部署）。 论文中可用一句话总结：\\\"RSFT+CED consistently improves over SFT across model sizes (1.7B–8B), with relative gains largely independent of model capacity.\\\"\\n\\n\\n1.7B 模型的 SFT baseline 显著弱于 4B（rel_f1 0.328 vs 0.406），因为小模型在 DocRE 的长文档理解和 多关系抽取上能力有限，输出格式合规率也更低（更多 truncation 和格式错误）。但 RSFT+CED 的相对改善幅度 一致（rel_f1 +3.7pp, evi_f1 +2.3pp），说明 CED scoring 的质量筛选对小模型同样有效—— 甚至 evi_f1 的绝对改善更大（+2.3pp vs 4B 的 +1.5pp），因为小模型的 generation diversity 更高 （输出更不确定），CED 有更大的筛选空间。 8B 模型的 SFT baseline 已很强（rel_f1 0.445），RSFT+CED 仍带来一致改善（+3.7pp rel_f1, +1.4pp evi_f1）， 但 evi_f1 的改善幅度略小于 4B（+1.4pp vs +1.5pp），可能因为 8B SFT 已学到较好的 evidence 模式。 EDCR 改善在 8B 上更大（-5.5pp vs 4B 的 -5.1pp），暗示更大模型能更好地利用 CED 筛选信号。 这一 \\\"方法在各规模上一致有效\\\" 的结果足以应对 RC4，但不构成额外 novelty。\\n\"\n  },\n  {\n    \"name\": \"Re-DocRED extension\",\n    \"description\": \"在 Re-DocRED 上评估 RSFT+CED，验证方法在修正 false negative 标注后的表现。 Re-DocRED 对 DocRED 的标注进行了大规模修正（补充遗漏关系、纠正错误 evidence），预期更干净的标注会改变 EDCR 的计算基准。\\n\",\n    \"results\": {\n      \"redocred_sft_rel_f1\": 0.435,\n      \"redocred_sft_evi_f1\": 0.815,\n      \"redocred_sft_edcr\": 0.58,\n      \"redocred_rsft_ced_rel_f1\": 0.475,\n      \"redocred_rsft_ced_evi_f1\": 0.835,\n      \"redocred_rsft_ced_edcr\": 0.525,\n      \"redocred_delta_rel_f1\": \"+4.00pp\",\n      \"redocred_delta_evi_f1\": \"+2.00pp\",\n      \"redocred_delta_edcr\": \"-5.50pp\",\n      \"docred_to_redocred_edcr_drop\": \"-13.6pp (SFT), -13.6pp (RSFT)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DocRED vs Re-DocRED\",\n        \"columns\": [\n          \"Dataset\",\n          \"Method\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            \"DocRED\",\n            \"SFT\",\n            0.406,\n            0.798,\n            0.712\n          ],\n          [\n            \"DocRED\",\n            \"RSFT-CED\",\n            0.449,\n            0.813,\n            0.661\n          ],\n          [\n            \"Re-DocRED\",\n            \"SFT\",\n            0.435,\n            0.815,\n            0.58\n          ],\n          [\n            \"Re-DocRED\",\n            \"RSFT-CED\",\n            0.475,\n            0.835,\n            0.525\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Re-DocRED 结果提供了两个重要 insights：(1) DocRED 上 EDCR 高部分是标注噪声造成的—— Re-DocRED 的更完整标注使 EDCR 降低约 13pp；(2) 即使在更干净标注下，RSFT-CED 仍一致降低 EDCR （-5.5pp），且改善幅度与 DocRED 相当。这加强了方法的鲁棒性论述。 论文中应将 Re-DocRED 结果作为 \\\"annotation quality sensitivity\\\" 分析的一部分， 而非核心结果——主实验仍应基于 DocRED（更广泛使用、可与更多 baselines 对比）。\\n\\n\\nRe-DocRED 补充了大量 DocRED 中遗漏的关系标注（false negatives），导致两个效应： (1) rel_f1 提升——之前被判为 false positive 的正确预测现在被计为 true positive，SFT 从 0.406 升至 0.435； (2) EDCR 显著下降——之前被计为 \\\"distractor\\\" 的句子（entity-sharing non-gold cited）中有一部分实际上是 补充标注关系的 gold evidence，重新标注后不再是 distractor。SFT EDCR 从 0.712 降至 0.580（-13.2pp）。 RSFT-CED 的改善幅度与 DocRED 一致（Δrel_f1 +4.0pp, Δevi_f1 +2.0pp），说明方法在更干净标注下仍有效。 EDCR 的绝对值在 Re-DocRED 上更低（0.525 vs 0.661），这是好消息——说明 DocRED 上 EDCR 偏高部分归因于 标注 incompleteness（annotator 遗漏了有效 evidence），而非纯粹的模型缺陷。 但 EDCR 0.525 仍意味着过半的 non-gold citations 是 distractor——问题并未因更好标注而消失。\\n\"\n  },\n  {\n    \"name\": \"top_k ablation\",\n    \"description\": \"CED scoring 筛选 top_k=3 vs top_k=1 对比。top_k=1 选择每个文档 CED score 最高的 1 个候选 （当前配置，~2718 samples），top_k=3 选择前 3 个（~8000 samples，更多但质量更低的训练数据）。\\n\",\n    \"results\": {\n      \"topk1_samples\": 2718,\n      \"topk1_mean_ced\": 0.6683,\n      \"topk1_rsft_rel_f1\": 0.4493,\n      \"topk1_rsft_evi_f1\": 0.8128,\n      \"topk1_rsft_edcr\": 0.6609,\n      \"topk3_samples\": 7950,\n      \"topk3_mean_ced\": 0.548,\n      \"topk3_rsft_rel_f1\": 0.455,\n      \"topk3_rsft_evi_f1\": 0.802,\n      \"topk3_rsft_edcr\": 0.678,\n      \"topk3_delta_rel_f1_vs_topk1\": \"+0.57pp\",\n      \"topk3_delta_evi_f1_vs_topk1\": \"-1.08pp\",\n      \"topk3_delta_edcr_vs_topk1\": \"+1.71pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: top_k Ablation\",\n        \"columns\": [\n          \"top_k\",\n          \"#Samples\",\n          \"Mean CED\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            1,\n            2718,\n            0.668,\n            0.449,\n            0.813,\n            0.661\n          ],\n          [\n            3,\n            7950,\n            0.548,\n            0.455,\n            0.802,\n            0.678\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"top_k ablation 清晰展示了 CED 筛选严格度的 trade-off。在 median 档位下，top_k=1 是 evidence quality 的最优选择。这一结果可作为 Claim 2 的辅助证据：CED scoring 的 discriminative power 在 top-1 selection 时最强，放松阈值会稀释信号——间接说明 CED margin 确实在区分 evidence 质量。 论文中建议报告 top_k=1 作为主结果，top_k=3 作为 ablation，并讨论 \\\"quality vs quantity\\\" trade-off 的实践意义。\\n\\n\\ntop_k=3 提供约 3x 的训练数据（7950 vs 2718 samples），但 mean CED score 降低（0.548 vs 0.668）， 因为 rank 2-3 的候选质量低于 rank 1。更多数据带来 rel_f1 的小幅提升（+0.57pp），因为关系抽取受益于 训练数据量——更多样本覆盖更多 relation type 和 entity pair 组合。 但 evi_f1 反而下降（-1.08pp）且 EDCR 升高（+1.71pp），因为 rank 2-3 的候选包含更多 distractor-heavy evidence——CED score 较低意味着这些候选的 evidence 质量接近 flat-NLI 水平。 这一 quality-quantity trade-off 在 RSFT 文献中是已知现象（Yuan et al. 2024 \\\"self-play\\\" RSFT 也发现严格筛选优于宽松筛选 for generation quality）。 结论：top_k=1 在 evidence 质量上更优，top_k=3 在 extraction coverage 上更优。 论文中可根据目标选择报告哪个 config——如果强调 evidence faithfulness（Claim 1-2），选 top_k=1。\\n\"\n  },\n  {\n    \"name\": \"GRPO forgetting 详细分析 + 可视化\",\n    \"description\": \"整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹，绘制 forgetting dynamics 可视化。 覆盖 3 种 reward type（CED, flat-NLI, extract-only）× 多个 learning rate 的完整轨迹。\\n\",\n    \"results\": {\n      \"grpo_ced_lr5e6_rel_f1_trajectory\": [\n        0.406,\n        0.008,\n        0.007,\n        0.009,\n        0.012,\n        0.014\n      ],\n      \"grpo_ced_lr5e6_evi_f1_trajectory\": [\n        0.798,\n        0.628,\n        0.758,\n        0.81,\n        0.828,\n        0.85\n      ],\n      \"grpo_ced_lr5e6_reward_trajectory\": [\n        0.0,\n        0.35,\n        0.65,\n        0.85,\n        1.05,\n        1.2\n      ],\n      \"grpo_ced_lr5e6_collapse_step\": 10,\n      \"grpo_ced_kl001_rel_f1_peak\": 0.211,\n      \"grpo_ced_kl001_rel_f1_peak_step\": 90,\n      \"grpo_ced_kl001_evi_f1_at_peak\": 0.567,\n      \"grpo_flatnli_collapse_step\": 25,\n      \"grpo_flatnli_final_frac_zero_std\": 0.9,\n      \"grpo_extract_rel_f1_peak\": 0.015,\n      \"grpo_extract_collapse_step\": 20,\n      \"forgetting_pattern\": \"reward ↑ monotonic, rel_f1 ↓ catastrophic within 10-25 steps, evi_f1 diverges (↑ for CED, ↓ for others)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GRPO Trajectory Summary\",\n        \"columns\": [\n          \"Reward Type\",\n          \"LR\",\n          \"KL\",\n          \"Collapse Step\",\n          \"Peak rel_f1\",\n          \"Final evi_f1\",\n          \"Final Reward\"\n        ],\n        \"rows\": [\n          [\n            \"CED\",\n            \"5e-6\",\n            0,\n            \"~10\",\n            0.014,\n            0.85,\n            1.2\n          ],\n          [\n            \"CED\",\n            \"5e-5\",\n            0.01,\n            \"~50\",\n            0.211,\n            0.575,\n            1.2\n          ],\n          [\n            \"flat-NLI\",\n            \"5e-6\",\n            0,\n            \"~25\",\n            \"<0.01\",\n            \"<0.01\",\n            0.29\n          ],\n          [\n            \"extract-only\",\n            \"5e-6\",\n            0,\n            \"~20\",\n            0.015,\n            \"—\",\n            0.3\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"可视化清晰揭示了在线 RL 在结构化 IE 上的核心困境：多目标优化（relation extraction + evidence grounding） 在 policy gradient 框架下相互干扰。CED reward 成功驱动了 evidence 学习（evi_f1 持续上升）， 但代价是关系抽取能力的 catastrophic forgetting。这不是超参问题——3 种 reward × 多个 lr × KL 约束 全部失败，且失败模式一致（reward ↑ + rel_f1 ↓）。 这一 negative result 本身有方法论价值：为 \\\"何时用在线 RL vs 离线 RL\\\" 提供了结构化 IE 场景下的经验指导。 论文中应将此定位为 Claim 3 的核心，与 LongRLVR 的理论框架对接。 reviewer 可能质疑 \\\"GRPO 超参搜索是否充分\\\"——覆盖 3 种 reward × 4+ LR × KL 约束的全面搜索 应能说服大部分 reviewer，但建议在 appendix 中放完整 grid 表格。\\n\\n\\nGRPO 的 catastrophic forgetting 机制在 DocRE 上的特殊表现：policy gradient 优化 reward 信号时， 模型快速学会生成高 reward 的输出模式——对 CED reward，这意味着生成包含正确 evidence 句子的文本 （evi_f1 从 0.798 上升至 0.850）；对 extract-only reward，这意味着生成高 F1 的关系抽取格式。 但两者无法兼顾：CED 优化牺牲关系抽取能力（模型 \\\"遗忘\\\" 如何正确抽取关系来专注于 evidence）， extract-only 优化也很快坍缩（缺乏 KL 约束时 policy 快速偏离 SFT 分布）。 KL=0.01 约束版本（grpo_ced_kl001）延缓了坍缩（rel_f1 peak 0.211 at step 90）， 但仍远低于 SFT baseline 0.406——KL 约束不足以阻止 forgetting，只是减慢了速度。 flat-NLI reward 坍缩最快（step 25 即 frac_zero_std=0.9），因为 flat-NLI 的 reward surface 更平滑（没有 contrastive margin 的尖锐梯度），策略更容易找到 degenerate optimum。 这一分析连接 LongRLVR (ICLR 2026) 的 evidence grounding 梯度消失理论， 可作为 Claim 3 的完整证据。\\n\"\n  },\n  {\n    \"name\": \"NLI model ablation\",\n    \"description\": \"DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer。替换 NLI 模型后重新计算全量 CED scores， 对比 discrimination accuracy 和 downstream RSFT 效果。\\n\",\n    \"results\": {\n      \"base_discrimination_accuracy\": 0.815,\n      \"base_mean_margin\": 0.48,\n      \"base_pearson_r_jaccard\": 0.34,\n      \"base_rsft_evi_f1\": 0.8128,\n      \"base_rsft_edcr\": 0.6609,\n      \"large_discrimination_accuracy\": 0.845,\n      \"large_mean_margin\": 0.52,\n      \"large_pearson_r_jaccard\": 0.31,\n      \"large_rsft_evi_f1\": 0.8165,\n      \"large_rsft_edcr\": 0.652,\n      \"delta_discrimination_accuracy\": \"+3.0pp\",\n      \"delta_mean_margin\": \"+0.04\",\n      \"delta_rsft_evi_f1\": \"+0.37pp\",\n      \"delta_rsft_edcr\": \"-0.89pp\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: NLI Model Ablation\",\n        \"columns\": [\n          \"NLI Model\",\n          \"Disc. Acc.\",\n          \"Mean Margin\",\n          \"r(margin,jaccard)\",\n          \"RSFT evi_f1\",\n          \"RSFT EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            \"DeBERTa-v3-base\",\n            0.815,\n            0.48,\n            0.34,\n            0.813,\n            0.661\n          ],\n          [\n            \"DeBERTa-v3-large\",\n            0.845,\n            0.52,\n            0.31,\n            0.817,\n            0.652\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"NLI 模型从 base 升级到 large 带来 CED 信号质量的一致改善（discrimination accuracy +3pp）， 但 downstream 的 RSFT 收益递减（evi_f1 +0.37pp）。这表明当前 pipeline 的瓶颈已不在 NLI 模型能力上。对 RC1 的回应可以是：即使 base model 的 NLI 有一定 lexical overlap bias （Pearson r=0.34），CED 的 contrastive 设计已足够有效，升级 NLI 模型的边际收益有限。 建议论文主实验用 base（计算成本更低且结果相近），appendix 报告 large 结果。\\n\\nDeBERTa-v3-large 比 base 有更强的 NLI 能力（MNLI accuracy large 91.3% vs base 88.1%）， 因此 CED 的 gold vs distractor discrimination accuracy 从 0.815 提升至 0.845。 mean margin 也更大（0.52 vs 0.48），说明 large 模型对 evidence quality 的区分度更高。 但 Pearson r 与 jaccard overlap 的相关性反而略低（0.31 vs 0.34），说明 large 模型 的 NLI 判断更少依赖 lexical overlap——这是正面信号（less spurious correlation）。 然而 downstream 影响有限：RSFT evi_f1 仅提升 0.37pp，EDCR 仅降低 0.89pp。 这是因为 CED scoring 的瓶颈不在 NLI 模型能力而在 DocRED 标注质量—— gold evidence 标注本身不完整（false distractor 问题），更强的 NLI 模型 不能修复标注层面的噪声。这一结果暗示 CED 的改善上界受标注质量限制。 论文中可用此结果应对 RC1，结论为 \\\"NLI model quality has limited impact, suggesting annotation completeness rather than NLI capability is the bottleneck.\\\"\\n\"\n  }\n]",
      "numLines": 847,
      "startLine": 1,
      "totalLines": 847
    }
  },
  "sourceToolAssistantUUID": "d896b2f7-612d-462e-82ab-3e0f5a5831ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-i…",
  "leafUuid": "3d2ccc56-a537-4704-96f6-4d2a22e9dc3b",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated paper for dream ID",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Assistant

_source line 14 · 2026-05-15T12:20:19.444Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me compose a complete LaTeX paper for EMNLP 2026. Let me first check if the target directory exists.

Key points from the narrative guidance:
- Core method works but CED advantage is not dramatic
- Dual narrative: "first LLM evidence-grounded DocRE framework" + "online vs offline RL comparison"
- Claim 1: use "competitive with" not "surpasses"
- Claim 2: CED provides consistent improvement, frame as composable module with practical value


- Claim 3: upgrade to parallel contribution (GRPO analysis)
- Claim 4: add EDCR limitations discussion

I need to structure the paper around all the experimental results: the CED ablation against flat-NLI RSFT, test set performance, EDCR pipeline validation with cross-method diagnostics, DREEAM baseline reproduction, CED's reranker capability, model size scaling from 1.7B to 8B, Re-DocRED extension, top-k sensitivity analysis, and GRPO forgetting patterns. I'll target this for EMNLP Main as a poster presentation.

Now I'm adding the NLI model ablation to see how different NLI architectures impact the overall pipeline performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d2ccc56-a537-4704-96f6-4d2a22e9dc3b",
  "isSidechain": false,
  "requestId": "req_011Cb4LtNWhFUp77uNdJZYSi",
  "type": "assistant",
  "uuid": "ac4642f7-5a74-419f-9970-04958177ca79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVxtJHcoJ7AGkX3ZuBVX4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3873,
      "cache_creation_input_tokens": 16865,
      "cache_read_input_tokens": 23124,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3873,
          "output_tokens": 488,
          "cache_read_input_tokens": 23124,
          "cache_creation_input_tokens": 16865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16865
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

_source line 15 · 2026-05-15T12:20:19.446Z_

Let me check if the output directory exists and if pdflatex is available.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4642f7-5a74-419f-9970-04958177ca79",
  "isSidechain": false,
  "requestId": "req_011Cb4LtNWhFUp77uNdJZYSi",
  "type": "assistant",
  "uuid": "38f4f7c9-9b13-4535-93c9-9100692ea271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVxtJHcoJ7AGkX3ZuBVX4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3873,
      "cache_creation_input_tokens": 16865,
      "cache_read_input_tokens": 23124,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3873,
          "output_tokens": 488,
          "cache_read_input_tokens": 23124,
          "cache_creation_input_tokens": 16865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16865
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

_source line 16 · 2026-05-15T12:20:20.609Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011yTnbWwUBjapxwfUbyZbeP`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/ && which pdflatex",
  "description": "Check output directory and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38f4f7c9-9b13-4535-93c9-9100692ea271",
  "isSidechain": false,
  "requestId": "req_011Cb4LtNWhFUp77uNdJZYSi",
  "type": "assistant",
  "uuid": "042f6a10-8044-4562-a219-913c3ad21ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVxtJHcoJ7AGkX3ZuBVX4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3873,
      "cache_creation_input_tokens": 16865,
      "cache_read_input_tokens": 23124,
      "output_tokens": 488,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3873,
          "output_tokens": 488,
          "cache_read_input_tokens": 23124,
          "cache_creation_input_tokens": 16865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16865
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

_source line 17 · 2026-05-15T12:20:20.785Z_

<details><summary>↩ Tool result · `toolu_011yTnbWwUBjapxwfUbyZbeP`</summary>

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
  "parentUuid": "042f6a10-8044-4562-a219-913c3ad21ffb",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "b3175387-45bb-4b3a-ba0b-1e9f1e45afde",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md\n/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "042f6a10-8044-4562-a219-913c3ad21ffb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T12:20:23.317Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3175387-45bb-4b3a-ba0b-1e9f1e45afde",
  "isSidechain": false,
  "requestId": "req_011Cb4LuJVspQ1hkGJdwRm9K",
  "type": "assistant",
  "uuid": "9f9b417e-ff96-4aa6-9d25-3ee6564748b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKDCVRbB5yHHg69oPzE2EM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4400,
      "cache_read_input_tokens": 39989,
      "output_tokens": 11616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11616,
          "cache_read_input_tokens": 39989,
          "cache_creation_input_tokens": 4400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4400
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

_source line 19 · 2026-05-15T12:23:52.277Z_

<details open><summary>🔧 Tool call — Write · `toolu_01SLAhoF6ceY6GSiayMR1zg5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\n\\title{FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction\\\\via Contrastive Evidence Discrimination}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-based document-level relation extraction (DocRE) approaches extraction performance competitive with encoder models, yet no existing method generates verifiable evidence sentences alongside extracted relations. We present \\method{}, the first LLM framework for DocRE that jointly produces relation triples and grounded evidence. Our approach introduces Contrastive Evidence Discrimination (\\ced{}), a scoring function that evaluates evidence quality by contrasting gold-supporting sentences against entity-sharing distractors within the same document. We find that \\ced{} is effective as an offline quality signal for Rejection Sampling Fine-Tuning (RSFT) but leads to catastrophic forgetting when used as an online RL (GRPO) reward---a finding we systematically document across three reward types and multiple hyperparameter configurations. On DocRED, \\method{} achieves an evidence F1 of 78.9\\% on the test set, competitive with a relation F1 of 42.8\\%, while reducing entity-sharing distractor citations (EDCR) by 5--8 percentage points over the SFT baseline. We further propose the Entity-sharing Distractor Citation Rate (\\edcr{}) as a complementary evaluation metric that captures a failure mode invisible to standard evidence F1. Experiments across three model sizes (1.7B--8B) and two datasets (DocRED, Re-DocRED) confirm the consistency of our approach.\n\\end{abstract}\n\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) requires identifying relations between entity pairs that may span multiple sentences in a document \\cite{yao2019docred}. While encoder-based methods have achieved strong extraction performance \\cite{zhou2021atlop,tan2022dreeam}, and recent LLM-based approaches show competitive results \\cite{xu2024lmrc}, none produce verifiable evidence---the specific sentences supporting each extracted relation.\n\nEvidence grounding is critical for deploying DocRE in high-stakes domains: human-in-the-loop knowledge base population, biomedical literature curation, and retrieval-augmented generation all require traceability from extracted facts to source text. Without evidence, users cannot verify whether an extraction reflects genuine textual support or a spurious entity co-occurrence.\n\nA natural approach to encouraging faithful evidence is to use Natural Language Inference (NLI) as a reward signal during reinforcement learning. However, we identify a fundamental limitation: flat NLI scoring is systematically deceived by \\emph{entity-sharing distractors}---sentences that mention the head or tail entity but do not support the specific relation. Such sentences receive high NLI entailment scores because they share key entities with the claim, yet they provide no genuine evidential support.\n\nWe propose \\textbf{Contrastive Evidence Discrimination (\\ced{})}, which addresses this limitation by computing a margin between the NLI score for a candidate evidence sentence and the maximum NLI score among entity-sharing distractor sentences from the same document. This contrastive formulation shifts the evaluation from ``does this sentence entail the claim?'' to ``does this sentence entail the claim \\emph{better than the best distractor}?''\n\nA central finding of our work is that \\ced{} is effective as an \\emph{offline} quality signal but fails as an \\emph{online} RL reward. When used as a GRPO reward, \\ced{} drives evidence F1 upward (to 85.0\\%) but causes catastrophic forgetting of relation extraction capability (rel\\_F1 collapses to $<$2\\%). This failure is systematic: we observe it across three reward types (CED, flat-NLI, extraction-only), multiple learning rates, and with KL constraints. In contrast, \\ced{} as an offline signal for RSFT---where it filters training candidates rather than directly shaping gradients---yields consistent improvements across all metrics.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\method{}, the first LLM-based DocRE framework that jointly generates relation triples and evidence sentences, achieving competitive extraction and evidence quality on DocRED.\n    \\item Contrastive Evidence Discrimination (\\ced{}), a scoring function that provides consistent improvement over flat-NLI scoring for evidence quality, functioning as a composable module applicable at both training and inference time.\n    \\item A systematic analysis of online vs.\\ offline RL for structured IE, documenting catastrophic forgetting in GRPO and connecting it to the evidence grounding gradient vanishing phenomenon described in LongRLVR.\n    \\item \\edcr{}, a diagnostic metric for entity-sharing distractor citations, with analysis revealing its correlation with relation type characteristics.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Document-Level Relation Extraction.}\nDocRED \\cite{yao2019docred} established the benchmark for document-level RE with evidence annotations. Encoder-based methods achieve strong extraction F1: ATLOP \\cite{zhou2021atlop} (63.4\\%), DocuNet \\cite{zhang2021docunet} (64.6\\%). For evidence, DREEAM \\cite{tan2022dreeam} uses attention supervision to achieve evidence F1 of 57.34\\%, and SAIS \\cite{xiao2022sais} reaches 55.67\\%. However, these methods treat evidence as attention weights rather than explicit outputs. Recent LLM approaches---LMRC \\cite{xu2024lmrc} (60.69\\% F1 with LLaMA3.1-8B) and DocKS-RAG \\cite{docks2025} (63.59\\% with GNN+RAG)---improve extraction but produce no evidence.\n\n\\paragraph{RL for Language Model Alignment.}\nRLHF and its variants \\cite{ouyang2022training,rafailov2023direct} align LLMs with human preferences. For structured tasks, Group Relative Policy Optimization (GRPO) \\cite{shao2024deepseekmath} and Rejection Sampling Fine-Tuning (RSFT) \\cite{yuan2024rrhf} offer complementary paradigms. The theoretical equivalence between RSFT and PPO under certain conditions \\cite{tang2024rsftppo} motivates using offline approaches when online RL is unstable. LongRLVR \\cite{song2026longrlvr} provides theoretical analysis of evidence grounding gradient vanishing in long-context RL.\n\n\\paragraph{Faithfulness Evaluation.}\nNLI-based faithfulness metrics \\cite{honovich2022true,laban2022summac} assess whether generated text is entailed by source documents. However, document-level IE poses unique challenges: entity-sharing distractors receive high entailment scores despite not supporting the specific relation, a failure mode not addressed by existing metrics.\n\n\\section{Method}\n\n\\subsection{Task Formulation}\n\nGiven a document $D = \\{s_1, s_2, \\ldots, s_n\\}$ consisting of $n$ sentences with annotated entity mentions, the task is to generate a set of relation tuples $\\{(h_i, r_i, t_i, E_i)\\}$ where $h_i$ is the head entity, $r_i$ is the relation type, $t_i$ is the tail entity, and $E_i \\subseteq \\{s_1, \\ldots, s_n\\}$ is the set of evidence sentences supporting the relation.\n\nWe formulate this as a sequence-to-sequence task where an LLM generates structured output containing relation triples with explicit sentence indices as evidence markers.\n\n\\subsection{SFT Baseline}\n\nWe fine-tune Qwen3-4B with LoRA \\cite{hu2022lora} on DocRED training data, where each training example maps a document to its gold relation triples with evidence annotations. The output format is:\n\\begin{quote}\n\\texttt{(head; relation; tail; [S$_i$, S$_j$, ...])}\n\\end{quote}\nwhere \\texttt{S$_i$} denotes the $i$-th sentence in the document.\n\n\\subsection{Contrastive Evidence Discrimination (CED)}\n\nFor a candidate output containing a relation triple $(h, r, t)$ with cited evidence sentences $E = \\{e_1, \\ldots, e_k\\}$, we construct the evaluation as follows.\n\n\\paragraph{Claim Construction.} We form a natural language claim $c = $ ``\\texttt{[h] [r\\_verbalized] [t]}'' from the relation triple.\n\n\\paragraph{Positive and Negative Sets.} For each cited sentence $e_i \\in E$:\n\\begin{itemize}\n    \\item \\textbf{Positive score}: $p_{\\text{pos}}(e_i) = \\text{NLI}_{\\text{entail}}(e_i, c)$, the entailment probability from a pre-trained NLI model (DeBERTa-v3-base fine-tuned on MNLI).\n    \\item \\textbf{Negative set}: $N_i = \\{s \\in D \\setminus E \\mid s \\text{ mentions } h \\text{ or } t\\}$---all non-cited sentences that share entities with the triple.\n    \\item \\textbf{Maximum negative score}: $p_{\\text{neg}}^*(e_i) = \\max_{s \\in N_i} \\text{NLI}_{\\text{entail}}(s, c)$.\n\\end{itemize}\n\n\\paragraph{CED Score.} The CED score for a candidate is:\n\\begin{equation}\n    \\text{CED} = \\frac{1}{|E|} \\sum_{e_i \\in E} \\left[ p_{\\text{pos}}(e_i) - p_{\\text{neg}}^*(e_i) \\right]\n\\end{equation}\n\nA high CED score indicates that cited evidence sentences are more strongly entailing than the best entity-sharing distractors. Unlike flat NLI scoring ($\\max_i p_{\\text{pos}}(e_i)$), CED explicitly penalizes candidates whose evidence is no more informative than distractor sentences.\n\n\\subsection{Rejection Sampling Fine-Tuning (RSFT)}\n\nWe apply CED as an offline quality signal for RSFT:\n\n\\begin{enumerate}\n    \\item \\textbf{Candidate Generation}: The SFT model generates $N=8$ candidate outputs per training document (21,952 candidates total).\n    \\item \\textbf{CED Scoring}: Each candidate is scored with CED.\n    \\item \\textbf{Selection}: The top-$k$ candidate per document (default $k{=}1$) is selected, yielding 2,718 high-quality training examples.\n    \\item \\textbf{Fine-Tuning}: The SFT model is further fine-tuned on the selected examples with LoRA ($\\alpha{=}32$, lr$=10^{-5}$, 1 epoch).\n\\end{enumerate}\n\n\\subsection{CED as Inference-Time Reranker}\n\nCED can also be applied at inference time without additional training. Given $N$ candidate outputs from the SFT model, we select the candidate with the highest CED score. This provides a training-free approach to reducing distractor citations at the cost of increased inference time ($\\sim$8$\\times$).\n\n\\subsection{Entity-Sharing Distractor Citation Rate (EDCR)}\n\nWe propose EDCR as a complementary metric to evidence F1:\n\\begin{equation}\n    \\text{EDCR} = \\frac{|\\{s \\in C \\setminus G \\mid s \\text{ mentions } h \\text{ or } t\\}|}{|C|}\n\\end{equation}\nwhere $C$ is the set of all cited sentences and $G$ is the gold evidence set. EDCR measures the proportion of citations that are entity-sharing distractors---sentences that mention relevant entities but do not support the specific relation. Standard evidence F1 treats all false positive citations equally; EDCR specifically quantifies the most deceptive type of error.\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Dataset.} We evaluate on DocRED \\cite{yao2019docred} (3,053 train / 1,000 dev / 1,000 test documents, 96 relation types) and Re-DocRED \\cite{tan2022redocred}, a revised version with corrected annotations.\n\n\\paragraph{Models.} Our primary model is Qwen3-4B with LoRA fine-tuning. We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.\n\n\\paragraph{Baselines.} We compare against: (1)~SFT baseline (Qwen3-4B LoRA, no RL); (2)~RSFT with flat-NLI scoring; (3)~GRPO with CED/flat-NLI/extraction-only rewards; (4)~DREEAM \\cite{tan2022dreeam} (encoder, evidence SOTA); (5)~SAIS \\cite{xiao2022sais} (encoder, evidence baseline).\n\n\\paragraph{Metrics.} Relation F1 (rel\\_F1), Ign\\_F1 (excluding training relational facts), Evidence F1 (evi\\_F1), and EDCR (lower is better).\n\n\\paragraph{CED Configuration.} NLI model: DeBERTa-v3-base fine-tuned on MNLI. Discrimination accuracy on gold vs.\\ distractor pairs: 81.5\\%.\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the test set results. \\method{} (RSFT+CED) achieves test rel\\_F1 of 42.8--43.8\\% and evi\\_F1 of 78.3--78.9\\%, representing a +4.2pp rel\\_F1 and +1.4pp evi\\_F1 improvement over the SFT baseline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{ign\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT baseline & 38.6 & 37.8 & 77.5 & 69.5 \\\\\nRSFT flat-NLI & 42.0 & --- & 77.6 & 66.8 \\\\\nRSFT CED (r2b) & 42.8 & 42.0 & 78.9 & 63.8 \\\\\nRSFT CED (s44) & 43.8 & 42.9 & 78.3 & 62.0 \\\\\n\\midrule\nDREEAM$^\\dagger$ & --- & --- & 57.3 & --- \\\\\nSAIS$^\\dagger$ & --- & --- & 55.7 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test set results on DocRED. $^\\dagger$Encoder-based methods using attention-based evidence extraction (see \\S\\ref{sec:protocol} for evaluation protocol discussion). EDCR computed on dev set (test evidence labels unavailable for EDCR computation). Two RSFT+CED configurations are reported: r2b (1 epoch, $\\alpha{=}32$) and s44 (3 epochs, $\\alpha{=}128$, seed 44).}\n\\label{tab:main}\n\\end{table}\n\nThe evi\\_F1 gap between \\method{} and encoder baselines (78.9\\% vs.\\ 57.3\\% for DREEAM) is substantial but requires careful interpretation due to evaluation protocol differences (\\S\\ref{sec:protocol}). The ign\\_F1 values closely track rel\\_F1 ($<$1pp difference), indicating that RSFT does not overfit to training-set relation co-occurrences.\n\n\\paragraph{Dev$\\to$Test Generalization.}\nTable~\\ref{tab:devtest} shows the generalization gap. The rel\\_F1 drop of 2.1--2.8pp is consistent with the SFT baseline (2.0pp) and within the expected range for DocRED. The s44 configuration (3 epochs) shows slightly larger degradation, suggesting mild dev-set overfitting compared to the 1-epoch r2b configuration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{dev} & \\textbf{test} & $\\Delta$\\textbf{rel\\_F1} & $\\Delta$\\textbf{evi\\_F1} \\\\\n\\midrule\nSFT & 40.6 / 79.8 & 38.6 / 77.5 & $-$2.0 & $-$2.3 \\\\\nr2b & 44.9 / 81.3 & 42.8 / 78.9 & $-$2.1 & $-$2.4 \\\\\ns44 & 46.6 / 80.9 & 43.8 / 78.3 & $-$2.8 & $-$2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dev$\\to$test generalization gap (rel\\_F1 / evi\\_F1).}\n\\label{tab:devtest}\n\\end{table}\n\n\\subsection{CED vs.\\ Flat-NLI Scoring (Claim 2)}\n\\label{sec:ced_vs_nli}\n\nTable~\\ref{tab:ced_nli} compares CED and flat-NLI as RSFT scoring functions in an apple-to-apple ablation: both use the same candidate pool (21,952 generations), same selection threshold ($k{=}1$), and same RSFT hyperparameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Scoring} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT & --- & 40.6 & 79.8 & 71.2 \\\\\nRSFT & flat-NLI & 44.2 & 79.9 & 68.5 \\\\\nRSFT & CED & 44.9 & 81.3 & 66.1 \\\\\n\\midrule\n\\multicolumn{2}{l}{$\\Delta$ (CED $-$ flat-NLI)} & +0.7 & +1.4 & $-$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CED vs.\\ flat-NLI RSFT ablation (dev set). CED provides consistent improvement across all three metrics.}\n\\label{tab:ced_nli}\n\\end{table}\n\nCED scoring improves over flat-NLI on all three dimensions: rel\\_F1 (+0.7pp), evi\\_F1 (+1.4pp), and EDCR ($-$2.4pp). The critical observation is that flat-NLI RSFT achieves virtually no evi\\_F1 improvement over SFT (+0.1pp), while CED RSFT achieves +1.5pp. This reveals that flat-NLI scoring fails to discriminate evidence quality: it filters out candidates with globally low NLI scores but cannot distinguish entity-sharing distractors from genuine evidence, since both receive high entailment scores. CED's contrastive margin directly addresses this blind spot.\n\n\\subsection{CED as Inference-Time Reranker}\n\nTable~\\ref{tab:reranker} evaluates CED as a reranker applied at inference time. CED reranking of SFT outputs (no additional training) achieves the largest EDCR reduction ($-$10.7pp), demonstrating CED's direct value as a quality signal. Combining RSFT+CED training with CED reranking further reduces EDCR to 58.5\\% while maintaining rel\\_F1 and evi\\_F1.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Train?} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT & SFT only & 40.6 & 79.8 & 71.2 \\\\\nCED reranker & No & 41.5 & 80.5 & 60.5 \\\\\nRSFT-CED & Yes & 44.9 & 81.3 & 66.1 \\\\\nRSFT-CED + reranker & Yes & 45.2 & 81.8 & 58.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CED as a composable module (dev set). Reranking uses $N{=}8$ candidates; inference cost is $\\sim$8$\\times$.}\n\\label{tab:reranker}\n\\end{table}\n\nThe composability of CED is noteworthy: RSFT improves generation quality (higher rel\\_F1 and evi\\_F1), while reranking provides additional distractor filtering (lower EDCR). These two applications are complementary because RSFT modifies the model's generation distribution while reranking performs sharp selection among candidates.\n\n\\subsection{Online RL Fails: GRPO Analysis (Claim 3)}\n\\label{sec:grpo}\n\nTable~\\ref{tab:grpo} summarizes GRPO experiments across three reward types and multiple configurations. All configurations exhibit the same pattern: reward increases monotonically while rel\\_F1 collapses catastrophically within 10--50 steps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Reward} & \\textbf{LR} & \\textbf{KL} & \\textbf{Collapse} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Final} \\\\\n& & & \\textbf{Step} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{Reward} \\\\\n\\midrule\nCED & 5e-6 & 0 & $\\sim$10 & 1.4 & 85.0 & 1.20 \\\\\nCED & 5e-5 & 0.01 & $\\sim$50 & 21.1 & 57.5 & 1.20 \\\\\nflat-NLI & 5e-6 & 0 & $\\sim$25 & $<$1 & $<$1 & 0.29 \\\\\nextract & 5e-6 & 0 & $\\sim$20 & 1.5 & --- & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GRPO trajectory summary. ``Collapse Step'' = step at which rel\\_F1 drops below 5\\%. All configs start from the same SFT checkpoint (rel\\_F1 = 40.6\\%).}\n\\label{tab:grpo}\n\\end{table}\n\nThe CED reward without KL constraint (lr=5e-6) is particularly revealing: evi\\_F1 \\emph{increases} to 85.0\\% (surpassing RSFT's 81.3\\%) while rel\\_F1 collapses to 1.4\\%. The model learns to generate high-quality evidence but ``forgets'' how to extract relations---the policy gradient from CED reward reshapes generation toward evidence-rich outputs at the expense of structured extraction.\n\nAdding KL constraints (KL=0.01) delays but does not prevent collapse: rel\\_F1 peaks at 21.1\\% (step 90) before declining, still far below the SFT baseline. The flat-NLI reward collapses fastest (90\\% of groups reach zero-variance outputs by step 25), because its smoother reward surface enables rapid convergence to degenerate optima.\n\nThis systematic failure across reward types and hyperparameters is consistent with the evidence grounding gradient vanishing analysis in LongRLVR \\cite{song2026longrlvr}: in multi-objective structured generation, the evidence grounding signal dominates the policy gradient while the extraction signal vanishes, creating an irreconcilable conflict. RSFT sidesteps this by using CED as a \\emph{selection criterion} rather than a gradient signal, preserving the balanced generation capability of the SFT checkpoint.\n\n\\subsection{EDCR Diagnostic Analysis (Claim 4)}\n\\label{sec:edcr}\n\nTable~\\ref{tab:edcr_diag} presents cross-method EDCR diagnostics. CED-based methods consistently reduce the mean number of distractor citations per relation instance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{EDCR}$\\downarrow$ & \\textbf{evi\\_F1} & \\textbf{\\#Distr.} & \\textbf{\\#Gold} & \\textbf{\\#Total} \\\\\n\\midrule\nSFT & 71.2 & 79.8 & 3.2 & 2.1 & 5.3 \\\\\nRSFT flat-NLI & 68.5 & 79.9 & 2.9 & 2.0 & 4.9 \\\\\nRSFT CED & 66.1 & 81.3 & 2.6 & 2.1 & 4.7 \\\\\nCED reranker & 60.5 & 79.0 & 2.2 & 2.0 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-method EDCR diagnostic (dev set). \\#Distr.\\ = mean entity-sharing distractor count, \\#Gold = mean gold evidence cited, \\#Total = mean total citations per instance.}\n\\label{tab:edcr_diag}\n\\end{table}\n\n\\paragraph{Relation-Type Analysis.}\nEDCR varies dramatically across relation types (Table~\\ref{tab:edcr_rel}). Geographic and nationality relations (P17, P131, P27) exhibit high EDCR ($\\geq$0.74 even after RSFT+CED), because documents about locations contain many sentences mentioning country and city names without supporting the specific relation. Creative-domain relations (P50, P86, P175) have lower EDCR ($\\leq$0.42), as these relations are typically stated in specific sentences with fewer entity-sharing distractors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Relation} & \\textbf{SFT} & \\textbf{RSFT-CED} & $\\Delta$ & \\textbf{\\#Inst.} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{High-EDCR relations}} \\\\\nP17 (country) & 85.0 & 79.0 & $-$6.0 & 1205 \\\\\nP131 (located in) & 83.0 & 78.0 & $-$5.0 & 987 \\\\\nP27 (citizenship) & 80.0 & 74.0 & $-$6.0 & 654 \\\\\nP30 (continent) & 78.0 & 73.0 & $-$5.0 & 321 \\\\\nP150 (contains) & 77.0 & 72.0 & $-$5.0 & 445 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Low-EDCR relations}} \\\\\nP86 (composer) & 48.0 & 42.0 & $-$6.0 & 198 \\\\\nP50 (author) & 45.0 & 39.0 & $-$6.0 & 276 \\\\\nP175 (performer) & 42.0 & 37.0 & $-$5.0 & 312 \\\\\nP40 (child) & 40.0 & 35.0 & $-$5.0 & 187 \\\\\nP26 (spouse) & 38.0 & 33.0 & $-$5.0 & 156 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EDCR (\\%) by relation type (dev set, top-5 and bottom-5). CED reduces EDCR consistently (5--6pp) but high-EDCR relations remain challenging.}\n\\label{tab:edcr_rel}\n\\end{table}\n\nCED provides a uniform 5--6pp EDCR reduction across all relation types, suggesting it captures a general distractor pattern rather than being relation-specific. However, the absolute EDCR values for geographic relations remain high (73--79\\%), indicating that entity-sharing distractor confusion in these domains is structural: documents about locations inherently contain many entity-mentioning sentences, and resolving this likely requires relation-type-aware scoring.\n\n\\paragraph{Limitations.} EDCR of 58.5--66.1\\% across our best configurations means that a majority of non-gold citations are still entity-sharing distractors. While this represents meaningful progress over the SFT baseline (71.2\\%), we acknowledge that the distractor problem is far from solved. Part of this is attributable to annotation incompleteness in DocRED---our Re-DocRED analysis (\\S\\ref{sec:redocred}) shows that EDCR drops significantly under more complete annotations.\n\n\\subsection{Evidence Baseline Comparison}\n\\label{sec:protocol}\n\nTable~\\ref{tab:baseline} contextualizes our evidence results against encoder baselines. An important caveat: DREEAM and SAIS extract evidence via attention weight thresholding (binary classification per sentence), while \\method{} generates explicit sentence indices. These evaluation protocols differ fundamentally---our model ``knows what it is citing'' while attention-based methods derive evidence post-hoc.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{dev evi\\_F1} & \\textbf{test evi\\_F1} & \\textbf{dev rel\\_F1} \\\\\n\\midrule\nDREEAM (paper) & encoder & --- & 57.3 & 63.5 \\\\\nDREEAM (reprod.) & encoder & 56.8 & --- & 62.8 \\\\\nSAIS (reprod.) & encoder & 54.8 & 55.7 & 61.8 \\\\\nFREIGE (ours) & generative & 81.3 & 78.9$^*$ & 44.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Evidence baseline comparison. $^*$Test evi\\_F1 computed locally (not from CodaLab). DREEAM reproduction gap: $-$0.5pp from reported test evi\\_F1.}\n\\label{tab:baseline}\n\\end{table}\n\n\\method{}'s evi\\_F1 substantially exceeds encoder baselines (78.9\\% vs.\\ 57.3\\%), but we emphasize that this comparison should be treated as a reference point rather than a direct superiority claim. The evaluation protocols produce different error distributions: attention-based methods suffer from threshold sensitivity, while generative methods may over-cite (producing more citations that happen to include gold sentences). \\method{}'s rel\\_F1 (44.9\\%) is lower than encoder methods (62.8\\% for DREEAM), reflecting the current gap between generative and encoder approaches for extraction---\\method{}'s contribution is evidence grounding, not extraction supremacy.\n\n\\subsection{Model Size Ablation}\n\nTable~\\ref{tab:size} evaluates the RSFT+CED pipeline across three model sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ & $\\Delta$\\textbf{rel} & $\\Delta$\\textbf{evi} \\\\\n\\midrule\n\\multirow{2}{*}{1.7B} & SFT & 32.8 & 73.5 & 75.0 & --- & --- \\\\\n & RSFT-CED & 36.5 & 75.8 & 70.5 & +3.7 & +2.3 \\\\\n\\midrule\n\\multirow{2}{*}{4B} & SFT & 40.6 & 79.8 & 71.2 & --- & --- \\\\\n & RSFT-CED & 44.9 & 81.3 & 66.1 & +4.4 & +1.5 \\\\\n\\midrule\n\\multirow{2}{*}{8B} & SFT & 44.5 & 81.8 & 69.0 & --- & --- \\\\\n & RSFT-CED & 48.2 & 83.2 & 63.5 & +3.7 & +1.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model size ablation (dev set). RSFT+CED consistently improves over SFT across 1.7B--8B, with relative gains largely independent of model capacity.}\n\\label{tab:size}\n\\end{table}\n\nRSFT+CED provides consistent improvements at all scales: $\\Delta$rel\\_F1 ranges from +3.7 to +4.4pp, and $\\Delta$evi\\_F1 from +1.4 to +2.3pp. The 1.7B model shows the largest evi\\_F1 gain (+2.3pp), likely because smaller models have higher generation diversity, giving CED more room for discrimination. The 8B model achieves the best absolute performance (rel\\_F1 48.2\\%, evi\\_F1 83.2\\%) and the largest EDCR improvement ($-$5.5pp). The marginal gain from 4B to 8B is modest (rel\\_F1 +3.3pp, evi\\_F1 +1.9pp), suggesting diminishing returns at larger scales for this task.\n\n\\subsection{Re-DocRED Extension}\n\\label{sec:redocred}\n\nTable~\\ref{tab:redocred} compares results on DocRED and Re-DocRED, which corrects annotation incompleteness in DocRED by supplementing missing relations and evidence labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & SFT & 40.6 & 79.8 & 71.2 \\\\\n & RSFT-CED & 44.9 & 81.3 & 66.1 \\\\\n\\midrule\n\\multirow{2}{*}{Re-DocRED} & SFT & 43.5 & 81.5 & 58.0 \\\\\n & RSFT-CED & 47.5 & 83.5 & 52.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED vs.\\ Re-DocRED (dev set). Re-DocRED's more complete annotations reduce EDCR by $\\sim$13pp across methods.}\n\\label{tab:redocred}\n\\end{table}\n\nTwo findings emerge: (1)~EDCR drops substantially on Re-DocRED ($-$13.2pp for SFT, $-$13.6pp for RSFT-CED), confirming that a significant portion of apparent entity-sharing distractors in DocRED are actually valid evidence sentences missed by annotators. (2)~RSFT+CED maintains consistent improvements on Re-DocRED ($\\Delta$rel\\_F1 +4.0pp, $\\Delta$evi\\_F1 +2.0pp, $\\Delta$EDCR $-$5.5pp), demonstrating robustness to annotation quality. The residual EDCR of 52.5\\% on Re-DocRED indicates that the distractor problem persists even with better annotations, though at a reduced level.\n\n\\subsection{Ablation Studies}\n\n\\paragraph{Top-$k$ Selection.}\nTable~\\ref{tab:topk} evaluates the quality-quantity trade-off in CED candidate selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccccc}\n\\toprule\n\\textbf{$k$} & \\textbf{\\#Samples} & \\textbf{Mean CED} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\n1 & 2,718 & 0.668 & 44.9 & 81.3 & 66.1 \\\\\n3 & 7,950 & 0.548 & 45.5 & 80.2 & 67.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-$k$ selection ablation (dev set).}\n\\label{tab:topk}\n\\end{table}\n\n$k{=}3$ provides $\\sim$3$\\times$ more training data with lower mean CED score (0.548 vs.\\ 0.668). This yields a slight rel\\_F1 improvement (+0.6pp) from greater data diversity, but \\emph{degrades} evi\\_F1 ($-$1.1pp) and EDCR (+1.7pp). The rank-2 and rank-3 candidates contain more distractor-heavy evidence, diluting the CED signal. We use $k{=}1$ as the default since evidence quality is our primary objective.\n\n\\paragraph{NLI Model Capacity.}\nTable~\\ref{tab:nli} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{Disc.\\ Acc.} & \\textbf{Margin} & \\textbf{RSFT evi\\_F1} & \\textbf{RSFT EDCR}$\\downarrow$ \\\\\n\\midrule\nDeBERTa-v3-base & 81.5 & 0.48 & 81.3 & 66.1 \\\\\nDeBERTa-v3-large & 84.5 & 0.52 & 81.7 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NLI model ablation (dev set). ``Disc.\\ Acc.'' = CED discrimination accuracy on gold vs.\\ distractor pairs.}\n\\label{tab:nli}\n\\end{table}\n\nThe larger NLI model improves discrimination accuracy by +3.0pp and mean CED margin by +0.04, but downstream RSFT gains are marginal (evi\\_F1 +0.4pp, EDCR $-$0.9pp). This suggests that the current bottleneck is annotation completeness rather than NLI model capability: a stronger NLI model cannot compensate for gold evidence labels that are themselves incomplete.\n\n\\section{Analysis}\n\n\\paragraph{Why Flat-NLI Fails at Evidence Discrimination.}\nThe flat-NLI RSFT result (Table~\\ref{tab:ced_nli}) reveals that flat-NLI scoring achieves virtually zero evi\\_F1 improvement over SFT (+0.1pp), despite meaningfully improving rel\\_F1 (+3.6pp). This asymmetry arises because flat-NLI can filter candidates with globally poor NLI scores (improving extraction quality) but cannot distinguish entity-sharing distractors from genuine evidence---both receive high entailment scores because they share key entities. CED's contrastive design directly targets this blind spot: the margin $p_{\\text{pos}} - \\max(p_{\\text{neg}})$ penalizes candidates where distractor sentences also receive high NLI scores.\n\n\\paragraph{Online vs.\\ Offline RL for Structured IE.}\nOur GRPO analysis (\\S\\ref{sec:grpo}) provides empirical evidence for a broader methodological insight: online RL is poorly suited for multi-objective structured generation where different objectives (extraction accuracy, evidence faithfulness) create competing gradient signals. The CED GRPO experiment is the clearest illustration---evi\\_F1 rises to 85.0\\% while rel\\_F1 collapses to 1.4\\%, because the CED reward gradient overwhelms the extraction objective. RSFT avoids this conflict entirely by treating CED as a data selection criterion rather than a training objective, preserving the SFT model's balanced generation capability.\n\n\\paragraph{CED as a Composable Module.}\nCED can be applied at three points in the pipeline: (1)~training data selection for RSFT, (2)~inference-time reranking, and (3)~both combined. Each application provides additive benefits (Table~\\ref{tab:reranker}), with the combined approach achieving the best EDCR (58.5\\%) while maintaining strong rel\\_F1 and evi\\_F1. This composability makes CED practical for deployment: teams can start with the training-free reranker and optionally add RSFT when compute allows.\n\n\\section{Conclusion}\n\nWe presented \\method{}, the first LLM-based framework for document-level relation extraction with evidence grounding. Our Contrastive Evidence Discrimination (\\ced{}) scoring function provides consistent improvements over flat-NLI scoring and functions as a composable module for both training and inference. We documented the systematic failure of online RL (GRPO) for structured IE and showed that offline application of \\ced{} via RSFT effectively sidesteps catastrophic forgetting.\n\nOur results demonstrate that LLMs can generate both relation triples and verifiable evidence for DocRE, with evidence quality competitive across model sizes and datasets. The EDCR metric provides complementary diagnostic value by quantifying entity-sharing distractor citations.\n\n\\paragraph{Limitations.}\n\\method{}'s rel\\_F1 (42.8--43.8\\%) remains below encoder SOTA ($\\sim$63\\%), reflecting the current gap between generative and encoder approaches for extraction. EDCR of 58.5--66.1\\% indicates that distractor citations remain a significant issue. The evi\\_F1 comparison with encoder baselines is not directly apple-to-apple due to different evidence extraction mechanisms. Our experiments are limited to English DocRE on DocRED/Re-DocRED.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{GRPO Full Configuration Grid}\n\\label{app:grpo}\n\nWe evaluated GRPO across 3 reward types $\\times$ 4+ learning rates $\\times$ KL constraint configurations. All configurations exhibited the same failure pattern: monotonically increasing reward with catastrophic rel\\_F1 collapse within 10--50 gradient steps. The KL-constrained CED variant (lr=5e-5, KL=0.01) achieved the highest peak rel\\_F1 (21.1\\% at step 90) but still fell far short of the SFT baseline (40.6\\%).\n\n\\section{RSFT Hyperparameter Configurations}\n\\label{app:rsft}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Epochs} & $\\alpha$ & \\textbf{LR} & \\textbf{dev rel\\_F1} \\\\\n\\midrule\nr1 (s42) & 3 & 128 & 2e-5 & 44.5 \\\\\nr1 (s44) & 3 & 128 & 2e-5 & 46.6 \\\\\nr2a & 1 & 128 & 2e-5 & 44.9 \\\\\nr2b & 1 & 32 & 1e-5 & 44.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RSFT hyperparameter configurations. All use LoRA with rank 16.}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f9b417e-ff96-4aa6-9d25-3ee6564748b7",
  "isSidechain": false,
  "requestId": "req_011Cb4LuJVspQ1hkGJdwRm9K",
  "type": "assistant",
  "uuid": "f12c5ac4-e3e6-4e12-81eb-be9e918f0202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKDCVRbB5yHHg69oPzE2EM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4400,
      "cache_read_input_tokens": 39989,
      "output_tokens": 11616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4400,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11616,
          "cache_read_input_tokens": 39989,
          "cache_creation_input_tokens": 4400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4400
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

_source line 20 · 2026-05-15T12:23:52.299Z_

<details><summary>↩ Tool result · `toolu_01SLAhoF6ceY6GSiayMR1zg5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f12c5ac4-e3e6-4e12-81eb-be9e918f0202",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "abd78194-6608-45c8-9fce-308e44fb4aad",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{tablefootnote}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\n\\title{FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction\\\\via Contrastive Evidence Discrimination}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nLLM-based document-level relation extraction (DocRE) approaches extraction performance competitive with encoder models, yet no existing method generates verifiable evidence sentences alongside extracted relations. We present \\method{}, the first LLM framework for DocRE that jointly produces relation triples and grounded evidence. Our approach introduces Contrastive Evidence Discrimination (\\ced{}), a scoring function that evaluates evidence quality by contrasting gold-supporting sentences against entity-sharing distractors within the same document. We find that \\ced{} is effective as an offline quality signal for Rejection Sampling Fine-Tuning (RSFT) but leads to catastrophic forgetting when used as an online RL (GRPO) reward---a finding we systematically document across three reward types and multiple hyperparameter configurations. On DocRED, \\method{} achieves an evidence F1 of 78.9\\% on the test set, competitive with a relation F1 of 42.8\\%, while reducing entity-sharing distractor citations (EDCR) by 5--8 percentage points over the SFT baseline. We further propose the Entity-sharing Distractor Citation Rate (\\edcr{}) as a complementary evaluation metric that captures a failure mode invisible to standard evidence F1. Experiments across three model sizes (1.7B--8B) and two datasets (DocRED, Re-DocRED) confirm the consistency of our approach.\n\\end{abstract}\n\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) requires identifying relations between entity pairs that may span multiple sentences in a document \\cite{yao2019docred}. While encoder-based methods have achieved strong extraction performance \\cite{zhou2021atlop,tan2022dreeam}, and recent LLM-based approaches show competitive results \\cite{xu2024lmrc}, none produce verifiable evidence---the specific sentences supporting each extracted relation.\n\nEvidence grounding is critical for deploying DocRE in high-stakes domains: human-in-the-loop knowledge base population, biomedical literature curation, and retrieval-augmented generation all require traceability from extracted facts to source text. Without evidence, users cannot verify whether an extraction reflects genuine textual support or a spurious entity co-occurrence.\n\nA natural approach to encouraging faithful evidence is to use Natural Language Inference (NLI) as a reward signal during reinforcement learning. However, we identify a fundamental limitation: flat NLI scoring is systematically deceived by \\emph{entity-sharing distractors}---sentences that mention the head or tail entity but do not support the specific relation. Such sentences receive high NLI entailment scores because they share key entities with the claim, yet they provide no genuine evidential support.\n\nWe propose \\textbf{Contrastive Evidence Discrimination (\\ced{})}, which addresses this limitation by computing a margin between the NLI score for a candidate evidence sentence and the maximum NLI score among entity-sharing distractor sentences from the same document. This contrastive formulation shifts the evaluation from ``does this sentence entail the claim?'' to ``does this sentence entail the claim \\emph{better than the best distractor}?''\n\nA central finding of our work is that \\ced{} is effective as an \\emph{offline} quality signal but fails as an \\emph{online} RL reward. When used as a GRPO reward, \\ced{} drives evidence F1 upward (to 85.0\\%) but causes catastrophic forgetting of relation extraction capability (rel\\_F1 collapses to $<$2\\%). This failure is systematic: we observe it across three reward types (CED, flat-NLI, extraction-only), multiple learning rates, and with KL constraints. In contrast, \\ced{} as an offline signal for RSFT---where it filters training candidates rather than directly shaping gradients---yields consistent improvements across all metrics.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\method{}, the first LLM-based DocRE framework that jointly generates relation triples and evidence sentences, achieving competitive extraction and evidence quality on DocRED.\n    \\item Contrastive Evidence Discrimination (\\ced{}), a scoring function that provides consistent improvement over flat-NLI scoring for evidence quality, functioning as a composable module applicable at both training and inference time.\n    \\item A systematic analysis of online vs.\\ offline RL for structured IE, documenting catastrophic forgetting in GRPO and connecting it to the evidence grounding gradient vanishing phenomenon described in LongRLVR.\n    \\item \\edcr{}, a diagnostic metric for entity-sharing distractor citations, with analysis revealing its correlation with relation type characteristics.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Document-Level Relation Extraction.}\nDocRED \\cite{yao2019docred} established the benchmark for document-level RE with evidence annotations. Encoder-based methods achieve strong extraction F1: ATLOP \\cite{zhou2021atlop} (63.4\\%), DocuNet \\cite{zhang2021docunet} (64.6\\%). For evidence, DREEAM \\cite{tan2022dreeam} uses attention supervision to achieve evidence F1 of 57.34\\%, and SAIS \\cite{xiao2022sais} reaches 55.67\\%. However, these methods treat evidence as attention weights rather than explicit outputs. Recent LLM approaches---LMRC \\cite{xu2024lmrc} (60.69\\% F1 with LLaMA3.1-8B) and DocKS-RAG \\cite{docks2025} (63.59\\% with GNN+RAG)---improve extraction but produce no evidence.\n\n\\paragraph{RL for Language Model Alignment.}\nRLHF and its variants \\cite{ouyang2022training,rafailov2023direct} align LLMs with human preferences. For structured tasks, Group Relative Policy Optimization (GRPO) \\cite{shao2024deepseekmath} and Rejection Sampling Fine-Tuning (RSFT) \\cite{yuan2024rrhf} offer complementary paradigms. The theoretical equivalence between RSFT and PPO under certain conditions \\cite{tang2024rsftppo} motivates using offline approaches when online RL is unstable. LongRLVR \\cite{song2026longrlvr} provides theoretical analysis of evidence grounding gradient vanishing in long-context RL.\n\n\\paragraph{Faithfulness Evaluation.}\nNLI-based faithfulness metrics \\cite{honovich2022true,laban2022summac} assess whether generated text is entailed by source documents. However, document-level IE poses unique challenges: entity-sharing distractors receive high entailment scores despite not supporting the specific relation, a failure mode not addressed by existing metrics.\n\n\\section{Method}\n\n\\subsection{Task Formulation}\n\nGiven a document $D = \\{s_1, s_2, \\ldots, s_n\\}$ consisting of $n$ sentences with annotated entity mentions, the task is to generate a set of relation tuples $\\{(h_i, r_i, t_i, E_i)\\}$ where $h_i$ is the head entity, $r_i$ is the relation type, $t_i$ is the tail entity, and $E_i \\subseteq \\{s_1, \\ldots, s_n\\}$ is the set of evidence sentences supporting the relation.\n\nWe formulate this as a sequence-to-sequence task where an LLM generates structured output containing relation triples with explicit sentence indices as evidence markers.\n\n\\subsection{SFT Baseline}\n\nWe fine-tune Qwen3-4B with LoRA \\cite{hu2022lora} on DocRED training data, where each training example maps a document to its gold relation triples with evidence annotations. The output format is:\n\\begin{quote}\n\\texttt{(head; relation; tail; [S$_i$, S$_j$, ...])}\n\\end{quote}\nwhere \\texttt{S$_i$} denotes the $i$-th sentence in the document.\n\n\\subsection{Contrastive Evidence Discrimination (CED)}\n\nFor a candidate output containing a relation triple $(h, r, t)$ with cited evidence sentences $E = \\{e_1, \\ldots, e_k\\}$, we construct the evaluation as follows.\n\n\\paragraph{Claim Construction.} We form a natural language claim $c = $ ``\\texttt{[h] [r\\_verbalized] [t]}'' from the relation triple.\n\n\\paragraph{Positive and Negative Sets.} For each cited sentence $e_i \\in E$:\n\\begin{itemize}\n    \\item \\textbf{Positive score}: $p_{\\text{pos}}(e_i) = \\text{NLI}_{\\text{entail}}(e_i, c)$, the entailment probability from a pre-trained NLI model (DeBERTa-v3-base fine-tuned on MNLI).\n    \\item \\textbf{Negative set}: $N_i = \\{s \\in D \\setminus E \\mid s \\text{ mentions } h \\text{ or } t\\}$---all non-cited sentences that share entities with the triple.\n    \\item \\textbf{Maximum negative score}: $p_{\\text{neg}}^*(e_i) = \\max_{s \\in N_i} \\text{NLI}_{\\text{entail}}(s, c)$.\n\\end{itemize}\n\n\\paragraph{CED Score.} The CED score for a candidate is:\n\\begin{equation}\n    \\text{CED} = \\frac{1}{|E|} \\sum_{e_i \\in E} \\left[ p_{\\text{pos}}(e_i) - p_{\\text{neg}}^*(e_i) \\right]\n\\end{equation}\n\nA high CED score indicates that cited evidence sentences are more strongly entailing than the best entity-sharing distractors. Unlike flat NLI scoring ($\\max_i p_{\\text{pos}}(e_i)$), CED explicitly penalizes candidates whose evidence is no more informative than distractor sentences.\n\n\\subsection{Rejection Sampling Fine-Tuning (RSFT)}\n\nWe apply CED as an offline quality signal for RSFT:\n\n\\begin{enumerate}\n    \\item \\textbf{Candidate Generation}: The SFT model generates $N=8$ candidate outputs per training document (21,952 candidates total).\n    \\item \\textbf{CED Scoring}: Each candidate is scored with CED.\n    \\item \\textbf{Selection}: The top-$k$ candidate per document (default $k{=}1$) is selected, yielding 2,718 high-quality training examples.\n    \\item \\textbf{Fine-Tuning}: The SFT model is further fine-tuned on the selected examples with LoRA ($\\alpha{=}32$, lr$=10^{-5}$, 1 epoch).\n\\end{enumerate}\n\n\\subsection{CED as Inference-Time Reranker}\n\nCED can also be applied at inference time without additional training. Given $N$ candidate outputs from the SFT model, we select the candidate with the highest CED score. This provides a training-free approach to reducing distractor citations at the cost of increased inference time ($\\sim$8$\\times$).\n\n\\subsection{Entity-Sharing Distractor Citation Rate (EDCR)}\n\nWe propose EDCR as a complementary metric to evidence F1:\n\\begin{equation}\n    \\text{EDCR} = \\frac{|\\{s \\in C \\setminus G \\mid s \\text{ mentions } h \\text{ or } t\\}|}{|C|}\n\\end{equation}\nwhere $C$ is the set of all cited sentences and $G$ is the gold evidence set. EDCR measures the proportion of citations that are entity-sharing distractors---sentences that mention relevant entities but do not support the specific relation. Standard evidence F1 treats all false positive citations equally; EDCR specifically quantifies the most deceptive type of error.\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Dataset.} We evaluate on DocRED \\cite{yao2019docred} (3,053 train / 1,000 dev / 1,000 test documents, 96 relation types) and Re-DocRED \\cite{tan2022redocred}, a revised version with corrected annotations.\n\n\\paragraph{Models.} Our primary model is Qwen3-4B with LoRA fine-tuning. We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.\n\n\\paragraph{Baselines.} We compare against: (1)~SFT baseline (Qwen3-4B LoRA, no RL); (2)~RSFT with flat-NLI scoring; (3)~GRPO with CED/flat-NLI/extraction-only rewards; (4)~DREEAM \\cite{tan2022dreeam} (encoder, evidence SOTA); (5)~SAIS \\cite{xiao2022sais} (encoder, evidence baseline).\n\n\\paragraph{Metrics.} Relation F1 (rel\\_F1), Ign\\_F1 (excluding training relational facts), Evidence F1 (evi\\_F1), and EDCR (lower is better).\n\n\\paragraph{CED Configuration.} NLI model: DeBERTa-v3-base fine-tuned on MNLI. Discrimination accuracy on gold vs.\\ distractor pairs: 81.5\\%.\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the test set results. \\method{} (RSFT+CED) achieves test rel\\_F1 of 42.8--43.8\\% and evi\\_F1 of 78.3--78.9\\%, representing a +4.2pp rel\\_F1 and +1.4pp evi\\_F1 improvement over the SFT baseline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{ign\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT baseline & 38.6 & 37.8 & 77.5 & 69.5 \\\\\nRSFT flat-NLI & 42.0 & --- & 77.6 & 66.8 \\\\\nRSFT CED (r2b) & 42.8 & 42.0 & 78.9 & 63.8 \\\\\nRSFT CED (s44) & 43.8 & 42.9 & 78.3 & 62.0 \\\\\n\\midrule\nDREEAM$^\\dagger$ & --- & --- & 57.3 & --- \\\\\nSAIS$^\\dagger$ & --- & --- & 55.7 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Test set results on DocRED. $^\\dagger$Encoder-based methods using attention-based evidence extraction (see \\S\\ref{sec:protocol} for evaluation protocol discussion). EDCR computed on dev set (test evidence labels unavailable for EDCR computation). Two RSFT+CED configurations are reported: r2b (1 epoch, $\\alpha{=}32$) and s44 (3 epochs, $\\alpha{=}128$, seed 44).}\n\\label{tab:main}\n\\end{table}\n\nThe evi\\_F1 gap between \\method{} and encoder baselines (78.9\\% vs.\\ 57.3\\% for DREEAM) is substantial but requires careful interpretation due to evaluation protocol differences (\\S\\ref{sec:protocol}). The ign\\_F1 values closely track rel\\_F1 ($<$1pp difference), indicating that RSFT does not overfit to training-set relation co-occurrences.\n\n\\paragraph{Dev$\\to$Test Generalization.}\nTable~\\ref{tab:devtest} shows the generalization gap. The rel\\_F1 drop of 2.1--2.8pp is consistent with the SFT baseline (2.0pp) and within the expected range for DocRED. The s44 configuration (3 epochs) shows slightly larger degradation, suggesting mild dev-set overfitting compared to the 1-epoch r2b configuration.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{dev} & \\textbf{test} & $\\Delta$\\textbf{rel\\_F1} & $\\Delta$\\textbf{evi\\_F1} \\\\\n\\midrule\nSFT & 40.6 / 79.8 & 38.6 / 77.5 & $-$2.0 & $-$2.3 \\\\\nr2b & 44.9 / 81.3 & 42.8 / 78.9 & $-$2.1 & $-$2.4 \\\\\ns44 & 46.6 / 80.9 & 43.8 / 78.3 & $-$2.8 & $-$2.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dev$\\to$test generalization gap (rel\\_F1 / evi\\_F1).}\n\\label{tab:devtest}\n\\end{table}\n\n\\subsection{CED vs.\\ Flat-NLI Scoring (Claim 2)}\n\\label{sec:ced_vs_nli}\n\nTable~\\ref{tab:ced_nli} compares CED and flat-NLI as RSFT scoring functions in an apple-to-apple ablation: both use the same candidate pool (21,952 generations), same selection threshold ($k{=}1$), and same RSFT hyperparameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Scoring} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT & --- & 40.6 & 79.8 & 71.2 \\\\\nRSFT & flat-NLI & 44.2 & 79.9 & 68.5 \\\\\nRSFT & CED & 44.9 & 81.3 & 66.1 \\\\\n\\midrule\n\\multicolumn{2}{l}{$\\Delta$ (CED $-$ flat-NLI)} & +0.7 & +1.4 & $-$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CED vs.\\ flat-NLI RSFT ablation (dev set). CED provides consistent improvement across all three metrics.}\n\\label{tab:ced_nli}\n\\end{table}\n\nCED scoring improves over flat-NLI on all three dimensions: rel\\_F1 (+0.7pp), evi\\_F1 (+1.4pp), and EDCR ($-$2.4pp). The critical observation is that flat-NLI RSFT achieves virtually no evi\\_F1 improvement over SFT (+0.1pp), while CED RSFT achieves +1.5pp. This reveals that flat-NLI scoring fails to discriminate evidence quality: it filters out candidates with globally low NLI scores but cannot distinguish entity-sharing distractors from genuine evidence, since both receive high entailment scores. CED's contrastive margin directly addresses this blind spot.\n\n\\subsection{CED as Inference-Time Reranker}\n\nTable~\\ref{tab:reranker} evaluates CED as a reranker applied at inference time. CED reranking of SFT outputs (no additional training) achieves the largest EDCR reduction ($-$10.7pp), demonstrating CED's direct value as a quality signal. Combining RSFT+CED training with CED reranking further reduces EDCR to 58.5\\% while maintaining rel\\_F1 and evi\\_F1.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Train?} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\nSFT & SFT only & 40.6 & 79.8 & 71.2 \\\\\nCED reranker & No & 41.5 & 80.5 & 60.5 \\\\\nRSFT-CED & Yes & 44.9 & 81.3 & 66.1 \\\\\nRSFT-CED + reranker & Yes & 45.2 & 81.8 & 58.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CED as a composable module (dev set). Reranking uses $N{=}8$ candidates; inference cost is $\\sim$8$\\times$.}\n\\label{tab:reranker}\n\\end{table}\n\nThe composability of CED is noteworthy: RSFT improves generation quality (higher rel\\_F1 and evi\\_F1), while reranking provides additional distractor filtering (lower EDCR). These two applications are complementary because RSFT modifies the model's generation distribution while reranking performs sharp selection among candidates.\n\n\\subsection{Online RL Fails: GRPO Analysis (Claim 3)}\n\\label{sec:grpo}\n\nTable~\\ref{tab:grpo} summarizes GRPO experiments across three reward types and multiple configurations. All configurations exhibit the same pattern: reward increases monotonically while rel\\_F1 collapses catastrophically within 10--50 steps.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Reward} & \\textbf{LR} & \\textbf{KL} & \\textbf{Collapse} & \\textbf{Peak} & \\textbf{Final} & \\textbf{Final} \\\\\n& & & \\textbf{Step} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{Reward} \\\\\n\\midrule\nCED & 5e-6 & 0 & $\\sim$10 & 1.4 & 85.0 & 1.20 \\\\\nCED & 5e-5 & 0.01 & $\\sim$50 & 21.1 & 57.5 & 1.20 \\\\\nflat-NLI & 5e-6 & 0 & $\\sim$25 & $<$1 & $<$1 & 0.29 \\\\\nextract & 5e-6 & 0 & $\\sim$20 & 1.5 & --- & 0.30 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{GRPO trajectory summary. ``Collapse Step'' = step at which rel\\_F1 drops below 5\\%. All configs start from the same SFT checkpoint (rel\\_F1 = 40.6\\%).}\n\\label{tab:grpo}\n\\end{table}\n\nThe CED reward without KL constraint (lr=5e-6) is particularly revealing: evi\\_F1 \\emph{increases} to 85.0\\% (surpassing RSFT's 81.3\\%) while rel\\_F1 collapses to 1.4\\%. The model learns to generate high-quality evidence but ``forgets'' how to extract relations---the policy gradient from CED reward reshapes generation toward evidence-rich outputs at the expense of structured extraction.\n\nAdding KL constraints (KL=0.01) delays but does not prevent collapse: rel\\_F1 peaks at 21.1\\% (step 90) before declining, still far below the SFT baseline. The flat-NLI reward collapses fastest (90\\% of groups reach zero-variance outputs by step 25), because its smoother reward surface enables rapid convergence to degenerate optima.\n\nThis systematic failure across reward types and hyperparameters is consistent with the evidence grounding gradient vanishing analysis in LongRLVR \\cite{song2026longrlvr}: in multi-objective structured generation, the evidence grounding signal dominates the policy gradient while the extraction signal vanishes, creating an irreconcilable conflict. RSFT sidesteps this by using CED as a \\emph{selection criterion} rather than a gradient signal, preserving the balanced generation capability of the SFT checkpoint.\n\n\\subsection{EDCR Diagnostic Analysis (Claim 4)}\n\\label{sec:edcr}\n\nTable~\\ref{tab:edcr_diag} presents cross-method EDCR diagnostics. CED-based methods consistently reduce the mean number of distractor citations per relation instance.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{EDCR}$\\downarrow$ & \\textbf{evi\\_F1} & \\textbf{\\#Distr.} & \\textbf{\\#Gold} & \\textbf{\\#Total} \\\\\n\\midrule\nSFT & 71.2 & 79.8 & 3.2 & 2.1 & 5.3 \\\\\nRSFT flat-NLI & 68.5 & 79.9 & 2.9 & 2.0 & 4.9 \\\\\nRSFT CED & 66.1 & 81.3 & 2.6 & 2.1 & 4.7 \\\\\nCED reranker & 60.5 & 79.0 & 2.2 & 2.0 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-method EDCR diagnostic (dev set). \\#Distr.\\ = mean entity-sharing distractor count, \\#Gold = mean gold evidence cited, \\#Total = mean total citations per instance.}\n\\label{tab:edcr_diag}\n\\end{table}\n\n\\paragraph{Relation-Type Analysis.}\nEDCR varies dramatically across relation types (Table~\\ref{tab:edcr_rel}). Geographic and nationality relations (P17, P131, P27) exhibit high EDCR ($\\geq$0.74 even after RSFT+CED), because documents about locations contain many sentences mentioning country and city names without supporting the specific relation. Creative-domain relations (P50, P86, P175) have lower EDCR ($\\leq$0.42), as these relations are typically stated in specific sentences with fewer entity-sharing distractors.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccr}\n\\toprule\n\\textbf{Relation} & \\textbf{SFT} & \\textbf{RSFT-CED} & $\\Delta$ & \\textbf{\\#Inst.} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{High-EDCR relations}} \\\\\nP17 (country) & 85.0 & 79.0 & $-$6.0 & 1205 \\\\\nP131 (located in) & 83.0 & 78.0 & $-$5.0 & 987 \\\\\nP27 (citizenship) & 80.0 & 74.0 & $-$6.0 & 654 \\\\\nP30 (continent) & 78.0 & 73.0 & $-$5.0 & 321 \\\\\nP150 (contains) & 77.0 & 72.0 & $-$5.0 & 445 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Low-EDCR relations}} \\\\\nP86 (composer) & 48.0 & 42.0 & $-$6.0 & 198 \\\\\nP50 (author) & 45.0 & 39.0 & $-$6.0 & 276 \\\\\nP175 (performer) & 42.0 & 37.0 & $-$5.0 & 312 \\\\\nP40 (child) & 40.0 & 35.0 & $-$5.0 & 187 \\\\\nP26 (spouse) & 38.0 & 33.0 & $-$5.0 & 156 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{EDCR (\\%) by relation type (dev set, top-5 and bottom-5). CED reduces EDCR consistently (5--6pp) but high-EDCR relations remain challenging.}\n\\label{tab:edcr_rel}\n\\end{table}\n\nCED provides a uniform 5--6pp EDCR reduction across all relation types, suggesting it captures a general distractor pattern rather than being relation-specific. However, the absolute EDCR values for geographic relations remain high (73--79\\%), indicating that entity-sharing distractor confusion in these domains is structural: documents about locations inherently contain many entity-mentioning sentences, and resolving this likely requires relation-type-aware scoring.\n\n\\paragraph{Limitations.} EDCR of 58.5--66.1\\% across our best configurations means that a majority of non-gold citations are still entity-sharing distractors. While this represents meaningful progress over the SFT baseline (71.2\\%), we acknowledge that the distractor problem is far from solved. Part of this is attributable to annotation incompleteness in DocRED---our Re-DocRED analysis (\\S\\ref{sec:redocred}) shows that EDCR drops significantly under more complete annotations.\n\n\\subsection{Evidence Baseline Comparison}\n\\label{sec:protocol}\n\nTable~\\ref{tab:baseline} contextualizes our evidence results against encoder baselines. An important caveat: DREEAM and SAIS extract evidence via attention weight thresholding (binary classification per sentence), while \\method{} generates explicit sentence indices. These evaluation protocols differ fundamentally---our model ``knows what it is citing'' while attention-based methods derive evidence post-hoc.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{dev evi\\_F1} & \\textbf{test evi\\_F1} & \\textbf{dev rel\\_F1} \\\\\n\\midrule\nDREEAM (paper) & encoder & --- & 57.3 & 63.5 \\\\\nDREEAM (reprod.) & encoder & 56.8 & --- & 62.8 \\\\\nSAIS (reprod.) & encoder & 54.8 & 55.7 & 61.8 \\\\\nFREIGE (ours) & generative & 81.3 & 78.9$^*$ & 44.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Evidence baseline comparison. $^*$Test evi\\_F1 computed locally (not from CodaLab). DREEAM reproduction gap: $-$0.5pp from reported test evi\\_F1.}\n\\label{tab:baseline}\n\\end{table}\n\n\\method{}'s evi\\_F1 substantially exceeds encoder baselines (78.9\\% vs.\\ 57.3\\%), but we emphasize that this comparison should be treated as a reference point rather than a direct superiority claim. The evaluation protocols produce different error distributions: attention-based methods suffer from threshold sensitivity, while generative methods may over-cite (producing more citations that happen to include gold sentences). \\method{}'s rel\\_F1 (44.9\\%) is lower than encoder methods (62.8\\% for DREEAM), reflecting the current gap between generative and encoder approaches for extraction---\\method{}'s contribution is evidence grounding, not extraction supremacy.\n\n\\subsection{Model Size Ablation}\n\nTable~\\ref{tab:size} evaluates the RSFT+CED pipeline across three model sizes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ & $\\Delta$\\textbf{rel} & $\\Delta$\\textbf{evi} \\\\\n\\midrule\n\\multirow{2}{*}{1.7B} & SFT & 32.8 & 73.5 & 75.0 & --- & --- \\\\\n & RSFT-CED & 36.5 & 75.8 & 70.5 & +3.7 & +2.3 \\\\\n\\midrule\n\\multirow{2}{*}{4B} & SFT & 40.6 & 79.8 & 71.2 & --- & --- \\\\\n & RSFT-CED & 44.9 & 81.3 & 66.1 & +4.4 & +1.5 \\\\\n\\midrule\n\\multirow{2}{*}{8B} & SFT & 44.5 & 81.8 & 69.0 & --- & --- \\\\\n & RSFT-CED & 48.2 & 83.2 & 63.5 & +3.7 & +1.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Model size ablation (dev set). RSFT+CED consistently improves over SFT across 1.7B--8B, with relative gains largely independent of model capacity.}\n\\label{tab:size}\n\\end{table}\n\nRSFT+CED provides consistent improvements at all scales: $\\Delta$rel\\_F1 ranges from +3.7 to +4.4pp, and $\\Delta$evi\\_F1 from +1.4 to +2.3pp. The 1.7B model shows the largest evi\\_F1 gain (+2.3pp), likely because smaller models have higher generation diversity, giving CED more room for discrimination. The 8B model achieves the best absolute performance (rel\\_F1 48.2\\%, evi\\_F1 83.2\\%) and the largest EDCR improvement ($-$5.5pp). The marginal gain from 4B to 8B is modest (rel\\_F1 +3.3pp, evi\\_F1 +1.9pp), suggesting diminishing returns at larger scales for this task.\n\n\\subsection{Re-DocRED Extension}\n\\label{sec:redocred}\n\nTable~\\ref{tab:redocred} compares results on DocRED and Re-DocRED, which corrects annotation incompleteness in DocRED by supplementing missing relations and evidence labels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\n\\multirow{2}{*}{DocRED} & SFT & 40.6 & 79.8 & 71.2 \\\\\n & RSFT-CED & 44.9 & 81.3 & 66.1 \\\\\n\\midrule\n\\multirow{2}{*}{Re-DocRED} & SFT & 43.5 & 81.5 & 58.0 \\\\\n & RSFT-CED & 47.5 & 83.5 & 52.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED vs.\\ Re-DocRED (dev set). Re-DocRED's more complete annotations reduce EDCR by $\\sim$13pp across methods.}\n\\label{tab:redocred}\n\\end{table}\n\nTwo findings emerge: (1)~EDCR drops substantially on Re-DocRED ($-$13.2pp for SFT, $-$13.6pp for RSFT-CED), confirming that a significant portion of apparent entity-sharing distractors in DocRED are actually valid evidence sentences missed by annotators. (2)~RSFT+CED maintains consistent improvements on Re-DocRED ($\\Delta$rel\\_F1 +4.0pp, $\\Delta$evi\\_F1 +2.0pp, $\\Delta$EDCR $-$5.5pp), demonstrating robustness to annotation quality. The residual EDCR of 52.5\\% on Re-DocRED indicates that the distractor problem persists even with better annotations, though at a reduced level.\n\n\\subsection{Ablation Studies}\n\n\\paragraph{Top-$k$ Selection.}\nTable~\\ref{tab:topk} evaluates the quality-quantity trade-off in CED candidate selection.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{ccccccc}\n\\toprule\n\\textbf{$k$} & \\textbf{\\#Samples} & \\textbf{Mean CED} & \\textbf{rel\\_F1} & \\textbf{evi\\_F1} & \\textbf{EDCR}$\\downarrow$ \\\\\n\\midrule\n1 & 2,718 & 0.668 & 44.9 & 81.3 & 66.1 \\\\\n3 & 7,950 & 0.548 & 45.5 & 80.2 & 67.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-$k$ selection ablation (dev set).}\n\\label{tab:topk}\n\\end{table}\n\n$k{=}3$ provides $\\sim$3$\\times$ more training data with lower mean CED score (0.548 vs.\\ 0.668). This yields a slight rel\\_F1 improvement (+0.6pp) from greater data diversity, but \\emph{degrades} evi\\_F1 ($-$1.1pp) and EDCR (+1.7pp). The rank-2 and rank-3 candidates contain more distractor-heavy evidence, diluting the CED signal. We use $k{=}1$ as the default since evidence quality is our primary objective.\n\n\\paragraph{NLI Model Capacity.}\nTable~\\ref{tab:nli} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{Disc.\\ Acc.} & \\textbf{Margin} & \\textbf{RSFT evi\\_F1} & \\textbf{RSFT EDCR}$\\downarrow$ \\\\\n\\midrule\nDeBERTa-v3-base & 81.5 & 0.48 & 81.3 & 66.1 \\\\\nDeBERTa-v3-large & 84.5 & 0.52 & 81.7 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{NLI model ablation (dev set). ``Disc.\\ Acc.'' = CED discrimination accuracy on gold vs.\\ distractor pairs.}\n\\label{tab:nli}\n\\end{table}\n\nThe larger NLI model improves discrimination accuracy by +3.0pp and mean CED margin by +0.04, but downstream RSFT gains are marginal (evi\\_F1 +0.4pp, EDCR $-$0.9pp). This suggests that the current bottleneck is annotation completeness rather than NLI model capability: a stronger NLI model cannot compensate for gold evidence labels that are themselves incomplete.\n\n\\section{Analysis}\n\n\\paragraph{Why Flat-NLI Fails at Evidence Discrimination.}\nThe flat-NLI RSFT result (Table~\\ref{tab:ced_nli}) reveals that flat-NLI scoring achieves virtually zero evi\\_F1 improvement over SFT (+0.1pp), despite meaningfully improving rel\\_F1 (+3.6pp). This asymmetry arises because flat-NLI can filter candidates with globally poor NLI scores (improving extraction quality) but cannot distinguish entity-sharing distractors from genuine evidence---both receive high entailment scores because they share key entities. CED's contrastive design directly targets this blind spot: the margin $p_{\\text{pos}} - \\max(p_{\\text{neg}})$ penalizes candidates where distractor sentences also receive high NLI scores.\n\n\\paragraph{Online vs.\\ Offline RL for Structured IE.}\nOur GRPO analysis (\\S\\ref{sec:grpo}) provides empirical evidence for a broader methodological insight: online RL is poorly suited for multi-objective structured generation where different objectives (extraction accuracy, evidence faithfulness) create competing gradient signals. The CED GRPO experiment is the clearest illustration---evi\\_F1 rises to 85.0\\% while rel\\_F1 collapses to 1.4\\%, because the CED reward gradient overwhelms the extraction objective. RSFT avoids this conflict entirely by treating CED as a data selection criterion rather than a training objective, preserving the SFT model's balanced generation capability.\n\n\\paragraph{CED as a Composable Module.}\nCED can be applied at three points in the pipeline: (1)~training data selection for RSFT, (2)~inference-time reranking, and (3)~both combined. Each application provides additive benefits (Table~\\ref{tab:reranker}), with the combined approach achieving the best EDCR (58.5\\%) while maintaining strong rel\\_F1 and evi\\_F1. This composability makes CED practical for deployment: teams can start with the training-free reranker and optionally add RSFT when compute allows.\n\n\\section{Conclusion}\n\nWe presented \\method{}, the first LLM-based framework for document-level relation extraction with evidence grounding. Our Contrastive Evidence Discrimination (\\ced{}) scoring function provides consistent improvements over flat-NLI scoring and functions as a composable module for both training and inference. We documented the systematic failure of online RL (GRPO) for structured IE and showed that offline application of \\ced{} via RSFT effectively sidesteps catastrophic forgetting.\n\nOur results demonstrate that LLMs can generate both relation triples and verifiable evidence for DocRE, with evidence quality competitive across model sizes and datasets. The EDCR metric provides complementary diagnostic value by quantifying entity-sharing distractor citations.\n\n\\paragraph{Limitations.}\n\\method{}'s rel\\_F1 (42.8--43.8\\%) remains below encoder SOTA ($\\sim$63\\%), reflecting the current gap between generative and encoder approaches for extraction. EDCR of 58.5--66.1\\% indicates that distractor citations remain a significant issue. The evi\\_F1 comparison with encoder baselines is not directly apple-to-apple due to different evidence extraction mechanisms. Our experiments are limited to English DocRE on DocRED/Re-DocRED.\n\n\\bibliography{custom}\n\n\\appendix\n\n\\section{GRPO Full Configuration Grid}\n\\label{app:grpo}\n\nWe evaluated GRPO across 3 reward types $\\times$ 4+ learning rates $\\times$ KL constraint configurations. All configurations exhibited the same failure pattern: monotonically increasing reward with catastrophic rel\\_F1 collapse within 10--50 gradient steps. The KL-constrained CED variant (lr=5e-5, KL=0.01) achieved the highest peak rel\\_F1 (21.1\\% at step 90) but still fell far short of the SFT baseline (40.6\\%).\n\n\\section{RSFT Hyperparameter Configurations}\n\\label{app:rsft}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Epochs} & $\\alpha$ & \\textbf{LR} & \\textbf{dev rel\\_F1} \\\\\n\\midrule\nr1 (s42) & 3 & 128 & 2e-5 & 44.5 \\\\\nr1 (s44) & 3 & 128 & 2e-5 & 46.6 \\\\\nr2a & 1 & 128 & 2e-5 & 44.9 \\\\\nr2b & 1 & 32 & 1e-5 & 44.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RSFT hyperparameter configurations. All use LoRA with rank 16.}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f12c5ac4-e3e6-4e12-81eb-be9e918f0202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-i…",
  "leafUuid": "abd78194-6608-45c8-9fce-308e44fb4aad",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated paper for dream ID",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Tool call

_source line 23 · 2026-05-15T12:23:57.217Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wri8rAdV7kc2x81wMRR1K3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abd78194-6608-45c8-9fce-308e44fb4aad",
  "isSidechain": false,
  "requestId": "req_011Cb4MAu2gqYc2oMwMyTGSX",
  "type": "assistant",
  "uuid": "80cb8389-bc10-4762-905d-4865fa2d9111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Re9GydjMKqJ6YuZRD3Rvgv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11681,
      "cache_read_input_tokens": 44389,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 44389,
          "cache_creation_input_tokens": 11681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11681
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

_source line 24 · 2026-05-15T12:23:57.396Z_

<details><summary>↩ Tool result · `toolu_01Wri8rAdV7kc2x81wMRR1K3`</summary>

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

! LaTeX Error: File `emnlp2023.sty' not found.

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
  "parentUuid": "80cb8389-bc10-4762-905d-4865fa2d9111",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "59c01496-a9de-4c7f-aa7d-69ff6951626b",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "80cb8389-bc10-4762-905d-4865fa2d9111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T12:24:01.209Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023.sty file is not available. Let me switch to a standard article class with appropriate formatting to mimic a conference paper style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59c01496-a9de-4c7f-aa7d-69ff6951626b",
  "isSidechain": false,
  "requestId": "req_011Cb4MBH3G3jw4aNN8oM6mc",
  "type": "assistant",
  "uuid": "dd85b95d-f0f5-4d32-8c1e-a3d4fd3f9188",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPvyUPjfRBRnaXqLQGLPot",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 56070,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 56070,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 26 · 2026-05-15T12:24:01.687Z_

`emnlp2023.sty` not available. Switching to standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd85b95d-f0f5-4d32-8c1e-a3d4fd3f9188",
  "isSidechain": false,
  "requestId": "req_011Cb4MBH3G3jw4aNN8oM6mc",
  "type": "assistant",
  "uuid": "80901b80-49ec-4e30-9e79-67a6b225eb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPvyUPjfRBRnaXqLQGLPot",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 56070,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 56070,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 27 · 2026-05-15T12:24:04.844Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01TvzqDApa61Ciu5WpS8oNPs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
  "old_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{tablefootnote}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{hyperref}\n\\usepackage{enumitem}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80901b80-49ec-4e30-9e79-67a6b225eb73",
  "isSidechain": false,
  "requestId": "req_011Cb4MBH3G3jw4aNN8oM6mc",
  "type": "assistant",
  "uuid": "c9a82b9b-3388-40ba-96c6-4fa9b17d6b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPvyUPjfRBRnaXqLQGLPot",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 56070,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 56070,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 28 · 2026-05-15T12:24:04.871Z_

<details><summary>↩ Tool result · `toolu_01TvzqDApa61Ciu5WpS8oNPs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a82b9b-3388-40ba-96c6-4fa9b17d6b23",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "47225b55-a2a1-432b-b583-fa55f0363985",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex",
    "oldString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{tablefootnote}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{soul}\n\\usepackage{hyperref}\n\\usepackage{enumitem}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " \\documentclass[11pt,a4paper]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          " \\usepackage{soul}",
          "-\\usepackage{tablefootnote}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{enumitem}",
          " ",
          " \\newcommand{\\method}{FREIGE}",
          " \\newcommand{\\ced}{CED}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c9a82b9b-3388-40ba-96c6-4fa9b17d6b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-15T12:24:04.941Z_

```json
{
  "parentUuid": "47225b55-a2a1-432b-b583-fa55f0363985",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9d45449b-fd8f-4038-b88d-8d9568bde1db",
  "timestamp": "2026-05-15T12:24:04.941Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-15T12:24:08.563Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LaoTvuJt7EgP8pNUTyNThD`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d45449b-fd8f-4038-b88d-8d9568bde1db",
  "isSidechain": false,
  "requestId": "req_011Cb4MBppi4bgY4qtrBZ3vF",
  "type": "assistant",
  "uuid": "2174de21-e505-476f-a449-09bcde596f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiWbF7ZMvczMA4G5HbHGjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 56515,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 56515,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
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

_source line 31 · 2026-05-15T12:24:09.148Z_

<details><summary>↩ Tool result · `toolu_01LaoTvuJt7EgP8pNUTyNThD`</summary>

```text
No file paper.bbl.
[9] [10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (10 pages, 177865 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2174de21-e505-476f-a449-09bcde596f39",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "0604b8b3-3637-44db-8b0d-79f854e5efc1",
  "toolUseResult": {
    "stdout": "No file paper.bbl.\n[9] [10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 177865 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2174de21-e505-476f-a449-09bcde596f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:24:12.528Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01577z3tn6YCpteEa3Liu3bm`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0604b8b3-3637-44db-8b0d-79f854e5efc1",
  "isSidechain": false,
  "requestId": "req_011Cb4MC8pBqqvZffAV6rNM7",
  "type": "assistant",
  "uuid": "463d9c5e-e0ed-4410-88f3-58b73d566622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y72aFc3Be5ahF8G2oRdyRK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 57166,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 57166,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 33 · 2026-05-15T12:24:13.060Z_

<details><summary>↩ Tool result · `toolu_01577z3tn6YCpteEa3Liu3bm`</summary>

```text
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (10 pages, 180494 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "463d9c5e-e0ed-4410-88f3-58b73d566622",
  "isSidechain": false,
  "promptId": "bc737e0a-730e-45af-8b9e-dcac775874fc",
  "type": "user",
  "uuid": "d09a8f78-0db9-4985-8b04-225c782e0e84",
  "toolUseResult": {
    "stdout": "fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 180494 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "463d9c5e-e0ed-4410-88f3-58b73d566622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T12:24:25.985Z_

编译成功，10 页 PDF。

`paper.tex` 已写入并编译为 `paper.pdf`（10 页）。论文覆盖了 `experiment_data.json` 中全部 8 个实验：

- **Table 1**: 主 test set 结果（RSFT-CED r2b/s44 + baselines）
- **Table 2**: Dev→Test 泛化 gap
- **Table 3**: CED vs flat-NLI RSFT ablation（Claim 2）
- **Table 4**: CED-as-reranker + composability（含 RSFT+reranker 组合）
- **Table 5**: GRPO 轨迹摘要（Claim 3，3 种 reward × 多 config 全线失败）
- **Table 6**: Cross-method EDCR diagnostic（Claim 4）
- **Table 7**: EDCR 按关系类型分层分析
- **Table 8**: Evidence baseline 复现对比（DREEAM/SAIS）
- **Table 9**: 模型规模 ablation（1.7B/4B/8B）
- **Table 10**: Re-DocRED 扩展
- **Table 11**: top\_k 选择 ablation
- **Table 12**: NLI 模型容量 ablation

叙事按 guidance 调整：Claim 1 用 "competitive with"；Claim 2 强调 flat-NLI 在 evidence 维度几乎无效、CED 作为可组合模块；Claim 3 升级为并列 contribution；Claim 4 坦诚讨论 EDCR 局限性。所有数字均来自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d09a8f78-0db9-4985-8b04-225c782e0e84",
  "isSidechain": false,
  "requestId": "req_011Cb4MCRYGUcaWkKVwdMnRp",
  "type": "assistant",
  "uuid": "35bad97b-e2cb-4351-87dc-a47600ce4df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SrzR7oj2nwmH556H9UCrRW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 449,
      "cache_read_input_tokens": 57898,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 57898,
          "cache_creation_input_tokens": 449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 449
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-i…",
  "leafUuid": "35bad97b-e2cb-4351-87dc-a47600ce4df3",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate median-tier simulated paper for dream ID",
  "sessionId": "04664d5d-6490-4063-ad83-836ebb88cfce"
}
```

---
