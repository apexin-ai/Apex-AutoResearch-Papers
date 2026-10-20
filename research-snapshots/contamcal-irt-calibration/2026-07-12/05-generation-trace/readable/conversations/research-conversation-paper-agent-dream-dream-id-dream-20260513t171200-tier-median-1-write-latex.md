# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/530f5efb-d29b-4342-9da3-66d253c182cd.jsonl`
- **Structured JSON:** [`9feaf531e16786c6b92f.json`](../../sessions/9f/9feaf531e16786c6b92f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T17:39:06.738Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T17:39:06.738Z",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/experiment_data.json`（先 Read 此文件）\n- Venue：AAAI 2027\n- Narrative guidance：Claims需要分regime表述。ContamCal在SFT regime下显著校准（MAE 2-4pp），在RL regime下提供保守但诚实的宽CI。 Claim 2（signal survival）实际上升为最强贡献——systematic signal×regime mapping是empirically novel。 Claim 3 identifiability bounds从\"guarantee\"变为\"diagnostic tool\"。HumanEval降级为appendix注释。 需要补充ablation showing measurement error model边际贡献 + sensitivity analysis showing coverage gap与local independence violation关系。 仍然beat DCR和majority baselines，paper viable for AAAI但需要honest limitations section。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T17:39:06.750Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T17:39:06.750Z",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-13T17:39:06.832Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/experiment_data.json`（先 Read 此文件）
- Venue：AAAI 2027
- Narrative guidance：Claims需要分regime表述。ContamCal在SFT regime下显著校准（MAE 2-4pp），在RL regime下提供保守但诚实的宽CI。 Claim 2（signal survival）实际上升为最强贡献——systematic signal×regime mapping是empirically novel。 Claim 3 identifiability bounds从"guarantee"变为"diagnostic tool"。HumanEval降级为appendix注释。 需要补充ablation showing measurement error model边际贡献 + sensitivity analysis showing coverage gap与local independence violation关系。 仍然beat DCR和majority baselines，paper viable for AAAI但需要honest limitations section。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "6fe8cc64-18c3-4cb4-9950-33354ad68ba4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T17:39:06.831Z_

```json
{
  "parentUuid": "6fe8cc64-18c3-4cb4-9950-33354ad68ba4",
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
  "uuid": "f13b6e2c-15cc-4fae-a83e-a9c4445db034",
  "timestamp": "2026-05-13T17:39:06.831Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T17:39:06.832Z_

```json
{
  "parentUuid": "f13b6e2c-15cc-4fae-a83e-a9c4445db034",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "595ea5cb-f95c-47fb-9303-aed4c9c1141b",
  "timestamp": "2026-05-13T17:39:06.832Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
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
  "aiTitle": "Generate AAAI paper for contamination calibration IRT",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Assistant

_source line 7 · 2026-05-13T17:39:09.791Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment data and paper framing files to understand what I need to write.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595ea5cb-f95c-47fb-9303-aed4c9c1141b",
  "isSidechain": false,
  "requestId": "req_011CazybLmLrdQb1UyB6sobd",
  "type": "assistant",
  "uuid": "08a10d0b-b0ec-4f5f-8eba-db89184c3821",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhQLWKUDugiT3Z1az7GL1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 11841,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 233,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11253
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

_source line 8 · 2026-05-13T17:39:10.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HZo3MaJDyd7ac3SRJENBU3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08a10d0b-b0ec-4f5f-8eba-db89184c3821",
  "isSidechain": false,
  "requestId": "req_011CazybLmLrdQb1UyB6sobd",
  "type": "assistant",
  "uuid": "f6c84420-cfd9-4f21-b37a-143afc308465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhQLWKUDugiT3Z1az7GL1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 11841,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 233,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11253
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

_source line 9 · 2026-05-13T17:39:11.203Z_

<details><summary>↩ Tool result · `toolu_01HZo3MaJDyd7ac3SRJENBU3`</summary>

```text
1	[
2	  {
3	    "name": "controlled_sft_injection",
4	    "description": "Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT injection， 3 seeds per condition，45 SFT runs total。Paraphrase quality validated via cosine similarity + BLEU。\n",
5	    "results": {
6	      "paraphrase_cosine_sim_mean": 0.88,
7	      "paraphrase_bleu_mean": 0.22,
8	      "human_spotcheck_quality_rate": 0.91,
9	      "mmlu_inflation_at_100pct_0.5B_pp": 11.2,
10	      "mmlu_inflation_at_100pct_1.5B_pp": 9.4,
11	      "mmlu_inflation_at_100pct_3B_pp": 7.8,
12	      "gsm8k_inflation_at_100pct_0.5B_pp": 14.6,
13	      "gsm8k_inflation_at_100pct_3B_pp": 10.3,
14	      "arc_inflation_at_100pct_3B_pp": 8.1,
15	      "humaneval_inflation_at_100pct_3B_pp": 6.2,
16	      "inflation_at_5pct_mean_pp": 1.8,
17	      "inflation_at_25pct_mean_pp": 5.9,
18	      "inflation_at_50pct_mean_pp": 8.7,
19	      "dose_response_perfectly_monotonic": false,
20	      "dose_response_25_to_50_plateau_count": 2,
21	      "cross_seed_std_mmlu_pp": 0.6,
22	      "cross_seed_std_gsm8k_pp": 1.1,
23	      "cross_seed_std_humaneval_pp": 2.3,
24	      "sft_runs_completed": 45,
25	      "sft_runs_failed": 1,
26	      "gpu_hours_actual": 46
27	    },
28	    "tables": [
29	      {
30	        "name": "Table 1: Score Inflation by Dosage and Model Scale",
31	        "rows": [
32	          {
33	            "model": "Qwen2.5-0.5B",
34	            "dose_0": "baseline",
35	            "dose_5": "+1.9±0.4",
36	            "dose_25": "+7.1±0.8",
37	            "dose_50": "+9.8±1.0",
38	            "dose_100": "+11.2±0.7"
39	          },
40	          {
41	            "model": "Qwen2.5-1.5B",
42	            "dose_0": "baseline",
43	            "dose_5": "+1.6±0.5",
44	            "dose_25": "+5.6±0.7",
45	            "dose_50": "+8.2±0.9",
46	            "dose_100": "+9.4±0.6"
47	          },
48	          {
49	            "model": "Qwen2.5-3B",
50	            "dose_0": "baseline",
51	            "dose_5": "+1.4±0.4",
52	            "dose_25": "+4.9±0.6",
53	            "dose_50": "+7.5±1.1",
54	            "dose_100": "+7.8±0.5",
55	            "note": "MMLU average across 3 seeds; 25→50 plateau visible at 3B"
56	          }
57	        ]
58	      }
59	    ],
60	    "figures": [],
61	    "analysis": "Injection pipeline工作正常，产生了可用的ground-truth对。主要发现：(1) inflation magnitude与scale负相关（符合预期）， (2) dose-response大体单调但25%→50%区间有plateau/非单调扰动（在2/12 benchmark×scale条件中）， (3) HumanEval的cross-seed variance是MMLU的~4倍，预示后续γ estimation在HumanEval上会不稳定。 需要在paper中将25%→50% plateau解释为\"SFT memorization的marginal return递减\"而非pipeline artifact。\n\n\nMedian档下contamination injection成功产生可测量的inflation，但dose-response不完全单调。 小模型(0.5B)受contamination影响更大（memorization capacity更受限，overfitting更快）， 大模型(3B)的inflation相对较小因为其pre-training knowledge已覆盖更多benchmark内容。 25%→50%区间出现plateau是因为SFT的marginal memorization return在这个区间递减—— 模型已经从25%的paraphrases中学到了大部分pattern，额外的25%主要是冗余reinforcement。 GSM8K和HumanEval的cross-seed variance更大因为item数少、格式更结构化导致memorization效果更variable。 有1个run失败是realistic的（OOM或NaN loss），在45 runs中是合理的failure rate。\n"
62	  },
63	  {
64	    "name": "stage1_signal_pipeline",
65	    "description": "4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique)  computed on all exp-001 models。输出per-model-item exposure scores。\n",
66	    "results": {
67	      "embedding_auc_sft_contaminated_mean": 0.81,
68	      "minkpp_auc_sft_contaminated_mean": 0.74,
69	      "constat_auc_sft_contaminated_mean": 0.69,
70	      "selfcritique_auc_sft_contaminated_mean": 0.66,
71	      "embedding_auc_clean_models_mean": 0.52,
72	      "minkpp_auc_clean_models_mean": 0.51,
73	      "constat_auc_clean_models_mean": 0.53,
74	      "selfcritique_auc_clean_models_mean": 0.5,
75	      "signal_computation_gpu_hours": 18,
76	      "per_item_score_coverage_pct": 98.5,
77	      "embedding_fp_rate_at_tpr_80": 0.18,
78	      "minkpp_fp_rate_at_tpr_80": 0.24,
79	      "constat_fp_rate_at_tpr_80": 0.3,
80	      "selfcritique_fp_rate_at_tpr_80": 0.33,
81	      "signal_corr_embedding_minkpp": 0.58,
82	      "signal_corr_embedding_constat": 0.31,
83	      "signal_corr_embedding_selfcritique": 0.22,
84	      "auc_variance_across_dosage_5pct": 0.04,
85	      "auc_variance_across_dosage_100pct": 0.01
86	    },
87	    "tables": [
88	      {
89	        "name": "Table 2: Per-Signal AUC by Training Regime (SFT contaminated models)",
90	        "rows": [
91	          {
92	            "signal": "Embedding Retrieval",
93	            "auc_sft_5pct": "0.61±0.04",
94	            "auc_sft_25pct": "0.77±0.02",
95	            "auc_sft_100pct": "0.86±0.01"
96	          },
97	          {
98	            "signal": "Min-K%++",
99	            "auc_sft_5pct": "0.57±0.05",
100	            "auc_sft_25pct": "0.71±0.03",
101	            "auc_sft_100pct": "0.79±0.02"
102	          },
103	          {
104	            "signal": "ConStat",
105	            "auc_sft_5pct": "0.55±0.06",
106	            "auc_sft_25pct": "0.66±0.04",
107	            "auc_sft_100pct": "0.74±0.02"
108	          },
109	          {
110	            "signal": "Self-Critique",
111	            "auc_sft_5pct": "0.54±0.05",
112	            "auc_sft_25pct": "0.63±0.04",
113	            "auc_sft_100pct": "0.71±0.03"
114	          }
115	        ]
116	      }
117	    ],
118	    "figures": [],
119	    "analysis": "Individual signals在SFT regime下都work但各有weakness。Embedding最强但需要access to training data embeddings， Self-Critique最弱但也是唯一不需要logits的信号。Key insight for downstream:  没有单一signal AUC>0.85（averaged across dosages），所以fusion是必要的而非optional。 Clean model specificity good（AUC≈0.50），为exp-009的near-zero γ check提供了baseline expectation。\n\n\nMedian档下individual signal AUCs在SFT regime下可用但没有一个是outstanding。 Embedding retrieval最强(0.81)因为paraphrase保持了高semantic similarity，这是最直接的信号。 Min-K%++次之(0.74)因为SFT contamination确实改变了token-level surprise pattern，但noise较大。 ConStat(0.69)和Self-Critique(0.66)在SFT下弱一些——ConStat依赖original vs paraphrase gap， 但我们的paraphrase quality较高导致gap缩小；Self-Critique是最indirect的信号。 Clean model上所有signal AUC≈0.50-0.53（near-chance），confirming specificity。 Signal间correlation中等偏低（0.22-0.58），说明RRF fusion有信息互补空间但也意味着 每个signal捕获contamination的不同facet。低dosage(5%)时AUC variance大是因为signal-to-noise低， high dosage时AUC稳定。1.5%的items缺失coverage来自少数OOM或parsing failure cases。\n"
120	  },
121	  {
122	    "name": "rrf_aggregation_ablation",
123	    "description": "RRF fusion of 4 signals + ablations (equal-weight averaging, single-signal,  calibration-weighted RRF, 2-signal closed-weight mode, FP injection robustness)。\n",
124	    "results": {
125	      "rrf_4signal_auc_mean": 0.76,
126	      "rrf_4signal_auc_at_25pct_dose": 0.74,
127	      "rrf_4signal_auc_at_100pct_dose": 0.82,
128	      "equal_weight_avg_auc_mean": 0.73,
129	      "calibration_weighted_rrf_auc_mean": 0.77,
130	      "best_single_signal_auc_mean": 0.74,
131	      "worst_single_signal_auc_mean": 0.66,
132	      "rrf_2signal_closed_weight_auc_mean": 0.65,
133	      "rrf_fp_injection_1x_auc": 0.73,
134	      "rrf_fp_injection_2x_auc": 0.68,
135	      "rrf_vs_best_single_improvement_pp": 2.0,
136	      "calibration_weighted_vs_rrf_improvement_pp": 1.0
137	    },
138	    "tables": [
139	      {
140	        "name": "Table 3: Aggregation Method Comparison",
141	        "rows": [
142	          {
143	            "method": "RRF (4 signals)",
144	            "auc_mean": 0.76,
145	            "auc_std": 0.03,
146	            "note": "primary"
147	          },
148	          {
149	            "method": "Calibration-weighted RRF",
150	            "auc_mean": 0.77,
151	            "auc_std": 0.03,
152	            "note": "marginal gain, adds circularity"
153	          },
154	          {
155	            "method": "Equal-weight averaging",
156	            "auc_mean": 0.73,
157	            "auc_std": 0.04,
158	            "note": ""
159	          },
160	          {
161	            "method": "Best single (Embedding)",
162	            "auc_mean": 0.74,
163	            "auc_std": 0.03,
164	            "note": ""
165	          },
166	          {
167	            "method": "2-signal closed-weight",
168	            "auc_mean": 0.65,
169	            "auc_std": 0.05,
170	            "note": "ConStat + Self-Critique only"
171	          }
172	        ]
173	      }
174	    ],
175	    "figures": [],
176	    "analysis": "RRF fusion confirms其作为design choice的合理性。核心发现：(1) fusion > single signal但margin modest(2pp)， (2) calibration weighting几乎不优于vanilla RRF——empirically validates anti-meta-circularity argument， (3) closed-weight 2-signal mode可用但significantly degraded，需要honest reporting。 Paper中应将RRF framed as \"principled default\"而非methodological contribution。 FP robustness check为exp-005的measurement error model提供了complementary evidence。\n\n\nMedian档下RRF fusion AUC=0.76，落在[0.7, 0.8]范围内。RRF比best single signal(embedding, 0.74) 提升仅2pp——improvement存在但不dramatic，因为signals间correlation虽然不高(0.22-0.58)但也不够低 到让fusion产生大幅增益。Calibration-weighted RRF(0.77)略优于vanilla RRF但差距很小(1pp)， 这是meta-circularity argument的empirical support——learned weights不值得引入的复杂性和circularity风险。 Equal-weight averaging(0.73)几乎和RRF持平说明rank-based vs score-based的差异在此setting不大。 2-signal closed-weight mode(0.65)显著下降——缺少embedding和Min-K%++这两个strongest signals 让AUC落到仅marginal above useful threshold。FP injection at 2x rate将AUC降至0.68， 说明RRF对noise有一定robustness但不是immune。这些结果support \"RRF as principled design choice\" 的framing——不是contribution，而是在simplicity/performance/circularity三角中的合理选择。\n"
177	  },
178	  {
179	    "name": "simulation_identifiability_sweep",
180	    "description": "144-condition synthetic sweep: AUC(6) × N_models(4) × prior(3) × exposure_type(2)， 10 seeds each。Fisher Information analysis。Growing Pains pre-estimation sub-experiment。\n",
181	    "results": {
182	      "total_conditions_run": 144,
183	      "total_fits": 1440,
184	      "convergence_rate_pct": 96.5,
185	      "gamma_rmse_at_auc55_n50": 0.34,
186	      "gamma_rmse_at_auc65_n50": 0.21,
187	      "gamma_rmse_at_auc70_n50": 0.14,
188	      "gamma_rmse_at_auc80_n50": 0.08,
189	      "gamma_rmse_at_auc90_n50": 0.05,
190	      "theta_corr_at_auc70_n50": 0.91,
191	      "theta_corr_at_auc55_n50": 0.76,
192	      "coverage_95_at_auc70_n50_pct": 86,
193	      "coverage_95_at_auc55_n50_pct": 72,
194	      "coverage_80_at_auc70_n50_pct": 69,
195	      "ci_width_at_auc70_n50_pp": 5.2,
196	      "ci_width_at_auc55_n50_pp": 17.3,
197	      "posterior_corr_theta_gamma_at_auc70": -0.38,
198	      "posterior_corr_theta_gamma_at_auc55": -0.67,
199	      "minimum_useful_auc_threshold": 0.65,
200	      "n_models_20_coverage_95_at_auc70": 79,
201	      "n_models_200_coverage_95_at_auc70": 91,
202	      "growing_pains_improvement_n20_coverage_pp": 4.5,
203	      "growing_pains_improvement_n50_coverage_pp": 1.8,
204	      "fisher_info_structural_identifiable_above_auc": 0.58,
205	      "fisher_info_practical_identifiable_above_auc": 0.68,
206	      "prior_sensitivity_strong_vs_weak_gamma_rmse_ratio": 0.72,
207	      "continuous_vs_binary_exposure_gamma_rmse_ratio": 0.85,
208	      "divergent_transition_rate_overall_pct": 1.2
209	    },
210	    "tables": [
211	      {
212	        "name": "Table 4: γ Recovery RMSE by AUC × N_models (continuous exposure, medium prior)",
213	        "rows": [
214	          {
215	            "auc": 0.55,
216	            "n20": "0.48±0.12",
217	            "n50": "0.34±0.08",
218	            "n100": "0.27±0.06",
219	            "n200": "0.22±0.04"
220	          },
221	          {
222	            "auc": 0.65,
223	            "n20": "0.31±0.09",
224	            "n50": "0.21±0.05",
225	            "n100": "0.15±0.03",
226	            "n200": "0.11±0.02"
227	          },
228	          {
229	            "auc": 0.7,
230	            "n20": "0.23±0.07",
231	            "n50": "0.14±0.04",
232	            "n100": "0.10±0.02",
233	            "n200": "0.07±0.01"
234	          },
235	          {
236	            "auc": 0.8,
237	            "n20": "0.15±0.05",
238	            "n50": "0.08±0.02",
239	            "n100": "0.06±0.01",
240	            "n200": "0.04±0.01"
241	          },
242	          {
243	            "auc": 0.9,
244	            "n20": "0.09±0.03",
245	            "n50": "0.05±0.01",
246	            "n100": "0.03±0.01",
247	            "n200": "0.02±0.01"
248	          }
249	        ]
250	      },
251	      {
252	        "name": "Table 5: 95% Coverage by AUC × N_models",
253	        "rows": [
254	          {
255	            "auc": 0.55,
256	            "n50": "72%",
257	            "n100": "77%",
258	            "n200": "81%"
259	          },
260	          {
261	            "auc": 0.65,
262	            "n50": "80%",
263	            "n100": "84%",
264	            "n200": "88%"
265	          },
266	          {
267	            "auc": 0.7,
268	            "n50": "86%",
269	            "n100": "89%",
270	            "n200": "92%"
271	          },
272	          {
273	            "auc": 0.8,
274	            "n50": "90%",
275	            "n100": "93%",
276	            "n200": "95%"
277	          }
278	        ]
279	      }
280	    ],
281	    "figures": [],
282	    "analysis": "Identifiability sweep confirms paper Claim 3但需要nuanced framing。AUC≥0.70是\"safe zone\"， 0.58-0.68是\"structural but not practical\" zone，<0.58是fundamentally unidentifiable。 Coverage gap(95% nominal → 86% actual at AUC=0.70, N=50)是persistent——measurement error model(exp-005) 需要close this gap。Fisher Information analysis提供了theoretical grounding， 将empirical threshold elevated from \"observed rule-of-thumb\" to \"information-theoretically justified bound\"。 Paper中Claim 3应reframe为\"diagnostic tool\"——告诉用户何时可信任校准结果。\n\n\nMedian档下identifiability呈现clear但imperfect pattern。AUC=0.70是practical threshold—— γ RMSE=0.14足以distinguish contaminated from clean，CI width=5.2pp是actionable的。 AUC<0.65时coverage严重退化(72% at 95% nominal)因为posterior θ-γ correlation升高(-0.67)， model难以区分\"high ability\"和\"high contamination\"。这是fundamental——low-quality signal 下contamination effect和ability是confounded的。 Coverage即使在good conditions(AUC=0.70, N=50)下也only 86%而非95%，gap来自： (a) 4PL的c/d参数引入额外uncertainty未完全captured by priors， (b) local independence violation的residual effects（synthetic data也有correlation through shared generation process）。 Fisher Information分析区分structural vs practical identifiability：structurally identifiable above AUC≈0.58 （参数theoretically unique），但practically identifiable above AUC≈0.68（estimation precision sufficient）。 这10pp gap就是\"theoretically possible but practically unreliable\"的zone。 Growing Pains pre-estimation在N=20时帮助较大(+4.5pp coverage)因为informative item priors 弥补了few-examinee setting的information deficit，但N≥50时边际收益递减。 Continuous exposure优于binary(RMSE ratio 0.85)但差距不如预期大，因为在moderate AUC下 continuous scores的额外precision被noise offset。Prior sensitivity存在(ratio 0.72) 但不dominant——数据information足以在good AUC下override prior，但weak AUC下prior matters more。 3.5%的fits未converge主要集中在AUC=0.55 + N=20的extreme corner。\n"
283	  },
284	  {
285	    "name": "noise_propagation_analysis",
286	    "description": "(A) Measurement error model: exposure_ij ~ N(τ_ij, σ_e²) in Stan。 (B) Post-hoc noise injection at 1×/1.5×/2× levels。 Compare coverage against point-estimate exposure baseline。\n",
287	    "results": {
288	      "measurement_error_model_converges": true,
289	      "convergence_rate_pct": 94,
290	      "me_model_coverage_95_sft_pct": 88,
291	      "me_model_coverage_80_sft_pct": 72,
292	      "me_model_coverage_50_sft_pct": 43,
293	      "point_estimate_coverage_95_sft_pct": 81,
294	      "point_estimate_coverage_80_sft_pct": 63,
295	      "point_estimate_coverage_50_sft_pct": 36,
296	      "me_model_coverage_improvement_95_pp": 7,
297	      "me_model_coverage_improvement_80_pp": 9,
298	      "me_model_ci_width_increase_sft_pp": 1.4,
299	      "me_model_ci_width_increase_rl_pp": 4.2,
300	      "me_model_mae_change_pp": 0.3,
301	      "sigma_e_estimated_sft": 0.18,
302	      "sigma_e_estimated_rl": 0.41,
303	      "posthoc_noise_1x_coverage_95": 83,
304	      "posthoc_noise_1.5x_coverage_95": 79,
305	      "posthoc_noise_2x_coverage_95": 74,
306	      "me_model_fit_time_ratio_vs_standard": 1.8,
307	      "me_model_gamma_posterior_width_increase_pct": 25,
308	      "residual_coverage_gap_from_nominal_pp": 7
309	    },
310	    "tables": [
311	      {
312	        "name": "Table 6: Coverage Comparison — Measurement Error Model vs Point Estimate",
313	        "rows": [
314	          {
315	            "level": "50%",
316	            "point_est": "36%",
317	            "me_model": "43%",
318	            "delta": "+7pp"
319	          },
320	          {
321	            "level": "80%",
322	            "point_est": "63%",
323	            "me_model": "72%",
324	            "delta": "+9pp"
325	          },
326	          {
327	            "level": "95%",
328	            "point_est": "81%",
329	            "me_model": "88%",
330	            "delta": "+7pp"
331	          },
332	          {
333	            "level": "nominal gap at 95%",
334	            "point_est": "14pp",
335	            "me_model": "7pp",
336	            "delta": "halved"
337	          }
338	        ]
339	      }
340	    ],
341	    "figures": [],
342	    "analysis": "Measurement error model是paper的necessary component而非optional enhancement。7pp coverage improvement 是substantive的，且mechanism principled(noise propagation vs ad-hoc widening)。 但残余7pp gap需要honest discussion——attributable to local independence violation。 这实际strengthens paper: 我们can diagnose为什么coverage不perfect（local independence） 而非simply report unexplained undercoverage。建议在Limitations section写： \"residual coverage gap is consistent with local independence violation magnitude estimated from posterior predictive checks on item residual correlations\"。\n\n\nMedian档下measurement error model改善coverage但不完全close the gap。 从81%→88%(at 95% nominal)——gap从14pp缩至7pp。剩余7pp gap来源： (a) local independence violation（single model的item responses correlated through shared parameters， measurement error model不address这个），(b) 4PL参数estimation uncertainty的propagation不完整 （c/d参数的priors可能too tight）。 ME model的mechanism是通过σ_e将exposure noise propagate到γ posterior，导致CI自动变宽。 SFT regime σ_e=0.18(signals较reliable)，RL regime σ_e=0.41(signals noisy)—— 这个差异drives CI width的regime-conditional behavior，是\"correct behavior\"framing的key evidence。 MAE几乎不变(+0.3pp)说明ME model主要影响uncertainty而非point estimate—— point estimate已经reasonable，问题在于CI太narrow。 Post-hoc noise injection的coverage反而下降(83→74 at 2x)因为injected noise不matching model's noise assumption——这validates为什么proper ME model优于ad-hoc noise injection。 Fit time增加1.8倍因为latent τ的sampling增加了posterior dimension。\n"
343	  },
344	  {
345	    "name": "irt_calibration_and_baselines",
346	    "description": "4PL+γ IRT (global γ and per-benchmark γ_k) on controlled models。 7 baselines comparison。5 evaluation metrics。3 seeds。\n",
347	    "results": {
348	      "global_gamma_mae_pp": 3.8,
349	      "global_gamma_coverage_95_pct": 84,
350	      "global_gamma_coverage_80_pct": 67,
351	      "global_gamma_ci_width_mean_pp": 5.1,
352	      "global_gamma_kendall_tau": 0.85,
353	      "global_gamma_value": 0.38,
354	      "global_gamma_ci": [
355	        0.24,
356	        0.53
357	      ],
358	      "perbench_gamma_k_mmlu": 0.42,
359	      "perbench_gamma_k_gsm8k": 0.51,
360	      "perbench_gamma_k_arc": 0.35,
361	      "perbench_gamma_k_humaneval": 0.19,
362	      "perbench_gamma_k_humaneval_ci": [
363	        -0.14,
364	        0.52
365	      ],
366	      "perbench_gamma_k_humaneval_ci_includes_zero": true,
367	      "perbench_mae_pp": 3.1,
368	      "perbench_coverage_95_pct": 87,
369	      "perbench_coverage_80_pct": 71,
370	      "perbench_ci_width_mean_pp": 4.8,
371	      "perbench_kendall_tau": 0.88,
372	      "perbench_dose_response_monotonic": false,
373	      "perbench_dose_response_violation_benchmarks": [
374	        "MMLU-3B-25to50",
375	        "ARC-3B-25to50"
376	      ],
377	      "raw_mae_pp": 8.4,
378	      "remove_rescore_mae_pp": 5.6,
379	      "single_signal_2pl_mae_pp": 5.2,
380	      "vanilla_4pl_mae_pp": 7.1,
381	      "linear_regression_mae_pp": 4.5,
382	      "emperor_rephrase_mae_pp": 6.8,
383	      "emperor_shuffle_mae_pp": 7.2,
384	      "dcr_mae_pp": 4.1,
385	      "contam_cal_vs_raw_p": 0.001,
386	      "contam_cal_vs_remove_rescore_p": 0.008,
387	      "contam_cal_vs_dcr_p": 0.042,
388	      "contam_cal_vs_linear_regression_p": 0.087,
389	      "baselines_significantly_beaten_count": 5,
390	      "baselines_not_significantly_beaten": [
391	        "linear_regression (p=0.087)",
392	        "DCR (p=0.042 marginal)"
393	      ],
394	      "max_rhat": 1.008,
395	      "min_bulk_ess": 820,
396	      "divergent_pct": 0.8,
397	      "posterior_predictive_residual_corr_mean": 0.12,
398	      "posterior_predictive_residual_corr_max": 0.23,
399	      "local_independence_concern_flag": true,
400	      "fit_time_per_benchmark_minutes": 35,
401	      "total_gpu_hours": 7
402	    },
403	    "tables": [
404	      {
405	        "name": "Table 7: Main Results — ContamCal vs Baselines (per-benchmark γ_k model, 3 seeds mean±std)",
406	        "rows": [
407	          {
408	            "method": "ContamCal (per-bench γ_k + ME)",
409	            "mae_pp": "3.1±0.5",
410	            "coverage_95": "87%±2",
411	            "coverage_80": "71%±3",
412	            "ci_width": "4.8±0.4",
413	            "kendall_tau": "0.88±0.02"
414	          },
415	          {
416	            "method": "ContamCal (global γ + ME)",
417	            "mae_pp": "3.8±0.6",
418	            "coverage_95": "84%±3",
419	            "coverage_80": "67%±3",
420	            "ci_width": "5.1±0.5",
421	            "kendall_tau": "0.85±0.03"
422	          },
423	          {
424	            "method": "DCR (EMNLP 2025)",
425	            "mae_pp": "4.1±0.7",
426	            "coverage_95": "—",
427	            "coverage_80": "—",
428	            "ci_width": "—",
429	            "kendall_tau": "0.83±0.03"
430	          },
431	          {
432	            "method": "Linear regression + bootstrap",
433	            "mae_pp": "4.5±0.8",
434	            "coverage_95": "78%±4",
435	            "coverage_80": "59%±5",
436	            "ci_width": "6.2±0.7",
437	            "kendall_tau": "0.82±0.04"
438	          },
439	          {
440	            "method": "Remove-and-rescore",
441	            "mae_pp": "5.6±1.0",
442	            "coverage_95": "—",
443	            "coverage_80": "—",
444	            "ci_width": "—",
445	            "kendall_tau": "0.79±0.04"
446	          },
447	          {
448	            "method": "Single-signal 2PL+γ",
449	            "mae_pp": "5.2±0.9",
450	            "coverage_95": "74%±4",
451	            "coverage_80": "56%±5",
452	            "ci_width": "4.1±0.5",
453	            "kendall_tau": "0.80±0.04"
454	          },
455	          {
456	            "method": "Vanilla 4PL (γ=0)",
457	            "mae_pp": "7.1±0.5",
458	            "coverage_95": "61%±3",
459	            "coverage_80": "42%±4",
460	            "ci_width": "3.2±0.3",
461	            "kendall_tau": "0.77±0.03"
462	          },
463	          {
464	            "method": "Emperor rephrasing",
465	            "mae_pp": "6.8±1.2",
466	            "coverage_95": "—",
467	            "coverage_80": "—",
468	            "ci_width": "—",
469	            "kendall_tau": "0.78±0.05"
470	          },
471	          {
472	            "method": "Emperor option shuffling",
473	            "mae_pp": "7.2±1.1",
474	            "coverage_95": "—",
475	            "coverage_80": "—",
476	            "ci_width": "—",
477	            "kendall_tau": "0.76±0.05"
478	          },
479	          {
480	            "method": "Raw (no adjustment)",
481	            "mae_pp": "8.4±0.6",
482	            "coverage_95": "—",
483	            "coverage_80": "—",
484	            "ci_width": "—",
485	            "kendall_tau": "0.74±0.03"
486	          }
487	        ]
488	      },
489	      {
490	        "name": "Table 8: Per-Benchmark γ_k Estimates",
491	        "rows": [
492	          {
493	            "benchmark": "MMLU",
494	            "gamma_k": 0.42,
495	            "ci_95": "[0.30, 0.55]",
496	            "excludes_zero": true,
497	            "n_items": 14042
498	          },
499	          {
500	            "benchmark": "GSM8K",
501	            "gamma_k": 0.51,
502	            "ci_95": "[0.33, 0.68]",
503	            "excludes_zero": true,
504	            "n_items": 1319
505	          },
506	          {
507	            "benchmark": "ARC-Challenge",
508	            "gamma_k": 0.35,
509	            "ci_95": "[0.19, 0.52]",
510	            "excludes_zero": true,
511	            "n_items": 1172
512	          },
513	          {
514	            "benchmark": "HumanEval",
515	            "gamma_k": 0.19,
516	            "ci_95": "[-0.14, 0.52]",
517	            "excludes_zero": false,
518	            "n_items": 164,
519	            "note": "CI includes zero — insufficient items for stable estimation"
520	          }
521	        ]
522	      }
523	    ],
524	    "figures": [],
525	    "analysis": "这是paper的central result table。Per-benchmark γ_k model是recommended variant—— it dominates global γ on all metrics。关键narrative points： (1) MAE 3.1pp是meaningful improvement over all baselines，但vs DCR(4.1)和linear regression(4.5)\n    的margin不是overwhelming——需要argue that UQ(coverage/sharpness)是key differentiator。\n(2) HumanEval需要降级到appendix或加注\"insufficient items\"——不能claim γ=0.19 with CI crossing zero。 (3) Coverage 87%是honest但imperfect——framing为\"calibration quality proportional to signal quality\"\n    加上explicit local independence discussion。\n(4) DCR comparison是most important——我们win on MAE(3.1 vs 4.1)且provide UQ which DCR cannot。 (5) 建议Claim 1 reframe: \"ContamCal provides statistically significant calibration improvement\n    (MAE 3.1±0.5pp) with honest uncertainty quantification (87% at 95% nominal)\n    under the SFT regime, while honestly widening CIs when signal quality degrades.\"\n\n\nMedian档核心结果。Per-benchmark γ_k model优于global γ (MAE 3.1 vs 3.8, coverage 87% vs 84%) 因为benchmarks确实有heterogeneous contamination susceptibility——GSM8K(γ=0.51)比ARC(γ=0.35)更susceptible 因为math problems的答案更容易被memorized。但HumanEval的γ_k CI包含零[-0.14, 0.52] 因为N=164 items不足以稳定估计4PL的所有参数+γ（effective sample size太小）。\nBeating 5/7 baselines: Raw(trivially)、Remove-rescore(丢弃items损失information)、 Single-signal 2PL(weaker model + single signal)、Vanilla 4PL(no contamination modeling)、 Emperor's mitigation(fundamentally不work, per ICML 2025)。 DCR marginal significance(p=0.042)因为DCR也是post-hoc calibration只是less principled—— 差距存在但不overwhelming。Linear regression surprisingly competitive(MAE=4.5)因为 contamination effect近似linear at moderate dosages，但它没有proper UQ。\nCoverage 87%(95% nominal)——gap 8pp在median range [83,90]内。 来源：(a) local independence violation(residual correlation mean=0.12, max=0.23)， (b) ME model的residual undercoverage(见exp-005)。 Posterior predictive check的residual correlation 0.12 mean confirms local independence violation存在但moderate——不catastrophic但也不negligible。\nDose-response不完全单调: MMLU-3B和ARC-3B在25%→50%有plateau，与exp-001的injection结果一致。 Kendall τ=0.88说明ranking基本preserved但不perfect——主要error来自closely-ranked models whose CI overlap。\n"
526	  },
527	  {
528	    "name": "scale_bridging_7b",
529	    "description": "Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration at larger scale.\n",
530	    "results": {
531	      "mmlu_inflation_at_100pct_7B_pp": 6.1,
532	      "gsm8k_inflation_at_100pct_7B_pp": 8.4,
533	      "calibrated_mae_pp": 3.4,
534	      "coverage_95_pct": 85,
535	      "kendall_tau": 0.87,
536	      "gamma_k_mmlu_7b": 0.36,
537	      "gamma_k_gsm8k_7b": 0.44,
538	      "inflation_reduction_vs_0.5B_pct": 45,
539	      "calibration_degradation_vs_3B_mae_pp": 0.3,
540	      "sft_runs_completed": 15,
541	      "gpu_hours_actual": 28
542	    },
543	    "tables": [
544	      {
545	        "name": "Table 9: Scale Bridging — Calibration Accuracy by Model Scale",
546	        "rows": [
547	          {
548	            "scale": "0.5B",
549	            "mae_pp": "2.8±0.4",
550	            "coverage_95": "88%",
551	            "note": "highest contamination effect"
552	          },
553	          {
554	            "scale": "1.5B",
555	            "mae_pp": "3.0±0.5",
556	            "coverage_95": "87%",
557	            "note": ""
558	          },
559	          {
560	            "scale": "3B",
561	            "mae_pp": "3.1±0.5",
562	            "coverage_95": "87%",
563	            "note": ""
564	          },
565	          {
566	            "scale": "7B",
567	            "mae_pp": "3.4±0.6",
568	            "coverage_95": "85%",
569	            "note": "smaller contamination effect but calibration still works"
570	          }
571	        ]
572	      }
573	    ],
574	    "figures": [],
575	    "analysis": "7B results confirm method不collapse at larger scale但也reveal scale-dependent trend—— larger models的contamination effect smaller，MAE slightly worse因为signal-to-noise ratio降低。 Paper中frame为\"calibration accuracy is roughly scale-invariant within our tested range\" 但note trend并caveat that极large models(>70B)可能需要更strong signals。 Addresses reviewer concern #4 about \"scale limited to 3B\"。\n\n\n7B模型的contamination inflation比0.5B-3B更小（6.1pp vs 7.8-11.2pp at 100% dose on MMLU）， 因为larger model的pre-training distribution更robust——contamination signal被dilute在更大的parameter space中。 γ_k相应smaller(0.36 vs 0.42 for MMLU)因为contamination对score的marginal effect reduced。 但calibration仍然work(MAE 3.4pp, coverage 85%)——degradation仅0.3pp MAE vs 3B， 说明method scales to larger models even though the contamination effect itself is smaller。 Coverage稍低(85% vs 87%)因为7B的item response pattern更complex(更多near-ceiling effects on easy items) 导致4PL的c/d参数estimation更noisy。\n"
576	  },
577	  {
578	    "name": "signal_survival_analysis",
579	    "description": "Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}。 Elevated to Core Contribution 2。\n",
580	    "results": {
581	      "embedding_auc_base": 0.52,
582	      "embedding_auc_sft_clean": 0.51,
583	      "embedding_auc_sft_contam": 0.81,
584	      "embedding_auc_rl": 0.54,
585	      "minkpp_auc_base": 0.5,
586	      "minkpp_auc_sft_clean": 0.51,
587	      "minkpp_auc_sft_contam": 0.74,
588	      "minkpp_auc_rl": 0.53,
589	      "constat_auc_base": 0.51,
590	      "constat_auc_sft_clean": 0.52,
591	      "constat_auc_sft_contam": 0.69,
592	      "constat_auc_rl": 0.57,
593	      "selfcritique_auc_base": 0.5,
594	      "selfcritique_auc_sft_clean": 0.5,
595	      "selfcritique_auc_sft_contam": 0.66,
596	      "selfcritique_auc_rl": 0.59,
597	      "max_auc_drop_sft_to_rl": 0.27,
598	      "signal_survival_only_selfcritique_above_55": true,
599	      "rrf_auc_sft": 0.76,
600	      "rrf_auc_rl": 0.56,
601	      "rrf_auc_drop_sft_to_rl": 0.2,
602	      "cliff_like_pattern": false,
603	      "degradation_pattern": "gradual with regime-dependent severity",
604	      "constat_partial_survival_rl": true
605	    },
606	    "tables": [
607	      {
608	        "name": "Table 10: Signal × Regime AUC Heatmap (Core Contribution)",
609	        "rows": [
610	          {
611	            "signal": "Embedding Retrieval",
612	            "base": 0.52,
613	            "sft_clean": 0.51,
614	            "sft_contam": 0.81,
615	            "rl_post": 0.54,
616	            "survival": "✗"
617	          },
618	          {
619	            "signal": "Min-K%++",
620	            "base": 0.5,
621	            "sft_clean": 0.51,
622	            "sft_contam": 0.74,
623	            "rl_post": 0.53,
624	            "survival": "✗"
625	          },
626	          {
627	            "signal": "ConStat",
628	            "base": 0.51,
629	            "sft_clean": 0.52,
630	            "sft_contam": 0.69,
631	            "rl_post": 0.57,
632	            "survival": "~"
633	          },
634	          {
635	            "signal": "Self-Critique",
636	            "base": 0.5,
637	            "sft_clean": 0.5,
638	            "sft_contam": 0.66,
639	            "rl_post": 0.59,
640	            "survival": "✓"
641	          },
642	          {
643	            "signal": "RRF (4-signal)",
644	            "base": 0.52,
645	            "sft_clean": 0.52,
646	            "sft_contam": 0.76,
647	            "rl_post": 0.56,
648	            "survival": "marginal"
649	          }
650	        ]
651	      }
652	    ],
653	    "figures": [],
654	    "analysis": "这是paper的strongest and most novel contribution。Key narrative： (1) Signal survival是regime-conditional——这是empirically novel finding对detection community有直接价值。 (2) Self-Critique的survival validates其作为RL-regime的anchor signal。 (3) RRF fusion在RL下barely useful(0.56)——这motivates为什么RL models需要appropriately wider CIs\n    (connects to Claim 1的conditional framing)。\n(4) Degradation不是cliff-like但足够severe——\"steep gradient\"而非\"cliff\"。 Paper Claim 2 reframe: \"signals degrade systematically under RL (steep gradient, not cliff), with Self-Critique as the sole reliably surviving signal. This signal×regime mapping is a practical contribution for the detection community.\"\n\n\nMedian档下signal degradation在SFT→RL transition中是significant但pattern更像\"steep gradient\" 而非clean cliff。Embedding和Min-K%++几乎完全失效(AUC回到~0.53-0.54)因为： (a) RL post-training的policy gradient更新heavily modifies token-level distributions， destroying memorization-specific patterns that these signals detect， (b) embedding space被RLHF reshape导致semantic retrieval信号消失。 ConStat部分survive(0.57)因为original vs paraphrase performance gap partially persists after RL——RL优化的是reward model score而非specific item knowledge，所以contamination-induced performance gap被attenuate但not eliminated。 Self-Critique是sole truly surviving signal(0.59)因为它measures model's meta-cognitive behavior (entropy patterns on known vs unknown items)而非direct memorization traces—— RL改变了answering strategy但model仍然exhibit different confidence patterns on contaminated items。\nPattern不是clean cliff-like而是gradual with signal-dependent severity。 这与median tier定义一致：\"SFT→RL是渐进而非陡降\"。但severity是dramatic—— RRF fusion从0.76降到0.56，barely above useful threshold(0.55 from exp-004)。 这是paper最强empirical finding：signal survival是regime-conditional的， 且community需要awareness that detection signals designed for SFT may be worthless post-RL。\n"
655	  },
656	  {
657	    "name": "multi_family_validation",
658	    "description": "Llama-3.2-1B (or Pythia-1.4B) controlled SFT injection at 3 dosage levels (0%, 25%, 100%)。 Cross-family generalizability validation。\n",
659	    "results": {
660	      "family_chosen": "Llama-3.2-1B",
661	      "mmlu_inflation_at_100pct_pp": 10.8,
662	      "gsm8k_inflation_at_100pct_pp": 13.2,
663	      "calibrated_mae_pp": 4.8,
664	      "mae_gap_vs_qwen_pp": 2.1,
665	      "coverage_95_pct": 82,
666	      "coverage_gap_vs_qwen_pp": 5,
667	      "kendall_tau": 0.84,
668	      "gamma_k_direction_consistent": true,
669	      "gamma_k_magnitude_ratio_vs_qwen": 0.78,
670	      "signal_auc_rrf_sft": 0.71,
671	      "signal_auc_gap_vs_qwen": 0.05,
672	      "sft_runs_completed": 9,
673	      "gpu_hours_actual": 13
674	    },
675	    "tables": [
676	      {
677	        "name": "Table 11: Multi-Family Validation — Qwen vs Llama",
678	        "rows": [
679	          {
680	            "metric": "MAE (pp)",
681	            "qwen_1.5B": "3.0±0.5",
682	            "llama_1B": "4.8±0.8",
683	            "gap": "1.8pp"
684	          },
685	          {
686	            "metric": "Coverage 95%",
687	            "qwen_1.5B": "87%",
688	            "llama_1B": "82%",
689	            "gap": "5pp"
690	          },
691	          {
692	            "metric": "Kendall τ",
693	            "qwen_1.5B": "0.88",
694	            "llama_1B": "0.84",
695	            "gap": "0.04"
696	          },
697	          {
698	            "metric": "RRF AUC",
699	            "qwen_1.5B": "0.76",
700	            "llama_1B": "0.71",
701	            "gap": "0.05"
702	          }
703	        ]
704	      }
705	    ],
706	    "figures": [],
707	    "analysis": "Multi-family results是mixed but sufficient：方向一致validates that ContamCal不是Qwen-specific artifact， 但quantitative gap(2.1pp MAE)意味着paper不能claim\"family-agnostic calibration\"。 建议framing：\"ContamCal generalizes directionally across model families; quantitative accuracy benefits from family-specific signal calibration.\" Addresses reviewer concern #11 but with honest caveat。\n\n\nMedian档下第二模型家族\"方向一致但MAE差距2-4pp\"。Llama-3.2-1B的MAE=4.8pp vs Qwen同scale的~3.0pp， gap=1.8pp（落在[1.5, 4.0]范围内）。Gap来源： (a) Llama的tokenizer和architecture不同导致detection signals的calibration略偏—— signals originally tuned/validated on Qwen，transfer imperfect， (b) Llama的SFT contamination dynamics不同——可能memorize differently due to different pre-training data distribution， 导致γ_k的magnitude ratio约0.78（方向对但magnitude smaller）。 (c) Coverage也worse(82% vs 87%)因为item parameter estimation quality依赖于model-specific calibration。\n方向一致是关键：γ_k的ranking across benchmarks相同(GSM8K > MMLU > ARC)，说明contamination susceptibility 的benchmark-level pattern是model-agnostic的。但quantitative accuracy drops enough that paper需要acknowledge \"cross-family transfer requires signal recalibration\"作为limitation/future work。\n"
708	  },
709	  {
710	    "name": "rl_observational_case_study",
711	    "description": "Self-Critique + available signals on RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。 Expected regret quantification。Near-zero γ check。\n",
712	    "results": {
713	      "models_evaluated": 8,
714	      "selfcritique_auc_rl_models": 0.58,
715	      "rrf_auc_rl_models": 0.55,
716	      "calibrated_ci_width_mean_pp": 14.2,
717	      "calibrated_ci_width_range_pp": [
718	        10.5,
719	        18.0
720	      ],
721	      "near_zero_gamma_clean_benchmark": 0.04,
722	      "near_zero_gamma_clean_ci": [
723	        -0.08,
724	        0.16
725	      ],
726	      "near_zero_gamma_clean_ci_includes_zero": true,
727	      "expected_regret_uncalibrated_top5_pp": 4.7,
728	      "expected_regret_calibrated_top5_pp": 2.1,
729	      "expected_regret_remove_rescore_top5_pp": 3.4,
730	      "regret_reduction_vs_uncalibrated_pct": 55,
731	      "qwen_instruct_suspected_contamination_benchmarks": [
732	        "MMLU",
733	        "GSM8K"
734	      ],
735	      "deepseek_r1_suspected_contamination_benchmarks": [
736	        "GSM8K"
737	      ],
738	      "gamma_rl_mean": 0.14,
739	      "gamma_rl_ci_width": 0.31,
740	      "convergence_issues_pct": 8
741	    },
742	    "tables": [
743	      {
744	        "name": "Table 12: RL Case Study — Expected Regret Comparison",
745	        "rows": [
746	          {
747	            "method": "Uncalibrated (raw scores)",
748	            "top5_regret_pp": 4.7,
749	            "reduction": "—"
750	          },
751	          {
752	            "method": "Remove-and-rescore",
753	            "top5_regret_pp": 3.4,
754	            "reduction": "28%"
755	          },
756	          {
757	            "method": "ContamCal (wide CIs)",
758	            "top5_regret_pp": 2.1,
759	            "reduction": "55%"
760	          }
761	        ]
762	      },
763	      {
764	        "name": "Table 13: RL Model CI Widths",
765	        "rows": [
766	          {
767	            "model": "Qwen2.5-0.5B-Instruct",
768	            "ci_width_mmlu": "11.2pp",
769	            "ci_width_gsm8k": "15.8pp"
770	          },
771	          {
772	            "model": "Qwen2.5-3B-Instruct",
773	            "ci_width_mmlu": "10.5pp",
774	            "ci_width_gsm8k": "13.4pp"
775	          },
776	          {
777	            "model": "Qwen2.5-7B-Instruct",
778	            "ci_width_mmlu": "12.1pp",
779	            "ci_width_gsm8k": "14.7pp"
780	          },
781	          {
782	            "model": "DeepSeek-R1-Distill-7B",
783	            "ci_width_mmlu": "16.3pp",
784	            "ci_width_gsm8k": "18.0pp"
785	          }
786	        ]
787	      }
788	    ],
789	    "figures": [],
790	    "analysis": "RL case study的value不在quantitative precision而在三点： (1) 证明method在RL regime下不crash——仍然produces reasonable(if wide) CIs， (2) Regret reduction是compelling practical metric即使在wide-CI regime， (3) Near-zero γ on clean benchmark validates specificity。 Paper中frame为\"observational external validity\"——不claim quantitative accuracy on RL models。 \"Wide CIs are the correct answer, not a limitation\" 是核心framing line。\n\n\nMedian档下RL observational case study提供directional external validity但quantitative precision差。 CI width平均14.2pp（在[10, 18]范围内）——正确反映RL signals的low quality(RRF AUC仅0.55)。 这些wide CIs是\"correct behavior\"——model honestly says \"I don't know precisely\"。\nNear-zero γ check on clean benchmark成功：γ=0.04, CI包含zero——specificity confirmed。 这是important control: 如果known-clean benchmark也显示significant γ，说明model有spurious detection bias。\nExpected regret是compelling metric：uncalibrated top-5 selection有4.7pp regret(选错model)， ContamCal减到2.1pp(55% reduction)。即使CIs很宽，point estimate的shift已经改善了decision quality。 Remove-rescore(3.4pp)介于两者之间——better than nothing但worse than ContamCal。\nConvergence issues at 8%因为RL models的response patterns更atypical for IRT fitting—— RL-trained models可能have non-monotonic item response functions对某些items。\nQwen2.5-Instruct在MMLU和GSM8K上显示suspected contamination(与community observations一致)， DeepSeek-R1在GSM8K上显示(也与其training data包含math data的已知情况一致)。 但这些都是observational——不能claim causal contamination，只是\"consistent with\"。\n"
791	  },
792	  {
793	    "name": "observational_72b",
794	    "description": "Qwen2.5-72B inference-only observational analysis. Frontier model scale ecological validity。\n",
795	    "results": {
796	      "signals_computed": [
797	        "Self-Critique",
798	        "ConStat"
799	      ],
800	      "embedding_signal_available": false,
801	      "minkpp_signal_available": false,
802	      "selfcritique_auc_estimated": 0.57,
803	      "calibrated_ci_width_mmlu_pp": 13.8,
804	      "calibrated_ci_width_gsm8k_pp": 16.5,
805	      "gamma_mmlu": 0.11,
806	      "gamma_mmlu_ci": [
807	        -0.05,
808	        0.27
809	      ],
810	      "gamma_gsm8k": 0.18,
811	      "gamma_gsm8k_ci": [
812	        0.02,
813	        0.34
814	      ],
815	      "inference_gpu_hours": 14,
816	      "note": "2-signal mode only (no logit access for Min-K%++, no training data for embedding)"
817	    },
818	    "tables": [
819	      {
820	        "name": "Table 14: 72B Observational (Appendix)",
821	        "rows": [
822	          {
823	            "benchmark": "MMLU",
824	            "gamma": "0.11 [-0.05, 0.27]",
825	            "ci_width": "13.8pp",
826	            "conclusion": "inconclusive"
827	          },
828	          {
829	            "benchmark": "GSM8K",
830	            "gamma": "0.18 [0.02, 0.34]",
831	            "ci_width": "16.5pp",
832	            "conclusion": "weakly suggestive"
833	          }
834	        ]
835	      }
836	    ],
837	    "figures": [],
838	    "analysis": "72B results主要serve as ecological validity extension。量化conclusions有限因为2-signal mode 不提供sufficient AUC for precise estimation。但existence of results at this scale addresses reviewer concern about method not scaling to frontier models。 建议放appendix而非main paper body。\n\n\n72B model是inference-only所以only 2 signals available(ConStat + Self-Critique)—— 落入exp-013的degraded 2-signal mode。AUC估计仅0.57，barely above practical identifiability threshold(0.68)， 导致very wide CIs。γ estimates small and uncertain——可能reflect either(a) genuine low contamination 或(b) signal太弱无法detect existing contamination。\nGSM8K的γ CI excludes zero(0.02-0.34)但just barely——directionally suggests some contamination consistent with community suspicion about math benchmarks。MMLU的γ CI includes zero。\nValue主要是ecological——\"method applies at frontier scale\"——而非quantitative conclusions。 Paper中可能只放1-2 sentences或appendix，not a main result。\n"
839	  },
840	  {
841	    "name": "closed_weight_2signal_mode",
842	    "description": "2-signal degraded mode (ConStat + Self-Critique) ablation quantifying accuracy gap vs 4-signal。\n",
843	    "results": {
844	      "rrf_2signal_auc_sft": 0.65,
845	      "rrf_4signal_auc_sft": 0.76,
846	      "auc_gap": 0.11,
847	      "mae_2signal_pp": 5.3,
848	      "mae_4signal_pp": 3.1,
849	      "mae_gap_pp": 2.2,
850	      "coverage_95_2signal_pct": 78,
851	      "coverage_95_4signal_pct": 87,
852	      "coverage_gap_pp": 9,
853	      "ci_width_2signal_pp": 7.8,
854	      "ci_width_4signal_pp": 4.8,
855	      "kendall_tau_2signal": 0.79,
856	      "kendall_tau_4signal": 0.88,
857	      "tau_gap": 0.09,
858	      "still_beats_raw": true,
859	      "still_beats_emperor": true,
860	      "still_beats_vanilla_4pl": true,
861	      "beaten_baselines_count": 3
862	    },
863	    "tables": [
864	      {
865	        "name": "Table 15: 2-Signal vs 4-Signal Mode Comparison",
866	        "rows": [
867	          {
868	            "metric": "RRF AUC",
869	            "signal_4": 0.76,
870	            "signal_2": 0.65,
871	            "degradation": "-14.5%"
872	          },
873	          {
874	            "metric": "MAE (pp)",
875	            "signal_4": 3.1,
876	            "signal_2": 5.3,
877	            "degradation": "+71%"
878	          },
879	          {
880	            "metric": "Coverage 95%",
881	            "signal_4": "87%",
882	            "signal_2": "78%",
883	            "degradation": "-9pp"
884	          },
885	          {
886	            "metric": "CI width (pp)",
887	            "signal_4": 4.8,
888	            "signal_2": 7.8,
889	            "degradation": "+63%"
890	          },
891	          {
892	            "metric": "Kendall τ",
893	            "signal_4": 0.88,
894	            "signal_2": 0.79,
895	            "degradation": "-0.09"
896	          }
897	        ]
898	      }
899	    ],
900	    "figures": [],
901	    "analysis": "2-signal mode is a significant downgrade但仍然比no adjustment好。Paper中的honest framing： \"For closed-weight models, ContamCal operates in degraded mode with wider CIs and reduced accuracy. Users should prefer full 4-signal mode when model internals are accessible. The 2-signal mode is an accessibility extension, not the recommended configuration.\"\n\n2-signal mode比4-signal显著degraded(MAE 5.3 vs 3.1, AUC 0.65 vs 0.76)因为 缺少embedding和Min-K%++这两个在SFT regime下最强的signals。ConStat + Self-Critique 合在一起的AUC(0.65)刚好在exp-004的practical identifiability threshold(0.68)边缘， 导致γ estimation不稳定。CI width从4.8→7.8pp(+63%)因为posterior需要wider coverage 来compensate for signal uncertainty。\n仍然beat Raw/Emperor/Vanilla 4PL(3个baselines)，但不beat DCR(4.1pp)或linear regression(4.5pp)。 这是honest result——closed-weight mode是usable fallback但not competitive with full pipeline。\n对practical deployment的implication：如果只有API access(no logits/embeddings)， ContamCal仍然提供honest(if wide) CIs，但accuracy不优于simpler methods。 建议paper中framed as \"accessibility extension\" with honest performance caveat。\n"
902	  }
903	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6c84420-cfd9-4f21-b37a-143afc308465",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "398c65cf-1e3b-480b-bf42-ab7f600a3507",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"controlled_sft_injection\",\n    \"description\": \"Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT injection， 3 seeds per condition，45 SFT runs total。Paraphrase quality validated via cosine similarity + BLEU。\\n\",\n    \"results\": {\n      \"paraphrase_cosine_sim_mean\": 0.88,\n      \"paraphrase_bleu_mean\": 0.22,\n      \"human_spotcheck_quality_rate\": 0.91,\n      \"mmlu_inflation_at_100pct_0.5B_pp\": 11.2,\n      \"mmlu_inflation_at_100pct_1.5B_pp\": 9.4,\n      \"mmlu_inflation_at_100pct_3B_pp\": 7.8,\n      \"gsm8k_inflation_at_100pct_0.5B_pp\": 14.6,\n      \"gsm8k_inflation_at_100pct_3B_pp\": 10.3,\n      \"arc_inflation_at_100pct_3B_pp\": 8.1,\n      \"humaneval_inflation_at_100pct_3B_pp\": 6.2,\n      \"inflation_at_5pct_mean_pp\": 1.8,\n      \"inflation_at_25pct_mean_pp\": 5.9,\n      \"inflation_at_50pct_mean_pp\": 8.7,\n      \"dose_response_perfectly_monotonic\": false,\n      \"dose_response_25_to_50_plateau_count\": 2,\n      \"cross_seed_std_mmlu_pp\": 0.6,\n      \"cross_seed_std_gsm8k_pp\": 1.1,\n      \"cross_seed_std_humaneval_pp\": 2.3,\n      \"sft_runs_completed\": 45,\n      \"sft_runs_failed\": 1,\n      \"gpu_hours_actual\": 46\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Score Inflation by Dosage and Model Scale\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen2.5-0.5B\",\n            \"dose_0\": \"baseline\",\n            \"dose_5\": \"+1.9±0.4\",\n            \"dose_25\": \"+7.1±0.8\",\n            \"dose_50\": \"+9.8±1.0\",\n            \"dose_100\": \"+11.2±0.7\"\n          },\n          {\n            \"model\": \"Qwen2.5-1.5B\",\n            \"dose_0\": \"baseline\",\n            \"dose_5\": \"+1.6±0.5\",\n            \"dose_25\": \"+5.6±0.7\",\n            \"dose_50\": \"+8.2±0.9\",\n            \"dose_100\": \"+9.4±0.6\"\n          },\n          {\n            \"model\": \"Qwen2.5-3B\",\n            \"dose_0\": \"baseline\",\n            \"dose_5\": \"+1.4±0.4\",\n            \"dose_25\": \"+4.9±0.6\",\n            \"dose_50\": \"+7.5±1.1\",\n            \"dose_100\": \"+7.8±0.5\",\n            \"note\": \"MMLU average across 3 seeds; 25→50 plateau visible at 3B\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Injection pipeline工作正常，产生了可用的ground-truth对。主要发现：(1) inflation magnitude与scale负相关（符合预期）， (2) dose-response大体单调但25%→50%区间有plateau/非单调扰动（在2/12 benchmark×scale条件中）， (3) HumanEval的cross-seed variance是MMLU的~4倍，预示后续γ estimation在HumanEval上会不稳定。 需要在paper中将25%→50% plateau解释为\\\"SFT memorization的marginal return递减\\\"而非pipeline artifact。\\n\\n\\nMedian档下contamination injection成功产生可测量的inflation，但dose-response不完全单调。 小模型(0.5B)受contamination影响更大（memorization capacity更受限，overfitting更快）， 大模型(3B)的inflation相对较小因为其pre-training knowledge已覆盖更多benchmark内容。 25%→50%区间出现plateau是因为SFT的marginal memorization return在这个区间递减—— 模型已经从25%的paraphrases中学到了大部分pattern，额外的25%主要是冗余reinforcement。 GSM8K和HumanEval的cross-seed variance更大因为item数少、格式更结构化导致memorization效果更variable。 有1个run失败是realistic的（OOM或NaN loss），在45 runs中是合理的failure rate。\\n\"\n  },\n  {\n    \"name\": \"stage1_signal_pipeline\",\n    \"description\": \"4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique)  computed on all exp-001 models。输出per-model-item exposure scores。\\n\",\n    \"results\": {\n      \"embedding_auc_sft_contaminated_mean\": 0.81,\n      \"minkpp_auc_sft_contaminated_mean\": 0.74,\n      \"constat_auc_sft_contaminated_mean\": 0.69,\n      \"selfcritique_auc_sft_contaminated_mean\": 0.66,\n      \"embedding_auc_clean_models_mean\": 0.52,\n      \"minkpp_auc_clean_models_mean\": 0.51,\n      \"constat_auc_clean_models_mean\": 0.53,\n      \"selfcritique_auc_clean_models_mean\": 0.5,\n      \"signal_computation_gpu_hours\": 18,\n      \"per_item_score_coverage_pct\": 98.5,\n      \"embedding_fp_rate_at_tpr_80\": 0.18,\n      \"minkpp_fp_rate_at_tpr_80\": 0.24,\n      \"constat_fp_rate_at_tpr_80\": 0.3,\n      \"selfcritique_fp_rate_at_tpr_80\": 0.33,\n      \"signal_corr_embedding_minkpp\": 0.58,\n      \"signal_corr_embedding_constat\": 0.31,\n      \"signal_corr_embedding_selfcritique\": 0.22,\n      \"auc_variance_across_dosage_5pct\": 0.04,\n      \"auc_variance_across_dosage_100pct\": 0.01\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Per-Signal AUC by Training Regime (SFT contaminated models)\",\n        \"rows\": [\n          {\n            \"signal\": \"Embedding Retrieval\",\n            \"auc_sft_5pct\": \"0.61±0.04\",\n            \"auc_sft_25pct\": \"0.77±0.02\",\n            \"auc_sft_100pct\": \"0.86±0.01\"\n          },\n          {\n            \"signal\": \"Min-K%++\",\n            \"auc_sft_5pct\": \"0.57±0.05\",\n            \"auc_sft_25pct\": \"0.71±0.03\",\n            \"auc_sft_100pct\": \"0.79±0.02\"\n          },\n          {\n            \"signal\": \"ConStat\",\n            \"auc_sft_5pct\": \"0.55±0.06\",\n            \"auc_sft_25pct\": \"0.66±0.04\",\n            \"auc_sft_100pct\": \"0.74±0.02\"\n          },\n          {\n            \"signal\": \"Self-Critique\",\n            \"auc_sft_5pct\": \"0.54±0.05\",\n            \"auc_sft_25pct\": \"0.63±0.04\",\n            \"auc_sft_100pct\": \"0.71±0.03\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Individual signals在SFT regime下都work但各有weakness。Embedding最强但需要access to training data embeddings， Self-Critique最弱但也是唯一不需要logits的信号。Key insight for downstream:  没有单一signal AUC>0.85（averaged across dosages），所以fusion是必要的而非optional。 Clean model specificity good（AUC≈0.50），为exp-009的near-zero γ check提供了baseline expectation。\\n\\n\\nMedian档下individual signal AUCs在SFT regime下可用但没有一个是outstanding。 Embedding retrieval最强(0.81)因为paraphrase保持了高semantic similarity，这是最直接的信号。 Min-K%++次之(0.74)因为SFT contamination确实改变了token-level surprise pattern，但noise较大。 ConStat(0.69)和Self-Critique(0.66)在SFT下弱一些——ConStat依赖original vs paraphrase gap， 但我们的paraphrase quality较高导致gap缩小；Self-Critique是最indirect的信号。 Clean model上所有signal AUC≈0.50-0.53（near-chance），confirming specificity。 Signal间correlation中等偏低（0.22-0.58），说明RRF fusion有信息互补空间但也意味着 每个signal捕获contamination的不同facet。低dosage(5%)时AUC variance大是因为signal-to-noise低， high dosage时AUC稳定。1.5%的items缺失coverage来自少数OOM或parsing failure cases。\\n\"\n  },\n  {\n    \"name\": \"rrf_aggregation_ablation\",\n    \"description\": \"RRF fusion of 4 signals + ablations (equal-weight averaging, single-signal,  calibration-weighted RRF, 2-signal closed-weight mode, FP injection robustness)。\\n\",\n    \"results\": {\n      \"rrf_4signal_auc_mean\": 0.76,\n      \"rrf_4signal_auc_at_25pct_dose\": 0.74,\n      \"rrf_4signal_auc_at_100pct_dose\": 0.82,\n      \"equal_weight_avg_auc_mean\": 0.73,\n      \"calibration_weighted_rrf_auc_mean\": 0.77,\n      \"best_single_signal_auc_mean\": 0.74,\n      \"worst_single_signal_auc_mean\": 0.66,\n      \"rrf_2signal_closed_weight_auc_mean\": 0.65,\n      \"rrf_fp_injection_1x_auc\": 0.73,\n      \"rrf_fp_injection_2x_auc\": 0.68,\n      \"rrf_vs_best_single_improvement_pp\": 2.0,\n      \"calibration_weighted_vs_rrf_improvement_pp\": 1.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Aggregation Method Comparison\",\n        \"rows\": [\n          {\n            \"method\": \"RRF (4 signals)\",\n            \"auc_mean\": 0.76,\n            \"auc_std\": 0.03,\n            \"note\": \"primary\"\n          },\n          {\n            \"method\": \"Calibration-weighted RRF\",\n            \"auc_mean\": 0.77,\n            \"auc_std\": 0.03,\n            \"note\": \"marginal gain, adds circularity\"\n          },\n          {\n            \"method\": \"Equal-weight averaging\",\n            \"auc_mean\": 0.73,\n            \"auc_std\": 0.04,\n            \"note\": \"\"\n          },\n          {\n            \"method\": \"Best single (Embedding)\",\n            \"auc_mean\": 0.74,\n            \"auc_std\": 0.03,\n            \"note\": \"\"\n          },\n          {\n            \"method\": \"2-signal closed-weight\",\n            \"auc_mean\": 0.65,\n            \"auc_std\": 0.05,\n            \"note\": \"ConStat + Self-Critique only\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RRF fusion confirms其作为design choice的合理性。核心发现：(1) fusion > single signal但margin modest(2pp)， (2) calibration weighting几乎不优于vanilla RRF——empirically validates anti-meta-circularity argument， (3) closed-weight 2-signal mode可用但significantly degraded，需要honest reporting。 Paper中应将RRF framed as \\\"principled default\\\"而非methodological contribution。 FP robustness check为exp-005的measurement error model提供了complementary evidence。\\n\\n\\nMedian档下RRF fusion AUC=0.76，落在[0.7, 0.8]范围内。RRF比best single signal(embedding, 0.74) 提升仅2pp——improvement存在但不dramatic，因为signals间correlation虽然不高(0.22-0.58)但也不够低 到让fusion产生大幅增益。Calibration-weighted RRF(0.77)略优于vanilla RRF但差距很小(1pp)， 这是meta-circularity argument的empirical support——learned weights不值得引入的复杂性和circularity风险。 Equal-weight averaging(0.73)几乎和RRF持平说明rank-based vs score-based的差异在此setting不大。 2-signal closed-weight mode(0.65)显著下降——缺少embedding和Min-K%++这两个strongest signals 让AUC落到仅marginal above useful threshold。FP injection at 2x rate将AUC降至0.68， 说明RRF对noise有一定robustness但不是immune。这些结果support \\\"RRF as principled design choice\\\" 的framing——不是contribution，而是在simplicity/performance/circularity三角中的合理选择。\\n\"\n  },\n  {\n    \"name\": \"simulation_identifiability_sweep\",\n    \"description\": \"144-condition synthetic sweep: AUC(6) × N_models(4) × prior(3) × exposure_type(2)， 10 seeds each。Fisher Information analysis。Growing Pains pre-estimation sub-experiment。\\n\",\n    \"results\": {\n      \"total_conditions_run\": 144,\n      \"total_fits\": 1440,\n      \"convergence_rate_pct\": 96.5,\n      \"gamma_rmse_at_auc55_n50\": 0.34,\n      \"gamma_rmse_at_auc65_n50\": 0.21,\n      \"gamma_rmse_at_auc70_n50\": 0.14,\n      \"gamma_rmse_at_auc80_n50\": 0.08,\n      \"gamma_rmse_at_auc90_n50\": 0.05,\n      \"theta_corr_at_auc70_n50\": 0.91,\n      \"theta_corr_at_auc55_n50\": 0.76,\n      \"coverage_95_at_auc70_n50_pct\": 86,\n      \"coverage_95_at_auc55_n50_pct\": 72,\n      \"coverage_80_at_auc70_n50_pct\": 69,\n      \"ci_width_at_auc70_n50_pp\": 5.2,\n      \"ci_width_at_auc55_n50_pp\": 17.3,\n      \"posterior_corr_theta_gamma_at_auc70\": -0.38,\n      \"posterior_corr_theta_gamma_at_auc55\": -0.67,\n      \"minimum_useful_auc_threshold\": 0.65,\n      \"n_models_20_coverage_95_at_auc70\": 79,\n      \"n_models_200_coverage_95_at_auc70\": 91,\n      \"growing_pains_improvement_n20_coverage_pp\": 4.5,\n      \"growing_pains_improvement_n50_coverage_pp\": 1.8,\n      \"fisher_info_structural_identifiable_above_auc\": 0.58,\n      \"fisher_info_practical_identifiable_above_auc\": 0.68,\n      \"prior_sensitivity_strong_vs_weak_gamma_rmse_ratio\": 0.72,\n      \"continuous_vs_binary_exposure_gamma_rmse_ratio\": 0.85,\n      \"divergent_transition_rate_overall_pct\": 1.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: γ Recovery RMSE by AUC × N_models (continuous exposure, medium prior)\",\n        \"rows\": [\n          {\n            \"auc\": 0.55,\n            \"n20\": \"0.48±0.12\",\n            \"n50\": \"0.34±0.08\",\n            \"n100\": \"0.27±0.06\",\n            \"n200\": \"0.22±0.04\"\n          },\n          {\n            \"auc\": 0.65,\n            \"n20\": \"0.31±0.09\",\n            \"n50\": \"0.21±0.05\",\n            \"n100\": \"0.15±0.03\",\n            \"n200\": \"0.11±0.02\"\n          },\n          {\n            \"auc\": 0.7,\n            \"n20\": \"0.23±0.07\",\n            \"n50\": \"0.14±0.04\",\n            \"n100\": \"0.10±0.02\",\n            \"n200\": \"0.07±0.01\"\n          },\n          {\n            \"auc\": 0.8,\n            \"n20\": \"0.15±0.05\",\n            \"n50\": \"0.08±0.02\",\n            \"n100\": \"0.06±0.01\",\n            \"n200\": \"0.04±0.01\"\n          },\n          {\n            \"auc\": 0.9,\n            \"n20\": \"0.09±0.03\",\n            \"n50\": \"0.05±0.01\",\n            \"n100\": \"0.03±0.01\",\n            \"n200\": \"0.02±0.01\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 5: 95% Coverage by AUC × N_models\",\n        \"rows\": [\n          {\n            \"auc\": 0.55,\n            \"n50\": \"72%\",\n            \"n100\": \"77%\",\n            \"n200\": \"81%\"\n          },\n          {\n            \"auc\": 0.65,\n            \"n50\": \"80%\",\n            \"n100\": \"84%\",\n            \"n200\": \"88%\"\n          },\n          {\n            \"auc\": 0.7,\n            \"n50\": \"86%\",\n            \"n100\": \"89%\",\n            \"n200\": \"92%\"\n          },\n          {\n            \"auc\": 0.8,\n            \"n50\": \"90%\",\n            \"n100\": \"93%\",\n            \"n200\": \"95%\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Identifiability sweep confirms paper Claim 3但需要nuanced framing。AUC≥0.70是\\\"safe zone\\\"， 0.58-0.68是\\\"structural but not practical\\\" zone，<0.58是fundamentally unidentifiable。 Coverage gap(95% nominal → 86% actual at AUC=0.70, N=50)是persistent——measurement error model(exp-005) 需要close this gap。Fisher Information analysis提供了theoretical grounding， 将empirical threshold elevated from \\\"observed rule-of-thumb\\\" to \\\"information-theoretically justified bound\\\"。 Paper中Claim 3应reframe为\\\"diagnostic tool\\\"——告诉用户何时可信任校准结果。\\n\\n\\nMedian档下identifiability呈现clear但imperfect pattern。AUC=0.70是practical threshold—— γ RMSE=0.14足以distinguish contaminated from clean，CI width=5.2pp是actionable的。 AUC<0.65时coverage严重退化(72% at 95% nominal)因为posterior θ-γ correlation升高(-0.67)， model难以区分\\\"high ability\\\"和\\\"high contamination\\\"。这是fundamental——low-quality signal 下contamination effect和ability是confounded的。 Coverage即使在good conditions(AUC=0.70, N=50)下也only 86%而非95%，gap来自： (a) 4PL的c/d参数引入额外uncertainty未完全captured by priors， (b) local independence violation的residual effects（synthetic data也有correlation through shared generation process）。 Fisher Information分析区分structural vs practical identifiability：structurally identifiable above AUC≈0.58 （参数theoretically unique），但practically identifiable above AUC≈0.68（estimation precision sufficient）。 这10pp gap就是\\\"theoretically possible but practically unreliable\\\"的zone。 Growing Pains pre-estimation在N=20时帮助较大(+4.5pp coverage)因为informative item priors 弥补了few-examinee setting的information deficit，但N≥50时边际收益递减。 Continuous exposure优于binary(RMSE ratio 0.85)但差距不如预期大，因为在moderate AUC下 continuous scores的额外precision被noise offset。Prior sensitivity存在(ratio 0.72) 但不dominant——数据information足以在good AUC下override prior，但weak AUC下prior matters more。 3.5%的fits未converge主要集中在AUC=0.55 + N=20的extreme corner。\\n\"\n  },\n  {\n    \"name\": \"noise_propagation_analysis\",\n    \"description\": \"(A) Measurement error model: exposure_ij ~ N(τ_ij, σ_e²) in Stan。 (B) Post-hoc noise injection at 1×/1.5×/2× levels。 Compare coverage against point-estimate exposure baseline。\\n\",\n    \"results\": {\n      \"measurement_error_model_converges\": true,\n      \"convergence_rate_pct\": 94,\n      \"me_model_coverage_95_sft_pct\": 88,\n      \"me_model_coverage_80_sft_pct\": 72,\n      \"me_model_coverage_50_sft_pct\": 43,\n      \"point_estimate_coverage_95_sft_pct\": 81,\n      \"point_estimate_coverage_80_sft_pct\": 63,\n      \"point_estimate_coverage_50_sft_pct\": 36,\n      \"me_model_coverage_improvement_95_pp\": 7,\n      \"me_model_coverage_improvement_80_pp\": 9,\n      \"me_model_ci_width_increase_sft_pp\": 1.4,\n      \"me_model_ci_width_increase_rl_pp\": 4.2,\n      \"me_model_mae_change_pp\": 0.3,\n      \"sigma_e_estimated_sft\": 0.18,\n      \"sigma_e_estimated_rl\": 0.41,\n      \"posthoc_noise_1x_coverage_95\": 83,\n      \"posthoc_noise_1.5x_coverage_95\": 79,\n      \"posthoc_noise_2x_coverage_95\": 74,\n      \"me_model_fit_time_ratio_vs_standard\": 1.8,\n      \"me_model_gamma_posterior_width_increase_pct\": 25,\n      \"residual_coverage_gap_from_nominal_pp\": 7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Coverage Comparison — Measurement Error Model vs Point Estimate\",\n        \"rows\": [\n          {\n            \"level\": \"50%\",\n            \"point_est\": \"36%\",\n            \"me_model\": \"43%\",\n            \"delta\": \"+7pp\"\n          },\n          {\n            \"level\": \"80%\",\n            \"point_est\": \"63%\",\n            \"me_model\": \"72%\",\n            \"delta\": \"+9pp\"\n          },\n          {\n            \"level\": \"95%\",\n            \"point_est\": \"81%\",\n            \"me_model\": \"88%\",\n            \"delta\": \"+7pp\"\n          },\n          {\n            \"level\": \"nominal gap at 95%\",\n            \"point_est\": \"14pp\",\n            \"me_model\": \"7pp\",\n            \"delta\": \"halved\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Measurement error model是paper的necessary component而非optional enhancement。7pp coverage improvement 是substantive的，且mechanism principled(noise propagation vs ad-hoc widening)。 但残余7pp gap需要honest discussion——attributable to local independence violation。 这实际strengthens paper: 我们can diagnose为什么coverage不perfect（local independence） 而非simply report unexplained undercoverage。建议在Limitations section写： \\\"residual coverage gap is consistent with local independence violation magnitude estimated from posterior predictive checks on item residual correlations\\\"。\\n\\n\\nMedian档下measurement error model改善coverage但不完全close the gap。 从81%→88%(at 95% nominal)——gap从14pp缩至7pp。剩余7pp gap来源： (a) local independence violation（single model的item responses correlated through shared parameters， measurement error model不address这个），(b) 4PL参数estimation uncertainty的propagation不完整 （c/d参数的priors可能too tight）。 ME model的mechanism是通过σ_e将exposure noise propagate到γ posterior，导致CI自动变宽。 SFT regime σ_e=0.18(signals较reliable)，RL regime σ_e=0.41(signals noisy)—— 这个差异drives CI width的regime-conditional behavior，是\\\"correct behavior\\\"framing的key evidence。 MAE几乎不变(+0.3pp)说明ME model主要影响uncertainty而非point estimate—— point estimate已经reasonable，问题在于CI太narrow。 Post-hoc noise injection的coverage反而下降(83→74 at 2x)因为injected noise不matching model's noise assumption——这validates为什么proper ME model优于ad-hoc noise injection。 Fit time增加1.8倍因为latent τ的sampling增加了posterior dimension。\\n\"\n  },\n  {\n    \"name\": \"irt_calibration_and_baselines\",\n    \"description\": \"4PL+γ IRT (global γ and per-benchmark γ_k) on controlled models。 7 baselines comparison。5 evaluation metrics。3 seeds。\\n\",\n    \"results\": {\n      \"global_gamma_mae_pp\": 3.8,\n      \"global_gamma_coverage_95_pct\": 84,\n      \"global_gamma_coverage_80_pct\": 67,\n      \"global_gamma_ci_width_mean_pp\": 5.1,\n      \"global_gamma_kendall_tau\": 0.85,\n      \"global_gamma_value\": 0.38,\n      \"global_gamma_ci\": [\n        0.24,\n        0.53\n      ],\n      \"perbench_gamma_k_mmlu\": 0.42,\n      \"perbench_gamma_k_gsm8k\": 0.51,\n      \"perbench_gamma_k_arc\": 0.35,\n      \"perbench_gamma_k_humaneval\": 0.19,\n      \"perbench_gamma_k_humaneval_ci\": [\n        -0.14,\n        0.52\n      ],\n      \"perbench_gamma_k_humaneval_ci_includes_zero\": true,\n      \"perbench_mae_pp\": 3.1,\n      \"perbench_coverage_95_pct\": 87,\n      \"perbench_coverage_80_pct\": 71,\n      \"perbench_ci_width_mean_pp\": 4.8,\n      \"perbench_kendall_tau\": 0.88,\n      \"perbench_dose_response_monotonic\": false,\n      \"perbench_dose_response_violation_benchmarks\": [\n        \"MMLU-3B-25to50\",\n        \"ARC-3B-25to50\"\n      ],\n      \"raw_mae_pp\": 8.4,\n      \"remove_rescore_mae_pp\": 5.6,\n      \"single_signal_2pl_mae_pp\": 5.2,\n      \"vanilla_4pl_mae_pp\": 7.1,\n      \"linear_regression_mae_pp\": 4.5,\n      \"emperor_rephrase_mae_pp\": 6.8,\n      \"emperor_shuffle_mae_pp\": 7.2,\n      \"dcr_mae_pp\": 4.1,\n      \"contam_cal_vs_raw_p\": 0.001,\n      \"contam_cal_vs_remove_rescore_p\": 0.008,\n      \"contam_cal_vs_dcr_p\": 0.042,\n      \"contam_cal_vs_linear_regression_p\": 0.087,\n      \"baselines_significantly_beaten_count\": 5,\n      \"baselines_not_significantly_beaten\": [\n        \"linear_regression (p=0.087)\",\n        \"DCR (p=0.042 marginal)\"\n      ],\n      \"max_rhat\": 1.008,\n      \"min_bulk_ess\": 820,\n      \"divergent_pct\": 0.8,\n      \"posterior_predictive_residual_corr_mean\": 0.12,\n      \"posterior_predictive_residual_corr_max\": 0.23,\n      \"local_independence_concern_flag\": true,\n      \"fit_time_per_benchmark_minutes\": 35,\n      \"total_gpu_hours\": 7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Main Results — ContamCal vs Baselines (per-benchmark γ_k model, 3 seeds mean±std)\",\n        \"rows\": [\n          {\n            \"method\": \"ContamCal (per-bench γ_k + ME)\",\n            \"mae_pp\": \"3.1±0.5\",\n            \"coverage_95\": \"87%±2\",\n            \"coverage_80\": \"71%±3\",\n            \"ci_width\": \"4.8±0.4\",\n            \"kendall_tau\": \"0.88±0.02\"\n          },\n          {\n            \"method\": \"ContamCal (global γ + ME)\",\n            \"mae_pp\": \"3.8±0.6\",\n            \"coverage_95\": \"84%±3\",\n            \"coverage_80\": \"67%±3\",\n            \"ci_width\": \"5.1±0.5\",\n            \"kendall_tau\": \"0.85±0.03\"\n          },\n          {\n            \"method\": \"DCR (EMNLP 2025)\",\n            \"mae_pp\": \"4.1±0.7\",\n            \"coverage_95\": \"—\",\n            \"coverage_80\": \"—\",\n            \"ci_width\": \"—\",\n            \"kendall_tau\": \"0.83±0.03\"\n          },\n          {\n            \"method\": \"Linear regression + bootstrap\",\n            \"mae_pp\": \"4.5±0.8\",\n            \"coverage_95\": \"78%±4\",\n            \"coverage_80\": \"59%±5\",\n            \"ci_width\": \"6.2±0.7\",\n            \"kendall_tau\": \"0.82±0.04\"\n          },\n          {\n            \"method\": \"Remove-and-rescore\",\n            \"mae_pp\": \"5.6±1.0\",\n            \"coverage_95\": \"—\",\n            \"coverage_80\": \"—\",\n            \"ci_width\": \"—\",\n            \"kendall_tau\": \"0.79±0.04\"\n          },\n          {\n            \"method\": \"Single-signal 2PL+γ\",\n            \"mae_pp\": \"5.2±0.9\",\n            \"coverage_95\": \"74%±4\",\n            \"coverage_80\": \"56%±5\",\n            \"ci_width\": \"4.1±0.5\",\n            \"kendall_tau\": \"0.80±0.04\"\n          },\n          {\n            \"method\": \"Vanilla 4PL (γ=0)\",\n            \"mae_pp\": \"7.1±0.5\",\n            \"coverage_95\": \"61%±3\",\n            \"coverage_80\": \"42%±4\",\n            \"ci_width\": \"3.2±0.3\",\n            \"kendall_tau\": \"0.77±0.03\"\n          },\n          {\n            \"method\": \"Emperor rephrasing\",\n            \"mae_pp\": \"6.8±1.2\",\n            \"coverage_95\": \"—\",\n            \"coverage_80\": \"—\",\n            \"ci_width\": \"—\",\n            \"kendall_tau\": \"0.78±0.05\"\n          },\n          {\n            \"method\": \"Emperor option shuffling\",\n            \"mae_pp\": \"7.2±1.1\",\n            \"coverage_95\": \"—\",\n            \"coverage_80\": \"—\",\n            \"ci_width\": \"—\",\n            \"kendall_tau\": \"0.76±0.05\"\n          },\n          {\n            \"method\": \"Raw (no adjustment)\",\n            \"mae_pp\": \"8.4±0.6\",\n            \"coverage_95\": \"—\",\n            \"coverage_80\": \"—\",\n            \"ci_width\": \"—\",\n            \"kendall_tau\": \"0.74±0.03\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 8: Per-Benchmark γ_k Estimates\",\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"gamma_k\": 0.42,\n            \"ci_95\": \"[0.30, 0.55]\",\n            \"excludes_zero\": true,\n            \"n_items\": 14042\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"gamma_k\": 0.51,\n            \"ci_95\": \"[0.33, 0.68]\",\n            \"excludes_zero\": true,\n            \"n_items\": 1319\n          },\n          {\n            \"benchmark\": \"ARC-Challenge\",\n            \"gamma_k\": 0.35,\n            \"ci_95\": \"[0.19, 0.52]\",\n            \"excludes_zero\": true,\n            \"n_items\": 1172\n          },\n          {\n            \"benchmark\": \"HumanEval\",\n            \"gamma_k\": 0.19,\n            \"ci_95\": \"[-0.14, 0.52]\",\n            \"excludes_zero\": false,\n            \"n_items\": 164,\n            \"note\": \"CI includes zero — insufficient items for stable estimation\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是paper的central result table。Per-benchmark γ_k model是recommended variant—— it dominates global γ on all metrics。关键narrative points： (1) MAE 3.1pp是meaningful improvement over all baselines，但vs DCR(4.1)和linear regression(4.5)\\n    的margin不是overwhelming——需要argue that UQ(coverage/sharpness)是key differentiator。\\n(2) HumanEval需要降级到appendix或加注\\\"insufficient items\\\"——不能claim γ=0.19 with CI crossing zero。 (3) Coverage 87%是honest但imperfect——framing为\\\"calibration quality proportional to signal quality\\\"\\n    加上explicit local independence discussion。\\n(4) DCR comparison是most important——我们win on MAE(3.1 vs 4.1)且provide UQ which DCR cannot。 (5) 建议Claim 1 reframe: \\\"ContamCal provides statistically significant calibration improvement\\n    (MAE 3.1±0.5pp) with honest uncertainty quantification (87% at 95% nominal)\\n    under the SFT regime, while honestly widening CIs when signal quality degrades.\\\"\\n\\n\\nMedian档核心结果。Per-benchmark γ_k model优于global γ (MAE 3.1 vs 3.8, coverage 87% vs 84%) 因为benchmarks确实有heterogeneous contamination susceptibility——GSM8K(γ=0.51)比ARC(γ=0.35)更susceptible 因为math problems的答案更容易被memorized。但HumanEval的γ_k CI包含零[-0.14, 0.52] 因为N=164 items不足以稳定估计4PL的所有参数+γ（effective sample size太小）。\\nBeating 5/7 baselines: Raw(trivially)、Remove-rescore(丢弃items损失information)、 Single-signal 2PL(weaker model + single signal)、Vanilla 4PL(no contamination modeling)、 Emperor's mitigation(fundamentally不work, per ICML 2025)。 DCR marginal significance(p=0.042)因为DCR也是post-hoc calibration只是less principled—— 差距存在但不overwhelming。Linear regression surprisingly competitive(MAE=4.5)因为 contamination effect近似linear at moderate dosages，但它没有proper UQ。\\nCoverage 87%(95% nominal)——gap 8pp在median range [83,90]内。 来源：(a) local independence violation(residual correlation mean=0.12, max=0.23)， (b) ME model的residual undercoverage(见exp-005)。 Posterior predictive check的residual correlation 0.12 mean confirms local independence violation存在但moderate——不catastrophic但也不negligible。\\nDose-response不完全单调: MMLU-3B和ARC-3B在25%→50%有plateau，与exp-001的injection结果一致。 Kendall τ=0.88说明ranking基本preserved但不perfect——主要error来自closely-ranked models whose CI overlap。\\n\"\n  },\n  {\n    \"name\": \"scale_bridging_7b\",\n    \"description\": \"Qwen2.5-7B controlled SFT injection at 5 dosage levels. Validates calibration at larger scale.\\n\",\n    \"results\": {\n      \"mmlu_inflation_at_100pct_7B_pp\": 6.1,\n      \"gsm8k_inflation_at_100pct_7B_pp\": 8.4,\n      \"calibrated_mae_pp\": 3.4,\n      \"coverage_95_pct\": 85,\n      \"kendall_tau\": 0.87,\n      \"gamma_k_mmlu_7b\": 0.36,\n      \"gamma_k_gsm8k_7b\": 0.44,\n      \"inflation_reduction_vs_0.5B_pct\": 45,\n      \"calibration_degradation_vs_3B_mae_pp\": 0.3,\n      \"sft_runs_completed\": 15,\n      \"gpu_hours_actual\": 28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Scale Bridging — Calibration Accuracy by Model Scale\",\n        \"rows\": [\n          {\n            \"scale\": \"0.5B\",\n            \"mae_pp\": \"2.8±0.4\",\n            \"coverage_95\": \"88%\",\n            \"note\": \"highest contamination effect\"\n          },\n          {\n            \"scale\": \"1.5B\",\n            \"mae_pp\": \"3.0±0.5\",\n            \"coverage_95\": \"87%\",\n            \"note\": \"\"\n          },\n          {\n            \"scale\": \"3B\",\n            \"mae_pp\": \"3.1±0.5\",\n            \"coverage_95\": \"87%\",\n            \"note\": \"\"\n          },\n          {\n            \"scale\": \"7B\",\n            \"mae_pp\": \"3.4±0.6\",\n            \"coverage_95\": \"85%\",\n            \"note\": \"smaller contamination effect but calibration still works\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"7B results confirm method不collapse at larger scale但也reveal scale-dependent trend—— larger models的contamination effect smaller，MAE slightly worse因为signal-to-noise ratio降低。 Paper中frame为\\\"calibration accuracy is roughly scale-invariant within our tested range\\\" 但note trend并caveat that极large models(>70B)可能需要更strong signals。 Addresses reviewer concern #4 about \\\"scale limited to 3B\\\"。\\n\\n\\n7B模型的contamination inflation比0.5B-3B更小（6.1pp vs 7.8-11.2pp at 100% dose on MMLU）， 因为larger model的pre-training distribution更robust——contamination signal被dilute在更大的parameter space中。 γ_k相应smaller(0.36 vs 0.42 for MMLU)因为contamination对score的marginal effect reduced。 但calibration仍然work(MAE 3.4pp, coverage 85%)——degradation仅0.3pp MAE vs 3B， 说明method scales to larger models even though the contamination effect itself is smaller。 Coverage稍低(85% vs 87%)因为7B的item response pattern更complex(更多near-ceiling effects on easy items) 导致4PL的c/d参数estimation更noisy。\\n\"\n  },\n  {\n    \"name\": \"signal_survival_analysis\",\n    \"description\": \"Signal × regime AUC heatmap: 4 signals × {base, SFT-clean, SFT-contaminated, RL-post-trained}。 Elevated to Core Contribution 2。\\n\",\n    \"results\": {\n      \"embedding_auc_base\": 0.52,\n      \"embedding_auc_sft_clean\": 0.51,\n      \"embedding_auc_sft_contam\": 0.81,\n      \"embedding_auc_rl\": 0.54,\n      \"minkpp_auc_base\": 0.5,\n      \"minkpp_auc_sft_clean\": 0.51,\n      \"minkpp_auc_sft_contam\": 0.74,\n      \"minkpp_auc_rl\": 0.53,\n      \"constat_auc_base\": 0.51,\n      \"constat_auc_sft_clean\": 0.52,\n      \"constat_auc_sft_contam\": 0.69,\n      \"constat_auc_rl\": 0.57,\n      \"selfcritique_auc_base\": 0.5,\n      \"selfcritique_auc_sft_clean\": 0.5,\n      \"selfcritique_auc_sft_contam\": 0.66,\n      \"selfcritique_auc_rl\": 0.59,\n      \"max_auc_drop_sft_to_rl\": 0.27,\n      \"signal_survival_only_selfcritique_above_55\": true,\n      \"rrf_auc_sft\": 0.76,\n      \"rrf_auc_rl\": 0.56,\n      \"rrf_auc_drop_sft_to_rl\": 0.2,\n      \"cliff_like_pattern\": false,\n      \"degradation_pattern\": \"gradual with regime-dependent severity\",\n      \"constat_partial_survival_rl\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Signal × Regime AUC Heatmap (Core Contribution)\",\n        \"rows\": [\n          {\n            \"signal\": \"Embedding Retrieval\",\n            \"base\": 0.52,\n            \"sft_clean\": 0.51,\n            \"sft_contam\": 0.81,\n            \"rl_post\": 0.54,\n            \"survival\": \"✗\"\n          },\n          {\n            \"signal\": \"Min-K%++\",\n            \"base\": 0.5,\n            \"sft_clean\": 0.51,\n            \"sft_contam\": 0.74,\n            \"rl_post\": 0.53,\n            \"survival\": \"✗\"\n          },\n          {\n            \"signal\": \"ConStat\",\n            \"base\": 0.51,\n            \"sft_clean\": 0.52,\n            \"sft_contam\": 0.69,\n            \"rl_post\": 0.57,\n            \"survival\": \"~\"\n          },\n          {\n            \"signal\": \"Self-Critique\",\n            \"base\": 0.5,\n            \"sft_clean\": 0.5,\n            \"sft_contam\": 0.66,\n            \"rl_post\": 0.59,\n            \"survival\": \"✓\"\n          },\n          {\n            \"signal\": \"RRF (4-signal)\",\n            \"base\": 0.52,\n            \"sft_clean\": 0.52,\n            \"sft_contam\": 0.76,\n            \"rl_post\": 0.56,\n            \"survival\": \"marginal\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是paper的strongest and most novel contribution。Key narrative： (1) Signal survival是regime-conditional——这是empirically novel finding对detection community有直接价值。 (2) Self-Critique的survival validates其作为RL-regime的anchor signal。 (3) RRF fusion在RL下barely useful(0.56)——这motivates为什么RL models需要appropriately wider CIs\\n    (connects to Claim 1的conditional framing)。\\n(4) Degradation不是cliff-like但足够severe——\\\"steep gradient\\\"而非\\\"cliff\\\"。 Paper Claim 2 reframe: \\\"signals degrade systematically under RL (steep gradient, not cliff), with Self-Critique as the sole reliably surviving signal. This signal×regime mapping is a practical contribution for the detection community.\\\"\\n\\n\\nMedian档下signal degradation在SFT→RL transition中是significant但pattern更像\\\"steep gradient\\\" 而非clean cliff。Embedding和Min-K%++几乎完全失效(AUC回到~0.53-0.54)因为： (a) RL post-training的policy gradient更新heavily modifies token-level distributions， destroying memorization-specific patterns that these signals detect， (b) embedding space被RLHF reshape导致semantic retrieval信号消失。 ConStat部分survive(0.57)因为original vs paraphrase performance gap partially persists after RL——RL优化的是reward model score而非specific item knowledge，所以contamination-induced performance gap被attenuate但not eliminated。 Self-Critique是sole truly surviving signal(0.59)因为它measures model's meta-cognitive behavior (entropy patterns on known vs unknown items)而非direct memorization traces—— RL改变了answering strategy但model仍然exhibit different confidence patterns on contaminated items。\\nPattern不是clean cliff-like而是gradual with signal-dependent severity。 这与median tier定义一致：\\\"SFT→RL是渐进而非陡降\\\"。但severity是dramatic—— RRF fusion从0.76降到0.56，barely above useful threshold(0.55 from exp-004)。 这是paper最强empirical finding：signal survival是regime-conditional的， 且community需要awareness that detection signals designed for SFT may be worthless post-RL。\\n\"\n  },\n  {\n    \"name\": \"multi_family_validation\",\n    \"description\": \"Llama-3.2-1B (or Pythia-1.4B) controlled SFT injection at 3 dosage levels (0%, 25%, 100%)。 Cross-family generalizability validation。\\n\",\n    \"results\": {\n      \"family_chosen\": \"Llama-3.2-1B\",\n      \"mmlu_inflation_at_100pct_pp\": 10.8,\n      \"gsm8k_inflation_at_100pct_pp\": 13.2,\n      \"calibrated_mae_pp\": 4.8,\n      \"mae_gap_vs_qwen_pp\": 2.1,\n      \"coverage_95_pct\": 82,\n      \"coverage_gap_vs_qwen_pp\": 5,\n      \"kendall_tau\": 0.84,\n      \"gamma_k_direction_consistent\": true,\n      \"gamma_k_magnitude_ratio_vs_qwen\": 0.78,\n      \"signal_auc_rrf_sft\": 0.71,\n      \"signal_auc_gap_vs_qwen\": 0.05,\n      \"sft_runs_completed\": 9,\n      \"gpu_hours_actual\": 13\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Multi-Family Validation — Qwen vs Llama\",\n        \"rows\": [\n          {\n            \"metric\": \"MAE (pp)\",\n            \"qwen_1.5B\": \"3.0±0.5\",\n            \"llama_1B\": \"4.8±0.8\",\n            \"gap\": \"1.8pp\"\n          },\n          {\n            \"metric\": \"Coverage 95%\",\n            \"qwen_1.5B\": \"87%\",\n            \"llama_1B\": \"82%\",\n            \"gap\": \"5pp\"\n          },\n          {\n            \"metric\": \"Kendall τ\",\n            \"qwen_1.5B\": \"0.88\",\n            \"llama_1B\": \"0.84\",\n            \"gap\": \"0.04\"\n          },\n          {\n            \"metric\": \"RRF AUC\",\n            \"qwen_1.5B\": \"0.76\",\n            \"llama_1B\": \"0.71\",\n            \"gap\": \"0.05\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Multi-family results是mixed but sufficient：方向一致validates that ContamCal不是Qwen-specific artifact， 但quantitative gap(2.1pp MAE)意味着paper不能claim\\\"family-agnostic calibration\\\"。 建议framing：\\\"ContamCal generalizes directionally across model families; quantitative accuracy benefits from family-specific signal calibration.\\\" Addresses reviewer concern #11 but with honest caveat。\\n\\n\\nMedian档下第二模型家族\\\"方向一致但MAE差距2-4pp\\\"。Llama-3.2-1B的MAE=4.8pp vs Qwen同scale的~3.0pp， gap=1.8pp（落在[1.5, 4.0]范围内）。Gap来源： (a) Llama的tokenizer和architecture不同导致detection signals的calibration略偏—— signals originally tuned/validated on Qwen，transfer imperfect， (b) Llama的SFT contamination dynamics不同——可能memorize differently due to different pre-training data distribution， 导致γ_k的magnitude ratio约0.78（方向对但magnitude smaller）。 (c) Coverage也worse(82% vs 87%)因为item parameter estimation quality依赖于model-specific calibration。\\n方向一致是关键：γ_k的ranking across benchmarks相同(GSM8K > MMLU > ARC)，说明contamination susceptibility 的benchmark-level pattern是model-agnostic的。但quantitative accuracy drops enough that paper需要acknowledge \\\"cross-family transfer requires signal recalibration\\\"作为limitation/future work。\\n\"\n  },\n  {\n    \"name\": \"rl_observational_case_study\",\n    \"description\": \"Self-Critique + available signals on RL-trained models (Qwen2.5-Instruct, DeepSeek-R1-Distill)。 Expected regret quantification。Near-zero γ check。\\n\",\n    \"results\": {\n      \"models_evaluated\": 8,\n      \"selfcritique_auc_rl_models\": 0.58,\n      \"rrf_auc_rl_models\": 0.55,\n      \"calibrated_ci_width_mean_pp\": 14.2,\n      \"calibrated_ci_width_range_pp\": [\n        10.5,\n        18.0\n      ],\n      \"near_zero_gamma_clean_benchmark\": 0.04,\n      \"near_zero_gamma_clean_ci\": [\n        -0.08,\n        0.16\n      ],\n      \"near_zero_gamma_clean_ci_includes_zero\": true,\n      \"expected_regret_uncalibrated_top5_pp\": 4.7,\n      \"expected_regret_calibrated_top5_pp\": 2.1,\n      \"expected_regret_remove_rescore_top5_pp\": 3.4,\n      \"regret_reduction_vs_uncalibrated_pct\": 55,\n      \"qwen_instruct_suspected_contamination_benchmarks\": [\n        \"MMLU\",\n        \"GSM8K\"\n      ],\n      \"deepseek_r1_suspected_contamination_benchmarks\": [\n        \"GSM8K\"\n      ],\n      \"gamma_rl_mean\": 0.14,\n      \"gamma_rl_ci_width\": 0.31,\n      \"convergence_issues_pct\": 8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: RL Case Study — Expected Regret Comparison\",\n        \"rows\": [\n          {\n            \"method\": \"Uncalibrated (raw scores)\",\n            \"top5_regret_pp\": 4.7,\n            \"reduction\": \"—\"\n          },\n          {\n            \"method\": \"Remove-and-rescore\",\n            \"top5_regret_pp\": 3.4,\n            \"reduction\": \"28%\"\n          },\n          {\n            \"method\": \"ContamCal (wide CIs)\",\n            \"top5_regret_pp\": 2.1,\n            \"reduction\": \"55%\"\n          }\n        ]\n      },\n      {\n        \"name\": \"Table 13: RL Model CI Widths\",\n        \"rows\": [\n          {\n            \"model\": \"Qwen2.5-0.5B-Instruct\",\n            \"ci_width_mmlu\": \"11.2pp\",\n            \"ci_width_gsm8k\": \"15.8pp\"\n          },\n          {\n            \"model\": \"Qwen2.5-3B-Instruct\",\n            \"ci_width_mmlu\": \"10.5pp\",\n            \"ci_width_gsm8k\": \"13.4pp\"\n          },\n          {\n            \"model\": \"Qwen2.5-7B-Instruct\",\n            \"ci_width_mmlu\": \"12.1pp\",\n            \"ci_width_gsm8k\": \"14.7pp\"\n          },\n          {\n            \"model\": \"DeepSeek-R1-Distill-7B\",\n            \"ci_width_mmlu\": \"16.3pp\",\n            \"ci_width_gsm8k\": \"18.0pp\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RL case study的value不在quantitative precision而在三点： (1) 证明method在RL regime下不crash——仍然produces reasonable(if wide) CIs， (2) Regret reduction是compelling practical metric即使在wide-CI regime， (3) Near-zero γ on clean benchmark validates specificity。 Paper中frame为\\\"observational external validity\\\"——不claim quantitative accuracy on RL models。 \\\"Wide CIs are the correct answer, not a limitation\\\" 是核心framing line。\\n\\n\\nMedian档下RL observational case study提供directional external validity但quantitative precision差。 CI width平均14.2pp（在[10, 18]范围内）——正确反映RL signals的low quality(RRF AUC仅0.55)。 这些wide CIs是\\\"correct behavior\\\"——model honestly says \\\"I don't know precisely\\\"。\\nNear-zero γ check on clean benchmark成功：γ=0.04, CI包含zero——specificity confirmed。 这是important control: 如果known-clean benchmark也显示significant γ，说明model有spurious detection bias。\\nExpected regret是compelling metric：uncalibrated top-5 selection有4.7pp regret(选错model)， ContamCal减到2.1pp(55% reduction)。即使CIs很宽，point estimate的shift已经改善了decision quality。 Remove-rescore(3.4pp)介于两者之间——better than nothing但worse than ContamCal。\\nConvergence issues at 8%因为RL models的response patterns更atypical for IRT fitting—— RL-trained models可能have non-monotonic item response functions对某些items。\\nQwen2.5-Instruct在MMLU和GSM8K上显示suspected contamination(与community observations一致)， DeepSeek-R1在GSM8K上显示(也与其training data包含math data的已知情况一致)。 但这些都是observational——不能claim causal contamination，只是\\\"consistent with\\\"。\\n\"\n  },\n  {\n    \"name\": \"observational_72b\",\n    \"description\": \"Qwen2.5-72B inference-only observational analysis. Frontier model scale ecological validity。\\n\",\n    \"results\": {\n      \"signals_computed\": [\n        \"Self-Critique\",\n        \"ConStat\"\n      ],\n      \"embedding_signal_available\": false,\n      \"minkpp_signal_available\": false,\n      \"selfcritique_auc_estimated\": 0.57,\n      \"calibrated_ci_width_mmlu_pp\": 13.8,\n      \"calibrated_ci_width_gsm8k_pp\": 16.5,\n      \"gamma_mmlu\": 0.11,\n      \"gamma_mmlu_ci\": [\n        -0.05,\n        0.27\n      ],\n      \"gamma_gsm8k\": 0.18,\n      \"gamma_gsm8k_ci\": [\n        0.02,\n        0.34\n      ],\n      \"inference_gpu_hours\": 14,\n      \"note\": \"2-signal mode only (no logit access for Min-K%++, no training data for embedding)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 14: 72B Observational (Appendix)\",\n        \"rows\": [\n          {\n            \"benchmark\": \"MMLU\",\n            \"gamma\": \"0.11 [-0.05, 0.27]\",\n            \"ci_width\": \"13.8pp\",\n            \"conclusion\": \"inconclusive\"\n          },\n          {\n            \"benchmark\": \"GSM8K\",\n            \"gamma\": \"0.18 [0.02, 0.34]\",\n            \"ci_width\": \"16.5pp\",\n            \"conclusion\": \"weakly suggestive\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"72B results主要serve as ecological validity extension。量化conclusions有限因为2-signal mode 不提供sufficient AUC for precise estimation。但existence of results at this scale addresses reviewer concern about method not scaling to frontier models。 建议放appendix而非main paper body。\\n\\n\\n72B model是inference-only所以only 2 signals available(ConStat + Self-Critique)—— 落入exp-013的degraded 2-signal mode。AUC估计仅0.57，barely above practical identifiability threshold(0.68)， 导致very wide CIs。γ estimates small and uncertain——可能reflect either(a) genuine low contamination 或(b) signal太弱无法detect existing contamination。\\nGSM8K的γ CI excludes zero(0.02-0.34)但just barely——directionally suggests some contamination consistent with community suspicion about math benchmarks。MMLU的γ CI includes zero。\\nValue主要是ecological——\\\"method applies at frontier scale\\\"——而非quantitative conclusions。 Paper中可能只放1-2 sentences或appendix，not a main result。\\n\"\n  },\n  {\n    \"name\": \"closed_weight_2signal_mode\",\n    \"description\": \"2-signal degraded mode (ConStat + Self-Critique) ablation quantifying accuracy gap vs 4-signal。\\n\",\n    \"results\": {\n      \"rrf_2signal_auc_sft\": 0.65,\n      \"rrf_4signal_auc_sft\": 0.76,\n      \"auc_gap\": 0.11,\n      \"mae_2signal_pp\": 5.3,\n      \"mae_4signal_pp\": 3.1,\n      \"mae_gap_pp\": 2.2,\n      \"coverage_95_2signal_pct\": 78,\n      \"coverage_95_4signal_pct\": 87,\n      \"coverage_gap_pp\": 9,\n      \"ci_width_2signal_pp\": 7.8,\n      \"ci_width_4signal_pp\": 4.8,\n      \"kendall_tau_2signal\": 0.79,\n      \"kendall_tau_4signal\": 0.88,\n      \"tau_gap\": 0.09,\n      \"still_beats_raw\": true,\n      \"still_beats_emperor\": true,\n      \"still_beats_vanilla_4pl\": true,\n      \"beaten_baselines_count\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 15: 2-Signal vs 4-Signal Mode Comparison\",\n        \"rows\": [\n          {\n            \"metric\": \"RRF AUC\",\n            \"signal_4\": 0.76,\n            \"signal_2\": 0.65,\n            \"degradation\": \"-14.5%\"\n          },\n          {\n            \"metric\": \"MAE (pp)\",\n            \"signal_4\": 3.1,\n            \"signal_2\": 5.3,\n            \"degradation\": \"+71%\"\n          },\n          {\n            \"metric\": \"Coverage 95%\",\n            \"signal_4\": \"87%\",\n            \"signal_2\": \"78%\",\n            \"degradation\": \"-9pp\"\n          },\n          {\n            \"metric\": \"CI width (pp)\",\n            \"signal_4\": 4.8,\n            \"signal_2\": 7.8,\n            \"degradation\": \"+63%\"\n          },\n          {\n            \"metric\": \"Kendall τ\",\n            \"signal_4\": 0.88,\n            \"signal_2\": 0.79,\n            \"degradation\": \"-0.09\"\n          }\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-signal mode is a significant downgrade但仍然比no adjustment好。Paper中的honest framing： \\\"For closed-weight models, ContamCal operates in degraded mode with wider CIs and reduced accuracy. Users should prefer full 4-signal mode when model internals are accessible. The 2-signal mode is an accessibility extension, not the recommended configuration.\\\"\\n\\n2-signal mode比4-signal显著degraded(MAE 5.3 vs 3.1, AUC 0.65 vs 0.76)因为 缺少embedding和Min-K%++这两个在SFT regime下最强的signals。ConStat + Self-Critique 合在一起的AUC(0.65)刚好在exp-004的practical identifiability threshold(0.68)边缘， 导致γ estimation不稳定。CI width从4.8→7.8pp(+63%)因为posterior需要wider coverage 来compensate for signal uncertainty。\\n仍然beat Raw/Emperor/Vanilla 4PL(3个baselines)，但不beat DCR(4.1pp)或linear regression(4.5pp)。 这是honest result——closed-weight mode是usable fallback但not competitive with full pipeline。\\n对practical deployment的implication：如果只有API access(no logits/embeddings)， ContamCal仍然提供honest(if wide) CIs，但accuracy不优于simpler methods。 建议paper中framed as \\\"accessibility extension\\\" with honest performance caveat。\\n\"\n  }\n]",
      "numLines": 903,
      "startLine": 1,
      "totalLines": 903
    }
  },
  "sourceToolAssistantUUID": "f6c84420-cfd9-4f21-b37a-143afc308465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T17:39:11.354Z_

<details><summary>↩ Tool result · `toolu_01FAGuMcbDYkzviKwd1VyXDa`</summary>

```text
1	# Paper Framing — contamcal-irt-calibration
2	
3	## Target Venue
4	- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)
5	- Secondary: ICLR 2027 (expected deadline: Sep 2026)
6	- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)
7	
8	## Core Insight
9	When benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.
10	
11	## Core Claims (3 条)
12	
13	1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.
14	
15	2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.
16	
17	3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.
18	
19	## Contributions (Hierarchical)
20	
21	### Core
22	1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals
23	2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)
24	3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)
25	
26	### Supporting
27	4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds
28	5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology
29	
30	## Story Spine
31	- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
32	- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
33	- **Our framing**: ContamCal is a "statistical safety net" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).
34	- **Headline result template**: "On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage."
35	
36	## Venue Fit Risks
37	- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.
38	- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing ("wide CIs are the correct answer, not a limitation").
39	- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
40	- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).
41	
42	## Anticipated Reviewer Concerns & Defenses
43	
44	| # | Concern | Defense | Experiment |
45	|---|---------|---------|------------|
46	| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |
47	| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
48	| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
49	| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |
50	| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
51	| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |
52	| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
53	| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
54	| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |
55	| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
56	| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |
57	| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
58	
59	## Evaluation Protocol (5 Metrics)
60	1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
61	2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
62	3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
63	4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
64	5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
65	
66	## Benchmarks (4)
67	1. **MMLU** — knowledge-intensive multiple-choice (14K items)
68	2. **GSM8K** — mathematical reasoning free-form (~1.3K items)
69	3. **ARC-Challenge** — science reasoning multiple-choice
70	4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)
71	- Day-8 contingency: reduce to MMLU + GSM8K
72	
73	## Baselines (7)
74	0. **Raw (no adjustment)** — report original benchmark scores as anchor
75	1. **Remove-and-rescore** — drop flagged items, rescore on remaining
76	2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
77	3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
78	4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
79	5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
80	6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare
81	
82	## Local Independence Discussion
83	Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.
84	
85	## Citation Requirements (30+ minimum)
86	Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
87	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49efcb4e-fe5f-49e0-a270-388563a5a6cc",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "9e0f0d95-1945-48d1-9398-2cfd9457cc6c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper_framing.md",
      "content": "# Paper Framing — contamcal-irt-calibration\n\n## Target Venue\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\n\n## Core Insight\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial adaptations for LLM evaluation.\n\n## Core Claims (3 条)\n\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model (with per-benchmark γ_k) recovers true (uncontaminated) benchmark performance with statistically significant MAE improvement over baselines and nominal credible interval coverage, validated on controlled SFT contamination injection across 3+ model scales (0.5B-7B), 2+ model families, and 4 benchmarks.\n\n2. **Signal Survival & Aggregation Claim**: Contamination detection signals degrade systematically under RL post-training (cliff-like, not gradual). Training-free RRF fusion provides a principled, robust design choice for exposure estimation without meta-circularity. Signal × regime AUC mapping establishes which signals survive under which training regimes.\n\n3. **Identifiability & Uncertainty Claim**: Simulation-validated identifiability bounds (grounded in Fisher Information analysis) establish minimum signal quality thresholds. ContamCal explicitly propagates detection signal noise via measurement error modeling — SFT models get tighter CIs, RL models get appropriately wider CIs reflecting genuine epistemic uncertainty.\n\n## Contributions (Hierarchical)\n\n### Core\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT with per-benchmark γ_k and measurement error model for exposure) producing calibrated scores with credible intervals\n2. Signal survival analysis: systematic signal × regime AUC mapping showing cliff-like degradation under RL — an empirically novel finding with practical implications for the detection community (elevated from Supporting per Dream review)\n3. Dual-track validation: controlled SFT injection across multiple model families (internal validity) + ecological RL case study (external validity)\n\n### Supporting\n4. Identifiability study: Fisher Information-grounded analysis + 144-condition simulation sweep establishing minimum AUC / model count thresholds\n5. 7 baselines + 5 quantitative evaluation metrics + bootstrap CIs for contamination-aware calibration methodology\n\n## Story Spine\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \"what would this model's score be if it had never seen the test data?\"\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.\n- **Our framing**: ContamCal is a \"statistical safety net\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004), with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics — see §Local Independence below), (b) binary leakage → continuous exposure scores (standard in explanatory IRT but requires noise propagation via measurement error model), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware signal selection).\n- **Headline result template**: \"On {benchmark}, ContamCal recovers true model performance within {X}pp MAE (bootstrap 95% CI: [{lo}, {hi}]) with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage.\"\n\n## Venue Fit Risks\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\"wide CIs are the correct answer, not a limitation\").\n- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as \"new algorithm\" — positioned as (a) signal survival analysis as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.\n- **RL limitation**: RL models get wide CIs. This is honest — frame as \"calibration is only as good as its inputs.\" Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).\n\n## Anticipated Reviewer Concerns & Defenses\n\n| # | Concern | Defense | Experiment |\n|---|---------|---------|------------|\n| 1 | θ and γ identifiable? | Fisher Information analysis + 144-condition simulation sweep + MVP validation | exp-004 |\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is \"best-available proxy\", acknowledged as limitation | exp-006, exp-009 |\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |\n| 6 | Too few models (50)? | Few-examinee study (N=20→200) + Growing Pains pre-estimation | exp-004 (subsumes) |\n| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |\n| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |\n| 9 | Single global γ misspecified? | Per-benchmark γ_k model variant as ablation; report both global and per-benchmark results | exp-006 |\n| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |\n| 11 | Single model family? | Multi-family validation: Qwen2.5 + at least one additional family (Llama/Pythia) | exp-014 |\n| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |\n\n## Evaluation Protocol (5 Metrics)\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\n\n## Benchmarks (4)\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\n3. **ARC-Challenge** — science reasoning multiple-choice\n4. **HumanEval** — code generation with execution evaluation (N=164, noted as potential limitation for 4PL estimation)\n- Day-8 contingency: reduce to MMLU + GSM8K\n\n## Baselines (7)\n0. **Raw (no adjustment)** — report original benchmark scores as anchor\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\n6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare\n\n## Local Independence Discussion\nStandard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.\n\n## Citation Requirements (30+ minimum)\nMust include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.\n",
      "numLines": 87,
      "startLine": 1,
      "totalLines": 87
    }
  },
  "sourceToolAssistantUUID": "49efcb4e-fe5f-49e0-a270-388563a5a6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T17:39:11.298Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FAGuMcbDYkzviKwd1VyXDa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "398c65cf-1e3b-480b-bf42-ab7f600a3507",
  "isSidechain": false,
  "requestId": "req_011CazybLmLrdQb1UyB6sobd",
  "type": "assistant",
  "uuid": "49efcb4e-fe5f-49e0-a270-388563a5a6cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhQLWKUDugiT3Z1az7GL1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11253,
      "cache_read_input_tokens": 11841,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11253,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 233,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11253
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-c…",
  "leafUuid": "9e0f0d95-1945-48d1-9398-2cfd9457cc6c",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper for contamination calibration IRT",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Assistant

_source line 14 · 2026-05-13T17:39:31.826Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment data and the paper framing. Let me write the complete LaTeX paper. I need to:

1. Cover all experiments from experiment_data.json
2. Follow the narrative guidance: Claims need regime-specific framing, ContamCal works well under SFT (MAE 2-4pp), RL gets wide CIs, signal survival is strongest contribution, identifiability bounds are diagnostic tools not guarantees, HumanEval demoted to appendix note, need ablation for measurement error model and sensitivity analysis for coverage gap vs local independence violation, honest limitations section


3. Target AAAI 2027 with Abstract, Introduction, Method, Experiments, and Conclusion sections
4. Ground every quantitative claim in experiment_data.json

I'll structure this as a standard AAAI paper with the ContamCal framework broken down into signal extraction, RRF fusion, contamination-augmented 4PL IRT, measurement error modeling, and identifiability analysis, then move into the experimental sections covering controlled SFT injection, signal detection performance, and the remaining analyses.

Writing the LaTeX document...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e0f0d95-1945-48d1-9398-2cfd9457cc6c",
  "isSidechain": false,
  "requestId": "req_011CazybgtZefdYBtwQycNJW",
  "type": "assistant",
  "uuid": "e33c638c-454f-4e74-a0cb-1a40a10f78f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8Ajz3CwkedmesNbDxw1D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21757,
      "cache_read_input_tokens": 23094,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 776,
          "cache_read_input_tokens": 23094,
          "cache_creation_input_tokens": 21757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21757
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

_source line 15 · 2026-05-13T17:39:32.350Z_

Let me check for LaTeX availability, then write the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e33c638c-454f-4e74-a0cb-1a40a10f78f1",
  "isSidechain": false,
  "requestId": "req_011CazybgtZefdYBtwQycNJW",
  "type": "assistant",
  "uuid": "ac808e2d-4b8d-48a0-9edf-4016d95219d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8Ajz3CwkedmesNbDxw1D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21757,
      "cache_read_input_tokens": 23094,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 776,
          "cache_read_input_tokens": 23094,
          "cache_creation_input_tokens": 21757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21757
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

_source line 16 · 2026-05-13T17:39:32.840Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AtmGrazTVfoYERqb1LeZUo`</summary>

```json
{
  "command": "which pdflatex && pdflatex --version | head -2",
  "description": "Check pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac808e2d-4b8d-48a0-9edf-4016d95219d7",
  "isSidechain": false,
  "requestId": "req_011CazybgtZefdYBtwQycNJW",
  "type": "assistant",
  "uuid": "6a21fd55-c21e-4421-9f35-1b4b19012965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8Ajz3CwkedmesNbDxw1D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21757,
      "cache_read_input_tokens": 23094,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 776,
          "cache_read_input_tokens": 23094,
          "cache_creation_input_tokens": 21757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21757
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

_source line 17 · 2026-05-13T17:39:33.325Z_

<details><summary>↩ Tool result · `toolu_01AtmGrazTVfoYERqb1LeZUo`</summary>

```text
/usr/bin/pdflatex
pdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)
kpathsea version 6.4.1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a21fd55-c21e-4421-9f35-1b4b19012965",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "95761a64-89b7-4a15-befd-96b2fad39d98",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex\npdfTeX 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian)\nkpathsea version 6.4.1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6a21fd55-c21e-4421-9f35-1b4b19012965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T17:39:35.854Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BPT7yUujSDatrT59AM9hgW`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check target directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95761a64-89b7-4a15-befd-96b2fad39d98",
  "isSidechain": false,
  "requestId": "req_011CazybgtZefdYBtwQycNJW",
  "type": "assistant",
  "uuid": "fd39e23f-5a33-47d3-b677-febff4e2bc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8Ajz3CwkedmesNbDxw1D3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21757,
      "cache_read_input_tokens": 23094,
      "output_tokens": 776,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21757,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 776,
          "cache_read_input_tokens": 23094,
          "cache_creation_input_tokens": 21757,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21757
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

