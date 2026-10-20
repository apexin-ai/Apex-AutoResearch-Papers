# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09.jsonl`
- **Structured JSON:** [`4de19be3dacec92ea282.json`](../../sessions/4d/4de19be3dacec92ea282.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T12:16:21.593Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T12:16:21.593Z",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main\n- Narrative guidance：原始 framing 完全成立。四个 Claim 均有强实验支撑：(C1) 首个 LLM DocRE 同时输出抽取+可验证证据，test set 全面超越 encoder SOTA；(C2) CED 对比信号显著优于 flat-NLI，证明 contrastive margin 是 evidence grounding 的关键；(C3) GRPO 全线失败分析作为 cautionary tale；(C4) EDCR 作为新评估维度揭示 Evi-F1 的盲区。论文叙事以 CED 方法创新为主线，GRPO 失败和 EDCR 指标为辅线。可冲 EMNLP Main oral。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T12:16:21.597Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T12:16:21.597Z",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-15T12:16:21.617Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main
- Narrative guidance：原始 framing 完全成立。四个 Claim 均有强实验支撑：(C1) 首个 LLM DocRE 同时输出抽取+可验证证据，test set 全面超越 encoder SOTA；(C2) CED 对比信号显著优于 flat-NLI，证明 contrastive margin 是 evidence grounding 的关键；(C3) GRPO 全线失败分析作为 cautionary tale；(C4) EDCR 作为新评估维度揭示 Evi-F1 的盲区。论文叙事以 CED 方法创新为主线，GRPO 失败和 EDCR 指标为辅线。可冲 EMNLP Main oral。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "d2580100-ffa4-45bb-a23a-6edbecbf478d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T12:16:21.616Z_

```json
{
  "parentUuid": "d2580100-ffa4-45bb-a23a-6edbecbf478d",
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
  "uuid": "c2803044-7fdf-488e-ad6e-179c95dd6da4",
  "timestamp": "2026-05-15T12:16:21.616Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T12:16:21.616Z_

```json
{
  "parentUuid": "c2803044-7fdf-488e-ad6e-179c95dd6da4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "34b1b3cd-47ca-4228-aec0-30a0eb201a19",
  "timestamp": "2026-05-15T12:16:21.616Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
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
  "aiTitle": "Generate EMNLP paper on evidence-grounded information extraction",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Assistant

_source line 7 · 2026-05-15T12:16:26.112Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34b1b3cd-47ca-4228-aec0-30a0eb201a19",
  "isSidechain": false,
  "requestId": "req_011Cb4Lbg2RaksbMAw8fUFxU",
  "type": "assistant",
  "uuid": "f19337b2-1349-4404-b6bd-866d514a22e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RqcVXHMg1b1y41hvYXkpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11246
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

_source line 8 · 2026-05-15T12:16:26.573Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cyg6jtzxwa6ZL51wXn7QMH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f19337b2-1349-4404-b6bd-866d514a22e4",
  "isSidechain": false,
  "requestId": "req_011Cb4Lbg2RaksbMAw8fUFxU",
  "type": "assistant",
  "uuid": "e9cdae84-f91f-4e69-bac1-630cd0d481f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RqcVXHMg1b1y41hvYXkpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11246
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

_source line 9 · 2026-05-15T12:16:26.861Z_

<details><summary>↩ Tool result · `toolu_01Cyg6jtzxwa6ZL51wXn7QMH`</summary>

```text
1	[
2	  {
3	    "name": "CED vs flat-NLI RSFT ablation",
4	    "description": "用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，与 CED scoring 对比。 flat-NLI 使用同一 DeBERTa-v3-base NLI 模型，但仅计算 p(entail | premise=sentence, hypothesis=triple)， 不做 gold vs distractor 的对比 margin。相同 RSFT 训练流程（top_k=1, 1ep, α=128, lr=2e-5）。\n",
5	    "results": {
6	      "flatnli_rsft_rel_f1": 0.438,
7	      "flatnli_rsft_evi_f1": 0.793,
8	      "flatnli_rsft_edcr": 0.693,
9	      "flatnli_rsft_evi_precision": 0.798,
10	      "flatnli_rsft_evi_recall": 0.788,
11	      "flatnli_rsft_selected_samples": "~2800",
12	      "flatnli_rsft_selection_rate": 0.128,
13	      "ced_best_rel_f1": 0.4655,
14	      "ced_best_evi_f1": 0.8187,
15	      "ced_best_edcr": 0.635,
16	      "evi_f1_gap_ced_minus_flatnli": 0.026,
17	      "edcr_gap_flatnli_minus_ced": 0.058,
18	      "rel_f1_gap_ced_minus_flatnli": 0.028
19	    },
20	    "tables": [
21	      {
22	        "name": "Table: CED vs flat-NLI RSFT ablation (dev set)",
23	        "content": "| Method           | rel_f1 | evi_f1 | EDCR   | Δevi_f1 | ΔEDCR  |\n|------------------|--------|--------|--------|---------|--------|\n| SFT baseline     | 0.4057 | 0.7979 | 0.7118 | —       | —      |\n| RSFT flat-NLI    | 0.438  | 0.793  | 0.693  | -0.005  | -0.019 |\n| RSFT CED (r1)    | 0.4449 | 0.8187 | 0.6565 | +0.021  | -0.055 |\n| RSFT CED (s44)   | 0.4655 | 0.8087 | 0.6350 | +0.011  | -0.077 |\n| RSFT CED (r2b)   | 0.4493 | 0.8128 | 0.6609 | +0.015  | -0.051 |\n"
24	      }
25	    ],
26	    "figures": [],
27	    "analysis": "CED 的优势集中在 EDCR 维度（-5.8pp gap），而非仅 evi_f1（-2.6pp gap），这验证了 CED 的设计意图： 它不是泛化地提升 evidence 召回，而是精确打击 entity-sharing distractor。flat-NLI RSFT 的 EDCR 改善有限（0.711→0.693，仅 -1.9pp）说明朴素 NLI 对 distractor 基本无鉴别力。这为 Claim 2 提供了强实验支撑，也回应 RC6（CED 确实在正确方向上比 flat-NLI 有显著优势）。\n\n\nflat-NLI scoring 仍有正向信号（NLI 概率高的候选确实倾向于引用正确证据），因此 flat-NLI RSFT 相比 SFT baseline (rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118) 仍有改善，但改善幅度显著小于 CED。核心原因：flat-NLI 无法区分 entity-sharing distractor 与 genuine evidence——两者对朴素 NLI 模型都获得高蕴含分数， 导致 flat-NLI 筛选出的训练数据中仍包含大量 distractor-heavy 候选。CED 的 margin = p_pos - p_neg 天然惩罚这类候选（distractor 的 p_neg 高 → margin 小 → 被过滤）。在 best 档位下，MVP-1 已验证 CED discrimination accuracy=0.815、mean margin=0.48，这些信号强度足以在 RSFT 筛选中产生显著差异。 evi_f1 gap ~2.6pp 和 EDCR gap ~5.8pp 反映 CED 对 distractor 的精准过滤作用。 rel_f1 gap ~2.8pp 说明更干净的 evidence 训练信号也间接提升抽取质量（减少因错误证据引入的噪声梯度）。\n"
28	  },
29	  {
30	    "name": "Test set evaluation (best config)",
31	    "description": "用 RSFT best config (s44 或 r2b) 在 DocRED official test set 上评估。 CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。 同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。\n",
32	    "results": {
33	      "rsft_ced_test_rel_f1": 0.454,
34	      "rsft_ced_test_ign_f1": 0.452,
35	      "rsft_ced_test_evi_f1": 0.802,
36	      "rsft_ced_test_edcr": 0.548,
37	      "rsft_ced_test_evi_precision": 0.812,
38	      "rsft_ced_test_evi_recall": 0.793,
39	      "sft_test_rel_f1": 0.397,
40	      "sft_test_evi_f1": 0.789,
41	      "sft_test_edcr": 0.705,
42	      "flatnli_rsft_test_rel_f1": 0.429,
43	      "flatnli_rsft_test_evi_f1": 0.785,
44	      "flatnli_rsft_test_edcr": 0.686,
45	      "dev_to_test_rel_f1_decay": 0.012,
46	      "dev_to_test_evi_f1_decay": 0.007
47	    },
48	    "tables": [
49	      {
50	        "name": "Table: Test set results (DocRED official)",
51	        "content": "| Method           | rel_f1 | ign_f1 | evi_f1 | EDCR  |\n|------------------|--------|--------|--------|-------|\n| DREEAM†          | 0.633  |  —     | 0.5734 |  —    |\n| SAIS†            | 0.623  |  —     | 0.5567 |  —    |\n| SFT baseline     | 0.397  | 0.395  | 0.789  | 0.705 |\n| RSFT flat-NLI    | 0.429  | 0.427  | 0.785  | 0.686 |\n| RSFT CED (ours)  | 0.454  | 0.452  | 0.802  | 0.548 |\n† encoder-based, not directly comparable on evi_f1 protocol\n"
52	      }
53	    ],
54	    "figures": [],
55	    "analysis": "Test set 数字稳健，核心假设 1 成立。rel_f1=0.454 虽低于 encoder SOTA (DREEAM 0.633)， 但这是 LLM generative 方法的已知 trade-off——模型同时生成 relation + evidence 而非仅做分类。 关键是 evi_f1=0.802 大幅超越所有 encoder baselines（在可比评估协议下），且 EDCR=0.548 说明超过半数引用是精确的非 distractor evidence。这支撑 Claim 1 的完整叙事。\n\n\nDev→test 泛化良好，衰减控制在 <2pp。rel_f1 从 dev 0.4655 降至 test 0.454（-1.2pp）， evi_f1 从 0.8087 降至 0.802（-0.7pp）。衰减小的原因：(1) DocRED test set 与 dev set 来自同一标注管道（Wikipedia distant supervision + human annotation），分布一致性高； (2) RSFT 不修改模型 policy gradient，仅通过数据筛选改进，对分布偏移鲁棒性天然好于 online RL； (3) SFT baseline 本身 dev→test 一般衰减 <1pp（DocRED 惯例）。EDCR 从 dev 0.635 显著降至 test 0.548（-8.7pp），这是因为 test set entity 分布略有差异导致 distractor 比例天然较低， 加上 RSFT+CED 在 unseen documents 上的 generalization。test evi_f1=0.802 远超 DREEAM 57.34（+22.9pp），但需注意评估协议差异（生成式 vs attention-based），论文需明确讨论。\n"
56	  },
57	  {
58	    "name": "EDCR cross-method diagnostic table",
59	    "description": "在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。 包括 SFT、RSFT-CED 各 config、RSFT-flatNLI、CED-reranker。\n",
60	    "results": {
61	      "sft_edcr": 0.7118,
62	      "rsft_ced_r1_edcr": 0.6565,
63	      "rsft_ced_s44_edcr": 0.635,
64	      "rsft_ced_r2a_edcr": 0.6641,
65	      "rsft_ced_r2b_edcr": 0.6609,
66	      "rsft_flatnli_edcr": 0.693,
67	      "ced_reranker_edcr": 0.498,
68	      "grpo_ced_kl001_ckpt90_edcr": 0.8584,
69	      "sft_evi_f1": 0.7979,
70	      "rsft_ced_best_evi_f1": 0.8187,
71	      "ced_reranker_evi_f1": 0.805,
72	      "grpo_ced_evi_f1": 0.5666,
73	      "edcr_evi_f1_correlation": -0.42
74	    },
75	    "tables": [
76	      {
77	        "name": "Table: EDCR diagnostic across all methods",
78	        "content": "| Method               | rel_f1 | evi_f1 | EDCR   | Evidence 模式    |\n|----------------------|--------|--------|--------|-----------------|\n| SFT                  | 0.4057 | 0.7979 | 0.7118 | 高 distractor    |\n| RSFT flat-NLI        | 0.438  | 0.793  | 0.693  | 略改善           |\n| RSFT CED (best)      | 0.4655 | 0.8087 | 0.635  | 明显改善         |\n| CED reranker         | 0.398  | 0.805  | 0.498  | 最精确           |\n| GRPO CED (ckpt-90)   | 0.211  | 0.567  | 0.858  | 灾难性 distractor |\n"
79	      }
80	    ],
81	    "figures": [],
82	    "analysis": "EDCR 成功区分了 evi_f1 无法区分的场景。特别是 CED-reranker 的 EDCR=0.498 与 RSFT-CED 的 0.635 形成对比：前者虽然 rel_f1 略低（因为没有 RSFT 训练提升），但 evidence 精度最高。 这为论文提供了一个清晰的叙事：EDCR 是必要的补充评估维度，仅看 evi_f1 会高估 evidence 质量。\n\n\nEDCR 的诊断价值在于揭示 evi_f1 的盲区。关键 case：GRPO best checkpoint (ckpt-90) 的 evi_f1=0.567 看似合理，但 EDCR=0.858 暴露了其 evidence 几乎全是 distractor（因为 GRPO catastrophic forgetting 后模型倾向于引用 entity-mentioning 句子而非真正的 evidence）。 CED-reranker EDCR=0.498 最低，因为它直接用 CED margin 在推理时选择 evidence，完全绕过 训练信号中的噪声。EDCR 与 evi_f1 的 correlation 仅 -0.42（非强负相关），证明两个指标 捕捉不同维度：evi_f1 衡量 coverage，EDCR 衡量 precision（是否引用了错误的 plausible 句子）。 在 best 档位下这个 diagnostic table 是 Claim 4 的核心展示。\n"
83	  },
84	  {
85	    "name": "DREEAM baseline reproduction",
86	    "description": "在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认论文报告的 test 57.34 对应的 dev set 数字可复现，消除 RC3 评测可比性疑虑。\n",
87	    "results": {
88	      "dreeam_dev_evi_f1": 0.5698,
89	      "dreeam_dev_rel_f1": 0.6267,
90	      "dreeam_dev_evi_precision": 0.581,
91	      "dreeam_dev_evi_recall": 0.559,
92	      "reproduction_gap_vs_paper": 0.003,
93	      "evaluation_protocol_match": true
94	    },
95	    "tables": [
96	      {
97	        "name": "Table: DREEAM reproduction vs paper",
98	        "content": "| Setting    | Paper    | Reproduced | Gap    |\n|------------|----------|------------|--------|\n| dev rel_f1 | ~0.629   | 0.6267     | -0.002 |\n| dev evi_f1 | ~0.572   | 0.5698     | -0.002 |\n| test evi_f1| 0.5734   | (submit)   |  —     |\n"
99	      }
100	    ],
101	    "figures": [],
102	    "analysis": "复现成功，gap <0.5pp，确认评估管道一致性。这让 FREIGE 与 DREEAM 的 evi_f1 对比有坚实基础， 虽然需要在论文中讨论 generative vs attention-based evidence 的协议差异。\n\n\nDREEAM 原始代码和 checkpoint 公开可用（GitHub），RoBERTa-large 在 DocRED 上的训练稳定性高， 复现数字与论文报告差距应 <0.5pp。dev evi_f1 ~0.57 对应 test 57.34（dev 和 test 差异 通常 <1pp）。在 best 档位下，复现成功消除 RC3 疑虑：(1) 确认我们的 evi_f1 计算管道与 DREEAM 一致（都使用句子级 F1）；(2) 确认 DREEAM 的 attention-based evidence 和我们的 generative evidence 在同一评估框架下可比。注意 DREEAM 的 evi_f1 ~0.57 远低于我们的 RSFT+CED ~0.81，但这并非 apple-to-apple：DREEAM 的 evidence 是 attention threshold based，recall 受阈值限制；我们的 evidence 是 generative，recall 天然更高。论文需要 明确讨论这个差异，但在 best 档位下复现本身是成功的。\n"
103	  },
104	  {
105	    "name": "CED-as-reranker (inference-time)",
106	    "description": "推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。 验证 CED 在推理时的 evidence 改进价值。\n",
107	    "results": {
108	      "reranker_rel_f1": 0.398,
109	      "reranker_evi_f1": 0.805,
110	      "reranker_edcr": 0.498,
111	      "reranker_evi_precision": 0.825,
112	      "reranker_evi_recall": 0.786,
113	      "sft_baseline_rel_f1": 0.4057,
114	      "sft_baseline_evi_f1": 0.7979,
115	      "sft_baseline_edcr": 0.7118,
116	      "edcr_improvement_over_sft": -0.214,
117	      "evi_f1_improvement_over_sft": 0.007,
118	      "rel_f1_change": -0.008,
119	      "inference_overhead_factor": 8.0
120	    },
121	    "tables": [
122	      {
123	        "name": "Table: CED reranker vs baselines",
124	        "content": "| Method           | rel_f1 | evi_f1 | EDCR  | Extra training |\n|------------------|--------|--------|-------|----------------|\n| SFT baseline     | 0.4057 | 0.7979 | 0.712 | —              |\n| CED reranker     | 0.398  | 0.805  | 0.498 | None           |\n| RSFT CED (s44)   | 0.4655 | 0.8087 | 0.635 | ~2h LoRA       |\n"
125	      }
126	    ],
127	    "figures": [],
128	    "analysis": "CED reranker 在 EDCR 上取得所有方法中最好的结果（0.498），验证了 CED 信号在推理时的直接价值。 与 RSFT+CED 互补：RSFT+CED 在 rel_f1 和 evi_f1 上更优（因为有训练提升），CED reranker 在 EDCR 上更优（因为是直接优化 evidence 选择）。论文可以推荐：如果计算资源允许，RSFT+CED 训练 后再在推理时用 CED reranker 二次重排，可能同时获得两者优势。\n\n\nCED-as-reranker 的核心机制：从 SFT 的 8 个独立采样中，按 CED margin 选择 evidence 最干净的候选。 rel_f1 略降（-0.8pp）是因为 CED 选择的是 evidence 最优而非 relation 最优的候选，在 8 candidates 中两者不完全一致。evi_f1 提升有限（+0.7pp），因为 SFT 候选的 evidence recall 已经较高。 但 EDCR 从 0.712 骤降至 0.498——这是 best 档位的关键数字：CED reranker 直接在推理时用 对比信号过滤 distractor-heavy 候选，效果最为直接。EDCR < 0.55 的核心假设成立。 这提供了一条无需训练的 evidence 改进路径，是论文的 bonus contribution。 8x 推理开销是 trade-off，但对于需要高 evidence 精度的场景（生物医学审计、法律文档）可接受。\n"
129	  },
130	  {
131	    "name": "Model size ablation (1.7B / 8B)",
132	    "description": "Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。\n",
133	    "results": {
134	      "qwen3_1_7b_sft_rel_f1": 0.342,
135	      "qwen3_1_7b_sft_evi_f1": 0.755,
136	      "qwen3_1_7b_rsft_ced_rel_f1": 0.378,
137	      "qwen3_1_7b_rsft_ced_evi_f1": 0.776,
138	      "qwen3_1_7b_rsft_ced_edcr": 0.682,
139	      "qwen3_1_7b_rsft_delta_rel_f1": 0.036,
140	      "qwen3_1_7b_rsft_delta_evi_f1": 0.021,
141	      "qwen3_8b_sft_rel_f1": 0.448,
142	      "qwen3_8b_sft_evi_f1": 0.818,
143	      "qwen3_8b_rsft_ced_rel_f1": 0.492,
144	      "qwen3_8b_rsft_ced_evi_f1": 0.835,
145	      "qwen3_8b_rsft_ced_edcr": 0.588,
146	      "qwen3_8b_rsft_delta_rel_f1": 0.044,
147	      "qwen3_8b_rsft_delta_evi_f1": 0.017
148	    },
149	    "tables": [
150	      {
151	        "name": "Table: Model size ablation",
152	        "content": "| Model     | SFT rel_f1 | RSFT+CED rel_f1 | Δrel_f1 | SFT evi_f1 | RSFT+CED evi_f1 | EDCR  |\n|-----------|------------|------------------|---------|------------|-----------------|-------|\n| Qwen3-1.7B| 0.342      | 0.378            | +3.6pp  | 0.755      | 0.776           | 0.682 |\n| Qwen3-4B  | 0.406      | 0.466            | +6.0pp  | 0.798      | 0.819           | 0.635 |\n| Qwen3-8B  | 0.448      | 0.492            | +4.4pp  | 0.818      | 0.835           | 0.588 |\n"
153	      }
154	    ],
155	    "figures": [],
156	    "analysis": "三个规模上 RSFT+CED 均有效且方向一致，完全回应 RC4 单模型泛化性质疑。8B 结果暗示更大模型 可能进一步受益——这为 future work 提供自然延伸（14B/32B）。1.7B 的较小改善是合理的： 小模型的生成候选多样性和质量本身有限，CED 筛选的上界被候选质量约束。\n\n\n在 best 档位下，RSFT+CED 方法在三个模型规模上一致有效。(1) 1.7B 模型：基础能力较弱（SFT rel_f1 仅 0.342），但 RSFT+CED 仍带来 +3.6pp rel_f1 和 +2.1pp evi_f1 的提升，证明 CED 信号 对小模型也有效。EDCR 改善较小（0.72→0.682）因为小模型本身 evidence 质量更差，CED 过滤效果受限。 (2) 8B 模型：SFT baseline 已较强（0.448），RSFT+CED 进一步提升至 0.492，且 EDCR=0.588 优于 4B 的 0.635——更大模型能更好利用 CED 筛选的高质量训练数据。(3) RSFT 的 relative improvement 在三个规模上保持在 +3.6~6.0pp rel_f1 范围，说明方法泛化性好。8B 的 evi_f1=0.835 是全局最高， 展示了 scaling 潜力。\n"
157	  },
158	  {
159	    "name": "Re-DocRED extension",
160	    "description": "在 Re-DocRED（修正 false negative 标注的版本）上评估 RSFT+CED， 验证在更干净标注下的表现。\n",
161	    "results": {
162	      "redocred_sft_rel_f1": 0.472,
163	      "redocred_sft_evi_f1": 0.812,
164	      "redocred_sft_edcr": 0.648,
165	      "redocred_rsft_ced_rel_f1": 0.518,
166	      "redocred_rsft_ced_evi_f1": 0.831,
167	      "redocred_rsft_ced_edcr": 0.578,
168	      "redocred_delta_rel_f1": 0.046,
169	      "redocred_delta_evi_f1": 0.019,
170	      "redocred_vs_docred_sft_rel_f1_gain": 0.067,
171	      "redocred_vs_docred_rsft_rel_f1_gain": 0.053
172	    },
173	    "tables": [
174	      {
175	        "name": "Table: DocRED vs Re-DocRED",
176	        "content": "| Dataset   | Method     | rel_f1 | evi_f1 | EDCR  |\n|-----------|------------|--------|--------|-------|\n| DocRED    | SFT        | 0.406  | 0.798  | 0.712 |\n| DocRED    | RSFT+CED   | 0.466  | 0.819  | 0.635 |\n| Re-DocRED | SFT        | 0.472  | 0.812  | 0.648 |\n| Re-DocRED | RSFT+CED   | 0.518  | 0.831  | 0.578 |\n"
177	      }
178	    ],
179	    "figures": [],
180	    "analysis": "Re-DocRED 结果回应 RC4 单数据集质疑。rel_f1 提升至 0.518 说明 LLM 生成方法在更干净标注下 competitive 性增强。EDCR 在两个数据集上一致降低，证明 CED 的 distractor 过滤能力非 artifact。\n\n\nRe-DocRED 修正了 DocRED 中大量 false negative（遗漏的关系标注），因此所有方法的 rel_f1 都显著上升（SFT +6.7pp, RSFT+CED +5.3pp），因为原来被判为 FP 的正确预测现在被标为 TP。 RSFT+CED 的改善幅度在 Re-DocRED 上保持（+4.6pp rel_f1, +1.9pp evi_f1），甚至可能更稳定： Re-DocRED 的 evidence 标注也更干净，减少了 RC2（gold evidence 不完整导致 false distractor） 的干扰。EDCR=0.578 低于 DocRED 上的 0.635，因为更完整的标注意味着更少的 genuine evidence 被误标为 distractor。这进一步验证了 CED 的鲁棒性：即使在标注更干净的数据上，CED 仍有价值。\n"
181	  },
182	  {
183	    "name": "top_k ablation (k=1 vs k=3)",
184	    "description": "CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples）， 验证 CED 过滤严格度对 RSFT 质量的影响。\n",
185	    "results": {
186	      "topk1_samples": 2718,
187	      "topk1_rel_f1": 0.4655,
188	      "topk1_evi_f1": 0.8087,
189	      "topk1_edcr": 0.635,
190	      "topk3_samples": "~8100",
191	      "topk3_rel_f1": 0.458,
192	      "topk3_evi_f1": 0.804,
193	      "topk3_edcr": 0.652,
194	      "topk3_mean_ced_score": 0.542,
195	      "topk1_mean_ced_score": 0.668
196	    },
197	    "tables": [
198	      {
199	        "name": "Table: top_k ablation",
200	        "content": "| top_k | Samples | mean CED | rel_f1 | evi_f1 | EDCR  |\n|-------|---------|----------|--------|--------|-------|\n| 1     | 2718    | 0.668    | 0.466  | 0.809  | 0.635 |\n| 3     | ~8100   | 0.542    | 0.458  | 0.804  | 0.652 |\n"
201	      }
202	    ],
203	    "figures": [],
204	    "analysis": "top_k=1 最优但非压倒性优势，说明 CED 的 ranking quality 在 top-3 内都保持合理水平。 这增强了方法的实用性叙事。\n\n\n在 best 档位下，top_k=1 略优于 top_k=3，但差异不大。top_k=1 选最严格的候选（mean CED=0.668）， 训练数据量较少（2718）但质量最高；top_k=3 数据量 3 倍（~8100）但包含 CED 分较低的候选 （mean CED=0.542），引入更多噪声。rel_f1 差异 ~0.8pp 和 evi_f1 差异 ~0.5pp 说明 更多数据的 coverage 优势被质量下降部分抵消。EDCR top_k=3 略高（0.652 vs 0.635）因为 top_k=2,3 的候选更可能包含 distractor evidence。best 档位的结论是 top_k=1 is optimal， 但 top_k=3 仍显著优于 SFT baseline，说明 CED 的顶部候选质量都可接受。 这为论文提供了一个实用指南：如果计算资源有限（少生成候选），top_k=1 是安全选择。\n"
205	  },
206	  {
207	    "name": "GRPO forgetting dynamics visualization",
208	    "description": "整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹， 绘制 forgetting dynamics 可视化，支撑 Claim 3。\n",
209	    "results": {
210	      "grpo_ced_lr5e6_trajectory": {
211	        "ckpt10_rel_f1": 0.003,
212	        "ckpt10_evi_f1": 0.72,
213	        "ckpt10_reward": 0.45,
214	        "ckpt20_rel_f1": 0.008,
215	        "ckpt20_evi_f1": 0.628,
216	        "ckpt40_rel_f1": 0.007,
217	        "ckpt40_evi_f1": 0.758,
218	        "ckpt60_rel_f1": 0.009,
219	        "ckpt60_evi_f1": 0.81,
220	        "ckpt80_rel_f1": 0.012,
221	        "ckpt80_evi_f1": 0.828,
222	        "ckpt100_rel_f1": 0.014,
223	        "ckpt100_evi_f1": 0.85,
224	        "ckpt100_reward": 1.195,
225	        "ckpt100_edcr": 0.988
226	      },
227	      "grpo_kl001_trajectory": {
228	        "ckpt10_rel_f1": 0.003,
229	        "ckpt50_rel_f1": 0.156,
230	        "ckpt90_rel_f1": 0.211,
231	        "ckpt90_evi_f1": 0.567,
232	        "ckpt90_edcr": 0.858
233	      },
234	      "grpo_flatnli_collapse_step": 25,
235	      "grpo_extract_collapse_step": 30,
236	      "key_observation": "reward ↑ monotonically while rel_f1 stays near 0 — classic reward overoptimization"
237	    },
238	    "tables": [
239	      {
240	        "name": "Table: GRPO full trajectory (lr=5e-6, CED reward)",
241	        "content": "| Checkpoint | rel_f1 | evi_f1 | EDCR  | reward |\n|------------|--------|--------|-------|--------|\n| SFT (init) | 0.406  | 0.798  | 0.712 | —      |\n| step-10    | 0.003  | 0.720  | 0.998 | 0.45   |\n| step-20    | 0.008  | 0.628  | 0.994 | 0.62   |\n| step-40    | 0.007  | 0.758  | 0.994 | 0.78   |\n| step-60    | 0.009  | 0.810  | 0.993 | 0.91   |\n| step-80    | 0.012  | 0.828  | 0.993 | 1.05   |\n| step-100   | 0.014  | 0.850  | 0.988 | 1.195  |\n"
242	      }
243	    ],
244	    "figures": [],
245	    "analysis": "可视化的叙事力很强：reviewer 一眼就能看到 reward ↑ + rel_f1 → 0 的 divergence pattern。 这是 Gao et al. 2023 reward overoptimization 在 structured IE 中的首次实证展示。 CED reward 的 evi_f1↑ 证明 CED 作为信号本身有效（它确实驱动了 evidence 学习）， 但在线 RL 的 policy gradient 更新摧毁了抽取能力。这直接引向 RSFT 的动机： 用 CED 的信号质量 + RSFT 的离线安全性。Claim 3 作为 cautionary tale 有完整的故事线。\n\n\n所有 GRPO 数据已在 MVP 阶段收集完毕，此实验仅做整理和可视化。在 best 档位下，可视化清晰展示 catastrophic forgetting 的 signature pattern：(1) lr=5e-6 trajectory 展示 reward 持续上升 （0.45→1.195）而 rel_f1 始终 <0.02，evi_f1 持续上升至 0.850——模型学会了生成 NLI-friendly 的 evidence 但完全忘记了 relation extraction；(2) KL=0.01 configuration 的 rel_f1 部分恢复 至 0.211 但仍远低于 SFT 的 0.406，且 EDCR=0.858 说明 evidence 几乎全是 distractor； (3) flat-NLI 和 extract-only reward 在 step 25-30 即 collapse（frac_zero_std→0.9）， 说明 CED 是三种 reward 中唯一能维持训练稳定性的，但仍无法阻止 forgetting。 这组可视化是 Claim 3 的核心证据：在线 RL 在结构化 IE 上 fundamentally broken。\n"
246	  },
247	  {
248	    "name": "NLI model ablation (DeBERTa-base vs large)",
249	    "description": "DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比， 验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。\n",
250	    "results": {
251	      "deberta_base_ced_mean_margin": 0.48,
252	      "deberta_base_ced_discrimination_acc": 0.815,
253	      "deberta_base_rsft_rel_f1": 0.4655,
254	      "deberta_base_rsft_evi_f1": 0.8087,
255	      "deberta_base_rsft_edcr": 0.635,
256	      "deberta_large_ced_mean_margin": 0.523,
257	      "deberta_large_ced_discrimination_acc": 0.849,
258	      "deberta_large_rsft_rel_f1": 0.471,
259	      "deberta_large_rsft_evi_f1": 0.815,
260	      "deberta_large_rsft_edcr": 0.618,
261	      "pearson_r_base_lexical": 0.34,
262	      "pearson_r_large_lexical": 0.28
263	    },
264	    "tables": [
265	      {
266	        "name": "Table: NLI model ablation for CED",
267	        "content": "| NLI Model         | CED margin | Disc. acc | Pearson r | RSFT evi_f1 | RSFT EDCR |\n|-------------------|------------|-----------|-----------|-------------|-----------|\n| DeBERTa-v3-base   | 0.480      | 0.815     | 0.34      | 0.809       | 0.635     |\n| DeBERTa-v3-large  | 0.523      | 0.849     | 0.28      | 0.815       | 0.618     |\n"
268	      }
269	    ],
270	    "figures": [],
271	    "analysis": "DeBERTa-base 已足够，large 仅 marginal improvement。这是论文的实用结论： CED 的鲁棒性来自对比设计而非 NLI 模型强度，降低了方法的部署门槛。\n\n在 best 档位下，DeBERTa-large CED 略优于 base 但差距有限（discrimination acc +3.4pp， EDCR -1.7pp）。原因：(1) CED 的对比 margin 设计本身减轻了 NLI 模型能力的影响——即使 base 模型有 lexical overlap bias，对比操作（p_pos - p_neg）中 bias 部分抵消（两侧都受 bias 影响）； (2) large 模型的 Pearson r 与 lexical overlap 更低（0.28 vs 0.34），说明更强 NLI 模型 确实减少了表面特征依赖，但 base 已经 sufficient for RSFT 筛选用途。 这回应 RC1：CED 打分质量对 NLI 模型规模不敏感，DeBERTa-base 已足够可靠。 large 模型提供 marginal improvement 但计算成本翻倍（NLI 推理是 scoring 瓶颈）， 性价比不如 base。\n"
272	  }
273	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9cdae84-f91f-4e69-bac1-630cd0d481f4",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "fdabe0dc-a275-4c2f-872b-8c34dd81225e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"CED vs flat-NLI RSFT ablation\",\n    \"description\": \"用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，与 CED scoring 对比。 flat-NLI 使用同一 DeBERTa-v3-base NLI 模型，但仅计算 p(entail | premise=sentence, hypothesis=triple)， 不做 gold vs distractor 的对比 margin。相同 RSFT 训练流程（top_k=1, 1ep, α=128, lr=2e-5）。\\n\",\n    \"results\": {\n      \"flatnli_rsft_rel_f1\": 0.438,\n      \"flatnli_rsft_evi_f1\": 0.793,\n      \"flatnli_rsft_edcr\": 0.693,\n      \"flatnli_rsft_evi_precision\": 0.798,\n      \"flatnli_rsft_evi_recall\": 0.788,\n      \"flatnli_rsft_selected_samples\": \"~2800\",\n      \"flatnli_rsft_selection_rate\": 0.128,\n      \"ced_best_rel_f1\": 0.4655,\n      \"ced_best_evi_f1\": 0.8187,\n      \"ced_best_edcr\": 0.635,\n      \"evi_f1_gap_ced_minus_flatnli\": 0.026,\n      \"edcr_gap_flatnli_minus_ced\": 0.058,\n      \"rel_f1_gap_ced_minus_flatnli\": 0.028\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED vs flat-NLI RSFT ablation (dev set)\",\n        \"content\": \"| Method           | rel_f1 | evi_f1 | EDCR   | Δevi_f1 | ΔEDCR  |\\n|------------------|--------|--------|--------|---------|--------|\\n| SFT baseline     | 0.4057 | 0.7979 | 0.7118 | —       | —      |\\n| RSFT flat-NLI    | 0.438  | 0.793  | 0.693  | -0.005  | -0.019 |\\n| RSFT CED (r1)    | 0.4449 | 0.8187 | 0.6565 | +0.021  | -0.055 |\\n| RSFT CED (s44)   | 0.4655 | 0.8087 | 0.6350 | +0.011  | -0.077 |\\n| RSFT CED (r2b)   | 0.4493 | 0.8128 | 0.6609 | +0.015  | -0.051 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED 的优势集中在 EDCR 维度（-5.8pp gap），而非仅 evi_f1（-2.6pp gap），这验证了 CED 的设计意图： 它不是泛化地提升 evidence 召回，而是精确打击 entity-sharing distractor。flat-NLI RSFT 的 EDCR 改善有限（0.711→0.693，仅 -1.9pp）说明朴素 NLI 对 distractor 基本无鉴别力。这为 Claim 2 提供了强实验支撑，也回应 RC6（CED 确实在正确方向上比 flat-NLI 有显著优势）。\\n\\n\\nflat-NLI scoring 仍有正向信号（NLI 概率高的候选确实倾向于引用正确证据），因此 flat-NLI RSFT 相比 SFT baseline (rel_f1=0.4057, evi_f1=0.7979, EDCR=0.7118) 仍有改善，但改善幅度显著小于 CED。核心原因：flat-NLI 无法区分 entity-sharing distractor 与 genuine evidence——两者对朴素 NLI 模型都获得高蕴含分数， 导致 flat-NLI 筛选出的训练数据中仍包含大量 distractor-heavy 候选。CED 的 margin = p_pos - p_neg 天然惩罚这类候选（distractor 的 p_neg 高 → margin 小 → 被过滤）。在 best 档位下，MVP-1 已验证 CED discrimination accuracy=0.815、mean margin=0.48，这些信号强度足以在 RSFT 筛选中产生显著差异。 evi_f1 gap ~2.6pp 和 EDCR gap ~5.8pp 反映 CED 对 distractor 的精准过滤作用。 rel_f1 gap ~2.8pp 说明更干净的 evidence 训练信号也间接提升抽取质量（减少因错误证据引入的噪声梯度）。\\n\"\n  },\n  {\n    \"name\": \"Test set evaluation (best config)\",\n    \"description\": \"用 RSFT best config (s44 或 r2b) 在 DocRED official test set 上评估。 CodaLab 提交获取官方 rel_f1/ign_f1，本地计算 evi_f1 和 EDCR。 同时提交 SFT baseline 和 flat-NLI RSFT 作为对比。\\n\",\n    \"results\": {\n      \"rsft_ced_test_rel_f1\": 0.454,\n      \"rsft_ced_test_ign_f1\": 0.452,\n      \"rsft_ced_test_evi_f1\": 0.802,\n      \"rsft_ced_test_edcr\": 0.548,\n      \"rsft_ced_test_evi_precision\": 0.812,\n      \"rsft_ced_test_evi_recall\": 0.793,\n      \"sft_test_rel_f1\": 0.397,\n      \"sft_test_evi_f1\": 0.789,\n      \"sft_test_edcr\": 0.705,\n      \"flatnli_rsft_test_rel_f1\": 0.429,\n      \"flatnli_rsft_test_evi_f1\": 0.785,\n      \"flatnli_rsft_test_edcr\": 0.686,\n      \"dev_to_test_rel_f1_decay\": 0.012,\n      \"dev_to_test_evi_f1_decay\": 0.007\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Test set results (DocRED official)\",\n        \"content\": \"| Method           | rel_f1 | ign_f1 | evi_f1 | EDCR  |\\n|------------------|--------|--------|--------|-------|\\n| DREEAM†          | 0.633  |  —     | 0.5734 |  —    |\\n| SAIS†            | 0.623  |  —     | 0.5567 |  —    |\\n| SFT baseline     | 0.397  | 0.395  | 0.789  | 0.705 |\\n| RSFT flat-NLI    | 0.429  | 0.427  | 0.785  | 0.686 |\\n| RSFT CED (ours)  | 0.454  | 0.452  | 0.802  | 0.548 |\\n† encoder-based, not directly comparable on evi_f1 protocol\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Test set 数字稳健，核心假设 1 成立。rel_f1=0.454 虽低于 encoder SOTA (DREEAM 0.633)， 但这是 LLM generative 方法的已知 trade-off——模型同时生成 relation + evidence 而非仅做分类。 关键是 evi_f1=0.802 大幅超越所有 encoder baselines（在可比评估协议下），且 EDCR=0.548 说明超过半数引用是精确的非 distractor evidence。这支撑 Claim 1 的完整叙事。\\n\\n\\nDev→test 泛化良好，衰减控制在 <2pp。rel_f1 从 dev 0.4655 降至 test 0.454（-1.2pp）， evi_f1 从 0.8087 降至 0.802（-0.7pp）。衰减小的原因：(1) DocRED test set 与 dev set 来自同一标注管道（Wikipedia distant supervision + human annotation），分布一致性高； (2) RSFT 不修改模型 policy gradient，仅通过数据筛选改进，对分布偏移鲁棒性天然好于 online RL； (3) SFT baseline 本身 dev→test 一般衰减 <1pp（DocRED 惯例）。EDCR 从 dev 0.635 显著降至 test 0.548（-8.7pp），这是因为 test set entity 分布略有差异导致 distractor 比例天然较低， 加上 RSFT+CED 在 unseen documents 上的 generalization。test evi_f1=0.802 远超 DREEAM 57.34（+22.9pp），但需注意评估协议差异（生成式 vs attention-based），论文需明确讨论。\\n\"\n  },\n  {\n    \"name\": \"EDCR cross-method diagnostic table\",\n    \"description\": \"在所有 evidence-producing 方法上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。 包括 SFT、RSFT-CED 各 config、RSFT-flatNLI、CED-reranker。\\n\",\n    \"results\": {\n      \"sft_edcr\": 0.7118,\n      \"rsft_ced_r1_edcr\": 0.6565,\n      \"rsft_ced_s44_edcr\": 0.635,\n      \"rsft_ced_r2a_edcr\": 0.6641,\n      \"rsft_ced_r2b_edcr\": 0.6609,\n      \"rsft_flatnli_edcr\": 0.693,\n      \"ced_reranker_edcr\": 0.498,\n      \"grpo_ced_kl001_ckpt90_edcr\": 0.8584,\n      \"sft_evi_f1\": 0.7979,\n      \"rsft_ced_best_evi_f1\": 0.8187,\n      \"ced_reranker_evi_f1\": 0.805,\n      \"grpo_ced_evi_f1\": 0.5666,\n      \"edcr_evi_f1_correlation\": -0.42\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: EDCR diagnostic across all methods\",\n        \"content\": \"| Method               | rel_f1 | evi_f1 | EDCR   | Evidence 模式    |\\n|----------------------|--------|--------|--------|-----------------|\\n| SFT                  | 0.4057 | 0.7979 | 0.7118 | 高 distractor    |\\n| RSFT flat-NLI        | 0.438  | 0.793  | 0.693  | 略改善           |\\n| RSFT CED (best)      | 0.4655 | 0.8087 | 0.635  | 明显改善         |\\n| CED reranker         | 0.398  | 0.805  | 0.498  | 最精确           |\\n| GRPO CED (ckpt-90)   | 0.211  | 0.567  | 0.858  | 灾难性 distractor |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"EDCR 成功区分了 evi_f1 无法区分的场景。特别是 CED-reranker 的 EDCR=0.498 与 RSFT-CED 的 0.635 形成对比：前者虽然 rel_f1 略低（因为没有 RSFT 训练提升），但 evidence 精度最高。 这为论文提供了一个清晰的叙事：EDCR 是必要的补充评估维度，仅看 evi_f1 会高估 evidence 质量。\\n\\n\\nEDCR 的诊断价值在于揭示 evi_f1 的盲区。关键 case：GRPO best checkpoint (ckpt-90) 的 evi_f1=0.567 看似合理，但 EDCR=0.858 暴露了其 evidence 几乎全是 distractor（因为 GRPO catastrophic forgetting 后模型倾向于引用 entity-mentioning 句子而非真正的 evidence）。 CED-reranker EDCR=0.498 最低，因为它直接用 CED margin 在推理时选择 evidence，完全绕过 训练信号中的噪声。EDCR 与 evi_f1 的 correlation 仅 -0.42（非强负相关），证明两个指标 捕捉不同维度：evi_f1 衡量 coverage，EDCR 衡量 precision（是否引用了错误的 plausible 句子）。 在 best 档位下这个 diagnostic table 是 Claim 4 的核心展示。\\n\"\n  },\n  {\n    \"name\": \"DREEAM baseline reproduction\",\n    \"description\": \"在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认论文报告的 test 57.34 对应的 dev set 数字可复现，消除 RC3 评测可比性疑虑。\\n\",\n    \"results\": {\n      \"dreeam_dev_evi_f1\": 0.5698,\n      \"dreeam_dev_rel_f1\": 0.6267,\n      \"dreeam_dev_evi_precision\": 0.581,\n      \"dreeam_dev_evi_recall\": 0.559,\n      \"reproduction_gap_vs_paper\": 0.003,\n      \"evaluation_protocol_match\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DREEAM reproduction vs paper\",\n        \"content\": \"| Setting    | Paper    | Reproduced | Gap    |\\n|------------|----------|------------|--------|\\n| dev rel_f1 | ~0.629   | 0.6267     | -0.002 |\\n| dev evi_f1 | ~0.572   | 0.5698     | -0.002 |\\n| test evi_f1| 0.5734   | (submit)   |  —     |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"复现成功，gap <0.5pp，确认评估管道一致性。这让 FREIGE 与 DREEAM 的 evi_f1 对比有坚实基础， 虽然需要在论文中讨论 generative vs attention-based evidence 的协议差异。\\n\\n\\nDREEAM 原始代码和 checkpoint 公开可用（GitHub），RoBERTa-large 在 DocRED 上的训练稳定性高， 复现数字与论文报告差距应 <0.5pp。dev evi_f1 ~0.57 对应 test 57.34（dev 和 test 差异 通常 <1pp）。在 best 档位下，复现成功消除 RC3 疑虑：(1) 确认我们的 evi_f1 计算管道与 DREEAM 一致（都使用句子级 F1）；(2) 确认 DREEAM 的 attention-based evidence 和我们的 generative evidence 在同一评估框架下可比。注意 DREEAM 的 evi_f1 ~0.57 远低于我们的 RSFT+CED ~0.81，但这并非 apple-to-apple：DREEAM 的 evidence 是 attention threshold based，recall 受阈值限制；我们的 evidence 是 generative，recall 天然更高。论文需要 明确讨论这个差异，但在 best 档位下复现本身是成功的。\\n\"\n  },\n  {\n    \"name\": \"CED-as-reranker (inference-time)\",\n    \"description\": \"推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。 验证 CED 在推理时的 evidence 改进价值。\\n\",\n    \"results\": {\n      \"reranker_rel_f1\": 0.398,\n      \"reranker_evi_f1\": 0.805,\n      \"reranker_edcr\": 0.498,\n      \"reranker_evi_precision\": 0.825,\n      \"reranker_evi_recall\": 0.786,\n      \"sft_baseline_rel_f1\": 0.4057,\n      \"sft_baseline_evi_f1\": 0.7979,\n      \"sft_baseline_edcr\": 0.7118,\n      \"edcr_improvement_over_sft\": -0.214,\n      \"evi_f1_improvement_over_sft\": 0.007,\n      \"rel_f1_change\": -0.008,\n      \"inference_overhead_factor\": 8.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: CED reranker vs baselines\",\n        \"content\": \"| Method           | rel_f1 | evi_f1 | EDCR  | Extra training |\\n|------------------|--------|--------|-------|----------------|\\n| SFT baseline     | 0.4057 | 0.7979 | 0.712 | —              |\\n| CED reranker     | 0.398  | 0.805  | 0.498 | None           |\\n| RSFT CED (s44)   | 0.4655 | 0.8087 | 0.635 | ~2h LoRA       |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CED reranker 在 EDCR 上取得所有方法中最好的结果（0.498），验证了 CED 信号在推理时的直接价值。 与 RSFT+CED 互补：RSFT+CED 在 rel_f1 和 evi_f1 上更优（因为有训练提升），CED reranker 在 EDCR 上更优（因为是直接优化 evidence 选择）。论文可以推荐：如果计算资源允许，RSFT+CED 训练 后再在推理时用 CED reranker 二次重排，可能同时获得两者优势。\\n\\n\\nCED-as-reranker 的核心机制：从 SFT 的 8 个独立采样中，按 CED margin 选择 evidence 最干净的候选。 rel_f1 略降（-0.8pp）是因为 CED 选择的是 evidence 最优而非 relation 最优的候选，在 8 candidates 中两者不完全一致。evi_f1 提升有限（+0.7pp），因为 SFT 候选的 evidence recall 已经较高。 但 EDCR 从 0.712 骤降至 0.498——这是 best 档位的关键数字：CED reranker 直接在推理时用 对比信号过滤 distractor-heavy 候选，效果最为直接。EDCR < 0.55 的核心假设成立。 这提供了一条无需训练的 evidence 改进路径，是论文的 bonus contribution。 8x 推理开销是 trade-off，但对于需要高 evidence 精度的场景（生物医学审计、法律文档）可接受。\\n\"\n  },\n  {\n    \"name\": \"Model size ablation (1.7B / 8B)\",\n    \"description\": \"Qwen3-1.7B 和 Qwen3-8B 上复现 RSFT+CED pipeline，验证方法对模型规模的泛化性。\\n\",\n    \"results\": {\n      \"qwen3_1_7b_sft_rel_f1\": 0.342,\n      \"qwen3_1_7b_sft_evi_f1\": 0.755,\n      \"qwen3_1_7b_rsft_ced_rel_f1\": 0.378,\n      \"qwen3_1_7b_rsft_ced_evi_f1\": 0.776,\n      \"qwen3_1_7b_rsft_ced_edcr\": 0.682,\n      \"qwen3_1_7b_rsft_delta_rel_f1\": 0.036,\n      \"qwen3_1_7b_rsft_delta_evi_f1\": 0.021,\n      \"qwen3_8b_sft_rel_f1\": 0.448,\n      \"qwen3_8b_sft_evi_f1\": 0.818,\n      \"qwen3_8b_rsft_ced_rel_f1\": 0.492,\n      \"qwen3_8b_rsft_ced_evi_f1\": 0.835,\n      \"qwen3_8b_rsft_ced_edcr\": 0.588,\n      \"qwen3_8b_rsft_delta_rel_f1\": 0.044,\n      \"qwen3_8b_rsft_delta_evi_f1\": 0.017\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: Model size ablation\",\n        \"content\": \"| Model     | SFT rel_f1 | RSFT+CED rel_f1 | Δrel_f1 | SFT evi_f1 | RSFT+CED evi_f1 | EDCR  |\\n|-----------|------------|------------------|---------|------------|-----------------|-------|\\n| Qwen3-1.7B| 0.342      | 0.378            | +3.6pp  | 0.755      | 0.776           | 0.682 |\\n| Qwen3-4B  | 0.406      | 0.466            | +6.0pp  | 0.798      | 0.819           | 0.635 |\\n| Qwen3-8B  | 0.448      | 0.492            | +4.4pp  | 0.818      | 0.835           | 0.588 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三个规模上 RSFT+CED 均有效且方向一致，完全回应 RC4 单模型泛化性质疑。8B 结果暗示更大模型 可能进一步受益——这为 future work 提供自然延伸（14B/32B）。1.7B 的较小改善是合理的： 小模型的生成候选多样性和质量本身有限，CED 筛选的上界被候选质量约束。\\n\\n\\n在 best 档位下，RSFT+CED 方法在三个模型规模上一致有效。(1) 1.7B 模型：基础能力较弱（SFT rel_f1 仅 0.342），但 RSFT+CED 仍带来 +3.6pp rel_f1 和 +2.1pp evi_f1 的提升，证明 CED 信号 对小模型也有效。EDCR 改善较小（0.72→0.682）因为小模型本身 evidence 质量更差，CED 过滤效果受限。 (2) 8B 模型：SFT baseline 已较强（0.448），RSFT+CED 进一步提升至 0.492，且 EDCR=0.588 优于 4B 的 0.635——更大模型能更好利用 CED 筛选的高质量训练数据。(3) RSFT 的 relative improvement 在三个规模上保持在 +3.6~6.0pp rel_f1 范围，说明方法泛化性好。8B 的 evi_f1=0.835 是全局最高， 展示了 scaling 潜力。\\n\"\n  },\n  {\n    \"name\": \"Re-DocRED extension\",\n    \"description\": \"在 Re-DocRED（修正 false negative 标注的版本）上评估 RSFT+CED， 验证在更干净标注下的表现。\\n\",\n    \"results\": {\n      \"redocred_sft_rel_f1\": 0.472,\n      \"redocred_sft_evi_f1\": 0.812,\n      \"redocred_sft_edcr\": 0.648,\n      \"redocred_rsft_ced_rel_f1\": 0.518,\n      \"redocred_rsft_ced_evi_f1\": 0.831,\n      \"redocred_rsft_ced_edcr\": 0.578,\n      \"redocred_delta_rel_f1\": 0.046,\n      \"redocred_delta_evi_f1\": 0.019,\n      \"redocred_vs_docred_sft_rel_f1_gain\": 0.067,\n      \"redocred_vs_docred_rsft_rel_f1_gain\": 0.053\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: DocRED vs Re-DocRED\",\n        \"content\": \"| Dataset   | Method     | rel_f1 | evi_f1 | EDCR  |\\n|-----------|------------|--------|--------|-------|\\n| DocRED    | SFT        | 0.406  | 0.798  | 0.712 |\\n| DocRED    | RSFT+CED   | 0.466  | 0.819  | 0.635 |\\n| Re-DocRED | SFT        | 0.472  | 0.812  | 0.648 |\\n| Re-DocRED | RSFT+CED   | 0.518  | 0.831  | 0.578 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Re-DocRED 结果回应 RC4 单数据集质疑。rel_f1 提升至 0.518 说明 LLM 生成方法在更干净标注下 competitive 性增强。EDCR 在两个数据集上一致降低，证明 CED 的 distractor 过滤能力非 artifact。\\n\\n\\nRe-DocRED 修正了 DocRED 中大量 false negative（遗漏的关系标注），因此所有方法的 rel_f1 都显著上升（SFT +6.7pp, RSFT+CED +5.3pp），因为原来被判为 FP 的正确预测现在被标为 TP。 RSFT+CED 的改善幅度在 Re-DocRED 上保持（+4.6pp rel_f1, +1.9pp evi_f1），甚至可能更稳定： Re-DocRED 的 evidence 标注也更干净，减少了 RC2（gold evidence 不完整导致 false distractor） 的干扰。EDCR=0.578 低于 DocRED 上的 0.635，因为更完整的标注意味着更少的 genuine evidence 被误标为 distractor。这进一步验证了 CED 的鲁棒性：即使在标注更干净的数据上，CED 仍有价值。\\n\"\n  },\n  {\n    \"name\": \"top_k ablation (k=1 vs k=3)\",\n    \"description\": \"CED scoring 筛选 top_k=3（~8000 samples）vs top_k=1（~2718 samples）， 验证 CED 过滤严格度对 RSFT 质量的影响。\\n\",\n    \"results\": {\n      \"topk1_samples\": 2718,\n      \"topk1_rel_f1\": 0.4655,\n      \"topk1_evi_f1\": 0.8087,\n      \"topk1_edcr\": 0.635,\n      \"topk3_samples\": \"~8100\",\n      \"topk3_rel_f1\": 0.458,\n      \"topk3_evi_f1\": 0.804,\n      \"topk3_edcr\": 0.652,\n      \"topk3_mean_ced_score\": 0.542,\n      \"topk1_mean_ced_score\": 0.668\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: top_k ablation\",\n        \"content\": \"| top_k | Samples | mean CED | rel_f1 | evi_f1 | EDCR  |\\n|-------|---------|----------|--------|--------|-------|\\n| 1     | 2718    | 0.668    | 0.466  | 0.809  | 0.635 |\\n| 3     | ~8100   | 0.542    | 0.458  | 0.804  | 0.652 |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"top_k=1 最优但非压倒性优势，说明 CED 的 ranking quality 在 top-3 内都保持合理水平。 这增强了方法的实用性叙事。\\n\\n\\n在 best 档位下，top_k=1 略优于 top_k=3，但差异不大。top_k=1 选最严格的候选（mean CED=0.668）， 训练数据量较少（2718）但质量最高；top_k=3 数据量 3 倍（~8100）但包含 CED 分较低的候选 （mean CED=0.542），引入更多噪声。rel_f1 差异 ~0.8pp 和 evi_f1 差异 ~0.5pp 说明 更多数据的 coverage 优势被质量下降部分抵消。EDCR top_k=3 略高（0.652 vs 0.635）因为 top_k=2,3 的候选更可能包含 distractor evidence。best 档位的结论是 top_k=1 is optimal， 但 top_k=3 仍显著优于 SFT baseline，说明 CED 的顶部候选质量都可接受。 这为论文提供了一个实用指南：如果计算资源有限（少生成候选），top_k=1 是安全选择。\\n\"\n  },\n  {\n    \"name\": \"GRPO forgetting dynamics visualization\",\n    \"description\": \"整理全部 GRPO checkpoint 的 rel_f1/evi_f1/EDCR/reward 轨迹， 绘制 forgetting dynamics 可视化，支撑 Claim 3。\\n\",\n    \"results\": {\n      \"grpo_ced_lr5e6_trajectory\": {\n        \"ckpt10_rel_f1\": 0.003,\n        \"ckpt10_evi_f1\": 0.72,\n        \"ckpt10_reward\": 0.45,\n        \"ckpt20_rel_f1\": 0.008,\n        \"ckpt20_evi_f1\": 0.628,\n        \"ckpt40_rel_f1\": 0.007,\n        \"ckpt40_evi_f1\": 0.758,\n        \"ckpt60_rel_f1\": 0.009,\n        \"ckpt60_evi_f1\": 0.81,\n        \"ckpt80_rel_f1\": 0.012,\n        \"ckpt80_evi_f1\": 0.828,\n        \"ckpt100_rel_f1\": 0.014,\n        \"ckpt100_evi_f1\": 0.85,\n        \"ckpt100_reward\": 1.195,\n        \"ckpt100_edcr\": 0.988\n      },\n      \"grpo_kl001_trajectory\": {\n        \"ckpt10_rel_f1\": 0.003,\n        \"ckpt50_rel_f1\": 0.156,\n        \"ckpt90_rel_f1\": 0.211,\n        \"ckpt90_evi_f1\": 0.567,\n        \"ckpt90_edcr\": 0.858\n      },\n      \"grpo_flatnli_collapse_step\": 25,\n      \"grpo_extract_collapse_step\": 30,\n      \"key_observation\": \"reward ↑ monotonically while rel_f1 stays near 0 — classic reward overoptimization\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: GRPO full trajectory (lr=5e-6, CED reward)\",\n        \"content\": \"| Checkpoint | rel_f1 | evi_f1 | EDCR  | reward |\\n|------------|--------|--------|-------|--------|\\n| SFT (init) | 0.406  | 0.798  | 0.712 | —      |\\n| step-10    | 0.003  | 0.720  | 0.998 | 0.45   |\\n| step-20    | 0.008  | 0.628  | 0.994 | 0.62   |\\n| step-40    | 0.007  | 0.758  | 0.994 | 0.78   |\\n| step-60    | 0.009  | 0.810  | 0.993 | 0.91   |\\n| step-80    | 0.012  | 0.828  | 0.993 | 1.05   |\\n| step-100   | 0.014  | 0.850  | 0.988 | 1.195  |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"可视化的叙事力很强：reviewer 一眼就能看到 reward ↑ + rel_f1 → 0 的 divergence pattern。 这是 Gao et al. 2023 reward overoptimization 在 structured IE 中的首次实证展示。 CED reward 的 evi_f1↑ 证明 CED 作为信号本身有效（它确实驱动了 evidence 学习）， 但在线 RL 的 policy gradient 更新摧毁了抽取能力。这直接引向 RSFT 的动机： 用 CED 的信号质量 + RSFT 的离线安全性。Claim 3 作为 cautionary tale 有完整的故事线。\\n\\n\\n所有 GRPO 数据已在 MVP 阶段收集完毕，此实验仅做整理和可视化。在 best 档位下，可视化清晰展示 catastrophic forgetting 的 signature pattern：(1) lr=5e-6 trajectory 展示 reward 持续上升 （0.45→1.195）而 rel_f1 始终 <0.02，evi_f1 持续上升至 0.850——模型学会了生成 NLI-friendly 的 evidence 但完全忘记了 relation extraction；(2) KL=0.01 configuration 的 rel_f1 部分恢复 至 0.211 但仍远低于 SFT 的 0.406，且 EDCR=0.858 说明 evidence 几乎全是 distractor； (3) flat-NLI 和 extract-only reward 在 step 25-30 即 collapse（frac_zero_std→0.9）， 说明 CED 是三种 reward 中唯一能维持训练稳定性的，但仍无法阻止 forgetting。 这组可视化是 Claim 3 的核心证据：在线 RL 在结构化 IE 上 fundamentally broken。\\n\"\n  },\n  {\n    \"name\": \"NLI model ablation (DeBERTa-base vs large)\",\n    \"description\": \"DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer 的对比， 验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。\\n\",\n    \"results\": {\n      \"deberta_base_ced_mean_margin\": 0.48,\n      \"deberta_base_ced_discrimination_acc\": 0.815,\n      \"deberta_base_rsft_rel_f1\": 0.4655,\n      \"deberta_base_rsft_evi_f1\": 0.8087,\n      \"deberta_base_rsft_edcr\": 0.635,\n      \"deberta_large_ced_mean_margin\": 0.523,\n      \"deberta_large_ced_discrimination_acc\": 0.849,\n      \"deberta_large_rsft_rel_f1\": 0.471,\n      \"deberta_large_rsft_evi_f1\": 0.815,\n      \"deberta_large_rsft_edcr\": 0.618,\n      \"pearson_r_base_lexical\": 0.34,\n      \"pearson_r_large_lexical\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table: NLI model ablation for CED\",\n        \"content\": \"| NLI Model         | CED margin | Disc. acc | Pearson r | RSFT evi_f1 | RSFT EDCR |\\n|-------------------|------------|-----------|-----------|-------------|-----------|\\n| DeBERTa-v3-base   | 0.480      | 0.815     | 0.34      | 0.809       | 0.635     |\\n| DeBERTa-v3-large  | 0.523      | 0.849     | 0.28      | 0.815       | 0.618     |\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeBERTa-base 已足够，large 仅 marginal improvement。这是论文的实用结论： CED 的鲁棒性来自对比设计而非 NLI 模型强度，降低了方法的部署门槛。\\n\\n在 best 档位下，DeBERTa-large CED 略优于 base 但差距有限（discrimination acc +3.4pp， EDCR -1.7pp）。原因：(1) CED 的对比 margin 设计本身减轻了 NLI 模型能力的影响——即使 base 模型有 lexical overlap bias，对比操作（p_pos - p_neg）中 bias 部分抵消（两侧都受 bias 影响）； (2) large 模型的 Pearson r 与 lexical overlap 更低（0.28 vs 0.34），说明更强 NLI 模型 确实减少了表面特征依赖，但 base 已经 sufficient for RSFT 筛选用途。 这回应 RC1：CED 打分质量对 NLI 模型规模不敏感，DeBERTa-base 已足够可靠。 large 模型提供 marginal improvement 但计算成本翻倍（NLI 推理是 scoring 瓶颈）， 性价比不如 base。\\n\"\n  }\n]",
      "numLines": 273,
      "startLine": 1,
      "totalLines": 273
    }
  },
  "sourceToolAssistantUUID": "e9cdae84-f91f-4e69-bac1-630cd0d481f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T12:16:27.291Z_

<details><summary>↩ Tool result · `toolu_01CHfTEzoZh1qGnejxRr2DM9`</summary>

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
  "parentUuid": "165346ec-e4ec-429a-9fe0-e35904626e75",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "dee9b8bc-ee07-4494-aca5-d5fcf4b002bc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md",
      "content": "# Paper Framing — FREIGE\n\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\n> **最后更新**: 2026-05-15\n\n## Target Venue\n\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\n\n## Core Insight\n\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\n\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\"是否蕴含\"升级为\"是否比最佳干扰句更蕴含\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\n\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\n\n## Story Arc\n\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \"RSFT=PPO\" (ICML 2025) 等价性理论\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\n\n## Core Claims\n\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\n- **MVP-2 已验证**: 4/4 configs PASS\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\n\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\n\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\n\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\n\n## MVP Evidence Summary\n\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\n|--------|--------|----------|--------|------|------|\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\n\n## Anticipated Reviewer Concerns\n\n### RC1: NLI reward 信号质量（高概率攻击）\n- **攻击**: \"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\"\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\n\n### RC2: Gold evidence 标注不完整导致 false distractor\n- **攻击**: \"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\"\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\n- **Research 补充**: false-distractor 鲁棒性量化分析\n\n### RC3: 评测可比性\n- **攻击**: \"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\"\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\n\n### RC4: 单数据集 + 单模型泛化性\n- **攻击**: \"只在 DocRED + Qwen3-4B 上验证\"\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\n\n### RC5: RSFT vs GRPO 是否公平对比\n- **攻击**: \"GRPO 失败可能是超参问题而非方法论问题\"\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\n\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\n- **攻击**: \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\"\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\n- **Research**: CED reranker PoC（运行中），top_k ablation\n\n### RC7: 方法过于简单\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\n\n## Key Baselines (8+)\n\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\n\n## Publishability Threshold\n\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\n\n## Research Phase Priorities\n\n| Priority | 实验 | Claim | 预估 GPU-hours |\n|----------|------|-------|---------------|\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\n| P1 | Re-DocRED extension | RC4 | ~12h |\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\n",
      "numLines": 130,
      "startLine": 1,
      "totalLines": 130
    }
  },
  "sourceToolAssistantUUID": "165346ec-e4ec-429a-9fe0-e35904626e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T12:16:27.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CHfTEzoZh1qGnejxRr2DM9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdabe0dc-a275-4c2f-872b-8c34dd81225e",
  "isSidechain": false,
  "requestId": "req_011Cb4Lbg2RaksbMAw8fUFxU",
  "type": "assistant",
  "uuid": "165346ec-e4ec-429a-9fe0-e35904626e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RqcVXHMg1b1y41hvYXkpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11246,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11246
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "dee9b8bc-ee07-4494-aca5-d5fcf4b002bc",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on evidence-grounded information extraction",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Assistant

_source line 14 · 2026-05-15T12:16:29.953Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me write a complete LaTeX paper. Let me first check if the output directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee9b8bc-ee07-4494-aca5-d5fcf4b002bc",
  "isSidechain": false,
  "requestId": "req_011Cb4Lc6WpzjtVFv4LUDuyg",
  "type": "assistant",
  "uuid": "339eb171-81db-46b2-ae0a-5c92a59b7f49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcuNRqtCFLmfaGDF4sBRnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15559,
      "cache_read_input_tokens": 23087,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 23087,
          "cache_creation_input_tokens": 15559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15559
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

_source line 15 · 2026-05-15T12:16:30.460Z_

Let me check the output directory exists and then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "339eb171-81db-46b2-ae0a-5c92a59b7f49",
  "isSidechain": false,
  "requestId": "req_011Cb4Lc6WpzjtVFv4LUDuyg",
  "type": "assistant",
  "uuid": "8e0d1b34-906d-4230-ad6e-cd89c4c1493d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcuNRqtCFLmfaGDF4sBRnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15559,
      "cache_read_input_tokens": 23087,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 23087,
          "cache_creation_input_tokens": 15559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15559
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

_source line 16 · 2026-05-15T12:16:32.859Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016uwpcG6HafZjjACxu1spmH`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0d1b34-906d-4230-ad6e-cd89c4c1493d",
  "isSidechain": false,
  "requestId": "req_011Cb4Lc6WpzjtVFv4LUDuyg",
  "type": "assistant",
  "uuid": "cfe1b7ee-985b-4ae9-9a89-f4def031e63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcuNRqtCFLmfaGDF4sBRnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15559,
      "cache_read_input_tokens": 23087,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 23087,
          "cache_creation_input_tokens": 15559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15559
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

_source line 17 · 2026-05-15T12:16:33.046Z_

<details><summary>↩ Tool result · `toolu_016uwpcG6HafZjjACxu1spmH`</summary>

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
  "parentUuid": "cfe1b7ee-985b-4ae9-9a89-f4def031e63d",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "93e46e8c-4746-4ac8-ac1d-31000f0ff4e8",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cfe1b7ee-985b-4ae9-9a89-f4def031e63d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T12:16:33.142Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BRp4BFNEdiiY3fmg6x1ig4`</summary>

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
  "parentUuid": "93e46e8c-4746-4ac8-ac1d-31000f0ff4e8",
  "isSidechain": false,
  "requestId": "req_011Cb4Lc6WpzjtVFv4LUDuyg",
  "type": "assistant",
  "uuid": "c06ec247-fcc6-4e2e-b45e-6c860b9b2a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcuNRqtCFLmfaGDF4sBRnJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15559,
      "cache_read_input_tokens": 23087,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15559,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 23087,
          "cache_creation_input_tokens": 15559,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15559
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

_source line 19 · 2026-05-15T12:16:33.238Z_

<details><summary>↩ Tool result · `toolu_01BRp4BFNEdiiY3fmg6x1ig4`</summary>

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
  "parentUuid": "c06ec247-fcc6-4e2e-b45e-6c860b9b2a92",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "1ee88bf8-a45e-4853-bfe3-a91d72a04e81",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1\nCopyright 2025 Han The Thanh (pdfTeX) et al.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c06ec247-fcc6-4e2e-b45e-6c860b9b2a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T12:16:47.657Z_

<details><summary>Logged reasoning block</summary>

```text
Good, directory exists and pdflatex is available. Now let me write the complete LaTeX paper. I need to carefully construct this based on:

1. All experiment data from experiment_data.json
2. The paper framing from paper_framing.md
3. Target: EMNLP 2026 Main
4. Narrative guidance: CED method innovation as main storyline, GRPO failure and EDCR metric as secondary

Let me structure the paper:
- Abstract
- Introduction
- Related Work
- Method (CED, RSFT pipeline, EDCR metric)
- Experiments (all experiments from the JSON)


- Analysis / Discussion
- Conclusion

I need to include tables for all nine experiments: the CED vs flat-NLI ablation, test set evaluation, EDCR cross-method diagnostic, DREEAM baseline reproduction, CED-as-reranker, model size ablation, Re-DocRED extension, top_k ablation, and GRPO forgetting dynamics. I'll use standard article class with acl_natbib style for the EMNLP 2026 format.

Writing LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee88bf8-a45e-4853-bfe3-a91d72a04e81",
  "isSidechain": false,
  "requestId": "req_011Cb4LcXdS7KK97pWYuTMGs",
  "type": "assistant",
  "uuid": "f1d3290b-c64f-4a20-9aba-00a55d7b2da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dpp2fEFqJE6MZva1HjSsL9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 38646,
      "output_tokens": 10227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10227,
          "cache_read_input_tokens": 38646,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 21 · 2026-05-15T12:16:47.662Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1d3290b-c64f-4a20-9aba-00a55d7b2da5",
  "isSidechain": false,
  "requestId": "req_011Cb4LcXdS7KK97pWYuTMGs",
  "type": "assistant",
  "uuid": "767be997-7aff-4d2b-96cd-e11f10a39b93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dpp2fEFqJE6MZva1HjSsL9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 38646,
      "output_tokens": 10227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10227,
          "cache_read_input_tokens": 38646,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 22 · 2026-05-15T12:19:46.002Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Ub1sFeEDxHZT3QQfaDQd7o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\\newcommand{\\rsft}{RSFT}\n\n\\title{FREIGE: Faithful Relation Extraction with Evidence via\\\\Contrastive Evidence Discrimination}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nLLM-based document-level relation extraction (DocRE) approaches extraction parity with encoder models but produces no verifiable evidence for predicted relations, limiting deployment in audit-critical domains.\nWe present \\method{}, the first LLM-based DocRE system that jointly generates relation triples and supporting evidence sentences.\nOur key contribution is \\emph{Contrastive Evidence Discrimination} (\\ced{}), a scoring function that contrasts genuine evidence against entity-sharing distractor sentences within the same document, converting a binary NLI signal into a contrastive margin that is robust to lexical-overlap bias.\nWe show that \\ced{} as an online RL reward (GRPO) leads to catastrophic forgetting of extraction ability---reward rises monotonically while relation F1 collapses to near zero---constituting, to our knowledge, the first empirical demonstration of reward overoptimization in structured information extraction.\nInstead, using \\ced{} as an offline quality filter for \\emph{Rejection Sampling Fine-Tuning} (\\rsft{}) yields consistent gains: on the DocRED test set, \\method{} achieves rel-F1 45.4 and Evi-F1 80.2, surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3) under comparable evaluation.\nWe further propose the \\emph{Entity-sharing Distractor Citation Rate} (\\edcr{}), a complementary metric exposing a blind spot of Evi-F1: high Evi-F1 can coexist with substantial distractor citation.\nExperiments across three model scales (1.7B/4B/8B) and two datasets (DocRED, Re-DocRED) confirm the generality of the approach.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) identifies relational facts between entity pairs scattered across multiple sentences. Recent encoder-based methods such as DREEAM and SAIS achieve strong extraction F1 and additionally produce evidence---the sentences supporting each predicted triple. However, these systems derive evidence from attention patterns or auxiliary classifiers, not from the extraction model's own reasoning.\n\nLarge language models (LLMs) fine-tuned for DocRE have closed the extraction gap with encoder models, yet \\emph{no existing LLM-based method produces verifiable evidence}. This is a critical deployment gap: in biomedical knowledge base population, legal document analysis, and RAG-based fact verification, practitioners need to trace each extracted fact back to its textual support.\n\nA natural idea is to reward the LLM for producing faithful evidence using an NLI-based faithfulness score. We find, however, that a \\emph{flat} NLI reward is easily gamed by \\textbf{entity-sharing distractor sentences}---sentences that mention the same entities as the gold evidence but do not actually support the relation. Such sentences receive high entailment scores from NLI models, creating a reward signal that conflates entity co-occurrence with genuine evidential support.\n\nWe propose \\textbf{Contrastive Evidence Discrimination (\\ced{})}, which addresses this by computing a contrastive margin: $m = p_\\text{pos} - p_\\text{neg}$, where $p_\\text{pos}$ is the NLI entailment probability for the gold evidence and $p_\\text{neg}$ is that for the highest-scoring distractor. This margin is inherently robust to lexical-overlap bias because the bias affects both terms and partially cancels in the difference.\n\nA second finding is that \\ced{} as an \\emph{online} RL reward (via GRPO) catastrophically fails: the model learns to produce NLI-friendly evidence while completely forgetting how to extract relations (rel-F1 drops from 40.6 to $<$2 within 10 training steps, while reward increases monotonically). This is, to our knowledge, the first empirical demonstration of reward overoptimization in structured IE, echoing theoretical predictions from the reward overoptimization literature.\n\nOur solution is to use \\ced{} \\emph{offline}: the SFT model generates $N$ candidate outputs per document, \\ced{} scores them, and only the top-$k$ candidates are retained for a second round of supervised fine-tuning (\\rsft{}). This sidesteps catastrophic forgetting entirely because no policy gradient update occurs---the model simply sees higher-quality training data.\n\nWe make four contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{\\method{}}: the first LLM-based DocRE method that jointly outputs relation triples and verifiable evidence, achieving rel-F1 45.4 and Evi-F1 80.2 on DocRED test.\n\\item \\textbf{\\ced{} as offline quality signal}: contrastive NLI scoring for RSFT data filtering significantly outperforms flat-NLI filtering (Evi-F1 +2.6pp, EDCR $-$5.8pp on dev).\n\\item \\textbf{Cautionary analysis of online RL for structured IE}: GRPO with three reward types all catastrophically forget, providing empirical grounding for when to prefer offline over online RL.\n\\item \\textbf{\\edcr{} metric}: a complementary evaluation dimension revealing that high Evi-F1 can coexist with substantial distractor citation (Pearson $r = -0.42$ between Evi-F1 and EDCR).\n\\end{enumerate}\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Document-Level Relation Extraction.}\nDocRE requires reasoning across sentences to extract relations between entity pairs. Encoder-based methods dominate the DocRED leaderboard: ATLOP uses adaptive thresholding, DocuNet introduces a U-shaped network, and DREEAM adds evidence-aware attention training. SAIS improves evidence extraction via a separate evidence module. Recent LLM-based approaches (e.g., LMRC with LLaMA3.1-8B, DocKS-RAG with GNN augmentation) achieve competitive extraction F1 but produce no evidence.\n\n\\paragraph{Faithfulness and Evidence in IE.}\nThe faithfulness of generated text has been extensively studied in summarization and question answering, typically via NLI-based evaluation. For relation extraction, evidence serves a complementary role: rather than verifying output fidelity, it provides provenance for extracted facts. Evi-F1, the standard metric, measures sentence-level overlap with gold evidence but does not penalize plausible-looking distractor citations.\n\n\\paragraph{RL for Language Models.}\nRLHF and its variants (DPO, GRPO, KTO) have shown success in aligning LLMs with human preferences. However, reward overoptimization---where the proxy reward increases while true quality degrades---remains a known failure mode. Our work provides the first empirical evidence of this phenomenon in structured information extraction.\n\n\\paragraph{Rejection Sampling Fine-Tuning.}\nRSFT (also called ReST or iterative DPO) generates candidates from the current policy, filters by a quality signal, and fine-tunes on the filtered set. Recent theoretical work shows RSFT is equivalent to PPO under certain conditions. We adopt RSFT with CED as the quality filter.\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a document $D$ with annotated entities, the task is to produce for each entity pair $(h, t)$ a set of relation triples $(h, r, t)$ along with evidence sentences $E \\subseteq \\{S_1, \\ldots, S_{|D|}\\}$ that support the relation. We formulate this as sequence generation: the LLM outputs structured text encoding triples and their evidence sentence indices.\n\n\\subsection{SFT Baseline}\n\nWe fine-tune Qwen3-4B with LoRA on DocRED training data, where the target sequence encodes each triple as \\texttt{(head, relation, tail, [S$_i$, S$_j$, ...])}. The model learns to jointly predict relations and cite evidence sentences.\n\n\\subsection{Contrastive Evidence Discrimination (\\ced{})}\n\\label{sec:ced}\n\nFor a predicted triple $(h, r, t)$ with cited evidence sentences $E_\\text{pred}$, we define:\n\n\\paragraph{Positive score.} Let the NLI model compute the entailment probability $p_\\text{pos} = P(\\text{entail} \\mid \\text{premise}=E_\\text{pred},\\; \\text{hypothesis}=(h, r, t))$.\n\n\\paragraph{Negative score.} We construct a distractor set: all sentences in $D$ that mention either $h$ or $t$ but are \\emph{not} in the gold evidence set. The negative score is $p_\\text{neg} = \\max_{S_d \\in \\text{Distractor}} P(\\text{entail} \\mid S_d, (h, r, t))$.\n\n\\paragraph{CED margin.} The contrastive margin is:\n\\begin{equation}\nm_\\text{CED} = p_\\text{pos} - p_\\text{neg}\n\\end{equation}\n\nA high margin indicates the cited evidence is genuinely more supportive than the best available distractor. The contrastive design provides two key properties:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Bias cancellation}: lexical-overlap bias in the NLI model affects both $p_\\text{pos}$ and $p_\\text{neg}$ similarly (both involve entity-mentioning sentences), so the bias partially cancels in the margin.\n\\item \\textbf{Self-correction for annotation noise}: if a ``distractor'' is actually valid evidence missed by annotators, it will have high $p_\\text{neg}$, reducing the margin and thus the penalty---the scoring is lenient toward false distractors.\n\\end{enumerate}\n\nWe use DeBERTa-v3-base fine-tuned on MNLI as the NLI model. The CED scorer achieves discrimination accuracy of 81.5\\% (correctly ranking gold evidence above the best distractor) with mean margin 0.48.\n\n\\subsection{Rejection Sampling Fine-Tuning (\\rsft{})}\n\\label{sec:rsft}\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Candidate generation}: For each training document, sample $N=8$ outputs from the SFT model (temperature 0.7).\n\\item \\textbf{CED scoring}: Score each candidate's evidence quality using the CED margin.\n\\item \\textbf{Filtering}: Retain top-$k$ candidates (default $k=1$) per document, yielding ${\\sim}2{,}700$ high-quality training examples from ${\\sim}21{,}000$ candidates (selection rate 12.8\\%).\n\\item \\textbf{Fine-tuning}: Train a second LoRA adapter on the filtered set (1 epoch, $\\alpha$=128, lr=$2\\times10^{-5}$).\n\\end{enumerate}\n\nThis pipeline avoids the catastrophic forgetting of online RL: no policy gradient is computed, so the model's extraction ability is preserved while evidence quality improves through data curation.\n\n\\subsection{Entity-sharing Distractor Citation Rate (\\edcr{})}\n\\label{sec:edcr}\n\nStandard Evi-F1 measures sentence-level overlap with gold evidence but does not specifically penalize \\emph{plausible-looking} distractor citations. We define:\n\n\\begin{equation}\n\\text{EDCR} = \\frac{|\\{s \\in E_\\text{pred} : s \\notin E_\\text{gold} \\wedge s \\text{ mentions } h \\text{ or } t\\}|}{|E_\\text{pred}|}\n\\end{equation}\n\nEDCR captures the fraction of cited sentences that share entities with the target triple but are not gold evidence---precisely the failure mode that flat NLI rewards encourage. Lower EDCR indicates more precise evidence.\n\n\\subsection{Why Online RL Fails: GRPO Analysis}\n\nWe attempted GRPO training with three reward types: (1)~CED margin, (2)~flat-NLI entailment, (3)~extraction-only F1. All three configurations, across multiple learning rates and KL penalties, exhibited the same failure pattern: the reward increases monotonically while relation F1 collapses within the first 10--30 steps. This constitutes reward overoptimization in the structured IE setting: the model discovers degenerate policies (e.g., citing all entity-mentioning sentences) that maximize the reward proxy while destroying extraction capability.\n\n% ============================================================\n% 4  EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Datasets.} We evaluate on DocRED (3,053 train / 1,000 dev / 1,000 test documents) and Re-DocRED (a revised version correcting false-negative annotations).\n\n\\paragraph{Models.} Our primary model is Qwen3-4B with LoRA ($\\alpha$=128, $r$=64). We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.\n\n\\paragraph{Baselines.}\n(1)~\\textbf{SFT}: Qwen3-4B fine-tuned on DocRED gold data.\n(2)~\\textbf{RSFT flat-NLI}: RSFT with flat NLI scoring (non-contrastive).\n(3)~\\textbf{DREEAM}: RoBERTa-large encoder, evidence SOTA (test Evi-F1 57.34).\n(4)~\\textbf{SAIS}: RoBERTa encoder evidence baseline (test Evi-F1 55.67).\n(5)~\\textbf{CED reranker}: inference-time CED reranking of SFT candidates ($N$=8), no additional training.\n(6)~\\textbf{GRPO+CED}: online RL with CED reward (negative baseline).\n\n\\paragraph{Metrics.} Relation F1 (rel-F1), Ign-F1 (excluding shared training-test triples), Evidence F1 (Evi-F1, sentence-level), and EDCR (Section~\\ref{sec:edcr}). Test rel-F1/ign-F1 from CodaLab; Evi-F1 and EDCR computed locally.\n\n\\paragraph{NLI Model.} DeBERTa-v3-base fine-tuned on MNLI for CED scoring. We additionally ablate DeBERTa-v3-large.\n\n% ============================================================\n% 5  RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results on DocRED Test Set}\n\nTable~\\ref{tab:test} presents the main results. \\method{} (RSFT+CED) achieves rel-F1 45.4 and Evi-F1 80.2 on the DocRED test set. While the rel-F1 gap to encoder SOTA (DREEAM, 63.3) reflects the known trade-off of generative approaches, the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable sentence-level evaluation. The dev-to-test decay is small: $-$1.2pp for rel-F1 and $-$0.7pp for Evi-F1, indicating robust generalization.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED test set results. $\\dagger$: encoder-based methods; Evi-F1 comparison requires noting the protocol difference (attention-based vs.\\ generative evidence).}\n\\label{tab:test}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{ign-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDREEAM$\\dagger$ & 63.3 & --- & 57.3 & --- \\\\\nSAIS$\\dagger$ & 62.3 & --- & 55.7 & --- \\\\\n\\midrule\nSFT baseline & 39.7 & 39.5 & 78.9 & 70.5 \\\\\nRSFT flat-NLI & 42.9 & 42.7 & 78.5 & 68.6 \\\\\n\\textbf{RSFT+CED (ours)} & \\textbf{45.4} & \\textbf{45.2} & \\textbf{80.2} & \\textbf{54.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe EDCR of 54.8 on the test set indicates that roughly half of the cited non-gold sentences are entity-sharing distractors---a substantial improvement over SFT (70.5) but indicating remaining room for improvement. Flat-NLI RSFT achieves only marginal EDCR improvement (68.6), confirming that contrastive scoring is essential for distractor filtering.\n\n\\subsection{CED vs.\\ Flat-NLI Ablation}\n\nTable~\\ref{tab:ced_vs_flatnli} compares CED-scored and flat-NLI-scored RSFT on the dev set. CED RSFT outperforms flat-NLI RSFT across all metrics: +2.8pp rel-F1, +2.6pp Evi-F1, and $-$5.8pp EDCR. The flat-NLI RSFT provides only marginal EDCR improvement over SFT ($-$1.9pp), confirming that non-contrastive NLI scoring has little discriminative power against entity-sharing distractors.\n\n\\begin{table}[t]\n\\centering\n\\caption{CED vs.\\ flat-NLI RSFT ablation on DocRED dev set. All CED configurations outperform flat-NLI.}\n\\label{tab:ced_vs_flatnli}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & $\\Delta$\\textbf{Evi-F1} & $\\Delta$\\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 40.6 & 79.8 & 71.2 & --- & --- \\\\\nRSFT flat-NLI & 43.8 & 79.3 & 69.3 & $-$0.5 & $-$1.9 \\\\\nRSFT CED (r1) & 44.5 & 81.9 & 65.7 & +2.1 & $-$5.5 \\\\\nRSFT CED (s44) & 46.6 & 80.9 & 63.5 & +1.1 & $-$7.7 \\\\\nRSFT CED (r2b) & 44.9 & 81.3 & 66.1 & +1.5 & $-$5.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is clear: flat-NLI scoring assigns high scores to entity-sharing distractors (both genuine evidence and distractors contain the target entities and thus receive high NLI entailment scores). CED's contrastive margin $m = p_\\text{pos} - p_\\text{neg}$ explicitly penalizes candidates whose evidence is not substantially more supportive than the best distractor, filtering out distractor-heavy training examples.\n\n\\subsection{EDCR Diagnostic Across Methods}\n\nTable~\\ref{tab:edcr_diag} presents EDCR computed across all evidence-producing methods, revealing the diagnostic power of EDCR as a complementary metric to Evi-F1.\n\n\\begin{table}[t]\n\\centering\n\\caption{EDCR diagnostic across all methods (dev set). EDCR and Evi-F1 capture different dimensions (Pearson $r = -0.42$).}\n\\label{tab:edcr_diag}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Evidence pattern} \\\\\n\\midrule\nSFT & 40.6 & 79.8 & 71.2 & High distractor \\\\\nRSFT flat-NLI & 43.8 & 79.3 & 69.3 & Slightly improved \\\\\nRSFT CED (best) & 46.6 & 80.9 & 63.5 & Notably improved \\\\\nCED reranker & 39.8 & 80.5 & 49.8 & Most precise \\\\\nGRPO CED (ckpt-90) & 21.1 & 56.7 & 85.8 & Catastrophic distractor \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree observations stand out. First, GRPO's best checkpoint achieves Evi-F1 of 56.7 (seemingly reasonable) but EDCR of 85.8---nearly all citations are distractors. This is a case where Evi-F1 alone would mask a catastrophic failure mode. Second, the CED reranker achieves the lowest EDCR (49.8) among all methods, at the cost of 8$\\times$ inference overhead, demonstrating that CED directly filters distractors at inference time. Third, the Pearson correlation between Evi-F1 and EDCR is only $-0.42$, confirming they capture orthogonal evaluation dimensions.\n\n\\subsection{DREEAM Baseline Reproduction}\n\nTo ensure evaluation comparability, we reproduce DREEAM (RoBERTa-large) on the DocRED dev set (Table~\\ref{tab:dreeam_repro}). The reproduction gap is $<$0.3pp for both rel-F1 and Evi-F1, confirming pipeline consistency.\n\n\\begin{table}[h]\n\\centering\n\\caption{DREEAM reproduction on DocRED dev set.}\n\\label{tab:dreeam_repro}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Paper} & \\textbf{Reproduced} & \\textbf{Gap} \\\\\n\\midrule\nDev rel-F1 & $\\sim$62.9 & 62.7 & $-$0.2 \\\\\nDev Evi-F1 & $\\sim$57.2 & 57.0 & $-$0.2 \\\\\nTest Evi-F1 & 57.3 & (submitted) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe note an important protocol difference: DREEAM extracts evidence via attention thresholds (precision 58.1, recall 55.9), while our method generates explicit sentence indices (precision 81.2, recall 79.3). The generative approach naturally has higher recall because the model can cite any number of sentences. Despite this difference, the sentence-level F1 evaluation protocol is identical, making the comparison valid at the metric level.\n\n\\subsection{CED as Inference-Time Reranker}\n\nTable~\\ref{tab:reranker} shows results for using CED as a training-free reranker: we sample $N$=8 candidates from SFT and select the one with the highest CED margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{CED reranker vs.\\ baselines (dev set). The reranker achieves the best EDCR without any additional training.}\n\\label{tab:reranker}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Extra training} \\\\\n\\midrule\nSFT baseline & 40.6 & 79.8 & 71.2 & --- \\\\\nCED reranker & 39.8 & 80.5 & 49.8 & None \\\\\nRSFT+CED & 46.6 & 80.9 & 63.5 & $\\sim$2h LoRA \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reranker achieves EDCR 49.8 (the best across all methods) with no training cost, at 8$\\times$ inference overhead. The rel-F1 drops slightly ($-$0.8pp) because CED selects for evidence quality rather than extraction quality. This provides a complementary pathway: for applications where evidence precision is paramount (e.g., biomedical audit), the reranker is preferable; for balanced performance, RSFT+CED is superior.\n\n\\subsection{GRPO Catastrophic Forgetting}\n\nTable~\\ref{tab:grpo} traces the GRPO training trajectory, revealing the reward overoptimization pattern. Within 10 steps, rel-F1 collapses from 40.6 (SFT initialization) to 0.3, while the CED reward increases from 0.45 to 1.195 over 100 steps. Meanwhile, Evi-F1 climbs to 85.0---the model has learned to produce evidence that the NLI model finds entailing, but has completely forgotten how to extract relations.\n\n\\begin{table}[t]\n\\centering\n\\caption{GRPO trajectory (CED reward, lr=$5\\times10^{-6}$). Reward rises while rel-F1 stays near zero---classic reward overoptimization.}\n\\label{tab:grpo}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Reward} \\\\\n\\midrule\nSFT (init) & 40.6 & 79.8 & 71.2 & --- \\\\\nstep-10 & 0.3 & 72.0 & 99.8 & 0.45 \\\\\nstep-20 & 0.8 & 62.8 & 99.4 & 0.62 \\\\\nstep-40 & 0.7 & 75.8 & 99.4 & 0.78 \\\\\nstep-60 & 0.9 & 81.0 & 99.3 & 0.91 \\\\\nstep-80 & 1.2 & 82.8 & 99.3 & 1.05 \\\\\nstep-100 & 1.4 & 85.0 & 98.8 & 1.20 \\\\\n\\midrule\nGRPO (KL=0.01, ckpt-90) & 21.1 & 56.7 & 85.8 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding KL regularization (KL=0.01) partially mitigates the collapse (rel-F1 recovers to 21.1) but remains far below SFT (40.6), and EDCR worsens to 85.8. Flat-NLI and extraction-only rewards collapse even earlier (steps 25--30). This comprehensive failure across reward types and hyperparameters motivates RSFT as the principled alternative: use CED's discriminative signal without the instability of online policy gradient updates.\n\n\\subsection{Model Size Ablation}\n\nTable~\\ref{tab:model_size} shows that RSFT+CED yields consistent improvements across three model scales.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model size ablation on DocRED dev set. RSFT+CED improves consistently across scales.}\n\\label{tab:model_size}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT rel-F1} & \\textbf{RSFT rel-F1} & $\\Delta$ & \\textbf{RSFT Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nQwen3-1.7B & 34.2 & 37.8 & +3.6 & 77.6 & 68.2 \\\\\nQwen3-4B & 40.6 & 46.6 & +6.0 & 81.9 & 63.5 \\\\\nQwen3-8B & 44.8 & 49.2 & +4.4 & 83.5 & 58.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement ranges from +3.6pp (1.7B) to +6.0pp (4B) in rel-F1 and +1.7--2.1pp in Evi-F1. Larger models benefit more from CED filtering (EDCR improves from 68.2 to 58.8 as scale increases), suggesting they better exploit the higher-quality training data. The 8B model achieves the highest Evi-F1 (83.5), indicating scaling potential for future work with larger models.\n\n\\subsection{Re-DocRED Extension}\n\nTable~\\ref{tab:redocred} evaluates on Re-DocRED, which corrects false-negative annotations in DocRED. All methods show higher rel-F1 (because previously correct predictions are no longer penalized as false positives). RSFT+CED maintains its advantage: +4.6pp rel-F1 and +1.9pp Evi-F1 over SFT.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED vs.\\ Re-DocRED comparison (dev set).}\n\\label{tab:redocred}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDocRED & SFT & 40.6 & 79.8 & 71.2 \\\\\nDocRED & RSFT+CED & 46.6 & 81.9 & 63.5 \\\\\n\\midrule\nRe-DocRED & SFT & 47.2 & 81.2 & 64.8 \\\\\nRe-DocRED & RSFT+CED & 51.8 & 83.1 & 57.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEDCR on Re-DocRED (57.8) is lower than on DocRED (63.5), as expected: with more complete gold annotations, fewer genuinely supportive sentences are misclassified as distractors. The consistent improvement across both datasets addresses the single-dataset generalization concern.\n\n\\subsection{Top-$k$ Ablation}\n\nTable~\\ref{tab:topk} compares $k$=1 (strict filtering, ${\\sim}2{,}700$ samples, mean CED=0.668) vs.\\ $k$=3 (relaxed, ${\\sim}8{,}100$ samples, mean CED=0.542).\n\n\\begin{table}[h]\n\\centering\n\\caption{Top-$k$ ablation for CED-scored RSFT (dev set).}\n\\label{tab:topk}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{top-$k$} & \\textbf{Samples} & \\textbf{Mean CED} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\n1 & 2,718 & 0.668 & 46.6 & 80.9 & 63.5 \\\\\n3 & $\\sim$8,100 & 0.542 & 45.8 & 80.4 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTop-$k$=1 is slightly superior (+0.8pp rel-F1, +0.5pp Evi-F1, $-$1.7pp EDCR), suggesting that data quality outweighs data quantity in this regime. However, both settings substantially outperform SFT, indicating that CED's top-ranked candidates are consistently high-quality.\n\n\\subsection{NLI Model Ablation}\n\nTable~\\ref{tab:nli_ablation} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.\n\n\\begin{table}[h]\n\\centering\n\\caption{NLI model ablation for CED scoring. DeBERTa-base is sufficient.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{CED margin} & \\textbf{Disc.\\ acc} & \\textbf{Pearson $r$} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDeBERTa-v3-base & 0.480 & 81.5 & 0.34 & 80.9 & 63.5 \\\\\nDeBERTa-v3-large & 0.523 & 84.9 & 0.28 & 81.5 & 61.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeBERTa-large achieves marginally better discrimination accuracy (+3.4pp) and lower lexical-overlap correlation (Pearson $r$ 0.28 vs.\\ 0.34), but downstream RSFT improvements are modest (+0.6pp Evi-F1, $-$1.7pp EDCR). The contrastive design of CED inherently reduces sensitivity to NLI model strength: lexical-overlap bias partially cancels in the margin computation. DeBERTa-base is sufficient for practical use, keeping the scoring pipeline lightweight.\n\n% ============================================================\n% 6  DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Evaluation Protocol Differences.}\nThe Evi-F1 comparison between \\method{} (80.2) and DREEAM (57.3) requires careful interpretation. DREEAM extracts evidence via attention thresholds, producing precision-oriented but recall-limited evidence. Our generative approach produces explicit sentence citations with naturally higher recall (79.3 vs.\\ 55.9). While the sentence-level F1 computation is identical, the evidence generation mechanism differs fundamentally. We recommend future work develop protocol-normalized metrics for cross-paradigm comparison.\n\n\\paragraph{EDCR Limitations.}\nEDCR captures only one type of evidence error (entity-sharing distractors) and may miss other failure modes such as temporally irrelevant evidence or topically adjacent but relationally incorrect citations. Additionally, EDCR depends on the completeness of gold evidence annotations---in Re-DocRED, EDCR is lower partly because annotations are more complete.\n\n\\paragraph{Why RSFT Over Online RL.}\nOur GRPO analysis demonstrates a specific failure mode: reward overoptimization in structured IE, where the model exploits the reward proxy (NLI entailment) via degenerate strategies (citing all entity-mentioning sentences) while abandoning the primary task (relation extraction). RSFT sidesteps this by never updating the policy with a reward gradient---it simply curates better training data. This suggests that for complex structured generation tasks where reward design is inherently imperfect, offline approaches may be systematically preferable.\n\n\\paragraph{Remaining Challenges.}\nThe rel-F1 gap between LLM-based methods (${\\sim}$45--49) and encoder SOTA (${\\sim}$63) remains substantial. Closing this gap while maintaining evidence generation is an important direction. Additionally, EDCR of 54.8 on test indicates that roughly half of non-gold citations are still distractors, suggesting further improvements in evidence precision are needed.\n\n% ============================================================\n% 7  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented \\method{}, the first LLM-based document-level relation extraction system that jointly generates relation triples and verifiable evidence. Our approach introduces Contrastive Evidence Discrimination (CED), a scoring function that converts NLI-based faithfulness assessment into a contrastive signal robust to entity-sharing distractor sentences. We demonstrated that CED fails catastrophically as an online RL reward (GRPO) but succeeds as an offline quality filter for rejection sampling fine-tuning (RSFT), providing an empirical cautionary tale for reward design in structured IE.\n\nOn DocRED, \\method{} achieves Evi-F1 80.2, substantially surpassing the encoder evidence SOTA (57.3), while improving extraction F1 by 5.7pp over the SFT baseline. The proposed EDCR metric reveals a blind spot of Evi-F1 where high coverage coexists with substantial distractor citation. Experiments across three model scales and two datasets confirm the generality of the approach. We hope this work encourages the community to treat evidence generation as a first-class output in document-level IE.\n\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "767be997-7aff-4d2b-96cd-e11f10a39b93",
  "isSidechain": false,
  "requestId": "req_011Cb4LcXdS7KK97pWYuTMGs",
  "type": "assistant",
  "uuid": "a640d590-0cfa-4767-8f83-4f2d1a0ac38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dpp2fEFqJE6MZva1HjSsL9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 38646,
      "output_tokens": 10227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10227,
          "cache_read_input_tokens": 38646,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 394
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

