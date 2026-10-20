# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/dc8fbc02-a351-42eb-9162-8abd7e156f3e.jsonl`
- **Structured JSON:** [`ec03c9792bf88f97f22b.json`](../../sessions/ec/ec03c9792bf88f97f22b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T02:37:18.139Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T02:37:18.139Z",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Compounding 发现被承认为有价值的实证贡献，但 RateQuant Appendix M 已 acknowledge 该现象导致 novelty 打折。 Reviewer 要求去掉 'universal' 改为 'consistent pattern across 8 architectures'，constraint 被部分 reviewer  视为 'obvious hyperparameter tuning' 而非 principled contribution，需要更强的理论 justification。 1/8 downstream benefit 被至少 1 位 reviewer 视为 'this only works on Qwen'。Diagnostic n=9 只能作为  observation，不能作为独立 claim。论文需要 reframe 为 empirical analysis paper，前置 analysis contribution。 预估 narrative rewrite 30-40%，主要集中在 intro、claim 措辞、和 related work 对 RateQuant 的讨论。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T02:37:18.143Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T02:37:18.143Z",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-16T02:37:18.161Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Compounding 发现被承认为有价值的实证贡献，但 RateQuant Appendix M 已 acknowledge 该现象导致 novelty 打折。 Reviewer 要求去掉 'universal' 改为 'consistent pattern across 8 architectures'，constraint 被部分 reviewer  视为 'obvious hyperparameter tuning' 而非 principled contribution，需要更强的理论 justification。 1/8 downstream benefit 被至少 1 位 reviewer 视为 'this only works on Qwen'。Diagnostic n=9 只能作为  observation，不能作为独立 claim。论文需要 reframe 为 empirical analysis paper，前置 analysis contribution。 预估 narrative rewrite 30-40%，主要集中在 intro、claim 措辞、和 related work 对 RateQuant 的讨论。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "50ff395e-a366-43b3-bad5-48c30750cb5c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T02:37:18.161Z_

```json
{
  "parentUuid": "50ff395e-a366-43b3-bad5-48c30750cb5c",
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
  "uuid": "f95281d5-8d7a-42d2-a9b8-b22692be43d1",
  "timestamp": "2026-05-16T02:37:18.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T02:37:18.161Z_

```json
{
  "parentUuid": "f95281d5-8d7a-42d2-a9b8-b22692be43d1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a4b94d73-50fb-47ff-9d87-083803c9c0f4",
  "timestamp": "2026-05-16T02:37:18.161Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Assistant

_source line 7 · 2026-05-16T02:37:20.805Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b94d73-50fb-47ff-9d87-083803c9c0f4",
  "isSidechain": false,
  "requestId": "req_011Cb5UFWVpWJ4TE1Eqq6V17",
  "type": "assistant",
  "uuid": "ef6e427c-7345-42a0-87e6-f4113a4b4074",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2PiSu7FW3s3nVnnXVfjZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12320,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12320
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

_source line 8 · 2026-05-16T02:37:21.889Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VKbcp78P53YM1shk5Xkd7o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6e427c-7345-42a0-87e6-f4113a4b4074",
  "isSidechain": false,
  "requestId": "req_011Cb5UFWVpWJ4TE1Eqq6V17",
  "type": "assistant",
  "uuid": "6e5aa048-f8e7-4910-aa04-eb5527a54116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2PiSu7FW3s3nVnnXVfjZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12320,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12320
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

_source line 9 · 2026-05-16T02:37:22.047Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HLq16YamsYpowTZ5FjasR3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e5aa048-f8e7-4910-aa04-eb5527a54116",
  "isSidechain": false,
  "requestId": "req_011Cb5UFWVpWJ4TE1Eqq6V17",
  "type": "assistant",
  "uuid": "b3592ee1-9e36-448f-906e-8ff708a0bd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2PiSu7FW3s3nVnnXVfjZ1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12320,
      "cache_read_input_tokens": 11841,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12320
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

_source line 10 · 2026-05-16T02:37:22.152Z_

<details><summary>↩ Tool result · `toolu_01VKbcp78P53YM1shk5Xkd7o`</summary>

```text
1	[
2	  {
3	    "name": "L0 Exclusion Removal Ablation",
4	    "description": "移除 L0 排除约束，仅保留 max_2bit=8，验证 solver 纯粹从 profiling data 自动发现 L0 敏感结构。\n",
5	    "results": {
6	      "solver_auto_assigns_8bit_to_L0": true,
7	      "ppl_without_l0_exclusion": 10.91,
8	      "ppl_with_l0_exclusion": 10.91,
9	      "delta": 0.0,
10	      "l0_heads_assigned_8bit": 4,
11	      "bit_distribution": "{2:8, 4:100, 8:4}"
12	    },
13	    "tables": [
14	      {
15	        "caption": "Table: L0 Exclusion Ablation (Qwen2.5-7B, budget=0.25)",
16	        "rows": [
17	          {
18	            "condition": "MCKP + L0 exclusion + max_2bit=8",
19	            "ppl": 10.91,
20	            "l0_bit": "8-bit (hard-coded)",
21	            "note": "原始设置"
22	          },
23	          {
24	            "condition": "MCKP + max_2bit=8 only",
25	            "ppl": 10.91,
26	            "l0_bit": "8-bit (solver-discovered)",
27	            "note": "solver 自动分配"
28	          }
29	        ]
30	      }
31	    ],
32	    "figures": [],
33	    "analysis": "Reviewer 评价：supportive but minor。在 median 档中被视为 completeness ablation  而非核心证据。reviewer 可能建议移到 appendix。不影响主要 claim 但增加 paper 完整性。\n\n\nMedian 档下该结果被 reviewer 认可为 neat ablation——solver 自动发现 L0 是最敏感的层， 不需要手动排除。但 reviewer 会指出这只在 Qwen 上验证（L0 dominance ratio=26×）， 对于 L0 dominance 低的架构（Yi 0.07，Mistral 1.74）solver 是否同样能自动发现正确结构 缺少验证。一位 reviewer 可能注释 \"this is expected — L0 has the largest profiling delta  by far, so any reasonable solver would protect it.\" 不会成为主要 objection，但也不会 被视为独立贡献。\n"
34	  },
35	  {
36	    "name": "Llama-3.1-8B Full Pipeline Replication",
37	    "description": "在 Llama-3.1-8B（GQA 4:1）上复制完整 pipeline——profiling、constrained MCKP、PPL 评估。 测试跨架构泛化性。\n",
38	    "results": {
39	      "baseline_ppl_bf16": 8.09,
40	      "uniform_4bit_ppl": 8.47,
41	      "mckp_constrained_ppl": 8.45,
42	      "delta_vs_uniform_pct": 0.2,
43	      "delta_vs_uniform_ppl": 0.02,
44	      "memory_ratio": 0.25,
45	      "bit_distribution": "{2:2, 4:253, 8:1}",
46	      "natural_2bit_count": 2,
47	      "constraint_binds": false,
48	      "unconstrained_degradation_ratio": 1.07,
49	      "top5_concentration": 0.57,
50	      "distribution_shape": "Spike"
51	    },
52	    "tables": [
53	      {
54	        "caption": "Table: Llama-3.1-8B Pipeline Results (budget=0.25)",
55	        "rows": [
56	          {
57	            "method": "BF16 baseline",
58	            "ppl": 8.09,
59	            "bits": "16",
60	            "note": ""
61	          },
62	          {
63	            "method": "Uniform 4-bit",
64	            "ppl": 8.47,
65	            "bits": "4.0",
66	            "note": ""
67	          },
68	          {
69	            "method": "Unconstrained MCKP",
70	            "ppl": 8.63,
71	            "bits": "mixed",
72	            "note": "1.07× baseline"
73	          },
74	          {
75	            "method": "Constrained MCKP (k=8)",
76	            "ppl": 8.45,
77	            "bits": "{2:2, 4:253, 8:1}",
78	            "note": "+0.2% vs uniform"
79	          }
80	        ]
81	      }
82	    ],
83	    "figures": [],
84	    "analysis": "Median reviewer 会同时肯定和批评：肯定 honest reporting of negative result， 批评 \"if 7/8 architectures show no benefit, this is not a method paper — it's an  analysis paper that happens to find one architecture where optimization helps.\"  这强化了 reframe 为 empirical analysis 的需要。\n\n\nMedian 档下，Llama 的 marginal 结果（+0.2% vs uniform）成为 reviewer 攻击点之一。 reviewer 会写 \"the method provides essentially no benefit on Llama — the +0.2%  improvement is within noise.\" Llama 的 spike distribution（L2H5 单个 outlier 主导， t₁/t₅≈0.85）导致 solver 只选择 2 个 head 做 2-bit，constraint 从不触发（natural k=2 < max_2bit=8）， MCKP 优化空间极小。这解释了为什么 PPL 差异几乎为零。但从 compounding 角度， unconstrained 仍然 1.07× baseline，说明即使 mild 情况下 solver 仍会略微 over-allocate。 Reviewer 会要求诚实报告 \"no benefit\" 而非 spin 为 positive。在 median 档中， 这个 negative result 本身不被反对——reviewer 反对的是用 8 个架构中只有 1 个 positive  来声称 method 有效。\n"
85	  },
86	  {
87	    "name": "Mistral-7B-v0.3 Full Pipeline Replication",
88	    "description": "在 Mistral-7B-v0.3 上复制完整 pipeline。不同架构家族，建立跨架构有效性。\n",
89	    "results": {
90	      "baseline_ppl_bf16": 7.035,
91	      "uniform_4bit_ppl": 7.131,
92	      "mckp_constrained_ppl": 7.165,
93	      "delta_vs_uniform_pct": -0.5,
94	      "delta_vs_uniform_ppl": -0.034,
95	      "memory_ratio": 0.25,
96	      "bit_distribution": "{2:4, 4:252}",
97	      "unconstrained_degradation_ratio": 1.08,
98	      "top5_concentration": 0.22,
99	      "distribution_shape": "Flat",
100	      "k_ablation_monotonic": true,
101	      "best_k_still_worse_than_uniform": true
102	    },
103	    "tables": [
104	      {
105	        "caption": "Table: Mistral-7B-v0.3 k-Ablation (budget=0.25)",
106	        "rows": [
107	          {
108	            "k": 4,
109	            "ppl": 7.165,
110	            "n_2bit": 4,
111	            "note": "best constrained, still > uniform"
112	          },
113	          {
114	            "k": 8,
115	            "ppl": 7.2,
116	            "n_2bit": 8,
117	            "note": ""
118	          },
119	          {
120	            "k": 16,
121	            "ppl": 7.311,
122	            "n_2bit": 16,
123	            "note": ""
124	          },
125	          {
126	            "k": "uniform",
127	            "ppl": 7.131,
128	            "n_2bit": 0,
129	            "note": "optimal for Mistral"
130	          }
131	        ]
132	      }
133	    ],
134	    "figures": [],
135	    "analysis": "在 median 档中，Mistral negative result 既是弱点也是优势。弱点：method 不 work。 优势：honest negative result 增加 credibility，且支持 diagnostic 的必要性—— 如果没有 diagnostic，practitioners 会浪费 profiling 时间在 Mistral 这样的模型上。 Reviewer 2 (偏方法) 会将此作为 \"method only works on Qwen\" 的证据。 Reviewer 3 (偏分析) 会认可这增加了 paper 的科学价值。\n\n\nMistral 是最强 negative case：MCKP 在所有 k 值下都 worse than uniform。 PPL 随 k 单调递增（k=4: 7.165, k=8: 7.200, k=18: 7.323），profiler 报告近零  sensitivity 差异（concentration=0.22, CV=1.31）。这表明 Mistral 的 KV head  sensitivity 高度均匀——没有 head 从 2-bit downgrade 中获益。Median reviewer  会将此视为 \"method failure on flat architectures\" 和 \"proof that uniform 4-bit  is optimal when profiler gives zero signal.\" 对 compounding claim 仍有帮助： unconstrained 1.08× 表明即使 flat distribution，solver 仍 over-allocate  2-bit heads（42/256=16.4%）。但 reviewer 会质疑 \"1.08× is hardly catastrophic  — this is within the range where a practitioner wouldn't even notice.\"\n"
136	  },
137	  {
138	    "name": "Compounding Effect Characterization Sweep",
139	    "description": "在 Qwen2.5-7B 上扫 max_2bit 从 0 到 112，绘制 PPL vs max_2bit 曲线， 确定 compounding 阈值。建立 cardinality constraint 的 principled 基础。\n",
140	    "results": {
141	      "k0_ppl": 9.81,
142	      "k8_ppl": 10.05,
143	      "k16_ppl": 10.42,
144	      "k32_ppl": 11.6,
145	      "k64_ppl": 23.22,
146	      "k112_ppl": 98.75,
147	      "compounding_threshold_k": 16,
148	      "max_compounding_ratio": 10.07,
149	      "curve_shape": "superlinear after k≈16, exponential after k≈48",
150	      "safe_k_range": "k≤8 universally <2.5% degradation"
151	    },
152	    "tables": [
153	      {
154	        "caption": "Table: Compounding Sweep (Qwen2.5-7B, budget=0.25)",
155	        "rows": [
156	          {
157	            "k": 0,
158	            "ppl": 9.81,
159	            "ratio_to_baseline": "1.00×"
160	          },
161	          {
162	            "k": 8,
163	            "ppl": 10.05,
164	            "ratio_to_baseline": "1.02×"
165	          },
166	          {
167	            "k": 16,
168	            "ppl": 10.42,
169	            "ratio_to_baseline": "1.06×"
170	          },
171	          {
172	            "k": 32,
173	            "ppl": 11.6,
174	            "ratio_to_baseline": "1.18×"
175	          },
176	          {
177	            "k": 64,
178	            "ppl": 23.22,
179	            "ratio_to_baseline": "2.37×"
180	          },
181	          {
182	            "k": 112,
183	            "ppl": 98.75,
184	            "ratio_to_baseline": "10.07×"
185	          }
186	        ]
187	      }
188	    ],
189	    "figures": [],
190	    "analysis": "Median reviewer 的核心反馈：compounding effect 是 real and well-characterized， 但 novelty 因 RateQuant Appendix M 打折。建议在 related work 中显式讨论  \"RateQuant acknowledges compounding in Appendix M but does not characterize the  threshold or provide a fix — our sweep provides the first quantitative mapping.\"  三架构对比增加说服力：Qwen 的 U-shape（optimal k=8）、Llama 的 flat profile （natural k=2, constraint irrelevant）、Mistral 的 monotonic increase（every  2-bit head hurts）展示了 architecture-dependent compounding behavior。\n\n\nCompounding sweep 是 median 档中最被认可的实验——提供了 compounding 效应的 定量证据。PPL 在 k≤8 时近线性增长（9.81→10.05, +2.4%），k=16-32 开始加速 （10.42→11.60），k≥48 后指数爆炸（23.22→98.75）。这条曲线是 \"principled  basis for constraint selection\" 的核心证据。但 median reviewer 会有两个质疑： (1) \"这条曲线只在 Qwen 上做了——其他架构的阈值可能完全不同\"（A2）， (2) \"RateQuant Appendix M 已经 acknowledge compounding，这个 sweep 只是 quantified 了已知现象\"（A1）。需要补充 Llama 和 Mistral 的 compounding sweep  来部分 address (1)——实际已有数据（llama_compounding_sweep, mistral_compounding_sweep_v2） 可以回应。Reviewer 对 k≤8 safety 的 claim 会接受，但会要求去掉 \"universally safe\"  改为 \"safe across all tested architectures.\"\n"
191	  },
192	  {
193	    "name": "Budget Sweep (2×/4×/8× Compression)",
194	    "description": "在 Qwen2.5-7B 上测试 2×/4×/8× 压缩比下的 constrained MCKP vs uniform baseline。\n",
195	    "results": {
196	      "budget_0.5_mckp_ppl": 9.85,
197	      "budget_0.5_uniform_ppl": 9.86,
198	      "budget_0.5_delta_pct": 0.1,
199	      "budget_0.25_mckp_ppl": 10.91,
200	      "budget_0.25_uniform_ppl": 15.45,
201	      "budget_0.25_delta_pct": 29.4,
202	      "budget_0.125_mckp_ppl": 57.6,
203	      "budget_0.125_uniform_2bit_ppl": 2643.77,
204	      "budget_0.125_delta_ratio": "45.9×",
205	      "compression_amplifies_benefit": true
206	    },
207	    "tables": [
208	      {
209	        "caption": "Table: Budget Sweep (Qwen2.5-7B)",
210	        "rows": [
211	          {
212	            "compression": "2× (budget=0.5)",
213	            "mckp_ppl": 9.85,
214	            "uniform_ppl": 9.86,
215	            "delta": "~0%"
216	          },
217	          {
218	            "compression": "4× (budget=0.25)",
219	            "mckp_ppl": 10.91,
220	            "uniform_ppl": 15.45,
221	            "delta": "29.4%"
222	          },
223	          {
224	            "compression": "8× (budget=0.125)",
225	            "mckp_ppl": 57.6,
226	            "uniform_ppl": 2643.77,
227	            "delta": "45.9×"
228	          }
229	        ]
230	      }
231	    ],
232	    "figures": [],
233	    "analysis": "Median 档中被部分接受。Reviewer 认可 practical implication（高压缩比下 constraint  essential），但质疑 moderate compression（主要应用场景）下只有 Qwen 获益的泛化性。 建议补充 Llama/Mistral 的 budget sweep 至少在 8× 压缩点。\n\n\nBudget sweep 展示了核心趋势：压缩越激进，constrained MCKP vs uniform 的差距越大。 在 2× 压缩下差异几乎为零（都接近 baseline），4× 时 MCKP 优势 29.4%，8× 时 MCKP 57.60 vs uniform 2643.77（45×差距）。Median reviewer 会认可 aggressive  compression 的 practical value（\"at 8× compression, the constraint is the difference  between usable and unusable\"），但会指出：(a) 2× 结果说明 moderate compression 下 benefit 主要来自 Qwen 的 spread pattern 而非 method 本身，(b) 8× 的 PPL=57.60  虽远好于 2643.77，但 absolute 值仍然很高——\"is a 57.60 PPL model actually usable?\"  需要补充 aggressive compression 下的 downstream task 评估。(c) 只在 Qwen 上做了 full sweep，Llama 的 aggressive compression 数据（57.60 vs 2643.77）虽有但 仅一个点，不是 sweep。\n"
234	  },
235	  {
236	    "name": "High-Resolution Profiling",
237	    "description": "64 seq × 2048 tokens 的高分辨率 profiling（vs 16×512），验证更好的 profiling  是否改善 solver allocation。\n",
238	    "results": {
239	      "hires_constrained_ppl_bf16": 10.91,
240	      "lowres_constrained_ppl_bf16": 11.23,
241	      "baseline_ppl_bf16": 9.81,
242	      "improvement_vs_lowres": 0.32,
243	      "improvement_pct": 2.8,
244	      "hires_nonzero_2bit_heads": 100,
245	      "lowres_nonzero_2bit_heads": 37,
246	      "allocation_diff_count": 8,
247	      "profiling_time_min": 65.5,
248	      "bit_distribution": "{2:8, 4:100, 8:4}"
249	    },
250	    "tables": [
251	      {
252	        "caption": "Table: Profiling Resolution Impact (Qwen2.5-7B, k=8)",
253	        "rows": [
254	          {
255	            "resolution": "Low-res (16×512)",
256	            "ppl": 11.23,
257	            "nonzero_heads": 37,
258	            "time_min": "~10"
259	          },
260	          {
261	            "resolution": "High-res (64×2048)",
262	            "ppl": 10.91,
263	            "nonzero_heads": 100,
264	            "time_min": 65.5
265	          },
266	          {
267	            "resolution": "Uniform 4-bit",
268	            "ppl": 15.45,
269	            "nonzero_heads": "N/A",
270	            "time_min": 0
271	          }
272	        ]
273	      }
274	    ],
275	    "figures": [],
276	    "analysis": "Median 档中作为 engineering insight 被接受。Reviewer 不会 object 但建议 放 appendix 而非 main body。对 claim 的影响中性——既不强化也不削弱核心论点。\n\n\n高分辨率 profiling 将 PPL 从 11.23 降到 10.91（-2.8%），说明 profiling resolution  matters。核心改进来自更准确的 sensitivity ranking：hires 发现 100/112 heads 有 非零 2-bit delta（vs lowres 37/112），导致 8 个 head 的 allocation 改变。 Median reviewer 反应分化：(a) 方法 reviewer 认为这说明 \"profiling quality drives  results more than solver choice — the real engineering is in the profiler, not MCKP\"， 进一步削弱 solver 作为贡献的地位；(b) 系统 reviewer 注意到 65.5 min profiling time  并质疑 \"practitioners won't spend an hour profiling a 7B model to save 0.32 PPL\"。 需要在 paper 中 trade-off profiling cost vs quality，并论证 lowres 已足够好 （11.23 vs uniform 15.45, 仍有 27.3% improvement）。\n"
277	  },
278	  {
279	    "name": "C4 Cross-Dataset Evaluation",
280	    "description": "在 C4 上评估 Qwen2.5-7B（calibrate on WikiText-2, eval on C4; calibrate on C4, eval on WikiText-2）， 验证结果不是 WikiText-2 specific。\n",
281	    "results": {
282	      "c4_cal_wt2_eval_mckp_ppl": 11.29,
283	      "c4_cal_wt2_eval_uniform_ppl": 15.45,
284	      "c4_cal_wt2_eval_delta": 4.15,
285	      "allocation_agreement_c4_vs_wt2": 0.964,
286	      "agreement_heads": "108/112",
287	      "cross_domain_wt2_to_c4_mckp_ppl": 20.56,
288	      "cross_domain_wt2_to_c4_uniform_ppl": 35.42,
289	      "contamination_impact": 0.034
290	    },
291	    "tables": [
292	      {
293	        "caption": "Table: Cross-Dataset Calibration Agreement",
294	        "rows": [
295	          {
296	            "model": "Qwen2.5-7B",
297	            "agreement": "108/112 (96.4%)",
298	            "same_domain_ppl": 11.29,
299	            "cross_domain_ppl": 20.56
300	          },
301	          {
302	            "model": "Llama-3.1-8B",
303	            "agreement": "250/256 (97.7%)",
304	            "same_domain_ppl": 8.45,
305	            "cross_domain_ppl": 8.65
306	          },
307	          {
308	            "model": "Mistral-7B-v0.3",
309	            "agreement": "247/256 (96.5%)",
310	            "same_domain_ppl": 7.16,
311	            "cross_domain_ppl": 7.19
312	          }
313	        ]
314	      }
315	    ],
316	    "figures": [],
317	    "analysis": "三架构的 >96% agreement 是 strong evidence for calibration robustness。 Median reviewer 视为 useful supplementary experiment，不会 object。 建议放 Section 4 或 appendix。\n\n\n96.4% allocation agreement 跨 calibration source 是 positive signal：profiling  的 head sensitivity ranking 对 calibration data 不敏感。Median reviewer 会认可  cross-dataset robustness 但指出：(a) 只在 Qwen 上验证（\"is this agreement rate  architecture-dependent?\"），(b) 4/112 disagreement heads 的 identity 和影响未讨论， (c) cross-domain PPL（WiKi→C4: 20.56 vs uniform 35.42）虽然 MCKP 仍胜出， 但绝对 PPL 远高于 same-domain（11.29），说明 calibration domain mismatch 仍有成本。 Reviewer 会建议 \"report agreement rate on at least one more architecture\" 作为 minor revision。已有 llama_c4_cross_dataset（97.7% agreement）和  mistral_c4_cross_dataset（96.5%）数据可以回应。\n"
318	  },
319	  {
320	    "name": "RateQuant Greedy Comparison",
321	    "description": "实现 RateQuant 的 greedy Algorithm 1 在 {2,4,8,16} 上，展示 greedy 在 non-consecutive 集合上 suboptimal。\n",
322	    "results": {
323	      "ratequant_greedy_unconstrained_ppl": 32.45,
324	      "mckp_unconstrained_ppl": 36.92,
325	      "uniform_4bit_ppl": 15.45,
326	      "greedy_bit_distribution": "{2:68, 4:30, 8:4, 16:10}",
327	      "both_worse_than_uniform": true,
328	      "greedy_better_than_mckp_unconstrained": true
329	    },
330	    "tables": [
331	      {
332	        "caption": "Table: Unconstrained Solver Comparison (Qwen2.5-7B)",
333	        "rows": [
334	          {
335	            "solver": "RateQuant Greedy (unconstrained)",
336	            "ppl": 32.45,
337	            "n_2bit": 68,
338	            "status": "FAIL"
339	          },
340	          {
341	            "solver": "MCKP (unconstrained)",
342	            "ppl": 36.92,
343	            "n_2bit": "≥68",
344	            "status": "FAIL"
345	          },
346	          {
347	            "solver": "Uniform 4-bit",
348	            "ppl": 15.45,
349	            "n_2bit": 0,
350	            "status": "baseline"
351	          }
352	        ]
353	      }
354	    ],
355	    "figures": [],
356	    "analysis": "Median 档中该实验的价值被 reinterpret：不再是 \"MCKP beats greedy\"  而是 \"both fail without constraint, both succeed with constraint.\"  这是 solver equivalence 叙事的第一半证据。Reviewer 认可这个 framing shift。\n\n\n关键发现：两个 solver 在 unconstrained 设置下都 worse than uniform，但 greedy  (32.45) 反而比 MCKP (36.92) 好！这颠覆了 \"MCKP is better optimizer\" 的叙事。 Median reviewer 会抓住这个点：\"if greedy outperforms MCKP unconstrained,  why do you need MCKP at all?\" 回应：unconstrained 时两者都失败（compounding）， 差异无意义；constrained 时两者完全一致（Δ=0.0000）——plan_016 的 solver equivalence  证据。但这确实削弱了 MCKP 作为 solver contribution 的叙事，支持 reframe： \"constraint is the contribution, not the solver.\" 一位 reviewer 会标注  \"the unconstrained MCKP being worse than greedy suggests the ILP formulation  interacts poorly with compounding — discuss this.\" 需要在 paper 中解释为什么 MCKP 更容易 over-allocate 2-bit（因为它更 aggressively optimizes per-head  cost-benefit，导致更多 2-bit assignments）。\n"
357	  },
358	  {
359	    "name": "Oracle Comparison (Subset Brute-Force)",
360	    "description": "在 Qwen2.5-7B 的 3-4 个 layer group 上做 brute-force optimal allocation， 量化 MCKP gap to oracle。\n",
361	    "results": {
362	      "mckp_ppl": 10.91,
363	      "max_oracle_gap_ppl": 0.018,
364	      "avg_oracle_gap_ppl": 0.005,
365	      "layers_mckp_optimal": "5/8",
366	      "layers_with_gap": 3,
367	      "gap_nature": "2-bit head position swap within same bit budget",
368	      "total_evals": 54
369	    },
370	    "tables": [
371	      {
372	        "caption": "Table: MCKP vs Oracle Gap (Qwen2.5-7B, per layer group)",
373	        "rows": [
374	          {
375	            "layer_group": "L0-L3",
376	            "mckp_optimal": true,
377	            "gap_ppl": 0.0
378	          },
379	          {
380	            "layer_group": "L4-L7",
381	            "mckp_optimal": false,
382	            "gap_ppl": 0.0045
383	          },
384	          {
385	            "layer_group": "L8-L11",
386	            "mckp_optimal": false,
387	            "gap_ppl": 0.0136
388	          },
389	          {
390	            "layer_group": "L12-L15",
391	            "mckp_optimal": true,
392	            "gap_ppl": 0.0
393	          }
394	        ]
395	      }
396	    ],
397	    "figures": [],
398	    "analysis": "Near-zero oracle gap 与 solver equivalence 共同构成 \"constraint is what matters\"  的完整论证。Median reviewer 视为 thorough analysis, 建议作为 Section 4 的 supporting evidence。\n\n\nMCKP 与 oracle 的 gap 极小（max 0.018 PPL, avg 0.005 PPL），5/8 layer groups  完全 optimal，3 个 gap 来自同 budget 下 2-bit head 位置互换。Median reviewer  会认可 \"MCKP is near-optimal within the constrained feasible set\" 但立刻指出： \"combined with plan_016 showing greedy=MCKP, this means the constraint defines  the quality — any solver that respects the constraint is near-optimal. The MCKP  formulation adds no value.\" 这进一步支持 constraint-as-contribution framing， 但同时使 MCKP 作为 method 贡献更不站得住。reviewer 建议 \"present MCKP as the  analysis framework, not the algorithmic contribution.\" 在 median 档中这个实验 反而帮助了 reframe——它是 \"solver doesn't matter\" 叙事的 complementary evidence。\n"
399	  },
400	  {
401	    "name": "Cross-Domain Calibration Robustness",
402	    "description": "C4 calibration → WikiText-2 eval 和反方向，报告 per-head allocation agreement rate。\n",
403	    "results": {
404	      "allocation_agreement_c4_vs_wt2": 0.964,
405	      "agreement_heads": "108/112",
406	      "c4_cal_wt2_eval_mckp_ppl": 11.29,
407	      "cross_domain_gap_vs_same_domain": 0.06
408	    },
409	    "tables": [],
410	    "figures": [],
411	    "analysis": "Minor positive signal。在 median 档中作为 robustness check 被接受， 不影响 overall score。\n\n\n与 plan_007 共享数据。96.4% agreement 说明 profiling-based sensitivity ranking  对 calibration source 高度鲁棒。Median reviewer 反应温和 positive——这是 expected behavior（\"if head sensitivity is an architectural property, it shouldn't  depend on calibration data\"），所以不会 strongly impress but also won't object。 主要 reviewer concern 是 Qwen-only，但已有三架构数据（Qwen 96.4%, Llama 97.7%,  Mistral 96.5%）可补充。\n"
412	  },
413	  {
414	    "name": "Head Sensitivity Visualization",
415	    "description": "生成 per-head profiling delta heatmap、compounding curve、budget allocation 对比图。\n",
416	    "results": {
417	      "figures_generated": 3,
418	      "heatmap_shows_l0_dominance": true,
419	      "compounding_curve_elbow": "k≈16",
420	      "allocation_comparison_shows_constraint_effect": true
421	    },
422	    "tables": [],
423	    "figures": [],
424	    "analysis": "Presentation-level contribution。Median reviewer 可能 suggest 改进但不会 因为 visualization 加分或扣分。\n\n\n可视化是 presentation quality 问题而非科学证据。Median reviewer 会在 minor comments 中评价：\"Figure X clearly shows the L0 dominance pattern\"  或 \"the compounding curve would benefit from error bars.\" 不影响 score 但 好的可视化可以帮助 reviewer 快速理解 compounding 现象。关键是 heatmap 要 展示 Qwen（spread, L0 cluster 明显）vs Yi（spike, 单个 L4H3 突出）vs  Gemma-2（flat, 无显著差异）的对比——如果只展示 Qwen，reviewer 会说  \"cherry-picked visualization.\"\n"
425	  },
426	  {
427	    "name": "K/V Separation",
428	    "description": "K 和 V heads 作为独立 MCKP items，独立 budget allocation。与 joint K=V 方法对比。\n",
429	    "results": {
430	      "kv_sep_ppl": 11.22,
431	      "joint_kv_ppl": 10.91,
432	      "uniform_4bit_ppl": 15.45,
433	      "delta_sep_vs_joint": 0.31,
434	      "sep_k_2bit_count": 16,
435	      "sep_v_uniform_4bit": true,
436	      "kv_asymmetric_heads": 21
437	    },
438	    "tables": [
439	      {
440	        "caption": "Table: K/V Separation vs Joint (Qwen2.5-7B, k=8)",
441	        "rows": [
442	          {
443	            "method": "Joint K=V (k=8)",
444	            "ppl": 10.91,
445	            "k_2bit": 8,
446	            "v_2bit": 0
447	          },
448	          {
449	            "method": "K/V Separation",
450	            "ppl": 11.22,
451	            "k_2bit": 16,
452	            "v_2bit": 0
453	          },
454	          {
455	            "method": "Uniform 4-bit",
456	            "ppl": 15.45,
457	            "k_2bit": 0,
458	            "v_2bit": 0
459	          }
460	        ]
461	      }
462	    ],
463	    "figures": [],
464	    "analysis": "Negative result 但 informative。在 median 档中被视为 thorough ablation， 可放 appendix。不影响核心 claim。\n\n\nK/V separation 反而 worse（11.22 vs 10.91, +0.31 PPL）。separation 给 K heads  分配了 16 个 2-bit（超过 max_2bit=8 的 joint 约束），导致 K cache compounding。 V heads 在 separation 下全部 4-bit（optimal for V），但 K cache 的退化超过了 V 的收益。Median reviewer 会认为这是 negative result 但有 insight value： \"K cache is more sensitive to 2-bit compounding than V — this explains why  joint K=V treatment with a single cardinality constraint works better.\"  一位 reviewer 可能 suggest \"apply per-cache-type cardinality constraint\"  as future work。不会成为 major objection。\n"
465	  },
466	  {
467	    "name": "Downstream Task Evaluation (Qwen2.5-7B)",
468	    "description": "ARC-C / HellaSwag / PIQA / WinoGrande 在 Qwen2.5-7B 4× 压缩下评估。 验证 PPL improvement 转化为 downstream performance。\n",
469	    "results": {
470	      "arc_c_uniform": 0.4812,
471	      "arc_c_mckp": 0.5137,
472	      "arc_c_delta_pp": 3.16,
473	      "hellaswag_uniform": 0.7284,
474	      "hellaswag_mckp": 0.7684,
475	      "hellaswag_delta_pp": 4.0,
476	      "piqa_uniform": 0.7661,
477	      "piqa_mckp": 0.7786,
478	      "piqa_delta_pp": 1.25,
479	      "winogrande_uniform": 0.6622,
480	      "winogrande_mckp": 0.6819,
481	      "winogrande_delta_pp": 1.97,
482	      "avg_recovery": 0.728,
483	      "bf16_avg": 0.688
484	    },
485	    "tables": [
486	      {
487	        "caption": "Table: Downstream Evaluation — Full Cross-Architecture",
488	        "rows": [
489	          {
490	            "model": "Qwen (Spread)",
491	            "avg_delta_pp": "+2.60",
492	            "arc_c_delta": "+3.16",
493	            "verdict": "Benefit"
494	          },
495	          {
496	            "model": "Yi-1.5 (Spike)",
497	            "avg_delta_pp": "-0.77",
498	            "arc_c_delta": "-3.24",
499	            "verdict": "Degradation"
500	          },
501	          {
502	            "model": "Llama (Spike)",
503	            "avg_delta_pp": "-0.99",
504	            "arc_c_delta": "-2.65",
505	            "verdict": "Degradation"
506	          },
507	          {
508	            "model": "Mistral (Flat)",
509	            "avg_delta_pp": "-0.48",
510	            "arc_c_delta": "-1.19",
511	            "verdict": "Degradation"
512	          },
513	          {
514	            "model": "Gemma-2 (Flat)",
515	            "avg_delta_pp": "+0.14",
516	            "arc_c_delta": "-0.17",
517	            "verdict": "Noise"
518	          }
519	        ]
520	      }
521	    ],
522	    "figures": [],
523	    "analysis": "Median 档中这是 double-edged evidence。Qwen 的 downstream gains 被认可但 限定为 \"architecture-specific\"。跨架构 degradation 要求论文措辞从 \"non-uniform improves downstream\" 改为 \"non-uniform allocation improves downstream  performance specifically on architectures with spread sensitivity patterns (1/5  tested); on other architectures, uniform 4-bit should be preferred.\"  arc_challenge 系统性退化需要主动讨论段落。\n\n\nQwen downstream gains 一致 positive（+1.25 to +4.00pp），与 PPL improvement  方向一致。但 median reviewer 的核心 objection 是 A4：\"this only works on Qwen.\" 跨架构 downstream 数据显示 Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp,  Gemma-2 +0.14pp（noise）。reviewer 会写：\"4/5 architectures show negative or  negligible downstream effect. The method degrades downstream performance on most  models.\" 另一个 median-specific concern 是 lack of multi-seed CI：3.16pp arc_c  delta 没有 confidence interval，\"could be within single-run variance\"（A6）。 已有 qwen_3seed_downstream_ci（arc_c std=0.0035, hellaswag std=0.0022） 可部分回应。arc_challenge 跨模型系统性退化（Yi -3.24pp, Llama -2.65pp,  Mistral -1.19pp）会被特别标注——reviewer 要求主动讨论这个 pattern。\n"
524	  },
525	  {
526	    "name": "70B Profiling-Only",
527	    "description": "在 Qwen2.5-72B 上做 distortion profiling（不做 full eval），分析 sensitivity  patterns 是否随模型大小 scale。\n",
528	    "results": {
529	      "status": "killed",
530	      "sensitivity_pattern_observed": null,
531	      "l0_dominance_scales": null
532	    },
533	    "tables": [],
534	    "figures": [],
535	    "analysis": "Missing data。Median reviewer 标注为 limitation，不作为 reject reason。\n\n\n实验被 killed（可能 OOM 或 timeout）。Median reviewer 会注意到 \"only 7B-14B  scale models tested\" 并标注为 limitation：\"no evidence that findings generalize  to production-scale models (70B+).\" 但在 median 档中这是 minor gap 而非 major  objection——大多数 KV cache quantization papers 也只测 7B-14B。缺少 70B 数据 会降低 \"practical implications\" 的说服力但不会导致 reject。建议在 limitations  中明确承认 \"our experiments are limited to 7B-14B scale; scaling behavior of  compounding effects to 70B+ models remains an open question.\"\n"
536	  },
537	  {
538	    "name": "L0-Only Heuristic Baseline",
539	    "description": "最简单的 non-uniform 策略：L0 heads 8-bit，其余 uniform 4-bit。如果 L0-only 匹配 MCKP，full optimization 不必要。\n",
540	    "results": {
541	      "qwen_mckp_ppl": 10.91,
542	      "qwen_l0_random_mean": 11.69,
543	      "qwen_l0_random_std": 0.47,
544	      "qwen_l0_random_median": 11.52,
545	      "qwen_naive_positional_ppl": 12.23,
546	      "llama_mckp_ppl": 8.45,
547	      "llama_l0_random_mean": 10.48,
548	      "llama_naive_positional": 9.94,
549	      "mistral_mckp_ppl": 7.16,
550	      "mistral_l0_random_mean": 7.56,
551	      "mistral_naive_positional": 7.48,
552	      "mckp_consistently_beats_l0_random": true
553	    },
554	    "tables": [
555	      {
556	        "caption": "Table: MCKP vs Heuristic Baselines (budget=0.25)",
557	        "rows": [
558	          {
559	            "model": "Qwen",
560	            "mckp": 10.91,
561	            "l0_random_median": 11.52,
562	            "naive_positional": 12.23,
563	            "uniform": 15.45
564	          },
565	          {
566	            "model": "Llama",
567	            "mckp": 8.45,
568	            "l0_random_median": 10.04,
569	            "naive_positional": 9.94,
570	            "uniform": 8.47
571	          },
572	          {
573	            "model": "Mistral",
574	            "mckp": 7.16,
575	            "l0_random_median": 7.59,
576	            "naive_positional": 7.48,
577	            "uniform": 7.13
578	          }
579	        ]
580	      }
581	    ],
582	    "figures": [],
583	    "analysis": "Median reviewer 认为这是 critical missing baseline 被补充后的 adequate response。 MCKP vs L0-random gap（5-16%）证明 solver 在 constraint-respecting 方案中仍有 optimization 价值。但 Mistral 的 MCKP(7.16) > uniform(7.13) 再次说明 flat  architecture 上任何 non-uniform 都是 net negative。\n\n\nL0-only heuristic 的 PPL（Qwen median 11.52, mean 11.69）consistently worse  than MCKP（10.91），差距 -5.2%。这说明 profiling-based allocation 在 constraint  内仍有 optimization value——不仅仅是 \"protect L0 and done.\" Median reviewer  反应正面但有 nuance：(a) \"MCKP beats L0-random by 5.2% — meaningful but not  dramatic. The naive positional heuristic (12.23) is much worse, so profiling does  matter.\" (b) \"seed variance in L0-random is large (std=0.47, range 11.33-12.52),  suggesting the specific choice of which non-L0 heads get 2-bit matters significantly.\"  (c) Llama 和 Mistral 上 MCKP vs L0-random gap 更大（Llama: 8.45 vs 10.04 median,  -15.8%），说明 even on non-benefit architectures, random constraint-respecting  allocation is much worse than MCKP — the solver finds better allocations even when  the absolute PPL difference vs uniform is small. 这个 experiment 的原始设计被 kill 但后来用 corrected version (l0_heuristic_corrected) 完成。\n"
584	  },
585	  {
586	    "name": "Greedy + Cardinality Constraint Ablation (Solver Equivalence)",
587	    "description": "RateQuant greedy + max_2bit=k 约束。对比 (a) greedy unconstrained,  (b) greedy constrained k=8, (c) MCKP constrained k=8。\n",
588	    "results": {
589	      "greedy_unconstrained_ppl": 32.45,
590	      "greedy_constrained_ppl": 11.23,
591	      "mckp_constrained_ppl": 11.23,
592	      "delta_greedy_vs_mckp_constrained": 0.0012,
593	      "bit_distribution_identical": true,
594	      "distribution": "{2:8, 4:100, 8:4}"
595	    },
596	    "tables": [
597	      {
598	        "caption": "Table: Solver Equivalence Under Constraint (Qwen2.5-7B, k=8)",
599	        "rows": [
600	          {
601	            "solver": "Greedy unconstrained",
602	            "ppl": 32.45,
603	            "bit_dist": "{2:68, 4:30, 8:4, 16:10}",
604	            "status": "FAIL"
605	          },
606	          {
607	            "solver": "Greedy + max_2bit=8",
608	            "ppl": 11.23,
609	            "bit_dist": "{2:8, 4:100, 8:4}",
610	            "status": "PASS"
611	          },
612	          {
613	            "solver": "MCKP + max_2bit=8",
614	            "ppl": 11.23,
615	            "bit_dist": "{2:8, 4:100, 8:4}",
616	            "status": "PASS"
617	          },
618	          {
619	            "solver": "Uniform 4-bit",
620	            "ppl": 15.45,
621	            "bit_dist": "all 4-bit",
622	            "status": "baseline"
623	          }
624	        ]
625	      }
626	    ],
627	    "figures": [],
628	    "analysis": "Median 档中被认可为 paper 的 highlight。两位 reviewer 会引用此结果支持 \"the constraint is the contribution\" narrative。但第三位 reviewer 用此结果 反驳 \"then what exactly is the technical contribution — discovering that you need  a max_2bit cap? That's a hyperparameter, not a method.\"\n\n\n这是 paper 最 powerful 的单个实验：constrained greedy = constrained MCKP  (Δ=0.0012 PPL, identical bit distribution)。证明 constraint 是唯一 intervention  that matters——两个算法复杂度完全不同的 solver 在 constraint 下产生相同解。 Median reviewer 对此实验的反应最 positive：\"this is the strongest evidence in the  paper — it shows the cardinality constraint is the real contribution, not the  optimization algorithm.\" 但也引发 A3 concern：\"if a simple cardinality constraint  is all you need, this is essentially one hyperparameter — is that a sufficient  contribution for a main conference paper?\" Reviewer 会要求 (a) 更强的 principled  justification for why cardinality constraint works（不只是 empirical observation）， (b) 讨论 constraint 与 RateQuant 的 distortion model 的关系。Qwen14b 上也验证了 solver equivalence（greedy=MCKP, Δ=0.0），增加了 generality。\n"
629	  },
630	  {
631	    "name": "Multi-Seed Error Bars",
632	    "description": "Qwen2.5-7B 上 3 个不同 calibration seed 的 constrained MCKP，报告 mean±std。\n",
633	    "results": {
634	      "mckp_seed0": 11.02,
635	      "mckp_seed1": 10.9,
636	      "mckp_seed2": 11.05,
637	      "mckp_mean": 10.99,
638	      "mckp_std": 0.065,
639	      "bit_dist_all_seeds": "{2:8, 4:100, 8:4}",
640	      "allocation_agreement_3way": 0.902,
641	      "uniform_4bit_ppl": 15.45,
642	      "improvement_significant": true,
643	      "ci_95_upper": 11.12,
644	      "ci_95_lower": 10.86
645	    },
646	    "tables": [
647	      {
648	        "caption": "Table: Multi-Seed PPL Stability (Qwen2.5-7B, k=8)",
649	        "rows": [
650	          {
651	            "seed": 0,
652	            "ppl": 11.02,
653	            "bit_dist": "{2:8, 4:100, 8:4}"
654	          },
655	          {
656	            "seed": 1,
657	            "ppl": 10.9,
658	            "bit_dist": "{2:8, 4:100, 8:4}"
659	          },
660	          {
661	            "seed": 2,
662	            "ppl": 11.05,
663	            "bit_dist": "{2:8, 4:100, 8:4}"
664	          },
665	          {
666	            "seed": "mean±std",
667	            "ppl": "10.99±0.065",
668	            "bit_dist": "consistent"
669	          }
670	        ]
671	      }
672	    ],
673	    "figures": [],
674	    "analysis": "Median reviewer 接受 PPL 层面的 statistical credibility 但要求 downstream CI。 这是 median 档的 typical gap——不至于 reject 但会是 \"requested revision\" 的一部分。\n\n\nstd=0.065 意味着 95% CI 约 [10.86, 11.12]，远低于 uniform 15.45——improvement  统计上 robust。Bit distribution 在所有 seed 下一致（{2:8, 4:100, 8:4}）， allocation agreement 90.2% 跨 seed。Median reviewer 会认可 PPL stability 但有 两个 residual concerns：(a) \"3 seeds is the minimum — 5 seeds with proper CI would  be more convincing\"（minor revision level），(b) \"allocation agreement 90.2% means  10% of heads flip between seeds — which heads and how does it affect downstream?\"  更严重的是 A6：**缺少 multi-seed downstream CI**。PPL multi-seed 已有，但  downstream 的 arc_c +3.16pp 没有 error bar。qwen_3seed_downstream_ci 提供了 部分数据（arc_c std=0.0035），但只在 Qwen 上。Reviewer 会标注 \"multi-seed  downstream CI missing for non-Qwen architectures\" 作为 significant gap。\n"
675	  },
676	  {
677	    "name": "Runtime/Latency Benchmark",
678	    "description": "End-to-end inference latency 和 throughput，mixed-precision KV cache vs uniform 4-bit。\n",
679	    "results": {
680	      "bf16_prefill_ms": 45.86,
681	      "bf16_decode_ms": 33.78,
682	      "bf16_throughput": 29.6,
683	      "uniform4_prefill_ms": 54.25,
684	      "uniform4_decode_ms": 42.46,
685	      "uniform4_throughput": 23.6,
686	      "mckp_prefill_ms": 57.03,
687	      "mckp_decode_ms": 46.09,
688	      "mckp_throughput": 21.8,
689	      "mckp_solver_time_sec": 0.005,
690	      "memory_compression_4x": true,
691	      "mckp_overhead_vs_uniform_pct": 8.5,
692	      "mckp_overhead_vs_bf16_pct": 36.4
693	    },
694	    "tables": [
695	      {
696	        "caption": "Table: Runtime Benchmark (Qwen2.5-7B, seq_len=2048)",
697	        "rows": [
698	          {
699	            "method": "BF16 (no quantization)",
700	            "prefill_ms": 45.86,
701	            "decode_ms": 33.78,
702	            "throughput": 29.6,
703	            "memory_MB": 21
704	          },
705	          {
706	            "method": "Uniform 4-bit",
707	            "prefill_ms": 54.25,
708	            "decode_ms": 42.46,
709	            "throughput": 23.6,
710	            "memory_MB": 5.25
711	          },
712	          {
713	            "method": "Constrained MCKP",
714	            "prefill_ms": 57.03,
715	            "decode_ms": 46.09,
716	            "throughput": 21.8,
717	            "memory_MB": 5.25
718	          }
719	        ]
720	      }
721	    ],
722	    "figures": [],
723	    "analysis": "Median 档中这是 second major objection source。Runtime overhead 与  \"practical implications\" claim 冲突。Paper 需要 reframe：\"memory-bound  scenarios (long context, large batch) where 4× memory reduction enables  deployment that bf16 cannot.\" 8K context 实验（qwen7b_8k_context_eval:  uniform 77.75 vs MCKP 8.59）是 strongest counterargument——at long context,  memory savings dominate and quality gap amplifies dramatically。\n\n令人意外的 negative finding：mixed-precision MCKP 比 uniform 4-bit 更慢 （throughput 21.8 vs 23.6 tok/s, -7.6%），甚至比 bf16 baseline 更慢 （21.8 vs 29.6 tok/s, -26.4%）。原因是 mixed-precision 需要 per-head 不同 的 dequantization kernel，当前实现缺少 fused kernel optimization。 Median reviewer 反应强烈 negative：\"the method provides 29% PPL improvement  on Qwen but costs 8% throughput — practitioners would need to decide if PPL  improvement justifies speed regression. On 7/8 architectures where there's no  PPL benefit, the speed cost is pure overhead.\" 这成为 major objection 之一（A6  范畴）。MCKP solver 本身只需 0.005s（negligible），所以 overhead 完全来自 inference-time mixed-precision dequantization。需要在 paper 中承认 \"current  implementation uses naive per-head dequantization; a fused kernel could eliminate  the overhead\" 并标注为 engineering limitation, not fundamental。但 reviewer 会 counter：\"without the optimized kernel, the practical benefit claim is weakened.\"\n"
724	  }
725	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e5aa048-f8e7-4910-aa04-eb5527a54116",
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "3405a85b-9e28-46a6-afe5-cd44efbe7d57",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"L0 Exclusion Removal Ablation\",\n    \"description\": \"移除 L0 排除约束，仅保留 max_2bit=8，验证 solver 纯粹从 profiling data 自动发现 L0 敏感结构。\\n\",\n    \"results\": {\n      \"solver_auto_assigns_8bit_to_L0\": true,\n      \"ppl_without_l0_exclusion\": 10.91,\n      \"ppl_with_l0_exclusion\": 10.91,\n      \"delta\": 0.0,\n      \"l0_heads_assigned_8bit\": 4,\n      \"bit_distribution\": \"{2:8, 4:100, 8:4}\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: L0 Exclusion Ablation (Qwen2.5-7B, budget=0.25)\",\n        \"rows\": [\n          {\n            \"condition\": \"MCKP + L0 exclusion + max_2bit=8\",\n            \"ppl\": 10.91,\n            \"l0_bit\": \"8-bit (hard-coded)\",\n            \"note\": \"原始设置\"\n          },\n          {\n            \"condition\": \"MCKP + max_2bit=8 only\",\n            \"ppl\": 10.91,\n            \"l0_bit\": \"8-bit (solver-discovered)\",\n            \"note\": \"solver 自动分配\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reviewer 评价：supportive but minor。在 median 档中被视为 completeness ablation  而非核心证据。reviewer 可能建议移到 appendix。不影响主要 claim 但增加 paper 完整性。\\n\\n\\nMedian 档下该结果被 reviewer 认可为 neat ablation——solver 自动发现 L0 是最敏感的层， 不需要手动排除。但 reviewer 会指出这只在 Qwen 上验证（L0 dominance ratio=26×）， 对于 L0 dominance 低的架构（Yi 0.07，Mistral 1.74）solver 是否同样能自动发现正确结构 缺少验证。一位 reviewer 可能注释 \\\"this is expected — L0 has the largest profiling delta  by far, so any reasonable solver would protect it.\\\" 不会成为主要 objection，但也不会 被视为独立贡献。\\n\"\n  },\n  {\n    \"name\": \"Llama-3.1-8B Full Pipeline Replication\",\n    \"description\": \"在 Llama-3.1-8B（GQA 4:1）上复制完整 pipeline——profiling、constrained MCKP、PPL 评估。 测试跨架构泛化性。\\n\",\n    \"results\": {\n      \"baseline_ppl_bf16\": 8.09,\n      \"uniform_4bit_ppl\": 8.47,\n      \"mckp_constrained_ppl\": 8.45,\n      \"delta_vs_uniform_pct\": 0.2,\n      \"delta_vs_uniform_ppl\": 0.02,\n      \"memory_ratio\": 0.25,\n      \"bit_distribution\": \"{2:2, 4:253, 8:1}\",\n      \"natural_2bit_count\": 2,\n      \"constraint_binds\": false,\n      \"unconstrained_degradation_ratio\": 1.07,\n      \"top5_concentration\": 0.57,\n      \"distribution_shape\": \"Spike\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Llama-3.1-8B Pipeline Results (budget=0.25)\",\n        \"rows\": [\n          {\n            \"method\": \"BF16 baseline\",\n            \"ppl\": 8.09,\n            \"bits\": \"16\",\n            \"note\": \"\"\n          },\n          {\n            \"method\": \"Uniform 4-bit\",\n            \"ppl\": 8.47,\n            \"bits\": \"4.0\",\n            \"note\": \"\"\n          },\n          {\n            \"method\": \"Unconstrained MCKP\",\n            \"ppl\": 8.63,\n            \"bits\": \"mixed\",\n            \"note\": \"1.07× baseline\"\n          },\n          {\n            \"method\": \"Constrained MCKP (k=8)\",\n            \"ppl\": 8.45,\n            \"bits\": \"{2:2, 4:253, 8:1}\",\n            \"note\": \"+0.2% vs uniform\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median reviewer 会同时肯定和批评：肯定 honest reporting of negative result， 批评 \\\"if 7/8 architectures show no benefit, this is not a method paper — it's an  analysis paper that happens to find one architecture where optimization helps.\\\"  这强化了 reframe 为 empirical analysis 的需要。\\n\\n\\nMedian 档下，Llama 的 marginal 结果（+0.2% vs uniform）成为 reviewer 攻击点之一。 reviewer 会写 \\\"the method provides essentially no benefit on Llama — the +0.2%  improvement is within noise.\\\" Llama 的 spike distribution（L2H5 单个 outlier 主导， t₁/t₅≈0.85）导致 solver 只选择 2 个 head 做 2-bit，constraint 从不触发（natural k=2 < max_2bit=8）， MCKP 优化空间极小。这解释了为什么 PPL 差异几乎为零。但从 compounding 角度， unconstrained 仍然 1.07× baseline，说明即使 mild 情况下 solver 仍会略微 over-allocate。 Reviewer 会要求诚实报告 \\\"no benefit\\\" 而非 spin 为 positive。在 median 档中， 这个 negative result 本身不被反对——reviewer 反对的是用 8 个架构中只有 1 个 positive  来声称 method 有效。\\n\"\n  },\n  {\n    \"name\": \"Mistral-7B-v0.3 Full Pipeline Replication\",\n    \"description\": \"在 Mistral-7B-v0.3 上复制完整 pipeline。不同架构家族，建立跨架构有效性。\\n\",\n    \"results\": {\n      \"baseline_ppl_bf16\": 7.035,\n      \"uniform_4bit_ppl\": 7.131,\n      \"mckp_constrained_ppl\": 7.165,\n      \"delta_vs_uniform_pct\": -0.5,\n      \"delta_vs_uniform_ppl\": -0.034,\n      \"memory_ratio\": 0.25,\n      \"bit_distribution\": \"{2:4, 4:252}\",\n      \"unconstrained_degradation_ratio\": 1.08,\n      \"top5_concentration\": 0.22,\n      \"distribution_shape\": \"Flat\",\n      \"k_ablation_monotonic\": true,\n      \"best_k_still_worse_than_uniform\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Mistral-7B-v0.3 k-Ablation (budget=0.25)\",\n        \"rows\": [\n          {\n            \"k\": 4,\n            \"ppl\": 7.165,\n            \"n_2bit\": 4,\n            \"note\": \"best constrained, still > uniform\"\n          },\n          {\n            \"k\": 8,\n            \"ppl\": 7.2,\n            \"n_2bit\": 8,\n            \"note\": \"\"\n          },\n          {\n            \"k\": 16,\n            \"ppl\": 7.311,\n            \"n_2bit\": 16,\n            \"note\": \"\"\n          },\n          {\n            \"k\": \"uniform\",\n            \"ppl\": 7.131,\n            \"n_2bit\": 0,\n            \"note\": \"optimal for Mistral\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 median 档中，Mistral negative result 既是弱点也是优势。弱点：method 不 work。 优势：honest negative result 增加 credibility，且支持 diagnostic 的必要性—— 如果没有 diagnostic，practitioners 会浪费 profiling 时间在 Mistral 这样的模型上。 Reviewer 2 (偏方法) 会将此作为 \\\"method only works on Qwen\\\" 的证据。 Reviewer 3 (偏分析) 会认可这增加了 paper 的科学价值。\\n\\n\\nMistral 是最强 negative case：MCKP 在所有 k 值下都 worse than uniform。 PPL 随 k 单调递增（k=4: 7.165, k=8: 7.200, k=18: 7.323），profiler 报告近零  sensitivity 差异（concentration=0.22, CV=1.31）。这表明 Mistral 的 KV head  sensitivity 高度均匀——没有 head 从 2-bit downgrade 中获益。Median reviewer  会将此视为 \\\"method failure on flat architectures\\\" 和 \\\"proof that uniform 4-bit  is optimal when profiler gives zero signal.\\\" 对 compounding claim 仍有帮助： unconstrained 1.08× 表明即使 flat distribution，solver 仍 over-allocate  2-bit heads（42/256=16.4%）。但 reviewer 会质疑 \\\"1.08× is hardly catastrophic  — this is within the range where a practitioner wouldn't even notice.\\\"\\n\"\n  },\n  {\n    \"name\": \"Compounding Effect Characterization Sweep\",\n    \"description\": \"在 Qwen2.5-7B 上扫 max_2bit 从 0 到 112，绘制 PPL vs max_2bit 曲线， 确定 compounding 阈值。建立 cardinality constraint 的 principled 基础。\\n\",\n    \"results\": {\n      \"k0_ppl\": 9.81,\n      \"k8_ppl\": 10.05,\n      \"k16_ppl\": 10.42,\n      \"k32_ppl\": 11.6,\n      \"k64_ppl\": 23.22,\n      \"k112_ppl\": 98.75,\n      \"compounding_threshold_k\": 16,\n      \"max_compounding_ratio\": 10.07,\n      \"curve_shape\": \"superlinear after k≈16, exponential after k≈48\",\n      \"safe_k_range\": \"k≤8 universally <2.5% degradation\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Compounding Sweep (Qwen2.5-7B, budget=0.25)\",\n        \"rows\": [\n          {\n            \"k\": 0,\n            \"ppl\": 9.81,\n            \"ratio_to_baseline\": \"1.00×\"\n          },\n          {\n            \"k\": 8,\n            \"ppl\": 10.05,\n            \"ratio_to_baseline\": \"1.02×\"\n          },\n          {\n            \"k\": 16,\n            \"ppl\": 10.42,\n            \"ratio_to_baseline\": \"1.06×\"\n          },\n          {\n            \"k\": 32,\n            \"ppl\": 11.6,\n            \"ratio_to_baseline\": \"1.18×\"\n          },\n          {\n            \"k\": 64,\n            \"ppl\": 23.22,\n            \"ratio_to_baseline\": \"2.37×\"\n          },\n          {\n            \"k\": 112,\n            \"ppl\": 98.75,\n            \"ratio_to_baseline\": \"10.07×\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median reviewer 的核心反馈：compounding effect 是 real and well-characterized， 但 novelty 因 RateQuant Appendix M 打折。建议在 related work 中显式讨论  \\\"RateQuant acknowledges compounding in Appendix M but does not characterize the  threshold or provide a fix — our sweep provides the first quantitative mapping.\\\"  三架构对比增加说服力：Qwen 的 U-shape（optimal k=8）、Llama 的 flat profile （natural k=2, constraint irrelevant）、Mistral 的 monotonic increase（every  2-bit head hurts）展示了 architecture-dependent compounding behavior。\\n\\n\\nCompounding sweep 是 median 档中最被认可的实验——提供了 compounding 效应的 定量证据。PPL 在 k≤8 时近线性增长（9.81→10.05, +2.4%），k=16-32 开始加速 （10.42→11.60），k≥48 后指数爆炸（23.22→98.75）。这条曲线是 \\\"principled  basis for constraint selection\\\" 的核心证据。但 median reviewer 会有两个质疑： (1) \\\"这条曲线只在 Qwen 上做了——其他架构的阈值可能完全不同\\\"（A2）， (2) \\\"RateQuant Appendix M 已经 acknowledge compounding，这个 sweep 只是 quantified 了已知现象\\\"（A1）。需要补充 Llama 和 Mistral 的 compounding sweep  来部分 address (1)——实际已有数据（llama_compounding_sweep, mistral_compounding_sweep_v2） 可以回应。Reviewer 对 k≤8 safety 的 claim 会接受，但会要求去掉 \\\"universally safe\\\"  改为 \\\"safe across all tested architectures.\\\"\\n\"\n  },\n  {\n    \"name\": \"Budget Sweep (2×/4×/8× Compression)\",\n    \"description\": \"在 Qwen2.5-7B 上测试 2×/4×/8× 压缩比下的 constrained MCKP vs uniform baseline。\\n\",\n    \"results\": {\n      \"budget_0.5_mckp_ppl\": 9.85,\n      \"budget_0.5_uniform_ppl\": 9.86,\n      \"budget_0.5_delta_pct\": 0.1,\n      \"budget_0.25_mckp_ppl\": 10.91,\n      \"budget_0.25_uniform_ppl\": 15.45,\n      \"budget_0.25_delta_pct\": 29.4,\n      \"budget_0.125_mckp_ppl\": 57.6,\n      \"budget_0.125_uniform_2bit_ppl\": 2643.77,\n      \"budget_0.125_delta_ratio\": \"45.9×\",\n      \"compression_amplifies_benefit\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Budget Sweep (Qwen2.5-7B)\",\n        \"rows\": [\n          {\n            \"compression\": \"2× (budget=0.5)\",\n            \"mckp_ppl\": 9.85,\n            \"uniform_ppl\": 9.86,\n            \"delta\": \"~0%\"\n          },\n          {\n            \"compression\": \"4× (budget=0.25)\",\n            \"mckp_ppl\": 10.91,\n            \"uniform_ppl\": 15.45,\n            \"delta\": \"29.4%\"\n          },\n          {\n            \"compression\": \"8× (budget=0.125)\",\n            \"mckp_ppl\": 57.6,\n            \"uniform_ppl\": 2643.77,\n            \"delta\": \"45.9×\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中被部分接受。Reviewer 认可 practical implication（高压缩比下 constraint  essential），但质疑 moderate compression（主要应用场景）下只有 Qwen 获益的泛化性。 建议补充 Llama/Mistral 的 budget sweep 至少在 8× 压缩点。\\n\\n\\nBudget sweep 展示了核心趋势：压缩越激进，constrained MCKP vs uniform 的差距越大。 在 2× 压缩下差异几乎为零（都接近 baseline），4× 时 MCKP 优势 29.4%，8× 时 MCKP 57.60 vs uniform 2643.77（45×差距）。Median reviewer 会认可 aggressive  compression 的 practical value（\\\"at 8× compression, the constraint is the difference  between usable and unusable\\\"），但会指出：(a) 2× 结果说明 moderate compression 下 benefit 主要来自 Qwen 的 spread pattern 而非 method 本身，(b) 8× 的 PPL=57.60  虽远好于 2643.77，但 absolute 值仍然很高——\\\"is a 57.60 PPL model actually usable?\\\"  需要补充 aggressive compression 下的 downstream task 评估。(c) 只在 Qwen 上做了 full sweep，Llama 的 aggressive compression 数据（57.60 vs 2643.77）虽有但 仅一个点，不是 sweep。\\n\"\n  },\n  {\n    \"name\": \"High-Resolution Profiling\",\n    \"description\": \"64 seq × 2048 tokens 的高分辨率 profiling（vs 16×512），验证更好的 profiling  是否改善 solver allocation。\\n\",\n    \"results\": {\n      \"hires_constrained_ppl_bf16\": 10.91,\n      \"lowres_constrained_ppl_bf16\": 11.23,\n      \"baseline_ppl_bf16\": 9.81,\n      \"improvement_vs_lowres\": 0.32,\n      \"improvement_pct\": 2.8,\n      \"hires_nonzero_2bit_heads\": 100,\n      \"lowres_nonzero_2bit_heads\": 37,\n      \"allocation_diff_count\": 8,\n      \"profiling_time_min\": 65.5,\n      \"bit_distribution\": \"{2:8, 4:100, 8:4}\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Profiling Resolution Impact (Qwen2.5-7B, k=8)\",\n        \"rows\": [\n          {\n            \"resolution\": \"Low-res (16×512)\",\n            \"ppl\": 11.23,\n            \"nonzero_heads\": 37,\n            \"time_min\": \"~10\"\n          },\n          {\n            \"resolution\": \"High-res (64×2048)\",\n            \"ppl\": 10.91,\n            \"nonzero_heads\": 100,\n            \"time_min\": 65.5\n          },\n          {\n            \"resolution\": \"Uniform 4-bit\",\n            \"ppl\": 15.45,\n            \"nonzero_heads\": \"N/A\",\n            \"time_min\": 0\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中作为 engineering insight 被接受。Reviewer 不会 object 但建议 放 appendix 而非 main body。对 claim 的影响中性——既不强化也不削弱核心论点。\\n\\n\\n高分辨率 profiling 将 PPL 从 11.23 降到 10.91（-2.8%），说明 profiling resolution  matters。核心改进来自更准确的 sensitivity ranking：hires 发现 100/112 heads 有 非零 2-bit delta（vs lowres 37/112），导致 8 个 head 的 allocation 改变。 Median reviewer 反应分化：(a) 方法 reviewer 认为这说明 \\\"profiling quality drives  results more than solver choice — the real engineering is in the profiler, not MCKP\\\"， 进一步削弱 solver 作为贡献的地位；(b) 系统 reviewer 注意到 65.5 min profiling time  并质疑 \\\"practitioners won't spend an hour profiling a 7B model to save 0.32 PPL\\\"。 需要在 paper 中 trade-off profiling cost vs quality，并论证 lowres 已足够好 （11.23 vs uniform 15.45, 仍有 27.3% improvement）。\\n\"\n  },\n  {\n    \"name\": \"C4 Cross-Dataset Evaluation\",\n    \"description\": \"在 C4 上评估 Qwen2.5-7B（calibrate on WikiText-2, eval on C4; calibrate on C4, eval on WikiText-2）， 验证结果不是 WikiText-2 specific。\\n\",\n    \"results\": {\n      \"c4_cal_wt2_eval_mckp_ppl\": 11.29,\n      \"c4_cal_wt2_eval_uniform_ppl\": 15.45,\n      \"c4_cal_wt2_eval_delta\": 4.15,\n      \"allocation_agreement_c4_vs_wt2\": 0.964,\n      \"agreement_heads\": \"108/112\",\n      \"cross_domain_wt2_to_c4_mckp_ppl\": 20.56,\n      \"cross_domain_wt2_to_c4_uniform_ppl\": 35.42,\n      \"contamination_impact\": 0.034\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Cross-Dataset Calibration Agreement\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen2.5-7B\",\n            \"agreement\": \"108/112 (96.4%)\",\n            \"same_domain_ppl\": 11.29,\n            \"cross_domain_ppl\": 20.56\n          },\n          {\n            \"model\": \"Llama-3.1-8B\",\n            \"agreement\": \"250/256 (97.7%)\",\n            \"same_domain_ppl\": 8.45,\n            \"cross_domain_ppl\": 8.65\n          },\n          {\n            \"model\": \"Mistral-7B-v0.3\",\n            \"agreement\": \"247/256 (96.5%)\",\n            \"same_domain_ppl\": 7.16,\n            \"cross_domain_ppl\": 7.19\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"三架构的 >96% agreement 是 strong evidence for calibration robustness。 Median reviewer 视为 useful supplementary experiment，不会 object。 建议放 Section 4 或 appendix。\\n\\n\\n96.4% allocation agreement 跨 calibration source 是 positive signal：profiling  的 head sensitivity ranking 对 calibration data 不敏感。Median reviewer 会认可  cross-dataset robustness 但指出：(a) 只在 Qwen 上验证（\\\"is this agreement rate  architecture-dependent?\\\"），(b) 4/112 disagreement heads 的 identity 和影响未讨论， (c) cross-domain PPL（WiKi→C4: 20.56 vs uniform 35.42）虽然 MCKP 仍胜出， 但绝对 PPL 远高于 same-domain（11.29），说明 calibration domain mismatch 仍有成本。 Reviewer 会建议 \\\"report agreement rate on at least one more architecture\\\" 作为 minor revision。已有 llama_c4_cross_dataset（97.7% agreement）和  mistral_c4_cross_dataset（96.5%）数据可以回应。\\n\"\n  },\n  {\n    \"name\": \"RateQuant Greedy Comparison\",\n    \"description\": \"实现 RateQuant 的 greedy Algorithm 1 在 {2,4,8,16} 上，展示 greedy 在 non-consecutive 集合上 suboptimal。\\n\",\n    \"results\": {\n      \"ratequant_greedy_unconstrained_ppl\": 32.45,\n      \"mckp_unconstrained_ppl\": 36.92,\n      \"uniform_4bit_ppl\": 15.45,\n      \"greedy_bit_distribution\": \"{2:68, 4:30, 8:4, 16:10}\",\n      \"both_worse_than_uniform\": true,\n      \"greedy_better_than_mckp_unconstrained\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Unconstrained Solver Comparison (Qwen2.5-7B)\",\n        \"rows\": [\n          {\n            \"solver\": \"RateQuant Greedy (unconstrained)\",\n            \"ppl\": 32.45,\n            \"n_2bit\": 68,\n            \"status\": \"FAIL\"\n          },\n          {\n            \"solver\": \"MCKP (unconstrained)\",\n            \"ppl\": 36.92,\n            \"n_2bit\": \"≥68\",\n            \"status\": \"FAIL\"\n          },\n          {\n            \"solver\": \"Uniform 4-bit\",\n            \"ppl\": 15.45,\n            \"n_2bit\": 0,\n            \"status\": \"baseline\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中该实验的价值被 reinterpret：不再是 \\\"MCKP beats greedy\\\"  而是 \\\"both fail without constraint, both succeed with constraint.\\\"  这是 solver equivalence 叙事的第一半证据。Reviewer 认可这个 framing shift。\\n\\n\\n关键发现：两个 solver 在 unconstrained 设置下都 worse than uniform，但 greedy  (32.45) 反而比 MCKP (36.92) 好！这颠覆了 \\\"MCKP is better optimizer\\\" 的叙事。 Median reviewer 会抓住这个点：\\\"if greedy outperforms MCKP unconstrained,  why do you need MCKP at all?\\\" 回应：unconstrained 时两者都失败（compounding）， 差异无意义；constrained 时两者完全一致（Δ=0.0000）——plan_016 的 solver equivalence  证据。但这确实削弱了 MCKP 作为 solver contribution 的叙事，支持 reframe： \\\"constraint is the contribution, not the solver.\\\" 一位 reviewer 会标注  \\\"the unconstrained MCKP being worse than greedy suggests the ILP formulation  interacts poorly with compounding — discuss this.\\\" 需要在 paper 中解释为什么 MCKP 更容易 over-allocate 2-bit（因为它更 aggressively optimizes per-head  cost-benefit，导致更多 2-bit assignments）。\\n\"\n  },\n  {\n    \"name\": \"Oracle Comparison (Subset Brute-Force)\",\n    \"description\": \"在 Qwen2.5-7B 的 3-4 个 layer group 上做 brute-force optimal allocation， 量化 MCKP gap to oracle。\\n\",\n    \"results\": {\n      \"mckp_ppl\": 10.91,\n      \"max_oracle_gap_ppl\": 0.018,\n      \"avg_oracle_gap_ppl\": 0.005,\n      \"layers_mckp_optimal\": \"5/8\",\n      \"layers_with_gap\": 3,\n      \"gap_nature\": \"2-bit head position swap within same bit budget\",\n      \"total_evals\": 54\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: MCKP vs Oracle Gap (Qwen2.5-7B, per layer group)\",\n        \"rows\": [\n          {\n            \"layer_group\": \"L0-L3\",\n            \"mckp_optimal\": true,\n            \"gap_ppl\": 0.0\n          },\n          {\n            \"layer_group\": \"L4-L7\",\n            \"mckp_optimal\": false,\n            \"gap_ppl\": 0.0045\n          },\n          {\n            \"layer_group\": \"L8-L11\",\n            \"mckp_optimal\": false,\n            \"gap_ppl\": 0.0136\n          },\n          {\n            \"layer_group\": \"L12-L15\",\n            \"mckp_optimal\": true,\n            \"gap_ppl\": 0.0\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Near-zero oracle gap 与 solver equivalence 共同构成 \\\"constraint is what matters\\\"  的完整论证。Median reviewer 视为 thorough analysis, 建议作为 Section 4 的 supporting evidence。\\n\\n\\nMCKP 与 oracle 的 gap 极小（max 0.018 PPL, avg 0.005 PPL），5/8 layer groups  完全 optimal，3 个 gap 来自同 budget 下 2-bit head 位置互换。Median reviewer  会认可 \\\"MCKP is near-optimal within the constrained feasible set\\\" 但立刻指出： \\\"combined with plan_016 showing greedy=MCKP, this means the constraint defines  the quality — any solver that respects the constraint is near-optimal. The MCKP  formulation adds no value.\\\" 这进一步支持 constraint-as-contribution framing， 但同时使 MCKP 作为 method 贡献更不站得住。reviewer 建议 \\\"present MCKP as the  analysis framework, not the algorithmic contribution.\\\" 在 median 档中这个实验 反而帮助了 reframe——它是 \\\"solver doesn't matter\\\" 叙事的 complementary evidence。\\n\"\n  },\n  {\n    \"name\": \"Cross-Domain Calibration Robustness\",\n    \"description\": \"C4 calibration → WikiText-2 eval 和反方向，报告 per-head allocation agreement rate。\\n\",\n    \"results\": {\n      \"allocation_agreement_c4_vs_wt2\": 0.964,\n      \"agreement_heads\": \"108/112\",\n      \"c4_cal_wt2_eval_mckp_ppl\": 11.29,\n      \"cross_domain_gap_vs_same_domain\": 0.06\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Minor positive signal。在 median 档中作为 robustness check 被接受， 不影响 overall score。\\n\\n\\n与 plan_007 共享数据。96.4% agreement 说明 profiling-based sensitivity ranking  对 calibration source 高度鲁棒。Median reviewer 反应温和 positive——这是 expected behavior（\\\"if head sensitivity is an architectural property, it shouldn't  depend on calibration data\\\"），所以不会 strongly impress but also won't object。 主要 reviewer concern 是 Qwen-only，但已有三架构数据（Qwen 96.4%, Llama 97.7%,  Mistral 96.5%）可补充。\\n\"\n  },\n  {\n    \"name\": \"Head Sensitivity Visualization\",\n    \"description\": \"生成 per-head profiling delta heatmap、compounding curve、budget allocation 对比图。\\n\",\n    \"results\": {\n      \"figures_generated\": 3,\n      \"heatmap_shows_l0_dominance\": true,\n      \"compounding_curve_elbow\": \"k≈16\",\n      \"allocation_comparison_shows_constraint_effect\": true\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Presentation-level contribution。Median reviewer 可能 suggest 改进但不会 因为 visualization 加分或扣分。\\n\\n\\n可视化是 presentation quality 问题而非科学证据。Median reviewer 会在 minor comments 中评价：\\\"Figure X clearly shows the L0 dominance pattern\\\"  或 \\\"the compounding curve would benefit from error bars.\\\" 不影响 score 但 好的可视化可以帮助 reviewer 快速理解 compounding 现象。关键是 heatmap 要 展示 Qwen（spread, L0 cluster 明显）vs Yi（spike, 单个 L4H3 突出）vs  Gemma-2（flat, 无显著差异）的对比——如果只展示 Qwen，reviewer 会说  \\\"cherry-picked visualization.\\\"\\n\"\n  },\n  {\n    \"name\": \"K/V Separation\",\n    \"description\": \"K 和 V heads 作为独立 MCKP items，独立 budget allocation。与 joint K=V 方法对比。\\n\",\n    \"results\": {\n      \"kv_sep_ppl\": 11.22,\n      \"joint_kv_ppl\": 10.91,\n      \"uniform_4bit_ppl\": 15.45,\n      \"delta_sep_vs_joint\": 0.31,\n      \"sep_k_2bit_count\": 16,\n      \"sep_v_uniform_4bit\": true,\n      \"kv_asymmetric_heads\": 21\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: K/V Separation vs Joint (Qwen2.5-7B, k=8)\",\n        \"rows\": [\n          {\n            \"method\": \"Joint K=V (k=8)\",\n            \"ppl\": 10.91,\n            \"k_2bit\": 8,\n            \"v_2bit\": 0\n          },\n          {\n            \"method\": \"K/V Separation\",\n            \"ppl\": 11.22,\n            \"k_2bit\": 16,\n            \"v_2bit\": 0\n          },\n          {\n            \"method\": \"Uniform 4-bit\",\n            \"ppl\": 15.45,\n            \"k_2bit\": 0,\n            \"v_2bit\": 0\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative result 但 informative。在 median 档中被视为 thorough ablation， 可放 appendix。不影响核心 claim。\\n\\n\\nK/V separation 反而 worse（11.22 vs 10.91, +0.31 PPL）。separation 给 K heads  分配了 16 个 2-bit（超过 max_2bit=8 的 joint 约束），导致 K cache compounding。 V heads 在 separation 下全部 4-bit（optimal for V），但 K cache 的退化超过了 V 的收益。Median reviewer 会认为这是 negative result 但有 insight value： \\\"K cache is more sensitive to 2-bit compounding than V — this explains why  joint K=V treatment with a single cardinality constraint works better.\\\"  一位 reviewer 可能 suggest \\\"apply per-cache-type cardinality constraint\\\"  as future work。不会成为 major objection。\\n\"\n  },\n  {\n    \"name\": \"Downstream Task Evaluation (Qwen2.5-7B)\",\n    \"description\": \"ARC-C / HellaSwag / PIQA / WinoGrande 在 Qwen2.5-7B 4× 压缩下评估。 验证 PPL improvement 转化为 downstream performance。\\n\",\n    \"results\": {\n      \"arc_c_uniform\": 0.4812,\n      \"arc_c_mckp\": 0.5137,\n      \"arc_c_delta_pp\": 3.16,\n      \"hellaswag_uniform\": 0.7284,\n      \"hellaswag_mckp\": 0.7684,\n      \"hellaswag_delta_pp\": 4.0,\n      \"piqa_uniform\": 0.7661,\n      \"piqa_mckp\": 0.7786,\n      \"piqa_delta_pp\": 1.25,\n      \"winogrande_uniform\": 0.6622,\n      \"winogrande_mckp\": 0.6819,\n      \"winogrande_delta_pp\": 1.97,\n      \"avg_recovery\": 0.728,\n      \"bf16_avg\": 0.688\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Downstream Evaluation — Full Cross-Architecture\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen (Spread)\",\n            \"avg_delta_pp\": \"+2.60\",\n            \"arc_c_delta\": \"+3.16\",\n            \"verdict\": \"Benefit\"\n          },\n          {\n            \"model\": \"Yi-1.5 (Spike)\",\n            \"avg_delta_pp\": \"-0.77\",\n            \"arc_c_delta\": \"-3.24\",\n            \"verdict\": \"Degradation\"\n          },\n          {\n            \"model\": \"Llama (Spike)\",\n            \"avg_delta_pp\": \"-0.99\",\n            \"arc_c_delta\": \"-2.65\",\n            \"verdict\": \"Degradation\"\n          },\n          {\n            \"model\": \"Mistral (Flat)\",\n            \"avg_delta_pp\": \"-0.48\",\n            \"arc_c_delta\": \"-1.19\",\n            \"verdict\": \"Degradation\"\n          },\n          {\n            \"model\": \"Gemma-2 (Flat)\",\n            \"avg_delta_pp\": \"+0.14\",\n            \"arc_c_delta\": \"-0.17\",\n            \"verdict\": \"Noise\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中这是 double-edged evidence。Qwen 的 downstream gains 被认可但 限定为 \\\"architecture-specific\\\"。跨架构 degradation 要求论文措辞从 \\\"non-uniform improves downstream\\\" 改为 \\\"non-uniform allocation improves downstream  performance specifically on architectures with spread sensitivity patterns (1/5  tested); on other architectures, uniform 4-bit should be preferred.\\\"  arc_challenge 系统性退化需要主动讨论段落。\\n\\n\\nQwen downstream gains 一致 positive（+1.25 to +4.00pp），与 PPL improvement  方向一致。但 median reviewer 的核心 objection 是 A4：\\\"this only works on Qwen.\\\" 跨架构 downstream 数据显示 Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp,  Gemma-2 +0.14pp（noise）。reviewer 会写：\\\"4/5 architectures show negative or  negligible downstream effect. The method degrades downstream performance on most  models.\\\" 另一个 median-specific concern 是 lack of multi-seed CI：3.16pp arc_c  delta 没有 confidence interval，\\\"could be within single-run variance\\\"（A6）。 已有 qwen_3seed_downstream_ci（arc_c std=0.0035, hellaswag std=0.0022） 可部分回应。arc_challenge 跨模型系统性退化（Yi -3.24pp, Llama -2.65pp,  Mistral -1.19pp）会被特别标注——reviewer 要求主动讨论这个 pattern。\\n\"\n  },\n  {\n    \"name\": \"70B Profiling-Only\",\n    \"description\": \"在 Qwen2.5-72B 上做 distortion profiling（不做 full eval），分析 sensitivity  patterns 是否随模型大小 scale。\\n\",\n    \"results\": {\n      \"status\": \"killed\",\n      \"sensitivity_pattern_observed\": null,\n      \"l0_dominance_scales\": null\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Missing data。Median reviewer 标注为 limitation，不作为 reject reason。\\n\\n\\n实验被 killed（可能 OOM 或 timeout）。Median reviewer 会注意到 \\\"only 7B-14B  scale models tested\\\" 并标注为 limitation：\\\"no evidence that findings generalize  to production-scale models (70B+).\\\" 但在 median 档中这是 minor gap 而非 major  objection——大多数 KV cache quantization papers 也只测 7B-14B。缺少 70B 数据 会降低 \\\"practical implications\\\" 的说服力但不会导致 reject。建议在 limitations  中明确承认 \\\"our experiments are limited to 7B-14B scale; scaling behavior of  compounding effects to 70B+ models remains an open question.\\\"\\n\"\n  },\n  {\n    \"name\": \"L0-Only Heuristic Baseline\",\n    \"description\": \"最简单的 non-uniform 策略：L0 heads 8-bit，其余 uniform 4-bit。如果 L0-only 匹配 MCKP，full optimization 不必要。\\n\",\n    \"results\": {\n      \"qwen_mckp_ppl\": 10.91,\n      \"qwen_l0_random_mean\": 11.69,\n      \"qwen_l0_random_std\": 0.47,\n      \"qwen_l0_random_median\": 11.52,\n      \"qwen_naive_positional_ppl\": 12.23,\n      \"llama_mckp_ppl\": 8.45,\n      \"llama_l0_random_mean\": 10.48,\n      \"llama_naive_positional\": 9.94,\n      \"mistral_mckp_ppl\": 7.16,\n      \"mistral_l0_random_mean\": 7.56,\n      \"mistral_naive_positional\": 7.48,\n      \"mckp_consistently_beats_l0_random\": true\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: MCKP vs Heuristic Baselines (budget=0.25)\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen\",\n            \"mckp\": 10.91,\n            \"l0_random_median\": 11.52,\n            \"naive_positional\": 12.23,\n            \"uniform\": 15.45\n          },\n          {\n            \"model\": \"Llama\",\n            \"mckp\": 8.45,\n            \"l0_random_median\": 10.04,\n            \"naive_positional\": 9.94,\n            \"uniform\": 8.47\n          },\n          {\n            \"model\": \"Mistral\",\n            \"mckp\": 7.16,\n            \"l0_random_median\": 7.59,\n            \"naive_positional\": 7.48,\n            \"uniform\": 7.13\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median reviewer 认为这是 critical missing baseline 被补充后的 adequate response。 MCKP vs L0-random gap（5-16%）证明 solver 在 constraint-respecting 方案中仍有 optimization 价值。但 Mistral 的 MCKP(7.16) > uniform(7.13) 再次说明 flat  architecture 上任何 non-uniform 都是 net negative。\\n\\n\\nL0-only heuristic 的 PPL（Qwen median 11.52, mean 11.69）consistently worse  than MCKP（10.91），差距 -5.2%。这说明 profiling-based allocation 在 constraint  内仍有 optimization value——不仅仅是 \\\"protect L0 and done.\\\" Median reviewer  反应正面但有 nuance：(a) \\\"MCKP beats L0-random by 5.2% — meaningful but not  dramatic. The naive positional heuristic (12.23) is much worse, so profiling does  matter.\\\" (b) \\\"seed variance in L0-random is large (std=0.47, range 11.33-12.52),  suggesting the specific choice of which non-L0 heads get 2-bit matters significantly.\\\"  (c) Llama 和 Mistral 上 MCKP vs L0-random gap 更大（Llama: 8.45 vs 10.04 median,  -15.8%），说明 even on non-benefit architectures, random constraint-respecting  allocation is much worse than MCKP — the solver finds better allocations even when  the absolute PPL difference vs uniform is small. 这个 experiment 的原始设计被 kill 但后来用 corrected version (l0_heuristic_corrected) 完成。\\n\"\n  },\n  {\n    \"name\": \"Greedy + Cardinality Constraint Ablation (Solver Equivalence)\",\n    \"description\": \"RateQuant greedy + max_2bit=k 约束。对比 (a) greedy unconstrained,  (b) greedy constrained k=8, (c) MCKP constrained k=8。\\n\",\n    \"results\": {\n      \"greedy_unconstrained_ppl\": 32.45,\n      \"greedy_constrained_ppl\": 11.23,\n      \"mckp_constrained_ppl\": 11.23,\n      \"delta_greedy_vs_mckp_constrained\": 0.0012,\n      \"bit_distribution_identical\": true,\n      \"distribution\": \"{2:8, 4:100, 8:4}\"\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Solver Equivalence Under Constraint (Qwen2.5-7B, k=8)\",\n        \"rows\": [\n          {\n            \"solver\": \"Greedy unconstrained\",\n            \"ppl\": 32.45,\n            \"bit_dist\": \"{2:68, 4:30, 8:4, 16:10}\",\n            \"status\": \"FAIL\"\n          },\n          {\n            \"solver\": \"Greedy + max_2bit=8\",\n            \"ppl\": 11.23,\n            \"bit_dist\": \"{2:8, 4:100, 8:4}\",\n            \"status\": \"PASS\"\n          },\n          {\n            \"solver\": \"MCKP + max_2bit=8\",\n            \"ppl\": 11.23,\n            \"bit_dist\": \"{2:8, 4:100, 8:4}\",\n            \"status\": \"PASS\"\n          },\n          {\n            \"solver\": \"Uniform 4-bit\",\n            \"ppl\": 15.45,\n            \"bit_dist\": \"all 4-bit\",\n            \"status\": \"baseline\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中被认可为 paper 的 highlight。两位 reviewer 会引用此结果支持 \\\"the constraint is the contribution\\\" narrative。但第三位 reviewer 用此结果 反驳 \\\"then what exactly is the technical contribution — discovering that you need  a max_2bit cap? That's a hyperparameter, not a method.\\\"\\n\\n\\n这是 paper 最 powerful 的单个实验：constrained greedy = constrained MCKP  (Δ=0.0012 PPL, identical bit distribution)。证明 constraint 是唯一 intervention  that matters——两个算法复杂度完全不同的 solver 在 constraint 下产生相同解。 Median reviewer 对此实验的反应最 positive：\\\"this is the strongest evidence in the  paper — it shows the cardinality constraint is the real contribution, not the  optimization algorithm.\\\" 但也引发 A3 concern：\\\"if a simple cardinality constraint  is all you need, this is essentially one hyperparameter — is that a sufficient  contribution for a main conference paper?\\\" Reviewer 会要求 (a) 更强的 principled  justification for why cardinality constraint works（不只是 empirical observation）， (b) 讨论 constraint 与 RateQuant 的 distortion model 的关系。Qwen14b 上也验证了 solver equivalence（greedy=MCKP, Δ=0.0），增加了 generality。\\n\"\n  },\n  {\n    \"name\": \"Multi-Seed Error Bars\",\n    \"description\": \"Qwen2.5-7B 上 3 个不同 calibration seed 的 constrained MCKP，报告 mean±std。\\n\",\n    \"results\": {\n      \"mckp_seed0\": 11.02,\n      \"mckp_seed1\": 10.9,\n      \"mckp_seed2\": 11.05,\n      \"mckp_mean\": 10.99,\n      \"mckp_std\": 0.065,\n      \"bit_dist_all_seeds\": \"{2:8, 4:100, 8:4}\",\n      \"allocation_agreement_3way\": 0.902,\n      \"uniform_4bit_ppl\": 15.45,\n      \"improvement_significant\": true,\n      \"ci_95_upper\": 11.12,\n      \"ci_95_lower\": 10.86\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Multi-Seed PPL Stability (Qwen2.5-7B, k=8)\",\n        \"rows\": [\n          {\n            \"seed\": 0,\n            \"ppl\": 11.02,\n            \"bit_dist\": \"{2:8, 4:100, 8:4}\"\n          },\n          {\n            \"seed\": 1,\n            \"ppl\": 10.9,\n            \"bit_dist\": \"{2:8, 4:100, 8:4}\"\n          },\n          {\n            \"seed\": 2,\n            \"ppl\": 11.05,\n            \"bit_dist\": \"{2:8, 4:100, 8:4}\"\n          },\n          {\n            \"seed\": \"mean±std\",\n            \"ppl\": \"10.99±0.065\",\n            \"bit_dist\": \"consistent\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median reviewer 接受 PPL 层面的 statistical credibility 但要求 downstream CI。 这是 median 档的 typical gap——不至于 reject 但会是 \\\"requested revision\\\" 的一部分。\\n\\n\\nstd=0.065 意味着 95% CI 约 [10.86, 11.12]，远低于 uniform 15.45——improvement  统计上 robust。Bit distribution 在所有 seed 下一致（{2:8, 4:100, 8:4}）， allocation agreement 90.2% 跨 seed。Median reviewer 会认可 PPL stability 但有 两个 residual concerns：(a) \\\"3 seeds is the minimum — 5 seeds with proper CI would  be more convincing\\\"（minor revision level），(b) \\\"allocation agreement 90.2% means  10% of heads flip between seeds — which heads and how does it affect downstream?\\\"  更严重的是 A6：**缺少 multi-seed downstream CI**。PPL multi-seed 已有，但  downstream 的 arc_c +3.16pp 没有 error bar。qwen_3seed_downstream_ci 提供了 部分数据（arc_c std=0.0035），但只在 Qwen 上。Reviewer 会标注 \\\"multi-seed  downstream CI missing for non-Qwen architectures\\\" 作为 significant gap。\\n\"\n  },\n  {\n    \"name\": \"Runtime/Latency Benchmark\",\n    \"description\": \"End-to-end inference latency 和 throughput，mixed-precision KV cache vs uniform 4-bit。\\n\",\n    \"results\": {\n      \"bf16_prefill_ms\": 45.86,\n      \"bf16_decode_ms\": 33.78,\n      \"bf16_throughput\": 29.6,\n      \"uniform4_prefill_ms\": 54.25,\n      \"uniform4_decode_ms\": 42.46,\n      \"uniform4_throughput\": 23.6,\n      \"mckp_prefill_ms\": 57.03,\n      \"mckp_decode_ms\": 46.09,\n      \"mckp_throughput\": 21.8,\n      \"mckp_solver_time_sec\": 0.005,\n      \"memory_compression_4x\": true,\n      \"mckp_overhead_vs_uniform_pct\": 8.5,\n      \"mckp_overhead_vs_bf16_pct\": 36.4\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table: Runtime Benchmark (Qwen2.5-7B, seq_len=2048)\",\n        \"rows\": [\n          {\n            \"method\": \"BF16 (no quantization)\",\n            \"prefill_ms\": 45.86,\n            \"decode_ms\": 33.78,\n            \"throughput\": 29.6,\n            \"memory_MB\": 21\n          },\n          {\n            \"method\": \"Uniform 4-bit\",\n            \"prefill_ms\": 54.25,\n            \"decode_ms\": 42.46,\n            \"throughput\": 23.6,\n            \"memory_MB\": 5.25\n          },\n          {\n            \"method\": \"Constrained MCKP\",\n            \"prefill_ms\": 57.03,\n            \"decode_ms\": 46.09,\n            \"throughput\": 21.8,\n            \"memory_MB\": 5.25\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Median 档中这是 second major objection source。Runtime overhead 与  \\\"practical implications\\\" claim 冲突。Paper 需要 reframe：\\\"memory-bound  scenarios (long context, large batch) where 4× memory reduction enables  deployment that bf16 cannot.\\\" 8K context 实验（qwen7b_8k_context_eval:  uniform 77.75 vs MCKP 8.59）是 strongest counterargument——at long context,  memory savings dominate and quality gap amplifies dramatically。\\n\\n令人意外的 negative finding：mixed-precision MCKP 比 uniform 4-bit 更慢 （throughput 21.8 vs 23.6 tok/s, -7.6%），甚至比 bf16 baseline 更慢 （21.8 vs 29.6 tok/s, -26.4%）。原因是 mixed-precision 需要 per-head 不同 的 dequantization kernel，当前实现缺少 fused kernel optimization。 Median reviewer 反应强烈 negative：\\\"the method provides 29% PPL improvement  on Qwen but costs 8% throughput — practitioners would need to decide if PPL  improvement justifies speed regression. On 7/8 architectures where there's no  PPL benefit, the speed cost is pure overhead.\\\" 这成为 major objection 之一（A6  范畴）。MCKP solver 本身只需 0.005s（negligible），所以 overhead 完全来自 inference-time mixed-precision dequantization。需要在 paper 中承认 \\\"current  implementation uses naive per-head dequantization; a fused kernel could eliminate  the overhead\\\" 并标注为 engineering limitation, not fundamental。但 reviewer 会 counter：\\\"without the optimized kernel, the practical benefit claim is weakened.\\\"\\n\"\n  }\n]",
      "numLines": 725,
      "startLine": 1,
      "totalLines": 725
    }
  },
  "sourceToolAssistantUUID": "6e5aa048-f8e7-4910-aa04-eb5527a54116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "3405a85b-9e28-46a6-afe5-cd44efbe7d57",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Tool result

_source line 13 · 2026-05-16T02:37:22.370Z_

<details><summary>↩ Tool result · `toolu_01HLq16YamsYpowTZ5FjasR3`</summary>

```text
1	# Paper Framing — ratekv
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR submission)
5	- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
6	- Track: Efficient Methods for NLP
7	
8	## bf16 Consistency Resolution (2026-05-14)
9	
10	**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。
11	
12	**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。
13	
14	| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |
15	|------|---------------------|----------------------|-----------|
16	| Baseline | **9.8106** | 8.819 | 9.81 |
17	| Uniform 4-bit | **15.4454** | — | 15.45 |
18	| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |
19	| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |
20	
21	## Core Insight
22	
23	Per-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption "non-uniform is always better than uniform" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.
24	
25	## Core Claims (3 条)
26	
27	1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.
28	
29	2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.
30	
31	3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, "spread" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says "no" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.
32	
33	## Story Spine
34	
35	- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.
36	
37	- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.
38	
39	- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.
40	
41	- **Headline result template**: "We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value."
42	
43	## "When Does Non-Uniform Allocation Help?" — Analysis Chapter
44	
45	Five case studies representing the full spectrum of heterogeneity:
46	
47	| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |
48	|------|-------|-----|--------------|------------------------------|---------------|
49	| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; "spread" pattern (L0 cluster, 4 heads, 26× dominance) |
50	| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; "spike" pattern (L4H3 single outlier, 64% of total delta) |
51	| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |
52	| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |
53	| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |
54	
55	**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.
56	
57	**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).
58	
59	**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.
60	
61	## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)
62	
63	| Method | PPL | Bit Distribution | Budget |
64	|--------|-----|-------------------|--------|
65	| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |
66	| MCKP unconstrained | 36.92 | — | 0.25 |
67	| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
68	| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |
69	| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |
70	
71	Key takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.
72	
73	## Cross-Architecture Evidence Summary
74	
75	| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |
76	|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|
77	| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |
78	| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |
79	| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |
80	| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |
81	| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |
82	
83	**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:
84	- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding
85	- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta
86	- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)
87	- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads
88	
89	**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):
90	
91	Three-tier labeling (NOT binary catastrophe/benign):
92	- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding
93	- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions
94	- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)
95	
96	Reviewer-suggested paragraph for paper (1 段, 3-4 句):
97	"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape."
98	
99	This **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.
100	
101	⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.
102	
103	**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.
104	
105	**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.
106	
107	### Mistral k Ablation (256 KV heads, budget=0.25)
108	
109	PPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).
110	
111	| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |
112	|---|-----|-------|-------|-------|--------|-----|
113	| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |
114	| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |
115	| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |
116	| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |
117	| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |
118	| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |
119	
120	Contrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.
121	
122	### Llama k Ablation (256 KV heads, budget=0.25)
123	
124	All k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).
125	
126	### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)
127	
128	**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅
129	
130	| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |
131	|------|---------------|------------|---|---------------|
132	| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |
133	| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |
134	| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |
135	| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |
136	| **Avg recovery** | — | — | **72.8%** | — |
137	
138	**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)
139	
140	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
141	|------|---------------|------------|---|
142	| arc_easy | 0.7946 | 0.7854 | -0.92pp |
143	| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |
144	| hellaswag | 0.5857 | 0.5797 | -0.60pp |
145	| piqa | 0.7927 | 0.7894 | -0.33pp |
146	| winogrande | 0.7174 | 0.7301 | +1.27pp |
147	| **Average** | **0.6822** | **0.6745** | **-0.77pp** |
148	
149	**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)
150	
151	| Task | Uniform 4-bit | MCKP (k=8) | Δ |
152	|------|---------------|------------|---|
153	| arc_easy | 0.8173 | 0.8039 | -1.34pp |
154	| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |
155	| hellaswag | 0.6026 | 0.6012 | -0.14pp |
156	| piqa | 0.7867 | 0.7802 | -0.65pp |
157	| winogrande | 0.7253 | 0.7238 | -0.15pp |
158	| **Average** | **0.6915** | **0.6816** | **-0.99pp** |
159	
160	**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)
161	
162	| Task | Uniform 4-bit | MCKP (k=4) | Δ |
163	|------|---------------|------------|---|
164	| arc_easy | — | — | — |
165	| arc_challenge | — | — | — |
166	| hellaswag | — | — | — |
167	| piqa | — | — | — |
168	| winogrande | — | — | — |
169	| **Average** | **0.6894** | **0.6846** | **-0.48pp** |
170	
171	**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)
172	
173	| Task | Uniform 4-bit | MCKP | Δ |
174	|------|---------------|------|---|
175	| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |
176	
177	**Downstream summary (Reviewer-verified framing)**:
178	- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**
179	- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)
180	- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)
181	- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise
182	- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)
183	- **Paper must**: (a) report full per-task tables, not just averages, (b) use "shows minor degradation" NOT "preserves accuracy" — the latter has spin, (c) note arc_challenge as worst-case explicitly
184	- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance
185	- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论："ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate."
186	- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞："Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge)."
187	
188	## Allocation Baseline Evidence (plan_015, mckp_reeval)
189	
190	All numbers from unified bf16 eval pipeline, budget=0.25.
191	
192	| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |
193	|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|
194	| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |
195	| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |
196	| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |
197	
198	**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.
199	
200	**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.
201	
202	## Differentiation from RateQuant
203	
204	| Aspect | RateQuant | Ours |
205	|--------|-----------|------|
206	| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |
207	| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |
208	| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |
209	| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |
210	| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |
211	| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |
212	| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |
213	
214	## Venue Fit Risks
215	
216	- **"The constraint is just a heuristic, not a real contribution"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.
217	- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.
218	- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive "higher GQA = more benefit" hypothesis and shows our diagnostic is needed.
219	- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The "spike vs spread" analysis explains WHY same-GQA models differ.
220	- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim "significant correlation" — use "consistent pattern across 8 architectures" or "8/8 correctly classified by the 0.50 threshold."
221	- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.
222	
223	## Anticipated Reviewer Concerns
224	
225	1. **"The cardinality constraint is trivial — just cap the extreme allocations"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.
226	2. **"This is just RateQuant with a constraint added"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.
227	3. **"The method only works on Qwen — isn't this a Qwen paper?"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.
228	4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.
229	5. **"n=3/4/5 models is not enough for the heterogeneity claim"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.
230	6. **"RateQuant does K/V asymmetric allocation, do you?"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.
231	7. **"Where are the downstream task results?"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use "shows minor degradation" not "preserves accuracy".
232	8. **"The profiler distortion=0.0 on Mistral suggests the profiling method is broken"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.
233	9. **"If solver doesn't matter, why present MCKP at all?"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.
234	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3592ee1-9e36-448f-906e-8ff708a0bd83",
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "20ef5691-ae61-422a-a839-9339559f1734",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper_framing.md",
      "content": "# Paper Framing — ratekv\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)\n- Track: Efficient Methods for NLP\n\n## bf16 Consistency Resolution (2026-05-14)\n\n**已解决**：qwen_bf16_reeval 确认 bf16 ≈ fp16（baseline delta=0.0006, uniform delta=0.005）。compounding_sweep bf16 rerun 不需要。\n\n**eval pipeline 一致性**：exp_e 使用了不同的 eval 参数（baseline=8.82, MCKP=9.57），与主 pipeline（baseline=9.81）不一致。hires_mckp_reeval 用统一 pipeline 重测：MCKP hires bf16=10.9131。**论文使用统一 pipeline 数字**。\n\n| 指标 | 统一 pipeline (bf16) | exp_e pipeline (bf16) | fp16 (旧) |\n|------|---------------------|----------------------|-----------|\n| Baseline | **9.8106** | 8.819 | 9.81 |\n| Uniform 4-bit | **15.4454** | — | 15.45 |\n| MCKP hires (max_2bit=8) | **10.9131** | 9.569 | — |\n| MCKP lowres (max_2bit=8) | ~11.23 | 11.345 | 11.23 |\n\n## Core Insight\n\nPer-head KV cache quantization on hardware-aligned bit-widths {2,4,8,16} has an unreported universal failure mode: 2-bit quantization distortions compound non-additively through the residual stream, causing ALL tested unconstrained solvers (greedy, MCKP) to systematically over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 architectures (1.07×–3.31× baseline). A cardinality constraint (≤k heads at 2-bit) universally prevents this over-allocation, and furthermore reduces the feasible set to where solver choice becomes irrelevant (greedy = MCKP, Δ=0.0000). Under moderate compression (4×), only 1/8 architectures benefits from non-uniform allocation over uniform 4-bit — providing the first empirical evidence that the implicit assumption \"non-uniform is always better than uniform\" is wrong in KV cache quantization. The core contribution is the compounding effect discovery + universal constraint fix, not the allocation algorithm.\n\n## Core Claims (3 条)\n\n1. **2-bit compounding is a universal failure mode for unconstrained per-head allocation**: On hardware-aligned non-consecutive bit-widths {2,4,8,16}, per-head independent profiling distortions compound non-additively when multiple heads are simultaneously assigned 2-bit quantization. This causes ALL tested unconstrained solvers to over-allocate 2-bit heads and underperform uniform 4-bit across 8/8 diverse architectures (Qwen 3.31×, Gemma-2 1.47×, Yi 1.08×, Llama 1.07×, Mistral 1.08×, Pythia, Qwen-14B, Phi-3-medium). Quantitative evidence of non-additivity: per-head profiling predicts joint PPL ≈11 but actual joint 2-bit PPL is 32–37 (3× prediction error). This is the first systematic characterization of compounding effects in per-head KV cache quantization. Long-context amplifies the failure: at 8K tokens, uniform 4-bit degrades 11.15× baseline while constrained MCKP degrades only 1.23× — a 9× gap in degradation rate.\n\n2. **A cardinality constraint is the universal fix — and makes solver choice irrelevant**: A simple cardinality constraint (max_2bit ≤ k) is sufficient to prevent compounding across ALL tested architectures. Three universally beneficial properties: (a) prevents catastrophic over-allocation on sensitive architectures (Qwen: 32.45 → 10.91), (b) prevents moderate over-allocation on flat architectures (Gemma-2: 8.85 → 6.17, reducing 2-bit heads from 106 to 8), (c) reduces the feasible set to where solver choice is irrelevant — constrained greedy and constrained MCKP produce IDENTICAL bit allocations and PPL (Δ=0.0000). The constraint is parameterizable via small-scale compounding test (k≤8 universally safe: <2.5% degradation across all architectures). Practical implication: practitioners need only add one integer parameter to existing pipelines.\n\n3. **Non-uniform allocation benefit is rare — most models should use uniform 4-bit**: Under moderate compression (4×), only 1/8 tested architectures (Qwen2.5-7B, \"spread\" sensitivity pattern) benefits from non-uniform allocation (+27.3% PPL, +1.9pp downstream avg). The remaining 7/8 show no benefit or minor degradation (<1pp avg downstream). A 2-metric empirical diagnostic (concentration ≳0.50 AND t₁/t₅ ≲0.70) correctly classifies all 9 tested models (9/9 accuracy), providing practitioners a simple check: if the diagnostic says \"no\" — skip profiling and use uniform 4-bit with zero quality loss. This is the first systematic study of *when* non-uniform KV cache quantization is beneficial, correcting the implicit assumption that it always helps.\n\n## Story Spine\n\n- **Problem**: Per-head mixed-precision KV cache quantization promises better quality-compression tradeoffs than uniform bit-width. But on hardware-aligned non-consecutive bit-widths {2,4,8,16}, we discover that existing allocation algorithms (greedy, MCKP) systematically FAIL — producing worse results than naive uniform 4-bit across ALL tested architectures. The failure mode is unreported: 2-bit quantization distortions compound non-additively, and solvers consistently over-allocate 2-bit heads. Meanwhile, the field implicitly assumes non-uniform allocation always helps, but no systematic study has tested this across architectures.\n\n- **Existing approaches & gaps**: RateQuant provides R-D optimal per-head allocation via continuous closed-form and discrete greedy (optimal on consecutive integers {2,...,6}). KIVI and ARKV apply uniform or heuristic mixed-precision. However, on hardware-aligned {2,4,8,16}: (a) RateQuant's greedy produces PPL 32.45 vs optimal ~10.91 — polymatroid optimality breaks, (b) unconstrained MCKP fares even worse (PPL 36.92) due to compounding, (c) NO prior work addresses *when* non-uniform allocation is actually beneficial vs when uniform suffices.\n\n- **Our framing**: We present three contributions: (1) the first characterization of 2-bit compounding effects in per-head KV cache quantization — showing that profiling non-additivity causes ALL unconstrained solvers to fail on {2,4,8,16} across 8/8 architectures; (2) a simple universal fix: a cardinality constraint (≤k heads at 2-bit) that prevents compounding, makes solver choice irrelevant (greedy=MCKP, Δ=0.0000), and is safely parameterizable (k≤8 universally safe); (3) the first systematic study of *when* non-uniform allocation helps — answer: rarely (1/8 architectures at moderate compression), with a 2-metric diagnostic (9/9 correct) that tells practitioners whether to invest in profiling or just use uniform 4-bit.\n\n- **Headline result template**: \"We show that per-head KV cache quantization on hardware-aligned bit-widths has a universal failure mode: 2-bit distortions compound non-additively, causing ALL unconstrained solvers to underperform uniform 4-bit across 8 architectures. A cardinality constraint (≤k heads at 2-bit) universally fixes this, making solver choice irrelevant (greedy=MCKP, Δ=0.0000). Surprisingly, under moderate compression, only 1/8 architectures benefits from non-uniform allocation at all — most models should simply use uniform 4-bit. A 2-metric diagnostic (9/9 accuracy) provides practitioners a simple check to determine when profiling is worthwhile. At long context (8K tokens), the constraint reduces degradation from 11.15× to 1.23× baseline, demonstrating critical deployment value.\"\n\n## \"When Does Non-Uniform Allocation Help?\" — Analysis Chapter\n\nFive case studies representing the full spectrum of heterogeneity:\n\n| Case | Model | GQA | Top-5% Conc. | Constrained vs Uniform (4×) | Role in Paper |\n|------|-------|-----|--------------|------------------------------|---------------|\n| **Strong positive** | Qwen2.5-7B | 7:1 | 0.59-0.66 | **+27.3% (11.23 vs 15.45)** | Primary showcase; \"spread\" pattern (L0 cluster, 4 heads, 26× dominance) |\n| **GQA counterexample** | Yi-1.5-9B | 8:1 | 0.71 (hires) | ≈0% (7.22 vs 7.22) | Highest GQA but no benefit; \"spike\" pattern (L4H3 single outlier, 64% of total delta) |\n| **Marginal** | Llama-3.1-8B | 4:1 | 0.57 (hires) | +0.2% (8.45 vs 8.47) | Boundary condition; constraint never binds (natural k=2) |\n| **Negative** | Mistral-7B-v0.3 | 4:1 | 0.22 (hires) | -0.4% (7.16 vs 7.13) | Profiler zero-signal; monotonic k-PPL curve |\n| **Strongest negative** | Gemma-2-9B | 2:1 | 0.23 (hires) | -0.3% (9.05 vs 9.03) | Low-end anchor; most uniform sensitivity (CV=1.28, t₁/t₅=0.38) |\n\n**Spike vs Spread insight**: Yi-1.5 vs Qwen illustrates why GQA ratio alone is insufficient. Both have high GQA (8:1 vs 7:1), but Qwen's L0 *cluster* of sensitive heads creates optimization opportunities for MCKP, while Yi-1.5's single extreme outlier (L4H3) cannot be exploited — the solver assigns 8-bit to that one head but has no other heads to differentiate. Distribution shape matters more than the existence of outliers.\n\n**Compression amplifies benefit**: Even on low-heterogeneity Llama, aggressive 5.3× compression yields constrained PPL=57.60 vs uniform 2-bit=2643.77 (45× better).\n\n**Joint diagnostic** (n=8, 8/8 correct): concentration ≳0.50 AND t₁/t₅ ≲0.70 → non-uniform allocation recommended (spread pattern). Either condition violated → uniform suffices at moderate compression; non-uniform still valuable at aggressive compression. Yi-1.5 (concentration 0.71 but t₁/t₅=0.90 — spike), CodeLlama (0.80, t₁/t₅=0.81 — spike), and Qwen (0.61, t₁/t₅=0.57 — spread) illustrate why concentration alone is insufficient.\n\n## Solver Equivalence Evidence (plan_016, CONFIRMED ✅)\n\n| Method | PPL | Bit Distribution | Budget |\n|--------|-----|-------------------|--------|\n| Greedy unconstrained | 32.45 | {2:68, 4:30, 8:4, 16:10} | 0.25 |\n| MCKP unconstrained | 36.92 | — | 0.25 |\n| **Greedy + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| **MCKP + max_2bit=8** | **11.2312** | **{8:4, 4:100, 2:8}** | **0.25** |\n| Uniform 4-bit | 15.4454 | all 4-bit | 0.25 |\n\nKey takeaway: The constraint is the primary intervention — without it, both solvers fail; with it, solver choice is irrelevant (Δ=0.0000). This powerfully demonstrates the constraint is THE contribution.\n\n## Cross-Architecture Evidence Summary\n\n| Model | GQA | KV Heads | Top-5% Conc. | Unconstrained ×baseline (W2 v2) | Constrained vs Uniform (4×) | Distribution Shape | Conclusion |\n|-------|-----|----------|--------------|--------------------------------|------------------------------|-------------------|------------|\n| Qwen2.5-7B | 7:1 | 112 | **0.61** | **3.31× (32.45)** ☠️ | **+27.3% (11.23 vs 15.45)** | Spread (L0 cluster, 4 heads) | ✅ Strong benefit |\n| Yi-1.5-9B | 8:1 | 192 | **0.71** (hires) | 1.08× (7.56) | **≈0% (7.22 vs 7.22)** | Spike (L4H3 single outlier) | ❌ GQA counterexample |\n| Llama-3.1-8B | 4:1 | 256 | **0.57** (hires) | 1.07× (8.63) | **+0.2% (8.45 vs 8.47)** | Spike (t₁/t₅≈0.85, single dominant L2H5) | ≈ Marginal |\n| Mistral-7B-v0.3 | 4:1 | 256 | **0.22** (hires) | 1.08× (7.57) | **-0.4% (7.16 vs 7.13)** | Flat (profiler zero-signal) | ❌ Negative |\n| Gemma-2-9B | 2:1 | 336 | **0.23** (hires) | 1.47× (8.85) | **-0.3% (9.05 vs 9.03)** | Flat (CV=1.28, t₁/t₅=0.38) | ❌ Strongest negative |\n\n**Unconstrained pattern** (W2 v2, all WikiText-2 test eval, gradient narrative): Unconstrained degradation follows a **concentration-dependent gradient**, not a binary catastrophe/benign split:\n- **Spread** (Qwen, conc=0.61): **3.31×** catastrophic — L0 cluster creates massive compounding\n- **Flat-high-2bit** (Gemma-2, conc=0.23): **1.47×** moderate — solver assigns 106/336=31.5% heads to 2-bit because distortions are indistinguishable (CV=1.28), cumulative effect significant despite small per-head delta\n- **Spike/Flat-low-2bit** (Yi 1.08×, Llama 1.07×, Mistral 1.08×): mild — solver selects few 2-bit heads (Yi 11.5%, Llama 4.7%, Mistral 16.4%)\n- In ALL cases unconstrained ≤ uniform 4-bit — solver consistently over-allocates 2-bit heads\n\n**Gemma-2 1.47× must be discussed in paper** (Reviewer mandate, severity: warning):\n\nThree-tier labeling (NOT binary catastrophe/benign):\n- **Catastrophic** (3.31×): Spread model (Qwen) — L0 cluster compounding\n- **Moderate** (1.47×): Flat-high-2bit (Gemma-2) — solver over-allocation from indistinguishable distortions\n- **Mild** (1.07-1.08×): Spike/Flat-low-2bit (Yi, Llama, Mistral)\n\nReviewer-suggested paragraph for paper (1 段, 3-4 句):\n\"Gemma-2-9B exhibits a moderate 1.47× degradation under unconstrained allocation, higher than the 1.07–1.08× observed in other non-Spread models. This stems from its flat sensitivity distribution (concentration 0.23, CV 1.28): the solver cannot meaningfully differentiate heads, leading to 31.5% of heads assigned to 2-bit (vs 4.7–16.4% in other models). While not catastrophic, this over-allocation still motivates the cardinality constraint even on flat-distribution architectures. The constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3% of uniform — confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\"\n\nThis **strengthens** the paper: (1) honesty → credibility, (2) constraint has universal value (not just Spread), (3) explains solver degradation mechanism under low signal → added insight depth.\n\n⚠️ **Data file note**: `artifacts/w2_unconstrained_v2_results.json` still has old Gemma-2 BOS bug data (baseline=711.6). Fix in `artifacts/w2_gemma2_bos_fix_results.json`. Agent tasked to merge.\n\n**Key pattern**: Constrained allocation benefit depends on the joint condition (concentration ≳0.50 AND t₁/t₅ ≲0.70, 5/5 correct), NOT GQA ratio or concentration alone. Yi-1.5 (GQA 8:1, concentration 0.71 — highest — yet no benefit) vs Qwen (GQA 7:1, concentration 0.61, +27.3%) demonstrates that neither GQA nor concentration alone is a reliable proxy. The critical factor is sensitivity *distribution shape*: spread (multiple heads with cross-bitwidth gradients) enables MCKP, while spike (single outlier) or flat (uniform sensitivity) does not.\n\n**Aggressive compression** (Llama): At 5.3× compression, constrained PPL=57.60 vs uniform 2-bit=2643.77 — prevents catastrophic collapse even on low-heterogeneity architectures.\n\n### Mistral k Ablation (256 KV heads, budget=0.25)\n\nPPL monotonically increases with k — every additional 2-bit head hurts. Even best k=4 (PPL 7.1648) is worse than uniform (7.131).\n\n| k | PPL | 2-bit | 4-bit | 8-bit | 16-bit | mem |\n|---|-----|-------|-------|-------|--------|-----|\n| 4 | **7.1648** | 4 | 252 | 0 | 0 | 0.248 |\n| 8 | 7.1997 | 8 | 247 | 0 | 1 | 0.249 |\n| 12 | 7.2448 | 12 | 242 | 0 | 2 | 0.250 |\n| 16 | 7.3106 | 16 | 238 | 0 | 2 | 0.248 |\n| 18 | 7.3231 | 18 | 235 | 0 | 3 | 0.250 |\n| uniform 4-bit | 7.131 | 0 | 256 | 0 | 0 | 0.250 |\n\nContrast with Qwen (U-shaped, optimal k=8) and Llama (flat, natural k=2). Mistral's monotonic pattern confirms profiler zero-signal: no head benefits from 2-bit downgrade.\n\n### Llama k Ablation (256 KV heads, budget=0.25)\n\nAll k values produce identical PPL=8.4498. MCKP naturally selects only 2 heads for 2-bit — constraint never binds. Marginal +0.2% over uniform (8.4498 vs 8.469).\n\n### Downstream Eval — Cross-Architecture (W3, 0-shot, 5 tasks)\n\n**Qwen2.5-7B (Spread) — MCKP benefits translate to downstream** ✅\n\n| Task | Uniform 4-bit | MCKP hires | Δ | BF16 Baseline |\n|------|---------------|------------|---|---------------|\n| ARC-C | 0.4812 | 0.5137 | **+3.16pp** | 0.5290 |\n| HellaSwag | 0.7284 | 0.7684 | **+4.00pp** | 0.7833 |\n| PIQA | 0.7661 | 0.7786 | **+1.25pp** | 0.7932 |\n| WinoGrande | 0.6622 | 0.6819 | **+1.97pp** | 0.6898 |\n| **Avg recovery** | — | — | **72.8%** | — |\n\n**Yi-1.5-9B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.7946 | 0.7854 | -0.92pp |\n| arc_challenge | 0.5205 | 0.4881 | **-3.24pp** |\n| hellaswag | 0.5857 | 0.5797 | -0.60pp |\n| piqa | 0.7927 | 0.7894 | -0.33pp |\n| winogrande | 0.7174 | 0.7301 | +1.27pp |\n| **Average** | **0.6822** | **0.6745** | **-0.77pp** |\n\n**Llama-3.1-8B (Spike) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=8) | Δ |\n|------|---------------|------------|---|\n| arc_easy | 0.8173 | 0.8039 | -1.34pp |\n| arc_challenge | 0.5256 | 0.4991 | **-2.65pp** |\n| hellaswag | 0.6026 | 0.6012 | -0.14pp |\n| piqa | 0.7867 | 0.7802 | -0.65pp |\n| winogrande | 0.7253 | 0.7238 | -0.15pp |\n| **Average** | **0.6915** | **0.6816** | **-0.99pp** |\n\n**Mistral-7B-v0.3 (Flat) — No MCKP benefit, consistent with PPL** (W3)\n\n| Task | Uniform 4-bit | MCKP (k=4) | Δ |\n|------|---------------|------------|---|\n| arc_easy | — | — | — |\n| arc_challenge | — | — | — |\n| hellaswag | — | — | — |\n| piqa | — | — | — |\n| winogrande | — | — | — |\n| **Average** | **0.6894** | **0.6846** | **-0.48pp** |\n\n**Gemma-2-9B (Flat) — Negligible MCKP effect, noise range** (W3)\n\n| Task | Uniform 4-bit | MCKP | Δ |\n|------|---------------|------|---|\n| **Average** | **0.7251** | **0.7265** | **+0.14pp** (noise) |\n\n**Downstream summary (Reviewer-verified framing)**:\n- Diagnostic correctly predicts both PPL and downstream outcomes across **all 5 tested models**\n- Spread (Qwen): consistent downstream gains (+1.25 to +4.00pp)\n- Non-Spread (4 models): MCKP shows **minor systematic degradation** vs uniform (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp noise)\n- **Llama signal**: 0/5 tasks where MCKP ≥ uniform — degradation is systematic, not task-specific noise\n- arc_challenge shows largest per-task effect (Yi -3.24pp, Llama -2.65pp)\n- **Paper must**: (a) report full per-task tables, not just averages, (b) use \"shows minor degradation\" NOT \"preserves accuracy\" — the latter has spin, (c) note arc_challenge as worst-case explicitly\n- **Limitation**: no multi-seed CI for downstream — 0-shot arc_challenge -3.24pp could be questioned for significance\n- **arc_challenge 系统性信号** (Reviewer 观察): arc_challenge 退化跨模型一致（Yi -3.24pp, Llama -2.65pp, Mistral -1.19pp, Gemma-2 -0.17pp），不是随机噪声。论文应主动讨论：\"ARC-Challenge shows the largest per-task sensitivity to allocation strategy, consistent with its reliance on multi-step reasoning where subtle KV cache errors accumulate.\"\n- **呈现方式**: 主表放完整 per-task 数据，文字用均值+range 概括。建议措辞：\"Across four non-Spread architectures, constrained MCKP shows minor average degradation vs uniform 4-bit (Yi -0.77pp, Llama -0.99pp, Mistral -0.48pp, Gemma-2 +0.14pp). Per-task variation ranges from +1.27pp (Yi, WinoGrande) to -3.24pp (Yi, ARC-Challenge).\"\n\n## Allocation Baseline Evidence (plan_015, mckp_reeval)\n\nAll numbers from unified bf16 eval pipeline, budget=0.25.\n\n| Model | Baseline | Uniform 4-bit | MCKP | L0-random (mean±std) | L0-random (median) | Naive Positional | MCKP improvement |\n|-------|----------|---------------|------|----------------------|---------------------|------------------|------------------|\n| Qwen2.5-7B (k=8) | 9.8106 | 15.4454 | 10.9131 | 11.691±0.422 | **11.515** | 12.230 | 27.3% vs uniform (standard); 29.4% (hires, §5.4) |\n| Llama-3.1-8B (k=2) | 8.0918 | 8.469 | 8.4498 | 10.479±1.033 | **10.038** | 9.941 | +0.2% vs uniform |\n| Mistral-7B-v0.3 (k=4) | 7.035 | 7.131 | 7.1648 | 7.560±0.087 | **7.586** | 7.481 | -0.4% vs uniform |\n\n**Outlier note**: seed_4 inflates mean on Qwen (12.51) and Llama (12.44). Median is more robust: Qwen median 11.515 vs mean 11.691 (−0.176); Llama median 10.038 vs mean 10.479 (−0.441). Mistral has no outlier (median ≈ mean). Paper should report both mean±std and median.\n\n**MCKP vs L0-random (median)**: Qwen 10.91 vs 11.52 (−5.2%); Llama 8.45 vs 10.04 (−15.8%); Mistral 7.16 vs 7.59 (−5.7%). MCKP consistently outperforms random L0-constrained allocation across all architectures.\n\n## Differentiation from RateQuant\n\n| Aspect | RateQuant | Ours |\n|--------|-----------|------|\n| Bit-width selection | Greedy on consecutive integers {2,...,6} (Prop. 6 optimal) + continuous closed-form (Thm. 2) | Cardinality-constrained allocation on hardware-aligned {2,4,8,16}-bit |\n| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization for non-additivity |\n| Compounding effects | Acknowledged (Appendix M) but unaddressed | **Core contribution**: cardinality constraint prevents compounding; first quantitative evidence |\n| Action space | Consecutive integers (polymatroid → greedy optimal) | Non-consecutive hardware-aligned (polymatroid breaks → constraint needed, solver doesn't matter) |\n| Solver requirement | Greedy (provably optimal in their setting) | **Any solver** — constrained greedy = constrained MCKP (Δ=0.0000 PPL) |\n| K/V allocation | Asymmetric K/V budget (e.g. K=2.85, V=2.15) | MCKP/greedy treats K/V heads as independent items (natural extension) |\n| **Applicability analysis** | **Not addressed — assumes non-uniform always helps** | **Systematic study of when non-uniform allocation is beneficial (new contribution)** |\n\n## Venue Fit Risks\n\n- **\"The constraint is just a heuristic, not a real contribution\"**: Strongest reviewer attack under new framing. Defense: (a) principled motivation from compounding effect non-additivity with first quantitative evidence, (b) constraint parameterization via systematic compounding test, (c) the finding that constraint alone makes solver choice irrelevant is a surprising and practically useful result — practitioners need only add one parameter to existing pipelines.\n- **Incrementality over RateQuant**: Defense: (a) RateQuant's greedy is suboptimal unconstrained on {2,4,8,16} (PPL 32.45), (b) our constraint fixes RateQuant's greedy to match MCKP — we're improving their method, not replacing it, (c) applicability analysis is entirely new.\n- **Method only strong on one architecture (Qwen)**: 5 models tested, only Qwen shows clear benefit. Mitigate: (a) analysis contribution framing — characterizing boundary conditions is more useful than universal positive, (b) honest negative/marginal results (Yi-1.5, Gemma-2, Mistral, Llama) strengthen credibility, (c) unlike prior work that assumes non-uniform always helps, we provide the first systematic study of *when it fails*, (d) Yi-1.5 (GQA 8:1, FAIL) is particularly powerful — it disproves the naive \"higher GQA = more benefit\" hypothesis and shows our diagnostic is needed.\n- **GQA ratio is not a reliable proxy**: Yi-1.5 (GQA 8:1) directly contradicts a GQA-based prediction. Do NOT present GQA ratio as a predictor — present it as one contributing factor. The reliable predictor is Top-5% concentration (0.50 threshold, 8/8 correct). The \"spike vs spread\" analysis explains WHY same-GQA models differ.\n- **Statistical power**: n=8 models is directional evidence, not statistical claim. Do NOT claim \"significant correlation\" — use \"consistent pattern across 8 architectures\" or \"8/8 correctly classified by the 0.50 threshold.\"\n- **No eviction arm**: Mention as negative finding; framework extends naturally to eviction.\n\n## Anticipated Reviewer Concerns\n\n1. **\"The cardinality constraint is trivial — just cap the extreme allocations\"** → (a) Trivial in retrospect, but without it both greedy (PPL 32.45) and MCKP (PPL 36.92) fail catastrophically — the failure mode is non-obvious, (b) principled motivation from compounding effect characterization (plan_004), (c) optimal k selection via systematic small-scale test, (d) the finding that this single intervention eliminates solver complexity is surprising and practically valuable.\n2. **\"This is just RateQuant with a constraint added\"** → (a) We agree — and that's the point: RateQuant's greedy + our constraint achieves identical results to MCKP + constraint, (b) the constraint addresses a real gap: compounding effects on {2,4,8,16} that RateQuant acknowledges but doesn't solve, (c) applicability analysis is new.\n3. **\"The method only works on Qwen — isn't this a Qwen paper?\"** → We systematically test 4-5 architectures spanning GQA 2:1 to 8:1 and honestly report negative results (Gemma-2, Mistral). The analysis contribution — characterizing *boundary conditions* of non-uniform quantization — generalizes beyond any single model and is more useful than a universally positive but misleading claim.\n4. **\"How does this work at different compression ratios?\"** → Budget sweep across 2×, 4×, 8× (plan_005). Aggressive compression on Llama shows benefit amplifies even on low-heterogeneity models.\n5. **\"n=3/4/5 models is not enough for the heterogeneity claim\"** → Acknowledged as limitation. We present directional evidence across 4-5 architectures spanning GQA 2:1 to 8:1, with a monotonic trend between GQA ratio, heterogeneity, and MCKP benefit. The Top-5% concentration diagnostic is a testable hypothesis, not a statistical claim.\n6. **\"RateQuant does K/V asymmetric allocation, do you?\"** → Framework naturally treats K and V heads as independent items; plan_014 tests K/V separation.\n7. **\"Where are the downstream task results?\"** → ✅ DONE (plan_012 + W3, all 5 models): Qwen (Spread): +1.25 to +4.00pp across 4 tasks, 72.8% avg recovery. Yi-1.5 (Spike): avg -0.77pp. Llama (Spike): avg -0.99pp (0/5 tasks positive — systematic). Mistral (Flat): avg -0.48pp. Gemma-2 (Flat): avg +0.14pp (noise). **Diagnostic predicts both PPL and downstream correctly across all 5 architectures**. Must report full per-task tables; use \"shows minor degradation\" not \"preserves accuracy\".\n8. **\"The profiler distortion=0.0 on Mistral suggests the profiling method is broken\"** → Profiler correctly reports near-zero sensitivity differences. Some architectures genuinely have homogeneous head sensitivity, making non-uniform allocation futile.\n9. **\"If solver doesn't matter, why present MCKP at all?\"** → (a) MCKP provides the formal framework for the constrained allocation problem — it's the lens through which we analyze the problem even if greedy solves it equally well, (b) presenting both solvers with identical results IS the evidence that the constraint is what matters, (c) for future extensions (more bit-widths, per-layer budgets), MCKP may regain advantage — we keep it as general framework.\n",
      "numLines": 234,
      "startLine": 1,
      "totalLines": 234
    }
  },
  "sourceToolAssistantUUID": "b3592ee1-9e36-448f-906e-8ff708a0bd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "20ef5691-ae61-422a-a839-9339559f1734",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Assistant

