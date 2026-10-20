# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/09c25452-0401-4009-b9de-190aa2a341c2.jsonl`
- **Structured JSON:** [`c790dc92009aa17977ae.json`](../../sessions/c7/c790dc92009aa17977ae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T06:07:34.688Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T06:07:34.688Z",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心假设 (embedding-based confusability 独立可分离) 不成立。Reframe 方向： 将 pairwise 分析 (Few-NERD 上 r=0.156, p=4.6e-12 仍然成立) 定位为 \"confusability exists but is entangled with type frequency and schema structure, not separable by embedding similarity alone\"。论文重心从 \"confusability as independent factor + SDGD solution\" 转向 \"empirical anatomy of schema complexity in training-free LLM IE\"—— 一篇方法学/分析论文而非方法论文。核心贡献变为： (1) 发现并量化频率-confusability 混淆这一此前被忽略的 confound； (2) 证明 batch-level 分析不可靠、pairwise 分析必要的方法学教训； (3) count→recall 单调退化的干净证据； (4) negative result on embedding SCS 作为 confusability proxy 的实证检验。 放弃 SDGD 作为 contribution，改为 discussion 中的 \"limitations and future directions\"。 目标仍是 EMNLP main (empirical/analysis track)，以 \"Lost in the Middle\" 风格的 controlled study 定位。Findings 作为 realistic fallback。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T06:07:34.691Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T06:07:34.691Z",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-15T06:07:34.711Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心假设 (embedding-based confusability 独立可分离) 不成立。Reframe 方向： 将 pairwise 分析 (Few-NERD 上 r=0.156, p=4.6e-12 仍然成立) 定位为 "confusability exists but is entangled with type frequency and schema structure, not separable by embedding similarity alone"。论文重心从 "confusability as independent factor + SDGD solution" 转向 "empirical anatomy of schema complexity in training-free LLM IE"—— 一篇方法学/分析论文而非方法论文。核心贡献变为： (1) 发现并量化频率-confusability 混淆这一此前被忽略的 confound； (2) 证明 batch-level 分析不可靠、pairwise 分析必要的方法学教训； (3) count→recall 单调退化的干净证据； (4) negative result on embedding SCS 作为 confusability proxy 的实证检验。 放弃 SDGD 作为 contribution，改为 discussion 中的 "limitations and future directions"。 目标仍是 EMNLP main (empirical/analysis track)，以 "Lost in the Middle" 风格的 controlled study 定位。Findings 作为 realistic fallback。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "3c11a04e-f136-43b0-9f6c-159f25e01538",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T06:07:34.710Z_

```json
{
  "parentUuid": "3c11a04e-f136-43b0-9f6c-159f25e01538",
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
  "uuid": "bffbfbed-a24f-4873-9917-39ce7eb781c0",
  "timestamp": "2026-05-15T06:07:34.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T06:07:34.710Z_

```json
{
  "parentUuid": "bffbfbed-a24f-4873-9917-39ce7eb781c0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ddbab2de-57bf-4cbe-865e-f218edc30c81",
  "timestamp": "2026-05-15T06:07:34.710Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
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
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Assistant

_source line 7 · 2026-05-15T06:07:37.268Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddbab2de-57bf-4cbe-865e-f218edc30c81",
  "isSidechain": false,
  "requestId": "req_011Cb3rUc5bMwP69LTEXSfQy",
  "type": "assistant",
  "uuid": "77a32c6c-53b0-46ad-99ed-6818863680d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WScDnMRHWcsURDHDP5JQZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11389,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11389
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

_source line 8 · 2026-05-15T06:07:38.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N51EGeNqYnFM7rZhBLNmVv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a32c6c-53b0-46ad-99ed-6818863680d6",
  "isSidechain": false,
  "requestId": "req_011Cb3rUc5bMwP69LTEXSfQy",
  "type": "assistant",
  "uuid": "aa64c885-15a9-49c3-b5a3-a664221df100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WScDnMRHWcsURDHDP5JQZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11389,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11389
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

_source line 9 · 2026-05-15T06:07:38.596Z_

<details><summary>↩ Tool result · `toolu_01N51EGeNqYnFM7rZhBLNmVv`</summary>

```text
1	[
2	  {
3	    "name": "MAVEN confusability study",
4	    "description": "Count curve + within-count BCS correlation on MAVEN Event Detection (168 event types, FrameNet hierarchy)。验证 NER→ED 跨任务复现。\n",
5	    "results": {
6	      "count_curve_recall_at_1": 0.58,
7	      "count_curve_recall_at_6": 0.41,
8	      "count_curve_recall_at_20": 0.3,
9	      "count_curve_recall_at_50": 0.22,
10	      "count_curve_recall_at_100": 0.15,
11	      "count_curve_recall_at_168": 0.1,
12	      "count_curve_f1_at_1": 0.28,
13	      "count_curve_f1_at_6": 0.27,
14	      "count_curve_f1_at_20": 0.26,
15	      "count_curve_f1_at_50": 0.23,
16	      "count_curve_f1_at_100": 0.18,
17	      "count_curve_f1_at_168": 0.13,
18	      "within_count_r_f1_bcs_count6": 0.04,
19	      "within_count_p_f1_bcs_count6": 0.42,
20	      "within_count_r_f1_bcs_count20": 0.08,
21	      "within_count_p_f1_bcs_count20": 0.28,
22	      "partial_r_f1_bcs": 0.05,
23	      "partial_p_f1_bcs": 0.38,
24	      "pairwise_pearson_r": 0.04,
25	      "pairwise_pearson_p": 0.12,
26	      "pairwise_n_pairs": 14028,
27	      "pairwise_nonzero_spearman_rho": 0.06,
28	      "pairwise_nonzero_spearman_p": 0.08,
29	      "confusion_ratio_extreme_high_vs_low": 1.4,
30	      "confusion_ratio_random_high_vs_low": 1.1,
31	      "wrong_type_count_at_1": 0,
32	      "wrong_type_count_at_50": 820,
33	      "wrong_type_count_at_168": 3100
34	    },
35	    "tables": [
36	      {
37	        "name": "Table: MAVEN Count Curve (Qwen3-32B, text_match)",
38	        "content": "| Count |  P     |  R     |  F1    | pred/gold | WrongType |\n|------:|-------:|-------:|-------:|----------:|----------:|\n|     1 | 0.170  | 0.580  | 0.280  |   3.41    |      0    |\n|     6 | 0.195  | 0.410  | 0.270  |   2.10    |    310    |\n|    20 | 0.225  | 0.300  | 0.260  |   1.33    |    640    |\n|    50 | 0.240  | 0.220  | 0.230  |   0.92    |    820    |\n|   100 | 0.215  | 0.150  | 0.180  |   0.70    |   1950    |\n|   168 | 0.185  | 0.100  | 0.130  |   0.54    |   3100    |\n"
39	      },
40	      {
41	        "name": "Table: MAVEN Within-Count BCS-F1 Correlation",
42	        "content": "| Count | r(F1,BCS) |   p    |  n  | Verdict |\n|------:|----------:|-------:|----:|---------|\n|     6 |    0.04   | 0.420  |  25 |  FAIL   |\n|    20 |    0.08   | 0.280  |  25 |  FAIL   |\n| partial|   0.05   | 0.380  |  50 |  FAIL   |\n"
43	      },
44	      {
45	        "name": "Table: MAVEN Pairwise BCS-Confusion",
46	        "content": "| Subset       | n_pairs | Pearson r |    p    | Verdict |\n|--------------|--------:|----------:|--------:|---------|\n| All          |  14028  |   0.040   |  0.120  |  FAIL   |\n| Nonzero-only |    385  |   0.060   |  0.080  |  FAIL   |\n"
47	      }
48	    ],
49	    "figures": [],
50	    "analysis": "MAVEN 未能复现 Few-NERD 上的 pairwise BCS-confusion 相关（r=0.04 vs 0.156）。 Count channel 依然稳健（recall 单调下降），但 confusability channel 在跨任务验证中失败。 这表明 embedding SCS 作为 confusability proxy 具有任务特异性： 对 NER 的名词性类型标签有效，对 ED 的动词性/事件性标签失效。 MAVEN 事件类型的混淆更多由 trigger polysemy 和 frame overlap 驱动， 这些因素无法被静态 embedding 相似度捕捉。 此结果直接支持 worst-tier 叙事：confusability 存在但与频率和 schema 结构纠缠， 不可通过 embedding similarity alone 分离。\n\n\nMAVEN 的 168 个事件类型源于 FrameNet 层级结构，存在大量「同父节点兄弟类型」 （如 Arriving/Departing, Killing/Death），这些兄弟对的 embedding SCS 确实很高。 然而 MAVEN 的关键特征是类型频率分布极度不均：高频事件（如 Causation, Statement） 占据大量标注，而 ~40% 的类型在验证集中仅有 <20 个 mention。在 worst 档下， pairwise BCS-confusion 相关不显著（r=0.04, p=0.12），原因在于： (a) MAVEN 事件触发词通常是动词，同一动词在不同上下文中映射不同事件类型， 混淆主要由上下文歧义驱动而非类型名称的 embedding 相似度； (b) 低频类型的 confusion 计数极度稀疏（大量 0），pearson r 受 zero-inflation 压制； (c) FrameNet 兄弟类型虽然 SCS 高，但它们的实际混淆更多由 frame element overlap 和 trigger polysemy 决定，embedding similarity 无法捕捉这些语用层面的混淆源。 Count curve 仍然展示 recall 单调下降（0.58→0.10），验证 count channel， 但 confusability channel 在 MAVEN 上未能独立分离。 Confusion ratio 在极端 batch 间仅 1.4x（对比 Few-NERD 的 27.5x）， 说明高 BCS batch 和低 BCS batch 在 MAVEN 上的 type substitution 率差异不显著。\n"
51	  },
52	  {
53	    "name": "DocRED confusability study",
54	    "description": "Count curve + BCS correlation on DocRED (96 relation types)。 Scaling stress test，关系抽取任务验证。\n",
55	    "results": {
56	      "count_curve_recall_at_1": 0.32,
57	      "count_curve_recall_at_10": 0.18,
58	      "count_curve_recall_at_30": 0.11,
59	      "count_curve_recall_at_96": 0.05,
60	      "count_curve_f1_at_1": 0.22,
61	      "count_curve_f1_at_96": 0.06,
62	      "pairwise_pearson_r": 0.02,
63	      "pairwise_pearson_p": 0.35,
64	      "partial_r_f1_bcs": -0.03,
65	      "partial_p_f1_bcs": 0.62,
66	      "confusion_ratio_extreme": 1.1
67	    },
68	    "tables": [
69	      {
70	        "name": "Table: DocRED Count Curve (Qwen3-32B)",
71	        "content": "| Count |  P     |  R     |  F1    |\n|------:|-------:|-------:|-------:|\n|     1 | 0.150  | 0.320  | 0.220  |\n|    10 | 0.165  | 0.180  | 0.170  |\n|    30 | 0.130  | 0.110  | 0.120  |\n|    96 | 0.085  | 0.050  | 0.060  |\n"
72	      }
73	    ],
74	    "figures": [],
75	    "analysis": "DocRED 在 worst 档下进一步确认 embedding SCS 不是通用的 confusability proxy。 关系抽取任务的 floor effect（full schema F1=6%）使得 confusability 分析 缺乏统计功率。此实验降级为 appendix 补充材料。\n\n\nDocRED 关系抽取整体难度远高于 NER/ED（需要跨句推理，training-free 基线极低）。 96 个关系类型中大量为低频长尾（~30% 类型在验证集中 <5 个 instance）。 Embedding SCS 对关系类型更不适用：关系类型名称（如 \"country of citizenship\" vs \"country of origin\"）在 embedding 空间确实相似，但实际混淆更多由 entity pair 的语义角色和文档级推理路径决定。Training-free LLM 在 DocRED 上 recall 本身就极低（full schema ~5%），confusability 效应被 floor effect 淹没。 Pairwise 相关不显著（r=0.02），partial r 甚至为负（-0.03）， 完全无法支持 confusability independence 假设。\n"
76	  },
77	  {
78	    "name": "Interaction effect 2×2",
79	    "description": "{low count, high count} × {low BCS, high BCS} on Few-NERD。 测试 count 和 confusability 的 additive vs multiplicative 交互。\n",
80	    "results": {
81	      "cell_low_count_low_bcs_f1": 0.34,
82	      "cell_low_count_high_bcs_f1": 0.33,
83	      "cell_high_count_low_bcs_f1": 0.31,
84	      "cell_high_count_high_bcs_f1": 0.3,
85	      "main_effect_count_f1_delta": -0.03,
86	      "main_effect_count_p": 0.04,
87	      "main_effect_bcs_f1_delta": -0.01,
88	      "main_effect_bcs_p": 0.42,
89	      "interaction_f1_delta": 0.0,
90	      "interaction_p": 0.88,
91	      "eta_squared_count": 0.08,
92	      "eta_squared_bcs": 0.01,
93	      "eta_squared_interaction": 0.001
94	    },
95	    "tables": [
96	      {
97	        "name": "Table: 2×2 Factorial Results (Few-NERD, Qwen3-32B)",
98	        "content": "|            | Low BCS  | High BCS | Δ(BCS) |\n|------------|----------|----------|--------|\n| Low Count  |  0.340   |  0.330   | -0.010 |\n| High Count |  0.310   |  0.300   | -0.010 |\n| Δ(Count)   | -0.030   | -0.030   |  0.000 |\n"
99	      },
100	      {
101	        "name": "Table: Two-Way ANOVA Summary",
102	        "content": "| Source      |   SS   |  df |   F    |   p    |  η²   |\n|-------------|-------:|----:|-------:|-------:|------:|\n| Count       | 0.0180 |   1 |  4.25  | 0.040  | 0.080 |\n| BCS         | 0.0022 |   1 |  0.52  | 0.420  | 0.010 |\n| Count×BCS   | 0.0002 |   1 |  0.05  | 0.880  | 0.001 |\n| Residual    | 0.2100 |  96 |        |        |       |\n"
103	      }
104	    ],
105	    "figures": [],
106	    "analysis": "BCS 主效应在控制 type frequency 后消失（p=0.42），交互效应为零。 Count 是唯一显著预测因子。这与 exp-002 中 batch-level 正相关的发现一致—— batch-level BCS 效应完全由 type frequency confound 解释。 Pairwise 分析中的 r=0.156 可能反映的是类型间的共现模式 而非独立的 confusability 效应。\n\n\n在 worst 档下，Per-type 频率控制后 BCS 主效应消失。2×2 ANOVA 显示： count 主效应显著但效应量小（η²=0.08, p=0.04），BCS 主效应不显著 （η²=0.01, p=0.42），交互效应不显著（η²≈0, p=0.88）。 这意味着 low BCS 和 high BCS batch 在相同 count 条件下 F1 差异仅 ~1 点， 远低于 exp-002 中未控制频率时观察到的差异。count 仍然是主要驱动因素， 但 confusability 在控制频率后不提供独立解释力。交互项为零说明 两个因素既非 additive 也非 multiplicative——BCS 根本不是独立因素。 这直接支持 \"confusability entangled with frequency\" 的 worst-tier 叙事。\n"
107	  },
108	  {
109	    "name": "Error taxonomy",
110	    "description": "系统化 FP 分类 (type_substitution / boundary_error / false_negative / hallucination) across BCS bins。Mechanistic evidence for multi-channel model。\n",
111	    "results": {
112	      "high_bcs_type_substitution_pct": 0.18,
113	      "high_bcs_boundary_error_pct": 0.22,
114	      "high_bcs_false_negative_pct": 0.45,
115	      "high_bcs_hallucination_pct": 0.15,
116	      "low_bcs_type_substitution_pct": 0.15,
117	      "low_bcs_boundary_error_pct": 0.2,
118	      "low_bcs_false_negative_pct": 0.48,
119	      "low_bcs_hallucination_pct": 0.17,
120	      "type_sub_high_vs_low_ratio": 1.2,
121	      "type_sub_chi2_p": 0.18,
122	      "boundary_error_ratio": 1.1,
123	      "fn_ratio": 0.94
124	    },
125	    "tables": [
126	      {
127	        "name": "Table: Error Taxonomy by BCS Bin (Few-NERD, frequency-controlled)",
128	        "content": "| Error Type         | High BCS | Low BCS | Ratio | χ² p  |\n|--------------------|----------|---------|-------|-------|\n| Type Substitution  |  18.0%   |  15.0%  |  1.20 | 0.180 |\n| Boundary Error     |  22.0%   |  20.0%  |  1.10 | 0.350 |\n| False Negative     |  45.0%   |  48.0%  |  0.94 | 0.410 |\n| Hallucination      |  15.0%   |  17.0%  |  0.88 | 0.520 |\n"
129	      }
130	    ],
131	    "figures": [],
132	    "analysis": "Error taxonomy 未能提供 multi-channel 模型的 mechanistic 证据。 Type substitution 在 BCS bins 间无显著差异表明：控制频率后， embedding similarity 不预测类型替换错误。False negative 在所有 bin 中 稳定主导（~45-48%），支持 count→recall 单调退化作为主要退化机制。 这是 worst-tier 的关键 negative result：multi-channel 模型中的 Channel 2 (confusability→type confusion) 在频率控制后不可独立验证。\n\n\n在 worst 档下，type_substitution 在 high-BCS 和 low-BCS batch 间无显著差异 （比率仅 1.2x, p=0.18）。这是因为一旦控制 type frequency，高 BCS batch 中 额外的 type substitution 消失了。exp-002 中观察到的 confusion ratio（27.5x 在 extreme batches）主要来自 frequency 效应：高频类型既有更高的 BCS（因为 它们在 Few-NERD 中本身就是 fine-grained 同层级类型），也有更多绝对混淆计数。 当按 per-type frequency 标准化后，high-BCS 和 low-BCS 的错误分布几乎相同。 所有 BCS bin 中最主导的错误类型都是 false_negative（~45-48%）， 这进一步支持 count channel（recall decline）是主要退化机制， 而非 confusability channel（type confusion）。Hallucination 比例在两组间 也无差异（15% vs 17%），说明 LLM 的类型替换是随机的而非 confusability-driven。\n"
133	  },
134	  {
135	    "name": "Multi-model validation",
136	    "description": "用第二个模型（LLaMA-3.3-70B-Instruct）复现 exp-002 协议。 验证 single-model 结果的 generalizability。\n",
137	    "results": {
138	      "llama_count_1_f1": 0.29,
139	      "llama_count_6_f1": 0.28,
140	      "llama_count_12_f1": 0.31,
141	      "llama_count_44_f1": 0.4,
142	      "llama_count_64_f1": 0.37,
143	      "llama_count_1_recall": 0.6,
144	      "llama_count_64_recall": 0.28,
145	      "llama_partial_r_f1_bcs": 0.06,
146	      "llama_partial_p_f1_bcs": 0.33,
147	      "llama_pairwise_r": 0.05,
148	      "llama_pairwise_p": 0.08,
149	      "llama_pairwise_n_pairs": 1953,
150	      "llama_nonzero_spearman_rho": 0.07,
151	      "llama_nonzero_spearman_p": 0.12,
152	      "llama_confusion_ratio_extreme": 1.6,
153	      "llama_confusion_ratio_random": 1.2
154	    },
155	    "tables": [
156	      {
157	        "name": "Table: Multi-Model Count Curve Comparison",
158	        "content": "| Count | Qwen3-32B F1 | LLaMA-3.3-70B F1 | ΔF1   |\n|------:|-------------:|------------------:|------:|\n|     1 |    0.323     |      0.290        | -0.033|\n|     6 |    0.306     |      0.280        | -0.026|\n|    12 |    0.347     |      0.310        | -0.037|\n|    44 |    0.445     |      0.400        | -0.045|\n|    64 |    0.414     |      0.370        | -0.044|\n"
159	      },
160	      {
161	        "name": "Table: Multi-Model Pairwise BCS-Confusion",
162	        "content": "| Model         | n_pairs | Pearson r |    p    | ρ (nonzero) | p (nonzero) |\n|---------------|--------:|----------:|--------:|------------:|------------:|\n| Qwen3-32B     |   1953  |   0.156   | 4.6e-12 |    0.254    |   1.1e-6    |\n| LLaMA-3.3-70B |   1953  |   0.050   |  0.080  |    0.070    |   0.120     |\n"
163	      }
164	    ],
165	    "figures": [],
166	    "analysis": "第二模型未能复现 pairwise BCS-confusion 相关。Qwen3-32B 上的 r=0.156 可能是模型特异性的：该模型的 confusion 模式恰好与 embedding SCS 弱对齐， 但这不是 LLM 的普遍特性。Count channel 跨模型稳健复现。 此结果使得 Claim 1 的 \"replicated on >=2 models\" 条件不满足。\n\n\nLLaMA-3.3-70B 在 Few-NERD 上的 pairwise BCS-confusion 相关不显著 （r=0.05, p=0.08）或方向不一致。Worst 档的核心预测是： Qwen3-32B 上观察到的 r=0.156 是模型特异性的而非普遍现象。 原因：(a) 不同模型的 type embedding 空间不同，Qwen3 的 confusion 模式 可能恰好与 all-MiniLM-L6-v2 的 SCS 对齐，而 LLaMA 的不对齐； (b) LLaMA-3.3 作为不同架构和训练数据的模型，其类型混淆模式 可能更多由其预训练数据中的 entity type 共现频率决定， 而非类型名称的 surface-level embedding similarity； (c) LLaMA 的 instruction following 能力不同于 Qwen， 可能在 type disambiguation 上有不同的 failure mode（如更多 boundary error 而非 type substitution）。Count curve 仍展示 recall 单调下降（0.60→0.28）， confirming count channel 跨模型稳健。\n"
167	  },
168	  {
169	    "name": "SDGD-zero on Few-NERD",
170	    "description": "Embedding SCS + graph coloring 实现 confusability-minimizing batch composition。 与 single-pass full-schema baseline 对比。\n",
171	    "results": {
172	      "sdgd_zero_f1": 0.43,
173	      "sdgd_zero_precision": 0.48,
174	      "sdgd_zero_recall": 0.39,
175	      "sdgd_zero_n_batches": 8,
176	      "single_pass_f1": 0.414,
177	      "single_pass_precision": 0.648,
178	      "single_pass_recall": 0.304,
179	      "sdgd_vs_single_pass_delta_f1": 1.6,
180	      "sdgd_vs_single_pass_p": 0.12,
181	      "sdgd_api_calls": 8,
182	      "single_pass_api_calls": 1,
183	      "sdgd_latency_seconds": 48,
184	      "single_pass_latency_seconds": 7,
185	      "sdgd_latency_ratio": 6.86
186	    },
187	    "tables": [
188	      {
189	        "name": "Table: SDGD-zero vs Single-Pass (Few-NERD)",
190	        "content": "| Method       |  P     |  R     |  F1    | #Calls | Latency(s) |\n|--------------|-------:|-------:|-------:|-------:|-----------:|\n| Single-Pass  | 0.648  | 0.304  | 0.414  |      1 |        7   |\n| SDGD-zero    | 0.480  | 0.390  | 0.430  |      8 |       48   |\n| Δ            | -0.168 | +0.086 | +0.016 |    +7  |      +41   |\n"
191	      }
192	    ],
193	    "figures": [],
194	    "analysis": "SDGD-zero 的微弱增益（+1.6 F1）不显著，且主要来自 batch size reduction 而非 confusability-aware grouping。需要 exp-013（random batching ablation） 来确认这一判断。\n\n\nSDGD-zero 对比 single-pass 有微弱 F1 提升（+1.6 点），但未达显著性（p=0.12）。 提升主要来自 batch size reduction 效应（8 个 batch 平均每个 ~8 types）， 而非 confusability-aware grouping。F1 增益可分解为： (a) recall 提升（0.304→0.39）来自更小的 batch size 减轻 count 压力， (b) precision 下降（0.648→0.48）来自 multi-batch aggregation 引入的 跨 batch 重复预测和合并冲突。净效果微弱且 variance 大。 关键问题是 SDGD-zero 的增益与 random batching（exp-013）无显著差异， 说明 confusability-aware grouping 本身不提供额外价值—— 任何 batch size reduction 都能获得类似增益。 Latency 增加 ~7x（48s vs 7s for 8 API calls），cost-benefit 不佳。\n"
195	  },
196	  {
197	    "name": "SDGD-zero on MAVEN",
198	    "description": "SDGD-zero on 168 event types。 与 single-pass + random batching 对比。Cross-task validation。\n",
199	    "results": {
200	      "sdgd_zero_f1": 0.15,
201	      "single_pass_f1": 0.13,
202	      "sdgd_vs_single_pass_delta": 2.0,
203	      "random_batching_f1": 0.155,
204	      "sdgd_vs_random_delta": -0.5,
205	      "sdgd_n_batches": 12,
206	      "random_n_batches": 12,
207	      "sdgd_latency_seconds": 85,
208	      "single_pass_latency_seconds": 10
209	    },
210	    "tables": [
211	      {
212	        "name": "Table: SDGD-zero vs Baselines (MAVEN)",
213	        "content": "| Method          |  F1    | #Calls | Latency(s) | ΔF1 vs single |\n|-----------------|-------:|-------:|-----------:|---------------:|\n| Single-Pass     | 0.130  |      1 |        10  |          —     |\n| Random-k12      | 0.155  |     12 |        80  |      +2.5      |\n| SDGD-zero-k12   | 0.150  |     12 |        85  |      +2.0      |\n"
214	      }
215	    ],
216	    "figures": [],
217	    "analysis": "MAVEN 上 SDGD-zero 不优于 random batching（甚至略低 0.5 点）， 直接否定 embedding SCS 作为 confusability proxy 的跨任务有效性。\n\n\nMAVEN 上 SDGD-zero 对比 single-pass 增益 +2.0 F1 点（0.13→0.15）， 看似有提升，但对比 random batching（同样 12 batches）甚至略低（-0.5 点）。 这彻底证明增益来自 batch count reduction 而非 confusability-aware grouping。 Random batching 在 MAVEN 上略优于 SDGD-zero 的原因可能是： SDGD 的 graph coloring 将相似类型分开，但这导致每个 batch 内类型语义跨度大， LLM 更难维持一致的抽取策略（如一个 batch 同时包含 Conflict 事件和 Life 事件）， 反而略增加了混淆。这个 ironic 的结果表明 embedding SCS 不是有效的 confusability proxy——它分离的「相似」类型实际上不是 LLM 的混淆源。\n"
218	  },
219	  {
220	    "name": "SDGD-cal on Few-NERD",
221	    "description": "用 5-10 个 calibration examples 计算 empirical confusability（无梯度）， 构建 SDGD-cal。与 SDGD-zero 对比。\n",
222	    "results": {
223	      "sdgd_cal_f1": 0.44,
224	      "sdgd_zero_f1": 0.43,
225	      "sdgd_cal_vs_zero_delta": 1.0,
226	      "sdgd_cal_vs_zero_p": 0.28,
227	      "sdgd_cal_n_batches": 8,
228	      "calibration_cost_api_calls": 66,
229	      "total_api_calls": 74,
230	      "sdgd_cal_latency_seconds": 420
231	    },
232	    "tables": [
233	      {
234	        "name": "Table: SDGD-cal vs SDGD-zero (Few-NERD)",
235	        "content": "| Method     |  F1    | Calibration Calls | Extraction Calls | Total | Latency(s) |\n|------------|-------:|------------------:|-----------------:|------:|-----------:|\n| SDGD-zero  | 0.430  |                 0 |                8 |     8 |        48  |\n| SDGD-cal   | 0.440  |                66 |                8 |    74 |       420  |\n| Δ          | +0.010 |               +66 |                0 |   +66 |      +372  |\n"
236	      }
237	    ],
238	    "figures": [],
239	    "analysis": "Empirical calibration 未能提供有意义的增益。少量 calibration data 下 confusion matrix 稀疏度过高，无法克服 embedding proxy 的局限性。 SDGD-cal 作为 contribution 不可行。\n\n\nSDGD-cal 使用 empirical confusion matrix 替代 embedding SCS 构建 confusability graph， 理论上应更准确。但在 worst 档下，calibration 仅 5-10 examples， empirical confusion matrix 极度稀疏：66 types × 5 examples = 330 predictions， 大多数 type pair 的经验混淆计数为 0，无法可靠估计 pairwise confusability。 结果 SDGD-cal 仅比 SDGD-zero 高 1.0 F1 点（不显著, p=0.28）， 但 calibration 额外消耗 66 次 API call（每个 type 一次），总 latency 420s（7 分钟）， cost-benefit 极差。这是因为少量 calibration data 下 empirical 和 embedding 两种 proxy 都不可靠，所获信息增量接近零。\n"
240	  },
241	  {
242	    "name": "SDGD-cal on MAVEN",
243	    "description": "SDGD-cal on 168 event types。Full comparison table。\n",
244	    "results": {
245	      "sdgd_cal_f1": 0.16,
246	      "sdgd_zero_f1": 0.15,
247	      "random_batching_f1": 0.155,
248	      "per_type_f1": 0.18,
249	      "sdgd_cal_vs_random_delta": 0.5,
250	      "sdgd_cal_vs_per_type_f1_ratio": 0.89,
251	      "sdgd_cal_latency_seconds": 1250,
252	      "per_type_latency_seconds": 1680,
253	      "sdgd_cal_vs_per_type_latency_ratio": 0.26,
254	      "calibration_cost_api_calls": 168
255	    },
256	    "tables": [
257	      {
258	        "name": "Table: Full Comparison (MAVEN)",
259	        "content": "| Method          |  F1    | #Calls | Latency(s) | ΔF1 vs single |\n|-----------------|-------:|-------:|-----------:|---------------:|\n| Single-Pass     | 0.130  |      1 |        10  |          —     |\n| Random-k12      | 0.155  |     12 |        80  |      +2.5      |\n| SDGD-zero-k12   | 0.150  |     12 |        85  |      +2.0      |\n| SDGD-cal-k12    | 0.160  |    180 |      1250  |      +3.0      |\n| Per-Type (k168) | 0.180  |    168 |      1680  |      +5.0      |\n"
260	      }
261	    ],
262	    "figures": [],
263	    "analysis": "MAVEN full comparison 确认 SDGD 框架在 worst 档下无实质贡献。 Per-type splitting 仍是质量上限，SDGD 变体与 random batching 无显著差异。\n\n\n168 个事件类型的 calibration 需要 168 次额外 API call， empirical confusion matrix 更加稀疏（168×167 = 28056 pairs，5 examples 每 type 几乎不可能覆盖）。SDGD-cal 仅比 SDGD-zero 高 1 F1 点（0.15→0.16）， 比 random batching 高 0.5 点（不显著）。Per-type splitting 仍是上限（0.18）， SDGD-cal 达到其 89%（符合 worst 档预测的 0.8-0.9 ratio）。 但 per-type 的 latency（1680s）远高于 SDGD-cal（1250s）， latency ratio 0.26 在 worst 档范围内。核心问题不变： SDGD-cal 的增益来自 batch size reduction，不来自 confusability-aware grouping。\n"
264	  },
265	  {
266	    "name": "Ablation: random batching",
267	    "description": "Same batch count k as SDGD, random composition。 隔离 confusability-aware grouping vs batch count reduction。\n",
268	    "results": {
269	      "random_k8_f1_fewnerd": 0.435,
270	      "sdgd_zero_k8_f1_fewnerd": 0.43,
271	      "sdgd_vs_random_delta_fewnerd": -0.5,
272	      "sdgd_vs_random_p": 0.72,
273	      "random_k8_f1_std": 0.015,
274	      "random_5_seeds_f1_range": [
275	        0.42,
276	        0.45
277	      ],
278	      "random_k8_recall": 0.395,
279	      "random_k8_precision": 0.485
280	    },
281	    "tables": [
282	      {
283	        "name": "Table: SDGD vs Random Batching (Few-NERD, k=8)",
284	        "content": "| Method       |  F1    |  F1 std |  R     |  P     | Δ vs SDGD |   p   |\n|--------------|-------:|--------:|-------:|-------:|----------:|------:|\n| SDGD-zero    | 0.430  |    —    | 0.390  | 0.480  |     —     |   —   |\n| Random (s1)  | 0.420  |    —    | 0.380  | 0.470  |  -1.0     |       |\n| Random (s2)  | 0.445  |    —    | 0.405  | 0.495  |  +1.5     |       |\n| Random (s3)  | 0.430  |    —    | 0.390  | 0.480  |   0.0     |       |\n| Random (s4)  | 0.450  |    —    | 0.410  | 0.500  |  +2.0     |       |\n| Random (s5)  | 0.435  |    —    | 0.395  | 0.485  |  +0.5     |       |\n| Random (avg) | 0.436  |  0.011 | 0.396  | 0.486  |  +0.6     | 0.72  |\n"
285	      }
286	    ],
287	    "figures": [],
288	    "analysis": "决定性 negative result：SDGD-zero 不优于 random batching。 Embedding SCS 不是有效的 confusability proxy。 论文中 SDGD 从 contribution 降级为 discussion/future work。\n\n\n这是 worst 档的决定性实验。Random batching（同 k=8）的 F1 为 0.435， 甚至略高于 SDGD-zero（0.430），差异 -0.5 点完全不显著（p=0.72）。 5 个 random seed 的 F1 range [0.42, 0.45] 完全包含 SDGD-zero 的 0.430。 这直接证明：SDGD 的全部增益来自 batch size reduction（从 64 types single-pass 到 ~8 types/batch），confusability-aware grouping 提供零额外价值。 Embedding SCS 不是有效的 confusability proxy：基于它的 graph coloring 分离出的类型组合与随机组合在 F1 上无差异。 这是对 Claim 3 (SDGD Effectiveness) 的直接否定。\n"
289	  },
290	  {
291	    "name": "Ablation: per-type splitting",
292	    "description": "Per-type splitting (UniNER-style, 1 type per batch)。 Upper bound on decomposition benefit。\n",
293	    "results": {
294	      "per_type_f1_fewnerd": 0.5,
295	      "per_type_precision": 0.42,
296	      "per_type_recall": 0.62,
297	      "per_type_n_calls": 64,
298	      "per_type_latency_seconds": 385,
299	      "sdgd_zero_f1": 0.43,
300	      "single_pass_f1": 0.414,
301	      "sdgd_vs_pertype_f1_ratio": 0.86,
302	      "sdgd_vs_pertype_latency_ratio": 0.125
303	    },
304	    "tables": [
305	      {
306	        "name": "Table: Decomposition Strategy Comparison (Few-NERD)",
307	        "content": "| Method       |  P     |  R     |  F1    | #Calls | Latency(s) | F1/PerType |\n|--------------|-------:|-------:|-------:|-------:|-----------:|-----------:|\n| Single-Pass  | 0.648  | 0.304  | 0.414  |      1 |          7 |    0.83    |\n| Random-k8    | 0.486  | 0.396  | 0.436  |      8 |         48 |    0.87    |\n| SDGD-zero-k8 | 0.480  | 0.390  | 0.430  |      8 |         48 |    0.86    |\n| Per-Type     | 0.420  | 0.620  | 0.500  |     64 |        385 |    1.00    |\n"
308	      }
309	    ],
310	    "figures": [],
311	    "analysis": "Per-type splitting 作为上限证明 batch decomposition 有价值， 但 SDGD 的 confusability-aware grouping 不提供超越 random 的增益。 论文可以报告 per-type 作为 practical baseline， 并讨论 \"intelligent decomposition\" 为何难以超越简单方案。\n\n\nPer-type splitting 消除了 batch 内所有类型间交互（count=1, BCS=0）， 是 decomposition 的理论上限。F1=0.50 比 single-pass（0.414）高 ~9 points， 比 SDGD-zero（0.43）高 ~7 points。SDGD-zero 仅达到 per-type 的 86% （在 worst 档的 0.8-0.9 range 内）。 Per-type 的增益主要来自 recall 大幅提升（0.304→0.62）， 因为每个 batch 只有 1 个 type，模型不需要在多个类型间分配注意力。 但 precision 下降（0.648→0.42），因为 per-type 提示下模型倾向于 over-extract（只被告知一个类型时，模型会将更多 span 标注为该类型）。 Latency 385s（64 次 API call），是 SDGD-zero 的 8x（48s）。 SDGD-zero 的 latency ratio 0.125 在 worst 档范围下限。 结论：per-type splitting 虽然质量最高，但 SDGD 并非 \"match per-type at lower cost\" 的有效中间方案——它只是 random batching 的等价物。\n"
312	  },
313	  {
314	    "name": "SCS validation",
315	    "description": "Embedding SCS vs empirical confusion matrix 的 rank correlation。 验证 embedding proxy 的实际有效性。\n",
316	    "results": {
317	      "spearman_rho_scs_vs_empirical": 0.12,
318	      "spearman_p": 0.03,
319	      "kendall_tau": 0.09,
320	      "kendall_p": 0.04,
321	      "top_10_empirical_pairs_in_top_10_scs": 2,
322	      "top_10_overlap_pct": 0.2,
323	      "scs_auc_for_confusion_binary": 0.56
324	    },
325	    "tables": [
326	      {
327	        "name": "Table: SCS vs Empirical Confusion Correlation",
328	        "content": "| Metric               | Value  |   p    |\n|----------------------|-------:|-------:|\n| Spearman ρ           |  0.12  | 0.030  |\n| Kendall τ            |  0.09  | 0.040  |\n| Top-10 overlap       |  2/10  |   —    |\n| AUC (binary)         |  0.56  |   —    |\n"
329	      },
330	      {
331	        "name": "Table: Top-10 Empirical vs SCS Mismatch",
332	        "content": "| Rank | Top Empirical Pair                          | In Top-10 SCS? |\n|-----:|---------------------------------------------|----------------|\n|    1 | person-other ↔ person-politician            |      Yes       |\n|    2 | person-other ↔ organization-other           |       No       |\n|    3 | location-GPE ↔ location-bodiesofwater       |       No       |\n|    4 | person-scholar ↔ person-artist              |      Yes       |\n|    5 | building-library ↔ building-other           |       No       |\n|    6 | event-sportsevent ↔ event-other             |       No       |\n|    7 | organization-company ↔ organization-other   |       No       |\n|    8 | person-athlete ↔ person-other               |       No       |\n|    9 | location-GPE ↔ location-other               |       No       |\n|   10 | product-car ↔ product-other                 |       No       |\n"
333	      }
334	    ],
335	    "figures": [],
336	    "analysis": "SCS 作为 confusability proxy 在实证检验中几乎失效（AUC=0.56 ≈ random）。 Top confused pairs 多涉及 \"-other\" 标签歧义，这是 schema design issue 而非 embedding similarity 能捕捉的。此 negative result 成为论文的 核心方法学贡献之一：证明 embedding similarity ≠ LLM confusability。\n\nEmbedding SCS 与 empirical confusion 的 rank correlation 很弱（ρ=0.12）， 虽然由于 n=1953 pairs 而 p<0.05（统计显著），但实际效应量极小。 Top-10 overlap 仅 20%（10 个最高经验混淆 pair 中仅 2 个也在最高 SCS pair 中）， 说明 embedding similarity 无法预测真实的混淆热点。 AUC=0.56（仅略高于 random 0.50），进一步证明 SCS 作为 binary confusion classifier 几乎无用。原因：(a) embedding similarity 捕捉的是语义接近性， 但 LLM 的 type confusion 更多由 schema 中的 type definition overlap、 training data 中的 type co-occurrence 和 prompt format 驱动； (b) 高 SCS pair 中很多是语义相关但 LLM 不混淆的 （如 \"building-library\" 和 \"building-hotel\" SCS 高但 LLM 不混淆）； (c) 低 SCS pair 中有些 LLM 频繁混淆 （如 \"person-other\" 和 \"organization-other\" SCS 较低但因 \"other\" 标签 歧义导致大量混淆）。这是 worst 档的关键 negative result， 直接否定 embedding SCS 作为 practical confusability proxy 的可行性。\n"
337	  }
338	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa64c885-15a9-49c3-b5a3-a664221df100",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "38964f37-49f0-4f60-85e6-9ba85e5e95e4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"MAVEN confusability study\",\n    \"description\": \"Count curve + within-count BCS correlation on MAVEN Event Detection (168 event types, FrameNet hierarchy)。验证 NER→ED 跨任务复现。\\n\",\n    \"results\": {\n      \"count_curve_recall_at_1\": 0.58,\n      \"count_curve_recall_at_6\": 0.41,\n      \"count_curve_recall_at_20\": 0.3,\n      \"count_curve_recall_at_50\": 0.22,\n      \"count_curve_recall_at_100\": 0.15,\n      \"count_curve_recall_at_168\": 0.1,\n      \"count_curve_f1_at_1\": 0.28,\n      \"count_curve_f1_at_6\": 0.27,\n      \"count_curve_f1_at_20\": 0.26,\n      \"count_curve_f1_at_50\": 0.23,\n      \"count_curve_f1_at_100\": 0.18,\n      \"count_curve_f1_at_168\": 0.13,\n      \"within_count_r_f1_bcs_count6\": 0.04,\n      \"within_count_p_f1_bcs_count6\": 0.42,\n      \"within_count_r_f1_bcs_count20\": 0.08,\n      \"within_count_p_f1_bcs_count20\": 0.28,\n      \"partial_r_f1_bcs\": 0.05,\n      \"partial_p_f1_bcs\": 0.38,\n      \"pairwise_pearson_r\": 0.04,\n      \"pairwise_pearson_p\": 0.12,\n      \"pairwise_n_pairs\": 14028,\n      \"pairwise_nonzero_spearman_rho\": 0.06,\n      \"pairwise_nonzero_spearman_p\": 0.08,\n      \"confusion_ratio_extreme_high_vs_low\": 1.4,\n      \"confusion_ratio_random_high_vs_low\": 1.1,\n      \"wrong_type_count_at_1\": 0,\n      \"wrong_type_count_at_50\": 820,\n      \"wrong_type_count_at_168\": 3100\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: MAVEN Count Curve (Qwen3-32B, text_match)\",\n        \"content\": \"| Count |  P     |  R     |  F1    | pred/gold | WrongType |\\n|------:|-------:|-------:|-------:|----------:|----------:|\\n|     1 | 0.170  | 0.580  | 0.280  |   3.41    |      0    |\\n|     6 | 0.195  | 0.410  | 0.270  |   2.10    |    310    |\\n|    20 | 0.225  | 0.300  | 0.260  |   1.33    |    640    |\\n|    50 | 0.240  | 0.220  | 0.230  |   0.92    |    820    |\\n|   100 | 0.215  | 0.150  | 0.180  |   0.70    |   1950    |\\n|   168 | 0.185  | 0.100  | 0.130  |   0.54    |   3100    |\\n\"\n      },\n      {\n        \"name\": \"Table: MAVEN Within-Count BCS-F1 Correlation\",\n        \"content\": \"| Count | r(F1,BCS) |   p    |  n  | Verdict |\\n|------:|----------:|-------:|----:|---------|\\n|     6 |    0.04   | 0.420  |  25 |  FAIL   |\\n|    20 |    0.08   | 0.280  |  25 |  FAIL   |\\n| partial|   0.05   | 0.380  |  50 |  FAIL   |\\n\"\n      },\n      {\n        \"name\": \"Table: MAVEN Pairwise BCS-Confusion\",\n        \"content\": \"| Subset       | n_pairs | Pearson r |    p    | Verdict |\\n|--------------|--------:|----------:|--------:|---------|\\n| All          |  14028  |   0.040   |  0.120  |  FAIL   |\\n| Nonzero-only |    385  |   0.060   |  0.080  |  FAIL   |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 未能复现 Few-NERD 上的 pairwise BCS-confusion 相关（r=0.04 vs 0.156）。 Count channel 依然稳健（recall 单调下降），但 confusability channel 在跨任务验证中失败。 这表明 embedding SCS 作为 confusability proxy 具有任务特异性： 对 NER 的名词性类型标签有效，对 ED 的动词性/事件性标签失效。 MAVEN 事件类型的混淆更多由 trigger polysemy 和 frame overlap 驱动， 这些因素无法被静态 embedding 相似度捕捉。 此结果直接支持 worst-tier 叙事：confusability 存在但与频率和 schema 结构纠缠， 不可通过 embedding similarity alone 分离。\\n\\n\\nMAVEN 的 168 个事件类型源于 FrameNet 层级结构，存在大量「同父节点兄弟类型」 （如 Arriving/Departing, Killing/Death），这些兄弟对的 embedding SCS 确实很高。 然而 MAVEN 的关键特征是类型频率分布极度不均：高频事件（如 Causation, Statement） 占据大量标注，而 ~40% 的类型在验证集中仅有 <20 个 mention。在 worst 档下， pairwise BCS-confusion 相关不显著（r=0.04, p=0.12），原因在于： (a) MAVEN 事件触发词通常是动词，同一动词在不同上下文中映射不同事件类型， 混淆主要由上下文歧义驱动而非类型名称的 embedding 相似度； (b) 低频类型的 confusion 计数极度稀疏（大量 0），pearson r 受 zero-inflation 压制； (c) FrameNet 兄弟类型虽然 SCS 高，但它们的实际混淆更多由 frame element overlap 和 trigger polysemy 决定，embedding similarity 无法捕捉这些语用层面的混淆源。 Count curve 仍然展示 recall 单调下降（0.58→0.10），验证 count channel， 但 confusability channel 在 MAVEN 上未能独立分离。 Confusion ratio 在极端 batch 间仅 1.4x（对比 Few-NERD 的 27.5x）， 说明高 BCS batch 和低 BCS batch 在 MAVEN 上的 type substitution 率差异不显著。\\n\"\n  },\n  {\n    \"name\": \"DocRED confusability study\",\n    \"description\": \"Count curve + BCS correlation on DocRED (96 relation types)。 Scaling stress test，关系抽取任务验证。\\n\",\n    \"results\": {\n      \"count_curve_recall_at_1\": 0.32,\n      \"count_curve_recall_at_10\": 0.18,\n      \"count_curve_recall_at_30\": 0.11,\n      \"count_curve_recall_at_96\": 0.05,\n      \"count_curve_f1_at_1\": 0.22,\n      \"count_curve_f1_at_96\": 0.06,\n      \"pairwise_pearson_r\": 0.02,\n      \"pairwise_pearson_p\": 0.35,\n      \"partial_r_f1_bcs\": -0.03,\n      \"partial_p_f1_bcs\": 0.62,\n      \"confusion_ratio_extreme\": 1.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DocRED Count Curve (Qwen3-32B)\",\n        \"content\": \"| Count |  P     |  R     |  F1    |\\n|------:|-------:|-------:|-------:|\\n|     1 | 0.150  | 0.320  | 0.220  |\\n|    10 | 0.165  | 0.180  | 0.170  |\\n|    30 | 0.130  | 0.110  | 0.120  |\\n|    96 | 0.085  | 0.050  | 0.060  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DocRED 在 worst 档下进一步确认 embedding SCS 不是通用的 confusability proxy。 关系抽取任务的 floor effect（full schema F1=6%）使得 confusability 分析 缺乏统计功率。此实验降级为 appendix 补充材料。\\n\\n\\nDocRED 关系抽取整体难度远高于 NER/ED（需要跨句推理，training-free 基线极低）。 96 个关系类型中大量为低频长尾（~30% 类型在验证集中 <5 个 instance）。 Embedding SCS 对关系类型更不适用：关系类型名称（如 \\\"country of citizenship\\\" vs \\\"country of origin\\\"）在 embedding 空间确实相似，但实际混淆更多由 entity pair 的语义角色和文档级推理路径决定。Training-free LLM 在 DocRED 上 recall 本身就极低（full schema ~5%），confusability 效应被 floor effect 淹没。 Pairwise 相关不显著（r=0.02），partial r 甚至为负（-0.03）， 完全无法支持 confusability independence 假设。\\n\"\n  },\n  {\n    \"name\": \"Interaction effect 2×2\",\n    \"description\": \"{low count, high count} × {low BCS, high BCS} on Few-NERD。 测试 count 和 confusability 的 additive vs multiplicative 交互。\\n\",\n    \"results\": {\n      \"cell_low_count_low_bcs_f1\": 0.34,\n      \"cell_low_count_high_bcs_f1\": 0.33,\n      \"cell_high_count_low_bcs_f1\": 0.31,\n      \"cell_high_count_high_bcs_f1\": 0.3,\n      \"main_effect_count_f1_delta\": -0.03,\n      \"main_effect_count_p\": 0.04,\n      \"main_effect_bcs_f1_delta\": -0.01,\n      \"main_effect_bcs_p\": 0.42,\n      \"interaction_f1_delta\": 0.0,\n      \"interaction_p\": 0.88,\n      \"eta_squared_count\": 0.08,\n      \"eta_squared_bcs\": 0.01,\n      \"eta_squared_interaction\": 0.001\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: 2×2 Factorial Results (Few-NERD, Qwen3-32B)\",\n        \"content\": \"|            | Low BCS  | High BCS | Δ(BCS) |\\n|------------|----------|----------|--------|\\n| Low Count  |  0.340   |  0.330   | -0.010 |\\n| High Count |  0.310   |  0.300   | -0.010 |\\n| Δ(Count)   | -0.030   | -0.030   |  0.000 |\\n\"\n      },\n      {\n        \"name\": \"Table: Two-Way ANOVA Summary\",\n        \"content\": \"| Source      |   SS   |  df |   F    |   p    |  η²   |\\n|-------------|-------:|----:|-------:|-------:|------:|\\n| Count       | 0.0180 |   1 |  4.25  | 0.040  | 0.080 |\\n| BCS         | 0.0022 |   1 |  0.52  | 0.420  | 0.010 |\\n| Count×BCS   | 0.0002 |   1 |  0.05  | 0.880  | 0.001 |\\n| Residual    | 0.2100 |  96 |        |        |       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"BCS 主效应在控制 type frequency 后消失（p=0.42），交互效应为零。 Count 是唯一显著预测因子。这与 exp-002 中 batch-level 正相关的发现一致—— batch-level BCS 效应完全由 type frequency confound 解释。 Pairwise 分析中的 r=0.156 可能反映的是类型间的共现模式 而非独立的 confusability 效应。\\n\\n\\n在 worst 档下，Per-type 频率控制后 BCS 主效应消失。2×2 ANOVA 显示： count 主效应显著但效应量小（η²=0.08, p=0.04），BCS 主效应不显著 （η²=0.01, p=0.42），交互效应不显著（η²≈0, p=0.88）。 这意味着 low BCS 和 high BCS batch 在相同 count 条件下 F1 差异仅 ~1 点， 远低于 exp-002 中未控制频率时观察到的差异。count 仍然是主要驱动因素， 但 confusability 在控制频率后不提供独立解释力。交互项为零说明 两个因素既非 additive 也非 multiplicative——BCS 根本不是独立因素。 这直接支持 \\\"confusability entangled with frequency\\\" 的 worst-tier 叙事。\\n\"\n  },\n  {\n    \"name\": \"Error taxonomy\",\n    \"description\": \"系统化 FP 分类 (type_substitution / boundary_error / false_negative / hallucination) across BCS bins。Mechanistic evidence for multi-channel model。\\n\",\n    \"results\": {\n      \"high_bcs_type_substitution_pct\": 0.18,\n      \"high_bcs_boundary_error_pct\": 0.22,\n      \"high_bcs_false_negative_pct\": 0.45,\n      \"high_bcs_hallucination_pct\": 0.15,\n      \"low_bcs_type_substitution_pct\": 0.15,\n      \"low_bcs_boundary_error_pct\": 0.2,\n      \"low_bcs_false_negative_pct\": 0.48,\n      \"low_bcs_hallucination_pct\": 0.17,\n      \"type_sub_high_vs_low_ratio\": 1.2,\n      \"type_sub_chi2_p\": 0.18,\n      \"boundary_error_ratio\": 1.1,\n      \"fn_ratio\": 0.94\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Error Taxonomy by BCS Bin (Few-NERD, frequency-controlled)\",\n        \"content\": \"| Error Type         | High BCS | Low BCS | Ratio | χ² p  |\\n|--------------------|----------|---------|-------|-------|\\n| Type Substitution  |  18.0%   |  15.0%  |  1.20 | 0.180 |\\n| Boundary Error     |  22.0%   |  20.0%  |  1.10 | 0.350 |\\n| False Negative     |  45.0%   |  48.0%  |  0.94 | 0.410 |\\n| Hallucination      |  15.0%   |  17.0%  |  0.88 | 0.520 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error taxonomy 未能提供 multi-channel 模型的 mechanistic 证据。 Type substitution 在 BCS bins 间无显著差异表明：控制频率后， embedding similarity 不预测类型替换错误。False negative 在所有 bin 中 稳定主导（~45-48%），支持 count→recall 单调退化作为主要退化机制。 这是 worst-tier 的关键 negative result：multi-channel 模型中的 Channel 2 (confusability→type confusion) 在频率控制后不可独立验证。\\n\\n\\n在 worst 档下，type_substitution 在 high-BCS 和 low-BCS batch 间无显著差异 （比率仅 1.2x, p=0.18）。这是因为一旦控制 type frequency，高 BCS batch 中 额外的 type substitution 消失了。exp-002 中观察到的 confusion ratio（27.5x 在 extreme batches）主要来自 frequency 效应：高频类型既有更高的 BCS（因为 它们在 Few-NERD 中本身就是 fine-grained 同层级类型），也有更多绝对混淆计数。 当按 per-type frequency 标准化后，high-BCS 和 low-BCS 的错误分布几乎相同。 所有 BCS bin 中最主导的错误类型都是 false_negative（~45-48%）， 这进一步支持 count channel（recall decline）是主要退化机制， 而非 confusability channel（type confusion）。Hallucination 比例在两组间 也无差异（15% vs 17%），说明 LLM 的类型替换是随机的而非 confusability-driven。\\n\"\n  },\n  {\n    \"name\": \"Multi-model validation\",\n    \"description\": \"用第二个模型（LLaMA-3.3-70B-Instruct）复现 exp-002 协议。 验证 single-model 结果的 generalizability。\\n\",\n    \"results\": {\n      \"llama_count_1_f1\": 0.29,\n      \"llama_count_6_f1\": 0.28,\n      \"llama_count_12_f1\": 0.31,\n      \"llama_count_44_f1\": 0.4,\n      \"llama_count_64_f1\": 0.37,\n      \"llama_count_1_recall\": 0.6,\n      \"llama_count_64_recall\": 0.28,\n      \"llama_partial_r_f1_bcs\": 0.06,\n      \"llama_partial_p_f1_bcs\": 0.33,\n      \"llama_pairwise_r\": 0.05,\n      \"llama_pairwise_p\": 0.08,\n      \"llama_pairwise_n_pairs\": 1953,\n      \"llama_nonzero_spearman_rho\": 0.07,\n      \"llama_nonzero_spearman_p\": 0.12,\n      \"llama_confusion_ratio_extreme\": 1.6,\n      \"llama_confusion_ratio_random\": 1.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Multi-Model Count Curve Comparison\",\n        \"content\": \"| Count | Qwen3-32B F1 | LLaMA-3.3-70B F1 | ΔF1   |\\n|------:|-------------:|------------------:|------:|\\n|     1 |    0.323     |      0.290        | -0.033|\\n|     6 |    0.306     |      0.280        | -0.026|\\n|    12 |    0.347     |      0.310        | -0.037|\\n|    44 |    0.445     |      0.400        | -0.045|\\n|    64 |    0.414     |      0.370        | -0.044|\\n\"\n      },\n      {\n        \"name\": \"Table: Multi-Model Pairwise BCS-Confusion\",\n        \"content\": \"| Model         | n_pairs | Pearson r |    p    | ρ (nonzero) | p (nonzero) |\\n|---------------|--------:|----------:|--------:|------------:|------------:|\\n| Qwen3-32B     |   1953  |   0.156   | 4.6e-12 |    0.254    |   1.1e-6    |\\n| LLaMA-3.3-70B |   1953  |   0.050   |  0.080  |    0.070    |   0.120     |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"第二模型未能复现 pairwise BCS-confusion 相关。Qwen3-32B 上的 r=0.156 可能是模型特异性的：该模型的 confusion 模式恰好与 embedding SCS 弱对齐， 但这不是 LLM 的普遍特性。Count channel 跨模型稳健复现。 此结果使得 Claim 1 的 \\\"replicated on >=2 models\\\" 条件不满足。\\n\\n\\nLLaMA-3.3-70B 在 Few-NERD 上的 pairwise BCS-confusion 相关不显著 （r=0.05, p=0.08）或方向不一致。Worst 档的核心预测是： Qwen3-32B 上观察到的 r=0.156 是模型特异性的而非普遍现象。 原因：(a) 不同模型的 type embedding 空间不同，Qwen3 的 confusion 模式 可能恰好与 all-MiniLM-L6-v2 的 SCS 对齐，而 LLaMA 的不对齐； (b) LLaMA-3.3 作为不同架构和训练数据的模型，其类型混淆模式 可能更多由其预训练数据中的 entity type 共现频率决定， 而非类型名称的 surface-level embedding similarity； (c) LLaMA 的 instruction following 能力不同于 Qwen， 可能在 type disambiguation 上有不同的 failure mode（如更多 boundary error 而非 type substitution）。Count curve 仍展示 recall 单调下降（0.60→0.28）， confirming count channel 跨模型稳健。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on Few-NERD\",\n    \"description\": \"Embedding SCS + graph coloring 实现 confusability-minimizing batch composition。 与 single-pass full-schema baseline 对比。\\n\",\n    \"results\": {\n      \"sdgd_zero_f1\": 0.43,\n      \"sdgd_zero_precision\": 0.48,\n      \"sdgd_zero_recall\": 0.39,\n      \"sdgd_zero_n_batches\": 8,\n      \"single_pass_f1\": 0.414,\n      \"single_pass_precision\": 0.648,\n      \"single_pass_recall\": 0.304,\n      \"sdgd_vs_single_pass_delta_f1\": 1.6,\n      \"sdgd_vs_single_pass_p\": 0.12,\n      \"sdgd_api_calls\": 8,\n      \"single_pass_api_calls\": 1,\n      \"sdgd_latency_seconds\": 48,\n      \"single_pass_latency_seconds\": 7,\n      \"sdgd_latency_ratio\": 6.86\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD-zero vs Single-Pass (Few-NERD)\",\n        \"content\": \"| Method       |  P     |  R     |  F1    | #Calls | Latency(s) |\\n|--------------|-------:|-------:|-------:|-------:|-----------:|\\n| Single-Pass  | 0.648  | 0.304  | 0.414  |      1 |        7   |\\n| SDGD-zero    | 0.480  | 0.390  | 0.430  |      8 |       48   |\\n| Δ            | -0.168 | +0.086 | +0.016 |    +7  |      +41   |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SDGD-zero 的微弱增益（+1.6 F1）不显著，且主要来自 batch size reduction 而非 confusability-aware grouping。需要 exp-013（random batching ablation） 来确认这一判断。\\n\\n\\nSDGD-zero 对比 single-pass 有微弱 F1 提升（+1.6 点），但未达显著性（p=0.12）。 提升主要来自 batch size reduction 效应（8 个 batch 平均每个 ~8 types）， 而非 confusability-aware grouping。F1 增益可分解为： (a) recall 提升（0.304→0.39）来自更小的 batch size 减轻 count 压力， (b) precision 下降（0.648→0.48）来自 multi-batch aggregation 引入的 跨 batch 重复预测和合并冲突。净效果微弱且 variance 大。 关键问题是 SDGD-zero 的增益与 random batching（exp-013）无显著差异， 说明 confusability-aware grouping 本身不提供额外价值—— 任何 batch size reduction 都能获得类似增益。 Latency 增加 ~7x（48s vs 7s for 8 API calls），cost-benefit 不佳。\\n\"\n  },\n  {\n    \"name\": \"SDGD-zero on MAVEN\",\n    \"description\": \"SDGD-zero on 168 event types。 与 single-pass + random batching 对比。Cross-task validation。\\n\",\n    \"results\": {\n      \"sdgd_zero_f1\": 0.15,\n      \"single_pass_f1\": 0.13,\n      \"sdgd_vs_single_pass_delta\": 2.0,\n      \"random_batching_f1\": 0.155,\n      \"sdgd_vs_random_delta\": -0.5,\n      \"sdgd_n_batches\": 12,\n      \"random_n_batches\": 12,\n      \"sdgd_latency_seconds\": 85,\n      \"single_pass_latency_seconds\": 10\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD-zero vs Baselines (MAVEN)\",\n        \"content\": \"| Method          |  F1    | #Calls | Latency(s) | ΔF1 vs single |\\n|-----------------|-------:|-------:|-----------:|---------------:|\\n| Single-Pass     | 0.130  |      1 |        10  |          —     |\\n| Random-k12      | 0.155  |     12 |        80  |      +2.5      |\\n| SDGD-zero-k12   | 0.150  |     12 |        85  |      +2.0      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN 上 SDGD-zero 不优于 random batching（甚至略低 0.5 点）， 直接否定 embedding SCS 作为 confusability proxy 的跨任务有效性。\\n\\n\\nMAVEN 上 SDGD-zero 对比 single-pass 增益 +2.0 F1 点（0.13→0.15）， 看似有提升，但对比 random batching（同样 12 batches）甚至略低（-0.5 点）。 这彻底证明增益来自 batch count reduction 而非 confusability-aware grouping。 Random batching 在 MAVEN 上略优于 SDGD-zero 的原因可能是： SDGD 的 graph coloring 将相似类型分开，但这导致每个 batch 内类型语义跨度大， LLM 更难维持一致的抽取策略（如一个 batch 同时包含 Conflict 事件和 Life 事件）， 反而略增加了混淆。这个 ironic 的结果表明 embedding SCS 不是有效的 confusability proxy——它分离的「相似」类型实际上不是 LLM 的混淆源。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on Few-NERD\",\n    \"description\": \"用 5-10 个 calibration examples 计算 empirical confusability（无梯度）， 构建 SDGD-cal。与 SDGD-zero 对比。\\n\",\n    \"results\": {\n      \"sdgd_cal_f1\": 0.44,\n      \"sdgd_zero_f1\": 0.43,\n      \"sdgd_cal_vs_zero_delta\": 1.0,\n      \"sdgd_cal_vs_zero_p\": 0.28,\n      \"sdgd_cal_n_batches\": 8,\n      \"calibration_cost_api_calls\": 66,\n      \"total_api_calls\": 74,\n      \"sdgd_cal_latency_seconds\": 420\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD-cal vs SDGD-zero (Few-NERD)\",\n        \"content\": \"| Method     |  F1    | Calibration Calls | Extraction Calls | Total | Latency(s) |\\n|------------|-------:|------------------:|-----------------:|------:|-----------:|\\n| SDGD-zero  | 0.430  |                 0 |                8 |     8 |        48  |\\n| SDGD-cal   | 0.440  |                66 |                8 |    74 |       420  |\\n| Δ          | +0.010 |               +66 |                0 |   +66 |      +372  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Empirical calibration 未能提供有意义的增益。少量 calibration data 下 confusion matrix 稀疏度过高，无法克服 embedding proxy 的局限性。 SDGD-cal 作为 contribution 不可行。\\n\\n\\nSDGD-cal 使用 empirical confusion matrix 替代 embedding SCS 构建 confusability graph， 理论上应更准确。但在 worst 档下，calibration 仅 5-10 examples， empirical confusion matrix 极度稀疏：66 types × 5 examples = 330 predictions， 大多数 type pair 的经验混淆计数为 0，无法可靠估计 pairwise confusability。 结果 SDGD-cal 仅比 SDGD-zero 高 1.0 F1 点（不显著, p=0.28）， 但 calibration 额外消耗 66 次 API call（每个 type 一次），总 latency 420s（7 分钟）， cost-benefit 极差。这是因为少量 calibration data 下 empirical 和 embedding 两种 proxy 都不可靠，所获信息增量接近零。\\n\"\n  },\n  {\n    \"name\": \"SDGD-cal on MAVEN\",\n    \"description\": \"SDGD-cal on 168 event types。Full comparison table。\\n\",\n    \"results\": {\n      \"sdgd_cal_f1\": 0.16,\n      \"sdgd_zero_f1\": 0.15,\n      \"random_batching_f1\": 0.155,\n      \"per_type_f1\": 0.18,\n      \"sdgd_cal_vs_random_delta\": 0.5,\n      \"sdgd_cal_vs_per_type_f1_ratio\": 0.89,\n      \"sdgd_cal_latency_seconds\": 1250,\n      \"per_type_latency_seconds\": 1680,\n      \"sdgd_cal_vs_per_type_latency_ratio\": 0.26,\n      \"calibration_cost_api_calls\": 168\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Full Comparison (MAVEN)\",\n        \"content\": \"| Method          |  F1    | #Calls | Latency(s) | ΔF1 vs single |\\n|-----------------|-------:|-------:|-----------:|---------------:|\\n| Single-Pass     | 0.130  |      1 |        10  |          —     |\\n| Random-k12      | 0.155  |     12 |        80  |      +2.5      |\\n| SDGD-zero-k12   | 0.150  |     12 |        85  |      +2.0      |\\n| SDGD-cal-k12    | 0.160  |    180 |      1250  |      +3.0      |\\n| Per-Type (k168) | 0.180  |    168 |      1680  |      +5.0      |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MAVEN full comparison 确认 SDGD 框架在 worst 档下无实质贡献。 Per-type splitting 仍是质量上限，SDGD 变体与 random batching 无显著差异。\\n\\n\\n168 个事件类型的 calibration 需要 168 次额外 API call， empirical confusion matrix 更加稀疏（168×167 = 28056 pairs，5 examples 每 type 几乎不可能覆盖）。SDGD-cal 仅比 SDGD-zero 高 1 F1 点（0.15→0.16）， 比 random batching 高 0.5 点（不显著）。Per-type splitting 仍是上限（0.18）， SDGD-cal 达到其 89%（符合 worst 档预测的 0.8-0.9 ratio）。 但 per-type 的 latency（1680s）远高于 SDGD-cal（1250s）， latency ratio 0.26 在 worst 档范围内。核心问题不变： SDGD-cal 的增益来自 batch size reduction，不来自 confusability-aware grouping。\\n\"\n  },\n  {\n    \"name\": \"Ablation: random batching\",\n    \"description\": \"Same batch count k as SDGD, random composition。 隔离 confusability-aware grouping vs batch count reduction。\\n\",\n    \"results\": {\n      \"random_k8_f1_fewnerd\": 0.435,\n      \"sdgd_zero_k8_f1_fewnerd\": 0.43,\n      \"sdgd_vs_random_delta_fewnerd\": -0.5,\n      \"sdgd_vs_random_p\": 0.72,\n      \"random_k8_f1_std\": 0.015,\n      \"random_5_seeds_f1_range\": [\n        0.42,\n        0.45\n      ],\n      \"random_k8_recall\": 0.395,\n      \"random_k8_precision\": 0.485\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SDGD vs Random Batching (Few-NERD, k=8)\",\n        \"content\": \"| Method       |  F1    |  F1 std |  R     |  P     | Δ vs SDGD |   p   |\\n|--------------|-------:|--------:|-------:|-------:|----------:|------:|\\n| SDGD-zero    | 0.430  |    —    | 0.390  | 0.480  |     —     |   —   |\\n| Random (s1)  | 0.420  |    —    | 0.380  | 0.470  |  -1.0     |       |\\n| Random (s2)  | 0.445  |    —    | 0.405  | 0.495  |  +1.5     |       |\\n| Random (s3)  | 0.430  |    —    | 0.390  | 0.480  |   0.0     |       |\\n| Random (s4)  | 0.450  |    —    | 0.410  | 0.500  |  +2.0     |       |\\n| Random (s5)  | 0.435  |    —    | 0.395  | 0.485  |  +0.5     |       |\\n| Random (avg) | 0.436  |  0.011 | 0.396  | 0.486  |  +0.6     | 0.72  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"决定性 negative result：SDGD-zero 不优于 random batching。 Embedding SCS 不是有效的 confusability proxy。 论文中 SDGD 从 contribution 降级为 discussion/future work。\\n\\n\\n这是 worst 档的决定性实验。Random batching（同 k=8）的 F1 为 0.435， 甚至略高于 SDGD-zero（0.430），差异 -0.5 点完全不显著（p=0.72）。 5 个 random seed 的 F1 range [0.42, 0.45] 完全包含 SDGD-zero 的 0.430。 这直接证明：SDGD 的全部增益来自 batch size reduction（从 64 types single-pass 到 ~8 types/batch），confusability-aware grouping 提供零额外价值。 Embedding SCS 不是有效的 confusability proxy：基于它的 graph coloring 分离出的类型组合与随机组合在 F1 上无差异。 这是对 Claim 3 (SDGD Effectiveness) 的直接否定。\\n\"\n  },\n  {\n    \"name\": \"Ablation: per-type splitting\",\n    \"description\": \"Per-type splitting (UniNER-style, 1 type per batch)。 Upper bound on decomposition benefit。\\n\",\n    \"results\": {\n      \"per_type_f1_fewnerd\": 0.5,\n      \"per_type_precision\": 0.42,\n      \"per_type_recall\": 0.62,\n      \"per_type_n_calls\": 64,\n      \"per_type_latency_seconds\": 385,\n      \"sdgd_zero_f1\": 0.43,\n      \"single_pass_f1\": 0.414,\n      \"sdgd_vs_pertype_f1_ratio\": 0.86,\n      \"sdgd_vs_pertype_latency_ratio\": 0.125\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Decomposition Strategy Comparison (Few-NERD)\",\n        \"content\": \"| Method       |  P     |  R     |  F1    | #Calls | Latency(s) | F1/PerType |\\n|--------------|-------:|-------:|-------:|-------:|-----------:|-----------:|\\n| Single-Pass  | 0.648  | 0.304  | 0.414  |      1 |          7 |    0.83    |\\n| Random-k8    | 0.486  | 0.396  | 0.436  |      8 |         48 |    0.87    |\\n| SDGD-zero-k8 | 0.480  | 0.390  | 0.430  |      8 |         48 |    0.86    |\\n| Per-Type     | 0.420  | 0.620  | 0.500  |     64 |        385 |    1.00    |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Per-type splitting 作为上限证明 batch decomposition 有价值， 但 SDGD 的 confusability-aware grouping 不提供超越 random 的增益。 论文可以报告 per-type 作为 practical baseline， 并讨论 \\\"intelligent decomposition\\\" 为何难以超越简单方案。\\n\\n\\nPer-type splitting 消除了 batch 内所有类型间交互（count=1, BCS=0）， 是 decomposition 的理论上限。F1=0.50 比 single-pass（0.414）高 ~9 points， 比 SDGD-zero（0.43）高 ~7 points。SDGD-zero 仅达到 per-type 的 86% （在 worst 档的 0.8-0.9 range 内）。 Per-type 的增益主要来自 recall 大幅提升（0.304→0.62）， 因为每个 batch 只有 1 个 type，模型不需要在多个类型间分配注意力。 但 precision 下降（0.648→0.42），因为 per-type 提示下模型倾向于 over-extract（只被告知一个类型时，模型会将更多 span 标注为该类型）。 Latency 385s（64 次 API call），是 SDGD-zero 的 8x（48s）。 SDGD-zero 的 latency ratio 0.125 在 worst 档范围下限。 结论：per-type splitting 虽然质量最高，但 SDGD 并非 \\\"match per-type at lower cost\\\" 的有效中间方案——它只是 random batching 的等价物。\\n\"\n  },\n  {\n    \"name\": \"SCS validation\",\n    \"description\": \"Embedding SCS vs empirical confusion matrix 的 rank correlation。 验证 embedding proxy 的实际有效性。\\n\",\n    \"results\": {\n      \"spearman_rho_scs_vs_empirical\": 0.12,\n      \"spearman_p\": 0.03,\n      \"kendall_tau\": 0.09,\n      \"kendall_p\": 0.04,\n      \"top_10_empirical_pairs_in_top_10_scs\": 2,\n      \"top_10_overlap_pct\": 0.2,\n      \"scs_auc_for_confusion_binary\": 0.56\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: SCS vs Empirical Confusion Correlation\",\n        \"content\": \"| Metric               | Value  |   p    |\\n|----------------------|-------:|-------:|\\n| Spearman ρ           |  0.12  | 0.030  |\\n| Kendall τ            |  0.09  | 0.040  |\\n| Top-10 overlap       |  2/10  |   —    |\\n| AUC (binary)         |  0.56  |   —    |\\n\"\n      },\n      {\n        \"name\": \"Table: Top-10 Empirical vs SCS Mismatch\",\n        \"content\": \"| Rank | Top Empirical Pair                          | In Top-10 SCS? |\\n|-----:|---------------------------------------------|----------------|\\n|    1 | person-other ↔ person-politician            |      Yes       |\\n|    2 | person-other ↔ organization-other           |       No       |\\n|    3 | location-GPE ↔ location-bodiesofwater       |       No       |\\n|    4 | person-scholar ↔ person-artist              |      Yes       |\\n|    5 | building-library ↔ building-other           |       No       |\\n|    6 | event-sportsevent ↔ event-other             |       No       |\\n|    7 | organization-company ↔ organization-other   |       No       |\\n|    8 | person-athlete ↔ person-other               |       No       |\\n|    9 | location-GPE ↔ location-other               |       No       |\\n|   10 | product-car ↔ product-other                 |       No       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"SCS 作为 confusability proxy 在实证检验中几乎失效（AUC=0.56 ≈ random）。 Top confused pairs 多涉及 \\\"-other\\\" 标签歧义，这是 schema design issue 而非 embedding similarity 能捕捉的。此 negative result 成为论文的 核心方法学贡献之一：证明 embedding similarity ≠ LLM confusability。\\n\\nEmbedding SCS 与 empirical confusion 的 rank correlation 很弱（ρ=0.12）， 虽然由于 n=1953 pairs 而 p<0.05（统计显著），但实际效应量极小。 Top-10 overlap 仅 20%（10 个最高经验混淆 pair 中仅 2 个也在最高 SCS pair 中）， 说明 embedding similarity 无法预测真实的混淆热点。 AUC=0.56（仅略高于 random 0.50），进一步证明 SCS 作为 binary confusion classifier 几乎无用。原因：(a) embedding similarity 捕捉的是语义接近性， 但 LLM 的 type confusion 更多由 schema 中的 type definition overlap、 training data 中的 type co-occurrence 和 prompt format 驱动； (b) 高 SCS pair 中很多是语义相关但 LLM 不混淆的 （如 \\\"building-library\\\" 和 \\\"building-hotel\\\" SCS 高但 LLM 不混淆）； (c) 低 SCS pair 中有些 LLM 频繁混淆 （如 \\\"person-other\\\" 和 \\\"organization-other\\\" SCS 较低但因 \\\"other\\\" 标签 歧义导致大量混淆）。这是 worst 档的关键 negative result， 直接否定 embedding SCS 作为 practical confusability proxy 的可行性。\\n\"\n  }\n]",
      "numLines": 338,
      "startLine": 1,
      "totalLines": 338
    }
  },
  "sourceToolAssistantUUID": "aa64c885-15a9-49c3-b5a3-a664221df100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T06:07:38.606Z_

<details><summary>↩ Tool result · `toolu_01X8pKLZ6wPsenhqk3SVcXqS`</summary>

```text
1	# Paper Framing — schema-dag-extraction
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25 cycle)
5	- Commitment deadline: August 2, 2026
6	- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
7	- Deadline: ARR May 25, 2026 (10 days from today)
8	
9	## Core Claims (3 conditions)
10	
11	1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.
12	
13	2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.
14	
15	3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).
16	
17	## Story Spine
18	
19	- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.
20	
21	- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.
22	
23	- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.
24	
25	- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.
26	
27	- **Headline result template**: "Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost."
28	
29	## Core Insight (Narrative A -- Multi-Channel Degradation)
30	
31	Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
32	- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.
33	- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Addressable by separating confusable types into different batches.
34	
35	These channels are orthogonal and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.
36	
37	## Evidence Hierarchy (D008 — restructured after type frequency confound discovery)
38	
39	**Layer 1 (Primary — strongest)**: Pairwise BCS-confusion analysis
40	- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs); nonzero-only Spearman ρ=0.254 (p=1.1e-6)
41	- Top confused pairs are all high-BCS semantic neighbors (e.g., person-other ↔ person-politician, BCS=0.934)
42	- This analysis is immune to type frequency confound (operates at type-pair level)
43	
44	**Layer 2 (Supporting — pending)**: Per-type F1 vs mean BCS analysis
45	- Controls for type frequency by computing F1 per type, not per batch
46	- Partial correlation controlling for type frequency
47	- Status: analysis in progress
48	
49	**Layer 3 (Discussion — transparent reporting)**: Batch-level BCS-F1 positive correlation
50	- Within-count batch-level r(F1, BCS) is POSITIVE (high BCS → high F1), opposite to naive prediction
51	- Explanation: type frequency confound — high-frequency types tend to have high BCS AND high F1
52	- This is NOT evidence for the hypothesis; reported transparently as methodological finding
53	- Demonstrates the importance of controlling for confounds — strengthens methodological rigor
54	
55	**Methodological note**: The positive batch-level correlation motivated our shift from batch-level to type-pair-level and per-type analysis. This progression (naive → controlled → mechanistic) is itself a methodological contribution.
56	
57	## Venue Fit Risks
58	
59	- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024) methodology.
60	- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.
61	- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.
62	- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.
63	
64	## Anticipated Reviewer Concerns
65	
66	| Concern | Response Strategy | Experiment |
67	|---------|------------------|------------|
68	| Only one model | Add >=1 more model | exp-012 |
69	| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |
70	| No practical method | SDGD framework | exp-008 to exp-011 |
71	| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |
72	| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |
73	| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |
74	| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |
75	| Type frequency confound | Transparent reporting: batch-level positive correlation + per-type and pairwise analysis controlling for frequency | exp-002, per-type analysis |
76	| BCS direction unexpected | Pairwise analysis (immune to frequency) confirms hypothesis; batch-level reported in discussion | exp-002 |
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea47959c-a8ed-4f3d-a040-d8c753e6b3f8",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "e5ba7e90-cd91-4551-9530-80dad4275859",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper_framing.md",
      "content": "# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (3 conditions)\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. Evidence required: within-count correlation r(metric, BCS) significant after controlling for count, replicated on >=2 datasets and >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the SCS-thresholded confusability graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\n\n## Story Spine\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches (per-type splitting, similarity-based partitioning, fixed k-step pipelines) operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). ProUIE/KGGen use fixed task-level decomposition (ignores intra-layer schema structure). No prior work isolates confusability from count in training-free LLM IE.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE. We discover a multi-channel degradation model: count drives recall decline (capacity bottleneck) while confusability drives type confusion (disambiguation failure). We then operationalize this into SDGD -- a principled framework for confusability-minimizing schema decomposition.\n\n- **Cross-task validation**: We validate on two complementary IE tasks — NER (Few-NERD, 66 fine-grained types) and Event Detection (MAVEN, 168 FrameNet-based event types). MAVEN's hierarchical type structure with known sibling confusion rates (14.6-19.8%) provides a natural testbed where confusability is independently documented. Cross-task replication (NER + ED) demonstrates confusability-aware decomposition is task-agnostic, not NER-specific.\n\n- **Headline result template**: \"Controlling for type count, batch confusability score (BCS) independently predicts F1 degradation (partial r=0.30, p<0.05), with high-confusability batches showing 10-28x more type confusion errors. SDGD-zero improves F1 by X points over single-pass on Few-NERD (66 types) and Y points on MAVEN (168 types), matching per-type splitting quality at Z% of the API cost.\"\n\n## Core Insight (Narrative A -- Multi-Channel Degradation)\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt -> attention dilution -> entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types -> interference during type assignment -> correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable. SDGD targets Channel 2; batch size reduction targets Channel 1; combining both yields additive gains.\n\n## Evidence Hierarchy (D008 — restructured after type frequency confound discovery)\n\n**Layer 1 (Primary — strongest)**: Pairwise BCS-confusion analysis\n- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs); nonzero-only Spearman ρ=0.254 (p=1.1e-6)\n- Top confused pairs are all high-BCS semantic neighbors (e.g., person-other ↔ person-politician, BCS=0.934)\n- This analysis is immune to type frequency confound (operates at type-pair level)\n\n**Layer 2 (Supporting — pending)**: Per-type F1 vs mean BCS analysis\n- Controls for type frequency by computing F1 per type, not per batch\n- Partial correlation controlling for type frequency\n- Status: analysis in progress\n\n**Layer 3 (Discussion — transparent reporting)**: Batch-level BCS-F1 positive correlation\n- Within-count batch-level r(F1, BCS) is POSITIVE (high BCS → high F1), opposite to naive prediction\n- Explanation: type frequency confound — high-frequency types tend to have high BCS AND high F1\n- This is NOT evidence for the hypothesis; reported transparently as methodological finding\n- Demonstrates the importance of controlling for confounds — strengthens methodological rigor\n\n**Methodological note**: The positive batch-level correlation motivated our shift from batch-level to type-pair-level and per-type analysis. This progression (naive → controlled → mechanistic) is itself a methodological contribution.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024) methodology.\n- **Training-free IE relevance**: Cite deployment scenarios -- clinical (mCODEGPT), regulatory (FINRA 2026), multilingual (50+ languages with no IE corpora). Training-free is sometimes the ONLY option.\n- **Multi-model generalizability**: MVP used only Qwen3-32B. Need >=2 models. Plan: add one model from different family.\n- **Over-prediction confound**: F1 curve reversal at low counts needs careful framing. Present recall as clean degradation signal; precision artifact explained in methodology section.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | Add >=1 more model | exp-012 |\n| Only one dataset for Claim 1 | Replicate on MAVEN (168 event types, cross-task) + optionally DocRED | exp-004, exp-005 |\n| No practical method | SDGD framework | exp-008 to exp-011 |\n| Confusability measure validity | SCS validation: embedding vs empirical | exp-015 |\n| Effect size small | Report batch-level + type-pair-level + error decomposition | exp-006, exp-007 |\n| Why not just per-type splitting? | Ablation: SDGD vs per-type vs random | exp-013, exp-014 |\n| Latency overhead of decomposition | Report API calls and wall-clock time | exp-008 |\n| Type frequency confound | Transparent reporting: batch-level positive correlation + per-type and pairwise analysis controlling for frequency | exp-002, per-type analysis |\n| BCS direction unexpected | Pairwise analysis (immune to frequency) confirms hypothesis; batch-level reported in discussion | exp-002 |\n",
      "numLines": 77,
      "startLine": 1,
      "totalLines": 77
    }
  },
  "sourceToolAssistantUUID": "ea47959c-a8ed-4f3d-a040-d8c753e6b3f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T06:07:38.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X8pKLZ6wPsenhqk3SVcXqS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38964f37-49f0-4f60-85e6-9ba85e5e95e4",
  "isSidechain": false,
  "requestId": "req_011Cb3rUc5bMwP69LTEXSfQy",
  "type": "assistant",
  "uuid": "ea47959c-a8ed-4f3d-a040-d8c753e6b3f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WScDnMRHWcsURDHDP5JQZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11389,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11389,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11389,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11389
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "e5ba7e90-cd91-4551-9530-80dad4275859",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Assistant

