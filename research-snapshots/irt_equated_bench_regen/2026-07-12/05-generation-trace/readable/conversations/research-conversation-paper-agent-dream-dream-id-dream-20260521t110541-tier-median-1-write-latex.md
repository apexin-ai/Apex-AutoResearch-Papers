# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/ca482af7-7948-4e9b-b65f-42d545ce5059.jsonl`
- **Structured JSON:** [`b9ce1781743da03cb96d.json`](../../sessions/b9/b9ce1781743da03cb96d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T11:34:12.948Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T11:34:12.948Z",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/experiment_data.json`（先 Read 此文件）\n- Venue：emnlp-2026\n- Narrative guidance：核心 6-benchmark DIF finding 成立（C% 17.5–30.8%，全部 ≥45× above random）， 但 reviewer 在两个方向施压：(1) temporal coarseness—binary 2023/2024 split 可能掩盖 within-year 变异， 要求 quarterly sensitivity 或承认 limitation；(2) IRT misfit—98% 模型 |Lz|>2， 至少一个 reviewer 要求 multidimensional IRT robustness check 而非仅在 limitations 中讨论。 Simpson's paradox（OR 1.48→0.76）被视为 interesting 但 reviewer 质疑 CTT difficulty/discrimination 是否是正确 conditioning variables，要求 sensitivity analysis。Claim 1 措辞从 'temporal instability' 软化为 'systematic cohort-conditional differences in item functioning'。Audit protocol 从 numbered contribution 降级为 discussion recommendation。Benchmark 间 C% 变异（17.5–30.8%） 需要 moderator-level 解释。Semi-synthetic（ΔTPR=0.43 at p=0.5）被接受。 RL robustness（N=13 reasoning-RL）被标记为 underpowered。 预期 reviewer_avg ≈ 3.4，1–2 major concerns（temporal coarseness + IRT misfit）， borderline accept / major revision。Camera-ready 需补充 quarterly split + MIRT pilot 或 rebuttal 承诺。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T11:34:12.952Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T11:34:12.952Z",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-21T11:34:12.973Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/experiment_data.json`（先 Read 此文件）
- Venue：emnlp-2026
- Narrative guidance：核心 6-benchmark DIF finding 成立（C% 17.5–30.8%，全部 ≥45× above random）， 但 reviewer 在两个方向施压：(1) temporal coarseness—binary 2023/2024 split 可能掩盖 within-year 变异， 要求 quarterly sensitivity 或承认 limitation；(2) IRT misfit—98% 模型 |Lz|>2， 至少一个 reviewer 要求 multidimensional IRT robustness check 而非仅在 limitations 中讨论。 Simpson's paradox（OR 1.48→0.76）被视为 interesting 但 reviewer 质疑 CTT difficulty/discrimination 是否是正确 conditioning variables，要求 sensitivity analysis。Claim 1 措辞从 'temporal instability' 软化为 'systematic cohort-conditional differences in item functioning'。Audit protocol 从 numbered contribution 降级为 discussion recommendation。Benchmark 间 C% 变异（17.5–30.8%） 需要 moderator-level 解释。Semi-synthetic（ΔTPR=0.43 at p=0.5）被接受。 RL robustness（N=13 reasoning-RL）被标记为 underpowered。 预期 reviewer_avg ≈ 3.4，1–2 major concerns（temporal coarseness + IRT misfit）， borderline accept / major revision。Camera-ready 需补充 quarterly split + MIRT pilot 或 rebuttal 承诺。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "787adc94-f09c-4e2b-9bc0-63507c42a6cc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T11:34:12.972Z_

```json
{
  "parentUuid": "787adc94-f09c-4e2b-9bc0-63507c42a6cc",
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
  "uuid": "3b1f47d2-c952-48d9-9698-291c9849ad20",
  "timestamp": "2026-05-21T11:34:12.972Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T11:34:12.972Z_

```json
{
  "parentUuid": "3b1f47d2-c952-48d9-9698-291c9849ad20",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4863b2f4-791c-4dab-81c1-d458972eef62",
  "timestamp": "2026-05-21T11:34:12.972Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
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
  "aiTitle": "Generate simulated paper for dream session",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Assistant

_source line 7 · 2026-05-21T11:34:16.892Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4863b2f4-791c-4dab-81c1-d458972eef62",
  "isSidechain": false,
  "requestId": "req_011CbFeEmiHaucDN8sLunpGB",
  "type": "assistant",
  "uuid": "8ec22fc7-afca-41ee-a6d8-8c281f38b039",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hEup9X7BSgswgb8EHQdzf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
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
          "output_tokens": 218,
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

_source line 8 · 2026-05-21T11:34:17.853Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UFgNoeRd7ewHeFNRisSG74`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ec22fc7-afca-41ee-a6d8-8c281f38b039",
  "isSidechain": false,
  "requestId": "req_011CbFeEmiHaucDN8sLunpGB",
  "type": "assistant",
  "uuid": "29497275-098d-4872-bf82-cdf7d71887b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hEup9X7BSgswgb8EHQdzf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
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
          "output_tokens": 218,
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

_source line 9 · 2026-05-21T11:34:18.148Z_

<details><summary>↩ Tool result · `toolu_01UFgNoeRd7ewHeFNRisSG74`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU 5219×12508 response matrix MH-DIF，temporal/ability/within-family cohort",
5	    "results": {
6	      "temporal_ets_c_pct": 30.8,
7	      "temporal_n_c_items": 3855,
8	      "temporal_fpr_on_li_clean": 0.312,
9	      "temporal_enrichment_vs_li": 0.97,
10	      "ability_ets_c_pct": 2.7,
11	      "ability_enrichment": 1.16,
12	      "within_family_llama2v3_c_pct": 58.7,
13	      "within_family_mistral_mixtral_c_pct": 36.2,
14	      "domain_spearman_rho": 0.29,
15	      "domain_spearman_p": 0.028,
16	      "sanity_random_split_c_pct": 0.21,
17	      "temporal_ability_jaccard": 0.016,
18	      "n_ref": 1080,
19	      "n_foc": 807,
20	      "bh_fdr_items_removed": 4,
21	      "negative_disc_sensitivity_delta": -1.2
22	    },
23	    "tables": [
24	      "Table 1: 4-way sensitivity matrix — temporal/ability × ±negative-disc items: C%, enrichment, FPR",
25	      "Table 2: Within-family DIF — Llama-2v3, Mistral-Mixtral: C%, Jaccard with temporal",
26	      "Table 3: Domain-specificity — top/bottom 10 subjects by C% with accuracy delta"
27	    ],
28	    "figures": [],
29	    "analysis": "30.8% 是 headline number。Reviewer 接受量级但施压两点：(a) binary temporal split 的 coarseness，(b) domain ρ=0.29 的 causal interpretation。Rebuttal 需要 item-level decomposition + quarterly IFT 作为 sensitivity。Within-family 结果是双刃剑—— 支持 confound control 但 58.7% 可能暗示 capability jump 而非 contamination。\n\n\nMedian 档核心 temporal DIF 成立但数值略低于 actual best（30.8% vs 31.3%）， 因为 median 档对 cross_bench_c_pct_max 的上界在 33%，中值预期在 30% 附近。 Random split 0.21% 确保信号真实（ratio≈147×）。Ability split 仅 2.7% 说明 DIF 不是 ability 差异的 artifact。Domain ρ=0.29 是弱正相关——reviewer 会追问 item-level decomposition 是否证明 improvement 是 confound，但 median 档下 plan_019/027 的 ability confound 仅 ~3pp （在 [2,5] 范围），说明 confound 存在但小。Within-family Llama-2v3 的 58.7% 确认 family-level jump 比 temporal 更极端，但也暴露了混入 capability gain 的可能。 Enrichment≈0.97 支持 ground truth critique。\n"
30	  },
31	  {
32	    "name": "rl_robustness_validation",
33	    "description": "DIF 对 alignment-RL (N=477) 和 reasoning-RL (N=13) 的鲁棒性验证",
34	    "results": {
35	      "sft_baseline_c_pct": 30.8,
36	      "alignment_rl_cohort_c_pct": 29.4,
37	      "alignment_rl_jaccard_vs_sft": 0.83,
38	      "reasoning_rl_added_c_pct": 30.2,
39	      "reasoning_rl_added_jaccard": 0.91,
40	      "constat_auroc_non_rl": 0.71,
41	      "constat_auroc_reasoning_rl": 0.59,
42	      "mink_auroc_non_rl": 0.68,
43	      "mink_auroc_reasoning_rl": 0.53,
44	      "delong_p_dif_vs_constat": 0.082,
45	      "tost_equivalence_p": 0.14,
46	      "tost_verdict": "inconclusive",
47	      "power_detection_boundary_p": 0.48,
48	      "bootstrap_ci_dif_auroc": [
49	        0.67,
50	        0.78
51	      ],
52	      "bootstrap_ci_constat_auroc": [
53	        0.42,
54	        0.73
55	      ],
56	      "partial_exploitation_tpr_p10": 0.72,
57	      "partial_exploitation_tpr_p07": 0.58,
58	      "partial_exploitation_tpr_p05": 0.41
59	    },
60	    "tables": [
61	      "Table: DIF flag retention — SFT / alignment-RL / +reasoning-RL: C%, Jaccard",
62	      "Table: Per-detector AUROC (DIF/ConStat/Min-K%) × model type, 95% bootstrap CI"
63	    ],
64	    "figures": [],
65	    "analysis": "Alignment-RL 验证成功。Reasoning-RL 是已知弱点但非 fatal——paper 已将 regeneration 从 core contribution 移除。Reviewer 会在 minor revision 中要求措辞调整。 Partial exploitation curve 支持 semi-synthetic framework 的 dose-response 发现。\n\n\nAlignment-RL（DPO/ORPO）不涉及 PPO clipping 或 NLL gap contraction，DIF 对此鲁棒 是预期结果——Jaccard 0.83 表明 flag 集合高度稳定。但 reasoning-RL（GRPO/PPO）仅 N=13， 远低于统计显著性需求。DeLong p=0.082（>0.05）和 TOST p=0.14 均不确定—— CI 太宽（ConStat bootstrap [0.42, 0.73] 跨越 chance level）。在 median 档下 reviewer 不将此视为 major concern（reasoning-RL 不是 paper 核心论点），但要求 soften claim 从 \"RL-robust\" 到 \"robust to alignment RL; reasoning-RL未验证\"。 Power analysis 显示 p<0.48 时 DIF power 快速下降，与 semi-synthetic 一致。\n"
66	  },
67	  {
68	    "name": "constat_perturbation_eval",
69	    "description": "ConStat perturbation 检测基线：218 MMLU items 语义等价重写",
70	    "results": {
71	      "n_items_reformulated": 218,
72	      "detection_rate_non_rl": 0.19,
73	      "detection_rate_rl": 0.07,
74	      "fdr_controlled_fpr": 0.038,
75	      "avg_effect_size_non_rl_d": 0.74,
76	      "avg_effect_size_rl_d": 0.31,
77	      "paraphrase_quality_human_eval": 0.82,
78	      "difficulty_shift_from_reformulation": 0.06,
79	      "overlap_dif_flags_jaccard": 0.14
80	    },
81	    "tables": [
82	      "Table: ConStat detection rates by model type — SFT / alignment-RL / reasoning-RL"
83	    ],
84	    "figures": [],
85	    "analysis": "ConStat 提供 complementary baseline 但 coverage 太低。Paper 中作为 comparison 使用， 不作为独立 contribution。Median 档 reviewer 不会对此施压——bonus analysis。\n\n\nConStat 在 non-RL 模型上检测 19% 是合理的——perturbation-based 方法对 verbatim memorization 敏感但对 differential functioning 不敏感。RL 模型降至 7% 确认 理论预测（NLL gap contraction 削弱 perturbation signal）。与 DIF 的 Jaccard 仅 0.14 说明两种方法检测本质不同的信号——DIF 是 group-level differential functioning， ConStat 是 individual-level memorization。这在 median 档下作为 Related Work 中的 empirical comparison 有用，但不够强以支撑独立 contribution。覆盖仅 218/12508 items（1.7%）， representativeness 受限。\n"
86	  },
87	  {
88	    "name": "dvd_generation_variance_eval",
89	    "description": "DVD generation variance 检测：12 models × 50 responses/item via temperature sampling",
90	    "results": {
91	      "n_models": 12,
92	      "n_responses_per_item": 50,
93	      "bimodal_detection_rate": 0.13,
94	      "correlation_with_dif_flags": 0.17,
95	      "snr_large_models": 2.1,
96	      "snr_small_models": 0.8,
97	      "detection_verbatim": 0.24,
98	      "detection_variant": 0.09,
99	      "gpu_hours_used": 62
100	    },
101	    "tables": [
102	      "Table: DVD detection rates by contamination type (verbatim/variant/none)"
103	    ],
104	    "figures": [],
105	    "analysis": "DVD 确认 DIF 和 generation variance 是正交信号。低 correlation 支持 paper 的 reframing：DIF ≠ contamination detector。在 median 档下作为 appendix 材料。\n\n\nDVD 检测 13% items 的 bimodal distribution——信号集中在大模型（SNR=2.1）， 小模型噪声淹没信号（SNR=0.8）。与 DIF 相关性仅 0.17 证实两种方法测量不同构念。 对 verbatim contamination 24% vs variant contamination 9% 的差异说明 DVD 更适合 detection 而非 differential functioning 分析。在 median 档下这是 informative negative： ensemble 不会显著提升 DIF，因为信号维度不同。62 GPU hours 是可接受成本但 scalability 有限。\n"
106	  },
107	  {
108	    "name": "ensemble_fusion",
109	    "description": "DIF + ConStat + DVD 三信号融合评估",
110	    "results": {
111	      "ensemble_auroc": 0.73,
112	      "dif_only_auroc": 0.7,
113	      "constat_only_auroc": 0.64,
114	      "dvd_only_auroc": 0.57,
115	      "auroc_gain_over_dif": 0.03,
116	      "majority_voting_precision": 0.79,
117	      "majority_voting_recall": 0.52,
118	      "fusion_weight_cv_stability": "±28% across folds",
119	      "uniform_weight_auroc": 0.72,
120	      "optimized_weight_auroc": 0.73,
121	      "fpr": 0.09
122	    },
123	    "tables": [
124	      "Table: Per-signal and ensemble AUROC/precision/recall comparison"
125	    ],
126	    "figures": [],
127	    "analysis": "Ensemble negative result 加强了 paper 的 pivoted framing。 三种方法检测不同东西→DIF 的 unique value 是 group-level differential functioning， 不需要与 individual-level detectors 竞争。\n\n\nEnsemble 仅比 DIF-only 提升 0.03 AUROC——marginal gain 不值得额外复杂度。 三种方法 flag 的 item 集合 overlap 太低（pairwise Jaccard <0.20），majority voting recall 仅 0.52。Fusion weights 跨 fold 不稳定（±28%），uniform 和 optimized 无差别。 这是 informative negative result：三种检测器捕获不同信号维度，强行融合没有意义。 在 median 档下 paper 正确地放弃 ensemble，将 DIF reframe 为 diagnostic tool 而非 contamination detector。Reviewer 不会追问——ensemble 不是 expected contribution。\n"
128	  },
129	  {
130	    "name": "cross_benchmark_gsm8k",
131	    "description": "GSM8K DIF 复制 + GSM1K ground truth 验证（1319 items × 6702 models）",
132	    "results": {
133	      "temporal_c_pct_standard": 18.3,
134	      "temporal_c_pct_external": 45.8,
135	      "sanity_c_pct": 0.28,
136	      "standard_external_spearman": 0.92,
137	      "semi_synthetic_standard_delta_tpr_p10": 0.79,
138	      "semi_synthetic_external_delta_tpr_p10": 0.5,
139	      "gsm1k_n_models": 33,
140	      "gsm1k_pearson_r": -0.46,
141	      "gsm1k_pearson_p": 0.007,
142	      "gsm1k_spearman_rho": -0.39,
143	      "gsm1k_spearman_p": 0.025,
144	      "gsm1k_partial_r": -0.37,
145	      "gsm1k_partial_p": 0.035,
146	      "gsm1k_direction": "NEGATIVE",
147	      "gsm1k_leave_one_out_r_range": [
148	        -0.52,
149	        -0.36
150	      ]
151	    },
152	    "tables": [
153	      "Table: GSM8K temporal DIF — C%, sample sizes, random control",
154	      "Table: GSM1K correlation — Pearson/Spearman/partial with CIs"
155	    ],
156	    "figures": [],
157	    "analysis": "GSM8K 提供 cross-benchmark 支持但 C%=18.3% vs MMLU 30.8% 的差异需要解释。 GSM1K negative correlation demoted to exploratory。Reviewer 在 median 档下 不会对此 major concern——GSM8K 是 supplementary evidence。\n\n\nGSM8K C%=18.3% 在 cross_bench_c_pct_min [15,19] 范围内。作为单一数学 domain， DIF rate 低于多 domain benchmark（MMLU 30.8%）——domain homogeneity 减少了 construct-irrelevant variance。Semi-synthetic ΔTPR=0.79 确认 framework 可移植。 GSM1K correlation r=-0.46 方向为负——与 contamination hypothesis 相反。 这在 median 档下被 reviewer 要求 demote 到 exploratory（N=33，CI 宽 [-0.52, -0.36]）。 Paper 的解释（DIF measures differential functioning, not contamination）合理但 需要更多 evidence 支撑。Leave-one-out 稳定排除单一 outlier 驱动。\n"
158	  },
159	  {
160	    "name": "bifactor_irt_equating_pilot",
161	    "description": "MMLU bifactor IRT 模型拟合 + anchor item equating pipeline pilot",
162	    "results": {
163	      "convergence": "partial — reduced to 5-factor from 57",
164	      "rmsea": 0.034,
165	      "cfi": 0.73,
166	      "tli": 0.7,
167	      "srmr": 0.062,
168	      "general_factor_variance_pct": 41,
169	      "specific_factor_range": [
170	        0.03,
171	        0.18
172	      ],
173	      "anchor_items_selected": 0,
174	      "pipeline_status": "killed"
175	    },
176	    "tables": [
177	      "Table: IRT model fit — unidimensional vs 5-factor bifactor: RMSEA/CFI/TLI/SRMR"
178	    ],
179	    "figures": [],
180	    "analysis": "Bifactor 失败是 median 档 IRT misfit 攻击面的根源。Reviewer 会要求至少在 5 个 subject 上跑 within-subject MIRT 作为 robustness check，或在 rebuttal 中提供 MH nonparametric conditioning 不依赖 IRT fit 的详细 argument。 这是 median 档的 1-2 个 major concerns 之一。\n\n\n57 subjects 使得 full bifactor 不收敛，降至 5-factor（STEM/humanities/social/professional/other） 后 fit 仍差（CFI=0.73 远低于 0.90 标准）。General factor 仅解释 41% variance—— MMLU 本质高度多维。Anchor item selection 在 poor fit 下不可靠，equating pipeline 无法推进。 实验被 kill。在 median 档下这个 negative result 是 reviewer 施压 IRT misfit concern 的 关键根据——\"你们自己的 bifactor 尝试也失败了，unidimensional IRT misfit 是真实问题\"。 Paper 需要回应：MH 是 nonparametric 方法，不直接依赖 IRT fit，但 conditioning variable （cross-subject total score）的 validity 在 multidimensional context 中减弱。\n"
181	  },
182	  {
183	    "name": "item_generation_calibration",
184	    "description": "LLM 生成替换 items + student simulation 校准",
185	    "results": {
186	      "n_items_generated": 150,
187	      "n_subjects": 5,
188	      "difficulty_corr_student_sim": 0.56,
189	      "difficulty_corr_real_models": 0.41,
190	      "expert_pass_rate": 0.58,
191	      "construct_drift_subjects": 2,
192	      "adequate_subjects": 3,
193	      "calibration_status": "insufficient for equating"
194	    },
195	    "tables": [
196	      "Table: Per-subject generation quality — difficulty ρ, pass rate, construct coverage"
197	    ],
198	    "figures": [],
199	    "analysis": "Item generation negative result 加强了 audit protocol 的 human-in-the-loop 设计。 在 median 档下不是 attack surface——paper 正确地将此从 contribution 移除。\n\n\nStudent simulation difficulty ρ=0.56 低于 literature 报告的 0.75-0.82——MMLU 的 domain diversity 使得 difficulty 预测更难。Expert pass rate 仅 58% 说明 LLM generation 在保持 construct equivalence 上仍有困难。2/5 subjects 出现 construct drift（生成 items 测量了不同知识维度）。Real model ρ=0.41 进一步确认 calibration 不足以支撑自动替换。 在 median 档下这个 negative result 支持 paper 的 framing 调整：audit protocol 推荐 monitoring + flagging，而非 automatic replacement。Reviewer 不会追问—— paper 已放弃 replacement 作为 contribution。\n"
200	  },
201	  {
202	    "name": "cumulative_bayesian_dif",
203	    "description": "Sinharay et al. 2006 累积贝叶斯 DIF 先验 simulation（4 administrations）",
204	    "results": {
205	      "individual_power": 0.39,
206	      "cumulative_2_power": 0.53,
207	      "cumulative_3_power": 0.67,
208	      "cumulative_4_power": 0.73,
209	      "fpr_all_stages": 0.044,
210	      "delta_simulated": 1.0,
211	      "n_per_group": 80
212	    },
213	    "tables": [
214	      "Table: Cumulative power by administration count × effect size (δ=0.8/1.0/1.2/1.4)"
215	    ],
216	    "figures": [],
217	    "analysis": "Simulation 支持 longitudinal monitoring 但不是 paper-level contribution。 Median 档 reviewer 不施压——appendix 材料。\n\n\nSimulation 结果符合理论预期——evidence accumulation 将 medium effect（δ=1.0） 的 power 从单次 0.39 提升到 4 次后 0.73。FPR 保持 <0.05。 在 median 档下 reviewer 接受 simulation 的 directional insight 但不给 contribution credit——simulation-only，无 empirical validation。Paper 正确地放在 appendix。 对 audit protocol 的 \"regular monitoring\" 建议提供了理论支撑。\n"
218	  },
219	  {
220	    "name": "graceful_degradation_analysis",
221	    "description": "渐进式 item 替换下的 ranking stability / reliability / construct coverage 退化",
222	    "results": {
223	      "rho_5pct": 0.9991,
224	      "rho_10pct": 0.9982,
225	      "rho_20pct": 0.9958,
226	      "rho_31pct": 0.9941,
227	      "rho_50pct": 0.9847,
228	      "shr_5pct": 0.9928,
229	      "shr_10pct": 0.9921,
230	      "shr_20pct": 0.9896,
231	      "shr_31pct": 0.9862,
232	      "shr_50pct": 0.9735,
233	      "construct_gap_onset": "20%",
234	      "construct_gaps_at_31pct": "2-3 domains underrepresented"
235	    },
236	    "tables": [
237	      "Table: Validity metrics at 5%/10%/20%/31%/50% replacement — ρ, SHR, coverage gaps"
238	    ],
239	    "figures": [],
240	    "analysis": "Graceful degradation 定量支撑 \"instability ≠ invalidity\"。ρ=0.994 at 31% 是 strong evidence。但 median 档 reviewer 会追问 tension：如果 MMLU 如此冗余， 是否应该 recommend benchmark compression？Discussion 需要处理。\n\n\nρ=0.994 at 31% 在 ranking_rho_after_removal [0.993, 0.998] 范围内。 MMLU 的 massive redundancy 使得即使移除近三分之一 items，ranking 仍极其稳定。 SHR 从 0.993 降至 0.986——轻微但 measurable 的 reliability 损失。 Construct coverage 在 20%+ 开始出现 gaps——DIF-C items 在某些 domain 集中， 移除后这些 domain 的 representation 不足。50% 替换时 ρ 仍高（0.985）但 construct validity 已有明显空洞。这支持 \"instability ≠ invalidity\" 的核心 framing—— ranking 稳定，但 construct representation 最终会受影响。\n"
241	  },
242	  {
243	    "name": "item_focused_trees",
244	    "description": "Item-Focused Trees — continuous release date 作为 covariate 的非参数 DIF",
245	    "results": {
246	      "ift_mh_spearman": 0.78,
247	      "ift_mh_jaccard_matched": 0.71,
248	      "breakpoint": "2023-Q4 to 2024-Q1",
249	      "nonlinear_pattern": true,
250	      "additional_items_flagged": 127,
251	      "computational_cost_ratio_vs_mh": 8.3,
252	      "models_with_precise_date_pct": 37
253	    },
254	    "tables": [
255	      "Table: IFT vs MH — agreement rates, unique flags, breakpoint analysis"
256	    ],
257	    "figures": [],
258	    "analysis": "IFT 是 temporal coarseness concern 的最直接回应。Breakpoint 在 2023-Q4 部分缓解 \"binary split arbitrary\" 的 critique。但 reviewer 可能仍不满足—— quarterly MH analysis 是 camera-ready 或 rebuttal 的 preparation item。\n\n\nIFT 与 MH 高度一致（ρ=0.78, Jaccard=0.71），说明 binary split 捕获了主要信号。 IFT 额外识别 127 items——DIF 效应在 2023-Q4 突变的 items（MH 的 binary threshold 恰好 在 split point 附近 miss 了 borderline cases）。关键发现：nonlinear temporal pattern， 大部分 DIF 集中在 2023-Q4 到 2024-Q1，暗示 LLM capability jump 在此窗口最密集。 在 median 档下 IFT 是 temporal coarseness concern 的 partial answer——binary split 捕获了 breakpoint 的正确位置。但仅 37% 模型有 precise date 限制了 IFT 的覆盖率， 且计算成本 8.3× higher than MH。Reviewer 可能接受但仍要求 quarterly MH 作为 更直接的 sensitivity check。\n"
259	  },
260	  {
261	    "name": "architecture_stratified_dif",
262	    "description": "仅 decoder-only 模型的 DIF + IRT fit diagnostic",
263	    "results": {
264	      "decoder_only_n": 5222,
265	      "decoder_only_pct": 99.9,
266	      "decoder_only_c_pct": 30.8,
267	      "full_c_pct": 30.8,
268	      "jaccard_decoder_vs_full": 1.0,
269	      "irt_rmsea_decoder": 0.041,
270	      "irt_cfi_decoder": 0.68,
271	      "irt_rmsea_full": 0.041,
272	      "irt_cfi_full": 0.68,
273	      "non_decoder_removed": 5
274	    },
275	    "tables": [
276	      "Table: Architecture composition — decoder-only vs other",
277	      "Table: IRT fit — full vs decoder-only: RMSEA/CFI/TLI"
278	    ],
279	    "figures": [],
280	    "analysis": "Architecture 实验关闭一个 concern 但暴露另一个。IRT misfit（CFI=0.68） 成为 median 档 reviewer 的 major concern 之一。Paper 需要在 Discussion 中 argue MH 是 nonparametric（不依赖 IRT fit），但 conditioning variable （cross-subject total score）的 construct validity 在 multidimensional context 减弱。\n\n\nMETABENCH MMLU 99.9% decoder-only——移除 5 个非 decoder 模型后 C% 和 IRT fit 完全不变（Jaccard=1.0）。Architecture heterogeneity 是 non-issue。 但更重要的发现是 IRT fit 也未改善（RMSEA=0.041, CFI=0.68 仍 poor）—— misfit 来源是 57-subject multidimensionality，不是 architecture 混合。 这在 median 档下关闭了 architecture 攻击面但打开了 IRT misfit 攻击面—— reviewer 从 \"architecture confound?\" 转向 \"如果 IRT fit poor，MH conditioning 可靠吗？\"\n"
281	  },
282	  {
283	    "name": "semi_synthetic_contamination_validation",
284	    "description": "Known contamination injection into real response matrix — DIF detection power",
285	    "results": {
286	      "temporal_external_tpr_p0": 0.314,
287	      "temporal_external_tpr_p03": 0.51,
288	      "temporal_external_tpr_p05": 0.74,
289	      "temporal_external_tpr_p07": 0.95,
290	      "temporal_external_tpr_p10": 1.0,
291	      "temporal_external_fpr": 0.308,
292	      "temporal_external_delta_tpr_p05": 0.43,
293	      "temporal_external_delta_tpr_p10": 0.69,
294	      "ability_external_delta_tpr_p10": 0.29,
295	      "standard_mh_fpr_inflation_p10": 0.31,
296	      "cross_subject_matching_delta_fpr": 0.0,
297	      "n_clean_items": 500,
298	      "n_injected_items": 150
299	    },
300	    "tables": [
301	      "Table: ΔTPR/ΔFPR at p=0/0.3/0.5/0.7/1.0 — standard vs cross-subject matching",
302	      "Table: FPR stability — cross-subject (constant) vs within-subject (inflating)"
303	    ],
304	    "figures": [],
305	    "analysis": "Semi-synthetic framework (Claim 3) 是 paper 最 well-defended claim。 ΔTPR=0.43 是 \"moderate\"——足以证明 detection power 但不 dramatic。 Cross-subject ΔFPR=0.0 是 clean, publishable result。Reviewer concern 限于 injection artificiality——paper 在 limitations 中承认即可。\n\n\nMedian 档 ΔTPR=0.43 at p=0.5（在 [0.35, 0.50] 范围内），低于 best 档的 ~0.51 因为 median 档预设 semi-synthetic 信号稍弱。p=1.0 时 ΔTPR=0.69 仍表明 full exploitation 可被可靠检测。Baseline FPR=0.308 反映 temporal DIF 的 ~31% background rate（不是 false positive 而是 pre-existing DIF）。Cross-subject matching ΔFPR=0.0 是 framework 的核心创新—— 完全消除了 matching variable contamination。Within-subject matching FPR inflation 0.31 确认了 within-subject 方法的问题。在 median 档下 reviewer 接受 framework 但质疑 injection mechanism（incorrect→correct flip）是否代表 real contamination 的作用方式。 这是 acknowledged limitation，not fatal。ΔTPR=0.43 足够支撑 \"moderate detection power\" 但 reviewer 不会将此视为 \"strong\" detection。\n"
306	  },
307	  {
308	    "name": "multi_benchmark_temporal_dif",
309	    "description": "6 benchmarks (MMLU/WinoGrande/TruthfulQA/ARC/GSM8K/HellaSwag) temporal DIF",
310	    "results": {
311	      "mmlu_c_pct": 30.8,
312	      "mmlu_n_items": 12508,
313	      "mmlu_random": 0.2,
314	      "winogrande_c_pct": 29.1,
315	      "winogrande_n_items": 1267,
316	      "winogrande_random": 0.35,
317	      "truthfulqa_c_pct": 27.8,
318	      "truthfulqa_n_items": 817,
319	      "truthfulqa_random": 0.41,
320	      "arc_c_pct": 24.5,
321	      "arc_n_items": 1172,
322	      "arc_random": 0.55,
323	      "gsm8k_c_pct": 18.3,
324	      "gsm8k_n_items": 1319,
325	      "gsm8k_random": 0.28,
326	      "hellaswag_c_pct": 17.5,
327	      "hellaswag_n_items": 10042,
328	      "hellaswag_random": 0.3,
329	      "range": "17.5–30.8%",
330	      "all_random_below_1pct": true,
331	      "min_enrichment_vs_random": 50,
332	      "n_benchmarks": 6,
333	      "c_pct_coefficient_of_variation": 0.22
334	    },
335	    "tables": [
336	      "Table: 6-benchmark temporal DIF — C%, N items, N ref/foc, random control, enrichment ratio",
337	      "Table: Benchmark characteristics — domain count, item format, mean difficulty, C%"
338	    ],
339	    "figures": [],
340	    "analysis": "6-benchmark 是最强 generalizability argument。但 C% 变异 17.5–30.8% 是 median 档 reviewer 的关注焦点——\"为什么 HellaSwag 17.5% 而 MMLU 30.8%？\" Rebuttal 需准备 descriptive moderator analysis。N=6 太少做 formal test——acknowledge 为 limitation， 建议 future work with more benchmarks。\n\n\n6 benchmark 全部显示显著 temporal DIF（min 17.5%, max 30.8%），满足 median 档 cross_bench_c_pct_min [15,19] 和 cross_bench_c_pct_max [28,33]。所有 random controls <1% 确认信号真实。但变异显著（CV=0.22）：高 C% 群（MMLU 30.8%, WinoGrande 29.1%,  TruthfulQA 27.8%）与低 C% 群（GSM8K 18.3%, HellaSwag 17.5%）之间存在 ~13pp 差距。 Pattern 的直觉解释：multi-domain benchmarks（MMLU 57 subjects, WinoGrande 多场景） 比 single-domain（GSM8K 纯数学）有更多 construct-irrelevant variance 源；HellaSwag 虽有 10042 items 但 domain 高度同质（常识推理），C% 最低。Reviewer 在 median 档下 要求 moderator analysis（item count, domain count, item format, difficulty distribution 作为 C% predictor），但 N=6 benchmarks 使 formal regression 不可行——只能做 descriptive。 这是 median 档的 signature concern：结果成立但需要更多结构解释。\n"
341	  },
342	  {
343	    "name": "permutation_null_c_rate",
344	    "description": "1000× permutation test：随机重分配 temporal labels 建立 C% null distribution",
345	    "results": {
346	      "n_permutations": 1000,
347	      "null_mean_c_pct": 0.45,
348	      "null_sd_c_pct": 0.16,
349	      "null_max_c_pct": 1.14,
350	      "observed_c_pct": 30.8,
351	      "z_score": 189.7,
352	      "empirical_p": "<0.001 (0/1000)",
353	      "group_sizes_preserved": true
354	    },
355	    "tables": [
356	      "Table: Permutation null summary — mean, SD, max, observed, z, p"
357	    ],
358	    "figures": [],
359	    "analysis": "Permutation null 关闭了 statistical significance 攻击面。在 median 档下 reviewer 满意后转向 temporal coarseness——更深层的 interpretation 问题。 这是 defensive experiment，必要但不 exciting。\n\n\nPermutation null 均值 0.45%（SD=0.16%）远低于观测 30.8%（z≈190），0/1000 permutations exceed observed → empirical p<0.001。Null 最大值 1.14%（比 random-split 0.21% 略高， 因为 permutation preserves unequal group sizes 1080:807 而非 equal split）。 这比 random-split control 更严格地回答了 \"is 31% above chance?\"——definitively yes。 Permutation 保留了 group size 不平衡但 shuffle 了 temporal 标签，所以 null 测试的是 \"temporal 标签是否 informative\"。在 median 档下 reviewer 接受这个结果， statistical significance 不再是攻击面。但 reviewer 会从 significance 转向 interpretation： \"okay it's real, but is binary split the right granularity?\"\n"
360	  },
361	  {
362	    "name": "odds_ratio_regression_transparency",
363	    "description": "4 logistic regression models 揭示 Simpson's paradox + OR/CI/R² 全透明报告",
364	    "results": {
365	      "m1_acc_delta_or_per_010": 1.48,
366	      "m1_acc_delta_ci": [
367	        1.14,
368	        1.93
369	      ],
370	      "m1_mcfadden_r2": 0.0008,
371	      "m1_nagelkerke_r2": 0.0013,
372	      "m2_acc_delta_or_per_010": 0.76,
373	      "m2_difficulty_or_per_010": 0.79,
374	      "m2_discrimination_or_per_010": 1.48,
375	      "m2_mcfadden_r2": 0.04,
376	      "m2_nagelkerke_r2": 0.068,
377	      "m3_item_delta_or_per_010": 1.07,
378	      "m3_mcfadden_r2": 0.0013,
379	      "m4_item_delta_or_per_010": 0.93,
380	      "m4_difficulty_or_per_010": 0.78,
381	      "m4_discrimination_or_per_010": 1.52,
382	      "m4_mcfadden_r2": 0.042,
383	      "simpsons_paradox": true,
384	      "or_flip_magnitude": 0.72,
385	      "lr_test_m1_vs_m2_chi2": 634,
386	      "lr_test_p": "<0.001",
387	      "best_model_r2": 0.042,
388	      "variance_unexplained": "~96%"
389	    },
390	    "tables": [
391	      "Table: Four logistic models — predictors, OR [95% CI], McFadden/Nagelkerke R², AIC",
392	      "Table: Simpson's paradox summary — M1 vs M2 sign flip with LR test"
393	    ],
394	    "figures": [],
395	    "analysis": "Simpson's paradox 在 median 档下从 main evidence 降级为 supplementary。 OR flip magnitude 0.72 在 range 下界——效应真实但不 dramatic。Reviewer 要求 sensitivity analysis（alternative confounders: item length, cognitive level, topic） 是 median 档的 signature concern 之一。R²=0.042 实际上支持 Claim 1—— DIF 是 item-specific 的，不能被简单 characteristics 解释。\n\nSimpson's paradox 清晰成立：M1 中 accuracy delta 正向预测 DIF（OR=1.48/0.10）， M2 加入 CTT difficulty/discrimination 后 OR 翻转为 0.76。Flip magnitude=|1.48-0.76|=0.72 在 [0.7, 1.1] 范围下界。这意味着 domain-level accuracy improvement 与 DIF 的表面正相关 被 item properties confound 驱动——difficulty 高且 discrimination 高的 items 更容易 show DIF 也更容易 show accuracy improvement。CTT discrimination 是最强 predictor （OR=1.48-1.52）。但 best model R²=0.042——96% variance unexplained，DIF 本质 item-specific，无简单 predictor。在 median 档下 reviewer 接受 Simpson's paradox 作为 interesting methodological insight 但施压两点：(a) CTT difficulty/discrimination 是否是正确 conditioning variables——sensitivity analysis with alternatives needed； (b) R² 如此低是否意味着 regression exercise 缺乏实际解释力。 Paper 将此从 main evidence 调整为 supplementary robustness check。\n"
396	  }
397	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29497275-098d-4872-bf82-cdf7d71887b5",
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "f7cc722f-b04b-4557-976d-4a840be1deb5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU 5219×12508 response matrix MH-DIF，temporal/ability/within-family cohort\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 30.8,\n      \"temporal_n_c_items\": 3855,\n      \"temporal_fpr_on_li_clean\": 0.312,\n      \"temporal_enrichment_vs_li\": 0.97,\n      \"ability_ets_c_pct\": 2.7,\n      \"ability_enrichment\": 1.16,\n      \"within_family_llama2v3_c_pct\": 58.7,\n      \"within_family_mistral_mixtral_c_pct\": 36.2,\n      \"domain_spearman_rho\": 0.29,\n      \"domain_spearman_p\": 0.028,\n      \"sanity_random_split_c_pct\": 0.21,\n      \"temporal_ability_jaccard\": 0.016,\n      \"n_ref\": 1080,\n      \"n_foc\": 807,\n      \"bh_fdr_items_removed\": 4,\n      \"negative_disc_sensitivity_delta\": -1.2\n    },\n    \"tables\": [\n      \"Table 1: 4-way sensitivity matrix — temporal/ability × ±negative-disc items: C%, enrichment, FPR\",\n      \"Table 2: Within-family DIF — Llama-2v3, Mistral-Mixtral: C%, Jaccard with temporal\",\n      \"Table 3: Domain-specificity — top/bottom 10 subjects by C% with accuracy delta\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"30.8% 是 headline number。Reviewer 接受量级但施压两点：(a) binary temporal split 的 coarseness，(b) domain ρ=0.29 的 causal interpretation。Rebuttal 需要 item-level decomposition + quarterly IFT 作为 sensitivity。Within-family 结果是双刃剑—— 支持 confound control 但 58.7% 可能暗示 capability jump 而非 contamination。\\n\\n\\nMedian 档核心 temporal DIF 成立但数值略低于 actual best（30.8% vs 31.3%）， 因为 median 档对 cross_bench_c_pct_max 的上界在 33%，中值预期在 30% 附近。 Random split 0.21% 确保信号真实（ratio≈147×）。Ability split 仅 2.7% 说明 DIF 不是 ability 差异的 artifact。Domain ρ=0.29 是弱正相关——reviewer 会追问 item-level decomposition 是否证明 improvement 是 confound，但 median 档下 plan_019/027 的 ability confound 仅 ~3pp （在 [2,5] 范围），说明 confound 存在但小。Within-family Llama-2v3 的 58.7% 确认 family-level jump 比 temporal 更极端，但也暴露了混入 capability gain 的可能。 Enrichment≈0.97 支持 ground truth critique。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"DIF 对 alignment-RL (N=477) 和 reasoning-RL (N=13) 的鲁棒性验证\",\n    \"results\": {\n      \"sft_baseline_c_pct\": 30.8,\n      \"alignment_rl_cohort_c_pct\": 29.4,\n      \"alignment_rl_jaccard_vs_sft\": 0.83,\n      \"reasoning_rl_added_c_pct\": 30.2,\n      \"reasoning_rl_added_jaccard\": 0.91,\n      \"constat_auroc_non_rl\": 0.71,\n      \"constat_auroc_reasoning_rl\": 0.59,\n      \"mink_auroc_non_rl\": 0.68,\n      \"mink_auroc_reasoning_rl\": 0.53,\n      \"delong_p_dif_vs_constat\": 0.082,\n      \"tost_equivalence_p\": 0.14,\n      \"tost_verdict\": \"inconclusive\",\n      \"power_detection_boundary_p\": 0.48,\n      \"bootstrap_ci_dif_auroc\": [\n        0.67,\n        0.78\n      ],\n      \"bootstrap_ci_constat_auroc\": [\n        0.42,\n        0.73\n      ],\n      \"partial_exploitation_tpr_p10\": 0.72,\n      \"partial_exploitation_tpr_p07\": 0.58,\n      \"partial_exploitation_tpr_p05\": 0.41\n    },\n    \"tables\": [\n      \"Table: DIF flag retention — SFT / alignment-RL / +reasoning-RL: C%, Jaccard\",\n      \"Table: Per-detector AUROC (DIF/ConStat/Min-K%) × model type, 95% bootstrap CI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Alignment-RL 验证成功。Reasoning-RL 是已知弱点但非 fatal——paper 已将 regeneration 从 core contribution 移除。Reviewer 会在 minor revision 中要求措辞调整。 Partial exploitation curve 支持 semi-synthetic framework 的 dose-response 发现。\\n\\n\\nAlignment-RL（DPO/ORPO）不涉及 PPO clipping 或 NLL gap contraction，DIF 对此鲁棒 是预期结果——Jaccard 0.83 表明 flag 集合高度稳定。但 reasoning-RL（GRPO/PPO）仅 N=13， 远低于统计显著性需求。DeLong p=0.082（>0.05）和 TOST p=0.14 均不确定—— CI 太宽（ConStat bootstrap [0.42, 0.73] 跨越 chance level）。在 median 档下 reviewer 不将此视为 major concern（reasoning-RL 不是 paper 核心论点），但要求 soften claim 从 \\\"RL-robust\\\" 到 \\\"robust to alignment RL; reasoning-RL未验证\\\"。 Power analysis 显示 p<0.48 时 DIF power 快速下降，与 semi-synthetic 一致。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat perturbation 检测基线：218 MMLU items 语义等价重写\",\n    \"results\": {\n      \"n_items_reformulated\": 218,\n      \"detection_rate_non_rl\": 0.19,\n      \"detection_rate_rl\": 0.07,\n      \"fdr_controlled_fpr\": 0.038,\n      \"avg_effect_size_non_rl_d\": 0.74,\n      \"avg_effect_size_rl_d\": 0.31,\n      \"paraphrase_quality_human_eval\": 0.82,\n      \"difficulty_shift_from_reformulation\": 0.06,\n      \"overlap_dif_flags_jaccard\": 0.14\n    },\n    \"tables\": [\n      \"Table: ConStat detection rates by model type — SFT / alignment-RL / reasoning-RL\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"ConStat 提供 complementary baseline 但 coverage 太低。Paper 中作为 comparison 使用， 不作为独立 contribution。Median 档 reviewer 不会对此施压——bonus analysis。\\n\\n\\nConStat 在 non-RL 模型上检测 19% 是合理的——perturbation-based 方法对 verbatim memorization 敏感但对 differential functioning 不敏感。RL 模型降至 7% 确认 理论预测（NLL gap contraction 削弱 perturbation signal）。与 DIF 的 Jaccard 仅 0.14 说明两种方法检测本质不同的信号——DIF 是 group-level differential functioning， ConStat 是 individual-level memorization。这在 median 档下作为 Related Work 中的 empirical comparison 有用，但不够强以支撑独立 contribution。覆盖仅 218/12508 items（1.7%）， representativeness 受限。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance 检测：12 models × 50 responses/item via temperature sampling\",\n    \"results\": {\n      \"n_models\": 12,\n      \"n_responses_per_item\": 50,\n      \"bimodal_detection_rate\": 0.13,\n      \"correlation_with_dif_flags\": 0.17,\n      \"snr_large_models\": 2.1,\n      \"snr_small_models\": 0.8,\n      \"detection_verbatim\": 0.24,\n      \"detection_variant\": 0.09,\n      \"gpu_hours_used\": 62\n    },\n    \"tables\": [\n      \"Table: DVD detection rates by contamination type (verbatim/variant/none)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD 确认 DIF 和 generation variance 是正交信号。低 correlation 支持 paper 的 reframing：DIF ≠ contamination detector。在 median 档下作为 appendix 材料。\\n\\n\\nDVD 检测 13% items 的 bimodal distribution——信号集中在大模型（SNR=2.1）， 小模型噪声淹没信号（SNR=0.8）。与 DIF 相关性仅 0.17 证实两种方法测量不同构念。 对 verbatim contamination 24% vs variant contamination 9% 的差异说明 DVD 更适合 detection 而非 differential functioning 分析。在 median 档下这是 informative negative： ensemble 不会显著提升 DIF，因为信号维度不同。62 GPU hours 是可接受成本但 scalability 有限。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD 三信号融合评估\",\n    \"results\": {\n      \"ensemble_auroc\": 0.73,\n      \"dif_only_auroc\": 0.7,\n      \"constat_only_auroc\": 0.64,\n      \"dvd_only_auroc\": 0.57,\n      \"auroc_gain_over_dif\": 0.03,\n      \"majority_voting_precision\": 0.79,\n      \"majority_voting_recall\": 0.52,\n      \"fusion_weight_cv_stability\": \"±28% across folds\",\n      \"uniform_weight_auroc\": 0.72,\n      \"optimized_weight_auroc\": 0.73,\n      \"fpr\": 0.09\n    },\n    \"tables\": [\n      \"Table: Per-signal and ensemble AUROC/precision/recall comparison\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble negative result 加强了 paper 的 pivoted framing。 三种方法检测不同东西→DIF 的 unique value 是 group-level differential functioning， 不需要与 individual-level detectors 竞争。\\n\\n\\nEnsemble 仅比 DIF-only 提升 0.03 AUROC——marginal gain 不值得额外复杂度。 三种方法 flag 的 item 集合 overlap 太低（pairwise Jaccard <0.20），majority voting recall 仅 0.52。Fusion weights 跨 fold 不稳定（±28%），uniform 和 optimized 无差别。 这是 informative negative result：三种检测器捕获不同信号维度，强行融合没有意义。 在 median 档下 paper 正确地放弃 ensemble，将 DIF reframe 为 diagnostic tool 而非 contamination detector。Reviewer 不会追问——ensemble 不是 expected contribution。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K DIF 复制 + GSM1K ground truth 验证（1319 items × 6702 models）\",\n    \"results\": {\n      \"temporal_c_pct_standard\": 18.3,\n      \"temporal_c_pct_external\": 45.8,\n      \"sanity_c_pct\": 0.28,\n      \"standard_external_spearman\": 0.92,\n      \"semi_synthetic_standard_delta_tpr_p10\": 0.79,\n      \"semi_synthetic_external_delta_tpr_p10\": 0.5,\n      \"gsm1k_n_models\": 33,\n      \"gsm1k_pearson_r\": -0.46,\n      \"gsm1k_pearson_p\": 0.007,\n      \"gsm1k_spearman_rho\": -0.39,\n      \"gsm1k_spearman_p\": 0.025,\n      \"gsm1k_partial_r\": -0.37,\n      \"gsm1k_partial_p\": 0.035,\n      \"gsm1k_direction\": \"NEGATIVE\",\n      \"gsm1k_leave_one_out_r_range\": [\n        -0.52,\n        -0.36\n      ]\n    },\n    \"tables\": [\n      \"Table: GSM8K temporal DIF — C%, sample sizes, random control\",\n      \"Table: GSM1K correlation — Pearson/Spearman/partial with CIs\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K 提供 cross-benchmark 支持但 C%=18.3% vs MMLU 30.8% 的差异需要解释。 GSM1K negative correlation demoted to exploratory。Reviewer 在 median 档下 不会对此 major concern——GSM8K 是 supplementary evidence。\\n\\n\\nGSM8K C%=18.3% 在 cross_bench_c_pct_min [15,19] 范围内。作为单一数学 domain， DIF rate 低于多 domain benchmark（MMLU 30.8%）——domain homogeneity 减少了 construct-irrelevant variance。Semi-synthetic ΔTPR=0.79 确认 framework 可移植。 GSM1K correlation r=-0.46 方向为负——与 contamination hypothesis 相反。 这在 median 档下被 reviewer 要求 demote 到 exploratory（N=33，CI 宽 [-0.52, -0.36]）。 Paper 的解释（DIF measures differential functioning, not contamination）合理但 需要更多 evidence 支撑。Leave-one-out 稳定排除单一 outlier 驱动。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"MMLU bifactor IRT 模型拟合 + anchor item equating pipeline pilot\",\n    \"results\": {\n      \"convergence\": \"partial — reduced to 5-factor from 57\",\n      \"rmsea\": 0.034,\n      \"cfi\": 0.73,\n      \"tli\": 0.7,\n      \"srmr\": 0.062,\n      \"general_factor_variance_pct\": 41,\n      \"specific_factor_range\": [\n        0.03,\n        0.18\n      ],\n      \"anchor_items_selected\": 0,\n      \"pipeline_status\": \"killed\"\n    },\n    \"tables\": [\n      \"Table: IRT model fit — unidimensional vs 5-factor bifactor: RMSEA/CFI/TLI/SRMR\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor 失败是 median 档 IRT misfit 攻击面的根源。Reviewer 会要求至少在 5 个 subject 上跑 within-subject MIRT 作为 robustness check，或在 rebuttal 中提供 MH nonparametric conditioning 不依赖 IRT fit 的详细 argument。 这是 median 档的 1-2 个 major concerns 之一。\\n\\n\\n57 subjects 使得 full bifactor 不收敛，降至 5-factor（STEM/humanities/social/professional/other） 后 fit 仍差（CFI=0.73 远低于 0.90 标准）。General factor 仅解释 41% variance—— MMLU 本质高度多维。Anchor item selection 在 poor fit 下不可靠，equating pipeline 无法推进。 实验被 kill。在 median 档下这个 negative result 是 reviewer 施压 IRT misfit concern 的 关键根据——\\\"你们自己的 bifactor 尝试也失败了，unidimensional IRT misfit 是真实问题\\\"。 Paper 需要回应：MH 是 nonparametric 方法，不直接依赖 IRT fit，但 conditioning variable （cross-subject total score）的 validity 在 multidimensional context 中减弱。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"LLM 生成替换 items + student simulation 校准\",\n    \"results\": {\n      \"n_items_generated\": 150,\n      \"n_subjects\": 5,\n      \"difficulty_corr_student_sim\": 0.56,\n      \"difficulty_corr_real_models\": 0.41,\n      \"expert_pass_rate\": 0.58,\n      \"construct_drift_subjects\": 2,\n      \"adequate_subjects\": 3,\n      \"calibration_status\": \"insufficient for equating\"\n    },\n    \"tables\": [\n      \"Table: Per-subject generation quality — difficulty ρ, pass rate, construct coverage\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation negative result 加强了 audit protocol 的 human-in-the-loop 设计。 在 median 档下不是 attack surface——paper 正确地将此从 contribution 移除。\\n\\n\\nStudent simulation difficulty ρ=0.56 低于 literature 报告的 0.75-0.82——MMLU 的 domain diversity 使得 difficulty 预测更难。Expert pass rate 仅 58% 说明 LLM generation 在保持 construct equivalence 上仍有困难。2/5 subjects 出现 construct drift（生成 items 测量了不同知识维度）。Real model ρ=0.41 进一步确认 calibration 不足以支撑自动替换。 在 median 档下这个 negative result 支持 paper 的 framing 调整：audit protocol 推荐 monitoring + flagging，而非 automatic replacement。Reviewer 不会追问—— paper 已放弃 replacement 作为 contribution。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Sinharay et al. 2006 累积贝叶斯 DIF 先验 simulation（4 administrations）\",\n    \"results\": {\n      \"individual_power\": 0.39,\n      \"cumulative_2_power\": 0.53,\n      \"cumulative_3_power\": 0.67,\n      \"cumulative_4_power\": 0.73,\n      \"fpr_all_stages\": 0.044,\n      \"delta_simulated\": 1.0,\n      \"n_per_group\": 80\n    },\n    \"tables\": [\n      \"Table: Cumulative power by administration count × effect size (δ=0.8/1.0/1.2/1.4)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simulation 支持 longitudinal monitoring 但不是 paper-level contribution。 Median 档 reviewer 不施压——appendix 材料。\\n\\n\\nSimulation 结果符合理论预期——evidence accumulation 将 medium effect（δ=1.0） 的 power 从单次 0.39 提升到 4 次后 0.73。FPR 保持 <0.05。 在 median 档下 reviewer 接受 simulation 的 directional insight 但不给 contribution credit——simulation-only，无 empirical validation。Paper 正确地放在 appendix。 对 audit protocol 的 \\\"regular monitoring\\\" 建议提供了理论支撑。\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"渐进式 item 替换下的 ranking stability / reliability / construct coverage 退化\",\n    \"results\": {\n      \"rho_5pct\": 0.9991,\n      \"rho_10pct\": 0.9982,\n      \"rho_20pct\": 0.9958,\n      \"rho_31pct\": 0.9941,\n      \"rho_50pct\": 0.9847,\n      \"shr_5pct\": 0.9928,\n      \"shr_10pct\": 0.9921,\n      \"shr_20pct\": 0.9896,\n      \"shr_31pct\": 0.9862,\n      \"shr_50pct\": 0.9735,\n      \"construct_gap_onset\": \"20%\",\n      \"construct_gaps_at_31pct\": \"2-3 domains underrepresented\"\n    },\n    \"tables\": [\n      \"Table: Validity metrics at 5%/10%/20%/31%/50% replacement — ρ, SHR, coverage gaps\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Graceful degradation 定量支撑 \\\"instability ≠ invalidity\\\"。ρ=0.994 at 31% 是 strong evidence。但 median 档 reviewer 会追问 tension：如果 MMLU 如此冗余， 是否应该 recommend benchmark compression？Discussion 需要处理。\\n\\n\\nρ=0.994 at 31% 在 ranking_rho_after_removal [0.993, 0.998] 范围内。 MMLU 的 massive redundancy 使得即使移除近三分之一 items，ranking 仍极其稳定。 SHR 从 0.993 降至 0.986——轻微但 measurable 的 reliability 损失。 Construct coverage 在 20%+ 开始出现 gaps——DIF-C items 在某些 domain 集中， 移除后这些 domain 的 representation 不足。50% 替换时 ρ 仍高（0.985）但 construct validity 已有明显空洞。这支持 \\\"instability ≠ invalidity\\\" 的核心 framing—— ranking 稳定，但 construct representation 最终会受影响。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees — continuous release date 作为 covariate 的非参数 DIF\",\n    \"results\": {\n      \"ift_mh_spearman\": 0.78,\n      \"ift_mh_jaccard_matched\": 0.71,\n      \"breakpoint\": \"2023-Q4 to 2024-Q1\",\n      \"nonlinear_pattern\": true,\n      \"additional_items_flagged\": 127,\n      \"computational_cost_ratio_vs_mh\": 8.3,\n      \"models_with_precise_date_pct\": 37\n    },\n    \"tables\": [\n      \"Table: IFT vs MH — agreement rates, unique flags, breakpoint analysis\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT 是 temporal coarseness concern 的最直接回应。Breakpoint 在 2023-Q4 部分缓解 \\\"binary split arbitrary\\\" 的 critique。但 reviewer 可能仍不满足—— quarterly MH analysis 是 camera-ready 或 rebuttal 的 preparation item。\\n\\n\\nIFT 与 MH 高度一致（ρ=0.78, Jaccard=0.71），说明 binary split 捕获了主要信号。 IFT 额外识别 127 items——DIF 效应在 2023-Q4 突变的 items（MH 的 binary threshold 恰好 在 split point 附近 miss 了 borderline cases）。关键发现：nonlinear temporal pattern， 大部分 DIF 集中在 2023-Q4 到 2024-Q1，暗示 LLM capability jump 在此窗口最密集。 在 median 档下 IFT 是 temporal coarseness concern 的 partial answer——binary split 捕获了 breakpoint 的正确位置。但仅 37% 模型有 precise date 限制了 IFT 的覆盖率， 且计算成本 8.3× higher than MH。Reviewer 可能接受但仍要求 quarterly MH 作为 更直接的 sensitivity check。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"仅 decoder-only 模型的 DIF + IRT fit diagnostic\",\n    \"results\": {\n      \"decoder_only_n\": 5222,\n      \"decoder_only_pct\": 99.9,\n      \"decoder_only_c_pct\": 30.8,\n      \"full_c_pct\": 30.8,\n      \"jaccard_decoder_vs_full\": 1.0,\n      \"irt_rmsea_decoder\": 0.041,\n      \"irt_cfi_decoder\": 0.68,\n      \"irt_rmsea_full\": 0.041,\n      \"irt_cfi_full\": 0.68,\n      \"non_decoder_removed\": 5\n    },\n    \"tables\": [\n      \"Table: Architecture composition — decoder-only vs other\",\n      \"Table: IRT fit — full vs decoder-only: RMSEA/CFI/TLI\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Architecture 实验关闭一个 concern 但暴露另一个。IRT misfit（CFI=0.68） 成为 median 档 reviewer 的 major concern 之一。Paper 需要在 Discussion 中 argue MH 是 nonparametric（不依赖 IRT fit），但 conditioning variable （cross-subject total score）的 construct validity 在 multidimensional context 减弱。\\n\\n\\nMETABENCH MMLU 99.9% decoder-only——移除 5 个非 decoder 模型后 C% 和 IRT fit 完全不变（Jaccard=1.0）。Architecture heterogeneity 是 non-issue。 但更重要的发现是 IRT fit 也未改善（RMSEA=0.041, CFI=0.68 仍 poor）—— misfit 来源是 57-subject multidimensionality，不是 architecture 混合。 这在 median 档下关闭了 architecture 攻击面但打开了 IRT misfit 攻击面—— reviewer 从 \\\"architecture confound?\\\" 转向 \\\"如果 IRT fit poor，MH conditioning 可靠吗？\\\"\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Known contamination injection into real response matrix — DIF detection power\",\n    \"results\": {\n      \"temporal_external_tpr_p0\": 0.314,\n      \"temporal_external_tpr_p03\": 0.51,\n      \"temporal_external_tpr_p05\": 0.74,\n      \"temporal_external_tpr_p07\": 0.95,\n      \"temporal_external_tpr_p10\": 1.0,\n      \"temporal_external_fpr\": 0.308,\n      \"temporal_external_delta_tpr_p05\": 0.43,\n      \"temporal_external_delta_tpr_p10\": 0.69,\n      \"ability_external_delta_tpr_p10\": 0.29,\n      \"standard_mh_fpr_inflation_p10\": 0.31,\n      \"cross_subject_matching_delta_fpr\": 0.0,\n      \"n_clean_items\": 500,\n      \"n_injected_items\": 150\n    },\n    \"tables\": [\n      \"Table: ΔTPR/ΔFPR at p=0/0.3/0.5/0.7/1.0 — standard vs cross-subject matching\",\n      \"Table: FPR stability — cross-subject (constant) vs within-subject (inflating)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic framework (Claim 3) 是 paper 最 well-defended claim。 ΔTPR=0.43 是 \\\"moderate\\\"——足以证明 detection power 但不 dramatic。 Cross-subject ΔFPR=0.0 是 clean, publishable result。Reviewer concern 限于 injection artificiality——paper 在 limitations 中承认即可。\\n\\n\\nMedian 档 ΔTPR=0.43 at p=0.5（在 [0.35, 0.50] 范围内），低于 best 档的 ~0.51 因为 median 档预设 semi-synthetic 信号稍弱。p=1.0 时 ΔTPR=0.69 仍表明 full exploitation 可被可靠检测。Baseline FPR=0.308 反映 temporal DIF 的 ~31% background rate（不是 false positive 而是 pre-existing DIF）。Cross-subject matching ΔFPR=0.0 是 framework 的核心创新—— 完全消除了 matching variable contamination。Within-subject matching FPR inflation 0.31 确认了 within-subject 方法的问题。在 median 档下 reviewer 接受 framework 但质疑 injection mechanism（incorrect→correct flip）是否代表 real contamination 的作用方式。 这是 acknowledged limitation，not fatal。ΔTPR=0.43 足够支撑 \\\"moderate detection power\\\" 但 reviewer 不会将此视为 \\\"strong\\\" detection。\\n\"\n  },\n  {\n    \"name\": \"multi_benchmark_temporal_dif\",\n    \"description\": \"6 benchmarks (MMLU/WinoGrande/TruthfulQA/ARC/GSM8K/HellaSwag) temporal DIF\",\n    \"results\": {\n      \"mmlu_c_pct\": 30.8,\n      \"mmlu_n_items\": 12508,\n      \"mmlu_random\": 0.2,\n      \"winogrande_c_pct\": 29.1,\n      \"winogrande_n_items\": 1267,\n      \"winogrande_random\": 0.35,\n      \"truthfulqa_c_pct\": 27.8,\n      \"truthfulqa_n_items\": 817,\n      \"truthfulqa_random\": 0.41,\n      \"arc_c_pct\": 24.5,\n      \"arc_n_items\": 1172,\n      \"arc_random\": 0.55,\n      \"gsm8k_c_pct\": 18.3,\n      \"gsm8k_n_items\": 1319,\n      \"gsm8k_random\": 0.28,\n      \"hellaswag_c_pct\": 17.5,\n      \"hellaswag_n_items\": 10042,\n      \"hellaswag_random\": 0.3,\n      \"range\": \"17.5–30.8%\",\n      \"all_random_below_1pct\": true,\n      \"min_enrichment_vs_random\": 50,\n      \"n_benchmarks\": 6,\n      \"c_pct_coefficient_of_variation\": 0.22\n    },\n    \"tables\": [\n      \"Table: 6-benchmark temporal DIF — C%, N items, N ref/foc, random control, enrichment ratio\",\n      \"Table: Benchmark characteristics — domain count, item format, mean difficulty, C%\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"6-benchmark 是最强 generalizability argument。但 C% 变异 17.5–30.8% 是 median 档 reviewer 的关注焦点——\\\"为什么 HellaSwag 17.5% 而 MMLU 30.8%？\\\" Rebuttal 需准备 descriptive moderator analysis。N=6 太少做 formal test——acknowledge 为 limitation， 建议 future work with more benchmarks。\\n\\n\\n6 benchmark 全部显示显著 temporal DIF（min 17.5%, max 30.8%），满足 median 档 cross_bench_c_pct_min [15,19] 和 cross_bench_c_pct_max [28,33]。所有 random controls <1% 确认信号真实。但变异显著（CV=0.22）：高 C% 群（MMLU 30.8%, WinoGrande 29.1%,  TruthfulQA 27.8%）与低 C% 群（GSM8K 18.3%, HellaSwag 17.5%）之间存在 ~13pp 差距。 Pattern 的直觉解释：multi-domain benchmarks（MMLU 57 subjects, WinoGrande 多场景） 比 single-domain（GSM8K 纯数学）有更多 construct-irrelevant variance 源；HellaSwag 虽有 10042 items 但 domain 高度同质（常识推理），C% 最低。Reviewer 在 median 档下 要求 moderator analysis（item count, domain count, item format, difficulty distribution 作为 C% predictor），但 N=6 benchmarks 使 formal regression 不可行——只能做 descriptive。 这是 median 档的 signature concern：结果成立但需要更多结构解释。\\n\"\n  },\n  {\n    \"name\": \"permutation_null_c_rate\",\n    \"description\": \"1000× permutation test：随机重分配 temporal labels 建立 C% null distribution\",\n    \"results\": {\n      \"n_permutations\": 1000,\n      \"null_mean_c_pct\": 0.45,\n      \"null_sd_c_pct\": 0.16,\n      \"null_max_c_pct\": 1.14,\n      \"observed_c_pct\": 30.8,\n      \"z_score\": 189.7,\n      \"empirical_p\": \"<0.001 (0/1000)\",\n      \"group_sizes_preserved\": true\n    },\n    \"tables\": [\n      \"Table: Permutation null summary — mean, SD, max, observed, z, p\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Permutation null 关闭了 statistical significance 攻击面。在 median 档下 reviewer 满意后转向 temporal coarseness——更深层的 interpretation 问题。 这是 defensive experiment，必要但不 exciting。\\n\\n\\nPermutation null 均值 0.45%（SD=0.16%）远低于观测 30.8%（z≈190），0/1000 permutations exceed observed → empirical p<0.001。Null 最大值 1.14%（比 random-split 0.21% 略高， 因为 permutation preserves unequal group sizes 1080:807 而非 equal split）。 这比 random-split control 更严格地回答了 \\\"is 31% above chance?\\\"——definitively yes。 Permutation 保留了 group size 不平衡但 shuffle 了 temporal 标签，所以 null 测试的是 \\\"temporal 标签是否 informative\\\"。在 median 档下 reviewer 接受这个结果， statistical significance 不再是攻击面。但 reviewer 会从 significance 转向 interpretation： \\\"okay it's real, but is binary split the right granularity?\\\"\\n\"\n  },\n  {\n    \"name\": \"odds_ratio_regression_transparency\",\n    \"description\": \"4 logistic regression models 揭示 Simpson's paradox + OR/CI/R² 全透明报告\",\n    \"results\": {\n      \"m1_acc_delta_or_per_010\": 1.48,\n      \"m1_acc_delta_ci\": [\n        1.14,\n        1.93\n      ],\n      \"m1_mcfadden_r2\": 0.0008,\n      \"m1_nagelkerke_r2\": 0.0013,\n      \"m2_acc_delta_or_per_010\": 0.76,\n      \"m2_difficulty_or_per_010\": 0.79,\n      \"m2_discrimination_or_per_010\": 1.48,\n      \"m2_mcfadden_r2\": 0.04,\n      \"m2_nagelkerke_r2\": 0.068,\n      \"m3_item_delta_or_per_010\": 1.07,\n      \"m3_mcfadden_r2\": 0.0013,\n      \"m4_item_delta_or_per_010\": 0.93,\n      \"m4_difficulty_or_per_010\": 0.78,\n      \"m4_discrimination_or_per_010\": 1.52,\n      \"m4_mcfadden_r2\": 0.042,\n      \"simpsons_paradox\": true,\n      \"or_flip_magnitude\": 0.72,\n      \"lr_test_m1_vs_m2_chi2\": 634,\n      \"lr_test_p\": \"<0.001\",\n      \"best_model_r2\": 0.042,\n      \"variance_unexplained\": \"~96%\"\n    },\n    \"tables\": [\n      \"Table: Four logistic models — predictors, OR [95% CI], McFadden/Nagelkerke R², AIC\",\n      \"Table: Simpson's paradox summary — M1 vs M2 sign flip with LR test\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Simpson's paradox 在 median 档下从 main evidence 降级为 supplementary。 OR flip magnitude 0.72 在 range 下界——效应真实但不 dramatic。Reviewer 要求 sensitivity analysis（alternative confounders: item length, cognitive level, topic） 是 median 档的 signature concern 之一。R²=0.042 实际上支持 Claim 1—— DIF 是 item-specific 的，不能被简单 characteristics 解释。\\n\\nSimpson's paradox 清晰成立：M1 中 accuracy delta 正向预测 DIF（OR=1.48/0.10）， M2 加入 CTT difficulty/discrimination 后 OR 翻转为 0.76。Flip magnitude=|1.48-0.76|=0.72 在 [0.7, 1.1] 范围下界。这意味着 domain-level accuracy improvement 与 DIF 的表面正相关 被 item properties confound 驱动——difficulty 高且 discrimination 高的 items 更容易 show DIF 也更容易 show accuracy improvement。CTT discrimination 是最强 predictor （OR=1.48-1.52）。但 best model R²=0.042——96% variance unexplained，DIF 本质 item-specific，无简单 predictor。在 median 档下 reviewer 接受 Simpson's paradox 作为 interesting methodological insight 但施压两点：(a) CTT difficulty/discrimination 是否是正确 conditioning variables——sensitivity analysis with alternatives needed； (b) R² 如此低是否意味着 regression exercise 缺乏实际解释力。 Paper 将此从 main evidence 调整为 supplementary robustness check。\\n\"\n  }\n]",
      "numLines": 397,
      "startLine": 1,
      "totalLines": 397
    }
  },
  "sourceToolAssistantUUID": "29497275-098d-4872-bf82-cdf7d71887b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T11:34:18.226Z_

