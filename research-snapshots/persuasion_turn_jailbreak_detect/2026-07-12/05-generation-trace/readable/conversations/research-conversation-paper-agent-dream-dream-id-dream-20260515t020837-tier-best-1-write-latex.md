# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/5876900b-bca3-4056-abfb-7d44763c8c40.jsonl`
- **Structured JSON:** [`e3b61cecda7581d9bc11.json`](../../sessions/e3/e3b61cecda7581d9bc11.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:32:39.163Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:32:39.163Z",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/experiment_data.json`（先 Read 此文件）\n- Venue：Insights from Negative Results in NLP @ EMNLP 2026\n- Narrative guidance：原始 framing 完全成立。三个核心 finding 在补充实验中逐一获得独立多 seed 证据： (1) 方差梯度 Vanilla<Random<TaxEI 是 robust ordering，在每个 seed 和 dose 水平均成立； (2) 阈值-平台是 error injection 的通用属性——两种注入方法在 10→25% 同步崩溃 12.8pp，跨 seed 偏差 ≤2.2pp； (3) ~6.4pp taxonomy penalty 是 systematic additive bias，跨 3 seed × 3 dose = 9 个独立观测点保持稳定（SD ≈ 0.4pp）。 训练动态分析提供 mechanistic explanation——注入样本的梯度方向与 clean 样本弱对齐（cosine ~0.3）， 系统性拉高 clean 样本 loss 约 14%。定性分析显示 TaxEI 特有的 \"taxonomy-operator 回放\" 失败模式， 区别于随机噪声。WebShop 第二环境部分复现方差梯度和阈值效应，进一步支撑 task-structural boundary condition。 论文可做 strong negative claim + actionable boundary condition guideline，标题级 claim 不变。 Pooled permutation test TaxEI vs Vanilla 达 p=0.031，paired t TaxEI vs Random 达 p=0.024。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T02:32:39.166Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:32:39.166Z",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-15T02:32:39.182Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/experiment_data.json`（先 Read 此文件）
- Venue：Insights from Negative Results in NLP @ EMNLP 2026
- Narrative guidance：原始 framing 完全成立。三个核心 finding 在补充实验中逐一获得独立多 seed 证据： (1) 方差梯度 Vanilla<Random<TaxEI 是 robust ordering，在每个 seed 和 dose 水平均成立； (2) 阈值-平台是 error injection 的通用属性——两种注入方法在 10→25% 同步崩溃 12.8pp，跨 seed 偏差 ≤2.2pp； (3) ~6.4pp taxonomy penalty 是 systematic additive bias，跨 3 seed × 3 dose = 9 个独立观测点保持稳定（SD ≈ 0.4pp）。 训练动态分析提供 mechanistic explanation——注入样本的梯度方向与 clean 样本弱对齐（cosine ~0.3）， 系统性拉高 clean 样本 loss 约 14%。定性分析显示 TaxEI 特有的 "taxonomy-operator 回放" 失败模式， 区别于随机噪声。WebShop 第二环境部分复现方差梯度和阈值效应，进一步支撑 task-structural boundary condition。 论文可做 strong negative claim + actionable boundary condition guideline，标题级 claim 不变。 Pooled permutation test TaxEI vs Vanilla 达 p=0.031，paired t TaxEI vs Random 达 p=0.024。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "fac0f9eb-e258-4b6c-9d06-a352af9b43f3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:32:39.182Z_

```json
{
  "parentUuid": "fac0f9eb-e258-4b6c-9d06-a352af9b43f3",
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
  "uuid": "226fc86b-e106-440a-bbc6-154b0dda7867",
  "timestamp": "2026-05-15T02:32:39.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:32:39.182Z_

```json
{
  "parentUuid": "226fc86b-e106-440a-bbc6-154b0dda7867",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "48d3b5e9-fd63-4dd5-9441-006c82ffa879",
  "timestamp": "2026-05-15T02:32:39.182Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
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
  "aiTitle": "Error injection robustness in NLP taxonomy tasks",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Assistant

_source line 7 · 2026-05-15T02:32:41.922Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48d3b5e9-fd63-4dd5-9441-006c82ffa879",
  "isSidechain": false,
  "requestId": "req_011Cb3a628h3MVKNTXAwwJSE",
  "type": "assistant",
  "uuid": "6a5c5928-3f6d-4017-8b2b-acbfb34c6570",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X32iksMriYk5rWvFRzBwVc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11479,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11479
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

_source line 8 · 2026-05-15T02:32:42.414Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C9hYSj4tYz1vpqWtrhMaRs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a5c5928-3f6d-4017-8b2b-acbfb34c6570",
  "isSidechain": false,
  "requestId": "req_011Cb3a628h3MVKNTXAwwJSE",
  "type": "assistant",
  "uuid": "cc1c0e27-a4dc-41fa-8f7e-880f4e7d2220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X32iksMriYk5rWvFRzBwVc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11479,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11479
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

_source line 9 · 2026-05-15T02:32:42.697Z_

<details><summary>↩ Tool result · `toolu_01C9hYSj4tYz1vpqWtrhMaRs`</summary>

```text
1	[
2	  {
3	    "name": "Random Dose-Response Curve Completion",
4	    "description": "Random injection 的 10%/25%/50% 剂量-响应曲线（固定 4,358 总样本，seed=42）， 与 TaxEI 剂量-响应并行对比，验证共享阈值-平台效应和恒定 taxonomy penalty。\n",
5	    "results": {
6	      "random_inject10_pct": 68.1,
7	      "random_inject25_pct": 55.3,
8	      "random_inject50_pct": 57.4,
9	      "random_10to25_drop_pp": 12.8,
10	      "taxei_10to25_drop_pp": 12.8,
11	      "shared_drop_difference_pp": 0.0,
12	      "taxonomy_penalty_10_pp": 6.4,
13	      "taxonomy_penalty_25_pp": 6.4,
14	      "taxonomy_penalty_50_pp": 6.3,
15	      "taxonomy_penalty_mean_pp": 6.37,
16	      "taxonomy_penalty_sd_pp": 0.06
17	    },
18	    "tables": [
19	      {
20	        "title": "Combined Dose-Response Table (seed=42, fixed 4,358 total)",
21	        "content": "| Dose  | Vanilla | TaxEI  | Random | Δ(R−T) | TaxEI Δ(vs 10%) | Random Δ(vs 10%) |\n|-------|---------|--------|--------|--------|------------------|------------------|\n| 0%    | 61.7%   | 61.7%  | 61.7%  | 0.0    | —                | —                |\n| 10%   | —       | 61.7%  | 68.1%  | +6.4   | 0.0              | 0.0              |\n| 25%   | —       | 48.9%  | 55.3%  | +6.4   | −12.8            | −12.8            |\n| 50%   | —       | 51.1%  | 57.4%  | +6.3   | −10.6            | −10.7            |\n"
22	      }
23	    ],
24	    "figures": [],
25	    "analysis": "剂量-响应曲线揭示两个可分离的独立效应：(1) 共享的信噪比阈值——两种注入方法在同一临界区间 [10%, 25%] 发生等幅崩溃，证明这是 error injection 的 fundamental property 而非 taxonomy 特异性； (2) 恒定的 taxonomy penalty——TaxEI 在每个 dose 点均落后 Random 恰好 ~6.4pp，说明 taxonomy label 引入的是正交于注入剂量的 additive bias。Random 10% 的 +6.4pp 增益是意外发现，提供了重要的正面 对照：说明少量未标记噪声注入本身可以是有效的 data augmentation，但 taxonomy label 消除了这一好处。\n\n\nRandom 10% = 68.1% 高于 vanilla 6.4pp，反映纯数据增强效应——无标签的噪声注入在低剂量下增加 训练分布多样性，实质上是合法的 data augmentation。TaxEI 10% = 61.7% 无此增益，说明 taxonomy label 抵消了增强效应，将 +6.4pp augmentation bonus 精确归零。10→25% 两种方法同步崩溃 12.8pp （Random 68.1→55.3, TaxEI 61.7→48.9），证明阈值效应是 error injection 的通用属性：当注入比例 超过 ~15-20%，clean 梯度信号被稀释至临界点以下，模型无法维持正确的 action distribution。 50% 处两者均回升 ~2pp（平台效应），因为极高注入比例下 clean 和 injected 样本的梯度已充分混合， 进一步增加注入不再额外恶化。6.4/6.4/6.3pp 的恒定 taxonomy penalty 在三个独立 dose 点保持 一致（SD=0.06），精确对应 3 个 ALFWorld 任务的分辨率（3/47=6.38pp），强烈支持 taxonomy label 引入的是与剂量无关的 systematic bias——结构化错误模式教会模型特定的错误行为，而非仅增加噪声。\n"
26	  },
27	  {
28	    "name": "Multi-Seed Dose-Response Replication",
29	    "description": "在 seed=0 和 seed=123 上重复完整的剂量-响应实验（10%/25%/50%，固定 4,358 总样本）， 验证阈值-平台效应和 taxonomy penalty 的跨 seed 稳定性。共 12 次训练 + 12 次 eval。\n",
30	    "results": {
31	      "seed0_taxei_inject10_pct": 68.1,
32	      "seed0_taxei_inject25_pct": 55.3,
33	      "seed0_taxei_inject50_pct": 57.4,
34	      "seed0_random_inject10_pct": 74.5,
35	      "seed0_random_inject25_pct": 61.7,
36	      "seed0_random_inject50_pct": 63.8,
37	      "seed0_shared_10to25_drop_pp": 12.8,
38	      "seed0_taxonomy_penalty_mean_pp": 6.4,
39	      "seed123_taxei_inject10_pct": 63.8,
40	      "seed123_taxei_inject25_pct": 53.2,
41	      "seed123_taxei_inject50_pct": 53.2,
42	      "seed123_random_inject10_pct": 70.2,
43	      "seed123_random_inject25_pct": 59.6,
44	      "seed123_random_inject50_pct": 59.6,
45	      "seed123_shared_10to25_drop_pp": 10.6,
46	      "seed123_taxonomy_penalty_mean_pp": 6.4,
47	      "all_seeds_10to25_drop_mean_pp": 12.1,
48	      "all_seeds_10to25_drop_sd_pp": 1.1,
49	      "all_seeds_taxonomy_penalty_mean_pp": 6.37,
50	      "all_seeds_taxonomy_penalty_sd_pp": 0.4,
51	      "dose_response_cross_seed_agreement": 1.0
52	    },
53	    "tables": [
54	      {
55	        "title": "Multi-Seed Dose-Response: TaxEI (fixed 4,358 total)",
56	        "content": "| Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |\n|------|---------|--------|----------|--------|-------|\n| 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |\n| 10%  | 61.7%   | 68.1%  | 63.8%    | 64.5%  | 3.3pp |\n| 25%  | 48.9%   | 55.3%  | 53.2%    | 52.5%  | 3.3pp |\n| 50%  | 51.1%   | 57.4%  | 53.2%    | 53.9%  | 3.2pp |\n"
57	      },
58	      {
59	        "title": "Multi-Seed Dose-Response: Random (fixed 4,358 total)",
60	        "content": "| Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |\n|------|---------|--------|----------|--------|-------|\n| 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |\n| 10%  | 68.1%   | 74.5%  | 70.2%    | 70.9%  | 3.3pp |\n| 25%  | 55.3%   | 61.7%  | 59.6%    | 58.9%  | 3.3pp |\n| 50%  | 57.4%   | 63.8%  | 59.6%    | 60.3%  | 3.3pp |\n"
61	      },
62	      {
63	        "title": "Taxonomy Penalty Across Seeds × Doses",
64	        "content": "| Dose | Seed 42 | Seed 0 | Seed 123 | Mean  |\n|------|---------|--------|----------|-------|\n| 10%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |\n| 25%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |\n| 50%  | 6.3pp   | 6.4pp  | 6.4pp    | 6.4pp |\n"
65	      },
66	      {
67	        "title": "Shared 10→25% Drop Across Seeds",
68	        "content": "| Seed | TaxEI Drop | Random Drop | Difference |\n|------|------------|-------------|------------|\n| 42   | 12.8pp     | 12.8pp      | 0.0pp      |\n| 0    | 12.8pp     | 12.8pp      | 0.0pp      |\n| 123  | 10.6pp     | 10.6pp      | 0.0pp      |\n| Mean | 12.1pp     | 12.1pp      | 0.0pp      |\n"
69	      }
70	    ],
71	    "figures": [],
72	    "analysis": "多 seed 剂量-响应是 best 档的决定性实验。9 个独立的 taxonomy penalty 观测点（3 seed × 3 dose） 形成的 SD ≈ 0.4pp 远低于 1.5pp 阈值，为 systematic additive bias 假说提供了近乎完美的证据。 共享阈值-平台在所有 seed 复现（10→25% drop 均 ≥10pp），最大跨 seed 偏差 2.2pp（seed 123 的 10.6pp vs seed 42 的 12.8pp），落在 ≤3pp 预算内。值得注意的是，每个 seed 内 TaxEI 和 Random 的 drop 幅度精确匹配（差异 ≤0.1pp），再次证明阈值效应是数据组成而非方法特异性的结果。 这些结果使论文可以做出 definitive statement：error injection 的剂量-响应是 task-structural 属性，taxonomy label 只在此基础上叠加恒定惩罚。\n\n\n阈值-平台效应的物理机制是数据组成决定的信噪比边界，与随机初始化无关：当 clean 样本占比从 90%（dose=10%）降至 75%（dose=25%）时，clean 梯度信号不再足以维持正确的 action distribution。 这一边界由数据比例而非 seed 决定，因此跨 seed 高度稳定。Seed 42 的 12.8pp 在 seed 0 处精确 复现（12.8pp），seed 123 略低（10.6pp），反映 seed 123 的 vanilla baseline 较低（66.0%）， 留给崩溃的绝对空间较小——但所有 seed 均在 [10.0, 15.0]pp 范围内。Taxonomy penalty 的跨 seed 稳定性（SD ≈ 0.4pp）更进一步确认这是一个由 label 结构决定的 systematic bias：taxonomy label 在每个 seed 的每个 dose 点均将 3 个额外任务从成功翻转为失败，对应于 47 任务中固定的一组 对 taxonomy-specific 错误模式敏感的任务。Seed 0 的 Random 10% = 74.5% 高于其他 seed， 但仍符合 data augmentation 效应——seed 0 的 vanilla baseline 已较高（68.1%）， augmentation bonus 叠加后接近 ALFWorld 的性能天花板。\n"
73	  },
74	  {
75	    "name": "Training Dynamics Analysis",
76	    "description": "从 v4 seed=42 的 training log 中提取逐 step loss 曲线，分离 clean 和 injected 样本的 loss， 分析注入样本对 clean 学习信号的污染程度。不需要新训练。\n",
77	    "results": {
78	      "vanilla_clean_loss_final": 0.29,
79	      "taxei_overall_loss_final": 0.355,
80	      "taxei_clean_loss_final": 0.338,
81	      "taxei_injected_loss_final": 0.482,
82	      "random_overall_loss_final": 0.355,
83	      "random_clean_loss_final": 0.318,
84	      "random_injected_loss_final": 0.445,
85	      "clean_loss_inflation_taxei_pct": 16.6,
86	      "clean_loss_inflation_random_pct": 9.7,
87	      "injected_to_clean_loss_ratio_taxei": 1.43,
88	      "injected_to_clean_loss_ratio_random": 1.4,
89	      "loss_divergence_onset_step": 500,
90	      "gradient_cosine_clean_vs_injected_taxei": 0.28,
91	      "gradient_cosine_clean_vs_injected_random": 0.35
92	    },
93	    "tables": [
94	      {
95	        "title": "Loss Decomposition (seed=42, final epoch)",
96	        "content": "| Method  | Overall | Clean  | Injected | Clean Inflation | Inj/Clean Ratio |\n|---------|---------|--------|----------|-----------------|-----------------|\n| Vanilla | 0.290   | 0.290  | —        | baseline        | —               |\n| TaxEI   | 0.355   | 0.338  | 0.482    | +16.6%          | 1.43×           |\n| Random  | 0.355   | 0.318  | 0.445    | +9.7%           | 1.40×           |\n"
97	      },
98	      {
99	        "title": "Gradient Alignment Metrics",
100	        "content": "| Metric                         | TaxEI | Random |\n|--------------------------------|-------|--------|\n| Cosine(clean, injected)        | 0.28  | 0.35   |\n| Clean loss inflation vs Vanilla| 16.6% | 9.7%  |\n| Injected loss convergence      | No    | Partial|\n"
101	      }
102	    ],
103	    "figures": [],
104	    "analysis": "训练动态分析将方差梯度的统计现象转化为可解释的梯度力学：注入样本在权重空间中施加与 clean 样本不一致的梯度力，TaxEI 因 taxonomy 标签产生 structured gradient interference（cosine 0.28）， Random 因随机性产生 diffuse interference（cosine 0.35）。Clean loss inflation 的 TaxEI > Random 排序（16.6% vs 9.7%）完美对应 final performance 的 Vanilla > Random > TaxEI 排序，提供了 从训练 loss 到 eval performance 的因果链。这一 mechanistic explanation 是论文从 \"观察到负面结果\" 升级为 \"解释负面结果\" 的关键——reviewer 可能质疑统计功效，但 loss decomposition 提供了 independent 的 process-level 证据。injected 样本 loss 不完全收敛的现象进一步说明模型未能 有效学习错误模式——与 PALADIN 在 tool-use 中 recovery trajectories 可以被学习形成对比。\n\n\nVanilla clean loss 收敛至 ~0.29（registry: v4-vanilla-seed0 final_loss=0.297），这是无干扰 baseline。TaxEI 的 overall loss = 0.355 是 clean 和 injected 样本的加权混合——分离后 clean 部分 ~0.338 高于 vanilla 16.6%，直接量化了注入样本对 clean 学习信号的污染。这一 \"corruption signal\" 是 finding 3（方差梯度）的 mechanistic explanation：注入样本的梯度方向与 clean 样本 弱对齐（cosine ~0.28），在反向传播中将模型权重推离 clean optimal，导致 clean 样本 loss 系统性 升高。Random injection 的 clean loss inflation（9.7%）低于 TaxEI（16.6%），因为随机错误的 梯度方向更加分散（cosine ~0.35，paradoxically higher），不会形成 coherent 的 \"拉力方向\"—— 相当于在权重空间中添加各向同性噪声，而 TaxEI 的 taxonomy 标签创建了 structured 的错误梯度 方向，对 clean learning 造成更大的 systematic interference。Loss 分歧在 step ~500（epoch 1 后期）开始显现，对应于模型开始记忆训练样本而非仅学习通用模式的阶段——此后 injected 样本的 错误模式开始与 clean 模式竞争权重空间。\n"
105	  },
106	  {
107	    "name": "Qualitative Failure Analysis",
108	    "description": "手动分析 20+ TaxEI 失败案例，区分 \"taxonomy-specific wrong learning\"（模型学到了特定的 错误行为）和 \"random noise\"（模型只是表现更不稳定），为 Claim 1 和 Claim 6 提供定性证据。\n",
109	    "results": {
110	      "total_cases_analyzed": 24,
111	      "taxei_fail_vanilla_succeed": 8,
112	      "both_fail": 10,
113	      "taxei_succeed_vanilla_fail": 6,
114	      "failure_taxonomy": {
115	        "operator_replay": 6,
116	        "action_sequence_disorder": 5,
117	        "premature_termination": 4,
118	        "wrong_object_selection": 4,
119	        "identical_to_vanilla_failure": 5
120	      },
121	      "operator_replay_pct": 25.0,
122	      "wrong_learning_pct": 62.5,
123	      "noise_pct": 20.8,
124	      "ambiguous_pct": 16.7
125	    },
126	    "tables": [
127	      {
128	        "title": "Failure Mode Taxonomy (24 cases)",
129	        "content": "| Failure Mode             | Count | Pct   | TaxEI-Specific? |\n|--------------------------|-------|-------|-----------------|\n| Operator replay (P2/C1)  | 6     | 25.0% | Yes             |\n| Action sequence disorder | 5     | 20.8% | Partially       |\n| Premature termination    | 4     | 16.7% | Partially       |\n| Wrong object selection   | 4     | 16.7% | No              |\n| Same as vanilla failure  | 5     | 20.8% | No              |\n"
130	      },
131	      {
132	        "title": "Failure Attribution Summary",
133	        "content": "| Category       | Count | Pct   | Interpretation                          |\n|----------------|-------|-------|-----------------------------------------|\n| Wrong learning | 15    | 62.5% | Model internalized error patterns       |\n| Noise          | 5     | 20.8% | Indistinguishable from baseline noise   |\n| Ambiguous      | 4     | 16.7% | Could be either                         |\n"
134	      }
135	    ],
136	    "figures": [],
137	    "analysis": "定性分析将统计现象 \"taxonomy penalty\" 具象化为可观察的行为模式：TaxEI 模型在 clean eval 中 \"回放\" 训练数据中的 taxonomy 错误，特别是 P2 (sub_goal_deletion) 和 C1 (context_truncation) 两种 operator 的特征最明显。这解释了为何 taxonomy penalty 与 dose 无关——只要训练数据中存在 taxonomy-标记的错误样本，模型就会 internalize 特定的错误策略，无论这些样本占比多少。 与之对比，Random injection 的失败模式不呈现 operator-specific 聚类，支持其 gradient 干扰是 diffuse 而非 structured 的解释。这一发现为论文提供了最具说服力的 \"为什么 taxonomy labels 有害\" 的直觉解释，适合放在 Analysis 部分作为 bridge between statistics and mechanism。\n\n\n定性分析揭示 TaxEI 失败中最具诊断意义的模式是 \"operator replay\"——模型在 clean 任务中 生成与训练数据中某种 taxonomy operator 一致的错误行为。例如，模型在 pick_clean_then_place 任务中跳过 clean 步骤（对应 P2 sub_goal_deletion 的训练模式），或在需要仔细观察环境时 截断上下文信息（对应 C1 context_truncation 的训练模式）。这些 operator replay 案例（6/24, 25%）是 TaxEI 特有的——Random 和 Vanilla 的失败案例中不存在与特定 taxonomy operator 匹配的模式。另有 9/24 案例（37.5%）表现为非 operator-specific 但系统性的错误行为（action disorder, premature termination），合计 \"wrong learning\" 占 62.5%。仅 5/24（20.8%） 的失败模式与 Vanilla 失败完全一致（baseline noise）。这一分布支持 \"TaxEI 教会模型特定的 错误行为\" 假说而非 \"TaxEI 仅增加随机噪声\" 假说，与 training dynamics 中 TaxEI 的 structured gradient interference（cosine 0.28 < Random 0.35）一致。\n"
138	  },
139	  {
140	    "name": "Second Environment Validation (WebShop)",
141	    "description": "在 WebShop 环境中复现 Vanilla/TaxEI/Random 三组实验（2-seed），验证方差梯度和 阈值效应是否泛化到 ALFWorld 以外的 embodied planning 领域。需要适配 error taxonomy、 采集轨迹、训练和评估。\n",
142	    "results": {
143	      "webshop_vanilla_mean_pct": 58.5,
144	      "webshop_vanilla_sd_pp": 2.8,
145	      "webshop_taxei_mean_pct": 51.2,
146	      "webshop_taxei_sd_pp": 7.4,
147	      "webshop_random_mean_pct": 55.8,
148	      "webshop_random_sd_pp": 5.9,
149	      "variance_gradient_holds": true,
150	      "variance_ratio_taxei_vs_vanilla": 2.6,
151	      "taxonomy_penalty_pp": 4.6,
152	      "webshop_dose_10_taxei_pct": 57.3,
153	      "webshop_dose_25_taxei_pct": 47.8,
154	      "webshop_dose_10to25_drop_pp": 9.5,
155	      "engineering_days": 4
156	    },
157	    "tables": [
158	      {
159	        "title": "WebShop 2-Seed Results",
160	        "content": "| Method  | Mean   | SD    | vs Vanilla |\n|---------|--------|-------|------------|\n| Vanilla | 58.5%  | 2.8pp | —          |\n| TaxEI   | 51.2%  | 7.4pp | −7.3pp     |\n| Random  | 55.8%  | 5.9pp | −2.7pp     |\n"
161	      },
162	      {
163	        "title": "Cross-Environment Pattern Comparison",
164	        "content": "| Pattern                | ALFWorld      | WebShop       | Consistent? |\n|------------------------|---------------|---------------|-------------|\n| Variance gradient      | 3.3<7.0<8.6   | 2.8<5.9<7.4   | ✓           |\n| TaxEI vs Vanilla       | −8.6pp (NS)   | −7.3pp        | ✓           |\n| Taxonomy penalty       | 6.4pp         | 4.6pp         | ✓ (weaker)  |\n| 10→25% drop            | 12.8pp        | 9.5pp         | ✓ (weaker)  |\n"
165	      }
166	    ],
167	    "figures": [],
168	    "analysis": "WebShop 复现了方差梯度和 taxonomy penalty 的方向，但 magnitude 较小——与 WebShop 更密集的 reward signal 和更结构化的 action space 一致。这提供了一个重要的 dose-response in task structure：随着任务从 \"完全 open-ended planning\" (ALFWorld) 向 \"semi-structured interaction\" (WebShop) 移动，error injection 的负面效应减弱但仍存在。这一 gradient 支持论文的核心论点： task structure 是决定 error injection 效果的 primary factor，而非二元的 \"works/doesn't work\"。 与 EEF 的对比（EEF 在 WebShop 成功但用了相反的 injection direction）进一步细化了 boundary condition：即使在同一环境中，\"注入错误\" 和 \"从错误中提取正确\" 的效果完全不同。\n\n\nWebShop 与 ALFWorld 共享 embodied planning 的关键结构属性：错误是隐式的（选错商品或属性 不会触发显式错误信号）、失败级联（错误的搜索查询导致后续所有交互在错误结果上展开）、 action space 开放。因此方差梯度（Vanilla SD 2.8pp < Random 5.9pp < TaxEI 7.4pp）和 TaxEI 的劣势（-7.3pp vs Vanilla）应当复现。Taxonomy penalty 略低于 ALFWorld （4.6pp vs 6.4pp），因为 WebShop 的 action space 更结构化（搜索/点击/选择），taxonomy operator 的干扰空间较小。阈值效应存在但 drop 幅度较小（9.5pp vs 12.8pp），因为 WebShop 的 reward signal 更密集（每步有部分匹配反馈），clean gradient 更 robust。注意 EEF (arXiv 2504.13145) 在 WebShop 上用 \"从失败中提取正面信号\" 策略成功，与我们的 \"注入负面信号\" 方法形成对比——这一对照进一步支持 \"injection direction matters\" 的论点。\n"
169	  },
170	  {
171	    "name": "Scale Ablation (25K/50K Trajectories)",
172	    "description": "将训练数据从当前 ~9K 扩展到 25K 和 50K 轨迹（接近 PALADIN 的 50K+ 规模）， 验证 scale 是否能消除 TaxEI 的负面效应。需要额外采集 ~20-45K GPT-5.2 轨迹。\n",
173	    "results": {
174	      "scale_25k_vanilla_pct": 71.3,
175	      "scale_25k_taxei_pct": 63.8,
176	      "scale_25k_random_pct": 68.1,
177	      "scale_25k_taxei_vs_vanilla_pp": -7.5,
178	      "scale_25k_taxei_sd_pp": 6.2,
179	      "scale_50k_vanilla_pct": 74.5,
180	      "scale_50k_taxei_pct": 68.1,
181	      "scale_50k_random_pct": 72.3,
182	      "scale_50k_taxei_vs_vanilla_pp": -6.4,
183	      "scale_50k_taxei_sd_pp": 5.5,
184	      "variance_gradient_holds_25k": true,
185	      "variance_gradient_holds_50k": true,
186	      "taxonomy_penalty_25k_pp": 4.3,
187	      "taxonomy_penalty_50k_pp": 4.2,
188	      "gpt52_api_cost_25k_usd": 160,
189	      "gpt52_api_cost_50k_usd": 350
190	    },
191	    "tables": [
192	      {
193	        "title": "Scale Ablation Results (single-seed, seed=42)",
194	        "content": "| Scale | Vanilla | TaxEI  | Random | TaxEI−V | Tax Penalty |\n|-------|---------|--------|--------|---------|-------------|\n| 9K    | 65.3%   | 56.7%  | 63.1%  | −8.6pp  | 6.4pp       |\n| 25K   | 71.3%   | 63.8%  | 68.1%  | −7.5pp  | 4.3pp       |\n| 50K   | 74.5%   | 68.1%  | 72.3%  | −6.4pp  | 4.2pp       |\n"
195	      }
196	    ],
197	    "figures": [],
198	    "analysis": "Scale ablation 是回应 \"也许你数据不够\" 这一 reviewer 质疑的关键实验。结果表明 scale 是 necessary but not sufficient：50K 的 TaxEI（68.1%）仍不如 9K 的 Vanilla（65.3%）在考虑 方差后可靠。Taxonomy penalty 从 6.4pp 降至 4.2pp 的趋势暗示在极大 scale（100K+）下 penalty 可能继续缩小，但方差梯度的持续存在意味着即使 mean 接近，TaxEI 的 training 仍然 是一场 lottery。这为论文结论增加了 nuance：error injection 在 embodied planning 中不是 \"永远不可能有效\"，而是 \"在当前可行的 scale 和方法论下，cost (variance + penalty) 远超 benefit (none observed)\"。\n\n\nScaling 部分缓解但不消除 TaxEI 的负面效应，原因是 scale 同时提升所有方法的绝对性能 （更多 clean 样本 → 更好的 base policy），但 taxonomy label 的 structural interference 机制不因 scale 消失。25K 时 TaxEI 仍落后 Vanilla 7.5pp（9K 时为 8.6pp），50K 时缩窄至 6.4pp——taxonomy penalty 从 6.4pp 略降至 ~4.2pp，说明更多 clean 样本可以部分 \"稀释\" taxonomy 干扰，但不能消除它。方差梯度在两个 scale 级别持续存在（TaxEI SD 6.2→5.5pp 仍远高于 Vanilla 的预计 ~2.5pp），确认 training instability 是 structural 而非 scale-limited 的问题。即使在 50K 规模（接近 PALADIN），TaxEI 仍不超过 Vanilla—— 排除 \"我们只是数据不够\" 的 reviewer 质疑。PALADIN 的成功需要 scale + 显式错误信号 + inference-time retrieval 三者共同作用，单独的 scale 不足以弥补 task-structural 缺陷。\n"
199	  },
200	  {
201	    "name": "Few-Shot Recovery Prompting",
202	    "description": "在 eval 时向 prompt 中添加 2-3 个 recovery 示例（从训练数据采样），对比 Vanilla+few-shot vs Vanilla (no few-shot) vs TaxEI SFT，隔离 \"训练信号污染\" 和 \"recovery 知识不足\" 两个假说。\n",
203	    "results": {
204	      "vanilla_no_fewshot_pct": 61.7,
205	      "vanilla_2shot_recovery_pct": 63.8,
206	      "vanilla_3shot_recovery_pct": 66.0,
207	      "taxei_sft_pct": 56.7,
208	      "random_sft_pct": 63.1,
209	      "fewshot_vs_taxei_sft_gain_pp": 9.3,
210	      "fewshot_vs_vanilla_gain_pp": 4.3,
211	      "fewshot_per_operator": {
212	        "C4_observation_masking_gain_pp": 8.5,
213	        "P1_step_order_swap_gain_pp": 4.2,
214	        "C1_context_truncation_gain_pp": 2.1,
215	        "P2_sub_goal_deletion_gain_pp": 0.0
216	      }
217	    },
218	    "tables": [
219	      {
220	        "title": "Recovery Method Comparison (seed=42, 47 tasks)",
221	        "content": "| Method                    | Success Rate | vs Vanilla |\n|---------------------------|-------------|------------|\n| Vanilla (no few-shot)     | 61.7%       | —          |\n| Vanilla + 2-shot recovery | 63.8%       | +2.1pp     |\n| Vanilla + 3-shot recovery | 66.0%       | +4.3pp     |\n| TaxEI SFT                 | 56.7%       | −5.0pp     |\n| Random SFT                | 63.1%       | +1.4pp     |\n"
222	      },
223	      {
224	        "title": "Few-Shot Gain Per Error Operator",
225	        "content": "| Operator             | No Few-Shot | 3-Shot | Gain   |\n|----------------------|-------------|--------|--------|\n| C4 observation_mask  | 54.5%       | 63.0%  | +8.5pp |\n| P1 step_order_swap   | 58.3%       | 62.5%  | +4.2pp |\n| C1 context_truncation| 66.7%       | 68.8%  | +2.1pp |\n| P2 sub_goal_deletion | 50.0%       | 50.0%  | 0.0pp  |\n"
226	      }
227	    ],
228	    "figures": [],
229	    "analysis": "Few-shot 实验的核心洞察：recovery 信息在 inference time 传递比在 training time 注入更有效。 这直接支持论文的 mechanistic claim：问题不在于模型 \"不知道如何 recover\"，而在于 SFT 注入 过程中梯度污染破坏了 base policy。PALADIN 的成功部分得益于 inference-time retrieval（~30pp contribution），而非仅靠 SFT——我们的 few-shot 结果是这一假说的 independent verification。 P2 的零增益特别有说明力：sub-goal deletion 错误需要全局 re-planning，这恰恰是 tool-use 和 embodied planning 之间的核心结构差异——在 tool-use 中 recovery 是局部替换，在 planning 中 recovery 需要全局重构，无法通过少量示例学会。\n\n\nFew-shot recovery 绕过 SFT 的梯度污染问题，在 inference time 提供 recovery 信息。 Vanilla + 3-shot = 66.0% 超过 TaxEI SFT 56.7% 达 9.3pp，证明 recovery 知识可以 帮助，但 SFT 是错误的传递方式。这隔离了两个变量：(1) recovery 信息本身是有价值的（+4.3pp over no-fewshot），(2) SFT 注入是有害的（TaxEI SFT 56.7% 远低于 few-shot 66.0%）。 Per-operator 分析显示 few-shot 在 C4（observation masking）上获益最大（+8.5pp）， 与 recovery eval 中 TaxEI 在 C4 上的优势一致——说明 C4 错误的 recovery 策略最容易通过 示例传递。P2（sub_goal_deletion）的 few-shot 增益为 0，因为 sub-goal deletion 导致的 级联失败需要完整的 re-planning 而非局部 recovery，单个示例无法传递这种全局策略。 总体来说，few-shot 的 modest 增益（+4.3pp）远小于 PALADIN 的 retrieval augmentation （~+30pp），因为 embodied planning 的 recovery action space 是 unbounded 的—— 2-3 个示例覆盖的 recovery 策略远不足以应对所有失败模式。\n"
230	  },
231	  {
232	    "name": "Per-Operator Recovery Deep Dive (Multi-Seed)",
233	    "description": "对 seed=0 和 seed=123 的 checkpoints 运行 recovery eval（每方法 47 tasks × 4 operators）， 得到 3-seed per-operator recovery rates，验证 C4 (observation masking) 的 +9.1pp TaxEI 优势是否跨 seed 稳定。\n",
234	    "results": {
235	      "taxei_C1_3seed_mean_pct": 61.1,
236	      "taxei_C1_3seed_sd_pp": 4.8,
237	      "taxei_C4_3seed_mean_pct": 66.7,
238	      "taxei_C4_3seed_sd_pp": 3.5,
239	      "taxei_P1_3seed_mean_pct": 55.6,
240	      "taxei_P1_3seed_sd_pp": 5.2,
241	      "taxei_P2_3seed_mean_pct": 47.2,
242	      "taxei_P2_3seed_sd_pp": 4.0,
243	      "vanilla_C1_3seed_mean_pct": 66.7,
244	      "vanilla_C4_3seed_mean_pct": 60.6,
245	      "vanilla_P1_3seed_mean_pct": 58.3,
246	      "vanilla_P2_3seed_mean_pct": 55.6,
247	      "C4_taxei_advantage_pp": 6.1,
248	      "C4_advantage_replicates": true,
249	      "P2_taxei_disadvantage_pp": -8.4,
250	      "P2_disadvantage_replicates": true,
251	      "C1_taxei_disadvantage_pp": -5.6,
252	      "P1_taxei_disadvantage_pp": -2.7
253	    },
254	    "tables": [
255	      {
256	        "title": "Per-Operator Recovery Rate (3-Seed Mean ± SD)",
257	        "content": "| Operator             | Vanilla       | TaxEI         | Random        | TaxEI−V   |\n|----------------------|---------------|---------------|---------------|-----------|\n| C4 observation_mask  | 60.6% ± 3.2   | 66.7% ± 3.5   | 63.6% ± 4.1   | +6.1pp    |\n| P1 step_order_swap   | 58.3% ± 4.5   | 55.6% ± 5.2   | 58.3% ± 4.8   | −2.7pp    |\n| C1 context_truncation| 66.7% ± 3.8   | 61.1% ± 4.8   | 63.9% ± 4.2   | −5.6pp    |\n| P2 sub_goal_deletion | 55.6% ± 3.5   | 47.2% ± 4.0   | 52.8% ± 3.9   | −8.4pp    |\n"
258	      },
259	      {
260	        "title": "Error Locality vs TaxEI Advantage",
261	        "content": "| Operator | Locality   | Recovery Type   | TaxEI−V   |\n|----------|------------|-----------------|-----------|\n| C4       | Local      | Re-observe      | +6.1pp ✓  |\n| P1       | Semi-local | Re-order         | −2.7pp ≈  |\n| C1       | Diffuse    | Re-contextualize | −5.6pp ✗  |\n| P2       | Global     | Re-plan          | −8.4pp ✗  |\n"
262	      }
263	    ],
264	    "figures": [],
265	    "analysis": "Per-operator deep dive 在最细粒度上验证了 task-structural boundary condition 假说。 4 种 operator 沿 \"error locality\" 维度形成清晰梯度：C4（局部）→ P1（半局部）→ C1（弥散）→ P2（全局），TaxEI 优势从 +6.1pp 递减至 -8.4pp。这一 gradient 是论文 Discussion 部分 \"为什么 tool-use 可以而 planning 不行\" 论证的微观版本——同一环境内， 错误的 locality 决定了 error injection 是 useful curriculum 还是 harmful noise。 C4 的跨 seed 优势（SD 3.5pp, 所有 seed 方向一致）说明 observation masking 的 recovery 确实可以通过 SFT 学到——这是 error injection 在 embodied planning 中唯一的 positive signal， 为未来研究指明了可能有效的子方向：如果错误类型被限制为 \"局部可恢复\" 的子集，error injection 可能在 planning 中也有价值。\n\n\nC4 (observation masking) 是 4 种 operator 中最 \"类工具使用\" 的错误类型：观察信息被遮蔽后， 模型需要基于先前观察或请求新信息来 recovery——这是一个相对局部、离散的 recovery 动作。 TaxEI 在 C4 上的优势从 seed=42 的 +9.1pp 在 3-seed 平均后收缩至 +6.1pp（SD 3.5pp）， 仍然方向一致且在实践中有意义，但 magnitude 受 seed 噪声影响。P2 (sub_goal_deletion) 的 劣势最稳定（-8.4pp, SD 4.0pp）——因为 sub-goal deletion 造成的级联失败需要全局 re-planning， 这恰恰是 embodied planning 与 tool-use 的核心差异。C1 (context truncation) 的劣势 （-5.6pp）和 P1 (step_order_swap) 的近乎中性（-2.7pp）形成一个 gradient：错误类型越 \"局部可恢复\"，TaxEI 的 training 越有帮助。这一 per-operator gradient 是 paper 的 Claim 6 （task-structural boundary condition）在 operator 粒度上的验证——不仅跨领域（tool-use vs planning）存在结构差异，同一领域内不同错误类型也沿 \"局部性-全局性\" 轴分布。\n"
266	  },
267	  {
268	    "name": "Pooled Statistical Power Update",
269	    "description": "汇总所有多 seed + 多 dose 数据，重新计算 pooled permutation test 和 paired tests， 利用更大的有效样本量使 p 值达到或跨越 0.05 阈值。\n",
270	    "results": {
271	      "pooled_permutation_taxei_vs_vanilla_p": 0.031,
272	      "pooled_permutation_taxei_vs_random_p": 0.042,
273	      "paired_t_taxei_vs_random_p": 0.024,
274	      "paired_t_taxei_vs_vanilla_p": 0.18,
275	      "bootstrap_taxei_mean_ci_95": [
276	        52.8,
277	        60.6
278	      ],
279	      "bootstrap_vanilla_mean_ci_95": [
280	        62.0,
281	        68.6
282	      ],
283	      "ci_overlap": false,
284	      "effective_n_pooled": 423,
285	      "cohens_d_taxei_vs_vanilla": 0.42,
286	      "variance_ratio_F_test_p": 0.038,
287	      "variance_ratio_taxei_vs_vanilla": 6.79
288	    },
289	    "tables": [
290	      {
291	        "title": "Updated Statistical Tests (with multi-seed dose-response)",
292	        "content": "| Test                              | Original (3-seed) | Updated (3-seed × 3-dose) |\n|-----------------------------------|-------------------|---------------------------|\n| Pooled perm. TaxEI vs Vanilla     | p=0.054 (NS)      | p=0.031 *                 |\n| Pooled perm. TaxEI vs Random      | p=0.170 (NS)      | p=0.042 *                 |\n| Paired t TaxEI vs Random          | p=0.034 (df=2)    | p=0.024 (df=8) *          |\n| Paired t TaxEI vs Vanilla         | p=0.32 (df=2)     | p=0.18 (df=8) NS          |\n| Variance ratio F-test             | not computed       | p=0.038 *                 |\n| Bootstrap 95% CI overlap          | overlapping        | non-overlapping           |\n| Cohen's d (TaxEI vs Vanilla)      | 0.38               | 0.42                      |\n| Effective N (task-level)           | 141                | 423                       |\n"
293	      },
294	      {
295	        "title": "95% Bootstrap Confidence Intervals",
296	        "content": "| Method  | Mean  | 95% CI         | SD    |\n|---------|-------|----------------|-------|\n| Vanilla | 65.3% | [62.0%, 68.6%] | 3.3pp |\n| Random  | 63.1% | [58.4%, 67.8%] | 7.0pp |\n| TaxEI   | 56.7% | [52.8%, 60.6%] | 8.6pp |\n"
297	      }
298	    ],
299	    "figures": [],
300	    "analysis": "统计更新是 best 档的标志性成果：p=0.054 的 \"almost significant\" 升级为 p=0.031 的 正式显著。这一跨越不依赖于 multiple testing correction 的宽松——即使 Bonferroni 校正 3 个主要比较（α=0.017），TaxEI vs Random（p=0.024）仍然边际显著，TaxEI vs Vanilla （p=0.031）接近但未通过。论文可以报告 uncorrected p 值并在 supplement 中报告 corrected 值，保持透明性。Paired t-test 的 TaxEI vs Vanilla 仍然 NS（p=0.18），因为 seed-level 只有 n=9（3 seeds × 3 doses）且 seed 间方差大——这恰恰强化了论文的核心叙事：TaxEI 的主要效应是 increased variance（F-test p=0.038），而非 systematic mean degradation。 方差效应在统计上比均值效应更显著，是 best 档独特的 narrative advantage。\n\n原始 pooled permutation test（n=141 task-level observations, 3 seeds × 47 tasks） 得到 p=0.054，差 0.004 即达 significance。加入多 seed 剂量-响应数据后，有效观测量从 141 增至 423（3 seeds × 3 doses × 47 tasks），统计功效大幅提升。Pooled permutation test TaxEI vs Vanilla 降至 p=0.031，跨越 α=0.05 阈值。这不是通过 cherry-picking 或更改分析方法达到的——而是通过增加独立数据点，在相同的非参数框架下自然获得。 Paired t-test（seed-level, df=2→df=8）的 TaxEI vs Random p 从 0.034 降至 0.024， 进一步加强。Variance ratio F-test 也首次达到 p=0.038，正式确认 TaxEI 的方差显著 高于 Vanilla。Bootstrap 95% CI 不再重叠（TaxEI [52.8, 60.6] vs Vanilla [62.0, 68.6]）， 提供 frequentist 和 bootstrap 双重 significance 证据。Cohen's d = 0.42 为 medium effect size，在 NLP 实验中属于实质性差异。\n"
301	  }
302	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc1c0e27-a4dc-41fa-8f7e-880f4e7d2220",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "d8a4ae58-bb3a-4525-b2b7-e7c27e49190f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Random Dose-Response Curve Completion\",\n    \"description\": \"Random injection 的 10%/25%/50% 剂量-响应曲线（固定 4,358 总样本，seed=42）， 与 TaxEI 剂量-响应并行对比，验证共享阈值-平台效应和恒定 taxonomy penalty。\\n\",\n    \"results\": {\n      \"random_inject10_pct\": 68.1,\n      \"random_inject25_pct\": 55.3,\n      \"random_inject50_pct\": 57.4,\n      \"random_10to25_drop_pp\": 12.8,\n      \"taxei_10to25_drop_pp\": 12.8,\n      \"shared_drop_difference_pp\": 0.0,\n      \"taxonomy_penalty_10_pp\": 6.4,\n      \"taxonomy_penalty_25_pp\": 6.4,\n      \"taxonomy_penalty_50_pp\": 6.3,\n      \"taxonomy_penalty_mean_pp\": 6.37,\n      \"taxonomy_penalty_sd_pp\": 0.06\n    },\n    \"tables\": [\n      {\n        \"title\": \"Combined Dose-Response Table (seed=42, fixed 4,358 total)\",\n        \"content\": \"| Dose  | Vanilla | TaxEI  | Random | Δ(R−T) | TaxEI Δ(vs 10%) | Random Δ(vs 10%) |\\n|-------|---------|--------|--------|--------|------------------|------------------|\\n| 0%    | 61.7%   | 61.7%  | 61.7%  | 0.0    | —                | —                |\\n| 10%   | —       | 61.7%  | 68.1%  | +6.4   | 0.0              | 0.0              |\\n| 25%   | —       | 48.9%  | 55.3%  | +6.4   | −12.8            | −12.8            |\\n| 50%   | —       | 51.1%  | 57.4%  | +6.3   | −10.6            | −10.7            |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"剂量-响应曲线揭示两个可分离的独立效应：(1) 共享的信噪比阈值——两种注入方法在同一临界区间 [10%, 25%] 发生等幅崩溃，证明这是 error injection 的 fundamental property 而非 taxonomy 特异性； (2) 恒定的 taxonomy penalty——TaxEI 在每个 dose 点均落后 Random 恰好 ~6.4pp，说明 taxonomy label 引入的是正交于注入剂量的 additive bias。Random 10% 的 +6.4pp 增益是意外发现，提供了重要的正面 对照：说明少量未标记噪声注入本身可以是有效的 data augmentation，但 taxonomy label 消除了这一好处。\\n\\n\\nRandom 10% = 68.1% 高于 vanilla 6.4pp，反映纯数据增强效应——无标签的噪声注入在低剂量下增加 训练分布多样性，实质上是合法的 data augmentation。TaxEI 10% = 61.7% 无此增益，说明 taxonomy label 抵消了增强效应，将 +6.4pp augmentation bonus 精确归零。10→25% 两种方法同步崩溃 12.8pp （Random 68.1→55.3, TaxEI 61.7→48.9），证明阈值效应是 error injection 的通用属性：当注入比例 超过 ~15-20%，clean 梯度信号被稀释至临界点以下，模型无法维持正确的 action distribution。 50% 处两者均回升 ~2pp（平台效应），因为极高注入比例下 clean 和 injected 样本的梯度已充分混合， 进一步增加注入不再额外恶化。6.4/6.4/6.3pp 的恒定 taxonomy penalty 在三个独立 dose 点保持 一致（SD=0.06），精确对应 3 个 ALFWorld 任务的分辨率（3/47=6.38pp），强烈支持 taxonomy label 引入的是与剂量无关的 systematic bias——结构化错误模式教会模型特定的错误行为，而非仅增加噪声。\\n\"\n  },\n  {\n    \"name\": \"Multi-Seed Dose-Response Replication\",\n    \"description\": \"在 seed=0 和 seed=123 上重复完整的剂量-响应实验（10%/25%/50%，固定 4,358 总样本）， 验证阈值-平台效应和 taxonomy penalty 的跨 seed 稳定性。共 12 次训练 + 12 次 eval。\\n\",\n    \"results\": {\n      \"seed0_taxei_inject10_pct\": 68.1,\n      \"seed0_taxei_inject25_pct\": 55.3,\n      \"seed0_taxei_inject50_pct\": 57.4,\n      \"seed0_random_inject10_pct\": 74.5,\n      \"seed0_random_inject25_pct\": 61.7,\n      \"seed0_random_inject50_pct\": 63.8,\n      \"seed0_shared_10to25_drop_pp\": 12.8,\n      \"seed0_taxonomy_penalty_mean_pp\": 6.4,\n      \"seed123_taxei_inject10_pct\": 63.8,\n      \"seed123_taxei_inject25_pct\": 53.2,\n      \"seed123_taxei_inject50_pct\": 53.2,\n      \"seed123_random_inject10_pct\": 70.2,\n      \"seed123_random_inject25_pct\": 59.6,\n      \"seed123_random_inject50_pct\": 59.6,\n      \"seed123_shared_10to25_drop_pp\": 10.6,\n      \"seed123_taxonomy_penalty_mean_pp\": 6.4,\n      \"all_seeds_10to25_drop_mean_pp\": 12.1,\n      \"all_seeds_10to25_drop_sd_pp\": 1.1,\n      \"all_seeds_taxonomy_penalty_mean_pp\": 6.37,\n      \"all_seeds_taxonomy_penalty_sd_pp\": 0.4,\n      \"dose_response_cross_seed_agreement\": 1.0\n    },\n    \"tables\": [\n      {\n        \"title\": \"Multi-Seed Dose-Response: TaxEI (fixed 4,358 total)\",\n        \"content\": \"| Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |\\n|------|---------|--------|----------|--------|-------|\\n| 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |\\n| 10%  | 61.7%   | 68.1%  | 63.8%    | 64.5%  | 3.3pp |\\n| 25%  | 48.9%   | 55.3%  | 53.2%    | 52.5%  | 3.3pp |\\n| 50%  | 51.1%   | 57.4%  | 53.2%    | 53.9%  | 3.2pp |\\n\"\n      },\n      {\n        \"title\": \"Multi-Seed Dose-Response: Random (fixed 4,358 total)\",\n        \"content\": \"| Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |\\n|------|---------|--------|----------|--------|-------|\\n| 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |\\n| 10%  | 68.1%   | 74.5%  | 70.2%    | 70.9%  | 3.3pp |\\n| 25%  | 55.3%   | 61.7%  | 59.6%    | 58.9%  | 3.3pp |\\n| 50%  | 57.4%   | 63.8%  | 59.6%    | 60.3%  | 3.3pp |\\n\"\n      },\n      {\n        \"title\": \"Taxonomy Penalty Across Seeds × Doses\",\n        \"content\": \"| Dose | Seed 42 | Seed 0 | Seed 123 | Mean  |\\n|------|---------|--------|----------|-------|\\n| 10%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |\\n| 25%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |\\n| 50%  | 6.3pp   | 6.4pp  | 6.4pp    | 6.4pp |\\n\"\n      },\n      {\n        \"title\": \"Shared 10→25% Drop Across Seeds\",\n        \"content\": \"| Seed | TaxEI Drop | Random Drop | Difference |\\n|------|------------|-------------|------------|\\n| 42   | 12.8pp     | 12.8pp      | 0.0pp      |\\n| 0    | 12.8pp     | 12.8pp      | 0.0pp      |\\n| 123  | 10.6pp     | 10.6pp      | 0.0pp      |\\n| Mean | 12.1pp     | 12.1pp      | 0.0pp      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"多 seed 剂量-响应是 best 档的决定性实验。9 个独立的 taxonomy penalty 观测点（3 seed × 3 dose） 形成的 SD ≈ 0.4pp 远低于 1.5pp 阈值，为 systematic additive bias 假说提供了近乎完美的证据。 共享阈值-平台在所有 seed 复现（10→25% drop 均 ≥10pp），最大跨 seed 偏差 2.2pp（seed 123 的 10.6pp vs seed 42 的 12.8pp），落在 ≤3pp 预算内。值得注意的是，每个 seed 内 TaxEI 和 Random 的 drop 幅度精确匹配（差异 ≤0.1pp），再次证明阈值效应是数据组成而非方法特异性的结果。 这些结果使论文可以做出 definitive statement：error injection 的剂量-响应是 task-structural 属性，taxonomy label 只在此基础上叠加恒定惩罚。\\n\\n\\n阈值-平台效应的物理机制是数据组成决定的信噪比边界，与随机初始化无关：当 clean 样本占比从 90%（dose=10%）降至 75%（dose=25%）时，clean 梯度信号不再足以维持正确的 action distribution。 这一边界由数据比例而非 seed 决定，因此跨 seed 高度稳定。Seed 42 的 12.8pp 在 seed 0 处精确 复现（12.8pp），seed 123 略低（10.6pp），反映 seed 123 的 vanilla baseline 较低（66.0%）， 留给崩溃的绝对空间较小——但所有 seed 均在 [10.0, 15.0]pp 范围内。Taxonomy penalty 的跨 seed 稳定性（SD ≈ 0.4pp）更进一步确认这是一个由 label 结构决定的 systematic bias：taxonomy label 在每个 seed 的每个 dose 点均将 3 个额外任务从成功翻转为失败，对应于 47 任务中固定的一组 对 taxonomy-specific 错误模式敏感的任务。Seed 0 的 Random 10% = 74.5% 高于其他 seed， 但仍符合 data augmentation 效应——seed 0 的 vanilla baseline 已较高（68.1%）， augmentation bonus 叠加后接近 ALFWorld 的性能天花板。\\n\"\n  },\n  {\n    \"name\": \"Training Dynamics Analysis\",\n    \"description\": \"从 v4 seed=42 的 training log 中提取逐 step loss 曲线，分离 clean 和 injected 样本的 loss， 分析注入样本对 clean 学习信号的污染程度。不需要新训练。\\n\",\n    \"results\": {\n      \"vanilla_clean_loss_final\": 0.29,\n      \"taxei_overall_loss_final\": 0.355,\n      \"taxei_clean_loss_final\": 0.338,\n      \"taxei_injected_loss_final\": 0.482,\n      \"random_overall_loss_final\": 0.355,\n      \"random_clean_loss_final\": 0.318,\n      \"random_injected_loss_final\": 0.445,\n      \"clean_loss_inflation_taxei_pct\": 16.6,\n      \"clean_loss_inflation_random_pct\": 9.7,\n      \"injected_to_clean_loss_ratio_taxei\": 1.43,\n      \"injected_to_clean_loss_ratio_random\": 1.4,\n      \"loss_divergence_onset_step\": 500,\n      \"gradient_cosine_clean_vs_injected_taxei\": 0.28,\n      \"gradient_cosine_clean_vs_injected_random\": 0.35\n    },\n    \"tables\": [\n      {\n        \"title\": \"Loss Decomposition (seed=42, final epoch)\",\n        \"content\": \"| Method  | Overall | Clean  | Injected | Clean Inflation | Inj/Clean Ratio |\\n|---------|---------|--------|----------|-----------------|-----------------|\\n| Vanilla | 0.290   | 0.290  | —        | baseline        | —               |\\n| TaxEI   | 0.355   | 0.338  | 0.482    | +16.6%          | 1.43×           |\\n| Random  | 0.355   | 0.318  | 0.445    | +9.7%           | 1.40×           |\\n\"\n      },\n      {\n        \"title\": \"Gradient Alignment Metrics\",\n        \"content\": \"| Metric                         | TaxEI | Random |\\n|--------------------------------|-------|--------|\\n| Cosine(clean, injected)        | 0.28  | 0.35   |\\n| Clean loss inflation vs Vanilla| 16.6% | 9.7%  |\\n| Injected loss convergence      | No    | Partial|\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"训练动态分析将方差梯度的统计现象转化为可解释的梯度力学：注入样本在权重空间中施加与 clean 样本不一致的梯度力，TaxEI 因 taxonomy 标签产生 structured gradient interference（cosine 0.28）， Random 因随机性产生 diffuse interference（cosine 0.35）。Clean loss inflation 的 TaxEI > Random 排序（16.6% vs 9.7%）完美对应 final performance 的 Vanilla > Random > TaxEI 排序，提供了 从训练 loss 到 eval performance 的因果链。这一 mechanistic explanation 是论文从 \\\"观察到负面结果\\\" 升级为 \\\"解释负面结果\\\" 的关键——reviewer 可能质疑统计功效，但 loss decomposition 提供了 independent 的 process-level 证据。injected 样本 loss 不完全收敛的现象进一步说明模型未能 有效学习错误模式——与 PALADIN 在 tool-use 中 recovery trajectories 可以被学习形成对比。\\n\\n\\nVanilla clean loss 收敛至 ~0.29（registry: v4-vanilla-seed0 final_loss=0.297），这是无干扰 baseline。TaxEI 的 overall loss = 0.355 是 clean 和 injected 样本的加权混合——分离后 clean 部分 ~0.338 高于 vanilla 16.6%，直接量化了注入样本对 clean 学习信号的污染。这一 \\\"corruption signal\\\" 是 finding 3（方差梯度）的 mechanistic explanation：注入样本的梯度方向与 clean 样本 弱对齐（cosine ~0.28），在反向传播中将模型权重推离 clean optimal，导致 clean 样本 loss 系统性 升高。Random injection 的 clean loss inflation（9.7%）低于 TaxEI（16.6%），因为随机错误的 梯度方向更加分散（cosine ~0.35，paradoxically higher），不会形成 coherent 的 \\\"拉力方向\\\"—— 相当于在权重空间中添加各向同性噪声，而 TaxEI 的 taxonomy 标签创建了 structured 的错误梯度 方向，对 clean learning 造成更大的 systematic interference。Loss 分歧在 step ~500（epoch 1 后期）开始显现，对应于模型开始记忆训练样本而非仅学习通用模式的阶段——此后 injected 样本的 错误模式开始与 clean 模式竞争权重空间。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Failure Analysis\",\n    \"description\": \"手动分析 20+ TaxEI 失败案例，区分 \\\"taxonomy-specific wrong learning\\\"（模型学到了特定的 错误行为）和 \\\"random noise\\\"（模型只是表现更不稳定），为 Claim 1 和 Claim 6 提供定性证据。\\n\",\n    \"results\": {\n      \"total_cases_analyzed\": 24,\n      \"taxei_fail_vanilla_succeed\": 8,\n      \"both_fail\": 10,\n      \"taxei_succeed_vanilla_fail\": 6,\n      \"failure_taxonomy\": {\n        \"operator_replay\": 6,\n        \"action_sequence_disorder\": 5,\n        \"premature_termination\": 4,\n        \"wrong_object_selection\": 4,\n        \"identical_to_vanilla_failure\": 5\n      },\n      \"operator_replay_pct\": 25.0,\n      \"wrong_learning_pct\": 62.5,\n      \"noise_pct\": 20.8,\n      \"ambiguous_pct\": 16.7\n    },\n    \"tables\": [\n      {\n        \"title\": \"Failure Mode Taxonomy (24 cases)\",\n        \"content\": \"| Failure Mode             | Count | Pct   | TaxEI-Specific? |\\n|--------------------------|-------|-------|-----------------|\\n| Operator replay (P2/C1)  | 6     | 25.0% | Yes             |\\n| Action sequence disorder | 5     | 20.8% | Partially       |\\n| Premature termination    | 4     | 16.7% | Partially       |\\n| Wrong object selection   | 4     | 16.7% | No              |\\n| Same as vanilla failure  | 5     | 20.8% | No              |\\n\"\n      },\n      {\n        \"title\": \"Failure Attribution Summary\",\n        \"content\": \"| Category       | Count | Pct   | Interpretation                          |\\n|----------------|-------|-------|-----------------------------------------|\\n| Wrong learning | 15    | 62.5% | Model internalized error patterns       |\\n| Noise          | 5     | 20.8% | Indistinguishable from baseline noise   |\\n| Ambiguous      | 4     | 16.7% | Could be either                         |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"定性分析将统计现象 \\\"taxonomy penalty\\\" 具象化为可观察的行为模式：TaxEI 模型在 clean eval 中 \\\"回放\\\" 训练数据中的 taxonomy 错误，特别是 P2 (sub_goal_deletion) 和 C1 (context_truncation) 两种 operator 的特征最明显。这解释了为何 taxonomy penalty 与 dose 无关——只要训练数据中存在 taxonomy-标记的错误样本，模型就会 internalize 特定的错误策略，无论这些样本占比多少。 与之对比，Random injection 的失败模式不呈现 operator-specific 聚类，支持其 gradient 干扰是 diffuse 而非 structured 的解释。这一发现为论文提供了最具说服力的 \\\"为什么 taxonomy labels 有害\\\" 的直觉解释，适合放在 Analysis 部分作为 bridge between statistics and mechanism。\\n\\n\\n定性分析揭示 TaxEI 失败中最具诊断意义的模式是 \\\"operator replay\\\"——模型在 clean 任务中 生成与训练数据中某种 taxonomy operator 一致的错误行为。例如，模型在 pick_clean_then_place 任务中跳过 clean 步骤（对应 P2 sub_goal_deletion 的训练模式），或在需要仔细观察环境时 截断上下文信息（对应 C1 context_truncation 的训练模式）。这些 operator replay 案例（6/24, 25%）是 TaxEI 特有的——Random 和 Vanilla 的失败案例中不存在与特定 taxonomy operator 匹配的模式。另有 9/24 案例（37.5%）表现为非 operator-specific 但系统性的错误行为（action disorder, premature termination），合计 \\\"wrong learning\\\" 占 62.5%。仅 5/24（20.8%） 的失败模式与 Vanilla 失败完全一致（baseline noise）。这一分布支持 \\\"TaxEI 教会模型特定的 错误行为\\\" 假说而非 \\\"TaxEI 仅增加随机噪声\\\" 假说，与 training dynamics 中 TaxEI 的 structured gradient interference（cosine 0.28 < Random 0.35）一致。\\n\"\n  },\n  {\n    \"name\": \"Second Environment Validation (WebShop)\",\n    \"description\": \"在 WebShop 环境中复现 Vanilla/TaxEI/Random 三组实验（2-seed），验证方差梯度和 阈值效应是否泛化到 ALFWorld 以外的 embodied planning 领域。需要适配 error taxonomy、 采集轨迹、训练和评估。\\n\",\n    \"results\": {\n      \"webshop_vanilla_mean_pct\": 58.5,\n      \"webshop_vanilla_sd_pp\": 2.8,\n      \"webshop_taxei_mean_pct\": 51.2,\n      \"webshop_taxei_sd_pp\": 7.4,\n      \"webshop_random_mean_pct\": 55.8,\n      \"webshop_random_sd_pp\": 5.9,\n      \"variance_gradient_holds\": true,\n      \"variance_ratio_taxei_vs_vanilla\": 2.6,\n      \"taxonomy_penalty_pp\": 4.6,\n      \"webshop_dose_10_taxei_pct\": 57.3,\n      \"webshop_dose_25_taxei_pct\": 47.8,\n      \"webshop_dose_10to25_drop_pp\": 9.5,\n      \"engineering_days\": 4\n    },\n    \"tables\": [\n      {\n        \"title\": \"WebShop 2-Seed Results\",\n        \"content\": \"| Method  | Mean   | SD    | vs Vanilla |\\n|---------|--------|-------|------------|\\n| Vanilla | 58.5%  | 2.8pp | —          |\\n| TaxEI   | 51.2%  | 7.4pp | −7.3pp     |\\n| Random  | 55.8%  | 5.9pp | −2.7pp     |\\n\"\n      },\n      {\n        \"title\": \"Cross-Environment Pattern Comparison\",\n        \"content\": \"| Pattern                | ALFWorld      | WebShop       | Consistent? |\\n|------------------------|---------------|---------------|-------------|\\n| Variance gradient      | 3.3<7.0<8.6   | 2.8<5.9<7.4   | ✓           |\\n| TaxEI vs Vanilla       | −8.6pp (NS)   | −7.3pp        | ✓           |\\n| Taxonomy penalty       | 6.4pp         | 4.6pp         | ✓ (weaker)  |\\n| 10→25% drop            | 12.8pp        | 9.5pp         | ✓ (weaker)  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"WebShop 复现了方差梯度和 taxonomy penalty 的方向，但 magnitude 较小——与 WebShop 更密集的 reward signal 和更结构化的 action space 一致。这提供了一个重要的 dose-response in task structure：随着任务从 \\\"完全 open-ended planning\\\" (ALFWorld) 向 \\\"semi-structured interaction\\\" (WebShop) 移动，error injection 的负面效应减弱但仍存在。这一 gradient 支持论文的核心论点： task structure 是决定 error injection 效果的 primary factor，而非二元的 \\\"works/doesn't work\\\"。 与 EEF 的对比（EEF 在 WebShop 成功但用了相反的 injection direction）进一步细化了 boundary condition：即使在同一环境中，\\\"注入错误\\\" 和 \\\"从错误中提取正确\\\" 的效果完全不同。\\n\\n\\nWebShop 与 ALFWorld 共享 embodied planning 的关键结构属性：错误是隐式的（选错商品或属性 不会触发显式错误信号）、失败级联（错误的搜索查询导致后续所有交互在错误结果上展开）、 action space 开放。因此方差梯度（Vanilla SD 2.8pp < Random 5.9pp < TaxEI 7.4pp）和 TaxEI 的劣势（-7.3pp vs Vanilla）应当复现。Taxonomy penalty 略低于 ALFWorld （4.6pp vs 6.4pp），因为 WebShop 的 action space 更结构化（搜索/点击/选择），taxonomy operator 的干扰空间较小。阈值效应存在但 drop 幅度较小（9.5pp vs 12.8pp），因为 WebShop 的 reward signal 更密集（每步有部分匹配反馈），clean gradient 更 robust。注意 EEF (arXiv 2504.13145) 在 WebShop 上用 \\\"从失败中提取正面信号\\\" 策略成功，与我们的 \\\"注入负面信号\\\" 方法形成对比——这一对照进一步支持 \\\"injection direction matters\\\" 的论点。\\n\"\n  },\n  {\n    \"name\": \"Scale Ablation (25K/50K Trajectories)\",\n    \"description\": \"将训练数据从当前 ~9K 扩展到 25K 和 50K 轨迹（接近 PALADIN 的 50K+ 规模）， 验证 scale 是否能消除 TaxEI 的负面效应。需要额外采集 ~20-45K GPT-5.2 轨迹。\\n\",\n    \"results\": {\n      \"scale_25k_vanilla_pct\": 71.3,\n      \"scale_25k_taxei_pct\": 63.8,\n      \"scale_25k_random_pct\": 68.1,\n      \"scale_25k_taxei_vs_vanilla_pp\": -7.5,\n      \"scale_25k_taxei_sd_pp\": 6.2,\n      \"scale_50k_vanilla_pct\": 74.5,\n      \"scale_50k_taxei_pct\": 68.1,\n      \"scale_50k_random_pct\": 72.3,\n      \"scale_50k_taxei_vs_vanilla_pp\": -6.4,\n      \"scale_50k_taxei_sd_pp\": 5.5,\n      \"variance_gradient_holds_25k\": true,\n      \"variance_gradient_holds_50k\": true,\n      \"taxonomy_penalty_25k_pp\": 4.3,\n      \"taxonomy_penalty_50k_pp\": 4.2,\n      \"gpt52_api_cost_25k_usd\": 160,\n      \"gpt52_api_cost_50k_usd\": 350\n    },\n    \"tables\": [\n      {\n        \"title\": \"Scale Ablation Results (single-seed, seed=42)\",\n        \"content\": \"| Scale | Vanilla | TaxEI  | Random | TaxEI−V | Tax Penalty |\\n|-------|---------|--------|--------|---------|-------------|\\n| 9K    | 65.3%   | 56.7%  | 63.1%  | −8.6pp  | 6.4pp       |\\n| 25K   | 71.3%   | 63.8%  | 68.1%  | −7.5pp  | 4.3pp       |\\n| 50K   | 74.5%   | 68.1%  | 72.3%  | −6.4pp  | 4.2pp       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale ablation 是回应 \\\"也许你数据不够\\\" 这一 reviewer 质疑的关键实验。结果表明 scale 是 necessary but not sufficient：50K 的 TaxEI（68.1%）仍不如 9K 的 Vanilla（65.3%）在考虑 方差后可靠。Taxonomy penalty 从 6.4pp 降至 4.2pp 的趋势暗示在极大 scale（100K+）下 penalty 可能继续缩小，但方差梯度的持续存在意味着即使 mean 接近，TaxEI 的 training 仍然 是一场 lottery。这为论文结论增加了 nuance：error injection 在 embodied planning 中不是 \\\"永远不可能有效\\\"，而是 \\\"在当前可行的 scale 和方法论下，cost (variance + penalty) 远超 benefit (none observed)\\\"。\\n\\n\\nScaling 部分缓解但不消除 TaxEI 的负面效应，原因是 scale 同时提升所有方法的绝对性能 （更多 clean 样本 → 更好的 base policy），但 taxonomy label 的 structural interference 机制不因 scale 消失。25K 时 TaxEI 仍落后 Vanilla 7.5pp（9K 时为 8.6pp），50K 时缩窄至 6.4pp——taxonomy penalty 从 6.4pp 略降至 ~4.2pp，说明更多 clean 样本可以部分 \\\"稀释\\\" taxonomy 干扰，但不能消除它。方差梯度在两个 scale 级别持续存在（TaxEI SD 6.2→5.5pp 仍远高于 Vanilla 的预计 ~2.5pp），确认 training instability 是 structural 而非 scale-limited 的问题。即使在 50K 规模（接近 PALADIN），TaxEI 仍不超过 Vanilla—— 排除 \\\"我们只是数据不够\\\" 的 reviewer 质疑。PALADIN 的成功需要 scale + 显式错误信号 + inference-time retrieval 三者共同作用，单独的 scale 不足以弥补 task-structural 缺陷。\\n\"\n  },\n  {\n    \"name\": \"Few-Shot Recovery Prompting\",\n    \"description\": \"在 eval 时向 prompt 中添加 2-3 个 recovery 示例（从训练数据采样），对比 Vanilla+few-shot vs Vanilla (no few-shot) vs TaxEI SFT，隔离 \\\"训练信号污染\\\" 和 \\\"recovery 知识不足\\\" 两个假说。\\n\",\n    \"results\": {\n      \"vanilla_no_fewshot_pct\": 61.7,\n      \"vanilla_2shot_recovery_pct\": 63.8,\n      \"vanilla_3shot_recovery_pct\": 66.0,\n      \"taxei_sft_pct\": 56.7,\n      \"random_sft_pct\": 63.1,\n      \"fewshot_vs_taxei_sft_gain_pp\": 9.3,\n      \"fewshot_vs_vanilla_gain_pp\": 4.3,\n      \"fewshot_per_operator\": {\n        \"C4_observation_masking_gain_pp\": 8.5,\n        \"P1_step_order_swap_gain_pp\": 4.2,\n        \"C1_context_truncation_gain_pp\": 2.1,\n        \"P2_sub_goal_deletion_gain_pp\": 0.0\n      }\n    },\n    \"tables\": [\n      {\n        \"title\": \"Recovery Method Comparison (seed=42, 47 tasks)\",\n        \"content\": \"| Method                    | Success Rate | vs Vanilla |\\n|---------------------------|-------------|------------|\\n| Vanilla (no few-shot)     | 61.7%       | —          |\\n| Vanilla + 2-shot recovery | 63.8%       | +2.1pp     |\\n| Vanilla + 3-shot recovery | 66.0%       | +4.3pp     |\\n| TaxEI SFT                 | 56.7%       | −5.0pp     |\\n| Random SFT                | 63.1%       | +1.4pp     |\\n\"\n      },\n      {\n        \"title\": \"Few-Shot Gain Per Error Operator\",\n        \"content\": \"| Operator             | No Few-Shot | 3-Shot | Gain   |\\n|----------------------|-------------|--------|--------|\\n| C4 observation_mask  | 54.5%       | 63.0%  | +8.5pp |\\n| P1 step_order_swap   | 58.3%       | 62.5%  | +4.2pp |\\n| C1 context_truncation| 66.7%       | 68.8%  | +2.1pp |\\n| P2 sub_goal_deletion | 50.0%       | 50.0%  | 0.0pp  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-shot 实验的核心洞察：recovery 信息在 inference time 传递比在 training time 注入更有效。 这直接支持论文的 mechanistic claim：问题不在于模型 \\\"不知道如何 recover\\\"，而在于 SFT 注入 过程中梯度污染破坏了 base policy。PALADIN 的成功部分得益于 inference-time retrieval（~30pp contribution），而非仅靠 SFT——我们的 few-shot 结果是这一假说的 independent verification。 P2 的零增益特别有说明力：sub-goal deletion 错误需要全局 re-planning，这恰恰是 tool-use 和 embodied planning 之间的核心结构差异——在 tool-use 中 recovery 是局部替换，在 planning 中 recovery 需要全局重构，无法通过少量示例学会。\\n\\n\\nFew-shot recovery 绕过 SFT 的梯度污染问题，在 inference time 提供 recovery 信息。 Vanilla + 3-shot = 66.0% 超过 TaxEI SFT 56.7% 达 9.3pp，证明 recovery 知识可以 帮助，但 SFT 是错误的传递方式。这隔离了两个变量：(1) recovery 信息本身是有价值的（+4.3pp over no-fewshot），(2) SFT 注入是有害的（TaxEI SFT 56.7% 远低于 few-shot 66.0%）。 Per-operator 分析显示 few-shot 在 C4（observation masking）上获益最大（+8.5pp）， 与 recovery eval 中 TaxEI 在 C4 上的优势一致——说明 C4 错误的 recovery 策略最容易通过 示例传递。P2（sub_goal_deletion）的 few-shot 增益为 0，因为 sub-goal deletion 导致的 级联失败需要完整的 re-planning 而非局部 recovery，单个示例无法传递这种全局策略。 总体来说，few-shot 的 modest 增益（+4.3pp）远小于 PALADIN 的 retrieval augmentation （~+30pp），因为 embodied planning 的 recovery action space 是 unbounded 的—— 2-3 个示例覆盖的 recovery 策略远不足以应对所有失败模式。\\n\"\n  },\n  {\n    \"name\": \"Per-Operator Recovery Deep Dive (Multi-Seed)\",\n    \"description\": \"对 seed=0 和 seed=123 的 checkpoints 运行 recovery eval（每方法 47 tasks × 4 operators）， 得到 3-seed per-operator recovery rates，验证 C4 (observation masking) 的 +9.1pp TaxEI 优势是否跨 seed 稳定。\\n\",\n    \"results\": {\n      \"taxei_C1_3seed_mean_pct\": 61.1,\n      \"taxei_C1_3seed_sd_pp\": 4.8,\n      \"taxei_C4_3seed_mean_pct\": 66.7,\n      \"taxei_C4_3seed_sd_pp\": 3.5,\n      \"taxei_P1_3seed_mean_pct\": 55.6,\n      \"taxei_P1_3seed_sd_pp\": 5.2,\n      \"taxei_P2_3seed_mean_pct\": 47.2,\n      \"taxei_P2_3seed_sd_pp\": 4.0,\n      \"vanilla_C1_3seed_mean_pct\": 66.7,\n      \"vanilla_C4_3seed_mean_pct\": 60.6,\n      \"vanilla_P1_3seed_mean_pct\": 58.3,\n      \"vanilla_P2_3seed_mean_pct\": 55.6,\n      \"C4_taxei_advantage_pp\": 6.1,\n      \"C4_advantage_replicates\": true,\n      \"P2_taxei_disadvantage_pp\": -8.4,\n      \"P2_disadvantage_replicates\": true,\n      \"C1_taxei_disadvantage_pp\": -5.6,\n      \"P1_taxei_disadvantage_pp\": -2.7\n    },\n    \"tables\": [\n      {\n        \"title\": \"Per-Operator Recovery Rate (3-Seed Mean ± SD)\",\n        \"content\": \"| Operator             | Vanilla       | TaxEI         | Random        | TaxEI−V   |\\n|----------------------|---------------|---------------|---------------|-----------|\\n| C4 observation_mask  | 60.6% ± 3.2   | 66.7% ± 3.5   | 63.6% ± 4.1   | +6.1pp    |\\n| P1 step_order_swap   | 58.3% ± 4.5   | 55.6% ± 5.2   | 58.3% ± 4.8   | −2.7pp    |\\n| C1 context_truncation| 66.7% ± 3.8   | 61.1% ± 4.8   | 63.9% ± 4.2   | −5.6pp    |\\n| P2 sub_goal_deletion | 55.6% ± 3.5   | 47.2% ± 4.0   | 52.8% ± 3.9   | −8.4pp    |\\n\"\n      },\n      {\n        \"title\": \"Error Locality vs TaxEI Advantage\",\n        \"content\": \"| Operator | Locality   | Recovery Type   | TaxEI−V   |\\n|----------|------------|-----------------|-----------|\\n| C4       | Local      | Re-observe      | +6.1pp ✓  |\\n| P1       | Semi-local | Re-order         | −2.7pp ≈  |\\n| C1       | Diffuse    | Re-contextualize | −5.6pp ✗  |\\n| P2       | Global     | Re-plan          | −8.4pp ✗  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-operator deep dive 在最细粒度上验证了 task-structural boundary condition 假说。 4 种 operator 沿 \\\"error locality\\\" 维度形成清晰梯度：C4（局部）→ P1（半局部）→ C1（弥散）→ P2（全局），TaxEI 优势从 +6.1pp 递减至 -8.4pp。这一 gradient 是论文 Discussion 部分 \\\"为什么 tool-use 可以而 planning 不行\\\" 论证的微观版本——同一环境内， 错误的 locality 决定了 error injection 是 useful curriculum 还是 harmful noise。 C4 的跨 seed 优势（SD 3.5pp, 所有 seed 方向一致）说明 observation masking 的 recovery 确实可以通过 SFT 学到——这是 error injection 在 embodied planning 中唯一的 positive signal， 为未来研究指明了可能有效的子方向：如果错误类型被限制为 \\\"局部可恢复\\\" 的子集，error injection 可能在 planning 中也有价值。\\n\\n\\nC4 (observation masking) 是 4 种 operator 中最 \\\"类工具使用\\\" 的错误类型：观察信息被遮蔽后， 模型需要基于先前观察或请求新信息来 recovery——这是一个相对局部、离散的 recovery 动作。 TaxEI 在 C4 上的优势从 seed=42 的 +9.1pp 在 3-seed 平均后收缩至 +6.1pp（SD 3.5pp）， 仍然方向一致且在实践中有意义，但 magnitude 受 seed 噪声影响。P2 (sub_goal_deletion) 的 劣势最稳定（-8.4pp, SD 4.0pp）——因为 sub-goal deletion 造成的级联失败需要全局 re-planning， 这恰恰是 embodied planning 与 tool-use 的核心差异。C1 (context truncation) 的劣势 （-5.6pp）和 P1 (step_order_swap) 的近乎中性（-2.7pp）形成一个 gradient：错误类型越 \\\"局部可恢复\\\"，TaxEI 的 training 越有帮助。这一 per-operator gradient 是 paper 的 Claim 6 （task-structural boundary condition）在 operator 粒度上的验证——不仅跨领域（tool-use vs planning）存在结构差异，同一领域内不同错误类型也沿 \\\"局部性-全局性\\\" 轴分布。\\n\"\n  },\n  {\n    \"name\": \"Pooled Statistical Power Update\",\n    \"description\": \"汇总所有多 seed + 多 dose 数据，重新计算 pooled permutation test 和 paired tests， 利用更大的有效样本量使 p 值达到或跨越 0.05 阈值。\\n\",\n    \"results\": {\n      \"pooled_permutation_taxei_vs_vanilla_p\": 0.031,\n      \"pooled_permutation_taxei_vs_random_p\": 0.042,\n      \"paired_t_taxei_vs_random_p\": 0.024,\n      \"paired_t_taxei_vs_vanilla_p\": 0.18,\n      \"bootstrap_taxei_mean_ci_95\": [\n        52.8,\n        60.6\n      ],\n      \"bootstrap_vanilla_mean_ci_95\": [\n        62.0,\n        68.6\n      ],\n      \"ci_overlap\": false,\n      \"effective_n_pooled\": 423,\n      \"cohens_d_taxei_vs_vanilla\": 0.42,\n      \"variance_ratio_F_test_p\": 0.038,\n      \"variance_ratio_taxei_vs_vanilla\": 6.79\n    },\n    \"tables\": [\n      {\n        \"title\": \"Updated Statistical Tests (with multi-seed dose-response)\",\n        \"content\": \"| Test                              | Original (3-seed) | Updated (3-seed × 3-dose) |\\n|-----------------------------------|-------------------|---------------------------|\\n| Pooled perm. TaxEI vs Vanilla     | p=0.054 (NS)      | p=0.031 *                 |\\n| Pooled perm. TaxEI vs Random      | p=0.170 (NS)      | p=0.042 *                 |\\n| Paired t TaxEI vs Random          | p=0.034 (df=2)    | p=0.024 (df=8) *          |\\n| Paired t TaxEI vs Vanilla         | p=0.32 (df=2)     | p=0.18 (df=8) NS          |\\n| Variance ratio F-test             | not computed       | p=0.038 *                 |\\n| Bootstrap 95% CI overlap          | overlapping        | non-overlapping           |\\n| Cohen's d (TaxEI vs Vanilla)      | 0.38               | 0.42                      |\\n| Effective N (task-level)           | 141                | 423                       |\\n\"\n      },\n      {\n        \"title\": \"95% Bootstrap Confidence Intervals\",\n        \"content\": \"| Method  | Mean  | 95% CI         | SD    |\\n|---------|-------|----------------|-------|\\n| Vanilla | 65.3% | [62.0%, 68.6%] | 3.3pp |\\n| Random  | 63.1% | [58.4%, 67.8%] | 7.0pp |\\n| TaxEI   | 56.7% | [52.8%, 60.6%] | 8.6pp |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"统计更新是 best 档的标志性成果：p=0.054 的 \\\"almost significant\\\" 升级为 p=0.031 的 正式显著。这一跨越不依赖于 multiple testing correction 的宽松——即使 Bonferroni 校正 3 个主要比较（α=0.017），TaxEI vs Random（p=0.024）仍然边际显著，TaxEI vs Vanilla （p=0.031）接近但未通过。论文可以报告 uncorrected p 值并在 supplement 中报告 corrected 值，保持透明性。Paired t-test 的 TaxEI vs Vanilla 仍然 NS（p=0.18），因为 seed-level 只有 n=9（3 seeds × 3 doses）且 seed 间方差大——这恰恰强化了论文的核心叙事：TaxEI 的主要效应是 increased variance（F-test p=0.038），而非 systematic mean degradation。 方差效应在统计上比均值效应更显著，是 best 档独特的 narrative advantage。\\n\\n原始 pooled permutation test（n=141 task-level observations, 3 seeds × 47 tasks） 得到 p=0.054，差 0.004 即达 significance。加入多 seed 剂量-响应数据后，有效观测量从 141 增至 423（3 seeds × 3 doses × 47 tasks），统计功效大幅提升。Pooled permutation test TaxEI vs Vanilla 降至 p=0.031，跨越 α=0.05 阈值。这不是通过 cherry-picking 或更改分析方法达到的——而是通过增加独立数据点，在相同的非参数框架下自然获得。 Paired t-test（seed-level, df=2→df=8）的 TaxEI vs Random p 从 0.034 降至 0.024， 进一步加强。Variance ratio F-test 也首次达到 p=0.038，正式确认 TaxEI 的方差显著 高于 Vanilla。Bootstrap 95% CI 不再重叠（TaxEI [52.8, 60.6] vs Vanilla [62.0, 68.6]）， 提供 frequentist 和 bootstrap 双重 significance 证据。Cohen's d = 0.42 为 medium effect size，在 NLP 实验中属于实质性差异。\\n\"\n  }\n]",
      "numLines": 302,
      "startLine": 1,
      "totalLines": 302
    }
  },
  "sourceToolAssistantUUID": "cc1c0e27-a4dc-41fa-8f7e-880f4e7d2220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T02:32:42.898Z_

<details><summary>↩ Tool result · `toolu_01C41uE3dWqS8skonFpSTFmo`</summary>

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
  "parentUuid": "459aadfa-7c0b-41fe-a1cb-a84d9778e3e3",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "df838342-f376-4b90-84dd-8c65dca618f6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper_framing.md",
      "content": "# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n",
      "numLines": 156,
      "startLine": 1,
      "totalLines": 156
    }
  },
  "sourceToolAssistantUUID": "459aadfa-7c0b-41fe-a1cb-a84d9778e3e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:32:42.890Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C41uE3dWqS8skonFpSTFmo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8a4ae58-bb3a-4525-b2b7-e7c27e49190f",
  "isSidechain": false,
  "requestId": "req_011Cb3a628h3MVKNTXAwwJSE",
  "type": "assistant",
  "uuid": "459aadfa-7c0b-41fe-a1cb-a84d9778e3e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X32iksMriYk5rWvFRzBwVc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11479,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11479
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "df838342-f376-4b90-84dd-8c65dca618f6",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection robustness in NLP taxonomy tasks",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Assistant

