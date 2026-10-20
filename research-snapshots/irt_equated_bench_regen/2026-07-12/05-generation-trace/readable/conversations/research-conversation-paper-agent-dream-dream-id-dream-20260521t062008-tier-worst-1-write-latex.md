# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/ed986e33-bb2e-41ac-8746-1983d5200adc.jsonl`
- **Structured JSON:** [`9ad6a0d2af5b0aaa99b9.json`](../../sessions/9a/9ad6a0d2af5b0aaa99b9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T06:49:06.811Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T06:49:06.811Z",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：核心叙事：novelty 被彻底否定（\"applying textbook MH 1988 to new data ≠ contribution\"），IRT misspecification 被视为 根本性方法论缺陷（\"98% |Lz|>2 → ability matching 系统性偏差 → 31% C% 是 artifact 而非 finding\"）， semi-synthetic framework 被认为 too simple to publish，meta-critique 被 dismiss 为 obvious。 每个实验的结果要么被重新解读为 artifact，要么被认为 underpowered/scope-limited。 reviewer 立场：3 位中 2-3 位给 reject，平均分 3.5，novelty sub-score 1.5。 三条 reframe 路径（Framework-first / MIRT upgrade / Benchmark science）是唯一出路。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T06:49:06.815Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T06:49:06.815Z",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-21T06:49:06.837Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：核心叙事：novelty 被彻底否定（"applying textbook MH 1988 to new data ≠ contribution"），IRT misspecification 被视为 根本性方法论缺陷（"98% |Lz|>2 → ability matching 系统性偏差 → 31% C% 是 artifact 而非 finding"）， semi-synthetic framework 被认为 too simple to publish，meta-critique 被 dismiss 为 obvious。 每个实验的结果要么被重新解读为 artifact，要么被认为 underpowered/scope-limited。 reviewer 立场：3 位中 2-3 位给 reject，平均分 3.5，novelty sub-score 1.5。 三条 reframe 路径（Framework-first / MIRT upgrade / Benchmark science）是唯一出路。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "b6d9dfe2-e2e0-4574-93a9-72fad4a055fa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T06:49:06.835Z_

```json
{
  "parentUuid": "b6d9dfe2-e2e0-4574-93a9-72fad4a055fa",
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
  "uuid": "42ccf11c-abe1-45e0-a4c0-5f16935b0c79",
  "timestamp": "2026-05-21T06:49:06.835Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T06:49:06.835Z_

```json
{
  "parentUuid": "42ccf11c-abe1-45e0-a4c0-5f16935b0c79",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "351ba8f5-0604-4bfb-9419-aab3dad406ec",
  "timestamp": "2026-05-21T06:49:06.835Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
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
  "aiTitle": "Generate worst-case review simulation paper",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Assistant

_source line 7 · 2026-05-21T06:49:09.206Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "351ba8f5-0604-4bfb-9419-aab3dad406ec",
  "isSidechain": false,
  "requestId": "req_011CbFGVomAoMjQ68LrG63D8",
  "type": "assistant",
  "uuid": "a26af7a3-d334-4193-9698-6479e62af638",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmFxVmTn53TpRFftTsrFrE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11910,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11910
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

_source line 8 · 2026-05-21T06:49:10.250Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LR5xb8UWcmpV1tHBWr5WuU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a26af7a3-d334-4193-9698-6479e62af638",
  "isSidechain": false,
  "requestId": "req_011CbFGVomAoMjQ68LrG63D8",
  "type": "assistant",
  "uuid": "cc1410fc-59f1-4b32-b471-bd594c78e9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmFxVmTn53TpRFftTsrFrE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11910,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11910
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

_source line 9 · 2026-05-21T06:49:10.530Z_

<details><summary>↩ Tool result · `toolu_01LR5xb8UWcmpV1tHBWr5WuU`</summary>

```text
1	[
2	  {
3	    "name": "real_data_dif_mmlu",
4	    "description": "METABENCH MMLU 5,227×12,508 response matrix 上的 MH-DIF 分析",
5	    "results": {
6	      "temporal_ets_c_pct": 31.3,
7	      "temporal_fpr_li_clean": 0.318,
8	      "temporal_enrichment": 0.96,
9	      "ability_ets_c_pct": 2.9,
10	      "within_family_llama2v3_c_pct": 61.3,
11	      "domain_spearman_rho": 0.307,
12	      "domain_spearman_p": 0.02,
13	      "sanity_random_split_c_pct": 0.18,
14	      "irt_lz_pct_above_2": 98,
15	      "reviewer_interpretation": "artifact_of_misspecification"
16	    },
17	    "tables": [
18	      "Table 1: Temporal DIF results — C%=31.3%, enrichment=0.96 — reviewer 标注 'enrichment≈1 = no detection value'",
19	      "Table 2: Cohort comparison — ability split C%=2.9% vs temporal 31.3% — reviewer 认为差异来自 ability shift 而非 item-level effect"
20	    ],
21	    "figures": [],
22	    "analysis": "Reviewer 的核心攻击：31.3% 是一个 misspecified model 下的 baseline rate，不是 finding。 类比：如果你用线性回归拟合非线性数据，residual patterns 不代表新发现，而代表 model misfit。 MH-DIF on multidimensional data with 1D matching = structural Type I error inflation。 Llama-2 vs Llama-3 within-family C%=61.3% 被读为更强的证据——\"同一 family 内 61% items show DIF = 显然是 ability structure change, not contamination\"。\n\n\n数据本身与已完成 registry 一致——31.3% C% 是真实观测。但在 worst 档下，reviewer 的解读路径是： (1) 98% 模型 |Lz|>2 表明 1D IRT ability estimates 系统性不可靠； (2) MH 的 ability matching 依赖 total score 作为 ability proxy，而 MMLU 57 subjects 的 multidimensionality 意味着 total score 是一个 collapsed composite，无法真正 match ability； (3) 因此 31.3% C% 中有大量是 ability confounding 造成的 spurious DIF—— 两个模型在不同 subject domains 上能力结构不同，但 total score 相近，被 MH 视为 \"matched\"， 实际上它们在特定 subject 上的 ability 并不 matched； (4) enrichment≈0.96 直接验证了 DIF flags 与已知 contamination labels 无关联—— reviewer 读为 \"你的方法检测不到 contamination\"； (5) 0.18% sanity check 虽然证明不是纯噪声，但 reviewer 认为这只是证明 temporal cohort 之间 确实存在 ability distribution shift，而非 item-level contamination。 ρ=0.307 (p=0.02) 被 reviewer 解读为 \"domain improvement 是 confound 的证据， 不是被排除的证据\"——因为 item-level decomposition (plan_019) 的 pseudo R²=0.0007 只说明 linear relationship 弱，不排除 nonlinear 或 interaction effects。\n"
23	  },
24	  {
25	    "name": "rl_robustness_validation",
26	    "description": "验证 DIF 对 reasoning-RL 模型（GRPO/PPO）的鲁棒性",
27	    "results": {
28	      "n_reasoning_rl_models": 13,
29	      "alignment_rl_cohort_n": 477,
30	      "grpo_cohort_dif_c_pct": 34.8,
31	      "sft_baseline_dif_c_pct": 30.2,
32	      "alignment_rl_dif_c_pct": 31.9,
33	      "jaccard_sft_vs_grpo": 0.71,
34	      "delong_p_dif_vs_constat": 0.38,
35	      "tost_equivalence_p": 0.22,
36	      "constat_auroc_on_rl": 0.54,
37	      "mink_auroc_on_rl": 0.51,
38	      "dif_auroc_on_rl": 0.58,
39	      "bootstrap_ci_auroc_dif": [
40	        0.41,
41	        0.73
42	      ],
43	      "power_at_p04": 0.12,
44	      "power_at_p07": 0.43,
45	      "power_at_p10": 0.68
46	    },
47	    "tables": [
48	      "Table: AUROC comparison across 3 methods × 3 cohort types — all CIs overlap, no method dominates",
49	      "Table: Power curve p ∈ [0.4, 1.0] — reviewer notes 'useful range starts at p≥0.7, narrowing practical applicability'"
50	    ],
51	    "figures": [],
52	    "analysis": "Reviewer consensus: \"N=13 RL models is a pilot, not a validation. The authors cannot claim RL-robustness based on mixing 13 models into a 600+ cohort — the signal is drowned. Individual-model analysis (ConStat/Min-K%) at least tests each model; DIF by design cannot. This is a structural limitation of group-level methods, acknowledged but not resolved.\" 致命打击：reviewer 将此解读为 DIF 的固有缺陷——无法做 per-model detection——而非优势。\n\n\nWorst 档下的问题不是实验跑不出来，而是 N=13 reasoning-RL 模型被 reviewer 视为 fundamentally underpowered： (1) 13 个 GRPO/PPO 模型混入 focal cohort 后，C% 从 30.2% 微升到 34.8%—— reviewer 解读为 \"adding stronger models → more ability confounding → more spurious DIF\"， 而非 \"DIF robust to RL\"； (2) AUROC 比较（DIF 0.58 vs ConStat 0.54 vs Min-K% 0.51）差异不显著（DeLong p=0.38）， bootstrap CI 跨越 0.5——reviewer 说 \"all methods are at chance, you've shown nothing\"； (3) TOST equivalence test p=0.22，无法 reject \"DIF 和传统方法等效\" 的 H0—— reviewer 认为 \"failure to demonstrate equivalence or superiority = uninformative\"； (4) Power analysis 显示 p=0.4 时 TPR=0.12——reviewer 说 \"DIF can only detect near-complete exploitation, which is the trivial case\"； (5) 核心问题：整个实验无法区分 \"DIF works on RL models\" 和 \"DIF produces same artifacts regardless of model type\"——在 IRT misspecification 框架下，两者不可区分。\n"
53	  },
54	  {
55	    "name": "constat_perturbation_eval",
56	    "description": "ConStat-style perturbation testing 在 MMLU 上的独立评估",
57	    "results": {
58	      "n_items_reformulated": 220,
59	      "reformulation_quality_human_eval": 0.82,
60	      "constat_detection_rate_non_rl": 0.41,
61	      "constat_detection_rate_rl": 0.08,
62	      "constat_fdr_controlled_rate": 0.23,
63	      "constat_vs_dif_overlap_pct": 12.7,
64	      "constat_fpr": 0.067,
65	      "constat_unique_detections": 158,
66	      "dif_unique_detections": 892
67	    },
68	    "tables": [
69	      "Table: ConStat vs DIF detection comparison — ConStat lower recall but much lower FPR"
70	    ],
71	    "figures": [],
72	    "analysis": "Reviewer 用 ConStat 的低 FPR 作为武器：\"ConStat achieves controlled FPR by design (FDR correction); DIF's 31.8% FPR on Li-clean items means nearly 1 in 3 flags is false, and you cannot tell which ones without ground truth.\" 这强化了 \"DIF C% is inflated by misspecification\" 的叙事。\n\n\nConStat 在 non-RL 模型上表现合理（41% detection rate），FPR 远低于 DIF（0.067 vs 0.318）。 Worst 档下 reviewer 解读： (1) ConStat FPR=0.067 vs DIF FPR=0.318——\"DIF 的高 detection rate 主要来自高 FPR， 不是真正的 detection power\"； (2) 12.7% overlap 表明两种方法检测的是完全不同的现象——reviewer 认为 ConStat 检测 actual contamination (perturbation sensitivity)，而 DIF 检测 ability shift artifact； (3) ConStat 在 RL 模型上确实退化（8%），但 reviewer 说 \"at least ConStat has a clear mechanism story; DIF's mechanism is unfalsifiable because any result can be attributed to either contamination or ability change\"； (4) 220 items 的 reformulation 质量（0.82 human eval）足够，但 scope 太小—— reviewer 要求 full-scale replication 才能比较。\n"
73	  },
74	  {
75	    "name": "dvd_generation_variance_eval",
76	    "description": "DVD generation variance 在 MMLU 上的独立评估",
77	    "results": {
78	      "n_models_evaluated": 12,
79	      "n_items_per_model": 200,
80	      "n_generations_per_item": 50,
81	      "bimodal_detection_rate": 0.14,
82	      "variance_based_detection_rate": 0.22,
83	      "dvd_vs_dif_overlap": 0.09,
84	      "dvd_fpr": 0.04,
85	      "gpu_hours_used": 65,
86	      "variant_contamination_detected": 31
87	    },
88	    "tables": [
89	      "Table: DVD detection rates by contamination type (verbatim vs variant) — low overall"
90	    ],
91	    "figures": [],
92	    "analysis": "DVD 作为独立信号太弱（14% bimodal detection），且 per-model inference 的 cost 使其不 scalable。 Reviewer 建议 \"DVD is better suited as a follow-up diagnostic on flagged items, not a primary detector\" ——削弱 ensemble 的 motivation。\n\n\nDVD 需要 per-model inference access（50 generations × 200 items × 12 models = 120K generations）， cost 高但可行。Worst 档下： (1) Bimodal detection rate 仅 14%——reviewer 说 \"variant contamination is rare or this method is underpowered, either way not compelling\"； (2) 9% overlap with DIF——再次证明方法检测不同现象，但 worst 档下 reviewer 解读为 \"three orthogonal weak signals don't add up to one strong signal\"； (3) DVD FPR=0.04 很低，但 detection rate 也低——reviewer 认为 precision-recall tradeoff 不足以支撑 contribution； (4) 12 models 太少——reviewer 要求 \"at minimum 50+ models to characterize generation variance distribution\"，而 GPU budget 不支持。\n"
93	  },
94	  {
95	    "name": "ensemble_fusion",
96	    "description": "DIF + ConStat + DVD 三信号融合",
97	    "results": {
98	      "majority_vote_precision": 0.38,
99	      "majority_vote_recall": 0.09,
100	      "weighted_fusion_precision": 0.44,
101	      "weighted_fusion_recall": 0.15,
102	      "ensemble_fpr": 0.087,
103	      "cross_val_weight_stability": "low — std/mean > 0.6 across folds",
104	      "dif_weight": 0.28,
105	      "constat_weight": 0.51,
106	      "dvd_weight": 0.21,
107	      "uniform_baseline_vs_optimized_delta_f1": 0.02
108	    },
109	    "tables": [
110	      "Table: Ensemble configurations — all recall < 0.20, precision < 0.50",
111	      "Table: Cross-validation fold weights — high variance across folds"
112	    ],
113	    "figures": [],
114	    "analysis": "Ensemble 在 paper 中降级为 appendix negative result。Reviewer 的结论性评价： \"The ensemble experiment confirms what the low pairwise overlaps predicted — these methods detect different phenomena (or noise), and combining them doesn't produce a coherent detector. This is informative but not a contribution; it's a null result.\"\n\n\nEnsemble 在 worst 档下彻底失败，原因链： (1) 三个信号 overlap 极低（pairwise Jaccard < 0.15）→ majority vote 几乎不触发（recall 9%）； (2) 加权融合稍好但 cross-validation 权重不稳定（std/mean > 0.6）——reviewer 说 \"overfitting to a small calibration set with unstable weights is not a methodology contribution\"； (3) Optimized vs uniform weight F1 差异仅 0.02——\"no evidence that learned fusion outperforms naive averaging, suggesting insufficient signal diversity\"； (4) DIF weight 仅 0.28（最低），ConStat 0.51——reviewer 读为 \"even the ensemble downweights DIF, your supposed primary contribution\"； (5) FPR=0.087 达标（<0.10），但 recall=0.15 意味着 85% contamination 未检测—— \"an ensemble that misses 85% of contaminated items is not operationally useful\"。 核心问题：Claim 2（ensemble = contribution）在 worst 档下被视为 negative result， 不是 contribution——\"showing that three weak detectors don't combine well is not novel\"。\n"
115	  },
116	  {
117	    "name": "cross_benchmark_gsm8k",
118	    "description": "GSM8K 上复制 DIF 分析，用 GSM1K 作为 contamination ground truth",
119	    "results": {
120	      "gsm8k_n_items": 1319,
121	      "gsm8k_n_ref": 1017,
122	      "gsm8k_n_foc": 804,
123	      "gsm8k_standard_c_pct": 18.9,
124	      "gsm8k_external_c_pct": 47.4,
125	      "gsm8k_sanity_c_pct": 0.3,
126	      "semi_synthetic_delta_tpr_p10": 0.818,
127	      "gsm1k_n_models": 33,
128	      "gsm1k_pearson_r": -0.478,
129	      "gsm1k_pearson_p": 0.005,
130	      "gsm1k_spearman_rho": -0.403,
131	      "gsm1k_bca_ci_upper": -0.155,
132	      "gsm1k_partial_r": -0.385,
133	      "reviewer_dismiss_gsm1k": true
134	    },
135	    "tables": [
136	      "Table: GSM1K correlation — r=-0.478 with wide CI, reviewer highlights N=33 limitation",
137	      "Table: Semi-synthetic ΔTPR=0.818 — reviewer acknowledges but says 'synthetic ≠ real'"
138	    ],
139	    "figures": [],
140	    "analysis": "GSM8K semi-synthetic (ΔTPR=0.818) 是最强结果，但 reviewer 将其与 MMLU 主分析隔离： \"The GSM8K semi-synthetic result is impressive but says nothing about whether the 31.3% MMLU finding is real or artifact — different benchmark, different dimensionality, different N.\" GSM1K correlation 被 dismiss due to N=33 和 difficulty confound alternative explanation。\n\n\n数据与 registry 一致。Worst 档下 reviewer 的攻击矩阵： (1) N=33 模型——\"33 data points with r=-0.478 is suggestive at best; BCa CI upper bound |r|=0.155 means the true effect could be trivially small\"； (2) 负相关方向 (r=-0.478) 与 contamination hypothesis 相反——DIF items 上 contamination gap 更小，不是更大。Paper 解释为 \"DIF items resist contamination-based gains\"， reviewer 替代解读：\"DIF items are simply harder items where all models struggle, contaminated or not — the negative correlation is a difficulty confound, not a detection signal\"； (3) Spearman CI [−0.687, −0.031] 上界接近 0——\"barely significant, and with N=33 a single influential point shifts everything\"（尽管 Cook's D robust, leave-one-out stable）； (4) GSM8K 是 single-domain math benchmark, MMLU 是 57-subject multidomain—— \"generalization from GSM8K to MMLU is not justified; the DIF mechanism operates differently on unidimensional vs multidimensional benchmarks\"； (5) GSM1K 本身作为 ground truth 被质疑——\"GSM1K measures a different construct (novel math problems) and the gap may reflect test-taking strategy differences, not contamination\"。 核心：A6 不成立——GSM1K 被 dismiss。\n"
141	  },
142	  {
143	    "name": "bifactor_irt_equating_pilot",
144	    "description": "Bifactor IRT equating pilot — general factor + subject-specific factors",
145	    "results": {
146	      "bifactor_convergence": false,
147	      "rmsea": 0.089,
148	      "cfi": 0.71,
149	      "tli": 0.68,
150	      "srmr": 0.112,
151	      "n_heywood_cases": 47,
152	      "anchor_items_identified": 0,
153	      "equated_score_rho": null,
154	      "decision": "killed"
155	    },
156	    "tables": [
157	      "Table: Bifactor fit indices — all below acceptable thresholds"
158	    ],
159	    "figures": [],
160	    "analysis": "Bifactor 失败在 worst 档下是 double-edged：不仅 equating 路径 dead， 还为 reviewer 提供了 \"see, even the authors tried to fix IRT misspecification and failed\" 的叙事。 在 reframe 路径 B（MIRT upgrade）中需要换 exploratory MIRT 或 mixture IRT 而非 confirmatory bifactor。\n\n\n与 registry (plan_015 killed) 一致。Worst 档下 bifactor 失败的机制： (1) 12,508 items × 5,227 models 的 bifactor model（general + 57 subject factors） 参数空间巨大（~12,508 × 59 = ~738K parameters），mirt 不收敛； (2) 即使降到 subset（5 subjects, ~1,200 items），Heywood cases（负方差估计）出现 47 次—— 说明 data 不支持 bifactor structure，或者需要 constrained estimation； (3) RMSEA=0.089 > 0.06 cutoff, CFI=0.71 < 0.90 cutoff——fit 远低于 acceptable 标准； (4) 无法识别 anchor items（因为 model 本身不 fit）→ 整个 equating pipeline 断裂； (5) Reviewer 的解读最致命：\"You can't even fit a bifactor model to this data — this CONFIRMS that IRT assumptions are fundamentally violated for MMLU. If bifactor doesn't fit, your 1D MH-DIF is even more misspecified than we thought.\" 这个 killed experiment 在 worst 档下反而成为 reviewer 攻击 IRT misspecification 的额外弹药。\n"
161	  },
162	  {
163	    "name": "item_generation_calibration",
164	    "description": "LLM 生成替换 items + student simulation 校准",
165	    "results": {
166	      "n_items_generated": 500,
167	      "difficulty_rho_prompt_based": 0.18,
168	      "difficulty_rho_student_sim": 0.52,
169	      "target_difficulty_rho": 0.75,
170	      "construct_alignment_human_eval": 0.64,
171	      "holdout_panel_correlation": 0.41,
172	      "replacement_quality_verdict": "below_benchmark"
173	    },
174	    "tables": [
175	      "Table: Difficulty calibration — prompt-based vs student-sim vs target, all below threshold"
176	    ],
177	    "figures": [],
178	    "analysis": "Item generation 在 worst 档下是 Claim 3（benchmark regeneration）的棺材钉。 即使不考虑 bifactor failure，生成 items 的质量本身不足以支撑 \"operational replacement\" 的 claim。 Reviewer 建议 \"demote to future work\"——which is exactly what the reframe paths do。\n\n\nWorst 档下 item generation 全面低于 benchmarks： (1) Prompt-based difficulty targeting ρ=0.18（文献报告 0.10-0.45 range 的下端）； (2) Student simulation 校准 ρ=0.52（文献报告 0.75-0.82 的下限以下）—— MMLU 的 domain diversity 使得单一 student simulator 无法准确估计 57 subjects 的 difficulty； (3) Construct alignment human evaluation 仅 0.64——36% 的生成 items 被判定 与原 item 不在同一 cognitive level 或 subject boundary 内； (4) Holdout model panel correlation 0.41——替换 items 上的 model ranking 与原 items ranking 相关性太低，equating 无法保证 score equivalence； (5) Reviewer 的攻击：\"If you can't generate calibrated replacement items, the entire benchmark regeneration pipeline is aspirational, not operational. This undermines Claim 3's practical value.\" 依赖 plan_005 的 anchor items 识别，而 plan_005 已 killed → 整条 pipeline dead。\n"
179	  },
180	  {
181	    "name": "cumulative_bayesian_dif",
182	    "description": "Cumulative Bayesian DIF priors — 4 successive administrations模拟",
183	    "results": {
184	      "single_admin_power_d10": 0.38,
185	      "cumulative_2_admin_power_d10": 0.49,
186	      "cumulative_3_admin_power_d10": 0.58,
187	      "cumulative_4_admin_power_d10": 0.64,
188	      "target_cumulative_power": 0.7,
189	      "simulation_only": true,
190	      "real_data_validation": "none"
191	    },
192	    "tables": [
193	      "Table: Power accumulation over 4 administrations — falls short of 0.70 target at δ=1.0"
194	    ],
195	    "figures": [],
196	    "analysis": "Cumulative Bayesian DIF 在 worst 档下是 appendix filler，不贡献 novelty 也不贡献 empirical evidence。 Reviewer consensus: underdeveloped simulation study without real-data anchoring。\n\n\nWorst 档下 cumulative Bayesian DIF 问题： (1) 即使 4 次 administration 后 power 仅 0.64，低于 target 0.70—— prior accumulation 的增益被 IRT misspecification 的 systematic bias 抵消； (2) 纯 simulation，无 real data validation——reviewer 说 \"simulation under your assumed generative model will always confirm your method; this is tautological\"； (3) \"4 successive administrations\" 假设 benchmark 不变——但如果 items 在 generation 之间 确实 drift（即你自己的 Claim 1），则 prior 积累的是 stale information； (4) Sinharay et al. (2006) 原始方法设计为 human testing with stable construct—— LLM benchmark 的 rapid capability shift 违反了 prior accumulation 的 stationarity 假设； (5) Reviewer 直接 dismiss：\"Simulation-only, no real data, questionable assumptions about temporal stationarity. Appendix material at best.\"\n"
197	  },
198	  {
199	    "name": "graceful_degradation_analysis",
200	    "description": "Benchmark validity degradation under progressive item replacement",
201	    "results": {
202	      "rho_at_5pct_replacement": 0.994,
203	      "rho_at_10pct_replacement": 0.986,
204	      "rho_at_20pct_replacement": 0.961,
205	      "rho_at_50pct_replacement": 0.873,
206	      "reliability_alpha_original": 0.94,
207	      "reliability_alpha_at_20pct": 0.88,
208	      "construct_coverage_gap_at_20pct": "3 subjects lose >30% items",
209	      "theoretical_bound_tight": false
210	    },
211	    "tables": [
212	      "Table: Validity metrics × replacement rate — degradation faster than expected"
213	    ],
214	    "figures": [],
215	    "analysis": "在 bifactor 和 item generation 都失败的前提下，graceful degradation 变成 \"removing items\" 分析而非 \"replacing items\" 分析。与 plan_017 的 ρ≈0.997 冲突——removing DIF items 更安全 than replacing them with poorly calibrated alternatives。Reviewer 结论： \"The regeneration pipeline is not ready for deployment.\"\n\n\nWorst 档下 graceful degradation 的问题： (1) 依赖 plan_005/006 的替换 items——两者都 failed/below benchmark， 因此 \"replacement\" 实际上是 random item removal，不是 calibrated replacement； (2) ρ at 20% replacement = 0.961 看似 ok，但 reviewer 用 plan_017 的结果反驳： \"You already showed ρ≈0.997 when removing 31% DIF items. Random replacement at 20% gives ρ=0.961 — WORSE than just removing items entirely. Your replacement items ADD noise.\"； (3) Reliability alpha 从 0.94 降到 0.88——\"degradation is measurable and concerning at only 20% replacement\"； (4) 3 subjects lose >30% items at 20% replacement rate——construct coverage 不均匀， 某些 domain 被 disproportionately 影响； (5) Theoretical bounds 不 tight——无法给出 \"replace up to X% safely\" 的 actionable threshold， 削弱 practical contribution。\n"
216	  },
217	  {
218	    "name": "item_focused_trees",
219	    "description": "Item-Focused Trees (Tutz & Berger 2016) — continuous temporal covariate DIF",
220	    "results": {
221	      "ift_n_items_flagged": 4102,
222	      "ift_vs_mh_jaccard": 0.48,
223	      "ift_unique_flags": 1834,
224	      "mh_unique_flags": 1650,
225	      "ift_first_split_variable": "release_date",
226	      "ift_interaction_with_size": "significant (p<0.01)",
227	      "ift_temporal_granularity": "quarterly splits emerge naturally"
228	    },
229	    "tables": [
230	      "Table: MH vs IFT flag comparison — 48% Jaccard, significant disagreement"
231	    ],
232	    "figures": [],
233	    "analysis": "IFT 本意是 \"alternative method validates MH\"，但 worst 档下 48% overlap 被读为 refutation。 Reviewer 的 steel-man 攻击：\"If items' DIF status depends on which method you use, the phenomenon is not robust — it's an artifact of methodological choices.\" IFT 降级为 appendix，与主 finding 的 tension 在 limitations 中 discuss。\n\n\nIFT 在 worst 档下成为双刃剑： (1) IFT flags 4,102 items (32.8%) vs MH flags 3,918 (31.3%)——数量相近但 overlap 仅 48%， meaning 52% 的 flags 不一致； (2) Reviewer 解读：\"Two DIF methods on the same data flag different items — this means at least one (probably both) is detecting noise, not signal. If the phenomenon were real and large, methods should converge.\"； (3) IFT 的 continuous treatment 本身挑战了 MH 的 binary temporal split—— \"IFT shows the split is not clean at your chosen cutoff; DIF is gradual across the timeline, suggesting capability drift not contamination events\"； (4) IFT interaction with model size (p<0.01) 引入新 confound—— \"bigger models released later AND are more capable, so temporal DIF = size+capability confound\"； (5) IFT 作为 robustness check 未能 confirm MH——在 worst 档下这是 negative evidence。\n"
234	  },
235	  {
236	    "name": "architecture_stratified_dif",
237	    "description": "Decoder-only 子群内 DIF 分析 — 测试 architecture heterogeneity 影响",
238	    "results": {
239	      "n_decoder_only": 5226,
240	      "n_non_decoder": 1,
241	      "decoder_only_c_pct": 31.3,
242	      "full_population_c_pct": 31.3,
243	      "jaccard_decoder_vs_full": 1.0,
244	      "rmsea_decoder_only": 0.087,
245	      "cfi_decoder_only": 0.73,
246	      "tlr_decoder_only": 0.7,
247	      "irt_lz_pct_above_2_decoder_only": 97.8
248	    },
249	    "tables": [
250	      "Table: Full vs decoder-only DIF — identical results, confirming architecture is not the confound"
251	    ],
252	    "figures": [],
253	    "analysis": "Architecture stratification 是一个 true-but-trivial result。99.98% decoder-only 意味着 这个 check 从设计上就不可能找到 architecture effect。Reviewer 用它作为 \"authors address the wrong confound\" 的证据——the real confound is multidimensionality, not architecture。 在 reframe 路径下，这个实验仍然 reportable but not defensive。\n\n\n与 paper_framing 一致——METABENCH MMLU 是 99.98% decoder-only (5226/5227)。 Worst 档下这个实验 backfires： (1) Removing 1 non-decoder model 什么都不改变 (Jaccard=1.0, C% identical)—— reviewer 说 \"this is a vacuous robustness check; with 1 non-decoder model, architecture stratification is meaningless\"； (2) 真正的问题是 IRT fit——RMSEA=0.087, CFI=0.73, |Lz|>2 仍然 97.8%—— \"decoder-only homogeneity doesn't fix IRT misspecification because the misfit comes from 57-subject multidimensionality, not architecture mixing\"； (3) Reviewer 的核心反驳：\"You showed architecture isn't the problem — fine. But you still haven't addressed THE problem: multidimensional ability with 1D matching. Removing 1 model is irrelevant; fitting a multidimensional IRT model is what's needed.\"； (4) 实验在 paper_framing 中被列为 \"✅ RESOLVED\"，但 worst 档 reviewer 认为 它 resolved a non-issue while ignoring the actual issue。\n"
254	  },
255	  {
256	    "name": "semi_synthetic_contamination_validation",
257	    "description": "Known contamination injection into real METABENCH matrix — controlled ground truth",
258	    "results": {
259	      "n_clean_items_selected": 500,
260	      "n_injected_items": 200,
261	      "temporal_external_tpr_p0": 0.326,
262	      "temporal_external_tpr_p03": 0.548,
263	      "temporal_external_tpr_p05": 0.834,
264	      "temporal_external_tpr_p10": 1.0,
265	      "temporal_external_fpr": 0.314,
266	      "temporal_external_delta_tpr_p05": 0.508,
267	      "temporal_external_delta_tpr_p10": 0.674,
268	      "ability_external_tpr_p10": 0.8,
269	      "ability_external_fpr": 0.493,
270	      "standard_mh_fpr_inflation_at_p10": "0.298→0.616",
271	      "matching_variable_contamination": true,
272	      "cross_subject_delta_fpr": 0.0
273	    },
274	    "tables": [
275	      "Table: Semi-synthetic TPR/FPR across injection rates — reviewer annotates baseline FPR as 'the real story'",
276	      "Table: Standard vs cross-subject matching — ΔFPR=0.000 is acknowledged but Q3 caveat raised"
277	    ],
278	    "figures": [],
279	    "analysis": "Semi-synthetic 在 worst 档下从 \"validates DIF\" 被重新解读为 \"validates that injecting signal into a high-FPR detector produces more flags.\" Cross-subject matching (ΔFPR=0.000) 是 最 defensible 的技术结果，但被 reviewer 用 Q3 cross-subject correlation 削弱。 在 reframe 路径 A（Framework-first）中，这个实验升为 primary contribution—— 即使 reviewer 攻击 MMLU DIF 本身，framework 的 reusability 和 ΔFPR=0.000 innovation 仍有独立价值。这是 worst 档下最有 salvage potential 的实验。\n\n与 registry 一致。Semi-synthetic 是 paper 最强技术贡献，但 worst 档下： (1) baseline FPR=0.314——\"even before injection, 31.4% items are flagged. ΔTPR is measured against this inflated baseline, so the 'detection power' is really 'additional flags on top of already-massive false positive rate'\"； (2) Reviewer 的关键攻击：ΔTPR=0.508 at p=0.5 means \"if half the focal group memorizes an item, DIF has 50% chance of catching it ON TOP of 31% baseline noise. In absolute terms, you flag 83.4% of injected items — but you also flag 31.4% of clean items. Your precision is ~(0.508×200)/(0.508×200+0.314×300) ≈ 52%.\"； (3) injection mechanism (incorrect→correct flip) 是 simplification—— \"real contamination doesn't flip all wrong answers to correct; partial memorization produces answer-distribution shifts, not binary flips\"； (4) FPR inflation under standard matching (0.298→0.616) 虽然被 cross-subject matching 解决 (ΔFPR=0.000)，但 reviewer 质疑 cross-subject matching 本身： \"using other-subject scores as matching variable assumes subjects are independent — but Q3 analysis (plan_013) showed cross-subject |Q3| can reach 0.20+\"； (5) 最深层攻击：injection into a matrix where 1D IRT is already misspecified → \"you're testing detection power of a misspecified method on a misspecified baseline; positive ΔTPR doesn't validate the method, it validates that adding signal to a noisy detector shifts its output\"。 尽管如此，ΔTPR dose-response (0.3→0.5→0.7→1.0 : 0.548→0.834→0.99→1.0) 和 cross-subject ΔFPR=0.000 仍然是 technically impressive，reviewer 不否认技术执行， 而是质疑其 interpretive value given misspecification。\n"
280	  }
281	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc1410fc-59f1-4b32-b471-bd594c78e9e1",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "eced7b09-9b64-4772-9bc2-9b649ef42ef1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"real_data_dif_mmlu\",\n    \"description\": \"METABENCH MMLU 5,227×12,508 response matrix 上的 MH-DIF 分析\",\n    \"results\": {\n      \"temporal_ets_c_pct\": 31.3,\n      \"temporal_fpr_li_clean\": 0.318,\n      \"temporal_enrichment\": 0.96,\n      \"ability_ets_c_pct\": 2.9,\n      \"within_family_llama2v3_c_pct\": 61.3,\n      \"domain_spearman_rho\": 0.307,\n      \"domain_spearman_p\": 0.02,\n      \"sanity_random_split_c_pct\": 0.18,\n      \"irt_lz_pct_above_2\": 98,\n      \"reviewer_interpretation\": \"artifact_of_misspecification\"\n    },\n    \"tables\": [\n      \"Table 1: Temporal DIF results — C%=31.3%, enrichment=0.96 — reviewer 标注 'enrichment≈1 = no detection value'\",\n      \"Table 2: Cohort comparison — ability split C%=2.9% vs temporal 31.3% — reviewer 认为差异来自 ability shift 而非 item-level effect\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reviewer 的核心攻击：31.3% 是一个 misspecified model 下的 baseline rate，不是 finding。 类比：如果你用线性回归拟合非线性数据，residual patterns 不代表新发现，而代表 model misfit。 MH-DIF on multidimensional data with 1D matching = structural Type I error inflation。 Llama-2 vs Llama-3 within-family C%=61.3% 被读为更强的证据——\\\"同一 family 内 61% items show DIF = 显然是 ability structure change, not contamination\\\"。\\n\\n\\n数据本身与已完成 registry 一致——31.3% C% 是真实观测。但在 worst 档下，reviewer 的解读路径是： (1) 98% 模型 |Lz|>2 表明 1D IRT ability estimates 系统性不可靠； (2) MH 的 ability matching 依赖 total score 作为 ability proxy，而 MMLU 57 subjects 的 multidimensionality 意味着 total score 是一个 collapsed composite，无法真正 match ability； (3) 因此 31.3% C% 中有大量是 ability confounding 造成的 spurious DIF—— 两个模型在不同 subject domains 上能力结构不同，但 total score 相近，被 MH 视为 \\\"matched\\\"， 实际上它们在特定 subject 上的 ability 并不 matched； (4) enrichment≈0.96 直接验证了 DIF flags 与已知 contamination labels 无关联—— reviewer 读为 \\\"你的方法检测不到 contamination\\\"； (5) 0.18% sanity check 虽然证明不是纯噪声，但 reviewer 认为这只是证明 temporal cohort 之间 确实存在 ability distribution shift，而非 item-level contamination。 ρ=0.307 (p=0.02) 被 reviewer 解读为 \\\"domain improvement 是 confound 的证据， 不是被排除的证据\\\"——因为 item-level decomposition (plan_019) 的 pseudo R²=0.0007 只说明 linear relationship 弱，不排除 nonlinear 或 interaction effects。\\n\"\n  },\n  {\n    \"name\": \"rl_robustness_validation\",\n    \"description\": \"验证 DIF 对 reasoning-RL 模型（GRPO/PPO）的鲁棒性\",\n    \"results\": {\n      \"n_reasoning_rl_models\": 13,\n      \"alignment_rl_cohort_n\": 477,\n      \"grpo_cohort_dif_c_pct\": 34.8,\n      \"sft_baseline_dif_c_pct\": 30.2,\n      \"alignment_rl_dif_c_pct\": 31.9,\n      \"jaccard_sft_vs_grpo\": 0.71,\n      \"delong_p_dif_vs_constat\": 0.38,\n      \"tost_equivalence_p\": 0.22,\n      \"constat_auroc_on_rl\": 0.54,\n      \"mink_auroc_on_rl\": 0.51,\n      \"dif_auroc_on_rl\": 0.58,\n      \"bootstrap_ci_auroc_dif\": [\n        0.41,\n        0.73\n      ],\n      \"power_at_p04\": 0.12,\n      \"power_at_p07\": 0.43,\n      \"power_at_p10\": 0.68\n    },\n    \"tables\": [\n      \"Table: AUROC comparison across 3 methods × 3 cohort types — all CIs overlap, no method dominates\",\n      \"Table: Power curve p ∈ [0.4, 1.0] — reviewer notes 'useful range starts at p≥0.7, narrowing practical applicability'\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reviewer consensus: \\\"N=13 RL models is a pilot, not a validation. The authors cannot claim RL-robustness based on mixing 13 models into a 600+ cohort — the signal is drowned. Individual-model analysis (ConStat/Min-K%) at least tests each model; DIF by design cannot. This is a structural limitation of group-level methods, acknowledged but not resolved.\\\" 致命打击：reviewer 将此解读为 DIF 的固有缺陷——无法做 per-model detection——而非优势。\\n\\n\\nWorst 档下的问题不是实验跑不出来，而是 N=13 reasoning-RL 模型被 reviewer 视为 fundamentally underpowered： (1) 13 个 GRPO/PPO 模型混入 focal cohort 后，C% 从 30.2% 微升到 34.8%—— reviewer 解读为 \\\"adding stronger models → more ability confounding → more spurious DIF\\\"， 而非 \\\"DIF robust to RL\\\"； (2) AUROC 比较（DIF 0.58 vs ConStat 0.54 vs Min-K% 0.51）差异不显著（DeLong p=0.38）， bootstrap CI 跨越 0.5——reviewer 说 \\\"all methods are at chance, you've shown nothing\\\"； (3) TOST equivalence test p=0.22，无法 reject \\\"DIF 和传统方法等效\\\" 的 H0—— reviewer 认为 \\\"failure to demonstrate equivalence or superiority = uninformative\\\"； (4) Power analysis 显示 p=0.4 时 TPR=0.12——reviewer 说 \\\"DIF can only detect near-complete exploitation, which is the trivial case\\\"； (5) 核心问题：整个实验无法区分 \\\"DIF works on RL models\\\" 和 \\\"DIF produces same artifacts regardless of model type\\\"——在 IRT misspecification 框架下，两者不可区分。\\n\"\n  },\n  {\n    \"name\": \"constat_perturbation_eval\",\n    \"description\": \"ConStat-style perturbation testing 在 MMLU 上的独立评估\",\n    \"results\": {\n      \"n_items_reformulated\": 220,\n      \"reformulation_quality_human_eval\": 0.82,\n      \"constat_detection_rate_non_rl\": 0.41,\n      \"constat_detection_rate_rl\": 0.08,\n      \"constat_fdr_controlled_rate\": 0.23,\n      \"constat_vs_dif_overlap_pct\": 12.7,\n      \"constat_fpr\": 0.067,\n      \"constat_unique_detections\": 158,\n      \"dif_unique_detections\": 892\n    },\n    \"tables\": [\n      \"Table: ConStat vs DIF detection comparison — ConStat lower recall but much lower FPR\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reviewer 用 ConStat 的低 FPR 作为武器：\\\"ConStat achieves controlled FPR by design (FDR correction); DIF's 31.8% FPR on Li-clean items means nearly 1 in 3 flags is false, and you cannot tell which ones without ground truth.\\\" 这强化了 \\\"DIF C% is inflated by misspecification\\\" 的叙事。\\n\\n\\nConStat 在 non-RL 模型上表现合理（41% detection rate），FPR 远低于 DIF（0.067 vs 0.318）。 Worst 档下 reviewer 解读： (1) ConStat FPR=0.067 vs DIF FPR=0.318——\\\"DIF 的高 detection rate 主要来自高 FPR， 不是真正的 detection power\\\"； (2) 12.7% overlap 表明两种方法检测的是完全不同的现象——reviewer 认为 ConStat 检测 actual contamination (perturbation sensitivity)，而 DIF 检测 ability shift artifact； (3) ConStat 在 RL 模型上确实退化（8%），但 reviewer 说 \\\"at least ConStat has a clear mechanism story; DIF's mechanism is unfalsifiable because any result can be attributed to either contamination or ability change\\\"； (4) 220 items 的 reformulation 质量（0.82 human eval）足够，但 scope 太小—— reviewer 要求 full-scale replication 才能比较。\\n\"\n  },\n  {\n    \"name\": \"dvd_generation_variance_eval\",\n    \"description\": \"DVD generation variance 在 MMLU 上的独立评估\",\n    \"results\": {\n      \"n_models_evaluated\": 12,\n      \"n_items_per_model\": 200,\n      \"n_generations_per_item\": 50,\n      \"bimodal_detection_rate\": 0.14,\n      \"variance_based_detection_rate\": 0.22,\n      \"dvd_vs_dif_overlap\": 0.09,\n      \"dvd_fpr\": 0.04,\n      \"gpu_hours_used\": 65,\n      \"variant_contamination_detected\": 31\n    },\n    \"tables\": [\n      \"Table: DVD detection rates by contamination type (verbatim vs variant) — low overall\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DVD 作为独立信号太弱（14% bimodal detection），且 per-model inference 的 cost 使其不 scalable。 Reviewer 建议 \\\"DVD is better suited as a follow-up diagnostic on flagged items, not a primary detector\\\" ——削弱 ensemble 的 motivation。\\n\\n\\nDVD 需要 per-model inference access（50 generations × 200 items × 12 models = 120K generations）， cost 高但可行。Worst 档下： (1) Bimodal detection rate 仅 14%——reviewer 说 \\\"variant contamination is rare or this method is underpowered, either way not compelling\\\"； (2) 9% overlap with DIF——再次证明方法检测不同现象，但 worst 档下 reviewer 解读为 \\\"three orthogonal weak signals don't add up to one strong signal\\\"； (3) DVD FPR=0.04 很低，但 detection rate 也低——reviewer 认为 precision-recall tradeoff 不足以支撑 contribution； (4) 12 models 太少——reviewer 要求 \\\"at minimum 50+ models to characterize generation variance distribution\\\"，而 GPU budget 不支持。\\n\"\n  },\n  {\n    \"name\": \"ensemble_fusion\",\n    \"description\": \"DIF + ConStat + DVD 三信号融合\",\n    \"results\": {\n      \"majority_vote_precision\": 0.38,\n      \"majority_vote_recall\": 0.09,\n      \"weighted_fusion_precision\": 0.44,\n      \"weighted_fusion_recall\": 0.15,\n      \"ensemble_fpr\": 0.087,\n      \"cross_val_weight_stability\": \"low — std/mean > 0.6 across folds\",\n      \"dif_weight\": 0.28,\n      \"constat_weight\": 0.51,\n      \"dvd_weight\": 0.21,\n      \"uniform_baseline_vs_optimized_delta_f1\": 0.02\n    },\n    \"tables\": [\n      \"Table: Ensemble configurations — all recall < 0.20, precision < 0.50\",\n      \"Table: Cross-validation fold weights — high variance across folds\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Ensemble 在 paper 中降级为 appendix negative result。Reviewer 的结论性评价： \\\"The ensemble experiment confirms what the low pairwise overlaps predicted — these methods detect different phenomena (or noise), and combining them doesn't produce a coherent detector. This is informative but not a contribution; it's a null result.\\\"\\n\\n\\nEnsemble 在 worst 档下彻底失败，原因链： (1) 三个信号 overlap 极低（pairwise Jaccard < 0.15）→ majority vote 几乎不触发（recall 9%）； (2) 加权融合稍好但 cross-validation 权重不稳定（std/mean > 0.6）——reviewer 说 \\\"overfitting to a small calibration set with unstable weights is not a methodology contribution\\\"； (3) Optimized vs uniform weight F1 差异仅 0.02——\\\"no evidence that learned fusion outperforms naive averaging, suggesting insufficient signal diversity\\\"； (4) DIF weight 仅 0.28（最低），ConStat 0.51——reviewer 读为 \\\"even the ensemble downweights DIF, your supposed primary contribution\\\"； (5) FPR=0.087 达标（<0.10），但 recall=0.15 意味着 85% contamination 未检测—— \\\"an ensemble that misses 85% of contaminated items is not operationally useful\\\"。 核心问题：Claim 2（ensemble = contribution）在 worst 档下被视为 negative result， 不是 contribution——\\\"showing that three weak detectors don't combine well is not novel\\\"。\\n\"\n  },\n  {\n    \"name\": \"cross_benchmark_gsm8k\",\n    \"description\": \"GSM8K 上复制 DIF 分析，用 GSM1K 作为 contamination ground truth\",\n    \"results\": {\n      \"gsm8k_n_items\": 1319,\n      \"gsm8k_n_ref\": 1017,\n      \"gsm8k_n_foc\": 804,\n      \"gsm8k_standard_c_pct\": 18.9,\n      \"gsm8k_external_c_pct\": 47.4,\n      \"gsm8k_sanity_c_pct\": 0.3,\n      \"semi_synthetic_delta_tpr_p10\": 0.818,\n      \"gsm1k_n_models\": 33,\n      \"gsm1k_pearson_r\": -0.478,\n      \"gsm1k_pearson_p\": 0.005,\n      \"gsm1k_spearman_rho\": -0.403,\n      \"gsm1k_bca_ci_upper\": -0.155,\n      \"gsm1k_partial_r\": -0.385,\n      \"reviewer_dismiss_gsm1k\": true\n    },\n    \"tables\": [\n      \"Table: GSM1K correlation — r=-0.478 with wide CI, reviewer highlights N=33 limitation\",\n      \"Table: Semi-synthetic ΔTPR=0.818 — reviewer acknowledges but says 'synthetic ≠ real'\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"GSM8K semi-synthetic (ΔTPR=0.818) 是最强结果，但 reviewer 将其与 MMLU 主分析隔离： \\\"The GSM8K semi-synthetic result is impressive but says nothing about whether the 31.3% MMLU finding is real or artifact — different benchmark, different dimensionality, different N.\\\" GSM1K correlation 被 dismiss due to N=33 和 difficulty confound alternative explanation。\\n\\n\\n数据与 registry 一致。Worst 档下 reviewer 的攻击矩阵： (1) N=33 模型——\\\"33 data points with r=-0.478 is suggestive at best; BCa CI upper bound |r|=0.155 means the true effect could be trivially small\\\"； (2) 负相关方向 (r=-0.478) 与 contamination hypothesis 相反——DIF items 上 contamination gap 更小，不是更大。Paper 解释为 \\\"DIF items resist contamination-based gains\\\"， reviewer 替代解读：\\\"DIF items are simply harder items where all models struggle, contaminated or not — the negative correlation is a difficulty confound, not a detection signal\\\"； (3) Spearman CI [−0.687, −0.031] 上界接近 0——\\\"barely significant, and with N=33 a single influential point shifts everything\\\"（尽管 Cook's D robust, leave-one-out stable）； (4) GSM8K 是 single-domain math benchmark, MMLU 是 57-subject multidomain—— \\\"generalization from GSM8K to MMLU is not justified; the DIF mechanism operates differently on unidimensional vs multidimensional benchmarks\\\"； (5) GSM1K 本身作为 ground truth 被质疑——\\\"GSM1K measures a different construct (novel math problems) and the gap may reflect test-taking strategy differences, not contamination\\\"。 核心：A6 不成立——GSM1K 被 dismiss。\\n\"\n  },\n  {\n    \"name\": \"bifactor_irt_equating_pilot\",\n    \"description\": \"Bifactor IRT equating pilot — general factor + subject-specific factors\",\n    \"results\": {\n      \"bifactor_convergence\": false,\n      \"rmsea\": 0.089,\n      \"cfi\": 0.71,\n      \"tli\": 0.68,\n      \"srmr\": 0.112,\n      \"n_heywood_cases\": 47,\n      \"anchor_items_identified\": 0,\n      \"equated_score_rho\": null,\n      \"decision\": \"killed\"\n    },\n    \"tables\": [\n      \"Table: Bifactor fit indices — all below acceptable thresholds\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bifactor 失败在 worst 档下是 double-edged：不仅 equating 路径 dead， 还为 reviewer 提供了 \\\"see, even the authors tried to fix IRT misspecification and failed\\\" 的叙事。 在 reframe 路径 B（MIRT upgrade）中需要换 exploratory MIRT 或 mixture IRT 而非 confirmatory bifactor。\\n\\n\\n与 registry (plan_015 killed) 一致。Worst 档下 bifactor 失败的机制： (1) 12,508 items × 5,227 models 的 bifactor model（general + 57 subject factors） 参数空间巨大（~12,508 × 59 = ~738K parameters），mirt 不收敛； (2) 即使降到 subset（5 subjects, ~1,200 items），Heywood cases（负方差估计）出现 47 次—— 说明 data 不支持 bifactor structure，或者需要 constrained estimation； (3) RMSEA=0.089 > 0.06 cutoff, CFI=0.71 < 0.90 cutoff——fit 远低于 acceptable 标准； (4) 无法识别 anchor items（因为 model 本身不 fit）→ 整个 equating pipeline 断裂； (5) Reviewer 的解读最致命：\\\"You can't even fit a bifactor model to this data — this CONFIRMS that IRT assumptions are fundamentally violated for MMLU. If bifactor doesn't fit, your 1D MH-DIF is even more misspecified than we thought.\\\" 这个 killed experiment 在 worst 档下反而成为 reviewer 攻击 IRT misspecification 的额外弹药。\\n\"\n  },\n  {\n    \"name\": \"item_generation_calibration\",\n    \"description\": \"LLM 生成替换 items + student simulation 校准\",\n    \"results\": {\n      \"n_items_generated\": 500,\n      \"difficulty_rho_prompt_based\": 0.18,\n      \"difficulty_rho_student_sim\": 0.52,\n      \"target_difficulty_rho\": 0.75,\n      \"construct_alignment_human_eval\": 0.64,\n      \"holdout_panel_correlation\": 0.41,\n      \"replacement_quality_verdict\": \"below_benchmark\"\n    },\n    \"tables\": [\n      \"Table: Difficulty calibration — prompt-based vs student-sim vs target, all below threshold\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item generation 在 worst 档下是 Claim 3（benchmark regeneration）的棺材钉。 即使不考虑 bifactor failure，生成 items 的质量本身不足以支撑 \\\"operational replacement\\\" 的 claim。 Reviewer 建议 \\\"demote to future work\\\"——which is exactly what the reframe paths do。\\n\\n\\nWorst 档下 item generation 全面低于 benchmarks： (1) Prompt-based difficulty targeting ρ=0.18（文献报告 0.10-0.45 range 的下端）； (2) Student simulation 校准 ρ=0.52（文献报告 0.75-0.82 的下限以下）—— MMLU 的 domain diversity 使得单一 student simulator 无法准确估计 57 subjects 的 difficulty； (3) Construct alignment human evaluation 仅 0.64——36% 的生成 items 被判定 与原 item 不在同一 cognitive level 或 subject boundary 内； (4) Holdout model panel correlation 0.41——替换 items 上的 model ranking 与原 items ranking 相关性太低，equating 无法保证 score equivalence； (5) Reviewer 的攻击：\\\"If you can't generate calibrated replacement items, the entire benchmark regeneration pipeline is aspirational, not operational. This undermines Claim 3's practical value.\\\" 依赖 plan_005 的 anchor items 识别，而 plan_005 已 killed → 整条 pipeline dead。\\n\"\n  },\n  {\n    \"name\": \"cumulative_bayesian_dif\",\n    \"description\": \"Cumulative Bayesian DIF priors — 4 successive administrations模拟\",\n    \"results\": {\n      \"single_admin_power_d10\": 0.38,\n      \"cumulative_2_admin_power_d10\": 0.49,\n      \"cumulative_3_admin_power_d10\": 0.58,\n      \"cumulative_4_admin_power_d10\": 0.64,\n      \"target_cumulative_power\": 0.7,\n      \"simulation_only\": true,\n      \"real_data_validation\": \"none\"\n    },\n    \"tables\": [\n      \"Table: Power accumulation over 4 administrations — falls short of 0.70 target at δ=1.0\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Cumulative Bayesian DIF 在 worst 档下是 appendix filler，不贡献 novelty 也不贡献 empirical evidence。 Reviewer consensus: underdeveloped simulation study without real-data anchoring。\\n\\n\\nWorst 档下 cumulative Bayesian DIF 问题： (1) 即使 4 次 administration 后 power 仅 0.64，低于 target 0.70—— prior accumulation 的增益被 IRT misspecification 的 systematic bias 抵消； (2) 纯 simulation，无 real data validation——reviewer 说 \\\"simulation under your assumed generative model will always confirm your method; this is tautological\\\"； (3) \\\"4 successive administrations\\\" 假设 benchmark 不变——但如果 items 在 generation 之间 确实 drift（即你自己的 Claim 1），则 prior 积累的是 stale information； (4) Sinharay et al. (2006) 原始方法设计为 human testing with stable construct—— LLM benchmark 的 rapid capability shift 违反了 prior accumulation 的 stationarity 假设； (5) Reviewer 直接 dismiss：\\\"Simulation-only, no real data, questionable assumptions about temporal stationarity. Appendix material at best.\\\"\\n\"\n  },\n  {\n    \"name\": \"graceful_degradation_analysis\",\n    \"description\": \"Benchmark validity degradation under progressive item replacement\",\n    \"results\": {\n      \"rho_at_5pct_replacement\": 0.994,\n      \"rho_at_10pct_replacement\": 0.986,\n      \"rho_at_20pct_replacement\": 0.961,\n      \"rho_at_50pct_replacement\": 0.873,\n      \"reliability_alpha_original\": 0.94,\n      \"reliability_alpha_at_20pct\": 0.88,\n      \"construct_coverage_gap_at_20pct\": \"3 subjects lose >30% items\",\n      \"theoretical_bound_tight\": false\n    },\n    \"tables\": [\n      \"Table: Validity metrics × replacement rate — degradation faster than expected\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"在 bifactor 和 item generation 都失败的前提下，graceful degradation 变成 \\\"removing items\\\" 分析而非 \\\"replacing items\\\" 分析。与 plan_017 的 ρ≈0.997 冲突——removing DIF items 更安全 than replacing them with poorly calibrated alternatives。Reviewer 结论： \\\"The regeneration pipeline is not ready for deployment.\\\"\\n\\n\\nWorst 档下 graceful degradation 的问题： (1) 依赖 plan_005/006 的替换 items——两者都 failed/below benchmark， 因此 \\\"replacement\\\" 实际上是 random item removal，不是 calibrated replacement； (2) ρ at 20% replacement = 0.961 看似 ok，但 reviewer 用 plan_017 的结果反驳： \\\"You already showed ρ≈0.997 when removing 31% DIF items. Random replacement at 20% gives ρ=0.961 — WORSE than just removing items entirely. Your replacement items ADD noise.\\\"； (3) Reliability alpha 从 0.94 降到 0.88——\\\"degradation is measurable and concerning at only 20% replacement\\\"； (4) 3 subjects lose >30% items at 20% replacement rate——construct coverage 不均匀， 某些 domain 被 disproportionately 影响； (5) Theoretical bounds 不 tight——无法给出 \\\"replace up to X% safely\\\" 的 actionable threshold， 削弱 practical contribution。\\n\"\n  },\n  {\n    \"name\": \"item_focused_trees\",\n    \"description\": \"Item-Focused Trees (Tutz & Berger 2016) — continuous temporal covariate DIF\",\n    \"results\": {\n      \"ift_n_items_flagged\": 4102,\n      \"ift_vs_mh_jaccard\": 0.48,\n      \"ift_unique_flags\": 1834,\n      \"mh_unique_flags\": 1650,\n      \"ift_first_split_variable\": \"release_date\",\n      \"ift_interaction_with_size\": \"significant (p<0.01)\",\n      \"ift_temporal_granularity\": \"quarterly splits emerge naturally\"\n    },\n    \"tables\": [\n      \"Table: MH vs IFT flag comparison — 48% Jaccard, significant disagreement\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"IFT 本意是 \\\"alternative method validates MH\\\"，但 worst 档下 48% overlap 被读为 refutation。 Reviewer 的 steel-man 攻击：\\\"If items' DIF status depends on which method you use, the phenomenon is not robust — it's an artifact of methodological choices.\\\" IFT 降级为 appendix，与主 finding 的 tension 在 limitations 中 discuss。\\n\\n\\nIFT 在 worst 档下成为双刃剑： (1) IFT flags 4,102 items (32.8%) vs MH flags 3,918 (31.3%)——数量相近但 overlap 仅 48%， meaning 52% 的 flags 不一致； (2) Reviewer 解读：\\\"Two DIF methods on the same data flag different items — this means at least one (probably both) is detecting noise, not signal. If the phenomenon were real and large, methods should converge.\\\"； (3) IFT 的 continuous treatment 本身挑战了 MH 的 binary temporal split—— \\\"IFT shows the split is not clean at your chosen cutoff; DIF is gradual across the timeline, suggesting capability drift not contamination events\\\"； (4) IFT interaction with model size (p<0.01) 引入新 confound—— \\\"bigger models released later AND are more capable, so temporal DIF = size+capability confound\\\"； (5) IFT 作为 robustness check 未能 confirm MH——在 worst 档下这是 negative evidence。\\n\"\n  },\n  {\n    \"name\": \"architecture_stratified_dif\",\n    \"description\": \"Decoder-only 子群内 DIF 分析 — 测试 architecture heterogeneity 影响\",\n    \"results\": {\n      \"n_decoder_only\": 5226,\n      \"n_non_decoder\": 1,\n      \"decoder_only_c_pct\": 31.3,\n      \"full_population_c_pct\": 31.3,\n      \"jaccard_decoder_vs_full\": 1.0,\n      \"rmsea_decoder_only\": 0.087,\n      \"cfi_decoder_only\": 0.73,\n      \"tlr_decoder_only\": 0.7,\n      \"irt_lz_pct_above_2_decoder_only\": 97.8\n    },\n    \"tables\": [\n      \"Table: Full vs decoder-only DIF — identical results, confirming architecture is not the confound\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Architecture stratification 是一个 true-but-trivial result。99.98% decoder-only 意味着 这个 check 从设计上就不可能找到 architecture effect。Reviewer 用它作为 \\\"authors address the wrong confound\\\" 的证据——the real confound is multidimensionality, not architecture。 在 reframe 路径下，这个实验仍然 reportable but not defensive。\\n\\n\\n与 paper_framing 一致——METABENCH MMLU 是 99.98% decoder-only (5226/5227)。 Worst 档下这个实验 backfires： (1) Removing 1 non-decoder model 什么都不改变 (Jaccard=1.0, C% identical)—— reviewer 说 \\\"this is a vacuous robustness check; with 1 non-decoder model, architecture stratification is meaningless\\\"； (2) 真正的问题是 IRT fit——RMSEA=0.087, CFI=0.73, |Lz|>2 仍然 97.8%—— \\\"decoder-only homogeneity doesn't fix IRT misspecification because the misfit comes from 57-subject multidimensionality, not architecture mixing\\\"； (3) Reviewer 的核心反驳：\\\"You showed architecture isn't the problem — fine. But you still haven't addressed THE problem: multidimensional ability with 1D matching. Removing 1 model is irrelevant; fitting a multidimensional IRT model is what's needed.\\\"； (4) 实验在 paper_framing 中被列为 \\\"✅ RESOLVED\\\"，但 worst 档 reviewer 认为 它 resolved a non-issue while ignoring the actual issue。\\n\"\n  },\n  {\n    \"name\": \"semi_synthetic_contamination_validation\",\n    \"description\": \"Known contamination injection into real METABENCH matrix — controlled ground truth\",\n    \"results\": {\n      \"n_clean_items_selected\": 500,\n      \"n_injected_items\": 200,\n      \"temporal_external_tpr_p0\": 0.326,\n      \"temporal_external_tpr_p03\": 0.548,\n      \"temporal_external_tpr_p05\": 0.834,\n      \"temporal_external_tpr_p10\": 1.0,\n      \"temporal_external_fpr\": 0.314,\n      \"temporal_external_delta_tpr_p05\": 0.508,\n      \"temporal_external_delta_tpr_p10\": 0.674,\n      \"ability_external_tpr_p10\": 0.8,\n      \"ability_external_fpr\": 0.493,\n      \"standard_mh_fpr_inflation_at_p10\": \"0.298→0.616\",\n      \"matching_variable_contamination\": true,\n      \"cross_subject_delta_fpr\": 0.0\n    },\n    \"tables\": [\n      \"Table: Semi-synthetic TPR/FPR across injection rates — reviewer annotates baseline FPR as 'the real story'\",\n      \"Table: Standard vs cross-subject matching — ΔFPR=0.000 is acknowledged but Q3 caveat raised\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Semi-synthetic 在 worst 档下从 \\\"validates DIF\\\" 被重新解读为 \\\"validates that injecting signal into a high-FPR detector produces more flags.\\\" Cross-subject matching (ΔFPR=0.000) 是 最 defensible 的技术结果，但被 reviewer 用 Q3 cross-subject correlation 削弱。 在 reframe 路径 A（Framework-first）中，这个实验升为 primary contribution—— 即使 reviewer 攻击 MMLU DIF 本身，framework 的 reusability 和 ΔFPR=0.000 innovation 仍有独立价值。这是 worst 档下最有 salvage potential 的实验。\\n\\n与 registry 一致。Semi-synthetic 是 paper 最强技术贡献，但 worst 档下： (1) baseline FPR=0.314——\\\"even before injection, 31.4% items are flagged. ΔTPR is measured against this inflated baseline, so the 'detection power' is really 'additional flags on top of already-massive false positive rate'\\\"； (2) Reviewer 的关键攻击：ΔTPR=0.508 at p=0.5 means \\\"if half the focal group memorizes an item, DIF has 50% chance of catching it ON TOP of 31% baseline noise. In absolute terms, you flag 83.4% of injected items — but you also flag 31.4% of clean items. Your precision is ~(0.508×200)/(0.508×200+0.314×300) ≈ 52%.\\\"； (3) injection mechanism (incorrect→correct flip) 是 simplification—— \\\"real contamination doesn't flip all wrong answers to correct; partial memorization produces answer-distribution shifts, not binary flips\\\"； (4) FPR inflation under standard matching (0.298→0.616) 虽然被 cross-subject matching 解决 (ΔFPR=0.000)，但 reviewer 质疑 cross-subject matching 本身： \\\"using other-subject scores as matching variable assumes subjects are independent — but Q3 analysis (plan_013) showed cross-subject |Q3| can reach 0.20+\\\"； (5) 最深层攻击：injection into a matrix where 1D IRT is already misspecified → \\\"you're testing detection power of a misspecified method on a misspecified baseline; positive ΔTPR doesn't validate the method, it validates that adding signal to a noisy detector shifts its output\\\"。 尽管如此，ΔTPR dose-response (0.3→0.5→0.7→1.0 : 0.548→0.834→0.99→1.0) 和 cross-subject ΔFPR=0.000 仍然是 technically impressive，reviewer 不否认技术执行， 而是质疑其 interpretive value given misspecification。\\n\"\n  }\n]",
      "numLines": 281,
      "startLine": 1,
      "totalLines": 281
    }
  },
  "sourceToolAssistantUUID": "cc1410fc-59f1-4b32-b471-bd594c78e9e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T06:49:10.607Z_

<details><summary>↩ Tool result · `toolu_016mJnSJ9oRvhzeJLuNGPCMg`</summary>

```text
1	# Paper Framing — irt_equated_bench_regen
2	
3	## Target Venue
4	- Primary: ICLR 2027 (expected deadline ~October 2026)
5	
6	## Paper Type
7	Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."
8	
9	## Core Claims (4 条, 可证伪)
10	
11	**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
12	- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)
13	- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
14	- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.
15	
16	**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
17	- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
18	- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"
19	
20	**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
21	- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
22	- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
23	- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability
24	
25	**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
26	1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
27	2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
28	3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
29	4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
30	- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
31	- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
32	- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
33	- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed
34	
35	## Story Spine (v2 — no-pivot narrative)
36	
37	**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.
38	
39	**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**
40	
41	**What we find** (4 contributions, focused):
42	
43	1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."
44	
45	2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.
46	
47	3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.
48	
49	4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).
50	
51	**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations."
52	
53	## Scope Control (main body vs appendix)
54	
55	**MAIN BODY (4 claims + robustness)**:
56	- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
57	- §2 Related Work (45 papers, 5 clusters)
58	- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
59	- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
60	- §5 Discussion + Limitations
61	- §6 Conclusion
62	
63	**APPENDIX (pruned from main body)**:
64	- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
65	- RL robustness (plan_002) — N=13, underpowered
66	- Ensemble fusion (plan_003a/b/c) — negative, not executed
67	- Bifactor equating pilot — below target fit
68	- Item generation pilot — below benchmarks
69	- Graceful degradation — clean but supplementary
70	- Item-Focused Trees — robustness check, supplementary
71	- ConStat/DVD comparisons — complementary baselines
72	
73	## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks
74	
75	Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.
76	
77	## Venue Fit
78	
79	- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
80	
81	## Novelty Articulation (三层，显式化)
82	
83	MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:
84	
85	1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.
86	
87	2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).
88	
89	3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).
90	
91	**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."
92	
93	## Anticipated Reviewer Concerns (updated for pivot)
94	
95	1. **"38% could just mean models got better"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.
96	
97	2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.
98	
99	3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.
100	
101	4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.
102	
103	5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.
104	
105	6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.
106	
107	7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.
108	
109	8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.
110	
111	9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."
112	
113	10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.
114	
115	11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.
116	
117	## Dropped from Original Framing
118	
119	- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
120	- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
121	- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
122	- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."
123	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f296f4df-2161-44c1-988d-a9244640d7f1",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "67d99cb1-1151-4ca7-ba13-104f89a166cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper_framing.md",
      "content": "# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% BCa CI [−0.714, −0.155]; Spearman ρ=−0.403, p=0.020, CI [−0.687, −0.031]; partial r=−0.385 controlling GSM8K accuracy, p=0.030, CI [−0.640, −0.058]; permutation p=0.014). All CIs exclude zero. Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. Cross-benchmark: DIF items resist contamination-based gains (r=−0.478, BCa CI [−0.71, −0.16]).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF items resist contamination-based gains (r=−0.478) and serve as a diagnostic lens for understanding what changed across model generations.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — ✅ RESOLVED (plan_019). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%). Subject-level ρ=0.307 is an ecological correlation that grossly overstates the item-level relationship (pseudo R²=0.0007). The instability is predominantly item-specific. Present Model 1 (2.4pp) as primary; acknowledge confounder-vs-mediator ambiguity in Model 2 as honest discussion.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  },
  "sourceToolAssistantUUID": "f296f4df-2161-44c1-988d-a9244640d7f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T06:49:10.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_016mJnSJ9oRvhzeJLuNGPCMg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eced7b09-9b64-4772-9bc2-9b649ef42ef1",
  "isSidechain": false,
  "requestId": "req_011CbFGVomAoMjQ68LrG63D8",
  "type": "assistant",
  "uuid": "f296f4df-2161-44c1-988d-a9244640d7f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmFxVmTn53TpRFftTsrFrE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11910,
      "cache_read_input_tokens": 11841,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11910
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "67d99cb1-1151-4ca7-ba13-104f89a166cb",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case review simulation paper",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Assistant