_source line 14 · 2026-05-15T06:07:47.697Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and the paper framing. Let me write the LaTeX paper based on the narrative guidance for the "worst" tier.

Key narrative points for worst tier:
1. Core hypothesis (embedding-based confusability independently separable) doesn't hold
2. Reframe as empirical anatomy of schema complexity in training-free LLM IE
3. An analysis/methodology paper, not a method paper
4. Core contributions:
   - Frequency-confusability confound discovery
   - Batch-level vs pairwise analysis methodology lesson
   - Count→recall monotonic degradation evidence
   - Negative result on embedding SCS as confusability proxy
5. SDGD becomes discussion/future work, not a contribution
6. Target: EMNLP main (empirical/analysis track), "Lost in the Middle" style

Now I'm setting up the LaTeX document and writing out the full paper with this reframed narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ba7e90-cd91-4551-9530-80dad4275859",
  "isSidechain": false,
  "requestId": "req_011Cb3rUthiVXbsRd2Hwhajf",
  "type": "assistant",
  "uuid": "9582cbf4-634d-490c-b3e1-b573282fc106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AmeZmeMczDM8r9DjEGszB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15500,
      "cache_read_input_tokens": 23230,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 23230,
          "cache_creation_input_tokens": 15500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15500
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

_source line 15 · 2026-05-15T06:07:47.697Z_

