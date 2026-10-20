# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/20f4d989-b56d-4594-ae93-7274d38db3de.jsonl`
- **Structured JSON:** [`16ebb4601f4d0ef8729e.json`](../../sessions/16/16ebb4601f4d0ef8729e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T15:26:07.498Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T15:26:07.498Z",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Capability trap 被结构性确认。Temperature ablation (§5) 展示 diversity 通过 temperature 可连续操控 (C0: 28%→68%), 但 SICA-SC gap 在所有温度下恒为零 (|Δ|≤1.7pp, 全部 p>0.30) ——这是结构性限制而非调参失败。F2 hero figure per-problem scatter (n=307) 直观展示 constraint precision ≈ 0.50 (近随机) 且与 vote_entropy 无相关 (slope=0.003, r²<0.01), 无需 binning 即清晰可读。Qwen 7B/14B/72B 产出三个 distinct C0 水平 (65%/53%/15%), Claim 3 diagnostic predictor 成立。五个模型族 combined N>1300 全部 SICA≈SC (最大 |Δ|=6.67pp 但 p=0.22, 零个 p<0.10)。MaxSAT≈count-only≈random-weight 确认 solver 无贡献, 与 F2 per-problem 形成双重机制证据。Discordant pair aggregate winrate=50.7% (34/67), weighted Δ=+0.20pp——统计上精确为零。三条 claims 措辞不改, title \"The Capability Trap\" 不变。强 EMNLP main submission, contribution = mechanism identification + first systematic negative result + zero-cost diagnostic。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-17T15:26:07.502Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T15:26:07.502Z",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-17T15:26:07.538Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Capability trap 被结构性确认。Temperature ablation (§5) 展示 diversity 通过 temperature 可连续操控 (C0: 28%→68%), 但 SICA-SC gap 在所有温度下恒为零 (|Δ|≤1.7pp, 全部 p>0.30) ——这是结构性限制而非调参失败。F2 hero figure per-problem scatter (n=307) 直观展示 constraint precision ≈ 0.50 (近随机) 且与 vote_entropy 无相关 (slope=0.003, r²<0.01), 无需 binning 即清晰可读。Qwen 7B/14B/72B 产出三个 distinct C0 水平 (65%/53%/15%), Claim 3 diagnostic predictor 成立。五个模型族 combined N>1300 全部 SICA≈SC (最大 |Δ|=6.67pp 但 p=0.22, 零个 p<0.10)。MaxSAT≈count-only≈random-weight 确认 solver 无贡献, 与 F2 per-problem 形成双重机制证据。Discordant pair aggregate winrate=50.7% (34/67), weighted Δ=+0.20pp——统计上精确为零。三条 claims 措辞不改, title "The Capability Trap" 不变。强 EMNLP main submission, contribution = mechanism identification + first systematic negative result + zero-cost diagnostic。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "d67ed967-c461-47d5-8741-33ae85d9288e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T15:26:07.525Z_

```json
{
  "parentUuid": "d67ed967-c461-47d5-8741-33ae85d9288e",
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
  "uuid": "2eeec1a5-94b2-4324-b5f4-5038c36dfdba",
  "timestamp": "2026-05-17T15:26:07.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T15:26:07.525Z_

```json
{
  "parentUuid": "2eeec1a5-94b2-4324-b5f4-5038c36dfdba",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b046311e-187a-4651-beab-c14d9af98bc9",
  "timestamp": "2026-05-17T15:26:07.525Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
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
  "aiTitle": "Generate symbolic invariant consensus paper",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Assistant

_source line 7 · 2026-05-17T15:26:10.668Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b046311e-187a-4651-beab-c14d9af98bc9",
  "isSidechain": false,
  "requestId": "req_011Cb8NgovaFedo7xHqkEciJ",
  "type": "assistant",
  "uuid": "fe422153-ef74-4baf-b4b1-eae2b697f661",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzCqb4gFCcXT4eRGi1enSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12723
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

_source line 8 · 2026-05-17T15:26:11.152Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FydNW2cnwDPWRyFW3Fm2ad`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe422153-ef74-4baf-b4b1-eae2b697f661",
  "isSidechain": false,
  "requestId": "req_011Cb8NgovaFedo7xHqkEciJ",
  "type": "assistant",
  "uuid": "e6046c91-c636-46d6-ae3a-f7e377b1d599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzCqb4gFCcXT4eRGi1enSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12723
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

_source line 9 · 2026-05-17T15:26:11.599Z_

<details><summary>↩ Tool result · `toolu_01FydNW2cnwDPWRyFW3Fm2ad`</summary>

```text
1	[
2	  {
3	    "name": "sica_k_ablation_14b",
4	    "description": "K=6/8/11/12/16/20 sensitivity on D012 60q, 含 odd K=11 tiebreak 隔离测试",
5	    "results": {
6	      "n": 60,
7	      "K6_sica": 0.733,
8	      "K6_sc": 0.733,
9	      "K6_delta_pp": 0.0,
10	      "K8_sica": 0.733,
11	      "K8_sc": 0.75,
12	      "K8_delta_pp": -1.7,
13	      "K11_sica": 0.733,
14	      "K11_sc": 0.733,
15	      "K11_delta_pp": 0.0,
16	      "K12_sica": 0.7,
17	      "K12_sc": 0.75,
18	      "K12_delta_pp": -5.0,
19	      "K16_sica": 0.717,
20	      "K16_sc": 0.75,
21	      "K16_delta_pp": -3.3,
22	      "K20_sica": 0.7,
23	      "K20_sc": 0.733,
24	      "K20_delta_pp": -3.3,
25	      "all_K_sica_leq_sc": true,
26	      "larger_K_degrades_sica": true,
27	      "mcnemar_p_all_gt_020": true
28	    },
29	    "tables": [
30	      "Appendix: K sensitivity table (all K × accuracy)"
31	    ],
32	    "figures": [],
33	    "analysis": "K ablation 消除 'wrong K' counterargument。K=11 odd-K test 最锐利: 若 SICA 在 tiebreaking 之外有价值, gap 应在 odd K 也存在; gap=0 确认 SICA = tiebreaker。 Combined with exp-003 (tiebreak 仅占 17% 问题), SICA 的唯一 mechanism 被量化为 micro-scale effect。Paper §4.2 mechanism analysis。\n\n\nSICA ≤ SC at all K 因为 MaxSAT over non-discriminative constraints 只注入噪声。 K=11 (odd) Δ=0 是关键: odd K 消除 SC ties, SICA 失去唯一有效机制 (tiebreaking), collapse to SC。Larger K (16, 20) 放大噪声注入——更多 traces → 更多 non-discriminative constraints → MaxSAT 更大概率排除正确答案。-5pp at K=12 和 -3.3pp at K=16/20 反映此噪声累积。All p>0.20 因 n=60 (SE≈5-6pp), 个体波动是 sampling noise 叠加在 true effect ≈ 0 之上。\n"
34	  },
35	  {
36	    "name": "tiebreak_baseline_analysis",
37	    "description": "CPU-only: SICA vs SC-random vs SC-alphabetical vs SC-first-seen tiebreak 比较",
38	    "results": {
39	      "n_tied_questions": 10,
40	      "pct_tied_of_total": 0.167,
41	      "sica_tiebreak_accuracy": 0.8,
42	      "random_tiebreak_accuracy": 0.5,
43	      "alphabetical_tiebreak_accuracy": 0.6,
44	      "first_seen_tiebreak_accuracy": 0.4,
45	      "sica_net_gain_over_random_on_all_60": 0.5
46	    },
47	    "tables": [
48	      "T4: Tiebreak Analysis (tied subset)"
49	    ],
50	    "figures": [],
51	    "analysis": "回应 reviewer 'SICA is just a better tiebreaker'。Answer: yes, and an effective one, but ties are structurally rare at K=12. At odd K (exp-002 K=11), ties = 0, SICA≡SC。Even at even K, 80% × 17% = 1.3% net correct → <1pp overall。 Cost-benefit: 49% overhead (exp-009) for <1pp on tied subset = not worthwhile。\n\n\nSICA 在 tied questions 上 80% 正确, 因为 constraint weighting 即使不判别 correct vs incorrect, 对 tie (两个 answer 票数相等) 仍能通过微弱信号打破平衡。但 tied questions 仅占 17% (K=12 even-K 才产生 tie)。10 题中多赢 3 题 (vs random) 对 60 题整体贡献 +0.5pp——在 SE≈6pp 的噪声中不可见。Random 50% 是理论 期望值; alphabetical 60% 反映答案选项 label 与正确答案的偶然相关; first-seen 40% 因为 model 首条 trace 并非最准确。\n"
52	  },
53	  {
54	    "name": "sica_constraint_ablation",
55	    "description": "CPU-only ablation: MaxSAT vs count-only vs random-weight on exp-001 (n=804)",
56	    "results": {
57	      "n": 804,
58	      "maxsat_accuracy": 0.7649,
59	      "count_only_accuracy": 0.7662,
60	      "random_weight_accuracy": 0.7637,
61	      "sc_baseline_accuracy": 0.7624,
62	      "agreement_802_of_804": true,
63	      "maxsat_vs_count_mcnemar_p": 0.99,
64	      "maxsat_vs_random_mcnemar_p": 0.85,
65	      "maxsat_vs_sc_mcnemar_p": 0.74,
66	      "all_pairwise_nonsignificant": true
67	    },
68	    "tables": [
69	      "T3: Constraint Ablation (MaxSAT vs count-only vs random-weight vs SC)"
70	    ],
71	    "figures": [],
72	    "analysis": "Make-or-break evidence for capability trap mechanism。如果 MaxSAT ≈ count-only, solver 无附加值——constraints 没有 exploitable satisfiability structure。Combined with F2 (precision≈0.50), 形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Paper §4.1 核心机制结果。exp-013 + exp-019 共同构成 Claim 1 的 evidence base。\n\n\nMaxSAT ≈ count-only 因为 constraint satisfiability 不携带判别信息。当 constraints 对正确/错误答案同等满足时, solver 的优化退化为计数: satisfiability structure 无 贡献。Random-weight ≈ MaxSAT 因为权重差异在 non-discriminative constraints 上是 纯噪声。802/804 题四种方法答案一致, 仅 2 题分歧 (互相抵消)。这直接证明 SAT 解算机制空洞化——是 capability trap 的 mechanism evidence。\n"
73	  },
74	  {
75	    "name": "sica_strategyqa_14b",
76	    "description": "Qwen2.5-14B on StrategyQA 60q (K=12), commonsense reasoning domain",
77	    "results": {
78	      "n": 60,
79	      "k": 12,
80	      "sica_accuracy": 0.5667,
81	      "sc_accuracy": 0.5333,
82	      "delta_pp": 3.33,
83	      "mcnemar_p": ">0.30",
84	      "bootstrap_p": 0.1346,
85	      "multi_candidate_rate": 0.1,
86	      "extraction_rate_trace": 0.704,
87	      "discordant_sica_wins": 2,
88	      "discordant_sc_wins": 0,
89	      "model": "Qwen2.5-14B-Instruct",
90	      "dataset": "StrategyQA"
91	    },
92	    "tables": [
93	      "T1: Main Results (StrategyQA × Qwen-14B row)",
94	      "F3: Operating Regime Heatmap (StrategyQA × Qwen-14B cell)"
95	    ],
96	    "figures": [],
97	    "analysis": "StrategyQA 结果挑战 best-case-diversity 假设: commonsense domain 并非 diversity 最高场景 (对强模型而言)。但强化 capability trap: 即使 C0 恰好产生少量 discordant, SICA 仍无显著优势。与 ARC (C0=5%) 和 PW+FOLIO (C0=38%) 形成三域覆盖。\n\n\nStrategyQA C0=10% 远低于 plan 预期 (35-50%), 因为 14B 在 binary commonsense (yes/no) 上足够强, 大多数问题 12 traces 一致。仅 6 题多候选, 2 题 SICA 翻转正确。+3.33pp non-significant (n=60 SE≈6pp, bootstrap p=0.13)。Extraction rate 仅 70.4% (commonsense 推理链缺少可形式化逻辑结构), 进一步限制 SICA 操作空间。2:0 discordant ratio 看似 SICA 占优, 但 n=2 discordant pairs 无统计意义。\n"
98	  },
99	  {
100	    "name": "sica_arc_challenge_14b",
101	    "description": "Qwen2.5-14B on ARC-Challenge 60q (K=12), 科学推理 4 选 1",
102	    "results": {
103	      "n": 60,
104	      "k": 12,
105	      "sica_accuracy": 0.95,
106	      "sc_accuracy": 0.9667,
107	      "delta_pp": -1.67,
108	      "multi_candidate_rate": 0.05,
109	      "extraction_rate": 1.0,
110	      "discordant_sica_wins": 0,
111	      "discordant_sc_wins": 1,
112	      "model": "Qwen2.5-14B-Instruct",
113	      "dataset": "ARC-Challenge"
114	    },
115	    "tables": [
116	      "T1: Main Results (ARC × Qwen-14B row)",
117	      "F3: Operating Regime Heatmap (ARC × Qwen-14B cell)"
118	    ],
119	    "figures": [],
120	    "analysis": "ARC 是 14B 的 ceiling 域: SC 已达 96.7%, 无提升空间。SICA 微损 (-1.7pp) 因为 solver 在极少数 multi-candidate 问题上注入噪声。与 FOLIO (acc ~79%, C0 ~38%) 对比展示 capability-diversity 反向关系: high accuracy → low C0 → method degenerates。\n\n\n14B 在 ARC-Challenge SC 高达 96.7%, C0 仅 5% (3 题多候选)。模型对 science 常识 足够自信, 12 traces 几乎总一致。唯一 discordant pair SC 赢——MaxSAT 排除了正确 答案的 constraint。4-choice format 理论上增加 diversity (更多选项), 但 14B 能力 过强, format 效应被 capability 压制。C0=5% 接近 QwQ-32B 退化阈值。\n"
121	  },
122	  {
123	    "name": "constraint_quality_correlation",
124	    "description": "CPU-only: per-problem constraint precision vs vote_entropy (exp-001 n≈307 multi-candidate). F2 hero figure",
125	    "results": {
126	      "n_multi_candidate": 307,
127	      "constraint_precision_mean": 0.505,
128	      "constraint_precision_std": 0.148,
129	      "constraint_precision_median": 0.5,
130	      "precision_vs_entropy_slope": 0.003,
131	      "precision_vs_entropy_r_squared": 0.002,
132	      "precision_vs_entropy_p": 0.42,
133	      "folio_precision_mean": 0.512,
134	      "proofwriter_precision_mean": 0.498,
135	      "cross_domain_precision_diff_p": 0.6,
136	      "fraction_precision_below_040": 0.28,
137	      "fraction_precision_above_060": 0.25,
138	      "discordant_pair_sica_winrate_overall": 0.48
139	    },
140	    "tables": [
141	      "T2: Constraint Quality Summary (precision by domain × model)"
142	    ],
143	    "figures": [],
144	    "analysis": "F2 是论文 hero figure, 一图传达 capability trap: diversity (x) 存在且可变, 但 constraint quality (y) 恒为随机水平。'Regardless of diversity' 可视化为 slope=0。 与 T3 (MaxSAT≈count-only) 形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Per-problem granularity (n=307) 比 experiment-level correlation (n=7, r=0.15 p=0.74) 统计力强两个数量级, 是 D035 识别的 F2 data gap 的完整解决。\n\n\nConstraint precision ≈ 0.50 (近随机) 因为 LLM 提取的 FOL constraints 捕获推理 trace 的表面结构 (变量命名、逻辑连接词模式) 而非深层语义正确性。正确和错误 traces 共享相似表面结构 (都使用 if-then/forall/exists), 导致 constraints 无法区分二者。 Slope ≈ 0 因为此限制是 structural 的: 无论 vote 分布多分散 (高 entropy) 或多集中 (低 entropy), constraint discriminative power 都不变——它取决于 extraction quality 而非 diversity level。FOLIO 和 ProofWriter precision 几乎相同 (0.512 vs 0.498, 差异 p=0.60), 说明跨域一致。28% 问题 precision<0.40 (constraints 反向判别), 25% precision>0.60 (偶然判别), 呈对称分布围绕 0.50。\n"
145	  },
146	  {
147	    "name": "sica_7b_scaling",
148	    "description": "Qwen2.5-7B-Instruct on D012 60q. Within-Qwen weak model, high C0",
149	    "results": {
150	      "n": 60,
151	      "k": 12,
152	      "sica_accuracy": 0.533,
153	      "sc_accuracy": 0.55,
154	      "delta_pp": -1.7,
155	      "multi_candidate_rate": 0.65,
156	      "extraction_rate": 0.82,
157	      "answer_extraction_rate": 0.88,
158	      "contradiction_rate": 0.08,
159	      "discordant_sica_wins": 2,
160	      "discordant_sc_wins": 3,
161	      "mcnemar_p": 0.65,
162	      "proofwriter_sica": 0.5,
163	      "proofwriter_sc": 0.533,
164	      "folio_sica": 0.567,
165	      "folio_sc": 0.567,
166	      "model": "Qwen2.5-7B-Instruct"
167	    },
168	    "tables": [
169	      "T1 appendix: Qwen-7B row",
170	      "F4: C0 vs Gap (7B 数据点: C0=65%, Δ=-1.7pp)"
171	    ],
172	    "figures": [],
173	    "analysis": "7B 提供 within-Qwen scaling 的 high-diversity anchor。Combined with 14B (C0=53%) and 72B (C0≈15%), 三个 distinct C0 levels within single model family 成立 (c0_scaling_distinct_levels=3)。C0 与 model scale 反向 (7B→65%, 14B→53%, 72B→15%) 验证 C0 as capability proxy。但 SICA-SC gap 在三个 scale 都 ≈ 0, 证明 C0 是 necessary but insufficient。For Claim 3: C0=65% + Δ=-1.7pp 是 'high C0 but no gain' 的最强数据点。\n\n\n7B 在 formal logic 上显著弱于 14B (SC 55% vs 73%), 产生大量 answer disagreement (C0=65%)。但更弱模型也提取更差 constraints: extraction_rate 89%→82%, contradiction_rate 2.2%→8%。高 C0 意味着更多 multi-candidate 问题可操作, 但 constraints 质量更差意味着 MaxSAT 优化方向更随机。5 discordant pairs 中 SC 赢 3 个: MaxSAT 在 noisy constraints 上更大概率排除正确答案。 这完美展示 capability trap weak-model 端: diversity abundant, quality absent。\n"
174	  },
175	  {
176	    "name": "qwq_32b_operating_regime",
177	    "description": "QwQ-32B negative results: C0<5%, SICA≡SC. CPU-only格式化 MVP 已有数据",
178	    "results": {
179	      "total_problems": 46,
180	      "qwq_c0_nominal_pct": 10.3,
181	      "qwq_c0_effective_pct": 2.6,
182	      "qwen14b_c0_pct": 46.0,
183	      "diversity_ratio": 17.7,
184	      "aime_delta_pp": 0.0,
185	      "aime_n": 22,
186	      "proofwriter_delta_pp": -5.9,
187	      "proofwriter_n": 17,
188	      "folio_n": 2,
189	      "c0_below_20_threshold": true,
190	      "sica_structurally_degenerate": true
191	    },
192	    "tables": [
193	      "T1: Main Results (QwQ-32B row, all cells 'SICA≡SC')",
194	      "F3: Operating Regime Heatmap (QwQ-32B column 全灰)"
195	    ],
196	    "figures": [],
197	    "analysis": "QwQ-32B 是 Claim 2 'operating regime empty' 的一极: full reasoning → no diversity → method degenerates。对称地, instruction models 展示另一极: high diversity → no constraint quality → method fails。No model hits the sweet spot。C0=2.6% 远低于 20% 阈值, 直接支撑 Claim 3 early-stopping criterion。\n\n\nQwQ-32B 作为 full reasoning model, deterministic chain-of-thought 压制 sampling diversity: 即使 T=0.7, 12 traces 几乎总产生相同答案 (effective C0=2.6%)。AIME 22 题 0% multi-candidate (完全一致)。Nominal C0=10.3% vs effective C0=2.6% 的差距来自 answer extraction 格式噪声 (如 \"30\" vs \"30.0\"), 非真实 reasoning divergence。 ProofWriter -5.9pp 是 n=17 噪声 (SE≈12pp)。QwQ-32B 展示 capability trap strong- reasoning 端: model 足够强 → 无 diversity → SICA 结构性退化为 SC。\n"
198	  },
199	  {
200	    "name": "c0_diagnostic_validation",
201	    "description": "CPU-only: C0 vs SICA-SC gap 散点, 跨所有 models/K/domains, 验证 C0 as predictor",
202	    "results": {
203	      "n_conditions": 14,
204	      "c0_range_pct": [
205	        2.6,
206	        65.0
207	      ],
208	      "gap_range_pp": [
209	        -3.3,
210	        6.67
211	      ],
212	      "regression_slope": -0.02,
213	      "regression_r_squared": 0.06,
214	      "regression_p": 0.4,
215	      "c0_below_5_n": 3,
216	      "c0_below_5_mean_abs_gap": 0.6,
217	      "c0_above_20_n": 8,
218	      "c0_above_20_mean_gap": 0.1,
219	      "c0_above_20_all_p_gt_010": true,
220	      "distinct_c0_levels_qwen_family": 3,
221	      "distinct_c0_levels_all_models": 5
222	    },
223	    "tables": [
224	      "F4: C0 vs Gap (所有条件)"
225	    ],
226	    "figures": [],
227	    "analysis": "F4 是 Claim 3 核心 figure。Bifurcation 清晰: C0<5% → degenerate (grey), C0>20% → trapped (red), no sweet spot。理论上界展示 SICA 在 C0=50% 时应有 5-10pp gain if constraints discriminative——this unrealized potential IS the trap。 C0 因此是 zero-cost early stopping criterion: compute C0, if <20% stop (method degenerate), if >20% stop (trap guarantees no gain)。Either way, don't proceed。\n\n\nC0 与 gap 无线性关系 (r²=0.06, p=0.40) 因为 gap 在所有 C0 水平围绕 0 波动。 C0<5% 条件 (QwQ-32B 2.6%, ARC-14B 5%, StrategyQA-14B 10%) SICA≡SC: 方法 结构性退化。C0>20% 条件 (Qwen-7B 65%, LLaMA-8B 62%, DeepSeek-R1-7B 58%, Mistral 50%, Qwen-14B 53%) mean gap≈0: diversity 存在但 constraints 不判别。 Within-Qwen 三水平 (15%/53%/65%) + DeepSeek (58%) + LLaMA (62%) ≈ 5 distinct levels。F4 展示理论上界 vs 实际数据的 gap = capability trap 的视觉量化。\n"
228	  },
229	  {
230	    "name": "sica_72b_awq",
231	    "description": "Qwen2.5-72B-Instruct-AWQ on D012 60q. Within-Qwen strong model, low C0",
232	    "results": {
233	      "n": 60,
234	      "k": 12,
235	      "sica_accuracy": 0.867,
236	      "sc_accuracy": 0.867,
237	      "delta_pp": 0.0,
238	      "multi_candidate_rate": 0.15,
239	      "extraction_rate": 0.93,
240	      "answer_extraction_rate": 1.0,
241	      "contradiction_rate": 0.01,
242	      "discordant_sica_wins": 1,
243	      "discordant_sc_wins": 1,
244	      "mcnemar_p": 1.0,
245	      "proofwriter_sica": 0.833,
246	      "proofwriter_sc": 0.833,
247	      "folio_sica": 0.9,
248	      "folio_sc": 0.9,
249	      "model": "Qwen2.5-72B-Instruct-AWQ"
250	    },
251	    "tables": [
252	      "T1 appendix: Qwen-72B row",
253	      "F4: C0 vs Gap (72B 数据点: C0=15%, Δ=0)"
254	    ],
255	    "figures": [],
256	    "analysis": "72B 是 within-Qwen scaling 的 low-diversity anchor。三点连线清晰展示 C0 随 model scale 单调递减 (65%→53%→15%) 但 gap 恒为 ≈0。这证明 'even when you scale up within a family, you trade diversity for accuracy without ever hitting the sweet spot'。72B extraction quality 最高 (93%, 1% contradiction) 佐证 strong model → better constraints, 但 futile when C0 is low。\n\n\n72B SC accuracy 高达 86.7%, C0 仅 15% (9 题多候选)。能力强到大部分问题 12 traces 一致。Extraction_rate 高 (93%), contradiction_rate 极低 (1%)——72B 的 constraints 质量确实更好。但 C0 太低, 没有足够 multi-candidate 问题让 SICA 操作。 仅 ~2 discordant pairs, 各赢一题, 净 Δ=0。AWQ 4-bit quantization 可能引入 微量额外噪声, 使 C0 略高于 full-precision 72B (否则可能 C0<10%), 但仍远低于 14B。这是 capability trap strong-model 端: quality improves but diversity vanishes。\n"
257	  },
258	  {
259	    "name": "overhead_analysis",
260	    "description": "exp-001 Wall-time breakdown: trace generation, constraint extraction, MaxSAT",
261	    "results": {
262	      "n": 804,
263	      "mean_total_wall_s": 61.6,
264	      "mean_trace_gen_s": 31.6,
265	      "trace_gen_pct": 51.3,
266	      "mean_extract_s": 29.0,
267	      "extract_pct": 47.0,
268	      "mean_dedup_s": 1.0,
269	      "dedup_pct": 1.6,
270	      "mean_maxsat_s": 0.003,
271	      "maxsat_pct": 0.005,
272	      "sica_overhead_over_sc_pct": 48.7,
273	      "p50_overhead_pct": 48.9,
274	      "p90_overhead_pct": 57.6
275	    },
276	    "tables": [
277	      "Appendix: Overhead breakdown table"
278	    ],
279	    "figures": [],
280	    "analysis": "回应 reviewer 'is the overhead worth it': 不值得。49% overhead = 零精度收益。 SC 是 Pareto dominant (same accuracy, half the cost)。Solver time <0.01% 表明 MaxSAT formulation 计算效率不是问题——问题在于输入质量。This strengthens practical guidance: even if future work improves constraint quality, the extraction cost remains substantial。\n\n\nSICA 相比 SC 增加 ~49% wall time, 几乎全部来自 constraint extraction (一次额外 LLM inference pass per trace, 解析 FOL)。MaxSAT solver 本身极快 (0.003s, <0.01% 总时间)——瓶颈不在 solver complexity 而在 extraction cost。如果 constraints 是 discriminative 的, 49% overhead 可能值得 (每 query 多花 30s 换 5pp+ accuracy); 但 Δ≈0 意味着 49% 额外计算换零收益。P90 overhead 57.6% 来自长 traces (FOLIO domain), extraction 时间与 trace 长度成正比。\n"
281	  },
282	  {
283	    "name": "sica_llama_8b",
284	    "description": "LLaMA-3.1-8B-Instruct on D012 60q. 第三 instruction-scale 家族",
285	    "results": {
286	      "n": 60,
287	      "k": 12,
288	      "sica_accuracy": 0.6667,
289	      "sc_accuracy": 0.6,
290	      "delta_pp": 6.67,
291	      "multi_candidate_rate": 0.617,
292	      "extraction_rate": 0.856,
293	      "answer_extraction_rate": 0.896,
294	      "contradiction_rate": 0.053,
295	      "truncated_traces": 44,
296	      "discordant_sica_wins": 5,
297	      "discordant_sc_wins": 1,
298	      "mcnemar_p": 0.22,
299	      "model": "LLaMA-3.1-8B-Instruct"
300	    },
301	    "tables": [
302	      "T1: Main Results (LLaMA-8B D012 row)"
303	    ],
304	    "figures": [],
305	    "analysis": "exp-011 的 +6.67pp 是全研究最大正 delta, 但 exp-019/020 (同模型 n=200+) 展示 true effect ≈ 0。Paper framing: 'small-sample positive signal does not survive powered replication'——本身是方法论 lesson。LLaMA-8B 作为第三 instruction-scale family (加 Qwen/Mistral), 满足 EMNLP 三家族最低门槛。\n\n\nLLaMA-8B C0=62%, SC=60% (instruction-scale models 中最弱)。+6.67pp 是 n=60 采样噪声: SE≈6pp, 1.1σ deviation, p=0.22 non-significant。5:1 discordant ratio 看似强烈, 但绝对数量小 (6 pairs)。关键验证来自同模型更大 n: exp-019 (StrategyQA n=200, Δ=+2.0pp p=0.42) 和 exp-020 (FOLIO n=204, Δ=-2.45pp p=0.27) 确认 true effect 接近 0。正 delta 与 负 delta 在不同 domains 交替出现 = 纯噪声。 44/720 truncated traces 因 8B context limit, 但 truncation 对 SICA/SC 影响对称。\n"
306	  },
307	  {
308	    "name": "gsm8k_pilot_14b",
309	    "description": "Qwen2.5-14B on GSM8K 30q pilot (K=12). 数学推理域覆盖",
310	    "results": {
311	      "n": 30,
312	      "k": 12,
313	      "sica_accuracy": 0.867,
314	      "sc_accuracy": 0.867,
315	      "delta_pp": 0.0,
316	      "multi_candidate_rate": 0.1,
317	      "extraction_rate": 0.75,
318	      "answer_extraction_rate": 0.95,
319	      "discordant_sica_wins": 0,
320	      "discordant_sc_wins": 0,
321	      "model": "Qwen2.5-14B-Instruct",
322	      "dataset": "GSM8K"
323	    },
324	    "tables": [
325	      "Appendix: Cross-domain (GSM8K row)",
326	      "F4: C0 vs Gap (GSM8K point)"
327	    ],
328	    "figures": [],
329	    "analysis": "GSM8K 确认: 当模型在目标 domain 足够强时, C0 自然低, SICA 无操作空间。 Extraction rate 75% (vs logic domain 89%) 说明 domain 影响 extraction feasibility。 Appendix material, 回应 'what about math reasoning' 的 reviewer。\n\n\n14B 在 GSM8K accuracy ~87%, C0 ≈ 10%。开放式数学答案 (具体数字) 理论上有更大 answer space, 但模型能力足以收敛到正确数值。Extraction rate 偏低 (75%) 因为数值 计算步骤难以 FOL 形式化 (例 \"3×5+2=17\" → FOL 表达不自然)。0 discordant pairs → SICA ≡ SC on all 30 题。C0≈10% 类似 ARC/StrategyQA: 14B 在 'easier' domains 上能力过强, diversity 不足。\n"
330	  },
331	  {
332	    "name": "sica_deepseek_r1_llama_8b",
333	    "description": "DeepSeek-R1-Distill-Qwen-7B on D012 60q. Distilled reasoning model 行为验证",
334	    "results": {
335	      "n": 60,
336	      "k": 12,
337	      "sica_accuracy": 0.683,
338	      "sc_accuracy": 0.717,
339	      "delta_pp": -3.33,
340	      "multi_candidate_rate": 0.583,
341	      "extraction_rate": 0.839,
342	      "answer_extraction_rate": 0.939,
343	      "truncated_traces": 72,
344	      "contradiction_rate": 0.037,
345	      "discordant_sica_wins": 0,
346	      "discordant_sc_wins": 2,
347	      "mcnemar_p": 0.48,
348	      "model": "DeepSeek-R1-Distill-Qwen-7B"
349	    },
350	    "tables": [
351	      "T1: Main Results (DeepSeek-R1-7B row)",
352	      "Appendix: Reasoning model comparison (QwQ C0=2.6% vs DeepSeek C0=58.3%)"
353	    ],
354	    "figures": [],
355	    "analysis": "exp-014 解决分类问题: DeepSeek-R1-7B 归入 instruction-scale (C0=58%) 非 reasoning (C0<5%)。Model taxonomy 应以行为 (C0 水平) 而非训练方法定义。Paper 重分类 DeepSeek-R1-7B 为 'instruction-scale with reasoning-style training', 避免 reviewer 'only one reasoning model' 攻击。QwQ-32B remains sole full reasoning model。\n\n\n关键发现: C0=58.3%, 行为完全像 instruction-scale model, 非 plan 预期的 reasoning model (C0<5%)。7B 参数量不足以维持 R1 的 deterministic reasoning chain——蒸馏后 小模型在 7B 容量下退化为高 diversity 行为。Δ=-3.33pp: 2 discordant pairs SC 全赢, MaxSAT constraint 排除恰好排错。Truncated traces 最多 (72/720), 因 R1 风格长 reasoning + 7B context 限制。结论: distilled reasoning ≠ full reasoning, 参数量是决定性因素, 非训练方法。\n"
356	  },
357	  {
358	    "name": "logic_lm_baseline",
359	    "description": "Logic-LM × K: single-trace FOL verification K 次后 vote, CPU-only on FOLIO",
360	    "results": {
361	      "n": 204,
362	      "k": 12,
363	      "logic_lm_k_accuracy": 0.789,
364	      "sc_accuracy": 0.794,
365	      "sica_accuracy": 0.794,
366	      "logic_lm_vs_sc_delta_pp": -0.5,
367	      "logic_lm_vs_sica_delta_pp": -0.5,
368	      "verification_pass_rate": 0.92,
369	      "verification_discriminative": false,
370	      "mcnemar_logic_lm_vs_sc_p": 0.82
371	    },
372	    "tables": [
373	      "Appendix: Logic-LM × K baseline comparison"
374	    ],
375	    "figures": [],
376	    "analysis": "回应 reviewer 'compare to Logic-LM/LINC'。Answer: Logic-LM-K 也 ≈ SC, 因为 bottleneck 是 extraction quality 非 aggregation method。Single-trace verification 也失败, 因为 underlying constraints non-discriminative。This generalizes the capability trap beyond SICA to any FOL-constraint-based method。\n\n\nLogic-LM-K 将每条 trace 独立验证 (extract FOL → solver check → pass/fail) 后 majority vote。Accuracy ≈ SC 因为 verification pass rate 极高 (92%): solver 对 大部分 traces 返回 satisfiable, 无论 trace 是否正确。原因同 SICA: constraints 不判别。'Verification' 退化为 'format check'——只要 FOL syntax 正确 solver 就 pass。这消除 'maybe aggregation is the problem, single-trace verification works better' 反论。瓶颈是 constraint quality, 非 aggregation architecture。\n"
377	  },
378	  {
379	    "name": "weighted_sc_baseline",
380	    "description": "Weighted SC (Taubenfeld 2024 style): uniform/inv-length/length/constraint-count on exp-001",
381	    "results": {
382	      "n": 804,
383	      "sc_uniform_accuracy": 0.7624,
384	      "sica_maxsat_accuracy": 0.7649,
385	      "inv_length_accuracy": 0.7674,
386	      "length_weighted_accuracy": 0.7525,
387	      "constraint_count_accuracy": 0.7525,
388	      "inv_length_vs_sc_p": 0.453,
389	      "length_vs_sc_p": 0.153,
390	      "inv_length_vs_sica_p": 0.864,
391	      "all_nonsignificant": true
392	    },
393	    "tables": [
394	      "Appendix: Weighted SC comparison table"
395	    ],
396	    "figures": [],
397	    "analysis": "Weighted SC 是最直接竞争 baseline。All variants ≈ SC 确认: (1) 无简单 weighting 能 rescue method, (2) bottleneck 是 signal quality 非 aggregation sophistication。 SICA 失败不是因为 MaxSAT over-engineering, 而是因为 input signals (constraints) non-discriminative。Any aggregation over non-discriminative signals degenerates to counting, which ≈ voting。\n\n\n所有 weighting 方案 ≈ SC, 因为 trace-level 信号 (长度、constraint 数量) 同样 不具判别性。Inv-length 略高 (+0.50pp, p=0.45): shorter traces 可能稍 more focused, 但效果不显著。Length-weighted 和 constraint-count 略低 (-1pp): longer/more-constrained traces 未必更正确 (可能是 model 在错误路径上 elaborating)。关键 insight: 简单 weighting 也无法修复 non-discriminative 信号, 因为问题在底层信号质量而非权重方案。\n"
398	  },
399	  {
400	    "name": "constraint_quality_case_studies",
401	    "description": "8 representative problems 定性分析: constraints 为何 non-discriminative",
402	    "results": {
403	      "n_case_studies": 8,
404	      "correct_trace_precision": 0.52,
405	      "incorrect_trace_precision": 0.48,
406	      "constraint_overlap_rate": 0.78,
407	      "typical_constraint_types": [
408	        "conditional (if-then)",
409	        "universal quantifier (forall)",
410	        "negation",
411	        "predicate application"
412	      ],
413	      "discriminative_constraints_pct": 0.12
414	    },
415	    "tables": [],
416	    "figures": [],
417	    "analysis": "Case studies 提供定性理解, 补充 F2 定量证据。Reader 直观看到 WHY precision ≈ 0.50: constraints capture what the model reads (premises), not how it reasons (inference)。 也解释 WHY MaxSAT ≈ count-only: 如果 constraints mostly shared, satisfiability structure carries no information about answer correctness。1-2 examples 进 §4.1, 其余进 appendix。\n\n\nNon-discrimination 的 root cause: LLM 提取的 constraints 主要 formalize 题目 premises (前提条件) 而非 reasoning steps (推理步骤)。Premises 对正确/错误 traces 共享 (都正确读取了题目)——constraint overlap rate 78%。推理错误发生在 inference chain 更深位置: 这些错误要么不被 formalized (extraction 跳过复杂推导), 要么被 formalized 为看起来合理但语义不同的 constraints (surface structure 相似)。 仅 12% constraints 是 truly discriminative (只出现在正确或只出现在错误 traces), 且方向随机 (一半 favor correct, 一半 favor incorrect)。\n"
418	  },
419	  {
420	    "name": "temperature_ablation_t03_t05_t10",
421	    "description": "T=0.3/0.5/1.0 on Qwen-14B D012 60q. Temperature 操控 diversity, 验证 trap 结构性",
422	    "results": {
423	      "dataset": "D012",
424	      "model": "Qwen2.5-14B-Instruct",
425	      "n": 60,
426	      "k": 12,
427	      "t03_c0_pct": 28.3,
428	      "t03_sc_accuracy": 0.767,
429	      "t03_sica_accuracy": 0.767,
430	      "t03_delta_pp": 0.0,
431	      "t03_discordant_sica": 1,
432	      "t03_discordant_sc": 1,
433	      "t03_mcnemar_p": 1.0,
434	      "t03_extraction_rate": 0.91,
435	      "t05_c0_pct": 41.7,
436	      "t05_sc_accuracy": 0.75,
437	      "t05_sica_accuracy": 0.75,
438	      "t05_delta_pp": 0.0,
439	      "t05_discordant_sica": 1,
440	      "t05_discordant_sc": 1,
441	      "t05_mcnemar_p": 1.0,
442	      "t05_extraction_rate": 0.9,
443	      "t10_c0_pct": 68.3,
444	      "t10_sc_accuracy": 0.7,
445	      "t10_sica_accuracy": 0.683,
446	      "t10_delta_pp": -1.7,
447	      "t10_discordant_sica": 1,
448	      "t10_discordant_sc": 2,
449	      "t10_mcnemar_p": 0.56,
450	      "t10_extraction_rate": 0.87,
451	      "baseline_t07_c0_pct": 53.3,
452	      "baseline_t07_delta_pp": 0.0,
453	      "c0_monotonic_increase": true,
454	      "c0_sequence": "28.3% → 41.7% → 53.3% → 68.3%",
455	      "max_abs_delta_pp": 1.7,
456	      "all_p_gt_020": true
457	    },
458	    "tables": [
459	      "§5 Table: Temperature ablation (T × C0 × SC × SICA × Δ)"
460	    ],
461	    "figures": [],
462	    "analysis": "Temperature ablation 是论文最强 causal evidence: 通过实验操控 diversity (非仅 跨模型观察), 确认 diversity↑ 不改善 SICA。排除 confounders: 同一模型、同一数据、 只改 T, C0 从 28% 到 68% 连续变化, gap 恒为 0。如 reviewer 问 'maybe you haven't found the right diversity level': this answers definitively — we swept the full range, it doesn't help。与 F2 互补: F2 shows WHY (precision≈0.50), temp ablation shows THAT (gap=0 at all diversity levels)。§5 new evidence for EMNLP submission。\n\n\nTemperature 直接控制 sampling distribution entropy, 因此 C0 随 T 单调递增: T=0.3 时 logit distribution 尖锐, traces 集中到 modal answer, 仅 17 题多候选; T=1.0 时分布平坦, 41 题多候选。这是 structural: T→entropy→C0 是因果链。\nSC accuracy 随 T 先平后降: T=0.3-0.7 SC≈73-77% (集中在正确答案近邻), T=1.0 SC 降到 70% (更多随机错误破坏多数票)。已知 SC behavior。\nSICA-SC gap 在所有 T 下 |Δ| ≤ 1.7pp: - T=0.3 (C0=28%): 仅 17 题多候选, 1 discordant, 1:1 → Δ=0。少数 multi-candidate\n  问题上 constraints 恰好一胜一负。\n- T=0.5 (C0=42%): 25 题多候选, constraints 仍 non-discriminative → Δ=0。\n  更多 problems 可操作, 但操作方向随机。\n- T=1.0 (C0=68%): 41 题多候选, constraints 质量因 noisier traces 进一步下降\n  (高温 traces 更长、更散漫, extraction noise 增加) → Δ=-1.7pp。MaxSAT 在\n  嘈杂 constraints 上做了一次净错误排除。\n\nAll p>0.20 at n=60 (SE≈5-6pp)。True effect = 0 at all temperatures。\n"
463	  },
464	  {
465	    "name": "gsm8k_pilot_30q",
466	    "description": "等同 exp-012。Qwen-14B on GSM8K 30q, 数学推理域 pilot",
467	    "results": {
468	      "note": "同 exp-012, 参见上方 gsm8k_pilot_14b entry",
469	      "n": 30,
470	      "k": 12,
471	      "sica_accuracy": 0.867,
472	      "sc_accuracy": 0.867,
473	      "delta_pp": 0.0,
474	      "multi_candidate_rate": 0.1,
475	      "extraction_rate": 0.75,
476	      "model": "Qwen2.5-14B-Instruct",
477	      "dataset": "GSM8K"
478	    },
479	    "tables": [
480	      "Appendix: GSM8K row (同 exp-012)"
481	    ],
482	    "figures": [],
483	    "analysis": "与 exp-012 完全重复。收录条件: 如果 GPU budget 允许, 作为第四个 domain 进入 appendix (主文已有 FOLIO + StrategyQA + ARC + ProofWriter 四域)。\n\n与 exp-012 相同实验。14B 在 GSM8K accuracy ~87%, C0 ~10%。数学推理的 open-ended answer space (具体数字) 理论上增加 diversity, 但 14B 能力收敛到正确数值。 Extraction rate 偏低 (75%) 因为数值计算难以 FOL 化。SICA ≡ SC。 作为 appendix cross-domain data point, 为 'what about math' reviewer concern 提供证据。\n"
484	  }
485	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6046c91-c636-46d6-ae3a-f7e377b1d599",
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "e8281642-546c-4406-9679-29953018ab40",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"sica_k_ablation_14b\",\n    \"description\": \"K=6/8/11/12/16/20 sensitivity on D012 60q, 含 odd K=11 tiebreak 隔离测试\",\n    \"results\": {\n      \"n\": 60,\n      \"K6_sica\": 0.733,\n      \"K6_sc\": 0.733,\n      \"K6_delta_pp\": 0.0,\n      \"K8_sica\": 0.733,\n      \"K8_sc\": 0.75,\n      \"K8_delta_pp\": -1.7,\n      \"K11_sica\": 0.733,\n      \"K11_sc\": 0.733,\n      \"K11_delta_pp\": 0.0,\n      \"K12_sica\": 0.7,\n      \"K12_sc\": 0.75,\n      \"K12_delta_pp\": -5.0,\n      \"K16_sica\": 0.717,\n      \"K16_sc\": 0.75,\n      \"K16_delta_pp\": -3.3,\n      \"K20_sica\": 0.7,\n      \"K20_sc\": 0.733,\n      \"K20_delta_pp\": -3.3,\n      \"all_K_sica_leq_sc\": true,\n      \"larger_K_degrades_sica\": true,\n      \"mcnemar_p_all_gt_020\": true\n    },\n    \"tables\": [\n      \"Appendix: K sensitivity table (all K × accuracy)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"K ablation 消除 'wrong K' counterargument。K=11 odd-K test 最锐利: 若 SICA 在 tiebreaking 之外有价值, gap 应在 odd K 也存在; gap=0 确认 SICA = tiebreaker。 Combined with exp-003 (tiebreak 仅占 17% 问题), SICA 的唯一 mechanism 被量化为 micro-scale effect。Paper §4.2 mechanism analysis。\\n\\n\\nSICA ≤ SC at all K 因为 MaxSAT over non-discriminative constraints 只注入噪声。 K=11 (odd) Δ=0 是关键: odd K 消除 SC ties, SICA 失去唯一有效机制 (tiebreaking), collapse to SC。Larger K (16, 20) 放大噪声注入——更多 traces → 更多 non-discriminative constraints → MaxSAT 更大概率排除正确答案。-5pp at K=12 和 -3.3pp at K=16/20 反映此噪声累积。All p>0.20 因 n=60 (SE≈5-6pp), 个体波动是 sampling noise 叠加在 true effect ≈ 0 之上。\\n\"\n  },\n  {\n    \"name\": \"tiebreak_baseline_analysis\",\n    \"description\": \"CPU-only: SICA vs SC-random vs SC-alphabetical vs SC-first-seen tiebreak 比较\",\n    \"results\": {\n      \"n_tied_questions\": 10,\n      \"pct_tied_of_total\": 0.167,\n      \"sica_tiebreak_accuracy\": 0.8,\n      \"random_tiebreak_accuracy\": 0.5,\n      \"alphabetical_tiebreak_accuracy\": 0.6,\n      \"first_seen_tiebreak_accuracy\": 0.4,\n      \"sica_net_gain_over_random_on_all_60\": 0.5\n    },\n    \"tables\": [\n      \"T4: Tiebreak Analysis (tied subset)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"回应 reviewer 'SICA is just a better tiebreaker'。Answer: yes, and an effective one, but ties are structurally rare at K=12. At odd K (exp-002 K=11), ties = 0, SICA≡SC。Even at even K, 80% × 17% = 1.3% net correct → <1pp overall。 Cost-benefit: 49% overhead (exp-009) for <1pp on tied subset = not worthwhile。\\n\\n\\nSICA 在 tied questions 上 80% 正确, 因为 constraint weighting 即使不判别 correct vs incorrect, 对 tie (两个 answer 票数相等) 仍能通过微弱信号打破平衡。但 tied questions 仅占 17% (K=12 even-K 才产生 tie)。10 题中多赢 3 题 (vs random) 对 60 题整体贡献 +0.5pp——在 SE≈6pp 的噪声中不可见。Random 50% 是理论 期望值; alphabetical 60% 反映答案选项 label 与正确答案的偶然相关; first-seen 40% 因为 model 首条 trace 并非最准确。\\n\"\n  },\n  {\n    \"name\": \"sica_constraint_ablation\",\n    \"description\": \"CPU-only ablation: MaxSAT vs count-only vs random-weight on exp-001 (n=804)\",\n    \"results\": {\n      \"n\": 804,\n      \"maxsat_accuracy\": 0.7649,\n      \"count_only_accuracy\": 0.7662,\n      \"random_weight_accuracy\": 0.7637,\n      \"sc_baseline_accuracy\": 0.7624,\n      \"agreement_802_of_804\": true,\n      \"maxsat_vs_count_mcnemar_p\": 0.99,\n      \"maxsat_vs_random_mcnemar_p\": 0.85,\n      \"maxsat_vs_sc_mcnemar_p\": 0.74,\n      \"all_pairwise_nonsignificant\": true\n    },\n    \"tables\": [\n      \"T3: Constraint Ablation (MaxSAT vs count-only vs random-weight vs SC)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Make-or-break evidence for capability trap mechanism。如果 MaxSAT ≈ count-only, solver 无附加值——constraints 没有 exploitable satisfiability structure。Combined with F2 (precision≈0.50), 形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Paper §4.1 核心机制结果。exp-013 + exp-019 共同构成 Claim 1 的 evidence base。\\n\\n\\nMaxSAT ≈ count-only 因为 constraint satisfiability 不携带判别信息。当 constraints 对正确/错误答案同等满足时, solver 的优化退化为计数: satisfiability structure 无 贡献。Random-weight ≈ MaxSAT 因为权重差异在 non-discriminative constraints 上是 纯噪声。802/804 题四种方法答案一致, 仅 2 题分歧 (互相抵消)。这直接证明 SAT 解算机制空洞化——是 capability trap 的 mechanism evidence。\\n\"\n  },\n  {\n    \"name\": \"sica_strategyqa_14b\",\n    \"description\": \"Qwen2.5-14B on StrategyQA 60q (K=12), commonsense reasoning domain\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.5667,\n      \"sc_accuracy\": 0.5333,\n      \"delta_pp\": 3.33,\n      \"mcnemar_p\": \">0.30\",\n      \"bootstrap_p\": 0.1346,\n      \"multi_candidate_rate\": 0.1,\n      \"extraction_rate_trace\": 0.704,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 0,\n      \"model\": \"Qwen2.5-14B-Instruct\",\n      \"dataset\": \"StrategyQA\"\n    },\n    \"tables\": [\n      \"T1: Main Results (StrategyQA × Qwen-14B row)\",\n      \"F3: Operating Regime Heatmap (StrategyQA × Qwen-14B cell)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"StrategyQA 结果挑战 best-case-diversity 假设: commonsense domain 并非 diversity 最高场景 (对强模型而言)。但强化 capability trap: 即使 C0 恰好产生少量 discordant, SICA 仍无显著优势。与 ARC (C0=5%) 和 PW+FOLIO (C0=38%) 形成三域覆盖。\\n\\n\\nStrategyQA C0=10% 远低于 plan 预期 (35-50%), 因为 14B 在 binary commonsense (yes/no) 上足够强, 大多数问题 12 traces 一致。仅 6 题多候选, 2 题 SICA 翻转正确。+3.33pp non-significant (n=60 SE≈6pp, bootstrap p=0.13)。Extraction rate 仅 70.4% (commonsense 推理链缺少可形式化逻辑结构), 进一步限制 SICA 操作空间。2:0 discordant ratio 看似 SICA 占优, 但 n=2 discordant pairs 无统计意义。\\n\"\n  },\n  {\n    \"name\": \"sica_arc_challenge_14b\",\n    \"description\": \"Qwen2.5-14B on ARC-Challenge 60q (K=12), 科学推理 4 选 1\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.95,\n      \"sc_accuracy\": 0.9667,\n      \"delta_pp\": -1.67,\n      \"multi_candidate_rate\": 0.05,\n      \"extraction_rate\": 1.0,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 1,\n      \"model\": \"Qwen2.5-14B-Instruct\",\n      \"dataset\": \"ARC-Challenge\"\n    },\n    \"tables\": [\n      \"T1: Main Results (ARC × Qwen-14B row)\",\n      \"F3: Operating Regime Heatmap (ARC × Qwen-14B cell)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ARC 是 14B 的 ceiling 域: SC 已达 96.7%, 无提升空间。SICA 微损 (-1.7pp) 因为 solver 在极少数 multi-candidate 问题上注入噪声。与 FOLIO (acc ~79%, C0 ~38%) 对比展示 capability-diversity 反向关系: high accuracy → low C0 → method degenerates。\\n\\n\\n14B 在 ARC-Challenge SC 高达 96.7%, C0 仅 5% (3 题多候选)。模型对 science 常识 足够自信, 12 traces 几乎总一致。唯一 discordant pair SC 赢——MaxSAT 排除了正确 答案的 constraint。4-choice format 理论上增加 diversity (更多选项), 但 14B 能力 过强, format 效应被 capability 压制。C0=5% 接近 QwQ-32B 退化阈值。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_correlation\",\n    \"description\": \"CPU-only: per-problem constraint precision vs vote_entropy (exp-001 n≈307 multi-candidate). F2 hero figure\",\n    \"results\": {\n      \"n_multi_candidate\": 307,\n      \"constraint_precision_mean\": 0.505,\n      \"constraint_precision_std\": 0.148,\n      \"constraint_precision_median\": 0.5,\n      \"precision_vs_entropy_slope\": 0.003,\n      \"precision_vs_entropy_r_squared\": 0.002,\n      \"precision_vs_entropy_p\": 0.42,\n      \"folio_precision_mean\": 0.512,\n      \"proofwriter_precision_mean\": 0.498,\n      \"cross_domain_precision_diff_p\": 0.6,\n      \"fraction_precision_below_040\": 0.28,\n      \"fraction_precision_above_060\": 0.25,\n      \"discordant_pair_sica_winrate_overall\": 0.48\n    },\n    \"tables\": [\n      \"T2: Constraint Quality Summary (precision by domain × model)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"F2 是论文 hero figure, 一图传达 capability trap: diversity (x) 存在且可变, 但 constraint quality (y) 恒为随机水平。'Regardless of diversity' 可视化为 slope=0。 与 T3 (MaxSAT≈count-only) 形成双重机制证据: (1) constraints 不判别 (F2), (2) solver 因此无法提取信号 (T3)。Per-problem granularity (n=307) 比 experiment-level correlation (n=7, r=0.15 p=0.74) 统计力强两个数量级, 是 D035 识别的 F2 data gap 的完整解决。\\n\\n\\nConstraint precision ≈ 0.50 (近随机) 因为 LLM 提取的 FOL constraints 捕获推理 trace 的表面结构 (变量命名、逻辑连接词模式) 而非深层语义正确性。正确和错误 traces 共享相似表面结构 (都使用 if-then/forall/exists), 导致 constraints 无法区分二者。 Slope ≈ 0 因为此限制是 structural 的: 无论 vote 分布多分散 (高 entropy) 或多集中 (低 entropy), constraint discriminative power 都不变——它取决于 extraction quality 而非 diversity level。FOLIO 和 ProofWriter precision 几乎相同 (0.512 vs 0.498, 差异 p=0.60), 说明跨域一致。28% 问题 precision<0.40 (constraints 反向判别), 25% precision>0.60 (偶然判别), 呈对称分布围绕 0.50。\\n\"\n  },\n  {\n    \"name\": \"sica_7b_scaling\",\n    \"description\": \"Qwen2.5-7B-Instruct on D012 60q. Within-Qwen weak model, high C0\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.533,\n      \"sc_accuracy\": 0.55,\n      \"delta_pp\": -1.7,\n      \"multi_candidate_rate\": 0.65,\n      \"extraction_rate\": 0.82,\n      \"answer_extraction_rate\": 0.88,\n      \"contradiction_rate\": 0.08,\n      \"discordant_sica_wins\": 2,\n      \"discordant_sc_wins\": 3,\n      \"mcnemar_p\": 0.65,\n      \"proofwriter_sica\": 0.5,\n      \"proofwriter_sc\": 0.533,\n      \"folio_sica\": 0.567,\n      \"folio_sc\": 0.567,\n      \"model\": \"Qwen2.5-7B-Instruct\"\n    },\n    \"tables\": [\n      \"T1 appendix: Qwen-7B row\",\n      \"F4: C0 vs Gap (7B 数据点: C0=65%, Δ=-1.7pp)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B 提供 within-Qwen scaling 的 high-diversity anchor。Combined with 14B (C0=53%) and 72B (C0≈15%), 三个 distinct C0 levels within single model family 成立 (c0_scaling_distinct_levels=3)。C0 与 model scale 反向 (7B→65%, 14B→53%, 72B→15%) 验证 C0 as capability proxy。但 SICA-SC gap 在三个 scale 都 ≈ 0, 证明 C0 是 necessary but insufficient。For Claim 3: C0=65% + Δ=-1.7pp 是 'high C0 but no gain' 的最强数据点。\\n\\n\\n7B 在 formal logic 上显著弱于 14B (SC 55% vs 73%), 产生大量 answer disagreement (C0=65%)。但更弱模型也提取更差 constraints: extraction_rate 89%→82%, contradiction_rate 2.2%→8%。高 C0 意味着更多 multi-candidate 问题可操作, 但 constraints 质量更差意味着 MaxSAT 优化方向更随机。5 discordant pairs 中 SC 赢 3 个: MaxSAT 在 noisy constraints 上更大概率排除正确答案。 这完美展示 capability trap weak-model 端: diversity abundant, quality absent。\\n\"\n  },\n  {\n    \"name\": \"qwq_32b_operating_regime\",\n    \"description\": \"QwQ-32B negative results: C0<5%, SICA≡SC. CPU-only格式化 MVP 已有数据\",\n    \"results\": {\n      \"total_problems\": 46,\n      \"qwq_c0_nominal_pct\": 10.3,\n      \"qwq_c0_effective_pct\": 2.6,\n      \"qwen14b_c0_pct\": 46.0,\n      \"diversity_ratio\": 17.7,\n      \"aime_delta_pp\": 0.0,\n      \"aime_n\": 22,\n      \"proofwriter_delta_pp\": -5.9,\n      \"proofwriter_n\": 17,\n      \"folio_n\": 2,\n      \"c0_below_20_threshold\": true,\n      \"sica_structurally_degenerate\": true\n    },\n    \"tables\": [\n      \"T1: Main Results (QwQ-32B row, all cells 'SICA≡SC')\",\n      \"F3: Operating Regime Heatmap (QwQ-32B column 全灰)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"QwQ-32B 是 Claim 2 'operating regime empty' 的一极: full reasoning → no diversity → method degenerates。对称地, instruction models 展示另一极: high diversity → no constraint quality → method fails。No model hits the sweet spot。C0=2.6% 远低于 20% 阈值, 直接支撑 Claim 3 early-stopping criterion。\\n\\n\\nQwQ-32B 作为 full reasoning model, deterministic chain-of-thought 压制 sampling diversity: 即使 T=0.7, 12 traces 几乎总产生相同答案 (effective C0=2.6%)。AIME 22 题 0% multi-candidate (完全一致)。Nominal C0=10.3% vs effective C0=2.6% 的差距来自 answer extraction 格式噪声 (如 \\\"30\\\" vs \\\"30.0\\\"), 非真实 reasoning divergence。 ProofWriter -5.9pp 是 n=17 噪声 (SE≈12pp)。QwQ-32B 展示 capability trap strong- reasoning 端: model 足够强 → 无 diversity → SICA 结构性退化为 SC。\\n\"\n  },\n  {\n    \"name\": \"c0_diagnostic_validation\",\n    \"description\": \"CPU-only: C0 vs SICA-SC gap 散点, 跨所有 models/K/domains, 验证 C0 as predictor\",\n    \"results\": {\n      \"n_conditions\": 14,\n      \"c0_range_pct\": [\n        2.6,\n        65.0\n      ],\n      \"gap_range_pp\": [\n        -3.3,\n        6.67\n      ],\n      \"regression_slope\": -0.02,\n      \"regression_r_squared\": 0.06,\n      \"regression_p\": 0.4,\n      \"c0_below_5_n\": 3,\n      \"c0_below_5_mean_abs_gap\": 0.6,\n      \"c0_above_20_n\": 8,\n      \"c0_above_20_mean_gap\": 0.1,\n      \"c0_above_20_all_p_gt_010\": true,\n      \"distinct_c0_levels_qwen_family\": 3,\n      \"distinct_c0_levels_all_models\": 5\n    },\n    \"tables\": [\n      \"F4: C0 vs Gap (所有条件)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"F4 是 Claim 3 核心 figure。Bifurcation 清晰: C0<5% → degenerate (grey), C0>20% → trapped (red), no sweet spot。理论上界展示 SICA 在 C0=50% 时应有 5-10pp gain if constraints discriminative——this unrealized potential IS the trap。 C0 因此是 zero-cost early stopping criterion: compute C0, if <20% stop (method degenerate), if >20% stop (trap guarantees no gain)。Either way, don't proceed。\\n\\n\\nC0 与 gap 无线性关系 (r²=0.06, p=0.40) 因为 gap 在所有 C0 水平围绕 0 波动。 C0<5% 条件 (QwQ-32B 2.6%, ARC-14B 5%, StrategyQA-14B 10%) SICA≡SC: 方法 结构性退化。C0>20% 条件 (Qwen-7B 65%, LLaMA-8B 62%, DeepSeek-R1-7B 58%, Mistral 50%, Qwen-14B 53%) mean gap≈0: diversity 存在但 constraints 不判别。 Within-Qwen 三水平 (15%/53%/65%) + DeepSeek (58%) + LLaMA (62%) ≈ 5 distinct levels。F4 展示理论上界 vs 实际数据的 gap = capability trap 的视觉量化。\\n\"\n  },\n  {\n    \"name\": \"sica_72b_awq\",\n    \"description\": \"Qwen2.5-72B-Instruct-AWQ on D012 60q. Within-Qwen strong model, low C0\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.867,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.15,\n      \"extraction_rate\": 0.93,\n      \"answer_extraction_rate\": 1.0,\n      \"contradiction_rate\": 0.01,\n      \"discordant_sica_wins\": 1,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 1.0,\n      \"proofwriter_sica\": 0.833,\n      \"proofwriter_sc\": 0.833,\n      \"folio_sica\": 0.9,\n      \"folio_sc\": 0.9,\n      \"model\": \"Qwen2.5-72B-Instruct-AWQ\"\n    },\n    \"tables\": [\n      \"T1 appendix: Qwen-72B row\",\n      \"F4: C0 vs Gap (72B 数据点: C0=15%, Δ=0)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B 是 within-Qwen scaling 的 low-diversity anchor。三点连线清晰展示 C0 随 model scale 单调递减 (65%→53%→15%) 但 gap 恒为 ≈0。这证明 'even when you scale up within a family, you trade diversity for accuracy without ever hitting the sweet spot'。72B extraction quality 最高 (93%, 1% contradiction) 佐证 strong model → better constraints, 但 futile when C0 is low。\\n\\n\\n72B SC accuracy 高达 86.7%, C0 仅 15% (9 题多候选)。能力强到大部分问题 12 traces 一致。Extraction_rate 高 (93%), contradiction_rate 极低 (1%)——72B 的 constraints 质量确实更好。但 C0 太低, 没有足够 multi-candidate 问题让 SICA 操作。 仅 ~2 discordant pairs, 各赢一题, 净 Δ=0。AWQ 4-bit quantization 可能引入 微量额外噪声, 使 C0 略高于 full-precision 72B (否则可能 C0<10%), 但仍远低于 14B。这是 capability trap strong-model 端: quality improves but diversity vanishes。\\n\"\n  },\n  {\n    \"name\": \"overhead_analysis\",\n    \"description\": \"exp-001 Wall-time breakdown: trace generation, constraint extraction, MaxSAT\",\n    \"results\": {\n      \"n\": 804,\n      \"mean_total_wall_s\": 61.6,\n      \"mean_trace_gen_s\": 31.6,\n      \"trace_gen_pct\": 51.3,\n      \"mean_extract_s\": 29.0,\n      \"extract_pct\": 47.0,\n      \"mean_dedup_s\": 1.0,\n      \"dedup_pct\": 1.6,\n      \"mean_maxsat_s\": 0.003,\n      \"maxsat_pct\": 0.005,\n      \"sica_overhead_over_sc_pct\": 48.7,\n      \"p50_overhead_pct\": 48.9,\n      \"p90_overhead_pct\": 57.6\n    },\n    \"tables\": [\n      \"Appendix: Overhead breakdown table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"回应 reviewer 'is the overhead worth it': 不值得。49% overhead = 零精度收益。 SC 是 Pareto dominant (same accuracy, half the cost)。Solver time <0.01% 表明 MaxSAT formulation 计算效率不是问题——问题在于输入质量。This strengthens practical guidance: even if future work improves constraint quality, the extraction cost remains substantial。\\n\\n\\nSICA 相比 SC 增加 ~49% wall time, 几乎全部来自 constraint extraction (一次额外 LLM inference pass per trace, 解析 FOL)。MaxSAT solver 本身极快 (0.003s, <0.01% 总时间)——瓶颈不在 solver complexity 而在 extraction cost。如果 constraints 是 discriminative 的, 49% overhead 可能值得 (每 query 多花 30s 换 5pp+ accuracy); 但 Δ≈0 意味着 49% 额外计算换零收益。P90 overhead 57.6% 来自长 traces (FOLIO domain), extraction 时间与 trace 长度成正比。\\n\"\n  },\n  {\n    \"name\": \"sica_llama_8b\",\n    \"description\": \"LLaMA-3.1-8B-Instruct on D012 60q. 第三 instruction-scale 家族\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.6667,\n      \"sc_accuracy\": 0.6,\n      \"delta_pp\": 6.67,\n      \"multi_candidate_rate\": 0.617,\n      \"extraction_rate\": 0.856,\n      \"answer_extraction_rate\": 0.896,\n      \"contradiction_rate\": 0.053,\n      \"truncated_traces\": 44,\n      \"discordant_sica_wins\": 5,\n      \"discordant_sc_wins\": 1,\n      \"mcnemar_p\": 0.22,\n      \"model\": \"LLaMA-3.1-8B-Instruct\"\n    },\n    \"tables\": [\n      \"T1: Main Results (LLaMA-8B D012 row)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-011 的 +6.67pp 是全研究最大正 delta, 但 exp-019/020 (同模型 n=200+) 展示 true effect ≈ 0。Paper framing: 'small-sample positive signal does not survive powered replication'——本身是方法论 lesson。LLaMA-8B 作为第三 instruction-scale family (加 Qwen/Mistral), 满足 EMNLP 三家族最低门槛。\\n\\n\\nLLaMA-8B C0=62%, SC=60% (instruction-scale models 中最弱)。+6.67pp 是 n=60 采样噪声: SE≈6pp, 1.1σ deviation, p=0.22 non-significant。5:1 discordant ratio 看似强烈, 但绝对数量小 (6 pairs)。关键验证来自同模型更大 n: exp-019 (StrategyQA n=200, Δ=+2.0pp p=0.42) 和 exp-020 (FOLIO n=204, Δ=-2.45pp p=0.27) 确认 true effect 接近 0。正 delta 与 负 delta 在不同 domains 交替出现 = 纯噪声。 44/720 truncated traces 因 8B context limit, 但 truncation 对 SICA/SC 影响对称。\\n\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_14b\",\n    \"description\": \"Qwen2.5-14B on GSM8K 30q pilot (K=12). 数学推理域覆盖\",\n    \"results\": {\n      \"n\": 30,\n      \"k\": 12,\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.867,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.1,\n      \"extraction_rate\": 0.75,\n      \"answer_extraction_rate\": 0.95,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 0,\n      \"model\": \"Qwen2.5-14B-Instruct\",\n      \"dataset\": \"GSM8K\"\n    },\n    \"tables\": [\n      \"Appendix: Cross-domain (GSM8K row)\",\n      \"F4: C0 vs Gap (GSM8K point)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K 确认: 当模型在目标 domain 足够强时, C0 自然低, SICA 无操作空间。 Extraction rate 75% (vs logic domain 89%) 说明 domain 影响 extraction feasibility。 Appendix material, 回应 'what about math reasoning' 的 reviewer。\\n\\n\\n14B 在 GSM8K accuracy ~87%, C0 ≈ 10%。开放式数学答案 (具体数字) 理论上有更大 answer space, 但模型能力足以收敛到正确数值。Extraction rate 偏低 (75%) 因为数值 计算步骤难以 FOL 形式化 (例 \\\"3×5+2=17\\\" → FOL 表达不自然)。0 discordant pairs → SICA ≡ SC on all 30 题。C0≈10% 类似 ARC/StrategyQA: 14B 在 'easier' domains 上能力过强, diversity 不足。\\n\"\n  },\n  {\n    \"name\": \"sica_deepseek_r1_llama_8b\",\n    \"description\": \"DeepSeek-R1-Distill-Qwen-7B on D012 60q. Distilled reasoning model 行为验证\",\n    \"results\": {\n      \"n\": 60,\n      \"k\": 12,\n      \"sica_accuracy\": 0.683,\n      \"sc_accuracy\": 0.717,\n      \"delta_pp\": -3.33,\n      \"multi_candidate_rate\": 0.583,\n      \"extraction_rate\": 0.839,\n      \"answer_extraction_rate\": 0.939,\n      \"truncated_traces\": 72,\n      \"contradiction_rate\": 0.037,\n      \"discordant_sica_wins\": 0,\n      \"discordant_sc_wins\": 2,\n      \"mcnemar_p\": 0.48,\n      \"model\": \"DeepSeek-R1-Distill-Qwen-7B\"\n    },\n    \"tables\": [\n      \"T1: Main Results (DeepSeek-R1-7B row)\",\n      \"Appendix: Reasoning model comparison (QwQ C0=2.6% vs DeepSeek C0=58.3%)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-014 解决分类问题: DeepSeek-R1-7B 归入 instruction-scale (C0=58%) 非 reasoning (C0<5%)。Model taxonomy 应以行为 (C0 水平) 而非训练方法定义。Paper 重分类 DeepSeek-R1-7B 为 'instruction-scale with reasoning-style training', 避免 reviewer 'only one reasoning model' 攻击。QwQ-32B remains sole full reasoning model。\\n\\n\\n关键发现: C0=58.3%, 行为完全像 instruction-scale model, 非 plan 预期的 reasoning model (C0<5%)。7B 参数量不足以维持 R1 的 deterministic reasoning chain——蒸馏后 小模型在 7B 容量下退化为高 diversity 行为。Δ=-3.33pp: 2 discordant pairs SC 全赢, MaxSAT constraint 排除恰好排错。Truncated traces 最多 (72/720), 因 R1 风格长 reasoning + 7B context 限制。结论: distilled reasoning ≠ full reasoning, 参数量是决定性因素, 非训练方法。\\n\"\n  },\n  {\n    \"name\": \"logic_lm_baseline\",\n    \"description\": \"Logic-LM × K: single-trace FOL verification K 次后 vote, CPU-only on FOLIO\",\n    \"results\": {\n      \"n\": 204,\n      \"k\": 12,\n      \"logic_lm_k_accuracy\": 0.789,\n      \"sc_accuracy\": 0.794,\n      \"sica_accuracy\": 0.794,\n      \"logic_lm_vs_sc_delta_pp\": -0.5,\n      \"logic_lm_vs_sica_delta_pp\": -0.5,\n      \"verification_pass_rate\": 0.92,\n      \"verification_discriminative\": false,\n      \"mcnemar_logic_lm_vs_sc_p\": 0.82\n    },\n    \"tables\": [\n      \"Appendix: Logic-LM × K baseline comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"回应 reviewer 'compare to Logic-LM/LINC'。Answer: Logic-LM-K 也 ≈ SC, 因为 bottleneck 是 extraction quality 非 aggregation method。Single-trace verification 也失败, 因为 underlying constraints non-discriminative。This generalizes the capability trap beyond SICA to any FOL-constraint-based method。\\n\\n\\nLogic-LM-K 将每条 trace 独立验证 (extract FOL → solver check → pass/fail) 后 majority vote。Accuracy ≈ SC 因为 verification pass rate 极高 (92%): solver 对 大部分 traces 返回 satisfiable, 无论 trace 是否正确。原因同 SICA: constraints 不判别。'Verification' 退化为 'format check'——只要 FOL syntax 正确 solver 就 pass。这消除 'maybe aggregation is the problem, single-trace verification works better' 反论。瓶颈是 constraint quality, 非 aggregation architecture。\\n\"\n  },\n  {\n    \"name\": \"weighted_sc_baseline\",\n    \"description\": \"Weighted SC (Taubenfeld 2024 style): uniform/inv-length/length/constraint-count on exp-001\",\n    \"results\": {\n      \"n\": 804,\n      \"sc_uniform_accuracy\": 0.7624,\n      \"sica_maxsat_accuracy\": 0.7649,\n      \"inv_length_accuracy\": 0.7674,\n      \"length_weighted_accuracy\": 0.7525,\n      \"constraint_count_accuracy\": 0.7525,\n      \"inv_length_vs_sc_p\": 0.453,\n      \"length_vs_sc_p\": 0.153,\n      \"inv_length_vs_sica_p\": 0.864,\n      \"all_nonsignificant\": true\n    },\n    \"tables\": [\n      \"Appendix: Weighted SC comparison table\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Weighted SC 是最直接竞争 baseline。All variants ≈ SC 确认: (1) 无简单 weighting 能 rescue method, (2) bottleneck 是 signal quality 非 aggregation sophistication。 SICA 失败不是因为 MaxSAT over-engineering, 而是因为 input signals (constraints) non-discriminative。Any aggregation over non-discriminative signals degenerates to counting, which ≈ voting。\\n\\n\\n所有 weighting 方案 ≈ SC, 因为 trace-level 信号 (长度、constraint 数量) 同样 不具判别性。Inv-length 略高 (+0.50pp, p=0.45): shorter traces 可能稍 more focused, 但效果不显著。Length-weighted 和 constraint-count 略低 (-1pp): longer/more-constrained traces 未必更正确 (可能是 model 在错误路径上 elaborating)。关键 insight: 简单 weighting 也无法修复 non-discriminative 信号, 因为问题在底层信号质量而非权重方案。\\n\"\n  },\n  {\n    \"name\": \"constraint_quality_case_studies\",\n    \"description\": \"8 representative problems 定性分析: constraints 为何 non-discriminative\",\n    \"results\": {\n      \"n_case_studies\": 8,\n      \"correct_trace_precision\": 0.52,\n      \"incorrect_trace_precision\": 0.48,\n      \"constraint_overlap_rate\": 0.78,\n      \"typical_constraint_types\": [\n        \"conditional (if-then)\",\n        \"universal quantifier (forall)\",\n        \"negation\",\n        \"predicate application\"\n      ],\n      \"discriminative_constraints_pct\": 0.12\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Case studies 提供定性理解, 补充 F2 定量证据。Reader 直观看到 WHY precision ≈ 0.50: constraints capture what the model reads (premises), not how it reasons (inference)。 也解释 WHY MaxSAT ≈ count-only: 如果 constraints mostly shared, satisfiability structure carries no information about answer correctness。1-2 examples 进 §4.1, 其余进 appendix。\\n\\n\\nNon-discrimination 的 root cause: LLM 提取的 constraints 主要 formalize 题目 premises (前提条件) 而非 reasoning steps (推理步骤)。Premises 对正确/错误 traces 共享 (都正确读取了题目)——constraint overlap rate 78%。推理错误发生在 inference chain 更深位置: 这些错误要么不被 formalized (extraction 跳过复杂推导), 要么被 formalized 为看起来合理但语义不同的 constraints (surface structure 相似)。 仅 12% constraints 是 truly discriminative (只出现在正确或只出现在错误 traces), 且方向随机 (一半 favor correct, 一半 favor incorrect)。\\n\"\n  },\n  {\n    \"name\": \"temperature_ablation_t03_t05_t10\",\n    \"description\": \"T=0.3/0.5/1.0 on Qwen-14B D012 60q. Temperature 操控 diversity, 验证 trap 结构性\",\n    \"results\": {\n      \"dataset\": \"D012\",\n      \"model\": \"Qwen2.5-14B-Instruct\",\n      \"n\": 60,\n      \"k\": 12,\n      \"t03_c0_pct\": 28.3,\n      \"t03_sc_accuracy\": 0.767,\n      \"t03_sica_accuracy\": 0.767,\n      \"t03_delta_pp\": 0.0,\n      \"t03_discordant_sica\": 1,\n      \"t03_discordant_sc\": 1,\n      \"t03_mcnemar_p\": 1.0,\n      \"t03_extraction_rate\": 0.91,\n      \"t05_c0_pct\": 41.7,\n      \"t05_sc_accuracy\": 0.75,\n      \"t05_sica_accuracy\": 0.75,\n      \"t05_delta_pp\": 0.0,\n      \"t05_discordant_sica\": 1,\n      \"t05_discordant_sc\": 1,\n      \"t05_mcnemar_p\": 1.0,\n      \"t05_extraction_rate\": 0.9,\n      \"t10_c0_pct\": 68.3,\n      \"t10_sc_accuracy\": 0.7,\n      \"t10_sica_accuracy\": 0.683,\n      \"t10_delta_pp\": -1.7,\n      \"t10_discordant_sica\": 1,\n      \"t10_discordant_sc\": 2,\n      \"t10_mcnemar_p\": 0.56,\n      \"t10_extraction_rate\": 0.87,\n      \"baseline_t07_c0_pct\": 53.3,\n      \"baseline_t07_delta_pp\": 0.0,\n      \"c0_monotonic_increase\": true,\n      \"c0_sequence\": \"28.3% → 41.7% → 53.3% → 68.3%\",\n      \"max_abs_delta_pp\": 1.7,\n      \"all_p_gt_020\": true\n    },\n    \"tables\": [\n      \"§5 Table: Temperature ablation (T × C0 × SC × SICA × Δ)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Temperature ablation 是论文最强 causal evidence: 通过实验操控 diversity (非仅 跨模型观察), 确认 diversity↑ 不改善 SICA。排除 confounders: 同一模型、同一数据、 只改 T, C0 从 28% 到 68% 连续变化, gap 恒为 0。如 reviewer 问 'maybe you haven't found the right diversity level': this answers definitively — we swept the full range, it doesn't help。与 F2 互补: F2 shows WHY (precision≈0.50), temp ablation shows THAT (gap=0 at all diversity levels)。§5 new evidence for EMNLP submission。\\n\\n\\nTemperature 直接控制 sampling distribution entropy, 因此 C0 随 T 单调递增: T=0.3 时 logit distribution 尖锐, traces 集中到 modal answer, 仅 17 题多候选; T=1.0 时分布平坦, 41 题多候选。这是 structural: T→entropy→C0 是因果链。\\nSC accuracy 随 T 先平后降: T=0.3-0.7 SC≈73-77% (集中在正确答案近邻), T=1.0 SC 降到 70% (更多随机错误破坏多数票)。已知 SC behavior。\\nSICA-SC gap 在所有 T 下 |Δ| ≤ 1.7pp: - T=0.3 (C0=28%): 仅 17 题多候选, 1 discordant, 1:1 → Δ=0。少数 multi-candidate\\n  问题上 constraints 恰好一胜一负。\\n- T=0.5 (C0=42%): 25 题多候选, constraints 仍 non-discriminative → Δ=0。\\n  更多 problems 可操作, 但操作方向随机。\\n- T=1.0 (C0=68%): 41 题多候选, constraints 质量因 noisier traces 进一步下降\\n  (高温 traces 更长、更散漫, extraction noise 增加) → Δ=-1.7pp。MaxSAT 在\\n  嘈杂 constraints 上做了一次净错误排除。\\n\\nAll p>0.20 at n=60 (SE≈5-6pp)。True effect = 0 at all temperatures。\\n\"\n  },\n  {\n    \"name\": \"gsm8k_pilot_30q\",\n    \"description\": \"等同 exp-012。Qwen-14B on GSM8K 30q, 数学推理域 pilot\",\n    \"results\": {\n      \"note\": \"同 exp-012, 参见上方 gsm8k_pilot_14b entry\",\n      \"n\": 30,\n      \"k\": 12,\n      \"sica_accuracy\": 0.867,\n      \"sc_accuracy\": 0.867,\n      \"delta_pp\": 0.0,\n      \"multi_candidate_rate\": 0.1,\n      \"extraction_rate\": 0.75,\n      \"model\": \"Qwen2.5-14B-Instruct\",\n      \"dataset\": \"GSM8K\"\n    },\n    \"tables\": [\n      \"Appendix: GSM8K row (同 exp-012)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"与 exp-012 完全重复。收录条件: 如果 GPU budget 允许, 作为第四个 domain 进入 appendix (主文已有 FOLIO + StrategyQA + ARC + ProofWriter 四域)。\\n\\n与 exp-012 相同实验。14B 在 GSM8K accuracy ~87%, C0 ~10%。数学推理的 open-ended answer space (具体数字) 理论上增加 diversity, 但 14B 能力收敛到正确数值。 Extraction rate 偏低 (75%) 因为数值计算难以 FOL 化。SICA ≡ SC。 作为 appendix cross-domain data point, 为 'what about math' reviewer concern 提供证据。\\n\"\n  }\n]",
      "numLines": 485,
      "startLine": 1,
      "totalLines": 485
    }
  },
  "sourceToolAssistantUUID": "e6046c91-c636-46d6-ae3a-f7e377b1d599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T15:26:11.693Z_

<details><summary>↩ Tool result · `toolu_01Deos7cFCwUs4zAcHGtn2xC`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)
8	
9	1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).
10	2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
11	3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.
12	
13	## Core Insight
14	Symbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.
15	
16	## Story Spine
17	- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
18	- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
19	- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.
20	- **Headline result**: "Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level."
21	
22	## Anticipated Reviewer Concerns & Defensive Experiments
23	1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
24	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
25	3. **"Only Qwen models"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B
26	4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
27	5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
28	6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
29	7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
30	8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
31	9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
32	10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
33	11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
34	12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.
35	
36	## Working Title
37	**"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"**
38	(Alternatives: 
39	- "When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why"
40	- "Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation")
41	
42	## Paper Structure (EMNLP 8pp + appendix)
43	- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)
44	- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)
45	- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data
46	
47	## Claim Risk Notes (Updated D035 + exp-014)
48	- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
49	- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
50	- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator". Need exp-004/007 for gradient data. OPEN.
51	- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
52	- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.
53	
54	## Venue Fit Risks
55	- EMNLP: Negative-results/analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic + overhead analysis.
56	- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
57	- Statistical power: Now strong (N>1,200 combined across powered tests).
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef2807ea-12d5-4d4c-aa9a-1ddcd2dec626",
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "4713dfd0-0ca4-469b-9893-ee653eb827d8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md",
      "content": "# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n\n## Working Title\n**\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"**\n(Alternatives: \n- \"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\"\n- \"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\". Need exp-004/007 for gradient data. OPEN.\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  },
  "sourceToolAssistantUUID": "ef2807ea-12d5-4d4c-aa9a-1ddcd2dec626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:26:11.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Deos7cFCwUs4zAcHGtn2xC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8281642-546c-4406-9679-29953018ab40",
  "isSidechain": false,
  "requestId": "req_011Cb8NgovaFedo7xHqkEciJ",
  "type": "assistant",
  "uuid": "ef2807ea-12d5-4d4c-aa9a-1ddcd2dec626",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzCqb4gFCcXT4eRGi1enSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12723,
      "cache_read_input_tokens": 11841,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 229,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12723
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_con…",
  "leafUuid": "4713dfd0-0ca4-469b-9893-ee653eb827d8",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic invariant consensus paper",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Assistant

_source line 14 · 2026-05-17T15:26:43.535Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the experimental data and the paper framing. Let me write a complete LaTeX paper that covers:

1. Abstract
2. Introduction
3. Related Work
4. Method (SICA pipeline description)
5. Experiments (covering all the experiment data)
6. Analysis/Discussion (the capability trap mechanism)
7. Conclusion

Let me structure the paper according to the framing document:
- Title: "The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"
- Three core claims


- Main Tables: T1, T2, T3, T4
- Main Figures: F1, F2, F3, F4
- Temperature ablation in §5

I need to be careful to use the exact numbers from experiment_data.json, follow proper paper writing conventions, and organize the experiments into sections covering the SICA pipeline description, main results, and ablation studies. Writing the full LaTeX now... Looking at the baseline comparisons and overhead analysis, then reconsidering the paper structure against the framing document to ensure the main tables and figures align with the narrative flow—I need to organize this as a clean progression through abstract, introduction, related work, the SICA method, and then experiments starting with setup.

The key insight from the narrative guidance is that temperature ablation should be its own section (§5), so I'm restructuring to pull that out as a dedicated section rather than nesting it under experiments. This means the main results and mechanism analysis sit in §4, temperature ablation gets §5, and then discussion covers the baseline comparisons, overhead, tiebreak analysis, and case studies. Now I'm mapping out all the experimental results I need to weave into the paper—the K sensitivity analysis, tiebreak baseline comparisons, constraint ablations, main results across StrategyQA and ARC, the constraint quality correlation figure, scaling experiments with the 7B model, the negative control with QwQ-32B, and the diagnostic validation data—making sure each finding gets placed in the appropriate section to build the narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4713dfd0-0ca4-469b-9893-ee653eb827d8",
  "isSidechain": false,
  "requestId": "req_011Cb8Nh7raj4u7WsDuVqvAQ",
  "type": "assistant",
  "uuid": "80d2a5bb-d8c7-4417-a018-d5eae6b1bd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLZGkXCxpfwNAsYXY6rxaC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16485,
      "cache_read_input_tokens": 24564,
      "output_tokens": 1659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1659,
          "cache_read_input_tokens": 24564,
          "cache_creation_input_tokens": 16485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16485
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

_source line 15 · 2026-05-17T15:26:43.537Z_

I'll read the files and write the complete paper. Let me first check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80d2a5bb-d8c7-4417-a018-d5eae6b1bd83",
  "isSidechain": false,
  "requestId": "req_011Cb8Nh7raj4u7WsDuVqvAQ",
  "type": "assistant",
  "uuid": "685db51e-618b-4e82-9697-1ba2ef7daed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLZGkXCxpfwNAsYXY6rxaC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16485,
      "cache_read_input_tokens": 24564,
      "output_tokens": 1659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1659,
          "cache_read_input_tokens": 24564,
          "cache_creation_input_tokens": 16485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16485
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

_source line 16 · 2026-05-17T15:26:45.780Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DJWzmBu9eBye6vzj5iPAcB`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "685db51e-618b-4e82-9697-1ba2ef7daed1",
  "isSidechain": false,
  "requestId": "req_011Cb8Nh7raj4u7WsDuVqvAQ",
  "type": "assistant",
  "uuid": "19f6a15b-48bc-4d83-83d4-999833baa51f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLZGkXCxpfwNAsYXY6rxaC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16485,
      "cache_read_input_tokens": 24564,
      "output_tokens": 1659,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1659,
          "cache_read_input_tokens": 24564,
          "cache_creation_input_tokens": 16485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16485
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

_source line 17 · 2026-05-17T15:26:45.993Z_

<details><summary>↩ Tool result · `toolu_01DJWzmBu9eBye6vzj5iPAcB`</summary>

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
  "parentUuid": "19f6a15b-48bc-4d83-83d4-999833baa51f",
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "68ba36c7-35b3-4234-858b-a895e50b17e5",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "19f6a15b-48bc-4d83-83d4-999833baa51f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-17T15:26:49.157Z_

Now writing the complete LaTeX paper based on the experiment data and framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68ba36c7-35b3-4234-858b-a895e50b17e5",
  "isSidechain": false,
  "requestId": "req_011Cb8NjeLT6sXR6ibg49h76",
  "type": "assistant",
  "uuid": "539ff736-9d9c-4839-a689-59e3c6369703",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URc4r1qBMBUvpxePu5Q37c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 41049,
      "output_tokens": 9512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9512,
          "cache_read_input_tokens": 41049,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1685
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

_source line 19 · 2026-05-17T15:29:50.380Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QZcbaYPRymSmVdjW4MfjVp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\title{The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% =============================================================\n%% ABSTRACT\n%% =============================================================\n\\begin{abstract}\nSymbolic consensus methods augment Large Language Model (LLM) reasoning by extracting first-order logic (FOL) constraints from multiple reasoning traces and selecting answers via MAX-SAT optimization. We present the first systematic study asking \\emph{when} such methods improve over simple majority voting (Self-Consistency, SC). Across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model (combined $N{>}1{,}300$ problems), we find that symbolic consensus provides no significant accuracy gain over SC. We identify the structural cause: a \\textbf{capability trap}. Instruction-scale models produce abundant output diversity (candidate disagreement rate $C_0{=}38$--$65\\%$), yet the extracted constraints achieve only random-level discriminative precision ($\\approx 0.50$). MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, confirmed by an ablation showing MAX-SAT $\\approx$ count-only $\\approx$ random-weight (802/804 identical answers, McNemar $p{=}0.99$). A temperature ablation causally manipulates diversity from $C_0{=}28\\%$ to $68\\%$, with the accuracy gap remaining zero at every level ($|\\Delta|{\\leq}1.7$pp, all $p{>}0.30$). Full reasoning models avoid the trap only by eliminating diversity entirely ($C_0{<}5\\%$), making symbolic methods structurally degenerate. We propose $C_0$ as a zero-cost early stopping criterion: if $C_0{<}5\\%$, the method is degenerate; if $C_0{>}20\\%$, the capability trap guarantees no gain.\n\\end{abstract}\n\n%% =============================================================\n%% 1. INTRODUCTION\n%% =============================================================\n\\section{Introduction}\n\nSelf-Consistency (SC) aggregates multiple LLM reasoning traces by majority voting over extracted answers. Recent work proposes replacing this simple aggregation with symbolic methods: extracting formal constraints from each trace and using satisfiability solvers to select the maximally consistent answer. The intuition is compelling. When traces disagree, a solver that reasons about logical structure should outperform naive counting. But does it?\n\nThis question has practical urgency. Symbolic consensus adds computational overhead (we measure 49\\% wall-time increase) and engineering complexity. Practitioners need guidance on when this investment pays off. Prior work evaluates symbolic reasoning pipelines on individual benchmarks without systematically characterizing the conditions under which they provide gains over majority voting.\n\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation): extract FOL constraints from each trace, formulate a weighted MAX-SAT problem, and select the answer whose traces maximize total satisfied constraint weight. We evaluate SICA across 3 reasoning domains (formal logic, commonsense, science), 4 instruction-scale model families (Qwen, LLaMA, Mistral, DeepSeek-R1-Distill), and 1 full reasoning model (QwQ-32B), totaling over 1,300 problem instances across powered experiments.\n\nOur central finding is negative: SICA provides no significant accuracy gain over SC in any tested condition. The largest positive signal ($+6.67$pp with LLaMA-8B, $n{=}60$) does not survive powered replication ($n{=}200$: $\\Delta{=}+2.0$pp, $p{=}0.42$). Five model families show $|\\Delta|{\\leq}6.67$pp with zero significant results. We identify the structural cause, which we term the \\textbf{capability trap}: symbolic consensus requires both output diversity (disagreement to resolve) and discriminative constraints (to resolve correctly), but no model simultaneously satisfies both requirements.\n\nWe make three contributions:\n\\begin{enumerate}\n\\item \\textbf{Mechanism identification.} We show that LLM-extracted constraints achieve random-level precision ($0.505 \\pm 0.148$, $n{=}307$ problems) regardless of diversity level (regression slope $= 0.003$, $r^2 < 0.01$). MAX-SAT optimization thus degenerates to counting, confirmed by the ablation MAX-SAT $\\approx$ count-only $\\approx$ random-weight.\n\\item \\textbf{First systematic negative result.} Five model families (combined $N{>}1{,}300$) all show SICA $\\approx$ SC. A temperature ablation causally confirms the trap is structural, not a tuning failure.\n\\item \\textbf{Zero-cost diagnostic.} We propose $C_0$ (candidate disagreement rate) as a practitioner-facing early stopping criterion that requires no additional compute beyond standard SC.\n\\end{enumerate}\n\n%% =============================================================\n%% 2. RELATED WORK\n%% =============================================================\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and voting methods.}\n\\citet{wang2023selfconsistency} introduced SC as a decoding strategy that samples diverse reasoning paths and marginalizes over answers. Universal SC \\citep{chen2023universal} extends this to free-form generation by clustering. Weighted SC variants \\citep{taubenfeld2024} assign trace-level confidence scores before voting. We compare against multiple weighting schemes (inverse-length, length-based, constraint-count) and find all equivalent to uniform voting when the underlying signals lack discriminative power.\n\n\\paragraph{Symbolic reasoning augmentation.}\nLogic-LM \\citep{pan2023logiclm} translates NL problems to symbolic form for solver verification. LINC \\citep{olausson2023linc} uses FOL translation with theorem provers. These methods apply symbolic verification to single traces. SICA extends the paradigm to multi-trace aggregation: rather than verifying one trace, it extracts constraints from all $K$ traces and selects the answer maximizing joint satisfiability. We show that multi-trace symbolic aggregation faces the same bottleneck as single-trace verification: constraint quality is the binding limitation.\n\n\\paragraph{Outcome and process reward models.}\nORM \\citep{cobbe2021gsm8k} and PRM \\citep{lightman2023lets} train verifiers to score reasoning steps. These learned methods require training data for each domain. Symbolic consensus promises domain-general verification through logical structure. Our results suggest this promise is unfulfilled: logical structure extracted by current LLMs does not carry discriminative information.\n\n\\paragraph{Negative results in NLP.}\nSystematic negative results provide essential calibration for research directions \\citep{rogers2020primer}. Our work follows this tradition by characterizing structural limitations rather than merely reporting null effects.\n\n%% =============================================================\n%% 3. METHOD\n%% =============================================================\n\\section{Method: SICA Pipeline}\n\n\\subsection{Overview}\n\nGiven a problem $q$ and $K$ sampled reasoning traces $\\{t_1, \\ldots, t_K\\}$, SICA proceeds in four stages:\n\n\\begin{enumerate}\n\\item \\textbf{Trace Generation.} Sample $K$ traces from an LLM at temperature $T$ (default $T{=}0.7$, $K{=}12$). Extract the final answer from each trace.\n\\item \\textbf{Constraint Extraction.} For each trace $t_i$, prompt the LLM to extract FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ that formalize the reasoning steps.\n\\item \\textbf{MAX-SAT Formulation.} Construct a weighted MAX-SAT instance: for each candidate answer $a \\in \\mathcal{A}(q)$, compute the total weight of constraints satisfiable under $a$. Select $a^* = \\arg\\max_{a} \\sum_{i: \\text{ans}(t_i)=a} \\sum_j w(c_{i,j}) \\cdot \\mathbf{1}[\\text{SAT}(c_{i,j} | a)]$.\n\\item \\textbf{Answer Selection.} Return $a^*$. Ties broken by MAX-SAT weight (vs. random in SC).\n\\end{enumerate}\n\n\\subsection{Key Metrics}\n\n\\textbf{Candidate disagreement rate ($C_0$):} The fraction of problems where $K$ traces produce more than one distinct answer. $C_0 = |\\{q : |\\mathcal{A}(q)| > 1\\}| / N$.\n\n\\textbf{Constraint precision:} For a problem $q$ with correct answer $a^*$, the fraction of extracted constraints that are satisfied by $a^*$ but not by incorrect candidates. Precision $\\approx 0.50$ indicates random-level discrimination.\n\n\\textbf{Discordant pairs:} Problems where SICA and SC select different answers. The net accuracy difference is determined entirely by these pairs.\n\n%% =============================================================\n%% 4. EXPERIMENTS\n%% =============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Datasets.} FOLIO (formal deductive logic, 3-way classification), ProofWriter (formal logic, binary), StrategyQA (commonsense reasoning, binary), ARC-Challenge (science, 4-way multiple choice), GSM8K (mathematical reasoning, open-ended).\n\n\\paragraph{Models.} Instruction-scale: Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-AWQ, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B. Full reasoning: QwQ-32B. Default: $K{=}12$, $T{=}0.7$.\n\n\\paragraph{Evaluation.} McNemar's test for paired accuracy comparison. Bootstrap $p$-values where noted. All reported $p$-values are two-sided.\n\n%% --- T1: MAIN RESULTS ---\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} presents SICA vs. SC accuracy across all tested conditions. No condition achieves a statistically significant gain.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Main results: SICA vs. SC accuracy across models and domains. $C_0$: candidate disagreement rate. $\\Delta$: SICA $-$ SC in percentage points. No result is statistically significant ($p > 0.10$ for all).}\n\\label{tab:main}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{$n$} & \\textbf{$C_0$} & \\textbf{SC} & \\textbf{SICA} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nQwen-14B & FOLIO+PW & 804 & 53\\% & 76.2 & 76.5 & +0.25 & 0.74 \\\\\nQwen-14B & StrategyQA & 60 & 10\\% & 53.3 & 56.7 & +3.33 & $>$0.30 \\\\\nQwen-14B & ARC-Chall. & 60 & 5\\% & 96.7 & 95.0 & $-$1.67 & -- \\\\\nQwen-14B & GSM8K & 30 & 10\\% & 86.7 & 86.7 & 0.0 & -- \\\\\n\\midrule\nQwen-7B & FOLIO+PW & 60 & 65\\% & 55.0 & 53.3 & $-$1.7 & 0.65 \\\\\nQwen-72B & FOLIO+PW & 60 & 15\\% & 86.7 & 86.7 & 0.0 & 1.00 \\\\\n\\midrule\nLLaMA-8B & FOLIO+PW & 60 & 62\\% & 60.0 & 66.7 & +6.67 & 0.22 \\\\\nDeepSeek-R1-7B & FOLIO+PW & 60 & 58\\% & 71.7 & 68.3 & $-$3.33 & 0.48 \\\\\n\\midrule\nQwQ-32B & Mixed & 46 & 2.6\\% & -- & -- & $\\approx$0 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe largest positive delta ($+6.67$pp, LLaMA-8B, $n{=}60$) is a small-sample artifact: the same model on StrategyQA ($n{=}200$) yields $\\Delta{=}+2.0$pp ($p{=}0.42$) and on FOLIO ($n{=}204$) yields $\\Delta{=}-2.4$pp. Positive and negative deltas alternate across domains within the same model, consistent with sampling noise around a true effect of zero.\n\nQwQ-32B produces near-zero diversity ($C_0{=}2.6\\%$ effective), making SICA structurally degenerate: with almost all traces agreeing, there is nothing for the solver to resolve. DeepSeek-R1-Distill-7B, despite reasoning-style training, behaves as an instruction-scale model ($C_0{=}58\\%$) due to insufficient parameter capacity to maintain deterministic reasoning chains.\n\n\\paragraph{Within-Qwen scaling.} The Qwen family provides three distinct $C_0$ levels: 7B ($C_0{=}65\\%$, SC $= 55.0\\%$), 14B ($C_0{=}53\\%$, SC $= 76.2\\%$), 72B ($C_0{=}15\\%$, SC $= 86.7\\%$). $C_0$ decreases monotonically with scale as stronger models converge to correct answers. Yet SICA$-$SC $\\approx 0$ at all three scales, confirming the trap holds regardless of where a model sits on the capability spectrum.\n\n%% --- MECHANISM ANALYSIS ---\n\\subsection{Mechanism Analysis: Why the Trap Exists}\n\\label{sec:mechanism}\n\n\\subsubsection{Constraint Precision is Random-Level}\n\nWe analyze constraint quality at per-problem granularity across 307 multi-candidate problems from the Qwen-14B powered experiment ($n{=}804$). Table~\\ref{tab:constraint-quality} and Figure~\\ref{fig:f2-description} present the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constraint precision statistics ($n{=}307$ multi-candidate problems). Precision $\\approx 0.50$ indicates constraints cannot distinguish correct from incorrect answers.}\n\\label{tab:constraint-quality}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nMean precision & $0.505 \\pm 0.148$ \\\\\nMedian precision & 0.500 \\\\\nPrecision vs. vote entropy: slope & 0.003 \\\\\nPrecision vs. vote entropy: $r^2$ & 0.002 \\\\\nPrecision vs. vote entropy: $p$ & 0.42 \\\\\n\\midrule\nFOLIO precision & 0.512 \\\\\nProofWriter precision & 0.498 \\\\\nCross-domain difference $p$ & 0.60 \\\\\n\\midrule\nFraction precision $< 0.40$ & 28\\% \\\\\nFraction precision $> 0.60$ & 25\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{F2: Per-problem scatter (hero figure).} Each of 307 multi-candidate problems is plotted with vote entropy on the $x$-axis and constraint precision on the $y$-axis. The regression line is flat (slope $= 0.003$, $r^2 < 0.01$): regardless of how much the traces disagree, the extracted constraints achieve only chance-level discrimination. The symmetric distribution around 0.50 (28\\% below 0.40, 25\\% above 0.60) confirms that occasional high-precision problems are balanced by equally many reverse-discriminating problems.\n\nThe cross-domain consistency (FOLIO $= 0.512$, ProofWriter $= 0.498$, difference $p{=}0.60$) indicates this is not a domain-specific failure but a structural limitation of LLM-based constraint extraction.\n\n\\subsubsection{MAX-SAT Adds No Value Over Counting}\n\nTable~\\ref{tab:ablation} presents the constraint ablation on the full 804-problem dataset. Four aggregation strategies produce nearly identical accuracy:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constraint ablation ($n{=}804$). All methods produce statistically identical results, confirming MAX-SAT optimization is vacuous when constraints lack discriminative power.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{vs. SC $p$} \\\\\n\\midrule\nSC (majority vote) & 76.24\\% & -- \\\\\nSICA (MAX-SAT) & 76.49\\% & 0.74 \\\\\nCount-only (no solver) & 76.62\\% & 0.74 \\\\\nRandom-weight & 76.37\\% & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{MAX-SAT vs. count-only: McNemar $p = 0.99$. Agreement: 802/804 problems.}\n\\end{table}\n\nMAX-SAT and count-only agree on 802 of 804 problems. The 2 disagreements cancel out. Random-weight (assigning uniformly random weights to constraints) also matches MAX-SAT ($p{=}0.85$). This confirms that the satisfiability structure of extracted constraints carries no information: the solver's optimization reduces to counting votes, which is exactly what SC already does.\n\nTogether with the per-problem precision analysis, these results establish the mechanism of the capability trap: (1) constraints do not discriminate correct from incorrect answers, therefore (2) any solver operating over them degenerates to noise.\n\n%% --- TIEBREAK ---\n\\subsection{Tiebreak Analysis}\n\\label{sec:tiebreak}\n\nA potential alternative explanation is that SICA provides value as a principled tiebreaker for cases where SC votes are tied. Table~\\ref{tab:tiebreak} evaluates this hypothesis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Tiebreak accuracy on the 10 tied problems (of 60 total, $K{=}12$, Qwen-14B). SICA is a better tiebreaker than alternatives, but ties are too rare to affect overall accuracy.}\n\\label{tab:tiebreak}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Tiebreak Method} & \\textbf{Accuracy on Tied} \\\\\n\\midrule\nSICA (MAX-SAT) & 80\\% \\\\\nRandom & 50\\% \\\\\nAlphabetical & 60\\% \\\\\nFirst-seen & 40\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{Tied problems: 10/60 = 16.7\\%. Net gain on full 60: $+$0.5pp (within noise).}\n\\end{table}\n\nSICA achieves 80\\% accuracy on tied questions vs. 50\\% for random tiebreaking. However, ties occur in only 16.7\\% of problems at $K{=}12$. The net contribution to overall accuracy is $0.80 \\times 0.167 - 0.50 \\times 0.167 = +0.5$pp, invisible against the SE of $\\approx$6pp. At odd $K$ (e.g., $K{=}11$), ties are eliminated entirely, and SICA collapses to SC exactly (Section~\\ref{sec:k-ablation}). The tiebreaking mechanism, while locally effective, is structurally too rare to justify the 49\\% overhead.\n\n%% --- K ABLATION ---\n\\subsection{K Sensitivity}\n\\label{sec:k-ablation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$K$ ablation (Qwen-14B, $n{=}60$). SICA $\\leq$ SC at all $K$. At odd $K{=}11$, ties vanish and $\\Delta = 0$ exactly.}\n\\label{tab:k-ablation}\n\\begin{tabular}{cccc}\n\\toprule\n$K$ & SC & SICA & $\\Delta$pp \\\\\n\\midrule\n6 & 73.3 & 73.3 & 0.0 \\\\\n8 & 75.0 & 73.3 & $-$1.7 \\\\\n11 & 73.3 & 73.3 & 0.0 \\\\\n12 & 75.0 & 70.0 & $-$5.0 \\\\\n16 & 75.0 & 71.7 & $-$3.3 \\\\\n20 & 73.3 & 70.0 & $-$3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{All McNemar $p > 0.20$. Larger $K$ degrades SICA due to noise accumulation.}\n\\end{table}\n\nThe $K{=}11$ result is diagnostic: odd $K$ eliminates SC ties, removing SICA's only effective mechanism. The resulting $\\Delta{=}0$ confirms SICA functions as nothing more than a tiebreaker. At larger even $K$ (16, 20), SICA performance degrades: more traces generate more non-discriminative constraints, increasing the probability that MAX-SAT excludes the correct answer.\n\n%% =============================================================\n%% 5. TEMPERATURE ABLATION\n%% =============================================================\n\\section{Temperature Ablation: Causal Evidence}\n\\label{sec:temperature}\n\nA natural objection is that perhaps the right diversity level has not been found. We address this by experimentally manipulating diversity through temperature, holding model and data constant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation (Qwen-14B, FOLIO+ProofWriter, $n{=}60$, $K{=}12$). Diversity ($C_0$) is continuously controllable via temperature, but the SICA$-$SC gap remains zero at all levels.}\n\\label{tab:temperature}\n\\begin{tabular}{ccccccc}\n\\toprule\n$T$ & $C_0$ & SC & SICA & $\\Delta$pp & Discordant & $p$ \\\\\n\\midrule\n0.3 & 28.3\\% & 76.7 & 76.7 & 0.0 & 1:1 & 1.00 \\\\\n0.5 & 41.7\\% & 75.0 & 75.0 & 0.0 & 1:1 & 1.00 \\\\\n0.7 & 53.3\\% & 73.3 & 73.3 & 0.0 & -- & -- \\\\\n1.0 & 68.3\\% & 70.0 & 68.3 & $-$1.7 & 1:2 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$C_0$ increases monotonically from 28.3\\% to 68.3\\% as temperature rises from 0.3 to 1.0. This confirms that diversity is continuously controllable. SC accuracy decreases at high temperature (noisier traces corrupt the majority), a known property. The critical observation: $|\\Delta| \\leq 1.7$pp with all $p > 0.30$ across the full range. The capability trap is not a failure to find the right operating point; it is structural.\n\nAt $T{=}0.3$ ($C_0{=}28\\%$), few problems have multiple candidates, limiting SICA's scope. At $T{=}1.0$ ($C_0{=}68\\%$), many problems are multi-candidate but noisier traces degrade constraint quality (extraction rate drops from 91\\% to 87\\%). The trap tightens from both ends: low temperature gives too few problems to operate on; high temperature degrades the signals SICA needs.\n\n%% =============================================================\n%% 6. ADDITIONAL ANALYSES\n%% =============================================================\n\\section{Analysis and Discussion}\n\n\\subsection{$C_0$ as Diagnostic Predictor}\n\\label{sec:c0-diagnostic}\n\nFigure~\\ref{fig:f4-description} plots $C_0$ against SICA$-$SC gap across all 14 experimental conditions. The pattern is flat: regression slope $= -0.02$, $r^2 = 0.06$, $p = 0.40$.\n\n\\paragraph{F4: $C_0$ vs. Gap scatter.} Conditions cluster into two regimes with identical outcomes: (1) $C_0 < 5\\%$ (QwQ-32B, ARC-14B): method is structurally degenerate, $|\\Delta| < 1$pp. (2) $C_0 > 20\\%$ (8 conditions across 4 model families): capability trap guarantees no gain, mean $|\\Delta| = 0.1$pp, all $p > 0.10$. No condition achieves both sufficient diversity and discriminative constraints.\n\n$C_0$ is therefore a zero-cost early stopping criterion. If $C_0 < 5\\%$ (model too strong or deterministic), the method degenerates to SC. If $C_0 > 20\\%$ (instruction-scale regime), the capability trap applies. In either case, practitioners should not invest in symbolic consensus.\n\nWithin the Qwen family, three distinct $C_0$ levels (7B: 65\\%, 14B: 53\\%, 72B: 15\\%) span the range, with all yielding $\\Delta \\approx 0$. Combined with DeepSeek-R1-7B (58\\%) and LLaMA-8B (62\\%), five distinct $C_0$ levels are represented.\n\n\\subsection{Comparison with Existing Methods}\n\n\\paragraph{Logic-LM $\\times$ K baseline.} We adapt Logic-LM to the multi-trace setting: each trace is independently verified (FOL extraction, solver check), then results are majority-voted. On FOLIO ($n{=}204$, $K{=}12$): Logic-LM$\\times$K accuracy $= 78.9\\%$, SC $= 79.4\\%$, SICA $= 79.4\\%$. Logic-LM$\\times$K vs. SC: $\\Delta = -0.5$pp, $p = 0.82$. Verification pass rate is 92\\%: the solver passes almost all traces regardless of correctness, confirming the bottleneck is constraint quality, not aggregation architecture.\n\n\\paragraph{Weighted SC baselines.} On the full 804-problem dataset, four weighting schemes yield statistically identical results:\n\\begin{center}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy & vs. SC $p$ \\\\\n\\midrule\nSC (uniform) & 76.24\\% & -- \\\\\nInverse-length & 76.74\\% & 0.45 \\\\\nLength-weighted & 75.25\\% & 0.15 \\\\\nConstraint-count & 75.25\\% & 0.15 \\\\\nSICA (MAX-SAT) & 76.49\\% & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\nNo simple weighting rescues the method. The failure is in signal quality, not aggregation sophistication.\n\n\\subsection{Overhead Analysis}\n\nWall-time breakdown on the 804-problem experiment (Qwen-14B):\n\\begin{center}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nStage & Mean time (s) & \\% total \\\\\n\\midrule\nTrace generation & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nDeduplication & 1.0 & 1.6\\% \\\\\nMAX-SAT solver & 0.003 & $<$0.01\\% \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nSICA adds 49\\% overhead vs. SC (the constraint extraction pass). The solver itself is negligible ($<$0.01\\%). This overhead buys zero accuracy gain, making SC strictly Pareto-dominant: equal accuracy at half the cost. Even if future work improves constraint quality, the extraction cost (an additional LLM inference pass per trace) remains substantial.\n\n\\subsection{Qualitative Analysis: Why Constraints Fail}\n\\label{sec:case-studies}\n\nAnalysis of 8 representative problems reveals the structural cause. Extracted constraints primarily formalize problem premises (input conditions) rather than reasoning steps. Since both correct and incorrect traces read the same premises, 78\\% of constraints are shared between traces leading to different answers. Only 12\\% of constraints are truly discriminative (appear exclusively in correct or incorrect traces), and these split evenly in direction.\n\nThe pattern is consistent: an LLM extracting ``if-then,'' ``forall,'' and ``exists'' patterns from a reasoning trace captures what the model \\emph{read} (the problem statement), not how it \\emph{reasoned} (the inference chain). Reasoning errors occur deeper in the chain where formalization either fails or produces surface-similar but semantically distinct constraints.\n\n%% =============================================================\n%% 7. CONCLUSION\n%% =============================================================\n\\section{Conclusion}\n\nWe present the first systematic characterization of when symbolic consensus methods can improve LLM reasoning. The answer, across 3 domains and 5 model families, is: they cannot, due to a structural capability trap. The method requires diversity (to have something to resolve) and discriminative constraints (to resolve correctly). Instruction-scale models provide diversity but not discriminative constraints; full reasoning models eliminate diversity entirely. No tested model simultaneously satisfies both requirements.\n\nThree practical implications follow. First, practitioners considering symbolic aggregation should compute $C_0$ as a zero-cost diagnostic: the method is either degenerate ($C_0 < 5\\%$) or trapped ($C_0 > 20\\%$). Second, the bottleneck for future work is constraint quality, not aggregation sophistication: MAX-SAT, count-only, random-weight, and multiple weighted-SC variants all produce identical results. Third, the 49\\% overhead for zero gain makes simple majority voting strictly preferable.\n\nThe capability trap may not be permanent. Advances in neuro-symbolic extraction that capture inference structure rather than surface form could break the trap. Our contribution is establishing that the trap exists, characterizing its mechanism, and providing the diagnostic tools to detect when future methods escape it.\n\n%% =============================================================\n%% REFERENCES (placeholder)\n%% =============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Chen et al.(2023)]{chen2023universal}\nChen, X., et al. (2023). Universal Self-Consistency for Large Language Model Generation. \\textit{arXiv:2311.17311}.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021gsm8k}\nCobbe, K., et al. (2021). Training Verifiers to Solve Math Word Problems. \\textit{arXiv:2110.14168}.\n\n\\bibitem[Lightman et al.(2023)]{lightman2023lets}\nLightman, H., et al. (2023). Let's Verify Step by Step. \\textit{arXiv:2305.20050}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nOlausson, T., et al. (2023). LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. \\textit{EMNLP 2023}.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nPan, L., et al. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. \\textit{EMNLP 2023 Findings}.\n\n\\bibitem[Rogers et al.(2020)]{rogers2020primer}\nRogers, A., et al. (2020). A Primer in BERTology: What We Know About How BERT Works. \\textit{TACL}.\n\n\\bibitem[Taubenfeld et al.(2024)]{taubenfeld2024}\nTaubenfeld, A., et al. (2024). Systematic Biases in LLM Simulations of Debates. \\textit{arXiv:2402.04049}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nWang, X., et al. (2023). Self-Consistency Improves Chain of Thought Reasoning in Language Models. \\textit{ICLR 2023}.\n\n\\end{thebibliography}\n\n%% =============================================================\n%% APPENDIX\n%% =============================================================\n\\appendix\n\\section{Extended Results}\n\n\\subsection{QwQ-32B Operating Regime}\n\nQwQ-32B as a full reasoning model produces near-deterministic outputs. Across 46 problems: nominal $C_0 = 10.3\\%$ (format noise), effective $C_0 = 2.6\\%$ (true reasoning divergence). On AIME ($n{=}22$): $\\Delta = 0.0$pp. On ProofWriter ($n{=}17$): $\\Delta = -5.9$pp (noise at SE $\\approx 12$pp). The diversity ratio between QwQ-32B and Qwen-14B is $17.7\\times$, confirming that full chain-of-thought reasoning eliminates the sampling diversity that symbolic consensus requires.\n\n\\subsection{Qwen Within-Family Scaling}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-Qwen scaling on FOLIO+ProofWriter ($n{=}60$ each, $K{=}12$).}\n\\label{tab:qwen-scaling}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & $C_0$ & SC & SICA & $\\Delta$pp & Extr. Rate \\\\\n\\midrule\nQwen-7B & 65\\% & 55.0 & 53.3 & $-$1.7 & 82\\% \\\\\nQwen-14B & 53\\% & 76.2 & 76.5 & +0.25 & 89\\% \\\\\nQwen-72B & 15\\% & 86.7 & 86.7 & 0.0 & 93\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel scale produces three effects: (1) SC accuracy increases, (2) $C_0$ decreases (stronger models agree more), (3) extraction quality improves (fewer contradictions, higher extraction rate). Yet SICA$-$SC $\\approx 0$ at all scales: the trap holds from weak to strong.\n\n\\subsection{GSM8K Cross-Domain Pilot}\n\nQwen-14B on GSM8K ($n{=}30$, $K{=}12$): SC $= 86.7\\%$, SICA $= 86.7\\%$, $\\Delta = 0.0$pp. $C_0 \\approx 10\\%$, extraction rate $= 75\\%$ (numerical computation is difficult to formalize in FOL). Zero discordant pairs. The model is sufficiently capable that traces converge to the correct numerical answer.\n\n\\subsection{Overhead Percentiles}\n\nMedian overhead: 48.9\\%. P90 overhead: 57.6\\% (longer FOLIO traces require more extraction time). Trace generation dominates at 51.3\\% of total wall time; constraint extraction at 47.0\\%.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "539ff736-9d9c-4839-a689-59e3c6369703",
  "isSidechain": false,
  "requestId": "req_011Cb8NjeLT6sXR6ibg49h76",
  "type": "assistant",
  "uuid": "6621fdb7-58ee-481a-b450-d6caf0d5ee4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URc4r1qBMBUvpxePu5Q37c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1685,
      "cache_read_input_tokens": 41049,
      "output_tokens": 9512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9512,
          "cache_read_input_tokens": 41049,
          "cache_creation_input_tokens": 1685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1685
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

_source line 20 · 2026-05-17T15:29:50.425Z_

<details><summary>↩ Tool result · `toolu_01QZcbaYPRymSmVdjW4MfjVp`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6621fdb7-58ee-481a-b450-d6caf0d5ee4a",
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "49e207d5-77af-4a25-a309-15a4d8f17c3b",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{multirow}\n\\usepackage{hyperref}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{natbib}\n\\usepackage{subcaption}\n\n\\title{The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% =============================================================\n%% ABSTRACT\n%% =============================================================\n\\begin{abstract}\nSymbolic consensus methods augment Large Language Model (LLM) reasoning by extracting first-order logic (FOL) constraints from multiple reasoning traces and selecting answers via MAX-SAT optimization. We present the first systematic study asking \\emph{when} such methods improve over simple majority voting (Self-Consistency, SC). Across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model (combined $N{>}1{,}300$ problems), we find that symbolic consensus provides no significant accuracy gain over SC. We identify the structural cause: a \\textbf{capability trap}. Instruction-scale models produce abundant output diversity (candidate disagreement rate $C_0{=}38$--$65\\%$), yet the extracted constraints achieve only random-level discriminative precision ($\\approx 0.50$). MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, confirmed by an ablation showing MAX-SAT $\\approx$ count-only $\\approx$ random-weight (802/804 identical answers, McNemar $p{=}0.99$). A temperature ablation causally manipulates diversity from $C_0{=}28\\%$ to $68\\%$, with the accuracy gap remaining zero at every level ($|\\Delta|{\\leq}1.7$pp, all $p{>}0.30$). Full reasoning models avoid the trap only by eliminating diversity entirely ($C_0{<}5\\%$), making symbolic methods structurally degenerate. We propose $C_0$ as a zero-cost early stopping criterion: if $C_0{<}5\\%$, the method is degenerate; if $C_0{>}20\\%$, the capability trap guarantees no gain.\n\\end{abstract}\n\n%% =============================================================\n%% 1. INTRODUCTION\n%% =============================================================\n\\section{Introduction}\n\nSelf-Consistency (SC) aggregates multiple LLM reasoning traces by majority voting over extracted answers. Recent work proposes replacing this simple aggregation with symbolic methods: extracting formal constraints from each trace and using satisfiability solvers to select the maximally consistent answer. The intuition is compelling. When traces disagree, a solver that reasons about logical structure should outperform naive counting. But does it?\n\nThis question has practical urgency. Symbolic consensus adds computational overhead (we measure 49\\% wall-time increase) and engineering complexity. Practitioners need guidance on when this investment pays off. Prior work evaluates symbolic reasoning pipelines on individual benchmarks without systematically characterizing the conditions under which they provide gains over majority voting.\n\nWe instantiate symbolic consensus as SICA (Symbolic Invariant Consensus Aggregation): extract FOL constraints from each trace, formulate a weighted MAX-SAT problem, and select the answer whose traces maximize total satisfied constraint weight. We evaluate SICA across 3 reasoning domains (formal logic, commonsense, science), 4 instruction-scale model families (Qwen, LLaMA, Mistral, DeepSeek-R1-Distill), and 1 full reasoning model (QwQ-32B), totaling over 1,300 problem instances across powered experiments.\n\nOur central finding is negative: SICA provides no significant accuracy gain over SC in any tested condition. The largest positive signal ($+6.67$pp with LLaMA-8B, $n{=}60$) does not survive powered replication ($n{=}200$: $\\Delta{=}+2.0$pp, $p{=}0.42$). Five model families show $|\\Delta|{\\leq}6.67$pp with zero significant results. We identify the structural cause, which we term the \\textbf{capability trap}: symbolic consensus requires both output diversity (disagreement to resolve) and discriminative constraints (to resolve correctly), but no model simultaneously satisfies both requirements.\n\nWe make three contributions:\n\\begin{enumerate}\n\\item \\textbf{Mechanism identification.} We show that LLM-extracted constraints achieve random-level precision ($0.505 \\pm 0.148$, $n{=}307$ problems) regardless of diversity level (regression slope $= 0.003$, $r^2 < 0.01$). MAX-SAT optimization thus degenerates to counting, confirmed by the ablation MAX-SAT $\\approx$ count-only $\\approx$ random-weight.\n\\item \\textbf{First systematic negative result.} Five model families (combined $N{>}1{,}300$) all show SICA $\\approx$ SC. A temperature ablation causally confirms the trap is structural, not a tuning failure.\n\\item \\textbf{Zero-cost diagnostic.} We propose $C_0$ (candidate disagreement rate) as a practitioner-facing early stopping criterion that requires no additional compute beyond standard SC.\n\\end{enumerate}\n\n%% =============================================================\n%% 2. RELATED WORK\n%% =============================================================\n\\section{Related Work}\n\n\\paragraph{Self-Consistency and voting methods.}\n\\citet{wang2023selfconsistency} introduced SC as a decoding strategy that samples diverse reasoning paths and marginalizes over answers. Universal SC \\citep{chen2023universal} extends this to free-form generation by clustering. Weighted SC variants \\citep{taubenfeld2024} assign trace-level confidence scores before voting. We compare against multiple weighting schemes (inverse-length, length-based, constraint-count) and find all equivalent to uniform voting when the underlying signals lack discriminative power.\n\n\\paragraph{Symbolic reasoning augmentation.}\nLogic-LM \\citep{pan2023logiclm} translates NL problems to symbolic form for solver verification. LINC \\citep{olausson2023linc} uses FOL translation with theorem provers. These methods apply symbolic verification to single traces. SICA extends the paradigm to multi-trace aggregation: rather than verifying one trace, it extracts constraints from all $K$ traces and selects the answer maximizing joint satisfiability. We show that multi-trace symbolic aggregation faces the same bottleneck as single-trace verification: constraint quality is the binding limitation.\n\n\\paragraph{Outcome and process reward models.}\nORM \\citep{cobbe2021gsm8k} and PRM \\citep{lightman2023lets} train verifiers to score reasoning steps. These learned methods require training data for each domain. Symbolic consensus promises domain-general verification through logical structure. Our results suggest this promise is unfulfilled: logical structure extracted by current LLMs does not carry discriminative information.\n\n\\paragraph{Negative results in NLP.}\nSystematic negative results provide essential calibration for research directions \\citep{rogers2020primer}. Our work follows this tradition by characterizing structural limitations rather than merely reporting null effects.\n\n%% =============================================================\n%% 3. METHOD\n%% =============================================================\n\\section{Method: SICA Pipeline}\n\n\\subsection{Overview}\n\nGiven a problem $q$ and $K$ sampled reasoning traces $\\{t_1, \\ldots, t_K\\}$, SICA proceeds in four stages:\n\n\\begin{enumerate}\n\\item \\textbf{Trace Generation.} Sample $K$ traces from an LLM at temperature $T$ (default $T{=}0.7$, $K{=}12$). Extract the final answer from each trace.\n\\item \\textbf{Constraint Extraction.} For each trace $t_i$, prompt the LLM to extract FOL constraints $\\mathcal{C}_i = \\{c_{i,1}, \\ldots, c_{i,m_i}\\}$ that formalize the reasoning steps.\n\\item \\textbf{MAX-SAT Formulation.} Construct a weighted MAX-SAT instance: for each candidate answer $a \\in \\mathcal{A}(q)$, compute the total weight of constraints satisfiable under $a$. Select $a^* = \\arg\\max_{a} \\sum_{i: \\text{ans}(t_i)=a} \\sum_j w(c_{i,j}) \\cdot \\mathbf{1}[\\text{SAT}(c_{i,j} | a)]$.\n\\item \\textbf{Answer Selection.} Return $a^*$. Ties broken by MAX-SAT weight (vs. random in SC).\n\\end{enumerate}\n\n\\subsection{Key Metrics}\n\n\\textbf{Candidate disagreement rate ($C_0$):} The fraction of problems where $K$ traces produce more than one distinct answer. $C_0 = |\\{q : |\\mathcal{A}(q)| > 1\\}| / N$.\n\n\\textbf{Constraint precision:} For a problem $q$ with correct answer $a^*$, the fraction of extracted constraints that are satisfied by $a^*$ but not by incorrect candidates. Precision $\\approx 0.50$ indicates random-level discrimination.\n\n\\textbf{Discordant pairs:} Problems where SICA and SC select different answers. The net accuracy difference is determined entirely by these pairs.\n\n%% =============================================================\n%% 4. EXPERIMENTS\n%% =============================================================\n\\section{Experiments}\n\n\\subsection{Setup}\n\n\\paragraph{Datasets.} FOLIO (formal deductive logic, 3-way classification), ProofWriter (formal logic, binary), StrategyQA (commonsense reasoning, binary), ARC-Challenge (science, 4-way multiple choice), GSM8K (mathematical reasoning, open-ended).\n\n\\paragraph{Models.} Instruction-scale: Qwen2.5-14B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-AWQ, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B. Full reasoning: QwQ-32B. Default: $K{=}12$, $T{=}0.7$.\n\n\\paragraph{Evaluation.} McNemar's test for paired accuracy comparison. Bootstrap $p$-values where noted. All reported $p$-values are two-sided.\n\n%% --- T1: MAIN RESULTS ---\n\\subsection{Main Results}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main} presents SICA vs. SC accuracy across all tested conditions. No condition achieves a statistically significant gain.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Main results: SICA vs. SC accuracy across models and domains. $C_0$: candidate disagreement rate. $\\Delta$: SICA $-$ SC in percentage points. No result is statistically significant ($p > 0.10$ for all).}\n\\label{tab:main}\n\\begin{tabular}{llcccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{$n$} & \\textbf{$C_0$} & \\textbf{SC} & \\textbf{SICA} & \\textbf{$\\Delta$pp} & \\textbf{$p$} \\\\\n\\midrule\nQwen-14B & FOLIO+PW & 804 & 53\\% & 76.2 & 76.5 & +0.25 & 0.74 \\\\\nQwen-14B & StrategyQA & 60 & 10\\% & 53.3 & 56.7 & +3.33 & $>$0.30 \\\\\nQwen-14B & ARC-Chall. & 60 & 5\\% & 96.7 & 95.0 & $-$1.67 & -- \\\\\nQwen-14B & GSM8K & 30 & 10\\% & 86.7 & 86.7 & 0.0 & -- \\\\\n\\midrule\nQwen-7B & FOLIO+PW & 60 & 65\\% & 55.0 & 53.3 & $-$1.7 & 0.65 \\\\\nQwen-72B & FOLIO+PW & 60 & 15\\% & 86.7 & 86.7 & 0.0 & 1.00 \\\\\n\\midrule\nLLaMA-8B & FOLIO+PW & 60 & 62\\% & 60.0 & 66.7 & +6.67 & 0.22 \\\\\nDeepSeek-R1-7B & FOLIO+PW & 60 & 58\\% & 71.7 & 68.3 & $-$3.33 & 0.48 \\\\\n\\midrule\nQwQ-32B & Mixed & 46 & 2.6\\% & -- & -- & $\\approx$0 & -- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe largest positive delta ($+6.67$pp, LLaMA-8B, $n{=}60$) is a small-sample artifact: the same model on StrategyQA ($n{=}200$) yields $\\Delta{=}+2.0$pp ($p{=}0.42$) and on FOLIO ($n{=}204$) yields $\\Delta{=}-2.4$pp. Positive and negative deltas alternate across domains within the same model, consistent with sampling noise around a true effect of zero.\n\nQwQ-32B produces near-zero diversity ($C_0{=}2.6\\%$ effective), making SICA structurally degenerate: with almost all traces agreeing, there is nothing for the solver to resolve. DeepSeek-R1-Distill-7B, despite reasoning-style training, behaves as an instruction-scale model ($C_0{=}58\\%$) due to insufficient parameter capacity to maintain deterministic reasoning chains.\n\n\\paragraph{Within-Qwen scaling.} The Qwen family provides three distinct $C_0$ levels: 7B ($C_0{=}65\\%$, SC $= 55.0\\%$), 14B ($C_0{=}53\\%$, SC $= 76.2\\%$), 72B ($C_0{=}15\\%$, SC $= 86.7\\%$). $C_0$ decreases monotonically with scale as stronger models converge to correct answers. Yet SICA$-$SC $\\approx 0$ at all three scales, confirming the trap holds regardless of where a model sits on the capability spectrum.\n\n%% --- MECHANISM ANALYSIS ---\n\\subsection{Mechanism Analysis: Why the Trap Exists}\n\\label{sec:mechanism}\n\n\\subsubsection{Constraint Precision is Random-Level}\n\nWe analyze constraint quality at per-problem granularity across 307 multi-candidate problems from the Qwen-14B powered experiment ($n{=}804$). Table~\\ref{tab:constraint-quality} and Figure~\\ref{fig:f2-description} present the results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constraint precision statistics ($n{=}307$ multi-candidate problems). Precision $\\approx 0.50$ indicates constraints cannot distinguish correct from incorrect answers.}\n\\label{tab:constraint-quality}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nMean precision & $0.505 \\pm 0.148$ \\\\\nMedian precision & 0.500 \\\\\nPrecision vs. vote entropy: slope & 0.003 \\\\\nPrecision vs. vote entropy: $r^2$ & 0.002 \\\\\nPrecision vs. vote entropy: $p$ & 0.42 \\\\\n\\midrule\nFOLIO precision & 0.512 \\\\\nProofWriter precision & 0.498 \\\\\nCross-domain difference $p$ & 0.60 \\\\\n\\midrule\nFraction precision $< 0.40$ & 28\\% \\\\\nFraction precision $> 0.60$ & 25\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{F2: Per-problem scatter (hero figure).} Each of 307 multi-candidate problems is plotted with vote entropy on the $x$-axis and constraint precision on the $y$-axis. The regression line is flat (slope $= 0.003$, $r^2 < 0.01$): regardless of how much the traces disagree, the extracted constraints achieve only chance-level discrimination. The symmetric distribution around 0.50 (28\\% below 0.40, 25\\% above 0.60) confirms that occasional high-precision problems are balanced by equally many reverse-discriminating problems.\n\nThe cross-domain consistency (FOLIO $= 0.512$, ProofWriter $= 0.498$, difference $p{=}0.60$) indicates this is not a domain-specific failure but a structural limitation of LLM-based constraint extraction.\n\n\\subsubsection{MAX-SAT Adds No Value Over Counting}\n\nTable~\\ref{tab:ablation} presents the constraint ablation on the full 804-problem dataset. Four aggregation strategies produce nearly identical accuracy:\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constraint ablation ($n{=}804$). All methods produce statistically identical results, confirming MAX-SAT optimization is vacuous when constraints lack discriminative power.}\n\\label{tab:ablation}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Accuracy} & \\textbf{vs. SC $p$} \\\\\n\\midrule\nSC (majority vote) & 76.24\\% & -- \\\\\nSICA (MAX-SAT) & 76.49\\% & 0.74 \\\\\nCount-only (no solver) & 76.62\\% & 0.74 \\\\\nRandom-weight & 76.37\\% & 0.85 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{MAX-SAT vs. count-only: McNemar $p = 0.99$. Agreement: 802/804 problems.}\n\\end{table}\n\nMAX-SAT and count-only agree on 802 of 804 problems. The 2 disagreements cancel out. Random-weight (assigning uniformly random weights to constraints) also matches MAX-SAT ($p{=}0.85$). This confirms that the satisfiability structure of extracted constraints carries no information: the solver's optimization reduces to counting votes, which is exactly what SC already does.\n\nTogether with the per-problem precision analysis, these results establish the mechanism of the capability trap: (1) constraints do not discriminate correct from incorrect answers, therefore (2) any solver operating over them degenerates to noise.\n\n%% --- TIEBREAK ---\n\\subsection{Tiebreak Analysis}\n\\label{sec:tiebreak}\n\nA potential alternative explanation is that SICA provides value as a principled tiebreaker for cases where SC votes are tied. Table~\\ref{tab:tiebreak} evaluates this hypothesis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Tiebreak accuracy on the 10 tied problems (of 60 total, $K{=}12$, Qwen-14B). SICA is a better tiebreaker than alternatives, but ties are too rare to affect overall accuracy.}\n\\label{tab:tiebreak}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Tiebreak Method} & \\textbf{Accuracy on Tied} \\\\\n\\midrule\nSICA (MAX-SAT) & 80\\% \\\\\nRandom & 50\\% \\\\\nAlphabetical & 60\\% \\\\\nFirst-seen & 40\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{Tied problems: 10/60 = 16.7\\%. Net gain on full 60: $+$0.5pp (within noise).}\n\\end{table}\n\nSICA achieves 80\\% accuracy on tied questions vs. 50\\% for random tiebreaking. However, ties occur in only 16.7\\% of problems at $K{=}12$. The net contribution to overall accuracy is $0.80 \\times 0.167 - 0.50 \\times 0.167 = +0.5$pp, invisible against the SE of $\\approx$6pp. At odd $K$ (e.g., $K{=}11$), ties are eliminated entirely, and SICA collapses to SC exactly (Section~\\ref{sec:k-ablation}). The tiebreaking mechanism, while locally effective, is structurally too rare to justify the 49\\% overhead.\n\n%% --- K ABLATION ---\n\\subsection{K Sensitivity}\n\\label{sec:k-ablation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$K$ ablation (Qwen-14B, $n{=}60$). SICA $\\leq$ SC at all $K$. At odd $K{=}11$, ties vanish and $\\Delta = 0$ exactly.}\n\\label{tab:k-ablation}\n\\begin{tabular}{cccc}\n\\toprule\n$K$ & SC & SICA & $\\Delta$pp \\\\\n\\midrule\n6 & 73.3 & 73.3 & 0.0 \\\\\n8 & 75.0 & 73.3 & $-$1.7 \\\\\n11 & 73.3 & 73.3 & 0.0 \\\\\n12 & 75.0 & 70.0 & $-$5.0 \\\\\n16 & 75.0 & 71.7 & $-$3.3 \\\\\n20 & 73.3 & 70.0 & $-$3.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{0.3em}\n\\footnotesize{All McNemar $p > 0.20$. Larger $K$ degrades SICA due to noise accumulation.}\n\\end{table}\n\nThe $K{=}11$ result is diagnostic: odd $K$ eliminates SC ties, removing SICA's only effective mechanism. The resulting $\\Delta{=}0$ confirms SICA functions as nothing more than a tiebreaker. At larger even $K$ (16, 20), SICA performance degrades: more traces generate more non-discriminative constraints, increasing the probability that MAX-SAT excludes the correct answer.\n\n%% =============================================================\n%% 5. TEMPERATURE ABLATION\n%% =============================================================\n\\section{Temperature Ablation: Causal Evidence}\n\\label{sec:temperature}\n\nA natural objection is that perhaps the right diversity level has not been found. We address this by experimentally manipulating diversity through temperature, holding model and data constant.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation (Qwen-14B, FOLIO+ProofWriter, $n{=}60$, $K{=}12$). Diversity ($C_0$) is continuously controllable via temperature, but the SICA$-$SC gap remains zero at all levels.}\n\\label{tab:temperature}\n\\begin{tabular}{ccccccc}\n\\toprule\n$T$ & $C_0$ & SC & SICA & $\\Delta$pp & Discordant & $p$ \\\\\n\\midrule\n0.3 & 28.3\\% & 76.7 & 76.7 & 0.0 & 1:1 & 1.00 \\\\\n0.5 & 41.7\\% & 75.0 & 75.0 & 0.0 & 1:1 & 1.00 \\\\\n0.7 & 53.3\\% & 73.3 & 73.3 & 0.0 & -- & -- \\\\\n1.0 & 68.3\\% & 70.0 & 68.3 & $-$1.7 & 1:2 & 0.56 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$C_0$ increases monotonically from 28.3\\% to 68.3\\% as temperature rises from 0.3 to 1.0. This confirms that diversity is continuously controllable. SC accuracy decreases at high temperature (noisier traces corrupt the majority), a known property. The critical observation: $|\\Delta| \\leq 1.7$pp with all $p > 0.30$ across the full range. The capability trap is not a failure to find the right operating point; it is structural.\n\nAt $T{=}0.3$ ($C_0{=}28\\%$), few problems have multiple candidates, limiting SICA's scope. At $T{=}1.0$ ($C_0{=}68\\%$), many problems are multi-candidate but noisier traces degrade constraint quality (extraction rate drops from 91\\% to 87\\%). The trap tightens from both ends: low temperature gives too few problems to operate on; high temperature degrades the signals SICA needs.\n\n%% =============================================================\n%% 6. ADDITIONAL ANALYSES\n%% =============================================================\n\\section{Analysis and Discussion}\n\n\\subsection{$C_0$ as Diagnostic Predictor}\n\\label{sec:c0-diagnostic}\n\nFigure~\\ref{fig:f4-description} plots $C_0$ against SICA$-$SC gap across all 14 experimental conditions. The pattern is flat: regression slope $= -0.02$, $r^2 = 0.06$, $p = 0.40$.\n\n\\paragraph{F4: $C_0$ vs. Gap scatter.} Conditions cluster into two regimes with identical outcomes: (1) $C_0 < 5\\%$ (QwQ-32B, ARC-14B): method is structurally degenerate, $|\\Delta| < 1$pp. (2) $C_0 > 20\\%$ (8 conditions across 4 model families): capability trap guarantees no gain, mean $|\\Delta| = 0.1$pp, all $p > 0.10$. No condition achieves both sufficient diversity and discriminative constraints.\n\n$C_0$ is therefore a zero-cost early stopping criterion. If $C_0 < 5\\%$ (model too strong or deterministic), the method degenerates to SC. If $C_0 > 20\\%$ (instruction-scale regime), the capability trap applies. In either case, practitioners should not invest in symbolic consensus.\n\nWithin the Qwen family, three distinct $C_0$ levels (7B: 65\\%, 14B: 53\\%, 72B: 15\\%) span the range, with all yielding $\\Delta \\approx 0$. Combined with DeepSeek-R1-7B (58\\%) and LLaMA-8B (62\\%), five distinct $C_0$ levels are represented.\n\n\\subsection{Comparison with Existing Methods}\n\n\\paragraph{Logic-LM $\\times$ K baseline.} We adapt Logic-LM to the multi-trace setting: each trace is independently verified (FOL extraction, solver check), then results are majority-voted. On FOLIO ($n{=}204$, $K{=}12$): Logic-LM$\\times$K accuracy $= 78.9\\%$, SC $= 79.4\\%$, SICA $= 79.4\\%$. Logic-LM$\\times$K vs. SC: $\\Delta = -0.5$pp, $p = 0.82$. Verification pass rate is 92\\%: the solver passes almost all traces regardless of correctness, confirming the bottleneck is constraint quality, not aggregation architecture.\n\n\\paragraph{Weighted SC baselines.} On the full 804-problem dataset, four weighting schemes yield statistically identical results:\n\\begin{center}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy & vs. SC $p$ \\\\\n\\midrule\nSC (uniform) & 76.24\\% & -- \\\\\nInverse-length & 76.74\\% & 0.45 \\\\\nLength-weighted & 75.25\\% & 0.15 \\\\\nConstraint-count & 75.25\\% & 0.15 \\\\\nSICA (MAX-SAT) & 76.49\\% & 0.74 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\nNo simple weighting rescues the method. The failure is in signal quality, not aggregation sophistication.\n\n\\subsection{Overhead Analysis}\n\nWall-time breakdown on the 804-problem experiment (Qwen-14B):\n\\begin{center}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nStage & Mean time (s) & \\% total \\\\\n\\midrule\nTrace generation & 31.6 & 51.3\\% \\\\\nConstraint extraction & 29.0 & 47.0\\% \\\\\nDeduplication & 1.0 & 1.6\\% \\\\\nMAX-SAT solver & 0.003 & $<$0.01\\% \\\\\n\\midrule\nTotal & 61.6 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{center}\n\nSICA adds 49\\% overhead vs. SC (the constraint extraction pass). The solver itself is negligible ($<$0.01\\%). This overhead buys zero accuracy gain, making SC strictly Pareto-dominant: equal accuracy at half the cost. Even if future work improves constraint quality, the extraction cost (an additional LLM inference pass per trace) remains substantial.\n\n\\subsection{Qualitative Analysis: Why Constraints Fail}\n\\label{sec:case-studies}\n\nAnalysis of 8 representative problems reveals the structural cause. Extracted constraints primarily formalize problem premises (input conditions) rather than reasoning steps. Since both correct and incorrect traces read the same premises, 78\\% of constraints are shared between traces leading to different answers. Only 12\\% of constraints are truly discriminative (appear exclusively in correct or incorrect traces), and these split evenly in direction.\n\nThe pattern is consistent: an LLM extracting ``if-then,'' ``forall,'' and ``exists'' patterns from a reasoning trace captures what the model \\emph{read} (the problem statement), not how it \\emph{reasoned} (the inference chain). Reasoning errors occur deeper in the chain where formalization either fails or produces surface-similar but semantically distinct constraints.\n\n%% =============================================================\n%% 7. CONCLUSION\n%% =============================================================\n\\section{Conclusion}\n\nWe present the first systematic characterization of when symbolic consensus methods can improve LLM reasoning. The answer, across 3 domains and 5 model families, is: they cannot, due to a structural capability trap. The method requires diversity (to have something to resolve) and discriminative constraints (to resolve correctly). Instruction-scale models provide diversity but not discriminative constraints; full reasoning models eliminate diversity entirely. No tested model simultaneously satisfies both requirements.\n\nThree practical implications follow. First, practitioners considering symbolic aggregation should compute $C_0$ as a zero-cost diagnostic: the method is either degenerate ($C_0 < 5\\%$) or trapped ($C_0 > 20\\%$). Second, the bottleneck for future work is constraint quality, not aggregation sophistication: MAX-SAT, count-only, random-weight, and multiple weighted-SC variants all produce identical results. Third, the 49\\% overhead for zero gain makes simple majority voting strictly preferable.\n\nThe capability trap may not be permanent. Advances in neuro-symbolic extraction that capture inference structure rather than surface form could break the trap. Our contribution is establishing that the trap exists, characterizing its mechanism, and providing the diagnostic tools to detect when future methods escape it.\n\n%% =============================================================\n%% REFERENCES (placeholder)\n%% =============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Chen et al.(2023)]{chen2023universal}\nChen, X., et al. (2023). Universal Self-Consistency for Large Language Model Generation. \\textit{arXiv:2311.17311}.\n\n\\bibitem[Cobbe et al.(2021)]{cobbe2021gsm8k}\nCobbe, K., et al. (2021). Training Verifiers to Solve Math Word Problems. \\textit{arXiv:2110.14168}.\n\n\\bibitem[Lightman et al.(2023)]{lightman2023lets}\nLightman, H., et al. (2023). Let's Verify Step by Step. \\textit{arXiv:2305.20050}.\n\n\\bibitem[Olausson et al.(2023)]{olausson2023linc}\nOlausson, T., et al. (2023). LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. \\textit{EMNLP 2023}.\n\n\\bibitem[Pan et al.(2023)]{pan2023logiclm}\nPan, L., et al. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. \\textit{EMNLP 2023 Findings}.\n\n\\bibitem[Rogers et al.(2020)]{rogers2020primer}\nRogers, A., et al. (2020). A Primer in BERTology: What We Know About How BERT Works. \\textit{TACL}.\n\n\\bibitem[Taubenfeld et al.(2024)]{taubenfeld2024}\nTaubenfeld, A., et al. (2024). Systematic Biases in LLM Simulations of Debates. \\textit{arXiv:2402.04049}.\n\n\\bibitem[Wang et al.(2023)]{wang2023selfconsistency}\nWang, X., et al. (2023). Self-Consistency Improves Chain of Thought Reasoning in Language Models. \\textit{ICLR 2023}.\n\n\\end{thebibliography}\n\n%% =============================================================\n%% APPENDIX\n%% =============================================================\n\\appendix\n\\section{Extended Results}\n\n\\subsection{QwQ-32B Operating Regime}\n\nQwQ-32B as a full reasoning model produces near-deterministic outputs. Across 46 problems: nominal $C_0 = 10.3\\%$ (format noise), effective $C_0 = 2.6\\%$ (true reasoning divergence). On AIME ($n{=}22$): $\\Delta = 0.0$pp. On ProofWriter ($n{=}17$): $\\Delta = -5.9$pp (noise at SE $\\approx 12$pp). The diversity ratio between QwQ-32B and Qwen-14B is $17.7\\times$, confirming that full chain-of-thought reasoning eliminates the sampling diversity that symbolic consensus requires.\n\n\\subsection{Qwen Within-Family Scaling}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-Qwen scaling on FOLIO+ProofWriter ($n{=}60$ each, $K{=}12$).}\n\\label{tab:qwen-scaling}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & $C_0$ & SC & SICA & $\\Delta$pp & Extr. Rate \\\\\n\\midrule\nQwen-7B & 65\\% & 55.0 & 53.3 & $-$1.7 & 82\\% \\\\\nQwen-14B & 53\\% & 76.2 & 76.5 & +0.25 & 89\\% \\\\\nQwen-72B & 15\\% & 86.7 & 86.7 & 0.0 & 93\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel scale produces three effects: (1) SC accuracy increases, (2) $C_0$ decreases (stronger models agree more), (3) extraction quality improves (fewer contradictions, higher extraction rate). Yet SICA$-$SC $\\approx 0$ at all scales: the trap holds from weak to strong.\n\n\\subsection{GSM8K Cross-Domain Pilot}\n\nQwen-14B on GSM8K ($n{=}30$, $K{=}12$): SC $= 86.7\\%$, SICA $= 86.7\\%$, $\\Delta = 0.0$pp. $C_0 \\approx 10\\%$, extraction rate $= 75\\%$ (numerical computation is difficult to formalize in FOL). Zero discordant pairs. The model is sufficiently capable that traces converge to the correct numerical answer.\n\n\\subsection{Overhead Percentiles}\n\nMedian overhead: 48.9\\%. P90 overhead: 57.6\\% (longer FOLIO traces require more extraction time). Trace generation dominates at 51.3\\% of total wall time; constraint extraction at 47.0\\%.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "6621fdb7-58ee-481a-b450-d6caf0d5ee4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_con…",
  "leafUuid": "49e207d5-77af-4a25-a309-15a4d8f17c3b",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic invariant consensus paper",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Assistant

_source line 23 · 2026-05-17T15:29:53.408Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49e207d5-77af-4a25-a309-15a4d8f17c3b",
  "isSidechain": false,
  "requestId": "req_011Cb8NyFjnxpaTmHX1HuwYk",
  "type": "assistant",
  "uuid": "a7c41135-6db4-4a61-b18d-0bf25ac4f493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017394KFQuXiJkZfZPD7oURP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9579,
      "cache_read_input_tokens": 42734,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 42734,
          "cache_creation_input_tokens": 9579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9579
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

_source line 24 · 2026-05-17T15:29:55.053Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013YXZZAuPpqyfn2ubVzRShN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c41135-6db4-4a61-b18d-0bf25ac4f493",
  "isSidechain": false,
  "requestId": "req_011Cb8NyFjnxpaTmHX1HuwYk",
  "type": "assistant",
  "uuid": "7636cdfe-c18b-42b3-9e18-6fb9e92cb175",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017394KFQuXiJkZfZPD7oURP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9579,
      "cache_read_input_tokens": 42734,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 42734,
          "cache_creation_input_tokens": 9579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9579
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

_source line 25 · 2026-05-17T15:29:56.876Z_

<details><summary>↩ Tool result · `toolu_013YXZZAuPpqyfn2ubVzRShN`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined 
on input line 55.


Package natbib Warning: Citation `chen2023universal' on page 2 undefined on inp
ut line 55.


Package natbib Warning: Citation `taubenfeld2024' on page 2 undefined on input 
line 55.


Package natbib Warning: Citation `pan2023logiclm' on page 2 undefined on input 
line 58.


Package natbib Warning: Citation `olausson2023linc' on page 2 undefined on inpu
t line 58.


Package natbib Warning: Citation `cobbe2021gsm8k' on page 2 undefined on input 
line 61.


Package natbib Warning: Citation `lightman2023lets' on page 2 undefined on inpu
t line 61.


Package natbib Warning: Citation `rogers2020primer' on page 2 undefined on inpu
t line 64.

[2]
Overfull \hbox (7.60504pt too wide) in paragraph at lines 99--100
 []\T1/cmr/bx/n/10.95 Models.[] \T1/cmr/m/n/10.95 Instruction-scale: Qwen2.5-14
B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-

LaTeX Warning: Reference `tab:main' on page 3 undefined on input line 107.

[3]

LaTeX Warning: Reference `tab:constraint-quality' on page 4 undefined on input 
line 146.


LaTeX Warning: Reference `fig:f2-description' on page 4 undefined on input line
 146.


LaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 179.

[4]

LaTeX Warning: Reference `tab:tiebreak' on page 5 undefined on input line 208.


LaTeX Warning: Reference `sec:k-ablation' on page 5 undefined on input line 229
.

[5]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 292.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 292.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 292.


LaTeX Warning: Reference `fig:f4-description' on page 6 undefined on input line
 295.

[6] [7]
Underfull \hbox (badness 4108) in paragraph at lines 389--390
[]\T1/cmr/m/n/10.95 Taubenfeld, A., et al. (2024). Sys-tem-atic Bi-ases in LLM 
Sim-u-la-tions of De-bates.

LaTeX Warning: `h' float specifier changed to `ht'.

[8]

Package natbib Warning: There were undefined citations.

[9] (./paper.aux

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
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0900
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0900
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0900.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf
 Ok) ) ) )
