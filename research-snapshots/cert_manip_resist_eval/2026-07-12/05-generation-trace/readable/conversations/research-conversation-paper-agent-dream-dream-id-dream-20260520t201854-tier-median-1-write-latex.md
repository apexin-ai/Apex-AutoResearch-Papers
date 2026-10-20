# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/0d3cc3e1-6aa1-400a-9ec7-57570d53ef19.jsonl`
- **Structured JSON:** [`b7a0b0833c3104e72297.json`](../../sessions/b7/b7a0b0833c3104e72297.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T20:46:25.777Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T20:46:25.777Z",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Analysis paper with principled negative result as centerpiece. Narrative arc: (1) Pareto frontier established on two large MoE architectures — qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming architecture-dependent shape; (2) CKA reveals geometric misalignment increasing with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across 3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions but cannot correct the rotation of the correctness direction across language subspaces; (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and orthogonality are supporting evidence. Decomposition shows difficulty is shared but capability-specific component drives degradation (~65% of combos improved). Orthogonality persists across languages (cosine < 0.10) but with more variance in low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn are weaker. ECE improvements over temperature scaling are negligible — emphasize AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T20:46:25.781Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T20:46:25.781Z",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

## Round 1

53 recorded events

### User

_source line 3 · 2026-05-20T20:46:25.808Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Analysis paper with principled negative result as centerpiece. Narrative arc: (1) Pareto frontier established on two large MoE architectures — qualitatively replicates MVP findings but rho is moderate (median ~-0.52), confirming architecture-dependent shape; (2) CKA reveals geometric misalignment increasing with depth — CKA-transfer correlation r≈0.58 provides mechanistic explanation for WHY deeper layers transfer worse; (3) CaCLR consistency loss (β) is inert across 3 OOM sweep — this is PREDICTED by the geometric explanation: MMD matches distributions but cannot correct the rotation of the correctness direction across language subspaces; (4) Linear projection succeeds (~+3.5pp over zero-shot) precisely because it learns the rotation that MMD cannot, saturating at ~70 parallel pairs. Decomposition and orthogonality are supporting evidence. Decomposition shows difficulty is shared but capability-specific component drives degradation (~65% of combos improved). Orthogonality persists across languages (cosine < 0.10) but with more variance in low-resource languages. Control tasks confirm probe selectivity (>10pp) but sw/bn are weaker. ECE improvements over temperature scaling are negligible — emphasize AUROC and mechanistic understanding. Target: borderline to weak accept at EACL.

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "dc81014b-950e-4a11-8694-5137ef2540e2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T20:46:25.807Z_

```json
{
  "parentUuid": "dc81014b-950e-4a11-8694-5137ef2540e2",
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
  "uuid": "8e8f692f-e829-4f9b-9f31-6af711a1d361",
  "timestamp": "2026-05-20T20:46:25.807Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T20:46:25.807Z_

```json
{
  "parentUuid": "8e8f692f-e829-4f9b-9f31-6af711a1d361",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "03b962f4-877d-4dba-bb4b-d025f12354b6",
  "timestamp": "2026-05-20T20:46:25.807Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
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
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Assistant

_source line 7 · 2026-05-20T20:46:41.235Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b962f4-877d-4dba-bb4b-d025f12354b6",
  "isSidechain": false,
  "requestId": "req_011CbEUYDuBsMzhyhPdA22Dp",
  "type": "assistant",
  "uuid": "b6118811-68c2-41ee-9ed5-c16f6bdcd89f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkUWwcbqzDPxfo2X3DLfRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11618
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

_source line 8 · 2026-05-20T20:46:42.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DQbwfj1ixJGu186VGf4H3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6118811-68c2-41ee-9ed5-c16f6bdcd89f",
  "isSidechain": false,
  "requestId": "req_011CbEUYDuBsMzhyhPdA22Dp",
  "type": "assistant",
  "uuid": "99c136ae-5794-4823-ac10-7a29c4c5130b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkUWwcbqzDPxfo2X3DLfRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11618
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

_source line 9 · 2026-05-20T20:46:43.013Z_

<details><summary>↩ Tool result · `toolu_01DQbwfj1ixJGu186VGf4H3n`</summary>

```text
1	[
2	  {
3	    "name": "Qwen3-235B-A22B Full Pareto Frontier",
4	    "description": "Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24 probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.\n",
5	    "results": {
6	      "en_best_auroc": 0.81,
7	      "en_best_layer": 72,
8	      "en_best_ece_raw": 0.17,
9	      "en_best_ece_tempcal": 0.065,
10	      "temp_scaling_T": 5.8,
11	      "en_auroc_range": [
12	        0.58,
13	        0.81
14	      ],
15	      "en_auroc_50pct_depth_layer47": 0.76,
16	      "zs_transfer_auroc_median_20lang_at_en_optimal": 0.63,
17	      "zs_transfer_auroc_median_20lang_at_best_transfer_layer": 0.7,
18	      "best_transfer_layer": 48,
19	      "pareto_rho_global": -0.58,
20	      "pareto_rho_per_lang_median": -0.51,
21	      "pareto_rho_per_lang_range": [
22	        -0.78,
23	        -0.21
24	      ],
25	      "zs_langs_above_0p65": 13,
26	      "zs_auroc_zh": 0.74,
27	      "zs_auroc_es": 0.73,
28	      "zs_auroc_fr": 0.73,
29	      "zs_auroc_de": 0.72,
30	      "zs_auroc_ar": 0.7,
31	      "zs_auroc_hi": 0.69,
32	      "zs_auroc_ru": 0.71,
33	      "zs_auroc_ko": 0.69,
34	      "zs_auroc_ja": 0.7,
35	      "zs_auroc_pt": 0.72,
36	      "zs_auroc_vi": 0.68,
37	      "zs_auroc_tr": 0.67,
38	      "zs_auroc_id": 0.68,
39	      "zs_auroc_th": 0.66,
40	      "zs_auroc_pl": 0.69,
41	      "zs_auroc_uk": 0.68,
42	      "zs_auroc_he": 0.66,
43	      "zs_auroc_el": 0.65,
44	      "zs_auroc_sw": 0.58,
45	      "zs_auroc_bn": 0.57,
46	      "mean_shift_delta_auroc_median": 0.0,
47	      "linear_proj_delta_auroc_over_zs_median": 0.035,
48	      "fewshot_25_delta_auroc_over_zs_median": 0.025,
49	      "fewshot_100_delta_auroc_over_zs_median": 0.045,
50	      "ece_reduction_vs_temp_scaling_median": 0.008
51	    },
52	    "tables": [
53	      {
54	        "name": "Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer",
55	        "description": "24 probed layers (rows) × 20 languages + English (columns). Cells show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI. Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most languages. High-resource languages show flatter profiles; low-resource show steeper drop-off at deep layers.\n"
56	      },
57	      {
58	        "name": "Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers",
59	        "description": "5 transfer methods (columns) × 20 languages (rows), evaluated at two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation test p-values. Cohen's d for each method vs zero-shot baseline.\n"
60	      }
61	    ],
62	    "figures": [],
63	    "analysis": "The Pareto frontier replicates on this large MoE model but with moderate per-language rho (-0.51 median). The architecture-dependent shape is visible: MoE routing creates more variable layer representations, so the depth-transfer tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating the approach for most languages. The 7 languages below threshold cluster in low-resource (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear projection provides the most consistent improvement across languages.\n\n\nQwen3-235B-A22B is a 94-layer MoE model — significantly deeper than the 7B MVP. The English best AUROC rises to 0.81 because the larger model encodes stronger correctness signals (more parameters, more knowledge). The best English layer is at ~76% depth (layer 72), consistent with the MVP pattern where correctness peaks in deep-but-not-final layers. The Pareto frontier is present but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates more heterogeneous layer representations, reducing the clean monotonic depth-degradation pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr) have strong multilingual representations even at deeper layers due to extensive pretraining data, attenuating the negative correlation. The per-language rho range [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative correlation (their representations diverge from English more sharply at depth) while high-resource languages show weaker correlation (they maintain reasonable alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57) remain below threshold due to limited pretraining representation for these languages. Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because it directly corrects geometric misalignment rather than relying on a small labeled sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based calibration and temperature scaling address different aspects — at the median tier, probes don't provide much additional calibration beyond what temperature scaling already captures.\n"
64	  },
65	  {
66	    "name": "Llama 4 Scout Full Pareto Frontier",
67	    "description": "Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.\n",
68	    "results": {
69	      "en_best_auroc": 0.79,
70	      "en_best_layer": 36,
71	      "en_best_ece_raw": 0.19,
72	      "en_best_ece_tempcal": 0.07,
73	      "temp_scaling_T": 6.0,
74	      "en_auroc_range": [
75	        0.6,
76	        0.79
77	      ],
78	      "en_auroc_50pct_depth_layer24": 0.74,
79	      "zs_transfer_auroc_median_20lang_at_en_optimal": 0.62,
80	      "zs_transfer_auroc_median_20lang_at_best_transfer_layer": 0.68,
81	      "best_transfer_layer": 24,
82	      "pareto_rho_global": -0.62,
83	      "pareto_rho_per_lang_median": -0.54,
84	      "pareto_rho_per_lang_range": [
85	        -0.82,
86	        -0.28
87	      ],
88	      "zs_langs_above_0p65": 11,
89	      "zs_auroc_zh": 0.72,
90	      "zs_auroc_es": 0.71,
91	      "zs_auroc_fr": 0.71,
92	      "zs_auroc_de": 0.7,
93	      "zs_auroc_ar": 0.68,
94	      "zs_auroc_hi": 0.67,
95	      "zs_auroc_ru": 0.69,
96	      "zs_auroc_ko": 0.66,
97	      "zs_auroc_ja": 0.67,
98	      "zs_auroc_pt": 0.7,
99	      "zs_auroc_vi": 0.65,
100	      "zs_auroc_tr": 0.64,
101	      "zs_auroc_id": 0.66,
102	      "zs_auroc_th": 0.63,
103	      "zs_auroc_pl": 0.67,
104	      "zs_auroc_uk": 0.65,
105	      "zs_auroc_he": 0.63,
106	      "zs_auroc_el": 0.62,
107	      "zs_auroc_sw": 0.55,
108	      "zs_auroc_bn": 0.54,
109	      "mean_shift_delta_auroc_median": 0.0,
110	      "linear_proj_delta_auroc_over_zs_median": 0.032,
111	      "fewshot_25_delta_auroc_over_zs_median": 0.022,
112	      "fewshot_100_delta_auroc_over_zs_median": 0.04,
113	      "ece_reduction_vs_temp_scaling_median": 0.005
114	    },
115	    "tables": [
116	      {
117	        "name": "Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer",
118	        "description": "12 probed layers × 20 languages + English. Same format as Table 1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal set due to coarser layer sampling.\n"
119	      },
120	      {
121	        "name": "Table 4: Llama 4 Scout Transfer Method Comparison",
122	        "description": "Same format as Table 2. Llama 4 Scout results. Key finding: linear projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric correction transfers across architectures.\n"
123	      }
124	    ],
125	    "figures": [],
126	    "analysis": "Llama 4 Scout confirms the Pareto frontier generalizes across architectures. The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that supports the architecture-dependence claim but is not dramatic enough to call it a strong architectural contrast. This is the median-tier signature: same qualitative finding, quantitatively less distinct than ideal. Both models agree on the key implication: mid-depth layers are the right operating point for cross-lingual transfer.\n\n\nLlama 4 Scout has fewer layers (48 vs 94) and a different MoE architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81) reflecting somewhat weaker correctness encoding in a shallower architecture. The Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers, each layer step represents a larger proportional depth change, making the depth-transfer tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent with the pattern that mid-depth layers balance English quality and cross-lingual alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4's multilingual pretraining may be less balanced, particularly for mid-resource languages like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55) and bn (0.54) are again the weakest, confirming this is a fundamental limitation of pretraining representation rather than architecture-specific. The same qualitative Pareto pattern holds but the quantitative frontier shape differs — the drop-off from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence without requiring architecture-specific tuning as a paper claim.\n"
127	  },
128	  {
129	    "name": "CaCLR Implementation and Comparative Evaluation",
130	    "description": "CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD). α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot, mean-shift, linear projection, few-shot on both models × 20 langs.\n",
131	    "results": {
132	      "alpha_optimal": 0.5,
133	      "alpha_only_en_auroc_at_en_optimal_layer_qwen": 0.805,
134	      "alpha_only_en_ece_at_en_optimal_layer_qwen": 0.058,
135	      "alpha_only_zs_median_auroc_qwen": 0.695,
136	      "alpha_only_zs_median_auroc_llama": 0.675,
137	      "beta_0p001_delta_auroc_over_alpha_only_median": 0.002,
138	      "beta_0p01_delta_auroc_over_alpha_only_median": 0.001,
139	      "beta_0p1_delta_auroc_over_alpha_only_median": -0.001,
140	      "beta_1p0_delta_auroc_over_alpha_only_median": -0.003,
141	      "beta_sweep_max_delta_auroc": 0.003,
142	      "beta_sweep_significant_at_p05": false,
143	      "caclr_full_delta_auroc_over_zeroshot_median": 0.012,
144	      "caclr_full_delta_auroc_over_zeroshot_range": [
145	        -0.005,
146	        0.035
147	      ],
148	      "caclr_vs_linear_proj_delta_median": -0.023,
149	      "caclr_vs_fewshot100_delta_median": -0.033,
150	      "linear_proj_delta_auroc_over_zs_median_qwen": 0.035,
151	      "linear_proj_delta_auroc_over_zs_median_llama": 0.032,
152	      "fewshot_25_delta_auroc_over_zs_median": 0.024,
153	      "fewshot_100_delta_auroc_over_zs_median": 0.043,
154	      "mean_shift_delta_auroc_median": 0.0,
155	      "method_ranking": [
156	        "few-shot-100",
157	        "linear-projection",
158	        "few-shot-25",
159	        "CaCLR-full",
160	        "CaCLR-α-only",
161	        "zero-shot",
162	        "mean-shift"
163	      ],
164	      "caclr_beta_delta_high_resource": 0.004,
165	      "caclr_beta_delta_mid_resource": 0.0,
166	      "caclr_beta_delta_low_resource": -0.002,
167	      "caclr_beta_vs_alpha_only_paired_perm_p": 0.42,
168	      "caclr_beta_vs_alpha_only_cohens_d": 0.08,
169	      "linear_proj_vs_zeroshot_paired_perm_p": 0.001,
170	      "linear_proj_vs_zeroshot_cohens_d": 0.55
171	    },
172	    "tables": [
173	      {
174	        "name": "Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline",
175	        "description": "β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns: median ΔAUROC, mean, std, min, max, # languages improved, paired permutation p-value, Cohen's d). Both models shown side-by-side. Key: no β value achieves p < 0.05 or d > 0.2 — consistency loss is definitively inert.\n"
176	      },
177	      {
178	        "name": "Table 6: Transfer Method Comparison — Median AUROC across 20 Languages",
179	        "description": "Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full, linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama 4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap 95% CI. Ranking is consistent across models. Linear projection and few-shot clearly dominate.\n"
180	      },
181	      {
182	        "name": "Table 7: CaCLR β Effect by Resource Tier",
183	        "description": "Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness is consistent across tiers — not a power issue with low-resource languages but a fundamental limitation of distributional matching.\n"
184	      }
185	    ],
186	    "figures": [],
187	    "analysis": "CaCLR's β inertness is the paper's centerpiece negative result. The analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08, p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear projection's success (+3.5pp) confirms the geometric explanation — it succeeds precisely because it learns the rotation that MMD cannot represent. This three-part argument closes the distributional-matching path with both theory and evidence. The α-only variant retains value as a calibration regularizer — it improves ECE without hurting AUROC.\n\n\nThe β (consistency loss) is inert because MMD-based distributional matching fundamentally cannot correct the geometric misalignment that CKA reveals. MMD penalizes differences in mean embeddings and kernel-space distributional moments — it can align marginal distributions but cannot learn the rotation of the correctness direction across language subspaces. At low β (0.001), the MMD signal is too weak to affect optimization. At medium β (0.01–0.1), the gradient signal exists but points in the wrong direction — it pushes overall distributional alignment without specifically aligning the correctness-relevant subspace. At high β (1.0), the MMD term dominates and slightly hurts English AUROC by distorting the probe weights. The α-only (SB-ECE) variant provides small but real calibration improvement (better ECE) because smooth-binned ECE regularization is a well-motivated objective that doesn't require cross-lingual alignment. The total CaCLR improvement over zero-shot (+1.2pp) comes entirely from the α term's calibration regularization, not from cross-lingual consistency. Cohen's d = 0.08 for β effect is negligible. In contrast, linear projection achieves +3.5pp because it directly estimates and corrects the rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves +4.3pp because it sidesteps alignment entirely by training on target-language labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot > mean-shift — is the key empirical result that the geometric explanation predicts.\n"
188	  },
189	  {
190	    "name": "Difficulty-Controlled Decomposition Ablation",
191	    "description": "IRT difficulty probes, project out difficulty direction, retrain correctness probes on residuals. 10 languages × 8 layers per model. Random-direction control.\n",
192	    "results": {
193	      "difficulty_probe_r2_en_median_across_layers": 0.42,
194	      "difficulty_probe_r2_range": [
195	        0.25,
196	        0.55
197	      ],
198	      "decomposition_transfer_delta_median": 0.012,
199	      "decomposition_transfer_delta_range": [
200	        -0.01,
201	        0.035
202	      ],
203	      "pct_combos_improved": 0.65,
204	      "pct_combos_improved_by_tier_high": 0.72,
205	      "pct_combos_improved_by_tier_mid": 0.65,
206	      "pct_combos_improved_by_tier_low": 0.53,
207	      "improvement_stronger_at_deep_layers": true,
208	      "improvement_at_shallow_layers_pct": 0.5,
209	      "improvement_at_deep_layers_pct": 0.78,
210	      "random_direction_delta_median": 0.003,
211	      "random_direction_delta_significant": false,
212	      "difficulty_correctness_cosine_median": 0.18,
213	      "difficulty_correctness_cosine_range": [
214	        0.08,
215	        0.3
216	      ],
217	      "decomposition_vs_baseline_paired_p": 0.03,
218	      "decomposition_cohens_d": 0.28
219	    },
220	    "tables": [
221	      {
222	        "name": "Table 8: Decomposition Results — 10 Languages × 8 Layers",
223	        "description": "Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded. Marginal summaries: % improved per language, per layer. Shows concentration of improvement at deep layers and high-resource languages.\n"
224	      },
225	      {
226	        "name": "Table 9: Decomposition vs Random Direction Control",
227	        "description": "Comparison: difficulty projection vs random projection vs no projection. Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically — not arbitrary dimensionality reduction — drives improvement.\n"
228	      }
229	    ],
230	    "figures": [],
231	    "analysis": "Decomposition provides supporting evidence for the geometric misalignment narrative. The fact that difficulty removal helps more at deep layers aligns with the CKA finding — at depth, the capability-specific component (which is geometrically misaligned across languages) drives transfer failure, and removing the shared difficulty component isolates this effect. However, the partial success rate (65%) and modest effect size (d=0.28) keep this as supporting analysis rather than a standalone claim. The finding is prescriptive: researchers attempting cross-lingual probe transfer should first assess whether difficulty confounding explains their transfer gaps — in ~65% of cases, it partially does.\n\n\nDecomposition works but is partial because the difficulty-capability separation is not clean. The difficulty direction (IRT-derived) captures ~42% variance in human difficulty scores (R²) — reasonable but not perfect, meaning the projection leaves residual difficulty signal mixed with capability. At deep layers, removing difficulty helps more often (78% of combos) because the capability-specific component dominates transfer degradation there — once you remove the shared difficulty signal, the residual is more language-specific and harder to transfer. At shallow layers, the improvement rate drops to ~50% (near chance) because both difficulty and capability signals are more entangled and less linearly separable. The 65% overall improvement rate is genuine but not universal — it demonstrates the decomposition is prescriptive for about two-thirds of settings. The random-direction control (median +0.3pp, not significant) confirms this isn't a dimensionality-reduction artifact. Low-resource languages show weaker improvement (53%) because their correctness probes are noisier to begin with, and the difficulty projection may remove some of the limited signal they have. The modest Cohen's d (0.28) reflects that improvements are real but small — this is a supporting analytical result, not a standalone method contribution.\n"
232	  },
233	  {
234	    "name": "Cross-Lingual Orthogonality Analysis",
235	    "description": "Verbalized confidence direction extraction, cosine similarity with correctness direction. 20 languages × 2 architectures. Resource-tier and family analysis.\n",
236	    "results": {
237	      "en_cosine_qwen": 0.035,
238	      "en_cosine_llama": 0.038,
239	      "cosine_median_across_langs_qwen": 0.055,
240	      "cosine_median_across_langs_llama": 0.06,
241	      "cosine_max_across_langs": 0.1,
242	      "cosine_max_language": "sw",
243	      "cosine_range": [
244	        0.02,
245	        0.1
246	      ],
247	      "cosine_median_high_resource": 0.04,
248	      "cosine_median_mid_resource": 0.06,
249	      "cosine_median_low_resource": 0.085,
250	      "cosine_variance_high": 0.0003,
251	      "cosine_variance_mid": 0.0008,
252	      "cosine_variance_low": 0.0018,
253	      "all_langs_below_threshold": true,
254	      "cosine_vs_resource_spearman_rho": 0.52,
255	      "cosine_vs_resource_p": 0.018
256	    },
257	    "tables": [
258	      {
259	        "name": "Table 10: Correctness–Confidence Cosine Similarity Across Languages",
260	        "description": "20 languages (rows, grouped by resource tier) × 2 architectures (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier medians and Spearman correlation with log(pretraining data estimate). All values < 0.12.\n"
261	      }
262	    ],
263	    "figures": [],
264	    "analysis": "Orthogonality holds universally (max 0.10 < 0.12 threshold) but with a resource- tier gradient that is novel relative to Miao & Ungar's English-only finding. This extends their claim to multilingual settings with a nuance: the structural separation is slightly weaker for low-resource languages, though never approaching a level that would make output-based calibration viable. This supports the paper's broader argument that probe-based calibration is the right paradigm for all languages, but the cross-lingual transfer challenge is the bottleneck — not the underlying signal quality.\n\n\nOrthogonality persists across languages because the separation between correctness and verbalized confidence is a structural property of how transformers process MCQA — the model's internal \"do I know this?\" signal (correctness) and its verbalized \"how confident am I?\" output occupy orthogonal subspaces by design (the former is a representation-level property, the latter is optimized during RLHF/instruction-tuning for human-readable outputs). The English cosine (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly higher (median 0.055-0.060) because: (a) non-English confidence verbalization is noisier (models are less calibrated in non-English expression of uncertainty); (b) the confidence probe may capture some language-switching signal that correlates weakly with correctness (lower-resource languages trigger more uncertain generation behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold (<0.12) but shows more variance — Swahili's limited pretraining data means both probes are noisier, and noise correlations inflate apparent cosine. The resource- tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger (lower cosine) for high-resource languages, suggesting that abundant pretraining data helps separate correctness from confidence representations. However, even the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment, confirming that output-based calibration is structurally limited across all languages.\n"
265	  },
266	  {
267	    "name": "Probe Complexity Comparison",
268	    "description": "Logistic regression vs 2-layer MLP at each probed layer for both models. English accuracy, cross-lingual transfer degradation, calibration quality.\n",
269	    "results": {
270	      "logreg_en_best_auroc_qwen": 0.81,
271	      "mlp_en_best_auroc_qwen": 0.835,
272	      "logreg_en_best_auroc_llama": 0.79,
273	      "mlp_en_best_auroc_llama": 0.815,
274	      "logreg_zs_median_qwen": 0.7,
275	      "mlp_zs_median_qwen": 0.665,
276	      "logreg_zs_median_llama": 0.68,
277	      "mlp_zs_median_llama": 0.645,
278	      "logreg_transfer_gap": 0.11,
279	      "mlp_transfer_gap": 0.17,
280	      "logreg_ece_median": 0.068,
281	      "mlp_ece_median": 0.075,
282	      "mlp_advantage_en_deep_layers": 0.03,
283	      "mlp_advantage_en_shallow_layers": 0.01,
284	      "logreg_better_transfer_pct_langs": 0.8
285	    },
286	    "tables": [
287	      {
288	        "name": "Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer",
289	        "description": "Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP's higher EN AUROC comes at cost of larger transfer gap. Gap difference increases with depth.\n"
290	      }
291	    ],
292	    "figures": [],
293	    "analysis": "This experiment justifies the methodological choice of logistic regression probes and provides additional evidence for the geometric/linear framing. If the correctness signal were deeply nonlinear, MLP's advantage would transfer — the fact that it doesn't confirms that the transferable component is linear. Goes in supplementary material as a methodological validation.\n\n\nMLP probes achieve ~2.5pp higher English AUROC because they can capture nonlinear interactions in the representation — the correctness signal has a small nonlinear component that logistic regression misses. However, this nonlinear component is language-specific (learned from English data, doesn't generalize), so MLP probes show 6pp larger transfer gap than logistic regression. The MLP essentially overfits to English-specific nonlinearities in the correctness representation. This confirms the hypothesis that linear probes transfer better cross-lingually — the linear component of the correctness signal is more universal across languages, while nonlinear components are language-specific. The MLP advantage is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper representations have more complex, language-specific structure for the MLP to exploit. 80% of languages see better transfer with logistic regression, with the exceptions being high- resource languages (zh, es) where the MLP's nonlinear component partially transfers due to shared pretraining features. This result justifies the paper's focus on logistic regression probes and reinforces the geometric (linear) framing.\n"
294	  },
295	  {
296	    "name": "Additional Benchmark Evaluation (Belebele + MMLU-ProX)",
297	    "description": "Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages each). Validates generalization beyond GlobalMMLU.\n",
298	    "results": {
299	      "belebele_en_best_auroc_qwen": 0.78,
300	      "belebele_zs_median_qwen": 0.68,
301	      "belebele_pareto_rho_median": -0.48,
302	      "belebele_linear_proj_delta": 0.03,
303	      "belebele_caclr_beta_delta": 0.003,
304	      "mmlupx_en_best_auroc_qwen": 0.82,
305	      "mmlupx_zs_median_qwen": 0.69,
306	      "mmlupx_pareto_rho_median": -0.5,
307	      "mmlupx_linear_proj_delta": 0.033,
308	      "mmlupx_caclr_beta_delta": 0.002,
309	      "auroc_rank_correlation_globalmmlu_vs_belebele": 0.82,
310	      "auroc_rank_correlation_globalmmlu_vs_mmlupx": 0.88,
311	      "method_ranking_consistent_across_benchmarks": true
312	    },
313	    "tables": [
314	      {
315	        "name": "Table S2: Cross-Benchmark Generalization",
316	        "description": "Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX) × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows consistent patterns across benchmarks. Rank correlation between per-language AUROCs.\n"
317	      }
318	    ],
319	    "figures": [],
320	    "analysis": "Benchmark generalization confirms all findings are not artifacts of GlobalMMLU. The consistent method ranking across three benchmarks strengthens the negative result — CaCLR's β inertness is a fundamental property of distributional matching vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary or a short main-text paragraph.\n\n\nBelebele is a reading comprehension benchmark — fundamentally different from MCQA knowledge testing. The correctness signal is still present (models either comprehend or don't) but Belebele's English AUROC is slightly lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly encoded than factual knowledge correctness. The Pareto rho is slightly weaker (-0.48) because Belebele's parallel passages provide more uniform cross-lingual signal than GlobalMMLU's diverse topics. MMLU-ProX, being closer to GlobalMMLU in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding is that method rankings are consistent — linear projection still outperforms CaCLR, and CaCLR's β term remains inert across benchmarks. This rules out the possibility that CaCLR's failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88) between benchmarks confirm that per-language transfer difficulty is a property of the model's multilingual representations, not the benchmark.\n"
321	  },
322	  {
323	    "name": "INT8 Validation Ablation",
324	    "description": "INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout on 5% subset.\n",
325	    "results": {
326	      "int8_fp16_auroc_max_diff": 0.008,
327	      "int8_fp16_auroc_mean_diff": 0.003,
328	      "int8_fp16_ece_max_diff": 0.012,
329	      "int8_fp16_correlation_r": 0.997,
330	      "int8_fp16_rank_agreement_pct": 0.98,
331	      "distortion_significant": false
332	    },
333	    "tables": [
334	      {
335	        "name": "Table S3: INT8 vs FP16 Validation",
336	        "description": "Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank correlation). All differences within bootstrap CI. Conclusion: INT8 does not distort correctness signals.\n"
337	      }
338	    ],
339	    "figures": [],
340	    "analysis": "Straightforward validation that INT8 quantization doesn't affect conclusions. One paragraph in supplementary material with the table. Addresses anticipated reviewer concern #5.\n\n\nINT8 weight-only quantization preserves the vast majority of activation-space structure because (a) it quantizes weights, not activations — the internal representations used for probing are computed in higher precision; (b) 7B+ models are robust to INT8 quantization (well-established in the quantization literature); (c) correctness probes operate on high-dimensional representations (4096+ dims) where small per-dimension perturbations from quantization average out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that quantization shifts all scores by a near-constant offset without affecting ranking. This validation is necessary for reviewer reassurance but expected to be a non-issue.\n"
341	  },
342	  {
343	    "name": "CKA Cross-Lingual Representation Similarity",
344	    "description": "CKA (linear kernel) between English and each target language at every probed layer, both models. Correlate CKA with transfer AUROC.\n",
345	    "results": {
346	      "cka_en_zh_shallow_layer12_qwen": 0.88,
347	      "cka_en_zh_deep_layer72_qwen": 0.62,
348	      "cka_en_sw_shallow_layer12_qwen": 0.78,
349	      "cka_en_sw_deep_layer72_qwen": 0.38,
350	      "cka_median_shallow_across_langs": 0.84,
351	      "cka_median_deep_across_langs": 0.52,
352	      "cka_decrease_with_depth_significant": true,
353	      "cka_transfer_pearson_r_qwen": 0.62,
354	      "cka_transfer_pearson_r_llama": 0.54,
355	      "cka_transfer_pearson_r_pooled": 0.58,
356	      "cka_transfer_pearson_p": 1e-05,
357	      "cka_deep_high_resource_median": 0.6,
358	      "cka_deep_mid_resource_median": 0.48,
359	      "cka_deep_low_resource_median": 0.36,
360	      "mmd_transfer_pearson_r": 0.25,
361	      "mmd_explains_variance_pct": 6,
362	      "cka_explains_variance_pct": 34
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 11: CKA Similarity — Languages × Layers",
367	        "description": "Probed layers (rows) × 20 languages (columns, sorted by resource tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing with depth. Resource-tier banding visible. Both models shown.\n"
368	      },
369	      {
370	        "name": "Table 12: CKA vs MMD as Transfer Predictors",
371	        "description": "Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy. Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric > distributional as explanation.\n"
372	      }
373	    ],
374	    "figures": [],
375	    "analysis": "CKA analysis is the mechanistic backbone of the paper. It upgrades the contribution from \"we measured that transfer fails at deep layers\" to \"we explain WHY transfer fails — geometric misalignment increases with depth, and this misalignment type (rotation/scaling) is specifically not addressable by distributional matching (MMD).\" The CKA–transfer correlation (r=0.58) provides quantitative support, and the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical distinction that makes the negative CaCLR result theoretically interpretable rather than just empirically observed. This transforms the paper from a measurement study to one with mechanistic insight.\n\n\nCKA measures representational similarity including geometric structure (rotation, scaling), while MMD measures distributional distance (mean, variance, higher moments). CKA decreases with depth because deeper transformer layers specialize more for language-specific processing — the cross-lingual alignment enforced by shared vocabulary embeddings and early layers gradually gives way to language- specific feature extraction. The CKA–transfer correlation (r=0.58) is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming that representational geometry is a major (but not the only) factor in transfer success. The remaining variance comes from factors like probe quality, dataset difficulty distribution, and non-geometric aspects of the representation. Critically, CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer success — this is the key mechanistic finding. If cross-lingual misalignment were distributional (mean/covariance shift), MMD would predict transfer as well as or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that the misalignment is geometric (rotation/scaling of the entire representational space), not merely distributional. This directly explains why MMD-based CaCLR fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing a mechanistic explanation for why low-resource languages transfer worse — their deep-layer representations are more geometrically dissimilar from English.\n"
376	  },
377	  {
378	    "name": "Linear Projection Sensitivity Analysis",
379	    "description": "Vary parallel pairs (10, 20, 50, 100, 200) for linear projection. Both models × 5 layers × 20 languages.\n",
380	    "results": {
381	      "pairs_10_delta_auroc_median": 0.012,
382	      "pairs_20_delta_auroc_median": 0.022,
383	      "pairs_50_delta_auroc_median": 0.03,
384	      "pairs_100_delta_auroc_median": 0.035,
385	      "pairs_200_delta_auroc_median": 0.036,
386	      "saturation_knee_point": 70,
387	      "pairs_for_90pct_max_improvement": 55,
388	      "pairs_for_95pct_max_improvement": 85,
389	      "pairs_10_std_across_langs": 0.025,
390	      "pairs_50_std_across_langs": 0.012,
391	      "pairs_100_std_across_langs": 0.008,
392	      "saturation_consistent_across_models": true,
393	      "qwen_saturation_knee": 65,
394	      "llama_saturation_knee": 75
395	    },
396	    "tables": [
397	      {
398	        "name": "Table 13: Linear Projection — Sample Efficiency",
399	        "description": "Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear diminishing returns after 50 pairs.\n"
400	      }
401	    ],
402	    "figures": [],
403	    "analysis": "Linear projection's sample efficiency is the constructive complement to CaCLR's negative result. The message: you don't need MMD-based distributional matching (which doesn't work anyway) — you just need ~50-100 parallel pairs and a linear mapping. This is practically actionable and theoretically consistent with the geometric explanation (linear projection learns the rotation that MMD cannot). The learning curve figure — showing linear projection surpassing CaCLR at ~20 pairs — is one of the paper's most compelling visuals.\n\n\nLinear projection learns a rotation matrix mapping source-language representations to target-language space. The sample complexity for estimating a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because: (a) the effective dimensionality of the correctness-relevant subspace is much lower than the full representation dimensionality — the probe operates in a low-rank subspace; (b) parallel pairs provide direct supervision on the mapping, unlike distributional matching which uses indirect statistical signals. With 10 pairs, the mapping is underdetermined but captures the dominant rotation component (+1.2pp). By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture difference in knee points (65 vs 75) reflects that Llama 4's representations may require slightly more pairs to estimate the rotation due to its MoE routing introducing more heterogeneity. The practical implication is clear: ~50-100 parallel pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match or exceed CaCLR's entire training pipeline.\n"
404	  },
405	  {
406	    "name": "Probing Control Tasks (Hewitt & Liang 2019)",
407	    "description": "Train probes on randomly permuted labels at each layer. Selectivity analysis across layers and languages.\n",
408	    "results": {
409	      "control_auroc_en_median": 0.545,
410	      "control_auroc_en_range": [
411	        0.52,
412	        0.58
413	      ],
414	      "control_auroc_noneng_median": 0.54,
415	      "selectivity_en_median": 0.265,
416	      "selectivity_en_range": [
417	        0.18,
418	        0.31
419	      ],
420	      "selectivity_noneng_median_high_resource": 0.2,
421	      "selectivity_noneng_median_mid_resource": 0.16,
422	      "selectivity_noneng_median_low_resource": 0.1,
423	      "selectivity_min_across_all": 0.08,
424	      "selectivity_min_language": "sw",
425	      "selectivity_min_layer": "layer_4",
426	      "all_selectivities_positive": true,
427	      "pct_above_10pp": 0.88,
428	      "pct_above_10pp_high_resource": 0.95,
429	      "pct_above_10pp_low_resource": 0.7,
430	      "selectivity_peaks_at_mid_depth": true,
431	      "selectivity_peak_layer_pct_depth": 0.55
432	    },
433	    "tables": [
434	      {
435	        "name": "Table S4: Control Task Selectivity",
436	        "description": "Supplementary. Languages (rows, grouped by resource tier) × representative layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded: green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in selectivity.\n"
437	      }
438	    ],
439	    "figures": [],
440	    "analysis": "Control tasks validate that probe AUROC reflects genuine correctness signal for the large majority of settings (88% above 10pp). The resource-tier gradient in selectivity is a limitation to acknowledge: for low-resource languages, probe signal quality is weaker, and conclusions about transfer should be interpreted with this caveat. This doesn't undermine the paper's core claims (which are about the mechanism of transfer failure, not about achieving high probe quality in every language) but sets appropriate epistemic bounds.\n\n\nControl tasks with random labels test whether probe capacity (model expressiveness) alone can achieve high AUROC without genuine correctness signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms that logistic regression probes do not have sufficient capacity to memorize random label assignments in high-dimensional space — any AUROC above this baseline reflects genuine signal. English selectivity (median 0.265) is strong: the probe captures real correctness information 26.5pp above what capacity alone could achieve. Non-English selectivity decreases with resource tier because: (a) the correctness signal itself is weaker for languages with less pretraining data; (b) the cross-lingual transfer means probes must generalize from English-learned patterns, which is inherently harder for distant languages. Low-resource languages (sw, bn) show selectivity ~10pp, still positive but approaching the threshold where a reviewer might question signal quality. The 88% of language-layer combinations exceeding 10pp provides reasonable validation, but the 30% failure rate for low-resource languages at this threshold is a genuine limitation that the paper should acknowledge. Selectivity peaks at mid-depth (~55%) because shallow layers have weaker correctness signals (less processed) and very deep layers have stronger but more language-specific signals (high probe AUROC but also higher control AUROC due to richer features).\n"
441	  },
442	  {
443	    "name": "Gemma 4 31B Dense Pareto Frontier",
444	    "description": "Third architecture for camera-ready. 60 layers, dense, FP16. Full Pareto frontier, 20+ languages. Dense vs MoE contrast.\n",
445	    "results": {
446	      "en_best_auroc": 0.8,
447	      "en_best_layer": 45,
448	      "zs_transfer_auroc_median": 0.69,
449	      "best_transfer_layer": 33,
450	      "pareto_rho_per_lang_median": -0.58,
451	      "zs_langs_above_0p65": 12,
452	      "pareto_rho_smoother_than_moe": true,
453	      "pareto_rho_std_across_langs_gemma": 0.12,
454	      "pareto_rho_std_across_langs_qwen": 0.16,
455	      "pareto_rho_std_across_langs_llama": 0.15,
456	      "cka_depth_decline_steeper_dense": true,
457	      "linear_proj_delta_median": 0.033
458	    },
459	    "tables": [
460	      {
461	        "name": "Table CR1: Three-Architecture Pareto Comparison",
462	        "description": "Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense) × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.\n"
463	      }
464	    ],
465	    "figures": [],
466	    "analysis": "Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture- dependence evidence: MoE routing introduces heterogeneity that partially buffers against geometric misalignment at deep layers, while dense models show cleaner depth-dependent degradation. This doesn't change the paper's conclusions but provides a more compelling architectural contrast than two MoE models alone.\n\n\nGemma 4 31B Dense provides the critical dense-vs-MoE architectural contrast. As a dense model, every token passes through every layer (no routing), creating more uniform layer-to-layer transformations. This produces a smoother Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE models) because the depth-transfer tradeoff is more consistent without routing-induced heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense models show a cleaner monotonic decline in cross-lingual alignment with depth — MoE routing partially breaks this monotonicity by allowing some expert pathways to maintain cross-lingual features at deeper layers. CKA declines more steeply with depth in the dense model, confirming that MoE routing provides a modest buffer against geometric misalignment (different experts can specialize differently per language). English AUROC (0.80) is comparable to the larger MoE models despite smaller parameter count because the 31B dense architecture is parameter-efficient for representation quality. This is a P2 camera-ready experiment that strengthens the architecture-dependence claim from \"two MoE models differ moderately\" to \"dense vs MoE is a qualitatively distinct contrast.\"\n"
467	  },
468	  {
469	    "name": "Extended Language Coverage (50+ Languages)",
470	    "description": "Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele language sets.\n",
471	    "results": {
472	      "total_languages": 52,
473	      "zs_langs_above_0p65": 28,
474	      "zs_median_auroc_52lang": 0.66,
475	      "zs_auroc_range": [
476	        0.5,
477	        0.74
478	      ],
479	      "new_low_resource_langs_below_0p55": [
480	        "am",
481	        "my",
482	        "zu",
483	        "sn",
484	        "rw"
485	      ],
486	      "resource_tier_gradient_replicates": true,
487	      "pareto_rho_median_52lang": -0.49,
488	      "linear_proj_delta_median_52lang": 0.031,
489	      "tail_langs_below_0p55_count": 8,
490	      "tail_langs_above_0p70_count": 12
491	    },
492	    "tables": [
493	      {
494	        "name": "Table CR2: Extended Language Coverage — 52 Languages",
495	        "description": "Camera-ready. Full 52-language results sorted by zero-shot AUROC. Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100 AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65 (marginal), <0.55 (failed).\n"
496	      }
497	    ],
498	    "figures": [],
499	    "analysis": "Camera-ready extension. The 52-language analysis adds scale but the median-tier conclusion is clear: probe-based cross-lingual calibration works for a majority but not all languages, and the resource-tier gradient is the dominant predictor of success. This sets realistic expectations for practitioners and motivates future work on low-resource language probe training.\n\nExpanding to 52 languages adds many more low-resource and typologically diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated 20) because the additional languages are disproportionately low-resource. Five extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda) fall below 0.55, approaching chance performance — these languages have minimal pretraining representation in both models. The resource-tier gradient continues to hold and becomes even more pronounced with the extended tail. Pareto rho weakens slightly (-0.49) because many of the new languages show weak, noisy correlations due to low base probe quality. Linear projection improvement remains consistent (+3.1pp), confirming the geometric correction generalizes beyond the curated language set. The practical message: probe-based cross-lingual calibration is viable for ~28/52 languages (54%) without any target-language data, and linear projection extends this to ~35/52 (67%). The remaining ~17 languages need language-specific probes or alternative approaches.\n"
500	  }
501	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99c136ae-5794-4823-ac10-7a29c4c5130b",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "260402f9-f69d-47ae-9bb0-d994474792ee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Qwen3-235B-A22B Full Pareto Frontier\",\n    \"description\": \"Full Pareto frontier on Qwen3-235B-A22B (94 layers, MoE, INT8): 24 probed layers, 20 languages, 5 transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR). Per-language and global Spearman rho.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.81,\n      \"en_best_layer\": 72,\n      \"en_best_ece_raw\": 0.17,\n      \"en_best_ece_tempcal\": 0.065,\n      \"temp_scaling_T\": 5.8,\n      \"en_auroc_range\": [\n        0.58,\n        0.81\n      ],\n      \"en_auroc_50pct_depth_layer47\": 0.76,\n      \"zs_transfer_auroc_median_20lang_at_en_optimal\": 0.63,\n      \"zs_transfer_auroc_median_20lang_at_best_transfer_layer\": 0.7,\n      \"best_transfer_layer\": 48,\n      \"pareto_rho_global\": -0.58,\n      \"pareto_rho_per_lang_median\": -0.51,\n      \"pareto_rho_per_lang_range\": [\n        -0.78,\n        -0.21\n      ],\n      \"zs_langs_above_0p65\": 13,\n      \"zs_auroc_zh\": 0.74,\n      \"zs_auroc_es\": 0.73,\n      \"zs_auroc_fr\": 0.73,\n      \"zs_auroc_de\": 0.72,\n      \"zs_auroc_ar\": 0.7,\n      \"zs_auroc_hi\": 0.69,\n      \"zs_auroc_ru\": 0.71,\n      \"zs_auroc_ko\": 0.69,\n      \"zs_auroc_ja\": 0.7,\n      \"zs_auroc_pt\": 0.72,\n      \"zs_auroc_vi\": 0.68,\n      \"zs_auroc_tr\": 0.67,\n      \"zs_auroc_id\": 0.68,\n      \"zs_auroc_th\": 0.66,\n      \"zs_auroc_pl\": 0.69,\n      \"zs_auroc_uk\": 0.68,\n      \"zs_auroc_he\": 0.66,\n      \"zs_auroc_el\": 0.65,\n      \"zs_auroc_sw\": 0.58,\n      \"zs_auroc_bn\": 0.57,\n      \"mean_shift_delta_auroc_median\": 0.0,\n      \"linear_proj_delta_auroc_over_zs_median\": 0.035,\n      \"fewshot_25_delta_auroc_over_zs_median\": 0.025,\n      \"fewshot_100_delta_auroc_over_zs_median\": 0.045,\n      \"ece_reduction_vs_temp_scaling_median\": 0.008\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Qwen3-235B-A22B Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer\",\n        \"description\": \"24 probed layers (rows) × 20 languages + English (columns). Cells show AUROC. Bold: best layer per language. Gray shading: layers within 1pp of best. Bottom rows: global and per-language Spearman rho with 95% bootstrap CI. Key pattern: English-optimal layer (72) ≠ transfer-optimal layer (48) for most languages. High-resource languages show flatter profiles; low-resource show steeper drop-off at deep layers.\\n\"\n      },\n      {\n        \"name\": \"Table 2: Qwen3-235B-A22B Transfer Method Comparison at Fixed Layers\",\n        \"description\": \"5 transfer methods (columns) × 20 languages (rows), evaluated at two fixed layers (50% depth = layer 47, EN-optimal = layer 72) plus per-language oracle. Shows AUROC and ΔAUROC vs zero-shot. Bootstrap 95% CI and paired permutation test p-values. Cohen's d for each method vs zero-shot baseline.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"The Pareto frontier replicates on this large MoE model but with moderate per-language rho (-0.51 median). The architecture-dependent shape is visible: MoE routing creates more variable layer representations, so the depth-transfer tradeoff is less smooth than in a dense model. The key finding is that 13/20 languages achieve usable zero-shot transfer (>0.65 AUROC) at optimal layers, validating the approach for most languages. The 7 languages below threshold cluster in low-resource (sw, bn) and morphologically distant categories (th, he at marginal 0.66). Linear projection provides the most consistent improvement across languages.\\n\\n\\nQwen3-235B-A22B is a 94-layer MoE model — significantly deeper than the 7B MVP. The English best AUROC rises to 0.81 because the larger model encodes stronger correctness signals (more parameters, more knowledge). The best English layer is at ~76% depth (layer 72), consistent with the MVP pattern where correctness peaks in deep-but-not-final layers. The Pareto frontier is present but rho is moderate (-0.51 median per-language) because: (a) the MoE routing creates more heterogeneous layer representations, reducing the clean monotonic depth-degradation pattern seen in dense models; (b) some languages (especially high-resource zh/es/fr) have strong multilingual representations even at deeper layers due to extensive pretraining data, attenuating the negative correlation. The per-language rho range [-0.78, -0.21] reflects that low-resource languages (sw, bn) show stronger negative correlation (their representations diverge from English more sharply at depth) while high-resource languages show weaker correlation (they maintain reasonable alignment throughout). 13/20 languages cross 0.65 AUROC — most European and major Asian languages transfer adequately at optimal layers, but sw (0.58) and bn (0.57) remain below threshold due to limited pretraining representation for these languages. Mean-shift produces exactly zero AUROC change (rank-invariance proof holds), confirming the MVP finding. Linear projection (+3.5pp) outperforms few-shot-25 (+2.5pp) because it directly corrects geometric misalignment rather than relying on a small labeled sample. ECE improvement over temperature scaling is marginal (0.8pp) because probe-based calibration and temperature scaling address different aspects — at the median tier, probes don't provide much additional calibration beyond what temperature scaling already captures.\\n\"\n  },\n  {\n    \"name\": \"Llama 4 Scout Full Pareto Frontier\",\n    \"description\": \"Full Pareto frontier on Llama 4 Scout (48 layers, MoE, INT8): 12 probed layers, 20 languages, 5 transfer conditions. Per-language Spearman rho.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.79,\n      \"en_best_layer\": 36,\n      \"en_best_ece_raw\": 0.19,\n      \"en_best_ece_tempcal\": 0.07,\n      \"temp_scaling_T\": 6.0,\n      \"en_auroc_range\": [\n        0.6,\n        0.79\n      ],\n      \"en_auroc_50pct_depth_layer24\": 0.74,\n      \"zs_transfer_auroc_median_20lang_at_en_optimal\": 0.62,\n      \"zs_transfer_auroc_median_20lang_at_best_transfer_layer\": 0.68,\n      \"best_transfer_layer\": 24,\n      \"pareto_rho_global\": -0.62,\n      \"pareto_rho_per_lang_median\": -0.54,\n      \"pareto_rho_per_lang_range\": [\n        -0.82,\n        -0.28\n      ],\n      \"zs_langs_above_0p65\": 11,\n      \"zs_auroc_zh\": 0.72,\n      \"zs_auroc_es\": 0.71,\n      \"zs_auroc_fr\": 0.71,\n      \"zs_auroc_de\": 0.7,\n      \"zs_auroc_ar\": 0.68,\n      \"zs_auroc_hi\": 0.67,\n      \"zs_auroc_ru\": 0.69,\n      \"zs_auroc_ko\": 0.66,\n      \"zs_auroc_ja\": 0.67,\n      \"zs_auroc_pt\": 0.7,\n      \"zs_auroc_vi\": 0.65,\n      \"zs_auroc_tr\": 0.64,\n      \"zs_auroc_id\": 0.66,\n      \"zs_auroc_th\": 0.63,\n      \"zs_auroc_pl\": 0.67,\n      \"zs_auroc_uk\": 0.65,\n      \"zs_auroc_he\": 0.63,\n      \"zs_auroc_el\": 0.62,\n      \"zs_auroc_sw\": 0.55,\n      \"zs_auroc_bn\": 0.54,\n      \"mean_shift_delta_auroc_median\": 0.0,\n      \"linear_proj_delta_auroc_over_zs_median\": 0.032,\n      \"fewshot_25_delta_auroc_over_zs_median\": 0.022,\n      \"fewshot_100_delta_auroc_over_zs_median\": 0.04,\n      \"ece_reduction_vs_temp_scaling_median\": 0.005\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Llama 4 Scout Pareto Frontier — Zero-Shot Transfer AUROC by Language × Layer\",\n        \"description\": \"12 probed layers × 20 languages + English. Same format as Table 1. Key contrast with Qwen3: steeper Pareto drop-off, fewer layers in the Pareto-optimal set due to coarser layer sampling.\\n\"\n      },\n      {\n        \"name\": \"Table 4: Llama 4 Scout Transfer Method Comparison\",\n        \"description\": \"Same format as Table 2. Llama 4 Scout results. Key finding: linear projection improvement (+3.2pp) is comparable to Qwen3, suggesting the geometric correction transfers across architectures.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Llama 4 Scout confirms the Pareto frontier generalizes across architectures. The steeper negative rho (-0.54) vs Qwen3 (-0.51) is a moderate difference that supports the architecture-dependence claim but is not dramatic enough to call it a strong architectural contrast. This is the median-tier signature: same qualitative finding, quantitatively less distinct than ideal. Both models agree on the key implication: mid-depth layers are the right operating point for cross-lingual transfer.\\n\\n\\nLlama 4 Scout has fewer layers (48 vs 94) and a different MoE architecture from Qwen3. The English best AUROC is slightly lower (0.79 vs 0.81) reflecting somewhat weaker correctness encoding in a shallower architecture. The Pareto rho is slightly stronger negative (-0.54 vs -0.51) because with fewer layers, each layer step represents a larger proportional depth change, making the depth-transfer tradeoff more pronounced. The best transfer layer at 50% depth (layer 24) is consistent with the pattern that mid-depth layers balance English quality and cross-lingual alignment. 11/20 languages cross 0.65, slightly fewer than Qwen3 — Llama 4's multilingual pretraining may be less balanced, particularly for mid-resource languages like tr (0.64) and vi (0.65) that were marginal on Qwen3. Low-resource sw (0.55) and bn (0.54) are again the weakest, confirming this is a fundamental limitation of pretraining representation rather than architecture-specific. The same qualitative Pareto pattern holds but the quantitative frontier shape differs — the drop-off from English-optimal to transfer-optimal is steeper on Llama 4, confirming architecture-dependence without requiring architecture-specific tuning as a paper claim.\\n\"\n  },\n  {\n    \"name\": \"CaCLR Implementation and Comparative Evaluation\",\n    \"description\": \"CaCLR probe training with L_BCE + α·L_SB-ECE + β·L_consistency (MMD). α sweep (0.01–10.0), β sweep (0.001–1.0) across 3 OOM. Full comparison vs zero-shot, mean-shift, linear projection, few-shot on both models × 20 langs.\\n\",\n    \"results\": {\n      \"alpha_optimal\": 0.5,\n      \"alpha_only_en_auroc_at_en_optimal_layer_qwen\": 0.805,\n      \"alpha_only_en_ece_at_en_optimal_layer_qwen\": 0.058,\n      \"alpha_only_zs_median_auroc_qwen\": 0.695,\n      \"alpha_only_zs_median_auroc_llama\": 0.675,\n      \"beta_0p001_delta_auroc_over_alpha_only_median\": 0.002,\n      \"beta_0p01_delta_auroc_over_alpha_only_median\": 0.001,\n      \"beta_0p1_delta_auroc_over_alpha_only_median\": -0.001,\n      \"beta_1p0_delta_auroc_over_alpha_only_median\": -0.003,\n      \"beta_sweep_max_delta_auroc\": 0.003,\n      \"beta_sweep_significant_at_p05\": false,\n      \"caclr_full_delta_auroc_over_zeroshot_median\": 0.012,\n      \"caclr_full_delta_auroc_over_zeroshot_range\": [\n        -0.005,\n        0.035\n      ],\n      \"caclr_vs_linear_proj_delta_median\": -0.023,\n      \"caclr_vs_fewshot100_delta_median\": -0.033,\n      \"linear_proj_delta_auroc_over_zs_median_qwen\": 0.035,\n      \"linear_proj_delta_auroc_over_zs_median_llama\": 0.032,\n      \"fewshot_25_delta_auroc_over_zs_median\": 0.024,\n      \"fewshot_100_delta_auroc_over_zs_median\": 0.043,\n      \"mean_shift_delta_auroc_median\": 0.0,\n      \"method_ranking\": [\n        \"few-shot-100\",\n        \"linear-projection\",\n        \"few-shot-25\",\n        \"CaCLR-full\",\n        \"CaCLR-α-only\",\n        \"zero-shot\",\n        \"mean-shift\"\n      ],\n      \"caclr_beta_delta_high_resource\": 0.004,\n      \"caclr_beta_delta_mid_resource\": 0.0,\n      \"caclr_beta_delta_low_resource\": -0.002,\n      \"caclr_beta_vs_alpha_only_paired_perm_p\": 0.42,\n      \"caclr_beta_vs_alpha_only_cohens_d\": 0.08,\n      \"linear_proj_vs_zeroshot_paired_perm_p\": 0.001,\n      \"linear_proj_vs_zeroshot_cohens_d\": 0.55\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: β Sensitivity Sweep — ΔAUROC over α-only baseline\",\n        \"description\": \"β values (rows: 0, 0.001, 0.01, 0.1, 1.0) × summary statistics (columns: median ΔAUROC, mean, std, min, max, # languages improved, paired permutation p-value, Cohen's d). Both models shown side-by-side. Key: no β value achieves p < 0.05 or d > 0.2 — consistency loss is definitively inert.\\n\"\n      },\n      {\n        \"name\": \"Table 6: Transfer Method Comparison — Median AUROC across 20 Languages\",\n        \"description\": \"Methods (rows: zero-shot, mean-shift, CaCLR-α-only, CaCLR-full, linear-projection, few-shot-25, few-shot-100) × Models (columns: Qwen3, Llama 4) × 2 fixed layers + per-language oracle. ΔAUROC vs zero-shot with bootstrap 95% CI. Ranking is consistent across models. Linear projection and few-shot clearly dominate.\\n\"\n      },\n      {\n        \"name\": \"Table 7: CaCLR β Effect by Resource Tier\",\n        \"description\": \"Resource tier (rows: HIGH, MID, LOW) × β levels. Shows that inertness is consistent across tiers — not a power issue with low-resource languages but a fundamental limitation of distributional matching.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CaCLR's β inertness is the paper's centerpiece negative result. The analysis proceeds in three steps: (1) empirically, β has negligible effect (d=0.08, p=0.42) across 3 OOM and both architectures; (2) mechanistically, CKA analysis (plan_011) reveals that cross-lingual misalignment at deeper layers is geometric (rotation/scaling) rather than distributional (mean/covariance shift); (3) linear projection's success (+3.5pp) confirms the geometric explanation — it succeeds precisely because it learns the rotation that MMD cannot represent. This three-part argument closes the distributional-matching path with both theory and evidence. The α-only variant retains value as a calibration regularizer — it improves ECE without hurting AUROC.\\n\\n\\nThe β (consistency loss) is inert because MMD-based distributional matching fundamentally cannot correct the geometric misalignment that CKA reveals. MMD penalizes differences in mean embeddings and kernel-space distributional moments — it can align marginal distributions but cannot learn the rotation of the correctness direction across language subspaces. At low β (0.001), the MMD signal is too weak to affect optimization. At medium β (0.01–0.1), the gradient signal exists but points in the wrong direction — it pushes overall distributional alignment without specifically aligning the correctness-relevant subspace. At high β (1.0), the MMD term dominates and slightly hurts English AUROC by distorting the probe weights. The α-only (SB-ECE) variant provides small but real calibration improvement (better ECE) because smooth-binned ECE regularization is a well-motivated objective that doesn't require cross-lingual alignment. The total CaCLR improvement over zero-shot (+1.2pp) comes entirely from the α term's calibration regularization, not from cross-lingual consistency. Cohen's d = 0.08 for β effect is negligible. In contrast, linear projection achieves +3.5pp because it directly estimates and corrects the rotation via a learned affine transformation on parallel pairs. Few-shot-100 achieves +4.3pp because it sidesteps alignment entirely by training on target-language labels. This ranking — few-shot > linear-projection > CaCLR ≈ α-only > zero-shot > mean-shift — is the key empirical result that the geometric explanation predicts.\\n\"\n  },\n  {\n    \"name\": \"Difficulty-Controlled Decomposition Ablation\",\n    \"description\": \"IRT difficulty probes, project out difficulty direction, retrain correctness probes on residuals. 10 languages × 8 layers per model. Random-direction control.\\n\",\n    \"results\": {\n      \"difficulty_probe_r2_en_median_across_layers\": 0.42,\n      \"difficulty_probe_r2_range\": [\n        0.25,\n        0.55\n      ],\n      \"decomposition_transfer_delta_median\": 0.012,\n      \"decomposition_transfer_delta_range\": [\n        -0.01,\n        0.035\n      ],\n      \"pct_combos_improved\": 0.65,\n      \"pct_combos_improved_by_tier_high\": 0.72,\n      \"pct_combos_improved_by_tier_mid\": 0.65,\n      \"pct_combos_improved_by_tier_low\": 0.53,\n      \"improvement_stronger_at_deep_layers\": true,\n      \"improvement_at_shallow_layers_pct\": 0.5,\n      \"improvement_at_deep_layers_pct\": 0.78,\n      \"random_direction_delta_median\": 0.003,\n      \"random_direction_delta_significant\": false,\n      \"difficulty_correctness_cosine_median\": 0.18,\n      \"difficulty_correctness_cosine_range\": [\n        0.08,\n        0.3\n      ],\n      \"decomposition_vs_baseline_paired_p\": 0.03,\n      \"decomposition_cohens_d\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Decomposition Results — 10 Languages × 8 Layers\",\n        \"description\": \"Heatmap table: languages (rows) × layers (columns). Cells show ΔAUROC after difficulty removal. Green: improved (>0.5pp), white: unchanged, red: degraded. Marginal summaries: % improved per language, per layer. Shows concentration of improvement at deep layers and high-resource languages.\\n\"\n      },\n      {\n        \"name\": \"Table 9: Decomposition vs Random Direction Control\",\n        \"description\": \"Comparison: difficulty projection vs random projection vs no projection. Median ΔAUROC, bootstrap CI, paired test. Confirms difficulty projection specifically — not arbitrary dimensionality reduction — drives improvement.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Decomposition provides supporting evidence for the geometric misalignment narrative. The fact that difficulty removal helps more at deep layers aligns with the CKA finding — at depth, the capability-specific component (which is geometrically misaligned across languages) drives transfer failure, and removing the shared difficulty component isolates this effect. However, the partial success rate (65%) and modest effect size (d=0.28) keep this as supporting analysis rather than a standalone claim. The finding is prescriptive: researchers attempting cross-lingual probe transfer should first assess whether difficulty confounding explains their transfer gaps — in ~65% of cases, it partially does.\\n\\n\\nDecomposition works but is partial because the difficulty-capability separation is not clean. The difficulty direction (IRT-derived) captures ~42% variance in human difficulty scores (R²) — reasonable but not perfect, meaning the projection leaves residual difficulty signal mixed with capability. At deep layers, removing difficulty helps more often (78% of combos) because the capability-specific component dominates transfer degradation there — once you remove the shared difficulty signal, the residual is more language-specific and harder to transfer. At shallow layers, the improvement rate drops to ~50% (near chance) because both difficulty and capability signals are more entangled and less linearly separable. The 65% overall improvement rate is genuine but not universal — it demonstrates the decomposition is prescriptive for about two-thirds of settings. The random-direction control (median +0.3pp, not significant) confirms this isn't a dimensionality-reduction artifact. Low-resource languages show weaker improvement (53%) because their correctness probes are noisier to begin with, and the difficulty projection may remove some of the limited signal they have. The modest Cohen's d (0.28) reflects that improvements are real but small — this is a supporting analytical result, not a standalone method contribution.\\n\"\n  },\n  {\n    \"name\": \"Cross-Lingual Orthogonality Analysis\",\n    \"description\": \"Verbalized confidence direction extraction, cosine similarity with correctness direction. 20 languages × 2 architectures. Resource-tier and family analysis.\\n\",\n    \"results\": {\n      \"en_cosine_qwen\": 0.035,\n      \"en_cosine_llama\": 0.038,\n      \"cosine_median_across_langs_qwen\": 0.055,\n      \"cosine_median_across_langs_llama\": 0.06,\n      \"cosine_max_across_langs\": 0.1,\n      \"cosine_max_language\": \"sw\",\n      \"cosine_range\": [\n        0.02,\n        0.1\n      ],\n      \"cosine_median_high_resource\": 0.04,\n      \"cosine_median_mid_resource\": 0.06,\n      \"cosine_median_low_resource\": 0.085,\n      \"cosine_variance_high\": 0.0003,\n      \"cosine_variance_mid\": 0.0008,\n      \"cosine_variance_low\": 0.0018,\n      \"all_langs_below_threshold\": true,\n      \"cosine_vs_resource_spearman_rho\": 0.52,\n      \"cosine_vs_resource_p\": 0.018\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Correctness–Confidence Cosine Similarity Across Languages\",\n        \"description\": \"20 languages (rows, grouped by resource tier) × 2 architectures (column pairs). Each cell: cosine similarity ± bootstrap 95% CI. Bottom: tier medians and Spearman correlation with log(pretraining data estimate). All values < 0.12.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Orthogonality holds universally (max 0.10 < 0.12 threshold) but with a resource- tier gradient that is novel relative to Miao & Ungar's English-only finding. This extends their claim to multilingual settings with a nuance: the structural separation is slightly weaker for low-resource languages, though never approaching a level that would make output-based calibration viable. This supports the paper's broader argument that probe-based calibration is the right paradigm for all languages, but the cross-lingual transfer challenge is the bottleneck — not the underlying signal quality.\\n\\n\\nOrthogonality persists across languages because the separation between correctness and verbalized confidence is a structural property of how transformers process MCQA — the model's internal \\\"do I know this?\\\" signal (correctness) and its verbalized \\\"how confident am I?\\\" output occupy orthogonal subspaces by design (the former is a representation-level property, the latter is optimized during RLHF/instruction-tuning for human-readable outputs). The English cosine (~0.035- 0.038) replicates Miao & Ungar (2026). Non-English cosines are slightly higher (median 0.055-0.060) because: (a) non-English confidence verbalization is noisier (models are less calibrated in non-English expression of uncertainty); (b) the confidence probe may capture some language-switching signal that correlates weakly with correctness (lower-resource languages trigger more uncertain generation behavior). The max cosine at 0.10 (sw) still satisfies the orthogonality threshold (<0.12) but shows more variance — Swahili's limited pretraining data means both probes are noisier, and noise correlations inflate apparent cosine. The resource- tier gradient (rho=0.52, p=0.018) is a novel finding: orthogonality is stronger (lower cosine) for high-resource languages, suggesting that abundant pretraining data helps separate correctness from confidence representations. However, even the worst case (0.10) is far from the ~0.5+ that would indicate meaningful alignment, confirming that output-based calibration is structurally limited across all languages.\\n\"\n  },\n  {\n    \"name\": \"Probe Complexity Comparison\",\n    \"description\": \"Logistic regression vs 2-layer MLP at each probed layer for both models. English accuracy, cross-lingual transfer degradation, calibration quality.\\n\",\n    \"results\": {\n      \"logreg_en_best_auroc_qwen\": 0.81,\n      \"mlp_en_best_auroc_qwen\": 0.835,\n      \"logreg_en_best_auroc_llama\": 0.79,\n      \"mlp_en_best_auroc_llama\": 0.815,\n      \"logreg_zs_median_qwen\": 0.7,\n      \"mlp_zs_median_qwen\": 0.665,\n      \"logreg_zs_median_llama\": 0.68,\n      \"mlp_zs_median_llama\": 0.645,\n      \"logreg_transfer_gap\": 0.11,\n      \"mlp_transfer_gap\": 0.17,\n      \"logreg_ece_median\": 0.068,\n      \"mlp_ece_median\": 0.075,\n      \"mlp_advantage_en_deep_layers\": 0.03,\n      \"mlp_advantage_en_shallow_layers\": 0.01,\n      \"logreg_better_transfer_pct_langs\": 0.8\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: Probe Complexity — English AUROC and Transfer Gap by Layer\",\n        \"description\": \"Supplementary table. Layers (rows) × (LogReg EN, MLP EN, LogReg ZS-median, MLP ZS-median, LogReg gap, MLP gap) for each model. Shows MLP's higher EN AUROC comes at cost of larger transfer gap. Gap difference increases with depth.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"This experiment justifies the methodological choice of logistic regression probes and provides additional evidence for the geometric/linear framing. If the correctness signal were deeply nonlinear, MLP's advantage would transfer — the fact that it doesn't confirms that the transferable component is linear. Goes in supplementary material as a methodological validation.\\n\\n\\nMLP probes achieve ~2.5pp higher English AUROC because they can capture nonlinear interactions in the representation — the correctness signal has a small nonlinear component that logistic regression misses. However, this nonlinear component is language-specific (learned from English data, doesn't generalize), so MLP probes show 6pp larger transfer gap than logistic regression. The MLP essentially overfits to English-specific nonlinearities in the correctness representation. This confirms the hypothesis that linear probes transfer better cross-lingually — the linear component of the correctness signal is more universal across languages, while nonlinear components are language-specific. The MLP advantage is concentrated at deep layers (+3pp at deep vs +1pp at shallow) because deeper representations have more complex, language-specific structure for the MLP to exploit. 80% of languages see better transfer with logistic regression, with the exceptions being high- resource languages (zh, es) where the MLP's nonlinear component partially transfers due to shared pretraining features. This result justifies the paper's focus on logistic regression probes and reinforces the geometric (linear) framing.\\n\"\n  },\n  {\n    \"name\": \"Additional Benchmark Evaluation (Belebele + MMLU-ProX)\",\n    \"description\": \"Evaluate best probes + CaCLR on Belebele and MMLU-ProX (20 languages each). Validates generalization beyond GlobalMMLU.\\n\",\n    \"results\": {\n      \"belebele_en_best_auroc_qwen\": 0.78,\n      \"belebele_zs_median_qwen\": 0.68,\n      \"belebele_pareto_rho_median\": -0.48,\n      \"belebele_linear_proj_delta\": 0.03,\n      \"belebele_caclr_beta_delta\": 0.003,\n      \"mmlupx_en_best_auroc_qwen\": 0.82,\n      \"mmlupx_zs_median_qwen\": 0.69,\n      \"mmlupx_pareto_rho_median\": -0.5,\n      \"mmlupx_linear_proj_delta\": 0.033,\n      \"mmlupx_caclr_beta_delta\": 0.002,\n      \"auroc_rank_correlation_globalmmlu_vs_belebele\": 0.82,\n      \"auroc_rank_correlation_globalmmlu_vs_mmlupx\": 0.88,\n      \"method_ranking_consistent_across_benchmarks\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S2: Cross-Benchmark Generalization\",\n        \"description\": \"Supplementary. Benchmarks (rows: GlobalMMLU, Belebele, MMLU-ProX) × key metrics (EN AUROC, ZS median, Pareto rho, linear-proj Δ, CaCLR-β Δ). Shows consistent patterns across benchmarks. Rank correlation between per-language AUROCs.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Benchmark generalization confirms all findings are not artifacts of GlobalMMLU. The consistent method ranking across three benchmarks strengthens the negative result — CaCLR's β inertness is a fundamental property of distributional matching vs geometric misalignment, not a benchmark-specific failure. Goes in supplementary or a short main-text paragraph.\\n\\n\\nBelebele is a reading comprehension benchmark — fundamentally different from MCQA knowledge testing. The correctness signal is still present (models either comprehend or don't) but Belebele's English AUROC is slightly lower (0.78 vs 0.81) because reading comprehension correctness is less cleanly encoded than factual knowledge correctness. The Pareto rho is slightly weaker (-0.48) because Belebele's parallel passages provide more uniform cross-lingual signal than GlobalMMLU's diverse topics. MMLU-ProX, being closer to GlobalMMLU in format, shows more similar results (0.82 EN AUROC, -0.50 rho). The key finding is that method rankings are consistent — linear projection still outperforms CaCLR, and CaCLR's β term remains inert across benchmarks. This rules out the possibility that CaCLR's failure is GlobalMMLU-specific. The high rank correlations (0.82–0.88) between benchmarks confirm that per-language transfer difficulty is a property of the model's multilingual representations, not the benchmark.\\n\"\n  },\n  {\n    \"name\": \"INT8 Validation Ablation\",\n    \"description\": \"INT8 vs FP16 comparison at 5 representative layers for Llama 4 Scout on 5% subset.\\n\",\n    \"results\": {\n      \"int8_fp16_auroc_max_diff\": 0.008,\n      \"int8_fp16_auroc_mean_diff\": 0.003,\n      \"int8_fp16_ece_max_diff\": 0.012,\n      \"int8_fp16_correlation_r\": 0.997,\n      \"int8_fp16_rank_agreement_pct\": 0.98,\n      \"distortion_significant\": false\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S3: INT8 vs FP16 Validation\",\n        \"description\": \"Supplementary. 5 layers × metrics (INT8 AUROC, FP16 AUROC, Δ, rank correlation). All differences within bootstrap CI. Conclusion: INT8 does not distort correctness signals.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Straightforward validation that INT8 quantization doesn't affect conclusions. One paragraph in supplementary material with the table. Addresses anticipated reviewer concern #5.\\n\\n\\nINT8 weight-only quantization preserves the vast majority of activation-space structure because (a) it quantizes weights, not activations — the internal representations used for probing are computed in higher precision; (b) 7B+ models are robust to INT8 quantization (well-established in the quantization literature); (c) correctness probes operate on high-dimensional representations (4096+ dims) where small per-dimension perturbations from quantization average out. The max AUROC difference of 0.8pp across any layer is within bootstrap confidence intervals. The 0.997 correlation between INT8 and FP16 probe scores confirms that quantization shifts all scores by a near-constant offset without affecting ranking. This validation is necessary for reviewer reassurance but expected to be a non-issue.\\n\"\n  },\n  {\n    \"name\": \"CKA Cross-Lingual Representation Similarity\",\n    \"description\": \"CKA (linear kernel) between English and each target language at every probed layer, both models. Correlate CKA with transfer AUROC.\\n\",\n    \"results\": {\n      \"cka_en_zh_shallow_layer12_qwen\": 0.88,\n      \"cka_en_zh_deep_layer72_qwen\": 0.62,\n      \"cka_en_sw_shallow_layer12_qwen\": 0.78,\n      \"cka_en_sw_deep_layer72_qwen\": 0.38,\n      \"cka_median_shallow_across_langs\": 0.84,\n      \"cka_median_deep_across_langs\": 0.52,\n      \"cka_decrease_with_depth_significant\": true,\n      \"cka_transfer_pearson_r_qwen\": 0.62,\n      \"cka_transfer_pearson_r_llama\": 0.54,\n      \"cka_transfer_pearson_r_pooled\": 0.58,\n      \"cka_transfer_pearson_p\": 1e-05,\n      \"cka_deep_high_resource_median\": 0.6,\n      \"cka_deep_mid_resource_median\": 0.48,\n      \"cka_deep_low_resource_median\": 0.36,\n      \"mmd_transfer_pearson_r\": 0.25,\n      \"mmd_explains_variance_pct\": 6,\n      \"cka_explains_variance_pct\": 34\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: CKA Similarity — Languages × Layers\",\n        \"description\": \"Probed layers (rows) × 20 languages (columns, sorted by resource tier). Cells: CKA values. Clear gradient: high CKA at shallow layers, decreasing with depth. Resource-tier banding visible. Both models shown.\\n\"\n      },\n      {\n        \"name\": \"Table 12: CKA vs MMD as Transfer Predictors\",\n        \"description\": \"Predictor comparison: CKA linear, CKA RBF, MMD, H-divergence proxy. Columns: Pearson r, R², p-value. CKA linear clearly dominant. Demonstrates geometric > distributional as explanation.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CKA analysis is the mechanistic backbone of the paper. It upgrades the contribution from \\\"we measured that transfer fails at deep layers\\\" to \\\"we explain WHY transfer fails — geometric misalignment increases with depth, and this misalignment type (rotation/scaling) is specifically not addressable by distributional matching (MMD).\\\" The CKA–transfer correlation (r=0.58) provides quantitative support, and the CKA vs MMD comparison (34% vs 6% variance explained) provides the critical distinction that makes the negative CaCLR result theoretically interpretable rather than just empirically observed. This transforms the paper from a measurement study to one with mechanistic insight.\\n\\n\\nCKA measures representational similarity including geometric structure (rotation, scaling), while MMD measures distributional distance (mean, variance, higher moments). CKA decreases with depth because deeper transformer layers specialize more for language-specific processing — the cross-lingual alignment enforced by shared vocabulary embeddings and early layers gradually gives way to language- specific feature extraction. The CKA–transfer correlation (r=0.58) is moderate- to-strong: it explains 34% of variance in transfer AUROC, confirming that representational geometry is a major (but not the only) factor in transfer success. The remaining variance comes from factors like probe quality, dataset difficulty distribution, and non-geometric aspects of the representation. Critically, CKA (r=0.58) substantially outpredicts MMD (r=0.25) as a predictor of transfer success — this is the key mechanistic finding. If cross-lingual misalignment were distributional (mean/covariance shift), MMD would predict transfer as well as or better than CKA. The fact that CKA is 2.3× more predictive demonstrates that the misalignment is geometric (rotation/scaling of the entire representational space), not merely distributional. This directly explains why MMD-based CaCLR fails: it optimizes the wrong measure of alignment. The resource-tier CKA gradient (0.60 > 0.48 > 0.36 at deep layers) mirrors the transfer AUROC gradient, providing a mechanistic explanation for why low-resource languages transfer worse — their deep-layer representations are more geometrically dissimilar from English.\\n\"\n  },\n  {\n    \"name\": \"Linear Projection Sensitivity Analysis\",\n    \"description\": \"Vary parallel pairs (10, 20, 50, 100, 200) for linear projection. Both models × 5 layers × 20 languages.\\n\",\n    \"results\": {\n      \"pairs_10_delta_auroc_median\": 0.012,\n      \"pairs_20_delta_auroc_median\": 0.022,\n      \"pairs_50_delta_auroc_median\": 0.03,\n      \"pairs_100_delta_auroc_median\": 0.035,\n      \"pairs_200_delta_auroc_median\": 0.036,\n      \"saturation_knee_point\": 70,\n      \"pairs_for_90pct_max_improvement\": 55,\n      \"pairs_for_95pct_max_improvement\": 85,\n      \"pairs_10_std_across_langs\": 0.025,\n      \"pairs_50_std_across_langs\": 0.012,\n      \"pairs_100_std_across_langs\": 0.008,\n      \"saturation_consistent_across_models\": true,\n      \"qwen_saturation_knee\": 65,\n      \"llama_saturation_knee\": 75\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 13: Linear Projection — Sample Efficiency\",\n        \"description\": \"Pair counts (rows: 10, 20, 50, 100, 200) × summary statistics (median ΔAUROC, mean, std, min, max, % languages improved). Both models. Shows clear diminishing returns after 50 pairs.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Linear projection's sample efficiency is the constructive complement to CaCLR's negative result. The message: you don't need MMD-based distributional matching (which doesn't work anyway) — you just need ~50-100 parallel pairs and a linear mapping. This is practically actionable and theoretically consistent with the geometric explanation (linear projection learns the rotation that MMD cannot). The learning curve figure — showing linear projection surpassing CaCLR at ~20 pairs — is one of the paper's most compelling visuals.\\n\\n\\nLinear projection learns a rotation matrix mapping source-language representations to target-language space. The sample complexity for estimating a linear mapping in high-dimensional space (4096+ dims) is surprisingly low because: (a) the effective dimensionality of the correctness-relevant subspace is much lower than the full representation dimensionality — the probe operates in a low-rank subspace; (b) parallel pairs provide direct supervision on the mapping, unlike distributional matching which uses indirect statistical signals. With 10 pairs, the mapping is underdetermined but captures the dominant rotation component (+1.2pp). By 50 pairs, 90% of the achievable improvement is captured as the major rotation/scaling axes are identified. The knee point at ~70 pairs and saturation by 100 pairs is consistent with the cross-lingual alignment literature (MUSE, VecMap) where bilingual dictionaries of 50–100 entries suffice for word-level alignment. The slight architecture difference in knee points (65 vs 75) reflects that Llama 4's representations may require slightly more pairs to estimate the rotation due to its MoE routing introducing more heterogeneity. The practical implication is clear: ~50-100 parallel pairs (trivially obtainable from GlobalMMLU train split) are sufficient to match or exceed CaCLR's entire training pipeline.\\n\"\n  },\n  {\n    \"name\": \"Probing Control Tasks (Hewitt & Liang 2019)\",\n    \"description\": \"Train probes on randomly permuted labels at each layer. Selectivity analysis across layers and languages.\\n\",\n    \"results\": {\n      \"control_auroc_en_median\": 0.545,\n      \"control_auroc_en_range\": [\n        0.52,\n        0.58\n      ],\n      \"control_auroc_noneng_median\": 0.54,\n      \"selectivity_en_median\": 0.265,\n      \"selectivity_en_range\": [\n        0.18,\n        0.31\n      ],\n      \"selectivity_noneng_median_high_resource\": 0.2,\n      \"selectivity_noneng_median_mid_resource\": 0.16,\n      \"selectivity_noneng_median_low_resource\": 0.1,\n      \"selectivity_min_across_all\": 0.08,\n      \"selectivity_min_language\": \"sw\",\n      \"selectivity_min_layer\": \"layer_4\",\n      \"all_selectivities_positive\": true,\n      \"pct_above_10pp\": 0.88,\n      \"pct_above_10pp_high_resource\": 0.95,\n      \"pct_above_10pp_low_resource\": 0.7,\n      \"selectivity_peaks_at_mid_depth\": true,\n      \"selectivity_peak_layer_pct_depth\": 0.55\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S4: Control Task Selectivity\",\n        \"description\": \"Supplementary. Languages (rows, grouped by resource tier) × representative layers (columns). Cells: selectivity (probe AUROC - control AUROC). Color-coded: green >15pp, yellow 10-15pp, orange 5-10pp. Shows resource- tier gradient in selectivity.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Control tasks validate that probe AUROC reflects genuine correctness signal for the large majority of settings (88% above 10pp). The resource-tier gradient in selectivity is a limitation to acknowledge: for low-resource languages, probe signal quality is weaker, and conclusions about transfer should be interpreted with this caveat. This doesn't undermine the paper's core claims (which are about the mechanism of transfer failure, not about achieving high probe quality in every language) but sets appropriate epistemic bounds.\\n\\n\\nControl tasks with random labels test whether probe capacity (model expressiveness) alone can achieve high AUROC without genuine correctness signal. The control AUROC of ~0.54-0.55 (barely above chance at 0.50) confirms that logistic regression probes do not have sufficient capacity to memorize random label assignments in high-dimensional space — any AUROC above this baseline reflects genuine signal. English selectivity (median 0.265) is strong: the probe captures real correctness information 26.5pp above what capacity alone could achieve. Non-English selectivity decreases with resource tier because: (a) the correctness signal itself is weaker for languages with less pretraining data; (b) the cross-lingual transfer means probes must generalize from English-learned patterns, which is inherently harder for distant languages. Low-resource languages (sw, bn) show selectivity ~10pp, still positive but approaching the threshold where a reviewer might question signal quality. The 88% of language-layer combinations exceeding 10pp provides reasonable validation, but the 30% failure rate for low-resource languages at this threshold is a genuine limitation that the paper should acknowledge. Selectivity peaks at mid-depth (~55%) because shallow layers have weaker correctness signals (less processed) and very deep layers have stronger but more language-specific signals (high probe AUROC but also higher control AUROC due to richer features).\\n\"\n  },\n  {\n    \"name\": \"Gemma 4 31B Dense Pareto Frontier\",\n    \"description\": \"Third architecture for camera-ready. 60 layers, dense, FP16. Full Pareto frontier, 20+ languages. Dense vs MoE contrast.\\n\",\n    \"results\": {\n      \"en_best_auroc\": 0.8,\n      \"en_best_layer\": 45,\n      \"zs_transfer_auroc_median\": 0.69,\n      \"best_transfer_layer\": 33,\n      \"pareto_rho_per_lang_median\": -0.58,\n      \"zs_langs_above_0p65\": 12,\n      \"pareto_rho_smoother_than_moe\": true,\n      \"pareto_rho_std_across_langs_gemma\": 0.12,\n      \"pareto_rho_std_across_langs_qwen\": 0.16,\n      \"pareto_rho_std_across_langs_llama\": 0.15,\n      \"cka_depth_decline_steeper_dense\": true,\n      \"linear_proj_delta_median\": 0.033\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table CR1: Three-Architecture Pareto Comparison\",\n        \"description\": \"Camera-ready. Architecture (rows: Qwen3-MoE, Llama4-MoE, Gemma4-Dense) × key metrics (EN AUROC, ZS median, rho median, rho std, CKA slope, linear-proj Δ). Highlights dense vs MoE contrast in rho variance and CKA slope.\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready addition. The dense-vs-MoE contrast is the strongest architecture- dependence evidence: MoE routing introduces heterogeneity that partially buffers against geometric misalignment at deep layers, while dense models show cleaner depth-dependent degradation. This doesn't change the paper's conclusions but provides a more compelling architectural contrast than two MoE models alone.\\n\\n\\nGemma 4 31B Dense provides the critical dense-vs-MoE architectural contrast. As a dense model, every token passes through every layer (no routing), creating more uniform layer-to-layer transformations. This produces a smoother Pareto frontier (lower rho variance across languages: 0.12 vs 0.15-0.16 for MoE models) because the depth-transfer tradeoff is more consistent without routing-induced heterogeneity. The rho itself is slightly stronger negative (-0.58) because dense models show a cleaner monotonic decline in cross-lingual alignment with depth — MoE routing partially breaks this monotonicity by allowing some expert pathways to maintain cross-lingual features at deeper layers. CKA declines more steeply with depth in the dense model, confirming that MoE routing provides a modest buffer against geometric misalignment (different experts can specialize differently per language). English AUROC (0.80) is comparable to the larger MoE models despite smaller parameter count because the 31B dense architecture is parameter-efficient for representation quality. This is a P2 camera-ready experiment that strengthens the architecture-dependence claim from \\\"two MoE models differ moderately\\\" to \\\"dense vs MoE is a qualitatively distinct contrast.\\\"\\n\"\n  },\n  {\n    \"name\": \"Extended Language Coverage (50+ Languages)\",\n    \"description\": \"Expand from 20 to 50+ languages for camera-ready. Full GlobalMMLU/Belebele language sets.\\n\",\n    \"results\": {\n      \"total_languages\": 52,\n      \"zs_langs_above_0p65\": 28,\n      \"zs_median_auroc_52lang\": 0.66,\n      \"zs_auroc_range\": [\n        0.5,\n        0.74\n      ],\n      \"new_low_resource_langs_below_0p55\": [\n        \"am\",\n        \"my\",\n        \"zu\",\n        \"sn\",\n        \"rw\"\n      ],\n      \"resource_tier_gradient_replicates\": true,\n      \"pareto_rho_median_52lang\": -0.49,\n      \"linear_proj_delta_median_52lang\": 0.031,\n      \"tail_langs_below_0p55_count\": 8,\n      \"tail_langs_above_0p70_count\": 12\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table CR2: Extended Language Coverage — 52 Languages\",\n        \"description\": \"Camera-ready. Full 52-language results sorted by zero-shot AUROC. Columns: language, family, resource tier, ZS AUROC, linear-proj AUROC, few-shot-100 AUROC. Grouped into tiers: >0.70 (strong transfer), 0.65-0.70 (viable), 0.55-0.65 (marginal), <0.55 (failed).\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Camera-ready extension. The 52-language analysis adds scale but the median-tier conclusion is clear: probe-based cross-lingual calibration works for a majority but not all languages, and the resource-tier gradient is the dominant predictor of success. This sets realistic expectations for practitioners and motivates future work on low-resource language probe training.\\n\\nExpanding to 52 languages adds many more low-resource and typologically diverse languages. The median AUROC drops slightly (0.66 vs 0.70 for the curated 20) because the additional languages are disproportionately low-resource. Five extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda) fall below 0.55, approaching chance performance — these languages have minimal pretraining representation in both models. The resource-tier gradient continues to hold and becomes even more pronounced with the extended tail. Pareto rho weakens slightly (-0.49) because many of the new languages show weak, noisy correlations due to low base probe quality. Linear projection improvement remains consistent (+3.1pp), confirming the geometric correction generalizes beyond the curated language set. The practical message: probe-based cross-lingual calibration is viable for ~28/52 languages (54%) without any target-language data, and linear projection extends this to ~35/52 (67%). The remaining ~17 languages need language-specific probes or alternative approaches.\\n\"\n  }\n]",
      "numLines": 501,
      "startLine": 1,
      "totalLines": 501
    }
  },
  "sourceToolAssistantUUID": "99c136ae-5794-4823-ac10-7a29c4c5130b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:46:43.268Z_

<details><summary>↩ Tool result · `toolu_016hJUEgKgJF57LEw8MfaQcg`</summary>

```text
1	# Paper Framing — xling_calib_direction
2	
3	## Target Venue
4	- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)
5	- Core submission: 2 models × 20 languages × all contributions
6	- Camera-ready extension: Gemma 4 31B Dense + 30+ languages
7	
8	## Core Insight
9	The model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.
10	
11	## Core Claims (4, causal chain)
12	
13	### Claim 1 — Pareto Frontier (Discovery)
14	Cross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.
15	- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.
16	- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.
17	
18	### Claim 2 — Decomposition (Analysis)
19	Cross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.
20	- Evidence: IRT difficulty probes → project out → retrain → compare transfer.
21	
22	### Claim 3 — CaCLR (Method / Diagnostic)
23	CaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.
24	- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.
25	- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.
26	- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.
27	- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.
28	- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.
29	
30	### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)
31	The correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.
32	- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.
33	
34	## Story Spine
35	- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).
36	- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.
37	- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.
38	- **Headline template (method success)**: "On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels."
39	- **Headline template (negative result)**: "Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines."
40	- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.
41	
42	## Field-Level Significance
43	This paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.
44	
45	## Anticipated Reviewer Concerns & Responses
46	1. **"Xiao et al. already did this"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.
47	2. **"Temperature scaling baseline"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.
48	3. **"Mean-shift too weak / why does it fail?"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.
49	4. **"Difficulty confound"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.
50	5. **"INT8 artifacts"** → Validation ablation comparing INT8 vs FP16 at representative layers.
51	6. **"Only MCQA"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.
52	7. **"Predictable from domain adaptation theory"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.
53	8. **"No statistical tests"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.
54	9. **"Probing methodology concerns"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.
55	10. **"No mechanistic explanation"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.
56	11. **"Why not conformal prediction?"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.
57	12. **"CaCLR parallel activations = test leakage?"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.
58	
59	## Additional Related Work Coverage (Dream-identified gaps)
60	- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.
61	- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.
62	- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.
63	- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.
64	- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.
65	
66	## Differentiation from Closest Prior Work
67	| Paper | Their Focus | Our Difference |
68	|-------|-------------|----------------|
69	| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |
70	| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |
71	| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |
72	| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |
73	| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efa921cb-f4bb-4947-85ee-0e783b63dc87",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "2b190086-1f61-47b7-af02-7a56458434c2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md",
      "content": "# Paper Framing — xling_calib_direction\n\n## Target Venue\n- Primary: **EACL 2027** (ARR submission deadline: August 3, 2026 — 10.5 weeks from project start)\n- Core submission: 2 models × 20 languages × all contributions\n- Camera-ready extension: Gemma 4 31B Dense + 30+ languages\n\n## Core Insight\nThe model's internal correctness direction — linearly accessible but orthogonal to verbalized confidence — transfers cross-lingually through intermediate layers, but with a depth-transferability Pareto tradeoff: deeper layers yield better English calibration while shallower layers transfer better. This tradeoff is architecture-dependent and can be shifted by CaCLR, a probe training objective that jointly optimizes correctness prediction and cross-lingual calibration invariance without requiring target-language correctness labels.\n\n## Core Claims (4, causal chain)\n\n### Claim 1 — Pareto Frontier (Discovery)\nCross-lingual correctness probes reveal a depth-transferability Pareto frontier: deeper layers produce better-calibrated English probes but degrade in cross-lingual zero-shot transfer. The optimal transfer depth is architecture-dependent.\n- MVP evidence: L27 AUROC=0.754 (EN best) but transfer drops 2-4pp vs L24 on Qwen2.5-7B.\n- Full evidence: 2 architectures × 20 languages × all layers × 5 transfer conditions.\n\n### Claim 2 — Decomposition (Analysis)\nCross-lingual correctness transfer decomposes into a difficulty-shared component (language-agnostic, transferable at all depths) and a capability-specific component (language-dependent, driving deep-layer transfer degradation). This decomposition is prescriptive: it predicts which alignment strategy is needed per language-layer combination.\n- Evidence: IRT difficulty probes → project out → retrain → compare transfer.\n\n### Claim 3 — CaCLR (Method / Diagnostic)\nCaCLR (L_BCE + α·L_SB-ECE + β·L_consistency, where L_consistency uses MMD on parallel activations from GlobalMMLU translated items, train split only) tests whether joint calibration + cross-lingual invariance optimization can shift the Pareto frontier without target-language correctness labels.\n- **If consistency loss helps**: CaCLR is a method contribution that enables deeper, better-calibrated probe transfer.\n- **If consistency loss is inert**: The negative result itself is the contribution — demonstrating that distributional matching fails for correctness probe transfer. CKA analysis provides the theoretical explanation: cross-lingual misalignment at deeper layers is *geometric* (correctness direction rotates/scales across language subspaces), not merely *distributional* (mean/covariance shift). MMD-based alignment cannot correct geometric transformations, which is why linear projection (which learns the rotation) succeeds where distributional matching fails. This closes the distributional-matching path with both empirical evidence and mechanistic explanation.\n- Parallel activations source: GlobalMMLU train-split translations (not test items). This requires parallel *inputs* but zero target-language *labels* — a weaker requirement than per-language annotation.\n- MVP evidence: Mean-shift fails (unreliable across 5 languages) — motivates principled approach.\n- Evidence: CaCLR vs zero-shot/mean-shift/linear-projection/few-shot across full Pareto frontier. α sensitivity sweep required. β sweep across 3 OOM to test consistency loss value.\n\n### Claim 4 — Cross-Lingual Orthogonality (Mechanistic)\nThe correctness-confidence orthogonality (Miao & Ungar, 2026; cosine < 0.04) persists across languages but varies with resource tier and architecture, establishing output-based calibration as structurally limited regardless of language.\n- Evidence: Cosine similarity measurement in 20 languages × 2+ architectures.\n\n## Story Spine\n- **Problem**: Non-English languages suffer 5x worse calibration (ECE) in multilingual LLMs. Output-based calibration is fundamentally limited — correctness and verbalized confidence directions are orthogonal. Existing fixes require per-language data (LACE) or 5x inference cost (MKA).\n- **Gaps**: All probe-based calibration methods (CORAL, CCPS, Confidence Manifold, Miao & Ungar steering) are English-only. Nobody has tested whether this research line works multilingually. Xiao et al. transferred knowledge-boundary probes (input-level answerability), not correctness probes (output-dependent accuracy) — fundamentally different targets.\n- **Our framing**: First systematic test of probe-based calibration in multilingual settings. We discover the Pareto frontier, decompose transfer into difficulty/capability components, test CaCLR as the natural distributional-matching approach, and provide mechanistic analysis (CKA) explaining why transfer succeeds or fails at each depth. This is both a field-level viability test and (depending on CaCLR results) a practical method contribution or a principled negative result.\n- **Headline template (method success)**: \"On GlobalMMLU across 20 languages, CaCLR-trained correctness probes reduce non-English ECE by X% compared to temperature scaling, requiring zero target-language correctness labels.\"\n- **Headline template (negative result)**: \"Cross-lingual correctness probe transfer reveals architecture-dependent Pareto frontier; the natural distributional-matching approach (CaCLR) fails, but simple linear projection with ~50 parallel pairs matches supervised baselines.\"\n- **Constructive path forward**: For languages where zero-shot transfer fails, the paper identifies three viable directions: (1) language-specific probes with minimal labeled data (few-shot 25-100 shown effective), (2) adapter-based alignment leveraging pretrained multilingual adapters, (3) multilingual probe training on pooled high-resource languages.\n\n## Field-Level Significance\nThis paper tests whether the entire probe-based calibration research line works beyond English. Regardless of results, it answers a field-level question about multilingual viability of representation-level calibration — validating or closing this path for the community.\n\n## Anticipated Reviewer Concerns & Responses\n1. **\"Xiao et al. already did this\"** → Knowledge boundary (input-level, binary answerability) vs correctness (output-dependent accuracy). They measure probing accuracy, not calibration. 8 languages vs our 20+. No Pareto frontier. We explicitly analyze why answerability transfers (Xiao's partial success) but correctness does not — different signal types have different cross-lingual alignment properties.\n2. **\"Temperature scaling baseline\"** → We compare against it. CaCLR optimizes during training, not post-hoc. Temperature scaling can't address cross-lingual representation misalignment.\n3. **\"Mean-shift too weak / why does it fail?\"** → We provide a formal proof: under StandardScaler + logistic regression, mean-shift adds a constant offset to all logits → AUROC is rank-invariant → ΔAUROC ≡ 0 mathematically. MVP data confirms: ΔAUROC = 0.000000 across all 5 languages × all layers. ECE changes are unreliable because they depend on threshold-sensitive binning of shifted probabilities. This proof (1-2 paragraphs + experimental validation) distinguishes us from Xiao et al. (where mean-shift works under different metrics/pipeline) and directly motivates why stronger alignment methods (linear projection, CaCLR) are needed.\n4. **\"Difficulty confound\"** → Claim 2's decomposition ablation explicitly controls for this via IRT difficulty probes.\n5. **\"INT8 artifacts\"** → Validation ablation comparing INT8 vs FP16 at representative layers.\n6. **\"Only MCQA\"** → Acknowledged. MCQA enables clean correctness labeling and parallel multilingual evaluation via GlobalMMLU.\n7. **\"Predictable from domain adaptation theory\"** → We explicitly derive predictions from Ben-David et al. (2010) H-divergence framework and test them. The resource-tier gradient is expected; the novel findings are (a) the Pareto frontier shape is architecture-dependent (not predicted by theory), (b) difficulty-capability entanglement, and (c) distributional matching (CaCLR) fails despite seemingly matching the theory's prescription.\n8. **\"No statistical tests\"** → All key comparisons include bootstrap CIs (1000 resamples) and paired permutation tests across languages. Effect sizes reported with Cohen's d.\n9. **\"Probing methodology concerns\"** → We include Hewitt & Liang (2019) control tasks to validate that probe AUROC reflects genuine correctness directions, not dataset artifacts.\n10. **\"No mechanistic explanation\"** → CKA analysis across layers × languages explains WHY transfer fails at deeper layers (cross-lingual representation similarity decreases with depth) and correlates with transfer success.\n11. **\"Why not conformal prediction?\"** → Discussed in Related Work. Conformal prediction provides distribution-free coverage guarantees but requires calibration data per language; our approach targets zero-label transfer. Complementary, not competing.\n12. **\"CaCLR parallel activations = test leakage?\"** → Parallel activations are from GlobalMMLU train split only, never test items. The requirement is parallel inputs (available via existing translations), not target-language labels.\n\n## Additional Related Work Coverage (Dream-identified gaps)\n- **Domain adaptation theory**: Ben-David et al. (2010) H-divergence provides theoretical grounding for resource-tier gradient. We derive predictions and test them.\n- **Cross-lingual alignment**: MUSE (Conneau et al. 2018), VecMap (Artetxe et al. 2018) — linear projection's effectiveness is consistent with this literature; CaCLR's failure despite distributional matching is the novel finding.\n- **Representation similarity**: CKA (Kornblith et al. 2019), SVCCA (Raghu et al. 2017) — we use CKA to provide mechanistic explanation for the Pareto frontier.\n- **Probing methodology**: Hewitt & Liang (2019) control tasks, Voita & Titov (2020) MDL probes — we include control tasks to validate probe selectivity.\n- **Conformal prediction**: Angelopoulos & Bates (2023) — complementary approach discussed in Related Work; requires per-language calibration data vs our zero-label target.\n\n## Differentiation from Closest Prior Work\n| Paper | Their Focus | Our Difference |\n|-------|-------------|----------------|\n| Xiao et al. (ACL 2025) | Knowledge boundary cross-lingual probe transfer | Correctness (not boundary); calibration metrics (not probing accuracy); 20+ languages; Pareto frontier. We analyze WHY answerability transfers but correctness does not. |\n| LACE (Zhou et al.) | Per-language layer ensemble | Zero target-language labels; directional probe transfer; CaCLR method |\n| CORAL (Miao et al.) | Cross-task English correctness probes | Cross-lingual (not cross-task); CaCLR solves their identified distribution-shift problem |\n| Miao & Ungar (2026) | Correctness-confidence orthogonality + steering | English-only 7-8B → multilingual multi-architecture; first non-English orthogonality measurement |\n| Civelli et al. | Cross-lingual difficulty probe transfer | Correctness (not difficulty); difficulty is their control for our ablation |\n",
      "numLines": 74,
      "startLine": 1,
      "totalLines": 74
    }
  },
  "sourceToolAssistantUUID": "efa921cb-f4bb-4947-85ee-0e783b63dc87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:46:43.258Z_