Now I have all the data. Let me create the output directory and write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9582cbf4-634d-490c-b3e1-b573282fc106",
  "isSidechain": false,
  "requestId": "req_011Cb3rUthiVXbsRd2Hwhajf",
  "type": "assistant",
  "uuid": "600641b9-ef1d-4205-b4a4-96d1bd471314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AmeZmeMczDM8r9DjEGszB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15500,
      "cache_read_input_tokens": 23230,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 23230,
          "cache_creation_input_tokens": 15500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15500
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

_source line 16 · 2026-05-15T06:07:48.812Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M8UDTLHw969K2Zb79dXYMJ`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600641b9-ef1d-4205-b4a4-96d1bd471314",
  "isSidechain": false,
  "requestId": "req_011Cb3rUthiVXbsRd2Hwhajf",
  "type": "assistant",
  "uuid": "87167270-8183-498a-b4bb-bfc44f750027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019AmeZmeMczDM8r9DjEGszB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15500,
      "cache_read_input_tokens": 23230,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 23230,
          "cache_creation_input_tokens": 15500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15500
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

_source line 17 · 2026-05-15T06:07:49.005Z_

<details><summary>↩ Tool result · `toolu_01M8UDTLHw969K2Zb79dXYMJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87167270-8183-498a-b4bb-bfc44f750027",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "4d9aaa95-a73a-49ae-8d67-4c5cb7e7bbfe",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "87167270-8183-498a-b4bb-bfc44f750027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T06:10:25.498Z_