<details><summary>↩ Tool result · `toolu_01D5qYVUPQDiG8tRm2Vr8Miu`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)
5	- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)
6	
7	## Paper Type
8	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
9	
10	## Core Claims (4 条, 可证伪)
11	
12	**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
13	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
14	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
15	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
16	
17	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
18	- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
19	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection" — now with direct empirical evidence, not just conceptual argument
20	
21	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
22	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
23	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
24	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
25	
26	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
27	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
28	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
29	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
30	4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.
31	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
32	- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.
33	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
34	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
35	
36	## Story Spine (v2 — no-pivot narrative)
37	
38	**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.
39	
40	**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**
41	
42	**What we find** (4 contributions, focused):
43	
44	1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."
45	
46	2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.
47	
48	3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.
49	
50	4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).
51	
52	**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance."
53	
54	## Scope Control (main body vs appendix)
55	
56	**MAIN BODY (4 claims + robustness)**:
57	- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
58	- §2 Related Work (45 papers, 5 clusters)
59	- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
60	- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
61	- §5 Discussion + Limitations
62	- §6 Conclusion
63	
64	**APPENDIX (pruned from main body)**:
65	- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
66	- RL robustness (plan_002) — N=13, underpowered
67	- Ensemble fusion (plan_003a/b/c) — negative, not executed
68	- Bifactor equating pilot — below target fit
69	- Item generation pilot — below benchmarks
70	- Graceful degradation — clean but supplementary
71	- Item-Focused Trees — robustness check, supplementary
72	- ConStat/DVD comparisons — complementary baselines
73	
74	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
75	
76	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
77	
78	## Venue Fit
79	
80	- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. "Empirical, not algorithmic" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.
81	
82	## Novelty Articulation (三层，显式化)
83	
84	MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:
85	
86	1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.
87	
88	2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).
89	
90	3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).
91	
92	**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."
93	
94	## Anticipated Reviewer Concerns (updated for pivot)
95	
96	1. **"31% could just mean models got better / ability confound inflates C%"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.
97	
98	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
99	
100	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
101	
102	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
103	
104	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.
105	
106	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
107	
108	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
109	
110	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
111	
112	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."
113	
114	10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.
115	
116	11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
117	
118	## Dropped from Original Framing
119	
120	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
121	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
122	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
123	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1a20dd8-a50a-4a4d-b949-f8ec9fe70446",
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "081f52d9-3d57-4f6f-a0ff-2131051a091d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 124,
      "startLine": 1,
      "totalLines": 124
    }
  },
  "sourceToolAssistantUUID": "f1a20dd8-a50a-4a4d-b949-f8ec9fe70446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:34:18.212Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D5qYVUPQDiG8tRm2Vr8Miu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cc722f-b04b-4557-976d-4a840be1deb5",
  "isSidechain": false,
  "requestId": "req_011CbFeEmiHaucDN8sLunpGB",
  "type": "assistant",
  "uuid": "f1a20dd8-a50a-4a4d-b949-f8ec9fe70446",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011hEup9X7BSgswgb8EHQdzf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12476,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
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
          "output_tokens": 218,
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "081f52d9-3d57-4f6f-a0ff-2131051a091d",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream session",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Assistant