_source line 16 · 2026-05-16T02:37:25.853Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experiment data and paper framing. Let me write a complete LaTeX paper based on this information. Let me first check if the target directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20ef5691-ae61-422a-a839-9339559f1734",
  "isSidechain": false,
  "requestId": "req_011Cb5UFoyHwEpBJ9uSmjotf",
  "type": "assistant",
  "uuid": "2ac13e78-e513-4838-9419-230352ccd96a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No5VPARS1vipRRs4MqABA3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25629,
      "cache_read_input_tokens": 24161,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 24161,
          "cache_creation_input_tokens": 25629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25629
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

_source line 17 · 2026-05-16T02:37:26.383Z_

Now let me check the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ac13e78-e513-4838-9419-230352ccd96a",
  "isSidechain": false,
  "requestId": "req_011Cb5UFoyHwEpBJ9uSmjotf",
  "type": "assistant",
  "uuid": "07daacf3-5cfe-4c3e-8b92-633cdae0bc01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No5VPARS1vipRRs4MqABA3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25629,
      "cache_read_input_tokens": 24161,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 24161,
          "cache_creation_input_tokens": 25629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25629
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

_source line 18 · 2026-05-16T02:37:28.809Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014skbf6Lz52YsLQky8w56dX`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/",
  "description": "List target directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07daacf3-5cfe-4c3e-8b92-633cdae0bc01",
  "isSidechain": false,
  "requestId": "req_011Cb5UFoyHwEpBJ9uSmjotf",
  "type": "assistant",
  "uuid": "5645a8a1-45ed-4f93-8b3c-b97be79278fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No5VPARS1vipRRs4MqABA3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25629,
      "cache_read_input_tokens": 24161,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 24161,
          "cache_creation_input_tokens": 25629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25629
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

_source line 19 · 2026-05-16T02:37:29.807Z_

<details><summary>↩ Tool result · `toolu_014skbf6Lz52YsLQky8w56dX`</summary>

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
  "parentUuid": "5645a8a1-45ed-4f93-8b3c-b97be79278fa",
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "71a14623-fddc-41d6-bb8c-00f0a99b5f81",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "5645a8a1-45ed-4f93-8b3c-b97be79278fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-16T02:37:34.208Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a14623-fddc-41d6-bb8c-00f0a99b5f81",
  "isSidechain": false,
  "requestId": "req_011Cb5UGMvuHAfRL4jAmywBG",
  "type": "assistant",
  "uuid": "efe77b82-b158-4be0-bcd7-468ce86e4d7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuFuegjcxNxHb48SNco6Mm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 49790,
      "output_tokens": 11443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11443,
          "cache_read_input_tokens": 49790,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 21 · 2026-05-16T02:41:06.707Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LPpfzcM382YUoKGKK2yVyZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\title{Compounding Failures in Per-Head KV Cache Quantization:\\\\An Empirical Analysis of When Non-Uniform Allocation Helps}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression tradeoffs than uniform bit-width assignment.\nWe show that on hardware-aligned non-consecutive bit-widths $\\{2,4,8,16\\}$, this promise breaks:\n2-bit quantization distortions compound non-additively through the residual stream, causing \\emph{all} tested unconstrained solvers (greedy, MCKP) to over-allocate 2-bit heads and underperform uniform 4-bit across 8 diverse architectures (degradation $1.07\\times$--$3.31\\times$ baseline).\nA simple cardinality constraint ($\\le k$ heads at 2-bit) prevents compounding across all tested architectures, and reduces the feasible set to where solver choice is irrelevant: constrained greedy and constrained MCKP produce identical bit allocations ($\\Delta=0.0000$ PPL).\nSurprisingly, under moderate (4$\\times$) compression, only 1 of 8 tested architectures benefits from non-uniform allocation; the remaining 7 show no benefit or minor degradation.\nWe propose a 2-metric empirical diagnostic (top-5\\% concentration $\\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$) that correctly classifies all 9 tested models, giving practitioners a simple check: if the diagnostic says ``no,'' skip profiling and use uniform 4-bit with zero quality loss.\nAt aggressive compression (8$\\times$), the constraint reduces degradation from $45.9\\times$ to $5.9\\times$ baseline on Qwen2.5-7B, demonstrating critical deployment value.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nKV cache memory is a primary bottleneck for long-context LLM serving.\nPer-head mixed-precision quantization---assigning different bit-widths to different attention heads based on their sensitivity---has been proposed as a principled approach to improve the quality--compression tradeoff over uniform quantization~\\cite{hooper2024kvquant,liu2024kivi,dong2024qaq}.\nThe underlying assumption is straightforward: allocate fewer bits to insensitive heads and more bits to sensitive ones.\n\nHowever, modern hardware efficiently supports only non-consecutive bit-widths $\\{2,4,8,16\\}$, creating a large gap between the lowest two options.\nWe discover that this gap introduces a previously unreported failure mode: \\textbf{2-bit quantization distortions compound non-additively} when multiple heads are simultaneously assigned 2-bit precision.\nPer-head profiling predicts a joint PPL of ${\\sim}11$ when assigning many heads to 2-bit, but the actual PPL is 32--37---a $3\\times$ prediction error.\nThis compounding causes all tested unconstrained allocation algorithms to systematically over-allocate 2-bit heads, producing worse results than naive uniform 4-bit across \\emph{all 8 tested architectures} (degradation ranging from $1.07\\times$ to $3.31\\times$ baseline).\n\nThis paper makes three contributions, framed as an empirical analysis:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Compounding effect characterization.} We provide the first quantitative mapping of 2-bit compounding in per-head KV cache quantization, showing superlinear PPL growth after $k \\approx 16$ simultaneous 2-bit heads and exponential growth after $k \\approx 48$ on Qwen2.5-7B (Table~\\ref{tab:compounding_sweep}).\nThe pattern is consistent across 8 architectures spanning GQA ratios 2:1 to 8:1.\n\n\\item \\textbf{Cardinality constraint as universal fix.} A cardinality constraint ($\\le k$ heads at 2-bit) prevents compounding across all tested architectures.\nUnder this constraint, solver choice becomes irrelevant: constrained greedy and constrained MCKP produce \\emph{identical} allocations ($\\Delta = 0.0000$; Table~\\ref{tab:solver_equivalence}).\nThe safe range $k \\le 8$ yields $<2.5\\%$ degradation across all tested architectures.\n\n\\item \\textbf{When does non-uniform allocation help?} Under moderate ($4\\times$) compression, only 1/8 architectures (Qwen2.5-7B, ``spread'' sensitivity pattern) benefits from non-uniform allocation (+27.3\\% PPL improvement, +2.6pp average downstream gain).\nThe remaining 7/8 show no benefit or minor degradation.\nA 2-metric diagnostic (9/9 correct) tells practitioners whether profiling is worthwhile.\n\\end{enumerate}\n\nOur work differs from RateQuant~\\cite{ratequant2024} in three key aspects: (a)~RateQuant operates on consecutive bit-widths $\\{2,\\ldots,6\\}$ where polymatroid structure guarantees greedy optimality; on hardware-aligned $\\{2,4,8,16\\}$ this structure breaks, (b)~RateQuant acknowledges compounding in Appendix~M but does not characterize it or propose a fix---we provide the first quantitative sweep and a universal constraint, (c)~we provide the first systematic study of \\emph{when} non-uniform allocation is actually beneficial versus when uniform suffices.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{KV Cache Quantization.}\nKIVI~\\cite{liu2024kivi} applies uniform per-channel quantization to KV caches with asymmetric K/V treatment.\nKVQuant~\\cite{hooper2024kvquant} introduces per-channel sensitivity-aware quantization with non-uniform codebooks.\nQAQ~\\cite{dong2024qaq} proposes attention-aware quantization with quality-adaptive bit-width selection.\n\n\\paragraph{Mixed-Precision Allocation.}\nRateQuant~\\cite{ratequant2024} formulates per-head bit allocation as a rate--distortion problem, deriving a continuous closed-form solution (Thm.~2) and a discrete greedy algorithm (Prop.~6) that is provably optimal on consecutive integer bit-widths.\nOn non-consecutive hardware-aligned widths $\\{2,4,8,16\\}$, the polymatroid structure underlying this optimality guarantee breaks.\nRateQuant acknowledges compounding effects in Appendix~M but provides no quantitative characterization or mitigation.\nOur work provides the first such characterization and shows that a cardinality constraint both fixes the compounding failure and makes the solver choice irrelevant---constrained greedy matches constrained MCKP exactly.\n\n\\paragraph{Compounding Effects in Quantization.}\nNon-additive error accumulation is well-known in weight quantization~\\cite{nagel2020up}, but its manifestation in per-head KV cache quantization---where the residual stream propagates head-level errors across layers---has not been systematically studied.\nWe provide the first quantitative evidence that per-head independent profiling underestimates joint 2-bit degradation by ${\\sim}3\\times$.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\nGiven an LLM with $H$ KV heads and a set of hardware-aligned bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, per-head mixed-precision allocation assigns a bit-width $b_h \\in \\mathcal{B}$ to each head $h$ subject to a memory budget constraint:\n\\begin{equation}\n\\min_{\\{b_h\\}} \\; \\text{PPL}(\\{b_h\\}) \\quad \\text{s.t.} \\quad \\sum_{h=1}^{H} b_h \\le B\n\\label{eq:allocation}\n\\end{equation}\nwhere $B$ is the total bit budget.\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each head $h$ and candidate bit-width $b \\in \\mathcal{B}$, we measure the \\emph{distortion delta}: the PPL increase when head $h$ alone is quantized to $b$-bit while all other heads remain at 16-bit.\nThis produces a distortion matrix $\\Delta(h, b)$ of size $H \\times |\\mathcal{B}|$.\n\nProfiling uses calibration data from WikiText-2 (train split).\nWe evaluate two resolutions: low-resolution (16 sequences $\\times$ 512 tokens) and high-resolution (64 sequences $\\times$ 2048 tokens).\nHigh-resolution profiling detects sensitivity in 100/112 heads versus 37/112 for low-resolution on Qwen2.5-7B, improving constrained PPL from 11.23 to 10.91 ($-2.8\\%$; Table~\\ref{tab:profiling_resolution}).\n\n\\subsection{MCKP Formulation with Cardinality Constraint}\n\nWe formulate bit-width allocation as a Multiple-Choice Knapsack Problem (MCKP): each head selects exactly one bit-width from $\\mathcal{B}$, with the objective of minimizing total distortion subject to the memory budget.\nCritically, we add a \\textbf{cardinality constraint}:\n\\begin{equation}\n\\sum_{h=1}^{H} \\mathbf{1}[b_h = 2] \\le k\n\\label{eq:constraint}\n\\end{equation}\nlimiting the number of heads assigned to 2-bit quantization.\nThis constraint is motivated by our empirical observation that 2-bit distortions compound non-additively (Section~\\ref{sec:compounding}).\n\nThe constraint parameter $k$ is selected via a small-scale compounding test: sweep $k$ on a validation set and identify the ``safe'' range where PPL growth remains approximately linear.\nAcross all tested architectures, $k \\le 8$ consistently yields $<2.5\\%$ degradation relative to the unconstrained optimal (Table~\\ref{tab:compounding_sweep}).\n\n\\subsection{Applicability Diagnostic}\n\nNot all architectures benefit from non-uniform allocation.\nWe propose a 2-metric diagnostic based on the per-head sensitivity profile:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Top-5\\% concentration} ($c$): the fraction of total distortion delta concentrated in the top 5\\% of heads.\n\\item \\textbf{$t_1/t_5$ ratio}: the ratio of the largest single-head distortion to the sum of the top-5 distortions.\n\\end{itemize}\n\nThe decision rule: if $c \\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$, the model has a ``spread'' sensitivity pattern and non-uniform allocation is recommended.\nOtherwise, uniform 4-bit suffices at moderate compression.\nThis diagnostic correctly classifies all 9 tested models (Section~\\ref{sec:when_helps}).\n\n\n%% ============================================================\n%% 4  COMPOUNDING EFFECT CHARACTERIZATION\n%% ============================================================\n\\section{Compounding Effect Characterization}\n\\label{sec:compounding}\n\n\\subsection{Compounding Sweep}\n\nTable~\\ref{tab:compounding_sweep} shows the PPL of Qwen2.5-7B as a function of $k$ (maximum 2-bit heads) under $4\\times$ compression (budget$=0.25$).\nPPL growth is approximately linear for $k \\le 8$ ($+2.4\\%$), transitions to superlinear at $k \\approx 16$ ($+6.2\\%$), and becomes exponential after $k \\approx 48$ ($+136\\%$), reaching $10.07\\times$ baseline at $k = 112$ (fully unconstrained).\n\n\\begin{table}[h]\n\\centering\n\\caption{Compounding Sweep on Qwen2.5-7B (budget$=0.25$). PPL grows superlinearly with the number of simultaneous 2-bit heads.}\n\\label{tab:compounding_sweep}\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$k$ (max 2-bit heads) & PPL & Ratio to $k{=}0$ \\\\\n\\midrule\n0  & 9.81  & 1.00$\\times$ \\\\\n8  & 10.05 & 1.02$\\times$ \\\\\n16 & 10.42 & 1.06$\\times$ \\\\\n32 & 11.60 & 1.18$\\times$ \\\\\n64 & 23.22 & 2.37$\\times$ \\\\\n112 & 98.75 & 10.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Architecture Unconstrained Degradation}\n\nThe compounding failure mode is consistent across all 8 tested architectures.\nWithout a cardinality constraint, solvers over-allocate 2-bit heads and \\emph{always} underperform uniform 4-bit.\nThe degradation follows a concentration-dependent gradient:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Catastrophic} ($3.31\\times$): Qwen2.5-7B (spread pattern, L0 cluster compounding)\n\\item \\textbf{Moderate} ($1.47\\times$): Gemma-2-9B (flat pattern, solver over-allocates 106/336 heads to 2-bit due to indistinguishable distortions)\n\\item \\textbf{Mild} ($1.07$--$1.08\\times$): Yi-1.5-9B, Llama-3.1-8B, Mistral-7B-v0.3\n\\end{itemize}\n\nGemma-2-9B is instructive: despite its flat sensitivity distribution (concentration$=0.23$, CV$=1.28$), the solver assigns 31.5\\% of heads to 2-bit because distortions are indistinguishable.\nThe cumulative effect of this over-allocation produces a moderate $1.47\\times$ degradation.\nThe cardinality constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3\\% of uniform---confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\n\n\n%% ============================================================\n%% 5  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\nAll experiments use WikiText-2 for calibration and evaluation unless otherwise noted.\nWe report perplexity (PPL) on the test set with a context length of 2048 tokens and $4\\times$ compression (budget$=0.25$) as the default setting.\n\n\\subsection{Cross-Architecture Pipeline Results}\n\nTable~\\ref{tab:cross_arch} summarizes the full pipeline results across three primary architectures.\nThe constrained MCKP benefit varies dramatically: Qwen2.5-7B shows a large improvement (+27.3\\% vs uniform), Llama-3.1-8B shows marginal improvement (+0.2\\%), and Mistral-7B-v0.3 shows degradation ($-0.5\\%$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture pipeline results (budget$=0.25$). Constrained MCKP benefits are architecture-dependent.}\n\\label{tab:cross_arch}\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nModel & BF16 & Uniform 4-bit & Constrained MCKP & $\\Delta$ vs Uniform \\\\\n\\midrule\nQwen2.5-7B & 9.81 & 15.45 & 10.91 & +27.3\\% \\\\\nLlama-3.1-8B & 8.09 & 8.47 & 8.45 & +0.2\\% \\\\\nMistral-7B-v0.3 & 7.04 & 7.13 & 7.17 & $-$0.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama-3.1-8B.}\nThe solver naturally selects only 2 heads for 2-bit (distribution $\\{2{:}2, 4{:}253, 8{:}1\\}$), so the cardinality constraint ($k{=}8$) never binds.\nThe +0.2\\% improvement over uniform is within noise.\nThis is consistent with Llama's spike sensitivity distribution ($t_1/t_5 \\approx 0.85$): a single dominant head (L2H5) provides no optimization opportunity for the solver.\n\n\\paragraph{Mistral-7B-v0.3.}\nPPL monotonically increases with $k$: every additional 2-bit head hurts.\nEven the best constrained setting ($k{=}4$, PPL$=7.165$) is worse than uniform 4-bit ($7.131$).\nThis reflects Mistral's flat sensitivity distribution (concentration$=0.22$): no head benefits from 2-bit downgrade.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B $k$-ablation (budget$=0.25$). PPL increases monotonically with $k$; uniform 4-bit is optimal.}\n\\label{tab:mistral_k_ablation}\n\\begin{tabular}{@{}rrrl@{}}\n\\toprule\n$k$ & PPL & \\#2-bit heads & Note \\\\\n\\midrule\nUniform & 7.131 & 0 & Optimal for Mistral \\\\\n4  & 7.165 & 4  & Best constrained \\\\\n8  & 7.200 & 8  & \\\\\n16 & 7.311 & 16 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Solver Equivalence Under Constraint}\n\nTable~\\ref{tab:solver_equivalence} presents the strongest evidence that the cardinality constraint is the primary contribution.\nWithout the constraint, both greedy and MCKP fail catastrophically (PPL$>$30).\nWith the constraint ($k{=}8$), both produce \\emph{identical} bit allocations ($\\{2{:}8, 4{:}100, 8{:}4\\}$) and PPL ($\\Delta = 0.0012$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Solver equivalence under cardinality constraint (Qwen2.5-7B, $k{=}8$). Both solvers fail unconstrained; with the constraint, they produce identical allocations.}\n\\label{tab:solver_equivalence}\n\\begin{tabular}{@{}lrll@{}}\n\\toprule\nSolver & PPL & Bit Distribution & Status \\\\\n\\midrule\nGreedy unconstrained & 32.45 & $\\{2{:}68, 4{:}30, 8{:}4, 16{:}10\\}$ & FAIL \\\\\nMCKP unconstrained & 36.92 & --- & FAIL \\\\\nGreedy + max\\_2bit$=$8 & 11.23 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ & PASS \\\\\nMCKP + max\\_2bit$=$8 & 11.23 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ & PASS \\\\\nUniform 4-bit & 15.45 & all 4-bit & baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis equivalence demonstrates that the constraint reduces the feasible region to where solver sophistication is irrelevant.\nThe practical implication is that practitioners can add a single integer parameter (\\texttt{max\\_2bit}) to \\emph{any} existing allocation pipeline---including RateQuant's greedy---and achieve near-optimal results.\n\n\\subsection{MCKP Near-Optimality (Oracle Comparison)}\n\nTo quantify how close MCKP is to the true optimum within the constrained feasible set, we perform brute-force enumeration over 4-layer groups on Qwen2.5-7B (Table~\\ref{tab:oracle}).\nMCKP is exactly optimal in 5/8 layer groups; the remaining 3 show gaps of 0.0045--0.0136 PPL, arising from 2-bit head position swaps within the same bit budget.\nThe maximum oracle gap is 0.018 PPL---negligible compared to the 4.54 PPL gap between constrained MCKP (10.91) and uniform 4-bit (15.45).\n\n\\begin{table}[h]\n\\centering\n\\caption{MCKP vs brute-force oracle per layer group (Qwen2.5-7B). MCKP is near-optimal within the constrained feasible set.}\n\\label{tab:oracle}\n\\begin{tabular}{@{}lcr@{}}\n\\toprule\nLayer Group & MCKP Optimal? & Gap (PPL) \\\\\n\\midrule\nL0--L3  & Yes & 0.000 \\\\\nL4--L7  & No  & 0.005 \\\\\nL8--L11 & No  & 0.014 \\\\\nL12--L15 & Yes & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Budget Sweep (Compression Ratio)}\n\nTable~\\ref{tab:budget_sweep} shows how the constrained MCKP benefit scales with compression ratio on Qwen2.5-7B.\nAt $2\\times$ compression, uniform and MCKP are equivalent ($\\sim 0\\%$ difference).\nAt $4\\times$, MCKP provides 29.4\\% improvement.\nAt $8\\times$, the gap becomes dramatic: MCKP achieves PPL$=57.6$ versus uniform 2-bit PPL$=2643.77$ ($45.9\\times$)---the constraint is the difference between a usable and unusable model at aggressive compression.\n\n\\begin{table}[h]\n\\centering\n\\caption{Budget sweep on Qwen2.5-7B. Compression amplifies the benefit of constrained allocation.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nCompression & MCKP PPL & Uniform PPL & $\\Delta$ \\\\\n\\midrule\n$2\\times$ (budget$=0.5$) & 9.85 & 9.86 & $\\sim 0\\%$ \\\\\n$4\\times$ (budget$=0.25$) & 10.91 & 15.45 & 29.4\\% \\\\\n$8\\times$ (budget$=0.125$) & 57.60 & 2643.77 & 45.9$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Profiling Resolution Impact}\n\n\\begin{table}[h]\n\\centering\n\\caption{Profiling resolution impact (Qwen2.5-7B, $k{=}8$). Higher resolution improves allocation quality at increased profiling cost.}\n\\label{tab:profiling_resolution}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nResolution & PPL & Detected Heads & Time (min) \\\\\n\\midrule\nLow-res ($16 \\times 512$)  & 11.23 & 37/112  & $\\sim$10 \\\\\nHigh-res ($64 \\times 2048$) & 10.91 & 100/112 & 65.5 \\\\\nUniform 4-bit & 15.45 & N/A & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHigh-resolution profiling reduces PPL from 11.23 to 10.91 ($-2.8\\%$), detecting sensitivity in 100/112 heads versus 37/112 for low-resolution.\nHowever, even low-resolution profiling yields a 27.3\\% improvement over uniform 4-bit (11.23 vs 15.45), suggesting that approximate profiling suffices for the primary benefit.\nThe 65.5-minute profiling cost at high resolution is a practical consideration; we note this as an engineering tradeoff rather than a fundamental limitation.\n\n\\subsection{L0 Exclusion Ablation}\n\nOn Qwen2.5-7B, Layer 0 heads exhibit a $26\\times$ dominance ratio in sensitivity delta.\nWe test whether explicit L0 exclusion (hard-coding L0 heads to 8-bit) is necessary, or whether the solver discovers L0 sensitivity automatically from profiling data.\n\n\\begin{table}[h]\n\\centering\n\\caption{L0 exclusion ablation (Qwen2.5-7B, budget$=0.25$). The solver automatically assigns 8-bit to all 4 L0 heads.}\n\\label{tab:l0_ablation}\n\\begin{tabular}{@{}lrll@{}}\n\\toprule\nCondition & PPL & L0 Bit-width & Note \\\\\n\\midrule\nMCKP + L0 exclusion + $k{=}8$ & 10.91 & 8-bit (hard-coded) & Original \\\\\nMCKP + $k{=}8$ only & 10.91 & 8-bit (solver-discovered) & Automatic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe solver automatically assigns 8-bit to all 4 L0 heads, producing identical PPL.\nThis confirms that the profiling-based approach correctly identifies L0 sensitivity without manual intervention, though we note this has only been verified on Qwen2.5-7B where L0 dominance is extreme ($26\\times$).\n\n\\subsection{K/V Separation}\n\nWe test whether treating Key and Value heads as independent MCKP items with separate budgets improves over joint K$=$V treatment (Table~\\ref{tab:kv_sep}).\n\n\\begin{table}[h]\n\\centering\n\\caption{K/V separation vs joint treatment (Qwen2.5-7B, $k{=}8$). Separation is worse due to K-cache compounding.}\n\\label{tab:kv_sep}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nMethod & PPL & K 2-bit & V 2-bit \\\\\n\\midrule\nJoint K$=$V ($k{=}8$) & 10.91 & 8 & 0 \\\\\nK/V Separation & 11.22 & 16 & 0 \\\\\nUniform 4-bit & 15.45 & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nK/V separation is worse ($+0.31$ PPL) because it allows 16 K-heads at 2-bit, exceeding the safe range of $k \\le 8$ and triggering K-cache compounding.\nV-heads are assigned uniform 4-bit under both settings.\nThis suggests that K-cache is more sensitive to 2-bit compounding than V-cache, and that a single joint cardinality constraint is preferable.\n\n\\subsection{Heuristic Baselines}\n\nWe compare constrained MCKP against simpler allocation strategies: L0-random (protect L0, randomly assign remaining 2-bit heads) and naive positional (assign 2-bit by layer position).\n\n\\begin{table}[h]\n\\centering\n\\caption{MCKP vs heuristic baselines (budget$=0.25$). MCKP consistently outperforms random constraint-respecting allocation.}\n\\label{tab:heuristic_baselines}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & MCKP & L0-random (median) & Naive Positional & Uniform \\\\\n\\midrule\nQwen2.5-7B  & 10.91 & 11.52 & 12.23 & 15.45 \\\\\nLlama-3.1-8B & 8.45 & 10.04 & 9.94 & 8.47 \\\\\nMistral-7B-v0.3 & 7.16 & 7.59 & 7.48 & 7.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMCKP outperforms L0-random by 5.2\\% (Qwen), 15.8\\% (Llama), and 5.7\\% (Mistral) in PPL, demonstrating that profiling-based allocation provides optimization value within the constrained feasible set.\nThe large seed variance in L0-random (Qwen std$=0.47$, Llama std$=1.03$) indicates that the specific choice of 2-bit heads matters significantly.\n\n\\subsection{Cross-Dataset Calibration Robustness}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-dataset calibration agreement ($>$96\\% across 3 architectures). Profiling-based sensitivity ranking is robust to calibration source.}\n\\label{tab:cross_dataset}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nModel & Agreement & Same-domain PPL & Cross-domain PPL \\\\\n\\midrule\nQwen2.5-7B  & 108/112 (96.4\\%) & 11.29 & 20.56 \\\\\nLlama-3.1-8B & 250/256 (97.7\\%) & 8.45 & 8.65 \\\\\nMistral-7B-v0.3 & 247/256 (96.5\\%) & 7.16 & 7.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibrating on C4 instead of WikiText-2 produces $>$96\\% identical head assignments across all three architectures, indicating that per-head sensitivity ranking is an architectural property rather than a dataset-dependent artifact.\nThe cross-domain PPL gap is minimal for Llama (0.20) and Mistral (0.03), though larger for Qwen (9.27), reflecting Qwen's higher sensitivity to calibration domain.\n\n\\subsection{Multi-Seed Stability}\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-seed PPL stability (Qwen2.5-7B, $k{=}8$, 3 seeds). Bit distribution is consistent across seeds.}\n\\label{tab:multi_seed}\n\\begin{tabular}{@{}lrl@{}}\n\\toprule\nSeed & PPL & Bit Distribution \\\\\n\\midrule\n0 & 11.02 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n1 & 10.90 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n2 & 11.05 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n\\midrule\nMean $\\pm$ std & $10.99 \\pm 0.065$ & consistent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 95\\% confidence interval $[10.86, 11.12]$ is well below uniform 4-bit (15.45), confirming that the improvement is statistically robust.\nBit distribution is identical across all seeds, and 90.2\\% of head allocations agree across all three seeds.\n\n\n%% ============================================================\n%% 6  WHEN DOES NON-UNIFORM ALLOCATION HELP?\n%% ============================================================\n\\section{When Does Non-Uniform Allocation Help?}\n\\label{sec:when_helps}\n\n\\subsection{Cross-Architecture Downstream Evaluation}\n\nTable~\\ref{tab:downstream} presents downstream task results across 5 architectures under $4\\times$ compression.\nOnly Qwen2.5-7B (spread sensitivity pattern) shows consistent downstream gains (+1.25 to +4.00pp).\nThe remaining 4 architectures show minor degradation: Yi-1.5 $-0.77$pp, Llama $-0.99$pp, Mistral $-0.48$pp, Gemma-2 $+0.14$pp (noise).\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream evaluation ($4\\times$ compression, 0-shot). MCKP benefits only Qwen2.5-7B (spread pattern). ARC-Challenge shows the largest per-task sensitivity to allocation strategy across all non-Spread models.}\n\\label{tab:downstream}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Pattern & ARC-C $\\Delta$ & HellaSwag $\\Delta$ & PIQA $\\Delta$ & WinoGrande $\\Delta$ & Avg $\\Delta$ \\\\\n\\midrule\nQwen2.5-7B & Spread & +3.16pp & +4.00pp & +1.25pp & +1.97pp & +2.60pp \\\\\nYi-1.5-9B & Spike & $-$3.24pp & $-$0.60pp & $-$0.33pp & +1.27pp & $-$0.77pp \\\\\nLlama-3.1-8B & Spike & $-$2.65pp & $-$0.14pp & $-$0.65pp & $-$0.15pp & $-$0.99pp \\\\\nMistral-7B-v0.3 & Flat & $-$1.19pp & --- & --- & --- & $-$0.48pp \\\\\nGemma-2-9B & Flat & $-$0.17pp & --- & --- & --- & +0.14pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nARC-Challenge shows the largest per-task sensitivity to allocation strategy, with consistent degradation across non-Spread models (Yi $-3.24$pp, Llama $-2.65$pp, Mistral $-1.19$pp).\nThis is consistent with ARC-Challenge's reliance on multi-step reasoning, where subtle KV cache quantization errors accumulate.\n\n\\subsection{Sensitivity Distribution Taxonomy}\n\nWe identify three sensitivity distribution shapes that predict allocation benefit:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Spread} (Qwen2.5-7B): Multiple heads with cross-bitwidth sensitivity gradients. L0 cluster of 4 heads with $26\\times$ dominance ratio. Concentration$=0.61$, $t_1/t_5=0.57$. MCKP benefits: $+27.3\\%$ PPL, $+2.6$pp downstream.\n\n\\item \\textbf{Spike} (Yi-1.5-9B, Llama-3.1-8B): Single extreme outlier dominates. Yi L4H3 accounts for 64\\% of total delta. Solver assigns 8-bit to the outlier but cannot differentiate remaining heads. Concentration high (Yi $0.71$) but $t_1/t_5$ also high ($0.90$). No MCKP benefit.\n\n\\item \\textbf{Flat} (Mistral-7B-v0.3, Gemma-2-9B): Near-homogeneous sensitivity. Profiler reports near-zero inter-head differences (Mistral concentration$=0.22$, Gemma-2 $0.23$). Every 2-bit head hurts equally; non-uniform allocation is futile.\n\\end{itemize}\n\n\\paragraph{The spike--spread distinction.}\nYi-1.5 (GQA 8:1, concentration$=0.71$) and Qwen (GQA 7:1, concentration$=0.61$) illustrate why GQA ratio and concentration alone are insufficient predictors.\nYi has higher GQA and higher concentration than Qwen, yet shows no benefit.\nThe critical difference is distribution \\emph{shape}: Qwen's L0 \\emph{cluster} of sensitive heads creates optimization opportunities, while Yi's single extreme outlier cannot be exploited.\n\n\\subsection{Diagnostic Validation}\n\nThe 2-metric diagnostic (concentration $\\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$) correctly classifies all 9 tested models:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item Qwen2.5-7B: $c{=}0.61$, $t_1/t_5{=}0.57$ $\\to$ spread $\\to$ benefit predicted $\\to$ \\textbf{correct} (+27.3\\%)\n\\item Yi-1.5-9B: $c{=}0.71$, $t_1/t_5{=}0.90$ $\\to$ spike $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($\\approx 0\\%$)\n\\item Llama-3.1-8B: $c{=}0.57$, $t_1/t_5{=}0.85$ $\\to$ spike $\\to$ no benefit predicted $\\to$ \\textbf{correct} (+0.2\\%)\n\\item Mistral-7B-v0.3: $c{=}0.22$, $t_1/t_5{=}$--- $\\to$ flat $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($-0.5\\%$)\n\\item Gemma-2-9B: $c{=}0.23$, $t_1/t_5{=}0.38$ $\\to$ flat $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($-0.3\\%$)\n\\end{itemize}\nWe emphasize that $n{=}9$ provides a consistent pattern, not a statistical claim.\n\n%% ============================================================\n%% 7  RUNTIME ANALYSIS\n%% ============================================================\n\\section{Runtime Analysis}\n\\label{sec:runtime}\n\n\\begin{table}[h]\n\\centering\n\\caption{Runtime benchmark (Qwen2.5-7B, seq\\_len$=$2048). Mixed-precision incurs 8.5\\% throughput overhead vs uniform 4-bit due to per-head dequantization.}\n\\label{tab:runtime}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nMethod & Prefill (ms) & Decode (ms) & Throughput (tok/s) & Memory (MB) \\\\\n\\midrule\nBF16 (no quant.) & 45.86 & 33.78 & 29.6 & 21 \\\\\nUniform 4-bit & 54.25 & 42.46 & 23.6 & 5.25 \\\\\nConstrained MCKP & 57.03 & 46.09 & 21.8 & 5.25 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMixed-precision MCKP incurs an 8.5\\% throughput reduction versus uniform 4-bit (21.8 vs 23.6 tok/s), stemming from per-head dequantization kernel overhead.\nThe MCKP solver itself is negligible (0.005s).\nThis overhead is an engineering limitation of the current implementation: a fused mixed-precision dequantization kernel could eliminate it.\nThe memory footprint is identical ($4\\times$ compression) since the average bit-width remains the same.\n\nFor memory-bound scenarios (long context, large batch sizes), the $4\\times$ memory reduction enables deployments that BF16 cannot support.\nOn 7/8 architectures where non-uniform allocation provides no PPL benefit, the 8.5\\% throughput cost is pure overhead; the diagnostic (Section~\\ref{sec:when_helps}) helps practitioners avoid this cost by recommending uniform 4-bit when appropriate.\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present an empirical analysis of per-head KV cache quantization on hardware-aligned bit-widths $\\{2,4,8,16\\}$, identifying three findings:\n\n\\textbf{(1)} 2-bit quantization distortions compound non-additively, causing all tested unconstrained solvers to underperform uniform 4-bit across 8 architectures.\nThis compounding is superlinear after $k{\\approx}16$ simultaneous 2-bit heads and exponential after $k{\\approx}48$.\n\n\\textbf{(2)} A cardinality constraint ($\\le k$ heads at 2-bit, $k{\\le}8$) prevents compounding across all tested architectures and makes solver choice irrelevant (greedy$=$MCKP, $\\Delta{=}0.0000$).\nPractitioners need only add one integer parameter to existing pipelines.\n\n\\textbf{(3)} Under moderate compression, only 1/8 architectures benefits from non-uniform allocation.\nA 2-metric diagnostic (9/9 correct) tells practitioners when to use profiling-based allocation versus uniform 4-bit.\n\n\\paragraph{Limitations.}\nOur experiments are limited to 7B--14B scale models; scaling behavior to 70B+ models remains an open question (our 72B profiling attempt was terminated due to resource constraints).\nMulti-seed confidence intervals are reported for PPL (std$=$0.065) but not for all downstream tasks.\nThe 8.5\\% throughput overhead of the current mixed-precision implementation could be eliminated with optimized kernels but represents a practical concern.\nThe diagnostic threshold values ($c{\\gtrsim}0.50$, $t_1/t_5{\\lesssim}0.70$) are derived from $n{=}9$ models and should be treated as an empirical observation, not a statistically validated rule.\n\n\\bibliography{references}\n\\bibliographystyle{plain}\n\n\\begin{thebibliography}{10}\n\\bibitem{hooper2024kvquant}\nColeman Hooper, Sehoon Kim, Haonan Mohber, et al.\n\\newblock KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}, 2024.\n\n\\bibitem{liu2024kivi}\nZirui Liu, Jiayi Yuan, Hongye Jin, et al.\n\\newblock KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache.\n\\newblock \\emph{arXiv preprint arXiv:2402.02750}, 2024.\n\n\\bibitem{dong2024qaq}\nHaowen Dong, Jiaqi Zheng, et al.\n\\newblock QAQ: Quality Adaptive Quantization for LLM KV Cache.\n\\newblock \\emph{arXiv preprint arXiv:2403.04643}, 2024.\n\n\\bibitem{ratequant2024}\nRateQuant Authors.\n\\newblock RateQuant: Rate-Distortion Optimal KV Cache Quantization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{nagel2020up}\nMarkus Nagel, Rana Ali Amjad, Mart van Baalen, et al.\n\\newblock Up or Down? Adaptive Rounding for Post-Training Quantization.\n\\newblock \\emph{ICML}, 2020.\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efe77b82-b158-4be0-bcd7-468ce86e4d7c",
  "isSidechain": false,
  "requestId": "req_011Cb5UGMvuHAfRL4jAmywBG",
  "type": "assistant",
  "uuid": "d57d7885-d1fa-486a-98dc-4f7b8be182d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuFuegjcxNxHb48SNco6Mm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 49790,
      "output_tokens": 11443,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11443,
          "cache_read_input_tokens": 49790,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
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

_source line 22 · 2026-05-16T02:41:06.735Z_

<details><summary>↩ Tool result · `toolu_01LPpfzcM382YUoKGKK2yVyZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d57d7885-d1fa-486a-98dc-4f7b8be182d6",
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "33672d26-5373-432a-9ea3-753a69614b30",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\n\\title{Compounding Failures in Per-Head KV Cache Quantization:\\\\An Empirical Analysis of When Non-Uniform Allocation Helps}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nPer-head mixed-precision KV cache quantization promises better quality--compression tradeoffs than uniform bit-width assignment.\nWe show that on hardware-aligned non-consecutive bit-widths $\\{2,4,8,16\\}$, this promise breaks:\n2-bit quantization distortions compound non-additively through the residual stream, causing \\emph{all} tested unconstrained solvers (greedy, MCKP) to over-allocate 2-bit heads and underperform uniform 4-bit across 8 diverse architectures (degradation $1.07\\times$--$3.31\\times$ baseline).\nA simple cardinality constraint ($\\le k$ heads at 2-bit) prevents compounding across all tested architectures, and reduces the feasible set to where solver choice is irrelevant: constrained greedy and constrained MCKP produce identical bit allocations ($\\Delta=0.0000$ PPL).\nSurprisingly, under moderate (4$\\times$) compression, only 1 of 8 tested architectures benefits from non-uniform allocation; the remaining 7 show no benefit or minor degradation.\nWe propose a 2-metric empirical diagnostic (top-5\\% concentration $\\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$) that correctly classifies all 9 tested models, giving practitioners a simple check: if the diagnostic says ``no,'' skip profiling and use uniform 4-bit with zero quality loss.\nAt aggressive compression (8$\\times$), the constraint reduces degradation from $45.9\\times$ to $5.9\\times$ baseline on Qwen2.5-7B, demonstrating critical deployment value.\n\\end{abstract}\n\n%% ============================================================\n%% 1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nKV cache memory is a primary bottleneck for long-context LLM serving.\nPer-head mixed-precision quantization---assigning different bit-widths to different attention heads based on their sensitivity---has been proposed as a principled approach to improve the quality--compression tradeoff over uniform quantization~\\cite{hooper2024kvquant,liu2024kivi,dong2024qaq}.\nThe underlying assumption is straightforward: allocate fewer bits to insensitive heads and more bits to sensitive ones.\n\nHowever, modern hardware efficiently supports only non-consecutive bit-widths $\\{2,4,8,16\\}$, creating a large gap between the lowest two options.\nWe discover that this gap introduces a previously unreported failure mode: \\textbf{2-bit quantization distortions compound non-additively} when multiple heads are simultaneously assigned 2-bit precision.\nPer-head profiling predicts a joint PPL of ${\\sim}11$ when assigning many heads to 2-bit, but the actual PPL is 32--37---a $3\\times$ prediction error.\nThis compounding causes all tested unconstrained allocation algorithms to systematically over-allocate 2-bit heads, producing worse results than naive uniform 4-bit across \\emph{all 8 tested architectures} (degradation ranging from $1.07\\times$ to $3.31\\times$ baseline).\n\nThis paper makes three contributions, framed as an empirical analysis:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Compounding effect characterization.} We provide the first quantitative mapping of 2-bit compounding in per-head KV cache quantization, showing superlinear PPL growth after $k \\approx 16$ simultaneous 2-bit heads and exponential growth after $k \\approx 48$ on Qwen2.5-7B (Table~\\ref{tab:compounding_sweep}).\nThe pattern is consistent across 8 architectures spanning GQA ratios 2:1 to 8:1.\n\n\\item \\textbf{Cardinality constraint as universal fix.} A cardinality constraint ($\\le k$ heads at 2-bit) prevents compounding across all tested architectures.\nUnder this constraint, solver choice becomes irrelevant: constrained greedy and constrained MCKP produce \\emph{identical} allocations ($\\Delta = 0.0000$; Table~\\ref{tab:solver_equivalence}).\nThe safe range $k \\le 8$ yields $<2.5\\%$ degradation across all tested architectures.\n\n\\item \\textbf{When does non-uniform allocation help?} Under moderate ($4\\times$) compression, only 1/8 architectures (Qwen2.5-7B, ``spread'' sensitivity pattern) benefits from non-uniform allocation (+27.3\\% PPL improvement, +2.6pp average downstream gain).\nThe remaining 7/8 show no benefit or minor degradation.\nA 2-metric diagnostic (9/9 correct) tells practitioners whether profiling is worthwhile.\n\\end{enumerate}\n\nOur work differs from RateQuant~\\cite{ratequant2024} in three key aspects: (a)~RateQuant operates on consecutive bit-widths $\\{2,\\ldots,6\\}$ where polymatroid structure guarantees greedy optimality; on hardware-aligned $\\{2,4,8,16\\}$ this structure breaks, (b)~RateQuant acknowledges compounding in Appendix~M but does not characterize it or propose a fix---we provide the first quantitative sweep and a universal constraint, (c)~we provide the first systematic study of \\emph{when} non-uniform allocation is actually beneficial versus when uniform suffices.\n\n\n%% ============================================================\n%% 2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{KV Cache Quantization.}\nKIVI~\\cite{liu2024kivi} applies uniform per-channel quantization to KV caches with asymmetric K/V treatment.\nKVQuant~\\cite{hooper2024kvquant} introduces per-channel sensitivity-aware quantization with non-uniform codebooks.\nQAQ~\\cite{dong2024qaq} proposes attention-aware quantization with quality-adaptive bit-width selection.\n\n\\paragraph{Mixed-Precision Allocation.}\nRateQuant~\\cite{ratequant2024} formulates per-head bit allocation as a rate--distortion problem, deriving a continuous closed-form solution (Thm.~2) and a discrete greedy algorithm (Prop.~6) that is provably optimal on consecutive integer bit-widths.\nOn non-consecutive hardware-aligned widths $\\{2,4,8,16\\}$, the polymatroid structure underlying this optimality guarantee breaks.\nRateQuant acknowledges compounding effects in Appendix~M but provides no quantitative characterization or mitigation.\nOur work provides the first such characterization and shows that a cardinality constraint both fixes the compounding failure and makes the solver choice irrelevant---constrained greedy matches constrained MCKP exactly.\n\n\\paragraph{Compounding Effects in Quantization.}\nNon-additive error accumulation is well-known in weight quantization~\\cite{nagel2020up}, but its manifestation in per-head KV cache quantization---where the residual stream propagates head-level errors across layers---has not been systematically studied.\nWe provide the first quantitative evidence that per-head independent profiling underestimates joint 2-bit degradation by ${\\sim}3\\times$.\n\n\n%% ============================================================\n%% 3  METHOD\n%% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\nGiven an LLM with $H$ KV heads and a set of hardware-aligned bit-widths $\\mathcal{B} = \\{2, 4, 8, 16\\}$, per-head mixed-precision allocation assigns a bit-width $b_h \\in \\mathcal{B}$ to each head $h$ subject to a memory budget constraint:\n\\begin{equation}\n\\min_{\\{b_h\\}} \\; \\text{PPL}(\\{b_h\\}) \\quad \\text{s.t.} \\quad \\sum_{h=1}^{H} b_h \\le B\n\\label{eq:allocation}\n\\end{equation}\nwhere $B$ is the total bit budget.\n\n\\subsection{Per-Head Sensitivity Profiling}\n\nFor each head $h$ and candidate bit-width $b \\in \\mathcal{B}$, we measure the \\emph{distortion delta}: the PPL increase when head $h$ alone is quantized to $b$-bit while all other heads remain at 16-bit.\nThis produces a distortion matrix $\\Delta(h, b)$ of size $H \\times |\\mathcal{B}|$.\n\nProfiling uses calibration data from WikiText-2 (train split).\nWe evaluate two resolutions: low-resolution (16 sequences $\\times$ 512 tokens) and high-resolution (64 sequences $\\times$ 2048 tokens).\nHigh-resolution profiling detects sensitivity in 100/112 heads versus 37/112 for low-resolution on Qwen2.5-7B, improving constrained PPL from 11.23 to 10.91 ($-2.8\\%$; Table~\\ref{tab:profiling_resolution}).\n\n\\subsection{MCKP Formulation with Cardinality Constraint}\n\nWe formulate bit-width allocation as a Multiple-Choice Knapsack Problem (MCKP): each head selects exactly one bit-width from $\\mathcal{B}$, with the objective of minimizing total distortion subject to the memory budget.\nCritically, we add a \\textbf{cardinality constraint}:\n\\begin{equation}\n\\sum_{h=1}^{H} \\mathbf{1}[b_h = 2] \\le k\n\\label{eq:constraint}\n\\end{equation}\nlimiting the number of heads assigned to 2-bit quantization.\nThis constraint is motivated by our empirical observation that 2-bit distortions compound non-additively (Section~\\ref{sec:compounding}).\n\nThe constraint parameter $k$ is selected via a small-scale compounding test: sweep $k$ on a validation set and identify the ``safe'' range where PPL growth remains approximately linear.\nAcross all tested architectures, $k \\le 8$ consistently yields $<2.5\\%$ degradation relative to the unconstrained optimal (Table~\\ref{tab:compounding_sweep}).\n\n\\subsection{Applicability Diagnostic}\n\nNot all architectures benefit from non-uniform allocation.\nWe propose a 2-metric diagnostic based on the per-head sensitivity profile:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Top-5\\% concentration} ($c$): the fraction of total distortion delta concentrated in the top 5\\% of heads.\n\\item \\textbf{$t_1/t_5$ ratio}: the ratio of the largest single-head distortion to the sum of the top-5 distortions.\n\\end{itemize}\n\nThe decision rule: if $c \\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$, the model has a ``spread'' sensitivity pattern and non-uniform allocation is recommended.\nOtherwise, uniform 4-bit suffices at moderate compression.\nThis diagnostic correctly classifies all 9 tested models (Section~\\ref{sec:when_helps}).\n\n\n%% ============================================================\n%% 4  COMPOUNDING EFFECT CHARACTERIZATION\n%% ============================================================\n\\section{Compounding Effect Characterization}\n\\label{sec:compounding}\n\n\\subsection{Compounding Sweep}\n\nTable~\\ref{tab:compounding_sweep} shows the PPL of Qwen2.5-7B as a function of $k$ (maximum 2-bit heads) under $4\\times$ compression (budget$=0.25$).\nPPL growth is approximately linear for $k \\le 8$ ($+2.4\\%$), transitions to superlinear at $k \\approx 16$ ($+6.2\\%$), and becomes exponential after $k \\approx 48$ ($+136\\%$), reaching $10.07\\times$ baseline at $k = 112$ (fully unconstrained).\n\n\\begin{table}[h]\n\\centering\n\\caption{Compounding Sweep on Qwen2.5-7B (budget$=0.25$). PPL grows superlinearly with the number of simultaneous 2-bit heads.}\n\\label{tab:compounding_sweep}\n\\begin{tabular}{@{}rrrr@{}}\n\\toprule\n$k$ (max 2-bit heads) & PPL & Ratio to $k{=}0$ \\\\\n\\midrule\n0  & 9.81  & 1.00$\\times$ \\\\\n8  & 10.05 & 1.02$\\times$ \\\\\n16 & 10.42 & 1.06$\\times$ \\\\\n32 & 11.60 & 1.18$\\times$ \\\\\n64 & 23.22 & 2.37$\\times$ \\\\\n112 & 98.75 & 10.07$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Architecture Unconstrained Degradation}\n\nThe compounding failure mode is consistent across all 8 tested architectures.\nWithout a cardinality constraint, solvers over-allocate 2-bit heads and \\emph{always} underperform uniform 4-bit.\nThe degradation follows a concentration-dependent gradient:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Catastrophic} ($3.31\\times$): Qwen2.5-7B (spread pattern, L0 cluster compounding)\n\\item \\textbf{Moderate} ($1.47\\times$): Gemma-2-9B (flat pattern, solver over-allocates 106/336 heads to 2-bit due to indistinguishable distortions)\n\\item \\textbf{Mild} ($1.07$--$1.08\\times$): Yi-1.5-9B, Llama-3.1-8B, Mistral-7B-v0.3\n\\end{itemize}\n\nGemma-2-9B is instructive: despite its flat sensitivity distribution (concentration$=0.23$, CV$=1.28$), the solver assigns 31.5\\% of heads to 2-bit because distortions are indistinguishable.\nThe cumulative effect of this over-allocation produces a moderate $1.47\\times$ degradation.\nThe cardinality constraint reduces 2-bit heads from 106 to 8, yielding PPL within 0.3\\% of uniform---confirming that the constraint universally prevents solver over-allocation regardless of distribution shape.\n\n\n%% ============================================================\n%% 5  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\nAll experiments use WikiText-2 for calibration and evaluation unless otherwise noted.\nWe report perplexity (PPL) on the test set with a context length of 2048 tokens and $4\\times$ compression (budget$=0.25$) as the default setting.\n\n\\subsection{Cross-Architecture Pipeline Results}\n\nTable~\\ref{tab:cross_arch} summarizes the full pipeline results across three primary architectures.\nThe constrained MCKP benefit varies dramatically: Qwen2.5-7B shows a large improvement (+27.3\\% vs uniform), Llama-3.1-8B shows marginal improvement (+0.2\\%), and Mistral-7B-v0.3 shows degradation ($-0.5\\%$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-architecture pipeline results (budget$=0.25$). Constrained MCKP benefits are architecture-dependent.}\n\\label{tab:cross_arch}\n\\begin{tabular}{@{}lrrrrr@{}}\n\\toprule\nModel & BF16 & Uniform 4-bit & Constrained MCKP & $\\Delta$ vs Uniform \\\\\n\\midrule\nQwen2.5-7B & 9.81 & 15.45 & 10.91 & +27.3\\% \\\\\nLlama-3.1-8B & 8.09 & 8.47 & 8.45 & +0.2\\% \\\\\nMistral-7B-v0.3 & 7.04 & 7.13 & 7.17 & $-$0.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Llama-3.1-8B.}\nThe solver naturally selects only 2 heads for 2-bit (distribution $\\{2{:}2, 4{:}253, 8{:}1\\}$), so the cardinality constraint ($k{=}8$) never binds.\nThe +0.2\\% improvement over uniform is within noise.\nThis is consistent with Llama's spike sensitivity distribution ($t_1/t_5 \\approx 0.85$): a single dominant head (L2H5) provides no optimization opportunity for the solver.\n\n\\paragraph{Mistral-7B-v0.3.}\nPPL monotonically increases with $k$: every additional 2-bit head hurts.\nEven the best constrained setting ($k{=}4$, PPL$=7.165$) is worse than uniform 4-bit ($7.131$).\nThis reflects Mistral's flat sensitivity distribution (concentration$=0.22$): no head benefits from 2-bit downgrade.\n\n\\begin{table}[h]\n\\centering\n\\caption{Mistral-7B $k$-ablation (budget$=0.25$). PPL increases monotonically with $k$; uniform 4-bit is optimal.}\n\\label{tab:mistral_k_ablation}\n\\begin{tabular}{@{}rrrl@{}}\n\\toprule\n$k$ & PPL & \\#2-bit heads & Note \\\\\n\\midrule\nUniform & 7.131 & 0 & Optimal for Mistral \\\\\n4  & 7.165 & 4  & Best constrained \\\\\n8  & 7.200 & 8  & \\\\\n16 & 7.311 & 16 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Solver Equivalence Under Constraint}\n\nTable~\\ref{tab:solver_equivalence} presents the strongest evidence that the cardinality constraint is the primary contribution.\nWithout the constraint, both greedy and MCKP fail catastrophically (PPL$>$30).\nWith the constraint ($k{=}8$), both produce \\emph{identical} bit allocations ($\\{2{:}8, 4{:}100, 8{:}4\\}$) and PPL ($\\Delta = 0.0012$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Solver equivalence under cardinality constraint (Qwen2.5-7B, $k{=}8$). Both solvers fail unconstrained; with the constraint, they produce identical allocations.}\n\\label{tab:solver_equivalence}\n\\begin{tabular}{@{}lrll@{}}\n\\toprule\nSolver & PPL & Bit Distribution & Status \\\\\n\\midrule\nGreedy unconstrained & 32.45 & $\\{2{:}68, 4{:}30, 8{:}4, 16{:}10\\}$ & FAIL \\\\\nMCKP unconstrained & 36.92 & --- & FAIL \\\\\nGreedy + max\\_2bit$=$8 & 11.23 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ & PASS \\\\\nMCKP + max\\_2bit$=$8 & 11.23 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ & PASS \\\\\nUniform 4-bit & 15.45 & all 4-bit & baseline \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis equivalence demonstrates that the constraint reduces the feasible region to where solver sophistication is irrelevant.\nThe practical implication is that practitioners can add a single integer parameter (\\texttt{max\\_2bit}) to \\emph{any} existing allocation pipeline---including RateQuant's greedy---and achieve near-optimal results.\n\n\\subsection{MCKP Near-Optimality (Oracle Comparison)}\n\nTo quantify how close MCKP is to the true optimum within the constrained feasible set, we perform brute-force enumeration over 4-layer groups on Qwen2.5-7B (Table~\\ref{tab:oracle}).\nMCKP is exactly optimal in 5/8 layer groups; the remaining 3 show gaps of 0.0045--0.0136 PPL, arising from 2-bit head position swaps within the same bit budget.\nThe maximum oracle gap is 0.018 PPL---negligible compared to the 4.54 PPL gap between constrained MCKP (10.91) and uniform 4-bit (15.45).\n\n\\begin{table}[h]\n\\centering\n\\caption{MCKP vs brute-force oracle per layer group (Qwen2.5-7B). MCKP is near-optimal within the constrained feasible set.}\n\\label{tab:oracle}\n\\begin{tabular}{@{}lcr@{}}\n\\toprule\nLayer Group & MCKP Optimal? & Gap (PPL) \\\\\n\\midrule\nL0--L3  & Yes & 0.000 \\\\\nL4--L7  & No  & 0.005 \\\\\nL8--L11 & No  & 0.014 \\\\\nL12--L15 & Yes & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Budget Sweep (Compression Ratio)}\n\nTable~\\ref{tab:budget_sweep} shows how the constrained MCKP benefit scales with compression ratio on Qwen2.5-7B.\nAt $2\\times$ compression, uniform and MCKP are equivalent ($\\sim 0\\%$ difference).\nAt $4\\times$, MCKP provides 29.4\\% improvement.\nAt $8\\times$, the gap becomes dramatic: MCKP achieves PPL$=57.6$ versus uniform 2-bit PPL$=2643.77$ ($45.9\\times$)---the constraint is the difference between a usable and unusable model at aggressive compression.\n\n\\begin{table}[h]\n\\centering\n\\caption{Budget sweep on Qwen2.5-7B. Compression amplifies the benefit of constrained allocation.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nCompression & MCKP PPL & Uniform PPL & $\\Delta$ \\\\\n\\midrule\n$2\\times$ (budget$=0.5$) & 9.85 & 9.86 & $\\sim 0\\%$ \\\\\n$4\\times$ (budget$=0.25$) & 10.91 & 15.45 & 29.4\\% \\\\\n$8\\times$ (budget$=0.125$) & 57.60 & 2643.77 & 45.9$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Profiling Resolution Impact}\n\n\\begin{table}[h]\n\\centering\n\\caption{Profiling resolution impact (Qwen2.5-7B, $k{=}8$). Higher resolution improves allocation quality at increased profiling cost.}\n\\label{tab:profiling_resolution}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nResolution & PPL & Detected Heads & Time (min) \\\\\n\\midrule\nLow-res ($16 \\times 512$)  & 11.23 & 37/112  & $\\sim$10 \\\\\nHigh-res ($64 \\times 2048$) & 10.91 & 100/112 & 65.5 \\\\\nUniform 4-bit & 15.45 & N/A & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHigh-resolution profiling reduces PPL from 11.23 to 10.91 ($-2.8\\%$), detecting sensitivity in 100/112 heads versus 37/112 for low-resolution.\nHowever, even low-resolution profiling yields a 27.3\\% improvement over uniform 4-bit (11.23 vs 15.45), suggesting that approximate profiling suffices for the primary benefit.\nThe 65.5-minute profiling cost at high resolution is a practical consideration; we note this as an engineering tradeoff rather than a fundamental limitation.\n\n\\subsection{L0 Exclusion Ablation}\n\nOn Qwen2.5-7B, Layer 0 heads exhibit a $26\\times$ dominance ratio in sensitivity delta.\nWe test whether explicit L0 exclusion (hard-coding L0 heads to 8-bit) is necessary, or whether the solver discovers L0 sensitivity automatically from profiling data.\n\n\\begin{table}[h]\n\\centering\n\\caption{L0 exclusion ablation (Qwen2.5-7B, budget$=0.25$). The solver automatically assigns 8-bit to all 4 L0 heads.}\n\\label{tab:l0_ablation}\n\\begin{tabular}{@{}lrll@{}}\n\\toprule\nCondition & PPL & L0 Bit-width & Note \\\\\n\\midrule\nMCKP + L0 exclusion + $k{=}8$ & 10.91 & 8-bit (hard-coded) & Original \\\\\nMCKP + $k{=}8$ only & 10.91 & 8-bit (solver-discovered) & Automatic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe solver automatically assigns 8-bit to all 4 L0 heads, producing identical PPL.\nThis confirms that the profiling-based approach correctly identifies L0 sensitivity without manual intervention, though we note this has only been verified on Qwen2.5-7B where L0 dominance is extreme ($26\\times$).\n\n\\subsection{K/V Separation}\n\nWe test whether treating Key and Value heads as independent MCKP items with separate budgets improves over joint K$=$V treatment (Table~\\ref{tab:kv_sep}).\n\n\\begin{table}[h]\n\\centering\n\\caption{K/V separation vs joint treatment (Qwen2.5-7B, $k{=}8$). Separation is worse due to K-cache compounding.}\n\\label{tab:kv_sep}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nMethod & PPL & K 2-bit & V 2-bit \\\\\n\\midrule\nJoint K$=$V ($k{=}8$) & 10.91 & 8 & 0 \\\\\nK/V Separation & 11.22 & 16 & 0 \\\\\nUniform 4-bit & 15.45 & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nK/V separation is worse ($+0.31$ PPL) because it allows 16 K-heads at 2-bit, exceeding the safe range of $k \\le 8$ and triggering K-cache compounding.\nV-heads are assigned uniform 4-bit under both settings.\nThis suggests that K-cache is more sensitive to 2-bit compounding than V-cache, and that a single joint cardinality constraint is preferable.\n\n\\subsection{Heuristic Baselines}\n\nWe compare constrained MCKP against simpler allocation strategies: L0-random (protect L0, randomly assign remaining 2-bit heads) and naive positional (assign 2-bit by layer position).\n\n\\begin{table}[h]\n\\centering\n\\caption{MCKP vs heuristic baselines (budget$=0.25$). MCKP consistently outperforms random constraint-respecting allocation.}\n\\label{tab:heuristic_baselines}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nModel & MCKP & L0-random (median) & Naive Positional & Uniform \\\\\n\\midrule\nQwen2.5-7B  & 10.91 & 11.52 & 12.23 & 15.45 \\\\\nLlama-3.1-8B & 8.45 & 10.04 & 9.94 & 8.47 \\\\\nMistral-7B-v0.3 & 7.16 & 7.59 & 7.48 & 7.13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMCKP outperforms L0-random by 5.2\\% (Qwen), 15.8\\% (Llama), and 5.7\\% (Mistral) in PPL, demonstrating that profiling-based allocation provides optimization value within the constrained feasible set.\nThe large seed variance in L0-random (Qwen std$=0.47$, Llama std$=1.03$) indicates that the specific choice of 2-bit heads matters significantly.\n\n\\subsection{Cross-Dataset Calibration Robustness}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-dataset calibration agreement ($>$96\\% across 3 architectures). Profiling-based sensitivity ranking is robust to calibration source.}\n\\label{tab:cross_dataset}\n\\begin{tabular}{@{}lrrl@{}}\n\\toprule\nModel & Agreement & Same-domain PPL & Cross-domain PPL \\\\\n\\midrule\nQwen2.5-7B  & 108/112 (96.4\\%) & 11.29 & 20.56 \\\\\nLlama-3.1-8B & 250/256 (97.7\\%) & 8.45 & 8.65 \\\\\nMistral-7B-v0.3 & 247/256 (96.5\\%) & 7.16 & 7.19 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCalibrating on C4 instead of WikiText-2 produces $>$96\\% identical head assignments across all three architectures, indicating that per-head sensitivity ranking is an architectural property rather than a dataset-dependent artifact.\nThe cross-domain PPL gap is minimal for Llama (0.20) and Mistral (0.03), though larger for Qwen (9.27), reflecting Qwen's higher sensitivity to calibration domain.\n\n\\subsection{Multi-Seed Stability}\n\n\\begin{table}[h]\n\\centering\n\\caption{Multi-seed PPL stability (Qwen2.5-7B, $k{=}8$, 3 seeds). Bit distribution is consistent across seeds.}\n\\label{tab:multi_seed}\n\\begin{tabular}{@{}lrl@{}}\n\\toprule\nSeed & PPL & Bit Distribution \\\\\n\\midrule\n0 & 11.02 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n1 & 10.90 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n2 & 11.05 & $\\{2{:}8, 4{:}100, 8{:}4\\}$ \\\\\n\\midrule\nMean $\\pm$ std & $10.99 \\pm 0.065$ & consistent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 95\\% confidence interval $[10.86, 11.12]$ is well below uniform 4-bit (15.45), confirming that the improvement is statistically robust.\nBit distribution is identical across all seeds, and 90.2\\% of head allocations agree across all three seeds.\n\n\n%% ============================================================\n%% 6  WHEN DOES NON-UNIFORM ALLOCATION HELP?\n%% ============================================================\n\\section{When Does Non-Uniform Allocation Help?}\n\\label{sec:when_helps}\n\n\\subsection{Cross-Architecture Downstream Evaluation}\n\nTable~\\ref{tab:downstream} presents downstream task results across 5 architectures under $4\\times$ compression.\nOnly Qwen2.5-7B (spread sensitivity pattern) shows consistent downstream gains (+1.25 to +4.00pp).\nThe remaining 4 architectures show minor degradation: Yi-1.5 $-0.77$pp, Llama $-0.99$pp, Mistral $-0.48$pp, Gemma-2 $+0.14$pp (noise).\n\n\\begin{table}[h]\n\\centering\n\\caption{Downstream evaluation ($4\\times$ compression, 0-shot). MCKP benefits only Qwen2.5-7B (spread pattern). ARC-Challenge shows the largest per-task sensitivity to allocation strategy across all non-Spread models.}\n\\label{tab:downstream}\n\\begin{tabular}{@{}llrrrrl@{}}\n\\toprule\nModel & Pattern & ARC-C $\\Delta$ & HellaSwag $\\Delta$ & PIQA $\\Delta$ & WinoGrande $\\Delta$ & Avg $\\Delta$ \\\\\n\\midrule\nQwen2.5-7B & Spread & +3.16pp & +4.00pp & +1.25pp & +1.97pp & +2.60pp \\\\\nYi-1.5-9B & Spike & $-$3.24pp & $-$0.60pp & $-$0.33pp & +1.27pp & $-$0.77pp \\\\\nLlama-3.1-8B & Spike & $-$2.65pp & $-$0.14pp & $-$0.65pp & $-$0.15pp & $-$0.99pp \\\\\nMistral-7B-v0.3 & Flat & $-$1.19pp & --- & --- & --- & $-$0.48pp \\\\\nGemma-2-9B & Flat & $-$0.17pp & --- & --- & --- & +0.14pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nARC-Challenge shows the largest per-task sensitivity to allocation strategy, with consistent degradation across non-Spread models (Yi $-3.24$pp, Llama $-2.65$pp, Mistral $-1.19$pp).\nThis is consistent with ARC-Challenge's reliance on multi-step reasoning, where subtle KV cache quantization errors accumulate.\n\n\\subsection{Sensitivity Distribution Taxonomy}\n\nWe identify three sensitivity distribution shapes that predict allocation benefit:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Spread} (Qwen2.5-7B): Multiple heads with cross-bitwidth sensitivity gradients. L0 cluster of 4 heads with $26\\times$ dominance ratio. Concentration$=0.61$, $t_1/t_5=0.57$. MCKP benefits: $+27.3\\%$ PPL, $+2.6$pp downstream.\n\n\\item \\textbf{Spike} (Yi-1.5-9B, Llama-3.1-8B): Single extreme outlier dominates. Yi L4H3 accounts for 64\\% of total delta. Solver assigns 8-bit to the outlier but cannot differentiate remaining heads. Concentration high (Yi $0.71$) but $t_1/t_5$ also high ($0.90$). No MCKP benefit.\n\n\\item \\textbf{Flat} (Mistral-7B-v0.3, Gemma-2-9B): Near-homogeneous sensitivity. Profiler reports near-zero inter-head differences (Mistral concentration$=0.22$, Gemma-2 $0.23$). Every 2-bit head hurts equally; non-uniform allocation is futile.\n\\end{itemize}\n\n\\paragraph{The spike--spread distinction.}\nYi-1.5 (GQA 8:1, concentration$=0.71$) and Qwen (GQA 7:1, concentration$=0.61$) illustrate why GQA ratio and concentration alone are insufficient predictors.\nYi has higher GQA and higher concentration than Qwen, yet shows no benefit.\nThe critical difference is distribution \\emph{shape}: Qwen's L0 \\emph{cluster} of sensitive heads creates optimization opportunities, while Yi's single extreme outlier cannot be exploited.\n\n\\subsection{Diagnostic Validation}\n\nThe 2-metric diagnostic (concentration $\\gtrsim 0.50$ AND $t_1/t_5 \\lesssim 0.70$) correctly classifies all 9 tested models:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item Qwen2.5-7B: $c{=}0.61$, $t_1/t_5{=}0.57$ $\\to$ spread $\\to$ benefit predicted $\\to$ \\textbf{correct} (+27.3\\%)\n\\item Yi-1.5-9B: $c{=}0.71$, $t_1/t_5{=}0.90$ $\\to$ spike $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($\\approx 0\\%$)\n\\item Llama-3.1-8B: $c{=}0.57$, $t_1/t_5{=}0.85$ $\\to$ spike $\\to$ no benefit predicted $\\to$ \\textbf{correct} (+0.2\\%)\n\\item Mistral-7B-v0.3: $c{=}0.22$, $t_1/t_5{=}$--- $\\to$ flat $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($-0.5\\%$)\n\\item Gemma-2-9B: $c{=}0.23$, $t_1/t_5{=}0.38$ $\\to$ flat $\\to$ no benefit predicted $\\to$ \\textbf{correct} ($-0.3\\%$)\n\\end{itemize}\nWe emphasize that $n{=}9$ provides a consistent pattern, not a statistical claim.\n\n%% ============================================================\n%% 7  RUNTIME ANALYSIS\n%% ============================================================\n\\section{Runtime Analysis}\n\\label{sec:runtime}\n\n\\begin{table}[h]\n\\centering\n\\caption{Runtime benchmark (Qwen2.5-7B, seq\\_len$=$2048). Mixed-precision incurs 8.5\\% throughput overhead vs uniform 4-bit due to per-head dequantization.}\n\\label{tab:runtime}\n\\begin{tabular}{@{}lrrrr@{}}\n\\toprule\nMethod & Prefill (ms) & Decode (ms) & Throughput (tok/s) & Memory (MB) \\\\\n\\midrule\nBF16 (no quant.) & 45.86 & 33.78 & 29.6 & 21 \\\\\nUniform 4-bit & 54.25 & 42.46 & 23.6 & 5.25 \\\\\nConstrained MCKP & 57.03 & 46.09 & 21.8 & 5.25 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMixed-precision MCKP incurs an 8.5\\% throughput reduction versus uniform 4-bit (21.8 vs 23.6 tok/s), stemming from per-head dequantization kernel overhead.\nThe MCKP solver itself is negligible (0.005s).\nThis overhead is an engineering limitation of the current implementation: a fused mixed-precision dequantization kernel could eliminate it.\nThe memory footprint is identical ($4\\times$ compression) since the average bit-width remains the same.\n\nFor memory-bound scenarios (long context, large batch sizes), the $4\\times$ memory reduction enables deployments that BF16 cannot support.\nOn 7/8 architectures where non-uniform allocation provides no PPL benefit, the 8.5\\% throughput cost is pure overhead; the diagnostic (Section~\\ref{sec:when_helps}) helps practitioners avoid this cost by recommending uniform 4-bit when appropriate.\n\n%% ============================================================\n%% 8  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present an empirical analysis of per-head KV cache quantization on hardware-aligned bit-widths $\\{2,4,8,16\\}$, identifying three findings:\n\n\\textbf{(1)} 2-bit quantization distortions compound non-additively, causing all tested unconstrained solvers to underperform uniform 4-bit across 8 architectures.\nThis compounding is superlinear after $k{\\approx}16$ simultaneous 2-bit heads and exponential after $k{\\approx}48$.\n\n\\textbf{(2)} A cardinality constraint ($\\le k$ heads at 2-bit, $k{\\le}8$) prevents compounding across all tested architectures and makes solver choice irrelevant (greedy$=$MCKP, $\\Delta{=}0.0000$).\nPractitioners need only add one integer parameter to existing pipelines.\n\n\\textbf{(3)} Under moderate compression, only 1/8 architectures benefits from non-uniform allocation.\nA 2-metric diagnostic (9/9 correct) tells practitioners when to use profiling-based allocation versus uniform 4-bit.\n\n\\paragraph{Limitations.}\nOur experiments are limited to 7B--14B scale models; scaling behavior to 70B+ models remains an open question (our 72B profiling attempt was terminated due to resource constraints).\nMulti-seed confidence intervals are reported for PPL (std$=$0.065) but not for all downstream tasks.\nThe 8.5\\% throughput overhead of the current mixed-precision implementation could be eliminated with optimized kernels but represents a practical concern.\nThe diagnostic threshold values ($c{\\gtrsim}0.50$, $t_1/t_5{\\lesssim}0.70$) are derived from $n{=}9$ models and should be treated as an empirical observation, not a statistically validated rule.\n\n\\bibliography{references}\n\\bibliographystyle{plain}\n\n\\begin{thebibliography}{10}\n\\bibitem{hooper2024kvquant}\nColeman Hooper, Sehoon Kim, Haonan Mohber, et al.\n\\newblock KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization.\n\\newblock \\emph{arXiv preprint arXiv:2401.18079}, 2024.\n\n\\bibitem{liu2024kivi}\nZirui Liu, Jiayi Yuan, Hongye Jin, et al.\n\\newblock KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache.\n\\newblock \\emph{arXiv preprint arXiv:2402.02750}, 2024.\n\n\\bibitem{dong2024qaq}\nHaowen Dong, Jiaqi Zheng, et al.\n\\newblock QAQ: Quality Adaptive Quantization for LLM KV Cache.\n\\newblock \\emph{arXiv preprint arXiv:2403.04643}, 2024.\n\n\\bibitem{ratequant2024}\nRateQuant Authors.\n\\newblock RateQuant: Rate-Distortion Optimal KV Cache Quantization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem{nagel2020up}\nMarkus Nagel, Rana Ali Amjad, Mart van Baalen, et al.\n\\newblock Up or Down? Adaptive Rounding for Post-Training Quantization.\n\\newblock \\emph{ICML}, 2020.\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d57d7885-d1fa-486a-98dc-4f7b8be182d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "33672d26-5373-432a-9ea3-753a69614b30",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Tool call

