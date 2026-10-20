# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/c4b48419-90ca-4468-8335-af2b24dda8d3.jsonl`
- **Structured JSON:** [`163a9b6271ec959586ea.json`](../../sessions/16/163a9b6271ec959586ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T13:00:11.031Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T13:00:11.031Z",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Claim 1 reframed from 'accuracy improvement' to 'principled interpretable tiebreaking with positive trend on formal-logic domains.' Claim 2 becomes lead — C0 operating regime characterization is primary contribution, validated directionally across 3 families even though per-family SICA-SC deltas are noisy. Claim 3 downgraded from 'continuous predictor' to 'binary diagnostic' (C0>20% = try SICA, C0<5% = skip). MaxSAT framed as 'interpretability + marginal gains.' Title: 'When Does Symbolic Consensus Help?' Target: EMNLP Findings (55-65%).\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T13:00:11.035Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T13:00:11.035Z",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-16T13:00:11.059Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Claim 1 reframed from 'accuracy improvement' to 'principled interpretable tiebreaking with positive trend on formal-logic domains.' Claim 2 becomes lead — C0 operating regime characterization is primary contribution, validated directionally across 3 families even though per-family SICA-SC deltas are noisy. Claim 3 downgraded from 'continuous predictor' to 'binary diagnostic' (C0>20% = try SICA, C0<5% = skip). MaxSAT framed as 'interpretability + marginal gains.' Title: 'When Does Symbolic Consensus Help?' Target: EMNLP Findings (55-65%).
- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "25ae9856-02b4-489f-8378-91d763d4d1c1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T13:00:11.058Z_

```json
{
  "parentUuid": "25ae9856-02b4-489f-8378-91d763d4d1c1",
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
  "uuid": "10b81ce1-be3a-4309-899e-7cf285e02944",
  "timestamp": "2026-05-16T13:00:11.058Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T13:00:11.058Z_

```json
{
  "parentUuid": "10b81ce1-be3a-4309-899e-7cf285e02944",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "228685fd-b13c-4f48-b1b6-2357f54375f9",
  "timestamp": "2026-05-16T13:00:11.058Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
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
  "aiTitle": "Generate EMNLP paper on symbolic consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Assistant

_source line 7 · 2026-05-16T13:00:14.155Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228685fd-b13c-4f48-b1b6-2357f54375f9",
  "isSidechain": false,
  "requestId": "req_011Cb6HkR8PqFNM5vwSJvU1r",
  "type": "assistant",
  "uuid": "0a1f67e3-e32a-4f56-b314-064961402be2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjPvETqMFFBT5PXyduj5BS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11212,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11212
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

_source line 8 · 2026-05-16T13:00:14.649Z_

<details open><summary>🔧 Tool call — Read · `toolu_018xVnCUvKGKbp1CQRddLHD3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a1f67e3-e32a-4f56-b314-064961402be2",
  "isSidechain": false,
  "requestId": "req_011Cb6HkR8PqFNM5vwSJvU1r",
  "type": "assistant",
  "uuid": "5af4867f-8668-419d-9084-0244628d63e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjPvETqMFFBT5PXyduj5BS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11212,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11212
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

_source line 9 · 2026-05-16T13:00:14.963Z_

<details><summary>↩ Tool result · `toolu_018xVnCUvKGKbp1CQRddLHD3`</summary>

```text
1	[
2	  {
3	    "name": "sica_expanded_14b",
4	    "description": "PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7, Qwen2.5-14B-Instruct",
5	    "results": {
6	      "n_total": 804,
7	      "n_folio": 204,
8	      "n_proofwriter": 600,
9	      "sica_accuracy_combined": 0.718,
10	      "sc_accuracy_combined": 0.703,
11	      "sica_sc_gap_combined_pp": 1.5,
12	      "bootstrap_p_combined": 0.19,
13	      "sica_accuracy_folio": 0.784,
14	      "sc_accuracy_folio": 0.745,
15	      "sica_sc_gap_folio_pp": 3.9,
16	      "bootstrap_p_folio": 0.08,
17	      "sica_accuracy_proofwriter": 0.695,
18	      "sc_accuracy_proofwriter": 0.689,
19	      "sica_sc_gap_proofwriter_pp": 0.6,
20	      "bootstrap_p_proofwriter": 0.38,
21	      "c0_multi_candidate_rate": 0.42,
22	      "c0_folio": 0.52,
23	      "c0_proofwriter": 0.38,
24	      "tiebreak_cases": 68,
25	      "tiebreak_sica_wins": 44,
26	      "tiebreak_win_rate": 0.647,
27	      "maxsat_exclusion_rate": 0.031,
28	      "total_constraints_unique": 23800,
29	      "wall_time_hours": 13.2
30	    },
31	    "tables": [
32	      "T1: Main Results (14B row: FOLIO 78.4 vs 74.5, PW 69.5 vs 68.9, Combined 71.8 vs 70.3)",
33	      "T2: Tiebreak Analysis (68 ties, SICA wins 44, SC wins 24, win rate 64.7%)"
34	    ],
35	    "figures": [],
36	    "analysis": "FOLIO is strongest evidence for Claim 1 but p=0.08 requires careful framing — 'trending toward significance' or report one-tailed. Combined result is not significant; paper must not overclaim. ProofWriter contributes to C0 validation (even at C0=0.38, gains are minimal on closed-world tasks) which actually supports the narrative that task formality matters. Key insight for paper: SICA's value concentrates in tie-heavy formal-logic domains, not uniformly across all logic tasks.\n\nAt scale, FOLIO retains a real but attenuated gap (~3.9pp vs pilot's 6.7pp) because the pilot's 30 questions were disproportionately tie-heavy; the full 204 includes easier items where SC already converges (C0 drops on easy items). Bootstrap p lands at 0.08 — suggestive but not clean at α=0.05. ProofWriter's closed-world reasoning produces less diverse traces than FOLIO's open-world NLI; most PW gains come from depth-5 items where traces occasionally diverge, but the majority of PW questions show near-unanimous SC votes, yielding a negligible 0.6pp gap (p=0.38). Combined significance is diluted by PW's 600-question mass pulling the average toward zero. The C0 rate of 0.42 confirms the operating regime (>20%) but the per-question C0 variance means many individual questions contribute zero signal. Tiebreak win rate of 64.7% is above random (50%) but below the pilot's 80% (small-sample inflation in pilot)."
37	  },
38	  {
39	    "name": "sica_k_ablation_14b",
40	    "description": "K sensitivity (K=6,8,12,16,20) on D012's 60 questions, Qwen2.5-14B-Instruct",
41	    "results": {
42	      "k6_sica_accuracy": 0.717,
43	      "k6_sc_accuracy": 0.7,
44	      "k6_gap_pp": 1.7,
45	      "k6_c0": 0.4,
46	      "k6_tie_rate": 0.15,
47	      "k8_sica_accuracy": 0.733,
48	      "k8_sc_accuracy": 0.7,
49	      "k8_gap_pp": 3.3,
50	      "k8_c0": 0.47,
51	      "k8_tie_rate": 0.22,
52	      "k12_sica_accuracy": 0.733,
53	      "k12_sc_accuracy": 0.7,
54	      "k12_gap_pp": 3.3,
55	      "k12_c0": 0.53,
56	      "k12_tie_rate": 0.25,
57	      "k16_sica_accuracy": 0.75,
58	      "k16_sc_accuracy": 0.717,
59	      "k16_gap_pp": 3.3,
60	      "k16_c0": 0.57,
61	      "k16_tie_rate": 0.18,
62	      "k20_sica_accuracy": 0.75,
63	      "k20_sc_accuracy": 0.733,
64	      "k20_gap_pp": 1.7,
65	      "k20_c0": 0.6,
66	      "k20_tie_rate": 0.13,
67	      "wall_time_hours": 4.5
68	    },
69	    "tables": [
70	      "T3: K Sensitivity (K vs gap, C0, tie_rate — shows inverted-U peak at K=8-12)"
71	    ],
72	    "figures": [],
73	    "analysis": "The inverted-U supports the 'principled tiebreaker' narrative: SICA's value is mechanistically tied to tie frequency, not a general accuracy boost. Paper should emphasize K=8-12 as practical recommendation. The fact that gap doesn't grow unboundedly with K is actually a feature for the 'operating regime' story — it shows SICA's contribution is bounded and predictable.\n\nC0 increases monotonically with K (more samples → more chance of diverse answers), but SICA-SC gap does not scale linearly. At K=6, too few traces means ties are rare (15%) and SC often has a clear majority — SICA has few opportunities to intervene. K=8 and K=12 hit the sweet spot: even K values create more exact ties, giving SICA maximum leverage. At K=16/20, C0 rises further but the majority winner becomes more stable (law of large numbers); ties actually decrease because the leading answer accumulates enough margin. The gap at K=20 shrinks because SC's majority is robust enough that tiebreaking matters less. This produces an inverted-U pattern peaking around K=8-12. Critically, odd K values (not tested here but inferrable) would show fewer ties, further supporting that SICA's primary mechanism is tiebreaking rather than general accuracy improvement."
74	  },
75	  {
76	    "name": "tiebreak_baseline_analysis",
77	    "description": "SICA vs SC-random vs SC-deterministic on all available data. CPU reanalysis.",
78	    "results": {
79	      "n_tiebreak_cases_d012": 5,
80	      "sica_tiebreak_accuracy": 0.8,
81	      "random_tiebreak_accuracy_mean": 0.5,
82	      "alphabetical_tiebreak_accuracy": 0.6,
83	      "first_seen_tiebreak_accuracy": 0.4,
84	      "n_tiebreak_cases_expanded": 68,
85	      "sica_tiebreak_accuracy_expanded": 0.647,
86	      "random_tiebreak_accuracy_expanded_mean": 0.485,
87	      "sica_vs_random_p_expanded": 0.035,
88	      "overall_sica_accuracy_with_random_baseline": 0.71,
89	      "sica_minus_random_baseline_gap_pp": 0.8
90	    },
91	    "tables": [
92	      "T2 extended: Tiebreak comparison table (SICA 64.7%, Random 48.5%, Alphabetical 52.9%, First-seen 45.6%)"
93	    ],
94	    "figures": [],
95	    "analysis": "This is both the strongest and most modest result: SICA is a statistically significant better tiebreaker (p=0.035 on ties), but overall accuracy gain over a fair random baseline is small (~0.8pp). Paper must be honest about this decomposition. Reframe: 'SICA provides principled, interpretable tiebreaking with significant per-tie advantage, contributing a modest but consistent overall accuracy improvement.' The interpretability angle (you can inspect WHY SICA chose an answer via constraints) becomes the differentiator over random.\n\nOn the original D012 5 ties, SICA's 80% (4/5) is consistent with pilot data. On expanded 68 ties, SICA's advantage regresses toward a more realistic 64.7% — still meaningfully above random's ~48.5% (random doesn't hit exactly 50% due to answer distribution asymmetry in the dataset). The critical comparison is: if SC uses random tiebreaking instead of alphabetical, it already captures some of the 'gap' attributed to SICA. The overall SICA-vs-SC-random gap shrinks to ~0.8pp (from 1.5pp vs deterministic), because random tiebreak is correct ~50% of the time on ties vs SICA's ~65%. This means roughly half of SICA's overall accuracy advantage comes from better tiebreaking specifically, and the other half from ties where SICA's constraint-weighted answer happens to differ from SC's majority (non-tie cases where MaxSAT exclusion changes the winner). The p=0.035 on tie-only comparison is the paper's cleanest statistical result."
96	  },
97	  {
98	    "name": "sica_7b_scaling",
99	    "description": "Qwen2.5-7B-Instruct on D012 60 questions, K=12, T=0.7",
100	    "results": {
101	      "sica_accuracy": 0.65,
102	      "sc_accuracy": 0.617,
103	      "sica_sc_gap_pp": 3.3,
104	      "c0_multi_candidate_rate": 0.55,
105	      "bootstrap_p": 0.18,
106	      "folio_sica": 0.7,
107	      "folio_sc": 0.633,
108	      "folio_gap_pp": 6.7,
109	      "proofwriter_sica": 0.619,
110	      "proofwriter_sc": 0.607,
111	      "proofwriter_gap_pp": 1.2,
112	      "tiebreak_cases": 11,
113	      "tiebreak_win_rate": 0.636,
114	      "constraint_extraction_rate": 0.92,
115	      "wall_time_hours": 1.8
116	    },
117	    "tables": [
118	      "T1: 7B row (FOLIO 70.0 vs 63.3, PW 61.9 vs 60.7, Combined 65.0 vs 61.7)"
119	    ],
120	    "figures": [],
121	    "analysis": "7B confirms 'weaker model → higher C0 → SICA helps more' directionally. But the C0 jump (0.53→0.55) is smaller than hoped — median tier says the scaling trend is noisy. The 7B point helps the F2 scatter plot but doesn't create a clean linear relationship. For the paper: include in T1 and F2, note that within-family scaling shows the expected direction but the gradient is shallow for adjacent sizes.\n\n7B is weaker than 14B (SC baseline drops from 70% to ~62%), producing more diverse outputs (C0 rises from 0.53 to 0.55). The C0 increase is real but modest — the 7B model is weaker but not dramatically so on these tasks; it still often converges on common answers. The SICA gap of 3.3pp matches the median expectation — higher C0 creates more intervention opportunities, but 7B's constraint extraction quality is lower (92% vs 100% for 14B), partially offsetting the diversity advantage. FOLIO shows the clearest gain (+6.7pp) because open-world NLI with a 3-class answer space maximizes tie probability for a confused model. However, bootstrap p=0.18 on 60 questions means none of this is individually significant — only the cross-model pattern matters. The key data point is: C0(7B)=0.55 > C0(14B)=0.53, confirming the directional scaling trend even if the magnitude is modest."
122	  },
123	  {
124	    "name": "qwq_32b_operating_regime",
125	    "description": "Format existing QwQ-32B data for Operating Regime Analysis section",
126	    "results": {
127	      "c0_combined": 0.036,
128	      "c0_aime": 0.0,
129	      "c0_proofwriter": 0.1875,
130	      "c0_folio": 0.0,
131	      "sica_sc_gap_pp": 0.0,
132	      "n_problems_total": 48,
133	      "n_aime": 22,
134	      "n_proofwriter": 16,
135	      "n_folio": 10,
136	      "reasoning_model_conclusion": "C0<5% → SICA≡SC structurally"
137	    },
138	    "tables": [
139	      "T1: QwQ-32B row (all gaps = 0.0pp, C0 = 3.6%)"
140	    ],
141	    "figures": [],
142	    "analysis": "This is Claim 2's strongest evidence in the paper. The contrast between 14B-Instruct (C0=53%, gap=+3.3pp) and QwQ-32B (C0=3.6%, gap=0pp) on the SAME tasks demonstrates that C0 is the governing variable, not task difficulty. Present as: 'reasoning models self-consistent → SICA redundant; instruction models diverse → SICA helps.' This frames the negative result as a positive insight about operating regimes.\n\nQwQ-32B's reasoning chains are so self-consistent that sampling temperature has negligible effect on final answers. The model's extended chain-of-thought process (often 2000+ tokens) acts as an internal consistency mechanism — by the time it reaches an answer, it has self-corrected any stochastic variation. C0=3.6% means only ~2 out of 48 problems produced any answer diversity at all, and even those had overwhelming majorities. SICA is structurally identical to SC because there are no ties to break and no minority answers for MaxSAT to potentially elevate. This is the 'degenerate regime' — the method's mechanism (resolving disagreement) has no disagreement to resolve. The key insight is that this is model-class-dependent (reasoning vs instruction), not task-dependent (same FOLIO/PW tasks show high C0 on 14B instruction model)."
143	  },
144	  {
145	    "name": "c0_diagnostic_validation",
146	    "description": "C0 vs SICA-SC gap scatter plot across all models and K values. CPU analysis.",
147	    "results": {
148	      "n_data_points": 14,
149	      "pearson_r": 0.58,
150	      "spearman_rho": 0.64,
151	      "c0_threshold_20_precision": 0.75,
152	      "c0_threshold_20_recall": 1.0,
153	      "c0_below_5_all_zero_gap": true,
154	      "c0_above_20_positive_gap_rate": 0.75,
155	      "binary_classification_accuracy": 0.857,
156	      "auc_roc": 0.82
157	    },
158	    "tables": [
159	      "Appendix table: All (model, dataset, K, C0, gap) data points"
160	    ],
161	    "figures": [],
162	    "analysis": "The binary diagnostic (C0>20% → try SICA, C0<5% → skip) is the paper's Claim 3 contribution. In median tier, it works as a diagnostic but NOT as a continuous predictor — the scatter has too much variance for a regression line to be useful. Paper should present the binary threshold clearly and acknowledge that within the 'SICA regime' (C0>20%), the magnitude of gain is task-dependent and not precisely predicted by C0 alone. This downgrades Claim 3 from 'continuous predictor' to 'binary diagnostic' as specified in the tier definition.\n\nWith ~14 data points (7B, 14B, 72B on 60q; 14B on 804q; QwQ on 48q; Mistral on 60q; LLaMA on 60q; DeepSeek-R1 on 60q; plus K-ablation variants), the correlation is positive but noisy (r=0.58). The noise comes from: (1) Mistral and LLaMA having high C0 but inconsistent gaps (one shows gain, one flat — median tier assumption), (2) K-ablation points clustering in a narrow C0 range, (3) PW subset having moderate C0 but near-zero gap (task formality confound). However, the BINARY diagnostic works well: C0<5% always means gap≈0 (reasoning models), and C0>20% means gap>0 in 75% of cases. The 25% failure rate (C0>20% but gap≈0) corresponds to cases where high diversity exists but constraint extraction quality is poor or the task doesn't benefit from symbolic reasoning (e.g., one cross-family model). Spearman (rank correlation) beats Pearson because the relationship is monotone but non-linear — there's a threshold effect rather than a smooth gradient."
163	  },
164	  {
165	    "name": "sica_72b_awq",
166	    "description": "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions, K=12, T=0.7",
167	    "results": {
168	      "sica_accuracy": 0.783,
169	      "sc_accuracy": 0.767,
170	      "sica_sc_gap_pp": 1.6,
171	      "c0_multi_candidate_rate": 0.37,
172	      "bootstrap_p": 0.35,
173	      "folio_sica": 0.867,
174	      "folio_sc": 0.833,
175	      "folio_gap_pp": 3.4,
176	      "proofwriter_sica": 0.738,
177	      "proofwriter_sc": 0.738,
178	      "proofwriter_gap_pp": 0.0,
179	      "tiebreak_cases": 4,
180	      "tiebreak_win_rate": 0.75,
181	      "constraint_extraction_rate": 1.0,
182	      "wall_time_hours": 3.8
183	    },
184	    "tables": [
185	      "T1: 72B row (FOLIO 86.7 vs 83.3, PW 73.8 vs 73.8, Combined 78.3 vs 76.7)"
186	    ],
187	    "figures": [],
188	    "analysis": "72B data creates the within-Qwen scaling dimension for the paper: 7B→14B→72B shows C0 decreasing and gap decreasing. But the pattern is noisy (7B and 14B are close, then 72B drops more). This is enough for a 'directional trend' claim but not a clean power law. Present as evidence that stronger instruction models approach but don't reach the reasoning model's degenerate regime. The 72B-AWQ quantization is a potential confound to acknowledge in limitations (4-bit may slightly increase randomness vs full precision).\n\n72B is stronger than 14B (SC baseline 76.7% vs 70%), so it converges more often — but NOT dramatically more. C0=0.37 is below 14B's 0.53 but still well above the 20% threshold. In median tier, '72B not clearly below 14B' means the C0 drop is real but modest (0.53→0.37, not 0.53→0.15). This happens because 72B is still an instruction model — it doesn't have the reasoning model's self-consistency mechanism, just better initial accuracy. It still produces diverse outputs on genuinely ambiguous items. The SICA gap is small (1.6pp) because: (1) fewer ties with 72B's stronger majorities, (2) on PW, 72B is so accurate that there's no room for improvement. FOLIO still shows a gap (+3.4pp) because even 72B finds open-world NLI challenging enough to produce diverse traces. The scaling story becomes: 7B (C0=0.55) > 14B (C0=0.53) > 72B (C0=0.37) — directionally correct but the 7B-14B gap is tiny while the 14B-72B gap is larger. This is 'noisy' because you'd expect a more uniform gradient."
189	  },
190	  {
191	    "name": "constraint_quality_case_studies",
192	    "description": "Qualitative analysis of constraints on 5-10 representative questions from exp-001",
193	    "results": {
194	      "n_cases_analyzed": 8,
195	      "semantically_meaningful_rate": 0.75,
196	      "excluded_constraints_error_rate": 0.83,
197	      "constraint_types": [
198	        "entailment_chain",
199	        "negation",
200	        "universal_quantifier",
201	        "conditional",
202	        "disjunction"
203	      ],
204	      "avg_constraints_per_trace": 4.2,
205	      "avg_unique_constraints_per_problem": 14.8,
206	      "failure_modes": [
207	        "over-literal parsing",
208	        "scope ambiguity in quantifiers",
209	        "implicit premises missed"
210	      ]
211	    },
212	    "tables": [],
213	    "figures": [],
214	    "analysis": "Case studies serve the interpretability narrative. Even if accuracy gains are modest, showing that MaxSAT exclusion corresponds to actual reasoning errors (83% of the time) validates the mechanism as principled rather than lucky. This supports reframing from 'accuracy tool' to 'interpretable reasoning aggregation.' Include 2-3 cherry-picked examples in main paper §4, full set in appendix.\n\nConstraint extraction from 14B traces is generally meaningful because FOLIO premises are already semi-formal (natural language with clear logical structure). ~75% of extracted constraints correctly capture the intended logical relationship. The 25% failures come from: (1) overly literal parsing of hedging language ('might', 'usually'), (2) quantifier scope ambiguity in nested sentences, (3) implicit common-sense premises that the model encodes but the extractor can't formalize. Excluded constraints (those MaxSAT deems unsatisfiable with the rest) correspond to reasoning errors ~83% of the time — this validates the MaxSAT mechanism as genuinely detecting flawed reasoning rather than randomly dropping constraints. The remaining 17% of exclusions are valid constraints that happen to conflict with the majority due to alternative valid interpretations."
215	  },
216	  {
217	    "name": "overhead_analysis",
218	    "description": "Wall-time breakdown per question from exp-001 logs",
219	    "results": {
220	      "avg_total_time_per_question_s": 59.1,
221	      "avg_generation_time_s": 48.3,
222	      "avg_extraction_time_s": 8.4,
223	      "avg_maxsat_time_s": 2.4,
224	      "generation_fraction": 0.817,
225	      "extraction_fraction": 0.142,
226	      "maxsat_fraction": 0.041,
227	      "overhead_vs_sc_percent": 22.4,
228	      "sc_only_time_per_question_s": 48.3,
229	      "batch_throughput_questions_per_hour": 61
230	    },
231	    "tables": [
232	      "T4: Overhead breakdown (Generation 48.3s/81.7%, Extraction 8.4s/14.2%, MaxSAT 2.4s/4.1%, Total overhead +22.4%)"
233	    ],
234	    "figures": [],
235	    "analysis": "22% overhead is defensible for EMNLP — it's not 10x. Frame as: 'SICA adds modest overhead concentrated in constraint extraction (parallelizable), while MaxSAT solving is negligible. The primary cost is generation (shared with SC). Practical deployment with a dedicated extraction model could reduce overhead to <10%.' Reviewer concern addressed: the overhead IS worth it if you're in the C0>20% regime and want interpretable tiebreaking.\n\nGeneration dominates (82%) because K=12 traces each require a full forward pass through the 14B model. Constraint extraction adds ~8.4s per question (LLM-based extraction of FOL from 12 traces, batched). MaxSAT solving is negligible (~2.4s, Z3 on small instances). Total overhead vs pure SC is ~22% — SC would take 48.3s (just generation), SICA adds 10.8s for extraction+solving. This is modest for a research prototype but worth noting. The extraction step could be parallelized (currently sequential over traces) or replaced with a smaller model, suggesting practical deployment could reduce overhead to <10%. Generation time dominates because vLLM batches efficiently but 12 traces × 14B parameters × ~500 output tokens each is substantial."
236	  },
237	  {
238	    "name": "sica_mistral_7b",
239	    "description": "Mistral-7B-Instruct-v0.3 on D012 60 questions, K=12, T=0.7",
240	    "results": {
241	      "sica_accuracy": 0.583,
242	      "sc_accuracy": 0.567,
243	      "sica_sc_gap_pp": 1.6,
244	      "c0_multi_candidate_rate": 0.35,
245	      "bootstrap_p": 0.38,
246	      "folio_sica": 0.6,
247	      "folio_sc": 0.567,
248	      "folio_gap_pp": 3.3,
249	      "proofwriter_sica": 0.571,
250	      "proofwriter_sc": 0.571,
251	      "proofwriter_gap_pp": 0.0,
252	      "tiebreak_cases": 6,
253	      "tiebreak_win_rate": 0.667,
254	      "constraint_extraction_rate": 0.85,
255	      "wall_time_hours": 1.3
256	    },
257	    "tables": [
258	      "T1: Mistral-7B row (FOLIO 60.0 vs 56.7, PW 57.1 vs 57.1, Combined 58.3 vs 56.7)"
259	    ],
260	    "figures": [],
261	    "analysis": "Mistral confirms C0>20% across families (critical) but shows that C0 is necessary-not-sufficient for SICA gains. The paper should acknowledge: 'Cross-family C0 pattern holds, but per-family SICA-SC delta varies with constraint extraction quality.' This is honest and actually strengthens the analysis paper framing — it identifies a second prerequisite beyond C0 (extraction quality). For the escalation decision: gap>0 but p>0.2 on 60 questions — per the plan note, could expand to 200+ questions, but median tier assumes we don't (GPU budget constraint or decision that the 60-question C0 confirmation is sufficient).\n\nMistral-7B is the 'one flat' family in the median tier's 'one shows gain, one flat' cross-family pattern. C0=0.35 confirms C0>20% holds outside Qwen (critical for Claim 2), but the SICA-SC gap is small and noisy (+1.6pp, p=0.38). This happens because Mistral's constraint extraction quality is lower (85% vs Qwen's 100%) — the model produces less structured reasoning traces, leading to more extraction failures and lower-quality constraints. When MaxSAT operates on noisy constraints, its tiebreaking advantage is partially offset by occasional wrong exclusions. FOLIO still shows a positive direction (+3.3pp) but PW is flat. The key takeaway is: C0 pattern generalizes (Mistral instruction model produces diverse outputs), but SICA's benefit depends on BOTH diversity AND extraction quality. Mistral's shorter, less structured traces hurt extraction."
262	  },
263	  {
264	    "name": "sica_llama_8b",
265	    "description": "LLaMA-3.1-8B-Instruct on D012 60 questions, K=12, T=0.7",
266	    "results": {
267	      "sica_accuracy": 0.617,
268	      "sc_accuracy": 0.583,
269	      "sica_sc_gap_pp": 3.4,
270	      "c0_multi_candidate_rate": 0.4,
271	      "bootstrap_p": 0.14,
272	      "folio_sica": 0.667,
273	      "folio_sc": 0.6,
274	      "folio_gap_pp": 6.7,
275	      "proofwriter_sica": 0.583,
276	      "proofwriter_sc": 0.571,
277	      "proofwriter_gap_pp": 1.2,
278	      "tiebreak_cases": 9,
279	      "tiebreak_win_rate": 0.667,
280	      "constraint_extraction_rate": 0.93,
281	      "wall_time_hours": 1.4
282	    },
283	    "tables": [
284	      "T1: LLaMA-8B row (FOLIO 66.7 vs 60.0, PW 58.3 vs 57.1, Combined 61.7 vs 58.3)"
285	    ],
286	    "figures": [],
287	    "analysis": "LLaMA provides the second positive cross-family confirmation. The 3-family narrative becomes: 'All three instruction-model families show C0>20% (operating regime confirmed), with two of three showing positive SICA-SC gaps and the third showing directional but flat improvement.' This is sufficient for EMNLP Findings — not every family needs significant gains if the C0 pattern is the primary claim. Paper frames Mistral's flat result as 'extraction quality moderates effectiveness' rather than as a failure.\n\nLLaMA-8B is the 'one shows gain' family in the median tier's cross-family pattern. C0=0.40 confirms diversity, and the gap (+3.4pp) is comparable to Qwen-14B's pilot result. LLaMA's instruction tuning produces reasonably structured outputs (extraction rate 93%), and at 8B parameters it's weak enough on FOLIO to produce genuine disagreement. The FOLIO gap of +6.7pp looks impressive but with only 30 FOLIO questions it's not significant (p=0.14 for combined). The key difference vs Mistral: LLaMA's traces are more structured (Meta's instruction tuning format includes clearer step markers), enabling better constraint extraction. This makes LLaMA the second 'positive signal' family alongside Qwen, while Mistral is the 'C0 holds but gains are flat' family. Together they support: 'C0 pattern generalizes; SICA benefit depends on both C0 and trace quality.'"
288	  },
289	  {
290	    "name": "gsm8k_pilot_14b",
291	    "description": "Qwen2.5-14B on GSM8K 30 questions (K=12, T=0.7). Cross-domain C0 test.",
292	    "results": {
293	      "sica_accuracy": 0.867,
294	      "sc_accuracy": 0.867,
295	      "sica_sc_gap_pp": 0.0,
296	      "c0_multi_candidate_rate": 0.1,
297	      "n_problems": 30,
298	      "tiebreak_cases": 0,
299	      "constraint_extraction_rate": 0.97,
300	      "sc_baseline_accuracy": 0.867,
301	      "wall_time_hours": 0.9
302	    },
303	    "tables": [
304	      "Appendix table: GSM8K pilot (C0=10%, gap=0pp, SC accuracy=86.7%)"
305	    ],
306	    "figures": [],
307	    "analysis": "GSM8K confirms that C0 is low when model competence is high, regardless of answer-space type. This is important for the paper's claim that C0 reflects 'task-relative model confidence.' Include in appendix as cross-domain validation. The result also pre-empts reviewer concern 'only works on restricted answer spaces' — we tested open-answer math and found C0 naturally low (model doesn't need help), which is exactly the predicted behavior.\n\nQwen2.5-14B is strong on GSM8K (baseline ~87% with SC@12). The open-answer-space (numeric) combined with high model competence means the model almost always converges on the correct numerical answer. C0=10% — only 3 out of 30 questions produce any answer diversity, and those are the hardest items where the model sometimes makes arithmetic errors. With C0=10% (below 20% threshold but above 5%), this lands in the 'uncertain zone' — not quite degenerate but not clearly in SICA's operating regime. Zero ties means SICA has no mechanism to help. Gap is 0pp. This validates C0 as a cross-domain diagnostic: on tasks where the model is confident (high accuracy), C0 is low and SICA is unnecessary. The result also shows C0 reflects task-relative confidence, not answer-space properties (math has infinite answer space but low C0 when the model is competent)."
308	  },
309	  {
310	    "name": "constraint_ablation",
311	    "description": "CPU ablation: SICA-MaxSAT vs SICA-count-only vs SICA-random-weight on exp-001 data",
312	    "results": {
313	      "maxsat_accuracy_combined": 0.718,
314	      "count_only_accuracy_combined": 0.711,
315	      "random_weight_accuracy_combined": 0.706,
316	      "maxsat_vs_countonly_gap_pp": 0.7,
317	      "maxsat_vs_random_gap_pp": 1.2,
318	      "countonly_vs_sc_gap_pp": 0.8,
319	      "maxsat_folio_accuracy": 0.784,
320	      "count_only_folio_accuracy": 0.77,
321	      "maxsat_vs_countonly_folio_pp": 1.4,
322	      "tiebreak_agreement_maxsat_countonly": 0.78,
323	      "n_problems": 804
324	    },
325	    "tables": [
326	      "Appendix table: Constraint Ablation (MaxSAT 71.8%, Count-only 71.1%, Random-weight 70.6%, SC 70.3%)"
327	    ],
328	    "figures": [],
329	    "analysis": "MaxSAT is NOT essential for the core accuracy claim — count-only gets you 70% of the way there. But MaxSAT provides: (1) marginal additional accuracy, (2) interpretability (you can inspect which constraints were satisfied/excluded), (3) formal grounding (satisfiability checking is principled). Paper frames this as: 'MaxSAT provides interpretability and marginal accuracy gains over simpler alternatives. The primary contribution is the constraint-based framework and C0 diagnostic, not the specific solver.' This defuses the 'over-engineering' attack while preserving the intellectual contribution.\n\nIn the median tier, MaxSAT is marginally better than count-only but the delta is <2pp. This happens because on most tie cases, the constraint count already correlates with the correct answer (more constraints → more reasoning traces support it → more likely correct). MaxSAT adds value only when constraint QUALITY matters — i.e., when a few high-quality constraints for the correct answer outweigh many low-quality constraints for the wrong answer. On 804 questions with 68 ties, only ~15 cases show this pattern, yielding the marginal 0.7pp overall difference. Count-only still beats SC (by 0.8pp) because even raw constraint counting provides better tiebreaking than arbitrary rules. Random-weight performs worst because it destroys the informative signal entirely. The FOLIO subset shows the clearest MaxSAT advantage (+1.4pp over count-only) because formal-logic constraints have clearer satisfiability structure."
330	  },
331	  {
332	    "name": "sica_deepseek_r1_llama_8b",
333	    "description": "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions, K=12, T=0.7",
334	    "results": {
335	      "sica_accuracy": 0.683,
336	      "sc_accuracy": 0.683,
337	      "sica_sc_gap_pp": 0.0,
338	      "c0_multi_candidate_rate": 0.05,
339	      "bootstrap_p": null,
340	      "folio_sica": 0.7,
341	      "folio_sc": 0.7,
342	      "folio_gap_pp": 0.0,
343	      "proofwriter_sica": 0.667,
344	      "proofwriter_sc": 0.667,
345	      "proofwriter_gap_pp": 0.0,
346	      "tiebreak_cases": 0,
347	      "tiebreak_win_rate": null,
348	      "constraint_extraction_rate": 0.95,
349	      "wall_time_hours": 1.8
350	    },
351	    "tables": [
352	      "T1: DeepSeek-R1-LLaMA-8B row (all gaps = 0.0pp, C0 = 5%)"
353	    ],
354	    "figures": [],
355	    "analysis": "DeepSeek-R1 is the second reasoning model confirmation. Together with QwQ-32B, establishes: reasoning models (any architecture, any scale) → C0<5% → SICA redundant. The contrast with LLaMA-8B-Instruct (same base, C0=40%, gap=+3.4pp) is particularly powerful: same architecture, instruction tuning vs reasoning distillation, completely different operating regime. This becomes a key comparison pair in the paper: 'LLaMA-8B-Instruct (C0=40%, +3.4pp) vs DeepSeek-R1-LLaMA-8B (C0=5%, 0pp) — same architecture, different training paradigm, opposite SICA behavior.'\n\nDeepSeek-R1-Distill-LLaMA-8B is a reasoning model (distilled from R1) despite its smaller size. Like QwQ-32B, it has internalized extended chain-of-thought that produces self-consistent outputs. C0=5% (borderline, at the threshold) — only 3 out of 60 questions show any diversity, and those have overwhelming majorities. The key difference from QwQ-32B: DeepSeek-R1 has a LLaMA base architecture, eliminating the 'still Qwen family' attack on the QwQ data. Combined with QwQ-32B (C0=3.6%), this establishes: reasoning models as a CLASS show C0<5%, regardless of base architecture (Qwen or LLaMA) or scale (8B or 32B). SICA≡SC structurally. SC accuracy of 68.3% is higher than LLaMA-8B-Instruct's 58.3% despite same parameter count — reasoning distillation significantly improves accuracy while eliminating diversity. This is the clean 'reasoning vs instruction' contrast within the same architecture family."
356	  }
357	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5af4867f-8668-419d-9084-0244628d63e7",
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "5364d42c-27cc-45c9-b29f-83ebbfd34347",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"sica_expanded_14b\",\n    \"description\": \"PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7, Qwen2.5-14B-Instruct\",\n    \"results\": {\n      \"n_total\": 804,\n      \"n_folio\": 204,\n      \"n_proofwriter\": 600,\n      \"sica_accuracy_combined\": 0.718,\n      \"sc_accuracy_combined\": 0.703,\n      \"sica_sc_gap_combined_pp\": 1.5,\n      \"bootstrap_p_combined\": 0.19,\n      \"sica_accuracy_folio\": 0.784,\n      \"sc_accuracy_folio\": 0.745,\n      \"sica_sc_gap_folio_pp\": 3.9,\n      \"bootstrap_p_folio\": 0.08,\n      \"sica_accuracy_proofwriter\": 0.695,\n      \"sc_accuracy_proofwriter\": 0.689,\n      \"sica_sc_gap_proofwriter_pp\": 0.6,\n      \"bootstrap_p_proofwriter\": 0.38,\n      \"c0_multi_candidate_rate\": 0.42,\n      \"c0_folio\": 0.52,\n      \"c0_proofwriter\": 0.38,\n      \"tiebreak_cases\": 68,\n      \"tiebreak_sica_wins\": 44,\n      \"tiebreak_win_rate\": 0.647,\n      \"maxsat_exclusion_rate\": 0.031,\n      \"total_constraints_unique\": 23800,\n      \"wall_time_hours\": 13.2\n    },\n    \"tables\": [\n      \"T1: Main Results (14B row: FOLIO 78.4 vs 74.5, PW 69.5 vs 68.9, Combined 71.8 vs 70.3)\",\n      \"T2: Tiebreak Analysis (68 ties, SICA wins 44, SC wins 24, win rate 64.7%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"FOLIO is strongest evidence for Claim 1 but p=0.08 requires careful framing — 'trending toward significance' or report one-tailed. Combined result is not significant; paper must not overclaim. ProofWriter contributes to C0 validation (even at C0=0.38, gains are minimal on closed-world tasks) which actually supports the narrative that task formality matters. Key insight for paper: SICA's value concentrates in tie-heavy formal-logic domains, not uniformly across all logic tasks.\\n\\nAt scale, FOLIO retains a real but attenuated gap (~3.9pp vs pilot's 6.7pp) because the pilot's 30 questions were disproportionately tie-heavy; the full 204 includes easier items where SC already converges (C0 drops on easy items). Bootstrap p lands at 0.08 — suggestive but not clean at α=0.05. ProofWriter's closed-world reasoning produces less diverse traces than FOLIO's open-world NLI; most PW gains come from depth-5 items where traces occasionally diverge, but the majority of PW questions show near-unanimous SC votes, yielding a negligible 0.6pp gap (p=0.38). Combined significance is diluted by PW's 600-question mass pulling the average toward zero. The C0 rate of 0.42 confirms the operating regime (>20%) but the per-question C0 variance means many individual questions contribute zero signal. Tiebreak win rate of 64.7% is above random (50%) but below the pilot's 80% (small-sample inflation in pilot).\"\n  },\n  {\n    \"name\": \"sica_k_ablation_14b\",\n    \"description\": \"K sensitivity (K=6,8,12,16,20) on D012's 60 questions, Qwen2.5-14B-Instruct\",\n    \"results\": {\n      \"k6_sica_accuracy\": 0.717,\n      \"k6_sc_accuracy\": 0.7,\n      \"k6_gap_pp\": 1.7,\n      \"k6_c0\": 0.4,\n      \"k6_tie_rate\": 0.15,\n      \"k8_sica_accuracy\": 0.733,\n      \"k8_sc_accuracy\": 0.7,\n      \"k8_gap_pp\": 3.3,\n      \"k8_c0\": 0.47,\n      \"k8_tie_rate\": 0.22,\n      \"k12_sica_accuracy\": 0.733,\n      \"k12_sc_accuracy\": 0.7,\n      \"k12_gap_pp\": 3.3,\n      \"k12_c0\": 0.53,\n      \"k12_tie_rate\": 0.25,\n      \"k16_sica_accuracy\": 0.75,\n      \"k16_sc_accuracy\": 0.717,\n      \"k16_gap_pp\": 3.3,\n      \"k16_c0\": 0.57,\n      \"k16_tie_rate\": 0.18,\n      \"k20_sica_accuracy\": 0.75,\n      \"k20_sc_accuracy\": 0.733,\n      \"k20_gap_pp\": 1.7,\n      \"k20_c0\": 0.6,\n      \"k20_tie_rate\": 0.13,\n      \"wall_time_hours\": 4.5\n    },\n    \"tables\": [\n      \"T3: K Sensitivity (K vs gap, C0, tie_rate — shows inverted-U peak at K=8-12)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"The inverted-U supports the 'principled tiebreaker' narrative: SICA's value is mechanistically tied to tie frequency, not a general accuracy boost. Paper should emphasize K=8-12 as practical recommendation. The fact that gap doesn't grow unboundedly with K is actually a feature for the 'operating regime' story — it shows SICA's contribution is bounded and predictable.\\n\\nC0 increases monotonically with K (more samples → more chance of diverse answers), but SICA-SC gap does not scale linearly. At K=6, too few traces means ties are rare (15%) and SC often has a clear majority — SICA has few opportunities to intervene. K=8 and K=12 hit the sweet spot: even K values create more exact ties, giving SICA maximum leverage. At K=16/20, C0 rises further but the majority winner becomes more stable (law of large numbers); ties actually decrease because the leading answer accumulates enough margin. The gap at K=20 shrinks because SC's majority is robust enough that tiebreaking matters less. This produces an inverted-U pattern peaking around K=8-12. Critically, odd K values (not tested here but inferrable) would show fewer ties, further supporting that SICA's primary mechanism is tiebreaking rather than general accuracy improvement.\"\n  },\n  {\n    \"name\": \"tiebreak_baseline_analysis\",\n    \"description\": \"SICA vs SC-random vs SC-deterministic on all available data. CPU reanalysis.\",\n    \"results\": {\n      \"n_tiebreak_cases_d012\": 5,\n      \"sica_tiebreak_accuracy\": 0.8,\n      \"random_tiebreak_accuracy_mean\": 0.5,\n      \"alphabetical_tiebreak_accuracy\": 0.6,\n      \"first_seen_tiebreak_accuracy\": 0.4,\n      \"n_tiebreak_cases_expanded\": 68,\n      \"sica_tiebreak_accuracy_expanded\": 0.647,\n      \"random_tiebreak_accuracy_expanded_mean\": 0.485,\n      \"sica_vs_random_p_expanded\": 0.035,\n      \"overall_sica_accuracy_with_random_baseline\": 0.71,\n      \"sica_minus_random_baseline_gap_pp\": 0.8\n    },\n    \"tables\": [\n      \"T2 extended: Tiebreak comparison table (SICA 64.7%, Random 48.5%, Alphabetical 52.9%, First-seen 45.6%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is both the strongest and most modest result: SICA is a statistically significant better tiebreaker (p=0.035 on ties), but overall accuracy gain over a fair random baseline is small (~0.8pp). Paper must be honest about this decomposition. Reframe: 'SICA provides principled, interpretable tiebreaking with significant per-tie advantage, contributing a modest but consistent overall accuracy improvement.' The interpretability angle (you can inspect WHY SICA chose an answer via constraints) becomes the differentiator over random.\\n\\nOn the original D012 5 ties, SICA's 80% (4/5) is consistent with pilot data. On expanded 68 ties, SICA's advantage regresses toward a more realistic 64.7% — still meaningfully above random's ~48.5% (random doesn't hit exactly 50% due to answer distribution asymmetry in the dataset). The critical comparison is: if SC uses random tiebreaking instead of alphabetical, it already captures some of the 'gap' attributed to SICA. The overall SICA-vs-SC-random gap shrinks to ~0.8pp (from 1.5pp vs deterministic), because random tiebreak is correct ~50% of the time on ties vs SICA's ~65%. This means roughly half of SICA's overall accuracy advantage comes from better tiebreaking specifically, and the other half from ties where SICA's constraint-weighted answer happens to differ from SC's majority (non-tie cases where MaxSAT exclusion changes the winner). The p=0.035 on tie-only comparison is the paper's cleanest statistical result.\"\n  },\n  {\n    \"name\": \"sica_7b_scaling\",\n    \"description\": \"Qwen2.5-7B-Instruct on D012 60 questions, K=12, T=0.7\",\n    \"results\": {\n      \"sica_accuracy\": 0.65,\n      \"sc_accuracy\": 0.617,\n      \"sica_sc_gap_pp\": 3.3,\n      \"c0_multi_candidate_rate\": 0.55,\n      \"bootstrap_p\": 0.18,\n      \"folio_sica\": 0.7,\n      \"folio_sc\": 0.633,\n      \"folio_gap_pp\": 6.7,\n      \"proofwriter_sica\": 0.619,\n      \"proofwriter_sc\": 0.607,\n      \"proofwriter_gap_pp\": 1.2,\n      \"tiebreak_cases\": 11,\n      \"tiebreak_win_rate\": 0.636,\n      \"constraint_extraction_rate\": 0.92,\n      \"wall_time_hours\": 1.8\n    },\n    \"tables\": [\n      \"T1: 7B row (FOLIO 70.0 vs 63.3, PW 61.9 vs 60.7, Combined 65.0 vs 61.7)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B confirms 'weaker model → higher C0 → SICA helps more' directionally. But the C0 jump (0.53→0.55) is smaller than hoped — median tier says the scaling trend is noisy. The 7B point helps the F2 scatter plot but doesn't create a clean linear relationship. For the paper: include in T1 and F2, note that within-family scaling shows the expected direction but the gradient is shallow for adjacent sizes.\\n\\n7B is weaker than 14B (SC baseline drops from 70% to ~62%), producing more diverse outputs (C0 rises from 0.53 to 0.55). The C0 increase is real but modest — the 7B model is weaker but not dramatically so on these tasks; it still often converges on common answers. The SICA gap of 3.3pp matches the median expectation — higher C0 creates more intervention opportunities, but 7B's constraint extraction quality is lower (92% vs 100% for 14B), partially offsetting the diversity advantage. FOLIO shows the clearest gain (+6.7pp) because open-world NLI with a 3-class answer space maximizes tie probability for a confused model. However, bootstrap p=0.18 on 60 questions means none of this is individually significant — only the cross-model pattern matters. The key data point is: C0(7B)=0.55 > C0(14B)=0.53, confirming the directional scaling trend even if the magnitude is modest.\"\n  },\n  {\n    \"name\": \"qwq_32b_operating_regime\",\n    \"description\": \"Format existing QwQ-32B data for Operating Regime Analysis section\",\n    \"results\": {\n      \"c0_combined\": 0.036,\n      \"c0_aime\": 0.0,\n      \"c0_proofwriter\": 0.1875,\n      \"c0_folio\": 0.0,\n      \"sica_sc_gap_pp\": 0.0,\n      \"n_problems_total\": 48,\n      \"n_aime\": 22,\n      \"n_proofwriter\": 16,\n      \"n_folio\": 10,\n      \"reasoning_model_conclusion\": \"C0<5% → SICA≡SC structurally\"\n    },\n    \"tables\": [\n      \"T1: QwQ-32B row (all gaps = 0.0pp, C0 = 3.6%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"This is Claim 2's strongest evidence in the paper. The contrast between 14B-Instruct (C0=53%, gap=+3.3pp) and QwQ-32B (C0=3.6%, gap=0pp) on the SAME tasks demonstrates that C0 is the governing variable, not task difficulty. Present as: 'reasoning models self-consistent → SICA redundant; instruction models diverse → SICA helps.' This frames the negative result as a positive insight about operating regimes.\\n\\nQwQ-32B's reasoning chains are so self-consistent that sampling temperature has negligible effect on final answers. The model's extended chain-of-thought process (often 2000+ tokens) acts as an internal consistency mechanism — by the time it reaches an answer, it has self-corrected any stochastic variation. C0=3.6% means only ~2 out of 48 problems produced any answer diversity at all, and even those had overwhelming majorities. SICA is structurally identical to SC because there are no ties to break and no minority answers for MaxSAT to potentially elevate. This is the 'degenerate regime' — the method's mechanism (resolving disagreement) has no disagreement to resolve. The key insight is that this is model-class-dependent (reasoning vs instruction), not task-dependent (same FOLIO/PW tasks show high C0 on 14B instruction model).\"\n  },\n  {\n    \"name\": \"c0_diagnostic_validation\",\n    \"description\": \"C0 vs SICA-SC gap scatter plot across all models and K values. CPU analysis.\",\n    \"results\": {\n      \"n_data_points\": 14,\n      \"pearson_r\": 0.58,\n      \"spearman_rho\": 0.64,\n      \"c0_threshold_20_precision\": 0.75,\n      \"c0_threshold_20_recall\": 1.0,\n      \"c0_below_5_all_zero_gap\": true,\n      \"c0_above_20_positive_gap_rate\": 0.75,\n      \"binary_classification_accuracy\": 0.857,\n      \"auc_roc\": 0.82\n    },\n    \"tables\": [\n      \"Appendix table: All (model, dataset, K, C0, gap) data points\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"The binary diagnostic (C0>20% → try SICA, C0<5% → skip) is the paper's Claim 3 contribution. In median tier, it works as a diagnostic but NOT as a continuous predictor — the scatter has too much variance for a regression line to be useful. Paper should present the binary threshold clearly and acknowledge that within the 'SICA regime' (C0>20%), the magnitude of gain is task-dependent and not precisely predicted by C0 alone. This downgrades Claim 3 from 'continuous predictor' to 'binary diagnostic' as specified in the tier definition.\\n\\nWith ~14 data points (7B, 14B, 72B on 60q; 14B on 804q; QwQ on 48q; Mistral on 60q; LLaMA on 60q; DeepSeek-R1 on 60q; plus K-ablation variants), the correlation is positive but noisy (r=0.58). The noise comes from: (1) Mistral and LLaMA having high C0 but inconsistent gaps (one shows gain, one flat — median tier assumption), (2) K-ablation points clustering in a narrow C0 range, (3) PW subset having moderate C0 but near-zero gap (task formality confound). However, the BINARY diagnostic works well: C0<5% always means gap≈0 (reasoning models), and C0>20% means gap>0 in 75% of cases. The 25% failure rate (C0>20% but gap≈0) corresponds to cases where high diversity exists but constraint extraction quality is poor or the task doesn't benefit from symbolic reasoning (e.g., one cross-family model). Spearman (rank correlation) beats Pearson because the relationship is monotone but non-linear — there's a threshold effect rather than a smooth gradient.\"\n  },\n  {\n    \"name\": \"sica_72b_awq\",\n    \"description\": \"Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions, K=12, T=0.7\",\n    \"results\": {\n      \"sica_accuracy\": 0.783,\n      \"sc_accuracy\": 0.767,\n      \"sica_sc_gap_pp\": 1.6,\n      \"c0_multi_candidate_rate\": 0.37,\n      \"bootstrap_p\": 0.35,\n      \"folio_sica\": 0.867,\n      \"folio_sc\": 0.833,\n      \"folio_gap_pp\": 3.4,\n      \"proofwriter_sica\": 0.738,\n      \"proofwriter_sc\": 0.738,\n      \"proofwriter_gap_pp\": 0.0,\n      \"tiebreak_cases\": 4,\n      \"tiebreak_win_rate\": 0.75,\n      \"constraint_extraction_rate\": 1.0,\n      \"wall_time_hours\": 3.8\n    },\n    \"tables\": [\n      \"T1: 72B row (FOLIO 86.7 vs 83.3, PW 73.8 vs 73.8, Combined 78.3 vs 76.7)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B data creates the within-Qwen scaling dimension for the paper: 7B→14B→72B shows C0 decreasing and gap decreasing. But the pattern is noisy (7B and 14B are close, then 72B drops more). This is enough for a 'directional trend' claim but not a clean power law. Present as evidence that stronger instruction models approach but don't reach the reasoning model's degenerate regime. The 72B-AWQ quantization is a potential confound to acknowledge in limitations (4-bit may slightly increase randomness vs full precision).\\n\\n72B is stronger than 14B (SC baseline 76.7% vs 70%), so it converges more often — but NOT dramatically more. C0=0.37 is below 14B's 0.53 but still well above the 20% threshold. In median tier, '72B not clearly below 14B' means the C0 drop is real but modest (0.53→0.37, not 0.53→0.15). This happens because 72B is still an instruction model — it doesn't have the reasoning model's self-consistency mechanism, just better initial accuracy. It still produces diverse outputs on genuinely ambiguous items. The SICA gap is small (1.6pp) because: (1) fewer ties with 72B's stronger majorities, (2) on PW, 72B is so accurate that there's no room for improvement. FOLIO still shows a gap (+3.4pp) because even 72B finds open-world NLI challenging enough to produce diverse traces. The scaling story becomes: 7B (C0=0.55) > 14B (C0=0.53) > 72B (C0=0.37) — directionally correct but the 7B-14B gap is tiny while the 14B-72B gap is larger. This is 'noisy' because you'd expect a more uniform gradient.\"\n  },\n  {\n    \"name\": \"constraint_quality_case_studies\",\n    \"description\": \"Qualitative analysis of constraints on 5-10 representative questions from exp-001\",\n    \"results\": {\n      \"n_cases_analyzed\": 8,\n      \"semantically_meaningful_rate\": 0.75,\n      \"excluded_constraints_error_rate\": 0.83,\n      \"constraint_types\": [\n        \"entailment_chain\",\n        \"negation\",\n        \"universal_quantifier\",\n        \"conditional\",\n        \"disjunction\"\n      ],\n      \"avg_constraints_per_trace\": 4.2,\n      \"avg_unique_constraints_per_problem\": 14.8,\n      \"failure_modes\": [\n        \"over-literal parsing\",\n        \"scope ambiguity in quantifiers\",\n        \"implicit premises missed\"\n      ]\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies serve the interpretability narrative. Even if accuracy gains are modest, showing that MaxSAT exclusion corresponds to actual reasoning errors (83% of the time) validates the mechanism as principled rather than lucky. This supports reframing from 'accuracy tool' to 'interpretable reasoning aggregation.' Include 2-3 cherry-picked examples in main paper §4, full set in appendix.\\n\\nConstraint extraction from 14B traces is generally meaningful because FOLIO premises are already semi-formal (natural language with clear logical structure). ~75% of extracted constraints correctly capture the intended logical relationship. The 25% failures come from: (1) overly literal parsing of hedging language ('might', 'usually'), (2) quantifier scope ambiguity in nested sentences, (3) implicit common-sense premises that the model encodes but the extractor can't formalize. Excluded constraints (those MaxSAT deems unsatisfiable with the rest) correspond to reasoning errors ~83% of the time — this validates the MaxSAT mechanism as genuinely detecting flawed reasoning rather than randomly dropping constraints. The remaining 17% of exclusions are valid constraints that happen to conflict with the majority due to alternative valid interpretations.\"\n  },\n  {\n    \"name\": \"overhead_analysis\",\n    \"description\": \"Wall-time breakdown per question from exp-001 logs\",\n    \"results\": {\n      \"avg_total_time_per_question_s\": 59.1,\n      \"avg_generation_time_s\": 48.3,\n      \"avg_extraction_time_s\": 8.4,\n      \"avg_maxsat_time_s\": 2.4,\n      \"generation_fraction\": 0.817,\n      \"extraction_fraction\": 0.142,\n      \"maxsat_fraction\": 0.041,\n      \"overhead_vs_sc_percent\": 22.4,\n      \"sc_only_time_per_question_s\": 48.3,\n      \"batch_throughput_questions_per_hour\": 61\n    },\n    \"tables\": [\n      \"T4: Overhead breakdown (Generation 48.3s/81.7%, Extraction 8.4s/14.2%, MaxSAT 2.4s/4.1%, Total overhead +22.4%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"22% overhead is defensible for EMNLP — it's not 10x. Frame as: 'SICA adds modest overhead concentrated in constraint extraction (parallelizable), while MaxSAT solving is negligible. The primary cost is generation (shared with SC). Practical deployment with a dedicated extraction model could reduce overhead to <10%.' Reviewer concern addressed: the overhead IS worth it if you're in the C0>20% regime and want interpretable tiebreaking.\\n\\nGeneration dominates (82%) because K=12 traces each require a full forward pass through the 14B model. Constraint extraction adds ~8.4s per question (LLM-based extraction of FOL from 12 traces, batched). MaxSAT solving is negligible (~2.4s, Z3 on small instances). Total overhead vs pure SC is ~22% — SC would take 48.3s (just generation), SICA adds 10.8s for extraction+solving. This is modest for a research prototype but worth noting. The extraction step could be parallelized (currently sequential over traces) or replaced with a smaller model, suggesting practical deployment could reduce overhead to <10%. Generation time dominates because vLLM batches efficiently but 12 traces × 14B parameters × ~500 output tokens each is substantial.\"\n  },\n  {\n    \"name\": \"sica_mistral_7b\",\n    \"description\": \"Mistral-7B-Instruct-v0.3 on D012 60 questions, K=12, T=0.7\",\n    \"results\": {\n      \"sica_accuracy\": 0.583,\n      \"sc_accuracy\": 0.567,\n      \"sica_sc_gap_pp\": 1.6,\n      \"c0_multi_candidate_rate\": 0.35,\n      \"bootstrap_p\": 0.38,\n      \"folio_sica\": 0.6,\n      \"folio_sc\": 0.567,\n      \"folio_gap_pp\": 3.3,\n      \"proofwriter_sica\": 0.571,\n      \"proofwriter_sc\": 0.571,\n      \"proofwriter_gap_pp\": 0.0,\n      \"tiebreak_cases\": 6,\n      \"tiebreak_win_rate\": 0.667,\n      \"constraint_extraction_rate\": 0.85,\n      \"wall_time_hours\": 1.3\n    },\n    \"tables\": [\n      \"T1: Mistral-7B row (FOLIO 60.0 vs 56.7, PW 57.1 vs 57.1, Combined 58.3 vs 56.7)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mistral confirms C0>20% across families (critical) but shows that C0 is necessary-not-sufficient for SICA gains. The paper should acknowledge: 'Cross-family C0 pattern holds, but per-family SICA-SC delta varies with constraint extraction quality.' This is honest and actually strengthens the analysis paper framing — it identifies a second prerequisite beyond C0 (extraction quality). For the escalation decision: gap>0 but p>0.2 on 60 questions — per the plan note, could expand to 200+ questions, but median tier assumes we don't (GPU budget constraint or decision that the 60-question C0 confirmation is sufficient).\\n\\nMistral-7B is the 'one flat' family in the median tier's 'one shows gain, one flat' cross-family pattern. C0=0.35 confirms C0>20% holds outside Qwen (critical for Claim 2), but the SICA-SC gap is small and noisy (+1.6pp, p=0.38). This happens because Mistral's constraint extraction quality is lower (85% vs Qwen's 100%) — the model produces less structured reasoning traces, leading to more extraction failures and lower-quality constraints. When MaxSAT operates on noisy constraints, its tiebreaking advantage is partially offset by occasional wrong exclusions. FOLIO still shows a positive direction (+3.3pp) but PW is flat. The key takeaway is: C0 pattern generalizes (Mistral instruction model produces diverse outputs), but SICA's benefit depends on BOTH diversity AND extraction quality. Mistral's shorter, less structured traces hurt extraction.\"\n  },\n  {\n    \"name\": \"sica_llama_8b\",\n    \"description\": \"LLaMA-3.1-8B-Instruct on D012 60 questions, K=12, T=0.7\",\n    \"results\": {\n      \"sica_accuracy\": 0.617,\n      \"sc_accuracy\": 0.583,\n      \"sica_sc_gap_pp\": 3.4,\n      \"c0_multi_candidate_rate\": 0.4,\n      \"bootstrap_p\": 0.14,\n      \"folio_sica\": 0.667,\n      \"folio_sc\": 0.6,\n      \"folio_gap_pp\": 6.7,\n      \"proofwriter_sica\": 0.583,\n      \"proofwriter_sc\": 0.571,\n      \"proofwriter_gap_pp\": 1.2,\n      \"tiebreak_cases\": 9,\n      \"tiebreak_win_rate\": 0.667,\n      \"constraint_extraction_rate\": 0.93,\n      \"wall_time_hours\": 1.4\n    },\n    \"tables\": [\n      \"T1: LLaMA-8B row (FOLIO 66.7 vs 60.0, PW 58.3 vs 57.1, Combined 61.7 vs 58.3)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"LLaMA provides the second positive cross-family confirmation. The 3-family narrative becomes: 'All three instruction-model families show C0>20% (operating regime confirmed), with two of three showing positive SICA-SC gaps and the third showing directional but flat improvement.' This is sufficient for EMNLP Findings — not every family needs significant gains if the C0 pattern is the primary claim. Paper frames Mistral's flat result as 'extraction quality moderates effectiveness' rather than as a failure.\\n\\nLLaMA-8B is the 'one shows gain' family in the median tier's cross-family pattern. C0=0.40 confirms diversity, and the gap (+3.4pp) is comparable to Qwen-14B's pilot result. LLaMA's instruction tuning produces reasonably structured outputs (extraction rate 93%), and at 8B parameters it's weak enough on FOLIO to produce genuine disagreement. The FOLIO gap of +6.7pp looks impressive but with only 30 FOLIO questions it's not significant (p=0.14 for combined). The key difference vs Mistral: LLaMA's traces are more structured (Meta's instruction tuning format includes clearer step markers), enabling better constraint extraction. This makes LLaMA the second 'positive signal' family alongside Qwen, while Mistral is the 'C0 holds but gains are flat' family. Together they support: 'C0 pattern generalizes; SICA benefit depends on both C0 and trace quality.'\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_14b\",\n    \"description\": \"Qwen2.5-14B on GSM8K 30 questions (K=12, T=0.7). Cross-domain C0 test.\",\n    \"results\": {\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.867,\n      \"sica_sc_gap_pp\": 0.0,\n      \"c0_multi_candidate_rate\": 0.1,\n      \"n_problems\": 30,\n      \"tiebreak_cases\": 0,\n      \"constraint_extraction_rate\": 0.97,\n      \"sc_baseline_accuracy\": 0.867,\n      \"wall_time_hours\": 0.9\n    },\n    \"tables\": [\n      \"Appendix table: GSM8K pilot (C0=10%, gap=0pp, SC accuracy=86.7%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K confirms that C0 is low when model competence is high, regardless of answer-space type. This is important for the paper's claim that C0 reflects 'task-relative model confidence.' Include in appendix as cross-domain validation. The result also pre-empts reviewer concern 'only works on restricted answer spaces' — we tested open-answer math and found C0 naturally low (model doesn't need help), which is exactly the predicted behavior.\\n\\nQwen2.5-14B is strong on GSM8K (baseline ~87% with SC@12). The open-answer-space (numeric) combined with high model competence means the model almost always converges on the correct numerical answer. C0=10% — only 3 out of 30 questions produce any answer diversity, and those are the hardest items where the model sometimes makes arithmetic errors. With C0=10% (below 20% threshold but above 5%), this lands in the 'uncertain zone' — not quite degenerate but not clearly in SICA's operating regime. Zero ties means SICA has no mechanism to help. Gap is 0pp. This validates C0 as a cross-domain diagnostic: on tasks where the model is confident (high accuracy), C0 is low and SICA is unnecessary. The result also shows C0 reflects task-relative confidence, not answer-space properties (math has infinite answer space but low C0 when the model is competent).\"\n  },\n  {\n    \"name\": \"constraint_ablation\",\n    \"description\": \"CPU ablation: SICA-MaxSAT vs SICA-count-only vs SICA-random-weight on exp-001 data\",\n    \"results\": {\n      \"maxsat_accuracy_combined\": 0.718,\n      \"count_only_accuracy_combined\": 0.711,\n      \"random_weight_accuracy_combined\": 0.706,\n      \"maxsat_vs_countonly_gap_pp\": 0.7,\n      \"maxsat_vs_random_gap_pp\": 1.2,\n      \"countonly_vs_sc_gap_pp\": 0.8,\n      \"maxsat_folio_accuracy\": 0.784,\n      \"count_only_folio_accuracy\": 0.77,\n      \"maxsat_vs_countonly_folio_pp\": 1.4,\n      \"tiebreak_agreement_maxsat_countonly\": 0.78,\n      \"n_problems\": 804\n    },\n    \"tables\": [\n      \"Appendix table: Constraint Ablation (MaxSAT 71.8%, Count-only 71.1%, Random-weight 70.6%, SC 70.3%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"MaxSAT is NOT essential for the core accuracy claim — count-only gets you 70% of the way there. But MaxSAT provides: (1) marginal additional accuracy, (2) interpretability (you can inspect which constraints were satisfied/excluded), (3) formal grounding (satisfiability checking is principled). Paper frames this as: 'MaxSAT provides interpretability and marginal accuracy gains over simpler alternatives. The primary contribution is the constraint-based framework and C0 diagnostic, not the specific solver.' This defuses the 'over-engineering' attack while preserving the intellectual contribution.\\n\\nIn the median tier, MaxSAT is marginally better than count-only but the delta is <2pp. This happens because on most tie cases, the constraint count already correlates with the correct answer (more constraints → more reasoning traces support it → more likely correct). MaxSAT adds value only when constraint QUALITY matters — i.e., when a few high-quality constraints for the correct answer outweigh many low-quality constraints for the wrong answer. On 804 questions with 68 ties, only ~15 cases show this pattern, yielding the marginal 0.7pp overall difference. Count-only still beats SC (by 0.8pp) because even raw constraint counting provides better tiebreaking than arbitrary rules. Random-weight performs worst because it destroys the informative signal entirely. The FOLIO subset shows the clearest MaxSAT advantage (+1.4pp over count-only) because formal-logic constraints have clearer satisfiability structure.\"\n  },\n  {\n    \"name\": \"sica_deepseek_r1_llama_8b\",\n    \"description\": \"DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions, K=12, T=0.7\",\n    \"results\": {\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.683,\n      \"sica_sc_gap_pp\": 0.0,\n      \"c0_multi_candidate_rate\": 0.05,\n      \"bootstrap_p\": null,\n      \"folio_sica\": 0.7,\n      \"folio_sc\": 0.7,\n      \"folio_gap_pp\": 0.0,\n      \"proofwriter_sica\": 0.667,\n      \"proofwriter_sc\": 0.667,\n      \"proofwriter_gap_pp\": 0.0,\n      \"tiebreak_cases\": 0,\n      \"tiebreak_win_rate\": null,\n      \"constraint_extraction_rate\": 0.95,\n      \"wall_time_hours\": 1.8\n    },\n    \"tables\": [\n      \"T1: DeepSeek-R1-LLaMA-8B row (all gaps = 0.0pp, C0 = 5%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DeepSeek-R1 is the second reasoning model confirmation. Together with QwQ-32B, establishes: reasoning models (any architecture, any scale) → C0<5% → SICA redundant. The contrast with LLaMA-8B-Instruct (same base, C0=40%, gap=+3.4pp) is particularly powerful: same architecture, instruction tuning vs reasoning distillation, completely different operating regime. This becomes a key comparison pair in the paper: 'LLaMA-8B-Instruct (C0=40%, +3.4pp) vs DeepSeek-R1-LLaMA-8B (C0=5%, 0pp) — same architecture, different training paradigm, opposite SICA behavior.'\\n\\nDeepSeek-R1-Distill-LLaMA-8B is a reasoning model (distilled from R1) despite its smaller size. Like QwQ-32B, it has internalized extended chain-of-thought that produces self-consistent outputs. C0=5% (borderline, at the threshold) — only 3 out of 60 questions show any diversity, and those have overwhelming majorities. The key difference from QwQ-32B: DeepSeek-R1 has a LLaMA base architecture, eliminating the 'still Qwen family' attack on the QwQ data. Combined with QwQ-32B (C0=3.6%), this establishes: reasoning models as a CLASS show C0<5%, regardless of base architecture (Qwen or LLaMA) or scale (8B or 32B). SICA≡SC structurally. SC accuracy of 68.3% is higher than LLaMA-8B-Instruct's 58.3% despite same parameter count — reasoning distillation significantly improves accuracy while eliminating diversity. This is the clean 'reasoning vs instruction' contrast within the same architecture family.\"\n  }\n]",
      "numLines": 357,
      "startLine": 1,
      "totalLines": 357
    }
  },
  "sourceToolAssistantUUID": "5af4867f-8668-419d-9084-0244628d63e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T13:00:15.239Z_

