# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/858b0d51-d42d-4da5-bcf3-851792c21102.jsonl`
- **Structured JSON:** [`8a1e2bfaa5056b11b580.json`](../../sessions/8a/8a1e2bfaa5056b11b580.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T20:31:50.755Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T20:31:50.755Z",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026\n- Narrative guidance：需要重构 story：从 method paper 转型为 empirical analysis / negative-result paper。 新 framing：\"递归合成文本的代际信号在 depth 2 后迅速坍缩到不可区分——这是 DPI 的直接后果， 且当前 1-7B 规模模型无法通过解码策略调控。这一负面结果本身具有重要实践意义： 它表明 depth-aware curation 的窗口极窄（仅 human vs gen-1 vs gen-2+），数据治理应聚焦于 first-generation detection 而非精细 depth estimation。\" C1 变为纯 characterization（\"K*=2 is a hard, universal ceiling\"），C2 被 drop 或降级到 appendix， C3 从\"graduated filtering works\"变为\"graduated filtering has fundamental limits explained by rapid signal collapse\"。 论文价值来自 rigorous negative characterization + DPI 理论预测的实验验证 + 对社区的 cautionary message。 投稿策略：EMNLP Findings 或 AAAI 2027；也可考虑 workshop paper (SyntheticData@NeurIPS)。\n\n- paper_framing.md 节选：\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Core Claims (3 条)\n\n1. **C1 (Saturation Boundary)**: 递归合成文本的代际辨别能力存在可测量的饱和边界 K*，这是一个信息论基本量（DPI 的必然推论），而非分类器能力上限。首次在受控实验中系统测量 K* 并表征其随模型、解码策略的变化。\n2. **C2 (Linguistic Degradation Ordering)**: 递归生成导致语言特征按特定顺序逐层坍缩——vocabulary diversity 先于 surprisal dynamics 饱和，揭示递归生成的结构性规律。\n3. **C3 (Graduated Filtering)**: 即使在 K*=2 的粗粒度 ordinal signal（human/gen-1/gen-2+三级）下，depth-graduated filtering 仍优于 binary filtering，因为 ordinal signal 在阈值附近提供更 calibrated 的质量估计。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al.) 描述宏观现象但不提供检测工具；verification-based methods (Feng et al., Yi et al.) 用外部验证器做 binary quality gate 但不估计递归深度。**无任何方法估计文本经历了多少轮递归生成。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（Data Processing Inequality）推导出辨别饱和边界 K* 的必然存在。K* 本身是首次测量的基本量——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过系统测量 K* 随模型架构和解码策略的变化，揭示控制 K* 的因素，为实际数据治理提供 actionable guidance。\n- **Headline result template**: \"We establish K*=2 as the generational discrimination boundary for 1.5B-scale models under standard decoding, with JSD decaying monotonically (0.27→0.004) across 5 generations, and demonstrate that even this coarse 3-class signal yields X% improvement over binary filtering on MMLU/HellaSwag.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*=2 太浅，graduated filtering 收益有限\"** → K* 是模型/解码策略依赖的；展示不同解码策略（高温度/low top-p）如何调控 K*；即使 K*=2，3-class 比 binary 在阈值附近更 calibrated\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation（首次将 depth estimation 作为 prediction task）+ empirical characterization（首次测量 K*）+ 理论框架（DPI impossibility boundary），不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法；wild data 的 Common Crawl 验证作为 appendix\n4. **\"单模型/单数据集，泛化性不够\"** → 扩展到 3 个模型族（Pythia/OLMo/Qwen）+ cross-scale probe（7B）+ 2 个种子数据集\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → 显式讨论此 design choice：这衡量的是\"模型对自身递归输出的 self-recognition\"，与 binary detection 的 premise 一致；cross-model transfer 实验验证特征不是模型特异的\n6. **\"为什么不用 learned representations\"** → 作为 baseline 对比（frozen LM embeddings + MLP），但 hand-crafted features 更 interpretable 且支持 degradation ordering 分析\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 本文同时是 method（depth estimation algorithm）和 empirical study（K* characterization），符合 EMNLP 对 \"Resources and Evaluation\" track 的要求\n- 风险：如果审稿人偏 methods，K*=2 + standard classifier 可能被认为贡献不足 → 强调 problem formulation + characterization 的 novelty\n\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T20:31:50.758Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T20:31:50.758Z",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-12T20:31:50.775Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026
- Narrative guidance：需要重构 story：从 method paper 转型为 empirical analysis / negative-result paper。 新 framing："递归合成文本的代际信号在 depth 2 后迅速坍缩到不可区分——这是 DPI 的直接后果， 且当前 1-7B 规模模型无法通过解码策略调控。这一负面结果本身具有重要实践意义： 它表明 depth-aware curation 的窗口极窄（仅 human vs gen-1 vs gen-2+），数据治理应聚焦于 first-generation detection 而非精细 depth estimation。" C1 变为纯 characterization（"K*=2 is a hard, universal ceiling"），C2 被 drop 或降级到 appendix， C3 从"graduated filtering works"变为"graduated filtering has fundamental limits explained by rapid signal collapse"。 论文价值来自 rigorous negative characterization + DPI 理论预测的实验验证 + 对社区的 cautionary message。 投稿策略：EMNLP Findings 或 AAAI 2027；也可考虑 workshop paper (SyntheticData@NeurIPS)。

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
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "2187cff3-a13e-4c89-b19b-bb8b499ed22b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T20:31:50.774Z_

```json
{
  "parentUuid": "2187cff3-a13e-4c89-b19b-bb8b499ed22b",
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
  "uuid": "c99453e5-5dad-4d17-8a88-b16ee09121eb",
  "timestamp": "2026-05-12T20:31:50.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T20:31:50.774Z_

```json
{
  "parentUuid": "c99453e5-5dad-4d17-8a88-b16ee09121eb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dc752b53-dc00-468b-aa5a-f73d1f01717a",
  "timestamp": "2026-05-12T20:31:50.774Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
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
  "aiTitle": "Characterizing generational depth saturation in synthetic text",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Assistant

_source line 7 · 2026-05-12T20:31:55.187Z_

Let me start by reading the experiment data and understanding the project structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc752b53-dc00-468b-aa5a-f73d1f01717a",
  "isSidechain": false,
  "requestId": "req_011CayJxPg1EaGf961uBQyzr",
  "type": "assistant",
  "uuid": "cb205ee8-6cac-4b7a-9197-9587a233753c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9tc77bK22uDKq2zh2p5sE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12670,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12670
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

_source line 8 · 2026-05-12T20:31:55.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C3NTnuSU3crDpzyNrBxbqd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb205ee8-6cac-4b7a-9197-9587a233753c",
  "isSidechain": false,
  "requestId": "req_011CayJxPg1EaGf961uBQyzr",
  "type": "assistant",
  "uuid": "eb1dd495-7f7a-46f9-ad06-a44b1aa5391f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9tc77bK22uDKq2zh2p5sE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12670,
      "cache_read_input_tokens": 11841,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12670
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

_source line 9 · 2026-05-12T20:31:56.066Z_

<details><summary>↩ Tool result · `toolu_01C3NTnuSU3crDpzyNrBxbqd`</summary>

```text
1	[
2	  {
3	    "name": "Pythia-1.4B cross-model depth chain",
4	    "description": "Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。\n",
5	    "results": {
6	      "k_star": 2,
7	      "pairwise_auc_0v1": 0.991,
8	      "pairwise_auc_1v2": 0.63,
9	      "pairwise_auc_2v3": 0.55,
10	      "pairwise_auc_3v4": 0.52,
11	      "pairwise_auc_4v5": 0.51,
12	      "pairwise_auc_0v1_std": 0.001,
13	      "pairwise_auc_1v2_std": 0.009,
14	      "pairwise_auc_2v3_std": 0.015,
15	      "pairwise_auc_3v4_std": 0.008,
16	      "pairwise_auc_4v5_std": 0.01,
17	      "pairwise_jsd_0v1": 0.231,
18	      "pairwise_jsd_1v2": 0.012,
19	      "pairwise_jsd_2v3": 0.004,
20	      "pairwise_jsd_3v4": 0.002,
21	      "pairwise_jsd_4v5": 0.002,
22	      "ordinal_accuracy": 0.35,
23	      "ordinal_mae": 1.18
24	    },
25	    "tables": [
26	      {
27	        "name": "Table: Pythia-1.4B pairwise discrimination",
28	        "columns": [
29	          "depth_pair",
30	          "AUC_mean",
31	          "AUC_std",
32	          "JSD"
33	        ],
34	        "rows": [
35	          [
36	            "0 vs 1",
37	            0.991,
38	            0.001,
39	            0.231
40	          ],
41	          [
42	            "1 vs 2",
43	            0.63,
44	            0.009,
45	            0.012
46	          ],
47	          [
48	            "2 vs 3",
49	            0.55,
50	            0.015,
51	            0.004
52	          ],
53	          [
54	            "3 vs 4",
55	            0.52,
56	            0.008,
57	            0.002
58	          ],
59	          [
60	            "4 vs 5",
61	            0.51,
62	            0.01,
63	            0.002
64	          ]
65	        ]
66	      }
67	    ],
68	    "figures": [],
69	    "analysis": "Pythia-1.4B 复现了 MVP 的核心发现：K*=2，且 depth 2+ 区域信号坍缩。 0v1 JSD 较 Qwen 低约 13%，可能因为 Pythia 的 base generation quality 更低， human-gen1 boundary 本身就不如 Qwen 清晰。但 K* 不变——这对 worst 叙事是关键证据： K*=2 不是 Qwen-specific artifact，而是当前规模模型的 fundamental limitation。 ordinal MAE 1.18 表明平均预测偏差超过 1 个 depth level，graduated estimation 实用性极低。\n\n\nPythia-1.4B 是较早一代架构（GPT-NeoX based），训练数据量和质量低于 Qwen2.5-1.5B。 在 worst 档下，Pythia 的 pairwise AUC 1v2 低于 MVP（0.63 vs 0.70），因为 Pythia 的 generation 质量本身更低——第一代输出已经引入更大噪声，使得后续代际之间的差异更快被噪声淹没。 JSD 从 0v1 的 0.231 迅速衰减到 1v2 的 0.012，与 DPI 预测的指数衰减一致。 depth 2+ 区域 AUC 在 0.51-0.55 之间，接近 chance level。 ordinal_accuracy 仅 0.35，因 depth 2-5 几乎不可区分，classifier 在这些类上接近随机猜测。 这强化了 K*=2 的 universality claim——即使换了不同架构家族，ceiling 不变。\n"
70	  },
71	  {
72	    "name": "OLMo-1B cross-model depth chain",
73	    "description": "OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5.\n",
74	    "results": {
75	      "k_star": 2,
76	      "pairwise_auc_0v1": 0.988,
77	      "pairwise_auc_1v2": 0.61,
78	      "pairwise_auc_2v3": 0.54,
79	      "pairwise_auc_3v4": 0.52,
80	      "pairwise_auc_4v5": 0.51,
81	      "pairwise_auc_0v1_std": 0.001,
82	      "pairwise_auc_1v2_std": 0.011,
83	      "pairwise_auc_2v3_std": 0.014,
84	      "pairwise_auc_3v4_std": 0.009,
85	      "pairwise_auc_4v5_std": 0.012,
86	      "pairwise_jsd_0v1": 0.218,
87	      "pairwise_jsd_1v2": 0.01,
88	      "pairwise_jsd_2v3": 0.004,
89	      "pairwise_jsd_3v4": 0.002,
90	      "pairwise_jsd_4v5": 0.001,
91	      "ordinal_accuracy": 0.33,
92	      "ordinal_mae": 1.22
93	    },
94	    "tables": [
95	      {
96	        "name": "Table: OLMo-1B pairwise discrimination",
97	        "columns": [
98	          "depth_pair",
99	          "AUC_mean",
100	          "AUC_std",
101	          "JSD"
102	        ],
103	        "rows": [
104	          [
105	            "0 vs 1",
106	            0.988,
107	            0.001,
108	            0.218
109	          ],
110	          [
111	            "1 vs 2",
112	            0.61,
113	            0.011,
114	            0.01
115	          ],
116	          [
117	            "2 vs 3",
118	            0.54,
119	            0.014,
120	            0.004
121	          ],
122	          [
123	            "3 vs 4",
124	            0.52,
125	            0.009,
126	            0.002
127	          ],
128	          [
129	            "4 vs 5",
130	            0.51,
131	            0.012,
132	            0.001
133	          ]
134	        ]
135	      }
136	    ],
137	    "figures": [],
138	    "analysis": "OLMo-1B 进一步确认 K*=2 的 universality。三个模型的 K* 完全一致， 差异仅在 0v1 和 1v2 的绝对值上——这些差异反映了模型 generation quality 的差异， 但不影响 saturation boundary 的位置。这是 worst 档最有力的论据： K* 是 architecture-invariant 的 hard ceiling。\n\n\nOLMo-1B 参数量最小（1B vs Pythia 1.4B vs Qwen 1.5B），且训练数据虽然开源透明但 总 token 量较少。在 worst 档下，OLMo 的信号衰减最快：1v2 AUC 仅 0.61，是三个模型中 最低的。这与 DPI 一致——更小/更弱的模型作为 lossy channel，每次 pass 丢失更多互信息， 使得代际差异更快趋同。0v1 仍然高（0.988），因为 human vs machine 的 distributional gap 足够大，即使弱模型也能被检测。但 gen-1 vs gen-2 的 gap 已经极小（JSD 0.010）， gen-2+ 完全不可区分。ordinal_accuracy 0.33 接近 6-class random baseline（0.167）， 说明 classifier 只在 depth 0 和 depth 1 上有意义区分能力。\n"
139	  },
140	  {
141	    "name": "Qwen2.5-1.5B decoding strategy ablation",
142	    "description": "Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。\n",
143	    "results": {
144	      "greedy": {
145	        "k_star": 2,
146	        "pairwise_auc_0v1": 0.997,
147	        "pairwise_auc_1v2": 0.62,
148	        "pairwise_auc_2v3": 0.55,
149	        "pairwise_auc_3v4": 0.53,
150	        "pairwise_auc_4v5": 0.52,
151	        "pairwise_jsd_0v1": 0.305,
152	        "pairwise_jsd_1v2": 0.014,
153	        "pairwise_jsd_2v3": 0.005,
154	        "pairwise_jsd_3v4": 0.003,
155	        "pairwise_jsd_4v5": 0.002
156	      },
157	      "nucleus_p09": {
158	        "k_star": 2,
159	        "pairwise_auc_0v1": 0.996,
160	        "pairwise_auc_1v2": 0.68,
161	        "pairwise_auc_2v3": 0.57,
162	        "pairwise_auc_3v4": 0.54,
163	        "pairwise_auc_4v5": 0.53,
164	        "pairwise_jsd_0v1": 0.28,
165	        "pairwise_jsd_1v2": 0.015,
166	        "pairwise_jsd_2v3": 0.006,
167	        "pairwise_jsd_3v4": 0.004,
168	        "pairwise_jsd_4v5": 0.003
169	      },
170	      "temp_07": {
171	        "k_star": 2,
172	        "pairwise_auc_0v1": 0.997,
173	        "pairwise_auc_1v2": 0.65,
174	        "pairwise_auc_2v3": 0.56,
175	        "pairwise_auc_3v4": 0.53,
176	        "pairwise_auc_4v5": 0.52,
177	        "pairwise_jsd_0v1": 0.295,
178	        "pairwise_jsd_1v2": 0.014,
179	        "pairwise_jsd_2v3": 0.005,
180	        "pairwise_jsd_3v4": 0.003,
181	        "pairwise_jsd_4v5": 0.002
182	      },
183	      "temp_12": {
184	        "k_star": 2,
185	        "pairwise_auc_0v1": 0.993,
186	        "pairwise_auc_1v2": 0.64,
187	        "pairwise_auc_2v3": 0.54,
188	        "pairwise_auc_3v4": 0.52,
189	        "pairwise_auc_4v5": 0.51,
190	        "pairwise_jsd_0v1": 0.24,
191	        "pairwise_jsd_1v2": 0.011,
192	        "pairwise_jsd_2v3": 0.004,
193	        "pairwise_jsd_3v4": 0.002,
194	        "pairwise_jsd_4v5": 0.001
195	      }
196	    },
197	    "tables": [
198	      {
199	        "name": "Table: Decoding strategy ablation — K* and pairwise AUC",
200	        "columns": [
201	          "strategy",
202	          "K*",
203	          "AUC_0v1",
204	          "AUC_1v2",
205	          "AUC_2v3",
206	          "JSD_0v1",
207	          "JSD_1v2"
208	        ],
209	        "rows": [
210	          [
211	            "greedy",
212	            2,
213	            0.997,
214	            0.62,
215	            0.55,
216	            0.305,
217	            0.014
218	          ],
219	          [
220	            "nucleus p=0.9",
221	            2,
222	            0.996,
223	            0.68,
224	            0.57,
225	            0.28,
226	            0.015
227	          ],
228	          [
229	            "T=0.7",
230	            2,
231	            0.997,
232	            0.65,
233	            0.56,
234	            0.295,
235	            0.014
236	          ],
237	          [
238	            "T=1.2",
239	            2,
240	            0.993,
241	            0.64,
242	            0.54,
243	            0.24,
244	            0.011
245	          ],
246	          [
247	            "nucleus p=0.95 (MVP)",
248	            2,
249	            0.996,
250	            0.7,
251	            0.59,
252	            0.267,
253	            0.016
254	          ]
255	        ]
256	      }
257	    ],
258	    "figures": [],
259	    "analysis": "解码策略消融是 worst 档的决定性实验。四种策略覆盖了从 deterministic（greedy）到 high-entropy（T=1.2）的全谱系，但 K* 完全不变。 策略之间的 1v2 AUC 差异（0.62-0.68）虽存在但幅度小且不改变 K*。 这使 C1 claim 从 \"K* is measurable\" 退化为 \"K*=2 is a hard, unmodulable constant\"—— 实用价值有限，因为无法通过工程手段扩展 depth-aware curation 的窗口。 对论文而言，这是核心 negative result：current-scale 模型的 recursive generation inherently collapses to binary regime。\n\n\n在 worst 档下，解码策略对 K* 没有任何调控效应——所有四种策略均产生 K*=2。 这是因为 DPI bound 取决于 channel 的信息损失率，而不同解码策略改变的是 generation 的 方差/多样性，但不改变 iterated lossy channel 的 fundamental bottleneck。\nGreedy decoding 产生最高的 0v1 JSD（0.305），因为确定性输出与 human text 的 distributional gap 最大——greedy 输出高度 peaked、缺少 human text 的 variability。 但这并不帮助 depth 2+ 的区分：greedy 的 gen-1 输出已经是 degenerate distribution， 再次 greedy decode 只是在 narrow mode 上迭代，信号迅速坍缩。\nT=1.2（高温度）使 0v1 gap 缩小（JSD 0.240），因为高温度输出更接近 uniform 分布， 与 human text 的差异减小。同时高温度加速后续代际的 entropy 增长和 mode mixing， 使 depth 2+ 的信号衰减更快。\nNucleus p=0.9（较 MVP 的 p=0.95 更 conservative）的 1v2 AUC 略高（0.68）， 因为 truncation 保留了更集中的 probability mass，但仍不足以突破 K*=2 的 ceiling。\n关键：没有任何解码策略能将 K* 推到 3。这直接否定了 Route B framing 中 \"decoding strategy modulates K*\" 的希望，使 K*=2 成为 unmodulable constant。\n"
260	  },
261	  {
262	    "name": "Qwen2.5-7B cross-scale probe",
263	    "description": "Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3. 测试 K* 是否随模型规模变化。\n",
264	    "results": {
265	      "k_star": 2,
266	      "pairwise_auc_0v1": 0.994,
267	      "pairwise_auc_1v2": 0.65,
268	      "pairwise_auc_2v3": 0.56,
269	      "pairwise_auc_0v1_std": 0.002,
270	      "pairwise_auc_1v2_std": 0.012,
271	      "pairwise_auc_2v3_std": 0.018,
272	      "pairwise_jsd_0v1": 0.258,
273	      "pairwise_jsd_1v2": 0.014,
274	      "pairwise_jsd_2v3": 0.005
275	    },
276	    "tables": [
277	      {
278	        "name": "Table: Cross-scale comparison (1.5B vs 7B)",
279	        "columns": [
280	          "model",
281	          "params",
282	          "K*",
283	          "AUC_0v1",
284	          "AUC_1v2",
285	          "AUC_2v3",
286	          "JSD_0v1"
287	        ],
288	        "rows": [
289	          [
290	            "Qwen2.5-1.5B (MVP)",
291	            "1.5B",
292	            2,
293	            0.996,
294	            0.7,
295	            0.59,
296	            0.267
297	          ],
298	          [
299	            "Qwen2.5-7B",
300	            "7B",
301	            2,
302	            0.994,
303	            0.65,
304	            0.56,
305	            0.258
306	          ]
307	        ]
308	      }
309	    ],
310	    "figures": [],
311	    "analysis": "7B 结果是对 \"bigger models solve the problem\" narrative 的直接否定。 在 DPI 框架下可以理解：更好的 channel（7B）确实每步丢失更少信息， 但 detection threshold 也随之提高（因为连续代际更相似），两个效应相互抵消。 样本量（1K）是局限，但 std 可控（<0.02），结论稳健。 对论文 narrative：K*=2 是 1-7B scale 下的 hard ceiling， 突破可能需要 order-of-magnitude 的 scale jump（如 70B+），超出本文 scope。\n\n\n在 worst 档下，7B 模型也产生 K*=2，这是最令人沮丧的发现。 直觉上，更大模型作为更\"高保真\"的 channel 应该保留更多 inter-generational 信息， 从而可能推高 K*。但在 worst scenario 下，7B 的 1v2 AUC（0.65）仅比 1.5B MVP（0.70） 略低——这看似反直觉，但可以解释：\n7B 模型的 generation quality 更高，意味着 gen-1 输出更接近 human distribution， 因此 1v2 boundary 反而更难区分（higher-fidelity channel 使连续代际更相似）。 0v1 AUC 略低于 1.5B（0.994 vs 0.996）也符合这一逻辑——更好的模型产生更 human-like 的输出，使 binary detection 本身就更困难。\ndepth 0-3 的 truncated range（因 GPU 预算限制只到 depth 3）已经足以确认 K*=2， 因为 2v3 AUC 已经接近 chance。1K docs 的较小样本量导致 std 略大， 但中位数点估计仍清晰地在 [0.55, 0.65] 的 worst 范围内。\n这一结果否定了 \"scaling to larger models might yield higher K*\" 的希望， 使 K*=2 not only architecture-invariant but also scale-invariant（至少在 1-7B 范围内）。\n"
312	  },
313	  {
314	    "name": "Feature group ablation and degradation ordering",
315	    "description": "对每个模型的 depth chain，按 feature group（surprisal/diversity/tail-thinning） 分别计算 pairwise AUC 和饱和深度，绘制 degradation ordering heatmap。\n",
316	    "results": {
317	      "qwen_1p5b_degradation_order": [
318	        "diversity",
319	        "tail-thinning",
320	        "surprisal"
321	      ],
322	      "qwen_1p5b_diversity_saturation_depth": 2,
323	      "qwen_1p5b_surprisal_saturation_depth": 2,
324	      "qwen_1p5b_tail_saturation_depth": 2,
325	      "pythia_degradation_order": [
326	        "surprisal",
327	        "diversity",
328	        "tail-thinning"
329	      ],
330	      "pythia_diversity_saturation_depth": 2,
331	      "pythia_surprisal_saturation_depth": 2,
332	      "pythia_tail_saturation_depth": 2,
333	      "olmo_degradation_order": [
334	        "tail-thinning",
335	        "surprisal",
336	        "diversity"
337	      ],
338	      "olmo_diversity_saturation_depth": 2,
339	      "olmo_surprisal_saturation_depth": 2,
340	      "olmo_tail_saturation_depth": 2,
341	      "cross_model_kendall_tau_ordering": 0.33,
342	      "per_group_1v2_auc_range": [
343	        0.55,
344	        0.68
345	      ]
346	    },
347	    "tables": [
348	      {
349	        "name": "Table: Feature group pairwise AUC (1v2) by model",
350	        "columns": [
351	          "model",
352	          "surprisal_AUC_1v2",
353	          "diversity_AUC_1v2",
354	          "tail_AUC_1v2",
355	          "ordering_rank"
356	        ],
357	        "rows": [
358	          [
359	            "Qwen2.5-1.5B",
360	            0.63,
361	            0.58,
362	            0.61,
363	            "div → tail → surp"
364	          ],
365	          [
366	            "Pythia-1.4B",
367	            0.56,
368	            0.6,
369	            0.59,
370	            "surp → tail → div"
371	          ],
372	          [
373	            "OLMo-1B",
374	            0.58,
375	            0.59,
376	            0.55,
377	            "tail → surp → div"
378	          ]
379	        ]
380	      },
381	      {
382	        "name": "Table: Feature group saturation depth by model",
383	        "columns": [
384	          "model",
385	          "surprisal_sat",
386	          "diversity_sat",
387	          "tail_sat"
388	        ],
389	        "rows": [
390	          [
391	            "Qwen2.5-1.5B",
392	            2,
393	            2,
394	            2
395	          ],
396	          [
397	            "Pythia-1.4B",
398	            2,
399	            2,
400	            2
401	          ],
402	          [
403	            "OLMo-1B",
404	            2,
405	            2,
406	            2
407	          ]
408	        ]
409	      }
410	    ],
411	    "figures": [],
412	    "analysis": "C2（Linguistic Degradation Ordering）在 worst 档下基本失败。 Kendall tau 0.33 远低于 0.5 的 meaningful agreement 阈值。 虽然每个模型内部可以描述一个 ordering，但缺乏跨模型泛化性， 使得 C2 不构成独立 contribution——它退化为模型特定的描述性观察。 建议：C2 整体降级到 appendix，仅作为 supplementary characterization， 不作为论文 main claim。framing 变为 \"degradation ordering is model-specific, further underscoring the difficulty of generalizable depth estimation\"。\n\n\n在 worst 档下，degradation ordering 在不同模型间不一致（Kendall tau 0.33）。\nQwen 上 vocabulary diversity 先饱和（符合 MVP 初步观察），因为 nucleus sampling 本身就限制了 token diversity 的变化空间，diversity metrics 在 gen-1 就被压到低值。 但 Pythia 上 surprisal 先饱和——因为 Pythia 的 next-token 分布本身更 peaked， 递归生成迅速固化 surprisal 模式。OLMo 上 tail-thinning 先饱和，可能因为其 训练数据分布使得 rare token usage 在第一代就显著下降。\n关键问题：所有三个 feature group 在所有模型上都在 depth 2 饱和—— 即使 ordering 不同，saturation depth 完全相同。这意味着虽然不同 features 的 degradation speed 有微妙差异（体现在 1v2 AUC 的 feature-specific 值）， 但这些差异在 depth 2 的 floor 上完全消失。degradation ordering 因此不具备 跨模型的 prescriptive value——你无法基于某个 feature group 预测它在另一个模型上的 discriminative utility。\ntau=0.33 表明三个模型的 ordering 几乎是 random permutation （3 个 items 的 random tau 期望值约 0，范围 [-1, 1]，0.33 表示 weak agreement）。\n"
413	  },
414	  {
415	    "name": "Downstream filtering evaluation",
416	    "description": "Qwen2.5-1.5B depth chain 上比较 no-filter / binary / graduated / surprisal-based 四种策略，continued pretraining + lm-eval-harness (MMLU, HellaSwag)。3 seeds。\n",
417	    "results": {
418	      "no_filter_mmlu": 25.1,
419	      "no_filter_hellaswag": 42.3,
420	      "binary_mmlu": 25.8,
421	      "binary_hellaswag": 43.2,
422	      "graduated_mmlu": 25.9,
423	      "graduated_hellaswag": 43.4,
424	      "surprisal_mmlu": 25.7,
425	      "surprisal_hellaswag": 43.1,
426	      "delta_graduated_vs_binary_mmlu_pp": 0.1,
427	      "delta_graduated_vs_binary_hellaswag_pp": 0.2,
428	      "delta_graduated_vs_binary_mmlu_std": 0.3,
429	      "delta_graduated_vs_binary_hellaswag_std": 0.4,
430	      "binary_vs_nofilter_mmlu_pp": 0.7,
431	      "binary_vs_nofilter_hellaswag_pp": 0.9,
432	      "graduated_vs_nofilter_mmlu_pp": 0.8,
433	      "graduated_vs_nofilter_hellaswag_pp": 1.1,
434	      "p_value_graduated_vs_binary_mmlu": 0.62,
435	      "p_value_graduated_vs_binary_hellaswag": 0.48
436	    },
437	    "tables": [
438	      {
439	        "name": "Table: Downstream filtering comparison",
440	        "columns": [
441	          "strategy",
442	          "MMLU_mean",
443	          "MMLU_std",
444	          "HellaSwag_mean",
445	          "HellaSwag_std"
446	        ],
447	        "rows": [
448	          [
449	            "No filter",
450	            25.1,
451	            0.2,
452	            42.3,
453	            0.3
454	          ],
455	          [
456	            "Binary",
457	            25.8,
458	            0.3,
459	            43.2,
460	            0.4
461	          ],
462	          [
463	            "Graduated",
464	            25.9,
465	            0.3,
466	            43.4,
467	            0.3
468	          ],
469	          [
470	            "Surprisal-based",
471	            25.7,
472	            0.2,
473	            43.1,
474	            0.4
475	          ]
476	        ]
477	      },
478	      {
479	        "name": "Table: Pairwise significance tests (graduated vs binary)",
480	        "columns": [
481	          "benchmark",
482	          "delta_pp",
483	          "p_value",
484	          "significant_at_005"
485	        ],
486	        "rows": [
487	          [
488	            "MMLU",
489	            "+0.1",
490	            0.62,
491	            "No"
492	          ],
493	          [
494	            "HellaSwag",
495	            "+0.2",
496	            0.48,
497	            "No"
498	          ]
499	        ]
500	      }
501	    ],
502	    "figures": [],
503	    "analysis": "C3 在 worst 档下被否定为独立 positive claim。graduated filtering 的理论优势 （更 calibrated 的 quality 估计）在实践中被两个因素消解： (1) K*=2 限制了 ordinal signal 只有 3 个有效 class； (2) ordinal classifier 的不可靠性使得即使这 3 个 class 的 assignment 也 noisy。 论文 narrative 转变：C3 变为 \"graduated filtering has fundamental limits explained by rapid signal collapse\"，并从 positive claim 变为 characterization of why the approach fails。实践建议简化为：use binary detection + discard， 不需要 depth estimation。\n\n\n在 worst 档下，graduated filtering 相对 binary 的增益微乎其微（MMLU +0.1pp, HellaSwag +0.2pp）， 且在 3 seeds 上不显著（p > 0.4）。\n根本原因：graduated filtering 的优势来自对 depth 1 vs depth 2+ 的更精细处理—— 例如对 gen-1 赋予中等权重而非完全删除。但在 worst 档下： (1) K*=2 意味着 graduated signal 只有三个有效等级（human/gen-1/gen-2+），\n    与 binary 相比仅多一个 bucket；\n(2) gen-1 的 ordinal prediction 不够 reliable（accuracy ~0.35），\n    所以 graduated filter 经常错误地 upweight 或 downweight gen-1 文本；\n(3) continued pretraining 本身对训练数据质量的敏感度在 1.5B scale 下有限——\n    模型的 learning capacity 不足以从 marginal quality differences 中获益。\n\nBinary filtering 本身有意义（vs no-filter: +0.7 MMLU, +0.9 HellaSwag）， 因为移除明显的 synthetic text 确实有用。但 graduated 在 binary 之上的 marginal gain 消失在 noise 中。surprisal-based filtering 与 binary 接近， 说明 surprisal features 的连续值在这个 scale 下不提供额外的 quality signal。\n这使 C3 从 \"graduated filtering outperforms binary\" 变为 \"graduated filtering offers no statistically significant advantage over binary when K*=2 limits the ordinal signal to three coarse classes\"。\n"
504	  },
505	  {
506	    "name": "K* sensitivity to AUC threshold",
507	    "description": "在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。\n",
508	    "results": {
509	      "threshold_055": {
510	        "k_star_qwen": 3,
511	        "k_star_pythia": 2,
512	        "k_star_olmo": 2
513	      },
514	      "threshold_060": {
515	        "k_star_qwen": 2,
516	        "k_star_pythia": 2,
517	        "k_star_olmo": 2
518	      },
519	      "threshold_065": {
520	        "k_star_qwen": 2,
521	        "k_star_pythia": 2,
522	        "k_star_olmo": 2
523	      },
524	      "threshold_070": {
525	        "k_star_qwen": 2,
526	        "k_star_pythia": 2,
527	        "k_star_olmo": 2
528	      },
529	      "robustness_summary": "K*=2 at thresholds ≥0.60; Qwen bumps to K*=3 only at 0.55 due to its 2v3 AUC=0.59 being marginally above threshold"
530	    },
531	    "tables": [
532	      {
533	        "name": "Table: K* across AUC thresholds",
534	        "columns": [
535	          "threshold",
536	          "Qwen_K*",
537	          "Pythia_K*",
538	          "OLMo_K*"
539	        ],
540	        "rows": [
541	          [
542	            0.55,
543	            3,
544	            2,
545	            2
546	          ],
547	          [
548	            0.6,
549	            2,
550	            2,
551	            2
552	          ],
553	          [
554	            0.65,
555	            2,
556	            2,
557	            2
558	          ],
559	          [
560	            0.7,
561	            2,
562	            2,
563	            2
564	          ]
565	        ]
566	      }
567	    ],
568	    "figures": [],
569	    "analysis": "Sensitivity analysis 确认 K*=2 在 reasonable threshold range 内稳健。 Qwen 在 0.55 处的 K*=3 是唯一例外，但其 2v3 AUC（0.5893）仅比 threshold 高 0.04， 属于统计噪声。在论文中建议选取 0.60 作为默认 threshold（与 binary detection 的 常见 convention 一致），并在 sensitivity analysis section 报告此结果。 核心信息：K*=2 的稳健性不是 precision 的体现，而是 signal collapse 的体现。\n\n\nK* 的定义是 max depth k such that pairwise AUC(k-1, k) > threshold。 在 worst 档下，MVP 的 2v3 AUC 是 0.5893——恰好在 0.55 和 0.60 之间。\n当 threshold=0.55 时，Qwen 的 2v3 AUC（0.5893）> 0.55，所以 K*=3。 但 Pythia（2v3 AUC=0.55）和 OLMo（2v3 AUC=0.54）在 0.55 阈值下仍为 K*=2， 因为它们的 2v3 AUC 刚好在边界上或以下。\n当 threshold≥0.60 时，所有模型统一 K*=2。\n这表面上看是 \"K* is robust\"，但在 worst 的叙事下，robustness 是因为 signal 衰减太快——2v3 AUC 总是在 0.54-0.59 的狭窄区间内， 远低于 practical utility 所需的水平（≥0.70）。K*=2 的 \"稳健性\" 其实是 bad news：它不是因为测量精确，而是因为 cliff 太陡——threshold 选择不影响 K* 恰恰是因为 depth 2+ 的 signal 已经完全坍缩。\n唯一的 exception（Qwen at 0.55）恰好暴露了 K* 定义的 brittleness： 0.5893 vs 0.55 threshold 是统计噪声量级的差异，但 K* 从 2 跳到 3。 这可以在论文中讨论为 \"threshold sensitivity at the margin\"， 但不改变核心结论。\n"
570	  },
571	  {
572	    "name": "Retrain-chain ecological validity",
573	    "description": "Pythia-1.4B LoRA (rank=16, alpha=32), C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。\n",
574	    "results": {
575	      "retrain_k_star": 2,
576	      "retrain_pairwise_auc_0v1": 0.972,
577	      "retrain_pairwise_auc_1v2": 0.58,
578	      "retrain_pairwise_auc_2v3": 0.53,
579	      "retrain_pairwise_auc_3v4": 0.51,
580	      "retrain_jsd_0v1": 0.185,
581	      "retrain_jsd_1v2": 0.008,
582	      "retrain_jsd_2v3": 0.003,
583	      "retrain_jsd_3v4": 0.001,
584	      "prompt_vs_retrain_jsd_correlation": 0.82,
585	      "prompt_vs_retrain_feature_distribution_ks_test_p": 0.03,
586	      "feature_dynamics_qualitative_match": false
587	    },
588	    "tables": [
589	      {
590	        "name": "Table: Prompt-chain vs retrain-chain comparison (Pythia-1.4B)",
591	        "columns": [
592	          "metric",
593	          "prompt-chain",
594	          "retrain-chain"
595	        ],
596	        "rows": [
597	          [
598	            "K*",
599	            2,
600	            2
601	          ],
602	          [
603	            "AUC 0v1",
604	            0.991,
605	            0.972
606	          ],
607	          [
608	            "AUC 1v2",
609	            0.63,
610	            0.58
611	          ],
612	          [
613	            "AUC 2v3",
614	            0.55,
615	            0.53
616	          ],
617	          [
618	            "JSD 0v1",
619	            0.231,
620	            0.185
621	          ],
622	          [
623	            "JSD 1v2",
624	            0.012,
625	            0.008
626	          ],
627	          [
628	            "Feature KS-test p-value",
629	            "—",
630	            0.03
631	          ]
632	        ]
633	      }
634	    ],
635	    "figures": [],
636	    "analysis": "Retrain-chain 结果在 worst 档下对论文有双重影响： (1) Positive: K*=2 在 retrain-chain 下仍然成立，支持 universality； (2) Negative: feature dynamics 不同（KS p=0.03），意味着 prompt-chain 实验的\n    features 和 classifier 不能直接 generalize to real-world retrain scenarios。\n这是 reviewers 会攻击的弱点。论文需要 explicitly acknowledge 这一 limitation， 将 prompt-chain 定位为 \"controlled upper bound\"（因 retrain 加速衰减）， 而非 faithful simulation。建议将此实验降级为 appendix 的 validity check， 避免在 main paper 中给出过强的 ecological validity claim。\n\n\n在 worst 档下，retrain-chain 产生 K*=2（与 prompt-chain 一致），但特征动态不同。\nRetrain-chain 通过 LoRA fine-tuning 模拟真实世界的\"模型在自身输出上训练\"场景。 LoRA rank=16 提供足够的 adaptation capacity，使模型逐代\"记住\"自己的 generation 模式， 导致 model collapse 效应更快显现。\nK* 仍为 2，因为即使 retrain 加速了 signal collapse，saturation boundary 不变——retrain-chain 下 gen-1 与 gen-2 的差异同样在 noise floor。 但绝对值更低：0v1 AUC 从 prompt-chain 的 0.991 降到 0.972， 因为 retrained model 的 gen-1 输出已经部分 \"adapted to\" synthetic distribution， 使 human vs gen-1 gap 缩小。\n关键差异：feature distribution KS test 显著（p=0.03），表明 prompt-chain 和 retrain-chain 产生的文本虽然在 depth discrimination 上有相似的 K*， 但在 feature space 中的轨迹不同。Prompt-chain 的代际漂移主要表现为 diversity 下降；retrain-chain 的漂移还包括 surprisal distribution 的 mode sharpening （因为模型被 fine-tuned 到更 confident 地复制自身模式）。\n这在 worst 档下是 problematic：prompt-chain 上训练的 features 和 classifier 不能直接 transfer 到 retrain-chain 场景，削弱了实验的 ecological validity。 prompt-chain 仅是 retrain-chain 的 noisy proxy。\n"
637	  },
638	  {
639	    "name": "Contamination dose-response",
640	    "description": "在 10%/30%/50% synthetic injection 比例下测试 graduated vs binary filtering 的收益差异。\n",
641	    "results": {
642	      "dose_10pct": {
643	        "binary_mmlu": 25.6,
644	        "graduated_mmlu": 25.6,
645	        "binary_hellaswag": 43.0,
646	        "graduated_hellaswag": 43.0,
647	        "delta_graduated_vs_binary_mmlu": 0.0,
648	        "delta_graduated_vs_binary_hellaswag": 0.0
649	      },
650	      "dose_30pct": {
651	        "binary_mmlu": 25.5,
652	        "graduated_mmlu": 25.6,
653	        "binary_hellaswag": 42.8,
654	        "graduated_hellaswag": 42.9,
655	        "delta_graduated_vs_binary_mmlu": 0.1,
656	        "delta_graduated_vs_binary_hellaswag": 0.1
657	      },
658	      "dose_50pct": {
659	        "binary_mmlu": 25.2,
660	        "graduated_mmlu": 25.3,
661	        "binary_hellaswag": 42.3,
662	        "graduated_hellaswag": 42.5,
663	        "delta_graduated_vs_binary_mmlu": 0.1,
664	        "delta_graduated_vs_binary_hellaswag": 0.2
665	      },
666	      "max_delta_across_doses_mmlu": 0.1,
667	      "max_delta_across_doses_hellaswag": 0.2,
668	      "trend_description": "graduated advantage does not scale with contamination dose; remains ≤0.2pp and non-significant at all doses"
669	    },
670	    "tables": [
671	      {
672	        "name": "Table: Dose-response for graduated vs binary filtering",
673	        "columns": [
674	          "dose",
675	          "binary_MMLU",
676	          "graduated_MMLU",
677	          "delta_MMLU",
678	          "binary_HS",
679	          "graduated_HS",
680	          "delta_HS"
681	        ],
682	        "rows": [
683	          [
684	            "10%",
685	            25.6,
686	            25.6,
687	            0.0,
688	            43.0,
689	            43.0,
690	            0.0
691	          ],
692	          [
693	            "30%",
694	            25.5,
695	            25.6,
696	            "+0.1",
697	            42.8,
698	            42.9,
699	            "+0.1"
700	          ],
701	          [
702	            "50%",
703	            25.2,
704	            25.3,
705	            "+0.1",
706	            42.3,
707	            42.5,
708	            "+0.2"
709	          ]
710	        ]
711	      }
712	    ],
713	    "figures": [],
714	    "analysis": "Dose-response 实验彻底关闭了 \"graduated filtering at higher doses\" 的逃生通道。 即使在 50% contamination（已经是极端场景），graduated 的优势仅 0.1-0.2pp。 这强化了 exp-006 的结论，并为论文提供更完整的 negative characterization。 在 worst 叙事中，此实验可以作为 supplementary evidence 支撑 \"graduated filtering is fundamentally limited by K*=2 signal collapse\"。\n\n\n在 worst 档下，graduated filtering 的 marginal advantage 不随 contamination dose 放大。\n直觉上，更高的 synthetic injection 比例应该放大 graduated 的优势—— 如果有更多 depth-1 文本需要被精细处理（保留 vs 删除），graduated 的 nuance 应该更有价值。 但在 K*=2 + noisy ordinal classifier 的条件下：\n10% injection: 太少的 synthetic 文本使 any filtering strategy 的影响可忽略。 Binary 和 graduated 表现完全一致（delta=0.0），因为 impact 被 90% clean data 稀释。\n30% injection: binary filter 已经移除了大部分 harmful synthetic text； graduated 的 marginal refinement（对 gen-1 给予中等权重）只影响 30% 中的 gen-1 subset（约 30%×(1/5)=6% 的总数据），且 refinement 本身因 classifier noise 不可靠。\n50% injection: 这是 graduated 最有机会显示优势的场景——大量 synthetic data 需要精细处理。但即使这里，delta 仅 0.1-0.2pp，完全不显著。 原因：当 50% 数据是 synthetic 时，binary filter 激进地删除一半数据， graduated filter 保留部分 gen-1 但以 noisy weights——保留 noisy gen-1 text 不比完全删除好多少。\n总结：dose-response 曲线是平坦的（graduated advantage 不随 dose 增长）， 直接否定了 \"graduated becomes more useful at higher contamination\" 的假设。\n"
715	  },
716	  {
717	    "name": "Ordinal vs multinomial vs regression baseline comparison",
718	    "description": "CORAL vs standard multiclass vs ordinal regression， 证明 ordinal structure 的必要性。\n",
719	    "results": {
720	      "coral_ordinal": {
721	        "accuracy": 0.37,
722	        "mae": 1.08,
723	        "macro_f1": 0.22
724	      },
725	      "standard_multiclass": {
726	        "accuracy": 0.35,
727	        "mae": 1.22,
728	        "macro_f1": 0.19
729	      },
730	      "ordinal_regression": {
731	        "accuracy": 0.36,
732	        "mae": 1.1,
733	        "macro_f1": 0.21
734	      },
735	      "binary_plus_random_depth": {
736	        "accuracy": 0.32,
737	        "mae": 1.25,
738	        "macro_f1": 0.18
739	      },
740	      "coral_vs_binary_random_accuracy_delta": 0.05,
741	      "coral_vs_binary_random_mae_delta": -0.17
742	    },
743	    "tables": [
744	      {
745	        "name": "Table: Classifier comparison",
746	        "columns": [
747	          "method",
748	          "accuracy",
749	          "MAE",
750	          "macro_F1"
751	        ],
752	        "rows": [
753	          [
754	            "CORAL (ordinal)",
755	            0.37,
756	            1.08,
757	            0.22
758	          ],
759	          [
760	            "Standard multiclass",
761	            0.35,
762	            1.22,
763	            0.19
764	          ],
765	          [
766	            "Ordinal regression",
767	            0.36,
768	            1.1,
769	            0.21
770	          ],
771	          [
772	            "Binary + random depth",
773	            0.32,
774	            1.25,
775	            0.18
776	          ]
777	        ]
778	      }
779	    ],
780	    "figures": [],
781	    "analysis": "Classifier comparison 实验为 worst 叙事提供重要支撑： depth estimation 的瓶颈不在 classifier architecture，而在 feature-level signal。 无论用什么 classifier，depth 2+ 的分类都接近 random。 这意味着 C1 的 framing 是正确的——K*=2 是 information-theoretic ceiling， 不是 classifier capacity 的限制。 对论文：此实验可以简洁地放在 main paper 中，一个 table + 一段分析即可， 用于排除 \"better classifier might help\" 的 reviewer objection。\n\n\n在 worst 档下，ordinal classifier（CORAL）仅 marginally 优于 binary + random depth assignment。\nCORAL accuracy 0.37 vs binary+random 0.32: delta 仅 5pp。这个 delta 主要来自 CORAL 在 depth 0 和 depth 1 上的正确分类——对 depth 2-5 的预测，CORAL 几乎和 random assignment 一样糟糕，因为 features 在 depth 2+ 不可区分。\nStandard multiclass（不利用 ordinal structure）的 accuracy（0.35）和 CORAL（0.37） 接近，说明 ordinal structure 的额外 inductive bias 在 K*=2 条件下几乎无用—— 当只有 2 个 meaningfully distinct levels 时，ordinal vs nominal 的区别消失。\nOrdinal regression（连续 depth 预测 + discretization）的 MAE 1.10 略好于 multiclass 的 1.22， 但差异很小。所有方法的 macro_F1 都很低（0.18-0.22），因为 depth 2-5 的 per-class F1 接近 0。\n这直接验证了 worst 档的核心假设：\"ordinal classifier barely outperforms binary + random depth assignment\"。ordinal 方法的 overhead（更复杂的 loss function， 更多 hyperparameters）不 justify 其 marginal gain。\n"
782	  },
783	  {
784	    "name": "LLM zero-shot depth estimation baseline",
785	    "description": "GPT-4o / Claude 3.5 对 depth 0-4 文本做 zero-shot depth 判断。\n",
786	    "results": {
787	      "gpt4o": {
788	        "accuracy": 0.24,
789	        "mae": 1.65,
790	        "binary_accuracy_human_vs_synthetic": 0.78,
791	        "depth_estimation_kendall_tau": 0.12
792	      },
793	      "claude35": {
794	        "accuracy": 0.22,
795	        "mae": 1.72,
796	        "binary_accuracy_human_vs_synthetic": 0.81,
797	        "depth_estimation_kendall_tau": 0.1
798	      },
799	      "random_baseline_accuracy": 0.2,
800	      "both_models_depth_2plus_accuracy": 0.08
801	    },
802	    "tables": [
803	      {
804	        "name": "Table: LLM zero-shot depth estimation",
805	        "columns": [
806	          "model",
807	          "5-class_acc",
808	          "MAE",
809	          "binary_acc",
810	          "kendall_tau"
811	        ],
812	        "rows": [
813	          [
814	            "GPT-4o",
815	            0.24,
816	            1.65,
817	            0.78,
818	            0.12
819	          ],
820	          [
821	            "Claude 3.5",
822	            0.22,
823	            1.72,
824	            0.81,
825	            0.1
826	          ],
827	          [
828	            "Random baseline",
829	            0.2,
830	            2.0,
831	            0.5,
832	            0.0
833	          ],
834	          [
835	            "Our classifier (CORAL)",
836	            0.37,
837	            1.08,
838	            0.93,
839	            0.35
840	          ]
841	        ]
842	      }
843	    ],
844	    "figures": [],
845	    "analysis": "LLM zero-shot 实验的价值在于建立 lower bound 和验证 problem difficulty。 即使 frontier models 也无法做 depth estimation，说明这不是 trivial task。 但在 worst 档下，我们的 specialized method（CORAL, acc 0.37）也只比 LLMs 高 13-15pp， 且仍远低于实用水平——这更多地证明了 task difficulty 而非 method value。 论文中可以用此实验支撑 \"depth estimation is fundamentally hard\" 的叙事。\n\n\n在 worst 档下，frontier LLMs 的 zero-shot depth estimation 接近 random baseline。\nGPT-4o 和 Claude 3.5 都有一定的 binary detection 能力（human vs synthetic: 78-81%）， 这与它们的 RLHF training 中对 \"machine-generated text\" 的 implicit awareness 一致。 但 depth estimation（0/1/2/3/4 的精确分类）完全失败：accuracy 0.22-0.24 仅比 5-class random（0.20）高 2-4pp。\n原因分析： (1) Zero-shot 没有 calibrated features——LLMs 依赖 surface-level heuristics\n    （如 repetitiveness, formality）而非 information-theoretic statistics；\n(2) 即使 LLMs 有 implicit depth awareness，depth 2-4 的文本在 surface features\n    上几乎不可区分——这与我们 handcrafted features 的发现一致；\n(3) LLMs 倾向于 overestimate depth（把 gen-1 判为 gen-3），因为它们 associate\n    \"synthetic\" with \"low quality\" 但不能 quantify degradation degree。\n\nKendall tau 0.10-0.12 表明 predicted depth 与 true depth 几乎没有 monotonic 关系。 两个模型在 depth 2+ 上的 accuracy 仅 8%（5-class random 在 3 个 class 上的 期望准确率 = 3/5 × 1/5 = 12%，实际低于 random 因为 LLMs 系统性地 misclassify depth 2+ 为 depth 1）。\n这验证了 \"depth estimation needs specialized methods\" 的 premise， 但在 worst 档下也削弱了 positive framing——即使专门方法也只能做到 K*=2。\n"
846	  },
847	  {
848	    "name": "Binary detector confidence as depth proxy",
849	    "description": "用 DivEye/Binoculars score 的 Spearman correlation with true depth， 验证 binary confidence ≠ depth。\n",
850	    "results": {
851	      "diveye_spearman_rho": 0.18,
852	      "diveye_spearman_p": 0.001,
853	      "binoculars_spearman_rho": 0.22,
854	      "binoculars_spearman_p": 0.001,
855	      "diveye_auc_0v1": 0.91,
856	      "diveye_auc_1v2": 0.54,
857	      "binoculars_auc_0v1": 0.94,
858	      "binoculars_auc_1v2": 0.56,
859	      "diveye_depth_2plus_rank_correlation": 0.03,
860	      "binoculars_depth_2plus_rank_correlation": 0.05
861	    },
862	    "tables": [
863	      {
864	        "name": "Table: Binary detector confidence vs true depth",
865	        "columns": [
866	          "detector",
867	          "spearman_rho",
868	          "p_value",
869	          "AUC_0v1",
870	          "AUC_1v2",
871	          "depth_2plus_rho"
872	        ],
873	        "rows": [
874	          [
875	            "DivEye",
876	            0.18,
877	            "<0.001",
878	            0.91,
879	            0.54,
880	            0.03
881	          ],
882	          [
883	            "Binoculars",
884	            0.22,
885	            "<0.001",
886	            0.94,
887	            0.56,
888	            0.05
889	          ]
890	        ]
891	      }
892	    ],
893	    "figures": [],
894	    "analysis": "此实验确认 binary detection 和 depth estimation 是不同的 tasks。 但在 worst 档下，depth estimation 本身因 K*=2 而被限制为近 binary problem， 削弱了 \"we need depth estimation\" 的 motivation。 论文需要 nuanced framing：不是 \"binary is insufficient so we need depth\"， 而是 \"we investigated whether depth estimation is possible beyond binary, and found a hard ceiling at K*=2 — this is itself a useful finding for the community\"。\n\n\n在 worst 档下，binary detector 的 confidence score 与 true depth 的 correlation 很低。\nDivEye 和 Binoculars 的 Spearman rho（0.18, 0.22）虽然统计显著（p < 0.001， 因大样本量），但 effect size 很小。这些 detector 是为 binary detection 设计的， 它们的 score 反映的是 \"how synthetic\" 而非 \"which generation\"。\nBinary detectors 在 0v1 上表现优秀（AUC 0.91-0.94），因为它们正是为此设计的。 但 1v2 AUC 急剧下降到 0.54-0.56——binary confidence 不能区分 gen-1 和 gen-2， 因为两者对 detector 来说都是 \"synthetic\"。\n在 depth 2+ 区域，rank correlation 几乎为 0（0.03-0.05），表明 binary confidence 完全不 encode depth information beyond binary distinction。 这支持了论文的 problem formulation：\"binary detection ≠ depth estimation， 需要专门方法\"。但在 worst 档下，\"专门方法\"的收益也很有限（K*=2）， 使得这个 motivation story 变得尴尬—— \"we need specialized methods, but they also can't do much better\"。\n"
895	  },
896	  {
897	    "name": "Cross-model transfer",
898	    "description": "在 model A 训练的 depth classifier 在 model B 的 depth chain 上的 transfer accuracy。\n",
899	    "results": {
900	      "transfer_matrix_accuracy": {
901	        "qwen_to_pythia": 0.28,
902	        "qwen_to_olmo": 0.26,
903	        "pythia_to_qwen": 0.3,
904	        "pythia_to_olmo": 0.25,
905	        "olmo_to_qwen": 0.29,
906	        "olmo_to_pythia": 0.27
907	      },
908	      "transfer_matrix_binary_accuracy": {
909	        "qwen_to_pythia": 0.82,
910	        "qwen_to_olmo": 0.79,
911	        "pythia_to_qwen": 0.84,
912	        "pythia_to_olmo": 0.77,
913	        "olmo_to_qwen": 0.83,
914	        "olmo_to_pythia": 0.8
915	      },
916	      "in_domain_accuracy_avg": 0.35,
917	      "cross_model_accuracy_avg": 0.28,
918	      "retention_pct": 40,
919	      "cross_model_binary_accuracy_avg": 0.81
920	    },
921	    "tables": [
922	      {
923	        "name": "Table: Cross-model transfer matrix (6-class accuracy)",
924	        "columns": [
925	          "train\\test",
926	          "Qwen",
927	          "Pythia",
928	          "OLMo"
929	        ],
930	        "rows": [
931	          [
932	            "Qwen",
933	            "0.37*",
934	            0.28,
935	            0.26
936	          ],
937	          [
938	            "Pythia",
939	            0.3,
940	            "0.35*",
941	            0.25
942	          ],
943	          [
944	            "OLMo",
945	            0.29,
946	            0.27,
947	            "0.33*"
948	          ]
949	        ]
950	      },
951	      {
952	        "name": "Table: Cross-model transfer matrix (binary accuracy)",
953	        "columns": [
954	          "train\\test",
955	          "Qwen",
956	          "Pythia",
957	          "OLMo"
958	        ],
959	        "rows": [
960	          [
961	            "Qwen",
962	            "0.93*",
963	            0.82,
964	            0.79
965	          ],
966	          [
967	            "Pythia",
968	            0.84,
969	            "0.91*",
970	            0.77
971	          ],
972	          [
973	            "OLMo",
974	            0.83,
975	            0.8,
976	            "0.88*"
977	          ]
978	        ]
979	      }
980	    ],
981	    "figures": [],
982	    "analysis": "Cross-model transfer 实验清楚地分离了 two levels of signal： (1) Binary (human vs synthetic): transfers well (avg 0.81) — this is the robust, universal signal； (2) Depth-specific: transfers poorly (avg 0.28, retention 40%) — this is model-specific。 在 worst 档下，depth estimation 不仅 K*=2，而且 model-specific， 进一步限制了其实用价值——你需要为每个 target model 重新训练 classifier。 论文可以将此 framing 为 additional evidence that depth signal beyond binary is fragile。\n\n\n在 worst 档下，cross-model transfer 的 6-class accuracy 平均 0.28， 是 in-domain accuracy（0.35）的 40%——正好在 worst 范围 [30%, 50%] 内。\nBinary transfer（human vs synthetic）表现尚可（平均 0.81），因为 human vs machine 的 distributional gap 具有跨模型的 generality——不同模型生成的文本与 human text 的 统计差异是 qualitatively similar 的（如更低的 perplexity variance, 更 peaked surprisal）。\n但 depth-specific transfer 几乎完全失败：cross-model depth estimation 的 accuracy 仅 0.25-0.30，接近 6-class random（0.167）。原因：不同模型的 depth-specific feature signatures 是 model-specific 的——Qwen 的 gen-2 和 Pythia 的 gen-2 在 feature space 中的位置不同，因为 degradation 的 trajectory 取决于 model-specific generation dynamics。\nretention_pct = 40% 表明 cross-model transfer 保留了不到一半的 in-domain performance，且 retention 主要来自 binary distinction。 对 depth 2+ 的 transfer 接近 chance。\n这直接支持 worst 档假设：\"cross-model transfer for depth is near chance beyond binary distinction\"。\n"
983	  },
984	  {
985	    "name": "Naturalistic validation on Common Crawl",
986	    "description": "对 Common Crawl 2025/2026 snapshot 样本做 depth 预测， 与 AlignScore 和独立 vocabulary richness 指标做 correlation。\n",
987	    "results": {
988	      "predicted_depth_distribution": {
989	        "depth_0": 0.62,
990	        "depth_1": 0.25,
991	        "depth_2plus": 0.13
992	      },
993	      "correlation_predicted_depth_vs_alignscore": -0.15,
994	      "correlation_predicted_depth_vs_vocab_richness": -0.19,
995	      "correlation_binary_synthetic_vs_alignscore": -0.28,
996	      "fraction_predicted_synthetic": 0.38,
997	      "confidence_calibration_note": "predictions heavily concentrated in depth 0-1; depth 2+ predictions are low-confidence and unreliable"
998	    },
999	    "tables": [
1000	      {
1001	        "name": "Table: Common Crawl naturalistic validation",
1002	        "columns": [
1003	          "metric",
1004	          "value"
1005	        ],
1006	        "rows": [
1007	          [
1008	            "Predicted human fraction",
1009	            0.62
1010	          ],
1011	          [
1012	            "Predicted gen-1 fraction",
1013	            0.25
1014	          ],
1015	          [
1016	            "Predicted depth-2+ fraction",
1017	            0.13
1018	          ],
1019	          [
1020	            "Corr(predicted_depth, AlignScore)",
1021	            -0.15
1022	          ],
1023	          [
1024	            "Corr(predicted_depth, vocab_richness)",
1025	            -0.19
1026	          ],
1027	          [
1028	            "Corr(binary_synthetic, AlignScore)",
1029	            -0.28
1030	          ]
1031	        ]
1032	      }
1033	    ],
1034	    "figures": [],
1035	    "analysis": "Naturalistic validation 在 worst 档下提供 weak signal at best。 这是意料之中的——将 controlled experiment 的 classifier 直接 deploy 到 heterogeneous wild data 是 domain shift 问题。 论文可以将此作为 appendix 的 preliminary exploration，但不应依赖此实验 支撑任何 claim。在 worst narrative 中，此实验实际上 supports 论文的 cautionary message：\"depth estimation 在 controlled 条件下都 limited， 在 wild 条件下更不可靠\"。\n\n\n在 worst 档下，naturalistic validation 结果 weak 且 ambiguous。\nPredicted depth distribution（62% human, 25% gen-1, 13% gen-2+）看似 reasonable， 但缺乏 ground truth 使得无法验证准确性。38% predicted synthetic rate 与近期估计（Common Crawl 2025+ 含 15-40% synthetic text）粗略一致， 但 confidence interval 极宽。\nPredicted depth 与 AlignScore 的 correlation（-0.15）很弱—— higher predicted depth 仅 weakly 关联 lower quality。原因： (1) AlignScore 衡量的 factual consistency 与 generation depth 不直接对应； (2) 我们的 depth predictor 在 depth 2+ 上 unreliable，产生 noisy predictions； (3) Common Crawl 中的 synthetic text 来自 diverse models/prompts/settings，\n    与我们 controlled experiment 的 distribution 不匹配。\n\nVocabulary richness correlation（-0.19）略高但仍弱，反映 generation depth 对 lexical diversity 确有 monotone 影响，但在 wild data 中被其他 confounders 淹没 （topic, domain, author style, length）。\nBinary detection（synthetic vs human）与 quality metrics 的 correlation（-0.28） 高于 depth estimation，再次表明 binary signal 是 robust 且 useful 的， 而 graduated depth 在 wild data 上几乎没有额外信息。\n"
1036	  },
1037	  {
1038	    "name": "Learned representation baseline",
1039	    "description": "Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features。\n",
1040	    "results": {
1041	      "learned_repr_accuracy": 0.39,
1042	      "learned_repr_mae": 1.05,
1043	      "handcrafted_accuracy": 0.37,
1044	      "handcrafted_mae": 1.08,
1045	      "learned_repr_auc_0v1": 0.997,
1046	      "learned_repr_auc_1v2": 0.72,
1047	      "learned_repr_auc_2v3": 0.58,
1048	      "learned_repr_k_star": 2,
1049	      "accuracy_delta": 0.02,
1050	      "mae_delta": -0.03
1051	    },
1052	    "tables": [
1053	      {
1054	        "name": "Table: Handcrafted vs learned representations",
1055	        "columns": [
1056	          "feature_type",
1057	          "accuracy",
1058	          "MAE",
1059	          "AUC_1v2",
1060	          "AUC_2v3",
1061	          "K*"
1062	        ],
1063	        "rows": [
1064	          [
1065	            "Handcrafted (15D)",
1066	            0.37,
1067	            1.08,
1068	            0.7,
1069	            0.59,
1070	            2
1071	          ],
1072	          [
1073	            "Learned (4096D + MLP)",
1074	            0.39,
1075	            1.05,
1076	            0.72,
1077	            0.58,
1078	            2
1079	          ]
1080	        ]
1081	      }
1082	    ],
1083	    "figures": [],
1084	    "analysis": "Learned representation 实验排除了 feature engineering 作为 bottleneck 的可能性。 在论文中，这是 important control：证明 K*=2 是 data-intrinsic 的 ceiling， 与 feature choice 无关。同时 justify 了使用 interpretable handcrafted features 作为 primary analysis tool（loss < 2pp accuracy, gain = full interpretability for C2 analysis）。\n\n\n在 worst 档下，learned representations 略优于 handcrafted features，但不改变 K*。\nFrozen LM embeddings（4096-dim from last layer）+ 2-layer MLP 有更大的 capacity 来 capture subtle distributional differences。1v2 AUC 从 handcrafted 的 0.70 提升到 0.72——这表明 LM embeddings 确实 encode 了一些 handcrafted features 未 capture 的信息。 但 2v3 AUC 仍然只有 0.58，不足以突破 K*=2 的 boundary。\naccuracy 提升 2pp（0.39 vs 0.37），MAE 改善 0.03（1.05 vs 1.08）—— 这些差异在统计上可能 significant（取决于 test set size），但 practically negligible。\n关键洞察：learned representations 的 marginal improvement 确认了 handcrafted features 不是 bottleneck——K*=2 是 information-theoretic ceiling，不是 feature engineering 的限制。 即使用模型自身的 full-dimensional representation，depth 2+ 的信号仍然不足。\n这对 worst narrative 是重要支撑：既排除了 \"better features might help\" 的 objection， 又验证了 handcrafted features 的 interpretability 价值不是以 significant accuracy 为代价的。\n"
1085	  },
1086	  {
1087	    "name": "Base vs Instruct model comparison",
1088	    "description": "Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异。\n",
1089	    "results": {
1090	      "base": {
1091	        "k_star": 2,
1092	        "pairwise_auc_0v1": 0.982,
1093	        "pairwise_auc_1v2": 0.64,
1094	        "pairwise_auc_2v3": 0.55,
1095	        "pairwise_jsd_0v1": 0.21,
1096	        "pairwise_jsd_1v2": 0.012,
1097	        "pairwise_jsd_2v3": 0.004,
1098	        "ordinal_accuracy": 0.34,
1099	        "ordinal_mae": 1.15
1100	      },
1101	      "instruct_mvp_reference": {
1102	        "k_star": 2,
1103	        "pairwise_auc_0v1": 0.996,
1104	        "pairwise_auc_1v2": 0.7,
1105	        "pairwise_auc_2v3": 0.59,
1106	        "pairwise_jsd_0v1": 0.267,
1107	        "pairwise_jsd_1v2": 0.016,
1108	        "pairwise_jsd_2v3": 0.007
1109	      },
1110	      "base_vs_instruct_0v1_jsd_delta": -0.057,
1111	      "base_vs_instruct_1v2_auc_delta": -0.06
1112	    },
1113	    "tables": [
1114	      {
1115	        "name": "Table: Base vs Instruct comparison (Qwen2.5-1.5B)",
1116	        "columns": [
1117	          "variant",
1118	          "K*",
1119	          "AUC_0v1",
1120	          "AUC_1v2",
1121	          "AUC_2v3",
1122	          "JSD_0v1",
1123	          "ordinal_acc"
1124	        ],
1125	        "rows": [
1126	          [
1127	            "Instruct (MVP)",
1128	            2,
1129	            0.996,
1130	            0.7,
1131	            0.59,
1132	            0.267,
1133	            0.42
1134	          ],
1135	          [
1136	            "Base",
1137	            2,
1138	            0.982,
1139	            0.64,
1140	            0.55,
1141	            0.21,
1142	            0.34
1143	          ]
1144	        ]
1145	      }
1146	    ],
1147	    "figures": [],
1148	    "analysis": "Base vs Instruct 对比提供了对 RLHF 效应的洞察：instruction tuning 增强了 human vs machine 的 detectability（因为 RLHF 引入了 specific stylistic patterns）， 但不改变 recursive degradation dynamics。在 worst 档下，两个 variant 的 K*=2 进一步缩小了 \"K* might vary with model variant\" 的可能性空间。 论文可以简短讨论此结果，作为 K* universality 的 additional evidence point。\n\n在 worst 档下，Base model 也产生 K*=2，但信号绝对值更低。\nBase model（未经 instruction tuning）的 generation 更 \"raw\"—— less coherent, higher entropy, less human-like structure。这导致：\n(1) 0v1 gap 更小（JSD 0.210 vs Instruct 0.267）：base model 的输出本身就\n    less structured than human text but also less \"distinctively machine-like\"\n    compared to Instruct models（后者有 RLHF-induced patterns 如 hedging language,\n    structured responses that are clearly non-human）；\n\n(2) 1v2 AUC 更低（0.64 vs 0.70）：base model 的递归 generation 更 chaotic，\n    gen-1 和 gen-2 在 feature space 中更接近——high entropy generation 在\n    first pass 就引入大量噪声，使后续代际差异更小；\n\n(3) K* 不变：尽管绝对信号更弱，depth 2+ 的 collapse 模式相同。\n这表明 RLHF/instruction tuning 使模型输出更 \"detectably machine-like\" （higher 0v1 signal），但不改变 recursive degradation 的 fundamental dynamics。 对 worst narrative：base model 结果是对 K*=2 universality 的又一确认， 且暗示实际世界中 base model 生成的 recursive text 更难检测（更低的 0v1 AUC）。\n"
1149	  }
1150	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb1dd495-7f7a-46f9-ad06-a44b1aa5391f",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "0544a6e3-1a10-432e-95d9-1bedbc2ca2a3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Pythia-1.4B cross-model depth chain\",\n    \"description\": \"Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。\\n\",\n    \"results\": {\n      \"k_star\": 2,\n      \"pairwise_auc_0v1\": 0.991,\n      \"pairwise_auc_1v2\": 0.63,\n      \"pairwise_auc_2v3\": 0.55,\n      \"pairwise_auc_3v4\": 0.52,\n      \"pairwise_auc_4v5\": 0.51,\n      \"pairwise_auc_0v1_std\": 0.001,\n      \"pairwise_auc_1v2_std\": 0.009,\n      \"pairwise_auc_2v3_std\": 0.015,\n      \"pairwise_auc_3v4_std\": 0.008,\n      \"pairwise_auc_4v5_std\": 0.01,\n      \"pairwise_jsd_0v1\": 0.231,\n      \"pairwise_jsd_1v2\": 0.012,\n      \"pairwise_jsd_2v3\": 0.004,\n      \"pairwise_jsd_3v4\": 0.002,\n      \"pairwise_jsd_4v5\": 0.002,\n      \"ordinal_accuracy\": 0.35,\n      \"ordinal_mae\": 1.18\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Pythia-1.4B pairwise discrimination\",\n        \"columns\": [\n          \"depth_pair\",\n          \"AUC_mean\",\n          \"AUC_std\",\n          \"JSD\"\n        ],\n        \"rows\": [\n          [\n            \"0 vs 1\",\n            0.991,\n            0.001,\n            0.231\n          ],\n          [\n            \"1 vs 2\",\n            0.63,\n            0.009,\n            0.012\n          ],\n          [\n            \"2 vs 3\",\n            0.55,\n            0.015,\n            0.004\n          ],\n          [\n            \"3 vs 4\",\n            0.52,\n            0.008,\n            0.002\n          ],\n          [\n            \"4 vs 5\",\n            0.51,\n            0.01,\n            0.002\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Pythia-1.4B 复现了 MVP 的核心发现：K*=2，且 depth 2+ 区域信号坍缩。 0v1 JSD 较 Qwen 低约 13%，可能因为 Pythia 的 base generation quality 更低， human-gen1 boundary 本身就不如 Qwen 清晰。但 K* 不变——这对 worst 叙事是关键证据： K*=2 不是 Qwen-specific artifact，而是当前规模模型的 fundamental limitation。 ordinal MAE 1.18 表明平均预测偏差超过 1 个 depth level，graduated estimation 实用性极低。\\n\\n\\nPythia-1.4B 是较早一代架构（GPT-NeoX based），训练数据量和质量低于 Qwen2.5-1.5B。 在 worst 档下，Pythia 的 pairwise AUC 1v2 低于 MVP（0.63 vs 0.70），因为 Pythia 的 generation 质量本身更低——第一代输出已经引入更大噪声，使得后续代际之间的差异更快被噪声淹没。 JSD 从 0v1 的 0.231 迅速衰减到 1v2 的 0.012，与 DPI 预测的指数衰减一致。 depth 2+ 区域 AUC 在 0.51-0.55 之间，接近 chance level。 ordinal_accuracy 仅 0.35，因 depth 2-5 几乎不可区分，classifier 在这些类上接近随机猜测。 这强化了 K*=2 的 universality claim——即使换了不同架构家族，ceiling 不变。\\n\"\n  },\n  {\n    \"name\": \"OLMo-1B cross-model depth chain\",\n    \"description\": \"OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5.\\n\",\n    \"results\": {\n      \"k_star\": 2,\n      \"pairwise_auc_0v1\": 0.988,\n      \"pairwise_auc_1v2\": 0.61,\n      \"pairwise_auc_2v3\": 0.54,\n      \"pairwise_auc_3v4\": 0.52,\n      \"pairwise_auc_4v5\": 0.51,\n      \"pairwise_auc_0v1_std\": 0.001,\n      \"pairwise_auc_1v2_std\": 0.011,\n      \"pairwise_auc_2v3_std\": 0.014,\n      \"pairwise_auc_3v4_std\": 0.009,\n      \"pairwise_auc_4v5_std\": 0.012,\n      \"pairwise_jsd_0v1\": 0.218,\n      \"pairwise_jsd_1v2\": 0.01,\n      \"pairwise_jsd_2v3\": 0.004,\n      \"pairwise_jsd_3v4\": 0.002,\n      \"pairwise_jsd_4v5\": 0.001,\n      \"ordinal_accuracy\": 0.33,\n      \"ordinal_mae\": 1.22\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: OLMo-1B pairwise discrimination\",\n        \"columns\": [\n          \"depth_pair\",\n          \"AUC_mean\",\n          \"AUC_std\",\n          \"JSD\"\n        ],\n        \"rows\": [\n          [\n            \"0 vs 1\",\n            0.988,\n            0.001,\n            0.218\n          ],\n          [\n            \"1 vs 2\",\n            0.61,\n            0.011,\n            0.01\n          ],\n          [\n            \"2 vs 3\",\n            0.54,\n            0.014,\n            0.004\n          ],\n          [\n            \"3 vs 4\",\n            0.52,\n            0.009,\n            0.002\n          ],\n          [\n            \"4 vs 5\",\n            0.51,\n            0.012,\n            0.001\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"OLMo-1B 进一步确认 K*=2 的 universality。三个模型的 K* 完全一致， 差异仅在 0v1 和 1v2 的绝对值上——这些差异反映了模型 generation quality 的差异， 但不影响 saturation boundary 的位置。这是 worst 档最有力的论据： K* 是 architecture-invariant 的 hard ceiling。\\n\\n\\nOLMo-1B 参数量最小（1B vs Pythia 1.4B vs Qwen 1.5B），且训练数据虽然开源透明但 总 token 量较少。在 worst 档下，OLMo 的信号衰减最快：1v2 AUC 仅 0.61，是三个模型中 最低的。这与 DPI 一致——更小/更弱的模型作为 lossy channel，每次 pass 丢失更多互信息， 使得代际差异更快趋同。0v1 仍然高（0.988），因为 human vs machine 的 distributional gap 足够大，即使弱模型也能被检测。但 gen-1 vs gen-2 的 gap 已经极小（JSD 0.010）， gen-2+ 完全不可区分。ordinal_accuracy 0.33 接近 6-class random baseline（0.167）， 说明 classifier 只在 depth 0 和 depth 1 上有意义区分能力。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-1.5B decoding strategy ablation\",\n    \"description\": \"Qwen2.5-1.5B: greedy / nucleus p=0.9 / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。\\n\",\n    \"results\": {\n      \"greedy\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.997,\n        \"pairwise_auc_1v2\": 0.62,\n        \"pairwise_auc_2v3\": 0.55,\n        \"pairwise_auc_3v4\": 0.53,\n        \"pairwise_auc_4v5\": 0.52,\n        \"pairwise_jsd_0v1\": 0.305,\n        \"pairwise_jsd_1v2\": 0.014,\n        \"pairwise_jsd_2v3\": 0.005,\n        \"pairwise_jsd_3v4\": 0.003,\n        \"pairwise_jsd_4v5\": 0.002\n      },\n      \"nucleus_p09\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.996,\n        \"pairwise_auc_1v2\": 0.68,\n        \"pairwise_auc_2v3\": 0.57,\n        \"pairwise_auc_3v4\": 0.54,\n        \"pairwise_auc_4v5\": 0.53,\n        \"pairwise_jsd_0v1\": 0.28,\n        \"pairwise_jsd_1v2\": 0.015,\n        \"pairwise_jsd_2v3\": 0.006,\n        \"pairwise_jsd_3v4\": 0.004,\n        \"pairwise_jsd_4v5\": 0.003\n      },\n      \"temp_07\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.997,\n        \"pairwise_auc_1v2\": 0.65,\n        \"pairwise_auc_2v3\": 0.56,\n        \"pairwise_auc_3v4\": 0.53,\n        \"pairwise_auc_4v5\": 0.52,\n        \"pairwise_jsd_0v1\": 0.295,\n        \"pairwise_jsd_1v2\": 0.014,\n        \"pairwise_jsd_2v3\": 0.005,\n        \"pairwise_jsd_3v4\": 0.003,\n        \"pairwise_jsd_4v5\": 0.002\n      },\n      \"temp_12\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.993,\n        \"pairwise_auc_1v2\": 0.64,\n        \"pairwise_auc_2v3\": 0.54,\n        \"pairwise_auc_3v4\": 0.52,\n        \"pairwise_auc_4v5\": 0.51,\n        \"pairwise_jsd_0v1\": 0.24,\n        \"pairwise_jsd_1v2\": 0.011,\n        \"pairwise_jsd_2v3\": 0.004,\n        \"pairwise_jsd_3v4\": 0.002,\n        \"pairwise_jsd_4v5\": 0.001\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Decoding strategy ablation — K* and pairwise AUC\",\n        \"columns\": [\n          \"strategy\",\n          \"K*\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"JSD_0v1\",\n          \"JSD_1v2\"\n        ],\n        \"rows\": [\n          [\n            \"greedy\",\n            2,\n            0.997,\n            0.62,\n            0.55,\n            0.305,\n            0.014\n          ],\n          [\n            \"nucleus p=0.9\",\n            2,\n            0.996,\n            0.68,\n            0.57,\n            0.28,\n            0.015\n          ],\n          [\n            \"T=0.7\",\n            2,\n            0.997,\n            0.65,\n            0.56,\n            0.295,\n            0.014\n          ],\n          [\n            \"T=1.2\",\n            2,\n            0.993,\n            0.64,\n            0.54,\n            0.24,\n            0.011\n          ],\n          [\n            \"nucleus p=0.95 (MVP)\",\n            2,\n            0.996,\n            0.7,\n            0.59,\n            0.267,\n            0.016\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"解码策略消融是 worst 档的决定性实验。四种策略覆盖了从 deterministic（greedy）到 high-entropy（T=1.2）的全谱系，但 K* 完全不变。 策略之间的 1v2 AUC 差异（0.62-0.68）虽存在但幅度小且不改变 K*。 这使 C1 claim 从 \\\"K* is measurable\\\" 退化为 \\\"K*=2 is a hard, unmodulable constant\\\"—— 实用价值有限，因为无法通过工程手段扩展 depth-aware curation 的窗口。 对论文而言，这是核心 negative result：current-scale 模型的 recursive generation inherently collapses to binary regime。\\n\\n\\n在 worst 档下，解码策略对 K* 没有任何调控效应——所有四种策略均产生 K*=2。 这是因为 DPI bound 取决于 channel 的信息损失率，而不同解码策略改变的是 generation 的 方差/多样性，但不改变 iterated lossy channel 的 fundamental bottleneck。\\nGreedy decoding 产生最高的 0v1 JSD（0.305），因为确定性输出与 human text 的 distributional gap 最大——greedy 输出高度 peaked、缺少 human text 的 variability。 但这并不帮助 depth 2+ 的区分：greedy 的 gen-1 输出已经是 degenerate distribution， 再次 greedy decode 只是在 narrow mode 上迭代，信号迅速坍缩。\\nT=1.2（高温度）使 0v1 gap 缩小（JSD 0.240），因为高温度输出更接近 uniform 分布， 与 human text 的差异减小。同时高温度加速后续代际的 entropy 增长和 mode mixing， 使 depth 2+ 的信号衰减更快。\\nNucleus p=0.9（较 MVP 的 p=0.95 更 conservative）的 1v2 AUC 略高（0.68）， 因为 truncation 保留了更集中的 probability mass，但仍不足以突破 K*=2 的 ceiling。\\n关键：没有任何解码策略能将 K* 推到 3。这直接否定了 Route B framing 中 \\\"decoding strategy modulates K*\\\" 的希望，使 K*=2 成为 unmodulable constant。\\n\"\n  },\n  {\n    \"name\": \"Qwen2.5-7B cross-scale probe\",\n    \"description\": \"Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 1K docs, depth 0-3. 测试 K* 是否随模型规模变化。\\n\",\n    \"results\": {\n      \"k_star\": 2,\n      \"pairwise_auc_0v1\": 0.994,\n      \"pairwise_auc_1v2\": 0.65,\n      \"pairwise_auc_2v3\": 0.56,\n      \"pairwise_auc_0v1_std\": 0.002,\n      \"pairwise_auc_1v2_std\": 0.012,\n      \"pairwise_auc_2v3_std\": 0.018,\n      \"pairwise_jsd_0v1\": 0.258,\n      \"pairwise_jsd_1v2\": 0.014,\n      \"pairwise_jsd_2v3\": 0.005\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-scale comparison (1.5B vs 7B)\",\n        \"columns\": [\n          \"model\",\n          \"params\",\n          \"K*\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"JSD_0v1\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-1.5B (MVP)\",\n            \"1.5B\",\n            2,\n            0.996,\n            0.7,\n            0.59,\n            0.267\n          ],\n          [\n            \"Qwen2.5-7B\",\n            \"7B\",\n            2,\n            0.994,\n            0.65,\n            0.56,\n            0.258\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 结果是对 \\\"bigger models solve the problem\\\" narrative 的直接否定。 在 DPI 框架下可以理解：更好的 channel（7B）确实每步丢失更少信息， 但 detection threshold 也随之提高（因为连续代际更相似），两个效应相互抵消。 样本量（1K）是局限，但 std 可控（<0.02），结论稳健。 对论文 narrative：K*=2 是 1-7B scale 下的 hard ceiling， 突破可能需要 order-of-magnitude 的 scale jump（如 70B+），超出本文 scope。\\n\\n\\n在 worst 档下，7B 模型也产生 K*=2，这是最令人沮丧的发现。 直觉上，更大模型作为更\\\"高保真\\\"的 channel 应该保留更多 inter-generational 信息， 从而可能推高 K*。但在 worst scenario 下，7B 的 1v2 AUC（0.65）仅比 1.5B MVP（0.70） 略低——这看似反直觉，但可以解释：\\n7B 模型的 generation quality 更高，意味着 gen-1 输出更接近 human distribution， 因此 1v2 boundary 反而更难区分（higher-fidelity channel 使连续代际更相似）。 0v1 AUC 略低于 1.5B（0.994 vs 0.996）也符合这一逻辑——更好的模型产生更 human-like 的输出，使 binary detection 本身就更困难。\\ndepth 0-3 的 truncated range（因 GPU 预算限制只到 depth 3）已经足以确认 K*=2， 因为 2v3 AUC 已经接近 chance。1K docs 的较小样本量导致 std 略大， 但中位数点估计仍清晰地在 [0.55, 0.65] 的 worst 范围内。\\n这一结果否定了 \\\"scaling to larger models might yield higher K*\\\" 的希望， 使 K*=2 not only architecture-invariant but also scale-invariant（至少在 1-7B 范围内）。\\n\"\n  },\n  {\n    \"name\": \"Feature group ablation and degradation ordering\",\n    \"description\": \"对每个模型的 depth chain，按 feature group（surprisal/diversity/tail-thinning） 分别计算 pairwise AUC 和饱和深度，绘制 degradation ordering heatmap。\\n\",\n    \"results\": {\n      \"qwen_1p5b_degradation_order\": [\n        \"diversity\",\n        \"tail-thinning\",\n        \"surprisal\"\n      ],\n      \"qwen_1p5b_diversity_saturation_depth\": 2,\n      \"qwen_1p5b_surprisal_saturation_depth\": 2,\n      \"qwen_1p5b_tail_saturation_depth\": 2,\n      \"pythia_degradation_order\": [\n        \"surprisal\",\n        \"diversity\",\n        \"tail-thinning\"\n      ],\n      \"pythia_diversity_saturation_depth\": 2,\n      \"pythia_surprisal_saturation_depth\": 2,\n      \"pythia_tail_saturation_depth\": 2,\n      \"olmo_degradation_order\": [\n        \"tail-thinning\",\n        \"surprisal\",\n        \"diversity\"\n      ],\n      \"olmo_diversity_saturation_depth\": 2,\n      \"olmo_surprisal_saturation_depth\": 2,\n      \"olmo_tail_saturation_depth\": 2,\n      \"cross_model_kendall_tau_ordering\": 0.33,\n      \"per_group_1v2_auc_range\": [\n        0.55,\n        0.68\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Feature group pairwise AUC (1v2) by model\",\n        \"columns\": [\n          \"model\",\n          \"surprisal_AUC_1v2\",\n          \"diversity_AUC_1v2\",\n          \"tail_AUC_1v2\",\n          \"ordering_rank\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-1.5B\",\n            0.63,\n            0.58,\n            0.61,\n            \"div → tail → surp\"\n          ],\n          [\n            \"Pythia-1.4B\",\n            0.56,\n            0.6,\n            0.59,\n            \"surp → tail → div\"\n          ],\n          [\n            \"OLMo-1B\",\n            0.58,\n            0.59,\n            0.55,\n            \"tail → surp → div\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Feature group saturation depth by model\",\n        \"columns\": [\n          \"model\",\n          \"surprisal_sat\",\n          \"diversity_sat\",\n          \"tail_sat\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen2.5-1.5B\",\n            2,\n            2,\n            2\n          ],\n          [\n            \"Pythia-1.4B\",\n            2,\n            2,\n            2\n          ],\n          [\n            \"OLMo-1B\",\n            2,\n            2,\n            2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C2（Linguistic Degradation Ordering）在 worst 档下基本失败。 Kendall tau 0.33 远低于 0.5 的 meaningful agreement 阈值。 虽然每个模型内部可以描述一个 ordering，但缺乏跨模型泛化性， 使得 C2 不构成独立 contribution——它退化为模型特定的描述性观察。 建议：C2 整体降级到 appendix，仅作为 supplementary characterization， 不作为论文 main claim。framing 变为 \\\"degradation ordering is model-specific, further underscoring the difficulty of generalizable depth estimation\\\"。\\n\\n\\n在 worst 档下，degradation ordering 在不同模型间不一致（Kendall tau 0.33）。\\nQwen 上 vocabulary diversity 先饱和（符合 MVP 初步观察），因为 nucleus sampling 本身就限制了 token diversity 的变化空间，diversity metrics 在 gen-1 就被压到低值。 但 Pythia 上 surprisal 先饱和——因为 Pythia 的 next-token 分布本身更 peaked， 递归生成迅速固化 surprisal 模式。OLMo 上 tail-thinning 先饱和，可能因为其 训练数据分布使得 rare token usage 在第一代就显著下降。\\n关键问题：所有三个 feature group 在所有模型上都在 depth 2 饱和—— 即使 ordering 不同，saturation depth 完全相同。这意味着虽然不同 features 的 degradation speed 有微妙差异（体现在 1v2 AUC 的 feature-specific 值）， 但这些差异在 depth 2 的 floor 上完全消失。degradation ordering 因此不具备 跨模型的 prescriptive value——你无法基于某个 feature group 预测它在另一个模型上的 discriminative utility。\\ntau=0.33 表明三个模型的 ordering 几乎是 random permutation （3 个 items 的 random tau 期望值约 0，范围 [-1, 1]，0.33 表示 weak agreement）。\\n\"\n  },\n  {\n    \"name\": \"Downstream filtering evaluation\",\n    \"description\": \"Qwen2.5-1.5B depth chain 上比较 no-filter / binary / graduated / surprisal-based 四种策略，continued pretraining + lm-eval-harness (MMLU, HellaSwag)。3 seeds。\\n\",\n    \"results\": {\n      \"no_filter_mmlu\": 25.1,\n      \"no_filter_hellaswag\": 42.3,\n      \"binary_mmlu\": 25.8,\n      \"binary_hellaswag\": 43.2,\n      \"graduated_mmlu\": 25.9,\n      \"graduated_hellaswag\": 43.4,\n      \"surprisal_mmlu\": 25.7,\n      \"surprisal_hellaswag\": 43.1,\n      \"delta_graduated_vs_binary_mmlu_pp\": 0.1,\n      \"delta_graduated_vs_binary_hellaswag_pp\": 0.2,\n      \"delta_graduated_vs_binary_mmlu_std\": 0.3,\n      \"delta_graduated_vs_binary_hellaswag_std\": 0.4,\n      \"binary_vs_nofilter_mmlu_pp\": 0.7,\n      \"binary_vs_nofilter_hellaswag_pp\": 0.9,\n      \"graduated_vs_nofilter_mmlu_pp\": 0.8,\n      \"graduated_vs_nofilter_hellaswag_pp\": 1.1,\n      \"p_value_graduated_vs_binary_mmlu\": 0.62,\n      \"p_value_graduated_vs_binary_hellaswag\": 0.48\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Downstream filtering comparison\",\n        \"columns\": [\n          \"strategy\",\n          \"MMLU_mean\",\n          \"MMLU_std\",\n          \"HellaSwag_mean\",\n          \"HellaSwag_std\"\n        ],\n        \"rows\": [\n          [\n            \"No filter\",\n            25.1,\n            0.2,\n            42.3,\n            0.3\n          ],\n          [\n            \"Binary\",\n            25.8,\n            0.3,\n            43.2,\n            0.4\n          ],\n          [\n            \"Graduated\",\n            25.9,\n            0.3,\n            43.4,\n            0.3\n          ],\n          [\n            \"Surprisal-based\",\n            25.7,\n            0.2,\n            43.1,\n            0.4\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Pairwise significance tests (graduated vs binary)\",\n        \"columns\": [\n          \"benchmark\",\n          \"delta_pp\",\n          \"p_value\",\n          \"significant_at_005\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            \"+0.1\",\n            0.62,\n            \"No\"\n          ],\n          [\n            \"HellaSwag\",\n            \"+0.2\",\n            0.48,\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"C3 在 worst 档下被否定为独立 positive claim。graduated filtering 的理论优势 （更 calibrated 的 quality 估计）在实践中被两个因素消解： (1) K*=2 限制了 ordinal signal 只有 3 个有效 class； (2) ordinal classifier 的不可靠性使得即使这 3 个 class 的 assignment 也 noisy。 论文 narrative 转变：C3 变为 \\\"graduated filtering has fundamental limits explained by rapid signal collapse\\\"，并从 positive claim 变为 characterization of why the approach fails。实践建议简化为：use binary detection + discard， 不需要 depth estimation。\\n\\n\\n在 worst 档下，graduated filtering 相对 binary 的增益微乎其微（MMLU +0.1pp, HellaSwag +0.2pp）， 且在 3 seeds 上不显著（p > 0.4）。\\n根本原因：graduated filtering 的优势来自对 depth 1 vs depth 2+ 的更精细处理—— 例如对 gen-1 赋予中等权重而非完全删除。但在 worst 档下： (1) K*=2 意味着 graduated signal 只有三个有效等级（human/gen-1/gen-2+），\\n    与 binary 相比仅多一个 bucket；\\n(2) gen-1 的 ordinal prediction 不够 reliable（accuracy ~0.35），\\n    所以 graduated filter 经常错误地 upweight 或 downweight gen-1 文本；\\n(3) continued pretraining 本身对训练数据质量的敏感度在 1.5B scale 下有限——\\n    模型的 learning capacity 不足以从 marginal quality differences 中获益。\\n\\nBinary filtering 本身有意义（vs no-filter: +0.7 MMLU, +0.9 HellaSwag）， 因为移除明显的 synthetic text 确实有用。但 graduated 在 binary 之上的 marginal gain 消失在 noise 中。surprisal-based filtering 与 binary 接近， 说明 surprisal features 的连续值在这个 scale 下不提供额外的 quality signal。\\n这使 C3 从 \\\"graduated filtering outperforms binary\\\" 变为 \\\"graduated filtering offers no statistically significant advantage over binary when K*=2 limits the ordinal signal to three coarse classes\\\"。\\n\"\n  },\n  {\n    \"name\": \"K* sensitivity to AUC threshold\",\n    \"description\": \"在 0.55/0.60/0.65/0.70 四个阈值下计算 K*，展示 K* 对阈值选择的稳健性。\\n\",\n    \"results\": {\n      \"threshold_055\": {\n        \"k_star_qwen\": 3,\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2\n      },\n      \"threshold_060\": {\n        \"k_star_qwen\": 2,\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2\n      },\n      \"threshold_065\": {\n        \"k_star_qwen\": 2,\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2\n      },\n      \"threshold_070\": {\n        \"k_star_qwen\": 2,\n        \"k_star_pythia\": 2,\n        \"k_star_olmo\": 2\n      },\n      \"robustness_summary\": \"K*=2 at thresholds ≥0.60; Qwen bumps to K*=3 only at 0.55 due to its 2v3 AUC=0.59 being marginally above threshold\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: K* across AUC thresholds\",\n        \"columns\": [\n          \"threshold\",\n          \"Qwen_K*\",\n          \"Pythia_K*\",\n          \"OLMo_K*\"\n        ],\n        \"rows\": [\n          [\n            0.55,\n            3,\n            2,\n            2\n          ],\n          [\n            0.6,\n            2,\n            2,\n            2\n          ],\n          [\n            0.65,\n            2,\n            2,\n            2\n          ],\n          [\n            0.7,\n            2,\n            2,\n            2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Sensitivity analysis 确认 K*=2 在 reasonable threshold range 内稳健。 Qwen 在 0.55 处的 K*=3 是唯一例外，但其 2v3 AUC（0.5893）仅比 threshold 高 0.04， 属于统计噪声。在论文中建议选取 0.60 作为默认 threshold（与 binary detection 的 常见 convention 一致），并在 sensitivity analysis section 报告此结果。 核心信息：K*=2 的稳健性不是 precision 的体现，而是 signal collapse 的体现。\\n\\n\\nK* 的定义是 max depth k such that pairwise AUC(k-1, k) > threshold。 在 worst 档下，MVP 的 2v3 AUC 是 0.5893——恰好在 0.55 和 0.60 之间。\\n当 threshold=0.55 时，Qwen 的 2v3 AUC（0.5893）> 0.55，所以 K*=3。 但 Pythia（2v3 AUC=0.55）和 OLMo（2v3 AUC=0.54）在 0.55 阈值下仍为 K*=2， 因为它们的 2v3 AUC 刚好在边界上或以下。\\n当 threshold≥0.60 时，所有模型统一 K*=2。\\n这表面上看是 \\\"K* is robust\\\"，但在 worst 的叙事下，robustness 是因为 signal 衰减太快——2v3 AUC 总是在 0.54-0.59 的狭窄区间内， 远低于 practical utility 所需的水平（≥0.70）。K*=2 的 \\\"稳健性\\\" 其实是 bad news：它不是因为测量精确，而是因为 cliff 太陡——threshold 选择不影响 K* 恰恰是因为 depth 2+ 的 signal 已经完全坍缩。\\n唯一的 exception（Qwen at 0.55）恰好暴露了 K* 定义的 brittleness： 0.5893 vs 0.55 threshold 是统计噪声量级的差异，但 K* 从 2 跳到 3。 这可以在论文中讨论为 \\\"threshold sensitivity at the margin\\\"， 但不改变核心结论。\\n\"\n  },\n  {\n    \"name\": \"Retrain-chain ecological validity\",\n    \"description\": \"Pythia-1.4B LoRA (rank=16, alpha=32), C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。\\n\",\n    \"results\": {\n      \"retrain_k_star\": 2,\n      \"retrain_pairwise_auc_0v1\": 0.972,\n      \"retrain_pairwise_auc_1v2\": 0.58,\n      \"retrain_pairwise_auc_2v3\": 0.53,\n      \"retrain_pairwise_auc_3v4\": 0.51,\n      \"retrain_jsd_0v1\": 0.185,\n      \"retrain_jsd_1v2\": 0.008,\n      \"retrain_jsd_2v3\": 0.003,\n      \"retrain_jsd_3v4\": 0.001,\n      \"prompt_vs_retrain_jsd_correlation\": 0.82,\n      \"prompt_vs_retrain_feature_distribution_ks_test_p\": 0.03,\n      \"feature_dynamics_qualitative_match\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Prompt-chain vs retrain-chain comparison (Pythia-1.4B)\",\n        \"columns\": [\n          \"metric\",\n          \"prompt-chain\",\n          \"retrain-chain\"\n        ],\n        \"rows\": [\n          [\n            \"K*\",\n            2,\n            2\n          ],\n          [\n            \"AUC 0v1\",\n            0.991,\n            0.972\n          ],\n          [\n            \"AUC 1v2\",\n            0.63,\n            0.58\n          ],\n          [\n            \"AUC 2v3\",\n            0.55,\n            0.53\n          ],\n          [\n            \"JSD 0v1\",\n            0.231,\n            0.185\n          ],\n          [\n            \"JSD 1v2\",\n            0.012,\n            0.008\n          ],\n          [\n            \"Feature KS-test p-value\",\n            \"—\",\n            0.03\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Retrain-chain 结果在 worst 档下对论文有双重影响： (1) Positive: K*=2 在 retrain-chain 下仍然成立，支持 universality； (2) Negative: feature dynamics 不同（KS p=0.03），意味着 prompt-chain 实验的\\n    features 和 classifier 不能直接 generalize to real-world retrain scenarios。\\n这是 reviewers 会攻击的弱点。论文需要 explicitly acknowledge 这一 limitation， 将 prompt-chain 定位为 \\\"controlled upper bound\\\"（因 retrain 加速衰减）， 而非 faithful simulation。建议将此实验降级为 appendix 的 validity check， 避免在 main paper 中给出过强的 ecological validity claim。\\n\\n\\n在 worst 档下，retrain-chain 产生 K*=2（与 prompt-chain 一致），但特征动态不同。\\nRetrain-chain 通过 LoRA fine-tuning 模拟真实世界的\\\"模型在自身输出上训练\\\"场景。 LoRA rank=16 提供足够的 adaptation capacity，使模型逐代\\\"记住\\\"自己的 generation 模式， 导致 model collapse 效应更快显现。\\nK* 仍为 2，因为即使 retrain 加速了 signal collapse，saturation boundary 不变——retrain-chain 下 gen-1 与 gen-2 的差异同样在 noise floor。 但绝对值更低：0v1 AUC 从 prompt-chain 的 0.991 降到 0.972， 因为 retrained model 的 gen-1 输出已经部分 \\\"adapted to\\\" synthetic distribution， 使 human vs gen-1 gap 缩小。\\n关键差异：feature distribution KS test 显著（p=0.03），表明 prompt-chain 和 retrain-chain 产生的文本虽然在 depth discrimination 上有相似的 K*， 但在 feature space 中的轨迹不同。Prompt-chain 的代际漂移主要表现为 diversity 下降；retrain-chain 的漂移还包括 surprisal distribution 的 mode sharpening （因为模型被 fine-tuned 到更 confident 地复制自身模式）。\\n这在 worst 档下是 problematic：prompt-chain 上训练的 features 和 classifier 不能直接 transfer 到 retrain-chain 场景，削弱了实验的 ecological validity。 prompt-chain 仅是 retrain-chain 的 noisy proxy。\\n\"\n  },\n  {\n    \"name\": \"Contamination dose-response\",\n    \"description\": \"在 10%/30%/50% synthetic injection 比例下测试 graduated vs binary filtering 的收益差异。\\n\",\n    \"results\": {\n      \"dose_10pct\": {\n        \"binary_mmlu\": 25.6,\n        \"graduated_mmlu\": 25.6,\n        \"binary_hellaswag\": 43.0,\n        \"graduated_hellaswag\": 43.0,\n        \"delta_graduated_vs_binary_mmlu\": 0.0,\n        \"delta_graduated_vs_binary_hellaswag\": 0.0\n      },\n      \"dose_30pct\": {\n        \"binary_mmlu\": 25.5,\n        \"graduated_mmlu\": 25.6,\n        \"binary_hellaswag\": 42.8,\n        \"graduated_hellaswag\": 42.9,\n        \"delta_graduated_vs_binary_mmlu\": 0.1,\n        \"delta_graduated_vs_binary_hellaswag\": 0.1\n      },\n      \"dose_50pct\": {\n        \"binary_mmlu\": 25.2,\n        \"graduated_mmlu\": 25.3,\n        \"binary_hellaswag\": 42.3,\n        \"graduated_hellaswag\": 42.5,\n        \"delta_graduated_vs_binary_mmlu\": 0.1,\n        \"delta_graduated_vs_binary_hellaswag\": 0.2\n      },\n      \"max_delta_across_doses_mmlu\": 0.1,\n      \"max_delta_across_doses_hellaswag\": 0.2,\n      \"trend_description\": \"graduated advantage does not scale with contamination dose; remains ≤0.2pp and non-significant at all doses\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Dose-response for graduated vs binary filtering\",\n        \"columns\": [\n          \"dose\",\n          \"binary_MMLU\",\n          \"graduated_MMLU\",\n          \"delta_MMLU\",\n          \"binary_HS\",\n          \"graduated_HS\",\n          \"delta_HS\"\n        ],\n        \"rows\": [\n          [\n            \"10%\",\n            25.6,\n            25.6,\n            0.0,\n            43.0,\n            43.0,\n            0.0\n          ],\n          [\n            \"30%\",\n            25.5,\n            25.6,\n            \"+0.1\",\n            42.8,\n            42.9,\n            \"+0.1\"\n          ],\n          [\n            \"50%\",\n            25.2,\n            25.3,\n            \"+0.1\",\n            42.3,\n            42.5,\n            \"+0.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dose-response 实验彻底关闭了 \\\"graduated filtering at higher doses\\\" 的逃生通道。 即使在 50% contamination（已经是极端场景），graduated 的优势仅 0.1-0.2pp。 这强化了 exp-006 的结论，并为论文提供更完整的 negative characterization。 在 worst 叙事中，此实验可以作为 supplementary evidence 支撑 \\\"graduated filtering is fundamentally limited by K*=2 signal collapse\\\"。\\n\\n\\n在 worst 档下，graduated filtering 的 marginal advantage 不随 contamination dose 放大。\\n直觉上，更高的 synthetic injection 比例应该放大 graduated 的优势—— 如果有更多 depth-1 文本需要被精细处理（保留 vs 删除），graduated 的 nuance 应该更有价值。 但在 K*=2 + noisy ordinal classifier 的条件下：\\n10% injection: 太少的 synthetic 文本使 any filtering strategy 的影响可忽略。 Binary 和 graduated 表现完全一致（delta=0.0），因为 impact 被 90% clean data 稀释。\\n30% injection: binary filter 已经移除了大部分 harmful synthetic text； graduated 的 marginal refinement（对 gen-1 给予中等权重）只影响 30% 中的 gen-1 subset（约 30%×(1/5)=6% 的总数据），且 refinement 本身因 classifier noise 不可靠。\\n50% injection: 这是 graduated 最有机会显示优势的场景——大量 synthetic data 需要精细处理。但即使这里，delta 仅 0.1-0.2pp，完全不显著。 原因：当 50% 数据是 synthetic 时，binary filter 激进地删除一半数据， graduated filter 保留部分 gen-1 但以 noisy weights——保留 noisy gen-1 text 不比完全删除好多少。\\n总结：dose-response 曲线是平坦的（graduated advantage 不随 dose 增长）， 直接否定了 \\\"graduated becomes more useful at higher contamination\\\" 的假设。\\n\"\n  },\n  {\n    \"name\": \"Ordinal vs multinomial vs regression baseline comparison\",\n    \"description\": \"CORAL vs standard multiclass vs ordinal regression， 证明 ordinal structure 的必要性。\\n\",\n    \"results\": {\n      \"coral_ordinal\": {\n        \"accuracy\": 0.37,\n        \"mae\": 1.08,\n        \"macro_f1\": 0.22\n      },\n      \"standard_multiclass\": {\n        \"accuracy\": 0.35,\n        \"mae\": 1.22,\n        \"macro_f1\": 0.19\n      },\n      \"ordinal_regression\": {\n        \"accuracy\": 0.36,\n        \"mae\": 1.1,\n        \"macro_f1\": 0.21\n      },\n      \"binary_plus_random_depth\": {\n        \"accuracy\": 0.32,\n        \"mae\": 1.25,\n        \"macro_f1\": 0.18\n      },\n      \"coral_vs_binary_random_accuracy_delta\": 0.05,\n      \"coral_vs_binary_random_mae_delta\": -0.17\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Classifier comparison\",\n        \"columns\": [\n          \"method\",\n          \"accuracy\",\n          \"MAE\",\n          \"macro_F1\"\n        ],\n        \"rows\": [\n          [\n            \"CORAL (ordinal)\",\n            0.37,\n            1.08,\n            0.22\n          ],\n          [\n            \"Standard multiclass\",\n            0.35,\n            1.22,\n            0.19\n          ],\n          [\n            \"Ordinal regression\",\n            0.36,\n            1.1,\n            0.21\n          ],\n          [\n            \"Binary + random depth\",\n            0.32,\n            1.25,\n            0.18\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier comparison 实验为 worst 叙事提供重要支撑： depth estimation 的瓶颈不在 classifier architecture，而在 feature-level signal。 无论用什么 classifier，depth 2+ 的分类都接近 random。 这意味着 C1 的 framing 是正确的——K*=2 是 information-theoretic ceiling， 不是 classifier capacity 的限制。 对论文：此实验可以简洁地放在 main paper 中，一个 table + 一段分析即可， 用于排除 \\\"better classifier might help\\\" 的 reviewer objection。\\n\\n\\n在 worst 档下，ordinal classifier（CORAL）仅 marginally 优于 binary + random depth assignment。\\nCORAL accuracy 0.37 vs binary+random 0.32: delta 仅 5pp。这个 delta 主要来自 CORAL 在 depth 0 和 depth 1 上的正确分类——对 depth 2-5 的预测，CORAL 几乎和 random assignment 一样糟糕，因为 features 在 depth 2+ 不可区分。\\nStandard multiclass（不利用 ordinal structure）的 accuracy（0.35）和 CORAL（0.37） 接近，说明 ordinal structure 的额外 inductive bias 在 K*=2 条件下几乎无用—— 当只有 2 个 meaningfully distinct levels 时，ordinal vs nominal 的区别消失。\\nOrdinal regression（连续 depth 预测 + discretization）的 MAE 1.10 略好于 multiclass 的 1.22， 但差异很小。所有方法的 macro_F1 都很低（0.18-0.22），因为 depth 2-5 的 per-class F1 接近 0。\\n这直接验证了 worst 档的核心假设：\\\"ordinal classifier barely outperforms binary + random depth assignment\\\"。ordinal 方法的 overhead（更复杂的 loss function， 更多 hyperparameters）不 justify 其 marginal gain。\\n\"\n  },\n  {\n    \"name\": \"LLM zero-shot depth estimation baseline\",\n    \"description\": \"GPT-4o / Claude 3.5 对 depth 0-4 文本做 zero-shot depth 判断。\\n\",\n    \"results\": {\n      \"gpt4o\": {\n        \"accuracy\": 0.24,\n        \"mae\": 1.65,\n        \"binary_accuracy_human_vs_synthetic\": 0.78,\n        \"depth_estimation_kendall_tau\": 0.12\n      },\n      \"claude35\": {\n        \"accuracy\": 0.22,\n        \"mae\": 1.72,\n        \"binary_accuracy_human_vs_synthetic\": 0.81,\n        \"depth_estimation_kendall_tau\": 0.1\n      },\n      \"random_baseline_accuracy\": 0.2,\n      \"both_models_depth_2plus_accuracy\": 0.08\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: LLM zero-shot depth estimation\",\n        \"columns\": [\n          \"model\",\n          \"5-class_acc\",\n          \"MAE\",\n          \"binary_acc\",\n          \"kendall_tau\"\n        ],\n        \"rows\": [\n          [\n            \"GPT-4o\",\n            0.24,\n            1.65,\n            0.78,\n            0.12\n          ],\n          [\n            \"Claude 3.5\",\n            0.22,\n            1.72,\n            0.81,\n            0.1\n          ],\n          [\n            \"Random baseline\",\n            0.2,\n            2.0,\n            0.5,\n            0.0\n          ],\n          [\n            \"Our classifier (CORAL)\",\n            0.37,\n            1.08,\n            0.93,\n            0.35\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLM zero-shot 实验的价值在于建立 lower bound 和验证 problem difficulty。 即使 frontier models 也无法做 depth estimation，说明这不是 trivial task。 但在 worst 档下，我们的 specialized method（CORAL, acc 0.37）也只比 LLMs 高 13-15pp， 且仍远低于实用水平——这更多地证明了 task difficulty 而非 method value。 论文中可以用此实验支撑 \\\"depth estimation is fundamentally hard\\\" 的叙事。\\n\\n\\n在 worst 档下，frontier LLMs 的 zero-shot depth estimation 接近 random baseline。\\nGPT-4o 和 Claude 3.5 都有一定的 binary detection 能力（human vs synthetic: 78-81%）， 这与它们的 RLHF training 中对 \\\"machine-generated text\\\" 的 implicit awareness 一致。 但 depth estimation（0/1/2/3/4 的精确分类）完全失败：accuracy 0.22-0.24 仅比 5-class random（0.20）高 2-4pp。\\n原因分析： (1) Zero-shot 没有 calibrated features——LLMs 依赖 surface-level heuristics\\n    （如 repetitiveness, formality）而非 information-theoretic statistics；\\n(2) 即使 LLMs 有 implicit depth awareness，depth 2-4 的文本在 surface features\\n    上几乎不可区分——这与我们 handcrafted features 的发现一致；\\n(3) LLMs 倾向于 overestimate depth（把 gen-1 判为 gen-3），因为它们 associate\\n    \\\"synthetic\\\" with \\\"low quality\\\" 但不能 quantify degradation degree。\\n\\nKendall tau 0.10-0.12 表明 predicted depth 与 true depth 几乎没有 monotonic 关系。 两个模型在 depth 2+ 上的 accuracy 仅 8%（5-class random 在 3 个 class 上的 期望准确率 = 3/5 × 1/5 = 12%，实际低于 random 因为 LLMs 系统性地 misclassify depth 2+ 为 depth 1）。\\n这验证了 \\\"depth estimation needs specialized methods\\\" 的 premise， 但在 worst 档下也削弱了 positive framing——即使专门方法也只能做到 K*=2。\\n\"\n  },\n  {\n    \"name\": \"Binary detector confidence as depth proxy\",\n    \"description\": \"用 DivEye/Binoculars score 的 Spearman correlation with true depth， 验证 binary confidence ≠ depth。\\n\",\n    \"results\": {\n      \"diveye_spearman_rho\": 0.18,\n      \"diveye_spearman_p\": 0.001,\n      \"binoculars_spearman_rho\": 0.22,\n      \"binoculars_spearman_p\": 0.001,\n      \"diveye_auc_0v1\": 0.91,\n      \"diveye_auc_1v2\": 0.54,\n      \"binoculars_auc_0v1\": 0.94,\n      \"binoculars_auc_1v2\": 0.56,\n      \"diveye_depth_2plus_rank_correlation\": 0.03,\n      \"binoculars_depth_2plus_rank_correlation\": 0.05\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Binary detector confidence vs true depth\",\n        \"columns\": [\n          \"detector\",\n          \"spearman_rho\",\n          \"p_value\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"depth_2plus_rho\"\n        ],\n        \"rows\": [\n          [\n            \"DivEye\",\n            0.18,\n            \"<0.001\",\n            0.91,\n            0.54,\n            0.03\n          ],\n          [\n            \"Binoculars\",\n            0.22,\n            \"<0.001\",\n            0.94,\n            0.56,\n            0.05\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"此实验确认 binary detection 和 depth estimation 是不同的 tasks。 但在 worst 档下，depth estimation 本身因 K*=2 而被限制为近 binary problem， 削弱了 \\\"we need depth estimation\\\" 的 motivation。 论文需要 nuanced framing：不是 \\\"binary is insufficient so we need depth\\\"， 而是 \\\"we investigated whether depth estimation is possible beyond binary, and found a hard ceiling at K*=2 — this is itself a useful finding for the community\\\"。\\n\\n\\n在 worst 档下，binary detector 的 confidence score 与 true depth 的 correlation 很低。\\nDivEye 和 Binoculars 的 Spearman rho（0.18, 0.22）虽然统计显著（p < 0.001， 因大样本量），但 effect size 很小。这些 detector 是为 binary detection 设计的， 它们的 score 反映的是 \\\"how synthetic\\\" 而非 \\\"which generation\\\"。\\nBinary detectors 在 0v1 上表现优秀（AUC 0.91-0.94），因为它们正是为此设计的。 但 1v2 AUC 急剧下降到 0.54-0.56——binary confidence 不能区分 gen-1 和 gen-2， 因为两者对 detector 来说都是 \\\"synthetic\\\"。\\n在 depth 2+ 区域，rank correlation 几乎为 0（0.03-0.05），表明 binary confidence 完全不 encode depth information beyond binary distinction。 这支持了论文的 problem formulation：\\\"binary detection ≠ depth estimation， 需要专门方法\\\"。但在 worst 档下，\\\"专门方法\\\"的收益也很有限（K*=2）， 使得这个 motivation story 变得尴尬—— \\\"we need specialized methods, but they also can't do much better\\\"。\\n\"\n  },\n  {\n    \"name\": \"Cross-model transfer\",\n    \"description\": \"在 model A 训练的 depth classifier 在 model B 的 depth chain 上的 transfer accuracy。\\n\",\n    \"results\": {\n      \"transfer_matrix_accuracy\": {\n        \"qwen_to_pythia\": 0.28,\n        \"qwen_to_olmo\": 0.26,\n        \"pythia_to_qwen\": 0.3,\n        \"pythia_to_olmo\": 0.25,\n        \"olmo_to_qwen\": 0.29,\n        \"olmo_to_pythia\": 0.27\n      },\n      \"transfer_matrix_binary_accuracy\": {\n        \"qwen_to_pythia\": 0.82,\n        \"qwen_to_olmo\": 0.79,\n        \"pythia_to_qwen\": 0.84,\n        \"pythia_to_olmo\": 0.77,\n        \"olmo_to_qwen\": 0.83,\n        \"olmo_to_pythia\": 0.8\n      },\n      \"in_domain_accuracy_avg\": 0.35,\n      \"cross_model_accuracy_avg\": 0.28,\n      \"retention_pct\": 40,\n      \"cross_model_binary_accuracy_avg\": 0.81\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Cross-model transfer matrix (6-class accuracy)\",\n        \"columns\": [\n          \"train\\\\test\",\n          \"Qwen\",\n          \"Pythia\",\n          \"OLMo\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"0.37*\",\n            0.28,\n            0.26\n          ],\n          [\n            \"Pythia\",\n            0.3,\n            \"0.35*\",\n            0.25\n          ],\n          [\n            \"OLMo\",\n            0.29,\n            0.27,\n            \"0.33*\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table: Cross-model transfer matrix (binary accuracy)\",\n        \"columns\": [\n          \"train\\\\test\",\n          \"Qwen\",\n          \"Pythia\",\n          \"OLMo\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen\",\n            \"0.93*\",\n            0.82,\n            0.79\n          ],\n          [\n            \"Pythia\",\n            0.84,\n            \"0.91*\",\n            0.77\n          ],\n          [\n            \"OLMo\",\n            0.83,\n            0.8,\n            \"0.88*\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cross-model transfer 实验清楚地分离了 two levels of signal： (1) Binary (human vs synthetic): transfers well (avg 0.81) — this is the robust, universal signal； (2) Depth-specific: transfers poorly (avg 0.28, retention 40%) — this is model-specific。 在 worst 档下，depth estimation 不仅 K*=2，而且 model-specific， 进一步限制了其实用价值——你需要为每个 target model 重新训练 classifier。 论文可以将此 framing 为 additional evidence that depth signal beyond binary is fragile。\\n\\n\\n在 worst 档下，cross-model transfer 的 6-class accuracy 平均 0.28， 是 in-domain accuracy（0.35）的 40%——正好在 worst 范围 [30%, 50%] 内。\\nBinary transfer（human vs synthetic）表现尚可（平均 0.81），因为 human vs machine 的 distributional gap 具有跨模型的 generality——不同模型生成的文本与 human text 的 统计差异是 qualitatively similar 的（如更低的 perplexity variance, 更 peaked surprisal）。\\n但 depth-specific transfer 几乎完全失败：cross-model depth estimation 的 accuracy 仅 0.25-0.30，接近 6-class random（0.167）。原因：不同模型的 depth-specific feature signatures 是 model-specific 的——Qwen 的 gen-2 和 Pythia 的 gen-2 在 feature space 中的位置不同，因为 degradation 的 trajectory 取决于 model-specific generation dynamics。\\nretention_pct = 40% 表明 cross-model transfer 保留了不到一半的 in-domain performance，且 retention 主要来自 binary distinction。 对 depth 2+ 的 transfer 接近 chance。\\n这直接支持 worst 档假设：\\\"cross-model transfer for depth is near chance beyond binary distinction\\\"。\\n\"\n  },\n  {\n    \"name\": \"Naturalistic validation on Common Crawl\",\n    \"description\": \"对 Common Crawl 2025/2026 snapshot 样本做 depth 预测， 与 AlignScore 和独立 vocabulary richness 指标做 correlation。\\n\",\n    \"results\": {\n      \"predicted_depth_distribution\": {\n        \"depth_0\": 0.62,\n        \"depth_1\": 0.25,\n        \"depth_2plus\": 0.13\n      },\n      \"correlation_predicted_depth_vs_alignscore\": -0.15,\n      \"correlation_predicted_depth_vs_vocab_richness\": -0.19,\n      \"correlation_binary_synthetic_vs_alignscore\": -0.28,\n      \"fraction_predicted_synthetic\": 0.38,\n      \"confidence_calibration_note\": \"predictions heavily concentrated in depth 0-1; depth 2+ predictions are low-confidence and unreliable\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Common Crawl naturalistic validation\",\n        \"columns\": [\n          \"metric\",\n          \"value\"\n        ],\n        \"rows\": [\n          [\n            \"Predicted human fraction\",\n            0.62\n          ],\n          [\n            \"Predicted gen-1 fraction\",\n            0.25\n          ],\n          [\n            \"Predicted depth-2+ fraction\",\n            0.13\n          ],\n          [\n            \"Corr(predicted_depth, AlignScore)\",\n            -0.15\n          ],\n          [\n            \"Corr(predicted_depth, vocab_richness)\",\n            -0.19\n          ],\n          [\n            \"Corr(binary_synthetic, AlignScore)\",\n            -0.28\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Naturalistic validation 在 worst 档下提供 weak signal at best。 这是意料之中的——将 controlled experiment 的 classifier 直接 deploy 到 heterogeneous wild data 是 domain shift 问题。 论文可以将此作为 appendix 的 preliminary exploration，但不应依赖此实验 支撑任何 claim。在 worst narrative 中，此实验实际上 supports 论文的 cautionary message：\\\"depth estimation 在 controlled 条件下都 limited， 在 wild 条件下更不可靠\\\"。\\n\\n\\n在 worst 档下，naturalistic validation 结果 weak 且 ambiguous。\\nPredicted depth distribution（62% human, 25% gen-1, 13% gen-2+）看似 reasonable， 但缺乏 ground truth 使得无法验证准确性。38% predicted synthetic rate 与近期估计（Common Crawl 2025+ 含 15-40% synthetic text）粗略一致， 但 confidence interval 极宽。\\nPredicted depth 与 AlignScore 的 correlation（-0.15）很弱—— higher predicted depth 仅 weakly 关联 lower quality。原因： (1) AlignScore 衡量的 factual consistency 与 generation depth 不直接对应； (2) 我们的 depth predictor 在 depth 2+ 上 unreliable，产生 noisy predictions； (3) Common Crawl 中的 synthetic text 来自 diverse models/prompts/settings，\\n    与我们 controlled experiment 的 distribution 不匹配。\\n\\nVocabulary richness correlation（-0.19）略高但仍弱，反映 generation depth 对 lexical diversity 确有 monotone 影响，但在 wild data 中被其他 confounders 淹没 （topic, domain, author style, length）。\\nBinary detection（synthetic vs human）与 quality metrics 的 correlation（-0.28） 高于 depth estimation，再次表明 binary signal 是 robust 且 useful 的， 而 graduated depth 在 wild data 上几乎没有额外信息。\\n\"\n  },\n  {\n    \"name\": \"Learned representation baseline\",\n    \"description\": \"Frozen Qwen2.5-1.5B embeddings + MLP vs hand-crafted 15D features。\\n\",\n    \"results\": {\n      \"learned_repr_accuracy\": 0.39,\n      \"learned_repr_mae\": 1.05,\n      \"handcrafted_accuracy\": 0.37,\n      \"handcrafted_mae\": 1.08,\n      \"learned_repr_auc_0v1\": 0.997,\n      \"learned_repr_auc_1v2\": 0.72,\n      \"learned_repr_auc_2v3\": 0.58,\n      \"learned_repr_k_star\": 2,\n      \"accuracy_delta\": 0.02,\n      \"mae_delta\": -0.03\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Handcrafted vs learned representations\",\n        \"columns\": [\n          \"feature_type\",\n          \"accuracy\",\n          \"MAE\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"K*\"\n        ],\n        \"rows\": [\n          [\n            \"Handcrafted (15D)\",\n            0.37,\n            1.08,\n            0.7,\n            0.59,\n            2\n          ],\n          [\n            \"Learned (4096D + MLP)\",\n            0.39,\n            1.05,\n            0.72,\n            0.58,\n            2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Learned representation 实验排除了 feature engineering 作为 bottleneck 的可能性。 在论文中，这是 important control：证明 K*=2 是 data-intrinsic 的 ceiling， 与 feature choice 无关。同时 justify 了使用 interpretable handcrafted features 作为 primary analysis tool（loss < 2pp accuracy, gain = full interpretability for C2 analysis）。\\n\\n\\n在 worst 档下，learned representations 略优于 handcrafted features，但不改变 K*。\\nFrozen LM embeddings（4096-dim from last layer）+ 2-layer MLP 有更大的 capacity 来 capture subtle distributional differences。1v2 AUC 从 handcrafted 的 0.70 提升到 0.72——这表明 LM embeddings 确实 encode 了一些 handcrafted features 未 capture 的信息。 但 2v3 AUC 仍然只有 0.58，不足以突破 K*=2 的 boundary。\\naccuracy 提升 2pp（0.39 vs 0.37），MAE 改善 0.03（1.05 vs 1.08）—— 这些差异在统计上可能 significant（取决于 test set size），但 practically negligible。\\n关键洞察：learned representations 的 marginal improvement 确认了 handcrafted features 不是 bottleneck——K*=2 是 information-theoretic ceiling，不是 feature engineering 的限制。 即使用模型自身的 full-dimensional representation，depth 2+ 的信号仍然不足。\\n这对 worst narrative 是重要支撑：既排除了 \\\"better features might help\\\" 的 objection， 又验证了 handcrafted features 的 interpretability 价值不是以 significant accuracy 为代价的。\\n\"\n  },\n  {\n    \"name\": \"Base vs Instruct model comparison\",\n    \"description\": \"Qwen2.5-1.5B base vs Instruct 的 K* 和特征分布差异。\\n\",\n    \"results\": {\n      \"base\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.982,\n        \"pairwise_auc_1v2\": 0.64,\n        \"pairwise_auc_2v3\": 0.55,\n        \"pairwise_jsd_0v1\": 0.21,\n        \"pairwise_jsd_1v2\": 0.012,\n        \"pairwise_jsd_2v3\": 0.004,\n        \"ordinal_accuracy\": 0.34,\n        \"ordinal_mae\": 1.15\n      },\n      \"instruct_mvp_reference\": {\n        \"k_star\": 2,\n        \"pairwise_auc_0v1\": 0.996,\n        \"pairwise_auc_1v2\": 0.7,\n        \"pairwise_auc_2v3\": 0.59,\n        \"pairwise_jsd_0v1\": 0.267,\n        \"pairwise_jsd_1v2\": 0.016,\n        \"pairwise_jsd_2v3\": 0.007\n      },\n      \"base_vs_instruct_0v1_jsd_delta\": -0.057,\n      \"base_vs_instruct_1v2_auc_delta\": -0.06\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Base vs Instruct comparison (Qwen2.5-1.5B)\",\n        \"columns\": [\n          \"variant\",\n          \"K*\",\n          \"AUC_0v1\",\n          \"AUC_1v2\",\n          \"AUC_2v3\",\n          \"JSD_0v1\",\n          \"ordinal_acc\"\n        ],\n        \"rows\": [\n          [\n            \"Instruct (MVP)\",\n            2,\n            0.996,\n            0.7,\n            0.59,\n            0.267,\n            0.42\n          ],\n          [\n            \"Base\",\n            2,\n            0.982,\n            0.64,\n            0.55,\n            0.21,\n            0.34\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Base vs Instruct 对比提供了对 RLHF 效应的洞察：instruction tuning 增强了 human vs machine 的 detectability（因为 RLHF 引入了 specific stylistic patterns）， 但不改变 recursive degradation dynamics。在 worst 档下，两个 variant 的 K*=2 进一步缩小了 \\\"K* might vary with model variant\\\" 的可能性空间。 论文可以简短讨论此结果，作为 K* universality 的 additional evidence point。\\n\\n在 worst 档下，Base model 也产生 K*=2，但信号绝对值更低。\\nBase model（未经 instruction tuning）的 generation 更 \\\"raw\\\"—— less coherent, higher entropy, less human-like structure。这导致：\\n(1) 0v1 gap 更小（JSD 0.210 vs Instruct 0.267）：base model 的输出本身就\\n    less structured than human text but also less \\\"distinctively machine-like\\\"\\n    compared to Instruct models（后者有 RLHF-induced patterns 如 hedging language,\\n    structured responses that are clearly non-human）；\\n\\n(2) 1v2 AUC 更低（0.64 vs 0.70）：base model 的递归 generation 更 chaotic，\\n    gen-1 和 gen-2 在 feature space 中更接近——high entropy generation 在\\n    first pass 就引入大量噪声，使后续代际差异更小；\\n\\n(3) K* 不变：尽管绝对信号更弱，depth 2+ 的 collapse 模式相同。\\n这表明 RLHF/instruction tuning 使模型输出更 \\\"detectably machine-like\\\" （higher 0v1 signal），但不改变 recursive degradation 的 fundamental dynamics。 对 worst narrative：base model 结果是对 K*=2 universality 的又一确认， 且暗示实际世界中 base model 生成的 recursive text 更难检测（更低的 0v1 AUC）。\\n\"\n  }\n]",
      "numLines": 1150,
      "startLine": 1,
      "totalLines": 1150
    }
  },
  "sourceToolAssistantUUID": "eb1dd495-7f7a-46f9-ad06-a44b1aa5391f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contami…",
  "leafUuid": "0544a6e3-1a10-432e-95d9-1bedbc2ca2a3",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing generational depth saturation in synthetic text",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Assistant

_source line 12 · 2026-05-12T20:32:15.172Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the experiment data and craft a complete LaTeX paper. This is a "worst" tier dream paper, framed as a negative-result / empirical analysis paper. The narrative guidance says:

- Reframe from method paper to empirical analysis / negative-result paper
- Core message: "Generational signals in recursive synthetic text collapse to indistinguishable after depth 2 — a direct consequence of DPI, and current 1-7B models cannot modulate this via decoding strategy"
- C1 becomes pure characterization: "K*=2 is a hard, universal ceiling"
- C2 is dropped or demoted to appendix


- C3 shifts to showing graduated filtering hits fundamental limits once signal collapse occurs
- The paper's contribution is rigorous negative characterization, DPI theory verification, and a cautionary message about the approach

Now I'm compiling the LaTeX paper using the experimental results. The data consistently shows K*=2 as the saturation point across all tested models and decoding strategies, which becomes the empirical anchor for the entire narrative.

Looking at the key findings: JSD measurements reveal steep decay between layers, graduated versus binary filtering shows no meaningful performance difference, cross-model transfer is dramatically asymmetric, and feature degradation patterns are inconsistent across architectures. The learned representations don't overcome the K*=2 ceiling, zero-shot depth estimation fails, and retraining preserves K* but shifts the underlying feature dynamics. These results paint a picture where the fundamental constraint isn't about the filtering method—it's about what the model can actually learn to represent.

Now I'm setting up the paper structure and preparing the output directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0544a6e3-1a10-432e-95d9-1bedbc2ca2a3",
  "isSidechain": false,
  "requestId": "req_011CayJxn9rrgPyxFUJh939q",
  "type": "assistant",
  "uuid": "44d07532-8b7b-404d-b577-54f9deb30df9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHQUxdbAmtHcHRFJo5WioJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22489,
      "cache_read_input_tokens": 24511,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 24511,
          "cache_creation_input_tokens": 22489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22489
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

_source line 13 · 2026-05-12T20:32:15.177Z_

Data loaded. Now writing the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44d07532-8b7b-404d-b577-54f9deb30df9",
  "isSidechain": false,
  "requestId": "req_011CayJxn9rrgPyxFUJh939q",
  "type": "assistant",
  "uuid": "8b0cb9a6-9e0a-4f84-a84a-f5ea018fba5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHQUxdbAmtHcHRFJo5WioJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22489,
      "cache_read_input_tokens": 24511,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 24511,
          "cache_creation_input_tokens": 22489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22489
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

_source line 14 · 2026-05-12T20:32:16.865Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01S1PcPoHUrV4pxHzR3ggBuA`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/",
  "description": "Check output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b0cb9a6-9e0a-4f84-a84a-f5ea018fba5f",
  "isSidechain": false,
  "requestId": "req_011CayJxn9rrgPyxFUJh939q",
  "type": "assistant",
  "uuid": "ef72a4e4-072a-4c57-ab67-c8a310b895af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FHQUxdbAmtHcHRFJo5WioJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22489,
      "cache_read_input_tokens": 24511,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 724,
          "cache_read_input_tokens": 24511,
          "cache_creation_input_tokens": 22489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22489
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

_source line 15 · 2026-05-12T20:32:17.022Z_

<details><summary>↩ Tool result · `toolu_01S1PcPoHUrV4pxHzR3ggBuA`</summary>

```text
experiment_data.json
imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef72a4e4-072a-4c57-ab67-c8a310b895af",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "4c336daf-830b-4d9e-9a75-b10990d0f5f7",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ef72a4e4-072a-4c57-ab67-c8a310b895af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T20:34:56.206Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VhCPNVpLckiUbY51AHPopV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Depth~2 Ceiling: Generational Signals in Recursive Synthetic Text\\\\Collapse Beyond First-Generation Detection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic text---machine-generated content that is itself generated from prior machine outputs.\nWhile binary detection (human vs.\\ synthetic) is well studied, estimating the \\emph{generational depth} of such text remains unexplored.\nWe formalize recursive generation as an iterated lossy channel and derive from the Data Processing Inequality (DPI) that a \\emph{saturation boundary} $K^*$ must exist beyond which consecutive generations become statistically indistinguishable.\nThrough controlled experiments across three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B), four decoding strategies, and a 7B scale probe, we establish $K^*=2$ as a hard, universal ceiling for models in the 1--7B range: pairwise Jensen--Shannon divergence decays from 0.27 (depth 0 vs.\\ 1) to $<$0.005 (depth 2 vs.\\ 3), and no combination of model architecture, decoding strategy, or feature representation shifts this boundary.\nConsequently, graduated depth-aware filtering offers no statistically significant advantage over binary filtering on downstream benchmarks ($\\Delta\\leq$0.2pp, $p>0.4$).\nThese negative results carry direct practical implications: depth-aware data curation has an extremely narrow actionable window (human / gen-1 / gen-2+), and community efforts should focus on first-generation detection rather than fine-grained depth estimation.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe proliferation of large language models (LLMs) has led to a feedback loop in which machine-generated text enters web corpora, is scraped, and is used to train subsequent models~\\cite{shumailov2024ai}.\nThis \\emph{recursive contamination} raises data quality concerns that binary synthetic-text detectors~\\cite{mitchell2023detectgpt,hans2024binoculars} are not designed to address: they classify text as human or machine-generated but do not distinguish first-generation synthetic text (relatively high quality) from fourth-generation text (potentially degenerate).\n\nA natural question arises: \\emph{can we estimate the generational depth of synthetic text, and does such estimation improve data curation?}\nIn this work, we provide a rigorous negative answer to both questions for current-scale (1--7B) language models.\n\nWe model recursive text generation as an iterated lossy channel, where each generation pass loses mutual information with the original human distribution.\nThe Data Processing Inequality (DPI) guarantees the existence of a \\emph{saturation boundary} $K^*$---the maximum depth at which consecutive generations remain distinguishable.\nOur contribution is the first systematic measurement of $K^*$ across controlled experimental conditions, yielding a stark finding:\n\n\\begin{itemize}\n    \\item $K^*=2$ is invariant across three model families (Qwen2.5, Pythia, OLMo), four decoding strategies (greedy, nucleus $p$=0.9, $T$=0.7, $T$=1.2), base vs.\\ instruct variants, and scales from 1B to 7B parameters.\n    \\item Graduated filtering (exploiting depth beyond the binary distinction) provides $\\leq$0.2 percentage points of improvement over binary filtering, statistically indistinguishable from zero ($p>0.4$).\n    \\item Neither learned representations (frozen LM embeddings) nor frontier LLMs (GPT-4o, Claude~3.5) can penetrate the $K^*=2$ ceiling.\n\\end{itemize}\n\nThese results constitute a \\emph{cautionary message} for the community: the window for depth-aware data curation is extremely narrow---effectively a three-class problem (human / gen-1 / gen-2+)---and the marginal value of depth estimation over binary detection is negligible at current model scales.\nData governance efforts are better directed at robust first-generation detection.\n\n\\section{Background and Theoretical Framework}\n\n\\subsection{Recursive Generation as an Iterated Lossy Channel}\n\nLet $P_0$ denote the human text distribution and $P_k$ the distribution after $k$ rounds of generation through a language model $\\mathcal{M}$.\nEach generation step applies a stochastic mapping $T_\\mathcal{M}: P_{k-1} \\mapsto P_k$.\nWe model $T_\\mathcal{M}$ as a lossy channel: while $\\mathcal{M}$ approximates its input distribution, it introduces systematic biases (lower perplexity variance, reduced lexical diversity, peaked token distributions) that constitute information loss.\n\n\\subsection{Data Processing Inequality and the Saturation Boundary}\n\nBy the DPI, for any Markov chain $P_0 \\to P_1 \\to \\cdots \\to P_k$:\n\\begin{equation}\n    I(P_0; P_k) \\leq I(P_0; P_{k-1}) \\leq \\cdots \\leq I(P_0; P_1)\n\\end{equation}\nwhere $I(\\cdot;\\cdot)$ denotes mutual information.\nThe Jensen--Shannon divergence between consecutive generations $\\text{JSD}(P_{k-1}, P_k)$ is bounded above by the mutual information, and must therefore be monotonically non-increasing.\nWe define the \\emph{saturation boundary}:\n\\begin{equation}\n    K^* = \\max\\{k : \\text{AUC}(P_{k-1}, P_k) > \\tau\\}\n\\end{equation}\nwhere $\\text{AUC}(P_{k-1}, P_k)$ is the area under the ROC curve for pairwise binary classification between generations $k{-}1$ and $k$, and $\\tau$ is a discrimination threshold (default $\\tau=0.60$).\n\nThe DPI guarantees that $K^*$ is finite for any lossy channel.\nOur empirical question is: \\emph{how small is $K^*$ in practice?}\n\n\\subsection{Related Work}\n\n\\paragraph{Model Collapse.} \\citet{shumailov2024ai} demonstrate that iterative training on model outputs leads to distributional collapse. Our work measures the \\emph{speed} of this collapse in the feature space relevant to detection, rather than its long-run consequences for model quality.\n\n\\paragraph{Binary Synthetic Text Detection.} Methods such as DetectGPT~\\cite{mitchell2023detectgpt}, Binoculars~\\cite{hans2024binoculars}, and DivEye treat detection as a binary task. We show that the confidence scores of these detectors carry negligible depth information (Spearman $\\rho \\leq 0.22$; depth-2+ $\\rho < 0.05$).\n\n\\paragraph{Data Quality Filtering.} Verification-based approaches~\\cite{feng2024towards,yi2024on} use external verifiers for binary quality gating. We investigate whether \\emph{ordinal} depth signals can refine such filtering, and find that they cannot.\n\n\\section{Experimental Setup}\n\n\\subsection{Depth Chain Construction}\n\nFor each model $\\mathcal{M}$ and seed corpus, we construct a \\emph{depth chain}: a sequence of corpora $\\{D_0, D_1, \\ldots, D_5\\}$ where $D_0$ is human text and $D_k$ ($k \\geq 1$) is generated by prompting $\\mathcal{M}$ to continue or paraphrase documents from $D_{k-1}$.\nWe use 5,000 documents from C4 as the seed corpus $D_0$.\n\n\\paragraph{Models.} Qwen2.5-1.5B-Instruct (primary), Pythia-1.4B, OLMo-1B, and Qwen2.5-7B (scale probe, 1K documents, depth 0--3).\n\n\\paragraph{Decoding Strategies.} Nucleus $p$=0.95 $T$=1.0 (default), greedy, nucleus $p$=0.9, $T$=0.7, and $T$=1.2.\n\n\\subsection{Feature Extraction}\n\nWe extract 15 handcrafted features organized into three groups:\n\\textbf{Surprisal statistics} (mean, variance, skewness of token-level log-probabilities under an external scorer),\n\\textbf{Diversity metrics} (type-token ratio, hapax ratio, entropy of unigram distribution), and\n\\textbf{Tail-thinning indicators} (fraction of tokens in the bottom-5\\% probability mass, kurtosis of the token distribution).\n\nAs a control, we also evaluate \\textbf{learned representations}: frozen Qwen2.5-1.5B last-layer embeddings (4096-dim) with a 2-layer MLP.\n\n\\subsection{Depth Estimation Methods}\n\nWe compare four approaches: (1) \\textbf{CORAL}~\\cite{cao2020rank}---ordinal classification with consistent rank predictions; (2) \\textbf{Standard multiclass}---softmax cross-entropy, no ordinal structure; (3) \\textbf{Ordinal regression}---continuous depth prediction with discretization; (4) \\textbf{Binary + random depth}---binary (human vs.\\ synthetic) classifier followed by uniform random depth assignment for synthetic texts.\n\n\\subsection{Downstream Evaluation}\n\nWe evaluate four data filtering strategies via continued pretraining of Qwen2.5-1.5B on filtered corpora, followed by evaluation on MMLU and HellaSwag (3 seeds):\n\\textbf{No filter}, \\textbf{Binary} (remove all predicted synthetic), \\textbf{Graduated} (depth-weighted inclusion), and \\textbf{Surprisal-based} (continuous surprisal score as quality proxy).\n\n\\section{Results}\n\n\\subsection{$K^*=2$ Is a Universal Ceiling}\n\nTable~\\ref{tab:cross_model} presents pairwise discrimination results across three model families.\nAll models yield $K^*=2$ at $\\tau=0.60$: the 0-vs-1 boundary is nearly perfectly separable (AUC $\\geq$ 0.988), the 1-vs-2 boundary is marginally above chance (AUC 0.61--0.70), and all subsequent boundaries are at chance level (AUC $\\leq$ 0.56).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$K^*$} & \\textbf{AUC} & \\textbf{AUC} & \\textbf{AUC} & \\textbf{JSD} \\\\\n & & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & \\textbf{0v1} \\\\\n\\midrule\nQwen2.5-1.5B & 2 & .996 & .70 & .59 & .267 \\\\\nPythia-1.4B   & 2 & .991 & .63 & .55 & .231 \\\\\nOLMo-1B      & 2 & .988 & .61 & .54 & .218 \\\\\nQwen2.5-7B   & 2 & .994 & .65 & .56 & .258 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise discrimination across model families and scales. $K^*=2$ at $\\tau=0.60$ is universal. JSD decays by an order of magnitude from 0v1 to 1v2 in all cases.}\n\\label{tab:cross_model}\n\\end{table}\n\nThe JSD between consecutive generations exhibits rapid monotonic decay consistent with DPI predictions.\nFor Qwen2.5-1.5B, JSD drops from 0.267 (0v1) to 0.016 (1v2) to 0.007 (2v3)---a 38$\\times$ reduction in two steps.\n\n\\paragraph{Scale does not help.}\nQwen2.5-7B ($5\\times$ parameters) yields $K^*=2$ with 1v2 AUC of 0.65---\\emph{lower} than the 1.5B variant (0.70).\nLarger models produce higher-fidelity outputs, making consecutive generations \\emph{more} similar and thus harder to distinguish, offsetting their greater capacity.\n\n\\subsection{Decoding Strategy Cannot Modulate $K^*$}\n\nTable~\\ref{tab:decoding} shows that $K^*=2$ is invariant across four decoding strategies spanning the deterministic-to-high-entropy spectrum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{$K^*$} & \\textbf{AUC 0v1} & \\textbf{AUC 1v2} & \\textbf{JSD 0v1} \\\\\n\\midrule\nGreedy        & 2 & .997 & .62 & .305 \\\\\nNucleus $p$=0.9  & 2 & .996 & .68 & .280 \\\\\n$T$=0.7       & 2 & .997 & .65 & .295 \\\\\n$T$=1.2       & 2 & .993 & .64 & .240 \\\\\nNuc.\\ $p$=0.95 (default) & 2 & .996 & .70 & .267 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). All strategies yield $K^*=2$. The 1v2 AUC range (0.62--0.70) is narrow and never approaches the utility threshold.}\n\\label{tab:decoding}\n\\end{table}\n\nGreedy decoding maximizes the 0v1 JSD (0.305) because deterministic outputs are most distributional distinct from human text, but this does not propagate to deeper generations.\nHigh temperature ($T$=1.2) reduces the 0v1 gap (JSD 0.240) while accelerating signal collapse at depth 2+.\nNo decoding configuration pushes $K^*$ to 3.\n\n\\subsection{$K^*$ Is Robust to Threshold Choice}\n\nWe verify that $K^*=2$ is not an artifact of the threshold $\\tau=0.60$ by computing $K^*$ at four thresholds (Table~\\ref{tab:threshold}).\nAt $\\tau \\geq 0.60$, all models yield $K^*=2$.\nThe sole exception---Qwen at $\\tau=0.55$---reflects its 2v3 AUC of 0.59, marginally above threshold, within statistical noise.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Threshold $\\tau$} & \\textbf{Qwen} & \\textbf{Pythia} & \\textbf{OLMo} \\\\\n\\midrule\n0.55 & 3 & 2 & 2 \\\\\n0.60 & 2 & 2 & 2 \\\\\n0.65 & 2 & 2 & 2 \\\\\n0.70 & 2 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K^*$ across AUC thresholds. Robustness reflects rapid signal collapse rather than measurement precision.}\n\\label{tab:threshold}\n\\end{table}\n\n\\subsection{Feature Representation Does Not Break the Ceiling}\n\nTable~\\ref{tab:features} compares handcrafted features with learned representations.\nFrozen LM embeddings (4096-dim + MLP) achieve 1v2 AUC of 0.72 (+0.02 over handcrafted) and 2v3 AUC of 0.58, yielding the same $K^*=2$.\nThe ceiling is data-intrinsic, not a limitation of feature engineering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Features} & \\textbf{Acc.} & \\textbf{MAE} & \\textbf{AUC 1v2} & \\textbf{$K^*$} \\\\\n\\midrule\nHandcrafted (15D) & .37 & 1.08 & .70 & 2 \\\\\nLearned (4096D) & .39 & 1.05 & .72 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Handcrafted vs.\\ learned representations. The 2pp accuracy gain from 4096-dim learned features does not shift $K^*$.}\n\\label{tab:features}\n\\end{table}\n\n\\subsection{Depth Estimation Accuracy Is Near-Chance}\n\nTable~\\ref{tab:classifiers} compares depth estimation methods.\nCORAL achieves 37\\% accuracy (6-class) with MAE 1.08---only 5pp above a binary classifier with random depth assignment.\nAll methods achieve near-random performance on depth 2--5 classes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Macro-$F_1$} \\\\\n\\midrule\nCORAL (ordinal) & .37 & 1.08 & .22 \\\\\nStandard multiclass & .35 & 1.22 & .19 \\\\\nOrdinal regression & .36 & 1.10 & .21 \\\\\nBinary + random depth & .32 & 1.25 & .18 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Classifier comparison. Ordinal structure provides minimal benefit when only two depth levels are meaningfully distinguishable.}\n\\label{tab:classifiers}\n\\end{table}\n\nFrontier LLMs fare even worse: GPT-4o achieves 24\\% depth accuracy (MAE 1.65) and Claude~3.5 achieves 22\\% (MAE 1.72), both near the 20\\% random baseline.\nNotably, both LLMs retain reasonable binary accuracy (78--81\\%), confirming that depth estimation is a fundamentally harder task than binary detection.\n\n\\subsection{Binary Detector Confidence Is Not a Depth Proxy}\n\nExisting binary detectors' confidence scores carry negligible depth information.\nDivEye and Binoculars achieve strong 0v1 AUC (0.91 and 0.94) but their 1v2 AUC drops to 0.54 and 0.56.\nSpearman correlation between confidence and true depth is weak ($\\rho = 0.18$ and $0.22$), and at depth 2+ the rank correlation is essentially zero ($\\rho < 0.05$).\n\n\\subsection{Graduated Filtering Offers No Significant Advantage}\n\nTable~\\ref{tab:filtering} presents the downstream filtering evaluation.\nBinary filtering improves over no filtering (+0.7pp MMLU, +0.9pp HellaSwag), confirming that removing synthetic text is beneficial.\nHowever, graduated filtering provides only +0.1pp (MMLU) and +0.2pp (HellaSwag) over binary, both statistically non-significant ($p=0.62$ and $p=0.48$, respectively).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo filter & 25.1 \\scriptsize{$\\pm$0.2} & 42.3 \\scriptsize{$\\pm$0.3} \\\\\nBinary & 25.8 \\scriptsize{$\\pm$0.3} & 43.2 \\scriptsize{$\\pm$0.4} \\\\\nGraduated & 25.9 \\scriptsize{$\\pm$0.3} & 43.4 \\scriptsize{$\\pm$0.3} \\\\\nSurprisal-based & 25.7 \\scriptsize{$\\pm$0.2} & 43.1 \\scriptsize{$\\pm$0.4} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation (3 seeds). Graduated filtering's advantage over binary is $\\leq$0.2pp and non-significant ($p > 0.4$).}\n\\label{tab:filtering}\n\\end{table}\n\nThe dose-response experiment (Table~\\ref{tab:dose}) confirms this null result scales with contamination severity: even at 50\\% synthetic injection, graduated filtering gains at most 0.2pp over binary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Bin.\\ MMLU} & \\textbf{Grad.\\ MMLU} & \\textbf{Bin.\\ HS} & \\textbf{Grad.\\ HS} \\\\\n\\midrule\n10\\% & 25.6 & 25.6 & 43.0 & 43.0 \\\\\n30\\% & 25.5 & 25.6 & 42.8 & 42.9 \\\\\n50\\% & 25.2 & 25.3 & 42.3 & 42.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dose-response: graduated advantage does not scale with contamination level ($\\Delta \\leq 0.2$pp at all doses).}\n\\label{tab:dose}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\nTable~\\ref{tab:transfer} reveals a clean separation: binary detection transfers well across models (average accuracy 81\\%), while depth-specific features do not (average 6-class accuracy 28\\%, retention 40\\% of in-domain performance).\nDepth signal beyond the binary distinction is model-specific, requiring per-model classifier retraining---further limiting the practical utility of depth estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Train $\\backslash$ Test} & \\textbf{Qwen} & \\textbf{Pythia} & \\textbf{OLMo} \\\\\n\\midrule\n\\multicolumn{4}{c}{\\emph{6-class accuracy}} \\\\\nQwen  & .37$^*$ & .28 & .26 \\\\\nPythia & .30 & .35$^*$ & .25 \\\\\nOLMo  & .29 & .27 & .33$^*$ \\\\\n\\midrule\n\\multicolumn{4}{c}{\\emph{Binary accuracy (human vs.\\ synthetic)}} \\\\\nQwen  & .93$^*$ & .82 & .79 \\\\\nPythia & .84 & .91$^*$ & .77 \\\\\nOLMo  & .83 & .80 & .88$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer. Binary detection transfers well (avg.\\ 81\\%); depth estimation does not (avg.\\ 28\\%). $^*$In-domain.}\n\\label{tab:transfer}\n\\end{table}\n\n\\section{Discussion}\n\n\\subsection{Why $K^*=2$? An Information-Theoretic Interpretation}\n\nThe DPI predicts monotonic decay of inter-generational mutual information, but does not specify the \\emph{rate}.\nOur measurements suggest that for 1--7B-scale models, the channel $T_\\mathcal{M}$ is sufficiently lossy that a single pass eliminates the vast majority of distributional features distinguishing $P_0$ from $P_1$: the JSD drops by 17--23$\\times$ from 0v1 to 1v2.\nThe second pass reduces the remaining signal to noise floor.\n\nThe invariance of $K^*$ across model families, scales (1B--7B), and decoding strategies implies that $K^*=2$ is not a property of any individual model but a regime-level characteristic of current-scale language models.\nWhether larger models (70B+) would exhibit higher $K^*$ remains an open question beyond our computational scope.\n\n\\subsection{Implications for Data Governance}\n\nOur results simplify the practical problem of synthetic text curation: \\textbf{the actionable regime is binary}.\nPractitioners should invest in robust first-generation detectors (human vs.\\ synthetic) rather than depth estimators.\nThe three-class signal (human / gen-1 / gen-2+) is the finest granularity supported by current detection technology, and even this distinction provides no measurable downstream benefit over binary filtering.\n\n\\subsection{Limitations}\n\n\\paragraph{Prompt-chain vs.\\ retrain-chain.}\nOur primary experiments use prompt chains (model generates from prior outputs without retraining).\nA retrain-chain validation with Pythia-1.4B (LoRA, rank 16) confirms $K^*=2$ but reveals statistically different feature dynamics (KS test $p=0.03$, JSD correlation $r=0.82$).\nPrompt chains are thus a controlled proxy, not a faithful simulation of real-world recursive contamination.\n\n\\paragraph{Scale.}\nOur 7B probe is limited to 1K documents and depth 0--3 due to GPU budget.\nWe cannot rule out that $K^*>2$ at significantly larger scales (e.g., 70B+).\n\n\\paragraph{Feature degradation ordering.}\nIndividual feature groups (surprisal, diversity, tail-thinning) show model-specific degradation orderings (cross-model Kendall $\\tau = 0.33$), with all groups saturating at depth~2 regardless.\nWe do not claim a universal degradation ordering; this remains a descriptive observation.\n\n\\paragraph{Naturalistic validation.}\nApplying our classifier to Common Crawl yields predicted depth--quality correlations of only $\\rho=-0.15$ to $-0.19$, reflecting domain shift from controlled to in-the-wild data.\n\n\\subsection{Base vs.\\ Instruct Models}\n\nInstruction tuning (RLHF) increases 0v1 detectability (JSD 0.267 vs.\\ 0.210 for Qwen2.5-1.5B Instruct vs.\\ Base) by introducing distinctive stylistic patterns, but does not alter the recursive degradation dynamics: both variants yield $K^*=2$.\nBase models may thus pose a greater challenge for binary detection in practice, while the depth estimation ceiling remains unchanged.\n\n\\section{Conclusion}\n\nWe present the first systematic measurement of the generational discrimination boundary $K^*$ for recursive synthetic text.\nAcross three model families, four decoding strategies, two model scales, and two feature representations, $K^*=2$ emerges as a hard, universal ceiling for 1--7B-parameter language models.\nThis is a direct empirical confirmation of the DPI prediction: the iterated lossy channel of recursive generation destroys inter-generational signal within two passes.\n\nThe practical consequence is stark: depth-aware data curation reduces to binary filtering.\nGraduated filtering, ordinal classification, and depth estimation---despite their theoretical appeal---provide no statistically significant improvement over simply removing all detected synthetic text.\nWe urge the community to focus on robust first-generation detection and to treat depth estimation as a fundamentally limited task at current model scales.\n\n\\section*{Acknowledgments}\nOmitted for review.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Retrain-Chain Ecological Validity}\n\\label{app:retrain}\n\nTo assess ecological validity, we construct a retrain chain using Pythia-1.4B with LoRA fine-tuning (rank=16, $\\alpha$=32) on C4 5K documents through depth 0--4.\nTable~\\ref{tab:retrain} compares prompt-chain and retrain-chain results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Prompt-chain} & \\textbf{Retrain-chain} \\\\\n\\midrule\n$K^*$ & 2 & 2 \\\\\nAUC 0v1 & .991 & .972 \\\\\nAUC 1v2 & .63 & .58 \\\\\nAUC 2v3 & .55 & .53 \\\\\nJSD 0v1 & .231 & .185 \\\\\nJSD 1v2 & .012 & .008 \\\\\nFeature KS-test $p$ & --- & .03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-chain vs.\\ retrain-chain (Pythia-1.4B). $K^*$ is preserved; absolute signal levels are lower under retraining; feature distributions differ significantly.}\n\\label{tab:retrain}\n\\end{table}\n\n$K^*=2$ is preserved under retraining, but absolute AUC and JSD values are uniformly lower, consistent with retraining accelerating the lossy-channel effect.\nThe significant KS test ($p=0.03$) indicates that while the saturation boundary is consistent, the feature-level dynamics differ, and prompt-chain classifiers should not be directly deployed on retrain-chain data without adaptation.\n\n\\section{Feature Group Degradation Analysis}\n\\label{app:features}\n\nTable~\\ref{tab:feat_group} presents per-feature-group 1v2 AUC by model.\nAll groups saturate at depth~2 regardless of model, but the \\emph{ordering} of degradation (which group loses signal first) is model-specific (cross-model Kendall $\\tau = 0.33$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Surprisal} & \\textbf{Diversity} & \\textbf{Tail} \\\\\n\\midrule\nQwen2.5-1.5B & .63 & .58 & .61 \\\\\nPythia-1.4B & .56 & .60 & .59 \\\\\nOLMo-1B & .58 & .59 & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-feature-group 1v2 AUC. All groups saturate at depth 2; degradation ordering is inconsistent across models.}\n\\label{tab:feat_group}\n\\end{table}\n\n\\section{LLM Zero-Shot Depth Estimation}\n\\label{app:llm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{5-class Acc.} & \\textbf{MAE} & \\textbf{Binary Acc.} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nGPT-4o & .24 & 1.65 & .78 & .12 \\\\\nClaude 3.5 & .22 & 1.72 & .81 & .10 \\\\\nRandom & .20 & 2.00 & .50 & .00 \\\\\nCORAL (ours) & .37 & 1.08 & .93 & .35 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM zero-shot depth estimation. Frontier LLMs achieve near-random depth accuracy despite reasonable binary detection.}\n\\label{tab:llm_zeroshot}\n\\end{table}\n\n\\section{Naturalistic Validation}\n\\label{app:naturalistic}\n\nApplying our Qwen2.5-1.5B-trained classifier to Common Crawl 2025--2026 snapshots yields:\npredicted 62\\% human, 25\\% gen-1, 13\\% depth-2+.\nCorrelation of predicted depth with AlignScore is $-0.15$; with vocabulary richness, $-0.19$.\nBinary synthetic prediction correlates more strongly with quality ($\\rho=-0.28$), consistent with our main finding that depth signal beyond binary is weak.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c336daf-830b-4d9e-9a75-b10990d0f5f7",
  "isSidechain": false,
  "requestId": "req_011CayJzKkfdciCjWocvYJ1c",
  "type": "assistant",
  "uuid": "10faee29-85ea-4d8c-9924-d84324c8e34a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TE7mraUeK7w6zCfJsaWab",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 47000,
      "output_tokens": 8457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8457,
          "cache_read_input_tokens": 47000,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 17 · 2026-05-12T20:34:56.223Z_

<details><summary>↩ Tool result · `toolu_01VhCPNVpLckiUbY51AHPopV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10faee29-85ea-4d8c-9924-d84324c8e34a",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "0d53b3eb-ed1d-48a3-b451-ac3e288d559a",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\title{The Depth~2 Ceiling: Generational Signals in Recursive Synthetic Text\\\\Collapse Beyond First-Generation Detection}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic text---machine-generated content that is itself generated from prior machine outputs.\nWhile binary detection (human vs.\\ synthetic) is well studied, estimating the \\emph{generational depth} of such text remains unexplored.\nWe formalize recursive generation as an iterated lossy channel and derive from the Data Processing Inequality (DPI) that a \\emph{saturation boundary} $K^*$ must exist beyond which consecutive generations become statistically indistinguishable.\nThrough controlled experiments across three model families (Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B), four decoding strategies, and a 7B scale probe, we establish $K^*=2$ as a hard, universal ceiling for models in the 1--7B range: pairwise Jensen--Shannon divergence decays from 0.27 (depth 0 vs.\\ 1) to $<$0.005 (depth 2 vs.\\ 3), and no combination of model architecture, decoding strategy, or feature representation shifts this boundary.\nConsequently, graduated depth-aware filtering offers no statistically significant advantage over binary filtering on downstream benchmarks ($\\Delta\\leq$0.2pp, $p>0.4$).\nThese negative results carry direct practical implications: depth-aware data curation has an extremely narrow actionable window (human / gen-1 / gen-2+), and community efforts should focus on first-generation detection rather than fine-grained depth estimation.\n\\end{abstract}\n\n\\section{Introduction}\n\nThe proliferation of large language models (LLMs) has led to a feedback loop in which machine-generated text enters web corpora, is scraped, and is used to train subsequent models~\\cite{shumailov2024ai}.\nThis \\emph{recursive contamination} raises data quality concerns that binary synthetic-text detectors~\\cite{mitchell2023detectgpt,hans2024binoculars} are not designed to address: they classify text as human or machine-generated but do not distinguish first-generation synthetic text (relatively high quality) from fourth-generation text (potentially degenerate).\n\nA natural question arises: \\emph{can we estimate the generational depth of synthetic text, and does such estimation improve data curation?}\nIn this work, we provide a rigorous negative answer to both questions for current-scale (1--7B) language models.\n\nWe model recursive text generation as an iterated lossy channel, where each generation pass loses mutual information with the original human distribution.\nThe Data Processing Inequality (DPI) guarantees the existence of a \\emph{saturation boundary} $K^*$---the maximum depth at which consecutive generations remain distinguishable.\nOur contribution is the first systematic measurement of $K^*$ across controlled experimental conditions, yielding a stark finding:\n\n\\begin{itemize}\n    \\item $K^*=2$ is invariant across three model families (Qwen2.5, Pythia, OLMo), four decoding strategies (greedy, nucleus $p$=0.9, $T$=0.7, $T$=1.2), base vs.\\ instruct variants, and scales from 1B to 7B parameters.\n    \\item Graduated filtering (exploiting depth beyond the binary distinction) provides $\\leq$0.2 percentage points of improvement over binary filtering, statistically indistinguishable from zero ($p>0.4$).\n    \\item Neither learned representations (frozen LM embeddings) nor frontier LLMs (GPT-4o, Claude~3.5) can penetrate the $K^*=2$ ceiling.\n\\end{itemize}\n\nThese results constitute a \\emph{cautionary message} for the community: the window for depth-aware data curation is extremely narrow---effectively a three-class problem (human / gen-1 / gen-2+)---and the marginal value of depth estimation over binary detection is negligible at current model scales.\nData governance efforts are better directed at robust first-generation detection.\n\n\\section{Background and Theoretical Framework}\n\n\\subsection{Recursive Generation as an Iterated Lossy Channel}\n\nLet $P_0$ denote the human text distribution and $P_k$ the distribution after $k$ rounds of generation through a language model $\\mathcal{M}$.\nEach generation step applies a stochastic mapping $T_\\mathcal{M}: P_{k-1} \\mapsto P_k$.\nWe model $T_\\mathcal{M}$ as a lossy channel: while $\\mathcal{M}$ approximates its input distribution, it introduces systematic biases (lower perplexity variance, reduced lexical diversity, peaked token distributions) that constitute information loss.\n\n\\subsection{Data Processing Inequality and the Saturation Boundary}\n\nBy the DPI, for any Markov chain $P_0 \\to P_1 \\to \\cdots \\to P_k$:\n\\begin{equation}\n    I(P_0; P_k) \\leq I(P_0; P_{k-1}) \\leq \\cdots \\leq I(P_0; P_1)\n\\end{equation}\nwhere $I(\\cdot;\\cdot)$ denotes mutual information.\nThe Jensen--Shannon divergence between consecutive generations $\\text{JSD}(P_{k-1}, P_k)$ is bounded above by the mutual information, and must therefore be monotonically non-increasing.\nWe define the \\emph{saturation boundary}:\n\\begin{equation}\n    K^* = \\max\\{k : \\text{AUC}(P_{k-1}, P_k) > \\tau\\}\n\\end{equation}\nwhere $\\text{AUC}(P_{k-1}, P_k)$ is the area under the ROC curve for pairwise binary classification between generations $k{-}1$ and $k$, and $\\tau$ is a discrimination threshold (default $\\tau=0.60$).\n\nThe DPI guarantees that $K^*$ is finite for any lossy channel.\nOur empirical question is: \\emph{how small is $K^*$ in practice?}\n\n\\subsection{Related Work}\n\n\\paragraph{Model Collapse.} \\citet{shumailov2024ai} demonstrate that iterative training on model outputs leads to distributional collapse. Our work measures the \\emph{speed} of this collapse in the feature space relevant to detection, rather than its long-run consequences for model quality.\n\n\\paragraph{Binary Synthetic Text Detection.} Methods such as DetectGPT~\\cite{mitchell2023detectgpt}, Binoculars~\\cite{hans2024binoculars}, and DivEye treat detection as a binary task. We show that the confidence scores of these detectors carry negligible depth information (Spearman $\\rho \\leq 0.22$; depth-2+ $\\rho < 0.05$).\n\n\\paragraph{Data Quality Filtering.} Verification-based approaches~\\cite{feng2024towards,yi2024on} use external verifiers for binary quality gating. We investigate whether \\emph{ordinal} depth signals can refine such filtering, and find that they cannot.\n\n\\section{Experimental Setup}\n\n\\subsection{Depth Chain Construction}\n\nFor each model $\\mathcal{M}$ and seed corpus, we construct a \\emph{depth chain}: a sequence of corpora $\\{D_0, D_1, \\ldots, D_5\\}$ where $D_0$ is human text and $D_k$ ($k \\geq 1$) is generated by prompting $\\mathcal{M}$ to continue or paraphrase documents from $D_{k-1}$.\nWe use 5,000 documents from C4 as the seed corpus $D_0$.\n\n\\paragraph{Models.} Qwen2.5-1.5B-Instruct (primary), Pythia-1.4B, OLMo-1B, and Qwen2.5-7B (scale probe, 1K documents, depth 0--3).\n\n\\paragraph{Decoding Strategies.} Nucleus $p$=0.95 $T$=1.0 (default), greedy, nucleus $p$=0.9, $T$=0.7, and $T$=1.2.\n\n\\subsection{Feature Extraction}\n\nWe extract 15 handcrafted features organized into three groups:\n\\textbf{Surprisal statistics} (mean, variance, skewness of token-level log-probabilities under an external scorer),\n\\textbf{Diversity metrics} (type-token ratio, hapax ratio, entropy of unigram distribution), and\n\\textbf{Tail-thinning indicators} (fraction of tokens in the bottom-5\\% probability mass, kurtosis of the token distribution).\n\nAs a control, we also evaluate \\textbf{learned representations}: frozen Qwen2.5-1.5B last-layer embeddings (4096-dim) with a 2-layer MLP.\n\n\\subsection{Depth Estimation Methods}\n\nWe compare four approaches: (1) \\textbf{CORAL}~\\cite{cao2020rank}---ordinal classification with consistent rank predictions; (2) \\textbf{Standard multiclass}---softmax cross-entropy, no ordinal structure; (3) \\textbf{Ordinal regression}---continuous depth prediction with discretization; (4) \\textbf{Binary + random depth}---binary (human vs.\\ synthetic) classifier followed by uniform random depth assignment for synthetic texts.\n\n\\subsection{Downstream Evaluation}\n\nWe evaluate four data filtering strategies via continued pretraining of Qwen2.5-1.5B on filtered corpora, followed by evaluation on MMLU and HellaSwag (3 seeds):\n\\textbf{No filter}, \\textbf{Binary} (remove all predicted synthetic), \\textbf{Graduated} (depth-weighted inclusion), and \\textbf{Surprisal-based} (continuous surprisal score as quality proxy).\n\n\\section{Results}\n\n\\subsection{$K^*=2$ Is a Universal Ceiling}\n\nTable~\\ref{tab:cross_model} presents pairwise discrimination results across three model families.\nAll models yield $K^*=2$ at $\\tau=0.60$: the 0-vs-1 boundary is nearly perfectly separable (AUC $\\geq$ 0.988), the 1-vs-2 boundary is marginally above chance (AUC 0.61--0.70), and all subsequent boundaries are at chance level (AUC $\\leq$ 0.56).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{$K^*$} & \\textbf{AUC} & \\textbf{AUC} & \\textbf{AUC} & \\textbf{JSD} \\\\\n & & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & \\textbf{0v1} \\\\\n\\midrule\nQwen2.5-1.5B & 2 & .996 & .70 & .59 & .267 \\\\\nPythia-1.4B   & 2 & .991 & .63 & .55 & .231 \\\\\nOLMo-1B      & 2 & .988 & .61 & .54 & .218 \\\\\nQwen2.5-7B   & 2 & .994 & .65 & .56 & .258 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise discrimination across model families and scales. $K^*=2$ at $\\tau=0.60$ is universal. JSD decays by an order of magnitude from 0v1 to 1v2 in all cases.}\n\\label{tab:cross_model}\n\\end{table}\n\nThe JSD between consecutive generations exhibits rapid monotonic decay consistent with DPI predictions.\nFor Qwen2.5-1.5B, JSD drops from 0.267 (0v1) to 0.016 (1v2) to 0.007 (2v3)---a 38$\\times$ reduction in two steps.\n\n\\paragraph{Scale does not help.}\nQwen2.5-7B ($5\\times$ parameters) yields $K^*=2$ with 1v2 AUC of 0.65---\\emph{lower} than the 1.5B variant (0.70).\nLarger models produce higher-fidelity outputs, making consecutive generations \\emph{more} similar and thus harder to distinguish, offsetting their greater capacity.\n\n\\subsection{Decoding Strategy Cannot Modulate $K^*$}\n\nTable~\\ref{tab:decoding} shows that $K^*=2$ is invariant across four decoding strategies spanning the deterministic-to-high-entropy spectrum.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{$K^*$} & \\textbf{AUC 0v1} & \\textbf{AUC 1v2} & \\textbf{JSD 0v1} \\\\\n\\midrule\nGreedy        & 2 & .997 & .62 & .305 \\\\\nNucleus $p$=0.9  & 2 & .996 & .68 & .280 \\\\\n$T$=0.7       & 2 & .997 & .65 & .295 \\\\\n$T$=1.2       & 2 & .993 & .64 & .240 \\\\\nNuc.\\ $p$=0.95 (default) & 2 & .996 & .70 & .267 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decoding strategy ablation (Qwen2.5-1.5B). All strategies yield $K^*=2$. The 1v2 AUC range (0.62--0.70) is narrow and never approaches the utility threshold.}\n\\label{tab:decoding}\n\\end{table}\n\nGreedy decoding maximizes the 0v1 JSD (0.305) because deterministic outputs are most distributional distinct from human text, but this does not propagate to deeper generations.\nHigh temperature ($T$=1.2) reduces the 0v1 gap (JSD 0.240) while accelerating signal collapse at depth 2+.\nNo decoding configuration pushes $K^*$ to 3.\n\n\\subsection{$K^*$ Is Robust to Threshold Choice}\n\nWe verify that $K^*=2$ is not an artifact of the threshold $\\tau=0.60$ by computing $K^*$ at four thresholds (Table~\\ref{tab:threshold}).\nAt $\\tau \\geq 0.60$, all models yield $K^*=2$.\nThe sole exception---Qwen at $\\tau=0.55$---reflects its 2v3 AUC of 0.59, marginally above threshold, within statistical noise.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Threshold $\\tau$} & \\textbf{Qwen} & \\textbf{Pythia} & \\textbf{OLMo} \\\\\n\\midrule\n0.55 & 3 & 2 & 2 \\\\\n0.60 & 2 & 2 & 2 \\\\\n0.65 & 2 & 2 & 2 \\\\\n0.70 & 2 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$K^*$ across AUC thresholds. Robustness reflects rapid signal collapse rather than measurement precision.}\n\\label{tab:threshold}\n\\end{table}\n\n\\subsection{Feature Representation Does Not Break the Ceiling}\n\nTable~\\ref{tab:features} compares handcrafted features with learned representations.\nFrozen LM embeddings (4096-dim + MLP) achieve 1v2 AUC of 0.72 (+0.02 over handcrafted) and 2v3 AUC of 0.58, yielding the same $K^*=2$.\nThe ceiling is data-intrinsic, not a limitation of feature engineering.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Features} & \\textbf{Acc.} & \\textbf{MAE} & \\textbf{AUC 1v2} & \\textbf{$K^*$} \\\\\n\\midrule\nHandcrafted (15D) & .37 & 1.08 & .70 & 2 \\\\\nLearned (4096D) & .39 & 1.05 & .72 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Handcrafted vs.\\ learned representations. The 2pp accuracy gain from 4096-dim learned features does not shift $K^*$.}\n\\label{tab:features}\n\\end{table}\n\n\\subsection{Depth Estimation Accuracy Is Near-Chance}\n\nTable~\\ref{tab:classifiers} compares depth estimation methods.\nCORAL achieves 37\\% accuracy (6-class) with MAE 1.08---only 5pp above a binary classifier with random depth assignment.\nAll methods achieve near-random performance on depth 2--5 classes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{MAE} & \\textbf{Macro-$F_1$} \\\\\n\\midrule\nCORAL (ordinal) & .37 & 1.08 & .22 \\\\\nStandard multiclass & .35 & 1.22 & .19 \\\\\nOrdinal regression & .36 & 1.10 & .21 \\\\\nBinary + random depth & .32 & 1.25 & .18 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Classifier comparison. Ordinal structure provides minimal benefit when only two depth levels are meaningfully distinguishable.}\n\\label{tab:classifiers}\n\\end{table}\n\nFrontier LLMs fare even worse: GPT-4o achieves 24\\% depth accuracy (MAE 1.65) and Claude~3.5 achieves 22\\% (MAE 1.72), both near the 20\\% random baseline.\nNotably, both LLMs retain reasonable binary accuracy (78--81\\%), confirming that depth estimation is a fundamentally harder task than binary detection.\n\n\\subsection{Binary Detector Confidence Is Not a Depth Proxy}\n\nExisting binary detectors' confidence scores carry negligible depth information.\nDivEye and Binoculars achieve strong 0v1 AUC (0.91 and 0.94) but their 1v2 AUC drops to 0.54 and 0.56.\nSpearman correlation between confidence and true depth is weak ($\\rho = 0.18$ and $0.22$), and at depth 2+ the rank correlation is essentially zero ($\\rho < 0.05$).\n\n\\subsection{Graduated Filtering Offers No Significant Advantage}\n\nTable~\\ref{tab:filtering} presents the downstream filtering evaluation.\nBinary filtering improves over no filtering (+0.7pp MMLU, +0.9pp HellaSwag), confirming that removing synthetic text is beneficial.\nHowever, graduated filtering provides only +0.1pp (MMLU) and +0.2pp (HellaSwag) over binary, both statistically non-significant ($p=0.62$ and $p=0.48$, respectively).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo filter & 25.1 \\scriptsize{$\\pm$0.2} & 42.3 \\scriptsize{$\\pm$0.3} \\\\\nBinary & 25.8 \\scriptsize{$\\pm$0.3} & 43.2 \\scriptsize{$\\pm$0.4} \\\\\nGraduated & 25.9 \\scriptsize{$\\pm$0.3} & 43.4 \\scriptsize{$\\pm$0.3} \\\\\nSurprisal-based & 25.7 \\scriptsize{$\\pm$0.2} & 43.1 \\scriptsize{$\\pm$0.4} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream evaluation (3 seeds). Graduated filtering's advantage over binary is $\\leq$0.2pp and non-significant ($p > 0.4$).}\n\\label{tab:filtering}\n\\end{table}\n\nThe dose-response experiment (Table~\\ref{tab:dose}) confirms this null result scales with contamination severity: even at 50\\% synthetic injection, graduated filtering gains at most 0.2pp over binary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Bin.\\ MMLU} & \\textbf{Grad.\\ MMLU} & \\textbf{Bin.\\ HS} & \\textbf{Grad.\\ HS} \\\\\n\\midrule\n10\\% & 25.6 & 25.6 & 43.0 & 43.0 \\\\\n30\\% & 25.5 & 25.6 & 42.8 & 42.9 \\\\\n50\\% & 25.2 & 25.3 & 42.3 & 42.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dose-response: graduated advantage does not scale with contamination level ($\\Delta \\leq 0.2$pp at all doses).}\n\\label{tab:dose}\n\\end{table}\n\n\\subsection{Cross-Model Transfer}\n\nTable~\\ref{tab:transfer} reveals a clean separation: binary detection transfers well across models (average accuracy 81\\%), while depth-specific features do not (average 6-class accuracy 28\\%, retention 40\\% of in-domain performance).\nDepth signal beyond the binary distinction is model-specific, requiring per-model classifier retraining---further limiting the practical utility of depth estimation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Train $\\backslash$ Test} & \\textbf{Qwen} & \\textbf{Pythia} & \\textbf{OLMo} \\\\\n\\midrule\n\\multicolumn{4}{c}{\\emph{6-class accuracy}} \\\\\nQwen  & .37$^*$ & .28 & .26 \\\\\nPythia & .30 & .35$^*$ & .25 \\\\\nOLMo  & .29 & .27 & .33$^*$ \\\\\n\\midrule\n\\multicolumn{4}{c}{\\emph{Binary accuracy (human vs.\\ synthetic)}} \\\\\nQwen  & .93$^*$ & .82 & .79 \\\\\nPythia & .84 & .91$^*$ & .77 \\\\\nOLMo  & .83 & .80 & .88$^*$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-model transfer. Binary detection transfers well (avg.\\ 81\\%); depth estimation does not (avg.\\ 28\\%). $^*$In-domain.}\n\\label{tab:transfer}\n\\end{table}\n\n\\section{Discussion}\n\n\\subsection{Why $K^*=2$? An Information-Theoretic Interpretation}\n\nThe DPI predicts monotonic decay of inter-generational mutual information, but does not specify the \\emph{rate}.\nOur measurements suggest that for 1--7B-scale models, the channel $T_\\mathcal{M}$ is sufficiently lossy that a single pass eliminates the vast majority of distributional features distinguishing $P_0$ from $P_1$: the JSD drops by 17--23$\\times$ from 0v1 to 1v2.\nThe second pass reduces the remaining signal to noise floor.\n\nThe invariance of $K^*$ across model families, scales (1B--7B), and decoding strategies implies that $K^*=2$ is not a property of any individual model but a regime-level characteristic of current-scale language models.\nWhether larger models (70B+) would exhibit higher $K^*$ remains an open question beyond our computational scope.\n\n\\subsection{Implications for Data Governance}\n\nOur results simplify the practical problem of synthetic text curation: \\textbf{the actionable regime is binary}.\nPractitioners should invest in robust first-generation detectors (human vs.\\ synthetic) rather than depth estimators.\nThe three-class signal (human / gen-1 / gen-2+) is the finest granularity supported by current detection technology, and even this distinction provides no measurable downstream benefit over binary filtering.\n\n\\subsection{Limitations}\n\n\\paragraph{Prompt-chain vs.\\ retrain-chain.}\nOur primary experiments use prompt chains (model generates from prior outputs without retraining).\nA retrain-chain validation with Pythia-1.4B (LoRA, rank 16) confirms $K^*=2$ but reveals statistically different feature dynamics (KS test $p=0.03$, JSD correlation $r=0.82$).\nPrompt chains are thus a controlled proxy, not a faithful simulation of real-world recursive contamination.\n\n\\paragraph{Scale.}\nOur 7B probe is limited to 1K documents and depth 0--3 due to GPU budget.\nWe cannot rule out that $K^*>2$ at significantly larger scales (e.g., 70B+).\n\n\\paragraph{Feature degradation ordering.}\nIndividual feature groups (surprisal, diversity, tail-thinning) show model-specific degradation orderings (cross-model Kendall $\\tau = 0.33$), with all groups saturating at depth~2 regardless.\nWe do not claim a universal degradation ordering; this remains a descriptive observation.\n\n\\paragraph{Naturalistic validation.}\nApplying our classifier to Common Crawl yields predicted depth--quality correlations of only $\\rho=-0.15$ to $-0.19$, reflecting domain shift from controlled to in-the-wild data.\n\n\\subsection{Base vs.\\ Instruct Models}\n\nInstruction tuning (RLHF) increases 0v1 detectability (JSD 0.267 vs.\\ 0.210 for Qwen2.5-1.5B Instruct vs.\\ Base) by introducing distinctive stylistic patterns, but does not alter the recursive degradation dynamics: both variants yield $K^*=2$.\nBase models may thus pose a greater challenge for binary detection in practice, while the depth estimation ceiling remains unchanged.\n\n\\section{Conclusion}\n\nWe present the first systematic measurement of the generational discrimination boundary $K^*$ for recursive synthetic text.\nAcross three model families, four decoding strategies, two model scales, and two feature representations, $K^*=2$ emerges as a hard, universal ceiling for 1--7B-parameter language models.\nThis is a direct empirical confirmation of the DPI prediction: the iterated lossy channel of recursive generation destroys inter-generational signal within two passes.\n\nThe practical consequence is stark: depth-aware data curation reduces to binary filtering.\nGraduated filtering, ordinal classification, and depth estimation---despite their theoretical appeal---provide no statistically significant improvement over simply removing all detected synthetic text.\nWe urge the community to focus on robust first-generation detection and to treat depth estimation as a fundamentally limited task at current model scales.\n\n\\section*{Acknowledgments}\nOmitted for review.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\n\\section{Retrain-Chain Ecological Validity}\n\\label{app:retrain}\n\nTo assess ecological validity, we construct a retrain chain using Pythia-1.4B with LoRA fine-tuning (rank=16, $\\alpha$=32) on C4 5K documents through depth 0--4.\nTable~\\ref{tab:retrain} compares prompt-chain and retrain-chain results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Prompt-chain} & \\textbf{Retrain-chain} \\\\\n\\midrule\n$K^*$ & 2 & 2 \\\\\nAUC 0v1 & .991 & .972 \\\\\nAUC 1v2 & .63 & .58 \\\\\nAUC 2v3 & .55 & .53 \\\\\nJSD 0v1 & .231 & .185 \\\\\nJSD 1v2 & .012 & .008 \\\\\nFeature KS-test $p$ & --- & .03 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prompt-chain vs.\\ retrain-chain (Pythia-1.4B). $K^*$ is preserved; absolute signal levels are lower under retraining; feature distributions differ significantly.}\n\\label{tab:retrain}\n\\end{table}\n\n$K^*=2$ is preserved under retraining, but absolute AUC and JSD values are uniformly lower, consistent with retraining accelerating the lossy-channel effect.\nThe significant KS test ($p=0.03$) indicates that while the saturation boundary is consistent, the feature-level dynamics differ, and prompt-chain classifiers should not be directly deployed on retrain-chain data without adaptation.\n\n\\section{Feature Group Degradation Analysis}\n\\label{app:features}\n\nTable~\\ref{tab:feat_group} presents per-feature-group 1v2 AUC by model.\nAll groups saturate at depth~2 regardless of model, but the \\emph{ordering} of degradation (which group loses signal first) is model-specific (cross-model Kendall $\\tau = 0.33$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Surprisal} & \\textbf{Diversity} & \\textbf{Tail} \\\\\n\\midrule\nQwen2.5-1.5B & .63 & .58 & .61 \\\\\nPythia-1.4B & .56 & .60 & .59 \\\\\nOLMo-1B & .58 & .59 & .55 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-feature-group 1v2 AUC. All groups saturate at depth 2; degradation ordering is inconsistent across models.}\n\\label{tab:feat_group}\n\\end{table}\n\n\\section{LLM Zero-Shot Depth Estimation}\n\\label{app:llm}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{5-class Acc.} & \\textbf{MAE} & \\textbf{Binary Acc.} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nGPT-4o & .24 & 1.65 & .78 & .12 \\\\\nClaude 3.5 & .22 & 1.72 & .81 & .10 \\\\\nRandom & .20 & 2.00 & .50 & .00 \\\\\nCORAL (ours) & .37 & 1.08 & .93 & .35 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{LLM zero-shot depth estimation. Frontier LLMs achieve near-random depth accuracy despite reasonable binary detection.}\n\\label{tab:llm_zeroshot}\n\\end{table}\n\n\\section{Naturalistic Validation}\n\\label{app:naturalistic}\n\nApplying our Qwen2.5-1.5B-trained classifier to Common Crawl 2025--2026 snapshots yields:\npredicted 62\\% human, 25\\% gen-1, 13\\% depth-2+.\nCorrelation of predicted depth with AlignScore is $-0.15$; with vocabulary richness, $-0.19$.\nBinary synthetic prediction correlates more strongly with quality ($\\rho=-0.28$), consistent with our main finding that depth signal beyond binary is weak.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "10faee29-85ea-4d8c-9924-d84324c8e34a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contami…",
  "leafUuid": "0d53b3eb-ed1d-48a3-b451-ac3e288d559a",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing generational depth saturation in synthetic text",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Tool call

_source line 20 · 2026-05-12T20:34:59.494Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016DueeSHKBHxMqGCRKy9Tmq`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d53b3eb-ed1d-48a3-b451-ac3e288d559a",
  "isSidechain": false,
  "requestId": "req_011CayKC4XDfX4z3mGzXiNyn",
  "type": "assistant",
  "uuid": "a8758e3e-2a10-4f83-b3b6-816a16cd9be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEC5m8H2KfVSQSQWzd6Uhv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8523,
      "cache_read_input_tokens": 47746,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 47746,
          "cache_creation_input_tokens": 8523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8523
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

_source line 21 · 2026-05-12T20:34:59.637Z_

<details><summary>↩ Tool result · `toolu_016DueeSHKBHxMqGCRKy9Tmq`</summary>

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

! LaTeX Error: File `acl.sty' not found.

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
  "parentUuid": "a8758e3e-2a10-4f83-b3b6-816a16cd9be5",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "4e0ab224-e359-407c-88c0-ae7d9e18efbe",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a8758e3e-2a10-4f83-b3b6-816a16cd9be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T20:35:03.530Z_

<details><summary>Logged reasoning block</summary>

```text
Need to check what style files are available and adjust accordingly. Let me find available LaTeX packages or use a basic article class.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e0ab224-e359-407c-88c0-ae7d9e18efbe",
  "isSidechain": false,
  "requestId": "req_011CayKCJwt7D21paVj44y3s",
  "type": "assistant",
  "uuid": "37c9561f-a090-482d-a0e4-d27fe6a487ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WgmZHfnHgxUdoyrScEpDh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 56269,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 56269,
          "cache_creation_input_tokens": 424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 424
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

_source line 23 · 2026-05-12T20:35:04.729Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CaoNzvbEumtXfcVdqfkNiE`</summary>

```json
{
  "command": "find /usr/share/texlive -name \"acl*\" 2>/dev/null; find /usr/share/texlive -name \"naaclhlt*\" 2>/dev/null; find /usr/share/texlive -name \"emnlp*\" 2>/dev/null",
  "description": "Search for ACL style files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37c9561f-a090-482d-a0e4-d27fe6a487ac",
  "isSidechain": false,
  "requestId": "req_011CayKCJwt7D21paVj44y3s",
  "type": "assistant",
  "uuid": "51b751c9-bf62-4bdc-bdda-957c4d54f3c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WgmZHfnHgxUdoyrScEpDh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 56269,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 56269,
          "cache_creation_input_tokens": 424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 424
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

_source line 24 · 2026-05-12T20:35:05.017Z_

<details><summary>↩ Tool result · `toolu_01CaoNzvbEumtXfcVdqfkNiE`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51b751c9-bf62-4bdc-bdda-957c4d54f3c2",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "05a236dc-3f27-4b51-9fc8-03b02e9d4bf6",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "51b751c9-bf62-4bdc-bdda-957c4d54f3c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T20:35:08.032Z_

No ACL style available. I'll replace it with a standard article class setup that mimics the conference format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05a236dc-3f27-4b51-9fc8-03b02e9d4bf6",
  "isSidechain": false,
  "requestId": "req_011CayKCi7QhXiW2P7b1TFid",
  "type": "assistant",
  "uuid": "cbda0644-ca18-4053-bec2-a79b5e6248fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gBA5RWFNegAQ6pLtq5vNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 56693,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 56693,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 26 · 2026-05-12T20:35:08.640Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T23JCQBqjgJ1bFz8A4Zj2i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbda0644-ca18-4053-bec2-a79b5e6248fc",
  "isSidechain": false,
  "requestId": "req_011CayKCi7QhXiW2P7b1TFid",
  "type": "assistant",
  "uuid": "c88adb98-d51f-4535-960b-e48411b67148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gBA5RWFNegAQ6pLtq5vNy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 205,
      "cache_read_input_tokens": 56693,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 56693,
          "cache_creation_input_tokens": 205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 205
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

_source line 27 · 2026-05-12T20:35:08.645Z_

<details><summary>↩ Tool result · `toolu_01T23JCQBqjgJ1bFz8A4Zj2i`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c88adb98-d51f-4535-960b-e48411b67148",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "ef6f5c7a-e9f9-4731-af9f-d4b7bad42244",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 452
    }
  },
  "sourceToolAssistantUUID": "c88adb98-d51f-4535-960b-e48411b67148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T20:35:14.238Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0113zYaxKd8JPGX9yaRW9dEg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6f5c7a-e9f9-4731-af9f-d4b7bad42244",
  "isSidechain": false,
  "requestId": "req_011CayKCzCJ8nXqrnJ5XEFkf",
  "type": "assistant",
  "uuid": "da0561b7-f96a-493f-bb6e-5d27f9570be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCs3whAQqsFLmHfQEZyNWf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 56898,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 389,
          "cache_read_input_tokens": 56898,
          "cache_creation_input_tokens": 272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 272
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

_source line 29 · 2026-05-12T20:35:14.265Z_

<details><summary>↩ Tool result · `toolu_0113zYaxKd8JPGX9yaRW9dEg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da0561b7-f96a-493f-bb6e-5d27f9570be1",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "cd132773-8e7d-456f-b68e-611c2200ab6a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
          " ",
          " \\title{The Depth~2 Ceiling: Generational Signals in Recursive Synthetic Text\\\\Collapse Beyond First-Generation Detection}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "da0561b7-f96a-493f-bb6e-5d27f9570be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-12T20:35:14.271Z_

```json
{
  "parentUuid": "cd132773-8e7d-456f-b68e-611c2200ab6a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "880503dd-87fa-43c8-a80c-c029bb7a411d",
  "timestamp": "2026-05-12T20:35:14.271Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-12T20:35:29.917Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01YZB5sJGYBo18jBgMzQAEm7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using random perturbations.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLMs} with {B}inoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{cao2020rank}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with a proportional odds model.\n\\newblock \\emph{Pattern Recognition}, 108:107616, 2020.\n\n\\bibitem[Feng et~al.(2024)]{feng2024towards}\nJifan Feng, et~al.\n\\newblock Towards verifiable text generation with evolving memory.\n\\newblock \\emph{arXiv preprint arXiv:2312.09075}, 2024.\n\n\\bibitem[Yi et~al.(2024)]{yi2024on}\nJunjie Yi, et~al.\n\\newblock On the detectability of {LLM}-generated text.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880503dd-87fa-43c8-a80c-c029bb7a411d",
  "isSidechain": false,
  "requestId": "req_011CayKDPYjSkq79rBoZKdB5",
  "type": "assistant",
  "uuid": "19c6b42a-c89a-4576-8f11-e6209d3f6aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ifwJDLbenvd8u383KckDH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 57170,
      "output_tokens": 742,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 742,
          "cache_read_input_tokens": 57170,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 579
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

_source line 32 · 2026-05-12T20:35:29.933Z_

<details><summary>↩ Tool result · `toolu_01YZB5sJGYBo18jBgMzQAEm7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19c6b42a-c89a-4576-8f11-e6209d3f6aa0",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "a3a2191d-ba11-4ff2-b4aa-de7ff75e401c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}\nIlia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nEric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D Manning, and Chelsea Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using random perturbations.\n\\newblock In \\emph{Proceedings of ICML}, 2023.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nAbhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.\n\\newblock Spotting {LLMs} with {B}inoculars: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{Proceedings of ICML}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{cao2020rank}\nWenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with a proportional odds model.\n\\newblock \\emph{Pattern Recognition}, 108:107616, 2020.\n\n\\bibitem[Feng et~al.(2024)]{feng2024towards}\nJifan Feng, et~al.\n\\newblock Towards verifiable text generation with evolving memory.\n\\newblock \\emph{arXiv preprint arXiv:2312.09075}, 2024.\n\n\\bibitem[Yi et~al.(2024)]{yi2024on}\nJunjie Yi, et~al.\n\\newblock On the detectability of {LLM}-generated text.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 366,
        "oldLines": 9,
        "newStart": 366,
        "newLines": 41,
        "lines": [
          " \\section*{Acknowledgments}",
          " Omitted for review.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          "+\\begin{thebibliography}{10}",
          " ",
          "+\\bibitem[Shumailov et~al.(2024)]{shumailov2024ai}",
          "+Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, and Yarin Gal.",
          "+\\newblock {AI} models collapse when trained on recursively generated data.",
          "+\\newblock \\emph{Nature}, 631:755--759, 2024.",
          "+",
          "+\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}",
          "+Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher~D Manning, and Chelsea Finn.",
          "+\\newblock {DetectGPT}: Zero-shot machine-generated text detection using random perturbations.",
          "+\\newblock In \\emph{Proceedings of ICML}, 2023.",
          "+",
          "+\\bibitem[Hans et~al.(2024)]{hans2024binoculars}",
          "+Abhimanyu Hans, Avi Schwarzschild, Valeriia Cherepanova, Hamid Kazemi, Aniruddha Saha, Micah Goldblum, Jonas Geiping, and Tom Goldstein.",
          "+\\newblock Spotting {LLMs} with {B}inoculars: Zero-shot detection of machine-generated text.",
          "+\\newblock In \\emph{Proceedings of ICML}, 2024.",
          "+",
          "+\\bibitem[Cao et~al.(2020)]{cao2020rank}",
          "+Wenzhi Cao, Vahid Mirjalili, and Sebastian Raschka.",
          "+\\newblock Rank consistent ordinal regression for neural networks with a proportional odds model.",
          "+\\newblock \\emph{Pattern Recognition}, 108:107616, 2020.",
          "+",
          "+\\bibitem[Feng et~al.(2024)]{feng2024towards}",
          "+Jifan Feng, et~al.",
          "+\\newblock Towards verifiable text generation with evolving memory.",
          "+\\newblock \\emph{arXiv preprint arXiv:2312.09075}, 2024.",
          "+",
          "+\\bibitem[Yi et~al.(2024)]{yi2024on}",
          "+Junjie Yi, et~al.",
          "+\\newblock On the detectability of {LLM}-generated text.",
          "+\\newblock \\emph{arXiv preprint}, 2024.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\appendix",
          " ",
          " \\section{Retrain-Chain Ecological Validity}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "19c6b42a-c89a-4576-8f11-e6209d3f6aa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-12T20:35:33.307Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KTUVrEu2QnkQacoUREpjwr`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3a2191d-ba11-4ff2-b4aa-de7ff75e401c",
  "isSidechain": false,
  "requestId": "req_011CayKEYhRgB1hna2XKRDEF",
  "type": "assistant",
  "uuid": "aaa2e3a6-f9c6-4bf5-99d1-d0026fb45005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEJiqkygakinEZ9XKwP33i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 57749,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 57749,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 34 · 2026-05-12T20:35:33.794Z_

<details><summary>↩ Tool result · `toolu_01KTUVrEu2QnkQacoUREpjwr`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 170920 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaa2e3a6-f9c6-4bf5-99d1-d0026fb45005",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "ccb06775-9599-446b-aab1-184523986998",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 170920 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "aaa2e3a6-f9c6-4bf5-99d1-d0026fb45005",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T20:35:37.569Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0158JHQBAuMNunZZLTsZ3Rc8`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccb06775-9599-446b-aab1-184523986998",
  "isSidechain": false,
  "requestId": "req_011CayKEq9do3zdrQZiPCp79",
  "type": "assistant",
  "uuid": "0b07fa09-f50e-42ae-80bd-56586ce07daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nhsPyoEa3B7yLCzXwkN3z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 58577,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 665,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 58577,
          "cache_creation_input_tokens": 665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 665
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

_source line 36 · 2026-05-12T20:35:38.036Z_

<details><summary>↩ Tool result · `toolu_0158JHQBAuMNunZZLTsZ3Rc8`</summary>

```text
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 175310 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b07fa09-f50e-42ae-80bd-56586ce07daa",
  "isSidechain": false,
  "promptId": "18d73d3f-de4c-43f8-9b75-ca3fc9ae70da",
  "type": "user",
  "uuid": "5399148c-5a97-420b-9064-217179fa5bf3",
  "toolUseResult": {
    "stdout": "ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 175310 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b07fa09-f50e-42ae-80bd-56586ce07daa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contami…",
  "leafUuid": "5399148c-5a97-420b-9064-217179fa5bf3",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing generational depth saturation in synthetic text",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Assistant

_source line 39 · 2026-05-12T20:35:46.258Z_

编译成功，9 页 PDF 已生成。

输出文件：`.../dream_20260512T200328/worst/paper.pdf`

论文以 negative-result / empirical analysis 框架展开，核心发现：$K^*=2$ 是 1–7B 模型的 hard, universal ceiling——跨 3 个模型族、4 种解码策略、base/instruct、1B–7B scale 不变。Graduated filtering 相对 binary 无统计显著优势（$\Delta \leq 0.2$pp, $p > 0.4$）。C2（degradation ordering）降级至 appendix，C3 重构为 negative characterization。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5399148c-5a97-420b-9064-217179fa5bf3",
  "isSidechain": false,
  "requestId": "req_011CayKF9BM8A597Sqowkuh1",
  "type": "assistant",
  "uuid": "45bca75c-38a7-440a-b86a-4761b3c2e71e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260512T200328/worst",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TKvzvNXykJ2BvW2hvSbFC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 59242,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 235,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 59242,
          "cache_creation_input_tokens": 235,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 235
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T200328 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contami…",
  "leafUuid": "45bca75c-38a7-440a-b86a-4761b3c2e71e",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing generational depth saturation in synthetic text",
  "sessionId": "858b0d51-d42d-4da5-bcf3-851792c21102"
}
```

---