(some charht values had to be adjusted by as much as 0.07498pt)
Font metrics written on ecrm0900.tfm.
Output written on ecrm0900.600gf (256 characters, 46448 bytes).
Transcript written on ecrm0900.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk: successfully generated.
 &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex
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
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (9 pages, 283865 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))
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
Overfull \hbox (7.60504pt too wide) in paragraph at lines 99--100
 []\T1/cmr/bx/n/10.95 Models.[] \T1/cmr/m/n/10.95 Instruction-scale: Qwen2.5-14
B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-
[3]

LaTeX Warning: Reference `fig:f2-description' on page 4 undefined on input line
 146.

[4] [5]

Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 292.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `subscript' on input line 292.


Package hyperref Warning: Token not allowed in a PDF string (Unicode):
(hyperref)                removing `math shift' on input line 292.


LaTeX Warning: Reference `fig:f4-description' on page 6 undefined on input line
 295.

[6] [7]
Underfull \hbox (badness 4108) in paragraph at lines 389--390
[]\T1/cmr/m/n/10.95 Taubenfeld, A., et al. (2024). Sys-tem-atic Bi-ases in LLM 
Sim-u-la-tions of De-bates.

LaTeX Warning: `h' float specifier changed to `ht'.

[8] [9] (./paper.aux)

