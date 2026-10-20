# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e.jsonl`
- **Structured JSON:** [`9c9bc2e4dd26f75cba8d.json`](../../sessions/9c/9c9bc2e4dd26f75cba8d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:57:58.321Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:57:58.321Z",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Main Conference\n- Narrative guidance：放弃 capability trap 作为 unifying framework。Reframe 为条件性研究： 'Conditions for Effective Test-Time Scaling in Structured IE'。 核心转向：不是 'selection universally fails'，而是 'selection fails under high-convergence regimes induced by aggressive fine-tuning, but succeeds when output diversity is preserved.' LP compression 仍成立（free-form ablation 证据不受影响）。 Instance degeneracy 从 'inevitable consequence of capability' 变为 'controllable artifact of training configuration'。 Paper 变 prescriptive：给出什么条件下可以/不可以用 multi-sample 策略。 标题改为 'When Does Multi-Sample Selection Help Structured IE? A Diagnostic Study of Output Convergence'。 仍冲 EMNLP Main——从 novel insight paper 转为 large-scale empirical study with actionable guidelines。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:57:58.324Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:57:58.324Z",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-16T09:57:58.345Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Main Conference
- Narrative guidance：放弃 capability trap 作为 unifying framework。Reframe 为条件性研究： 'Conditions for Effective Test-Time Scaling in Structured IE'。 核心转向：不是 'selection universally fails'，而是 'selection fails under high-convergence regimes induced by aggressive fine-tuning, but succeeds when output diversity is preserved.' LP compression 仍成立（free-form ablation 证据不受影响）。 Instance degeneracy 从 'inevitable consequence of capability' 变为 'controllable artifact of training configuration'。 Paper 变 prescriptive：给出什么条件下可以/不可以用 multi-sample 策略。 标题改为 'When Does Multi-Sample Selection Help Structured IE? A Diagnostic Study of Output Convergence'。 仍冲 EMNLP Main——从 novel insight paper 转为 large-scale empirical study with actionable guidelines。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "098ea8b1-6cf1-4165-8d6d-09d3f0d80cec",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:57:58.344Z_

```json
{
  "parentUuid": "098ea8b1-6cf1-4165-8d6d-09d3f0d80cec",
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
  "uuid": "b600d95b-45dc-4314-8684-63dd0d58ca76",
  "timestamp": "2026-05-16T09:57:58.344Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:57:58.344Z_

```json
{
  "parentUuid": "b600d95b-45dc-4314-8684-63dd0d58ca76",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5531013f-1aea-465d-b183-b592ad25852d",
  "timestamp": "2026-05-16T09:57:58.344Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 6 · 2026-05-16T09:58:00.591Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5531013f-1aea-465d-b183-b592ad25852d",
  "isSidechain": false,
  "requestId": "req_011Cb63rX6c1qFHkaQXGjsCM",
  "type": "assistant",
  "uuid": "ed4e0bf7-a3da-43ac-8e66-76375eee3c30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM2oowqHSB91Wt7LCDhj5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11301,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11301
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

_source line 7 · 2026-05-16T09:58:01.653Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GqkMJ2nPtQSXHfW84Q7sgV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed4e0bf7-a3da-43ac-8e66-76375eee3c30",
  "isSidechain": false,
  "requestId": "req_011Cb63rX6c1qFHkaQXGjsCM",
  "type": "assistant",
  "uuid": "a20e9056-1b8c-4fc2-bf25-1de99057b88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM2oowqHSB91Wt7LCDhj5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11301,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11301
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

_source line 8 · 2026-05-16T09:58:01.850Z_

<details open><summary>🔧 Tool call — Read · `toolu_013zN9huArANfRPtmHDveaRm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a20e9056-1b8c-4fc2-bf25-1de99057b88d",
  "isSidechain": false,
  "requestId": "req_011Cb63rX6c1qFHkaQXGjsCM",
  "type": "assistant",
  "uuid": "3cdc9f2f-07f7-4613-b0f8-f9c584e6b27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM2oowqHSB91Wt7LCDhj5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11301,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11301,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11301
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

_source line 9 · 2026-05-16T09:58:01.942Z_

<details><summary>↩ Tool result · `toolu_01GqkMJ2nPtQSXHfW84Q7sgV`</summary>

```text
1	[
2	  {
3	    "name": "exp-020: fewnerd_smoke",
4	    "description": "Few-NERD INTRA (coarse 8-type) smoke test: 1-epoch LoRA fine-tune on Qwen3-8B + N=8 pilot inference on 200 instances. 验证数据管线和模型可学性，Gate exp-021.\n",
5	    "results": {
6	      "n_instances": 200,
7	      "n_valid": 188,
8	      "n_gold_empty": 12,
9	      "parse_rate": 0.985,
10	      "parse_failures": 24,
11	      "N": 8,
12	      "T": 1.0,
13	      "seed": 42,
14	      "ner_greedy_f1": 0.718,
15	      "ner_oracle_f1": 0.828,
16	      "ner_headroom_pp": 11.0,
17	      "degeneracy_rate": 0.101,
18	      "sj_rho_full": 0.192,
19	      "fk_rho_full": 0.148,
20	      "lp_rho_full": 0.214,
21	      "vc_rho_full": 0.248,
22	      "em_rho_full": 0.175,
23	      "sj_auroc": 0.582,
24	      "lp_auroc": 0.604,
25	      "vc_auroc": 0.638,
26	      "em_auroc": 0.621,
27	      "lp_selection_f1": 0.74,
28	      "lp_selection_delta_pp": 2.2,
29	      "greedy_selection_ref": 0.718,
30	      "sample_f1_pct_zero": 5.3,
31	      "sample_f1_mean": 0.671,
32	      "sample_f1_std": 0.248,
33	      "fleiss_kappa_mean": 0.371,
34	      "soft_jaccard_mean": 0.612,
35	      "elapsed_minutes": 18,
36	      "train_loss_1epoch": 0.142,
37	      "eval_loss_1epoch": 0.128
38	    },
39	    "tables": [
40	      {
41	        "name": "Table S-smoke: Few-NERD Smoke Test QE Metrics (n=188, 1-epoch, N=8)",
42	        "columns": [
43	          "Signal",
44	          "rho_full",
45	          "AUROC",
46	          "tau"
47	        ],
48	        "rows": [
49	          [
50	            "VC",
51	            0.248,
52	            0.638,
53	            0.18
54	          ],
55	          [
56	            "LP",
57	            0.214,
58	            0.604,
59	            0.153
60	          ],
61	          [
62	            "SJ",
63	            0.192,
64	            0.582,
65	            0.139
66	          ],
67	          [
68	            "EM",
69	            0.175,
70	            0.621,
71	            0.125
72	          ],
73	          [
74	            "FK",
75	            0.148,
76	            0.555,
77	            0.108
78	          ]
79	        ]
80	      }
81	    ],
82	    "figures": [],
83	    "analysis": "Smoke test 成功验证数据管线和模型训练。关键早期信号： degeneracy rate (10.1%) 明显低于 capability trap 对 F1=0.718 的预测值 (~15-20%), 暗示 fine-tuning 配置（1 epoch, LoRA rank=16）而非 capability 驱动 degeneracy。 LP 在 QE 和 selection 上均优于 SJ，与 SciERC 模式不同—— 提示数据集特性对最优信号有影响。Gate 通过，进入 exp-021 full run。 注意 parse_rate 0.985 可接受，fine-tuned model 对 Few-NERD 格式适应良好。\n\n\n1-epoch fine-tune 不够充分训练，F1=0.718 低于 full run 预期（~0.78） 但已验证任务可学性。Degeneracy 10.1% 初步暗示 Few-NERD 不符合 capability trap 预测——按 capability trap 的 F1→degeneracy 单调关系， 0.718 F1 应对应 ~15-20% degeneracy（介于 SciERC 21% 和 WNUT 0% 之间）， 但实际更低。原因：(a) Few-NERD 每句平均 3-4 实体、多词实体边界变异空间大； (b) 1-epoch 训练保留了预训练模型的高输出多样性，weight update 幅度小； (c) coarse 8-type 标签系统清晰，类型错误少但边界变异多。 SJ rho 仅 0.192 因 inter-sample 结构一致性弱——不同样本在多词实体 边界上产生变化，SJ 对此敏感但 F1 对此宽容。 LP rho 0.214 略优于 SJ，初步提示 LP 在低 degeneracy regime 下有效。 LP selection +2.2pp 是 directional positive，200 instances 样本量 不足以达到统计显著但方向明确。Smoke test 通过，gate exp-021.\n"
84	  },
85	  {
86	    "name": "exp-021: fewnerd_full",
87	    "description": "Few-NERD INTRA (coarse 8-type) full experiment: 3-epoch LoRA fine-tune + N=8 inference on full test set with 3 seeds [42, 123, 456]. Captures log-probs. 第三个 NER 数据集，Main Conference 必要条件.\n",
88	    "results": {
89	      "n_instances_total": 5218,
90	      "n_valid": 4506,
91	      "n_gold_empty": 712,
92	      "N": 8,
93	      "T": 1.0,
94	      "lora_rank": 16,
95	      "lora_alpha": 32,
96	      "epochs": 3,
97	      "train_final_loss": 0.058,
98	      "eval_loss": 0.072,
99	      "train_runtime_min": 95,
100	      "seed42_ner": {
101	        "greedy_f1": 0.782,
102	        "oracle_f1": 0.873,
103	        "headroom_pp": 9.1,
104	        "degeneracy_rate": 0.048,
105	        "sj_rho_full": 0.238,
106	        "fk_rho_full": 0.183,
107	        "lp_rho_full": 0.291,
108	        "vc_rho_full": 0.312,
109	        "em_rho_full": 0.228,
110	        "sj_auroc": 0.624,
111	        "fk_auroc": 0.588,
112	        "lp_auroc": 0.658,
113	        "vc_auroc": 0.681,
114	        "em_auroc": 0.718,
115	        "sj_tau": 0.172,
116	        "lp_tau": 0.211,
117	        "lp_selection_f1": 0.818,
118	        "vc_selection_f1": 0.805,
119	        "sj_selection_f1": 0.798,
120	        "fk_selection_f1": 0.793,
121	        "em_selection_f1": 0.795,
122	        "random_f1": 0.769,
123	        "sample_f1_pct_zero": 3.8,
124	        "tied_fraction_f1": 0.048,
125	        "lp_within_instance_range_median": 0.088
126	      },
127	      "seed123_ner": {
128	        "greedy_f1": 0.776,
129	        "oracle_f1": 0.868,
130	        "headroom_pp": 9.2,
131	        "degeneracy_rate": 0.055,
132	        "sj_rho_full": 0.208,
133	        "fk_rho_full": 0.165,
134	        "lp_rho_full": 0.271,
135	        "vc_rho_full": 0.285,
136	        "em_rho_full": 0.21,
137	        "lp_selection_f1": 0.808,
138	        "vc_selection_f1": 0.798,
139	        "sj_selection_f1": 0.791,
140	        "random_f1": 0.764,
141	        "sample_f1_pct_zero": 4.1,
142	        "lp_within_instance_range_median": 0.083
143	      },
144	      "seed456_ner": {
145	        "greedy_f1": 0.775,
146	        "oracle_f1": 0.865,
147	        "headroom_pp": 9.0,
148	        "degeneracy_rate": 0.058,
149	        "sj_rho_full": 0.203,
150	        "fk_rho_full": 0.17,
151	        "lp_rho_full": 0.262,
152	        "vc_rho_full": 0.289,
153	        "em_rho_full": 0.198,
154	        "lp_selection_f1": 0.805,
155	        "vc_selection_f1": 0.796,
156	        "sj_selection_f1": 0.789,
157	        "random_f1": 0.762,
158	        "sample_f1_pct_zero": 4.5,
159	        "lp_within_instance_range_median": 0.081
160	      },
161	      "mean_greedy_f1": 0.778,
162	      "mean_oracle_f1": 0.869,
163	      "mean_headroom_pp": 9.1,
164	      "mean_degeneracy_rate": 0.054,
165	      "sd_degeneracy_rate": 0.005,
166	      "mean_sj_rho_full": 0.216,
167	      "sd_sj_rho_full": 0.019,
168	      "mean_fk_rho_full": 0.173,
169	      "sd_fk_rho_full": 0.009,
170	      "mean_lp_rho_full": 0.275,
171	      "sd_lp_rho_full": 0.015,
172	      "mean_vc_rho_full": 0.295,
173	      "sd_vc_rho_full": 0.015,
174	      "mean_em_rho_full": 0.212,
175	      "sd_em_rho_full": 0.015,
176	      "mean_lp_selection_f1": 0.81,
177	      "mean_lp_selection_gap_pp": 3.2,
178	      "lp_selection_bootstrap_ci95": [
179	        0.004,
180	        0.06
181	      ],
182	      "lp_selection_bootstrap_p": 0.028,
183	      "lp_selection_cohen_d": 0.152,
184	      "mean_vc_selection_gap_pp": 2.1,
185	      "vc_selection_bootstrap_p": 0.065,
186	      "mean_sj_selection_gap_pp": 1.5,
187	      "sj_selection_bootstrap_p": 0.12,
188	      "mean_lp_within_instance_range_median": 0.084,
189	      "lp_range_ratio_vs_scierc": 2.05,
190	      "capability_trap_r2_3datasets": 0.98,
191	      "capability_trap_r2_4datasets_with_fewnerd": 0.51,
192	      "capability_trap_regression_residual_fewnerd_pp": 30.2
193	    },
194	    "tables": [
195	      {
196	        "name": "Table 5: Few-NERD QE Metrics (3-seed mean +/- SD, N=8, T=1.0, n=4506)",
197	        "columns": [
198	          "Signal",
199	          "rho_full",
200	          "SD",
201	          "AUROC",
202	          "tau",
203	          "Sel_F1",
204	          "Delta_greedy_pp",
205	          "p"
206	        ],
207	        "rows": [
208	          [
209	            "LP",
210	            0.275,
211	            0.015,
212	            0.658,
213	            0.211,
214	            0.81,
215	            "+3.2",
216	            "0.028*"
217	          ],
218	          [
219	            "VC",
220	            0.295,
221	            0.015,
222	            0.681,
223	            0.214,
224	            0.799,
225	            "+2.1",
226	            "0.065"
227	          ],
228	          [
229	            "SJ",
230	            0.216,
231	            0.019,
232	            0.624,
233	            0.172,
234	            0.793,
235	            "+1.5",
236	            "0.12"
237	          ],
238	          [
239	            "EM",
240	            0.212,
241	            0.015,
242	            0.718,
243	            0.153,
244	            0.793,
245	            "+1.5",
246	            "0.13"
247	          ],
248	          [
249	            "FK",
250	            0.173,
251	            0.009,
252	            0.588,
253	            0.125,
254	            0.79,
255	            "+1.2",
256	            "0.18"
257	          ],
258	          [
259	            "greedy",
260	            "---",
261	            "---",
262	            "---",
263	            "---",
264	            0.778,
265	            "---",
266	            "---"
267	          ],
268	          [
269	            "oracle",
270	            "---",
271	            "---",
272	            "---",
273	            "---",
274	            0.869,
275	            "+9.1",
276	            "---"
277	          ],
278	          [
279	            "random",
280	            "---",
281	            "---",
282	            "---",
283	            "---",
284	            0.765,
285	            "-1.3",
286	            "---"
287	          ]
288	        ]
289	      },
290	      {
291	        "name": "Table 6: Capability Trap — F1 vs Degeneracy Across 4 Datasets",
292	        "columns": [
293	          "Dataset",
294	          "greedy_F1",
295	          "degen_pct",
296	          "predicted_degen_pct",
297	          "residual_pp"
298	        ],
299	        "rows": [
300	          [
301	            "CoNLL-2003",
302	            0.912,
303	            58.0,
304	            "55-60",
305	            "~0"
306	          ],
307	          [
308	            "Few-NERD*",
309	            0.778,
310	            5.4,
311	            "35-40",
312	            "-30.2"
313	          ],
314	          [
315	            "SciERC",
316	            0.664,
317	            21.0,
318	            "20-25",
319	            "~0"
320	          ],
321	          [
322	            "WNUT-17",
323	            0.523,
324	            0.0,
325	            "0-5",
326	            "~0"
327	          ]
328	        ]
329	      },
330	      {
331	        "name": "Table 7: LP Compression Comparison Across Datasets",
332	        "columns": [
333	          "Dataset",
334	          "LP_range_median_nats",
335	          "degen_pct",
336	          "LP_sel_gap_pp",
337	          "LP_sel_p"
338	        ],
339	        "rows": [
340	          [
341	            "Few-NERD",
342	            0.084,
343	            5.4,
344	            "+3.2",
345	            0.028
346	          ],
347	          [
348	            "SciERC NER",
349	            0.041,
350	            21.0,
351	            "+0.6",
352	            0.39
353	          ],
354	          [
355	            "CoNLL NER",
356	            0.018,
357	            58.0,
358	            "-1.0",
359	            0.62
360	          ]
361	        ]
362	      }
363	    ],
364	    "figures": [],
365	    "analysis": "Few-NERD 实验产生三个核心 worst-tier 结论：\n(1) Capability trap 预测失败 (R² 0.98→0.51)。F1=0.778 + degen=5.4% 不在 F1→degeneracy 回归线上。Few-NERD 的残差 30.2pp 是压倒性的 反面证据。\"Capability drives degeneracy\" 被替换为 \"degeneracy is a joint function of fine-tuning intensity, entity density, and task structure.\"\n(2) Selection 在低 degeneracy regime 下有效。LP +3.2pp (p=0.028) 证明 \"universal failure\" 不成立。Selection 失败是 condition-dependent, not structural. 关键条件：degeneracy < 10% + LP range > 0.08 nats.\n(3) 最优信号依赖数据集。SciERC: SJ > LP. Few-NERD: LP > SJ. 不存在 universal best signal——进一步支持 conditional/prescriptive framing. Paper 需要给出 practitioners 决策指南：根据数据集的 degeneracy rate 和 LP compression degree 选择策略 (multi-sample vs greedy).\n\n\nFew-NERD 打破 capability trap 的 F1→degeneracy 单调预测： F1=0.778（高于 SciERC 0.664）但 degeneracy 仅 5.4% （远低于 SciERC 21%，更远低于 CoNLL 58%）。 按 capability trap 线性回归，F1=0.778 应预测 ~35-40% degeneracy。 实际偏差超过 30pp。\n低 degeneracy 的根因： (1) 实体密度高——Few-NERD INTRA 每实例平均 3.4 个实体（vs SciERC 2.1）， 更多实体意味着更多的组合变异空间。即使每个实体的 type 高度一致 （coarse 8-type 系统下类型错误极少），多词实体的边界变异 仍能产生不同的 entity sets——不同的 sets 有不同的 F1。 (2) 3-epoch LoRA（vs SciERC 5-epoch）对预训练权重修改幅度更小， 输出分布未被压缩至 mode collapse。 (3) 8 类粗粒度标签意味着类型空间简单， 模型不需要 overly specialize 就能达到高 F1，保留了 generation diversity。\nSelection 首次显著有效：LP +3.2pp (p=0.028, d=0.152)。 这是全研究中首个某信号显著优于 greedy 的结果。 LP 成功的原因：degeneracy 低 → LP 有真实 within-instance variance (median range 0.084 nats, 是 SciERC 0.041 的 2×) → LP 可区分好坏样本。 VC +2.1pp 接近显著 (p=0.065)。SJ +1.5pp 不显著 (p=0.12)—— SJ 的弱 rho (0.216) 限制了其 selection 能力。\nSJ rho 仅 0.216 的原因：coarse entity types 使得 SJ 的 type-aware matching 在多数实例上给出高分（类型一致）， 区分力来自边界差异——但边界差异与 F1 的对齐度弱。 LP 直接捕获 generation confidence，与 F1 的关联更强。 这是与 SciERC 的关键区别：SciERC 上 SJ > LP (rho 0.36 vs 0.21)， Few-NERD 上 LP > SJ (rho 0.275 vs 0.216)。 信号有效性取决于数据集特性，不存在 universal best signal。\nCapability trap R² 从 0.98 (3 datasets) 降至 0.51 (4 datasets)。 Few-NERD 是一个明确的 outlier，残差 30.2pp。 这迫使叙事从 \"capability drives degeneracy\" 转向 \"fine-tuning intensity and dataset properties drive degeneracy\"。\n"
366	  },
367	  {
368	    "name": "exp-022: 3rd_seed_scierc",
369	    "description": "SciERC NER+RE N=8 第三个 seed (seed=789). 强化 Fisher p-value power，测试 cross-seed stability.\n",
370	    "results": {
371	      "n_instances": 551,
372	      "n_valid_ner": 529,
373	      "n_valid_re": 397,
374	      "N": 8,
375	      "T": 1.0,
376	      "seed": 789,
377	      "parse_rate": 1.0,
378	      "ner_greedy_f1": 0.658,
379	      "ner_oracle_f1": 0.772,
380	      "ner_headroom_pp": 11.4,
381	      "ner_degeneracy_rate": 0.235,
382	      "ner_sj_rho_full": 0.285,
383	      "ner_fk_rho_full": 0.218,
384	      "ner_lp_rho_full": 0.228,
385	      "ner_vc_rho_full": 0.338,
386	      "ner_em_rho_full": 0.272,
387	      "ner_sj_rho_cond": 0.248,
388	      "ner_fk_rho_cond": 0.162,
389	      "ner_lp_rho_cond": 0.178,
390	      "ner_vc_rho_cond": 0.295,
391	      "ner_em_rho_cond": 0.345,
392	      "ner_sj_auroc": 0.648,
393	      "ner_fk_auroc": 0.598,
394	      "ner_lp_auroc": 0.578,
395	      "ner_vc_auroc": 0.662,
396	      "ner_em_auroc": 0.738,
397	      "ner_lp_selection_f1": 0.65,
398	      "ner_sj_selection_f1": 0.645,
399	      "ner_greedy_ref": 0.658,
400	      "ner_sample_f1_pct_zero": 13.2,
401	      "re_greedy_f1": 0.412,
402	      "re_oracle_f1": 0.582,
403	      "re_headroom_pp": 17.0,
404	      "re_sj_rho_full": 0.308,
405	      "re_fk_rho_full": 0.248,
406	      "re_lp_rho_full": 0.192,
407	      "re_vc_rho_full": 0.293,
408	      "re_em_rho_full": 0.198,
409	      "re_sj_rho_cond": 0.352,
410	      "re_lp_rho_cond": 0.022,
411	      "re_zero_f1_pct": 44.8,
412	      "three_seed_ner_sj_rho_values": [
413	        0.36,
414	        0.385,
415	        0.285
416	      ],
417	      "three_seed_ner_sj_rho_mean": 0.343,
418	      "three_seed_ner_sj_rho_sd": 0.053,
419	      "three_seed_ner_fk_rho_values": [
420	        0.267,
421	        0.29,
422	        0.218
423	      ],
424	      "three_seed_ner_fk_rho_mean": 0.258,
425	      "three_seed_ner_fk_rho_sd": 0.037,
426	      "three_seed_ner_lp_rho_values": [
427	        0.205,
428	        0.225,
429	        0.228
430	      ],
431	      "three_seed_ner_lp_rho_mean": 0.219,
432	      "three_seed_ner_lp_rho_sd": 0.013,
433	      "three_seed_ner_vc_rho_values": [
434	        0.379,
435	        0.395,
436	        0.338
437	      ],
438	      "three_seed_ner_vc_rho_mean": 0.371,
439	      "three_seed_ner_vc_rho_sd": 0.03,
440	      "three_seed_re_sj_rho_values": [
441	        0.25,
442	        0.283,
443	        0.308
444	      ],
445	      "three_seed_re_sj_rho_mean": 0.28,
446	      "three_seed_re_sj_rho_sd": 0.029,
447	      "three_seed_re_fk_rho_values": [
448	        0.275,
449	        0.317,
450	        0.248
451	      ],
452	      "three_seed_re_fk_rho_mean": 0.28,
453	      "three_seed_re_fk_rho_sd": 0.035,
454	      "three_seed_re_lp_rho_values": [
455	        0.266,
456	        0.29,
457	        0.192
458	      ],
459	      "three_seed_re_lp_rho_mean": 0.249,
460	      "three_seed_re_lp_rho_sd": 0.051,
461	      "three_seed_re_vc_rho_values": [
462	        0.35,
463	        0.32,
464	        0.293
465	      ],
466	      "three_seed_re_vc_rho_mean": 0.321,
467	      "three_seed_re_vc_rho_sd": 0.029,
468	      "re_ranking_seed42": "VC(0.350) > FK(0.275) > LP(0.266) > SJ(0.250) > EM(0.134)",
469	      "re_ranking_seed123": "FK(0.317) > LP(0.290) > SJ(0.283) > VC(0.320) > EM(0.170)",
470	      "re_ranking_seed789": "SJ(0.308) > VC(0.293) > FK(0.248) > EM(0.198) > LP(0.192)",
471	      "re_ranking_top1_consistent": false,
472	      "fisher_sj_gt_lp_ner_individual_p": [
473	        0.002,
474	        0.003,
475	        0.18
476	      ],
477	      "fisher_sj_gt_lp_ner_combined_p": 0.085,
478	      "fisher_sj_gt_fk_ner_combined_p": 0.032,
479	      "fisher_vc_gt_lp_ner_combined_p": 0.018,
480	      "fisher_structural_gt_surface_ner_combined_p": 0.042,
481	      "ner_sj_cv": 0.154,
482	      "ner_lp_cv": 0.059,
483	      "re_sj_cv": 0.104,
484	      "re_lp_cv": 0.205
485	    },
486	    "tables": [
487	      {
488	        "name": "Table 8: SciERC NER 3-Seed QE (N=8, T=1.0, n=529)",
489	        "columns": [
490	          "Seed",
491	          "SJ_rho",
492	          "FK_rho",
493	          "LP_rho",
494	          "VC_rho",
495	          "EM_rho"
496	        ],
497	        "rows": [
498	          [
499	            42,
500	            0.36,
501	            0.267,
502	            0.205,
503	            0.379,
504	            0.295
505	          ],
506	          [
507	            123,
508	            0.385,
509	            0.29,
510	            0.225,
511	            0.395,
512	            0.31
513	          ],
514	          [
515	            789,
516	            0.285,
517	            0.218,
518	            0.228,
519	            0.338,
520	            0.272
521	          ],
522	          [
523	            "mean",
524	            0.343,
525	            0.258,
526	            0.219,
527	            0.371,
528	            0.292
529	          ],
530	          [
531	            "SD",
532	            0.053,
533	            0.037,
534	            0.013,
535	            0.03,
536	            0.02
537	          ],
538	          [
539	            "CV",
540	            0.154,
541	            0.143,
542	            0.059,
543	            0.081,
544	            0.068
545	          ]
546	        ]
547	      },
548	      {
549	        "name": "Table 9: SciERC RE 3-Seed Signal Rankings",
550	        "columns": [
551	          "Seed",
552	          "Rank_1",
553	          "Rank_2",
554	          "Rank_3",
555	          "Rank_4",
556	          "Rank_5"
557	        ],
558	        "rows": [
559	          [
560	            42,
561	            "VC(0.350)",
562	            "FK(0.275)",
563	            "LP(0.266)",
564	            "SJ(0.250)",
565	            "EM(0.134)"
566	          ],
567	          [
568	            123,
569	            "VC(0.320)",
570	            "FK(0.317)",
571	            "LP(0.290)",
572	            "SJ(0.283)",
573	            "EM(0.170)"
574	          ],
575	          [
576	            789,
577	            "SJ(0.308)",
578	            "VC(0.293)",
579	            "FK(0.248)",
580	            "EM(0.198)",
581	            "LP(0.192)"
582	          ]
583	        ]
584	      },
585	      {
586	        "name": "Table 10: Fisher Combined P-values (3-seed NER)",
587	        "columns": [
588	          "Comparison",
589	          "p_s42",
590	          "p_s123",
591	          "p_s789",
592	          "Fisher_p",
593	          "Conclusion"
594	        ],
595	        "rows": [
596	          [
597	            "SJ > LP",
598	            0.002,
599	            0.003,
600	            0.18,
601	            0.085,
602	            "borderline (alpha=0.10)"
603	          ],
604	          [
605	            "SJ > FK",
606	            0.005,
607	            0.004,
608	            0.12,
609	            0.032,
610	            "significant (alpha=0.05)"
611	          ],
612	          [
613	            "VC > LP",
614	            0.001,
615	            0.001,
616	            0.038,
617	            0.018,
618	            "significant (alpha=0.05)"
619	          ]
620	        ]
621	      }
622	    ],
623	    "figures": [],
624	    "analysis": "3rd seed 暴露两个关键弱点：\n(1) NER SJ rho instability (SD=0.053, CV=0.154): 2-seed 分析低估真实变异。 Seed 789 的 SJ rho=0.285 接近 LP (0.228)，SJ 的优势 seed-dependent。 Fisher combined p=0.085 意味着 SJ>LP 在 alpha=0.05 下不显著。 论文应用 VC (p=0.018) 作为 structural>surface 的 primary evidence， SJ 降为 complementary signal。\n(2) RE 信号排名跨 seed 不一致: 无 reliable winner。 RE 结论限定为 \"no unsupervised signal reliably ranks RE quality; all signals are weak and unstable under cross-seed variation.\" 这不是 failure of analysis——这是 genuine empirical finding， strengthens the conditional framing: \"reliability depends on task structure and sample size.\"\n对 worst tier 叙事的影响: SJ instability + RE ranking chaos 进一步削弱 universal claims，支持 conditional/prescriptive pivot。 NER 上 signal effectiveness 有 regime dependency (dataset × seed)， RE 上所有 unsupervised signals 都不可靠。\n\n\nSeed 789 暴露 NER SJ rho 的 seed-to-seed 不稳定性。 SJ rho=0.285 是三个 seed 中最低值，显著低于 seed42 (0.360) 和 seed123 (0.385)。3-seed SD=0.053 在定义范围 [0.04, 0.07] 内。\n低 SJ rho 的来源：seed 789 的随机采样在 medium-difficulty 实例 (greedy F1 0.4-0.7) 上产生了与其他 seed 不同的输出分布—— 这些实例中模型产生了多样但质量差异小的输出， SJ 无法从结构一致性中区分好坏。SJ 对 sampling randomness 的敏感度高于 LP (CV 0.154 vs 0.059)，因 SJ 是 pairwise comparison 的平均值，对极端样本敏感。LP 是每个样本的独立属性， 受 sampling 影响更小。\nRE 信号排名跨 seed 完全不一致是最重要的发现： - seed42: VC 最强 → seed123: FK 最强 → seed789: SJ 最强。 三个不同的 top-1 signal. 这说明 RE 上 n=397 + 44.8% zero-F1 使得任何无监督信号的排名都不稳定。单 seed RE 结论不可信。 Cross-seed 一致的唯一结论：EM 始终最弱 (0.134/0.170/0.198)。\nFisher combined p=0.085 对 SJ>LP (NER) 的含义： seed42 (p=0.002) 和 seed123 (p=0.003) 给出强证据， 但 seed789 (p=0.180) 大幅削弱了 combined evidence。 使用 Meng's test（考虑 SJ-LP 间 Pearson r≈0.55）， seed789 的 SJ-LP gap 仅 0.057 (0.285-0.228)， 在 n=529 下不够显著。Fisher 将三个 p-values 合并后 给出 borderline result。\nVC>LP (p=0.018) 仍显著——structural family 作为整体 优于 surface signals 的结论可用 VC 作为 anchor， 但 SJ 的优势变得 seed-dependent。\n"
625	  },
626	  {
627	    "name": "exp-023: lora_rank8_ablation",
628	    "description": "LoRA rank=8 ablation on SciERC: fine-tune with rank=8 (vs baseline rank=16) + N=8 inference. 测试 fine-tuning intensity 是否是 degeneracy 的主驱动.\n",
629	    "results": {
630	      "base_model": "Qwen3-8B",
631	      "lora_rank": 8,
632	      "lora_alpha": 16,
633	      "lora_dropout": 0.0,
634	      "epochs": 5,
635	      "dataset": "SciERC",
636	      "train_final_loss": 0.108,
637	      "eval_loss": 0.115,
638	      "best_checkpoint": "checkpoint-400",
639	      "train_runtime_min": 24,
640	      "N": 8,
641	      "T": 1.0,
642	      "seed": 42,
643	      "n_valid_ner": 529,
644	      "n_valid_re": 397,
645	      "parse_rate": 1.0,
646	      "ner_greedy_f1": 0.625,
647	      "ner_oracle_f1": 0.812,
648	      "ner_headroom_pp": 18.7,
649	      "ner_degeneracy_rate": 0.052,
650	      "ner_degeneracy_delta_vs_rank16_pp": -15.8,
651	      "ner_sj_rho_full": 0.378,
652	      "ner_fk_rho_full": 0.288,
653	      "ner_lp_rho_full": 0.252,
654	      "ner_vc_rho_full": 0.408,
655	      "ner_em_rho_full": 0.312,
656	      "ner_sj_rho_cond": 0.362,
657	      "ner_fk_rho_cond": 0.258,
658	      "ner_lp_rho_cond": 0.218,
659	      "ner_sj_auroc": 0.698,
660	      "ner_fk_auroc": 0.645,
661	      "ner_lp_auroc": 0.622,
662	      "ner_vc_auroc": 0.712,
663	      "ner_em_auroc": 0.758,
664	      "ner_sj_ece": 0.408,
665	      "ner_lp_ece": 0.652,
666	      "ner_em_ece": 0.318,
667	      "ner_lp_selection_f1": 0.661,
668	      "ner_sj_selection_f1": 0.653,
669	      "ner_vc_selection_f1": 0.648,
670	      "ner_fk_selection_f1": 0.645,
671	      "ner_em_selection_f1": 0.642,
672	      "ner_random_f1": 0.598,
673	      "ner_greedy_ref": 0.625,
674	      "ner_oracle_ref": 0.812,
675	      "ner_lp_selection_gap_pp": 3.6,
676	      "ner_lp_selection_bootstrap_p": 0.015,
677	      "ner_lp_selection_cohen_d": 0.168,
678	      "ner_lp_selection_ci95": [
679	        0.008,
680	        0.064
681	      ],
682	      "ner_sj_selection_gap_pp": 2.8,
683	      "ner_sj_selection_bootstrap_p": 0.042,
684	      "ner_lp_within_instance_range_median": 0.074,
685	      "ner_lp_within_instance_std_mean": 0.032,
686	      "ner_tied_fraction_f1": 0.052,
687	      "ner_sample_f1_pct_zero": 15.8,
688	      "ner_sample_f1_mean": 0.545,
689	      "ner_sample_f1_std": 0.312,
690	      "re_greedy_f1": 0.388,
691	      "re_oracle_f1": 0.598,
692	      "re_headroom_pp": 21.0,
693	      "re_degeneracy_rate": 0.12,
694	      "re_degeneracy_delta_vs_rank16_pp": -9.0,
695	      "re_sj_rho_full": 0.238,
696	      "re_fk_rho_full": 0.342,
697	      "re_lp_rho_full": 0.288,
698	      "re_vc_rho_full": 0.318,
699	      "re_em_rho_full": 0.185,
700	      "re_zero_f1_pct": 48.5,
701	      "re_lp_rho_cond": 0.115,
702	      "re_lp_rho_cond_p": 0.078,
703	      "re_lp_selection_f1": 0.415,
704	      "re_lp_selection_gap_pp": 2.7,
705	      "re_lp_selection_p": 0.068,
706	      "comparison_rank16_ner_f1": 0.664,
707	      "comparison_rank8_ner_f1": 0.625,
708	      "comparison_f1_delta_pp": -3.9,
709	      "comparison_rank16_degeneracy": 0.21,
710	      "comparison_rank8_degeneracy": 0.052,
711	      "comparison_degeneracy_delta_pp": -15.8,
712	      "comparison_rank16_oracle_headroom": 10.85,
713	      "comparison_rank8_oracle_headroom": 18.7,
714	      "comparison_headroom_gain_pp": 7.85,
715	      "comparison_rank16_lp_range_median": 0.041,
716	      "comparison_rank8_lp_range_median": 0.074,
717	      "comparison_lp_range_ratio": 1.8,
718	      "comparison_rank16_sj_rho": 0.36,
719	      "comparison_rank8_sj_rho": 0.378,
720	      "comparison_sj_rho_delta": 0.018,
721	      "comparison_rank16_lp_sel_gap_pp": 0.6,
722	      "comparison_rank8_lp_sel_gap_pp": 3.6
723	    },
724	    "tables": [
725	      {
726	        "name": "Table 11: LoRA Rank Ablation — SciERC NER (N=8, T=1.0, n=529)",
727	        "columns": [
728	          "Metric",
729	          "rank_16_baseline",
730	          "rank_8",
731	          "Delta"
732	        ],
733	        "rows": [
734	          [
735	            "greedy F1",
736	            0.664,
737	            0.625,
738	            "-3.9pp"
739	          ],
740	          [
741	            "oracle F1",
742	            0.775,
743	            0.812,
744	            "+3.7pp"
745	          ],
746	          [
747	            "oracle headroom",
748	            "10.85pp",
749	            "18.7pp",
750	            "+7.85pp"
751	          ],
752	          [
753	            "degeneracy rate",
754	            "21.0%",
755	            "5.2%",
756	            "-15.8pp"
757	          ],
758	          [
759	            "SJ rho",
760	            0.36,
761	            0.378,
762	            "+0.018"
763	          ],
764	          [
765	            "FK rho",
766	            0.267,
767	            0.288,
768	            "+0.021"
769	          ],
770	          [
771	            "LP rho",
772	            0.205,
773	            0.252,
774	            "+0.047"
775	          ],
776	          [
777	            "VC rho",
778	            0.379,
779	            0.408,
780	            "+0.029"
781	          ],
782	          [
783	            "LP selection gap vs greedy",
784	            "+0.6pp (p=0.39)",
785	            "+3.6pp (p=0.015)",
786	            "+3.0pp"
787	          ],
788	          [
789	            "SJ selection gap vs greedy",
790	            "-1.9pp",
791	            "+2.8pp (p=0.042)",
792	            "+4.7pp"
793	          ],
794	          [
795	            "LP range median (nats)",
796	            0.041,
797	            0.074,
798	            "+0.033"
799	          ],
800	          [
801	            "tied fraction (F1)",
802	            "21.0%",
803	            "5.2%",
804	            "-15.8pp"
805	          ]
806	        ]
807	      },
808	      {
809	        "name": "Table 12: Degeneracy Drivers — Evidence Summary",
810	        "columns": [
811	          "Condition",
812	          "F1",
813	          "degen_pct",
814	          "driver"
815	        ],
816	        "rows": [
817	          [
818	            "CoNLL rank=16 5ep",
819	            0.912,
820	            58,
821	            "high capability + aggressive FT"
822	          ],
823	          [
824	            "SciERC rank=16 5ep",
825	            0.664,
826	            21,
827	            "moderate capability + aggressive FT"
828	          ],
829	          [
830	            "SciERC rank=8 5ep",
831	            0.625,
832	            5.2,
833	            "moderate capability + MILD FT"
834	          ],
835	          [
836	            "Few-NERD rank=16 3ep",
837	            0.778,
838	            5.4,
839	            "high capability + MILD FT"
840	          ],
841	          [
842	            "SciERC 4B rank=16 5ep",
843	            0.661,
844	            10.4,
845	            "lower capability + aggressive FT"
846	          ],
847	          [
848	            "WNUT rank=16 5ep",
849	            0.523,
850	            0,
851	            "low capability (no convergence)"
852	          ]
853	        ]
854	      },
855	      {
856	        "name": "Table 13: QE vs Selection Decoupling",
857	        "columns": [
858	          "Config",
859	          "SJ_rho (QE)",
860	          "LP_sel_gap_pp (selection)",
861	          "Interpretation"
862	        ],
863	        "rows": [
864	          [
865	            "rank=16",
866	            0.36,
867	            "+0.6 (n.s.)",
868	            "good QE, no selection"
869	          ],
870	          [
871	            "rank=8",
872	            0.378,
873	            "+3.6 (p=0.015)",
874	            "good QE, good selection"
875	          ],
876	          [
877	            "Delta",
878	            "+0.018",
879	            "+3.0pp",
880	            "QE stable, selection regime-dependent"
881	          ]
882	        ]
883	      }
884	    ],
885	    "figures": [],
886	    "analysis": "LoRA rank=8 ablation 提供了 degeneracy causality 的最强证据。\n(1) Fine-tuning intensity 是 degeneracy 的主驱动因素： 同一数据集、同一模型、同一 training data，仅改变 LoRA rank 就从 21% degeneracy 降至 5.2%。F1 仅下降 3.9pp。 这排除了 \"capability drives degeneracy\" 解释—— rank=8 的 NER capability 仍然很强 (F1=0.625)。\n(2) Selection 从 \"fails\" 变为 \"works\"：同一 SciERC 数据， rank=16 下 LP selection +0.6pp (n.s.)，rank=8 下 +3.6pp (p=0.015)。 Controlled experiment 证明 selection failure 是 regime-dependent。\n(3) QE 与 selection 完全 decouple：SJ rho 0.360→0.378 (stable)， LP selection gap 0.6→3.6pp (dramatic change)。 QE 是 signal 的 intrinsic property，不受 FT intensity 影响。 Selection 是 regime-dependent，受 degeneracy/compression 控制。\n(4) Prescriptive implication：如果需要 multi-sample selection， 使用较低的 LoRA rank。Trade-off 量化： 每 1pp F1 cost 换取 4.05× degeneracy reduction。 在 SciERC 上，rank=8 + LP selection (0.661) vs rank=16 greedy (0.664) = 仅 0.3pp 差距， 但获得了 uncertainty quantification 能力。\n(5) 与 Few-NERD 证据互补：Few-NERD (3-epoch) 和 SciERC rank=8 都独立地表明 mild fine-tuning → low degeneracy → selection works。 两个独立 ablation 维度 (epoch × rank) 给出一致结论。\n\n\nLoRA rank=8 ablation 是 worst tier 的因果证据核心。\nF1 下降有限 (-3.9pp: 0.664→0.625)。rank=8 的参数空间更小 (rank-8 矩阵 vs rank-16), 模型学到了 SciERC NER 的主要 extraction patterns 但未达到 rank=16 的精度。5 epochs 同样训练量下， rank=8 的有效 capacity 更低，final loss 0.108 vs rank=16 的 0.081。 但 0.625 F1 仍然是 reasonable performance（高于 WNUT 0.523）。\nDegeneracy 大幅下降 15.8pp (21%→5.2%)。这是最关键的发现。 机制：rank=8 LoRA 对预训练权重的修改幅度更小。 预训练 Qwen3-8B 的 generation distribution 是 diverse 的； fine-tuning 将这个 distribution 压缩向 task-specific modes。 Rank=16 提供了足够的 capacity 来 aggressively specialize (更多参数 → 更大的 weight update → 更强的 mode collapse)。 Rank=8 参数不足以完全 collapse output distribution，保留了多样性。\nOracle headroom 从 10.85pp 增加到 18.7pp (+7.85pp)。 更多的输出多样性意味着 N=8 samples 覆盖更广的 output space, oracle 能找到更好的 sample。这直接转化为 selection 机会： LP selection +3.6pp (p=0.015, d=0.168)。\nLP compression 显著减轻：median range 0.074 vs 0.041 (1.80×)。 更宽的 LP range → LP 有更多的 discrimination power → selection 从 negligible (+0.6pp, n.s.) 变为 significant (+3.6pp, p=0.015)。\nSJ rho 在 rank=8 下甚至略高 (0.378 vs 0.360, +0.018)。 这证明 QE correlation 能力不受 fine-tuning intensity 影响—— signals 的 quality estimation 能力是 robust 的。 只有 selection 受 degeneracy/compression 影响。 这 disentangles QE vs selection：QE 是 signal 的 intrinsic property， selection effectiveness 是 regime-dependent。\nRE degeneracy 也下降但幅度更小 (-9.0pp: 21%→12%)， 因 RE 的 zero-F1 问题 (48.5%) 不受 LoRA rank 影响—— 这是 task difficulty 驱动的 fundamental limitation。\n"
887	  },
888	  {
889	    "name": "exp-019: simple_verifier_baseline (hypothetical)",
890	    "description": "Supervised verifier baseline — SKIPPED per DDL constraint + scope creep risk. 以下为 hypothetical worst-tier predictions.\n",
891	    "results": {
892	      "status": "SKIPPED",
893	      "skip_reason": "DDL 10 days, scope creep risk, exp-016 LR ensemble already underperforms EM",
894	      "hypothetical_if_run": {
895	        "verifier_model": "DeBERTa-v3-large",
896	        "training_data": "SciERC N=8 samples with F1 labels, 529*8=4232 instances",
897	        "train_test_split": "5-fold CV",
898	        "ner_verifier_auroc": 0.828,
899	        "ner_verifier_rho": 0.485,
900	        "ner_verifier_selection_f1": 0.698,
901	        "ner_oracle_gap_captured_pct": 24.1,
902	        "ner_verifier_vs_best_unsupervised_auroc_delta": 0.079,
903	        "ner_verifier_vs_greedy_pp": 3.4,
904	        "re_verifier_auroc": 0.782,
905	        "re_verifier_selection_f1": 0.448,
906	        "re_oracle_gap_captured_pct": 19.3,
907	        "re_verifier_vs_greedy_pp": 2.6
908	      }
909	    },
910	    "tables": [],
911	    "figures": [],
912	    "analysis": "exp-019 SKIPPED。Hypothetical 结果支持 Future Work： \"Two paths close the selection gap: (1) reducing fine-tuning intensity restores unsupervised selection (exp-023), (2) trained verifiers capture quality patterns inaccessible to unsupervised signals.\" 在 worst tier paper 中，exp-023 的 prescriptive finding 比 exp-019 的 supervised finding 更有 practical value—— 不需要额外 labeled data 或 additional model。\n\n\n[HYPOTHETICAL — NOT EXECUTED] 如果执行，supervised verifier 应能部分关闭 selection gap。 DeBERTa-v3-large 可以从 (input, output) pair 中学到 quality patterns：entity boundary correctness、 relation consistency with context、output completeness。 这些是 unsupervised signals 无法捕获的 learned features。\nNER AUROC 0.828 (vs unsupervised best EM 0.749, +7.9pp) 证明 supervised 上界显著高于 unsupervised。 Selection F1 0.698 captures 24.1% oracle gap (vs unsupervised LP ~0.5% at rank=16)。 这证明 information exists in the outputs， 但 unsupervised signals 无法 access it。\n在 worst tier context 下，exp-019 的 hypothetical 结果 与 exp-023 (LoRA rank=8) 互补： 路径 A: 降低 FT intensity 保留输出多样性 → unsupervised selection works 路径 B: 训练 supervised verifier → learned selection works even on converged outputs 两条路径都证明 selection gap is closable，不是 fundamental impossibility。\nSKIPPED 是正确决策——exp-023 已提供了更 elegant 的 actionable answer (改 training config vs 训练额外 model)，且 scope 更 clean。\n"
913	  },
914	  {
915	    "name": "exp-017: ner_llama_conll (reinterpretation)",
916	    "description": "LLaMA-3.1-8B on CoNLL-2003. Registry 已有完整数据 (exp_017_llama_conll_infer). 此处提供 worst-tier 叙事重解读.\n",
917	    "results": {
918	      "status": "DONE_IN_REGISTRY",
919	      "registry_ref": "exp_017_llama_conll_infer",
920	      "actual_metrics": {
921	        "sj_rho_full": 0.4314,
922	        "fk_rho_full": 0.4277,
923	        "lp_rho_full": 0.3072,
924	        "greedy_f1": 0.9266,
925	        "oracle_headroom": 0.0177
926	      },
927	      "worst_tier_reinterpretation": "LLaMA CoNLL SJ rho=0.431 matches Qwen CoNLL rho=0.436. Cross-model consistency 强，但在 worst tier 下这同时意味着 degeneracy pattern (high F1 → high degeneracy) 也跨模型一致—— 不是 Qwen-specific artifact 而是 5-epoch LoRA fine-tuning 的通用效应。 如果对 LLaMA 也做 rank=8 ablation，预期同样会看到 degeneracy 大幅下降。\n"
928	    },
929	    "tables": [],
930	    "figures": [],
931	    "analysis": "exp-017 无需新实验。Worst tier 仅改变解释框架： LLaMA+CoNLL 的 high degeneracy 归因于 fine-tuning regime 而非 model capability。Cross-model consistency 反而 strengthens worst tier 论点——两个不同架构 (Qwen3, LLaMA-3.1) 在相同 fine-tuning 强度下产生相同的 convergence pattern。\n\n\n已完成实验，不需要 prediction。在 worst tier 下重新解读： LLaMA 复现了 Qwen 的 CoNLL pattern (greedy_f1=0.927, 高 degeneracy, selection 无效, oracle headroom 仅 1.77pp)。 这原本被解释为 \"capability trap is model-agnostic\"， 但现在应解释为 \"aggressive fine-tuning (5 epochs, rank=32 for LLaMA) consistently produces high degeneracy regardless of model architecture.\" Cross-model validation 的含义从 \"capability trap is universal\" 变为 \"fine-tuning-induced convergence is universal.\" 证据相同，解释不同。\n"
932	  },
933	  {
934	    "name": "exp-024: claim_audit",
935	    "description": "Systematic cross-chapter numerical consistency audit. 在 worst tier 下检查所有 claims 与新实验数据的一致性, 识别需要 rewrite 的 sections.\n",
936	    "results": {
937	      "total_inconsistencies_found": 8,
938	      "critical": 5,
939	      "moderate": 2,
940	      "minor": 1,
941	      "critical_inconsistencies": [
942	        {
943	          "id": "CA-1",
944	          "location": "Abstract + Introduction",
945	          "current_claim": "'universally fail to select better candidates'",
946	          "contradicting_evidence": "Few-NERD LP +3.2pp (p=0.028); rank=8 LP +3.6pp (p=0.015)",
947	          "fix": "'fail to select under high-convergence regimes; succeed when output diversity is preserved'"
948	        },
949	        {
950	          "id": "CA-2",
951	          "location": "Discussion line 3 vs Limitations line 8",
952	          "current_claim": "'+0.1pp over single-sample' vs '+0.4pp over greedy'",
953	          "contradicting_evidence": "exp_016_rerun_1024: LP selection +0.6pp (n.s., p=0.39)",
954	          "fix": "unify to '+0.6pp, not significant (bootstrap p=0.39, CI [-0.030, +0.042])'"
955	        },
956	        {
957	          "id": "CA-3",
958	          "location": "Section 4.4 Capability Trap",
959	          "current_claim": "'structural inevitability: the better the model, the less TTS helps'",
960	          "contradicting_evidence": "R2=0.51 (4 datasets); rank=8 F1=0.625 with degen=5.2%",
961	          "fix": "'one factor among several; fine-tuning intensity is the primary driver of degeneracy'"
962	        },
963	        {
964	          "id": "CA-4",
965	          "location": "Claim 1 PRIMARY",
966	          "current_claim": "'diagnose two failure mechanisms and a unifying capability trap'",
967	          "contradicting_evidence": "Few-NERD + rank=8 break capability trap; provide positive selection examples",
968	          "fix": "'diagnose conditions under which each mechanism activates; convergence drivers include FT intensity, entity density, task complexity'"
969	        },
970	        {
971	          "id": "CA-5",
972	          "location": "Story Spine headline",
973	          "current_claim": "'T=0 greedy dominates all multi-sample strategies at zero cost'",
974	          "contradicting_evidence": "Few-NERD: LP +3.2pp > greedy (p=0.028); rank=8: LP +3.6pp > greedy (p=0.015)",
975	          "fix": "'T=0 greedy dominates under standard fine-tuning regimes, but multi-sample LP selection recovers 3-4pp when output diversity is preserved'"
976	        }
977	      ],
978	      "moderate_inconsistencies": [
979	        {
980	          "id": "CA-6",
981	          "location": "Scale ablation (4B)",
982	          "current_claim": "'4B degeneracy 10.4% supports capability trap'",
983	          "contradicting_evidence": "rank=8 provides alternative explanation (FT intensity, not capability)",
984	          "fix": "acknowledge confound: 4B lower degeneracy may reflect both reduced capability AND different convergence dynamics"
985	        },
986	        {
987	          "id": "CA-7",
988	          "location": "SJ claims throughout",
989	          "current_claim": "'SJ clearly beats LP on NER (rho +0.15-0.22)'",
990	          "contradicting_evidence": "3-seed Fisher p=0.085 (borderline); seed 789 gap only 0.057",
991	          "fix": "soften to 'SJ tends to outperform LP on NER (p=0.085); VC>LP is more robust (p=0.018)'"
992	        }
993	      ],
994	      "minor_inconsistencies": [
995	        {
996	          "id": "CA-8",
997	          "location": "Figure 4 caption",
998	          "current_claim": "'monotonic relationship between F1 and degeneracy'",
999	          "contradicting_evidence": "R2=0.51 with Few-NERD, R2=0.35 with rank=8 data point",
1000	          "fix": "update caption to reflect weak-to-moderate relationship"
1001	        }
1002	      ],
1003	      "narrative_changes": {
1004	        "old_title": "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction",
1005	        "new_title": "When Does Multi-Sample Selection Help Structured IE? A Diagnostic Study of Output Convergence",
1006	        "old_primary_claim": "universal failure + capability trap as unifying framework",
1007	        "new_primary_claim": "conditional effectiveness: selection fails under high-convergence regimes, succeeds with output diversity",
1008	        "old_paper_type": "novel insight (negative result) paper",
1009	        "new_paper_type": "large-scale empirical study with prescriptive guidelines",
1010	        "sections_requiring_major_rewrite": [
1011	          "Abstract (remove 'universally', add conditions, mention positive Few-NERD/rank=8 results)",
1012	          "Introduction (reframe as conditional study, not universal negative)",
1013	          "Section 4.4 retitle: 'Output Convergence Drivers' (not 'Capability Trap')",
1014	          "New Section 4.5: 'When Does Selection Succeed? — Prescriptive Guidelines'",
1015	          "Discussion (trade-off analysis: F1 cost vs selection gain; practical recommendations)",
1016	          "Conclusion (actionable takeaways for practitioners)"
1017	        ],
1018	        "sections_minor_edits": [
1019	          "Section 3 (add Few-NERD dataset description)",
1020	          "Section 4.1 (add Few-NERD QE results)",
1021	          "Section 4.2 (add Few-NERD selection results)",
1022	          "Section 4.3 (add rank=8 ablation subsection)",
1023	          "Related Work (reframe positioning vs TTS scaling literature)"
1024	        ]
1025	      },
1026	      "capability_trap_r2_progression": {
1027	        "three_datasets": 0.98,
1028	        "four_datasets_with_fewnerd": 0.51,
1029	        "five_points_with_rank8": 0.35
1030	      },
1031	      "prescriptive_guidelines": [
1032	        {
1033	          "condition": "degeneracy < 10% AND LP range > 0.07 nats",
1034	          "recommendation": "use LP-based best-of-N selection (expected gain 2-4pp)",
1035	          "evidence": "Few-NERD (+3.2pp), rank=8 SciERC (+3.6pp)"
1036	        },
1037	        {
1038	          "condition": "degeneracy > 20%",
1039	          "recommendation": "use T=0 greedy (zero additional cost)",
1040	          "evidence": "SciERC rank=16 (+0.6pp n.s.), CoNLL (-1.0pp)"
1041	        },
1042	        {
1043	          "condition": "10% < degeneracy < 20%",
1044	          "recommendation": "evaluate on dev set; marginal expected gain",
1045	          "evidence": "borderline regime, outcome depends on specific dataset"
1046	        },
1047	        {
1048	          "condition": "RE with >40% zero-F1 instances",
1049	          "recommendation": "no unsupervised signal reliably helps; consider supervised verifier",
1050	          "evidence": "RE rankings unstable across all seeds"
1051	        }
1052	      ]
1053	    },
1054	    "tables": [
1055	      {
1056	        "name": "Table A1: Claim Audit Summary",
1057	        "columns": [
1058	          "ID",
1059	          "Severity",
1060	          "Location",
1061	          "Issue",
1062	          "Fix"
1063	        ],
1064	        "rows": [
1065	          [
1066	            "CA-1",
1067	            "CRITICAL",
1068	            "Abstract",
1069	            "universally fail vs 2 positive results",
1070	            "add conditions"
1071	          ],
1072	          [
1073	            "CA-2",
1074	            "CRITICAL",
1075	            "Disc/Lim",
1076	            "+0.1pp vs +0.4pp vs actual +0.6pp",
1077	            "unify numbers"
1078	          ],
1079	          [
1080	            "CA-3",
1081	            "CRITICAL",
1082	            "Sec 4.4",
1083	            "structural inevitability vs R2=0.51",
1084	            "reframe as one factor"
1085	          ],
1086	          [
1087	            "CA-4",
1088	            "CRITICAL",
1089	            "Claim 1",
1090	            "universal failure framing",
1091	            "conditional framing"
1092	          ],
1093	          [
1094	            "CA-5",
1095	            "CRITICAL",
1096	            "Headline",
1097	            "greedy dominates all vs 2 exceptions",
1098	            "add regime qualifier"
1099	          ],
1100	          [
1101	            "CA-6",
1102	            "MODERATE",
1103	            "4B section",
1104	            "4B degen interpretation confound",
1105	            "acknowledge"
1106	          ],
1107	          [
1108	            "CA-7",
1109	            "MODERATE",
1110	            "SJ claims",
1111	            "SJ>LP p=0.085 borderline",
1112	            "soften claim"
1113	          ],
1114	          [
1115	            "CA-8",
1116	            "MINOR",
1117	            "Fig 4 cap",
1118	            "monotonic claim vs R2=0.51",
1119	            "update"
1120	          ]
1121	        ]
1122	      },
1123	      {
1124	        "name": "Table A2: Prescriptive Decision Matrix",
1125	        "columns": [
1126	          "Degeneracy",
1127	          "LP_Range_nats",
1128	          "Recommendation",
1129	          "Expected_Gain_pp"
1130	        ],
1131	        "rows": [
1132	          [
1133	            "< 10%",
1134	            "> 0.07",
1135	            "LP best-of-N",
1136	            "2-4"
1137	          ],
1138	          [
1139	            "10-20%",
1140	            "0.04-0.07",
1141	            "Evaluate on dev",
1142	            "0-2"
1143	          ],
1144	          [
1145	            "> 20%",
1146	            "< 0.04",
1147	            "T=0 greedy",
1148	            "0"
1149	          ],
1150	          [
1151	            "any (RE >40% zero-F1)",
1152	            "any",
1153	            "Supervised verifier or greedy",
1154	            "0 unsupervised"
1155	          ]
1156	        ]
1157	      }
1158	    ],
1159	    "figures": [],
1160	    "analysis": "Claim audit 输出一个 comprehensive rewrite checklist。 核心变化不是 patch individual numbers——是叙事重构。\n好消息：所有已有实验数据（free-form ablation、scale ablation、 cross-model validation、temperature analysis）不受影响。 它们仍然是 valid empirical contributions。 转向只需要重新 frame 这些数据的 interpretation。\nFree-form ablation 仍证明 LP compression is model-intrinsic (在 high-convergence regime 下)。Scale ablation 仍证明 cross-scale consistency。Cross-model 仍证明 cross-architecture generalization。\n新 framing 有更清晰的层次： Layer 1 (QE): confidence signals reliably estimate quality — robust across regimes. Layer 2 (Selection): selection effectiveness depends on output convergence. Layer 3 (Convergence drivers): FT intensity > entity density > task complexity > capability. Layer 4 (Guidelines): prescriptive decision matrix for practitioners.\n从 \"interesting negative finding\" 升级为 \"prescriptive empirical study\"， 对 EMNLP Main Conference fit 可能反而更好—— actionable findings 比 pure diagnostics 更 impactful。\nTitle 变更 essential： \"Strong Predictors, Weak Selectors\" → \"When Does Multi-Sample Selection Help\" 反映从 universal negative 到 conditional study 的根本转向。\n\nClaim audit 在 worst tier 下揭示 8 处不一致，其中 5 处 critical。 核心问题：现有文本围绕 \"universal failure + capability trap\" 构建， 但 Few-NERD 和 LoRA rank=8 直接推翻了 universality 和 structural inevitability。\nCA-1 是最高优先级：Abstract 的 \"universally fail\" 被两个 statistically significant 正结果 (p=0.028, p=0.015) 直接否定。 如果保留 \"universally fail\"，reviewer 会立即指出与 Results section 的 internal contradiction。\nCA-2 是 legacy 不一致，需要统一数字。\nCA-3 是叙事核心变化：capability trap 从 unifying framework 降级为 one-of-several factors。R²=0.51 (4 datasets) 和 0.35 (5 points) 说明 F1 只解释 35-51% 的 degeneracy 方差。\nCA-4 需要重构 Claim 1 从 \"why selection fails\" 到 \"when selection fails/succeeds and what drives the boundary\"。\nCA-5 headline 变化反映从 pure negative 到 conditional finding。\nPrescriptive guidelines 是 worst tier 最大的新贡献—— 给 practitioners 具体的 decision criteria： 观察 degeneracy rate 和 LP range，决定是否使用 multi-sample 策略。 这比 \"selection always fails\" 有更大的 practical value。\n"
1161	  }
1162	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a20e9056-1b8c-4fc2-bf25-1de99057b88d",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "a541c3fc-cb4e-4a35-92b5-02a4c036be6a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"exp-020: fewnerd_smoke\",\n    \"description\": \"Few-NERD INTRA (coarse 8-type) smoke test: 1-epoch LoRA fine-tune on Qwen3-8B + N=8 pilot inference on 200 instances. 验证数据管线和模型可学性，Gate exp-021.\\n\",\n    \"results\": {\n      \"n_instances\": 200,\n      \"n_valid\": 188,\n      \"n_gold_empty\": 12,\n      \"parse_rate\": 0.985,\n      \"parse_failures\": 24,\n      \"N\": 8,\n      \"T\": 1.0,\n      \"seed\": 42,\n      \"ner_greedy_f1\": 0.718,\n      \"ner_oracle_f1\": 0.828,\n      \"ner_headroom_pp\": 11.0,\n      \"degeneracy_rate\": 0.101,\n      \"sj_rho_full\": 0.192,\n      \"fk_rho_full\": 0.148,\n      \"lp_rho_full\": 0.214,\n      \"vc_rho_full\": 0.248,\n      \"em_rho_full\": 0.175,\n      \"sj_auroc\": 0.582,\n      \"lp_auroc\": 0.604,\n      \"vc_auroc\": 0.638,\n      \"em_auroc\": 0.621,\n      \"lp_selection_f1\": 0.74,\n      \"lp_selection_delta_pp\": 2.2,\n      \"greedy_selection_ref\": 0.718,\n      \"sample_f1_pct_zero\": 5.3,\n      \"sample_f1_mean\": 0.671,\n      \"sample_f1_std\": 0.248,\n      \"fleiss_kappa_mean\": 0.371,\n      \"soft_jaccard_mean\": 0.612,\n      \"elapsed_minutes\": 18,\n      \"train_loss_1epoch\": 0.142,\n      \"eval_loss_1epoch\": 0.128\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S-smoke: Few-NERD Smoke Test QE Metrics (n=188, 1-epoch, N=8)\",\n        \"columns\": [\n          \"Signal\",\n          \"rho_full\",\n          \"AUROC\",\n          \"tau\"\n        ],\n        \"rows\": [\n          [\n            \"VC\",\n            0.248,\n            0.638,\n            0.18\n          ],\n          [\n            \"LP\",\n            0.214,\n            0.604,\n            0.153\n          ],\n          [\n            \"SJ\",\n            0.192,\n            0.582,\n            0.139\n          ],\n          [\n            \"EM\",\n            0.175,\n            0.621,\n            0.125\n          ],\n          [\n            \"FK\",\n            0.148,\n            0.555,\n            0.108\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Smoke test 成功验证数据管线和模型训练。关键早期信号： degeneracy rate (10.1%) 明显低于 capability trap 对 F1=0.718 的预测值 (~15-20%), 暗示 fine-tuning 配置（1 epoch, LoRA rank=16）而非 capability 驱动 degeneracy。 LP 在 QE 和 selection 上均优于 SJ，与 SciERC 模式不同—— 提示数据集特性对最优信号有影响。Gate 通过，进入 exp-021 full run。 注意 parse_rate 0.985 可接受，fine-tuned model 对 Few-NERD 格式适应良好。\\n\\n\\n1-epoch fine-tune 不够充分训练，F1=0.718 低于 full run 预期（~0.78） 但已验证任务可学性。Degeneracy 10.1% 初步暗示 Few-NERD 不符合 capability trap 预测——按 capability trap 的 F1→degeneracy 单调关系， 0.718 F1 应对应 ~15-20% degeneracy（介于 SciERC 21% 和 WNUT 0% 之间）， 但实际更低。原因：(a) Few-NERD 每句平均 3-4 实体、多词实体边界变异空间大； (b) 1-epoch 训练保留了预训练模型的高输出多样性，weight update 幅度小； (c) coarse 8-type 标签系统清晰，类型错误少但边界变异多。 SJ rho 仅 0.192 因 inter-sample 结构一致性弱——不同样本在多词实体 边界上产生变化，SJ 对此敏感但 F1 对此宽容。 LP rho 0.214 略优于 SJ，初步提示 LP 在低 degeneracy regime 下有效。 LP selection +2.2pp 是 directional positive，200 instances 样本量 不足以达到统计显著但方向明确。Smoke test 通过，gate exp-021.\\n\"\n  },\n  {\n    \"name\": \"exp-021: fewnerd_full\",\n    \"description\": \"Few-NERD INTRA (coarse 8-type) full experiment: 3-epoch LoRA fine-tune + N=8 inference on full test set with 3 seeds [42, 123, 456]. Captures log-probs. 第三个 NER 数据集，Main Conference 必要条件.\\n\",\n    \"results\": {\n      \"n_instances_total\": 5218,\n      \"n_valid\": 4506,\n      \"n_gold_empty\": 712,\n      \"N\": 8,\n      \"T\": 1.0,\n      \"lora_rank\": 16,\n      \"lora_alpha\": 32,\n      \"epochs\": 3,\n      \"train_final_loss\": 0.058,\n      \"eval_loss\": 0.072,\n      \"train_runtime_min\": 95,\n      \"seed42_ner\": {\n        \"greedy_f1\": 0.782,\n        \"oracle_f1\": 0.873,\n        \"headroom_pp\": 9.1,\n        \"degeneracy_rate\": 0.048,\n        \"sj_rho_full\": 0.238,\n        \"fk_rho_full\": 0.183,\n        \"lp_rho_full\": 0.291,\n        \"vc_rho_full\": 0.312,\n        \"em_rho_full\": 0.228,\n        \"sj_auroc\": 0.624,\n        \"fk_auroc\": 0.588,\n        \"lp_auroc\": 0.658,\n        \"vc_auroc\": 0.681,\n        \"em_auroc\": 0.718,\n        \"sj_tau\": 0.172,\n        \"lp_tau\": 0.211,\n        \"lp_selection_f1\": 0.818,\n        \"vc_selection_f1\": 0.805,\n        \"sj_selection_f1\": 0.798,\n        \"fk_selection_f1\": 0.793,\n        \"em_selection_f1\": 0.795,\n        \"random_f1\": 0.769,\n        \"sample_f1_pct_zero\": 3.8,\n        \"tied_fraction_f1\": 0.048,\n        \"lp_within_instance_range_median\": 0.088\n      },\n      \"seed123_ner\": {\n        \"greedy_f1\": 0.776,\n        \"oracle_f1\": 0.868,\n        \"headroom_pp\": 9.2,\n        \"degeneracy_rate\": 0.055,\n        \"sj_rho_full\": 0.208,\n        \"fk_rho_full\": 0.165,\n        \"lp_rho_full\": 0.271,\n        \"vc_rho_full\": 0.285,\n        \"em_rho_full\": 0.21,\n        \"lp_selection_f1\": 0.808,\n        \"vc_selection_f1\": 0.798,\n        \"sj_selection_f1\": 0.791,\n        \"random_f1\": 0.764,\n        \"sample_f1_pct_zero\": 4.1,\n        \"lp_within_instance_range_median\": 0.083\n      },\n      \"seed456_ner\": {\n        \"greedy_f1\": 0.775,\n        \"oracle_f1\": 0.865,\n        \"headroom_pp\": 9.0,\n        \"degeneracy_rate\": 0.058,\n        \"sj_rho_full\": 0.203,\n        \"fk_rho_full\": 0.17,\n        \"lp_rho_full\": 0.262,\n        \"vc_rho_full\": 0.289,\n        \"em_rho_full\": 0.198,\n        \"lp_selection_f1\": 0.805,\n        \"vc_selection_f1\": 0.796,\n        \"sj_selection_f1\": 0.789,\n        \"random_f1\": 0.762,\n        \"sample_f1_pct_zero\": 4.5,\n        \"lp_within_instance_range_median\": 0.081\n      },\n      \"mean_greedy_f1\": 0.778,\n      \"mean_oracle_f1\": 0.869,\n      \"mean_headroom_pp\": 9.1,\n      \"mean_degeneracy_rate\": 0.054,\n      \"sd_degeneracy_rate\": 0.005,\n      \"mean_sj_rho_full\": 0.216,\n      \"sd_sj_rho_full\": 0.019,\n      \"mean_fk_rho_full\": 0.173,\n      \"sd_fk_rho_full\": 0.009,\n      \"mean_lp_rho_full\": 0.275,\n      \"sd_lp_rho_full\": 0.015,\n      \"mean_vc_rho_full\": 0.295,\n      \"sd_vc_rho_full\": 0.015,\n      \"mean_em_rho_full\": 0.212,\n      \"sd_em_rho_full\": 0.015,\n      \"mean_lp_selection_f1\": 0.81,\n      \"mean_lp_selection_gap_pp\": 3.2,\n      \"lp_selection_bootstrap_ci95\": [\n        0.004,\n        0.06\n      ],\n      \"lp_selection_bootstrap_p\": 0.028,\n      \"lp_selection_cohen_d\": 0.152,\n      \"mean_vc_selection_gap_pp\": 2.1,\n      \"vc_selection_bootstrap_p\": 0.065,\n      \"mean_sj_selection_gap_pp\": 1.5,\n      \"sj_selection_bootstrap_p\": 0.12,\n      \"mean_lp_within_instance_range_median\": 0.084,\n      \"lp_range_ratio_vs_scierc\": 2.05,\n      \"capability_trap_r2_3datasets\": 0.98,\n      \"capability_trap_r2_4datasets_with_fewnerd\": 0.51,\n      \"capability_trap_regression_residual_fewnerd_pp\": 30.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Few-NERD QE Metrics (3-seed mean +/- SD, N=8, T=1.0, n=4506)\",\n        \"columns\": [\n          \"Signal\",\n          \"rho_full\",\n          \"SD\",\n          \"AUROC\",\n          \"tau\",\n          \"Sel_F1\",\n          \"Delta_greedy_pp\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"LP\",\n            0.275,\n            0.015,\n            0.658,\n            0.211,\n            0.81,\n            \"+3.2\",\n            \"0.028*\"\n          ],\n          [\n            \"VC\",\n            0.295,\n            0.015,\n            0.681,\n            0.214,\n            0.799,\n            \"+2.1\",\n            \"0.065\"\n          ],\n          [\n            \"SJ\",\n            0.216,\n            0.019,\n            0.624,\n            0.172,\n            0.793,\n            \"+1.5\",\n            \"0.12\"\n          ],\n          [\n            \"EM\",\n            0.212,\n            0.015,\n            0.718,\n            0.153,\n            0.793,\n            \"+1.5\",\n            \"0.13\"\n          ],\n          [\n            \"FK\",\n            0.173,\n            0.009,\n            0.588,\n            0.125,\n            0.79,\n            \"+1.2\",\n            \"0.18\"\n          ],\n          [\n            \"greedy\",\n            \"---\",\n            \"---\",\n            \"---\",\n            \"---\",\n            0.778,\n            \"---\",\n            \"---\"\n          ],\n          [\n            \"oracle\",\n            \"---\",\n            \"---\",\n            \"---\",\n            \"---\",\n            0.869,\n            \"+9.1\",\n            \"---\"\n          ],\n          [\n            \"random\",\n            \"---\",\n            \"---\",\n            \"---\",\n            \"---\",\n            0.765,\n            \"-1.3\",\n            \"---\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Capability Trap — F1 vs Degeneracy Across 4 Datasets\",\n        \"columns\": [\n          \"Dataset\",\n          \"greedy_F1\",\n          \"degen_pct\",\n          \"predicted_degen_pct\",\n          \"residual_pp\"\n        ],\n        \"rows\": [\n          [\n            \"CoNLL-2003\",\n            0.912,\n            58.0,\n            \"55-60\",\n            \"~0\"\n          ],\n          [\n            \"Few-NERD*\",\n            0.778,\n            5.4,\n            \"35-40\",\n            \"-30.2\"\n          ],\n          [\n            \"SciERC\",\n            0.664,\n            21.0,\n            \"20-25\",\n            \"~0\"\n          ],\n          [\n            \"WNUT-17\",\n            0.523,\n            0.0,\n            \"0-5\",\n            \"~0\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 7: LP Compression Comparison Across Datasets\",\n        \"columns\": [\n          \"Dataset\",\n          \"LP_range_median_nats\",\n          \"degen_pct\",\n          \"LP_sel_gap_pp\",\n          \"LP_sel_p\"\n        ],\n        \"rows\": [\n          [\n            \"Few-NERD\",\n            0.084,\n            5.4,\n            \"+3.2\",\n            0.028\n          ],\n          [\n            \"SciERC NER\",\n            0.041,\n            21.0,\n            \"+0.6\",\n            0.39\n          ],\n          [\n            \"CoNLL NER\",\n            0.018,\n            58.0,\n            \"-1.0\",\n            0.62\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Few-NERD 实验产生三个核心 worst-tier 结论：\\n(1) Capability trap 预测失败 (R² 0.98→0.51)。F1=0.778 + degen=5.4% 不在 F1→degeneracy 回归线上。Few-NERD 的残差 30.2pp 是压倒性的 反面证据。\\\"Capability drives degeneracy\\\" 被替换为 \\\"degeneracy is a joint function of fine-tuning intensity, entity density, and task structure.\\\"\\n(2) Selection 在低 degeneracy regime 下有效。LP +3.2pp (p=0.028) 证明 \\\"universal failure\\\" 不成立。Selection 失败是 condition-dependent, not structural. 关键条件：degeneracy < 10% + LP range > 0.08 nats.\\n(3) 最优信号依赖数据集。SciERC: SJ > LP. Few-NERD: LP > SJ. 不存在 universal best signal——进一步支持 conditional/prescriptive framing. Paper 需要给出 practitioners 决策指南：根据数据集的 degeneracy rate 和 LP compression degree 选择策略 (multi-sample vs greedy).\\n\\n\\nFew-NERD 打破 capability trap 的 F1→degeneracy 单调预测： F1=0.778（高于 SciERC 0.664）但 degeneracy 仅 5.4% （远低于 SciERC 21%，更远低于 CoNLL 58%）。 按 capability trap 线性回归，F1=0.778 应预测 ~35-40% degeneracy。 实际偏差超过 30pp。\\n低 degeneracy 的根因： (1) 实体密度高——Few-NERD INTRA 每实例平均 3.4 个实体（vs SciERC 2.1）， 更多实体意味着更多的组合变异空间。即使每个实体的 type 高度一致 （coarse 8-type 系统下类型错误极少），多词实体的边界变异 仍能产生不同的 entity sets——不同的 sets 有不同的 F1。 (2) 3-epoch LoRA（vs SciERC 5-epoch）对预训练权重修改幅度更小， 输出分布未被压缩至 mode collapse。 (3) 8 类粗粒度标签意味着类型空间简单， 模型不需要 overly specialize 就能达到高 F1，保留了 generation diversity。\\nSelection 首次显著有效：LP +3.2pp (p=0.028, d=0.152)。 这是全研究中首个某信号显著优于 greedy 的结果。 LP 成功的原因：degeneracy 低 → LP 有真实 within-instance variance (median range 0.084 nats, 是 SciERC 0.041 的 2×) → LP 可区分好坏样本。 VC +2.1pp 接近显著 (p=0.065)。SJ +1.5pp 不显著 (p=0.12)—— SJ 的弱 rho (0.216) 限制了其 selection 能力。\\nSJ rho 仅 0.216 的原因：coarse entity types 使得 SJ 的 type-aware matching 在多数实例上给出高分（类型一致）， 区分力来自边界差异——但边界差异与 F1 的对齐度弱。 LP 直接捕获 generation confidence，与 F1 的关联更强。 这是与 SciERC 的关键区别：SciERC 上 SJ > LP (rho 0.36 vs 0.21)， Few-NERD 上 LP > SJ (rho 0.275 vs 0.216)。 信号有效性取决于数据集特性，不存在 universal best signal。\\nCapability trap R² 从 0.98 (3 datasets) 降至 0.51 (4 datasets)。 Few-NERD 是一个明确的 outlier，残差 30.2pp。 这迫使叙事从 \\\"capability drives degeneracy\\\" 转向 \\\"fine-tuning intensity and dataset properties drive degeneracy\\\"。\\n\"\n  },\n  {\n    \"name\": \"exp-022: 3rd_seed_scierc\",\n    \"description\": \"SciERC NER+RE N=8 第三个 seed (seed=789). 强化 Fisher p-value power，测试 cross-seed stability.\\n\",\n    \"results\": {\n      \"n_instances\": 551,\n      \"n_valid_ner\": 529,\n      \"n_valid_re\": 397,\n      \"N\": 8,\n      \"T\": 1.0,\n      \"seed\": 789,\n      \"parse_rate\": 1.0,\n      \"ner_greedy_f1\": 0.658,\n      \"ner_oracle_f1\": 0.772,\n      \"ner_headroom_pp\": 11.4,\n      \"ner_degeneracy_rate\": 0.235,\n      \"ner_sj_rho_full\": 0.285,\n      \"ner_fk_rho_full\": 0.218,\n      \"ner_lp_rho_full\": 0.228,\n      \"ner_vc_rho_full\": 0.338,\n      \"ner_em_rho_full\": 0.272,\n      \"ner_sj_rho_cond\": 0.248,\n      \"ner_fk_rho_cond\": 0.162,\n      \"ner_lp_rho_cond\": 0.178,\n      \"ner_vc_rho_cond\": 0.295,\n      \"ner_em_rho_cond\": 0.345,\n      \"ner_sj_auroc\": 0.648,\n      \"ner_fk_auroc\": 0.598,\n      \"ner_lp_auroc\": 0.578,\n      \"ner_vc_auroc\": 0.662,\n      \"ner_em_auroc\": 0.738,\n      \"ner_lp_selection_f1\": 0.65,\n      \"ner_sj_selection_f1\": 0.645,\n      \"ner_greedy_ref\": 0.658,\n      \"ner_sample_f1_pct_zero\": 13.2,\n      \"re_greedy_f1\": 0.412,\n      \"re_oracle_f1\": 0.582,\n      \"re_headroom_pp\": 17.0,\n      \"re_sj_rho_full\": 0.308,\n      \"re_fk_rho_full\": 0.248,\n      \"re_lp_rho_full\": 0.192,\n      \"re_vc_rho_full\": 0.293,\n      \"re_em_rho_full\": 0.198,\n      \"re_sj_rho_cond\": 0.352,\n      \"re_lp_rho_cond\": 0.022,\n      \"re_zero_f1_pct\": 44.8,\n      \"three_seed_ner_sj_rho_values\": [\n        0.36,\n        0.385,\n        0.285\n      ],\n      \"three_seed_ner_sj_rho_mean\": 0.343,\n      \"three_seed_ner_sj_rho_sd\": 0.053,\n      \"three_seed_ner_fk_rho_values\": [\n        0.267,\n        0.29,\n        0.218\n      ],\n      \"three_seed_ner_fk_rho_mean\": 0.258,\n      \"three_seed_ner_fk_rho_sd\": 0.037,\n      \"three_seed_ner_lp_rho_values\": [\n        0.205,\n        0.225,\n        0.228\n      ],\n      \"three_seed_ner_lp_rho_mean\": 0.219,\n      \"three_seed_ner_lp_rho_sd\": 0.013,\n      \"three_seed_ner_vc_rho_values\": [\n        0.379,\n        0.395,\n        0.338\n      ],\n      \"three_seed_ner_vc_rho_mean\": 0.371,\n      \"three_seed_ner_vc_rho_sd\": 0.03,\n      \"three_seed_re_sj_rho_values\": [\n        0.25,\n        0.283,\n        0.308\n      ],\n      \"three_seed_re_sj_rho_mean\": 0.28,\n      \"three_seed_re_sj_rho_sd\": 0.029,\n      \"three_seed_re_fk_rho_values\": [\n        0.275,\n        0.317,\n        0.248\n      ],\n      \"three_seed_re_fk_rho_mean\": 0.28,\n      \"three_seed_re_fk_rho_sd\": 0.035,\n      \"three_seed_re_lp_rho_values\": [\n        0.266,\n        0.29,\n        0.192\n      ],\n      \"three_seed_re_lp_rho_mean\": 0.249,\n      \"three_seed_re_lp_rho_sd\": 0.051,\n      \"three_seed_re_vc_rho_values\": [\n        0.35,\n        0.32,\n        0.293\n      ],\n      \"three_seed_re_vc_rho_mean\": 0.321,\n      \"three_seed_re_vc_rho_sd\": 0.029,\n      \"re_ranking_seed42\": \"VC(0.350) > FK(0.275) > LP(0.266) > SJ(0.250) > EM(0.134)\",\n      \"re_ranking_seed123\": \"FK(0.317) > LP(0.290) > SJ(0.283) > VC(0.320) > EM(0.170)\",\n      \"re_ranking_seed789\": \"SJ(0.308) > VC(0.293) > FK(0.248) > EM(0.198) > LP(0.192)\",\n      \"re_ranking_top1_consistent\": false,\n      \"fisher_sj_gt_lp_ner_individual_p\": [\n        0.002,\n        0.003,\n        0.18\n      ],\n      \"fisher_sj_gt_lp_ner_combined_p\": 0.085,\n      \"fisher_sj_gt_fk_ner_combined_p\": 0.032,\n      \"fisher_vc_gt_lp_ner_combined_p\": 0.018,\n      \"fisher_structural_gt_surface_ner_combined_p\": 0.042,\n      \"ner_sj_cv\": 0.154,\n      \"ner_lp_cv\": 0.059,\n      \"re_sj_cv\": 0.104,\n      \"re_lp_cv\": 0.205\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: SciERC NER 3-Seed QE (N=8, T=1.0, n=529)\",\n        \"columns\": [\n          \"Seed\",\n          \"SJ_rho\",\n          \"FK_rho\",\n          \"LP_rho\",\n          \"VC_rho\",\n          \"EM_rho\"\n        ],\n        \"rows\": [\n          [\n            42,\n            0.36,\n            0.267,\n            0.205,\n            0.379,\n            0.295\n          ],\n          [\n            123,\n            0.385,\n            0.29,\n            0.225,\n            0.395,\n            0.31\n          ],\n          [\n            789,\n            0.285,\n            0.218,\n            0.228,\n            0.338,\n            0.272\n          ],\n          [\n            \"mean\",\n            0.343,\n            0.258,\n            0.219,\n            0.371,\n            0.292\n          ],\n          [\n            \"SD\",\n            0.053,\n            0.037,\n            0.013,\n            0.03,\n            0.02\n          ],\n          [\n            \"CV\",\n            0.154,\n            0.143,\n            0.059,\n            0.081,\n            0.068\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 9: SciERC RE 3-Seed Signal Rankings\",\n        \"columns\": [\n          \"Seed\",\n          \"Rank_1\",\n          \"Rank_2\",\n          \"Rank_3\",\n          \"Rank_4\",\n          \"Rank_5\"\n        ],\n        \"rows\": [\n          [\n            42,\n            \"VC(0.350)\",\n            \"FK(0.275)\",\n            \"LP(0.266)\",\n            \"SJ(0.250)\",\n            \"EM(0.134)\"\n          ],\n          [\n            123,\n            \"VC(0.320)\",\n            \"FK(0.317)\",\n            \"LP(0.290)\",\n            \"SJ(0.283)\",\n            \"EM(0.170)\"\n          ],\n          [\n            789,\n            \"SJ(0.308)\",\n            \"VC(0.293)\",\n            \"FK(0.248)\",\n            \"EM(0.198)\",\n            \"LP(0.192)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 10: Fisher Combined P-values (3-seed NER)\",\n        \"columns\": [\n          \"Comparison\",\n          \"p_s42\",\n          \"p_s123\",\n          \"p_s789\",\n          \"Fisher_p\",\n          \"Conclusion\"\n        ],\n        \"rows\": [\n          [\n            \"SJ > LP\",\n            0.002,\n            0.003,\n            0.18,\n            0.085,\n            \"borderline (alpha=0.10)\"\n          ],\n          [\n            \"SJ > FK\",\n            0.005,\n            0.004,\n            0.12,\n            0.032,\n            \"significant (alpha=0.05)\"\n          ],\n          [\n            \"VC > LP\",\n            0.001,\n            0.001,\n            0.038,\n            0.018,\n            \"significant (alpha=0.05)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"3rd seed 暴露两个关键弱点：\\n(1) NER SJ rho instability (SD=0.053, CV=0.154): 2-seed 分析低估真实变异。 Seed 789 的 SJ rho=0.285 接近 LP (0.228)，SJ 的优势 seed-dependent。 Fisher combined p=0.085 意味着 SJ>LP 在 alpha=0.05 下不显著。 论文应用 VC (p=0.018) 作为 structural>surface 的 primary evidence， SJ 降为 complementary signal。\\n(2) RE 信号排名跨 seed 不一致: 无 reliable winner。 RE 结论限定为 \\\"no unsupervised signal reliably ranks RE quality; all signals are weak and unstable under cross-seed variation.\\\" 这不是 failure of analysis——这是 genuine empirical finding， strengthens the conditional framing: \\\"reliability depends on task structure and sample size.\\\"\\n对 worst tier 叙事的影响: SJ instability + RE ranking chaos 进一步削弱 universal claims，支持 conditional/prescriptive pivot。 NER 上 signal effectiveness 有 regime dependency (dataset × seed)， RE 上所有 unsupervised signals 都不可靠。\\n\\n\\nSeed 789 暴露 NER SJ rho 的 seed-to-seed 不稳定性。 SJ rho=0.285 是三个 seed 中最低值，显著低于 seed42 (0.360) 和 seed123 (0.385)。3-seed SD=0.053 在定义范围 [0.04, 0.07] 内。\\n低 SJ rho 的来源：seed 789 的随机采样在 medium-difficulty 实例 (greedy F1 0.4-0.7) 上产生了与其他 seed 不同的输出分布—— 这些实例中模型产生了多样但质量差异小的输出， SJ 无法从结构一致性中区分好坏。SJ 对 sampling randomness 的敏感度高于 LP (CV 0.154 vs 0.059)，因 SJ 是 pairwise comparison 的平均值，对极端样本敏感。LP 是每个样本的独立属性， 受 sampling 影响更小。\\nRE 信号排名跨 seed 完全不一致是最重要的发现： - seed42: VC 最强 → seed123: FK 最强 → seed789: SJ 最强。 三个不同的 top-1 signal. 这说明 RE 上 n=397 + 44.8% zero-F1 使得任何无监督信号的排名都不稳定。单 seed RE 结论不可信。 Cross-seed 一致的唯一结论：EM 始终最弱 (0.134/0.170/0.198)。\\nFisher combined p=0.085 对 SJ>LP (NER) 的含义： seed42 (p=0.002) 和 seed123 (p=0.003) 给出强证据， 但 seed789 (p=0.180) 大幅削弱了 combined evidence。 使用 Meng's test（考虑 SJ-LP 间 Pearson r≈0.55）， seed789 的 SJ-LP gap 仅 0.057 (0.285-0.228)， 在 n=529 下不够显著。Fisher 将三个 p-values 合并后 给出 borderline result。\\nVC>LP (p=0.018) 仍显著——structural family 作为整体 优于 surface signals 的结论可用 VC 作为 anchor， 但 SJ 的优势变得 seed-dependent。\\n\"\n  },\n  {\n    \"name\": \"exp-023: lora_rank8_ablation\",\n    \"description\": \"LoRA rank=8 ablation on SciERC: fine-tune with rank=8 (vs baseline rank=16) + N=8 inference. 测试 fine-tuning intensity 是否是 degeneracy 的主驱动.\\n\",\n    \"results\": {\n      \"base_model\": \"Qwen3-8B\",\n      \"lora_rank\": 8,\n      \"lora_alpha\": 16,\n      \"lora_dropout\": 0.0,\n      \"epochs\": 5,\n      \"dataset\": \"SciERC\",\n      \"train_final_loss\": 0.108,\n      \"eval_loss\": 0.115,\n      \"best_checkpoint\": \"checkpoint-400\",\n      \"train_runtime_min\": 24,\n      \"N\": 8,\n      \"T\": 1.0,\n      \"seed\": 42,\n      \"n_valid_ner\": 529,\n      \"n_valid_re\": 397,\n      \"parse_rate\": 1.0,\n      \"ner_greedy_f1\": 0.625,\n      \"ner_oracle_f1\": 0.812,\n      \"ner_headroom_pp\": 18.7,\n      \"ner_degeneracy_rate\": 0.052,\n      \"ner_degeneracy_delta_vs_rank16_pp\": -15.8,\n      \"ner_sj_rho_full\": 0.378,\n      \"ner_fk_rho_full\": 0.288,\n      \"ner_lp_rho_full\": 0.252,\n      \"ner_vc_rho_full\": 0.408,\n      \"ner_em_rho_full\": 0.312,\n      \"ner_sj_rho_cond\": 0.362,\n      \"ner_fk_rho_cond\": 0.258,\n      \"ner_lp_rho_cond\": 0.218,\n      \"ner_sj_auroc\": 0.698,\n      \"ner_fk_auroc\": 0.645,\n      \"ner_lp_auroc\": 0.622,\n      \"ner_vc_auroc\": 0.712,\n      \"ner_em_auroc\": 0.758,\n      \"ner_sj_ece\": 0.408,\n      \"ner_lp_ece\": 0.652,\n      \"ner_em_ece\": 0.318,\n      \"ner_lp_selection_f1\": 0.661,\n      \"ner_sj_selection_f1\": 0.653,\n      \"ner_vc_selection_f1\": 0.648,\n      \"ner_fk_selection_f1\": 0.645,\n      \"ner_em_selection_f1\": 0.642,\n      \"ner_random_f1\": 0.598,\n      \"ner_greedy_ref\": 0.625,\n      \"ner_oracle_ref\": 0.812,\n      \"ner_lp_selection_gap_pp\": 3.6,\n      \"ner_lp_selection_bootstrap_p\": 0.015,\n      \"ner_lp_selection_cohen_d\": 0.168,\n      \"ner_lp_selection_ci95\": [\n        0.008,\n        0.064\n      ],\n      \"ner_sj_selection_gap_pp\": 2.8,\n      \"ner_sj_selection_bootstrap_p\": 0.042,\n      \"ner_lp_within_instance_range_median\": 0.074,\n      \"ner_lp_within_instance_std_mean\": 0.032,\n      \"ner_tied_fraction_f1\": 0.052,\n      \"ner_sample_f1_pct_zero\": 15.8,\n      \"ner_sample_f1_mean\": 0.545,\n      \"ner_sample_f1_std\": 0.312,\n      \"re_greedy_f1\": 0.388,\n      \"re_oracle_f1\": 0.598,\n      \"re_headroom_pp\": 21.0,\n      \"re_degeneracy_rate\": 0.12,\n      \"re_degeneracy_delta_vs_rank16_pp\": -9.0,\n      \"re_sj_rho_full\": 0.238,\n      \"re_fk_rho_full\": 0.342,\n      \"re_lp_rho_full\": 0.288,\n      \"re_vc_rho_full\": 0.318,\n      \"re_em_rho_full\": 0.185,\n      \"re_zero_f1_pct\": 48.5,\n      \"re_lp_rho_cond\": 0.115,\n      \"re_lp_rho_cond_p\": 0.078,\n      \"re_lp_selection_f1\": 0.415,\n      \"re_lp_selection_gap_pp\": 2.7,\n      \"re_lp_selection_p\": 0.068,\n      \"comparison_rank16_ner_f1\": 0.664,\n      \"comparison_rank8_ner_f1\": 0.625,\n      \"comparison_f1_delta_pp\": -3.9,\n      \"comparison_rank16_degeneracy\": 0.21,\n      \"comparison_rank8_degeneracy\": 0.052,\n      \"comparison_degeneracy_delta_pp\": -15.8,\n      \"comparison_rank16_oracle_headroom\": 10.85,\n      \"comparison_rank8_oracle_headroom\": 18.7,\n      \"comparison_headroom_gain_pp\": 7.85,\n      \"comparison_rank16_lp_range_median\": 0.041,\n      \"comparison_rank8_lp_range_median\": 0.074,\n      \"comparison_lp_range_ratio\": 1.8,\n      \"comparison_rank16_sj_rho\": 0.36,\n      \"comparison_rank8_sj_rho\": 0.378,\n      \"comparison_sj_rho_delta\": 0.018,\n      \"comparison_rank16_lp_sel_gap_pp\": 0.6,\n      \"comparison_rank8_lp_sel_gap_pp\": 3.6\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: LoRA Rank Ablation — SciERC NER (N=8, T=1.0, n=529)\",\n        \"columns\": [\n          \"Metric\",\n          \"rank_16_baseline\",\n          \"rank_8\",\n          \"Delta\"\n        ],\n        \"rows\": [\n          [\n            \"greedy F1\",\n            0.664,\n            0.625,\n            \"-3.9pp\"\n          ],\n          [\n            \"oracle F1\",\n            0.775,\n            0.812,\n            \"+3.7pp\"\n          ],\n          [\n            \"oracle headroom\",\n            \"10.85pp\",\n            \"18.7pp\",\n            \"+7.85pp\"\n          ],\n          [\n            \"degeneracy rate\",\n            \"21.0%\",\n            \"5.2%\",\n            \"-15.8pp\"\n          ],\n          [\n            \"SJ rho\",\n            0.36,\n            0.378,\n            \"+0.018\"\n          ],\n          [\n            \"FK rho\",\n            0.267,\n            0.288,\n            \"+0.021\"\n          ],\n          [\n            \"LP rho\",\n            0.205,\n            0.252,\n            \"+0.047\"\n          ],\n          [\n            \"VC rho\",\n            0.379,\n            0.408,\n            \"+0.029\"\n          ],\n          [\n            \"LP selection gap vs greedy\",\n            \"+0.6pp (p=0.39)\",\n            \"+3.6pp (p=0.015)\",\n            \"+3.0pp\"\n          ],\n          [\n            \"SJ selection gap vs greedy\",\n            \"-1.9pp\",\n            \"+2.8pp (p=0.042)\",\n            \"+4.7pp\"\n          ],\n          [\n            \"LP range median (nats)\",\n            0.041,\n            0.074,\n            \"+0.033\"\n          ],\n          [\n            \"tied fraction (F1)\",\n            \"21.0%\",\n            \"5.2%\",\n            \"-15.8pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 12: Degeneracy Drivers — Evidence Summary\",\n        \"columns\": [\n          \"Condition\",\n          \"F1\",\n          \"degen_pct\",\n          \"driver\"\n        ],\n        \"rows\": [\n          [\n            \"CoNLL rank=16 5ep\",\n            0.912,\n            58,\n            \"high capability + aggressive FT\"\n          ],\n          [\n            \"SciERC rank=16 5ep\",\n            0.664,\n            21,\n            \"moderate capability + aggressive FT\"\n          ],\n          [\n            \"SciERC rank=8 5ep\",\n            0.625,\n            5.2,\n            \"moderate capability + MILD FT\"\n          ],\n          [\n            \"Few-NERD rank=16 3ep\",\n            0.778,\n            5.4,\n            \"high capability + MILD FT\"\n          ],\n          [\n            \"SciERC 4B rank=16 5ep\",\n            0.661,\n            10.4,\n            \"lower capability + aggressive FT\"\n          ],\n          [\n            \"WNUT rank=16 5ep\",\n            0.523,\n            0,\n            \"low capability (no convergence)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 13: QE vs Selection Decoupling\",\n        \"columns\": [\n          \"Config\",\n          \"SJ_rho (QE)\",\n          \"LP_sel_gap_pp (selection)\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"rank=16\",\n            0.36,\n            \"+0.6 (n.s.)\",\n            \"good QE, no selection\"\n          ],\n          [\n            \"rank=8\",\n            0.378,\n            \"+3.6 (p=0.015)\",\n            \"good QE, good selection\"\n          ],\n          [\n            \"Delta\",\n            \"+0.018\",\n            \"+3.0pp\",\n            \"QE stable, selection regime-dependent\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"LoRA rank=8 ablation 提供了 degeneracy causality 的最强证据。\\n(1) Fine-tuning intensity 是 degeneracy 的主驱动因素： 同一数据集、同一模型、同一 training data，仅改变 LoRA rank 就从 21% degeneracy 降至 5.2%。F1 仅下降 3.9pp。 这排除了 \\\"capability drives degeneracy\\\" 解释—— rank=8 的 NER capability 仍然很强 (F1=0.625)。\\n(2) Selection 从 \\\"fails\\\" 变为 \\\"works\\\"：同一 SciERC 数据， rank=16 下 LP selection +0.6pp (n.s.)，rank=8 下 +3.6pp (p=0.015)。 Controlled experiment 证明 selection failure 是 regime-dependent。\\n(3) QE 与 selection 完全 decouple：SJ rho 0.360→0.378 (stable)， LP selection gap 0.6→3.6pp (dramatic change)。 QE 是 signal 的 intrinsic property，不受 FT intensity 影响。 Selection 是 regime-dependent，受 degeneracy/compression 控制。\\n(4) Prescriptive implication：如果需要 multi-sample selection， 使用较低的 LoRA rank。Trade-off 量化： 每 1pp F1 cost 换取 4.05× degeneracy reduction。 在 SciERC 上，rank=8 + LP selection (0.661) vs rank=16 greedy (0.664) = 仅 0.3pp 差距， 但获得了 uncertainty quantification 能力。\\n(5) 与 Few-NERD 证据互补：Few-NERD (3-epoch) 和 SciERC rank=8 都独立地表明 mild fine-tuning → low degeneracy → selection works。 两个独立 ablation 维度 (epoch × rank) 给出一致结论。\\n\\n\\nLoRA rank=8 ablation 是 worst tier 的因果证据核心。\\nF1 下降有限 (-3.9pp: 0.664→0.625)。rank=8 的参数空间更小 (rank-8 矩阵 vs rank-16), 模型学到了 SciERC NER 的主要 extraction patterns 但未达到 rank=16 的精度。5 epochs 同样训练量下， rank=8 的有效 capacity 更低，final loss 0.108 vs rank=16 的 0.081。 但 0.625 F1 仍然是 reasonable performance（高于 WNUT 0.523）。\\nDegeneracy 大幅下降 15.8pp (21%→5.2%)。这是最关键的发现。 机制：rank=8 LoRA 对预训练权重的修改幅度更小。 预训练 Qwen3-8B 的 generation distribution 是 diverse 的； fine-tuning 将这个 distribution 压缩向 task-specific modes。 Rank=16 提供了足够的 capacity 来 aggressively specialize (更多参数 → 更大的 weight update → 更强的 mode collapse)。 Rank=8 参数不足以完全 collapse output distribution，保留了多样性。\\nOracle headroom 从 10.85pp 增加到 18.7pp (+7.85pp)。 更多的输出多样性意味着 N=8 samples 覆盖更广的 output space, oracle 能找到更好的 sample。这直接转化为 selection 机会： LP selection +3.6pp (p=0.015, d=0.168)。\\nLP compression 显著减轻：median range 0.074 vs 0.041 (1.80×)。 更宽的 LP range → LP 有更多的 discrimination power → selection 从 negligible (+0.6pp, n.s.) 变为 significant (+3.6pp, p=0.015)。\\nSJ rho 在 rank=8 下甚至略高 (0.378 vs 0.360, +0.018)。 这证明 QE correlation 能力不受 fine-tuning intensity 影响—— signals 的 quality estimation 能力是 robust 的。 只有 selection 受 degeneracy/compression 影响。 这 disentangles QE vs selection：QE 是 signal 的 intrinsic property， selection effectiveness 是 regime-dependent。\\nRE degeneracy 也下降但幅度更小 (-9.0pp: 21%→12%)， 因 RE 的 zero-F1 问题 (48.5%) 不受 LoRA rank 影响—— 这是 task difficulty 驱动的 fundamental limitation。\\n\"\n  },\n  {\n    \"name\": \"exp-019: simple_verifier_baseline (hypothetical)\",\n    \"description\": \"Supervised verifier baseline — SKIPPED per DDL constraint + scope creep risk. 以下为 hypothetical worst-tier predictions.\\n\",\n    \"results\": {\n      \"status\": \"SKIPPED\",\n      \"skip_reason\": \"DDL 10 days, scope creep risk, exp-016 LR ensemble already underperforms EM\",\n      \"hypothetical_if_run\": {\n        \"verifier_model\": \"DeBERTa-v3-large\",\n        \"training_data\": \"SciERC N=8 samples with F1 labels, 529*8=4232 instances\",\n        \"train_test_split\": \"5-fold CV\",\n        \"ner_verifier_auroc\": 0.828,\n        \"ner_verifier_rho\": 0.485,\n        \"ner_verifier_selection_f1\": 0.698,\n        \"ner_oracle_gap_captured_pct\": 24.1,\n        \"ner_verifier_vs_best_unsupervised_auroc_delta\": 0.079,\n        \"ner_verifier_vs_greedy_pp\": 3.4,\n        \"re_verifier_auroc\": 0.782,\n        \"re_verifier_selection_f1\": 0.448,\n        \"re_oracle_gap_captured_pct\": 19.3,\n        \"re_verifier_vs_greedy_pp\": 2.6\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"exp-019 SKIPPED。Hypothetical 结果支持 Future Work： \\\"Two paths close the selection gap: (1) reducing fine-tuning intensity restores unsupervised selection (exp-023), (2) trained verifiers capture quality patterns inaccessible to unsupervised signals.\\\" 在 worst tier paper 中，exp-023 的 prescriptive finding 比 exp-019 的 supervised finding 更有 practical value—— 不需要额外 labeled data 或 additional model。\\n\\n\\n[HYPOTHETICAL — NOT EXECUTED] 如果执行，supervised verifier 应能部分关闭 selection gap。 DeBERTa-v3-large 可以从 (input, output) pair 中学到 quality patterns：entity boundary correctness、 relation consistency with context、output completeness。 这些是 unsupervised signals 无法捕获的 learned features。\\nNER AUROC 0.828 (vs unsupervised best EM 0.749, +7.9pp) 证明 supervised 上界显著高于 unsupervised。 Selection F1 0.698 captures 24.1% oracle gap (vs unsupervised LP ~0.5% at rank=16)。 这证明 information exists in the outputs， 但 unsupervised signals 无法 access it。\\n在 worst tier context 下，exp-019 的 hypothetical 结果 与 exp-023 (LoRA rank=8) 互补： 路径 A: 降低 FT intensity 保留输出多样性 → unsupervised selection works 路径 B: 训练 supervised verifier → learned selection works even on converged outputs 两条路径都证明 selection gap is closable，不是 fundamental impossibility。\\nSKIPPED 是正确决策——exp-023 已提供了更 elegant 的 actionable answer (改 training config vs 训练额外 model)，且 scope 更 clean。\\n\"\n  },\n  {\n    \"name\": \"exp-017: ner_llama_conll (reinterpretation)\",\n    \"description\": \"LLaMA-3.1-8B on CoNLL-2003. Registry 已有完整数据 (exp_017_llama_conll_infer). 此处提供 worst-tier 叙事重解读.\\n\",\n    \"results\": {\n      \"status\": \"DONE_IN_REGISTRY\",\n      \"registry_ref\": \"exp_017_llama_conll_infer\",\n      \"actual_metrics\": {\n        \"sj_rho_full\": 0.4314,\n        \"fk_rho_full\": 0.4277,\n        \"lp_rho_full\": 0.3072,\n        \"greedy_f1\": 0.9266,\n        \"oracle_headroom\": 0.0177\n      },\n      \"worst_tier_reinterpretation\": \"LLaMA CoNLL SJ rho=0.431 matches Qwen CoNLL rho=0.436. Cross-model consistency 强，但在 worst tier 下这同时意味着 degeneracy pattern (high F1 → high degeneracy) 也跨模型一致—— 不是 Qwen-specific artifact 而是 5-epoch LoRA fine-tuning 的通用效应。 如果对 LLaMA 也做 rank=8 ablation，预期同样会看到 degeneracy 大幅下降。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"exp-017 无需新实验。Worst tier 仅改变解释框架： LLaMA+CoNLL 的 high degeneracy 归因于 fine-tuning regime 而非 model capability。Cross-model consistency 反而 strengthens worst tier 论点——两个不同架构 (Qwen3, LLaMA-3.1) 在相同 fine-tuning 强度下产生相同的 convergence pattern。\\n\\n\\n已完成实验，不需要 prediction。在 worst tier 下重新解读： LLaMA 复现了 Qwen 的 CoNLL pattern (greedy_f1=0.927, 高 degeneracy, selection 无效, oracle headroom 仅 1.77pp)。 这原本被解释为 \\\"capability trap is model-agnostic\\\"， 但现在应解释为 \\\"aggressive fine-tuning (5 epochs, rank=32 for LLaMA) consistently produces high degeneracy regardless of model architecture.\\\" Cross-model validation 的含义从 \\\"capability trap is universal\\\" 变为 \\\"fine-tuning-induced convergence is universal.\\\" 证据相同，解释不同。\\n\"\n  },\n  {\n    \"name\": \"exp-024: claim_audit\",\n    \"description\": \"Systematic cross-chapter numerical consistency audit. 在 worst tier 下检查所有 claims 与新实验数据的一致性, 识别需要 rewrite 的 sections.\\n\",\n    \"results\": {\n      \"total_inconsistencies_found\": 8,\n      \"critical\": 5,\n      \"moderate\": 2,\n      \"minor\": 1,\n      \"critical_inconsistencies\": [\n        {\n          \"id\": \"CA-1\",\n          \"location\": \"Abstract + Introduction\",\n          \"current_claim\": \"'universally fail to select better candidates'\",\n          \"contradicting_evidence\": \"Few-NERD LP +3.2pp (p=0.028); rank=8 LP +3.6pp (p=0.015)\",\n          \"fix\": \"'fail to select under high-convergence regimes; succeed when output diversity is preserved'\"\n        },\n        {\n          \"id\": \"CA-2\",\n          \"location\": \"Discussion line 3 vs Limitations line 8\",\n          \"current_claim\": \"'+0.1pp over single-sample' vs '+0.4pp over greedy'\",\n          \"contradicting_evidence\": \"exp_016_rerun_1024: LP selection +0.6pp (n.s., p=0.39)\",\n          \"fix\": \"unify to '+0.6pp, not significant (bootstrap p=0.39, CI [-0.030, +0.042])'\"\n        },\n        {\n          \"id\": \"CA-3\",\n          \"location\": \"Section 4.4 Capability Trap\",\n          \"current_claim\": \"'structural inevitability: the better the model, the less TTS helps'\",\n          \"contradicting_evidence\": \"R2=0.51 (4 datasets); rank=8 F1=0.625 with degen=5.2%\",\n          \"fix\": \"'one factor among several; fine-tuning intensity is the primary driver of degeneracy'\"\n        },\n        {\n          \"id\": \"CA-4\",\n          \"location\": \"Claim 1 PRIMARY\",\n          \"current_claim\": \"'diagnose two failure mechanisms and a unifying capability trap'\",\n          \"contradicting_evidence\": \"Few-NERD + rank=8 break capability trap; provide positive selection examples\",\n          \"fix\": \"'diagnose conditions under which each mechanism activates; convergence drivers include FT intensity, entity density, task complexity'\"\n        },\n        {\n          \"id\": \"CA-5\",\n          \"location\": \"Story Spine headline\",\n          \"current_claim\": \"'T=0 greedy dominates all multi-sample strategies at zero cost'\",\n          \"contradicting_evidence\": \"Few-NERD: LP +3.2pp > greedy (p=0.028); rank=8: LP +3.6pp > greedy (p=0.015)\",\n          \"fix\": \"'T=0 greedy dominates under standard fine-tuning regimes, but multi-sample LP selection recovers 3-4pp when output diversity is preserved'\"\n        }\n      ],\n      \"moderate_inconsistencies\": [\n        {\n          \"id\": \"CA-6\",\n          \"location\": \"Scale ablation (4B)\",\n          \"current_claim\": \"'4B degeneracy 10.4% supports capability trap'\",\n          \"contradicting_evidence\": \"rank=8 provides alternative explanation (FT intensity, not capability)\",\n          \"fix\": \"acknowledge confound: 4B lower degeneracy may reflect both reduced capability AND different convergence dynamics\"\n        },\n        {\n          \"id\": \"CA-7\",\n          \"location\": \"SJ claims throughout\",\n          \"current_claim\": \"'SJ clearly beats LP on NER (rho +0.15-0.22)'\",\n          \"contradicting_evidence\": \"3-seed Fisher p=0.085 (borderline); seed 789 gap only 0.057\",\n          \"fix\": \"soften to 'SJ tends to outperform LP on NER (p=0.085); VC>LP is more robust (p=0.018)'\"\n        }\n      ],\n      \"minor_inconsistencies\": [\n        {\n          \"id\": \"CA-8\",\n          \"location\": \"Figure 4 caption\",\n          \"current_claim\": \"'monotonic relationship between F1 and degeneracy'\",\n          \"contradicting_evidence\": \"R2=0.51 with Few-NERD, R2=0.35 with rank=8 data point\",\n          \"fix\": \"update caption to reflect weak-to-moderate relationship\"\n        }\n      ],\n      \"narrative_changes\": {\n        \"old_title\": \"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\",\n        \"new_title\": \"When Does Multi-Sample Selection Help Structured IE? A Diagnostic Study of Output Convergence\",\n        \"old_primary_claim\": \"universal failure + capability trap as unifying framework\",\n        \"new_primary_claim\": \"conditional effectiveness: selection fails under high-convergence regimes, succeeds with output diversity\",\n        \"old_paper_type\": \"novel insight (negative result) paper\",\n        \"new_paper_type\": \"large-scale empirical study with prescriptive guidelines\",\n        \"sections_requiring_major_rewrite\": [\n          \"Abstract (remove 'universally', add conditions, mention positive Few-NERD/rank=8 results)\",\n          \"Introduction (reframe as conditional study, not universal negative)\",\n          \"Section 4.4 retitle: 'Output Convergence Drivers' (not 'Capability Trap')\",\n          \"New Section 4.5: 'When Does Selection Succeed? — Prescriptive Guidelines'\",\n          \"Discussion (trade-off analysis: F1 cost vs selection gain; practical recommendations)\",\n          \"Conclusion (actionable takeaways for practitioners)\"\n        ],\n        \"sections_minor_edits\": [\n          \"Section 3 (add Few-NERD dataset description)\",\n          \"Section 4.1 (add Few-NERD QE results)\",\n          \"Section 4.2 (add Few-NERD selection results)\",\n          \"Section 4.3 (add rank=8 ablation subsection)\",\n          \"Related Work (reframe positioning vs TTS scaling literature)\"\n        ]\n      },\n      \"capability_trap_r2_progression\": {\n        \"three_datasets\": 0.98,\n        \"four_datasets_with_fewnerd\": 0.51,\n        \"five_points_with_rank8\": 0.35\n      },\n      \"prescriptive_guidelines\": [\n        {\n          \"condition\": \"degeneracy < 10% AND LP range > 0.07 nats\",\n          \"recommendation\": \"use LP-based best-of-N selection (expected gain 2-4pp)\",\n          \"evidence\": \"Few-NERD (+3.2pp), rank=8 SciERC (+3.6pp)\"\n        },\n        {\n          \"condition\": \"degeneracy > 20%\",\n          \"recommendation\": \"use T=0 greedy (zero additional cost)\",\n          \"evidence\": \"SciERC rank=16 (+0.6pp n.s.), CoNLL (-1.0pp)\"\n        },\n        {\n          \"condition\": \"10% < degeneracy < 20%\",\n          \"recommendation\": \"evaluate on dev set; marginal expected gain\",\n          \"evidence\": \"borderline regime, outcome depends on specific dataset\"\n        },\n        {\n          \"condition\": \"RE with >40% zero-F1 instances\",\n          \"recommendation\": \"no unsupervised signal reliably helps; consider supervised verifier\",\n          \"evidence\": \"RE rankings unstable across all seeds\"\n        }\n      ]\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table A1: Claim Audit Summary\",\n        \"columns\": [\n          \"ID\",\n          \"Severity\",\n          \"Location\",\n          \"Issue\",\n          \"Fix\"\n        ],\n        \"rows\": [\n          [\n            \"CA-1\",\n            \"CRITICAL\",\n            \"Abstract\",\n            \"universally fail vs 2 positive results\",\n            \"add conditions\"\n          ],\n          [\n            \"CA-2\",\n            \"CRITICAL\",\n            \"Disc/Lim\",\n            \"+0.1pp vs +0.4pp vs actual +0.6pp\",\n            \"unify numbers\"\n          ],\n          [\n            \"CA-3\",\n            \"CRITICAL\",\n            \"Sec 4.4\",\n            \"structural inevitability vs R2=0.51\",\n            \"reframe as one factor\"\n          ],\n          [\n            \"CA-4\",\n            \"CRITICAL\",\n            \"Claim 1\",\n            \"universal failure framing\",\n            \"conditional framing\"\n          ],\n          [\n            \"CA-5\",\n            \"CRITICAL\",\n            \"Headline\",\n            \"greedy dominates all vs 2 exceptions\",\n            \"add regime qualifier\"\n          ],\n          [\n            \"CA-6\",\n            \"MODERATE\",\n            \"4B section\",\n            \"4B degen interpretation confound\",\n            \"acknowledge\"\n          ],\n          [\n            \"CA-7\",\n            \"MODERATE\",\n            \"SJ claims\",\n            \"SJ>LP p=0.085 borderline\",\n            \"soften claim\"\n          ],\n          [\n            \"CA-8\",\n            \"MINOR\",\n            \"Fig 4 cap\",\n            \"monotonic claim vs R2=0.51\",\n            \"update\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table A2: Prescriptive Decision Matrix\",\n        \"columns\": [\n          \"Degeneracy\",\n          \"LP_Range_nats\",\n          \"Recommendation\",\n          \"Expected_Gain_pp\"\n        ],\n        \"rows\": [\n          [\n            \"< 10%\",\n            \"> 0.07\",\n            \"LP best-of-N\",\n            \"2-4\"\n          ],\n          [\n            \"10-20%\",\n            \"0.04-0.07\",\n            \"Evaluate on dev\",\n            \"0-2\"\n          ],\n          [\n            \"> 20%\",\n            \"< 0.04\",\n            \"T=0 greedy\",\n            \"0\"\n          ],\n          [\n            \"any (RE >40% zero-F1)\",\n            \"any\",\n            \"Supervised verifier or greedy\",\n            \"0 unsupervised\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim audit 输出一个 comprehensive rewrite checklist。 核心变化不是 patch individual numbers——是叙事重构。\\n好消息：所有已有实验数据（free-form ablation、scale ablation、 cross-model validation、temperature analysis）不受影响。 它们仍然是 valid empirical contributions。 转向只需要重新 frame 这些数据的 interpretation。\\nFree-form ablation 仍证明 LP compression is model-intrinsic (在 high-convergence regime 下)。Scale ablation 仍证明 cross-scale consistency。Cross-model 仍证明 cross-architecture generalization。\\n新 framing 有更清晰的层次： Layer 1 (QE): confidence signals reliably estimate quality — robust across regimes. Layer 2 (Selection): selection effectiveness depends on output convergence. Layer 3 (Convergence drivers): FT intensity > entity density > task complexity > capability. Layer 4 (Guidelines): prescriptive decision matrix for practitioners.\\n从 \\\"interesting negative finding\\\" 升级为 \\\"prescriptive empirical study\\\"， 对 EMNLP Main Conference fit 可能反而更好—— actionable findings 比 pure diagnostics 更 impactful。\\nTitle 变更 essential： \\\"Strong Predictors, Weak Selectors\\\" → \\\"When Does Multi-Sample Selection Help\\\" 反映从 universal negative 到 conditional study 的根本转向。\\n\\nClaim audit 在 worst tier 下揭示 8 处不一致，其中 5 处 critical。 核心问题：现有文本围绕 \\\"universal failure + capability trap\\\" 构建， 但 Few-NERD 和 LoRA rank=8 直接推翻了 universality 和 structural inevitability。\\nCA-1 是最高优先级：Abstract 的 \\\"universally fail\\\" 被两个 statistically significant 正结果 (p=0.028, p=0.015) 直接否定。 如果保留 \\\"universally fail\\\"，reviewer 会立即指出与 Results section 的 internal contradiction。\\nCA-2 是 legacy 不一致，需要统一数字。\\nCA-3 是叙事核心变化：capability trap 从 unifying framework 降级为 one-of-several factors。R²=0.51 (4 datasets) 和 0.35 (5 points) 说明 F1 只解释 35-51% 的 degeneracy 方差。\\nCA-4 需要重构 Claim 1 从 \\\"why selection fails\\\" 到 \\\"when selection fails/succeeds and what drives the boundary\\\"。\\nCA-5 headline 变化反映从 pure negative 到 conditional finding。\\nPrescriptive guidelines 是 worst tier 最大的新贡献—— 给 practitioners 具体的 decision criteria： 观察 degeneracy rate 和 LP range，决定是否使用 multi-sample 策略。 这比 \\\"selection always fails\\\" 有更大的 practical value。\\n\"\n  }\n]",
      "numLines": 1162,
      "startLine": 1,
      "totalLines": 1162
    }
  },
  "sourceToolAssistantUUID": "a20e9056-1b8c-4fc2-bf25-1de99057b88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "a541c3fc-cb4e-4a35-92b5-02a4c036be6a",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Tool result

_source line 11 · 2026-05-16T09:58:02.239Z_

<details><summary>↩ Tool result · `toolu_013zN9huArANfRPtmHDveaRm`</summary>

```text
1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。
4	
5	## Target Venue
6	- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (4 layers, D112 updated — Main Conference framing with capability trap + degeneracy)
10	
11	### Claim 1 (PRIMARY — Diagnosing Two Failure Mechanisms + Capability Trap)
12	Confidence signals reliably predict output quality across instances (AUROC up to 0.82, ρ up to 0.45) but universally fail to select better candidates from multiple samples. We diagnose **two failure mechanisms** and a unifying **capability trap** that explains why the gap is structurally inevitable for capable models.
13	
14	**Three-layer argument + Capability Trap**:
15	- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the "methodological premise" — not an empirical finding.
16	- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. T=0 greedy dominates all signals (greedy F1=0.663 > best LP selection 0.647 on SciERC) — zero-cost strongest argument.
17	- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).
18	- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an "artifact" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.
19	
20	**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.
21	
22	**Key evidence (score compression)**:
23	- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
24	- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
25	- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it
26	
27	**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:
28	- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)
29	- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)
30	- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)
31	- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)
32	- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)
33	- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)
34	- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.
35	
36	**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:
37	- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)
38	- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)
39	- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales
40	- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.
41	- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust
42	- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B
43	- **4B selection results** (correlation-selection gap at 4B):
44	  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)
45	  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**
46	  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B
47	- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.
48	- **Paper framing**: "Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity."
49	
50	**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.
51	
52	**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.
53	
54	**Implications**: Not just "signals don't work" but "here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints)."
55	
56	### Claim 2 (METHODOLOGY — QE Evaluation Framework)
57	Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.
58	
59	**Key results**:
60	- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122
61	- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures "did the model get any relations right" better than structural overlap measures.
62	- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
63	- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.
64	- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.
65	
66	**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
67	- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
68	- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
69	- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706
70	
71	### Claim 2b (Selection evidence)
72	**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):
73	- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
74	- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)
75	
76	**4B selection evidence** (N=8, T=1.0):
77	- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable
78	- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed
79	
80	**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
81	- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
82	- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466
83	
84	### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)
85	The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.
86	
87	**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures "complete failure vs partial success" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just "compound error" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.
88	
89	**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.
90	
91	**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.
92	
93	**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
94	- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
95	- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
96	- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
97	- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.
98	
99	## Story Spine (D112 — Two Failure Mechanisms + Capability Trap, Main Conference)
100	
101	**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?
102	
103	**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection. Eikema et al.'s MBR failure stems from utility misalignment; our work reveals a qualitatively novel failure mode.
104	
105	**Our framing (D112 — "two failure mechanisms + capability trap")**:
106	
107	We systematically compare five confidence signals for IE and diagnose **why** unsupervised selection universally fails:
108	1. **Methodological premise**: Four of five signals are instance-level by construction and cannot rank candidates — a definitional property, not discovered empirically.
109	2. **Failure Mechanism 1 — Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples. Within-instance signals ARE correlated (ρ=0.524) but degeneracy eliminates headroom. Non-degenerate subset: MBR closes 23-41% of oracle gap. T=0 greedy dominates all signals (0.663 > 0.647 best LP) — zero additional inference cost.
110	3. **Failure Mechanism 2 — LP Compression**: Logprob's within-instance range is compressed (median 0.041 nats). Entity-token LP shows 4× variance but produces WORSE selection (-2.0pp). Free-form decoding ablation confirms compression is intrinsic (std ratio 0.97), not caused by constrained decoding.
111	4. **Capability Trap** (unifying): Model capability → convergence → degeneracy → vanishing headroom. CoNLL (91% F1) → 58% degen, SciERC (66%) → 21%, WNUT (48%) → ~0%. Scale: 8B 21% vs 4B 10.4%. The better the model, the less test-time scaling helps — a structural inevitability, not an artifact.
112	5. **Path forward**: Breaking the capability trap requires fundamentally different approaches (trained verifiers, multi-round refinement). The non-tied subset (+2.9pp, p=0.01) proves LP selection works WHERE degeneracy is absent.
113	
114	**Headline**: "We diagnose why confidence signals that reliably predict structured IE output quality (AUROC 0.82, ρ 0.45) universally fail to select better candidates. Two mechanisms — instance degeneracy and logprob compression — are unified by a capability trap: the better the model, the more outputs converge, eliminating selection headroom. T=0 greedy dominates all multi-sample strategies at zero cost."
115	
116	**Title**: "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction"
117	
118	## Anticipated Reviewer Concerns
119	
120	### R1: "Only one NER dataset — generalization unclear"
121	- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
122	- **Priority**: P0
123	
124	### R2: "Only one model family (Qwen3-8B)"
125	- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。
126	- **Priority**: P0
127	
128	### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
129	- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).
130	- **Priority**: P0, RESOLVED — results decisive
131	
132	### R3b: "EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?"
133	- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.
134	- **Priority**: P1 — narrative adjusted for 1024-token results
135	
136	### R4: "No actual TTS improvement demonstrated"
137	- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.
138	- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
139	- **Priority**: P0 — narrative pivot complete, bootstrap confirms
140	
141	### R5: "Sample size N=8 may be too small for reliable SJ estimation"
142	- **Mitigation**: exp-001 (N=16) with multi-seed robustness
143	- **Priority**: P0
144	
145	### R6: "Conditional analysis cherry-picks favorable instances"
146	- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
147	- **Priority**: P0 (add sensitivity analysis)
148	
149	### R7: "Only ρ as evaluation metric"
150	- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).
151	- **Priority**: P0
152	
153	### R8: "Formula-implementation discrepancy"
154	- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
155	- **Priority**: P0, paper writing fix
156	
157	### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
158	- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
159	- **Priority**: P0
160	
161	### R10: "Insufficient related work" (三档一致 [B][M][W])
162	- **Mitigation**: Expand to 35+ references. Must cite:
163	  - USC (Chen 2024) — empirical differentiation, not just citation
164	  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
165	  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
166	  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
167	  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
168	  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
169	  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
170	  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
171	  - **IE confidence**: Culotta & McCallum 2004
172	  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
173	  - **[2025-2026 新颖性自查补充 — 必引]**:
174	    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
175	    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
176	    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
177	    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
178	    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
179	  - **[2025-2026 新颖性自查补充 — 应引]**:
180	    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
181	    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
182	    - Semantic Entropy Probes (2024) — 低成本不确定性估计
183	    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
184	    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
185	    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
186	    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
187	    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
188	    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
189	  - **需新增 Related Work 小节**:
190	    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
191	    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
192	- **Priority**: P0, Paper Agent handles
193	
194	### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
195	- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:
196	  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078
197	  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706
198	  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)
199	  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.
200	- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)
201	
202	### R12: "No supervised upper bound / reward model comparison" (Dream 2)
203	- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the "so what": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.
204	- **Priority**: P1, addressed via framing (future work motivated by ablation)
205	
206	### R13: "Headroom capture rate low" (Dream 2)
207	- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
208	- **Priority**: P0, paper writing
209	
210	### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
211	- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.
212	- **Priority**: P0, RESOLVED
213	
214	### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
215	- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
216	- **Priority**: P0, Paper Agent handles
217	
218	### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
219	- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
220	- **Priority**: P0, Paper Agent handles
221	
222	### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
223	- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
224	- **Priority**: P0, Paper Agent handles
225	
226	### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
227	- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
228	- **Priority**: P1, Paper Agent handles
229	
230	### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
231	- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
232	- **Priority**: P1, Paper Agent handles
233	
234	## Venue Fit
235	
236	EMNLP **Main Conference** target. Strengths:
237	- Systematic empirical comparison with mechanistic diagnosis (not just "signals don't work" but "here's exactly why")
238	- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight
239	- Controlled ablation (free-form decoding) providing causal evidence
240	- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation
241	
242	Main Conference gap vs Findings:
243	- **Need**: 3rd NER dataset (Few-NERD) to close "only 2 NER datasets" concern
244	- **Need**: 3rd seed for Fisher p-value power on key claims
245	- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy
246	- **Need**: Systematic claim audit resolving numerical contradictions
247	
248	Risk assessment:
249	- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy
250	- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)
251	- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3cdc9f2f-07f7-4613-b0f8-f9c584e6b27e",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "16f59a4f-1577-43dd-9cf7-6164a89c54a9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper_framing.md",
      "content": "# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\n\n## Target Venue\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (4 layers, D112 updated — Main Conference framing with capability trap + degeneracy)\n\n### Claim 1 (PRIMARY — Diagnosing Two Failure Mechanisms + Capability Trap)\nConfidence signals reliably predict output quality across instances (AUROC up to 0.82, ρ up to 0.45) but universally fail to select better candidates from multiple samples. We diagnose **two failure mechanisms** and a unifying **capability trap** that explains why the gap is structurally inevitable for capable models.\n\n**Three-layer argument + Capability Trap**:\n- Layer A (design property, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification — the \"methodological premise\" — not an empirical finding.\n- Layer B (empirical — instance degeneracy): 21-58% of instances produce identical F1 across all N samples, eliminating selection headroom. Within-instance ρ=0.524 (SciERC) and 0.994 (CoNLL) — signals ARE correlated within instances, but degeneracy makes this irrelevant. Non-degenerate instances show MBR closing 23-41% of oracle gap. T=0 greedy dominates all signals (greedy F1=0.663 > best LP selection 0.647 on SciERC) — zero-cost strongest argument.\n- Layer C (empirical — LP compression): Logprob — the only per-sample signal — fails due to intrinsic score compression (median within-instance LP range = 0.041 nats). Entity-token LP shows 4× variance but WORSE selection (-2.0pp). Free-form ablation confirms compression is model/task intrinsic (std ratio 0.97).\n- **Capability Trap** (unifying insight, D111): Model capability → output convergence → instance degeneracy → vanishing selection headroom. Evidence: CoNLL (91% F1) → 58% degeneracy, SciERC (66% F1) → 21%, WNUT (48% F1) → ~0%. Scale dimension: 8B → 21% degen vs 4B → 10.4% on SciERC. This is NOT an \"artifact\" — it is a **consequence of capability**, a structural inevitability. The better the model, the less test-time scaling can help via unsupervised selection.\n\n**Distinction from MBR literature**: Eikema et al.'s MBR failure = utility function misalignment. Our failure = utility IS aligned (within-instance ρ=0.524) but headroom eliminated by degeneracy — qualitatively novel mechanism.\n\n**Key evidence (score compression)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it\n\n**Key evidence (free-form ablation)** [DONE — exp_freeform_ablation, NEGATIVE]:\n- LP distribution: constrained std=0.0206, free-form std=0.0199 (ratio 0.97, virtually unchanged)\n- Tied fraction: 59.7% → 57.7% (-2.0pp, negligible)\n- NER selection: +0.59pp → +0.18pp (both negligible vs greedy)\n- RE selection: -0.68pp → +1.69pp (flipped positive — secondary finding)\n- NER VC rho: 0.379 → 0.409 (slight QE improvement, selection still fails)\n- Parse rate: 99.95% (fine-tuned model retains JSON format without grammar)\n- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.\n\n**Key evidence (scale ablation)** [DONE — 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}]:\n- CoNLL NER: 4B greedy_f1=0.9234 (>8B 0.9123, +1.11pp), SJ_ρ=0.4217 (≈8B 0.4357, −1.4pp), FK_ρ=0.4181 (>8B 0.3998, +1.83pp)\n- SciERC NER: 4B SJ_ρ=0.4221 (>8B 0.3825, +3.96pp), FK_ρ=0.3258 (>8B 0.2590, +6.68pp)\n- SciERC RE: 4B SJ_ρ=0.2673 (>8B 0.2441, +2.32pp), FK_ρ=0.3593 (>8B 0.2782, +8.11pp); struct>surface ✗ at both scales\n- **Conclusion**: Correlation strength maintained or improved at 4B across all 4 cells. The gap originates from within-instance signal misalignment, not model capacity. Task difficulty (SciERC RE zero-F1 rate) remains the primary driver, consistent across scales.\n- CoNLL 4B headroom: 1.70pp (vs 8B 4.20pp) → MARGINAL for selection power, but QE correlations robust\n- SciERC RE 4B: 47.6% zero-F1, RE LP_ρ_cond=0.1135 (p=0.074, n.s.) → confirms binary dominance at 4B\n- **4B selection results** (correlation-selection gap at 4B):\n  - CoNLL NER 4B (n=2756): SJ +0.07pp, FK +0.03pp, LP +0.09pp vs greedy 0.9213. All ≤0.1pp — MARGINAL (headroom 1.70pp)\n  - SciERC NER 4B (n=529): SJ **-1.49pp**, FK -1.56pp, LP -2.23pp vs greedy 0.6622. Oracle 0.7925 (+13.02pp). **All signals WORSE than greedy despite 13pp oracle headroom — gap confirmed at 4B**\n  - SciERC NER 4B gap demonstration: SJ-FK ρ gap = +0.096 (strong correlation advantage), SJ-FK selection F1 gap = +0.0007 (zero selection advantage) → correlation-selection gap quantified at 4B\n- **n_samples confound control**: Qwen3-8B n=8 data exists as control. CoNLL SJ: n8 ρ=0.4389 → n16 ρ=0.4496 (Δ=0.011, CI crosses zero). SciERC SJ: n8→n16 Δ=0.066, CI=[0.004, 0.128] weak effect. n_samples not a confound for 4B-8B comparison.\n- **Paper framing**: \"Scale ablation shows the gap is not an artifact of a particular model size; correlation strength is maintained at 4B, confirming that the gap originates from within-instance signal misalignment rather than model capacity.\"\n\n**exp-019 supervised verifier**: SKIPPED (Reviewer recommendation). Reasons: DDL 10 days, scope creep risk (analytical paper + solution = type mismatch), exp-016 LR ensemble already underperforms EM (0.666 vs 0.749). Verifier is follow-up paper material.\n\n**Bonus finding (parse rate)**: Free-form parse rate 99.95% (4406/4408) — fine-tuned 8B model generates valid JSON without grammar constraints. Challenges intro:19 claim about constrained decoding necessity for format compliance.\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation via elimination), and here's the forward direction (breaking LP compression requires fundamentally different approaches — trained verifiers, multi-round refinement — not simply relaxing decoding constraints).\"\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205). 3-seed consistent: SJ > FK delta=0.093~0.122\n- RE (3-seed confirmed): **LP > SJ > FK** (mean ρ: LP 0.302, SJ 0.265, FK 0.254). Signal ranking reverses vs NER — structural signals lose advantage when 43-45% of RE samples have F1=0 (binary signal dominance). LP's coarse but stable generation-confidence signal captures \"did the model get any relations right\" better than structural overlap measures.\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09. T=0.7: LP full ρ improves 0.205→0.249, LP cond ρ 0.154→0.185; FK 0.267→0.289 despite more compression → concentrated signal hypothesis (non-tied instances at lower T carry more informative variance). **Paper citation rule**: robustness/temperature tables use full ρ; score compression analysis uses cond ρ. Always annotate which variant.\n- **Task-dependent signal effectiveness** (new finding from RE 3-seed): The optimal signal family depends on task structure. NER (token-level, graded F1) → structural agreement captures quality gradients. RE (relation-level, binary-dominated F1) → logprob captures generation confidence better. This is NOT a weakness — it's a nuanced finding that enriches the diagnostic framework.\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC 8B, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**4B selection evidence** (N=8, T=1.0):\n- CoNLL NER 4B (n=2756): greedy 0.9213, SJ 0.9220 (+0.07pp), FK 0.9215, LP 0.9221 (+0.09pp), oracle 0.9382. Headroom 1.70pp → selection indistinguishable\n- SciERC NER 4B (n=529): greedy 0.6622, SJ 0.6473 (-1.49pp), FK 0.6466 (-1.56pp), LP 0.6399 (-2.23pp), oracle 0.7925 (+13.02pp). **All signals worse than greedy** → correlation-selection gap at 4B confirmed\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary + task-dependent signal effectiveness)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**RE 3-seed mechanism** (D073, confirmed at 4B): 43-47% of RE samples have F1=0 (8B: 43-45%, 4B: 47.6%), creating binary-dominated signal distributions where structural overlap (SJ/FK) cannot differentiate quality gradients. Pattern consistent across model scales — confirming task difficulty, not model capacity, drives this boundary. LP's generation confidence captures \"complete failure vs partial success\" more reliably. 3-seed RE QE: LP ρ=0.302 > SJ 0.265 > FK 0.254. **Definitive binary dominance evidence**: RE LP full ρ=0.266 but cond ρ=0.011 (p=0.86, completely n.s.) — LP's entire RE signal comes from the zero/nonzero F1 split; once conditioned on samples where the model extracts at least one relation, LP has zero predictive power for RE quality gradients. In contrast, NER LP cond ρ remains informative (0.154–0.185). This provides the concrete mechanism for Claim 3's task-complexity boundary: it's not just \"compound error\" in the abstract — it's specifically the high zero-F1 rate that shifts the optimal signal family from structural to probabilistic, and LP's RE advantage is entirely a binary classification effect, not genuine quality estimation.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D112 — Two Failure Mechanisms + Capability Trap, Main Conference)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) present a fundamentally different challenge — and prior work conflates quality estimation with selection. Eikema et al.'s MBR failure stems from utility misalignment; our work reveals a qualitatively novel failure mode.\n\n**Our framing (D112 — \"two failure mechanisms + capability trap\")**:\n\nWe systematically compare five confidence signals for IE and diagnose **why** unsupervised selection universally fails:\n1. **Methodological premise**: Four of five signals are instance-level by construction and cannot rank candidates — a definitional property, not discovered empirically.\n2. **Failure Mechanism 1 — Instance Degeneracy**: 21-58% of instances produce identical F1 across all N samples. Within-instance signals ARE correlated (ρ=0.524) but degeneracy eliminates headroom. Non-degenerate subset: MBR closes 23-41% of oracle gap. T=0 greedy dominates all signals (0.663 > 0.647 best LP) — zero additional inference cost.\n3. **Failure Mechanism 2 — LP Compression**: Logprob's within-instance range is compressed (median 0.041 nats). Entity-token LP shows 4× variance but produces WORSE selection (-2.0pp). Free-form decoding ablation confirms compression is intrinsic (std ratio 0.97), not caused by constrained decoding.\n4. **Capability Trap** (unifying): Model capability → convergence → degeneracy → vanishing headroom. CoNLL (91% F1) → 58% degen, SciERC (66%) → 21%, WNUT (48%) → ~0%. Scale: 8B 21% vs 4B 10.4%. The better the model, the less test-time scaling helps — a structural inevitability, not an artifact.\n5. **Path forward**: Breaking the capability trap requires fundamentally different approaches (trained verifiers, multi-round refinement). The non-tied subset (+2.9pp, p=0.01) proves LP selection works WHERE degeneracy is absent.\n\n**Headline**: \"We diagnose why confidence signals that reliably predict structured IE output quality (AUROC 0.82, ρ 0.45) universally fail to select better candidates. Two mechanisms — instance degeneracy and logprob compression — are unified by a capability trap: the better the model, the more outputs converge, eliminating selection headroom. T=0 greedy dominates all multi-sample strategies at zero cost.\"\n\n**Title**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: LLaMA-3.1-8B shows model-agnostic effect. ⚠️ **exp-007 数据被污染 (test data leakage)**，LLaMA SciERC 正确值来自 exp_018 (clean rerun)。unified_rho_full.json 的 LLaMA SciERC 条目必须替换为 exp_018 数据。正确 LLaMA SciERC N=8 3-seed mean: SJ 0.325, FK 0.256, VC 0.384, EM 0.279, LP 0.162。\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: exp-016 LR ensemble (5-signal, 5-fold CV) underperforms best single signal EM (AUROC 0.666 vs 0.749), suggesting feature redundancy. exp-019 supervised verifier SKIPPED (DDL risk + scope creep). Free-form ablation provides the \"so what\": gap is fundamental → closing it requires fundamentally different approaches (trained verifiers, not just better unsupervised signals). Positioned as future work with explicit motivation from ablation evidence.\n- **Priority**: P1, addressed via framing (future work motivated by ablation)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Status**: ✅ RESOLVED by 4B scale ablation. 2×2 matrix: {CoNLL, SciERC} × {Qwen3-8B, Qwen3-4B}. All correlation metrics maintained or improved at 4B (e.g. SciERC NER SJ_ρ: 0.3825→0.4221, +3.96pp). Combined with LLaMA-3.1-8B cross-architecture data, now have 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B). 70B infeasible — acknowledge as limitation.\n- **Priority**: P0, RESOLVED\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP **Main Conference** target. Strengths:\n- Systematic empirical comparison with mechanistic diagnosis (not just \"signals don't work\" but \"here's exactly why\")\n- Two novel failure mechanisms (instance degeneracy + LP compression) + unifying capability trap insight\n- Controlled ablation (free-form decoding) providing causal evidence\n- Cross-model (Qwen3-8B/4B + LLaMA-3.1-8B), cross-dataset (SciERC + CoNLL + WNUT), cross-task (NER + RE) validation\n\nMain Conference gap vs Findings:\n- **Need**: 3rd NER dataset (Few-NERD) to close \"only 2 NER datasets\" concern\n- **Need**: 3rd seed for Fisher p-value power on key claims\n- **Need**: LoRA rank=8 ablation to confirm fine-tuning degree doesn't drive degeneracy\n- **Need**: Systematic claim audit resolving numerical contradictions\n\nRisk assessment:\n- **Strongest asset**: Capability trap is a genuinely novel insight — no prior work connects model capability to vanishing TTS headroom via degeneracy\n- **Weakest flank**: Dataset breadth (2 NER + 1 RE → 3 NER + 1 RE with Few-NERD)\n- **Critical path**: Few-NERD + 3rd seed experiments must complete before DDL (2026-05-25, 9 days)",
      "numLines": 251,
      "startLine": 1,
      "totalLines": 251
    }
  },
  "sourceToolAssistantUUID": "3cdc9f2f-07f7-4613-b0f8-f9c584e6b27e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "16f59a4f-1577-43dd-9cf7-6164a89c54a9",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260516T092241",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Assistant

_source line 14 · 2026-05-16T10:00:02.455Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now carefully synthesize the experiment data and paper framing to write a complete LaTeX paper. Let me understand the key narrative:

1. The paper was originally framed as "universal failure + capability trap" but the worst-tier narrative guidance says to reframe as conditional study: "When Does Multi-Sample Selection Help Structured IE?"
2. Core shift: selection fails under high-convergence regimes but succeeds when output diversity is preserved
3. LP compression still holds (free-form ablation evidence)
4. Instance degeneracy becomes "controllable artifact of training configuration" not "inevitable consequence of capability"


5. The paper now becomes prescriptive—laying out the specific conditions where multi-sample strategies actually work

I need to structure the experiments strategically: Few-NERD gets the main treatment with both a quick validation and full results showing how selection breaks through the capability trap, then I'll use the SciERC seed replication to demonstrate stability, the LoRA ablation to establish that fine-tuning intensity directly causes degeneracy, and cross-model results to show generalization. The claim audit will ground everything in what we can actually support.

Now I'm pulling together all the empirical evidence—the NER and RE metrics from SciERC, the CoNLL and WNUT numbers, the ablation results across different scales and temperatures, and the N-scaling patterns—to build the paper's narrative. I'm organizing this into a clear structure: abstract and introduction to frame the problem, related work to position the contribution, then the method section covering our diagnostic signals and experimental setup, followed by the core experiments section with convergence analysis and ablations, and finally discussion that translates findings into actionable guidelines.

Writing the paper now with a title that captures the core insight about output convergence... me outline the sections:
1. Abstract
2. Introduction - reframed as conditional study
3. Related Work
4. Method
   4.1 Confidence Signals (5 signals)
   4.2 Datasets (SciERC, CoNLL-2003, Few-NERD, WNUT-17)
   4.3 Experimental Setup (models, LoRA, inference)
5. Results
   5.1 Quality Estimation (QE correlation results across datasets)
   5.2 Selection Effectiveness (best-of-N results)
   5.3 Output Convergence Analysis (degeneracy, LP compression)
   5.4 Convergence Drivers (not capability trap - FT intensity, entity density)
   5.5 LoRA Rank Ablation (causal evidence)
   5.6 Prescriptive Guidelines
6. Discussion
7. Conclusion

Now I'm looking at the QE correlation results across the different datasets and signal types. The metrics show varying performance - variance-based signals like VC tend to perform well, while LP shows more modest correlations. I'm seeing consistent patterns across SciERC NER and RE tasks, with Few-NERD showing similar trends, which suggests these findings generalize across different NER benchmarks.

For the selection results, I'm examining how well the best-performing signals can actually improve model outputs when used to select from multiple generations. The improvements are modest but statistically significant in some cases - particularly for Few-NERD and SciERC at rank 8, though CoNLL shows no improvement, which is interesting given its already high baseline performance.

The degeneracy analysis is where things get more complex - I need to understand what's driving the convergence patterns and whether it's actually a limitation or just a natural outcome of the task structure.

Now I'm looking at the compression metrics and capability trap results to understand how the model's internal representations are changing across these different datasets and configurations. The R² values suggest the relationship between dataset size and performance breaks down once I include Few-NERD, which hints at something more fundamental about how these models generalize. I should write this up carefully with all the numbers intact.

For the paper structure, I need to organize seven tables covering dataset statistics, NER and RE quality estimation results, selection outcomes, convergence analysis, ablation studies, and a decision matrix. The challenge is that my experimental data comes from multiple sources—the newer experiments are in one file while the older baseline results are scattered across my framing notes, so I'll need to synthesize both to tell the complete story. paper_framing.md I can extract:
- SciERC NER full (n=529): ρ — VC 0.379, SJ 0.360, EM 0.295, FK 0.267, LP 0.205; AUROC — EM 0.749, SJ 0.692, VC 0.684, FK 0.629, LP 0.578
- SciERC RE full (n=397): AUROC — EM 0.706, VC 0.694, SJ 0.670, FK 0.609, LP 0.601
- Selection: NER best-of-N (n=529): LP 0.6501 > SJ 0.6450 > greedy 0.6439 > random 0.6077 (oracle 0.7758)
- RE best-of-N: greedy 0.4042 > LP 0.3948 > SJ 0.3855 > random 0.3544 (oracle 0.5850)
- Non-tied subset shows LP with a significant +2.9pp improvement (p=0.01), though the full set only gains 0.6pp (p=0.39)
- CoNLL results show greedy at 0.9123 with 58% degeneracy, while SJ, FK, and LP correlations range from 0.307 to 0.436
- LLaMA on CoNLL achieves similar correlations with greedy F1 at 0.927, and WNUT shows greedy F1 of 0.523 with minimal degeneracy
- Looking at scale ablations starting with the 4B model on CoNLL reaching 0.9234, and SciERC 4B showing SJ correlation of 0.4221
- Free-form ablation reveals LP's standard deviation barely changes between constrained and free-form settings (0.0206 vs 0.0199), with tied fractions dropping from 59.7% to 57.7%

Now I have the data I need to write the paper. I'm planning to include results from Few-NERD, a third seed run on SciERC, LoRA rank ablations, and a claim audit with prescriptive guidelines, plus the existing results from my framing document. I'm going to write this in LaTeX using a standard format.

Writing the paper structure... I'm restructuring the paper to follow a clearer narrative arc that builds from quality estimation through selection effectiveness and into the diagnostic analysis of convergence. I'm checking my experimental data to make sure I'm grounding the claims in actual numbers—looking at the Few-NERD results and other key metrics to support each section. Looking at the experimental results, I'm seeing that reducing the LoRA rank to 8 actually improves some metrics like degeneracy and selection performance, though it does hurt the greedy F1 score. The LLaMA model on CoNLL shows strong performance across different metrics, and I'm also pulling in some guidance from the paper framing notes on SciERC. Now I'm looking at the calibration metrics and free-form results across different seeds. I've got a complete picture of the experiments, so I'm ready to write the paper. I need to make sure I'm using the 3-seed means from exp-022 instead of the single-seed numbers from exp-012 for SciERC, since those give me more reliable estimates with confidence intervals. I'm looking at the AUROC results from exp-022 with seed 789, and cross-referencing them with the paper_framing.md values from seed 42 to get a fuller picture of the performance across methods. Since I don't have multi-seed AUROC means, I'll report the 3-seed ρ averages and note the AUROC from the primary seed. Now I'm ready to structure the paper around the conditional framing approach, starting with the core tables I need: dataset statistics, NER QE performance metrics across the four datasets, and then additional analysis.

For the paper structure, I'm planning roughly 6-7 tables total—NER selection results by condition, convergence analysis, LoRA rank ablation on SciERC, the prescriptive decision matrix, and possibly cross-seed stability and RE results if space allows. I need to pull WNUT results from exp-024 to complete the datasets section, where the greedy F1 is 0.523 at rank 16 with 5 epochs and no degeneration. I'm pulling together the CoNLL metrics from the detailed results and compression analysis, then mapping out the paper's core argument: selection doesn't universally fail, but rather succeeds when diversity is maintained and struggles under high-convergence conditions, while LP compression remains robust and degeneracy acts as a controllable training artifact. Now I need to structure the narrative around these key findings. I'm pulling together the experimental numbers for the paper—using the 8B Qwen results for consistency and noting the selection gap from the LP experiments. For WNUT, I'll include it in the convergence analysis but flag that it comes from a different experimental setup. The introduction should frame this as a conditional study examining when multi-sample selection actually works, grounded in the key finding that confidence signals predict quality reliably, but selection only succeeds when output diversity is preserved rather than collapsed through convergence.

Now I'm ready to write the paper itself. Let me set up the LaTeX structure and start building out the sections systematically, beginning with the dataset statistics table and working through the experimental results. Now I'm looking at how these tables map back to my experiments and considering consolidation. I can merge the NER quality estimation with selection results into a single table, and potentially handle the RE results as a subsection rather than a standalone table—that would bring me down to around 6-7 tables instead of 8.

I'm settling on 7 tables as a reasonable scope for an empirical paper: dataset statistics, the main NER results across conditions, output convergence metrics, LoRA rank ablation for causal evidence, cross-seed stability, RE results, and prescriptive guidelines. Now I'll start writing the LaTeX with booktabs formatting for clean presentation.

Writing LaTeX tables... I need to verify the directory structure exists before I start writing the LaTeX file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16f59a4f-1577-43dd-9cf7-6164a89c54a9",
  "isSidechain": false,
  "requestId": "req_011Cb63rogFCgADHe8F32xNP",
  "type": "assistant",
  "uuid": "a6307360-6de4-45d1-b1e7-06d81e1b1fac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u8R2n7keAnTzC7o2xnLgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30671,
      "cache_read_input_tokens": 23142,
      "output_tokens": 6507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6507,
          "cache_read_input_tokens": 23142,
          "cache_creation_input_tokens": 30671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30671
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

_source line 15 · 2026-05-16T10:00:02.458Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6307360-6de4-45d1-b1e7-06d81e1b1fac",
  "isSidechain": false,
  "requestId": "req_011Cb63rogFCgADHe8F32xNP",
  "type": "assistant",
  "uuid": "9e97a124-2a6b-43d4-bfc7-fa6f3398ed96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u8R2n7keAnTzC7o2xnLgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30671,
      "cache_read_input_tokens": 23142,
      "output_tokens": 6507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6507,
          "cache_read_input_tokens": 23142,
          "cache_creation_input_tokens": 30671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30671
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

_source line 16 · 2026-05-16T10:00:07.707Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MFjwQZFJ3mihZGRYRyjxo5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/",
  "description": "List output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e97a124-2a6b-43d4-bfc7-fa6f3398ed96",
  "isSidechain": false,
  "requestId": "req_011Cb63rogFCgADHe8F32xNP",
  "type": "assistant",
  "uuid": "b3e50bc9-948a-4c22-938c-f19603b19fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012u8R2n7keAnTzC7o2xnLgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30671,
      "cache_read_input_tokens": 23142,
      "output_tokens": 6507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6507,
          "cache_read_input_tokens": 23142,
          "cache_creation_input_tokens": 30671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30671
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

_source line 17 · 2026-05-16T10:00:07.922Z_

<details><summary>↩ Tool result · `toolu_01MFjwQZFJ3mihZGRYRyjxo5`</summary>

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
  "parentUuid": "b3e50bc9-948a-4c22-938c-f19603b19fd0",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "785e63dd-fe73-4c96-977d-d09e91af789f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b3e50bc9-948a-4c22-938c-f19603b19fd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "785e63dd-fe73-4c96-977d-d09e91af789f",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260516T092241",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Assistant

_source line 20 · 2026-05-16T10:00:14.743Z_

Directory exists. Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "785e63dd-fe73-4c96-977d-d09e91af789f",
  "isSidechain": false,
  "requestId": "req_011Cb64255wySDVYnShFDqHv",
  "type": "assistant",
  "uuid": "f3b0428a-4339-4c84-a733-4c52cf100d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVE1B2saqaVtugt9wzxaE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 53813,
      "output_tokens": 15636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15636,
          "cache_read_input_tokens": 53813,
          "cache_creation_input_tokens": 6520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6520
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

_source line 21 · 2026-05-16T10:05:02.999Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GzEKT9w1tVqDsCyhvTTsmD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\n\\newcommand{\\rmark}[1]{\\textsuperscript{#1}}\n\n\\title{When Does Multi-Sample Selection Help Structured IE?\\\\A Diagnostic Study of Output Convergence}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n%  ABSTRACT\n% ===========================================================================\n\\begin{abstract}\nTest-time scaling via multi-sample generation improves LLM performance on reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear.\nWe conduct a large-scale diagnostic study across four NER datasets (SciERC, CoNLL-2003, Few-NERD, WNUT-17), one RE dataset (SciERC), three model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and five confidence signal families.\nWe find that confidence signals \\emph{reliably} estimate output quality across instances (Spearman $\\rho$ up to 0.37, AUROC up to 0.75), yet their ability to \\emph{select} better candidates from multiple samples is \\textbf{regime-dependent}: under standard fine-tuning configurations that produce high output convergence (degeneracy 21--58\\%), no unsupervised signal significantly outperforms greedy decoding.\nHowever, when output diversity is preserved---through reduced fine-tuning intensity (LoRA rank 8 vs.\\ 16) or lower training epochs---log-probability selection recovers 3--4 percentage points over greedy ($p<0.03$).\nWe diagnose two mechanisms underlying selection failure: \\emph{instance degeneracy} (identical outputs across samples) and \\emph{log-probability compression} (within-instance score ranges $<$0.05 nats), and show that both are primarily driven by fine-tuning intensity rather than model capability alone.\nWe provide prescriptive guidelines: practitioners should assess output degeneracy rate and log-probability range to decide between multi-sample selection and greedy decoding.\n\\end{abstract}\n\n% ===========================================================================\n%  1  INTRODUCTION\n% ===========================================================================\n\\section{Introduction}\n\nTest-time scaling (TTS) strategies---generating multiple candidate outputs and selecting or aggregating the best---have yielded substantial improvements for LLM reasoning \\citep{wang2023selfconsistency,brown2024tts,snell2024scaling}.\nSelf-consistency~\\citep{wang2023selfconsistency} selects the majority answer among sampled chain-of-thought traces; best-of-$N$ with reward models~\\citep{cobbe2021gsm8k,lightman2023lets} ranks candidates by learned quality scores.\nA natural question arises: \\emph{can similar strategies improve structured information extraction?}\n\nStructured IE tasks---named entity recognition (NER) and relation extraction (RE)---produce \\emph{set-valued} outputs (entity sets, relation triples) whose quality is measured by token-level or tuple-level F1.\nUnlike discrete-answer reasoning, structured outputs admit partial credit and fine-grained quality variation, seemingly creating opportunity for selection.\nYet applying multi-sample strategies to structured IE requires confidence signals that can \\emph{rank} candidates within an instance---a requirement that goes beyond instance-level quality estimation.\n\nIn this work, we conduct a systematic diagnostic study of five unsupervised confidence signals across four NER datasets and one RE dataset, three model architectures, and controlled ablations of fine-tuning intensity.\nOur central finding is that the effectiveness of multi-sample selection is \\textbf{conditional on output convergence regime}:\n\n\\begin{itemize}\n\\item \\textbf{High-convergence regime} (degeneracy $>$20\\%, log-probability range $<$0.04 nats): Standard fine-tuning configurations produce outputs that are largely identical across samples. Selection is ineffective because there is nothing meaningful to select among. Greedy decoding ($T{=}0$) dominates at zero additional cost.\n\n\\item \\textbf{Low-convergence regime} (degeneracy $<$10\\%, log-probability range $>$0.07 nats): When fine-tuning is less aggressive---via lower LoRA rank or fewer training epochs---output diversity is preserved. Log-probability-based best-of-$N$ selection yields statistically significant gains of 3--4 percentage points over greedy ($p<0.03$).\n\\end{itemize}\n\nWe diagnose two failure mechanisms that explain selection ineffectiveness in the high-convergence regime.\nFirst, \\emph{instance degeneracy}: 21--58\\% of instances produce identical F1 scores across all $N{=}8$ samples, eliminating any selection headroom.\nSecond, \\emph{log-probability compression}: even among non-degenerate instances, within-instance log-probability ranges are compressed to a median of 0.018--0.041 nats, leaving insufficient signal for ranking.\n\nCritically, we show that output convergence is not an inevitable consequence of model capability---it is primarily driven by \\emph{fine-tuning intensity}.\nOn SciERC, reducing LoRA rank from 16 to 8 (same model, same data, same epochs) cuts degeneracy from 21\\% to 5.2\\% while sacrificing only 3.9 percentage points of greedy F1, and transforms log-probability selection from negligible (+0.6pp, $p{=}0.39$) to significant (+3.6pp, $p{=}0.015$).\nSimilarly, Few-NERD with 3-epoch training achieves F1=0.778 with only 5.4\\% degeneracy, enabling log-probability selection gains of +3.2pp ($p{=}0.028$)---despite having higher F1 than SciERC (0.664) where selection fails.\n\nOur contributions are:\n\\begin{enumerate}\n\\item A systematic evaluation of five confidence signal families for structured IE quality estimation across four datasets and three model configurations.\n\\item Identification of two failure mechanisms (instance degeneracy, log-probability compression) and evidence that both are driven by fine-tuning intensity rather than capability alone.\n\\item A controlled LoRA rank ablation providing causal evidence that output convergence is a tunable property of the training configuration.\n\\item Prescriptive guidelines for practitioners: assess degeneracy rate and log-probability range to determine whether multi-sample selection or greedy decoding is appropriate.\n\\end{enumerate}\n\n% ===========================================================================\n%  2  RELATED WORK\n% ===========================================================================\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency~\\citep{wang2023selfconsistency} aggregates reasoning traces via majority voting.\nRecent extensions include CISC~\\citep{cisc2025acl}, which uses confidence-weighted majority voting, Self-Certainty Best-of-$N$~\\citep{selfcertainty2026iclr}, which performs reward-free selection via KL-divergence, and ReASC~\\citep{reasc2026}, which adapts sampling to instance reliability.\nAtomic Self-Consistency~\\citep{atomicsc2024emnlp} decomposes long-form outputs into sub-claims.\nAll of these target reasoning tasks with discrete or decomposable answers; none address set-structured IE outputs.\nOur work is the first systematic study of multi-sample selection for structured IE, revealing that the output convergence properties of fine-tuned extraction models create qualitatively different challenges.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nSemantic uncertainty~\\citep{kuhn2023semantic} clusters outputs by meaning; calibration methods~\\citep{guo2017calibration,kadavath2022language,desai2020calibration} align confidence with accuracy.\nRecent surveys~\\citep{uqsurvey2025acl,uqcalibsurvey2025} provide comprehensive overviews.\nSemantic Entropy Probes~\\citep{semanticprobes2024} enable low-cost estimation.\nSelfCheckGPT~\\citep{manakul2023selfcheckgpt} uses sampling consistency for hallucination detection.\nCoCoA~\\citep{cocoa2025neurips} combines confidence and consistency for MBR-based UQ in QA and summarization.\nThese methods evaluate quality at the instance level; we additionally evaluate \\emph{within-instance ranking} for candidate selection.\n\n\\paragraph{Consistency for Structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for entity and relation extraction using surface-level string matching across four LLMs.\nThey acknowledge that their approach ``overlooks semantically consistent outputs.''\nOur structured Jaccard metric directly addresses this limitation by performing type-grouped Hungarian matching that captures partial structural agreement.\nMoreover, we go beyond correlation analysis to evaluate best-of-$N$ selection and diagnose why it fails.\n\n\\paragraph{Confidence in Information Extraction.}\nClassical IE confidence methods~\\citep{culotta2004confidence} rely on model internals (CRF marginals, sequence probabilities).\nToken-level NER uncertainty~\\citep{xiao2019quantifying,shelmanov2021certain,he2020towards} and structured calibration~\\citep{kuleshov2015calibrated,jagannatha2022calibrating} address the extraction setting.\nSelective prediction~\\citep{geifman2017selective,knowyourlimits2025tacl} abstains on uncertain instances.\nOur work differs by focusing on the gap between quality estimation (which works) and selection (which is regime-dependent).\n\n\\paragraph{MBR Decoding.}\nMinimum Bayes Risk decoding~\\citep{eikema2022map} selects outputs maximizing expected utility under a sample-based approximation.\nPrior MBR failure analyses attribute poor performance to utility function misalignment.\nOur failure mechanism is qualitatively different: the utility function (structured F1) \\emph{is} aligned with the confidence signal (within-instance $\\rho{=}0.52$), but instance degeneracy and score compression eliminate actionable selection headroom.\n\n% ===========================================================================\n%  3  METHODOLOGY\n% ===========================================================================\n\\section{Methodology}\n\n\\subsection{Task and Datasets}\n\nWe evaluate on four NER datasets and one RE dataset, chosen to span different entity densities, type granularities, and domains (\\Cref{tab:datasets}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dataset statistics. $|E|$/inst = mean entities per instance.}\n\\label{tab:datasets}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{Types} & \\textbf{$n$ (test)} & \\textbf{$|E|$/inst} \\\\\n\\midrule\nSciERC       & NER+RE & 6 NER, 7 RE & 529 / 397  & $\\sim$2.1 \\\\\nCoNLL-2003   & NER    & 4            & 2,756      & $\\sim$1.8 \\\\\nFew-NERD     & NER    & 8 (coarse)   & 4,506      & $\\sim$3.4 \\\\\nWNUT-17      & NER    & 6            & 1,287      & $\\sim$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{SciERC}~\\citep{luan2018scierc} provides scientific abstracts annotated for entities and relations, with fine-grained types and complex relation structures.\n\\textbf{CoNLL-2003}~\\citep{tjong2003conll} is the standard newswire NER benchmark with four coarse entity types.\n\\textbf{Few-NERD}~\\citep{ding2021fewnerd} (INTRA, coarse 8-type) features high entity density ($\\sim$3.4 entities/instance) with many multi-word entities, providing substantial boundary variation.\n\\textbf{WNUT-17}~\\citep{derczynski2017wnut} targets emerging and rare entities in social media text.\n\n\\subsection{Confidence Signals}\n\\label{sec:signals}\n\nWe evaluate five confidence signals spanning four families:\n\n\\paragraph{Structural Consistency.}\n\\textbf{Soft Jaccard (SJ)}: For each pair of samples, compute type-grouped Hungarian matching between entity (or relation) sets, then average pairwise Jaccard similarity across all $\\binom{N}{2}$ pairs.\nSJ captures partial structural agreement.\n\n\\textbf{Fleiss' Kappa (FK)}: Treat each token position as rated by $N$ annotators (samples), with categories being entity types (including O). Compute Fleiss' $\\kappa$ as inter-annotator agreement.\n\n\\textbf{Exact Match (EM)}: Fraction of sample pairs producing identical entity/relation sets. A strict binary signal.\n\n\\paragraph{Voting Confidence (VC).}\nFor each entity mention appearing in any sample, compute the fraction of samples containing it. Instance-level VC is the mean entity-level vote fraction.\n\n\\paragraph{Log-Probability (LP).}\nMean token-level log-probability of the generated output, computed from the model's own probability estimates. The only per-sample (not per-instance) signal.\n\n\\subsection{Models and Training}\n\n\\textbf{Primary model}: Qwen3-8B with LoRA fine-tuning. Default configuration: rank=16, $\\alpha$=32, 5 epochs for SciERC/CoNLL/WNUT, 3 epochs for Few-NERD.\n\\textbf{Scale ablation}: Qwen3-4B with matched hyperparameters.\n\\textbf{Cross-architecture}: LLaMA-3.1-8B with LoRA rank=32.\n\\textbf{Fine-tuning intensity ablation}: Qwen3-8B with LoRA rank=8, $\\alpha$=16, 5 epochs on SciERC.\n\nAll models are fine-tuned to generate structured JSON outputs containing entity mentions, types, and (for RE) relation triples.\n\n\\subsection{Inference and Evaluation}\n\\label{sec:eval}\n\nFor each test instance, we generate $N{=}8$ samples at temperature $T{=}1.0$ (unless stated otherwise) and compute all five confidence signals.\nEvaluation metrics:\n\n\\paragraph{Quality Estimation (QE).}\nSpearman $\\rho$ between signal value and instance-level F1, measuring cross-instance ranking ability. AUROC for binary discrimination (above/below median F1). Reported over 3 random seeds where available.\n\n\\paragraph{Selection.}\nBest-of-$N$: select the sample with the highest signal value; report its F1. Compared against greedy ($T{=}0$), random sample, and oracle (best F1 among $N$ samples). Statistical significance via bootstrap with 1000 iterations.\n\n\\paragraph{Convergence Diagnostics.}\n\\emph{Degeneracy rate}: fraction of instances where all $N$ samples produce identical F1.\n\\emph{LP compression}: median within-instance range of log-probability scores across $N$ samples (in nats).\n\n% ===========================================================================\n%  4  QUALITY ESTIMATION RESULTS\n% ===========================================================================\n\\section{Quality Estimation Results}\n\n\\subsection{Cross-Dataset NER Quality Estimation}\n\n\\Cref{tab:ner_qe} presents QE results across four NER datasets. Confidence signals provide moderate-to-strong quality estimation in all settings, with Spearman $\\rho$ ranging from 0.17 to 0.44.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{NER quality estimation (Spearman $\\rho$). SciERC and Few-NERD report 3-seed mean $\\pm$ SD. CoNLL and WNUT are single-seed. Best $\\rho$ per dataset in \\textbf{bold}.}\n\\label{tab:ner_qe}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Signal} & \\textbf{SciERC} & \\textbf{CoNLL} & \\textbf{Few-NERD} & \\textbf{WNUT} \\\\\n\\midrule\nVC   & \\textbf{.371}{\\scriptsize$\\pm$.030} & ---   & \\textbf{.295}{\\scriptsize$\\pm$.015} & --- \\\\\nSJ   & .343{\\scriptsize$\\pm$.053} & \\textbf{.436} & .216{\\scriptsize$\\pm$.019} & --- \\\\\nEM   & .292{\\scriptsize$\\pm$.020} & ---   & .212{\\scriptsize$\\pm$.015} & --- \\\\\nFK   & .258{\\scriptsize$\\pm$.037} & .400  & .173{\\scriptsize$\\pm$.009} & --- \\\\\nLP   & .219{\\scriptsize$\\pm$.013} & .307  & .275{\\scriptsize$\\pm$.015} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nFirst, all five signals provide meaningful QE across datasets---the worst signal family (FK on Few-NERD, $\\rho{=}0.173$) still exceeds chance.\nSecond, the \\emph{optimal signal depends on the dataset}: on SciERC, structural signals (VC, SJ) dominate log-probability ($\\rho{=}0.371$ vs.\\ 0.219); on Few-NERD, LP is competitive with structural signals ($\\rho{=}0.275$ vs.\\ VC 0.295) and significantly outperforms SJ ($\\rho{=}0.275$ vs.\\ 0.216).\nThird, on SciERC, VC consistently outperforms LP across seeds (Fisher combined $p{=}0.018$), while the SJ advantage over LP is borderline (Fisher $p{=}0.085$) due to seed-to-seed instability in SJ (CV=0.154 vs.\\ LP CV=0.059).\n\nOn CoNLL-2003, SJ achieves the highest $\\rho{=}0.436$.\nCross-model validation with LLaMA-3.1-8B on CoNLL yields SJ $\\rho{=}0.431$ and FK $\\rho{=}0.428$, confirming cross-architecture consistency.\n\nAUROC results on SciERC NER (seed 42) show EM achieves the best binary discrimination (0.749), followed by SJ (0.692) and VC (0.684), with LP lowest (0.578). EM excels at binary go/no-go decisions but ranks lower on Spearman $\\rho$ (0.295) due to its coarse-grained nature.\n\n\\subsection{Task Complexity: NER vs.\\ RE}\n\nSciERC relation extraction presents a qualitatively different challenge (\\Cref{tab:re_qe}).\nWith 43--48\\% of RE samples producing F1=0, the quality distribution is binary-dominated.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC RE quality estimation (3-seed mean $\\rho$). Signal rankings are unstable across seeds---no signal is consistently ranked first.}\n\\label{tab:re_qe}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Signal} & \\textbf{$\\rho$ (mean $\\pm$ SD)} & \\textbf{Rank-1 seeds} \\\\\n\\midrule\nVC   & .321 $\\pm$ .029 & 2 of 3 \\\\\nSJ   & .280 $\\pm$ .029 & 1 of 3 \\\\\nFK   & .280 $\\pm$ .035 & 0 of 3 \\\\\nLP   & .249 $\\pm$ .051 & 0 of 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLP's conditional $\\rho$ (conditioned on non-zero F1 samples) drops to 0.011 ($p{=}0.86$), confirming that LP's entire RE correlation comes from discriminating zero vs.\\ non-zero F1---it has no power for quality gradients within the model's capability range.\nRE signal rankings are unstable across seeds: seed 42 ranks VC first, seed 123 ranks FK first, seed 789 ranks SJ first.\nWe conclude that no unsupervised signal reliably ranks RE quality; all are weak and unstable under cross-seed variation.\n\n% ===========================================================================\n%  5  SELECTION EFFECTIVENESS\n% ===========================================================================\n\\section{Selection Effectiveness}\n\n\\subsection{When Selection Fails: High-Convergence Regimes}\n\nUnder standard fine-tuning configurations (LoRA rank=16, 5 epochs), multi-sample selection provides negligible or negative gains (\\Cref{tab:selection}).\n\nOn SciERC NER, the best signal (LP) achieves F1=0.650 vs.\\ greedy 0.644---a gain of +0.6pp that is not statistically significant (bootstrap $p{=}0.39$, 95\\% CI [$-$0.030, +0.042], Cohen's $d{=}0.038$).\nOn CoNLL NER, LP selection yields $-$1.0pp vs.\\ greedy ($p{=}0.62$).\nOn SciERC RE, greedy (F1=0.404) outperforms all signals; the best unsupervised method (LP, F1=0.395) is 0.9pp worse.\n\nScale ablation at 4B confirms the pattern: on SciERC NER, all signals perform \\emph{worse} than greedy (SJ $-$1.5pp, LP $-$2.2pp) despite 13pp of oracle headroom.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across conditions. $\\Delta$ = gap vs.\\ greedy in percentage points. Statistically significant gains ($p<0.05$) in \\textbf{bold}. Standard FT = LoRA rank=16, 5 epochs (3 for Few-NERD). Mild FT = LoRA rank=8, 5 epochs.}\n\\label{tab:selection}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Config} & \\textbf{Greedy} & \\textbf{LP Sel.} & \\textbf{$\\Delta$} & \\textbf{$p$} & \\textbf{Oracle} \\\\\n\\midrule\nSciERC NER  & Standard FT & .664 & .650 & +0.6  & .39  & .776 \\\\\nSciERC NER  & Mild FT     & .625 & .661 & \\textbf{+3.6}  & \\textbf{.015} & .812 \\\\\nFew-NERD    & 3 epochs    & .778 & .810 & \\textbf{+3.2}  & \\textbf{.028} & .869 \\\\\nCoNLL NER   & Standard FT & .912 & .902 & $-$1.0 & .62  & --- \\\\\n\\midrule\nSciERC RE   & Standard FT & .404 & .395 & $-$0.9 & ---  & .585 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{When Selection Succeeds: Preserved Output Diversity}\n\nTwo conditions independently demonstrate that selection \\emph{can} work:\n\n\\paragraph{Few-NERD (3-epoch training, rank=16).}\nDespite achieving high greedy F1 (0.778---higher than SciERC's 0.664), Few-NERD exhibits only 5.4\\% degeneracy.\nLP selection yields +3.2pp ($p{=}0.028$, Cohen's $d{=}0.152$, 95\\% CI [0.004, 0.060]).\nThis result directly contradicts any ``capability trap'' narrative that posits higher F1 necessarily implies higher degeneracy and useless selection.\n\n\\paragraph{SciERC with LoRA rank=8.}\nOn the \\emph{same} SciERC dataset where standard fine-tuning produces failed selection (+0.6pp, n.s.), reducing LoRA rank from 16 to 8 transforms the outcome: LP selection achieves +3.6pp ($p{=}0.015$, $d{=}0.168$, 95\\% CI [0.008, 0.064]).\nGreedy F1 drops from 0.664 to 0.625 ($-$3.9pp), but the selection gain more than compensates within the multi-sample framework: rank=8 with LP selection (0.661) is only 0.3pp below rank=16 greedy (0.664), while gaining uncertainty quantification capability.\n\n\\paragraph{Non-degenerate subset analysis.}\nOn SciERC (rank=16), restricting to the 40\\% of non-degenerate instances reveals LP selection gains of +2.9pp ($p{=}0.01$), with within-instance $\\rho$ jumping from 0.08 to 0.39.\nThe signal \\emph{works} where there is something to select among---the problem is that aggressive fine-tuning eliminates this headroom for most instances.\n\n% ===========================================================================\n%  6  DIAGNOSING OUTPUT CONVERGENCE\n% ===========================================================================\n\\section{Diagnosing Output Convergence}\n\n\\subsection{Instance Degeneracy}\n\nInstance degeneracy---the fraction of instances producing identical F1 across all $N{=}8$ samples---varies dramatically across conditions (\\Cref{tab:convergence}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output convergence diagnostics across conditions. Degen.\\ = degeneracy rate (\\%). LP range = median within-instance log-probability range (nats). Selection gain = LP best-of-$N$ vs.\\ greedy (pp).}\n\\label{tab:convergence}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{F1} & \\textbf{Degen.\\ (\\%)} & \\textbf{LP range} & \\textbf{Sel.\\ gain} & \\textbf{$p$} \\\\\n\\midrule\nCoNLL r16 5ep         & .912 & 58.0 & 0.018 & $-$1.0 & .62 \\\\\nSciERC r16 5ep        & .664 & 21.0 & 0.041 & +0.6  & .39 \\\\\nSciERC 4B r16 5ep     & .662 & 10.4 & ---   & $-$2.2 & --- \\\\\nSciERC r8 5ep         & .625 &  5.2 & 0.074 & +3.6  & .015 \\\\\nFew-NERD r16 3ep      & .778 &  5.4 & 0.084 & +3.2  & .028 \\\\\nWNUT r16 5ep          & .523 &  0.0 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder standard fine-tuning, degeneracy correlates with greedy F1 across three datasets (CoNLL, SciERC, WNUT; $R^2{=}0.98$).\nHowever, adding Few-NERD to the regression collapses $R^2$ to 0.51: Few-NERD achieves F1=0.778 with only 5.4\\% degeneracy, producing a residual of 30.2 percentage points from the three-dataset regression line that would predict $\\sim$35--40\\% degeneracy.\nAdding the rank=8 SciERC data point further reduces $R^2$ to 0.35.\n\nThis demonstrates that \\textbf{model capability (F1) is not the primary driver of degeneracy}.\nThe same model (Qwen3-8B) on the same dataset (SciERC) produces 21\\% or 5.2\\% degeneracy depending solely on LoRA rank.\nFew-NERD's low degeneracy despite high F1 reflects both higher entity density (3.4 entities/instance, creating more boundary variation) and milder fine-tuning (3 epochs vs.\\ 5).\n\n\\subsection{Log-Probability Compression}\n\nLog-probability is the only per-sample signal capable of ranking candidates within an instance.\nHowever, within-instance LP ranges are severely compressed under high-convergence conditions.\n\nCoNLL exhibits a median LP range of only 0.018 nats---samples are nearly indistinguishable by log-probability.\nSciERC (rank=16) shows 0.041 nats.\nWhen convergence is reduced, LP ranges expand: SciERC rank=8 yields 0.074 nats (1.8$\\times$ wider than rank=16), and Few-NERD yields 0.084 nats (2.0$\\times$ wider than SciERC rank=16).\n\n\\paragraph{Free-form decoding ablation.}\nTo test whether LP compression is caused by constrained (JSON) decoding, we run an ablation with free-form output on SciERC.\nLP standard deviation is virtually unchanged: constrained $\\sigma{=}0.0206$ vs.\\ free-form $\\sigma{=}0.0199$ (ratio 0.97).\nTied fraction drops negligibly from 59.7\\% to 57.7\\%.\nParse rate remains 99.95\\%, confirming the fine-tuned model generates valid JSON without grammar constraints.\nThis proves LP compression is \\textbf{intrinsic to the model's output distribution}, not an artifact of decoding format.\n\n\\subsection{Convergence Drivers}\n\\label{sec:drivers}\n\nWe consolidate evidence from six experimental conditions to identify convergence drivers (\\Cref{tab:drivers}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Degeneracy drivers across conditions. FT intensity = combination of LoRA rank and training epochs.}\n\\label{tab:drivers}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Condition} & \\textbf{F1} & \\textbf{Degen.\\ (\\%)} & \\textbf{LoRA/Epochs} & \\textbf{Primary driver} \\\\\n\\midrule\nCoNLL r16 5ep     & .912 & 58.0 & 16 / 5 & high F1 + aggressive FT \\\\\nSciERC r16 5ep    & .664 & 21.0 & 16 / 5 & moderate F1 + aggressive FT \\\\\nSciERC r8 5ep     & .625 &  5.2 & 8 / 5  & moderate F1 + \\textbf{mild FT} \\\\\nFew-NERD r16 3ep  & .778 &  5.4 & 16 / 3 & high F1 + \\textbf{mild FT} \\\\\nSciERC 4B r16 5ep & .662 & 10.4 & 16 / 5 & lower capacity + aggressive FT \\\\\nWNUT r16 5ep      & .523 &  0.0 & 16 / 5 & low F1 (no convergence) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe key comparison is SciERC rank=16 (21\\% degeneracy) vs.\\ rank=8 (5.2\\% degeneracy): same model, same data, same training epochs---only LoRA rank differs.\nThis controlled experiment isolates fine-tuning intensity as the primary degeneracy driver.\n\nFew-NERD provides complementary evidence along the epoch dimension: 3 epochs produce 5.4\\% degeneracy at F1=0.778, while CoNLL with 5 epochs produces 58\\% degeneracy at F1=0.912.\nThe F1 difference (0.134) would predict $\\sim$30pp degeneracy difference under a capability-only model; the actual difference is 52.6pp, far exceeding what F1 alone explains.\n\nEntity density also contributes: Few-NERD's $\\sim$3.4 entities per instance create more combinatorial variation in boundary positions than SciERC's $\\sim$2.1 or CoNLL's $\\sim$1.8, mechanically reducing the probability that all $N$ samples produce identical entity sets.\n\n\\subsection{LoRA Rank Ablation: Causal Evidence}\n\\label{sec:ablation}\n\nThe LoRA rank=8 ablation on SciERC provides the strongest evidence that convergence is a controllable training parameter (\\Cref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA rank ablation on SciERC NER ($N{=}8$, $T{=}1.0$, $n{=}529$). Rank=8 preserves output diversity at modest F1 cost.}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Rank=16} & \\textbf{Rank=8} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGreedy F1           & .664   & .625   & $-$3.9pp \\\\\nOracle F1           & .776   & .812   & +3.7pp \\\\\nOracle headroom     & 10.9pp & 18.7pp & +7.9pp \\\\\nDegeneracy          & 21.0\\% &  5.2\\% & $-$15.8pp \\\\\n\\midrule\nSJ $\\rho$           & .360   & .378   & +0.018 \\\\\nLP $\\rho$           & .205   & .252   & +0.047 \\\\\nVC $\\rho$           & .379   & .408   & +0.029 \\\\\n\\midrule\nLP sel.\\ gap (pp)   & +0.6   & +3.6   & +3.0pp \\\\\nLP sel.\\ $p$        & .39    & .015   & --- \\\\\nSJ sel.\\ gap (pp)   & $-$1.9 & +2.8   & +4.7pp \\\\\nSJ sel.\\ $p$        & ---    & .042   & --- \\\\\n\\midrule\nLP range (nats)     & 0.041  & 0.074  & +0.033 \\\\\nTied fraction       & 21.0\\% &  5.2\\% & $-$15.8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral findings are noteworthy:\n\n\\paragraph{QE is decoupled from selection.}\nQE correlations are \\emph{stable} across rank configurations: SJ $\\rho$ changes by only +0.018 (0.360$\\to$0.378).\nSelection effectiveness changes \\emph{dramatically}: LP selection gap moves from +0.6pp (n.s.) to +3.6pp ($p{=}0.015$).\nThis decoupling demonstrates that QE is an intrinsic property of the signal, while selection effectiveness is regime-dependent---governed by the output convergence properties of the fine-tuning configuration.\n\n\\paragraph{Trade-off quantification.}\nEach 1pp of greedy F1 sacrificed by reducing LoRA rank buys a 4.1$\\times$ reduction in degeneracy (3.9pp F1 cost / 15.8pp degeneracy reduction).\nThe practical implication is that rank=8 with LP selection (F1=0.661) is only 0.3pp below rank=16 greedy (0.664), while providing calibrated uncertainty estimates as a bonus.\n\n\\paragraph{Oracle headroom expansion.}\nRank=8's oracle F1 (0.812) is 3.7pp \\emph{higher} than rank=16's oracle (0.776), despite lower greedy F1.\nMore diverse outputs span a wider region of output space, providing better candidates for an ideal selector.\nThis confirms that reducing fine-tuning intensity preserves the information needed for effective selection.\n\n% ===========================================================================\n%  7  CROSS-SEED AND CROSS-MODEL STABILITY\n% ===========================================================================\n\\section{Robustness Analysis}\n\n\\subsection{Cross-Seed Stability}\n\nThree-seed evaluation on SciERC NER reveals important stability differences (\\Cref{tab:seeds}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER 3-seed QE ($\\rho$, $N{=}8$, $T{=}1.0$, $n{=}529$). CV = coefficient of variation.}\n\\label{tab:seeds}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Signal} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 789} & \\textbf{Mean} & \\textbf{CV} \\\\\n\\midrule\nVC  & .379 & .395 & .338 & .371 & .081 \\\\\nSJ  & .360 & .385 & .285 & .343 & .154 \\\\\nEM  & .295 & .310 & .272 & .292 & .068 \\\\\nFK  & .267 & .290 & .218 & .258 & .143 \\\\\nLP  & .205 & .225 & .228 & .219 & .059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSJ exhibits the highest variability (CV=0.154): seed 789 yields SJ $\\rho{=}0.285$, close to LP's 0.228, while seeds 42 and 123 show a clear SJ advantage.\nFisher's combined test for SJ$>$LP gives $p{=}0.085$---borderline at $\\alpha{=}0.05$.\nIn contrast, VC$>$LP is robust ($p{=}0.018$), and LP is the most stable signal (CV=0.059).\nFor SciERC RE, signal rankings are completely unstable across seeds (three different top-1 signals), leading us to conclude that no unsupervised signal reliably ranks RE quality at current sample sizes.\n\n\\subsection{Cross-Model Validation}\n\nLLaMA-3.1-8B on CoNLL NER produces SJ $\\rho{=}0.431$ and FK $\\rho{=}0.428$, closely matching Qwen3-8B (SJ $\\rho{=}0.436$, FK $\\rho{=}0.400$).\nBoth models exhibit high degeneracy and ineffective selection on CoNLL under aggressive fine-tuning, confirming that convergence patterns are architecture-independent under matched training intensity.\n\nThe Qwen3-4B scale ablation on SciERC yields SJ $\\rho{=}0.422$ ($\\ge$ 8B's 0.343 three-seed mean), demonstrating that QE correlations are maintained or even improved at smaller scale.\nHowever, 4B selection is equally ineffective: SJ $-$1.5pp, LP $-$2.2pp vs.\\ greedy on SciERC NER, confirming that the correlation--selection gap persists across model sizes.\n\n% ===========================================================================\n%  8  PRESCRIPTIVE GUIDELINES\n% ===========================================================================\n\\section{Prescriptive Guidelines}\n\nBased on our empirical findings, we propose a decision matrix for practitioners (\\Cref{tab:guidelines}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Prescriptive decision matrix for multi-sample selection in structured IE.}\n\\label{tab:guidelines}\n\\begin{tabular}{p{2.3cm}p{2cm}p{4.5cm}c}\n\\toprule\n\\textbf{Degeneracy} & \\textbf{LP Range} & \\textbf{Recommendation} & \\textbf{Gain} \\\\\n\\midrule\n$<$10\\% & $>$0.07 nats & LP best-of-$N$ selection & 2--4pp \\\\\n10--20\\% & 0.04--0.07 & Evaluate on dev set; marginal & 0--2pp \\\\\n$>$20\\% & $<$0.04 & $T{=}0$ greedy decoding & 0pp \\\\\n\\midrule\n\\multicolumn{2}{l}{RE with $>$40\\% zero-F1} & Supervised verifier or greedy & 0pp\\rmark{$\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\scriptsize \\rmark{$\\dagger$} No unsupervised signal reliably helps; supervised approaches are future work.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{How to diagnose the regime.}\nBefore deploying multi-sample inference, run a pilot on a small development set ($n \\ge 200$) with $N{=}8$ samples at $T{=}1.0$.\nCompute the degeneracy rate (fraction of instances with identical outputs across all samples) and the median within-instance LP range.\nIf degeneracy $<$10\\% and LP range $>$0.07 nats, LP-based best-of-$N$ is likely beneficial.\n\n\\paragraph{How to control the regime.}\nIf the standard fine-tuning configuration produces high convergence, practitioners can reduce LoRA rank (our evidence: rank 16$\\to$8 cuts degeneracy from 21\\% to 5.2\\% at 3.9pp F1 cost) or reduce training epochs.\nThe trade-off is explicit: each percentage point of greedy F1 sacrificed yields approximately 4$\\times$ degeneracy reduction, and LP selection can recover much of the sacrificed F1.\n\n\\paragraph{Signal choice.}\nLP is the recommended selection signal because it is the only per-sample signal and shows the most consistent selection gains.\nFor quality estimation (instance-level), VC and SJ provide stronger correlations on entity-rich datasets, but the optimal QE signal is dataset-dependent.\n\n% ===========================================================================\n%  9  DISCUSSION\n% ===========================================================================\n\\section{Discussion}\n\n\\paragraph{Reinterpreting the capability--convergence relationship.}\nA naive analysis of three datasets (CoNLL, SciERC, WNUT) suggests a tight relationship between model capability (F1) and output degeneracy ($R^2{=}0.98$), tempting the conclusion that better models inevitably produce less diverse outputs.\nHowever, Few-NERD and the LoRA rank ablation break this narrative: F1 explains at most 35--51\\% of degeneracy variance when these additional data points are included.\nFine-tuning intensity (LoRA rank, training epochs) and dataset properties (entity density, type granularity) are equally or more important determinants.\nThis has practical implications: practitioners need not accept convergence as an unavoidable consequence of training a good model---they can actively manage it.\n\n\\paragraph{QE vs.\\ selection: a fundamental decoupling.}\nOur results reveal that quality estimation and selection are governed by different factors.\nQE correlation ($\\rho$ between signal and F1) is an intrinsic property of the signal and the task, robust to changes in fine-tuning intensity (SJ $\\rho$ changes by only 0.018 between rank=16 and rank=8).\nSelection effectiveness depends on the \\emph{convergence regime}: the same signals that produce useful QE rankings across instances fail to select within instances when outputs are too similar.\nThis distinction is important for system design: QE is always useful for flagging uncertain instances (selective prediction, human-in-the-loop), even when selection fails.\n\n\\paragraph{Comparison with reasoning TTS.}\nIn reasoning tasks, self-consistency works because candidate answers are discrete and diverse: the model genuinely ``considers'' different solution paths.\nIn fine-tuned structured IE, the model has learned a dominant extraction pattern, and sampling merely introduces boundary noise around this pattern.\nThe fundamental difference is that reasoning diversity arises from \\emph{multiple valid solution strategies}, while IE sampling diversity (when present) arises from \\emph{boundary perturbations} around a single learned extraction strategy.\n\n\\paragraph{Limitations.}\n(1) We evaluate one primary model family (Qwen3) with LLaMA and 4B as secondary validations; larger models ($>$70B) remain untested.\n(2) All experiments use LoRA fine-tuning; full fine-tuning or in-context learning may produce different convergence dynamics.\n(3) Our prescriptive thresholds (degeneracy 10\\%, LP range 0.07) are derived from four NER datasets and one RE dataset---validation on additional domains (biomedical, legal, multilingual) is needed.\n(4) We do not evaluate supervised verifiers, which could close the selection gap even under high convergence; this is important future work.\n(5) WNUT results are limited due to low model capability on out-of-distribution entities.\n\n% ===========================================================================\n%  10  CONCLUSION\n% ===========================================================================\n\\section{Conclusion}\n\nWe present a diagnostic study of multi-sample selection for structured information extraction across four NER datasets, three model configurations, and five confidence signal families.\nOur central finding is that selection effectiveness is regime-dependent: under standard fine-tuning configurations that induce high output convergence, no unsupervised signal outperforms greedy decoding; but when output diversity is preserved through reduced fine-tuning intensity, log-probability selection yields statistically significant gains of 3--4 percentage points.\n\nWe identify two mechanisms (instance degeneracy and log-probability compression) that underlie selection failure and provide causal evidence---via a controlled LoRA rank ablation---that both are driven primarily by fine-tuning intensity rather than model capability.\nThese findings lead to actionable guidelines: practitioners should diagnose their fine-tuning regime's convergence properties before investing in multi-sample inference, and can actively control these properties through training configuration choices.\n\n% ===========================================================================\n%  REFERENCES (placeholder)\n% ===========================================================================\n\\begingroup\n\\small\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Brown et~al.(2024)]{brown2024tts}\nB.~Brown, J.~Juravsky, R.~Ehrlich, R.~Clark, Q.~V.~Le, C.~R\\'{e}, and A.~Roshan~Ghias.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nC.~Snell, J.~Lee, K.~Xu, and A.~Kumar.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023lets}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[CISC(2025)]{cisc2025acl}\nConfidence-weighted majority voting for reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Self-Certainty(2026)]{selfcertainty2026iclr}\nSelf-certainty best-of-{N}: Reward-free selection via {KL}-divergence.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[ReASC(2026)]{reasc2026}\nReliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[Atomic SC(2024)]{atomicsc2024emnlp}\nAtomic self-consistency for long-form text.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nL.~Kuhn, Y.~Gal, and S.~Farquhar.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q.~Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Kadavath et~al.(2022)]{kadavath2022language}\nS.~Kadavath et~al.\n\\newblock Language models (mostly) know what they know.\n\\newblock \\emph{arXiv:2207.05221}, 2022.\n\n\\bibitem[Desai and Durrett(2020)]{desai2020calibration}\nS.~Desai and G.~Durrett.\n\\newblock Calibration of pre-trained transformers.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[UQ Survey(2025)]{uqsurvey2025acl}\nUncertainty quantification for {LLMs}: A comprehensive survey.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[UQ+Calibration Survey(2025)]{uqcalibsurvey2025}\nUncertainty quantification and calibration in large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[Semantic Probes(2024)]{semanticprobes2024}\nSemantic entropy probes: Low-cost uncertainty estimation.\n\\newblock 2024.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nP.~Manakul, A.~Liusie, and M.~J.~F.~Gales.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[CoCoA(2025)]{cocoa2025neurips}\nM.~Vashurin et~al.\n\\newblock {CoCoA}: Combining confidence and consistency for {MBR}-based uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[N\\'{e}dellec and Xia(2026)]{nedellec2026consistency}\nC.~N\\'{e}dellec and R.~Xia.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLMs} for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nA.~Culotta and A.~McCallum.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019quantifying}\nY.~Xiao and W.~Y.~Wang.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021certain}\nA.~Shelmanov et~al.\n\\newblock How certain is your {Transformer}?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[He et~al.(2020)]{he2020towards}\nJ.~He, X.~Zhong, J.~Su, and P.~Zhang.\n\\newblock Towards better uncertainty estimation for {NER}.\n\\newblock 2020.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibrated}\nV.~Kuleshov and P.~Liang.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibrating}\nA.~Jagannatha and H.~Yu.\n\\newblock Calibrating structured output predictors.\n\\newblock 2022.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nY.~Geifman and R.~El-Yaniv.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Know Your Limits(2025)]{knowyourlimits2025tacl}\nKnow your limits: A survey on abstention in {NLP}.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Eikema et~al.(2022)]{eikema2022map}\nB.~Eikema and W.~Aziz.\n\\newblock Is {MAP} decoding all you need? {The} inadequacy of the mode in neural machine translation.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nY.~Luan, L.~He, M.~Ostendorf, and H.~Hajishirzi.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nE.~F.~Tjong Kim~Sang and F.~De~Meulder.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[Ding et~al.(2021)]{ding2021fewnerd}\nN.~Ding, G.~Xu, Y.~Chen, X.~Wang, Z.~Han, P.~Xie, H.~Zheng, and Z.~Liu.\n\\newblock {Few-NERD}: A few-shot named entity recognition dataset.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Derczynski et~al.(2017)]{derczynski2017wnut}\nL.~Derczynski, E.~Nichols, M.~van Erp, and N.~Limsopatham.\n\\newblock Results of the {WNUT}2017 shared task on novel and emerging entity recognition.\n\\newblock In \\emph{W-NUT}, 2017.\n\n\\end{thebibliography}\n\\endgroup\n\n% ===========================================================================\n%  APPENDIX\n% ===========================================================================\n\\appendix\n\n\\section{Few-NERD Detailed Results}\n\\label{app:fewnerd}\n\n\\Cref{tab:fewnerd_full} presents the full Few-NERD QE results across three seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD NER QE metrics (3-seed, $N{=}8$, $T{=}1.0$, $n{=}4506$).}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Signal} & \\textbf{$\\rho$} & \\textbf{SD} & \\textbf{AUROC} & \\textbf{Sel.\\ F1} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nLP     & .275 & .015 & .658 & .810 & +3.2 & .028 \\\\\nVC     & .295 & .015 & .681 & .799 & +2.1 & .065 \\\\\nSJ     & .216 & .019 & .624 & .793 & +1.5 & .12 \\\\\nEM     & .212 & .015 & .718 & .793 & +1.5 & .13 \\\\\nFK     & .173 & .009 & .588 & .790 & +1.2 & .18 \\\\\n\\midrule\ngreedy & ---  & ---  & ---  & .778 & ---  & --- \\\\\noracle & ---  & ---  & ---  & .869 & +9.1 & --- \\\\\nrandom & ---  & ---  & ---  & .765 & $-$1.3 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SciERC RE Cross-Seed Signal Rankings}\n\\label{app:re_seeds}\n\n\\Cref{tab:re_rankings} demonstrates the instability of RE signal rankings across seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SciERC RE signal rankings by Spearman $\\rho$ (full set, 3 seeds).}\n\\label{tab:re_rankings}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Rank 1} & \\textbf{Rank 2} & \\textbf{Rank 3} & \\textbf{Rank 4} & \\textbf{Rank 5} \\\\\n\\midrule\n42  & VC (.350) & FK (.275) & LP (.266) & SJ (.250) & EM (.134) \\\\\n123 & VC (.320) & FK (.317) & LP (.290) & SJ (.283) & EM (.170) \\\\\n789 & SJ (.308) & VC (.293) & FK (.248) & EM (.198) & LP (.192) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Fisher Combined P-Values}\n\\label{app:fisher}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Fisher combined $p$-values for signal comparisons (SciERC NER, 3 seeds).}\n\\label{tab:fisher}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$p_{42}$} & \\textbf{$p_{123}$} & \\textbf{$p_{789}$} & \\textbf{Fisher $p$} \\\\\n\\midrule\nSJ $>$ LP & .002 & .003 & .180 & .085 \\\\\nSJ $>$ FK & .005 & .004 & .120 & .032 \\\\\nVC $>$ LP & .001 & .001 & .038 & .018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Smoke Test Results}\n\\label{app:smoke}\n\nA 1-epoch LoRA fine-tune on Few-NERD with 200 instances served as a pilot experiment (exp-020).\nGreedy F1=0.718, oracle F1=0.828, degeneracy rate=10.1\\%, parse rate=0.985.\nLP selection F1=0.740 (+2.2pp over greedy), directionally positive but below statistical significance at $n{=}200$.\nThe smoke test confirmed data pipeline viability and model learnability, gating the full experiment (exp-021).\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3b0428a-4339-4c84-a733-4c52cf100d9b",
  "isSidechain": false,
  "requestId": "req_011Cb64255wySDVYnShFDqHv",
  "type": "assistant",
  "uuid": "a8843284-3085-4387-b9d4-ed35cbfaee83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVE1B2saqaVtugt9wzxaE1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 53813,
      "output_tokens": 15636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15636,
          "cache_read_input_tokens": 53813,
          "cache_creation_input_tokens": 6520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6520
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

_source line 22 · 2026-05-16T10:05:03.022Z_

<details><summary>↩ Tool result · `toolu_01GzEKT9w1tVqDsCyhvTTsmD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8843284-3085-4387-b9d4-ed35cbfaee83",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "76c5a816-394d-41cc-807b-833cdff5bfbf",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\\usepackage{tabularx}\n\\usepackage{array}\n\n\\newcolumntype{C}[1]{>{\\centering\\arraybackslash}p{#1}}\n\\newcommand{\\rmark}[1]{\\textsuperscript{#1}}\n\n\\title{When Does Multi-Sample Selection Help Structured IE?\\\\A Diagnostic Study of Output Convergence}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ===========================================================================\n%  ABSTRACT\n% ===========================================================================\n\\begin{abstract}\nTest-time scaling via multi-sample generation improves LLM performance on reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear.\nWe conduct a large-scale diagnostic study across four NER datasets (SciERC, CoNLL-2003, Few-NERD, WNUT-17), one RE dataset (SciERC), three model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and five confidence signal families.\nWe find that confidence signals \\emph{reliably} estimate output quality across instances (Spearman $\\rho$ up to 0.37, AUROC up to 0.75), yet their ability to \\emph{select} better candidates from multiple samples is \\textbf{regime-dependent}: under standard fine-tuning configurations that produce high output convergence (degeneracy 21--58\\%), no unsupervised signal significantly outperforms greedy decoding.\nHowever, when output diversity is preserved---through reduced fine-tuning intensity (LoRA rank 8 vs.\\ 16) or lower training epochs---log-probability selection recovers 3--4 percentage points over greedy ($p<0.03$).\nWe diagnose two mechanisms underlying selection failure: \\emph{instance degeneracy} (identical outputs across samples) and \\emph{log-probability compression} (within-instance score ranges $<$0.05 nats), and show that both are primarily driven by fine-tuning intensity rather than model capability alone.\nWe provide prescriptive guidelines: practitioners should assess output degeneracy rate and log-probability range to decide between multi-sample selection and greedy decoding.\n\\end{abstract}\n\n% ===========================================================================\n%  1  INTRODUCTION\n% ===========================================================================\n\\section{Introduction}\n\nTest-time scaling (TTS) strategies---generating multiple candidate outputs and selecting or aggregating the best---have yielded substantial improvements for LLM reasoning \\citep{wang2023selfconsistency,brown2024tts,snell2024scaling}.\nSelf-consistency~\\citep{wang2023selfconsistency} selects the majority answer among sampled chain-of-thought traces; best-of-$N$ with reward models~\\citep{cobbe2021gsm8k,lightman2023lets} ranks candidates by learned quality scores.\nA natural question arises: \\emph{can similar strategies improve structured information extraction?}\n\nStructured IE tasks---named entity recognition (NER) and relation extraction (RE)---produce \\emph{set-valued} outputs (entity sets, relation triples) whose quality is measured by token-level or tuple-level F1.\nUnlike discrete-answer reasoning, structured outputs admit partial credit and fine-grained quality variation, seemingly creating opportunity for selection.\nYet applying multi-sample strategies to structured IE requires confidence signals that can \\emph{rank} candidates within an instance---a requirement that goes beyond instance-level quality estimation.\n\nIn this work, we conduct a systematic diagnostic study of five unsupervised confidence signals across four NER datasets and one RE dataset, three model architectures, and controlled ablations of fine-tuning intensity.\nOur central finding is that the effectiveness of multi-sample selection is \\textbf{conditional on output convergence regime}:\n\n\\begin{itemize}\n\\item \\textbf{High-convergence regime} (degeneracy $>$20\\%, log-probability range $<$0.04 nats): Standard fine-tuning configurations produce outputs that are largely identical across samples. Selection is ineffective because there is nothing meaningful to select among. Greedy decoding ($T{=}0$) dominates at zero additional cost.\n\n\\item \\textbf{Low-convergence regime} (degeneracy $<$10\\%, log-probability range $>$0.07 nats): When fine-tuning is less aggressive---via lower LoRA rank or fewer training epochs---output diversity is preserved. Log-probability-based best-of-$N$ selection yields statistically significant gains of 3--4 percentage points over greedy ($p<0.03$).\n\\end{itemize}\n\nWe diagnose two failure mechanisms that explain selection ineffectiveness in the high-convergence regime.\nFirst, \\emph{instance degeneracy}: 21--58\\% of instances produce identical F1 scores across all $N{=}8$ samples, eliminating any selection headroom.\nSecond, \\emph{log-probability compression}: even among non-degenerate instances, within-instance log-probability ranges are compressed to a median of 0.018--0.041 nats, leaving insufficient signal for ranking.\n\nCritically, we show that output convergence is not an inevitable consequence of model capability---it is primarily driven by \\emph{fine-tuning intensity}.\nOn SciERC, reducing LoRA rank from 16 to 8 (same model, same data, same epochs) cuts degeneracy from 21\\% to 5.2\\% while sacrificing only 3.9 percentage points of greedy F1, and transforms log-probability selection from negligible (+0.6pp, $p{=}0.39$) to significant (+3.6pp, $p{=}0.015$).\nSimilarly, Few-NERD with 3-epoch training achieves F1=0.778 with only 5.4\\% degeneracy, enabling log-probability selection gains of +3.2pp ($p{=}0.028$)---despite having higher F1 than SciERC (0.664) where selection fails.\n\nOur contributions are:\n\\begin{enumerate}\n\\item A systematic evaluation of five confidence signal families for structured IE quality estimation across four datasets and three model configurations.\n\\item Identification of two failure mechanisms (instance degeneracy, log-probability compression) and evidence that both are driven by fine-tuning intensity rather than capability alone.\n\\item A controlled LoRA rank ablation providing causal evidence that output convergence is a tunable property of the training configuration.\n\\item Prescriptive guidelines for practitioners: assess degeneracy rate and log-probability range to determine whether multi-sample selection or greedy decoding is appropriate.\n\\end{enumerate}\n\n% ===========================================================================\n%  2  RELATED WORK\n% ===========================================================================\n\\section{Related Work}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency~\\citep{wang2023selfconsistency} aggregates reasoning traces via majority voting.\nRecent extensions include CISC~\\citep{cisc2025acl}, which uses confidence-weighted majority voting, Self-Certainty Best-of-$N$~\\citep{selfcertainty2026iclr}, which performs reward-free selection via KL-divergence, and ReASC~\\citep{reasc2026}, which adapts sampling to instance reliability.\nAtomic Self-Consistency~\\citep{atomicsc2024emnlp} decomposes long-form outputs into sub-claims.\nAll of these target reasoning tasks with discrete or decomposable answers; none address set-structured IE outputs.\nOur work is the first systematic study of multi-sample selection for structured IE, revealing that the output convergence properties of fine-tuned extraction models create qualitatively different challenges.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\nSemantic uncertainty~\\citep{kuhn2023semantic} clusters outputs by meaning; calibration methods~\\citep{guo2017calibration,kadavath2022language,desai2020calibration} align confidence with accuracy.\nRecent surveys~\\citep{uqsurvey2025acl,uqcalibsurvey2025} provide comprehensive overviews.\nSemantic Entropy Probes~\\citep{semanticprobes2024} enable low-cost estimation.\nSelfCheckGPT~\\citep{manakul2023selfcheckgpt} uses sampling consistency for hallucination detection.\nCoCoA~\\citep{cocoa2025neurips} combines confidence and consistency for MBR-based UQ in QA and summarization.\nThese methods evaluate quality at the instance level; we additionally evaluate \\emph{within-instance ranking} for candidate selection.\n\n\\paragraph{Consistency for Structured IE.}\n\\citet{nedellec2026consistency} study consistency--accuracy correlations for entity and relation extraction using surface-level string matching across four LLMs.\nThey acknowledge that their approach ``overlooks semantically consistent outputs.''\nOur structured Jaccard metric directly addresses this limitation by performing type-grouped Hungarian matching that captures partial structural agreement.\nMoreover, we go beyond correlation analysis to evaluate best-of-$N$ selection and diagnose why it fails.\n\n\\paragraph{Confidence in Information Extraction.}\nClassical IE confidence methods~\\citep{culotta2004confidence} rely on model internals (CRF marginals, sequence probabilities).\nToken-level NER uncertainty~\\citep{xiao2019quantifying,shelmanov2021certain,he2020towards} and structured calibration~\\citep{kuleshov2015calibrated,jagannatha2022calibrating} address the extraction setting.\nSelective prediction~\\citep{geifman2017selective,knowyourlimits2025tacl} abstains on uncertain instances.\nOur work differs by focusing on the gap between quality estimation (which works) and selection (which is regime-dependent).\n\n\\paragraph{MBR Decoding.}\nMinimum Bayes Risk decoding~\\citep{eikema2022map} selects outputs maximizing expected utility under a sample-based approximation.\nPrior MBR failure analyses attribute poor performance to utility function misalignment.\nOur failure mechanism is qualitatively different: the utility function (structured F1) \\emph{is} aligned with the confidence signal (within-instance $\\rho{=}0.52$), but instance degeneracy and score compression eliminate actionable selection headroom.\n\n% ===========================================================================\n%  3  METHODOLOGY\n% ===========================================================================\n\\section{Methodology}\n\n\\subsection{Task and Datasets}\n\nWe evaluate on four NER datasets and one RE dataset, chosen to span different entity densities, type granularities, and domains (\\Cref{tab:datasets}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dataset statistics. $|E|$/inst = mean entities per instance.}\n\\label{tab:datasets}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{Types} & \\textbf{$n$ (test)} & \\textbf{$|E|$/inst} \\\\\n\\midrule\nSciERC       & NER+RE & 6 NER, 7 RE & 529 / 397  & $\\sim$2.1 \\\\\nCoNLL-2003   & NER    & 4            & 2,756      & $\\sim$1.8 \\\\\nFew-NERD     & NER    & 8 (coarse)   & 4,506      & $\\sim$3.4 \\\\\nWNUT-17      & NER    & 6            & 1,287      & $\\sim$1.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{SciERC}~\\citep{luan2018scierc} provides scientific abstracts annotated for entities and relations, with fine-grained types and complex relation structures.\n\\textbf{CoNLL-2003}~\\citep{tjong2003conll} is the standard newswire NER benchmark with four coarse entity types.\n\\textbf{Few-NERD}~\\citep{ding2021fewnerd} (INTRA, coarse 8-type) features high entity density ($\\sim$3.4 entities/instance) with many multi-word entities, providing substantial boundary variation.\n\\textbf{WNUT-17}~\\citep{derczynski2017wnut} targets emerging and rare entities in social media text.\n\n\\subsection{Confidence Signals}\n\\label{sec:signals}\n\nWe evaluate five confidence signals spanning four families:\n\n\\paragraph{Structural Consistency.}\n\\textbf{Soft Jaccard (SJ)}: For each pair of samples, compute type-grouped Hungarian matching between entity (or relation) sets, then average pairwise Jaccard similarity across all $\\binom{N}{2}$ pairs.\nSJ captures partial structural agreement.\n\n\\textbf{Fleiss' Kappa (FK)}: Treat each token position as rated by $N$ annotators (samples), with categories being entity types (including O). Compute Fleiss' $\\kappa$ as inter-annotator agreement.\n\n\\textbf{Exact Match (EM)}: Fraction of sample pairs producing identical entity/relation sets. A strict binary signal.\n\n\\paragraph{Voting Confidence (VC).}\nFor each entity mention appearing in any sample, compute the fraction of samples containing it. Instance-level VC is the mean entity-level vote fraction.\n\n\\paragraph{Log-Probability (LP).}\nMean token-level log-probability of the generated output, computed from the model's own probability estimates. The only per-sample (not per-instance) signal.\n\n\\subsection{Models and Training}\n\n\\textbf{Primary model}: Qwen3-8B with LoRA fine-tuning. Default configuration: rank=16, $\\alpha$=32, 5 epochs for SciERC/CoNLL/WNUT, 3 epochs for Few-NERD.\n\\textbf{Scale ablation}: Qwen3-4B with matched hyperparameters.\n\\textbf{Cross-architecture}: LLaMA-3.1-8B with LoRA rank=32.\n\\textbf{Fine-tuning intensity ablation}: Qwen3-8B with LoRA rank=8, $\\alpha$=16, 5 epochs on SciERC.\n\nAll models are fine-tuned to generate structured JSON outputs containing entity mentions, types, and (for RE) relation triples.\n\n\\subsection{Inference and Evaluation}\n\\label{sec:eval}\n\nFor each test instance, we generate $N{=}8$ samples at temperature $T{=}1.0$ (unless stated otherwise) and compute all five confidence signals.\nEvaluation metrics:\n\n\\paragraph{Quality Estimation (QE).}\nSpearman $\\rho$ between signal value and instance-level F1, measuring cross-instance ranking ability. AUROC for binary discrimination (above/below median F1). Reported over 3 random seeds where available.\n\n\\paragraph{Selection.}\nBest-of-$N$: select the sample with the highest signal value; report its F1. Compared against greedy ($T{=}0$), random sample, and oracle (best F1 among $N$ samples). Statistical significance via bootstrap with 1000 iterations.\n\n\\paragraph{Convergence Diagnostics.}\n\\emph{Degeneracy rate}: fraction of instances where all $N$ samples produce identical F1.\n\\emph{LP compression}: median within-instance range of log-probability scores across $N$ samples (in nats).\n\n% ===========================================================================\n%  4  QUALITY ESTIMATION RESULTS\n% ===========================================================================\n\\section{Quality Estimation Results}\n\n\\subsection{Cross-Dataset NER Quality Estimation}\n\n\\Cref{tab:ner_qe} presents QE results across four NER datasets. Confidence signals provide moderate-to-strong quality estimation in all settings, with Spearman $\\rho$ ranging from 0.17 to 0.44.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{NER quality estimation (Spearman $\\rho$). SciERC and Few-NERD report 3-seed mean $\\pm$ SD. CoNLL and WNUT are single-seed. Best $\\rho$ per dataset in \\textbf{bold}.}\n\\label{tab:ner_qe}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Signal} & \\textbf{SciERC} & \\textbf{CoNLL} & \\textbf{Few-NERD} & \\textbf{WNUT} \\\\\n\\midrule\nVC   & \\textbf{.371}{\\scriptsize$\\pm$.030} & ---   & \\textbf{.295}{\\scriptsize$\\pm$.015} & --- \\\\\nSJ   & .343{\\scriptsize$\\pm$.053} & \\textbf{.436} & .216{\\scriptsize$\\pm$.019} & --- \\\\\nEM   & .292{\\scriptsize$\\pm$.020} & ---   & .212{\\scriptsize$\\pm$.015} & --- \\\\\nFK   & .258{\\scriptsize$\\pm$.037} & .400  & .173{\\scriptsize$\\pm$.009} & --- \\\\\nLP   & .219{\\scriptsize$\\pm$.013} & .307  & .275{\\scriptsize$\\pm$.015} & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge.\nFirst, all five signals provide meaningful QE across datasets---the worst signal family (FK on Few-NERD, $\\rho{=}0.173$) still exceeds chance.\nSecond, the \\emph{optimal signal depends on the dataset}: on SciERC, structural signals (VC, SJ) dominate log-probability ($\\rho{=}0.371$ vs.\\ 0.219); on Few-NERD, LP is competitive with structural signals ($\\rho{=}0.275$ vs.\\ VC 0.295) and significantly outperforms SJ ($\\rho{=}0.275$ vs.\\ 0.216).\nThird, on SciERC, VC consistently outperforms LP across seeds (Fisher combined $p{=}0.018$), while the SJ advantage over LP is borderline (Fisher $p{=}0.085$) due to seed-to-seed instability in SJ (CV=0.154 vs.\\ LP CV=0.059).\n\nOn CoNLL-2003, SJ achieves the highest $\\rho{=}0.436$.\nCross-model validation with LLaMA-3.1-8B on CoNLL yields SJ $\\rho{=}0.431$ and FK $\\rho{=}0.428$, confirming cross-architecture consistency.\n\nAUROC results on SciERC NER (seed 42) show EM achieves the best binary discrimination (0.749), followed by SJ (0.692) and VC (0.684), with LP lowest (0.578). EM excels at binary go/no-go decisions but ranks lower on Spearman $\\rho$ (0.295) due to its coarse-grained nature.\n\n\\subsection{Task Complexity: NER vs.\\ RE}\n\nSciERC relation extraction presents a qualitatively different challenge (\\Cref{tab:re_qe}).\nWith 43--48\\% of RE samples producing F1=0, the quality distribution is binary-dominated.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC RE quality estimation (3-seed mean $\\rho$). Signal rankings are unstable across seeds---no signal is consistently ranked first.}\n\\label{tab:re_qe}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Signal} & \\textbf{$\\rho$ (mean $\\pm$ SD)} & \\textbf{Rank-1 seeds} \\\\\n\\midrule\nVC   & .321 $\\pm$ .029 & 2 of 3 \\\\\nSJ   & .280 $\\pm$ .029 & 1 of 3 \\\\\nFK   & .280 $\\pm$ .035 & 0 of 3 \\\\\nLP   & .249 $\\pm$ .051 & 0 of 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLP's conditional $\\rho$ (conditioned on non-zero F1 samples) drops to 0.011 ($p{=}0.86$), confirming that LP's entire RE correlation comes from discriminating zero vs.\\ non-zero F1---it has no power for quality gradients within the model's capability range.\nRE signal rankings are unstable across seeds: seed 42 ranks VC first, seed 123 ranks FK first, seed 789 ranks SJ first.\nWe conclude that no unsupervised signal reliably ranks RE quality; all are weak and unstable under cross-seed variation.\n\n% ===========================================================================\n%  5  SELECTION EFFECTIVENESS\n% ===========================================================================\n\\section{Selection Effectiveness}\n\n\\subsection{When Selection Fails: High-Convergence Regimes}\n\nUnder standard fine-tuning configurations (LoRA rank=16, 5 epochs), multi-sample selection provides negligible or negative gains (\\Cref{tab:selection}).\n\nOn SciERC NER, the best signal (LP) achieves F1=0.650 vs.\\ greedy 0.644---a gain of +0.6pp that is not statistically significant (bootstrap $p{=}0.39$, 95\\% CI [$-$0.030, +0.042], Cohen's $d{=}0.038$).\nOn CoNLL NER, LP selection yields $-$1.0pp vs.\\ greedy ($p{=}0.62$).\nOn SciERC RE, greedy (F1=0.404) outperforms all signals; the best unsupervised method (LP, F1=0.395) is 0.9pp worse.\n\nScale ablation at 4B confirms the pattern: on SciERC NER, all signals perform \\emph{worse} than greedy (SJ $-$1.5pp, LP $-$2.2pp) despite 13pp of oracle headroom.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across conditions. $\\Delta$ = gap vs.\\ greedy in percentage points. Statistically significant gains ($p<0.05$) in \\textbf{bold}. Standard FT = LoRA rank=16, 5 epochs (3 for Few-NERD). Mild FT = LoRA rank=8, 5 epochs.}\n\\label{tab:selection}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Dataset} & \\textbf{Config} & \\textbf{Greedy} & \\textbf{LP Sel.} & \\textbf{$\\Delta$} & \\textbf{$p$} & \\textbf{Oracle} \\\\\n\\midrule\nSciERC NER  & Standard FT & .664 & .650 & +0.6  & .39  & .776 \\\\\nSciERC NER  & Mild FT     & .625 & .661 & \\textbf{+3.6}  & \\textbf{.015} & .812 \\\\\nFew-NERD    & 3 epochs    & .778 & .810 & \\textbf{+3.2}  & \\textbf{.028} & .869 \\\\\nCoNLL NER   & Standard FT & .912 & .902 & $-$1.0 & .62  & --- \\\\\n\\midrule\nSciERC RE   & Standard FT & .404 & .395 & $-$0.9 & ---  & .585 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{When Selection Succeeds: Preserved Output Diversity}\n\nTwo conditions independently demonstrate that selection \\emph{can} work:\n\n\\paragraph{Few-NERD (3-epoch training, rank=16).}\nDespite achieving high greedy F1 (0.778---higher than SciERC's 0.664), Few-NERD exhibits only 5.4\\% degeneracy.\nLP selection yields +3.2pp ($p{=}0.028$, Cohen's $d{=}0.152$, 95\\% CI [0.004, 0.060]).\nThis result directly contradicts any ``capability trap'' narrative that posits higher F1 necessarily implies higher degeneracy and useless selection.\n\n\\paragraph{SciERC with LoRA rank=8.}\nOn the \\emph{same} SciERC dataset where standard fine-tuning produces failed selection (+0.6pp, n.s.), reducing LoRA rank from 16 to 8 transforms the outcome: LP selection achieves +3.6pp ($p{=}0.015$, $d{=}0.168$, 95\\% CI [0.008, 0.064]).\nGreedy F1 drops from 0.664 to 0.625 ($-$3.9pp), but the selection gain more than compensates within the multi-sample framework: rank=8 with LP selection (0.661) is only 0.3pp below rank=16 greedy (0.664), while gaining uncertainty quantification capability.\n\n\\paragraph{Non-degenerate subset analysis.}\nOn SciERC (rank=16), restricting to the 40\\% of non-degenerate instances reveals LP selection gains of +2.9pp ($p{=}0.01$), with within-instance $\\rho$ jumping from 0.08 to 0.39.\nThe signal \\emph{works} where there is something to select among---the problem is that aggressive fine-tuning eliminates this headroom for most instances.\n\n% ===========================================================================\n%  6  DIAGNOSING OUTPUT CONVERGENCE\n% ===========================================================================\n\\section{Diagnosing Output Convergence}\n\n\\subsection{Instance Degeneracy}\n\nInstance degeneracy---the fraction of instances producing identical F1 across all $N{=}8$ samples---varies dramatically across conditions (\\Cref{tab:convergence}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output convergence diagnostics across conditions. Degen.\\ = degeneracy rate (\\%). LP range = median within-instance log-probability range (nats). Selection gain = LP best-of-$N$ vs.\\ greedy (pp).}\n\\label{tab:convergence}\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{F1} & \\textbf{Degen.\\ (\\%)} & \\textbf{LP range} & \\textbf{Sel.\\ gain} & \\textbf{$p$} \\\\\n\\midrule\nCoNLL r16 5ep         & .912 & 58.0 & 0.018 & $-$1.0 & .62 \\\\\nSciERC r16 5ep        & .664 & 21.0 & 0.041 & +0.6  & .39 \\\\\nSciERC 4B r16 5ep     & .662 & 10.4 & ---   & $-$2.2 & --- \\\\\nSciERC r8 5ep         & .625 &  5.2 & 0.074 & +3.6  & .015 \\\\\nFew-NERD r16 3ep      & .778 &  5.4 & 0.084 & +3.2  & .028 \\\\\nWNUT r16 5ep          & .523 &  0.0 & ---   & ---   & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nUnder standard fine-tuning, degeneracy correlates with greedy F1 across three datasets (CoNLL, SciERC, WNUT; $R^2{=}0.98$).\nHowever, adding Few-NERD to the regression collapses $R^2$ to 0.51: Few-NERD achieves F1=0.778 with only 5.4\\% degeneracy, producing a residual of 30.2 percentage points from the three-dataset regression line that would predict $\\sim$35--40\\% degeneracy.\nAdding the rank=8 SciERC data point further reduces $R^2$ to 0.35.\n\nThis demonstrates that \\textbf{model capability (F1) is not the primary driver of degeneracy}.\nThe same model (Qwen3-8B) on the same dataset (SciERC) produces 21\\% or 5.2\\% degeneracy depending solely on LoRA rank.\nFew-NERD's low degeneracy despite high F1 reflects both higher entity density (3.4 entities/instance, creating more boundary variation) and milder fine-tuning (3 epochs vs.\\ 5).\n\n\\subsection{Log-Probability Compression}\n\nLog-probability is the only per-sample signal capable of ranking candidates within an instance.\nHowever, within-instance LP ranges are severely compressed under high-convergence conditions.\n\nCoNLL exhibits a median LP range of only 0.018 nats---samples are nearly indistinguishable by log-probability.\nSciERC (rank=16) shows 0.041 nats.\nWhen convergence is reduced, LP ranges expand: SciERC rank=8 yields 0.074 nats (1.8$\\times$ wider than rank=16), and Few-NERD yields 0.084 nats (2.0$\\times$ wider than SciERC rank=16).\n\n\\paragraph{Free-form decoding ablation.}\nTo test whether LP compression is caused by constrained (JSON) decoding, we run an ablation with free-form output on SciERC.\nLP standard deviation is virtually unchanged: constrained $\\sigma{=}0.0206$ vs.\\ free-form $\\sigma{=}0.0199$ (ratio 0.97).\nTied fraction drops negligibly from 59.7\\% to 57.7\\%.\nParse rate remains 99.95\\%, confirming the fine-tuned model generates valid JSON without grammar constraints.\nThis proves LP compression is \\textbf{intrinsic to the model's output distribution}, not an artifact of decoding format.\n\n\\subsection{Convergence Drivers}\n\\label{sec:drivers}\n\nWe consolidate evidence from six experimental conditions to identify convergence drivers (\\Cref{tab:drivers}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Degeneracy drivers across conditions. FT intensity = combination of LoRA rank and training epochs.}\n\\label{tab:drivers}\n\\begin{tabular}{lcccl}\n\\toprule\n\\textbf{Condition} & \\textbf{F1} & \\textbf{Degen.\\ (\\%)} & \\textbf{LoRA/Epochs} & \\textbf{Primary driver} \\\\\n\\midrule\nCoNLL r16 5ep     & .912 & 58.0 & 16 / 5 & high F1 + aggressive FT \\\\\nSciERC r16 5ep    & .664 & 21.0 & 16 / 5 & moderate F1 + aggressive FT \\\\\nSciERC r8 5ep     & .625 &  5.2 & 8 / 5  & moderate F1 + \\textbf{mild FT} \\\\\nFew-NERD r16 3ep  & .778 &  5.4 & 16 / 3 & high F1 + \\textbf{mild FT} \\\\\nSciERC 4B r16 5ep & .662 & 10.4 & 16 / 5 & lower capacity + aggressive FT \\\\\nWNUT r16 5ep      & .523 &  0.0 & 16 / 5 & low F1 (no convergence) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe key comparison is SciERC rank=16 (21\\% degeneracy) vs.\\ rank=8 (5.2\\% degeneracy): same model, same data, same training epochs---only LoRA rank differs.\nThis controlled experiment isolates fine-tuning intensity as the primary degeneracy driver.\n\nFew-NERD provides complementary evidence along the epoch dimension: 3 epochs produce 5.4\\% degeneracy at F1=0.778, while CoNLL with 5 epochs produces 58\\% degeneracy at F1=0.912.\nThe F1 difference (0.134) would predict $\\sim$30pp degeneracy difference under a capability-only model; the actual difference is 52.6pp, far exceeding what F1 alone explains.\n\nEntity density also contributes: Few-NERD's $\\sim$3.4 entities per instance create more combinatorial variation in boundary positions than SciERC's $\\sim$2.1 or CoNLL's $\\sim$1.8, mechanically reducing the probability that all $N$ samples produce identical entity sets.\n\n\\subsection{LoRA Rank Ablation: Causal Evidence}\n\\label{sec:ablation}\n\nThe LoRA rank=8 ablation on SciERC provides the strongest evidence that convergence is a controllable training parameter (\\Cref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LoRA rank ablation on SciERC NER ($N{=}8$, $T{=}1.0$, $n{=}529$). Rank=8 preserves output diversity at modest F1 cost.}\n\\label{tab:ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Rank=16} & \\textbf{Rank=8} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGreedy F1           & .664   & .625   & $-$3.9pp \\\\\nOracle F1           & .776   & .812   & +3.7pp \\\\\nOracle headroom     & 10.9pp & 18.7pp & +7.9pp \\\\\nDegeneracy          & 21.0\\% &  5.2\\% & $-$15.8pp \\\\\n\\midrule\nSJ $\\rho$           & .360   & .378   & +0.018 \\\\\nLP $\\rho$           & .205   & .252   & +0.047 \\\\\nVC $\\rho$           & .379   & .408   & +0.029 \\\\\n\\midrule\nLP sel.\\ gap (pp)   & +0.6   & +3.6   & +3.0pp \\\\\nLP sel.\\ $p$        & .39    & .015   & --- \\\\\nSJ sel.\\ gap (pp)   & $-$1.9 & +2.8   & +4.7pp \\\\\nSJ sel.\\ $p$        & ---    & .042   & --- \\\\\n\\midrule\nLP range (nats)     & 0.041  & 0.074  & +0.033 \\\\\nTied fraction       & 21.0\\% &  5.2\\% & $-$15.8pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral findings are noteworthy:\n\n\\paragraph{QE is decoupled from selection.}\nQE correlations are \\emph{stable} across rank configurations: SJ $\\rho$ changes by only +0.018 (0.360$\\to$0.378).\nSelection effectiveness changes \\emph{dramatically}: LP selection gap moves from +0.6pp (n.s.) to +3.6pp ($p{=}0.015$).\nThis decoupling demonstrates that QE is an intrinsic property of the signal, while selection effectiveness is regime-dependent---governed by the output convergence properties of the fine-tuning configuration.\n\n\\paragraph{Trade-off quantification.}\nEach 1pp of greedy F1 sacrificed by reducing LoRA rank buys a 4.1$\\times$ reduction in degeneracy (3.9pp F1 cost / 15.8pp degeneracy reduction).\nThe practical implication is that rank=8 with LP selection (F1=0.661) is only 0.3pp below rank=16 greedy (0.664), while providing calibrated uncertainty estimates as a bonus.\n\n\\paragraph{Oracle headroom expansion.}\nRank=8's oracle F1 (0.812) is 3.7pp \\emph{higher} than rank=16's oracle (0.776), despite lower greedy F1.\nMore diverse outputs span a wider region of output space, providing better candidates for an ideal selector.\nThis confirms that reducing fine-tuning intensity preserves the information needed for effective selection.\n\n% ===========================================================================\n%  7  CROSS-SEED AND CROSS-MODEL STABILITY\n% ===========================================================================\n\\section{Robustness Analysis}\n\n\\subsection{Cross-Seed Stability}\n\nThree-seed evaluation on SciERC NER reveals important stability differences (\\Cref{tab:seeds}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER 3-seed QE ($\\rho$, $N{=}8$, $T{=}1.0$, $n{=}529$). CV = coefficient of variation.}\n\\label{tab:seeds}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Signal} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 789} & \\textbf{Mean} & \\textbf{CV} \\\\\n\\midrule\nVC  & .379 & .395 & .338 & .371 & .081 \\\\\nSJ  & .360 & .385 & .285 & .343 & .154 \\\\\nEM  & .295 & .310 & .272 & .292 & .068 \\\\\nFK  & .267 & .290 & .218 & .258 & .143 \\\\\nLP  & .205 & .225 & .228 & .219 & .059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSJ exhibits the highest variability (CV=0.154): seed 789 yields SJ $\\rho{=}0.285$, close to LP's 0.228, while seeds 42 and 123 show a clear SJ advantage.\nFisher's combined test for SJ$>$LP gives $p{=}0.085$---borderline at $\\alpha{=}0.05$.\nIn contrast, VC$>$LP is robust ($p{=}0.018$), and LP is the most stable signal (CV=0.059).\nFor SciERC RE, signal rankings are completely unstable across seeds (three different top-1 signals), leading us to conclude that no unsupervised signal reliably ranks RE quality at current sample sizes.\n\n\\subsection{Cross-Model Validation}\n\nLLaMA-3.1-8B on CoNLL NER produces SJ $\\rho{=}0.431$ and FK $\\rho{=}0.428$, closely matching Qwen3-8B (SJ $\\rho{=}0.436$, FK $\\rho{=}0.400$).\nBoth models exhibit high degeneracy and ineffective selection on CoNLL under aggressive fine-tuning, confirming that convergence patterns are architecture-independent under matched training intensity.\n\nThe Qwen3-4B scale ablation on SciERC yields SJ $\\rho{=}0.422$ ($\\ge$ 8B's 0.343 three-seed mean), demonstrating that QE correlations are maintained or even improved at smaller scale.\nHowever, 4B selection is equally ineffective: SJ $-$1.5pp, LP $-$2.2pp vs.\\ greedy on SciERC NER, confirming that the correlation--selection gap persists across model sizes.\n\n% ===========================================================================\n%  8  PRESCRIPTIVE GUIDELINES\n% ===========================================================================\n\\section{Prescriptive Guidelines}\n\nBased on our empirical findings, we propose a decision matrix for practitioners (\\Cref{tab:guidelines}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Prescriptive decision matrix for multi-sample selection in structured IE.}\n\\label{tab:guidelines}\n\\begin{tabular}{p{2.3cm}p{2cm}p{4.5cm}c}\n\\toprule\n\\textbf{Degeneracy} & \\textbf{LP Range} & \\textbf{Recommendation} & \\textbf{Gain} \\\\\n\\midrule\n$<$10\\% & $>$0.07 nats & LP best-of-$N$ selection & 2--4pp \\\\\n10--20\\% & 0.04--0.07 & Evaluate on dev set; marginal & 0--2pp \\\\\n$>$20\\% & $<$0.04 & $T{=}0$ greedy decoding & 0pp \\\\\n\\midrule\n\\multicolumn{2}{l}{RE with $>$40\\% zero-F1} & Supervised verifier or greedy & 0pp\\rmark{$\\dagger$} \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\scriptsize \\rmark{$\\dagger$} No unsupervised signal reliably helps; supervised approaches are future work.}\n\\end{tabular}\n\\end{table}\n\n\\paragraph{How to diagnose the regime.}\nBefore deploying multi-sample inference, run a pilot on a small development set ($n \\ge 200$) with $N{=}8$ samples at $T{=}1.0$.\nCompute the degeneracy rate (fraction of instances with identical outputs across all samples) and the median within-instance LP range.\nIf degeneracy $<$10\\% and LP range $>$0.07 nats, LP-based best-of-$N$ is likely beneficial.\n\n\\paragraph{How to control the regime.}\nIf the standard fine-tuning configuration produces high convergence, practitioners can reduce LoRA rank (our evidence: rank 16$\\to$8 cuts degeneracy from 21\\% to 5.2\\% at 3.9pp F1 cost) or reduce training epochs.\nThe trade-off is explicit: each percentage point of greedy F1 sacrificed yields approximately 4$\\times$ degeneracy reduction, and LP selection can recover much of the sacrificed F1.\n\n\\paragraph{Signal choice.}\nLP is the recommended selection signal because it is the only per-sample signal and shows the most consistent selection gains.\nFor quality estimation (instance-level), VC and SJ provide stronger correlations on entity-rich datasets, but the optimal QE signal is dataset-dependent.\n\n% ===========================================================================\n%  9  DISCUSSION\n% ===========================================================================\n\\section{Discussion}\n\n\\paragraph{Reinterpreting the capability--convergence relationship.}\nA naive analysis of three datasets (CoNLL, SciERC, WNUT) suggests a tight relationship between model capability (F1) and output degeneracy ($R^2{=}0.98$), tempting the conclusion that better models inevitably produce less diverse outputs.\nHowever, Few-NERD and the LoRA rank ablation break this narrative: F1 explains at most 35--51\\% of degeneracy variance when these additional data points are included.\nFine-tuning intensity (LoRA rank, training epochs) and dataset properties (entity density, type granularity) are equally or more important determinants.\nThis has practical implications: practitioners need not accept convergence as an unavoidable consequence of training a good model---they can actively manage it.\n\n\\paragraph{QE vs.\\ selection: a fundamental decoupling.}\nOur results reveal that quality estimation and selection are governed by different factors.\nQE correlation ($\\rho$ between signal and F1) is an intrinsic property of the signal and the task, robust to changes in fine-tuning intensity (SJ $\\rho$ changes by only 0.018 between rank=16 and rank=8).\nSelection effectiveness depends on the \\emph{convergence regime}: the same signals that produce useful QE rankings across instances fail to select within instances when outputs are too similar.\nThis distinction is important for system design: QE is always useful for flagging uncertain instances (selective prediction, human-in-the-loop), even when selection fails.\n\n\\paragraph{Comparison with reasoning TTS.}\nIn reasoning tasks, self-consistency works because candidate answers are discrete and diverse: the model genuinely ``considers'' different solution paths.\nIn fine-tuned structured IE, the model has learned a dominant extraction pattern, and sampling merely introduces boundary noise around this pattern.\nThe fundamental difference is that reasoning diversity arises from \\emph{multiple valid solution strategies}, while IE sampling diversity (when present) arises from \\emph{boundary perturbations} around a single learned extraction strategy.\n\n\\paragraph{Limitations.}\n(1) We evaluate one primary model family (Qwen3) with LLaMA and 4B as secondary validations; larger models ($>$70B) remain untested.\n(2) All experiments use LoRA fine-tuning; full fine-tuning or in-context learning may produce different convergence dynamics.\n(3) Our prescriptive thresholds (degeneracy 10\\%, LP range 0.07) are derived from four NER datasets and one RE dataset---validation on additional domains (biomedical, legal, multilingual) is needed.\n(4) We do not evaluate supervised verifiers, which could close the selection gap even under high convergence; this is important future work.\n(5) WNUT results are limited due to low model capability on out-of-distribution entities.\n\n% ===========================================================================\n%  10  CONCLUSION\n% ===========================================================================\n\\section{Conclusion}\n\nWe present a diagnostic study of multi-sample selection for structured information extraction across four NER datasets, three model configurations, and five confidence signal families.\nOur central finding is that selection effectiveness is regime-dependent: under standard fine-tuning configurations that induce high output convergence, no unsupervised signal outperforms greedy decoding; but when output diversity is preserved through reduced fine-tuning intensity, log-probability selection yields statistically significant gains of 3--4 percentage points.\n\nWe identify two mechanisms (instance degeneracy and log-probability compression) that underlie selection failure and provide causal evidence---via a controlled LoRA rank ablation---that both are driven primarily by fine-tuning intensity rather than model capability.\nThese findings lead to actionable guidelines: practitioners should diagnose their fine-tuning regime's convergence properties before investing in multi-sample inference, and can actively control these properties through training configuration choices.\n\n% ===========================================================================\n%  REFERENCES (placeholder)\n% ===========================================================================\n\\begingroup\n\\small\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Brown et~al.(2024)]{brown2024tts}\nB.~Brown, J.~Juravsky, R.~Ehrlich, R.~Clark, Q.~V.~Le, C.~R\\'{e}, and A.~Roshan~Ghias.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nC.~Snell, J.~Lee, K.~Xu, and A.~Kumar.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023lets}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[CISC(2025)]{cisc2025acl}\nConfidence-weighted majority voting for reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[Self-Certainty(2026)]{selfcertainty2026iclr}\nSelf-certainty best-of-{N}: Reward-free selection via {KL}-divergence.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[ReASC(2026)]{reasc2026}\nReliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[Atomic SC(2024)]{atomicsc2024emnlp}\nAtomic self-consistency for long-form text.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nL.~Kuhn, Y.~Gal, and S.~Farquhar.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nC.~Guo, G.~Pleiss, Y.~Sun, and K.~Q.~Weinberger.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Kadavath et~al.(2022)]{kadavath2022language}\nS.~Kadavath et~al.\n\\newblock Language models (mostly) know what they know.\n\\newblock \\emph{arXiv:2207.05221}, 2022.\n\n\\bibitem[Desai and Durrett(2020)]{desai2020calibration}\nS.~Desai and G.~Durrett.\n\\newblock Calibration of pre-trained transformers.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[UQ Survey(2025)]{uqsurvey2025acl}\nUncertainty quantification for {LLMs}: A comprehensive survey.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[UQ+Calibration Survey(2025)]{uqcalibsurvey2025}\nUncertainty quantification and calibration in large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[Semantic Probes(2024)]{semanticprobes2024}\nSemantic entropy probes: Low-cost uncertainty estimation.\n\\newblock 2024.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nP.~Manakul, A.~Liusie, and M.~J.~F.~Gales.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[CoCoA(2025)]{cocoa2025neurips}\nM.~Vashurin et~al.\n\\newblock {CoCoA}: Combining confidence and consistency for {MBR}-based uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[N\\'{e}dellec and Xia(2026)]{nedellec2026consistency}\nC.~N\\'{e}dellec and R.~Xia.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLMs} for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nA.~Culotta and A.~McCallum.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019quantifying}\nY.~Xiao and W.~Y.~Wang.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021certain}\nA.~Shelmanov et~al.\n\\newblock How certain is your {Transformer}?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[He et~al.(2020)]{he2020towards}\nJ.~He, X.~Zhong, J.~Su, and P.~Zhang.\n\\newblock Towards better uncertainty estimation for {NER}.\n\\newblock 2020.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibrated}\nV.~Kuleshov and P.~Liang.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibrating}\nA.~Jagannatha and H.~Yu.\n\\newblock Calibrating structured output predictors.\n\\newblock 2022.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nY.~Geifman and R.~El-Yaniv.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Know Your Limits(2025)]{knowyourlimits2025tacl}\nKnow your limits: A survey on abstention in {NLP}.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[Eikema et~al.(2022)]{eikema2022map}\nB.~Eikema and W.~Aziz.\n\\newblock Is {MAP} decoding all you need? {The} inadequacy of the mode in neural machine translation.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Luan et~al.(2018)]{luan2018scierc}\nY.~Luan, L.~He, M.~Ostendorf, and H.~Hajishirzi.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nE.~F.~Tjong Kim~Sang and F.~De~Meulder.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[Ding et~al.(2021)]{ding2021fewnerd}\nN.~Ding, G.~Xu, Y.~Chen, X.~Wang, Z.~Han, P.~Xie, H.~Zheng, and Z.~Liu.\n\\newblock {Few-NERD}: A few-shot named entity recognition dataset.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Derczynski et~al.(2017)]{derczynski2017wnut}\nL.~Derczynski, E.~Nichols, M.~van Erp, and N.~Limsopatham.\n\\newblock Results of the {WNUT}2017 shared task on novel and emerging entity recognition.\n\\newblock In \\emph{W-NUT}, 2017.\n\n\\end{thebibliography}\n\\endgroup\n\n% ===========================================================================\n%  APPENDIX\n% ===========================================================================\n\\appendix\n\n\\section{Few-NERD Detailed Results}\n\\label{app:fewnerd}\n\n\\Cref{tab:fewnerd_full} presents the full Few-NERD QE results across three seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD NER QE metrics (3-seed, $N{=}8$, $T{=}1.0$, $n{=}4506$).}\n\\label{tab:fewnerd_full}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Signal} & \\textbf{$\\rho$} & \\textbf{SD} & \\textbf{AUROC} & \\textbf{Sel.\\ F1} & \\textbf{$\\Delta$ (pp)} & \\textbf{$p$} \\\\\n\\midrule\nLP     & .275 & .015 & .658 & .810 & +3.2 & .028 \\\\\nVC     & .295 & .015 & .681 & .799 & +2.1 & .065 \\\\\nSJ     & .216 & .019 & .624 & .793 & +1.5 & .12 \\\\\nEM     & .212 & .015 & .718 & .793 & +1.5 & .13 \\\\\nFK     & .173 & .009 & .588 & .790 & +1.2 & .18 \\\\\n\\midrule\ngreedy & ---  & ---  & ---  & .778 & ---  & --- \\\\\noracle & ---  & ---  & ---  & .869 & +9.1 & --- \\\\\nrandom & ---  & ---  & ---  & .765 & $-$1.3 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SciERC RE Cross-Seed Signal Rankings}\n\\label{app:re_seeds}\n\n\\Cref{tab:re_rankings} demonstrates the instability of RE signal rankings across seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SciERC RE signal rankings by Spearman $\\rho$ (full set, 3 seeds).}\n\\label{tab:re_rankings}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Rank 1} & \\textbf{Rank 2} & \\textbf{Rank 3} & \\textbf{Rank 4} & \\textbf{Rank 5} \\\\\n\\midrule\n42  & VC (.350) & FK (.275) & LP (.266) & SJ (.250) & EM (.134) \\\\\n123 & VC (.320) & FK (.317) & LP (.290) & SJ (.283) & EM (.170) \\\\\n789 & SJ (.308) & VC (.293) & FK (.248) & EM (.198) & LP (.192) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Fisher Combined P-Values}\n\\label{app:fisher}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Fisher combined $p$-values for signal comparisons (SciERC NER, 3 seeds).}\n\\label{tab:fisher}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$p_{42}$} & \\textbf{$p_{123}$} & \\textbf{$p_{789}$} & \\textbf{Fisher $p$} \\\\\n\\midrule\nSJ $>$ LP & .002 & .003 & .180 & .085 \\\\\nSJ $>$ FK & .005 & .004 & .120 & .032 \\\\\nVC $>$ LP & .001 & .001 & .038 & .018 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Smoke Test Results}\n\\label{app:smoke}\n\nA 1-epoch LoRA fine-tune on Few-NERD with 200 instances served as a pilot experiment (exp-020).\nGreedy F1=0.718, oracle F1=0.828, degeneracy rate=10.1\\%, parse rate=0.985.\nLP selection F1=0.740 (+2.2pp over greedy), directionally positive but below statistical significance at $n{=}200$.\nThe smoke test confirmed data pipeline viability and model learnability, gating the full experiment (exp-021).\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "a8843284-3085-4387-b9d4-ed35cbfaee83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "76c5a816-394d-41cc-807b-833cdff5bfbf",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260516T092241",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Assistant

_source line 25 · 2026-05-16T10:05:05.508Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76c5a816-394d-41cc-807b-833cdff5bfbf",
  "isSidechain": false,
  "requestId": "req_011Cb64PpoaeYZ2bS8g2FoDK",
  "type": "assistant",
  "uuid": "dff70602-e8e5-4d1b-8d90-ad3ff85dfd8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxqV48dbjGHRb4vjSkN5WQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15703,
      "cache_read_input_tokens": 60333,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 60333,
          "cache_creation_input_tokens": 15703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15703
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

_source line 26 · 2026-05-16T10:05:06.727Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01D69kmaJbTmbyvyR7jdhAs3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dff70602-e8e5-4d1b-8d90-ad3ff85dfd8d",
  "isSidechain": false,
  "requestId": "req_011Cb64PpoaeYZ2bS8g2FoDK",
  "type": "assistant",
  "uuid": "a9898add-b5df-4401-8ba7-c817b528522d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxqV48dbjGHRb4vjSkN5WQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15703,
      "cache_read_input_tokens": 60333,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 60333,
          "cache_creation_input_tokens": 15703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15703
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

_source line 27 · 2026-05-16T10:05:09.387Z_

<details><summary>↩ Tool result · `toolu_01D69kmaJbTmbyvyR7jdhAs3`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/cleveref/cleveref.sty)
==> First Aid for cleveref.sty applied!
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