_source line 14 · 2026-05-21T11:34:36.291Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me write the full LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the narrative guidance
3. Target median quality (reviewer avg ~3.4)
4. Follow the paper_framing.md structure
5. 8-page limit for EMNLP 2026

Let me organize the experiments into sections:

**Main body experiments:**
1. real_data_dif_mmlu - Claim 1 (temporal DIF)
2. multi_benchmark_temporal_dif - 6-benchmark generalization


3. permutation_null_c_rate - Statistical validation
4. architecture_stratified_dif - Architecture robustness
5. semi_synthetic_contamination_validation - Claim 3
6. cross_benchmark_gsm8k - GSM8K replication
7. odds_ratio_regression_transparency - Simpson's paradox
8. item_focused_trees - Temporal coarseness response
9. graceful_degradation_analysis - Ranking stability

**Supplementary/Appendix:**
10. rl_robustness_validation - RL robustness (underpowered)
11. constat_perturbation_eval - ConStat baseline
12. dv

_generation_variance_eval - DVD baseline
13. ensemble_fusion - Negative result
14. bifactor_irt_equating_pilot - Failed pilot
15. item_generation_calibration - Failed pilot
16. cumulative_bayesian_dif - Simulation only

Now I'm mapping out the full paper structure with all 16 experiments organized into coherent sections. I'll group the core experiments into main sections covering temporal DIF on MMLU, cross-benchmark generalization, and robustness checks, then place the underpowered and failed pilots in the appendix.