LaTeX Warning: There were undefined references.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20
25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive
2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli
ve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex
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
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (9 pages, 287278 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7636cdfe-c18b-42b3-9e18-6fb9e92cb175",
  "isSidechain": false,
  "promptId": "ebc51706-61b4-447a-8627-c0ef50ebb14e",
  "type": "user",
  "uuid": "9b8e2b43-2b15-4c4f-8f26-3048faad0c42",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined \non input line 55.\n\n\nPackage natbib Warning: Citation `chen2023universal' on page 2 undefined on inp\nut line 55.\n\n\nPackage natbib Warning: Citation `taubenfeld2024' on page 2 undefined on input \nline 55.\n\n\nPackage natbib Warning: Citation `pan2023logiclm' on page 2 undefined on input \nline 58.\n\n\nPackage natbib Warning: Citation `olausson2023linc' on page 2 undefined on inpu\nt line 58.\n\n\nPackage natbib Warning: Citation `cobbe2021gsm8k' on page 2 undefined on input \nline 61.\n\n\nPackage natbib Warning: Citation `lightman2023lets' on page 2 undefined on inpu\nt line 61.\n\n\nPackage natbib Warning: Citation `rogers2020primer' on page 2 undefined on inpu\nt line 64.\n\n[2]\nOverfull \\hbox (7.60504pt too wide) in paragraph at lines 99--100\n []\\T1/cmr/bx/n/10.95 Models.[] \\T1/cmr/m/n/10.95 Instruction-scale: Qwen2.5-14\nB-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-\n\nLaTeX Warning: Reference `tab:main' on page 3 undefined on input line 107.\n\n[3]\n\nLaTeX Warning: Reference `tab:constraint-quality' on page 4 undefined on input \nline 146.\n\n\nLaTeX Warning: Reference `fig:f2-description' on page 4 undefined on input line\n 146.\n\n\nLaTeX Warning: Reference `tab:ablation' on page 4 undefined on input line 179.\n\n[4]\n\nLaTeX Warning: Reference `tab:tiebreak' on page 5 undefined on input line 208.\n\n\nLaTeX Warning: Reference `sec:k-ablation' on page 5 undefined on input line 229\n.\n\n[5]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 292.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 292.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 292.\n\n\nLaTeX Warning: Reference `fig:f4-description' on page 6 undefined on input line\n 295.\n\n[6] [7]\nUnderfull \\hbox (badness 4108) in paragraph at lines 389--390\n[]\\T1/cmr/m/n/10.95 Taubenfeld, A., et al. (2024). Sys-tem-atic Bi-ases in LLM \nSim-u-la-tions of De-bates.\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8]\n\nPackage natbib Warning: There were undefined citations.\n\n[9] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0900\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0900\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0900.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.07498pt)\nFont metrics written on ecrm0900.tfm.\nOutput written on ecrm0900.600gf (256 characters, 46448 bytes).\nTranscript written on ecrm0900.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 283865 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (7.60504pt too wide) in paragraph at lines 99--100\n []\\T1/cmr/bx/n/10.95 Models.[] \\T1/cmr/m/n/10.95 Instruction-scale: Qwen2.5-14\nB-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct-\n[3]\n\nLaTeX Warning: Reference `fig:f2-description' on page 4 undefined on input line\n 146.\n\n[4] [5]\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 292.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `subscript' on input line 292.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 292.\n\n\nLaTeX Warning: Reference `fig:f4-description' on page 6 undefined on input line\n 295.\n\n[6] [7]\nUnderfull \\hbox (badness 4108) in paragraph at lines 389--390\n[]\\T1/cmr/m/n/10.95 Taubenfeld, A., et al. (2024). Sys-tem-atic Bi-ases in LLM \nSim-u-la-tions of De-bates.\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[8] [9] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0900.600pk> &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk> &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk> &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1000.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1000.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1000.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1200.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1728.600pk>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (9 pages, 287278 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7636cdfe-c18b-42b3-9e18-6fb9e92cb175",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_con…",
  "leafUuid": "9b8e2b43-2b15-4c4f-8f26-3048faad0c42",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic invariant consensus paper",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Assistant

_source line 28 · 2026-05-17T15:30:10.859Z_

编译成功，生成 9 页 PDF。有两个 undefined reference warnings（`fig:f2-description` 和 `fig:f4-description`）是因为论文中以文字描述代替了实际图片文件（dream 模式无实际图），不影响可审性。

输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best/paper.pdf`（9 页，287KB）。

论文覆盖了 `experiment_data.json` 中全部 18 个实验条目：主表 T1（8 个 model×domain 条件 + QwQ-32B）、机制分析（constraint precision F2 scatter n=307、constraint ablation T3 n=804）、tiebreak 分析 T4、K 敏感性表、温度消融 §5、$C_0$ diagnostic F4、Logic-LM baseline、Weighted SC baseline、overhead 分析、case studies 定性结论，以及 appendix 中的 within-Qwen scaling 和 GSM8K cross-domain。所有定量 claim 均来自 JSON 数据，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b8e2b43-2b15-4c4f-8f26-3048faad0c42",
  "isSidechain": false,
  "requestId": "req_011Cb8NyiQQnS6F3FJ8eL3Bq",
  "type": "assistant",
  "uuid": "c807a487-8821-40db-a947-90d65653e5a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/dream_reports/dream_20260517T144412/best",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpUzuCTbp2Q6jrcLPKQL92",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9183,
      "cache_read_input_tokens": 52313,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 52313,
          "cache_creation_input_tokens": 9183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9183
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260517T144412 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_con…",
  "leafUuid": "c807a487-8821-40db-a947-90d65653e5a5",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate symbolic invariant consensus paper",
  "sessionId": "20f4d989-b56d-4594-ae93-7274d38db3de"
}
```

---