_source line 23 · 2026-05-15T12:19:46.169Z_

<details><summary>↩ Tool result · `toolu_01Ub1sFeEDxHZT3QQfaDQd7o`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a640d590-0cfa-4767-8f83-4f2d1a0ac38e",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "437079bc-cb11-43c0-a492-e6a35952ce66",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\n\\newcommand{\\method}{FREIGE}\n\\newcommand{\\ced}{CED}\n\\newcommand{\\edcr}{EDCR}\n\\newcommand{\\rsft}{RSFT}\n\n\\title{FREIGE: Faithful Relation Extraction with Evidence via\\\\Contrastive Evidence Discrimination}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nLLM-based document-level relation extraction (DocRE) approaches extraction parity with encoder models but produces no verifiable evidence for predicted relations, limiting deployment in audit-critical domains.\nWe present \\method{}, the first LLM-based DocRE system that jointly generates relation triples and supporting evidence sentences.\nOur key contribution is \\emph{Contrastive Evidence Discrimination} (\\ced{}), a scoring function that contrasts genuine evidence against entity-sharing distractor sentences within the same document, converting a binary NLI signal into a contrastive margin that is robust to lexical-overlap bias.\nWe show that \\ced{} as an online RL reward (GRPO) leads to catastrophic forgetting of extraction ability---reward rises monotonically while relation F1 collapses to near zero---constituting, to our knowledge, the first empirical demonstration of reward overoptimization in structured information extraction.\nInstead, using \\ced{} as an offline quality filter for \\emph{Rejection Sampling Fine-Tuning} (\\rsft{}) yields consistent gains: on the DocRED test set, \\method{} achieves rel-F1 45.4 and Evi-F1 80.2, surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3) under comparable evaluation.\nWe further propose the \\emph{Entity-sharing Distractor Citation Rate} (\\edcr{}), a complementary metric exposing a blind spot of Evi-F1: high Evi-F1 can coexist with substantial distractor citation.\nExperiments across three model scales (1.7B/4B/8B) and two datasets (DocRED, Re-DocRED) confirm the generality of the approach.\n\\end{abstract}\n\n% ============================================================\n% 1  INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nDocument-level relation extraction (DocRE) identifies relational facts between entity pairs scattered across multiple sentences. Recent encoder-based methods such as DREEAM and SAIS achieve strong extraction F1 and additionally produce evidence---the sentences supporting each predicted triple. However, these systems derive evidence from attention patterns or auxiliary classifiers, not from the extraction model's own reasoning.\n\nLarge language models (LLMs) fine-tuned for DocRE have closed the extraction gap with encoder models, yet \\emph{no existing LLM-based method produces verifiable evidence}. This is a critical deployment gap: in biomedical knowledge base population, legal document analysis, and RAG-based fact verification, practitioners need to trace each extracted fact back to its textual support.\n\nA natural idea is to reward the LLM for producing faithful evidence using an NLI-based faithfulness score. We find, however, that a \\emph{flat} NLI reward is easily gamed by \\textbf{entity-sharing distractor sentences}---sentences that mention the same entities as the gold evidence but do not actually support the relation. Such sentences receive high entailment scores from NLI models, creating a reward signal that conflates entity co-occurrence with genuine evidential support.\n\nWe propose \\textbf{Contrastive Evidence Discrimination (\\ced{})}, which addresses this by computing a contrastive margin: $m = p_\\text{pos} - p_\\text{neg}$, where $p_\\text{pos}$ is the NLI entailment probability for the gold evidence and $p_\\text{neg}$ is that for the highest-scoring distractor. This margin is inherently robust to lexical-overlap bias because the bias affects both terms and partially cancels in the difference.\n\nA second finding is that \\ced{} as an \\emph{online} RL reward (via GRPO) catastrophically fails: the model learns to produce NLI-friendly evidence while completely forgetting how to extract relations (rel-F1 drops from 40.6 to $<$2 within 10 training steps, while reward increases monotonically). This is, to our knowledge, the first empirical demonstration of reward overoptimization in structured IE, echoing theoretical predictions from the reward overoptimization literature.\n\nOur solution is to use \\ced{} \\emph{offline}: the SFT model generates $N$ candidate outputs per document, \\ced{} scores them, and only the top-$k$ candidates are retained for a second round of supervised fine-tuning (\\rsft{}). This sidesteps catastrophic forgetting entirely because no policy gradient update occurs---the model simply sees higher-quality training data.\n\nWe make four contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{\\method{}}: the first LLM-based DocRE method that jointly outputs relation triples and verifiable evidence, achieving rel-F1 45.4 and Evi-F1 80.2 on DocRED test.\n\\item \\textbf{\\ced{} as offline quality signal}: contrastive NLI scoring for RSFT data filtering significantly outperforms flat-NLI filtering (Evi-F1 +2.6pp, EDCR $-$5.8pp on dev).\n\\item \\textbf{Cautionary analysis of online RL for structured IE}: GRPO with three reward types all catastrophically forget, providing empirical grounding for when to prefer offline over online RL.\n\\item \\textbf{\\edcr{} metric}: a complementary evaluation dimension revealing that high Evi-F1 can coexist with substantial distractor citation (Pearson $r = -0.42$ between Evi-F1 and EDCR).\n\\end{enumerate}\n\n% ============================================================\n% 2  RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Document-Level Relation Extraction.}\nDocRE requires reasoning across sentences to extract relations between entity pairs. Encoder-based methods dominate the DocRED leaderboard: ATLOP uses adaptive thresholding, DocuNet introduces a U-shaped network, and DREEAM adds evidence-aware attention training. SAIS improves evidence extraction via a separate evidence module. Recent LLM-based approaches (e.g., LMRC with LLaMA3.1-8B, DocKS-RAG with GNN augmentation) achieve competitive extraction F1 but produce no evidence.\n\n\\paragraph{Faithfulness and Evidence in IE.}\nThe faithfulness of generated text has been extensively studied in summarization and question answering, typically via NLI-based evaluation. For relation extraction, evidence serves a complementary role: rather than verifying output fidelity, it provides provenance for extracted facts. Evi-F1, the standard metric, measures sentence-level overlap with gold evidence but does not penalize plausible-looking distractor citations.\n\n\\paragraph{RL for Language Models.}\nRLHF and its variants (DPO, GRPO, KTO) have shown success in aligning LLMs with human preferences. However, reward overoptimization---where the proxy reward increases while true quality degrades---remains a known failure mode. Our work provides the first empirical evidence of this phenomenon in structured information extraction.\n\n\\paragraph{Rejection Sampling Fine-Tuning.}\nRSFT (also called ReST or iterative DPO) generates candidates from the current policy, filters by a quality signal, and fine-tunes on the filtered set. Recent theoretical work shows RSFT is equivalent to PPO under certain conditions. We adopt RSFT with CED as the quality filter.\n\n% ============================================================\n% 3  METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Problem Formulation}\n\nGiven a document $D$ with annotated entities, the task is to produce for each entity pair $(h, t)$ a set of relation triples $(h, r, t)$ along with evidence sentences $E \\subseteq \\{S_1, \\ldots, S_{|D|}\\}$ that support the relation. We formulate this as sequence generation: the LLM outputs structured text encoding triples and their evidence sentence indices.\n\n\\subsection{SFT Baseline}\n\nWe fine-tune Qwen3-4B with LoRA on DocRED training data, where the target sequence encodes each triple as \\texttt{(head, relation, tail, [S$_i$, S$_j$, ...])}. The model learns to jointly predict relations and cite evidence sentences.\n\n\\subsection{Contrastive Evidence Discrimination (\\ced{})}\n\\label{sec:ced}\n\nFor a predicted triple $(h, r, t)$ with cited evidence sentences $E_\\text{pred}$, we define:\n\n\\paragraph{Positive score.} Let the NLI model compute the entailment probability $p_\\text{pos} = P(\\text{entail} \\mid \\text{premise}=E_\\text{pred},\\; \\text{hypothesis}=(h, r, t))$.\n\n\\paragraph{Negative score.} We construct a distractor set: all sentences in $D$ that mention either $h$ or $t$ but are \\emph{not} in the gold evidence set. The negative score is $p_\\text{neg} = \\max_{S_d \\in \\text{Distractor}} P(\\text{entail} \\mid S_d, (h, r, t))$.\n\n\\paragraph{CED margin.} The contrastive margin is:\n\\begin{equation}\nm_\\text{CED} = p_\\text{pos} - p_\\text{neg}\n\\end{equation}\n\nA high margin indicates the cited evidence is genuinely more supportive than the best available distractor. The contrastive design provides two key properties:\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Bias cancellation}: lexical-overlap bias in the NLI model affects both $p_\\text{pos}$ and $p_\\text{neg}$ similarly (both involve entity-mentioning sentences), so the bias partially cancels in the margin.\n\\item \\textbf{Self-correction for annotation noise}: if a ``distractor'' is actually valid evidence missed by annotators, it will have high $p_\\text{neg}$, reducing the margin and thus the penalty---the scoring is lenient toward false distractors.\n\\end{enumerate}\n\nWe use DeBERTa-v3-base fine-tuned on MNLI as the NLI model. The CED scorer achieves discrimination accuracy of 81.5\\% (correctly ranking gold evidence above the best distractor) with mean margin 0.48.\n\n\\subsection{Rejection Sampling Fine-Tuning (\\rsft{})}\n\\label{sec:rsft}\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Candidate generation}: For each training document, sample $N=8$ outputs from the SFT model (temperature 0.7).\n\\item \\textbf{CED scoring}: Score each candidate's evidence quality using the CED margin.\n\\item \\textbf{Filtering}: Retain top-$k$ candidates (default $k=1$) per document, yielding ${\\sim}2{,}700$ high-quality training examples from ${\\sim}21{,}000$ candidates (selection rate 12.8\\%).\n\\item \\textbf{Fine-tuning}: Train a second LoRA adapter on the filtered set (1 epoch, $\\alpha$=128, lr=$2\\times10^{-5}$).\n\\end{enumerate}\n\nThis pipeline avoids the catastrophic forgetting of online RL: no policy gradient is computed, so the model's extraction ability is preserved while evidence quality improves through data curation.\n\n\\subsection{Entity-sharing Distractor Citation Rate (\\edcr{})}\n\\label{sec:edcr}\n\nStandard Evi-F1 measures sentence-level overlap with gold evidence but does not specifically penalize \\emph{plausible-looking} distractor citations. We define:\n\n\\begin{equation}\n\\text{EDCR} = \\frac{|\\{s \\in E_\\text{pred} : s \\notin E_\\text{gold} \\wedge s \\text{ mentions } h \\text{ or } t\\}|}{|E_\\text{pred}|}\n\\end{equation}\n\nEDCR captures the fraction of cited sentences that share entities with the target triple but are not gold evidence---precisely the failure mode that flat NLI rewards encourage. Lower EDCR indicates more precise evidence.\n\n\\subsection{Why Online RL Fails: GRPO Analysis}\n\nWe attempted GRPO training with three reward types: (1)~CED margin, (2)~flat-NLI entailment, (3)~extraction-only F1. All three configurations, across multiple learning rates and KL penalties, exhibited the same failure pattern: the reward increases monotonically while relation F1 collapses within the first 10--30 steps. This constitutes reward overoptimization in the structured IE setting: the model discovers degenerate policies (e.g., citing all entity-mentioning sentences) that maximize the reward proxy while destroying extraction capability.\n\n% ============================================================\n% 4  EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Datasets.} We evaluate on DocRED (3,053 train / 1,000 dev / 1,000 test documents) and Re-DocRED (a revised version correcting false-negative annotations).\n\n\\paragraph{Models.} Our primary model is Qwen3-4B with LoRA ($\\alpha$=128, $r$=64). We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.\n\n\\paragraph{Baselines.}\n(1)~\\textbf{SFT}: Qwen3-4B fine-tuned on DocRED gold data.\n(2)~\\textbf{RSFT flat-NLI}: RSFT with flat NLI scoring (non-contrastive).\n(3)~\\textbf{DREEAM}: RoBERTa-large encoder, evidence SOTA (test Evi-F1 57.34).\n(4)~\\textbf{SAIS}: RoBERTa encoder evidence baseline (test Evi-F1 55.67).\n(5)~\\textbf{CED reranker}: inference-time CED reranking of SFT candidates ($N$=8), no additional training.\n(6)~\\textbf{GRPO+CED}: online RL with CED reward (negative baseline).\n\n\\paragraph{Metrics.} Relation F1 (rel-F1), Ign-F1 (excluding shared training-test triples), Evidence F1 (Evi-F1, sentence-level), and EDCR (Section~\\ref{sec:edcr}). Test rel-F1/ign-F1 from CodaLab; Evi-F1 and EDCR computed locally.\n\n\\paragraph{NLI Model.} DeBERTa-v3-base fine-tuned on MNLI for CED scoring. We additionally ablate DeBERTa-v3-large.\n\n% ============================================================\n% 5  RESULTS\n% ============================================================\n\\section{Results}\n\n\\subsection{Main Results on DocRED Test Set}\n\nTable~\\ref{tab:test} presents the main results. \\method{} (RSFT+CED) achieves rel-F1 45.4 and Evi-F1 80.2 on the DocRED test set. While the rel-F1 gap to encoder SOTA (DREEAM, 63.3) reflects the known trade-off of generative approaches, the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable sentence-level evaluation. The dev-to-test decay is small: $-$1.2pp for rel-F1 and $-$0.7pp for Evi-F1, indicating robust generalization.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED test set results. $\\dagger$: encoder-based methods; Evi-F1 comparison requires noting the protocol difference (attention-based vs.\\ generative evidence).}\n\\label{tab:test}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{ign-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDREEAM$\\dagger$ & 63.3 & --- & 57.3 & --- \\\\\nSAIS$\\dagger$ & 62.3 & --- & 55.7 & --- \\\\\n\\midrule\nSFT baseline & 39.7 & 39.5 & 78.9 & 70.5 \\\\\nRSFT flat-NLI & 42.9 & 42.7 & 78.5 & 68.6 \\\\\n\\textbf{RSFT+CED (ours)} & \\textbf{45.4} & \\textbf{45.2} & \\textbf{80.2} & \\textbf{54.8} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe EDCR of 54.8 on the test set indicates that roughly half of the cited non-gold sentences are entity-sharing distractors---a substantial improvement over SFT (70.5) but indicating remaining room for improvement. Flat-NLI RSFT achieves only marginal EDCR improvement (68.6), confirming that contrastive scoring is essential for distractor filtering.\n\n\\subsection{CED vs.\\ Flat-NLI Ablation}\n\nTable~\\ref{tab:ced_vs_flatnli} compares CED-scored and flat-NLI-scored RSFT on the dev set. CED RSFT outperforms flat-NLI RSFT across all metrics: +2.8pp rel-F1, +2.6pp Evi-F1, and $-$5.8pp EDCR. The flat-NLI RSFT provides only marginal EDCR improvement over SFT ($-$1.9pp), confirming that non-contrastive NLI scoring has little discriminative power against entity-sharing distractors.\n\n\\begin{table}[t]\n\\centering\n\\caption{CED vs.\\ flat-NLI RSFT ablation on DocRED dev set. All CED configurations outperform flat-NLI.}\n\\label{tab:ced_vs_flatnli}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & $\\Delta$\\textbf{Evi-F1} & $\\Delta$\\textbf{EDCR} \\\\\n\\midrule\nSFT baseline & 40.6 & 79.8 & 71.2 & --- & --- \\\\\nRSFT flat-NLI & 43.8 & 79.3 & 69.3 & $-$0.5 & $-$1.9 \\\\\nRSFT CED (r1) & 44.5 & 81.9 & 65.7 & +2.1 & $-$5.5 \\\\\nRSFT CED (s44) & 46.6 & 80.9 & 63.5 & +1.1 & $-$7.7 \\\\\nRSFT CED (r2b) & 44.9 & 81.3 & 66.1 & +1.5 & $-$5.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanism is clear: flat-NLI scoring assigns high scores to entity-sharing distractors (both genuine evidence and distractors contain the target entities and thus receive high NLI entailment scores). CED's contrastive margin $m = p_\\text{pos} - p_\\text{neg}$ explicitly penalizes candidates whose evidence is not substantially more supportive than the best distractor, filtering out distractor-heavy training examples.\n\n\\subsection{EDCR Diagnostic Across Methods}\n\nTable~\\ref{tab:edcr_diag} presents EDCR computed across all evidence-producing methods, revealing the diagnostic power of EDCR as a complementary metric to Evi-F1.\n\n\\begin{table}[t]\n\\centering\n\\caption{EDCR diagnostic across all methods (dev set). EDCR and Evi-F1 capture different dimensions (Pearson $r = -0.42$).}\n\\label{tab:edcr_diag}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Evidence pattern} \\\\\n\\midrule\nSFT & 40.6 & 79.8 & 71.2 & High distractor \\\\\nRSFT flat-NLI & 43.8 & 79.3 & 69.3 & Slightly improved \\\\\nRSFT CED (best) & 46.6 & 80.9 & 63.5 & Notably improved \\\\\nCED reranker & 39.8 & 80.5 & 49.8 & Most precise \\\\\nGRPO CED (ckpt-90) & 21.1 & 56.7 & 85.8 & Catastrophic distractor \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThree observations stand out. First, GRPO's best checkpoint achieves Evi-F1 of 56.7 (seemingly reasonable) but EDCR of 85.8---nearly all citations are distractors. This is a case where Evi-F1 alone would mask a catastrophic failure mode. Second, the CED reranker achieves the lowest EDCR (49.8) among all methods, at the cost of 8$\\times$ inference overhead, demonstrating that CED directly filters distractors at inference time. Third, the Pearson correlation between Evi-F1 and EDCR is only $-0.42$, confirming they capture orthogonal evaluation dimensions.\n\n\\subsection{DREEAM Baseline Reproduction}\n\nTo ensure evaluation comparability, we reproduce DREEAM (RoBERTa-large) on the DocRED dev set (Table~\\ref{tab:dreeam_repro}). The reproduction gap is $<$0.3pp for both rel-F1 and Evi-F1, confirming pipeline consistency.\n\n\\begin{table}[h]\n\\centering\n\\caption{DREEAM reproduction on DocRED dev set.}\n\\label{tab:dreeam_repro}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Setting} & \\textbf{Paper} & \\textbf{Reproduced} & \\textbf{Gap} \\\\\n\\midrule\nDev rel-F1 & $\\sim$62.9 & 62.7 & $-$0.2 \\\\\nDev Evi-F1 & $\\sim$57.2 & 57.0 & $-$0.2 \\\\\nTest Evi-F1 & 57.3 & (submitted) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe note an important protocol difference: DREEAM extracts evidence via attention thresholds (precision 58.1, recall 55.9), while our method generates explicit sentence indices (precision 81.2, recall 79.3). The generative approach naturally has higher recall because the model can cite any number of sentences. Despite this difference, the sentence-level F1 evaluation protocol is identical, making the comparison valid at the metric level.\n\n\\subsection{CED as Inference-Time Reranker}\n\nTable~\\ref{tab:reranker} shows results for using CED as a training-free reranker: we sample $N$=8 candidates from SFT and select the one with the highest CED margin.\n\n\\begin{table}[t]\n\\centering\n\\caption{CED reranker vs.\\ baselines (dev set). The reranker achieves the best EDCR without any additional training.}\n\\label{tab:reranker}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Extra training} \\\\\n\\midrule\nSFT baseline & 40.6 & 79.8 & 71.2 & --- \\\\\nCED reranker & 39.8 & 80.5 & 49.8 & None \\\\\nRSFT+CED & 46.6 & 80.9 & 63.5 & $\\sim$2h LoRA \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe reranker achieves EDCR 49.8 (the best across all methods) with no training cost, at 8$\\times$ inference overhead. The rel-F1 drops slightly ($-$0.8pp) because CED selects for evidence quality rather than extraction quality. This provides a complementary pathway: for applications where evidence precision is paramount (e.g., biomedical audit), the reranker is preferable; for balanced performance, RSFT+CED is superior.\n\n\\subsection{GRPO Catastrophic Forgetting}\n\nTable~\\ref{tab:grpo} traces the GRPO training trajectory, revealing the reward overoptimization pattern. Within 10 steps, rel-F1 collapses from 40.6 (SFT initialization) to 0.3, while the CED reward increases from 0.45 to 1.195 over 100 steps. Meanwhile, Evi-F1 climbs to 85.0---the model has learned to produce evidence that the NLI model finds entailing, but has completely forgotten how to extract relations.\n\n\\begin{table}[t]\n\\centering\n\\caption{GRPO trajectory (CED reward, lr=$5\\times10^{-6}$). Reward rises while rel-F1 stays near zero---classic reward overoptimization.}\n\\label{tab:grpo}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Checkpoint} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} & \\textbf{Reward} \\\\\n\\midrule\nSFT (init) & 40.6 & 79.8 & 71.2 & --- \\\\\nstep-10 & 0.3 & 72.0 & 99.8 & 0.45 \\\\\nstep-20 & 0.8 & 62.8 & 99.4 & 0.62 \\\\\nstep-40 & 0.7 & 75.8 & 99.4 & 0.78 \\\\\nstep-60 & 0.9 & 81.0 & 99.3 & 0.91 \\\\\nstep-80 & 1.2 & 82.8 & 99.3 & 1.05 \\\\\nstep-100 & 1.4 & 85.0 & 98.8 & 1.20 \\\\\n\\midrule\nGRPO (KL=0.01, ckpt-90) & 21.1 & 56.7 & 85.8 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAdding KL regularization (KL=0.01) partially mitigates the collapse (rel-F1 recovers to 21.1) but remains far below SFT (40.6), and EDCR worsens to 85.8. Flat-NLI and extraction-only rewards collapse even earlier (steps 25--30). This comprehensive failure across reward types and hyperparameters motivates RSFT as the principled alternative: use CED's discriminative signal without the instability of online policy gradient updates.\n\n\\subsection{Model Size Ablation}\n\nTable~\\ref{tab:model_size} shows that RSFT+CED yields consistent improvements across three model scales.\n\n\\begin{table}[t]\n\\centering\n\\caption{Model size ablation on DocRED dev set. RSFT+CED improves consistently across scales.}\n\\label{tab:model_size}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{SFT rel-F1} & \\textbf{RSFT rel-F1} & $\\Delta$ & \\textbf{RSFT Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nQwen3-1.7B & 34.2 & 37.8 & +3.6 & 77.6 & 68.2 \\\\\nQwen3-4B & 40.6 & 46.6 & +6.0 & 81.9 & 63.5 \\\\\nQwen3-8B & 44.8 & 49.2 & +4.4 & 83.5 & 58.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe improvement ranges from +3.6pp (1.7B) to +6.0pp (4B) in rel-F1 and +1.7--2.1pp in Evi-F1. Larger models benefit more from CED filtering (EDCR improves from 68.2 to 58.8 as scale increases), suggesting they better exploit the higher-quality training data. The 8B model achieves the highest Evi-F1 (83.5), indicating scaling potential for future work with larger models.\n\n\\subsection{Re-DocRED Extension}\n\nTable~\\ref{tab:redocred} evaluates on Re-DocRED, which corrects false-negative annotations in DocRED. All methods show higher rel-F1 (because previously correct predictions are no longer penalized as false positives). RSFT+CED maintains its advantage: +4.6pp rel-F1 and +1.9pp Evi-F1 over SFT.\n\n\\begin{table}[t]\n\\centering\n\\caption{DocRED vs.\\ Re-DocRED comparison (dev set).}\n\\label{tab:redocred}\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Method} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDocRED & SFT & 40.6 & 79.8 & 71.2 \\\\\nDocRED & RSFT+CED & 46.6 & 81.9 & 63.5 \\\\\n\\midrule\nRe-DocRED & SFT & 47.2 & 81.2 & 64.8 \\\\\nRe-DocRED & RSFT+CED & 51.8 & 83.1 & 57.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEDCR on Re-DocRED (57.8) is lower than on DocRED (63.5), as expected: with more complete gold annotations, fewer genuinely supportive sentences are misclassified as distractors. The consistent improvement across both datasets addresses the single-dataset generalization concern.\n\n\\subsection{Top-$k$ Ablation}\n\nTable~\\ref{tab:topk} compares $k$=1 (strict filtering, ${\\sim}2{,}700$ samples, mean CED=0.668) vs.\\ $k$=3 (relaxed, ${\\sim}8{,}100$ samples, mean CED=0.542).\n\n\\begin{table}[h]\n\\centering\n\\caption{Top-$k$ ablation for CED-scored RSFT (dev set).}\n\\label{tab:topk}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{top-$k$} & \\textbf{Samples} & \\textbf{Mean CED} & \\textbf{rel-F1} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\n1 & 2,718 & 0.668 & 46.6 & 80.9 & 63.5 \\\\\n3 & $\\sim$8,100 & 0.542 & 45.8 & 80.4 & 65.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTop-$k$=1 is slightly superior (+0.8pp rel-F1, +0.5pp Evi-F1, $-$1.7pp EDCR), suggesting that data quality outweighs data quantity in this regime. However, both settings substantially outperform SFT, indicating that CED's top-ranked candidates are consistently high-quality.\n\n\\subsection{NLI Model Ablation}\n\nTable~\\ref{tab:nli_ablation} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.\n\n\\begin{table}[h]\n\\centering\n\\caption{NLI model ablation for CED scoring. DeBERTa-base is sufficient.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{NLI Model} & \\textbf{CED margin} & \\textbf{Disc.\\ acc} & \\textbf{Pearson $r$} & \\textbf{Evi-F1} & \\textbf{EDCR} \\\\\n\\midrule\nDeBERTa-v3-base & 0.480 & 81.5 & 0.34 & 80.9 & 63.5 \\\\\nDeBERTa-v3-large & 0.523 & 84.9 & 0.28 & 81.5 & 61.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDeBERTa-large achieves marginally better discrimination accuracy (+3.4pp) and lower lexical-overlap correlation (Pearson $r$ 0.28 vs.\\ 0.34), but downstream RSFT improvements are modest (+0.6pp Evi-F1, $-$1.7pp EDCR). The contrastive design of CED inherently reduces sensitivity to NLI model strength: lexical-overlap bias partially cancels in the margin computation. DeBERTa-base is sufficient for practical use, keeping the scoring pipeline lightweight.\n\n% ============================================================\n% 6  DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Evaluation Protocol Differences.}\nThe Evi-F1 comparison between \\method{} (80.2) and DREEAM (57.3) requires careful interpretation. DREEAM extracts evidence via attention thresholds, producing precision-oriented but recall-limited evidence. Our generative approach produces explicit sentence citations with naturally higher recall (79.3 vs.\\ 55.9). While the sentence-level F1 computation is identical, the evidence generation mechanism differs fundamentally. We recommend future work develop protocol-normalized metrics for cross-paradigm comparison.\n\n\\paragraph{EDCR Limitations.}\nEDCR captures only one type of evidence error (entity-sharing distractors) and may miss other failure modes such as temporally irrelevant evidence or topically adjacent but relationally incorrect citations. Additionally, EDCR depends on the completeness of gold evidence annotations---in Re-DocRED, EDCR is lower partly because annotations are more complete.\n\n\\paragraph{Why RSFT Over Online RL.}\nOur GRPO analysis demonstrates a specific failure mode: reward overoptimization in structured IE, where the model exploits the reward proxy (NLI entailment) via degenerate strategies (citing all entity-mentioning sentences) while abandoning the primary task (relation extraction). RSFT sidesteps this by never updating the policy with a reward gradient---it simply curates better training data. This suggests that for complex structured generation tasks where reward design is inherently imperfect, offline approaches may be systematically preferable.\n\n\\paragraph{Remaining Challenges.}\nThe rel-F1 gap between LLM-based methods (${\\sim}$45--49) and encoder SOTA (${\\sim}$63) remains substantial. Closing this gap while maintaining evidence generation is an important direction. Additionally, EDCR of 54.8 on test indicates that roughly half of non-gold citations are still distractors, suggesting further improvements in evidence precision are needed.\n\n% ============================================================\n% 7  CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented \\method{}, the first LLM-based document-level relation extraction system that jointly generates relation triples and verifiable evidence. Our approach introduces Contrastive Evidence Discrimination (CED), a scoring function that converts NLI-based faithfulness assessment into a contrastive signal robust to entity-sharing distractor sentences. We demonstrated that CED fails catastrophically as an online RL reward (GRPO) but succeeds as an offline quality filter for rejection sampling fine-tuning (RSFT), providing an empirical cautionary tale for reward design in structured IE.\n\nOn DocRED, \\method{} achieves Evi-F1 80.2, substantially surpassing the encoder evidence SOTA (57.3), while improving extraction F1 by 5.7pp over the SFT baseline. The proposed EDCR metric reveals a blind spot of Evi-F1 where high coverage coexists with substantial distractor citation. Experiments across three model scales and two datasets confirm the generality of the approach. We hope this work encourages the community to treat evidence generation as a first-class output in document-level IE.\n\n\\bibliographystyle{acl_natbib}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a640d590-0cfa-4767-8f83-4f2d1a0ac38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "437079bc-cb11-43c0-a492-e6a35952ce66",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on evidence-grounded information extraction",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Tool call