_source line 14 · 2026-05-21T06:49:27.925Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me now write the "worst" tier paper — this is a dream simulation where the paper faces the harshest reviewer interpretation. The narrative guidance says:

- Novelty is thoroughly denied ("applying textbook MH 1988 to new data ≠ contribution")
- IRT misspecification is seen as fundamental flaw (98% |Lz|>2 → ability matching systematically biased → 31% C% is artifact not finding)
- Semi-synthetic framework too simple to publish
- Meta-critique dismissed as obvious
- Each experiment's results reinterpreted as artifact or underpowered/scope-limited


- 2-3 of 3 reviewers give reject, average 3.5, novelty sub-score 1.5

I need to write the paper as-is (the original paper the authors would submit), but framed in a way that makes the reviewers' worst-case interpretations plausible. The paper should present the actual data from experiment_data.json faithfully, but the presentation should highlight the vulnerabilities that lead to rejection. Let me now draft a complete LaTeX paper covering all experiments with sections and tables for each one in the JSON.

I'm mapping out the full experiment list and planning the paper structure with abstract, introduction, brief related work, and methods sections, then results for each of the thirteen experiments.

Writing LaTeX template...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67d99cb1-1151-4ca7-ba13-104f89a166cb",
  "isSidechain": false,
  "requestId": "req_011CbFGW5rYjVoUmUtR5vt2S",
  "type": "assistant",
  "uuid": "35fa34ea-d1d5-4e96-979c-c96ffe6d27f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUAN1Ptx2Y5gL5VCP6KE3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16320,
      "cache_read_input_tokens": 23751,
      "output_tokens": 739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 739,
          "cache_read_input_tokens": 23751,
          "cache_creation_input_tokens": 16320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16320
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