<details open><summary>🔧 Tool call — Write · `toolu_01WUJabrts477ruWEkebTevv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\n\\title{Anatomy of Schema Complexity in Training-Free LLM Information Extraction:\\\\A Controlled Study of Type Count, Confusability, and Their Entanglement}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM-based information extraction degrades severely on complex schemas, yet the mechanisms driving this degradation remain poorly understood.\nWe conduct a controlled empirical study across three IE tasks---NER (Few-NERD, 66 types), Event Detection (MAVEN, 168 types), and Relation Extraction (DocRED, 96 types)---isolating the effects of type count and type confusability on extraction quality.\nWe report four findings.\nFirst, type count drives monotonic recall decline across all tasks and models: recall drops from 0.58 to 0.10 on MAVEN (1$\\to$168 types) and from 0.60 to 0.28 on Few-NERD (1$\\to$64 types).\nSecond, embedding-based semantic confusability scores (SCS), widely assumed to proxy inter-type confusability, fail as independent predictors of extraction degradation once type frequency is controlled (partial $r$=0.05, $p$=0.38 on MAVEN; BCS main effect $p$=0.42 in factorial analysis on Few-NERD).\nThird, a pairwise BCS-confusion correlation observed on one model (Qwen3-32B, $r$=0.156, $p$=4.6e-12) fails to replicate on a second model (LLaMA-3.3-70B, $r$=0.05, $p$=0.08), indicating model-specificity rather than a general phenomenon.\nFourth, confusability-aware schema decomposition (SDGD) provides no significant gain over random batching at the same granularity ($\\Delta$F1=$-$0.5, $p$=0.72), confirming that decomposition benefits derive entirely from batch size reduction, not confusability-aware grouping.\nThese results expose a previously unrecognized frequency--confusability confound and establish that batch-level confusability analysis is methodologically unreliable.\nWe advocate pairwise analysis as the methodological standard and characterize the conditions under which embedding similarity does and does not predict LLM type confusion.\n\\end{abstract}\n\n\\section{Introduction}\n\nTraining-free LLM-based information extraction---prompting large language models with schema definitions and extracting structured information without task-specific fine-tuning---has emerged as a practical paradigm for deployment scenarios where labeled data is unavailable: clinical NLP \\cite{}, regulatory compliance \\cite{}, and multilingual IE across 50+ languages with no IE corpora \\cite{}.\nHowever, extraction quality degrades severely as schema complexity increases, with 20--60 F1-point gaps compared to supervised methods on complex schemas \\cite{}.\n\nPrior work has proposed various decomposition strategies to mitigate this degradation.\nUniNER \\cite{} splits extraction into per-type passes, gaining 3.3 F1 but sacrificing cross-type context.\nLLM-PEE \\cite{} uses type similarity as an implicit confusability proxy without empirical validation.\nProUIE \\cite{} and KGGen \\cite{} employ fixed task-level decomposition that ignores intra-layer schema structure.\nAll these approaches operate on unvalidated assumptions about \\emph{what} makes schemas complex for LLMs---specifically, the assumption that semantically similar types confuse the model and that separating them improves extraction.\n\nThis assumption has intuitive appeal but has never been empirically isolated from a confounding factor: type count.\nSchemas with many types tend to contain more semantically similar pairs, making it impossible to attribute degradation to confusability versus count without controlled analysis.\n\nWe conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE.\nOur study spans three tasks (NER, Event Detection, Relation Extraction), two models (Qwen3-32B, LLaMA-3.3-70B), and employs both batch-level and pairwise analysis methodologies.\nOur core finding is \\textbf{negative}: embedding-based confusability, once frequency is controlled, does not independently predict extraction degradation.\nThis negative result carries important methodological and practical implications:\n\n\\begin{enumerate}\n\\item We discover and quantify a \\textbf{frequency--confusability confound} that invalidates batch-level confusability analysis---high-frequency types tend to have both high confusability scores and high F1, producing spurious positive correlations.\n\\item We demonstrate that \\textbf{batch-level analysis is unreliable} and that pairwise type-pair analysis is necessary for valid confusability studies.\n\\item We provide clean evidence of \\textbf{count$\\to$recall monotonic degradation} as the primary mechanism of schema-induced quality loss.\n\\item We report a rigorous \\textbf{negative result on embedding SCS as a confusability proxy}: SCS achieves AUC=0.56 for predicting actual type confusion (near random), and confusability-aware decomposition provides no benefit over random batching.\n\\end{enumerate}\n\n\\section{Background and Related Work}\n\n\\paragraph{Training-free LLM IE.}\nThe paradigm of prompting LLMs with type definitions for zero-shot IE has been explored across NER \\cite{}, relation extraction \\cite{}, and event detection \\cite{}.\nPerformance degrades with schema complexity, but the degradation mechanisms have not been systematically studied.\n\n\\paragraph{Schema decomposition.}\nUniNER decomposes NER into per-type binary extraction passes.\nLLM-PEE partitions types by embedding similarity.\nThese approaches implicitly assume that type confusability drives degradation but provide no controlled evidence separating confusability effects from count effects.\n\n\\paragraph{Confusability in classification.}\nConfusion between semantically similar categories is well-documented in image classification \\cite{} and text classification \\cite{}.\nHowever, LLM IE differs fundamentally: the model receives explicit type definitions in the prompt, and confusion patterns may be driven by prompt formatting, type definition overlap, and training data biases rather than label-space geometry.\n\n\\section{Methodology}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Datasets.}\nWe use three datasets spanning distinct IE tasks:\n\\textbf{Few-NERD} (66 fine-grained entity types, flat schema),\n\\textbf{MAVEN} (168 event types, FrameNet hierarchy),\nand \\textbf{DocRED} (96 relation types, document-level).\nFew-NERD serves as the primary testbed; MAVEN and DocRED provide cross-task validation.\n\n\\paragraph{Models.}\nWe evaluate on Qwen3-32B (primary) and LLaMA-3.3-70B-Instruct (validation), representing different model families and scales.\n\n\\paragraph{Extraction protocol.}\nFor each dataset, we prompt the model with a type schema (subset or full) and a set of test instances, using text-match evaluation.\nWe systematically vary the number of types in the prompt (count variable) and the semantic similarity structure of the included types (confusability variable).\n\n\\subsection{Confusability Measurement}\n\n\\paragraph{Schema Confusability Score (SCS).}\nFor each pair of types $(t_i, t_j)$, we compute the cosine similarity of their label embeddings using all-MiniLM-L6-v2.\nThe Batch Confusability Score (BCS) of a type set $T$ is the mean pairwise SCS:\n\\begin{equation}\n\\text{BCS}(T) = \\frac{2}{|T|(|T|-1)} \\sum_{i<j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\n\\paragraph{Empirical confusion.}\nWe construct an empirical confusion matrix from model predictions, recording how often type $t_i$ is predicted when the gold label is $t_j$.\n\n\\subsection{Analysis Methodology}\n\nWe employ three complementary analysis strategies:\n\n\\textbf{Count curve analysis}: Vary type count while holding confusability constant (or averaging over it). Measures the count$\\to$performance channel.\n\n\\textbf{Factorial analysis}: 2$\\times$2 design crossing \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for main effects and interaction.\n\n\\textbf{Pairwise analysis}: Correlate pairwise SCS with pairwise empirical confusion counts. Immune to batch-level frequency confounds.\n\n\\section{Experiment 1: Count$\\to$Recall Degradation}\n\nWe first establish the count channel as the primary degradation mechanism.\n\n\\subsection{Few-NERD}\n\nTable~\\ref{tab:fewnerd_count} shows extraction performance as a function of type count.\nRecall declines monotonically from 0.60 (count=1) to 0.28 (count=64) on LLaMA-3.3-70B, confirming that adding types to the prompt systematically reduces the model's ability to identify entities.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{r|cc|cc|c}\n\\toprule\n& \\multicolumn{2}{c|}{Qwen3-32B} & \\multicolumn{2}{c|}{LLaMA-3.3-70B} & \\\\\nCount & F1 & R & F1 & R & $\\Delta$F1 \\\\\n\\midrule\n1  & 0.323 & --- & 0.290 & 0.600 & $-$0.033 \\\\\n6  & 0.306 & --- & 0.280 & --- & $-$0.026 \\\\\n12 & 0.347 & --- & 0.310 & --- & $-$0.037 \\\\\n44 & 0.445 & --- & 0.400 & --- & $-$0.045 \\\\\n64 & 0.414 & 0.304 & 0.370 & 0.280 & $-$0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Count curve on Few-NERD. Both models exhibit consistent recall degradation as type count increases. $\\Delta$F1 = LLaMA $-$ Qwen3.}\n\\label{tab:fewnerd_count}\n\\end{table}\n\n\\subsection{MAVEN (168 Event Types)}\n\nTable~\\ref{tab:maven_count} shows the count curve on MAVEN, which exhibits more severe degradation due to the larger type space.\nRecall drops from 0.58 (count=1) to 0.10 (count=168), a 83\\% reduction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcccc|c}\n\\toprule\nCount & P & R & F1 & pred/gold & WrongType \\\\\n\\midrule\n1   & 0.170 & 0.580 & 0.280 & 3.41 &    0 \\\\\n6   & 0.195 & 0.410 & 0.270 & 2.10 &  310 \\\\\n20  & 0.225 & 0.300 & 0.260 & 1.33 &  640 \\\\\n50  & 0.240 & 0.220 & 0.230 & 0.92 &  820 \\\\\n100 & 0.215 & 0.150 & 0.180 & 0.70 & 1950 \\\\\n168 & 0.185 & 0.100 & 0.130 & 0.54 & 3100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MAVEN count curve (Qwen3-32B). Recall declines monotonically from 0.58 to 0.10. WrongType errors increase from 0 to 3100 as more types compete for assignment.}\n\\label{tab:maven_count}\n\\end{table}\n\n\\subsection{DocRED (96 Relation Types)}\n\nDocRED exhibits an extreme floor effect (Table~\\ref{tab:docred_count}), with full-schema F1 at just 6\\%.\nTraining-free LLM RE on complex schemas is largely non-functional, limiting the statistical power of confusability analysis on this dataset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rccc}\n\\toprule\nCount & P & R & F1 \\\\\n\\midrule\n1  & 0.150 & 0.320 & 0.220 \\\\\n10 & 0.165 & 0.180 & 0.170 \\\\\n30 & 0.130 & 0.110 & 0.120 \\\\\n96 & 0.085 & 0.050 & 0.060 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED count curve (Qwen3-32B). Floor effect at full schema (F1=6\\%) limits confusability analysis.}\n\\label{tab:docred_count}\n\\end{table}\n\n\\paragraph{Summary.}\nCount$\\to$recall degradation is the single most robust finding across all three tasks and both models.\nRecall decline is monotonic, substantial, and consistent.\nThis establishes the baseline against which any confusability effect must be measured.\n\n\\section{Experiment 2: Testing Confusability Independence}\n\n\\subsection{Factorial Analysis on Few-NERD}\n\nWe conduct a 2$\\times$2 factorial experiment crossing type count (low/high) with BCS (low/high) on Few-NERD (Table~\\ref{tab:factorial}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc|c}\n\\toprule\n         & Low BCS & High BCS & $\\Delta$(BCS) \\\\\n\\midrule\nLow Count  & 0.340 & 0.330 & $-$0.010 \\\\\nHigh Count & 0.310 & 0.300 & $-$0.010 \\\\\n\\midrule\n$\\Delta$(Count) & $-$0.030 & $-$0.030 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{2$\\times$2 factorial F1 results on Few-NERD (Qwen3-32B). BCS has negligible effect ($\\Delta$=0.01) compared to count ($\\Delta$=0.03).}\n\\label{tab:factorial}\n\\end{table}\n\nTable~\\ref{tab:anova} shows the two-way ANOVA results.\nThe count main effect is marginally significant ($\\eta^2$=0.08, $p$=0.04), but the BCS main effect is not significant ($\\eta^2$=0.01, $p$=0.42).\nThe interaction term is negligible ($\\eta^2 \\approx$ 0, $p$=0.88).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrc}\n\\toprule\nSource & SS & df & $F$ & $p$ & $\\eta^2$ \\\\\n\\midrule\nCount     & 0.0180 & 1 & 4.25 & 0.040 & 0.080 \\\\\nBCS       & 0.0022 & 1 & 0.52 & 0.420 & 0.010 \\\\\nCount$\\times$BCS & 0.0002 & 1 & 0.05 & 0.880 & 0.001 \\\\\nResidual  & 0.2100 & 96 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Two-way ANOVA. BCS main effect is not significant after controlling for count. The interaction is zero, indicating confusability is not an independent factor.}\n\\label{tab:anova}\n\\end{table}\n\n\\subsection{Within-Count BCS Correlation on MAVEN}\n\nOn MAVEN, within-count BCS--F1 correlations are uniformly non-significant (Table~\\ref{tab:maven_bcs}).\nThe partial correlation controlling for count is $r$=0.05, $p$=0.38.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrrl}\n\\toprule\nCount & $r$(F1,BCS) & $p$ & $n$ & Verdict \\\\\n\\midrule\n6   & 0.04 & 0.420 & 25 & FAIL \\\\\n20  & 0.08 & 0.280 & 25 & FAIL \\\\\npartial & 0.05 & 0.380 & 50 & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MAVEN within-count BCS--F1 correlation. No evidence for confusability independence on event detection.}\n\\label{tab:maven_bcs}\n\\end{table}\n\n\\subsection{Pairwise BCS--Confusion Analysis}\n\nPairwise analysis on Few-NERD with Qwen3-32B yields a statistically significant but small correlation ($r$=0.156, $p$=4.6e-12), which is the strongest evidence for a confusability signal in our study.\nHowever, this result fails to replicate on LLaMA-3.3-70B ($r$=0.05, $p$=0.08) and on MAVEN ($r$=0.04, $p$=0.12), as shown in Table~\\ref{tab:pairwise}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\nDataset & Model & $n$ & $r$ & $p$ & $\\rho_{\\text{nz}}$ \\\\\n\\midrule\nFew-NERD & Qwen3-32B     & 1953  & 0.156 & 4.6e-12 & 0.254 \\\\\nFew-NERD & LLaMA-3.3-70B & 1953  & 0.050 & 0.080   & 0.070 \\\\\nMAVEN    & Qwen3-32B     & 14028 & 0.040 & 0.120   & 0.060 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise BCS--confusion correlations. The Few-NERD/Qwen3 result ($r$=0.156) does not replicate across models or tasks. $\\rho_{\\text{nz}}$: Spearman $\\rho$ on nonzero confusion pairs.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe Few-NERD/Qwen3-32B pairwise signal, while statistically significant, appears model-specific.\nThe failure to replicate on a second model from a different family (LLaMA-3.3) and on a second task (MAVEN) prevents us from claiming confusability independence as a general phenomenon.\n\n\\section{Experiment 3: Error Taxonomy}\n\nIf confusability drives a distinct error channel (type substitution), we should observe more type substitution errors in high-BCS conditions after controlling for frequency.\nTable~\\ref{tab:errors} shows the error taxonomy across BCS bins with frequency controlled.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc|cc}\n\\toprule\nError Type & High BCS & Low BCS & Ratio & $\\chi^2$ $p$ \\\\\n\\midrule\nType Substitution & 18.0\\% & 15.0\\% & 1.20 & 0.180 \\\\\nBoundary Error    & 22.0\\% & 20.0\\% & 1.10 & 0.350 \\\\\nFalse Negative    & 45.0\\% & 48.0\\% & 0.94 & 0.410 \\\\\nHallucination     & 15.0\\% & 17.0\\% & 0.88 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error taxonomy by BCS bin (Few-NERD, frequency-controlled). No significant difference in type substitution between high- and low-BCS conditions.}\n\\label{tab:errors}\n\\end{table}\n\nNone of the error type proportions differ significantly between BCS bins.\nFalse negatives dominate uniformly (45--48\\%), consistent with count-driven recall decline as the primary degradation mechanism.\nType substitution shows only a non-significant 1.2$\\times$ ratio ($p$=0.18), insufficient to support a distinct confusability$\\to$type confusion channel.\n\n\\section{Experiment 4: Validating the Confusability Proxy}\n\nWe directly evaluate embedding SCS as a proxy for empirical LLM confusion (Table~\\ref{tab:scs_validation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSpearman $\\rho$ (SCS vs.\\ empirical confusion) & 0.12 ($p$=0.03) \\\\\nKendall $\\tau$ & 0.09 ($p$=0.04) \\\\\nTop-10 pair overlap & 2/10 (20\\%) \\\\\nAUC (binary confusion prediction) & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SCS vs.\\ empirical confusion. Despite weak statistical significance ($p$<0.05 due to large $n$), practical predictive value is near-random (AUC=0.56).}\n\\label{tab:scs_validation}\n\\end{table}\n\nThe rank correlation is weak ($\\rho$=0.12) and barely exceeds chance for binary prediction (AUC=0.56).\nTable~\\ref{tab:mismatch} reveals the source of the mismatch: the most confused type pairs predominantly involve ``-other'' label ambiguity (e.g., \\texttt{person-other} $\\leftrightarrow$ \\texttt{organization-other}), a schema design phenomenon that embedding similarity cannot capture.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rlc}\n\\toprule\nRank & Top Empirical Confusion Pair & In Top-10 SCS? \\\\\n\\midrule\n1 & person-other $\\leftrightarrow$ person-politician & Yes \\\\\n2 & person-other $\\leftrightarrow$ organization-other & No \\\\\n3 & location-GPE $\\leftrightarrow$ location-bodiesofwater & No \\\\\n4 & person-scholar $\\leftrightarrow$ person-artist & Yes \\\\\n5 & building-library $\\leftrightarrow$ building-other & No \\\\\n6 & event-sportsevent $\\leftrightarrow$ event-other & No \\\\\n7 & organization-company $\\leftrightarrow$ organization-other & No \\\\\n8 & person-athlete $\\leftrightarrow$ person-other & No \\\\\n9 & location-GPE $\\leftrightarrow$ location-other & No \\\\\n10 & product-car $\\leftrightarrow$ product-other & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 empirically confused type pairs. Only 2/10 overlap with top-10 SCS pairs. Confusion is driven by ``-other'' label ambiguity, not embedding similarity.}\n\\label{tab:mismatch}\n\\end{table}\n\n\\section{Experiment 5: Schema Decomposition}\n\nDespite the negative confusability results, schema decomposition itself (reducing the number of types per prompt) does improve performance, as shown by the count curves.\nWe evaluate whether confusability-\\emph{aware} decomposition (SDGD) provides benefit beyond simple batch size reduction.\n\n\\subsection{Few-NERD}\n\nTable~\\ref{tab:decomp_fewnerd} compares all decomposition strategies on Few-NERD.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & P & R & F1 & Calls & Lat.(s) \\\\\n\\midrule\nSingle-Pass      & 0.648 & 0.304 & 0.414 &  1 &   7 \\\\\nRandom-$k$8 (avg)& 0.486 & 0.396 & 0.436 &  8 &  48 \\\\\nSDGD-zero-$k$8   & 0.480 & 0.390 & 0.430 &  8 &  48 \\\\\nSDGD-cal-$k$8    & 0.480 & 0.390 & 0.440 & 74 & 420 \\\\\nPer-Type ($k$64) & 0.420 & 0.620 & 0.500 & 64 & 385 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition strategies on Few-NERD. SDGD-zero does not outperform random batching at the same $k$.}\n\\label{tab:decomp_fewnerd}\n\\end{table}\n\nSDGD-zero (F1=0.430) performs \\emph{below} random batching (F1=0.436, averaged over 5 seeds), with $\\Delta$F1=$-$0.5 ($p$=0.72).\nSDGD-cal adds 66 calibration API calls for a further non-significant +1.0 F1 gain ($p$=0.28) at 8.8$\\times$ the latency.\nPer-type splitting remains the quality upper bound (F1=0.500).\n\nTable~\\ref{tab:random_seeds} shows that SDGD-zero falls within the variance of random batching.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & F1 std & $\\Delta$ vs SDGD & $p$ \\\\\n\\midrule\nSDGD-zero  & 0.430 & --- & --- & --- \\\\\nRandom (s1) & 0.420 & & $-$1.0 & \\\\\nRandom (s2) & 0.445 & & +1.5 & \\\\\nRandom (s3) & 0.430 & & 0.0 & \\\\\nRandom (s4) & 0.450 & & +2.0 & \\\\\nRandom (s5) & 0.435 & & +0.5 & \\\\\n\\midrule\nRandom (avg) & 0.436 & 0.011 & +0.6 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD-zero vs.\\ 5 random batching seeds ($k$=8, Few-NERD). SDGD falls within the random variance.}\n\\label{tab:random_seeds}\n\\end{table}\n\n\\subsection{MAVEN}\n\nTable~\\ref{tab:decomp_maven} extends the comparison to MAVEN's 168 event types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & Calls & Lat.(s) & $\\Delta$F1 vs single \\\\\n\\midrule\nSingle-Pass     & 0.130 &   1 &   10 & --- \\\\\nRandom-$k$12    & 0.155 &  12 &   80 & +2.5 \\\\\nSDGD-zero-$k$12 & 0.150 &  12 &   85 & +2.0 \\\\\nSDGD-cal-$k$12  & 0.160 & 180 & 1250 & +3.0 \\\\\nPer-Type ($k$168)& 0.180 & 168 & 1680 & +5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition strategies on MAVEN. SDGD-zero underperforms random batching ($-$0.5 F1) while SDGD-cal's marginal gain costs 15$\\times$ more API calls.}\n\\label{tab:decomp_maven}\n\\end{table}\n\nSDGD-zero is 0.5 F1 points \\emph{below} random batching on MAVEN.\nThe confusability-aware grouping may actually hurt by forcing semantically diverse types into the same batch, disrupting the model's extraction consistency.\n\n\\section{Discussion}\n\n\\paragraph{The frequency--confusability confound.}\nOur most important methodological finding is that type frequency confounds batch-level confusability analysis.\nHigh-frequency types in Few-NERD tend to be fine-grained subtypes within the same coarse category (e.g., multiple \\texttt{person-*} types), which naturally have high pairwise SCS.\nThese same types also have higher per-type F1 due to frequency effects.\nThe result is a spurious positive correlation between BCS and batch F1---the opposite of the confusability hypothesis prediction.\nThis confound is invisible in batch-level analysis and requires per-type or pairwise analysis to detect.\n\n\\paragraph{Why embedding SCS fails as a confusability proxy.}\nSCS captures semantic proximity in label embedding space, but LLM type confusion is driven by different mechanisms:\n(1) ``-other'' label ambiguity, a schema design artifact where underspecified catch-all categories absorb mentions from multiple specific types;\n(2) trigger/mention polysemy, where the same surface form maps to different types depending on context;\n(3) training data biases in type co-occurrence that shape the model's prior over type assignments.\nNone of these mechanisms are captured by static embedding similarity, explaining the near-random AUC of 0.56.\n\n\\paragraph{When does the pairwise signal exist?}\nThe Few-NERD/Qwen3-32B pairwise result ($r$=0.156) is real but model-specific.\nWe hypothesize this reflects an alignment between Qwen3's internal type representations and the all-MiniLM-L6-v2 embedding space---an accident of training data overlap rather than a general property of LLMs.\nLLaMA-3.3-70B, trained on different data with a different architecture, shows no such alignment.\n\n\\paragraph{Practical implications for schema decomposition.}\nOur results suggest a simple prescription: when decomposing complex schemas, batch size reduction is all that matters.\nRandom partitioning into $k$ batches of roughly equal size is sufficient; confusability-aware grouping adds cost without benefit.\nPer-type splitting remains the quality upper bound but at proportionally higher latency.\nThe optimal $k$ is a cost--quality tradeoff that depends on the deployment scenario.\n\n\\paragraph{Limitations and future directions.}\nSeveral limitations constrain our conclusions.\nFirst, our SCS measure uses a single sentence embedding model (all-MiniLM-L6-v2); alternative embeddings (e.g., from the target LLM itself) might yield better confusability proxies.\nSecond, our calibration approach uses only 5--10 examples per type; larger calibration sets could overcome the sparsity problem.\nThird, we evaluate only two LLMs; broader model coverage may reveal architectures where embedding confusability is more predictive.\nSDGD could potentially be revived with better confusability proxies---e.g., using the LLM's own logit-based confusion signals or leveraging schema metadata (hierarchical structure, definition overlap).\n\n\\section{Conclusion}\n\nWe present a controlled empirical study of schema complexity in training-free LLM information extraction.\nOur findings challenge the widely held assumption that type confusability independently drives extraction degradation: once type frequency is controlled, embedding-based confusability scores do not predict performance, confusability-aware decomposition does not outperform random batching, and the error distribution does not differ between high- and low-confusability conditions.\n\nThe primary degradation mechanism is type count: more types in the prompt cause monotonic recall decline, robustly replicated across three tasks and two models.\nThis count channel accounts for the vast majority of schema-induced quality loss, with confusability at best a minor, model-specific, and task-specific secondary factor.\n\nOur methodological contribution---exposing the frequency--confusability confound and demonstrating the unreliability of batch-level analysis---has implications beyond this study, as any future work on type confusability in IE must control for this confound.\nWe release our experimental framework and data to support such future work.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\\section{DocRED Supplementary Results}\n\\label{app:docred}\n\nDocRED exhibits an extreme floor effect, with full-schema F1 at 6\\%.\nPairwise BCS--confusion correlation is not significant ($r$=0.02, $p$=0.35).\nThe partial correlation controlling for frequency is $r$=$-$0.03, $p$=0.62.\nThe confusion ratio between extreme BCS batches is 1.1$\\times$, indicating no confusability effect.\nThese results are consistent with the main findings but lack statistical power due to the low baseline performance.\n\n\\section{SDGD-cal Detailed Results}\n\nOn Few-NERD, SDGD-cal uses 66 calibration API calls (one per type with 5 examples) to construct an empirical confusion matrix.\nDespite the added cost, SDGD-cal improves over SDGD-zero by only 1.0 F1 point ($p$=0.28).\nWith 5 examples per type, the empirical confusion matrix is extremely sparse---most of the 66$\\times$65 = 4290 type pairs have zero observed confusion---limiting the information gain over the embedding proxy.\n\nOn MAVEN, calibration requires 168 additional API calls.\nSDGD-cal achieves F1=0.16, only 0.5 points above random batching and 2.0 points below per-type splitting.\nThe calibration cost (1250s total latency) approaches per-type splitting (1680s) without matching its quality, yielding a poor cost--benefit ratio.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d9aaa95-a73a-49ae-8d67-4c5cb7e7bbfe",
  "isSidechain": false,
  "requestId": "req_011Cb3rVf4DAy54fYgfYroQu",
  "type": "assistant",
  "uuid": "a00b5408-a59d-41de-a7b6-364c4604bcd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193H3GFx1258rDACxRF6a68",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 385,
      "cache_read_input_tokens": 38730,
      "output_tokens": 8805,
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
          "output_tokens": 8805,
          "cache_read_input_tokens": 38730,
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

### Tool result

_source line 19 · 2026-05-15T06:10:25.520Z_

<details><summary>↩ Tool result · `toolu_01WUJabrts477ruWEkebTevv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a00b5408-a59d-41de-a7b6-364c4604bcd1",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "62de3520-b70d-485d-846d-7531b65df92c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\n\\title{Anatomy of Schema Complexity in Training-Free LLM Information Extraction:\\\\A Controlled Study of Type Count, Confusability, and Their Entanglement}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nTraining-free LLM-based information extraction degrades severely on complex schemas, yet the mechanisms driving this degradation remain poorly understood.\nWe conduct a controlled empirical study across three IE tasks---NER (Few-NERD, 66 types), Event Detection (MAVEN, 168 types), and Relation Extraction (DocRED, 96 types)---isolating the effects of type count and type confusability on extraction quality.\nWe report four findings.\nFirst, type count drives monotonic recall decline across all tasks and models: recall drops from 0.58 to 0.10 on MAVEN (1$\\to$168 types) and from 0.60 to 0.28 on Few-NERD (1$\\to$64 types).\nSecond, embedding-based semantic confusability scores (SCS), widely assumed to proxy inter-type confusability, fail as independent predictors of extraction degradation once type frequency is controlled (partial $r$=0.05, $p$=0.38 on MAVEN; BCS main effect $p$=0.42 in factorial analysis on Few-NERD).\nThird, a pairwise BCS-confusion correlation observed on one model (Qwen3-32B, $r$=0.156, $p$=4.6e-12) fails to replicate on a second model (LLaMA-3.3-70B, $r$=0.05, $p$=0.08), indicating model-specificity rather than a general phenomenon.\nFourth, confusability-aware schema decomposition (SDGD) provides no significant gain over random batching at the same granularity ($\\Delta$F1=$-$0.5, $p$=0.72), confirming that decomposition benefits derive entirely from batch size reduction, not confusability-aware grouping.\nThese results expose a previously unrecognized frequency--confusability confound and establish that batch-level confusability analysis is methodologically unreliable.\nWe advocate pairwise analysis as the methodological standard and characterize the conditions under which embedding similarity does and does not predict LLM type confusion.\n\\end{abstract}\n\n\\section{Introduction}\n\nTraining-free LLM-based information extraction---prompting large language models with schema definitions and extracting structured information without task-specific fine-tuning---has emerged as a practical paradigm for deployment scenarios where labeled data is unavailable: clinical NLP \\cite{}, regulatory compliance \\cite{}, and multilingual IE across 50+ languages with no IE corpora \\cite{}.\nHowever, extraction quality degrades severely as schema complexity increases, with 20--60 F1-point gaps compared to supervised methods on complex schemas \\cite{}.\n\nPrior work has proposed various decomposition strategies to mitigate this degradation.\nUniNER \\cite{} splits extraction into per-type passes, gaining 3.3 F1 but sacrificing cross-type context.\nLLM-PEE \\cite{} uses type similarity as an implicit confusability proxy without empirical validation.\nProUIE \\cite{} and KGGen \\cite{} employ fixed task-level decomposition that ignores intra-layer schema structure.\nAll these approaches operate on unvalidated assumptions about \\emph{what} makes schemas complex for LLMs---specifically, the assumption that semantically similar types confuse the model and that separating them improves extraction.\n\nThis assumption has intuitive appeal but has never been empirically isolated from a confounding factor: type count.\nSchemas with many types tend to contain more semantically similar pairs, making it impossible to attribute degradation to confusability versus count without controlled analysis.\n\nWe conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE.\nOur study spans three tasks (NER, Event Detection, Relation Extraction), two models (Qwen3-32B, LLaMA-3.3-70B), and employs both batch-level and pairwise analysis methodologies.\nOur core finding is \\textbf{negative}: embedding-based confusability, once frequency is controlled, does not independently predict extraction degradation.\nThis negative result carries important methodological and practical implications:\n\n\\begin{enumerate}\n\\item We discover and quantify a \\textbf{frequency--confusability confound} that invalidates batch-level confusability analysis---high-frequency types tend to have both high confusability scores and high F1, producing spurious positive correlations.\n\\item We demonstrate that \\textbf{batch-level analysis is unreliable} and that pairwise type-pair analysis is necessary for valid confusability studies.\n\\item We provide clean evidence of \\textbf{count$\\to$recall monotonic degradation} as the primary mechanism of schema-induced quality loss.\n\\item We report a rigorous \\textbf{negative result on embedding SCS as a confusability proxy}: SCS achieves AUC=0.56 for predicting actual type confusion (near random), and confusability-aware decomposition provides no benefit over random batching.\n\\end{enumerate}\n\n\\section{Background and Related Work}\n\n\\paragraph{Training-free LLM IE.}\nThe paradigm of prompting LLMs with type definitions for zero-shot IE has been explored across NER \\cite{}, relation extraction \\cite{}, and event detection \\cite{}.\nPerformance degrades with schema complexity, but the degradation mechanisms have not been systematically studied.\n\n\\paragraph{Schema decomposition.}\nUniNER decomposes NER into per-type binary extraction passes.\nLLM-PEE partitions types by embedding similarity.\nThese approaches implicitly assume that type confusability drives degradation but provide no controlled evidence separating confusability effects from count effects.\n\n\\paragraph{Confusability in classification.}\nConfusion between semantically similar categories is well-documented in image classification \\cite{} and text classification \\cite{}.\nHowever, LLM IE differs fundamentally: the model receives explicit type definitions in the prompt, and confusion patterns may be driven by prompt formatting, type definition overlap, and training data biases rather than label-space geometry.\n\n\\section{Methodology}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Datasets.}\nWe use three datasets spanning distinct IE tasks:\n\\textbf{Few-NERD} (66 fine-grained entity types, flat schema),\n\\textbf{MAVEN} (168 event types, FrameNet hierarchy),\nand \\textbf{DocRED} (96 relation types, document-level).\nFew-NERD serves as the primary testbed; MAVEN and DocRED provide cross-task validation.\n\n\\paragraph{Models.}\nWe evaluate on Qwen3-32B (primary) and LLaMA-3.3-70B-Instruct (validation), representing different model families and scales.\n\n\\paragraph{Extraction protocol.}\nFor each dataset, we prompt the model with a type schema (subset or full) and a set of test instances, using text-match evaluation.\nWe systematically vary the number of types in the prompt (count variable) and the semantic similarity structure of the included types (confusability variable).\n\n\\subsection{Confusability Measurement}\n\n\\paragraph{Schema Confusability Score (SCS).}\nFor each pair of types $(t_i, t_j)$, we compute the cosine similarity of their label embeddings using all-MiniLM-L6-v2.\nThe Batch Confusability Score (BCS) of a type set $T$ is the mean pairwise SCS:\n\\begin{equation}\n\\text{BCS}(T) = \\frac{2}{|T|(|T|-1)} \\sum_{i<j} \\text{SCS}(t_i, t_j)\n\\end{equation}\n\n\\paragraph{Empirical confusion.}\nWe construct an empirical confusion matrix from model predictions, recording how often type $t_i$ is predicted when the gold label is $t_j$.\n\n\\subsection{Analysis Methodology}\n\nWe employ three complementary analysis strategies:\n\n\\textbf{Count curve analysis}: Vary type count while holding confusability constant (or averaging over it). Measures the count$\\to$performance channel.\n\n\\textbf{Factorial analysis}: 2$\\times$2 design crossing \\{low count, high count\\} $\\times$ \\{low BCS, high BCS\\} to test for main effects and interaction.\n\n\\textbf{Pairwise analysis}: Correlate pairwise SCS with pairwise empirical confusion counts. Immune to batch-level frequency confounds.\n\n\\section{Experiment 1: Count$\\to$Recall Degradation}\n\nWe first establish the count channel as the primary degradation mechanism.\n\n\\subsection{Few-NERD}\n\nTable~\\ref{tab:fewnerd_count} shows extraction performance as a function of type count.\nRecall declines monotonically from 0.60 (count=1) to 0.28 (count=64) on LLaMA-3.3-70B, confirming that adding types to the prompt systematically reduces the model's ability to identify entities.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{r|cc|cc|c}\n\\toprule\n& \\multicolumn{2}{c|}{Qwen3-32B} & \\multicolumn{2}{c|}{LLaMA-3.3-70B} & \\\\\nCount & F1 & R & F1 & R & $\\Delta$F1 \\\\\n\\midrule\n1  & 0.323 & --- & 0.290 & 0.600 & $-$0.033 \\\\\n6  & 0.306 & --- & 0.280 & --- & $-$0.026 \\\\\n12 & 0.347 & --- & 0.310 & --- & $-$0.037 \\\\\n44 & 0.445 & --- & 0.400 & --- & $-$0.045 \\\\\n64 & 0.414 & 0.304 & 0.370 & 0.280 & $-$0.044 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Count curve on Few-NERD. Both models exhibit consistent recall degradation as type count increases. $\\Delta$F1 = LLaMA $-$ Qwen3.}\n\\label{tab:fewnerd_count}\n\\end{table}\n\n\\subsection{MAVEN (168 Event Types)}\n\nTable~\\ref{tab:maven_count} shows the count curve on MAVEN, which exhibits more severe degradation due to the larger type space.\nRecall drops from 0.58 (count=1) to 0.10 (count=168), a 83\\% reduction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rcccc|c}\n\\toprule\nCount & P & R & F1 & pred/gold & WrongType \\\\\n\\midrule\n1   & 0.170 & 0.580 & 0.280 & 3.41 &    0 \\\\\n6   & 0.195 & 0.410 & 0.270 & 2.10 &  310 \\\\\n20  & 0.225 & 0.300 & 0.260 & 1.33 &  640 \\\\\n50  & 0.240 & 0.220 & 0.230 & 0.92 &  820 \\\\\n100 & 0.215 & 0.150 & 0.180 & 0.70 & 1950 \\\\\n168 & 0.185 & 0.100 & 0.130 & 0.54 & 3100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MAVEN count curve (Qwen3-32B). Recall declines monotonically from 0.58 to 0.10. WrongType errors increase from 0 to 3100 as more types compete for assignment.}\n\\label{tab:maven_count}\n\\end{table}\n\n\\subsection{DocRED (96 Relation Types)}\n\nDocRED exhibits an extreme floor effect (Table~\\ref{tab:docred_count}), with full-schema F1 at just 6\\%.\nTraining-free LLM RE on complex schemas is largely non-functional, limiting the statistical power of confusability analysis on this dataset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rccc}\n\\toprule\nCount & P & R & F1 \\\\\n\\midrule\n1  & 0.150 & 0.320 & 0.220 \\\\\n10 & 0.165 & 0.180 & 0.170 \\\\\n30 & 0.130 & 0.110 & 0.120 \\\\\n96 & 0.085 & 0.050 & 0.060 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{DocRED count curve (Qwen3-32B). Floor effect at full schema (F1=6\\%) limits confusability analysis.}\n\\label{tab:docred_count}\n\\end{table}\n\n\\paragraph{Summary.}\nCount$\\to$recall degradation is the single most robust finding across all three tasks and both models.\nRecall decline is monotonic, substantial, and consistent.\nThis establishes the baseline against which any confusability effect must be measured.\n\n\\section{Experiment 2: Testing Confusability Independence}\n\n\\subsection{Factorial Analysis on Few-NERD}\n\nWe conduct a 2$\\times$2 factorial experiment crossing type count (low/high) with BCS (low/high) on Few-NERD (Table~\\ref{tab:factorial}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc|c}\n\\toprule\n         & Low BCS & High BCS & $\\Delta$(BCS) \\\\\n\\midrule\nLow Count  & 0.340 & 0.330 & $-$0.010 \\\\\nHigh Count & 0.310 & 0.300 & $-$0.010 \\\\\n\\midrule\n$\\Delta$(Count) & $-$0.030 & $-$0.030 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{2$\\times$2 factorial F1 results on Few-NERD (Qwen3-32B). BCS has negligible effect ($\\Delta$=0.01) compared to count ($\\Delta$=0.03).}\n\\label{tab:factorial}\n\\end{table}\n\nTable~\\ref{tab:anova} shows the two-way ANOVA results.\nThe count main effect is marginally significant ($\\eta^2$=0.08, $p$=0.04), but the BCS main effect is not significant ($\\eta^2$=0.01, $p$=0.42).\nThe interaction term is negligible ($\\eta^2 \\approx$ 0, $p$=0.88).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lrrrrc}\n\\toprule\nSource & SS & df & $F$ & $p$ & $\\eta^2$ \\\\\n\\midrule\nCount     & 0.0180 & 1 & 4.25 & 0.040 & 0.080 \\\\\nBCS       & 0.0022 & 1 & 0.52 & 0.420 & 0.010 \\\\\nCount$\\times$BCS & 0.0002 & 1 & 0.05 & 0.880 & 0.001 \\\\\nResidual  & 0.2100 & 96 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Two-way ANOVA. BCS main effect is not significant after controlling for count. The interaction is zero, indicating confusability is not an independent factor.}\n\\label{tab:anova}\n\\end{table}\n\n\\subsection{Within-Count BCS Correlation on MAVEN}\n\nOn MAVEN, within-count BCS--F1 correlations are uniformly non-significant (Table~\\ref{tab:maven_bcs}).\nThe partial correlation controlling for count is $r$=0.05, $p$=0.38.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrrl}\n\\toprule\nCount & $r$(F1,BCS) & $p$ & $n$ & Verdict \\\\\n\\midrule\n6   & 0.04 & 0.420 & 25 & FAIL \\\\\n20  & 0.08 & 0.280 & 25 & FAIL \\\\\npartial & 0.05 & 0.380 & 50 & FAIL \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{MAVEN within-count BCS--F1 correlation. No evidence for confusability independence on event detection.}\n\\label{tab:maven_bcs}\n\\end{table}\n\n\\subsection{Pairwise BCS--Confusion Analysis}\n\nPairwise analysis on Few-NERD with Qwen3-32B yields a statistically significant but small correlation ($r$=0.156, $p$=4.6e-12), which is the strongest evidence for a confusability signal in our study.\nHowever, this result fails to replicate on LLaMA-3.3-70B ($r$=0.05, $p$=0.08) and on MAVEN ($r$=0.04, $p$=0.12), as shown in Table~\\ref{tab:pairwise}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llrrrr}\n\\toprule\nDataset & Model & $n$ & $r$ & $p$ & $\\rho_{\\text{nz}}$ \\\\\n\\midrule\nFew-NERD & Qwen3-32B     & 1953  & 0.156 & 4.6e-12 & 0.254 \\\\\nFew-NERD & LLaMA-3.3-70B & 1953  & 0.050 & 0.080   & 0.070 \\\\\nMAVEN    & Qwen3-32B     & 14028 & 0.040 & 0.120   & 0.060 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise BCS--confusion correlations. The Few-NERD/Qwen3 result ($r$=0.156) does not replicate across models or tasks. $\\rho_{\\text{nz}}$: Spearman $\\rho$ on nonzero confusion pairs.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe Few-NERD/Qwen3-32B pairwise signal, while statistically significant, appears model-specific.\nThe failure to replicate on a second model from a different family (LLaMA-3.3) and on a second task (MAVEN) prevents us from claiming confusability independence as a general phenomenon.\n\n\\section{Experiment 3: Error Taxonomy}\n\nIf confusability drives a distinct error channel (type substitution), we should observe more type substitution errors in high-BCS conditions after controlling for frequency.\nTable~\\ref{tab:errors} shows the error taxonomy across BCS bins with frequency controlled.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcc|cc}\n\\toprule\nError Type & High BCS & Low BCS & Ratio & $\\chi^2$ $p$ \\\\\n\\midrule\nType Substitution & 18.0\\% & 15.0\\% & 1.20 & 0.180 \\\\\nBoundary Error    & 22.0\\% & 20.0\\% & 1.10 & 0.350 \\\\\nFalse Negative    & 45.0\\% & 48.0\\% & 0.94 & 0.410 \\\\\nHallucination     & 15.0\\% & 17.0\\% & 0.88 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Error taxonomy by BCS bin (Few-NERD, frequency-controlled). No significant difference in type substitution between high- and low-BCS conditions.}\n\\label{tab:errors}\n\\end{table}\n\nNone of the error type proportions differ significantly between BCS bins.\nFalse negatives dominate uniformly (45--48\\%), consistent with count-driven recall decline as the primary degradation mechanism.\nType substitution shows only a non-significant 1.2$\\times$ ratio ($p$=0.18), insufficient to support a distinct confusability$\\to$type confusion channel.\n\n\\section{Experiment 4: Validating the Confusability Proxy}\n\nWe directly evaluate embedding SCS as a proxy for empirical LLM confusion (Table~\\ref{tab:scs_validation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lr}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSpearman $\\rho$ (SCS vs.\\ empirical confusion) & 0.12 ($p$=0.03) \\\\\nKendall $\\tau$ & 0.09 ($p$=0.04) \\\\\nTop-10 pair overlap & 2/10 (20\\%) \\\\\nAUC (binary confusion prediction) & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SCS vs.\\ empirical confusion. Despite weak statistical significance ($p$<0.05 due to large $n$), practical predictive value is near-random (AUC=0.56).}\n\\label{tab:scs_validation}\n\\end{table}\n\nThe rank correlation is weak ($\\rho$=0.12) and barely exceeds chance for binary prediction (AUC=0.56).\nTable~\\ref{tab:mismatch} reveals the source of the mismatch: the most confused type pairs predominantly involve ``-other'' label ambiguity (e.g., \\texttt{person-other} $\\leftrightarrow$ \\texttt{organization-other}), a schema design phenomenon that embedding similarity cannot capture.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rlc}\n\\toprule\nRank & Top Empirical Confusion Pair & In Top-10 SCS? \\\\\n\\midrule\n1 & person-other $\\leftrightarrow$ person-politician & Yes \\\\\n2 & person-other $\\leftrightarrow$ organization-other & No \\\\\n3 & location-GPE $\\leftrightarrow$ location-bodiesofwater & No \\\\\n4 & person-scholar $\\leftrightarrow$ person-artist & Yes \\\\\n5 & building-library $\\leftrightarrow$ building-other & No \\\\\n6 & event-sportsevent $\\leftrightarrow$ event-other & No \\\\\n7 & organization-company $\\leftrightarrow$ organization-other & No \\\\\n8 & person-athlete $\\leftrightarrow$ person-other & No \\\\\n9 & location-GPE $\\leftrightarrow$ location-other & No \\\\\n10 & product-car $\\leftrightarrow$ product-other & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Top-10 empirically confused type pairs. Only 2/10 overlap with top-10 SCS pairs. Confusion is driven by ``-other'' label ambiguity, not embedding similarity.}\n\\label{tab:mismatch}\n\\end{table}\n\n\\section{Experiment 5: Schema Decomposition}\n\nDespite the negative confusability results, schema decomposition itself (reducing the number of types per prompt) does improve performance, as shown by the count curves.\nWe evaluate whether confusability-\\emph{aware} decomposition (SDGD) provides benefit beyond simple batch size reduction.\n\n\\subsection{Few-NERD}\n\nTable~\\ref{tab:decomp_fewnerd} compares all decomposition strategies on Few-NERD.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & P & R & F1 & Calls & Lat.(s) \\\\\n\\midrule\nSingle-Pass      & 0.648 & 0.304 & 0.414 &  1 &   7 \\\\\nRandom-$k$8 (avg)& 0.486 & 0.396 & 0.436 &  8 &  48 \\\\\nSDGD-zero-$k$8   & 0.480 & 0.390 & 0.430 &  8 &  48 \\\\\nSDGD-cal-$k$8    & 0.480 & 0.390 & 0.440 & 74 & 420 \\\\\nPer-Type ($k$64) & 0.420 & 0.620 & 0.500 & 64 & 385 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition strategies on Few-NERD. SDGD-zero does not outperform random batching at the same $k$.}\n\\label{tab:decomp_fewnerd}\n\\end{table}\n\nSDGD-zero (F1=0.430) performs \\emph{below} random batching (F1=0.436, averaged over 5 seeds), with $\\Delta$F1=$-$0.5 ($p$=0.72).\nSDGD-cal adds 66 calibration API calls for a further non-significant +1.0 F1 gain ($p$=0.28) at 8.8$\\times$ the latency.\nPer-type splitting remains the quality upper bound (F1=0.500).\n\nTable~\\ref{tab:random_seeds} shows that SDGD-zero falls within the variance of random batching.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & F1 std & $\\Delta$ vs SDGD & $p$ \\\\\n\\midrule\nSDGD-zero  & 0.430 & --- & --- & --- \\\\\nRandom (s1) & 0.420 & & $-$1.0 & \\\\\nRandom (s2) & 0.445 & & +1.5 & \\\\\nRandom (s3) & 0.430 & & 0.0 & \\\\\nRandom (s4) & 0.450 & & +2.0 & \\\\\nRandom (s5) & 0.435 & & +0.5 & \\\\\n\\midrule\nRandom (avg) & 0.436 & 0.011 & +0.6 & 0.72 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SDGD-zero vs.\\ 5 random batching seeds ($k$=8, Few-NERD). SDGD falls within the random variance.}\n\\label{tab:random_seeds}\n\\end{table}\n\n\\subsection{MAVEN}\n\nTable~\\ref{tab:decomp_maven} extends the comparison to MAVEN's 168 event types.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & F1 & Calls & Lat.(s) & $\\Delta$F1 vs single \\\\\n\\midrule\nSingle-Pass     & 0.130 &   1 &   10 & --- \\\\\nRandom-$k$12    & 0.155 &  12 &   80 & +2.5 \\\\\nSDGD-zero-$k$12 & 0.150 &  12 &   85 & +2.0 \\\\\nSDGD-cal-$k$12  & 0.160 & 180 & 1250 & +3.0 \\\\\nPer-Type ($k$168)& 0.180 & 168 & 1680 & +5.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Decomposition strategies on MAVEN. SDGD-zero underperforms random batching ($-$0.5 F1) while SDGD-cal's marginal gain costs 15$\\times$ more API calls.}\n\\label{tab:decomp_maven}\n\\end{table}\n\nSDGD-zero is 0.5 F1 points \\emph{below} random batching on MAVEN.\nThe confusability-aware grouping may actually hurt by forcing semantically diverse types into the same batch, disrupting the model's extraction consistency.\n\n\\section{Discussion}\n\n\\paragraph{The frequency--confusability confound.}\nOur most important methodological finding is that type frequency confounds batch-level confusability analysis.\nHigh-frequency types in Few-NERD tend to be fine-grained subtypes within the same coarse category (e.g., multiple \\texttt{person-*} types), which naturally have high pairwise SCS.\nThese same types also have higher per-type F1 due to frequency effects.\nThe result is a spurious positive correlation between BCS and batch F1---the opposite of the confusability hypothesis prediction.\nThis confound is invisible in batch-level analysis and requires per-type or pairwise analysis to detect.\n\n\\paragraph{Why embedding SCS fails as a confusability proxy.}\nSCS captures semantic proximity in label embedding space, but LLM type confusion is driven by different mechanisms:\n(1) ``-other'' label ambiguity, a schema design artifact where underspecified catch-all categories absorb mentions from multiple specific types;\n(2) trigger/mention polysemy, where the same surface form maps to different types depending on context;\n(3) training data biases in type co-occurrence that shape the model's prior over type assignments.\nNone of these mechanisms are captured by static embedding similarity, explaining the near-random AUC of 0.56.\n\n\\paragraph{When does the pairwise signal exist?}\nThe Few-NERD/Qwen3-32B pairwise result ($r$=0.156) is real but model-specific.\nWe hypothesize this reflects an alignment between Qwen3's internal type representations and the all-MiniLM-L6-v2 embedding space---an accident of training data overlap rather than a general property of LLMs.\nLLaMA-3.3-70B, trained on different data with a different architecture, shows no such alignment.\n\n\\paragraph{Practical implications for schema decomposition.}\nOur results suggest a simple prescription: when decomposing complex schemas, batch size reduction is all that matters.\nRandom partitioning into $k$ batches of roughly equal size is sufficient; confusability-aware grouping adds cost without benefit.\nPer-type splitting remains the quality upper bound but at proportionally higher latency.\nThe optimal $k$ is a cost--quality tradeoff that depends on the deployment scenario.\n\n\\paragraph{Limitations and future directions.}\nSeveral limitations constrain our conclusions.\nFirst, our SCS measure uses a single sentence embedding model (all-MiniLM-L6-v2); alternative embeddings (e.g., from the target LLM itself) might yield better confusability proxies.\nSecond, our calibration approach uses only 5--10 examples per type; larger calibration sets could overcome the sparsity problem.\nThird, we evaluate only two LLMs; broader model coverage may reveal architectures where embedding confusability is more predictive.\nSDGD could potentially be revived with better confusability proxies---e.g., using the LLM's own logit-based confusion signals or leveraging schema metadata (hierarchical structure, definition overlap).\n\n\\section{Conclusion}\n\nWe present a controlled empirical study of schema complexity in training-free LLM information extraction.\nOur findings challenge the widely held assumption that type confusability independently drives extraction degradation: once type frequency is controlled, embedding-based confusability scores do not predict performance, confusability-aware decomposition does not outperform random batching, and the error distribution does not differ between high- and low-confusability conditions.\n\nThe primary degradation mechanism is type count: more types in the prompt cause monotonic recall decline, robustly replicated across three tasks and two models.\nThis count channel accounts for the vast majority of schema-induced quality loss, with confusability at best a minor, model-specific, and task-specific secondary factor.\n\nOur methodological contribution---exposing the frequency--confusability confound and demonstrating the unreliability of batch-level analysis---has implications beyond this study, as any future work on type confusability in IE must control for this confound.\nWe release our experimental framework and data to support such future work.\n\n\\bibliography{references}\n\\bibliographystyle{acl_natbib}\n\n\\appendix\n\\section{DocRED Supplementary Results}\n\\label{app:docred}\n\nDocRED exhibits an extreme floor effect, with full-schema F1 at 6\\%.\nPairwise BCS--confusion correlation is not significant ($r$=0.02, $p$=0.35).\nThe partial correlation controlling for frequency is $r$=$-$0.03, $p$=0.62.\nThe confusion ratio between extreme BCS batches is 1.1$\\times$, indicating no confusability effect.\nThese results are consistent with the main findings but lack statistical power due to the low baseline performance.\n\n\\section{SDGD-cal Detailed Results}\n\nOn Few-NERD, SDGD-cal uses 66 calibration API calls (one per type with 5 examples) to construct an empirical confusion matrix.\nDespite the added cost, SDGD-cal improves over SDGD-zero by only 1.0 F1 point ($p$=0.28).\nWith 5 examples per type, the empirical confusion matrix is extremely sparse---most of the 66$\\times$65 = 4290 type pairs have zero observed confusion---limiting the information gain over the embedding proxy.\n\nOn MAVEN, calibration requires 168 additional API calls.\nSDGD-cal achieves F1=0.16, only 0.5 points above random batching and 2.0 points below per-type splitting.\nThe calibration cost (1250s total latency) approaches per-type splitting (1680s) without matching its quality, yielding a poor cost--benefit ratio.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a00b5408-a59d-41de-a7b6-364c4604bcd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "62de3520-b70d-485d-846d-7531b65df92c",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Tool call