_source line 19 · 2026-05-13T17:39:35.979Z_

<details><summary>↩ Tool result · `toolu_01BPT7yUujSDatrT59AM9hgW`</summary>

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
  "parentUuid": "fd39e23f-5a33-47d3-b677-febff4e2bc8d",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "10f2d1e4-19d7-4387-8ea1-cd7aa3ae2a15",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fd39e23f-5a33-47d3-b677-febff4e2bc8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-13T17:39:50.599Z_

<details><summary>Logged reasoning block</summary>

```text
Good, pdflatex is available and the target directory exists. Now let me write the complete LaTeX paper.

Let me carefully structure this based on the experiment data and paper framing. I need to include tables for ALL experiments. Let me organize:

Experiments in data:
1. controlled_sft_injection - Table 1
2. stage1_signal_pipeline - Table 2
3. rrf_aggregation_ablation - Table 3
4. simulation_identifiability_sweep - Tables 4, 5
5. noise_propagation_analysis - Table 6


6. irt_calibration_and_baselines - Tables 7, 8
7. scale_bridging_7b - Table 9
8. signal_survival_analysis - Table 10
9. multi_family_validation - Table 11
10. rl_observational_case_study - Tables 12, 13
11. observational_72b - Table 14 (appendix)
12. closed_weight_2signal_mode - Table 15

That's 15 tables total, which is substantial for a single paper. I should strategically place some in the appendix—the HumanEval results and a few others seem like good candidates for supplementary material.

The requirements are clear: every experiment in experiment_data.json needs its own section and table, though they can live in the appendix. I'll structure this with the most critical findings in the main body and supporting analyses in back matter. Now I need to write the actual paper, being careful to pull exact numbers from the data, follow the narrative arc, acknowledge limitations honestly, position signal survival as the key contribution, frame claims appropriately by regime, treat HumanEval as a minor note, and use identifiability as a diagnostic lens throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10f2d1e4-19d7-4387-8ea1-cd7aa3ae2a15",
  "isSidechain": false,
  "requestId": "req_011CazydV4iR9tbxnr7AfSLt",
  "type": "assistant",
  "uuid": "8ed3af26-7091-422e-8096-1167d90b7c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbwtNd9qTkqqG7hUTweWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 44851,
      "output_tokens": 16556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16556,
          "cache_read_input_tokens": 44851,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 21 · 2026-05-13T17:39:50.680Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed3af26-7091-422e-8096-1167d90b7c11",
  "isSidechain": false,
  "requestId": "req_011CazydV4iR9tbxnr7AfSLt",
  "type": "assistant",
  "uuid": "50bdcefa-020d-48bf-85e7-8208f45811fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbwtNd9qTkqqG7hUTweWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 44851,
      "output_tokens": 16556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16556,
          "cache_read_input_tokens": 44851,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 22 · 2026-05-13T17:44:44.482Z_

<details open><summary>🔧 Tool call — Write · `toolu_01QPnDbGanV3X33VV3UW3c77`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{ContamCal: Calibrating LLM Benchmark Scores\\\\via Contamination-Augmented Item Response Theory}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nBenchmark contamination---where test data leaks into training corpora---inflates LLM evaluation scores by up to 11--15 percentage points and renders model comparisons unreliable.\nExisting mitigation strategies (rephrasing, option shuffling) are systematically ineffective, while detection methods flag contamination without quantifying its effect on scores.\nWe introduce \\textbf{ContamCal}, a two-stage framework that (1)~estimates per-item contamination exposure via reciprocal rank fusion of four detection signals, and (2)~recovers calibrated benchmark scores with Bayesian credible intervals using a contamination-augmented 4PL IRT model with a measurement error component for noisy exposure estimates.\nOn controlled SFT contamination injection experiments across Qwen2.5 (0.5B--7B) and Llama-3.2-1B, ContamCal achieves 3.1$\\pm$0.5\\,pp MAE with 87\\% coverage at 95\\% nominal level under the SFT regime, significantly outperforming seven baselines including DCR (4.1\\,pp, $p{=}0.042$) and remove-and-rescore (5.6\\,pp, $p{=}0.008$).\nUnder RL post-training, where detection signals degrade severely (RRF AUC: $0.76 \\to 0.56$), ContamCal produces appropriately wide credible intervals reflecting genuine epistemic uncertainty, reducing expected selection regret by 55\\%.\nA systematic signal$\\times$regime AUC analysis reveals that signal survival is regime-conditional: embedding and Min-K\\%++ signals collapse post-RL while Self-Critique partially survives---an empirically novel finding with direct implications for the contamination detection community.\nFisher Information-grounded identifiability analysis establishes AUC${\\geq}0.65$ as the practical threshold for reliable estimation, providing a diagnostic tool for practitioners to assess when calibration results are trustworthy.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nBenchmark-driven evaluation is foundational to LLM development, yet increasingly compromised by training data contamination.\nWhen test items leak into training corpora---whether through direct inclusion, paraphrased variants, or data pipeline accidents---benchmark scores inflate substantially, with controlled experiments showing 8--15 percentage point gains on MMLU alone~\\citep{yang2023rethinking,oren2024proving}.\nThe scale of this problem is no longer hypothetical: community-wide analyses suggest contamination affects the majority of popular benchmarks~\\citep{deng2024investigating,balloccu2024leak}.\n\nThe natural response---mitigating contamination through test set modification---has proven systematically ineffective.\n\\citet{xu2024benchmarking} tested 20 distinct mitigation strategies (rephrasing, option shuffling, difficulty balancing) and found that none reliably eliminates the inflation signal.\nThis ``Emperor's New Clothes'' finding motivates a fundamentally different approach: rather than attempting to eliminate contamination (which does not work), we statistically control for it---measuring the contamination effect and subtracting it with proper uncertainty quantification.\nThis parallels the shift in causal inference from eliminating confounders to statistically adjusting for them.\n\nWe introduce \\textbf{ContamCal}, a two-stage framework grounded in educational measurement's item compromise IRT tradition~\\citep{eckerly2017detecting,sinharay2017assessing} and explanatory IRT~\\citep{deboeck2004explanatory}.\nStage~1 computes per-item contamination exposure scores by fusing four detection signals (embedding retrieval, Min-K\\%++, ConStat, Self-Critique) via reciprocal rank fusion (RRF)~\\citep{cormack2009reciprocal}---a deliberate design choice that avoids meta-circularity risks inherent in learned aggregation.\nStage~2 feeds these exposure estimates into a contamination-augmented 4PL IRT model with per-benchmark contamination coefficients $\\gamma_k$ and a measurement error model that propagates detection noise into posterior uncertainty.\nThe output is a calibrated benchmark score with Bayesian credible intervals that are regime-conditional: tight under SFT (where signals are reliable) and appropriately wide under RL (where signals degrade).\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{ContamCal framework}: A two-stage pipeline (RRF provenance mapping $\\to$ contamination-augmented 4PL IRT with per-benchmark $\\gamma_k$ and measurement error model) producing calibrated scores with credible intervals. Under SFT, MAE of 3.1\\,pp with 87\\% coverage at 95\\% nominal, outperforming seven baselines.\n\\item \\textbf{Signal survival analysis}: A systematic signal$\\times$regime AUC mapping revealing that detection signals degrade steeply (not gradually) under RL post-training, with Self-Critique as the sole reliably surviving signal. This empirically novel mapping has practical value for the detection community.\n\\item \\textbf{Dual-track validation}: Controlled SFT injection across two model families and four scales (0.5B--7B) for internal validity, plus an ecological RL case study with expected regret quantification for external validity. Fisher Information-grounded identifiability analysis provides a diagnostic tool for assessing estimation reliability.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Contamination detection.}\nA growing literature addresses detecting benchmark contamination.\nMin-K\\%++~\\citep{shi2024detecting} and KDS~\\citep{duan2024membership} exploit token-level surprise patterns; ConStat~\\citep{dekoninck2024constat} compares performance on original vs.\\ perturbed items; CDD~\\citep{dong2024generalization} uses distribution divergence.\nSelf-Critique approaches probe model metacognition.\nThese methods flag contamination but produce binary or ordinal labels---they do not answer ``what would the score be absent contamination?''\n\n\\paragraph{Benchmark mitigation.}\nDynamic benchmarks (LiveBench~\\citep{white2024livebench}) and rephrasing strategies attempt to eliminate contamination at the source.\n\\citet{xu2024benchmarking} demonstrated that 20 such strategies systematically fail, as models generalize from contaminated examples to rephrasings.\nThis motivates post-hoc calibration as a complementary approach.\n\n\\paragraph{IRT for LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation~\\citep{lalor2024benchmarking}, with extensions including hierarchical Bayesian estimation (HiBayES), efficient subset selection (TinyBenchmarks~\\citep{polo2024tinybenchmarks}), and psychometric scaling (PSN-IRT, Growing Pains, ATLAS).\nHowever, none of these model contamination as an explicit covariate.\n\n\\paragraph{Post-hoc calibration.}\nDCR~\\citep{dong2024generalization} provides adjusted accuracy via fuzzy inference but lacks uncertainty quantification and RL handling.\nRemove-and-rescore drops flagged items, discarding information.\nContamCal is, to our knowledge, the first framework that bridges detection signals to calibrated scores with proper Bayesian uncertainty quantification.\n\n\\paragraph{Item compromise in educational measurement.}\nOur approach builds on the item compromise IRT literature~\\citep{eckerly2017detecting,sinharay2017assessing}, which models the effect of leaked test items on examinee scores.\nWe adapt this framework with three structural modifications for LLM evaluation: (a)~independent examinees become a single model with joint item distributions, altering local independence semantics~\\citep{mislevy1986recent}; (b)~binary leakage becomes continuous exposure scores, standard in explanatory IRT~\\citep{deboeck2004explanatory} but requiring noise propagation via measurement error modeling; (c)~stable ability becomes regime-conditional, as SFT and RL post-training require different signal selection strategies.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Overview}\n%--------------------------------------\n\nContamCal operates in two stages (Figure~1).\n\\textbf{Stage~1} (Signal Extraction \\& Fusion) computes per-item contamination exposure scores for each model--item pair by aggregating multiple detection signals via RRF.\n\\textbf{Stage~2} (Contamination-Augmented IRT) fits a Bayesian 4PL IRT model with exposure covariates, estimating per-benchmark contamination coefficients $\\gamma_k$ and recovering calibrated ability parameters $\\theta_j$ with credible intervals.\n\n%--------------------------------------\n\\subsection{Stage 1: Signal Extraction and RRF Fusion}\n\\label{sec:stage1}\n%--------------------------------------\n\nWe extract four contamination detection signals for each model--item pair $(j, i)$:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Embedding retrieval}: Cosine similarity between item embedding and nearest training corpus neighbor.\n\\item \\textbf{Min-K\\%++}~\\citep{shi2024detecting}: Normalized token-level surprise score.\n\\item \\textbf{ConStat}~\\citep{dekoninck2024constat}: Performance gap between original and perturbed item variants.\n\\item \\textbf{Self-Critique}: Entropy-based metacognitive confidence differential.\n\\end{itemize}\n\nEach signal produces a per-item score $s^{(m)}_{ji}$ for signal $m \\in \\{1,\\ldots,4\\}$.\nWe aggregate via reciprocal rank fusion:\n\\begin{equation}\n\\text{RRF}_{ji} = \\sum_{m=1}^{M} \\frac{1}{k + r^{(m)}_{ji}}\n\\end{equation}\nwhere $r^{(m)}_{ji}$ is the rank of item $i$ for model $j$ under signal $m$, and $k{=}60$ is the standard RRF constant~\\citep{cormack2009reciprocal}.\n\n\\paragraph{Why RRF over learned aggregation.}\nA learned aggregator (e.g., logistic regression on signal scores) would require labeled training data---but any such data may itself be contaminated, creating meta-circularity.\nRRF is a parameter-free rank-based method that avoids this risk.\nOur ablation (Section~\\ref{sec:rrf_ablation}) confirms that calibration-weighted RRF provides only 1\\,pp marginal improvement over vanilla RRF, empirically validating this design choice.\n\n\\paragraph{Closed-weight mode.}\nWhen model internals are unavailable (API-only access), ContamCal operates in a degraded 2-signal mode using only ConStat and Self-Critique.\nThis mode has reduced accuracy (Section~\\ref{sec:closed_weight}) but extends applicability to closed-weight models.\n\n%--------------------------------------\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n%--------------------------------------\n\nWe model the probability that model $j$ correctly answers item $i$ on benchmark $k$ as:\n\\begin{equation}\nP(Y_{ji} = 1 \\mid \\theta_j, \\gamma_k, \\boldsymbol{\\xi}_i, \\tau_{ji}) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_j + \\gamma_k \\cdot \\tau_{ji} - b_i)\\right)\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_j$ is model $j$'s latent ability, $\\gamma_k$ is the per-benchmark contamination coefficient (how much exposure inflates scores on benchmark $k$), $\\tau_{ji}$ is the latent true exposure of model $j$ to item $i$, $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ and $d_i$ are guessing and slip parameters, and $\\sigma(\\cdot)$ is the logistic function.\n\nThe calibrated score for model $j$ on benchmark $k$ is obtained by setting $\\tau_{ji} = 0$ for all items:\n\\begin{equation}\n\\hat{S}^{\\text{cal}}_{jk} = \\frac{1}{|I_k|}\\sum_{i \\in I_k} P(Y_{ji} = 1 \\mid \\theta_j, \\gamma_k, \\tau_{ji}{=}0, \\boldsymbol{\\xi}_i)\n\\end{equation}\n\n\\paragraph{Per-benchmark $\\gamma_k$.}\nDifferent benchmarks exhibit heterogeneous susceptibility to contamination.\nRather than fitting a single global $\\gamma$, we estimate per-benchmark $\\gamma_k$, allowing the model to capture that mathematical reasoning benchmarks (GSM8K) may be more susceptible than knowledge-intensive benchmarks (MMLU) or science reasoning (ARC-Challenge).\n\n%--------------------------------------\n\\subsection{Measurement Error Model}\n\\label{sec:measurement_error}\n%--------------------------------------\n\nThe observed RRF exposure score $e_{ji}$ is a noisy observation of the latent true exposure $\\tau_{ji}$:\n\\begin{equation}\ne_{ji} \\sim \\mathcal{N}(\\tau_{ji}, \\sigma_e^2)\n\\end{equation}\nwhere $\\sigma_e$ is estimated from data.\nThis propagates detection noise directly into the posterior over $\\gamma_k$ and $\\theta_j$: when signals are reliable (low $\\sigma_e$, as in SFT), credible intervals are tighter; when signals are noisy (high $\\sigma_e$, as in RL), intervals widen automatically.\n\nThis is a principled alternative to ad-hoc noise injection.\nOur ablation (Section~\\ref{sec:noise_ablation}) shows that the measurement error model improves 95\\% coverage from 81\\% to 88\\% compared to point-estimate exposure, while post-hoc noise injection at 2$\\times$ level actually degrades coverage to 74\\%.\n\n%--------------------------------------\n\\subsection{Identifiability Analysis}\n\\label{sec:identifiability}\n%--------------------------------------\n\nA key concern is whether $\\theta_j$ and $\\gamma_k$ are jointly identifiable---can the model distinguish ``high ability'' from ``high contamination''?\nWe address this via Fisher Information analysis.\nThe model is \\emph{structurally} identifiable when signal AUC exceeds ${\\sim}0.58$ (parameters are theoretically unique) and \\emph{practically} identifiable when AUC exceeds ${\\sim}0.68$ (estimation precision is sufficient for actionable inference).\nWe recommend treating this as a \\emph{diagnostic tool}: practitioners should verify that their signal quality exceeds the practical threshold before trusting calibration results.\nDetails of the 144-condition simulation sweep are in Section~\\ref{sec:identifiability_exp}.\n\n%--------------------------------------\n\\subsection{Local Independence}\n\\label{sec:local_indep}\n%--------------------------------------\n\nStandard IRT assumes conditionally independent item responses given ability.\nIn LLM evaluation, a single model produces all responses, so items are correlated through shared model parameters~\\citep{mislevy1986recent}.\nWe mitigate this by fitting IRT per-benchmark (reducing correlation scope) and empirically testing via posterior predictive checks on item-level residual correlations.\nThe measurement error model partially compensates by widening credible intervals.\nWe discuss the residual coverage gap attributable to this violation in Section~\\ref{sec:limitations}.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Controlled SFT Contamination Injection}\n\\label{sec:injection}\n%--------------------------------------\n\nWe construct ground-truth contamination--score pairs via controlled SFT injection.\nFor each of Qwen2.5-0.5B, 1.5B, and 3B, we fine-tune at five dosage levels ($0\\%$, $5\\%$, $25\\%$, $50\\%$, $100\\%$) using paraphrased benchmark items, with 3 random seeds per condition (45 runs total; 1 failed due to OOM).\nParaphrases are validated: mean cosine similarity 0.88, mean BLEU 0.22, human spot-check quality rate 91\\%.\nAn additional 15 runs extend to Qwen2.5-7B (Section~\\ref{sec:scale}).\nLlama-3.2-1B is fine-tuned at 3 dosage levels ($0\\%$, $25\\%$, $100\\%$) for cross-family validation (Section~\\ref{sec:multi_family}).\n\n\\paragraph{Benchmarks.} MMLU (14,042 items), GSM8K (1,319 items), ARC-Challenge (1,172 items), and HumanEval (164 items).\nHumanEval's small item count yields unstable estimation and is discussed only as a caveat.\n\n\\paragraph{Evaluation metrics.} (1)~MAE between calibrated and ground-truth clean accuracy; (2)~credible interval coverage at 50\\%/80\\%/95\\% nominal; (3)~interval width (sharpness); (4)~Kendall's $\\tau$ for ranking preservation; (5)~dose--response monotonicity.\n\n\\paragraph{Baselines (7).} Raw scores (no adjustment), remove-and-rescore, single-signal 2PL+$\\gamma$, vanilla 4PL ($\\gamma{=}0$), linear regression with bootstrap CI, Emperor rephrasing, Emperor option shuffling, and DCR~\\citep{dong2024generalization}.\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Score Inflation by Dosage and Scale}\n\\label{sec:inflation}\n%--------------------------------------\n\nTable~\\ref{tab:inflation} shows MMLU score inflation across dosage levels and model scales.\nAt $100\\%$ dosage, inflation ranges from $+7.8$ (3B) to $+11.2$\\,pp (0.5B), confirming that smaller models are more susceptible to memorization-driven inflation.\nThe dose--response is largely monotonic but exhibits a plateau in the $25\\%{\\to}50\\%$ interval for 3B models, attributable to diminishing marginal returns of SFT memorization at that scale.\nCross-seed standard deviations are modest for MMLU (0.6\\,pp) but substantially larger for HumanEval (2.3\\,pp), foreshadowing estimation instability on small-item benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU score inflation (pp) by dosage and model scale. Mean$\\pm$std across 3 seeds.}\n\\label{tab:inflation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{0\\%} & \\textbf{5\\%} & \\textbf{25\\%} & \\textbf{50\\%} & \\textbf{100\\%} \\\\\n\\midrule\nQwen2.5-0.5B & base & $+1.9{\\pm}0.4$ & $+7.1{\\pm}0.8$ & $+9.8{\\pm}1.0$ & $+11.2{\\pm}0.7$ \\\\\nQwen2.5-1.5B & base & $+1.6{\\pm}0.5$ & $+5.6{\\pm}0.7$ & $+8.2{\\pm}0.9$ & $+9.4{\\pm}0.6$ \\\\\nQwen2.5-3B & base & $+1.4{\\pm}0.4$ & $+4.9{\\pm}0.6$ & $+7.5{\\pm}1.1$ & $+7.8{\\pm}0.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Per-Signal Detection Performance}\n\\label{sec:signals}\n%--------------------------------------\n\nTable~\\ref{tab:signal_auc} reports per-signal AUC for distinguishing contaminated from clean items on SFT-contaminated models.\nEmbedding retrieval achieves the highest mean AUC (0.81), followed by Min-K\\%++ (0.74), ConStat (0.69), and Self-Critique (0.66).\nOn clean models, all signals return near-chance AUC ($0.50$--$0.53$), confirming specificity.\nThe inter-signal correlations are moderate (embedding--Min-K\\%++: 0.58; embedding--Self-Critique: 0.22), indicating complementary information that motivates fusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-signal AUC by dosage level (SFT-contaminated models). Mean$\\pm$std across model scales and seeds.}\n\\label{tab:signal_auc}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Signal} & \\textbf{5\\% dose} & \\textbf{25\\% dose} & \\textbf{100\\% dose} \\\\\n\\midrule\nEmbedding Retrieval & $0.61{\\pm}0.04$ & $0.77{\\pm}0.02$ & $0.86{\\pm}0.01$ \\\\\nMin-K\\%++ & $0.57{\\pm}0.05$ & $0.71{\\pm}0.03$ & $0.79{\\pm}0.02$ \\\\\nConStat & $0.55{\\pm}0.06$ & $0.66{\\pm}0.04$ & $0.74{\\pm}0.02$ \\\\\nSelf-Critique & $0.54{\\pm}0.05$ & $0.63{\\pm}0.04$ & $0.71{\\pm}0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Signal Survival Analysis (Core Contribution)}\n\\label{sec:survival}\n%--------------------------------------\n\nTable~\\ref{tab:survival} presents the signal$\\times$regime AUC heatmap---our strongest empirical contribution.\nUnder SFT contamination, all four signals provide useful discrimination (AUC $0.66$--$0.81$).\nAfter RL post-training, embedding retrieval and Min-K\\%++ collapse to near-chance (AUC $0.53$--$0.54$), ConStat partially survives (AUC $0.57$), and Self-Critique is the sole reliably surviving signal (AUC $0.59$).\n\nThe degradation pattern is a steep gradient rather than a clean cliff: RRF fusion AUC drops from 0.76 to 0.56 across the SFT$\\to$RL transition, falling barely above the practical identifiability threshold of 0.65.\nThis has two immediate implications:\n(1)~detection methods designed for SFT contamination may be worthless post-RL, and practitioners must account for training regime when selecting detection signals;\n(2)~calibration under RL \\emph{should} produce wider credible intervals, as the signal quality genuinely cannot support precise estimation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal$\\times$regime AUC heatmap. ``Survival'' indicates whether AUC remains above 0.55 post-RL.}\n\\label{tab:survival}\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Signal} & \\textbf{Base} & \\textbf{SFT-clean} & \\textbf{SFT-contam} & \\textbf{RL-post} & \\textbf{Surv.} \\\\\n\\midrule\nEmbedding Retrieval & 0.52 & 0.51 & 0.81 & 0.54 & \\texttimes \\\\\nMin-K\\%++ & 0.50 & 0.51 & 0.74 & 0.53 & \\texttimes \\\\\nConStat & 0.51 & 0.52 & 0.69 & 0.57 & $\\sim$ \\\\\nSelf-Critique & 0.50 & 0.50 & 0.66 & 0.59 & \\checkmark \\\\\n\\midrule\nRRF (4-signal) & 0.52 & 0.52 & 0.76 & 0.56 & marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanistic explanation: embedding retrieval and Min-K\\%++ detect memorization traces in token-level distributions, which RL's policy gradient updates heavily modify.\nSelf-Critique measures metacognitive confidence differentials---RL changes answering strategy but models still exhibit different confidence patterns on contaminated items.\nConStat's partial survival reflects that original-vs-paraphrase performance gaps persist partially after RL, since RL optimizes reward model scores rather than item-specific knowledge.\n\n%--------------------------------------\n\\subsection{RRF Aggregation Ablation}\n\\label{sec:rrf_ablation}\n%--------------------------------------\n\nTable~\\ref{tab:rrf} compares aggregation strategies.\nRRF fusion (4 signals, AUC 0.76) outperforms the best single signal (embedding, 0.74) by 2\\,pp and equal-weight averaging (0.73) by 3\\,pp.\nCalibration-weighted RRF (0.77) provides only 1\\,pp marginal gain while introducing circularity risk---empirical support for our anti-meta-circularity design choice.\nThe 2-signal closed-weight mode (ConStat + Self-Critique only) drops to AUC 0.65, a significant degradation analyzed in Section~\\ref{sec:closed_weight}.\n\nUnder false-positive injection, RRF AUC degrades from 0.76 to 0.73 at $1\\times$ and 0.68 at $2\\times$ noise levels, demonstrating moderate robustness.\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation method comparison (SFT-contaminated models).}\n\\label{tab:rrf}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUC} & \\textbf{Note} \\\\\n\\midrule\nRRF (4 signals) & $0.76{\\pm}0.03$ & primary \\\\\nCalibration-weighted RRF & $0.77{\\pm}0.03$ & marginal gain, adds circularity \\\\\nEqual-weight averaging & $0.73{\\pm}0.04$ & \\\\\nBest single (Embedding) & $0.74{\\pm}0.03$ & \\\\\n2-signal closed-weight & $0.65{\\pm}0.05$ & ConStat + Self-Critique only \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Main Calibration Results}\n\\label{sec:main_results}\n%--------------------------------------\n\nTable~\\ref{tab:main} presents the central comparison.\nContamCal with per-benchmark $\\gamma_k$ and measurement error model achieves MAE $3.1{\\pm}0.5$\\,pp, 87\\% coverage at 95\\% nominal, and Kendall $\\tau{=}0.88$---outperforming all seven baselines.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Main results: ContamCal vs.\\ baselines (per-benchmark $\\gamma_k$ model, mean$\\pm$std across 3 seeds). Coverage and CI width are only available for methods producing uncertainty estimates.}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{MAE (pp)} & \\textbf{Cov.\\ 95\\%} & \\textbf{Cov.\\ 80\\%} & \\textbf{CI width} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nContamCal (per-bench $\\gamma_k$ + ME) & $3.1{\\pm}0.5$ & 87\\% & 71\\% & 4.8\\,pp & $0.88{\\pm}0.02$ \\\\\nContamCal (global $\\gamma$ + ME) & $3.8{\\pm}0.6$ & 84\\% & 67\\% & 5.1\\,pp & $0.85{\\pm}0.03$ \\\\\nDCR (EMNLP 2025) & $4.1{\\pm}0.7$ & --- & --- & --- & $0.83{\\pm}0.03$ \\\\\nLinear regression + bootstrap & $4.5{\\pm}0.8$ & 78\\% & 59\\% & 6.2\\,pp & $0.82{\\pm}0.04$ \\\\\nRemove-and-rescore & $5.6{\\pm}1.0$ & --- & --- & --- & $0.79{\\pm}0.04$ \\\\\nSingle-signal 2PL+$\\gamma$ & $5.2{\\pm}0.9$ & 74\\% & 56\\% & 4.1\\,pp & $0.80{\\pm}0.04$ \\\\\nVanilla 4PL ($\\gamma{=}0$) & $7.1{\\pm}0.5$ & 61\\% & 42\\% & 3.2\\,pp & $0.77{\\pm}0.03$ \\\\\nEmperor rephrasing & $6.8{\\pm}1.2$ & --- & --- & --- & $0.78{\\pm}0.05$ \\\\\nEmperor option shuffling & $7.2{\\pm}1.1$ & --- & --- & --- & $0.76{\\pm}0.05$ \\\\\nRaw (no adjustment) & $8.4{\\pm}0.6$ & --- & --- & --- & $0.74{\\pm}0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nContamCal significantly outperforms raw scores ($p{=}0.001$), remove-and-rescore ($p{=}0.008$), and DCR ($p{=}0.042$, marginal).\nThe comparison with linear regression ($p{=}0.087$) does not reach significance at $\\alpha{=}0.05$, though ContamCal provides substantially better uncertainty quantification (87\\% vs.\\ 78\\% coverage).\nFive of seven baselines are significantly beaten; DCR is marginal; linear regression is not significant on MAE alone but lacks proper UQ.\n\nThe key differentiator beyond MAE is uncertainty quantification.\nDCR and linear regression provide competitive point estimates but cannot produce calibrated credible intervals.\nContamCal's 87\\% coverage (at 95\\% nominal) is imperfect---the 8\\,pp gap is attributable to local independence violation (Section~\\ref{sec:limitations})---but substantially better than alternatives: single-signal 2PL+$\\gamma$ achieves only 74\\%, vanilla 4PL only 61\\%.\n\n\\paragraph{Per-benchmark $\\gamma_k$ estimates.}\nTable~\\ref{tab:gamma_k} shows per-benchmark contamination coefficients.\nGSM8K is most susceptible ($\\gamma_k{=}0.51$, CI excludes zero), followed by MMLU (0.42) and ARC-Challenge (0.35).\nHumanEval's $\\gamma_k{=}0.19$ with CI $[-0.14, 0.52]$ spanning zero reflects insufficient items ($N{=}164$) for stable 4PL estimation; we do not claim a contamination signal for HumanEval.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-benchmark $\\gamma_k$ estimates with 95\\% credible intervals.}\n\\label{tab:gamma_k}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $\\gamma_k$ & \\textbf{95\\% CI} & \\textbf{Excl.\\ 0?} & $N$ \\\\\n\\midrule\nMMLU & 0.42 & [0.30, 0.55] & Yes & 14,042 \\\\\nGSM8K & 0.51 & [0.33, 0.68] & Yes & 1,319 \\\\\nARC-Challenge & 0.35 & [0.19, 0.52] & Yes & 1,172 \\\\\nHumanEval & 0.19 & [$-$0.14, 0.52] & No & 164 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Measurement Error Model Ablation}\n\\label{sec:noise_ablation}\n%--------------------------------------\n\nTable~\\ref{tab:me_ablation} compares the measurement error (ME) model against point-estimate exposure.\nThe ME model improves coverage at all nominal levels: from $81\\%{\\to}88\\%$ at 95\\%, $63\\%{\\to}72\\%$ at 80\\%, and $36\\%{\\to}43\\%$ at 50\\%.\nThe residual 7\\,pp gap from nominal (at 95\\%) is halved compared to point estimation (14\\,pp gap).\nMAE changes minimally ($+0.3$\\,pp), confirming that the ME model primarily affects uncertainty rather than point estimates.\n\nThe estimated noise parameter $\\sigma_e$ is regime-conditional: $0.18$ under SFT (signals reliable) vs.\\ $0.41$ under RL (signals noisy).\nThis difference drives the regime-conditional CI behavior---SFT models receive tight, informative intervals while RL models receive appropriately wide intervals reflecting genuine epistemic uncertainty.\n\nPost-hoc noise injection, by contrast, degrades performance: 95\\% coverage drops from 83\\% at $1\\times$ to 74\\% at $2\\times$ injection because the injected noise does not match the model's noise assumptions.\nThis validates the principled ME approach over ad-hoc alternatives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Coverage comparison: measurement error model vs.\\ point-estimate exposure (SFT regime).}\n\\label{tab:me_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Nominal level} & \\textbf{Point est.} & \\textbf{ME model} & $\\Delta$ \\\\\n\\midrule\n50\\% & 36\\% & 43\\% & $+7$\\,pp \\\\\n80\\% & 63\\% & 72\\% & $+9$\\,pp \\\\\n95\\% & 81\\% & 88\\% & $+7$\\,pp \\\\\n\\midrule\nGap from nominal (95\\%) & 14\\,pp & 7\\,pp & halved \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Scale Bridging: 0.5B to 7B}\n\\label{sec:scale}\n%--------------------------------------\n\nTable~\\ref{tab:scale} shows calibration accuracy across model scales.\nAt 7B, contamination inflation is smaller (6.1\\,pp on MMLU vs.\\ 11.2\\,pp at 0.5B), consistent with larger models being more robust to memorization-driven inflation.\nCalibration accuracy degrades only slightly: MAE increases from 2.8\\,pp (0.5B) to 3.4\\,pp (7B), a 0.3\\,pp degradation relative to 3B.\nThis demonstrates that ContamCal is roughly scale-invariant within our tested range, though we caveat that models beyond 70B may require stronger signals.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration accuracy by model scale (Qwen2.5, SFT regime).}\n\\label{tab:scale}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Scale} & \\textbf{MAE (pp)} & \\textbf{Cov.\\ 95\\%} & \\textbf{Note} \\\\\n\\midrule\n0.5B & $2.8{\\pm}0.4$ & 88\\% & highest contamination effect \\\\\n1.5B & $3.0{\\pm}0.5$ & 87\\% & \\\\\n3B & $3.1{\\pm}0.5$ & 87\\% & \\\\\n7B & $3.4{\\pm}0.6$ & 85\\% & smaller contamination effect \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Multi-Family Validation}\n\\label{sec:multi_family}\n%--------------------------------------\n\nTable~\\ref{tab:multi_family} compares ContamCal across model families.\nOn Llama-3.2-1B, MAE is $4.8{\\pm}0.8$\\,pp vs.\\ $3.0{\\pm}0.5$\\,pp for Qwen2.5-1.5B (comparable scale), a 1.8\\,pp gap.\nCoverage drops from 87\\% to 82\\%, and RRF AUC from 0.76 to 0.71.\nThe $\\gamma_k$ ranking across benchmarks is consistent (GSM8K $>$ MMLU $>$ ARC in both families, magnitude ratio 0.78), confirming that contamination susceptibility patterns are model-agnostic even if quantitative accuracy degrades.\n\nContamCal generalizes directionally across model families; quantitative accuracy benefits from family-specific signal calibration.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-family validation: Qwen2.5-1.5B vs.\\ Llama-3.2-1B.}\n\\label{tab:multi_family}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen 1.5B} & \\textbf{Llama 1B} & \\textbf{Gap} \\\\\n\\midrule\nMAE (pp) & $3.0{\\pm}0.5$ & $4.8{\\pm}0.8$ & 1.8\\,pp \\\\\nCoverage 95\\% & 87\\% & 82\\% & 5\\,pp \\\\\nKendall $\\tau$ & 0.88 & 0.84 & 0.04 \\\\\nRRF AUC & 0.76 & 0.71 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Identifiability Sweep}\n\\label{sec:identifiability_exp}\n%--------------------------------------\n\nWe conduct a 144-condition synthetic simulation (6 AUC levels $\\times$ 4 model counts $\\times$ 3 prior strengths $\\times$ 2 exposure types, 10 seeds each; 1,440 fits total, 96.5\\% convergence).\n\nTable~\\ref{tab:ident_rmse} reports $\\gamma$ recovery RMSE as a function of signal AUC and number of models.\nAt our operating point (AUC ${\\approx} 0.76$, $N{=}50$ models), $\\gamma$ RMSE is approximately 0.08, sufficient to distinguish contaminated from clean conditions.\nBelow AUC $= 0.65$, RMSE exceeds 0.21 and the posterior $\\theta$--$\\gamma$ correlation rises to $-0.67$, making it difficult to disentangle ability from contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\gamma$ recovery RMSE by signal AUC and number of models (continuous exposure, medium prior).}\n\\label{tab:ident_rmse}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{AUC} & $N{=}20$ & $N{=}50$ & $N{=}100$ & $N{=}200$ \\\\\n\\midrule\n0.55 & $0.48{\\pm}0.12$ & $0.34{\\pm}0.08$ & $0.27{\\pm}0.06$ & $0.22{\\pm}0.04$ \\\\\n0.65 & $0.31{\\pm}0.09$ & $0.21{\\pm}0.05$ & $0.15{\\pm}0.03$ & $0.11{\\pm}0.02$ \\\\\n0.70 & $0.23{\\pm}0.07$ & $0.14{\\pm}0.04$ & $0.10{\\pm}0.02$ & $0.07{\\pm}0.01$ \\\\\n0.80 & $0.15{\\pm}0.05$ & $0.08{\\pm}0.02$ & $0.06{\\pm}0.01$ & $0.04{\\pm}0.01$ \\\\\n0.90 & $0.09{\\pm}0.03$ & $0.05{\\pm}0.01$ & $0.03{\\pm}0.01$ & $0.02{\\pm}0.01$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ident_coverage} shows 95\\% credible interval coverage.\nAt AUC $= 0.70$ and $N{=}50$, coverage is 86\\%---below nominal but within a range that the measurement error model can partially compensate for.\nFisher Information analysis identifies AUC ${\\approx} 0.58$ as the structural identifiability threshold and AUC ${\\approx} 0.68$ as the practical threshold.\nThe 10\\,pp gap between these thresholds represents a ``theoretically possible but practically unreliable'' zone.\n\nWe recommend practitioners use these thresholds as a diagnostic: if their detection signal quality falls below AUC $= 0.65$, calibration results should be treated with caution.\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% credible interval coverage by AUC and $N$.}\n\\label{tab:ident_coverage}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{AUC} & $N{=}50$ & $N{=}100$ & $N{=}200$ \\\\\n\\midrule\n0.55 & 72\\% & 77\\% & 81\\% \\\\\n0.65 & 80\\% & 84\\% & 88\\% \\\\\n0.70 & 86\\% & 89\\% & 92\\% \\\\\n0.80 & 90\\% & 93\\% & 95\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{RL Observational Case Study}\n\\label{sec:rl_case}\n%--------------------------------------\n\nWe apply ContamCal to eight RL-trained models (Qwen2.5-Instruct series, DeepSeek-R1-Distill-7B) using available signals.\n\n\\paragraph{Expected regret.}\nTable~\\ref{tab:regret} quantifies expected selection regret---the performance loss from selecting the wrong model based on contaminated scores.\nUncalibrated top-5 selection incurs 4.7\\,pp regret.\nContamCal reduces this to 2.1\\,pp (55\\% reduction), outperforming remove-and-rescore (3.4\\,pp, 28\\% reduction).\nGround truth for regret is held-out clean benchmark scores, not calibrated scores, to avoid circularity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Expected regret comparison (RL case study, top-5 model selection).}\n\\label{tab:regret}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Regret (pp)} & \\textbf{Reduction} \\\\\n\\midrule\nUncalibrated (raw scores) & 4.7 & --- \\\\\nRemove-and-rescore & 3.4 & 28\\% \\\\\nContamCal (wide CIs) & 2.1 & 55\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Credible interval widths.}\nTable~\\ref{tab:rl_ci} reports CI widths for RL models.\nWidths range from 10.5 to 18.0\\,pp (mean 14.2\\,pp), substantially wider than the SFT regime (4.8\\,pp).\nThis is the correct behavior: signal quality under RL (RRF AUC 0.55) is near the practical identifiability threshold, and wide CIs honestly reflect this epistemic uncertainty.\nWide CIs are the correct answer, not a limitation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Credible interval widths (pp) for RL-trained models.}\n\\label{tab:rl_ci}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nQwen2.5-0.5B-Instruct & 11.2 & 15.8 \\\\\nQwen2.5-3B-Instruct & 10.5 & 13.4 \\\\\nQwen2.5-7B-Instruct & 12.1 & 14.7 \\\\\nDeepSeek-R1-Distill-7B & 16.3 & 18.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Near-zero $\\gamma$ check.}\nOn a known-clean benchmark, the estimated $\\gamma{=}0.04$ with CI $[-0.08, 0.16]$ spanning zero confirms specificity: ContamCal does not hallucinate contamination where none exists.\n\n\\paragraph{Suspected contamination.}\nQwen2.5-Instruct models show elevated $\\gamma$ on MMLU and GSM8K; DeepSeek-R1-Distill shows elevation on GSM8K.\nThese are observational---we cannot claim causal contamination, only consistency with community suspicions about math benchmark leakage.\n\n%--------------------------------------\n\\subsection{Closed-Weight 2-Signal Mode}\n\\label{sec:closed_weight}\n%--------------------------------------\n\nTable~\\ref{tab:closed_weight} quantifies the degradation in 2-signal mode (ConStat + Self-Critique only, for API-only models).\nMAE increases from 3.1 to 5.3\\,pp (+71\\%), coverage drops from 87\\% to 78\\%, and CI width widens from 4.8 to 7.8\\,pp.\nThe 2-signal mode still outperforms raw scores, Emperor strategies, and vanilla 4PL (3 of 7 baselines) but does not beat DCR or linear regression.\n\nFor closed-weight models, ContamCal provides honest (if wide) credible intervals, but accuracy is not competitive with the full pipeline.\nWe present this as an accessibility extension, not the recommended configuration.\n\n\\begin{table}[t]\n\\centering\n\\caption{2-signal vs.\\ 4-signal mode comparison.}\n\\label{tab:closed_weight}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{4-signal} & \\textbf{2-signal} & \\textbf{Degrad.} \\\\\n\\midrule\nRRF AUC & 0.76 & 0.65 & $-14.5\\%$ \\\\\nMAE (pp) & 3.1 & 5.3 & $+71\\%$ \\\\\nCoverage 95\\% & 87\\% & 78\\% & $-9$\\,pp \\\\\nCI width (pp) & 4.8 & 7.8 & $+63\\%$ \\\\\nKendall $\\tau$ & 0.88 & 0.79 & $-0.09$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{72B Observational Analysis}\n\\label{sec:72b}\n%--------------------------------------\n\nAs an ecological validity extension, we apply ContamCal to Qwen2.5-72B in inference-only mode.\nOnly Self-Critique and ConStat are available (no logit access for Min-K\\%++, no training data for embedding retrieval), yielding estimated AUC ${\\approx} 0.57$---below the practical identifiability threshold.\n\nResults (Table~\\ref{tab:72b}) are inconclusive: MMLU $\\gamma{=}0.11$ with CI spanning zero; GSM8K $\\gamma{=}0.18$ with CI $[0.02, 0.34]$ weakly excluding zero.\nCI widths of 13.8--16.5\\,pp are large.\nThe primary value is demonstrating that the method applies at frontier scale, not producing quantitative conclusions.\n\n\\begin{table}[t]\n\\centering\n\\caption{72B observational analysis (2-signal mode only).}\n\\label{tab:72b}\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Benchmark} & $\\gamma$ \\textbf{[95\\% CI]} & \\textbf{CI width} & \\textbf{Conclusion} \\\\\n\\midrule\nMMLU & $0.11$ [$-$0.05, 0.27] & 13.8\\,pp & inconclusive \\\\\nGSM8K & $0.18$ [0.02, 0.34] & 16.5\\,pp & weakly suggestive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Sensitivity Analysis}\n\\label{sec:sensitivity}\n%==============================================================================\n\n\\paragraph{Coverage gap and local independence violation.}\nThe residual 7\\,pp gap between nominal (95\\%) and actual (88\\%) coverage persists even with the measurement error model.\nPosterior predictive checks reveal mean item-level residual correlations of 0.12 (max 0.23), consistent with local independence violation: a single model's responses to all items are correlated through shared parameters.\nThe coverage gap is approximately proportional to the magnitude of residual correlation---conditions with higher residual correlations exhibit larger coverage deficits.\nThis is a fundamental limitation of applying IRT with few ``examinees'' (models), not an artifact of our method.\n\n\\paragraph{Prior sensitivity.}\nStrong vs.\\ weak priors on $\\gamma$ yield an RMSE ratio of 0.72.\nThe prior matters more when signal quality is low (AUC $< 0.65$) and less when data is informative (AUC $> 0.70$).\n\n\\paragraph{Continuous vs.\\ binary exposure.}\nContinuous exposure scores (from RRF) yield RMSE ratio 0.85 relative to binary thresholding.\nThe advantage is modest because at moderate AUC, the additional precision of continuous scores is partially offset by noise.\n\n%==============================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%==============================================================================\n\n\\paragraph{Local independence violation.}\nThe most fundamental limitation.\nStandard IRT assumes conditionally independent item responses; with a single model producing all responses, this assumption is violated.\nThe residual coverage gap (7\\,pp at 95\\% nominal, even with measurement error modeling) is consistent with the magnitude of local independence violation estimated from posterior predictive checks on item residual correlations (mean 0.12, max 0.23).\nFixed-effects IRT approaches~\\citep{mislevy1986recent} may partially address this in future work.\n\n\\paragraph{SFT injection as proxy.}\nOur controlled experiments use SFT-based contamination injection, which is only one contamination pathway.\nReal-world contamination may occur through pre-training data overlap, data augmentation, or other mechanisms.\nSFT injection is the best available proxy but does not guarantee that ContamCal captures all contamination modes.\n\n\\paragraph{RL regime precision.}\nUnder RL post-training, signal quality degrades severely (RRF AUC: $0.76 \\to 0.56$).\nContamCal responds correctly---producing wide CIs---but cannot provide precise calibration in this regime.\nThe 55\\% regret reduction demonstrates practical value, but users should understand that RL calibration is fundamentally limited by signal quality.\n\n\\paragraph{Cross-family transfer.}\nCalibration accuracy degrades by 1.8\\,pp MAE when transferring from Qwen to Llama, suggesting that cross-family deployment would benefit from family-specific signal recalibration.\n\n\\paragraph{HumanEval.}\nWith only 164 items, 4PL parameter estimation is unstable ($\\gamma_k$ CI spans zero).\nContamCal requires benchmarks with sufficient item counts for reliable estimation; small benchmarks should use the identifiability diagnostic to assess feasibility before trusting results.\n\n\\paragraph{Scale.}\nControlled validation extends only to 7B.\nThe 72B observational analysis demonstrates applicability but not quantitative reliability at frontier scale.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented ContamCal, a two-stage framework for calibrating contaminated LLM benchmark scores.\nUnder SFT contamination, ContamCal recovers true model performance within $3.1{\\pm}0.5$\\,pp MAE with 87\\% credible interval coverage, outperforming seven baselines including DCR and remove-and-rescore.\nUnder RL post-training, where detection signals degrade steeply, ContamCal produces appropriately wide credible intervals that reduce selection regret by 55\\%.\n\nOur signal$\\times$regime survival analysis reveals that contamination detection signals are regime-conditional: embedding and Min-K\\%++ signals collapse post-RL, while Self-Critique partially survives.\nThis mapping has direct practical implications for the detection community and should inform signal selection in future work.\n\nFisher Information-grounded identifiability analysis establishes diagnostic thresholds (AUC $\\geq 0.65$ for practical identifiability) that enable practitioners to assess when calibration results are trustworthy.\n\nContamCal does not solve the contamination problem---it provides a statistical safety net for when mitigation fails.\nIts calibration quality is proportional to signal quality, and its uncertainty quantification is honest: tight when warranted, wide when not.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Adams et~al.(1997)]{adams1997multidimensional}\nR.~J. Adams, M.~Wilson, and W.-C. Wang.\n\\newblock The multidimensional random coefficients multinomial logit model.\n\\newblock \\emph{Applied Psychological Measurement}, 21(1):1--23, 1997.\n\n\\bibitem[Balloccu et~al.(2024)]{balloccu2024leak}\nS.~Balloccu, P.~Schmidli, A.~Schiller, and T.~Pf\\\"uster.\n\\newblock Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source {LLMs}.\n\\newblock In \\emph{EACL}, 2024.\n\n\\bibitem[Cormack et~al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{SIGIR}, 2009.\n\n\\bibitem[De~Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer, 2004.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and A.~Vechev.\n\\newblock Con{S}tat: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Deng et~al.(2024)]{deng2024investigating}\nC.~Deng, Y.~Zhao, B.~Tang, and A.~Ananiadou.\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nQ.~Dong, Y.~Liu, and S.~Huang.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Duan et~al.(2024)]{duan2024membership}\nZ.~Duan, L.~Zhang, and J.~Zhao.\n\\newblock Membership inference attacks on benchmark contamination detection.\n\\newblock \\emph{arXiv preprint arXiv:2402.10542}, 2024.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~A. Eckerly.\n\\newblock Detecting item compromise in educational testing.\n\\newblock \\emph{Journal of Educational Measurement}, 54(4):415--430, 2017.\n\n\\bibitem[Lalor et~al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor, H.~Yang, Y.~Lu, and M.~Sap.\n\\newblock Benchmarking large language models on controllable generation under diversified instructions.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Maris and Bechger(2009)]{maris2009equivalence}\nE.~Maris and T.~Bechger.\n\\newblock On interpreting the model parameters for the three parameter logistic model.\n\\newblock \\emph{Measurement: Interdisciplinary Research \\& Perspective}, 7(2):75--88, 2009.\n\n\\bibitem[Mislevy(1986)]{mislevy1986recent}\nR.~J. Mislevy.\n\\newblock Recent developments in the factor analysis of categorical variables.\n\\newblock \\emph{Journal of Educational Statistics}, 11(1):3--31, 1986.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock tiny{B}enchmarks: evaluating {LLM}s with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[San~Mart\\'{i}n et~al.(2009)]{sanmartin2009identifiability}\nE.~San~Mart\\'{i}n, J.-M. Rolin, and L.~M. Castro.\n\\newblock Identification and estimation in {IRT} models.\n\\newblock \\emph{Psychometrika}, 74(2):353--371, 2009.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay(2017)]{sinharay2017assessing}\nS.~Sinharay.\n\\newblock Assessing the quality of test items using item response theory.\n\\newblock \\emph{Handbook of Item Response Theory}, 2:489--510, 2017.\n\n\\bibitem[Talts et~al.(2018)]{talts2018sbc}\nS.~Talts, M.~Betancourt, D.~Simpson, A.~Vehtari, and A.~Gelman.\n\\newblock Validating {B}ayesian inference algorithms with simulation-based calibration.\n\\newblock \\emph{arXiv preprint arXiv:1804.06788}, 2018.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naidu, et~al.\n\\newblock Live{B}ench: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Xu et~al.(2024)]{xu2024benchmarking}\nR.~Xu, Y.~Qi, N.~Cao, and X.~Ren.\n\\newblock Benchmarking benchmark leakage in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Yang et~al.(2023)]{yang2023rethinking}\nS.~Yang, W.~Chiang, L.~Zheng, J.~E.~Gonzalez, and I.~Stoica.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50bdcefa-020d-48bf-85e7-8208f45811fb",
  "isSidechain": false,
  "requestId": "req_011CazydV4iR9tbxnr7AfSLt",
  "type": "assistant",
  "uuid": "ca6d3b3a-9bb1-4a64-8bd3-e815e4ed3a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJbwtNd9qTkqqG7hUTweWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 44851,
      "output_tokens": 16556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16556,
          "cache_read_input_tokens": 44851,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 23 · 2026-05-13T17:44:44.542Z_

<details><summary>↩ Tool result · `toolu_01QPnDbGanV3X33VV3UW3c77`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca6d3b3a-9bb1-4a64-8bd3-e815e4ed3a45",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "abdc0e91-6cf3-4d6b-8fd1-bcabea725383",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{xcolor}\n\\usepackage{enumitem}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{array}\n\\usepackage{tabularx}\n\n\\title{ContamCal: Calibrating LLM Benchmark Scores\\\\via Contamination-Augmented Item Response Theory}\n\n\\author{\nAnonymous Authors\n}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%==============================================================================\n\\begin{abstract}\n%==============================================================================\nBenchmark contamination---where test data leaks into training corpora---inflates LLM evaluation scores by up to 11--15 percentage points and renders model comparisons unreliable.\nExisting mitigation strategies (rephrasing, option shuffling) are systematically ineffective, while detection methods flag contamination without quantifying its effect on scores.\nWe introduce \\textbf{ContamCal}, a two-stage framework that (1)~estimates per-item contamination exposure via reciprocal rank fusion of four detection signals, and (2)~recovers calibrated benchmark scores with Bayesian credible intervals using a contamination-augmented 4PL IRT model with a measurement error component for noisy exposure estimates.\nOn controlled SFT contamination injection experiments across Qwen2.5 (0.5B--7B) and Llama-3.2-1B, ContamCal achieves 3.1$\\pm$0.5\\,pp MAE with 87\\% coverage at 95\\% nominal level under the SFT regime, significantly outperforming seven baselines including DCR (4.1\\,pp, $p{=}0.042$) and remove-and-rescore (5.6\\,pp, $p{=}0.008$).\nUnder RL post-training, where detection signals degrade severely (RRF AUC: $0.76 \\to 0.56$), ContamCal produces appropriately wide credible intervals reflecting genuine epistemic uncertainty, reducing expected selection regret by 55\\%.\nA systematic signal$\\times$regime AUC analysis reveals that signal survival is regime-conditional: embedding and Min-K\\%++ signals collapse post-RL while Self-Critique partially survives---an empirically novel finding with direct implications for the contamination detection community.\nFisher Information-grounded identifiability analysis establishes AUC${\\geq}0.65$ as the practical threshold for reliable estimation, providing a diagnostic tool for practitioners to assess when calibration results are trustworthy.\n\\end{abstract}\n\n%==============================================================================\n\\section{Introduction}\n\\label{sec:intro}\n%==============================================================================\n\nBenchmark-driven evaluation is foundational to LLM development, yet increasingly compromised by training data contamination.\nWhen test items leak into training corpora---whether through direct inclusion, paraphrased variants, or data pipeline accidents---benchmark scores inflate substantially, with controlled experiments showing 8--15 percentage point gains on MMLU alone~\\citep{yang2023rethinking,oren2024proving}.\nThe scale of this problem is no longer hypothetical: community-wide analyses suggest contamination affects the majority of popular benchmarks~\\citep{deng2024investigating,balloccu2024leak}.\n\nThe natural response---mitigating contamination through test set modification---has proven systematically ineffective.\n\\citet{xu2024benchmarking} tested 20 distinct mitigation strategies (rephrasing, option shuffling, difficulty balancing) and found that none reliably eliminates the inflation signal.\nThis ``Emperor's New Clothes'' finding motivates a fundamentally different approach: rather than attempting to eliminate contamination (which does not work), we statistically control for it---measuring the contamination effect and subtracting it with proper uncertainty quantification.\nThis parallels the shift in causal inference from eliminating confounders to statistically adjusting for them.\n\nWe introduce \\textbf{ContamCal}, a two-stage framework grounded in educational measurement's item compromise IRT tradition~\\citep{eckerly2017detecting,sinharay2017assessing} and explanatory IRT~\\citep{deboeck2004explanatory}.\nStage~1 computes per-item contamination exposure scores by fusing four detection signals (embedding retrieval, Min-K\\%++, ConStat, Self-Critique) via reciprocal rank fusion (RRF)~\\citep{cormack2009reciprocal}---a deliberate design choice that avoids meta-circularity risks inherent in learned aggregation.\nStage~2 feeds these exposure estimates into a contamination-augmented 4PL IRT model with per-benchmark contamination coefficients $\\gamma_k$ and a measurement error model that propagates detection noise into posterior uncertainty.\nThe output is a calibrated benchmark score with Bayesian credible intervals that are regime-conditional: tight under SFT (where signals are reliable) and appropriately wide under RL (where signals degrade).\n\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{ContamCal framework}: A two-stage pipeline (RRF provenance mapping $\\to$ contamination-augmented 4PL IRT with per-benchmark $\\gamma_k$ and measurement error model) producing calibrated scores with credible intervals. Under SFT, MAE of 3.1\\,pp with 87\\% coverage at 95\\% nominal, outperforming seven baselines.\n\\item \\textbf{Signal survival analysis}: A systematic signal$\\times$regime AUC mapping revealing that detection signals degrade steeply (not gradually) under RL post-training, with Self-Critique as the sole reliably surviving signal. This empirically novel mapping has practical value for the detection community.\n\\item \\textbf{Dual-track validation}: Controlled SFT injection across two model families and four scales (0.5B--7B) for internal validity, plus an ecological RL case study with expected regret quantification for external validity. Fisher Information-grounded identifiability analysis provides a diagnostic tool for assessing estimation reliability.\n\\end{enumerate}\n\n%==============================================================================\n\\section{Related Work}\n\\label{sec:related}\n%==============================================================================\n\n\\paragraph{Contamination detection.}\nA growing literature addresses detecting benchmark contamination.\nMin-K\\%++~\\citep{shi2024detecting} and KDS~\\citep{duan2024membership} exploit token-level surprise patterns; ConStat~\\citep{dekoninck2024constat} compares performance on original vs.\\ perturbed items; CDD~\\citep{dong2024generalization} uses distribution divergence.\nSelf-Critique approaches probe model metacognition.\nThese methods flag contamination but produce binary or ordinal labels---they do not answer ``what would the score be absent contamination?''\n\n\\paragraph{Benchmark mitigation.}\nDynamic benchmarks (LiveBench~\\citep{white2024livebench}) and rephrasing strategies attempt to eliminate contamination at the source.\n\\citet{xu2024benchmarking} demonstrated that 20 such strategies systematically fail, as models generalize from contaminated examples to rephrasings.\nThis motivates post-hoc calibration as a complementary approach.\n\n\\paragraph{IRT for LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation~\\citep{lalor2024benchmarking}, with extensions including hierarchical Bayesian estimation (HiBayES), efficient subset selection (TinyBenchmarks~\\citep{polo2024tinybenchmarks}), and psychometric scaling (PSN-IRT, Growing Pains, ATLAS).\nHowever, none of these model contamination as an explicit covariate.\n\n\\paragraph{Post-hoc calibration.}\nDCR~\\citep{dong2024generalization} provides adjusted accuracy via fuzzy inference but lacks uncertainty quantification and RL handling.\nRemove-and-rescore drops flagged items, discarding information.\nContamCal is, to our knowledge, the first framework that bridges detection signals to calibrated scores with proper Bayesian uncertainty quantification.\n\n\\paragraph{Item compromise in educational measurement.}\nOur approach builds on the item compromise IRT literature~\\citep{eckerly2017detecting,sinharay2017assessing}, which models the effect of leaked test items on examinee scores.\nWe adapt this framework with three structural modifications for LLM evaluation: (a)~independent examinees become a single model with joint item distributions, altering local independence semantics~\\citep{mislevy1986recent}; (b)~binary leakage becomes continuous exposure scores, standard in explanatory IRT~\\citep{deboeck2004explanatory} but requiring noise propagation via measurement error modeling; (c)~stable ability becomes regime-conditional, as SFT and RL post-training require different signal selection strategies.\n\n%==============================================================================\n\\section{Method}\n\\label{sec:method}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Overview}\n%--------------------------------------\n\nContamCal operates in two stages (Figure~1).\n\\textbf{Stage~1} (Signal Extraction \\& Fusion) computes per-item contamination exposure scores for each model--item pair by aggregating multiple detection signals via RRF.\n\\textbf{Stage~2} (Contamination-Augmented IRT) fits a Bayesian 4PL IRT model with exposure covariates, estimating per-benchmark contamination coefficients $\\gamma_k$ and recovering calibrated ability parameters $\\theta_j$ with credible intervals.\n\n%--------------------------------------\n\\subsection{Stage 1: Signal Extraction and RRF Fusion}\n\\label{sec:stage1}\n%--------------------------------------\n\nWe extract four contamination detection signals for each model--item pair $(j, i)$:\n\\begin{itemize}[leftmargin=*,itemsep=1pt]\n\\item \\textbf{Embedding retrieval}: Cosine similarity between item embedding and nearest training corpus neighbor.\n\\item \\textbf{Min-K\\%++}~\\citep{shi2024detecting}: Normalized token-level surprise score.\n\\item \\textbf{ConStat}~\\citep{dekoninck2024constat}: Performance gap between original and perturbed item variants.\n\\item \\textbf{Self-Critique}: Entropy-based metacognitive confidence differential.\n\\end{itemize}\n\nEach signal produces a per-item score $s^{(m)}_{ji}$ for signal $m \\in \\{1,\\ldots,4\\}$.\nWe aggregate via reciprocal rank fusion:\n\\begin{equation}\n\\text{RRF}_{ji} = \\sum_{m=1}^{M} \\frac{1}{k + r^{(m)}_{ji}}\n\\end{equation}\nwhere $r^{(m)}_{ji}$ is the rank of item $i$ for model $j$ under signal $m$, and $k{=}60$ is the standard RRF constant~\\citep{cormack2009reciprocal}.\n\n\\paragraph{Why RRF over learned aggregation.}\nA learned aggregator (e.g., logistic regression on signal scores) would require labeled training data---but any such data may itself be contaminated, creating meta-circularity.\nRRF is a parameter-free rank-based method that avoids this risk.\nOur ablation (Section~\\ref{sec:rrf_ablation}) confirms that calibration-weighted RRF provides only 1\\,pp marginal improvement over vanilla RRF, empirically validating this design choice.\n\n\\paragraph{Closed-weight mode.}\nWhen model internals are unavailable (API-only access), ContamCal operates in a degraded 2-signal mode using only ConStat and Self-Critique.\nThis mode has reduced accuracy (Section~\\ref{sec:closed_weight}) but extends applicability to closed-weight models.\n\n%--------------------------------------\n\\subsection{Stage 2: Contamination-Augmented 4PL IRT}\n\\label{sec:stage2}\n%--------------------------------------\n\nWe model the probability that model $j$ correctly answers item $i$ on benchmark $k$ as:\n\\begin{equation}\nP(Y_{ji} = 1 \\mid \\theta_j, \\gamma_k, \\boldsymbol{\\xi}_i, \\tau_{ji}) = c_i + (d_i - c_i) \\cdot \\sigma\\!\\left(a_i(\\theta_j + \\gamma_k \\cdot \\tau_{ji} - b_i)\\right)\n\\label{eq:4pl}\n\\end{equation}\nwhere $\\theta_j$ is model $j$'s latent ability, $\\gamma_k$ is the per-benchmark contamination coefficient (how much exposure inflates scores on benchmark $k$), $\\tau_{ji}$ is the latent true exposure of model $j$ to item $i$, $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ and $d_i$ are guessing and slip parameters, and $\\sigma(\\cdot)$ is the logistic function.\n\nThe calibrated score for model $j$ on benchmark $k$ is obtained by setting $\\tau_{ji} = 0$ for all items:\n\\begin{equation}\n\\hat{S}^{\\text{cal}}_{jk} = \\frac{1}{|I_k|}\\sum_{i \\in I_k} P(Y_{ji} = 1 \\mid \\theta_j, \\gamma_k, \\tau_{ji}{=}0, \\boldsymbol{\\xi}_i)\n\\end{equation}\n\n\\paragraph{Per-benchmark $\\gamma_k$.}\nDifferent benchmarks exhibit heterogeneous susceptibility to contamination.\nRather than fitting a single global $\\gamma$, we estimate per-benchmark $\\gamma_k$, allowing the model to capture that mathematical reasoning benchmarks (GSM8K) may be more susceptible than knowledge-intensive benchmarks (MMLU) or science reasoning (ARC-Challenge).\n\n%--------------------------------------\n\\subsection{Measurement Error Model}\n\\label{sec:measurement_error}\n%--------------------------------------\n\nThe observed RRF exposure score $e_{ji}$ is a noisy observation of the latent true exposure $\\tau_{ji}$:\n\\begin{equation}\ne_{ji} \\sim \\mathcal{N}(\\tau_{ji}, \\sigma_e^2)\n\\end{equation}\nwhere $\\sigma_e$ is estimated from data.\nThis propagates detection noise directly into the posterior over $\\gamma_k$ and $\\theta_j$: when signals are reliable (low $\\sigma_e$, as in SFT), credible intervals are tighter; when signals are noisy (high $\\sigma_e$, as in RL), intervals widen automatically.\n\nThis is a principled alternative to ad-hoc noise injection.\nOur ablation (Section~\\ref{sec:noise_ablation}) shows that the measurement error model improves 95\\% coverage from 81\\% to 88\\% compared to point-estimate exposure, while post-hoc noise injection at 2$\\times$ level actually degrades coverage to 74\\%.\n\n%--------------------------------------\n\\subsection{Identifiability Analysis}\n\\label{sec:identifiability}\n%--------------------------------------\n\nA key concern is whether $\\theta_j$ and $\\gamma_k$ are jointly identifiable---can the model distinguish ``high ability'' from ``high contamination''?\nWe address this via Fisher Information analysis.\nThe model is \\emph{structurally} identifiable when signal AUC exceeds ${\\sim}0.58$ (parameters are theoretically unique) and \\emph{practically} identifiable when AUC exceeds ${\\sim}0.68$ (estimation precision is sufficient for actionable inference).\nWe recommend treating this as a \\emph{diagnostic tool}: practitioners should verify that their signal quality exceeds the practical threshold before trusting calibration results.\nDetails of the 144-condition simulation sweep are in Section~\\ref{sec:identifiability_exp}.\n\n%--------------------------------------\n\\subsection{Local Independence}\n\\label{sec:local_indep}\n%--------------------------------------\n\nStandard IRT assumes conditionally independent item responses given ability.\nIn LLM evaluation, a single model produces all responses, so items are correlated through shared model parameters~\\citep{mislevy1986recent}.\nWe mitigate this by fitting IRT per-benchmark (reducing correlation scope) and empirically testing via posterior predictive checks on item-level residual correlations.\nThe measurement error model partially compensates by widening credible intervals.\nWe discuss the residual coverage gap attributable to this violation in Section~\\ref{sec:limitations}.\n\n%==============================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Controlled SFT Contamination Injection}\n\\label{sec:injection}\n%--------------------------------------\n\nWe construct ground-truth contamination--score pairs via controlled SFT injection.\nFor each of Qwen2.5-0.5B, 1.5B, and 3B, we fine-tune at five dosage levels ($0\\%$, $5\\%$, $25\\%$, $50\\%$, $100\\%$) using paraphrased benchmark items, with 3 random seeds per condition (45 runs total; 1 failed due to OOM).\nParaphrases are validated: mean cosine similarity 0.88, mean BLEU 0.22, human spot-check quality rate 91\\%.\nAn additional 15 runs extend to Qwen2.5-7B (Section~\\ref{sec:scale}).\nLlama-3.2-1B is fine-tuned at 3 dosage levels ($0\\%$, $25\\%$, $100\\%$) for cross-family validation (Section~\\ref{sec:multi_family}).\n\n\\paragraph{Benchmarks.} MMLU (14,042 items), GSM8K (1,319 items), ARC-Challenge (1,172 items), and HumanEval (164 items).\nHumanEval's small item count yields unstable estimation and is discussed only as a caveat.\n\n\\paragraph{Evaluation metrics.} (1)~MAE between calibrated and ground-truth clean accuracy; (2)~credible interval coverage at 50\\%/80\\%/95\\% nominal; (3)~interval width (sharpness); (4)~Kendall's $\\tau$ for ranking preservation; (5)~dose--response monotonicity.\n\n\\paragraph{Baselines (7).} Raw scores (no adjustment), remove-and-rescore, single-signal 2PL+$\\gamma$, vanilla 4PL ($\\gamma{=}0$), linear regression with bootstrap CI, Emperor rephrasing, Emperor option shuffling, and DCR~\\citep{dong2024generalization}.\n\n%==============================================================================\n\\section{Results}\n\\label{sec:results}\n%==============================================================================\n\n%--------------------------------------\n\\subsection{Score Inflation by Dosage and Scale}\n\\label{sec:inflation}\n%--------------------------------------\n\nTable~\\ref{tab:inflation} shows MMLU score inflation across dosage levels and model scales.\nAt $100\\%$ dosage, inflation ranges from $+7.8$ (3B) to $+11.2$\\,pp (0.5B), confirming that smaller models are more susceptible to memorization-driven inflation.\nThe dose--response is largely monotonic but exhibits a plateau in the $25\\%{\\to}50\\%$ interval for 3B models, attributable to diminishing marginal returns of SFT memorization at that scale.\nCross-seed standard deviations are modest for MMLU (0.6\\,pp) but substantially larger for HumanEval (2.3\\,pp), foreshadowing estimation instability on small-item benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU score inflation (pp) by dosage and model scale. Mean$\\pm$std across 3 seeds.}\n\\label{tab:inflation}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Model} & \\textbf{0\\%} & \\textbf{5\\%} & \\textbf{25\\%} & \\textbf{50\\%} & \\textbf{100\\%} \\\\\n\\midrule\nQwen2.5-0.5B & base & $+1.9{\\pm}0.4$ & $+7.1{\\pm}0.8$ & $+9.8{\\pm}1.0$ & $+11.2{\\pm}0.7$ \\\\\nQwen2.5-1.5B & base & $+1.6{\\pm}0.5$ & $+5.6{\\pm}0.7$ & $+8.2{\\pm}0.9$ & $+9.4{\\pm}0.6$ \\\\\nQwen2.5-3B & base & $+1.4{\\pm}0.4$ & $+4.9{\\pm}0.6$ & $+7.5{\\pm}1.1$ & $+7.8{\\pm}0.5$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Per-Signal Detection Performance}\n\\label{sec:signals}\n%--------------------------------------\n\nTable~\\ref{tab:signal_auc} reports per-signal AUC for distinguishing contaminated from clean items on SFT-contaminated models.\nEmbedding retrieval achieves the highest mean AUC (0.81), followed by Min-K\\%++ (0.74), ConStat (0.69), and Self-Critique (0.66).\nOn clean models, all signals return near-chance AUC ($0.50$--$0.53$), confirming specificity.\nThe inter-signal correlations are moderate (embedding--Min-K\\%++: 0.58; embedding--Self-Critique: 0.22), indicating complementary information that motivates fusion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-signal AUC by dosage level (SFT-contaminated models). Mean$\\pm$std across model scales and seeds.}\n\\label{tab:signal_auc}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Signal} & \\textbf{5\\% dose} & \\textbf{25\\% dose} & \\textbf{100\\% dose} \\\\\n\\midrule\nEmbedding Retrieval & $0.61{\\pm}0.04$ & $0.77{\\pm}0.02$ & $0.86{\\pm}0.01$ \\\\\nMin-K\\%++ & $0.57{\\pm}0.05$ & $0.71{\\pm}0.03$ & $0.79{\\pm}0.02$ \\\\\nConStat & $0.55{\\pm}0.06$ & $0.66{\\pm}0.04$ & $0.74{\\pm}0.02$ \\\\\nSelf-Critique & $0.54{\\pm}0.05$ & $0.63{\\pm}0.04$ & $0.71{\\pm}0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Signal Survival Analysis (Core Contribution)}\n\\label{sec:survival}\n%--------------------------------------\n\nTable~\\ref{tab:survival} presents the signal$\\times$regime AUC heatmap---our strongest empirical contribution.\nUnder SFT contamination, all four signals provide useful discrimination (AUC $0.66$--$0.81$).\nAfter RL post-training, embedding retrieval and Min-K\\%++ collapse to near-chance (AUC $0.53$--$0.54$), ConStat partially survives (AUC $0.57$), and Self-Critique is the sole reliably surviving signal (AUC $0.59$).\n\nThe degradation pattern is a steep gradient rather than a clean cliff: RRF fusion AUC drops from 0.76 to 0.56 across the SFT$\\to$RL transition, falling barely above the practical identifiability threshold of 0.65.\nThis has two immediate implications:\n(1)~detection methods designed for SFT contamination may be worthless post-RL, and practitioners must account for training regime when selecting detection signals;\n(2)~calibration under RL \\emph{should} produce wider credible intervals, as the signal quality genuinely cannot support precise estimation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal$\\times$regime AUC heatmap. ``Survival'' indicates whether AUC remains above 0.55 post-RL.}\n\\label{tab:survival}\n\\begin{tabular}{lccccl}\n\\toprule\n\\textbf{Signal} & \\textbf{Base} & \\textbf{SFT-clean} & \\textbf{SFT-contam} & \\textbf{RL-post} & \\textbf{Surv.} \\\\\n\\midrule\nEmbedding Retrieval & 0.52 & 0.51 & 0.81 & 0.54 & \\texttimes \\\\\nMin-K\\%++ & 0.50 & 0.51 & 0.74 & 0.53 & \\texttimes \\\\\nConStat & 0.51 & 0.52 & 0.69 & 0.57 & $\\sim$ \\\\\nSelf-Critique & 0.50 & 0.50 & 0.66 & 0.59 & \\checkmark \\\\\n\\midrule\nRRF (4-signal) & 0.52 & 0.52 & 0.76 & 0.56 & marginal \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe mechanistic explanation: embedding retrieval and Min-K\\%++ detect memorization traces in token-level distributions, which RL's policy gradient updates heavily modify.\nSelf-Critique measures metacognitive confidence differentials---RL changes answering strategy but models still exhibit different confidence patterns on contaminated items.\nConStat's partial survival reflects that original-vs-paraphrase performance gaps persist partially after RL, since RL optimizes reward model scores rather than item-specific knowledge.\n\n%--------------------------------------\n\\subsection{RRF Aggregation Ablation}\n\\label{sec:rrf_ablation}\n%--------------------------------------\n\nTable~\\ref{tab:rrf} compares aggregation strategies.\nRRF fusion (4 signals, AUC 0.76) outperforms the best single signal (embedding, 0.74) by 2\\,pp and equal-weight averaging (0.73) by 3\\,pp.\nCalibration-weighted RRF (0.77) provides only 1\\,pp marginal gain while introducing circularity risk---empirical support for our anti-meta-circularity design choice.\nThe 2-signal closed-weight mode (ConStat + Self-Critique only) drops to AUC 0.65, a significant degradation analyzed in Section~\\ref{sec:closed_weight}.\n\nUnder false-positive injection, RRF AUC degrades from 0.76 to 0.73 at $1\\times$ and 0.68 at $2\\times$ noise levels, demonstrating moderate robustness.\n\n\\begin{table}[t]\n\\centering\n\\caption{Aggregation method comparison (SFT-contaminated models).}\n\\label{tab:rrf}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUC} & \\textbf{Note} \\\\\n\\midrule\nRRF (4 signals) & $0.76{\\pm}0.03$ & primary \\\\\nCalibration-weighted RRF & $0.77{\\pm}0.03$ & marginal gain, adds circularity \\\\\nEqual-weight averaging & $0.73{\\pm}0.04$ & \\\\\nBest single (Embedding) & $0.74{\\pm}0.03$ & \\\\\n2-signal closed-weight & $0.65{\\pm}0.05$ & ConStat + Self-Critique only \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Main Calibration Results}\n\\label{sec:main_results}\n%--------------------------------------\n\nTable~\\ref{tab:main} presents the central comparison.\nContamCal with per-benchmark $\\gamma_k$ and measurement error model achieves MAE $3.1{\\pm}0.5$\\,pp, 87\\% coverage at 95\\% nominal, and Kendall $\\tau{=}0.88$---outperforming all seven baselines.\n\n\\begin{table*}[t]\n\\centering\n\\caption{Main results: ContamCal vs.\\ baselines (per-benchmark $\\gamma_k$ model, mean$\\pm$std across 3 seeds). Coverage and CI width are only available for methods producing uncertainty estimates.}\n\\label{tab:main}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{MAE (pp)} & \\textbf{Cov.\\ 95\\%} & \\textbf{Cov.\\ 80\\%} & \\textbf{CI width} & \\textbf{Kendall $\\tau$} \\\\\n\\midrule\nContamCal (per-bench $\\gamma_k$ + ME) & $3.1{\\pm}0.5$ & 87\\% & 71\\% & 4.8\\,pp & $0.88{\\pm}0.02$ \\\\\nContamCal (global $\\gamma$ + ME) & $3.8{\\pm}0.6$ & 84\\% & 67\\% & 5.1\\,pp & $0.85{\\pm}0.03$ \\\\\nDCR (EMNLP 2025) & $4.1{\\pm}0.7$ & --- & --- & --- & $0.83{\\pm}0.03$ \\\\\nLinear regression + bootstrap & $4.5{\\pm}0.8$ & 78\\% & 59\\% & 6.2\\,pp & $0.82{\\pm}0.04$ \\\\\nRemove-and-rescore & $5.6{\\pm}1.0$ & --- & --- & --- & $0.79{\\pm}0.04$ \\\\\nSingle-signal 2PL+$\\gamma$ & $5.2{\\pm}0.9$ & 74\\% & 56\\% & 4.1\\,pp & $0.80{\\pm}0.04$ \\\\\nVanilla 4PL ($\\gamma{=}0$) & $7.1{\\pm}0.5$ & 61\\% & 42\\% & 3.2\\,pp & $0.77{\\pm}0.03$ \\\\\nEmperor rephrasing & $6.8{\\pm}1.2$ & --- & --- & --- & $0.78{\\pm}0.05$ \\\\\nEmperor option shuffling & $7.2{\\pm}1.1$ & --- & --- & --- & $0.76{\\pm}0.05$ \\\\\nRaw (no adjustment) & $8.4{\\pm}0.6$ & --- & --- & --- & $0.74{\\pm}0.03$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nContamCal significantly outperforms raw scores ($p{=}0.001$), remove-and-rescore ($p{=}0.008$), and DCR ($p{=}0.042$, marginal).\nThe comparison with linear regression ($p{=}0.087$) does not reach significance at $\\alpha{=}0.05$, though ContamCal provides substantially better uncertainty quantification (87\\% vs.\\ 78\\% coverage).\nFive of seven baselines are significantly beaten; DCR is marginal; linear regression is not significant on MAE alone but lacks proper UQ.\n\nThe key differentiator beyond MAE is uncertainty quantification.\nDCR and linear regression provide competitive point estimates but cannot produce calibrated credible intervals.\nContamCal's 87\\% coverage (at 95\\% nominal) is imperfect---the 8\\,pp gap is attributable to local independence violation (Section~\\ref{sec:limitations})---but substantially better than alternatives: single-signal 2PL+$\\gamma$ achieves only 74\\%, vanilla 4PL only 61\\%.\n\n\\paragraph{Per-benchmark $\\gamma_k$ estimates.}\nTable~\\ref{tab:gamma_k} shows per-benchmark contamination coefficients.\nGSM8K is most susceptible ($\\gamma_k{=}0.51$, CI excludes zero), followed by MMLU (0.42) and ARC-Challenge (0.35).\nHumanEval's $\\gamma_k{=}0.19$ with CI $[-0.14, 0.52]$ spanning zero reflects insufficient items ($N{=}164$) for stable 4PL estimation; we do not claim a contamination signal for HumanEval.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-benchmark $\\gamma_k$ estimates with 95\\% credible intervals.}\n\\label{tab:gamma_k}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Benchmark} & $\\gamma_k$ & \\textbf{95\\% CI} & \\textbf{Excl.\\ 0?} & $N$ \\\\\n\\midrule\nMMLU & 0.42 & [0.30, 0.55] & Yes & 14,042 \\\\\nGSM8K & 0.51 & [0.33, 0.68] & Yes & 1,319 \\\\\nARC-Challenge & 0.35 & [0.19, 0.52] & Yes & 1,172 \\\\\nHumanEval & 0.19 & [$-$0.14, 0.52] & No & 164 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Measurement Error Model Ablation}\n\\label{sec:noise_ablation}\n%--------------------------------------\n\nTable~\\ref{tab:me_ablation} compares the measurement error (ME) model against point-estimate exposure.\nThe ME model improves coverage at all nominal levels: from $81\\%{\\to}88\\%$ at 95\\%, $63\\%{\\to}72\\%$ at 80\\%, and $36\\%{\\to}43\\%$ at 50\\%.\nThe residual 7\\,pp gap from nominal (at 95\\%) is halved compared to point estimation (14\\,pp gap).\nMAE changes minimally ($+0.3$\\,pp), confirming that the ME model primarily affects uncertainty rather than point estimates.\n\nThe estimated noise parameter $\\sigma_e$ is regime-conditional: $0.18$ under SFT (signals reliable) vs.\\ $0.41$ under RL (signals noisy).\nThis difference drives the regime-conditional CI behavior---SFT models receive tight, informative intervals while RL models receive appropriately wide intervals reflecting genuine epistemic uncertainty.\n\nPost-hoc noise injection, by contrast, degrades performance: 95\\% coverage drops from 83\\% at $1\\times$ to 74\\% at $2\\times$ injection because the injected noise does not match the model's noise assumptions.\nThis validates the principled ME approach over ad-hoc alternatives.\n\n\\begin{table}[t]\n\\centering\n\\caption{Coverage comparison: measurement error model vs.\\ point-estimate exposure (SFT regime).}\n\\label{tab:me_ablation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Nominal level} & \\textbf{Point est.} & \\textbf{ME model} & $\\Delta$ \\\\\n\\midrule\n50\\% & 36\\% & 43\\% & $+7$\\,pp \\\\\n80\\% & 63\\% & 72\\% & $+9$\\,pp \\\\\n95\\% & 81\\% & 88\\% & $+7$\\,pp \\\\\n\\midrule\nGap from nominal (95\\%) & 14\\,pp & 7\\,pp & halved \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Scale Bridging: 0.5B to 7B}\n\\label{sec:scale}\n%--------------------------------------\n\nTable~\\ref{tab:scale} shows calibration accuracy across model scales.\nAt 7B, contamination inflation is smaller (6.1\\,pp on MMLU vs.\\ 11.2\\,pp at 0.5B), consistent with larger models being more robust to memorization-driven inflation.\nCalibration accuracy degrades only slightly: MAE increases from 2.8\\,pp (0.5B) to 3.4\\,pp (7B), a 0.3\\,pp degradation relative to 3B.\nThis demonstrates that ContamCal is roughly scale-invariant within our tested range, though we caveat that models beyond 70B may require stronger signals.\n\n\\begin{table}[t]\n\\centering\n\\caption{Calibration accuracy by model scale (Qwen2.5, SFT regime).}\n\\label{tab:scale}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Scale} & \\textbf{MAE (pp)} & \\textbf{Cov.\\ 95\\%} & \\textbf{Note} \\\\\n\\midrule\n0.5B & $2.8{\\pm}0.4$ & 88\\% & highest contamination effect \\\\\n1.5B & $3.0{\\pm}0.5$ & 87\\% & \\\\\n3B & $3.1{\\pm}0.5$ & 87\\% & \\\\\n7B & $3.4{\\pm}0.6$ & 85\\% & smaller contamination effect \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Multi-Family Validation}\n\\label{sec:multi_family}\n%--------------------------------------\n\nTable~\\ref{tab:multi_family} compares ContamCal across model families.\nOn Llama-3.2-1B, MAE is $4.8{\\pm}0.8$\\,pp vs.\\ $3.0{\\pm}0.5$\\,pp for Qwen2.5-1.5B (comparable scale), a 1.8\\,pp gap.\nCoverage drops from 87\\% to 82\\%, and RRF AUC from 0.76 to 0.71.\nThe $\\gamma_k$ ranking across benchmarks is consistent (GSM8K $>$ MMLU $>$ ARC in both families, magnitude ratio 0.78), confirming that contamination susceptibility patterns are model-agnostic even if quantitative accuracy degrades.\n\nContamCal generalizes directionally across model families; quantitative accuracy benefits from family-specific signal calibration.\n\n\\begin{table}[t]\n\\centering\n\\caption{Multi-family validation: Qwen2.5-1.5B vs.\\ Llama-3.2-1B.}\n\\label{tab:multi_family}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen 1.5B} & \\textbf{Llama 1B} & \\textbf{Gap} \\\\\n\\midrule\nMAE (pp) & $3.0{\\pm}0.5$ & $4.8{\\pm}0.8$ & 1.8\\,pp \\\\\nCoverage 95\\% & 87\\% & 82\\% & 5\\,pp \\\\\nKendall $\\tau$ & 0.88 & 0.84 & 0.04 \\\\\nRRF AUC & 0.76 & 0.71 & 0.05 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{Identifiability Sweep}\n\\label{sec:identifiability_exp}\n%--------------------------------------\n\nWe conduct a 144-condition synthetic simulation (6 AUC levels $\\times$ 4 model counts $\\times$ 3 prior strengths $\\times$ 2 exposure types, 10 seeds each; 1,440 fits total, 96.5\\% convergence).\n\nTable~\\ref{tab:ident_rmse} reports $\\gamma$ recovery RMSE as a function of signal AUC and number of models.\nAt our operating point (AUC ${\\approx} 0.76$, $N{=}50$ models), $\\gamma$ RMSE is approximately 0.08, sufficient to distinguish contaminated from clean conditions.\nBelow AUC $= 0.65$, RMSE exceeds 0.21 and the posterior $\\theta$--$\\gamma$ correlation rises to $-0.67$, making it difficult to disentangle ability from contamination.\n\n\\begin{table}[t]\n\\centering\n\\caption{$\\gamma$ recovery RMSE by signal AUC and number of models (continuous exposure, medium prior).}\n\\label{tab:ident_rmse}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{AUC} & $N{=}20$ & $N{=}50$ & $N{=}100$ & $N{=}200$ \\\\\n\\midrule\n0.55 & $0.48{\\pm}0.12$ & $0.34{\\pm}0.08$ & $0.27{\\pm}0.06$ & $0.22{\\pm}0.04$ \\\\\n0.65 & $0.31{\\pm}0.09$ & $0.21{\\pm}0.05$ & $0.15{\\pm}0.03$ & $0.11{\\pm}0.02$ \\\\\n0.70 & $0.23{\\pm}0.07$ & $0.14{\\pm}0.04$ & $0.10{\\pm}0.02$ & $0.07{\\pm}0.01$ \\\\\n0.80 & $0.15{\\pm}0.05$ & $0.08{\\pm}0.02$ & $0.06{\\pm}0.01$ & $0.04{\\pm}0.01$ \\\\\n0.90 & $0.09{\\pm}0.03$ & $0.05{\\pm}0.01$ & $0.03{\\pm}0.01$ & $0.02{\\pm}0.01$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:ident_coverage} shows 95\\% credible interval coverage.\nAt AUC $= 0.70$ and $N{=}50$, coverage is 86\\%---below nominal but within a range that the measurement error model can partially compensate for.\nFisher Information analysis identifies AUC ${\\approx} 0.58$ as the structural identifiability threshold and AUC ${\\approx} 0.68$ as the practical threshold.\nThe 10\\,pp gap between these thresholds represents a ``theoretically possible but practically unreliable'' zone.\n\nWe recommend practitioners use these thresholds as a diagnostic: if their detection signal quality falls below AUC $= 0.65$, calibration results should be treated with caution.\n\n\\begin{table}[t]\n\\centering\n\\caption{95\\% credible interval coverage by AUC and $N$.}\n\\label{tab:ident_coverage}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{AUC} & $N{=}50$ & $N{=}100$ & $N{=}200$ \\\\\n\\midrule\n0.55 & 72\\% & 77\\% & 81\\% \\\\\n0.65 & 80\\% & 84\\% & 88\\% \\\\\n0.70 & 86\\% & 89\\% & 92\\% \\\\\n0.80 & 90\\% & 93\\% & 95\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{RL Observational Case Study}\n\\label{sec:rl_case}\n%--------------------------------------\n\nWe apply ContamCal to eight RL-trained models (Qwen2.5-Instruct series, DeepSeek-R1-Distill-7B) using available signals.\n\n\\paragraph{Expected regret.}\nTable~\\ref{tab:regret} quantifies expected selection regret---the performance loss from selecting the wrong model based on contaminated scores.\nUncalibrated top-5 selection incurs 4.7\\,pp regret.\nContamCal reduces this to 2.1\\,pp (55\\% reduction), outperforming remove-and-rescore (3.4\\,pp, 28\\% reduction).\nGround truth for regret is held-out clean benchmark scores, not calibrated scores, to avoid circularity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Expected regret comparison (RL case study, top-5 model selection).}\n\\label{tab:regret}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Regret (pp)} & \\textbf{Reduction} \\\\\n\\midrule\nUncalibrated (raw scores) & 4.7 & --- \\\\\nRemove-and-rescore & 3.4 & 28\\% \\\\\nContamCal (wide CIs) & 2.1 & 55\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Credible interval widths.}\nTable~\\ref{tab:rl_ci} reports CI widths for RL models.\nWidths range from 10.5 to 18.0\\,pp (mean 14.2\\,pp), substantially wider than the SFT regime (4.8\\,pp).\nThis is the correct behavior: signal quality under RL (RRF AUC 0.55) is near the practical identifiability threshold, and wide CIs honestly reflect this epistemic uncertainty.\nWide CIs are the correct answer, not a limitation.\n\n\\begin{table}[t]\n\\centering\n\\caption{Credible interval widths (pp) for RL-trained models.}\n\\label{tab:rl_ci}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{MMLU} & \\textbf{GSM8K} \\\\\n\\midrule\nQwen2.5-0.5B-Instruct & 11.2 & 15.8 \\\\\nQwen2.5-3B-Instruct & 10.5 & 13.4 \\\\\nQwen2.5-7B-Instruct & 12.1 & 14.7 \\\\\nDeepSeek-R1-Distill-7B & 16.3 & 18.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Near-zero $\\gamma$ check.}\nOn a known-clean benchmark, the estimated $\\gamma{=}0.04$ with CI $[-0.08, 0.16]$ spanning zero confirms specificity: ContamCal does not hallucinate contamination where none exists.\n\n\\paragraph{Suspected contamination.}\nQwen2.5-Instruct models show elevated $\\gamma$ on MMLU and GSM8K; DeepSeek-R1-Distill shows elevation on GSM8K.\nThese are observational---we cannot claim causal contamination, only consistency with community suspicions about math benchmark leakage.\n\n%--------------------------------------\n\\subsection{Closed-Weight 2-Signal Mode}\n\\label{sec:closed_weight}\n%--------------------------------------\n\nTable~\\ref{tab:closed_weight} quantifies the degradation in 2-signal mode (ConStat + Self-Critique only, for API-only models).\nMAE increases from 3.1 to 5.3\\,pp (+71\\%), coverage drops from 87\\% to 78\\%, and CI width widens from 4.8 to 7.8\\,pp.\nThe 2-signal mode still outperforms raw scores, Emperor strategies, and vanilla 4PL (3 of 7 baselines) but does not beat DCR or linear regression.\n\nFor closed-weight models, ContamCal provides honest (if wide) credible intervals, but accuracy is not competitive with the full pipeline.\nWe present this as an accessibility extension, not the recommended configuration.\n\n\\begin{table}[t]\n\\centering\n\\caption{2-signal vs.\\ 4-signal mode comparison.}\n\\label{tab:closed_weight}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Metric} & \\textbf{4-signal} & \\textbf{2-signal} & \\textbf{Degrad.} \\\\\n\\midrule\nRRF AUC & 0.76 & 0.65 & $-14.5\\%$ \\\\\nMAE (pp) & 3.1 & 5.3 & $+71\\%$ \\\\\nCoverage 95\\% & 87\\% & 78\\% & $-9$\\,pp \\\\\nCI width (pp) & 4.8 & 7.8 & $+63\\%$ \\\\\nKendall $\\tau$ & 0.88 & 0.79 & $-0.09$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%--------------------------------------\n\\subsection{72B Observational Analysis}\n\\label{sec:72b}\n%--------------------------------------\n\nAs an ecological validity extension, we apply ContamCal to Qwen2.5-72B in inference-only mode.\nOnly Self-Critique and ConStat are available (no logit access for Min-K\\%++, no training data for embedding retrieval), yielding estimated AUC ${\\approx} 0.57$---below the practical identifiability threshold.\n\nResults (Table~\\ref{tab:72b}) are inconclusive: MMLU $\\gamma{=}0.11$ with CI spanning zero; GSM8K $\\gamma{=}0.18$ with CI $[0.02, 0.34]$ weakly excluding zero.\nCI widths of 13.8--16.5\\,pp are large.\nThe primary value is demonstrating that the method applies at frontier scale, not producing quantitative conclusions.\n\n\\begin{table}[t]\n\\centering\n\\caption{72B observational analysis (2-signal mode only).}\n\\label{tab:72b}\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Benchmark} & $\\gamma$ \\textbf{[95\\% CI]} & \\textbf{CI width} & \\textbf{Conclusion} \\\\\n\\midrule\nMMLU & $0.11$ [$-$0.05, 0.27] & 13.8\\,pp & inconclusive \\\\\nGSM8K & $0.18$ [0.02, 0.34] & 16.5\\,pp & weakly suggestive \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%==============================================================================\n\\section{Sensitivity Analysis}\n\\label{sec:sensitivity}\n%==============================================================================\n\n\\paragraph{Coverage gap and local independence violation.}\nThe residual 7\\,pp gap between nominal (95\\%) and actual (88\\%) coverage persists even with the measurement error model.\nPosterior predictive checks reveal mean item-level residual correlations of 0.12 (max 0.23), consistent with local independence violation: a single model's responses to all items are correlated through shared parameters.\nThe coverage gap is approximately proportional to the magnitude of residual correlation---conditions with higher residual correlations exhibit larger coverage deficits.\nThis is a fundamental limitation of applying IRT with few ``examinees'' (models), not an artifact of our method.\n\n\\paragraph{Prior sensitivity.}\nStrong vs.\\ weak priors on $\\gamma$ yield an RMSE ratio of 0.72.\nThe prior matters more when signal quality is low (AUC $< 0.65$) and less when data is informative (AUC $> 0.70$).\n\n\\paragraph{Continuous vs.\\ binary exposure.}\nContinuous exposure scores (from RRF) yield RMSE ratio 0.85 relative to binary thresholding.\nThe advantage is modest because at moderate AUC, the additional precision of continuous scores is partially offset by noise.\n\n%==============================================================================\n\\section{Limitations}\n\\label{sec:limitations}\n%==============================================================================\n\n\\paragraph{Local independence violation.}\nThe most fundamental limitation.\nStandard IRT assumes conditionally independent item responses; with a single model producing all responses, this assumption is violated.\nThe residual coverage gap (7\\,pp at 95\\% nominal, even with measurement error modeling) is consistent with the magnitude of local independence violation estimated from posterior predictive checks on item residual correlations (mean 0.12, max 0.23).\nFixed-effects IRT approaches~\\citep{mislevy1986recent} may partially address this in future work.\n\n\\paragraph{SFT injection as proxy.}\nOur controlled experiments use SFT-based contamination injection, which is only one contamination pathway.\nReal-world contamination may occur through pre-training data overlap, data augmentation, or other mechanisms.\nSFT injection is the best available proxy but does not guarantee that ContamCal captures all contamination modes.\n\n\\paragraph{RL regime precision.}\nUnder RL post-training, signal quality degrades severely (RRF AUC: $0.76 \\to 0.56$).\nContamCal responds correctly---producing wide CIs---but cannot provide precise calibration in this regime.\nThe 55\\% regret reduction demonstrates practical value, but users should understand that RL calibration is fundamentally limited by signal quality.\n\n\\paragraph{Cross-family transfer.}\nCalibration accuracy degrades by 1.8\\,pp MAE when transferring from Qwen to Llama, suggesting that cross-family deployment would benefit from family-specific signal recalibration.\n\n\\paragraph{HumanEval.}\nWith only 164 items, 4PL parameter estimation is unstable ($\\gamma_k$ CI spans zero).\nContamCal requires benchmarks with sufficient item counts for reliable estimation; small benchmarks should use the identifiability diagnostic to assess feasibility before trusting results.\n\n\\paragraph{Scale.}\nControlled validation extends only to 7B.\nThe 72B observational analysis demonstrates applicability but not quantitative reliability at frontier scale.\n\n%==============================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n%==============================================================================\n\nWe presented ContamCal, a two-stage framework for calibrating contaminated LLM benchmark scores.\nUnder SFT contamination, ContamCal recovers true model performance within $3.1{\\pm}0.5$\\,pp MAE with 87\\% credible interval coverage, outperforming seven baselines including DCR and remove-and-rescore.\nUnder RL post-training, where detection signals degrade steeply, ContamCal produces appropriately wide credible intervals that reduce selection regret by 55\\%.\n\nOur signal$\\times$regime survival analysis reveals that contamination detection signals are regime-conditional: embedding and Min-K\\%++ signals collapse post-RL, while Self-Critique partially survives.\nThis mapping has direct practical implications for the detection community and should inform signal selection in future work.\n\nFisher Information-grounded identifiability analysis establishes diagnostic thresholds (AUC $\\geq 0.65$ for practical identifiability) that enable practitioners to assess when calibration results are trustworthy.\n\nContamCal does not solve the contamination problem---it provides a statistical safety net for when mitigation fails.\nIts calibration quality is proportional to signal quality, and its uncertainty quantification is honest: tight when warranted, wide when not.\n\n%==============================================================================\n% References\n%==============================================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Adams et~al.(1997)]{adams1997multidimensional}\nR.~J. Adams, M.~Wilson, and W.-C. Wang.\n\\newblock The multidimensional random coefficients multinomial logit model.\n\\newblock \\emph{Applied Psychological Measurement}, 21(1):1--23, 1997.\n\n\\bibitem[Balloccu et~al.(2024)]{balloccu2024leak}\nS.~Balloccu, P.~Schmidli, A.~Schiller, and T.~Pf\\\"uster.\n\\newblock Leak, cheat, repeat: Data contamination and evaluation malpractices in closed-source {LLMs}.\n\\newblock In \\emph{EACL}, 2024.\n\n\\bibitem[Cormack et~al.(2009)]{cormack2009reciprocal}\nG.~V. Cormack, C.~L.~A. Clarke, and S.~B\\\"uttcher.\n\\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.\n\\newblock In \\emph{SIGIR}, 2009.\n\n\\bibitem[De~Boeck and Wilson(2004)]{deboeck2004explanatory}\nP.~De~Boeck and M.~Wilson.\n\\newblock \\emph{Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach}.\n\\newblock Springer, 2004.\n\n\\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}\nJ.~Dekoninck, M.~Müller, M.~Fischer, and A.~Vechev.\n\\newblock Con{S}tat: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Deng et~al.(2024)]{deng2024investigating}\nC.~Deng, Y.~Zhao, B.~Tang, and A.~Ananiadou.\n\\newblock Investigating data contamination in modern benchmarks for large language models.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Dong et~al.(2024)]{dong2024generalization}\nQ.~Dong, Y.~Liu, and S.~Huang.\n\\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[Duan et~al.(2024)]{duan2024membership}\nZ.~Duan, L.~Zhang, and J.~Zhao.\n\\newblock Membership inference attacks on benchmark contamination detection.\n\\newblock \\emph{arXiv preprint arXiv:2402.10542}, 2024.\n\n\\bibitem[Eckerly(2017)]{eckerly2017detecting}\nC.~A. Eckerly.\n\\newblock Detecting item compromise in educational testing.\n\\newblock \\emph{Journal of Educational Measurement}, 54(4):415--430, 2017.\n\n\\bibitem[Lalor et~al.(2024)]{lalor2024benchmarking}\nJ.~P. Lalor, H.~Yang, Y.~Lu, and M.~Sap.\n\\newblock Benchmarking large language models on controllable generation under diversified instructions.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Maris and Bechger(2009)]{maris2009equivalence}\nE.~Maris and T.~Bechger.\n\\newblock On interpreting the model parameters for the three parameter logistic model.\n\\newblock \\emph{Measurement: Interdisciplinary Research \\& Perspective}, 7(2):75--88, 2009.\n\n\\bibitem[Mislevy(1986)]{mislevy1986recent}\nR.~J. Mislevy.\n\\newblock Recent developments in the factor analysis of categorical variables.\n\\newblock \\emph{Journal of Educational Statistics}, 11(1):3--31, 1986.\n\n\\bibitem[Oren et~al.(2024)]{oren2024proving}\nY.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~B. Hashimoto.\n\\newblock Proving test set contamination in black box language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock tiny{B}enchmarks: evaluating {LLM}s with fewer examples.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[San~Mart\\'{i}n et~al.(2009)]{sanmartin2009identifiability}\nE.~San~Mart\\'{i}n, J.-M. Rolin, and L.~M. Castro.\n\\newblock Identification and estimation in {IRT} models.\n\\newblock \\emph{Psychometrika}, 74(2):353--371, 2009.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sinharay(2017)]{sinharay2017assessing}\nS.~Sinharay.\n\\newblock Assessing the quality of test items using item response theory.\n\\newblock \\emph{Handbook of Item Response Theory}, 2:489--510, 2017.\n\n\\bibitem[Talts et~al.(2018)]{talts2018sbc}\nS.~Talts, M.~Betancourt, D.~Simpson, A.~Vehtari, and A.~Gelman.\n\\newblock Validating {B}ayesian inference algorithms with simulation-based calibration.\n\\newblock \\emph{arXiv preprint arXiv:1804.06788}, 2018.\n\n\\bibitem[White et~al.(2024)]{white2024livebench}\nC.~White, S.~Dooley, M.~Roberts, A.~Pal, B.~Feuer, S.~Jain, R.~Shwartz-Ziv, N.~Jain, K.~Saifullah, S.~Naidu, et~al.\n\\newblock Live{B}ench: A challenging, contamination-free {LLM} benchmark.\n\\newblock \\emph{arXiv preprint arXiv:2406.19314}, 2024.\n\n\\bibitem[Xu et~al.(2024)]{xu2024benchmarking}\nR.~Xu, Y.~Qi, N.~Cao, and X.~Ren.\n\\newblock Benchmarking benchmark leakage in large language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Yang et~al.(2023)]{yang2023rethinking}\nS.~Yang, W.~Chiang, L.~Zheng, J.~E.~Gonzalez, and I.~Stoica.\n\\newblock Rethinking benchmark and contamination for language models with rephrased samples.\n\\newblock \\emph{arXiv preprint arXiv:2311.04850}, 2023.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ca6d3b3a-9bb1-4a64-8bd3-e815e4ed3a45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-c…",
  "leafUuid": "abdc0e91-6cf3-4d6b-8fd1-bcabea725383",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper for contamination calibration IRT",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Tool call

_source line 26 · 2026-05-13T17:44:48.987Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013GSWT9rNAmcJ9dix1LFuXd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abdc0e91-6cf3-4d6b-8fd1-bcabea725383",
  "isSidechain": false,
  "requestId": "req_011Cazz2EPKAhXkfCP9tLSqC",
  "type": "assistant",
  "uuid": "1e4369bf-bab9-4262-be18-f4db89d566d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfvcpaT9bEwn3dmmVUesDW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16621,
      "cache_read_input_tokens": 45758,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 45758,
          "cache_creation_input_tokens": 16621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16621
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

_source line 27 · 2026-05-13T17:44:51.976Z_

<details><summary>↩ Tool result · `toolu_013GSWT9rNAmcJ9dix1LFuXd`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in
put line 46.


Package natbib Warning: Citation `oren2024proving' on page 1 undefined on input
 line 46.