_source line 15 · 2026-05-21T06:49:27.973Z_

Now I have both files. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35fa34ea-d1d5-4e96-979c-c96ffe6d27f5",
  "isSidechain": false,
  "requestId": "req_011CbFGW5rYjVoUmUtR5vt2S",
  "type": "assistant",
  "uuid": "d218176c-4446-40d3-b559-e52471e265a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUAN1Ptx2Y5gL5VCP6KE3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16320,
      "cache_read_input_tokens": 23751,
      "output_tokens": 739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 739,
          "cache_read_input_tokens": 23751,
          "cache_creation_input_tokens": 16320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16320
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

_source line 16 · 2026-05-21T06:49:30.323Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KmKew9qBBD1o3qqkjjcz3X`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d218176c-4446-40d3-b559-e52471e265a0",
  "isSidechain": false,
  "requestId": "req_011CbFGW5rYjVoUmUtR5vt2S",
  "type": "assistant",
  "uuid": "d07a52a6-aae2-4f03-b18e-e8a380fa10ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUAN1Ptx2Y5gL5VCP6KE3s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16320,
      "cache_read_input_tokens": 23751,
      "output_tokens": 739,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16320,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 739,
          "cache_read_input_tokens": 23751,
          "cache_creation_input_tokens": 16320,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16320
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

_source line 17 · 2026-05-21T06:49:30.484Z_

<details><summary>↩ Tool result · `toolu_01KmKew9qBBD1o3qqkjjcz3X`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d07a52a6-aae2-4f03-b18e-e8a380fa10ce",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "3abb2a15-9605-4d10-95d5-e1c240542994",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "d07a52a6-aae2-4f03-b18e-e8a380fa10ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T06:52:40.895Z_

<details open><summary>🔧 Tool call — Write · `toolu_01NkUmr3pzjsXHFTDiXMp1yK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper.tex",
  "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric DIF Analysis Reveals 31\\% Temporal Item Instability\\\\in MMLU: A Large-Scale Characterization of Benchmark Measurement Properties}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%%  ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWhen we compare language model scores across time, we implicitly assume that benchmark items function identically for all model cohorts.\nWe test this assumption by applying Mantel--Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items)---the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of items exhibit large DIF (ETS Category~C, $|\\Delta_{\\mathrm{MH}}|\\!\\ge\\!1.5$) between 2023 and 2024-H1 model cohorts, robust across thresholds (10--49\\% at $|\\Delta|\\in[1.0,2.5]$), not explained by domain-level capability improvement ($\\le$7.6\\%), and architecturally homogeneous (99.98\\% decoder-only).\nWe show that the field's standard web-overlap contamination labels cannot validate item-level differential detectors (enrichment$\\approx$1.0) and propose a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR$=$0.000).\nDespite 31\\% instability, MMLU model rankings are massively redundant ($\\rho\\!\\approx\\!0.997$), and DIF items serve as a diagnostic lens---identifying \\emph{which} capability dimensions shift across generations rather than flagging ``bad'' items.\nCross-benchmark replication on GSM8K (1{,}319 items $\\times$ 6{,}702 models) confirms framework portability ($\\Delta$TPR$=+$0.818) and shows DIF items resist contamination-based gains ($r\\!=\\!-0.478$, $p\\!=\\!0.005$).\n\\end{abstract}\n\n%% ============================================================\n%%  1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmarks such as MMLU~\\citep{hendrycks2021measuring} are the primary yardstick for comparing language models.\nTemporal comparisons---``GPT-4 surpasses GPT-3.5 on MMLU''---rest on an untested assumption: that every item measures the same construct with the same difficulty for every model cohort.\nPsychometrics has a mature tool for evaluating exactly this assumption: \\emph{Differential Item Functioning} (DIF) analysis, which detects items whose difficulty changes across groups after controlling for overall ability~\\citep{holland1988differential}.\n\nWe apply the Mantel--Haenszel (MH) DIF procedure---unchanged since 1988---to the METABENCH response matrix comprising 5{,}227 models and 12{,}508 MMLU items.\nWe do \\emph{not} claim algorithmic novelty; MH-DIF is a textbook method.\nOur contributions are empirical:\n\n\\begin{enumerate}\n    \\item \\textbf{Temporal instability at scale.}\n    31.3\\% of MMLU items are ETS Category~C between 2023 and 2024-H1 cohorts.\n    This is not a statistical artifact (random-split sanity: 0.18\\%), not driven by capability improvement ($\\le$7.6\\%), and robust to threshold choice.\n    \\item \\textbf{Ground-truth meta-critique.}\n    Web-overlap contamination labels (e.g., Li et al.) measure global exposure, not differential contamination.\n    Enrichment$\\approx$1.0 is the expected outcome, not method failure.\n    \\item \\textbf{Semi-synthetic validation framework.}\n    $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000).\n    Portable to GSM8K ($\\Delta$TPR$=+$0.818).\n    \\item \\textbf{DIF as diagnostic lens.}\n    Despite 31\\% instability, rankings are stable ($\\rho\\!\\approx\\!0.997$).\n    DIF items are the \\emph{least} disruptive non-random removal strategy ($z\\!=\\!-9.5$ vs.\\ accuracy-gap $z\\!=\\!-157$), isolating genuine differential functioning.\n\\end{enumerate}\n\n\\paragraph{Key framing.}\nInstability $\\neq$ invalidity.\nDIF flags items whose measurement properties changed---a diagnostic signal, not a quality verdict.\nMMLU rankings survive 31\\% item removal because the benchmark is massively redundant.\nDIF tells us \\emph{what changed}, not ``what is broken.''\n\n%% ============================================================\n%%  2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM benchmark contamination.}\nWeb-overlap and $n$-gram methods~\\citep{li2024task} identify publicly available items but do not assess \\emph{differential} item functioning.\nConStat~\\citep{constat2024} uses perturbation testing; Min-K\\%~\\citep{shi2024detecting} uses token-level statistics.\nBoth operate per-model, unlike DIF which is a group-level method.\n\n\\paragraph{Differential Item Functioning.}\nThe MH procedure~\\citep{mantel1959statistical,holland1988differential} tests whether item difficulty differs between focal and reference groups after conditioning on total score.\nETS classifies items as A ($|\\Delta_{\\mathrm{MH}}|<1.0$), B ($1.0$--$1.5$), or C ($\\ge\\!1.5$).\nDIF analysis has been standard in educational testing for decades.\n\n\\paragraph{IRT and LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation~\\citep{irt_llm2024}, though IRT model fit for multidimensional benchmarks remains challenging.\n\n%% ============================================================\n%%  3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Mantel--Haenszel DIF}\n\nGiven a binary response matrix $\\mathbf{X}\\in\\{0,1\\}^{N\\times J}$ ($N$ models, $J$ items), we partition models into a \\emph{reference} group (2023 cohort) and a \\emph{focal} group (2024-H1 cohort).\nFor each item $j$ and total-score stratum $k$, the MH statistic tests the null hypothesis that the item--group odds ratio is 1.\nThe effect size $\\Delta_{\\mathrm{MH}}$ (in ETS delta units) quantifies the magnitude.\nItems with $|\\Delta_{\\mathrm{MH}}|\\ge 1.5$ and statistically significant MH $\\chi^2$ are classified as ETS Category~C.\n\n\\paragraph{IRT fit caveat.}\nMH conditions on total score as an ability proxy.\nOn MMLU (57 subjects), the unidimensional IRT model is misspecified: 98\\% of models show person-fit $|L_z|>2$.\nTotal score collapses a multidimensional ability space into a single composite.\nThis is a known limitation throughout the paper.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo evaluate DIF detection power with known ground truth, we inject controlled contamination into the real METABENCH response matrix:\n\\begin{enumerate}\n    \\item Select $n_{\\mathrm{clean}}$ items with no DIF signal as ``clean'' items.\n    \\item For each ``injected'' item, flip a fraction $p$ of focal-group incorrect responses to correct, simulating differential contamination.\n    \\item Run MH-DIF on the modified matrix and measure $\\Delta\\text{TPR} = \\text{TPR}_{\\text{injected}} - \\text{TPR}_{\\text{baseline}}$.\n\\end{enumerate}\n\n\\paragraph{Cross-subject matching.}\nStandard MH uses total score (all subjects) as matching variable.\nWhen contamination affects the matching variable itself, FPR is inflated.\nWe propose using total score on \\emph{other} subjects as the matching variable, eliminating this confound.\n\n\\subsection{Comparison Methods}\n\n\\paragraph{ConStat perturbation testing.}\nWe reformulate 220 MMLU items and measure detection rate via paired accuracy drop.\n\n\\paragraph{DVD generation variance.}\nFor 12 models $\\times$ 200 items $\\times$ 50 generations, we detect bimodal response variance as a contamination signal.\n\n\\paragraph{Ensemble fusion.}\nMajority vote and weighted fusion of DIF + ConStat + DVD signals.\n\n%% ============================================================\n%%  4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Experiment 1: Temporal DIF on MMLU}\n\\label{sec:exp1}\n\n\\paragraph{Setup.}\n5{,}227 models $\\times$ 12{,}508 MMLU items from METABENCH.\nReference: models released before 2024; Focal: 2024-H1.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temporal DIF results on MMLU. C\\% = fraction of items classified ETS Category~C. Enrichment measures overlap with Li et al.\\ web-overlap contamination labels. Random-split sanity check confirms non-trivial signal.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nTemporal C\\% & 31.3\\% \\\\\nLi-clean FPR & 0.318 \\\\\nEnrichment (DIF $\\cap$ Li-contaminated) & 0.96 \\\\\nRandom-split sanity C\\% & 0.18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohort comparison. Temporal vs.\\ ability-split DIF and within-family (Llama-2 vs.\\ Llama-3) DIF. Domain-level Spearman $\\rho=0.307$ ($p=0.02$) between C\\% and accuracy improvement.}\n\\label{tab:cohort}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Cohort split} & \\textbf{C\\%} \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024-H1) & 31.3\\% \\\\\nAbility-matched & 2.9\\% \\\\\nWithin-family (Llama-2 vs.\\ Llama-3) & 61.3\\% \\\\\nDomain $\\rho$ (C\\% $\\sim$ accuracy gain) & 0.307 ($p=0.02$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n31.3\\% of items show large DIF between temporal cohorts.\nThe ability-matched split (2.9\\%) shows that the effect is predominantly temporal, not ability-driven.\nWithin-family comparison (Llama-2 vs.\\ Llama-3) reaches 61.3\\%, consistent with rapid within-family capability shifts.\nEnrichment with web-overlap labels is $\\approx$1.0, indicating DIF flags and web-overlap labels capture different phenomena.\nThe random-split sanity check (0.18\\%) confirms the signal is not statistical noise.\n\n\\paragraph{IRT person-fit.}\n98\\% of models show $|L_z|>2$ under a unidimensional IRT model, confirming that MMLU's 57-subject structure violates 1D assumptions.\nThe MH procedure's conditioning on total score is therefore an approximation to multidimensional ability matching.\n\n\\subsection{Experiment 2: Architecture Stratification}\n\\label{sec:arch}\n\nMETABENCH MMLU comprises 5{,}226 decoder-only models and 1 non-decoder model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Architecture stratification. Removing the single non-decoder model produces identical DIF results.}\n\\label{tab:arch}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Population} & \\textbf{C\\%} & \\textbf{Jaccard} & \\textbf{RMSEA} & \\textbf{CFI} \\\\\n\\midrule\nFull ($N=5{,}227$) & 31.3\\% & --- & 0.087 & 0.73 \\\\\nDecoder-only ($N=5{,}226$) & 31.3\\% & 1.00 & 0.087 & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture heterogeneity is a non-issue: Jaccard similarity between full and decoder-only DIF flags is 1.0.\nIRT fit remains poor (RMSEA$=$0.087, CFI$=$0.73, $|L_z|>2$: 97.8\\%), confirming that misfit stems from multidimensionality, not architecture mixing.\n\n\\subsection{Experiment 3: Semi-Synthetic Contamination Validation}\n\\label{sec:semisyn}\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic TPR/FPR across injection rates $p$. Temporal-external matching. Baseline FPR = 0.314 reflects the underlying DIF rate prior to injection.}\n\\label{tab:semisyn}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection rate $p$} & \\textbf{TPR} & \\textbf{$\\Delta$TPR} & \\textbf{FPR} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & --- & 0.314 \\\\\n0.3 & 0.548 & +0.222 & --- \\\\\n0.5 & 0.834 & +0.508 & --- \\\\\n1.0 & 1.000 & +0.674 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Standard vs.\\ cross-subject matching. Cross-subject matching eliminates FPR inflation ($\\Delta$FPR$=$0.000). Standard matching shows inflation from 0.298 to 0.616 at $p=1.0$.}\n\\label{tab:matching}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Matching strategy} & \\textbf{$\\Delta$FPR at $p=1.0$} \\\\\n\\midrule\nStandard (all subjects) & $0.298 \\to 0.616$ (+0.318) \\\\\nCross-subject (other subjects) & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Delta$TPR shows a clear dose-response: detection power increases monotonically with injection rate.\nAt $p=0.5$, $\\Delta$TPR$=+$0.508, confirming DIF can detect differential contamination above baseline.\nCross-subject matching ($\\Delta$FPR$=$0.000) is a key methodological contribution, eliminating the matching-variable contamination artifact.\n\n\\paragraph{Ability-split results.}\nUnder ability-based matching, TPR at $p=1.0$ is 0.80, but FPR rises to 0.493---confirming that ability-based cohorts confound the matching variable more severely.\n\n\\subsection{Experiment 4: Cross-Benchmark Replication (GSM8K)}\n\\label{sec:gsm8k}\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K DIF analysis (1{,}319 items, $N_{\\mathrm{ref}}=1{,}017$, $N_{\\mathrm{foc}}=804$) and GSM1K contamination gap correlation ($N=33$ models).}\n\\label{tab:gsm8k}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nGSM8K standard temporal C\\% & 18.9\\% \\\\\nGSM8K external C\\% & 47.4\\% \\\\\nGSM8K sanity C\\% & 0.3\\% \\\\\nSemi-synthetic $\\Delta$TPR ($p=1.0$) & 0.818 \\\\\n\\midrule\nGSM1K Pearson $r$ & $-0.478$ ($p=0.005$) \\\\\nGSM1K Spearman $\\rho$ & $-0.403$ ($p=0.020$) \\\\\nGSM1K BCa CI (Pearson) & $[-0.714, -0.155]$ \\\\\nGSM1K partial $r$ (controlling accuracy) & $-0.385$ ($p=0.030$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K replication confirms framework portability.\nSemi-synthetic $\\Delta$TPR$=+$0.818 on a unidimensional math benchmark demonstrates strong detection power when IRT assumptions are better satisfied.\nGSM1K contamination gap correlates negatively with DIF flags ($r=-0.478$, $p=0.005$): models with larger contamination gaps show lower performance on DIF-flagged items.\nThis is consistent with DIF items capturing genuine capability rather than memorization-based gains.\n\n\\paragraph{Caveats.}\n$N=33$ models limits statistical power; BCa CI upper bound $|r|=0.155$ admits a small true effect.\nGSM8K is single-domain (math), so generalization to MMLU's 57-subject multidimensionality is not direct.\n\n\\subsection{Experiment 5: RL Model Robustness}\n\\label{sec:rl}\n\n\\begin{table}[h]\n\\centering\n\\caption{AUROC comparison across detection methods on reasoning-RL models ($N=13$ GRPO/PPO models within a $N=477$ alignment-RL cohort). Bootstrap 95\\% CI in brackets.}\n\\label{tab:rl_auroc}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{95\\% CI} \\\\\n\\midrule\nDIF & 0.58 & $[0.41, 0.73]$ \\\\\nConStat & 0.54 & --- \\\\\nMin-K\\% & 0.51 & --- \\\\\n\\midrule\nDeLong $p$ (DIF vs.\\ ConStat) & 0.38 & \\\\\nTOST equivalence $p$ & 0.22 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF C\\% by cohort type and power analysis at varying injection rates.}\n\\label{tab:rl_power}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Cohort} & \\textbf{C\\%} \\\\\n\\midrule\nSFT baseline & 30.2\\% \\\\\nAlignment-RL ($N=477$) & 31.9\\% \\\\\nGRPO-specific ($N=13$) & 34.8\\% \\\\\nJaccard (SFT vs.\\ GRPO) & 0.71 \\\\\n\\midrule\n\\textbf{Injection rate $p$} & \\textbf{Power (TPR)} \\\\\n\\midrule\n0.4 & 0.12 \\\\\n0.7 & 0.43 \\\\\n1.0 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith only 13 reasoning-RL models, this analysis is exploratory.\nC\\% is comparable across SFT (30.2\\%), alignment-RL (31.9\\%), and GRPO-specific (34.8\\%) cohorts, and item-level overlap is high (Jaccard$=$0.71).\nNo method achieves significant AUROC advantage (DeLong $p=0.38$); all CIs overlap chance.\nPower is limited: at $p=0.4$, TPR$=$0.12.\nDIF is a group-level method and cannot provide per-model detection---a structural limitation acknowledged but not resolved.\n\n\\subsection{Experiment 6: ConStat Perturbation Evaluation}\n\\label{sec:constat}\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat vs.\\ DIF detection comparison on 220 reformulated MMLU items.}\n\\label{tab:constat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{ConStat} & \\textbf{DIF} \\\\\n\\midrule\nDetection rate (non-RL) & 0.41 & --- \\\\\nDetection rate (RL) & 0.08 & --- \\\\\nFDR-controlled rate & 0.23 & --- \\\\\nFPR & 0.067 & 0.318 \\\\\nUnique detections & 158 & 892 \\\\\nOverlap (\\%) & \\multicolumn{2}{c}{12.7\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat achieves controlled FPR (0.067) by design via FDR correction, substantially lower than DIF's 0.318 on Li-clean items.\nDetection overlap is only 12.7\\%, suggesting the methods capture different phenomena: ConStat detects perturbation sensitivity (per-model), while DIF detects group-level item functioning changes.\nConStat degrades sharply on RL models (0.08 vs.\\ 0.41 on non-RL), consistent with RL training producing more robust response patterns.\n\n\\subsection{Experiment 7: DVD Generation Variance Evaluation}\n\\label{sec:dvd}\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection rates across 12 models $\\times$ 200 items $\\times$ 50 generations per item.}\n\\label{tab:dvd}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nBimodal detection rate & 0.14 \\\\\nVariance-based detection rate & 0.22 \\\\\nDVD vs.\\ DIF overlap & 0.09 \\\\\nDVD FPR & 0.04 \\\\\nGPU hours & 65 \\\\\nVariant contamination detected & 31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves very low FPR (0.04) but limited detection rate (bimodal: 14\\%, variance: 22\\%).\nOverlap with DIF is only 9\\%, again confirming orthogonality.\nThe method requires 120K inference generations (65 GPU hours), limiting scalability.\nDVD may be better positioned as a follow-up diagnostic on flagged items rather than a primary detector.\n\n\\subsection{Experiment 8: Ensemble Fusion}\n\\label{sec:ensemble}\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble configurations combining DIF, ConStat, and DVD signals.}\n\\label{tab:ensemble_config}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\nMajority vote & 0.38 & 0.09 \\\\\nWeighted fusion & 0.44 & 0.15 \\\\\nEnsemble FPR & \\multicolumn{2}{c}{0.087} \\\\\n$\\Delta F_1$ (optimized $-$ uniform) & \\multicolumn{2}{c}{0.02} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-validation fold weights for weighted fusion. High variance (std/mean $>$ 0.6) indicates instability.}\n\\label{tab:ensemble_weights}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Signal} & \\textbf{Weight (mean)} \\\\\n\\midrule\nDIF & 0.28 \\\\\nConStat & 0.51 \\\\\nDVD & 0.21 \\\\\n\\midrule\nWeight stability & std/mean $>$ 0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble results are a negative finding.\nMajority vote achieves only 9\\% recall; weighted fusion reaches 15\\%.\nThe marginal benefit of optimization over uniform weights ($\\Delta F_1 = 0.02$) is negligible.\nCross-validation weights are unstable (std/mean $>$ 0.6), and DIF receives the lowest weight (0.28) among the three signals.\nLow pairwise overlaps ($<$15\\%) between methods predict this failure: combining orthogonal weak signals does not produce a coherent detector.\nWe report this as an informative null result.\n\n\\subsection{Experiment 9: Bifactor IRT Equating Pilot}\n\\label{sec:bifactor}\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor IRT model fit indices. All indices below acceptable thresholds. Model did not converge.}\n\\label{tab:bifactor}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Index} & \\textbf{Value} & \\textbf{Threshold} \\\\\n\\midrule\nConvergence & No & --- \\\\\nRMSEA & 0.089 & $<0.06$ \\\\\nCFI & 0.71 & $>0.90$ \\\\\nTLI & 0.68 & $>0.90$ \\\\\nSRMR & 0.112 & $<0.08$ \\\\\nHeywood cases & 47 & 0 \\\\\nAnchor items identified & 0 & $>0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor IRT model (general factor + 57 subject-specific factors) fails to converge on the full matrix, with 47 Heywood cases (negative variance estimates).\nAll fit indices are far below acceptable thresholds.\nNo anchor items could be identified, terminating the IRT equating pipeline.\nThis negative result confirms that MMLU's item--model structure does not support confirmatory bifactor modeling at scale, consistent with the 98\\% person-misfit finding.\n\n\\subsection{Experiment 10: Item Generation and Calibration}\n\\label{sec:itemgen}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLM-generated replacement item calibration. Difficulty correlation targets the 0.75 benchmark from the educational testing literature.}\n\\label{tab:itemgen}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Target} \\\\\n\\midrule\n$N$ items generated & 500 & --- \\\\\nDifficulty $\\rho$ (prompt-based) & 0.18 & 0.75 \\\\\nDifficulty $\\rho$ (student-sim) & 0.52 & 0.75 \\\\\nConstruct alignment (human) & 0.64 & $>0.80$ \\\\\nHoldout panel $\\rho$ & 0.41 & $>0.70$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem generation falls below all calibration benchmarks.\nPrompt-based difficulty targeting ($\\rho=0.18$) is near the bottom of the literature range (0.10--0.45).\nStudent-simulation calibration ($\\rho=0.52$) approaches but does not meet the 0.75 target.\nHuman-evaluated construct alignment (0.64) indicates 36\\% of generated items fall outside the intended cognitive level or subject boundary.\nHoldout model panel correlation (0.41) is insufficient to guarantee score equivalence.\nThe benchmark regeneration pipeline is not ready for deployment.\n\n\\subsection{Experiment 11: Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power over successive administrations (simulation, $\\delta=1.0$). Target power: 0.70.}\n\\label{tab:bayesian}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Administrations} & \\textbf{Power} \\\\\n\\midrule\n1 & 0.38 \\\\\n2 & 0.49 \\\\\n3 & 0.58 \\\\\n4 & 0.64 \\\\\n\\midrule\nTarget & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSimulation shows monotonic power accumulation across successive administrations, but the target of 0.70 is not reached after 4 administrations at $\\delta=1.0$.\nThis is a simulation-only result with no real-data validation.\nThe stationarity assumption (benchmark items remain fixed across administrations) may be violated in the LLM setting where benchmarks themselves are subject to contamination over time.\n\n\\subsection{Experiment 12: Graceful Degradation Analysis}\n\\label{sec:degradation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Benchmark validity metrics under progressive item replacement. $\\rho$ = Spearman rank correlation of model rankings with original benchmark. $\\alpha$ = Cronbach's reliability.}\n\\label{tab:degradation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Replacement \\%} & $\\rho$ & $\\alpha$ & \\textbf{Coverage gap} \\\\\n\\midrule\n0\\% & 1.000 & 0.94 & --- \\\\\n5\\% & 0.994 & --- & --- \\\\\n10\\% & 0.986 & --- & --- \\\\\n20\\% & 0.961 & 0.88 & 3 subjects $>$30\\% loss \\\\\n50\\% & 0.873 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRanking correlation degrades faster than expected under item replacement.\nAt 20\\% replacement, $\\rho=0.961$ and reliability drops from 0.94 to 0.88.\nCritically, simple item \\emph{removal} (as in the diagnostic analysis of \\S\\ref{sec:exp1}) achieves $\\rho\\approx 0.997$---better than replacement---because the generated replacement items (\\S\\ref{sec:itemgen}) add noise rather than preserving measurement properties.\nThree subjects lose $>$30\\% of their items at 20\\% replacement, creating uneven construct coverage.\nTheoretical bounds are not tight enough to provide actionable replacement thresholds.\n\n\\subsection{Experiment 13: Item-Focused Trees}\n\\label{sec:ift}\n\n\\begin{table}[h]\n\\centering\n\\caption{MH vs.\\ Item-Focused Trees (IFT) flag comparison. IFT uses continuous temporal covariates rather than binary cohort splits.}\n\\label{tab:ift}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Items flagged} & \\textbf{Unique flags} \\\\\n\\midrule\nMH-DIF & 3{,}918 (31.3\\%) & 1{,}650 \\\\\nIFT & 4{,}102 (32.8\\%) & 1{,}834 \\\\\n\\midrule\nJaccard overlap & \\multicolumn{2}{c}{0.48} \\\\\nFirst split variable & \\multicolumn{2}{c}{release\\_date} \\\\\nInteraction with model size & \\multicolumn{2}{c}{$p<0.01$} \\\\\nTemporal granularity & \\multicolumn{2}{c}{quarterly splits} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees flag a comparable number of items (32.8\\%) but with only 48\\% overlap with MH, indicating substantial method disagreement.\nIFT's continuous temporal treatment reveals quarterly granularity and a significant interaction with model size ($p<0.01$), suggesting that larger models (released later) contribute disproportionately to DIF.\nThe 52\\% disagreement between methods raises questions about whether either method is detecting a robust item-level phenomenon or whether different modeling choices produce different artifact patterns.\n\n%% ============================================================\n%%  5  DISCUSSION AND LIMITATIONS\n%% ============================================================\n\\section{Discussion and Limitations}\n\n\\paragraph{Summary of findings.}\nWe characterize MMLU's temporal measurement properties using MH-DIF at unprecedented scale.\n31.3\\% of items show large DIF between model generations, robust to multiple analytical variations.\nThe semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000) provides a reusable evaluation infrastructure.\nDespite instability, MMLU rankings are resilient ($\\rho\\approx 0.997$), and DIF serves as a diagnostic lens for understanding inter-generational capability shifts.\n\n\\paragraph{IRT misspecification.}\nThe most significant limitation is the fundamental misspecification of unidimensional IRT for MMLU.\nWith 98\\% of models showing $|L_z|>2$, the total score used for MH ability matching is a collapsed composite of 57-subject abilities.\nTwo models with identical total scores may have very different subject-level ability profiles, creating systematic ability confounding that inflates DIF detection rates.\nThe 31.3\\% C\\% figure must be interpreted in this context: it represents items flagged under 1D matching, and an unknown fraction may be spurious DIF driven by multidimensional ability differences rather than genuine item-level changes.\n\n\\paragraph{Bifactor failure.}\nOur attempt to address misspecification via bifactor IRT modeling (\\S\\ref{sec:bifactor}) failed entirely (non-convergence, 47 Heywood cases).\nThis does not prove IRT is inapplicable to MMLU---exploratory MIRT or mixture IRT approaches may succeed---but it does confirm that confirmatory bifactor models are not viable at this scale.\n\n\\paragraph{Enrichment $\\approx$ 1.0.}\nDIF flags show no enrichment with web-overlap contamination labels.\nWe argue this is expected because web-overlap measures global exposure, not differential contamination.\nAn alternative interpretation is that DIF simply does not detect contamination.\nThe semi-synthetic results show DIF \\emph{can} detect injected differential contamination, but the gap between semi-synthetic injection (binary flipping) and real-world contamination mechanisms remains.\n\n\\paragraph{FPR.}\nDIF's FPR on Li-clean items is 0.318---nearly 1 in 3 clean items are flagged.\nCross-subject matching eliminates \\emph{inflation} but not the baseline rate.\nWithout ground truth for item-level differential contamination, we cannot determine what fraction of the 31.3\\% represents genuine item functioning changes vs.\\ multidimensional confounding.\n\n\\paragraph{GSM1K limitations.}\nThe GSM1K correlation ($r=-0.478$, $N=33$) is suggestive but limited by sample size (BCa CI upper bound $|r|=0.155$) and potential difficulty confounding.\n\n\\paragraph{Comparison method scope.}\nConStat evaluation covers only 220 reformulated items; DVD covers 200 items $\\times$ 12 models.\nEnsemble fusion produces a null result.\nFull-scale comparison would require substantially more resources.\n\n\\paragraph{Novelty.}\nMH-DIF is a textbook method from 1988.\nWe apply it without modification to a new domain.\nOur contributions are the empirical findings, the validation framework, and the ground-truth meta-critique---not algorithmic innovation.\n\n\\paragraph{Future directions.}\nThree paths forward: (1) multidimensional IRT or MIMIC models that properly account for MMLU's 57-subject structure, (2) larger-scale cross-benchmark validation with more matched models, and (3) integration with perturbation-based methods for a multi-signal diagnostic framework.\n\n%% ============================================================\n%%  6  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe apply Mantel--Haenszel DIF analysis to 5{,}227 models $\\times$ 12{,}508 MMLU items, finding 31.3\\% temporal item instability.\nThis finding is robust to threshold choice, multiple testing correction, and architecture composition, and is not explained by domain-level capability improvement ($\\le$7.6\\%).\nWe demonstrate that web-overlap contamination labels cannot validate item-level differential detectors and propose a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000).\nDespite 31\\% instability, MMLU rankings are massively redundant ($\\rho\\approx 0.997$), and DIF items serve as a diagnostic lens for inter-generational capability shifts rather than a quality filter.\n\nThe primary caveat is IRT misspecification: 98\\% of models show poor person-fit under unidimensional IRT, and the true rate of genuine item-level instability may be lower than 31.3\\%.\nResolving this requires multidimensional IRT methods that we have not yet successfully applied to MMLU-scale data.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021measuring}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item functioning and the {M}antel--{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, Y.~Wang, and others.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mantel \\& Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Polo et~al.(2024)]{constat2024}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Irt-llm(2024)]{irt_llm2024}\nIRT for LLM Evaluation.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3abb2a15-9605-4d10-95d5-e1c240542994",
  "isSidechain": false,
  "requestId": "req_011CbFGXYmpqHVuyYvBB7xi3",
  "type": "assistant",
  "uuid": "29734c7a-8094-46fa-af86-48eed0a9f6e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3CA1iZMz83moroBuMCafN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 756,
      "cache_read_input_tokens": 40071,
      "output_tokens": 10424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 756,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10424,
          "cache_read_input_tokens": 40071,
          "cache_creation_input_tokens": 756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 756
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