<details><summary>↩ Tool result · `toolu_014wicuHGJ75P5BACuMUQwwm`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Fallback: AAAI 2027 (Aug 1)
6	- Deadline: May 25, 2026 (ARR submission)
7	
8	## Core Claims (3 条)
9	1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).
10	2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: "C0 → epistemic uncertainty" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]
11	3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.
12	
13	## Core Insight
14	Symbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from "yet another ensemble method" into "a method with formally characterizable applicability boundaries," validated across 3 model families and multiple reasoning domains.
15	
16	## Story Spine
17	- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.
18	- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.
19	- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).
20	- **Headline result template**: "On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty."
21	
22	## Anticipated Reviewer Concerns & Defensive Experiments
23	1. **"Gains not statistically significant"** → exp-001: Expand to 804 questions for statistical power
24	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)
25	3. **"Only Qwen models — family-specific artifact?"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)
26	4. **"Only one reasoning model"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)
27	5. **"Only logic domain — restricted answer space"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)
28	6. **"ProofWriter shows 0pp gain"** → Domain analysis in exp-001 expanded results
29	7. **"Random tiebreak baseline closes the gap"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)
30	8. **"Why not just use a reasoning model?"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit
31	9. **"MAX-SAT is over-engineering"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting
32	10. **"Within-family scaling?"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family
33	
34	## Working Title
35	**"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"**
36	(Alternatives: "Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning")
37	
38	## Paper Structure (EMNLP 8pp + appendix)
39	- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)
40	- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)
41	- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail
42	
43	## Claim Risk Notes
44	- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as "principled weighting" not "satisfiability-based reasoning"
45	- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator" not "continuous predictor". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.
46	- **"Epistemic uncertainty" terminology**: Reserve for Discussion section only. Main text uses "effective output diversity" / "task-relative model confidence". UQ community would attack formal misuse.
47	
48	## Contingency Plan (D023)
49	**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）
50	**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)
51	- 论文主线从"SICA improves accuracy"转为"characterizing operating conditions of symbolic consensus"
52	- C0 threshold pattern 成为核心贡献（"at what C0 level does SICA begin to match/exceed SC?")
53	- FOLIO 正向结果嵌入为"domain formality → effectiveness"子 claim
54	- Claim 1 弱化为"principled + interpretable tiebreaking"（不 claim accuracy gain）
55	- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）
56	- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback
57	**Decision point**: exp-001 FOLIO 70题的 C0 和 delta
58	
59	## Venue Fit Risks
60	- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the "operating regime characterization" — the tiebreaking mechanism is evidence, not the claim.
61	- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.
62	- Negative results: QwQ-32B data must be presented as insight ("When Does Symbolic Consensus Degenerate?"), not failure.
63	- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.
64	- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce281765-9138-42f7-915f-c20255daf2bb",
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "d9ec2788-7918-48dd-806d-b32ef7363be7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: \"C0 → epistemic uncertainty\" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries,\" validated across 3 model families and multiple reasoning domains.\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 804 questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)\n3. **\"Only Qwen models — family-specific artifact?\"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)\n4. **\"Only one reasoning model\"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)\n5. **\"Only logic domain — restricted answer space\"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)\n6. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n7. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)\n8. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit\n9. **\"MAX-SAT is over-engineering\"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting\n10. **\"Within-family scaling?\"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family\n\n## Working Title\n**\"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation\"**\n(Alternatives: \"Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)\n- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)\n- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail\n\n## Claim Risk Notes\n- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as \"principled weighting\" not \"satisfiability-based reasoning\"\n- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\" not \"continuous predictor\". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.\n- **\"Epistemic uncertainty\" terminology**: Reserve for Discussion section only. Main text uses \"effective output diversity\" / \"task-relative model confidence\". UQ community would attack formal misuse.\n\n## Contingency Plan (D023)\n**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）\n**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)\n- 论文主线从\"SICA improves accuracy\"转为\"characterizing operating conditions of symbolic consensus\"\n- C0 threshold pattern 成为核心贡献（\"at what C0 level does SICA begin to match/exceed SC?\")\n- FOLIO 正向结果嵌入为\"domain formality → effectiveness\"子 claim\n- Claim 1 弱化为\"principled + interpretable tiebreaking\"（不 claim accuracy gain）\n- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）\n- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback\n**Decision point**: exp-001 FOLIO 70题的 C0 和 delta\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  },
  "sourceToolAssistantUUID": "ce281765-9138-42f7-915f-c20255daf2bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T13:00:15.234Z_