<details open><summary>🔧 Tool call — Read · `toolu_016hJUEgKgJF57LEw8MfaQcg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "260402f9-f69d-47ae-9bb0-d994474792ee",
  "isSidechain": false,
  "requestId": "req_011CbEUYDuBsMzhyhPdA22Dp",
  "type": "assistant",
  "uuid": "efa921cb-f4bb-4947-85ee-0e783b63dc87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkUWwcbqzDPxfo2X3DLfRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11618,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11618
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "2b190086-1f61-47b7-af02-7a56458434c2",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Assistant

_source line 14 · 2026-05-20T20:47:09.797Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment data and paper framing. Let me also load the research and writing skills to get patterns.

Actually, let me just proceed to write the paper directly based on the data I have. I have a thorough understanding of:

1. The narrative arc: Pareto frontier → CKA mechanistic explanation → CaCLR β inertness (negative result) → linear projection as constructive alternative
2. All experiment data with exact numbers
3. Paper framing with claims, story spine, reviewer concerns

Let me write the LaTeX paper now. I need to include:
- Abstract
- Introduction
- Related Work
- Method (probing setup, CaCLR, decomposition, CKA)


- Experiments section with all 11 experiments mapped to tables and subsections
- Results & Analysis covering the Pareto frontier, CKA mechanistic findings, CaCLR implementation results, linear projection sensitivity, and decomposition analysis
- Conclusion

I'm organizing the experiments into a coherent narrative: the Pareto frontier analysis with Qwen3-235B and Llama 4 Scout goes into the first results subsection with tables showing the trade-offs, then CKA analysis reveals the mechanistic explanation, followed by CaCLR implementation results demonstrating the negative finding about β inertness, and finally linear projection sensitivity as the constructive alternative with decomposition analysis supporting the overall story.

For the supplementary material, I'm placing the probe complexity, benchmark generalization, INT8 validation, and control tasks analyses in the appendix to support the main narrative without cluttering the core results.

Given the median-tier positioning for EACL, I'm aiming for a solid, well-structured paper that clearly presents the findings without overreaching—the narrative flows from empirical observations through mechanistic analysis to practical implications, which should land well for a borderline-to-weak accept trajectory.

Now I'm writing the full LaTeX document, making sure to ground everything in the actual metrics from the data: Qwen3-235B peaks at 0.81 AUROC with layer 72 for English, shows a zero-shot transfer median of 0.70 at layer 48, and exhibits a correlation of -0.51; Llama 4 Scout reaches 0.79 AUROC at layer 36 with 0.68 median transfer at layer 24 and -0.54 correlation; Gemma 4 31B achieves 0.80 AUROC at layer 45 with 0.69 median transfer at layer 33 and -0.58 correlation; the CaCLR β inert condition shows negligible effect at d=0.08 with p=0.42; and the linear projection baseline provides a comparison point.

I'm now incorporating the additional findings: the projection method improves performance by 3.5 percentage points for Qwen and 3.2 for Llama, saturating around 70 training pairs; CKA-based transfer achieves r=0.58 correlation and explains 34% of variance compared to just 6% for MMD; orthogonality analysis shows all cosine similarities stay below 0.10 with a resource-tier gradient correlation of 0.52; the decomposition analysis reveals 65% improvement with d=0.28; and control tasks maintain 88% selectivity above the 10 percentage point threshold. I'll structure this using ACL formatting conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b190086-1f61-47b7-af02-7a56458434c2",
  "isSidechain": false,
  "requestId": "req_011CbEUZWZ5ZFUuckLosbPqa",
  "type": "assistant",
  "uuid": "b94ab2e9-9911-490c-917f-e05ce7cfb289",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhizxHZ2vPq81qXZVypKsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17751,
      "cache_read_input_tokens": 23459,
      "output_tokens": 1006,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1006,
          "cache_read_input_tokens": 23459,
          "cache_creation_input_tokens": 17751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17751
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

_source line 15 · 2026-05-20T20:47:09.799Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b94ab2e9-9911-490c-917f-e05ce7cfb289",
  "isSidechain": false,
  "requestId": "req_011CbEUZWZ5ZFUuckLosbPqa",
  "type": "assistant",
  "uuid": "c60866ae-1cca-47d9-b0c0-55d39b773e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhizxHZ2vPq81qXZVypKsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17751,
      "cache_read_input_tokens": 23459,
      "output_tokens": 1006,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1006,
          "cache_read_input_tokens": 23459,
          "cache_creation_input_tokens": 17751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17751
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

_source line 16 · 2026-05-20T20:47:09.996Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WyMBYaLj9PpkVL76yyKpbF`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c60866ae-1cca-47d9-b0c0-55d39b773e0a",
  "isSidechain": false,
  "requestId": "req_011CbEUZWZ5ZFUuckLosbPqa",
  "type": "assistant",
  "uuid": "c8e1b80f-684e-4b5f-a684-de32492fda52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhizxHZ2vPq81qXZVypKsB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17751,
      "cache_read_input_tokens": 23459,
      "output_tokens": 1006,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1006,
          "cache_read_input_tokens": 23459,
          "cache_creation_input_tokens": 17751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17751
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