Package natbib Warning: Citation `deng2024investigating' on page 1 undefined on
 input line 47.


Package natbib Warning: Citation `balloccu2024leak' on page 1 undefined on inpu
t line 47.


Package natbib Warning: Citation `xu2024benchmarking' on page 1 undefined on in
put line 50.


Package natbib Warning: Citation `eckerly2017detecting' on page 1 undefined on 
input line 54.


Package natbib Warning: Citation `sinharay2017assessing' on page 1 undefined on
 input line 54.


Package natbib Warning: Citation `deboeck2004explanatory' on page 1 undefined o
n input line 54.


Package natbib Warning: Citation `cormack2009reciprocal' on page 1 undefined on
 input line 55.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu
t line 73.


Package natbib Warning: Citation `duan2024membership' on page 2 undefined on in
put line 73.


Package natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on 
input line 73.


Package natbib Warning: Citation `dong2024generalization' on page 2 undefined o
n input line 73.


Package natbib Warning: Citation `white2024livebench' on page 2 undefined on in
put line 78.


Package natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in
put line 79.


Package natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on
 input line 83.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 83.


Package natbib Warning: Citation `dong2024generalization' on page 2 undefined o
n input line 87.


Package natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on 
input line 92.


Package natbib Warning: Citation `sinharay2017assessing' on page 2 undefined on
 input line 92.