<details open><summary>🔧 Tool call — Read · `toolu_014wicuHGJ75P5BACuMUQwwm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5364d42c-27cc-45c9-b29f-83ebbfd34347",
  "isSidechain": false,
  "requestId": "req_011Cb6HkR8PqFNM5vwSJvU1r",
  "type": "assistant",
  "uuid": "ce281765-9138-42f7-915f-c20255daf2bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjPvETqMFFBT5PXyduj5BS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11212,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11212,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11212
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_c…",
  "leafUuid": "d9ec2788-7918-48dd-806d-b32ef7363be7",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on symbolic consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Assistant

_source line 14 · 2026-05-16T13:00:30.686Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data and framing. Let me write the paper. This is a median-tier dream paper for EMNLP Findings targeting 55-65% acceptance. The narrative guidance says:

1. Claim 1: reframed from 'accuracy improvement' to 'principled interpretable tiebreaking with positive trend on formal-logic domains'
2. Claim 2 (LEAD): C0 operating regime characterization is primary contribution, validated directionally across 3 families even though per-family SICA-SC deltas are noisy
3. Claim 3: downgraded from 'continuous predictor' to 'binary diagnostic' (C0>20% = try SICA, C0<5% = skip)


4. MaxSAT framed as 'interpretability + marginal gains'
5. Title: 'When Does Symbolic Consensus Help?'
6. Target: EMNLP Findings (55-65%)

Now I'm structuring the full paper with tables for each experiment—main results across model scales, K sensitivity analysis, tiebreak baseline comparisons, and the operating regime characterization across different model families. I'm organizing the paper structure with different sections for the operating regime analysis, diagnostic validation, model comparisons, and ablation studies. Now I need to ensure the output directory is ready before writing everything out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9ec2788-7918-48dd-806d-b32ef7363be7",
  "isSidechain": false,
  "requestId": "req_011Cb6HkjDaNsbpon4Zrhih8",
  "type": "assistant",
  "uuid": "b72adee1-4c46-4926-8978-b33961406f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qig31iyHQssJ3ct4CKoJ4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13066,
      "cache_read_input_tokens": 23053,
      "output_tokens": 657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 657,
          "cache_read_input_tokens": 23053,
          "cache_creation_input_tokens": 13066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13066
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

_source line 15 · 2026-05-16T13:00:30.688Z_

Let me check the output directory exists, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b72adee1-4c46-4926-8978-b33961406f85",
  "isSidechain": false,
  "requestId": "req_011Cb6HkjDaNsbpon4Zrhih8",
  "type": "assistant",
  "uuid": "74b974dd-da9c-4034-bbaf-e076352c78d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qig31iyHQssJ3ct4CKoJ4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13066,
      "cache_read_input_tokens": 23053,
      "output_tokens": 657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 657,
          "cache_read_input_tokens": 23053,
          "cache_creation_input_tokens": 13066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13066
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

_source line 16 · 2026-05-16T13:00:31.672Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012S5RFZwCrG9AmD7kMUyjZ2`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b974dd-da9c-4034-bbaf-e076352c78d5",
  "isSidechain": false,
  "requestId": "req_011Cb6HkjDaNsbpon4Zrhih8",
  "type": "assistant",
  "uuid": "69425996-5e17-4f69-b023-90ba7780ec7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qig31iyHQssJ3ct4CKoJ4n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13066,
      "cache_read_input_tokens": 23053,
      "output_tokens": 657,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 657,
          "cache_read_input_tokens": 23053,
          "cache_creation_input_tokens": 13066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13066
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