_source line 19 · 2026-05-21T06:52:40.921Z_

<details><summary>↩ Tool result · `toolu_01NkUmr3pzjsXHFTDiXMp1yK`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29734c7a-8094-46fa-af86-48eed0a9f6e8",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "58c2e60f-07ef-4272-9f9e-a83eb85d0c16",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst/paper.tex",
    "content": "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{graphicx}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{geometry}\n\\geometry{margin=1in}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\n\\title{Psychometric DIF Analysis Reveals 31\\% Temporal Item Instability\\\\in MMLU: A Large-Scale Characterization of Benchmark Measurement Properties}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n%% ============================================================\n%%  ABSTRACT\n%% ============================================================\n\\begin{abstract}\nWhen we compare language model scores across time, we implicitly assume that benchmark items function identically for all model cohorts.\nWe test this assumption by applying Mantel--Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5{,}227 models $\\times$ 12{,}508 MMLU items)---the largest-scale DIF analysis on LLM benchmarks to date.\nWe find that 31.3\\% of items exhibit large DIF (ETS Category~C, $|\\Delta_{\\mathrm{MH}}|\\!\\ge\\!1.5$) between 2023 and 2024-H1 model cohorts, robust across thresholds (10--49\\% at $|\\Delta|\\in[1.0,2.5]$), not explained by domain-level capability improvement ($\\le$7.6\\%), and architecturally homogeneous (99.98\\% decoder-only).\nWe show that the field's standard web-overlap contamination labels cannot validate item-level differential detectors (enrichment$\\approx$1.0) and propose a semi-synthetic validation framework with cross-subject matching that eliminates false-positive inflation ($\\Delta$FPR$=$0.000).\nDespite 31\\% instability, MMLU model rankings are massively redundant ($\\rho\\!\\approx\\!0.997$), and DIF items serve as a diagnostic lens---identifying \\emph{which} capability dimensions shift across generations rather than flagging ``bad'' items.\nCross-benchmark replication on GSM8K (1{,}319 items $\\times$ 6{,}702 models) confirms framework portability ($\\Delta$TPR$=+$0.818) and shows DIF items resist contamination-based gains ($r\\!=\\!-0.478$, $p\\!=\\!0.005$).\n\\end{abstract}\n\n%% ============================================================\n%%  1  INTRODUCTION\n%% ============================================================\n\\section{Introduction}\n\nBenchmarks such as MMLU~\\citep{hendrycks2021measuring} are the primary yardstick for comparing language models.\nTemporal comparisons---``GPT-4 surpasses GPT-3.5 on MMLU''---rest on an untested assumption: that every item measures the same construct with the same difficulty for every model cohort.\nPsychometrics has a mature tool for evaluating exactly this assumption: \\emph{Differential Item Functioning} (DIF) analysis, which detects items whose difficulty changes across groups after controlling for overall ability~\\citep{holland1988differential}.\n\nWe apply the Mantel--Haenszel (MH) DIF procedure---unchanged since 1988---to the METABENCH response matrix comprising 5{,}227 models and 12{,}508 MMLU items.\nWe do \\emph{not} claim algorithmic novelty; MH-DIF is a textbook method.\nOur contributions are empirical:\n\n\\begin{enumerate}\n    \\item \\textbf{Temporal instability at scale.}\n    31.3\\% of MMLU items are ETS Category~C between 2023 and 2024-H1 cohorts.\n    This is not a statistical artifact (random-split sanity: 0.18\\%), not driven by capability improvement ($\\le$7.6\\%), and robust to threshold choice.\n    \\item \\textbf{Ground-truth meta-critique.}\n    Web-overlap contamination labels (e.g., Li et al.) measure global exposure, not differential contamination.\n    Enrichment$\\approx$1.0 is the expected outcome, not method failure.\n    \\item \\textbf{Semi-synthetic validation framework.}\n    $\\Delta$TPR methodology with cross-subject matching ($\\Delta$FPR$=$0.000).\n    Portable to GSM8K ($\\Delta$TPR$=+$0.818).\n    \\item \\textbf{DIF as diagnostic lens.}\n    Despite 31\\% instability, rankings are stable ($\\rho\\!\\approx\\!0.997$).\n    DIF items are the \\emph{least} disruptive non-random removal strategy ($z\\!=\\!-9.5$ vs.\\ accuracy-gap $z\\!=\\!-157$), isolating genuine differential functioning.\n\\end{enumerate}\n\n\\paragraph{Key framing.}\nInstability $\\neq$ invalidity.\nDIF flags items whose measurement properties changed---a diagnostic signal, not a quality verdict.\nMMLU rankings survive 31\\% item removal because the benchmark is massively redundant.\nDIF tells us \\emph{what changed}, not ``what is broken.''\n\n%% ============================================================\n%%  2  RELATED WORK\n%% ============================================================\n\\section{Related Work}\n\n\\paragraph{LLM benchmark contamination.}\nWeb-overlap and $n$-gram methods~\\citep{li2024task} identify publicly available items but do not assess \\emph{differential} item functioning.\nConStat~\\citep{constat2024} uses perturbation testing; Min-K\\%~\\citep{shi2024detecting} uses token-level statistics.\nBoth operate per-model, unlike DIF which is a group-level method.\n\n\\paragraph{Differential Item Functioning.}\nThe MH procedure~\\citep{mantel1959statistical,holland1988differential} tests whether item difficulty differs between focal and reference groups after conditioning on total score.\nETS classifies items as A ($|\\Delta_{\\mathrm{MH}}|<1.0$), B ($1.0$--$1.5$), or C ($\\ge\\!1.5$).\nDIF analysis has been standard in educational testing for decades.\n\n\\paragraph{IRT and LLM evaluation.}\nItem Response Theory has been applied to LLM evaluation~\\citep{irt_llm2024}, though IRT model fit for multidimensional benchmarks remains challenging.\n\n%% ============================================================\n%%  3  METHOD\n%% ============================================================\n\\section{Method}\n\n\\subsection{Mantel--Haenszel DIF}\n\nGiven a binary response matrix $\\mathbf{X}\\in\\{0,1\\}^{N\\times J}$ ($N$ models, $J$ items), we partition models into a \\emph{reference} group (2023 cohort) and a \\emph{focal} group (2024-H1 cohort).\nFor each item $j$ and total-score stratum $k$, the MH statistic tests the null hypothesis that the item--group odds ratio is 1.\nThe effect size $\\Delta_{\\mathrm{MH}}$ (in ETS delta units) quantifies the magnitude.\nItems with $|\\Delta_{\\mathrm{MH}}|\\ge 1.5$ and statistically significant MH $\\chi^2$ are classified as ETS Category~C.\n\n\\paragraph{IRT fit caveat.}\nMH conditions on total score as an ability proxy.\nOn MMLU (57 subjects), the unidimensional IRT model is misspecified: 98\\% of models show person-fit $|L_z|>2$.\nTotal score collapses a multidimensional ability space into a single composite.\nThis is a known limitation throughout the paper.\n\n\\subsection{Semi-Synthetic Validation Framework}\n\nTo evaluate DIF detection power with known ground truth, we inject controlled contamination into the real METABENCH response matrix:\n\\begin{enumerate}\n    \\item Select $n_{\\mathrm{clean}}$ items with no DIF signal as ``clean'' items.\n    \\item For each ``injected'' item, flip a fraction $p$ of focal-group incorrect responses to correct, simulating differential contamination.\n    \\item Run MH-DIF on the modified matrix and measure $\\Delta\\text{TPR} = \\text{TPR}_{\\text{injected}} - \\text{TPR}_{\\text{baseline}}$.\n\\end{enumerate}\n\n\\paragraph{Cross-subject matching.}\nStandard MH uses total score (all subjects) as matching variable.\nWhen contamination affects the matching variable itself, FPR is inflated.\nWe propose using total score on \\emph{other} subjects as the matching variable, eliminating this confound.\n\n\\subsection{Comparison Methods}\n\n\\paragraph{ConStat perturbation testing.}\nWe reformulate 220 MMLU items and measure detection rate via paired accuracy drop.\n\n\\paragraph{DVD generation variance.}\nFor 12 models $\\times$ 200 items $\\times$ 50 generations, we detect bimodal response variance as a contamination signal.\n\n\\paragraph{Ensemble fusion.}\nMajority vote and weighted fusion of DIF + ConStat + DVD signals.\n\n%% ============================================================\n%%  4  EXPERIMENTS\n%% ============================================================\n\\section{Experiments}\n\n\\subsection{Experiment 1: Temporal DIF on MMLU}\n\\label{sec:exp1}\n\n\\paragraph{Setup.}\n5{,}227 models $\\times$ 12{,}508 MMLU items from METABENCH.\nReference: models released before 2024; Focal: 2024-H1.\n\n\\begin{table}[h]\n\\centering\n\\caption{Temporal DIF results on MMLU. C\\% = fraction of items classified ETS Category~C. Enrichment measures overlap with Li et al.\\ web-overlap contamination labels. Random-split sanity check confirms non-trivial signal.}\n\\label{tab:temporal_dif}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nTemporal C\\% & 31.3\\% \\\\\nLi-clean FPR & 0.318 \\\\\nEnrichment (DIF $\\cap$ Li-contaminated) & 0.96 \\\\\nRandom-split sanity C\\% & 0.18\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cohort comparison. Temporal vs.\\ ability-split DIF and within-family (Llama-2 vs.\\ Llama-3) DIF. Domain-level Spearman $\\rho=0.307$ ($p=0.02$) between C\\% and accuracy improvement.}\n\\label{tab:cohort}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Cohort split} & \\textbf{C\\%} \\\\\n\\midrule\nTemporal (2023 vs.\\ 2024-H1) & 31.3\\% \\\\\nAbility-matched & 2.9\\% \\\\\nWithin-family (Llama-2 vs.\\ Llama-3) & 61.3\\% \\\\\nDomain $\\rho$ (C\\% $\\sim$ accuracy gain) & 0.307 ($p=0.02$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n31.3\\% of items show large DIF between temporal cohorts.\nThe ability-matched split (2.9\\%) shows that the effect is predominantly temporal, not ability-driven.\nWithin-family comparison (Llama-2 vs.\\ Llama-3) reaches 61.3\\%, consistent with rapid within-family capability shifts.\nEnrichment with web-overlap labels is $\\approx$1.0, indicating DIF flags and web-overlap labels capture different phenomena.\nThe random-split sanity check (0.18\\%) confirms the signal is not statistical noise.\n\n\\paragraph{IRT person-fit.}\n98\\% of models show $|L_z|>2$ under a unidimensional IRT model, confirming that MMLU's 57-subject structure violates 1D assumptions.\nThe MH procedure's conditioning on total score is therefore an approximation to multidimensional ability matching.\n\n\\subsection{Experiment 2: Architecture Stratification}\n\\label{sec:arch}\n\nMETABENCH MMLU comprises 5{,}226 decoder-only models and 1 non-decoder model.\n\n\\begin{table}[h]\n\\centering\n\\caption{Architecture stratification. Removing the single non-decoder model produces identical DIF results.}\n\\label{tab:arch}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Population} & \\textbf{C\\%} & \\textbf{Jaccard} & \\textbf{RMSEA} & \\textbf{CFI} \\\\\n\\midrule\nFull ($N=5{,}227$) & 31.3\\% & --- & 0.087 & 0.73 \\\\\nDecoder-only ($N=5{,}226$) & 31.3\\% & 1.00 & 0.087 & 0.73 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nArchitecture heterogeneity is a non-issue: Jaccard similarity between full and decoder-only DIF flags is 1.0.\nIRT fit remains poor (RMSEA$=$0.087, CFI$=$0.73, $|L_z|>2$: 97.8\\%), confirming that misfit stems from multidimensionality, not architecture mixing.\n\n\\subsection{Experiment 3: Semi-Synthetic Contamination Validation}\n\\label{sec:semisyn}\n\n\\begin{table}[h]\n\\centering\n\\caption{Semi-synthetic TPR/FPR across injection rates $p$. Temporal-external matching. Baseline FPR = 0.314 reflects the underlying DIF rate prior to injection.}\n\\label{tab:semisyn}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Injection rate $p$} & \\textbf{TPR} & \\textbf{$\\Delta$TPR} & \\textbf{FPR} \\\\\n\\midrule\n0.0 (baseline) & 0.326 & --- & 0.314 \\\\\n0.3 & 0.548 & +0.222 & --- \\\\\n0.5 & 0.834 & +0.508 & --- \\\\\n1.0 & 1.000 & +0.674 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Standard vs.\\ cross-subject matching. Cross-subject matching eliminates FPR inflation ($\\Delta$FPR$=$0.000). Standard matching shows inflation from 0.298 to 0.616 at $p=1.0$.}\n\\label{tab:matching}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Matching strategy} & \\textbf{$\\Delta$FPR at $p=1.0$} \\\\\n\\midrule\nStandard (all subjects) & $0.298 \\to 0.616$ (+0.318) \\\\\nCross-subject (other subjects) & 0.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Delta$TPR shows a clear dose-response: detection power increases monotonically with injection rate.\nAt $p=0.5$, $\\Delta$TPR$=+$0.508, confirming DIF can detect differential contamination above baseline.\nCross-subject matching ($\\Delta$FPR$=$0.000) is a key methodological contribution, eliminating the matching-variable contamination artifact.\n\n\\paragraph{Ability-split results.}\nUnder ability-based matching, TPR at $p=1.0$ is 0.80, but FPR rises to 0.493---confirming that ability-based cohorts confound the matching variable more severely.\n\n\\subsection{Experiment 4: Cross-Benchmark Replication (GSM8K)}\n\\label{sec:gsm8k}\n\n\\begin{table}[h]\n\\centering\n\\caption{GSM8K DIF analysis (1{,}319 items, $N_{\\mathrm{ref}}=1{,}017$, $N_{\\mathrm{foc}}=804$) and GSM1K contamination gap correlation ($N=33$ models).}\n\\label{tab:gsm8k}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nGSM8K standard temporal C\\% & 18.9\\% \\\\\nGSM8K external C\\% & 47.4\\% \\\\\nGSM8K sanity C\\% & 0.3\\% \\\\\nSemi-synthetic $\\Delta$TPR ($p=1.0$) & 0.818 \\\\\n\\midrule\nGSM1K Pearson $r$ & $-0.478$ ($p=0.005$) \\\\\nGSM1K Spearman $\\rho$ & $-0.403$ ($p=0.020$) \\\\\nGSM1K BCa CI (Pearson) & $[-0.714, -0.155]$ \\\\\nGSM1K partial $r$ (controlling accuracy) & $-0.385$ ($p=0.030$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGSM8K replication confirms framework portability.\nSemi-synthetic $\\Delta$TPR$=+$0.818 on a unidimensional math benchmark demonstrates strong detection power when IRT assumptions are better satisfied.\nGSM1K contamination gap correlates negatively with DIF flags ($r=-0.478$, $p=0.005$): models with larger contamination gaps show lower performance on DIF-flagged items.\nThis is consistent with DIF items capturing genuine capability rather than memorization-based gains.\n\n\\paragraph{Caveats.}\n$N=33$ models limits statistical power; BCa CI upper bound $|r|=0.155$ admits a small true effect.\nGSM8K is single-domain (math), so generalization to MMLU's 57-subject multidimensionality is not direct.\n\n\\subsection{Experiment 5: RL Model Robustness}\n\\label{sec:rl}\n\n\\begin{table}[h]\n\\centering\n\\caption{AUROC comparison across detection methods on reasoning-RL models ($N=13$ GRPO/PPO models within a $N=477$ alignment-RL cohort). Bootstrap 95\\% CI in brackets.}\n\\label{tab:rl_auroc}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{AUROC} & \\textbf{95\\% CI} \\\\\n\\midrule\nDIF & 0.58 & $[0.41, 0.73]$ \\\\\nConStat & 0.54 & --- \\\\\nMin-K\\% & 0.51 & --- \\\\\n\\midrule\nDeLong $p$ (DIF vs.\\ ConStat) & 0.38 & \\\\\nTOST equivalence $p$ & 0.22 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{DIF C\\% by cohort type and power analysis at varying injection rates.}\n\\label{tab:rl_power}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Cohort} & \\textbf{C\\%} \\\\\n\\midrule\nSFT baseline & 30.2\\% \\\\\nAlignment-RL ($N=477$) & 31.9\\% \\\\\nGRPO-specific ($N=13$) & 34.8\\% \\\\\nJaccard (SFT vs.\\ GRPO) & 0.71 \\\\\n\\midrule\n\\textbf{Injection rate $p$} & \\textbf{Power (TPR)} \\\\\n\\midrule\n0.4 & 0.12 \\\\\n0.7 & 0.43 \\\\\n1.0 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith only 13 reasoning-RL models, this analysis is exploratory.\nC\\% is comparable across SFT (30.2\\%), alignment-RL (31.9\\%), and GRPO-specific (34.8\\%) cohorts, and item-level overlap is high (Jaccard$=$0.71).\nNo method achieves significant AUROC advantage (DeLong $p=0.38$); all CIs overlap chance.\nPower is limited: at $p=0.4$, TPR$=$0.12.\nDIF is a group-level method and cannot provide per-model detection---a structural limitation acknowledged but not resolved.\n\n\\subsection{Experiment 6: ConStat Perturbation Evaluation}\n\\label{sec:constat}\n\n\\begin{table}[h]\n\\centering\n\\caption{ConStat vs.\\ DIF detection comparison on 220 reformulated MMLU items.}\n\\label{tab:constat}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{ConStat} & \\textbf{DIF} \\\\\n\\midrule\nDetection rate (non-RL) & 0.41 & --- \\\\\nDetection rate (RL) & 0.08 & --- \\\\\nFDR-controlled rate & 0.23 & --- \\\\\nFPR & 0.067 & 0.318 \\\\\nUnique detections & 158 & 892 \\\\\nOverlap (\\%) & \\multicolumn{2}{c}{12.7\\%} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nConStat achieves controlled FPR (0.067) by design via FDR correction, substantially lower than DIF's 0.318 on Li-clean items.\nDetection overlap is only 12.7\\%, suggesting the methods capture different phenomena: ConStat detects perturbation sensitivity (per-model), while DIF detects group-level item functioning changes.\nConStat degrades sharply on RL models (0.08 vs.\\ 0.41 on non-RL), consistent with RL training producing more robust response patterns.\n\n\\subsection{Experiment 7: DVD Generation Variance Evaluation}\n\\label{sec:dvd}\n\n\\begin{table}[h]\n\\centering\n\\caption{DVD detection rates across 12 models $\\times$ 200 items $\\times$ 50 generations per item.}\n\\label{tab:dvd}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nBimodal detection rate & 0.14 \\\\\nVariance-based detection rate & 0.22 \\\\\nDVD vs.\\ DIF overlap & 0.09 \\\\\nDVD FPR & 0.04 \\\\\nGPU hours & 65 \\\\\nVariant contamination detected & 31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDVD achieves very low FPR (0.04) but limited detection rate (bimodal: 14\\%, variance: 22\\%).\nOverlap with DIF is only 9\\%, again confirming orthogonality.\nThe method requires 120K inference generations (65 GPU hours), limiting scalability.\nDVD may be better positioned as a follow-up diagnostic on flagged items rather than a primary detector.\n\n\\subsection{Experiment 8: Ensemble Fusion}\n\\label{sec:ensemble}\n\n\\begin{table}[h]\n\\centering\n\\caption{Ensemble configurations combining DIF, ConStat, and DVD signals.}\n\\label{tab:ensemble_config}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{Precision} & \\textbf{Recall} \\\\\n\\midrule\nMajority vote & 0.38 & 0.09 \\\\\nWeighted fusion & 0.44 & 0.15 \\\\\nEnsemble FPR & \\multicolumn{2}{c}{0.087} \\\\\n$\\Delta F_1$ (optimized $-$ uniform) & \\multicolumn{2}{c}{0.02} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-validation fold weights for weighted fusion. High variance (std/mean $>$ 0.6) indicates instability.}\n\\label{tab:ensemble_weights}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Signal} & \\textbf{Weight (mean)} \\\\\n\\midrule\nDIF & 0.28 \\\\\nConStat & 0.51 \\\\\nDVD & 0.21 \\\\\n\\midrule\nWeight stability & std/mean $>$ 0.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nEnsemble results are a negative finding.\nMajority vote achieves only 9\\% recall; weighted fusion reaches 15\\%.\nThe marginal benefit of optimization over uniform weights ($\\Delta F_1 = 0.02$) is negligible.\nCross-validation weights are unstable (std/mean $>$ 0.6), and DIF receives the lowest weight (0.28) among the three signals.\nLow pairwise overlaps ($<$15\\%) between methods predict this failure: combining orthogonal weak signals does not produce a coherent detector.\nWe report this as an informative null result.\n\n\\subsection{Experiment 9: Bifactor IRT Equating Pilot}\n\\label{sec:bifactor}\n\n\\begin{table}[h]\n\\centering\n\\caption{Bifactor IRT model fit indices. All indices below acceptable thresholds. Model did not converge.}\n\\label{tab:bifactor}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Index} & \\textbf{Value} & \\textbf{Threshold} \\\\\n\\midrule\nConvergence & No & --- \\\\\nRMSEA & 0.089 & $<0.06$ \\\\\nCFI & 0.71 & $>0.90$ \\\\\nTLI & 0.68 & $>0.90$ \\\\\nSRMR & 0.112 & $<0.08$ \\\\\nHeywood cases & 47 & 0 \\\\\nAnchor items identified & 0 & $>0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe bifactor IRT model (general factor + 57 subject-specific factors) fails to converge on the full matrix, with 47 Heywood cases (negative variance estimates).\nAll fit indices are far below acceptable thresholds.\nNo anchor items could be identified, terminating the IRT equating pipeline.\nThis negative result confirms that MMLU's item--model structure does not support confirmatory bifactor modeling at scale, consistent with the 98\\% person-misfit finding.\n\n\\subsection{Experiment 10: Item Generation and Calibration}\n\\label{sec:itemgen}\n\n\\begin{table}[h]\n\\centering\n\\caption{LLM-generated replacement item calibration. Difficulty correlation targets the 0.75 benchmark from the educational testing literature.}\n\\label{tab:itemgen}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} & \\textbf{Target} \\\\\n\\midrule\n$N$ items generated & 500 & --- \\\\\nDifficulty $\\rho$ (prompt-based) & 0.18 & 0.75 \\\\\nDifficulty $\\rho$ (student-sim) & 0.52 & 0.75 \\\\\nConstruct alignment (human) & 0.64 & $>0.80$ \\\\\nHoldout panel $\\rho$ & 0.41 & $>0.70$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem generation falls below all calibration benchmarks.\nPrompt-based difficulty targeting ($\\rho=0.18$) is near the bottom of the literature range (0.10--0.45).\nStudent-simulation calibration ($\\rho=0.52$) approaches but does not meet the 0.75 target.\nHuman-evaluated construct alignment (0.64) indicates 36\\% of generated items fall outside the intended cognitive level or subject boundary.\nHoldout model panel correlation (0.41) is insufficient to guarantee score equivalence.\nThe benchmark regeneration pipeline is not ready for deployment.\n\n\\subsection{Experiment 11: Cumulative Bayesian DIF}\n\\label{sec:bayesian}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cumulative Bayesian DIF power over successive administrations (simulation, $\\delta=1.0$). Target power: 0.70.}\n\\label{tab:bayesian}\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Administrations} & \\textbf{Power} \\\\\n\\midrule\n1 & 0.38 \\\\\n2 & 0.49 \\\\\n3 & 0.58 \\\\\n4 & 0.64 \\\\\n\\midrule\nTarget & 0.70 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSimulation shows monotonic power accumulation across successive administrations, but the target of 0.70 is not reached after 4 administrations at $\\delta=1.0$.\nThis is a simulation-only result with no real-data validation.\nThe stationarity assumption (benchmark items remain fixed across administrations) may be violated in the LLM setting where benchmarks themselves are subject to contamination over time.\n\n\\subsection{Experiment 12: Graceful Degradation Analysis}\n\\label{sec:degradation}\n\n\\begin{table}[h]\n\\centering\n\\caption{Benchmark validity metrics under progressive item replacement. $\\rho$ = Spearman rank correlation of model rankings with original benchmark. $\\alpha$ = Cronbach's reliability.}\n\\label{tab:degradation}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Replacement \\%} & $\\rho$ & $\\alpha$ & \\textbf{Coverage gap} \\\\\n\\midrule\n0\\% & 1.000 & 0.94 & --- \\\\\n5\\% & 0.994 & --- & --- \\\\\n10\\% & 0.986 & --- & --- \\\\\n20\\% & 0.961 & 0.88 & 3 subjects $>$30\\% loss \\\\\n50\\% & 0.873 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRanking correlation degrades faster than expected under item replacement.\nAt 20\\% replacement, $\\rho=0.961$ and reliability drops from 0.94 to 0.88.\nCritically, simple item \\emph{removal} (as in the diagnostic analysis of \\S\\ref{sec:exp1}) achieves $\\rho\\approx 0.997$---better than replacement---because the generated replacement items (\\S\\ref{sec:itemgen}) add noise rather than preserving measurement properties.\nThree subjects lose $>$30\\% of their items at 20\\% replacement, creating uneven construct coverage.\nTheoretical bounds are not tight enough to provide actionable replacement thresholds.\n\n\\subsection{Experiment 13: Item-Focused Trees}\n\\label{sec:ift}\n\n\\begin{table}[h]\n\\centering\n\\caption{MH vs.\\ Item-Focused Trees (IFT) flag comparison. IFT uses continuous temporal covariates rather than binary cohort splits.}\n\\label{tab:ift}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{Items flagged} & \\textbf{Unique flags} \\\\\n\\midrule\nMH-DIF & 3{,}918 (31.3\\%) & 1{,}650 \\\\\nIFT & 4{,}102 (32.8\\%) & 1{,}834 \\\\\n\\midrule\nJaccard overlap & \\multicolumn{2}{c}{0.48} \\\\\nFirst split variable & \\multicolumn{2}{c}{release\\_date} \\\\\nInteraction with model size & \\multicolumn{2}{c}{$p<0.01$} \\\\\nTemporal granularity & \\multicolumn{2}{c}{quarterly splits} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nItem-Focused Trees flag a comparable number of items (32.8\\%) but with only 48\\% overlap with MH, indicating substantial method disagreement.\nIFT's continuous temporal treatment reveals quarterly granularity and a significant interaction with model size ($p<0.01$), suggesting that larger models (released later) contribute disproportionately to DIF.\nThe 52\\% disagreement between methods raises questions about whether either method is detecting a robust item-level phenomenon or whether different modeling choices produce different artifact patterns.\n\n%% ============================================================\n%%  5  DISCUSSION AND LIMITATIONS\n%% ============================================================\n\\section{Discussion and Limitations}\n\n\\paragraph{Summary of findings.}\nWe characterize MMLU's temporal measurement properties using MH-DIF at unprecedented scale.\n31.3\\% of items show large DIF between model generations, robust to multiple analytical variations.\nThe semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000) provides a reusable evaluation infrastructure.\nDespite instability, MMLU rankings are resilient ($\\rho\\approx 0.997$), and DIF serves as a diagnostic lens for understanding inter-generational capability shifts.\n\n\\paragraph{IRT misspecification.}\nThe most significant limitation is the fundamental misspecification of unidimensional IRT for MMLU.\nWith 98\\% of models showing $|L_z|>2$, the total score used for MH ability matching is a collapsed composite of 57-subject abilities.\nTwo models with identical total scores may have very different subject-level ability profiles, creating systematic ability confounding that inflates DIF detection rates.\nThe 31.3\\% C\\% figure must be interpreted in this context: it represents items flagged under 1D matching, and an unknown fraction may be spurious DIF driven by multidimensional ability differences rather than genuine item-level changes.\n\n\\paragraph{Bifactor failure.}\nOur attempt to address misspecification via bifactor IRT modeling (\\S\\ref{sec:bifactor}) failed entirely (non-convergence, 47 Heywood cases).\nThis does not prove IRT is inapplicable to MMLU---exploratory MIRT or mixture IRT approaches may succeed---but it does confirm that confirmatory bifactor models are not viable at this scale.\n\n\\paragraph{Enrichment $\\approx$ 1.0.}\nDIF flags show no enrichment with web-overlap contamination labels.\nWe argue this is expected because web-overlap measures global exposure, not differential contamination.\nAn alternative interpretation is that DIF simply does not detect contamination.\nThe semi-synthetic results show DIF \\emph{can} detect injected differential contamination, but the gap between semi-synthetic injection (binary flipping) and real-world contamination mechanisms remains.\n\n\\paragraph{FPR.}\nDIF's FPR on Li-clean items is 0.318---nearly 1 in 3 clean items are flagged.\nCross-subject matching eliminates \\emph{inflation} but not the baseline rate.\nWithout ground truth for item-level differential contamination, we cannot determine what fraction of the 31.3\\% represents genuine item functioning changes vs.\\ multidimensional confounding.\n\n\\paragraph{GSM1K limitations.}\nThe GSM1K correlation ($r=-0.478$, $N=33$) is suggestive but limited by sample size (BCa CI upper bound $|r|=0.155$) and potential difficulty confounding.\n\n\\paragraph{Comparison method scope.}\nConStat evaluation covers only 220 reformulated items; DVD covers 200 items $\\times$ 12 models.\nEnsemble fusion produces a null result.\nFull-scale comparison would require substantially more resources.\n\n\\paragraph{Novelty.}\nMH-DIF is a textbook method from 1988.\nWe apply it without modification to a new domain.\nOur contributions are the empirical findings, the validation framework, and the ground-truth meta-critique---not algorithmic innovation.\n\n\\paragraph{Future directions.}\nThree paths forward: (1) multidimensional IRT or MIMIC models that properly account for MMLU's 57-subject structure, (2) larger-scale cross-benchmark validation with more matched models, and (3) integration with perturbation-based methods for a multi-signal diagnostic framework.\n\n%% ============================================================\n%%  6  CONCLUSION\n%% ============================================================\n\\section{Conclusion}\n\nWe apply Mantel--Haenszel DIF analysis to 5{,}227 models $\\times$ 12{,}508 MMLU items, finding 31.3\\% temporal item instability.\nThis finding is robust to threshold choice, multiple testing correction, and architecture composition, and is not explained by domain-level capability improvement ($\\le$7.6\\%).\nWe demonstrate that web-overlap contamination labels cannot validate item-level differential detectors and propose a semi-synthetic validation framework with cross-subject matching ($\\Delta$FPR$=$0.000).\nDespite 31\\% instability, MMLU rankings are massively redundant ($\\rho\\approx 0.997$), and DIF items serve as a diagnostic lens for inter-generational capability shifts rather than a quality filter.\n\nThe primary caveat is IRT misspecification: 98\\% of models show poor person-fit under unidimensional IRT, and the true rate of genuine item-level instability may be lower than 31.3\\%.\nResolving this requires multidimensional IRT methods that we have not yet successfully applied to MMLU-scale data.\n\n\\bibliographystyle{plainnat}\n\\begin{thebibliography}{10}\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021measuring}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Holland \\& Thayer(1988)]{holland1988differential}\nP.~W. Holland and D.~T. Thayer.\n\\newblock Differential item functioning and the {M}antel--{H}aenszel procedure.\n\\newblock In H.~Wainer and H.~I. Braun, editors, \\emph{Test Validity}, pages 129--145. Lawrence Erlbaum, 1988.\n\n\\bibitem[Li et~al.(2024)]{li2024task}\nY.~Li, Y.~Wang, and others.\n\\newblock Task contamination: Language models may not be few-shot anymore.\n\\newblock In \\emph{AAAI}, 2024.\n\n\\bibitem[Mantel \\& Haenszel(1959)]{mantel1959statistical}\nN.~Mantel and W.~Haenszel.\n\\newblock Statistical aspects of the analysis of data from retrospective studies of disease.\n\\newblock \\emph{Journal of the National Cancer Institute}, 22(4):719--748, 1959.\n\n\\bibitem[Polo et~al.(2024)]{constat2024}\nF.~M. Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.\n\\newblock {ConStat}: Performance-based contamination detection in large language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.16281}, 2024.\n\n\\bibitem[Shi et~al.(2024)]{shi2024detecting}\nW.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.\n\\newblock Detecting pretraining data from large language models.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Irt-llm(2024)]{irt_llm2024}\nIRT for LLM Evaluation.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "29734c7a-8094-46fa-af86-48eed0a9f6e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "58c2e60f-07ef-4272-9f9e-a83eb85d0c16",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case review simulation paper",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Tool call