Package natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined 
on input line 45.


Package natbib Warning: Citation `brown2024tts' on page 1 undefined on input li
ne 45.


Package natbib Warning: Citation `snell2024scaling' on page 1 undefined on inpu
t line 45.


Package natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined 
on input line 46.


Package natbib Warning: Citation `cobbe2021gsm8k' on page 1 undefined on input 
line 46.


Package natbib Warning: Citation `lightman2023lets' on page 1 undefined on inpu
t line 46.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]

Package natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined 
on input line 84.


Package natbib Warning: Citation `cisc2025acl' on page 2 undefined on input lin
e 85.


Package natbib Warning: Citation `selfcertainty2026iclr' on page 2 undefined on
 input line 85.


Package natbib Warning: Citation `reasc2026' on page 2 undefined on input line 
85.


Package natbib Warning: Citation `atomicsc2024emnlp' on page 2 undefined on inp
ut line 86.


Package natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu
t line 91.


Package natbib Warning: Citation `guo2017calibration' on page 2 undefined on in
put line 91.


Package natbib Warning: Citation `kadavath2022language' on page 2 undefined on 
input line 91.


Package natbib Warning: Citation `desai2020calibration' on page 2 undefined on 
input line 91.


Package natbib Warning: Citation `uqsurvey2025acl' on page 2 undefined on input
 line 92.


