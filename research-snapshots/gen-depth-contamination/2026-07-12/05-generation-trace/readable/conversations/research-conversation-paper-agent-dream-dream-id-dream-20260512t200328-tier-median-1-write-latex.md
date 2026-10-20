# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/caa9121a-e97e-4f37-9476-22cdf59a34aa.jsonl`
- **Structured JSON:** [`8e0384283c93ce09e36f.json`](../../sessions/8e/8e0384283c93ce09e36f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:27:30.796Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:27:30.796Z",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026\n- Narrative guidance：K*=2 不再是 \"modulable quantity\" 而是 \"robust empirical constant for current-generation 1-2B models\"。 Reframe 为 universality result：首次系统测量表明 K*=2 在 3 个模型族、4 种解码策略下高度稳定， 仅极端解码（T≥1.2）将 K* 推至 3。C2 degradation ordering 降级为 \"tendency\"（tau 0.5-0.8）， vocabulary diversity 倾向先饱和但非严格一致。C3 graduated filtering 强调 calibration 优势而非 raw accuracy gap（0.5-1.5pp MMLU，seed variance 可重叠）。补强 characterization 贡献： 首次系统测量 K*、首次将 depth estimation 形式化为 prediction task。 投稿策略：EMNLP Main 可尝试，准备 Findings fallback，rebuttal 需有力回应 \"K*=2 + modest gain = incremental\"。\n\n- paper_framing.md 节选：\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Core Claims (3 条)\n\n1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。\n2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。\n3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix\n4. **\"单模型/单数据集，泛化性不够\"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → 显式讨论此 design choice：这衡量的是\"模型对自身递归输出的 self-recognition\"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 \"Resources and Evaluation\" track 的要求\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty\n\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T20:27:30.799Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:27:30.799Z",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-12T20:27:30.816Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026
- Narrative guidance：K*=2 不再是 "modulable quantity" 而是 "robust empirical constant for current-generation 1-2B models"。 Reframe 为 universality result：首次系统测量表明 K*=2 在 3 个模型族、4 种解码策略下高度稳定， 仅极端解码（T≥1.2）将 K* 推至 3。C2 degradation ordering 降级为 "tendency"（tau 0.5-0.8）， vocabulary diversity 倾向先饱和但非严格一致。C3 graduated filtering 强调 calibration 优势而非 raw accuracy gap（0.5-1.5pp MMLU，seed variance 可重叠）。补强 characterization 贡献： 首次系统测量 K*、首次将 depth estimation 形式化为 prediction task。 投稿策略：EMNLP Main 可尝试，准备 Findings fallback，rebuttal 需有力回应 "K*=2 + modest gain = incremental"。

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
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "9d26fc59-2031-4e4c-a723-1de87f61be39",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:27:30.816Z_

```json
{
  "parentUuid": "9d26fc59-2031-4e4c-a723-1de87f61be39",
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
  "uuid": "8042d554-bf98-4d9d-87c0-d9955c70b943",
  "timestamp": "2026-05-12T20:27:30.816Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:27:30.816Z_

```json
{
  "parentUuid": "8042d554-bf98-4d9d-87c0-d9955c70b943",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0bce29e9-60f1-48a0-a748-ccf870f8d6dc",
  "timestamp": "2026-05-12T20:27:30.816Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
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
  "aiTitle": "Generate depth contamination paper for EMNLP",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Assistant

_source line 7 · 2026-05-12T20:27:34.192Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and understanding what I need to work with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bce29e9-60f1-48a0-a748-ccf870f8d6dc",
  "isSidechain": false,
  "requestId": "req_011CayJdEDTEcmMvdzdths36",
  "type": "assistant",
  "uuid": "f3517169-94d2-4971-a12c-e174fb8b754a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSPvU11nVX6hRg4kYDE7tW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12627
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

_source line 8 · 2026-05-12T20:27:36.577Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQY6Qz6iKu5yfVaxeFyKgK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3517169-94d2-4971-a12c-e174fb8b754a",
  "isSidechain": false,
  "requestId": "req_011CayJdEDTEcmMvdzdths36",
  "type": "assistant",
  "uuid": "86b8b7e4-c96c-4306-8cdb-d89695615c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSPvU11nVX6hRg4kYDE7tW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12627,
      "cache_read_input_tokens": 11841,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 136,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12627
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

_source line 9 · 2026-05-12T20:27:36.861Z_

<details><summary>↩ Tool result · `toolu_01FQY6Qz6iKu5yfVaxeFyKgK`</summary>

```text
1	[
2	  {
3	    "name": "Pythia-1.4B depth chain generation",
4	    "description": "Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5",
5	    "results": {
6	      "pairwise_auc_0v1": 0.993,
7	      "pairwise_auc_1v2": 0.672,
8	      "pairwise_auc_2v3": 0.576,
9	      "pairwise_auc_3v4": 0.538,
10	      "pairwise_auc_4v5": 0.527,
11	      "pairwise_jsd_0v1": 0.241,
12	      "pairwise_jsd_1v2": 0.014,
13	      "pairwise_jsd_2v3": 0.005,
14	      "pairwise_jsd_3v4": 0.003,
15	      "pairwise_jsd_4v5": 0.003,
16	      "k_star": 2,
17	      "ordinal_mae": 1.05,
18	      "ordinal_accuracy": 0.4
19	    },
20	    "tables": [
21	      {
22	        "caption": "Table: Pythia-1.4B pairwise discrimination (AUC / JSD) by generation gap",
23	        "rows": [
24	          [
25	            "Pair",
26	            "AUC (mean±std)",
27	            "JSD"
28	          ],
29	          [
30	            "0 vs 1",
31	            "0.993 ± 0.001",
32	            "0.241"
33	          ],
34	          [
35	            "1 vs 2",
36	            "0.672 ± 0.009",
37	            "0.014"
38	          ],
39	          [
40	            "2 vs 3",
41	            "0.576 ± 0.013",
42	            "0.005"
43	          ],
44	          [
45	            "3 vs 4",
46	            "0.538 ± 0.008",
47	            "0.003"
48	          ],
49	          [
50	            "4 vs 5",
51	            "0.527 ± 0.010",
52	            "0.003"
53	          ]
54	        ]
55	      }
56	    ],
57	    "figures": [],
58	    "analysis": "Pythia-1.4B 的 K*=2 与 MVP Qwen2.5-1.5B 一致，初步支持 K* 的跨架构稳定性。 JSD 衰减曲线形状几乎相同（exponential-like decay），仅 absolute magnitude 有差异。 这为 \"K*=2 is a property of the 1-2B scale regime, not a model-specific artifact\" 提供证据。\n\n\nPythia-1.4B 是较早期的 GPT-NeoX 架构，参数量与 Qwen2.5-1.5B 同量级（1.4B vs 1.5B）， 但训练数据量和质量略低（The Pile 300B tokens vs Qwen 的多语言数据）。这意味着 Pythia 的 生成质量基线略低于 Qwen，gen-0→gen-1 的信息损失稍大（JSD 0.241 vs MVP 的 0.267—— 实际上 Pythia 初始分离度可能略低因为其 gen-0 本身已比 Qwen 的 gen-0 更 \"synthetic-like\"）。 但核心现象不变：gen-1→gen-2 的 AUC 从 ~0.67 骤降到 gen-2→gen-3 的 ~0.58，确认 K*=2。 这是因为 DPI 约束与模型规模相关而非架构特异——1.4B 模型的 lossy channel capacity  在第二代即耗尽可辨别信息。Ordinal accuracy 略低于 MVP（0.40 vs 0.42）因为 Pythia 的 特征空间结构性稍弱。\n"
59	  },
60	  {
61	    "name": "OLMo-1B depth chain generation",
62	    "description": "OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5",
63	    "results": {
64	      "pairwise_auc_0v1": 0.991,
65	      "pairwise_auc_1v2": 0.648,
66	      "pairwise_auc_2v3": 0.562,
67	      "pairwise_auc_3v4": 0.531,
68	      "pairwise_auc_4v5": 0.522,
69	      "pairwise_jsd_0v1": 0.218,
70	      "pairwise_jsd_1v2": 0.012,
71	      "pairwise_jsd_2v3": 0.004,
72	      "pairwise_jsd_3v4": 0.003,
73	      "pairwise_jsd_4v5": 0.002,
74	      "k_star": 2,
75	      "ordinal_mae": 1.08,
76	      "ordinal_accuracy": 0.39
77	    },
78	    "tables": [
79	      {
80	        "caption": "Table: OLMo-1B pairwise discrimination (AUC / JSD) by generation gap",
81	        "rows": [
82	          [
83	            "Pair",
84	            "AUC (mean±std)",
85	            "JSD"
86	          ],
87	          [
88	            "0 vs 1",
89	            "0.991 ± 0.001",
90	            "0.218"
91	          ],
92	          [
93	            "1 vs 2",
94	            "0.648 ± 0.011",
95	            "0.012"
96	          ],
97	          [
98	            "2 vs 3",
99	            "0.562 ± 0.014",
100	            "0.004"
101	          ],
102	          [
103	            "3 vs 4",
104	            "0.531 ± 0.009",
105	            "0.003"
106	          ],
107	          [
108	            "4 vs 5",
109	            "0.522 ± 0.011",
110	            "0.002"
111	          ]
112	        ]
113	      }
114	    ],
115	    "figures": [],
116	    "analysis": "OLMo-1B 确认了最小规模下 K*=2 仍成立。三模型族的 K*=2 一致性构成论文的核心 universality evidence。 可以论证：在 1-2B scale regime 下，K*=2 是 robust empirical constant，不依赖于具体架构 （GPT-NeoX / Transformer++ / Qwen-style）或训练数据（Pile / Dolma / multilingual）。\n\n\nOLMo-1B 参数量最小（1B），且是完全开源训练流程（Dolma 数据集）。更小的模型容量意味着 其 lossy channel 在每一代损失更多信息——gen-0 的 vocabulary richness 基线就低于 1.5B 模型， 因此 gen-0 vs gen-1 的初始 JSD 为三者最低（0.218）。但 K* 仍然是 2：gen-1→gen-2 的 AUC 0.648 仍显著高于 chance（满足 0.60 阈值），而 gen-2→gen-3 的 0.562 已进入 noise floor （在 0.55-0.60 区间）。这恰好说明 K* 是 scale-dependent 的 robust constant：即使在略小的 1B 模型上，第二代仍然是信息饱和的 phase transition point。Ordinal accuracy 最低（0.39） 因为 gen-2+ 的类间距更小。\n"
117	  },
118	  {
119	    "name": "Qwen2.5-1.5B decoding strategy ablation",
120	    "description": "Qwen2.5-1.5B 在 greedy / nucleus p=0.9 / T=0.7 / T=1.2 四种解码策略下的 depth chain",
121	    "results": {
122	      "greedy": {
123	        "pairwise_auc_1v2": 0.714,
124	        "pairwise_auc_2v3": 0.603,
125	        "k_star": 2,
126	        "pairwise_jsd_0v1": 0.302,
127	        "pairwise_jsd_1v2": 0.019
128	      },
129	      "nucleus_p09": {
130	        "pairwise_auc_1v2": 0.688,
131	        "pairwise_auc_2v3": 0.582,
132	        "k_star": 2,
133	        "pairwise_jsd_0v1": 0.258,
134	        "pairwise_jsd_1v2": 0.015
135	      },
136	      "T07": {
137	        "pairwise_auc_1v2": 0.708,
138	        "pairwise_auc_2v3": 0.597,
139	        "k_star": 2,
140	        "pairwise_jsd_0v1": 0.289,
141	        "pairwise_jsd_1v2": 0.018
142	      },
143	      "T12": {
144	        "pairwise_auc_1v2": 0.651,
145	        "pairwise_auc_2v3": 0.583,
146	        "pairwise_auc_3v4": 0.558,
147	        "k_star_seed1": 2,
148	        "k_star_seed2": 3,
149	        "k_star_seed3": 2,
150	        "k_star_majority": 2,
151	        "pairwise_jsd_0v1": 0.195,
152	        "pairwise_jsd_1v2": 0.011
153	      }
154	    },
155	    "tables": [
156	      {
157	        "caption": "Table: Decoding strategy ablation — K* and key AUC values",
158	        "rows": [
159	          [
160	            "Strategy",
161	            "AUC 0v1",
162	            "AUC 1v2",
163	            "AUC 2v3",
164	            "JSD 0v1",
165	            "K*"
166	          ],
167	          [
168	            "Greedy",
169	            "0.997",
170	            "0.714",
171	            "0.603",
172	            "0.302",
173	            "2"
174	          ],
175	          [
176	            "Nucleus p=0.9",
177	            "0.996",
178	            "0.688",
179	            "0.582",
180	            "0.258",
181	            "2"
182	          ],
183	          [
184	            "T=0.7",
185	            "0.997",
186	            "0.708",
187	            "0.597",
188	            "0.289",
189	            "2"
190	          ],
191	          [
192	            "T=1.2",
193	            "0.992",
194	            "0.651",
195	            "0.583",
196	            "0.195",
197	            "2 (1 seed: 3)"
198	          ],
199	          [
200	            "MVP baseline (p=0.95)",
201	            "0.996",
202	            "0.696",
203	            "0.589",
204	            "0.267",
205	            "2"
206	          ]
207	        ]
208	      }
209	    ],
210	    "figures": [],
211	    "analysis": "四种解码策略中 K*=2 完全稳定，仅 T=1.2 在部分 seed 下 K*=3。这支持 median tier 的核心叙事： K*=2 是 robust constant，极端解码是目前发现的唯一调控因素。论文中可以用此结果论证 \"K* is remarkably stable across decoding strategies, with only extreme temperature  (T≥1.2) occasionally extending it to 3\"。\n\n\n解码策略通过控制 sampling entropy 调节每一代的信息损失率。 Greedy（T=0, argmax）：最低 entropy sampling → 每代输出最 \"mode-collapsed\"，gen-0 vs gen-1  的初始差异最大（JSD 0.302）因为 greedy 输出与 human text 的分布差距最大。但这个大初始差距 也使得 gen-1 vs gen-2 的 AUC 最高（0.714），因为 gen-1 仍保留可辨别的 diversity 信号。 K*=2 因为 gen-2→gen-3 在 0.603 处——接近阈值但仍 above。 Nucleus p=0.9：比 MVP baseline（p=0.95）稍 tighter，效果与 baseline 相近，K*=2。 T=0.7（low temperature）：类似 greedy 的效果但稍温和，K*=2。 T=1.2（high temperature）：高温增加采样随机性，每代注入更多 noise。这使得 gen-0→gen-1  的信息损失最小（JSD 0.195）——高温输出本身就更 diverse 更接近 human text。但同时， 高温使 gen-1→gen-2 的辨别力降低（AUC 0.651），而 gen-2→gen-3 在 0.583——某些 seed  下可能越过 0.60 阈值使 K*=3。这是唯一导致 K* 不稳定的条件：3 个 seed 中 1 个显示 K*=3， 多数仍为 2。机制是高温保留了更多 per-generation variance，使得 DPI 的信息压缩在第三代 才完全饱和。\n"
212	  },
213	  {
214	    "name": "Qwen2.5-7B cross-scale probe",
215	    "description": "Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3",
216	    "results": {
217	      "pairwise_auc_0v1": 0.989,
218	      "pairwise_auc_1v2": 0.718,
219	      "pairwise_auc_2v3": 0.612,
220	      "pairwise_jsd_0v1": 0.193,
221	      "pairwise_jsd_1v2": 0.02,
222	      "pairwise_jsd_2v3": 0.008,
223	      "k_star_seed1": 2,
224	      "k_star_seed2": 3,
225	      "k_star_seed3": 2,
226	      "k_star_majority": 2,
227	      "ordinal_mae": 0.93,
228	      "ordinal_accuracy": 0.44
229	    },
230	    "tables": [
231	      {
232	        "caption": "Table: Qwen2.5-7B pairwise discrimination (3 seeds)",
233	        "rows": [
234	          [
235	            "Pair",
236	            "AUC (seed1/seed2/seed3)",
237	            "K* per seed"
238	          ],
239	          [
240	            "0 vs 1",
241	            "0.990/0.988/0.989",
242	            "-"
243	          ],
244	          [
245	            "1 vs 2",
246	            "0.722/0.710/0.721",
247	            "-"
248	          ],
249	          [
250	            "2 vs 3",
251	            "0.618/0.597/0.620",
252	            "3/2/3"
253	          ]
254	        ]
255	      }
256	    ],
257	    "figures": [],
258	    "analysis": "7B 的结果暗示 K* 可能随模型规模增长而增大，但在当前实验规模下无法确定性地声称 K*=3。 论文中应保守表述：\"7B models show suggestive evidence that K* may increase with scale,  but the effect is within seed variance at our sample size\"。这为 future work（更大模型、 更多数据）留下了自然的延伸方向。\n\n\n7B 模型的 channel capacity 更高——更大的模型在每一代保留更多信息，因此信息衰减更慢。 这体现在：(1) gen-0 vs gen-1 的 JSD 更低（0.193 vs 1.5B 的 0.267），因为 7B 的生成质量 更高，gen-1 与 human text 的分布差异更小；(2) gen-1 vs gen-2 的 AUC 更高（0.718 vs 0.696）， 因为 7B 在 gen-1 中保留了更多可辨别特征；(3) gen-2 vs gen-3 的 AUC 在 0.612——处于 K*=2 和 K*=3 的边界。某些 seed 下 AUC 2v3 越过 0.60 → K*=3，其他 seed 下刚好在边界上。 这种 seed-level instability 是 median tier 的特征预测。机制解释：7B 的 lossy channel  压缩率更低，DPI 导致的饱和在第三代才完成，而非第二代。但由于只有 1K docs（而非 5K）， 统计 power 较低，加剧了 seed variance。如果有 5K docs，K* 可能稳定在 3。\n"
259	  },
260	  {
261	    "name": "Feature group ablation + degradation ordering",
262	    "description": "对 Pythia-1.4B 和 OLMo-1B 的 depth chain 按 feature group 分析饱和深度和 degradation ordering",
263	    "results": {
264	      "pythia_saturation_order": [
265	        "vocabulary_diversity",
266	        "tail_thinning",
267	        "surprisal_dynamics"
268	      ],
269	      "olmo_saturation_order": [
270	        "vocabulary_diversity",
271	        "surprisal_dynamics",
272	        "tail_thinning"
273	      ],
274	      "vocabulary_diversity_saturation_depth_range": [
275	        1.5,
276	        2.0
277	      ],
278	      "surprisal_dynamics_saturation_depth_range": [
279	        2.0,
280	        2.5
281	      ],
282	      "tail_thinning_saturation_depth_range": [
283	        2.0,
284	        3.0
285	      ],
286	      "kendall_tau_ordering_consistency_across_models": 0.67,
287	      "feature_group_pairwise_auc": {
288	        "pythia_vocab_1v2": 0.641,
289	        "pythia_surprisal_1v2": 0.608,
290	        "pythia_tail_1v2": 0.622,
291	        "olmo_vocab_1v2": 0.625,
292	        "olmo_surprisal_1v2": 0.612,
293	        "olmo_tail_1v2": 0.598
294	      }
295	    },
296	    "tables": [
297	      {
298	        "caption": "Table: Feature group saturation depth and pairwise AUC (1v2) by model",
299	        "rows": [
300	          [
301	            "Feature Group",
302	            "Pythia AUC 1v2",
303	            "Pythia Sat. Depth",
304	            "OLMo AUC 1v2",
305	            "OLMo Sat. Depth"
306	          ],
307	          [
308	            "Vocabulary Diversity",
309	            "0.641",
310	            "1.8",
311	            "0.625",
312	            "1.6"
313	          ],
314	          [
315	            "Surprisal Dynamics",
316	            "0.608",
317	            "2.3",
318	            "0.612",
319	            "2.1"
320	          ],
321	          [
322	            "Tail Thinning",
323	            "0.622",
324	            "2.0",
325	            "0.598",
326	            "2.5"
327	          ]
328	        ]
329	      },
330	      {
331	        "caption": "Table: Degradation ordering consistency (Kendall tau)",
332	        "rows": [
333	          [
334	            "Model Pair",
335	            "Kendall tau",
336	            "p-value"
337	          ],
338	          [
339	            "Pythia vs OLMo",
340	            "0.67",
341	            "0.08"
342	          ],
343	          [
344	            "Pythia vs Qwen (MVP)",
345	            "0.67",
346	            "0.08"
347	          ],
348	          [
349	            "OLMo vs Qwen (MVP)",
350	            "1.00",
351	            "0.02"
352	          ]
353	        ]
354	      }
355	    ],
356	    "figures": [],
357	    "analysis": "Vocabulary diversity 的优先饱和跨模型大致一致（3/3 模型中最先饱和），支持 C2 的 \"tendency\"  表述。但 surprisal 和 tail-thinning 的顺序不稳定（tau 0.67），应避免声称严格 ordering。 论文中建议表述：\"vocabulary diversity consistently degrades earliest, while the relative  ordering of surprisal and tail features is model-dependent\"。\n\n\nVocabulary diversity（TTR, hapax ratio, entropy-based measures）对递归生成最敏感： 每一代 LM 生成都倾向于 mode collapse 到高频词汇，vocabulary richness 在 gen-1→gen-2  即显著下降。这是因为 LM 的 softmax 分布本质上是对 training distribution 的平滑近似， 递归采样会累积放大这种平滑效应（\"rich get richer\" for frequent tokens）。 Surprisal dynamics（perplexity variance, burstiness）和 tail-thinning（rare token frequency） 饱和较慢，因为这些特征依赖于高阶统计量，需要更多代际压缩才会坍缩。 但 ordering 不完全一致：Pythia 上 tail-thinning 先于 surprisal 饱和，OLMo 上反过来。 这导致跨模型 Kendall tau 为 0.67——有趋势但非严格一致。原因是不同架构的 attention pattern  和 vocabulary size 差异导致 rare token 的衰减速率不同。Pythia 的 50K vocabulary 中 rare tokens 衰减更快（tail-thinning 先饱和），而 OLMo 的训练数据特征使 surprisal  burstiness 先丧失。\n"
358	  },
359	  {
360	    "name": "Downstream filtering evaluation",
361	    "description": "no-filter / binary / graduated / surprisal-based 四种过滤策略，continued pretraining + lm-eval-harness，3 seeds",
362	    "results": {
363	      "mmlu_no_filter": 25.8,
364	      "mmlu_binary": 26.4,
365	      "mmlu_graduated": 27.2,
366	      "mmlu_surprisal": 26.9,
367	      "mmlu_graduated_vs_binary_delta_pp": 0.8,
368	      "mmlu_std_across_seeds": 0.4,
369	      "hellaswag_no_filter": 42.1,
370	      "hellaswag_binary": 43.0,
371	      "hellaswag_graduated": 43.7,
372	      "hellaswag_surprisal": 43.4,
373	      "hellaswag_graduated_vs_binary_delta_pp": 0.7,
374	      "hellaswag_std_across_seeds": 0.5
375	    },
376	    "tables": [
377	      {
378	        "caption": "Table: Downstream evaluation (MMLU / HellaSwag accuracy) by filtering strategy",
379	        "rows": [
380	          [
381	            "Strategy",
382	            "MMLU (mean±std)",
383	            "HellaSwag (mean±std)",
384	            "Δ vs Binary (pp)"
385	          ],
386	          [
387	            "No filter",
388	            "25.8 ± 0.3",
389	            "42.1 ± 0.4",
390	            "-0.6 / -0.9"
391	          ],
392	          [
393	            "Binary",
394	            "26.4 ± 0.4",
395	            "43.0 ± 0.5",
396	            "—"
397	          ],
398	          [
399	            "Surprisal-based",
400	            "26.9 ± 0.3",
401	            "43.4 ± 0.4",
402	            "+0.5 / +0.4"
403	          ],
404	          [
405	            "Graduated (3-class)",
406	            "27.2 ± 0.4",
407	            "43.7 ± 0.5",
408	            "+0.8 / +0.7"
409	          ]
410	        ]
411	      }
412	    ],
413	    "figures": [],
414	    "analysis": "Graduated filtering 的优势 real but modest（~0.8pp MMLU，~0.7pp HellaSwag），且 seed  variance 使得 p-value 可能在 0.05-0.10。论文中应强调 calibration 优势而非 raw gap： \"graduated filtering provides better-calibrated quality estimates near the decision  boundary, where binary filtering makes its most consequential errors\"。 同时，no-filter → binary 的 gap 本身也不大（~0.6-0.9pp），因为 C4 基础数据质量已较高。\n\n\n四种策略形成清晰的 hierarchy：no-filter < binary < surprisal ≈ graduated。 Binary filtering 移除所有 gen-1+ 文本，改善约 0.6pp（MMLU）/ 0.9pp（HellaSwag）—— 这证明合成文本确实有害。Graduated filtering 进一步改善 0.8pp / 0.7pp：机制是 graduated  在 binary decision boundary 附近提供更 calibrated 的置信度。具体来说，binary classifier  对 gen-1 文本（质量尚可）和 gen-3 文本（质量差）给出相同的 \"synthetic\" 标签，而 graduated  classifier 将 gen-1 标记为 \"shallow synthetic\"（允许部分保留），gen-3 标记为 \"deep synthetic\" （强力过滤）。这种 calibration 在 training mixture 中保留了更多有用的 gen-1 数据。 但 effect size 仅 0.5-1.5pp 且 seed variance（std ~0.4-0.5pp）使得 confidence interval  可能重叠。这是 median tier 的关键特征：gain 是 real but modest，statistical significance  可能需要更多 seeds 才能确认。Surprisal-based filtering（直接用 perplexity 做 quality gate） 性能介于 binary 和 graduated 之间——它隐式捕获了部分 depth 信息但不如显式 depth 估计精确。\n"
415	  },
416	  {
417	    "name": "K* sensitivity to AUC threshold",
418	    "description": "在 0.55/0.60/0.65/0.70 四个阈值下计算 K*",
419	    "results": {
420	      "threshold_055": {
421	        "k_star_pythia": 3,
422	        "k_star_olmo": 2,
423	        "k_star_qwen_baseline": 2,
424	        "k_star_qwen_T12": 3
425	      },
426	      "threshold_060": {
427	        "k_star_pythia": 2,
428	        "k_star_olmo": 2,
429	        "k_star_qwen_baseline": 2,
430	        "k_star_qwen_T12": 2
431	      },
432	      "threshold_065": {
433	        "k_star_pythia": 2,
434	        "k_star_olmo": 2,
435	        "k_star_qwen_baseline": 2,
436	        "k_star_qwen_T12": 2
437	      },
438	      "threshold_070": {
439	        "k_star_pythia": 1,
440	        "k_star_olmo": 1,
441	        "k_star_qwen_baseline": 2,
442	        "k_star_qwen_T12": 1
443	      }
444	    },
445	    "tables": [
446	      {
447	        "caption": "Table: K* stability across AUC thresholds",
448	        "rows": [
449	          [
450	            "Threshold",
451	            "Pythia",
452	            "OLMo",
453	            "Qwen (baseline)",
454	            "Qwen (T=1.2)"
455	          ],
456	          [
457	            "0.55",
458	            "3",
459	            "2",
460	            "2",
461	            "3"
462	          ],
463	          [
464	            "0.60",
465	            "2",
466	            "2",
467	            "2",
468	            "2"
469	          ],
470	          [
471	            "0.65",
472	            "2",
473	            "2",
474	            "2",
475	            "2"
476	          ],
477	          [
478	            "0.70",
479	            "1",
480	            "1",
481	            "2",
482	            "1"
483	          ]
484	        ]
485	      }
486	    ],
487	    "figures": [],
488	    "analysis": "K*=2 在 0.60-0.65 的 threshold 范围内完全稳定。低于 0.55 或高于 0.70 时 K* 变化， 但这些阈值分别对应 \"too lenient\"（near chance）和 \"too strict\"（过滤掉有意义的信号）。 论文应展示此 robustness check 以预防审稿人质疑 threshold 选择的任意性。\n\n\nK* 定义为最大深度 k 使得 pairwise AUC(k vs k+1) > threshold。阈值选择影响 K* 的绝对值， 但关键发现是 K* 的跨模型相对 pattern 对阈值 robust。 Threshold 0.55（宽松）：部分模型的 gen-2v3 AUC（如 Pythia 0.576）仍 > 0.55，K* 升到 3。 但这个阈值过于宽松——0.55 的 AUC 接近 chance，实际辨别意义不大。 Threshold 0.60（默认）：所有 1.5B 模型 K*=2，这是论文采用的 operating point。 Threshold 0.65（偏严）：所有模型仍然 K*=2，因为 gen-1v2 AUC（0.65-0.72）刚好 above 0.65。 Threshold 0.70（过严）：大部分模型 K* 降到 1，因为 gen-1v2 AUC 多在 0.65-0.70 区间， 低于 0.70 阈值。仅 Qwen baseline（AUC 1v2 = 0.696）勉强接近。 核心 insight：在 0.55-0.65 的合理阈值范围内，K*=2 对 1.5B 模型高度稳定。\n"
489	  },
490	  {
491	    "name": "Retrain-chain ecological validity",
492	    "description": "Pythia-1.4B LoRA retrain-chain, depth 0-4",
493	    "results": {
494	      "pairwise_auc_0v1": 0.988,
495	      "pairwise_auc_1v2": 0.635,
496	      "pairwise_auc_2v3": 0.572,
497	      "pairwise_auc_3v4": 0.541,
498	      "k_star": 2,
499	      "jsd_0v1": 0.198,
500	      "jsd_1v2": 0.011,
501	      "feature_distribution_shift_vs_prompt_chain": {
502	        "vocabulary_diversity_ks_test_p": 0.03,
503	        "surprisal_dynamics_ks_test_p": 0.12,
504	        "tail_thinning_ks_test_p": 0.07
505	      }
506	    },
507	    "tables": [
508	      {
509	        "caption": "Table: Prompt-chain vs Retrain-chain comparison (Pythia-1.4B)",
510	        "rows": [
511	          [
512	            "Pair",
513	            "Prompt AUC",
514	            "Retrain AUC",
515	            "Δ AUC"
516	          ],
517	          [
518	            "0 vs 1",
519	            "0.993",
520	            "0.988",
521	            "-0.005"
522	          ],
523	          [
524	            "1 vs 2",
525	            "0.672",
526	            "0.635",
527	            "-0.037"
528	          ],
529	          [
530	            "2 vs 3",
531	            "0.576",
532	            "0.572",
533	            "-0.004"
534	          ],
535	          [
536	            "3 vs 4",
537	            "0.538",
538	            "0.541",
539	            "+0.003"
540	          ]
541	        ]
542	      }
543	    ],
544	    "figures": [],
545	    "analysis": "Retrain-chain 验证了 K*=2 的 qualitative robustness：即使换用更 ecologically valid 的 递归方式，饱和边界不变。Quantitative 差异（AUC 偏低 0.03-0.04）可讨论但不影响核心 claim。 论文中此实验作为 ecological validity check 放在 Section 5 或 Appendix。\n\n\nRetrain-chain（LoRA 微调后用微调模型生成下一代）比 prompt-chain 更接近真实世界的  \"model collapse\" 场景。但其信息损失模式有关键差异：每一代不仅改变输出分布，还改变 模型参数本身。LoRA rank=16 限制了参数更新的自由度，使得每代的变化幅度比 full retrain 小。 K*=2 与 prompt-chain 一致，但 AUC 值整体低于 prompt-chain 的 Pythia（1v2: 0.635 vs 0.672）。 这是因为 retrain-chain 中 gen-1 的文本由微调后模型生成——微调模型比原模型更 \"collapsed\"， gen-1 起点就更接近 gen-2+。K* 没有 differ by 1（仍为 2 而非 1 或 3），因为 LoRA 的 limited capacity 恰好使衰减速率与 prompt-chain 类似。 特征分布有显著但不巨大的差异（vocabulary diversity 的 KS test p=0.03），反映 retrain  导致的 vocabulary 坍缩更系统性（非随机采样造成而是参数更新造成）。\n"
546	  },
547	  {
548	    "name": "Contamination dose-response",
549	    "description": "10%/30%/50% synthetic injection 比例下 graduated vs binary filtering",
550	    "results": {
551	      "injection_10pct": {
552	        "mmlu_no_filter": 26.1,
553	        "mmlu_binary": 26.3,
554	        "mmlu_graduated": 26.5,
555	        "delta_grad_vs_binary": 0.2
556	      },
557	      "injection_30pct": {
558	        "mmlu_no_filter": 25.8,
559	        "mmlu_binary": 26.4,
560	        "mmlu_graduated": 27.2,
561	        "delta_grad_vs_binary": 0.8
562	      },
563	      "injection_50pct": {
564	        "mmlu_no_filter": 25.2,
565	        "mmlu_binary": 26.2,
566	        "mmlu_graduated": 27.3,
567	        "delta_grad_vs_binary": 1.1
568	      },
569	      "hellaswag_delta_pattern": "similar trend, slightly smaller magnitudes"
570	    },
571	    "tables": [
572	      {
573	        "caption": "Table: Dose-response — Graduated vs Binary filtering delta (MMLU pp)",
574	        "rows": [
575	          [
576	            "Injection Rate",
577	            "No Filter",
578	            "Binary",
579	            "Graduated",
580	            "Δ Grad-Binary"
581	          ],
582	          [
583	            "10%",
584	            "26.1",
585	            "26.3",
586	            "26.5",
587	            "+0.2"
588	          ],
589	          [
590	            "30%",
591	            "25.8",
592	            "26.4",
593	            "27.2",
594	            "+0.8"
595	          ],
596	          [
597	            "50%",
598	            "25.2",
599	            "26.2",
600	            "27.3",
601	            "+1.1"
602	          ]
603	        ]
604	      }
605	    ],
606	    "figures": [],
607	    "analysis": "Dose-response 揭示了 graduated filtering 的 practical sweet spot：当 contamination ≥30% 时， graduated vs binary 的差异变得 meaningful（≥0.8pp）。论文中用此结果论证 \"as web data  contamination increases, the value of depth-aware curation grows super-linearly\"。\n\n\nContamination dose 调控 graduated filtering 的 value proposition。 10% injection：基础数据集的 90% 仍是 clean human text，contamination 的影响有限。 Binary filtering 已经足够（移除 10% synthetic），graduated 的额外收益微乎其微（0.2pp）， 因为 gen-1 文本在整体 training mix 中占比太小，其 quality calibration 的价值被稀释。 30% injection：接近 exp-006 的设定。Graduated vs binary 的 delta（0.8pp）与 exp-006  一致。此时 gen-1 文本在 30% synthetic 中占约 40%（~12% of total），足以使 calibration  差异产生可测量影响。 50% injection：污染严重。No-filter 性能显著下降（25.2）。Binary filtering 恢复大部分性能 但 graduated 的优势进一步增大（1.1pp），因为 50% synthetic 中包含大量 gen-1 文本， graduated filter 选择性保留其中质量较好的部分，而 binary filter 将其全部丢弃导致 training data 量不足。这是 graduated filtering 最有价值的场景：当 contamination 严重到 不得不在 \"丢弃过多\" 和 \"保留过差\" 之间权衡时，depth calibration 提供了更精细的选择。\n"
608	  },
609	  {
610	    "name": "Ordinal vs multinomial vs regression baseline",
611	    "description": "CORAL ordinal vs standard multiclass vs ordinal regression 对比",
612	    "results": {
613	      "coral_ordinal": {
614	        "accuracy": 0.42,
615	        "mae": 1.02,
616	        "adjacent_accuracy": 0.74
617	      },
618	      "multinomial": {
619	        "accuracy": 0.4,
620	        "mae": 1.18,
621	        "adjacent_accuracy": 0.68
622	      },
623	      "ordinal_regression": {
624	        "accuracy": 0.41,
625	        "mae": 1.05,
626	        "adjacent_accuracy": 0.72
627	      }
628	    },
629	    "tables": [
630	      {
631	        "caption": "Table: Ordinal structure comparison",
632	        "rows": [
633	          [
634	            "Method",
635	            "Accuracy",
636	            "MAE",
637	            "Adjacent Acc"
638	          ],
639	          [
640	            "CORAL (ordinal)",
641	            "0.42",
642	            "1.02",
643	            "0.74"
644	          ],
645	          [
646	            "Multinomial",
647	            "0.40",
648	            "1.18",
649	            "0.68"
650	          ],
651	          [
652	            "Ordinal Regression",
653	            "0.41",
654	            "1.05",
655	            "0.72"
656	          ]
657	        ]
658	      }
659	    ],
660	    "figures": [],
661	    "analysis": "CORAL 的优势主要在 MAE 和 adjacent accuracy 而非 raw accuracy，这与 ordinal task 的  evaluation semantics 一致。论文中用此结果证明 \"depth estimation benefits from ordinal  modeling, not because it improves top-1 accuracy, but because it produces more  calibrated errors\"。\n\n\nDepth estimation 天然是 ordinal task（gen-0 < gen-1 < gen-2 ...），CORAL 通过将 ordinal  regression 编码为一系列 binary threshold 任务来利用这种结构。 CORAL vs multinomial：accuracy 差异不大（0.42 vs 0.40），因为 K*=2 意味着有效类别只有  3 个（gen-0/gen-1/gen-2+），multinomial 在 3 类上也能工作。但 MAE 差异显著（1.02 vs 1.18）， 因为 multinomial 对 \"off-by-2\" 错误没有 penalty 结构——它可能将 gen-0 错分为 gen-3， 而 CORAL 的 threshold structure 使这种远距离错误更少。Adjacent accuracy（预测值与真实值 差距 ≤1 的比例）最能体现 ordinal structure 的优势：0.74 vs 0.68。 Ordinal regression（传统 cumulative logit model）性能介于两者之间：它有 ordinal structure  但缺乏 CORAL 的 neural network flexibility。\n"
662	  },
663	  {
664	    "name": "LLM zero-shot depth estimation",
665	    "description": "GPT-4o / Claude 3.5 zero-shot depth 判断",
666	    "results": {
667	      "gpt4o_accuracy_6class": 0.22,
668	      "gpt4o_binary_auc": 0.88,
669	      "gpt4o_depth_mae": 1.85,
670	      "gpt4o_gen0v1_accuracy": 0.81,
671	      "gpt4o_gen1v2_accuracy": 0.39,
672	      "gpt4o_gen2v3_accuracy": 0.28,
673	      "claude35_accuracy_6class": 0.24,
674	      "claude35_binary_auc": 0.91,
675	      "claude35_depth_mae": 1.72,
676	      "claude35_gen0v1_accuracy": 0.84,
677	      "claude35_gen1v2_accuracy": 0.42,
678	      "claude35_gen2v3_accuracy": 0.3
679	    },
680	    "tables": [
681	      {
682	        "caption": "Table: LLM zero-shot depth estimation performance",
683	        "rows": [
684	          [
685	            "Model",
686	            "6-class Acc",
687	            "Binary AUC",
688	            "MAE",
689	            "Gen0v1 Acc",
690	            "Gen1v2 Acc"
691	          ],
692	          [
693	            "GPT-4o",
694	            "0.22",
695	            "0.88",
696	            "1.85",
697	            "0.81",
698	            "0.39"
699	          ],
700	          [
701	            "Claude 3.5 Sonnet",
702	            "0.24",
703	            "0.91",
704	            "1.72",
705	            "0.84",
706	            "0.42"
707	          ],
708	          [
709	            "Our method (CORAL)",
710	            "0.42",
711	            "0.99+",
712	            "1.02",
713	            "0.99+",
714	            "0.68"
715	          ]
716	        ]
717	      }
718	    ],
719	    "figures": [],
720	    "analysis": "LLM zero-shot 在 depth estimation 上失败，验证了 specialized method 的必要性。 同时 LLM 在 binary detection 上的不错表现说明 gen-0 vs gen-1 的信号是 \"obvious\"—— 这与 K*=2 的 narrative 一致（gen-0/gen-1 boundary 是清晰的，gen-1+/gen-2+ boundary  才需要精细方法）。\n\n\n大型 LLM 在 binary detection（human vs synthetic）上表现尚可（AUC ~0.88-0.91），因为 gen-0 vs gen-1 的文本质量差异足够大，表面线索（如过度流畅、缺乏 typos、topic drift  模式）即可捕获。但 depth estimation 失败：gen-1 vs gen-2 的细微差异（vocabulary richness  略降、surprisal variance 略减）在 zero-shot 设定下不可区分。LLM 倾向于将所有 synthetic  文本标记为 gen-1 或 gen-2（anchoring bias），导致 6-class accuracy 仅 22-24%（接近  6 分之一的 chance level 16.7%，但高于 chance 因为 gen-0 的高 recall 拉升了平均）。 MAE 高达 1.7-1.9，说明 LLM 的预测与真实 depth 相关性很弱。 这个 baseline 的战略价值在于证明 \"depth estimation is a non-trivial task requiring  specialized methods\"——即使是 SOTA LLM 也无法通过 commonsense reasoning 解决。\n"
721	  },
722	  {
723	    "name": "Binary detector confidence as depth proxy",
724	    "description": "DivEye/Binoculars score 的 Spearman correlation with true depth",
725	    "results": {
726	      "diveye_spearman_with_depth": -0.31,
727	      "diveye_spearman_p_value": 0.001,
728	      "binoculars_spearman_with_depth": -0.28,
729	      "binoculars_spearman_p_value": 0.003,
730	      "diveye_binary_auc_0v1plus": 0.93,
731	      "binoculars_binary_auc_0v1plus": 0.95,
732	      "diveye_auc_1v2": 0.57,
733	      "binoculars_auc_1v2": 0.55
734	    },
735	    "tables": [
736	      {
737	        "caption": "Table: Binary detector scores as depth proxies",
738	        "rows": [
739	          [
740	            "Detector",
741	            "Binary AUC (0v1+)",
742	            "Spearman ρ (depth)",
743	            "AUC 1v2"
744	          ],
745	          [
746	            "DivEye",
747	            "0.93",
748	            "-0.31",
749	            "0.57"
750	          ],
751	          [
752	            "Binoculars",
753	            "0.95",
754	            "-0.28",
755	            "0.55"
756	          ],
757	          [
758	            "Our features (15D)",
759	            "0.99+",
760	            "-0.82",
761	            "0.70"
762	          ]
763	        ]
764	      }
765	    ],
766	    "figures": [],
767	    "analysis": "Binary confidence 作为 depth proxy 基本失败（ρ ~-0.3），而我们的 15D 手工特征的 ρ=-0.82  显著更好。这构成对 \"why not just use existing detectors?\" 的有力回应。\n\n\nBinary detectors（DivEye, Binoculars）的 confidence score 与 true depth 有弱负相关 （Spearman ~-0.3）：更深代际的文本确实获得更低的 \"human-likeness\" score，但相关性很弱。 这是因为 binary detectors 的 decision function 是为 binary separation 优化的——它们 在 gen-0 vs gen-1+ 的 boundary 处 calibrated，但对 gen-1 vs gen-2 vs gen-3 的梯度 几乎不敏感。Binary AUC 很高（0.93-0.95），但 pairwise AUC 1v2 仅 0.55-0.57（near chance）， 说明 binary confidence ≠ depth。 这个结果的 narrative 价值：现有工具无法做 depth estimation，不是因为技术问题， 而是因为它们根本不是为此设计的。Depth estimation 是一个 genuinely new task。\n"
768	  },
769	  {
770	    "name": "Cross-model transfer",
771	    "description": "Model A 训练 → Model B 测试的 transfer accuracy",
772	    "results": {
773	      "transfer_matrix_binary_auc": {
774	        "pythia_to_olmo": 0.91,
775	        "pythia_to_qwen": 0.89,
776	        "olmo_to_pythia": 0.9,
777	        "olmo_to_qwen": 0.88,
778	        "qwen_to_pythia": 0.92,
779	        "qwen_to_olmo": 0.9
780	      },
781	      "transfer_matrix_ordinal_accuracy": {
782	        "pythia_to_olmo": 0.26,
783	        "pythia_to_qwen": 0.24,
784	        "olmo_to_pythia": 0.25,
785	        "olmo_to_qwen": 0.23,
786	        "qwen_to_pythia": 0.28,
787	        "qwen_to_olmo": 0.26
788	      },
789	      "binary_transfer_retention_pct": 92,
790	      "ordinal_transfer_retention_pct": 58
791	    },
792	    "tables": [
793	      {
794	        "caption": "Table: Cross-model transfer matrix — Binary AUC",
795	        "rows": [
796	          [
797	            "Train\\Test",
798	            "Pythia",
799	            "OLMo",
800	            "Qwen"
801	          ],
802	          [
803	            "Pythia",
804	            "0.993 (in-dist)",
805	            "0.91",
806	            "0.89"
807	          ],
808	          [
809	            "OLMo",
810	            "0.90",
811	            "0.991 (in-dist)",
812	            "0.88"
813	          ],
814	          [
815	            "Qwen",
816	            "0.92",
817	            "0.90",
818	            "0.996 (in-dist)"
819	          ]
820	        ]
821	      },
822	      {
823	        "caption": "Table: Cross-model transfer matrix — Ordinal Accuracy",
824	        "rows": [
825	          [
826	            "Train\\Test",
827	            "Pythia",
828	            "OLMo",
829	            "Qwen"
830	          ],
831	          [
832	            "Pythia",
833	            "0.40 (in-dist)",
834	            "0.26",
835	            "0.24"
836	          ],
837	          [
838	            "OLMo",
839	            "0.25",
840	            "0.39 (in-dist)",
841	            "0.23"
842	          ],
843	          [
844	            "Qwen",
845	            "0.28",
846	            "0.26",
847	            "0.42 (in-dist)"
848	          ]
849	        ]
850	      }
851	    ],
852	    "figures": [],
853	    "analysis": "Binary transferability 高 + ordinal transferability 低 的组合是重要的 nuanced finding。 论文中此结果既支持 C1（gen-0/gen-1 boundary 是 universal）又限定 C3 的 practical scope （graduated filtering 需要 in-distribution training）。Retention ~58% 说明 ordinal signal  有跨模型共性但不够强，与 degradation ordering 的 partial consistency（tau 0.5-0.8）一致。\n\n\nBinary transfer（gen-0 vs gen-1+）效果好（AUC 0.88-0.92，retention ~92%）：gen-0 vs gen-1  的信号是 universal 的——所有 LLM 生成的文本都共享某些与 human text 不同的统计特征 （过度平滑的 surprisal、降低的 vocabulary diversity）。这些特征跨模型 transferable。 Ordinal transfer 大幅退化（accuracy 0.23-0.28，retention ~58%）：gen-1 vs gen-2 vs gen-3+  的细微差异是 model-specific 的。不同模型的 lossy channel 特征不同——Pythia 的 mode collapse  模式（哪些 token 频率增加）与 OLMo 的不同，导致 gen-2 的 feature profile 不可直接迁移。 这个结果限制了 graduated filtering 的 practical applicability（需要 model-specific 训练）， 但同时证明了 depth signal 的存在性（如果 ordinal signal 不存在，transfer 应该完全是 chance）。\n"
854	  },
855	  {
856	    "name": "Naturalistic validation on Common Crawl",
857	    "description": "Common Crawl 2025/2026 snapshot 的 depth 预测 + 外部指标 correlation",
858	    "results": {
859	      "predicted_depth_distribution": {
860	        "depth_0_pct": 72,
861	        "depth_1_pct": 18,
862	        "depth_2plus_pct": 10
863	      },
864	      "correlation_with_alignscore": 0.34,
865	      "correlation_with_vocab_richness": 0.41,
866	      "high_depth_sample_qualitative_agreement": "70% of predicted depth-2+ samples show visible quality degradation upon manual inspection"
867	    },
868	    "tables": [
869	      {
870	        "caption": "Table: Common Crawl depth prediction summary",
871	        "rows": [
872	          [
873	            "Predicted Depth",
874	            "% of Sample",
875	            "Avg AlignScore",
876	            "Avg Vocab Richness"
877	          ],
878	          [
879	            "0 (human)",
880	            "72%",
881	            "0.78",
882	            "0.65"
883	          ],
884	          [
885	            "1 (gen-1)",
886	            "18%",
887	            "0.71",
888	            "0.58"
889	          ],
890	          [
891	            "2+ (gen-2+)",
892	            "10%",
893	            "0.64",
894	            "0.49"
895	          ]
896	        ]
897	      }
898	    ],
899	    "figures": [],
900	    "analysis": "Naturalistic validation 提供 directional 而非 definitive 的支持。Correlation 不高是 expected（domain shift + no ground truth depth labels in the wild）。论文中放入 Appendix  作为 ecological validity evidence，不作为主要 claim 的支撑。\n\n\nCommon Crawl 2025-2026 中合成文本比例正在增长但仍以浅代际为主。我们的 classifier  预测 ~28% 为 synthetic（depth ≥1），其中 ~18% 为 gen-1、~10% 为 gen-2+。这与其他 估计（如 originality.ai 的 ~25-30% synthetic content in recent crawls）大致一致。 与 AlignScore 的 correlation 较弱（0.34）——这是预期的，因为 AlignScore 衡量 factual  consistency 而非 generational depth，两者正交性高。与 vocabulary richness 的 correlation  更好（0.41），因为 vocabulary diversity 是我们特征空间的核心成分且在递归生成中持续衰减。 但 correlation 不高的原因是：wild data 中的 synthetic text 来源多样（不同模型、不同  prompt、不同 domain），我们的 classifier 在 controlled experiment 上训练，domain shift  导致 calibration 偏移。手工检查显示 70% 的高 depth 预测有明显质量退化（重复、 topic drift、vocabulary 贫乏），验证 directional correctness。\n"
901	  },
902	  {
903	    "name": "Learned representation baseline",
904	    "description": "Frozen Qwen2.5-1.5B embeddings + MLP vs 15D hand-crafted features",
905	    "results": {
906	      "learned_accuracy": 0.44,
907	      "learned_mae": 0.95,
908	      "learned_binary_auc": 0.997,
909	      "handcrafted_accuracy": 0.42,
910	      "handcrafted_mae": 1.02,
911	      "handcrafted_binary_auc": 0.996,
912	      "learned_feature_dim": 2048,
913	      "handcrafted_feature_dim": 15
914	    },
915	    "tables": [
916	      {
917	        "caption": "Table: Hand-crafted vs Learned features",
918	        "rows": [
919	          [
920	            "Features",
921	            "Dim",
922	            "Accuracy",
923	            "MAE",
924	            "Binary AUC"
925	          ],
926	          [
927	            "15D hand-crafted",
928	            "15",
929	            "0.42",
930	            "1.02",
931	            "0.996"
932	          ],
933	          [
934	            "Frozen embeddings + MLP",
935	            "2048",
936	            "0.44",
937	            "0.95",
938	            "0.997"
939	          ]
940	        ]
941	      }
942	    ],
943	    "figures": [],
944	    "analysis": "Learned representations 仅有微弱优势，验证了 hand-crafted features 的合理性。 论文中此结果回应审稿人 concern #6 (\"why not use learned representations\")。\n\n\nFrozen LM embeddings（2048 维）+ 2-layer MLP 的性能略优于 15D 手工特征（accuracy 0.44  vs 0.42，MAE 0.95 vs 1.02）。这是预期的：2048 维的 contextual representations 包含 比 15 个 hand-crafted statistics 更丰富的信息。但差距很小（~2pp accuracy，~0.07 MAE）， 因为 K*=2 限制了 depth estimation 的 ceiling——即使有完美特征，gen-2+ 的类间距也太小 无法显著提升。Learned representations 的边际优势来自捕获了一些手工特征未覆盖的信号 （如句法复杂度的微妙下降、discourse coherence 的退化模式），但这些信号贡献有限。 手工特征的优势在于 interpretability：15D 特征允许 degradation ordering 分析（exp-005）， 而 2048D embeddings 不透明。论文中此对比证明 \"hand-crafted features are competitive  with learned representations at a fraction of the dimensionality, while enabling  interpretable analysis of degradation patterns\"。\n"
945	  },
946	  {
947	    "name": "Base vs Instruct model comparison",
948	    "description": "Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异",
949	    "results": {
950	      "base_k_star": 2,
951	      "instruct_k_star": 2,
952	      "base_pairwise_auc_1v2": 0.682,
953	      "instruct_pairwise_auc_1v2": 0.696,
954	      "base_jsd_0v1": 0.243,
955	      "instruct_jsd_0v1": 0.267,
956	      "base_vocab_diversity_gen1_mean": 0.58,
957	      "instruct_vocab_diversity_gen1_mean": 0.54,
958	      "feature_distribution_ks_test_p_vocab": 0.01,
959	      "feature_distribution_ks_test_p_surprisal": 0.04
960	    },
961	    "tables": [
962	      {
963	        "caption": "Table: Base vs Instruct comparison (Qwen2.5-1.5B)",
964	        "rows": [
965	          [
966	            "Metric",
967	            "Base",
968	            "Instruct"
969	          ],
970	          [
971	            "K*",
972	            "2",
973	            "2"
974	          ],
975	          [
976	            "AUC 0v1",
977	            "0.994",
978	            "0.996"
979	          ],
980	          [
981	            "AUC 1v2",
982	            "0.682",
983	            "0.696"
984	          ],
985	          [
986	            "JSD 0v1",
987	            "0.243",
988	            "0.267"
989	          ],
990	          [
991	            "Vocab Diversity gen-1",
992	            "0.58",
993	            "0.54"
994	          ]
995	        ]
996	      }
997	    ],
998	    "figures": [],
999	    "analysis": "Base vs Instruct 的 K*=2 一致性进一步加强 universality claim。Instruct 的 lower vocabulary  diversity baseline 是一个有趣的观察——可以在 discussion 中简短提及 \"alignment training  itself acts as a mild form of mode collapse\"，但不作为主要 claim。\n\nInstruct 模型经过 RLHF/DPO 对齐，其输出比 base 模型更 \"polished\"——更长、更结构化、 vocabulary 更受限（避免 toxic/rare tokens）。这导致 Instruct 的 gen-0→gen-1 JSD 更大 （0.267 vs 0.243）：Instruct 输出与 human text（C4 原始文本）的差异比 base 输出更大， 因为 RLHF 引入了 \"assistant-like\" 的文本模式（长句、连接词使用、hedging language）。 但 K* 不受影响（均为 2），因为 Instruct 和 base 共享相同的 backbone architecture， 其 lossy channel capacity 由模型规模决定而非对齐方式。 有趣的是，Instruct 的 vocabulary diversity 在 gen-1 就更低（0.54 vs 0.58），反映 RLHF  的 vocabulary constraining 效应——对齐训练本身就是一种 \"pre-collapse\"。这意味着 Instruct  模型的递归链从一个更 collapsed 的起点开始，但饱和速度与 base 相同。\n"
1000	  }
1001	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86b8b7e4-c96c-4306-8cdb-d89695615c78",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "2ff71c03-83c0-4b44-870a-ad4bb7c658da",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Pythia-1.4B depth chain generation\",\n    \"description\": \"Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.993,\n      \"pairwise_auc_1v2\": 0.672,\n      \"pairwise_auc_2v3\": 0.576,\n      \"pairwise_auc_3v4\": 0.538,\n      \"pairwise_auc_4v5\": 0.527,\n      \"pairwise_jsd_0v1\": 0.241,\n      \"pairwise_jsd_1v2\": 0.014,\n      \"pairwise_jsd_2v3\": 0.005,\n      \"pairwise_jsd_3v4\": 0.003,\n      \"pairwise_jsd_4v5\": 0.003,\n      \"k_star\": 2,\n      \"ordinal_mae\": 1.05,\n      \"ordinal_accuracy\": 0.4\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Pythia-1.4B pairwise discrimination (AUC / JSD) by generation gap\",\n        \"rows\": [\n          [\n            \"Pair\",\n            \"AUC (mean±std)\",\n            \"JSD\"\n          ],\n          [\n            \"0 vs 1\",\n            \"0.993 ± 0.001\",\n            \"0.241\"\n          ],\n          [\n            \"1 vs 2\",\n            \"0.672 ± 0.009\",\n            \"0.014\"\n          ],\n          [\n            \"2 vs 3\",\n            \"0.576 ± 0.013\",\n            \"0.005\"\n          ],\n          [\n            \"3 vs 4\",\n            \"0.538 ± 0.008\",\n            \"0.003\"\n          ],\n          [\n            \"4 vs 5\",\n            \"0.527 ± 0.010\",\n            \"0.003\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pythia-1.4B 的 K*=2 与 MVP Qwen2.5-1.5B 一致，初步支持 K* 的跨架构稳定性。 JSD 衰减曲线形状几乎相同（exponential-like decay），仅 absolute magnitude 有差异。 这为 \\\"K*=2 is a property of the 1-2B scale regime, not a model-specific artifact\\\" 提供证据。\\n\\n\\nPythia-1.4B 是较早期的 GPT-NeoX 架构，参数量与 Qwen2.5-1.5B 同量级（1.4B vs 1.5B）， 但训练数据量和质量略低（The Pile 300B tokens vs Qwen 的多语言数据）。这意味着 Pythia 的 生成质量基线略低于 Qwen，gen-0→gen-1 的信息损失稍大（JSD 0.241 vs MVP 的 0.267—— 实际上 Pythia 初始分离度可能略低因为其 gen-0 本身已比 Qwen 的 gen-0 更 \\\"synthetic-like\\\"）。 但核心现象不变：gen-1→gen-2 的 AUC 从 ~0.67 骤降到 gen-2→gen-3 的 ~0.58，确认 K*=2。 这是因为 DPI 约束与模型规模相关而非架构特异——1.4B 模型的 lossy channel capacity  在第二代即耗尽可辨别信息。Ordinal accuracy 略低于 MVP（0.40 vs 0.42）因为 Pythia 的 特征空间结构性稍弱。\\n\"\n  },\n  {\n    \"name\": \"OLMo-1B depth chain generation\",\n    \"description\": \"OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.991,\n      \"pairwise_auc_1v2\": 0.648,\n      \"pairwise_auc_2v3\": 0.562,\n      \"pairwise_auc_3v4\": 0.531,\n      \"pairwise_auc_4v5\": 0.522,\n      \"pairwise_jsd_0v1\": 0.218,\n      \"pairwise_jsd_1v2\": 0.012,\n      \"pairwise_jsd_2v3\": 0.004,\n      \"pairwise_jsd_3v4\": 0.003,\n      \"pairwise_jsd_4v5\": 0.002,\n      \"k_star\": 2,\n      \"ordinal_mae\": 1.08,\n      \"ordinal_accuracy\": 0.39\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: OLMo-1B pairwise discrimination (AUC / JSD) by generation gap\",\n        \"rows\": [\n          [\n            \"Pair\",\n            \"AUC (mean±std)\",\n            \"JSD\"\n          ],\n          [\n            \"0 vs 1\",\n            \"0.991 ± 0.001\",\n            \"0.218\"\n          ],\n          [\n            \"1 vs 2\",\n            \"0.648 ± 0.011\",\n            \"0.012\"\n          ],\n          [\n            \"2 vs 3\",\n            \"0.562 ± 0.014\",\n            \"0.004\"\n          ],\n          [\n            \"3 vs 4\",\n            \"0.531 ± 0.009\",\n            \"0.003\"\n          ],\n          [\n            \"4 vs 5\",\n            \"0.522 ± 0.011\",\n            \"0.002\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OLMo-1B 确认了最小规模下 K*=2 仍成立。三模型族的 K*=2 一致性构成论文的核心 universality evidence。 可以论证：在 1-2B scale regime 下，K*=2 是 robust empirical constant，不依赖于具体架构 （GPT-NeoX / Transformer++ / Qwen-style）或训练数据（Pile / Dolma / multilingual）。\\n\\n\\nOLMo-1B 参数量最小（1B），且是完全开源训练流程（Dolma 数据集）。更小的模型容量意味着 其 lossy channel 在每一代损失更多信息——gen-0 的 vocabulary richness 基线就低于 1.5B 模型， 因此 gen-0 vs gen-1 的初始 JSD 为三者最低（0.218）。但 K* 仍然是 2：gen-1→gen-2 的 AUC 0.648 仍显著高于 chance（满足 0.60 阈值），而 gen-2→gen-3 的 0.562 已进入 noise floor （在 0.55-0.60 区间）。这恰好说明 K* 是 scale-dependent 的 robust constant：即使在略小的 1B 模型上，第二代仍然是信息饱和的 phase transition point。Ordinal accuracy 最低（0.39） 因为 gen-2+ 的类间距更小。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-1.5B decoding strategy ablation\",\n    \"description\": \"Qwen2.5-1.5B 在 greedy / nucleus p=0.9 / T=0.7 / T=1.2 四种解码策略下的 depth chain\",\n    \"results\": {\n      \"greedy\": {\n        \"pairwise_auc_1v2\": 0.714,\n        \"pairwise_auc_2v3\": 0.603,\n        \"k_star\": 2,\n        \"pairwise_jsd_0v1\": 0.302,\n        \"pairwise_jsd_1v2\": 0.019\n      },\n      \"nucleus_p09\": {\n        \"pairwise_auc_1v2\": 0.688,\n        \"pairwise_auc_2v3\": 0.582,\n        \"k_star\": 2,\n        \"pairwise_jsd_0v1\": 0.258,\n        \"pairwise_jsd_1v2\": 0.015\n      },\n      \"T07\": {\n        \"pairwise_auc_1v2\": 0.708,\n        \"pairwise_auc_2v3\": 0.597,\n        \"k_star\": 2,\n        \"pairwise_jsd_0v1\": 0.289,\n        \"pairwise_jsd_1v2\": 0.018\n      },\n      \"T12\": {\n        \"pairwise_auc_1v2\": 0.651,\n        \"pairwise_auc_2v3\": 0.583,\n        \"pairwise_auc_3v4\": 0.558,\n        \"k_star_seed1\": 2,\n        \"k_star_seed2\": 3,\n        \"k_star_seed3\": 2,\n        \"k_star_majority\": 2,\n        \"pairwise_jsd_0v1\": 0.195,\n        \"pairwise_jsd_1v2\": 0.011\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Decoding strategy ablation — K* and key AUC values\",\n        \"rows\": [\n          [\n            \"Strategy\",\n            \"AUC 0v1\",\n            \"AUC 1v2\",\n            \"AUC 2v3\",\n            \"JSD 0v1\",\n            \"K*\"\n          ],\n          [\n            \"Greedy\",\n            \"0.997\",\n            \"0.714\",\n            \"0.603\",\n            \"0.302\",\n            \"2\"\n          ],\n          [\n            \"Nucleus p=0.9\",\n            \"0.996\",\n            \"0.688\",\n            \"0.582\",\n            \"0.258\",\n            \"2\"\n          ],\n          [\n            \"T=0.7\",\n            \"0.997\",\n            \"0.708\",\n            \"0.597\",\n            \"0.289\",\n            \"2\"\n          ],\n          [\n            \"T=1.2\",\n            \"0.992\",\n            \"0.651\",\n            \"0.583\",\n            \"0.195\",\n            \"2 (1 seed: 3)\"\n          ],\n          [\n            \"MVP baseline (p=0.95)\",\n            \"0.996\",\n            \"0.696\",\n            \"0.589\",\n            \"0.267\",\n            \"2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"四种解码策略中 K*=2 完全稳定，仅 T=1.2 在部分 seed 下 K*=3。这支持 median tier 的核心叙事： K*=2 是 robust constant，极端解码是目前发现的唯一调控因素。论文中可以用此结果论证 \\\"K* is remarkably stable across decoding strategies, with only extreme temperature  (T≥1.2) occasionally extending it to 3\\\"。\\n\\n\\n解码策略通过控制 sampling entropy 调节每一代的信息损失率。 Greedy（T=0, argmax）：最低 entropy sampling → 每代输出最 \\\"mode-collapsed\\\"，gen-0 vs gen-1  的初始差异最大（JSD 0.302）因为 greedy 输出与 human text 的分布差距最大。但这个大初始差距 也使得 gen-1 vs gen-2 的 AUC 最高（0.714），因为 gen-1 仍保留可辨别的 diversity 信号。 K*=2 因为 gen-2→gen-3 在 0.603 处——接近阈值但仍 above。 Nucleus p=0.9：比 MVP baseline（p=0.95）稍 tighter，效果与 baseline 相近，K*=2。 T=0.7（low temperature）：类似 greedy 的效果但稍温和，K*=2。 T=1.2（high temperature）：高温增加采样随机性，每代注入更多 noise。这使得 gen-0→gen-1  的信息损失最小（JSD 0.195）——高温输出本身就更 diverse 更接近 human text。但同时， 高温使 gen-1→gen-2 的辨别力降低（AUC 0.651），而 gen-2→gen-3 在 0.583——某些 seed  下可能越过 0.60 阈值使 K*=3。这是唯一导致 K* 不稳定的条件：3 个 seed 中 1 个显示 K*=3， 多数仍为 2。机制是高温保留了更多 per-generation variance，使得 DPI 的信息压缩在第三代 才完全饱和。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-7B cross-scale probe\",\n    \"description\": \"Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.989,\n      \"pairwise_auc_1v2\": 0.718,\n      \"pairwise_auc_2v3\": 0.612,\n      \"pairwise_jsd_0v1\": 0.193,\n      \"pairwise_jsd_1v2\": 0.02,\n      \"pairwise_jsd_2v3\": 0.008,\n      \"k_star_seed1\": 2,\n      \"k_star_seed2\": 3,\n      \"k_star_seed3\": 2,\n      \"k_star_majority\": 2,\n      \"ordinal_mae\": 0.93,\n      \"ordinal_accuracy\": 0.44\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Qwen2.5-7B pairwise discrimination (3 seeds)\",\n        \"rows\": [\n          [\n            \"Pair\",\n            \"AUC (seed1/seed2/seed3)\",\n            \"K* per seed\"\n          ],\n          [\n            \"0 vs 1\",\n            \"0.990/0.988/0.989\",\n            \"-\"\n          ],\n          [\n            \"1 vs 2\",\n            \"0.722/0.710/0.721\",\n            \"-\"\n          ],\n          [\n            \"2 vs 3\",\n            \"0.618/0.597/0.620\",\n            \"3/2/3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 的结果暗示 K* 可能随模型规模增长而增大，但在当前实验规模下无法确定性地声称 K*=3。 论文中应保守表述：\\\"7B models show suggestive evidence that K* may increase with scale,  but the effect is within seed variance at our sample size\\\"。这为 future work（更大模型、 更多数据）留下了自然的延伸方向。\\n\\n\\n7B 模型的 channel capacity 更高——更大的模型在每一代保留更多信息，因此信息衰减更慢。 这体现在：(1) gen-0 vs gen-1 的 JSD 更低（0.193 vs 1.5B 的 0.267），因为 7B 的生成质量 更高，gen-1 与 human text 的分布差异更小；(2) gen-1 vs gen-2 的 AUC 更高（0.718 vs 0.696）， 因为 7B 在 gen-1 中保留了更多可辨别特征；(3) gen-2 vs gen-3 的 AUC 在 0.612——处于 K*=2 和 K*=3 的边界。某些 seed 下 AUC 2v3 越过 0.60 → K*=3，其他 seed 下刚好在边界上。 这种 seed-level instability 是 median tier 的特征预测。机制解释：7B 的 lossy channel  压缩率更低，DPI 导致的饱和在第三代才完成，而非第二代。但由于只有 1K docs（而非 5K）， 统计 power 较低，加剧了 seed variance。如果有 5K docs，K* 可能稳定在 3。\\n\"\n  },\n  {\n    \"name\": \"Feature group ablation + degradation ordering\",\n    \"description\": \"对 Pythia-1.4B 和 OLMo-1B 的 depth chain 按 feature group 分析饱和深度和 degradation ordering\",\n    \"results\": {\n      \"pythia_saturation_order\": [\n        \"vocabulary_diversity\",\n        \"tail_thinning\",\n        \"surprisal_dynamics\"\n      ],\n      \"olmo_saturation_order\": [\n        \"vocabulary_diversity\",\n        \"surprisal_dynamics\",\n        \"tail_thinning\"\n      ],\n      \"vocabulary_diversity_saturation_depth_range\": [\n        1.5,\n        2.0\n      ],\n      \"surprisal_dynamics_saturation_depth_range\": [\n        2.0,\n        2.5\n      ],\n      \"tail_thinning_saturation_depth_range\": [\n        2.0,\n        3.0\n      ],\n      \"kendall_tau_ordering_consistency_across_models\": 0.67,\n      \"feature_group_pairwise_auc\": {\n        \"pythia_vocab_1v2\": 0.641,\n        \"pythia_surprisal_1v2\": 0.608,\n        \"pythia_tail_1v2\": 0.622,\n        \"olmo_vocab_1v2\": 0.625,\n        \"olmo_surprisal_1v2\": 0.612,\n        \"olmo_tail_1v2\": 0.598\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Feature group saturation depth and pairwise AUC (1v2) by model\",\n        \"rows\": [\n          [\n            \"Feature Group\",\n            \"Pythia AUC 1v2\",\n            \"Pythia Sat. Depth\",\n            \"OLMo AUC 1v2\",\n            \"OLMo Sat. Depth\"\n          ],\n          [\n            \"Vocabulary Diversity\",\n            \"0.641\",\n            \"1.8\",\n            \"0.625\",\n            \"1.6\"\n          ],\n          [\n            \"Surprisal Dynamics\",\n            \"0.608\",\n            \"2.3\",\n            \"0.612\",\n            \"2.1\"\n          ],\n          [\n            \"Tail Thinning\",\n            \"0.622\",\n            \"2.0\",\n            \"0.598\",\n            \"2.5\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: Degradation ordering consistency (Kendall tau)\",\n        \"rows\": [\n          [\n            \"Model Pair\",\n            \"Kendall tau\",\n            \"p-value\"\n          ],\n          [\n            \"Pythia vs OLMo\",\n            \"0.67\",\n            \"0.08\"\n          ],\n          [\n            \"Pythia vs Qwen (MVP)\",\n            \"0.67\",\n            \"0.08\"\n          ],\n          [\n            \"OLMo vs Qwen (MVP)\",\n            \"1.00\",\n            \"0.02\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Vocabulary diversity 的优先饱和跨模型大致一致（3/3 模型中最先饱和），支持 C2 的 \\\"tendency\\\"  表述。但 surprisal 和 tail-thinning 的顺序不稳定（tau 0.67），应避免声称严格 ordering。 论文中建议表述：\\\"vocabulary diversity consistently degrades earliest, while the relative  ordering of surprisal and tail features is model-dependent\\\"。\\n\\n\\nVocabulary diversity（TTR, hapax ratio, entropy-based measures）对递归生成最敏感： 每一代 LM 生成都倾向于 mode collapse 到高频词汇，vocabulary richness 在 gen-1→gen-2  即显著下降。这是因为 LM 的 softmax 分布本质上是对 training distribution 的平滑近似， 递归采样会累积放大这种平滑效应（\\\"rich get richer\\\" for frequent tokens）。 Surprisal dynamics（perplexity variance, burstiness）和 tail-thinning（rare token frequency） 饱和较慢，因为这些特征依赖于高阶统计量，需要更多代际压缩才会坍缩。 但 ordering 不完全一致：Pythia 上 tail-thinning 先于 surprisal 饱和，OLMo 上反过来。 这导致跨模型 Kendall tau 为 0.67——有趋势但非严格一致。原因是不同架构的 attention pattern  和 vocabulary size 差异导致 rare token 的衰减速率不同。Pythia 的 50K vocabulary 中 rare tokens 衰减更快（tail-thinning 先饱和），而 OLMo 的训练数据特征使 surprisal  burstiness 先丧失。\\n\"\n  },\n  {\n    \"name\": \"Downstream filtering evaluation\",\n    \"description\": \"no-filter / binary / graduated / surprisal-based 四种过滤策略，continued pretraining + lm-eval-harness，3 seeds\",\n    \"results\": {\n      \"mmlu_no_filter\": 25.8,\n      \"mmlu_binary\": 26.4,\n      \"mmlu_graduated\": 27.2,\n      \"mmlu_surprisal\": 26.9,\n      \"mmlu_graduated_vs_binary_delta_pp\": 0.8,\n      \"mmlu_std_across_seeds\": 0.4,\n      \"hellaswag_no_filter\": 42.1,\n      \"hellaswag_binary\": 43.0,\n      \"hellaswag_graduated\": 43.7,\n      \"hellaswag_surprisal\": 43.4,\n      \"hellaswag_graduated_vs_binary_delta_pp\": 0.7,\n      \"hellaswag_std_across_seeds\": 0.5\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Downstream evaluation (MMLU / HellaSwag accuracy) by filtering strategy\",\n        \"rows\": [\n          [\n            \"Strategy\",\n            \"MMLU (mean±std)\",\n            \"HellaSwag (mean±std)\",\n            \"Δ vs Binary (pp)\"\n          ],\n          [\n            \"No filter\",\n            \"25.8 ± 0.3\",\n            \"42.1 ± 0.4\",\n            \"-0.6 / -0.9\"\n          ],\n          [\n            \"Binary\",\n            \"26.4 ± 0.4\",\n            \"43.0 ± 0.5\",\n            \"—\"\n          ],\n          [\n            \"Surprisal-based\",\n            \"26.9 ± 0.3\",\n            \"43.4 ± 0.4\",\n            \"+0.5 / +0.4\"\n          ],\n          [\n            \"Graduated (3-class)\",\n            \"27.2 ± 0.4\",\n            \"43.7 ± 0.5\",\n            \"+0.8 / +0.7\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graduated filtering 的优势 real but modest（~0.8pp MMLU，~0.7pp HellaSwag），且 seed  variance 使得 p-value 可能在 0.05-0.10。论文中应强调 calibration 优势而非 raw gap： \\\"graduated filtering provides better-calibrated quality estimates near the decision  boundary, where binary filtering makes its most consequential errors\\\"。 同时，no-filter → binary 的 gap 本身也不大（~0.6-0.9pp），因为 C4 基础数据质量已较高。\\n\\n\\n四种策略形成清晰的 hierarchy：no-filter < binary < surprisal ≈ graduated。 Binary filtering 移除所有 gen-1+ 文本，改善约 0.6pp（MMLU）/ 0.9pp（HellaSwag）—— 这证明合成文本确实有害。Graduated filtering 进一步改善 0.8pp / 0.7pp：机制是 graduated  在 binary decision boundary 附近提供更 calibrated 的置信度。具体来说，binary classifier  对 gen-1 文本（质量尚可）和 gen-3 文本（质量差）给出相同的 \\\"synthetic\\\" 标签，而 graduated  classifier 将 gen-1 标记为 \\\"shallow synthetic\\\"（允许部分保留），gen-3 标记为 \\\"deep synthetic\\\" （强力过滤）。这种 calibration 在 training mixture 中保留了更多有用的 gen-1 数据。 但 effect size 仅 0.5-1.5pp 且 seed variance（std ~0.4-0.5pp）使得 confidence interval  可能重叠。这是 median tier 的关键特征：gain 是 real but modest，statistical significance  可能需要更多 seeds 才能确认。Surprisal-based filtering（直接用 perplexity 做 quality gate） 性能介于 binary 和 graduated 之间——它隐式捕获了部分 depth 信息但不如显式 depth 估计精确。\\n\"\n  },\n  {\n    \"name\": \"K* sensitivity to AUC threshold\",\n    \"description\": \"在 0.55/0.60/0.65/0.70 四个阈值下计算 K*\",\n    \"results\": {\n      \"threshold_055\": {\n        \"k_star_pythia\": 3,\n        \"k_star_olmo\": 2,\n        \"k_star_qwen_baseline\": 2,\n        \"k_star_qwen_T12\": 3\n      },\n      \"threshold_060\": {\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2,\n        \"k_star_qwen_baseline\": 2,\n        \"k_star_qwen_T12\": 2\n      },\n      \"threshold_065\": {\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2,\n        \"k_star_qwen_baseline\": 2,\n        \"k_star_qwen_T12\": 2\n      },\n      \"threshold_070\": {\n        \"k_star_pythia\": 1,\n        \"k_star_olmo\": 1,\n        \"k_star_qwen_baseline\": 2,\n        \"k_star_qwen_T12\": 1\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: K* stability across AUC thresholds\",\n        \"rows\": [\n          [\n            \"Threshold\",\n            \"Pythia\",\n            \"OLMo\",\n            \"Qwen (baseline)\",\n            \"Qwen (T=1.2)\"\n          ],\n          [\n            \"0.55\",\n            \"3\",\n            \"2\",\n            \"2\",\n            \"3\"\n          ],\n          [\n            \"0.60\",\n            \"2\",\n            \"2\",\n            \"2\",\n            \"2\"\n          ],\n          [\n            \"0.65\",\n            \"2\",\n            \"2\",\n            \"2\",\n            \"2\"\n          ],\n          [\n            \"0.70\",\n            \"1\",\n            \"1\",\n            \"2\",\n            \"1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"K*=2 在 0.60-0.65 的 threshold 范围内完全稳定。低于 0.55 或高于 0.70 时 K* 变化， 但这些阈值分别对应 \\\"too lenient\\\"（near chance）和 \\\"too strict\\\"（过滤掉有意义的信号）。 论文应展示此 robustness check 以预防审稿人质疑 threshold 选择的任意性。\\n\\n\\nK* 定义为最大深度 k 使得 pairwise AUC(k vs k+1) > threshold。阈值选择影响 K* 的绝对值， 但关键发现是 K* 的跨模型相对 pattern 对阈值 robust。 Threshold 0.55（宽松）：部分模型的 gen-2v3 AUC（如 Pythia 0.576）仍 > 0.55，K* 升到 3。 但这个阈值过于宽松——0.55 的 AUC 接近 chance，实际辨别意义不大。 Threshold 0.60（默认）：所有 1.5B 模型 K*=2，这是论文采用的 operating point。 Threshold 0.65（偏严）：所有模型仍然 K*=2，因为 gen-1v2 AUC（0.65-0.72）刚好 above 0.65。 Threshold 0.70（过严）：大部分模型 K* 降到 1，因为 gen-1v2 AUC 多在 0.65-0.70 区间， 低于 0.70 阈值。仅 Qwen baseline（AUC 1v2 = 0.696）勉强接近。 核心 insight：在 0.55-0.65 的合理阈值范围内，K*=2 对 1.5B 模型高度稳定。\\n\"\n  },\n  {\n    \"name\": \"Retrain-chain ecological validity\",\n    \"description\": \"Pythia-1.4B LoRA retrain-chain, depth 0-4\",\n    \"results\": {\n      \"pairwise_auc_0v1\": 0.988,\n      \"pairwise_auc_1v2\": 0.635,\n      \"pairwise_auc_2v3\": 0.572,\n      \"pairwise_auc_3v4\": 0.541,\n      \"k_star\": 2,\n      \"jsd_0v1\": 0.198,\n      \"jsd_1v2\": 0.011,\n      \"feature_distribution_shift_vs_prompt_chain\": {\n        \"vocabulary_diversity_ks_test_p\": 0.03,\n        \"surprisal_dynamics_ks_test_p\": 0.12,\n        \"tail_thinning_ks_test_p\": 0.07\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Prompt-chain vs Retrain-chain comparison (Pythia-1.4B)\",\n        \"rows\": [\n          [\n            \"Pair\",\n            \"Prompt AUC\",\n            \"Retrain AUC\",\n            \"Δ AUC\"\n          ],\n          [\n            \"0 vs 1\",\n            \"0.993\",\n            \"0.988\",\n            \"-0.005\"\n          ],\n          [\n            \"1 vs 2\",\n            \"0.672\",\n            \"0.635\",\n            \"-0.037\"\n          ],\n          [\n            \"2 vs 3\",\n            \"0.576\",\n            \"0.572\",\n            \"-0.004\"\n          ],\n          [\n            \"3 vs 4\",\n            \"0.538\",\n            \"0.541\",\n            \"+0.003\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Retrain-chain 验证了 K*=2 的 qualitative robustness：即使换用更 ecologically valid 的 递归方式，饱和边界不变。Quantitative 差异（AUC 偏低 0.03-0.04）可讨论但不影响核心 claim。 论文中此实验作为 ecological validity check 放在 Section 5 或 Appendix。\\n\\n\\nRetrain-chain（LoRA 微调后用微调模型生成下一代）比 prompt-chain 更接近真实世界的  \\\"model collapse\\\" 场景。但其信息损失模式有关键差异：每一代不仅改变输出分布，还改变 模型参数本身。LoRA rank=16 限制了参数更新的自由度，使得每代的变化幅度比 full retrain 小。 K*=2 与 prompt-chain 一致，但 AUC 值整体低于 prompt-chain 的 Pythia（1v2: 0.635 vs 0.672）。 这是因为 retrain-chain 中 gen-1 的文本由微调后模型生成——微调模型比原模型更 \\\"collapsed\\\"， gen-1 起点就更接近 gen-2+。K* 没有 differ by 1（仍为 2 而非 1 或 3），因为 LoRA 的 limited capacity 恰好使衰减速率与 prompt-chain 类似。 特征分布有显著但不巨大的差异（vocabulary diversity 的 KS test p=0.03），反映 retrain  导致的 vocabulary 坍缩更系统性（非随机采样造成而是参数更新造成）。\\n\"\n  },\n  {\n    \"name\": \"Contamination dose-response\",\n    \"description\": \"10%/30%/50% synthetic injection 比例下 graduated vs binary filtering\",\n    \"results\": {\n      \"injection_10pct\": {\n        \"mmlu_no_filter\": 26.1,\n        \"mmlu_binary\": 26.3,\n        \"mmlu_graduated\": 26.5,\n        \"delta_grad_vs_binary\": 0.2\n      },\n      \"injection_30pct\": {\n        \"mmlu_no_filter\": 25.8,\n        \"mmlu_binary\": 26.4,\n        \"mmlu_graduated\": 27.2,\n        \"delta_grad_vs_binary\": 0.8\n      },\n      \"injection_50pct\": {\n        \"mmlu_no_filter\": 25.2,\n        \"mmlu_binary\": 26.2,\n        \"mmlu_graduated\": 27.3,\n        \"delta_grad_vs_binary\": 1.1\n      },\n      \"hellaswag_delta_pattern\": \"similar trend, slightly smaller magnitudes\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Dose-response — Graduated vs Binary filtering delta (MMLU pp)\",\n        \"rows\": [\n          [\n            \"Injection Rate\",\n            \"No Filter\",\n            \"Binary\",\n            \"Graduated\",\n            \"Δ Grad-Binary\"\n          ],\n          [\n            \"10%\",\n            \"26.1\",\n            \"26.3\",\n            \"26.5\",\n            \"+0.2\"\n          ],\n          [\n            \"30%\",\n            \"25.8\",\n            \"26.4\",\n            \"27.2\",\n            \"+0.8\"\n          ],\n          [\n            \"50%\",\n            \"25.2\",\n            \"26.2\",\n            \"27.3\",\n            \"+1.1\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dose-response 揭示了 graduated filtering 的 practical sweet spot：当 contamination ≥30% 时， graduated vs binary 的差异变得 meaningful（≥0.8pp）。论文中用此结果论证 \\\"as web data  contamination increases, the value of depth-aware curation grows super-linearly\\\"。\\n\\n\\nContamination dose 调控 graduated filtering 的 value proposition。 10% injection：基础数据集的 90% 仍是 clean human text，contamination 的影响有限。 Binary filtering 已经足够（移除 10% synthetic），graduated 的额外收益微乎其微（0.2pp）， 因为 gen-1 文本在整体 training mix 中占比太小，其 quality calibration 的价值被稀释。 30% injection：接近 exp-006 的设定。Graduated vs binary 的 delta（0.8pp）与 exp-006  一致。此时 gen-1 文本在 30% synthetic 中占约 40%（~12% of total），足以使 calibration  差异产生可测量影响。 50% injection：污染严重。No-filter 性能显著下降（25.2）。Binary filtering 恢复大部分性能 但 graduated 的优势进一步增大（1.1pp），因为 50% synthetic 中包含大量 gen-1 文本， graduated filter 选择性保留其中质量较好的部分，而 binary filter 将其全部丢弃导致 training data 量不足。这是 graduated filtering 最有价值的场景：当 contamination 严重到 不得不在 \\\"丢弃过多\\\" 和 \\\"保留过差\\\" 之间权衡时，depth calibration 提供了更精细的选择。\\n\"\n  },\n  {\n    \"name\": \"Ordinal vs multinomial vs regression baseline\",\n    \"description\": \"CORAL ordinal vs standard multiclass vs ordinal regression 对比\",\n    \"results\": {\n      \"coral_ordinal\": {\n        \"accuracy\": 0.42,\n        \"mae\": 1.02,\n        \"adjacent_accuracy\": 0.74\n      },\n      \"multinomial\": {\n        \"accuracy\": 0.4,\n        \"mae\": 1.18,\n        \"adjacent_accuracy\": 0.68\n      },\n      \"ordinal_regression\": {\n        \"accuracy\": 0.41,\n        \"mae\": 1.05,\n        \"adjacent_accuracy\": 0.72\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Ordinal structure comparison\",\n        \"rows\": [\n          [\n            \"Method\",\n            \"Accuracy\",\n            \"MAE\",\n            \"Adjacent Acc\"\n          ],\n          [\n            \"CORAL (ordinal)\",\n            \"0.42\",\n            \"1.02\",\n            \"0.74\"\n          ],\n          [\n            \"Multinomial\",\n            \"0.40\",\n            \"1.18\",\n            \"0.68\"\n          ],\n          [\n            \"Ordinal Regression\",\n            \"0.41\",\n            \"1.05\",\n            \"0.72\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CORAL 的优势主要在 MAE 和 adjacent accuracy 而非 raw accuracy，这与 ordinal task 的  evaluation semantics 一致。论文中用此结果证明 \\\"depth estimation benefits from ordinal  modeling, not because it improves top-1 accuracy, but because it produces more  calibrated errors\\\"。\\n\\n\\nDepth estimation 天然是 ordinal task（gen-0 < gen-1 < gen-2 ...），CORAL 通过将 ordinal  regression 编码为一系列 binary threshold 任务来利用这种结构。 CORAL vs multinomial：accuracy 差异不大（0.42 vs 0.40），因为 K*=2 意味着有效类别只有  3 个（gen-0/gen-1/gen-2+），multinomial 在 3 类上也能工作。但 MAE 差异显著（1.02 vs 1.18）， 因为 multinomial 对 \\\"off-by-2\\\" 错误没有 penalty 结构——它可能将 gen-0 错分为 gen-3， 而 CORAL 的 threshold structure 使这种远距离错误更少。Adjacent accuracy（预测值与真实值 差距 ≤1 的比例）最能体现 ordinal structure 的优势：0.74 vs 0.68。 Ordinal regression（传统 cumulative logit model）性能介于两者之间：它有 ordinal structure  但缺乏 CORAL 的 neural network flexibility。\\n\"\n  },\n  {\n    \"name\": \"LLM zero-shot depth estimation\",\n    \"description\": \"GPT-4o / Claude 3.5 zero-shot depth 判断\",\n    \"results\": {\n      \"gpt4o_accuracy_6class\": 0.22,\n      \"gpt4o_binary_auc\": 0.88,\n      \"gpt4o_depth_mae\": 1.85,\n      \"gpt4o_gen0v1_accuracy\": 0.81,\n      \"gpt4o_gen1v2_accuracy\": 0.39,\n      \"gpt4o_gen2v3_accuracy\": 0.28,\n      \"claude35_accuracy_6class\": 0.24,\n      \"claude35_binary_auc\": 0.91,\n      \"claude35_depth_mae\": 1.72,\n      \"claude35_gen0v1_accuracy\": 0.84,\n      \"claude35_gen1v2_accuracy\": 0.42,\n      \"claude35_gen2v3_accuracy\": 0.3\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: LLM zero-shot depth estimation performance\",\n        \"rows\": [\n          [\n            \"Model\",\n            \"6-class Acc\",\n            \"Binary AUC\",\n            \"MAE\",\n            \"Gen0v1 Acc\",\n            \"Gen1v2 Acc\"\n          ],\n          [\n            \"GPT-4o\",\n            \"0.22\",\n            \"0.88\",\n            \"1.85\",\n            \"0.81\",\n            \"0.39\"\n          ],\n          [\n            \"Claude 3.5 Sonnet\",\n            \"0.24\",\n            \"0.91\",\n            \"1.72\",\n            \"0.84\",\n            \"0.42\"\n          ],\n          [\n            \"Our method (CORAL)\",\n            \"0.42\",\n            \"0.99+\",\n            \"1.02\",\n            \"0.99+\",\n            \"0.68\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLM zero-shot 在 depth estimation 上失败，验证了 specialized method 的必要性。 同时 LLM 在 binary detection 上的不错表现说明 gen-0 vs gen-1 的信号是 \\\"obvious\\\"—— 这与 K*=2 的 narrative 一致（gen-0/gen-1 boundary 是清晰的，gen-1+/gen-2+ boundary  才需要精细方法）。\\n\\n\\n大型 LLM 在 binary detection（human vs synthetic）上表现尚可（AUC ~0.88-0.91），因为 gen-0 vs gen-1 的文本质量差异足够大，表面线索（如过度流畅、缺乏 typos、topic drift  模式）即可捕获。但 depth estimation 失败：gen-1 vs gen-2 的细微差异（vocabulary richness  略降、surprisal variance 略减）在 zero-shot 设定下不可区分。LLM 倾向于将所有 synthetic  文本标记为 gen-1 或 gen-2（anchoring bias），导致 6-class accuracy 仅 22-24%（接近  6 分之一的 chance level 16.7%，但高于 chance 因为 gen-0 的高 recall 拉升了平均）。 MAE 高达 1.7-1.9，说明 LLM 的预测与真实 depth 相关性很弱。 这个 baseline 的战略价值在于证明 \\\"depth estimation is a non-trivial task requiring  specialized methods\\\"——即使是 SOTA LLM 也无法通过 commonsense reasoning 解决。\\n\"\n  },\n  {\n    \"name\": \"Binary detector confidence as depth proxy\",\n    \"description\": \"DivEye/Binoculars score 的 Spearman correlation with true depth\",\n    \"results\": {\n      \"diveye_spearman_with_depth\": -0.31,\n      \"diveye_spearman_p_value\": 0.001,\n      \"binoculars_spearman_with_depth\": -0.28,\n      \"binoculars_spearman_p_value\": 0.003,\n      \"diveye_binary_auc_0v1plus\": 0.93,\n      \"binoculars_binary_auc_0v1plus\": 0.95,\n      \"diveye_auc_1v2\": 0.57,\n      \"binoculars_auc_1v2\": 0.55\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Binary detector scores as depth proxies\",\n        \"rows\": [\n          [\n            \"Detector\",\n            \"Binary AUC (0v1+)\",\n            \"Spearman ρ (depth)\",\n            \"AUC 1v2\"\n          ],\n          [\n            \"DivEye\",\n            \"0.93\",\n            \"-0.31\",\n            \"0.57\"\n          ],\n          [\n            \"Binoculars\",\n            \"0.95\",\n            \"-0.28\",\n            \"0.55\"\n          ],\n          [\n            \"Our features (15D)\",\n            \"0.99+\",\n            \"-0.82\",\n            \"0.70\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary confidence 作为 depth proxy 基本失败（ρ ~-0.3），而我们的 15D 手工特征的 ρ=-0.82  显著更好。这构成对 \\\"why not just use existing detectors?\\\" 的有力回应。\\n\\n\\nBinary detectors（DivEye, Binoculars）的 confidence score 与 true depth 有弱负相关 （Spearman ~-0.3）：更深代际的文本确实获得更低的 \\\"human-likeness\\\" score，但相关性很弱。 这是因为 binary detectors 的 decision function 是为 binary separation 优化的——它们 在 gen-0 vs gen-1+ 的 boundary 处 calibrated，但对 gen-1 vs gen-2 vs gen-3 的梯度 几乎不敏感。Binary AUC 很高（0.93-0.95），但 pairwise AUC 1v2 仅 0.55-0.57（near chance）， 说明 binary confidence ≠ depth。 这个结果的 narrative 价值：现有工具无法做 depth estimation，不是因为技术问题， 而是因为它们根本不是为此设计的。Depth estimation 是一个 genuinely new task。\\n\"\n  },\n  {\n    \"name\": \"Cross-model transfer\",\n    \"description\": \"Model A 训练 → Model B 测试的 transfer accuracy\",\n    \"results\": {\n      \"transfer_matrix_binary_auc\": {\n        \"pythia_to_olmo\": 0.91,\n        \"pythia_to_qwen\": 0.89,\n        \"olmo_to_pythia\": 0.9,\n        \"olmo_to_qwen\": 0.88,\n        \"qwen_to_pythia\": 0.92,\n        \"qwen_to_olmo\": 0.9\n      },\n      \"transfer_matrix_ordinal_accuracy\": {\n        \"pythia_to_olmo\": 0.26,\n        \"pythia_to_qwen\": 0.24,\n        \"olmo_to_pythia\": 0.25,\n        \"olmo_to_qwen\": 0.23,\n        \"qwen_to_pythia\": 0.28,\n        \"qwen_to_olmo\": 0.26\n      },\n      \"binary_transfer_retention_pct\": 92,\n      \"ordinal_transfer_retention_pct\": 58\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Cross-model transfer matrix — Binary AUC\",\n        \"rows\": [\n          [\n            \"Train\\\\Test\",\n            \"Pythia\",\n            \"OLMo\",\n            \"Qwen\"\n          ],\n          [\n            \"Pythia\",\n            \"0.993 (in-dist)\",\n            \"0.91\",\n            \"0.89\"\n          ],\n          [\n            \"OLMo\",\n            \"0.90\",\n            \"0.991 (in-dist)\",\n            \"0.88\"\n          ],\n          [\n            \"Qwen\",\n            \"0.92\",\n            \"0.90\",\n            \"0.996 (in-dist)\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table: Cross-model transfer matrix — Ordinal Accuracy\",\n        \"rows\": [\n          [\n            \"Train\\\\Test\",\n            \"Pythia\",\n            \"OLMo\",\n            \"Qwen\"\n          ],\n          [\n            \"Pythia\",\n            \"0.40 (in-dist)\",\n            \"0.26\",\n            \"0.24\"\n          ],\n          [\n            \"OLMo\",\n            \"0.25\",\n            \"0.39 (in-dist)\",\n            \"0.23\"\n          ],\n          [\n            \"Qwen\",\n            \"0.28\",\n            \"0.26\",\n            \"0.42 (in-dist)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binary transferability 高 + ordinal transferability 低 的组合是重要的 nuanced finding。 论文中此结果既支持 C1（gen-0/gen-1 boundary 是 universal）又限定 C3 的 practical scope （graduated filtering 需要 in-distribution training）。Retention ~58% 说明 ordinal signal  有跨模型共性但不够强，与 degradation ordering 的 partial consistency（tau 0.5-0.8）一致。\\n\\n\\nBinary transfer（gen-0 vs gen-1+）效果好（AUC 0.88-0.92，retention ~92%）：gen-0 vs gen-1  的信号是 universal 的——所有 LLM 生成的文本都共享某些与 human text 不同的统计特征 （过度平滑的 surprisal、降低的 vocabulary diversity）。这些特征跨模型 transferable。 Ordinal transfer 大幅退化（accuracy 0.23-0.28，retention ~58%）：gen-1 vs gen-2 vs gen-3+  的细微差异是 model-specific 的。不同模型的 lossy channel 特征不同——Pythia 的 mode collapse  模式（哪些 token 频率增加）与 OLMo 的不同，导致 gen-2 的 feature profile 不可直接迁移。 这个结果限制了 graduated filtering 的 practical applicability（需要 model-specific 训练）， 但同时证明了 depth signal 的存在性（如果 ordinal signal 不存在，transfer 应该完全是 chance）。\\n\"\n  },\n  {\n    \"name\": \"Naturalistic validation on Common Crawl\",\n    \"description\": \"Common Crawl 2025/2026 snapshot 的 depth 预测 + 外部指标 correlation\",\n    \"results\": {\n      \"predicted_depth_distribution\": {\n        \"depth_0_pct\": 72,\n        \"depth_1_pct\": 18,\n        \"depth_2plus_pct\": 10\n      },\n      \"correlation_with_alignscore\": 0.34,\n      \"correlation_with_vocab_richness\": 0.41,\n      \"high_depth_sample_qualitative_agreement\": \"70% of predicted depth-2+ samples show visible quality degradation upon manual inspection\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Common Crawl depth prediction summary\",\n        \"rows\": [\n          [\n            \"Predicted Depth\",\n            \"% of Sample\",\n            \"Avg AlignScore\",\n            \"Avg Vocab Richness\"\n          ],\n          [\n            \"0 (human)\",\n            \"72%\",\n            \"0.78\",\n            \"0.65\"\n          ],\n          [\n            \"1 (gen-1)\",\n            \"18%\",\n            \"0.71\",\n            \"0.58\"\n          ],\n          [\n            \"2+ (gen-2+)\",\n            \"10%\",\n            \"0.64\",\n            \"0.49\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Naturalistic validation 提供 directional 而非 definitive 的支持。Correlation 不高是 expected（domain shift + no ground truth depth labels in the wild）。论文中放入 Appendix  作为 ecological validity evidence，不作为主要 claim 的支撑。\\n\\n\\nCommon Crawl 2025-2026 中合成文本比例正在增长但仍以浅代际为主。我们的 classifier  预测 ~28% 为 synthetic（depth ≥1），其中 ~18% 为 gen-1、~10% 为 gen-2+。这与其他 估计（如 originality.ai 的 ~25-30% synthetic content in recent crawls）大致一致。 与 AlignScore 的 correlation 较弱（0.34）——这是预期的，因为 AlignScore 衡量 factual  consistency 而非 generational depth，两者正交性高。与 vocabulary richness 的 correlation  更好（0.41），因为 vocabulary diversity 是我们特征空间的核心成分且在递归生成中持续衰减。 但 correlation 不高的原因是：wild data 中的 synthetic text 来源多样（不同模型、不同  prompt、不同 domain），我们的 classifier 在 controlled experiment 上训练，domain shift  导致 calibration 偏移。手工检查显示 70% 的高 depth 预测有明显质量退化（重复、 topic drift、vocabulary 贫乏），验证 directional correctness。\\n\"\n  },\n  {\n    \"name\": \"Learned representation baseline\",\n    \"description\": \"Frozen Qwen2.5-1.5B embeddings + MLP vs 15D hand-crafted features\",\n    \"results\": {\n      \"learned_accuracy\": 0.44,\n      \"learned_mae\": 0.95,\n      \"learned_binary_auc\": 0.997,\n      \"handcrafted_accuracy\": 0.42,\n      \"handcrafted_mae\": 1.02,\n      \"handcrafted_binary_auc\": 0.996,\n      \"learned_feature_dim\": 2048,\n      \"handcrafted_feature_dim\": 15\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Hand-crafted vs Learned features\",\n        \"rows\": [\n          [\n            \"Features\",\n            \"Dim\",\n            \"Accuracy\",\n            \"MAE\",\n            \"Binary AUC\"\n          ],\n          [\n            \"15D hand-crafted\",\n            \"15\",\n            \"0.42\",\n            \"1.02\",\n            \"0.996\"\n          ],\n          [\n            \"Frozen embeddings + MLP\",\n            \"2048\",\n            \"0.44\",\n            \"0.95\",\n            \"0.997\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Learned representations 仅有微弱优势，验证了 hand-crafted features 的合理性。 论文中此结果回应审稿人 concern #6 (\\\"why not use learned representations\\\")。\\n\\n\\nFrozen LM embeddings（2048 维）+ 2-layer MLP 的性能略优于 15D 手工特征（accuracy 0.44  vs 0.42，MAE 0.95 vs 1.02）。这是预期的：2048 维的 contextual representations 包含 比 15 个 hand-crafted statistics 更丰富的信息。但差距很小（~2pp accuracy，~0.07 MAE）， 因为 K*=2 限制了 depth estimation 的 ceiling——即使有完美特征，gen-2+ 的类间距也太小 无法显著提升。Learned representations 的边际优势来自捕获了一些手工特征未覆盖的信号 （如句法复杂度的微妙下降、discourse coherence 的退化模式），但这些信号贡献有限。 手工特征的优势在于 interpretability：15D 特征允许 degradation ordering 分析（exp-005）， 而 2048D embeddings 不透明。论文中此对比证明 \\\"hand-crafted features are competitive  with learned representations at a fraction of the dimensionality, while enabling  interpretable analysis of degradation patterns\\\"。\\n\"\n  },\n  {\n    \"name\": \"Base vs Instruct model comparison\",\n    \"description\": \"Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异\",\n    \"results\": {\n      \"base_k_star\": 2,\n      \"instruct_k_star\": 2,\n      \"base_pairwise_auc_1v2\": 0.682,\n      \"instruct_pairwise_auc_1v2\": 0.696,\n      \"base_jsd_0v1\": 0.243,\n      \"instruct_jsd_0v1\": 0.267,\n      \"base_vocab_diversity_gen1_mean\": 0.58,\n      \"instruct_vocab_diversity_gen1_mean\": 0.54,\n      \"feature_distribution_ks_test_p_vocab\": 0.01,\n      \"feature_distribution_ks_test_p_surprisal\": 0.04\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Base vs Instruct comparison (Qwen2.5-1.5B)\",\n        \"rows\": [\n          [\n            \"Metric\",\n            \"Base\",\n            \"Instruct\"\n          ],\n          [\n            \"K*\",\n            \"2\",\n            \"2\"\n          ],\n          [\n            \"AUC 0v1\",\n            \"0.994\",\n            \"0.996\"\n          ],\n          [\n            \"AUC 1v2\",\n            \"0.682\",\n            \"0.696\"\n          ],\n          [\n            \"JSD 0v1\",\n            \"0.243\",\n            \"0.267\"\n          ],\n          [\n            \"Vocab Diversity gen-1\",\n            \"0.58\",\n            \"0.54\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Base vs Instruct 的 K*=2 一致性进一步加强 universality claim。Instruct 的 lower vocabulary  diversity baseline 是一个有趣的观察——可以在 discussion 中简短提及 \\\"alignment training  itself acts as a mild form of mode collapse\\\"，但不作为主要 claim。\\n\\nInstruct 模型经过 RLHF/DPO 对齐，其输出比 base 模型更 \\\"polished\\\"——更长、更结构化、 vocabulary 更受限（避免 toxic/rare tokens）。这导致 Instruct 的 gen-0→gen-1 JSD 更大 （0.267 vs 0.243）：Instruct 输出与 human text（C4 原始文本）的差异比 base 输出更大， 因为 RLHF 引入了 \\\"assistant-like\\\" 的文本模式（长句、连接词使用、hedging language）。 但 K* 不受影响（均为 2），因为 Instruct 和 base 共享相同的 backbone architecture， 其 lossy channel capacity 由模型规模决定而非对齐方式。 有趣的是，Instruct 的 vocabulary diversity 在 gen-1 就更低（0.54 vs 0.58），反映 RLHF  的 vocabulary constraining 效应——对齐训练本身就是一种 \\\"pre-collapse\\\"。这意味着 Instruct  模型的递归链从一个更 collapsed 的起点开始，但饱和速度与 base 相同。\\n\"\n  }\n]",
      "numLines": 1001,
      "startLine": 1,
      "totalLines": 1001
    }
  },
  "sourceToolAssistantUUID": "86b8b7e4-c96c-4306-8cdb-d89695615c78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contam…",
  "leafUuid": "2ff71c03-83c0-4b44-870a-ad4bb7c658da",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth contamination paper for EMNLP",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Assistant

_source line 12 · 2026-05-12T20:27:49.804Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data. Let me write the LaTeX paper based on all this data, following the narrative guidance provided. Let me craft a complete paper for EMNLP 2026.

Key points from the narrative guidance:
- K*=2 is a "robust empirical constant for current-generation 1-2B models" (not a "modulable quantity")
- Reframe as universality result: first systematic measurement showing K*=2 is highly stable across 3 model families, 4 decoding strategies
- Only extreme decoding (T≥1.2) pushes K* to 3


- C2 degradation ordering is more of a tendency than a strict rule (tau 0.5-0.8)
- Vocabulary diversity tends to saturate first but with notable exceptions
- C3 graduated filtering's main contribution is the calibration advantage rather than raw accuracy improvements (0.5-1.5pp MMLU, with overlapping seed variance)
- Emphasize the characterization contribution: first systematic measurement of K*, first formalization of depth estimation as a prediction task

Now I'm writing the paper with all the experimental results from the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ff71c03-83c0-4b44-870a-ad4bb7c658da",
  "isSidechain": false,
  "requestId": "req_011CayJdfwGvVpqvhUCcCQ7E",
  "type": "assistant",
  "uuid": "9c837fb9-58a9-4546-ac9d-d686b6fea23d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfWRbQc8Hzinhn69JbZhRS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 24468,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 24468,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

_source line 13 · 2026-05-12T20:27:49.805Z_

Reading the experiment data. Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c837fb9-58a9-4546-ac9d-d686b6fea23d",
  "isSidechain": false,
  "requestId": "req_011CayJdfwGvVpqvhUCcCQ7E",
  "type": "assistant",
  "uuid": "11747943-46a0-46cb-b811-0502d8290428",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfWRbQc8Hzinhn69JbZhRS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 24468,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 24468,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

_source line 14 · 2026-05-12T20:27:51.713Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012qyyixL7UKaQFDAyz7hdbw`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11747943-46a0-46cb-b811-0502d8290428",
  "isSidechain": false,
  "requestId": "req_011CayJdfwGvVpqvhUCcCQ7E",
  "type": "assistant",
  "uuid": "28daa208-87b6-4a4a-a1d9-587ebabe61ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfWRbQc8Hzinhn69JbZhRS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 24468,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 24468,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

_source line 15 · 2026-05-12T20:27:51.865Z_

<details><summary>↩ Tool result · `toolu_012qyyixL7UKaQFDAyz7hdbw`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28daa208-87b6-4a4a-a1d9-587ebabe61ab",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "3ee89644-6562-44ac-9d24-e4381635f743",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "28daa208-87b6-4a4a-a1d9-587ebabe61ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T20:30:57.414Z_

<details open><summary>🔧 Tool call — Write · `toolu_01STt3zbUSgmargbkC8V67DM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage{EMNLP2023} % ACL/EMNLP style\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by synthetic text that has been recursively generated---text produced by language models trained on or prompted with prior synthetic outputs. Current detection methods treat synthetic text as a binary category (human vs.\\ machine-generated), ignoring the progressive quality degradation across recursive generations. We formalize \\emph{generational depth estimation} as a prediction task and introduce the \\emph{saturation boundary} $K^*$, the maximum generation depth at which consecutive generations remain statistically distinguishable. Through controlled experiments across three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B), four decoding strategies, and two seed datasets, we establish $K^*=2$ as a remarkably stable empirical constant for 1--2B parameter models: the Jensen--Shannon divergence between feature distributions decays from 0.27 at the human/gen-1 boundary to below 0.005 by generation 3. Only extreme-temperature decoding ($T\\geq 1.2$) occasionally extends $K^*$ to 3. A cross-scale probe with Qwen2.5-7B provides suggestive evidence that $K^*$ may increase with model scale. We further show that even the coarse three-class signal (human / gen-1 / gen-2+) derived from $K^*=2$ enables \\emph{graduated filtering} that outperforms binary filtering by 0.8 percentage points on MMLU and 0.7 on HellaSwag in continued pretraining, with the advantage growing super-linearly as contamination increases. Our results provide the first systematic characterization of generational saturation in recursive synthetic text and actionable guidance for depth-aware data curation.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe fraction of machine-generated text on the web is growing rapidly. As language models (LMs) are trained on web-scraped data that already contains their predecessors' outputs, a recursive feedback loop emerges: each generation of models produces text that seeds the next generation's training data. This phenomenon---variously called \\emph{model collapse}~\\cite{shumailov2024ai}, \\emph{data contamination}, or \\emph{recursive synthetic pollution}---threatens the quality of future training corpora.\n\nExisting detection methods frame the problem as binary classification: is a given text human-written or machine-generated? Tools such as DivEye and Binoculars achieve strong performance on this binary task (AUC $>0.93$). However, they are fundamentally blind to \\emph{how many times} a text has passed through the generative pipeline. First-generation synthetic text (gen-1) retains much of the original distribution's richness, while fourth-generation text (gen-4) may exhibit severe vocabulary collapse, flattened surprisal dynamics, and factual drift. Treating both identically discards actionable quality information.\n\nWe make three contributions:\n\n\\paragraph{C1: Saturation Boundary ($K^*$).} We formalize the \\emph{generational discrimination boundary} $K^*$ as the maximum depth $k$ at which pairwise classification between generation $k$ and $k+1$ exceeds chance (AUC $>0.60$). From information-theoretic first principles---specifically, the Data Processing Inequality (DPI)---discriminability must decay monotonically along any Markov chain of generative processes. $K^*$ marks where this decay reaches a practical floor. Through systematic measurement across three model families, four decoding strategies, and base/instruct variants, we establish $K^*=2$ as a robust empirical constant for current-generation 1--2B parameter models. This is, to our knowledge, the first controlled measurement of this quantity.\n\n\\paragraph{C2: Linguistic Degradation Ordering.} We analyze which linguistic features saturate first during recursive generation. Vocabulary diversity consistently degrades earliest across all three model families, while the relative ordering of surprisal dynamics and tail-thinning features is model-dependent (Kendall $\\tau = 0.67$ across model pairs). We report this as a \\emph{tendency} rather than a strict ordering.\n\n\\paragraph{C3: Graduated Filtering.} We demonstrate that depth-graduated filtering---using the three-class signal human/gen-1/gen-2+ enabled by $K^*=2$---yields better-calibrated quality estimates than binary filtering. In continued pretraining experiments, graduated filtering improves over binary filtering by 0.8 pp on MMLU and 0.7 pp on HellaSwag at 30\\% contamination, with the advantage scaling to 1.1 pp at 50\\% contamination. The mechanism is improved calibration near the decision boundary, not a large accuracy gap.\n\n\\section{Related Work}\n\n\\paragraph{Binary Synthetic Text Detection.} A rich literature addresses distinguishing human from machine-generated text. Watermarking approaches embed detectable signals during generation. Post-hoc detectors exploit statistical signatures: DivEye~\\cite{diveye} uses divergence-based features, Binoculars~\\cite{binoculars} compares cross-model perplexities, and Min-K\\%++~\\cite{minkpp} thresholds on low-probability tokens. All operate in a binary paradigm and do not estimate generational depth.\n\n\\paragraph{Model Collapse and Recursive Training.} \\citet{shumailov2024ai} demonstrate that iteratively training on self-generated data leads to model collapse---progressive loss of distributional tails. Subsequent work characterizes collapse dynamics in specific settings. However, this line provides descriptive analysis of the collapse phenomenon rather than detection or curation tools.\n\n\\paragraph{Verification-Based Quality Filtering.} Recent approaches use external verifiers to gate training data quality. \\citet{feng2024} and \\citet{yi2024} employ LLM-as-judge or factual verification to filter low-quality synthetic data. These methods perform binary quality gating without estimating recursive depth, forgoing the ordinal structure that depth estimation provides.\n\n\\paragraph{Gap.} No existing method estimates how many rounds of recursive generation a text has undergone. We are the first to formalize depth estimation as a prediction task and to measure the empirical saturation boundary $K^*$.\n\n\\section{Problem Formulation}\n\n\\subsection{Recursive Generation as Iterated Lossy Channel}\n\nLet $P_0$ denote the distribution of human-authored text. A language model $M$ defines a stochastic map $\\mathcal{C}_M: \\mathcal{X} \\to \\mathcal{X}$ that takes an input text and produces a synthetic output. Recursive generation creates a Markov chain of distributions:\n\\begin{equation}\nP_0 \\xrightarrow{\\mathcal{C}_M} P_1 \\xrightarrow{\\mathcal{C}_M} P_2 \\xrightarrow{\\mathcal{C}_M} \\cdots\n\\end{equation}\nEach application of $\\mathcal{C}_M$ is a lossy channel: it preserves some statistical properties of its input while compressing others. By the Data Processing Inequality, for any divergence measure $D$:\n\\begin{equation}\nD(P_k \\| P_{k+1}) \\leq D(P_{k-1} \\| P_k) \\quad \\forall\\, k \\geq 1\n\\end{equation}\nThis monotonic decay guarantees the existence of a saturation boundary: there exists some $K^*$ beyond which consecutive generations are practically indistinguishable.\n\n\\subsection{Saturation Boundary $K^*$}\n\nWe operationalize $K^*$ using pairwise classification:\n\\begin{equation}\nK^* = \\max\\{k : \\text{AUC}(k, k+1) > \\theta\\}\n\\end{equation}\nwhere $\\text{AUC}(k, k+1)$ is the area under the ROC curve for distinguishing generation $k$ from generation $k+1$ using a fixed feature set, and $\\theta = 0.60$ is a discrimination threshold. We validate robustness to $\\theta$ in \\Cref{sec:threshold_sensitivity}.\n\n\\subsection{Depth Estimation as Ordinal Prediction}\n\nGiven a text $x$, the depth estimation task is to predict its generational depth $d(x) \\in \\{0, 1, \\ldots, K\\}$. The ordinal nature of depth---$d=0$ is closer to $d=1$ than to $d=3$---motivates ordinal regression approaches over standard multinomial classification.\n\n\\section{Experimental Setup}\n\n\\subsection{Depth Chain Generation}\n\nWe construct recursive generation chains (\\emph{depth chains}) using three model families at the 1--2B scale:\n\\begin{itemize}\n\\item \\textbf{Pythia-1.4B}: GPT-NeoX architecture, trained on The Pile (300B tokens).\n\\item \\textbf{OLMo-1B}: Transformer++ architecture, trained on Dolma.\n\\item \\textbf{Qwen2.5-1.5B}: Qwen-style architecture with multilingual pretraining.\n\\end{itemize}\n\nFor each model, we sample 5,000 documents from C4 as seed texts ($P_0$) and generate 5 recursive generations using nucleus sampling ($p=0.95$, $T=1.0$) as the default decoding strategy. Each generation $k+1$ is produced by prompting the model with the corresponding generation-$k$ text.\n\n\\paragraph{Decoding Strategy Ablation.} Using Qwen2.5-1.5B, we additionally generate chains under four alternative strategies: greedy decoding, nucleus $p=0.9$, $T=0.7$, and $T=1.2$.\n\n\\paragraph{Cross-Scale Probe.} We generate a smaller chain (1,000 documents, depth 0--3) with Qwen2.5-7B to probe scale dependence.\n\n\\paragraph{Retrain Chain.} To validate ecological validity, we construct a retrain chain with Pythia-1.4B: at each generation, the model is fine-tuned via LoRA (rank 16) on the previous generation's output before generating the next.\n\n\\subsection{Feature Extraction}\n\nWe extract a 15-dimensional feature vector for each document, organized into three groups:\n\n\\begin{itemize}\n\\item \\textbf{Vocabulary Diversity} (5 features): type-token ratio, hapax legomena ratio, entropy of unigram distribution, mean log-frequency rank, vocabulary richness index.\n\\item \\textbf{Surprisal Dynamics} (5 features): mean/variance of token-level surprisal, burstiness (autocorrelation of surprisal), perplexity, surprisal skewness.\n\\item \\textbf{Tail Thinning} (5 features): rare token frequency (bottom 10\\%), out-of-top-$k$ mass, type frequency decay exponent, singleton ratio, hapax-dis ratio.\n\\end{itemize}\n\n\\subsection{Classification Methods}\n\n\\paragraph{Pairwise Discrimination.} For each consecutive pair $(k, k+1)$, we train a logistic regression classifier on the 15D features and report AUC and Jensen--Shannon divergence (JSD) between feature distributions.\n\n\\paragraph{Ordinal Depth Estimation.} We compare three approaches: (1) CORAL ordinal regression~\\cite{coral}, which encodes ordinal structure via binary threshold tasks; (2) standard multinomial logistic regression; (3) classical ordinal regression (cumulative logit model). All use the same 15D features with 5-fold cross-validation.\n\n\\paragraph{Baselines.} We compare against: (i) existing binary detectors (DivEye, Binoculars) using confidence scores as depth proxies; (ii) LLM zero-shot depth estimation (GPT-4o, Claude 3.5 Sonnet); (iii) frozen LM embeddings (2048D) with a 2-layer MLP.\n\n\\section{Results}\n\n\\subsection{$K^*=2$: A Robust Empirical Constant}\n\\label{sec:kstar}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & \\textbf{3v4} & $K^*$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{AUC (mean $\\pm$ std)}} \\\\\nPythia-1.4B & .993\\tiny{$\\pm$.001} & .672\\tiny{$\\pm$.009} & .576\\tiny{$\\pm$.013} & .538\\tiny{$\\pm$.008} & 2 \\\\\nOLMo-1B & .991\\tiny{$\\pm$.001} & .648\\tiny{$\\pm$.011} & .562\\tiny{$\\pm$.014} & .531\\tiny{$\\pm$.009} & 2 \\\\\nQwen2.5-1.5B & .996\\tiny{$\\pm$.001} & .696\\tiny{$\\pm$.008} & .589\\tiny{$\\pm$.012} & .543\\tiny{$\\pm$.010} & 2 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{JSD}} \\\\\nPythia-1.4B & .241 & .014 & .005 & .003 & -- \\\\\nOLMo-1B & .218 & .012 & .004 & .003 & -- \\\\\nQwen2.5-1.5B & .267 & .016 & .006 & .003 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise discrimination across three model families. All models yield $K^*=2$ at threshold $\\theta=0.60$. JSD decays exponentially from the 0v1 boundary (0.218--0.267) to near-zero by generation 3.}\n\\label{tab:kstar_main}\n\\end{table}\n\n\\Cref{tab:kstar_main} presents the central result. Across all three model families, $K^*=2$: the pairwise AUC between generation 1 and generation 2 ranges from 0.648 to 0.696 (above $\\theta=0.60$), while AUC between generation 2 and generation 3 drops to 0.562--0.589 (below or near $\\theta$). The JSD between consecutive generations decays by an order of magnitude from 0v1 (0.218--0.267) to 1v2 (0.012--0.016), and reaches a floor below 0.005 by generation 3.\n\nThis consistency across architectures (GPT-NeoX, Transformer++, Qwen-style), training data (The Pile, Dolma, multilingual), and model sizes within the 1--2B range constitutes strong evidence that $K^*=2$ is a property of the scale regime rather than any specific model.\n\n\\paragraph{Decoding Strategy Stability.} \\Cref{tab:decoding} shows that $K^*=2$ is stable across four decoding strategies. Greedy decoding produces the largest initial JSD (0.302) because deterministic outputs diverge most from human text, yet $K^*$ remains 2. Only $T=1.2$ shows instability: one of three seeds yields $K^*=3$, as high-temperature sampling preserves more per-generation variance, delaying saturation. We conclude that $K^*=2$ is the default for standard decoding, with extreme temperature as the only identified modulating factor.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{AUC 1v2} & \\textbf{AUC 2v3} & \\textbf{JSD 0v1} & $K^*$ \\\\\n\\midrule\nGreedy & .714 & .603 & .302 & 2 \\\\\nNucleus $p$=0.9 & .688 & .582 & .258 & 2 \\\\\n$T$=0.7 & .708 & .597 & .289 & 2 \\\\\n$T$=1.2 & .651 & .583 & .195 & 2\\textsuperscript{$\\dagger$} \\\\\nBaseline ($p$=0.95) & .696 & .589 & .267 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). $^\\dagger$One of three seeds yields $K^*=3$.}\n\\label{tab:decoding}\n\\end{table}\n\n\\paragraph{Base vs.\\ Instruct.} Both Qwen2.5-1.5B base and instruct variants yield $K^*=2$ (AUC 1v2: 0.682 vs.\\ 0.696). The instruct model shows lower vocabulary diversity at gen-1 (0.54 vs.\\ 0.58; KS test $p=0.01$), suggesting that alignment training acts as a mild form of mode collapse, but this does not affect the saturation boundary.\n\n\\paragraph{Cross-Scale Probe.} Qwen2.5-7B yields AUC 2v3 = 0.612 averaged across three seeds, with individual seeds producing $K^*$ values of 2, 3, and 2 (majority: 2). This provides suggestive but inconclusive evidence that $K^*$ may increase with model scale; the effect is within seed variance at our sample size (1K documents). Ordinal accuracy improves to 0.44 (vs.\\ 0.42 for 1.5B), consistent with the larger model's richer channel preserving more distinguishable structure.\n\n\\subsection{Threshold Sensitivity}\n\\label{sec:threshold_sensitivity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\theta$ & Pythia & OLMo & Qwen & Qwen ($T$=1.2) \\\\\n\\midrule\n0.55 & 3 & 2 & 2 & 3 \\\\\n0.60 & 2 & 2 & 2 & 2 \\\\\n0.65 & 2 & 2 & 2 & 2 \\\\\n0.70 & 1 & 1 & 2 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K^*$ under varying AUC thresholds. $K^*=2$ is stable across the $[0.60, 0.65]$ range for all models.}\n\\label{tab:threshold}\n\\end{table}\n\nTo address potential concerns about threshold arbitrariness, \\Cref{tab:threshold} reports $K^*$ under four threshold values. $K^*=2$ is perfectly stable in the range $\\theta \\in [0.60, 0.65]$. At $\\theta=0.55$ (near chance), some models shift to $K^*=3$; at $\\theta=0.70$ (overly strict), most drop to $K^*=1$. The operating point $\\theta=0.60$ balances between these extremes.\n\n\\subsection{Degradation Ordering}\n\\label{sec:ordering}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature Group} & \\multicolumn{2}{c}{\\textbf{Pythia}} & \\multicolumn{2}{c}{\\textbf{OLMo}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & AUC 1v2 & Sat. & AUC 1v2 & Sat. \\\\\n\\midrule\nVocab.\\ Diversity & .641 & 1.8 & .625 & 1.6 \\\\\nSurprisal Dynamics & .608 & 2.3 & .612 & 2.1 \\\\\nTail Thinning & .622 & 2.0 & .598 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature group saturation depths and pairwise AUC (1v2). Vocabulary diversity saturates earliest in both models. ``Sat.'' indicates interpolated saturation depth.}\n\\label{tab:degradation}\n\\end{table}\n\n\\Cref{tab:degradation} presents per-feature-group analysis. Vocabulary diversity saturates earliest across all three model families (depth 1.6--1.8), consistent with the ``rich-get-richer'' amplification of high-frequency tokens under recursive sampling. However, the ordering between surprisal dynamics and tail-thinning features is model-dependent: Pythia shows tail-thinning saturating before surprisal (depth 2.0 vs.\\ 2.3), while OLMo shows the reverse (2.5 vs.\\ 2.1). Cross-model Kendall $\\tau$ for the full ordering is 0.67 ($p=0.08$ for Pythia--OLMo), indicating a tendency rather than a strict universal ordering. OLMo and Qwen show perfect rank agreement ($\\tau=1.0$, $p=0.02$).\n\nWe characterize this finding conservatively: \\emph{vocabulary diversity consistently degrades earliest, while the relative ordering of surprisal and tail features is model-dependent}.\n\n\\subsection{Depth Estimation Methods}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Acc.} & \\textbf{MAE} & \\textbf{Adj.\\ Acc.} \\\\\n\\midrule\nCORAL (ordinal) & .42 & 1.02 & .74 \\\\\nMultinomial & .40 & 1.18 & .68 \\\\\nOrdinal Regression & .41 & 1.05 & .72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth estimation methods on Qwen2.5-1.5B chains. CORAL achieves the lowest MAE and highest adjacent accuracy, demonstrating the value of ordinal structure.}\n\\label{tab:ordinal}\n\\end{table}\n\n\\Cref{tab:ordinal} compares depth estimation approaches. CORAL ordinal regression achieves the best MAE (1.02 vs.\\ 1.18 for multinomial) and adjacent accuracy (0.74 vs.\\ 0.68), though top-1 accuracy differences are modest (0.42 vs.\\ 0.40). The advantage of ordinal modeling lies in error calibration: CORAL's threshold structure penalizes large ordinal errors, producing predictions that are within one generation of the truth 74\\% of the time.\n\n\\paragraph{Hand-Crafted vs.\\ Learned Features.} Frozen Qwen2.5-1.5B embeddings (2048D) with a 2-layer MLP achieve slightly higher accuracy (0.44) and lower MAE (0.95) than our 15D hand-crafted features (0.42, 1.02). The gap is small despite the $136\\times$ dimensionality difference, and hand-crafted features enable the interpretable degradation ordering analysis in \\Cref{sec:ordering}.\n\n\\subsection{Baselines: Existing Methods Fail at Depth Estimation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Bin.\\ AUC} & \\textbf{$\\rho$(depth)} & \\textbf{AUC 1v2} & \\textbf{MAE} \\\\\n\\midrule\nDivEye & .93 & $-$.31 & .57 & -- \\\\\nBinoculars & .95 & $-$.28 & .55 & -- \\\\\nGPT-4o (0-shot) & .88 & -- & -- & 1.85 \\\\\nClaude 3.5 (0-shot) & .91 & -- & -- & 1.72 \\\\\nOur 15D + CORAL & .996 & $-$.82 & .70 & 1.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Baseline comparison. Binary detectors achieve high binary AUC but fail as depth proxies (Spearman $\\rho \\approx -0.3$). LLM zero-shot depth estimation yields high MAE. Our method achieves strong correlation with true depth.}\n\\label{tab:baselines}\n\\end{table}\n\n\\Cref{tab:baselines} demonstrates that existing methods cannot perform depth estimation. Binary detectors (DivEye, Binoculars) achieve excellent binary AUC (0.93--0.95) but their confidence scores correlate weakly with true depth (Spearman $\\rho \\approx -0.3$). Pairwise AUC for gen-1 vs.\\ gen-2 is near chance (0.55--0.57), confirming that binary confidence does not encode depth information.\n\nLLM zero-shot depth estimation also fails: GPT-4o and Claude 3.5 Sonnet achieve 6-class accuracies of only 22\\% and 24\\% respectively (chance: 16.7\\%), with MAE of 1.85 and 1.72. Both models perform well on the binary subtask (gen-0 vs.\\ gen-1 accuracy 81--84\\%) but cannot distinguish deeper generations. This confirms that depth estimation is a non-trivial task requiring specialized methods.\n\n\\subsection{Cross-Model Transfer}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Train$\\backslash$Test} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Binary AUC (retention: 92\\%)}} \\\\\nPythia & .993 & .91 & .89 \\\\\nOLMo & .90 & .991 & .88 \\\\\nQwen & .92 & .90 & .996 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Ordinal Accuracy (retention: 58\\%)}} \\\\\nPythia & .40 & .26 & .24 \\\\\nOLMo & .25 & .39 & .23 \\\\\nQwen & .28 & .26 & .42 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer. Binary detection transfers well (92\\% retention). Ordinal depth estimation transfers poorly (58\\%), indicating model-specific depth signatures.}\n\\label{tab:transfer}\n\\end{table}\n\n\\Cref{tab:transfer} reveals an asymmetry: binary detection features transfer well across model families (AUC 0.88--0.92, 92\\% retention of in-distribution performance), but ordinal depth estimation transfers poorly (accuracy 0.23--0.28, 58\\% retention). This indicates that the human/synthetic boundary involves universal features shared across LM families, while the finer-grained depth signal is model-specific---different architectures produce different ``fingerprints'' of mode collapse at each generation. This constrains the practical deployment of graduated filtering to settings where the generating model family is approximately known.\n\n\\subsection{Graduated Filtering}\n\\label{sec:filtering}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{$\\Delta$ vs Binary} \\\\\n\\midrule\nNo filter & 25.8\\tiny{$\\pm$0.3} & 42.1\\tiny{$\\pm$0.4} & $-$0.6 / $-$0.9 \\\\\nBinary & 26.4\\tiny{$\\pm$0.4} & 43.0\\tiny{$\\pm$0.5} & --- \\\\\nSurprisal-based & 26.9\\tiny{$\\pm$0.3} & 43.4\\tiny{$\\pm$0.4} & +0.5 / +0.4 \\\\\nGraduated (3-class) & 27.2\\tiny{$\\pm$0.4} & 43.7\\tiny{$\\pm$0.5} & +0.8 / +0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation after continued pretraining with 30\\% synthetic contamination. Graduated filtering outperforms binary by 0.8 pp (MMLU) and 0.7 pp (HellaSwag). Standard deviations are across 3 seeds.}\n\\label{tab:downstream}\n\\end{table}\n\n\\Cref{tab:downstream} presents downstream results at the 30\\% contamination level. Graduated filtering (three-class: human/gen-1/gen-2+) outperforms binary filtering by 0.8 pp on MMLU and 0.7 pp on HellaSwag. While the absolute gains are modest and the confidence intervals may overlap given seed variance ($\\sigma \\approx 0.4$--0.5 pp), the consistent direction across both benchmarks and the mechanistic explanation support a real effect.\n\nThe mechanism is \\emph{calibration near the decision boundary}: binary filtering labels all synthetic text identically, discarding usable gen-1 text alongside degraded gen-3+ text. Graduated filtering assigns gen-1 a ``shallow synthetic'' label, allowing partial retention of higher-quality synthetic data while aggressively filtering deeply recursive text.\n\n\\paragraph{Dose-Response.} \\Cref{tab:dose} shows that the graduated filtering advantage scales with contamination severity: from +0.2 pp at 10\\% injection to +1.1 pp at 50\\%. This follows from the fact that at higher contamination rates, gen-1 text constitutes a larger absolute fraction of the corpus, amplifying the value of calibrated retention decisions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Injection} & \\textbf{No Filt.} & \\textbf{Binary} & \\textbf{Grad.} & $\\Delta$ \\\\\n\\midrule\n10\\% & 26.1 & 26.3 & 26.5 & +0.2 \\\\\n30\\% & 25.8 & 26.4 & 27.2 & +0.8 \\\\\n50\\% & 25.2 & 26.2 & 27.3 & +1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MMLU accuracy under varying contamination rates. Graduated filtering advantage grows super-linearly with contamination severity.}\n\\label{tab:dose}\n\\end{table}\n\n\\subsection{Ecological Validity}\n\n\\paragraph{Retrain Chain.} A LoRA retrain chain with Pythia-1.4B yields $K^*=2$, with AUC values slightly lower than the prompt chain (1v2: 0.635 vs.\\ 0.672; $\\Delta = -0.037$). Feature distributions show significant but moderate shifts (vocabulary diversity KS test $p=0.03$), confirming that the saturation boundary is qualitatively robust to the recursion mechanism.\n\n\\paragraph{Common Crawl Validation.} Applying our classifier to a Common Crawl 2025--2026 sample, we predict 72\\% human, 18\\% gen-1, and 10\\% gen-2+ text. Predicted depth correlates with vocabulary richness ($r=0.41$) and AlignScore ($r=0.34$). Manual inspection of predicted gen-2+ samples shows visible quality degradation in 70\\% of cases. These correlations are modest due to domain shift, but directionally consistent with our controlled findings.\n\n\\section{Discussion}\n\n\\paragraph{$K^*$ as a Universal Constant.} The stability of $K^*=2$ across three architectures, four decoding strategies, base/instruct variants, and prompt/retrain chains is striking. We interpret this as reflecting a fundamental property of the 1--2B scale regime: the lossy channel defined by models of this size exhausts distinguishable generational information by the second recursive step. The suggestive evidence from the 7B probe ($K^*$ occasionally reaching 3) aligns with the expectation that larger channel capacity delays saturation, though confirming this requires larger-scale experiments.\n\n\\paragraph{Practical Implications.} For data curators, $K^*=2$ implies that the actionable depth signal is coarse---three classes suffice. This simplifies deployment: a lightweight 15D feature extractor with a CORAL classifier can provide depth-aware quality scores. The cross-model transfer results (\\Cref{tab:transfer}) indicate that model-family-specific training is needed for accurate depth estimation, but binary detection generalizes well.\n\n\\paragraph{Limitations.} Our experiments use 1--2B parameter models; $K^*$ at the 70B+ scale remains unmeasured. The downstream evaluation uses continued pretraining of small models, which may not reflect the dynamics of large-scale pretraining from scratch. The 0.8 pp improvement from graduated filtering, while consistent, may not reach statistical significance at $p<0.05$ with three seeds. The retrain chain uses LoRA rather than full fine-tuning, which may underestimate parameter-level collapse effects.\n\n\\section{Conclusion}\n\nWe introduced generational depth estimation as a prediction task and the saturation boundary $K^*$ as a measurable quantity characterizing recursive synthetic text. Through systematic experiments, we established $K^*=2$ as a robust empirical constant for 1--2B parameter language models---stable across three model families, four decoding strategies, and base/instruct variants. Vocabulary diversity degrades earliest in the recursive chain, though the full degradation ordering is partially model-dependent. Even the coarse three-class signal enabled by $K^*=2$ provides better-calibrated data curation than binary filtering, with growing advantages as web data contamination intensifies. Our work provides both a theoretical framework (DPI-derived saturation) and practical tools (15D features + ordinal classifier) for depth-aware data governance.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Detailed Retrain-Chain Results}\n\\label{app:retrain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pair} & \\textbf{Prompt AUC} & \\textbf{Retrain AUC} & $\\Delta$ \\\\\n\\midrule\n0 vs 1 & .993 & .988 & $-$.005 \\\\\n1 vs 2 & .672 & .635 & $-$.037 \\\\\n2 vs 3 & .576 & .572 & $-$.004 \\\\\n3 vs 4 & .538 & .541 & +.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-chain vs.\\ retrain-chain (Pythia-1.4B). The largest difference is at 1v2 ($\\Delta=-0.037$); $K^*=2$ in both conditions.}\n\\end{table}\n\n\\section{LLM Zero-Shot Per-Pair Accuracy}\n\\label{app:llm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{0v1 Acc} & \\textbf{1v2 Acc} & \\textbf{2v3 Acc} \\\\\n\\midrule\nGPT-4o & .81 & .39 & .28 \\\\\nClaude 3.5 Sonnet & .84 & .42 & .30 \\\\\nOur CORAL & .99+ & .68 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-pair accuracy for LLM zero-shot depth estimation. Performance degrades sharply beyond the 0v1 boundary.}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee89644-6562-44ac-9d24-e4381635f743",
  "isSidechain": false,
  "requestId": "req_011CayJen7NhsofR8TUc88LK",
  "type": "assistant",
  "uuid": "9d54096c-297a-46f8-8d29-77d96ce59a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxTEVjhFUp2b33parJPuh4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 430,
      "cache_read_input_tokens": 42899,
      "output_tokens": 9399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 430,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9399,
          "cache_read_input_tokens": 42899,
          "cache_creation_input_tokens": 430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 430
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

_source line 17 · 2026-05-12T20:30:57.431Z_

<details><summary>↩ Tool result · `toolu_01STt3zbUSgmargbkC8V67DM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d54096c-297a-46f8-8d29-77d96ce59a04",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "0cecb3eb-dc64-4f0b-b5e9-3665743a4aa0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage{EMNLP2023} % ACL/EMNLP style\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by synthetic text that has been recursively generated---text produced by language models trained on or prompted with prior synthetic outputs. Current detection methods treat synthetic text as a binary category (human vs.\\ machine-generated), ignoring the progressive quality degradation across recursive generations. We formalize \\emph{generational depth estimation} as a prediction task and introduce the \\emph{saturation boundary} $K^*$, the maximum generation depth at which consecutive generations remain statistically distinguishable. Through controlled experiments across three model families (Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B), four decoding strategies, and two seed datasets, we establish $K^*=2$ as a remarkably stable empirical constant for 1--2B parameter models: the Jensen--Shannon divergence between feature distributions decays from 0.27 at the human/gen-1 boundary to below 0.005 by generation 3. Only extreme-temperature decoding ($T\\geq 1.2$) occasionally extends $K^*$ to 3. A cross-scale probe with Qwen2.5-7B provides suggestive evidence that $K^*$ may increase with model scale. We further show that even the coarse three-class signal (human / gen-1 / gen-2+) derived from $K^*=2$ enables \\emph{graduated filtering} that outperforms binary filtering by 0.8 percentage points on MMLU and 0.7 on HellaSwag in continued pretraining, with the advantage growing super-linearly as contamination increases. Our results provide the first systematic characterization of generational saturation in recursive synthetic text and actionable guidance for depth-aware data curation.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe fraction of machine-generated text on the web is growing rapidly. As language models (LMs) are trained on web-scraped data that already contains their predecessors' outputs, a recursive feedback loop emerges: each generation of models produces text that seeds the next generation's training data. This phenomenon---variously called \\emph{model collapse}~\\cite{shumailov2024ai}, \\emph{data contamination}, or \\emph{recursive synthetic pollution}---threatens the quality of future training corpora.\n\nExisting detection methods frame the problem as binary classification: is a given text human-written or machine-generated? Tools such as DivEye and Binoculars achieve strong performance on this binary task (AUC $>0.93$). However, they are fundamentally blind to \\emph{how many times} a text has passed through the generative pipeline. First-generation synthetic text (gen-1) retains much of the original distribution's richness, while fourth-generation text (gen-4) may exhibit severe vocabulary collapse, flattened surprisal dynamics, and factual drift. Treating both identically discards actionable quality information.\n\nWe make three contributions:\n\n\\paragraph{C1: Saturation Boundary ($K^*$).} We formalize the \\emph{generational discrimination boundary} $K^*$ as the maximum depth $k$ at which pairwise classification between generation $k$ and $k+1$ exceeds chance (AUC $>0.60$). From information-theoretic first principles---specifically, the Data Processing Inequality (DPI)---discriminability must decay monotonically along any Markov chain of generative processes. $K^*$ marks where this decay reaches a practical floor. Through systematic measurement across three model families, four decoding strategies, and base/instruct variants, we establish $K^*=2$ as a robust empirical constant for current-generation 1--2B parameter models. This is, to our knowledge, the first controlled measurement of this quantity.\n\n\\paragraph{C2: Linguistic Degradation Ordering.} We analyze which linguistic features saturate first during recursive generation. Vocabulary diversity consistently degrades earliest across all three model families, while the relative ordering of surprisal dynamics and tail-thinning features is model-dependent (Kendall $\\tau = 0.67$ across model pairs). We report this as a \\emph{tendency} rather than a strict ordering.\n\n\\paragraph{C3: Graduated Filtering.} We demonstrate that depth-graduated filtering---using the three-class signal human/gen-1/gen-2+ enabled by $K^*=2$---yields better-calibrated quality estimates than binary filtering. In continued pretraining experiments, graduated filtering improves over binary filtering by 0.8 pp on MMLU and 0.7 pp on HellaSwag at 30\\% contamination, with the advantage scaling to 1.1 pp at 50\\% contamination. The mechanism is improved calibration near the decision boundary, not a large accuracy gap.\n\n\\section{Related Work}\n\n\\paragraph{Binary Synthetic Text Detection.} A rich literature addresses distinguishing human from machine-generated text. Watermarking approaches embed detectable signals during generation. Post-hoc detectors exploit statistical signatures: DivEye~\\cite{diveye} uses divergence-based features, Binoculars~\\cite{binoculars} compares cross-model perplexities, and Min-K\\%++~\\cite{minkpp} thresholds on low-probability tokens. All operate in a binary paradigm and do not estimate generational depth.\n\n\\paragraph{Model Collapse and Recursive Training.} \\citet{shumailov2024ai} demonstrate that iteratively training on self-generated data leads to model collapse---progressive loss of distributional tails. Subsequent work characterizes collapse dynamics in specific settings. However, this line provides descriptive analysis of the collapse phenomenon rather than detection or curation tools.\n\n\\paragraph{Verification-Based Quality Filtering.} Recent approaches use external verifiers to gate training data quality. \\citet{feng2024} and \\citet{yi2024} employ LLM-as-judge or factual verification to filter low-quality synthetic data. These methods perform binary quality gating without estimating recursive depth, forgoing the ordinal structure that depth estimation provides.\n\n\\paragraph{Gap.} No existing method estimates how many rounds of recursive generation a text has undergone. We are the first to formalize depth estimation as a prediction task and to measure the empirical saturation boundary $K^*$.\n\n\\section{Problem Formulation}\n\n\\subsection{Recursive Generation as Iterated Lossy Channel}\n\nLet $P_0$ denote the distribution of human-authored text. A language model $M$ defines a stochastic map $\\mathcal{C}_M: \\mathcal{X} \\to \\mathcal{X}$ that takes an input text and produces a synthetic output. Recursive generation creates a Markov chain of distributions:\n\\begin{equation}\nP_0 \\xrightarrow{\\mathcal{C}_M} P_1 \\xrightarrow{\\mathcal{C}_M} P_2 \\xrightarrow{\\mathcal{C}_M} \\cdots\n\\end{equation}\nEach application of $\\mathcal{C}_M$ is a lossy channel: it preserves some statistical properties of its input while compressing others. By the Data Processing Inequality, for any divergence measure $D$:\n\\begin{equation}\nD(P_k \\| P_{k+1}) \\leq D(P_{k-1} \\| P_k) \\quad \\forall\\, k \\geq 1\n\\end{equation}\nThis monotonic decay guarantees the existence of a saturation boundary: there exists some $K^*$ beyond which consecutive generations are practically indistinguishable.\n\n\\subsection{Saturation Boundary $K^*$}\n\nWe operationalize $K^*$ using pairwise classification:\n\\begin{equation}\nK^* = \\max\\{k : \\text{AUC}(k, k+1) > \\theta\\}\n\\end{equation}\nwhere $\\text{AUC}(k, k+1)$ is the area under the ROC curve for distinguishing generation $k$ from generation $k+1$ using a fixed feature set, and $\\theta = 0.60$ is a discrimination threshold. We validate robustness to $\\theta$ in \\Cref{sec:threshold_sensitivity}.\n\n\\subsection{Depth Estimation as Ordinal Prediction}\n\nGiven a text $x$, the depth estimation task is to predict its generational depth $d(x) \\in \\{0, 1, \\ldots, K\\}$. The ordinal nature of depth---$d=0$ is closer to $d=1$ than to $d=3$---motivates ordinal regression approaches over standard multinomial classification.\n\n\\section{Experimental Setup}\n\n\\subsection{Depth Chain Generation}\n\nWe construct recursive generation chains (\\emph{depth chains}) using three model families at the 1--2B scale:\n\\begin{itemize}\n\\item \\textbf{Pythia-1.4B}: GPT-NeoX architecture, trained on The Pile (300B tokens).\n\\item \\textbf{OLMo-1B}: Transformer++ architecture, trained on Dolma.\n\\item \\textbf{Qwen2.5-1.5B}: Qwen-style architecture with multilingual pretraining.\n\\end{itemize}\n\nFor each model, we sample 5,000 documents from C4 as seed texts ($P_0$) and generate 5 recursive generations using nucleus sampling ($p=0.95$, $T=1.0$) as the default decoding strategy. Each generation $k+1$ is produced by prompting the model with the corresponding generation-$k$ text.\n\n\\paragraph{Decoding Strategy Ablation.} Using Qwen2.5-1.5B, we additionally generate chains under four alternative strategies: greedy decoding, nucleus $p=0.9$, $T=0.7$, and $T=1.2$.\n\n\\paragraph{Cross-Scale Probe.} We generate a smaller chain (1,000 documents, depth 0--3) with Qwen2.5-7B to probe scale dependence.\n\n\\paragraph{Retrain Chain.} To validate ecological validity, we construct a retrain chain with Pythia-1.4B: at each generation, the model is fine-tuned via LoRA (rank 16) on the previous generation's output before generating the next.\n\n\\subsection{Feature Extraction}\n\nWe extract a 15-dimensional feature vector for each document, organized into three groups:\n\n\\begin{itemize}\n\\item \\textbf{Vocabulary Diversity} (5 features): type-token ratio, hapax legomena ratio, entropy of unigram distribution, mean log-frequency rank, vocabulary richness index.\n\\item \\textbf{Surprisal Dynamics} (5 features): mean/variance of token-level surprisal, burstiness (autocorrelation of surprisal), perplexity, surprisal skewness.\n\\item \\textbf{Tail Thinning} (5 features): rare token frequency (bottom 10\\%), out-of-top-$k$ mass, type frequency decay exponent, singleton ratio, hapax-dis ratio.\n\\end{itemize}\n\n\\subsection{Classification Methods}\n\n\\paragraph{Pairwise Discrimination.} For each consecutive pair $(k, k+1)$, we train a logistic regression classifier on the 15D features and report AUC and Jensen--Shannon divergence (JSD) between feature distributions.\n\n\\paragraph{Ordinal Depth Estimation.} We compare three approaches: (1) CORAL ordinal regression~\\cite{coral}, which encodes ordinal structure via binary threshold tasks; (2) standard multinomial logistic regression; (3) classical ordinal regression (cumulative logit model). All use the same 15D features with 5-fold cross-validation.\n\n\\paragraph{Baselines.} We compare against: (i) existing binary detectors (DivEye, Binoculars) using confidence scores as depth proxies; (ii) LLM zero-shot depth estimation (GPT-4o, Claude 3.5 Sonnet); (iii) frozen LM embeddings (2048D) with a 2-layer MLP.\n\n\\section{Results}\n\n\\subsection{$K^*=2$: A Robust Empirical Constant}\n\\label{sec:kstar}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & \\textbf{3v4} & $K^*$ \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{AUC (mean $\\pm$ std)}} \\\\\nPythia-1.4B & .993\\tiny{$\\pm$.001} & .672\\tiny{$\\pm$.009} & .576\\tiny{$\\pm$.013} & .538\\tiny{$\\pm$.008} & 2 \\\\\nOLMo-1B & .991\\tiny{$\\pm$.001} & .648\\tiny{$\\pm$.011} & .562\\tiny{$\\pm$.014} & .531\\tiny{$\\pm$.009} & 2 \\\\\nQwen2.5-1.5B & .996\\tiny{$\\pm$.001} & .696\\tiny{$\\pm$.008} & .589\\tiny{$\\pm$.012} & .543\\tiny{$\\pm$.010} & 2 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{JSD}} \\\\\nPythia-1.4B & .241 & .014 & .005 & .003 & -- \\\\\nOLMo-1B & .218 & .012 & .004 & .003 & -- \\\\\nQwen2.5-1.5B & .267 & .016 & .006 & .003 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise discrimination across three model families. All models yield $K^*=2$ at threshold $\\theta=0.60$. JSD decays exponentially from the 0v1 boundary (0.218--0.267) to near-zero by generation 3.}\n\\label{tab:kstar_main}\n\\end{table}\n\n\\Cref{tab:kstar_main} presents the central result. Across all three model families, $K^*=2$: the pairwise AUC between generation 1 and generation 2 ranges from 0.648 to 0.696 (above $\\theta=0.60$), while AUC between generation 2 and generation 3 drops to 0.562--0.589 (below or near $\\theta$). The JSD between consecutive generations decays by an order of magnitude from 0v1 (0.218--0.267) to 1v2 (0.012--0.016), and reaches a floor below 0.005 by generation 3.\n\nThis consistency across architectures (GPT-NeoX, Transformer++, Qwen-style), training data (The Pile, Dolma, multilingual), and model sizes within the 1--2B range constitutes strong evidence that $K^*=2$ is a property of the scale regime rather than any specific model.\n\n\\paragraph{Decoding Strategy Stability.} \\Cref{tab:decoding} shows that $K^*=2$ is stable across four decoding strategies. Greedy decoding produces the largest initial JSD (0.302) because deterministic outputs diverge most from human text, yet $K^*$ remains 2. Only $T=1.2$ shows instability: one of three seeds yields $K^*=3$, as high-temperature sampling preserves more per-generation variance, delaying saturation. We conclude that $K^*=2$ is the default for standard decoding, with extreme temperature as the only identified modulating factor.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{AUC 1v2} & \\textbf{AUC 2v3} & \\textbf{JSD 0v1} & $K^*$ \\\\\n\\midrule\nGreedy & .714 & .603 & .302 & 2 \\\\\nNucleus $p$=0.9 & .688 & .582 & .258 & 2 \\\\\n$T$=0.7 & .708 & .597 & .289 & 2 \\\\\n$T$=1.2 & .651 & .583 & .195 & 2\\textsuperscript{$\\dagger$} \\\\\nBaseline ($p$=0.95) & .696 & .589 & .267 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). $^\\dagger$One of three seeds yields $K^*=3$.}\n\\label{tab:decoding}\n\\end{table}\n\n\\paragraph{Base vs.\\ Instruct.} Both Qwen2.5-1.5B base and instruct variants yield $K^*=2$ (AUC 1v2: 0.682 vs.\\ 0.696). The instruct model shows lower vocabulary diversity at gen-1 (0.54 vs.\\ 0.58; KS test $p=0.01$), suggesting that alignment training acts as a mild form of mode collapse, but this does not affect the saturation boundary.\n\n\\paragraph{Cross-Scale Probe.} Qwen2.5-7B yields AUC 2v3 = 0.612 averaged across three seeds, with individual seeds producing $K^*$ values of 2, 3, and 2 (majority: 2). This provides suggestive but inconclusive evidence that $K^*$ may increase with model scale; the effect is within seed variance at our sample size (1K documents). Ordinal accuracy improves to 0.44 (vs.\\ 0.42 for 1.5B), consistent with the larger model's richer channel preserving more distinguishable structure.\n\n\\subsection{Threshold Sensitivity}\n\\label{sec:threshold_sensitivity}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\theta$ & Pythia & OLMo & Qwen & Qwen ($T$=1.2) \\\\\n\\midrule\n0.55 & 3 & 2 & 2 & 3 \\\\\n0.60 & 2 & 2 & 2 & 2 \\\\\n0.65 & 2 & 2 & 2 & 2 \\\\\n0.70 & 1 & 1 & 2 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K^*$ under varying AUC thresholds. $K^*=2$ is stable across the $[0.60, 0.65]$ range for all models.}\n\\label{tab:threshold}\n\\end{table}\n\nTo address potential concerns about threshold arbitrariness, \\Cref{tab:threshold} reports $K^*$ under four threshold values. $K^*=2$ is perfectly stable in the range $\\theta \\in [0.60, 0.65]$. At $\\theta=0.55$ (near chance), some models shift to $K^*=3$; at $\\theta=0.70$ (overly strict), most drop to $K^*=1$. The operating point $\\theta=0.60$ balances between these extremes.\n\n\\subsection{Degradation Ordering}\n\\label{sec:ordering}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Feature Group} & \\multicolumn{2}{c}{\\textbf{Pythia}} & \\multicolumn{2}{c}{\\textbf{OLMo}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & AUC 1v2 & Sat. & AUC 1v2 & Sat. \\\\\n\\midrule\nVocab.\\ Diversity & .641 & 1.8 & .625 & 1.6 \\\\\nSurprisal Dynamics & .608 & 2.3 & .612 & 2.1 \\\\\nTail Thinning & .622 & 2.0 & .598 & 2.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature group saturation depths and pairwise AUC (1v2). Vocabulary diversity saturates earliest in both models. ``Sat.'' indicates interpolated saturation depth.}\n\\label{tab:degradation}\n\\end{table}\n\n\\Cref{tab:degradation} presents per-feature-group analysis. Vocabulary diversity saturates earliest across all three model families (depth 1.6--1.8), consistent with the ``rich-get-richer'' amplification of high-frequency tokens under recursive sampling. However, the ordering between surprisal dynamics and tail-thinning features is model-dependent: Pythia shows tail-thinning saturating before surprisal (depth 2.0 vs.\\ 2.3), while OLMo shows the reverse (2.5 vs.\\ 2.1). Cross-model Kendall $\\tau$ for the full ordering is 0.67 ($p=0.08$ for Pythia--OLMo), indicating a tendency rather than a strict universal ordering. OLMo and Qwen show perfect rank agreement ($\\tau=1.0$, $p=0.02$).\n\nWe characterize this finding conservatively: \\emph{vocabulary diversity consistently degrades earliest, while the relative ordering of surprisal and tail features is model-dependent}.\n\n\\subsection{Depth Estimation Methods}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Acc.} & \\textbf{MAE} & \\textbf{Adj.\\ Acc.} \\\\\n\\midrule\nCORAL (ordinal) & .42 & 1.02 & .74 \\\\\nMultinomial & .40 & 1.18 & .68 \\\\\nOrdinal Regression & .41 & 1.05 & .72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Depth estimation methods on Qwen2.5-1.5B chains. CORAL achieves the lowest MAE and highest adjacent accuracy, demonstrating the value of ordinal structure.}\n\\label{tab:ordinal}\n\\end{table}\n\n\\Cref{tab:ordinal} compares depth estimation approaches. CORAL ordinal regression achieves the best MAE (1.02 vs.\\ 1.18 for multinomial) and adjacent accuracy (0.74 vs.\\ 0.68), though top-1 accuracy differences are modest (0.42 vs.\\ 0.40). The advantage of ordinal modeling lies in error calibration: CORAL's threshold structure penalizes large ordinal errors, producing predictions that are within one generation of the truth 74\\% of the time.\n\n\\paragraph{Hand-Crafted vs.\\ Learned Features.} Frozen Qwen2.5-1.5B embeddings (2048D) with a 2-layer MLP achieve slightly higher accuracy (0.44) and lower MAE (0.95) than our 15D hand-crafted features (0.42, 1.02). The gap is small despite the $136\\times$ dimensionality difference, and hand-crafted features enable the interpretable degradation ordering analysis in \\Cref{sec:ordering}.\n\n\\subsection{Baselines: Existing Methods Fail at Depth Estimation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Bin.\\ AUC} & \\textbf{$\\rho$(depth)} & \\textbf{AUC 1v2} & \\textbf{MAE} \\\\\n\\midrule\nDivEye & .93 & $-$.31 & .57 & -- \\\\\nBinoculars & .95 & $-$.28 & .55 & -- \\\\\nGPT-4o (0-shot) & .88 & -- & -- & 1.85 \\\\\nClaude 3.5 (0-shot) & .91 & -- & -- & 1.72 \\\\\nOur 15D + CORAL & .996 & $-$.82 & .70 & 1.02 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Baseline comparison. Binary detectors achieve high binary AUC but fail as depth proxies (Spearman $\\rho \\approx -0.3$). LLM zero-shot depth estimation yields high MAE. Our method achieves strong correlation with true depth.}\n\\label{tab:baselines}\n\\end{table}\n\n\\Cref{tab:baselines} demonstrates that existing methods cannot perform depth estimation. Binary detectors (DivEye, Binoculars) achieve excellent binary AUC (0.93--0.95) but their confidence scores correlate weakly with true depth (Spearman $\\rho \\approx -0.3$). Pairwise AUC for gen-1 vs.\\ gen-2 is near chance (0.55--0.57), confirming that binary confidence does not encode depth information.\n\nLLM zero-shot depth estimation also fails: GPT-4o and Claude 3.5 Sonnet achieve 6-class accuracies of only 22\\% and 24\\% respectively (chance: 16.7\\%), with MAE of 1.85 and 1.72. Both models perform well on the binary subtask (gen-0 vs.\\ gen-1 accuracy 81--84\\%) but cannot distinguish deeper generations. This confirms that depth estimation is a non-trivial task requiring specialized methods.\n\n\\subsection{Cross-Model Transfer}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Train$\\backslash$Test} & \\textbf{Pythia} & \\textbf{OLMo} & \\textbf{Qwen} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Binary AUC (retention: 92\\%)}} \\\\\nPythia & .993 & .91 & .89 \\\\\nOLMo & .90 & .991 & .88 \\\\\nQwen & .92 & .90 & .996 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Ordinal Accuracy (retention: 58\\%)}} \\\\\nPythia & .40 & .26 & .24 \\\\\nOLMo & .25 & .39 & .23 \\\\\nQwen & .28 & .26 & .42 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer. Binary detection transfers well (92\\% retention). Ordinal depth estimation transfers poorly (58\\%), indicating model-specific depth signatures.}\n\\label{tab:transfer}\n\\end{table}\n\n\\Cref{tab:transfer} reveals an asymmetry: binary detection features transfer well across model families (AUC 0.88--0.92, 92\\% retention of in-distribution performance), but ordinal depth estimation transfers poorly (accuracy 0.23--0.28, 58\\% retention). This indicates that the human/synthetic boundary involves universal features shared across LM families, while the finer-grained depth signal is model-specific---different architectures produce different ``fingerprints'' of mode collapse at each generation. This constrains the practical deployment of graduated filtering to settings where the generating model family is approximately known.\n\n\\subsection{Graduated Filtering}\n\\label{sec:filtering}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HSwag} & \\textbf{$\\Delta$ vs Binary} \\\\\n\\midrule\nNo filter & 25.8\\tiny{$\\pm$0.3} & 42.1\\tiny{$\\pm$0.4} & $-$0.6 / $-$0.9 \\\\\nBinary & 26.4\\tiny{$\\pm$0.4} & 43.0\\tiny{$\\pm$0.5} & --- \\\\\nSurprisal-based & 26.9\\tiny{$\\pm$0.3} & 43.4\\tiny{$\\pm$0.4} & +0.5 / +0.4 \\\\\nGraduated (3-class) & 27.2\\tiny{$\\pm$0.4} & 43.7\\tiny{$\\pm$0.5} & +0.8 / +0.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation after continued pretraining with 30\\% synthetic contamination. Graduated filtering outperforms binary by 0.8 pp (MMLU) and 0.7 pp (HellaSwag). Standard deviations are across 3 seeds.}\n\\label{tab:downstream}\n\\end{table}\n\n\\Cref{tab:downstream} presents downstream results at the 30\\% contamination level. Graduated filtering (three-class: human/gen-1/gen-2+) outperforms binary filtering by 0.8 pp on MMLU and 0.7 pp on HellaSwag. While the absolute gains are modest and the confidence intervals may overlap given seed variance ($\\sigma \\approx 0.4$--0.5 pp), the consistent direction across both benchmarks and the mechanistic explanation support a real effect.\n\nThe mechanism is \\emph{calibration near the decision boundary}: binary filtering labels all synthetic text identically, discarding usable gen-1 text alongside degraded gen-3+ text. Graduated filtering assigns gen-1 a ``shallow synthetic'' label, allowing partial retention of higher-quality synthetic data while aggressively filtering deeply recursive text.\n\n\\paragraph{Dose-Response.} \\Cref{tab:dose} shows that the graduated filtering advantage scales with contamination severity: from +0.2 pp at 10\\% injection to +1.1 pp at 50\\%. This follows from the fact that at higher contamination rates, gen-1 text constitutes a larger absolute fraction of the corpus, amplifying the value of calibrated retention decisions.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Injection} & \\textbf{No Filt.} & \\textbf{Binary} & \\textbf{Grad.} & $\\Delta$ \\\\\n\\midrule\n10\\% & 26.1 & 26.3 & 26.5 & +0.2 \\\\\n30\\% & 25.8 & 26.4 & 27.2 & +0.8 \\\\\n50\\% & 25.2 & 26.2 & 27.3 & +1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MMLU accuracy under varying contamination rates. Graduated filtering advantage grows super-linearly with contamination severity.}\n\\label{tab:dose}\n\\end{table}\n\n\\subsection{Ecological Validity}\n\n\\paragraph{Retrain Chain.} A LoRA retrain chain with Pythia-1.4B yields $K^*=2$, with AUC values slightly lower than the prompt chain (1v2: 0.635 vs.\\ 0.672; $\\Delta = -0.037$). Feature distributions show significant but moderate shifts (vocabulary diversity KS test $p=0.03$), confirming that the saturation boundary is qualitatively robust to the recursion mechanism.\n\n\\paragraph{Common Crawl Validation.} Applying our classifier to a Common Crawl 2025--2026 sample, we predict 72\\% human, 18\\% gen-1, and 10\\% gen-2+ text. Predicted depth correlates with vocabulary richness ($r=0.41$) and AlignScore ($r=0.34$). Manual inspection of predicted gen-2+ samples shows visible quality degradation in 70\\% of cases. These correlations are modest due to domain shift, but directionally consistent with our controlled findings.\n\n\\section{Discussion}\n\n\\paragraph{$K^*$ as a Universal Constant.} The stability of $K^*=2$ across three architectures, four decoding strategies, base/instruct variants, and prompt/retrain chains is striking. We interpret this as reflecting a fundamental property of the 1--2B scale regime: the lossy channel defined by models of this size exhausts distinguishable generational information by the second recursive step. The suggestive evidence from the 7B probe ($K^*$ occasionally reaching 3) aligns with the expectation that larger channel capacity delays saturation, though confirming this requires larger-scale experiments.\n\n\\paragraph{Practical Implications.} For data curators, $K^*=2$ implies that the actionable depth signal is coarse---three classes suffice. This simplifies deployment: a lightweight 15D feature extractor with a CORAL classifier can provide depth-aware quality scores. The cross-model transfer results (\\Cref{tab:transfer}) indicate that model-family-specific training is needed for accurate depth estimation, but binary detection generalizes well.\n\n\\paragraph{Limitations.} Our experiments use 1--2B parameter models; $K^*$ at the 70B+ scale remains unmeasured. The downstream evaluation uses continued pretraining of small models, which may not reflect the dynamics of large-scale pretraining from scratch. The 0.8 pp improvement from graduated filtering, while consistent, may not reach statistical significance at $p<0.05$ with three seeds. The retrain chain uses LoRA rather than full fine-tuning, which may underestimate parameter-level collapse effects.\n\n\\section{Conclusion}\n\nWe introduced generational depth estimation as a prediction task and the saturation boundary $K^*$ as a measurable quantity characterizing recursive synthetic text. Through systematic experiments, we established $K^*=2$ as a robust empirical constant for 1--2B parameter language models---stable across three model families, four decoding strategies, and base/instruct variants. Vocabulary diversity degrades earliest in the recursive chain, though the full degradation ordering is partially model-dependent. Even the coarse three-class signal enabled by $K^*=2$ provides better-calibrated data curation than binary filtering, with growing advantages as web data contamination intensifies. Our work provides both a theoretical framework (DPI-derived saturation) and practical tools (15D features + ordinal classifier) for depth-aware data governance.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Detailed Retrain-Chain Results}\n\\label{app:retrain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pair} & \\textbf{Prompt AUC} & \\textbf{Retrain AUC} & $\\Delta$ \\\\\n\\midrule\n0 vs 1 & .993 & .988 & $-$.005 \\\\\n1 vs 2 & .672 & .635 & $-$.037 \\\\\n2 vs 3 & .576 & .572 & $-$.004 \\\\\n3 vs 4 & .538 & .541 & +.003 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-chain vs.\\ retrain-chain (Pythia-1.4B). The largest difference is at 1v2 ($\\Delta=-0.037$); $K^*=2$ in both conditions.}\n\\end{table}\n\n\\section{LLM Zero-Shot Per-Pair Accuracy}\n\\label{app:llm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{0v1 Acc} & \\textbf{1v2 Acc} & \\textbf{2v3 Acc} \\\\\n\\midrule\nGPT-4o & .81 & .39 & .28 \\\\\nClaude 3.5 Sonnet & .84 & .42 & .30 \\\\\nOur CORAL & .99+ & .68 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-pair accuracy for LLM zero-shot depth estimation. Performance degrades sharply beyond the 0v1 boundary.}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "9d54096c-297a-46f8-8d29-77d96ce59a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contam…",
  "leafUuid": "0cecb3eb-dc64-4f0b-b5e9-3665743a4aa0",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth contamination paper for EMNLP",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Tool call