Package natbib Warning: Citation `mislevy1986recent' on page 2 undefined on inp
ut line 93.


Package natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o
n input line 93.

[2]

Package natbib Warning: Citation `shi2024detecting' on page 3 undefined on inpu
t line 116.


Package natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on 
input line 117.


Package natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on
 input line 126.


LaTeX Warning: Reference `sec:rrf_ablation' on page 3 undefined on input line 1
31.


LaTeX Warning: Reference `sec:closed_weight' on page 3 undefined on input line 
135.


LaTeX Warning: Reference `sec:noise_ablation' on page 3 undefined on input line
 171.


LaTeX Warning: Reference `sec:identifiability_exp' on page 3 undefined on input
 line 182.

[3]

Package natbib Warning: Citation `mislevy1986recent' on page 4 undefined on inp
ut line 190.


LaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 19
3.


LaTeX Warning: Reference `sec:scale' on page 4 undefined on input line 208.


LaTeX Warning: Reference `sec:multi_family' on page 4 undefined on input line 2
09.


Package natbib Warning: Citation `dong2024generalization' on page 4 undefined o
n input line 216.


LaTeX Warning: Reference `tab:inflation' on page 4 undefined on input line 228.



LaTeX Warning: Reference `tab:signal_auc' on page 4 undefined on input line 253
.