_source line 17 · 2026-05-20T20:47:10.158Z_

<details><summary>↩ Tool result · `toolu_01WyMBYaLj9PpkVL76yyKpbF`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8e1b80f-684e-4b5f-a684-de32492fda52",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "9b2172b9-0ac0-4667-8e94-3fa38d6495f4",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "c8e1b80f-684e-4b5f-a684-de32492fda52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T20:51:06.551Z_

<details open><summary>🔧 Tool call — Write · `toolu_013C1JyxQLEJcVVkcZFyTXv1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\definecolor{improved}{rgb}{0.85,0.95,0.85}\n\\definecolor{degraded}{rgb}{0.95,0.85,0.85}\n\n\\title{Cross-Lingual Correctness Probes Reveal a Depth--Transferability\\\\Pareto Frontier: Distributional Matching Fails\\\\Where Linear Projection Succeeds}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness signals from LLM representations, achieving strong results in English. Whether these signals transfer cross-lingually remains untested. We present the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20+ languages, and 5 transfer methods. We discover a \\emph{depth--transferability Pareto frontier}: deeper layers yield higher English calibration quality (AUROC up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman $\\rho = -0.52$ between English AUROC and transfer AUROC). CKA analysis reveals the mechanism---geometric misalignment between language subspaces increases with depth ($r = 0.58$ between CKA similarity and transfer AUROC, explaining 34\\% of variance). We test CaCLR, a probe training objective augmenting BCE loss with MMD-based cross-lingual consistency, and show that the consistency term is \\emph{inert} across three orders of magnitude ($\\beta$ sweep: Cohen's $d = 0.08$, $p = 0.42$)---predicted by the geometric explanation, since MMD cannot correct representational rotations. In contrast, linear projection with as few as 50--100 parallel pairs achieves +3.5\\,pp AUROC over zero-shot transfer, precisely because it learns the rotation that distributional matching cannot. Correctness--confidence orthogonality (cosine $< 0.10$) persists across all 20 languages, confirming that output-based calibration is structurally limited regardless of language. Our results establish that probe-based cross-lingual calibration is viable for the majority of languages at mid-depth layers, close the distributional-matching path with both empirical evidence and mechanistic explanation, and identify linear projection as the practical solution.\n\\end{abstract}\n\n%====================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) degrading up to 5$\\times$ compared to English \\cite{ahuja2024globalmmlu,lai2024llmsurvey}. Recent work has shown that probe-based calibration---extracting internal correctness signals via linear probes on model representations---outperforms output-based methods in English \\cite{miao2026coral,burns2023discovering}. A key finding by \\citet{miao2026orthogonality} is that correctness and verbalized confidence directions are nearly orthogonal (cosine $< 0.04$) in English, establishing a structural limitation of output-based approaches. However, all existing probe-based calibration methods operate exclusively in English, leaving a fundamental question unanswered: \\emph{do these internal correctness signals transfer across languages?}\n\nThe answer is not obvious. Cross-lingual representation transfer has been studied extensively for tasks like NER and classification \\cite{pires2019multilingual,conneau2020unsupervised}, but correctness probes target a fundamentally different signal---output-dependent accuracy rather than input-level features. \\citet{xiao2025knowledgeboundary} transferred \\emph{knowledge boundary} probes (input-level answerability) across 8 languages, but answerability and correctness are distinct signals with potentially different cross-lingual alignment properties.\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, contributing four findings organized as a causal chain:\n\n\\paragraph{(1) Pareto Frontier.} We discover a depth--transferability tradeoff: deeper layers produce better English probes but transfer worse cross-lingually. The frontier shape is architecture-dependent (Spearman $\\rho$ ranging from $-0.51$ to $-0.58$ across three architectures).\n\n\\paragraph{(2) Mechanistic Explanation.} CKA analysis reveals that cross-lingual geometric similarity decreases with depth. The CKA--transfer correlation ($r = 0.58$) explains 34\\% of transfer variance, substantially outpredicting distributional measures like MMD (6\\%).\n\n\\paragraph{(3) Principled Negative Result.} CaCLR, a probe training objective with MMD-based cross-lingual consistency loss, fails to shift the Pareto frontier ($d = 0.08$). This is \\emph{predicted} by the geometric explanation: MMD matches marginal distributions but cannot correct the rotation of the correctness direction across language subspaces.\n\n\\paragraph{(4) Constructive Alternative.} Linear projection with $\\sim$50--100 parallel pairs achieves +3.5\\,pp over zero-shot, succeeding precisely because it learns the rotation that MMD cannot. The correctness--confidence orthogonality persists across all 20 languages, confirming the structural necessity of probe-based approaches.\n\nWe evaluate on GlobalMMLU \\cite{ahuja2024globalmmlu}, Belebele \\cite{bandarkar2023belebele}, and MMLU-ProX across 20 languages and 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), with camera-ready extensions to 52 languages.\n\n%====================================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-Based Calibration.}\n\\citet{burns2023discovering} and \\citet{li2024inference} demonstrated that linear probes on internal representations can identify model knowledge states. CORAL \\cite{miao2026coral} extended this to cross-task English calibration. \\citet{miao2026orthogonality} showed correctness--confidence orthogonality and used steering to improve calibration. All are English-only.\n\n\\paragraph{Cross-Lingual Probe Transfer.}\n\\citet{xiao2025knowledgeboundary} transferred knowledge boundary probes across 8 languages, finding partial success. However, knowledge boundary (binary answerability) is an input-level property, while correctness depends on the model's actual output. \\citet{civelli2024difficulty} transferred difficulty probes cross-lingually---difficulty is a shared confound we explicitly control for. LACE \\cite{zhou2024lace} ensembles per-language probes but requires target-language labels.\n\n\\paragraph{Cross-Lingual Alignment.}\nMUSE \\cite{conneau2018muse} and VecMap \\cite{artetxe2018vecmap} achieve bilingual alignment with $\\sim$50--100 dictionary entries via linear mappings. Our linear projection's sample efficiency is consistent with this literature. The novel finding is that distributional matching (MMD, the natural choice from domain adaptation theory \\cite{bendavid2010theory}) fails for this specific alignment task.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} measures geometric similarity between representations. We use CKA to explain \\emph{why} transfer fails at depth---complementing prior work using CKA for layer-level analysis \\cite{nguyen2021wide}.\n\n\\paragraph{Conformal Prediction.}\nConformal methods \\cite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require calibration data per language. Our approach targets zero-label transfer; the two are complementary.\n\n%====================================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probes}\n\\label{sec:probes}\n\nGiven a multilingual MCQA dataset, we extract hidden representations $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each question, taking the last-token representation before answer generation. We train a logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ on English data to predict binary correctness (whether the model's selected answer matches the gold label). We evaluate via AUROC and ECE.\n\n\\paragraph{Cross-Lingual Transfer.}\nWe evaluate the English-trained probe on target-language representations without any adaptation (zero-shot transfer). We compare five transfer conditions:\n\n\\begin{enumerate}[itemsep=1pt,parsep=0pt]\n    \\item \\textbf{Zero-shot}: Direct application of the English probe.\n    \\item \\textbf{Mean-shift}: Center target representations to match English mean.\n    \\item \\textbf{Linear projection}: Learn an affine mapping $\\mathbf{h}_{\\text{tgt}} \\mapsto \\mathbf{W}\\mathbf{h}_{\\text{tgt}} + \\mathbf{b}$ from parallel pairs.\n    \\item \\textbf{Few-shot} (25/100): Train on small target-language labeled sets.\n    \\item \\textbf{CaCLR}: Our proposed training objective (\\S\\ref{sec:caclr}).\n\\end{enumerate}\n\n\\paragraph{Mean-Shift Rank Invariance.}\nUnder StandardScaler preprocessing and logistic regression, mean-shift adds a constant offset to all logits: $\\mathbf{w}^\\top (\\mathbf{h} + \\boldsymbol{\\delta}) + b = \\mathbf{w}^\\top \\mathbf{h} + (b + \\mathbf{w}^\\top \\boldsymbol{\\delta})$. Since AUROC depends only on ranking, $\\Delta\\text{AUROC} \\equiv 0$ mathematically. Our experiments confirm this ($\\Delta\\text{AUROC} = 0.000$ across all conditions).\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr}\n\nCaCLR augments the standard probe training objective with two regularization terms:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is a differentiable smooth-binned ECE loss and $\\mathcal{L}_{\\text{consistency}}$ is an MMD-based term:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2\\big(\\{f(\\mathbf{h}_i^{\\text{en}})\\}, \\{f(\\mathbf{h}_i^{\\text{tgt}})\\}\\big)\n\\end{equation}\ncomputed over parallel activations from GlobalMMLU train-split translations. This requires parallel \\emph{inputs} but zero target-language \\emph{labels}.\n\n\\subsection{Difficulty-Controlled Decomposition}\n\\label{sec:decomp}\n\nFollowing IRT-based difficulty estimation, we train a difficulty probe $g(\\mathbf{h}) = \\mathbf{v}^\\top \\mathbf{h} + c$ predicting item difficulty. We project out the difficulty direction: $\\mathbf{h}^{\\perp} = \\mathbf{h} - (\\mathbf{h}^\\top \\hat{\\mathbf{v}})\\hat{\\mathbf{v}}$, then retrain correctness probes on residuals. Improvement after difficulty removal indicates the capability-specific component drives transfer degradation.\n\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA \\cite{kornblith2019similarity} between English and target-language representations at each probed layer:\n\\begin{equation}\n\\text{CKA}(\\mathbf{X}_{\\text{en}}, \\mathbf{X}_{\\text{tgt}}) = \\frac{\\|\\mathbf{X}_{\\text{en}}^\\top \\mathbf{X}_{\\text{tgt}}\\|_F^2}{\\|\\mathbf{X}_{\\text{en}}^\\top \\mathbf{X}_{\\text{en}}\\|_F \\cdot \\|\\mathbf{X}_{\\text{tgt}}^\\top \\mathbf{X}_{\\text{tgt}}\\|_F}\n\\end{equation}\nCKA captures geometric similarity (rotation, scaling), while MMD captures distributional distance. We correlate both with transfer AUROC to determine which type of misalignment drives transfer failure.\n\n%====================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate three architectures: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), and Gemma~4 31B (60 layers, dense, FP16). INT8 quantization is validated against FP16 (Appendix~\\ref{app:int8}).\n\n\\paragraph{Languages.}\nCore evaluation: 20 languages spanning 4 resource tiers and 8 language families (zh, es, fr, de, ar, hi, ru, ko, ja, pt, vi, tr, id, th, pl, uk, he, el, sw, bn). Camera-ready extension: 52 languages.\n\n\\paragraph{Datasets.}\nPrimary: GlobalMMLU \\cite{ahuja2024globalmmlu}. Generalization: Belebele \\cite{bandarkar2023belebele} and MMLU-ProX. Train/test splits follow standard protocols; CaCLR parallel activations use train split only.\n\n\\paragraph{Probing Layers.}\nWe probe 24 layers for Qwen3-235B (evenly spaced across 94 layers), 12 for Llama~4 Scout, and 15 for Gemma~4 31B.\n\n\\paragraph{Evaluation Metrics.}\nAUROC (primary, rank-based), ECE (secondary, calibration quality), paired permutation tests ($p < 0.05$), bootstrap 95\\% CIs (1000 resamples), Cohen's $d$ for effect sizes.\n\n%====================================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pareto frontier summary across three architectures. EN\\textsubscript{best}: English optimal AUROC and layer. ZS\\textsubscript{med}: median zero-shot transfer AUROC at the best transfer layer. $\\rho$\\textsubscript{med}: median per-language Spearman correlation between English AUROC and transfer AUROC. $\\sigma_\\rho$: standard deviation of per-language $\\rho$.}\n\\label{tab:pareto_summary}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Architecture} & \\textbf{EN\\textsubscript{best}} & \\textbf{Layer} & \\textbf{ZS\\textsubscript{med}} & \\textbf{Xfer Layer} & \\textbf{$\\rho$\\textsubscript{med}} & \\textbf{$\\sigma_\\rho$} \\\\\n\\midrule\nQwen3-235B (MoE) & 0.81 & 72 & 0.70 & 48 & $-$0.51 & 0.16 \\\\\nLlama 4 Scout (MoE) & 0.79 & 36 & 0.68 & 24 & $-$0.54 & 0.15 \\\\\nGemma 4 31B (Dense) & 0.80 & 45 & 0.69 & 33 & $-$0.58 & 0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pareto_summary} presents the Pareto frontier across all three architectures. The key pattern is consistent: the English-optimal layer (72--76\\% depth) is \\emph{not} the transfer-optimal layer ($\\sim$50\\% depth) for most languages. The Spearman correlation between English AUROC and cross-lingual transfer AUROC is moderately negative across architectures ($\\rho$ median $-0.51$ to $-0.58$), confirming the depth--transferability tradeoff.\n\nThe architecture-dependent shape is visible in two contrasts. First, MoE models (Qwen3, Llama~4) show higher per-language $\\rho$ variance ($\\sigma_\\rho = 0.15$--$0.16$) than the dense model (Gemma~4, $\\sigma_\\rho = 0.12$), reflecting MoE routing's heterogeneous effect on cross-lingual alignment. Second, the per-language $\\rho$ range spans $[-0.82, -0.21]$ across models, with low-resource languages (sw: $\\rho \\approx -0.78$) showing stronger negative correlations than high-resource languages (zh: $\\rho \\approx -0.21$), indicating that representation divergence from English scales with both depth and pretraining exposure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot transfer AUROC at the best transfer layer for 20 languages on Qwen3-235B-A22B. Languages grouped by resource tier.}\n\\label{tab:zs_by_lang}\n\\begin{tabular}{llc|llc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{AUROC} & \\textbf{Lang} & \\textbf{Tier} & \\textbf{AUROC} \\\\\n\\midrule\nzh & High & 0.74 & vi & Mid & 0.68 \\\\\nes & High & 0.73 & tr & Mid & 0.67 \\\\\nfr & High & 0.73 & id & Mid & 0.68 \\\\\nde & High & 0.72 & th & Mid & 0.66 \\\\\npt & High & 0.72 & pl & Mid & 0.69 \\\\\n\\midrule\nar & Mid & 0.70 & uk & Mid & 0.68 \\\\\nru & Mid & 0.71 & he & Mid & 0.66 \\\\\nhi & Mid & 0.69 & el & Mid & 0.65 \\\\\nko & Mid & 0.69 & sw & Low & 0.58 \\\\\nja & Mid & 0.70 & bn & Low & 0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:zs_by_lang} shows per-language zero-shot transfer AUROC at the best transfer layer for Qwen3-235B. Of 20 languages, 13 exceed the 0.65 AUROC threshold for usable calibration (11 for Llama~4 Scout). The resource-tier gradient is clear: high-resource languages cluster at 0.72--0.74, mid-resource at 0.65--0.71, and low-resource sw/bn fall below 0.60.\n\n\\subsection{CKA Reveals Geometric Misalignment}\n\\label{sec:cka_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CKA similarity between English and target languages at shallow (12) vs.\\ deep (72) layers on Qwen3-235B, grouped by resource tier. Pearson $r$ between CKA and transfer AUROC shown at bottom.}\n\\label{tab:cka}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Resource Tier} & \\textbf{CKA\\textsubscript{shallow}} & \\textbf{CKA\\textsubscript{deep}} \\\\\n\\midrule\nHigh (zh, es, fr, de, pt) & 0.88 & 0.60 \\\\\nMid (ar, ru, hi, ko, ja, ...) & 0.84 & 0.48 \\\\\nLow (sw, bn) & 0.78 & 0.36 \\\\\n\\midrule\nAll languages (median) & 0.84 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{4pt}\n\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Predictor} & \\textbf{Pearson $r$} & \\textbf{Variance Explained} \\\\\n\\midrule\nCKA (linear) & 0.58 & 34\\% \\\\\nMMD & 0.25 & 6\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCKA similarity between English and target-language representations decreases significantly with depth ($p < 10^{-5}$; Table~\\ref{tab:cka}). The decline is steepest for low-resource languages (0.78 $\\to$ 0.36) and most gradual for high-resource languages (0.88 $\\to$ 0.60), mirroring the transfer AUROC gradient.\n\nThe CKA--transfer correlation ($r = 0.58$ pooled across both MoE models, $p < 10^{-5}$) explains 34\\% of transfer variance, substantially outpredicting MMD ($r = 0.25$, 6\\% variance explained). This asymmetry is the mechanistic key: if cross-lingual misalignment were distributional (mean/covariance shift), MMD would predict transfer comparably to CKA. The 5.7$\\times$ ratio in explained variance demonstrates that misalignment is geometric---the correctness direction \\emph{rotates} across language subspaces rather than merely shifting.\n\nThe dense model (Gemma~4 31B) shows steeper CKA decline with depth than both MoE models, consistent with MoE routing providing a modest buffer against geometric misalignment (different experts can maintain cross-lingual features at deeper layers).\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sensitivity sweep: $\\Delta$AUROC over the $\\alpha$-only baseline ($\\beta = 0$, $\\alpha = 0.5$). Median across 20 languages on both architectures. No $\\beta$ value achieves statistical significance.}\n\\label{tab:beta_sweep}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\beta$ & \\textbf{Med $\\Delta$AUROC} & \\textbf{Std} & \\textbf{$p$} & \\textbf{$d$} & \\textbf{\\#Improved} \\\\\n\\midrule\n0 (baseline) & --- & --- & --- & --- & --- \\\\\n0.001 & +0.002 & 0.015 & 0.61 & 0.05 & 12/20 \\\\\n0.01 & +0.001 & 0.014 & 0.53 & 0.03 & 11/20 \\\\\n0.1 & $-$0.001 & 0.016 & 0.48 & 0.04 & 9/20 \\\\\n1.0 & $-$0.003 & 0.018 & 0.35 & 0.10 & 7/20 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall $\\beta$ effect:} & & \\textbf{0.42} & \\textbf{0.08} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\beta$ (consistency loss) term in CaCLR is inert across three orders of magnitude (Table~\\ref{tab:beta_sweep}). The overall effect size is negligible (Cohen's $d = 0.08$, $p = 0.42$). This inertness is consistent across resource tiers: high-resource languages see $\\Delta = +0.004$, mid-resource $\\Delta = 0.000$, low-resource $\\Delta = -0.002$---none significant. The $\\alpha$-only variant (SB-ECE regularization) provides a small calibration improvement (ECE reduction of 0.7\\,pp) without AUROC degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer method comparison: median $\\Delta$AUROC over zero-shot across 20 languages. All methods at per-language oracle layer. Paired permutation test against zero-shot baseline.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{$p$} & \\textbf{$d$} \\\\\n\\midrule\nMean-shift & 0.000 & 0.000 & --- & --- \\\\\nCaCLR ($\\alpha$-only) & +0.005 & +0.005 & 0.18 & 0.12 \\\\\nCaCLR (full) & +0.012 & +0.010 & 0.08 & 0.15 \\\\\nLinear projection & \\textbf{+0.035} & \\textbf{+0.032} & \\textbf{0.001} & \\textbf{0.55} \\\\\nFew-shot (25) & +0.025 & +0.022 & 0.005 & 0.40 \\\\\nFew-shot (100) & +0.045 & +0.040 & $<$0.001 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:method_comparison} shows the full method ranking, consistent across both architectures: few-shot-100 $>$ linear-projection $>$ few-shot-25 $>$ CaCLR $>$ zero-shot $>$ mean-shift. Linear projection achieves +3.5\\,pp (Qwen3) and +3.2\\,pp (Llama~4) with strong statistical significance ($p = 0.001$, $d = 0.55$), while CaCLR's full improvement (+1.2\\,pp) comes entirely from $\\alpha$-term calibration regularization, not from cross-lingual consistency.\n\nThe CKA analysis (\\S\\ref{sec:cka_results}) provides the explanation: MMD optimizes distributional matching, but the misalignment is geometric (rotation/scaling). Linear projection succeeds because it directly estimates and corrects this rotation via a learned affine transformation on parallel pairs.\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linproj}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection $\\Delta$AUROC over zero-shot as a function of parallel pair count. Median across 20 languages, both models. Saturation knee at $\\sim$70 pairs.}\n\\label{tab:linproj_pairs}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med $\\Delta$AUROC} & \\textbf{Std} & \\textbf{\\% of Max} \\\\\n\\midrule\n10 & +0.012 & 0.025 & 33\\% \\\\\n20 & +0.022 & 0.018 & 61\\% \\\\\n50 & +0.030 & 0.012 & 83\\% \\\\\n100 & +0.035 & 0.008 & 97\\% \\\\\n200 & +0.036 & 0.007 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLinear projection shows rapid saturation (Table~\\ref{tab:linproj_pairs}), reaching 90\\% of maximum improvement at $\\sim$55 pairs and 95\\% at $\\sim$85 pairs. The knee point is $\\sim$70 pairs, consistent with the cross-lingual alignment literature where 50--100 bilingual dictionary entries suffice for word-level alignment \\cite{conneau2018muse,artetxe2018vecmap}. The saturation pattern is consistent across architectures (Qwen3 knee: 65 pairs; Llama~4: 75 pairs).\n\nThe practical implication is that $\\sim$50--100 parallel pairs (trivially obtainable from GlobalMMLU's train split or any parallel MCQA corpus) are sufficient to match or exceed CaCLR's entire training pipeline, while requiring no distributional matching, no hyperparameter tuning of $\\alpha$/$\\beta$, and providing a transparent geometric interpretation.\n\n\\subsection{Difficulty-Controlled Decomposition}\n\\label{sec:decomp_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition results: percentage of language--layer combinations improved by difficulty removal, grouped by layer depth and resource tier. Random-direction control shown for comparison.}\n\\label{tab:decomp}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{\\% Improved} & \\textbf{Med $\\Delta$AUROC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{By depth}} \\\\\n\\quad Shallow layers & 50\\% & +0.005 \\\\\n\\quad Deep layers & 78\\% & +0.020 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{By resource tier}} \\\\\n\\quad High-resource & 72\\% & +0.018 \\\\\n\\quad Mid-resource & 65\\% & +0.012 \\\\\n\\quad Low-resource & 53\\% & +0.006 \\\\\n\\midrule\nOverall & 65\\% & +0.012 \\\\\nRandom direction & 50\\% & +0.003 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRemoving the difficulty direction improves transfer in 65\\% of language--layer combinations (Table~\\ref{tab:decomp}; $p = 0.03$, $d = 0.28$). The improvement concentrates at deep layers (78\\% vs.\\ 50\\% at shallow layers), consistent with the CKA finding: at depth, the capability-specific component---which is geometrically misaligned across languages---drives transfer failure. Removing the shared difficulty signal isolates this effect.\n\nThe random-direction control (50\\% improved, $\\Delta = +0.003$, not significant) confirms that the improvement is specific to difficulty removal, not an artifact of dimensionality reduction. The difficulty and correctness directions have moderate cosine similarity (median 0.18, range [0.08, 0.30]), indicating partial but not full entanglement.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cosine similarity between correctness and verbalized confidence directions across languages and resource tiers. All values below the 0.12 orthogonality threshold.}\n\\label{tab:orthogonality}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Cosine (Qwen3)} & \\textbf{Cosine (Llama4)} \\\\\n\\midrule\nEnglish & 0.035 & 0.038 \\\\\n\\midrule\nHigh-resource (med) & 0.040 & 0.042 \\\\\nMid-resource (med) & 0.060 & 0.063 \\\\\nLow-resource (med) & 0.085 & 0.088 \\\\\n\\midrule\nAll languages (med) & 0.055 & 0.060 \\\\\nMax (sw) & 0.100 & 0.098 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe correctness--confidence orthogonality discovered by \\citet{miao2026orthogonality} in English (cosine $< 0.04$) extends to all 20 languages (Table~\\ref{tab:orthogonality}), with all cosine similarities below 0.10. However, a resource-tier gradient emerges: high-resource languages maintain tighter orthogonality (median 0.04) than low-resource languages (median 0.085), with a significant correlation between cosine and resource level (Spearman $\\rho = 0.52$, $p = 0.018$).\n\nEven the maximum cosine (0.10 for Swahili) is far below the $\\sim$0.5+ threshold that would indicate meaningful alignment between correctness and confidence signals. This confirms that output-based calibration is structurally limited across all languages---probe-based approaches are the appropriate paradigm regardless of language, though the cross-lingual \\emph{transfer} of these probes remains the bottleneck.\n\n\\subsection{Three-Architecture Comparison}\n\\label{sec:arch}\n\nThe Gemma~4 31B Dense results (Table~\\ref{tab:pareto_summary}) provide the critical dense-vs-MoE contrast. Dense models show smoother Pareto frontiers ($\\sigma_\\rho = 0.12$ vs.\\ 0.15--0.16 for MoE) because every token passes through every layer, creating more uniform layer-to-layer transformations. The dense model's $\\rho$ is slightly more negative ($-0.58$) and CKA declines more steeply with depth, confirming that MoE routing provides a modest buffer against geometric misalignment. All three architectures agree on the key finding: mid-depth layers ($\\sim$50\\% depth) are the right operating point for cross-lingual transfer.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExtending to 52 languages, 28 (54\\%) exceed 0.65 AUROC in zero-shot transfer. The median drops to 0.66 (vs.\\ 0.70 for the curated 20), reflecting the disproportionately low-resource nature of additional languages. Five extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda) fall below 0.55, approaching chance. The Pareto $\\rho$ weakens slightly ($-0.49$) due to noisier correlations in low-resource languages. Linear projection improvement remains consistent (+3.1\\,pp), confirming the geometric correction generalizes. With linear projection, viability extends to $\\sim$35/52 languages (67\\%).\n\n%====================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why Does Distributional Matching Fail?}\nCaCLR's $\\beta$ inertness is not a hyperparameter failure---it is a fundamental limitation of distributional matching for this alignment task. MMD penalizes differences in mean embeddings and kernel-space moments, aligning \\emph{marginal distributions} without correcting the \\emph{rotation of the correctness direction} across language subspaces. At low $\\beta$, the MMD signal is too weak; at medium $\\beta$, the gradient pushes distributional alignment without targeting the correctness-relevant subspace; at high $\\beta$, the MMD term dominates and distorts the probe. CKA's superiority as a transfer predictor (34\\% vs.\\ 6\\% variance explained) confirms the geometric nature of misalignment.\n\n\\paragraph{The Linear Projection Connection.}\nLinear projection succeeds because it directly estimates the rotation matrix mapping source to target representational spaces. The sample complexity is low ($\\sim$50--100 pairs) because the correctness-relevant subspace is much lower-dimensional than the full representation space. This is consistent with VecMap/MUSE results for word embeddings, extended here to sentence-level correctness representations.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA tasks, which enable clean correctness labeling. Extension to open-ended generation requires different correctness definitions. Low-resource languages (sw, bn) show marginal probe selectivity (control task selectivity $\\sim$10\\,pp), warranting cautious interpretation. The Pareto frontier characterization assumes layer-wise probing with fixed representations; methods that modify representations (fine-tuning, adapters) may reshape the frontier.\n\n%====================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, revealing a depth--transferability Pareto frontier across three architectures and 20+ languages. CKA analysis identifies geometric misalignment as the mechanism, explaining why distributional matching (CaCLR) fails while linear projection succeeds with as few as 50 parallel pairs. The correctness--confidence orthogonality persists across all tested languages, confirming the structural necessity of probe-based calibration. For practitioners, the prescription is: probe at $\\sim$50\\% model depth and, if parallel data is available, apply linear projection rather than distributional matching.\n\n%====================================================================\n\n\\bibliography{custom}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Ahuja et al.}2024]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}\n\n%====================================================================\n\\appendix\n\n\\section{INT8 Validation}\n\\label{app:int8}\n\nWe validate INT8 quantization against FP16 on Llama~4 Scout at 5 representative layers using a 5\\% data subset. The maximum AUROC difference is 0.8\\,pp, mean difference 0.3\\,pp, with Pearson $r = 0.997$ between INT8 and FP16 probe scores. Rank agreement is 98\\%. All differences fall within bootstrap confidence intervals, confirming INT8 does not distort correctness signals.\n\n\\section{Probe Complexity}\n\\label{app:probe_complexity}\n\nMLP probes (2-layer) achieve 2.5\\,pp higher English AUROC than logistic regression (0.835 vs.\\ 0.81 on Qwen3) but suffer 6\\,pp larger transfer gaps (0.17 vs.\\ 0.11). The MLP exploits English-specific nonlinearities that do not generalize cross-lingually. 80\\% of languages achieve better transfer with logistic regression, justifying our linear probe choice and reinforcing the geometric framing.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}\n\nResults replicate on Belebele (EN AUROC: 0.78, ZS median: 0.68, $\\rho$: $-0.48$) and MMLU-ProX (EN AUROC: 0.82, ZS median: 0.69, $\\rho$: $-0.50$). Per-language AUROC rank correlations with GlobalMMLU are 0.82 (Belebele) and 0.88 (MMLU-ProX). Method rankings are consistent across all three benchmarks, confirming CaCLR's $\\beta$ inertness is benchmark-independent.\n\n\\section{Control Task Selectivity}\n\\label{app:control}\n\nFollowing \\citet{hewitt2019control}, we train probes on randomly permuted labels. Control AUROC is 0.54--0.55 (near chance). Selectivity (probe AUROC minus control AUROC) is positive across all language--layer combinations: English median 26.5\\,pp, high-resource 20\\,pp, mid-resource 16\\,pp, low-resource 10\\,pp. 88\\% of combinations exceed 10\\,pp selectivity (95\\% for high-resource, 70\\% for low-resource). The weaker selectivity for low-resource languages is a genuine limitation: conclusions about sw/bn transfer should be interpreted with this caveat.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b2172b9-0ac0-4667-8e94-3fa38d6495f4",
  "isSidechain": false,
  "requestId": "req_011CbEUbV93xk9iBj1Z2CLF7",
  "type": "assistant",
  "uuid": "35f1fe28-2efb-429a-82c6-1bc24a7258cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHDnAic5ngdNKNNNu7NVLY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 41210,
      "output_tokens": 12446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1022,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12446,
          "cache_read_input_tokens": 41210,
          "cache_creation_input_tokens": 1022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1022
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

_source line 19 · 2026-05-20T20:51:06.568Z_

<details><summary>↩ Tool result · `toolu_013C1JyxQLEJcVVkcZFyTXv1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35f1fe28-2efb-429a-82c6-1bc24a7258cc",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "bc32f082-0e68-4847-aa0e-ded9344d4266",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\definecolor{improved}{rgb}{0.85,0.95,0.85}\n\\definecolor{degraded}{rgb}{0.95,0.85,0.85}\n\n\\title{Cross-Lingual Correctness Probes Reveal a Depth--Transferability\\\\Pareto Frontier: Distributional Matching Fails\\\\Where Linear Projection Succeeds}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nProbe-based calibration methods extract internal correctness signals from LLM representations, achieving strong results in English. Whether these signals transfer cross-lingually remains untested. We present the first systematic evaluation of cross-lingual correctness probe transfer across 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B), 20+ languages, and 5 transfer methods. We discover a \\emph{depth--transferability Pareto frontier}: deeper layers yield higher English calibration quality (AUROC up to 0.81) but degrade in cross-lingual zero-shot transfer (median Spearman $\\rho = -0.52$ between English AUROC and transfer AUROC). CKA analysis reveals the mechanism---geometric misalignment between language subspaces increases with depth ($r = 0.58$ between CKA similarity and transfer AUROC, explaining 34\\% of variance). We test CaCLR, a probe training objective augmenting BCE loss with MMD-based cross-lingual consistency, and show that the consistency term is \\emph{inert} across three orders of magnitude ($\\beta$ sweep: Cohen's $d = 0.08$, $p = 0.42$)---predicted by the geometric explanation, since MMD cannot correct representational rotations. In contrast, linear projection with as few as 50--100 parallel pairs achieves +3.5\\,pp AUROC over zero-shot transfer, precisely because it learns the rotation that distributional matching cannot. Correctness--confidence orthogonality (cosine $< 0.10$) persists across all 20 languages, confirming that output-based calibration is structurally limited regardless of language. Our results establish that probe-based cross-lingual calibration is viable for the majority of languages at mid-depth layers, close the distributional-matching path with both empirical evidence and mechanistic explanation, and identify linear projection as the practical solution.\n\\end{abstract}\n\n%====================================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models exhibit substantially worse calibration in non-English languages, with expected calibration error (ECE) degrading up to 5$\\times$ compared to English \\cite{ahuja2024globalmmlu,lai2024llmsurvey}. Recent work has shown that probe-based calibration---extracting internal correctness signals via linear probes on model representations---outperforms output-based methods in English \\cite{miao2026coral,burns2023discovering}. A key finding by \\citet{miao2026orthogonality} is that correctness and verbalized confidence directions are nearly orthogonal (cosine $< 0.04$) in English, establishing a structural limitation of output-based approaches. However, all existing probe-based calibration methods operate exclusively in English, leaving a fundamental question unanswered: \\emph{do these internal correctness signals transfer across languages?}\n\nThe answer is not obvious. Cross-lingual representation transfer has been studied extensively for tasks like NER and classification \\cite{pires2019multilingual,conneau2020unsupervised}, but correctness probes target a fundamentally different signal---output-dependent accuracy rather than input-level features. \\citet{xiao2025knowledgeboundary} transferred \\emph{knowledge boundary} probes (input-level answerability) across 8 languages, but answerability and correctness are distinct signals with potentially different cross-lingual alignment properties.\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, contributing four findings organized as a causal chain:\n\n\\paragraph{(1) Pareto Frontier.} We discover a depth--transferability tradeoff: deeper layers produce better English probes but transfer worse cross-lingually. The frontier shape is architecture-dependent (Spearman $\\rho$ ranging from $-0.51$ to $-0.58$ across three architectures).\n\n\\paragraph{(2) Mechanistic Explanation.} CKA analysis reveals that cross-lingual geometric similarity decreases with depth. The CKA--transfer correlation ($r = 0.58$) explains 34\\% of transfer variance, substantially outpredicting distributional measures like MMD (6\\%).\n\n\\paragraph{(3) Principled Negative Result.} CaCLR, a probe training objective with MMD-based cross-lingual consistency loss, fails to shift the Pareto frontier ($d = 0.08$). This is \\emph{predicted} by the geometric explanation: MMD matches marginal distributions but cannot correct the rotation of the correctness direction across language subspaces.\n\n\\paragraph{(4) Constructive Alternative.} Linear projection with $\\sim$50--100 parallel pairs achieves +3.5\\,pp over zero-shot, succeeding precisely because it learns the rotation that MMD cannot. The correctness--confidence orthogonality persists across all 20 languages, confirming the structural necessity of probe-based approaches.\n\nWe evaluate on GlobalMMLU \\cite{ahuja2024globalmmlu}, Belebele \\cite{bandarkar2023belebele}, and MMLU-ProX across 20 languages and 3 architectures (Qwen3-235B-A22B, Llama~4 Scout, Gemma~4 31B Dense), with camera-ready extensions to 52 languages.\n\n%====================================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Probe-Based Calibration.}\n\\citet{burns2023discovering} and \\citet{li2024inference} demonstrated that linear probes on internal representations can identify model knowledge states. CORAL \\cite{miao2026coral} extended this to cross-task English calibration. \\citet{miao2026orthogonality} showed correctness--confidence orthogonality and used steering to improve calibration. All are English-only.\n\n\\paragraph{Cross-Lingual Probe Transfer.}\n\\citet{xiao2025knowledgeboundary} transferred knowledge boundary probes across 8 languages, finding partial success. However, knowledge boundary (binary answerability) is an input-level property, while correctness depends on the model's actual output. \\citet{civelli2024difficulty} transferred difficulty probes cross-lingually---difficulty is a shared confound we explicitly control for. LACE \\cite{zhou2024lace} ensembles per-language probes but requires target-language labels.\n\n\\paragraph{Cross-Lingual Alignment.}\nMUSE \\cite{conneau2018muse} and VecMap \\cite{artetxe2018vecmap} achieve bilingual alignment with $\\sim$50--100 dictionary entries via linear mappings. Our linear projection's sample efficiency is consistent with this literature. The novel finding is that distributional matching (MMD, the natural choice from domain adaptation theory \\cite{bendavid2010theory}) fails for this specific alignment task.\n\n\\paragraph{Representation Similarity.}\nCKA \\cite{kornblith2019similarity} measures geometric similarity between representations. We use CKA to explain \\emph{why} transfer fails at depth---complementing prior work using CKA for layer-level analysis \\cite{nguyen2021wide}.\n\n\\paragraph{Conformal Prediction.}\nConformal methods \\cite{angelopoulos2023conformal} provide distribution-free coverage guarantees but require calibration data per language. Our approach targets zero-label transfer; the two are complementary.\n\n%====================================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Correctness Probes}\n\\label{sec:probes}\n\nGiven a multilingual MCQA dataset, we extract hidden representations $\\mathbf{h}_\\ell \\in \\mathbb{R}^d$ at layer $\\ell$ for each question, taking the last-token representation before answer generation. We train a logistic regression probe $f_\\ell(\\mathbf{h}) = \\sigma(\\mathbf{w}_\\ell^\\top \\mathbf{h} + b_\\ell)$ on English data to predict binary correctness (whether the model's selected answer matches the gold label). We evaluate via AUROC and ECE.\n\n\\paragraph{Cross-Lingual Transfer.}\nWe evaluate the English-trained probe on target-language representations without any adaptation (zero-shot transfer). We compare five transfer conditions:\n\n\\begin{enumerate}[itemsep=1pt,parsep=0pt]\n    \\item \\textbf{Zero-shot}: Direct application of the English probe.\n    \\item \\textbf{Mean-shift}: Center target representations to match English mean.\n    \\item \\textbf{Linear projection}: Learn an affine mapping $\\mathbf{h}_{\\text{tgt}} \\mapsto \\mathbf{W}\\mathbf{h}_{\\text{tgt}} + \\mathbf{b}$ from parallel pairs.\n    \\item \\textbf{Few-shot} (25/100): Train on small target-language labeled sets.\n    \\item \\textbf{CaCLR}: Our proposed training objective (\\S\\ref{sec:caclr}).\n\\end{enumerate}\n\n\\paragraph{Mean-Shift Rank Invariance.}\nUnder StandardScaler preprocessing and logistic regression, mean-shift adds a constant offset to all logits: $\\mathbf{w}^\\top (\\mathbf{h} + \\boldsymbol{\\delta}) + b = \\mathbf{w}^\\top \\mathbf{h} + (b + \\mathbf{w}^\\top \\boldsymbol{\\delta})$. Since AUROC depends only on ranking, $\\Delta\\text{AUROC} \\equiv 0$ mathematically. Our experiments confirm this ($\\Delta\\text{AUROC} = 0.000$ across all conditions).\n\n\\subsection{CaCLR: Calibration-Aware Cross-Lingual Regularization}\n\\label{sec:caclr}\n\nCaCLR augments the standard probe training objective with two regularization terms:\n\\begin{equation}\n\\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n\\end{equation}\nwhere $\\mathcal{L}_{\\text{SB-ECE}}$ is a differentiable smooth-binned ECE loss and $\\mathcal{L}_{\\text{consistency}}$ is an MMD-based term:\n\\begin{equation}\n\\mathcal{L}_{\\text{consistency}} = \\text{MMD}^2\\big(\\{f(\\mathbf{h}_i^{\\text{en}})\\}, \\{f(\\mathbf{h}_i^{\\text{tgt}})\\}\\big)\n\\end{equation}\ncomputed over parallel activations from GlobalMMLU train-split translations. This requires parallel \\emph{inputs} but zero target-language \\emph{labels}.\n\n\\subsection{Difficulty-Controlled Decomposition}\n\\label{sec:decomp}\n\nFollowing IRT-based difficulty estimation, we train a difficulty probe $g(\\mathbf{h}) = \\mathbf{v}^\\top \\mathbf{h} + c$ predicting item difficulty. We project out the difficulty direction: $\\mathbf{h}^{\\perp} = \\mathbf{h} - (\\mathbf{h}^\\top \\hat{\\mathbf{v}})\\hat{\\mathbf{v}}$, then retrain correctness probes on residuals. Improvement after difficulty removal indicates the capability-specific component drives transfer degradation.\n\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nWe compute linear CKA \\cite{kornblith2019similarity} between English and target-language representations at each probed layer:\n\\begin{equation}\n\\text{CKA}(\\mathbf{X}_{\\text{en}}, \\mathbf{X}_{\\text{tgt}}) = \\frac{\\|\\mathbf{X}_{\\text{en}}^\\top \\mathbf{X}_{\\text{tgt}}\\|_F^2}{\\|\\mathbf{X}_{\\text{en}}^\\top \\mathbf{X}_{\\text{en}}\\|_F \\cdot \\|\\mathbf{X}_{\\text{tgt}}^\\top \\mathbf{X}_{\\text{tgt}}\\|_F}\n\\end{equation}\nCKA captures geometric similarity (rotation, scaling), while MMD captures distributional distance. We correlate both with transfer AUROC to determine which type of misalignment drives transfer failure.\n\n%====================================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate three architectures: Qwen3-235B-A22B (94 layers, MoE, INT8), Llama~4 Scout (48 layers, MoE, INT8), and Gemma~4 31B (60 layers, dense, FP16). INT8 quantization is validated against FP16 (Appendix~\\ref{app:int8}).\n\n\\paragraph{Languages.}\nCore evaluation: 20 languages spanning 4 resource tiers and 8 language families (zh, es, fr, de, ar, hi, ru, ko, ja, pt, vi, tr, id, th, pl, uk, he, el, sw, bn). Camera-ready extension: 52 languages.\n\n\\paragraph{Datasets.}\nPrimary: GlobalMMLU \\cite{ahuja2024globalmmlu}. Generalization: Belebele \\cite{bandarkar2023belebele} and MMLU-ProX. Train/test splits follow standard protocols; CaCLR parallel activations use train split only.\n\n\\paragraph{Probing Layers.}\nWe probe 24 layers for Qwen3-235B (evenly spaced across 94 layers), 12 for Llama~4 Scout, and 15 for Gemma~4 31B.\n\n\\paragraph{Evaluation Metrics.}\nAUROC (primary, rank-based), ECE (secondary, calibration quality), paired permutation tests ($p < 0.05$), bootstrap 95\\% CIs (1000 resamples), Cohen's $d$ for effect sizes.\n\n%====================================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth--Transferability Pareto Frontier}\n\\label{sec:pareto}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pareto frontier summary across three architectures. EN\\textsubscript{best}: English optimal AUROC and layer. ZS\\textsubscript{med}: median zero-shot transfer AUROC at the best transfer layer. $\\rho$\\textsubscript{med}: median per-language Spearman correlation between English AUROC and transfer AUROC. $\\sigma_\\rho$: standard deviation of per-language $\\rho$.}\n\\label{tab:pareto_summary}\n\\begin{tabular}{lcccccc}\n\\toprule\n\\textbf{Architecture} & \\textbf{EN\\textsubscript{best}} & \\textbf{Layer} & \\textbf{ZS\\textsubscript{med}} & \\textbf{Xfer Layer} & \\textbf{$\\rho$\\textsubscript{med}} & \\textbf{$\\sigma_\\rho$} \\\\\n\\midrule\nQwen3-235B (MoE) & 0.81 & 72 & 0.70 & 48 & $-$0.51 & 0.16 \\\\\nLlama 4 Scout (MoE) & 0.79 & 36 & 0.68 & 24 & $-$0.54 & 0.15 \\\\\nGemma 4 31B (Dense) & 0.80 & 45 & 0.69 & 33 & $-$0.58 & 0.12 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:pareto_summary} presents the Pareto frontier across all three architectures. The key pattern is consistent: the English-optimal layer (72--76\\% depth) is \\emph{not} the transfer-optimal layer ($\\sim$50\\% depth) for most languages. The Spearman correlation between English AUROC and cross-lingual transfer AUROC is moderately negative across architectures ($\\rho$ median $-0.51$ to $-0.58$), confirming the depth--transferability tradeoff.\n\nThe architecture-dependent shape is visible in two contrasts. First, MoE models (Qwen3, Llama~4) show higher per-language $\\rho$ variance ($\\sigma_\\rho = 0.15$--$0.16$) than the dense model (Gemma~4, $\\sigma_\\rho = 0.12$), reflecting MoE routing's heterogeneous effect on cross-lingual alignment. Second, the per-language $\\rho$ range spans $[-0.82, -0.21]$ across models, with low-resource languages (sw: $\\rho \\approx -0.78$) showing stronger negative correlations than high-resource languages (zh: $\\rho \\approx -0.21$), indicating that representation divergence from English scales with both depth and pretraining exposure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Zero-shot transfer AUROC at the best transfer layer for 20 languages on Qwen3-235B-A22B. Languages grouped by resource tier.}\n\\label{tab:zs_by_lang}\n\\begin{tabular}{llc|llc}\n\\toprule\n\\textbf{Lang} & \\textbf{Tier} & \\textbf{AUROC} & \\textbf{Lang} & \\textbf{Tier} & \\textbf{AUROC} \\\\\n\\midrule\nzh & High & 0.74 & vi & Mid & 0.68 \\\\\nes & High & 0.73 & tr & Mid & 0.67 \\\\\nfr & High & 0.73 & id & Mid & 0.68 \\\\\nde & High & 0.72 & th & Mid & 0.66 \\\\\npt & High & 0.72 & pl & Mid & 0.69 \\\\\n\\midrule\nar & Mid & 0.70 & uk & Mid & 0.68 \\\\\nru & Mid & 0.71 & he & Mid & 0.66 \\\\\nhi & Mid & 0.69 & el & Mid & 0.65 \\\\\nko & Mid & 0.69 & sw & Low & 0.58 \\\\\nja & Mid & 0.70 & bn & Low & 0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:zs_by_lang} shows per-language zero-shot transfer AUROC at the best transfer layer for Qwen3-235B. Of 20 languages, 13 exceed the 0.65 AUROC threshold for usable calibration (11 for Llama~4 Scout). The resource-tier gradient is clear: high-resource languages cluster at 0.72--0.74, mid-resource at 0.65--0.71, and low-resource sw/bn fall below 0.60.\n\n\\subsection{CKA Reveals Geometric Misalignment}\n\\label{sec:cka_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CKA similarity between English and target languages at shallow (12) vs.\\ deep (72) layers on Qwen3-235B, grouped by resource tier. Pearson $r$ between CKA and transfer AUROC shown at bottom.}\n\\label{tab:cka}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Resource Tier} & \\textbf{CKA\\textsubscript{shallow}} & \\textbf{CKA\\textsubscript{deep}} \\\\\n\\midrule\nHigh (zh, es, fr, de, pt) & 0.88 & 0.60 \\\\\nMid (ar, ru, hi, ko, ja, ...) & 0.84 & 0.48 \\\\\nLow (sw, bn) & 0.78 & 0.36 \\\\\n\\midrule\nAll languages (median) & 0.84 & 0.52 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{4pt}\n\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Predictor} & \\textbf{Pearson $r$} & \\textbf{Variance Explained} \\\\\n\\midrule\nCKA (linear) & 0.58 & 34\\% \\\\\nMMD & 0.25 & 6\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nCKA similarity between English and target-language representations decreases significantly with depth ($p < 10^{-5}$; Table~\\ref{tab:cka}). The decline is steepest for low-resource languages (0.78 $\\to$ 0.36) and most gradual for high-resource languages (0.88 $\\to$ 0.60), mirroring the transfer AUROC gradient.\n\nThe CKA--transfer correlation ($r = 0.58$ pooled across both MoE models, $p < 10^{-5}$) explains 34\\% of transfer variance, substantially outpredicting MMD ($r = 0.25$, 6\\% variance explained). This asymmetry is the mechanistic key: if cross-lingual misalignment were distributional (mean/covariance shift), MMD would predict transfer comparably to CKA. The 5.7$\\times$ ratio in explained variance demonstrates that misalignment is geometric---the correctness direction \\emph{rotates} across language subspaces rather than merely shifting.\n\nThe dense model (Gemma~4 31B) shows steeper CKA decline with depth than both MoE models, consistent with MoE routing providing a modest buffer against geometric misalignment (different experts can maintain cross-lingual features at deeper layers).\n\n\\subsection{CaCLR: A Principled Negative Result}\n\\label{sec:caclr_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{CaCLR $\\beta$ sensitivity sweep: $\\Delta$AUROC over the $\\alpha$-only baseline ($\\beta = 0$, $\\alpha = 0.5$). Median across 20 languages on both architectures. No $\\beta$ value achieves statistical significance.}\n\\label{tab:beta_sweep}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\beta$ & \\textbf{Med $\\Delta$AUROC} & \\textbf{Std} & \\textbf{$p$} & \\textbf{$d$} & \\textbf{\\#Improved} \\\\\n\\midrule\n0 (baseline) & --- & --- & --- & --- & --- \\\\\n0.001 & +0.002 & 0.015 & 0.61 & 0.05 & 12/20 \\\\\n0.01 & +0.001 & 0.014 & 0.53 & 0.03 & 11/20 \\\\\n0.1 & $-$0.001 & 0.016 & 0.48 & 0.04 & 9/20 \\\\\n1.0 & $-$0.003 & 0.018 & 0.35 & 0.10 & 7/20 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall $\\beta$ effect:} & & \\textbf{0.42} & \\textbf{0.08} & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\beta$ (consistency loss) term in CaCLR is inert across three orders of magnitude (Table~\\ref{tab:beta_sweep}). The overall effect size is negligible (Cohen's $d = 0.08$, $p = 0.42$). This inertness is consistent across resource tiers: high-resource languages see $\\Delta = +0.004$, mid-resource $\\Delta = 0.000$, low-resource $\\Delta = -0.002$---none significant. The $\\alpha$-only variant (SB-ECE regularization) provides a small calibration improvement (ECE reduction of 0.7\\,pp) without AUROC degradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Transfer method comparison: median $\\Delta$AUROC over zero-shot across 20 languages. All methods at per-language oracle layer. Paired permutation test against zero-shot baseline.}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Qwen3} & \\textbf{Llama4} & \\textbf{$p$} & \\textbf{$d$} \\\\\n\\midrule\nMean-shift & 0.000 & 0.000 & --- & --- \\\\\nCaCLR ($\\alpha$-only) & +0.005 & +0.005 & 0.18 & 0.12 \\\\\nCaCLR (full) & +0.012 & +0.010 & 0.08 & 0.15 \\\\\nLinear projection & \\textbf{+0.035} & \\textbf{+0.032} & \\textbf{0.001} & \\textbf{0.55} \\\\\nFew-shot (25) & +0.025 & +0.022 & 0.005 & 0.40 \\\\\nFew-shot (100) & +0.045 & +0.040 & $<$0.001 & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:method_comparison} shows the full method ranking, consistent across both architectures: few-shot-100 $>$ linear-projection $>$ few-shot-25 $>$ CaCLR $>$ zero-shot $>$ mean-shift. Linear projection achieves +3.5\\,pp (Qwen3) and +3.2\\,pp (Llama~4) with strong statistical significance ($p = 0.001$, $d = 0.55$), while CaCLR's full improvement (+1.2\\,pp) comes entirely from $\\alpha$-term calibration regularization, not from cross-lingual consistency.\n\nThe CKA analysis (\\S\\ref{sec:cka_results}) provides the explanation: MMD optimizes distributional matching, but the misalignment is geometric (rotation/scaling). Linear projection succeeds because it directly estimates and corrects this rotation via a learned affine transformation on parallel pairs.\n\n\\subsection{Linear Projection Sample Efficiency}\n\\label{sec:linproj}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Linear projection $\\Delta$AUROC over zero-shot as a function of parallel pair count. Median across 20 languages, both models. Saturation knee at $\\sim$70 pairs.}\n\\label{tab:linproj_pairs}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Pairs} & \\textbf{Med $\\Delta$AUROC} & \\textbf{Std} & \\textbf{\\% of Max} \\\\\n\\midrule\n10 & +0.012 & 0.025 & 33\\% \\\\\n20 & +0.022 & 0.018 & 61\\% \\\\\n50 & +0.030 & 0.012 & 83\\% \\\\\n100 & +0.035 & 0.008 & 97\\% \\\\\n200 & +0.036 & 0.007 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nLinear projection shows rapid saturation (Table~\\ref{tab:linproj_pairs}), reaching 90\\% of maximum improvement at $\\sim$55 pairs and 95\\% at $\\sim$85 pairs. The knee point is $\\sim$70 pairs, consistent with the cross-lingual alignment literature where 50--100 bilingual dictionary entries suffice for word-level alignment \\cite{conneau2018muse,artetxe2018vecmap}. The saturation pattern is consistent across architectures (Qwen3 knee: 65 pairs; Llama~4: 75 pairs).\n\nThe practical implication is that $\\sim$50--100 parallel pairs (trivially obtainable from GlobalMMLU's train split or any parallel MCQA corpus) are sufficient to match or exceed CaCLR's entire training pipeline, while requiring no distributional matching, no hyperparameter tuning of $\\alpha$/$\\beta$, and providing a transparent geometric interpretation.\n\n\\subsection{Difficulty-Controlled Decomposition}\n\\label{sec:decomp_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Decomposition results: percentage of language--layer combinations improved by difficulty removal, grouped by layer depth and resource tier. Random-direction control shown for comparison.}\n\\label{tab:decomp}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{\\% Improved} & \\textbf{Med $\\Delta$AUROC} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{By depth}} \\\\\n\\quad Shallow layers & 50\\% & +0.005 \\\\\n\\quad Deep layers & 78\\% & +0.020 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\emph{By resource tier}} \\\\\n\\quad High-resource & 72\\% & +0.018 \\\\\n\\quad Mid-resource & 65\\% & +0.012 \\\\\n\\quad Low-resource & 53\\% & +0.006 \\\\\n\\midrule\nOverall & 65\\% & +0.012 \\\\\nRandom direction & 50\\% & +0.003 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRemoving the difficulty direction improves transfer in 65\\% of language--layer combinations (Table~\\ref{tab:decomp}; $p = 0.03$, $d = 0.28$). The improvement concentrates at deep layers (78\\% vs.\\ 50\\% at shallow layers), consistent with the CKA finding: at depth, the capability-specific component---which is geometrically misaligned across languages---drives transfer failure. Removing the shared difficulty signal isolates this effect.\n\nThe random-direction control (50\\% improved, $\\Delta = +0.003$, not significant) confirms that the improvement is specific to difficulty removal, not an artifact of dimensionality reduction. The difficulty and correctness directions have moderate cosine similarity (median 0.18, range [0.08, 0.30]), indicating partial but not full entanglement.\n\n\\subsection{Cross-Lingual Orthogonality}\n\\label{sec:orthogonality}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cosine similarity between correctness and verbalized confidence directions across languages and resource tiers. All values below the 0.12 orthogonality threshold.}\n\\label{tab:orthogonality}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Cosine (Qwen3)} & \\textbf{Cosine (Llama4)} \\\\\n\\midrule\nEnglish & 0.035 & 0.038 \\\\\n\\midrule\nHigh-resource (med) & 0.040 & 0.042 \\\\\nMid-resource (med) & 0.060 & 0.063 \\\\\nLow-resource (med) & 0.085 & 0.088 \\\\\n\\midrule\nAll languages (med) & 0.055 & 0.060 \\\\\nMax (sw) & 0.100 & 0.098 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe correctness--confidence orthogonality discovered by \\citet{miao2026orthogonality} in English (cosine $< 0.04$) extends to all 20 languages (Table~\\ref{tab:orthogonality}), with all cosine similarities below 0.10. However, a resource-tier gradient emerges: high-resource languages maintain tighter orthogonality (median 0.04) than low-resource languages (median 0.085), with a significant correlation between cosine and resource level (Spearman $\\rho = 0.52$, $p = 0.018$).\n\nEven the maximum cosine (0.10 for Swahili) is far below the $\\sim$0.5+ threshold that would indicate meaningful alignment between correctness and confidence signals. This confirms that output-based calibration is structurally limited across all languages---probe-based approaches are the appropriate paradigm regardless of language, though the cross-lingual \\emph{transfer} of these probes remains the bottleneck.\n\n\\subsection{Three-Architecture Comparison}\n\\label{sec:arch}\n\nThe Gemma~4 31B Dense results (Table~\\ref{tab:pareto_summary}) provide the critical dense-vs-MoE contrast. Dense models show smoother Pareto frontiers ($\\sigma_\\rho = 0.12$ vs.\\ 0.15--0.16 for MoE) because every token passes through every layer, creating more uniform layer-to-layer transformations. The dense model's $\\rho$ is slightly more negative ($-0.58$) and CKA declines more steeply with depth, confirming that MoE routing provides a modest buffer against geometric misalignment. All three architectures agree on the key finding: mid-depth layers ($\\sim$50\\% depth) are the right operating point for cross-lingual transfer.\n\n\\subsection{Extended Language Coverage}\n\\label{sec:extended}\n\nExtending to 52 languages, 28 (54\\%) exceed 0.65 AUROC in zero-shot transfer. The median drops to 0.66 (vs.\\ 0.70 for the curated 20), reflecting the disproportionately low-resource nature of additional languages. Five extremely low-resource languages (Amharic, Myanmar, Zulu, Shona, Kinyarwanda) fall below 0.55, approaching chance. The Pareto $\\rho$ weakens slightly ($-0.49$) due to noisier correlations in low-resource languages. Linear projection improvement remains consistent (+3.1\\,pp), confirming the geometric correction generalizes. With linear projection, viability extends to $\\sim$35/52 languages (67\\%).\n\n%====================================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why Does Distributional Matching Fail?}\nCaCLR's $\\beta$ inertness is not a hyperparameter failure---it is a fundamental limitation of distributional matching for this alignment task. MMD penalizes differences in mean embeddings and kernel-space moments, aligning \\emph{marginal distributions} without correcting the \\emph{rotation of the correctness direction} across language subspaces. At low $\\beta$, the MMD signal is too weak; at medium $\\beta$, the gradient pushes distributional alignment without targeting the correctness-relevant subspace; at high $\\beta$, the MMD term dominates and distorts the probe. CKA's superiority as a transfer predictor (34\\% vs.\\ 6\\% variance explained) confirms the geometric nature of misalignment.\n\n\\paragraph{The Linear Projection Connection.}\nLinear projection succeeds because it directly estimates the rotation matrix mapping source to target representational spaces. The sample complexity is low ($\\sim$50--100 pairs) because the correctness-relevant subspace is much lower-dimensional than the full representation space. This is consistent with VecMap/MUSE results for word embeddings, extended here to sentence-level correctness representations.\n\n\\paragraph{Limitations.}\nOur evaluation is limited to MCQA tasks, which enable clean correctness labeling. Extension to open-ended generation requires different correctness definitions. Low-resource languages (sw, bn) show marginal probe selectivity (control task selectivity $\\sim$10\\,pp), warranting cautious interpretation. The Pareto frontier characterization assumes layer-wise probing with fixed representations; methods that modify representations (fine-tuning, adapters) may reshape the frontier.\n\n%====================================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe present the first systematic evaluation of cross-lingual correctness probe transfer, revealing a depth--transferability Pareto frontier across three architectures and 20+ languages. CKA analysis identifies geometric misalignment as the mechanism, explaining why distributional matching (CaCLR) fails while linear projection succeeds with as few as 50 parallel pairs. The correctness--confidence orthogonality persists across all tested languages, confirming the structural necessity of probe-based calibration. For practitioners, the prescription is: probe at $\\sim$50\\% model depth and, if parallel data is available, apply linear projection rather than distributional matching.\n\n%====================================================================\n\n\\bibliography{custom}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Ahuja et al.}2024]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}\n\n%====================================================================\n\\appendix\n\n\\section{INT8 Validation}\n\\label{app:int8}\n\nWe validate INT8 quantization against FP16 on Llama~4 Scout at 5 representative layers using a 5\\% data subset. The maximum AUROC difference is 0.8\\,pp, mean difference 0.3\\,pp, with Pearson $r = 0.997$ between INT8 and FP16 probe scores. Rank agreement is 98\\%. All differences fall within bootstrap confidence intervals, confirming INT8 does not distort correctness signals.\n\n\\section{Probe Complexity}\n\\label{app:probe_complexity}\n\nMLP probes (2-layer) achieve 2.5\\,pp higher English AUROC than logistic regression (0.835 vs.\\ 0.81 on Qwen3) but suffer 6\\,pp larger transfer gaps (0.17 vs.\\ 0.11). The MLP exploits English-specific nonlinearities that do not generalize cross-lingually. 80\\% of languages achieve better transfer with logistic regression, justifying our linear probe choice and reinforcing the geometric framing.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}\n\nResults replicate on Belebele (EN AUROC: 0.78, ZS median: 0.68, $\\rho$: $-0.48$) and MMLU-ProX (EN AUROC: 0.82, ZS median: 0.69, $\\rho$: $-0.50$). Per-language AUROC rank correlations with GlobalMMLU are 0.82 (Belebele) and 0.88 (MMLU-ProX). Method rankings are consistent across all three benchmarks, confirming CaCLR's $\\beta$ inertness is benchmark-independent.\n\n\\section{Control Task Selectivity}\n\\label{app:control}\n\nFollowing \\citet{hewitt2019control}, we train probes on randomly permuted labels. Control AUROC is 0.54--0.55 (near chance). Selectivity (probe AUROC minus control AUROC) is positive across all language--layer combinations: English median 26.5\\,pp, high-resource 20\\,pp, mid-resource 16\\,pp, low-resource 10\\,pp. 88\\% of combinations exceed 10\\,pp selectivity (95\\% for high-resource, 70\\% for low-resource). The weaker selectivity for low-resource languages is a genuine limitation: conclusions about sw/bn transfer should be interpreted with this caveat.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "35f1fe28-2efb-429a-82c6-1bc24a7258cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "bc32f082-0e68-4847-aa0e-ded9344d4266",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Tool call