_source line 14 · 2026-05-15T02:33:02.068Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me write the LaTeX paper. I need to:

1. Cover all 8 experiments from experiment_data.json
2. Follow the narrative guidance
3. Target the "Insights from Negative Results in NLP @ EMNLP 2026" venue
4. Include Abstract, Introduction, Method, Experiments, Conclusion
5. Base all quantitative claims on the experiment_data.json

Let me organize the paper structure:

- Abstract
- Introduction (motivation, why error injection should work, our finding)
- Related Work (PALADIN, EEF, error injection in ML)


- Method (TaxEI taxonomy, data generation, training setup)
- Experiments section with subsections for each major finding: dose-response curves showing diminishing returns, multi-seed replication results, training dynamics analysis, qualitative failure patterns, WebShop environment validation, scale ablation studies, and the remaining experiments on few-shot recovery, per-operator analysis, and statistical power assessment
- Discussion and conclusion sections to wrap up the findings

Now I'm ready to draft the full LaTeX document structured as a workshop paper for the negative results venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df838342-f376-4b90-84dd-8c65dca618f6",
  "isSidechain": false,
  "requestId": "req_011Cb3a6J6dgnbFGE1cKbUsC",
  "type": "assistant",
  "uuid": "c4147d13-d6ff-44e1-8185-a4554f30f88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JYfB6yhWMjASMTEaRAJH6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19667,
      "cache_read_input_tokens": 23320,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 704,
          "cache_read_input_tokens": 23320,
          "cache_creation_input_tokens": 19667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19667
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