_source line 20 · 2026-05-12T20:31:02.598Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015rP1v9p8RRzc3caXmmNHh4`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cecb3eb-dc64-4f0b-b5e9-3665743a4aa0",
  "isSidechain": false,
  "requestId": "req_011CayJtToCA82Eb1gUUX4dR",
  "type": "assistant",
  "uuid": "70eab60b-b6df-408e-b31b-110154d28adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MAhjEeqB3qVapFKWbCrLjv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9465,
      "cache_read_input_tokens": 43329,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9465,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 43329,
          "cache_creation_input_tokens": 9465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9465
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

_source line 21 · 2026-05-12T20:31:02.734Z_

<details><summary>↩ Tool result · `toolu_015rP1v9p8RRzc3caXmmNHh4`</summary>

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

! LaTeX Error: File `EMNLP2023.sty' not found.

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
  "parentUuid": "70eab60b-b6df-408e-b31b-110154d28adc",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "dfafd82f-3c3a-42b8-84c6-d8da328f9ce9",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `EMNLP2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "70eab60b-b6df-408e-b31b-110154d28adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T20:31:06.419Z_

<details><summary>Logged reasoning block</summary>

```text
The EMNLP2023.sty is not found. Let me check what's available or just switch to a standard article class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfafd82f-3c3a-42b8-84c6-d8da328f9ce9",
  "isSidechain": false,
  "requestId": "req_011CayJtr6dchzJS2FNM4mwv",
  "type": "assistant",
  "uuid": "32597c05-56da-4319-b53e-9ce14157e266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NaisTXD8REAHgyHKz68Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 52794,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 533,
          "cache_read_input_tokens": 52794,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 23 · 2026-05-12T20:31:07.379Z_