Package natbib Warning: Citation `uqcalibsurvey2025' on page 2 undefined on inp
ut line 92.


Package natbib Warning: Citation `semanticprobes2024' on page 2 undefined on in
put line 93.


Package natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined 
on input line 94.


Package natbib Warning: Citation `cocoa2025neurips' on page 2 undefined on inpu
t line 95.


Package natbib Warning: Citation `nedellec2026consistency' on page 2 undefined 
on input line 99.


Package natbib Warning: Citation `culotta2004confidence' on page 2 undefined on
 input line 105.


Package natbib Warning: Citation `xiao2019quantifying' on page 2 undefined on i
nput line 106.


Package natbib Warning: Citation `shelmanov2021certain' on page 2 undefined on 
input line 106.


Package natbib Warning: Citation `he2020towards' on page 2 undefined on input l
ine 106.


Package natbib Warning: Citation `kuleshov2015calibrated' on page 2 undefined o
n input line 106.


Package natbib Warning: Citation `jagannatha2022calibrating' on page 2 undefine
d on input line 106.


Package natbib Warning: Citation `geifman2017selective' on page 2 undefined on 
input line 107.


Package natbib Warning: Citation `knowyourlimits2025tacl' on page 2 undefined o
n input line 107.

[2]

Package natbib Warning: Citation `eikema2022map' on page 3 undefined on input l
ine 111.


LaTeX Warning: Reference `tab:datasets' on page 1 undefined on input line 122.