_source line 17 · 2026-05-16T13:00:31.842Z_

<details><summary>↩ Tool result · `toolu_012S5RFZwCrG9AmD7kMUyjZ2`</summary>

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
  "parentUuid": "69425996-5e17-4f69-b023-90ba7780ec7a",
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "04b6ce02-0597-496d-befc-8f109d50a697",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "69425996-5e17-4f69-b023-90ba7780ec7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T13:03:21.545Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QyAJ6pPGzAM6CUHc1pLzkc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{xcolor}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\title{When Does Symbolic Consensus Help? \\\\ Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nSelf-Consistency (SC) aggregates multiple LLM reasoning paths via majority voting but discards the logical structure within traces and resorts to arbitrary rules when votes are tied. We propose SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from reasoning traces and resolves disagreements via weighted partial MAX-SAT. Rather than claiming uniform accuracy improvements, we systematically characterize \\emph{when} symbolic consensus adds value. We introduce the multi-candidate rate $C_0$ --- the fraction of questions producing multiple distinct answers across $K$ sampled traces --- as a zero-cost diagnostic of effective output diversity. Through experiments spanning 3 instruction-model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and 2 formal-logic benchmarks (FOLIO, ProofWriter), we establish: (1) SICA provides principled, interpretable tiebreaking with a 64.7\\% win rate on ties ($p=0.035$ vs.\\ random) and a positive accuracy trend on formal-logic domains; (2) the $C_0$ operating regime governs SICA effectiveness --- instruction models exhibit $C_0 > 20\\%$ and benefit from SICA, while reasoning models show $C_0 < 5\\%$ where SICA degenerates to SC; (3) $C_0$ functions as a binary deployment diagnostic ($C_0 > 20\\% \\Rightarrow$ try SICA; $C_0 < 5\\% \\Rightarrow$ skip) with 85.7\\% classification accuracy. Our analysis reframes symbolic consensus from ``yet another ensemble method'' into a method with formally characterizable applicability boundaries.\n\\end{abstract}\n\n\\section{Introduction}\n\nLarge language models solve reasoning tasks more reliably when multiple reasoning paths are sampled and aggregated. Self-Consistency \\cite{wang2023selfconsistency} established majority voting over diverse chain-of-thought traces as a simple and effective strategy. However, SC treats each trace as an opaque vote, discarding the logical structure within. When votes are tied --- a common occurrence with even-$K$ sampling or narrow answer margins --- SC falls back to arbitrary rules (alphabetical order, first-seen, or random selection) with no principled resolution mechanism.\n\nWe propose SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to identify the answer most consistent with the collective reasoning. Rather than positioning SICA as a uniform accuracy improvement over SC, we ask a more fundamental question: \\emph{when does symbolic consensus help?}\n\nOur primary contribution is characterizing the \\textbf{operating regime} of symbolic consensus through the lens of trace diversity. We define the multi-candidate rate $C_0$ as the fraction of questions that produce multiple distinct candidate answers across $K$ sampled traces. $C_0$ reflects effective output diversity --- a proxy for task-relative model confidence. Our key finding is that $C_0$ governs SICA's effectiveness:\n\n\\begin{itemize}\n    \\item When $C_0 > 20\\%$ (instruction models on challenging logic tasks), traces disagree frequently, creating opportunities for principled tiebreaking. SICA wins 64.7\\% of tie cases ($p=0.035$) and shows positive accuracy trends.\n    \\item When $C_0 < 5\\%$ (reasoning models universally), traces are self-consistent. SICA degenerates to SC structurally --- there is no disagreement to resolve.\n\\end{itemize}\n\nThis pattern holds across 3 instruction-model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B), establishing that the operating regime is determined by model \\emph{class} (instruction vs.\\ reasoning), not model family or task domain.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item A principled interpretable tiebreaking mechanism for SC that achieves statistically significant per-tie advantage ($p=0.035$) with positive accuracy trends on formal-logic domains (+3.9pp on FOLIO, $p=0.08$).\n    \\item Systematic characterization of the $C_0$ operating regime across 7 model configurations, revealing that instruction-tuned models exhibit high $C_0$ universally while reasoning models show near-zero $C_0$.\n    \\item Validation of $C_0$ as a practical binary deployment diagnostic (AUC=0.82, accuracy=85.7\\%) that enables practitioners to decide whether SICA deployment is worthwhile without running full symbolic analysis.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and Variants.} Wang et al.\\ (2023) introduced Self-Consistency, using majority voting over diverse reasoning paths. Universal Self-Consistency (Chen et al., 2023) extends SC to open-ended generation. Both methods treat traces as opaque votes and offer no mechanism for tie resolution or constraint-based reasoning. Our work complements SC by adding a principled aggregation layer that activates precisely when voting is insufficient.\n\n\\paragraph{Symbolic Reasoning with LLMs.} Recent work integrates symbolic solvers with neural generation: Logic-LM (Pan et al., 2023) translates problems to formal logic before solving, while Faithful CoT (Lyu et al., 2023) generates symbolic representations alongside natural language chains. Unlike these single-trace approaches, SICA operates \\emph{post-hoc} on multiple traces, requiring no modification to the generation process.\n\n\\paragraph{Ensemble Uncertainty.} Lakshminarayanan et al.\\ (2017) established deep ensemble disagreement as an uncertainty signal. Our $C_0$ metric is analogous --- measuring effective output diversity across sampled LLM traces --- but we use it prescriptively (to predict method applicability) rather than solely for uncertainty estimation.\n\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a reasoning problem $q$, we sample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from a language model at temperature $T$. Each trace produces a candidate answer $a_i$. Self-Consistency selects $\\hat{a}_{SC} = \\arg\\max_a \\sum_{i=1}^K \\mathbb{1}[a_i = a]$.\n\n\\subsection{SICA Pipeline}\n\nSICA augments SC with three additional stages:\n\n\\paragraph{Step 1: Constraint Extraction.} For each trace $t_i$, we extract a set of first-order logic constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ using the same LLM with a structured extraction prompt. Each constraint captures a logical relationship asserted in the reasoning (entailment chains, negations, universal quantifiers, conditionals, disjunctions). Across all traces, we collect $\\mathcal{C} = \\bigcup_i \\mathcal{C}_i$.\n\n\\paragraph{Step 2: Weighted Partial MAX-SAT.} We formulate answer selection as a weighted partial MAX-SAT problem. For each candidate answer $a$, we compute:\n\\begin{equation}\n    \\text{score}(a) = \\text{MAX-SAT}(\\mathcal{C}_a, w)\n\\end{equation}\nwhere $\\mathcal{C}_a \\subseteq \\mathcal{C}$ are constraints consistent with answer $a$, and weights $w$ reflect constraint frequency across traces. The solver (Z3) maximizes the total weight of satisfiable constraints, identifying the answer supported by the most coherent set of reasoning.\n\n\\paragraph{Step 3: Answer Selection.} SICA selects:\n\\begin{equation}\n    \\hat{a}_{SICA} = \\arg\\max_a \\text{score}(a)\n\\end{equation}\n\nWhen SC has a clear majority and no ties exist, SICA typically agrees with SC. The mechanism primarily activates on tie cases and near-ties where constraint quality distinguishes candidates.\n\n\\subsection{Multi-Candidate Rate ($C_0$)}\n\nWe define the multi-candidate rate as:\n\\begin{equation}\n    C_0 = \\frac{1}{N} \\sum_{j=1}^N \\mathbb{1}\\left[|\\{a_i^{(j)}\\}_{i=1}^K| > 1\\right]\n\\end{equation}\nwhere $N$ is the number of questions and $|\\{a_i^{(j)}\\}_{i=1}^K|$ counts distinct answers produced for question $j$. $C_0$ measures the fraction of questions exhibiting any output diversity --- a necessary condition for SICA to intervene.\n\n\\section{Experimental Setup}\n\n\\subsection{Benchmarks}\n\\begin{itemize}\n    \\item \\textbf{FOLIO} (Han et al., 2022): 204 natural language inference problems requiring first-order logic reasoning. 3-class classification (True/False/Unknown). Open-world semantics.\n    \\item \\textbf{ProofWriter} (Tafjord et al., 2021): 600 depth-5 deductive reasoning problems. Binary classification (True/False). Closed-world semantics.\n\\end{itemize}\n\n\\subsection{Models}\nWe evaluate 7 model configurations spanning 3 instruction families and 2 reasoning architectures:\n\\begin{itemize}\n    \\item \\textbf{Instruction models}: Qwen2.5-7B/14B/72B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct\n    \\item \\textbf{Reasoning models}: QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B\n\\end{itemize}\n\n\\subsection{Configuration}\nAll experiments use $K=12$ sampled traces at temperature $T=0.7$ unless otherwise noted. Constraint extraction uses the same model that generated the traces. MAX-SAT solving uses Z3. The expanded evaluation (804 questions) uses Qwen2.5-14B-Instruct; cross-model experiments use the 60-question subset (30 FOLIO + 30 ProofWriter from the D0+D1+D2 split).\n\n\\section{Results}\n\n\\subsection{Main Results: Operating Regime Characterization}\n\nTable~\\ref{tab:main} presents accuracy across all model configurations. The central finding is the stark contrast between instruction and reasoning models in terms of $C_0$ and SICA effectiveness.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results across model configurations ($K=12$, $T=0.7$). $C_0$: multi-candidate rate. $\\Delta$: SICA$-$SC gap in percentage points. Instruction models (top) show $C_0 > 20\\%$ with positive trends; reasoning models (bottom) show $C_0 < 5\\%$ with zero gap.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\n\\multirow{2}{*}{Model} & \\multirow{2}{*}{$C_0$} & \\multicolumn{2}{c}{FOLIO} & \\multicolumn{2}{c}{ProofWriter} & \\multicolumn{2}{c}{Combined} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\n & & SC & SICA & SC & SICA & SC & SICA \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Instruction Models ($C_0 > 20\\%$)}} \\\\\n\\midrule\nQwen2.5-7B & 0.55 & 63.3 & 70.0 & 60.7 & 61.9 & 61.7 & 65.0 \\\\\nQwen2.5-14B$^\\dagger$ & 0.42 & 74.5 & 78.4 & 68.9 & 69.5 & 70.3 & 71.8 \\\\\nQwen2.5-72B-AWQ & 0.37 & 83.3 & 86.7 & 73.8 & 73.8 & 76.7 & 78.3 \\\\\nMistral-7B & 0.35 & 56.7 & 60.0 & 57.1 & 57.1 & 56.7 & 58.3 \\\\\nLLaMA-3.1-8B & 0.40 & 60.0 & 66.7 & 57.1 & 58.3 & 58.3 & 61.7 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Reasoning Models ($C_0 < 5\\%$)}} \\\\\n\\midrule\nQwQ-32B & 0.036 & --- & --- & --- & --- & --- & --- \\\\\nDeepSeek-R1-LLaMA-8B & 0.05 & 70.0 & 70.0 & 66.7 & 66.7 & 68.3 & 68.3 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize $^\\dagger$ Expanded evaluation: 204 FOLIO + 600 ProofWriter = 804 questions. Others: 60 questions.} \\\\\n\\multicolumn{8}{l}{\\footnotesize QwQ-32B: all gaps = 0.0pp across 48 questions (22 AIME + 16 PW + 10 FOLIO).} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Key observations.} All five instruction models show $C_0 > 35\\%$, indicating substantial output diversity. All show non-negative SICA--SC gaps, with the strongest effects on FOLIO (open-world NLI). Both reasoning models show $C_0 < 5\\%$, with SICA $\\equiv$ SC structurally (zero ties, zero gap). The contrast is particularly striking for the LLaMA architecture pair: LLaMA-3.1-8B-Instruct ($C_0 = 40\\%$, $\\Delta = +3.4$pp) versus DeepSeek-R1-Distill-LLaMA-8B ($C_0 = 5\\%$, $\\Delta = 0$pp) --- same base architecture, different training paradigm, opposite SICA behavior.\n\n\\paragraph{Within-family scaling (Qwen).} $C_0$ decreases with scale: 7B (0.55) $>$ 14B (0.42) $>$ 72B (0.37). The SICA--SC gap shows a corresponding directional decrease, though the gradient is noisy (7B and 14B show similar gaps). Stronger instruction models approach but do not reach the reasoning model's degenerate regime ($C_0 < 5\\%$).\n\n\\paragraph{Cross-family validation.} All three instruction-model families confirm $C_0 > 20\\%$. Two of three (Qwen, LLaMA) show clear positive SICA--SC gaps; Mistral shows a directional but smaller improvement (+1.6pp). The difference is attributable to constraint extraction quality: Mistral's less structured traces yield 85\\% extraction rate versus 93--100\\% for Qwen and LLaMA.\n\n\\subsection{Tiebreak Analysis}\n\nTable~\\ref{tab:tiebreak} isolates SICA's performance specifically on tie cases --- questions where SC has no clear majority winner.\n\n\\begin{table}[t]\n\\centering\n\\caption{Tiebreak analysis on the expanded 804-question evaluation (Qwen2.5-14B). SICA is compared against alternative tiebreaking strategies applied only to tie cases.}\n\\label{tab:tiebreak}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nTiebreak Strategy & Accuracy on Ties & Win Rate & $p$-value (vs.\\ Random) \\\\\n\\midrule\nSICA (MAX-SAT) & 64.7\\% & 44/68 & 0.035 \\\\\nRandom & 48.5\\% & --- & --- \\\\\nAlphabetical & 52.9\\% & --- & --- \\\\\nFirst-seen & 45.6\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA achieves a 64.7\\% win rate on 68 tie cases, significantly outperforming random tiebreaking ($p = 0.035$). This is the paper's cleanest statistical result: on cases where SC provides no signal, symbolic constraint analysis correctly resolves the tie nearly two-thirds of the time. The overall accuracy contribution of better tiebreaking is modest ($\\sim$0.8pp over a fair random baseline), but the per-tie advantage is meaningful and, critically, \\emph{interpretable} --- practitioners can inspect which constraints led to SICA's decision.\n\n\\subsection{Expanded Evaluation (804 Questions)}\n\nOn the full 804-question evaluation with Qwen2.5-14B:\n\\begin{itemize}\n    \\item Combined: SICA 71.8\\% vs.\\ SC 70.3\\% (+1.5pp, bootstrap $p = 0.19$)\n    \\item FOLIO (204 questions): SICA 78.4\\% vs.\\ SC 74.5\\% (+3.9pp, $p = 0.08$)\n    \\item ProofWriter (600 questions): SICA 69.5\\% vs.\\ SC 68.9\\% (+0.6pp, $p = 0.38$)\n\\end{itemize}\n\nThe FOLIO result trends toward significance ($p = 0.08$) and represents the strongest evidence for SICA's value on formal-logic domains with open-world semantics. ProofWriter's closed-world reasoning produces less diverse traces (lower per-question $C_0$), yielding a negligible gap. The combined result is diluted by ProofWriter's 600-question mass. We note that the per-tie significance ($p = 0.035$) provides cleaner statistical support for SICA's mechanism than the overall accuracy comparison.\n\n\\subsection{$C_0$ as Binary Deployment Diagnostic}\n\n\\begin{table}[t]\n\\centering\n\\caption{$C_0$ diagnostic performance across 14 (model, dataset, $K$) configurations.}\n\\label{tab:diagnostic}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nData points & 14 \\\\\nPearson $r$ ($C_0$ vs.\\ gap) & 0.58 \\\\\nSpearman $\\rho$ & 0.64 \\\\\nBinary threshold ($C_0 = 20\\%$) precision & 0.75 \\\\\nBinary threshold ($C_0 = 20\\%$) recall & 1.00 \\\\\n$C_0 < 5\\%$ $\\Rightarrow$ gap $= 0$ & 100\\% \\\\\n$C_0 > 20\\%$ $\\Rightarrow$ gap $> 0$ & 75\\% \\\\\nBinary classification accuracy & 85.7\\% \\\\\nAUC-ROC & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe evaluate $C_0$ as a \\emph{binary} diagnostic rather than a continuous predictor (the scatter has too much variance for reliable regression). The practical rule is:\n\n\\begin{itemize}\n    \\item $C_0 > 20\\%$: Deploy SICA (positive gap in 75\\% of configurations).\n    \\item $C_0 < 5\\%$: Skip SICA (gap $= 0$ in 100\\% of configurations).\n    \\item $5\\% < C_0 < 20\\%$: Uncertain zone; task-specific evaluation recommended.\n\\end{itemize}\n\nThe diagnostic achieves 85.7\\% classification accuracy with AUC = 0.82. The 25\\% failure rate at $C_0 > 20\\%$ (positive $C_0$ but no gap) corresponds to configurations where output diversity exists but constraint extraction quality is poor (e.g., Mistral's less structured traces). This identifies a second prerequisite beyond $C_0$: trace quality must support reliable constraint extraction.\n\n\\subsection{$K$ Sensitivity Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Sensitivity to number of sampled traces $K$ (Qwen2.5-14B, 60 questions).}\n\\label{tab:k_sensitivity}\n\\small\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n$K$ & SC Acc. & SICA Acc. & $\\Delta$ (pp) & $C_0$ & Tie Rate \\\\\n\\midrule\n6 & 70.0 & 71.7 & +1.7 & 0.40 & 15\\% \\\\\n8 & 70.0 & 73.3 & +3.3 & 0.47 & 22\\% \\\\\n12 & 70.0 & 73.3 & +3.3 & 0.53 & 25\\% \\\\\n16 & 71.7 & 75.0 & +3.3 & 0.57 & 18\\% \\\\\n20 & 73.3 & 75.0 & +1.7 & 0.60 & 13\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:k_sensitivity} reveals an inverted-U relationship between $K$ and SICA's advantage. While $C_0$ increases monotonically with $K$ (more samples $\\rightarrow$ more diversity), the SICA--SC gap peaks at $K = 8$--$12$ and decreases at larger $K$. This occurs because: at low $K$, ties are rare (SC often has a clear majority); at the sweet spot ($K = 8$--$12$), even values create more exact ties, giving SICA maximum leverage; at high $K$, the majority winner stabilizes (law of large numbers), reducing tie frequency despite higher $C_0$.\n\nThis pattern supports the ``principled tiebreaker'' narrative: SICA's value is mechanistically tied to tie frequency, not a general accuracy boost that scales with sampling budget. $K = 8$--$12$ is the practical recommendation.\n\n\\subsection{Overhead Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Computational overhead breakdown (Qwen2.5-14B, per question average).}\n\\label{tab:overhead}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStage & Time (s) & Fraction & Shared with SC? \\\\\n\\midrule\nGeneration ($K=12$ traces) & 48.3 & 81.7\\% & Yes \\\\\nConstraint Extraction & 8.4 & 14.2\\% & No \\\\\nMAX-SAT Solving & 2.4 & 4.1\\% & No \\\\\n\\midrule\nTotal & 59.1 & 100\\% & --- \\\\\nOverhead vs.\\ SC & +10.8 & +22.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA adds 22.4\\% overhead over pure SC, concentrated in constraint extraction (14.2\\%). MAX-SAT solving is negligible (4.1\\%). The generation cost (81.7\\%) is shared with SC. The overhead is modest for a research prototype; a dedicated smaller extraction model could reduce it to $<10\\%$. Importantly, this overhead is only worthwhile in the $C_0 > 20\\%$ regime --- the diagnostic allows practitioners to avoid paying the cost when SICA cannot help.\n\n\\subsection{Constraint Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation of the constraint aggregation mechanism (804 questions, Qwen2.5-14B).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Combined & FOLIO & $\\Delta$ vs.\\ SC (pp) \\\\\n\\midrule\nSICA (MAX-SAT) & 71.8 & 78.4 & +1.5 \\\\\nCount-only & 71.1 & 77.0 & +0.8 \\\\\nRandom-weight & 70.6 & --- & +0.3 \\\\\nSC (baseline) & 70.3 & 74.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMAX-SAT provides marginal accuracy gains over simpler alternatives (+0.7pp over count-only). The primary contribution of MAX-SAT is \\emph{interpretability}: satisfiability checking identifies which constraints are mutually consistent, enabling inspection of \\emph{why} SICA chose a particular answer. Count-only still outperforms SC (+0.8pp), confirming that the constraint-based framework itself (not just the solver) provides value. Random weighting destroys the informative signal. On FOLIO specifically, MAX-SAT shows a clearer advantage (+1.4pp over count-only) because formal-logic constraints have well-defined satisfiability structure.\n\n\\subsection{Constraint Quality Analysis}\n\nAnalysis of 8 representative cases from the expanded evaluation reveals:\n\\begin{itemize}\n    \\item 75\\% of extracted constraints are semantically meaningful (correctly capturing intended logical relationships).\n    \\item 83\\% of \\emph{excluded} constraints (those MAX-SAT deems unsatisfiable with the majority) correspond to actual reasoning errors in the source trace.\n    \\item Common constraint types: entailment chains, negations, universal quantifiers, conditionals, disjunctions (average 14.8 unique constraints per problem).\n    \\item Failure modes: over-literal parsing of hedging language, scope ambiguity in quantifiers, implicit premises missed.\n\\end{itemize}\n\nThe 83\\% error-detection rate validates MAX-SAT as genuinely detecting flawed reasoning rather than randomly excluding constraints. This supports SICA's role as an interpretable reasoning aggregator: even when accuracy gains are modest, the constraint analysis provides actionable diagnostic information about trace quality.\n\n\\subsection{Cross-Domain Validation: GSM8K}\n\nA pilot evaluation on 30 GSM8K questions with Qwen2.5-14B yields $C_0 = 10\\%$, SC accuracy 86.7\\%, and SICA--SC gap of 0pp. This confirms that $C_0$ reflects task-relative model confidence rather than answer-space properties: despite GSM8K's open numeric answer space, the model is sufficiently competent that traces converge, placing it in the uncertain zone ($5\\% < C_0 < 20\\%$). The result pre-empts the concern that SICA only applies to restricted answer spaces --- it naturally deactivates when unnecessary.\n\n\\section{Discussion}\n\n\\paragraph{When does symbolic consensus help?} Our results establish a clear picture: SICA helps when (1) output diversity exists ($C_0 > 20\\%$) and (2) constraint extraction is reliable ($\\geq 90\\%$ extraction rate). Condition (1) is satisfied by instruction-tuned models on challenging logic tasks but not by reasoning models or on tasks where the model is highly competent. Condition (2) depends on trace structure and model family.\n\n\\paragraph{Instruction vs.\\ reasoning models.} The stark $C_0$ contrast (instruction: 35--55\\%, reasoning: $<5\\%$) reveals a fundamental architectural difference. Reasoning models (QwQ, DeepSeek-R1) internalize extended self-correction that eliminates output diversity, while instruction models sample diversely at non-zero temperature. This has practical implications: SICA targets the cheaper, more widely deployed instruction models where SC's limitations are most pronounced.\n\n\\paragraph{Limitations.} (1) The expanded evaluation achieves only borderline significance on FOLIO ($p = 0.08$) and is not significant combined ($p = 0.19$); larger-scale evaluation is needed. (2) The 72B results use 4-bit AWQ quantization, which may slightly increase randomness versus full precision. (3) $C_0$ as a diagnostic has a 25\\% false positive rate ($C_0 > 20\\%$ but no SICA benefit), indicating that $C_0$ alone is necessary but not sufficient. (4) Constraint extraction quality varies across model families, limiting SICA's generality without family-specific tuning.\n\n\\section{Conclusion}\n\nWe presented SICA, a symbolic constraint-based approach to reasoning aggregation that provides principled tiebreaking for Self-Consistency. Our primary contribution is not the mechanism itself but the systematic characterization of its operating regime. The multi-candidate rate $C_0$ serves as a zero-cost binary diagnostic: $C_0 > 20\\%$ indicates SICA deployment is likely beneficial; $C_0 < 5\\%$ indicates it is unnecessary. This transforms the question from ``does symbolic consensus work?'' to ``when does symbolic consensus work?'' --- providing practitioners with actionable guidance for deployment decisions. Validated across 3 model families and 2 reasoning architectures, the $C_0$ framework establishes formally characterizable applicability boundaries for constraint-based reasoning aggregation.\n\n\\bibliographystyle{plain}\n\\begin{thebibliography}{10}\n\n\\bibitem{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem{chen2023universal}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv preprint arXiv:2311.17311}, 2023.\n\n\\bibitem{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Y. Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem{lyu2023faithful}\nQ.~Lyu, S.~Havaldar, A.~Stein, L.~Zhang, D.~Rao, E.~Wong, M.~Apidianaki, and C.~Callison-Burch.\n\\newblock Faithful Chain-of-Thought Reasoning.\n\\newblock In \\emph{IJCNLP-AACL}, 2023.\n\n\\bibitem{lakshminarayanan2017simple}\nB.~Lakshminarayanan, A.~Pritzel, and C.~Blundell.\n\\newblock Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem{han2022folio}\nS.~Han, H.~Schoelkopf, Y.~Zhao, Z.~Qi, M.~Riddell, L.~Benson, L.~Sun, E.~Zubatiy, Y.~Shi, M.~Yang, B.~O.~Huang, and D.~Radev.\n\\newblock FOLIO: Natural Language Reasoning with First-Order Logic.\n\\newblock \\emph{arXiv preprint arXiv:2209.00840}, 2022.\n\n\\bibitem{tafjord2021proofwriter}\nO.~Tafjord, B.~Dalvi, and P.~Clark.\n\\newblock ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\n\\newblock In \\emph{Findings of ACL}, 2021.\n\n\\end{thebibliography}\n\n\\appendix\n\n\\section{Full $C_0$ Diagnostic Data Points}\n\\label{app:c0_data}\n\nTable~\\ref{tab:c0_full} lists all 14 (model, dataset, $K$) configurations used for the $C_0$ diagnostic analysis.\n\n\\begin{table}[h]\n\\centering\n\\caption{All data points for $C_0$ vs.\\ SICA--SC gap analysis.}\n\\label{tab:c0_full}\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Dataset & $K$ & $C_0$ & Gap (pp) \\\\\n\\midrule\nQwen2.5-7B & D012 (60q) & 12 & 0.55 & +3.3 \\\\\nQwen2.5-14B & Combined (804q) & 12 & 0.42 & +1.5 \\\\\nQwen2.5-72B-AWQ & D012 (60q) & 12 & 0.37 & +1.6 \\\\\nMistral-7B & D012 (60q) & 12 & 0.35 & +1.6 \\\\\nLLaMA-3.1-8B & D012 (60q) & 12 & 0.40 & +3.4 \\\\\nQwQ-32B & Mixed (48q) & 12 & 0.036 & 0.0 \\\\\nDeepSeek-R1-LLaMA-8B & D012 (60q) & 12 & 0.05 & 0.0 \\\\\nGSM8K-14B & GSM8K (30q) & 12 & 0.10 & 0.0 \\\\\nQwen-14B $K{=}6$ & D012 (60q) & 6 & 0.40 & +1.7 \\\\\nQwen-14B $K{=}8$ & D012 (60q) & 8 & 0.47 & +3.3 \\\\\nQwen-14B $K{=}12$ & D012 (60q) & 12 & 0.53 & +3.3 \\\\\nQwen-14B $K{=}16$ & D012 (60q) & 16 & 0.57 & +3.3 \\\\\nQwen-14B $K{=}20$ & D012 (60q) & 20 & 0.60 & +1.7 \\\\\nQwen-14B FOLIO & FOLIO (204q) & 12 & 0.52 & +3.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{GSM8K Pilot Results}\n\\label{app:gsm8k}\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K pilot evaluation (Qwen2.5-14B, $K=12$, $T=0.7$, 30 questions).}\n\\label{tab:gsm8k}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSC Accuracy & 86.7\\% \\\\\nSICA Accuracy & 86.7\\% \\\\\n$C_0$ & 10\\% \\\\\nTie Cases & 0 \\\\\nConstraint Extraction Rate & 97\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b6ce02-0597-496d-befc-8f109d50a697",
  "isSidechain": false,
  "requestId": "req_011Cb6Hmwv5sMt7QXGZWNofy",
  "type": "assistant",
  "uuid": "7154d87a-5bfc-4757-9911-3225fb9cd68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5GVUSLLU4vP9nDq3hQNro",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 36119,
      "output_tokens": 9298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9298,
          "cache_read_input_tokens": 36119,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 19 · 2026-05-16T13:03:21.571Z_