_source line 22 · 2026-05-15T06:10:31.057Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ELQNJgAF6MFLzPX4A58uod`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62de3520-b70d-485d-846d-7531b65df92c",
  "isSidechain": false,
  "requestId": "req_011Cb3rhCDWQ6vP2FtgZAfxG",
  "type": "assistant",
  "uuid": "05c87284-70ec-45ad-b8ce-748d5e675714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZQF5rHn9wKUN11RkSQS2Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8870,
      "cache_read_input_tokens": 39115,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 39115,
          "cache_creation_input_tokens": 8870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8870
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

_source line 23 · 2026-05-15T06:10:31.197Z_

<details><summary>↩ Tool result · reported error · `toolu_01ELQNJgAF6MFLzPX4A58uod`</summary>

```text
Exit code 1
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
  "parentUuid": "05c87284-70ec-45ad-b8ce-748d5e675714",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "fb08dbdb-e09f-4984-ba94-d1a6d9b1e2fd",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "05c87284-70ec-45ad-b8ce-748d5e675714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-15T06:10:33.865Z_

<details><summary>Logged reasoning block</summary>

```text
The ACL style file is not available. Let me switch to a simpler document class or find if there's an ACL style file available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb08dbdb-e09f-4984-ba94-d1a6d9b1e2fd",
  "isSidechain": false,
  "requestId": "req_011Cb3rhcWkFpgn1vg9xHQbU",
  "type": "assistant",
  "uuid": "a68812e0-877c-4938-9566-cdde5092d1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCEzVw9z5f57MYn6Q1R5N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 47985,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 47985,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 25 · 2026-05-15T06:10:34.374Z_

ACL style not available. Let me switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a68812e0-877c-4938-9566-cdde5092d1fc",
  "isSidechain": false,
  "requestId": "req_011Cb3rhcWkFpgn1vg9xHQbU",
  "type": "assistant",
  "uuid": "65a7fab5-1141-46c9-951c-1b958d62a103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCEzVw9z5f57MYn6Q1R5N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 47985,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 47985,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 26 · 2026-05-15T06:10:37.975Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NK7brKBQabxcoZVUVi6aNL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{hyperref}\n\\usepackage{natbib}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65a7fab5-1141-46c9-951c-1b958d62a103",
  "isSidechain": false,
  "requestId": "req_011Cb3rhcWkFpgn1vg9xHQbU",
  "type": "assistant",
  "uuid": "4b97c4b8-4e5e-45a2-8f64-39689c9f84d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCEzVw9z5f57MYn6Q1R5N4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 47985,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 47985,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 27 · 2026-05-15T06:10:37.996Z_

<details><summary>↩ Tool result · `toolu_01NK7brKBQabxcoZVUVi6aNL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b97c4b8-4e5e-45a2-8f64-39689c9f84d0",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "0c8a939b-4896-41e2-87f8-c513bd407dbb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{tabularx}\n\\usepackage{hyperref}\n\\usepackage{natbib}",
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
          " \\usepackage{tabularx}",
          "+\\usepackage{hyperref}",
          "+\\usepackage{natbib}",
          " ",
          " \\title{Anatomy of Schema Complexity in Training-Free LLM Information Extraction:\\\\A Controlled Study of Type Count, Confusability, and Their Entanglement}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "4b97c4b8-4e5e-45a2-8f64-39689c9f84d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T06:10:42.215Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0144uFW6Y54JSjgMoxcxeWG4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
  "old_string": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
  "new_string": "\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c8a939b-4896-41e2-87f8-c513bd407dbb",
  "isSidechain": false,
  "requestId": "req_011Cb3ri7u5MCXSkNFZAydqT",
  "type": "assistant",
  "uuid": "634e7c29-b80a-4a3e-970d-aeffe2afbd09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdzxLzCUuxKTWWc8brS6Ui",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 48449,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 48449,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 522
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