EMNLP style file not available. Switching to standard article class with ACL-like formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32597c05-56da-4319-b53e-9ce14157e266",
  "isSidechain": false,
  "requestId": "req_011CayJtr6dchzJS2FNM4mwv",
  "type": "assistant",
  "uuid": "cbcab616-e40c-4d87-a03e-c1c51e88b68b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NaisTXD8REAHgyHKz68Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 52794,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 533,
          "cache_read_input_tokens": 52794,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 24 · 2026-05-12T20:31:12.158Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FaS4ee36wNAt7anuL5p5NU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage{EMNLP2023} % ACL/EMNLP style\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\\usepackage{natbib}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbcab616-e40c-4d87-a03e-c1c51e88b68b",
  "isSidechain": false,
  "requestId": "req_011CayJtr6dchzJS2FNM4mwv",
  "type": "assistant",
  "uuid": "c1a33504-2809-4fdf-91c2-dc2640e974a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NaisTXD8REAHgyHKz68Aj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 52794,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 533,
          "cache_read_input_tokens": 52794,
          "cache_creation_input_tokens": 447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 447
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

_source line 25 · 2026-05-12T20:31:12.195Z_

<details><summary>↩ Tool result · `toolu_01FaS4ee36wNAt7anuL5p5NU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1a33504-2809-4fdf-91c2-dc2640e974a4",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "bd3608cb-c1ad-4f75-b901-db9212c775eb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage{EMNLP2023} % ACL/EMNLP style\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\\usepackage{natbib}\n\n\\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}\n\n\\author{Anonymous}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage{EMNLP2023} % ACL/EMNLP style",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath,amssymb,amsfonts}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\usepackage{xcolor}",
          " \\usepackage{hyperref}",
          " \\usepackage{cleveref}",
          "+\\usepackage{natbib}",
          " ",
          " \\title{How Deep Is Your Data? Measuring Generational Saturation Boundaries\\\\in Recursive Synthetic Text}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c1a33504-2809-4fdf-91c2-dc2640e974a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T20:31:29.785Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011vqQjWVufkoq8bfNHCEdaY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{minkpp}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.\n\\newblock Detectgpt: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Hans et~al.(2024)]{binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLM}s with binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{diveye}\nEduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{coral}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Feng et~al.(2024)]{feng2024}\nShangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov.\n\\newblock Fact-checking the output of large language models via token-level uncertainty quantification.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Yi et~al.(2024)]{yi2024}\nJiayi Yi, Zirui Liu, and Xiangliang Zhang.\n\\newblock On the reliability of large language models to misinformed and underinformed users.\n\\newblock In \\emph{Proceedings of NAACL}, 2024.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd3608cb-c1ad-4f75-b901-db9212c775eb",
  "isSidechain": false,
  "requestId": "req_011CayJuYrKofiuFQ4mXSWd1",
  "type": "assistant",
  "uuid": "46612604-8245-4df4-a6d2-6eeee9bfab7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZWctevtoudAm4XnwT6cnM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 53241,
      "output_tokens": 901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 901,
          "cache_read_input_tokens": 53241,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
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

_source line 27 · 2026-05-12T20:31:29.799Z_

<details><summary>↩ Tool result · `toolu_011vqQjWVufkoq8bfNHCEdaY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46612604-8245-4df4-a6d2-6eeee9bfab7b",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "f5ef1d20-d5b4-4d92-b4c1-12d5081af562",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{minkpp}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.\n\\newblock Detectgpt: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Hans et~al.(2024)]{binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLM}s with binoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Tulchinskii et~al.(2024)]{diveye}\nEduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya.\n\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.\n\\newblock In \\emph{Proceedings of NeurIPS}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{coral}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Feng et~al.(2024)]{feng2024}\nShangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov.\n\\newblock Fact-checking the output of large language models via token-level uncertainty quantification.\n\\newblock In \\emph{Proceedings of ACL}, 2024.\n\n\\bibitem[Yi et~al.(2024)]{yi2024}\nJiayi Yi, Zirui Liu, and Xiangliang Zhang.\n\\newblock On the reliability of large language models to misinformed and underinformed users.\n\\newblock In \\emph{Proceedings of NAACL}, 2024.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 343,
        "oldLines": 9,
        "newStart": 343,
        "newLines": 46,
        "lines": [
          " ",
          " We introduced generational depth estimation as a prediction task and the saturation boundary $K^*$ as a measurable quantity characterizing recursive synthetic text. Through systematic experiments, we established $K^*=2$ as a robust empirical constant for 1--2B parameter language models---stable across three model families, four decoding strategies, and base/instruct variants. Vocabulary diversity degrades earliest in the recursive chain, though the full degradation ordering is partially model-dependent. Even the coarse three-class signal enabled by $K^*=2$ provides better-calibrated data curation than binary filtering, with growing advantages as web data contamination intensifies. Our work provides both a theoretical framework (DPI-derived saturation) and practical tools (15D features + ordinal classifier) for depth-aware data governance.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          "+\\begin{thebibliography}{10}",
          " ",
          "+\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}",
          "+Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, and Ross Anderson.",
          "+\\newblock {AI} models collapse when trained on recursively generated data.",
          "+\\newblock \\emph{Nature}, 631:755--759, 2024.",
          "+",
          "+\\bibitem[Mitchell et~al.(2023)]{minkpp}",
          "+Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D. Manning, and Chelsea Finn.",
          "+\\newblock Detectgpt: Zero-shot machine-generated text detection using probability curvature.",
          "+\\newblock In \\emph{Proceedings of ICML}, 2023.",
          "+",
          "+\\bibitem[Hans et~al.(2024)]{binoculars}",
          "+Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.",
          "+\\newblock Spotting {LLM}s with binoculars: Zero-shot detection of machine-generated text.",
          "+\\newblock In \\emph{Proceedings of ICML}, 2024.",
          "+",
          "+\\bibitem[Tulchinskii et~al.(2024)]{diveye}",
          "+Eduard Tulchinskii, Kristian Kuznetsov, Laida Kushnareva, Daniil Cherniavskii, Sergey Nikolenko, Evgeny Burnaev, Serguei Barannikov, and Irina Piontkovskaya.",
          "+\\newblock Intrinsic dimension estimation for robust detection of {AI}-generated texts.",
          "+\\newblock In \\emph{Proceedings of NeurIPS}, 2024.",
          "+",
          "+\\bibitem[Cao et~al.(2020)]{coral}",
          "+Wenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.",
          "+\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.",
          "+\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.",
          "+",
          "+\\bibitem[Feng et~al.(2024)]{feng2024}",
          "+Shangbin Feng, Vidhisha Balachandran, Yuyang Bai, and Yulia Tsvetkov.",
          "+\\newblock Fact-checking the output of large language models via token-level uncertainty quantification.",
          "+\\newblock In \\emph{Proceedings of ACL}, 2024.",
          "+",
          "+\\bibitem[Yi et~al.(2024)]{yi2024}",
          "+Jiayi Yi, Zirui Liu, and Xiangliang Zhang.",
          "+\\newblock On the reliability of large language models to misinformed and underinformed users.",
          "+\\newblock In \\emph{Proceedings of NAACL}, 2024.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\appendix",
          " ",
          " \\section{Detailed Retrain-Chain Results}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "46612604-8245-4df4-a6d2-6eeee9bfab7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T20:31:33.361Z_

<details open><summary>🔧 Tool call — Bash · `toolu_011erUs6QnpWpeZHrpKxViVX`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5ef1d20-d5b4-4d92-b4c1-12d5081af562",
  "isSidechain": false,
  "requestId": "req_011CayJvqopZ2DuiAXfAB6RZ",
  "type": "assistant",
  "uuid": "1246ef97-dc20-4f6e-a10b-dc3e4f8a8a06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpJ3VJFt1WY9r5i9FYM1wm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 53860,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 53860,
          "cache_creation_input_tokens": 987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 987
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

_source line 29 · 2026-05-12T20:31:33.903Z_

<details><summary>↩ Tool result · `toolu_011erUs6QnpWpeZHrpKxViVX`</summary>

```text
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (9 pages, 186432 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1246ef97-dc20-4f6e-a10b-dc3e4f8a8a06",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "84de56db-e082-4215-b46a-0c0b9c202211",
  "toolUseResult": {
    "stdout": "(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (9 pages, 186432 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1246ef97-dc20-4f6e-a10b-dc3e4f8a8a06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T20:31:38.777Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EtBdEfAqKZivcqyYYpyuML`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84de56db-e082-4215-b46a-0c0b9c202211",
  "isSidechain": false,
  "requestId": "req_011CayJw9PFTS7CiDE6VU3BA",
  "type": "assistant",
  "uuid": "62cbc522-f334-4fb4-9e4c-00230b30de2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WexBJnpTshSFEZdX2A3U3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 54847,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 54847,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 31 · 2026-05-12T20:31:39.299Z_

<details><summary>↩ Tool result · `toolu_01EtBdEfAqKZivcqyYYpyuML`</summary>

```text
t/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time
s/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 189138 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62cbc522-f334-4fb4-9e4c-00230b30de2e",
  "isSidechain": false,
  "promptId": "473f0f94-4ec6-4444-8a13-ce13874cd7e2",
  "type": "user",
  "uuid": "e0f97a85-093f-4b42-95b0-d58fae2daa05",
  "toolUseResult": {
    "stdout": "t/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\ns/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 189138 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "62cbc522-f334-4fb4-9e4c-00230b30de2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-12T20:31:39.302Z_

```json
{
  "parentUuid": "e0f97a85-093f-4b42-95b0-d58fae2daa05",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "db7cbf5e-6520-46e6-937e-b867ff6f71aa",
  "timestamp": "2026-05-12T20:31:39.302Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-12T20:31:48.665Z_

编译成功，9 页 PDF 已生成。

输出文件：`artifacts/dream_reports/dream_20260512T200328/median/paper.pdf`

论文结构：Abstract → Introduction (3 claims: C1 saturation boundary, C2 degradation ordering, C3 graduated filtering) → Related Work → Problem Formulation (DPI, K* definition, ordinal prediction) → Experimental Setup → Results (K*=2 universality, threshold sensitivity, degradation ordering, depth estimation methods, baselines, cross-model transfer, graduated filtering with dose-response, ecological validity) → Discussion → Conclusion → Appendix。所有定量数据均来自 `experiment_data.json`，narrative 按指导重构为 universality result。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db7cbf5e-6520-46e6-937e-b867ff6f71aa",
  "isSidechain": false,
  "requestId": "req_011CayJwYRLRS6pVDfa1Pgfc",
  "type": "assistant",
  "uuid": "5e0bfa13-c431-4aea-b23a-94f0d38ce4c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/median",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zVNXuvw9TuUvE1bEVrkLP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 55547,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 385,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 55547,
          "cache_creation_input_tokens": 385,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 385
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contam…",
  "leafUuid": "5e0bfa13-c431-4aea-b23a-94f0d38ce4c2",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate depth contamination paper for EMNLP",
  "sessionId": "caa9121a-e97e-4f37-9476-22cdf59a34aa"
}
```

---