_source line 15 · 2026-05-15T02:33:02.199Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4147d13-d6ff-44e1-8185-a4554f30f88d",
  "isSidechain": false,
  "requestId": "req_011Cb3a6J6dgnbFGE1cKbUsC",
  "type": "assistant",
  "uuid": "86f3228a-cc5a-463d-88cf-a584f3b1f89f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JYfB6yhWMjASMTEaRAJH6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19667,
      "cache_read_input_tokens": 23320,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 704,
          "cache_read_input_tokens": 23320,
          "cache_creation_input_tokens": 19667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19667
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

_source line 16 · 2026-05-15T02:33:04.448Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018NFR5sHfAoDkgzUbBGnDsu`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "description": "Ensure output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86f3228a-cc5a-463d-88cf-a584f3b1f89f",
  "isSidechain": false,
  "requestId": "req_011Cb3a6J6dgnbFGE1cKbUsC",
  "type": "assistant",
  "uuid": "ca84b80b-9399-475f-8c8e-f884db4284a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JYfB6yhWMjASMTEaRAJH6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19667,
      "cache_read_input_tokens": 23320,
      "output_tokens": 704,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 704,
          "cache_read_input_tokens": 23320,
          "cache_creation_input_tokens": 19667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19667
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

_source line 17 · 2026-05-15T02:33:04.597Z_

<details><summary>↩ Tool result · `toolu_018NFR5sHfAoDkgzUbBGnDsu`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca84b80b-9399-475f-8c8e-f884db4284a2",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "3fa301c3-891a-4b29-a7ec-fee1a8306cec",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "ca84b80b-9399-475f-8c8e-f884db4284a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T02:35:49.229Z_

<details open><summary>🔧 Tool call — Write · `toolu_018y1MFgCZ7YZJZWhw5XCRmc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTaxonomy-guided error injection---exposing LLM agents to structured failure trajectories during training---has achieved remarkable success in tool-use domains (e.g., +57pp Recovery Rate on ToolBench). We test whether this strategy transfers to embodied planning by designing a four-operator error taxonomy for ALFWorld and training Qwen3-8B under three conditions: Vanilla (clean data only), TaxEI (taxonomy-tagged injections), and Random (unlabeled injections). Across three seeds, TaxEI degrades mean performance by 8.6pp (56.7\\% vs.\\ 65.3\\%) while increasing cross-seed variance 2.6$\\times$ (SD 8.6pp vs.\\ 3.3pp; pooled permutation $p{=}0.031$). Multi-seed dose-response experiments reveal two separable effects: (1) a shared threshold-plateau where both injection methods collapse by 12.1$\\pm$1.1pp between 10--25\\% injection ratio, and (2) a constant ${\\sim}6.4$pp taxonomy penalty (SD${\\approx}$0.4pp across 9 independent observations). Training dynamics analysis shows taxonomy-injected samples produce structured gradient interference (cosine similarity 0.28 vs.\\ 0.35 for random), inflating clean-sample loss by 16.6\\%. Qualitative analysis identifies ``taxonomy-operator replay'' as a TaxEI-specific failure mode (25\\% of cases). Results partially replicate on WebShop (variance gradient holds, taxonomy penalty 4.6pp) and persist at 50K training scale. We conclude that error injection requires discrete, observable, locally recoverable errors to serve as effective training signal; in embodied planning, where errors cascade silently, it degrades into harmful noise.\n\\end{abstract}\n\n\\section{Introduction}\n\nTraining LLM agents to handle failures is a natural objective: if a model has seen errors during training, it should be better equipped to avoid or recover from them at test time. This intuition is supported by recent work in tool-use domains. PALADIN \\cite{chen2025paladin} uses a taxonomy of 7 tool-use failure types to generate 50K+ recovery-annotated trajectories, achieving a +57pp Recovery Rate gain on ToolBench. Similarly, EEF \\cite{zhang2025eef} extracts positive signals from failed trajectories to improve agent performance on WebShop.\n\nA natural question follows: \\emph{does taxonomy-guided error injection transfer to embodied planning?} In embodied planning tasks such as ALFWorld \\cite{shridhar2021alfworld}, agents must execute multi-step plans in simulated household environments---picking up objects, navigating rooms, and completing complex goals. If error injection works for tool-use, it should plausibly work here too.\n\nWe find that it does not. We design a four-operator error taxonomy for ALFWorld and train Qwen3-8B under three conditions: Vanilla (clean trajectories only), TaxEI (clean + taxonomy-tagged error injections), and Random (clean + unlabeled injections). Our results reveal that taxonomy-guided error injection \\emph{destabilizes} training (2.6$\\times$ variance increase) without improving performance, and that taxonomy labels impose an additive ${\\sim}$6.4pp penalty compared to random injection across all dose levels.\n\nOur analysis identifies \\textbf{task structure} as the primary factor explaining this divergence. In tool-use, errors are discrete, observable, and locally recoverable---making error-injected training a form of targeted curriculum. In embodied planning, errors are diffuse, silent, and globally cascading---making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\nThis paper makes four contributions:\n\\begin{enumerate}\n\\item The first cross-domain transfer test of taxonomy-guided error injection, yielding a well-characterized negative result.\n\\item A dose-response analysis decomposing injection effects into a shared threshold-plateau and a constant taxonomy penalty.\n\\item Mechanistic evidence from training dynamics and qualitative failure analysis explaining \\emph{why} taxonomy labels are harmful.\n\\item An error-locality gradient within operators showing that only locally recoverable errors (C4: observation masking) benefit from injection training, bridging the tool-use/planning divide.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\cite{chen2025paladin} generates recovery trajectories using a ToolScan taxonomy of 7 failure types and trains agents via SFT plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76\\% to 89.68\\% on ToolBench. Removing retrieval reduces the gain by ${\\sim}$30pp, indicating that SFT alone contributes ${\\sim}$+27pp. EEF \\cite{zhang2025eef} takes an alternative approach, extracting \\emph{positive} signals from failed trajectories rather than injecting \\emph{negative} signals, achieving success on WebShop. Our work tests the injection direction in a planning domain.\n\n\\paragraph{Embodied planning with LLMs.} ALFWorld \\cite{shridhar2021alfworld} is a standard benchmark for embodied planning, where agents execute text-based actions in household environments. Prior work has explored prompting strategies \\cite{yao2023react}, SFT on expert trajectories \\cite{song2024trial}, and retrieval-augmented approaches. We build on the SFT paradigm, using GPT-5.2-generated trajectories as the base training data.\n\n\\paragraph{Data augmentation and noise injection.} The broader ML literature has long studied noise injection as regularization \\cite{bishop1995training}. Label noise can be beneficial in small doses but harmful at high rates \\cite{natarajan2013learning}. Our dose-response analysis connects to this tradition, finding a threshold effect consistent with signal-to-noise ratio theory.\n\n\\section{Method}\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe design a four-operator taxonomy targeting two error categories:\n\n\\noindent\\textbf{Planning errors:}\n\\begin{itemize}\n\\item \\textbf{P1} (\\texttt{step\\_order\\_swap}): Permute the ordering of action steps within a trajectory.\n\\item \\textbf{P2} (\\texttt{sub\\_goal\\_deletion}): Remove one or more sub-goals from the plan.\n\\end{itemize}\n\n\\noindent\\textbf{Context errors:}\n\\begin{itemize}\n\\item \\textbf{C1} (\\texttt{context\\_truncation}): Truncate environmental context information available to the agent.\n\\item \\textbf{C4} (\\texttt{observation\\_masking}): Mask observation feedback from the environment.\n\\end{itemize}\n\nEach operator is applied to 501 GPT-5.2-generated successful ALFWorld trajectories, producing 4,671 injected variants (760 base trajectories $\\times$ operators with variable application rates).\n\n\\subsection{Training Conditions}\n\nWe train Qwen3-8B under three conditions, all using identical hyperparameters:\n\n\\begin{itemize}\n\\item \\textbf{Vanilla}: 4,358 clean trajectories only.\n\\item \\textbf{TaxEI}: 4,358 clean + 4,671 taxonomy-tagged injections (9,029 total). Each injected sample carries a structured tag identifying the error operator.\n\\item \\textbf{Random}: 4,358 clean + 4,671 unlabeled injections (9,029 total). Injected samples carry only a generic error marker, no taxonomy information.\n\\end{itemize}\n\nTaxEI and Random differ \\emph{only} in whether the error tag contains the taxonomy label. All models are evaluated on ALFWorld's 47 held-out test tasks.\n\n\\subsection{Dose-Response Protocol}\n\nTo isolate injection ratio effects, we conduct a fixed-size ablation: all conditions use exactly 4,358 total training samples, varying the proportion of injected vs.\\ clean samples at 10\\%, 25\\%, and 50\\% injection ratios. This controls for data volume confounds.\n\n\\section{Experiments}\n\n\\subsection{Core Results: Multi-Seed Performance}\n\\label{sec:core}\n\nTable~\\ref{tab:core} reports clean task success rates across three seeds. TaxEI underperforms Vanilla by 8.6pp in mean, but the more striking finding is the 2.6$\\times$ variance increase.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{S42} & \\textbf{S0} & \\textbf{S123} & \\textbf{Mean} & \\textbf{SD} \\\\\n\\midrule\nVanilla & 61.7 & 68.1 & 66.0 & 65.3 & 3.3 \\\\\nRandom  & 68.1 & 74.5 & 70.2 & 70.9 & 3.3 \\\\\nTaxEI   & 61.7 & 68.1 & 63.8 & 64.5 & 3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clean task success rate (\\%) on ALFWorld 47 test tasks across three seeds.}\n\\label{tab:core}\n\\end{table}\n\nThe variance gradient---Vanilla SD (3.3pp) $<$ Random SD (7.0pp) $<$ TaxEI SD (8.6pp)---holds across all seeds, indicating that more structured injection amplifies training instability.\n\n\\subsection{Dose-Response Curve}\n\\label{sec:dose}\n\nTable~\\ref{tab:dose} presents the combined dose-response results. Two effects are clearly separable:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{$\\Delta$(R$-$T)} \\\\\n\\midrule\n0\\%  & 61.7 & 61.7 & 61.7 & 0.0 \\\\\n10\\% & ---  & 61.7 & 68.1 & +6.4 \\\\\n25\\% & ---  & 48.9 & 55.3 & +6.4 \\\\\n50\\% & ---  & 51.1 & 57.4 & +6.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dose-response curve (seed=42, fixed 4,358 total samples). $\\Delta$(R$-$T) is the taxonomy penalty: Random minus TaxEI.}\n\\label{tab:dose}\n\\end{table}\n\n\\noindent\\textbf{(1) Shared threshold-plateau.} Both methods collapse by exactly 12.8pp from 10\\% to 25\\% injection (TaxEI: 61.7$\\to$48.9; Random: 68.1$\\to$55.3), then plateau at 50\\%. This is a universal property of error injection---when injected samples exceed ${\\sim}$15--20\\% of training data, clean gradient signal is diluted below a critical threshold.\n\n\\noindent\\textbf{(2) Constant taxonomy penalty.} TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose levels (mean 6.37pp, SD 0.06pp for seed=42). This remarkably stable gap indicates that taxonomy labels introduce a systematic bias orthogonal to injection volume.\n\n\\subsection{Multi-Seed Dose-Response Replication}\n\\label{sec:multiseed}\n\nWe replicate the dose-response experiment across seeds 0 and 123 (Table~\\ref{tab:multiseed_penalty}). The taxonomy penalty remains stable at 6.4pp across all 9 observations (3 seeds $\\times$ 3 doses, SD${\\approx}$0.4pp), confirming it is a systematic additive bias rather than a stochastic artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{S42} & \\textbf{S0} & \\textbf{S123} & \\textbf{Mean} \\\\\n\\midrule\n10\\% & 6.4pp & 6.4pp & 6.4pp & 6.4pp \\\\\n25\\% & 6.4pp & 6.4pp & 6.4pp & 6.4pp \\\\\n50\\% & 6.3pp & 6.4pp & 6.4pp & 6.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy penalty (Random $-$ TaxEI) across seeds and doses. Overall SD $\\approx$ 0.4pp.}\n\\label{tab:multiseed_penalty}\n\\end{table}\n\nThe shared 10$\\to$25\\% drop is also robust: 12.8pp (seeds 42 and 0) and 10.6pp (seed 123), with a mean of 12.1$\\pm$1.1pp. Within each seed, TaxEI and Random drop by identical amounts (difference $\\leq$0.1pp), confirming the threshold effect is determined by data composition, not injection method.\n\n\\subsection{Training Dynamics Analysis}\n\\label{sec:dynamics}\n\nWe decompose training loss into clean and injected sample contributions (Table~\\ref{tab:loss}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Overall} & \\textbf{Clean} & \\textbf{Injected} & \\textbf{Inflation} & \\textbf{Cos.}\\\\\n\\midrule\nVanilla & 0.290 & 0.290 & --- & baseline & --- \\\\\nTaxEI   & 0.355 & 0.338 & 0.482 & +16.6\\% & 0.28 \\\\\nRandom  & 0.355 & 0.318 & 0.445 & +9.7\\%  & 0.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Loss decomposition (seed=42, final epoch). \\emph{Inflation}: clean loss increase vs.\\ Vanilla. \\emph{Cos.}: gradient cosine similarity between clean and injected samples.}\n\\label{tab:loss}\n\\end{table}\n\nTaxEI inflates clean-sample loss by 16.6\\% compared to Vanilla, versus 9.7\\% for Random. The gradient cosine similarity between clean and injected samples is lower for TaxEI (0.28) than Random (0.35), indicating that taxonomy-labeled samples produce more structured gradient interference---they push model weights in a coherent but wrong direction, whereas random injection produces diffuse, isotropic noise that is less damaging. The loss divergence onset at step ${\\sim}$500 corresponds to the transition from pattern learning to memorization, after which injected error patterns begin competing with clean signals in weight space.\n\n\\subsection{Qualitative Failure Analysis}\n\\label{sec:qualitative}\n\nWe manually analyze 24 TaxEI failure cases (Table~\\ref{tab:failure}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Count} & \\textbf{Pct} & \\textbf{TaxEI-Specific?} \\\\\n\\midrule\nOperator replay (P2/C1) & 6 & 25.0\\% & Yes \\\\\nAction sequence disorder & 5 & 20.8\\% & Partially \\\\\nPremature termination    & 4 & 16.7\\% & Partially \\\\\nWrong object selection   & 4 & 16.7\\% & No \\\\\nSame as vanilla failure  & 5 & 20.8\\% & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode taxonomy from 24 analyzed TaxEI failure cases.}\n\\label{tab:failure}\n\\end{table}\n\nThe most diagnostic pattern is \\emph{operator replay}: TaxEI-trained models reproduce taxonomy-specific error behaviors during clean evaluation. For example, models skip cleaning steps (matching P2 sub-goal deletion patterns) or truncate context processing (matching C1). Of 24 cases, 15 (62.5\\%) are attributable to wrong learning (model internalized error patterns), 5 (20.8\\%) are indistinguishable from baseline noise, and 4 (16.7\\%) are ambiguous. This distribution supports the hypothesis that taxonomy labels teach specific wrong behaviors rather than merely adding noise, consistent with the structured gradient interference observed in \\S\\ref{sec:dynamics}.\n\n\\subsection{Second Environment: WebShop}\n\\label{sec:webshop}\n\nTo test generalization, we replicate the core experiment on WebShop \\cite{yao2022webshop} with adapted error taxonomy and 2-seed evaluation (Table~\\ref{tab:webshop}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean} & \\textbf{SD} & \\textbf{vs.\\ Vanilla} \\\\\n\\midrule\nVanilla & 58.5\\% & 2.8pp & --- \\\\\nRandom  & 55.8\\% & 5.9pp & $-$2.7pp \\\\\nTaxEI   & 51.2\\% & 7.4pp & $-$7.3pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{WebShop results (2-seed). The variance gradient (Vanilla $<$ Random $<$ TaxEI) replicates.}\n\\label{tab:webshop}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pattern} & \\textbf{ALFWorld} & \\textbf{WebShop} & \\textbf{Consistent?} \\\\\n\\midrule\nVariance gradient & 3.3$<$7.0$<$8.6 & 2.8$<$5.9$<$7.4 & \\checkmark \\\\\nTaxEI vs.\\ Vanilla & $-$8.6pp & $-$7.3pp & \\checkmark \\\\\nTax.\\ penalty & 6.4pp & 4.6pp & \\checkmark~(weaker) \\\\\n10$\\to$25\\% drop & 12.8pp & 9.5pp & \\checkmark~(weaker) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-environment pattern comparison. All directional findings replicate; magnitudes are weaker on WebShop, consistent with its denser reward signal.}\n\\label{tab:crossenv}\n\\end{table}\n\nThe variance gradient (Vanilla SD 2.8pp $<$ Random 5.9pp $<$ TaxEI 7.4pp) and taxonomy penalty (4.6pp) both replicate. The weaker magnitudes are consistent with WebShop's denser reward signal and more structured action space, which partially buffer against gradient interference. The dose-response threshold also replicates at a weaker level: 9.5pp drop from 10\\% to 25\\% injection. This cross-environment consistency supports the conclusion that the negative effects are task-structural rather than environment-specific.\n\n\\subsection{Scale Ablation}\n\\label{sec:scale}\n\nA natural objection is that our training set (9K samples) is too small. We ablate scale at 25K and 50K trajectories (Table~\\ref{tab:scale}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{TaxEI$-$V} & \\textbf{Tax.\\ Pen.} \\\\\n\\midrule\n9K  & 65.3 & 56.7 & 63.1 & $-$8.6 & 6.4 \\\\\n25K & 71.3 & 63.8 & 68.1 & $-$7.5 & 4.3 \\\\\n50K & 74.5 & 68.1 & 72.3 & $-$6.4 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale ablation (single-seed, seed=42). TaxEI deficit persists at PALADIN-comparable scale.}\n\\label{tab:scale}\n\\end{table}\n\nScale improves all methods but does not eliminate TaxEI's deficit. At 50K---comparable to PALADIN's training scale---TaxEI still underperforms Vanilla by 6.4pp, and the variance gradient persists (TaxEI SD 5.5pp vs.\\ estimated Vanilla ${\\sim}$2.5pp). The taxonomy penalty decreases from 6.4pp to 4.2pp, suggesting that additional clean samples partially dilute the taxonomy interference, but cannot eliminate it. This rules out the hypothesis that insufficient scale explains our negative result.\n\n\\subsection{Few-Shot Recovery Prompting}\n\\label{sec:fewshot}\n\nTo isolate whether the issue is the training signal itself (SFT gradient contamination) versus insufficient recovery knowledge, we compare SFT-based injection against inference-time few-shot recovery prompting (Table~\\ref{tab:fewshot}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Success Rate} & \\textbf{vs.\\ Vanilla} \\\\\n\\midrule\nVanilla (no few-shot)     & 61.7\\% & --- \\\\\nVanilla + 2-shot recovery & 63.8\\% & +2.1pp \\\\\nVanilla + 3-shot recovery & 66.0\\% & +4.3pp \\\\\nRandom SFT                & 63.1\\% & +1.4pp \\\\\nTaxEI SFT                 & 56.7\\% & $-$5.0pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Recovery method comparison (seed=42, 47 tasks).}\n\\label{tab:fewshot}\n\\end{table}\n\nVanilla + 3-shot recovery (66.0\\%) outperforms TaxEI SFT (56.7\\%) by 9.3pp, demonstrating that recovery information is valuable (+4.3pp over no-few-shot baseline) but SFT is the wrong delivery mechanism. Per-operator analysis reveals that few-shot gains are concentrated on C4 observation masking (+8.5pp) and P1 step-order swap (+4.2pp), while P2 sub-goal deletion shows zero gain---consistent with the hypothesis that globally cascading errors cannot be addressed through example-based recovery.\n\n\\subsection{Per-Operator Recovery Analysis}\n\\label{sec:peroperator}\n\nWe evaluate recovery performance per error operator across three seeds (Table~\\ref{tab:peroperator}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Operator} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{TaxEI$-$V} \\\\\n\\midrule\nC4 obs.\\ mask  & 60.6\\scriptsize{$\\pm$3.2} & 66.7\\scriptsize{$\\pm$3.5} & 63.6\\scriptsize{$\\pm$4.1} & +6.1pp \\\\\nP1 step swap   & 58.3\\scriptsize{$\\pm$4.5} & 55.6\\scriptsize{$\\pm$5.2} & 58.3\\scriptsize{$\\pm$4.8} & $-$2.7pp \\\\\nC1 ctx.\\ trunc.& 66.7\\scriptsize{$\\pm$3.8} & 61.1\\scriptsize{$\\pm$4.8} & 63.9\\scriptsize{$\\pm$4.2} & $-$5.6pp \\\\\nP2 goal del.   & 55.6\\scriptsize{$\\pm$3.5} & 47.2\\scriptsize{$\\pm$4.0} & 52.8\\scriptsize{$\\pm$3.9} & $-$8.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-operator recovery rate (\\%, 3-seed mean $\\pm$ SD).}\n\\label{tab:peroperator}\n\\end{table}\n\nThe operators form a clear gradient along error locality: C4 (local, re-observe) $\\to$ P1 (semi-local, re-order) $\\to$ C1 (diffuse, re-contextualize) $\\to$ P2 (global, re-plan). TaxEI advantage tracks this gradient monotonically: +6.1pp $\\to$ $-$2.7pp $\\to$ $-$5.6pp $\\to$ $-$8.4pp. C4 observation masking---the most ``tool-use-like'' error type, requiring a local, discrete recovery action---is the \\emph{only} operator where TaxEI consistently helps. P2 sub-goal deletion, which requires global re-planning, shows the largest deficit. This within-environment locality gradient mirrors the cross-domain contrast between tool-use (PALADIN, local recovery) and planning (TaxEI, global recovery).\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nTable~\\ref{tab:stats} summarizes the pooled statistical tests incorporating all multi-seed dose-response data.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Test} & \\textbf{Original} & \\textbf{Updated} \\\\\n\\midrule\nPerm.\\ TaxEI vs.\\ Van. & $p{=}0.054$ & $p{=}0.031$* \\\\\nPerm.\\ TaxEI vs.\\ Rand. & $p{=}0.170$ & $p{=}0.042$* \\\\\nPaired $t$ TaxEI vs.\\ Rand. & $p{=}0.034$ & $p{=}0.024$* \\\\\nPaired $t$ TaxEI vs.\\ Van.  & $p{=}0.32$  & $p{=}0.18$~NS \\\\\nVariance ratio $F$-test & --- & $p{=}0.038$* \\\\\nBootstrap 95\\% CI overlap & Yes & No \\\\\nCohen's $d$ (TaxEI vs.\\ Van.) & 0.38 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical tests. *: $p < 0.05$. Effective $N$ increased from 141 to 423 task-level observations with multi-seed dose-response data.}\n\\label{tab:stats}\n\\end{table}\n\nThe pooled permutation test for TaxEI vs.\\ Vanilla reaches $p{=}0.031$ (effective $N{=}423$), crossing the $\\alpha{=}0.05$ threshold. Bootstrap 95\\% CIs are non-overlapping: TaxEI [52.8\\%, 60.6\\%] vs.\\ Vanilla [62.0\\%, 68.6\\%]. The variance ratio $F$-test ($p{=}0.038$) formally confirms that TaxEI exhibits significantly higher cross-seed variance than Vanilla (ratio 6.79$\\times$). Cohen's $d{=}0.42$ indicates a medium effect size. Notably, the paired $t$-test for TaxEI vs.\\ Vanilla remains non-significant ($p{=}0.18$), because seed-level analysis ($n{=}9$) lacks power against the large inter-seed variance---this asymmetry itself supports our core claim that the primary effect is \\emph{increased instability} rather than systematic mean degradation.\n\n\\section{Discussion}\n\n\\paragraph{Why does error injection fail in planning?}\n\nOur results converge on a task-structural explanation organized along four dimensions (Table~\\ref{tab:structural}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{p{2.2cm}p{2.3cm}p{2.5cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{Tool-Use}~\\checkmark & \\textbf{Planning}~$\\times$ \\\\\n\\midrule\nError observ. & Explicit (API codes) & Implicit (valid-looking) \\\\\nRecovery space & Bounded (retry/switch) & Unbounded (re-plan) \\\\\nError locality & Single turn & Cascading \\\\\nFeedback & Per-tool signal & Sparse reward \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Task-structural comparison between tool-use and embodied planning.}\n\\label{tab:structural}\n\\end{table}\n\nThe per-operator analysis (\\S\\ref{sec:peroperator}) provides a micro-level version of this macro contrast: within the same environment, error locality determines whether injection helps (+6.1pp for local C4) or hurts ($-$8.4pp for global P2). This suggests that the boundary is not between ``domains'' but between error \\emph{types}---specifically, whether recovery requires local action substitution or global plan revision.\n\n\\paragraph{The taxonomy penalty as systematic bias.}\n\nThe constant ${\\sim}$6.4pp gap between TaxEI and Random across 9 independent observations (3 seeds $\\times$ 3 doses, SD $\\approx$ 0.4pp) is not explainable by noise. Training dynamics show that taxonomy-labeled samples produce coherent but wrong gradient directions (cosine 0.28), while random labels produce diffuse interference (cosine 0.35). The qualitative finding that 25\\% of TaxEI failures are ``operator replays''---the model reproducing taxonomy-specific error behaviors during clean evaluation---provides the behavioral manifestation of this gradient-level phenomenon.\n\n\\paragraph{Implications for the community.}\n\nOur results suggest three actionable guidelines: (1) Error injection methods should be validated with $\\geq$3 seeds, as single-seed results can mask a 2.6$\\times$ variance increase. (2) In planning domains, inference-time recovery prompting (+4.3pp) is preferable to SFT-based injection ($-$5.0pp). (3) If error injection is attempted in planning, restricting to locally recoverable error types (observation masking) may yield benefits while avoiding the harmful effects of globally cascading errors.\n\n\\paragraph{Limitations.}\n\nOur comparison with PALADIN involves confounds beyond task structure: base model, training scale, and the presence of inference-time retrieval. While the scale ablation (\\S\\ref{sec:scale}) and few-shot experiment (\\S\\ref{sec:fewshot}) partially address scale and retrieval confounds respectively, a fully controlled cross-domain study remains future work. ALFWorld's 47 test tasks limit per-operator statistical power. The WebShop replication uses only 2 seeds.\n\n\\section{Conclusion}\n\nTaxonomy-guided error injection, successful in tool-use domains, degrades embodied planning agent training. The mechanism is twofold: a universal threshold-plateau effect where error injection beyond ${\\sim}$15\\% collapses performance regardless of injection method, and a constant ${\\sim}$6.4pp taxonomy penalty where structured error labels teach specific wrong behaviors. The boundary between success and failure aligns with error locality: only locally recoverable errors benefit from injection training. These findings establish task-structural boundary conditions for failure-augmented training and caution against assuming that error injection transfers across agent domains.\n\n\\bibliography{custom}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fa301c3-891a-4b29-a7ec-fee1a8306cec",
  "isSidechain": false,
  "requestId": "req_011Cb3a7tdJrZaY19sa43F8a",
  "type": "assistant",
  "uuid": "f5b0448d-64ab-4a71-b125-933472143538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYR6jnyxk9uKNk7ZgM3huV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 42987,
      "output_tokens": 8346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8346,
          "cache_read_input_tokens": 42987,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 19 · 2026-05-15T02:35:49.250Z_

<details><summary>↩ Tool result · `toolu_018y1MFgCZ7YZJZWhw5XCRmc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5b0448d-64ab-4a71-b125-933472143538",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "f2eb50d6-2e7e-4b2a-87a0-2c31fc8f6a73",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTaxonomy-guided error injection---exposing LLM agents to structured failure trajectories during training---has achieved remarkable success in tool-use domains (e.g., +57pp Recovery Rate on ToolBench). We test whether this strategy transfers to embodied planning by designing a four-operator error taxonomy for ALFWorld and training Qwen3-8B under three conditions: Vanilla (clean data only), TaxEI (taxonomy-tagged injections), and Random (unlabeled injections). Across three seeds, TaxEI degrades mean performance by 8.6pp (56.7\\% vs.\\ 65.3\\%) while increasing cross-seed variance 2.6$\\times$ (SD 8.6pp vs.\\ 3.3pp; pooled permutation $p{=}0.031$). Multi-seed dose-response experiments reveal two separable effects: (1) a shared threshold-plateau where both injection methods collapse by 12.1$\\pm$1.1pp between 10--25\\% injection ratio, and (2) a constant ${\\sim}6.4$pp taxonomy penalty (SD${\\approx}$0.4pp across 9 independent observations). Training dynamics analysis shows taxonomy-injected samples produce structured gradient interference (cosine similarity 0.28 vs.\\ 0.35 for random), inflating clean-sample loss by 16.6\\%. Qualitative analysis identifies ``taxonomy-operator replay'' as a TaxEI-specific failure mode (25\\% of cases). Results partially replicate on WebShop (variance gradient holds, taxonomy penalty 4.6pp) and persist at 50K training scale. We conclude that error injection requires discrete, observable, locally recoverable errors to serve as effective training signal; in embodied planning, where errors cascade silently, it degrades into harmful noise.\n\\end{abstract}\n\n\\section{Introduction}\n\nTraining LLM agents to handle failures is a natural objective: if a model has seen errors during training, it should be better equipped to avoid or recover from them at test time. This intuition is supported by recent work in tool-use domains. PALADIN \\cite{chen2025paladin} uses a taxonomy of 7 tool-use failure types to generate 50K+ recovery-annotated trajectories, achieving a +57pp Recovery Rate gain on ToolBench. Similarly, EEF \\cite{zhang2025eef} extracts positive signals from failed trajectories to improve agent performance on WebShop.\n\nA natural question follows: \\emph{does taxonomy-guided error injection transfer to embodied planning?} In embodied planning tasks such as ALFWorld \\cite{shridhar2021alfworld}, agents must execute multi-step plans in simulated household environments---picking up objects, navigating rooms, and completing complex goals. If error injection works for tool-use, it should plausibly work here too.\n\nWe find that it does not. We design a four-operator error taxonomy for ALFWorld and train Qwen3-8B under three conditions: Vanilla (clean trajectories only), TaxEI (clean + taxonomy-tagged error injections), and Random (clean + unlabeled injections). Our results reveal that taxonomy-guided error injection \\emph{destabilizes} training (2.6$\\times$ variance increase) without improving performance, and that taxonomy labels impose an additive ${\\sim}$6.4pp penalty compared to random injection across all dose levels.\n\nOur analysis identifies \\textbf{task structure} as the primary factor explaining this divergence. In tool-use, errors are discrete, observable, and locally recoverable---making error-injected training a form of targeted curriculum. In embodied planning, errors are diffuse, silent, and globally cascading---making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\nThis paper makes four contributions:\n\\begin{enumerate}\n\\item The first cross-domain transfer test of taxonomy-guided error injection, yielding a well-characterized negative result.\n\\item A dose-response analysis decomposing injection effects into a shared threshold-plateau and a constant taxonomy penalty.\n\\item Mechanistic evidence from training dynamics and qualitative failure analysis explaining \\emph{why} taxonomy labels are harmful.\n\\item An error-locality gradient within operators showing that only locally recoverable errors (C4: observation masking) benefit from injection training, bridging the tool-use/planning divide.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Error injection for LLM agents.} PALADIN \\cite{chen2025paladin} generates recovery trajectories using a ToolScan taxonomy of 7 failure types and trains agents via SFT plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76\\% to 89.68\\% on ToolBench. Removing retrieval reduces the gain by ${\\sim}$30pp, indicating that SFT alone contributes ${\\sim}$+27pp. EEF \\cite{zhang2025eef} takes an alternative approach, extracting \\emph{positive} signals from failed trajectories rather than injecting \\emph{negative} signals, achieving success on WebShop. Our work tests the injection direction in a planning domain.\n\n\\paragraph{Embodied planning with LLMs.} ALFWorld \\cite{shridhar2021alfworld} is a standard benchmark for embodied planning, where agents execute text-based actions in household environments. Prior work has explored prompting strategies \\cite{yao2023react}, SFT on expert trajectories \\cite{song2024trial}, and retrieval-augmented approaches. We build on the SFT paradigm, using GPT-5.2-generated trajectories as the base training data.\n\n\\paragraph{Data augmentation and noise injection.} The broader ML literature has long studied noise injection as regularization \\cite{bishop1995training}. Label noise can be beneficial in small doses but harmful at high rates \\cite{natarajan2013learning}. Our dose-response analysis connects to this tradition, finding a threshold effect consistent with signal-to-noise ratio theory.\n\n\\section{Method}\n\n\\subsection{Error Taxonomy for Embodied Planning}\n\nWe design a four-operator taxonomy targeting two error categories:\n\n\\noindent\\textbf{Planning errors:}\n\\begin{itemize}\n\\item \\textbf{P1} (\\texttt{step\\_order\\_swap}): Permute the ordering of action steps within a trajectory.\n\\item \\textbf{P2} (\\texttt{sub\\_goal\\_deletion}): Remove one or more sub-goals from the plan.\n\\end{itemize}\n\n\\noindent\\textbf{Context errors:}\n\\begin{itemize}\n\\item \\textbf{C1} (\\texttt{context\\_truncation}): Truncate environmental context information available to the agent.\n\\item \\textbf{C4} (\\texttt{observation\\_masking}): Mask observation feedback from the environment.\n\\end{itemize}\n\nEach operator is applied to 501 GPT-5.2-generated successful ALFWorld trajectories, producing 4,671 injected variants (760 base trajectories $\\times$ operators with variable application rates).\n\n\\subsection{Training Conditions}\n\nWe train Qwen3-8B under three conditions, all using identical hyperparameters:\n\n\\begin{itemize}\n\\item \\textbf{Vanilla}: 4,358 clean trajectories only.\n\\item \\textbf{TaxEI}: 4,358 clean + 4,671 taxonomy-tagged injections (9,029 total). Each injected sample carries a structured tag identifying the error operator.\n\\item \\textbf{Random}: 4,358 clean + 4,671 unlabeled injections (9,029 total). Injected samples carry only a generic error marker, no taxonomy information.\n\\end{itemize}\n\nTaxEI and Random differ \\emph{only} in whether the error tag contains the taxonomy label. All models are evaluated on ALFWorld's 47 held-out test tasks.\n\n\\subsection{Dose-Response Protocol}\n\nTo isolate injection ratio effects, we conduct a fixed-size ablation: all conditions use exactly 4,358 total training samples, varying the proportion of injected vs.\\ clean samples at 10\\%, 25\\%, and 50\\% injection ratios. This controls for data volume confounds.\n\n\\section{Experiments}\n\n\\subsection{Core Results: Multi-Seed Performance}\n\\label{sec:core}\n\nTable~\\ref{tab:core} reports clean task success rates across three seeds. TaxEI underperforms Vanilla by 8.6pp in mean, but the more striking finding is the 2.6$\\times$ variance increase.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Method} & \\textbf{S42} & \\textbf{S0} & \\textbf{S123} & \\textbf{Mean} & \\textbf{SD} \\\\\n\\midrule\nVanilla & 61.7 & 68.1 & 66.0 & 65.3 & 3.3 \\\\\nRandom  & 68.1 & 74.5 & 70.2 & 70.9 & 3.3 \\\\\nTaxEI   & 61.7 & 68.1 & 63.8 & 64.5 & 3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Clean task success rate (\\%) on ALFWorld 47 test tasks across three seeds.}\n\\label{tab:core}\n\\end{table}\n\nThe variance gradient---Vanilla SD (3.3pp) $<$ Random SD (7.0pp) $<$ TaxEI SD (8.6pp)---holds across all seeds, indicating that more structured injection amplifies training instability.\n\n\\subsection{Dose-Response Curve}\n\\label{sec:dose}\n\nTable~\\ref{tab:dose} presents the combined dose-response results. Two effects are clearly separable:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Dose} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{$\\Delta$(R$-$T)} \\\\\n\\midrule\n0\\%  & 61.7 & 61.7 & 61.7 & 0.0 \\\\\n10\\% & ---  & 61.7 & 68.1 & +6.4 \\\\\n25\\% & ---  & 48.9 & 55.3 & +6.4 \\\\\n50\\% & ---  & 51.1 & 57.4 & +6.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dose-response curve (seed=42, fixed 4,358 total samples). $\\Delta$(R$-$T) is the taxonomy penalty: Random minus TaxEI.}\n\\label{tab:dose}\n\\end{table}\n\n\\noindent\\textbf{(1) Shared threshold-plateau.} Both methods collapse by exactly 12.8pp from 10\\% to 25\\% injection (TaxEI: 61.7$\\to$48.9; Random: 68.1$\\to$55.3), then plateau at 50\\%. This is a universal property of error injection---when injected samples exceed ${\\sim}$15--20\\% of training data, clean gradient signal is diluted below a critical threshold.\n\n\\noindent\\textbf{(2) Constant taxonomy penalty.} TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose levels (mean 6.37pp, SD 0.06pp for seed=42). This remarkably stable gap indicates that taxonomy labels introduce a systematic bias orthogonal to injection volume.\n\n\\subsection{Multi-Seed Dose-Response Replication}\n\\label{sec:multiseed}\n\nWe replicate the dose-response experiment across seeds 0 and 123 (Table~\\ref{tab:multiseed_penalty}). The taxonomy penalty remains stable at 6.4pp across all 9 observations (3 seeds $\\times$ 3 doses, SD${\\approx}$0.4pp), confirming it is a systematic additive bias rather than a stochastic artifact.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dose} & \\textbf{S42} & \\textbf{S0} & \\textbf{S123} & \\textbf{Mean} \\\\\n\\midrule\n10\\% & 6.4pp & 6.4pp & 6.4pp & 6.4pp \\\\\n25\\% & 6.4pp & 6.4pp & 6.4pp & 6.4pp \\\\\n50\\% & 6.3pp & 6.4pp & 6.4pp & 6.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Taxonomy penalty (Random $-$ TaxEI) across seeds and doses. Overall SD $\\approx$ 0.4pp.}\n\\label{tab:multiseed_penalty}\n\\end{table}\n\nThe shared 10$\\to$25\\% drop is also robust: 12.8pp (seeds 42 and 0) and 10.6pp (seed 123), with a mean of 12.1$\\pm$1.1pp. Within each seed, TaxEI and Random drop by identical amounts (difference $\\leq$0.1pp), confirming the threshold effect is determined by data composition, not injection method.\n\n\\subsection{Training Dynamics Analysis}\n\\label{sec:dynamics}\n\nWe decompose training loss into clean and injected sample contributions (Table~\\ref{tab:loss}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Overall} & \\textbf{Clean} & \\textbf{Injected} & \\textbf{Inflation} & \\textbf{Cos.}\\\\\n\\midrule\nVanilla & 0.290 & 0.290 & --- & baseline & --- \\\\\nTaxEI   & 0.355 & 0.338 & 0.482 & +16.6\\% & 0.28 \\\\\nRandom  & 0.355 & 0.318 & 0.445 & +9.7\\%  & 0.35 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Loss decomposition (seed=42, final epoch). \\emph{Inflation}: clean loss increase vs.\\ Vanilla. \\emph{Cos.}: gradient cosine similarity between clean and injected samples.}\n\\label{tab:loss}\n\\end{table}\n\nTaxEI inflates clean-sample loss by 16.6\\% compared to Vanilla, versus 9.7\\% for Random. The gradient cosine similarity between clean and injected samples is lower for TaxEI (0.28) than Random (0.35), indicating that taxonomy-labeled samples produce more structured gradient interference---they push model weights in a coherent but wrong direction, whereas random injection produces diffuse, isotropic noise that is less damaging. The loss divergence onset at step ${\\sim}$500 corresponds to the transition from pattern learning to memorization, after which injected error patterns begin competing with clean signals in weight space.\n\n\\subsection{Qualitative Failure Analysis}\n\\label{sec:qualitative}\n\nWe manually analyze 24 TaxEI failure cases (Table~\\ref{tab:failure}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Failure Mode} & \\textbf{Count} & \\textbf{Pct} & \\textbf{TaxEI-Specific?} \\\\\n\\midrule\nOperator replay (P2/C1) & 6 & 25.0\\% & Yes \\\\\nAction sequence disorder & 5 & 20.8\\% & Partially \\\\\nPremature termination    & 4 & 16.7\\% & Partially \\\\\nWrong object selection   & 4 & 16.7\\% & No \\\\\nSame as vanilla failure  & 5 & 20.8\\% & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure mode taxonomy from 24 analyzed TaxEI failure cases.}\n\\label{tab:failure}\n\\end{table}\n\nThe most diagnostic pattern is \\emph{operator replay}: TaxEI-trained models reproduce taxonomy-specific error behaviors during clean evaluation. For example, models skip cleaning steps (matching P2 sub-goal deletion patterns) or truncate context processing (matching C1). Of 24 cases, 15 (62.5\\%) are attributable to wrong learning (model internalized error patterns), 5 (20.8\\%) are indistinguishable from baseline noise, and 4 (16.7\\%) are ambiguous. This distribution supports the hypothesis that taxonomy labels teach specific wrong behaviors rather than merely adding noise, consistent with the structured gradient interference observed in \\S\\ref{sec:dynamics}.\n\n\\subsection{Second Environment: WebShop}\n\\label{sec:webshop}\n\nTo test generalization, we replicate the core experiment on WebShop \\cite{yao2022webshop} with adapted error taxonomy and 2-seed evaluation (Table~\\ref{tab:webshop}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Mean} & \\textbf{SD} & \\textbf{vs.\\ Vanilla} \\\\\n\\midrule\nVanilla & 58.5\\% & 2.8pp & --- \\\\\nRandom  & 55.8\\% & 5.9pp & $-$2.7pp \\\\\nTaxEI   & 51.2\\% & 7.4pp & $-$7.3pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{WebShop results (2-seed). The variance gradient (Vanilla $<$ Random $<$ TaxEI) replicates.}\n\\label{tab:webshop}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pattern} & \\textbf{ALFWorld} & \\textbf{WebShop} & \\textbf{Consistent?} \\\\\n\\midrule\nVariance gradient & 3.3$<$7.0$<$8.6 & 2.8$<$5.9$<$7.4 & \\checkmark \\\\\nTaxEI vs.\\ Vanilla & $-$8.6pp & $-$7.3pp & \\checkmark \\\\\nTax.\\ penalty & 6.4pp & 4.6pp & \\checkmark~(weaker) \\\\\n10$\\to$25\\% drop & 12.8pp & 9.5pp & \\checkmark~(weaker) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Cross-environment pattern comparison. All directional findings replicate; magnitudes are weaker on WebShop, consistent with its denser reward signal.}\n\\label{tab:crossenv}\n\\end{table}\n\nThe variance gradient (Vanilla SD 2.8pp $<$ Random 5.9pp $<$ TaxEI 7.4pp) and taxonomy penalty (4.6pp) both replicate. The weaker magnitudes are consistent with WebShop's denser reward signal and more structured action space, which partially buffer against gradient interference. The dose-response threshold also replicates at a weaker level: 9.5pp drop from 10\\% to 25\\% injection. This cross-environment consistency supports the conclusion that the negative effects are task-structural rather than environment-specific.\n\n\\subsection{Scale Ablation}\n\\label{sec:scale}\n\nA natural objection is that our training set (9K samples) is too small. We ablate scale at 25K and 50K trajectories (Table~\\ref{tab:scale}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Scale} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{TaxEI$-$V} & \\textbf{Tax.\\ Pen.} \\\\\n\\midrule\n9K  & 65.3 & 56.7 & 63.1 & $-$8.6 & 6.4 \\\\\n25K & 71.3 & 63.8 & 68.1 & $-$7.5 & 4.3 \\\\\n50K & 74.5 & 68.1 & 72.3 & $-$6.4 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scale ablation (single-seed, seed=42). TaxEI deficit persists at PALADIN-comparable scale.}\n\\label{tab:scale}\n\\end{table}\n\nScale improves all methods but does not eliminate TaxEI's deficit. At 50K---comparable to PALADIN's training scale---TaxEI still underperforms Vanilla by 6.4pp, and the variance gradient persists (TaxEI SD 5.5pp vs.\\ estimated Vanilla ${\\sim}$2.5pp). The taxonomy penalty decreases from 6.4pp to 4.2pp, suggesting that additional clean samples partially dilute the taxonomy interference, but cannot eliminate it. This rules out the hypothesis that insufficient scale explains our negative result.\n\n\\subsection{Few-Shot Recovery Prompting}\n\\label{sec:fewshot}\n\nTo isolate whether the issue is the training signal itself (SFT gradient contamination) versus insufficient recovery knowledge, we compare SFT-based injection against inference-time few-shot recovery prompting (Table~\\ref{tab:fewshot}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Success Rate} & \\textbf{vs.\\ Vanilla} \\\\\n\\midrule\nVanilla (no few-shot)     & 61.7\\% & --- \\\\\nVanilla + 2-shot recovery & 63.8\\% & +2.1pp \\\\\nVanilla + 3-shot recovery & 66.0\\% & +4.3pp \\\\\nRandom SFT                & 63.1\\% & +1.4pp \\\\\nTaxEI SFT                 & 56.7\\% & $-$5.0pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Recovery method comparison (seed=42, 47 tasks).}\n\\label{tab:fewshot}\n\\end{table}\n\nVanilla + 3-shot recovery (66.0\\%) outperforms TaxEI SFT (56.7\\%) by 9.3pp, demonstrating that recovery information is valuable (+4.3pp over no-few-shot baseline) but SFT is the wrong delivery mechanism. Per-operator analysis reveals that few-shot gains are concentrated on C4 observation masking (+8.5pp) and P1 step-order swap (+4.2pp), while P2 sub-goal deletion shows zero gain---consistent with the hypothesis that globally cascading errors cannot be addressed through example-based recovery.\n\n\\subsection{Per-Operator Recovery Analysis}\n\\label{sec:peroperator}\n\nWe evaluate recovery performance per error operator across three seeds (Table~\\ref{tab:peroperator}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Operator} & \\textbf{Vanilla} & \\textbf{TaxEI} & \\textbf{Random} & \\textbf{TaxEI$-$V} \\\\\n\\midrule\nC4 obs.\\ mask  & 60.6\\scriptsize{$\\pm$3.2} & 66.7\\scriptsize{$\\pm$3.5} & 63.6\\scriptsize{$\\pm$4.1} & +6.1pp \\\\\nP1 step swap   & 58.3\\scriptsize{$\\pm$4.5} & 55.6\\scriptsize{$\\pm$5.2} & 58.3\\scriptsize{$\\pm$4.8} & $-$2.7pp \\\\\nC1 ctx.\\ trunc.& 66.7\\scriptsize{$\\pm$3.8} & 61.1\\scriptsize{$\\pm$4.8} & 63.9\\scriptsize{$\\pm$4.2} & $-$5.6pp \\\\\nP2 goal del.   & 55.6\\scriptsize{$\\pm$3.5} & 47.2\\scriptsize{$\\pm$4.0} & 52.8\\scriptsize{$\\pm$3.9} & $-$8.4pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-operator recovery rate (\\%, 3-seed mean $\\pm$ SD).}\n\\label{tab:peroperator}\n\\end{table}\n\nThe operators form a clear gradient along error locality: C4 (local, re-observe) $\\to$ P1 (semi-local, re-order) $\\to$ C1 (diffuse, re-contextualize) $\\to$ P2 (global, re-plan). TaxEI advantage tracks this gradient monotonically: +6.1pp $\\to$ $-$2.7pp $\\to$ $-$5.6pp $\\to$ $-$8.4pp. C4 observation masking---the most ``tool-use-like'' error type, requiring a local, discrete recovery action---is the \\emph{only} operator where TaxEI consistently helps. P2 sub-goal deletion, which requires global re-planning, shows the largest deficit. This within-environment locality gradient mirrors the cross-domain contrast between tool-use (PALADIN, local recovery) and planning (TaxEI, global recovery).\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nTable~\\ref{tab:stats} summarizes the pooled statistical tests incorporating all multi-seed dose-response data.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Test} & \\textbf{Original} & \\textbf{Updated} \\\\\n\\midrule\nPerm.\\ TaxEI vs.\\ Van. & $p{=}0.054$ & $p{=}0.031$* \\\\\nPerm.\\ TaxEI vs.\\ Rand. & $p{=}0.170$ & $p{=}0.042$* \\\\\nPaired $t$ TaxEI vs.\\ Rand. & $p{=}0.034$ & $p{=}0.024$* \\\\\nPaired $t$ TaxEI vs.\\ Van.  & $p{=}0.32$  & $p{=}0.18$~NS \\\\\nVariance ratio $F$-test & --- & $p{=}0.038$* \\\\\nBootstrap 95\\% CI overlap & Yes & No \\\\\nCohen's $d$ (TaxEI vs.\\ Van.) & 0.38 & 0.42 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Statistical tests. *: $p < 0.05$. Effective $N$ increased from 141 to 423 task-level observations with multi-seed dose-response data.}\n\\label{tab:stats}\n\\end{table}\n\nThe pooled permutation test for TaxEI vs.\\ Vanilla reaches $p{=}0.031$ (effective $N{=}423$), crossing the $\\alpha{=}0.05$ threshold. Bootstrap 95\\% CIs are non-overlapping: TaxEI [52.8\\%, 60.6\\%] vs.\\ Vanilla [62.0\\%, 68.6\\%]. The variance ratio $F$-test ($p{=}0.038$) formally confirms that TaxEI exhibits significantly higher cross-seed variance than Vanilla (ratio 6.79$\\times$). Cohen's $d{=}0.42$ indicates a medium effect size. Notably, the paired $t$-test for TaxEI vs.\\ Vanilla remains non-significant ($p{=}0.18$), because seed-level analysis ($n{=}9$) lacks power against the large inter-seed variance---this asymmetry itself supports our core claim that the primary effect is \\emph{increased instability} rather than systematic mean degradation.\n\n\\section{Discussion}\n\n\\paragraph{Why does error injection fail in planning?}\n\nOur results converge on a task-structural explanation organized along four dimensions (Table~\\ref{tab:structural}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{p{2.2cm}p{2.3cm}p{2.5cm}}\n\\toprule\n\\textbf{Dimension} & \\textbf{Tool-Use}~\\checkmark & \\textbf{Planning}~$\\times$ \\\\\n\\midrule\nError observ. & Explicit (API codes) & Implicit (valid-looking) \\\\\nRecovery space & Bounded (retry/switch) & Unbounded (re-plan) \\\\\nError locality & Single turn & Cascading \\\\\nFeedback & Per-tool signal & Sparse reward \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Task-structural comparison between tool-use and embodied planning.}\n\\label{tab:structural}\n\\end{table}\n\nThe per-operator analysis (\\S\\ref{sec:peroperator}) provides a micro-level version of this macro contrast: within the same environment, error locality determines whether injection helps (+6.1pp for local C4) or hurts ($-$8.4pp for global P2). This suggests that the boundary is not between ``domains'' but between error \\emph{types}---specifically, whether recovery requires local action substitution or global plan revision.\n\n\\paragraph{The taxonomy penalty as systematic bias.}\n\nThe constant ${\\sim}$6.4pp gap between TaxEI and Random across 9 independent observations (3 seeds $\\times$ 3 doses, SD $\\approx$ 0.4pp) is not explainable by noise. Training dynamics show that taxonomy-labeled samples produce coherent but wrong gradient directions (cosine 0.28), while random labels produce diffuse interference (cosine 0.35). The qualitative finding that 25\\% of TaxEI failures are ``operator replays''---the model reproducing taxonomy-specific error behaviors during clean evaluation---provides the behavioral manifestation of this gradient-level phenomenon.\n\n\\paragraph{Implications for the community.}\n\nOur results suggest three actionable guidelines: (1) Error injection methods should be validated with $\\geq$3 seeds, as single-seed results can mask a 2.6$\\times$ variance increase. (2) In planning domains, inference-time recovery prompting (+4.3pp) is preferable to SFT-based injection ($-$5.0pp). (3) If error injection is attempted in planning, restricting to locally recoverable error types (observation masking) may yield benefits while avoiding the harmful effects of globally cascading errors.\n\n\\paragraph{Limitations.}\n\nOur comparison with PALADIN involves confounds beyond task structure: base model, training scale, and the presence of inference-time retrieval. While the scale ablation (\\S\\ref{sec:scale}) and few-shot experiment (\\S\\ref{sec:fewshot}) partially address scale and retrieval confounds respectively, a fully controlled cross-domain study remains future work. ALFWorld's 47 test tasks limit per-operator statistical power. The WebShop replication uses only 2 seeds.\n\n\\section{Conclusion}\n\nTaxonomy-guided error injection, successful in tool-use domains, degrades embodied planning agent training. The mechanism is twofold: a universal threshold-plateau effect where error injection beyond ${\\sim}$15\\% collapses performance regardless of injection method, and a constant ${\\sim}$6.4pp taxonomy penalty where structured error labels teach specific wrong behaviors. The boundary between success and failure aligns with error locality: only locally recoverable errors benefit from injection training. These findings establish task-structural boundary conditions for failure-augmented training and caution against assuming that error injection transfers across agent domains.\n\n\\bibliography{custom}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f5b0448d-64ab-4a71-b125-933472143538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "f2eb50d6-2e7e-4b2a-87a0-2c31fc8f6a73",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection robustness in NLP taxonomy tasks",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Assistant

_source line 22 · 2026-05-15T02:35:51.883Z_

Now let me compile the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2eb50d6-2e7e-4b2a-87a0-2c31fc8f6a73",
  "isSidechain": false,
  "requestId": "req_011Cb3aL2wTHDxPfcDQ6EK5Z",
  "type": "assistant",
  "uuid": "8020969c-1e7b-4dad-ac37-8e17c21513ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VN6znYDQr98TzdG6ziWDn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8413,
      "cache_read_input_tokens": 43706,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 43706,
          "cache_creation_input_tokens": 8413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8413
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

_source line 23 · 2026-05-15T02:35:53.113Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RpAQL8KVsJtJtcDR7Vj77B`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8020969c-1e7b-4dad-ac37-8e17c21513ff",
  "isSidechain": false,
  "requestId": "req_011Cb3aL2wTHDxPfcDQ6EK5Z",
  "type": "assistant",
  "uuid": "8d5870a9-3616-4756-84f3-38d59862490e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012VN6znYDQr98TzdG6ziWDn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8413,
      "cache_read_input_tokens": 43706,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 43706,
          "cache_creation_input_tokens": 8413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8413
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

_source line 24 · 2026-05-15T02:35:53.283Z_

<details><summary>↩ Tool result · `toolu_01RpAQL8KVsJtJtcDR7Vj77B`</summary>

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
  "parentUuid": "8d5870a9-3616-4756-84f3-38d59862490e",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "3c169ca8-d915-403f-bdb0-a2d49a354995",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `emnlp2023.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8d5870a9-3616-4756-84f3-38d59862490e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T02:35:56.505Z_

<details><summary>Logged reasoning block</summary>

```text
The emnlp2023.sty is not available. Let me switch to a standard article class without the conference style file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c169ca8-d915-403f-bdb0-a2d49a354995",
  "isSidechain": false,
  "requestId": "req_011Cb3aLLEWi44ivukozBUco",
  "type": "assistant",
  "uuid": "36910430-2b48-4d11-be80-7e4530730e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxkEsAb9rx61bknnnFaHAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 52119,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 571,
          "cache_read_input_tokens": 52119,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 26 · 2026-05-15T02:35:57.520Z_

Need to use a standard document class since emnlp2023.sty isn't available. Let me fix the preamble.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36910430-2b48-4d11-be80-7e4530730e43",
  "isSidechain": false,
  "requestId": "req_011Cb3aLLEWi44ivukozBUco",
  "type": "assistant",
  "uuid": "5cc2bd30-2d12-4e8d-a325-e19d592e978d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxkEsAb9rx61bknnnFaHAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 52119,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 571,
          "cache_read_input_tokens": 52119,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 27 · 2026-05-15T02:36:02.615Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018hrzFXXBrasqFvhFQZWeJY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cc2bd30-2d12-4e8d-a325-e19d592e978d",
  "isSidechain": false,
  "requestId": "req_011Cb3aLLEWi44ivukozBUco",
  "type": "assistant",
  "uuid": "d880b429-cfd9-4264-a4a7-1e4a7489b095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxkEsAb9rx61bknnnFaHAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 438,
      "cache_read_input_tokens": 52119,
      "output_tokens": 571,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 571,
          "cache_read_input_tokens": 52119,
          "cache_creation_input_tokens": 438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 438
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

_source line 28 · 2026-05-15T02:36:02.643Z_

<details><summary>↩ Tool result · `toolu_018hrzFXXBrasqFvhFQZWeJY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d880b429-cfd9-4264-a4a7-1e4a7489b095",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "586e5866-bc4f-4de5-842b-a42072b70776",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{emnlp2023}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{hyperref}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\n\\title{Error Injection Helps Tool-Use but Hurts Planning:\\\\Boundary Conditions for Failure-Augmented Agent Training}\n\n\\author{Anonymous}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{emnlp2023}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 6,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{xcolor}",
          " \\usepackage{tabularx}",
          "+\\usepackage{hyperref}",
          " \\usepackage[T1]{fontenc}",
          " \\usepackage[utf8]{inputenc}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d880b429-cfd9-4264-a4a7-1e4a7489b095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-15T02:36:02.648Z_

```json
{
  "parentUuid": "586e5866-bc4f-4de5-842b-a42072b70776",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "df0ba56d-3c4a-471d-8cdf-b7e8ec83efec",
  "timestamp": "2026-05-15T02:36:02.648Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-15T02:36:05.724Z_

Also need to handle the bibliography since there's no .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df0ba56d-3c4a-471d-8cdf-b7e8ec83efec",
  "isSidechain": false,
  "requestId": "req_011Cb3aM23QYtFpGRPHQMevD",
  "type": "assistant",
  "uuid": "d4130da2-aa1f-4e5f-a541-caf9d54d47d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014isjnK8bDNRa6ax8U71L2z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 52557,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 709,
          "cache_read_input_tokens": 52557,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 31 · 2026-05-15T02:36:15.009Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0187vYinhkkXNfuUjw1jMPDA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
  "old_string": "\\bibliography{custom}\n\n\\end{document}",
  "new_string": "\\begin{thebibliography}{9}\n\n\\bibitem{chen2025paladin}\nChen et al.\n\\newblock PALADIN: Leveraging Tool-Use Failure Taxonomies for Robust LLM Agent Training.\n\\newblock \\emph{arXiv preprint arXiv:2509.25238}, 2025.\n\n\\bibitem{zhang2025eef}\nZhang et al.\n\\newblock EEF: Extracting Effective Signals from Failed Agent Trajectories.\n\\newblock \\emph{arXiv preprint arXiv:2504.13145}, 2025.\n\n\\bibitem{shridhar2021alfworld}\nShridhar, M. et al.\n\\newblock ALFWorld: Aligning Text and Embodied Environments for Interactive Learning.\n\\newblock In \\emph{Proc.\\ ICLR}, 2021.\n\n\\bibitem{yao2023react}\nYao, S. et al.\n\\newblock ReAct: Synergizing Reasoning and Acting in Language Models.\n\\newblock In \\emph{Proc.\\ ICLR}, 2023.\n\n\\bibitem{yao2022webshop}\nYao, S. et al.\n\\newblock WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2022.\n\n\\bibitem{song2024trial}\nSong, Y. et al.\n\\newblock Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{bishop1995training}\nBishop, C.M.\n\\newblock Training with Noise is Equivalent to Tikhonov Regularization.\n\\newblock \\emph{Neural Computation}, 7(1):108--116, 1995.\n\n\\bibitem{natarajan2013learning}\nNatarajan, N. et al.\n\\newblock Learning with Noisy Labels.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2013.\n\n\\end{thebibliography}\n\n\\end{document}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4130da2-aa1f-4e5f-a541-caf9d54d47d7",
  "isSidechain": false,
  "requestId": "req_011Cb3aM23QYtFpGRPHQMevD",
  "type": "assistant",
  "uuid": "f473ee64-eccd-4050-8f7b-5aa328204647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014isjnK8bDNRa6ax8U71L2z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 52557,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 709,
          "cache_read_input_tokens": 52557,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 32 · 2026-05-15T02:36:15.022Z_

<details><summary>↩ Tool result · `toolu_0187vYinhkkXNfuUjw1jMPDA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f473ee64-eccd-4050-8f7b-5aa328204647",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "dc1757f8-d639-4614-a4d4-f99b251e5664",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.tex",
    "oldString": "\\bibliography{custom}\n\n\\end{document}",
    "newString": "\\begin{thebibliography}{9}\n\n\\bibitem{chen2025paladin}\nChen et al.\n\\newblock PALADIN: Leveraging Tool-Use Failure Taxonomies for Robust LLM Agent Training.\n\\newblock \\emph{arXiv preprint arXiv:2509.25238}, 2025.\n\n\\bibitem{zhang2025eef}\nZhang et al.\n\\newblock EEF: Extracting Effective Signals from Failed Agent Trajectories.\n\\newblock \\emph{arXiv preprint arXiv:2504.13145}, 2025.\n\n\\bibitem{shridhar2021alfworld}\nShridhar, M. et al.\n\\newblock ALFWorld: Aligning Text and Embodied Environments for Interactive Learning.\n\\newblock In \\emph{Proc.\\ ICLR}, 2021.\n\n\\bibitem{yao2023react}\nYao, S. et al.\n\\newblock ReAct: Synergizing Reasoning and Acting in Language Models.\n\\newblock In \\emph{Proc.\\ ICLR}, 2023.\n\n\\bibitem{yao2022webshop}\nYao, S. et al.\n\\newblock WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2022.\n\n\\bibitem{song2024trial}\nSong, Y. et al.\n\\newblock Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents.\n\\newblock In \\emph{Proc.\\ ACL}, 2024.\n\n\\bibitem{bishop1995training}\nBishop, C.M.\n\\newblock Training with Noise is Equivalent to Tikhonov Regularization.\n\\newblock \\emph{Neural Computation}, 7(1):108--116, 1995.\n\n\\bibitem{natarajan2013learning}\nNatarajan, N. et al.\n\\newblock Learning with Noisy Labels.\n\\newblock In \\emph{Proc.\\ NeurIPS}, 2013.\n\n\\end{thebibliography}\n\n\\end{document}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 388,
        "oldLines": 6,
        "newStart": 388,
        "newLines": 48,
        "lines": [
          " ",
          " Taxonomy-guided error injection, successful in tool-use domains, degrades embodied planning agent training. The mechanism is twofold: a universal threshold-plateau effect where error injection beyond ${\\sim}$15\\% collapses performance regardless of injection method, and a constant ${\\sim}$6.4pp taxonomy penalty where structured error labels teach specific wrong behaviors. The boundary between success and failure aligns with error locality: only locally recoverable errors benefit from injection training. These findings establish task-structural boundary conditions for failure-augmented training and caution against assuming that error injection transfers across agent domains.",
          " ",
          "-\\bibliography{custom}",
          "+\\begin{thebibliography}{9}",
          " ",
          "+\\bibitem{chen2025paladin}",
          "+Chen et al.",
          "+\\newblock PALADIN: Leveraging Tool-Use Failure Taxonomies for Robust LLM Agent Training.",
          "+\\newblock \\emph{arXiv preprint arXiv:2509.25238}, 2025.",
          "+",
          "+\\bibitem{zhang2025eef}",
          "+Zhang et al.",
          "+\\newblock EEF: Extracting Effective Signals from Failed Agent Trajectories.",
          "+\\newblock \\emph{arXiv preprint arXiv:2504.13145}, 2025.",
          "+",
          "+\\bibitem{shridhar2021alfworld}",
          "+Shridhar, M. et al.",
          "+\\newblock ALFWorld: Aligning Text and Embodied Environments for Interactive Learning.",
          "+\\newblock In \\emph{Proc.\\ ICLR}, 2021.",
          "+",
          "+\\bibitem{yao2023react}",
          "+Yao, S. et al.",
          "+\\newblock ReAct: Synergizing Reasoning and Acting in Language Models.",
          "+\\newblock In \\emph{Proc.\\ ICLR}, 2023.",
          "+",
          "+\\bibitem{yao2022webshop}",
          "+Yao, S. et al.",
          "+\\newblock WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents.",
          "+\\newblock In \\emph{Proc.\\ NeurIPS}, 2022.",
          "+",
          "+\\bibitem{song2024trial}",
          "+Song, Y. et al.",
          "+\\newblock Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents.",
          "+\\newblock In \\emph{Proc.\\ ACL}, 2024.",
          "+",
          "+\\bibitem{bishop1995training}",
          "+Bishop, C.M.",
          "+\\newblock Training with Noise is Equivalent to Tikhonov Regularization.",
          "+\\newblock \\emph{Neural Computation}, 7(1):108--116, 1995.",
          "+",
          "+\\bibitem{natarajan2013learning}",
          "+Natarajan, N. et al.",
          "+\\newblock Learning with Noisy Labels.",
          "+\\newblock In \\emph{Proc.\\ NeurIPS}, 2013.",
          "+",
          "+\\end{thebibliography}",
          "+",
          " \\end{document}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f473ee64-eccd-4050-8f7b-5aa328204647",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T02:36:18.443Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CcmqkRsZPZoWT4mzntbjdX`</summary>

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
  "parentUuid": "dc1757f8-d639-4614-a4d4-f99b251e5664",
  "isSidechain": false,
  "requestId": "req_011Cb3aMvkBrxiiA5Vcs3oJM",
  "type": "assistant",
  "uuid": "4b81e81a-4690-4b29-a471-d65b3a93021b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCsJdZPbb5UzZqr3ZsnjRV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 53319,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 53319,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 34 · 2026-05-15T02:36:19.022Z_

<details><summary>↩ Tool result · `toolu_01CcmqkRsZPZoWT4mzntbjdX`</summary>

```text
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier
/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 133738 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b81e81a-4690-4b29-a471-d65b3a93021b",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "9483f383-c806-47ec-85a5-75a6add43844",
  "toolUseResult": {
    "stdout": "LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier\n/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 133738 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4b81e81a-4690-4b29-a471-d65b3a93021b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T02:36:23.398Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0179Xe3nYPGnkUwmeTZ3HwKt`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -10",
  "description": "Second pdflatex pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9483f383-c806-47ec-85a5-75a6add43844",
  "isSidechain": false,
  "requestId": "req_011Cb3aNDqbhjVDnxvLF83v4",
  "type": "assistant",
  "uuid": "6d8e6f4c-3b60-4680-8efb-6d33e8528e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6xRkFDHrya4vCgSpWxnh3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 54115,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 54115,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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

_source line 36 · 2026-05-15T02:36:23.852Z_

<details><summary>↩ Tool result · `toolu_0179Xe3nYPGnkUwmeTZ3HwKt`</summary>

```text
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier
/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on paper.pdf (8 pages, 136236 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d8e6f4c-3b60-4680-8efb-6d33e8528e52",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "6f2bf137-a1eb-4433-ac38-a0e7f9159929",
  "toolUseResult": {
    "stdout": "ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier\n/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (8 pages, 136236 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6d8e6f4c-3b60-4680-8efb-6d33e8528e52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T02:36:26.502Z_

Now let me verify there are no warnings about the core content — checking for any issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f2bf137-a1eb-4433-ac38-a0e7f9159929",
  "isSidechain": false,
  "requestId": "req_011Cb3aNaZXZRJ6DLSc4N7Pb",
  "type": "assistant",
  "uuid": "5ed2aa55-4a04-444a-8f5d-46f263749580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2zv3d4XSdfm92d8oGozV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 54653,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 446
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

_source line 38 · 2026-05-15T02:36:28.684Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015jgxPrSH6Np1h4WNgX2m4g`</summary>

```json
{
  "command": "grep -c \"Warning\\|Error\\|Undefined\" paper.log",
  "description": "Check for warnings in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ed2aa55-4a04-444a-8f5d-46f263749580",
  "isSidechain": false,
  "requestId": "req_011Cb3aNaZXZRJ6DLSc4N7Pb",
  "type": "assistant",
  "uuid": "cc603fd0-4a23-4234-8d31-47fece4d7be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2zv3d4XSdfm92d8oGozV9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 54653,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 54653,
          "cache_creation_input_tokens": 446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 446
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

_source line 39 · 2026-05-15T02:36:28.747Z_

<details><summary>↩ Tool result · `toolu_015jgxPrSH6Np1h4WNgX2m4g`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc603fd0-4a23-4234-8d31-47fece4d7be5",
  "isSidechain": false,
  "promptId": "23524231-4a4d-469e-b1c5-f8c3479b4ce0",
  "type": "user",
  "uuid": "f76f11b9-1b0f-48d9-9963-e73babe0afc2",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cc603fd0-4a23-4234-8d31-47fece4d7be5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "f76f11b9-1b0f-48d9-9963-e73babe0afc2",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection robustness in NLP taxonomy tasks",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Assistant

_source line 42 · 2026-05-15T02:36:43.614Z_

Clean compilation, 8 pages, no warnings or errors.

Paper written and compiled to `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best/paper.pdf` (8 pages). 

The paper covers all 8 experiments from `experiment_data.json`:

1. **Dose-Response Curve** (Table 2) — shared threshold-plateau + constant ~6.4pp taxonomy penalty
2. **Multi-Seed Dose-Response Replication** (Table 3) — 9-point taxonomy penalty stability (SD≈0.4pp)
3. **Training Dynamics** (Table 4) — loss decomposition, gradient cosine analysis
4. **Qualitative Failure Analysis** (Table 5) — 24 cases, operator replay as TaxEI-specific mode
5. **WebShop Validation** (Tables 6–7) — cross-environment pattern replication
6. **Scale Ablation** (Table 8) — 25K/50K, deficit persists at PALADIN scale
7. **Few-Shot Recovery** (Table 9) — inference-time delivery beats SFT
8. **Per-Operator Recovery** (Table 10) — error-locality gradient C4→P2
9. **Pooled Statistics** (Table 11) — permutation $p=0.031$, $F$-test $p=0.038$

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f76f11b9-1b0f-48d9-9963-e73babe0afc2",
  "isSidechain": false,
  "requestId": "req_011Cb3aNwSe7Q9dEVEwSo74D",
  "type": "assistant",
  "uuid": "a5ab54f5-da76-46ff-86ef-723fb3d70e33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dream_reports/dream_20260515T020837/best",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6aGRbryNYAV3xBKg4bi4d",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 120,
      "cache_read_input_tokens": 55099,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 55099,
          "cache_creation_input_tokens": 120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 120
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T020837 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_a…",
  "leafUuid": "a5ab54f5-da76-46ff-86ef-723fb3d70e33",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection robustness in NLP taxonomy tasks",
  "sessionId": "5876900b-bca3-4056-abfb-7d44763c8c40"
}
```

---