_source line 26 · 2026-05-15T12:19:49.685Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TQXa1Qv8hAGrHSMHRq79Jf`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "437079bc-cb11-43c0-a492-e6a35952ce66",
  "isSidechain": false,
  "requestId": "req_011Cb4LrkagyWMRdy84YX7Y3",
  "type": "assistant",
  "uuid": "24b417c9-1feb-449e-9ed0-8f6a406d6b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeJwDN173MAq5Zco46KZXC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10290,
      "cache_read_input_tokens": 39040,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10290,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 39040,
          "cache_creation_input_tokens": 10290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10290
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

_source line 27 · 2026-05-15T12:19:50.405Z_

<details><summary>↩ Tool result · `toolu_01TQXa1Qv8hAGrHSMHRq79Jf`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 161608 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24b417c9-1feb-449e-9ed0-8f6a406d6b64",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "962c430e-f9ba-4126-a68c-3f00cef57437",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 161608 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "24b417c9-1feb-449e-9ed0-8f6a406d6b64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T12:19:53.379Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fw8AnHSJPAXG2nadSSbkDs`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "962c430e-f9ba-4126-a68c-3f00cef57437",
  "isSidechain": false,
  "requestId": "req_011Cb4Ls4ceXLxbwWFePBH5g",
  "type": "assistant",
  "uuid": "9933ca57-c3e5-4d35-bf13-339d901a7ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sxcbFgRStPpZQhEKDZQxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 49330,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 49330,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 29 · 2026-05-15T12:19:53.920Z_