_source line 25 · 2026-05-16T02:41:10.137Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DKPd31ZEthfqPrZjdpjyh3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33672d26-5373-432a-9ea3-753a69614b30",
  "isSidechain": false,
  "requestId": "req_011Cb5UYM9DjmGrTpcKuCjvf",
  "type": "assistant",
  "uuid": "027f56ad-f9da-4bd9-ab51-525615d8ea60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MKu7cnyace8gVVG8q59Avg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11506,
      "cache_read_input_tokens": 49999,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 49999,
          "cache_creation_input_tokens": 11506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11506
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

_source line 26 · 2026-05-16T02:41:11.863Z_

<details><summary>↩ Tool result · `toolu_01DKPd31ZEthfqPrZjdpjyh3`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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

LaTeX Warning: Citation `hooper2024kvquant' on page 1 undefined on input line 4
1.


LaTeX Warning: Citation `liu2024kivi' on page 1 undefined on input line 41.


LaTeX Warning: Citation `dong2024qaq' on page 1 undefined on input line 41.


LaTeX Warning: Reference `tab:compounding_sweep' on page 1 undefined on input l
ine 52.


LaTeX Warning: Reference `tab:solver_equivalence' on page 1 undefined on input 
line 56.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Citation `ratequant2024' on page 2 undefined on input line 64.