Package natbib Warning: Citation `luan2018scierc' on page 3 undefined on input 
line 141.


Package natbib Warning: Citation `tjong2003conll' on page 3 undefined on input 
line 142.


Package natbib Warning: Citation `ding2021fewnerd' on page 3 undefined on input
 line 143.


Package natbib Warning: Citation `derczynski2017wnut' on page 3 undefined on in
put line 144.

[3]

LaTeX Warning: Reference `tab:ner_qe' on page 1 undefined on input line 197.

[4]

LaTeX Warning: Reference `tab:re_qe' on page 1 undefined on input line 229.


LaTeX Warning: Reference `tab:selection' on page 1 undefined on input line 260.


[5]

LaTeX Warning: Reference `tab:convergence' on page 1 undefined on input line 31
1.

[6]

LaTeX Warning: Reference `tab:drivers' on page 1 undefined on input line 359.


LaTeX Warning: Reference `tab:ablation' on page 1 undefined on input line 391.


Overfull \hbox (6.39282pt too wide) in paragraph at lines 434--437
 []\T1/ptm/b/n/10.95 Oracle head-room ex-pan-sion.[] \T1/ptm/m/n/10.95 Rank=8's
 or-a-cle F1 (0.812) is 3.7pp \T1/ptm/m/it/10.95 higher \T1/ptm/m/n/10.95 than 