Organizing the remaining experiments into sections for semi-synthetic validation, Simpson's paradox analysis, item-focused trees, ranking stability, detection baselines, RL robustness, and IRT model fit...

Now I'm wrapping up with item generation calibration and cumulative Bayesian DIF before moving into the discussion, limitations, and conclusion sections. I want to make sure the paper is well-structured and readable while covering all the experimental work.

Writing the LaTeX...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "081f52d9-3d57-4f6f-a0ff-2131051a091d",
  "isSidechain": false,
  "requestId": "req_011CbFeFAYir65FdgtKWg1Qk",
  "type": "assistant",
  "uuid": "c0c2e5ac-fb54-4c74-815c-0ae69ca5fab6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msgMgCjeLsNoK2qZNxSC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17865,
      "cache_read_input_tokens": 24317,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17865
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

_source line 15 · 2026-05-21T11:34:36.294Z_

Now I have both files. Let me write the full LaTeX paper covering all 16 experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0c2e5ac-fb54-4c74-815c-0ae69ca5fab6",
  "isSidechain": false,
  "requestId": "req_011CbFeFAYir65FdgtKWg1Qk",
  "type": "assistant",
  "uuid": "75135603-79ac-417e-9e4b-d317e2d43221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msgMgCjeLsNoK2qZNxSC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17865,
      "cache_read_input_tokens": 24317,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17865
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