_source line 22 · 2026-05-21T06:52:44.343Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017btM3a5ZXk52Q2869aR1jv`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c2e60f-07ef-4272-9f9e-a83eb85d0c16",
  "isSidechain": false,
  "requestId": "req_011CbFGmamXGVnJG5QmGSDPB",
  "type": "assistant",
  "uuid": "3ce0ae90-b1f1-4856-ad32-16f7fe887d76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015LrC2AUb4XJEoUmswKM3QG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10494,
      "cache_read_input_tokens": 40827,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10494,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 40827,
          "cache_creation_input_tokens": 10494,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10494
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

_source line 23 · 2026-05-21T06:52:45.290Z_

<details><summary>↩ Tool result · `toolu_017btM3a5ZXk52Q2869aR1jv`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
n input line 38.


Package natbib Warning: Citation `holland1988differential' on page 1 undefined 
on input line 40.


Overfull \hbox (26.74255pt too wide) in paragraph at lines 53--56
[]\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion frame-work. $\OT1/cmr/m/n/10 ^^
A$TPR method-ol-ogy with cross-subject match-ing ($^^A$FPR$=$0.000).

Package natbib Warning: Citation `li2024task' on page 1 undefined on input line
 73.


Package natbib Warning: Citation `constat2024' on page 1 undefined on input lin
e 74.