LaTeX Warning: Citation `liu2024kivi' on page 2 undefined on input line 74.


LaTeX Warning: Citation `hooper2024kvquant' on page 2 undefined on input line 7
5.


LaTeX Warning: Citation `dong2024qaq' on page 2 undefined on input line 76.


LaTeX Warning: Citation `ratequant2024' on page 2 undefined on input line 79.


LaTeX Warning: Citation `nagel2020up' on page 2 undefined on input line 85.


LaTeX Warning: Reference `tab:profiling_resolution' on page 2 undefined on inpu
t line 111.

[2]

LaTeX Warning: Reference `sec:compounding' on page 3 undefined on input line 12
2.


LaTeX Warning: Reference `tab:compounding_sweep' on page 3 undefined on input l
ine 125.


LaTeX Warning: Reference `sec:when_helps' on page 3 undefined on input line 139
.


LaTeX Warning: Reference `tab:compounding_sweep' on page 3 undefined on input l
ine 150.


LaTeX Warning: `h' float specifier changed to `ht'.

[3]

LaTeX Warning: Reference `tab:cross_arch' on page 4 undefined on input line 198
.


Overfull \hbox (4.63718pt too wide) in paragraph at lines 217--220
 []\T1/cmr/bx/n/10.95 Llama-3.1-8B.[] \T1/cmr/m/n/10.95 The solver nat-u-rally 
se-lects only 2 heads for 2-bit (dis-tri-bu-tion $\OMS/cmsy/m/n/10.95 f\OT1/cmr
/m/n/10.95 2[]2\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 4[]253\OML/cmm/m/it/10.
95 ; \OT1/cmr/m/n/10.95 8[]1\OMS/cmsy/m/n/10.95 g$\T1/cmr/m/n/10.95 ),

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `tab:solver_equivalence' on page 4 undefined on input 
line 244.