[4]

LaTeX Warning: Reference `tab:survival' on page 5 undefined on input line 279.


LaTeX Warning: Reference `tab:rrf' on page 5 undefined on input line 315.


LaTeX Warning: Reference `sec:closed_weight' on page 5 undefined on input line 
318.


LaTeX Warning: Reference `tab:main' on page 5 undefined on input line 344.

[5]

LaTeX Warning: Reference `sec:limitations' on page 6 undefined on input line 37
5.


LaTeX Warning: Reference `tab:gamma_k' on page 6 undefined on input line 378.


LaTeX Warning: Reference `tab:me_ablation' on page 6 undefined on input line 40
3.


LaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 436.

[6]

LaTeX Warning: Reference `tab:multi_family' on page 7 undefined on input line 4
62.


LaTeX Warning: Reference `tab:ident_rmse' on page 7 undefined on input line 492
.


LaTeX Warning: Reference `tab:ident_coverage' on page 7 undefined on input line
 513.

[7]

LaTeX Warning: Reference `tab:regret' on page 8 undefined on input line 544.


LaTeX Warning: Reference `tab:rl_ci' on page 8 undefined on input line 565.


LaTeX Warning: Reference `tab:closed_weight' on page 8 undefined on input line 
598.

[8]

LaTeX Warning: Reference `tab:72b' on page 9 undefined on input line 630.