rank=16's or-a-cle (0.776),
[7]

LaTeX Warning: Reference `tab:seeds' on page 1 undefined on input line 445.


LaTeX Warning: Reference `tab:guidelines' on page 1 undefined on input line 483
.

[8] [9] [10]

LaTeX Warning: Reference `tab:fewnerd_full' on page 1 undefined on input line 7
27.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:re_rankings' on page 1 undefined on input line 75
4.


LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: `h' float specifier changed to `ht'.

[11]

Package natbib Warning: There were undefined citations.

[12] [13] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (13 pages, 183781 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/cleveref/cleveref.sty)
==> First Aid for cleveref.sty applied!
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}] [2]
Overfull \hbox (8.47104pt too wide) in paragraph at lines 105--109
[]\T1/ptm/m/n/10.95 2004[]) rely on model in-ter-nals (CRF marginals, se-quence
 prob-a-bil-i-ties). Token-level NER un-cer-tainty ([]Xiao
[3] [4] [5] [6] [7]
Overfull \hbox (6.39282pt too wide) in paragraph at lines 434--437
 []\T1/ptm/b/n/10.95 Oracle head-room ex-pan-sion.[] \T1/ptm/m/n/10.95 Rank=8's
 or-a-cle F1 (0.812) is 3.7pp \T1/ptm/m/it/10.95 higher \T1/ptm/m/n/10.95 than 
rank=16's or-a-cle (0.776),
[8] [9] [10]

LaTeX Warning: `h' float specifier changed to `ht'.

[11] [12] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 188717 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9898add-b5df-4401-8ba7-c817b528522d",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "8090ae43-7c1f-4c1b-9f28-08c5b06c7f80",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/cleveref/cleveref.sty)\n==> First Aid for cleveref.sty applied!\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined \non input line 45.\n\n\nPackage natbib Warning: Citation `brown2024tts' on page 1 undefined on input li\nne 45.\n\n\nPackage natbib Warning: Citation `snell2024scaling' on page 1 undefined on inpu\nt line 45.\n\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined \non input line 46.\n\n\nPackage natbib Warning: Citation `cobbe2021gsm8k' on page 1 undefined on input \nline 46.\n\n\nPackage natbib Warning: Citation `lightman2023lets' on page 1 undefined on inpu\nt line 46.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined \non input line 84.\n\n\nPackage natbib Warning: Citation `cisc2025acl' on page 2 undefined on input lin\ne 85.\n\n\nPackage natbib Warning: Citation `selfcertainty2026iclr' on page 2 undefined on\n input line 85.\n\n\nPackage natbib Warning: Citation `reasc2026' on page 2 undefined on input line \n85.\n\n\nPackage natbib Warning: Citation `atomicsc2024emnlp' on page 2 undefined on inp\nut line 86.\n\n\nPackage natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu\nt line 91.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 2 undefined on in\nput line 91.\n\n\nPackage natbib Warning: Citation `kadavath2022language' on page 2 undefined on \ninput line 91.\n\n\nPackage natbib Warning: Citation `desai2020calibration' on page 2 undefined on \ninput line 91.\n\n\nPackage natbib Warning: Citation `uqsurvey2025acl' on page 2 undefined on input\n line 92.\n\n\nPackage natbib Warning: Citation `uqcalibsurvey2025' on page 2 undefined on inp\nut line 92.\n\n\nPackage natbib Warning: Citation `semanticprobes2024' on page 2 undefined on in\nput line 93.\n\n\nPackage natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined \non input line 94.\n\n\nPackage natbib Warning: Citation `cocoa2025neurips' on page 2 undefined on inpu\nt line 95.\n\n\nPackage natbib Warning: Citation `nedellec2026consistency' on page 2 undefined \non input line 99.\n\n\nPackage natbib Warning: Citation `culotta2004confidence' on page 2 undefined on\n input line 105.\n\n\nPackage natbib Warning: Citation `xiao2019quantifying' on page 2 undefined on i\nnput line 106.\n\n\nPackage natbib Warning: Citation `shelmanov2021certain' on page 2 undefined on \ninput line 106.\n\n\nPackage natbib Warning: Citation `he2020towards' on page 2 undefined on input l\nine 106.\n\n\nPackage natbib Warning: Citation `kuleshov2015calibrated' on page 2 undefined o\nn input line 106.\n\n\nPackage natbib Warning: Citation `jagannatha2022calibrating' on page 2 undefine\nd on input line 106.\n\n\nPackage natbib Warning: Citation `geifman2017selective' on page 2 undefined on \ninput line 107.\n\n\nPackage natbib Warning: Citation `knowyourlimits2025tacl' on page 2 undefined o\nn input line 107.\n\n[2]\n\nPackage natbib Warning: Citation `eikema2022map' on page 3 undefined on input l\nine 111.\n\n\nLaTeX Warning: Reference `tab:datasets' on page 1 undefined on input line 122.\n\n\nPackage natbib Warning: Citation `luan2018scierc' on page 3 undefined on input \nline 141.\n\n\nPackage natbib Warning: Citation `tjong2003conll' on page 3 undefined on input \nline 142.\n\n\nPackage natbib Warning: Citation `ding2021fewnerd' on page 3 undefined on input\n line 143.\n\n\nPackage natbib Warning: Citation `derczynski2017wnut' on page 3 undefined on in\nput line 144.\n\n[3]\n\nLaTeX Warning: Reference `tab:ner_qe' on page 1 undefined on input line 197.\n\n[4]\n\nLaTeX Warning: Reference `tab:re_qe' on page 1 undefined on input line 229.\n\n\nLaTeX Warning: Reference `tab:selection' on page 1 undefined on input line 260.\n\n\n[5]\n\nLaTeX Warning: Reference `tab:convergence' on page 1 undefined on input line 31\n1.\n\n[6]\n\nLaTeX Warning: Reference `tab:drivers' on page 1 undefined on input line 359.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 1 undefined on input line 391.\n\n\nOverfull \\hbox (6.39282pt too wide) in paragraph at lines 434--437\n []\\T1/ptm/b/n/10.95 Oracle head-room ex-pan-sion.[] \\T1/ptm/m/n/10.95 Rank=8's\n or-a-cle F1 (0.812) is 3.7pp \\T1/ptm/m/it/10.95 higher \\T1/ptm/m/n/10.95 than \nrank=16's or-a-cle (0.776),\n[7]\n\nLaTeX Warning: Reference `tab:seeds' on page 1 undefined on input line 445.\n\n\nLaTeX Warning: Reference `tab:guidelines' on page 1 undefined on input line 483\n.\n\n[8] [9] [10]\n\nLaTeX Warning: Reference `tab:fewnerd_full' on page 1 undefined on input line 7\n27.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:re_rankings' on page 1 undefined on input line 75\n4.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11]\n\nPackage natbib Warning: There were undefined citations.\n\n[12] [13] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (13 pages, 183781 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/cleveref/cleveref.sty)\n==> First Aid for cleveref.sty applied!\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}] [2]\nOverfull \\hbox (8.47104pt too wide) in paragraph at lines 105--109\n[]\\T1/ptm/m/n/10.95 2004[]) rely on model in-ter-nals (CRF marginals, se-quence\n prob-a-bil-i-ties). Token-level NER un-cer-tainty ([]Xiao\n[3] [4] [5] [6] [7]\nOverfull \\hbox (6.39282pt too wide) in paragraph at lines 434--437\n []\\T1/ptm/b/n/10.95 Oracle head-room ex-pan-sion.[] \\T1/ptm/m/n/10.95 Rank=8's\n or-a-cle F1 (0.812) is 3.7pp \\T1/ptm/m/it/10.95 higher \\T1/ptm/m/n/10.95 than \nrank=16's or-a-cle (0.776),\n[8] [9] [10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11] [12] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 188717 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a9898add-b5df-4401-8ba7-c817b528522d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "8090ae43-7c1f-4c1b-9f28-08c5b06c7f80",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260516T092241",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Assistant

_source line 30 · 2026-05-16T10:05:12.614Z_

<details><summary>Logged reasoning block</summary>

```text
The compilation had a "Label(s) may have changed" warning on the second pass. Let me run a third pass to resolve all cross-references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8090ae43-7c1f-4c1b-9f28-08c5b06c7f80",
  "isSidechain": false,
  "requestId": "req_011Cb64QHwUW8kbX8yqgtjQJ",
  "type": "assistant",
  "uuid": "67157734-831e-4477-b9e5-060fb356ab85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS8rFnV7igXgqexZNZgVbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7440,
      "cache_read_input_tokens": 76036,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 76036,
          "cache_creation_input_tokens": 7440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7440
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

_source line 31 · 2026-05-16T10:05:13.086Z_

Cross-references need one more pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67157734-831e-4477-b9e5-060fb356ab85",
  "isSidechain": false,
  "requestId": "req_011Cb64QHwUW8kbX8yqgtjQJ",
  "type": "assistant",
  "uuid": "86a0c47e-9c35-4196-8b34-2063c7b5ef65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS8rFnV7igXgqexZNZgVbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7440,
      "cache_read_input_tokens": 76036,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 76036,
          "cache_creation_input_tokens": 7440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7440
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

_source line 32 · 2026-05-16T10:05:15.299Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01999RcPmPudsQTrV8u263PE`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Third LaTeX pass to resolve cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a0c47e-9c35-4196-8b34-2063c7b5ef65",
  "isSidechain": false,
  "requestId": "req_011Cb64QHwUW8kbX8yqgtjQJ",
  "type": "assistant",
  "uuid": "ffd9d261-5ce7-42a4-b5e5-43bdf656842b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BS8rFnV7igXgqexZNZgVbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7440,
      "cache_read_input_tokens": 76036,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7440,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 76036,
          "cache_creation_input_tokens": 7440,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7440
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

_source line 33 · 2026-05-16T10:05:16.743Z_

<details><summary>↩ Tool result · `toolu_01999RcPmPudsQTrV8u263PE`</summary>

```text
[8] [9] [10]

LaTeX Warning: `h' float specifier changed to `ht'.

[11] [12] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/
times/utmri8a.pfb>
Output written on paper.pdf (12 pages, 188717 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffd9d261-5ce7-42a4-b5e5-43bdf656842b",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "a6d55045-e92b-4b59-8062-106e9d04511b",
  "toolUseResult": {
    "stdout": "[8] [9] [10]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[11] [12] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm\n/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/f\nonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/\ntimes/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 188717 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ffd9d261-5ce7-42a4-b5e5-43bdf656842b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-16T10:05:16.752Z_

```json
{
  "parentUuid": "a6d55045-e92b-4b59-8062-106e9d04511b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2c084ed1-ff8b-4b4a-9850-7598581bff0d",
  "timestamp": "2026-05-16T10:05:16.752Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 35 · 2026-05-16T10:05:22.979Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RKi5aB7H4aQqonHRi2LZZQ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c084ed1-ff8b-4b4a-9850-7598581bff0d",
  "isSidechain": false,
  "requestId": "req_011Cb64QqT42jPBCaxRv5K12",
  "type": "assistant",
  "uuid": "ee3f354c-0a36-4eaf-add0-085fddb491d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AXpq9crimM8MTa9JSQCjM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 83476,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 83476,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
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

_source line 36 · 2026-05-16T10:05:23.224Z_

<details><summary>↩ Tool result · `toolu_01RKi5aB7H4aQqonHRi2LZZQ`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 188717 May 16 10:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee3f354c-0a36-4eaf-add0-085fddb491d1",
  "isSidechain": false,
  "promptId": "fdaff240-463f-44c1-a9f1-7d9978d2717d",
  "type": "user",
  "uuid": "6f76b9bb-f078-4653-93ba-0e1abc592c18",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 188717 May 16 10:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ee3f354c-0a36-4eaf-add0-085fddb491d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T10:05:35.077Z_

论文已完成，12 页 PDF 已生成。

覆盖全部 6 个实验：
- **exp-020** (Few-NERD smoke test) → Appendix D
- **exp-021** (Few-NERD full) → Section 5.2 (selection succeeds), Table 5 in appendix, convergence analysis tables
- **exp-022** (SciERC 3rd seed) → Section 7.1 cross-seed stability table, Fisher p-values in appendix
- **exp-023** (LoRA rank=8 ablation) → Section 6.4 causal evidence, dedicated ablation table
- **exp-017** (LLaMA CoNLL) → Section 7.2 cross-model validation
- **exp-024** (claim audit) → 贯穿全文的 conditional framing + Section 8 prescriptive guidelines

核心叙事按 narrative guidance 重构：从 "universal failure + capability trap" 转为 "conditional effectiveness"——selection fails under high-convergence regimes, succeeds when output diversity is preserved。标题改为 "When Does Multi-Sample Selection Help Structured IE?"。包含 7 个正文表 + 3 个附录表，所有数字来自 experiment_data.json 和 paper_framing.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f76b9bb-f078-4653-93ba-0e1abc592c18",
  "isSidechain": false,
  "requestId": "req_011Cb64RKDeWtbKfLNYKXPf8",
  "type": "assistant",
  "uuid": "251292bb-2425-4492-b348-45cdd7a8f9a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuFW7eLu6ngFCNAQyCVAQc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 84293,
      "output_tokens": 332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 211,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 332,
          "cache_read_input_tokens": 84293,
          "cache_creation_input_tokens": 211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 211
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T092241 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consi…",
  "leafUuid": "251292bb-2425-4492-b348-45cdd7a8f9a1",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream_20260516T092241",
  "sessionId": "7bb2de8f-cf6e-4e67-a46f-5ec31f965d8e"
}
```

---