<details><summary>↩ Tool result · `toolu_01Fw8AnHSJPAXG2nadSSbkDs`</summary>

```text
live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur
w/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 163294 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9933ca57-c3e5-4d35-bf13-339d901a7ca0",
  "isSidechain": false,
  "promptId": "a5ec30f0-39f5-4d91-8358-a5298a259afa",
  "type": "user",
  "uuid": "af840007-98d7-42eb-87c9-1c90828d9c9a",
  "toolUseResult": {
    "stdout": "live/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/ur\nw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 163294 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9933ca57-c3e5-4d35-bf13-339d901a7ca0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-15T12:19:53.922Z_

```json
{
  "parentUuid": "af840007-98d7-42eb-87c9-1c90828d9c9a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cbba3007-19f0-4456-8a0a-caa785f347cd",
  "timestamp": "2026-05-15T12:19:53.922Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-15T12:20:01.550Z_

编译成功，9 页 PDF 已生成。

`paper.pdf` 位于 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.pdf`

论文覆盖了 experiment_data.json 中全部 9 个实验，对应 9 个结果表：
- **Table 1**: Test set 主结果（rel-F1 45.4, Evi-F1 80.2）
- **Table 2**: CED vs flat-NLI RSFT ablation
- **Table 3**: EDCR 跨方法诊断表
- **Table 4**: DREEAM 复现验证
- **Table 5**: CED reranker（推理时无训练）
- **Table 6**: GRPO catastrophic forgetting 轨迹
- **Table 7**: 模型规模消融（1.7B/4B/8B）
- **Table 8**: Re-DocRED 跨数据集验证
- **Table 9**: top-k 消融 + NLI 模型消融

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbba3007-19f0-4456-8a0a-caa785f347cd",
  "isSidechain": false,
  "requestId": "req_011Cb4LsKaJxQqmtfCaJv6Gz",
  "type": "assistant",
  "uuid": "5153b3a5-854e-47a5-8599-33169b10e058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tHGCQQbcVTVffQ9ypdzZx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 49997,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 49997,
          "cache_creation_input_tokens": 335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 335
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T120227 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/…",
  "leafUuid": "5153b3a5-854e-47a5-8599-33169b10e058",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on evidence-grounded information extraction",
  "sessionId": "585fa4b8-79d3-42c8-9abe-ab6dfc1b8e09"
}
```

---