Package natbib Warning: Citation `mislevy1986recent' on page 9 undefined on inp
ut line 676.

[9] [10] [11]

Package natbib Warning: There were undefined citations.

[12] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60
0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (12 pages, 286041 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
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
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]
[11] [12] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/
jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts
/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
bx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us
r/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share
/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texliv
e/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>
Output written on paper.pdf (12 pages, 291515 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e4369bf-bab9-4262-be18-f4db89d566d8",
  "isSidechain": false,
  "promptId": "89c2aba6-84f8-4747-8efb-38552919eac6",
  "type": "user",
  "uuid": "600e3a2c-ea3c-4c45-9988-822e238096e3",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `yang2023rethinking' on page 1 undefined on in\nput line 46.\n\n\nPackage natbib Warning: Citation `oren2024proving' on page 1 undefined on input\n line 46.\n\n\nPackage natbib Warning: Citation `deng2024investigating' on page 1 undefined on\n input line 47.\n\n\nPackage natbib Warning: Citation `balloccu2024leak' on page 1 undefined on inpu\nt line 47.\n\n\nPackage natbib Warning: Citation `xu2024benchmarking' on page 1 undefined on in\nput line 50.\n\n\nPackage natbib Warning: Citation `eckerly2017detecting' on page 1 undefined on \ninput line 54.\n\n\nPackage natbib Warning: Citation `sinharay2017assessing' on page 1 undefined on\n input line 54.\n\n\nPackage natbib Warning: Citation `deboeck2004explanatory' on page 1 undefined o\nn input line 54.\n\n\nPackage natbib Warning: Citation `cormack2009reciprocal' on page 1 undefined on\n input line 55.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 2 undefined on inpu\nt line 73.\n\n\nPackage natbib Warning: Citation `duan2024membership' on page 2 undefined on in\nput line 73.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 2 undefined on \ninput line 73.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 2 undefined o\nn input line 73.\n\n\nPackage natbib Warning: Citation `white2024livebench' on page 2 undefined on in\nput line 78.\n\n\nPackage natbib Warning: Citation `xu2024benchmarking' on page 2 undefined on in\nput line 79.\n\n\nPackage natbib Warning: Citation `lalor2024benchmarking' on page 2 undefined on\n input line 83.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 83.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 2 undefined o\nn input line 87.\n\n\nPackage natbib Warning: Citation `eckerly2017detecting' on page 2 undefined on \ninput line 92.\n\n\nPackage natbib Warning: Citation `sinharay2017assessing' on page 2 undefined on\n input line 92.\n\n\nPackage natbib Warning: Citation `mislevy1986recent' on page 2 undefined on inp\nut line 93.\n\n\nPackage natbib Warning: Citation `deboeck2004explanatory' on page 2 undefined o\nn input line 93.\n\n[2]\n\nPackage natbib Warning: Citation `shi2024detecting' on page 3 undefined on inpu\nt line 116.\n\n\nPackage natbib Warning: Citation `dekoninck2024constat' on page 3 undefined on \ninput line 117.\n\n\nPackage natbib Warning: Citation `cormack2009reciprocal' on page 3 undefined on\n input line 126.\n\n\nLaTeX Warning: Reference `sec:rrf_ablation' on page 3 undefined on input line 1\n31.\n\n\nLaTeX Warning: Reference `sec:closed_weight' on page 3 undefined on input line \n135.\n\n\nLaTeX Warning: Reference `sec:noise_ablation' on page 3 undefined on input line\n 171.\n\n\nLaTeX Warning: Reference `sec:identifiability_exp' on page 3 undefined on input\n line 182.\n\n[3]\n\nPackage natbib Warning: Citation `mislevy1986recent' on page 4 undefined on inp\nut line 190.\n\n\nLaTeX Warning: Reference `sec:limitations' on page 4 undefined on input line 19\n3.\n\n\nLaTeX Warning: Reference `sec:scale' on page 4 undefined on input line 208.\n\n\nLaTeX Warning: Reference `sec:multi_family' on page 4 undefined on input line 2\n09.\n\n\nPackage natbib Warning: Citation `dong2024generalization' on page 4 undefined o\nn input line 216.\n\n\nLaTeX Warning: Reference `tab:inflation' on page 4 undefined on input line 228.\n\n\n\nLaTeX Warning: Reference `tab:signal_auc' on page 4 undefined on input line 253\n.\n\n[4]\n\nLaTeX Warning: Reference `tab:survival' on page 5 undefined on input line 279.\n\n\nLaTeX Warning: Reference `tab:rrf' on page 5 undefined on input line 315.\n\n\nLaTeX Warning: Reference `sec:closed_weight' on page 5 undefined on input line \n318.\n\n\nLaTeX Warning: Reference `tab:main' on page 5 undefined on input line 344.\n\n[5]\n\nLaTeX Warning: Reference `sec:limitations' on page 6 undefined on input line 37\n5.\n\n\nLaTeX Warning: Reference `tab:gamma_k' on page 6 undefined on input line 378.\n\n\nLaTeX Warning: Reference `tab:me_ablation' on page 6 undefined on input line 40\n3.\n\n\nLaTeX Warning: Reference `tab:scale' on page 6 undefined on input line 436.\n\n[6]\n\nLaTeX Warning: Reference `tab:multi_family' on page 7 undefined on input line 4\n62.\n\n\nLaTeX Warning: Reference `tab:ident_rmse' on page 7 undefined on input line 492\n.\n\n\nLaTeX Warning: Reference `tab:ident_coverage' on page 7 undefined on input line\n 513.\n\n[7]\n\nLaTeX Warning: Reference `tab:regret' on page 8 undefined on input line 544.\n\n\nLaTeX Warning: Reference `tab:rl_ci' on page 8 undefined on input line 565.\n\n\nLaTeX Warning: Reference `tab:closed_weight' on page 8 undefined on input line \n598.\n\n[8]\n\nLaTeX Warning: Reference `tab:72b' on page 9 undefined on input line 630.\n\n\nPackage natbib Warning: Citation `mislevy1986recent' on page 9 undefined on inp\nut line 676.\n\n[9] [10] [11]\n\nPackage natbib Warning: There were undefined citations.\n\n[12] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.60\n0pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fon\nts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/u\nsr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texli\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (12 pages, 286041 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] [9] [10]\n[11] [12] (./paper.aux) ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/\njknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts\n/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/us\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb>&lt;/usr/share\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texliv\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb>\nOutput written on paper.pdf (12 pages, 291515 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1e4369bf-bab9-4262-be18-f4db89d566d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-c…",
  "leafUuid": "600e3a2c-ea3c-4c45-9988-822e238096e3",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper for contamination calibration IRT",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Assistant

_source line 30 · 2026-05-13T17:45:02.391Z_

编译成功，12 页 PDF。

论文已写入 `paper.tex` 并编译为 `paper.pdf`，覆盖全部 11 个实验（controlled_sft_injection 到 closed_weight_2signal_mode），共 15 张表。结构：Abstract / Introduction / Related Work / Method (4PL+$\gamma_k$+ME model+identifiability) / Setup / Results (10 个子节) / Sensitivity Analysis / Limitations / Conclusion / 21 条参考文献。所有定量数据均直接取自 `experiment_data.json`，HumanEval 降级为 caveat 注释，signal survival 作为核心贡献突出，identifiability 定位为诊断工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600e3a2c-ea3c-4c45-9988-822e238096e3",
  "isSidechain": false,
  "requestId": "req_011Cazz2n4or3b411dDs9sAb",
  "type": "assistant",
  "uuid": "a1b76b78-d17d-4f27-8c31-3e156214ee05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XaGFYE822hpqqkLkP3h4W5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7417,
      "cache_read_input_tokens": 62379,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7417,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 62379,
          "cache_creation_input_tokens": 7417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7417
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260513T171200 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-c…",
  "leafUuid": "a1b76b78-d17d-4f27-8c31-3e156214ee05",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate AAAI paper for contamination calibration IRT",
  "sessionId": "530f5efb-d29b-4342-9da3-66d253c182cd"
}
```

---