<details><summary>↩ Tool result · `toolu_01QyAJ6pPGzAM6CUHc1pLzkc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7154d87a-5bfc-4757-9911-3225fb9cd68a",
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "2a9b9b54-ad4a-459a-ad90-c335949e7125",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{xcolor}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\n\\title{When Does Symbolic Consensus Help? \\\\ Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nSelf-Consistency (SC) aggregates multiple LLM reasoning paths via majority voting but discards the logical structure within traces and resorts to arbitrary rules when votes are tied. We propose SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from reasoning traces and resolves disagreements via weighted partial MAX-SAT. Rather than claiming uniform accuracy improvements, we systematically characterize \\emph{when} symbolic consensus adds value. We introduce the multi-candidate rate $C_0$ --- the fraction of questions producing multiple distinct answers across $K$ sampled traces --- as a zero-cost diagnostic of effective output diversity. Through experiments spanning 3 instruction-model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and 2 formal-logic benchmarks (FOLIO, ProofWriter), we establish: (1) SICA provides principled, interpretable tiebreaking with a 64.7\\% win rate on ties ($p=0.035$ vs.\\ random) and a positive accuracy trend on formal-logic domains; (2) the $C_0$ operating regime governs SICA effectiveness --- instruction models exhibit $C_0 > 20\\%$ and benefit from SICA, while reasoning models show $C_0 < 5\\%$ where SICA degenerates to SC; (3) $C_0$ functions as a binary deployment diagnostic ($C_0 > 20\\% \\Rightarrow$ try SICA; $C_0 < 5\\% \\Rightarrow$ skip) with 85.7\\% classification accuracy. Our analysis reframes symbolic consensus from ``yet another ensemble method'' into a method with formally characterizable applicability boundaries.\n\\end{abstract}\n\n\\section{Introduction}\n\nLarge language models solve reasoning tasks more reliably when multiple reasoning paths are sampled and aggregated. Self-Consistency \\cite{wang2023selfconsistency} established majority voting over diverse chain-of-thought traces as a simple and effective strategy. However, SC treats each trace as an opaque vote, discarding the logical structure within. When votes are tied --- a common occurrence with even-$K$ sampling or narrow answer margins --- SC falls back to arbitrary rules (alphabetical order, first-seen, or random selection) with no principled resolution mechanism.\n\nWe propose SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to identify the answer most consistent with the collective reasoning. Rather than positioning SICA as a uniform accuracy improvement over SC, we ask a more fundamental question: \\emph{when does symbolic consensus help?}\n\nOur primary contribution is characterizing the \\textbf{operating regime} of symbolic consensus through the lens of trace diversity. We define the multi-candidate rate $C_0$ as the fraction of questions that produce multiple distinct candidate answers across $K$ sampled traces. $C_0$ reflects effective output diversity --- a proxy for task-relative model confidence. Our key finding is that $C_0$ governs SICA's effectiveness:\n\n\\begin{itemize}\n    \\item When $C_0 > 20\\%$ (instruction models on challenging logic tasks), traces disagree frequently, creating opportunities for principled tiebreaking. SICA wins 64.7\\% of tie cases ($p=0.035$) and shows positive accuracy trends.\n    \\item When $C_0 < 5\\%$ (reasoning models universally), traces are self-consistent. SICA degenerates to SC structurally --- there is no disagreement to resolve.\n\\end{itemize}\n\nThis pattern holds across 3 instruction-model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B), establishing that the operating regime is determined by model \\emph{class} (instruction vs.\\ reasoning), not model family or task domain.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item A principled interpretable tiebreaking mechanism for SC that achieves statistically significant per-tie advantage ($p=0.035$) with positive accuracy trends on formal-logic domains (+3.9pp on FOLIO, $p=0.08$).\n    \\item Systematic characterization of the $C_0$ operating regime across 7 model configurations, revealing that instruction-tuned models exhibit high $C_0$ universally while reasoning models show near-zero $C_0$.\n    \\item Validation of $C_0$ as a practical binary deployment diagnostic (AUC=0.82, accuracy=85.7\\%) that enables practitioners to decide whether SICA deployment is worthwhile without running full symbolic analysis.\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and Variants.} Wang et al.\\ (2023) introduced Self-Consistency, using majority voting over diverse reasoning paths. Universal Self-Consistency (Chen et al., 2023) extends SC to open-ended generation. Both methods treat traces as opaque votes and offer no mechanism for tie resolution or constraint-based reasoning. Our work complements SC by adding a principled aggregation layer that activates precisely when voting is insufficient.\n\n\\paragraph{Symbolic Reasoning with LLMs.} Recent work integrates symbolic solvers with neural generation: Logic-LM (Pan et al., 2023) translates problems to formal logic before solving, while Faithful CoT (Lyu et al., 2023) generates symbolic representations alongside natural language chains. Unlike these single-trace approaches, SICA operates \\emph{post-hoc} on multiple traces, requiring no modification to the generation process.\n\n\\paragraph{Ensemble Uncertainty.} Lakshminarayanan et al.\\ (2017) established deep ensemble disagreement as an uncertainty signal. Our $C_0$ metric is analogous --- measuring effective output diversity across sampled LLM traces --- but we use it prescriptively (to predict method applicability) rather than solely for uncertainty estimation.\n\n\\section{Method}\n\n\\subsection{Problem Setup}\n\nGiven a reasoning problem $q$, we sample $K$ reasoning traces $\\{t_1, \\ldots, t_K\\}$ from a language model at temperature $T$. Each trace produces a candidate answer $a_i$. Self-Consistency selects $\\hat{a}_{SC} = \\arg\\max_a \\sum_{i=1}^K \\mathbb{1}[a_i = a]$.\n\n\\subsection{SICA Pipeline}\n\nSICA augments SC with three additional stages:\n\n\\paragraph{Step 1: Constraint Extraction.} For each trace $t_i$, we extract a set of first-order logic constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ using the same LLM with a structured extraction prompt. Each constraint captures a logical relationship asserted in the reasoning (entailment chains, negations, universal quantifiers, conditionals, disjunctions). Across all traces, we collect $\\mathcal{C} = \\bigcup_i \\mathcal{C}_i$.\n\n\\paragraph{Step 2: Weighted Partial MAX-SAT.} We formulate answer selection as a weighted partial MAX-SAT problem. For each candidate answer $a$, we compute:\n\\begin{equation}\n    \\text{score}(a) = \\text{MAX-SAT}(\\mathcal{C}_a, w)\n\\end{equation}\nwhere $\\mathcal{C}_a \\subseteq \\mathcal{C}$ are constraints consistent with answer $a$, and weights $w$ reflect constraint frequency across traces. The solver (Z3) maximizes the total weight of satisfiable constraints, identifying the answer supported by the most coherent set of reasoning.\n\n\\paragraph{Step 3: Answer Selection.} SICA selects:\n\\begin{equation}\n    \\hat{a}_{SICA} = \\arg\\max_a \\text{score}(a)\n\\end{equation}\n\nWhen SC has a clear majority and no ties exist, SICA typically agrees with SC. The mechanism primarily activates on tie cases and near-ties where constraint quality distinguishes candidates.\n\n\\subsection{Multi-Candidate Rate ($C_0$)}\n\nWe define the multi-candidate rate as:\n\\begin{equation}\n    C_0 = \\frac{1}{N} \\sum_{j=1}^N \\mathbb{1}\\left[|\\{a_i^{(j)}\\}_{i=1}^K| > 1\\right]\n\\end{equation}\nwhere $N$ is the number of questions and $|\\{a_i^{(j)}\\}_{i=1}^K|$ counts distinct answers produced for question $j$. $C_0$ measures the fraction of questions exhibiting any output diversity --- a necessary condition for SICA to intervene.\n\n\\section{Experimental Setup}\n\n\\subsection{Benchmarks}\n\\begin{itemize}\n    \\item \\textbf{FOLIO} (Han et al., 2022): 204 natural language inference problems requiring first-order logic reasoning. 3-class classification (True/False/Unknown). Open-world semantics.\n    \\item \\textbf{ProofWriter} (Tafjord et al., 2021): 600 depth-5 deductive reasoning problems. Binary classification (True/False). Closed-world semantics.\n\\end{itemize}\n\n\\subsection{Models}\nWe evaluate 7 model configurations spanning 3 instruction families and 2 reasoning architectures:\n\\begin{itemize}\n    \\item \\textbf{Instruction models}: Qwen2.5-7B/14B/72B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct\n    \\item \\textbf{Reasoning models}: QwQ-32B, DeepSeek-R1-Distill-LLaMA-8B\n\\end{itemize}\n\n\\subsection{Configuration}\nAll experiments use $K=12$ sampled traces at temperature $T=0.7$ unless otherwise noted. Constraint extraction uses the same model that generated the traces. MAX-SAT solving uses Z3. The expanded evaluation (804 questions) uses Qwen2.5-14B-Instruct; cross-model experiments use the 60-question subset (30 FOLIO + 30 ProofWriter from the D0+D1+D2 split).\n\n\\section{Results}\n\n\\subsection{Main Results: Operating Regime Characterization}\n\nTable~\\ref{tab:main} presents accuracy across all model configurations. The central finding is the stark contrast between instruction and reasoning models in terms of $C_0$ and SICA effectiveness.\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results across model configurations ($K=12$, $T=0.7$). $C_0$: multi-candidate rate. $\\Delta$: SICA$-$SC gap in percentage points. Instruction models (top) show $C_0 > 20\\%$ with positive trends; reasoning models (bottom) show $C_0 < 5\\%$ with zero gap.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\n\\multirow{2}{*}{Model} & \\multirow{2}{*}{$C_0$} & \\multicolumn{2}{c}{FOLIO} & \\multicolumn{2}{c}{ProofWriter} & \\multicolumn{2}{c}{Combined} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8}\n & & SC & SICA & SC & SICA & SC & SICA \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Instruction Models ($C_0 > 20\\%$)}} \\\\\n\\midrule\nQwen2.5-7B & 0.55 & 63.3 & 70.0 & 60.7 & 61.9 & 61.7 & 65.0 \\\\\nQwen2.5-14B$^\\dagger$ & 0.42 & 74.5 & 78.4 & 68.9 & 69.5 & 70.3 & 71.8 \\\\\nQwen2.5-72B-AWQ & 0.37 & 83.3 & 86.7 & 73.8 & 73.8 & 76.7 & 78.3 \\\\\nMistral-7B & 0.35 & 56.7 & 60.0 & 57.1 & 57.1 & 56.7 & 58.3 \\\\\nLLaMA-3.1-8B & 0.40 & 60.0 & 66.7 & 57.1 & 58.3 & 58.3 & 61.7 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Reasoning Models ($C_0 < 5\\%$)}} \\\\\n\\midrule\nQwQ-32B & 0.036 & --- & --- & --- & --- & --- & --- \\\\\nDeepSeek-R1-LLaMA-8B & 0.05 & 70.0 & 70.0 & 66.7 & 66.7 & 68.3 & 68.3 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize $^\\dagger$ Expanded evaluation: 204 FOLIO + 600 ProofWriter = 804 questions. Others: 60 questions.} \\\\\n\\multicolumn{8}{l}{\\footnotesize QwQ-32B: all gaps = 0.0pp across 48 questions (22 AIME + 16 PW + 10 FOLIO).} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Key observations.} All five instruction models show $C_0 > 35\\%$, indicating substantial output diversity. All show non-negative SICA--SC gaps, with the strongest effects on FOLIO (open-world NLI). Both reasoning models show $C_0 < 5\\%$, with SICA $\\equiv$ SC structurally (zero ties, zero gap). The contrast is particularly striking for the LLaMA architecture pair: LLaMA-3.1-8B-Instruct ($C_0 = 40\\%$, $\\Delta = +3.4$pp) versus DeepSeek-R1-Distill-LLaMA-8B ($C_0 = 5\\%$, $\\Delta = 0$pp) --- same base architecture, different training paradigm, opposite SICA behavior.\n\n\\paragraph{Within-family scaling (Qwen).} $C_0$ decreases with scale: 7B (0.55) $>$ 14B (0.42) $>$ 72B (0.37). The SICA--SC gap shows a corresponding directional decrease, though the gradient is noisy (7B and 14B show similar gaps). Stronger instruction models approach but do not reach the reasoning model's degenerate regime ($C_0 < 5\\%$).\n\n\\paragraph{Cross-family validation.} All three instruction-model families confirm $C_0 > 20\\%$. Two of three (Qwen, LLaMA) show clear positive SICA--SC gaps; Mistral shows a directional but smaller improvement (+1.6pp). The difference is attributable to constraint extraction quality: Mistral's less structured traces yield 85\\% extraction rate versus 93--100\\% for Qwen and LLaMA.\n\n\\subsection{Tiebreak Analysis}\n\nTable~\\ref{tab:tiebreak} isolates SICA's performance specifically on tie cases --- questions where SC has no clear majority winner.\n\n\\begin{table}[t]\n\\centering\n\\caption{Tiebreak analysis on the expanded 804-question evaluation (Qwen2.5-14B). SICA is compared against alternative tiebreaking strategies applied only to tie cases.}\n\\label{tab:tiebreak}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nTiebreak Strategy & Accuracy on Ties & Win Rate & $p$-value (vs.\\ Random) \\\\\n\\midrule\nSICA (MAX-SAT) & 64.7\\% & 44/68 & 0.035 \\\\\nRandom & 48.5\\% & --- & --- \\\\\nAlphabetical & 52.9\\% & --- & --- \\\\\nFirst-seen & 45.6\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA achieves a 64.7\\% win rate on 68 tie cases, significantly outperforming random tiebreaking ($p = 0.035$). This is the paper's cleanest statistical result: on cases where SC provides no signal, symbolic constraint analysis correctly resolves the tie nearly two-thirds of the time. The overall accuracy contribution of better tiebreaking is modest ($\\sim$0.8pp over a fair random baseline), but the per-tie advantage is meaningful and, critically, \\emph{interpretable} --- practitioners can inspect which constraints led to SICA's decision.\n\n\\subsection{Expanded Evaluation (804 Questions)}\n\nOn the full 804-question evaluation with Qwen2.5-14B:\n\\begin{itemize}\n    \\item Combined: SICA 71.8\\% vs.\\ SC 70.3\\% (+1.5pp, bootstrap $p = 0.19$)\n    \\item FOLIO (204 questions): SICA 78.4\\% vs.\\ SC 74.5\\% (+3.9pp, $p = 0.08$)\n    \\item ProofWriter (600 questions): SICA 69.5\\% vs.\\ SC 68.9\\% (+0.6pp, $p = 0.38$)\n\\end{itemize}\n\nThe FOLIO result trends toward significance ($p = 0.08$) and represents the strongest evidence for SICA's value on formal-logic domains with open-world semantics. ProofWriter's closed-world reasoning produces less diverse traces (lower per-question $C_0$), yielding a negligible gap. The combined result is diluted by ProofWriter's 600-question mass. We note that the per-tie significance ($p = 0.035$) provides cleaner statistical support for SICA's mechanism than the overall accuracy comparison.\n\n\\subsection{$C_0$ as Binary Deployment Diagnostic}\n\n\\begin{table}[t]\n\\centering\n\\caption{$C_0$ diagnostic performance across 14 (model, dataset, $K$) configurations.}\n\\label{tab:diagnostic}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nData points & 14 \\\\\nPearson $r$ ($C_0$ vs.\\ gap) & 0.58 \\\\\nSpearman $\\rho$ & 0.64 \\\\\nBinary threshold ($C_0 = 20\\%$) precision & 0.75 \\\\\nBinary threshold ($C_0 = 20\\%$) recall & 1.00 \\\\\n$C_0 < 5\\%$ $\\Rightarrow$ gap $= 0$ & 100\\% \\\\\n$C_0 > 20\\%$ $\\Rightarrow$ gap $> 0$ & 75\\% \\\\\nBinary classification accuracy & 85.7\\% \\\\\nAUC-ROC & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe evaluate $C_0$ as a \\emph{binary} diagnostic rather than a continuous predictor (the scatter has too much variance for reliable regression). The practical rule is:\n\n\\begin{itemize}\n    \\item $C_0 > 20\\%$: Deploy SICA (positive gap in 75\\% of configurations).\n    \\item $C_0 < 5\\%$: Skip SICA (gap $= 0$ in 100\\% of configurations).\n    \\item $5\\% < C_0 < 20\\%$: Uncertain zone; task-specific evaluation recommended.\n\\end{itemize}\n\nThe diagnostic achieves 85.7\\% classification accuracy with AUC = 0.82. The 25\\% failure rate at $C_0 > 20\\%$ (positive $C_0$ but no gap) corresponds to configurations where output diversity exists but constraint extraction quality is poor (e.g., Mistral's less structured traces). This identifies a second prerequisite beyond $C_0$: trace quality must support reliable constraint extraction.\n\n\\subsection{$K$ Sensitivity Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Sensitivity to number of sampled traces $K$ (Qwen2.5-14B, 60 questions).}\n\\label{tab:k_sensitivity}\n\\small\n\\begin{tabular}{@{}cccccc@{}}\n\\toprule\n$K$ & SC Acc. & SICA Acc. & $\\Delta$ (pp) & $C_0$ & Tie Rate \\\\\n\\midrule\n6 & 70.0 & 71.7 & +1.7 & 0.40 & 15\\% \\\\\n8 & 70.0 & 73.3 & +3.3 & 0.47 & 22\\% \\\\\n12 & 70.0 & 73.3 & +3.3 & 0.53 & 25\\% \\\\\n16 & 71.7 & 75.0 & +3.3 & 0.57 & 18\\% \\\\\n20 & 73.3 & 75.0 & +1.7 & 0.60 & 13\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:k_sensitivity} reveals an inverted-U relationship between $K$ and SICA's advantage. While $C_0$ increases monotonically with $K$ (more samples $\\rightarrow$ more diversity), the SICA--SC gap peaks at $K = 8$--$12$ and decreases at larger $K$. This occurs because: at low $K$, ties are rare (SC often has a clear majority); at the sweet spot ($K = 8$--$12$), even values create more exact ties, giving SICA maximum leverage; at high $K$, the majority winner stabilizes (law of large numbers), reducing tie frequency despite higher $C_0$.\n\nThis pattern supports the ``principled tiebreaker'' narrative: SICA's value is mechanistically tied to tie frequency, not a general accuracy boost that scales with sampling budget. $K = 8$--$12$ is the practical recommendation.\n\n\\subsection{Overhead Analysis}\n\n\\begin{table}[t]\n\\centering\n\\caption{Computational overhead breakdown (Qwen2.5-14B, per question average).}\n\\label{tab:overhead}\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStage & Time (s) & Fraction & Shared with SC? \\\\\n\\midrule\nGeneration ($K=12$ traces) & 48.3 & 81.7\\% & Yes \\\\\nConstraint Extraction & 8.4 & 14.2\\% & No \\\\\nMAX-SAT Solving & 2.4 & 4.1\\% & No \\\\\n\\midrule\nTotal & 59.1 & 100\\% & --- \\\\\nOverhead vs.\\ SC & +10.8 & +22.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSICA adds 22.4\\% overhead over pure SC, concentrated in constraint extraction (14.2\\%). MAX-SAT solving is negligible (4.1\\%). The generation cost (81.7\\%) is shared with SC. The overhead is modest for a research prototype; a dedicated smaller extraction model could reduce it to $<10\\%$. Importantly, this overhead is only worthwhile in the $C_0 > 20\\%$ regime --- the diagnostic allows practitioners to avoid paying the cost when SICA cannot help.\n\n\\subsection{Constraint Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation of the constraint aggregation mechanism (804 questions, Qwen2.5-14B).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Combined & FOLIO & $\\Delta$ vs.\\ SC (pp) \\\\\n\\midrule\nSICA (MAX-SAT) & 71.8 & 78.4 & +1.5 \\\\\nCount-only & 71.1 & 77.0 & +0.8 \\\\\nRandom-weight & 70.6 & --- & +0.3 \\\\\nSC (baseline) & 70.3 & 74.5 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMAX-SAT provides marginal accuracy gains over simpler alternatives (+0.7pp over count-only). The primary contribution of MAX-SAT is \\emph{interpretability}: satisfiability checking identifies which constraints are mutually consistent, enabling inspection of \\emph{why} SICA chose a particular answer. Count-only still outperforms SC (+0.8pp), confirming that the constraint-based framework itself (not just the solver) provides value. Random weighting destroys the informative signal. On FOLIO specifically, MAX-SAT shows a clearer advantage (+1.4pp over count-only) because formal-logic constraints have well-defined satisfiability structure.\n\n\\subsection{Constraint Quality Analysis}\n\nAnalysis of 8 representative cases from the expanded evaluation reveals:\n\\begin{itemize}\n    \\item 75\\% of extracted constraints are semantically meaningful (correctly capturing intended logical relationships).\n    \\item 83\\% of \\emph{excluded} constraints (those MAX-SAT deems unsatisfiable with the majority) correspond to actual reasoning errors in the source trace.\n    \\item Common constraint types: entailment chains, negations, universal quantifiers, conditionals, disjunctions (average 14.8 unique constraints per problem).\n    \\item Failure modes: over-literal parsing of hedging language, scope ambiguity in quantifiers, implicit premises missed.\n\\end{itemize}\n\nThe 83\\% error-detection rate validates MAX-SAT as genuinely detecting flawed reasoning rather than randomly excluding constraints. This supports SICA's role as an interpretable reasoning aggregator: even when accuracy gains are modest, the constraint analysis provides actionable diagnostic information about trace quality.\n\n\\subsection{Cross-Domain Validation: GSM8K}\n\nA pilot evaluation on 30 GSM8K questions with Qwen2.5-14B yields $C_0 = 10\\%$, SC accuracy 86.7\\%, and SICA--SC gap of 0pp. This confirms that $C_0$ reflects task-relative model confidence rather than answer-space properties: despite GSM8K's open numeric answer space, the model is sufficiently competent that traces converge, placing it in the uncertain zone ($5\\% < C_0 < 20\\%$). The result pre-empts the concern that SICA only applies to restricted answer spaces --- it naturally deactivates when unnecessary.\n\n\\section{Discussion}\n\n\\paragraph{When does symbolic consensus help?} Our results establish a clear picture: SICA helps when (1) output diversity exists ($C_0 > 20\\%$) and (2) constraint extraction is reliable ($\\geq 90\\%$ extraction rate). Condition (1) is satisfied by instruction-tuned models on challenging logic tasks but not by reasoning models or on tasks where the model is highly competent. Condition (2) depends on trace structure and model family.\n\n\\paragraph{Instruction vs.\\ reasoning models.} The stark $C_0$ contrast (instruction: 35--55\\%, reasoning: $<5\\%$) reveals a fundamental architectural difference. Reasoning models (QwQ, DeepSeek-R1) internalize extended self-correction that eliminates output diversity, while instruction models sample diversely at non-zero temperature. This has practical implications: SICA targets the cheaper, more widely deployed instruction models where SC's limitations are most pronounced.\n\n\\paragraph{Limitations.} (1) The expanded evaluation achieves only borderline significance on FOLIO ($p = 0.08$) and is not significant combined ($p = 0.19$); larger-scale evaluation is needed. (2) The 72B results use 4-bit AWQ quantization, which may slightly increase randomness versus full precision. (3) $C_0$ as a diagnostic has a 25\\% false positive rate ($C_0 > 20\\%$ but no SICA benefit), indicating that $C_0$ alone is necessary but not sufficient. (4) Constraint extraction quality varies across model families, limiting SICA's generality without family-specific tuning.\n\n\\section{Conclusion}\n\nWe presented SICA, a symbolic constraint-based approach to reasoning aggregation that provides principled tiebreaking for Self-Consistency. Our primary contribution is not the mechanism itself but the systematic characterization of its operating regime. The multi-candidate rate $C_0$ serves as a zero-cost binary diagnostic: $C_0 > 20\\%$ indicates SICA deployment is likely beneficial; $C_0 < 5\\%$ indicates it is unnecessary. This transforms the question from ``does symbolic consensus work?'' to ``when does symbolic consensus work?'' --- providing practitioners with actionable guidance for deployment decisions. Validated across 3 model families and 2 reasoning architectures, the $C_0$ framework establishes formally characterizable applicability boundaries for constraint-based reasoning aggregation.\n\n\\bibliographystyle{plain}\n\\begin{thebibliography}{10}\n\n\\bibitem{wang2023selfconsistency}\nX.~Wang, J.~Wei, D.~Schuurmans, Q.~Le, E.~Chi, S.~Narang, A.~Chowdhery, and D.~Zhou.\n\\newblock Self-Consistency Improves Chain of Thought Reasoning in Language Models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem{chen2023universal}\nX.~Chen, R.~Aksitov, U.~Alon, J.~Ren, K.~Xiao, P.~Yin, S.~Prakash, C.~Sutton, X.~Wang, and D.~Zhou.\n\\newblock Universal Self-Consistency for Large Language Model Generation.\n\\newblock \\emph{arXiv preprint arXiv:2311.17311}, 2023.\n\n\\bibitem{pan2023logiclm}\nL.~Pan, A.~Albalak, X.~Wang, and W.~Y. Wang.\n\\newblock Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning.\n\\newblock In \\emph{Findings of EMNLP}, 2023.\n\n\\bibitem{lyu2023faithful}\nQ.~Lyu, S.~Havaldar, A.~Stein, L.~Zhang, D.~Rao, E.~Wong, M.~Apidianaki, and C.~Callison-Burch.\n\\newblock Faithful Chain-of-Thought Reasoning.\n\\newblock In \\emph{IJCNLP-AACL}, 2023.\n\n\\bibitem{lakshminarayanan2017simple}\nB.~Lakshminarayanan, A.~Pritzel, and C.~Blundell.\n\\newblock Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem{han2022folio}\nS.~Han, H.~Schoelkopf, Y.~Zhao, Z.~Qi, M.~Riddell, L.~Benson, L.~Sun, E.~Zubatiy, Y.~Shi, M.~Yang, B.~O.~Huang, and D.~Radev.\n\\newblock FOLIO: Natural Language Reasoning with First-Order Logic.\n\\newblock \\emph{arXiv preprint arXiv:2209.00840}, 2022.\n\n\\bibitem{tafjord2021proofwriter}\nO.~Tafjord, B.~Dalvi, and P.~Clark.\n\\newblock ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language.\n\\newblock In \\emph{Findings of ACL}, 2021.\n\n\\end{thebibliography}\n\n\\appendix\n\n\\section{Full $C_0$ Diagnostic Data Points}\n\\label{app:c0_data}\n\nTable~\\ref{tab:c0_full} lists all 14 (model, dataset, $K$) configurations used for the $C_0$ diagnostic analysis.\n\n\\begin{table}[h]\n\\centering\n\\caption{All data points for $C_0$ vs.\\ SICA--SC gap analysis.}\n\\label{tab:c0_full}\n\\small\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nModel & Dataset & $K$ & $C_0$ & Gap (pp) \\\\\n\\midrule\nQwen2.5-7B & D012 (60q) & 12 & 0.55 & +3.3 \\\\\nQwen2.5-14B & Combined (804q) & 12 & 0.42 & +1.5 \\\\\nQwen2.5-72B-AWQ & D012 (60q) & 12 & 0.37 & +1.6 \\\\\nMistral-7B & D012 (60q) & 12 & 0.35 & +1.6 \\\\\nLLaMA-3.1-8B & D012 (60q) & 12 & 0.40 & +3.4 \\\\\nQwQ-32B & Mixed (48q) & 12 & 0.036 & 0.0 \\\\\nDeepSeek-R1-LLaMA-8B & D012 (60q) & 12 & 0.05 & 0.0 \\\\\nGSM8K-14B & GSM8K (30q) & 12 & 0.10 & 0.0 \\\\\nQwen-14B $K{=}6$ & D012 (60q) & 6 & 0.40 & +1.7 \\\\\nQwen-14B $K{=}8$ & D012 (60q) & 8 & 0.47 & +3.3 \\\\\nQwen-14B $K{=}12$ & D012 (60q) & 12 & 0.53 & +3.3 \\\\\nQwen-14B $K{=}16$ & D012 (60q) & 16 & 0.57 & +3.3 \\\\\nQwen-14B $K{=}20$ & D012 (60q) & 20 & 0.60 & +1.7 \\\\\nQwen-14B FOLIO & FOLIO (204q) & 12 & 0.52 & +3.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{GSM8K Pilot Results}\n\\label{app:gsm8k}\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K pilot evaluation (Qwen2.5-14B, $K=12$, $T=0.7$, 30 questions).}\n\\label{tab:gsm8k}\n\\small\n\\begin{tabular}{@{}lc@{}}\n\\toprule\nMetric & Value \\\\\n\\midrule\nSC Accuracy & 86.7\\% \\\\\nSICA Accuracy & 86.7\\% \\\\\n$C_0$ & 10\\% \\\\\nTie Cases & 0 \\\\\nConstraint Extraction Rate & 97\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "7154d87a-5bfc-4757-9911-3225fb9cd68a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_c…",
  "leafUuid": "2a9b9b54-ad4a-459a-ad90-c335949e7125",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on symbolic consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Tool call

_source line 22 · 2026-05-16T13:03:25.640Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KsvDePLHkJtKhUKyxaFJJ9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper (two passes)",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a9b9b54-ad4a-459a-ad90-c335949e7125",
  "isSidechain": false,
  "requestId": "req_011Cb6HzTe6AzFBjzPQuavzx",
  "type": "assistant",
  "uuid": "0a589585-5b52-4c64-8ffd-5379924439ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcFGZqFrgA6vY4Dapp1gUa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9365,
      "cache_read_input_tokens": 36805,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9365,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 36805,
          "cache_creation_input_tokens": 9365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9365
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

_source line 23 · 2026-05-16T13:03:26.709Z_

<details><summary>↩ Tool result · `toolu_01KsvDePLHkJtKhUKyxaFJJ9`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty
(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)
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

LaTeX Warning: Citation `wang2023selfconsistency' on page 1 undefined on input 
line 28.


