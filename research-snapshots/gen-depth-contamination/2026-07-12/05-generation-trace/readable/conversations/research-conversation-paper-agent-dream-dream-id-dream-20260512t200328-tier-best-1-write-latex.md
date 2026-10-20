# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/15869c0c-9668-4be3-a2a7-f75590b57af9.jsonl`
- **Structured JSON:** [`5e9cbe405999d39a6485.json`](../../sessions/5e/5e9cbe405999d39a6485.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:22:44.711Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:22:44.711Z",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026\n- Narrative guidance：Original framing holds intact. K* is a first-measured, modulable information-theoretic boundary. Story: \"We establish K* as a fundamental quantity that varies predictably with model scale and decoding strategy (K*=2 at 1.5B, K*=3 at 7B / high-temperature), reveal a universal degradation ordering (lexical diversity collapses before distributional dynamics), and show that even a coarse 3-class depth signal yields 1.5-3.5% downstream improvement over binary filtering.\" All three claims (C1 saturation boundary, C2 degradation ordering, C3 graduated filtering) are well-supported. K* modulability directly addresses the \"K*=2 is too shallow\" concern. Target: EMNLP 2026 Main.\n\n- paper_framing.md 节选：\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Core Claims (3 条)\n\n1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。\n2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。\n3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix\n4. **\"单模型/单数据集，泛化性不够\"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → 显式讨论此 design choice：这衡量的是\"模型对自身递归输出的 self-recognition\"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 \"Resources and Evaluation\" track 的要求\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty\n\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T20:22:44.714Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:22:44.714Z",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-12T20:22:44.733Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026
- Narrative guidance：Original framing holds intact. K* is a first-measured, modulable information-theoretic boundary. Story: "We establish K* as a fundamental quantity that varies predictably with model scale and decoding strategy (K*=2 at 1.5B, K*=3 at 7B / high-temperature), reveal a universal degradation ordering (lexical diversity collapses before distributional dynamics), and show that even a coarse 3-class depth signal yields 1.5-3.5% downstream improvement over binary filtering." All three claims (C1 saturation boundary, C2 degradation ordering, C3 graduated filtering) are well-supported. K* modulability directly addresses the "K*=2 is too shallow" concern. Target: EMNLP 2026 Main.

- paper_framing.md 节选：
# Paper Framing — gen-depth-contamination

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Backup: AAAI 2027 (abstract July 25, paper August 1)

## Core Claims (3 条)

1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。
2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。
3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。

## Story Spine

- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。
- **Headline result template**: "We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag."

## Anticipated Reviewer Concerns & Responses

1. **"K*=2 太浅，graduated filtering 收益有限"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated
2. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身
3. **"Prompt-chain 不代表真实世界递归污染"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix
4. **"单模型/单数据集，泛化性不够"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集
5. **"同模型做生成和 surprisal 计算有 bias"** → 显式讨论此 design choice：这衡量的是"模型对自身递归输出的 self-recognition"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的
6. **"为什么不用 learned representations"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 "Resources and Evaluation" track 的要求
- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty


## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "6272820c-5646-4007-a64f-a4f895541757",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:22:44.732Z_

```json
{
  "parentUuid": "6272820c-5646-4007-a64f-a4f895541757",
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
  "uuid": "16d5712e-9cb2-42c3-b1cb-3dbf40803d7f",
  "timestamp": "2026-05-12T20:22:44.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:22:44.732Z_

```json
{
  "parentUuid": "16d5712e-9cb2-42c3-b1cb-3dbf40803d7f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "77071298-4de4-4c87-a90e-021134972340",
  "timestamp": "2026-05-12T20:22:44.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
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
  "aiTitle": "Generate simulated paper for dream_20260512T200328",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Assistant

_source line 7 · 2026-05-12T20:22:47.119Z_

Let me start by reading the experiment data and understanding the project structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77071298-4de4-4c87-a90e-021134972340",
  "isSidechain": false,
  "requestId": "req_011CayJG935D7VJ41dqB6D3D",
  "type": "assistant",
  "uuid": "d553dab0-6f91-4e0b-aae4-f0f69ebd4433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oTjc8PwS6vi4fcmoYdC35",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12529
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

_source line 8 · 2026-05-12T20:22:49.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SK9Baj7y1b1tEZ8itgXRZ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d553dab0-6f91-4e0b-aae4-f0f69ebd4433",
  "isSidechain": false,
  "requestId": "req_011CayJG935D7VJ41dqB6D3D",
  "type": "assistant",
  "uuid": "a3486cdc-3fdf-47e0-ad08-0b590f3d5db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oTjc8PwS6vi4fcmoYdC35",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12529,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12529
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

_source line 9 · 2026-05-12T20:22:50.109Z_

<details><summary>↩ Tool result · `toolu_01SK9Baj7y1b1tEZ8itgXRZ7`</summary>

```text
1	[
2	  {
3	    "name": "Pythia-1.4B depth chain generation",
4	    "description": "Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5",
5	    "results": {
6	      "pairwise_auc_0v1": 0.991,
7	      "pairwise_auc_1v2": 0.672,
8	      "pairwise_auc_2v3": 0.571,
9	      "pairwise_auc_3v4": 0.533,
10	      "pairwise_auc_4v5": 0.521,
11	      "pairwise_jsd_0v1": 0.243,
12	      "pairwise_jsd_1v2": 0.014,
13	      "pairwise_jsd_2v3": 0.005,
14	      "pairwise_jsd_3v4": 0.003,
15	      "pairwise_jsd_4v5": 0.002,
16	      "k_star": 2,
17	      "ordinal_accuracy": 0.401,
18	      "ordinal_mae": 1.08
19	    },
20	    "tables": [
21	      {
22	        "caption": "Pythia-1.4B pairwise discrimination across depths",
23	        "columns": [
24	          "depth_pair",
25	          "AUC_mean",
26	          "AUC_std",
27	          "JSD"
28	        ],
29	        "rows": [
30	          [
31	            "0v1",
32	            0.991,
33	            0.001,
34	            0.243
35	          ],
36	          [
37	            "1v2",
38	            0.672,
39	            0.008,
40	            0.014
41	          ],
42	          [
43	            "2v3",
44	            0.571,
45	            0.011,
46	            0.005
47	          ],
48	          [
49	            "3v4",
50	            0.533,
51	            0.006,
52	            0.003
53	          ],
54	          [
55	            "4v5",
56	            0.521,
57	            0.009,
58	            0.002
59	          ]
60	        ]
61	      }
62	    ],
63	    "figures": [],
64	    "analysis": "Pythia 确认 1.5B 规模下 K*=2 的鲁棒性。1v2 AUC=0.672 落入 best 档 [0.65, 0.75] 范围。 与 MVP 的差异（Δ AUC_1v2 = -0.024）方向符合预期：更弱的预训练基础 → 更浅的代际信号。 这支持 C1：K* 是模型能力的函数而非固定常数。\n\n\nPythia-1.4B 与 MVP 的 Qwen2.5-1.5B 参数规模相近但架构更旧（GPT-NeoX 基础）， 预训练数据量和质量略逊于 Qwen2.5。因此 0v1 AUC 仍极高（递归首代信息损失显著）， 但 1v2 AUC 略低于 Qwen（0.672 vs 0.696），因为 Pythia 生成质量本身更低， 递归代际间的边际信息损失更小——即\"起点已经更差，所以每代退化的增量更不明显\"。 K* 仍为 2，因为在 1.5B 规模 + 标准解码下，DPI 决定的信息瓶颈位置一致。 JSD 衰减模式与 MVP 高度一致（0v1 远大于后续），验证跨模型的 DPI 收敛规律。\n"
65	  },
66	  {
67	    "name": "OLMo-1B depth chain generation",
68	    "description": "OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5",
69	    "results": {
70	      "pairwise_auc_0v1": 0.988,
71	      "pairwise_auc_1v2": 0.654,
72	      "pairwise_auc_2v3": 0.558,
73	      "pairwise_auc_3v4": 0.527,
74	      "pairwise_auc_4v5": 0.515,
75	      "pairwise_jsd_0v1": 0.221,
76	      "pairwise_jsd_1v2": 0.012,
77	      "pairwise_jsd_2v3": 0.004,
78	      "pairwise_jsd_3v4": 0.003,
79	      "pairwise_jsd_4v5": 0.002,
80	      "k_star": 2,
81	      "ordinal_accuracy": 0.388,
82	      "ordinal_mae": 1.12
83	    },
84	    "tables": [
85	      {
86	        "caption": "OLMo-1B pairwise discrimination across depths",
87	        "columns": [
88	          "depth_pair",
89	          "AUC_mean",
90	          "AUC_std",
91	          "JSD"
92	        ],
93	        "rows": [
94	          [
95	            "0v1",
96	            0.988,
97	            0.001,
98	            0.221
99	          ],
100	          [
101	            "1v2",
102	            0.654,
103	            0.009,
104	            0.012
105	          ],
106	          [
107	            "2v3",
108	            0.558,
109	            0.013,
110	            0.004
111	          ],
112	          [
113	            "3v4",
114	            0.527,
115	            0.007,
116	            0.003
117	          ],
118	          [
119	            "4v5",
120	            0.515,
121	            0.01,
122	            0.002
123	          ]
124	        ]
125	      }
126	    ],
127	    "figures": [],
128	    "analysis": "OLMo 作为最小模型提供了 scale 连续体的下端锚点。1v2 AUC=0.654 恰在 best 档下限， 表明 1B 级是当前实验设置下 depth signal 的近似下界。三模型一致的 K*=2 强力支持 C1：K* 在 1-1.5B 规模下是信息论约束的稳健结果，而非某个模型的 artifact。\n\n\nOLMo-1B 参数量最小（1B vs 1.4-1.5B），且 OLMo 的 Dolma 预训练数据虽公开透明但 多样性略低于 Qwen 的预训练混合。更小的模型容量意味着单次生成的信息保持率更低， 因此 0v1 JSD 略低（起始分布差异稍小）。但关键是 1v2 AUC=0.654 仍在 best 档下限附近， K* 仍为 2——DPI 理论预测的收敛行为不依赖于具体架构细节，只依赖于信道容量， 而 1B 级模型的信道容量与 1.5B 级处于同一量级。ordinal 性能略低因信号更弱。\n"
129	  },
130	  {
131	    "name": "Qwen2.5-1.5B decoding strategy ablation",
132	    "description": "Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs, depth 0-5",
133	    "results": {
134	      "greedy": {
135	        "k_star": 2,
136	        "pairwise_auc_1v2": 0.651,
137	        "pairwise_auc_2v3": 0.554,
138	        "pairwise_jsd_0v1": 0.234
139	      },
140	      "nucleus_p0.9": {
141	        "k_star": 2,
142	        "pairwise_auc_1v2": 0.688,
143	        "pairwise_auc_2v3": 0.582,
144	        "pairwise_jsd_0v1": 0.259
145	      },
146	      "temp_0.7": {
147	        "k_star": 2,
148	        "pairwise_auc_1v2": 0.668,
149	        "pairwise_auc_2v3": 0.563,
150	        "pairwise_jsd_0v1": 0.241
151	      },
152	      "temp_1.2": {
153	        "k_star": 3,
154	        "pairwise_auc_1v2": 0.723,
155	        "pairwise_auc_2v3": 0.648,
156	        "pairwise_auc_3v4": 0.574,
157	        "pairwise_auc_4v5": 0.531,
158	        "pairwise_jsd_0v1": 0.312,
159	        "pairwise_jsd_1v2": 0.028,
160	        "pairwise_jsd_2v3": 0.011,
161	        "pairwise_jsd_3v4": 0.005
162	      }
163	    },
164	    "tables": [
165	      {
166	        "caption": "Decoding strategy ablation: K* and key pairwise AUCs",
167	        "columns": [
168	          "decoding",
169	          "K*",
170	          "AUC_0v1",
171	          "AUC_1v2",
172	          "AUC_2v3",
173	          "AUC_3v4",
174	          "JSD_0v1"
175	        ],
176	        "rows": [
177	          [
178	            "greedy",
179	            2,
180	            0.993,
181	            0.651,
182	            0.554,
183	            0.526,
184	            0.234
185	          ],
186	          [
187	            "nucleus p=0.9",
188	            2,
189	            0.994,
190	            0.688,
191	            0.582,
192	            0.538,
193	            0.259
194	          ],
195	          [
196	            "T=0.7",
197	            2,
198	            0.993,
199	            0.668,
200	            0.563,
201	            0.53,
202	            0.241
203	          ],
204	          [
205	            "T=1.2",
206	            3,
207	            0.997,
208	            0.723,
209	            0.648,
210	            0.574,
211	            0.312
212	          ],
213	          [
214	            "MVP (p=0.95 T=1.0)",
215	            2,
216	            0.996,
217	            0.696,
218	            0.589,
219	            0.543,
220	            0.267
221	          ]
222	        ]
223	      }
224	    ],
225	    "figures": [],
226	    "analysis": "这是论文的核心实验之一。T=1.2 → K*=3 直接证明 K* 是可调控的，消解\"K*=2 太浅\"的审稿人顾虑。 解码策略形成清晰的 K* 调控梯度：greedy ≤ low-temp ≤ standard nucleus ≤ high-temp。 这为 C1 提供了因果方向性证据：不是分类器能力限制了 K*，而是信道特性决定了 K*。\n\n\n解码策略通过控制 generation entropy 直接调控信道的有效容量。 Greedy 解码（T→0）将输出限制在最高概率 token，递归代际间差异被压缩到很窄的 mode 附近， 导致 1v2 AUC 最低——信息损失在首代就已经高度集中，后续代际几乎无额外损失可测。 T=0.7 和 nucleus p=0.9 居于中间：适度随机性保留了更多分布结构供后续代际逐步丢失。 T=1.2 是关键条件：高温度扩大了 token 采样空间，使得每代生成引入更多\"非主流\"token 选择， 这些选择在递归中被逐步\"洗掉\"——但因为起始多样性更高，这个洗掉过程需要更多代际才能饱和。 信息论解释：高温度提高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减， 但更高的起点意味着降到阈值需要更多步——因此 K* 从 2 升到 3。 这直接验证核心假设 1，且 2v3 AUC=0.648 落入 best 档 [0.62, 0.70]。\n"
227	  },
228	  {
229	    "name": "Qwen2.5-7B cross-scale probe",
230	    "description": "Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3",
231	    "results": {
232	      "pairwise_auc_0v1": 0.998,
233	      "pairwise_auc_1v2": 0.741,
234	      "pairwise_auc_2v3": 0.662,
235	      "pairwise_jsd_0v1": 0.341,
236	      "pairwise_jsd_1v2": 0.032,
237	      "pairwise_jsd_2v3": 0.013,
238	      "k_star": 3,
239	      "ordinal_accuracy": 0.518,
240	      "ordinal_mae": 0.81
241	    },
242	    "tables": [
243	      {
244	        "caption": "Qwen2.5-7B vs 1.5B pairwise discrimination comparison",
245	        "columns": [
246	          "depth_pair",
247	          "7B_AUC",
248	          "7B_JSD",
249	          "1.5B_AUC (MVP)",
250	          "1.5B_JSD (MVP)"
251	        ],
252	        "rows": [
253	          [
254	            "0v1",
255	            0.998,
256	            0.341,
257	            0.996,
258	            0.267
259	          ],
260	          [
261	            "1v2",
262	            0.741,
263	            0.032,
264	            0.696,
265	            0.016
266	          ],
267	          [
268	            "2v3",
269	            0.662,
270	            0.013,
271	            0.589,
272	            0.007
273	          ]
274	        ]
275	      }
276	    ],
277	    "figures": [],
278	    "analysis": "7B 实验确认核心假设 2：模型规模是 K* 的杠杆。K*=3 且 ordinal accuracy=0.518 证明更大模型在标准解码下就能支持更细粒度的 depth estimation。 结合 exp-003 (T=1.2 → K*=3)，两条独立路径都能将 K* 推到 3， 彻底消解\"K*=2 是天花板\"的叙事风险。对 EMNLP 审稿人的回应： \"K*=2 is not a ceiling but a floor that rises with model scale and decoding entropy.\"\n\n\n7B 模型的关键优势是更大的参数空间编码了更丰富的语言分布。递归生成时， 每代输出保留了更多原始分布的细微结构（rare n-grams、长距离依赖、discourse patterns）， 因此代际间的信息损失更\"均匀地分散\"到更多代际中，而不是在前两代就急剧塌缩。 具体机制：7B 模型的 next-token 分布具有更长的\"有意义尾巴\"（tail tokens 仍携带语义信息）， 递归第二代仍能保留这些尾巴 token 的部分分布特征，到第三代才显著丢失—— 因此 2v3 AUC=0.662 仍远高于机会水平，K* 达到 3。 这与 1.5B 级（K*=2）形成鲜明对比，建立了 scale → K* 的因果关系。 ordinal_accuracy=0.518 和 mae=0.81 均落入 best 档最优区间，因为更丰富的代际信号 使 ordinal classifier 有更多可利用的特征梯度。 注意 1K docs（vs 5K）引入更大方差，但 7B 的信号强度弥补了样本量不足。\n"
279	  },
280	  {
281	    "name": "Feature group ablation + degradation ordering",
282	    "description": "对每个模型的 depth chain，按 feature group 分析饱和深度和 degradation ordering",
283	    "results": {
284	      "saturation_depth_vocabulary_diversity": {
285	        "pythia_1.4b": 1,
286	        "olmo_1b": 1,
287	        "qwen_1.5b": 1
288	      },
289	      "saturation_depth_surprisal_dynamics": {
290	        "pythia_1.4b": 2,
291	        "olmo_1b": 2,
292	        "qwen_1.5b": 2
293	      },
294	      "saturation_depth_tail_thinning": {
295	        "pythia_1.4b": 2,
296	        "olmo_1b": 1,
297	        "qwen_1.5b": 2
298	      },
299	      "degradation_ordering_kendall_tau": {
300	        "pythia_vs_qwen": 0.87,
301	        "olmo_vs_qwen": 0.82,
302	        "pythia_vs_olmo": 0.84,
303	        "mean": 0.84
304	      },
305	      "feature_group_auc_at_depth1": {
306	        "vocabulary_diversity": 0.612,
307	        "surprisal_dynamics": 0.693,
308	        "tail_thinning": 0.641
309	      }
310	    },
311	    "tables": [
312	      {
313	        "caption": "Feature group saturation depth by model",
314	        "columns": [
315	          "feature_group",
316	          "Pythia-1.4B",
317	          "OLMo-1B",
318	          "Qwen2.5-1.5B"
319	        ],
320	        "rows": [
321	          [
322	            "vocabulary_diversity",
323	            1,
324	            1,
325	            1
326	          ],
327	          [
328	            "surprisal_dynamics",
329	            2,
330	            2,
331	            2
332	          ],
333	          [
334	            "tail_thinning",
335	            2,
336	            1,
337	            2
338	          ]
339	        ]
340	      },
341	      {
342	        "caption": "Cross-model degradation ordering consistency (Kendall tau)",
343	        "columns": [
344	          "model_pair",
345	          "tau"
346	        ],
347	        "rows": [
348	          [
349	            "Pythia vs Qwen",
350	            0.87
351	          ],
352	          [
353	            "OLMo vs Qwen",
354	            0.82
355	          ],
356	          [
357	            "Pythia vs OLMo",
358	            0.84
359	          ]
360	        ]
361	      }
362	    ],
363	    "figures": [],
364	    "analysis": "Kendall tau 均值 0.84 落入 best 档 [0.8, 1.0]。vocabulary diversity 一致在 depth=1 饱和 而 surprisal dynamics 在 depth=2 饱和，这为 C2 提供了直接证据。 OLMo 的 tail-thinning 在 depth=1 就饱和（vs 其他模型的 depth=2）是因为 1B 模型 本身的 tail 更薄，可在 discussion 中讨论。ordering 的跨模型一致性表明这是 递归生成的结构性规律而非模型特异现象。\n\n\nDPI 约束下，不同语言特征编码的互信息量不同，因此对递归损失的敏感度不同。 Vocabulary diversity（type-token ratio、hapax ratio 等）依赖于 token 分布的尾部—— 递归生成首先\"修剪\"低频 token（因为模型倾向于生成高概率 token）， 导致 vocabulary diversity 在 depth=1 就显著下降并迅速饱和。 Surprisal dynamics（mean surprisal、surprisal variance、auto-MI）编码的是序列级分布结构， 这种高阶统计量需要更多代际的累积损失才会饱和——因为即使 token 频率分布已经变窄， token 间的条件依赖结构仍然部分保持。 Tail-thinning 特征居于中间：它捕捉分布尾部的厚度，与 vocabulary diversity 相关但更稳健。 三个模型族的 ordering 高度一致（Kendall tau ≥ 0.82），因为这个 ordering 反映的是 信息论的结构性规律（边际统计量先于条件统计量饱和），而非特定模型的 artifact。\n"
365	  },
366	  {
367	    "name": "Downstream filtering evaluation",
368	    "description": "Qwen2.5-1.5B depth chain, no-filter / binary / graduated / surprisal-based, 3 seeds, MMLU+HellaSwag",
369	    "results": {
370	      "mmlu_pp": {
371	        "no_filter": 25.31,
372	        "binary": 26.18,
373	        "graduated": 28.42,
374	        "surprisal_based": 27.89
375	      },
376	      "hellaswag_pp": {
377	        "no_filter": 42.67,
378	        "binary": 43.54,
379	        "graduated": 45.61,
380	        "surprisal_based": 45.12
381	      },
382	      "mmlu_std_across_seeds": {
383	        "no_filter": 0.23,
384	        "binary": 0.31,
385	        "graduated": 0.28,
386	        "surprisal_based": 0.35
387	      },
388	      "hellaswag_std_across_seeds": {
389	        "no_filter": 0.19,
390	        "binary": 0.25,
391	        "graduated": 0.22,
392	        "surprisal_based": 0.29
393	      },
394	      "graduated_vs_binary_delta_mmlu_pp": 2.24,
395	      "graduated_vs_binary_delta_hellaswag_pp": 2.07,
396	      "graduated_vs_binary_p_value_mmlu": 0.008,
397	      "graduated_vs_binary_p_value_hellaswag": 0.013
398	    },
399	    "tables": [
400	      {
401	        "caption": "Downstream evaluation: continued pretraining perplexity and benchmark performance",
402	        "columns": [
403	          "strategy",
404	          "MMLU (pp)",
405	          "MMLU_std",
406	          "HellaSwag (pp)",
407	          "HS_std"
408	        ],
409	        "rows": [
410	          [
411	            "no-filter",
412	            25.31,
413	            0.23,
414	            42.67,
415	            0.19
416	          ],
417	          [
418	            "binary",
419	            26.18,
420	            0.31,
421	            43.54,
422	            0.25
423	          ],
424	          [
425	            "graduated (3-class)",
426	            28.42,
427	            0.28,
428	            45.61,
429	            0.22
430	          ],
431	          [
432	            "surprisal-based",
433	            27.89,
434	            0.35,
435	            45.12,
436	            0.29
437	          ]
438	        ]
439	      },
440	      {
441	        "caption": "Statistical significance: graduated vs binary (paired t-test, 3 seeds)",
442	        "columns": [
443	          "benchmark",
444	          "Δ (pp)",
445	          "p-value",
446	          "significant"
447	        ],
448	        "rows": [
449	          [
450	            "MMLU",
451	            2.24,
452	            0.008,
453	            "yes"
454	          ],
455	          [
456	            "HellaSwag",
457	            2.07,
458	            0.013,
459	            "yes"
460	          ]
461	        ]
462	      }
463	    ],
464	    "figures": [],
465	    "analysis": "graduated vs binary Δ=2.24pp (MMLU) 和 2.07pp (HellaSwag) 均落入 best 档范围 [1.5, 3.5] / [1.0, 3.0]。 p < 0.05 跨 3 seeds 确认 C3 成立。graduated 的优势来源明确：对 gen-1 的精细化处理。 surprisal-based 的存在证明即使单一特征也优于 binary，但多维 ordinal signal 更优。\n\n\nBinary filtering 将所有合成文本等同对待——保留或移除。但 gen-1 文本质量远高于 gen-3+， binary 策略要么丢掉高质量的 gen-1（过滤过严 → 损失有用数据）要么保留低质量的 gen-3+（过滤过松 → 引入噪声）。 Graduated filtering 利用 3-class ordinal signal（human / gen-1 / gen-2+）在阈值附近做更精细的决策： 对 gen-1 降权但不完全移除（因为它仍包含大部分原始信息），对 gen-2+ 移除（因为已过 K*）。 这种\"软阈值\"效应在 binary 策略的 precision-recall 权衡最痛苦的区间（gen-1 附近） 提供了 1.5-3.5 个百分点的改善。MMLU 收益（+2.24pp）略高于 HellaSwag（+2.07pp）， 因为 MMLU 对知识密度更敏感——graduated filtering 保留的 gen-1 中知识保真度高于 binary 移除后的缺失。 Surprisal-based 策略也优于 binary 但不及 graduated，因为它只用单一特征维度做决策， 而 graduated 利用了 ordinal classifier 融合的多维信号。 3 seeds 的 std 均 < 0.35pp，p 值 < 0.05，确认统计显著性。\n"
466	  },
467	  {
468	    "name": "K* sensitivity analysis",
469	    "description": "在 AUC 阈值 0.55/0.60/0.65/0.70 下计算 K*，展示稳健性",
470	    "results": {
471	      "qwen_1.5b_mvp": {
472	        "threshold_0.55": 3,
473	        "threshold_0.60": 2,
474	        "threshold_0.65": 2,
475	        "threshold_0.70": 1
476	      },
477	      "pythia_1.4b": {
478	        "threshold_0.55": 3,
479	        "threshold_0.60": 2,
480	        "threshold_0.65": 2,
481	        "threshold_0.70": 1
482	      },
483	      "olmo_1b": {
484	        "threshold_0.55": 2,
485	        "threshold_0.60": 2,
486	        "threshold_0.65": 2,
487	        "threshold_0.70": 1
488	      },
489	      "qwen_1.5b_temp_1.2": {
490	        "threshold_0.55": 4,
491	        "threshold_0.60": 3,
492	        "threshold_0.65": 3,
493	        "threshold_0.70": 2
494	      },
495	      "k_star_stability_within_0.60_0.65": "all models K*=2, perfectly stable"
496	    },
497	    "tables": [
498	      {
499	        "caption": "K* sensitivity to AUC threshold",
500	        "columns": [
501	          "model_condition",
502	          "θ=0.55",
503	          "θ=0.60",
504	          "θ=0.65",
505	          "θ=0.70"
506	        ],
507	        "rows": [
508	          [
509	            "Qwen2.5-1.5B (p=0.95,T=1.0)",
510	            3,
511	            2,
512	            2,
513	            1
514	          ],
515	          [
516	            "Pythia-1.4B (p=0.95,T=1.0)",
517	            3,
518	            2,
519	            2,
520	            1
521	          ],
522	          [
523	            "OLMo-1B (p=0.95,T=1.0)",
524	            2,
525	            2,
526	            2,
527	            1
528	          ],
529	          [
530	            "Qwen2.5-1.5B (T=1.2)",
531	            4,
532	            3,
533	            3,
534	            2
535	          ]
536	        ]
537	      }
538	    ],
539	    "figures": [],
540	    "analysis": "K* 在 θ∈[0.60, 0.65] 的\"合理区间\"内完全稳定，消解了\"K* 是阈值选择的 artifact\"的顾虑。 θ=0.60 作为默认推荐有理论支撑（显著高于 0.5 chance level）和实证支撑（稳定区间中心）。 T=1.2 条件的系统性偏移进一步证实 K* 的调控效应是真实的而非阈值敏感的幻觉。\n\n\nK* 本质是\"pairwise AUC 首次低于阈值的 depth\"，因此它对阈值有阶跃依赖。 但在合理的阈值范围内（0.60-0.65，即\"明显高于 chance 但不要求 near-perfect\"）， K* 应当稳定。原因：MVP 数据显示 AUC 从 1v2 (0.696) 到 2v3 (0.589) 有显著跳跃， 这意味着任何落在 0.589-0.696 之间的阈值都会给出同一个 K*=2。 0.55 阈值过松（2v3 AUC=0.589 > 0.55），所以 K* 升到 3； 0.70 阈值过严（1v2 AUC=0.696 < 0.70 对部分模型），所以 K* 降到 1。 T=1.2 条件下所有阈值的 K* 都系统性地高 1，反映其更强的代际信号。 关键发现：在论文推荐的 0.60 阈值下，K* 在所有标准解码条件下一致为 2，稳健。\n"
541	  },
542	  {
543	    "name": "Retrain-chain ecological validity",
544	    "description": "Pythia-1.4B LoRA retrain-chain vs prompt-chain, C4 5K docs, depth 0-4",
545	    "results": {
546	      "retrain_chain": {
547	        "k_star": 2,
548	        "pairwise_auc_0v1": 0.987,
549	        "pairwise_auc_1v2": 0.658,
550	        "pairwise_auc_2v3": 0.563,
551	        "pairwise_auc_3v4": 0.529,
552	        "pairwise_jsd_0v1": 0.231
553	      },
554	      "prompt_chain": {
555	        "k_star": 2,
556	        "pairwise_auc_0v1": 0.991,
557	        "pairwise_auc_1v2": 0.672,
558	        "pairwise_auc_2v3": 0.571,
559	        "pairwise_auc_3v4": 0.533
560	      },
561	      "kstar_diff": 0,
562	      "feature_distribution_jsd_retrain_vs_prompt": {
563	        "depth_0": 0.002,
564	        "depth_1": 0.018,
565	        "depth_2": 0.031,
566	        "depth_3": 0.042
567	      }
568	    },
569	    "tables": [
570	      {
571	        "caption": "Retrain-chain vs prompt-chain comparison (Pythia-1.4B)",
572	        "columns": [
573	          "depth_pair",
574	          "Retrain AUC",
575	          "Prompt AUC",
576	          "Δ AUC"
577	        ],
578	        "rows": [
579	          [
580	            "0v1",
581	            0.987,
582	            0.991,
583	            -0.004
584	          ],
585	          [
586	            "1v2",
587	            0.658,
588	            0.672,
589	            -0.014
590	          ],
591	          [
592	            "2v3",
593	            0.563,
594	            0.571,
595	            -0.008
596	          ],
597	          [
598	            "3v4",
599	            0.529,
600	            0.533,
601	            -0.004
602	          ]
603	        ]
604	      },
605	      {
606	        "caption": "Feature distribution divergence (retrain vs prompt)",
607	        "columns": [
608	          "depth",
609	          "JSD"
610	        ],
611	        "rows": [
612	          [
613	            0,
614	            0.002
615	          ],
616	          [
617	            1,
618	            0.018
619	          ],
620	          [
621	            2,
622	            0.031
623	          ],
624	          [
625	            3,
626	            0.042
627	          ]
628	        ]
629	      }
630	    ],
631	    "figures": [],
632	    "analysis": "K* diff=0 完美落入 best 档 [0,1]，直接验证假设 6。prompt-chain 作为 controlled proxy 的生态效度得到确认。审稿人关于\"prompt-chain 不代表真实递归污染\"的顾虑被有力回应。 Feature distribution JSD 随 depth 缓慢递增的模式也可报告为 supplementary finding。\n\n\nRetrain-chain（每代在前一代输出上 LoRA 微调后生成）比 prompt-chain 更接近真实世界的 model collapse 场景。但在 LoRA rank=16 / alpha=32 的轻量微调设置下， 模型权重的实际变化有限（LoRA 只修改了参数空间的低秩子空间）， 因此 retrain-chain 的输出分布与 prompt-chain 高度相似。 K* 一致为 2（diff=0，落入 best 档 [0,1]），因为 DPI 的约束是拓扑性的—— 只要信道是有损的（retrain 后仍是有损信道），收敛行为就保持。 但 retrain-chain 的 AUC 系统性地略低于 prompt-chain（Δ≈0.01-0.02）， 因为 LoRA 微调引入了微小的分布偏移使代际边界更模糊。 Feature distribution JSD 随 depth 递增——更深的代际中，retrain 和 prompt 的累积偏差更大， 但始终在可接受范围内（< 0.05），确认 prompt-chain 是 retrain-chain 的合理代理。\n"
633	  },
634	  {
635	    "name": "Contamination dose-response",
636	    "description": "10%/30%/50% synthetic injection, graduated vs binary filtering, MMLU+HellaSwag",
637	    "results": {
638	      "mmlu_delta_graduated_vs_binary": {
639	        "injection_10pct": 0.82,
640	        "injection_30pct": 2.24,
641	        "injection_50pct": 3.41
642	      },
643	      "hellaswag_delta_graduated_vs_binary": {
644	        "injection_10pct": 0.54,
645	        "injection_30pct": 2.07,
646	        "injection_50pct": 2.89
647	      },
648	      "graduated_advantage_trend": "monotonically increasing with injection rate"
649	    },
650	    "tables": [
651	      {
652	        "caption": "Dose-response: graduated vs binary Δ by contamination rate",
653	        "columns": [
654	          "injection_rate",
655	          "Δ_MMLU (pp)",
656	          "Δ_HellaSwag (pp)"
657	        ],
658	        "rows": [
659	          [
660	            "10%",
661	            0.82,
662	            0.54
663	          ],
664	          [
665	            "30%",
666	            2.24,
667	            2.07
668	          ],
669	          [
670	            "50%",
671	            3.41,
672	            2.89
673	          ]
674	        ]
675	      }
676	    ],
677	    "figures": [],
678	    "analysis": "单调递增的 dose-response 关系是 C3 的有力补充证据。在预计的 web-scale 污染率（30-50%）下， graduated filtering 的优势最为显著。这为 practical impact 叙事提供了直接支撑： \"随着合成文本在 web 数据中的比例持续增长，depth-aware curation 的价值只会越来越大。\"\n\n\n低污染率（10%）时，binary filtering 已经足够好——需要移除的合成文本少， 错分 gen-1 为\"全部合成\"的代价也小（因为总量少），所以 graduated 的边际收益有限（< 1pp）。 30% 污染率对应论文主实验（exp-006）条件，graduated 优势约 2pp。 50% 污染率时，binary filtering 的困境最大：半数数据是合成的，其中包含大量质量尚可的 gen-1， 全部移除导致训练数据量骤降，保留则引入大量 gen-2+ 噪声。graduated filtering 通过 \"保留 gen-1 降权 + 移除 gen-2+\"的策略在数据量和质量间取得更好平衡， 优势达到 ~3.4pp (MMLU) / ~2.9pp (HellaSwag)。 单调递增趋势证明 graduated filtering 的价值随污染严重程度而增加—— 即\"问题越严重，我们的方法越有价值\"，这是强有力的叙事。\n"
679	  },
680	  {
681	    "name": "Ordinal vs multinomial vs regression baseline",
682	    "description": "CORAL vs standard multiclass vs ordinal regression on depth classification",
683	    "results": {
684	      "coral_ordinal": {
685	        "accuracy": 0.483,
686	        "mae": 0.87,
687	        "adjacent_accuracy": 0.821
688	      },
689	      "multinomial": {
690	        "accuracy": 0.472,
691	        "mae": 1.03,
692	        "adjacent_accuracy": 0.784
693	      },
694	      "ordinal_regression": {
695	        "accuracy": 0.461,
696	        "mae": 0.91,
697	        "adjacent_accuracy": 0.808
698	      }
699	    },
700	    "tables": [
701	      {
702	        "caption": "Classifier architecture comparison",
703	        "columns": [
704	          "method",
705	          "accuracy",
706	          "MAE",
707	          "adjacent_acc"
708	        ],
709	        "rows": [
710	          [
711	            "CORAL (ordinal)",
712	            0.483,
713	            0.87,
714	            0.821
715	          ],
716	          [
717	            "multinomial",
718	            0.472,
719	            1.03,
720	            0.784
721	          ],
722	          [
723	            "ordinal regression",
724	            0.461,
725	            0.91,
726	            0.808
727	          ]
728	        ]
729	      }
730	    ],
731	    "figures": [],
732	    "analysis": "CORAL 在所有指标上最优，验证了 ordinal structure 的必要性。MAE 差异（0.87 vs 1.03） 对应下游 filtering 中每个错分导致的质量估计偏差，直接影响 graduated filtering 性能。 这为论文的方法论选择提供了消融实验支撑。\n\n\nDepth 具有天然的 ordinal 结构：gen-1 比 gen-3 更接近 gen-2，这种关系应被建模利用。 CORAL（Consistent Rank Logits）通过共享权重的累积概率建模天然适配 ordinal data， 在 MAE 上显著优于 multinomial（0.87 vs 1.03）——因为 multinomial 将 gen-1 和 gen-3 的 混淆视为与 gen-1 和 gen-2 的混淆同等严重，而 CORAL 的损失函数惩罚距离更远的错误。 Ordinal regression（proportional odds model）也利用了序数结构但参数化更受限（平行线假设）， 在 depth 数据的非等间距分布下表现略逊于 CORAL。 Accuracy 差异较小（因为所有模型都集中犯\"±1 depth 错误\"）， 但 MAE 和 adjacent accuracy 差异清晰地展示了 ordinal structure 的价值。\n"
733	  },
734	  {
735	    "name": "LLM zero-shot depth estimation",
736	    "description": "GPT-4o / Claude 3.5 zero-shot depth判断, depth 0-4, 200 samples per depth",
737	    "results": {
738	      "gpt4o": {
739	        "accuracy": 0.187,
740	        "mae": 1.82,
741	        "kendall_tau_with_true_depth": 0.11
742	      },
743	      "claude_3_5": {
744	        "accuracy": 0.203,
745	        "mae": 1.71,
746	        "kendall_tau_with_true_depth": 0.14
747	      },
748	      "human_baseline_estimated": {
749	        "accuracy": 0.162,
750	        "mae": 1.94
751	      }
752	    },
753	    "tables": [
754	      {
755	        "caption": "Zero-shot depth estimation by frontier LLMs",
756	        "columns": [
757	          "model",
758	          "accuracy",
759	          "MAE",
760	          "Kendall tau"
761	        ],
762	        "rows": [
763	          [
764	            "GPT-4o",
765	            0.187,
766	            1.82,
767	            0.11
768	          ],
769	          [
770	            "Claude 3.5 Sonnet",
771	            0.203,
772	            1.71,
773	            0.14
774	          ],
775	          [
776	            "Our ordinal classifier",
777	            0.483,
778	            0.87,
779	            0.52
780	          ]
781	        ]
782	      }
783	    ],
784	    "figures": [],
785	    "analysis": "LLM zero-shot 性能仅略高于 random chance (0.20 for 5-class)，而 ordinal classifier 是其 2.5 倍。这确立了 depth estimation 作为一个需要专门方法的 task—— 不能被 frontier LLM 的 general intelligence \"免费\"解决。强力支持论文的 problem formulation 贡献。\n\n\nLLM 的 zero-shot depth estimation 近乎随机，原因有三： (1) Depth 信号是统计性的（需要对比同一 domain 的多样本分布），单文本缺乏参照系； (2) LLM 未被训练理解\"递归生成导致的信息损失\"这一概念，其质量判断偏向 fluency 和 coherence， 而这些高层语义特征恰恰是最后才饱和的（与 C2 一致）——即使 gen-3 文本的 vocabulary diversity 已经严重退化，LLM 仍可能判定其\"写得不错\"因为它仍然 fluent； (3) Prompt 中无法有效传达\"相对于 seed 域的偏移\"信息。 Claude 略优于 GPT-4o 可能是偶然（差异在 noise range 内），也可能反映其对文本微妙质量差异的 slightly better calibration，但两者都远低于我们的 ordinal classifier（accuracy 0.48 vs 0.19）。 这个结果直接回应\"为什么不直接让 LLM 判断\"的审稿人问题。\n"
786	  },
787	  {
788	    "name": "Binary detector confidence as depth proxy",
789	    "description": "DivEye/Binoculars score 与 true depth 的 Spearman correlation",
790	    "results": {
791	      "diveye": {
792	        "spearman_rho": 0.23,
793	        "spearman_p_value": 0.001,
794	        "depth_discrimination_auc_0v1": 0.94,
795	        "depth_discrimination_auc_1v2": 0.53
796	      },
797	      "binoculars": {
798	        "spearman_rho": 0.19,
799	        "spearman_p_value": 0.003,
800	        "depth_discrimination_auc_0v1": 0.92,
801	        "depth_discrimination_auc_1v2": 0.51
802	      }
803	    },
804	    "tables": [
805	      {
806	        "caption": "Binary detector scores as depth proxy",
807	        "columns": [
808	          "detector",
809	          "Spearman ρ",
810	          "p-value",
811	          "AUC 0v1",
812	          "AUC 1v2"
813	        ],
814	        "rows": [
815	          [
816	            "DivEye",
817	            0.23,
818	            0.001,
819	            0.94,
820	            0.53
821	          ],
822	          [
823	            "Binoculars",
824	            0.19,
825	            0.003,
826	            0.92,
827	            0.51
828	          ],
829	          [
830	            "Our features (15D)",
831	            "-",
832	            "-",
833	            0.996,
834	            0.696
835	          ]
836	        ]
837	      }
838	    ],
839	    "figures": [],
840	    "analysis": "Binary detectors 在 0v1 分辨上强劲但在 1v2 上近乎 chance level， 直接证明\"binary detection ≠ depth estimation\"的核心论点。 这是论文 related work positioning 的关键数据点：现有方法解决的是不同的问题。\n\n\nBinary detectors 被优化为区分 human vs synthetic，其 confidence score 理论上与\"合成程度\"正相关。 但这种相关性极弱（ρ < 0.25），因为： (1) Binary detectors 的训练目标是最大化 real/synthetic 的决策边界，不是估计\"多 synthetic\"； (2) 它们的 score 在 gen-1 处已经几乎饱和（AUC_0v1 > 0.92）， 之后 gen-1 到 gen-5 的 score 差异被压缩到极窄的高 confidence 区间内—— 即\"所有合成文本都长得差不多 synthetic\"，无法区分代际； (3) Depth signal 是细粒度的分布特征偏移，而 binary detectors 用的 summary statistics （如 min-k% 概率）在 gen-1 之后就进入了平坦区。 Spearman ρ 显著但极弱，证明 binary confidence ≠ depth，binary 框架本质上不足以捕捉 ordinal structure。\n"
841	  },
842	  {
843	    "name": "Cross-model transfer",
844	    "description": "Model A 训练的 depth classifier 在 Model B 的 chain 上的 transfer accuracy",
845	    "results": {
846	      "transfer_matrix_accuracy": {
847	        "pythia_to_olmo": 0.364,
848	        "pythia_to_qwen": 0.371,
849	        "olmo_to_pythia": 0.352,
850	        "olmo_to_qwen": 0.358,
851	        "qwen_to_pythia": 0.387,
852	        "qwen_to_olmo": 0.374
853	      },
854	      "in_domain_accuracy": {
855	        "pythia": 0.401,
856	        "olmo": 0.388,
857	        "qwen": 0.418
858	      },
859	      "transfer_retention_pct": {
860	        "mean": 74.6,
861	        "min": 70.3,
862	        "max": 78.9
863	      },
864	      "transfer_ordinal_mae": {
865	        "mean": 1.14
866	      }
867	    },
868	    "tables": [
869	      {
870	        "caption": "Cross-model transfer accuracy matrix",
871	        "columns": [
872	          "train\\test",
873	          "Pythia",
874	          "OLMo",
875	          "Qwen",
876	          "mean_transfer"
877	        ],
878	        "rows": [
879	          [
880	            "Pythia",
881	            "0.401*",
882	            0.364,
883	            0.371,
884	            0.368
885	          ],
886	          [
887	            "OLMo",
888	            0.352,
889	            "0.388*",
890	            0.358,
891	            0.355
892	          ],
893	          [
894	            "Qwen",
895	            0.387,
896	            0.374,
897	            "0.418*",
898	            0.381
899	          ]
900	        ]
901	      },
902	      {
903	        "caption": "Transfer retention (%)",
904	        "columns": [
905	          "train→test",
906	          "retention %"
907	        ],
908	        "rows": [
909	          [
910	            "Pythia→OLMo",
911	            73.1
912	          ],
913	          [
914	            "Pythia→Qwen",
915	            74.2
916	          ],
917	          [
918	            "OLMo→Pythia",
919	            70.3
920	          ],
921	          [
922	            "OLMo→Qwen",
923	            71.5
924	          ],
925	          [
926	            "Qwen→Pythia",
927	            77.4
928	          ],
929	          [
930	            "Qwen→OLMo",
931	            78.9
932	          ]
933	        ]
934	      }
935	    ],
936	    "figures": [],
937	    "analysis": "Mean transfer retention 74.6% 落入 best 档 [70, 80]。这证明 depth signal 主要由 模型无关的语言统计量驱动，支持 C1 的\"信息论基本量\"叙事—— K* 不是某个特定模型的 artifact，而是递归信道的通用性质。 Qwen → others 最优暗示更强模型的 depth boundary 更 transferable。\n\n\nCross-model transfer 成功率反映了 depth signal 中\"模型无关成分\"的比例。 在 best 档下，transfer retention ≥70% 因为： (1) vocabulary diversity 特征（type-token ratio、hapax ratio）测量的是分布的通用统计性质， 不依赖于具体模型的 token 偏好——任何模型的递归生成都会收窄词汇分布； (2) surprisal dynamics 在 cross-model 设置下仍有 partial transfer， 因为虽然绝对 surprisal 值因模型而异，但相对变化模式（递归导致 surprisal 下降）是通用的； (3) 15D 特征中的 7-8 维是\"模型无关\"的，占特征预测力的大部分。 Qwen → others 的 transfer 最好（78.9%），因为 Qwen 作为最强模型学到的 decision boundary 更准确、更 general；OLMo → others 最差（70.3%），因为 1B 模型的信号更弱， 学到的 boundary 更 noisy。\n"
938	  },
939	  {
940	    "name": "Naturalistic validation (Common Crawl)",
941	    "description": "对 Common Crawl 2025/2026 snapshot 做 depth 预测，与 AlignScore 和 vocabulary richness correlation",
942	    "results": {
943	      "spearman_predicted_depth_vs_alignscore": -0.31,
944	      "spearman_predicted_depth_vs_vocab_richness": -0.37,
945	      "pct_samples_predicted_depth_geq_1": 18.4,
946	      "pct_samples_predicted_depth_geq_2": 7.2
947	    },
948	    "tables": [
949	      {
950	        "caption": "Naturalistic validation on Common Crawl",
951	        "columns": [
952	          "metric",
953	          "value"
954	        ],
955	        "rows": [
956	          [
957	            "Spearman(depth, AlignScore)",
958	            -0.31
959	          ],
960	          [
961	            "Spearman(depth, vocab richness)",
962	            -0.37
963	          ],
964	          [
965	            "% predicted depth≥1",
966	            "18.4%"
967	          ],
968	          [
969	            "% predicted depth≥2",
970	            "7.2%"
971	          ]
972	        ]
973	      }
974	    ],
975	    "figures": [],
976	    "analysis": "Naturalistic validation 提供了\"proof of concept\"级别的 wild-data 证据。 相关性中等偏弱但方向正确且显著，足以支持 appendix 或 discussion section 的 generalizability 论述。 不足以作为 main claim 但有效回应\"只在 controlled 设置下验证\"的审稿人顾虑。\n\n\nCommon Crawl 中的真实合成文本比例和代际深度无法获得 ground truth， 因此只能通过与外部质量指标的 correlation 间接验证。 Predicted depth 与 AlignScore（事实一致性指标）呈负相关（ρ≈-0.31）， 因为更深代际的文本事实偏差更大（递归\"电话游戏效应\"）。 与 vocabulary richness 的负相关更强（ρ≈-0.37），与 C2 一致：vocabulary diversity 是最先退化的特征。 ~18% 样本被预测为 depth≥1 与 2025-2026 时期 web 合成文本比例的外部估计（15-25%）一致。 depth≥2 仅 7.2%，但这正是 graduated filtering 最有价值的区间。 相关性不高是预期中的——wild data 的噪声、domain 多样性、unknown model 族都会稀释信号。\n"
977	  },
978	  {
979	    "name": "Learned representation baseline",
980	    "description": "Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features",
981	    "results": {
982	      "frozen_embeddings_mlp": {
983	        "accuracy": 0.452,
984	        "mae": 0.94,
985	        "training_time_gpu_hours": 2.8,
986	        "feature_dim": 4096
987	      },
988	      "handcrafted_15d": {
989	        "accuracy": 0.483,
990	        "mae": 0.87,
991	        "training_time_gpu_hours": 0.1,
992	        "feature_dim": 15
993	      }
994	    },
995	    "tables": [
996	      {
997	        "caption": "Learned vs hand-crafted features comparison",
998	        "columns": [
999	          "method",
1000	          "accuracy",
1001	          "MAE",
1002	          "dim",
1003	          "GPU hours"
1004	        ],
1005	        "rows": [
1006	          [
1007	            "frozen embeddings + MLP",
1008	            0.452,
1009	            0.94,
1010	            4096,
1011	            2.8
1012	          ],
1013	          [
1014	            "hand-crafted 15D",
1015	            0.483,
1016	            0.87,
1017	            15,
1018	            0.1
1019	          ]
1020	        ]
1021	      }
1022	    ],
1023	    "figures": [],
1024	    "analysis": "Hand-crafted features 在所有指标上优于或持平 frozen embeddings，且维度低 270 倍、训练快 28 倍。 这验证了论文\"选择 interpretable features 不是妥协而是优势\"的叙事， 回应审稿人\"为什么不用 learned representations\"的问题。\n\n\nFrozen embeddings 包含丰富的语义信息但存在两个劣势： (1) 4096 维中大部分编码的是内容语义（topic、entity）而非递归退化信号， MLP 需要从高维空间中\"挖掘\"少数相关维度，在 5K 样本量下容易过拟合； (2) Frozen embeddings 来自同一模型（Qwen2.5-1.5B），引入了自我参照偏差—— 模型对自己生成的文本的 embedding 可能有系统性偏向， 但这种偏向在 cross-model 设置下不 transfer。 Hand-crafted 15D features 虽然维度低，但每个特征都直接编码了与递归退化相关的统计量 （diversity、surprisal、tail weight），特征工程的人类先验弥补了维度不足。 更重要的是，15D 特征支持 degradation ordering 分析（C2）和 feature group ablation（exp-005）， 这是 frozen embeddings 无法提供的。 Hand-crafted 优于 frozen 的幅度不大（accuracy +3.1pp），但 interpretability 和 efficiency 优势明显。\n"
1025	  },
1026	  {
1027	    "name": "Base vs Instruct model comparison",
1028	    "description": "Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异",
1029	    "results": {
1030	      "base": {
1031	        "k_star": 2,
1032	        "pairwise_auc_0v1": 0.993,
1033	        "pairwise_auc_1v2": 0.714,
1034	        "pairwise_auc_2v3": 0.598,
1035	        "pairwise_jsd_0v1": 0.289
1036	      },
1037	      "instruct": {
1038	        "k_star": 2,
1039	        "pairwise_auc_0v1": 0.996,
1040	        "pairwise_auc_1v2": 0.696,
1041	        "pairwise_auc_2v3": 0.589,
1042	        "pairwise_jsd_0v1": 0.267
1043	      },
1044	      "base_vs_instruct_auc_1v2_diff": 0.018,
1045	      "base_vs_instruct_feature_divergence": {
1046	        "surprisal_mean_shift": -0.12,
1047	        "vocab_diversity_shift": 0.04
1048	      }
1049	    },
1050	    "tables": [
1051	      {
1052	        "caption": "Base vs Instruct comparison (Qwen2.5-1.5B)",
1053	        "columns": [
1054	          "variant",
1055	          "K*",
1056	          "AUC_0v1",
1057	          "AUC_1v2",
1058	          "AUC_2v3",
1059	          "JSD_0v1"
1060	        ],
1061	        "rows": [
1062	          [
1063	            "base",
1064	            2,
1065	            0.993,
1066	            0.714,
1067	            0.598,
1068	            0.289
1069	          ],
1070	          [
1071	            "instruct (MVP)",
1072	            2,
1073	            0.996,
1074	            0.696,
1075	            0.589,
1076	            0.267
1077	          ]
1078	        ]
1079	      }
1080	    ],
1081	    "figures": [],
1082	    "analysis": "Base model 信号略强但 K* 不变，表明 RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这个结果对实际应用有意义：野外数据可能来自 base 或 instruct model， K*=2 在两种设置下都成立意味着 graduated filtering 框架对两者都适用。\n\nBase model 的 depth signal 略强于 Instruct（AUC_1v2: 0.714 vs 0.696），原因： Instruct 微调（RLHF/DPO）将模型输出拉向\"人类偏好的模式\"——更规范的句式、更安全的措辞、 更集中的 vocabulary 选择。这种 alignment 相当于对输出分布施加了额外约束， 使得即使是 gen-0（human text passed through instruct model）也已经部分\"标准化\"了。 因此 instruct 模型的递归代际间差异更小——每代输出都被拉向同一个\"preferred mode\"。 但 K* 仍为 2，因为 alignment 的影响是 quantitative（减弱信号）而非 qualitative（改变收敛行为）。 Surprisal mean shift 为负（instruct 的 surprisal 更低），反映其输出更\"可预测\"； vocab diversity shift 为正（instruct 的词汇稍微更多样），反映 RLHF 鼓励的表达多样性。 这些差异小但方向一致，为 discussion 中关于\"检测 instruct model 输出\"的段落提供数据。\n"
1083	  }
1084	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3486cdc-3fdf-47e0-ad08-0b590f3d5db6",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "8e556c53-aee5-4f15-8bd5-f9785365fafc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Pythia-1.4B depth chain generation\",\n    \"description\": \"Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.991,\n      \"pairwise_auc_1v2\": 0.672,\n      \"pairwise_auc_2v3\": 0.571,\n      \"pairwise_auc_3v4\": 0.533,\n      \"pairwise_auc_4v5\": 0.521,\n      \"pairwise_jsd_0v1\": 0.243,\n      \"pairwise_jsd_1v2\": 0.014,\n      \"pairwise_jsd_2v3\": 0.005,\n      \"pairwise_jsd_3v4\": 0.003,\n      \"pairwise_jsd_4v5\": 0.002,\n      \"k_star\": 2,\n      \"ordinal_accuracy\": 0.401,\n      \"ordinal_mae\": 1.08\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Pythia-1.4B pairwise discrimination across depths\",\n        \"columns\": [\n          \"depth_pair\",\n          \"AUC_mean\",\n          \"AUC_std\",\n          \"JSD\"\n        ],\n        \"rows\": [\n          [\n            \"0v1\",\n            0.991,\n            0.001,\n            0.243\n          ],\n          [\n            \"1v2\",\n            0.672,\n            0.008,\n            0.014\n          ],\n          [\n            \"2v3\",\n            0.571,\n            0.011,\n            0.005\n          ],\n          [\n            \"3v4\",\n            0.533,\n            0.006,\n            0.003\n          ],\n          [\n            \"4v5\",\n            0.521,\n            0.009,\n            0.002\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pythia 确认 1.5B 规模下 K*=2 的鲁棒性。1v2 AUC=0.672 落入 best 档 [0.65, 0.75] 范围。 与 MVP 的差异（Δ AUC_1v2 = -0.024）方向符合预期：更弱的预训练基础 → 更浅的代际信号。 这支持 C1：K* 是模型能力的函数而非固定常数。\\n\\n\\nPythia-1.4B 与 MVP 的 Qwen2.5-1.5B 参数规模相近但架构更旧（GPT-NeoX 基础）， 预训练数据量和质量略逊于 Qwen2.5。因此 0v1 AUC 仍极高（递归首代信息损失显著）， 但 1v2 AUC 略低于 Qwen（0.672 vs 0.696），因为 Pythia 生成质量本身更低， 递归代际间的边际信息损失更小——即\\\"起点已经更差，所以每代退化的增量更不明显\\\"。 K* 仍为 2，因为在 1.5B 规模 + 标准解码下，DPI 决定的信息瓶颈位置一致。 JSD 衰减模式与 MVP 高度一致（0v1 远大于后续），验证跨模型的 DPI 收敛规律。\\n\"\n  },\n  {\n    \"name\": \"OLMo-1B depth chain generation\",\n    \"description\": \"OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.988,\n      \"pairwise_auc_1v2\": 0.654,\n      \"pairwise_auc_2v3\": 0.558,\n      \"pairwise_auc_3v4\": 0.527,\n      \"pairwise_auc_4v5\": 0.515,\n      \"pairwise_jsd_0v1\": 0.221,\n      \"pairwise_jsd_1v2\": 0.012,\n      \"pairwise_jsd_2v3\": 0.004,\n      \"pairwise_jsd_3v4\": 0.003,\n      \"pairwise_jsd_4v5\": 0.002,\n      \"k_star\": 2,\n      \"ordinal_accuracy\": 0.388,\n      \"ordinal_mae\": 1.12\n    },\n    \"tables\": [\n      {\n        \"caption\": \"OLMo-1B pairwise discrimination across depths\",\n        \"columns\": [\n          \"depth_pair\",\n          \"AUC_mean\",\n          \"AUC_std\",\n          \"JSD\"\n        ],\n        \"rows\": [\n          [\n            \"0v1\",\n            0.988,\n            0.001,\n            0.221\n          ],\n          [\n            \"1v2\",\n            0.654,\n            0.009,\n            0.012\n          ],\n          [\n            \"2v3\",\n            0.558,\n            0.013,\n            0.004\n          ],\n          [\n            \"3v4\",\n            0.527,\n            0.007,\n            0.003\n          ],\n          [\n            \"4v5\",\n            0.515,\n            0.01,\n            0.002\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OLMo 作为最小模型提供了 scale 连续体的下端锚点。1v2 AUC=0.654 恰在 best 档下限， 表明 1B 级是当前实验设置下 depth signal 的近似下界。三模型一致的 K*=2 强力支持 C1：K* 在 1-1.5B 规模下是信息论约束的稳健结果，而非某个模型的 artifact。\\n\\n\\nOLMo-1B 参数量最小（1B vs 1.4-1.5B），且 OLMo 的 Dolma 预训练数据虽公开透明但 多样性略低于 Qwen 的预训练混合。更小的模型容量意味着单次生成的信息保持率更低， 因此 0v1 JSD 略低（起始分布差异稍小）。但关键是 1v2 AUC=0.654 仍在 best 档下限附近， K* 仍为 2——DPI 理论预测的收敛行为不依赖于具体架构细节，只依赖于信道容量， 而 1B 级模型的信道容量与 1.5B 级处于同一量级。ordinal 性能略低因信号更弱。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-1.5B decoding strategy ablation\",\n    \"description\": \"Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs, depth 0-5\",\n    \"results\": {\n      \"greedy\": {\n        \"k_star\": 2,\n        \"pairwise_auc_1v2\": 0.651,\n        \"pairwise_auc_2v3\": 0.554,\n        \"pairwise_jsd_0v1\": 0.234\n      },\n      \"nucleus_p0.9\": {\n        \"k_star\": 2,\n        \"pairwise_auc_1v2\": 0.688,\n        \"pairwise_auc_2v3\": 0.582,\n        \"pairwise_jsd_0v1\": 0.259\n      },\n      \"temp_0.7\": {\n        \"k_star\": 2,\n        \"pairwise_auc_1v2\": 0.668,\n        \"pairwise_auc_2v3\": 0.563,\n        \"pairwise_jsd_0v1\": 0.241\n      },\n      \"temp_1.2\": {\n        \"k_star\": 3,\n        \"pairwise_auc_1v2\": 0.723,\n        \"pairwise_auc_2v3\": 0.648,\n        \"pairwise_auc_3v4\": 0.574,\n        \"pairwise_auc_4v5\": 0.531,\n        \"pairwise_jsd_0v1\": 0.312,\n        \"pairwise_jsd_1v2\": 0.028,\n        \"pairwise_jsd_2v3\": 0.011,\n        \"pairwise_jsd_3v4\": 0.005\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Decoding strategy ablation: K* and key pairwise AUCs\",\n        \"columns\": [\n          \"decoding\",\n          \"K*\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"AUC_3v4\",\n          \"JSD_0v1\"\n        ],\n        \"rows\": [\n          [\n            \"greedy\",\n            2,\n            0.993,\n            0.651,\n            0.554,\n            0.526,\n            0.234\n          ],\n          [\n            \"nucleus p=0.9\",\n            2,\n            0.994,\n            0.688,\n            0.582,\n            0.538,\n            0.259\n          ],\n          [\n            \"T=0.7\",\n            2,\n            0.993,\n            0.668,\n            0.563,\n            0.53,\n            0.241\n          ],\n          [\n            \"T=1.2\",\n            3,\n            0.997,\n            0.723,\n            0.648,\n            0.574,\n            0.312\n          ],\n          [\n            \"MVP (p=0.95 T=1.0)\",\n            2,\n            0.996,\n            0.696,\n            0.589,\n            0.543,\n            0.267\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是论文的核心实验之一。T=1.2 → K*=3 直接证明 K* 是可调控的，消解\\\"K*=2 太浅\\\"的审稿人顾虑。 解码策略形成清晰的 K* 调控梯度：greedy ≤ low-temp ≤ standard nucleus ≤ high-temp。 这为 C1 提供了因果方向性证据：不是分类器能力限制了 K*，而是信道特性决定了 K*。\\n\\n\\n解码策略通过控制 generation entropy 直接调控信道的有效容量。 Greedy 解码（T→0）将输出限制在最高概率 token，递归代际间差异被压缩到很窄的 mode 附近， 导致 1v2 AUC 最低——信息损失在首代就已经高度集中，后续代际几乎无额外损失可测。 T=0.7 和 nucleus p=0.9 居于中间：适度随机性保留了更多分布结构供后续代际逐步丢失。 T=1.2 是关键条件：高温度扩大了 token 采样空间，使得每代生成引入更多\\\"非主流\\\"token 选择， 这些选择在递归中被逐步\\\"洗掉\\\"——但因为起始多样性更高，这个洗掉过程需要更多代际才能饱和。 信息论解释：高温度提高了初始互信息 I(X;Y₁)，DPI 保证 I(X;Yₖ) 单调递减， 但更高的起点意味着降到阈值需要更多步——因此 K* 从 2 升到 3。 这直接验证核心假设 1，且 2v3 AUC=0.648 落入 best 档 [0.62, 0.70]。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-7B cross-scale probe\",\n    \"description\": \"Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.998,\n      \"pairwise_auc_1v2\": 0.741,\n      \"pairwise_auc_2v3\": 0.662,\n      \"pairwise_jsd_0v1\": 0.341,\n      \"pairwise_jsd_1v2\": 0.032,\n      \"pairwise_jsd_2v3\": 0.013,\n      \"k_star\": 3,\n      \"ordinal_accuracy\": 0.518,\n      \"ordinal_mae\": 0.81\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Qwen2.5-7B vs 1.5B pairwise discrimination comparison\",\n        \"columns\": [\n          \"depth_pair\",\n          \"7B_AUC\",\n          \"7B_JSD\",\n          \"1.5B_AUC (MVP)\",\n          \"1.5B_JSD (MVP)\"\n        ],\n        \"rows\": [\n          [\n            \"0v1\",\n            0.998,\n            0.341,\n            0.996,\n            0.267\n          ],\n          [\n            \"1v2\",\n            0.741,\n            0.032,\n            0.696,\n            0.016\n          ],\n          [\n            \"2v3\",\n            0.662,\n            0.013,\n            0.589,\n            0.007\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 实验确认核心假设 2：模型规模是 K* 的杠杆。K*=3 且 ordinal accuracy=0.518 证明更大模型在标准解码下就能支持更细粒度的 depth estimation。 结合 exp-003 (T=1.2 → K*=3)，两条独立路径都能将 K* 推到 3， 彻底消解\\\"K*=2 是天花板\\\"的叙事风险。对 EMNLP 审稿人的回应： \\\"K*=2 is not a ceiling but a floor that rises with model scale and decoding entropy.\\\"\\n\\n\\n7B 模型的关键优势是更大的参数空间编码了更丰富的语言分布。递归生成时， 每代输出保留了更多原始分布的细微结构（rare n-grams、长距离依赖、discourse patterns）， 因此代际间的信息损失更\\\"均匀地分散\\\"到更多代际中，而不是在前两代就急剧塌缩。 具体机制：7B 模型的 next-token 分布具有更长的\\\"有意义尾巴\\\"（tail tokens 仍携带语义信息）， 递归第二代仍能保留这些尾巴 token 的部分分布特征，到第三代才显著丢失—— 因此 2v3 AUC=0.662 仍远高于机会水平，K* 达到 3。 这与 1.5B 级（K*=2）形成鲜明对比，建立了 scale → K* 的因果关系。 ordinal_accuracy=0.518 和 mae=0.81 均落入 best 档最优区间，因为更丰富的代际信号 使 ordinal classifier 有更多可利用的特征梯度。 注意 1K docs（vs 5K）引入更大方差，但 7B 的信号强度弥补了样本量不足。\\n\"\n  },\n  {\n    \"name\": \"Feature group ablation + degradation ordering\",\n    \"description\": \"对每个模型的 depth chain，按 feature group 分析饱和深度和 degradation ordering\",\n    \"results\": {\n      \"saturation_depth_vocabulary_diversity\": {\n        \"pythia_1.4b\": 1,\n        \"olmo_1b\": 1,\n        \"qwen_1.5b\": 1\n      },\n      \"saturation_depth_surprisal_dynamics\": {\n        \"pythia_1.4b\": 2,\n        \"olmo_1b\": 2,\n        \"qwen_1.5b\": 2\n      },\n      \"saturation_depth_tail_thinning\": {\n        \"pythia_1.4b\": 2,\n        \"olmo_1b\": 1,\n        \"qwen_1.5b\": 2\n      },\n      \"degradation_ordering_kendall_tau\": {\n        \"pythia_vs_qwen\": 0.87,\n        \"olmo_vs_qwen\": 0.82,\n        \"pythia_vs_olmo\": 0.84,\n        \"mean\": 0.84\n      },\n      \"feature_group_auc_at_depth1\": {\n        \"vocabulary_diversity\": 0.612,\n        \"surprisal_dynamics\": 0.693,\n        \"tail_thinning\": 0.641\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Feature group saturation depth by model\",\n        \"columns\": [\n          \"feature_group\",\n          \"Pythia-1.4B\",\n          \"OLMo-1B\",\n          \"Qwen2.5-1.5B\"\n        ],\n        \"rows\": [\n          [\n            \"vocabulary_diversity\",\n            1,\n            1,\n            1\n          ],\n          [\n            \"surprisal_dynamics\",\n            2,\n            2,\n            2\n          ],\n          [\n            \"tail_thinning\",\n            2,\n            1,\n            2\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Cross-model degradation ordering consistency (Kendall tau)\",\n        \"columns\": [\n          \"model_pair\",\n          \"tau\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia vs Qwen\",\n            0.87\n          ],\n          [\n            \"OLMo vs Qwen\",\n            0.82\n          ],\n          [\n            \"Pythia vs OLMo\",\n            0.84\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Kendall tau 均值 0.84 落入 best 档 [0.8, 1.0]。vocabulary diversity 一致在 depth=1 饱和 而 surprisal dynamics 在 depth=2 饱和，这为 C2 提供了直接证据。 OLMo 的 tail-thinning 在 depth=1 就饱和（vs 其他模型的 depth=2）是因为 1B 模型 本身的 tail 更薄，可在 discussion 中讨论。ordering 的跨模型一致性表明这是 递归生成的结构性规律而非模型特异现象。\\n\\n\\nDPI 约束下，不同语言特征编码的互信息量不同，因此对递归损失的敏感度不同。 Vocabulary diversity（type-token ratio、hapax ratio 等）依赖于 token 分布的尾部—— 递归生成首先\\\"修剪\\\"低频 token（因为模型倾向于生成高概率 token）， 导致 vocabulary diversity 在 depth=1 就显著下降并迅速饱和。 Surprisal dynamics（mean surprisal、surprisal variance、auto-MI）编码的是序列级分布结构， 这种高阶统计量需要更多代际的累积损失才会饱和——因为即使 token 频率分布已经变窄， token 间的条件依赖结构仍然部分保持。 Tail-thinning 特征居于中间：它捕捉分布尾部的厚度，与 vocabulary diversity 相关但更稳健。 三个模型族的 ordering 高度一致（Kendall tau ≥ 0.82），因为这个 ordering 反映的是 信息论的结构性规律（边际统计量先于条件统计量饱和），而非特定模型的 artifact。\\n\"\n  },\n  {\n    \"name\": \"Downstream filtering evaluation\",\n    \"description\": \"Qwen2.5-1.5B depth chain, no-filter / binary / graduated / surprisal-based, 3 seeds, MMLU+HellaSwag\",\n    \"results\": {\n      \"mmlu_pp\": {\n        \"no_filter\": 25.31,\n        \"binary\": 26.18,\n        \"graduated\": 28.42,\n        \"surprisal_based\": 27.89\n      },\n      \"hellaswag_pp\": {\n        \"no_filter\": 42.67,\n        \"binary\": 43.54,\n        \"graduated\": 45.61,\n        \"surprisal_based\": 45.12\n      },\n      \"mmlu_std_across_seeds\": {\n        \"no_filter\": 0.23,\n        \"binary\": 0.31,\n        \"graduated\": 0.28,\n        \"surprisal_based\": 0.35\n      },\n      \"hellaswag_std_across_seeds\": {\n        \"no_filter\": 0.19,\n        \"binary\": 0.25,\n        \"graduated\": 0.22,\n        \"surprisal_based\": 0.29\n      },\n      \"graduated_vs_binary_delta_mmlu_pp\": 2.24,\n      \"graduated_vs_binary_delta_hellaswag_pp\": 2.07,\n      \"graduated_vs_binary_p_value_mmlu\": 0.008,\n      \"graduated_vs_binary_p_value_hellaswag\": 0.013\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Downstream evaluation: continued pretraining perplexity and benchmark performance\",\n        \"columns\": [\n          \"strategy\",\n          \"MMLU (pp)\",\n          \"MMLU_std\",\n          \"HellaSwag (pp)\",\n          \"HS_std\"\n        ],\n        \"rows\": [\n          [\n            \"no-filter\",\n            25.31,\n            0.23,\n            42.67,\n            0.19\n          ],\n          [\n            \"binary\",\n            26.18,\n            0.31,\n            43.54,\n            0.25\n          ],\n          [\n            \"graduated (3-class)\",\n            28.42,\n            0.28,\n            45.61,\n            0.22\n          ],\n          [\n            \"surprisal-based\",\n            27.89,\n            0.35,\n            45.12,\n            0.29\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Statistical significance: graduated vs binary (paired t-test, 3 seeds)\",\n        \"columns\": [\n          \"benchmark\",\n          \"Δ (pp)\",\n          \"p-value\",\n          \"significant\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            2.24,\n            0.008,\n            \"yes\"\n          ],\n          [\n            \"HellaSwag\",\n            2.07,\n            0.013,\n            \"yes\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"graduated vs binary Δ=2.24pp (MMLU) 和 2.07pp (HellaSwag) 均落入 best 档范围 [1.5, 3.5] / [1.0, 3.0]。 p < 0.05 跨 3 seeds 确认 C3 成立。graduated 的优势来源明确：对 gen-1 的精细化处理。 surprisal-based 的存在证明即使单一特征也优于 binary，但多维 ordinal signal 更优。\\n\\n\\nBinary filtering 将所有合成文本等同对待——保留或移除。但 gen-1 文本质量远高于 gen-3+， binary 策略要么丢掉高质量的 gen-1（过滤过严 → 损失有用数据）要么保留低质量的 gen-3+（过滤过松 → 引入噪声）。 Graduated filtering 利用 3-class ordinal signal（human / gen-1 / gen-2+）在阈值附近做更精细的决策： 对 gen-1 降权但不完全移除（因为它仍包含大部分原始信息），对 gen-2+ 移除（因为已过 K*）。 这种\\\"软阈值\\\"效应在 binary 策略的 precision-recall 权衡最痛苦的区间（gen-1 附近） 提供了 1.5-3.5 个百分点的改善。MMLU 收益（+2.24pp）略高于 HellaSwag（+2.07pp）， 因为 MMLU 对知识密度更敏感——graduated filtering 保留的 gen-1 中知识保真度高于 binary 移除后的缺失。 Surprisal-based 策略也优于 binary 但不及 graduated，因为它只用单一特征维度做决策， 而 graduated 利用了 ordinal classifier 融合的多维信号。 3 seeds 的 std 均 < 0.35pp，p 值 < 0.05，确认统计显著性。\\n\"\n  },\n  {\n    \"name\": \"K* sensitivity analysis\",\n    \"description\": \"在 AUC 阈值 0.55/0.60/0.65/0.70 下计算 K*，展示稳健性\",\n    \"results\": {\n      \"qwen_1.5b_mvp\": {\n        \"threshold_0.55\": 3,\n        \"threshold_0.60\": 2,\n        \"threshold_0.65\": 2,\n        \"threshold_0.70\": 1\n      },\n      \"pythia_1.4b\": {\n        \"threshold_0.55\": 3,\n        \"threshold_0.60\": 2,\n        \"threshold_0.65\": 2,\n        \"threshold_0.70\": 1\n      },\n      \"olmo_1b\": {\n        \"threshold_0.55\": 2,\n        \"threshold_0.60\": 2,\n        \"threshold_0.65\": 2,\n        \"threshold_0.70\": 1\n      },\n      \"qwen_1.5b_temp_1.2\": {\n        \"threshold_0.55\": 4,\n        \"threshold_0.60\": 3,\n        \"threshold_0.65\": 3,\n        \"threshold_0.70\": 2\n      },\n      \"k_star_stability_within_0.60_0.65\": \"all models K*=2, perfectly stable\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"K* sensitivity to AUC threshold\",\n        \"columns\": [\n          \"model_condition\",\n          \"θ=0.55\",\n          \"θ=0.60\",\n          \"θ=0.65\",\n          \"θ=0.70\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-1.5B (p=0.95,T=1.0)\",\n            3,\n            2,\n            2,\n            1\n          ],\n          [\n            \"Pythia-1.4B (p=0.95,T=1.0)\",\n            3,\n            2,\n            2,\n            1\n          ],\n          [\n            \"OLMo-1B (p=0.95,T=1.0)\",\n            2,\n            2,\n            2,\n            1\n          ],\n          [\n            \"Qwen2.5-1.5B (T=1.2)\",\n            4,\n            3,\n            3,\n            2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"K* 在 θ∈[0.60, 0.65] 的\\\"合理区间\\\"内完全稳定，消解了\\\"K* 是阈值选择的 artifact\\\"的顾虑。 θ=0.60 作为默认推荐有理论支撑（显著高于 0.5 chance level）和实证支撑（稳定区间中心）。 T=1.2 条件的系统性偏移进一步证实 K* 的调控效应是真实的而非阈值敏感的幻觉。\\n\\n\\nK* 本质是\\\"pairwise AUC 首次低于阈值的 depth\\\"，因此它对阈值有阶跃依赖。 但在合理的阈值范围内（0.60-0.65，即\\\"明显高于 chance 但不要求 near-perfect\\\"）， K* 应当稳定。原因：MVP 数据显示 AUC 从 1v2 (0.696) 到 2v3 (0.589) 有显著跳跃， 这意味着任何落在 0.589-0.696 之间的阈值都会给出同一个 K*=2。 0.55 阈值过松（2v3 AUC=0.589 > 0.55），所以 K* 升到 3； 0.70 阈值过严（1v2 AUC=0.696 < 0.70 对部分模型），所以 K* 降到 1。 T=1.2 条件下所有阈值的 K* 都系统性地高 1，反映其更强的代际信号。 关键发现：在论文推荐的 0.60 阈值下，K* 在所有标准解码条件下一致为 2，稳健。\\n\"\n  },\n  {\n    \"name\": \"Retrain-chain ecological validity\",\n    \"description\": \"Pythia-1.4B LoRA retrain-chain vs prompt-chain, C4 5K docs, depth 0-4\",\n    \"results\": {\n      \"retrain_chain\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.987,\n        \"pairwise_auc_1v2\": 0.658,\n        \"pairwise_auc_2v3\": 0.563,\n        \"pairwise_auc_3v4\": 0.529,\n        \"pairwise_jsd_0v1\": 0.231\n      },\n      \"prompt_chain\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.991,\n        \"pairwise_auc_1v2\": 0.672,\n        \"pairwise_auc_2v3\": 0.571,\n        \"pairwise_auc_3v4\": 0.533\n      },\n      \"kstar_diff\": 0,\n      \"feature_distribution_jsd_retrain_vs_prompt\": {\n        \"depth_0\": 0.002,\n        \"depth_1\": 0.018,\n        \"depth_2\": 0.031,\n        \"depth_3\": 0.042\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Retrain-chain vs prompt-chain comparison (Pythia-1.4B)\",\n        \"columns\": [\n          \"depth_pair\",\n          \"Retrain AUC\",\n          \"Prompt AUC\",\n          \"Δ AUC\"\n        ],\n        \"rows\": [\n          [\n            \"0v1\",\n            0.987,\n            0.991,\n            -0.004\n          ],\n          [\n            \"1v2\",\n            0.658,\n            0.672,\n            -0.014\n          ],\n          [\n            \"2v3\",\n            0.563,\n            0.571,\n            -0.008\n          ],\n          [\n            \"3v4\",\n            0.529,\n            0.533,\n            -0.004\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Feature distribution divergence (retrain vs prompt)\",\n        \"columns\": [\n          \"depth\",\n          \"JSD\"\n        ],\n        \"rows\": [\n          [\n            0,\n            0.002\n          ],\n          [\n            1,\n            0.018\n          ],\n          [\n            2,\n            0.031\n          ],\n          [\n            3,\n            0.042\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"K* diff=0 完美落入 best 档 [0,1]，直接验证假设 6。prompt-chain 作为 controlled proxy 的生态效度得到确认。审稿人关于\\\"prompt-chain 不代表真实递归污染\\\"的顾虑被有力回应。 Feature distribution JSD 随 depth 缓慢递增的模式也可报告为 supplementary finding。\\n\\n\\nRetrain-chain（每代在前一代输出上 LoRA 微调后生成）比 prompt-chain 更接近真实世界的 model collapse 场景。但在 LoRA rank=16 / alpha=32 的轻量微调设置下， 模型权重的实际变化有限（LoRA 只修改了参数空间的低秩子空间）， 因此 retrain-chain 的输出分布与 prompt-chain 高度相似。 K* 一致为 2（diff=0，落入 best 档 [0,1]），因为 DPI 的约束是拓扑性的—— 只要信道是有损的（retrain 后仍是有损信道），收敛行为就保持。 但 retrain-chain 的 AUC 系统性地略低于 prompt-chain（Δ≈0.01-0.02）， 因为 LoRA 微调引入了微小的分布偏移使代际边界更模糊。 Feature distribution JSD 随 depth 递增——更深的代际中，retrain 和 prompt 的累积偏差更大， 但始终在可接受范围内（< 0.05），确认 prompt-chain 是 retrain-chain 的合理代理。\\n\"\n  },\n  {\n    \"name\": \"Contamination dose-response\",\n    \"description\": \"10%/30%/50% synthetic injection, graduated vs binary filtering, MMLU+HellaSwag\",\n    \"results\": {\n      \"mmlu_delta_graduated_vs_binary\": {\n        \"injection_10pct\": 0.82,\n        \"injection_30pct\": 2.24,\n        \"injection_50pct\": 3.41\n      },\n      \"hellaswag_delta_graduated_vs_binary\": {\n        \"injection_10pct\": 0.54,\n        \"injection_30pct\": 2.07,\n        \"injection_50pct\": 2.89\n      },\n      \"graduated_advantage_trend\": \"monotonically increasing with injection rate\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Dose-response: graduated vs binary Δ by contamination rate\",\n        \"columns\": [\n          \"injection_rate\",\n          \"Δ_MMLU (pp)\",\n          \"Δ_HellaSwag (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"10%\",\n            0.82,\n            0.54\n          ],\n          [\n            \"30%\",\n            2.24,\n            2.07\n          ],\n          [\n            \"50%\",\n            3.41,\n            2.89\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"单调递增的 dose-response 关系是 C3 的有力补充证据。在预计的 web-scale 污染率（30-50%）下， graduated filtering 的优势最为显著。这为 practical impact 叙事提供了直接支撑： \\\"随着合成文本在 web 数据中的比例持续增长，depth-aware curation 的价值只会越来越大。\\\"\\n\\n\\n低污染率（10%）时，binary filtering 已经足够好——需要移除的合成文本少， 错分 gen-1 为\\\"全部合成\\\"的代价也小（因为总量少），所以 graduated 的边际收益有限（< 1pp）。 30% 污染率对应论文主实验（exp-006）条件，graduated 优势约 2pp。 50% 污染率时，binary filtering 的困境最大：半数数据是合成的，其中包含大量质量尚可的 gen-1， 全部移除导致训练数据量骤降，保留则引入大量 gen-2+ 噪声。graduated filtering 通过 \\\"保留 gen-1 降权 + 移除 gen-2+\\\"的策略在数据量和质量间取得更好平衡， 优势达到 ~3.4pp (MMLU) / ~2.9pp (HellaSwag)。 单调递增趋势证明 graduated filtering 的价值随污染严重程度而增加—— 即\\\"问题越严重，我们的方法越有价值\\\"，这是强有力的叙事。\\n\"\n  },\n  {\n    \"name\": \"Ordinal vs multinomial vs regression baseline\",\n    \"description\": \"CORAL vs standard multiclass vs ordinal regression on depth classification\",\n    \"results\": {\n      \"coral_ordinal\": {\n        \"accuracy\": 0.483,\n        \"mae\": 0.87,\n        \"adjacent_accuracy\": 0.821\n      },\n      \"multinomial\": {\n        \"accuracy\": 0.472,\n        \"mae\": 1.03,\n        \"adjacent_accuracy\": 0.784\n      },\n      \"ordinal_regression\": {\n        \"accuracy\": 0.461,\n        \"mae\": 0.91,\n        \"adjacent_accuracy\": 0.808\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Classifier architecture comparison\",\n        \"columns\": [\n          \"method\",\n          \"accuracy\",\n          \"MAE\",\n          \"adjacent_acc\"\n        ],\n        \"rows\": [\n          [\n            \"CORAL (ordinal)\",\n            0.483,\n            0.87,\n            0.821\n          ],\n          [\n            \"multinomial\",\n            0.472,\n            1.03,\n            0.784\n          ],\n          [\n            \"ordinal regression\",\n            0.461,\n            0.91,\n            0.808\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CORAL 在所有指标上最优，验证了 ordinal structure 的必要性。MAE 差异（0.87 vs 1.03） 对应下游 filtering 中每个错分导致的质量估计偏差，直接影响 graduated filtering 性能。 这为论文的方法论选择提供了消融实验支撑。\\n\\n\\nDepth 具有天然的 ordinal 结构：gen-1 比 gen-3 更接近 gen-2，这种关系应被建模利用。 CORAL（Consistent Rank Logits）通过共享权重的累积概率建模天然适配 ordinal data， 在 MAE 上显著优于 multinomial（0.87 vs 1.03）——因为 multinomial 将 gen-1 和 gen-3 的 混淆视为与 gen-1 和 gen-2 的混淆同等严重，而 CORAL 的损失函数惩罚距离更远的错误。 Ordinal regression（proportional odds model）也利用了序数结构但参数化更受限（平行线假设）， 在 depth 数据的非等间距分布下表现略逊于 CORAL。 Accuracy 差异较小（因为所有模型都集中犯\\\"±1 depth 错误\\\"）， 但 MAE 和 adjacent accuracy 差异清晰地展示了 ordinal structure 的价值。\\n\"\n  },\n  {\n    \"name\": \"LLM zero-shot depth estimation\",\n    \"description\": \"GPT-4o / Claude 3.5 zero-shot depth判断, depth 0-4, 200 samples per depth\",\n    \"results\": {\n      \"gpt4o\": {\n        \"accuracy\": 0.187,\n        \"mae\": 1.82,\n        \"kendall_tau_with_true_depth\": 0.11\n      },\n      \"claude_3_5\": {\n        \"accuracy\": 0.203,\n        \"mae\": 1.71,\n        \"kendall_tau_with_true_depth\": 0.14\n      },\n      \"human_baseline_estimated\": {\n        \"accuracy\": 0.162,\n        \"mae\": 1.94\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Zero-shot depth estimation by frontier LLMs\",\n        \"columns\": [\n          \"model\",\n          \"accuracy\",\n          \"MAE\",\n          \"Kendall tau\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4o\",\n            0.187,\n            1.82,\n            0.11\n          ],\n          [\n            \"Claude 3.5 Sonnet\",\n            0.203,\n            1.71,\n            0.14\n          ],\n          [\n            \"Our ordinal classifier\",\n            0.483,\n            0.87,\n            0.52\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLM zero-shot 性能仅略高于 random chance (0.20 for 5-class)，而 ordinal classifier 是其 2.5 倍。这确立了 depth estimation 作为一个需要专门方法的 task—— 不能被 frontier LLM 的 general intelligence \\\"免费\\\"解决。强力支持论文的 problem formulation 贡献。\\n\\n\\nLLM 的 zero-shot depth estimation 近乎随机，原因有三： (1) Depth 信号是统计性的（需要对比同一 domain 的多样本分布），单文本缺乏参照系； (2) LLM 未被训练理解\\\"递归生成导致的信息损失\\\"这一概念，其质量判断偏向 fluency 和 coherence， 而这些高层语义特征恰恰是最后才饱和的（与 C2 一致）——即使 gen-3 文本的 vocabulary diversity 已经严重退化，LLM 仍可能判定其\\\"写得不错\\\"因为它仍然 fluent； (3) Prompt 中无法有效传达\\\"相对于 seed 域的偏移\\\"信息。 Claude 略优于 GPT-4o 可能是偶然（差异在 noise range 内），也可能反映其对文本微妙质量差异的 slightly better calibration，但两者都远低于我们的 ordinal classifier（accuracy 0.48 vs 0.19）。 这个结果直接回应\\\"为什么不直接让 LLM 判断\\\"的审稿人问题。\\n\"\n  },\n  {\n    \"name\": \"Binary detector confidence as depth proxy\",\n    \"description\": \"DivEye/Binoculars score 与 true depth 的 Spearman correlation\",\n    \"results\": {\n      \"diveye\": {\n        \"spearman_rho\": 0.23,\n        \"spearman_p_value\": 0.001,\n        \"depth_discrimination_auc_0v1\": 0.94,\n        \"depth_discrimination_auc_1v2\": 0.53\n      },\n      \"binoculars\": {\n        \"spearman_rho\": 0.19,\n        \"spearman_p_value\": 0.003,\n        \"depth_discrimination_auc_0v1\": 0.92,\n        \"depth_discrimination_auc_1v2\": 0.51\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Binary detector scores as depth proxy\",\n        \"columns\": [\n          \"detector\",\n          \"Spearman ρ\",\n          \"p-value\",\n          \"AUC 0v1\",\n          \"AUC 1v2\"\n        ],\n        \"rows\": [\n          [\n            \"DivEye\",\n            0.23,\n            0.001,\n            0.94,\n            0.53\n          ],\n          [\n            \"Binoculars\",\n            0.19,\n            0.003,\n            0.92,\n            0.51\n          ],\n          [\n            \"Our features (15D)\",\n            \"-\",\n            \"-\",\n            0.996,\n            0.696\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary detectors 在 0v1 分辨上强劲但在 1v2 上近乎 chance level， 直接证明\\\"binary detection ≠ depth estimation\\\"的核心论点。 这是论文 related work positioning 的关键数据点：现有方法解决的是不同的问题。\\n\\n\\nBinary detectors 被优化为区分 human vs synthetic，其 confidence score 理论上与\\\"合成程度\\\"正相关。 但这种相关性极弱（ρ < 0.25），因为： (1) Binary detectors 的训练目标是最大化 real/synthetic 的决策边界，不是估计\\\"多 synthetic\\\"； (2) 它们的 score 在 gen-1 处已经几乎饱和（AUC_0v1 > 0.92）， 之后 gen-1 到 gen-5 的 score 差异被压缩到极窄的高 confidence 区间内—— 即\\\"所有合成文本都长得差不多 synthetic\\\"，无法区分代际； (3) Depth signal 是细粒度的分布特征偏移，而 binary detectors 用的 summary statistics （如 min-k% 概率）在 gen-1 之后就进入了平坦区。 Spearman ρ 显著但极弱，证明 binary confidence ≠ depth，binary 框架本质上不足以捕捉 ordinal structure。\\n\"\n  },\n  {\n    \"name\": \"Cross-model transfer\",\n    \"description\": \"Model A 训练的 depth classifier 在 Model B 的 chain 上的 transfer accuracy\",\n    \"results\": {\n      \"transfer_matrix_accuracy\": {\n        \"pythia_to_olmo\": 0.364,\n        \"pythia_to_qwen\": 0.371,\n        \"olmo_to_pythia\": 0.352,\n        \"olmo_to_qwen\": 0.358,\n        \"qwen_to_pythia\": 0.387,\n        \"qwen_to_olmo\": 0.374\n      },\n      \"in_domain_accuracy\": {\n        \"pythia\": 0.401,\n        \"olmo\": 0.388,\n        \"qwen\": 0.418\n      },\n      \"transfer_retention_pct\": {\n        \"mean\": 74.6,\n        \"min\": 70.3,\n        \"max\": 78.9\n      },\n      \"transfer_ordinal_mae\": {\n        \"mean\": 1.14\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Cross-model transfer accuracy matrix\",\n        \"columns\": [\n          \"train\\\\test\",\n          \"Pythia\",\n          \"OLMo\",\n          \"Qwen\",\n          \"mean_transfer\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia\",\n            \"0.401*\",\n            0.364,\n            0.371,\n            0.368\n          ],\n          [\n            \"OLMo\",\n            0.352,\n            \"0.388*\",\n            0.358,\n            0.355\n          ],\n          [\n            \"Qwen\",\n            0.387,\n            0.374,\n            \"0.418*\",\n            0.381\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Transfer retention (%)\",\n        \"columns\": [\n          \"train→test\",\n          \"retention %\"\n        ],\n        \"rows\": [\n          [\n            \"Pythia→OLMo\",\n            73.1\n          ],\n          [\n            \"Pythia→Qwen\",\n            74.2\n          ],\n          [\n            \"OLMo→Pythia\",\n            70.3\n          ],\n          [\n            \"OLMo→Qwen\",\n            71.5\n          ],\n          [\n            \"Qwen→Pythia\",\n            77.4\n          ],\n          [\n            \"Qwen→OLMo\",\n            78.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mean transfer retention 74.6% 落入 best 档 [70, 80]。这证明 depth signal 主要由 模型无关的语言统计量驱动，支持 C1 的\\\"信息论基本量\\\"叙事—— K* 不是某个特定模型的 artifact，而是递归信道的通用性质。 Qwen → others 最优暗示更强模型的 depth boundary 更 transferable。\\n\\n\\nCross-model transfer 成功率反映了 depth signal 中\\\"模型无关成分\\\"的比例。 在 best 档下，transfer retention ≥70% 因为： (1) vocabulary diversity 特征（type-token ratio、hapax ratio）测量的是分布的通用统计性质， 不依赖于具体模型的 token 偏好——任何模型的递归生成都会收窄词汇分布； (2) surprisal dynamics 在 cross-model 设置下仍有 partial transfer， 因为虽然绝对 surprisal 值因模型而异，但相对变化模式（递归导致 surprisal 下降）是通用的； (3) 15D 特征中的 7-8 维是\\\"模型无关\\\"的，占特征预测力的大部分。 Qwen → others 的 transfer 最好（78.9%），因为 Qwen 作为最强模型学到的 decision boundary 更准确、更 general；OLMo → others 最差（70.3%），因为 1B 模型的信号更弱， 学到的 boundary 更 noisy。\\n\"\n  },\n  {\n    \"name\": \"Naturalistic validation (Common Crawl)\",\n    \"description\": \"对 Common Crawl 2025/2026 snapshot 做 depth 预测，与 AlignScore 和 vocabulary richness correlation\",\n    \"results\": {\n      \"spearman_predicted_depth_vs_alignscore\": -0.31,\n      \"spearman_predicted_depth_vs_vocab_richness\": -0.37,\n      \"pct_samples_predicted_depth_geq_1\": 18.4,\n      \"pct_samples_predicted_depth_geq_2\": 7.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Naturalistic validation on Common Crawl\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Spearman(depth, AlignScore)\",\n            -0.31\n          ],\n          [\n            \"Spearman(depth, vocab richness)\",\n            -0.37\n          ],\n          [\n            \"% predicted depth≥1\",\n            \"18.4%\"\n          ],\n          [\n            \"% predicted depth≥2\",\n            \"7.2%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Naturalistic validation 提供了\\\"proof of concept\\\"级别的 wild-data 证据。 相关性中等偏弱但方向正确且显著，足以支持 appendix 或 discussion section 的 generalizability 论述。 不足以作为 main claim 但有效回应\\\"只在 controlled 设置下验证\\\"的审稿人顾虑。\\n\\n\\nCommon Crawl 中的真实合成文本比例和代际深度无法获得 ground truth， 因此只能通过与外部质量指标的 correlation 间接验证。 Predicted depth 与 AlignScore（事实一致性指标）呈负相关（ρ≈-0.31）， 因为更深代际的文本事实偏差更大（递归\\\"电话游戏效应\\\"）。 与 vocabulary richness 的负相关更强（ρ≈-0.37），与 C2 一致：vocabulary diversity 是最先退化的特征。 ~18% 样本被预测为 depth≥1 与 2025-2026 时期 web 合成文本比例的外部估计（15-25%）一致。 depth≥2 仅 7.2%，但这正是 graduated filtering 最有价值的区间。 相关性不高是预期中的——wild data 的噪声、domain 多样性、unknown model 族都会稀释信号。\\n\"\n  },\n  {\n    \"name\": \"Learned representation baseline\",\n    \"description\": \"Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features\",\n    \"results\": {\n      \"frozen_embeddings_mlp\": {\n        \"accuracy\": 0.452,\n        \"mae\": 0.94,\n        \"training_time_gpu_hours\": 2.8,\n        \"feature_dim\": 4096\n      },\n      \"handcrafted_15d\": {\n        \"accuracy\": 0.483,\n        \"mae\": 0.87,\n        \"training_time_gpu_hours\": 0.1,\n        \"feature_dim\": 15\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Learned vs hand-crafted features comparison\",\n        \"columns\": [\n          \"method\",\n          \"accuracy\",\n          \"MAE\",\n          \"dim\",\n          \"GPU hours\"\n        ],\n        \"rows\": [\n          [\n            \"frozen embeddings + MLP\",\n            0.452,\n            0.94,\n            4096,\n            2.8\n          ],\n          [\n            \"hand-crafted 15D\",\n            0.483,\n            0.87,\n            15,\n            0.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hand-crafted features 在所有指标上优于或持平 frozen embeddings，且维度低 270 倍、训练快 28 倍。 这验证了论文\\\"选择 interpretable features 不是妥协而是优势\\\"的叙事， 回应审稿人\\\"为什么不用 learned representations\\\"的问题。\\n\\n\\nFrozen embeddings 包含丰富的语义信息但存在两个劣势： (1) 4096 维中大部分编码的是内容语义（topic、entity）而非递归退化信号， MLP 需要从高维空间中\\\"挖掘\\\"少数相关维度，在 5K 样本量下容易过拟合； (2) Frozen embeddings 来自同一模型（Qwen2.5-1.5B），引入了自我参照偏差—— 模型对自己生成的文本的 embedding 可能有系统性偏向， 但这种偏向在 cross-model 设置下不 transfer。 Hand-crafted 15D features 虽然维度低，但每个特征都直接编码了与递归退化相关的统计量 （diversity、surprisal、tail weight），特征工程的人类先验弥补了维度不足。 更重要的是，15D 特征支持 degradation ordering 分析（C2）和 feature group ablation（exp-005）， 这是 frozen embeddings 无法提供的。 Hand-crafted 优于 frozen 的幅度不大（accuracy +3.1pp），但 interpretability 和 efficiency 优势明显。\\n\"\n  },\n  {\n    \"name\": \"Base vs Instruct model comparison\",\n    \"description\": \"Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异\",\n    \"results\": {\n      \"base\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.993,\n        \"pairwise_auc_1v2\": 0.714,\n        \"pairwise_auc_2v3\": 0.598,\n        \"pairwise_jsd_0v1\": 0.289\n      },\n      \"instruct\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.996,\n        \"pairwise_auc_1v2\": 0.696,\n        \"pairwise_auc_2v3\": 0.589,\n        \"pairwise_jsd_0v1\": 0.267\n      },\n      \"base_vs_instruct_auc_1v2_diff\": 0.018,\n      \"base_vs_instruct_feature_divergence\": {\n        \"surprisal_mean_shift\": -0.12,\n        \"vocab_diversity_shift\": 0.04\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Base vs Instruct comparison (Qwen2.5-1.5B)\",\n        \"columns\": [\n          \"variant\",\n          \"K*\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"JSD_0v1\"\n        ],\n        \"rows\": [\n          [\n            \"base\",\n            2,\n            0.993,\n            0.714,\n            0.598,\n            0.289\n          ],\n          [\n            \"instruct (MVP)\",\n            2,\n            0.996,\n            0.696,\n            0.589,\n            0.267\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Base model 信号略强但 K* 不变，表明 RLHF alignment 压缩了代际差异但未改变信息论收敛行为。 这个结果对实际应用有意义：野外数据可能来自 base 或 instruct model， K*=2 在两种设置下都成立意味着 graduated filtering 框架对两者都适用。\\n\\nBase model 的 depth signal 略强于 Instruct（AUC_1v2: 0.714 vs 0.696），原因： Instruct 微调（RLHF/DPO）将模型输出拉向\\\"人类偏好的模式\\\"——更规范的句式、更安全的措辞、 更集中的 vocabulary 选择。这种 alignment 相当于对输出分布施加了额外约束， 使得即使是 gen-0（human text passed through instruct model）也已经部分\\\"标准化\\\"了。 因此 instruct 模型的递归代际间差异更小——每代输出都被拉向同一个\\\"preferred mode\\\"。 但 K* 仍为 2，因为 alignment 的影响是 quantitative（减弱信号）而非 qualitative（改变收敛行为）。 Surprisal mean shift 为负（instruct 的 surprisal 更低），反映其输出更\\\"可预测\\\"； vocab diversity shift 为正（instruct 的词汇稍微更多样），反映 RLHF 鼓励的表达多样性。 这些差异小但方向一致，为 discussion 中关于\\\"检测 instruct model 输出\\\"的段落提供数据。\\n\"\n  }\n]",
      "numLines": 1084,
      "startLine": 1,
      "totalLines": 1084
    }
  },
  "sourceToolAssistantUUID": "a3486cdc-3fdf-47e0-ad08-0b590f3d5db6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamin…",
  "leafUuid": "8e556c53-aee5-4f15-8bd5-f9785365fafc",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260512T200328",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Assistant

_source line 12 · 2026-05-12T20:23:00.483Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data. Let me write the full LaTeX paper. I need to:

1. Write a complete LaTeX paper targeting EMNLP 2026
2. Include all the experimental results from the JSON
3. Follow the narrative guidance about K*, degradation ordering, and graduated filtering
4. Use proper EMNLP formatting

Let me compose the paper with:
- Abstract
- Introduction
- Related Work
- Method (theoretical framework + features + classifier)
- Experiments (all the experiments from the JSON)
- Conclusion


- References

Now I'm writing the complete LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e556c53-aee5-4f15-8bd5-f9785365fafc",
  "isSidechain": false,
  "requestId": "req_011CayJGXvjbjYHmguqzUYb1",
  "type": "assistant",
  "uuid": "10c16a31-3791-42f7-ad09-9793b677224c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyhuADTjUuyxH6eAMPbJGG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 24370,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 24370,
          "cache_creation_input_tokens": 18471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18471
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

_source line 13 · 2026-05-12T20:23:00.603Z_

Now I'll write the full LaTeX paper. Let me first check if the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c16a31-3791-42f7-ad09-9793b677224c",
  "isSidechain": false,
  "requestId": "req_011CayJGXvjbjYHmguqzUYb1",
  "type": "assistant",
  "uuid": "accbebe6-5536-4e27-85b7-df31bf6c4e69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyhuADTjUuyxH6eAMPbJGG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 24370,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 24370,
          "cache_creation_input_tokens": 18471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18471
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

_source line 14 · 2026-05-12T20:23:02.925Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019yRtYfdRWm5XhYUeNiNgWw`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "accbebe6-5536-4e27-85b7-df31bf6c4e69",
  "isSidechain": false,
  "requestId": "req_011CayJGXvjbjYHmguqzUYb1",
  "type": "assistant",
  "uuid": "3088e5c8-ca78-496b-b6f7-6b920fc44076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyhuADTjUuyxH6eAMPbJGG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18471,
      "cache_read_input_tokens": 24370,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 24370,
          "cache_creation_input_tokens": 18471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18471
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

_source line 15 · 2026-05-12T20:23:03.096Z_

<details><summary>↩ Tool result · `toolu_019yRtYfdRWm5XhYUeNiNgWw`</summary>

```text
experiment_data.json
imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3088e5c8-ca78-496b-b6f7-6b920fc44076",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "a2559348-0117-4b23-8247-340951263bb9",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3088e5c8-ca78-496b-b6f7-6b920fc44076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T20:23:06.337Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0115pwGMNsDQ2mYWwpeApTb9`</summary>

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
  "parentUuid": "a2559348-0117-4b23-8247-340951263bb9",
  "isSidechain": false,
  "requestId": "req_011CayJHVTvTdaX6qBPR8C29",
  "type": "assistant",
  "uuid": "3411138e-bd40-47cf-9aaa-fd8f42149dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ngn55bh1pqzbk6ZJec47He",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 42841,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 42841,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
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

_source line 17 · 2026-05-12T20:23:06.417Z_

<details><summary>↩ Tool result · `toolu_0115pwGMNsDQ2mYWwpeApTb9`</summary>

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
  "parentUuid": "3411138e-bd40-47cf-9aaa-fd8f42149dda",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "e59597a1-7dc8-49dd-828f-778b0128bb6c",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3411138e-bd40-47cf-9aaa-fd8f42149dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T20:23:10.298Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019GmtsoNdbRub5nF9k8KDqS`</summary>

```json
{
  "command": "kpsewhich acl.sty 2>/dev/null; kpsewhich acl_natbib.bst 2>/dev/null; kpsewhich natbib.sty 2>/dev/null; kpsewhich booktabs.sty 2>/dev/null; kpsewhich amsmath.sty 2>/dev/null; kpsewhich graphicx.sty 2>/dev/null; kpsewhich hyperref.sty 2>/dev/null; kpsewhich multirow.sty 2>/dev/null",
  "description": "Check available LaTeX packages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e59597a1-7dc8-49dd-828f-778b0128bb6c",
  "isSidechain": false,
  "requestId": "req_011CayJHjehvf1BwD3gUEMRU",
  "type": "assistant",
  "uuid": "0407907e-9411-455a-b3ae-7245867899f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018X69pjPn8LGYR5QQqHr4zN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 172,
      "cache_read_input_tokens": 43174,
      "output_tokens": 215,
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
          "output_tokens": 215,
          "cache_read_input_tokens": 43174,
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

_source line 19 · 2026-05-12T20:23:10.505Z_

<details><summary>↩ Tool result · `toolu_019GmtsoNdbRub5nF9k8KDqS`</summary>

```text
/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty
/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty
/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0407907e-9411-455a-b3ae-7245867899f4",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "fc0b9370-70c7-497b-b9fe-d4215f2a3456",
  "toolUseResult": {
    "stdout": "/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty\n/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty\n/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\n/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0407907e-9411-455a-b3ae-7245867899f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T20:23:14.333Z_

No acl.sty available, so I'll use a standalone article class with EMNLP-like formatting. Writing the full paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc0b9370-70c7-497b-b9fe-d4215f2a3456",
  "isSidechain": false,
  "requestId": "req_011CayJJ39RWHMtFaPa2My3V",
  "type": "assistant",
  "uuid": "8d495109-7dba-4fb0-b413-eb1fb1d01bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rkDe64vfq5Dz5ikhmUxms",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 43346,
      "output_tokens": 12484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12484,
          "cache_read_input_tokens": 43346,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 399
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

_source line 21 · 2026-05-12T20:27:01.083Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Hcsv9iiTuhVyvcp1B19U8v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}\n\n\\title{$K^*$: Measuring the Generational Discrimination Boundary\\\\in Recursive Synthetic Text}\n\n\\author{\n  Anonymous Authors\\\\\n  \\textit{Under Review at EMNLP 2026}\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by multi-generational synthetic text, yet existing detection methods treat synthetic content as a binary category, ignoring the non-linear quality degradation across recursive generations. We formalize recursive text generation as an iterated lossy channel and derive, via the Data Processing Inequality, the existence of a \\emph{saturation boundary} $K^*$---the generational depth beyond which pairwise discrimination becomes statistically indistinguishable from chance. Through controlled experiments across three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B) and a 7B cross-scale probe, we establish $K^*{=}2$ at the 1--1.5B scale under standard decoding, rising to $K^*{=}3$ under high-temperature decoding ($T{=}1.2$) or at the 7B scale. We reveal a universal degradation ordering: vocabulary diversity collapses before distributional dynamics (Kendall $\\tau{=}0.84$ across model pairs). Finally, we show that even a coarse 3-class depth signal (human / gen-1 / gen-2+) yields 2.2 and 2.1 percentage-point improvements over binary filtering on MMLU and HellaSwag respectively ($p{<}0.05$), with the advantage monotonically increasing with contamination severity. Our results establish $K^*$ as a fundamental, modulable quantity that provides actionable guidance for depth-aware data curation.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nThe proliferation of large language models (LLMs) has led to an accelerating feedback loop: models generate text that enters web corpora, which in turn train future models \\citep{shumailov2024model}. This recursive contamination is not merely a binary phenomenon---first-generation synthetic text retains most of the distributional properties of its human seed, while fourth-generation text may exhibit severe distributional collapse. Yet the dominant paradigm in synthetic text detection treats all machine-generated content identically, drawing a single boundary between ``human'' and ``synthetic'' \\citep{mitchell2023detectgpt,hans2024binoculars}.\n\nThis binary framing is fundamentally inadequate for data curation. A data curator who indiscriminately removes all synthetic-flagged content discards high-quality first-generation text alongside severely degraded later generations. Conversely, retaining all content below a lenient threshold admits deeply recursive text whose distributional pathologies can propagate into downstream models.\n\nWe propose a shift from binary detection to \\emph{generational depth estimation}: given a text, estimate how many rounds of recursive generation it has undergone. This reframing raises a natural question: \\textit{how deep can we see?} The Data Processing Inequality (DPI) guarantees that mutual information between the original human text and its $k$-th generation descendant decreases monotonically. At some depth, the signal must vanish. We call this depth the \\emph{saturation boundary} $K^*$ and argue it is a fundamental information-theoretic quantity, not merely a classifier performance ceiling.\n\nOur contributions are threefold:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Saturation Boundary ($K^*$).} We provide the first systematic measurement of $K^*$ across model families and decoding strategies. We establish $K^*{=}2$ for 1--1.5B-scale models under standard nucleus sampling, and demonstrate that $K^*$ is modulable: it rises to 3 under high-temperature decoding or at the 7B scale.\n\n    \\item \\textbf{Degradation Ordering.} We show that linguistic features collapse in a consistent order across model families: vocabulary diversity saturates at depth 1, while surprisal dynamics persist to depth 2 (mean Kendall $\\tau{=}0.84$). This ordering reflects information-theoretic structure, not model-specific artifacts.\n\n    \\item \\textbf{Graduated Filtering.} We demonstrate that a 3-class ordinal depth signal (human / gen-1 / gen-2+) yields statistically significant improvements over binary filtering: $+2.24$ pp on MMLU and $+2.07$ pp on HellaSwag ($p{<}0.05$), with the advantage growing monotonically with contamination rate.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic text detection.}\nBinary detection methods range from watermarking \\citep{kirchenbauer2023watermark} to statistical tests on token likelihood \\citep{mitchell2023detectgpt,hans2024binoculars}. DivEye \\citep{tulchinskii2024diveye} uses intrinsic dimensionality; Min-K\\%++ \\citep{zhang2024minkpp} uses minimum-probability tokens. All produce a scalar confidence score optimized for a binary decision boundary. We show (Section~\\ref{sec:binary_baseline}) that these scores correlate weakly with generational depth (Spearman $\\rho \\leq 0.23$), confirming that binary detection and depth estimation are distinct problems.\n\n\\paragraph{Model collapse.}\n\\citet{shumailov2024model} characterize the macroscopic phenomenon of iterative retraining on synthetic data, showing progressive loss of distributional tails. \\citet{dohmatob2024model} provide theoretical bounds on convergence rates. Our work complements this line by providing \\emph{detection} tools: rather than studying what happens when models are retrained on their own output, we ask whether the depth of recursive generation can be estimated from text alone.\n\n\\paragraph{Data quality estimation.}\nVerification-based methods use external models to assess factual consistency \\citep{feng2024factuality} or apply quality classifiers as binary gates \\citep{wettig2024qurating}. These approaches do not estimate recursive depth. Our graduated filtering framework subsumes binary quality gates as a special case ($K^*{=}1$).\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Recursive Generation as an Iterated Lossy Channel}\n\\label{sec:theory}\n\nLet $X_0$ denote human-written text drawn from distribution $P_0$. A language model $\\mathcal{M}$ with decoding strategy $\\mathcal{D}$ defines a stochastic channel $\\mathcal{C}_{\\mathcal{M},\\mathcal{D}}: P_k \\mapsto P_{k+1}$, where $P_k$ is the distribution of generation-$k$ text. The Data Processing Inequality guarantees:\n\\begin{equation}\nI(X_0; X_{k+1}) \\leq I(X_0; X_k) \\quad \\forall k \\geq 0\n\\label{eq:dpi}\n\\end{equation}\nwhere $I(\\cdot;\\cdot)$ denotes mutual information. Since the channel is lossy (non-invertible), the inequality is strict, and the sequence $\\{I(X_0; X_k)\\}_{k=0}^{\\infty}$ converges monotonically to a limit that depends on the fixed-point structure of $\\mathcal{C}$.\n\nWe define the \\emph{saturation boundary} $K^*$ as:\n\\begin{equation}\nK^* = \\max\\{k : \\text{AUC}(P_{k-1}, P_k) \\geq \\theta\\}\n\\label{eq:kstar}\n\\end{equation}\nwhere $\\text{AUC}(P_{k-1}, P_k)$ is the area under the ROC curve for pairwise discrimination between adjacent generations using a fixed feature set, and $\\theta$ is a discrimination threshold (we use $\\theta{=}0.60$ throughout). $K^*$ quantifies the depth at which adjacent generations become statistically indistinguishable.\n\n\\paragraph{$K^*$ is an information-theoretic quantity.}\nWhile the operational definition of $K^*$ depends on the feature set and threshold $\\theta$, we argue that it reflects an underlying information-theoretic boundary. The monotonic decay of Jensen--Shannon divergence (JSD) between adjacent generations (e.g., $0.243 \\to 0.014 \\to 0.005 \\to 0.003 \\to 0.002$ for Pythia-1.4B) mirrors the DPI-mandated decay of mutual information. The sharp drop between generations 0--1 and 1--2 (a 17$\\times$ reduction in JSD) followed by a slow asymptotic approach to zero is the empirical signature of an information bottleneck.\n\n\\subsection{Feature Design}\n\\label{sec:features}\n\nWe extract a 15-dimensional feature vector from each text, organized into three groups designed to capture complementary aspects of distributional degradation:\n\n\\paragraph{Vocabulary diversity (5 features).}\nType-token ratio, hapax legomena ratio, Yule's $K$, entropy of the unigram distribution, and Simpson's diversity index. These capture the narrowing of the lexical distribution that accompanies recursive generation.\n\n\\paragraph{Surprisal dynamics (5 features).}\nMean surprisal, surprisal variance, lag-1 autocorrelation of surprisal, auto-mutual information of the surprisal sequence, and mean pointwise mutual information of bigrams. These capture higher-order distributional structure that persists beyond lexical collapse.\n\n\\paragraph{Tail distribution (5 features).}\nProportion of tokens with probability below the 5th, 10th, and 20th percentiles of the reference distribution, kurtosis of the token probability distribution, and the ratio of tail mass to total mass. These capture the ``tail thinning'' effect identified in model collapse literature.\n\nSurprisal values are computed using the generating model itself. This design choice measures the model's self-recognition of its own recursive output, which is the relevant signal for depth estimation in a world where the generating model is unknown but distributional artifacts are universal.\n\n\\subsection{Ordinal Depth Classifier}\n\\label{sec:classifier}\n\nGenerational depth has a natural ordinal structure: gen-1 is ``closer'' to gen-0 than gen-3 is. We use CORAL (Consistent Rank Logits; \\citealp{cao2020coral}) to exploit this structure. CORAL extends binary logistic regression to ordinal outcomes by learning shared feature weights with rank-specific bias terms, estimating cumulative probabilities $P(Y > k | \\mathbf{x})$ for each rank $k$.\n\nFor downstream filtering, we collapse the ordinal predictions into three classes: human ($\\hat{y}{=}0$), gen-1 ($\\hat{y}{=}1$), and gen-2+ ($\\hat{y}{\\geq}2$). This 3-class signal is coarser than the full ordinal prediction but more robust, operating within the $K^*$ boundary where discrimination is reliable.\n\n\\subsection{Graduated Filtering}\n\\label{sec:filtering}\n\nGiven a training corpus with predicted depth labels, graduated filtering assigns depth-dependent weights:\n\\begin{equation}\nw(d) = \\begin{cases}\n1.0 & \\text{if } d = 0 \\text{ (human)} \\\\\n\\alpha & \\text{if } d = 1 \\text{ (gen-1)} \\\\\n0.0 & \\text{if } d \\geq 2 \\text{ (gen-2+)}\n\\end{cases}\n\\label{eq:weights}\n\\end{equation}\nwhere $\\alpha \\in (0, 1)$ is a retention weight for first-generation synthetic text (we use $\\alpha{=}0.5$). Binary filtering corresponds to the special case $\\alpha{=}0$. The key insight is that gen-1 text retains most of the information content of the original human text (JSD$_{0\\text{v}1} \\gg$ JSD$_{1\\text{v}2}$) and should be downweighted, not discarded.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Seed data.} 5,000 documents from C4 \\citep{raffel2020c4}, filtered for length (128--512 tokens) and English language.\n\n\\paragraph{Generation chains.} For each seed document, we generate recursive chains of depth 0--5 using three model families: Pythia-1.4B \\citep{biderman2023pythia}, OLMo-1B \\citep{groeneveld2024olmo}, and Qwen2.5-1.5B-Instruct \\citep{qwen2025qwen25}. Default decoding: nucleus sampling with $p{=}0.95$, $T{=}1.0$. Decoding ablations use greedy, nucleus $p{=}0.9$, $T{=}0.7$, and $T{=}1.2$.\n\n\\paragraph{Cross-scale probe.} Qwen2.5-7B-Instruct on 1,000 documents, depth 0--3 (reduced scale due to compute constraints).\n\n\\paragraph{Classifier.} CORAL with 15D hand-crafted features, trained with 5-fold cross-validation. Evaluation: accuracy, mean absolute error (MAE), and adjacent accuracy (predictions within $\\pm 1$ of true depth).\n\n\\paragraph{Downstream evaluation.} Continued pretraining of Qwen2.5-1.5B on filtered corpora with 30\\% synthetic injection (default), evaluated on MMLU and HellaSwag. Three random seeds; we report mean and standard deviation.\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{$K^*$ Across Model Families (C1)}\n\\label{sec:kstar_results}\n\nTable~\\ref{tab:pairwise} presents pairwise discrimination results for three model families at the 1--1.5B scale. All three exhibit the same qualitative pattern: near-perfect discrimination at depth 0 vs.\\ 1 (AUC $\\geq 0.988$), a sharp drop at 1 vs.\\ 2 (AUC $\\in [0.654, 0.696]$), and convergence toward chance by depth 2 vs.\\ 3 (AUC $\\in [0.558, 0.589]$). Under our threshold $\\theta{=}0.60$, all three models yield $K^*{=}2$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise discrimination across generational depths for three model families. AUC: area under ROC curve (mean $\\pm$ std over 5 folds). JSD: Jensen--Shannon divergence between adjacent depth distributions.}\n\\label{tab:pairwise}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Pair} & \\textbf{AUC} & \\textbf{std} & \\textbf{JSD} & \\textbf{$K^*$} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen2.5-1.5B} & 0v1 & 0.996 & 0.001 & 0.267 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.696 & 0.008 & 0.016 & \\\\\n & 2v3 & 0.589 & 0.011 & 0.007 & \\\\\n & 3v4 & 0.543 & 0.006 & 0.003 & \\\\\n\\midrule\n\\multirow{4}{*}{Pythia-1.4B} & 0v1 & 0.991 & 0.001 & 0.243 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.672 & 0.008 & 0.014 & \\\\\n & 2v3 & 0.571 & 0.011 & 0.005 & \\\\\n & 3v4 & 0.533 & 0.006 & 0.003 & \\\\\n\\midrule\n\\multirow{4}{*}{OLMo-1B} & 0v1 & 0.988 & 0.001 & 0.221 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.654 & 0.009 & 0.012 & \\\\\n & 2v3 & 0.558 & 0.013 & 0.004 & \\\\\n & 3v4 & 0.527 & 0.007 & 0.003 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe JSD decay pattern is remarkably consistent: a 17--18$\\times$ drop from 0v1 to 1v2, followed by a 2--3$\\times$ drop per subsequent pair. This exponential decay is the empirical signature of the DPI-mandated information loss, and its consistency across architecturally diverse models (GPT-NeoX, OLMo, Qwen) supports the interpretation of $K^*$ as an information-theoretic quantity rather than a model-specific artifact.\n\n\\subsection{$K^*$ Modulability: Decoding and Scale (C1)}\n\\label{sec:modulability}\n\n$K^*{=}2$ is not a ceiling but a floor. Table~\\ref{tab:decoding} shows that decoding strategy systematically modulates $K^*$. High-temperature decoding ($T{=}1.2$) increases initial generation entropy, raising $K^*$ to 3 with 2v3 AUC${=}0.648$. The ordering greedy $\\leq$ low-temp $\\leq$ standard nucleus $\\leq$ high-temp reflects the monotonic relationship between generation entropy and the depth of discriminable signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). $T{=}1.2$ raises $K^*$ from 2 to 3 by increasing generation entropy.}\n\\label{tab:decoding}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Decoding} & \\textbf{$K^*$} & \\textbf{AUC$_{1\\text{v}2}$} & \\textbf{AUC$_{2\\text{v}3}$} & \\textbf{AUC$_{3\\text{v}4}$} & \\textbf{JSD$_{0\\text{v}1}$} \\\\\n\\midrule\nGreedy & 2 & 0.651 & 0.554 & 0.526 & 0.234 \\\\\n$T{=}0.7$ & 2 & 0.668 & 0.563 & 0.530 & 0.241 \\\\\nNucleus $p{=}0.9$ & 2 & 0.688 & 0.582 & 0.538 & 0.259 \\\\\nNucleus $p{=}0.95$, $T{=}1.0$ & 2 & 0.696 & 0.589 & 0.543 & 0.267 \\\\\n$T{=}1.2$ & \\textbf{3} & 0.723 & 0.648 & 0.574 & 0.312 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel scale provides a second lever. Qwen2.5-7B achieves $K^*{=}3$ under standard decoding (Table~\\ref{tab:7b}), with 1v2 AUC${=}0.741$ and 2v3 AUC${=}0.662$---both substantially above the 1.5B counterparts. The 7B model's larger parameter space encodes richer distributional structure that persists across more generations before collapsing. These two independent paths to $K^*{=}3$ (high temperature at 1.5B, standard decoding at 7B) establish that $K^*$ varies predictably with model capacity and decoding entropy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale comparison: Qwen2.5-7B vs.\\ 1.5B under identical decoding ($p{=}0.95$, $T{=}1.0$).}\n\\label{tab:7b}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Pair} & \\textbf{7B AUC} & \\textbf{7B JSD} & \\textbf{1.5B AUC} & \\textbf{1.5B JSD} \\\\\n\\midrule\n0v1 & 0.998 & 0.341 & 0.996 & 0.267 \\\\\n1v2 & 0.741 & 0.032 & 0.696 & 0.016 \\\\\n2v3 & 0.662 & 0.013 & 0.589 & 0.007 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\small $K^*_{\\text{7B}} = 3$, $K^*_{\\text{1.5B}} = 2$. Ordinal accuracy: 7B = 0.518, 1.5B = 0.418.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{$K^*$ Sensitivity Analysis}\n\\label{sec:sensitivity}\n\nTable~\\ref{tab:sensitivity} shows that $K^*$ is robust to threshold choice within the reasonable range $\\theta \\in [0.60, 0.65]$, where all standard-decoding models yield $K^*{=}2$. The threshold $\\theta{=}0.60$ occupies the center of this stable interval and is meaningfully above chance (0.50). At $\\theta{=}0.55$, $K^*$ inflates because 2v3 AUC values (0.558--0.589) exceed this lenient threshold; at $\\theta{=}0.70$, $K^*$ deflates to 1. The $T{=}1.2$ condition shows a systematic upward shift of $+1$ across all thresholds, confirming that the modulability effect is not a threshold artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$K^*$ sensitivity to AUC threshold $\\theta$. Shaded region $[0.60, 0.65]$ is the recommended operating range.}\n\\label{tab:sensitivity}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.65$ & $\\theta{=}0.70$ \\\\\n\\midrule\nQwen2.5-1.5B & 3 & 2 & 2 & 1 \\\\\nPythia-1.4B & 3 & 2 & 2 & 1 \\\\\nOLMo-1B & 2 & 2 & 2 & 1 \\\\\nQwen2.5-1.5B ($T{=}1.2$) & 4 & 3 & 3 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Degradation Ordering (C2)}\n\\label{sec:ordering}\n\nTable~\\ref{tab:degradation} reveals a consistent ordering of feature group saturation across all three model families. Vocabulary diversity features saturate at depth 1 in all models---the narrowing of the lexical distribution is the earliest and most uniform effect of recursive generation. Surprisal dynamics persist to depth 2 in all models, reflecting the slower decay of higher-order conditional statistics. Tail-thinning features show model-dependent behavior: saturation at depth 1 for OLMo-1B (whose smaller capacity produces thinner tails from the outset) but depth 2 for the larger models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature group saturation depth by model (depth at which the feature group's discriminative AUC first falls below $\\theta{=}0.60$ for adjacent-generation classification).}\n\\label{tab:degradation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Feature Group} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen2.5-1.5B} \\\\\n\\midrule\nVocabulary diversity & 1 & 1 & 1 \\\\\nSurprisal dynamics & 2 & 2 & 2 \\\\\nTail distribution & 2 & 1 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-model consistency of this ordering is quantified by Kendall's $\\tau$ between feature-level saturation rank vectors (Table~\\ref{tab:kendall}). The mean $\\tau{=}0.84$ indicates that the degradation ordering is a structural property of recursive generation, not a model-specific phenomenon. This has practical implications: vocabulary diversity features alone are sufficient for depth-1 detection but insufficient for finer-grained depth estimation, which requires the slower-decaying surprisal dynamics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model consistency of degradation ordering (Kendall's $\\tau$).}\n\\label{tab:kendall}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Model Pair} & \\textbf{$\\tau$} \\\\\n\\midrule\nPythia vs.\\ Qwen & 0.87 \\\\\nOLMo vs.\\ Qwen & 0.82 \\\\\nPythia vs.\\ OLMo & 0.84 \\\\\n\\midrule\n\\textbf{Mean} & \\textbf{0.84} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graduated Filtering (C3)}\n\\label{sec:filtering_results}\n\nTable~\\ref{tab:downstream} presents downstream evaluation results under four data curation strategies. Graduated filtering (3-class: human / gen-1 / gen-2+) outperforms binary filtering by $+2.24$ pp on MMLU and $+2.07$ pp on HellaSwag, both statistically significant ($p{=}0.008$ and $p{=}0.013$ respectively, paired $t$-test across 3 seeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream evaluation: continued pretraining performance on MMLU and HellaSwag (percentage points). 30\\% synthetic injection rate. Mean $\\pm$ std over 3 seeds.}\n\\label{tab:downstream}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU (pp)} & \\textbf{HellaSwag (pp)} \\\\\n\\midrule\nNo filter & $25.31 \\pm 0.23$ & $42.67 \\pm 0.19$ \\\\\nBinary & $26.18 \\pm 0.31$ & $43.54 \\pm 0.25$ \\\\\nSurprisal-based & $27.89 \\pm 0.35$ & $45.12 \\pm 0.29$ \\\\\n\\textbf{Graduated (3-class)} & $\\mathbf{28.42 \\pm 0.28}$ & $\\mathbf{45.61 \\pm 0.22}$ \\\\\n\\midrule\n$\\Delta$ (graduated $-$ binary) & $+2.24$ ($p{=}0.008$) & $+2.07$ ($p{=}0.013$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe advantage of graduated filtering derives from its treatment of gen-1 text: rather than discarding it (binary) or retaining it at full weight (no filter), graduated filtering downweights it ($\\alpha{=}0.5$), preserving the substantial information content of first-generation text while attenuating its distributional artifacts.\n\n\\paragraph{Dose-response analysis.} Table~\\ref{tab:dose} shows that the graduated filtering advantage grows monotonically with contamination rate. At 10\\% injection, the advantage is modest ($+0.82$ pp MMLU). At 50\\%---approaching projected web contamination levels---it reaches $+3.41$ pp on MMLU and $+2.89$ pp on HellaSwag. This dose-response relationship implies that the value of depth-aware curation will increase as synthetic text becomes more prevalent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response: graduated vs.\\ binary filtering advantage ($\\Delta$ pp) by synthetic injection rate.}\n\\label{tab:dose}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Injection Rate} & $\\Delta$ \\textbf{MMLU (pp)} & $\\Delta$ \\textbf{HellaSwag (pp)} \\\\\n\\midrule\n10\\% & 0.82 & 0.54 \\\\\n30\\% & 2.24 & 2.07 \\\\\n50\\% & 3.41 & 2.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ablations and Baselines}\n\\label{sec:ablations}\n\n\\paragraph{Classifier architecture.}\nTable~\\ref{tab:classifier} compares CORAL against multinomial classification and ordinal regression. CORAL achieves the best MAE (0.87 vs.\\ 1.03 for multinomial), confirming that exploiting the ordinal structure of depth labels reduces prediction error. The gap is largest in MAE and adjacent accuracy, where ordinal-aware losses penalize distant misclassifications more heavily.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Classifier architecture comparison on depth estimation (Qwen2.5-1.5B, 5-fold CV).}\n\\label{tab:classifier}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Adj.\\ Acc.} \\\\\n\\midrule\nCORAL (ordinal) & \\textbf{0.483} & \\textbf{0.87} & \\textbf{0.821} \\\\\nOrdinal regression & 0.461 & 0.91 & 0.808 \\\\\nMultinomial & 0.472 & 1.03 & 0.784 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Hand-crafted vs.\\ learned features.}\nTable~\\ref{tab:features} shows that our 15D hand-crafted features outperform frozen Qwen2.5-1.5B embeddings (4096D) passed through an MLP, while being 270$\\times$ lower-dimensional and 28$\\times$ faster to train. The frozen embeddings encode primarily semantic content; the few dimensions relevant to depth estimation are diluted by thousands of irrelevant dimensions, leading to overfitting on 5K samples.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hand-crafted (15D) vs.\\ learned (4096D frozen embeddings + MLP) features.}\n\\label{tab:features}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Dim} & \\textbf{GPU-hrs} \\\\\n\\midrule\nFrozen emb.\\ + MLP & 0.452 & 0.94 & 4096 & 2.8 \\\\\nHand-crafted 15D & \\textbf{0.483} & \\textbf{0.87} & 15 & 0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LLM zero-shot baseline.}\nFrontier LLMs perform near chance on depth estimation (Table~\\ref{tab:llm}). GPT-4o achieves 18.7\\% accuracy (chance: 20\\% for 5-class) with Kendall $\\tau{=}0.11$; Claude 3.5 Sonnet reaches 20.3\\% with $\\tau{=}0.14$. Depth estimation requires population-level statistical features that cannot be assessed from a single text without a reference distribution, explaining why general-purpose LLMs fail at this task.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot depth estimation by frontier LLMs vs.\\ our ordinal classifier.}\n\\label{tab:llm}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nGPT-4o & 0.187 & 1.82 & 0.11 \\\\\nClaude 3.5 Sonnet & 0.203 & 1.71 & 0.14 \\\\\n\\textbf{Our classifier} & \\textbf{0.483} & \\textbf{0.87} & \\textbf{0.52} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Binary detector depth sensitivity.}\n\\label{sec:binary_baseline}\nExisting binary detectors correlate weakly with depth (Table~\\ref{tab:binary}). DivEye achieves Spearman $\\rho{=}0.23$ with true depth; Binoculars achieves $\\rho{=}0.19$. Both excel at 0v1 discrimination (AUC $\\geq 0.92$) but collapse to chance at 1v2 (AUC $\\leq 0.53$). Their confidence scores are optimized for the binary boundary, not for ordinal depth estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary detector scores as depth proxies.}\n\\label{tab:binary}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Detector} & \\textbf{Spearman $\\rho$} & \\textbf{$p$-value} & \\textbf{AUC$_{0\\text{v}1}$} & \\textbf{AUC$_{1\\text{v}2}$} \\\\\n\\midrule\nDivEye & 0.23 & 0.001 & 0.94 & 0.53 \\\\\nBinoculars & 0.19 & 0.003 & 0.92 & 0.51 \\\\\nOur features (15D) & --- & --- & 0.996 & 0.696 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer} shows that classifiers trained on one model's generation chain retain 70--79\\% of their in-domain accuracy when applied to chains from a different model family. Mean transfer retention is 74.6\\%, indicating that depth signals are predominantly model-agnostic. Qwen-trained classifiers transfer best (mean 78.2\\%), likely because the stronger model learns more generalizable decision boundaries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer accuracy matrix. Diagonal entries (marked *) are in-domain.}\n\\label{tab:transfer}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Train $\\backslash$ Test} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen} & \\textbf{Mean transfer} \\\\\n\\midrule\nPythia & 0.401* & 0.364 & 0.371 & 0.368 \\\\\nOLMo & 0.352 & 0.388* & 0.358 & 0.355 \\\\\nQwen & 0.387 & 0.374 & 0.418* & 0.381 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ecological Validity}\n\\label{sec:validity}\n\n\\paragraph{Retrain-chain validation.}\nTable~\\ref{tab:retrain} compares prompt-chain generation (our default) with retrain-chain generation (LoRA fine-tuning at each depth). Both yield identical $K^*{=}2$. AUC differences are small ($|\\Delta| \\leq 0.014$), and feature distribution divergence between the two paradigms remains below JSD${=}0.042$ at all depths. Prompt-chains are a valid experimental proxy for the retrain dynamics that drive real-world recursive contamination.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Retrain-chain vs.\\ prompt-chain (Pythia-1.4B, both $K^*{=}2$).}\n\\label{tab:retrain}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Pair} & \\textbf{Retrain AUC} & \\textbf{Prompt AUC} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.987 & 0.991 & $-0.004$ \\\\\n1v2 & 0.658 & 0.672 & $-0.014$ \\\\\n2v3 & 0.563 & 0.571 & $-0.008$ \\\\\n3v4 & 0.529 & 0.533 & $-0.004$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Base vs.\\ Instruct models.}\nComparing Qwen2.5-1.5B base and Instruct variants, both yield $K^*{=}2$. The base model shows slightly stronger depth signal (AUC$_{1\\text{v}2}$: 0.714 vs.\\ 0.696), likely because RLHF alignment compresses output distributions toward a ``preferred mode,'' reducing inter-generational variance. The quantitative but not qualitative difference confirms that our framework applies to both model types.\n\n\\paragraph{Common Crawl validation.}\nAs a naturalistic sanity check, we apply our classifier to Common Crawl 2025/2026 snapshots. Predicted depth correlates negatively with AlignScore (Spearman $\\rho{=}{-}0.31$) and vocabulary richness ($\\rho{=}{-}0.37$), both in the expected direction. The estimated proportion of depth${\\geq}1$ content (18.4\\%) aligns with external estimates of web synthetic text prevalence (15--25\\%).\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{$K^*$ as a fundamental quantity.}\nOur results position $K^*$ not as a classifier performance metric but as an information-theoretic property of the recursive generation channel. Its systematic variation with model scale ($K^*{=}2$ at 1.5B, $K^*{=}3$ at 7B) and decoding entropy ($K^*{=}2$ at $T{=}1.0$, $K^*{=}3$ at $T{=}1.2$) follows directly from the DPI: higher initial mutual information requires more lossy steps to reach the discrimination floor. The stability of $K^*$ across threshold choices $\\theta \\in [0.60, 0.65]$ and its consistency across three model families further support this interpretation.\n\n\\paragraph{Practical implications.}\nFor data curators, $K^*$ provides a concrete answer to ``how much depth resolution is useful?'' At current model scales (1--7B), distinguishing human text from gen-1 and gen-2+ (a 3-class problem) captures essentially all available depth information. This is good news: even coarse ordinal signals yield meaningful downstream improvements, and the 15D feature set required is computationally cheap (0.1 GPU-hours for full training).\n\n\\paragraph{Limitations.}\nOur experiments use models up to 7B parameters and English-only text. $K^*$ at the scale of frontier models (70B+) remains unmeasured, though our results predict it should be higher. The downstream evaluation uses continued pretraining rather than training from scratch, which may underestimate the impact of depth-aware filtering. Our retrain-chain validation uses LoRA rather than full fine-tuning, providing a lower bound on the retrain--prompt divergence.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced the saturation boundary $K^*$ as a fundamental measure of how deeply recursive generation can be discriminated, grounded it in the Data Processing Inequality, and measured it systematically across model families, scales, and decoding strategies. Our key findings are: (1) $K^*{=}2$ at 1--1.5B scale under standard decoding, rising to 3 at 7B or under high-temperature decoding; (2) linguistic features degrade in a universal order, with vocabulary diversity collapsing before distributional dynamics; and (3) even a coarse 3-class depth signal yields 1.5--3.5 pp downstream improvement over binary filtering, with the advantage growing with contamination severity. As recursive synthetic text becomes increasingly prevalent in web corpora, depth-aware data curation will become not just useful but necessary. $K^*$ tells us how much resolution is available; graduated filtering shows how to use it.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nStella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Cao et~al.(2020)]{cao2020coral}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Feng et~al.(2024)]{feng2024factuality}\nShangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov.\n\\newblock FactScore: Fine-grained atomic evaluation of factual precision in long form text generation.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nDirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLMs} with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Qwen Team(2025)]{qwen2025qwen25}\nQwen Team.\n\\newblock Qwen2.5: A party of foundation models.\n\\newblock \\emph{arXiv preprint arXiv:2412.15115}, 2025.\n\n\\bibitem[Raffel et~al.(2020)]{raffel2020c4}\nColin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter~J Liu.\n\\newblock Exploring the limits of transfer learning with a unified text-to-text transformer.\n\\newblock \\emph{JMLR}, 21(140):1--67, 2020.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024diveye}\nEduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nAlexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024minkpp}\nYijian Zhang, Jiaao Chen, Diyi Yang, and Thomas Hartvigsen.\n\\newblock Min-{K}\\%++: Improved baseline for detecting pre-training data from large language models.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d495109-7dba-4fb0-b413-eb1fb1d01bce",
  "isSidechain": false,
  "requestId": "req_011CayJJ39RWHMtFaPa2My3V",
  "type": "assistant",
  "uuid": "d2d1d853-0f9c-4d64-89e3-83c922c75008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019rkDe64vfq5Dz5ikhmUxms",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 43346,
      "output_tokens": 12484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12484,
          "cache_read_input_tokens": 43346,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 399
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

_source line 22 · 2026-05-12T20:27:01.098Z_

<details><summary>↩ Tool result · `toolu_01Hcsv9iiTuhVyvcp1B19U8v`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2d1d853-0f9c-4d64-89e3-83c922c75008",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "8c191948-bce9-4796-bbf8-bc299c6d37da",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\hypersetup{colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue}\n\n\\title{$K^*$: Measuring the Generational Discrimination Boundary\\\\in Recursive Synthetic Text}\n\n\\author{\n  Anonymous Authors\\\\\n  \\textit{Under Review at EMNLP 2026}\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by multi-generational synthetic text, yet existing detection methods treat synthetic content as a binary category, ignoring the non-linear quality degradation across recursive generations. We formalize recursive text generation as an iterated lossy channel and derive, via the Data Processing Inequality, the existence of a \\emph{saturation boundary} $K^*$---the generational depth beyond which pairwise discrimination becomes statistically indistinguishable from chance. Through controlled experiments across three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B) and a 7B cross-scale probe, we establish $K^*{=}2$ at the 1--1.5B scale under standard decoding, rising to $K^*{=}3$ under high-temperature decoding ($T{=}1.2$) or at the 7B scale. We reveal a universal degradation ordering: vocabulary diversity collapses before distributional dynamics (Kendall $\\tau{=}0.84$ across model pairs). Finally, we show that even a coarse 3-class depth signal (human / gen-1 / gen-2+) yields 2.2 and 2.1 percentage-point improvements over binary filtering on MMLU and HellaSwag respectively ($p{<}0.05$), with the advantage monotonically increasing with contamination severity. Our results establish $K^*$ as a fundamental, modulable quantity that provides actionable guidance for depth-aware data curation.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nThe proliferation of large language models (LLMs) has led to an accelerating feedback loop: models generate text that enters web corpora, which in turn train future models \\citep{shumailov2024model}. This recursive contamination is not merely a binary phenomenon---first-generation synthetic text retains most of the distributional properties of its human seed, while fourth-generation text may exhibit severe distributional collapse. Yet the dominant paradigm in synthetic text detection treats all machine-generated content identically, drawing a single boundary between ``human'' and ``synthetic'' \\citep{mitchell2023detectgpt,hans2024binoculars}.\n\nThis binary framing is fundamentally inadequate for data curation. A data curator who indiscriminately removes all synthetic-flagged content discards high-quality first-generation text alongside severely degraded later generations. Conversely, retaining all content below a lenient threshold admits deeply recursive text whose distributional pathologies can propagate into downstream models.\n\nWe propose a shift from binary detection to \\emph{generational depth estimation}: given a text, estimate how many rounds of recursive generation it has undergone. This reframing raises a natural question: \\textit{how deep can we see?} The Data Processing Inequality (DPI) guarantees that mutual information between the original human text and its $k$-th generation descendant decreases monotonically. At some depth, the signal must vanish. We call this depth the \\emph{saturation boundary} $K^*$ and argue it is a fundamental information-theoretic quantity, not merely a classifier performance ceiling.\n\nOur contributions are threefold:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Saturation Boundary ($K^*$).} We provide the first systematic measurement of $K^*$ across model families and decoding strategies. We establish $K^*{=}2$ for 1--1.5B-scale models under standard nucleus sampling, and demonstrate that $K^*$ is modulable: it rises to 3 under high-temperature decoding or at the 7B scale.\n\n    \\item \\textbf{Degradation Ordering.} We show that linguistic features collapse in a consistent order across model families: vocabulary diversity saturates at depth 1, while surprisal dynamics persist to depth 2 (mean Kendall $\\tau{=}0.84$). This ordering reflects information-theoretic structure, not model-specific artifacts.\n\n    \\item \\textbf{Graduated Filtering.} We demonstrate that a 3-class ordinal depth signal (human / gen-1 / gen-2+) yields statistically significant improvements over binary filtering: $+2.24$ pp on MMLU and $+2.07$ pp on HellaSwag ($p{<}0.05$), with the advantage growing monotonically with contamination rate.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Synthetic text detection.}\nBinary detection methods range from watermarking \\citep{kirchenbauer2023watermark} to statistical tests on token likelihood \\citep{mitchell2023detectgpt,hans2024binoculars}. DivEye \\citep{tulchinskii2024diveye} uses intrinsic dimensionality; Min-K\\%++ \\citep{zhang2024minkpp} uses minimum-probability tokens. All produce a scalar confidence score optimized for a binary decision boundary. We show (Section~\\ref{sec:binary_baseline}) that these scores correlate weakly with generational depth (Spearman $\\rho \\leq 0.23$), confirming that binary detection and depth estimation are distinct problems.\n\n\\paragraph{Model collapse.}\n\\citet{shumailov2024model} characterize the macroscopic phenomenon of iterative retraining on synthetic data, showing progressive loss of distributional tails. \\citet{dohmatob2024model} provide theoretical bounds on convergence rates. Our work complements this line by providing \\emph{detection} tools: rather than studying what happens when models are retrained on their own output, we ask whether the depth of recursive generation can be estimated from text alone.\n\n\\paragraph{Data quality estimation.}\nVerification-based methods use external models to assess factual consistency \\citep{feng2024factuality} or apply quality classifiers as binary gates \\citep{wettig2024qurating}. These approaches do not estimate recursive depth. Our graduated filtering framework subsumes binary quality gates as a special case ($K^*{=}1$).\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Recursive Generation as an Iterated Lossy Channel}\n\\label{sec:theory}\n\nLet $X_0$ denote human-written text drawn from distribution $P_0$. A language model $\\mathcal{M}$ with decoding strategy $\\mathcal{D}$ defines a stochastic channel $\\mathcal{C}_{\\mathcal{M},\\mathcal{D}}: P_k \\mapsto P_{k+1}$, where $P_k$ is the distribution of generation-$k$ text. The Data Processing Inequality guarantees:\n\\begin{equation}\nI(X_0; X_{k+1}) \\leq I(X_0; X_k) \\quad \\forall k \\geq 0\n\\label{eq:dpi}\n\\end{equation}\nwhere $I(\\cdot;\\cdot)$ denotes mutual information. Since the channel is lossy (non-invertible), the inequality is strict, and the sequence $\\{I(X_0; X_k)\\}_{k=0}^{\\infty}$ converges monotonically to a limit that depends on the fixed-point structure of $\\mathcal{C}$.\n\nWe define the \\emph{saturation boundary} $K^*$ as:\n\\begin{equation}\nK^* = \\max\\{k : \\text{AUC}(P_{k-1}, P_k) \\geq \\theta\\}\n\\label{eq:kstar}\n\\end{equation}\nwhere $\\text{AUC}(P_{k-1}, P_k)$ is the area under the ROC curve for pairwise discrimination between adjacent generations using a fixed feature set, and $\\theta$ is a discrimination threshold (we use $\\theta{=}0.60$ throughout). $K^*$ quantifies the depth at which adjacent generations become statistically indistinguishable.\n\n\\paragraph{$K^*$ is an information-theoretic quantity.}\nWhile the operational definition of $K^*$ depends on the feature set and threshold $\\theta$, we argue that it reflects an underlying information-theoretic boundary. The monotonic decay of Jensen--Shannon divergence (JSD) between adjacent generations (e.g., $0.243 \\to 0.014 \\to 0.005 \\to 0.003 \\to 0.002$ for Pythia-1.4B) mirrors the DPI-mandated decay of mutual information. The sharp drop between generations 0--1 and 1--2 (a 17$\\times$ reduction in JSD) followed by a slow asymptotic approach to zero is the empirical signature of an information bottleneck.\n\n\\subsection{Feature Design}\n\\label{sec:features}\n\nWe extract a 15-dimensional feature vector from each text, organized into three groups designed to capture complementary aspects of distributional degradation:\n\n\\paragraph{Vocabulary diversity (5 features).}\nType-token ratio, hapax legomena ratio, Yule's $K$, entropy of the unigram distribution, and Simpson's diversity index. These capture the narrowing of the lexical distribution that accompanies recursive generation.\n\n\\paragraph{Surprisal dynamics (5 features).}\nMean surprisal, surprisal variance, lag-1 autocorrelation of surprisal, auto-mutual information of the surprisal sequence, and mean pointwise mutual information of bigrams. These capture higher-order distributional structure that persists beyond lexical collapse.\n\n\\paragraph{Tail distribution (5 features).}\nProportion of tokens with probability below the 5th, 10th, and 20th percentiles of the reference distribution, kurtosis of the token probability distribution, and the ratio of tail mass to total mass. These capture the ``tail thinning'' effect identified in model collapse literature.\n\nSurprisal values are computed using the generating model itself. This design choice measures the model's self-recognition of its own recursive output, which is the relevant signal for depth estimation in a world where the generating model is unknown but distributional artifacts are universal.\n\n\\subsection{Ordinal Depth Classifier}\n\\label{sec:classifier}\n\nGenerational depth has a natural ordinal structure: gen-1 is ``closer'' to gen-0 than gen-3 is. We use CORAL (Consistent Rank Logits; \\citealp{cao2020coral}) to exploit this structure. CORAL extends binary logistic regression to ordinal outcomes by learning shared feature weights with rank-specific bias terms, estimating cumulative probabilities $P(Y > k | \\mathbf{x})$ for each rank $k$.\n\nFor downstream filtering, we collapse the ordinal predictions into three classes: human ($\\hat{y}{=}0$), gen-1 ($\\hat{y}{=}1$), and gen-2+ ($\\hat{y}{\\geq}2$). This 3-class signal is coarser than the full ordinal prediction but more robust, operating within the $K^*$ boundary where discrimination is reliable.\n\n\\subsection{Graduated Filtering}\n\\label{sec:filtering}\n\nGiven a training corpus with predicted depth labels, graduated filtering assigns depth-dependent weights:\n\\begin{equation}\nw(d) = \\begin{cases}\n1.0 & \\text{if } d = 0 \\text{ (human)} \\\\\n\\alpha & \\text{if } d = 1 \\text{ (gen-1)} \\\\\n0.0 & \\text{if } d \\geq 2 \\text{ (gen-2+)}\n\\end{cases}\n\\label{eq:weights}\n\\end{equation}\nwhere $\\alpha \\in (0, 1)$ is a retention weight for first-generation synthetic text (we use $\\alpha{=}0.5$). Binary filtering corresponds to the special case $\\alpha{=}0$. The key insight is that gen-1 text retains most of the information content of the original human text (JSD$_{0\\text{v}1} \\gg$ JSD$_{1\\text{v}2}$) and should be downweighted, not discarded.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Seed data.} 5,000 documents from C4 \\citep{raffel2020c4}, filtered for length (128--512 tokens) and English language.\n\n\\paragraph{Generation chains.} For each seed document, we generate recursive chains of depth 0--5 using three model families: Pythia-1.4B \\citep{biderman2023pythia}, OLMo-1B \\citep{groeneveld2024olmo}, and Qwen2.5-1.5B-Instruct \\citep{qwen2025qwen25}. Default decoding: nucleus sampling with $p{=}0.95$, $T{=}1.0$. Decoding ablations use greedy, nucleus $p{=}0.9$, $T{=}0.7$, and $T{=}1.2$.\n\n\\paragraph{Cross-scale probe.} Qwen2.5-7B-Instruct on 1,000 documents, depth 0--3 (reduced scale due to compute constraints).\n\n\\paragraph{Classifier.} CORAL with 15D hand-crafted features, trained with 5-fold cross-validation. Evaluation: accuracy, mean absolute error (MAE), and adjacent accuracy (predictions within $\\pm 1$ of true depth).\n\n\\paragraph{Downstream evaluation.} Continued pretraining of Qwen2.5-1.5B on filtered corpora with 30\\% synthetic injection (default), evaluated on MMLU and HellaSwag. Three random seeds; we report mean and standard deviation.\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{$K^*$ Across Model Families (C1)}\n\\label{sec:kstar_results}\n\nTable~\\ref{tab:pairwise} presents pairwise discrimination results for three model families at the 1--1.5B scale. All three exhibit the same qualitative pattern: near-perfect discrimination at depth 0 vs.\\ 1 (AUC $\\geq 0.988$), a sharp drop at 1 vs.\\ 2 (AUC $\\in [0.654, 0.696]$), and convergence toward chance by depth 2 vs.\\ 3 (AUC $\\in [0.558, 0.589]$). Under our threshold $\\theta{=}0.60$, all three models yield $K^*{=}2$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pairwise discrimination across generational depths for three model families. AUC: area under ROC curve (mean $\\pm$ std over 5 folds). JSD: Jensen--Shannon divergence between adjacent depth distributions.}\n\\label{tab:pairwise}\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Pair} & \\textbf{AUC} & \\textbf{std} & \\textbf{JSD} & \\textbf{$K^*$} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen2.5-1.5B} & 0v1 & 0.996 & 0.001 & 0.267 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.696 & 0.008 & 0.016 & \\\\\n & 2v3 & 0.589 & 0.011 & 0.007 & \\\\\n & 3v4 & 0.543 & 0.006 & 0.003 & \\\\\n\\midrule\n\\multirow{4}{*}{Pythia-1.4B} & 0v1 & 0.991 & 0.001 & 0.243 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.672 & 0.008 & 0.014 & \\\\\n & 2v3 & 0.571 & 0.011 & 0.005 & \\\\\n & 3v4 & 0.533 & 0.006 & 0.003 & \\\\\n\\midrule\n\\multirow{4}{*}{OLMo-1B} & 0v1 & 0.988 & 0.001 & 0.221 & \\multirow{4}{*}{2} \\\\\n & 1v2 & 0.654 & 0.009 & 0.012 & \\\\\n & 2v3 & 0.558 & 0.013 & 0.004 & \\\\\n & 3v4 & 0.527 & 0.007 & 0.003 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe JSD decay pattern is remarkably consistent: a 17--18$\\times$ drop from 0v1 to 1v2, followed by a 2--3$\\times$ drop per subsequent pair. This exponential decay is the empirical signature of the DPI-mandated information loss, and its consistency across architecturally diverse models (GPT-NeoX, OLMo, Qwen) supports the interpretation of $K^*$ as an information-theoretic quantity rather than a model-specific artifact.\n\n\\subsection{$K^*$ Modulability: Decoding and Scale (C1)}\n\\label{sec:modulability}\n\n$K^*{=}2$ is not a ceiling but a floor. Table~\\ref{tab:decoding} shows that decoding strategy systematically modulates $K^*$. High-temperature decoding ($T{=}1.2$) increases initial generation entropy, raising $K^*$ to 3 with 2v3 AUC${=}0.648$. The ordering greedy $\\leq$ low-temp $\\leq$ standard nucleus $\\leq$ high-temp reflects the monotonic relationship between generation entropy and the depth of discriminable signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). $T{=}1.2$ raises $K^*$ from 2 to 3 by increasing generation entropy.}\n\\label{tab:decoding}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Decoding} & \\textbf{$K^*$} & \\textbf{AUC$_{1\\text{v}2}$} & \\textbf{AUC$_{2\\text{v}3}$} & \\textbf{AUC$_{3\\text{v}4}$} & \\textbf{JSD$_{0\\text{v}1}$} \\\\\n\\midrule\nGreedy & 2 & 0.651 & 0.554 & 0.526 & 0.234 \\\\\n$T{=}0.7$ & 2 & 0.668 & 0.563 & 0.530 & 0.241 \\\\\nNucleus $p{=}0.9$ & 2 & 0.688 & 0.582 & 0.538 & 0.259 \\\\\nNucleus $p{=}0.95$, $T{=}1.0$ & 2 & 0.696 & 0.589 & 0.543 & 0.267 \\\\\n$T{=}1.2$ & \\textbf{3} & 0.723 & 0.648 & 0.574 & 0.312 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel scale provides a second lever. Qwen2.5-7B achieves $K^*{=}3$ under standard decoding (Table~\\ref{tab:7b}), with 1v2 AUC${=}0.741$ and 2v3 AUC${=}0.662$---both substantially above the 1.5B counterparts. The 7B model's larger parameter space encodes richer distributional structure that persists across more generations before collapsing. These two independent paths to $K^*{=}3$ (high temperature at 1.5B, standard decoding at 7B) establish that $K^*$ varies predictably with model capacity and decoding entropy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale comparison: Qwen2.5-7B vs.\\ 1.5B under identical decoding ($p{=}0.95$, $T{=}1.0$).}\n\\label{tab:7b}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Pair} & \\textbf{7B AUC} & \\textbf{7B JSD} & \\textbf{1.5B AUC} & \\textbf{1.5B JSD} \\\\\n\\midrule\n0v1 & 0.998 & 0.341 & 0.996 & 0.267 \\\\\n1v2 & 0.741 & 0.032 & 0.696 & 0.016 \\\\\n2v3 & 0.662 & 0.013 & 0.589 & 0.007 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\small $K^*_{\\text{7B}} = 3$, $K^*_{\\text{1.5B}} = 2$. Ordinal accuracy: 7B = 0.518, 1.5B = 0.418.}\n\\end{tabular}\n\\end{table}\n\n\\subsection{$K^*$ Sensitivity Analysis}\n\\label{sec:sensitivity}\n\nTable~\\ref{tab:sensitivity} shows that $K^*$ is robust to threshold choice within the reasonable range $\\theta \\in [0.60, 0.65]$, where all standard-decoding models yield $K^*{=}2$. The threshold $\\theta{=}0.60$ occupies the center of this stable interval and is meaningfully above chance (0.50). At $\\theta{=}0.55$, $K^*$ inflates because 2v3 AUC values (0.558--0.589) exceed this lenient threshold; at $\\theta{=}0.70$, $K^*$ deflates to 1. The $T{=}1.2$ condition shows a systematic upward shift of $+1$ across all thresholds, confirming that the modulability effect is not a threshold artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$K^*$ sensitivity to AUC threshold $\\theta$. Shaded region $[0.60, 0.65]$ is the recommended operating range.}\n\\label{tab:sensitivity}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Condition} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.65$ & $\\theta{=}0.70$ \\\\\n\\midrule\nQwen2.5-1.5B & 3 & 2 & 2 & 1 \\\\\nPythia-1.4B & 3 & 2 & 2 & 1 \\\\\nOLMo-1B & 2 & 2 & 2 & 1 \\\\\nQwen2.5-1.5B ($T{=}1.2$) & 4 & 3 & 3 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Degradation Ordering (C2)}\n\\label{sec:ordering}\n\nTable~\\ref{tab:degradation} reveals a consistent ordering of feature group saturation across all three model families. Vocabulary diversity features saturate at depth 1 in all models---the narrowing of the lexical distribution is the earliest and most uniform effect of recursive generation. Surprisal dynamics persist to depth 2 in all models, reflecting the slower decay of higher-order conditional statistics. Tail-thinning features show model-dependent behavior: saturation at depth 1 for OLMo-1B (whose smaller capacity produces thinner tails from the outset) but depth 2 for the larger models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Feature group saturation depth by model (depth at which the feature group's discriminative AUC first falls below $\\theta{=}0.60$ for adjacent-generation classification).}\n\\label{tab:degradation}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Feature Group} & \\textbf{Pythia-1.4B} & \\textbf{OLMo-1B} & \\textbf{Qwen2.5-1.5B} \\\\\n\\midrule\nVocabulary diversity & 1 & 1 & 1 \\\\\nSurprisal dynamics & 2 & 2 & 2 \\\\\nTail distribution & 2 & 1 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-model consistency of this ordering is quantified by Kendall's $\\tau$ between feature-level saturation rank vectors (Table~\\ref{tab:kendall}). The mean $\\tau{=}0.84$ indicates that the degradation ordering is a structural property of recursive generation, not a model-specific phenomenon. This has practical implications: vocabulary diversity features alone are sufficient for depth-1 detection but insufficient for finer-grained depth estimation, which requires the slower-decaying surprisal dynamics.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model consistency of degradation ordering (Kendall's $\\tau$).}\n\\label{tab:kendall}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Model Pair} & \\textbf{$\\tau$} \\\\\n\\midrule\nPythia vs.\\ Qwen & 0.87 \\\\\nOLMo vs.\\ Qwen & 0.82 \\\\\nPythia vs.\\ OLMo & 0.84 \\\\\n\\midrule\n\\textbf{Mean} & \\textbf{0.84} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Graduated Filtering (C3)}\n\\label{sec:filtering_results}\n\nTable~\\ref{tab:downstream} presents downstream evaluation results under four data curation strategies. Graduated filtering (3-class: human / gen-1 / gen-2+) outperforms binary filtering by $+2.24$ pp on MMLU and $+2.07$ pp on HellaSwag, both statistically significant ($p{=}0.008$ and $p{=}0.013$ respectively, paired $t$-test across 3 seeds).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Downstream evaluation: continued pretraining performance on MMLU and HellaSwag (percentage points). 30\\% synthetic injection rate. Mean $\\pm$ std over 3 seeds.}\n\\label{tab:downstream}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU (pp)} & \\textbf{HellaSwag (pp)} \\\\\n\\midrule\nNo filter & $25.31 \\pm 0.23$ & $42.67 \\pm 0.19$ \\\\\nBinary & $26.18 \\pm 0.31$ & $43.54 \\pm 0.25$ \\\\\nSurprisal-based & $27.89 \\pm 0.35$ & $45.12 \\pm 0.29$ \\\\\n\\textbf{Graduated (3-class)} & $\\mathbf{28.42 \\pm 0.28}$ & $\\mathbf{45.61 \\pm 0.22}$ \\\\\n\\midrule\n$\\Delta$ (graduated $-$ binary) & $+2.24$ ($p{=}0.008$) & $+2.07$ ($p{=}0.013$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe advantage of graduated filtering derives from its treatment of gen-1 text: rather than discarding it (binary) or retaining it at full weight (no filter), graduated filtering downweights it ($\\alpha{=}0.5$), preserving the substantial information content of first-generation text while attenuating its distributional artifacts.\n\n\\paragraph{Dose-response analysis.} Table~\\ref{tab:dose} shows that the graduated filtering advantage grows monotonically with contamination rate. At 10\\% injection, the advantage is modest ($+0.82$ pp MMLU). At 50\\%---approaching projected web contamination levels---it reaches $+3.41$ pp on MMLU and $+2.89$ pp on HellaSwag. This dose-response relationship implies that the value of depth-aware curation will increase as synthetic text becomes more prevalent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response: graduated vs.\\ binary filtering advantage ($\\Delta$ pp) by synthetic injection rate.}\n\\label{tab:dose}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Injection Rate} & $\\Delta$ \\textbf{MMLU (pp)} & $\\Delta$ \\textbf{HellaSwag (pp)} \\\\\n\\midrule\n10\\% & 0.82 & 0.54 \\\\\n30\\% & 2.24 & 2.07 \\\\\n50\\% & 3.41 & 2.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ablations and Baselines}\n\\label{sec:ablations}\n\n\\paragraph{Classifier architecture.}\nTable~\\ref{tab:classifier} compares CORAL against multinomial classification and ordinal regression. CORAL achieves the best MAE (0.87 vs.\\ 1.03 for multinomial), confirming that exploiting the ordinal structure of depth labels reduces prediction error. The gap is largest in MAE and adjacent accuracy, where ordinal-aware losses penalize distant misclassifications more heavily.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Classifier architecture comparison on depth estimation (Qwen2.5-1.5B, 5-fold CV).}\n\\label{tab:classifier}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Adj.\\ Acc.} \\\\\n\\midrule\nCORAL (ordinal) & \\textbf{0.483} & \\textbf{0.87} & \\textbf{0.821} \\\\\nOrdinal regression & 0.461 & 0.91 & 0.808 \\\\\nMultinomial & 0.472 & 1.03 & 0.784 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Hand-crafted vs.\\ learned features.}\nTable~\\ref{tab:features} shows that our 15D hand-crafted features outperform frozen Qwen2.5-1.5B embeddings (4096D) passed through an MLP, while being 270$\\times$ lower-dimensional and 28$\\times$ faster to train. The frozen embeddings encode primarily semantic content; the few dimensions relevant to depth estimation are diluted by thousands of irrelevant dimensions, leading to overfitting on 5K samples.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hand-crafted (15D) vs.\\ learned (4096D frozen embeddings + MLP) features.}\n\\label{tab:features}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Dim} & \\textbf{GPU-hrs} \\\\\n\\midrule\nFrozen emb.\\ + MLP & 0.452 & 0.94 & 4096 & 2.8 \\\\\nHand-crafted 15D & \\textbf{0.483} & \\textbf{0.87} & 15 & 0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{LLM zero-shot baseline.}\nFrontier LLMs perform near chance on depth estimation (Table~\\ref{tab:llm}). GPT-4o achieves 18.7\\% accuracy (chance: 20\\% for 5-class) with Kendall $\\tau{=}0.11$; Claude 3.5 Sonnet reaches 20.3\\% with $\\tau{=}0.14$. Depth estimation requires population-level statistical features that cannot be assessed from a single text without a reference distribution, explaining why general-purpose LLMs fail at this task.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot depth estimation by frontier LLMs vs.\\ our ordinal classifier.}\n\\label{tab:llm}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nGPT-4o & 0.187 & 1.82 & 0.11 \\\\\nClaude 3.5 Sonnet & 0.203 & 1.71 & 0.14 \\\\\n\\textbf{Our classifier} & \\textbf{0.483} & \\textbf{0.87} & \\textbf{0.52} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Binary detector depth sensitivity.}\n\\label{sec:binary_baseline}\nExisting binary detectors correlate weakly with depth (Table~\\ref{tab:binary}). DivEye achieves Spearman $\\rho{=}0.23$ with true depth; Binoculars achieves $\\rho{=}0.19$. Both excel at 0v1 discrimination (AUC $\\geq 0.92$) but collapse to chance at 1v2 (AUC $\\leq 0.53$). Their confidence scores are optimized for the binary boundary, not for ordinal depth estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Binary detector scores as depth proxies.}\n\\label{tab:binary}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Detector} & \\textbf{Spearman $\\rho$} & \\textbf{$p$-value} & \\textbf{AUC$_{0\\text{v}1}$} & \\textbf{AUC$_{1\\text{v}2}$} \\\\\n\\midrule\nDivEye & 0.23 & 0.001 & 0.94 & 0.53 \\\\\nBinoculars & 0.19 & 0.003 & 0.92 & 0.51 \\\\\nOur features (15D) & --- & --- & 0.996 & 0.696 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\\label{sec:transfer}\n\nTable~\\ref{tab:transfer} shows that classifiers trained on one model's generation chain retain 70--79\\% of their in-domain accuracy when applied to chains from a different model family. Mean transfer retention is 74.6\\%, indicating that depth signals are predominantly model-agnostic. Qwen-trained classifiers transfer best (mean 78.2\\%), likely because the stronger model learns more generalizable decision boundaries.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model transfer accuracy matrix. Diagonal entries (marked *) are in-domain.}\n\\label{tab:transfer}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Train $\\backslash$ Test} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen} & \\textbf{Mean transfer} \\\\\n\\midrule\nPythia & 0.401* & 0.364 & 0.371 & 0.368 \\\\\nOLMo & 0.352 & 0.388* & 0.358 & 0.355 \\\\\nQwen & 0.387 & 0.374 & 0.418* & 0.381 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Ecological Validity}\n\\label{sec:validity}\n\n\\paragraph{Retrain-chain validation.}\nTable~\\ref{tab:retrain} compares prompt-chain generation (our default) with retrain-chain generation (LoRA fine-tuning at each depth). Both yield identical $K^*{=}2$. AUC differences are small ($|\\Delta| \\leq 0.014$), and feature distribution divergence between the two paradigms remains below JSD${=}0.042$ at all depths. Prompt-chains are a valid experimental proxy for the retrain dynamics that drive real-world recursive contamination.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Retrain-chain vs.\\ prompt-chain (Pythia-1.4B, both $K^*{=}2$).}\n\\label{tab:retrain}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Pair} & \\textbf{Retrain AUC} & \\textbf{Prompt AUC} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.987 & 0.991 & $-0.004$ \\\\\n1v2 & 0.658 & 0.672 & $-0.014$ \\\\\n2v3 & 0.563 & 0.571 & $-0.008$ \\\\\n3v4 & 0.529 & 0.533 & $-0.004$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Base vs.\\ Instruct models.}\nComparing Qwen2.5-1.5B base and Instruct variants, both yield $K^*{=}2$. The base model shows slightly stronger depth signal (AUC$_{1\\text{v}2}$: 0.714 vs.\\ 0.696), likely because RLHF alignment compresses output distributions toward a ``preferred mode,'' reducing inter-generational variance. The quantitative but not qualitative difference confirms that our framework applies to both model types.\n\n\\paragraph{Common Crawl validation.}\nAs a naturalistic sanity check, we apply our classifier to Common Crawl 2025/2026 snapshots. Predicted depth correlates negatively with AlignScore (Spearman $\\rho{=}{-}0.31$) and vocabulary richness ($\\rho{=}{-}0.37$), both in the expected direction. The estimated proportion of depth${\\geq}1$ content (18.4\\%) aligns with external estimates of web synthetic text prevalence (15--25\\%).\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{$K^*$ as a fundamental quantity.}\nOur results position $K^*$ not as a classifier performance metric but as an information-theoretic property of the recursive generation channel. Its systematic variation with model scale ($K^*{=}2$ at 1.5B, $K^*{=}3$ at 7B) and decoding entropy ($K^*{=}2$ at $T{=}1.0$, $K^*{=}3$ at $T{=}1.2$) follows directly from the DPI: higher initial mutual information requires more lossy steps to reach the discrimination floor. The stability of $K^*$ across threshold choices $\\theta \\in [0.60, 0.65]$ and its consistency across three model families further support this interpretation.\n\n\\paragraph{Practical implications.}\nFor data curators, $K^*$ provides a concrete answer to ``how much depth resolution is useful?'' At current model scales (1--7B), distinguishing human text from gen-1 and gen-2+ (a 3-class problem) captures essentially all available depth information. This is good news: even coarse ordinal signals yield meaningful downstream improvements, and the 15D feature set required is computationally cheap (0.1 GPU-hours for full training).\n\n\\paragraph{Limitations.}\nOur experiments use models up to 7B parameters and English-only text. $K^*$ at the scale of frontier models (70B+) remains unmeasured, though our results predict it should be higher. The downstream evaluation uses continued pretraining rather than training from scratch, which may underestimate the impact of depth-aware filtering. Our retrain-chain validation uses LoRA rather than full fine-tuning, providing a lower bound on the retrain--prompt divergence.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced the saturation boundary $K^*$ as a fundamental measure of how deeply recursive generation can be discriminated, grounded it in the Data Processing Inequality, and measured it systematically across model families, scales, and decoding strategies. Our key findings are: (1) $K^*{=}2$ at 1--1.5B scale under standard decoding, rising to 3 at 7B or under high-temperature decoding; (2) linguistic features degrade in a universal order, with vocabulary diversity collapsing before distributional dynamics; and (3) even a coarse 3-class depth signal yields 1.5--3.5 pp downstream improvement over binary filtering, with the advantage growing with contamination severity. As recursive synthetic text becomes increasingly prevalent in web corpora, depth-aware data curation will become not just useful but necessary. $K^*$ tells us how much resolution is available; graduated filtering shows how to use it.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nStella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, et~al.\n\\newblock Pythia: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Cao et~al.(2020)]{cao2020coral}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024model}\nElvis Dohmatob, Yunzhen Feng, and Julia Kempe.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Feng et~al.(2024)]{feng2024factuality}\nShangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov.\n\\newblock FactScore: Fine-grained atomic evaluation of factual precision in long form text generation.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nDirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLMs} with Binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJohn Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Qwen Team(2025)]{qwen2025qwen25}\nQwen Team.\n\\newblock Qwen2.5: A party of foundation models.\n\\newblock \\emph{arXiv preprint arXiv:2412.15115}, 2025.\n\n\\bibitem[Raffel et~al.(2020)]{raffel2020c4}\nColin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter~J Liu.\n\\newblock Exploring the limits of transfer learning with a unified text-to-text transformer.\n\\newblock \\emph{JMLR}, 21(140):1--67, 2020.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{tulchinskii2024diveye}\nEduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{NeurIPS}, 2024.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nAlexander Wettig, Aatmik Gupta, Saumya Malik, and Danqi Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024minkpp}\nYijian Zhang, Jiaao Chen, Diyi Yang, and Thomas Hartvigsen.\n\\newblock Min-{K}\\%++: Improved baseline for detecting pre-training data from large language models.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d2d1d853-0f9c-4d64-89e3-83c922c75008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamin…",
  "leafUuid": "8c191948-bce9-4796-bbf8-bc299c6d37da",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260512T200328",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Tool call

_source line 25 · 2026-05-12T20:27:05.598Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DQ2KWf7DR4Z4ZCHnSPbsi3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c191948-bce9-4796-bbf8-bc299c6d37da",
  "isSidechain": false,
  "requestId": "req_011CayJb3D7mdxPBRss6nfna",
  "type": "assistant",
  "uuid": "a615ff29-76f4-4f82-a0ee-19be2f756cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QypM3PBGwDGMwEgtCzCNRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12546,
      "cache_read_input_tokens": 43745,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 43745,
          "cache_creation_input_tokens": 12546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12546
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

_source line 26 · 2026-05-12T20:27:06.617Z_

<details><summary>↩ Tool result · `toolu_01DQ2KWf7DR4Z4ZCHnSPbsi3`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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

Package natbib Warning: Citation `shumailov2024model' on page 1 undefined on in
put line 38.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on
 input line 38.


Package natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in
put line 38.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine
d on input line 59.


Package natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on
 input line 59.


Package natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in
put line 59.


Package natbib Warning: Citation `tulchinskii2024diveye' on page 2 undefined on
 input line 59.


Package natbib Warning: Citation `zhang2024minkpp' on page 2 undefined on input
 line 59.


LaTeX Warning: Reference `sec:binary_baseline' on page 2 undefined on input lin
e 59.


Package natbib Warning: Citation `shumailov2024model' on page 2 undefined on in
put line 62.


Package natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp
ut line 62.


Package natbib Warning: Citation `feng2024factuality' on page 2 undefined on in
put line 65.


Package natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in
put line 65.

[2]

Package natbib Warning: Citation `cao2020coral' on page 3 undefined on input li
ne 110.


Package natbib Warning: Citation `raffel2020c4' on page 3 undefined on input li
ne 132.


Package natbib Warning: Citation `biderman2023pythia' on page 3 undefined on in
put line 134.


Package natbib Warning: Citation `groeneveld2024olmo' on page 3 undefined on in
put line 134.


Package natbib Warning: Citation `qwen2025qwen25' on page 3 undefined on input 
line 134.

[3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 146.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 146.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 146.


LaTeX Warning: Reference `tab:pairwise' on page 4 undefined on input line 149.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 180.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 180.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 180.


LaTeX Warning: Reference `tab:decoding' on page 4 undefined on input line 183.


LaTeX Warning: Reference `tab:7b' on page 4 undefined on input line 203.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 222.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 222.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 222.


LaTeX Warning: Reference `tab:sensitivity' on page 4 undefined on input line 22
5.

[4]

LaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 24
7.


LaTeX Warning: Reference `tab:kendall' on page 5 undefined on input line 265.


LaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 288
.


LaTeX Warning: Reference `tab:dose' on page 5 undefined on input line 311.

[5]

LaTeX Warning: Reference `tab:classifier' on page 6 undefined on input line 333
.


LaTeX Warning: Reference `tab:features' on page 6 undefined on input line 352.


Overfull \hbox (2.95105pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 frozen Qwen2.5-1.5B em-bed-dings (4096D) passed through an ML
P, while be-ing 270$\OMS/cmsy/m/n/10.95 ^^B$ \T1/ptm/m/n/10.95 lower-dimensiona
l

LaTeX Warning: Reference `tab:llm' on page 6 undefined on input line 370.


LaTeX Warning: Reference `tab:binary' on page 6 undefined on input line 390.


LaTeX Warning: Reference `tab:transfer' on page 6 undefined on input line 411.

[6]

LaTeX Warning: Reference `tab:retrain' on page 7 undefined on input line 433.


Overfull \hbox (1.1102pt too wide) in paragraph at lines 433--434
\T1/ptm/m/n/10.95 ($\OMS/cmsy/m/n/10.95 j\OT1/cmr/m/n/10.95 ^^A\OMS/cmsy/m/n/10
.95 j ^^T \OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 014$\T1/p
tm/m/n/10.95 ), and fea-ture dis-tri-bu-tion di-ver-gence be-tween the two para
digms re-mains be-low JSD$[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m
/n/10.95 042$
[7] [8]

Package natbib Warning: There were undefined citations.

[9] [10] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (10 pages, 192148 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2] [3]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 146.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 146.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 146.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 180.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 180.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 180.

[4]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 222.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `superscript' on input line 222.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 222.

[5]
Overfull \hbox (2.95105pt too wide) in paragraph at lines 352--353
\T1/ptm/m/n/10.95 frozen Qwen2.5-1.5B em-bed-dings (4096D) passed through an ML
P, while be-ing 270$\OMS/cmsy/m/n/10.95 ^^B$ \T1/ptm/m/n/10.95 lower-dimensiona
l
[6]
Overfull \hbox (1.1102pt too wide) in paragraph at lines 433--434
\T1/ptm/m/n/10.95 ($\OMS/cmsy/m/n/10.95 j\OT1/cmr/m/n/10.95 ^^A\OMS/cmsy/m/n/10
.95 j ^^T \OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m/n/10.95 014$\T1/p
tm/m/n/10.95 ), and fea-ture dis-tri-bu-tion di-ver-gence be-tween the two para
digms re-mains be-low JSD$[]\OT1/cmr/m/n/10.95 0\OML/cmm/m/it/10.95 :\OT1/cmr/m
/n/10.95 042$
[7] [8] [9] [10] [11] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (11 pages, 195745 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a615ff29-76f4-4f82-a0ee-19be2f756cc3",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "2613154d-3526-4ced-88bf-172fbaf4cc8b",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 38.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 1 undefined on\n input line 38.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in\nput line 38.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine\nd on input line 59.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 59.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 59.\n\n\nPackage natbib Warning: Citation `tulchinskii2024diveye' on page 2 undefined on\n input line 59.\n\n\nPackage natbib Warning: Citation `zhang2024minkpp' on page 2 undefined on input\n line 59.\n\n\nLaTeX Warning: Reference `sec:binary_baseline' on page 2 undefined on input lin\ne 59.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 2 undefined on in\nput line 62.\n\n\nPackage natbib Warning: Citation `dohmatob2024model' on page 2 undefined on inp\nut line 62.\n\n\nPackage natbib Warning: Citation `feng2024factuality' on page 2 undefined on in\nput line 65.\n\n\nPackage natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in\nput line 65.\n\n[2]\n\nPackage natbib Warning: Citation `cao2020coral' on page 3 undefined on input li\nne 110.\n\n\nPackage natbib Warning: Citation `raffel2020c4' on page 3 undefined on input li\nne 132.\n\n\nPackage natbib Warning: Citation `biderman2023pythia' on page 3 undefined on in\nput line 134.\n\n\nPackage natbib Warning: Citation `groeneveld2024olmo' on page 3 undefined on in\nput line 134.\n\n\nPackage natbib Warning: Citation `qwen2025qwen25' on page 3 undefined on input \nline 134.\n\n[3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 146.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 146.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 146.\n\n\nLaTeX Warning: Reference `tab:pairwise' on page 4 undefined on input line 149.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 180.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 180.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 180.\n\n\nLaTeX Warning: Reference `tab:decoding' on page 4 undefined on input line 183.\n\n\nLaTeX Warning: Reference `tab:7b' on page 4 undefined on input line 203.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 222.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 222.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 222.\n\n\nLaTeX Warning: Reference `tab:sensitivity' on page 4 undefined on input line 22\n5.\n\n[4]\n\nLaTeX Warning: Reference `tab:degradation' on page 5 undefined on input line 24\n7.\n\n\nLaTeX Warning: Reference `tab:kendall' on page 5 undefined on input line 265.\n\n\nLaTeX Warning: Reference `tab:downstream' on page 5 undefined on input line 288\n.\n\n\nLaTeX Warning: Reference `tab:dose' on page 5 undefined on input line 311.\n\n[5]\n\nLaTeX Warning: Reference `tab:classifier' on page 6 undefined on input line 333\n.\n\n\nLaTeX Warning: Reference `tab:features' on page 6 undefined on input line 352.\n\n\nOverfull \\hbox (2.95105pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 frozen Qwen2.5-1.5B em-bed-dings (4096D) passed through an ML\nP, while be-ing 270$\\OMS/cmsy/m/n/10.95 ^^B$ \\T1/ptm/m/n/10.95 lower-dimensiona\nl\n\nLaTeX Warning: Reference `tab:llm' on page 6 undefined on input line 370.\n\n\nLaTeX Warning: Reference `tab:binary' on page 6 undefined on input line 390.\n\n\nLaTeX Warning: Reference `tab:transfer' on page 6 undefined on input line 411.\n\n[6]\n\nLaTeX Warning: Reference `tab:retrain' on page 7 undefined on input line 433.\n\n\nOverfull \\hbox (1.1102pt too wide) in paragraph at lines 433--434\n\\T1/ptm/m/n/10.95 ($\\OMS/cmsy/m/n/10.95 j\\OT1/cmr/m/n/10.95 ^^A\\OMS/cmsy/m/n/10\n.95 j ^^T \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 014$\\T1/p\ntm/m/n/10.95 ), and fea-ture dis-tri-bu-tion di-ver-gence be-tween the two para\ndigms re-mains be-low JSD$[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m\n/n/10.95 042$\n[7] [8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] [10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 192148 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2] [3]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 146.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 146.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 146.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 180.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 180.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 180.\n\n[4]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 222.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `superscript' on input line 222.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 222.\n\n[5]\nOverfull \\hbox (2.95105pt too wide) in paragraph at lines 352--353\n\\T1/ptm/m/n/10.95 frozen Qwen2.5-1.5B em-bed-dings (4096D) passed through an ML\nP, while be-ing 270$\\OMS/cmsy/m/n/10.95 ^^B$ \\T1/ptm/m/n/10.95 lower-dimensiona\nl\n[6]\nOverfull \\hbox (1.1102pt too wide) in paragraph at lines 433--434\n\\T1/ptm/m/n/10.95 ($\\OMS/cmsy/m/n/10.95 j\\OT1/cmr/m/n/10.95 ^^A\\OMS/cmsy/m/n/10\n.95 j ^^T \\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m/n/10.95 014$\\T1/p\ntm/m/n/10.95 ), and fea-ture dis-tri-bu-tion di-ver-gence be-tween the two para\ndigms re-mains be-low JSD$[]\\OT1/cmr/m/n/10.95 0\\OML/cmm/m/it/10.95 :\\OT1/cmr/m\n/n/10.95 042$\n[7] [8] [9] [10] [11] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr\n7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 195745 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a615ff29-76f4-4f82-a0ee-19be2f756cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamin…",
  "leafUuid": "2613154d-3526-4ced-88bf-172fbaf4cc8b",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260512T200328",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Assistant

_source line 29 · 2026-05-12T20:27:14.288Z_

Label references changed between runs. Running a third pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2613154d-3526-4ced-88bf-172fbaf4cc8b",
  "isSidechain": false,
  "requestId": "req_011CayJbSe21hARuUcae8Ppr",
  "type": "assistant",
  "uuid": "8ccf3a67-bc43-434a-9b84-da59aaa708a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHiDP6Pi6vuuxEJ3ngSodi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7734,
      "cache_read_input_tokens": 56291,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 56291,
          "cache_creation_input_tokens": 7734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7734
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

_source line 30 · 2026-05-12T20:27:17.321Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ELXL4qAoLhfEAup8BmuCv8`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third pdflatex pass to resolve labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ccf3a67-bc43-434a-9b84-da59aaa708a8",
  "isSidechain": false,
  "requestId": "req_011CayJbSe21hARuUcae8Ppr",
  "type": "assistant",
  "uuid": "91956060-111a-40ad-bca2-70de1165244e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHiDP6Pi6vuuxEJ3ngSodi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7734,
      "cache_read_input_tokens": 56291,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 56291,
          "cache_creation_input_tokens": 7734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7734
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

_source line 31 · 2026-05-12T20:27:17.797Z_

<details><summary>↩ Tool result · `toolu_01ELXL4qAoLhfEAup8BmuCv8`</summary>

```text
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (11 pages, 195745 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91956060-111a-40ad-bca2-70de1165244e",
  "isSidechain": false,
  "promptId": "68ef8d46-8f84-4b93-a9cb-b320943019da",
  "type": "user",
  "uuid": "111efec9-1a7c-4bdb-9e62-eb5cb3009916",
  "toolUseResult": {
    "stdout": "xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 195745 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "91956060-111a-40ad-bca2-70de1165244e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-12T20:27:17.799Z_

```json
{
  "parentUuid": "111efec9-1a7c-4bdb-9e62-eb5cb3009916",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7a030e01-3244-4882-9277-0ecf8fd65009",
  "timestamp": "2026-05-12T20:27:17.799Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-12T20:27:28.740Z_

编译成功，11 页 PDF。输出位于 `artifacts/dream_reports/dream_20260512T200328/best/paper.pdf`。

论文包含完整结构：Abstract、Introduction（3 条 contribution）、Related Work、Method（DPI 理论 + 15D 特征 + CORAL 分类器 + graduated filtering）、Experiments（$K^*$ 跨模型/解码/scale、sensitivity analysis、degradation ordering、downstream filtering + dose-response、classifier/feature/LLM/binary-detector ablation、cross-model transfer、ecological validity）、Discussion、Conclusion、14 条参考文献。所有定量数据直接来自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a030e01-3244-4882-9277-0ecf8fd65009",
  "isSidechain": false,
  "requestId": "req_011CayJcGQ9PTiQESoTJGLzj",
  "type": "assistant",
  "uuid": "35b66035-325a-49a1-94da-c09463375960",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/best",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017YeaGXw5V3GG67qEqnghcw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 64025,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 64025,
          "cache_creation_input_tokens": 346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 346
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamin…",
  "leafUuid": "35b66035-325a-49a1-94da-c09463375960",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260512T200328",
  "sessionId": "15869c0c-9668-4be3-a2a7-f75590b57af9"
}
```

---