_source line 22 · 2026-05-20T20:51:12.451Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015ANUAXTjCx8noouYWgZXb9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc32f082-0e68-4847-aa0e-ded9344d4266",
  "isSidechain": false,
  "requestId": "req_011CbEUtv3EPeHxibEJPQ6Xf",
  "type": "assistant",
  "uuid": "4888aa29-07e3-42b4-96c7-ddff00eb48b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRc6ShKSfcJDekV8V98Lyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12513,
      "cache_read_input_tokens": 42232,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 181,
          "cache_read_input_tokens": 42232,
          "cache_creation_input_tokens": 12513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12513
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

_source line 23 · 2026-05-20T20:51:12.597Z_

<details><summary>↩ Tool result · reported error · `toolu_015ANUAXTjCx8noouYWgZXb9`</summary>

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
  "parentUuid": "4888aa29-07e3-42b4-96c7-ddff00eb48b9",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "08e99b2a-6763-4346-a0b4-66e877e66425",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "4888aa29-07e3-42b4-96c7-ddff00eb48b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T20:51:18.207Z_

<details><summary>Logged reasoning block</summary>

```text
Need to use a different document class. Let me check what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08e99b2a-6763-4346-a0b4-66e877e66425",
  "isSidechain": false,
  "requestId": "req_011CbEUuMo2tLWfXv9gfFnyW",
  "type": "assistant",
  "uuid": "a2c7d96a-4ae7-4eae-8263-a5181c87c37a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT5QBWbHoxyz2RRoy2jSb4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 54745,
      "output_tokens": 520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 520,
          "cache_read_input_tokens": 54745,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 25 · 2026-05-20T20:51:18.244Z_

No `acl.sty` available. Let me switch to a standard article class.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2c7d96a-4ae7-4eae-8263-a5181c87c37a",
  "isSidechain": false,
  "requestId": "req_011CbEUuMo2tLWfXv9gfFnyW",
  "type": "assistant",
  "uuid": "bd821fb9-8e91-4a3a-ae5b-977cf49d53ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT5QBWbHoxyz2RRoy2jSb4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 54745,
      "output_tokens": 520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 520,
          "cache_read_input_tokens": 54745,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 26 · 2026-05-20T20:51:20.742Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LM1sT19J2aKSCDXqj8tNQw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\citename}[1]{#1}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd821fb9-8e91-4a3a-ae5b-977cf49d53ab",
  "isSidechain": false,
  "requestId": "req_011CbEUuMo2tLWfXv9gfFnyW",
  "type": "assistant",
  "uuid": "db6517b5-5cd5-492a-8145-f7c2bdef967c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT5QBWbHoxyz2RRoy2jSb4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 475,
      "cache_read_input_tokens": 54745,
      "output_tokens": 520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 520,
          "cache_read_input_tokens": 54745,
          "cache_creation_input_tokens": 475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 475
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

_source line 27 · 2026-05-20T20:51:20.756Z_

<details><summary>↩ Tool result · `toolu_01LM1sT19J2aKSCDXqj8tNQw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6517b5-5cd5-492a-8145-f7c2bdef967c",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "b0e87636-c165-4fba-953e-fb12dd788836",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{colortbl}\n\\usepackage{array}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}\n\\usepackage{natbib}\n\\renewcommand{\\citename}[1]{#1}",
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
          "+\\usepackage[margin=2.5cm]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{amsmath}"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 6,
        "newStart": 12,
        "newLines": 9,
        "lines": [
          " \\usepackage{array}",
          " \\usepackage{tabularx}",
          " \\usepackage{enumitem}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
          "+\\usepackage{natbib}",
          "+\\renewcommand{\\citename}[1]{#1}",
          " ",
          " \\definecolor{improved}{rgb}{0.85,0.95,0.85}",
          " \\definecolor{degraded}{rgb}{0.95,0.85,0.85}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "db6517b5-5cd5-492a-8145-f7c2bdef967c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T20:51:27.332Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hzw5n9XTvbGf2eeKcqGUN3`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "Compile LaTeX paper twice",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0e87636-c165-4fba-953e-fb12dd788836",
  "isSidechain": false,
  "requestId": "req_011CbEUuxZ4w8zk5ZdDUSjv8",
  "type": "assistant",
  "uuid": "0fef9bdd-c145-41c6-84eb-a21b14eeab8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QihNP6W5KP4iHaRkY41FoK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 55220,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 55220,
          "cache_creation_input_tokens": 607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 607
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

_source line 29 · 2026-05-20T20:51:27.871Z_

<details><summary>↩ Tool result · reported error · `toolu_01Hzw5n9XTvbGf2eeKcqGUN3`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/colortbl/colortbl.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `ahuja2024globalmmlu' on page 1 undefined on i
nput line 37.


Package natbib Warning: Citation `lai2024llmsurvey' on page 1 undefined on inpu
t line 37.


Package natbib Warning: Citation `miao2026coral' on page 1 undefined on input l
ine 37.


Package natbib Warning: Citation `burns2023discovering' on page 1 undefined on 
input line 37.


Package natbib Warning: Citation `miao2026orthogonality' on page 1 undefined on
 input line 37.


Package natbib Warning: Citation `pires2019multilingual' on page 1 undefined on
 input line 39.


Package natbib

... [5414 characters truncated] ...

18muse}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {conneau2020unsupervised}
l.438 ...eau et al.}2020]{conneau2020unsupervised}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {hewitt2019control}
l.443 ...Hewitt and Liang}2019]{hewitt2019control}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {kornblith2019similarity}
l.448 ...ith et al.}2019]{kornblith2019similarity}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {lai2024llmsurvey}
l.453 ...tename{Lai et al.}2024]{lai2024llmsurvey}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {li2024inference}
l.458 ...citename{Li et al.}2024]{li2024inference}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {miao2026coral}
l.463 ...itename{Miao et al.}2026a]{miao2026coral}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {miao2026orthogonality}
l.468 ...ao and Ungar}2026]{miao2026orthogonality}
                                                  
[9]
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {nguyen2021wide}
l.473 ...ename{Nguyen et al.}2021]{nguyen2021wide}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {pires2019multilingual}
l.478 ...Pires et al.}2019]{pires2019multilingual}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {raghu2017svcca}
l.483 ...tename{Raghu et al.}2017]{raghu2017svcca}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {voita2020mdl}
l.488 ...ename{Voita and Titov}2020]{voita2020mdl}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {xiao2025knowledgeboundary}
l.493 ...o et al.}2025]{xiao2025knowledgeboundary}
                                                  
! Undefined control sequence.
&lt;argument> ...ter \NAT@ifcmd \NAT@tmp (@)(@)\@nil 
                                                  {zhou2024lace}
l.498 ...\citename{Zhou et al.}2024]{zhou2024lace}
                                                  

Package natbib Warning: Citation `hewitt2019control' on page 10 undefined on in
put line 526.

[10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux)

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
blic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmri8a.pfb>
Output written on paper.pdf (11 pages, 184266 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fef9bdd-c145-41c6-84eb-a21b14eeab8a",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "f8bd3324-f8a8-4215-aba2-3af88d04a205",
  "toolUseResult": "Error: Exit code 1\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/colortbl/colortbl.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `ahuja2024globalmmlu' on page 1 undefined on i\nnput line 37.\n\n\nPackage natbib Warning: Citation `lai2024llmsurvey' on page 1 undefined on inpu\nt line 37.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 1 undefined on input l\nine 37.\n\n\nPackage natbib Warning: Citation `burns2023discovering' on page 1 undefined on \ninput line 37.\n\n\nPackage natbib Warning: Citation `miao2026orthogonality' on page 1 undefined on\n input line 37.\n\n\nPackage natbib Warning: Citation `pires2019multilingual' on page 1 undefined on\n input line 39.\n\n\nPackage natbib\n\n... [5414 characters truncated] ...\n\n18muse}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {conneau2020unsupervised}\nl.438 ...eau et al.}2020]{conneau2020unsupervised}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {hewitt2019control}\nl.443 ...Hewitt and Liang}2019]{hewitt2019control}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {kornblith2019similarity}\nl.448 ...ith et al.}2019]{kornblith2019similarity}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {lai2024llmsurvey}\nl.453 ...tename{Lai et al.}2024]{lai2024llmsurvey}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {li2024inference}\nl.458 ...citename{Li et al.}2024]{li2024inference}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {miao2026coral}\nl.463 ...itename{Miao et al.}2026a]{miao2026coral}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {miao2026orthogonality}\nl.468 ...ao and Ungar}2026]{miao2026orthogonality}\n                                                  \n[9]\n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {nguyen2021wide}\nl.473 ...ename{Nguyen et al.}2021]{nguyen2021wide}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {pires2019multilingual}\nl.478 ...Pires et al.}2019]{pires2019multilingual}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {raghu2017svcca}\nl.483 ...tename{Raghu et al.}2017]{raghu2017svcca}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {voita2020mdl}\nl.488 ...ename{Voita and Titov}2020]{voita2020mdl}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {xiao2025knowledgeboundary}\nl.493 ...o et al.}2025]{xiao2025knowledgeboundary}\n                                                  \n! Undefined control sequence.\n&lt;argument> ...ter \\NAT@ifcmd \\NAT@tmp (@)(@)\\@nil \n                                                  {zhou2024lace}\nl.498 ...\\citename{Zhou et al.}2024]{zhou2024lace}\n                                                  \n\nPackage natbib Warning: Citation `hewitt2019control' on page 10 undefined on in\nput line 526.\n\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmri8a.pfb>\nOutput written on paper.pdf (11 pages, 184266 bytes).\nTranscript written on paper.log.",
  "sourceToolAssistantUUID": "0fef9bdd-c145-41c6-84eb-a21b14eeab8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T20:51:27.877Z_

```json
{
  "parentUuid": "f8bd3324-f8a8-4215-aba2-3af88d04a205",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1989b92a-9202-4c2a-bf78-1661de1aa732",
  "timestamp": "2026-05-20T20:51:27.877Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "1989b92a-9202-4c2a-bf78-1661de1aa732",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Assistant

_source line 33 · 2026-05-20T20:51:32.299Z_

<details><summary>Logged reasoning block</summary>

```text
The issue is with the `\citename` usage in `thebibliography` - it's an ACL-specific command. Since I'm using natbib, the `\protect\citename` syntax doesn't work with natbib's `thebibliography`. Let me fix this by using a simpler bibliography format that works with natbib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1989b92a-9202-4c2a-bf78-1661de1aa732",
  "isSidechain": false,
  "requestId": "req_011CbEUvV297WwkV1rxjkruH",
  "type": "assistant",
  "uuid": "2d6de7f1-96b7-43d1-a75c-16007a2b5c2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLnpfbggqCpC7gMWG9zQk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4194,
      "cache_read_input_tokens": 55827,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 55827,
          "cache_creation_input_tokens": 4194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4194
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

_source line 34 · 2026-05-20T20:51:33.724Z_

The PDF was generated (11 pages, 184KB) but with natbib citation warnings due to `\citename` in the bibliography entries. Let me fix the bibliography format to work with natbib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6de7f1-96b7-43d1-a75c-16007a2b5c2d",
  "isSidechain": false,
  "requestId": "req_011CbEUvV297WwkV1rxjkruH",
  "type": "assistant",
  "uuid": "544fa62a-fbb7-43af-b489-1ff48b3275cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLnpfbggqCpC7gMWG9zQk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4194,
      "cache_read_input_tokens": 55827,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 55827,
          "cache_creation_input_tokens": 4194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4194
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

_source line 35 · 2026-05-20T20:51:36.468Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qc9QBh15PdGUST2vfs9Jdt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "offset": 410,
  "limit": 110
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "544fa62a-fbb7-43af-b489-1ff48b3275cb",
  "isSidechain": false,
  "requestId": "req_011CbEUvV297WwkV1rxjkruH",
  "type": "assistant",
  "uuid": "cb9f3ce2-a2b5-470a-ac0e-4b6cc61c1a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YLnpfbggqCpC7gMWG9zQk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4194,
      "cache_read_input_tokens": 55827,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 55827,
          "cache_creation_input_tokens": 4194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4194
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

_source line 36 · 2026-05-20T20:51:36.474Z_

<details><summary>↩ Tool result · `toolu_01Qc9QBh15PdGUST2vfs9Jdt`</summary>

```text
410	\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.
411	\newblock In \emph{Proceedings of ACL}, pages 789--798.
412	
413	\bibitem[\protect\citename{Bandarkar et al.}2023]{bandarkar2023belebele}
414	Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.
415	\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.
416	\newblock \emph{arXiv preprint arXiv:2308.16884}.
417	
418	\bibitem[\protect\citename{Ben-David et al.}2010]{bendavid2010theory}
419	Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.
420	\newblock A theory of learning from different domains.
421	\newblock \emph{Machine Learning}, 79(1):151--175.
422	
423	\bibitem[\protect\citename{Burns et al.}2023]{burns2023discovering}
424	Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.
425	\newblock Discovering latent knowledge in language models without supervision.
426	\newblock In \emph{Proceedings of ICLR}.
427	
428	\bibitem[\protect\citename{Civelli et al.}2024]{civelli2024difficulty}
429	Andrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.
430	\newblock Cross-lingual transfer of difficulty representations in multilingual language models.
431	\newblock In \emph{Proceedings of EMNLP}, pages 4521--4535.
432	
433	\bibitem[\protect\citename{Conneau et al.}2018]{conneau2018muse}
434	Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\'e} J{\'e}gou. 2018.
435	\newblock Word translation without parallel data.
436	\newblock In \emph{Proceedings of ICLR}.
437	
438	\bibitem[\protect\citename{Conneau et al.}2020]{conneau2020unsupervised}
439	Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.
440	\newblock Unsupervised cross-lingual representation learning at scale.
441	\newblock In \emph{Proceedings of ACL}, pages 8440--8451.
442	
443	\bibitem[\protect\citename{Hewitt and Liang}2019]{hewitt2019control}
444	John Hewitt and Percy Liang. 2019.
445	\newblock Designing and interpreting probes with control tasks.
446	\newblock In \emph{Proceedings of EMNLP}, pages 2733--2743.
447	
448	\bibitem[\protect\citename{Kornblith et al.}2019]{kornblith2019similarity}
449	Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.
450	\newblock Similarity of neural network representations revisited.
451	\newblock In \emph{Proceedings of ICML}, pages 3519--3529.
452	
453	\bibitem[\protect\citename{Lai et al.}2024]{lai2024llmsurvey}
454	Yuxuan Lai, Xingchen Li, and Yansong Feng. 2024.
455	\newblock LLM calibration and alignment: A survey and its connection to RLHF.
456	\newblock \emph{arXiv preprint arXiv:2404.01076}.
457	
458	\bibitem[\protect\citename{Li et al.}2024]{li2024inference}
459	Kenneth Li, Oam Patel, Fernanda Vi{\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.
460	\newblock Inference-time intervention: Eliciting truthful answers from a language model.
461	\newblock In \emph{Proceedings of NeurIPS}.
462	
463	\bibitem[\protect\citename{Miao et al.}2026a]{miao2026coral}
464	Qinyu Miao, Alex Wang, and Mark Johnson. 2026a.
465	\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.
466	\newblock In \emph{Proceedings of ACL}, pages 1823--1840.
467	
468	\bibitem[\protect\citename{Miao and Ungar}2026]{miao2026orthogonality}
469	Qinyu Miao and Lyle Ungar. 2026.
470	\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.
471	\newblock In \emph{Proceedings of NAACL}, pages 2941--2958.
472	
473	\bibitem[\protect\citename{Nguyen et al.}2021]{nguyen2021wide}
474	Thao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.
475	\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.
476	\newblock In \emph{Proceedings of ICLR}.
477	
478	\bibitem[\protect\citename{Pires et al.}2019]{pires2019multilingual}
479	Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.
480	\newblock How multilingual is multilingual {BERT}?
481	\newblock In \emph{Proceedings of ACL}, pages 4996--5001.
482	
483	\bibitem[\protect\citename{Raghu et al.}2017]{raghu2017svcca}
484	Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.
485	\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.
486	\newblock In \emph{Proceedings of NeurIPS}, pages 6076--6085.
487	
488	\bibitem[\protect\citename{Voita and Titov}2020]{voita2020mdl}
489	Elena Voita and Ivan Titov. 2020.
490	\newblock Information-theoretic probing with minimum description length.
491	\newblock In \emph{Proceedings of EMNLP}, pages 183--196.
492	
493	\bibitem[\protect\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}
494	Shiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.
495	\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.
496	\newblock In \emph{Proceedings of ACL}, pages 5312--5328.
497	
498	\bibitem[\protect\citename{Zhou et al.}2024]{zhou2024lace}
499	Wenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.
500	\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.
501	\newblock In \emph{Proceedings of EMNLP}, pages 7823--7838.
502	
503	\end{thebibliography}
504	
505	%====================================================================
506	\appendix
507	
508	\section{INT8 Validation}
509	\label{app:int8}
510	
511	We validate INT8 quantization against FP16 on Llama~4 Scout at 5 representative layers using a 5\% data subset. The maximum AUROC difference is 0.8\,pp, mean difference 0.3\,pp, with Pearson $r = 0.997$ between INT8 and FP16 probe scores. Rank agreement is 98\%. All differences fall within bootstrap confidence intervals, confirming INT8 does not distort correctness signals.
512	
513	\section{Probe Complexity}
514	\label{app:probe_complexity}
515	
516	MLP probes (2-layer) achieve 2.5\,pp higher English AUROC than logistic regression (0.835 vs.\ 0.81 on Qwen3) but suffer 6\,pp larger transfer gaps (0.17 vs.\ 0.11). The MLP exploits English-specific nonlinearities that do not generalize cross-lingually. 80\% of languages achieve better transfer with logistic regression, justifying our linear probe choice and reinforcing the geometric framing.
517	
518	\section{Cross-Benchmark Generalization}
519	\label{app:benchmarks}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb9f3ce2-a2b5-470a-ac0e-4b6cc61c1a21",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "1df7193a-ccc4-492a-91d2-2d2724cff008",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
      "content": "\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}\n\n%====================================================================\n\\appendix\n\n\\section{INT8 Validation}\n\\label{app:int8}\n\nWe validate INT8 quantization against FP16 on Llama~4 Scout at 5 representative layers using a 5\\% data subset. The maximum AUROC difference is 0.8\\,pp, mean difference 0.3\\,pp, with Pearson $r = 0.997$ between INT8 and FP16 probe scores. Rank agreement is 98\\%. All differences fall within bootstrap confidence intervals, confirming INT8 does not distort correctness signals.\n\n\\section{Probe Complexity}\n\\label{app:probe_complexity}\n\nMLP probes (2-layer) achieve 2.5\\,pp higher English AUROC than logistic regression (0.835 vs.\\ 0.81 on Qwen3) but suffer 6\\,pp larger transfer gaps (0.17 vs.\\ 0.11). The MLP exploits English-specific nonlinearities that do not generalize cross-lingually. 80\\% of languages achieve better transfer with logistic regression, justifying our linear probe choice and reinforcing the geometric framing.\n\n\\section{Cross-Benchmark Generalization}\n\\label{app:benchmarks}",
      "numLines": 110,
      "startLine": 410,
      "totalLines": 529
    }
  },
  "sourceToolAssistantUUID": "cb9f3ce2-a2b5-470a-ac0e-4b6cc61c1a21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T20:51:42.616Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NYfr47Q8XzHKXSKQQtM8oC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "old_string": "\\usepackage{natbib}\n\\renewcommand{\\citename}[1]{#1}",
  "new_string": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\\newcommand{\\citename}[1]{#1}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df7193a-ccc4-492a-91d2-2d2724cff008",
  "isSidechain": false,
  "requestId": "req_011CbEUw89JiXHPwduQuDZpv",
  "type": "assistant",
  "uuid": "ab70ae94-4a16-43aa-877f-bea6bf7c8645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WYEBGjpByu1inmYCgwqHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2746,
      "cache_read_input_tokens": 60021,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 60021,
          "cache_creation_input_tokens": 2746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2746
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

_source line 38 · 2026-05-20T20:51:42.735Z_

<details><summary>↩ Tool result · `toolu_01NYfr47Q8XzHKXSKQQtM8oC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab70ae94-4a16-43aa-877f-bea6bf7c8645",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "a70dc666-80b5-4cdf-8ec8-a3ea54ad1ff8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
    "oldString": "\\usepackage{natbib}\n\\renewcommand{\\citename}[1]{#1}",
    "newString": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\\newcommand{\\citename}[1]{#1}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 8,
        "lines": [
          " \\usepackage{enumitem}",
          " \\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
          " \\usepackage{natbib}",
          "-\\renewcommand{\\citename}[1]{#1}",
          "+\\bibliographystyle{plainnat}",
          "+\\newcommand{\\citename}[1]{#1}",
          " ",
          " \\definecolor{improved}{rgb}{0.85,0.95,0.85}",
          " \\definecolor{degraded}{rgb}{0.95,0.85,0.85}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ab70ae94-4a16-43aa-877f-bea6bf7c8645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T20:51:46.738Z_

Now fix the `\bibitem` entries to use natbib-compatible format:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a70dc666-80b5-4cdf-8ec8-a3ea54ad1ff8",
  "isSidechain": false,
  "requestId": "req_011CbEUwabGtvxrCWWRKmozB",
  "type": "assistant",
  "uuid": "d3fa8875-4d98-4039-b633-88b886f05796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mVbUrtBiRaagucGR54Cz2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 62767,
      "output_tokens": 4576,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4576,
          "cache_read_input_tokens": 62767,
          "cache_creation_input_tokens": 281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 281
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

_source line 40 · 2026-05-20T20:52:35.533Z_

<details open><summary>🔧 Tool call — Edit · `toolu_015fCmAQcia1mNrGCc3LK2ye`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "old_string": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Ahuja et al.}2024]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}",
  "new_string": "\\begin{thebibliography}{30}\n\n\\bibitem[Ahuja et~al.(2024)]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[Bandarkar et~al.(2023)]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[Burns et~al.(2023)]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Civelli et~al.(2024)]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Conneau et~al.(2020)]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[Lai et~al.(2024)]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[Li et~al.(2024)]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Miao et~al.(2026)]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[Nguyen et~al.(2021)]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[Voita and Titov(2020)]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3fa8875-4d98-4039-b633-88b886f05796",
  "isSidechain": false,
  "requestId": "req_011CbEUwabGtvxrCWWRKmozB",
  "type": "assistant",
  "uuid": "c3ecbab6-b2b7-4fb7-9d78-3b7b226c30c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mVbUrtBiRaagucGR54Cz2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 62767,
      "output_tokens": 4576,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 281,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4576,
          "cache_read_input_tokens": 62767,
          "cache_creation_input_tokens": 281,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 281
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

_source line 41 · 2026-05-20T20:52:35.564Z_

<details><summary>↩ Tool result · `toolu_015fCmAQcia1mNrGCc3LK2ye`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3ecbab6-b2b7-4fb7-9d78-3b7b226c30c6",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "77a5f223-2f56-4e4f-82e2-2bb7a786394f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
    "oldString": "\\begin{thebibliography}{30}\n\n\\bibitem[\\protect\\citename{Ahuja et al.}2024]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[\\protect\\citename{Artetxe et al.}2018]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026a.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}",
    "newString": "\\begin{thebibliography}{30}\n\n\\bibitem[Ahuja et~al.(2024)]{ahuja2024globalmmlu}\nKabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.\n\\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.\n\\newblock \\emph{arXiv preprint arXiv:2412.03304}.\n\n\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}\nAnastasios~N. Angelopoulos and Stephen Bates. 2023.\n\\newblock Conformal prediction: A gentle introduction.\n\\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.\n\n\\bibitem[Artetxe et~al.(2018)]{artetxe2018vecmap}\nMikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.\n\\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.\n\\newblock In \\emph{Proceedings of ACL}, pages 789--798.\n\n\\bibitem[Bandarkar et~al.(2023)]{bandarkar2023belebele}\nLucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.\n\\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.\n\\newblock \\emph{arXiv preprint arXiv:2308.16884}.\n\n\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}\nShai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.\n\\newblock A theory of learning from different domains.\n\\newblock \\emph{Machine Learning}, 79(1):151--175.\n\n\\bibitem[Burns et~al.(2023)]{burns2023discovering}\nCollin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.\n\\newblock Discovering latent knowledge in language models without supervision.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Civelli et~al.(2024)]{civelli2024difficulty}\nAndrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.\n\\newblock Cross-lingual transfer of difficulty representations in multilingual language models.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.\n\n\\bibitem[Conneau et~al.(2018)]{conneau2018muse}\nAlexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.\n\\newblock Word translation without parallel data.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Conneau et~al.(2020)]{conneau2020unsupervised}\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.\n\\newblock Unsupervised cross-lingual representation learning at scale.\n\\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.\n\n\\bibitem[Hewitt and Liang(2019)]{hewitt2019control}\nJohn Hewitt and Percy Liang. 2019.\n\\newblock Designing and interpreting probes with control tasks.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.\n\n\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}\nSimon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.\n\\newblock Similarity of neural network representations revisited.\n\\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.\n\n\\bibitem[Lai et~al.(2024)]{lai2024llmsurvey}\nYuxuan Lai, Xingchen Li, and Yansong Feng. 2024.\n\\newblock LLM calibration and alignment: A survey and its connection to RLHF.\n\\newblock \\emph{arXiv preprint arXiv:2404.01076}.\n\n\\bibitem[Li et~al.(2024)]{li2024inference}\nKenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.\n\\newblock Inference-time intervention: Eliciting truthful answers from a language model.\n\\newblock In \\emph{Proceedings of NeurIPS}.\n\n\\bibitem[Miao et~al.(2026)]{miao2026coral}\nQinyu Miao, Alex Wang, and Mark Johnson. 2026.\n\\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.\n\\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.\n\n\\bibitem[Miao and Ungar(2026)]{miao2026orthogonality}\nQinyu Miao and Lyle Ungar. 2026.\n\\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.\n\\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.\n\n\\bibitem[Nguyen et~al.(2021)]{nguyen2021wide}\nThao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.\n\\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.\n\\newblock In \\emph{Proceedings of ICLR}.\n\n\\bibitem[Pires et~al.(2019)]{pires2019multilingual}\nTelmo Pires, Eva Schlinger, and Dan Garrette. 2019.\n\\newblock How multilingual is multilingual {BERT}?\n\\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.\n\n\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}\nMaithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.\n\\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.\n\\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.\n\n\\bibitem[Voita and Titov(2020)]{voita2020mdl}\nElena Voita and Ivan Titov. 2020.\n\\newblock Information-theoretic probing with minimum description length.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.\n\n\\bibitem[Xiao et~al.(2025)]{xiao2025knowledgeboundary}\nShiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.\n\\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.\n\\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.\n\n\\bibitem[Zhou et~al.(2024)]{zhou2024lace}\nWenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.\n\\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.\n\\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838.\n\n\\end{thebibliography}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 396,
        "oldLines": 107,
        "newStart": 396,
        "newLines": 107,
        "lines": [
          " ",
          " \\begin{thebibliography}{30}",
          " ",
          "-\\bibitem[\\protect\\citename{Ahuja et al.}2024]{ahuja2024globalmmlu}",
          "+\\bibitem[Ahuja et~al.(2024)]{ahuja2024globalmmlu}",
          " Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Bansal, Tanvi Bansal, et~al. 2024.",
          " \\newblock Global{MMLU}: Understanding and addressing cultural and linguistic limitations in multilingual evaluation of large language models.",
          " \\newblock \\emph{arXiv preprint arXiv:2412.03304}.",
          " ",
          "-\\bibitem[\\protect\\citename{Angelopoulos and Bates}2023]{angelopoulos2023conformal}",
          "+\\bibitem[Angelopoulos and Bates(2023)]{angelopoulos2023conformal}",
          " Anastasios~N. Angelopoulos and Stephen Bates. 2023.",
          " \\newblock Conformal prediction: A gentle introduction.",
          " \\newblock \\emph{Foundations and Trends in Machine Learning}, 16(4):494--591.",
          " ",
          "-\\bibitem[\\protect\\citename{Artetxe et al.}2018]{artetxe2018vecmap}",
          "+\\bibitem[Artetxe et~al.(2018)]{artetxe2018vecmap}",
          " Mikel Artetxe, Gorka Labaka, and Eneko Agirre. 2018.",
          " \\newblock A robust self-learning method for fully unsupervised cross-lingual mappings of word embeddings.",
          " \\newblock In \\emph{Proceedings of ACL}, pages 789--798.",
          " ",
          "-\\bibitem[\\protect\\citename{Bandarkar et al.}2023]{bandarkar2023belebele}",
          "+\\bibitem[Bandarkar et~al.(2023)]{bandarkar2023belebele}",
          " Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya~Narayan Shukla, Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. 2023.",
          " \\newblock The {B}elebele benchmark: A parallel reading comprehension dataset in 122 language variants.",
          " \\newblock \\emph{arXiv preprint arXiv:2308.16884}.",
          " ",
          "-\\bibitem[\\protect\\citename{Ben-David et al.}2010]{bendavid2010theory}",
          "+\\bibitem[Ben-David et~al.(2010)]{bendavid2010theory}",
          " Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer~Wortman Vaughan. 2010.",
          " \\newblock A theory of learning from different domains.",
          " \\newblock \\emph{Machine Learning}, 79(1):151--175.",
          " ",
          "-\\bibitem[\\protect\\citename{Burns et al.}2023]{burns2023discovering}",
          "+\\bibitem[Burns et~al.(2023)]{burns2023discovering}",
          " Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023.",
          " \\newblock Discovering latent knowledge in language models without supervision.",
          " \\newblock In \\emph{Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Civelli et al.}2024]{civelli2024difficulty}",
          "+\\bibitem[Civelli et~al.(2024)]{civelli2024difficulty}",
          " Andrea Civelli, Brennan Lake, John Keston, and Tobias Roth. 2024.",
          " \\newblock Cross-lingual transfer of difficulty representations in multilingual language models.",
          " \\newblock In \\emph{Proceedings of EMNLP}, pages 4521--4535.",
          " ",
          "-\\bibitem[\\protect\\citename{Conneau et al.}2018]{conneau2018muse}",
          "+\\bibitem[Conneau et~al.(2018)]{conneau2018muse}",
          " Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, and Herv{\\'e} J{\\'e}gou. 2018.",
          " \\newblock Word translation without parallel data.",
          " \\newblock In \\emph{Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Conneau et al.}2020]{conneau2020unsupervised}",
          "+\\bibitem[Conneau et~al.(2020)]{conneau2020unsupervised}",
          " Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm{\\'a}n, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020.",
          " \\newblock Unsupervised cross-lingual representation learning at scale.",
          " \\newblock In \\emph{Proceedings of ACL}, pages 8440--8451.",
          " ",
          "-\\bibitem[\\protect\\citename{Hewitt and Liang}2019]{hewitt2019control}",
          "+\\bibitem[Hewitt and Liang(2019)]{hewitt2019control}",
          " John Hewitt and Percy Liang. 2019.",
          " \\newblock Designing and interpreting probes with control tasks.",
          " \\newblock In \\emph{Proceedings of EMNLP}, pages 2733--2743.",
          " ",
          "-\\bibitem[\\protect\\citename{Kornblith et al.}2019]{kornblith2019similarity}",
          "+\\bibitem[Kornblith et~al.(2019)]{kornblith2019similarity}",
          " Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019.",
          " \\newblock Similarity of neural network representations revisited.",
          " \\newblock In \\emph{Proceedings of ICML}, pages 3519--3529.",
          " ",
          "-\\bibitem[\\protect\\citename{Lai et al.}2024]{lai2024llmsurvey}",
          "+\\bibitem[Lai et~al.(2024)]{lai2024llmsurvey}",
          " Yuxuan Lai, Xingchen Li, and Yansong Feng. 2024.",
          " \\newblock LLM calibration and alignment: A survey and its connection to RLHF.",
          " \\newblock \\emph{arXiv preprint arXiv:2404.01076}.",
          " ",
          "-\\bibitem[\\protect\\citename{Li et al.}2024]{li2024inference}",
          "+\\bibitem[Li et~al.(2024)]{li2024inference}",
          " Kenneth Li, Oam Patel, Fernanda Vi{\\'e}gas, Hanspeter Pfister, and Martin Wattenberg. 2024.",
          " \\newblock Inference-time intervention: Eliciting truthful answers from a language model.",
          " \\newblock In \\emph{Proceedings of NeurIPS}.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao et al.}2026a]{miao2026coral}",
          "-Qinyu Miao, Alex Wang, and Mark Johnson. 2026a.",
          "+\\bibitem[Miao et~al.(2026)]{miao2026coral}",
          "+Qinyu Miao, Alex Wang, and Mark Johnson. 2026.",
          " \\newblock {CORAL}: Cross-task correctness probes for robust LLM calibration.",
          " \\newblock In \\emph{Proceedings of ACL}, pages 1823--1840.",
          " ",
          "-\\bibitem[\\protect\\citename{Miao and Ungar}2026]{miao2026orthogonality}",
          "+\\bibitem[Miao and Ungar(2026)]{miao2026orthogonality}",
          " Qinyu Miao and Lyle Ungar. 2026.",
          " \\newblock Orthogonal correctness and confidence directions in language models: Implications for calibration.",
          " \\newblock In \\emph{Proceedings of NAACL}, pages 2941--2958.",
          " ",
          "-\\bibitem[\\protect\\citename{Nguyen et al.}2021]{nguyen2021wide}",
          "+\\bibitem[Nguyen et~al.(2021)]{nguyen2021wide}",
          " Thao Nguyen, Maithra Raghu, and Simon Kornblith. 2021.",
          " \\newblock Do wide neural networks learn the same things? {C}onvergence over the training trajectory.",
          " \\newblock In \\emph{Proceedings of ICLR}.",
          " ",
          "-\\bibitem[\\protect\\citename{Pires et al.}2019]{pires2019multilingual}",
          "+\\bibitem[Pires et~al.(2019)]{pires2019multilingual}",
          " Telmo Pires, Eva Schlinger, and Dan Garrette. 2019.",
          " \\newblock How multilingual is multilingual {BERT}?",
          " \\newblock In \\emph{Proceedings of ACL}, pages 4996--5001.",
          " ",
          "-\\bibitem[\\protect\\citename{Raghu et al.}2017]{raghu2017svcca}",
          "+\\bibitem[Raghu et~al.(2017)]{raghu2017svcca}",
          " Maithra Raghu, Justin Gilmer, Jason Yosinski, and Jascha Sohl-Dickstein. 2017.",
          " \\newblock {SVCCA}: Singular vector canonical correlation analysis for deep learning dynamics and interpretability.",
          " \\newblock In \\emph{Proceedings of NeurIPS}, pages 6076--6085.",
          " ",
          "-\\bibitem[\\protect\\citename{Voita and Titov}2020]{voita2020mdl}",
          "+\\bibitem[Voita and Titov(2020)]{voita2020mdl}",
          " Elena Voita and Ivan Titov. 2020.",
          " \\newblock Information-theoretic probing with minimum description length.",
          " \\newblock In \\emph{Proceedings of EMNLP}, pages 183--196.",
          " ",
          "-\\bibitem[\\protect\\citename{Xiao et al.}2025]{xiao2025knowledgeboundary}",
          "+\\bibitem[Xiao et~al.(2025)]{xiao2025knowledgeboundary}",
          " Shiyuan Xiao, Jiaxin Zhang, and Yun Chen. 2025.",
          " \\newblock Cross-lingual transfer of knowledge boundary probes in multilingual language models.",
          " \\newblock In \\emph{Proceedings of ACL}, pages 5312--5328.",
          " ",
          "-\\bibitem[\\protect\\citename{Zhou et al.}2024]{zhou2024lace}",
          "+\\bibitem[Zhou et~al.(2024)]{zhou2024lace}",
          " Wenxuan Zhou, Sheng Zhang, Hoifung Poon, and Muhao Chen. 2024.",
          " \\newblock {LACE}: Layer-wise adaptive calibration ensembles for multilingual LLMs.",
          " \\newblock In \\emph{Proceedings of EMNLP}, pages 7823--7838."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c3ecbab6-b2b7-4fb7-9d78-3b7b226c30c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "77a5f223-2f56-4e4f-82e2-2bb7a786394f",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Tool call

_source line 44 · 2026-05-20T20:52:45.694Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TwcoqXLhriuUXoqB81cHjt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Error|Warning|Output written|pages)\"",
  "description": "Compile LaTeX paper with fixed bibliography",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a5f223-2f56-4e4f-82e2-2bb7a786394f",
  "isSidechain": false,
  "requestId": "req_011CbEV1USodHMbZ5QTrnUni",
  "type": "assistant",
  "uuid": "caebd75d-5c0c-4da0-8bde-f67ca368ad1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcJuMrMmnbnjdxSjphc1hk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 63048,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 63048,
          "cache_creation_input_tokens": 4644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4644
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

_source line 45 · 2026-05-20T20:52:46.227Z_

<details><summary>↩ Tool result · `toolu_01TwcoqXLhriuUXoqB81cHjt`</summary>

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
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/colortbl/colortbl.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
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

! LaTeX Error: Command \citename already defined.
               Or name \end... illegal, see p.192 of the manual.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H &lt;return>  for immediate help.
 ...                                              
                                                  
l.18 \newcommand{\citename}[1]{#1}
                                  
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
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `ahuja2024globalmmlu' on page 1 undefined on i
nput line 38.


Package natbib Warning: Citation `lai2024llmsurvey' on page 1 undefined on inpu
t line 38.


Package natbib Warning: Citation `miao2026coral' on page 1 undefined on input l
ine 38.


Package natbib Warning: Citation `burns2023discovering' on page 1 undefined on 
input line 38.


Package natbib Warning: Citation `miao2026orthogonality' on page 1 undefined on
 input line 38.


Package natbib Warning: Citation `pires2019multilingual' on page 1 undefined on
 input line 40.


Package natbib Warning: Citation `conneau2020unsupervised' on page 1 undefined 
on input line 40.


Package natbib Warning: Citation `xiao2025knowledgeboundary' on page 1 undefine
d on input line 40.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `ahuja2024globalmmlu' on page 2 undefined on i
nput line 52.


Package natbib Warning: Citation `bandarkar2023belebele' on page 2 undefined on
 input line 52.


Package natbib Warning: Citation `burns2023discovering' on page 2 undefined on 
input line 59.


Package natbib Warning: Citation `li2024inference' on page 2 undefined on input
 line 59.


Package natbib Warning: Citation `miao2026coral' on page 2 undefined on input l
ine 59.


Package natbib Warning: Citation `miao2026orthogonality' on page 2 undefined on
 input line 59.


Package natbib Warning: Citation `xiao2025knowledgeboundary' on page 2 undefine
d on input line 62.


Package natbib Warning: Citation `civelli2024difficulty' on page 2 undefined on
 input line 62.


Package natbib Warning: Citation `zhou2024lace' on page 2 undefined on input li
ne 62.


Package natbib Warning: Citation `conneau2018muse' on page 2 undefined on input
 line 65.


Package natbib Warning: Citation `artetxe2018vecmap' on page 2 undefined on inp
ut line 65.


Package natbib Warning: Citation `bendavid2010theory' on page 2 undefined on in
put line 65.


Package natbib Warning: Citation `kornblith2019similarity' on page 2 undefined 
on input line 68.


Package natbib Warning: Citation `nguyen2021wide' on page 2 undefined on input 
line 68.


Package natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine
d on input line 71.

[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

Package natbib Warning: Citation `kornblith2019similarity' on page 3 undefined 
on input line 117.

[3]

Package natbib Warning: Citation `ahuja2024globalmmlu' on page 4 undefined on i
nput line 134.


Package natbib Warning: Citation `bandarkar2023belebele' on page 4 undefined on
 input line 134.

[4] [5]

Package natbib Warning: Citation `conneau2018muse' on page 6 undefined on input
 line 301.


Package natbib Warning: Citation `artetxe2018vecmap' on page 6 undefined on inp
ut line 301.

[6]

Package natbib Warning: Citation `miao2026orthogonality' on page 7 undefined on
 input line 360.

[7]
No file paper.bbl.
[8] [9]

Package natbib Warning: Citation `hewitt2019control' on page 10 undefined on in
put line 527.


Package natbib Warning: There were undefined citations.

[10] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu
blic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am
sfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
r10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>
&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmri8a.pfb>
Output written on paper.pdf (10 pages, 185544 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caebd75d-5c0c-4da0-8bde-f67ca368ad1b",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "0762ba62-f27c-4de9-b074-6ffeac9db7fa",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/latexsym.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/colortbl/colortbl.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n\n! LaTeX Error: Command \\citename already defined.\n               Or name \\end... illegal, see p.192 of the manual.\n\nSee the LaTeX manual or LaTeX Companion for explanation.\nType  H &lt;return>  for immediate help.\n ...                                              \n                                                  \nl.18 \\newcommand{\\citename}[1]{#1}\n                                  \n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ot1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/base/ulasy.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `ahuja2024globalmmlu' on page 1 undefined on i\nnput line 38.\n\n\nPackage natbib Warning: Citation `lai2024llmsurvey' on page 1 undefined on inpu\nt line 38.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 1 undefined on input l\nine 38.\n\n\nPackage natbib Warning: Citation `burns2023discovering' on page 1 undefined on \ninput line 38.\n\n\nPackage natbib Warning: Citation `miao2026orthogonality' on page 1 undefined on\n input line 38.\n\n\nPackage natbib Warning: Citation `pires2019multilingual' on page 1 undefined on\n input line 40.\n\n\nPackage natbib Warning: Citation `conneau2020unsupervised' on page 1 undefined \non input line 40.\n\n\nPackage natbib Warning: Citation `xiao2025knowledgeboundary' on page 1 undefine\nd on input line 40.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `ahuja2024globalmmlu' on page 2 undefined on i\nnput line 52.\n\n\nPackage natbib Warning: Citation `bandarkar2023belebele' on page 2 undefined on\n input line 52.\n\n\nPackage natbib Warning: Citation `burns2023discovering' on page 2 undefined on \ninput line 59.\n\n\nPackage natbib Warning: Citation `li2024inference' on page 2 undefined on input\n line 59.\n\n\nPackage natbib Warning: Citation `miao2026coral' on page 2 undefined on input l\nine 59.\n\n\nPackage natbib Warning: Citation `miao2026orthogonality' on page 2 undefined on\n input line 59.\n\n\nPackage natbib Warning: Citation `xiao2025knowledgeboundary' on page 2 undefine\nd on input line 62.\n\n\nPackage natbib Warning: Citation `civelli2024difficulty' on page 2 undefined on\n input line 62.\n\n\nPackage natbib Warning: Citation `zhou2024lace' on page 2 undefined on input li\nne 62.\n\n\nPackage natbib Warning: Citation `conneau2018muse' on page 2 undefined on input\n line 65.\n\n\nPackage natbib Warning: Citation `artetxe2018vecmap' on page 2 undefined on inp\nut line 65.\n\n\nPackage natbib Warning: Citation `bendavid2010theory' on page 2 undefined on in\nput line 65.\n\n\nPackage natbib Warning: Citation `kornblith2019similarity' on page 2 undefined \non input line 68.\n\n\nPackage natbib Warning: Citation `nguyen2021wide' on page 2 undefined on input \nline 68.\n\n\nPackage natbib Warning: Citation `angelopoulos2023conformal' on page 2 undefine\nd on input line 71.\n\n[2] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nPackage natbib Warning: Citation `kornblith2019similarity' on page 3 undefined \non input line 117.\n\n[3]\n\nPackage natbib Warning: Citation `ahuja2024globalmmlu' on page 4 undefined on i\nnput line 134.\n\n\nPackage natbib Warning: Citation `bandarkar2023belebele' on page 4 undefined on\n input line 134.\n\n[4] [5]\n\nPackage natbib Warning: Citation `conneau2018muse' on page 6 undefined on input\n line 301.\n\n\nPackage natbib Warning: Citation `artetxe2018vecmap' on page 6 undefined on inp\nut line 301.\n\n[6]\n\nPackage natbib Warning: Citation `miao2026orthogonality' on page 7 undefined on\n input line 360.\n\n[7]\nNo file paper.bbl.\n[8] [9]\n\nPackage natbib Warning: Citation `hewitt2019control' on page 10 undefined on in\nput line 527.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[10] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pu\nblic/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/am\nsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmmib10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/\nshare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/te\nxlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u\nrw/times/utmri8a.pfb>\nOutput written on paper.pdf (10 pages, 185544 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "caebd75d-5c0c-4da0-8bde-f67ca368ad1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T20:52:54.669Z_

<details><summary>Logged reasoning block</summary>

```text
There's still an error about `\citename` already being defined (natbib defines it), and citation warnings. The PDF was generated but with undefined citations. Let me fix: remove the `\newcommand{\citename}` and run again. The citations are undefined because the thebibliography entries aren't being processed properly - need to run pdflatex again after the aux file is generated.

Actually wait - looking at the output more carefully: "Output written on paper.pdf (10 pages, 185544 bytes)." - the PDF was generated. The "undefined citations" warnings on the first pass are normal - they should resolve on the second pass. 

The real problem is the `\citename` conflict with natbib. Let me remove that definition and do multiple passes to let the citations resolve properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0762ba62-f27c-4de9-b074-6ffeac9db7fa",
  "isSidechain": false,
  "requestId": "req_011CbEV2FzyR62i2PRUZ8gad",
  "type": "assistant",
  "uuid": "4460c78c-4274-46cd-abf6-fb9df0dc14bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013h8h3UP84oh2Df37PmjYL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 67692,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 67692,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 47 · 2026-05-20T20:52:57.649Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Wi2FNU3jmfXzcSvbcYpkGW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
  "old_string": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\\newcommand{\\citename}[1]{#1}",
  "new_string": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4460c78c-4274-46cd-abf6-fb9df0dc14bd",
  "isSidechain": false,
  "requestId": "req_011CbEV2FzyR62i2PRUZ8gad",
  "type": "assistant",
  "uuid": "338c1cf7-49a3-4382-8ba4-3c8d6ae2042e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013h8h3UP84oh2Df37PmjYL1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 67692,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 67692,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 48 · 2026-05-20T20:52:57.669Z_

<details><summary>↩ Tool result · `toolu_01Wi2FNU3jmfXzcSvbcYpkGW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "338c1cf7-49a3-4382-8ba4-3c8d6ae2042e",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "bddbccbd-d042-412b-ba69-825c8a224a3a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/paper.tex",
    "oldString": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}\n\\newcommand{\\citename}[1]{#1}",
    "newString": "\\usepackage{natbib}\n\\bibliographystyle{plainnat}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 6,
        "lines": [
          " \\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}",
          " \\usepackage{natbib}",
          " \\bibliographystyle{plainnat}",
          "-\\newcommand{\\citename}[1]{#1}",
          " ",
          " \\definecolor{improved}{rgb}{0.85,0.95,0.85}",
          " \\definecolor{degraded}{rgb}{0.95,0.85,0.85}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "338c1cf7-49a3-4382-8ba4-3c8d6ae2042e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T20:53:03.090Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N4MxFsyYsVasvDMWt5qsee`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median && pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode paper.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode paper.tex 2>&1 | grep -E \"(Error|Output written|Warning.*undefined)\"",
  "description": "Compile LaTeX 3 passes for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bddbccbd-d042-412b-ba69-825c8a224a3a",
  "isSidechain": false,
  "requestId": "req_011CbEV372Vu9FmrVemWT5de",
  "type": "assistant",
  "uuid": "afe874a4-0751-4e84-be24-96e55bd9e20f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CAy8Ztk5ihJrMWwBLLRbgn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 497,
      "cache_read_input_tokens": 71675,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 497,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 71675,
          "cache_creation_input_tokens": 497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 497
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

_source line 50 · 2026-05-20T20:53:04.545Z_

<details><summary>↩ Tool result · `toolu_01N4MxFsyYsVasvDMWt5qsee`</summary>

```text
Output written on paper.pdf (10 pages, 188461 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afe874a4-0751-4e84-be24-96e55bd9e20f",
  "isSidechain": false,
  "promptId": "2d9e6f20-e658-4856-93e3-fcf266455fc2",
  "type": "user",
  "uuid": "cd9d40b7-7a44-4d3f-8d45-0b1dc53d9e34",
  "toolUseResult": {
    "stdout": "Output written on paper.pdf (10 pages, 188461 bytes).",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "afe874a4-0751-4e84-be24-96e55bd9e20f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T20:53:34.061Z_

PDF compiled successfully: 10 pages, 188KB, no errors or undefined references.

Output: `paper.tex` and `paper.pdf` at `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median/`.

论文结构：
- **Abstract** — 完整摘要，覆盖 Pareto frontier、CKA 机制解释、CaCLR 负结果、linear projection 正结果
- **Section 1 (Intro)** — 4 个 claim 的因果链
- **Section 2 (Related Work)** — 5 段覆盖 probe calibration、cross-lingual transfer、alignment、CKA、conformal prediction
- **Section 3 (Method)** — probes、CaCLR 公式、decomposition、CKA
- **Section 4 (Setup)** — 模型/语言/数据集/指标
- **Section 5 (Results)** — 7 个小节对应全部实验，含 8 个 table（Tables 1–7 + 主文中精简版）
- **Section 6 (Discussion)** — 解释分布匹配失败原因 + limitations
- **Section 7 (Conclusion)**
- **Appendix A–D** — INT8 验证、probe complexity、cross-benchmark、control tasks
- **21 条参考文献**

所有定量 claim 均来自 `experiment_data.json`，未编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9d40b7-7a44-4d3f-8d45-0b1dc53d9e34",
  "isSidechain": false,
  "requestId": "req_011CbEV3cHPkBLgVrdobv9tS",
  "type": "assistant",
  "uuid": "5ac99e67-405d-4e45-819a-133968380fe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/artifacts/dream_reports/dream_20260520T201854/median",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NjCjugNQmeoaw7992Peng",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 72172,
      "output_tokens": 406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 406,
          "cache_read_input_tokens": 72172,
          "cache_creation_input_tokens": 257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 257
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "5ac99e67-405d-4e45-819a-133968380fe2",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260520T201854 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_dire…",
  "leafUuid": "5ac99e67-405d-4e45-819a-133968380fe2",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate complete dream paper for cross-lingual calibration",
  "sessionId": "0d3cc3e1-6aa1-400a-9ec7-57570d53ef19"
}
```

---
