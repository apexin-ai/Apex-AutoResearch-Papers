# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/30fff989-e5a5-458f-9db4-12c70eff9bfe.jsonl`
- **Structured JSON:** [`55537dfb15430aa7ac29.json`](../../sessions/55/55537dfb15430aa7ac29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T17:15:28.817Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:15:28.817Z",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Capability trap 不再是 universal characterization，reframe 为 condition-dependent phenomenon。Title 改：'When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap'。从 pure negative 转 boundary-condition analysis。三条 claims 重构为：(a) positive boundary — 识别 capability trap 发生的 sufficient conditions (model capacity × domain formalizability × precision threshold)，(b) mechanism — oracle 仍证明 aggregation 有效性 + capability trap 解释多数失败条件，(c) diagnostic — C0 + constraint precision 联合 deployment framework（非单独 C0）。\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T17:15:28.821Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:15:28.821Z",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-17T17:15:28.841Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Capability trap 不再是 universal characterization，reframe 为 condition-dependent phenomenon。Title 改：'When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap'。从 pure negative 转 boundary-condition analysis。三条 claims 重构为：(a) positive boundary — 识别 capability trap 发生的 sufficient conditions (model capacity × domain formalizability × precision threshold)，(b) mechanism — oracle 仍证明 aggregation 有效性 + capability trap 解释多数失败条件，(c) diagnostic — C0 + constraint precision 联合 deployment framework（非单独 C0）。
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "1b2eaabd-e339-4def-a4f2-43314e56079f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T17:15:28.840Z_

```json
{
  "parentUuid": "1b2eaabd-e339-4def-a4f2-43314e56079f",
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
  "uuid": "ba9d48e3-cfc6-40f4-aa6c-2fba28a5cbaa",
  "timestamp": "2026-05-17T17:15:28.840Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T17:15:28.841Z_

```json
{
  "parentUuid": "ba9d48e3-cfc6-40f4-aa6c-2fba28a5cbaa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d26f7147-7781-4e01-af4b-2133cc6163cd",
  "timestamp": "2026-05-17T17:15:28.841Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
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
  "aiTitle": "Generate worst-tier simulated research paper",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Assistant

_source line 7 · 2026-05-17T17:15:32.278Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26f7147-7781-4e01-af4b-2133cc6163cd",
  "isSidechain": false,
  "requestId": "req_011Cb8X2UN5KyAYpaohxCXtT",
  "type": "assistant",
  "uuid": "a3ff21bf-6dda-4567-9e62-c7f6d0644d43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161twftq3t9vHccUQdnFchB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12476
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

_source line 8 · 2026-05-17T17:15:32.895Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FY7YbwnFg3xhsoZzzy5cBb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3ff21bf-6dda-4567-9e62-c7f6d0644d43",
  "isSidechain": false,
  "requestId": "req_011Cb8X2UN5KyAYpaohxCXtT",
  "type": "assistant",
  "uuid": "26e5af40-2300-4fd2-b5d2-5496d2dab60a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161twftq3t9vHccUQdnFchB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12476
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

_source line 9 · 2026-05-17T17:15:33.148Z_

<details><summary>↩ Tool result · `toolu_01FY7YbwnFg3xhsoZzzy5cBb`</summary>

```text
1	[
2	  {
3	    "name": "sica_k_ablation_14b",
4	    "description": "K sensitivity (K=6,8,11,12,16,20) on D012 60 questions",
5	    "results": {
6	      "K6_sica": 0.75,
7	      "K6_sc": 0.733,
8	      "K6_gap_pp": 1.7,
9	      "K8_sica": 0.767,
10	      "K8_sc": 0.75,
11	      "K8_gap_pp": 1.7,
12	      "K11_sica": 0.767,
13	      "K11_sc": 0.733,
14	      "K11_gap_pp": 3.3,
15	      "K12_sica": 0.733,
16	      "K12_sc": 0.7,
17	      "K12_gap_pp": 3.3,
18	      "K16_sica": 0.75,
19	      "K16_sc": 0.733,
20	      "K16_gap_pp": 1.7,
21	      "K20_sica": 0.733,
22	      "K20_sc": 0.717,
23	      "K20_gap_pp": 1.7,
24	      "K11_mcnemar_p": 0.157,
25	      "best_K_gap_pp": 3.3,
26	      "odd_K_gap_gt_0": true
27	    },
28	    "tables": [
29	      "T_appendix_K_ablation: K × SICA/SC accuracy matrix"
30	    ],
31	    "figures": [],
32	    "analysis": "K=11 odd-K positive gap 是 worst 档核心证据之一。如果 gap 仅存在于 even-K（tiebreak），可以 dismiss；但 odd-K +3.3pp 意味着 constraint exclusion 有 genuine discriminative value on this 60-question subset。Reframe: SICA has weak positive signal on D012-subset (Qwen-14B × formal logic × n=60) that doesn't survive power scaling (exp-001 n=804 shows +0.3pp)，但 heterogeneity 暗示 condition-dependence。\n\nWorst 档要求 universality 被打破。K=11（odd-K）仍出现 +3.3pp，证明 SICA 的增益不仅来自 tiebreak——odd-K 无精确平局，但 SICA 仍能通过 constraint exclusion 翻转少数问题。这打破了 'SICA value is purely tiebreak-driven' 叙事。虽然 p>0.1 因 n=60 power 不足，但方向一致且 K=11/K=12 两个 K 值重复 +3.3pp。需在论文中 reframe 为 'condition-dependent benefit at certain K ranges' 而非 'universally zero'。"
33	  },
34	  {
35	    "name": "tiebreak_baseline_analysis",
36	    "description": "SICA vs SC-random-tiebreak vs SC-deterministic comparison",
37	    "results": {
38	      "sica_tiebreak_win_rate": 0.8,
39	      "random_tiebreak_win_rate": 0.5,
40	      "alphabetical_tiebreak_win_rate": 0.6,
41	      "first_seen_tiebreak_win_rate": 0.4,
42	      "n_tied_questions": 5,
43	      "tied_fraction": 0.083,
44	      "sica_net_gain_from_tiebreak_pp": 2.5,
45	      "sica_gain_beyond_tiebreak_pp": 1.0
46	    },
47	    "tables": [
48	      "T_tiebreak: Tiebreak method × win rate on tied questions"
49	    ],
50	    "figures": [],
51	    "analysis": "Tiebreak 分析在 worst 档下支持 'SICA has genuine constraint signal on subset' 叙事。但 effect size 太小 to be practically meaningful（5 个 tie 中多赢 1-2 个 = 1-3pp on full set）。Paper 需 acknowledge SICA has weak positive signal in favorable conditions 而非 zero。\n\nWorst 档下，tiebreak 分析揭示 SICA 的 tiebreak 优势（80% win rate on ties）AND 有少量 non-tie flips。5/60 个问题有 exact tie，SICA 在其中 4/5 选对；另外还有 1 个非平局问题被 constraint exclusion 翻转。这意味着 SICA mechanism 不完全 reducible to tiebreak——有微弱但存在的 exclusion 效应。在 n=60 subset 上 beyond-tiebreak gain ≈ 1pp 不显著，但 existence 本身打破 'purely tiebreak' framing。"
52	  },
53	  {
54	    "name": "sica_7b_scaling",
55	    "description": "Qwen2.5-7B-Instruct on 60 questions, testing weaker model → higher C0 → larger gap",
56	    "results": {
57	      "sica_accuracy": 0.617,
58	      "sc_accuracy": 0.567,
59	      "delta_pp": 5.0,
60	      "mcnemar_p": 0.083,
61	      "multi_candidate_rate": 0.717,
62	      "c0_pct": 71.7,
63	      "extraction_rate": 0.82,
64	      "answer_extraction_rate": 0.91,
65	      "constraint_precision_mean": 0.54,
66	      "discordant_sica_wins": 4,
67	      "discordant_sc_wins": 1,
68	      "wall_time_min": 45
69	    },
70	    "tables": [
71	      "T1_main: add Qwen-7B row"
72	    ],
73	    "figures": [],
74	    "analysis": "7B 的 +5pp 是 worst 档的 smoking gun。虽然 n=60 power 不足以达到 p<0.05，但方向与 LLaMA-8B exp-011 FOLIO +10pp 一致。Pattern emerges: weaker models on formal logic domains show positive gaps。需 reframe capability trap 为 'high-capacity models extract non-discriminative constraints; low-capacity models paradoxically benefit because their higher error rate creates more room for constraint-based correction'。\n\nWorst 档的核心打破机制之一：weaker model (7B) 产生更高 C0 (71.7%) 且 delta=+5.0pp（p=0.083，接近 significance）。这暗示 capability trap 是 capacity-dependent 而非 universal。7B 模型 extraction quality 低（precision~0.54），但因为 baseline accuracy 也低（56.7%），constraints 的微弱 discriminative signal 足以翻转几个问题。C0-gap 正相关在 experiment-level 出现（7B: C0=72%, Δ=+5; 14B: C0=38%, Δ=+0.3; 72B: C0~15%, Δ≈0），产生 r=0.3-0.4 的 condition-level correlation。这打破了 'no correlation between diversity and benefit' 叙事。"
75	  },
76	  {
77	    "name": "qwq_32b_operating_regime",
78	    "description": "QwQ-32B negative results formatted for paper",
79	    "results": {
80	      "qwq_aggregate_c0_effective_pct": 3.6,
81	      "qwq_aime_delta_pp": 0,
82	      "qwq_proofwriter_delta_pp": 0,
83	      "qwq_folio_delta_pp": 0,
84	      "total_problems": 46,
85	      "sica_degenerate_to_sc": true,
86	      "reasoning_model_c0_threshold_confirmed": true
87	    },
88	    "tables": [
89	      "T1_main: QwQ-32B row (C0<5%, SICA≡SC)"
90	    ],
91	    "figures": [],
92	    "analysis": "QwQ 数据在 worst 档是 safe asset——不会产生 surprise。但 reviewer concern #4 ('only one reasoning model') 在 worst 档更尖锐：如果 instruction-scale 条件显示 condition-dependent gains，reviewer 会问 'what about reasoning models on tasks where they have moderate C0?' 可能需要 QwQ on easier tasks where it's not 100% accurate。\n\nQwQ-32B 在 worst 档下不变：C0<5%，SICA≡SC。Full reasoning model 的 deterministic chain 消除 diversity，SICA 结构性退化。这在 worst 档仍成立因为 worst 档打破的是 instruction-scale 模型的 universality，不是 reasoning model 的 behavior。QwQ 数据仍支持 Claim 3 (C0&lt;threshold → degenerate)。问题是 n=46 across heterogeneous tasks，reviewer 可能要求更多 reasoning model data points。"
93	  },
94	  {
95	    "name": "c0_diagnostic_validation",
96	    "description": "Plot C0 vs SICA-SC gap across all conditions",
97	    "results": {
98	      "n_conditions": 12,
99	      "pearson_r_c0_gap": 0.38,
100	      "pearson_p": 0.08,
101	      "spearman_rho": 0.42,
102	      "spearman_p": 0.06,
103	      "c0_below_5_all_zero_gap": true,
104	      "c0_above_30_gap_range_pp": [
105	        -3.3,
106	        6.7
107	      ],
108	      "c0_above_30_mean_gap_pp": 1.8,
109	      "linear_model_r2": 0.14,
110	      "c0_threshold_5_specificity": 1.0,
111	      "c0_threshold_5_sensitivity": 0.0
112	    },
113	    "tables": [
114	      "T_c0_diagnostic: condition × C0 × gap × n"
115	    ],
116	    "figures": [],
117	    "analysis": "Moderate correlation (r=0.38) 是 worst 档的 nuisance finding。不足以 claim C0 is predictive (p=0.08, R²=0.14)，但足以让 reviewer 质疑 'C0 is uninformative beyond threshold'。Paper 需 reframe Claim 3 为 joint diagnostic (C0 + constraint precision) 而非 C0 alone。\n\nWorst 档下，C0 与 gap 的 experiment-level correlation 是 moderate positive (r=0.38, p=0.08)，接近 significance。这与 best/mid 档 (r≈0.15, p=0.74) 截然不同。原因：7B 和 LLaMA-8B 条件的 high C0 + positive gap 拉高了 correlation。但 R²=0.14 说明 C0 只解释 14% variance——仍是 'necessary but insufficient' 但带有 weak positive predictive direction。Claim 3 需 reframe：C0 不仅是 binary gate (C0<5% → degenerate) 而是有 weak gradient effect（higher C0 correlates with slightly higher expected gap），但 variance 太大 for deployment use。"
118	  },
119	  {
120	    "name": "sica_72b_awq",
121	    "description": "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions",
122	    "results": {
123	      "sica_accuracy": 0.817,
124	      "sc_accuracy": 0.833,
125	      "delta_pp": -1.7,
126	      "multi_candidate_rate": 0.15,
127	      "c0_pct": 15.0,
128	      "extraction_rate": 0.93,
129	      "answer_extraction_rate": 1.0,
130	      "constraint_precision_mean": 0.61,
131	      "discordant_sica_wins": 0,
132	      "discordant_sc_wins": 1,
133	      "mcnemar_p": 1.0,
134	      "wall_time_min": 180
135	    },
136	    "tables": [
137	      "T1_main: Qwen-72B row",
138	      "T_precision: model size vs constraint precision"
139	    ],
140	    "figures": [],
141	    "analysis": "72B 结果支持 within-family scaling narrative：model capacity ↑ → C0 ↓ + precision ↑，两者抵消使 gap≈0。但 combined with 7B (C0=72%, precision=0.54, gap=+5pp)，creates a capacity-dependent boundary story。Worst 档的 paper structure 需 show this scaling dimension explicitly。\n\n72B 高 baseline (83.3%) 导致 C0 低 (15%)——模型太 confident，answer space 近 unanimous。SICA 轻微 negative (-1.7pp) 因仅 9 个 multi-candidate 问题，constraint exclusion 在 1 个问题上错误翻转。Interesting finding for worst 档：constraint precision 在 72B 较高 (0.61 vs 14B 的 0.52)——bigger model extracts better constraints，但 C0 太低 to matter。这支持 reframed story：capability trap 有两个 regime：(1) weak model = high C0 + low precision = marginal benefit，(2) strong model = low C0 + high precision = degenerate。Sweet spot 可能存在于 intermediate capacity × formal domain。"
142	  },
143	  {
144	    "name": "constraint_quality_case_studies",
145	    "description": "Qualitative analysis of extracted constraints on 5-10 representative questions",
146	    "results": {
147	      "n_analyzed": 10,
148	      "high_precision_cases": 3,
149	      "low_precision_cases": 5,
150	      "mixed_precision_cases": 2,
151	      "high_precision_constraint_example": "ForAll(x, Human(x) -> Mortal(x)) correctly excludes wrong answer",
152	      "low_precision_example": "Exists(x, Answer(x, 'True')) - tautologically matches any answer",
153	      "bimodal_finding": true,
154	      "precision_gt_0p7_fraction": 0.3,
155	      "precision_lt_0p4_fraction": 0.5
156	    },
157	    "tables": [],
158	    "figures": [],
159	    "analysis": "Case studies 在 worst 档是 double-edged：证明 mechanism CAN work (high-precision cases exist) 同时解释 WHY aggregate 结果 null (diluted by majority low-precision)。Paper 需 position as 'the capability trap is not a fundamental impossibility but a current extraction quality gap with identifiable conditions for success'。\n\nWorst 档下 case study 揭示 bimodal pattern：30% 的问题有 precision>0.7 的 genuinely discriminative constraints（特别是 FOLIO 中有明确 logical structure 的问题），50% 的问题 constraints 基本 random (precision<0.4)。这支持 'capability trap 非 uniform' 假设——部分问题 constraints 有效但被 low-precision 多数稀释。Qualitative evidence 展示 failure mode diversity：(a) 语义空约束 (∀x, True)，(b) 约束复述答案 (circular)，(c) 约束正确但对所有答案等效 (non-discriminative despite being valid FOL)。"
160	  },
161	  {
162	    "name": "sica_llama_8b",
163	    "description": "LLaMA-3.1-8B-Instruct on D012 60 questions",
164	    "results": {
165	      "sica_accuracy": 0.683,
166	      "sc_accuracy": 0.617,
167	      "delta_pp": 6.7,
168	      "mcnemar_p": 0.109,
169	      "multi_candidate_rate": 0.617,
170	      "c0_pct": 61.7,
171	      "extraction_rate": 0.856,
172	      "answer_extraction_rate": 0.896,
173	      "contradiction_rate": 0.053,
174	      "discordant_sica_wins": 5,
175	      "discordant_sc_wins": 1,
176	      "folio_sica": 0.7,
177	      "folio_sc": 0.6,
178	      "folio_delta_pp": 10.0,
179	      "proofwriter_sica": 0.633,
180	      "proofwriter_sc": 0.6,
181	      "proofwriter_delta_pp": 3.3,
182	      "wall_time_min": 66
183	    },
184	    "tables": [
185	      "T1_main: LLaMA-8B row with per-domain breakdown"
186	    ],
187	    "figures": [],
188	    "analysis": "LLaMA-8B FOLIO +10pp 是 worst 档最棘手的数据点。两种解释：(1) n=30 抽样 variance (SE≈9pp，+10pp 在 1σ 内)，(2) D012 的 30 题偏向 high-formalizability 子集。Worst 档假设 (2) 部分成立——exp-019 per-problem analysis 将揭示 constraint precision 双峰分布，其中 FOLIO 高 precision 子集确实 SICA>SC。Paper 需 acknowledge positive operating point 而非 dismiss as noise。\n\nWorst 档的关键 universality-breaker：LLaMA-8B on D012 显示 +6.7pp overall，FOLIO 子集 +10pp。虽然 mcnemar_p=0.109（n=60 power 不足），但 5:1 discordant ratio 方向强。FOLIO +10pp 特别有问题——与 exp-020 (n=204, LLaMA-8B×FOLIO, Δ=-2.4pp) 直接矛盾（D012 的 30 题 vs full FOLIO 204 题）。Worst 档假设这 60 题 subsample 碰巧包含了 LLaMA-8B constraints 高 precision 的问题（selection bias or genuine subpopulation）。如果 per-problem precision 分析（exp-019）确认 30% 问题 precision>0.7，则 +10pp 在 high-precision 子集是 real signal 被 low-precision 多数稀释。"
189	  },
190	  {
191	    "name": "gsm8k_pilot_14b",
192	    "description": "Qwen2.5-14B on GSM8K 30 questions (K=12)",
193	    "results": {
194	      "sica_accuracy": 0.867,
195	      "sc_accuracy": 0.8,
196	      "delta_pp": 6.7,
197	      "n": 30,
198	      "k": 12,
199	      "multi_candidate_rate": 0.367,
200	      "c0_pct": 36.7,
201	      "extraction_rate": 0.875,
202	      "answer_extraction_rate": 0.97,
203	      "constraint_precision_mean": 0.58,
204	      "discordant_sica_wins": 3,
205	      "discordant_sc_wins": 1,
206	      "mcnemar_p": 0.317,
207	      "bootstrap_p": 0.06,
208	      "wall_time_min": 25
209	    },
210	    "tables": [
211	      "T1_main: add GSM8K row (flagged as pilot, n=30)"
212	    ],
213	    "figures": [],
214	    "analysis": "GSM8K +6.7pp 是 worst 档最具 reframe 压力的结果。即使 n=30 不 significant，combined with 7B (+5pp) 和 LLaMA-8B FOLIO (+10pp on subset)，形成 'there exist positive operating points' 的 consistent pattern。Paper 必须从 'capability trap is universal' → 'capability trap characterizes the majority of conditions but positive boundaries exist'。需额外 200+ 题 powered replication（exp-012 扩展）才能 confirm，但 pilot 数据足以 force reframe。\n\nWorst 档核心假设 #1：GSM8K 出现 Δ>+4pp。14B on GSM8K baseline ~80% (不像 reviewer 预测的 95%+)，因为 pilot 选取了 medium-hard 问题。C0=36.7% 在 worst 档范围内 [25,50]。+6.7pp 虽然 p=0.317 (n=30 underpowered)，但 bootstrap p=0.06 接近 significance。机制：数学问题的 FOL constraints 更 well-formed（numerical equalities like 'x + y = 15'），比 NLI 的 modal logic 更容易 correctly extract。Constraint precision 0.58 高于 FOLIO/PW 的 ~0.50，因为 math constraints 有 concrete numerical ground truth。这直接打破 'universally empty operating regime'——新 domain + moderate C0 + real constraint quality = genuine gain。"
215	  },
216	  {
217	    "name": "constraint_ablation",
218	    "description": "SICA-MaxSAT vs SICA-count-only vs SICA-random-weight",
219	    "results": {
220	      "maxsat_accuracy": 0.7649,
221	      "count_only_accuracy": 0.7587,
222	      "random_weight_accuracy": 0.755,
223	      "sc_baseline_accuracy": 0.7624,
224	      "maxsat_vs_count_mcnemar_p": 0.317,
225	      "maxsat_vs_random_mcnemar_p": 0.157,
226	      "n_problems": 804,
227	      "agreement_maxsat_count": 798,
228	      "disagreement_maxsat_wins": 4,
229	      "disagreement_count_wins": 2,
230	      "high_precision_subset_n": 95,
231	      "high_precision_maxsat_acc": 0.821,
232	      "high_precision_count_acc": 0.789,
233	      "high_precision_gap_pp": 3.2,
234	      "high_precision_mcnemar_p": 0.083
235	    },
236	    "tables": [
237	      "T3: Ablation results overall + high-precision subset breakdown"
238	    ],
239	    "figures": [],
240	    "analysis": "Subset MaxSAT>count-only (p=0.083) 是 worst 档 mechanism evidence 的关键 crack。Paper 需 acknowledge: 'When constraints are discriminative, the satisfiability structure of MAX-SAT provides additional signal beyond counting. The aggregation mechanism is not vacuous — it is starved of quality input.' 这实际上 STRENGTHENS oracle story (exp-021) 但 weakens 'mechanism is vacuous' claim。Reframe: mechanism is effective but latent, activated only by discriminative constraints。\n\nWorst 档假设 #3：exp-013 ablation 在子集上 MaxSAT > count-only。Overall MaxSAT ≈ count-only（798/804 agree），但在 constraint precision>0.6 的 95 个问题子集上，MaxSAT 比 count-only 高 3.2pp (p=0.083)。这意味着 SAT solver 非完全 vacuous——当 constraints 有 genuine discriminative content 时，satisfiability structure 比 simple counting 更好。全局 null 是因为 709/804 个问题 constraints non-discriminative，MaxSAT 退化为 counting。On the subset where constraints matter, MaxSAT mechanism IS adding value。这打破 'aggregation mechanism is completely vacuous' 叙事。"
241	  },
242	  {
243	    "name": "sica_deepseek_r1_llama_8b",
244	    "description": "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions",
245	    "results": {
246	      "sica_accuracy": 0.7,
247	      "sc_accuracy": 0.717,
248	      "delta_pp": -1.7,
249	      "multi_candidate_rate": 0.55,
250	      "c0_pct": 55.0,
251	      "extraction_rate": 0.85,
252	      "answer_extraction_rate": 0.94,
253	      "truncated_traces": 65,
254	      "contradiction_rate": 0.04,
255	      "mcnemar_p": 1.0,
256	      "discordant_sica_wins": 1,
257	      "discordant_sc_wins": 2,
258	      "wall_time_min": 95,
259	      "model": "DeepSeek-R1-Distill-LLaMA-8B"
260	    },
261	    "tables": [
262	      "T1_main: DeepSeek-R1-Distill row (instruction-scale classification)"
263	    ],
264	    "figures": [],
265	    "analysis": "DeepSeek-R1-Distill on LLaMA base 在 worst 档是 neutral data point——confirms capability trap on distilled models。不打破 nor 强化 universality。Reclassification 为 instruction-scale (C0>50%) 在 worst 档与其他档一致。\n\nDeepSeek-R1-Distill-LLaMA-8B 在 worst 档 behaves like instruction model (C0=55%, high diversity) 但 SICA slightly negative (-1.7pp)。与 Qwen-based distill (exp-014 registry: C0=58.3%, Δ=-3.3pp) 一致。Distilled reasoning models 有 instruction-like diversity 但 constraint quality 比 pure instruction models 更差（truncated thinking traces → incomplete constraint extraction）。Worst 档下这个结果不打破 universality——它 confirms distilled models fall in same trap。但 LLaMA-base vs Qwen-base 的 subtle difference (LLaMA -1.7pp vs Qwen -3.3pp) 暗示 base architecture matters slightly。"
266	  },
267	  {
268	    "name": "logic_lm_baseline",
269	    "description": "Logic-LM × K + majority vote baseline on FOLIO",
270	    "results": {
271	      "logic_lm_k12_accuracy": 0.779,
272	      "logic_lm_sc_accuracy": 0.794,
273	      "sica_accuracy": 0.794,
274	      "sc_accuracy": 0.794,
275	      "logic_lm_vs_sc_delta_pp": -1.5,
276	      "logic_lm_vs_sica_delta_pp": -1.5,
277	      "logic_lm_single_trace_accuracy": 0.755,
278	      "logic_lm_extraction_success_rate": 0.72,
279	      "n": 204
280	    },
281	    "tables": [
282	      "T_baselines: Logic-LM × K vs SICA vs SC"
283	    ],
284	    "figures": [],
285	    "analysis": "Logic-LM 结果在 worst 档不直接打破 universality 但 complicates the story：如果 single-trace verification × vote ≈ multi-trace MAX-SAT aggregation，则 SICA 的 additional complexity (cross-answer constraint evaluation) provides no marginal benefit over simpler approach。Paper 需 address：'Even the richer MAX-SAT aggregation structure provides no benefit over simpler per-trace evaluation when extraction quality is the binding constraint.'\n\nWorst 档下 Logic-LM×K baseline 略低于 SC (-1.5pp)，因为 Logic-LM 的 single-trace verification 方式在 K 次独立抽取中累积 extraction error。Logic-LM 单 trace accuracy (75.5%) 低于 SC (79.4%) 因为 FOL 翻译错误导致 false negative verifications。但关键 finding：Logic-LM×K accuracy (77.9%) 与 SICA (79.4%) 差距仅 1.5pp，且 Logic-LM 不需要 cross-trace MAX-SAT——simple per-trace FOL check + vote 已经 competitive。Reviewer 可能 argue 'multi-trace aggregation (SICA) provides minimal value over single-trace verification (Logic-LM style)' even when both fail to beat SC。"
286	  },
287	  {
288	    "name": "weighted_sc_baseline",
289	    "description": "Weighted SC baselines (length/confidence/constraint-count) on exp-001 data",
290	    "results": {
291	      "sica_accuracy": 0.7649,
292	      "sc_uniform_accuracy": 0.7624,
293	      "inv_length_accuracy": 0.7699,
294	      "length_weighted_accuracy": 0.7538,
295	      "constraint_count_accuracy": 0.7587,
296	      "inv_length_vs_sc_delta_pp": 0.75,
297	      "inv_length_vs_sc_p": 0.317,
298	      "inv_length_vs_sica_delta_pp": 0.5,
299	      "inv_length_vs_sica_p": 0.564,
300	      "n_problems": 804,
301	      "best_method": "inv_length",
302	      "all_nonsignificant": true
303	    },
304	    "tables": [
305	      "T_baselines: Weighted SC variants vs SICA vs SC"
306	    ],
307	    "figures": [],
308	    "analysis": "Inv-length slightly above SICA 在 worst 档是 uncomfortable：reviewer 可能 ask 'why use MAX-SAT if trace-length heuristic does equally well?'。Defense: (1) on high-precision subset MAX-SAT > all (exp-013 subset finding), (2) inv-length has no theoretical justification while MAX-SAT has principled mechanism that activates with quality constraints (oracle proof), (3) difference is n.s.。\n\nWorst 档下 inverse-length weighted SC (76.99%) 略高于 SICA (76.49%) 和 SC (76.24%)，虽然不显著 (p=0.317)。这暗示 shorter traces（更 confident/decisive reasoning）作为 quality signal 比 FOL constraint satisfiability 更有效。Weighted SC 不需要 constraint extraction overhead（节省 48.7% time），performance comparable or slightly better。在 worst 档 'condition-dependent reframe' 中，这变成：simpler weighting heuristics capture similar or more signal than MAX-SAT on the majority of conditions；MAX-SAT only adds value on the high-precision subset (connecting to exp-013)。"
309	  },
310	  {
311	    "name": "sica_strategyqa_14b",
312	    "description": "Qwen2.5-14B on StrategyQA 60 questions",
313	    "results": {
314	      "sica_accuracy": 0.6,
315	      "sc_accuracy": 0.55,
316	      "delta_pp": 5.0,
317	      "mcnemar_p": 0.157,
318	      "multi_candidate_rate": 0.383,
319	      "c0_pct": 38.3,
320	      "extraction_rate": 0.72,
321	      "answer_extraction_rate": 0.95,
322	      "constraint_precision_mean": 0.55,
323	      "discordant_sica_wins": 4,
324	      "discordant_sc_wins": 1,
325	      "bootstrap_ci_95": [
326	        -1.67,
327	        10.0
328	      ],
329	      "bootstrap_p": 0.07,
330	      "wall_time_min": 40
331	    },
332	    "tables": [
333	      "T1_main: StrategyQA row"
334	    ],
335	    "figures": [],
336	    "analysis": "StrategyQA +5pp combined with GSM8K +6.7pp 形成 'new domains show positive signals' pattern。这不是单点 noise——两个不同 domain 独立产生 +5-7pp。Worst 档的 reframe 变为：capability trap 主要 afflicts formal logic domain with NLI-style 3-class answer space (FOLIO/PW)；binary or numerical domains with concrete constraints benefit more。\n\nWorst 档假设 StrategyQA 出现 +5pp (p=0.157, n=60)。Commonsense 领域 C0=38.3%——模型在 yes/no binary questions 上有 moderate disagreement。Constraint quality (precision=0.55) 略高于 chance，足以在 4/5 discordant 问题上正确翻转。这是 worst 档 'condition-dependent' 证据之一：binary answer space + moderate diversity + commonsense domain = weak positive signal。机制：binary yes/no 使 constraint exclusion 更 powerful（排除一个 constraint 直接 flip answer），不像 NLI 3-class 或 math open-ended 需要更精确的 discrimination。"
337	  },
338	  {
339	    "name": "sica_arc_challenge_14b",
340	    "description": "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)",
341	    "results": {
342	      "sica_accuracy": 0.917,
343	      "sc_accuracy": 0.933,
344	      "delta_pp": -1.7,
345	      "multi_candidate_rate": 0.067,
346	      "c0_pct": 6.7,
347	      "extraction_rate": 0.95,
348	      "answer_extraction_rate": 1.0,
349	      "discordant_sica_wins": 0,
350	      "discordant_sc_wins": 1,
351	      "mcnemar_p": 1.0,
352	      "wall_time_min": 30
353	    },
354	    "tables": [
355	      "T1_main: ARC-Challenge row (near-degenerate)"
356	    ],
357	    "figures": [],
358	    "analysis": "ARC 在 worst 档是 supporting data for C0 threshold but with complication：如果 threshold 从 5% 调到 10%，ARC falls below → degenerate (consistent with -1.7pp)。但这使 C0 threshold 变成 tuned parameter 而非 principled cutoff。Paper 需 use 20% as threshold (original) or argue for continuous interpretation。\n\nARC-Challenge 在 worst 档下 C0 极低 (6.7%)——14B 在 science questions 上太 confident (93.3% SC accuracy)，answer space 近 unanimous。仅 4 个 multi-candidate 问题，SICA 在 1 个上错误翻转。ARC 结果不打破 universality 反而 confirms C0 threshold story：high-accuracy condition → low diversity → SICA degenerate。但 C0=6.7% 是 borderline（threshold=5%），不像 QwQ 的 <3% 那么 clean。Worst 档需 consider moving threshold to 10% 或 framing as continuous gradient。"
359	  },
360	  {
361	    "name": "constraint_quality_correlation",
362	    "description": "Per-problem constraint precision analysis, correlate with C0 and gap",
363	    "results": {
364	      "n_problems_analyzed": 804,
365	      "n_multi_candidate": 307,
366	      "constraint_precision_mean": 0.52,
367	      "constraint_precision_std": 0.21,
368	      "constraint_precision_median": 0.48,
369	      "bimodal_test_dip_p": 0.04,
370	      "high_precision_cluster_n": 95,
371	      "high_precision_cluster_mean": 0.74,
372	      "low_precision_cluster_n": 212,
373	      "low_precision_cluster_mean": 0.41,
374	      "precision_vs_c0_per_problem_r": 0.31,
375	      "precision_vs_c0_p": 0.002,
376	      "precision_vs_sica_correct_r": 0.28,
377	      "precision_vs_sica_correct_p": 0.005,
378	      "high_precision_sica_win_rate": 0.68,
379	      "low_precision_sica_win_rate": 0.44,
380	      "f2_non_discriminative_fraction": 0.69,
381	      "domain_precision_folio": 0.54,
382	      "domain_precision_proofwriter": 0.5,
383	      "domain_precision_strategyqa": 0.58,
384	      "domain_precision_gsm8k": 0.62
385	    },
386	    "tables": [
387	      "T_precision: Precision distribution statistics + cluster breakdown",
388	      "T_precision_domain: Domain × precision mean"
389	    ],
390	    "figures": [],
391	    "analysis": "Bimodal precision distribution 是 worst 档 paper 的 centerpiece finding。它解释了 (a) aggregate null (low-precision majority dilutes signal), (b) sporadic positive results on subsets (high-precision problems exist in all domains), (c) condition-dependent pattern (domains/models with more high-precision problems show positive gaps)。Reframed Claim 1 becomes: 'The capability trap is condition-dependent: ~31% of problems yield constraints with precision>0.6, sufficient for MAX-SAT to add value; the remaining 69% produce non-discriminative constraints that reduce MAX-SAT to counting.' 这 more nuanced 但 reviewer 可能认为 'just identifying that precision matters is not novel.' Defense: systematic quantification + oracle proof + C0 deployment diagnostic 作为 joint contribution。\n\nWorst 档假设 #2：F2 per-problem 分析揭示 constraint precision 双峰分布。Hartigan dip test p=0.04 confirms bimodality。307 个 multi-candidate 问题分为两个 cluster：95 个 high-precision (mean=0.74) 和 212 个 low-precision (mean=0.41)。High-precision 子集 SICA win rate 68% vs low-precision 44%。Per-problem precision 与 SICA correctness 有 significant correlation (r=0.28, p=0.005)。Non-discriminative fraction=0.69（在 worst 档范围 [0.5, 0.7]）。这证明 capability trap 非 uniform——约 31% 的问题有 adequate constraint quality，但被 69% low-precision 问题稀释到 aggregate null。Precision 与 C0 的 per-problem correlation (r=0.31) 支持 condition-dependent story。"
392	  },
393	  {
394	    "name": "sica_llama8b_strategyqa_200",
395	    "description": "LLaMA-8B on StrategyQA 200 questions — powered replication of suggestive positive signal",
396	    "results": {
397	      "n": 200,
398	      "k": 12,
399	      "sica_accuracy": 0.74,
400	      "sc_accuracy": 0.72,
401	      "delta_pp": 2.0,
402	      "mcnemar_p": 0.424,
403	      "multi_candidate_rate": 0.41,
404	      "bootstrap_ci_95": [
405	        -1.5,
406	        5.5
407	      ],
408	      "bootstrap_p": 0.12,
409	      "discordant_sica_wins": 9,
410	      "discordant_sc_wins": 5
411	    },
412	    "tables": [
413	      "T1_main: LLaMA-8B × StrategyQA row (n=200)"
414	    ],
415	    "figures": [],
416	    "analysis": "n=200 replication shows classic power problem：effect exists (~2pp) but too small for n=200 to detect reliably。Combined with other positive signals in worst 档 (GSM8K +6.7, 7B +5.0), meta-analytic estimate across positive-signal conditions ≈ +2-3pp。Not zero, but small enough that practical significance is debatable。\n\nPowered StrategyQA replication (n=200) 在 worst 档下 attenuates pilot signal：Δ=+2.0pp (vs pilot +5.0pp)，p=0.424 not significant。Regression to mean 部分消除了 n=60 pilot 的 positive signal。但 direction remains positive (9:5 discordant ratio)，CI includes both 0 and +5.5pp。Worst 档 interpretation：true effect is ~+2pp (small but real)，n=200 仍 underpowered to detect。Contributes to meta-analytic estimate 但 individually not significant。"
417	  },
418	  {
419	    "name": "sica_llama8b_folio_204",
420	    "description": "LLaMA-8B on full FOLIO 204 questions — powered test of +10pp D012 signal",
421	    "results": {
422	      "n": 204,
423	      "k": 12,
424	      "sica_accuracy": 0.623,
425	      "sc_accuracy": 0.632,
426	      "delta_pp": -0.9,
427	      "mcnemar_p": 0.774,
428	      "multi_candidate_rate": 0.618,
429	      "discordant_sica_wins": 6,
430	      "discordant_sc_wins": 7,
431	      "constraint_precision_mean": 0.49,
432	      "high_precision_subset_n": 42,
433	      "high_precision_subset_delta_pp": 4.8
434	    },
435	    "tables": [
436	      "T1_main: LLaMA-8B × FOLIO row (n=204, with subset annotation)"
437	    ],
438	    "figures": [],
439	    "analysis": "FOLIO 204 结果 resolves D012 +10pp anomaly：sampling artifact from small n that over-represented high-precision problems。True signal exists but only on ~20% of problems。This finding perfectly illustrates the worst-档 narrative：capability trap is real on majority of problems (80%) but not universal (20% show genuine benefit)。\n\nFull FOLIO 204 题 overall Δ=-0.9pp (null)，but worst 档 reveals heterogeneity：在 42 个 high-precision 子集 (precision>0.6) 上 SICA = +4.8pp。D012 的 30 题 FOLIO over-sampled 了 high-precision 问题（12/30 vs population rate 42/204=20.6%），解释了 +10pp artifact。真实 effect 在 high-precision subset ≈ +4.8pp，aggregate null 因 dilution。这支持 condition-dependent reframe 但 weakens 'LLaMA-8B×FOLIO is positive operating point' — 只有 subset 是 positive，不是全 domain。"
440	  },
441	  {
442	    "name": "overhead_analysis",
443	    "description": "Wall-time breakdown per question",
444	    "results": {
445	      "n": 804,
446	      "mean_total_wall_s": 61.6,
447	      "mean_trace_gen_s": 31.6,
448	      "trace_gen_pct": 51.3,
449	      "mean_extract_s": 29.0,
450	      "extract_pct": 47.0,
451	      "mean_maxsat_s": 0.003,
452	      "maxsat_pct": 0.005,
453	      "sica_overhead_pct": 48.7,
454	      "cost_per_question_extraction_only": "$0.018",
455	      "breakeven_gain_needed_pp": 3.0
456	    },
457	    "tables": [
458	      "T_overhead: Time breakdown + cost-benefit analysis by condition"
459	    ],
460	    "figures": [],
461	    "analysis": "Overhead in worst 档 transitions from 'obviously not worth it' to 'depends on condition.' The deployment framework becomes genuinely useful rather than trivially 'never use SICA.'\n\nOverhead analysis 在 worst 档下 gains new significance：如果 condition-dependent gains 为 +2-5pp on favorable subsets，且 overhead=48.7%，则 cost-benefit analysis becomes interesting rather than trivially negative。Breakeven point ≈ 3pp（considering extraction doubles inference time）。Some worst-档 conditions (GSM8K +6.7, 7B +5.0) exceed breakeven，making SICA conditionally viable rather than universally wasteful。This feeds into the reframed story：practitioners should use C0 + domain formalizability to decide whether SICA overhead is justified。"
462	  },
463	  {
464	    "name": "meta_analysis_combined",
465	    "description": "Combined meta-analytic summary across all conditions",
466	    "results": {
467	      "total_conditions": 14,
468	      "combined_N": 1482,
469	      "positive_conditions": 4,
470	      "null_conditions": 7,
471	      "negative_conditions": 3,
472	      "meta_analytic_delta_pp": 1.8,
473	      "meta_analytic_ci_95": [
474	        0.2,
475	        3.4
476	      ],
477	      "meta_analytic_p": 0.03,
478	      "heterogeneity_I2": 0.62,
479	      "heterogeneity_Q_p": 0.008,
480	      "positive_condition_mean_delta": 5.1,
481	      "null_condition_mean_delta": 0.1,
482	      "negative_condition_mean_delta": -2.5,
483	      "moderator_precision_p": 0.012,
484	      "moderator_c0_p": 0.09,
485	      "moderator_domain_formalizability_p": 0.04
486	    },
487	    "tables": [
488	      "T_meta: Forest plot data for all 14 conditions"
489	    ],
490	    "figures": [],
491	    "analysis": "Meta-analytic positive overall (p=0.03) combined with high heterogeneity (I²=0.62) is worst 档的 statistical signature。Can't claim universal null (positive overall)，can't claim universal benefit (heterogeneity)。Must claim condition-dependent phenomenon。This is more complex but arguably more interesting than pure negative — reviewer reaction unpredictable。\n\nWorst 档 meta-analytic estimate Δ=+1.8pp [0.2, 3.4]，technically significant (p=0.03) but clinically small。Critical：I²=0.62 indicates substantial heterogeneity (Q-test p=0.008)，meaning a single overall estimate is inappropriate。Moderator analysis reveals constraint precision (p=0.012) and domain formalizability (p=0.04) are significant moderators。This is the statistical backbone for 'condition-dependent phenomenon' reframe：overall small positive，but driven entirely by specific conditions，and other conditions are genuinely null or negative。"
492	  }
493	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26e5af40-2300-4fd2-b5d2-5496d2dab60a",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "0d68eb24-ee52-4f86-a561-9b4144c4a3ba",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"sica_k_ablation_14b\",\n    \"description\": \"K sensitivity (K=6,8,11,12,16,20) on D012 60 questions\",\n    \"results\": {\n      \"K6_sica\": 0.75,\n      \"K6_sc\": 0.733,\n      \"K6_gap_pp\": 1.7,\n      \"K8_sica\": 0.767,\n      \"K8_sc\": 0.75,\n      \"K8_gap_pp\": 1.7,\n      \"K11_sica\": 0.767,\n      \"K11_sc\": 0.733,\n      \"K11_gap_pp\": 3.3,\n      \"K12_sica\": 0.733,\n      \"K12_sc\": 0.7,\n      \"K12_gap_pp\": 3.3,\n      \"K16_sica\": 0.75,\n      \"K16_sc\": 0.733,\n      \"K16_gap_pp\": 1.7,\n      \"K20_sica\": 0.733,\n      \"K20_sc\": 0.717,\n      \"K20_gap_pp\": 1.7,\n      \"K11_mcnemar_p\": 0.157,\n      \"best_K_gap_pp\": 3.3,\n      \"odd_K_gap_gt_0\": true\n    },\n    \"tables\": [\n      \"T_appendix_K_ablation: K × SICA/SC accuracy matrix\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"K=11 odd-K positive gap 是 worst 档核心证据之一。如果 gap 仅存在于 even-K（tiebreak），可以 dismiss；但 odd-K +3.3pp 意味着 constraint exclusion 有 genuine discriminative value on this 60-question subset。Reframe: SICA has weak positive signal on D012-subset (Qwen-14B × formal logic × n=60) that doesn't survive power scaling (exp-001 n=804 shows +0.3pp)，但 heterogeneity 暗示 condition-dependence。\\n\\nWorst 档要求 universality 被打破。K=11（odd-K）仍出现 +3.3pp，证明 SICA 的增益不仅来自 tiebreak——odd-K 无精确平局，但 SICA 仍能通过 constraint exclusion 翻转少数问题。这打破了 'SICA value is purely tiebreak-driven' 叙事。虽然 p>0.1 因 n=60 power 不足，但方向一致且 K=11/K=12 两个 K 值重复 +3.3pp。需在论文中 reframe 为 'condition-dependent benefit at certain K ranges' 而非 'universally zero'。\"\n  },\n  {\n    \"name\": \"tiebreak_baseline_analysis\",\n    \"description\": \"SICA vs SC-random-tiebreak vs SC-deterministic comparison\",\n    \"results\": {\n      \"sica_tiebreak_win_rate\": 0.8,\n      \"random_tiebreak_win_rate\": 0.5,\n      \"alphabetical_tiebreak_win_rate\": 0.6,\n      \"first_seen_tiebreak_win_rate\": 0.4,\n      \"n_tied_questions\": 5,\n      \"tied_fraction\": 0.083,\n      \"sica_net_gain_from_tiebreak_pp\": 2.5,\n      \"sica_gain_beyond_tiebreak_pp\": 1.0\n    },\n    \"tables\": [\n      \"T_tiebreak: Tiebreak method × win rate on tied questions\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Tiebreak 分析在 worst 档下支持 'SICA has genuine constraint signal on subset' 叙事。但 effect size 太小 to be practically meaningful（5 个 tie 中多赢 1-2 个 = 1-3pp on full set）。Paper 需 acknowledge SICA has weak positive signal in favorable conditions 而非 zero。\\n\\nWorst 档下，tiebreak 分析揭示 SICA 的 tiebreak 优势（80% win rate on ties）AND 有少量 non-tie flips。5/60 个问题有 exact tie，SICA 在其中 4/5 选对；另外还有 1 个非平局问题被 constraint exclusion 翻转。这意味着 SICA mechanism 不完全 reducible to tiebreak——有微弱但存在的 exclusion 效应。在 n=60 subset 上 beyond-tiebreak gain ≈ 1pp 不显著，但 existence 本身打破 'purely tiebreak' framing。\"\n  },\n  {\n    \"name\": \"sica_7b_scaling\",\n    \"description\": \"Qwen2.5-7B-Instruct on 60 questions, testing weaker model → higher C0 → larger gap\",\n    \"results\": {\n      \"sica_accuracy\": 0.617,\n      \"sc_accuracy\": 0.567,\n      \"delta_pp\": 5.0,\n      \"mcnemar_p\": 0.083,\n      \"multi_candidate_rate\": 0.717,\n      \"c0_pct\": 71.7,\n      \"extraction_rate\": 0.82,\n      \"answer_extraction_rate\": 0.91,\n      \"constraint_precision_mean\": 0.54,\n      \"discordant_sica_wins\": 4,\n      \"discordant_sc_wins\": 1,\n      \"wall_time_min\": 45\n    },\n    \"tables\": [\n      \"T1_main: add Qwen-7B row\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 的 +5pp 是 worst 档的 smoking gun。虽然 n=60 power 不足以达到 p<0.05，但方向与 LLaMA-8B exp-011 FOLIO +10pp 一致。Pattern emerges: weaker models on formal logic domains show positive gaps。需 reframe capability trap 为 'high-capacity models extract non-discriminative constraints; low-capacity models paradoxically benefit because their higher error rate creates more room for constraint-based correction'。\\n\\nWorst 档的核心打破机制之一：weaker model (7B) 产生更高 C0 (71.7%) 且 delta=+5.0pp（p=0.083，接近 significance）。这暗示 capability trap 是 capacity-dependent 而非 universal。7B 模型 extraction quality 低（precision~0.54），但因为 baseline accuracy 也低（56.7%），constraints 的微弱 discriminative signal 足以翻转几个问题。C0-gap 正相关在 experiment-level 出现（7B: C0=72%, Δ=+5; 14B: C0=38%, Δ=+0.3; 72B: C0~15%, Δ≈0），产生 r=0.3-0.4 的 condition-level correlation。这打破了 'no correlation between diversity and benefit' 叙事。\"\n  },\n  {\n    \"name\": \"qwq_32b_operating_regime\",\n    \"description\": \"QwQ-32B negative results formatted for paper\",\n    \"results\": {\n      \"qwq_aggregate_c0_effective_pct\": 3.6,\n      \"qwq_aime_delta_pp\": 0,\n      \"qwq_proofwriter_delta_pp\": 0,\n      \"qwq_folio_delta_pp\": 0,\n      \"total_problems\": 46,\n      \"sica_degenerate_to_sc\": true,\n      \"reasoning_model_c0_threshold_confirmed\": true\n    },\n    \"tables\": [\n      \"T1_main: QwQ-32B row (C0<5%, SICA≡SC)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"QwQ 数据在 worst 档是 safe asset——不会产生 surprise。但 reviewer concern #4 ('only one reasoning model') 在 worst 档更尖锐：如果 instruction-scale 条件显示 condition-dependent gains，reviewer 会问 'what about reasoning models on tasks where they have moderate C0?' 可能需要 QwQ on easier tasks where it's not 100% accurate。\\n\\nQwQ-32B 在 worst 档下不变：C0<5%，SICA≡SC。Full reasoning model 的 deterministic chain 消除 diversity，SICA 结构性退化。这在 worst 档仍成立因为 worst 档打破的是 instruction-scale 模型的 universality，不是 reasoning model 的 behavior。QwQ 数据仍支持 Claim 3 (C0&lt;threshold → degenerate)。问题是 n=46 across heterogeneous tasks，reviewer 可能要求更多 reasoning model data points。\"\n  },\n  {\n    \"name\": \"c0_diagnostic_validation\",\n    \"description\": \"Plot C0 vs SICA-SC gap across all conditions\",\n    \"results\": {\n      \"n_conditions\": 12,\n      \"pearson_r_c0_gap\": 0.38,\n      \"pearson_p\": 0.08,\n      \"spearman_rho\": 0.42,\n      \"spearman_p\": 0.06,\n      \"c0_below_5_all_zero_gap\": true,\n      \"c0_above_30_gap_range_pp\": [\n        -3.3,\n        6.7\n      ],\n      \"c0_above_30_mean_gap_pp\": 1.8,\n      \"linear_model_r2\": 0.14,\n      \"c0_threshold_5_specificity\": 1.0,\n      \"c0_threshold_5_sensitivity\": 0.0\n    },\n    \"tables\": [\n      \"T_c0_diagnostic: condition × C0 × gap × n\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Moderate correlation (r=0.38) 是 worst 档的 nuisance finding。不足以 claim C0 is predictive (p=0.08, R²=0.14)，但足以让 reviewer 质疑 'C0 is uninformative beyond threshold'。Paper 需 reframe Claim 3 为 joint diagnostic (C0 + constraint precision) 而非 C0 alone。\\n\\nWorst 档下，C0 与 gap 的 experiment-level correlation 是 moderate positive (r=0.38, p=0.08)，接近 significance。这与 best/mid 档 (r≈0.15, p=0.74) 截然不同。原因：7B 和 LLaMA-8B 条件的 high C0 + positive gap 拉高了 correlation。但 R²=0.14 说明 C0 只解释 14% variance——仍是 'necessary but insufficient' 但带有 weak positive predictive direction。Claim 3 需 reframe：C0 不仅是 binary gate (C0<5% → degenerate) 而是有 weak gradient effect（higher C0 correlates with slightly higher expected gap），但 variance 太大 for deployment use。\"\n  },\n  {\n    \"name\": \"sica_72b_awq\",\n    \"description\": \"Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions\",\n    \"results\": {\n      \"sica_accuracy\": 0.817,\n      \"sc_accuracy\": 0.833,\n      \"delta_pp\": -1.7,\n      \"multi_candidate_rate\": 0.15,\n      \"c0_pct\": 15.0,\n      \"extraction_rate\": 0.93,\n      \"answer_extraction_rate\": 1.0,\n      \"constraint_precision_mean\": 0.61,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 1.0,\n      \"wall_time_min\": 180\n    },\n    \"tables\": [\n      \"T1_main: Qwen-72B row\",\n      \"T_precision: model size vs constraint precision\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 结果支持 within-family scaling narrative：model capacity ↑ → C0 ↓ + precision ↑，两者抵消使 gap≈0。但 combined with 7B (C0=72%, precision=0.54, gap=+5pp)，creates a capacity-dependent boundary story。Worst 档的 paper structure 需 show this scaling dimension explicitly。\\n\\n72B 高 baseline (83.3%) 导致 C0 低 (15%)——模型太 confident，answer space 近 unanimous。SICA 轻微 negative (-1.7pp) 因仅 9 个 multi-candidate 问题，constraint exclusion 在 1 个问题上错误翻转。Interesting finding for worst 档：constraint precision 在 72B 较高 (0.61 vs 14B 的 0.52)——bigger model extracts better constraints，但 C0 太低 to matter。这支持 reframed story：capability trap 有两个 regime：(1) weak model = high C0 + low precision = marginal benefit，(2) strong model = low C0 + high precision = degenerate。Sweet spot 可能存在于 intermediate capacity × formal domain。\"\n  },\n  {\n    \"name\": \"constraint_quality_case_studies\",\n    \"description\": \"Qualitative analysis of extracted constraints on 5-10 representative questions\",\n    \"results\": {\n      \"n_analyzed\": 10,\n      \"high_precision_cases\": 3,\n      \"low_precision_cases\": 5,\n      \"mixed_precision_cases\": 2,\n      \"high_precision_constraint_example\": \"ForAll(x, Human(x) -> Mortal(x)) correctly excludes wrong answer\",\n      \"low_precision_example\": \"Exists(x, Answer(x, 'True')) - tautologically matches any answer\",\n      \"bimodal_finding\": true,\n      \"precision_gt_0p7_fraction\": 0.3,\n      \"precision_lt_0p4_fraction\": 0.5\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies 在 worst 档是 double-edged：证明 mechanism CAN work (high-precision cases exist) 同时解释 WHY aggregate 结果 null (diluted by majority low-precision)。Paper 需 position as 'the capability trap is not a fundamental impossibility but a current extraction quality gap with identifiable conditions for success'。\\n\\nWorst 档下 case study 揭示 bimodal pattern：30% 的问题有 precision>0.7 的 genuinely discriminative constraints（特别是 FOLIO 中有明确 logical structure 的问题），50% 的问题 constraints 基本 random (precision<0.4)。这支持 'capability trap 非 uniform' 假设——部分问题 constraints 有效但被 low-precision 多数稀释。Qualitative evidence 展示 failure mode diversity：(a) 语义空约束 (∀x, True)，(b) 约束复述答案 (circular)，(c) 约束正确但对所有答案等效 (non-discriminative despite being valid FOL)。\"\n  },\n  {\n    \"name\": \"sica_llama_8b\",\n    \"description\": \"LLaMA-3.1-8B-Instruct on D012 60 questions\",\n    \"results\": {\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.617,\n      \"delta_pp\": 6.7,\n      \"mcnemar_p\": 0.109,\n      \"multi_candidate_rate\": 0.617,\n      \"c0_pct\": 61.7,\n      \"extraction_rate\": 0.856,\n      \"answer_extraction_rate\": 0.896,\n      \"contradiction_rate\": 0.053,\n      \"discordant_sica_wins\": 5,\n      \"discordant_sc_wins\": 1,\n      \"folio_sica\": 0.7,\n      \"folio_sc\": 0.6,\n      \"folio_delta_pp\": 10.0,\n      \"proofwriter_sica\": 0.633,\n      \"proofwriter_sc\": 0.6,\n      \"proofwriter_delta_pp\": 3.3,\n      \"wall_time_min\": 66\n    },\n    \"tables\": [\n      \"T1_main: LLaMA-8B row with per-domain breakdown\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLaMA-8B FOLIO +10pp 是 worst 档最棘手的数据点。两种解释：(1) n=30 抽样 variance (SE≈9pp，+10pp 在 1σ 内)，(2) D012 的 30 题偏向 high-formalizability 子集。Worst 档假设 (2) 部分成立——exp-019 per-problem analysis 将揭示 constraint precision 双峰分布，其中 FOLIO 高 precision 子集确实 SICA>SC。Paper 需 acknowledge positive operating point 而非 dismiss as noise。\\n\\nWorst 档的关键 universality-breaker：LLaMA-8B on D012 显示 +6.7pp overall，FOLIO 子集 +10pp。虽然 mcnemar_p=0.109（n=60 power 不足），但 5:1 discordant ratio 方向强。FOLIO +10pp 特别有问题——与 exp-020 (n=204, LLaMA-8B×FOLIO, Δ=-2.4pp) 直接矛盾（D012 的 30 题 vs full FOLIO 204 题）。Worst 档假设这 60 题 subsample 碰巧包含了 LLaMA-8B constraints 高 precision 的问题（selection bias or genuine subpopulation）。如果 per-problem precision 分析（exp-019）确认 30% 问题 precision>0.7，则 +10pp 在 high-precision 子集是 real signal 被 low-precision 多数稀释。\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_14b\",\n    \"description\": \"Qwen2.5-14B on GSM8K 30 questions (K=12)\",\n    \"results\": {\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.8,\n      \"delta_pp\": 6.7,\n      \"n\": 30,\n      \"k\": 12,\n      \"multi_candidate_rate\": 0.367,\n      \"c0_pct\": 36.7,\n      \"extraction_rate\": 0.875,\n      \"answer_extraction_rate\": 0.97,\n      \"constraint_precision_mean\": 0.58,\n      \"discordant_sica_wins\": 3,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 0.317,\n      \"bootstrap_p\": 0.06,\n      \"wall_time_min\": 25\n    },\n    \"tables\": [\n      \"T1_main: add GSM8K row (flagged as pilot, n=30)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K +6.7pp 是 worst 档最具 reframe 压力的结果。即使 n=30 不 significant，combined with 7B (+5pp) 和 LLaMA-8B FOLIO (+10pp on subset)，形成 'there exist positive operating points' 的 consistent pattern。Paper 必须从 'capability trap is universal' → 'capability trap characterizes the majority of conditions but positive boundaries exist'。需额外 200+ 题 powered replication（exp-012 扩展）才能 confirm，但 pilot 数据足以 force reframe。\\n\\nWorst 档核心假设 #1：GSM8K 出现 Δ>+4pp。14B on GSM8K baseline ~80% (不像 reviewer 预测的 95%+)，因为 pilot 选取了 medium-hard 问题。C0=36.7% 在 worst 档范围内 [25,50]。+6.7pp 虽然 p=0.317 (n=30 underpowered)，但 bootstrap p=0.06 接近 significance。机制：数学问题的 FOL constraints 更 well-formed（numerical equalities like 'x + y = 15'），比 NLI 的 modal logic 更容易 correctly extract。Constraint precision 0.58 高于 FOLIO/PW 的 ~0.50，因为 math constraints 有 concrete numerical ground truth。这直接打破 'universally empty operating regime'——新 domain + moderate C0 + real constraint quality = genuine gain。\"\n  },\n  {\n    \"name\": \"constraint_ablation\",\n    \"description\": \"SICA-MaxSAT vs SICA-count-only vs SICA-random-weight\",\n    \"results\": {\n      \"maxsat_accuracy\": 0.7649,\n      \"count_only_accuracy\": 0.7587,\n      \"random_weight_accuracy\": 0.755,\n      \"sc_baseline_accuracy\": 0.7624,\n      \"maxsat_vs_count_mcnemar_p\": 0.317,\n      \"maxsat_vs_random_mcnemar_p\": 0.157,\n      \"n_problems\": 804,\n      \"agreement_maxsat_count\": 798,\n      \"disagreement_maxsat_wins\": 4,\n      \"disagreement_count_wins\": 2,\n      \"high_precision_subset_n\": 95,\n      \"high_precision_maxsat_acc\": 0.821,\n      \"high_precision_count_acc\": 0.789,\n      \"high_precision_gap_pp\": 3.2,\n      \"high_precision_mcnemar_p\": 0.083\n    },\n    \"tables\": [\n      \"T3: Ablation results overall + high-precision subset breakdown\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Subset MaxSAT>count-only (p=0.083) 是 worst 档 mechanism evidence 的关键 crack。Paper 需 acknowledge: 'When constraints are discriminative, the satisfiability structure of MAX-SAT provides additional signal beyond counting. The aggregation mechanism is not vacuous — it is starved of quality input.' 这实际上 STRENGTHENS oracle story (exp-021) 但 weakens 'mechanism is vacuous' claim。Reframe: mechanism is effective but latent, activated only by discriminative constraints。\\n\\nWorst 档假设 #3：exp-013 ablation 在子集上 MaxSAT > count-only。Overall MaxSAT ≈ count-only（798/804 agree），但在 constraint precision>0.6 的 95 个问题子集上，MaxSAT 比 count-only 高 3.2pp (p=0.083)。这意味着 SAT solver 非完全 vacuous——当 constraints 有 genuine discriminative content 时，satisfiability structure 比 simple counting 更好。全局 null 是因为 709/804 个问题 constraints non-discriminative，MaxSAT 退化为 counting。On the subset where constraints matter, MaxSAT mechanism IS adding value。这打破 'aggregation mechanism is completely vacuous' 叙事。\"\n  },\n  {\n    \"name\": \"sica_deepseek_r1_llama_8b\",\n    \"description\": \"DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions\",\n    \"results\": {\n      \"sica_accuracy\": 0.7,\n      \"sc_accuracy\": 0.717,\n      \"delta_pp\": -1.7,\n      \"multi_candidate_rate\": 0.55,\n      \"c0_pct\": 55.0,\n      \"extraction_rate\": 0.85,\n      \"answer_extraction_rate\": 0.94,\n      \"truncated_traces\": 65,\n      \"contradiction_rate\": 0.04,\n      \"mcnemar_p\": 1.0,\n      \"discordant_sica_wins\": 1,\n      \"discordant_sc_wins\": 2,\n      \"wall_time_min\": 95,\n      \"model\": \"DeepSeek-R1-Distill-LLaMA-8B\"\n    },\n    \"tables\": [\n      \"T1_main: DeepSeek-R1-Distill row (instruction-scale classification)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek-R1-Distill on LLaMA base 在 worst 档是 neutral data point——confirms capability trap on distilled models。不打破 nor 强化 universality。Reclassification 为 instruction-scale (C0>50%) 在 worst 档与其他档一致。\\n\\nDeepSeek-R1-Distill-LLaMA-8B 在 worst 档 behaves like instruction model (C0=55%, high diversity) 但 SICA slightly negative (-1.7pp)。与 Qwen-based distill (exp-014 registry: C0=58.3%, Δ=-3.3pp) 一致。Distilled reasoning models 有 instruction-like diversity 但 constraint quality 比 pure instruction models 更差（truncated thinking traces → incomplete constraint extraction）。Worst 档下这个结果不打破 universality——它 confirms distilled models fall in same trap。但 LLaMA-base vs Qwen-base 的 subtle difference (LLaMA -1.7pp vs Qwen -3.3pp) 暗示 base architecture matters slightly。\"\n  },\n  {\n    \"name\": \"logic_lm_baseline\",\n    \"description\": \"Logic-LM × K + majority vote baseline on FOLIO\",\n    \"results\": {\n      \"logic_lm_k12_accuracy\": 0.779,\n      \"logic_lm_sc_accuracy\": 0.794,\n      \"sica_accuracy\": 0.794,\n      \"sc_accuracy\": 0.794,\n      \"logic_lm_vs_sc_delta_pp\": -1.5,\n      \"logic_lm_vs_sica_delta_pp\": -1.5,\n      \"logic_lm_single_trace_accuracy\": 0.755,\n      \"logic_lm_extraction_success_rate\": 0.72,\n      \"n\": 204\n    },\n    \"tables\": [\n      \"T_baselines: Logic-LM × K vs SICA vs SC\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Logic-LM 结果在 worst 档不直接打破 universality 但 complicates the story：如果 single-trace verification × vote ≈ multi-trace MAX-SAT aggregation，则 SICA 的 additional complexity (cross-answer constraint evaluation) provides no marginal benefit over simpler approach。Paper 需 address：'Even the richer MAX-SAT aggregation structure provides no benefit over simpler per-trace evaluation when extraction quality is the binding constraint.'\\n\\nWorst 档下 Logic-LM×K baseline 略低于 SC (-1.5pp)，因为 Logic-LM 的 single-trace verification 方式在 K 次独立抽取中累积 extraction error。Logic-LM 单 trace accuracy (75.5%) 低于 SC (79.4%) 因为 FOL 翻译错误导致 false negative verifications。但关键 finding：Logic-LM×K accuracy (77.9%) 与 SICA (79.4%) 差距仅 1.5pp，且 Logic-LM 不需要 cross-trace MAX-SAT——simple per-trace FOL check + vote 已经 competitive。Reviewer 可能 argue 'multi-trace aggregation (SICA) provides minimal value over single-trace verification (Logic-LM style)' even when both fail to beat SC。\"\n  },\n  {\n    \"name\": \"weighted_sc_baseline\",\n    \"description\": \"Weighted SC baselines (length/confidence/constraint-count) on exp-001 data\",\n    \"results\": {\n      \"sica_accuracy\": 0.7649,\n      \"sc_uniform_accuracy\": 0.7624,\n      \"inv_length_accuracy\": 0.7699,\n      \"length_weighted_accuracy\": 0.7538,\n      \"constraint_count_accuracy\": 0.7587,\n      \"inv_length_vs_sc_delta_pp\": 0.75,\n      \"inv_length_vs_sc_p\": 0.317,\n      \"inv_length_vs_sica_delta_pp\": 0.5,\n      \"inv_length_vs_sica_p\": 0.564,\n      \"n_problems\": 804,\n      \"best_method\": \"inv_length\",\n      \"all_nonsignificant\": true\n    },\n    \"tables\": [\n      \"T_baselines: Weighted SC variants vs SICA vs SC\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Inv-length slightly above SICA 在 worst 档是 uncomfortable：reviewer 可能 ask 'why use MAX-SAT if trace-length heuristic does equally well?'。Defense: (1) on high-precision subset MAX-SAT > all (exp-013 subset finding), (2) inv-length has no theoretical justification while MAX-SAT has principled mechanism that activates with quality constraints (oracle proof), (3) difference is n.s.。\\n\\nWorst 档下 inverse-length weighted SC (76.99%) 略高于 SICA (76.49%) 和 SC (76.24%)，虽然不显著 (p=0.317)。这暗示 shorter traces（更 confident/decisive reasoning）作为 quality signal 比 FOL constraint satisfiability 更有效。Weighted SC 不需要 constraint extraction overhead（节省 48.7% time），performance comparable or slightly better。在 worst 档 'condition-dependent reframe' 中，这变成：simpler weighting heuristics capture similar or more signal than MAX-SAT on the majority of conditions；MAX-SAT only adds value on the high-precision subset (connecting to exp-013)。\"\n  },\n  {\n    \"name\": \"sica_strategyqa_14b\",\n    \"description\": \"Qwen2.5-14B on StrategyQA 60 questions\",\n    \"results\": {\n      \"sica_accuracy\": 0.6,\n      \"sc_accuracy\": 0.55,\n      \"delta_pp\": 5.0,\n      \"mcnemar_p\": 0.157,\n      \"multi_candidate_rate\": 0.383,\n      \"c0_pct\": 38.3,\n      \"extraction_rate\": 0.72,\n      \"answer_extraction_rate\": 0.95,\n      \"constraint_precision_mean\": 0.55,\n      \"discordant_sica_wins\": 4,\n      \"discordant_sc_wins\": 1,\n      \"bootstrap_ci_95\": [\n        -1.67,\n        10.0\n      ],\n      \"bootstrap_p\": 0.07,\n      \"wall_time_min\": 40\n    },\n    \"tables\": [\n      \"T1_main: StrategyQA row\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"StrategyQA +5pp combined with GSM8K +6.7pp 形成 'new domains show positive signals' pattern。这不是单点 noise——两个不同 domain 独立产生 +5-7pp。Worst 档的 reframe 变为：capability trap 主要 afflicts formal logic domain with NLI-style 3-class answer space (FOLIO/PW)；binary or numerical domains with concrete constraints benefit more。\\n\\nWorst 档假设 StrategyQA 出现 +5pp (p=0.157, n=60)。Commonsense 领域 C0=38.3%——模型在 yes/no binary questions 上有 moderate disagreement。Constraint quality (precision=0.55) 略高于 chance，足以在 4/5 discordant 问题上正确翻转。这是 worst 档 'condition-dependent' 证据之一：binary answer space + moderate diversity + commonsense domain = weak positive signal。机制：binary yes/no 使 constraint exclusion 更 powerful（排除一个 constraint 直接 flip answer），不像 NLI 3-class 或 math open-ended 需要更精确的 discrimination。\"\n  },\n  {\n    \"name\": \"sica_arc_challenge_14b\",\n    \"description\": \"Qwen2.5-14B on ARC-Challenge 60 questions (K=12)\",\n    \"results\": {\n      \"sica_accuracy\": 0.917,\n      \"sc_accuracy\": 0.933,\n      \"delta_pp\": -1.7,\n      \"multi_candidate_rate\": 0.067,\n      \"c0_pct\": 6.7,\n      \"extraction_rate\": 0.95,\n      \"answer_extraction_rate\": 1.0,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 1.0,\n      \"wall_time_min\": 30\n    },\n    \"tables\": [\n      \"T1_main: ARC-Challenge row (near-degenerate)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ARC 在 worst 档是 supporting data for C0 threshold but with complication：如果 threshold 从 5% 调到 10%，ARC falls below → degenerate (consistent with -1.7pp)。但这使 C0 threshold 变成 tuned parameter 而非 principled cutoff。Paper 需 use 20% as threshold (original) or argue for continuous interpretation。\\n\\nARC-Challenge 在 worst 档下 C0 极低 (6.7%)——14B 在 science questions 上太 confident (93.3% SC accuracy)，answer space 近 unanimous。仅 4 个 multi-candidate 问题，SICA 在 1 个上错误翻转。ARC 结果不打破 universality 反而 confirms C0 threshold story：high-accuracy condition → low diversity → SICA degenerate。但 C0=6.7% 是 borderline（threshold=5%），不像 QwQ 的 <3% 那么 clean。Worst 档需 consider moving threshold to 10% 或 framing as continuous gradient。\"\n  },\n  {\n    \"name\": \"constraint_quality_correlation\",\n    \"description\": \"Per-problem constraint precision analysis, correlate with C0 and gap\",\n    \"results\": {\n      \"n_problems_analyzed\": 804,\n      \"n_multi_candidate\": 307,\n      \"constraint_precision_mean\": 0.52,\n      \"constraint_precision_std\": 0.21,\n      \"constraint_precision_median\": 0.48,\n      \"bimodal_test_dip_p\": 0.04,\n      \"high_precision_cluster_n\": 95,\n      \"high_precision_cluster_mean\": 0.74,\n      \"low_precision_cluster_n\": 212,\n      \"low_precision_cluster_mean\": 0.41,\n      \"precision_vs_c0_per_problem_r\": 0.31,\n      \"precision_vs_c0_p\": 0.002,\n      \"precision_vs_sica_correct_r\": 0.28,\n      \"precision_vs_sica_correct_p\": 0.005,\n      \"high_precision_sica_win_rate\": 0.68,\n      \"low_precision_sica_win_rate\": 0.44,\n      \"f2_non_discriminative_fraction\": 0.69,\n      \"domain_precision_folio\": 0.54,\n      \"domain_precision_proofwriter\": 0.5,\n      \"domain_precision_strategyqa\": 0.58,\n      \"domain_precision_gsm8k\": 0.62\n    },\n    \"tables\": [\n      \"T_precision: Precision distribution statistics + cluster breakdown\",\n      \"T_precision_domain: Domain × precision mean\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bimodal precision distribution 是 worst 档 paper 的 centerpiece finding。它解释了 (a) aggregate null (low-precision majority dilutes signal), (b) sporadic positive results on subsets (high-precision problems exist in all domains), (c) condition-dependent pattern (domains/models with more high-precision problems show positive gaps)。Reframed Claim 1 becomes: 'The capability trap is condition-dependent: ~31% of problems yield constraints with precision>0.6, sufficient for MAX-SAT to add value; the remaining 69% produce non-discriminative constraints that reduce MAX-SAT to counting.' 这 more nuanced 但 reviewer 可能认为 'just identifying that precision matters is not novel.' Defense: systematic quantification + oracle proof + C0 deployment diagnostic 作为 joint contribution。\\n\\nWorst 档假设 #2：F2 per-problem 分析揭示 constraint precision 双峰分布。Hartigan dip test p=0.04 confirms bimodality。307 个 multi-candidate 问题分为两个 cluster：95 个 high-precision (mean=0.74) 和 212 个 low-precision (mean=0.41)。High-precision 子集 SICA win rate 68% vs low-precision 44%。Per-problem precision 与 SICA correctness 有 significant correlation (r=0.28, p=0.005)。Non-discriminative fraction=0.69（在 worst 档范围 [0.5, 0.7]）。这证明 capability trap 非 uniform——约 31% 的问题有 adequate constraint quality，但被 69% low-precision 问题稀释到 aggregate null。Precision 与 C0 的 per-problem correlation (r=0.31) 支持 condition-dependent story。\"\n  },\n  {\n    \"name\": \"sica_llama8b_strategyqa_200\",\n    \"description\": \"LLaMA-8B on StrategyQA 200 questions — powered replication of suggestive positive signal\",\n    \"results\": {\n      \"n\": 200,\n      \"k\": 12,\n      \"sica_accuracy\": 0.74,\n      \"sc_accuracy\": 0.72,\n      \"delta_pp\": 2.0,\n      \"mcnemar_p\": 0.424,\n      \"multi_candidate_rate\": 0.41,\n      \"bootstrap_ci_95\": [\n        -1.5,\n        5.5\n      ],\n      \"bootstrap_p\": 0.12,\n      \"discordant_sica_wins\": 9,\n      \"discordant_sc_wins\": 5\n    },\n    \"tables\": [\n      \"T1_main: LLaMA-8B × StrategyQA row (n=200)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"n=200 replication shows classic power problem：effect exists (~2pp) but too small for n=200 to detect reliably。Combined with other positive signals in worst 档 (GSM8K +6.7, 7B +5.0), meta-analytic estimate across positive-signal conditions ≈ +2-3pp。Not zero, but small enough that practical significance is debatable。\\n\\nPowered StrategyQA replication (n=200) 在 worst 档下 attenuates pilot signal：Δ=+2.0pp (vs pilot +5.0pp)，p=0.424 not significant。Regression to mean 部分消除了 n=60 pilot 的 positive signal。但 direction remains positive (9:5 discordant ratio)，CI includes both 0 and +5.5pp。Worst 档 interpretation：true effect is ~+2pp (small but real)，n=200 仍 underpowered to detect。Contributes to meta-analytic estimate 但 individually not significant。\"\n  },\n  {\n    \"name\": \"sica_llama8b_folio_204\",\n    \"description\": \"LLaMA-8B on full FOLIO 204 questions — powered test of +10pp D012 signal\",\n    \"results\": {\n      \"n\": 204,\n      \"k\": 12,\n      \"sica_accuracy\": 0.623,\n      \"sc_accuracy\": 0.632,\n      \"delta_pp\": -0.9,\n      \"mcnemar_p\": 0.774,\n      \"multi_candidate_rate\": 0.618,\n      \"discordant_sica_wins\": 6,\n      \"discordant_sc_wins\": 7,\n      \"constraint_precision_mean\": 0.49,\n      \"high_precision_subset_n\": 42,\n      \"high_precision_subset_delta_pp\": 4.8\n    },\n    \"tables\": [\n      \"T1_main: LLaMA-8B × FOLIO row (n=204, with subset annotation)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"FOLIO 204 结果 resolves D012 +10pp anomaly：sampling artifact from small n that over-represented high-precision problems。True signal exists but only on ~20% of problems。This finding perfectly illustrates the worst-档 narrative：capability trap is real on majority of problems (80%) but not universal (20% show genuine benefit)。\\n\\nFull FOLIO 204 题 overall Δ=-0.9pp (null)，but worst 档 reveals heterogeneity：在 42 个 high-precision 子集 (precision>0.6) 上 SICA = +4.8pp。D012 的 30 题 FOLIO over-sampled 了 high-precision 问题（12/30 vs population rate 42/204=20.6%），解释了 +10pp artifact。真实 effect 在 high-precision subset ≈ +4.8pp，aggregate null 因 dilution。这支持 condition-dependent reframe 但 weakens 'LLaMA-8B×FOLIO is positive operating point' — 只有 subset 是 positive，不是全 domain。\"\n  },\n  {\n    \"name\": \"overhead_analysis\",\n    \"description\": \"Wall-time breakdown per question\",\n    \"results\": {\n      \"n\": 804,\n      \"mean_total_wall_s\": 61.6,\n      \"mean_trace_gen_s\": 31.6,\n      \"trace_gen_pct\": 51.3,\n      \"mean_extract_s\": 29.0,\n      \"extract_pct\": 47.0,\n      \"mean_maxsat_s\": 0.003,\n      \"maxsat_pct\": 0.005,\n      \"sica_overhead_pct\": 48.7,\n      \"cost_per_question_extraction_only\": \"$0.018\",\n      \"breakeven_gain_needed_pp\": 3.0\n    },\n    \"tables\": [\n      \"T_overhead: Time breakdown + cost-benefit analysis by condition\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Overhead in worst 档 transitions from 'obviously not worth it' to 'depends on condition.' The deployment framework becomes genuinely useful rather than trivially 'never use SICA.'\\n\\nOverhead analysis 在 worst 档下 gains new significance：如果 condition-dependent gains 为 +2-5pp on favorable subsets，且 overhead=48.7%，则 cost-benefit analysis becomes interesting rather than trivially negative。Breakeven point ≈ 3pp（considering extraction doubles inference time）。Some worst-档 conditions (GSM8K +6.7, 7B +5.0) exceed breakeven，making SICA conditionally viable rather than universally wasteful。This feeds into the reframed story：practitioners should use C0 + domain formalizability to decide whether SICA overhead is justified。\"\n  },\n  {\n    \"name\": \"meta_analysis_combined\",\n    \"description\": \"Combined meta-analytic summary across all conditions\",\n    \"results\": {\n      \"total_conditions\": 14,\n      \"combined_N\": 1482,\n      \"positive_conditions\": 4,\n      \"null_conditions\": 7,\n      \"negative_conditions\": 3,\n      \"meta_analytic_delta_pp\": 1.8,\n      \"meta_analytic_ci_95\": [\n        0.2,\n        3.4\n      ],\n      \"meta_analytic_p\": 0.03,\n      \"heterogeneity_I2\": 0.62,\n      \"heterogeneity_Q_p\": 0.008,\n      \"positive_condition_mean_delta\": 5.1,\n      \"null_condition_mean_delta\": 0.1,\n      \"negative_condition_mean_delta\": -2.5,\n      \"moderator_precision_p\": 0.012,\n      \"moderator_c0_p\": 0.09,\n      \"moderator_domain_formalizability_p\": 0.04\n    },\n    \"tables\": [\n      \"T_meta: Forest plot data for all 14 conditions\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Meta-analytic positive overall (p=0.03) combined with high heterogeneity (I²=0.62) is worst 档的 statistical signature。Can't claim universal null (positive overall)，can't claim universal benefit (heterogeneity)。Must claim condition-dependent phenomenon。This is more complex but arguably more interesting than pure negative — reviewer reaction unpredictable。\\n\\nWorst 档 meta-analytic estimate Δ=+1.8pp [0.2, 3.4]，technically significant (p=0.03) but clinically small。Critical：I²=0.62 indicates substantial heterogeneity (Q-test p=0.008)，meaning a single overall estimate is inappropriate。Moderator analysis reveals constraint precision (p=0.012) and domain formalizability (p=0.04) are significant moderators。This is the statistical backbone for 'condition-dependent phenomenon' reframe：overall small positive，but driven entirely by specific conditions，and other conditions are genuinely null or negative。\"\n  }\n]",
      "numLines": 493,
      "startLine": 1,
      "totalLines": 493
    }
  },
  "sourceToolAssistantUUID": "26e5af40-2300-4fd2-b5d2-5496d2dab60a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:15:33.263Z_

<details><summary>↩ Tool result · `toolu_017KgFSeRYGVTNnDamRCCvqA`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)
8	
9	1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]
10	2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
11	3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.
12	
13	## Core Insight
14	LLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.
15	
16	**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.
17	
18	We provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]
19	
20	## Story Spine
21	- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
22	- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
23	- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.
24	- **Headline result**: "Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level."
25	
26	## Anticipated Reviewer Concerns & Defensive Experiments
27	1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
28	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
29	3. **"Only Qwen models"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B
30	4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
31	5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
32	6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
33	7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
34	8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
35	9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
36	10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
37	11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
38	12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.
39	13. **"Self-extraction confound — same model generates and extracts"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.
40	14. **"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.
41	15. **"MAX-SAT formulation is just weighted voting"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as "even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain."
42	
43	## Working Title
44	**"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting"**
45	(Alternatives: 
46	- "Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation"
47	- "When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints")
48	
49	NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA" — NOT "symbolic consensus" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.
50	
51	## Paper Structure (EMNLP 8pp + appendix)
52	- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)
53	- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)
54	- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data
55	
56	## Claim Risk Notes (Updated D035 + exp-014)
57	- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
58	- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
59	- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports "diversity is necessary but insufficient" NOT "gradient diagnostic." Claim 3 should be: "C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level." RESOLVED (temperature data in hand).
60	- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
61	- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.
62	
63	## Required Citations (Dream D037 — minimum 30 references)
64	
65	Paper Agent MUST include these categories (non-exhaustive list of must-cite works):
66	- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)
67	- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
68	- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)
69	- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)
70	- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
71	- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers
72	- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023
73	- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)
74	
75	## Claim Scoping Rules (Dream D037)
76	
77	- n=60 conditions: present as "suggestive/consistent with" NOT "confirming." Only n≥200 conditions can "confirm" null.
78	- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.
79	- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.
80	- "Capability trap" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.
81	
82	## Venue Fit Risks
83	- EMNLP: Negative-results/analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic + overhead analysis.
84	- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
85	- Statistical power: Now strong (N>1,200 combined across powered tests).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe9bbff7-64d5-4f81-886d-2dc451993b8b",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "f2017db4-06a4-4e30-b755-9efa1f3d218e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nLLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.\n\n**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.\n\nWe provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n13. **\"Self-extraction confound — same model generates and extracts\"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.\n14. **\"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)\"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.\n15. **\"MAX-SAT formulation is just weighted voting\"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as \"even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain.\"\n\n## Working Title\n**\"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\"**\n(Alternatives: \n- \"Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation\"\n- \"When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\" — NOT \"symbolic consensus\" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)\n- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports \"diversity is necessary but insufficient\" NOT \"gradient diagnostic.\" Claim 3 should be: \"C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level.\" RESOLVED (temperature data in hand).\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Required Citations (Dream D037 — minimum 30 references)\n\nPaper Agent MUST include these categories (non-exhaustive list of must-cite works):\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)\n- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)\n\n## Claim Scoping Rules (Dream D037)\n\n- n=60 conditions: present as \"suggestive/consistent with\" NOT \"confirming.\" Only n≥200 conditions can \"confirm\" null.\n- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.\n- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.\n- \"Capability trap\" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  },
  "sourceToolAssistantUUID": "fe9bbff7-64d5-4f81-886d-2dc451993b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:15:33.258Z_

<details open><summary>🔧 Tool call — Read · `toolu_017KgFSeRYGVTNnDamRCCvqA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d68eb24-ee52-4f86-a561-9b4144c4a3ba",
  "isSidechain": false,
  "requestId": "req_011Cb8X2UN5KyAYpaohxCXtT",
  "type": "assistant",
  "uuid": "fe9bbff7-64d5-4f81-886d-2dc451993b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0161twftq3t9vHccUQdnFchB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12476
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "f2017db4-06a4-4e30-b755-9efa1f3d218e",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated research paper",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Assistant

_source line 14 · 2026-05-17T17:16:07.654Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me synthesize the key points:

**Narrative guidance (worst tier)**: Reframe capability trap as condition-dependent phenomenon, not universal. Title: "When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap"

Three reframed claims:
1. Positive boundary: identify sufficient conditions for capability trap (model capacity × domain formalizability × precision threshold)
2. Mechanism: oracle proves aggregation works + capability trap explains most failures
3. Diagnostic: C0 + constraint precision joint framework

Key experiments to cover:


1. K sensitivity across model scales
2. Tiebreak analysis baseline
3. Qwen 7B showing +5pp improvement
4. QwQ operating regime with near-zero diversity
5. C0 diagnostic validation against performance gap
6. 72B model showing -1.7pp degradation
7. Qualitative constraint quality case studies
8. LLaMA-8B with +6.7pp gains
9. GSM8K results with +6.7pp from the pilot
10. MaxSAT constraint ablation versus simpler baselines
11. DeepSeek R1 distilled to LLaMA-8B
12. Logic-LM and Weighted SC baseline comparisons
13. StrategyQA results showing +5pp
14. ARC-Challenge exhibiting near-degenerate behavior
15. Per-problem precision analysis revealing bimodal constraint quality distribution
16. LLaMA-8B StrategyQA replication at scale
17. Full FOLIO dataset evaluation
18. Overhead analysis examining computational time and cost tradeoffs
19. Meta-analytic synthesis across all conditions

Now I'm structuring this into a complete paper with abstract, introduction, methods section covering the SICA pipeline, experiments organized by category, and discussion. I need to ensure the key statistics are accurate: 14 conditions with combined N=1482, meta-analytic effect of +1.8pp with 95% CI [0.2, 3.4] and p=0.03, substantial heterogeneity at I²=0.62, the bimodal constraint precision split between 95 high-quality problems (mean 0.74) and 212 low-quality ones (mean 0.41), and the oracle upper bound of +8.82pp.

I'm planning nine tables to comprehensively present the results: main results across model and domain combinations, oracle control, constraint ablations comparing MaxSAT against simpler baselines, constraint precision distribution, diagnostic analysis of C0 versus performance gap, comparisons with Logic-LM and weighted self-consistency, meta-analytic summary, tiebreak analysis, and computational overhead metrics.

Writing the LaTeX document now...

For the worst-performing tier, the key insight is that the capability trap isn't universal—certain conditions show meaningful gains like 5-7pp improvements on specific models and datasets—yet the overall meta-analytic effect remains modest at +1.8pp with substantial heterogeneity, driven partly by the bimodal constraint precision distribution where only 31% of constraints achieve high precision.

Now I'm writing the full LaTeX paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2017db4-06a4-4e30-b755-9efa1f3d218e",
  "isSidechain": false,
  "requestId": "req_011Cb8X2oUmi6au7qWefuhjE",
  "type": "assistant",
  "uuid": "c566e780-de6b-4ef5-9174-f0a7cb0f1cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153STft1cADpKQ7iWRPEtwH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17315,
      "cache_read_input_tokens": 24317,
      "output_tokens": 1306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1306,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17315
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

_source line 15 · 2026-05-17T17:16:07.657Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c566e780-de6b-4ef5-9174-f0a7cb0f1cdc",
  "isSidechain": false,
  "requestId": "req_011Cb8X2oUmi6au7qWefuhjE",
  "type": "assistant",
  "uuid": "3b3deaee-036c-4a59-92a5-dba065e41539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153STft1cADpKQ7iWRPEtwH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17315,
      "cache_read_input_tokens": 24317,
      "output_tokens": 1306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1306,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17315
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

_source line 16 · 2026-05-17T17:16:08.854Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KyydDi5iWDgr17qki3KA8J`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b3deaee-036c-4a59-92a5-dba065e41539",
  "isSidechain": false,
  "requestId": "req_011Cb8X2oUmi6au7qWefuhjE",
  "type": "assistant",
  "uuid": "3451d332-98bf-4c8b-b38f-8e3a4e0855af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0153STft1cADpKQ7iWRPEtwH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17315,
      "cache_read_input_tokens": 24317,
      "output_tokens": 1306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1306,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17315
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

_source line 17 · 2026-05-17T17:16:09.037Z_

<details><summary>↩ Tool result · `toolu_01KyydDi5iWDgr17qki3KA8J`</summary>

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
  "parentUuid": "3451d332-98bf-4c8b-b38f-8e3a4e0855af",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "88814200-c64c-49bc-9484-036f26c8e140",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3451d332-98bf-4c8b-b38f-8e3a4e0855af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T17:19:58.988Z_

<details open><summary>🔧 Tool call — Write · `toolu_01MbzsFNETabNaq2Ar41PgSE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\title{When Do Self-Extracted Constraints Improve LLM Reasoning? \\\\ Characterizing the Capability Trap}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nSymbolic constraint aggregation, where a Large Language Model (LLM) extracts First-Order Logic (FOL) constraints from its own reasoning traces and a MAX-SAT solver selects the most consistent answer, has been proposed as a principled alternative to majority voting (Self-Consistency, SC). We present a systematic study of Self-Extracted Invariant Constraint Aggregation (SICA) across 14 experimental conditions spanning 5 model families, 5 reasoning domains, and over 1,400 problems. A meta-analysis yields a small positive overall effect ($\\Delta$=+1.8pp, $p$=0.03) but with substantial heterogeneity ($I^2$=0.62), indicating that the benefit is condition-dependent rather than universal. We identify a \\emph{capability trap}: in the majority of conditions ($\\sim$69\\% of multi-candidate problems), self-extracted constraints lack discriminative power (precision $\\sim$0.41), reducing MAX-SAT to counting. However, a bimodal precision distribution reveals that $\\sim$31\\% of problems yield high-precision constraints (mean 0.74), on which SICA outperforms SC by +3--5pp. An oracle experiment replacing self-extracted constraints with gold FOL annotations achieves +8.82pp ($p<$0.001), confirming that the aggregation mechanism is effective when given discriminative input. We characterize the sufficient conditions for the capability trap (model capacity, domain formalizability, precision threshold) and propose a joint C0-precision diagnostic framework for practitioners deciding whether symbolic aggregation is worth the overhead.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nSelf-Consistency (SC) decoding \\citep{wang2023selfconsistency} improves LLM reasoning by sampling multiple chains of thought and selecting the majority answer. A natural extension is to extract structured constraints from these reasoning traces and use a formal solver to aggregate them, potentially capturing logical relationships that simple counting misses. Several methods pursue this direction: Logic-LM \\citep{pan2023logiclm} translates problems into FOL for solver-based verification, LINC \\citep{olausson2023linc} uses neurosymbolic integration, and recent work on DyLoS \\citep{dylos2026}, Aristotle \\citep{aristotle2025}, and FoVer \\citep{fover2025} shows gains using trained or external verifiers. But a fundamental question remains open: \\emph{when does self-extracted symbolic aggregation actually help over simple majority voting?}\n\nThis question matters because symbolic aggregation incurs substantial overhead. Constraint extraction nearly doubles inference time (+48.7\\%), and deploying a MAX-SAT solver adds engineering complexity. If practitioners cannot predict when the investment pays off, the method risks being either universally adopted at a loss or universally dismissed despite having genuine operating points.\n\nWe study this question through SICA (Self-Extracted Invariant Constraint Aggregation), which extracts FOL constraints from $K$ reasoning traces and uses weighted MAX-SAT to select the answer satisfying the most constraints. Unlike methods that use trained verifiers or external knowledge, SICA relies entirely on the same model for both generation and constraint extraction, isolating the fundamental capability question: can an LLM extract constraints from its own reasoning that are good enough to beat counting?\n\nOur study spans 14 experimental conditions: 5 model families (Qwen-2.5 at 7B/14B/72B, LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5 domains (FOLIO, ProofWriter, StrategyQA, GSM8K, ARC-Challenge), totaling over 1,400 evaluated problems. The answer we find is nuanced: SICA's benefit is condition-dependent, governed by a capability trap that affects the majority but not the entirety of conditions.\n\nWe make three contributions:\n\\begin{enumerate}\n    \\item \\textbf{Boundary conditions for the capability trap.} We identify three factors that jointly determine whether self-extracted constraints improve over voting: model capacity (weaker models benefit more), domain formalizability (mathematical and binary-answer domains yield higher constraint precision), and a precision threshold ($>$0.6) above which MAX-SAT adds genuine value. Approximately 31\\% of multi-candidate problems meet this threshold; on these, SICA outperforms SC.\n    \\item \\textbf{Mechanism validation via oracle control.} Replacing self-extracted constraints with gold FOL annotations yields +8.82pp over SC ($p<$0.001, $n$=204), proving that the MAX-SAT aggregation mechanism is effective given discriminative constraints. The capability trap is a quality bottleneck in self-extraction, not a flaw in the aggregation paradigm.\n    \\item \\textbf{Joint C0-precision diagnostic framework.} We show that candidate diversity (C0) alone is necessary but insufficient for predicting SICA benefit. C0 $<$ 5\\% guarantees degeneration to SC (specificity 1.0), but among high-C0 conditions, constraint precision is the binding moderator ($p$=0.012 in meta-regression). We propose a two-stage deployment check: first screen on C0, then estimate constraint precision on a pilot sample.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. METHOD\n%% ============================================================\n\\section{Method: SICA Pipeline}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$, SICA proceeds in four stages:\n(1) sample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from an LLM;\n(2) extract a candidate answer $a_i$ and a set of FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ from each trace $t_i$;\n(3) evaluate each constraint $c_{i,j}$ against each candidate answer $a_k$ to build a weighted MAX-SAT instance;\n(4) solve the MAX-SAT instance to select the answer satisfying the maximum total weight of constraints.\n\n\\subsection{Trace Generation}\n\nWe sample $K$ independent reasoning traces using temperature $\\tau > 0$. Each trace produces a natural-language chain of thought, from which we extract both the final answer and any intermediate logical constraints the model articulates.\n\n\\subsection{Constraint Extraction}\n\nA second LLM call (using the same model) receives the trace $t_i$ and a structured prompt requesting FOL constraints. The extraction prompt asks the model to formalize key reasoning steps as first-order logic statements. We parse the output to obtain $\\mathcal{C}_i$ and $a_i$. Extraction succeeds on 82--95\\% of traces depending on the model.\n\n\\subsection{MAX-SAT Aggregation}\n\nLet $\\mathcal{A} = \\{a_1, \\ldots, a_L\\}$ be the set of distinct candidate answers across all $K$ traces. For each candidate $a_\\ell$ and constraint $c_{i,j}$, we evaluate whether $c_{i,j}$ is consistent with $a_\\ell$ (a binary compatibility check). We construct a weighted MAX-SAT instance where each clause corresponds to a constraint-candidate pair, weighted by the number of traces supporting that constraint. The answer maximizing total satisfied weight is selected.\n\nWhen constraints are non-discriminative (equally compatible with all candidates), MAX-SAT reduces to weighted counting, equivalent to majority voting with trace-level weights.\n\n\\subsection{Candidate Diversity Metric: C0}\n\nWe define \\emph{candidate diversity} C0 as the fraction of problems where more than one distinct answer appears across $K$ traces:\n\\[\n    \\text{C0} = \\frac{|\\{q : |\\mathcal{A}_q| > 1\\}|}{|Q|}\n\\]\nC0 measures the potential scope for constraint-based re-ranking. When C0 = 0, all traces agree and SICA is identical to SC.\n\n%% ============================================================\n%% 3. EXPERIMENTS\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models}\n\nWe evaluate six models spanning three paradigms:\n\\textbf{Instruction-scale}: Qwen-2.5-7B-Instruct, Qwen-2.5-14B-Instruct, Qwen-2.5-72B-Instruct (AWQ 4-bit), LLaMA-3.1-8B-Instruct.\n\\textbf{Distilled reasoning}: DeepSeek-R1-Distill-LLaMA-8B.\n\\textbf{Full reasoning}: QwQ-32B.\n\n\\subsection{Domains}\n\nFive reasoning domains: FOLIO (formal deductive logic, 3-class), ProofWriter (rule-based logical inference), StrategyQA (commonsense binary questions), GSM8K (grade-school math), and ARC-Challenge (science multiple-choice).\n\n\\subsection{Protocol}\n\nUnless noted, we use $K$=12 traces per problem. We report accuracy, the SICA$-$SC gap ($\\Delta$pp), McNemar's test $p$-value, and C0. Sample sizes range from $n$=30 (pilots) to $n$=804 (powered main experiment).\n\n%% ============================================================\n%% 4. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Main Results Across Conditions}\n\nTable~\\ref{tab:main} reports SICA and SC accuracy across all model-domain conditions. The results reveal a heterogeneous pattern: four conditions show positive gaps ($\\Delta > +4$pp), seven are null ($|\\Delta| < 2$pp), and three are negative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results across model-domain conditions. $\\Delta$ = SICA $-$ SC in percentage points. Bold indicates $\\Delta > +4$pp. $^\\dagger$Pilot ($n$=30). $^\\ddagger$Near-degenerate (C0 $<$ 10\\%).}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{$n$} & \\textbf{SC} & \\textbf{SICA} & \\textbf{$\\Delta$pp} & \\textbf{C0\\%} & \\textbf{$p$} \\\\\n\\midrule\nQwen-14B & D012 mix & 804 & 76.2 & 76.5 & +0.3 & 38.2 & 0.87 \\\\\nQwen-7B & D012 mix & 60 & 56.7 & 61.7 & \\textbf{+5.0} & 71.7 & 0.083 \\\\\nQwen-72B & D012 mix & 60 & 83.3 & 81.7 & $-$1.7 & 15.0 & 1.0 \\\\\nLLaMA-8B & D012 mix & 60 & 61.7 & 68.3 & \\textbf{+6.7} & 61.7 & 0.109 \\\\\nLLaMA-8B & FOLIO & 204 & 63.2 & 62.3 & $-$0.9 & 61.8 & 0.774 \\\\\nLLaMA-8B & StrategyQA & 200 & 72.0 & 74.0 & +2.0 & 41.0 & 0.424 \\\\\nDeepSeek-R1 & D012 mix & 60 & 71.7 & 70.0 & $-$1.7 & 55.0 & 1.0 \\\\\nQwQ-32B & Aggregate & 46 & --- & --- & 0.0 & 3.6$^\\ddagger$ & --- \\\\\nQwen-14B & GSM8K$^\\dagger$ & 30 & 80.0 & 86.7 & \\textbf{+6.7} & 36.7 & 0.317 \\\\\nQwen-14B & StrategyQA & 60 & 55.0 & 60.0 & \\textbf{+5.0} & 38.3 & 0.157 \\\\\nQwen-14B & ARC-Chall.$^\\ddagger$ & 60 & 93.3 & 91.7 & $-$1.7 & 6.7 & 1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge. First, weaker models show larger positive gaps: Qwen-7B (+5.0pp, C0=71.7\\%) and LLaMA-8B on D012 (+6.7pp, C0=61.7\\%), compared to Qwen-14B on the same domain (+0.3pp). Second, new domains outside formal logic show positive signals: GSM8K (+6.7pp) and StrategyQA (+5.0pp for Qwen-14B). Third, high-capacity models and low-diversity conditions produce null or negative results: Qwen-72B ($-$1.7pp, C0=15\\%), QwQ-32B (C0=3.6\\%, SICA degenerates to SC), and ARC-Challenge ($-$1.7pp, C0=6.7\\%).\n\nThe LLaMA-8B FOLIO result ($n$=204, $\\Delta$=$-$0.9pp) contrasts with the D012 subset result (+6.7pp on $n$=60), suggesting the D012 subsample over-represented high-precision problems. On the high-precision subset of full FOLIO (42 problems with constraint precision $>$ 0.6), SICA achieves +4.8pp, consistent with condition-dependent benefit.\n\n\\subsection{Model Capacity Scaling}\n\nWithin the Qwen family, we observe a clear capacity-dependent pattern (Table~\\ref{tab:main}). Qwen-7B (C0=71.7\\%, precision=0.54) shows $\\Delta$=+5.0pp; Qwen-14B (C0=38.2\\%) shows $\\Delta$=+0.3pp; Qwen-72B (C0=15.0\\%, precision=0.61) shows $\\Delta$=$-$1.7pp. Weaker models produce higher diversity but lower constraint precision, while stronger models produce lower diversity but higher precision. The net effect favors weaker models because their higher error rate creates more room for constraint-based correction, even when constraint quality is imperfect.\n\n\\subsection{Constraint Quality Analysis}\n\\label{sec:precision}\n\nPer-problem analysis of 307 multi-candidate problems from the Qwen-14B $n$=804 condition reveals a bimodal constraint precision distribution (Hartigan's dip test $p$=0.04). Two clusters emerge: 95 high-precision problems (mean precision 0.74) and 212 low-precision problems (mean precision 0.41). Table~\\ref{tab:precision} summarizes the distribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint precision distribution across 307 multi-candidate problems. SICA win rate: fraction of discordant pairs where SICA selects the correct answer.}\n\\label{tab:precision}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Cluster} & \\textbf{$n$} & \\textbf{Mean Prec.} & \\textbf{SICA Win Rate} & \\textbf{Fraction} \\\\\n\\midrule\nHigh-precision ($>$0.6) & 95 & 0.74 & 0.68 & 31\\% \\\\\nLow-precision ($<$0.6) & 212 & 0.41 & 0.44 & 69\\% \\\\\n\\midrule\nOverall & 307 & 0.52 & 0.52 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn high-precision problems, SICA wins 68\\% of discordant cases, providing genuine discriminative value. On the low-precision majority, SICA wins only 44\\%, performing slightly worse than chance due to noisy constraint-based re-ranking. Precision correlates significantly with SICA correctness ($r$=0.28, $p$=0.005) and with per-problem C0 ($r$=0.31, $p$=0.002).\n\nDomain-level precision varies: GSM8K achieves the highest mean precision (0.62), followed by StrategyQA (0.58), FOLIO (0.54), and ProofWriter (0.50). Mathematical constraints with concrete numerical content (e.g., $x + y = 15$) are easier to correctly extract than modal logic statements in NLI tasks.\n\n\\subsection{Oracle Control Experiment}\n\nTo isolate whether the bottleneck is in constraint extraction or aggregation, we replace self-extracted constraints with gold FOL annotations from the FOLIO dataset and evaluate MAX-SAT aggregation on $n$=204 problems. Oracle-SICA achieves 88.24\\% accuracy, compared to SC at 79.41\\%, a gain of +8.82pp ($p < 0.001$). This confirms that the MAX-SAT aggregation mechanism is effective when given discriminative constraints. The capability trap is exclusively a self-extraction quality problem.\n\n\\subsection{Constraint Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares three aggregation variants on the Qwen-14B $n$=804 condition: full MAX-SAT, count-only (ignoring satisfiability structure), and random-weight (shuffled constraint weights).\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation ablation on Qwen-14B ($n$=804). High-precision subset: problems with constraint precision $>$ 0.6 ($n$=95).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Overall Acc.} & \\textbf{$\\Delta$ vs SC} & \\textbf{HP Subset Acc.} & \\textbf{HP $\\Delta$ vs SC} \\\\\n\\midrule\nSC (baseline) & 76.24 & --- & --- & --- \\\\\nSICA (MAX-SAT) & 76.49 & +0.25 & 82.1 & --- \\\\\nCount-only & 75.87 & $-$0.37 & 78.9 & --- \\\\\nRandom-weight & 75.50 & $-$0.74 & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{High-precision subset ($n$=95):}} \\\\\nMAX-SAT vs count-only & \\multicolumn{4}{c}{+3.2pp ($p$=0.083)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverall, all three variants perform within 1pp of SC, with 798/804 problems producing identical answers across MAX-SAT and count-only. The aggregation mechanism is latent: on the full dataset, non-discriminative constraints reduce all methods to counting. On the high-precision subset ($n$=95), MAX-SAT outperforms count-only by 3.2pp ($p$=0.083), indicating that satisfiability structure provides additional signal when constraints are genuinely discriminative.\n\n\\subsection{Baseline Comparisons}\n\n\\paragraph{Weighted SC variants.} Table~\\ref{tab:baselines} compares SICA against simpler weighted voting schemes on the $n$=804 condition.\n\n\\begin{table}[t]\n\\centering\n\\caption{SICA vs weighted SC baselines and Logic-LM (Qwen-14B). All differences are non-significant.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs SC} \\\\\n\\midrule\nSC (uniform voting) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & +0.25 \\\\\nInverse-length weighted & 76.99 & +0.75 \\\\\nLength weighted & 75.38 & $-$0.86 \\\\\nConstraint-count weighted & 75.87 & $-$0.37 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Logic-LM comparison (FOLIO, $n$=204):}} \\\\\nLogic-LM $\\times$ $K$=12 & 77.9 & $-$1.5 vs SC \\\\\nSC & 79.4 & --- \\\\\nSICA & 79.4 & 0.0 vs SC \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInverse-length weighted SC slightly outperforms both SC and SICA (+0.75pp, $p$=0.317), suggesting that trace brevity (a proxy for confidence) captures comparable signal without extraction overhead. Logic-LM $\\times$ $K$ (per-trace FOL verification with majority vote) achieves 77.9\\% on FOLIO, 1.5pp below SC, because single-trace translation errors accumulate across $K$ independent attempts.\n\n\\paragraph{Tiebreak analysis.} On 5/60 exactly tied problems (Qwen-14B D012), SICA's constraint-informed tiebreak wins 80\\% (4/5), compared to 50\\% for random and 60\\% for alphabetical tiebreak. Beyond tiebreak, SICA produces an additional $\\sim$1.0pp gain from non-tie flips. The tiebreak advantage is real but affects too few problems ($\\sim$8.3\\% tie rate) to be practically significant.\n\n\\subsection{C0 Diagnostic Analysis}\n\nTable~\\ref{tab:c0} and the corresponding analysis examine the relationship between C0 and the SICA-SC gap across all 12 non-degenerate conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{C0 vs SICA$-$SC gap across experimental conditions. Conditions with C0 $<$ 5\\% (QwQ-32B) produce $\\Delta$=0 by construction.}\n\\label{tab:c0}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nPearson $r$ (C0 vs $\\Delta$) & 0.38 & 0.08 \\\\\nSpearman $\\rho$ & 0.42 & 0.06 \\\\\nLinear $R^2$ & 0.14 & --- \\\\\nC0 $<$ 5\\%: all $\\Delta$=0 & Specificity 1.0 & --- \\\\\nC0 $>$ 30\\%: mean $\\Delta$ & +1.8pp & --- \\\\\nC0 $>$ 30\\%: $\\Delta$ range & [$-$3.3, +6.7] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nC0 shows a moderate positive correlation with the SICA gap ($r$=0.38, $p$=0.08), but explains only 14\\% of variance. The key finding is asymmetric: C0 $<$ 5\\% reliably predicts degeneration (specificity 1.0), but high C0 does not guarantee benefit. Among conditions with C0 $>$ 30\\%, the gap ranges from $-$3.3pp to +6.7pp. Constraint precision is the critical moderator within high-C0 conditions ($p$=0.012 in meta-regression, Section~\\ref{sec:meta}).\n\n\\subsection{K Sensitivity}\n\\label{sec:k_ablation}\n\nWe vary $K \\in \\{6, 8, 11, 12, 16, 20\\}$ on the Qwen-14B D012 $n$=60 subset (Table~\\ref{tab:kablation}). The SICA$-$SC gap is consistently small (+1.7 to +3.3pp) and never significant ($p > 0.15$). At odd $K$=11 (where exact ties are impossible), SICA still achieves +3.3pp, confirming that the mechanism is not purely tiebreak-driven. This gap matches $K$=12, suggesting constraint exclusion provides a small genuine signal on this subset that is independent of tie resolution.\n\n\\begin{table}[t]\n\\centering\n\\caption{$K$ sensitivity on Qwen-14B D012 ($n$=60).}\n\\label{tab:kablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{SICA} & \\textbf{SC} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\n6 & 75.0 & 73.3 & +1.7 \\\\\n8 & 76.7 & 75.0 & +1.7 \\\\\n11 & 76.7 & 73.3 & +3.3 \\\\\n12 & 73.3 & 70.0 & +3.3 \\\\\n16 & 75.0 & 73.3 & +1.7 \\\\\n20 & 73.3 & 71.7 & +1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reasoning Model Behavior}\n\nQwQ-32B produces near-deterministic reasoning chains with effective C0 of 3.6\\% across 46 problems (AIME, ProofWriter, FOLIO). With $\\Delta$=0.0pp on all three subsets, SICA degenerates to SC by construction. Full reasoning models' extended chain-of-thought process converges to consistent answers, eliminating the diversity that SICA requires.\n\nDeepSeek-R1-Distill-LLaMA-8B, despite being distilled from a reasoning model, behaves like an instruction model (C0=55.0\\%). Its 8B parameter count is insufficient for deterministic reasoning chains, producing instruction-like diversity. However, SICA shows $\\Delta$=$-$1.7pp ($p$=1.0), consistent with the capability trap: high diversity but non-discriminative constraints due to truncated thinking traces degrading extraction quality.\n\n\\subsection{Overhead Analysis}\n\\label{sec:overhead}\n\nOn the $n$=804 condition, mean wall time per problem is 61.6 seconds: 31.6s for trace generation (51.3\\%) and 29.0s for constraint extraction (47.0\\%). MAX-SAT solving takes 0.003s (negligible). SICA's overhead is 48.7\\% beyond standard SC, at an extraction cost of \\$0.018 per problem.\n\nThe breakeven point is approximately +3pp: conditions where SICA gains exceed 3pp justify the overhead. Four of our 14 conditions exceed this threshold (Qwen-7B +5.0, LLaMA-8B D012 +6.7, GSM8K +6.7, StrategyQA 14B +5.0), all characterized by moderate-to-high C0 ($>$35\\%) and at least moderate constraint precision ($>$0.55).\n\n\\subsection{Meta-Analysis}\n\\label{sec:meta}\n\nTable~\\ref{tab:meta} summarizes the meta-analytic results across all 14 conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Meta-analytic summary across 14 conditions ($N$=1,482 total problems).}\n\\label{tab:meta}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nOverall $\\Delta$ (random effects) & +1.8pp \\\\\n95\\% CI & [+0.2, +3.4] \\\\\n$p$-value & 0.03 \\\\\n$I^2$ (heterogeneity) & 0.62 \\\\\n$Q$-test $p$ & 0.008 \\\\\n\\midrule\nPositive conditions ($\\Delta > +4$pp) & 4 / 14 \\\\\nNull conditions ($|\\Delta| < 2$pp) & 7 / 14 \\\\\nNegative conditions ($\\Delta < -2$pp) & 3 / 14 \\\\\n\\midrule\nMean $\\Delta$ (positive conditions) & +5.1pp \\\\\nMean $\\Delta$ (null conditions) & +0.1pp \\\\\nMean $\\Delta$ (negative conditions) & $-$2.5pp \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Moderator analysis:}} \\\\\nConstraint precision & $p$ = 0.012 \\\\\nDomain formalizability & $p$ = 0.04 \\\\\nC0 & $p$ = 0.09 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall effect is small but statistically significant ($\\Delta$=+1.8pp, $p$=0.03). However, the substantial heterogeneity ($I^2$=0.62, $Q$ $p$=0.008) indicates that a single overall estimate is inadequate. Moderator analysis identifies constraint precision ($p$=0.012) and domain formalizability ($p$=0.04) as significant predictors of the gap, while C0 alone is marginally significant ($p$=0.09). The capability trap is not universal: it characterizes the majority of conditions, but positive operating points exist where model capacity, domain properties, and constraint quality align favorably.\n\n\\subsection{Qualitative Case Studies}\n\nAnalysis of 10 representative problems reveals three failure modes in low-precision constraints:\n(a) \\textit{Semantically empty}: constraints like $\\forall x, \\text{True}$ that are trivially satisfied by all answers;\n(b) \\textit{Circular}: constraints that restate the answer choice (e.g., $\\exists x, \\text{Answer}(x, \\text{`True'})$) without adding independent evidence;\n(c) \\textit{Valid but non-discriminative}: well-formed FOL that is equally consistent with all candidate answers.\n\nIn contrast, high-precision cases feature constraints with genuine logical content, such as $\\forall x, \\text{Human}(x) \\rightarrow \\text{Mortal}(x)$, which correctly exclude specific wrong answers. The bimodal pattern is not random: high-precision constraints concentrate in problems with clear logical structure (e.g., FOLIO syllogisms, GSM8K arithmetic relationships).\n\n%% ============================================================\n%% 5. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The capability trap as condition-dependent phenomenon.}\nOur results reframe the capability trap from a universal characterization to a boundary-condition analysis. The trap operates through a tension between two requirements: output diversity (C0 $>$ 5\\% to avoid degeneration) and constraint quality (precision $>$ 0.6 for MAX-SAT to outperform counting). In the majority of conditions, self-extracted constraints are non-discriminative (precision $\\sim$ 0.41), and MAX-SAT reduces to counting. But this is not inevitable. On approximately 31\\% of problems, models extract constraints with precision $>$ 0.6, and SICA provides 3--5pp gains on these subsets. The oracle experiment (+8.82pp with gold constraints) confirms that the aggregation mechanism itself is sound.\n\n\\paragraph{When does SICA help?}\nFour conditions in our study exceed the +3pp breakeven threshold: all involve either weaker models (7B--8B scale) with high baseline error rates, or domains where constraints have concrete numerical or binary structure (GSM8K, StrategyQA). The common thread is that these conditions produce constraint precision above 0.55, combined with C0 above 35\\%. Strong models (72B, QwQ-32B) fail either because diversity is too low (C0 $<$ 15\\%) or because their high baseline accuracy leaves little room for correction.\n\n\\paragraph{Practical deployment framework.}\nWe propose a two-stage decision process: (1) compute C0 on a pilot batch of 30--50 problems. If C0 $<$ 10\\%, SICA will degenerate to SC and should not be deployed. (2) If C0 $>$ 10\\%, estimate constraint precision on the pilot batch. If mean precision $>$ 0.55, SICA is likely to provide gains exceeding the 48.7\\% overhead cost. This framework reduces the deployment question from ``does symbolic aggregation work?'' to a measurable, condition-specific prediction.\n\n\\paragraph{Relation to published symbolic reasoning methods.}\nMethods such as DyLoS \\citep{dylos2026}, Aristotle \\citep{aristotle2025}, and FoVer \\citep{fover2025} achieve positive results on overlapping benchmarks using trained verifiers, logic-complete decomposition, or multi-paradigm solver selection. Our findings do not contradict these results. Rather, we isolate the specific limitation of \\emph{same-model self-extraction}: when the constraint generator and the reasoner are the same model, extraction quality becomes the binding bottleneck. External or trained verifiers bypass this bottleneck, explaining their success where SICA shows condition-dependent results.\n\n\\paragraph{Limitations.}\nOur study has several limitations. First, most positive signals come from small-sample conditions ($n$=30--60) that do not reach conventional significance thresholds individually. While the meta-analytic aggregate is significant, individual condition estimates carry wide confidence intervals. Second, we evaluate only English-language benchmarks. Third, our oracle experiment uses gold annotations available only for FOLIO, limiting the causal claim to formal logic. Fourth, the +48.7\\% overhead assumes sequential extraction; batched or cached extraction could reduce this substantially.\n\n%% ============================================================\n%% 6. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Self-consistency and extensions.}\n\\citet{wang2023selfconsistency} introduced SC as a simple decoding strategy that improves chain-of-thought reasoning via majority voting over sampled traces. Subsequent work extended this to universal SC for open-ended generation \\citep{chen2023usc}, confidence-weighted voting \\citep{taubenfeld2025weighted}, and diverse verifier ensembles \\citep{li2023diverse}. \\citet{loo2025scaling} showed that SC accuracy plateaus as $K$ increases, motivating richer aggregation mechanisms. Our work asks whether FOL constraint aggregation can break past this plateau.\n\n\\paragraph{Neurosymbolic reasoning.}\nLogic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} pioneered LLM-to-FOL translation for reasoning, documenting that translation errors limit downstream accuracy. DyLoS \\citep{dylos2026} uses dynamic logic solver selection, Aristotle \\citep{aristotle2025} employs trained verifiers, and FoVer \\citep{fover2025} combines formal verification with LLM reasoning. These methods achieve gains by using external verification or trained components, unlike our same-model self-extraction pipeline. Our oracle experiment confirms that the aggregation paradigm works, placing the bottleneck specifically at self-extraction quality.\n\n\\paragraph{Test-time compute scaling.}\n\\citet{snell2025scaling} formalize test-time compute scaling, showing that compute-optimal strategies depend on problem difficulty. DeepSeek-R1 \\citep{deepseek2025r1} demonstrates that extended reasoning chains can achieve strong performance without external tools. Our QwQ-32B results illustrate the consequence for symbolic aggregation: when a reasoning model reaches near-deterministic chains, diversity collapses and constraint-based methods become redundant.\n\n\\paragraph{Verification and reranking.}\nOutcome reward models \\citep{cobbe2021gsm8k} and process reward models \\citep{lightman2023prm} provide trained verification signals for reranking sampled solutions. Math-Shepherd \\citep{wang2024mathshepherd} scales process supervision to mathematical reasoning. These approaches use learned discriminative signals rather than self-extracted symbolic constraints, avoiding the capability trap we characterize.\n\n\\paragraph{Constraint satisfaction in NLP.}\nSATBench \\citep{satbench2025} evaluates LLMs' ability to solve satisfiability problems directly, while \\citet{llm_constraint2025} study constraint propagation in LLM reasoning. Our work uses MAX-SAT as an aggregation mechanism over extracted constraints, rather than asking LLMs to solve SAT instances.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic study of self-extracted constraint aggregation (SICA) across 14 conditions, identifying the capability trap as a condition-dependent phenomenon rather than a universal failure mode. The trap affects $\\sim$69\\% of multi-candidate problems where self-extracted constraints lack discriminative power, but $\\sim$31\\% of problems yield high-precision constraints where SICA provides genuine benefit. An oracle experiment confirms the aggregation mechanism works given quality constraints (+8.82pp), localizing the bottleneck to self-extraction. We propose a joint C0-precision diagnostic for practitioners: screen on diversity (C0 $<$ 10\\% rules out benefit), then assess constraint precision to predict whether the 48.7\\% overhead is justified.\n\nFuture work should investigate whether targeted extraction training or domain-specific prompting can shift the precision distribution toward the high-quality cluster, potentially expanding the effective operating regime of self-extracted symbolic aggregation.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Chen et~al.(2023)]{chen2023usc}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv preprint arXiv:2311.17311}, 2023.\n\n\\bibitem[Pan et~al.(2023)]{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et~al.(2023)]{olausson2023linc}\nT.~Olausson, A.~Gu, B.~Lipkin, C.~Zhang, A.~Solar-Lezama, J.~Tenenbaum, and R.~Levy.\n\\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[DyLoS(2026)]{dylos2026}\nDyLoS: Dynamic Logic Solver Selection for LLM Reasoning.\n\\newblock In \\emph{EACL}, 2026.\n\n\\bibitem[Aristotle(2025)]{aristotle2025}\nAristotle: Trained Verifiers for Logical Reasoning with Large Language Models.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[FoVer(2025)]{fover2025}\nFoVer: Formal Verification Meets LLM Reasoning.\n\\newblock In \\emph{TACL}, 2025.\n\n\\bibitem[Li et~al.(2023)]{li2023diverse}\nY.~Li, Z.~Lin, S.~Zhang, Q.~Fu, B.~Chen, J.-G.~Lou, and W.~Chen.\n\\newblock Making Language Models Better Reasoners with Step-Aware Verifier.\n\\newblock In \\emph{ACL}, 2023.\n\n\\bibitem[Loo et~al.(2025)]{loo2025scaling}\nN.~Loo, R.~Hasani, M.~Lechner, and D.~Rus.\n\\newblock Do More Samples Help? Scaling Self-Consistency Beyond Few Hundred.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Taubenfeld et~al.(2025)]{taubenfeld2025weighted}\nA.~Taubenfeld, Y.~Shichman, G.~Braverman, and L.~Wolf.\n\\newblock Confidence-Weighted Self-Consistency.\n\\newblock In \\emph{Findings of ACL}, 2025.\n\n\\bibitem[Snell et~al.(2025)]{snell2025scaling}\nC.~Snell, J.~Lee, K.~Xu, and A.~Kumar.\n\\newblock Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters.\n\\newblock In \\emph{ICLR (Oral)}, 2025.\n\n\\bibitem[DeepSeek(2025)]{deepseek2025r1}\nDeepSeek-AI.\n\\newblock DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.\n\\newblock \\emph{Nature}, 2025.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training Verifiers to Solve Math Word Problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023prm}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's Verify Step by Step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Wang et~al.(2024)]{wang2024mathshepherd}\nP.~Wang, L.~Li, Z.~Shao, R.~Xu, D.~Dai, Y.~Li, D.~Chen, Y.~Wu, and Z.~Sui.\n\\newblock Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[SATBench(2025)]{satbench2025}\nSATBench: Benchmarking LLMs on Satisfiability Problems.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[LLM Constraint(2025)]{llm_constraint2025}\nLLM Meets Constraint Propagation.\n\\newblock In \\emph{IJCAI}, 2025.\n\n\\bibitem[Liang et~al.(2023)]{liang2023debate}\nT.~Liang, Z.~He, W.~Jiao, X.~Wang, Y.~Wang, R.~Wang, Y.~Yang, Z.~Tu, and S.~Shi.\n\\newblock Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate.\n\\newblock \\emph{arXiv preprint arXiv:2305.19118}, 2023.\n\n\\bibitem[Du et~al.(2023)]{du2023debate}\nY.~Du, S.~Li, A.~Torralba, J.~Tenenbaum, and I.~Mordatch.\n\\newblock Improving Factuality and Reasoning in Language Models through Multiagent Debate.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[OpenAI(2024)]{openai2024o1}\nOpenAI.\n\\newblock Learning to Reason with LLMs.\n\\newblock \\emph{OpenAI Blog}, 2024.\n\n\\end{thebibliography}\n\n%% ============================================================\n%% APPENDIX\n%% ============================================================\n\\appendix\n\\section{Full K Ablation Results}\n\\label{app:kablation}\n\nTable~\\ref{tab:kablation} in the main text reports the full $K$ ablation. McNemar's $p$-value at $K$=11 (the highest-gap odd $K$) is 0.157, reflecting insufficient power at $n$=60 rather than absence of effect. The consistent +1.7 to +3.3pp gap across all $K$ values, including odd $K$ where exact ties are impossible, is suggestive of a genuine but small constraint exclusion signal on this 60-question subset.\n\n\\section{Overhead Breakdown}\n\\label{app:overhead}\n\n\\begin{table}[h]\n\\centering\n\\caption{Wall-time breakdown per problem ($n$=804, Qwen-14B).}\n\\label{tab:overhead_detail}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Component} & \\textbf{Mean (s)} & \\textbf{Fraction} \\\\\n\\midrule\nTrace generation ($K$=12) & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nMAX-SAT solving & 0.003 & $<$0.01\\% \\\\\nParsing + I/O & 1.0 & 1.7\\% \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overhead is dominated by the second LLM call for constraint extraction. The MAX-SAT solver itself is negligible. Cost-benefit analysis: at +3pp breakeven threshold, 4/14 conditions justify the overhead (Qwen-7B, LLaMA-8B D012, GSM8K pilot, StrategyQA 14B). The remaining 10 conditions do not.\n\n\\section{DeepSeek-R1-Distill Analysis}\n\\label{app:deepseek}\n\nDeepSeek-R1-Distill-LLaMA-8B on D012 ($n$=60): SICA 70.0\\%, SC 71.7\\%, $\\Delta$=$-$1.7pp, C0=55.0\\%. Despite being distilled from a reasoning model, the 8B parameter count produces instruction-like diversity. The extraction rate (85.0\\%) is slightly lower than comparable instruction models, likely due to truncated thinking traces. The contradiction rate (4.0\\%) is within normal range. Classification as instruction-scale is supported by C0 behavior matching other 7--8B instruction models rather than the near-zero C0 of full reasoning models.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88814200-c64c-49bc-9484-036f26c8e140",
  "isSidechain": false,
  "requestId": "req_011Cb8X5S9xgqoWAu4mzWPpr",
  "type": "assistant",
  "uuid": "88d59af3-db5a-47e6-a1ec-7990fec690f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2HDNec4KMD5DbYsftKR5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1336,
      "cache_read_input_tokens": 41632,
      "output_tokens": 12371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1336,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12371,
          "cache_read_input_tokens": 41632,
          "cache_creation_input_tokens": 1336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1336
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

_source line 19 · 2026-05-17T17:19:59.072Z_

<details><summary>↩ Tool result · `toolu_01MbzsFNETabNaq2Ar41PgSE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88d59af3-db5a-47e6-a1ec-7990fec690f1",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "6972bdf2-3e82-47fd-bdb7-514fe47f0863",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\\usepackage{tablefootnote}\n\n\\title{When Do Self-Extracted Constraints Improve LLM Reasoning? \\\\ Characterizing the Capability Trap}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%% ABSTRACT\n%% ============================================================\n\\begin{abstract}\nSymbolic constraint aggregation, where a Large Language Model (LLM) extracts First-Order Logic (FOL) constraints from its own reasoning traces and a MAX-SAT solver selects the most consistent answer, has been proposed as a principled alternative to majority voting (Self-Consistency, SC). We present a systematic study of Self-Extracted Invariant Constraint Aggregation (SICA) across 14 experimental conditions spanning 5 model families, 5 reasoning domains, and over 1,400 problems. A meta-analysis yields a small positive overall effect ($\\Delta$=+1.8pp, $p$=0.03) but with substantial heterogeneity ($I^2$=0.62), indicating that the benefit is condition-dependent rather than universal. We identify a \\emph{capability trap}: in the majority of conditions ($\\sim$69\\% of multi-candidate problems), self-extracted constraints lack discriminative power (precision $\\sim$0.41), reducing MAX-SAT to counting. However, a bimodal precision distribution reveals that $\\sim$31\\% of problems yield high-precision constraints (mean 0.74), on which SICA outperforms SC by +3--5pp. An oracle experiment replacing self-extracted constraints with gold FOL annotations achieves +8.82pp ($p<$0.001), confirming that the aggregation mechanism is effective when given discriminative input. We characterize the sufficient conditions for the capability trap (model capacity, domain formalizability, precision threshold) and propose a joint C0-precision diagnostic framework for practitioners deciding whether symbolic aggregation is worth the overhead.\n\\end{abstract}\n\n%% ============================================================\n%% 1. INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nSelf-Consistency (SC) decoding \\citep{wang2023selfconsistency} improves LLM reasoning by sampling multiple chains of thought and selecting the majority answer. A natural extension is to extract structured constraints from these reasoning traces and use a formal solver to aggregate them, potentially capturing logical relationships that simple counting misses. Several methods pursue this direction: Logic-LM \\citep{pan2023logiclm} translates problems into FOL for solver-based verification, LINC \\citep{olausson2023linc} uses neurosymbolic integration, and recent work on DyLoS \\citep{dylos2026}, Aristotle \\citep{aristotle2025}, and FoVer \\citep{fover2025} shows gains using trained or external verifiers. But a fundamental question remains open: \\emph{when does self-extracted symbolic aggregation actually help over simple majority voting?}\n\nThis question matters because symbolic aggregation incurs substantial overhead. Constraint extraction nearly doubles inference time (+48.7\\%), and deploying a MAX-SAT solver adds engineering complexity. If practitioners cannot predict when the investment pays off, the method risks being either universally adopted at a loss or universally dismissed despite having genuine operating points.\n\nWe study this question through SICA (Self-Extracted Invariant Constraint Aggregation), which extracts FOL constraints from $K$ reasoning traces and uses weighted MAX-SAT to select the answer satisfying the most constraints. Unlike methods that use trained verifiers or external knowledge, SICA relies entirely on the same model for both generation and constraint extraction, isolating the fundamental capability question: can an LLM extract constraints from its own reasoning that are good enough to beat counting?\n\nOur study spans 14 experimental conditions: 5 model families (Qwen-2.5 at 7B/14B/72B, LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5 domains (FOLIO, ProofWriter, StrategyQA, GSM8K, ARC-Challenge), totaling over 1,400 evaluated problems. The answer we find is nuanced: SICA's benefit is condition-dependent, governed by a capability trap that affects the majority but not the entirety of conditions.\n\nWe make three contributions:\n\\begin{enumerate}\n    \\item \\textbf{Boundary conditions for the capability trap.} We identify three factors that jointly determine whether self-extracted constraints improve over voting: model capacity (weaker models benefit more), domain formalizability (mathematical and binary-answer domains yield higher constraint precision), and a precision threshold ($>$0.6) above which MAX-SAT adds genuine value. Approximately 31\\% of multi-candidate problems meet this threshold; on these, SICA outperforms SC.\n    \\item \\textbf{Mechanism validation via oracle control.} Replacing self-extracted constraints with gold FOL annotations yields +8.82pp over SC ($p<$0.001, $n$=204), proving that the MAX-SAT aggregation mechanism is effective given discriminative constraints. The capability trap is a quality bottleneck in self-extraction, not a flaw in the aggregation paradigm.\n    \\item \\textbf{Joint C0-precision diagnostic framework.} We show that candidate diversity (C0) alone is necessary but insufficient for predicting SICA benefit. C0 $<$ 5\\% guarantees degeneration to SC (specificity 1.0), but among high-C0 conditions, constraint precision is the binding moderator ($p$=0.012 in meta-regression). We propose a two-stage deployment check: first screen on C0, then estimate constraint precision on a pilot sample.\n\\end{enumerate}\n\n%% ============================================================\n%% 2. METHOD\n%% ============================================================\n\\section{Method: SICA Pipeline}\n\n\\subsection{Overview}\n\nGiven a reasoning problem $q$, SICA proceeds in four stages:\n(1) sample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from an LLM;\n(2) extract a candidate answer $a_i$ and a set of FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ from each trace $t_i$;\n(3) evaluate each constraint $c_{i,j}$ against each candidate answer $a_k$ to build a weighted MAX-SAT instance;\n(4) solve the MAX-SAT instance to select the answer satisfying the maximum total weight of constraints.\n\n\\subsection{Trace Generation}\n\nWe sample $K$ independent reasoning traces using temperature $\\tau > 0$. Each trace produces a natural-language chain of thought, from which we extract both the final answer and any intermediate logical constraints the model articulates.\n\n\\subsection{Constraint Extraction}\n\nA second LLM call (using the same model) receives the trace $t_i$ and a structured prompt requesting FOL constraints. The extraction prompt asks the model to formalize key reasoning steps as first-order logic statements. We parse the output to obtain $\\mathcal{C}_i$ and $a_i$. Extraction succeeds on 82--95\\% of traces depending on the model.\n\n\\subsection{MAX-SAT Aggregation}\n\nLet $\\mathcal{A} = \\{a_1, \\ldots, a_L\\}$ be the set of distinct candidate answers across all $K$ traces. For each candidate $a_\\ell$ and constraint $c_{i,j}$, we evaluate whether $c_{i,j}$ is consistent with $a_\\ell$ (a binary compatibility check). We construct a weighted MAX-SAT instance where each clause corresponds to a constraint-candidate pair, weighted by the number of traces supporting that constraint. The answer maximizing total satisfied weight is selected.\n\nWhen constraints are non-discriminative (equally compatible with all candidates), MAX-SAT reduces to weighted counting, equivalent to majority voting with trace-level weights.\n\n\\subsection{Candidate Diversity Metric: C0}\n\nWe define \\emph{candidate diversity} C0 as the fraction of problems where more than one distinct answer appears across $K$ traces:\n\\[\n    \\text{C0} = \\frac{|\\{q : |\\mathcal{A}_q| > 1\\}|}{|Q|}\n\\]\nC0 measures the potential scope for constraint-based re-ranking. When C0 = 0, all traces agree and SICA is identical to SC.\n\n%% ============================================================\n%% 3. EXPERIMENTS\n%% ============================================================\n\\section{Experimental Setup}\n\n\\subsection{Models}\n\nWe evaluate six models spanning three paradigms:\n\\textbf{Instruction-scale}: Qwen-2.5-7B-Instruct, Qwen-2.5-14B-Instruct, Qwen-2.5-72B-Instruct (AWQ 4-bit), LLaMA-3.1-8B-Instruct.\n\\textbf{Distilled reasoning}: DeepSeek-R1-Distill-LLaMA-8B.\n\\textbf{Full reasoning}: QwQ-32B.\n\n\\subsection{Domains}\n\nFive reasoning domains: FOLIO (formal deductive logic, 3-class), ProofWriter (rule-based logical inference), StrategyQA (commonsense binary questions), GSM8K (grade-school math), and ARC-Challenge (science multiple-choice).\n\n\\subsection{Protocol}\n\nUnless noted, we use $K$=12 traces per problem. We report accuracy, the SICA$-$SC gap ($\\Delta$pp), McNemar's test $p$-value, and C0. Sample sizes range from $n$=30 (pilots) to $n$=804 (powered main experiment).\n\n%% ============================================================\n%% 4. RESULTS\n%% ============================================================\n\\section{Results}\n\n\\subsection{Main Results Across Conditions}\n\nTable~\\ref{tab:main} reports SICA and SC accuracy across all model-domain conditions. The results reveal a heterogeneous pattern: four conditions show positive gaps ($\\Delta > +4$pp), seven are null ($|\\Delta| < 2$pp), and three are negative.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results across model-domain conditions. $\\Delta$ = SICA $-$ SC in percentage points. Bold indicates $\\Delta > +4$pp. $^\\dagger$Pilot ($n$=30). $^\\ddagger$Near-degenerate (C0 $<$ 10\\%).}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{$n$} & \\textbf{SC} & \\textbf{SICA} & \\textbf{$\\Delta$pp} & \\textbf{C0\\%} & \\textbf{$p$} \\\\\n\\midrule\nQwen-14B & D012 mix & 804 & 76.2 & 76.5 & +0.3 & 38.2 & 0.87 \\\\\nQwen-7B & D012 mix & 60 & 56.7 & 61.7 & \\textbf{+5.0} & 71.7 & 0.083 \\\\\nQwen-72B & D012 mix & 60 & 83.3 & 81.7 & $-$1.7 & 15.0 & 1.0 \\\\\nLLaMA-8B & D012 mix & 60 & 61.7 & 68.3 & \\textbf{+6.7} & 61.7 & 0.109 \\\\\nLLaMA-8B & FOLIO & 204 & 63.2 & 62.3 & $-$0.9 & 61.8 & 0.774 \\\\\nLLaMA-8B & StrategyQA & 200 & 72.0 & 74.0 & +2.0 & 41.0 & 0.424 \\\\\nDeepSeek-R1 & D012 mix & 60 & 71.7 & 70.0 & $-$1.7 & 55.0 & 1.0 \\\\\nQwQ-32B & Aggregate & 46 & --- & --- & 0.0 & 3.6$^\\ddagger$ & --- \\\\\nQwen-14B & GSM8K$^\\dagger$ & 30 & 80.0 & 86.7 & \\textbf{+6.7} & 36.7 & 0.317 \\\\\nQwen-14B & StrategyQA & 60 & 55.0 & 60.0 & \\textbf{+5.0} & 38.3 & 0.157 \\\\\nQwen-14B & ARC-Chall.$^\\ddagger$ & 60 & 93.3 & 91.7 & $-$1.7 & 6.7 & 1.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeveral patterns emerge. First, weaker models show larger positive gaps: Qwen-7B (+5.0pp, C0=71.7\\%) and LLaMA-8B on D012 (+6.7pp, C0=61.7\\%), compared to Qwen-14B on the same domain (+0.3pp). Second, new domains outside formal logic show positive signals: GSM8K (+6.7pp) and StrategyQA (+5.0pp for Qwen-14B). Third, high-capacity models and low-diversity conditions produce null or negative results: Qwen-72B ($-$1.7pp, C0=15\\%), QwQ-32B (C0=3.6\\%, SICA degenerates to SC), and ARC-Challenge ($-$1.7pp, C0=6.7\\%).\n\nThe LLaMA-8B FOLIO result ($n$=204, $\\Delta$=$-$0.9pp) contrasts with the D012 subset result (+6.7pp on $n$=60), suggesting the D012 subsample over-represented high-precision problems. On the high-precision subset of full FOLIO (42 problems with constraint precision $>$ 0.6), SICA achieves +4.8pp, consistent with condition-dependent benefit.\n\n\\subsection{Model Capacity Scaling}\n\nWithin the Qwen family, we observe a clear capacity-dependent pattern (Table~\\ref{tab:main}). Qwen-7B (C0=71.7\\%, precision=0.54) shows $\\Delta$=+5.0pp; Qwen-14B (C0=38.2\\%) shows $\\Delta$=+0.3pp; Qwen-72B (C0=15.0\\%, precision=0.61) shows $\\Delta$=$-$1.7pp. Weaker models produce higher diversity but lower constraint precision, while stronger models produce lower diversity but higher precision. The net effect favors weaker models because their higher error rate creates more room for constraint-based correction, even when constraint quality is imperfect.\n\n\\subsection{Constraint Quality Analysis}\n\\label{sec:precision}\n\nPer-problem analysis of 307 multi-candidate problems from the Qwen-14B $n$=804 condition reveals a bimodal constraint precision distribution (Hartigan's dip test $p$=0.04). Two clusters emerge: 95 high-precision problems (mean precision 0.74) and 212 low-precision problems (mean precision 0.41). Table~\\ref{tab:precision} summarizes the distribution.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constraint precision distribution across 307 multi-candidate problems. SICA win rate: fraction of discordant pairs where SICA selects the correct answer.}\n\\label{tab:precision}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Cluster} & \\textbf{$n$} & \\textbf{Mean Prec.} & \\textbf{SICA Win Rate} & \\textbf{Fraction} \\\\\n\\midrule\nHigh-precision ($>$0.6) & 95 & 0.74 & 0.68 & 31\\% \\\\\nLow-precision ($<$0.6) & 212 & 0.41 & 0.44 & 69\\% \\\\\n\\midrule\nOverall & 307 & 0.52 & 0.52 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn high-precision problems, SICA wins 68\\% of discordant cases, providing genuine discriminative value. On the low-precision majority, SICA wins only 44\\%, performing slightly worse than chance due to noisy constraint-based re-ranking. Precision correlates significantly with SICA correctness ($r$=0.28, $p$=0.005) and with per-problem C0 ($r$=0.31, $p$=0.002).\n\nDomain-level precision varies: GSM8K achieves the highest mean precision (0.62), followed by StrategyQA (0.58), FOLIO (0.54), and ProofWriter (0.50). Mathematical constraints with concrete numerical content (e.g., $x + y = 15$) are easier to correctly extract than modal logic statements in NLI tasks.\n\n\\subsection{Oracle Control Experiment}\n\nTo isolate whether the bottleneck is in constraint extraction or aggregation, we replace self-extracted constraints with gold FOL annotations from the FOLIO dataset and evaluate MAX-SAT aggregation on $n$=204 problems. Oracle-SICA achieves 88.24\\% accuracy, compared to SC at 79.41\\%, a gain of +8.82pp ($p < 0.001$). This confirms that the MAX-SAT aggregation mechanism is effective when given discriminative constraints. The capability trap is exclusively a self-extraction quality problem.\n\n\\subsection{Constraint Ablation}\n\\label{sec:ablation}\n\nTable~\\ref{tab:ablation} compares three aggregation variants on the Qwen-14B $n$=804 condition: full MAX-SAT, count-only (ignoring satisfiability structure), and random-weight (shuffled constraint weights).\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation ablation on Qwen-14B ($n$=804). High-precision subset: problems with constraint precision $>$ 0.6 ($n$=95).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Overall Acc.} & \\textbf{$\\Delta$ vs SC} & \\textbf{HP Subset Acc.} & \\textbf{HP $\\Delta$ vs SC} \\\\\n\\midrule\nSC (baseline) & 76.24 & --- & --- & --- \\\\\nSICA (MAX-SAT) & 76.49 & +0.25 & 82.1 & --- \\\\\nCount-only & 75.87 & $-$0.37 & 78.9 & --- \\\\\nRandom-weight & 75.50 & $-$0.74 & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{High-precision subset ($n$=95):}} \\\\\nMAX-SAT vs count-only & \\multicolumn{4}{c}{+3.2pp ($p$=0.083)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOverall, all three variants perform within 1pp of SC, with 798/804 problems producing identical answers across MAX-SAT and count-only. The aggregation mechanism is latent: on the full dataset, non-discriminative constraints reduce all methods to counting. On the high-precision subset ($n$=95), MAX-SAT outperforms count-only by 3.2pp ($p$=0.083), indicating that satisfiability structure provides additional signal when constraints are genuinely discriminative.\n\n\\subsection{Baseline Comparisons}\n\n\\paragraph{Weighted SC variants.} Table~\\ref{tab:baselines} compares SICA against simpler weighted voting schemes on the $n$=804 condition.\n\n\\begin{table}[t]\n\\centering\n\\caption{SICA vs weighted SC baselines and Logic-LM (Qwen-14B). All differences are non-significant.}\n\\label{tab:baselines}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs SC} \\\\\n\\midrule\nSC (uniform voting) & 76.24 & --- \\\\\nSICA (MAX-SAT) & 76.49 & +0.25 \\\\\nInverse-length weighted & 76.99 & +0.75 \\\\\nLength weighted & 75.38 & $-$0.86 \\\\\nConstraint-count weighted & 75.87 & $-$0.37 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Logic-LM comparison (FOLIO, $n$=204):}} \\\\\nLogic-LM $\\times$ $K$=12 & 77.9 & $-$1.5 vs SC \\\\\nSC & 79.4 & --- \\\\\nSICA & 79.4 & 0.0 vs SC \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nInverse-length weighted SC slightly outperforms both SC and SICA (+0.75pp, $p$=0.317), suggesting that trace brevity (a proxy for confidence) captures comparable signal without extraction overhead. Logic-LM $\\times$ $K$ (per-trace FOL verification with majority vote) achieves 77.9\\% on FOLIO, 1.5pp below SC, because single-trace translation errors accumulate across $K$ independent attempts.\n\n\\paragraph{Tiebreak analysis.} On 5/60 exactly tied problems (Qwen-14B D012), SICA's constraint-informed tiebreak wins 80\\% (4/5), compared to 50\\% for random and 60\\% for alphabetical tiebreak. Beyond tiebreak, SICA produces an additional $\\sim$1.0pp gain from non-tie flips. The tiebreak advantage is real but affects too few problems ($\\sim$8.3\\% tie rate) to be practically significant.\n\n\\subsection{C0 Diagnostic Analysis}\n\nTable~\\ref{tab:c0} and the corresponding analysis examine the relationship between C0 and the SICA-SC gap across all 12 non-degenerate conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{C0 vs SICA$-$SC gap across experimental conditions. Conditions with C0 $<$ 5\\% (QwQ-32B) produce $\\Delta$=0 by construction.}\n\\label{tab:c0}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nPearson $r$ (C0 vs $\\Delta$) & 0.38 & 0.08 \\\\\nSpearman $\\rho$ & 0.42 & 0.06 \\\\\nLinear $R^2$ & 0.14 & --- \\\\\nC0 $<$ 5\\%: all $\\Delta$=0 & Specificity 1.0 & --- \\\\\nC0 $>$ 30\\%: mean $\\Delta$ & +1.8pp & --- \\\\\nC0 $>$ 30\\%: $\\Delta$ range & [$-$3.3, +6.7] & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nC0 shows a moderate positive correlation with the SICA gap ($r$=0.38, $p$=0.08), but explains only 14\\% of variance. The key finding is asymmetric: C0 $<$ 5\\% reliably predicts degeneration (specificity 1.0), but high C0 does not guarantee benefit. Among conditions with C0 $>$ 30\\%, the gap ranges from $-$3.3pp to +6.7pp. Constraint precision is the critical moderator within high-C0 conditions ($p$=0.012 in meta-regression, Section~\\ref{sec:meta}).\n\n\\subsection{K Sensitivity}\n\\label{sec:k_ablation}\n\nWe vary $K \\in \\{6, 8, 11, 12, 16, 20\\}$ on the Qwen-14B D012 $n$=60 subset (Table~\\ref{tab:kablation}). The SICA$-$SC gap is consistently small (+1.7 to +3.3pp) and never significant ($p > 0.15$). At odd $K$=11 (where exact ties are impossible), SICA still achieves +3.3pp, confirming that the mechanism is not purely tiebreak-driven. This gap matches $K$=12, suggesting constraint exclusion provides a small genuine signal on this subset that is independent of tie resolution.\n\n\\begin{table}[t]\n\\centering\n\\caption{$K$ sensitivity on Qwen-14B D012 ($n$=60).}\n\\label{tab:kablation}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{$K$} & \\textbf{SICA} & \\textbf{SC} & \\textbf{$\\Delta$pp} \\\\\n\\midrule\n6 & 75.0 & 73.3 & +1.7 \\\\\n8 & 76.7 & 75.0 & +1.7 \\\\\n11 & 76.7 & 73.3 & +3.3 \\\\\n12 & 73.3 & 70.0 & +3.3 \\\\\n16 & 75.0 & 73.3 & +1.7 \\\\\n20 & 73.3 & 71.7 & +1.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Reasoning Model Behavior}\n\nQwQ-32B produces near-deterministic reasoning chains with effective C0 of 3.6\\% across 46 problems (AIME, ProofWriter, FOLIO). With $\\Delta$=0.0pp on all three subsets, SICA degenerates to SC by construction. Full reasoning models' extended chain-of-thought process converges to consistent answers, eliminating the diversity that SICA requires.\n\nDeepSeek-R1-Distill-LLaMA-8B, despite being distilled from a reasoning model, behaves like an instruction model (C0=55.0\\%). Its 8B parameter count is insufficient for deterministic reasoning chains, producing instruction-like diversity. However, SICA shows $\\Delta$=$-$1.7pp ($p$=1.0), consistent with the capability trap: high diversity but non-discriminative constraints due to truncated thinking traces degrading extraction quality.\n\n\\subsection{Overhead Analysis}\n\\label{sec:overhead}\n\nOn the $n$=804 condition, mean wall time per problem is 61.6 seconds: 31.6s for trace generation (51.3\\%) and 29.0s for constraint extraction (47.0\\%). MAX-SAT solving takes 0.003s (negligible). SICA's overhead is 48.7\\% beyond standard SC, at an extraction cost of \\$0.018 per problem.\n\nThe breakeven point is approximately +3pp: conditions where SICA gains exceed 3pp justify the overhead. Four of our 14 conditions exceed this threshold (Qwen-7B +5.0, LLaMA-8B D012 +6.7, GSM8K +6.7, StrategyQA 14B +5.0), all characterized by moderate-to-high C0 ($>$35\\%) and at least moderate constraint precision ($>$0.55).\n\n\\subsection{Meta-Analysis}\n\\label{sec:meta}\n\nTable~\\ref{tab:meta} summarizes the meta-analytic results across all 14 conditions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Meta-analytic summary across 14 conditions ($N$=1,482 total problems).}\n\\label{tab:meta}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nOverall $\\Delta$ (random effects) & +1.8pp \\\\\n95\\% CI & [+0.2, +3.4] \\\\\n$p$-value & 0.03 \\\\\n$I^2$ (heterogeneity) & 0.62 \\\\\n$Q$-test $p$ & 0.008 \\\\\n\\midrule\nPositive conditions ($\\Delta > +4$pp) & 4 / 14 \\\\\nNull conditions ($|\\Delta| < 2$pp) & 7 / 14 \\\\\nNegative conditions ($\\Delta < -2$pp) & 3 / 14 \\\\\n\\midrule\nMean $\\Delta$ (positive conditions) & +5.1pp \\\\\nMean $\\Delta$ (null conditions) & +0.1pp \\\\\nMean $\\Delta$ (negative conditions) & $-$2.5pp \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Moderator analysis:}} \\\\\nConstraint precision & $p$ = 0.012 \\\\\nDomain formalizability & $p$ = 0.04 \\\\\nC0 & $p$ = 0.09 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overall effect is small but statistically significant ($\\Delta$=+1.8pp, $p$=0.03). However, the substantial heterogeneity ($I^2$=0.62, $Q$ $p$=0.008) indicates that a single overall estimate is inadequate. Moderator analysis identifies constraint precision ($p$=0.012) and domain formalizability ($p$=0.04) as significant predictors of the gap, while C0 alone is marginally significant ($p$=0.09). The capability trap is not universal: it characterizes the majority of conditions, but positive operating points exist where model capacity, domain properties, and constraint quality align favorably.\n\n\\subsection{Qualitative Case Studies}\n\nAnalysis of 10 representative problems reveals three failure modes in low-precision constraints:\n(a) \\textit{Semantically empty}: constraints like $\\forall x, \\text{True}$ that are trivially satisfied by all answers;\n(b) \\textit{Circular}: constraints that restate the answer choice (e.g., $\\exists x, \\text{Answer}(x, \\text{`True'})$) without adding independent evidence;\n(c) \\textit{Valid but non-discriminative}: well-formed FOL that is equally consistent with all candidate answers.\n\nIn contrast, high-precision cases feature constraints with genuine logical content, such as $\\forall x, \\text{Human}(x) \\rightarrow \\text{Mortal}(x)$, which correctly exclude specific wrong answers. The bimodal pattern is not random: high-precision constraints concentrate in problems with clear logical structure (e.g., FOLIO syllogisms, GSM8K arithmetic relationships).\n\n%% ============================================================\n%% 5. DISCUSSION\n%% ============================================================\n\\section{Discussion}\n\n\\paragraph{The capability trap as condition-dependent phenomenon.}\nOur results reframe the capability trap from a universal characterization to a boundary-condition analysis. The trap operates through a tension between two requirements: output diversity (C0 $>$ 5\\% to avoid degeneration) and constraint quality (precision $>$ 0.6 for MAX-SAT to outperform counting). In the majority of conditions, self-extracted constraints are non-discriminative (precision $\\sim$ 0.41), and MAX-SAT reduces to counting. But this is not inevitable. On approximately 31\\% of problems, models extract constraints with precision $>$ 0.6, and SICA provides 3--5pp gains on these subsets. The oracle experiment (+8.82pp with gold constraints) confirms that the aggregation mechanism itself is sound.\n\n\\paragraph{When does SICA help?}\nFour conditions in our study exceed the +3pp breakeven threshold: all involve either weaker models (7B--8B scale) with high baseline error rates, or domains where constraints have concrete numerical or binary structure (GSM8K, StrategyQA). The common thread is that these conditions produce constraint precision above 0.55, combined with C0 above 35\\%. Strong models (72B, QwQ-32B) fail either because diversity is too low (C0 $<$ 15\\%) or because their high baseline accuracy leaves little room for correction.\n\n\\paragraph{Practical deployment framework.}\nWe propose a two-stage decision process: (1) compute C0 on a pilot batch of 30--50 problems. If C0 $<$ 10\\%, SICA will degenerate to SC and should not be deployed. (2) If C0 $>$ 10\\%, estimate constraint precision on the pilot batch. If mean precision $>$ 0.55, SICA is likely to provide gains exceeding the 48.7\\% overhead cost. This framework reduces the deployment question from ``does symbolic aggregation work?'' to a measurable, condition-specific prediction.\n\n\\paragraph{Relation to published symbolic reasoning methods.}\nMethods such as DyLoS \\citep{dylos2026}, Aristotle \\citep{aristotle2025}, and FoVer \\citep{fover2025} achieve positive results on overlapping benchmarks using trained verifiers, logic-complete decomposition, or multi-paradigm solver selection. Our findings do not contradict these results. Rather, we isolate the specific limitation of \\emph{same-model self-extraction}: when the constraint generator and the reasoner are the same model, extraction quality becomes the binding bottleneck. External or trained verifiers bypass this bottleneck, explaining their success where SICA shows condition-dependent results.\n\n\\paragraph{Limitations.}\nOur study has several limitations. First, most positive signals come from small-sample conditions ($n$=30--60) that do not reach conventional significance thresholds individually. While the meta-analytic aggregate is significant, individual condition estimates carry wide confidence intervals. Second, we evaluate only English-language benchmarks. Third, our oracle experiment uses gold annotations available only for FOLIO, limiting the causal claim to formal logic. Fourth, the +48.7\\% overhead assumes sequential extraction; batched or cached extraction could reduce this substantially.\n\n%% ============================================================\n%% 6. RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{Self-consistency and extensions.}\n\\citet{wang2023selfconsistency} introduced SC as a simple decoding strategy that improves chain-of-thought reasoning via majority voting over sampled traces. Subsequent work extended this to universal SC for open-ended generation \\citep{chen2023usc}, confidence-weighted voting \\citep{taubenfeld2025weighted}, and diverse verifier ensembles \\citep{li2023diverse}. \\citet{loo2025scaling} showed that SC accuracy plateaus as $K$ increases, motivating richer aggregation mechanisms. Our work asks whether FOL constraint aggregation can break past this plateau.\n\n\\paragraph{Neurosymbolic reasoning.}\nLogic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} pioneered LLM-to-FOL translation for reasoning, documenting that translation errors limit downstream accuracy. DyLoS \\citep{dylos2026} uses dynamic logic solver selection, Aristotle \\citep{aristotle2025} employs trained verifiers, and FoVer \\citep{fover2025} combines formal verification with LLM reasoning. These methods achieve gains by using external verification or trained components, unlike our same-model self-extraction pipeline. Our oracle experiment confirms that the aggregation paradigm works, placing the bottleneck specifically at self-extraction quality.\n\n\\paragraph{Test-time compute scaling.}\n\\citet{snell2025scaling} formalize test-time compute scaling, showing that compute-optimal strategies depend on problem difficulty. DeepSeek-R1 \\citep{deepseek2025r1} demonstrates that extended reasoning chains can achieve strong performance without external tools. Our QwQ-32B results illustrate the consequence for symbolic aggregation: when a reasoning model reaches near-deterministic chains, diversity collapses and constraint-based methods become redundant.\n\n\\paragraph{Verification and reranking.}\nOutcome reward models \\citep{cobbe2021gsm8k} and process reward models \\citep{lightman2023prm} provide trained verification signals for reranking sampled solutions. Math-Shepherd \\citep{wang2024mathshepherd} scales process supervision to mathematical reasoning. These approaches use learned discriminative signals rather than self-extracted symbolic constraints, avoiding the capability trap we characterize.\n\n\\paragraph{Constraint satisfaction in NLP.}\nSATBench \\citep{satbench2025} evaluates LLMs' ability to solve satisfiability problems directly, while \\citet{llm_constraint2025} study constraint propagation in LLM reasoning. Our work uses MAX-SAT as an aggregation mechanism over extracted constraints, rather than asking LLMs to solve SAT instances.\n\n%% ============================================================\n%% 7. CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe presented a systematic study of self-extracted constraint aggregation (SICA) across 14 conditions, identifying the capability trap as a condition-dependent phenomenon rather than a universal failure mode. The trap affects $\\sim$69\\% of multi-candidate problems where self-extracted constraints lack discriminative power, but $\\sim$31\\% of problems yield high-precision constraints where SICA provides genuine benefit. An oracle experiment confirms the aggregation mechanism works given quality constraints (+8.82pp), localizing the bottleneck to self-extraction. We propose a joint C0-precision diagnostic for practitioners: screen on diversity (C0 $<$ 10\\% rules out benefit), then assess constraint precision to predict whether the 48.7\\% overhead is justified.\n\nFuture work should investigate whether targeted extraction training or domain-specific prompting can shift the precision distribution toward the high-quality cluster, potentially expanding the effective operating regime of self-extracted symbolic aggregation.\n\n%% ============================================================\n%% REFERENCES\n%% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Chen et~al.(2023)]{chen2023usc}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv preprint arXiv:2311.17311}, 2023.\n\n\\bibitem[Pan et~al.(2023)]{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem[Olausson et~al.(2023)]{olausson2023linc}\nT.~Olausson, A.~Gu, B.~Lipkin, C.~Zhang, A.~Solar-Lezama, J.~Tenenbaum, and R.~Levy.\n\\newblock LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[DyLoS(2026)]{dylos2026}\nDyLoS: Dynamic Logic Solver Selection for LLM Reasoning.\n\\newblock In \\emph{EACL}, 2026.\n\n\\bibitem[Aristotle(2025)]{aristotle2025}\nAristotle: Trained Verifiers for Logical Reasoning with Large Language Models.\n\\newblock In \\emph{ACL}, 2025.\n\n\\bibitem[FoVer(2025)]{fover2025}\nFoVer: Formal Verification Meets LLM Reasoning.\n\\newblock In \\emph{TACL}, 2025.\n\n\\bibitem[Li et~al.(2023)]{li2023diverse}\nY.~Li, Z.~Lin, S.~Zhang, Q.~Fu, B.~Chen, J.-G.~Lou, and W.~Chen.\n\\newblock Making Language Models Better Reasoners with Step-Aware Verifier.\n\\newblock In \\emph{ACL}, 2023.\n\n\\bibitem[Loo et~al.(2025)]{loo2025scaling}\nN.~Loo, R.~Hasani, M.~Lechner, and D.~Rus.\n\\newblock Do More Samples Help? Scaling Self-Consistency Beyond Few Hundred.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Taubenfeld et~al.(2025)]{taubenfeld2025weighted}\nA.~Taubenfeld, Y.~Shichman, G.~Braverman, and L.~Wolf.\n\\newblock Confidence-Weighted Self-Consistency.\n\\newblock In \\emph{Findings of ACL}, 2025.\n\n\\bibitem[Snell et~al.(2025)]{snell2025scaling}\nC.~Snell, J.~Lee, K.~Xu, and A.~Kumar.\n\\newblock Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters.\n\\newblock In \\emph{ICLR (Oral)}, 2025.\n\n\\bibitem[DeepSeek(2025)]{deepseek2025r1}\nDeepSeek-AI.\n\\newblock DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.\n\\newblock \\emph{Nature}, 2025.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training Verifiers to Solve Math Word Problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023prm}\nH.~Lightman, V.~Kosaraju, Y.~Burda, H.~Edwards, B.~Baker, T.~Lee, J.~Leike, J.~Schulman, I.~Sutskever, and K.~Cobbe.\n\\newblock Let's Verify Step by Step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Wang et~al.(2024)]{wang2024mathshepherd}\nP.~Wang, L.~Li, Z.~Shao, R.~Xu, D.~Dai, Y.~Li, D.~Chen, Y.~Wu, and Z.~Sui.\n\\newblock Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[SATBench(2025)]{satbench2025}\nSATBench: Benchmarking LLMs on Satisfiability Problems.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[LLM Constraint(2025)]{llm_constraint2025}\nLLM Meets Constraint Propagation.\n\\newblock In \\emph{IJCAI}, 2025.\n\n\\bibitem[Liang et~al.(2023)]{liang2023debate}\nT.~Liang, Z.~He, W.~Jiao, X.~Wang, Y.~Wang, R.~Wang, Y.~Yang, Z.~Tu, and S.~Shi.\n\\newblock Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate.\n\\newblock \\emph{arXiv preprint arXiv:2305.19118}, 2023.\n\n\\bibitem[Du et~al.(2023)]{du2023debate}\nY.~Du, S.~Li, A.~Torralba, J.~Tenenbaum, and I.~Mordatch.\n\\newblock Improving Factuality and Reasoning in Language Models through Multiagent Debate.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[OpenAI(2024)]{openai2024o1}\nOpenAI.\n\\newblock Learning to Reason with LLMs.\n\\newblock \\emph{OpenAI Blog}, 2024.\n\n\\end{thebibliography}\n\n%% ============================================================\n%% APPENDIX\n%% ============================================================\n\\appendix\n\\section{Full K Ablation Results}\n\\label{app:kablation}\n\nTable~\\ref{tab:kablation} in the main text reports the full $K$ ablation. McNemar's $p$-value at $K$=11 (the highest-gap odd $K$) is 0.157, reflecting insufficient power at $n$=60 rather than absence of effect. The consistent +1.7 to +3.3pp gap across all $K$ values, including odd $K$ where exact ties are impossible, is suggestive of a genuine but small constraint exclusion signal on this 60-question subset.\n\n\\section{Overhead Breakdown}\n\\label{app:overhead}\n\n\\begin{table}[h]\n\\centering\n\\caption{Wall-time breakdown per problem ($n$=804, Qwen-14B).}\n\\label{tab:overhead_detail}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Component} & \\textbf{Mean (s)} & \\textbf{Fraction} \\\\\n\\midrule\nTrace generation ($K$=12) & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nMAX-SAT solving & 0.003 & $<$0.01\\% \\\\\nParsing + I/O & 1.0 & 1.7\\% \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe overhead is dominated by the second LLM call for constraint extraction. The MAX-SAT solver itself is negligible. Cost-benefit analysis: at +3pp breakeven threshold, 4/14 conditions justify the overhead (Qwen-7B, LLaMA-8B D012, GSM8K pilot, StrategyQA 14B). The remaining 10 conditions do not.\n\n\\section{DeepSeek-R1-Distill Analysis}\n\\label{app:deepseek}\n\nDeepSeek-R1-Distill-LLaMA-8B on D012 ($n$=60): SICA 70.0\\%, SC 71.7\\%, $\\Delta$=$-$1.7pp, C0=55.0\\%. Despite being distilled from a reasoning model, the 8B parameter count produces instruction-like diversity. The extraction rate (85.0\\%) is slightly lower than comparable instruction models, likely due to truncated thinking traces. The contradiction rate (4.0\\%) is within normal range. Classification as instruction-scale is supported by C0 behavior matching other 7--8B instruction models rather than the near-zero C0 of full reasoning models.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "88d59af3-db5a-47e6-a1ec-7990fec690f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "6972bdf2-3e82-47fd-bdb7-514fe47f0863",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated research paper",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Tool call

_source line 22 · 2026-05-17T17:20:03.306Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X2yYNWieG1WiS7xvbReMx7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6972bdf2-3e82-47fd-bdb7-514fe47f0863",
  "isSidechain": false,
  "requestId": "req_011Cb8XNPjaco1XMXYVMeGis",
  "type": "assistant",
  "uuid": "4fe45a5d-a6cc-499f-9089-68c011614a1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFHh7GggjkfLKU7cb5KXAR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12438,
      "cache_read_input_tokens": 42968,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12438,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 42968,
          "cache_creation_input_tokens": 12438,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12438
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

_source line 23 · 2026-05-17T17:20:05.033Z_

<details><summary>↩ Tool result · `toolu_01X2yYNWieG1WiS7xvbReMx7`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
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
on input line 35.


Package natbib Warning: Citation `pan2023logiclm' on page 1 undefined on input 
line 35.


Package natbib Warning: Citation `olausson2023linc' on page 1 undefined on inpu
t line 35.


Package natbib Warning: Citation `dylos2026' on page 1 undefined on input line 
35.


Package natbib Warning: Citation `aristotle2025' on page 1 undefined on input l
ine 35.


Package natbib Warning: Citation `fover2025' on page 1 undefined on input line 
35.


Overfull \hbox (20.71796pt too wide) in paragraph at lines 41--42
\T1/cmr/m/n/10.95 LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5
 do-mains (FO-LIO, ProofWriter,
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]

LaTeX Warning: Reference `tab:main' on page 3 undefined on input line 112.


Overfull \hbox (1.53621pt too wide) in paragraph at lines 138--139
\T1/cmr/m/n/10.95 (+6.7pp) and Strat-e-gyQA (+5.0pp for Qwen-14B). Third, high-
capacity mod-els and low-diversity
[3]

LaTeX Warning: Reference `tab:main' on page 4 undefined on input line 144.


LaTeX Warning: Reference `tab:precision' on page 4 undefined on input line 149.



LaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 179.


Overfull \hbox (12.84616pt too wide) in paragraph at lines 179--180
\T1/cmr/m/n/10.95 SAT, count-only (ig-nor-ing sat-is-fi-a-bil-ity struc-ture), 
and random-weight (shuf-fled con-straint weights). 
[4]

LaTeX Warning: Reference `tab:baselines' on page 5 undefined on input line 205.



LaTeX Warning: Reference `tab:c0' on page 5 undefined on input line 236.

[5]

LaTeX Warning: Reference `sec:meta' on page 6 undefined on input line 257.


LaTeX Warning: Reference `tab:kablation' on page 6 undefined on input line 262.



Overfull \hbox (0.18013pt too wide) in paragraph at lines 262--263
\T1/cmr/m/n/10.95 We vary $\OML/cmm/m/it/10.95 K \OMS/cmsy/m/n/10.95 2 f\OT1/cm
r/m/n/10.95 6\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 8\OML/cmm/m/it/10.95 ; \O
T1/cmr/m/n/10.95 11\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 12\OML/cmm/m/it/10.
95 ; \OT1/cmr/m/n/10.95 16\OML/cmm/m/it/10.95 ; \OT1/cmr/m/n/10.95 20\OMS/cmsy/
m/n/10.95 g$ \T1/cmr/m/n/10.95 on the Qwen-14B D012 $\OML/cmm/m/it/10.95 n$\T1/
cmr/m/n/10.95 =60 sub-set (Ta-ble []). The SICA$\OMS/cmsy/m/n/10.95 ^^@$\T1/cmr
/m/n/10.95 SC
[6]

LaTeX Warning: Reference `tab:meta' on page 7 undefined on input line 299.

[7]

Package natbib Warning: Citation `dylos2026' on page 8 undefined on input line 
358.


Package natbib Warning: Citation `aristotle2025' on page 8 undefined on input l
ine 358.


Package natbib Warning: Citation `fover2025' on page 8 undefined on input line 
358.


Package natbib Warning: Citation `wang2023selfconsistency' on page 8 undefined 
on input line 369.


Package natbib Warning: Citation `chen2023usc' on page 8 undefined on input lin
e 369.


Package natbib Warning: Citation `taubenfeld2025weighted' on page 8 undefined o
n input line 369.


Package natbib Warning: Citation `li2023diverse' on page 8 undefined on input l
ine 369.


Package natbib Warning: Citation `loo2025scaling' on page 8 undefined on input 
line 369.


Package natbib Warning: Citation `pan2023logiclm' on page 8 undefined on input 
line 372.


Package natbib Warning: Citation `olausson2023linc' on page 8 undefined on inpu
t line 372.


Package natbib Warning: Citation `dylos2026' on page 8 undefined on input line 
372.


Package natbib Warning: Citation `aristotle2025' on page 8 undefined on input l
ine 372.


Package natbib Warning: Citation `fover2025' on page 8 undefined on input line 
372.

[8]

Package natbib Warning: Citation `snell2025scaling' on page 9 undefined on inpu
t line 375.


Package natbib Warning: Citation `deepseek2025r1' on page 9 undefined on input 
line 375.


Package natbib Warning: Citation `cobbe2021gsm8k' on page 9 undefined on input 
line 378.


Package natbib Warning: Citation `lightman2023prm' on page 9 undefined on input
 line 378.


Package natbib Warning: Citation `wang2024mathshepherd' on page 9 undefined on 
input line 378.


Package natbib Warning: Citation `satbench2025' on page 9 undefined on input li
ne 381.


Package natbib Warning: Citation `llm_constraint2025' on page 9 undefined on in
put line 381.


Overfull \hbox (8.69542pt too wide) in paragraph at lines 390--391
[]\T1/cmr/m/n/10.95 Future work should in-ves-ti-gate whether tar-geted ex-trac
-tion train-ing or domain-specific prompt-
[9]

LaTeX Warning: Reference `tab:kablation' on page 10 undefined on input line 503
.


LaTeX Warning: `h' float specifier changed to `ht'.

[10]
Overfull \hbox (8.89241pt too wide) in paragraph at lines 532--533
\T1/cmr/m/n/10.95 DeepSeek-R1-Distill-LLaMA-8B on D012 ($\OML/cmm/m/it/10.95 n$
\T1/cmr/m/n/10.95 =60): SICA 70.0%, SC 71.7%, $\OT1/cmr/m/n/10.95 ^^A$\T1/cmr/m
/n/10.95 =$\OMS/cmsy/m/n/10.95 ^^@$\T1/cmr/m/n/10.95 1.7pp, C0=55.0%.

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy8.pfb>
Output written on paper.pdf (11 pages, 263948 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty
(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)
(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)
Overfull \hbox (20.71796pt too wide) in paragraph at lines 41--42
\T1/cmr/m/n/10.95 LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5
 do-mains (FO-LIO, ProofWriter,
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (1.53621pt too wide) in paragraph at lines 138--139
\T1/cmr/m/n/10.95 (+6.7pp) and Strat-e-gyQA (+5.0pp for Qwen-14B). Third, high-
capacity mod-els and low-diversity
[3] [4] [5] [6] [7] [8]
Overfull \hbox (8.69542pt too wide) in paragraph at lines 390--391
[]\T1/cmr/m/n/10.95 Future work should in-ves-ti-gate whether tar-geted ex-trac
-tion train-ing or domain-specific prompt-
[9] [10]
Overfull \hbox (8.89241pt too wide) in paragraph at lines 532--533
\T1/cmr/m/n/10.95 DeepSeek-R1-Distill-LLaMA-8B on D012 ($\OML/cmm/m/it/10.95 n$
\T1/cmr/m/n/10.95 =60): SICA 70.0%, SC 71.7%, $\OT1/cmr/m/n/10.95 ^^A$\T1/cmr/m
/n/10.95 =$\OMS/cmsy/m/n/10.95 ^^@$\T1/cmr/m/n/10.95 1.7pp, C0=55.0%.
[11] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.tex
live2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.t
exlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/
.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt
u/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu
ntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u
buntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy8.pfb>
Output written on paper.pdf (11 pages, 268791 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fe45a5d-a6cc-499f-9089-68c011614a1b",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "f83ec91a-d50d-493f-8448-f1e6f4270bef",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined \non input line 35.\n\n\nPackage natbib Warning: Citation `pan2023logiclm' on page 1 undefined on input \nline 35.\n\n\nPackage natbib Warning: Citation `olausson2023linc' on page 1 undefined on inpu\nt line 35.\n\n\nPackage natbib Warning: Citation `dylos2026' on page 1 undefined on input line \n35.\n\n\nPackage natbib Warning: Citation `aristotle2025' on page 1 undefined on input l\nine 35.\n\n\nPackage natbib Warning: Citation `fover2025' on page 1 undefined on input line \n35.\n\n\nOverfull \\hbox (20.71796pt too wide) in paragraph at lines 41--42\n\\T1/cmr/m/n/10.95 LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5\n do-mains (FO-LIO, ProofWriter,\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\n\nLaTeX Warning: Reference `tab:main' on page 3 undefined on input line 112.\n\n\nOverfull \\hbox (1.53621pt too wide) in paragraph at lines 138--139\n\\T1/cmr/m/n/10.95 (+6.7pp) and Strat-e-gyQA (+5.0pp for Qwen-14B). Third, high-\ncapacity mod-els and low-diversity\n[3]\n\nLaTeX Warning: Reference `tab:main' on page 4 undefined on input line 144.\n\n\nLaTeX Warning: Reference `tab:precision' on page 4 undefined on input line 149.\n\n\n\nLaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 179.\n\n\nOverfull \\hbox (12.84616pt too wide) in paragraph at lines 179--180\n\\T1/cmr/m/n/10.95 SAT, count-only (ig-nor-ing sat-is-fi-a-bil-ity struc-ture), \nand random-weight (shuf-fled con-straint weights). \n[4]\n\nLaTeX Warning: Reference `tab:baselines' on page 5 undefined on input line 205.\n\n\n\nLaTeX Warning: Reference `tab:c0' on page 5 undefined on input line 236.\n\n[5]\n\nLaTeX Warning: Reference `sec:meta' on page 6 undefined on input line 257.\n\n\nLaTeX Warning: Reference `tab:kablation' on page 6 undefined on input line 262.\n\n\n\nOverfull \\hbox (0.18013pt too wide) in paragraph at lines 262--263\n\\T1/cmr/m/n/10.95 We vary $\\OML/cmm/m/it/10.95 K \\OMS/cmsy/m/n/10.95 2 f\\OT1/cm\nr/m/n/10.95 6\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 8\\OML/cmm/m/it/10.95 ; \\O\nT1/cmr/m/n/10.95 11\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 12\\OML/cmm/m/it/10.\n95 ; \\OT1/cmr/m/n/10.95 16\\OML/cmm/m/it/10.95 ; \\OT1/cmr/m/n/10.95 20\\OMS/cmsy/\nm/n/10.95 g$ \\T1/cmr/m/n/10.95 on the Qwen-14B D012 $\\OML/cmm/m/it/10.95 n$\\T1/\ncmr/m/n/10.95 =60 sub-set (Ta-ble []). The SICA$\\OMS/cmsy/m/n/10.95 ^^@$\\T1/cmr\n/m/n/10.95 SC\n[6]\n\nLaTeX Warning: Reference `tab:meta' on page 7 undefined on input line 299.\n\n[7]\n\nPackage natbib Warning: Citation `dylos2026' on page 8 undefined on input line \n358.\n\n\nPackage natbib Warning: Citation `aristotle2025' on page 8 undefined on input l\nine 358.\n\n\nPackage natbib Warning: Citation `fover2025' on page 8 undefined on input line \n358.\n\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 8 undefined \non input line 369.\n\n\nPackage natbib Warning: Citation `chen2023usc' on page 8 undefined on input lin\ne 369.\n\n\nPackage natbib Warning: Citation `taubenfeld2025weighted' on page 8 undefined o\nn input line 369.\n\n\nPackage natbib Warning: Citation `li2023diverse' on page 8 undefined on input l\nine 369.\n\n\nPackage natbib Warning: Citation `loo2025scaling' on page 8 undefined on input \nline 369.\n\n\nPackage natbib Warning: Citation `pan2023logiclm' on page 8 undefined on input \nline 372.\n\n\nPackage natbib Warning: Citation `olausson2023linc' on page 8 undefined on inpu\nt line 372.\n\n\nPackage natbib Warning: Citation `dylos2026' on page 8 undefined on input line \n372.\n\n\nPackage natbib Warning: Citation `aristotle2025' on page 8 undefined on input l\nine 372.\n\n\nPackage natbib Warning: Citation `fover2025' on page 8 undefined on input line \n372.\n\n[8]\n\nPackage natbib Warning: Citation `snell2025scaling' on page 9 undefined on inpu\nt line 375.\n\n\nPackage natbib Warning: Citation `deepseek2025r1' on page 9 undefined on input \nline 375.\n\n\nPackage natbib Warning: Citation `cobbe2021gsm8k' on page 9 undefined on input \nline 378.\n\n\nPackage natbib Warning: Citation `lightman2023prm' on page 9 undefined on input\n line 378.\n\n\nPackage natbib Warning: Citation `wang2024mathshepherd' on page 9 undefined on \ninput line 378.\n\n\nPackage natbib Warning: Citation `satbench2025' on page 9 undefined on input li\nne 381.\n\n\nPackage natbib Warning: Citation `llm_constraint2025' on page 9 undefined on in\nput line 381.\n\n\nOverfull \\hbox (8.69542pt too wide) in paragraph at lines 390--391\n[]\\T1/cmr/m/n/10.95 Future work should in-ves-ti-gate whether tar-geted ex-trac\n-tion train-ing or domain-specific prompt-\n[9]\n\nLaTeX Warning: Reference `tab:kablation' on page 10 undefined on input line 503\n.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10]\nOverfull \\hbox (8.89241pt too wide) in paragraph at lines 532--533\n\\T1/cmr/m/n/10.95 DeepSeek-R1-Distill-LLaMA-8B on D012 ($\\OML/cmm/m/it/10.95 n$\n\\T1/cmr/m/n/10.95 =60): SICA 70.0%, SC 71.7%, $\\OT1/cmr/m/n/10.95 ^^A$\\T1/cmr/m\n/n/10.95 =$\\OMS/cmsy/m/n/10.95 ^^@$\\T1/cmr/m/n/10.95 1.7pp, C0=55.0%.\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy8.pfb>\nOutput written on paper.pdf (11 pages, 263948 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/tablefootnote/tablefootnote.sty\n(/usr/share/texlive/texmf-dist/tex/latex/letltxmacro/letltxmacro.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xifthen/xifthen.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/calc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/ifmtarg/ifmtarg.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (20.71796pt too wide) in paragraph at lines 41--42\n\\T1/cmr/m/n/10.95 LLaMA-3.1-8B, DeepSeek-R1-Distill-LLaMA-8B, QwQ-32B) across 5\n do-mains (FO-LIO, ProofWriter,\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (1.53621pt too wide) in paragraph at lines 138--139\n\\T1/cmr/m/n/10.95 (+6.7pp) and Strat-e-gyQA (+5.0pp for Qwen-14B). Third, high-\ncapacity mod-els and low-diversity\n[3] [4] [5] [6] [7] [8]\nOverfull \\hbox (8.69542pt too wide) in paragraph at lines 390--391\n[]\\T1/cmr/m/n/10.95 Future work should in-ves-ti-gate whether tar-geted ex-trac\n-tion train-ing or domain-specific prompt-\n[9] [10]\nOverfull \\hbox (8.89241pt too wide) in paragraph at lines 532--533\n\\T1/cmr/m/n/10.95 DeepSeek-R1-Distill-LLaMA-8B on D012 ($\\OML/cmm/m/it/10.95 n$\n\\T1/cmr/m/n/10.95 =60): SICA 70.0%, SC 71.7%, $\\OT1/cmr/m/n/10.95 ^^A$\\T1/cmr/m\n/n/10.95 =$\\OMS/cmsy/m/n/10.95 ^^@$\\T1/cmr/m/n/10.95 1.7pp, C0=55.0%.\n[11] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/\ntexmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy8.pfb>\nOutput written on paper.pdf (11 pages, 268791 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4fe45a5d-a6cc-499f-9089-68c011614a1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "f83ec91a-d50d-493f-8448-f1e6f4270bef",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated research paper",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Assistant

_source line 26 · 2026-05-17T17:20:09.093Z_

<details><summary>Logged reasoning block</summary>

```text
There's a "Label(s) may have changed" warning on the second pass, meaning I need a third pass. Let me run one more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83ec91a-d50d-493f-8448-f1e6f4270bef",
  "isSidechain": false,
  "requestId": "req_011Cb8XNq8o6zkdiP6gxJRqm",
  "type": "assistant",
  "uuid": "7156660a-1625-4058-ac8e-f0d85c227936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ewLgfGJ54PTHkgGjiSVtu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8708,
      "cache_read_input_tokens": 55406,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 55406,
          "cache_creation_input_tokens": 8708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8708
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

_source line 27 · 2026-05-17T17:20:09.566Z_

One more pass needed to resolve cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7156660a-1625-4058-ac8e-f0d85c227936",
  "isSidechain": false,
  "requestId": "req_011Cb8XNq8o6zkdiP6gxJRqm",
  "type": "assistant",
  "uuid": "f0000de4-d6be-443b-8bf4-1cb709fdb8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ewLgfGJ54PTHkgGjiSVtu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8708,
      "cache_read_input_tokens": 55406,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 55406,
          "cache_creation_input_tokens": 8708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8708
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

_source line 28 · 2026-05-17T17:20:12.099Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UyG5CA457xaYQBr436WWaF`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass to resolve labels",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0000de4-d6be-443b-8bf4-1cb709fdb8e2",
  "isSidechain": false,
  "requestId": "req_011Cb8XNq8o6zkdiP6gxJRqm",
  "type": "assistant",
  "uuid": "e5f8f8f2-1d86-4d69-84b8-356bd7f4c7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ewLgfGJ54PTHkgGjiSVtu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8708,
      "cache_read_input_tokens": 55406,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8708,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 55406,
          "cache_creation_input_tokens": 8708,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8708
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

_source line 29 · 2026-05-17T17:20:12.773Z_

<details><summary>↩ Tool result · `toolu_01UyG5CA457xaYQBr436WWaF`</summary>

```text
amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
msy8.pfb>
Output written on paper.pdf (11 pages, 268791 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5f8f8f2-1d86-4d69-84b8-356bd7f4c7a2",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "2f8dcdd2-035e-41b5-b317-a74734b0e814",
  "toolUseResult": {
    "stdout": "amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmsy8.pfb>\nOutput written on paper.pdf (11 pages, 268791 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "e5f8f8f2-1d86-4d69-84b8-356bd7f4c7a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T17:20:17.784Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QW1BhHk8okccefZnsXvw8N`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.pdf",
  "description": "Verify PDF output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f8dcdd2-035e-41b5-b317-a74734b0e814",
  "isSidechain": false,
  "requestId": "req_011Cb8XPQ9QoPzRG673sTCJW",
  "type": "assistant",
  "uuid": "4b6157fd-2cd6-4fa7-b40a-1a3b31bd43c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVYagqqyad9e7Wv2yfmn4K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 64114,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 64114,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
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

_source line 31 · 2026-05-17T17:20:17.870Z_

<details><summary>↩ Tool result · `toolu_01QW1BhHk8okccefZnsXvw8N`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 263K May 17 17:20 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b6157fd-2cd6-4fa7-b40a-1a3b31bd43c1",
  "isSidechain": false,
  "promptId": "f97abd09-34b6-4aa8-9228-2d2473df52d0",
  "type": "user",
  "uuid": "5d4bacd2-8680-400b-b6b3-342bd084f9f0",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 263K May 17 17:20 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst/paper.pdf",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4b6157fd-2cd6-4fa7-b40a-1a3b31bd43c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-17T17:20:17.889Z_

```json
{
  "parentUuid": "5d4bacd2-8680-400b-b6b3-342bd084f9f0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "55ff14b8-ed59-43f5-8100-802937025944",
  "timestamp": "2026-05-17T17:20:17.889Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-17T17:20:28.537Z_

论文已生成：11 页，263K PDF。

覆盖了 experiment_data.json 中全部 18 个实验的数据，包括：
- **Table 1**: 11 个 model×domain 条件的主结果
- **Table 2**: Constraint precision 双峰分布（307 个 multi-candidate 问题）
- **Table 3**: 聚合消融（MAX-SAT vs count-only vs random-weight，含 high-precision 子集）
- **Table 4**: 基线对比（weighted SC + Logic-LM）
- **Table 5**: C0 诊断统计
- **Table 6**: K 敏感性消融
- **Table 7**: Meta-analytic 汇总（14 条件，N=1482，Δ=+1.8pp，I²=0.62）
- **Appendix**: overhead 分解、DeepSeek-R1-Distill 分析

叙事按 narrative guidance 重构为 condition-dependent phenomenon：正向边界条件 + oracle 机制验证 + C0-precision 联合诊断框架。所有数字来自 experiment_data.json，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ff14b8-ed59-43f5-8100-802937025944",
  "isSidechain": false,
  "requestId": "req_011Cb8XPn5XSVakxHeEUx6zF",
  "type": "assistant",
  "uuid": "62843ee4-0e1e-47da-ae5e-80276576db3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T165032/worst",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L75jhHH6vn6vAYUg2yHdBk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 64411,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 64411,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T165032 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_co…",
  "leafUuid": "62843ee4-0e1e-47da-ae5e-80276576db3f",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier simulated research paper",
  "sessionId": "30fff989-e5a5-458f-9db4-12c70eff9bfe"
}
```

---
