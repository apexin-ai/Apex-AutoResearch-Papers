# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/a0c1155d-3d78-4078-907e-86825dce7a7c.jsonl`
- **Structured JSON:** [`69955214e31c1ee3ce6d.json`](../../sessions/69/69955214e31c1ee3ce6d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T13:52:52.404Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T13:52:52.404Z",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main\n- Narrative guidance：原始 framing 完全成立。四个 Claims 全部有强证据支撑： C1（首个同时生成抽取+证据的 LLM DocRE）有 test set 显著优势； C2（CED > flat-NLI）有统计显著性； C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证 + DPO 中间点对比； C4（EDCR 指标）有人工标注背书。 论文可用完整的 \"problem → naive reward fails → online RL fails → CED+RSFT solves it\" story arc， 无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO → DPO → RSFT）。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T13:52:52.408Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T13:52:52.408Z",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-15T13:52:52.432Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main
- Narrative guidance：原始 framing 完全成立。四个 Claims 全部有强证据支撑： C1（首个同时生成抽取+证据的 LLM DocRE）有 test set 显著优势； C2（CED > flat-NLI）有统计显著性； C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证 + DPO 中间点对比； C4（EDCR 指标）有人工标注背书。 论文可用完整的 "problem → naive reward fails → online RL fails → CED+RSFT solves it" story arc， 无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO → DPO → RSFT）。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "74d694c7-6273-47b0-ad20-d5522cae77f6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T13:52:52.431Z_

```json
{
  "parentUuid": "74d694c7-6273-47b0-ad20-d5522cae77f6",
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
  "uuid": "f70d7580-d75e-48dd-99d1-34c42f64acd9",
  "timestamp": "2026-05-15T13:52:52.431Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T13:52:52.431Z_

```json
{
  "parentUuid": "f70d7580-d75e-48dd-99d1-34c42f64acd9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ce8a1e8-5685-4a6b-b133-aac8ec881f9c",
  "timestamp": "2026-05-15T13:52:52.431Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
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
  "aiTitle": "Generate complete ML research paper for dream session",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Assistant

_source line 7 · 2026-05-15T13:52:55.111Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce8a1e8-5685-4a6b-b133-aac8ec881f9c",
  "isSidechain": false,
  "requestId": "req_011Cb4TxYKUV6p1KTkPTu4WA",
  "type": "assistant",
  "uuid": "073bb31a-d4e4-47e0-a335-69d90e7e3a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAEgeiAWmzFZcxrAUXCxtn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11250,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11250
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

_source line 8 · 2026-05-15T13:52:56.061Z_

<details open><summary>🔧 Tool call — Read · `toolu_0149LgqUr3UJm6oUisPwB8za`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "073bb31a-d4e4-47e0-a335-69d90e7e3a33",
  "isSidechain": false,
  "requestId": "req_011Cb4TxYKUV6p1KTkPTu4WA",
  "type": "assistant",
  "uuid": "f7f861bb-b22e-4427-b41b-9c2e9a8eced3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAEgeiAWmzFZcxrAUXCxtn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11250,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11250
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

_source line 9 · 2026-05-15T13:52:56.249Z_

<details open><summary>🔧 Tool call — Read · `toolu_018pJqif5CcbmyEUXZ6XEvjk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f861bb-b22e-4427-b41b-9c2e9a8eced3",
  "isSidechain": false,
  "requestId": "req_011Cb4TxYKUV6p1KTkPTu4WA",
  "type": "assistant",
  "uuid": "a80ecd5b-9c29-4c0e-b663-e8ca47b7f0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAEgeiAWmzFZcxrAUXCxtn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11250,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11250
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

_source line 10 · 2026-05-15T13:52:56.268Z_

<details><summary>↩ Tool result · `toolu_018pJqif5CcbmyEUXZ6XEvjk`</summary>

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
41	- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为"一种可选 scoring function"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）
42	
43	### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling
44	- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险
45	- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败
46	- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction
47	- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据
48	- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功
49	- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound
50	
51	### Claim 4 (Evaluation): EDCR 作为独立评估指标
52	- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|
53	- Evi-F1 盲区：不惩罚 plausible-looking distractor citations
54	- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）
55	- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比
56	
57	## MVP Evidence Summary
58	
59	| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |
60	|--------|--------|----------|--------|------|------|
61	| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |
62	| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |
63	| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |
64	| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |
65	| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |
66	| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |
67	| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |
68	
69	## Anticipated Reviewer Concerns
70	
71	### RC1: NLI reward 信号质量（高概率攻击）
72	- **攻击**: "DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声"
73	- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径
74	- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比
75	
76	### RC2: Gold evidence 标注不完整导致 false distractor
77	- **攻击**: "被标为 distractor 的句子可能是 annotator 遗漏的有效证据"
78	- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱
79	- **Research 补充**: false-distractor 鲁棒性量化分析
80	
81	### RC3: 评测可比性
82	- **攻击**: "生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？"
83	- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation
84	
85	### RC4: 单数据集 + 单模型泛化性
86	- **攻击**: "只在 DocRED + Qwen3-4B 上验证"
87	- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation
88	
89	### RC5: GRPO 配置可能不充分（Dream 三档一致）
90	- **攻击**: "G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身"
91	- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 "GRPO+QLoRA" 而非 "online RL"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）
92	- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整
93	
94	### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限
95	- **攻击**: "RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著"
96	- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确
97	- **Research**: CED reranker PoC（运行中），top_k ablation
98	
99	### RC7: 方法过于简单
100	- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度
101	
102	### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）
103	- **攻击**: "GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界"
104	- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱
105	
106	### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）
107	- **攻击**: "EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声"
108	- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性
109	
110	### RC10: Evi-F1 评测协议不一致（D041 已确认）
111	- **攻击**: "你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比"
112	- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）
113	
114	## Key Baselines (8+)
115	
116	1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL
117	2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）
118	3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法
119	4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中
120	5. **GRPO+CED**: 在线 RL with CED reward — negative baseline
121	6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)
122	7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)
123	8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)
124	9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)
125	
126	## Publishability Threshold
127	
128	- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）
129	- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证
130	- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric"，CED 降为可选组件
131	- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）
132	
133	## Research Phase Priorities
134	
135	| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |
136	|----------|------|---------|---------------|-----------|
137	| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |
138	| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |
139	| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |
140	| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |
141	| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |
142	| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |
143	| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |
144	| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |
145	| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |
146	| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |
147	| P1 | Re-DocRED extension | RC4 | ~12h | |
148	| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |
149	| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |
150	| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |
151	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a80ecd5b-9c29-4c0e-b663-e8ca47b7f0ea",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "0fec4581-f7ff-4e71-bf78-80b91205238c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md",
      "content": "# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n- **⚠️ Dream 风险**: 三档 Dream 审稿均指出 CED vs flat-NLI 可能不显著（p>0.05）。**Contingency**: 如 plan_001 结果 p>0.05，降级 CED 为\"一种可选 scoring function\"而非核心贡献，论文主贡献重心转移到 Claim 1（首个 evidence-generating LLM for DocRE）和 Claim 3（decoupling phenomenon）\n\n### Claim 3 (Analysis): GRPO+QLoRA 在文档级 IE 上 catastrophic forgetting 且呈现 evidence-extraction decoupling\n- **范围限定**: 仅对 GRPO+QLoRA（非泛化到所有 online RL）——Dream 三档一致指出 overclaim 风险\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- **核心发现 (decoupling)**: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——RL 差异化优化了 evidence 但摧毁了 extraction\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n- **⚠️ Dream 风险**: G=4 太小（标准 G=8-16），需测 G=8 排除 advantage estimation noise 的干扰；LoRA-only 是额外 confound\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: GRPO 配置可能不充分（Dream 三档一致）\n- **攻击**: \"G=4 太小（标准 G=8-16），LoRA-only 是 confound，可能是 GRPO+QLoRA 的问题而非 GRPO 本身\"\n- **应对**: (1) 加 G=8 实验验证（plan_011）；(2) 论文范围限定为 \"GRPO+QLoRA\" 而非 \"online RL\"；(3) 完整轨迹数据仍有效（3 reward × 2 lr × 全 checkpoint）\n- **Research**: GRPO G=8 实验 + 论文标题/claim 措辞调整\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n### RC8: 缺少中间方法 baseline（Dream 两档一致 [M][W]）\n- **攻击**: \"GRPO(online) vs RSFT(offline) 缺少 DPO/KTO 等中间方法，无法定位失败边界\"\n- **应对**: 加 DPO+CED experiment（plan_012），至少一个中间方法填补 online-offline 光谱\n\n### RC9: EDCR 需要人工验证（Dream 两档一致 [M][W]）\n- **攻击**: \"EDCR 未经人工标注验证，与 Evi-F1 的弱相关 r=-0.42 无法区分信号与噪声\"\n- **应对**: 100 样本人工标注研究（plan_013），验证 EDCR 与人类判断的相关性\n\n### RC10: Evi-F1 评测协议不一致（D041 已确认）\n- **攻击**: \"你们的 Evi-F1 (conditional) 与 DREEAM (joint) 不可比\"\n- **已修复**: 实现 DREEAM 对齐评测函数，论文报告两种 Evi-F1（joint 为主，conditional 为辅）\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT 在 test set 上 Evi-F1_joint（DREEAM 协议）> SFT baseline AND rel_f1 显著 > SFT baseline（D041: Evi-F1 对比 DREEAM 需用对齐协议，暂冻结绝对阈值）\n- **充分条件**: 上述 + CED vs flat-NLI RSFT 差异显著 + GRPO decoupling 分析完整 + EDCR 人工验证\n- **CED contingency**: 如 CED vs flat-NLI p>0.05 → 论文重心转为\"首个 evidence-generating LLM for DocRE + GRPO decoupling phenomenon + EDCR metric\"，CED 降为可选组件\n- **Failure pivot**: RSFT 在 test set 上无显著改进 → 转为 analysis contribution（GRPO failure analysis paper）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim/RC | 预估 GPU-hours | Dream 驱动 |\n|----------|------|---------|---------------|-----------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~4h | ⚠️ 三档一致风险 |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h | |\n| P0 | Evi-F1 DREEAM 协议对齐 + 重评 | RC10 | ~1h (CPU) | D041 |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h | |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h | |\n| P0 | GRPO G=8 实验 | C3/RC5 | ~8h | ⚠️ 三档一致 |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h | |\n| P1 | DPO+CED experiment | RC8 | ~12h | Dream [M][W] |\n| P1 | EDCR 人工标注验证 (100 samples) | RC9/C4 | ~0h (人工) | Dream [M][W] |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h | |\n| P1 | Re-DocRED extension | RC4 | ~12h | |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h | |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h | |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h | |\n",
      "numLines": 151,
      "startLine": 1,
      "totalLines": 151
    }
  },
  "sourceToolAssistantUUID": "a80ecd5b-9c29-4c0e-b663-e8ca47b7f0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T13:52:56.375Z_

<details><summary>↩ Tool result · `toolu_0149LgqUr3UJm6oUisPwB8za`</summary>

```text
1	[
2	  {
3	    "name": "CED vs flat-NLI RSFT ablation",
4	    "description": "用 flat-NLI scoring（DeBERTa NLI entailment score，无 contrastive margin）替代 CED 作为 RSFT 候选筛选信号。 复用 mvp2_rsft_gen_s0~s3 已有的 21952 candidates，仅替换打分函数。 flat-NLI score = mean entailment probability over cited sentences（无 hard-negative 对比）。 选 top_k=1 per document，训练配置对齐 CED-RSFT 最优（s43: 3ep, α=128, seed=43；r2b: 1ep, α=32, lr=1e-5）。 共训练 2 个 flat-NLI RSFT 配置，全量 dev eval。\n",
5	    "results": {
6	      "flatnli_rsft_a_rel_f1": 0.4412,
7	      "flatnli_rsft_a_evi_f1": 0.7948,
8	      "flatnli_rsft_a_edcr": 0.6952,
9	      "flatnli_rsft_a_n_selected": 2845,
10	      "flatnli_rsft_b_rel_f1": 0.4378,
11	      "flatnli_rsft_b_evi_f1": 0.7972,
12	      "flatnli_rsft_b_edcr": 0.6887,
13	      "ced_rsft_best_rel_f1": 0.4683,
14	      "ced_rsft_best_evi_f1": 0.8156,
15	      "ced_rsft_best_edcr": 0.6388,
16	      "delta_rel_f1": 0.0271,
17	      "delta_evi_f1": 0.0208,
18	      "delta_edcr": -0.0564,
19	      "paired_bootstrap_evi_f1_p": 0.0038,
20	      "paired_bootstrap_edcr_p": 0.0021,
21	      "paired_bootstrap_rel_f1_p": 0.0067
22	    },
23	    "tables": [
24	      {
25	        "name": "Table: CED vs flat-NLI RSFT Ablation (dev set)",
26	        "columns": [
27	          "Method",
28	          "rel_f1",
29	          "evi_f1",
30	          "EDCR",
31	          "n_train"
32	        ],
33	        "rows": [
34	          [
35	            "SFT baseline",
36	            0.4057,
37	            0.7979,
38	            0.7118,
39	            "12151 (gold)"
40	          ],
41	          [
42	            "RSFT flat-NLI (A: 3ep, α=128)",
43	            0.4412,
44	            0.7948,
45	            0.6952,
46	            2845
47	          ],
48	          [
49	            "RSFT flat-NLI (B: 1ep, α=32)",
50	            0.4378,
51	            0.7972,
52	            0.6887,
53	            2845
54	          ],
55	          [
56	            "RSFT CED (s43: 3ep, α=128)",
57	            0.4683,
58	            0.8156,
59	            0.6388,
60	            2718
61	          ],
62	          [
63	            "RSFT CED (r2b: 1ep, α=32)",
64	            0.4493,
65	            0.8128,
66	            0.6609,
67	            2718
68	          ],
69	          [
70	            "Δ (CED best - flatNLI best)",
71	            "+2.71pp",
72	            "+2.08pp",
73	            "-5.64pp",
74	            "—"
75	          ],
76	          [
77	            "p-value (paired bootstrap)",
78	            0.0067,
79	            0.0038,
80	            0.0021,
81	            "—"
82	          ]
83	        ]
84	      }
85	    ],
86	    "figures": [],
87	    "analysis": "CED vs flat-NLI 的差异模式完美验证了核心假说：CED 的优势集中在 distractor-dense 文档上。 在 distractor density > 0.4 的文档子集中，CED RSFT 的 evi_f1 优势扩大到 ~3.5pp， 而在 distractor density < 0.2 的文档中差异缩小到 ~0.8pp（不显著）。 这证明 CED 的 contrastive margin 确实在做它该做的事：区分 entity-sharing distractors 和真正的 evidence。 EDCR 的差异更稳定（几乎所有子集都显著），因为 EDCR 直接测量 distractor citation rate， 而 evi_f1 还受 recall 影响（有些 gold evidence 即使用 flat-NLI 也能被正确引用）。 rel_f1 的差异虽然也显著，但这是 evidence 质量提升的 downstream 效应，而非 CED 的直接目标。\n\n\nflat-NLI scoring 仍然能过滤掉完全无关的候选（如 format 错误、zero-F1 的），因此 flat-NLI RSFT 仍优于 SFT baseline（+3.2~3.6pp rel_f1）。 但 flat-NLI 的核心缺陷在于：entity-sharing distractor sentences 的 NLI entailment score 往往偏高（因为共享实体提供了 lexical overlap）， flat-NLI 无法区分\"真正支持关系的证据句\"和\"仅提及相同实体的干扰句\"。 因此 flat-NLI 筛选出的 top-1 候选中会保留更多 distractor-heavy 样本——这些样本的 evidence 看起来\"合理\"（高 NLI score） 但实际上引用了大量 entity-sharing non-gold sentences。 CED 的 contrastive margin = p(entail|gold) - max(p(entail|distractor)) 直接惩罚这种模式， 因此 CED-filtered 数据的训练样本 evidence 质量系统性更高。 这导致 CED RSFT 在 evi_f1 上高出 ~2.1pp（因为训练数据中 evidence 更精确，模型学到更好的 evidence 引用模式）， 在 EDCR 上低 5.6pp（因为训练数据中 distractor citations 更少，模型被条件化为避免引用干扰句）。 rel_f1 差异 +2.7pp 来自间接效应：CED 筛选出的候选不仅 evidence 更好，整体生成质量也更高（因为能正确定位 evidence 的生成通常也更准确地识别了关系）。 p<0.01 的显著性来自两个因素：(1) dev set 有 985 docs 提供足够统计力，(2) CED vs flat-NLI 的差异是系统性的（几乎在每种关系类型上 CED 都更好），不是少数异常值驱动的。 flat-NLI 选出 ~2845 样本（vs CED 2718），因为 flat-NLI 的筛选 landscape 不同（一些 CED 会拒绝的 distractor-heavy 候选在 flat-NLI 下得分高）。\n"
88	  },
89	  {
90	    "name": "Test set evaluation (RSFT best + SFT baseline)",
91	    "description": "用 RSFT best config (s43_r2: 3ep, α=128, seed=43) 和 SFT baseline 在 DocRED test set 上评估。 (1) CodaLab 提交获取官方 rel_F1/Ign_F1；(2) 本地 test set 计算 Evi-F1_joint (DREEAM 协议) 和 Evi-F1_conditional + EDCR；(3) flat-NLI RSFT best 也提交作为 ablation。\n",
92	    "results": {
93	      "sft_test_rel_f1": 0.3998,
94	      "sft_test_ign_f1": 0.3814,
95	      "sft_test_evi_f1_conditional": 0.7902,
96	      "sft_test_evi_f1_joint": 0.3216,
97	      "sft_test_edcr": 0.7185,
98	      "rsft_test_rel_f1": 0.4548,
99	      "rsft_test_ign_f1": 0.4367,
100	      "rsft_test_evi_f1_conditional": 0.8072,
101	      "rsft_test_evi_f1_joint": 0.3758,
102	      "rsft_test_edcr": 0.6476,
103	      "flatnli_test_rel_f1": 0.4302,
104	      "flatnli_test_ign_f1": 0.4118,
105	      "flatnli_test_evi_f1_conditional": 0.7883,
106	      "flatnli_test_evi_f1_joint": 0.3421,
107	      "flatnli_test_edcr": 0.7014,
108	      "rsft_vs_sft_test_rel_f1_delta": 0.055,
109	      "dev_to_test_degradation_rel_f1": 0.0135,
110	      "rsft_test_evi_f1_joint_value": 0.3758
111	    },
112	    "tables": [
113	      {
114	        "name": "Table: Test Set Main Results",
115	        "columns": [
116	          "Method",
117	          "rel_F1",
118	          "Ign_F1",
119	          "Evi-F1_joint",
120	          "Evi-F1_cond",
121	          "EDCR"
122	        ],
123	        "rows": [
124	          [
125	            "SFT baseline",
126	            0.3998,
127	            0.3814,
128	            0.3216,
129	            0.7902,
130	            0.7185
131	          ],
132	          [
133	            "RSFT flat-NLI",
134	            0.4302,
135	            0.4118,
136	            0.3421,
137	            0.7883,
138	            0.7014
139	          ],
140	          [
141	            "RSFT CED (FREIGE)",
142	            0.4548,
143	            0.4367,
144	            0.3758,
145	            0.8072,
146	            0.6476
147	          ],
148	          [
149	            "DREEAM (RoBERTa-large)",
150	            "—",
151	            "—",
152	            0.5734,
153	            "—",
154	            "—"
155	          ],
156	          [
157	            "SAIS (RoBERTa-large)",
158	            "—",
159	            "—",
160	            0.5567,
161	            "—",
162	            "—"
163	          ]
164	        ]
165	      }
166	    ],
167	    "figures": [],
168	    "analysis": "Test set 结果验证了 Claim 1 的核心——RSFT+CED 在 test 上稳定保持 +5.5pp rel_f1 优势，dev→test 退化仅 1.35pp。 Evi-F1_joint 与 DREEAM 的绝对比较：FREIGE 0.376 vs DREEAM 0.573。 DREEAM 的 joint Evi-F1 更高，但 DREEAM 是 encoder-based 方法，其\"evidence\"是 attention weight thresholding， 而 FREIGE 是生成式方法同时输出 triple+evidence——二者的 evidence 形式不同（implicit attention vs explicit citation）。 论文可这样叙述：FREIGE 是首个生成式方法在 DocRED 上输出显式 evidence，且其 joint Evi-F1 在 LLM 方法中无可比对手（LMRC、DocKS-RAG 均不输出 evidence）。 flat-NLI RSFT 在 test 上的表现确认了 CED 优势的泛化性（delta 方向一致）。\n\n\nDev→test degradation 约 1.35pp rel_f1（0.4683 → 0.4548），这在 DocRED 上属正常范围。 DocRED test set 的关系分布与 dev 非常接近（同一标注 pipeline），但 test 略难因为： (1) annotator 间一致性略低的 hard cases 更多被分配到 test，(2) distant supervision noise 在 test 中比例略高。 SFT test rel_f1=0.3998 比 dev 0.4057 低 0.6pp，同样符合 DocRED 的典型 dev-test gap。 因此 RSFT vs SFT 的 delta 在 test 上为 +5.5pp（vs dev +6.26pp），退化幅度合理。 Evi-F1_joint (DREEAM 协议) 远低于 conditional（0.376 vs 0.807），因为 joint 计算方式为 evi_f1 = Σ(triple_correct AND evi_correct) / Σ(gold_triples)，未正确预测的 triple 直接贡献 0 到 evidence score。 RSFT rel_f1=0.455 意味着约 45.5% 的 gold triples 被正确预测；在这些正确预测中，evi_f1_conditional ≈ 0.807； 因此 joint ≈ 0.455 × 0.807 × correction_factor ≈ 0.376（correction factor 因为 recall/precision 不对称略偏离乘积）。 SFT 的 joint 更低（0.322）因为 rel_f1 更低（0.400）。 Ign_F1 低于 F1 约 1.8pp，因为 RSFT 和 SFT 都对 shared entity pairs（train+dev 中出现的）有略高的准确率， 忽略这些后 F1 下降——这是 DocRED 评测的正常模式。 EDCR 在 test 上略高于 dev（0.648 vs 0.639），因为 test set 文档平均 entity density 略高，distractor 机会更多。\n"
169	  },
170	  {
171	    "name": "EDCR pipeline 验证 + cross-method diagnostic table",
172	    "description": "在所有 evidence-producing 方法上计算统一的 EDCR 指标，构建 cross-method diagnostic table。 方法包括：SFT, RSFT-CED (4 configs), RSFT-flatNLI (2 configs), CED-reranker, GRPO checkpoints (selected)。 同时计算 EDCR 与 evi_f1 的相关性（per-method level 和 per-document level）。\n",
173	    "results": {
174	      "sft_edcr": 0.7118,
175	      "rsft_ced_s43_edcr": 0.6388,
176	      "rsft_ced_s44_edcr": 0.635,
177	      "rsft_ced_r2a_edcr": 0.6641,
178	      "rsft_ced_r2b_edcr": 0.6609,
179	      "rsft_flatnli_a_edcr": 0.6952,
180	      "rsft_flatnli_b_edcr": 0.6887,
181	      "ced_reranker_edcr": 0.5983,
182	      "grpo_ckpt90_edcr": 0.8584,
183	      "grpo_ckpt100_lr5e6_edcr": 0.9876,
184	      "cross_method_pearson_r_edcr_vs_evif1": -0.42,
185	      "per_doc_spearman_edcr_vs_evif1": -0.31
186	    },
187	    "tables": [
188	      {
189	        "name": "Table: Cross-Method EDCR Diagnostic",
190	        "columns": [
191	          "Method",
192	          "rel_F1",
193	          "Evi-F1",
194	          "EDCR↓",
195	          "n_cited_sent",
196	          "n_distractor"
197	        ],
198	        "rows": [
199	          [
200	            "GRPO ckpt-100 (lr=5e-6)",
201	            0.0138,
202	            0.8504,
203	            0.9876,
204	            12834,
205	            12675
206	          ],
207	          [
208	            "GRPO ckpt-90 (lr=5e-5)",
209	            0.2108,
210	            0.5666,
211	            0.8584,
212	            9821,
213	            8431
214	          ],
215	          [
216	            "SFT baseline",
217	            0.4057,
218	            0.7979,
219	            0.7118,
220	            14206,
221	            10113
222	          ],
223	          [
224	            "RSFT flat-NLI (best)",
225	            0.4412,
226	            0.7972,
227	            0.6887,
228	            13875,
229	            9556
230	          ],
231	          [
232	            "RSFT CED r2b",
233	            0.4493,
234	            0.8128,
235	            0.6609,
236	            13542,
237	            8950
238	          ],
239	          [
240	            "RSFT CED s43",
241	            0.4683,
242	            0.8156,
243	            0.6388,
244	            13267,
245	            8475
246	          ],
247	          [
248	            "CED-reranker",
249	            0.4152,
250	            0.8214,
251	            0.5983,
252	            12983,
253	            7768
254	          ]
255	        ]
256	      }
257	    ],
258	    "figures": [],
259	    "analysis": "EDCR diagnostic table 的核心发现：GRPO ckpt-100 的 EDCR=0.99 + Evi-F1=0.85 是一个极端案例—— 模型输出了大量 citations 且其中 evidence recall 高（0.787），但 99% 的 cited sentences 是 distractor。 这是因为 GRPO 崩塌后模型倾向于引用文档中几乎所有句子，recall 自然高但 precision 极低。 CED-reranker 的 EDCR=0.60 是最低的，因为推理时 CED 直接选择 margin 最大的候选—— 但其 rel_f1=0.415 不如 RSFT CED s43=0.468，因为 reranking 不改变 candidate pool 的质量上限。 这支持了\"CED 最适合作为训练数据筛选信号而非纯推理 reranker\"的结论。\n\n\nCross-method table 展现清晰的 EDCR 梯度：GRPO（0.86-0.99）>> SFT（0.71）>> RSFT-flatNLI（0.69）>> RSFT-CED（0.64）>> CED-reranker（0.60）。 这个梯度与直觉一致：(1) GRPO 的 catastrophic forgetting 导致模型生成大量重复 entity mentions 但极少正确 relation， 几乎所有 cited sentences 都是 distractor；(2) SFT 从 gold data 学习但无 evidence quality 信号； (3) flat-NLI RSFT 比 SFT 好因为至少过滤了 zero-evidence 候选，但 flat-NLI 被 entity overlap 欺骗； (4) CED RSFT 进一步降低因为 contrastive margin 训练数据中 distractor 更少； (5) CED-reranker 最低因为推理时直接按 CED 选最佳候选，不受训练数据分布约束。 Cross-method Pearson r ≈ -0.42 表明 EDCR 与 evi_f1 有中等负相关但远非完美—— 这正是 EDCR 作为独立指标的价值：它捕获了 evi_f1 的盲区（plausible-looking distractor citations）。 Per-document Spearman 较低（-0.31）因为 EDCR 在单文档粒度上噪声较大（小 denominator 问题）。\n"
260	  },
261	  {
262	    "name": "DREEAM baseline reproduction",
263	    "description": "在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 evidence extraction 结果。 使用官方代码和预训练权重，计算 joint Evi-F1（与 FREIGE 可直接对比）。\n",
264	    "results": {
265	      "dreeam_dev_evi_f1_joint": 0.5718,
266	      "dreeam_dev_evi_f1_conditional": 0.8342,
267	      "dreeam_dev_rel_f1": 0.6312,
268	      "dreeam_paper_evi_f1": 0.5734,
269	      "reproduction_gap": -0.0016,
270	      "sais_dev_evi_f1_joint": 0.5542
271	    },
272	    "tables": [
273	      {
274	        "name": "Table: Evidence Baseline Comparison (dev set)",
275	        "columns": [
276	          "Method",
277	          "Type",
278	          "rel_F1",
279	          "Evi-F1_joint",
280	          "Evidence Form"
281	        ],
282	        "rows": [
283	          [
284	            "DREEAM",
285	            "Encoder",
286	            0.6312,
287	            0.5718,
288	            "Attention threshold"
289	          ],
290	          [
291	            "SAIS",
292	            "Encoder",
293	            0.6103,
294	            0.5542,
295	            "Attention threshold"
296	          ],
297	          [
298	            "FREIGE (RSFT CED)",
299	            "Generative LLM",
300	            0.4683,
301	            0.3758,
302	            "Explicit [S_i] citation"
303	          ],
304	          [
305	            "SFT baseline",
306	            "Generative LLM",
307	            0.4057,
308	            0.3216,
309	            "Explicit [S_i] citation"
310	          ],
311	          [
312	            "LMRC",
313	            "Generative LLM",
314	            0.6069,
315	            "—",
316	            "No evidence"
317	          ]
318	        ]
319	      }
320	    ],
321	    "figures": [],
322	    "analysis": "DREEAM/SAIS 复现确认了数字可靠。FREIGE 在 joint Evi-F1 上低于 DREEAM（0.376 vs 0.572）， 这主要由 rel_f1 gap 驱动（0.468 vs 0.631）。论文需要清晰叙述： (1) FREIGE 是首个输出显式 evidence 的 generative LLM DocRE 方法； (2) 在 LLM 方法类别内无直接竞争者（LMRC 无 evidence）； (3) 与 encoder methods 的 gap 主要来自 extraction 能力而非 evidence 能力——\n    在正确预测的 triple 上，FREIGE 的 conditional Evi-F1 (0.807) 接近 DREEAM 的 (0.834)。\n\n\nDREEAM 论文报告 Evi-F1 = 57.34，这是 joint protocol（evidence score 仅在 relation 也正确时计入）。 复现应在 ±0.3pp 内——DREEAM 是确定性 encoder 方法（无采样），差异仅来自 PyTorch 版本和随机种子对 fine-tuning 的微小影响。 使用官方 released checkpoint 应几乎完全复现。 DREEAM 的 rel_f1 ≈ 63.1%（RoBERTa-large encoder 的典型 DocRED 表现），远高于 FREIGE 的 46.8%—— 但 FREIGE 的贡献不在于超越 encoder SOTA 的 extraction 精度，而在于首次提供显式 evidence。 DREEAM 的 evidence 是 attention-based（隐式的），而 FREIGE 输出显式句子索引。 SAIS 复现 Evi-F1_joint ≈ 55.42，略低于 DREEAM，符合论文报告。\n"
323	  },
324	  {
325	    "name": "CED-as-reranker PoC",
326	    "description": "推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。\n",
327	    "results": {
328	      "reranker_rel_f1": 0.4152,
329	      "reranker_evi_f1": 0.8214,
330	      "reranker_edcr": 0.5983,
331	      "reranker_evi_precision": 0.8356,
332	      "reranker_evi_recall": 0.8078,
333	      "sft_baseline_rel_f1": 0.4057,
334	      "sft_baseline_evi_f1": 0.7979,
335	      "sft_baseline_edcr": 0.7118,
336	      "delta_rel_f1_vs_sft": 0.0095,
337	      "delta_evi_f1_vs_sft": 0.0235,
338	      "delta_edcr_vs_sft": -0.1135
339	    },
340	    "tables": [
341	      {
342	        "name": "Table: CED Usage Modes Comparison",
343	        "columns": [
344	          "CED Usage",
345	          "rel_F1",
346	          "Evi-F1",
347	          "EDCR↓",
348	          "Extra Training"
349	        ],
350	        "rows": [
351	          [
352	            "SFT (no CED)",
353	            0.4057,
354	            0.7979,
355	            0.7118,
356	            "—"
357	          ],
358	          [
359	            "CED-reranker (inference)",
360	            0.4152,
361	            0.8214,
362	            0.5983,
363	            "None"
364	          ],
365	          [
366	            "RSFT flat-NLI (training, no CED)",
367	            0.4412,
368	            0.7972,
369	            0.6887,
370	            "RSFT"
371	          ],
372	          [
373	            "RSFT CED (training)",
374	            0.4683,
375	            0.8156,
376	            0.6388,
377	            "RSFT"
378	          ]
379	        ]
380	      }
381	    ],
382	    "figures": [],
383	    "analysis": "CED-reranker 证明了 CED 作为质量信号的有效性（EDCR 大幅下降 -11.35pp）， 但也证明了仅靠推理时 reranking 不够——rel_f1 提升微弱。 这形成一个很好的 ablation 故事：CED 信号本身有效，但需要通过 RSFT 训练来充分利用。 论文可在 analysis section 用此对比说明\"为什么选择 RSFT 而非 reranking\"。\n\n\nCED-reranker 在 EDCR 上表现最好（0.598），因为推理时直接选 CED margin 最大的候选—— 这等价于选 distractor citation 最少的那个生成。evi_f1 也因此改善（+2.35pp）， 因为更准确的 evidence 引用提升了 precision。 但 rel_f1 提升有限（+0.95pp），原因是 CED 的打分维度是 evidence quality 而非 extraction accuracy。 N=8 候选的 extraction diversity 有限（Jaccard 在 temp=0.7 下约 0.17）， 重排仅在候选间有 evidence 质量差异时有用，对 extraction 错误无能为力。 与 RSFT CED (rel_f1=0.468) 的差距（-5.3pp）证明了训练 vs 推理的区别： RSFT 通过高质量数据改变了模型的 generation distribution，而 reranker 仅从已有分布中选最佳。 这支持论文的\"CED 作为训练信号优于推理信号\"结论。\n"
384	  },
385	  {
386	    "name": "Model size ablation (1.7B / 8B)",
387	    "description": "在 Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT+CED pipeline，验证方法对模型规模的泛化性。 每个模型：SFT baseline + RSFT CED (best config from 4B)，dev set 评估。\n",
388	    "results": {
389	      "qwen_1_7b_sft_rel_f1": 0.3412,
390	      "qwen_1_7b_sft_evi_f1": 0.7534,
391	      "qwen_1_7b_sft_edcr": 0.7456,
392	      "qwen_1_7b_rsft_ced_rel_f1": 0.3724,
393	      "qwen_1_7b_rsft_ced_evi_f1": 0.7782,
394	      "qwen_1_7b_rsft_ced_edcr": 0.6934,
395	      "qwen_1_7b_delta_rel_f1": 0.0312,
396	      "qwen_8b_sft_rel_f1": 0.4423,
397	      "qwen_8b_sft_evi_f1": 0.8125,
398	      "qwen_8b_sft_edcr": 0.6892,
399	      "qwen_8b_rsft_ced_rel_f1": 0.4912,
400	      "qwen_8b_rsft_ced_evi_f1": 0.8367,
401	      "qwen_8b_rsft_ced_edcr": 0.6187,
402	      "qwen_8b_delta_rel_f1": 0.0489
403	    },
404	    "tables": [
405	      {
406	        "name": "Table: Model Size Ablation",
407	        "columns": [
408	          "Model",
409	          "Method",
410	          "rel_F1",
411	          "Evi-F1",
412	          "EDCR↓",
413	          "Δ rel_F1"
414	        ],
415	        "rows": [
416	          [
417	            "Qwen3-1.7B",
418	            "SFT",
419	            0.3412,
420	            0.7534,
421	            0.7456,
422	            "—"
423	          ],
424	          [
425	            "Qwen3-1.7B",
426	            "RSFT+CED",
427	            0.3724,
428	            0.7782,
429	            0.6934,
430	            "+3.12pp"
431	          ],
432	          [
433	            "Qwen3-4B",
434	            "SFT",
435	            0.4057,
436	            0.7979,
437	            0.7118,
438	            "—"
439	          ],
440	          [
441	            "Qwen3-4B",
442	            "RSFT+CED",
443	            0.4683,
444	            0.8156,
445	            0.6388,
446	            "+6.26pp"
447	          ],
448	          [
449	            "Qwen3-8B",
450	            "SFT",
451	            0.4423,
452	            0.8125,
453	            0.6892,
454	            "—"
455	          ],
456	          [
457	            "Qwen3-8B",
458	            "RSFT+CED",
459	            0.4912,
460	            0.8367,
461	            0.6187,
462	            "+4.89pp"
463	          ]
464	        ]
465	      }
466	    ],
467	    "figures": [],
468	    "analysis": "Model size ablation 证明 RSFT+CED 在 1.7B-8B 范围内一致有效。 4B 的相对提升最大可能因为它处于\"sweet spot\"——模型足够大产生多样高质量候选， 但还不够大到 SFT 已经很好。8B SFT 的 EDCR 已经较低（0.689），说明更大模型本身就更善于引用相关 evidence， 但 RSFT+CED 仍有增量价值。\n\n\n1.7B 模型基础能力更弱（SFT rel_f1 0.341 vs 4B 的 0.406），但 RSFT+CED 的相对提升仍然显著（+3.1pp）。 提升幅度略小于 4B（+6.3pp），因为 1.7B 的 candidate pool 质量上限更低—— N=8 生成中 top-1 CED candidate 的质量受限于模型的 generation capacity。 8B 模型基础更强（SFT 0.442），RSFT+CED 提升到 0.491（+4.9pp）， 提升幅度介于 1.7B 和 4B 之间。8B 的 SFT baseline 已经较高，留给 RSFT 的 headroom 相对更小， 但绝对性能最好。 跨三个规模的一致提升（+3.1 / +6.3 / +4.9pp）证明 CED+RSFT 不是模型特定的 trick， 而是一个通用的 evidence quality 提升机制。 EDCR 模式一致：1.7B SFT EDCR 最高（0.746）因为小模型更易引用不相关句子， RSFT+CED 在所有规模上都降低 EDCR（-5.2 / -7.3 / -7.1pp）。\n"
469	  },
470	  {
471	    "name": "Re-DocRED extension",
472	    "description": "在 Re-DocRED（修正 false negative 标注的版本）上评估 SFT 和 RSFT+CED，验证方法在更干净标注下的表现。\n",
473	    "results": {
474	      "redocred_sft_rel_f1": 0.4534,
475	      "redocred_sft_evi_f1": 0.8112,
476	      "redocred_rsft_ced_rel_f1": 0.5089,
477	      "redocred_rsft_ced_evi_f1": 0.8378,
478	      "redocred_rsft_ced_edcr": 0.6023,
479	      "redocred_delta_rel_f1": 0.0555
480	    },
481	    "tables": [
482	      {
483	        "name": "Table: DocRED vs Re-DocRED",
484	        "columns": [
485	          "Dataset",
486	          "Method",
487	          "rel_F1",
488	          "Evi-F1",
489	          "EDCR↓"
490	        ],
491	        "rows": [
492	          [
493	            "DocRED",
494	            "SFT",
495	            0.4057,
496	            0.7979,
497	            0.7118
498	          ],
499	          [
500	            "DocRED",
501	            "RSFT+CED",
502	            0.4683,
503	            0.8156,
504	            0.6388
505	          ],
506	          [
507	            "Re-DocRED",
508	            "SFT",
509	            0.4534,
510	            0.8112,
511	            0.6892
512	          ],
513	          [
514	            "Re-DocRED",
515	            "RSFT+CED",
516	            0.5089,
517	            0.8378,
518	            0.6023
519	          ]
520	        ]
521	      }
522	    ],
523	    "figures": [],
524	    "analysis": "Re-DocRED 结果为 RC4（单数据集泛化性）提供了部分回应。方法在更干净标注下表现更好且 delta 保持， 说明 CED+RSFT 不是在利用标注噪声。\n\n\nRe-DocRED 修正了 DocRED 中约 25% 的 false negative relations（标注遗漏）， 因此所有方法的绝对 F1 都上升（SFT 0.453 vs 原 0.406）——被原始标注遗漏的正确预测不再被惩罚。 RSFT+CED 的 delta（+5.55pp）与 DocRED 上的（+6.26pp）接近， 说明 CED 的 evidence quality 提升不依赖于标注噪声的存在。 EDCR 在 Re-DocRED 上略低（0.602 vs 0.639），因为部分被标为 distractor 的句子在 Re-DocRED 中被重新标注为 gold evidence， 降低了 false-distractor 率。这也间接验证了 CED margin 的鲁棒性—— 即使标注不完美，CED 仍然能有效区分 evidence 质量。\n"
525	  },
526	  {
527	    "name": "top_k ablation (k=1 vs k=3)",
528	    "description": "CED scoring 筛选 top_k=3（每文档选 CED top-3 候选，~8000 训练样本）vs top_k=1（~2718 样本）， 验证 CED 过滤严格度对 RSFT 训练质量的影响。\n",
529	    "results": {
530	      "topk1_n_samples": 2718,
531	      "topk1_rel_f1": 0.4683,
532	      "topk1_evi_f1": 0.8156,
533	      "topk1_edcr": 0.6388,
534	      "topk3_n_samples": 7856,
535	      "topk3_rel_f1": 0.4523,
536	      "topk3_evi_f1": 0.8034,
537	      "topk3_edcr": 0.6712,
538	      "topk3_mean_ced_score": 0.5234
539	    },
540	    "tables": [
541	      {
542	        "name": "Table: top_k Ablation",
543	        "columns": [
544	          "top_k",
545	          "n_train",
546	          "mean_CED",
547	          "rel_F1",
548	          "Evi-F1",
549	          "EDCR↓"
550	        ],
551	        "rows": [
552	          [
553	            1,
554	            2718,
555	            0.6683,
556	            0.4683,
557	            0.8156,
558	            0.6388
559	          ],
560	          [
561	            3,
562	            7856,
563	            0.5234,
564	            0.4523,
565	            0.8034,
566	            0.6712
567	          ]
568	        ]
569	      }
570	    ],
571	    "figures": [],
572	    "analysis": "top_k ablation 确认了 CED 质量过滤的重要性，同时也为 reviewer 提供了\"为什么不用更多数据\"的回答。 这是一个 diminishing-returns-with-quality-dilution 的经典案例。\n\n\ntop_k=3 引入了 ~5100 额外训练样本，但这些是每文档的第 2、3 名候选——CED score 系统性更低 （mean CED 0.523 vs top_k=1 的 0.668）。更多训练数据带来的拟合优势被更低数据质量抵消： (1) rel_f1 下降 1.6pp 因为质量较低的候选引入了更多 extraction 错误模式； (2) evi_f1 下降 1.2pp 因为 2nd/3rd 候选的 evidence 质量明显低于 1st； (3) EDCR 上升 3.2pp 因为训练数据中混入了更多 distractor-heavy 样本。 这验证了 CED 作为质量过滤器的\"宁缺毋滥\"策略——strict top_k=1 优于宽松 top_k=3， 因为 RSFT 的核心机制是让模型从高质量样本中学习，不需要海量数据。 这也解释了为什么 2718 样本（仅占 21952 候选的 12.4%）就足够有效—— SFT 阶段已经提供了足够的\"通用知识\"，RSFT 只需少量高质量样本来校准 evidence 引用行为。\n"
573	  },
574	  {
575	    "name": "GRPO G=8 实验",
576	    "description": "G=8 + CED reward + kl_coef=0.01 + lr=5e-6，验证 GRPO 在标准 group size 下是否仍然 catastrophic forgetting。 排除 G=4 的 advantage estimation noise 作为 confounding factor。\n",
577	    "results": {
578	      "grpo_g8_best_rel_f1": 0.0312,
579	      "grpo_g8_best_evi_f1": 0.8156,
580	      "grpo_g8_best_edcr": 0.9812,
581	      "grpo_g8_best_checkpoint": "ckpt-80",
582	      "grpo_g8_final_rel_f1": 0.0287,
583	      "grpo_g8_final_reward": 1.287,
584	      "grpo_g8_forgetting_onset_step": 15,
585	      "grpo_g8_collapse_pattern": "同 G=4：reward ↑ + rel_f1 ↓，但 collapse 稍慢",
586	      "grpo_g4_best_rel_f1": 0.0138,
587	      "grpo_g4_best_evi_f1": 0.8504
588	    },
589	    "tables": [
590	      {
591	        "name": "Table: GRPO Group Size Comparison",
592	        "columns": [
593	          "Config",
594	          "G",
595	          "Best rel_F1",
596	          "Best Evi-F1",
597	          "EDCR",
598	          "Forgetting?"
599	        ],
600	        "rows": [
601	          [
602	            "GRPO+CED lr=5e-6",
603	            4,
604	            0.0138,
605	            0.8504,
606	            0.9876,
607	            "Yes (step ~10)"
608	          ],
609	          [
610	            "GRPO+CED lr=5e-6",
611	            8,
612	            0.0312,
613	            0.8156,
614	            0.9812,
615	            "Yes (step ~15)"
616	          ],
617	          [
618	            "GRPO+CED lr=5e-5",
619	            4,
620	            0.2108,
621	            0.5666,
622	            0.8584,
623	            "Yes (partial)"
624	          ],
625	          [
626	            "SFT baseline",
627	            "—",
628	            0.4057,
629	            0.7979,
630	            0.7118,
631	            "No"
632	          ]
633	        ]
634	      }
635	    ],
636	    "figures": [],
637	    "analysis": "G=8 实验是 Claim 3 的关键验证——排除了 advantage estimation noise 作为 G=4 failure 的替代解释。 rel_f1 从 0.014 微升到 0.031 说明 G 确实有微弱影响，但量级上不改变结论。 论文可以写：\"Increasing group size from 4 to 8 marginally delays but does not prevent catastrophic forgetting (best rel_F1: 0.031 vs 0.014, both << SFT 0.406), confirming the structural incompatibility of GRPO+QLoRA with document-level IE.\"\n\n\nG=8 将 advantage estimation 的方差降低约 √2 倍（相对 G=4），这确实改善了 gradient quality。 然而 catastrophic forgetting 的根因不是 advantage noise，而是 GRPO+QLoRA 在文档级 IE 任务上的结构性问题： (1) QLoRA 的 rank-limited 参数空间在接收 RL gradient 时容易覆盖 SFT 学到的 extraction schema knowledge； (2) CED/NLI reward 在 evidence 维度上的梯度远强于 extraction 维度（因为 evidence quality 变化更容易被 reward 捕获），\n    导致模型优先优化 evidence 而放弃 extraction；\n(3) 文档级 IE 的输出空间极大（多 triple + evidence），policy gradient 的 credit assignment 困难。 G=8 的 rel_f1 峰值（0.031）略高于 G=4（0.014），说明更稳定的 advantage 确实有边际帮助， 但远不足以避免 forgetting（仍 < 0.05，远低于 SFT 的 0.406）。 evi_f1 仍然高（0.816），再次确认 decoupling phenomenon——RL 优化了 evidence 但摧毁了 extraction。 Forgetting onset 稍慢（step 15 vs G=4 的 step ~10），因为 G=8 的 gradient 更保守， 但最终 trajectory 殊途同归。\n"
638	  },
639	  {
640	    "name": "DPO+CED experiment",
641	    "description": "用 RSFT candidate pool 构造 preference pairs：每文档 CED top-1 为 chosen，CED bottom-1（F1>0.1 filter）为 rejected。 DPO 训练（β=0.1, lr=1e-5, 1 epoch），验证 offline preference learning 的表现。\n",
642	    "results": {
643	      "dpo_rel_f1": 0.3245,
644	      "dpo_evi_f1": 0.7856,
645	      "dpo_edcr": 0.6834,
646	      "dpo_n_pairs": 2412,
647	      "dpo_beta": 0.1,
648	      "sft_rel_f1": 0.4057,
649	      "rsft_ced_rel_f1": 0.4683,
650	      "grpo_g8_best_rel_f1": 0.0312
651	    },
652	    "tables": [
653	      {
654	        "name": "Table: Online-Offline RL Spectrum",
655	        "columns": [
656	          "Method",
657	          "RL Type",
658	          "rel_F1",
659	          "Evi-F1",
660	          "EDCR↓",
661	          "Catastrophic?"
662	        ],
663	        "rows": [
664	          [
665	            "GRPO G=8",
666	            "Online (on-policy)",
667	            0.0312,
668	            0.8156,
669	            0.9812,
670	            "Yes"
671	          ],
672	          [
673	            "GRPO G=4",
674	            "Online (on-policy)",
675	            0.0138,
676	            0.8504,
677	            0.9876,
678	            "Yes"
679	          ],
680	          [
681	            "DPO+CED",
682	            "Offline (preference)",
683	            0.3245,
684	            0.7856,
685	            0.6834,
686	            "No (but degraded)"
687	          ],
688	          [
689	            "SFT",
690	            "No RL",
691	            0.4057,
692	            0.7979,
693	            0.7118,
694	            "No"
695	          ],
696	          [
697	            "RSFT+CED",
698	            "Offline (filtered SFT)",
699	            0.4683,
700	            0.8156,
701	            0.6388,
702	            "No"
703	          ]
704	        ]
705	      }
706	    ],
707	    "figures": [],
708	    "analysis": "DPO 实验填补了 GRPO 和 RSFT 之间的空白。核心洞察： (1) 问题不在 \"offline vs online\" 的二元对立——DPO（offline）也退化了； (2) 问题在于 RL loss function 对文档级 IE 输出空间的适配性——\n    GRPO 的 policy gradient 和 DPO 的 preference loss 都在 token level 操作，\n    对长结构化输出的 credit assignment 困难；\n(3) RSFT 之所以成功，是因为它根本不用 RL loss——直接 supervised learning on filtered data，\n    避免了 credit assignment 问题。\n这加强了论文的理论贡献：不是\"CED reward 好\"而是\"CED 作为数据质量信号 + SFT 训练范式 = 最佳组合\"。\n\n\nDPO 作为 offline preference optimization，避免了 GRPO 的 on-policy sampling 导致的 distribution shift， 因此不会 catastrophic forgetting——rel_f1=0.325 远高于 GRPO 的 0.031。 但 DPO 弱于 RSFT（0.325 vs 0.468）的原因是： (1) DPO 的 implicit reward model 需要从 preference pairs 中学习 CED 信号，\n    而 RSFT 直接在 CED-selected 高质量样本上 supervised learning——后者更 sample-efficient；\n(2) DPO 的 contrastive loss 同时推高 chosen 和推低 rejected 的 likelihood，\n    但在 IE 任务中 chosen/rejected 的差异主要在 evidence 而非 extraction——\n    推低 rejected 可能意外降低了正确 extraction pattern 的概率；\n(3) DocRED 的输出空间太大（长 JSON），DPO 的 token-level KL penalty 对长序列的控制力不足。 DPO 的 evi_f1（0.786）接近 SFT（0.798），说明 evidence 质量未被显著改善—— DPO 未能从 preference pairs 中有效学到 CED 的 evidence quality 信号。 这与 RSFT 的 evi_f1=0.816 形成对比，进一步支持\"CED 适合作为筛选信号而非学习目标\"。 rel_f1=0.325 vs SFT=0.406 实际上是 DPO 的退化（-8.1pp），这是因为 DPO 的 rejected 样本中包含的 extraction pattern 被不当抑制了——一种轻度的 DPO \"over-optimization\"。 整体光谱：GRPO (0.031) << DPO (0.325) < SFT (0.406) < RSFT (0.468)， 清晰展示了 online → offline → no-RL → offline-filtered 的退化/改善梯度。\n"
709	  },
710	  {
711	    "name": "EDCR 人工标注验证",
712	    "description": "100 个样本（每样本 = 一个 predicted triple + 其 cited evidence sentences）， 3 名标注者独立判断每个 cited sentence 是否真正支持对应 relation。 计算 EDCR_auto 与 human_distractor_rate 的 Pearson r。\n",
713	    "results": {
714	      "n_samples": 100,
715	      "n_annotators": 3,
716	      "inter_annotator_kappa": 0.72,
717	      "edcr_human_pearson_r": 0.62,
718	      "edcr_human_spearman_r": 0.58,
719	      "human_distractor_rate_mean": 0.583,
720	      "auto_edcr_mean": 0.651,
721	      "edcr_auto_vs_human_bias": 0.068,
722	      "sft_human_distractor_rate": 0.645,
723	      "rsft_ced_human_distractor_rate": 0.524,
724	      "rsft_flatnli_human_distractor_rate": 0.608,
725	      "grpo_human_distractor_rate": 0.954
726	    },
727	    "tables": [
728	      {
729	        "name": "Table: EDCR Human Validation",
730	        "columns": [
731	          "Method",
732	          "EDCR_auto",
733	          "Human_distractor_rate",
734	          "Δ",
735	          "n"
736	        ],
737	        "rows": [
738	          [
739	            "GRPO ckpt-90",
740	            0.858,
741	            0.954,
742	            -0.096,
743	            25
744	          ],
745	          [
746	            "SFT",
747	            0.712,
748	            0.645,
749	            0.067,
750	            25
751	          ],
752	          [
753	            "RSFT flat-NLI",
754	            0.695,
755	            0.608,
756	            0.087,
757	            25
758	          ],
759	          [
760	            "RSFT CED",
761	            0.639,
762	            0.524,
763	            0.115,
764	            25
765	          ],
766	          [
767	            "Overall Pearson r",
768	            "—",
769	            "—",
770	            0.62,
771	            100
772	          ]
773	        ]
774	      }
775	    ],
776	    "figures": [],
777	    "analysis": "Pearson r=0.62 满足 best tier 要求（[0.55, 0.75]），验证了 EDCR 作为自动指标的有效性。 但需要在论文中诚实讨论 limitations：(1) entity-sharing 是 distractor 的代理指标而非完美定义； (2) CED RSFT 的 auto-human gap 最大（0.115），说明 CED 训练的模型引用模式与人类直觉有微妙差异—— 部分人类认为有用的 contextual sentences（虽然不是 gold evidence）被 EDCR 标为 distractor。 这实际上是一个有趣的发现，可以在 discussion 中展开。\n\n\nPearson r=0.62 表明 EDCR 与人类判断有中等偏强的正相关——EDCR 确实在测量有意义的 evidence 质量维度。 r 未达到 0.8+ 的原因：(1) EDCR 用 entity-sharing 作为 distractor 的操作性定义， 而人类判断基于语义支持关系——部分 entity-sharing sentences 人类认为确实支持关系（partial evidence）， 部分 non-entity-sharing sentences 人类认为是 distractor（基于语义而非 entity overlap）； (2) 100 样本的统计力有限，置信区间较宽。 Auto EDCR 略高估（bias +6.8pp），因为 entity-sharing 的自动判定过于严格—— 一些共享实体但确实提供支持的句子被 EDCR 错误标为 distractor。 Inter-annotator Cohen's κ=0.72（substantial agreement），说明 evidence 支持判断本身具有一定主观性， 但三人投票足以产生可靠的 gold standard。 分方法看，human distractor rate 的排序与 EDCR 一致：GRPO (0.954) >> SFT (0.645) > flatNLI (0.608) > CED (0.524)， 进一步验证了 EDCR 的诊断方向正确。\n"
778	  },
779	  {
780	    "name": "GRPO forgetting 详细分析 + 可视化",
781	    "description": "整理全部 GRPO checkpoint（G=4 lr=5e-5, G=4 lr=5e-6, G=8）的完整训练轨迹， 绘制 forgetting dynamics 可视化。\n",
782	    "results": {
783	      "n_checkpoints_analyzed": 42,
784	      "n_configs": 3,
785	      "decoupling_onset_step_g4_lr5e6": 10,
786	      "decoupling_onset_step_g4_lr5e5": 5,
787	      "decoupling_onset_step_g8": 15,
788	      "peak_evi_f1_across_configs": 0.8504,
789	      "min_rel_f1_across_configs": 0.0028
790	    },
791	    "tables": [],
792	    "figures": [],
793	    "analysis": "可视化清晰展示 decoupling phenomenon 的三个阶段。Phase diagram 是最有力的图—— 所有 GRPO configs 的 trajectory 都从 (SFT rel_f1, SFT evi_f1) 出发，向 (↓, ↑) 移动， 形成一个\"左上角 attractor\"。RSFT 的 trajectory 则从同一起点向 (↑, ↑) 移动， 两个方向的对比直观地说明了 online vs offline RL 的行为差异。\n\n\nGRPO 的 forgetting dynamics 在所有配置中呈现一致模式： (1) 早期（step 1-5/10/15 取决于 lr 和 G）：rel_f1 开始下降但 evi_f1 开始上升——decoupling onset； (2) 中期（step 5-50）：reward 持续上升，rel_f1 加速下降至 <0.05，evi_f1 平台期 ~0.80-0.85； (3) 后期（step 50-100）：reward 饱和，rel_f1 在底部震荡（<0.02），evi_f1 微调。 lr=5e-5 的 forgetting 最快（step 5 开始）但 rel_f1 最终峰值最高（0.211 at ckpt-90）， 因为高 lr 的 RL gradient 足够强同时推动 extraction 和 evidence，但最终 evidence gradient 占优。 lr=5e-6 的 forgetting 最慢开始但最终 rel_f1 最低（0.014）， 因为低 lr 的 RL gradient 更精细地优化了 reward 但缺乏足够的 extraction signal。 G=8 在 step 15 开始 forgetting——比 G=4 lr=5e-6 的 step 10 晚， 符合\"更稳定 advantage estimation → 更保守 update\"的预期。\n"
794	  },
795	  {
796	    "name": "NLI model ablation (DeBERTa-base vs large)",
797	    "description": "用 DeBERTa-v3-large 替代 DeBERTa-v3-base 作为 CED scorer，重新打分已有 candidates， 对比两个 NLI 模型对 CED scoring 质量的影响。\n",
798	    "results": {
799	      "deberta_base_mean_ced": 0.6683,
800	      "deberta_large_mean_ced": 0.7012,
801	      "deberta_base_discrimination_acc": 0.815,
802	      "deberta_large_discrimination_acc": 0.847,
803	      "deberta_large_rsft_rel_f1": 0.4721,
804	      "deberta_large_rsft_evi_f1": 0.8189,
805	      "deberta_large_rsft_edcr": 0.6312,
806	      "deberta_base_rsft_rel_f1": 0.4683,
807	      "deberta_base_rsft_evi_f1": 0.8156,
808	      "deberta_base_rsft_edcr": 0.6388,
809	      "delta_rel_f1": 0.0038,
810	      "delta_evi_f1": 0.0033
811	    },
812	    "tables": [
813	      {
814	        "name": "Table: NLI Model Ablation",
815	        "columns": [
816	          "NLI Model",
817	          "Params",
818	          "Disc. Acc",
819	          "Mean CED",
820	          "RSFT rel_F1",
821	          "RSFT Evi-F1"
822	        ],
823	        "rows": [
824	          [
825	            "DeBERTa-v3-base",
826	            "86M",
827	            0.815,
828	            0.668,
829	            0.4683,
830	            0.8156
831	          ],
832	          [
833	            "DeBERTa-v3-large",
834	            "304M",
835	            0.847,
836	            0.701,
837	            0.4721,
838	            0.8189
839	          ],
840	          [
841	            "Δ",
842	            "—",
843	            "+0.032",
844	            "+0.033",
845	            "+0.38pp",
846	            "+0.33pp"
847	          ]
848	        ]
849	      }
850	    ],
851	    "figures": [],
852	    "analysis": "NLI model ablation 的 marginal 差异是好消息——方法鲁棒、计算门槛低。 论文可以一句话带过：\"Replacing DeBERTa-base with DeBERTa-large yields marginal improvements (+0.38pp rel_F1), confirming that CED's effectiveness stems from the contrastive design rather than the NLI model's capacity.\"\n\n\nDeBERTa-large 的 NLI 能力确实更强（discrimination accuracy 0.847 vs 0.815）， CED margin 也更大（0.701 vs 0.668），但这些改善传导到 RSFT 最终结果时被大幅衰减： (1) CED scoring 已经是一个\"阈值化\"操作（top_k=1），只要排序大致正确即可——\n    base 和 large 的 top-1 选择一致率约 89%，仅 11% 文档的 top-1 不同；\n(2) 这 11% 不同的文档中，large 选出的候选确实稍好，但对总体 RSFT 训练的影响被稀释； (3) rel_f1 差异仅 +0.38pp，不具统计显著性。 这是一个积极结果：CED 方法对 NLI 模型选择不敏感，base 模型足够用， 降低了方法的计算门槛（DeBERTa-base ~86M vs large ~304M参数）。 同时回应了 RC1（NLI reward 信号质量）：即使用更强的 NLI 模型，CED 提升也很小—— 说明 CED 的瓶颈不在 NLI 模型质量，而在于 RSFT 训练本身的 sample efficiency。\n"
853	  },
854	  {
855	    "name": "Evi-F1 DREEAM 协议对齐重评",
856	    "description": "对所有已有 dev eval 结果重新计算 Evi-F1_joint（DREEAM 协议：evi score 仅在 relation 也正确时计入）。 已有的 Evi-F1 为 conditional（given correct relation），需要同时报告两种。\n",
857	    "results": {
858	      "sft_evi_f1_joint": 0.3216,
859	      "rsft_ced_s43_evi_f1_joint": 0.3812,
860	      "rsft_ced_s44_evi_f1_joint": 0.3724,
861	      "rsft_ced_r2a_evi_f1_joint": 0.3657,
862	      "rsft_ced_r2b_evi_f1_joint": 0.3663,
863	      "rsft_flatnli_best_evi_f1_joint": 0.3498,
864	      "grpo_best_evi_f1_joint": 0.0118,
865	      "ced_reranker_evi_f1_joint": 0.3412
866	    },
867	    "tables": [
868	      {
869	        "name": "Table: Conditional vs Joint Evi-F1",
870	        "columns": [
871	          "Method",
872	          "rel_F1",
873	          "Evi-F1_cond",
874	          "Evi-F1_joint",
875	          "EDCR"
876	        ],
877	        "rows": [
878	          [
879	            "SFT",
880	            0.4057,
881	            0.7979,
882	            0.3216,
883	            0.7118
884	          ],
885	          [
886	            "RSFT flat-NLI best",
887	            0.4412,
888	            0.7972,
889	            0.3498,
890	            0.6887
891	          ],
892	          [
893	            "CED-reranker",
894	            0.4152,
895	            0.8214,
896	            0.3412,
897	            0.5983
898	          ],
899	          [
900	            "RSFT CED s43",
901	            0.4683,
902	            0.8156,
903	            0.3812,
904	            0.6388
905	          ],
906	          [
907	            "GRPO best (lr=5e-5)",
908	            0.2108,
909	            0.5666,
910	            0.1192,
911	            0.8584
912	          ],
913	          [
914	            "GRPO best (lr=5e-6)",
915	            0.0138,
916	            0.8504,
917	            0.0118,
918	            0.9876
919	          ]
920	        ]
921	      }
922	    ],
923	    "figures": [],
924	    "analysis": "Joint Evi-F1 是论文主指标（与 DREEAM 可比），conditional 作为辅助指标。 Joint 指标下 GRPO 的灾难性表现（0.012）比 conditional（0.850）更直观地展示了 decoupling 的后果—— 模型学会了给好 evidence 但找不到正确 relation，导致 evidence 能力被浪费。 论文 main table 应以 joint 为主列，conditional 放 appendix。\n\nJoint Evi-F1 大幅低于 conditional，因为它对未正确预测的 relation triples 给 0 分。 公式近似为：joint ≈ Σ_{correct triples} evi_f1(triple) / |gold_triples|。 SFT rel_recall=0.407 → 约 40.7% gold triples 被正确预测 → joint ≈ 0.407 × 0.798 × factor ≈ 0.322。 RSFT CED s43 rel_recall=0.456 → joint ≈ 0.456 × 0.816 × factor ≈ 0.381。 GRPO rel_recall=0.014 → joint ≈ 0.014 × 0.850 × factor ≈ 0.012——catastrophic， 因为即使 evidence quality 高，几乎没有正确 relation 来\"兑现\"这个高 evi_f1。 这个数字本身就是 decoupling phenomenon 的最直观体现。 Joint Evi-F1 的 CED vs SFT delta（+5.96pp）比 conditional delta（+1.77pp）大得多， 因为 joint 同时受益于 rel_f1 提升和 evi_f1 提升——RSFT+CED 的双重优势在 joint 指标下被放大。\n"
925	  }
926	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f861bb-b22e-4427-b41b-9c2e9a8eced3",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "cabf3693-0ab0-4a54-953f-0b89d37055cc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"CED vs flat-NLI RSFT ablation\",\n    \"description\": \"用 flat-NLI scoring（DeBERTa NLI entailment score，无 contrastive margin）替代 CED 作为 RSFT 候选筛选信号。 复用 mvp2_rsft_gen_s0~s3 已有的 21952 candidates，仅替换打分函数。 flat-NLI score = mean entailment probability over cited sentences（无 hard-negative 对比）。 选 top_k=1 per document，训练配置对齐 CED-RSFT 最优（s43: 3ep, α=128, seed=43；r2b: 1ep, α=32, lr=1e-5）。 共训练 2 个 flat-NLI RSFT 配置，全量 dev eval。\\n\",\n    \"results\": {\n      \"flatnli_rsft_a_rel_f1\": 0.4412,\n      \"flatnli_rsft_a_evi_f1\": 0.7948,\n      \"flatnli_rsft_a_edcr\": 0.6952,\n      \"flatnli_rsft_a_n_selected\": 2845,\n      \"flatnli_rsft_b_rel_f1\": 0.4378,\n      \"flatnli_rsft_b_evi_f1\": 0.7972,\n      \"flatnli_rsft_b_edcr\": 0.6887,\n      \"ced_rsft_best_rel_f1\": 0.4683,\n      \"ced_rsft_best_evi_f1\": 0.8156,\n      \"ced_rsft_best_edcr\": 0.6388,\n      \"delta_rel_f1\": 0.0271,\n      \"delta_evi_f1\": 0.0208,\n      \"delta_edcr\": -0.0564,\n      \"paired_bootstrap_evi_f1_p\": 0.0038,\n      \"paired_bootstrap_edcr_p\": 0.0021,\n      \"paired_bootstrap_rel_f1_p\": 0.0067\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED vs flat-NLI RSFT Ablation (dev set)\",\n        \"columns\": [\n          \"Method\",\n          \"rel_f1\",\n          \"evi_f1\",\n          \"EDCR\",\n          \"n_train\"\n        ],\n        \"rows\": [\n          [\n            \"SFT baseline\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"12151 (gold)\"\n          ],\n          [\n            \"RSFT flat-NLI (A: 3ep, α=128)\",\n            0.4412,\n            0.7948,\n            0.6952,\n            2845\n          ],\n          [\n            \"RSFT flat-NLI (B: 1ep, α=32)\",\n            0.4378,\n            0.7972,\n            0.6887,\n            2845\n          ],\n          [\n            \"RSFT CED (s43: 3ep, α=128)\",\n            0.4683,\n            0.8156,\n            0.6388,\n            2718\n          ],\n          [\n            \"RSFT CED (r2b: 1ep, α=32)\",\n            0.4493,\n            0.8128,\n            0.6609,\n            2718\n          ],\n          [\n            \"Δ (CED best - flatNLI best)\",\n            \"+2.71pp\",\n            \"+2.08pp\",\n            \"-5.64pp\",\n            \"—\"\n          ],\n          [\n            \"p-value (paired bootstrap)\",\n            0.0067,\n            0.0038,\n            0.0021,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED vs flat-NLI 的差异模式完美验证了核心假说：CED 的优势集中在 distractor-dense 文档上。 在 distractor density > 0.4 的文档子集中，CED RSFT 的 evi_f1 优势扩大到 ~3.5pp， 而在 distractor density < 0.2 的文档中差异缩小到 ~0.8pp（不显著）。 这证明 CED 的 contrastive margin 确实在做它该做的事：区分 entity-sharing distractors 和真正的 evidence。 EDCR 的差异更稳定（几乎所有子集都显著），因为 EDCR 直接测量 distractor citation rate， 而 evi_f1 还受 recall 影响（有些 gold evidence 即使用 flat-NLI 也能被正确引用）。 rel_f1 的差异虽然也显著，但这是 evidence 质量提升的 downstream 效应，而非 CED 的直接目标。\\n\\n\\nflat-NLI scoring 仍然能过滤掉完全无关的候选（如 format 错误、zero-F1 的），因此 flat-NLI RSFT 仍优于 SFT baseline（+3.2~3.6pp rel_f1）。 但 flat-NLI 的核心缺陷在于：entity-sharing distractor sentences 的 NLI entailment score 往往偏高（因为共享实体提供了 lexical overlap）， flat-NLI 无法区分\\\"真正支持关系的证据句\\\"和\\\"仅提及相同实体的干扰句\\\"。 因此 flat-NLI 筛选出的 top-1 候选中会保留更多 distractor-heavy 样本——这些样本的 evidence 看起来\\\"合理\\\"（高 NLI score） 但实际上引用了大量 entity-sharing non-gold sentences。 CED 的 contrastive margin = p(entail|gold) - max(p(entail|distractor)) 直接惩罚这种模式， 因此 CED-filtered 数据的训练样本 evidence 质量系统性更高。 这导致 CED RSFT 在 evi_f1 上高出 ~2.1pp（因为训练数据中 evidence 更精确，模型学到更好的 evidence 引用模式）， 在 EDCR 上低 5.6pp（因为训练数据中 distractor citations 更少，模型被条件化为避免引用干扰句）。 rel_f1 差异 +2.7pp 来自间接效应：CED 筛选出的候选不仅 evidence 更好，整体生成质量也更高（因为能正确定位 evidence 的生成通常也更准确地识别了关系）。 p<0.01 的显著性来自两个因素：(1) dev set 有 985 docs 提供足够统计力，(2) CED vs flat-NLI 的差异是系统性的（几乎在每种关系类型上 CED 都更好），不是少数异常值驱动的。 flat-NLI 选出 ~2845 样本（vs CED 2718），因为 flat-NLI 的筛选 landscape 不同（一些 CED 会拒绝的 distractor-heavy 候选在 flat-NLI 下得分高）。\\n\"\n  },\n  {\n    \"name\": \"Test set evaluation (RSFT best + SFT baseline)\",\n    \"description\": \"用 RSFT best config (s43_r2: 3ep, α=128, seed=43) 和 SFT baseline 在 DocRED test set 上评估。 (1) CodaLab 提交获取官方 rel_F1/Ign_F1；(2) 本地 test set 计算 Evi-F1_joint (DREEAM 协议) 和 Evi-F1_conditional + EDCR；(3) flat-NLI RSFT best 也提交作为 ablation。\\n\",\n    \"results\": {\n      \"sft_test_rel_f1\": 0.3998,\n      \"sft_test_ign_f1\": 0.3814,\n      \"sft_test_evi_f1_conditional\": 0.7902,\n      \"sft_test_evi_f1_joint\": 0.3216,\n      \"sft_test_edcr\": 0.7185,\n      \"rsft_test_rel_f1\": 0.4548,\n      \"rsft_test_ign_f1\": 0.4367,\n      \"rsft_test_evi_f1_conditional\": 0.8072,\n      \"rsft_test_evi_f1_joint\": 0.3758,\n      \"rsft_test_edcr\": 0.6476,\n      \"flatnli_test_rel_f1\": 0.4302,\n      \"flatnli_test_ign_f1\": 0.4118,\n      \"flatnli_test_evi_f1_conditional\": 0.7883,\n      \"flatnli_test_evi_f1_joint\": 0.3421,\n      \"flatnli_test_edcr\": 0.7014,\n      \"rsft_vs_sft_test_rel_f1_delta\": 0.055,\n      \"dev_to_test_degradation_rel_f1\": 0.0135,\n      \"rsft_test_evi_f1_joint_value\": 0.3758\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Test Set Main Results\",\n        \"columns\": [\n          \"Method\",\n          \"rel_F1\",\n          \"Ign_F1\",\n          \"Evi-F1_joint\",\n          \"Evi-F1_cond\",\n          \"EDCR\"\n        ],\n        \"rows\": [\n          [\n            \"SFT baseline\",\n            0.3998,\n            0.3814,\n            0.3216,\n            0.7902,\n            0.7185\n          ],\n          [\n            \"RSFT flat-NLI\",\n            0.4302,\n            0.4118,\n            0.3421,\n            0.7883,\n            0.7014\n          ],\n          [\n            \"RSFT CED (FREIGE)\",\n            0.4548,\n            0.4367,\n            0.3758,\n            0.8072,\n            0.6476\n          ],\n          [\n            \"DREEAM (RoBERTa-large)\",\n            \"—\",\n            \"—\",\n            0.5734,\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"SAIS (RoBERTa-large)\",\n            \"—\",\n            \"—\",\n            0.5567,\n            \"—\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Test set 结果验证了 Claim 1 的核心——RSFT+CED 在 test 上稳定保持 +5.5pp rel_f1 优势，dev→test 退化仅 1.35pp。 Evi-F1_joint 与 DREEAM 的绝对比较：FREIGE 0.376 vs DREEAM 0.573。 DREEAM 的 joint Evi-F1 更高，但 DREEAM 是 encoder-based 方法，其\\\"evidence\\\"是 attention weight thresholding， 而 FREIGE 是生成式方法同时输出 triple+evidence——二者的 evidence 形式不同（implicit attention vs explicit citation）。 论文可这样叙述：FREIGE 是首个生成式方法在 DocRED 上输出显式 evidence，且其 joint Evi-F1 在 LLM 方法中无可比对手（LMRC、DocKS-RAG 均不输出 evidence）。 flat-NLI RSFT 在 test 上的表现确认了 CED 优势的泛化性（delta 方向一致）。\\n\\n\\nDev→test degradation 约 1.35pp rel_f1（0.4683 → 0.4548），这在 DocRED 上属正常范围。 DocRED test set 的关系分布与 dev 非常接近（同一标注 pipeline），但 test 略难因为： (1) annotator 间一致性略低的 hard cases 更多被分配到 test，(2) distant supervision noise 在 test 中比例略高。 SFT test rel_f1=0.3998 比 dev 0.4057 低 0.6pp，同样符合 DocRED 的典型 dev-test gap。 因此 RSFT vs SFT 的 delta 在 test 上为 +5.5pp（vs dev +6.26pp），退化幅度合理。 Evi-F1_joint (DREEAM 协议) 远低于 conditional（0.376 vs 0.807），因为 joint 计算方式为 evi_f1 = Σ(triple_correct AND evi_correct) / Σ(gold_triples)，未正确预测的 triple 直接贡献 0 到 evidence score。 RSFT rel_f1=0.455 意味着约 45.5% 的 gold triples 被正确预测；在这些正确预测中，evi_f1_conditional ≈ 0.807； 因此 joint ≈ 0.455 × 0.807 × correction_factor ≈ 0.376（correction factor 因为 recall/precision 不对称略偏离乘积）。 SFT 的 joint 更低（0.322）因为 rel_f1 更低（0.400）。 Ign_F1 低于 F1 约 1.8pp，因为 RSFT 和 SFT 都对 shared entity pairs（train+dev 中出现的）有略高的准确率， 忽略这些后 F1 下降——这是 DocRED 评测的正常模式。 EDCR 在 test 上略高于 dev（0.648 vs 0.639），因为 test set 文档平均 entity density 略高，distractor 机会更多。\\n\"\n  },\n  {\n    \"name\": \"EDCR pipeline 验证 + cross-method diagnostic table\",\n    \"description\": \"在所有 evidence-producing 方法上计算统一的 EDCR 指标，构建 cross-method diagnostic table。 方法包括：SFT, RSFT-CED (4 configs), RSFT-flatNLI (2 configs), CED-reranker, GRPO checkpoints (selected)。 同时计算 EDCR 与 evi_f1 的相关性（per-method level 和 per-document level）。\\n\",\n    \"results\": {\n      \"sft_edcr\": 0.7118,\n      \"rsft_ced_s43_edcr\": 0.6388,\n      \"rsft_ced_s44_edcr\": 0.635,\n      \"rsft_ced_r2a_edcr\": 0.6641,\n      \"rsft_ced_r2b_edcr\": 0.6609,\n      \"rsft_flatnli_a_edcr\": 0.6952,\n      \"rsft_flatnli_b_edcr\": 0.6887,\n      \"ced_reranker_edcr\": 0.5983,\n      \"grpo_ckpt90_edcr\": 0.8584,\n      \"grpo_ckpt100_lr5e6_edcr\": 0.9876,\n      \"cross_method_pearson_r_edcr_vs_evif1\": -0.42,\n      \"per_doc_spearman_edcr_vs_evif1\": -0.31\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-Method EDCR Diagnostic\",\n        \"columns\": [\n          \"Method\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\",\n          \"n_cited_sent\",\n          \"n_distractor\"\n        ],\n        \"rows\": [\n          [\n            \"GRPO ckpt-100 (lr=5e-6)\",\n            0.0138,\n            0.8504,\n            0.9876,\n            12834,\n            12675\n          ],\n          [\n            \"GRPO ckpt-90 (lr=5e-5)\",\n            0.2108,\n            0.5666,\n            0.8584,\n            9821,\n            8431\n          ],\n          [\n            \"SFT baseline\",\n            0.4057,\n            0.7979,\n            0.7118,\n            14206,\n            10113\n          ],\n          [\n            \"RSFT flat-NLI (best)\",\n            0.4412,\n            0.7972,\n            0.6887,\n            13875,\n            9556\n          ],\n          [\n            \"RSFT CED r2b\",\n            0.4493,\n            0.8128,\n            0.6609,\n            13542,\n            8950\n          ],\n          [\n            \"RSFT CED s43\",\n            0.4683,\n            0.8156,\n            0.6388,\n            13267,\n            8475\n          ],\n          [\n            \"CED-reranker\",\n            0.4152,\n            0.8214,\n            0.5983,\n            12983,\n            7768\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"EDCR diagnostic table 的核心发现：GRPO ckpt-100 的 EDCR=0.99 + Evi-F1=0.85 是一个极端案例—— 模型输出了大量 citations 且其中 evidence recall 高（0.787），但 99% 的 cited sentences 是 distractor。 这是因为 GRPO 崩塌后模型倾向于引用文档中几乎所有句子，recall 自然高但 precision 极低。 CED-reranker 的 EDCR=0.60 是最低的，因为推理时 CED 直接选择 margin 最大的候选—— 但其 rel_f1=0.415 不如 RSFT CED s43=0.468，因为 reranking 不改变 candidate pool 的质量上限。 这支持了\\\"CED 最适合作为训练数据筛选信号而非纯推理 reranker\\\"的结论。\\n\\n\\nCross-method table 展现清晰的 EDCR 梯度：GRPO（0.86-0.99）>> SFT（0.71）>> RSFT-flatNLI（0.69）>> RSFT-CED（0.64）>> CED-reranker（0.60）。 这个梯度与直觉一致：(1) GRPO 的 catastrophic forgetting 导致模型生成大量重复 entity mentions 但极少正确 relation， 几乎所有 cited sentences 都是 distractor；(2) SFT 从 gold data 学习但无 evidence quality 信号； (3) flat-NLI RSFT 比 SFT 好因为至少过滤了 zero-evidence 候选，但 flat-NLI 被 entity overlap 欺骗； (4) CED RSFT 进一步降低因为 contrastive margin 训练数据中 distractor 更少； (5) CED-reranker 最低因为推理时直接按 CED 选最佳候选，不受训练数据分布约束。 Cross-method Pearson r ≈ -0.42 表明 EDCR 与 evi_f1 有中等负相关但远非完美—— 这正是 EDCR 作为独立指标的价值：它捕获了 evi_f1 的盲区（plausible-looking distractor citations）。 Per-document Spearman 较低（-0.31）因为 EDCR 在单文档粒度上噪声较大（小 denominator 问题）。\\n\"\n  },\n  {\n    \"name\": \"DREEAM baseline reproduction\",\n    \"description\": \"在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 evidence extraction 结果。 使用官方代码和预训练权重，计算 joint Evi-F1（与 FREIGE 可直接对比）。\\n\",\n    \"results\": {\n      \"dreeam_dev_evi_f1_joint\": 0.5718,\n      \"dreeam_dev_evi_f1_conditional\": 0.8342,\n      \"dreeam_dev_rel_f1\": 0.6312,\n      \"dreeam_paper_evi_f1\": 0.5734,\n      \"reproduction_gap\": -0.0016,\n      \"sais_dev_evi_f1_joint\": 0.5542\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Evidence Baseline Comparison (dev set)\",\n        \"columns\": [\n          \"Method\",\n          \"Type\",\n          \"rel_F1\",\n          \"Evi-F1_joint\",\n          \"Evidence Form\"\n        ],\n        \"rows\": [\n          [\n            \"DREEAM\",\n            \"Encoder\",\n            0.6312,\n            0.5718,\n            \"Attention threshold\"\n          ],\n          [\n            \"SAIS\",\n            \"Encoder\",\n            0.6103,\n            0.5542,\n            \"Attention threshold\"\n          ],\n          [\n            \"FREIGE (RSFT CED)\",\n            \"Generative LLM\",\n            0.4683,\n            0.3758,\n            \"Explicit [S_i] citation\"\n          ],\n          [\n            \"SFT baseline\",\n            \"Generative LLM\",\n            0.4057,\n            0.3216,\n            \"Explicit [S_i] citation\"\n          ],\n          [\n            \"LMRC\",\n            \"Generative LLM\",\n            0.6069,\n            \"—\",\n            \"No evidence\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DREEAM/SAIS 复现确认了数字可靠。FREIGE 在 joint Evi-F1 上低于 DREEAM（0.376 vs 0.572）， 这主要由 rel_f1 gap 驱动（0.468 vs 0.631）。论文需要清晰叙述： (1) FREIGE 是首个输出显式 evidence 的 generative LLM DocRE 方法； (2) 在 LLM 方法类别内无直接竞争者（LMRC 无 evidence）； (3) 与 encoder methods 的 gap 主要来自 extraction 能力而非 evidence 能力——\\n    在正确预测的 triple 上，FREIGE 的 conditional Evi-F1 (0.807) 接近 DREEAM 的 (0.834)。\\n\\n\\nDREEAM 论文报告 Evi-F1 = 57.34，这是 joint protocol（evidence score 仅在 relation 也正确时计入）。 复现应在 ±0.3pp 内——DREEAM 是确定性 encoder 方法（无采样），差异仅来自 PyTorch 版本和随机种子对 fine-tuning 的微小影响。 使用官方 released checkpoint 应几乎完全复现。 DREEAM 的 rel_f1 ≈ 63.1%（RoBERTa-large encoder 的典型 DocRED 表现），远高于 FREIGE 的 46.8%—— 但 FREIGE 的贡献不在于超越 encoder SOTA 的 extraction 精度，而在于首次提供显式 evidence。 DREEAM 的 evidence 是 attention-based（隐式的），而 FREIGE 输出显式句子索引。 SAIS 复现 Evi-F1_joint ≈ 55.42，略低于 DREEAM，符合论文报告。\\n\"\n  },\n  {\n    \"name\": \"CED-as-reranker PoC\",\n    \"description\": \"推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。\\n\",\n    \"results\": {\n      \"reranker_rel_f1\": 0.4152,\n      \"reranker_evi_f1\": 0.8214,\n      \"reranker_edcr\": 0.5983,\n      \"reranker_evi_precision\": 0.8356,\n      \"reranker_evi_recall\": 0.8078,\n      \"sft_baseline_rel_f1\": 0.4057,\n      \"sft_baseline_evi_f1\": 0.7979,\n      \"sft_baseline_edcr\": 0.7118,\n      \"delta_rel_f1_vs_sft\": 0.0095,\n      \"delta_evi_f1_vs_sft\": 0.0235,\n      \"delta_edcr_vs_sft\": -0.1135\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED Usage Modes Comparison\",\n        \"columns\": [\n          \"CED Usage\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\",\n          \"Extra Training\"\n        ],\n        \"rows\": [\n          [\n            \"SFT (no CED)\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"—\"\n          ],\n          [\n            \"CED-reranker (inference)\",\n            0.4152,\n            0.8214,\n            0.5983,\n            \"None\"\n          ],\n          [\n            \"RSFT flat-NLI (training, no CED)\",\n            0.4412,\n            0.7972,\n            0.6887,\n            \"RSFT\"\n          ],\n          [\n            \"RSFT CED (training)\",\n            0.4683,\n            0.8156,\n            0.6388,\n            \"RSFT\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED-reranker 证明了 CED 作为质量信号的有效性（EDCR 大幅下降 -11.35pp）， 但也证明了仅靠推理时 reranking 不够——rel_f1 提升微弱。 这形成一个很好的 ablation 故事：CED 信号本身有效，但需要通过 RSFT 训练来充分利用。 论文可在 analysis section 用此对比说明\\\"为什么选择 RSFT 而非 reranking\\\"。\\n\\n\\nCED-reranker 在 EDCR 上表现最好（0.598），因为推理时直接选 CED margin 最大的候选—— 这等价于选 distractor citation 最少的那个生成。evi_f1 也因此改善（+2.35pp）， 因为更准确的 evidence 引用提升了 precision。 但 rel_f1 提升有限（+0.95pp），原因是 CED 的打分维度是 evidence quality 而非 extraction accuracy。 N=8 候选的 extraction diversity 有限（Jaccard 在 temp=0.7 下约 0.17）， 重排仅在候选间有 evidence 质量差异时有用，对 extraction 错误无能为力。 与 RSFT CED (rel_f1=0.468) 的差距（-5.3pp）证明了训练 vs 推理的区别： RSFT 通过高质量数据改变了模型的 generation distribution，而 reranker 仅从已有分布中选最佳。 这支持论文的\\\"CED 作为训练信号优于推理信号\\\"结论。\\n\"\n  },\n  {\n    \"name\": \"Model size ablation (1.7B / 8B)\",\n    \"description\": \"在 Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT+CED pipeline，验证方法对模型规模的泛化性。 每个模型：SFT baseline + RSFT CED (best config from 4B)，dev set 评估。\\n\",\n    \"results\": {\n      \"qwen_1_7b_sft_rel_f1\": 0.3412,\n      \"qwen_1_7b_sft_evi_f1\": 0.7534,\n      \"qwen_1_7b_sft_edcr\": 0.7456,\n      \"qwen_1_7b_rsft_ced_rel_f1\": 0.3724,\n      \"qwen_1_7b_rsft_ced_evi_f1\": 0.7782,\n      \"qwen_1_7b_rsft_ced_edcr\": 0.6934,\n      \"qwen_1_7b_delta_rel_f1\": 0.0312,\n      \"qwen_8b_sft_rel_f1\": 0.4423,\n      \"qwen_8b_sft_evi_f1\": 0.8125,\n      \"qwen_8b_sft_edcr\": 0.6892,\n      \"qwen_8b_rsft_ced_rel_f1\": 0.4912,\n      \"qwen_8b_rsft_ced_evi_f1\": 0.8367,\n      \"qwen_8b_rsft_ced_edcr\": 0.6187,\n      \"qwen_8b_delta_rel_f1\": 0.0489\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Model Size Ablation\",\n        \"columns\": [\n          \"Model\",\n          \"Method\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\",\n          \"Δ rel_F1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-1.7B\",\n            \"SFT\",\n            0.3412,\n            0.7534,\n            0.7456,\n            \"—\"\n          ],\n          [\n            \"Qwen3-1.7B\",\n            \"RSFT+CED\",\n            0.3724,\n            0.7782,\n            0.6934,\n            \"+3.12pp\"\n          ],\n          [\n            \"Qwen3-4B\",\n            \"SFT\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"—\"\n          ],\n          [\n            \"Qwen3-4B\",\n            \"RSFT+CED\",\n            0.4683,\n            0.8156,\n            0.6388,\n            \"+6.26pp\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"SFT\",\n            0.4423,\n            0.8125,\n            0.6892,\n            \"—\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"RSFT+CED\",\n            0.4912,\n            0.8367,\n            0.6187,\n            \"+4.89pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Model size ablation 证明 RSFT+CED 在 1.7B-8B 范围内一致有效。 4B 的相对提升最大可能因为它处于\\\"sweet spot\\\"——模型足够大产生多样高质量候选， 但还不够大到 SFT 已经很好。8B SFT 的 EDCR 已经较低（0.689），说明更大模型本身就更善于引用相关 evidence， 但 RSFT+CED 仍有增量价值。\\n\\n\\n1.7B 模型基础能力更弱（SFT rel_f1 0.341 vs 4B 的 0.406），但 RSFT+CED 的相对提升仍然显著（+3.1pp）。 提升幅度略小于 4B（+6.3pp），因为 1.7B 的 candidate pool 质量上限更低—— N=8 生成中 top-1 CED candidate 的质量受限于模型的 generation capacity。 8B 模型基础更强（SFT 0.442），RSFT+CED 提升到 0.491（+4.9pp）， 提升幅度介于 1.7B 和 4B 之间。8B 的 SFT baseline 已经较高，留给 RSFT 的 headroom 相对更小， 但绝对性能最好。 跨三个规模的一致提升（+3.1 / +6.3 / +4.9pp）证明 CED+RSFT 不是模型特定的 trick， 而是一个通用的 evidence quality 提升机制。 EDCR 模式一致：1.7B SFT EDCR 最高（0.746）因为小模型更易引用不相关句子， RSFT+CED 在所有规模上都降低 EDCR（-5.2 / -7.3 / -7.1pp）。\\n\"\n  },\n  {\n    \"name\": \"Re-DocRED extension\",\n    \"description\": \"在 Re-DocRED（修正 false negative 标注的版本）上评估 SFT 和 RSFT+CED，验证方法在更干净标注下的表现。\\n\",\n    \"results\": {\n      \"redocred_sft_rel_f1\": 0.4534,\n      \"redocred_sft_evi_f1\": 0.8112,\n      \"redocred_rsft_ced_rel_f1\": 0.5089,\n      \"redocred_rsft_ced_evi_f1\": 0.8378,\n      \"redocred_rsft_ced_edcr\": 0.6023,\n      \"redocred_delta_rel_f1\": 0.0555\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DocRED vs Re-DocRED\",\n        \"columns\": [\n          \"Dataset\",\n          \"Method\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            \"DocRED\",\n            \"SFT\",\n            0.4057,\n            0.7979,\n            0.7118\n          ],\n          [\n            \"DocRED\",\n            \"RSFT+CED\",\n            0.4683,\n            0.8156,\n            0.6388\n          ],\n          [\n            \"Re-DocRED\",\n            \"SFT\",\n            0.4534,\n            0.8112,\n            0.6892\n          ],\n          [\n            \"Re-DocRED\",\n            \"RSFT+CED\",\n            0.5089,\n            0.8378,\n            0.6023\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Re-DocRED 结果为 RC4（单数据集泛化性）提供了部分回应。方法在更干净标注下表现更好且 delta 保持， 说明 CED+RSFT 不是在利用标注噪声。\\n\\n\\nRe-DocRED 修正了 DocRED 中约 25% 的 false negative relations（标注遗漏）， 因此所有方法的绝对 F1 都上升（SFT 0.453 vs 原 0.406）——被原始标注遗漏的正确预测不再被惩罚。 RSFT+CED 的 delta（+5.55pp）与 DocRED 上的（+6.26pp）接近， 说明 CED 的 evidence quality 提升不依赖于标注噪声的存在。 EDCR 在 Re-DocRED 上略低（0.602 vs 0.639），因为部分被标为 distractor 的句子在 Re-DocRED 中被重新标注为 gold evidence， 降低了 false-distractor 率。这也间接验证了 CED margin 的鲁棒性—— 即使标注不完美，CED 仍然能有效区分 evidence 质量。\\n\"\n  },\n  {\n    \"name\": \"top_k ablation (k=1 vs k=3)\",\n    \"description\": \"CED scoring 筛选 top_k=3（每文档选 CED top-3 候选，~8000 训练样本）vs top_k=1（~2718 样本）， 验证 CED 过滤严格度对 RSFT 训练质量的影响。\\n\",\n    \"results\": {\n      \"topk1_n_samples\": 2718,\n      \"topk1_rel_f1\": 0.4683,\n      \"topk1_evi_f1\": 0.8156,\n      \"topk1_edcr\": 0.6388,\n      \"topk3_n_samples\": 7856,\n      \"topk3_rel_f1\": 0.4523,\n      \"topk3_evi_f1\": 0.8034,\n      \"topk3_edcr\": 0.6712,\n      \"topk3_mean_ced_score\": 0.5234\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: top_k Ablation\",\n        \"columns\": [\n          \"top_k\",\n          \"n_train\",\n          \"mean_CED\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\"\n        ],\n        \"rows\": [\n          [\n            1,\n            2718,\n            0.6683,\n            0.4683,\n            0.8156,\n            0.6388\n          ],\n          [\n            3,\n            7856,\n            0.5234,\n            0.4523,\n            0.8034,\n            0.6712\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"top_k ablation 确认了 CED 质量过滤的重要性，同时也为 reviewer 提供了\\\"为什么不用更多数据\\\"的回答。 这是一个 diminishing-returns-with-quality-dilution 的经典案例。\\n\\n\\ntop_k=3 引入了 ~5100 额外训练样本，但这些是每文档的第 2、3 名候选——CED score 系统性更低 （mean CED 0.523 vs top_k=1 的 0.668）。更多训练数据带来的拟合优势被更低数据质量抵消： (1) rel_f1 下降 1.6pp 因为质量较低的候选引入了更多 extraction 错误模式； (2) evi_f1 下降 1.2pp 因为 2nd/3rd 候选的 evidence 质量明显低于 1st； (3) EDCR 上升 3.2pp 因为训练数据中混入了更多 distractor-heavy 样本。 这验证了 CED 作为质量过滤器的\\\"宁缺毋滥\\\"策略——strict top_k=1 优于宽松 top_k=3， 因为 RSFT 的核心机制是让模型从高质量样本中学习，不需要海量数据。 这也解释了为什么 2718 样本（仅占 21952 候选的 12.4%）就足够有效—— SFT 阶段已经提供了足够的\\\"通用知识\\\"，RSFT 只需少量高质量样本来校准 evidence 引用行为。\\n\"\n  },\n  {\n    \"name\": \"GRPO G=8 实验\",\n    \"description\": \"G=8 + CED reward + kl_coef=0.01 + lr=5e-6，验证 GRPO 在标准 group size 下是否仍然 catastrophic forgetting。 排除 G=4 的 advantage estimation noise 作为 confounding factor。\\n\",\n    \"results\": {\n      \"grpo_g8_best_rel_f1\": 0.0312,\n      \"grpo_g8_best_evi_f1\": 0.8156,\n      \"grpo_g8_best_edcr\": 0.9812,\n      \"grpo_g8_best_checkpoint\": \"ckpt-80\",\n      \"grpo_g8_final_rel_f1\": 0.0287,\n      \"grpo_g8_final_reward\": 1.287,\n      \"grpo_g8_forgetting_onset_step\": 15,\n      \"grpo_g8_collapse_pattern\": \"同 G=4：reward ↑ + rel_f1 ↓，但 collapse 稍慢\",\n      \"grpo_g4_best_rel_f1\": 0.0138,\n      \"grpo_g4_best_evi_f1\": 0.8504\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GRPO Group Size Comparison\",\n        \"columns\": [\n          \"Config\",\n          \"G\",\n          \"Best rel_F1\",\n          \"Best Evi-F1\",\n          \"EDCR\",\n          \"Forgetting?\"\n        ],\n        \"rows\": [\n          [\n            \"GRPO+CED lr=5e-6\",\n            4,\n            0.0138,\n            0.8504,\n            0.9876,\n            \"Yes (step ~10)\"\n          ],\n          [\n            \"GRPO+CED lr=5e-6\",\n            8,\n            0.0312,\n            0.8156,\n            0.9812,\n            \"Yes (step ~15)\"\n          ],\n          [\n            \"GRPO+CED lr=5e-5\",\n            4,\n            0.2108,\n            0.5666,\n            0.8584,\n            \"Yes (partial)\"\n          ],\n          [\n            \"SFT baseline\",\n            \"—\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"G=8 实验是 Claim 3 的关键验证——排除了 advantage estimation noise 作为 G=4 failure 的替代解释。 rel_f1 从 0.014 微升到 0.031 说明 G 确实有微弱影响，但量级上不改变结论。 论文可以写：\\\"Increasing group size from 4 to 8 marginally delays but does not prevent catastrophic forgetting (best rel_F1: 0.031 vs 0.014, both << SFT 0.406), confirming the structural incompatibility of GRPO+QLoRA with document-level IE.\\\"\\n\\n\\nG=8 将 advantage estimation 的方差降低约 √2 倍（相对 G=4），这确实改善了 gradient quality。 然而 catastrophic forgetting 的根因不是 advantage noise，而是 GRPO+QLoRA 在文档级 IE 任务上的结构性问题： (1) QLoRA 的 rank-limited 参数空间在接收 RL gradient 时容易覆盖 SFT 学到的 extraction schema knowledge； (2) CED/NLI reward 在 evidence 维度上的梯度远强于 extraction 维度（因为 evidence quality 变化更容易被 reward 捕获），\\n    导致模型优先优化 evidence 而放弃 extraction；\\n(3) 文档级 IE 的输出空间极大（多 triple + evidence），policy gradient 的 credit assignment 困难。 G=8 的 rel_f1 峰值（0.031）略高于 G=4（0.014），说明更稳定的 advantage 确实有边际帮助， 但远不足以避免 forgetting（仍 < 0.05，远低于 SFT 的 0.406）。 evi_f1 仍然高（0.816），再次确认 decoupling phenomenon——RL 优化了 evidence 但摧毁了 extraction。 Forgetting onset 稍慢（step 15 vs G=4 的 step ~10），因为 G=8 的 gradient 更保守， 但最终 trajectory 殊途同归。\\n\"\n  },\n  {\n    \"name\": \"DPO+CED experiment\",\n    \"description\": \"用 RSFT candidate pool 构造 preference pairs：每文档 CED top-1 为 chosen，CED bottom-1（F1>0.1 filter）为 rejected。 DPO 训练（β=0.1, lr=1e-5, 1 epoch），验证 offline preference learning 的表现。\\n\",\n    \"results\": {\n      \"dpo_rel_f1\": 0.3245,\n      \"dpo_evi_f1\": 0.7856,\n      \"dpo_edcr\": 0.6834,\n      \"dpo_n_pairs\": 2412,\n      \"dpo_beta\": 0.1,\n      \"sft_rel_f1\": 0.4057,\n      \"rsft_ced_rel_f1\": 0.4683,\n      \"grpo_g8_best_rel_f1\": 0.0312\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Online-Offline RL Spectrum\",\n        \"columns\": [\n          \"Method\",\n          \"RL Type\",\n          \"rel_F1\",\n          \"Evi-F1\",\n          \"EDCR↓\",\n          \"Catastrophic?\"\n        ],\n        \"rows\": [\n          [\n            \"GRPO G=8\",\n            \"Online (on-policy)\",\n            0.0312,\n            0.8156,\n            0.9812,\n            \"Yes\"\n          ],\n          [\n            \"GRPO G=4\",\n            \"Online (on-policy)\",\n            0.0138,\n            0.8504,\n            0.9876,\n            \"Yes\"\n          ],\n          [\n            \"DPO+CED\",\n            \"Offline (preference)\",\n            0.3245,\n            0.7856,\n            0.6834,\n            \"No (but degraded)\"\n          ],\n          [\n            \"SFT\",\n            \"No RL\",\n            0.4057,\n            0.7979,\n            0.7118,\n            \"No\"\n          ],\n          [\n            \"RSFT+CED\",\n            \"Offline (filtered SFT)\",\n            0.4683,\n            0.8156,\n            0.6388,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DPO 实验填补了 GRPO 和 RSFT 之间的空白。核心洞察： (1) 问题不在 \\\"offline vs online\\\" 的二元对立——DPO（offline）也退化了； (2) 问题在于 RL loss function 对文档级 IE 输出空间的适配性——\\n    GRPO 的 policy gradient 和 DPO 的 preference loss 都在 token level 操作，\\n    对长结构化输出的 credit assignment 困难；\\n(3) RSFT 之所以成功，是因为它根本不用 RL loss——直接 supervised learning on filtered data，\\n    避免了 credit assignment 问题。\\n这加强了论文的理论贡献：不是\\\"CED reward 好\\\"而是\\\"CED 作为数据质量信号 + SFT 训练范式 = 最佳组合\\\"。\\n\\n\\nDPO 作为 offline preference optimization，避免了 GRPO 的 on-policy sampling 导致的 distribution shift， 因此不会 catastrophic forgetting——rel_f1=0.325 远高于 GRPO 的 0.031。 但 DPO 弱于 RSFT（0.325 vs 0.468）的原因是： (1) DPO 的 implicit reward model 需要从 preference pairs 中学习 CED 信号，\\n    而 RSFT 直接在 CED-selected 高质量样本上 supervised learning——后者更 sample-efficient；\\n(2) DPO 的 contrastive loss 同时推高 chosen 和推低 rejected 的 likelihood，\\n    但在 IE 任务中 chosen/rejected 的差异主要在 evidence 而非 extraction——\\n    推低 rejected 可能意外降低了正确 extraction pattern 的概率；\\n(3) DocRED 的输出空间太大（长 JSON），DPO 的 token-level KL penalty 对长序列的控制力不足。 DPO 的 evi_f1（0.786）接近 SFT（0.798），说明 evidence 质量未被显著改善—— DPO 未能从 preference pairs 中有效学到 CED 的 evidence quality 信号。 这与 RSFT 的 evi_f1=0.816 形成对比，进一步支持\\\"CED 适合作为筛选信号而非学习目标\\\"。 rel_f1=0.325 vs SFT=0.406 实际上是 DPO 的退化（-8.1pp），这是因为 DPO 的 rejected 样本中包含的 extraction pattern 被不当抑制了——一种轻度的 DPO \\\"over-optimization\\\"。 整体光谱：GRPO (0.031) << DPO (0.325) < SFT (0.406) < RSFT (0.468)， 清晰展示了 online → offline → no-RL → offline-filtered 的退化/改善梯度。\\n\"\n  },\n  {\n    \"name\": \"EDCR 人工标注验证\",\n    \"description\": \"100 个样本（每样本 = 一个 predicted triple + 其 cited evidence sentences）， 3 名标注者独立判断每个 cited sentence 是否真正支持对应 relation。 计算 EDCR_auto 与 human_distractor_rate 的 Pearson r。\\n\",\n    \"results\": {\n      \"n_samples\": 100,\n      \"n_annotators\": 3,\n      \"inter_annotator_kappa\": 0.72,\n      \"edcr_human_pearson_r\": 0.62,\n      \"edcr_human_spearman_r\": 0.58,\n      \"human_distractor_rate_mean\": 0.583,\n      \"auto_edcr_mean\": 0.651,\n      \"edcr_auto_vs_human_bias\": 0.068,\n      \"sft_human_distractor_rate\": 0.645,\n      \"rsft_ced_human_distractor_rate\": 0.524,\n      \"rsft_flatnli_human_distractor_rate\": 0.608,\n      \"grpo_human_distractor_rate\": 0.954\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: EDCR Human Validation\",\n        \"columns\": [\n          \"Method\",\n          \"EDCR_auto\",\n          \"Human_distractor_rate\",\n          \"Δ\",\n          \"n\"\n        ],\n        \"rows\": [\n          [\n            \"GRPO ckpt-90\",\n            0.858,\n            0.954,\n            -0.096,\n            25\n          ],\n          [\n            \"SFT\",\n            0.712,\n            0.645,\n            0.067,\n            25\n          ],\n          [\n            \"RSFT flat-NLI\",\n            0.695,\n            0.608,\n            0.087,\n            25\n          ],\n          [\n            \"RSFT CED\",\n            0.639,\n            0.524,\n            0.115,\n            25\n          ],\n          [\n            \"Overall Pearson r\",\n            \"—\",\n            \"—\",\n            0.62,\n            100\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pearson r=0.62 满足 best tier 要求（[0.55, 0.75]），验证了 EDCR 作为自动指标的有效性。 但需要在论文中诚实讨论 limitations：(1) entity-sharing 是 distractor 的代理指标而非完美定义； (2) CED RSFT 的 auto-human gap 最大（0.115），说明 CED 训练的模型引用模式与人类直觉有微妙差异—— 部分人类认为有用的 contextual sentences（虽然不是 gold evidence）被 EDCR 标为 distractor。 这实际上是一个有趣的发现，可以在 discussion 中展开。\\n\\n\\nPearson r=0.62 表明 EDCR 与人类判断有中等偏强的正相关——EDCR 确实在测量有意义的 evidence 质量维度。 r 未达到 0.8+ 的原因：(1) EDCR 用 entity-sharing 作为 distractor 的操作性定义， 而人类判断基于语义支持关系——部分 entity-sharing sentences 人类认为确实支持关系（partial evidence）， 部分 non-entity-sharing sentences 人类认为是 distractor（基于语义而非 entity overlap）； (2) 100 样本的统计力有限，置信区间较宽。 Auto EDCR 略高估（bias +6.8pp），因为 entity-sharing 的自动判定过于严格—— 一些共享实体但确实提供支持的句子被 EDCR 错误标为 distractor。 Inter-annotator Cohen's κ=0.72（substantial agreement），说明 evidence 支持判断本身具有一定主观性， 但三人投票足以产生可靠的 gold standard。 分方法看，human distractor rate 的排序与 EDCR 一致：GRPO (0.954) >> SFT (0.645) > flatNLI (0.608) > CED (0.524)， 进一步验证了 EDCR 的诊断方向正确。\\n\"\n  },\n  {\n    \"name\": \"GRPO forgetting 详细分析 + 可视化\",\n    \"description\": \"整理全部 GRPO checkpoint（G=4 lr=5e-5, G=4 lr=5e-6, G=8）的完整训练轨迹， 绘制 forgetting dynamics 可视化。\\n\",\n    \"results\": {\n      \"n_checkpoints_analyzed\": 42,\n      \"n_configs\": 3,\n      \"decoupling_onset_step_g4_lr5e6\": 10,\n      \"decoupling_onset_step_g4_lr5e5\": 5,\n      \"decoupling_onset_step_g8\": 15,\n      \"peak_evi_f1_across_configs\": 0.8504,\n      \"min_rel_f1_across_configs\": 0.0028\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"可视化清晰展示 decoupling phenomenon 的三个阶段。Phase diagram 是最有力的图—— 所有 GRPO configs 的 trajectory 都从 (SFT rel_f1, SFT evi_f1) 出发，向 (↓, ↑) 移动， 形成一个\\\"左上角 attractor\\\"。RSFT 的 trajectory 则从同一起点向 (↑, ↑) 移动， 两个方向的对比直观地说明了 online vs offline RL 的行为差异。\\n\\n\\nGRPO 的 forgetting dynamics 在所有配置中呈现一致模式： (1) 早期（step 1-5/10/15 取决于 lr 和 G）：rel_f1 开始下降但 evi_f1 开始上升——decoupling onset； (2) 中期（step 5-50）：reward 持续上升，rel_f1 加速下降至 <0.05，evi_f1 平台期 ~0.80-0.85； (3) 后期（step 50-100）：reward 饱和，rel_f1 在底部震荡（<0.02），evi_f1 微调。 lr=5e-5 的 forgetting 最快（step 5 开始）但 rel_f1 最终峰值最高（0.211 at ckpt-90）， 因为高 lr 的 RL gradient 足够强同时推动 extraction 和 evidence，但最终 evidence gradient 占优。 lr=5e-6 的 forgetting 最慢开始但最终 rel_f1 最低（0.014）， 因为低 lr 的 RL gradient 更精细地优化了 reward 但缺乏足够的 extraction signal。 G=8 在 step 15 开始 forgetting——比 G=4 lr=5e-6 的 step 10 晚， 符合\\\"更稳定 advantage estimation → 更保守 update\\\"的预期。\\n\"\n  },\n  {\n    \"name\": \"NLI model ablation (DeBERTa-base vs large)\",\n    \"description\": \"用 DeBERTa-v3-large 替代 DeBERTa-v3-base 作为 CED scorer，重新打分已有 candidates， 对比两个 NLI 模型对 CED scoring 质量的影响。\\n\",\n    \"results\": {\n      \"deberta_base_mean_ced\": 0.6683,\n      \"deberta_large_mean_ced\": 0.7012,\n      \"deberta_base_discrimination_acc\": 0.815,\n      \"deberta_large_discrimination_acc\": 0.847,\n      \"deberta_large_rsft_rel_f1\": 0.4721,\n      \"deberta_large_rsft_evi_f1\": 0.8189,\n      \"deberta_large_rsft_edcr\": 0.6312,\n      \"deberta_base_rsft_rel_f1\": 0.4683,\n      \"deberta_base_rsft_evi_f1\": 0.8156,\n      \"deberta_base_rsft_edcr\": 0.6388,\n      \"delta_rel_f1\": 0.0038,\n      \"delta_evi_f1\": 0.0033\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: NLI Model Ablation\",\n        \"columns\": [\n          \"NLI Model\",\n          \"Params\",\n          \"Disc. Acc\",\n          \"Mean CED\",\n          \"RSFT rel_F1\",\n          \"RSFT Evi-F1\"\n        ],\n        \"rows\": [\n          [\n            \"DeBERTa-v3-base\",\n            \"86M\",\n            0.815,\n            0.668,\n            0.4683,\n            0.8156\n          ],\n          [\n            \"DeBERTa-v3-large\",\n            \"304M\",\n            0.847,\n            0.701,\n            0.4721,\n            0.8189\n          ],\n          [\n            \"Δ\",\n            \"—\",\n            \"+0.032\",\n            \"+0.033\",\n            \"+0.38pp\",\n            \"+0.33pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"NLI model ablation 的 marginal 差异是好消息——方法鲁棒、计算门槛低。 论文可以一句话带过：\\\"Replacing DeBERTa-base with DeBERTa-large yields marginal improvements (+0.38pp rel_F1), confirming that CED's effectiveness stems from the contrastive design rather than the NLI model's capacity.\\\"\\n\\n\\nDeBERTa-large 的 NLI 能力确实更强（discrimination accuracy 0.847 vs 0.815）， CED margin 也更大（0.701 vs 0.668），但这些改善传导到 RSFT 最终结果时被大幅衰减： (1) CED scoring 已经是一个\\\"阈值化\\\"操作（top_k=1），只要排序大致正确即可——\\n    base 和 large 的 top-1 选择一致率约 89%，仅 11% 文档的 top-1 不同；\\n(2) 这 11% 不同的文档中，large 选出的候选确实稍好，但对总体 RSFT 训练的影响被稀释； (3) rel_f1 差异仅 +0.38pp，不具统计显著性。 这是一个积极结果：CED 方法对 NLI 模型选择不敏感，base 模型足够用， 降低了方法的计算门槛（DeBERTa-base ~86M vs large ~304M参数）。 同时回应了 RC1（NLI reward 信号质量）：即使用更强的 NLI 模型，CED 提升也很小—— 说明 CED 的瓶颈不在 NLI 模型质量，而在于 RSFT 训练本身的 sample efficiency。\\n\"\n  },\n  {\n    \"name\": \"Evi-F1 DREEAM 协议对齐重评\",\n    \"description\": \"对所有已有 dev eval 结果重新计算 Evi-F1_joint（DREEAM 协议：evi score 仅在 relation 也正确时计入）。 已有的 Evi-F1 为 conditional（given correct relation），需要同时报告两种。\\n\",\n    \"results\": {\n      \"sft_evi_f1_joint\": 0.3216,\n      \"rsft_ced_s43_evi_f1_joint\": 0.3812,\n      \"rsft_ced_s44_evi_f1_joint\": 0.3724,\n      \"rsft_ced_r2a_evi_f1_joint\": 0.3657,\n      \"rsft_ced_r2b_evi_f1_joint\": 0.3663,\n      \"rsft_flatnli_best_evi_f1_joint\": 0.3498,\n      \"grpo_best_evi_f1_joint\": 0.0118,\n      \"ced_reranker_evi_f1_joint\": 0.3412\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Conditional vs Joint Evi-F1\",\n        \"columns\": [\n          \"Method\",\n          \"rel_F1\",\n          \"Evi-F1_cond\",\n          \"Evi-F1_joint\",\n          \"EDCR\"\n        ],\n        \"rows\": [\n          [\n            \"SFT\",\n            0.4057,\n            0.7979,\n            0.3216,\n            0.7118\n          ],\n          [\n            \"RSFT flat-NLI best\",\n            0.4412,\n            0.7972,\n            0.3498,\n            0.6887\n          ],\n          [\n            \"CED-reranker\",\n            0.4152,\n            0.8214,\n            0.3412,\n            0.5983\n          ],\n          [\n            \"RSFT CED s43\",\n            0.4683,\n            0.8156,\n            0.3812,\n            0.6388\n          ],\n          [\n            \"GRPO best (lr=5e-5)\",\n            0.2108,\n            0.5666,\n            0.1192,\n            0.8584\n          ],\n          [\n            \"GRPO best (lr=5e-6)\",\n            0.0138,\n            0.8504,\n            0.0118,\n            0.9876\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Joint Evi-F1 是论文主指标（与 DREEAM 可比），conditional 作为辅助指标。 Joint 指标下 GRPO 的灾难性表现（0.012）比 conditional（0.850）更直观地展示了 decoupling 的后果—— 模型学会了给好 evidence 但找不到正确 relation，导致 evidence 能力被浪费。 论文 main table 应以 joint 为主列，conditional 放 appendix。\\n\\nJoint Evi-F1 大幅低于 conditional，因为它对未正确预测的 relation triples 给 0 分。 公式近似为：joint ≈ Σ_{correct triples} evi_f1(triple) / |gold_triples|。 SFT rel_recall=0.407 → 约 40.7% gold triples 被正确预测 → joint ≈ 0.407 × 0.798 × factor ≈ 0.322。 RSFT CED s43 rel_recall=0.456 → joint ≈ 0.456 × 0.816 × factor ≈ 0.381。 GRPO rel_recall=0.014 → joint ≈ 0.014 × 0.850 × factor ≈ 0.012——catastrophic， 因为即使 evidence quality 高，几乎没有正确 relation 来\\\"兑现\\\"这个高 evi_f1。 这个数字本身就是 decoupling phenomenon 的最直观体现。 Joint Evi-F1 的 CED vs SFT delta（+5.96pp）比 conditional delta（+1.77pp）大得多， 因为 joint 同时受益于 rel_f1 提升和 evi_f1 提升——RSFT+CED 的双重优势在 joint 指标下被放大。\\n\"\n  }\n]",
      "numLines": 926,
      "startLine": 1,
      "totalLines": 926
    }
  },
  "sourceToolAssistantUUID": "f7f861bb-b22e-4427-b41b-9c2e9a8eced3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "cabf3693-0ab0-4a54-953f-0b89d37055cc",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ML research paper for dream session",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Assistant

_source line 14 · 2026-05-15T13:53:17.813Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of:
1. The experiment data (12 experiments with detailed results)
2. The paper framing (claims, story arc, reviewer concerns)

Let me write the full LaTeX paper. I need to:
- Cover all 12 experiments
- Follow the story arc: problem → naive reward fails → online RL fails → CED+RSFT solves it
- Include Abstract, Introduction, Method, Experiments, Conclusion
- Use only real numbers from experiment_data.json
- Target EMNLP 2026 format

Let me structure the paper:

1. Abstract


2. Introduction (problem, why naive fails, why online RL fails, our solution)
3. Related Work
4. Method (CED scoring, RSFT pipeline, EDCR metric)
5. Experiments
   - Setup
   - Main Results (Test set - Experiment 2)
   - CED vs flat-NLI ablation (Experiment 1)
   - EDCR diagnostic (Experiment 3)
   - DREEAM baseline comparison (Experiment 4)
   - CED usage modes (Experiment 5 - reranker)
   - Online-Offline RL spectrum (Experiment 8 - GRPO, Experiment 9 - DPO)
   - GRPO forgetting analysis (Experiment 10, Experiment 8)
   - Model size ablation (Experiment 6)
   - Re-DocRED (Experiment 7)
   - top_k ablation (Experiment 7)
   - NLI model ablation (Experiment 11)
   - EDCR human validation (Experiment 9)
   - Evi-F1 protocol (Experiment 12)
6. Analysis/Discussion
7. Conclusion

Now I'm organizing the tables for the paper using ACL/EMNLP formatting. I'll create a main results table from the test set, an ablation comparing CED against flat-NLI, a cross-method diagnostic for EDCR, a comparison of evidence baselines, a table showing different CED usage modes, and a final table examining the online-offline RL spectrum across different training approaches.

I'm realizing I have way too many individual tables planned out—one for each experiment variation. I need to consolidate these significantly by merging related ablations together, like combining the GRPO group size comparisons with DPO and other RL configurations into a single spectrum table, and grouping the DocRED variants and top_k ablations into unified results. Now I'm ready to start writing the paper itself, making sure to follow the ACL style guidelines for EMNLP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabf3693-0ab0-4a54-953f-0b89d37055cc",
  "isSidechain": false,
  "requestId": "req_011Cb4TxqCV9XdgWkSzbRyPu",
  "type": "assistant",
  "uuid": "04550a23-a426-4cc0-b1e6-5065613ea98d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zzeSRwndjrrjDjKkN6uLM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4924,
      "cache_creation_input_tokens": 20101,
      "cache_read_input_tokens": 23091,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4924,
          "output_tokens": 1163,
          "cache_read_input_tokens": 23091,
          "cache_creation_input_tokens": 20101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20101
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

_source line 15 · 2026-05-15T13:53:17.820Z_

Now I have all the data. Let me write the complete LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04550a23-a426-4cc0-b1e6-5065613ea98d",
  "isSidechain": false,
  "requestId": "req_011Cb4TxqCV9XdgWkSzbRyPu",
  "type": "assistant",
  "uuid": "fb9cb140-3554-45d5-8fcd-7671f8efd5a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zzeSRwndjrrjDjKkN6uLM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4924,
      "cache_creation_input_tokens": 20101,
      "cache_read_input_tokens": 23091,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4924,
          "output_tokens": 1163,
          "cache_read_input_tokens": 23091,
          "cache_creation_input_tokens": 20101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20101
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

_source line 16 · 2026-05-15T13:53:19.562Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014EV7xNDc5g6mUkyNChJKMJ`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9cb140-3554-45d5-8fcd-7671f8efd5a6",
  "isSidechain": false,
  "requestId": "req_011Cb4TxqCV9XdgWkSzbRyPu",
  "type": "assistant",
  "uuid": "86779bf3-cdbb-4941-883c-83e26abdf375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zzeSRwndjrrjDjKkN6uLM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4924,
      "cache_creation_input_tokens": 20101,
      "cache_read_input_tokens": 23091,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20101,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4924,
          "output_tokens": 1163,
          "cache_read_input_tokens": 23091,
          "cache_creation_input_tokens": 20101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20101
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

_source line 17 · 2026-05-15T13:53:19.782Z_

<details><summary>↩ Tool result · `toolu_014EV7xNDc5g6mUkyNChJKMJ`</summary>

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
  "parentUuid": "86779bf3-cdbb-4941-883c-83e26abdf375",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "8a6fd87c-0156-42cc-81e1-5dd0097da7fb",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "86779bf3-cdbb-4941-883c-83e26abdf375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T13:53:23.585Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TmsZggBm42ebKunYZxhGE1`</summary>

```json
{
  "command": "which pdflatex && kpsewhich acl.sty 2>/dev/null; kpsewhich acl_natbib.bst 2>/dev/null; ls /usr/share/texlive/texmf-dist/tex/latex/acl/ 2>/dev/null || echo \"NO_ACL_STY\"",
  "description": "Check LaTeX availability and ACL style"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a6fd87c-0156-42cc-81e1-5dd0097da7fb",
  "isSidechain": false,
  "requestId": "req_011Cb4TzZ89vNPN6Uym9Yohc",
  "type": "assistant",
  "uuid": "81c8d80d-9c63-48a1-bd52-bd339432d523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pZ43gKYfmG4KREroqBz3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6112,
      "cache_read_input_tokens": 43192,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 43192,
          "cache_creation_input_tokens": 6112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6112
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

_source line 19 · 2026-05-15T13:53:23.724Z_

<details><summary>↩ Tool result · `toolu_01TmsZggBm42ebKunYZxhGE1`</summary>

```text
/usr/bin/pdflatex
NO_ACL_STY
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81c8d80d-9c63-48a1-bd52-bd339432d523",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "1475b9fa-02d6-4976-be75-a94037a115ec",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\nNO_ACL_STY",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "81c8d80d-9c63-48a1-bd52-bd339432d523",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T13:53:26.624Z_

No ACL style available — I'll use a self-contained article class with appropriate formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1475b9fa-02d6-4976-be75-a94037a115ec",
  "isSidechain": false,
  "requestId": "req_011Cb4Tzr2QB9hcQrqGWj2iJ",
  "type": "assistant",
  "uuid": "7ae76839-3774-466e-8ee6-829e9c23d678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSFunX8Y9JTrLt7czXtBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 49304,
      "output_tokens": 11791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11791,
          "cache_read_input_tokens": 49304,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 21 · 2026-05-15T13:56:55.494Z_

<details open><summary>🔧 Tool call — Write · `toolu_01DhSVvcVeG43qYDxGEbtEVX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\\newcommand{\\rsft}{RSFT}\n\n\\title{FREIGE: Faithful Evidence Generation for LLM-Based\\\\Document-Level Relation Extraction via\\\\Contrastive Evidence Discrimination}\n\n\\author{Anonymous Submission to EMNLP 2026}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language models (LLMs) are rapidly closing the gap with encoder-based methods on document-level relation extraction (DocRE), yet no existing LLM approach produces verifiable evidence---the supporting sentences that ground each predicted relation triple.\nWe present \\method{} (\\textbf{F}aithful \\textbf{R}elation \\textbf{E}xtraction with \\textbf{I}ntra-document \\textbf{G}rounded \\textbf{E}vidence), the first generative LLM framework that jointly outputs relation triples \\emph{and} explicit sentence-level evidence citations on DocRED.\nAt the core of \\method{} is \\ced{} (\\textbf{C}ontrastive \\textbf{E}vidence \\textbf{D}iscrimination), a scoring function that measures evidence quality through intra-document hard-negative contrast: the entailment gap between gold evidence and the best entity-sharing distractor sentence.\nWe show that na\\\"ive NLI-based scoring is fooled by entity-sharing distractors and that online RL (GRPO+QLoRA) with \\ced{} reward leads to catastrophic forgetting---a novel \\emph{evidence--extraction decoupling} phenomenon where evidence quality improves (Evi-F1 up to 0.850) while extraction collapses (rel\\_F1 $<$ 0.02).\nInstead, using \\ced{} as an offline quality filter for rejection sampling fine-tuning (\\rsft{}) yields consistent gains: +5.5pp rel\\_F1, +1.7pp Evi-F1 (conditional), and $-$7.1pp \\edcr{} on the DocRED test set over SFT.\nWe further propose the \\edcr{} (\\textbf{E}ntity-sharing \\textbf{D}istractor \\textbf{C}itation \\textbf{R}ate) metric, validated by human annotation (Pearson $r$=0.62), to diagnose plausible-looking but unfaithful evidence that standard Evi-F1 misses.\nExperiments across three model scales (1.7B--8B) and two DocRED variants confirm the generality of our approach.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nDocument-level relation extraction (DocRE) requires identifying relational facts between entity pairs that may span multiple sentences in a document.\nRecent encoder-based methods achieve strong extraction performance and provide implicit evidence through attention-weight thresholding, but their evidence is not directly interpretable.\nMeanwhile, LLM-based approaches to DocRE have shown competitive extraction accuracy, yet none produces explicit evidence citations that a human auditor can verify---a critical gap for deployment in knowledge base population, biomedical curation, and RAG provenance tracking.\n\nA natural approach is to train LLMs with faithfulness rewards derived from natural language inference (NLI) models.\nHowever, we identify a fundamental failure mode: \\emph{entity-sharing distractor sentences}---sentences that mention the same entities as the relation but do not actually support it---receive spuriously high NLI entailment scores due to lexical overlap.\nIn our SFT baseline, 71.2\\% of cited sentences are such distractors (\\edcr{}=0.712), revealing that standard evidence metrics like Evi-F1 are blind to this systematic error pattern.\n\nWe further discover that applying online RL (GRPO) with evidence-quality rewards causes \\emph{catastrophic forgetting with evidence--extraction decoupling}: the model learns to produce high-quality evidence (Evi-F1 up to 0.850) while its extraction capability collapses (rel\\_F1 $< 0.02$).\nThis phenomenon persists across multiple reward types, learning rates, and group sizes ($G$=4, 8), pointing to a structural incompatibility between on-policy RL and document-level structured IE under parameter-efficient fine-tuning.\n\nTo address these challenges, we propose \\method{}, comprising three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{\\ced{} (Contrastive Evidence Discrimination)}: A scoring function that evaluates evidence quality through the entailment margin between cited evidence and the best intra-document hard negative, effectively serving as an anti-reward-overoptimization mechanism for evidence grounding.\n\n\\item \\textbf{\\ced{}-guided \\rsft{}}: Rather than using \\ced{} as an online reward, we employ it as an offline quality filter---generating $N$ candidates from an SFT model, scoring with \\ced{}, and fine-tuning on the top-$k$ highest-quality outputs. This sidesteps the catastrophic forgetting of online RL while retaining the signal strength of \\ced{}.\n\n\\item \\textbf{\\edcr{} (Entity-sharing Distractor Citation Rate)}: A diagnostic metric that measures the proportion of cited sentences sharing entities with the target relation but absent from gold evidence, capturing a failure mode invisible to standard Evi-F1.\n\\end{enumerate}\n\nOn the DocRED test set, \\method{} achieves rel\\_F1=0.455, Evi-F1\\textsubscript{joint}=0.376, and \\edcr{}=0.648, representing the first LLM-based DocRE system with explicit evidence output.\nResults generalize across model scales (1.7B--8B), dataset variants (DocRED, Re-DocRED), and are robust to the choice of NLI backbone.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Document-Level Relation Extraction.}\nEncoder-based DocRE methods achieve state-of-the-art extraction performance.\nDREEAM provides evidence through attention-weight thresholding over a RoBERTa-large encoder, achieving Evi-F1\\textsubscript{joint}=0.573 on DocRED.\nSAIS follows a similar paradigm (Evi-F1\\textsubscript{joint}=0.557).\nRecent LLM-based approaches such as LMRC (LLaMA-3.1-8B, F1=60.69) demonstrate competitive extraction but produce no evidence.\n\\method{} bridges this gap by jointly generating triples and explicit evidence.\n\n\\paragraph{Reward Hacking and Overoptimization.}\nReward overoptimization in RLHF is well-documented: proxy rewards diverge from true objectives as policy optimization progresses.\nCED connects to this literature by providing a contrastive anti-overoptimization mechanism specifically designed for evidence grounding, where entity-sharing distractors create systematic reward hacking opportunities.\n\n\\paragraph{Rejection Sampling Fine-Tuning.}\nRSFT has been shown theoretically equivalent to PPO under certain conditions.\nOur work applies RSFT to a novel domain---evidence-grounded IE---and demonstrates that for structured document-level tasks, offline quality filtering outperforms both online RL (GRPO) and offline preference learning (DPO).\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Task Formulation}\n\nGiven a document $D$ with sentences $\\{S_1, \\ldots, S_n\\}$ and entity mentions, the model must output a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ is the relation type, $t$ is the tail entity, and $E \\subseteq \\{S_1, \\ldots, S_n\\}$ is the set of evidence sentences supporting the relation.\nThe model generates these tuples in a structured text format with explicit sentence index citations $[\\texttt{S}_i]$.\n\n\\subsection{Contrastive Evidence Discrimination (\\ced{})}\n\nStandard NLI-based evidence scoring computes the mean entailment probability over cited sentences:\n\\begin{equation}\n\\text{flat-NLI}(E) = \\frac{1}{|E|}\\sum_{s \\in E} p_{\\text{entail}}(s \\mid h, r, t)\n\\end{equation}\nThis score is vulnerable to entity-sharing distractors: sentences mentioning $h$ or $t$ that do not support $r$ but achieve high entailment scores due to lexical overlap.\n\n\\ced{} addresses this by computing a contrastive margin:\n\\begin{equation}\n\\text{\\ced{}}(E, D) = \\frac{1}{|E|}\\sum_{s \\in E} \\Big[ p_{\\text{entail}}(s) - \\max_{s' \\in \\mathcal{N}(h,t,D)} p_{\\text{entail}}(s') \\Big]\n\\end{equation}\nwhere $\\mathcal{N}(h,t,D) = \\{s' \\in D \\setminus E_{\\text{gold}} : s' \\text{ mentions } h \\text{ or } t\\}$ is the set of intra-document hard negatives---entity-sharing but non-gold sentences.\nThe margin directly penalizes evidence whose entailment score is not substantially higher than the best distractor, serving as an anti-reward-overoptimization mechanism.\n\nWe implement \\ced{} using DeBERTa-v3-base fine-tuned on MNLI (86M parameters), with the relation verbalized as the NLI hypothesis.\n\n\\subsection{\\ced{}-Guided Rejection Sampling Fine-Tuning}\n\nOur training pipeline proceeds in three stages:\n\n\\paragraph{Stage 1: SFT.}\nWe fine-tune a base LLM (Qwen3-4B) with QLoRA on gold DocRED training data, producing a model that can generate (triple, evidence) tuples but with high distractor citation rates.\n\n\\paragraph{Stage 2: Candidate Generation and \\ced{} Filtering.}\nFor each training document, we sample $N=8$ candidate outputs from the SFT model at temperature 0.7.\nEach candidate is scored by \\ced{}, and only the top-$k$ ($k=1$) candidate per document is retained.\nThis yields ${\\sim}$2,718 high-quality training samples from 21,952 candidates (12.4\\% retention rate).\n\n\\paragraph{Stage 3: \\rsft{}.}\nThe SFT model is further fine-tuned on the \\ced{}-filtered candidates with standard supervised loss.\nThe key insight is that \\ced{} serves as a \\emph{data quality filter} rather than a training reward, completely avoiding the credit-assignment difficulties and catastrophic forgetting of on-policy RL on structured outputs.\n\n\\subsection{\\edcr{}: Entity-Sharing Distractor Citation Rate}\n\\label{sec:edcr}\n\nWe propose \\edcr{} as a diagnostic metric:\n\\begin{equation}\n\\edcr{} = \\frac{|\\{s \\in \\hat{E} : s \\notin E_{\\text{gold}} \\wedge s \\in \\mathcal{N}(h,t,D)\\}|}{|\\hat{E}|}\n\\end{equation}\nwhere $\\hat{E}$ is the set of predicted evidence sentences.\n\\edcr{} captures a specific failure mode invisible to standard Evi-F1: citing sentences that \\emph{look} like evidence (they mention the right entities) but do not actually support the relation.\nLower \\edcr{} is better (denoted \\edcr{}$\\downarrow$ in tables).\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Setup}\n\n\\paragraph{Dataset.}\nWe evaluate on DocRED, the standard benchmark for document-level RE with sentence-level evidence annotations.\nWe additionally report results on Re-DocRED, which corrects ${\\sim}$25\\% false-negative relations in the original annotations.\nTest set evaluation uses the official CodaLab submission for rel\\_F1 and Ign\\_F1.\n\n\\paragraph{Model and Training.}\nOur base model is Qwen3-4B with QLoRA (rank=64).\nSFT uses the full DocRED gold training set (12,151 examples).\n\\rsft{} uses the best SFT checkpoint as the sampling policy, generating $N$=8 candidates per document at temperature 0.7.\nWe report results for the best \\rsft{} configuration (3 epochs, $\\alpha$=128, seed=43).\n\n\\paragraph{Metrics.}\nWe report: (1)~rel\\_F1 and Ign\\_F1 for extraction quality; (2)~Evi-F1\\textsubscript{joint} (DREEAM protocol: evidence counts only when the relation is also correct) and Evi-F1\\textsubscript{cond} (conditional on correct relation); (3)~\\edcr{}$\\downarrow$ for distractor citation diagnosis.\n\n\\paragraph{Baselines.}\nWe compare against: DREEAM (RoBERTa-large, attention-based evidence), SAIS (RoBERTa-large, attention-based), and LMRC (LLaMA-3.1-8B, no evidence).\n\n%------------------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:main_results} presents test set results.\n\\method{} (RSFT+CED) achieves rel\\_F1=0.455, a +5.5pp improvement over the SFT baseline (0.400), with consistent gains across all metrics.\nThe Evi-F1\\textsubscript{joint} of 0.376 represents the first reported number for any LLM-based method on this metric, as prior generative approaches (LMRC, DocKS-RAG) do not output evidence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Test set results on DocRED. $\\dagger$: encoder-based methods with attention-threshold evidence. $\\ddagger$: generative LLM methods. Evi-F1\\textsubscript{J} = joint (DREEAM protocol); Evi-F1\\textsubscript{C} = conditional on correct relation.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{rel\\_F1} & \\textbf{Ign\\_F1} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{Evi-F1\\textsubscript{C}} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\nDREEAM$^\\dagger$         & Enc.  & ---   & ---   & 0.573 & 0.834 & ---   \\\\\nSAIS$^\\dagger$           & Enc.  & ---   & ---   & 0.557 & ---   & ---   \\\\\nLMRC$^\\ddagger$          & Gen.  & 0.607 & ---   & ---   & ---   & ---   \\\\\n\\midrule\nSFT baseline$^\\ddagger$  & Gen.  & 0.400 & 0.381 & 0.322 & 0.790 & 0.719 \\\\\nRSFT flat-NLI$^\\ddagger$ & Gen.  & 0.430 & 0.412 & 0.342 & 0.788 & 0.701 \\\\\n\\textbf{\\method{}}$^\\ddagger$ & Gen. & \\textbf{0.455} & \\textbf{0.437} & \\textbf{0.376} & \\textbf{0.807} & \\textbf{0.648} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCompared with encoder-based methods, the gap in Evi-F1\\textsubscript{joint} (0.376 vs.\\ DREEAM's 0.573) is primarily driven by the extraction accuracy gap (rel\\_F1 0.455 vs.\\ ${\\sim}$0.631), not evidence quality: on correctly predicted triples, \\method{}'s conditional Evi-F1 (0.807) approaches DREEAM's (0.834).\nCritically, \\method{} outputs \\emph{explicit} sentence citations whereas DREEAM's evidence is implicit attention weights---a qualitatively different and more interpretable form.\n\nTable~\\ref{tab:joint_vs_cond} provides a comprehensive view of joint vs.\\ conditional Evi-F1 across methods on the dev set, demonstrating that the decoupling between extraction and evidence quality is most extreme for GRPO (joint Evi-F1 of 0.012 despite conditional Evi-F1 of 0.850).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Conditional vs.\\ Joint Evi-F1 on DocRED dev set. Joint Evi-F1 penalizes incorrect relation predictions with zero evidence credit.}\n\\label{tab:joint_vs_cond}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1\\textsubscript{C}} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\nGRPO (lr=5e-6)    & 0.014 & 0.850 & 0.012 & 0.988 \\\\\nGRPO (lr=5e-5)    & 0.211 & 0.567 & 0.119 & 0.858 \\\\\nSFT baseline      & 0.406 & 0.798 & 0.322 & 0.712 \\\\\nRSFT flat-NLI     & 0.441 & 0.797 & 0.350 & 0.689 \\\\\nCED-reranker      & 0.415 & 0.821 & 0.341 & 0.598 \\\\\n\\rsft{} CED       & 0.468 & 0.816 & 0.381 & 0.639 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Why Online RL Fails: Evidence--Extraction Decoupling}\n\\label{sec:grpo_failure}\n%------------------------------------------------------------------------------\n\nA central finding is that GRPO+QLoRA with evidence-quality rewards leads to catastrophic forgetting, regardless of reward type, learning rate, or group size.\nTable~\\ref{tab:rl_spectrum} presents the full online--offline RL spectrum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Online--offline RL spectrum on DocRED dev set. GRPO exhibits catastrophic forgetting across configurations. DPO avoids collapse but degrades below SFT. Only \\rsft{} improves over SFT.}\n\\label{tab:rl_spectrum}\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{RL Type} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{Catastrophic?} \\\\\n\\midrule\nGRPO $G$=4    & On-policy   & 0.014 & 0.850 & 0.988 & Yes \\\\\nGRPO $G$=8    & On-policy   & 0.031 & 0.816 & 0.981 & Yes \\\\\nDPO+CED       & Offline pref. & 0.325 & 0.786 & 0.683 & No (degraded) \\\\\nSFT            & No RL       & 0.406 & 0.798 & 0.712 & No \\\\\n\\textbf{\\rsft{}+CED} & Offline filtered & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{GRPO Catastrophic Forgetting.}\nAll GRPO configurations exhibit the same pattern: the CED reward increases while rel\\_F1 collapses to near zero.\nWith $G$=4 (lr=5e-6), rel\\_F1 drops to 0.014 while Evi-F1 reaches 0.850---the model learns to cite extensive evidence but can no longer extract relations.\nIncreasing $G$ to 8 marginally delays the onset of forgetting (step ${\\sim}$15 vs.\\ ${\\sim}$10) but does not prevent it: best rel\\_F1 remains 0.031, far below SFT's 0.406.\nThis rules out advantage-estimation noise as the root cause and points to a structural incompatibility: QLoRA's rank-limited parameter space, when updated by RL gradients, preferentially optimizes the easier evidence dimension at the expense of structured extraction.\n\n\\paragraph{DPO as Intermediate Baseline.}\nDPO+CED (Table~\\ref{tab:rl_spectrum}) avoids catastrophic forgetting (rel\\_F1=0.325) but \\emph{degrades} below SFT (0.406), yielding $-$8.1pp.\nThis demonstrates that the problem is not simply online vs.\\ offline RL: DPO's token-level contrastive loss struggles with credit assignment over long structured outputs, and suppressing rejected candidates inadvertently penalizes correct extraction patterns.\nThe full spectrum GRPO (0.014--0.031) $\\ll$ DPO (0.325) $<$ SFT (0.406) $<$ \\rsft{} (0.468) shows that for document-level IE, \\ced{} is most effective as a data filter, not a learning objective.\n\n\\paragraph{Forgetting Dynamics.}\nAnalysis of 42 checkpoints across 3 GRPO configurations reveals a consistent three-phase pattern: (1)~\\emph{Decoupling onset} (steps 5--15): rel\\_F1 begins declining while Evi-F1 rises; (2)~\\emph{Acceleration} (steps 15--50): rel\\_F1 collapses below 0.05, reward saturates; (3)~\\emph{Plateau} (steps 50--100): rel\\_F1 oscillates near zero, Evi-F1 stabilizes at 0.80--0.85.\nAll configurations converge to a common attractor in the (low-rel\\_F1, high-Evi-F1) region, regardless of learning rate or group size.\n\n%------------------------------------------------------------------------------\n\\subsection{\\ced{} vs.\\ Flat-NLI Scoring}\n\\label{sec:ced_vs_flatnli}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:ced_ablation} presents the core ablation comparing \\ced{}-filtered vs.\\ flat-NLI-filtered \\rsft{}.\n\\ced{} yields statistically significant improvements across all three metrics (paired bootstrap, $p < 0.01$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CED vs.\\ flat-NLI as \\rsft{} filtering signal (DocRED dev set). Both \\rsft{} variants improve over SFT; CED significantly outperforms flat-NLI ($p < 0.01$ for all metrics, paired bootstrap).}\n\\label{tab:ced_ablation}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{$n_{\\text{train}}$} \\\\\n\\midrule\nSFT baseline                    & 0.406 & 0.798 & 0.712 & 12,151 \\\\\n\\rsft{} flat-NLI (A: 3ep)       & 0.441 & 0.795 & 0.695 & 2,845 \\\\\n\\rsft{} flat-NLI (B: 1ep)       & 0.438 & 0.797 & 0.689 & 2,845 \\\\\n\\rsft{} CED (s43: 3ep)          & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} & 2,718 \\\\\n\\rsft{} CED (r2b: 1ep)          & 0.449 & 0.813 & 0.661 & 2,718 \\\\\n\\midrule\n$\\Delta$ (CED best $-$ flat-NLI best)  & +2.71pp & +2.08pp & $-$5.64pp & --- \\\\\n$p$-value (paired bootstrap)           & 0.007 & 0.004 & 0.002 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe advantage of \\ced{} is concentrated in distractor-dense documents (distractor density $>$ 0.4), where the Evi-F1 gap expands to ${\\sim}$3.5pp, while in low-distractor documents the difference is negligible (${\\sim}$0.8pp, not significant).\nThis confirms that the contrastive margin is specifically effective at distinguishing true evidence from entity-sharing distractors---precisely the failure mode that flat-NLI scoring cannot address.\n\nBoth flat-NLI \\rsft{} variants still improve over SFT (+3.2--3.6pp rel\\_F1), indicating that \\emph{any} quality filtering helps, but \\ced{}'s contrastive design provides additional discriminative power where it matters most.\n\n%------------------------------------------------------------------------------\n\\subsection{\\ced{} Usage Modes: Training vs.\\ Inference}\n\\label{sec:ced_usage}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:ced_modes} compares two usage modes of \\ced{}: as a training data filter (\\rsft{}) and as an inference-time reranker.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CED usage modes (DocRED dev set). CED as training signal (\\rsft{}) substantially outperforms CED as inference-time reranker.}\n\\label{tab:ced_modes}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{CED Usage} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{Extra Training} \\\\\n\\midrule\nSFT (no CED)                & 0.406 & 0.798 & 0.712 & --- \\\\\nCED-reranker (inference)     & 0.415 & 0.821 & 0.598 & None \\\\\n\\rsft{} flat-NLI (training)  & 0.441 & 0.797 & 0.689 & \\rsft{} \\\\\n\\rsft{} CED (training)       & \\textbf{0.468} & \\textbf{0.816} & 0.639 & \\rsft{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCED-reranking achieves the lowest \\edcr{} (0.598) by directly selecting the candidate with the highest contrastive margin, but its rel\\_F1 gain is modest (+0.95pp over SFT).\nThis is because reranking cannot improve beyond the quality ceiling of the candidate pool---it selects the best existing output but does not shift the model's generation distribution.\nIn contrast, \\rsft{} with CED filtering gains +6.26pp rel\\_F1 by teaching the model to \\emph{generate} higher-quality outputs, confirming that CED is most effective as a training signal rather than a pure inference-time mechanism.\n\n%------------------------------------------------------------------------------\n\\subsection{\\edcr{} as a Diagnostic Metric}\n\\label{sec:edcr_analysis}\n%------------------------------------------------------------------------------\n\n\\paragraph{Cross-Method Diagnostic.}\nTable~\\ref{tab:edcr_diagnostic} presents \\edcr{} computed across all evidence-producing methods, revealing a clear gradient that aligns with the training paradigm.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-method \\edcr{} diagnostic (DocRED dev set). Methods sorted by \\edcr{} descending. \\edcr{} captures a systematic gradient from catastrophic GRPO to CED-reranker.}\n\\label{tab:edcr_diagnostic}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{$n_{\\text{distractor}}$} \\\\\n\\midrule\nGRPO ckpt-100 (lr=5e-6) & 0.014 & 0.850 & 0.988 & 12,675 \\\\\nGRPO ckpt-90 (lr=5e-5)  & 0.211 & 0.567 & 0.858 & 8,431 \\\\\nSFT baseline             & 0.406 & 0.798 & 0.712 & 10,113 \\\\\nRSFT flat-NLI            & 0.441 & 0.797 & 0.689 & 9,556 \\\\\nRSFT CED (r2b)           & 0.449 & 0.813 & 0.661 & 8,950 \\\\\nRSFT CED (s43)           & 0.468 & 0.816 & 0.639 & 8,475 \\\\\nCED-reranker             & 0.415 & 0.821 & 0.598 & 7,768 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\edcr{} gradient (0.988 $\\to$ 0.598) is monotonically related to the strength of evidence-quality supervision: GRPO outputs nearly all distractors, SFT has no evidence signal, flat-NLI provides weak filtering, CED provides contrastive filtering, and CED-reranker applies CED directly at inference.\nNotably, the cross-method Pearson correlation between \\edcr{} and Evi-F1 is only $r$=$-$0.42, confirming that \\edcr{} captures a dimension of evidence quality \\emph{not} measured by standard Evi-F1.\n\n\\paragraph{Human Validation.}\nTo validate \\edcr{} as a meaningful automatic metric, we conduct a human annotation study on 100 samples (25 per method: GRPO, SFT, RSFT flat-NLI, RSFT CED).\nThree annotators independently judge whether each cited sentence truly supports its corresponding relation (inter-annotator Cohen's $\\kappa$=0.72, substantial agreement).\nTable~\\ref{tab:human_edcr} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Human validation of \\edcr{} (100 samples, 3 annotators, $\\kappa$=0.72). Auto \\edcr{} correlates with human distractor rate at Pearson $r$=0.62.}\n\\label{tab:human_edcr}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{\\edcr{}\\textsubscript{auto}} & \\textbf{Human dist.\\ rate} & $\\Delta$ & $n$ \\\\\n\\midrule\nGRPO ckpt-90     & 0.858 & 0.954 & $-$0.096 & 25 \\\\\nSFT              & 0.712 & 0.645 & +0.067 & 25 \\\\\nRSFT flat-NLI    & 0.695 & 0.608 & +0.087 & 25 \\\\\nRSFT CED         & 0.639 & 0.524 & +0.115 & 25 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{Overall Pearson $r$} & \\multicolumn{3}{c}{0.62 ($p < 0.001$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall Pearson $r$=0.62 confirms that \\edcr{} is a meaningful proxy for human-judged evidence quality.\nThe ranking of methods is preserved perfectly between automatic and human evaluation.\nAuto \\edcr{} exhibits a slight positive bias (+6.8pp on average), because the entity-sharing heuristic is somewhat stricter than human judgment---some entity-sharing sentences are deemed partially supportive by human annotators.\nThe CED RSFT method shows the largest auto--human gap (0.115), suggesting that CED-trained models produce citations that are correct by the entity-sharing criterion but occasionally omit contextually relevant (though not gold-annotated) sentences.\n\n%------------------------------------------------------------------------------\n\\subsection{Generalization Experiments}\n\\label{sec:generalization}\n%------------------------------------------------------------------------------\n\n\\paragraph{Model Size Ablation.}\nTable~\\ref{tab:model_size} verifies that \\rsft{}+CED is effective across model scales from 1.7B to 8B parameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model size ablation (DocRED dev set). \\rsft{}+CED improves consistently across 1.7B--8B.}\n\\label{tab:model_size}\n\\begin{tabular}{@{}llcccr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & $\\Delta$\\textbf{rel\\_F1} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-1.7B} & SFT      & 0.341 & 0.753 & 0.746 & --- \\\\\n                             & \\rsft{}+CED & 0.372 & 0.778 & 0.693 & +3.12pp \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-4B}   & SFT      & 0.406 & 0.798 & 0.712 & --- \\\\\n                             & \\rsft{}+CED & 0.468 & 0.816 & 0.639 & +6.26pp \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}   & SFT      & 0.442 & 0.813 & 0.689 & --- \\\\\n                             & \\rsft{}+CED & 0.491 & 0.837 & 0.619 & +4.89pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe absolute improvement ranges from +3.1pp (1.7B) to +6.3pp (4B) to +4.9pp (8B).\nThe 4B model occupies a sweet spot: large enough to generate diverse high-quality candidates but small enough that SFT alone leaves substantial room for improvement.\nThe 8B model achieves the highest absolute performance (rel\\_F1=0.491) but has smaller relative gains because its SFT baseline is already stronger.\n\\edcr{} decreases consistently across all scales ($-$5.2 to $-$7.3pp), confirming the generality of CED-based evidence improvement.\n\n\\paragraph{Re-DocRED.}\nTable~\\ref{tab:redocred} shows results on Re-DocRED, which corrects ${\\sim}$25\\% false-negative annotations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED vs.\\ Re-DocRED (dev set). \\rsft{}+CED gains are preserved on cleaner annotations.}\n\\label{tab:redocred}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}    & SFT      & 0.406 & 0.798 & 0.712 \\\\\n                           & \\rsft{}+CED & 0.468 & 0.816 & 0.639 \\\\\n\\midrule\n\\multirow{2}{*}{Re-DocRED} & SFT      & 0.453 & 0.811 & 0.689 \\\\\n                           & \\rsft{}+CED & 0.509 & 0.838 & 0.602 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\rsft{}+CED improvement (+5.55pp on Re-DocRED vs.\\ +6.26pp on DocRED) is preserved, demonstrating that CED is not exploiting annotation noise.\nAll methods benefit from cleaner annotations, with \\edcr{} decreasing on Re-DocRED because some previously labeled distractors are reclassified as gold evidence.\n\n\\paragraph{top-$k$ Ablation.}\nTable~\\ref{tab:topk} examines the effect of CED filtering strictness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{top-$k$ ablation for CED filtering (DocRED dev set). Stricter filtering ($k$=1) yields higher quality despite fewer training samples.}\n\\label{tab:topk}\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n\\textbf{top-$k$} & $n_{\\text{train}}$ & \\textbf{Mean CED} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\n1 & 2,718 & 0.668 & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} \\\\\n3 & 7,856 & 0.523 & 0.452 & 0.803 & 0.671 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrict filtering ($k$=1, 2,718 samples) outperforms relaxed filtering ($k$=3, 7,856 samples) across all metrics.\nThe additional samples from $k$=3 have systematically lower CED scores (mean 0.523 vs.\\ 0.668), introducing distractor-heavy training examples that dilute the quality signal.\nThis confirms the ``less is more'' principle for \\rsft{}: the SFT stage already provides broad coverage, and \\rsft{} needs only a small number of high-quality samples to calibrate evidence citation behavior.\n\n\\paragraph{NLI Model Ablation.}\nTable~\\ref{tab:nli_ablation} shows that replacing DeBERTa-v3-base (86M) with DeBERTa-v3-large (304M) yields marginal improvements (+0.38pp rel\\_F1), confirming that \\ced{}'s effectiveness stems from the contrastive design rather than the NLI model's capacity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{NLI model ablation for CED scoring. Larger NLI model provides marginal gains.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{NLI Model} & \\textbf{Params} & \\textbf{Disc.\\ Acc} & \\textbf{\\rsft{} rel\\_F1} & \\textbf{\\rsft{} Evi-F1} \\\\\n\\midrule\nDeBERTa-v3-base  & 86M  & 0.815 & 0.468 & 0.816 \\\\\nDeBERTa-v3-large & 304M & 0.847 & 0.472 & 0.819 \\\\\n\\midrule\n$\\Delta$ & --- & +0.032 & +0.38pp & +0.33pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe top-1 candidate selection agrees between base and large models on 89\\% of documents; the 11\\% disagreements produce only marginal downstream differences, lowering the computational barrier for adopting \\method{}.\n\n\\paragraph{Baseline Comparison with Evidence Methods.}\nTable~\\ref{tab:evidence_comparison} contextualizes \\method{} against encoder-based evidence methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence baseline comparison (dev set). \\method{} is the first generative LLM method with explicit evidence; the Evi-F1\\textsubscript{J} gap vs.\\ encoders is driven by extraction accuracy, not evidence quality.}\n\\label{tab:evidence_comparison}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{rel\\_F1} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{Evidence Form} \\\\\n\\midrule\nDREEAM      & Encoder  & 0.631 & 0.572 & Attention threshold \\\\\nSAIS        & Encoder  & 0.610 & 0.554 & Attention threshold \\\\\nLMRC        & Gen.\\ LLM & 0.607 & ---   & None \\\\\nSFT baseline & Gen.\\ LLM & 0.406 & 0.322 & Explicit citation \\\\\n\\textbf{\\method{}} & Gen.\\ LLM & 0.468 & 0.381 & Explicit citation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why \\rsft{} Succeeds Where RL Fails.}\nThe evidence--extraction decoupling phenomenon reveals that document-level IE presents unique challenges for on-policy RL: (1) QLoRA's rank-limited parameters are easily overwritten by RL gradients that preferentially optimize the more gradient-accessible evidence dimension; (2) evidence-quality rewards provide stronger gradients than extraction-accuracy signals, causing asymmetric optimization; (3) the combinatorial output space of multiple triples with evidence makes credit assignment intractable for policy-gradient methods.\n\\rsft{} bypasses all three issues by using standard supervised learning on curated data, inheriting the stability of SFT while benefiting from CED's quality signal.\n\n\\paragraph{Limitations of \\edcr{}.}\nEntity-sharing is an operationalized proxy for distractor sentences, not a perfect definition.\nThe auto--human gap of +6.8pp (Table~\\ref{tab:human_edcr}) indicates that some entity-sharing sentences provide partial contextual support.\nAdditionally, \\edcr{} does not capture non-entity-sharing distractors (sentences that are irrelevant but happen not to mention target entities).\nWe recommend using \\edcr{} as a complementary diagnostic alongside Evi-F1, not as a replacement.\n\n\\paragraph{Extraction Gap vs.\\ Encoders.}\n\\method{}'s primary limitation is the extraction accuracy gap compared to encoder-based methods (rel\\_F1 0.455 vs.\\ DREEAM's ${\\sim}$0.631).\nThis gap is inherent to the generative paradigm under current model scales and is not specific to our method---LMRC (LLaMA-3.1-8B) achieves 0.607 with 2$\\times$ parameters and no evidence output.\nAs LLM capabilities scale, this gap is expected to narrow, making evidence generation increasingly valuable.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented \\method{}, the first LLM-based document-level RE framework that jointly generates relation triples and verifiable sentence-level evidence.\nOur core technical contribution, \\ced{}, provides a contrastive evidence scoring mechanism that is effective as an offline data quality filter but causes catastrophic forgetting when used as an online RL reward---revealing a previously unreported evidence--extraction decoupling phenomenon in GRPO+QLoRA for structured IE.\nThe proposed \\edcr{} metric, validated by human annotation ($r$=0.62), captures a systematic failure mode of evidence citation invisible to standard Evi-F1.\nExperiments across three model scales, two dataset variants, multiple RL paradigms, and extensive ablations demonstrate the robustness of our approach.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae76839-3774-466e-8ee6-829e9c23d678",
  "isSidechain": false,
  "requestId": "req_011Cb4Tzr2QB9hcQrqGWj2iJ",
  "type": "assistant",
  "uuid": "505c6351-6ef9-4989-aaae-68864fb8bb8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aSFunX8Y9JTrLt7czXtBS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 49304,
      "output_tokens": 11791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11791,
          "cache_read_input_tokens": 49304,
          "cache_creation_input_tokens": 187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 187
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

_source line 22 · 2026-05-15T13:56:55.537Z_

<details><summary>↩ Tool result · `toolu_01DhSVvcVeG43qYDxGEbtEVX`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "505c6351-6ef9-4989-aaae-68864fb8bb8b",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "472f67c7-fd73-404b-981d-899291825180",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\\newcommand{\\rsft}{RSFT}\n\n\\title{FREIGE: Faithful Evidence Generation for LLM-Based\\\\Document-Level Relation Extraction via\\\\Contrastive Evidence Discrimination}\n\n\\author{Anonymous Submission to EMNLP 2026}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nLarge language models (LLMs) are rapidly closing the gap with encoder-based methods on document-level relation extraction (DocRE), yet no existing LLM approach produces verifiable evidence---the supporting sentences that ground each predicted relation triple.\nWe present \\method{} (\\textbf{F}aithful \\textbf{R}elation \\textbf{E}xtraction with \\textbf{I}ntra-document \\textbf{G}rounded \\textbf{E}vidence), the first generative LLM framework that jointly outputs relation triples \\emph{and} explicit sentence-level evidence citations on DocRED.\nAt the core of \\method{} is \\ced{} (\\textbf{C}ontrastive \\textbf{E}vidence \\textbf{D}iscrimination), a scoring function that measures evidence quality through intra-document hard-negative contrast: the entailment gap between gold evidence and the best entity-sharing distractor sentence.\nWe show that na\\\"ive NLI-based scoring is fooled by entity-sharing distractors and that online RL (GRPO+QLoRA) with \\ced{} reward leads to catastrophic forgetting---a novel \\emph{evidence--extraction decoupling} phenomenon where evidence quality improves (Evi-F1 up to 0.850) while extraction collapses (rel\\_F1 $<$ 0.02).\nInstead, using \\ced{} as an offline quality filter for rejection sampling fine-tuning (\\rsft{}) yields consistent gains: +5.5pp rel\\_F1, +1.7pp Evi-F1 (conditional), and $-$7.1pp \\edcr{} on the DocRED test set over SFT.\nWe further propose the \\edcr{} (\\textbf{E}ntity-sharing \\textbf{D}istractor \\textbf{C}itation \\textbf{R}ate) metric, validated by human annotation (Pearson $r$=0.62), to diagnose plausible-looking but unfaithful evidence that standard Evi-F1 misses.\nExperiments across three model scales (1.7B--8B) and two DocRED variants confirm the generality of our approach.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nDocument-level relation extraction (DocRE) requires identifying relational facts between entity pairs that may span multiple sentences in a document.\nRecent encoder-based methods achieve strong extraction performance and provide implicit evidence through attention-weight thresholding, but their evidence is not directly interpretable.\nMeanwhile, LLM-based approaches to DocRE have shown competitive extraction accuracy, yet none produces explicit evidence citations that a human auditor can verify---a critical gap for deployment in knowledge base population, biomedical curation, and RAG provenance tracking.\n\nA natural approach is to train LLMs with faithfulness rewards derived from natural language inference (NLI) models.\nHowever, we identify a fundamental failure mode: \\emph{entity-sharing distractor sentences}---sentences that mention the same entities as the relation but do not actually support it---receive spuriously high NLI entailment scores due to lexical overlap.\nIn our SFT baseline, 71.2\\% of cited sentences are such distractors (\\edcr{}=0.712), revealing that standard evidence metrics like Evi-F1 are blind to this systematic error pattern.\n\nWe further discover that applying online RL (GRPO) with evidence-quality rewards causes \\emph{catastrophic forgetting with evidence--extraction decoupling}: the model learns to produce high-quality evidence (Evi-F1 up to 0.850) while its extraction capability collapses (rel\\_F1 $< 0.02$).\nThis phenomenon persists across multiple reward types, learning rates, and group sizes ($G$=4, 8), pointing to a structural incompatibility between on-policy RL and document-level structured IE under parameter-efficient fine-tuning.\n\nTo address these challenges, we propose \\method{}, comprising three contributions:\n\n\\begin{enumerate}\n\\item \\textbf{\\ced{} (Contrastive Evidence Discrimination)}: A scoring function that evaluates evidence quality through the entailment margin between cited evidence and the best intra-document hard negative, effectively serving as an anti-reward-overoptimization mechanism for evidence grounding.\n\n\\item \\textbf{\\ced{}-guided \\rsft{}}: Rather than using \\ced{} as an online reward, we employ it as an offline quality filter---generating $N$ candidates from an SFT model, scoring with \\ced{}, and fine-tuning on the top-$k$ highest-quality outputs. This sidesteps the catastrophic forgetting of online RL while retaining the signal strength of \\ced{}.\n\n\\item \\textbf{\\edcr{} (Entity-sharing Distractor Citation Rate)}: A diagnostic metric that measures the proportion of cited sentences sharing entities with the target relation but absent from gold evidence, capturing a failure mode invisible to standard Evi-F1.\n\\end{enumerate}\n\nOn the DocRED test set, \\method{} achieves rel\\_F1=0.455, Evi-F1\\textsubscript{joint}=0.376, and \\edcr{}=0.648, representing the first LLM-based DocRE system with explicit evidence output.\nResults generalize across model scales (1.7B--8B), dataset variants (DocRED, Re-DocRED), and are robust to the choice of NLI backbone.\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Document-Level Relation Extraction.}\nEncoder-based DocRE methods achieve state-of-the-art extraction performance.\nDREEAM provides evidence through attention-weight thresholding over a RoBERTa-large encoder, achieving Evi-F1\\textsubscript{joint}=0.573 on DocRED.\nSAIS follows a similar paradigm (Evi-F1\\textsubscript{joint}=0.557).\nRecent LLM-based approaches such as LMRC (LLaMA-3.1-8B, F1=60.69) demonstrate competitive extraction but produce no evidence.\n\\method{} bridges this gap by jointly generating triples and explicit evidence.\n\n\\paragraph{Reward Hacking and Overoptimization.}\nReward overoptimization in RLHF is well-documented: proxy rewards diverge from true objectives as policy optimization progresses.\nCED connects to this literature by providing a contrastive anti-overoptimization mechanism specifically designed for evidence grounding, where entity-sharing distractors create systematic reward hacking opportunities.\n\n\\paragraph{Rejection Sampling Fine-Tuning.}\nRSFT has been shown theoretically equivalent to PPO under certain conditions.\nOur work applies RSFT to a novel domain---evidence-grounded IE---and demonstrates that for structured document-level tasks, offline quality filtering outperforms both online RL (GRPO) and offline preference learning (DPO).\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n\\subsection{Task Formulation}\n\nGiven a document $D$ with sentences $\\{S_1, \\ldots, S_n\\}$ and entity mentions, the model must output a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ is the relation type, $t$ is the tail entity, and $E \\subseteq \\{S_1, \\ldots, S_n\\}$ is the set of evidence sentences supporting the relation.\nThe model generates these tuples in a structured text format with explicit sentence index citations $[\\texttt{S}_i]$.\n\n\\subsection{Contrastive Evidence Discrimination (\\ced{})}\n\nStandard NLI-based evidence scoring computes the mean entailment probability over cited sentences:\n\\begin{equation}\n\\text{flat-NLI}(E) = \\frac{1}{|E|}\\sum_{s \\in E} p_{\\text{entail}}(s \\mid h, r, t)\n\\end{equation}\nThis score is vulnerable to entity-sharing distractors: sentences mentioning $h$ or $t$ that do not support $r$ but achieve high entailment scores due to lexical overlap.\n\n\\ced{} addresses this by computing a contrastive margin:\n\\begin{equation}\n\\text{\\ced{}}(E, D) = \\frac{1}{|E|}\\sum_{s \\in E} \\Big[ p_{\\text{entail}}(s) - \\max_{s' \\in \\mathcal{N}(h,t,D)} p_{\\text{entail}}(s') \\Big]\n\\end{equation}\nwhere $\\mathcal{N}(h,t,D) = \\{s' \\in D \\setminus E_{\\text{gold}} : s' \\text{ mentions } h \\text{ or } t\\}$ is the set of intra-document hard negatives---entity-sharing but non-gold sentences.\nThe margin directly penalizes evidence whose entailment score is not substantially higher than the best distractor, serving as an anti-reward-overoptimization mechanism.\n\nWe implement \\ced{} using DeBERTa-v3-base fine-tuned on MNLI (86M parameters), with the relation verbalized as the NLI hypothesis.\n\n\\subsection{\\ced{}-Guided Rejection Sampling Fine-Tuning}\n\nOur training pipeline proceeds in three stages:\n\n\\paragraph{Stage 1: SFT.}\nWe fine-tune a base LLM (Qwen3-4B) with QLoRA on gold DocRED training data, producing a model that can generate (triple, evidence) tuples but with high distractor citation rates.\n\n\\paragraph{Stage 2: Candidate Generation and \\ced{} Filtering.}\nFor each training document, we sample $N=8$ candidate outputs from the SFT model at temperature 0.7.\nEach candidate is scored by \\ced{}, and only the top-$k$ ($k=1$) candidate per document is retained.\nThis yields ${\\sim}$2,718 high-quality training samples from 21,952 candidates (12.4\\% retention rate).\n\n\\paragraph{Stage 3: \\rsft{}.}\nThe SFT model is further fine-tuned on the \\ced{}-filtered candidates with standard supervised loss.\nThe key insight is that \\ced{} serves as a \\emph{data quality filter} rather than a training reward, completely avoiding the credit-assignment difficulties and catastrophic forgetting of on-policy RL on structured outputs.\n\n\\subsection{\\edcr{}: Entity-Sharing Distractor Citation Rate}\n\\label{sec:edcr}\n\nWe propose \\edcr{} as a diagnostic metric:\n\\begin{equation}\n\\edcr{} = \\frac{|\\{s \\in \\hat{E} : s \\notin E_{\\text{gold}} \\wedge s \\in \\mathcal{N}(h,t,D)\\}|}{|\\hat{E}|}\n\\end{equation}\nwhere $\\hat{E}$ is the set of predicted evidence sentences.\n\\edcr{} captures a specific failure mode invisible to standard Evi-F1: citing sentences that \\emph{look} like evidence (they mention the right entities) but do not actually support the relation.\nLower \\edcr{} is better (denoted \\edcr{}$\\downarrow$ in tables).\n\n%==============================================================================\n\\section{Experiments}\n\\label{sec:experiments}\n%==============================================================================\n\n\\subsection{Setup}\n\n\\paragraph{Dataset.}\nWe evaluate on DocRED, the standard benchmark for document-level RE with sentence-level evidence annotations.\nWe additionally report results on Re-DocRED, which corrects ${\\sim}$25\\% false-negative relations in the original annotations.\nTest set evaluation uses the official CodaLab submission for rel\\_F1 and Ign\\_F1.\n\n\\paragraph{Model and Training.}\nOur base model is Qwen3-4B with QLoRA (rank=64).\nSFT uses the full DocRED gold training set (12,151 examples).\n\\rsft{} uses the best SFT checkpoint as the sampling policy, generating $N$=8 candidates per document at temperature 0.7.\nWe report results for the best \\rsft{} configuration (3 epochs, $\\alpha$=128, seed=43).\n\n\\paragraph{Metrics.}\nWe report: (1)~rel\\_F1 and Ign\\_F1 for extraction quality; (2)~Evi-F1\\textsubscript{joint} (DREEAM protocol: evidence counts only when the relation is also correct) and Evi-F1\\textsubscript{cond} (conditional on correct relation); (3)~\\edcr{}$\\downarrow$ for distractor citation diagnosis.\n\n\\paragraph{Baselines.}\nWe compare against: DREEAM (RoBERTa-large, attention-based evidence), SAIS (RoBERTa-large, attention-based), and LMRC (LLaMA-3.1-8B, no evidence).\n\n%------------------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:main_results} presents test set results.\n\\method{} (RSFT+CED) achieves rel\\_F1=0.455, a +5.5pp improvement over the SFT baseline (0.400), with consistent gains across all metrics.\nThe Evi-F1\\textsubscript{joint} of 0.376 represents the first reported number for any LLM-based method on this metric, as prior generative approaches (LMRC, DocKS-RAG) do not output evidence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Test set results on DocRED. $\\dagger$: encoder-based methods with attention-threshold evidence. $\\ddagger$: generative LLM methods. Evi-F1\\textsubscript{J} = joint (DREEAM protocol); Evi-F1\\textsubscript{C} = conditional on correct relation.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{rel\\_F1} & \\textbf{Ign\\_F1} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{Evi-F1\\textsubscript{C}} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\nDREEAM$^\\dagger$         & Enc.  & ---   & ---   & 0.573 & 0.834 & ---   \\\\\nSAIS$^\\dagger$           & Enc.  & ---   & ---   & 0.557 & ---   & ---   \\\\\nLMRC$^\\ddagger$          & Gen.  & 0.607 & ---   & ---   & ---   & ---   \\\\\n\\midrule\nSFT baseline$^\\ddagger$  & Gen.  & 0.400 & 0.381 & 0.322 & 0.790 & 0.719 \\\\\nRSFT flat-NLI$^\\ddagger$ & Gen.  & 0.430 & 0.412 & 0.342 & 0.788 & 0.701 \\\\\n\\textbf{\\method{}}$^\\ddagger$ & Gen. & \\textbf{0.455} & \\textbf{0.437} & \\textbf{0.376} & \\textbf{0.807} & \\textbf{0.648} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCompared with encoder-based methods, the gap in Evi-F1\\textsubscript{joint} (0.376 vs.\\ DREEAM's 0.573) is primarily driven by the extraction accuracy gap (rel\\_F1 0.455 vs.\\ ${\\sim}$0.631), not evidence quality: on correctly predicted triples, \\method{}'s conditional Evi-F1 (0.807) approaches DREEAM's (0.834).\nCritically, \\method{} outputs \\emph{explicit} sentence citations whereas DREEAM's evidence is implicit attention weights---a qualitatively different and more interpretable form.\n\nTable~\\ref{tab:joint_vs_cond} provides a comprehensive view of joint vs.\\ conditional Evi-F1 across methods on the dev set, demonstrating that the decoupling between extraction and evidence quality is most extreme for GRPO (joint Evi-F1 of 0.012 despite conditional Evi-F1 of 0.850).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Conditional vs.\\ Joint Evi-F1 on DocRED dev set. Joint Evi-F1 penalizes incorrect relation predictions with zero evidence credit.}\n\\label{tab:joint_vs_cond}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1\\textsubscript{C}} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\nGRPO (lr=5e-6)    & 0.014 & 0.850 & 0.012 & 0.988 \\\\\nGRPO (lr=5e-5)    & 0.211 & 0.567 & 0.119 & 0.858 \\\\\nSFT baseline      & 0.406 & 0.798 & 0.322 & 0.712 \\\\\nRSFT flat-NLI     & 0.441 & 0.797 & 0.350 & 0.689 \\\\\nCED-reranker      & 0.415 & 0.821 & 0.341 & 0.598 \\\\\n\\rsft{} CED       & 0.468 & 0.816 & 0.381 & 0.639 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------------------\n\\subsection{Why Online RL Fails: Evidence--Extraction Decoupling}\n\\label{sec:grpo_failure}\n%------------------------------------------------------------------------------\n\nA central finding is that GRPO+QLoRA with evidence-quality rewards leads to catastrophic forgetting, regardless of reward type, learning rate, or group size.\nTable~\\ref{tab:rl_spectrum} presents the full online--offline RL spectrum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Online--offline RL spectrum on DocRED dev set. GRPO exhibits catastrophic forgetting across configurations. DPO avoids collapse but degrades below SFT. Only \\rsft{} improves over SFT.}\n\\label{tab:rl_spectrum}\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{RL Type} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{Catastrophic?} \\\\\n\\midrule\nGRPO $G$=4    & On-policy   & 0.014 & 0.850 & 0.988 & Yes \\\\\nGRPO $G$=8    & On-policy   & 0.031 & 0.816 & 0.981 & Yes \\\\\nDPO+CED       & Offline pref. & 0.325 & 0.786 & 0.683 & No (degraded) \\\\\nSFT            & No RL       & 0.406 & 0.798 & 0.712 & No \\\\\n\\textbf{\\rsft{}+CED} & Offline filtered & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} & No \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{GRPO Catastrophic Forgetting.}\nAll GRPO configurations exhibit the same pattern: the CED reward increases while rel\\_F1 collapses to near zero.\nWith $G$=4 (lr=5e-6), rel\\_F1 drops to 0.014 while Evi-F1 reaches 0.850---the model learns to cite extensive evidence but can no longer extract relations.\nIncreasing $G$ to 8 marginally delays the onset of forgetting (step ${\\sim}$15 vs.\\ ${\\sim}$10) but does not prevent it: best rel\\_F1 remains 0.031, far below SFT's 0.406.\nThis rules out advantage-estimation noise as the root cause and points to a structural incompatibility: QLoRA's rank-limited parameter space, when updated by RL gradients, preferentially optimizes the easier evidence dimension at the expense of structured extraction.\n\n\\paragraph{DPO as Intermediate Baseline.}\nDPO+CED (Table~\\ref{tab:rl_spectrum}) avoids catastrophic forgetting (rel\\_F1=0.325) but \\emph{degrades} below SFT (0.406), yielding $-$8.1pp.\nThis demonstrates that the problem is not simply online vs.\\ offline RL: DPO's token-level contrastive loss struggles with credit assignment over long structured outputs, and suppressing rejected candidates inadvertently penalizes correct extraction patterns.\nThe full spectrum GRPO (0.014--0.031) $\\ll$ DPO (0.325) $<$ SFT (0.406) $<$ \\rsft{} (0.468) shows that for document-level IE, \\ced{} is most effective as a data filter, not a learning objective.\n\n\\paragraph{Forgetting Dynamics.}\nAnalysis of 42 checkpoints across 3 GRPO configurations reveals a consistent three-phase pattern: (1)~\\emph{Decoupling onset} (steps 5--15): rel\\_F1 begins declining while Evi-F1 rises; (2)~\\emph{Acceleration} (steps 15--50): rel\\_F1 collapses below 0.05, reward saturates; (3)~\\emph{Plateau} (steps 50--100): rel\\_F1 oscillates near zero, Evi-F1 stabilizes at 0.80--0.85.\nAll configurations converge to a common attractor in the (low-rel\\_F1, high-Evi-F1) region, regardless of learning rate or group size.\n\n%------------------------------------------------------------------------------\n\\subsection{\\ced{} vs.\\ Flat-NLI Scoring}\n\\label{sec:ced_vs_flatnli}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:ced_ablation} presents the core ablation comparing \\ced{}-filtered vs.\\ flat-NLI-filtered \\rsft{}.\n\\ced{} yields statistically significant improvements across all three metrics (paired bootstrap, $p < 0.01$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CED vs.\\ flat-NLI as \\rsft{} filtering signal (DocRED dev set). Both \\rsft{} variants improve over SFT; CED significantly outperforms flat-NLI ($p < 0.01$ for all metrics, paired bootstrap).}\n\\label{tab:ced_ablation}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{$n_{\\text{train}}$} \\\\\n\\midrule\nSFT baseline                    & 0.406 & 0.798 & 0.712 & 12,151 \\\\\n\\rsft{} flat-NLI (A: 3ep)       & 0.441 & 0.795 & 0.695 & 2,845 \\\\\n\\rsft{} flat-NLI (B: 1ep)       & 0.438 & 0.797 & 0.689 & 2,845 \\\\\n\\rsft{} CED (s43: 3ep)          & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} & 2,718 \\\\\n\\rsft{} CED (r2b: 1ep)          & 0.449 & 0.813 & 0.661 & 2,718 \\\\\n\\midrule\n$\\Delta$ (CED best $-$ flat-NLI best)  & +2.71pp & +2.08pp & $-$5.64pp & --- \\\\\n$p$-value (paired bootstrap)           & 0.007 & 0.004 & 0.002 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe advantage of \\ced{} is concentrated in distractor-dense documents (distractor density $>$ 0.4), where the Evi-F1 gap expands to ${\\sim}$3.5pp, while in low-distractor documents the difference is negligible (${\\sim}$0.8pp, not significant).\nThis confirms that the contrastive margin is specifically effective at distinguishing true evidence from entity-sharing distractors---precisely the failure mode that flat-NLI scoring cannot address.\n\nBoth flat-NLI \\rsft{} variants still improve over SFT (+3.2--3.6pp rel\\_F1), indicating that \\emph{any} quality filtering helps, but \\ced{}'s contrastive design provides additional discriminative power where it matters most.\n\n%------------------------------------------------------------------------------\n\\subsection{\\ced{} Usage Modes: Training vs.\\ Inference}\n\\label{sec:ced_usage}\n%------------------------------------------------------------------------------\n\nTable~\\ref{tab:ced_modes} compares two usage modes of \\ced{}: as a training data filter (\\rsft{}) and as an inference-time reranker.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CED usage modes (DocRED dev set). CED as training signal (\\rsft{}) substantially outperforms CED as inference-time reranker.}\n\\label{tab:ced_modes}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{CED Usage} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{Extra Training} \\\\\n\\midrule\nSFT (no CED)                & 0.406 & 0.798 & 0.712 & --- \\\\\nCED-reranker (inference)     & 0.415 & 0.821 & 0.598 & None \\\\\n\\rsft{} flat-NLI (training)  & 0.441 & 0.797 & 0.689 & \\rsft{} \\\\\n\\rsft{} CED (training)       & \\textbf{0.468} & \\textbf{0.816} & 0.639 & \\rsft{} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCED-reranking achieves the lowest \\edcr{} (0.598) by directly selecting the candidate with the highest contrastive margin, but its rel\\_F1 gain is modest (+0.95pp over SFT).\nThis is because reranking cannot improve beyond the quality ceiling of the candidate pool---it selects the best existing output but does not shift the model's generation distribution.\nIn contrast, \\rsft{} with CED filtering gains +6.26pp rel\\_F1 by teaching the model to \\emph{generate} higher-quality outputs, confirming that CED is most effective as a training signal rather than a pure inference-time mechanism.\n\n%------------------------------------------------------------------------------\n\\subsection{\\edcr{} as a Diagnostic Metric}\n\\label{sec:edcr_analysis}\n%------------------------------------------------------------------------------\n\n\\paragraph{Cross-Method Diagnostic.}\nTable~\\ref{tab:edcr_diagnostic} presents \\edcr{} computed across all evidence-producing methods, revealing a clear gradient that aligns with the training paradigm.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-method \\edcr{} diagnostic (DocRED dev set). Methods sorted by \\edcr{} descending. \\edcr{} captures a systematic gradient from catastrophic GRPO to CED-reranker.}\n\\label{tab:edcr_diagnostic}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & \\textbf{$n_{\\text{distractor}}$} \\\\\n\\midrule\nGRPO ckpt-100 (lr=5e-6) & 0.014 & 0.850 & 0.988 & 12,675 \\\\\nGRPO ckpt-90 (lr=5e-5)  & 0.211 & 0.567 & 0.858 & 8,431 \\\\\nSFT baseline             & 0.406 & 0.798 & 0.712 & 10,113 \\\\\nRSFT flat-NLI            & 0.441 & 0.797 & 0.689 & 9,556 \\\\\nRSFT CED (r2b)           & 0.449 & 0.813 & 0.661 & 8,950 \\\\\nRSFT CED (s43)           & 0.468 & 0.816 & 0.639 & 8,475 \\\\\nCED-reranker             & 0.415 & 0.821 & 0.598 & 7,768 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\edcr{} gradient (0.988 $\\to$ 0.598) is monotonically related to the strength of evidence-quality supervision: GRPO outputs nearly all distractors, SFT has no evidence signal, flat-NLI provides weak filtering, CED provides contrastive filtering, and CED-reranker applies CED directly at inference.\nNotably, the cross-method Pearson correlation between \\edcr{} and Evi-F1 is only $r$=$-$0.42, confirming that \\edcr{} captures a dimension of evidence quality \\emph{not} measured by standard Evi-F1.\n\n\\paragraph{Human Validation.}\nTo validate \\edcr{} as a meaningful automatic metric, we conduct a human annotation study on 100 samples (25 per method: GRPO, SFT, RSFT flat-NLI, RSFT CED).\nThree annotators independently judge whether each cited sentence truly supports its corresponding relation (inter-annotator Cohen's $\\kappa$=0.72, substantial agreement).\nTable~\\ref{tab:human_edcr} presents the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Human validation of \\edcr{} (100 samples, 3 annotators, $\\kappa$=0.72). Auto \\edcr{} correlates with human distractor rate at Pearson $r$=0.62.}\n\\label{tab:human_edcr}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{\\edcr{}\\textsubscript{auto}} & \\textbf{Human dist.\\ rate} & $\\Delta$ & $n$ \\\\\n\\midrule\nGRPO ckpt-90     & 0.858 & 0.954 & $-$0.096 & 25 \\\\\nSFT              & 0.712 & 0.645 & +0.067 & 25 \\\\\nRSFT flat-NLI    & 0.695 & 0.608 & +0.087 & 25 \\\\\nRSFT CED         & 0.639 & 0.524 & +0.115 & 25 \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{Overall Pearson $r$} & \\multicolumn{3}{c}{0.62 ($p < 0.001$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall Pearson $r$=0.62 confirms that \\edcr{} is a meaningful proxy for human-judged evidence quality.\nThe ranking of methods is preserved perfectly between automatic and human evaluation.\nAuto \\edcr{} exhibits a slight positive bias (+6.8pp on average), because the entity-sharing heuristic is somewhat stricter than human judgment---some entity-sharing sentences are deemed partially supportive by human annotators.\nThe CED RSFT method shows the largest auto--human gap (0.115), suggesting that CED-trained models produce citations that are correct by the entity-sharing criterion but occasionally omit contextually relevant (though not gold-annotated) sentences.\n\n%------------------------------------------------------------------------------\n\\subsection{Generalization Experiments}\n\\label{sec:generalization}\n%------------------------------------------------------------------------------\n\n\\paragraph{Model Size Ablation.}\nTable~\\ref{tab:model_size} verifies that \\rsft{}+CED is effective across model scales from 1.7B to 8B parameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model size ablation (DocRED dev set). \\rsft{}+CED improves consistently across 1.7B--8B.}\n\\label{tab:model_size}\n\\begin{tabular}{@{}llcccr@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} & $\\Delta$\\textbf{rel\\_F1} \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-1.7B} & SFT      & 0.341 & 0.753 & 0.746 & --- \\\\\n                             & \\rsft{}+CED & 0.372 & 0.778 & 0.693 & +3.12pp \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-4B}   & SFT      & 0.406 & 0.798 & 0.712 & --- \\\\\n                             & \\rsft{}+CED & 0.468 & 0.816 & 0.639 & +6.26pp \\\\\n\\midrule\n\\multirow{2}{*}{Qwen3-8B}   & SFT      & 0.442 & 0.813 & 0.689 & --- \\\\\n                             & \\rsft{}+CED & 0.491 & 0.837 & 0.619 & +4.89pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe absolute improvement ranges from +3.1pp (1.7B) to +6.3pp (4B) to +4.9pp (8B).\nThe 4B model occupies a sweet spot: large enough to generate diverse high-quality candidates but small enough that SFT alone leaves substantial room for improvement.\nThe 8B model achieves the highest absolute performance (rel\\_F1=0.491) but has smaller relative gains because its SFT baseline is already stronger.\n\\edcr{} decreases consistently across all scales ($-$5.2 to $-$7.3pp), confirming the generality of CED-based evidence improvement.\n\n\\paragraph{Re-DocRED.}\nTable~\\ref{tab:redocred} shows results on Re-DocRED, which corrects ${\\sim}$25\\% false-negative annotations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{DocRED vs.\\ Re-DocRED (dev set). \\rsft{}+CED gains are preserved on cleaner annotations.}\n\\label{tab:redocred}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\n\\multirow{2}{*}{DocRED}    & SFT      & 0.406 & 0.798 & 0.712 \\\\\n                           & \\rsft{}+CED & 0.468 & 0.816 & 0.639 \\\\\n\\midrule\n\\multirow{2}{*}{Re-DocRED} & SFT      & 0.453 & 0.811 & 0.689 \\\\\n                           & \\rsft{}+CED & 0.509 & 0.838 & 0.602 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe \\rsft{}+CED improvement (+5.55pp on Re-DocRED vs.\\ +6.26pp on DocRED) is preserved, demonstrating that CED is not exploiting annotation noise.\nAll methods benefit from cleaner annotations, with \\edcr{} decreasing on Re-DocRED because some previously labeled distractors are reclassified as gold evidence.\n\n\\paragraph{top-$k$ Ablation.}\nTable~\\ref{tab:topk} examines the effect of CED filtering strictness.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{top-$k$ ablation for CED filtering (DocRED dev set). Stricter filtering ($k$=1) yields higher quality despite fewer training samples.}\n\\label{tab:topk}\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n\\textbf{top-$k$} & $n_{\\text{train}}$ & \\textbf{Mean CED} & \\textbf{rel\\_F1} & \\textbf{Evi-F1} & \\textbf{\\edcr{}$\\downarrow$} \\\\\n\\midrule\n1 & 2,718 & 0.668 & \\textbf{0.468} & \\textbf{0.816} & \\textbf{0.639} \\\\\n3 & 7,856 & 0.523 & 0.452 & 0.803 & 0.671 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nStrict filtering ($k$=1, 2,718 samples) outperforms relaxed filtering ($k$=3, 7,856 samples) across all metrics.\nThe additional samples from $k$=3 have systematically lower CED scores (mean 0.523 vs.\\ 0.668), introducing distractor-heavy training examples that dilute the quality signal.\nThis confirms the ``less is more'' principle for \\rsft{}: the SFT stage already provides broad coverage, and \\rsft{} needs only a small number of high-quality samples to calibrate evidence citation behavior.\n\n\\paragraph{NLI Model Ablation.}\nTable~\\ref{tab:nli_ablation} shows that replacing DeBERTa-v3-base (86M) with DeBERTa-v3-large (304M) yields marginal improvements (+0.38pp rel\\_F1), confirming that \\ced{}'s effectiveness stems from the contrastive design rather than the NLI model's capacity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{NLI model ablation for CED scoring. Larger NLI model provides marginal gains.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{NLI Model} & \\textbf{Params} & \\textbf{Disc.\\ Acc} & \\textbf{\\rsft{} rel\\_F1} & \\textbf{\\rsft{} Evi-F1} \\\\\n\\midrule\nDeBERTa-v3-base  & 86M  & 0.815 & 0.468 & 0.816 \\\\\nDeBERTa-v3-large & 304M & 0.847 & 0.472 & 0.819 \\\\\n\\midrule\n$\\Delta$ & --- & +0.032 & +0.38pp & +0.33pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe top-1 candidate selection agrees between base and large models on 89\\% of documents; the 11\\% disagreements produce only marginal downstream differences, lowering the computational barrier for adopting \\method{}.\n\n\\paragraph{Baseline Comparison with Evidence Methods.}\nTable~\\ref{tab:evidence_comparison} contextualizes \\method{} against encoder-based evidence methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence baseline comparison (dev set). \\method{} is the first generative LLM method with explicit evidence; the Evi-F1\\textsubscript{J} gap vs.\\ encoders is driven by extraction accuracy, not evidence quality.}\n\\label{tab:evidence_comparison}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Type} & \\textbf{rel\\_F1} & \\textbf{Evi-F1\\textsubscript{J}} & \\textbf{Evidence Form} \\\\\n\\midrule\nDREEAM      & Encoder  & 0.631 & 0.572 & Attention threshold \\\\\nSAIS        & Encoder  & 0.610 & 0.554 & Attention threshold \\\\\nLMRC        & Gen.\\ LLM & 0.607 & ---   & None \\\\\nSFT baseline & Gen.\\ LLM & 0.406 & 0.322 & Explicit citation \\\\\n\\textbf{\\method{}} & Gen.\\ LLM & 0.468 & 0.381 & Explicit citation \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n%==============================================================================\n\n\\paragraph{Why \\rsft{} Succeeds Where RL Fails.}\nThe evidence--extraction decoupling phenomenon reveals that document-level IE presents unique challenges for on-policy RL: (1) QLoRA's rank-limited parameters are easily overwritten by RL gradients that preferentially optimize the more gradient-accessible evidence dimension; (2) evidence-quality rewards provide stronger gradients than extraction-accuracy signals, causing asymmetric optimization; (3) the combinatorial output space of multiple triples with evidence makes credit assignment intractable for policy-gradient methods.\n\\rsft{} bypasses all three issues by using standard supervised learning on curated data, inheriting the stability of SFT while benefiting from CED's quality signal.\n\n\\paragraph{Limitations of \\edcr{}.}\nEntity-sharing is an operationalized proxy for distractor sentences, not a perfect definition.\nThe auto--human gap of +6.8pp (Table~\\ref{tab:human_edcr}) indicates that some entity-sharing sentences provide partial contextual support.\nAdditionally, \\edcr{} does not capture non-entity-sharing distractors (sentences that are irrelevant but happen not to mention target entities).\nWe recommend using \\edcr{} as a complementary diagnostic alongside Evi-F1, not as a replacement.\n\n\\paragraph{Extraction Gap vs.\\ Encoders.}\n\\method{}'s primary limitation is the extraction accuracy gap compared to encoder-based methods (rel\\_F1 0.455 vs.\\ DREEAM's ${\\sim}$0.631).\nThis gap is inherent to the generative paradigm under current model scales and is not specific to our method---LMRC (LLaMA-3.1-8B) achieves 0.607 with 2$\\times$ parameters and no evidence output.\nAs LLM capabilities scale, this gap is expected to narrow, making evidence generation increasingly valuable.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented \\method{}, the first LLM-based document-level RE framework that jointly generates relation triples and verifiable sentence-level evidence.\nOur core technical contribution, \\ced{}, provides a contrastive evidence scoring mechanism that is effective as an offline data quality filter but causes catastrophic forgetting when used as an online RL reward---revealing a previously unreported evidence--extraction decoupling phenomenon in GRPO+QLoRA for structured IE.\nThe proposed \\edcr{} metric, validated by human annotation ($r$=0.62), captures a systematic failure mode of evidence citation invisible to standard Evi-F1.\nExperiments across three model scales, two dataset variants, multiple RL paradigms, and extensive ablations demonstrate the robustness of our approach.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "505c6351-6ef9-4989-aaae-68864fb8bb8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "472f67c7-fd73-404b-981d-899291825180",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ML research paper for dream session",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Tool call

_source line 25 · 2026-05-15T13:56:59.240Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YLNw4vKqsbWtJvy1hS8292`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "472f67c7-fd73-404b-981d-899291825180",
  "isSidechain": false,
  "requestId": "req_011Cb4UGTbDdVuNB7K1Uau9C",
  "type": "assistant",
  "uuid": "3aa1942d-8a18-4006-b9f5-03fb205ed088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxZj6WXLu9K4xTnGawQf4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11856,
      "cache_read_input_tokens": 49491,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 49491,
          "cache_creation_input_tokens": 11856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11856
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

_source line 26 · 2026-05-15T13:57:00.744Z_

<details><summary>↩ Tool result · `toolu_01YLNw4vKqsbWtJvy1hS8292`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
Overfull \hbox (21.71194pt too wide) in paragraph at lines 32--39
\T1/ptm/m/n/10 document-level re-la-tion ex-trac-tion (DocRE), yet no ex-ist-in
g LLM ap-proach pro-duces ver-i-fi-able evidence---
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (12.91803pt too wide) in paragraph at lines 76--81
\T1/ptm/m/n/10.95 trac-tion per-for-mance. DREEAM pro-vides ev-i-dence through 
attention-weight thresh-old-ing over a RoBERTa-

Overfull \hbox (18.32872pt too wide) in paragraph at lines 76--81
\T1/ptm/m/n/10.95 large en-coder, achiev-ing Evi-F1$[]$=0.573 on Do-cRED. SAIS 
fol-lows a sim-i-lar paradigm (Evi-F1$[]$=0.557).
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]
Overfull \hbox (14.6579pt too wide) in paragraph at lines 166--167
 []\T1/ptm/b/n/10.95 Baselines.[] \T1/ptm/m/n/10.95 We com-pare against: DREEAM
 (RoBERTa-large, attention-based ev-i-dence), SAIS (RoBERTa-

LaTeX Warning: Reference `tab:main_results' on page 4 undefined on input line 1
73.


LaTeX Warning: Reference `tab:joint_vs_cond' on page 4 undefined on input line 
200.


LaTeX Warning: Reference `tab:rl_spectrum' on page 4 undefined on input line 22
7.

[4]

LaTeX Warning: Reference `tab:rl_spectrum' on page 5 undefined on input line 25
4.


LaTeX Warning: Reference `tab:ced_ablation' on page 5 undefined on input line 2
67.


LaTeX Warning: Reference `tab:ced_modes' on page 5 undefined on input line 301.


[5]

LaTeX Warning: Reference `tab:edcr_diagnostic' on page 6 undefined on input lin
e 330.


LaTeX Warning: Reference `tab:human_edcr' on page 6 undefined on input line 358
.

[6]

LaTeX Warning: Reference `tab:model_size' on page 7 undefined on input line 390
.


LaTeX Warning: Reference `tab:redocred' on page 7 undefined on input line 419.


LaTeX Warning: Reference `tab:topk' on page 7 undefined on input line 443.


LaTeX Warning: Reference `tab:nli_ablation' on page 7 undefined on input line 4
65.

[7]

LaTeX Warning: Reference `tab:evidence_comparison' on page 8 undefined on input
 line 487.


LaTeX Warning: Reference `tab:human_edcr' on page 8 undefined on input line 518
.

[8] [9] [10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (10 pages, 169687 bytes).
Transcript written on paper.log.
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]
Overfull \hbox (14.6579pt too wide) in paragraph at lines 166--167
 []\T1/ptm/b/n/10.95 Baselines.[] \T1/ptm/m/n/10.95 We com-pare against: DREEAM
 (RoBERTa-large, attention-based ev-i-dence), SAIS (RoBERTa-
[4] [5] [6] [7] [8] [9] [10] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (10 pages, 171763 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3aa1942d-8a18-4006-b9f5-03fb205ed088",
  "isSidechain": false,
  "promptId": "32e50b4a-4698-45bc-b7f1-1f742b455c90",
  "type": "user",
  "uuid": "59c2df3f-b11b-4970-910c-8b5e0ebe1eb4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (21.71194pt too wide) in paragraph at lines 32--39\n\\T1/ptm/m/n/10 document-level re-la-tion ex-trac-tion (DocRE), yet no ex-ist-in\ng LLM ap-proach pro-duces ver-i-fi-able evidence---\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (12.91803pt too wide) in paragraph at lines 76--81\n\\T1/ptm/m/n/10.95 trac-tion per-for-mance. DREEAM pro-vides ev-i-dence through \nattention-weight thresh-old-ing over a RoBERTa-\n\nOverfull \\hbox (18.32872pt too wide) in paragraph at lines 76--81\n\\T1/ptm/m/n/10.95 large en-coder, achiev-ing Evi-F1$[]$=0.573 on Do-cRED. SAIS \nfol-lows a sim-i-lar paradigm (Evi-F1$[]$=0.557).\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]\nOverfull \\hbox (14.6579pt too wide) in paragraph at lines 166--167\n []\\T1/ptm/b/n/10.95 Baselines.[] \\T1/ptm/m/n/10.95 We com-pare against: DREEAM\n (RoBERTa-large, attention-based ev-i-dence), SAIS (RoBERTa-\n\nLaTeX Warning: Reference `tab:main_results' on page 4 undefined on input line 1\n73.\n\n\nLaTeX Warning: Reference `tab:joint_vs_cond' on page 4 undefined on input line \n200.\n\n\nLaTeX Warning: Reference `tab:rl_spectrum' on page 4 undefined on input line 22\n7.\n\n[4]\n\nLaTeX Warning: Reference `tab:rl_spectrum' on page 5 undefined on input line 25\n4.\n\n\nLaTeX Warning: Reference `tab:ced_ablation' on page 5 undefined on input line 2\n67.\n\n\nLaTeX Warning: Reference `tab:ced_modes' on page 5 undefined on input line 301.\n\n\n[5]\n\nLaTeX Warning: Reference `tab:edcr_diagnostic' on page 6 undefined on input lin\ne 330.\n\n\nLaTeX Warning: Reference `tab:human_edcr' on page 6 undefined on input line 358\n.\n\n[6]\n\nLaTeX Warning: Reference `tab:model_size' on page 7 undefined on input line 390\n.\n\n\nLaTeX Warning: Reference `tab:redocred' on page 7 undefined on input line 419.\n\n\nLaTeX Warning: Reference `tab:topk' on page 7 undefined on input line 443.\n\n\nLaTeX Warning: Reference `tab:nli_ablation' on page 7 undefined on input line 4\n65.\n\n[7]\n\nLaTeX Warning: Reference `tab:evidence_comparison' on page 8 undefined on input\n line 487.\n\n\nLaTeX Warning: Reference `tab:human_edcr' on page 8 undefined on input line 518\n.\n\n[8] [9] [10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 169687 bytes).\nTranscript written on paper.log.\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [2] [3]\nOverfull \\hbox (14.6579pt too wide) in paragraph at lines 166--167\n []\\T1/ptm/b/n/10.95 Baselines.[] \\T1/ptm/m/n/10.95 We com-pare against: DREEAM\n (RoBERTa-large, attention-based ev-i-dence), SAIS (RoBERTa-\n[4] [5] [6] [7] [8] [9] [10] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 171763 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3aa1942d-8a18-4006-b9f5-03fb205ed088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T13:57:11.470Z_

编译成功，PDF 10 页，无错误。所有 12 个实验均已覆盖：

- **Table 1**: Test set 主结果（实验 2）
- **Table 2**: Joint vs Conditional Evi-F1（实验 12）
- **Table 3**: Online-Offline RL 光谱（实验 8 GRPO G=8 + 实验 9 DPO）
- **Table 4**: CED vs flat-NLI 消融（实验 1）
- **Table 5**: CED 使用模式对比（实验 5 reranker）
- **Table 6**: Cross-method EDCR 诊断（实验 3）
- **Table 7**: EDCR 人工标注验证（实验 10）
- **Table 8**: 模型规模消融 1.7B/4B/8B（实验 6）
- **Table 9**: DocRED vs Re-DocRED（实验 7）
- **Table 10**: top-k 消融（实验 7b）
- **Table 11**: NLI 模型消融（实验 11）
- **Table 12**: Evidence baseline 对比含 DREEAM/SAIS 复现（实验 4）

GRPO forgetting 动态分析（实验 10b）在 §4.3 forgetting dynamics 段落中叙述。所有数字均直接取自 `experiment_data.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59c2df3f-b11b-4970-910c-8b5e0ebe1eb4",
  "isSidechain": false,
  "requestId": "req_011Cb4UGqxsd1GbufXHKrKaU",
  "type": "assistant",
  "uuid": "97e0e723-3c92-42dd-b6c3-5a9134d30d9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfZa9C4P7P2TjD68Griqj2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4305,
      "cache_read_input_tokens": 61347,
      "output_tokens": 393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4305,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 393,
          "cache_read_input_tokens": 61347,
          "cache_creation_input_tokens": 4305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4305
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T132059 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "97e0e723-3c92-42dd-b6c3-5a9134d30d9d",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete ML research paper for dream session",
  "sessionId": "a0c1155d-3d78-4078-907e-86825dce7a7c"
}
```

---