Package natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu
t line 74.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `mantel1959statistical' on page 2 undefined on
 input line 78.


Package natbib Warning: Citation `holland1988differential' on page 2 undefined 
on input line 78.


Package natbib Warning: Citation `irt_llm2024' on page 2 undefined on input lin
e 83.

[2]

LaTeX Warning: `h' float specifier changed to `ht'.


Underfull \hbox (badness 1325) in paragraph at lines 225--225
[]\OT1/cmr/m/n/10 Table 5: []Standard vs. cross-subject match-ing. Cross-subjec
t match-ing elim-i-nates FPR in-fla-tion

LaTeX Warning: `h' float specifier changed to `ht'.

[3] [4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.

[6]

LaTeX Warning: `h' float specifier changed to `ht'.


LaTeX Warning: Reference `sec:exp1' on page 7 undefined on input line 521.


LaTeX Warning: Reference `sec:itemgen' on page 7 undefined on input line 521.

[7]

LaTeX Warning: Reference `sec:bifactor' on page 8 undefined on input line 569.

[8] [9]

Package natbib Warning: There were undefined citations.

[10] (./paper.aux

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
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 257166 bytes).
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
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
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
Overfull \hbox (26.74255pt too wide) in paragraph at lines 53--56
[]\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion frame-work. $\OT1/cmr/m/n/10 ^^
A$TPR method-ol-ogy with cross-subject match-ing ($^^A$FPR$=$0.000).
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]
Underfull \hbox (badness 1325) in paragraph at lines 225--225
[]\OT1/cmr/m/n/10 Table 5: []Standard vs. cross-subject match-ing. Cross-subjec
t match-ing elim-i-nates FPR in-fla-tion
[4] [5]

LaTeX Warning: `h' float specifier changed to `ht'.

[6] [7] [8] [9] [10] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist
/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 260332 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ce0ae90-b1f1-4856-ad32-16f7fe887d76",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "6a7d9f1c-ec54-40fc-82b9-80b135b9039d",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `hendrycks2021measuring' on page 1 undefined o\nn input line 38.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 1 undefined \non input line 40.\n\n\nOverfull \\hbox (26.74255pt too wide) in paragraph at lines 53--56\n[]\\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion frame-work. $\\OT1/cmr/m/n/10 ^^\nA$TPR method-ol-ogy with cross-subject match-ing ($^^A$FPR$=$0.000).\n\nPackage natbib Warning: Citation `li2024task' on page 1 undefined on input line\n 73.\n\n\nPackage natbib Warning: Citation `constat2024' on page 1 undefined on input lin\ne 74.\n\n\nPackage natbib Warning: Citation `shi2024detecting' on page 1 undefined on inpu\nt line 74.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `mantel1959statistical' on page 2 undefined on\n input line 78.\n\n\nPackage natbib Warning: Citation `holland1988differential' on page 2 undefined \non input line 78.\n\n\nPackage natbib Warning: Citation `irt_llm2024' on page 2 undefined on input lin\ne 83.\n\n[2]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nUnderfull \\hbox (badness 1325) in paragraph at lines 225--225\n[]\\OT1/cmr/m/n/10 Table 5: []Standard vs. cross-subject match-ing. Cross-subjec\nt match-ing elim-i-nates FPR in-fla-tion\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[3] [4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nLaTeX Warning: Reference `sec:exp1' on page 7 undefined on input line 521.\n\n\nLaTeX Warning: Reference `sec:itemgen' on page 7 undefined on input line 521.\n\n[7]\n\nLaTeX Warning: Reference `sec:bifactor' on page 8 undefined on input line 569.\n\n[8] [9]\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 257166 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\nOverfull \\hbox (26.74255pt too wide) in paragraph at lines 53--56\n[]\\OT1/cmr/bx/n/10 Semi-synthetic val-i-da-tion frame-work. $\\OT1/cmr/m/n/10 ^^\nA$TPR method-ol-ogy with cross-subject match-ing ($^^A$FPR$=$0.000).\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}] [2] [3]\nUnderfull \\hbox (badness 1325) in paragraph at lines 225--225\n[]\\OT1/cmr/m/n/10 Table 5: []Standard vs. cross-subject match-ing. Cross-subjec\nt match-ing elim-i-nates FPR in-fla-tion\n[4] [5]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[6] [7] [8] [9] [10] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/te\nxmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist\n/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 260332 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3ce0ae90-b1f1-4856-ad32-16f7fe887d76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T06:52:48.221Z_

<details><summary>Logged reasoning block</summary>

```text
Some labels changed between runs - let me do a third pass to ensure cross-references are stable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a7d9f1c-ec54-40fc-82b9-80b135b9039d",
  "isSidechain": false,
  "requestId": "req_011CbFGmuRBsshQxvq2S2bQP",
  "type": "assistant",
  "uuid": "a807ce97-23a3-46ea-b6e2-64491357fb9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnRAazbN9x2pKtrHyxbv4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6257,
      "cache_read_input_tokens": 51321,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 51321,
          "cache_creation_input_tokens": 6257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6257
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

_source line 25 · 2026-05-21T06:52:48.656Z_

Labels shifted between passes. Running a third compilation to stabilize cross-references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a807ce97-23a3-46ea-b6e2-64491357fb9a",
  "isSidechain": false,
  "requestId": "req_011CbFGmuRBsshQxvq2S2bQP",
  "type": "assistant",
  "uuid": "4160d311-f016-42cd-9d78-fac17ea55b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnRAazbN9x2pKtrHyxbv4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6257,
      "cache_read_input_tokens": 51321,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 51321,
          "cache_creation_input_tokens": 6257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6257
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

_source line 26 · 2026-05-21T06:52:51.728Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HJPyPTvXYaqpDfxKMFdQDw`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass for stable cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4160d311-f016-42cd-9d78-fac17ea55b38",
  "isSidechain": false,
  "requestId": "req_011CbFGmuRBsshQxvq2S2bQP",
  "type": "assistant",
  "uuid": "8bc9ed91-9654-46af-8de8-89deb0d16e30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnRAazbN9x2pKtrHyxbv4R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6257,
      "cache_read_input_tokens": 51321,
      "output_tokens": 202,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 202,
          "cache_read_input_tokens": 51321,
          "cache_creation_input_tokens": 6257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6257
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "8bc9ed91-9654-46af-8de8-89deb0d16e30",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case review simulation paper",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Tool result

_source line 29 · 2026-05-21T06:52:52.256Z_

<details><summary>↩ Tool result · `toolu_01HJPyPTvXYaqpDfxKMFdQDw`</summary>

```text
public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmti9.pfb>
Output written on paper.pdf (10 pages, 260332 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bc9ed91-9654-46af-8de8-89deb0d16e30",
  "isSidechain": false,
  "promptId": "8cf10ffa-207e-4cd3-a377-eb54084e198b",
  "type": "user",
  "uuid": "c791bdc8-57d3-471e-97d3-98fee5423e98",
  "toolUseResult": {
    "stdout": "public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmti9.pfb>\nOutput written on paper.pdf (10 pages, 260332 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8bc9ed91-9654-46af-8de8-89deb0d16e30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T06:53:00.780Z_

PDF 编译成功，10 页，无错误。输出位于 `artifacts/dream_reports/dream_20260521T062008/worst/paper.pdf`。

论文覆盖全部 13 个实验（对应 experiment_data.json），每个实验有独立 section 和数据表。所有数字直接取自 JSON，未编造。narrative 按 worst-tier 定位：坦承 IRT misspecification（98% |Lz|>2）、bifactor 失败、ensemble null result、item generation below benchmark，为 reviewer 的 artifact 解读留出攻击面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c791bdc8-57d3-471e-97d3-98fee5423e98",
  "isSidechain": false,
  "requestId": "req_011CbFGnRHYKUTZb763REWsU",
  "type": "assistant",
  "uuid": "eaa3478e-3921-4a70-8e6f-f25c42394ce4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dream_reports/dream_20260521T062008/worst",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FR4LWPV98mvhJWcyGGyQLv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 57578,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 57578,
          "cache_creation_input_tokens": 277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 277
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T062008 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench…",
  "leafUuid": "eaa3478e-3921-4a70-8e6f-f25c42394ce4",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-case review simulation paper",
  "sessionId": "ed986e33-bb2e-41ac-8746-1983d5200adc"
}
```

---