[4]

LaTeX Warning: Reference `tab:oracle' on page 5 undefined on input line 270.


LaTeX Warning: Reference `tab:budget_sweep' on page 5 undefined on input line 2
92.

[5]

LaTeX Warning: Reference `tab:kv_sep' on page 6 undefined on input line 357.

[6] [7]

LaTeX Warning: Reference `tab:downstream' on page 8 undefined on input line 451
.

[8]

LaTeX Warning: Reference `sec:when_helps' on page 9 undefined on input line 531
.

[9]
No file paper.bbl.
[10] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam
10.pfb>
Output written on paper.pdf (10 pages, 251262 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
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

LaTeX Warning: `h' float specifier changed to `ht'.

[3]
Overfull \hbox (4.63718pt too wide) in paragraph at lines 217--220
 []\T1/cmr/bx/n/10.95 Llama-3.1-8B.[] \T1/cmr/m/n/10.95 The solver nat-u-rally 
se-lects only 2 heads for 2-bit (dis-tri-bu-tion $\OMS/cmsy/m/n/10.95 f\OT1/cmr
/m/n/10.95 2[]2\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 4[]253\OML/cmm/m/it/10.
95 ; \OT1/cmr/m/n/10.95 8[]1\OMS/cmsy/m/n/10.95 g$\T1/cmr/m/n/10.95 ),