Overfull \hbox (3.46445pt too wide) in paragraph at lines 32--33
[]\OT1/cmr/m/n/10.95 Our pri-mary con-tri-bu-tion is char-ac-ter-iz-ing the \OT
1/cmr/bx/n/10.95 op-er-at-ing regime \OT1/cmr/m/n/10.95 of sym-bolic con-sen-su
s through
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.

[3]

LaTeX Warning: Reference `tab:main' on page 4 undefined on input line 111.

[4
pdfTeX warning (ext4): destination with the same identifier (name{table.1}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.145 
      ]

LaTeX Warning: Reference `tab:tiebreak' on page 5 undefined on input line 150.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 182.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 182.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 182.

[5
pdfTeX warning (ext4): destination with the same identifier (name{table.2}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.210     \item $
                 C_0 < 5\%$: Skip SICA (gap $= 0$ in 100\% of configurations).]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 216.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 216.


LaTeX Warning: Reference `tab:k_sensitivity' on page 6 undefined on input line 
236.

[6
pdfTeX warning (ext4): destination with the same identifier (name{table.3}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.259 \end{table}
                 
pdfTeX warning (ext4): destination with the same identifier (name{table.4}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.259 \end{table}
                 ] [7
pdfTeX warning (ext4): destination with the same identifier (name{table.5}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.295 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.6}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.295 
      ] [8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 354.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 354.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 354.


LaTeX Warning: Reference `tab:c0_full' on page 9 undefined on input line 357.


LaTeX Warning: `h' float specifier changed to `ht'.

[9
pdfTeX warning (ext4): destination with the same identifier (name{table.7}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.407 \end{document}
                    ] [10
pdfTeX warning (ext4): destination with the same identifier (name{table.8}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.407 \end{document}
                    ] (./paper.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy
mbols/msbm10.pfb>
Output written on paper.pdf (10 pages, 246376 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty
(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)
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
Overfull \hbox (3.46445pt too wide) in paragraph at lines 32--33
[]\OT1/cmr/m/n/10.95 Our pri-mary con-tri-bu-tion is char-ac-ter-iz-ing the \OT
1/cmr/bx/n/10.95 op-er-at-ing regime \OT1/cmr/m/n/10.95 of sym-bolic con-sen-su
s through
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 81.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 81.

[3] [4
pdfTeX warning (ext4): destination with the same identifier (name{table.1}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.145 
      ]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 182.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 182.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 182.

[5
pdfTeX warning (ext4): destination with the same identifier (name{table.2}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.210     \item $
                 C_0 < 5\%$: Skip SICA (gap $= 0$ in 100\% of configurations).]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 216.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 216.

[6
pdfTeX warning (ext4): destination with the same identifier (name{table.3}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.259 \end{table}
                 
pdfTeX warning (ext4): destination with the same identifier (name{table.4}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.259 \end{table}
                 ] [7
pdfTeX warning (ext4): destination with the same identifier (name{table.5}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.295 
      
pdfTeX warning (ext4): destination with the same identifier (name{table.6}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.295 
      ] [8]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 354.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 354.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 354.


LaTeX Warning: `h' float specifier changed to `ht'.

[9
pdfTeX warning (ext4): destination with the same identifier (name{table.7}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.407 \end{document}
                    ] [10
pdfTeX warning (ext4): destination with the same identifier (name{table.8}) has
 been already used, duplicate ignored
&lt;argument> ...shipout:D \box_use:N \l_shipout_box 
                                                  \__shipout_drop_firstpage_...
l.407 \end{document}
                    ] (./paper.aux) )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy
mbols/msbm10.pfb>
Output written on paper.pdf (10 pages, 248432 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a589585-5b52-4c64-8ffd-5379924439ea",
  "isSidechain": false,
  "promptId": "24095bc1-6adf-4b23-ac81-ac17a8cfac86",
  "type": "user",
  "uuid": "114afe0d-e72b-49ce-9ea4-60355c32c2d4",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nLaTeX Warning: Citation `wang2023selfconsistency' on page 1 undefined on input \nline 28.\n\n\nOverfull \\hbox (3.46445pt too wide) in paragraph at lines 32--33\n[]\\OT1/cmr/m/n/10.95 Our pri-mary con-tri-bu-tion is char-ac-ter-iz-ing the \\OT\n1/cmr/bx/n/10.95 op-er-at-ing regime \\OT1/cmr/m/n/10.95 of sym-bolic con-sen-su\ns through\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n[3]\n\nLaTeX Warning: Reference `tab:main' on page 4 undefined on input line 111.\n\n[4\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.145 \n      ]\n\nLaTeX Warning: Reference `tab:tiebreak' on page 5 undefined on input line 150.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 182.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 182.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 182.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.210     \\item $\n                 C_0 < 5\\%$: Skip SICA (gap $= 0$ in 100\\% of configurations).]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 216.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 216.\n\n\nLaTeX Warning: Reference `tab:k_sensitivity' on page 6 undefined on input line \n236.\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.259 \\end{table}\n                 \npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.259 \\end{table}\n                 ] [7\npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.295 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.295 \n      ] [8]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 354.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 354.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 354.\n\n\nLaTeX Warning: Reference `tab:c0_full' on page 9 undefined on input line 357.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9\npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.407 \\end{document}\n                    ] [10\npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.407 \\end{document}\n                    ] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy\nmbols/msbm10.pfb>\nOutput written on paper.pdf (10 pages, 246376 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithm.sty\n(/usr/share/texlive/texmf-dist/tex/latex/float/float.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ifthen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/algorithms/algorithmic.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (3.46445pt too wide) in paragraph at lines 32--33\n[]\\OT1/cmr/m/n/10.95 Our pri-mary con-tri-bu-tion is char-ac-ter-iz-ing the \\OT\n1/cmr/bx/n/10.95 op-er-at-ing regime \\OT1/cmr/m/n/10.95 of sym-bolic con-sen-su\ns through\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 81.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 81.\n\n[3] [4\npdfTeX warning (ext4): destination with the same identifier (name{table.1}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.145 \n      ]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 182.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 182.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 182.\n\n[5\npdfTeX warning (ext4): destination with the same identifier (name{table.2}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.210     \\item $\n                 C_0 < 5\\%$: Skip SICA (gap $= 0$ in 100\\% of configurations).]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 216.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 216.\n\n[6\npdfTeX warning (ext4): destination with the same identifier (name{table.3}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.259 \\end{table}\n                 \npdfTeX warning (ext4): destination with the same identifier (name{table.4}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.259 \\end{table}\n                 ] [7\npdfTeX warning (ext4): destination with the same identifier (name{table.5}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.295 \n      \npdfTeX warning (ext4): destination with the same identifier (name{table.6}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.295 \n      ] [8]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 354.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 354.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 354.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[9\npdfTeX warning (ext4): destination with the same identifier (name{table.7}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.407 \\end{document}\n                    ] [10\npdfTeX warning (ext4): destination with the same identifier (name{table.8}) has\n been already used, duplicate ignored\n&lt;argument> ...shipout:D \\box_use:N \\l_shipout_box \n                                                  \\__shipout_drop_firstpage_...\nl.407 \\end{document}\n                    ] (./paper.aux) )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/sy\nmbols/msbm10.pfb>\nOutput written on paper.pdf (10 pages, 248432 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0a589585-5b52-4c64-8ffd-5379924439ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_c…",
  "leafUuid": "114afe0d-e72b-49ce-9ea4-60355c32c2d4",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on symbolic consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Assistant

_source line 26 · 2026-05-16T13:03:34.116Z_

编译成功，生成 10 页 PDF（248KB）。`paper.pdf` 已写入目标目录，所有交叉引用和引用均已解析（仅有 hyperref 的 math-in-section-title 警告，无实质错误）。

论文覆盖了全部 12 个实验数据集：T1 主表（7 模型配置）、T2 tiebreak 对比、T3 K 敏感性、T4 开销分析、constraint ablation、constraint quality case studies、GSM8K cross-domain pilot、以及附录完整 C0 诊断数据点表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "114afe0d-e72b-49ce-9ea4-60355c32c2d4",
  "isSidechain": false,
  "requestId": "req_011Cb6HzqVzL3MWSRdKjx7hf",
  "type": "assistant",
  "uuid": "418a75ac-5f12-41de-8834-8d2ce77b592d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260516T124139/median",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBcKgE9mZw74Fy7exHatxq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8134,
      "cache_read_input_tokens": 46170,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8134,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 46170,
          "cache_creation_input_tokens": 8134,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8134
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260516T124139 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_c…",
  "leafUuid": "418a75ac-5f12-41de-8834-8d2ce77b592d",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on symbolic consensus",
  "sessionId": "c4b48419-90ca-4468-8335-af2b24dda8d3"
}
```

---
