# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/e8bbcfe2-4536-4e05-a4c5-615fca01f226.jsonl`
- **Structured JSON:** [`5cca3c959a10cebb16c4.json`](../../sessions/5c/5cca3c959a10cebb16c4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T03:00:57.360Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T03:00:57.360Z",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：C2 从 \"significant asymmetry\" 调整为 \"remarkably consistent effect size across architectures\n(6.6±0.9pp) despite varying statistical power\"——强调 effect size stability 而非 p-value。\n引用 Cumming (2014) \"new statistics\" 框架: effect size + CI 优于 NHST。\nC1 (detectability) 升级为主 claim，C2 降为 strong supporting evidence。\nTrack 1 only 的贡献靠深度弥补: layer-wise 分析 + confound exclusion pipeline (token overlap +\nCOMET ablation) 作为方法论贡献。RC8 明确限定为 \"correlational evidence consistent with H1\"，\ncausal verification 列为 future work。论文定位: phenomenon characterization + methodology，\n仍 ICLR-viable 但需 supplementary experiments 充实 appendix（更多 ablation、error analysis）。\nTrack 2 SAE 若完成但 Jaccard < 0.10，可作为 \"negative/inconclusive result\" 放 appendix，\n反而增加诚实度和完整度。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T03:00:57.366Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T03:00:57.366Z",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-22T03:00:57.390Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：C2 从 "significant asymmetry" 调整为 "remarkably consistent effect size across architectures
(6.6±0.9pp) despite varying statistical power"——强调 effect size stability 而非 p-value。
引用 Cumming (2014) "new statistics" 框架: effect size + CI 优于 NHST。
C1 (detectability) 升级为主 claim，C2 降为 strong supporting evidence。
Track 1 only 的贡献靠深度弥补: layer-wise 分析 + confound exclusion pipeline (token overlap +
COMET ablation) 作为方法论贡献。RC8 明确限定为 "correlational evidence consistent with H1"，
causal verification 列为 future work。论文定位: phenomenon characterization + methodology，
仍 ICLR-viable 但需 supplementary experiments 充实 appendix（更多 ablation、error analysis）。
Track 2 SAE 若完成但 Jaccard < 0.10，可作为 "negative/inconclusive result" 放 appendix，
反而增加诚实度和完整度。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "54295829-2110-4ee0-b5c1-f86ba5dada10",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T03:00:57.389Z_

```json
{
  "parentUuid": "54295829-2110-4ee0-b5c1-f86ba5dada10",
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
  "uuid": "bc99c61a-2cc5-4808-8772-68f5247491e0",
  "timestamp": "2026-05-22T03:00:57.389Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T03:00:57.389Z_

```json
{
  "parentUuid": "bc99c61a-2cc5-4808-8772-68f5247491e0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f61bb01e-280e-49da-bed5-0f85441a3a34",
  "timestamp": "2026-05-22T03:00:57.389Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
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
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Assistant

_source line 7 · 2026-05-22T03:00:59.704Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f61bb01e-280e-49da-bed5-0f85441a3a34",
  "isSidechain": false,
  "requestId": "req_011CbGruchYNcJiLWbqxBdp9",
  "type": "assistant",
  "uuid": "4ca0aa8b-7b25-44a9-8d05-9ad338247e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnyivF6QRWZ7L4TmnHGsXk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11413,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11413
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

_source line 8 · 2026-05-22T03:01:01.183Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LVx9jzoxGuqEB1yUmcxLNk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca0aa8b-7b25-44a9-8d05-9ad338247e2c",
  "isSidechain": false,
  "requestId": "req_011CbGruchYNcJiLWbqxBdp9",
  "type": "assistant",
  "uuid": "22811f91-f1aa-439f-92af-2e0c90e594e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnyivF6QRWZ7L4TmnHGsXk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11413,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11413
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

_source line 9 · 2026-05-22T03:01:01.194Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YMbYDgw4XVz4bYEVNJXDgE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22811f91-f1aa-439f-92af-2e0c90e594e2",
  "isSidechain": false,
  "requestId": "req_011CbGruchYNcJiLWbqxBdp9",
  "type": "assistant",
  "uuid": "8082dcfd-2d63-4329-a8ac-41c82332852e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnyivF6QRWZ7L4TmnHGsXk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11413,
      "cache_read_input_tokens": 11841,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 200,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11413
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

_source line 10 · 2026-05-22T03:01:01.203Z_

<details><summary>↩ Tool result · `toolu_01YMbYDgw4XVz4bYEVNJXDgE`</summary>

```text
1	# Paper Framing — clkc_mech_interp
2	
3	> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)
4	
5	## Core Insight
6	
7	多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 "entity-centric factual conflicts 中 linguistic affinity 决定冲突解决" 提供了首个**机制层面的解释**。
8	
9	**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。
10	
11	## Narrative Structure
12	
13	**现象驱动的机制解释**（非 "applying X to Y"）：
14	
15	1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释
16	2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？
17	3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预
18	
19	**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界
20	
21	## Competing Hypotheses (pre-registered)
22	
23	**H1 — English-anchored universal detection**:
24	冲突检测信号本身是 language-independent 的（"是否存在冲突" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。
25	- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)
26	- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）
27	
28	**H2 — Language-pair-specific encoding**:
29	冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。
30	- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late
31	- 预测: 探针迁移准确率与语言对 typological distance 强相关
32	
33	**MVP 证据倾向**:
34	当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。
35	
36	## Core Claims
37	
38	### Claim 1: Cross-lingual conflict detectability
39	**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。
40	**Evidence needed**:
41	- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)
42	- Permutation test p < 0.001 ✅ (all directions)
43	- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)
44	**Status**: MVP 已验证 ✅
45	
46	### Claim 2: Asymmetric cross-lingual transfer
47	**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。
48	**Evidence needed**:
49	- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):
50	  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅
51	  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️
52	- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)
53	- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)
54	- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)
55	**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)
56	
57	### Claim 3: Direction-dependent non-linear components
58	**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。
59	**Evidence needed**:
60	- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)
61	- MLP 不使用 test set 做 early stopping ✅ (已修复)
62	- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)
63	- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)
64	**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)
65	
66	### Claim 4: Layer-wise conflict signal structure
67	**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。
68	**Evidence needed**:
69	- Layer-wise probe accuracy curves for ≥3 models ❌
70	- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌
71	- 与 "Lost in Multilinguality" 的 language transition 层对比 ❌
72	**Status**: 未验证 ❌
73	
74	### Claim 5: Cross-lingual SAE conflict features (Track 2)
75	**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。
76	**Evidence needed**:
77	- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌
78	- LangFIR random-token filtering 控制 ❌
79	- Cross-lingual feature Jaccard 分析 ❌
80	**Status**: 未开始 ❌
81	
82	### Claim 6: Cross-lingual conflict steering (Track 3)
83	**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。
84	**Evidence needed**:
85	- SpARE 框架跨语言扩展 ❌
86	- Monolingual → cross-lingual steering transfer ❌
87	- Steering effectiveness vs linguistic distance correlation ❌
88	**Status**: 未开始 ❌ (依赖 Track 2)
89	
90	## Anticipated Reviewer Concerns
91	
92	### RC1: Translation quality confound [RESOLVED ✅]
93	**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败
94	**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。
95	**Remaining**: Llama test COMET 完成后重复此分析确认一致性。
96	
97	### RC2: Token overlap confound [RESOLVED ✅]
98	**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动
99	**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**
100	
101	### RC3: Model coverage insufficient [HIGH]
102	**Concern**: 只有 2 个模型，无法声称 "架构无关"
103	**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性
104	**Experiment**: P0 — additional model verification
105	
106	### RC4: Dataset size and diversity [MEDIUM]
107	**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对
108	**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）
109	**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)
110	
111	### RC5: Linear probe expressiveness [LOW]
112	**Concern**: 线性探针可能遗漏复杂非线性信号
113	**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化
114	**Experiment**: Done — MLP vs Linear comparison
115	
116	### RC6: SAE base/instruct mismatch [MEDIUM]
117	**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配
118	**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证
119	**Experiment**: Track 2 设计已考虑
120	
121	### RC7: Steering failure precedent [MEDIUM]
122	**Concern**: "Interpretability without actionability" 证明 SAE steering 可能完全无效
123	**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式
124	**Experiment**: Track 3 包含 negative result framing
125	
126	### RC8: Causal claims without intervention [HIGH]
127	**Concern**: 探针只证明信号可检测，不证明因果关系
128	**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制
129	**Experiment**: Track 3 steering + representation steering (P1)
130	
131	## Paper Structure (Tentative)
132	
133	1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview
134	2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features
135	3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering
136	4. **Experiments & Results**:
137	   - 4.1 Cross-lingual conflict detectability (C1)
138	   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls
139	   - 4.3 Non-linear components (C3) + layer-wise structure (C4)
140	   - 4.4 SAE feature analysis (C5) [if Track 2 ready]
141	   - 4.5 Steering experiments (C6) [if Track 3 ready]
142	5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR
143	6. **Conclusion**
144	
145	## Scope Control
146	
147	**投稿最低要求 (must-have for submission)**:
148	- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)
149	- Claim 4 partially supported (layer-wise analysis on ≥2 models)
150	- ≥3 model architectures
151	- ≥2 language pairs (EN-ZH + one more)
152	- Token overlap control
153	- COMET translation quality validation
154	
155	**理想状态 (nice-to-have)**:
156	- Track 2 SAE analysis (Claim 5)
157	- Track 3 steering (Claim 6)
158	- 5+ language pairs covering multiple typological families
159	- Full CKA/SVCCA layer analysis
160	
161	**不做 (out of scope)**:
162	- 10-language full CLEAR replication
163	- Custom SAE training
164	- MoE model analysis
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8082dcfd-2d63-4329-a8ac-41c82332852e",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "b698b022-32bc-4153-8d2c-0e5021fa1248",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper_framing.md",
      "content": "# Paper Framing — clkc_mech_interp\n\n> 最后更新: 2026-05-22 | 目标: ICLR 2027 (DDL ~2026-09-24)\n\n## Core Insight\n\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致（Llama-3.1-8B 与 Qwen3-8B）。这为 CLEAR (Zhao et al. 2026) 发现的 \"entity-centric factual conflicts 中 linguistic affinity 决定冲突解决\" 提供了首个**机制层面的解释**。\n\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\n\n## Narrative Structure\n\n**现象驱动的机制解释**（非 \"applying X to Y\"）：\n\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity（而非 resource abundance）决定跨语言冲突解决，但未提供机制解释\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？是 language-universal 还是 language-specific？为什么 similarity 起决定作用？\n3. **Our answer**: 通过残差流探针、SAE 特征分析、激活干预三条互补分析轨道，揭示冲突检测信号的跨语言结构——是否共享、在哪些层出现、能否用于干预\n\n**Secondary framing**: SAE-based mechanistic interpretability 工具在跨语言条件下的 stress test——probing / SAE / steering 三种工具的跨语言适用性边界\n\n## Competing Hypotheses (pre-registered)\n\n**H1 — English-anchored universal detection**:\n冲突检测信号本身是 language-independent 的（\"是否存在冲突\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\n\n**H2 — Language-pair-specific encoding**:\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\n\n**MVP 证据倾向**:\n当前双模型结果倾向 **H1 的变体**——ZH→EN 迁移（71-72%）显著强于 EN→ZH（64-65%），暗示冲突信号以英语表征空间为锚点编码。非线性成分（MLP EN→ZH +9.2pp vs linear）提示 EN→ZH 方向的跨语言映射更复杂。\n\n## Core Claims\n\n### Claim 1: Cross-lingual conflict detectability\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\n**Evidence needed**:\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\n- Permutation test p < 0.001 ✅ (all directions)\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\n**Status**: MVP 已验证 ✅\n\n### Claim 2: Asymmetric cross-lingual transfer\n**Statement**: 跨语言探针迁移呈方向一致的不对称：ZH→EN 迁移强于 EN→ZH（~7.2pp），效果量跨架构高度一致（Llama 显著，Qwen 方向一致但未达显著）。\n**Evidence needed**:\n- Bootstrap CI for asymmetry gap (corrected, plan_099 ✅):\n  - Llama: +7.22pp, CI [1.1%, 13.6%] — 排除零但 borderline ✅\n  - Qwen: +7.18pp, CI [-1.2%, 13.4%] — 含零，方向一致 ⚠️\n- ≥2 models show consistent effect size ✅ (7.22pp vs 7.18pp)\n- Token overlap analysis 排除词汇重叠驱动的虚假迁移 ✅ (plan_101 完成: per-sample Jaccard 3-4%, Qwen 无相关 p>0.4, Llama 显著负相关 r=-0.15 p=0.012 — RC2 排除)\n- ≥1 additional model architecture 验证跨架构一致性 ❌ (planned P0)\n**Status**: 初步验证 ⚠️ (需补 token overlap + 第三模型)\n\n### Claim 3: Direction-dependent non-linear components\n**Statement**: 跨语言冲突信号的弱迁移方向（EN→ZH）包含方向依赖的非线性成分，MLP 探针在该方向提升最大。跨架构一致方向但幅度不同（Llama +9.2pp single-seed / ~+4.7pp bootstrap-corrected, Qwen +2.3pp），暗示非线性成分与模型的跨语言对齐程度相关。\n**Evidence needed**:\n- MLP vs linear probe comparison on ≥2 models ✅ (both show EN→ZH direction gains)\n- MLP 不使用 test set 做 early stopping ✅ (已修复)\n- 控制实验排除 MLP 过拟合 ❌ (需 train/test accuracy gap 分析)\n- 解释跨架构幅度差异 (Llama 4x > Qwen) ❌ (可能与 Qwen 更强的跨语言对齐有关——ZH 训练数据占比更高)\n**Status**: 初步验证 ⚠️ (方向一致但幅度差异需解释)\n\n### Claim 4: Layer-wise conflict signal structure\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\n**Evidence needed**:\n- Layer-wise probe accuracy curves for ≥3 models ❌\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\n- 与 \"Lost in Multilinguality\" 的 language transition 层对比 ❌\n**Status**: 未验证 ❌\n\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\n**Evidence needed**:\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\n- LangFIR random-token filtering 控制 ❌\n- Cross-lingual feature Jaccard 分析 ❌\n**Status**: 未开始 ❌\n\n### Claim 6: Cross-lingual conflict steering (Track 3)\n**Statement**: 通过 SAE 特征干预可以定向操控跨语言冲突解决行为。\n**Evidence needed**:\n- SpARE 框架跨语言扩展 ❌\n- Monolingual → cross-lingual steering transfer ❌\n- Steering effectiveness vs linguistic distance correlation ❌\n**Status**: 未开始 ❌ (依赖 Track 2)\n\n## Anticipated Reviewer Concerns\n\n### RC1: Translation quality confound [RESOLVED ✅]\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\n\n### RC2: Token overlap confound [RESOLVED ✅]\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\n\n### RC3: Model coverage insufficient [HIGH]\n**Concern**: 只有 2 个模型，无法声称 \"架构无关\"\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\n**Experiment**: P0 — additional model verification\n\n### RC4: Dataset size and diversity [MEDIUM]\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\n\n### RC5: Linear probe expressiveness [LOW]\n**Concern**: 线性探针可能遗漏复杂非线性信号\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\n**Experiment**: Done — MLP vs Linear comparison\n\n### RC6: SAE base/instruct mismatch [MEDIUM]\n**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配\n**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证\n**Experiment**: Track 2 设计已考虑\n\n### RC7: Steering failure precedent [MEDIUM]\n**Concern**: \"Interpretability without actionability\" 证明 SAE steering 可能完全无效\n**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式\n**Experiment**: Track 3 包含 negative result framing\n\n### RC8: Causal claims without intervention [HIGH]\n**Concern**: 探针只证明信号可检测，不证明因果关系\n**Mitigation**: Track 3 steering 实验提供因果证据；Track 1 permutation test 提供统计控制\n**Experiment**: Track 3 steering + representation steering (P1)\n\n## Paper Structure (Tentative)\n\n1. **Introduction**: CLEAR gap → mechanistic question → H1 vs H2 → three-track approach → key findings preview\n2. **Related Work**: Monolingual conflict mechanisms → Cross-lingual processing → SAE steering (successes & failures) → Cross-lingual SAE features\n3. **Method**: Data construction (ConflictQA + translation + verification pipeline) → Track 1 probing → Track 2 SAE analysis → Track 3 steering\n4. **Experiments & Results**:\n   - 4.1 Cross-lingual conflict detectability (C1)\n   - 4.2 Asymmetric transfer analysis (C2) + token overlap controls\n   - 4.3 Non-linear components (C3) + layer-wise structure (C4)\n   - 4.4 SAE feature analysis (C5) [if Track 2 ready]\n   - 4.5 Steering experiments (C6) [if Track 3 ready]\n5. **Discussion**: H1 vs H2 resolution → mechanism implications → limitations → connection to CLEAR\n6. **Conclusion**\n\n## Scope Control\n\n**投稿最低要求 (must-have for submission)**:\n- Claims 1-3 fully supported (cross-lingual detectability + asymmetry + non-linearity)\n- Claim 4 partially supported (layer-wise analysis on ≥2 models)\n- ≥3 model architectures\n- ≥2 language pairs (EN-ZH + one more)\n- Token overlap control\n- COMET translation quality validation\n\n**理想状态 (nice-to-have)**:\n- Track 2 SAE analysis (Claim 5)\n- Track 3 steering (Claim 6)\n- 5+ language pairs covering multiple typological families\n- Full CKA/SVCCA layer analysis\n\n**不做 (out of scope)**:\n- 10-language full CLEAR replication\n- Custom SAE training\n- MoE model analysis\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  },
  "sourceToolAssistantUUID": "8082dcfd-2d63-4329-a8ac-41c82332852e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifact…",
  "leafUuid": "b698b022-32bc-4153-8d2c-0e5021fa1248",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Tool result

_source line 13 · 2026-05-22T03:01:01.493Z_

<details><summary>↩ Tool result · `toolu_01LVx9jzoxGuqEB1yUmcxLNk`</summary>

```text
1	[
2	  {
3	    "name": "第三模型架构验证",
4	    "description": "在 Gemma-2-9B-IT 上重复完整探针实验，验证 ~7.2pp 不对称性跨架构一致性",
5	    "results": {
6	      "model": "Gemma-2-9B-IT",
7	      "en_en_bal_acc": 0.731,
8	      "zh_zh_bal_acc": 0.694,
9	      "en_zh_bal_acc": 0.641,
10	      "zh_en_bal_acc": 0.695,
11	      "asymmetry_gap_pp": 5.4,
12	      "bootstrap_ci_95": "[-0.8%, 11.6%]",
13	      "bootstrap_significant": false,
14	      "positive_iterations_of_100": 94,
15	      "permutation_p_en_en": "<0.001",
16	      "permutation_p_zh_zh": "<0.001",
17	      "permutation_p_en_zh": 0.006,
18	      "permutation_p_zh_en": "<0.001",
19	      "best_layer_en": 23,
20	      "best_layer_zh": 20,
21	      "best_layer_depth_pct": 0.72,
22	      "mlp_en_zh_gain_pp": 3.1,
23	      "mlp_zh_en_gain_pp": 0.8,
24	      "token_overlap_jaccard_mean": 0.035,
25	      "token_overlap_correlation_p": 0.31
26	    },
27	    "tables": [
28	      {
29	        "caption": "Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, n=100 bootstrap)",
30	        "columns": [
31	          "Train→Test",
32	          "Bal. Acc (%)",
33	          "95% CI",
34	          "Perm. p"
35	        ],
36	        "rows": [
37	          [
38	            "EN→EN",
39	            "73.1",
40	            "[70.2, 76.0]",
41	            "<0.001"
42	          ],
43	          [
44	            "ZH→ZH",
45	            "69.4",
46	            "[66.3, 72.5]",
47	            "<0.001"
48	          ],
49	          [
50	            "EN→ZH",
51	            "64.1",
52	            "[59.9, 68.3]",
53	            "0.006"
54	          ],
55	          [
56	            "ZH→EN",
57	            "69.5",
58	            "[65.7, 73.3]",
59	            "<0.001"
60	          ],
61	          [
62	            "Gap (ZH→EN − EN→ZH)",
63	            "+5.4",
64	            "[-0.8, 11.6]",
65	            "—"
66	          ]
67	        ]
68	      },
69	      {
70	        "caption": "Cross-architecture asymmetry consistency (all three models)",
71	        "columns": [
72	          "Model",
73	          "Gap (pp)",
74	          "95% CI",
75	          "Significant?",
76	          "Direction"
77	        ],
78	        "rows": [
79	          [
80	            "Llama-3.1-8B",
81	            "7.22",
82	            "[1.1, 13.6]",
83	            "Yes (borderline)",
84	            "ZH→EN > EN→ZH"
85	          ],
86	          [
87	            "Qwen3-8B",
88	            "7.18",
89	            "[-1.2, 13.4]",
90	            "No",
91	            "ZH→EN > EN→ZH"
92	          ],
93	          [
94	            "Gemma-2-9B-IT",
95	            "5.4",
96	            "[-0.8, 11.6]",
97	            "No",
98	            "ZH→EN > EN→ZH"
99	          ],
100	          [
101	            "Mean ± SD",
102	            "6.60 ± 1.04",
103	            "—",
104	            "1/3 sig, 3/3 consistent",
105	            "—"
106	          ]
107	        ]
108	      }
109	    ],
110	    "figures": [],
111	    "analysis": "三模型 effect size: 7.22, 7.18, 5.4 → mean=6.60, SD=1.04pp。Cochran's Q test 跨\n模型一致性 p=0.68（无显著异质性）。Gemma 偏低 1.8pp 可解释为架构效应而非方向不一致。\n关键叙事: \"In all three architectures spanning two distinct design families (GQA vs\nparallel attention), the ZH→EN transfer consistently exceeded EN→ZH, with a pooled\neffect of 6.6pp (range 5.4–7.2). Only Llama reached conventional significance\n(p<0.05), but the I² heterogeneity statistic of 0% and consistent directionality\nacross 3/3 models provides stronger evidence than any single p-value.\"\nCohen's d range: 0.32-0.48 (small-to-medium)。对 Cumming (2014) framing 足够。\nC2 claim 降级为: \"consistent directional asymmetry with stable effect size\" 而非\n\"statistically significant asymmetry\"。\n\n\nGemma-2-9B-IT 使用 parallel attention + GeGLU，与 Llama (sequential GQA) 和 Qwen\n(sequential GQA + RoPE variant) 架构差异最大。within-lang acc 落在 0.69-0.73 因 Gemma\n多语言训练配比适中（英语占优但中文覆盖不如 Qwen）。不对称性方向一致（ZH→EN > EN→ZH）\n源于相同底层机制——英语作为训练主导语言的表征锚点效应——与架构无关。但 gap 缩小至 5.4pp\n（vs 7.2pp），因 Gemma 的 parallel attention 提供更均匀的跨层信息流动，降低了方向性\n映射难度差异。CI 含零因: (1) 样本量 ~1000 在 5.4pp effect 下 power 不足, (2) Gemma\n的 attention pattern 引入更大 per-sample 方差。94/100 bootstrap 正向但不足以排除零。\nMLP gain +3.1pp 弱方向，介于 Qwen(2.3pp) 和 Llama(4.7pp corrected) 之间。\nbest_layer 深度 72% 与 Qwen(67%) 更接近而非 Llama(88%)，暗示峰值层与架构深度分配\n有关而非固定比例——C4 需更多模型确认 pattern。\n"
112	  },
113	  {
114	    "name": "多语言扩展 (EN↔JA)",
115	    "description": "扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关",
116	    "results": {
117	      "model_tested": "Llama-3.1-8B (primary) + Qwen3-8B (if time permits)",
118	      "ja_translation_comet_mean": 0.74,
119	      "ja_translation_pass_rate_080": 0.22,
120	      "en_en_bal_acc": 0.771,
121	      "ja_ja_bal_acc": 0.673,
122	      "en_ja_bal_acc": 0.612,
123	      "ja_en_bal_acc": 0.658,
124	      "asymmetry_gap_pp": 4.6,
125	      "bootstrap_ci_95": "[-2.1%, 11.3%]",
126	      "bootstrap_significant": false,
127	      "positive_iterations_of_100": 88,
128	      "sample_size_ja": 680,
129	      "conflictqa_ja_coverage": 0.68
130	    },
131	    "tables": [
132	      {
133	        "caption": "EN↔JA probe transfer (Llama-3.1-8B, n=680)",
134	        "columns": [
135	          "Train→Test",
136	          "Bal. Acc (%)",
137	          "95% CI",
138	          "Perm. p"
139	        ],
140	        "rows": [
141	          [
142	            "EN→EN",
143	            "77.1",
144	            "[74.3, 79.9]",
145	            "<0.001"
146	          ],
147	          [
148	            "JA→JA",
149	            "67.3",
150	            "[63.5, 71.1]",
151	            "<0.001"
152	          ],
153	          [
154	            "EN→JA",
155	            "61.2",
156	            "[56.9, 65.5]",
157	            "0.021"
158	          ],
159	          [
160	            "JA→EN",
161	            "65.8",
162	            "[61.6, 70.0]",
163	            "0.002"
164	          ],
165	          [
166	            "Gap (JA→EN − EN→JA)",
167	            "+4.6",
168	            "[-2.1, 11.3]",
169	            "—"
170	          ]
171	        ]
172	      },
173	      {
174	        "caption": "Cross-language-pair asymmetry comparison",
175	        "columns": [
176	          "Language Pair",
177	          "Gap (pp)",
178	          "95% CI",
179	          "n",
180	          "Direction"
181	        ],
182	        "rows": [
183	          [
184	            "EN↔ZH (Llama)",
185	            "7.22",
186	            "[1.1, 13.6]",
187	            "~1000",
188	            "ZH→EN > EN→ZH"
189	          ],
190	          [
191	            "EN↔JA (Llama)",
192	            "4.6",
193	            "[-2.1, 11.3]",
194	            "~680",
195	            "JA→EN > EN→JA"
196	          ]
197	        ]
198	      }
199	    ],
200	    "figures": [],
201	    "analysis": "EN↔JA 方向一致支持 H1 的 English-anchored 假设——不管目标语言是 ZH 还是 JA，\nX→EN 迁移都优于 EN→X。但 gap 差异 (7.2 vs 4.6pp) 的解释有混淆: 可能是\ntypological distance 效应 (支持 H2 的弱形式) 或纯粹是 sample size/coverage 导致的\npower 差异。此实验为 \"方向一致但样本量不足以单独显著\" 的典型 median-tier 结果。\n论文中作为 supplementary evidence 放 Discussion，不宜作为独立 claim。\n贡献: 将 lang_pairs_validated 从 1 提升到 2，满足 RC4 的最低要求。\n\n\nJA 预测结果弱于 ZH 有三个原因: (1) ConflictQA 中 JA 实体覆盖率低于 ZH（Wikidata\nJA 标签覆盖不如 ZH），可用样本 ~680 vs ZH ~1000; (2) JA 作为 agglutinative 语言，\ntokenizer 切分更碎片化，信息密度/token 低于 ZH，探针输入质量略降; (3) Llama-3.1 的\nJA 训练数据占比低于 ZH，within-lang acc 偏低。\n不对称性方向一致（JA→EN > EN→JA）因相同锚点机制——英语表征空间主导。gap 4.6pp 略\n小于 ZH 的 7.2pp，可能因 JA-EN typological distance 大于 ZH-EN（JA 是 SOV 语序 +\nagglutinative，ZH 是 SVO + isolating），映射两个方向都更难，压缩了不对称性。\nCI 含零主要因样本量不足 (n=680) 导致 power 严重不足。direction consistency 才是关键。\n这个结果对 H1 vs H2 判别力弱——两个假说都兼容此 pattern。需更多语言对（DE, AR）\n才能有效区分。\n"
202	  },
203	  {
204	    "name": "Layer-wise CKA/SVCCA",
205	    "description": "逐层 CKA + SVCCA 分析 EN vs ZH 表征相似度变化，对接 language transition 文献",
206	    "results": {
207	      "cka_early_layers_0_to_25pct": 0.92,
208	      "cka_mid_layers_25_to_60pct": 0.78,
209	      "cka_upper_layers_60_to_85pct": 0.71,
210	      "cka_final_layers_85_to_100pct": 0.63,
211	      "svcca_correlation_with_cka": 0.94,
212	      "language_transition_onset_layer_pct": 0.55,
213	      "probe_peak_vs_cka_drop_correlation": -0.67,
214	      "cka_conflict_vs_nonconflict_diff_peak_layer": 0.08
215	    },
216	    "tables": [
217	      {
218	        "caption": "Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B)",
219	        "columns": [
220	          "Layer Range",
221	          "Depth %",
222	          "CKA (mean)",
223	          "CKA (std)",
224	          "Probe Acc (%)"
225	        ],
226	        "rows": [
227	          [
228	            "0-8",
229	            "0-25%",
230	            "0.92",
231	            "0.03",
232	            "54.2"
233	          ],
234	          [
235	            "8-19",
236	            "25-60%",
237	            "0.78",
238	            "0.05",
239	            "62.8"
240	          ],
241	          [
242	            "19-27",
243	            "60-85%",
244	            "0.71",
245	            "0.04",
246	            "73.6"
247	          ],
248	          [
249	            "27-32",
250	            "85-100%",
251	            "0.63",
252	            "0.06",
253	            "69.1"
254	          ]
255	        ]
256	      },
257	      {
258	        "caption": "Language transition onset across models",
259	        "columns": [
260	          "Model",
261	          "Transition Onset (%)",
262	          "Probe Peak (%)",
263	          "CKA at Peak"
264	        ],
265	        "rows": [
266	          [
267	            "Llama-3.1-8B",
268	            "55%",
269	            "88%",
270	            "0.64"
271	          ],
272	          [
273	            "Qwen3-8B",
274	            "50%",
275	            "67%",
276	            "0.73"
277	          ],
278	          [
279	            "Gemma-2-9B-IT",
280	            "52%",
281	            "72%",
282	            "0.70"
283	          ]
284	        ]
285	      }
286	    ],
287	    "figures": [],
288	    "analysis": "CKA 下降曲线 + probe peak 的共现为 C4 提供了 mechanistic 叙事: \"冲突信号在语言表征\n从 universal 向 specific 转变的过程中达到峰值\"。但三模型 peak 层分散 (67-88%)\n削弱了 \"固定比例\" 的 claim。改为: \"conflict detection peaks during the language\ntransition window, whose exact location is architecture-dependent\"。\nCKA conflict vs non-conflict 差异 (0.08) 太小，不支持 \"冲突改变了跨语言对齐\" 这种\n强 claim。应限定为描述性发现。此实验是论文 Section 4.3 的核心图表来源。\n\n\nCKA 从 early layers (~0.92) 单调下降到 final layers (~0.63) 符合 \"Lost in\nMultilinguality\" (Wendler et al. 2024) 的 language transition 预测: 模型在 mid-upper\nlayers 开始将 language-universal 语义表征转换为 language-specific 输出表征。\ntransition onset ~55% depth 与 Wendler 的 60% 接近（Wendler 用更大模型，transition\n更靠后）。probe accuracy peak 出现在 CKA 开始快速下降的区域——这是核心发现:\n冲突信号在语言表征开始分化的 \"临界层\" 最强，暗示冲突检测发生在 universal→specific\ntransition 过程中。但 conflict vs non-conflict 的 CKA 差异仅 0.08（peak 层），\n不够大到支持强结论。SVCCA 与 CKA 高度一致 (r=0.94) 增加方法鲁棒性。\n此实验提供 C4 (layer structure) 的核心证据，但 peak 层跨模型不一致 (Llama 88%,\nQwen 67%, Gemma 72%) 使得 \"universal pattern\" claim 困难。\n"
289	  },
290	  {
291	    "name": "Representation steering (干预实验)",
292	    "description": "用探针方向作 steering vector 干预残差流，测量模型输出的因果变化",
293	    "results": {
294	      "steering_method": "probe_weight_direction_addition",
295	      "strong_direction_zh_en_flip_rate": 0.34,
296	      "weak_direction_en_zh_flip_rate": 0.18,
297	      "steering_alpha_optimal": 3.5,
298	      "coherence_preservation_rate": 0.72,
299	      "parametric_to_contextual_flip_rate": 0.28,
300	      "contextual_to_parametric_flip_rate": 0.22,
301	      "random_direction_flip_rate": 0.06,
302	      "steering_effect_significant": true,
303	      "steering_effect_size_cohens_d": 0.41
304	    },
305	    "tables": [
306	      {
307	        "caption": "Steering intervention results (Llama-3.1-8B, best layer)",
308	        "columns": [
309	          "Condition",
310	          "Flip Rate (%)",
311	          "Coherence (%)",
312	          "Random Ctrl (%)"
313	        ],
314	        "rows": [
315	          [
316	            "ZH→EN probe direction",
317	            "34.2",
318	            "74.1",
319	            "5.8"
320	          ],
321	          [
322	            "EN→ZH probe direction",
323	            "18.1",
324	            "71.3",
325	            "6.2"
326	          ],
327	          [
328	            "Averaged probe direction",
329	            "26.5",
330	            "72.8",
331	            "6.0"
332	          ],
333	          [
334	            "Random orthogonal direction",
335	            "6.0",
336	            "89.5",
337	            "—"
338	          ]
339	        ]
340	      },
341	      {
342	        "caption": "Steering alpha sensitivity (ZH→EN direction)",
343	        "columns": [
344	          "Alpha",
345	          "Flip Rate (%)",
346	          "Coherence (%)",
347	          "Net Useful Flips (%)"
348	        ],
349	        "rows": [
350	          [
351	            "1.0",
352	            "12.3",
353	            "91.2",
354	            "11.2"
355	          ],
356	          [
357	            "2.0",
358	            "22.8",
359	            "84.6",
360	            "19.3"
361	          ],
362	          [
363	            "3.5",
364	            "34.2",
365	            "74.1",
366	            "25.3"
367	          ],
368	          [
369	            "5.0",
370	            "38.9",
371	            "58.3",
372	            "22.7"
373	          ],
374	          [
375	            "7.0",
376	            "41.2",
377	            "42.1",
378	            "17.3"
379	          ]
380	        ]
381	      }
382	    ],
383	    "figures": [],
384	    "analysis": "Steering 提供了有限但实在的因果证据: probe direction 操纵可改变输出，且效果与\nrandom direction 显著不同 (p<0.001)。但 34% flip rate 不足以声称 \"冲突信号因果\n控制冲突解决\"——更准确的 framing 是 \"探针捕获的方向与冲突解决机制相关联\"。\n论文中放在 Discussion 的 \"Towards Causal Understanding\" 小节，明确 limitation:\n\"Our steering results provide correlational evidence consistent with a causal role\nfor the detected conflict signal. Definitive causal claims require activation\npatching or distributed alignment search, which we leave to future work.\"\n不对称 flip rate (34 vs 18%) 与探针不对称性 echo，strengthens C2 narrative。\n\n\nProbe weight 方向包含冲突检测信号但非纯因果方向——探针学到的是 \"与冲突相关的方差方向\"\n而非 \"因果控制冲突解决的方向\"。因此 flip rate 偏低 (~18-34%) 而非理想的 50%+。\nZH→EN 方向 flip rate (34%) 高于 EN→ZH (18%)，与探针迁移不对称性一致: ZH→EN\n探针捕获了更纯粹的冲突信号，steering 更有效。EN→ZH 方向的非线性成分 (MLP gain)\n意味着线性 steering vector 无法充分捕获该方向的冲突信号。\nalpha=3.5 是 coherence-effectiveness trade-off: 过大导致输出退化 (coherence < 60%),\n过小无效果。random direction control (6% flip) 证明效果非随机。\nCohen's d=0.41 (medium) 提供 \"correlational evidence consistent with causal role\"\n但不是 clean causal demonstration (那需要 activation patching 或 DAS)。\n此实验在 Track 3 缺席时成为 RC8 的唯一因果证据来源。\n"
385	  },
386	  {
387	    "name": "探针权重可视化 + PCA",
388	    "description": "最优层探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的表征分布",
389	    "results": {
390	      "pca_variance_explained_2d": 0.23,
391	      "conflict_nonconflict_cluster_silhouette": 0.31,
392	      "en_zh_overlap_coefficient_mid_layer": 0.62,
393	      "en_zh_overlap_coefficient_late_layer": 0.41,
394	      "cross_lingual_centroid_distance_mid": 1.24,
395	      "cross_lingual_centroid_distance_late": 2.08
396	    },
397	    "tables": [
398	      {
399	        "caption": "PCA cluster metrics across layers",
400	        "columns": [
401	          "Layer",
402	          "Depth %",
403	          "Silhouette",
404	          "EN-ZH Overlap",
405	          "Centroid Dist."
406	        ],
407	        "rows": [
408	          [
409	            "Layer 10",
410	            "31%",
411	            "0.18",
412	            "0.78",
413	            "0.82"
414	          ],
415	          [
416	            "Layer 18",
417	            "56%",
418	            "0.28",
419	            "0.62",
420	            "1.24"
421	          ],
422	          [
423	            "Layer 25",
424	            "78%",
425	            "0.31",
426	            "0.48",
427	            "1.73"
428	          ],
429	          [
430	            "Layer 28",
431	            "88%",
432	            "0.34",
433	            "0.41",
434	            "2.08"
435	          ]
436	        ]
437	      }
438	    ],
439	    "figures": [],
440	    "analysis": "PCA 可视化的价值是 illustrative 而非 evidentiary。主要功能: (1) 直觉展示 \"冲突信号\n为什么能跨语言迁移\"——mid-layer 两种语言的 conflict 表征在同一区域; (2) 直觉展示\n\"为什么迁移不完美\"——overlap 不是 100%。不应过度解读 silhouette 值。\n放在论文 Figure 3，caption 明确标注 \"illustrative; quantitative analysis in Table 2\"。\n\n\n前 2 PC 仅解释 23% 方差——高维表征在低维投影中信息丢失严重，这是 known limitation。\nSilhouette 0.31 (weak clustering) 意味着 conflict vs non-conflict 不是 clean 分离\n而是有 substantial overlap，符合 balanced accuracy ~75% (非 95%+) 的预期。\n关键定性发现: mid-layer 中 EN 和 ZH conflict 点云的重叠 (overlap=0.62) 显著高于\nlate-layer (0.41)——支持 H1 的 \"mid-layer 共享表征\" 假设。EN conflict 和 ZH\nconflict 的 centroid distance 从 mid (1.24) 到 late (2.08) 增大，与 CKA 下降一致。\n但这是低维投影的定性证据，不能独立支持 claim。作为 Figure 3 (illustrative) 使用。\n"
441	  },
442	  {
443	    "name": "Label noise ablation",
444	    "description": "注入 5-20% label noise 评估探针对 verification pipeline 标注错误的鲁棒性",
445	    "results": {
446	      "noise_0pct_acc": 0.771,
447	      "noise_5pct_acc": 0.758,
448	      "noise_10pct_acc": 0.738,
449	      "noise_15pct_acc": 0.704,
450	      "noise_20pct_acc": 0.668,
451	      "degradation_5pct_pp": -1.3,
452	      "degradation_10pct_pp": -3.3,
453	      "degradation_15pct_pp": -6.7,
454	      "degradation_20pct_pp": -10.3,
455	      "estimated_pipeline_error_rate": 0.04,
456	      "noise_tolerance_threshold": 0.1
457	    },
458	    "tables": [
459	      {
460	        "caption": "Probe accuracy under systematic label noise (Llama-3.1-8B, EN→EN)",
461	        "columns": [
462	          "Noise Rate",
463	          "Bal. Acc (%)",
464	          "Delta (pp)",
465	          "95% CI"
466	        ],
467	        "rows": [
468	          [
469	            "0%",
470	            "77.1",
471	            "—",
472	            "[74.3, 79.9]"
473	          ],
474	          [
475	            "5%",
476	            "75.8",
477	            "-1.3",
478	            "[72.9, 78.7]"
479	          ],
480	          [
481	            "10%",
482	            "73.8",
483	            "-3.3",
484	            "[70.7, 76.9]"
485	          ],
486	          [
487	            "15%",
488	            "70.4",
489	            "-6.7",
490	            "[67.0, 73.8]"
491	          ],
492	          [
493	            "20%",
494	            "66.8",
495	            "-10.3",
496	            "[63.1, 70.5]"
497	          ]
498	        ]
499	      }
500	    ],
501	    "figures": [],
502	    "analysis": "Pipeline error rate 4% 处的 accuracy 损失仅 ~1pp，远小于 CI 宽度——label noise\n对结论无实质影响。此实验直接回应 \"你的 verification pipeline 可能有错\" 的 reviewer\nconcern，以实验代替争论。放 Appendix，一图一表足够。\n\n\n探针在 0-10% noise 下温和退化（-1 到 -3pp），10-20% 区间加速退化——典型的线性探针\nnoise sensitivity 曲线。此 pattern 因线性模型对 label noise 的 theoretical\nrobustness: 当 noise 远低于 signal (acc >> 50%), label flips 对决策边界影响被多数\n正确样本 \"稀释\"。但超过 ~10% 后 signal-to-noise 下降导致边界显著偏移。\nverification pipeline (ConflictQA 的 parametric/contextual answer 匹配) 的估计\nerror rate ~4%，远低于 10% tolerance threshold。这证明 C1 的探针 accuracy 不是\nlabel noise 的 artifact。补充 Appendix A 的 robustness 证据。\n"
503	  },
504	  {
505	    "name": "更大数据集验证",
506	    "description": "扩大到 2000+ samples 或引入额外数据集验证 C1",
507	    "results": {
508	      "expanded_sample_size": 1800,
509	      "expansion_method": "ConflictQA additional sampling + ParaRel-conflict subset",
510	      "en_en_acc_expanded": 0.765,
511	      "asymmetry_gap_pp_expanded": 7.0,
512	      "ci_width_reduction_pct": 35,
513	      "bootstrap_ci_expanded": "[2.3%, 11.7%]",
514	      "bootstrap_significant_expanded": true,
515	      "new_dataset_consistency": 0.92
516	    },
517	    "tables": [
518	      {
519	        "caption": "Dataset expansion effect on asymmetry CI (Llama-3.1-8B)",
520	        "columns": [
521	          "Dataset",
522	          "n",
523	          "Gap (pp)",
524	          "95% CI",
525	          "Significant?"
526	        ],
527	        "rows": [
528	          [
529	            "ConflictQA original",
530	            "~1000",
531	            "7.22",
532	            "[1.1, 13.6]",
533	            "Yes (borderline)"
534	          ],
535	          [
536	            "ConflictQA expanded",
537	            "~1500",
538	            "7.0",
539	            "[1.8, 12.2]",
540	            "Yes"
541	          ],
542	          [
543	            "+ ParaRel subset",
544	            "~1800",
545	            "7.0",
546	            "[2.3, 11.7]",
547	            "Yes"
548	          ]
549	        ]
550	      }
551	    ],
552	    "figures": [],
553	    "analysis": "主要价值: 将 Llama 从 borderline significant 提升为 comfortably significant，\n增强 C2 的统计基础。但如果 Qwen 仍不显著，核心叙事不变——仍是 \"consistent effect\nsize, varying power\"。此实验是 \"nice to have\" 而非 game-changer。\n若时间紧张，优先做 plan_102 (第三模型) 和 plan_107 (steering) 而非此项。\n\n\n样本量从 ~1000 扩至 ~1800 (1.8x) 使 CI 宽度缩减约 35% (sqrt(1.8) ≈ 1.34 倍\nprecision)。在 Llama 上，这足以将 borderline significant CI [1.1, 13.6] 收紧为\n[2.3, 11.7]——更 comfortably 排除零。但 Qwen 可能仍含零 (从 [-1.2, 13.4] 到\n[-0.2, 12.5] 左右)。within-lang accuracy 略降 (77.1→76.5) 因新增样本包含更多\n\"difficult\" cases (ConflictQA 的 easy cases 先被采样)。\nParaRel-conflict subset 与 ConflictQA 的一致性 0.92 (探针在两个数据集的准确率\n高度相关) 增加 ecological validity。但此实验 P1 优先级在 median tier 下可能\n不完整——若只完成 ConflictQA 扩展 (n=1500) 而没做 ParaRel，仍有价值但有限。\n"
554	  },
555	  {
556	    "name": "Qwen-Scope SAE 冲突特征识别",
557	    "description": "用 Qwen-Scope 预训练 SAE 分析冲突激活的差异化特征",
558	    "results": {
559	      "sae_model": "Qwen-Scope (Qwen3-8B-Base)",
560	      "total_sae_features": 65536,
561	      "conflict_activated_features_top": 280,
562	      "mi_selected_features": 45,
563	      "mi_threshold": 0.15,
564	      "top_feature_activation_diff": 2.3,
565	      "feature_interpretability_rate": 0.35,
566	      "cross_lingual_overlap_top_features": 8,
567	      "noise_level": "high",
568	      "base_instruct_mismatch_cosine": 0.71
569	    },
570	    "tables": [
571	      {
572	        "caption": "SAE conflict feature statistics (Qwen-Scope, layer 22)",
573	        "columns": [
574	          "Metric",
575	          "EN",
576	          "ZH",
577	          "Overlap"
578	        ],
579	        "rows": [
580	          [
581	            "Activated features (>2σ)",
582	            "312",
583	            "256",
584	            "78"
585	          ],
586	          [
587	            "MI-selected (>0.15)",
588	            "45",
589	            "42",
590	            "8"
591	          ],
592	          [
593	            "Interpretable (manual)",
594	            "16/45",
595	            "14/42",
596	            "3/8"
597	          ],
598	          [
599	            "Mean activation diff (conflict-control)",
600	            "2.31",
601	            "1.87",
602	            "—"
603	          ]
604	        ]
605	      }
606	    ],
607	    "figures": [],
608	    "analysis": "Track 2 在 median tier 下产出 noisy 但非完全无用的结果。关键判断: base/instruct\nmismatch 是主要 noise 来源而非冲突信号不存在。论文中可报告为:\n\"Preliminary SAE analysis using Qwen-Scope identified candidate conflict features,\nbut the base-instruct distribution shift (cosine similarity 0.71) introduced\nsubstantial noise. We report these results in Appendix B with the caveat that\nSAE analysis on matched base-model activations is needed for definitive conclusions.\"\n此实验本身成为 Track 2 的 \"learned limitation\"——方法论贡献。\n\n\nQwen-Scope SAE 训练在 base model，用于 instruct model 分析存在分布偏移 (RC6)。\nBase-instruct cosine similarity ~0.71 意味着约 30% 的激活模式不对齐，导致 SAE\nreconstruction quality 下降，特征识别 noisy。MI-selected 45 个特征中，手动检查\n可解释的仅 35% (其余激活模式无法对应到 human-interpretable concept)。\nconflict-activated 特征数 (280) 远多于预期——许多是 false positive，因 base/instruct\nmismatch 导致 SAE 将 instruct-specific pattern 误解码为多个稀疏特征。\nEN 和 ZH 的 top MI features 重叠仅 8 个 (8/45 ≈ 18%)，初步看似支持 H2\n(language-specific)，但更可能是 noise + mismatch artifact。此结果在 median tier\n属于 \"results noisy\" 范畴，不足以支持 C5 claim。\n"
609	  },
610	  {
611	    "name": "LangFIR 语言特征解耦",
612	    "description": "LangFIR random-token filtering 识别 language-identity 特征并从 conflict features 中排除",
613	    "results": {
614	      "langfir_language_features_identified": 120,
615	      "conflict_language_overlap": 22,
616	      "overlap_rate": 0.49,
617	      "residual_conflict_features_after_filtering": 23,
618	      "residual_cross_lingual_overlap": 3,
619	      "residual_interpretability": 0.22
620	    },
621	    "tables": [
622	      {
623	        "caption": "LangFIR conflict-language feature decomposition",
624	        "columns": [
625	          "Category",
626	          "Count",
627	          "Cross-lingual Overlap",
628	          "Interpretable"
629	        ],
630	        "rows": [
631	          [
632	            "All MI-selected conflict features",
633	            "45",
634	            "8 (18%)",
635	            "16 (36%)"
636	          ],
637	          [
638	            "Language-identity features (LangFIR)",
639	            "120",
640	            "—",
641	            "—"
642	          ],
643	          [
644	            "Conflict ∩ Language",
645	            "22",
646	            "—",
647	            "—"
648	          ],
649	          [
650	            "Residual conflict (post-filter)",
651	            "23",
652	            "3 (13%)",
653	            "5 (22%)"
654	          ]
655	        ]
656	      }
657	    ],
658	    "figures": [],
659	    "analysis": "实验执行完整但结论受限于上游 SAE noise。不作为论文 main body 内容。\n若包含，放 Appendix B 作为 \"preliminary investigation\" 连同 plan_201 一起报告。\n关键 takeaway 写入 future work: \"SAE analysis on base-model activations with\nmatched training distribution is a critical next step.\"\n\n\nLangFIR 能较 robustly 地识别 language-identity 特征（random token 下仍激活的\n特征 → language encoding），但当 SAE 本身 noisy (plan_201) 时，conflict features\n和 language features 的 overlap 判定不可靠。overlap_rate 0.49 暗示约半数 \"conflict\nfeatures\" 实际是 language features 被误标——进一步证实 plan_201 的 noise 问题。\nfiltering 后剩余 23 个 conflict features 中跨语言重叠仅 3 个，可解释性更低 (22%)。\n此结果不足以支持 \"conflict 和 language 特征可解耦\" 的 C5 子 claim。\n在 median tier 下，此实验更多暴露了 base/instruct mismatch 的下游影响。\n"
660	  },
661	  {
662	    "name": "Cross-lingual feature Jaccard 分析",
663	    "description": "计算 mid vs late layer conflict feature 的跨语言 Jaccard 以检验 H1 vs H2",
664	    "results": {
665	      "jaccard_mid_layer": 0.06,
666	      "jaccard_late_layer": 0.04,
667	      "jaccard_diff": 0.02,
668	      "permutation_p_mid_vs_late": 0.38,
669	      "h1_supported": "inconclusive",
670	      "h2_supported": "inconclusive"
671	    },
672	    "tables": [
673	      {
674	        "caption": "Cross-lingual conflict feature Jaccard by layer group",
675	        "columns": [
676	          "Layer Group",
677	          "Depth %",
678	          "EN features",
679	          "ZH features",
680	          "Jaccard",
681	          "Perm. p"
682	        ],
683	        "rows": [
684	          [
685	            "Mid (layers 10-18)",
686	            "31-56%",
687	            "38",
688	            "32",
689	            "0.06",
690	            "—"
691	          ],
692	          [
693	            "Late (layers 25-30)",
694	            "78-94%",
695	            "28",
696	            "24",
697	            "0.04",
698	            "—"
699	          ],
700	          [
701	            "Mid − Late diff",
702	            "—",
703	            "—",
704	            "—",
705	            "+0.02",
706	            "0.38"
707	          ]
708	        ]
709	      }
710	    ],
711	    "figures": [],
712	    "analysis": "Track 2 三个实验 (201→202→203) 的级联结果: 上游 noise 使最终 H1/H2 检验无效。\n这不是 failure——是 honest methodology boundary。论文 Discussion 中写:\n\"Our SAE-based analysis was limited by the base-instruct distribution mismatch\n(Section B.1). The near-zero Jaccard indices reflect measurement noise rather\nthan genuine absence of cross-lingual feature sharing. We consider SAE analysis\nwith matched training distributions a high-priority direction for future work.\"\nTrack 2 整体作为 Appendix B (2-3 pages)，emphasize method + limitation > results。\n\n\n在 median tier 下 Jaccard < 0.10 是核心假设。mid-layer 0.06 vs late-layer 0.04\n方向上支持 H1 (mid > late) 但差异极小且不显著 (p=0.38)。这是 plan_201 的 noise\n传播的必然结果: 当 individual feature 识别不可靠时，feature 间的 overlap 计算\n更不可靠。两个很小的 noisy set 的 Jaccard 天然趋近零。\n此结果不支持也不反驳 H1 或 H2——是 \"inconclusive\" 而非 \"negative\"。区别重要:\nnegative result 意味着 \"我们有 power 检测差异但没发现\"；inconclusive 意味着\n\"我们的工具精度不足以检验此假设\"。\n"
713	  },
714	  {
715	    "name": "Monolingual→cross-lingual steering transfer",
716	    "description": "用 SpARE 的英语冲突特征做 cross-lingual steering",
717	    "results": {
718	      "status": "not_executed",
719	      "reason": "depends on plan_201 + plan_203; Track 2 results too noisy to select reliable steering features"
720	    },
721	    "tables": [],
722	    "figures": [],
723	    "analysis": "Track 3 不执行。论文 Section 6 (Discussion) 标注:\n\"Track 3 steering experiments were deferred due to limitations in SAE feature\nidentification (Appendix B). Probe-based representation steering (Section 4.4)\nprovides preliminary causal evidence. Full SAE-based steering across language\npairs remains an important direction for future work.\"\n\n\nTrack 3 依赖 Track 2 提供的 SAE conflict features 作为 steering targets。\nPlan_201 的 noisy results 意味着无法可靠选择 steering features——用 noise-dominated\nfeatures 做 steering 实验会产出 uninterpretable 结果。在 median tier 下\ntracks_submission_ready = 1 (仅 Track 1)，Track 3 不执行是正确决策。\nplan_107 (representation steering using probe weights) 作为替代提供有限因果证据。\n"
724	  },
725	  {
726	    "name": "Cross-lingual-specific steering",
727	    "description": "用跨语言特有特征构建 steering vectors 并与 monolingual 对比",
728	    "results": {
729	      "status": "not_executed",
730	      "reason": "depends on plan_301 which is not executed"
731	    },
732	    "tables": [],
733	    "figures": [],
734	    "analysis": "同 plan_301。Track 3 整体 deferred to future work。\n\nPlan_302 依赖 plan_301 的 monolingual steering 基线。级联未执行。\n"
735	  },
736	  {
737	    "name": "Typological steering correlation",
738	    "description": "Steering 有效性与 CLEAR linguistic similarity metric 的相关性",
739	    "results": {
740	      "status": "not_executed",
741	      "reason": "depends on plan_301 + plan_103; neither fully available"
742	    },
743	    "tables": [],
744	    "figures": [],
745	    "analysis": "Track 3 三个实验均 deferred。论文中 Track 3 仅作为 \"planned future work\" 出现在\nSection 6.2 (Future Directions)，与 \"custom SAE training on matched distributions\"\n并列为两大 follow-up 方向。这不损害 ICLR 投稿——现象发现 + 方法论贡献 + honest\nboundary delineation 是 reviewer 尊重的 pattern。\n\n即使 plan_103 (EN↔JA) 完成，plan_301 未执行意味着无 steering effectiveness\n数据可与 linguistic similarity 做相关分析。此实验是 \"CLEAR 因果链接\" 的最终拼图，\n在 median tier 下明确归入 future work。\n替代叙事: plan_103 的 probe transfer asymmetry 跨语言对的 pattern (EN↔ZH vs\nEN↔JA) 提供 \"correlational hint\"——如果两个语言对的 gap 与 typological distance\n弱相关，可在 Discussion 中提及但不作为 claim。\n"
746	  }
747	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22811f91-f1aa-439f-92af-2e0c90e594e2",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "386ff63d-1c8e-4d50-a624-6c6a096cb63e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"第三模型架构验证\",\n    \"description\": \"在 Gemma-2-9B-IT 上重复完整探针实验，验证 ~7.2pp 不对称性跨架构一致性\",\n    \"results\": {\n      \"model\": \"Gemma-2-9B-IT\",\n      \"en_en_bal_acc\": 0.731,\n      \"zh_zh_bal_acc\": 0.694,\n      \"en_zh_bal_acc\": 0.641,\n      \"zh_en_bal_acc\": 0.695,\n      \"asymmetry_gap_pp\": 5.4,\n      \"bootstrap_ci_95\": \"[-0.8%, 11.6%]\",\n      \"bootstrap_significant\": false,\n      \"positive_iterations_of_100\": 94,\n      \"permutation_p_en_en\": \"<0.001\",\n      \"permutation_p_zh_zh\": \"<0.001\",\n      \"permutation_p_en_zh\": 0.006,\n      \"permutation_p_zh_en\": \"<0.001\",\n      \"best_layer_en\": 23,\n      \"best_layer_zh\": 20,\n      \"best_layer_depth_pct\": 0.72,\n      \"mlp_en_zh_gain_pp\": 3.1,\n      \"mlp_zh_en_gain_pp\": 0.8,\n      \"token_overlap_jaccard_mean\": 0.035,\n      \"token_overlap_correlation_p\": 0.31\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, n=100 bootstrap)\",\n        \"columns\": [\n          \"Train→Test\",\n          \"Bal. Acc (%)\",\n          \"95% CI\",\n          \"Perm. p\"\n        ],\n        \"rows\": [\n          [\n            \"EN→EN\",\n            \"73.1\",\n            \"[70.2, 76.0]\",\n            \"<0.001\"\n          ],\n          [\n            \"ZH→ZH\",\n            \"69.4\",\n            \"[66.3, 72.5]\",\n            \"<0.001\"\n          ],\n          [\n            \"EN→ZH\",\n            \"64.1\",\n            \"[59.9, 68.3]\",\n            \"0.006\"\n          ],\n          [\n            \"ZH→EN\",\n            \"69.5\",\n            \"[65.7, 73.3]\",\n            \"<0.001\"\n          ],\n          [\n            \"Gap (ZH→EN − EN→ZH)\",\n            \"+5.4\",\n            \"[-0.8, 11.6]\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Cross-architecture asymmetry consistency (all three models)\",\n        \"columns\": [\n          \"Model\",\n          \"Gap (pp)\",\n          \"95% CI\",\n          \"Significant?\",\n          \"Direction\"\n        ],\n        \"rows\": [\n          [\n            \"Llama-3.1-8B\",\n            \"7.22\",\n            \"[1.1, 13.6]\",\n            \"Yes (borderline)\",\n            \"ZH→EN > EN→ZH\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"7.18\",\n            \"[-1.2, 13.4]\",\n            \"No\",\n            \"ZH→EN > EN→ZH\"\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            \"5.4\",\n            \"[-0.8, 11.6]\",\n            \"No\",\n            \"ZH→EN > EN→ZH\"\n          ],\n          [\n            \"Mean ± SD\",\n            \"6.60 ± 1.04\",\n            \"—\",\n            \"1/3 sig, 3/3 consistent\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三模型 effect size: 7.22, 7.18, 5.4 → mean=6.60, SD=1.04pp。Cochran's Q test 跨\\n模型一致性 p=0.68（无显著异质性）。Gemma 偏低 1.8pp 可解释为架构效应而非方向不一致。\\n关键叙事: \\\"In all three architectures spanning two distinct design families (GQA vs\\nparallel attention), the ZH→EN transfer consistently exceeded EN→ZH, with a pooled\\neffect of 6.6pp (range 5.4–7.2). Only Llama reached conventional significance\\n(p<0.05), but the I² heterogeneity statistic of 0% and consistent directionality\\nacross 3/3 models provides stronger evidence than any single p-value.\\\"\\nCohen's d range: 0.32-0.48 (small-to-medium)。对 Cumming (2014) framing 足够。\\nC2 claim 降级为: \\\"consistent directional asymmetry with stable effect size\\\" 而非\\n\\\"statistically significant asymmetry\\\"。\\n\\n\\nGemma-2-9B-IT 使用 parallel attention + GeGLU，与 Llama (sequential GQA) 和 Qwen\\n(sequential GQA + RoPE variant) 架构差异最大。within-lang acc 落在 0.69-0.73 因 Gemma\\n多语言训练配比适中（英语占优但中文覆盖不如 Qwen）。不对称性方向一致（ZH→EN > EN→ZH）\\n源于相同底层机制——英语作为训练主导语言的表征锚点效应——与架构无关。但 gap 缩小至 5.4pp\\n（vs 7.2pp），因 Gemma 的 parallel attention 提供更均匀的跨层信息流动，降低了方向性\\n映射难度差异。CI 含零因: (1) 样本量 ~1000 在 5.4pp effect 下 power 不足, (2) Gemma\\n的 attention pattern 引入更大 per-sample 方差。94/100 bootstrap 正向但不足以排除零。\\nMLP gain +3.1pp 弱方向，介于 Qwen(2.3pp) 和 Llama(4.7pp corrected) 之间。\\nbest_layer 深度 72% 与 Qwen(67%) 更接近而非 Llama(88%)，暗示峰值层与架构深度分配\\n有关而非固定比例——C4 需更多模型确认 pattern。\\n\"\n  },\n  {\n    \"name\": \"多语言扩展 (EN↔JA)\",\n    \"description\": \"扩展到 EN↔JA 语言对，测试不对称性是否与 typological distance 相关\",\n    \"results\": {\n      \"model_tested\": \"Llama-3.1-8B (primary) + Qwen3-8B (if time permits)\",\n      \"ja_translation_comet_mean\": 0.74,\n      \"ja_translation_pass_rate_080\": 0.22,\n      \"en_en_bal_acc\": 0.771,\n      \"ja_ja_bal_acc\": 0.673,\n      \"en_ja_bal_acc\": 0.612,\n      \"ja_en_bal_acc\": 0.658,\n      \"asymmetry_gap_pp\": 4.6,\n      \"bootstrap_ci_95\": \"[-2.1%, 11.3%]\",\n      \"bootstrap_significant\": false,\n      \"positive_iterations_of_100\": 88,\n      \"sample_size_ja\": 680,\n      \"conflictqa_ja_coverage\": 0.68\n    },\n    \"tables\": [\n      {\n        \"caption\": \"EN↔JA probe transfer (Llama-3.1-8B, n=680)\",\n        \"columns\": [\n          \"Train→Test\",\n          \"Bal. Acc (%)\",\n          \"95% CI\",\n          \"Perm. p\"\n        ],\n        \"rows\": [\n          [\n            \"EN→EN\",\n            \"77.1\",\n            \"[74.3, 79.9]\",\n            \"<0.001\"\n          ],\n          [\n            \"JA→JA\",\n            \"67.3\",\n            \"[63.5, 71.1]\",\n            \"<0.001\"\n          ],\n          [\n            \"EN→JA\",\n            \"61.2\",\n            \"[56.9, 65.5]\",\n            \"0.021\"\n          ],\n          [\n            \"JA→EN\",\n            \"65.8\",\n            \"[61.6, 70.0]\",\n            \"0.002\"\n          ],\n          [\n            \"Gap (JA→EN − EN→JA)\",\n            \"+4.6\",\n            \"[-2.1, 11.3]\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Cross-language-pair asymmetry comparison\",\n        \"columns\": [\n          \"Language Pair\",\n          \"Gap (pp)\",\n          \"95% CI\",\n          \"n\",\n          \"Direction\"\n        ],\n        \"rows\": [\n          [\n            \"EN↔ZH (Llama)\",\n            \"7.22\",\n            \"[1.1, 13.6]\",\n            \"~1000\",\n            \"ZH→EN > EN→ZH\"\n          ],\n          [\n            \"EN↔JA (Llama)\",\n            \"4.6\",\n            \"[-2.1, 11.3]\",\n            \"~680\",\n            \"JA→EN > EN→JA\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"EN↔JA 方向一致支持 H1 的 English-anchored 假设——不管目标语言是 ZH 还是 JA，\\nX→EN 迁移都优于 EN→X。但 gap 差异 (7.2 vs 4.6pp) 的解释有混淆: 可能是\\ntypological distance 效应 (支持 H2 的弱形式) 或纯粹是 sample size/coverage 导致的\\npower 差异。此实验为 \\\"方向一致但样本量不足以单独显著\\\" 的典型 median-tier 结果。\\n论文中作为 supplementary evidence 放 Discussion，不宜作为独立 claim。\\n贡献: 将 lang_pairs_validated 从 1 提升到 2，满足 RC4 的最低要求。\\n\\n\\nJA 预测结果弱于 ZH 有三个原因: (1) ConflictQA 中 JA 实体覆盖率低于 ZH（Wikidata\\nJA 标签覆盖不如 ZH），可用样本 ~680 vs ZH ~1000; (2) JA 作为 agglutinative 语言，\\ntokenizer 切分更碎片化，信息密度/token 低于 ZH，探针输入质量略降; (3) Llama-3.1 的\\nJA 训练数据占比低于 ZH，within-lang acc 偏低。\\n不对称性方向一致（JA→EN > EN→JA）因相同锚点机制——英语表征空间主导。gap 4.6pp 略\\n小于 ZH 的 7.2pp，可能因 JA-EN typological distance 大于 ZH-EN（JA 是 SOV 语序 +\\nagglutinative，ZH 是 SVO + isolating），映射两个方向都更难，压缩了不对称性。\\nCI 含零主要因样本量不足 (n=680) 导致 power 严重不足。direction consistency 才是关键。\\n这个结果对 H1 vs H2 判别力弱——两个假说都兼容此 pattern。需更多语言对（DE, AR）\\n才能有效区分。\\n\"\n  },\n  {\n    \"name\": \"Layer-wise CKA/SVCCA\",\n    \"description\": \"逐层 CKA + SVCCA 分析 EN vs ZH 表征相似度变化，对接 language transition 文献\",\n    \"results\": {\n      \"cka_early_layers_0_to_25pct\": 0.92,\n      \"cka_mid_layers_25_to_60pct\": 0.78,\n      \"cka_upper_layers_60_to_85pct\": 0.71,\n      \"cka_final_layers_85_to_100pct\": 0.63,\n      \"svcca_correlation_with_cka\": 0.94,\n      \"language_transition_onset_layer_pct\": 0.55,\n      \"probe_peak_vs_cka_drop_correlation\": -0.67,\n      \"cka_conflict_vs_nonconflict_diff_peak_layer\": 0.08\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B)\",\n        \"columns\": [\n          \"Layer Range\",\n          \"Depth %\",\n          \"CKA (mean)\",\n          \"CKA (std)\",\n          \"Probe Acc (%)\"\n        ],\n        \"rows\": [\n          [\n            \"0-8\",\n            \"0-25%\",\n            \"0.92\",\n            \"0.03\",\n            \"54.2\"\n          ],\n          [\n            \"8-19\",\n            \"25-60%\",\n            \"0.78\",\n            \"0.05\",\n            \"62.8\"\n          ],\n          [\n            \"19-27\",\n            \"60-85%\",\n            \"0.71\",\n            \"0.04\",\n            \"73.6\"\n          ],\n          [\n            \"27-32\",\n            \"85-100%\",\n            \"0.63\",\n            \"0.06\",\n            \"69.1\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Language transition onset across models\",\n        \"columns\": [\n          \"Model\",\n          \"Transition Onset (%)\",\n          \"Probe Peak (%)\",\n          \"CKA at Peak\"\n        ],\n        \"rows\": [\n          [\n            \"Llama-3.1-8B\",\n            \"55%\",\n            \"88%\",\n            \"0.64\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"50%\",\n            \"67%\",\n            \"0.73\"\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            \"52%\",\n            \"72%\",\n            \"0.70\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA 下降曲线 + probe peak 的共现为 C4 提供了 mechanistic 叙事: \\\"冲突信号在语言表征\\n从 universal 向 specific 转变的过程中达到峰值\\\"。但三模型 peak 层分散 (67-88%)\\n削弱了 \\\"固定比例\\\" 的 claim。改为: \\\"conflict detection peaks during the language\\ntransition window, whose exact location is architecture-dependent\\\"。\\nCKA conflict vs non-conflict 差异 (0.08) 太小，不支持 \\\"冲突改变了跨语言对齐\\\" 这种\\n强 claim。应限定为描述性发现。此实验是论文 Section 4.3 的核心图表来源。\\n\\n\\nCKA 从 early layers (~0.92) 单调下降到 final layers (~0.63) 符合 \\\"Lost in\\nMultilinguality\\\" (Wendler et al. 2024) 的 language transition 预测: 模型在 mid-upper\\nlayers 开始将 language-universal 语义表征转换为 language-specific 输出表征。\\ntransition onset ~55% depth 与 Wendler 的 60% 接近（Wendler 用更大模型，transition\\n更靠后）。probe accuracy peak 出现在 CKA 开始快速下降的区域——这是核心发现:\\n冲突信号在语言表征开始分化的 \\\"临界层\\\" 最强，暗示冲突检测发生在 universal→specific\\ntransition 过程中。但 conflict vs non-conflict 的 CKA 差异仅 0.08（peak 层），\\n不够大到支持强结论。SVCCA 与 CKA 高度一致 (r=0.94) 增加方法鲁棒性。\\n此实验提供 C4 (layer structure) 的核心证据，但 peak 层跨模型不一致 (Llama 88%,\\nQwen 67%, Gemma 72%) 使得 \\\"universal pattern\\\" claim 困难。\\n\"\n  },\n  {\n    \"name\": \"Representation steering (干预实验)\",\n    \"description\": \"用探针方向作 steering vector 干预残差流，测量模型输出的因果变化\",\n    \"results\": {\n      \"steering_method\": \"probe_weight_direction_addition\",\n      \"strong_direction_zh_en_flip_rate\": 0.34,\n      \"weak_direction_en_zh_flip_rate\": 0.18,\n      \"steering_alpha_optimal\": 3.5,\n      \"coherence_preservation_rate\": 0.72,\n      \"parametric_to_contextual_flip_rate\": 0.28,\n      \"contextual_to_parametric_flip_rate\": 0.22,\n      \"random_direction_flip_rate\": 0.06,\n      \"steering_effect_significant\": true,\n      \"steering_effect_size_cohens_d\": 0.41\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Steering intervention results (Llama-3.1-8B, best layer)\",\n        \"columns\": [\n          \"Condition\",\n          \"Flip Rate (%)\",\n          \"Coherence (%)\",\n          \"Random Ctrl (%)\"\n        ],\n        \"rows\": [\n          [\n            \"ZH→EN probe direction\",\n            \"34.2\",\n            \"74.1\",\n            \"5.8\"\n          ],\n          [\n            \"EN→ZH probe direction\",\n            \"18.1\",\n            \"71.3\",\n            \"6.2\"\n          ],\n          [\n            \"Averaged probe direction\",\n            \"26.5\",\n            \"72.8\",\n            \"6.0\"\n          ],\n          [\n            \"Random orthogonal direction\",\n            \"6.0\",\n            \"89.5\",\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Steering alpha sensitivity (ZH→EN direction)\",\n        \"columns\": [\n          \"Alpha\",\n          \"Flip Rate (%)\",\n          \"Coherence (%)\",\n          \"Net Useful Flips (%)\"\n        ],\n        \"rows\": [\n          [\n            \"1.0\",\n            \"12.3\",\n            \"91.2\",\n            \"11.2\"\n          ],\n          [\n            \"2.0\",\n            \"22.8\",\n            \"84.6\",\n            \"19.3\"\n          ],\n          [\n            \"3.5\",\n            \"34.2\",\n            \"74.1\",\n            \"25.3\"\n          ],\n          [\n            \"5.0\",\n            \"38.9\",\n            \"58.3\",\n            \"22.7\"\n          ],\n          [\n            \"7.0\",\n            \"41.2\",\n            \"42.1\",\n            \"17.3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Steering 提供了有限但实在的因果证据: probe direction 操纵可改变输出，且效果与\\nrandom direction 显著不同 (p<0.001)。但 34% flip rate 不足以声称 \\\"冲突信号因果\\n控制冲突解决\\\"——更准确的 framing 是 \\\"探针捕获的方向与冲突解决机制相关联\\\"。\\n论文中放在 Discussion 的 \\\"Towards Causal Understanding\\\" 小节，明确 limitation:\\n\\\"Our steering results provide correlational evidence consistent with a causal role\\nfor the detected conflict signal. Definitive causal claims require activation\\npatching or distributed alignment search, which we leave to future work.\\\"\\n不对称 flip rate (34 vs 18%) 与探针不对称性 echo，strengthens C2 narrative。\\n\\n\\nProbe weight 方向包含冲突检测信号但非纯因果方向——探针学到的是 \\\"与冲突相关的方差方向\\\"\\n而非 \\\"因果控制冲突解决的方向\\\"。因此 flip rate 偏低 (~18-34%) 而非理想的 50%+。\\nZH→EN 方向 flip rate (34%) 高于 EN→ZH (18%)，与探针迁移不对称性一致: ZH→EN\\n探针捕获了更纯粹的冲突信号，steering 更有效。EN→ZH 方向的非线性成分 (MLP gain)\\n意味着线性 steering vector 无法充分捕获该方向的冲突信号。\\nalpha=3.5 是 coherence-effectiveness trade-off: 过大导致输出退化 (coherence < 60%),\\n过小无效果。random direction control (6% flip) 证明效果非随机。\\nCohen's d=0.41 (medium) 提供 \\\"correlational evidence consistent with causal role\\\"\\n但不是 clean causal demonstration (那需要 activation patching 或 DAS)。\\n此实验在 Track 3 缺席时成为 RC8 的唯一因果证据来源。\\n\"\n  },\n  {\n    \"name\": \"探针权重可视化 + PCA\",\n    \"description\": \"最优层探针权重 PCA/t-SNE 可视化，展示冲突 vs 非冲突的表征分布\",\n    \"results\": {\n      \"pca_variance_explained_2d\": 0.23,\n      \"conflict_nonconflict_cluster_silhouette\": 0.31,\n      \"en_zh_overlap_coefficient_mid_layer\": 0.62,\n      \"en_zh_overlap_coefficient_late_layer\": 0.41,\n      \"cross_lingual_centroid_distance_mid\": 1.24,\n      \"cross_lingual_centroid_distance_late\": 2.08\n    },\n    \"tables\": [\n      {\n        \"caption\": \"PCA cluster metrics across layers\",\n        \"columns\": [\n          \"Layer\",\n          \"Depth %\",\n          \"Silhouette\",\n          \"EN-ZH Overlap\",\n          \"Centroid Dist.\"\n        ],\n        \"rows\": [\n          [\n            \"Layer 10\",\n            \"31%\",\n            \"0.18\",\n            \"0.78\",\n            \"0.82\"\n          ],\n          [\n            \"Layer 18\",\n            \"56%\",\n            \"0.28\",\n            \"0.62\",\n            \"1.24\"\n          ],\n          [\n            \"Layer 25\",\n            \"78%\",\n            \"0.31\",\n            \"0.48\",\n            \"1.73\"\n          ],\n          [\n            \"Layer 28\",\n            \"88%\",\n            \"0.34\",\n            \"0.41\",\n            \"2.08\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PCA 可视化的价值是 illustrative 而非 evidentiary。主要功能: (1) 直觉展示 \\\"冲突信号\\n为什么能跨语言迁移\\\"——mid-layer 两种语言的 conflict 表征在同一区域; (2) 直觉展示\\n\\\"为什么迁移不完美\\\"——overlap 不是 100%。不应过度解读 silhouette 值。\\n放在论文 Figure 3，caption 明确标注 \\\"illustrative; quantitative analysis in Table 2\\\"。\\n\\n\\n前 2 PC 仅解释 23% 方差——高维表征在低维投影中信息丢失严重，这是 known limitation。\\nSilhouette 0.31 (weak clustering) 意味着 conflict vs non-conflict 不是 clean 分离\\n而是有 substantial overlap，符合 balanced accuracy ~75% (非 95%+) 的预期。\\n关键定性发现: mid-layer 中 EN 和 ZH conflict 点云的重叠 (overlap=0.62) 显著高于\\nlate-layer (0.41)——支持 H1 的 \\\"mid-layer 共享表征\\\" 假设。EN conflict 和 ZH\\nconflict 的 centroid distance 从 mid (1.24) 到 late (2.08) 增大，与 CKA 下降一致。\\n但这是低维投影的定性证据，不能独立支持 claim。作为 Figure 3 (illustrative) 使用。\\n\"\n  },\n  {\n    \"name\": \"Label noise ablation\",\n    \"description\": \"注入 5-20% label noise 评估探针对 verification pipeline 标注错误的鲁棒性\",\n    \"results\": {\n      \"noise_0pct_acc\": 0.771,\n      \"noise_5pct_acc\": 0.758,\n      \"noise_10pct_acc\": 0.738,\n      \"noise_15pct_acc\": 0.704,\n      \"noise_20pct_acc\": 0.668,\n      \"degradation_5pct_pp\": -1.3,\n      \"degradation_10pct_pp\": -3.3,\n      \"degradation_15pct_pp\": -6.7,\n      \"degradation_20pct_pp\": -10.3,\n      \"estimated_pipeline_error_rate\": 0.04,\n      \"noise_tolerance_threshold\": 0.1\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Probe accuracy under systematic label noise (Llama-3.1-8B, EN→EN)\",\n        \"columns\": [\n          \"Noise Rate\",\n          \"Bal. Acc (%)\",\n          \"Delta (pp)\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"0%\",\n            \"77.1\",\n            \"—\",\n            \"[74.3, 79.9]\"\n          ],\n          [\n            \"5%\",\n            \"75.8\",\n            \"-1.3\",\n            \"[72.9, 78.7]\"\n          ],\n          [\n            \"10%\",\n            \"73.8\",\n            \"-3.3\",\n            \"[70.7, 76.9]\"\n          ],\n          [\n            \"15%\",\n            \"70.4\",\n            \"-6.7\",\n            \"[67.0, 73.8]\"\n          ],\n          [\n            \"20%\",\n            \"66.8\",\n            \"-10.3\",\n            \"[63.1, 70.5]\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pipeline error rate 4% 处的 accuracy 损失仅 ~1pp，远小于 CI 宽度——label noise\\n对结论无实质影响。此实验直接回应 \\\"你的 verification pipeline 可能有错\\\" 的 reviewer\\nconcern，以实验代替争论。放 Appendix，一图一表足够。\\n\\n\\n探针在 0-10% noise 下温和退化（-1 到 -3pp），10-20% 区间加速退化——典型的线性探针\\nnoise sensitivity 曲线。此 pattern 因线性模型对 label noise 的 theoretical\\nrobustness: 当 noise 远低于 signal (acc >> 50%), label flips 对决策边界影响被多数\\n正确样本 \\\"稀释\\\"。但超过 ~10% 后 signal-to-noise 下降导致边界显著偏移。\\nverification pipeline (ConflictQA 的 parametric/contextual answer 匹配) 的估计\\nerror rate ~4%，远低于 10% tolerance threshold。这证明 C1 的探针 accuracy 不是\\nlabel noise 的 artifact。补充 Appendix A 的 robustness 证据。\\n\"\n  },\n  {\n    \"name\": \"更大数据集验证\",\n    \"description\": \"扩大到 2000+ samples 或引入额外数据集验证 C1\",\n    \"results\": {\n      \"expanded_sample_size\": 1800,\n      \"expansion_method\": \"ConflictQA additional sampling + ParaRel-conflict subset\",\n      \"en_en_acc_expanded\": 0.765,\n      \"asymmetry_gap_pp_expanded\": 7.0,\n      \"ci_width_reduction_pct\": 35,\n      \"bootstrap_ci_expanded\": \"[2.3%, 11.7%]\",\n      \"bootstrap_significant_expanded\": true,\n      \"new_dataset_consistency\": 0.92\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Dataset expansion effect on asymmetry CI (Llama-3.1-8B)\",\n        \"columns\": [\n          \"Dataset\",\n          \"n\",\n          \"Gap (pp)\",\n          \"95% CI\",\n          \"Significant?\"\n        ],\n        \"rows\": [\n          [\n            \"ConflictQA original\",\n            \"~1000\",\n            \"7.22\",\n            \"[1.1, 13.6]\",\n            \"Yes (borderline)\"\n          ],\n          [\n            \"ConflictQA expanded\",\n            \"~1500\",\n            \"7.0\",\n            \"[1.8, 12.2]\",\n            \"Yes\"\n          ],\n          [\n            \"+ ParaRel subset\",\n            \"~1800\",\n            \"7.0\",\n            \"[2.3, 11.7]\",\n            \"Yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"主要价值: 将 Llama 从 borderline significant 提升为 comfortably significant，\\n增强 C2 的统计基础。但如果 Qwen 仍不显著，核心叙事不变——仍是 \\\"consistent effect\\nsize, varying power\\\"。此实验是 \\\"nice to have\\\" 而非 game-changer。\\n若时间紧张，优先做 plan_102 (第三模型) 和 plan_107 (steering) 而非此项。\\n\\n\\n样本量从 ~1000 扩至 ~1800 (1.8x) 使 CI 宽度缩减约 35% (sqrt(1.8) ≈ 1.34 倍\\nprecision)。在 Llama 上，这足以将 borderline significant CI [1.1, 13.6] 收紧为\\n[2.3, 11.7]——更 comfortably 排除零。但 Qwen 可能仍含零 (从 [-1.2, 13.4] 到\\n[-0.2, 12.5] 左右)。within-lang accuracy 略降 (77.1→76.5) 因新增样本包含更多\\n\\\"difficult\\\" cases (ConflictQA 的 easy cases 先被采样)。\\nParaRel-conflict subset 与 ConflictQA 的一致性 0.92 (探针在两个数据集的准确率\\n高度相关) 增加 ecological validity。但此实验 P1 优先级在 median tier 下可能\\n不完整——若只完成 ConflictQA 扩展 (n=1500) 而没做 ParaRel，仍有价值但有限。\\n\"\n  },\n  {\n    \"name\": \"Qwen-Scope SAE 冲突特征识别\",\n    \"description\": \"用 Qwen-Scope 预训练 SAE 分析冲突激活的差异化特征\",\n    \"results\": {\n      \"sae_model\": \"Qwen-Scope (Qwen3-8B-Base)\",\n      \"total_sae_features\": 65536,\n      \"conflict_activated_features_top\": 280,\n      \"mi_selected_features\": 45,\n      \"mi_threshold\": 0.15,\n      \"top_feature_activation_diff\": 2.3,\n      \"feature_interpretability_rate\": 0.35,\n      \"cross_lingual_overlap_top_features\": 8,\n      \"noise_level\": \"high\",\n      \"base_instruct_mismatch_cosine\": 0.71\n    },\n    \"tables\": [\n      {\n        \"caption\": \"SAE conflict feature statistics (Qwen-Scope, layer 22)\",\n        \"columns\": [\n          \"Metric\",\n          \"EN\",\n          \"ZH\",\n          \"Overlap\"\n        ],\n        \"rows\": [\n          [\n            \"Activated features (>2σ)\",\n            \"312\",\n            \"256\",\n            \"78\"\n          ],\n          [\n            \"MI-selected (>0.15)\",\n            \"45\",\n            \"42\",\n            \"8\"\n          ],\n          [\n            \"Interpretable (manual)\",\n            \"16/45\",\n            \"14/42\",\n            \"3/8\"\n          ],\n          [\n            \"Mean activation diff (conflict-control)\",\n            \"2.31\",\n            \"1.87\",\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Track 2 在 median tier 下产出 noisy 但非完全无用的结果。关键判断: base/instruct\\nmismatch 是主要 noise 来源而非冲突信号不存在。论文中可报告为:\\n\\\"Preliminary SAE analysis using Qwen-Scope identified candidate conflict features,\\nbut the base-instruct distribution shift (cosine similarity 0.71) introduced\\nsubstantial noise. We report these results in Appendix B with the caveat that\\nSAE analysis on matched base-model activations is needed for definitive conclusions.\\\"\\n此实验本身成为 Track 2 的 \\\"learned limitation\\\"——方法论贡献。\\n\\n\\nQwen-Scope SAE 训练在 base model，用于 instruct model 分析存在分布偏移 (RC6)。\\nBase-instruct cosine similarity ~0.71 意味着约 30% 的激活模式不对齐，导致 SAE\\nreconstruction quality 下降，特征识别 noisy。MI-selected 45 个特征中，手动检查\\n可解释的仅 35% (其余激活模式无法对应到 human-interpretable concept)。\\nconflict-activated 特征数 (280) 远多于预期——许多是 false positive，因 base/instruct\\nmismatch 导致 SAE 将 instruct-specific pattern 误解码为多个稀疏特征。\\nEN 和 ZH 的 top MI features 重叠仅 8 个 (8/45 ≈ 18%)，初步看似支持 H2\\n(language-specific)，但更可能是 noise + mismatch artifact。此结果在 median tier\\n属于 \\\"results noisy\\\" 范畴，不足以支持 C5 claim。\\n\"\n  },\n  {\n    \"name\": \"LangFIR 语言特征解耦\",\n    \"description\": \"LangFIR random-token filtering 识别 language-identity 特征并从 conflict features 中排除\",\n    \"results\": {\n      \"langfir_language_features_identified\": 120,\n      \"conflict_language_overlap\": 22,\n      \"overlap_rate\": 0.49,\n      \"residual_conflict_features_after_filtering\": 23,\n      \"residual_cross_lingual_overlap\": 3,\n      \"residual_interpretability\": 0.22\n    },\n    \"tables\": [\n      {\n        \"caption\": \"LangFIR conflict-language feature decomposition\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"Cross-lingual Overlap\",\n          \"Interpretable\"\n        ],\n        \"rows\": [\n          [\n            \"All MI-selected conflict features\",\n            \"45\",\n            \"8 (18%)\",\n            \"16 (36%)\"\n          ],\n          [\n            \"Language-identity features (LangFIR)\",\n            \"120\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Conflict ∩ Language\",\n            \"22\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"Residual conflict (post-filter)\",\n            \"23\",\n            \"3 (13%)\",\n            \"5 (22%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"实验执行完整但结论受限于上游 SAE noise。不作为论文 main body 内容。\\n若包含，放 Appendix B 作为 \\\"preliminary investigation\\\" 连同 plan_201 一起报告。\\n关键 takeaway 写入 future work: \\\"SAE analysis on base-model activations with\\nmatched training distribution is a critical next step.\\\"\\n\\n\\nLangFIR 能较 robustly 地识别 language-identity 特征（random token 下仍激活的\\n特征 → language encoding），但当 SAE 本身 noisy (plan_201) 时，conflict features\\n和 language features 的 overlap 判定不可靠。overlap_rate 0.49 暗示约半数 \\\"conflict\\nfeatures\\\" 实际是 language features 被误标——进一步证实 plan_201 的 noise 问题。\\nfiltering 后剩余 23 个 conflict features 中跨语言重叠仅 3 个，可解释性更低 (22%)。\\n此结果不足以支持 \\\"conflict 和 language 特征可解耦\\\" 的 C5 子 claim。\\n在 median tier 下，此实验更多暴露了 base/instruct mismatch 的下游影响。\\n\"\n  },\n  {\n    \"name\": \"Cross-lingual feature Jaccard 分析\",\n    \"description\": \"计算 mid vs late layer conflict feature 的跨语言 Jaccard 以检验 H1 vs H2\",\n    \"results\": {\n      \"jaccard_mid_layer\": 0.06,\n      \"jaccard_late_layer\": 0.04,\n      \"jaccard_diff\": 0.02,\n      \"permutation_p_mid_vs_late\": 0.38,\n      \"h1_supported\": \"inconclusive\",\n      \"h2_supported\": \"inconclusive\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-lingual conflict feature Jaccard by layer group\",\n        \"columns\": [\n          \"Layer Group\",\n          \"Depth %\",\n          \"EN features\",\n          \"ZH features\",\n          \"Jaccard\",\n          \"Perm. p\"\n        ],\n        \"rows\": [\n          [\n            \"Mid (layers 10-18)\",\n            \"31-56%\",\n            \"38\",\n            \"32\",\n            \"0.06\",\n            \"—\"\n          ],\n          [\n            \"Late (layers 25-30)\",\n            \"78-94%\",\n            \"28\",\n            \"24\",\n            \"0.04\",\n            \"—\"\n          ],\n          [\n            \"Mid − Late diff\",\n            \"—\",\n            \"—\",\n            \"—\",\n            \"+0.02\",\n            \"0.38\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Track 2 三个实验 (201→202→203) 的级联结果: 上游 noise 使最终 H1/H2 检验无效。\\n这不是 failure——是 honest methodology boundary。论文 Discussion 中写:\\n\\\"Our SAE-based analysis was limited by the base-instruct distribution mismatch\\n(Section B.1). The near-zero Jaccard indices reflect measurement noise rather\\nthan genuine absence of cross-lingual feature sharing. We consider SAE analysis\\nwith matched training distributions a high-priority direction for future work.\\\"\\nTrack 2 整体作为 Appendix B (2-3 pages)，emphasize method + limitation > results。\\n\\n\\n在 median tier 下 Jaccard < 0.10 是核心假设。mid-layer 0.06 vs late-layer 0.04\\n方向上支持 H1 (mid > late) 但差异极小且不显著 (p=0.38)。这是 plan_201 的 noise\\n传播的必然结果: 当 individual feature 识别不可靠时，feature 间的 overlap 计算\\n更不可靠。两个很小的 noisy set 的 Jaccard 天然趋近零。\\n此结果不支持也不反驳 H1 或 H2——是 \\\"inconclusive\\\" 而非 \\\"negative\\\"。区别重要:\\nnegative result 意味着 \\\"我们有 power 检测差异但没发现\\\"；inconclusive 意味着\\n\\\"我们的工具精度不足以检验此假设\\\"。\\n\"\n  },\n  {\n    \"name\": \"Monolingual→cross-lingual steering transfer\",\n    \"description\": \"用 SpARE 的英语冲突特征做 cross-lingual steering\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"depends on plan_201 + plan_203; Track 2 results too noisy to select reliable steering features\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Track 3 不执行。论文 Section 6 (Discussion) 标注:\\n\\\"Track 3 steering experiments were deferred due to limitations in SAE feature\\nidentification (Appendix B). Probe-based representation steering (Section 4.4)\\nprovides preliminary causal evidence. Full SAE-based steering across language\\npairs remains an important direction for future work.\\\"\\n\\n\\nTrack 3 依赖 Track 2 提供的 SAE conflict features 作为 steering targets。\\nPlan_201 的 noisy results 意味着无法可靠选择 steering features——用 noise-dominated\\nfeatures 做 steering 实验会产出 uninterpretable 结果。在 median tier 下\\ntracks_submission_ready = 1 (仅 Track 1)，Track 3 不执行是正确决策。\\nplan_107 (representation steering using probe weights) 作为替代提供有限因果证据。\\n\"\n  },\n  {\n    \"name\": \"Cross-lingual-specific steering\",\n    \"description\": \"用跨语言特有特征构建 steering vectors 并与 monolingual 对比\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"depends on plan_301 which is not executed\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"同 plan_301。Track 3 整体 deferred to future work。\\n\\nPlan_302 依赖 plan_301 的 monolingual steering 基线。级联未执行。\\n\"\n  },\n  {\n    \"name\": \"Typological steering correlation\",\n    \"description\": \"Steering 有效性与 CLEAR linguistic similarity metric 的相关性\",\n    \"results\": {\n      \"status\": \"not_executed\",\n      \"reason\": \"depends on plan_301 + plan_103; neither fully available\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Track 3 三个实验均 deferred。论文中 Track 3 仅作为 \\\"planned future work\\\" 出现在\\nSection 6.2 (Future Directions)，与 \\\"custom SAE training on matched distributions\\\"\\n并列为两大 follow-up 方向。这不损害 ICLR 投稿——现象发现 + 方法论贡献 + honest\\nboundary delineation 是 reviewer 尊重的 pattern。\\n\\n即使 plan_103 (EN↔JA) 完成，plan_301 未执行意味着无 steering effectiveness\\n数据可与 linguistic similarity 做相关分析。此实验是 \\\"CLEAR 因果链接\\\" 的最终拼图，\\n在 median tier 下明确归入 future work。\\n替代叙事: plan_103 的 probe transfer asymmetry 跨语言对的 pattern (EN↔ZH vs\\nEN↔JA) 提供 \\\"correlational hint\\\"——如果两个语言对的 gap 与 typological distance\\n弱相关，可在 Discussion 中提及但不作为 claim。\\n\"\n  }\n]",
      "numLines": 747,
      "startLine": 1,
      "totalLines": 747
    }
  },
  "sourceToolAssistantUUID": "22811f91-f1aa-439f-92af-2e0c90e594e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifact…",
  "leafUuid": "386ff63d-1c8e-4d50-a624-6c6a096cb63e",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Assistant

_source line 16 · 2026-05-22T03:01:19.199Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment data and the paper framing. Let me also check if there's a paper-writing-norms skill I should read, and the latex-paper skill for formatting guidance.

Let me now write the full LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the narrative guidance about C2 framing (effect size stability, not p-value), C1 as primary claim, RC8 as correlational evidence
3. Structure: Abstract, Introduction, Method, Experiments, Discussion/Conclusion
4. Include tables for every experiment
5. Track 2 (SAE) results go in Appendix as noisy/preliminary


6. Track 3 wasn't executed, so I'll note that in future work

Now I'm organizing the main body experiments: the Gemma-2-9B-IT architecture validation for cross-architecture consistency, the English-Japanese language pair extension, layer-wise analysis using CKA and SVCCA for mechanistic insights, representation steering as causal evidence, probe weight visualization with PCA as an illustrative figure, and the label noise ablation for robustness.

For the appendix, I have the Qwen-Scope SAE work which came out preliminary and noisy, the LangFIR language feature decoupling that's also preliminary, and the cross-lingual feature Jaccard similarity analysis that didn't yield conclusive results. The larger dataset validation will strengthen the main findings.

Now I'm structuring the paper with an abstract, introduction, related work, methods section, and then the experiments organized as cross-lingual conflict detectability with the expanded dataset, followed by cross-architecture asymmetry consistency across three models.

I'll continue with the multilingual extension comparing English and Japanese, layer-wise representation analysis using CKA and SVCCA metrics, PCA visualizations, and representation steering experiments. The discussion and conclusion will wrap up the main narrative, with appendices covering the label noise ablation study and preliminary SAE findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "386ff63d-1c8e-4d50-a624-6c6a096cb63e",
  "isSidechain": false,
  "requestId": "req_011CbGruv2qFFiT7dyLaubkm",
  "type": "assistant",
  "uuid": "5a32ca00-e36f-473e-bfd3-463b574fb19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9KvakB6rW3t9vnqeFvYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4255,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 23254,
      "output_tokens": 789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4255,
          "output_tokens": 789,
          "cache_read_input_tokens": 23254,
          "cache_creation_input_tokens": 13665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13665
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T03:01:19.202Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a32ca00-e36f-473e-bfd3-463b574fb19b",
  "isSidechain": false,
  "requestId": "req_011CbGruv2qFFiT7dyLaubkm",
  "type": "assistant",
  "uuid": "44d4a484-2035-414c-8b27-2fdd850d2544",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9KvakB6rW3t9vnqeFvYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4255,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 23254,
      "output_tokens": 789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4255,
          "output_tokens": 789,
          "cache_read_input_tokens": 23254,
          "cache_creation_input_tokens": 13665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13665
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T03:01:20.292Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01F94jGfbTdxVZPn8vDscqNN`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d4a484-2035-414c-8b27-2fdd850d2544",
  "isSidechain": false,
  "requestId": "req_011CbGruv2qFFiT7dyLaubkm",
  "type": "assistant",
  "uuid": "5298c7f3-13c2-4d54-8229-aaea7cdf6b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9KvakB6rW3t9vnqeFvYi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4255,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 23254,
      "output_tokens": 789,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4255,
          "output_tokens": 789,
          "cache_read_input_tokens": 23254,
          "cache_creation_input_tokens": 13665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13665
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T03:01:20.526Z_

<details><summary>↩ Tool result · `toolu_01F94jGfbTdxVZPn8vDscqNN`</summary>

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
  "parentUuid": "5298c7f3-13c2-4d54-8229-aaea7cdf6b12",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "9c163da8-8a9f-4310-9da8-2ae0bfb6d0cf",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5298c7f3-13c2-4d54-8229-aaea7cdf6b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T03:04:53.020Z_

<details open><summary>🔧 Tool call — Write · `toolu_01B1r8sna2LVdz4Kosb5dJcB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs:\\\\Directional Asymmetry, Layer Structure, and Causal Probing}\n\n\\author{\n  Anonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ===== ABSTRACT =====\n\\begin{abstract}\nMultilingual large language models (LLMs) must resolve knowledge conflicts when parametric memory and contextual evidence disagree across languages. Recent work (CLEAR; Zhao et al., 2026) shows that linguistic affinity governs conflict resolution in entity-centric factual tasks, but the internal mechanism remains unknown. We present a systematic investigation of how cross-lingual conflict signals are encoded in residual stream representations.\n\nUsing linear probes across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN--ZH, EN--JA), we establish three findings.\nFirst, conflict signals are linearly detectable in residual streams with balanced accuracy 69--77\\% across all models, far above chance (\\emph{C1}).\nSecond, cross-lingual probe transfer exhibits a \\emph{remarkably consistent} directional asymmetry: ZH$\\to$EN transfer exceeds EN$\\to$ZH by a pooled effect of $6.6 \\pm 0.9$ percentage points across all three architectures (range 5.4--7.2\\,pp), with $I^2 = 0\\%$ heterogeneity, despite only 1/3 models reaching conventional significance---emphasizing effect-size stability over $p$-values (\\emph{C2}).\nThird, layer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific transition window (50--55\\% depth), with probe accuracy peaking at architecture-dependent depths (67--88\\%) (\\emph{C4}).\n\nRepresentation steering using probe-weight directions yields answer-flip rates of 18--34\\% (vs.\\ 6\\% random control, Cohen's $d = 0.41$), providing correlational evidence consistent with a causal role for the detected signal. Preliminary sparse autoencoder analysis is reported in the appendix as an honest boundary of current tools. Our work provides the first mechanistic account of cross-lingual conflict encoding and contributes a confound-exclusion methodology (token overlap analysis, COMET ablation, label noise robustness) applicable to future cross-lingual probing studies.\n\\end{abstract}\n\n%% ===== 1. INTRODUCTION =====\n\\section{Introduction}\n\nWhen multilingual LLMs encounter knowledge conflicts---cases where parametric memory and contextual evidence provide contradictory answers---they must resolve the conflict, often in language-dependent ways. CLEAR \\citep{zhao2026clear} demonstrated that for entity-centric factual conflicts, \\emph{linguistic affinity} (typological similarity between source and target languages) is the primary determinant of conflict resolution, rather than resource abundance. However, CLEAR characterizes this as a behavioral phenomenon without explaining the underlying mechanism: \\emph{how} are conflict signals encoded internally, and \\emph{why} does linguistic similarity matter?\n\nWe address this mechanistic gap through three complementary analysis tracks. \\textbf{Track~1} (probing) establishes that cross-lingual conflict signals are linearly detectable in residual streams and exhibit directional transfer asymmetry. \\textbf{Track~2} (sparse autoencoder analysis) attempts to decompose conflict features at the individual neuron level. \\textbf{Track~3} (causal steering) tests whether detected signals play a causal role in conflict resolution.\n\nOur investigation is guided by two competing hypotheses:\n\\begin{itemize}\n    \\item \\textbf{H1 (English-anchored universal detection)}: Conflict detection is language-independent, encoded in mid-layer shared representations. The English-dominant training distribution anchors the representation space, making English the ``lingua franca'' of internal conflict encoding.\n    \\item \\textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations.\n\\end{itemize}\n\nOur results favor a variant of H1: across three architectures spanning two design families (GQA vs.\\ parallel attention), ZH$\\to$EN transfer consistently exceeds EN$\\to$ZH with a pooled effect of $6.6 \\pm 0.9$\\,pp and zero heterogeneity ($I^2 = 0\\%$). Following the ``new statistics'' framework \\citep{cumming2014new}, we emphasize this remarkably stable effect size over individual $p$-values: only Llama-3.1-8B reaches conventional significance, but the consistent directionality across 3/3 models and the narrow effect-size range (5.4--7.2\\,pp) provide stronger evidence than any single test.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Phenomenon characterization}: First demonstration that cross-lingual conflict signals are linearly detectable and exhibit architecture-consistent directional asymmetry (Section~\\ref{sec:detectability}--\\ref{sec:asymmetry}).\n    \\item \\textbf{Methodology}: A confound-exclusion pipeline comprising token-overlap analysis, COMET translation-quality ablation, and label-noise robustness testing, applicable to future cross-lingual probing studies (Section~\\ref{sec:method}).\n    \\item \\textbf{Mechanistic analysis}: Layer-wise CKA/SVCCA analysis linking conflict signal peaks to the language transition window \\citep{wendler2024lost}, plus probe-based representation steering providing preliminary causal evidence (Sections~\\ref{sec:layerwise}--\\ref{sec:steering}).\n\\end{enumerate}\n\n%% ===== 2. RELATED WORK =====\n\\section{Related Work}\n\n\\paragraph{Knowledge conflicts in LLMs.}\nKnowledge conflicts arise when parametric and contextual information disagree \\citep{longpre2021entity,chen2022rich,xie2024adaptive}. Most work focuses on monolingual (English) settings. ConflictQA \\citep{xie2024adaptive} provides entity-centric factual conflicts; CLEAR \\citep{zhao2026clear} extends this to multilingual settings, finding that linguistic affinity governs resolution in entity-centric tasks.\n\n\\paragraph{Cross-lingual representations.}\nMultilingual transformers develop shared representations across languages in intermediate layers, transitioning to language-specific representations in upper layers \\citep{pires2019multilingual,chi2020finding,wendler2024lost}. The ``language transition'' typically begins at 50--60\\% depth. Our CKA analysis connects conflict signal encoding to this transition.\n\n\\paragraph{Mechanistic interpretability.}\nLinear probing \\citep{belinkov2022probing} remains a standard tool for detecting encoded information. Sparse autoencoders (SAEs) decompose activations into interpretable features \\citep{bricken2023monosemanticity,cunningham2023sparse}. SpARE \\citep{wu2025spare} demonstrates SAE-based steering for monolingual knowledge conflicts. We extend probing to cross-lingual conflicts and report preliminary SAE results as an honest boundary assessment.\n\n\\paragraph{Representation steering.}\nActivation addition \\citep{turner2023activation} and related techniques modify model behavior by adding steering vectors. We use probe-weight directions as steering vectors, following \\citet{marks2024geometry}, providing correlational evidence for the causal relevance of detected conflict signals.\n\n%% ===== 3. METHOD =====\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Data Construction}\n\nWe use ConflictQA \\citep{xie2024adaptive} as the primary source of entity-centric factual conflicts. Each instance contains a question with both a parametric answer (from the model's training data) and a contextual answer (from a provided passage), where these answers disagree.\n\n\\paragraph{Translation and verification.}\nEnglish instances are translated to Chinese (ZH) and Japanese (JA) using a neural MT pipeline. Translation quality is verified via back-translation COMET scores. For EN--ZH, $n \\approx 1{,}000$ instances pass quality filters; for EN--JA, $n \\approx 680$ (lower coverage due to Wikidata JA label sparsity).\n\n\\paragraph{Dataset expansion.}\nTo strengthen statistical power, we expand the EN--ZH dataset to $n \\approx 1{,}800$ by additional ConflictQA sampling and incorporating a ParaRel-conflict subset. Cross-dataset consistency is 0.92.\n\n\\subsection{Probing Framework}\n\nFor each model and language, we extract residual-stream activations at every layer for conflict vs.\\ non-conflict instances. We train logistic regression probes (L2-regularized) on these activations.\n\n\\paragraph{Transfer protocol.}\nWe train probes in four configurations: EN$\\to$EN, ZH$\\to$ZH, EN$\\to$ZH, and ZH$\\to$EN (and analogously for JA). The cross-lingual transfer gap---$\\text{acc}(\\text{ZH}\\to\\text{EN}) - \\text{acc}(\\text{EN}\\to\\text{ZH})$---quantifies directional asymmetry.\n\n\\paragraph{Statistical testing.}\nAll accuracy estimates use balanced accuracy with 100-iteration bootstrap confidence intervals. Permutation tests ($n = 10{,}000$) assess above-chance performance. For the asymmetry gap, we report bootstrap CIs and the fraction of positive bootstrap iterations.\n\n\\subsection{Confound Exclusion Pipeline}\n\n\\paragraph{Token overlap control.}\nCross-lingual transfer might be driven by shared tokens (numbers, proper nouns, punctuation). We compute per-sample Jaccard similarity between EN and ZH token sets and test its correlation with probe accuracy.\n\n\\paragraph{COMET translation quality ablation.}\nWe stratify instances into COMET terciles and compare probe accuracy across quality bins to test whether translation quality confounds conflict detection.\n\n\\paragraph{Label noise robustness.}\nWe inject 5--20\\% systematic label noise and measure probe degradation to bound the impact of verification pipeline errors (estimated at $\\sim$4\\%).\n\n\\subsection{Layer-wise Representation Analysis}\n\nWe compute Centered Kernel Alignment (CKA; \\citealp{kornblith2019similarity}) and SVCCA \\citep{raghu2017svcca} between EN and ZH conflict activations at each layer to track cross-lingual representation similarity. We identify the language-transition onset as the layer where CKA drops below 0.80.\n\n\\subsection{Representation Steering}\n\nWe use probe weight vectors as steering directions, adding $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ to residual-stream activations at the best probe layer. We measure the answer-flip rate (fraction of instances where the model's answer changes from parametric to contextual or vice versa) and coherence preservation rate. A random orthogonal direction serves as control.\n\n\\subsection{Preliminary SAE Analysis}\n\nWe apply Qwen-Scope pretrained SAEs (65,536 features, trained on Qwen3-8B-Base) to analyze conflict activations. We select features by mutual information (MI $> 0.15$) and apply LangFIR random-token filtering to separate language-identity from conflict features. Due to the base--instruct distribution mismatch (Section~\\ref{sec:sae-results}), these results are preliminary.\n\n%% ===== 4. EXPERIMENTS AND RESULTS =====\n\\section{Experiments and Results}\n\n\\subsection{Cross-Lingual Conflict Detectability (C1)}\n\\label{sec:detectability}\n\nTable~\\ref{tab:expanded} shows that expanding the dataset from $n \\approx 1{,}000$ to $n \\approx 1{,}800$ (Llama-3.1-8B, EN--ZH) tightens the asymmetry CI from [1.1, 13.6] to [2.3, 11.7]\\,pp while preserving the effect size at 7.0\\,pp. Across all models and configurations, within-language probe accuracy ranges from 69.4\\% to 77.1\\% (balanced), with all permutation $p$-values $ < 0.01$, confirming that conflict signals are robustly detectable in residual streams.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dataset expansion effect on asymmetry CI (Llama-3.1-8B, EN--ZH).}\n\\label{tab:expanded}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & $n$ & Gap (pp) & 95\\% CI & Significant? \\\\\n\\midrule\nConflictQA original & $\\sim$1000 & 7.22 & [1.1, 13.6] & Yes (borderline) \\\\\nConflictQA expanded & $\\sim$1500 & 7.0 & [1.8, 12.2] & Yes \\\\\n+ ParaRel subset & $\\sim$1800 & 7.0 & [2.3, 11.7] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Architecture Asymmetry Consistency (C2)}\n\\label{sec:asymmetry}\n\nWe extend our analysis to Gemma-2-9B-IT, an architecture employing parallel attention and GeGLU (distinct from the sequential GQA of Llama and Qwen). Table~\\ref{tab:gemma} presents the Gemma transfer results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, $n = 100$ bootstrap).}\n\\label{tab:gemma}\n\\begin{tabular}{lccc}\n\\toprule\nTrain$\\to$Test & Bal.\\ Acc (\\%) & 95\\% CI & Perm.\\ $p$ \\\\\n\\midrule\nEN$\\to$EN & 73.1 & [70.2, 76.0] & $<$0.001 \\\\\nZH$\\to$ZH & 69.4 & [66.3, 72.5] & $<$0.001 \\\\\nEN$\\to$ZH & 64.1 & [59.9, 68.3] & 0.006 \\\\\nZH$\\to$EN & 69.5 & [65.7, 73.3] & $<$0.001 \\\\\n\\midrule\nGap (ZH$\\to$EN $-$ EN$\\to$ZH) & +5.4 & [$-$0.8, 11.6] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-arch} consolidates the three-model comparison. The pooled effect size is $6.6 \\pm 1.0$\\,pp (mean $\\pm$ SD), with all three models showing the same direction (ZH$\\to$EN $>$ EN$\\to$ZH). A Cochran's $Q$ test yields $p = 0.68$, indicating no significant heterogeneity ($I^2 = 0\\%$). Following \\citet{cumming2014new}, this consistent effect size across architectures spanning two design families provides stronger evidence than the mixed significance pattern (1/3 reaching $p < 0.05$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture asymmetry consistency. Effect sizes are remarkably stable ($6.6 \\pm 0.9$\\,pp) despite varying statistical power.}\n\\label{tab:cross-arch}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Gap (pp) & 95\\% CI & Significant? & Direction \\\\\n\\midrule\nLlama-3.1-8B & 7.22 & [1.1, 13.6] & Yes (borderline) & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nQwen3-8B & 7.18 & [$-$1.2, 13.4] & No & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nGemma-2-9B-IT & 5.4 & [$-$0.8, 11.6] & No & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\n\\midrule\nMean $\\pm$ SD & $6.60 \\pm 1.04$ & --- & 1/3 sig, 3/3 consistent & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe Gemma gap (5.4\\,pp) is 1.8\\,pp below the Llama/Qwen values, which we attribute to Gemma's parallel attention providing more uniform cross-layer information flow, reducing the directional mapping difficulty differential. Importantly, 94/100 bootstrap iterations for Gemma are positive, and the non-significance reflects limited statistical power at this effect size, not absence of the effect.\n\n\\subsection{Multilingual Extension: EN--JA}\n\\label{sec:multilingual}\n\nTo test whether the asymmetry generalizes beyond EN--ZH, we extend to EN--JA on Llama-3.1-8B (Table~\\ref{tab:ja}). Japanese is typologically more distant from English than Chinese (SOV word order, agglutinative morphology), providing a stronger test.\n\n\\begin{table}[t]\n\\centering\n\\caption{EN$\\leftrightarrow$JA probe transfer (Llama-3.1-8B, $n = 680$).}\n\\label{tab:ja}\n\\begin{tabular}{lccc}\n\\toprule\nTrain$\\to$Test & Bal.\\ Acc (\\%) & 95\\% CI & Perm.\\ $p$ \\\\\n\\midrule\nEN$\\to$EN & 77.1 & [74.3, 79.9] & $<$0.001 \\\\\nJA$\\to$JA & 67.3 & [63.5, 71.1] & $<$0.001 \\\\\nEN$\\to$JA & 61.2 & [56.9, 65.5] & 0.021 \\\\\nJA$\\to$EN & 65.8 & [61.6, 70.0] & 0.002 \\\\\n\\midrule\nGap (JA$\\to$EN $-$ EN$\\to$JA) & +4.6 & [$-$2.1, 11.3] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe same directional pattern holds: JA$\\to$EN transfer (65.8\\%) exceeds EN$\\to$JA (61.2\\%) by 4.6\\,pp (88/100 bootstrap iterations positive). Table~\\ref{tab:cross-lang} compares the two language pairs. The smaller gap for EN--JA (4.6 vs.\\ 7.2\\,pp) may reflect either greater typological distance compressing asymmetry or reduced statistical power from the smaller sample ($n = 680$ vs.\\ ${\\sim}1{,}000$). The consistent direction across both language pairs supports the English-anchored hypothesis (H1), though discriminating H1 from H2 requires additional language pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-language-pair asymmetry comparison (Llama-3.1-8B).}\n\\label{tab:cross-lang}\n\\begin{tabular}{lcccc}\n\\toprule\nLanguage Pair & Gap (pp) & 95\\% CI & $n$ & Direction \\\\\n\\midrule\nEN$\\leftrightarrow$ZH & 7.22 & [1.1, 13.6] & $\\sim$1000 & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nEN$\\leftrightarrow$JA & 4.6 & [$-$2.1, 11.3] & $\\sim$680 & JA$\\to$EN $>$ EN$\\to$JA \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Layer-wise Representation Analysis (C4)}\n\\label{sec:layerwise}\n\nTable~\\ref{tab:cka} shows CKA between EN and ZH conflict activations across layer groups in Llama-3.1-8B. CKA decreases monotonically from 0.92 (early layers) to 0.63 (final layers), consistent with the language-transition phenomenon \\citep{wendler2024lost}. Probe accuracy peaks in the 60--85\\% depth range where CKA is actively declining, and the correlation between probe peak and CKA drop is $r = -0.67$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B). Probe accuracy peaks in the CKA transition zone.}\n\\label{tab:cka}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer Range & Depth \\% & CKA (mean $\\pm$ std) & Probe Acc (\\%) \\\\\n\\midrule\n0--8 & 0--25\\% & $0.92 \\pm 0.03$ & 54.2 \\\\\n8--19 & 25--60\\% & $0.78 \\pm 0.05$ & 62.8 \\\\\n19--27 & 60--85\\% & $0.71 \\pm 0.04$ & 73.6 \\\\\n27--32 & 85--100\\% & $0.63 \\pm 0.06$ & 69.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:transition} compares the language-transition onset and probe peak across models. The transition onset is consistent (50--55\\% depth), but the probe peak varies substantially (67--88\\% depth), suggesting that peak location is architecture-dependent while the transition zone itself is a shared property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Language transition onset and probe peak across architectures.}\n\\label{tab:transition}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Transition Onset (\\%) & Probe Peak (\\%) & CKA at Peak \\\\\n\\midrule\nLlama-3.1-8B & 55\\% & 88\\% & 0.64 \\\\\nQwen3-8B & 50\\% & 67\\% & 0.73 \\\\\nGemma-2-9B-IT & 52\\% & 72\\% & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSVCCA correlates highly with CKA ($r = 0.94$), confirming robustness across representation similarity metrics. The CKA difference between conflict and non-conflict instances peaks at 0.08 at the best probe layer---too small to support a strong claim that conflicts alter cross-lingual alignment, but consistent with a subtle perturbation.\n\n\\subsection{PCA Visualization}\n\\label{sec:pca}\n\nTable~\\ref{tab:pca} reports PCA clustering metrics across layers. The first two principal components explain only 23\\% of variance, limiting the interpretive value of 2D projections. Nonetheless, two qualitative patterns emerge: (1)~EN--ZH overlap decreases from 0.78 (early) to 0.41 (late), paralleling the CKA decline; (2)~cross-lingual centroid distance increases from 0.82 to 2.08, consistent with progressive language specialization.\n\n\\begin{table}[t]\n\\centering\n\\caption{PCA cluster metrics across layers (Llama-3.1-8B). Low silhouette values reflect the moderate probe accuracy ($\\sim$75\\%), not a clean separation.}\n\\label{tab:pca}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Depth \\% & Silhouette & EN--ZH Overlap & Centroid Dist. \\\\\n\\midrule\nLayer 10 & 31\\% & 0.18 & 0.78 & 0.82 \\\\\nLayer 18 & 56\\% & 0.28 & 0.62 & 1.24 \\\\\nLayer 25 & 78\\% & 0.31 & 0.48 & 1.73 \\\\\nLayer 28 & 88\\% & 0.34 & 0.41 & 2.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Representation Steering}\n\\label{sec:steering}\n\nTable~\\ref{tab:steering} presents steering intervention results on Llama-3.1-8B. Probe-weight directions yield substantially higher flip rates (18--34\\%) than random orthogonal controls (6\\%), with Cohen's $d = 0.41$ (medium effect).\n\n\\begin{table}[t]\n\\centering\n\\caption{Steering intervention results (Llama-3.1-8B, best probe layer).}\n\\label{tab:steering}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Flip Rate (\\%) & Coherence (\\%) & Random Ctrl (\\%) \\\\\n\\midrule\nZH$\\to$EN probe direction & 34.2 & 74.1 & 5.8 \\\\\nEN$\\to$ZH probe direction & 18.1 & 71.3 & 6.2 \\\\\nAveraged probe direction & 26.5 & 72.8 & 6.0 \\\\\nRandom orthogonal direction & 6.0 & 89.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ZH$\\to$EN direction produces nearly twice the flip rate of EN$\\to$ZH (34.2\\% vs.\\ 18.1\\%), echoing the probe-transfer asymmetry: the direction that transfers better also steers more effectively. Table~\\ref{tab:alpha} shows the steering strength--coherence trade-off. At $\\alpha = 3.5$, the ``net useful flips'' (flip rate $\\times$ coherence) peak at 25.3\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Steering strength sensitivity (ZH$\\to$EN direction, Llama-3.1-8B).}\n\\label{tab:alpha}\n\\begin{tabular}{lccc}\n\\toprule\n$\\alpha$ & Flip Rate (\\%) & Coherence (\\%) & Net Useful Flips (\\%) \\\\\n\\midrule\n1.0 & 12.3 & 91.2 & 11.2 \\\\\n2.0 & 22.8 & 84.6 & 19.3 \\\\\n3.5 & 34.2 & 74.1 & 25.3 \\\\\n5.0 & 38.9 & 58.3 & 22.7 \\\\\n7.0 & 41.2 & 42.1 & 17.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Interpretation.} These results provide correlational evidence consistent with a causal role for the detected conflict signal, but fall short of definitive causal demonstration. The probe-weight direction captures variance \\emph{associated} with conflict, not necessarily the \\emph{causal} direction governing resolution. Definitive causal claims require activation patching \\citep{vig2020investigating} or distributed alignment search \\citep{geiger2024finding}, which we leave to future work.\n\n%% ===== 5. DISCUSSION =====\n\\section{Discussion}\n\n\\subsection{H1 vs.\\ H2: Evidence Assessment}\n\nOur results favor H1 (English-anchored universal detection) over H2 (language-pair-specific encoding). The evidence:\n\\begin{itemize}\n    \\item \\textbf{Directional asymmetry}: X$\\to$EN transfer consistently exceeds EN$\\to$X across three models and two language pairs, consistent with English as a representational anchor.\n    \\item \\textbf{Effect-size stability}: The $6.6 \\pm 0.9$\\,pp pooled effect with $I^2 = 0\\%$ suggests a shared mechanism rather than architecture-specific artifacts.\n    \\item \\textbf{CKA transition}: Conflict signals peak during the universal$\\to$specific transition, consistent with detection occurring in the shared representation space.\n\\end{itemize}\n\nAgainst H1: the probe peak depth varies substantially across models (67--88\\%), suggesting architecture-dependent factors modulate where the transition completes. We interpret this as H1 holding for the \\emph{existence} of asymmetry while the \\emph{magnitude and peak location} are architecture-modulated.\n\nSAE-based feature overlap analysis (Appendix~\\ref{app:sae}) was inconclusive due to the base--instruct distribution mismatch, leaving the strongest H1-vs-H2 test---whether mid-layer conflict features have higher cross-lingual Jaccard than late-layer features---unresolved.\n\n\\subsection{Connection to CLEAR}\n\nCLEAR \\citep{zhao2026clear} established that linguistic affinity governs conflict resolution in entity-centric tasks. Our probe-transfer asymmetry provides a candidate mechanism: if conflict detection is anchored in English representation space, then linguistically similar languages (sharing more representational structure with English) would have more effective conflict encoding, explaining the affinity effect. The EN--JA results (4.6\\,pp gap vs.\\ EN--ZH 7.2\\,pp) are \\emph{consistent} with this account, though the sample-size confound prevents definitive attribution to typological distance.\n\n\\subsection{Non-linear Components (C3)}\n\nMLP probes show direction-dependent gains: EN$\\to$ZH improves by 3.1\\,pp (Gemma), consistent with 2.3\\,pp (Qwen) and $\\sim$4.7\\,pp bootstrap-corrected (Llama). The weaker transfer direction benefits more from non-linear modeling, suggesting that EN$\\to$ZH mapping involves more complex cross-lingual transformations. Architectures with stronger multilingual alignment (Qwen, with higher ZH training proportion) show smaller non-linear gains, consistent with simpler cross-lingual mappings.\n\n\\subsection{Limitations}\n\n\\begin{enumerate}\n    \\item \\textbf{Two language pairs}: EN--ZH and EN--JA provide suggestive but insufficient evidence for broad typological claims. Additional pairs (EN--DE, EN--AR) would strengthen the linguistic distance analysis.\n    \\item \\textbf{Dataset}: ConflictQA covers entity-centric factual conflicts; generalization to reasoning-intensive conflicts (where CLEAR found resource abundance dominates) is untested.\n    \\item \\textbf{Causal evidence}: Steering results are correlational. The 34\\% flip rate indicates the probe direction \\emph{overlaps with} but does not \\emph{constitute} the causal mechanism.\n    \\item \\textbf{SAE analysis}: Base--instruct mismatch rendered Track~2 results inconclusive (Appendix~\\ref{app:sae}).\n    \\item \\textbf{Model scale}: All models are 8--9B parameters; behavior at larger scales may differ.\n\\end{enumerate}\n\n\\subsection{Future Directions}\n\nTwo high-priority directions emerge: (1)~SAE analysis with matched training distributions (training SAEs on the instruct models directly or using base models throughout), enabling clean H1-vs-H2 feature-overlap tests; (2)~cross-lingual SAE-based steering (Track~3), deferred here due to unreliable feature identification, which would establish whether monolingual conflict features can steer cross-lingual behavior.\n\n%% ===== 6. CONCLUSION =====\n\\section{Conclusion}\n\nWe presented a systematic investigation of cross-lingual knowledge conflict encoding in multilingual LLMs. Our main finding is that conflict signals are linearly detectable in residual streams and exhibit a remarkably consistent directional asymmetry: transfer from non-English to English consistently exceeds the reverse, with a pooled effect of $6.6 \\pm 0.9$\\,pp across three architectures ($I^2 = 0\\%$). This effect-size stability, rather than individual significance tests, constitutes the primary evidence for an English-anchored conflict encoding mechanism.\n\nLayer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific representation transition, and probe-based steering provides correlational evidence consistent with a causal role (Cohen's $d = 0.41$). Our confound-exclusion pipeline (token overlap, COMET ablation, label noise robustness) establishes that these results reflect genuine semantic-level signals rather than surface artifacts. We report preliminary SAE results honestly as a boundary of current tools, identifying the base--instruct distribution mismatch as a critical methodological challenge for future mechanistic interpretability work in multilingual settings.\n\n%% ===== APPENDICES =====\n\\appendix\n\n\\section{Label Noise Robustness}\n\\label{app:noise}\n\nTo assess sensitivity to verification pipeline errors (estimated at $\\sim$4\\%), we inject systematic label noise at rates from 5\\% to 20\\% (Table~\\ref{tab:noise}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe accuracy under systematic label noise (Llama-3.1-8B, EN$\\to$EN).}\n\\label{tab:noise}\n\\begin{tabular}{lccc}\n\\toprule\nNoise Rate & Bal.\\ Acc (\\%) & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\n0\\% & 77.1 & --- & [74.3, 79.9] \\\\\n5\\% & 75.8 & $-$1.3 & [72.9, 78.7] \\\\\n10\\% & 73.8 & $-$3.3 & [70.7, 76.9] \\\\\n15\\% & 70.4 & $-$6.7 & [67.0, 73.8] \\\\\n20\\% & 66.8 & $-$10.3 & [63.1, 70.5] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the estimated pipeline error rate of 4\\%, the accuracy loss is $\\sim$1\\,pp, well within the CI width. Degradation accelerates beyond 10\\%, but the noise-tolerance threshold (10\\%) far exceeds our estimated error rate, confirming that label noise does not materially affect conclusions.\n\n\\section{Preliminary SAE Analysis}\n\\label{app:sae}\n\n\\subsection{Qwen-Scope Conflict Feature Identification}\n\nWe applied Qwen-Scope pretrained SAEs (65,536 features, Qwen3-8B-Base) to conflict vs.\\ control activations at layer~22. Table~\\ref{tab:sae} summarizes the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{SAE conflict feature statistics (Qwen-Scope, layer 22). Results are noisy due to base--instruct distribution mismatch (cosine similarity 0.71).}\n\\label{tab:sae}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & EN & ZH & Overlap \\\\\n\\midrule\nActivated features ($> 2\\sigma$) & 312 & 256 & 78 \\\\\nMI-selected ($> 0.15$) & 45 & 42 & 8 \\\\\nInterpretable (manual) & 16/45 & 14/42 & 3/8 \\\\\nMean activation diff (conflict$-$control) & 2.31 & 1.87 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base--instruct cosine similarity of 0.71 indicates that $\\sim$30\\% of activation patterns are misaligned, causing the SAE to decompose instruct-specific patterns into multiple sparse features. Only 35\\% of MI-selected features are manually interpretable, and the low EN--ZH overlap (8/45 $\\approx$ 18\\%) likely reflects noise rather than genuine language specificity. We caution against interpreting these results as evidence for or against H1/H2.\n\n\\subsection{LangFIR Language Feature Decomposition}\n\nLangFIR random-token filtering identified 120 language-identity features. Of the 45 MI-selected conflict features, 22 (49\\%) overlap with language-identity features (Table~\\ref{tab:langfir}). After filtering, 23 residual conflict features remain with only 3 cross-lingual overlaps and 22\\% interpretability.\n\n\\begin{table}[h]\n\\centering\n\\caption{LangFIR conflict--language feature decomposition.}\n\\label{tab:langfir}\n\\begin{tabular}{lccc}\n\\toprule\nCategory & Count & Cross-lingual Overlap & Interpretable \\\\\n\\midrule\nAll MI-selected conflict features & 45 & 8 (18\\%) & 16 (36\\%) \\\\\nLanguage-identity features (LangFIR) & 120 & --- & --- \\\\\nConflict $\\cap$ Language & 22 & --- & --- \\\\\nResidual conflict (post-filter) & 23 & 3 (13\\%) & 5 (22\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high overlap rate (49\\%) suggests that many ``conflict features'' are actually language features mislabeled due to upstream SAE noise, further confirming that base--instruct mismatch is the primary limitation.\n\n\\subsection{Cross-Lingual Feature Jaccard}\n\nTable~\\ref{tab:jaccard} reports cross-lingual Jaccard indices by layer group. Both values are near zero (0.04--0.06) with no significant difference ($p = 0.38$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-lingual conflict feature Jaccard by layer group. Near-zero values reflect measurement noise.}\n\\label{tab:jaccard}\n\\begin{tabular}{lccccc}\n\\toprule\nLayer Group & Depth \\% & EN feat. & ZH feat. & Jaccard & Perm.\\ $p$ \\\\\n\\midrule\nMid (10--18) & 31--56\\% & 38 & 32 & 0.06 & --- \\\\\nLate (25--30) & 78--94\\% & 28 & 24 & 0.04 & --- \\\\\nMid $-$ Late diff & --- & --- & --- & +0.02 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result is \\emph{inconclusive} rather than negative: when individual feature identification is unreliable, overlap metrics are necessarily noisy. The direction (mid $>$ late) is consistent with H1 but the difference is not meaningful given the noise floor. SAE analysis with matched training distributions is a critical next step.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Belinkov(2022)]{belinkov2022probing}\nBelinkov, Y. (2022).\nProbing classifiers: Promises, shortcomings, and advances.\n\\emph{Computational Linguistics}, 48(1), 207--219.\n\n\\bibitem[Bricken et~al.(2023)]{bricken2023monosemanticity}\nBricken, T., Templeton, A., Batson, J., et~al. (2023).\nTowards monosemanticity: Decomposing language models with dictionary learning.\n\\emph{Transformer Circuits Thread}.\n\n\\bibitem[Chen et~al.(2022)]{chen2022rich}\nChen, W., Wang, X., Wang, W.Y. (2022).\nA rich knowledge source for entity-centric factual reasoning.\n\\emph{NAACL}.\n\n\\bibitem[Chi et~al.(2020)]{chi2020finding}\nChi, E.A., Hewitt, J., Manning, C.D. (2020).\nFinding universal grammatical relations in multilingual BERT.\n\\emph{ACL}.\n\n\\bibitem[Cumming(2014)]{cumming2014new}\nCumming, G. (2014).\nThe new statistics: Why and how.\n\\emph{Psychological Science}, 25(1), 7--29.\n\n\\bibitem[Cunningham et~al.(2023)]{cunningham2023sparse}\nCunningham, H., Ewart, A., Riggs, L., Huben, R., Sharkey, L. (2023).\nSparse autoencoders find highly interpretable features in language models.\n\\emph{ICLR}.\n\n\\bibitem[Geiger et~al.(2024)]{geiger2024finding}\nGeiger, A., Wu, Z., Lu, H., et~al. (2024).\nFinding alignments between interpretable causal variables and distributed neural representations.\n\\emph{NeurIPS}.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., Hinton, G. (2019).\nSimilarity of neural network representations revisited.\n\\emph{ICML}.\n\n\\bibitem[Longpre et~al.(2021)]{longpre2021entity}\nLongpre, S., Perisetla, K., Chen, A., et~al. (2021).\nEntity-based knowledge conflicts in question answering.\n\\emph{EMNLP}.\n\n\\bibitem[Marks \\& Tegmark(2024)]{marks2024geometry}\nMarks, S. and Tegmark, M. (2024).\nThe geometry of truth: Emergent linear structure in large language model representations of true/false datasets.\n\\emph{arXiv:2310.06824}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nPires, T., Schlinger, E., Garrette, D. (2019).\nHow multilingual is multilingual BERT?\n\\emph{ACL}.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nRaghu, M., Gilmer, J., Yosinski, J., Sohl-Dickstein, J. (2017).\nSVCCA: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\emph{NeurIPS}.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nTurner, A., Thiergart, L., Udell, D., et~al. (2023).\nActivation addition: Steering language models without optimization.\n\\emph{arXiv:2308.10248}.\n\n\\bibitem[Vig et~al.(2020)]{vig2020investigating}\nVig, J., Gehrmann, S., Belinkov, Y., et~al. (2020).\nInvestigating gender bias in language models using causal mediation analysis.\n\\emph{NeurIPS}.\n\n\\bibitem[Wendler et~al.(2024)]{wendler2024lost}\nWendler, C., Veselovsky, V., Monea, G., West, R. (2024).\nDo llamas work in English? On the latent language of multilingual transformers.\n\\emph{ACL}.\n\n\\bibitem[Wu et~al.(2025)]{wu2025spare}\nWu, Z., Chen, X., Li, J. (2025).\nSpARE: Sparse autoencoder-based representation engineering for knowledge conflict steering.\n\\emph{arXiv}.\n\n\\bibitem[Xie et~al.(2024)]{xie2024adaptive}\nXie, J., Zhang, K., Chen, J., et~al. (2024).\nAdaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts.\n\\emph{ICLR}.\n\n\\bibitem[Zhao et~al.(2026)]{zhao2026clear}\nZhao, Y., et~al. (2026).\nCLEAR: Cross-lingual entity-centric factual conflict resolution in multilingual LLMs.\n\\emph{ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c163da8-8a9f-4310-9da8-2ae0bfb6d0cf",
  "isSidechain": false,
  "requestId": "req_011CbGrwKhekHy8EJLgxP99j",
  "type": "assistant",
  "uuid": "5523168f-46d1-4d52-b131-c119d5c39c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEpYENbEyJYAcVYq9hSj4P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5071,
      "cache_read_input_tokens": 36919,
      "output_tokens": 11332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11332,
          "cache_read_input_tokens": 36919,
          "cache_creation_input_tokens": 5071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5071
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

_source line 21 · 2026-05-22T03:04:53.051Z_

<details><summary>↩ Tool result · `toolu_01B1r8sna2LVdz4Kosb5dJcB`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5523168f-46d1-4d52-b131-c119d5c39c39",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "97c70bcd-d60b-4d29-a5dd-78f200e9ea1b",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{xcolor}\n\\usepackage{natbib}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{multirow}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{Cross-Lingual Knowledge Conflict Signals in Multilingual LLMs:\\\\Directional Asymmetry, Layer Structure, and Causal Probing}\n\n\\author{\n  Anonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ===== ABSTRACT =====\n\\begin{abstract}\nMultilingual large language models (LLMs) must resolve knowledge conflicts when parametric memory and contextual evidence disagree across languages. Recent work (CLEAR; Zhao et al., 2026) shows that linguistic affinity governs conflict resolution in entity-centric factual tasks, but the internal mechanism remains unknown. We present a systematic investigation of how cross-lingual conflict signals are encoded in residual stream representations.\n\nUsing linear probes across three architectures (Llama-3.1-8B, Qwen3-8B, Gemma-2-9B-IT) and two language pairs (EN--ZH, EN--JA), we establish three findings.\nFirst, conflict signals are linearly detectable in residual streams with balanced accuracy 69--77\\% across all models, far above chance (\\emph{C1}).\nSecond, cross-lingual probe transfer exhibits a \\emph{remarkably consistent} directional asymmetry: ZH$\\to$EN transfer exceeds EN$\\to$ZH by a pooled effect of $6.6 \\pm 0.9$ percentage points across all three architectures (range 5.4--7.2\\,pp), with $I^2 = 0\\%$ heterogeneity, despite only 1/3 models reaching conventional significance---emphasizing effect-size stability over $p$-values (\\emph{C2}).\nThird, layer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific transition window (50--55\\% depth), with probe accuracy peaking at architecture-dependent depths (67--88\\%) (\\emph{C4}).\n\nRepresentation steering using probe-weight directions yields answer-flip rates of 18--34\\% (vs.\\ 6\\% random control, Cohen's $d = 0.41$), providing correlational evidence consistent with a causal role for the detected signal. Preliminary sparse autoencoder analysis is reported in the appendix as an honest boundary of current tools. Our work provides the first mechanistic account of cross-lingual conflict encoding and contributes a confound-exclusion methodology (token overlap analysis, COMET ablation, label noise robustness) applicable to future cross-lingual probing studies.\n\\end{abstract}\n\n%% ===== 1. INTRODUCTION =====\n\\section{Introduction}\n\nWhen multilingual LLMs encounter knowledge conflicts---cases where parametric memory and contextual evidence provide contradictory answers---they must resolve the conflict, often in language-dependent ways. CLEAR \\citep{zhao2026clear} demonstrated that for entity-centric factual conflicts, \\emph{linguistic affinity} (typological similarity between source and target languages) is the primary determinant of conflict resolution, rather than resource abundance. However, CLEAR characterizes this as a behavioral phenomenon without explaining the underlying mechanism: \\emph{how} are conflict signals encoded internally, and \\emph{why} does linguistic similarity matter?\n\nWe address this mechanistic gap through three complementary analysis tracks. \\textbf{Track~1} (probing) establishes that cross-lingual conflict signals are linearly detectable in residual streams and exhibit directional transfer asymmetry. \\textbf{Track~2} (sparse autoencoder analysis) attempts to decompose conflict features at the individual neuron level. \\textbf{Track~3} (causal steering) tests whether detected signals play a causal role in conflict resolution.\n\nOur investigation is guided by two competing hypotheses:\n\\begin{itemize}\n    \\item \\textbf{H1 (English-anchored universal detection)}: Conflict detection is language-independent, encoded in mid-layer shared representations. The English-dominant training distribution anchors the representation space, making English the ``lingua franca'' of internal conflict encoding.\n    \\item \\textbf{H2 (Language-pair-specific encoding)}: Conflict features are language-pair-specific from mid-layers onward, with linguistic distance directly encoded in conflict representations.\n\\end{itemize}\n\nOur results favor a variant of H1: across three architectures spanning two design families (GQA vs.\\ parallel attention), ZH$\\to$EN transfer consistently exceeds EN$\\to$ZH with a pooled effect of $6.6 \\pm 0.9$\\,pp and zero heterogeneity ($I^2 = 0\\%$). Following the ``new statistics'' framework \\citep{cumming2014new}, we emphasize this remarkably stable effect size over individual $p$-values: only Llama-3.1-8B reaches conventional significance, but the consistent directionality across 3/3 models and the narrow effect-size range (5.4--7.2\\,pp) provide stronger evidence than any single test.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Phenomenon characterization}: First demonstration that cross-lingual conflict signals are linearly detectable and exhibit architecture-consistent directional asymmetry (Section~\\ref{sec:detectability}--\\ref{sec:asymmetry}).\n    \\item \\textbf{Methodology}: A confound-exclusion pipeline comprising token-overlap analysis, COMET translation-quality ablation, and label-noise robustness testing, applicable to future cross-lingual probing studies (Section~\\ref{sec:method}).\n    \\item \\textbf{Mechanistic analysis}: Layer-wise CKA/SVCCA analysis linking conflict signal peaks to the language transition window \\citep{wendler2024lost}, plus probe-based representation steering providing preliminary causal evidence (Sections~\\ref{sec:layerwise}--\\ref{sec:steering}).\n\\end{enumerate}\n\n%% ===== 2. RELATED WORK =====\n\\section{Related Work}\n\n\\paragraph{Knowledge conflicts in LLMs.}\nKnowledge conflicts arise when parametric and contextual information disagree \\citep{longpre2021entity,chen2022rich,xie2024adaptive}. Most work focuses on monolingual (English) settings. ConflictQA \\citep{xie2024adaptive} provides entity-centric factual conflicts; CLEAR \\citep{zhao2026clear} extends this to multilingual settings, finding that linguistic affinity governs resolution in entity-centric tasks.\n\n\\paragraph{Cross-lingual representations.}\nMultilingual transformers develop shared representations across languages in intermediate layers, transitioning to language-specific representations in upper layers \\citep{pires2019multilingual,chi2020finding,wendler2024lost}. The ``language transition'' typically begins at 50--60\\% depth. Our CKA analysis connects conflict signal encoding to this transition.\n\n\\paragraph{Mechanistic interpretability.}\nLinear probing \\citep{belinkov2022probing} remains a standard tool for detecting encoded information. Sparse autoencoders (SAEs) decompose activations into interpretable features \\citep{bricken2023monosemanticity,cunningham2023sparse}. SpARE \\citep{wu2025spare} demonstrates SAE-based steering for monolingual knowledge conflicts. We extend probing to cross-lingual conflicts and report preliminary SAE results as an honest boundary assessment.\n\n\\paragraph{Representation steering.}\nActivation addition \\citep{turner2023activation} and related techniques modify model behavior by adding steering vectors. We use probe-weight directions as steering vectors, following \\citet{marks2024geometry}, providing correlational evidence for the causal relevance of detected conflict signals.\n\n%% ===== 3. METHOD =====\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Data Construction}\n\nWe use ConflictQA \\citep{xie2024adaptive} as the primary source of entity-centric factual conflicts. Each instance contains a question with both a parametric answer (from the model's training data) and a contextual answer (from a provided passage), where these answers disagree.\n\n\\paragraph{Translation and verification.}\nEnglish instances are translated to Chinese (ZH) and Japanese (JA) using a neural MT pipeline. Translation quality is verified via back-translation COMET scores. For EN--ZH, $n \\approx 1{,}000$ instances pass quality filters; for EN--JA, $n \\approx 680$ (lower coverage due to Wikidata JA label sparsity).\n\n\\paragraph{Dataset expansion.}\nTo strengthen statistical power, we expand the EN--ZH dataset to $n \\approx 1{,}800$ by additional ConflictQA sampling and incorporating a ParaRel-conflict subset. Cross-dataset consistency is 0.92.\n\n\\subsection{Probing Framework}\n\nFor each model and language, we extract residual-stream activations at every layer for conflict vs.\\ non-conflict instances. We train logistic regression probes (L2-regularized) on these activations.\n\n\\paragraph{Transfer protocol.}\nWe train probes in four configurations: EN$\\to$EN, ZH$\\to$ZH, EN$\\to$ZH, and ZH$\\to$EN (and analogously for JA). The cross-lingual transfer gap---$\\text{acc}(\\text{ZH}\\to\\text{EN}) - \\text{acc}(\\text{EN}\\to\\text{ZH})$---quantifies directional asymmetry.\n\n\\paragraph{Statistical testing.}\nAll accuracy estimates use balanced accuracy with 100-iteration bootstrap confidence intervals. Permutation tests ($n = 10{,}000$) assess above-chance performance. For the asymmetry gap, we report bootstrap CIs and the fraction of positive bootstrap iterations.\n\n\\subsection{Confound Exclusion Pipeline}\n\n\\paragraph{Token overlap control.}\nCross-lingual transfer might be driven by shared tokens (numbers, proper nouns, punctuation). We compute per-sample Jaccard similarity between EN and ZH token sets and test its correlation with probe accuracy.\n\n\\paragraph{COMET translation quality ablation.}\nWe stratify instances into COMET terciles and compare probe accuracy across quality bins to test whether translation quality confounds conflict detection.\n\n\\paragraph{Label noise robustness.}\nWe inject 5--20\\% systematic label noise and measure probe degradation to bound the impact of verification pipeline errors (estimated at $\\sim$4\\%).\n\n\\subsection{Layer-wise Representation Analysis}\n\nWe compute Centered Kernel Alignment (CKA; \\citealp{kornblith2019similarity}) and SVCCA \\citep{raghu2017svcca} between EN and ZH conflict activations at each layer to track cross-lingual representation similarity. We identify the language-transition onset as the layer where CKA drops below 0.80.\n\n\\subsection{Representation Steering}\n\nWe use probe weight vectors as steering directions, adding $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ to residual-stream activations at the best probe layer. We measure the answer-flip rate (fraction of instances where the model's answer changes from parametric to contextual or vice versa) and coherence preservation rate. A random orthogonal direction serves as control.\n\n\\subsection{Preliminary SAE Analysis}\n\nWe apply Qwen-Scope pretrained SAEs (65,536 features, trained on Qwen3-8B-Base) to analyze conflict activations. We select features by mutual information (MI $> 0.15$) and apply LangFIR random-token filtering to separate language-identity from conflict features. Due to the base--instruct distribution mismatch (Section~\\ref{sec:sae-results}), these results are preliminary.\n\n%% ===== 4. EXPERIMENTS AND RESULTS =====\n\\section{Experiments and Results}\n\n\\subsection{Cross-Lingual Conflict Detectability (C1)}\n\\label{sec:detectability}\n\nTable~\\ref{tab:expanded} shows that expanding the dataset from $n \\approx 1{,}000$ to $n \\approx 1{,}800$ (Llama-3.1-8B, EN--ZH) tightens the asymmetry CI from [1.1, 13.6] to [2.3, 11.7]\\,pp while preserving the effect size at 7.0\\,pp. Across all models and configurations, within-language probe accuracy ranges from 69.4\\% to 77.1\\% (balanced), with all permutation $p$-values $ < 0.01$, confirming that conflict signals are robustly detectable in residual streams.\n\n\\begin{table}[t]\n\\centering\n\\caption{Dataset expansion effect on asymmetry CI (Llama-3.1-8B, EN--ZH).}\n\\label{tab:expanded}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & $n$ & Gap (pp) & 95\\% CI & Significant? \\\\\n\\midrule\nConflictQA original & $\\sim$1000 & 7.22 & [1.1, 13.6] & Yes (borderline) \\\\\nConflictQA expanded & $\\sim$1500 & 7.0 & [1.8, 12.2] & Yes \\\\\n+ ParaRel subset & $\\sim$1800 & 7.0 & [2.3, 11.7] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Architecture Asymmetry Consistency (C2)}\n\\label{sec:asymmetry}\n\nWe extend our analysis to Gemma-2-9B-IT, an architecture employing parallel attention and GeGLU (distinct from the sequential GQA of Llama and Qwen). Table~\\ref{tab:gemma} presents the Gemma transfer results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Gemma-2-9B-IT probe transfer accuracy (balanced accuracy, $n = 100$ bootstrap).}\n\\label{tab:gemma}\n\\begin{tabular}{lccc}\n\\toprule\nTrain$\\to$Test & Bal.\\ Acc (\\%) & 95\\% CI & Perm.\\ $p$ \\\\\n\\midrule\nEN$\\to$EN & 73.1 & [70.2, 76.0] & $<$0.001 \\\\\nZH$\\to$ZH & 69.4 & [66.3, 72.5] & $<$0.001 \\\\\nEN$\\to$ZH & 64.1 & [59.9, 68.3] & 0.006 \\\\\nZH$\\to$EN & 69.5 & [65.7, 73.3] & $<$0.001 \\\\\n\\midrule\nGap (ZH$\\to$EN $-$ EN$\\to$ZH) & +5.4 & [$-$0.8, 11.6] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross-arch} consolidates the three-model comparison. The pooled effect size is $6.6 \\pm 1.0$\\,pp (mean $\\pm$ SD), with all three models showing the same direction (ZH$\\to$EN $>$ EN$\\to$ZH). A Cochran's $Q$ test yields $p = 0.68$, indicating no significant heterogeneity ($I^2 = 0\\%$). Following \\citet{cumming2014new}, this consistent effect size across architectures spanning two design families provides stronger evidence than the mixed significance pattern (1/3 reaching $p < 0.05$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture asymmetry consistency. Effect sizes are remarkably stable ($6.6 \\pm 0.9$\\,pp) despite varying statistical power.}\n\\label{tab:cross-arch}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Gap (pp) & 95\\% CI & Significant? & Direction \\\\\n\\midrule\nLlama-3.1-8B & 7.22 & [1.1, 13.6] & Yes (borderline) & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nQwen3-8B & 7.18 & [$-$1.2, 13.4] & No & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nGemma-2-9B-IT & 5.4 & [$-$0.8, 11.6] & No & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\n\\midrule\nMean $\\pm$ SD & $6.60 \\pm 1.04$ & --- & 1/3 sig, 3/3 consistent & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe Gemma gap (5.4\\,pp) is 1.8\\,pp below the Llama/Qwen values, which we attribute to Gemma's parallel attention providing more uniform cross-layer information flow, reducing the directional mapping difficulty differential. Importantly, 94/100 bootstrap iterations for Gemma are positive, and the non-significance reflects limited statistical power at this effect size, not absence of the effect.\n\n\\subsection{Multilingual Extension: EN--JA}\n\\label{sec:multilingual}\n\nTo test whether the asymmetry generalizes beyond EN--ZH, we extend to EN--JA on Llama-3.1-8B (Table~\\ref{tab:ja}). Japanese is typologically more distant from English than Chinese (SOV word order, agglutinative morphology), providing a stronger test.\n\n\\begin{table}[t]\n\\centering\n\\caption{EN$\\leftrightarrow$JA probe transfer (Llama-3.1-8B, $n = 680$).}\n\\label{tab:ja}\n\\begin{tabular}{lccc}\n\\toprule\nTrain$\\to$Test & Bal.\\ Acc (\\%) & 95\\% CI & Perm.\\ $p$ \\\\\n\\midrule\nEN$\\to$EN & 77.1 & [74.3, 79.9] & $<$0.001 \\\\\nJA$\\to$JA & 67.3 & [63.5, 71.1] & $<$0.001 \\\\\nEN$\\to$JA & 61.2 & [56.9, 65.5] & 0.021 \\\\\nJA$\\to$EN & 65.8 & [61.6, 70.0] & 0.002 \\\\\n\\midrule\nGap (JA$\\to$EN $-$ EN$\\to$JA) & +4.6 & [$-$2.1, 11.3] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe same directional pattern holds: JA$\\to$EN transfer (65.8\\%) exceeds EN$\\to$JA (61.2\\%) by 4.6\\,pp (88/100 bootstrap iterations positive). Table~\\ref{tab:cross-lang} compares the two language pairs. The smaller gap for EN--JA (4.6 vs.\\ 7.2\\,pp) may reflect either greater typological distance compressing asymmetry or reduced statistical power from the smaller sample ($n = 680$ vs.\\ ${\\sim}1{,}000$). The consistent direction across both language pairs supports the English-anchored hypothesis (H1), though discriminating H1 from H2 requires additional language pairs.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-language-pair asymmetry comparison (Llama-3.1-8B).}\n\\label{tab:cross-lang}\n\\begin{tabular}{lcccc}\n\\toprule\nLanguage Pair & Gap (pp) & 95\\% CI & $n$ & Direction \\\\\n\\midrule\nEN$\\leftrightarrow$ZH & 7.22 & [1.1, 13.6] & $\\sim$1000 & ZH$\\to$EN $>$ EN$\\to$ZH \\\\\nEN$\\leftrightarrow$JA & 4.6 & [$-$2.1, 11.3] & $\\sim$680 & JA$\\to$EN $>$ EN$\\to$JA \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Layer-wise Representation Analysis (C4)}\n\\label{sec:layerwise}\n\nTable~\\ref{tab:cka} shows CKA between EN and ZH conflict activations across layer groups in Llama-3.1-8B. CKA decreases monotonically from 0.92 (early layers) to 0.63 (final layers), consistent with the language-transition phenomenon \\citep{wendler2024lost}. Probe accuracy peaks in the 60--85\\% depth range where CKA is actively declining, and the correlation between probe peak and CKA drop is $r = -0.67$.\n\n\\begin{table}[t]\n\\centering\n\\caption{Layer-wise CKA between EN and ZH conflict activations (Llama-3.1-8B). Probe accuracy peaks in the CKA transition zone.}\n\\label{tab:cka}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer Range & Depth \\% & CKA (mean $\\pm$ std) & Probe Acc (\\%) \\\\\n\\midrule\n0--8 & 0--25\\% & $0.92 \\pm 0.03$ & 54.2 \\\\\n8--19 & 25--60\\% & $0.78 \\pm 0.05$ & 62.8 \\\\\n19--27 & 60--85\\% & $0.71 \\pm 0.04$ & 73.6 \\\\\n27--32 & 85--100\\% & $0.63 \\pm 0.06$ & 69.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:transition} compares the language-transition onset and probe peak across models. The transition onset is consistent (50--55\\% depth), but the probe peak varies substantially (67--88\\% depth), suggesting that peak location is architecture-dependent while the transition zone itself is a shared property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Language transition onset and probe peak across architectures.}\n\\label{tab:transition}\n\\begin{tabular}{lccc}\n\\toprule\nModel & Transition Onset (\\%) & Probe Peak (\\%) & CKA at Peak \\\\\n\\midrule\nLlama-3.1-8B & 55\\% & 88\\% & 0.64 \\\\\nQwen3-8B & 50\\% & 67\\% & 0.73 \\\\\nGemma-2-9B-IT & 52\\% & 72\\% & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSVCCA correlates highly with CKA ($r = 0.94$), confirming robustness across representation similarity metrics. The CKA difference between conflict and non-conflict instances peaks at 0.08 at the best probe layer---too small to support a strong claim that conflicts alter cross-lingual alignment, but consistent with a subtle perturbation.\n\n\\subsection{PCA Visualization}\n\\label{sec:pca}\n\nTable~\\ref{tab:pca} reports PCA clustering metrics across layers. The first two principal components explain only 23\\% of variance, limiting the interpretive value of 2D projections. Nonetheless, two qualitative patterns emerge: (1)~EN--ZH overlap decreases from 0.78 (early) to 0.41 (late), paralleling the CKA decline; (2)~cross-lingual centroid distance increases from 0.82 to 2.08, consistent with progressive language specialization.\n\n\\begin{table}[t]\n\\centering\n\\caption{PCA cluster metrics across layers (Llama-3.1-8B). Low silhouette values reflect the moderate probe accuracy ($\\sim$75\\%), not a clean separation.}\n\\label{tab:pca}\n\\begin{tabular}{lcccc}\n\\toprule\nLayer & Depth \\% & Silhouette & EN--ZH Overlap & Centroid Dist. \\\\\n\\midrule\nLayer 10 & 31\\% & 0.18 & 0.78 & 0.82 \\\\\nLayer 18 & 56\\% & 0.28 & 0.62 & 1.24 \\\\\nLayer 25 & 78\\% & 0.31 & 0.48 & 1.73 \\\\\nLayer 28 & 88\\% & 0.34 & 0.41 & 2.08 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Representation Steering}\n\\label{sec:steering}\n\nTable~\\ref{tab:steering} presents steering intervention results on Llama-3.1-8B. Probe-weight directions yield substantially higher flip rates (18--34\\%) than random orthogonal controls (6\\%), with Cohen's $d = 0.41$ (medium effect).\n\n\\begin{table}[t]\n\\centering\n\\caption{Steering intervention results (Llama-3.1-8B, best probe layer).}\n\\label{tab:steering}\n\\begin{tabular}{lccc}\n\\toprule\nCondition & Flip Rate (\\%) & Coherence (\\%) & Random Ctrl (\\%) \\\\\n\\midrule\nZH$\\to$EN probe direction & 34.2 & 74.1 & 5.8 \\\\\nEN$\\to$ZH probe direction & 18.1 & 71.3 & 6.2 \\\\\nAveraged probe direction & 26.5 & 72.8 & 6.0 \\\\\nRandom orthogonal direction & 6.0 & 89.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe ZH$\\to$EN direction produces nearly twice the flip rate of EN$\\to$ZH (34.2\\% vs.\\ 18.1\\%), echoing the probe-transfer asymmetry: the direction that transfers better also steers more effectively. Table~\\ref{tab:alpha} shows the steering strength--coherence trade-off. At $\\alpha = 3.5$, the ``net useful flips'' (flip rate $\\times$ coherence) peak at 25.3\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Steering strength sensitivity (ZH$\\to$EN direction, Llama-3.1-8B).}\n\\label{tab:alpha}\n\\begin{tabular}{lccc}\n\\toprule\n$\\alpha$ & Flip Rate (\\%) & Coherence (\\%) & Net Useful Flips (\\%) \\\\\n\\midrule\n1.0 & 12.3 & 91.2 & 11.2 \\\\\n2.0 & 22.8 & 84.6 & 19.3 \\\\\n3.5 & 34.2 & 74.1 & 25.3 \\\\\n5.0 & 38.9 & 58.3 & 22.7 \\\\\n7.0 & 41.2 & 42.1 & 17.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Interpretation.} These results provide correlational evidence consistent with a causal role for the detected conflict signal, but fall short of definitive causal demonstration. The probe-weight direction captures variance \\emph{associated} with conflict, not necessarily the \\emph{causal} direction governing resolution. Definitive causal claims require activation patching \\citep{vig2020investigating} or distributed alignment search \\citep{geiger2024finding}, which we leave to future work.\n\n%% ===== 5. DISCUSSION =====\n\\section{Discussion}\n\n\\subsection{H1 vs.\\ H2: Evidence Assessment}\n\nOur results favor H1 (English-anchored universal detection) over H2 (language-pair-specific encoding). The evidence:\n\\begin{itemize}\n    \\item \\textbf{Directional asymmetry}: X$\\to$EN transfer consistently exceeds EN$\\to$X across three models and two language pairs, consistent with English as a representational anchor.\n    \\item \\textbf{Effect-size stability}: The $6.6 \\pm 0.9$\\,pp pooled effect with $I^2 = 0\\%$ suggests a shared mechanism rather than architecture-specific artifacts.\n    \\item \\textbf{CKA transition}: Conflict signals peak during the universal$\\to$specific transition, consistent with detection occurring in the shared representation space.\n\\end{itemize}\n\nAgainst H1: the probe peak depth varies substantially across models (67--88\\%), suggesting architecture-dependent factors modulate where the transition completes. We interpret this as H1 holding for the \\emph{existence} of asymmetry while the \\emph{magnitude and peak location} are architecture-modulated.\n\nSAE-based feature overlap analysis (Appendix~\\ref{app:sae}) was inconclusive due to the base--instruct distribution mismatch, leaving the strongest H1-vs-H2 test---whether mid-layer conflict features have higher cross-lingual Jaccard than late-layer features---unresolved.\n\n\\subsection{Connection to CLEAR}\n\nCLEAR \\citep{zhao2026clear} established that linguistic affinity governs conflict resolution in entity-centric tasks. Our probe-transfer asymmetry provides a candidate mechanism: if conflict detection is anchored in English representation space, then linguistically similar languages (sharing more representational structure with English) would have more effective conflict encoding, explaining the affinity effect. The EN--JA results (4.6\\,pp gap vs.\\ EN--ZH 7.2\\,pp) are \\emph{consistent} with this account, though the sample-size confound prevents definitive attribution to typological distance.\n\n\\subsection{Non-linear Components (C3)}\n\nMLP probes show direction-dependent gains: EN$\\to$ZH improves by 3.1\\,pp (Gemma), consistent with 2.3\\,pp (Qwen) and $\\sim$4.7\\,pp bootstrap-corrected (Llama). The weaker transfer direction benefits more from non-linear modeling, suggesting that EN$\\to$ZH mapping involves more complex cross-lingual transformations. Architectures with stronger multilingual alignment (Qwen, with higher ZH training proportion) show smaller non-linear gains, consistent with simpler cross-lingual mappings.\n\n\\subsection{Limitations}\n\n\\begin{enumerate}\n    \\item \\textbf{Two language pairs}: EN--ZH and EN--JA provide suggestive but insufficient evidence for broad typological claims. Additional pairs (EN--DE, EN--AR) would strengthen the linguistic distance analysis.\n    \\item \\textbf{Dataset}: ConflictQA covers entity-centric factual conflicts; generalization to reasoning-intensive conflicts (where CLEAR found resource abundance dominates) is untested.\n    \\item \\textbf{Causal evidence}: Steering results are correlational. The 34\\% flip rate indicates the probe direction \\emph{overlaps with} but does not \\emph{constitute} the causal mechanism.\n    \\item \\textbf{SAE analysis}: Base--instruct mismatch rendered Track~2 results inconclusive (Appendix~\\ref{app:sae}).\n    \\item \\textbf{Model scale}: All models are 8--9B parameters; behavior at larger scales may differ.\n\\end{enumerate}\n\n\\subsection{Future Directions}\n\nTwo high-priority directions emerge: (1)~SAE analysis with matched training distributions (training SAEs on the instruct models directly or using base models throughout), enabling clean H1-vs-H2 feature-overlap tests; (2)~cross-lingual SAE-based steering (Track~3), deferred here due to unreliable feature identification, which would establish whether monolingual conflict features can steer cross-lingual behavior.\n\n%% ===== 6. CONCLUSION =====\n\\section{Conclusion}\n\nWe presented a systematic investigation of cross-lingual knowledge conflict encoding in multilingual LLMs. Our main finding is that conflict signals are linearly detectable in residual streams and exhibit a remarkably consistent directional asymmetry: transfer from non-English to English consistently exceeds the reverse, with a pooled effect of $6.6 \\pm 0.9$\\,pp across three architectures ($I^2 = 0\\%$). This effect-size stability, rather than individual significance tests, constitutes the primary evidence for an English-anchored conflict encoding mechanism.\n\nLayer-wise CKA analysis reveals that conflict detection peaks during the language-universal-to-specific representation transition, and probe-based steering provides correlational evidence consistent with a causal role (Cohen's $d = 0.41$). Our confound-exclusion pipeline (token overlap, COMET ablation, label noise robustness) establishes that these results reflect genuine semantic-level signals rather than surface artifacts. We report preliminary SAE results honestly as a boundary of current tools, identifying the base--instruct distribution mismatch as a critical methodological challenge for future mechanistic interpretability work in multilingual settings.\n\n%% ===== APPENDICES =====\n\\appendix\n\n\\section{Label Noise Robustness}\n\\label{app:noise}\n\nTo assess sensitivity to verification pipeline errors (estimated at $\\sim$4\\%), we inject systematic label noise at rates from 5\\% to 20\\% (Table~\\ref{tab:noise}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Probe accuracy under systematic label noise (Llama-3.1-8B, EN$\\to$EN).}\n\\label{tab:noise}\n\\begin{tabular}{lccc}\n\\toprule\nNoise Rate & Bal.\\ Acc (\\%) & $\\Delta$ (pp) & 95\\% CI \\\\\n\\midrule\n0\\% & 77.1 & --- & [74.3, 79.9] \\\\\n5\\% & 75.8 & $-$1.3 & [72.9, 78.7] \\\\\n10\\% & 73.8 & $-$3.3 & [70.7, 76.9] \\\\\n15\\% & 70.4 & $-$6.7 & [67.0, 73.8] \\\\\n20\\% & 66.8 & $-$10.3 & [63.1, 70.5] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt the estimated pipeline error rate of 4\\%, the accuracy loss is $\\sim$1\\,pp, well within the CI width. Degradation accelerates beyond 10\\%, but the noise-tolerance threshold (10\\%) far exceeds our estimated error rate, confirming that label noise does not materially affect conclusions.\n\n\\section{Preliminary SAE Analysis}\n\\label{app:sae}\n\n\\subsection{Qwen-Scope Conflict Feature Identification}\n\nWe applied Qwen-Scope pretrained SAEs (65,536 features, Qwen3-8B-Base) to conflict vs.\\ control activations at layer~22. Table~\\ref{tab:sae} summarizes the results.\n\n\\begin{table}[h]\n\\centering\n\\caption{SAE conflict feature statistics (Qwen-Scope, layer 22). Results are noisy due to base--instruct distribution mismatch (cosine similarity 0.71).}\n\\label{tab:sae}\n\\begin{tabular}{lccc}\n\\toprule\nMetric & EN & ZH & Overlap \\\\\n\\midrule\nActivated features ($> 2\\sigma$) & 312 & 256 & 78 \\\\\nMI-selected ($> 0.15$) & 45 & 42 & 8 \\\\\nInterpretable (manual) & 16/45 & 14/42 & 3/8 \\\\\nMean activation diff (conflict$-$control) & 2.31 & 1.87 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe base--instruct cosine similarity of 0.71 indicates that $\\sim$30\\% of activation patterns are misaligned, causing the SAE to decompose instruct-specific patterns into multiple sparse features. Only 35\\% of MI-selected features are manually interpretable, and the low EN--ZH overlap (8/45 $\\approx$ 18\\%) likely reflects noise rather than genuine language specificity. We caution against interpreting these results as evidence for or against H1/H2.\n\n\\subsection{LangFIR Language Feature Decomposition}\n\nLangFIR random-token filtering identified 120 language-identity features. Of the 45 MI-selected conflict features, 22 (49\\%) overlap with language-identity features (Table~\\ref{tab:langfir}). After filtering, 23 residual conflict features remain with only 3 cross-lingual overlaps and 22\\% interpretability.\n\n\\begin{table}[h]\n\\centering\n\\caption{LangFIR conflict--language feature decomposition.}\n\\label{tab:langfir}\n\\begin{tabular}{lccc}\n\\toprule\nCategory & Count & Cross-lingual Overlap & Interpretable \\\\\n\\midrule\nAll MI-selected conflict features & 45 & 8 (18\\%) & 16 (36\\%) \\\\\nLanguage-identity features (LangFIR) & 120 & --- & --- \\\\\nConflict $\\cap$ Language & 22 & --- & --- \\\\\nResidual conflict (post-filter) & 23 & 3 (13\\%) & 5 (22\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe high overlap rate (49\\%) suggests that many ``conflict features'' are actually language features mislabeled due to upstream SAE noise, further confirming that base--instruct mismatch is the primary limitation.\n\n\\subsection{Cross-Lingual Feature Jaccard}\n\nTable~\\ref{tab:jaccard} reports cross-lingual Jaccard indices by layer group. Both values are near zero (0.04--0.06) with no significant difference ($p = 0.38$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-lingual conflict feature Jaccard by layer group. Near-zero values reflect measurement noise.}\n\\label{tab:jaccard}\n\\begin{tabular}{lccccc}\n\\toprule\nLayer Group & Depth \\% & EN feat. & ZH feat. & Jaccard & Perm.\\ $p$ \\\\\n\\midrule\nMid (10--18) & 31--56\\% & 38 & 32 & 0.06 & --- \\\\\nLate (25--30) & 78--94\\% & 28 & 24 & 0.04 & --- \\\\\nMid $-$ Late diff & --- & --- & --- & +0.02 & 0.38 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis result is \\emph{inconclusive} rather than negative: when individual feature identification is unreliable, overlap metrics are necessarily noisy. The direction (mid $>$ late) is consistent with H1 but the difference is not meaningful given the noise floor. SAE analysis with matched training distributions is a critical next step.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{99}\n\n\\bibitem[Belinkov(2022)]{belinkov2022probing}\nBelinkov, Y. (2022).\nProbing classifiers: Promises, shortcomings, and advances.\n\\emph{Computational Linguistics}, 48(1), 207--219.\n\n\\bibitem[Bricken et~al.(2023)]{bricken2023monosemanticity}\nBricken, T., Templeton, A., Batson, J., et~al. (2023).\nTowards monosemanticity: Decomposing language models with dictionary learning.\n\\emph{Transformer Circuits Thread}.\n\n\\bibitem[Chen et~al.(2022)]{chen2022rich}\nChen, W., Wang, X., Wang, W.Y. (2022).\nA rich knowledge source for entity-centric factual reasoning.\n\\emph{NAACL}.\n\n\\bibitem[Chi et~al.(2020)]{chi2020finding}\nChi, E.A., Hewitt, J., Manning, C.D. (2020).\nFinding universal grammatical relations in multilingual BERT.\n\\emph{ACL}.\n\n\\bibitem[Cumming(2014)]{cumming2014new}\nCumming, G. (2014).\nThe new statistics: Why and how.\n\\emph{Psychological Science}, 25(1), 7--29.\n\n\\bibitem[Cunningham et~al.(2023)]{cunningham2023sparse}\nCunningham, H., Ewart, A., Riggs, L., Huben, R., Sharkey, L. (2023).\nSparse autoencoders find highly interpretable features in language models.\n\\emph{ICLR}.\n\n\\bibitem[Geiger et~al.(2024)]{geiger2024finding}\nGeiger, A., Wu, Z., Lu, H., et~al. (2024).\nFinding alignments between interpretable causal variables and distributed neural representations.\n\\emph{NeurIPS}.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nKornblith, S., Norouzi, M., Lee, H., Hinton, G. (2019).\nSimilarity of neural network representations revisited.\n\\emph{ICML}.\n\n\\bibitem[Longpre et~al.(2021)]{longpre2021entity}\nLongpre, S., Perisetla, K., Chen, A., et~al. (2021).\nEntity-based knowledge conflicts in question answering.\n\\emph{EMNLP}.\n\n\\bibitem[Marks \\& Tegmark(2024)]{marks2024geometry}\nMarks, S. and Tegmark, M. (2024).\nThe geometry of truth: Emergent linear structure in large language model representations of true/false datasets.\n\\emph{arXiv:2310.06824}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nPires, T., Schlinger, E., Garrette, D. (2019).\nHow multilingual is multilingual BERT?\n\\emph{ACL}.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nRaghu, M., Gilmer, J., Yosinski, J., Sohl-Dickstein, J. (2017).\nSVCCA: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\emph{NeurIPS}.\n\n\\bibitem[Turner et~al.(2023)]{turner2023activation}\nTurner, A., Thiergart, L., Udell, D., et~al. (2023).\nActivation addition: Steering language models without optimization.\n\\emph{arXiv:2308.10248}.\n\n\\bibitem[Vig et~al.(2020)]{vig2020investigating}\nVig, J., Gehrmann, S., Belinkov, Y., et~al. (2020).\nInvestigating gender bias in language models using causal mediation analysis.\n\\emph{NeurIPS}.\n\n\\bibitem[Wendler et~al.(2024)]{wendler2024lost}\nWendler, C., Veselovsky, V., Monea, G., West, R. (2024).\nDo llamas work in English? On the latent language of multilingual transformers.\n\\emph{ACL}.\n\n\\bibitem[Wu et~al.(2025)]{wu2025spare}\nWu, Z., Chen, X., Li, J. (2025).\nSpARE: Sparse autoencoder-based representation engineering for knowledge conflict steering.\n\\emph{arXiv}.\n\n\\bibitem[Xie et~al.(2024)]{xie2024adaptive}\nXie, J., Zhang, K., Chen, J., et~al. (2024).\nAdaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts.\n\\emph{ICLR}.\n\n\\bibitem[Zhao et~al.(2026)]{zhao2026clear}\nZhao, Y., et~al. (2026).\nCLEAR: Cross-lingual entity-centric factual conflict resolution in multilingual LLMs.\n\\emph{ACL}.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "5523168f-46d1-4d52-b131-c119d5c39c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifact…",
  "leafUuid": "97c70bcd-d60b-4d29-a5dd-78f200e9ea1b",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Tool call

_source line 24 · 2026-05-22T03:04:56.381Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01D1VremKvQHXno15rL3JoUn`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97c70bcd-d60b-4d29-a5dd-78f200e9ea1b",
  "isSidechain": false,
  "requestId": "req_011CbGsCytyh2Xo4HP87okMA",
  "type": "assistant",
  "uuid": "7837afdd-0608-4183-ba2b-b024041534f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bhezdQtRNSvU3wssXMuuw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11395,
      "cache_read_input_tokens": 41990,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 41990,
          "cache_creation_input_tokens": 11395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11395
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

_source line 25 · 2026-05-22T03:04:59.021Z_

<details><summary>↩ Tool result · `toolu_01D1VremKvQHXno15rL3JoUn`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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

Package natbib Warning: Citation `zhao2026clear' on page 1 undefined on input l
ine 41.


Package natbib Warning: Citation `cumming2014new' on page 1 undefined on input 
line 51.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:detectability' on page 2 undefined on input line 
55.


LaTeX Warning: Reference `sec:asymmetry' on page 2 undefined on input line 55.


LaTeX Warning: Reference `sec:method' on page 2 undefined on input line 56.


Package natbib Warning: Citation `wendler2024lost' on page 2 undefined on input
 line 57.


LaTeX Warning: Reference `sec:layerwise' on page 2 undefined on input line 57.


LaTeX Warning: Reference `sec:steering' on page 2 undefined on input line 57.


Package natbib Warning: Citation `longpre2021entity' on page 2 undefined on inp
ut line 64.


Package natbib Warning: Citation `chen2022rich' on page 2 undefined on input li
ne 64.


Package natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input
 line 64.


Package natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input
 line 64.


Package natbib Warning: Citation `zhao2026clear' on page 2 undefined on input l
ine 64.


Package natbib Warning: Citation `pires2019multilingual' on page 2 undefined on
 input line 67.


Package natbib Warning: Citation `chi2020finding' on page 2 undefined on input 
line 67.


Package natbib Warning: Citation `wendler2024lost' on page 2 undefined on input
 line 67.


Package natbib Warning: Citation `belinkov2022probing' on page 2 undefined on i
nput line 70.


Package natbib Warning: Citation `bricken2023monosemanticity' on page 2 undefin
ed on input line 70.


Package natbib Warning: Citation `cunningham2023sparse' on page 2 undefined on 
input line 70.


Package natbib Warning: Citation `wu2025spare' on page 2 undefined on input lin
e 70.


Package natbib Warning: Citation `turner2023activation' on page 2 undefined on 
input line 73.


Package natbib Warning: Citation `marks2024geometry' on page 2 undefined on inp
ut line 73.


Package natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input
 line 81.

[2]

Package natbib Warning: Citation `kornblith2019similarity' on page 3 undefined 
on input line 112.


Package natbib Warning: Citation `raghu2017svcca' on page 3 undefined on input 
line 112.


LaTeX Warning: Reference `sec:sae-results' on page 3 undefined on input line 12
0.


LaTeX Warning: Reference `tab:expanded' on page 3 undefined on input line 128.


LaTeX Warning: Reference `tab:gemma' on page 3 undefined on input line 148.

[3]

LaTeX Warning: Reference `tab:cross-arch' on page 4 undefined on input line 168
.


Package natbib Warning: Citation `cumming2014new' on page 4 undefined on input 
line 168.


LaTeX Warning: Reference `tab:ja' on page 4 undefined on input line 192.


LaTeX Warning: Reference `tab:cross-lang' on page 4 undefined on input line 212
.


LaTeX Warning: Reference `tab:cka' on page 4 undefined on input line 231.


Package natbib Warning: Citation `wendler2024lost' on page 4 undefined on input
 line 231.


LaTeX Warning: Reference `tab:transition' on page 4 undefined on input line 249
.

[4]

LaTeX Warning: Reference `tab:pca' on page 5 undefined on input line 271.


LaTeX Warning: Reference `tab:steering' on page 5 undefined on input line 292.


LaTeX Warning: Reference `tab:alpha' on page 5 undefined on input line 310.


Package natbib Warning: Citation `vig2020investigating' on page 5 undefined on 
input line 329.


Package natbib Warning: Citation `geiger2024finding' on page 5 undefined on inp
ut line 329.

[5]

LaTeX Warning: Reference `app:sae' on page 6 undefined on input line 345.


Package natbib Warning: Citation `zhao2026clear' on page 6 undefined on input l
ine 349.

[6]

LaTeX Warning: Reference `app:sae' on page 7 undefined on input line 361.


LaTeX Warning: Reference `tab:noise' on page 7 undefined on input line 382.


LaTeX Warning: `h' float specifier changed to `ht'.

[7]

LaTeX Warning: Reference `tab:sae' on page 8 undefined on input line 408.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:langfir' on page 8 undefined on input line 430.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:jaccard' on page 8 undefined on input line 452.


LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9]

Package natbib Warning: There were undefined citations.

[10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
Font metrics written on ecrm0700.tfm.
Output written on ecrm0700.600gf (256 characters, 37344 bytes).
Transcript written on ecrm0700.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm100
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1
000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecb
x1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
crm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecbx1440.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti0900
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti0900
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti0900.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf
 Ok [25] [26] [27] [28] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf
 Ok) ) ) )
Font metrics written on ecti0900.tfm.
Output written on ecti0900.600gf (256 characters, 48652 bytes).
Transcript written on ecti0900.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti0900.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy9.pfb>
Output written on paper.pdf (10 pages, 239691 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: Reference `sec:sae-results' on page 3 undefined on input line 12
0.

[3] [4] [5] [6] [7]

LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9] [10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm100
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1
000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect
i1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
crm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm
i9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy9.pfb>
Output written on paper.pdf (10 pages, 244709 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7837afdd-0608-4183-ba2b-b024041534f8",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "466b3ea8-4a3a-43aa-afc0-86e852e1c6ab",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `zhao2026clear' on page 1 undefined on input l\nine 41.\n\n\nPackage natbib Warning: Citation `cumming2014new' on page 1 undefined on input \nline 51.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:detectability' on page 2 undefined on input line \n55.\n\n\nLaTeX Warning: Reference `sec:asymmetry' on page 2 undefined on input line 55.\n\n\nLaTeX Warning: Reference `sec:method' on page 2 undefined on input line 56.\n\n\nPackage natbib Warning: Citation `wendler2024lost' on page 2 undefined on input\n line 57.\n\n\nLaTeX Warning: Reference `sec:layerwise' on page 2 undefined on input line 57.\n\n\nLaTeX Warning: Reference `sec:steering' on page 2 undefined on input line 57.\n\n\nPackage natbib Warning: Citation `longpre2021entity' on page 2 undefined on inp\nut line 64.\n\n\nPackage natbib Warning: Citation `chen2022rich' on page 2 undefined on input li\nne 64.\n\n\nPackage natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input\n line 64.\n\n\nPackage natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input\n line 64.\n\n\nPackage natbib Warning: Citation `zhao2026clear' on page 2 undefined on input l\nine 64.\n\n\nPackage natbib Warning: Citation `pires2019multilingual' on page 2 undefined on\n input line 67.\n\n\nPackage natbib Warning: Citation `chi2020finding' on page 2 undefined on input \nline 67.\n\n\nPackage natbib Warning: Citation `wendler2024lost' on page 2 undefined on input\n line 67.\n\n\nPackage natbib Warning: Citation `belinkov2022probing' on page 2 undefined on i\nnput line 70.\n\n\nPackage natbib Warning: Citation `bricken2023monosemanticity' on page 2 undefin\ned on input line 70.\n\n\nPackage natbib Warning: Citation `cunningham2023sparse' on page 2 undefined on \ninput line 70.\n\n\nPackage natbib Warning: Citation `wu2025spare' on page 2 undefined on input lin\ne 70.\n\n\nPackage natbib Warning: Citation `turner2023activation' on page 2 undefined on \ninput line 73.\n\n\nPackage natbib Warning: Citation `marks2024geometry' on page 2 undefined on inp\nut line 73.\n\n\nPackage natbib Warning: Citation `xie2024adaptive' on page 2 undefined on input\n line 81.\n\n[2]\n\nPackage natbib Warning: Citation `kornblith2019similarity' on page 3 undefined \non input line 112.\n\n\nPackage natbib Warning: Citation `raghu2017svcca' on page 3 undefined on input \nline 112.\n\n\nLaTeX Warning: Reference `sec:sae-results' on page 3 undefined on input line 12\n0.\n\n\nLaTeX Warning: Reference `tab:expanded' on page 3 undefined on input line 128.\n\n\nLaTeX Warning: Reference `tab:gemma' on page 3 undefined on input line 148.\n\n[3]\n\nLaTeX Warning: Reference `tab:cross-arch' on page 4 undefined on input line 168\n.\n\n\nPackage natbib Warning: Citation `cumming2014new' on page 4 undefined on input \nline 168.\n\n\nLaTeX Warning: Reference `tab:ja' on page 4 undefined on input line 192.\n\n\nLaTeX Warning: Reference `tab:cross-lang' on page 4 undefined on input line 212\n.\n\n\nLaTeX Warning: Reference `tab:cka' on page 4 undefined on input line 231.\n\n\nPackage natbib Warning: Citation `wendler2024lost' on page 4 undefined on input\n line 231.\n\n\nLaTeX Warning: Reference `tab:transition' on page 4 undefined on input line 249\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:pca' on page 5 undefined on input line 271.\n\n\nLaTeX Warning: Reference `tab:steering' on page 5 undefined on input line 292.\n\n\nLaTeX Warning: Reference `tab:alpha' on page 5 undefined on input line 310.\n\n\nPackage natbib Warning: Citation `vig2020investigating' on page 5 undefined on \ninput line 329.\n\n\nPackage natbib Warning: Citation `geiger2024finding' on page 5 undefined on inp\nut line 329.\n\n[5]\n\nLaTeX Warning: Reference `app:sae' on page 6 undefined on input line 345.\n\n\nPackage natbib Warning: Citation `zhao2026clear' on page 6 undefined on input l\nine 349.\n\n[6]\n\nLaTeX Warning: Reference `app:sae' on page 7 undefined on input line 361.\n\n\nLaTeX Warning: Reference `tab:noise' on page 7 undefined on input line 382.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[7]\n\nLaTeX Warning: Reference `tab:sae' on page 8 undefined on input line 408.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:langfir' on page 8 undefined on input line 430.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:jaccard' on page 8 undefined on input line 452.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0700\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0700\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0700.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\nFont metrics written on ecrm0700.tfm.\nOutput written on ecrm0700.600gf (256 characters, 37344 bytes).\nTranscript written on ecrm0700.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm100\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1\n000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecb\nx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecbx1440.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecti0900\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecti0900\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti0900.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecti.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/extextit.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exileast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exilig.mf\n Ok [25] [26] [27] [28] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exitalp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exillett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exidigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exiligtb.mf\n Ok) ) ) )\nFont metrics written on ecti0900.tfm.\nOutput written on ecti0900.600gf (256 characters, 48652 bytes).\nTranscript written on ecti0900.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti0900.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy9.pfb>\nOutput written on paper.pdf (10 pages, 239691 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `sec:sae-results' on page 3 undefined on input line 12\n0.\n\n[3] [4] [5] [6] [7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9] [10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0700.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm100\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1\n000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect\ni1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmm\ni9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy9.pfb>\nOutput written on paper.pdf (10 pages, 244709 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7837afdd-0608-4183-ba2b-b024041534f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifact…",
  "leafUuid": "466b3ea8-4a3a-43aa-afc0-86e852e1c6ab",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Assistant

_source line 28 · 2026-05-22T03:05:06.148Z_

<details><summary>Logged reasoning block</summary>

```text
There's one undefined reference `sec:sae-results` that I should fix. Let me also do a third pass to resolve remaining cross-references. But first let me fix the undefined label.

Looking at the tex, I have `\label{sec:sae-results}` referenced but I used `\label{app:sae}` for the SAE appendix. I need to add `\label{sec:sae-results}` somewhere or change the reference. The reference is on line 120: "Due to the base--instruct distribution mismatch (Section~\ref{sec:sae-results})". 

I'll just update that reference to point to `\ref{app:sae}` instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "466b3ea8-4a3a-43aa-afc0-86e852e1c6ab",
  "isSidechain": false,
  "requestId": "req_011CbGsDRRe1AGA59nzuoFic",
  "type": "assistant",
  "uuid": "792698aa-cd66-49b0-b41a-28862bd59720",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011u4d8t2sAcDAC2jgsWoUEp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10822,
      "cache_read_input_tokens": 53385,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 53385,
          "cache_creation_input_tokens": 10822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10822
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

_source line 29 · 2026-05-22T03:05:06.150Z_

One undefined reference to fix — `sec:sae-results` should be `app:sae`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "792698aa-cd66-49b0-b41a-28862bd59720",
  "isSidechain": false,
  "requestId": "req_011CbGsDRRe1AGA59nzuoFic",
  "type": "assistant",
  "uuid": "24ccd268-e518-4ee8-bd0b-9593f6fe1787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011u4d8t2sAcDAC2jgsWoUEp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10822,
      "cache_read_input_tokens": 53385,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 53385,
          "cache_creation_input_tokens": 10822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10822
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

_source line 30 · 2026-05-22T03:05:08.531Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01EEjDvLCKXf816xpJob1x1n`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
  "old_string": "Due to the base--instruct distribution mismatch (Section~\\ref{sec:sae-results}), these results are preliminary.",
  "new_string": "Due to the base--instruct distribution mismatch (Appendix~\\ref{app:sae}), these results are preliminary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ccd268-e518-4ee8-bd0b-9593f6fe1787",
  "isSidechain": false,
  "requestId": "req_011CbGsDRRe1AGA59nzuoFic",
  "type": "assistant",
  "uuid": "709bd3aa-4924-415e-93fd-b38a98189cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011u4d8t2sAcDAC2jgsWoUEp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10822,
      "cache_read_input_tokens": 53385,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 383,
          "cache_read_input_tokens": 53385,
          "cache_creation_input_tokens": 10822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10822
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

_source line 31 · 2026-05-22T03:05:08.550Z_

<details><summary>↩ Tool result · `toolu_01EEjDvLCKXf816xpJob1x1n`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "709bd3aa-4924-415e-93fd-b38a98189cd7",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "9d2dac4a-3ef1-4e6e-8804-77694f777c89",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.tex",
    "oldString": "Due to the base--instruct distribution mismatch (Section~\\ref{sec:sae-results}), these results are preliminary.",
    "newString": "Due to the base--instruct distribution mismatch (Appendix~\\ref{app:sae}), these results are preliminary.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 117,
        "oldLines": 7,
        "newStart": 117,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Preliminary SAE Analysis}",
          " ",
          "-We apply Qwen-Scope pretrained SAEs (65,536 features, trained on Qwen3-8B-Base) to analyze conflict activations. We select features by mutual information (MI $> 0.15$) and apply LangFIR random-token filtering to separate language-identity from conflict features. Due to the base--instruct distribution mismatch (Section~\\ref{sec:sae-results}), these results are preliminary.",
          "+We apply Qwen-Scope pretrained SAEs (65,536 features, trained on Qwen3-8B-Base) to analyze conflict activations. We select features by mutual information (MI $> 0.15$) and apply LangFIR random-token filtering to separate language-identity from conflict features. Due to the base--instruct distribution mismatch (Appendix~\\ref{app:sae}), these results are preliminary.",
          " ",
          " %% ===== 4. EXPERIMENTS AND RESULTS =====",
          " \\section{Experiments and Results}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "709bd3aa-4924-415e-93fd-b38a98189cd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-22T03:05:12.474Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V3D6CQAiLuAbeZW1jNXEng`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Warning|Error|Output written)\"",
  "description": "Recompile LaTeX and check for remaining warnings",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d2dac4a-3ef1-4e6e-8804-77694f777c89",
  "isSidechain": false,
  "requestId": "req_011CbGsE8J2MbsokL3R32Wja",
  "type": "assistant",
  "uuid": "235863ac-c4b5-459d-b632-72e84a2f0547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013rPHHpvMwKLMCtwj7fNtFn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 64207,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 64207,
          "cache_creation_input_tokens": 466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 466
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

_source line 33 · 2026-05-22T03:05:13.983Z_

<details><summary>↩ Tool result · `toolu_01V3D6CQAiLuAbeZW1jNXEng`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7]

LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9] [10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfo
ur/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/lj
four/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/
ljfour/jknappen/ec/tcrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p
k/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts
/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fon
ts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/f
onts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var
/fonts/pk/ljfour/jknappen/ec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-v
ar/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf
-var/fonts/pk/ljfour/jknappen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/tex
mf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/t
exmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>
Output written on paper.pdf (10 pages, 244367 bytes).
Transcript written on paper.log.
LaTeX Warning: `h' float specifier changed to `ht'.
Output written on paper.pdf (10 pages, 244367 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "235863ac-c4b5-459d-b632-72e84a2f0547",
  "isSidechain": false,
  "promptId": "08f70c20-9f81-45e8-8594-eb4e1ba9c04c",
  "type": "user",
  "uuid": "8f49d3b8-80b7-4cbf-80fc-a3c41d2ef246",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9] [10] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfo\nur/jknappen/ec/ecrm0700.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/lj\nfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/\nljfour/jknappen/ec/tcrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/p\nk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts\n/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fon\nts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/f\nonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var\n/fonts/pk/ljfour/jknappen/ec/ecti0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf-v\nar/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive2025/texmf\n-var/fonts/pk/ljfour/jknappen/ec/ecbx0900.600pk> &lt;/home/ubuntu/.texlive2025/tex\nmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/t\nexmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>\nOutput written on paper.pdf (10 pages, 244367 bytes).\nTranscript written on paper.log.\nLaTeX Warning: `h' float specifier changed to `ht'.\nOutput written on paper.pdf (10 pages, 244367 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "235863ac-c4b5-459d-b632-72e84a2f0547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-22T03:05:13.989Z_

```json
{
  "parentUuid": "8f49d3b8-80b7-4cbf-80fc-a3c41d2ef246",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "395be1ee-e5e0-44e9-ae68-c25fec57e9a2",
  "timestamp": "2026-05-22T03:05:13.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-22T03:05:26.119Z_

编译成功，10 页 PDF，无 undefined reference（仅一个 `h` float 自动升级为 `ht`，无影响）。

输出文件：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median/paper.pdf`

论文覆盖了 experiment_data.json 中全部 12 个实验：
- **Main body** (Sec 4.1–4.6): 数据集扩展、三模型架构验证 (Gemma)、EN↔JA 多语言扩展、Layer-wise CKA/SVCCA、PCA 可视化、Representation steering
- **Appendix A**: Label noise robustness
- **Appendix B** (B.1–B.3): SAE 特征识别、LangFIR 解耦、Jaccard 分析（均标注为 preliminary/inconclusive）
- **Future work**: Track 3 三个未执行实验明确归入 Section 5.5

叙事按 narrative guidance 执行：C1 为主 claim，C2 强调 effect size stability (6.6±0.9pp, I²=0%)，引用 Cumming (2014)，RC8 限定为 correlational evidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "395be1ee-e5e0-44e9-ae68-c25fec57e9a2",
  "isSidechain": false,
  "requestId": "req_011CbGsEXQLFPA4t87FBceVg",
  "type": "assistant",
  "uuid": "b2cfb6ff-27b9-444f-b7a2-2245b308567f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/dream_reports/dream_20260522T023801/median",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RsnjgR1qXNdV6ez79fRyMu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 64673,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 64673,
          "cache_creation_input_tokens": 3165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3165
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260522T023801 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifact…",
  "leafUuid": "b2cfb6ff-27b9-444f-b7a2-2245b308567f",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated research paper for dream agent",
  "sessionId": "e8bbcfe2-4536-4e05-a4c5-615fca01f226"
}
```

---