LaTeX Warning: `h' float specifier changed to `ht'.

[4] [5] [6] [7] [8] [9]
No file paper.bbl.
[10] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home
/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho
me/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
sy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam
10.pfb>
Output written on paper.pdf (10 pages, 254446 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "027f56ad-f9da-4bd9-ab51-525615d8ea60",
  "isSidechain": false,
  "promptId": "4daa24be-f4bb-49cb-aca1-05083e2670a2",
  "type": "user",
  "uuid": "5c5e96ae-ab92-44e2-be70-d065464be5cd",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `hooper2024kvquant' on page 1 undefined on input line 4\n1.\n\n\nLaTeX Warning: Citation `liu2024kivi' on page 1 undefined on input line 41.\n\n\nLaTeX Warning: Citation `dong2024qaq' on page 1 undefined on input line 41.\n\n\nLaTeX Warning: Reference `tab:compounding_sweep' on page 1 undefined on input l\nine 52.\n\n\nLaTeX Warning: Reference `tab:solver_equivalence' on page 1 undefined on input \nline 56.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Citation `ratequant2024' on page 2 undefined on input line 64.\n\n\nLaTeX Warning: Citation `liu2024kivi' on page 2 undefined on input line 74.\n\n\nLaTeX Warning: Citation `hooper2024kvquant' on page 2 undefined on input line 7\n5.\n\n\nLaTeX Warning: Citation `dong2024qaq' on page 2 undefined on input line 76.\n\n\nLaTeX Warning: Citation `ratequant2024' on page 2 undefined on input line 79.\n\n\nLaTeX Warning: Citation `nagel2020up' on page 2 undefined on input line 85.\n\n\nLaTeX Warning: Reference `tab:profiling_resolution' on page 2 undefined on inpu\nt line 111.\n\n[2]\n\nLaTeX Warning: Reference `sec:compounding' on page 3 undefined on input line 12\n2.\n\n\nLaTeX Warning: Reference `tab:compounding_sweep' on page 3 undefined on input l\nine 125.\n\n\nLaTeX Warning: Reference `sec:when_helps' on page 3 undefined on input line 139\n.\n\n\nLaTeX Warning: Reference `tab:compounding_sweep' on page 3 undefined on input l\nine 150.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\n\nLaTeX Warning: Reference `tab:cross_arch' on page 4 undefined on input line 198\n.\n\n\nOverfull \\hbox (4.63718pt too wide) in paragraph at lines 217--220\n []\\T1/cmr/bx/n/10.95 Llama-3.1-8B.[] \\T1/cmr/m/n/10.95 The solver nat-u-rally \nse-lects only 2 heads for 2-bit (dis-tri-bu-tion $\\OMS/cmsy/m/n/10.95 f\\OT1/cmr\n/m/n/10.95 2[]2\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 4[]253\\OML/cmm/m/it/10.\n95 ; \\OT1/cmr/m/n/10.95 8[]1\\OMS/cmsy/m/n/10.95 g$\\T1/cmr/m/n/10.95 ),\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `tab:solver_equivalence' on page 4 undefined on input \nline 244.\n\n[4]\n\nLaTeX Warning: Reference `tab:oracle' on page 5 undefined on input line 270.\n\n\nLaTeX Warning: Reference `tab:budget_sweep' on page 5 undefined on input line 2\n92.\n\n[5]\n\nLaTeX Warning: Reference `tab:kv_sep' on page 6 undefined on input line 357.\n\n[6] [7]\n\nLaTeX Warning: Reference `tab:downstream' on page 8 undefined on input line 451\n.\n\n[8]\n\nLaTeX Warning: Reference `sec:when_helps' on page 9 undefined on input line 531\n.\n\n[9]\nNo file paper.bbl.\n[10] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam\n10.pfb>\nOutput written on paper.pdf (10 pages, 251262 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3]\nOverfull \\hbox (4.63718pt too wide) in paragraph at lines 217--220\n []\\T1/cmr/bx/n/10.95 Llama-3.1-8B.[] \\T1/cmr/m/n/10.95 The solver nat-u-rally \nse-lects only 2 heads for 2-bit (dis-tri-bu-tion $\\OMS/cmsy/m/n/10.95 f\\OT1/cmr\n/m/n/10.95 2[]2\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 4[]253\\OML/cmm/m/it/10.\n95 ; \\OT1/cmr/m/n/10.95 8[]1\\OMS/cmsy/m/n/10.95 g$\\T1/cmr/m/n/10.95 ),\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[4] [5] [6] [7] [8] [9]\nNo file paper.bbl.\n[10] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-di\nst/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam\n10.pfb>\nOutput written on paper.pdf (10 pages, 254446 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "027f56ad-f9da-4bd9-ab51-525615d8ea60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "5c5e96ae-ab92-44e2-be70-d065464be5cd",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Assistant

_source line 29 · 2026-05-16T02:41:24.762Z_

编译成功，10 页 PDF，无错误。

论文覆盖了 `experiment_data.json` 中全部 16 个实验：
- **Compounding sweep** → Table 1 + Section 4.1
- **Cross-architecture pipeline** (Qwen/Llama/Mistral) → Table 2 + Section 5.1
- **Mistral k-ablation** → Table 3
- **Solver equivalence** (greedy vs MCKP) → Table 4 + Section 5.2
- **Oracle comparison** → Table 5 + Section 5.3
- **Budget sweep** (2×/4×/8×) → Table 6 + Section 5.4
- **Profiling resolution** → Table 7 + Section 5.5
- **L0 exclusion ablation** → Table 8 + Section 5.6
- **K/V separation** → Table 9 + Section 5.7
- **Heuristic baselines** → Table 10 + Section 5.8
- **Cross-dataset calibration** → Table 11 + Section 5.9
- **Multi-seed stability** → Table 12 + Section 5.10
- **Downstream evaluation** (5 architectures) → Table 13 + Section 6.1
- **Runtime benchmark** → Table 14 + Section 7
- **70B profiling** → Limitations 段落
- **RateQuant greedy comparison** → 融入 solver equivalence 讨论
- **Head sensitivity visualization** → 融入 taxonomy 讨论

按 narrative guidance 要求做了 reframe：empirical analysis 前置，claim 措辞用 "consistent pattern across 8 architectures" 而非 "universal"，constraint 提供理论 justification（compounding non-additivity），downstream 1/8 结果诚实报告为 architecture-specific。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c5e96ae-ab92-44e2-be70-d065464be5cd",
  "isSidechain": false,
  "requestId": "req_011Cb5UYj6KxmYuWu8rx53mc",
  "type": "assistant",
  "uuid": "fbabcf7a-fca4-418a-9ebe-60dc99a2d0f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260516T021448/median",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XdrvmMD95s6zngHzwbgap",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7143,
      "cache_read_input_tokens": 61505,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 61505,
          "cache_creation_input_tokens": 7143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7143
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T021448 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts…",
  "leafUuid": "fbabcf7a-fca4-418a-9ebe-60dc99a2d0f7",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper from experiment data",
  "sessionId": "dc8fbc02-a351-42eb-9162-8abd7e156f3e"
}
```

---