_source line 16 · 2026-05-21T11:34:38.264Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015g8eWjcuEaFbj2LyfT2fud`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75135603-79ac-417e-9e4b-d317e2d43221",
  "isSidechain": false,
  "requestId": "req_011CbFeFAYir65FdgtKWg1Qk",
  "type": "assistant",
  "uuid": "b070b7e1-df7f-4f17-8c7a-b31ae60248f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msgMgCjeLsNoK2qZNxSC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17865,
      "cache_read_input_tokens": 24317,
      "output_tokens": 959,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 959,
          "cache_read_input_tokens": 24317,
          "cache_creation_input_tokens": 17865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17865
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

_source line 17 · 2026-05-21T11:34:38.435Z_

<details><summary>↩ Tool result · `toolu_015g8eWjcuEaFbj2LyfT2fud`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b070b7e1-df7f-4f17-8c7a-b31ae60248f2",
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "7aca7015-77f7-4c5c-8dc6-71291c5df78e",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "b070b7e1-df7f-4f17-8c7a-b31ae60248f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T11:38:32.302Z_

<details open><summary>🔧 Tool call — Write · `toolu_01ArEQ7CRvPm3KTpk1AivmU3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Psychometric DIF Analysis Reveals Systematic Temporal Instability\\\\in LLM Benchmark Items at Scale}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen we compare language model scores across generations, we implicitly assume that benchmark items function equivalently for all model cohorts.\nWe test this assumption using Mantel--Haenszel Differential Item Functioning (MH-DIF) analysis on the METABENCH response matrix (5,219 models $\\times$ 12,508 MMLU items).\nWe find that 30.8\\% of MMLU items exhibit large DIF (ETS Category~C) between pre-2024 and 2024 model cohorts---a rate ${\\geq}147\\times$ the random-split baseline (0.21\\%) and confirmed by 1,000-fold permutation testing ($z{=}189.7$, $p{<}0.001$).\nThis instability generalizes across six benchmarks (C\\% range 17.5--30.8\\%, all ${\\geq}45\\times$ above random) and is not driven by capability improvement (${\\leq}$2.4\\,pp explained) or architecture heterogeneity (99.9\\% decoder-only, Jaccard${=}$1.0).\nWe show that the field's standard web-overlap ground truth cannot capture differential item functioning and propose a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR${=}$0.000).\nDespite 30.8\\% instability, benchmark rankings remain highly stable ($\\rho{=}$0.994 after removing all flagged items), revealing massive measurement redundancy.\nA Simpson's paradox (OR flip from 1.48 to 0.76) and Item-Focused Tree analysis (breakpoint at 2023-Q4) provide additional structural insights.\nWe discuss implications for benchmark maintenance and propose a DIF-based audit protocol.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLM benchmarks such as MMLU~\\citep{hendrycks2021measuring}, GSM8K~\\citep{cobbe2021gsm8k}, and HellaSwag~\\citep{zellers2019hellaswag} serve as the primary instruments for comparing model capabilities across generations.\nAn implicit assumption underlies every cross-generation comparison: items function equivalently regardless of when a model was trained.\nIf this assumption fails---if certain items become systematically easier or harder for newer models after controlling for overall ability---then cross-cohort score comparisons lose their psychometric grounding.\n\nDifferential Item Functioning (DIF) analysis~\\citep{holland1988differential} is the standard psychometric tool for detecting such comparability violations.\nAn item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly.\nThe Mantel--Haenszel (MH) procedure~\\citep{mantel1959statistical} provides a nonparametric test that conditions on total score, making it robust to overall ability differences between groups.\n\nWe apply MH-DIF to the METABENCH repository~\\citep{perlitz2024metabench}, analyzing 5,219 models $\\times$ 12,508 MMLU items---the largest DIF analysis on LLM benchmarks to date.\nOur central finding: \\textbf{30.8\\% of MMLU items show large temporal DIF} (ETS Category~C, $|\\Delta_\\text{MH}|{\\geq}1.5$).\nThis rate is $147\\times$ above the random-split control and confirmed at $p{<}0.001$ by permutation testing.\n\nA key framing principle: \\textbf{instability $\\neq$ invalidity}.\nDIF flags items whose functioning changed across model generations---a diagnostic signal, not a quality verdict.\nWe show that MMLU rankings are massively redundant ($\\rho{\\approx}0.994$ after removing all flagged items), so instability does not threaten ranking validity.\nInstead, DIF reveals \\emph{which} capability dimensions are shifting across generations.\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Temporal instability at scale}: 30.8\\% of MMLU items exhibit large DIF, generalizing across six benchmarks (17.5--30.8\\%), robust to threshold choice, multiple testing correction, and architecture composition.\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment${\\approx}$1.0 against existing labels is expected, not failure.\n\\item \\textbf{Semi-synthetic validation framework}: $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR${=}$0.000), portable across benchmarks.\n\\item \\textbf{DIF as diagnostic lens}: DIF items carry cross-cohort signal but are the least disruptive non-random removal strategy. We provide a concrete audit protocol for benchmark maintainers.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\nMin-K\\%~\\citep{shi2024detecting}, ConStat~\\citep{srivastava2024constat}, and n-gram overlap methods~\\citep{li2024task} detect memorization signals at the item or model level.\nThese approaches typically validate against web-overlap labels---a limitation we address empirically.\nDVD~\\citep{dong2024generalization} uses generation variance to detect memorization.\n\n\\paragraph{Benchmark evolution and maintenance.}\nLiveBench~\\citep{white2024livebench} and SEAL~\\citep{scale2024seal} propose dynamic benchmark designs.\nGrowing Pains~\\citep{perlitz2024growing} uses anchor items for efficient evaluation across benchmark versions.\nOur DIF analysis complements these approaches by identifying which items require replacement.\n\n\\paragraph{DIF in psychometrics.}\nThe Mantel--Haenszel procedure~\\citep{mantel1959statistical} with ETS classification~\\citep{zieky1993practical} is the gold standard for DIF detection in educational testing.\nItem-Focused Trees~\\citep{strobl2015rasch} extend DIF to continuous covariates.\nCumulative Bayesian DIF~\\citep{sinharay2006bayesian} enables longitudinal monitoring.\nWe bring these established tools to the LLM evaluation setting.\n\n\\paragraph{IRT for LLMs.}\nRecent work applies Item Response Theory to LLM evaluation~\\citep{polo2024tinybenchmarks,gu2024surveying}.\nOur bifactor pilot (Section~\\ref{sec:bifactor}) reveals fundamental challenges in fitting IRT models to multi-domain benchmarks like MMLU.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Mantel--Haenszel DIF}\n\nGiven a response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times I}$ where $N$ models respond to $I$ items, we partition models into reference (pre-2024) and focal (2024) groups.\nFor each item $i$, the MH procedure constructs $2 \\times 2$ tables at each total-score stratum $k$:\n\\begin{equation}\n\\alpha_\\text{MH}^{(i)} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k}\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are cell counts and $T_k$ is the stratum total.\nThe log-odds ratio $\\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH})$ is classified per ETS guidelines: Category~A ($|\\Delta_\\text{MH}|{<}1.0$), B ($1.0{\\leq}|\\Delta_\\text{MH}|{<}1.5$), or C ($|\\Delta_\\text{MH}|{\\geq}1.5$ and significant at $p{<}0.05$).\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo validate detection power without ground truth, we inject known differential contamination into real response matrices.\nFor a subset of items, we flip incorrect$\\to$correct responses for focal-group models with probability $p \\in [0, 1]$, simulating varying contamination levels.\nThe key metric is $\\Delta$TPR = TPR($p$) $-$ TPR($p{=}0$), measuring detection power gain.\n\n\\paragraph{Cross-subject matching.}\nFor multi-domain benchmarks, using total score on \\emph{other} subjects as the MH conditioning variable eliminates matching variable contamination ($\\Delta$FPR${=}$0.000), whereas within-subject matching suffers FPR inflation.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\nWe analyze the METABENCH MMLU response matrix (5,219 models: $N_\\text{ref}{=}1{,}080$ pre-2024, $N_\\text{foc}{=}807$ in 2024).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-way sensitivity matrix for MMLU DIF: temporal vs.\\ ability split, with and without negative-discrimination items. C\\% = proportion of ETS Category~C items.}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Split} & \\textbf{C\\%} & \\textbf{Enrichment} & \\textbf{FPR on clean} & \\textbf{Jaccard (T$\\cap$A)} \\\\\n\\midrule\nTemporal & 30.8 & 0.97 & 0.312 & \\multirow{2}{*}{0.016} \\\\\nAbility & 2.7 & 1.16 & --- & \\\\\n\\midrule\nRandom (sanity) & 0.21 & --- & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Neg-disc sensitivity}: $\\Delta$C\\% = $-1.2$\\,pp after BH-FDR removal of 4 items} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sensitivity} shows the primary result: 30.8\\% of items exhibit large temporal DIF (3,855 items at ETS~C).\nThe ability-split control (2.7\\%) confirms that DIF is not an artifact of overall ability differences; temporal--ability Jaccard overlap is only 0.016.\nThe random-split sanity check (0.21\\%) yields a ratio of $147\\times$.\nBH-FDR correction removes only 4 of 3,855 C-items ($-1.2$\\,pp).\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-family DIF analysis.}\n\\label{tab:within_family}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Family pair} & \\textbf{C\\%} & \\textbf{Jaccard w/ temporal} \\\\\n\\midrule\nLlama-2 vs.\\ Llama-3 & 58.7 & --- \\\\\nMistral vs.\\ Mixtral & 36.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithin-family analysis (Table~\\ref{tab:within_family}) reveals that family-level capability jumps (Llama-2$\\to$3: C\\%${=}$58.7\\%) are even more extreme than temporal DIF, supporting the diagnostic interpretation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain specificity: Spearman correlation between subject-level C\\% and accuracy improvement.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nSpearman $\\rho$ (domain C\\% vs.\\ $\\Delta$acc) & 0.29 & 0.028 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain-level accuracy improvement shows a modest correlation with C\\% ($\\rho{=}$0.29, $p{=}$0.028; Table~\\ref{tab:domain}), but item-level decomposition demonstrates that improvement explains ${\\leq}$2.4\\,pp of the 30.8\\% rate.\n\n\\subsection{Permutation Null Distribution}\n\\label{sec:permutation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Permutation null distribution for MMLU temporal DIF (1,000 permutations).}\n\\label{tab:permutation}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nNull mean C\\% & 0.45 \\\\\nNull SD & 0.16 \\\\\nNull max C\\% & 1.14 \\\\\nObserved C\\% & 30.8 \\\\\n$z$-score & 189.7 \\\\\nEmpirical $p$ & ${<}0.001$ (0/1000) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:permutation} reports the permutation test.\nRandomly reassigning temporal labels 1,000 times yields a null mean of 0.45\\% (SD${=}$0.16\\%, max${=}$1.14\\%), placing the observed 30.8\\% at $z{=}189.7$.\nThe temporal signal is unambiguously real.\n\n\\subsection{Architecture Stratification and IRT Diagnostics}\n\\label{sec:architecture}\n\n\\begin{table}[t]\n\\centering\n\\caption{Architecture composition and DIF invariance.}\n\\label{tab:arch_composition}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Full sample} & \\textbf{Decoder-only} \\\\\n\\midrule\n$N$ models & 5,227 & 5,222 (99.9\\%) \\\\\nNon-decoder removed & --- & 5 \\\\\nC\\% & 30.8 & 30.8 \\\\\nJaccard (full vs.\\ decoder) & \\multicolumn{2}{c}{1.000} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT model fit diagnostics: full sample vs.\\ decoder-only.}\n\\label{tab:irt_fit}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Sample} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} & \\textbf{SRMR} \\\\\n\\midrule\nFull & 0.041 & 0.68 & --- & --- \\\\\nDecoder-only & 0.041 & 0.68 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:arch_composition}--\\ref{tab:irt_fit} confirm that architecture heterogeneity is a non-issue (Jaccard${=}$1.0 between full and decoder-only DIF flags).\nIRT fit is poor (CFI${=}$0.68), reflecting MMLU's inherent 57-subject multidimensionality rather than architecture confounds.\nWe return to IRT misfit implications in Section~\\ref{sec:limitations}.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. All random controls ${<}$1\\%.}\n\\label{tab:six_bench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{$N$ items} & \\textbf{C\\%} & \\textbf{Random C\\%} & \\textbf{Enrichment} \\\\\n\\midrule\nMMLU & 12,508 & 30.8 & 0.20 & 154$\\times$ \\\\\nWinoGrande & 1,267 & 29.1 & 0.35 & 83$\\times$ \\\\\nTruthfulQA & 817 & 27.8 & 0.41 & 68$\\times$ \\\\\nARC & 1,172 & 24.5 & 0.55 & 45$\\times$ \\\\\nGSM8K & 1,319 & 18.3 & 0.28 & 65$\\times$ \\\\\nHellaSwag & 10,042 & 17.5 & 0.30 & 58$\\times$ \\\\\n\\midrule\n\\textbf{Range} & & \\multicolumn{2}{c}{\\textbf{17.5--30.8\\%}} & ${\\geq}$45$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Benchmark characteristics and temporal DIF rates.}\n\\label{tab:bench_chars}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Domain count} & \\textbf{Item format} & \\textbf{C\\%} \\\\\n\\midrule\nMMLU & 57 & 4-choice MC & 30.8 \\\\\nWinoGrande & Multi-scenario & Binary & 29.1 \\\\\nTruthfulQA & Multi-category & MC & 27.8 \\\\\nARC & Science & 4-choice MC & 24.5 \\\\\nGSM8K & Math & Open-ended & 18.3 \\\\\nHellaSwag & Commonsense & 4-choice MC & 17.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:six_bench} demonstrates that temporal DIF generalizes across all six benchmarks (C\\% range 17.5--30.8\\%, CV${=}$0.22).\nAll enrichment ratios exceed $45\\times$ above random.\nTable~\\ref{tab:bench_chars} provides descriptive moderator context: multi-domain benchmarks (MMLU, WinoGrande, TruthfulQA) tend toward higher C\\% than single-domain benchmarks (GSM8K, HellaSwag), though with $N{=}6$ benchmarks, formal moderator analysis is infeasible.\n\n\\subsection{GSM8K Replication and GSM1K Validation}\n\\label{sec:gsm8k}\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K temporal DIF (1,319 items $\\times$ 6,702 models).}\n\\label{tab:gsm8k_dif}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split type} & \\textbf{C\\%} & \\textbf{Random C\\%} & \\textbf{Spearman} \\\\\n\\midrule\nTemporal (standard) & 18.3 & 0.28 & \\multirow{2}{*}{0.92} \\\\\nTemporal (external) & 45.8 & --- & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM1K contamination gap correlation (exploratory, $N{=}33$).}\n\\label{tab:gsm1k}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Direction} \\\\\n\\midrule\nPearson & $-0.46$ & 0.007 & Negative \\\\\nSpearman $\\rho$ & $-0.39$ & 0.025 & Negative \\\\\nPartial $r$ & $-0.37$ & 0.035 & Negative \\\\\nLeave-one-out $r$ range & \\multicolumn{3}{c}{$[-0.52, -0.36]$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K replication (Table~\\ref{tab:gsm8k_dif}) confirms temporal DIF in a single-domain math benchmark (C\\%${=}$18.3\\%, consistent with the lower end of cross-benchmark range).\nStandard and external temporal splits correlate highly ($\\rho{=}$0.92).\n\nTable~\\ref{tab:gsm1k} reports an \\emph{exploratory} analysis: DIF flags anti-correlate with GSM1K contamination gap ($r{=}-0.46$, $p{=}0.007$, $N{=}33$).\nThe negative direction suggests DIF captures differential functioning distinct from contamination.\nGiven the small $N$ and wide confidence intervals, we treat this as suggestive evidence only.\n\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:semi_synthetic}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic $\\Delta$TPR/$\\Delta$FPR at varying contamination probability $p$ (500 clean + 150 injected items).}\n\\label{tab:semi_synth}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$p$ & \\textbf{TPR (ext.)} & \\textbf{$\\Delta$TPR} & \\textbf{FPR (ext.)} & \\textbf{$\\Delta$FPR} \\\\\n\\midrule\n0.0 & 0.314 & --- & 0.308 & --- \\\\\n0.3 & 0.510 & +0.20 & 0.308 & 0.000 \\\\\n0.5 & 0.740 & +0.43 & 0.308 & 0.000 \\\\\n0.7 & 0.950 & +0.64 & 0.308 & 0.000 \\\\\n1.0 & 1.000 & +0.69 & 0.308 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{FPR comparison: cross-subject (constant) vs.\\ within-subject (inflating) matching.}\n\\label{tab:fpr_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Matching type} & \\textbf{$\\Delta$FPR at $p{=}1.0$} & \\textbf{FPR inflation} \\\\\n\\midrule\nCross-subject & 0.000 & None \\\\\nWithin-subject (standard MH) & 0.310 & +31\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:semi_synth} validates the semi-synthetic framework.\nAt $p{=}0.5$, $\\Delta$TPR${=}$0.43---moderate detection power for half-contaminated items.\nCross-subject matching maintains $\\Delta$FPR${=}$0.000 across all contamination levels (Table~\\ref{tab:fpr_comparison}), while within-subject matching inflates FPR by 31\\%.\n\n\\subsection{Simpson's Paradox and Odds Ratio Analysis}\n\\label{sec:simpsons}\n\n\\begin{table}[t]\n\\centering\n\\caption{Four logistic regression models predicting DIF-C status. OR per 0.10 unit increase.}\n\\label{tab:logistic}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictor} & \\textbf{OR [95\\% CI]} & \\textbf{McF.\\ $R^2$} & \\textbf{Nag.\\ $R^2$} \\\\\n\\midrule\nM1 & Acc.\\ $\\Delta$ & 1.48 [1.14, 1.93] & 0.0008 & 0.0013 \\\\\n\\midrule\n\\multirow{3}{*}{M2} & Acc.\\ $\\Delta$ & 0.76 & \\multirow{3}{*}{0.040} & \\multirow{3}{*}{0.068} \\\\\n & Difficulty & 0.79 & & \\\\\n & Discrimination & 1.48 & & \\\\\n\\midrule\nM3 & Item $\\Delta$ & 1.07 & 0.0013 & --- \\\\\n\\midrule\n\\multirow{3}{*}{M4} & Item $\\Delta$ & 0.93 & \\multirow{3}{*}{0.042} & \\multirow{3}{*}{---} \\\\\n & Difficulty & 0.78 & & \\\\\n & Discrimination & 1.52 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's paradox: OR sign flip from M1 to M2 (LR test: $\\chi^2{=}634$, $p{<}0.001$).}\n\\label{tab:simpsons}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{M1 (unadjusted)} & \\textbf{M2 (adjusted)} \\\\\n\\midrule\nAcc.\\ $\\Delta$ OR & 1.48 & 0.76 \\\\\nFlip magnitude & \\multicolumn{2}{c}{$|1.48 - 0.76| = 0.72$} \\\\\nBest model $R^2$ & \\multicolumn{2}{c}{0.042 ($\\sim$96\\% unexplained)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:logistic} reveals a Simpson's paradox: accuracy improvement \\emph{positively} predicts DIF in the unadjusted model (M1: OR${=}$1.48) but \\emph{negatively} after conditioning on CTT item properties (M2: OR${=}$0.76).\nThe sign flip (Table~\\ref{tab:simpsons}) is driven by item difficulty and discrimination acting as confounders ($\\chi^2{=}634$, $p{<}0.001$).\nCTT discrimination is the strongest predictor (OR${=}$1.48--1.52 across models).\nHowever, the best model explains only 4.2\\% of variance---DIF is fundamentally item-specific and not reducible to simple predictors.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\n\\begin{table}[t]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF: agreement and unique contributions.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nIFT--MH Spearman $\\rho$ & 0.78 \\\\\nIFT--MH Jaccard (matched flags) & 0.71 \\\\\nDetected breakpoint & 2023-Q4 to 2024-Q1 \\\\\nNonlinear pattern & Yes \\\\\nAdditional items flagged by IFT & 127 \\\\\nComputational cost ratio (IFT/MH) & 8.3$\\times$ \\\\\nModels with precise release date & 37\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees (Table~\\ref{tab:ift}) use continuous release date as a covariate, partially addressing the temporal coarseness concern.\nIFT and MH show high agreement ($\\rho{=}0.78$, Jaccard${=}$0.71), confirming that the binary split captures the primary signal.\nThe detected breakpoint (2023-Q4 to 2024-Q1) identifies when DIF effects concentrate most.\nIFT flags 127 additional items at the breakpoint boundary that MH's binary threshold misses.\nCoverage is limited (37\\% of models have precise dates) and computational cost is $8.3\\times$ higher.\n\n\\subsection{Ranking Stability Under Item Removal}\n\\label{sec:graceful}\n\n\\begin{table}[t]\n\\centering\n\\caption{Ranking stability and reliability under progressive DIF-item replacement.}\n\\label{tab:graceful}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{$\\rho$ (ranking)} & \\textbf{SHR (reliability)} & \\textbf{Construct gaps} \\\\\n\\midrule\n5\\% & 0.9991 & 0.9928 & None \\\\\n10\\% & 0.9982 & 0.9921 & None \\\\\n20\\% & 0.9958 & 0.9896 & Onset \\\\\n31\\% & 0.9941 & 0.9862 & 2--3 domains \\\\\n50\\% & 0.9847 & 0.9735 & Significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:graceful} quantifies the ``instability $\\neq$ invalidity'' principle.\nAt the observed 31\\% DIF rate, ranking correlation remains $\\rho{=}0.9941$ and split-half reliability is 0.9862---minimal degradation.\nConstruct coverage gaps begin at 20\\% replacement (2--3 domains underrepresented at 31\\%).\nMMLU's massive item pool provides extreme redundancy: even removing half the items preserves $\\rho{>}0.98$.\n\n\\subsection{Detection Baselines: ConStat and DVD}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{ConStat perturbation detection rates by model type (218 reformulated items).}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model type} & \\textbf{Detection rate} & \\textbf{Effect size $d$} & \\textbf{FDR-controlled FPR} \\\\\n\\midrule\nNon-RL & 0.19 & 0.74 & 0.038 \\\\\nRL & 0.07 & 0.31 & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Jaccard with DIF flags} & 0.14 \\\\\n\\multicolumn{3}{l}{Paraphrase quality (human eval)} & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{DVD generation variance detection (12 models $\\times$ 50 responses/item).}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contamination type} & \\textbf{Detection rate} & \\textbf{SNR (large)} & \\textbf{SNR (small)} \\\\\n\\midrule\nVerbatim & 0.24 & 2.1 & 0.8 \\\\\nVariant & 0.09 & --- & --- \\\\\nNone (bimodal) & 0.13 & --- & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Correlation with DIF flags} & 0.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:constat}--\\ref{tab:dvd} compare DIF with perturbation-based (ConStat) and generation-variance (DVD) detectors.\nConStat detects 19\\% of reformulated items for non-RL models but only 7\\% for RL models, consistent with theoretical predictions about NLL gap contraction.\nDVD shows low correlation with DIF flags (0.17), confirming these methods capture orthogonal signals: DIF measures group-level differential functioning while ConStat and DVD target individual-level memorization.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-signal and ensemble AUROC comparison.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\nDIF only & 0.70 & --- & --- \\\\\nConStat only & 0.64 & --- & --- \\\\\nDVD only & 0.57 & --- & --- \\\\\n\\midrule\nEnsemble (optimized) & 0.73 & 0.79 & 0.52 \\\\\nEnsemble (uniform) & 0.72 & --- & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{$\\Delta$AUROC (ensemble $-$ DIF)} & +0.03 \\\\\n\\multicolumn{3}{l}{Fusion weight CV stability} & $\\pm$28\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion (Table~\\ref{tab:ensemble}) yields only +0.03 AUROC over DIF alone, with unstable fusion weights ($\\pm$28\\% across folds) and low majority-voting recall (0.52).\nThis informative negative result confirms that the three detectors capture different signal dimensions---forced fusion provides marginal benefit at substantial complexity cost, supporting DIF's standalone value as a group-level diagnostic.\n\n\\subsection{RL Robustness}\n\\label{sec:rl}\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF flag retention across training paradigms.}\n\\label{tab:rl_retention}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Cohort} & \\textbf{C\\%} & \\textbf{Jaccard vs.\\ SFT} \\\\\n\\midrule\nSFT baseline & 30.8 & --- \\\\\nAlignment-RL ($N{=}477$) & 29.4 & 0.83 \\\\\n+Reasoning-RL ($N{=}13$) & 30.2 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-detector AUROC by model type with 95\\% bootstrap CIs.}\n\\label{tab:rl_auroc}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Detector} & \\textbf{Non-RL} & \\textbf{Reasoning-RL} \\\\\n\\midrule\nDIF & 0.71 [0.67, 0.78] & 0.59 \\\\\nConStat & 0.68 [0.42, 0.73] & 0.53 \\\\\nMin-K\\% & --- & --- \\\\\n\\midrule\nDeLong $p$ (DIF vs.\\ ConStat) & \\multicolumn{2}{c}{0.082} \\\\\nTOST equivalence & \\multicolumn{2}{c}{$p{=}0.14$ (inconclusive)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF is robust to alignment-RL (Table~\\ref{tab:rl_retention}: C\\%${=}$29.4\\%, Jaccard${=}$0.83 with SFT).\nReasoning-RL results ($N{=}13$) are \\textbf{underpowered}: TOST equivalence is inconclusive ($p{=}0.14$) and bootstrap CIs for ConStat span chance level [0.42, 0.73].\nWe report these transparently but do not claim RL robustness beyond alignment-RL.\nPartial exploitation TPR at $p{=}0.5$ (0.41) is consistent with the semi-synthetic dose--response curve.\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{sec:bifactor}\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT model fit: unidimensional vs.\\ 5-factor bifactor.}\n\\label{tab:bifactor}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} & \\textbf{SRMR} \\\\\n\\midrule\nUnidimensional & 0.041 & 0.68 & --- & --- \\\\\nBifactor (5-factor) & 0.034 & 0.73 & 0.70 & 0.062 \\\\\n\\midrule\n\\multicolumn{5}{l}{Full 57-factor: did not converge} \\\\\n\\multicolumn{5}{l}{General factor variance: 41\\%} \\\\\n\\multicolumn{5}{l}{Specific factor range: [0.03, 0.18]} \\\\\n\\multicolumn{5}{l}{Anchor items selected: 0 --- \\textbf{pipeline killed}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bifactor} reports the bifactor IRT equating pilot.\nA full 57-factor model did not converge; reducing to 5 factors (STEM/humanities/social/professional/other) yields improved but still poor fit (CFI${=}$0.73, below the 0.90 standard).\nThe general factor explains only 41\\% of variance, confirming MMLU's essential multidimensionality.\nAnchor item selection failed under poor fit---the equating pipeline was terminated.\nThis negative result motivates the IRT misfit discussion in Section~\\ref{sec:limitations} and the need for future multidimensional IRT work.\n\n\\subsection{Item Generation Calibration}\n\\label{sec:item_gen}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-subject generation quality (150 items across 5 subjects).}\n\\label{tab:item_gen}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nDifficulty $\\rho$ (student sim.) & 0.56 \\\\\nDifficulty $\\rho$ (real models) & 0.41 \\\\\nExpert pass rate & 0.58 \\\\\nSubjects with construct drift & 2/5 \\\\\nAdequate subjects & 3/5 \\\\\nCalibration status & Insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLLM-generated replacement items (Table~\\ref{tab:item_gen}) show insufficient calibration for automatic equating: difficulty correlation with real models is only $\\rho{=}0.41$, expert pass rate is 58\\%, and 2 of 5 subjects exhibit construct drift.\nThis negative result supports the audit protocol's emphasis on human-in-the-loop item review rather than automatic replacement.\n\n\\subsection{Cumulative Bayesian DIF Simulation}\n\\label{sec:bayesian}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cumulative power by number of administrations ($\\delta{=}1.0$, $N{=}80$ per group).}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Administrations} & 1 & 2 & 3 & 4 \\\\\n\\midrule\nPower & 0.39 & 0.53 & 0.67 & 0.73 \\\\\nFPR (all stages) & \\multicolumn{4}{c}{0.044} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bayesian} shows that cumulative Bayesian evidence accumulation improves detection power from 0.39 (single administration) to 0.73 (four administrations) for medium effects ($\\delta{=}1.0$) while maintaining FPR at 0.044.\nThis simulation supports the audit protocol's recommendation for regular longitudinal monitoring.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{DIF as diagnostic, not filter.}\nThe 30.8\\% temporal instability rate might seem alarming, but the graceful degradation analysis ($\\rho{=}0.994$ at 31\\% removal) demonstrates that MMLU's massive item pool absorbs item-level instability without threatening ranking validity.\nDIF's value lies in identifying \\emph{which} items changed and \\emph{how}---a diagnostic lens for understanding benchmark evolution.\n\n\\paragraph{Cross-benchmark variation.}\nThe 17.5--30.8\\% range across six benchmarks demands explanation.\nDescriptively, multi-domain benchmarks (MMLU: 30.8\\%, WinoGrande: 29.1\\%) show higher C\\% than single-domain benchmarks (GSM8K: 18.3\\%, HellaSwag: 17.5\\%).\nDomain heterogeneity may introduce more construct-irrelevant variance sources.\nWith only $N{=}6$ benchmarks, formal moderator testing is infeasible; future work with additional benchmarks is needed.\n\n\\paragraph{Simpson's paradox implications.}\nThe OR flip (1.48$\\to$0.76) reveals that na\\\"ive association between accuracy improvement and DIF is confounded by item difficulty and discrimination.\nHowever, CTT properties explain only 4.2\\% of DIF variance---the phenomenon is fundamentally item-specific.\n\n\\paragraph{Audit protocol recommendation.}\nBased on our findings, we recommend a DIF-based audit protocol for benchmark maintainers: (1) run MH-DIF analysis at each major model generation release, (2) flag ETS Category~C items for review, (3) investigate flagged items for construct drift vs.\\ legitimate capability change, (4) maintain cumulative evidence across administrations.\nThis is a practical recommendation, not a formal contribution.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Temporal coarseness.}\nOur primary analysis uses a binary 2023/2024 split.\nItem-Focused Trees (Section~\\ref{sec:ift}) partially address this by identifying a 2023-Q4 breakpoint, but quarterly MH sensitivity analysis would strengthen the finding.\nWithin-year variation may be masked by the binary partition.\n\n\\textbf{IRT misfit.}\n98\\% of models show $|L_z|{>}2$, and CFI${=}$0.68 confirms poor unidimensional fit.\nThe MH procedure is nonparametric and does not directly depend on IRT model fit; however, the conditioning variable (cross-subject total score) may have reduced validity in a multidimensional context.\nA multidimensional IRT robustness check (e.g., within-subject MIRT on high-C\\% subjects) would address this concern but is beyond the scope of the current analysis.\n\n\\textbf{Reasoning-RL.}\nResults for reasoning-RL models ($N{=}$13) are underpowered.\nDIF robustness is confirmed only for alignment-RL; reasoning-RL remains unvalidated.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nApplying MH-DIF to 5,219 models $\\times$ 12,508 MMLU items, we find that 30.8\\% of items exhibit systematic cohort-conditional differences in item functioning between pre-2024 and 2024 model generations.\nThis instability generalizes across six benchmarks (17.5--30.8\\%, all ${\\geq}$45$\\times$ above random), is not driven by capability improvement (${\\leq}$2.4\\,pp), and does not threaten ranking validity ($\\rho{=}0.994$).\nThe field's web-overlap ground truth cannot capture this differential signal; our semi-synthetic framework with cross-subject matching ($\\Delta$FPR${=}$0.000) provides a reusable validation infrastructure.\nDIF analysis offers benchmark maintainers a principled tool for understanding how item functioning evolves across model generations.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}, 2021.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nY.~Dong, Y.~Jiang, H.~Deng, and L.~Qiu.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}, 2024.\n\n\\bibitem[Gu et~al.(2024)]{gu2024surveying}\nZ.~Gu, E.~Fan, and W.-L.~Chiang.\n\\newblock A survey on evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.03109}, 2024.\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021measuring}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I.~Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, Y.~Zhang, and Y.~Zhao.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Perlitz et~al.(2024a)]{perlitz2024metabench}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock {METABENCH}: A large-scale collection of model evaluation results.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Perlitz et~al.(2024b)]{perlitz2024growing}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Growing pains: Efficiently evaluating evolving benchmarks.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {tinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Scale(2024)]{scale2024seal}\nScale.\n\\newblock {SEAL} leaderboards.\n\\newblock \\url{https://scale.com/leaderboard}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nS.~Sinharay, M.~J. Haberman, and E.~T. Dorans.\n\\newblock A {B}ayesian approach to the detection of {DIF} across multiple administrations.\n\\newblock \\emph{Psychometrika}, 71(2):217--237, 2006.\n\n\\bibitem[Srivastava et~al.(2024)]{srivastava2024constat}\nM.~Srivastava, Y.~Chen, and Y.~Choi.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Strobl et~al.(2015)]{strobl2015rasch}\nC.~Strobl, J.~Kopf, and A.~Zeileis.\n\\newblock {R}asch trees: A new method for detecting differential item functioning in the {R}asch model.\n\\newblock \\emph{Psychometrika}, 80(2):289--316, 2015.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naber, et~al.\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Zellers et~al.(2019)]{zellers2019hellaswag}\nR.~Zellers, A.~Holtzman, Y.~Bisk, A.~Farcas, and Y.~Choi.\n\\newblock {HellaSwag}: Can a machine really finish your sentence?\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Zieky(1993)]{zieky1993practical}\nM.~Zieky.\n\\newblock Practical questions in the use of {DIF} statistics in test development.\n\\newblock In P.~W. Holland and H.~Wainer, editors, \\emph{Differential Item Functioning}, pages 337--347. Lawrence Erlbaum, 1993.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aca7015-77f7-4c5c-8dc6-71291c5df78e",
  "isSidechain": false,
  "requestId": "req_011CbFeGeRJ1R8gYg81aQ6GE",
  "type": "assistant",
  "uuid": "d53dec86-fb74-41d1-804f-c9eaa2e4f3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5FuoyyowUYwouuHNn6iUE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 42182,
      "output_tokens": 13525,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13525,
          "cache_read_input_tokens": 42182,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 976
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

_source line 19 · 2026-05-21T11:38:32.322Z_

<details><summary>↩ Tool result · `toolu_01ArEQ7CRvPm3KTpk1AivmU3`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d53dec86-fb74-41d1-804f-c9eaa2e4f3c3",
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "e3d87464-31d4-429b-ae6f-e13dec2b2390",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{caption}\n\n\\title{Psychometric DIF Analysis Reveals Systematic Temporal Instability\\\\in LLM Benchmark Items at Scale}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nWhen we compare language model scores across generations, we implicitly assume that benchmark items function equivalently for all model cohorts.\nWe test this assumption using Mantel--Haenszel Differential Item Functioning (MH-DIF) analysis on the METABENCH response matrix (5,219 models $\\times$ 12,508 MMLU items).\nWe find that 30.8\\% of MMLU items exhibit large DIF (ETS Category~C) between pre-2024 and 2024 model cohorts---a rate ${\\geq}147\\times$ the random-split baseline (0.21\\%) and confirmed by 1,000-fold permutation testing ($z{=}189.7$, $p{<}0.001$).\nThis instability generalizes across six benchmarks (C\\% range 17.5--30.8\\%, all ${\\geq}45\\times$ above random) and is not driven by capability improvement (${\\leq}$2.4\\,pp explained) or architecture heterogeneity (99.9\\% decoder-only, Jaccard${=}$1.0).\nWe show that the field's standard web-overlap ground truth cannot capture differential item functioning and propose a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR${=}$0.000).\nDespite 30.8\\% instability, benchmark rankings remain highly stable ($\\rho{=}$0.994 after removing all flagged items), revealing massive measurement redundancy.\nA Simpson's paradox (OR flip from 1.48 to 0.76) and Item-Focused Tree analysis (breakpoint at 2023-Q4) provide additional structural insights.\nWe discuss implications for benchmark maintenance and propose a DIF-based audit protocol.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLLM benchmarks such as MMLU~\\citep{hendrycks2021measuring}, GSM8K~\\citep{cobbe2021gsm8k}, and HellaSwag~\\citep{zellers2019hellaswag} serve as the primary instruments for comparing model capabilities across generations.\nAn implicit assumption underlies every cross-generation comparison: items function equivalently regardless of when a model was trained.\nIf this assumption fails---if certain items become systematically easier or harder for newer models after controlling for overall ability---then cross-cohort score comparisons lose their psychometric grounding.\n\nDifferential Item Functioning (DIF) analysis~\\citep{holland1988differential} is the standard psychometric tool for detecting such comparability violations.\nAn item exhibits DIF when examinees of equal ability from different groups have different probabilities of answering correctly.\nThe Mantel--Haenszel (MH) procedure~\\citep{mantel1959statistical} provides a nonparametric test that conditions on total score, making it robust to overall ability differences between groups.\n\nWe apply MH-DIF to the METABENCH repository~\\citep{perlitz2024metabench}, analyzing 5,219 models $\\times$ 12,508 MMLU items---the largest DIF analysis on LLM benchmarks to date.\nOur central finding: \\textbf{30.8\\% of MMLU items show large temporal DIF} (ETS Category~C, $|\\Delta_\\text{MH}|{\\geq}1.5$).\nThis rate is $147\\times$ above the random-split control and confirmed at $p{<}0.001$ by permutation testing.\n\nA key framing principle: \\textbf{instability $\\neq$ invalidity}.\nDIF flags items whose functioning changed across model generations---a diagnostic signal, not a quality verdict.\nWe show that MMLU rankings are massively redundant ($\\rho{\\approx}0.994$ after removing all flagged items), so instability does not threaten ranking validity.\nInstead, DIF reveals \\emph{which} capability dimensions are shifting across generations.\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Temporal instability at scale}: 30.8\\% of MMLU items exhibit large DIF, generalizing across six benchmarks (17.5--30.8\\%), robust to threshold choice, multiple testing correction, and architecture composition.\n\\item \\textbf{Ground truth meta-critique}: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment${\\approx}$1.0 against existing labels is expected, not failure.\n\\item \\textbf{Semi-synthetic validation framework}: $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR${=}$0.000), portable across benchmarks.\n\\item \\textbf{DIF as diagnostic lens}: DIF items carry cross-cohort signal but are the least disruptive non-random removal strategy. We provide a concrete audit protocol for benchmark maintainers.\n\\end{enumerate}\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Benchmark contamination detection.}\nMin-K\\%~\\citep{shi2024detecting}, ConStat~\\citep{srivastava2024constat}, and n-gram overlap methods~\\citep{li2024task} detect memorization signals at the item or model level.\nThese approaches typically validate against web-overlap labels---a limitation we address empirically.\nDVD~\\citep{dong2024generalization} uses generation variance to detect memorization.\n\n\\paragraph{Benchmark evolution and maintenance.}\nLiveBench~\\citep{white2024livebench} and SEAL~\\citep{scale2024seal} propose dynamic benchmark designs.\nGrowing Pains~\\citep{perlitz2024growing} uses anchor items for efficient evaluation across benchmark versions.\nOur DIF analysis complements these approaches by identifying which items require replacement.\n\n\\paragraph{DIF in psychometrics.}\nThe Mantel--Haenszel procedure~\\citep{mantel1959statistical} with ETS classification~\\citep{zieky1993practical} is the gold standard for DIF detection in educational testing.\nItem-Focused Trees~\\citep{strobl2015rasch} extend DIF to continuous covariates.\nCumulative Bayesian DIF~\\citep{sinharay2006bayesian} enables longitudinal monitoring.\nWe bring these established tools to the LLM evaluation setting.\n\n\\paragraph{IRT for LLMs.}\nRecent work applies Item Response Theory to LLM evaluation~\\citep{polo2024tinybenchmarks,gu2024surveying}.\nOur bifactor pilot (Section~\\ref{sec:bifactor}) reveals fundamental challenges in fitting IRT models to multi-domain benchmarks like MMLU.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Mantel--Haenszel DIF}\n\nGiven a response matrix $\\mathbf{X} \\in \\{0,1\\}^{N \\times I}$ where $N$ models respond to $I$ items, we partition models into reference (pre-2024) and focal (2024) groups.\nFor each item $i$, the MH procedure constructs $2 \\times 2$ tables at each total-score stratum $k$:\n\\begin{equation}\n\\alpha_\\text{MH}^{(i)} = \\frac{\\sum_k A_k D_k / T_k}{\\sum_k B_k C_k / T_k}\n\\end{equation}\nwhere $A_k, B_k, C_k, D_k$ are cell counts and $T_k$ is the stratum total.\nThe log-odds ratio $\\Delta_\\text{MH} = -2.35 \\ln(\\alpha_\\text{MH})$ is classified per ETS guidelines: Category~A ($|\\Delta_\\text{MH}|{<}1.0$), B ($1.0{\\leq}|\\Delta_\\text{MH}|{<}1.5$), or C ($|\\Delta_\\text{MH}|{\\geq}1.5$ and significant at $p{<}0.05$).\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo validate detection power without ground truth, we inject known differential contamination into real response matrices.\nFor a subset of items, we flip incorrect$\\to$correct responses for focal-group models with probability $p \\in [0, 1]$, simulating varying contamination levels.\nThe key metric is $\\Delta$TPR = TPR($p$) $-$ TPR($p{=}0$), measuring detection power gain.\n\n\\paragraph{Cross-subject matching.}\nFor multi-domain benchmarks, using total score on \\emph{other} subjects as the MH conditioning variable eliminates matching variable contamination ($\\Delta$FPR${=}$0.000), whereas within-subject matching suffers FPR inflation.\n\n% ============================================================\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Temporal DIF on MMLU}\n\\label{sec:temporal_dif}\n\nWe analyze the METABENCH MMLU response matrix (5,219 models: $N_\\text{ref}{=}1{,}080$ pre-2024, $N_\\text{foc}{=}807$ in 2024).\n\n\\begin{table}[t]\n\\centering\n\\caption{Four-way sensitivity matrix for MMLU DIF: temporal vs.\\ ability split, with and without negative-discrimination items. C\\% = proportion of ETS Category~C items.}\n\\label{tab:sensitivity}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Split} & \\textbf{C\\%} & \\textbf{Enrichment} & \\textbf{FPR on clean} & \\textbf{Jaccard (T$\\cap$A)} \\\\\n\\midrule\nTemporal & 30.8 & 0.97 & 0.312 & \\multirow{2}{*}{0.016} \\\\\nAbility & 2.7 & 1.16 & --- & \\\\\n\\midrule\nRandom (sanity) & 0.21 & --- & --- & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Neg-disc sensitivity}: $\\Delta$C\\% = $-1.2$\\,pp after BH-FDR removal of 4 items} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:sensitivity} shows the primary result: 30.8\\% of items exhibit large temporal DIF (3,855 items at ETS~C).\nThe ability-split control (2.7\\%) confirms that DIF is not an artifact of overall ability differences; temporal--ability Jaccard overlap is only 0.016.\nThe random-split sanity check (0.21\\%) yields a ratio of $147\\times$.\nBH-FDR correction removes only 4 of 3,855 C-items ($-1.2$\\,pp).\n\n\\begin{table}[t]\n\\centering\n\\caption{Within-family DIF analysis.}\n\\label{tab:within_family}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Family pair} & \\textbf{C\\%} & \\textbf{Jaccard w/ temporal} \\\\\n\\midrule\nLlama-2 vs.\\ Llama-3 & 58.7 & --- \\\\\nMistral vs.\\ Mixtral & 36.2 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWithin-family analysis (Table~\\ref{tab:within_family}) reveals that family-level capability jumps (Llama-2$\\to$3: C\\%${=}$58.7\\%) are even more extreme than temporal DIF, supporting the diagnostic interpretation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Domain specificity: Spearman correlation between subject-level C\\% and accuracy improvement.}\n\\label{tab:domain}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{$p$} \\\\\n\\midrule\nSpearman $\\rho$ (domain C\\% vs.\\ $\\Delta$acc) & 0.29 & 0.028 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDomain-level accuracy improvement shows a modest correlation with C\\% ($\\rho{=}$0.29, $p{=}$0.028; Table~\\ref{tab:domain}), but item-level decomposition demonstrates that improvement explains ${\\leq}$2.4\\,pp of the 30.8\\% rate.\n\n\\subsection{Permutation Null Distribution}\n\\label{sec:permutation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Permutation null distribution for MMLU temporal DIF (1,000 permutations).}\n\\label{tab:permutation}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Statistic} & \\textbf{Value} \\\\\n\\midrule\nNull mean C\\% & 0.45 \\\\\nNull SD & 0.16 \\\\\nNull max C\\% & 1.14 \\\\\nObserved C\\% & 30.8 \\\\\n$z$-score & 189.7 \\\\\nEmpirical $p$ & ${<}0.001$ (0/1000) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:permutation} reports the permutation test.\nRandomly reassigning temporal labels 1,000 times yields a null mean of 0.45\\% (SD${=}$0.16\\%, max${=}$1.14\\%), placing the observed 30.8\\% at $z{=}189.7$.\nThe temporal signal is unambiguously real.\n\n\\subsection{Architecture Stratification and IRT Diagnostics}\n\\label{sec:architecture}\n\n\\begin{table}[t]\n\\centering\n\\caption{Architecture composition and DIF invariance.}\n\\label{tab:arch_composition}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{Full sample} & \\textbf{Decoder-only} \\\\\n\\midrule\n$N$ models & 5,227 & 5,222 (99.9\\%) \\\\\nNon-decoder removed & --- & 5 \\\\\nC\\% & 30.8 & 30.8 \\\\\nJaccard (full vs.\\ decoder) & \\multicolumn{2}{c}{1.000} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT model fit diagnostics: full sample vs.\\ decoder-only.}\n\\label{tab:irt_fit}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Sample} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} & \\textbf{SRMR} \\\\\n\\midrule\nFull & 0.041 & 0.68 & --- & --- \\\\\nDecoder-only & 0.041 & 0.68 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:arch_composition}--\\ref{tab:irt_fit} confirm that architecture heterogeneity is a non-issue (Jaccard${=}$1.0 between full and decoder-only DIF flags).\nIRT fit is poor (CFI${=}$0.68), reflecting MMLU's inherent 57-subject multidimensionality rather than architecture confounds.\nWe return to IRT misfit implications in Section~\\ref{sec:limitations}.\n\n\\subsection{Cross-Benchmark Generalization}\n\\label{sec:cross_bench}\n\n\\begin{table}[t]\n\\centering\n\\caption{Temporal DIF across six benchmarks. All random controls ${<}$1\\%.}\n\\label{tab:six_bench}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{$N$ items} & \\textbf{C\\%} & \\textbf{Random C\\%} & \\textbf{Enrichment} \\\\\n\\midrule\nMMLU & 12,508 & 30.8 & 0.20 & 154$\\times$ \\\\\nWinoGrande & 1,267 & 29.1 & 0.35 & 83$\\times$ \\\\\nTruthfulQA & 817 & 27.8 & 0.41 & 68$\\times$ \\\\\nARC & 1,172 & 24.5 & 0.55 & 45$\\times$ \\\\\nGSM8K & 1,319 & 18.3 & 0.28 & 65$\\times$ \\\\\nHellaSwag & 10,042 & 17.5 & 0.30 & 58$\\times$ \\\\\n\\midrule\n\\textbf{Range} & & \\multicolumn{2}{c}{\\textbf{17.5--30.8\\%}} & ${\\geq}$45$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Benchmark characteristics and temporal DIF rates.}\n\\label{tab:bench_chars}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Benchmark} & \\textbf{Domain count} & \\textbf{Item format} & \\textbf{C\\%} \\\\\n\\midrule\nMMLU & 57 & 4-choice MC & 30.8 \\\\\nWinoGrande & Multi-scenario & Binary & 29.1 \\\\\nTruthfulQA & Multi-category & MC & 27.8 \\\\\nARC & Science & 4-choice MC & 24.5 \\\\\nGSM8K & Math & Open-ended & 18.3 \\\\\nHellaSwag & Commonsense & 4-choice MC & 17.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:six_bench} demonstrates that temporal DIF generalizes across all six benchmarks (C\\% range 17.5--30.8\\%, CV${=}$0.22).\nAll enrichment ratios exceed $45\\times$ above random.\nTable~\\ref{tab:bench_chars} provides descriptive moderator context: multi-domain benchmarks (MMLU, WinoGrande, TruthfulQA) tend toward higher C\\% than single-domain benchmarks (GSM8K, HellaSwag), though with $N{=}6$ benchmarks, formal moderator analysis is infeasible.\n\n\\subsection{GSM8K Replication and GSM1K Validation}\n\\label{sec:gsm8k}\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM8K temporal DIF (1,319 items $\\times$ 6,702 models).}\n\\label{tab:gsm8k_dif}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Split type} & \\textbf{C\\%} & \\textbf{Random C\\%} & \\textbf{Spearman} \\\\\n\\midrule\nTemporal (standard) & 18.3 & 0.28 & \\multirow{2}{*}{0.92} \\\\\nTemporal (external) & 45.8 & --- & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{GSM1K contamination gap correlation (exploratory, $N{=}33$).}\n\\label{tab:gsm1k}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{Direction} \\\\\n\\midrule\nPearson & $-0.46$ & 0.007 & Negative \\\\\nSpearman $\\rho$ & $-0.39$ & 0.025 & Negative \\\\\nPartial $r$ & $-0.37$ & 0.035 & Negative \\\\\nLeave-one-out $r$ range & \\multicolumn{3}{c}{$[-0.52, -0.36]$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K replication (Table~\\ref{tab:gsm8k_dif}) confirms temporal DIF in a single-domain math benchmark (C\\%${=}$18.3\\%, consistent with the lower end of cross-benchmark range).\nStandard and external temporal splits correlate highly ($\\rho{=}$0.92).\n\nTable~\\ref{tab:gsm1k} reports an \\emph{exploratory} analysis: DIF flags anti-correlate with GSM1K contamination gap ($r{=}-0.46$, $p{=}0.007$, $N{=}33$).\nThe negative direction suggests DIF captures differential functioning distinct from contamination.\nGiven the small $N$ and wide confidence intervals, we treat this as suggestive evidence only.\n\n\\subsection{Semi-Synthetic Contamination Validation}\n\\label{sec:semi_synthetic}\n\n\\begin{table}[t]\n\\centering\n\\caption{Semi-synthetic $\\Delta$TPR/$\\Delta$FPR at varying contamination probability $p$ (500 clean + 150 injected items).}\n\\label{tab:semi_synth}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$p$ & \\textbf{TPR (ext.)} & \\textbf{$\\Delta$TPR} & \\textbf{FPR (ext.)} & \\textbf{$\\Delta$FPR} \\\\\n\\midrule\n0.0 & 0.314 & --- & 0.308 & --- \\\\\n0.3 & 0.510 & +0.20 & 0.308 & 0.000 \\\\\n0.5 & 0.740 & +0.43 & 0.308 & 0.000 \\\\\n0.7 & 0.950 & +0.64 & 0.308 & 0.000 \\\\\n1.0 & 1.000 & +0.69 & 0.308 & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{FPR comparison: cross-subject (constant) vs.\\ within-subject (inflating) matching.}\n\\label{tab:fpr_comparison}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Matching type} & \\textbf{$\\Delta$FPR at $p{=}1.0$} & \\textbf{FPR inflation} \\\\\n\\midrule\nCross-subject & 0.000 & None \\\\\nWithin-subject (standard MH) & 0.310 & +31\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:semi_synth} validates the semi-synthetic framework.\nAt $p{=}0.5$, $\\Delta$TPR${=}$0.43---moderate detection power for half-contaminated items.\nCross-subject matching maintains $\\Delta$FPR${=}$0.000 across all contamination levels (Table~\\ref{tab:fpr_comparison}), while within-subject matching inflates FPR by 31\\%.\n\n\\subsection{Simpson's Paradox and Odds Ratio Analysis}\n\\label{sec:simpsons}\n\n\\begin{table}[t]\n\\centering\n\\caption{Four logistic regression models predicting DIF-C status. OR per 0.10 unit increase.}\n\\label{tab:logistic}\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Model} & \\textbf{Predictor} & \\textbf{OR [95\\% CI]} & \\textbf{McF.\\ $R^2$} & \\textbf{Nag.\\ $R^2$} \\\\\n\\midrule\nM1 & Acc.\\ $\\Delta$ & 1.48 [1.14, 1.93] & 0.0008 & 0.0013 \\\\\n\\midrule\n\\multirow{3}{*}{M2} & Acc.\\ $\\Delta$ & 0.76 & \\multirow{3}{*}{0.040} & \\multirow{3}{*}{0.068} \\\\\n & Difficulty & 0.79 & & \\\\\n & Discrimination & 1.48 & & \\\\\n\\midrule\nM3 & Item $\\Delta$ & 1.07 & 0.0013 & --- \\\\\n\\midrule\n\\multirow{3}{*}{M4} & Item $\\Delta$ & 0.93 & \\multirow{3}{*}{0.042} & \\multirow{3}{*}{---} \\\\\n & Difficulty & 0.78 & & \\\\\n & Discrimination & 1.52 & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Simpson's paradox: OR sign flip from M1 to M2 (LR test: $\\chi^2{=}634$, $p{<}0.001$).}\n\\label{tab:simpsons}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n& \\textbf{M1 (unadjusted)} & \\textbf{M2 (adjusted)} \\\\\n\\midrule\nAcc.\\ $\\Delta$ OR & 1.48 & 0.76 \\\\\nFlip magnitude & \\multicolumn{2}{c}{$|1.48 - 0.76| = 0.72$} \\\\\nBest model $R^2$ & \\multicolumn{2}{c}{0.042 ($\\sim$96\\% unexplained)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:logistic} reveals a Simpson's paradox: accuracy improvement \\emph{positively} predicts DIF in the unadjusted model (M1: OR${=}$1.48) but \\emph{negatively} after conditioning on CTT item properties (M2: OR${=}$0.76).\nThe sign flip (Table~\\ref{tab:simpsons}) is driven by item difficulty and discrimination acting as confounders ($\\chi^2{=}634$, $p{<}0.001$).\nCTT discrimination is the strongest predictor (OR${=}$1.48--1.52 across models).\nHowever, the best model explains only 4.2\\% of variance---DIF is fundamentally item-specific and not reducible to simple predictors.\n\n\\subsection{Item-Focused Trees}\n\\label{sec:ift}\n\n\\begin{table}[t]\n\\centering\n\\caption{Item-Focused Trees vs.\\ MH-DIF: agreement and unique contributions.}\n\\label{tab:ift}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nIFT--MH Spearman $\\rho$ & 0.78 \\\\\nIFT--MH Jaccard (matched flags) & 0.71 \\\\\nDetected breakpoint & 2023-Q4 to 2024-Q1 \\\\\nNonlinear pattern & Yes \\\\\nAdditional items flagged by IFT & 127 \\\\\nComputational cost ratio (IFT/MH) & 8.3$\\times$ \\\\\nModels with precise release date & 37\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees (Table~\\ref{tab:ift}) use continuous release date as a covariate, partially addressing the temporal coarseness concern.\nIFT and MH show high agreement ($\\rho{=}0.78$, Jaccard${=}$0.71), confirming that the binary split captures the primary signal.\nThe detected breakpoint (2023-Q4 to 2024-Q1) identifies when DIF effects concentrate most.\nIFT flags 127 additional items at the breakpoint boundary that MH's binary threshold misses.\nCoverage is limited (37\\% of models have precise dates) and computational cost is $8.3\\times$ higher.\n\n\\subsection{Ranking Stability Under Item Removal}\n\\label{sec:graceful}\n\n\\begin{table}[t]\n\\centering\n\\caption{Ranking stability and reliability under progressive DIF-item replacement.}\n\\label{tab:graceful}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Replacement \\%} & \\textbf{$\\rho$ (ranking)} & \\textbf{SHR (reliability)} & \\textbf{Construct gaps} \\\\\n\\midrule\n5\\% & 0.9991 & 0.9928 & None \\\\\n10\\% & 0.9982 & 0.9921 & None \\\\\n20\\% & 0.9958 & 0.9896 & Onset \\\\\n31\\% & 0.9941 & 0.9862 & 2--3 domains \\\\\n50\\% & 0.9847 & 0.9735 & Significant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:graceful} quantifies the ``instability $\\neq$ invalidity'' principle.\nAt the observed 31\\% DIF rate, ranking correlation remains $\\rho{=}0.9941$ and split-half reliability is 0.9862---minimal degradation.\nConstruct coverage gaps begin at 20\\% replacement (2--3 domains underrepresented at 31\\%).\nMMLU's massive item pool provides extreme redundancy: even removing half the items preserves $\\rho{>}0.98$.\n\n\\subsection{Detection Baselines: ConStat and DVD}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\caption{ConStat perturbation detection rates by model type (218 reformulated items).}\n\\label{tab:constat}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model type} & \\textbf{Detection rate} & \\textbf{Effect size $d$} & \\textbf{FDR-controlled FPR} \\\\\n\\midrule\nNon-RL & 0.19 & 0.74 & 0.038 \\\\\nRL & 0.07 & 0.31 & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Jaccard with DIF flags} & 0.14 \\\\\n\\multicolumn{3}{l}{Paraphrase quality (human eval)} & 0.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{DVD generation variance detection (12 models $\\times$ 50 responses/item).}\n\\label{tab:dvd}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Contamination type} & \\textbf{Detection rate} & \\textbf{SNR (large)} & \\textbf{SNR (small)} \\\\\n\\midrule\nVerbatim & 0.24 & 2.1 & 0.8 \\\\\nVariant & 0.09 & --- & --- \\\\\nNone (bimodal) & 0.13 & --- & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Correlation with DIF flags} & 0.17 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTables~\\ref{tab:constat}--\\ref{tab:dvd} compare DIF with perturbation-based (ConStat) and generation-variance (DVD) detectors.\nConStat detects 19\\% of reformulated items for non-RL models but only 7\\% for RL models, consistent with theoretical predictions about NLL gap contraction.\nDVD shows low correlation with DIF flags (0.17), confirming these methods capture orthogonal signals: DIF measures group-level differential functioning while ConStat and DVD target individual-level memorization.\n\n\\subsection{Ensemble Fusion}\n\\label{sec:ensemble}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-signal and ensemble AUROC comparison.}\n\\label{tab:ensemble}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\nDIF only & 0.70 & --- & --- \\\\\nConStat only & 0.64 & --- & --- \\\\\nDVD only & 0.57 & --- & --- \\\\\n\\midrule\nEnsemble (optimized) & 0.73 & 0.79 & 0.52 \\\\\nEnsemble (uniform) & 0.72 & --- & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{$\\Delta$AUROC (ensemble $-$ DIF)} & +0.03 \\\\\n\\multicolumn{3}{l}{Fusion weight CV stability} & $\\pm$28\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble fusion (Table~\\ref{tab:ensemble}) yields only +0.03 AUROC over DIF alone, with unstable fusion weights ($\\pm$28\\% across folds) and low majority-voting recall (0.52).\nThis informative negative result confirms that the three detectors capture different signal dimensions---forced fusion provides marginal benefit at substantial complexity cost, supporting DIF's standalone value as a group-level diagnostic.\n\n\\subsection{RL Robustness}\n\\label{sec:rl}\n\n\\begin{table}[t]\n\\centering\n\\caption{DIF flag retention across training paradigms.}\n\\label{tab:rl_retention}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Cohort} & \\textbf{C\\%} & \\textbf{Jaccard vs.\\ SFT} \\\\\n\\midrule\nSFT baseline & 30.8 & --- \\\\\nAlignment-RL ($N{=}477$) & 29.4 & 0.83 \\\\\n+Reasoning-RL ($N{=}13$) & 30.2 & 0.91 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-detector AUROC by model type with 95\\% bootstrap CIs.}\n\\label{tab:rl_auroc}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Detector} & \\textbf{Non-RL} & \\textbf{Reasoning-RL} \\\\\n\\midrule\nDIF & 0.71 [0.67, 0.78] & 0.59 \\\\\nConStat & 0.68 [0.42, 0.73] & 0.53 \\\\\nMin-K\\% & --- & --- \\\\\n\\midrule\nDeLong $p$ (DIF vs.\\ ConStat) & \\multicolumn{2}{c}{0.082} \\\\\nTOST equivalence & \\multicolumn{2}{c}{$p{=}0.14$ (inconclusive)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDIF is robust to alignment-RL (Table~\\ref{tab:rl_retention}: C\\%${=}$29.4\\%, Jaccard${=}$0.83 with SFT).\nReasoning-RL results ($N{=}13$) are \\textbf{underpowered}: TOST equivalence is inconclusive ($p{=}0.14$) and bootstrap CIs for ConStat span chance level [0.42, 0.73].\nWe report these transparently but do not claim RL robustness beyond alignment-RL.\nPartial exploitation TPR at $p{=}0.5$ (0.41) is consistent with the semi-synthetic dose--response curve.\n\n\\subsection{Bifactor IRT Equating Pilot}\n\\label{sec:bifactor}\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT model fit: unidimensional vs.\\ 5-factor bifactor.}\n\\label{tab:bifactor}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{RMSEA} & \\textbf{CFI} & \\textbf{TLI} & \\textbf{SRMR} \\\\\n\\midrule\nUnidimensional & 0.041 & 0.68 & --- & --- \\\\\nBifactor (5-factor) & 0.034 & 0.73 & 0.70 & 0.062 \\\\\n\\midrule\n\\multicolumn{5}{l}{Full 57-factor: did not converge} \\\\\n\\multicolumn{5}{l}{General factor variance: 41\\%} \\\\\n\\multicolumn{5}{l}{Specific factor range: [0.03, 0.18]} \\\\\n\\multicolumn{5}{l}{Anchor items selected: 0 --- \\textbf{pipeline killed}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bifactor} reports the bifactor IRT equating pilot.\nA full 57-factor model did not converge; reducing to 5 factors (STEM/humanities/social/professional/other) yields improved but still poor fit (CFI${=}$0.73, below the 0.90 standard).\nThe general factor explains only 41\\% of variance, confirming MMLU's essential multidimensionality.\nAnchor item selection failed under poor fit---the equating pipeline was terminated.\nThis negative result motivates the IRT misfit discussion in Section~\\ref{sec:limitations} and the need for future multidimensional IRT work.\n\n\\subsection{Item Generation Calibration}\n\\label{sec:item_gen}\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-subject generation quality (150 items across 5 subjects).}\n\\label{tab:item_gen}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nDifficulty $\\rho$ (student sim.) & 0.56 \\\\\nDifficulty $\\rho$ (real models) & 0.41 \\\\\nExpert pass rate & 0.58 \\\\\nSubjects with construct drift & 2/5 \\\\\nAdequate subjects & 3/5 \\\\\nCalibration status & Insufficient \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLLM-generated replacement items (Table~\\ref{tab:item_gen}) show insufficient calibration for automatic equating: difficulty correlation with real models is only $\\rho{=}0.41$, expert pass rate is 58\\%, and 2 of 5 subjects exhibit construct drift.\nThis negative result supports the audit protocol's emphasis on human-in-the-loop item review rather than automatic replacement.\n\n\\subsection{Cumulative Bayesian DIF Simulation}\n\\label{sec:bayesian}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cumulative power by number of administrations ($\\delta{=}1.0$, $N{=}80$ per group).}\n\\label{tab:bayesian}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Administrations} & 1 & 2 & 3 & 4 \\\\\n\\midrule\nPower & 0.39 & 0.53 & 0.67 & 0.73 \\\\\nFPR (all stages) & \\multicolumn{4}{c}{0.044} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:bayesian} shows that cumulative Bayesian evidence accumulation improves detection power from 0.39 (single administration) to 0.73 (four administrations) for medium effects ($\\delta{=}1.0$) while maintaining FPR at 0.044.\nThis simulation supports the audit protocol's recommendation for regular longitudinal monitoring.\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{DIF as diagnostic, not filter.}\nThe 30.8\\% temporal instability rate might seem alarming, but the graceful degradation analysis ($\\rho{=}0.994$ at 31\\% removal) demonstrates that MMLU's massive item pool absorbs item-level instability without threatening ranking validity.\nDIF's value lies in identifying \\emph{which} items changed and \\emph{how}---a diagnostic lens for understanding benchmark evolution.\n\n\\paragraph{Cross-benchmark variation.}\nThe 17.5--30.8\\% range across six benchmarks demands explanation.\nDescriptively, multi-domain benchmarks (MMLU: 30.8\\%, WinoGrande: 29.1\\%) show higher C\\% than single-domain benchmarks (GSM8K: 18.3\\%, HellaSwag: 17.5\\%).\nDomain heterogeneity may introduce more construct-irrelevant variance sources.\nWith only $N{=}6$ benchmarks, formal moderator testing is infeasible; future work with additional benchmarks is needed.\n\n\\paragraph{Simpson's paradox implications.}\nThe OR flip (1.48$\\to$0.76) reveals that na\\\"ive association between accuracy improvement and DIF is confounded by item difficulty and discrimination.\nHowever, CTT properties explain only 4.2\\% of DIF variance---the phenomenon is fundamentally item-specific.\n\n\\paragraph{Audit protocol recommendation.}\nBased on our findings, we recommend a DIF-based audit protocol for benchmark maintainers: (1) run MH-DIF analysis at each major model generation release, (2) flag ETS Category~C items for review, (3) investigate flagged items for construct drift vs.\\ legitimate capability change, (4) maintain cumulative evidence across administrations.\nThis is a practical recommendation, not a formal contribution.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\textbf{Temporal coarseness.}\nOur primary analysis uses a binary 2023/2024 split.\nItem-Focused Trees (Section~\\ref{sec:ift}) partially address this by identifying a 2023-Q4 breakpoint, but quarterly MH sensitivity analysis would strengthen the finding.\nWithin-year variation may be masked by the binary partition.\n\n\\textbf{IRT misfit.}\n98\\% of models show $|L_z|{>}2$, and CFI${=}$0.68 confirms poor unidimensional fit.\nThe MH procedure is nonparametric and does not directly depend on IRT model fit; however, the conditioning variable (cross-subject total score) may have reduced validity in a multidimensional context.\nA multidimensional IRT robustness check (e.g., within-subject MIRT on high-C\\% subjects) would address this concern but is beyond the scope of the current analysis.\n\n\\textbf{Reasoning-RL.}\nResults for reasoning-RL models ($N{=}$13) are underpowered.\nDIF robustness is confirmed only for alignment-RL; reasoning-RL remains unvalidated.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nApplying MH-DIF to 5,219 models $\\times$ 12,508 MMLU items, we find that 30.8\\% of items exhibit systematic cohort-conditional differences in item functioning between pre-2024 and 2024 model generations.\nThis instability generalizes across six benchmarks (17.5--30.8\\%, all ${\\geq}$45$\\times$ above random), is not driven by capability improvement (${\\leq}$2.4\\,pp), and does not threaten ranking validity ($\\rho{=}0.994$).\nThe field's web-overlap ground truth cannot capture this differential signal; our semi-synthetic framework with cross-subject matching ($\\Delta$FPR${=}$0.000) provides a reusable validation infrastructure.\nDIF analysis offers benchmark maintainers a principled tool for understanding how item functioning evolves across model generations.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{20}\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021gsm8k}\nK.~Cobbe, V.~Kosaraju, M.~Bavarian, M.~Chen, H.~Jun, L.~Kaiser, M.~Plappert, J.~Tworek, J.~Hilton, R.~Nakano, C.~Hesse, and J.~Schulman.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv preprint arXiv:2110.14168}, 2021.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nY.~Dong, Y.~Jiang, H.~Deng, and L.~Qiu.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock \\emph{arXiv preprint arXiv:2402.15938}, 2024.\n\n\\bibitem[Gu et~al.(2024)]{gu2024surveying}\nZ.~Gu, E.~Fan, and W.-L.~Chiang.\n\\newblock A survey on evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2307.03109}, 2024.\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021measuring}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Holland and Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item functioning and the {M}antel-{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I.~Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, Y.~Zhang, and Y.~Zhao.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mantel and Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Perlitz et~al.(2024a)]{perlitz2024metabench}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock {METABENCH}: A large-scale collection of model evaluation results.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Perlitz et~al.(2024b)]{perlitz2024growing}\nY.~Perlitz, E.~Bandel, et~al.\n\\newblock Growing pains: Efficiently evaluating evolving benchmarks.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {tinyBenchmarks}: Evaluating {LLMs} with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Scale(2024)]{scale2024seal}\nScale.\n\\newblock {SEAL} leaderboards.\n\\newblock \\url{https://scale.com/leaderboard}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay et~al.(2006)]{sinharay2006bayesian}\nS.~Sinharay, M.~J. Haberman, and E.~T. Dorans.\n\\newblock A {B}ayesian approach to the detection of {DIF} across multiple administrations.\n\\newblock \\emph{Psychometrika}, 71(2):217--237, 2006.\n\n\\bibitem[Srivastava et~al.(2024)]{srivastava2024constat}\nM.~Srivastava, Y.~Chen, and Y.~Choi.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Strobl et~al.(2015)]{strobl2015rasch}\nC.~Strobl, J.~Kopf, and A.~Zeileis.\n\\newblock {R}asch trees: A new method for detecting differential item functioning in the {R}asch model.\n\\newblock \\emph{Psychometrika}, 80(2):289--316, 2015.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naber, et~al.\n\\newblock {LiveBench}: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Zellers et~al.(2019)]{zellers2019hellaswag}\nR.~Zellers, A.~Holtzman, Y.~Bisk, A.~Farcas, and Y.~Choi.\n\\newblock {HellaSwag}: Can a machine really finish your sentence?\n\\newblock In \\emph{ACL}, 2019.\n\n\\bibitem[Zieky(1993)]{zieky1993practical}\nM.~Zieky.\n\\newblock Practical questions in the use of {DIF} statistics in test development.\n\\newblock In P.~W. Holland and H.~Wainer, editors, \\emph{Differential Item Functioning}, pages 337--347. Lawrence Erlbaum, 1993.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "d53dec86-fb74-41d1-804f-c9eaa2e4f3c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "e3d87464-31d4-429b-ae6f-e13dec2b2390",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream session",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Tool call

_source line 22 · 2026-05-21T11:38:35.764Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TDuNWxcEQKCqVA22R8FwU7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d87464-31d4-429b-ae6f-e13dec2b2390",
  "isSidechain": false,
  "requestId": "req_011CbFeZtbZJYujc3b2SHCPt",
  "type": "assistant",
  "uuid": "4b25bd68-714c-430a-b698-64def722e28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011J832KorUX8N4LmqFGB5pS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13595,
      "cache_read_input_tokens": 43158,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 43158,
          "cache_creation_input_tokens": 13595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13595
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

_source line 23 · 2026-05-21T11:38:36.862Z_

<details><summary>↩ Tool result · `toolu_01TDuNWxcEQKCqVA22R8FwU7`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
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

Package natbib Warning: Citation `hendrycks2021measuring' on page 1 undefined o
n input line 41.


Package natbib Warning: Citation `cobbe2021gsm8k' on page 1 undefined on input 
line 41.


Package natbib Warning: Citation `zellers2019hellaswag' on page 1 undefined on 
input line 41.


Package natbib Warning: Citation `holland1988differential' on page 1 undefined 
on input line 45.


Package natbib Warning: Citation `mantel1959statistical' on page 1 undefined on
 input line 47.


Package natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on 
input line 49.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (22.14032pt too wide) in paragraph at lines 62--63
[]\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\T1/ptm/m/n/10.95 : 
$\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subject 
match-ing ($\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 FPR$[]$0.000),

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 71.


Package natbib Warning: Citation `srivastava2024constat' on page 2 undefined on
 input line 71.


Package natbib Warning: Citation `li2024task' on page 2 undefined on input line
 71.


Package natbib Warning: Citation `dong2024generalization' on page 2 undefined o
n input line 73.


Package natbib Warning: Citation `white2024livebench' on page 2 undefined on in
put line 76.


Package natbib Warning: Citation `scale2024seal' on page 2 undefined on input l
ine 76.


Package natbib Warning: Citation `perlitz2024growing' on page 2 undefined on in
put line 77.


Package natbib Warning: Citation `mantel1959statistical' on page 2 undefined on
 input line 81.


Package natbib Warning: Citation `zieky1993practical' on page 2 undefined on in
put line 81.


Package natbib Warning: Citation `strobl2015rasch' on page 2 undefined on input
 line 82.


Package natbib Warning: Citation `sinharay2006bayesian' on page 2 undefined on 
input line 83.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 87.


Package natbib Warning: Citation `gu2024surveying' on page 2 undefined on input
 line 87.


LaTeX Warning: Reference `sec:bifactor' on page 2 undefined on input line 88.

[2]

LaTeX Warning: Reference `tab:sensitivity' on page 3 undefined on input line 14
1.


LaTeX Warning: Reference `tab:within_family' on page 3 undefined on input line 
161.


LaTeX Warning: Reference `tab:domain' on page 3 undefined on input line 177.


LaTeX Warning: Reference `tab:permutation' on page 3 undefined on input line 20
1.

[3]

LaTeX Warning: Reference `tab:arch_composition' on page 4 undefined on input li
ne 240.


LaTeX Warning: Reference `tab:irt_fit' on page 4 undefined on input line 240.


LaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 24
2.


LaTeX Warning: Reference `tab:six_bench' on page 4 undefined on input line 287.



LaTeX Warning: Reference `tab:bench_chars' on page 4 undefined on input line 28
9.


LaTeX Warning: Reference `tab:gsm8k_dif' on page 4 undefined on input line 326.



LaTeX Warning: Reference `tab:gsm1k' on page 4 undefined on input line 329.


LaTeX Warning: Reference `tab:semi_synth' on page 4 undefined on input line 369
.


LaTeX Warning: Reference `tab:fpr_comparison' on page 4 undefined on input line
 371.


LaTeX Warning: Reference `tab:logistic' on page 4 undefined on input line 416.


LaTeX Warning: Reference `tab:simpsons' on page 4 undefined on input line 417.

[4]

LaTeX Warning: Reference `tab:ift' on page 5 undefined on input line 444.


LaTeX Warning: Reference `tab:graceful' on page 5 undefined on input line 471.


LaTeX Warning: Reference `tab:constat' on page 5 undefined on input line 515.


LaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 515.


LaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 544.

[5]

LaTeX Warning: Reference `tab:rl_retention' on page 6 undefined on input line 5
85.


LaTeX Warning: Reference `tab:bifactor' on page 6 undefined on input line 613.


LaTeX Warning: Reference `sec:limitations' on page 6 undefined on input line 61
7.


LaTeX Warning: Reference `tab:item_gen' on page 6 undefined on input line 641.


LaTeX Warning: Reference `tab:bayesian' on page 6 undefined on input line 662.

[6]

LaTeX Warning: Reference `sec:ift' on page 7 undefined on input line 692.

[7] [8] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [9]

Package natbib Warning: There were undefined citations.

[10] [11] [12] (./paper.aux

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
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (12 pages, 182845 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
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
Overfull \hbox (20.44934pt too wide) in paragraph at lines 41--44
\T1/ptm/m/n/10.95 LLM bench-marks such as MMLU [[]Hendrycks et al.[], []2021[]]
, GSM8K [[]Cobbe et al.[], []2021[]], and Hel-laSwag [[]Zellers
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]
Overfull \hbox (22.14032pt too wide) in paragraph at lines 62--63
[]\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\T1/ptm/m/n/10.95 : 
$\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subject 
match-ing ($\OT1/cmr/m/n/10.95 ^^A$\T1/ptm/m/n/10.95 FPR$[]$0.000),
[2] [3] [4] [5] [6] [7] [8]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [9] [10] [11]
[12] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times
/utmri8a.pfb>
Output written on paper.pdf (12 pages, 187292 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b25bd68-714c-430a-b698-64def722e28f",
  "isSidechain": false,
  "promptId": "e2457fe4-0368-463d-8b25-914f7f7a2ad3",
  "type": "user",
  "uuid": "05128dcb-c8a2-4681-9639-b7c510c92285",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `hendrycks2021measuring' on page 1 undefined o\nn input line 41.\n\n\nPackage natbib Warning: Citation `cobbe2021gsm8k' on page 1 undefined on input \nline 41.\n\n\nPackage natbib Warning: Citation `zellers2019hellaswag' on page 1 undefined on \ninput line 41.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 1 undefined \non input line 45.\n\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 1 undefined on\n input line 47.\n\n\nPackage natbib Warning: Citation `perlitz2024metabench' on page 1 undefined on \ninput line 49.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (22.14032pt too wide) in paragraph at lines 62--63\n[]\\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\\T1/ptm/m/n/10.95 : \n$\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subject \nmatch-ing ($\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 FPR$[]$0.000),\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 71.\n\n\nPackage natbib Warning: Citation `srivastava2024constat' on page 2 undefined on\n input line 71.\n\n\nPackage natbib Warning: Citation `li2024task' on page 2 undefined on input line\n 71.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 2 undefined o\nn input line 73.\n\n\nPackage natbib Warning: Citation `white2024livebench' on page 2 undefined on in\nput line 76.\n\n\nPackage natbib Warning: Citation `scale2024seal' on page 2 undefined on input l\nine 76.\n\n\nPackage natbib Warning: Citation `perlitz2024growing' on page 2 undefined on in\nput line 77.\n\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 2 undefined on\n input line 81.\n\n\nPackage natbib Warning: Citation `zieky1993practical' on page 2 undefined on in\nput line 81.\n\n\nPackage natbib Warning: Citation `strobl2015rasch' on page 2 undefined on input\n line 82.\n\n\nPackage natbib Warning: Citation `sinharay2006bayesian' on page 2 undefined on \ninput line 83.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 87.\n\n\nPackage natbib Warning: Citation `gu2024surveying' on page 2 undefined on input\n line 87.\n\n\nLaTeX Warning: Reference `sec:bifactor' on page 2 undefined on input line 88.\n\n[2]\n\nLaTeX Warning: Reference `tab:sensitivity' on page 3 undefined on input line 14\n1.\n\n\nLaTeX Warning: Reference `tab:within_family' on page 3 undefined on input line \n161.\n\n\nLaTeX Warning: Reference `tab:domain' on page 3 undefined on input line 177.\n\n\nLaTeX Warning: Reference `tab:permutation' on page 3 undefined on input line 20\n1.\n\n[3]\n\nLaTeX Warning: Reference `tab:arch_composition' on page 4 undefined on input li\nne 240.\n\n\nLaTeX Warning: Reference `tab:irt_fit' on page 4 undefined on input line 240.\n\n\nLaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 24\n2.\n\n\nLaTeX Warning: Reference `tab:six_bench' on page 4 undefined on input line 287.\n\n\n\nLaTeX Warning: Reference `tab:bench_chars' on page 4 undefined on input line 28\n9.\n\n\nLaTeX Warning: Reference `tab:gsm8k_dif' on page 4 undefined on input line 326.\n\n\n\nLaTeX Warning: Reference `tab:gsm1k' on page 4 undefined on input line 329.\n\n\nLaTeX Warning: Reference `tab:semi_synth' on page 4 undefined on input line 369\n.\n\n\nLaTeX Warning: Reference `tab:fpr_comparison' on page 4 undefined on input line\n 371.\n\n\nLaTeX Warning: Reference `tab:logistic' on page 4 undefined on input line 416.\n\n\nLaTeX Warning: Reference `tab:simpsons' on page 4 undefined on input line 417.\n\n[4]\n\nLaTeX Warning: Reference `tab:ift' on page 5 undefined on input line 444.\n\n\nLaTeX Warning: Reference `tab:graceful' on page 5 undefined on input line 471.\n\n\nLaTeX Warning: Reference `tab:constat' on page 5 undefined on input line 515.\n\n\nLaTeX Warning: Reference `tab:dvd' on page 5 undefined on input line 515.\n\n\nLaTeX Warning: Reference `tab:ensemble' on page 5 undefined on input line 544.\n\n[5]\n\nLaTeX Warning: Reference `tab:rl_retention' on page 6 undefined on input line 5\n85.\n\n\nLaTeX Warning: Reference `tab:bifactor' on page 6 undefined on input line 613.\n\n\nLaTeX Warning: Reference `sec:limitations' on page 6 undefined on input line 61\n7.\n\n\nLaTeX Warning: Reference `tab:item_gen' on page 6 undefined on input line 641.\n\n\nLaTeX Warning: Reference `tab:bayesian' on page 6 undefined on input line 662.\n\n[6]\n\nLaTeX Warning: Reference `sec:ift' on page 7 undefined on input line 692.\n\n[7] [8] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] [11] [12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 182845 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (20.44934pt too wide) in paragraph at lines 41--44\n\\T1/ptm/m/n/10.95 LLM bench-marks such as MMLU [[]Hendrycks et al.[], []2021[]]\n, GSM8K [[]Cobbe et al.[], []2021[]], and Hel-laSwag [[]Zellers\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\nOverfull \\hbox (22.14032pt too wide) in paragraph at lines 62--63\n[]\\T1/ptm/b/n/10.95 Semi-synthetic val-i-da-tion frame-work\\T1/ptm/m/n/10.95 : \n$\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 TPR method-ol-ogy with cross-subject \nmatch-ing ($\\OT1/cmr/m/n/10.95 ^^A$\\T1/ptm/m/n/10.95 FPR$[]$0.000),\n[2] [3] [4] [5] [6] [7] [8]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [9] [10] [11]\n[12] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\n/utmri8a.pfb>\nOutput written on paper.pdf (12 pages, 187292 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4b25bd68-714c-430a-b698-64def722e28f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "05128dcb-c8a2-4681-9639-b7c510c92285",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream session",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Assistant

_source line 26 · 2026-05-21T11:38:48.429Z_

PDF 编译成功（12 页，187KB）。所有引用和交叉引用在第二遍编译后已正确解析。

论文覆盖了 experiment_data.json 中全部 16 个实验，每个实验对应专属 section 和 table：

- **主体实验** (Sections 4.1--4.8): MMLU temporal DIF、permutation null、architecture stratification、6-benchmark generalization、GSM8K+GSM1K、semi-synthetic validation、Simpson's paradox、Item-Focused Trees、ranking stability
- **基线对比** (Section 4.9): ConStat、DVD、ensemble fusion
- **鲁棒性与负面结果** (Sections 4.10--4.13): RL robustness、bifactor IRT pilot、item generation calibration、cumulative Bayesian DIF

narrative guidance 的关键要素已嵌入：temporal coarseness 在 IFT section 和 limitations 中显式处理；IRT misfit 在 architecture section 和 limitations 中讨论；Simpson's paradox 从 main evidence 降级为 supplementary；Claim 1 措辞为 "systematic cohort-conditional differences"；audit protocol 作为 discussion recommendation。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05128dcb-c8a2-4681-9639-b7c510c92285",
  "isSidechain": false,
  "requestId": "req_011CbFeaDmE9KQsDJqK9VueF",
  "type": "assistant",
  "uuid": "c66432b5-2a3a-4ef5-a45d-a17a1e699dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T110541/median",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LtG4s3EQxrcQXq6GWo2YEa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7327,
      "cache_read_input_tokens": 56753,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7327,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 56753,
          "cache_creation_input_tokens": 7327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7327
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T110541 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_benc…",
  "leafUuid": "c66432b5-2a3a-4ef5-a45d-a17a1e699dcb",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate simulated paper for dream session",
  "sessionId": "ca482af7-7948-4e9b-b65f-42d545ce5059"
}
```

---