_source line 29 · 2026-05-15T06:10:42.228Z_

<details><summary>↩ Tool result · `toolu_0144uFW6Y54JSjgMoxcxeWG4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "634e7c29-b80a-4a3e-970d-aeffe2afbd09",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "43466695-a2e9-471b-a2c2-35f0c867f22f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
    "oldString": "\\bibliography{references}\n\\bibliographystyle{acl_natbib}",
    "newString": "\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 477,
        "oldLines": 8,
        "newStart": 477,
        "newLines": 7,
        "lines": [
          " Our methodological contribution---exposing the frequency--confusability confound and demonstrating the unreliability of batch-level analysis---has implications beyond this study, as any future work on type confusability in IE must control for this confound.",
          " We release our experimental framework and data to support such future work.",
          " ",
          "-\\bibliography{references}",
          "-\\bibliographystyle{acl_natbib}",
          "+\\bibliographystyle{plainnat}",
          " ",
          " \\appendix",
          " \\section{DocRED Supplementary Results}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "634e7c29-b80a-4a3e-970d-aeffe2afbd09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T06:10:42.275Z_

```json
{
  "parentUuid": "43466695-a2e9-471b-a2c2-35f0c867f22f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9dd7f6e3-ce0f-468b-829a-6137b03180a2",
  "timestamp": "2026-05-15T06:10:42.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-15T06:10:45.353Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HYE6Cw4JE62afYL1zNRwb8`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dd7f6e3-ce0f-468b-829a-6137b03180a2",
  "isSidechain": false,
  "requestId": "req_011Cb3riRp6eF9jLMx6KHckq",
  "type": "assistant",
  "uuid": "20c6be2f-c096-46cb-977b-2a91605fb65a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhiEYNqhBj7xSnsBwZ8taH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 48971,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 351,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 48971,
          "cache_creation_input_tokens": 351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 351
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

_source line 32 · 2026-05-15T06:10:46.296Z_

<details><summary>↩ Tool result · `toolu_01HYE6Cw4JE62afYL1zNRwb8`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (4.83446pt too wide) in paragraph at lines 72--74
 []\OT1/ptm/b/n/10.95 Confusability in clas-si-fi-ca-tion.[] \OT1/ptm/m/n/10.95
 Con-fu-sion be-tween se-man-ti-cally sim-i-lar cat-e-gories is well-documented


Overfull \hbox (6.15985pt too wide) in paragraph at lines 80--85
\OT1/ptm/m/n/10.95 flat schema), \OT1/ptm/b/n/10.95 MAVEN \OT1/ptm/m/n/10.95 (1
68 event types, FrameNet hi-er-ar-chy), and \OT1/ptm/b/n/10.95 Do-cRED \OT1/ptm
/m/n/10.95 (96 re-la-tion types, document-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


LaTeX Warning: Reference `tab:fewnerd_count' on page 3 undefined on input line 
121.


LaTeX Warning: Reference `tab:maven_count' on page 3 undefined on input line 14
5.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:docred_count' on page 3 undefined on input line 1
69.

[3]

LaTeX Warning: Reference `tab:factorial' on page 4 undefined on input line 198.



LaTeX Warning: Reference `tab:anova' on page 4 undefined on input line 217.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:maven_bcs' on page 4 undefined on input line 240.


[4]

LaTeX Warning: Reference `tab:pairwise' on page 5 undefined on input line 262.


LaTeX Warning: Reference `tab:errors' on page 5 undefined on input line 286.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:scs_validation' on page 5 undefined on input line
 311.

[5]

LaTeX Warning: Reference `tab:mismatch' on page 6 undefined on input line 331.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)
Overfull \hbox (4.56255pt too wide) in paragraph at lines 358--360
\OT1/ptm/m/n/10.95 per prompt) does im-prove per-for-mance, as shown by the cou
nt curves. We eval-u-ate whether confusability-

LaTeX Warning: Reference `tab:decomp_fewnerd' on page 6 undefined on input line
 363.


LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: Reference `tab:random_seeds' on page 7 undefined on input line 3
87.


LaTeX Warning: Reference `tab:decomp_maven' on page 7 undefined on input line 4
12.

[7] [8] [9] (./paper.aux)

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
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 140809 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (4.83446pt too wide) in paragraph at lines 72--74
 []\OT1/ptm/b/n/10.95 Confusability in clas-si-fi-ca-tion.[] \OT1/ptm/m/n/10.95
 Con-fu-sion be-tween se-man-ti-cally sim-i-lar cat-e-gories is well-documented


Overfull \hbox (6.15985pt too wide) in paragraph at lines 80--85
\OT1/ptm/m/n/10.95 flat schema), \OT1/ptm/b/n/10.95 MAVEN \OT1/ptm/m/n/10.95 (1
68 event types, FrameNet hi-er-ar-chy), and \OT1/ptm/b/n/10.95 Do-cRED \OT1/ptm
/m/n/10.95 (96 re-la-tion types, document-
[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `\to' on input line 115.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 115.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]
Overfull \hbox (1.58006pt too wide) in paragraph at lines 217--220
[]\OT1/ptm/m/n/10.95 Table []5[] shows the two-way ANOVA re-sults. The count ma
in ef-fect is marginally sig-nif-i-cant ($\OML/cmm/m/it/10.95 ^^Q[]$\OT1/ptm/m/
n/10.95 =0.08,

LaTeX Warning: `h' float specifier changed to `ht'.

[4]

LaTeX Warning: `h' float specifier changed to `ht'.

[5] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)
Overfull \hbox (4.56255pt too wide) in paragraph at lines 358--360
\OT1/ptm/m/n/10.95 per prompt) does im-prove per-for-mance, as shown by the cou
nt curves. We eval-u-ate whether confusability-

LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7] [8] [9] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 142926 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20c6be2f-c096-46cb-977b-2a91605fb65a",
  "isSidechain": false,
  "promptId": "f7b5fbbb-62d1-4159-b027-775886e6cd1a",
  "type": "user",
  "uuid": "d676d5b1-ac08-4eb1-9ec8-0bb48fe2ee81",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (4.83446pt too wide) in paragraph at lines 72--74\n []\\OT1/ptm/b/n/10.95 Confusability in clas-si-fi-ca-tion.[] \\OT1/ptm/m/n/10.95\n Con-fu-sion be-tween se-man-ti-cally sim-i-lar cat-e-gories is well-documented\n\n\nOverfull \\hbox (6.15985pt too wide) in paragraph at lines 80--85\n\\OT1/ptm/m/n/10.95 flat schema), \\OT1/ptm/b/n/10.95 MAVEN \\OT1/ptm/m/n/10.95 (1\n68 event types, FrameNet hi-er-ar-chy), and \\OT1/ptm/b/n/10.95 Do-cRED \\OT1/ptm\n/m/n/10.95 (96 re-la-tion types, document-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nLaTeX Warning: Reference `tab:fewnerd_count' on page 3 undefined on input line \n121.\n\n\nLaTeX Warning: Reference `tab:maven_count' on page 3 undefined on input line 14\n5.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:docred_count' on page 3 undefined on input line 1\n69.\n\n[3]\n\nLaTeX Warning: Reference `tab:factorial' on page 4 undefined on input line 198.\n\n\n\nLaTeX Warning: Reference `tab:anova' on page 4 undefined on input line 217.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:maven_bcs' on page 4 undefined on input line 240.\n\n\n[4]\n\nLaTeX Warning: Reference `tab:pairwise' on page 5 undefined on input line 262.\n\n\nLaTeX Warning: Reference `tab:errors' on page 5 undefined on input line 286.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:scs_validation' on page 5 undefined on input line\n 311.\n\n[5]\n\nLaTeX Warning: Reference `tab:mismatch' on page 6 undefined on input line 331.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)\nOverfull \\hbox (4.56255pt too wide) in paragraph at lines 358--360\n\\OT1/ptm/m/n/10.95 per prompt) does im-prove per-for-mance, as shown by the cou\nnt curves. We eval-u-ate whether confusability-\n\nLaTeX Warning: Reference `tab:decomp_fewnerd' on page 6 undefined on input line\n 363.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: Reference `tab:random_seeds' on page 7 undefined on input line 3\n87.\n\n\nLaTeX Warning: Reference `tab:decomp_maven' on page 7 undefined on input line 4\n12.\n\n[7] [8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 140809 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (4.83446pt too wide) in paragraph at lines 72--74\n []\\OT1/ptm/b/n/10.95 Confusability in clas-si-fi-ca-tion.[] \\OT1/ptm/m/n/10.95\n Con-fu-sion be-tween se-man-ti-cally sim-i-lar cat-e-gories is well-documented\n\n\nOverfull \\hbox (6.15985pt too wide) in paragraph at lines 80--85\n\\OT1/ptm/m/n/10.95 flat schema), \\OT1/ptm/b/n/10.95 MAVEN \\OT1/ptm/m/n/10.95 (1\n68 event types, FrameNet hi-er-ar-chy), and \\OT1/ptm/b/n/10.95 Do-cRED \\OT1/ptm\n/m/n/10.95 (96 re-la-tion types, document-\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/omsptm.fd)\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\to' on input line 115.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 115.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\nOverfull \\hbox (1.58006pt too wide) in paragraph at lines 217--220\n[]\\OT1/ptm/m/n/10.95 Table []5[] shows the two-way ANOVA re-sults. The count ma\nin ef-fect is marginally sig-nif-i-cant ($\\OML/cmm/m/it/10.95 ^^Q[]$\\OT1/ptm/m/\nn/10.95 =0.08,\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[5] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1pcr.fd)\nOverfull \\hbox (4.56255pt too wide) in paragraph at lines 358--360\n\\OT1/ptm/m/n/10.95 per prompt) does im-prove per-for-mance, as shown by the cou\nnt curves. We eval-u-ate whether confusability-\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7] [8] [9] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 142926 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "20c6be2f-c096-46cb-977b-2a91605fb65a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "d676d5b1-ac08-4eb1-9ec8-0bb48fe2ee81",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Assistant

_source line 35 · 2026-05-15T06:10:53.370Z_

编译成功，生成 9 页 PDF。

`paper.pdf` 已写入 `worst/` 目录。论文以 negative result 为核心，覆盖了全部 11 个实验的数据：count curve（3 个数据集）、factorial 2×2、pairwise BCS-confusion（跨模型）、error taxonomy、SCS validation、SDGD-zero/cal（Few-NERD + MAVEN）、random batching ablation、per-type splitting。所有定量 claim 均来自 `experiment_data.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d676d5b1-ac08-4eb1-9ec8-0bb48fe2ee81",
  "isSidechain": false,
  "requestId": "req_011Cb3rij1wvvfta4rSAmiUu",
  "type": "assistant",
  "uuid": "a512f977-2738-4690-9514-855d61f9cdd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/dream_reports/dream_20260515T053106/worst",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhFhYTuM9QjNFrpCKktGxC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6861,
      "cache_read_input_tokens": 49322,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 49322,
          "cache_creation_input_tokens": 6861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6861
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T053106 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extra…",
  "leafUuid": "a512f977-2738-4690-9514-855d61f9cdd8",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream research",
  "sessionId": "09c25452-0401-4009-b9de-190aa2a341c2"
}
```

---
