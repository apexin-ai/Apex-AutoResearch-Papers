# Research conversation: You are **Reviewer 1 (R1)** for an EMNLP 2026 Main Conference submission. Your focus is **Methods and Experiments**. Pro

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 24
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3cded80d45c60cc1.jsonl`
- **Structured JSON:** [`96320471f61e4f94fdf8.json`](../../sessions/96/96320471f61e4f94fdf8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-16T12:13:10.067Z_

You are **Reviewer 1 (R1)** for an EMNLP 2026 Main Conference submission. Your focus is **Methods and Experiments**. Produce a detailed, independent review.

## Venue: EMNLP 2026 (via ACL Rolling Review)
- Acceptance rate ~22%
- Scoring scales:
  - **Soundness**: 1 (Major Issues) – 2 (Poor) – 3 (Acceptable) – 4 (Strong) – 5 (Excellent)
  - **Excitement**: 1 (Not Exciting) – 2 (Potentially Interesting) – 3 (Interesting) – 4 (Exciting) – 5 (Highly Exciting)
  - **Overall Assessment**: 1 (Do not resubmit) – 1.5 (Resubmit after next cycle) – 2 (Resubmit next cycle) – 2.5 (Borderline Findings) – 3 (Findings) – 3.5 (Borderline Conference) – 4 (Conference) – 4.5 (Borderline Award) – 5 (Award)
  - **Confidence**: 1-5

## Paper Summary
**Title**: "Not All Correlations Transfer: When Population-Level Quality Signals Fail at Instance-Level Selection"

The paper studies test-time scaling (TTS) for structured information extraction (IE). It argues that confidence signals which correlate with output quality at the population level (quality estimation / QE) fail to select better candidates at the instance level. Across 3 datasets (SciERC NER+RE, CoNLL-2003, WNUT-17), 3 models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), and 5 confidence signal families (Structural Jaccard, Fuzzy-match Kendall, Log-probability, Voting Confidence, Exact Match), they find:
- Moderate QE: Spearman ρ up to 0.45, AUROC up to 0.75
- Selection failure: Δ < 0.3pp vs greedy, all p > 0.05, despite 13pp oracle headroom
- Two mechanisms: instance degeneracy (21-58%) and logprob score compression (0.041 nats within-instance range)
- LoRA rank ablation (rank 8 vs 32): reduces degeneracy 3× but signals still fail
- Free-form ablation: LP compression intrinsic (std ratio 0.97 constrained vs free)
- Scale ablation: Qwen3-4B replicates the gap
- Supervised verifier (LR on 5 signals, 5-fold CV): closes only 3.2% of oracle gap
- Cross-model: LLaMA-3.1-8B on CoNLL replicates (ρ 0.31-0.43, selection ≤0.2pp, degeneracy 56%)

Paper is 6 pages + appendix with numerical consistency notes.

## Key Tables
- **Table 1**: QE on SciERC. EM AUROC 0.749 (NER), VC ρ 0.379 (NER). Signal ranking task-dependent.
- **Table 2**: Selection on SciERC. Best signal LP +0.6pp NER (p=0.39, CI [-3.0,+4.2]pp, d=0.038). Oracle +13.2pp NER, +18.1pp RE.
- **Table 3**: LLaMA CoNLL cross-model. ρ 0.31-0.43, selection ≤0.2pp, degeneracy 56%.
- **Table 4**: Supervised verifier. LR 5-sig AUROC 0.760 but selection F1 0.648 (+0.4pp), gap closed 3.2%.
- **Table 5**: Feature importance. High inter-signal correlation (mean ρ 0.45-0.72).
- **Table 6**: Scale ablation 4B vs 8B. QE preserved, selection fails at both scales.

## Experiment Design Reference (full planned experiments, paper may not cover all)
The experiment plan included:
1. **ner_llama_conll** (exp-017): LLaMA-3.1-8B on CoNLL. This IS in the paper (Table 3). Note: both models are 8B decoder-only with identical LoRA recipe → a reviewer might argue this isn't true "model-agnostic" validation. Needs encoder-based or 70B+ model.
2. **simple_verifier_baseline** (exp-019): LR verifier on 5 signals. This IS in the paper (Table 4). Note: LR on same 5 correlated signals is essentially a weighted average. A real verifier would use input representations. Gap closure 3.2% actually underperforms best single signal EM (4.6%).
3. **claim_audit** (exp-024): Found numerical inconsistencies. Abstract originally claimed "AUROC up to 0.82" — the paper now claims 0.75, but check carefully. Greedy F1 had 3 different values across versions; paper says 0.644. R²=0.94 claim on n=3 was downgraded to "qualitative" but may still appear.

## Your Review Focus (R1: Methods + Experiments)
Evaluate in depth:
1. **Experimental design soundness**: Are the experiments well-designed to support the claims? Are controls appropriate?
2. **Statistical rigor**: Bootstrap tests, confidence intervals, effect sizes — are they sufficient? Is p=0.39 appropriately interpreted?
3. **Ablation quality**: Do the LoRA rank, free-form, and scale ablations properly isolate variables?
4. **Numerical consistency**: Check all numbers across abstract, intro, tables, discussion. Flag any contradictions.
5. **Reproducibility**: Are details sufficient? Models, hyperparameters, seeds, data splits.
6. **Coverage**: What experiments are missing that would strengthen the claims? (encoder models, 70B+, larger N, more datasets, better verifier)
7. **Cross-model validation strength**: Two 8B decoder-only models with same LoRA setup — is this really model-agnostic?

## Output Format
Produce a structured review with:
1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with references to tables/sections)
4. **Questions for Authors**
5. **Missing Experiments / Suggestions**
6. **Numerical Consistency Check** (list any discrepancies found)
7. **Scores**: Soundness (1-5), Excitement (1-5), Overall Assessment (1-5 scale with 0.5 increments), Confidence (1-5)

Be rigorous. This is a top venue with 22% acceptance rate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "c10099a8-42cd-4412-88f6-e80cbd4e9374",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T12:13:10.073Z_

```json
{
  "parentUuid": "c10099a8-42cd-4412-88f6-e80cbd4e9374",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c19a5196-1003-4cdf-97c2-c8c4b82f157f",
  "timestamp": "2026-05-16T12:13:10.073Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-16T12:13:12.957Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c19a5196-1003-4cdf-97c2-c8c4b82f157f",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAU5SwxXDL2StTUFMg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90fdfeee-a758-4472-b193-808a9c36f3d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhvtWPSuauhLfPWRmS5mrk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15774,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15774,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T12:13:13.419Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013sishEuKhkubCofwjJ8tAY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90fdfeee-a758-4472-b193-808a9c36f3d5",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAU5SwxXDL2StTUFMg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8503a6e8-d013-4c3f-925b-8c7b6c7ad3a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PhvtWPSuauhLfPWRmS5mrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15774,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15774,
            "ephemeral_1h_input_tokens": 0
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

_source line 5 · 2026-05-16T12:13:13.423Z_

<details><summary>↩ Tool result · `toolu_013sishEuKhkubCofwjJ8tAY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8503a6e8-d013-4c3f-925b-8c7b6c7ad3a9",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "be08f7a1-f836-46ea-afff-311662cae62a",
  "sourceToolAssistantUUID": "8503a6e8-d013-4c3f-925b-8c7b6c7ad3a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T12:13:16.065Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01DmPk48w7sDGZ6KDvnivZyN`</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be08f7a1-f836-46ea-afff-311662cae62a",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAic4u79npSshhTquB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86e81aa0-6909-4163-8769-954f5bd6700d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCGyi175QjnWu83uPNygND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T12:13:16.458Z_

<details><summary>↩ Tool result · `toolu_01DmPk48w7sDGZ6KDvnivZyN`</summary>

```text
{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (114 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_022_seed789 | 3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis. | — | — | — |\n| exp_020_fewnerd_smoke | 1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST. | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_023_lora_rank8** (success): —\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\n\n## 趋势\n成功 62 / 负向 24 / 失败 4 / 共 112\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_007_ner_llama: 已被终止 — unknown\n- exp001_seed123: 已被终止 — unknown\n- exp001_seed456: 已被终止 — unknown\n- exp008_re_n16: 已被终止 — unknown\n- exp_002_merge_conll2003: 已被终止 — unknown\n- exp_001_n16_seed123_full: 已被终止 — unknown\n- exp_001_n16_seed456_full: 已被终止 — unknown\n- exp_008_re_n16_full: 已被终止 — unknown\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\n- exp_002_conll_n16_r1024: 已被终止 — unknown\n- exp_007_llama_n16_r1024: 已被终止 — unknown\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\n- exp_019_supervised_verifier: 已被终止 — unknown\n- exp_lp_t07_scierc: 已被终止 — unknown\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\n- exp_freeform_seed789_v2: 训练失败 — unknown\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\n- exp_tacred_re_benchmark: 已被终止 — unknown\n- exp_vc_lp_cascade_selection: 已被终止 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86e81aa0-6909-4163-8769-954f5bd6700d",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "bff1b6d0-7a32-4cb7-9a3c-d0ec93f8b01c",
  "sourceToolAssistantUUID": "86e81aa0-6909-4163-8769-954f5bd6700d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T12:13:16.781Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018TND4sYks36Bfk29HKiY4L`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bff1b6d0-7a32-4cb7-9a3c-d0ec93f8b01c",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAic4u79npSshhTquB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1284dc4e-0228-45af-8ef7-bce850c2a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCGyi175QjnWu83uPNygND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15774,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1448
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 15774,
          "cache_creation_input_tokens": 1448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1448,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-16T12:13:16.795Z_

<details><summary>↩ Tool result · `toolu_018TND4sYks36Bfk29HKiY4L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_022_seed789 | 3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis. | — | — | — |\\n| exp_020_fewnerd_smoke | 1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST. | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_023_lora_rank8** (success): —\\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\\n\\n## 趋势\\n成功 62 / 负向 24 / 失败 4 / 共 112\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- ft_002: 已被终止 — unknown\\n- mvp_pilot_002: 训练失败 — unknown\\n- exp_007_ner_llama: 已被终止 — unknown\\n- exp001_seed123: 已被终止 — unknown\\n- exp001_seed456: 已被终止 — unknown\\n- exp008_re_n16: 已被终止 — unknown\\n- exp_002_merge_conll2003: 已被终止 — unknown\\n- exp_001_n16_seed123_full: 已被终止 — unknown\\n- exp_001_n16_seed456_full: 已被终止 — unknown\\n- exp_008_re_n16_full: 已被终止 — unknown\\n- exp_001_seed42_v2_r1024: 已被终止 — unknown\\n- exp_001_seed123_v2_r1024: 已被终止 — unknown\\n- exp_001_seed456_v2_ner_r1024: 已被终止 — unknown\\n- exp_002_conll_n16_r1024: 已被终止 — unknown\\n- exp_007_llama_n16_r1024: 已被终止 — unknown\\n- exp_018_llama_scierc_seed456: 已被终止 — unknown\\n- exp_019_supervised_verifier: 已被终止 — unknown\\n- exp_lp_t07_scierc: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_finetune: 已被终止 — unknown\\n- exp_freeform_seed789_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v2: 训练失败 — unknown\\n- exp_qwen3_4b_scierc_finetune_v3: 训练失败 — unknown\\n- exp_qwen3_4b_conll_merge_inference_v2: 已被终止 — unknown\\n- exp_qwen3_4b_scierc_merge_inference: 已被终止 — unknown\\n- exp_tacred_re_benchmark: 已被终止 — unknown\\n- exp_vc_lp_cascade_selection: 已被终止 — unknown\\n\", \"total_chars\": 2392, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1284dc4e-0228-45af-8ef7-bce850c2a894",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "0f8caafb-8a2e-42ea-ad16-b27c7bd15903",
  "sourceToolAssistantUUID": "1284dc4e-0228-45af-8ef7-bce850c2a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-16T12:13:19.502Z_

Now let me read the paper itself and key project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f8caafb-8a2e-42ea-ad16-b27c7bd15903",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAxyWcMtep3iAs9uRb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145f7ac4-d704-4ba7-8a54-8fa58b1054e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMzZ7L1wXDW3TchdHR1zE8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 17222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:13:19.989Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Eu8uVzreF4W7P81pKS6pLK`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "145f7ac4-d704-4ba7-8a54-8fa58b1054e1",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAxyWcMtep3iAs9uRb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a618907-bf06-4600-82a1-e90bfaf31f7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMzZ7L1wXDW3TchdHR1zE8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 17222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:13:20.021Z_

<details><summary>↩ Tool result · `toolu_01Eu8uVzreF4W7P81pKS6pLK`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
docs/paper/main.tex
artifacts/dream_reports/dream_20260516T092241/best/paper.tex
artifacts/dream_reports/dream_20260516T092241/median/paper.tex
artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/abstract.tex
docs/paper/sections/introduction.tex
docs/paper/sections/appendix.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/conclusion.tex
artifacts/dream_reports/dream_20260516T113255/best/paper.tex
artifacts/dream_reports/dream_20260516T113255/median/paper.tex
artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a618907-bf06-4600-82a1-e90bfaf31f7a",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "ba566bc2-0778-40ea-980e-5409f88ccf5c",
  "sourceToolAssistantUUID": "2a618907-bf06-4600-82a1-e90bfaf31f7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:13:20.906Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018aB3ZZ1R6DNL8YMqeAMCCD`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba566bc2-0778-40ea-980e-5409f88ccf5c",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAxyWcMtep3iAs9uRb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e83a1b3-c5ed-4d19-8640-26bb27bde0ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMzZ7L1wXDW3TchdHR1zE8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 17222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:13:20.924Z_

<details><summary>↩ Tool result · `toolu_018aB3ZZ1R6DNL8YMqeAMCCD`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.pdf
artifacts/dream_reports/dream_20260514T093336/median/paper.pdf
artifacts/dream_reports/dream_20260514T093336/worst/paper.pdf
artifacts/dream_reports/dream_20260514T105303/best/paper.pdf
artifacts/dream_reports/dream_20260514T105303/median/paper.pdf
artifacts/dream_reports/dream_20260514T105303/worst/paper.pdf
artifacts/_project/chart/fig_overview_dd8aa3.pdf
artifacts/_project/chart/fig_overview.pdf
artifacts/_project/chart/fig_selection_gap.pdf
artifacts/_project/chart/fig_signal_heatmap.pdf
artifacts/_project/chart/fig_reliability_9105b7.pdf
artifacts/exp010_selection_curves/figures/paper/fig_selection_curves.pdf
artifacts/exp_010_selection_curves/chart/fig_selection_curves.pdf
artifacts/_project/chart/fig_signal_heatmap_3d83b9.pdf
artifacts/_project/chart/fig_reliability.pdf
artifacts/dream_reports/dream_20260514T203201/best/paper.pdf
artifacts/dream_reports/dream_20260514T203201/median/paper.pdf
artifacts/_project/chart/fig_signal_heatmap_86d3ba.pdf
artifacts/figures/fig_signal_heatmap.pdf
artifacts/_project/chart/fig_correlation_selection_gap.pdf
artifacts/figures/fig_correlation_selection_gap.pdf
artifacts/_project/chart/fig_temperature_robustness.pdf
artifacts/figures/fig_temperature_robustness.pdf
artifacts/dream_reports/dream_20260514T203201/worst/paper.pdf
artifacts/_project/chart/fig_selection_gap_1024.pdf
artifacts/_project/chart/fig_reliability_1024.pdf
artifacts/figures/fig_reliability_1024.pdf
artifacts/figures/fig_selection_gap_1024.pdf
artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf
artifacts/figures/fig_signal_heatmap_1024.pdf
artifacts/exp_012_rerun_1024/chart/fig_signal_heatmap_1024_219943.pdf
artifacts/exp_012_rerun_1024/chart/fig_signal_heatmap_1024.pdf
artifacts/figures/fig_length_logprob_scatter.pdf
artifacts/exp_012_rerun_1024/chart/fig_length_logprob_scatter.pdf
artifacts/dream_reports/dream_20260515T092545/best/paper.pdf
artifacts/dream_reports/dream_20260515T092545/median/paper.pdf
artifacts/dream_reports/dream_20260515T092545/worst/paper.pdf
artifacts/_project/chart/lp_range_cdf.pdf
artifacts/_project/chart/lp_range_cdf_f7f5de.pdf
artifacts/lp_range_cdf.pdf
artifacts/_project/chart/lp_range_cdf_n16_3seed.pdf
artifacts/lp_range_cdf_n16_3seed.pdf
artifacts/_project/chart/fig_selection_gap_e39ede.pdf
artifacts/_project/chart/fig_selection_gap_21a567.pdf
artifacts/figures/fig_selection_gap.pdf
artifacts/_project/chart/fig_selection_gap_e20038.pdf
artifacts/dream_reports/dream_20260516T092241/best/paper.pdf
artifacts/dream_reports/dream_20260516T092241/median/paper.pdf
artifacts/dream_reports/dream_20260516T092241/worst/paper.pdf
artifacts/dream_reports/dream_20260516T113255/best/paper.pdf
artifacts/dream_reports/dream_20260516T113255/median/paper.pdf
artifacts/dream_reports/dream_20260516T113255/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e83a1b3-c5ed-4d19-8640-26bb27bde0ef",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "49aa7953-1c82-411b-acc9-554fc2b86e5b",
  "sourceToolAssistantUUID": "9e83a1b3-c5ed-4d19-8640-26bb27bde0ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:13:21.945Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NT3WhrL5ZoS9N644tP53Xg`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49aa7953-1c82-411b-acc9-554fc2b86e5b",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAxyWcMtep3iAs9uRb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d63effa8-6fe4-40af-9fb0-169b79292d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMzZ7L1wXDW3TchdHR1zE8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 17222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:13:21.955Z_

<details><summary>↩ Tool result · `toolu_01NT3WhrL5ZoS9N644tP53Xg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence\\n    Signals for Test-Time Scaling in Information Extraction'\\n  version: 101\\n  generated_at: '2026-05-16T10:05:35.019736+00:00'\\n  source: manual provenance build by Paper Agent\\nclaims:\\n- id: c001_voting_rho_scierc_ner\\n  text: Voting Confidence achieves ρ=0.379 on SciERC NER (corrected from 0.502 truncation\\n    artifact)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_rho_full\\n    value: 0.379\\n  note: Old value 0.502 from exp_015 was inflated by max_tokens=512 truncation. Corrected\\n    via exp_012_rerun_1024 (max_tokens=1024).\\n- id: c002_auroc_dissociation_scierc\\n  text: ρ-AUROC dissociation on SciERC — EM leads AUROC (NER 0.749, RE 0.706) while\\n    Voting leads ρ (NER 0.379, RE 0.422)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.em_auroc\\n    value: 0.749\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.em_auroc\\n    value: 0.706\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.voting_auroc\\n    value: 0.684\\n  note: Old Table 1 had Voting NER AUROC=.741 (from exp_015 truncated). Corrected\\n    to .684 via exp_012_rerun_1024. EM now leads AUROC on both NER and RE. Headline\\n    claim changed from \\\"entity voting achieves ρ=0.38 and AUROC=0.74\\\" to split ρ (Voting\\n    0.38) / AUROC (EM 0.75) claim.\\n- id: c003_sj_rho_scierc_ner\\n  text: SJ achieves ρ=0.360 on SciERC NER (corrected from 0.357)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_004_re_diagnostic\\n    metric: bootstrap_ci_95.ner_sj\\n    value:\\n    - 0.2946\\n    - 0.4586\\n- id: c004_voting_leads_re\\n  text: Voting leads RE full set (ρ=0.350, corrected from 0.422)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.voting_rho_full\\n    value: 0.35\\n  note: Corrected from exp_015_metrics_expansion (0.4217) via exp_012_rerun_1024.\\n- id: c005_fk_beats_sj_re\\n  text: FK (ρ=0.275) exceeds SJ (ρ=0.250) on RE—a reversal from NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.fk_rho_full\\n    value: 0.275\\n  - exp_id: exp_012_rerun_1024\\n    metric: re.sj_rho_full\\n    value: 0.25\\n  note: Corrected from exp_015 (FK 0.253, SJ 0.211) via exp_012_rerun_1024.\\n- id: c006_re_40pct_zero_f1\\n  text: 40% of RE instances receive zero F1 (N=8, seed=42; 159/397)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: mvp_pilot_004\\n    metric: re_sample_f1_pct_zero\\n    value: 44.3\\n    note: 44.3% from mvp_pilot_004; paper uses 40% from primary config (N=8, seed=42)\\n  - exp_id: exp_008_re_n16_v2\\n    metric: f1_zero_pct\\n    value: 44.3\\n    note: 44.3% at N=16; zero-F1 fraction varies with N and seed\\n- id: c007_em_leads_conll\\n  text: EM leads CoNLL with ρ=0.451 and AUROC=0.816\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: em_rho_full\\n    value: 0.4507\\n  - exp_id: exp_002\\n    metric: em_auroc_full\\n    value: 0.8156\\n  - exp_id: exp_015_v2\\n    metric: auroc_best.EM.conll_ner\\n    value: 0.8156\\n- id: c008_cross_model_sj_stability\\n  text: 'SJ cross-model gap: ρ=0.436 (Qwen) vs 0.431 (LLaMA), Δ=0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: sj_rho_full\\n    value: 0.4357\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n- id: c009_logprob_paradox\\n  text: Logprob achieves highest AUROC (0.761) yet lowest ρ (0.307) on CoNLL LLaMA\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_AUROC\\n    value: 0.761\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.logprob_rho\\n    value: 0.3072\\n- id: c010_conll_oracle_headroom\\n  text: 'CoNLL oracle headroom: +4.2pp (Qwen), +1.8pp (LLaMA)'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_002\\n    metric: oracle_headroom\\n    value: 0.042\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: oracle_headroom\\n    value: 0.0177\\n- id: c011_ner_no_reliable_selection\\n  text: No signal reliably surpasses greedy on NER (logprob +0.6pp, p=0.39, 3-seed\\n    bootstrap)\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  - related_work\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner\\n    value:\\n      greedy: 0.644\\n      logprob: 0.65\\n      sj: 0.645\\n      voting: 0.634\\n      random: 0.608\\n      oracle: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: bootstrap_selection_test\\n    value:\\n      logprob_vs_greedy_p: 0.39\\n      ci_95:\\n      - -0.03\\n      - 0.042\\n      cohens_d: 0.038\\n      sign_test: 61W/70L\\n  note: 3-seed bootstrap confirms +0.6pp is NOT statistically significant. Unified\\n    with c012 — no signal reliably helps on either task.\\n- id: c012_re_no_signal_beats_greedy\\n  text: No signal surpasses greedy on RE; logprob drops to −0.9pp\\n  sections:\\n  - abstract\\n  - introduction\\n  - experiments\\n  - conclusion\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re\\n    value:\\n      greedy: 0.404\\n      logprob: 0.395\\n      sj: 0.386\\n      voting: 0.359\\n      random: 0.354\\n      oracle: 0.585\\n  note: CLAIM REVERSED from exp_016 (max_tokens=512). Old claim was \\\"only logprob\\n    helps on RE (+2.3pp)\\\". Corrected via exp_016_rerun_1024_bootstrap.\\n- id: c013_oracle_headroom_ner\\n  text: Oracle upper bound 0.776, 13.2pp above greedy 0.644 on NER\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.oracle\\n    value: 0.776\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_ner.greedy\\n    value: 0.644\\n- id: c014_re_oracle_headroom\\n  text: 'RE oracle gap: 18.1pp (0.585 vs 0.404)'\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.oracle\\n    value: 0.585\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: selection_f1_re.greedy\\n    value: 0.404\\n- id: c015_ensemble_auroc\\n  text: SJ+Voting ensemble AUROC=0.666, below best individual signal EM (0.749)\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: ensemble_ner_auroc\\n    value: 0.666\\n  note: Ensemble does NOT improve over best individual. Changed from positive to negative\\n    finding.\\n- id: c016_ece_calibration\\n  text: NER reasonably well-calibrated (calibration ECE 0.069-0.096), RE shows greater\\n    miscalibration (ECE 0.109-0.339)\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_016_rerun_1024_bootstrap\\n    metric: calibration_ece\\n    value:\\n      ner_range: 0.069-0.096\\n      re_range: 0.109-0.339\\n  note: Previous c016 used binary ECE (0.27-0.77) which was incorrect metric. Calibration\\n    ECE (signal confidence → mean F1 deviation) shows NER is well-calibrated, RE has\\n    moderate miscalibration. Consistent with fig_reliability_1024.\\n- id: c017_fisher_z_ner_vs_re\\n  text: 'Fisher''s z-test ρ_SJ NER vs RE: z=2.31, p=0.021'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_z\\n    value: 2.31\\n  - exp_id: exp_004_re_diagnostic\\n    metric: fisher_z_ner_vs_re.sj_p\\n    value: 0.0209\\n- id: c018_per_relation_diagnostic\\n  text: Feature-Of ρ≈0.004, Hyponym-Of ρ=0.646\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.FEATURE-OF.rho_sj\\n    value: 0.004\\n  - exp_id: exp_004_re_diagnostic\\n    metric: per_relation_type.HYPONYM-OF.rho_fk\\n    value: 0.646\\n- id: c019_entity_span_errors\\n  text: Entity span errors account for 55.5% of RE false negatives\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_004_re_diagnostic\\n    metric: error_propagation\\n    value: head_error 17.7% + tail_error (derived) + head_tail_error 15.9% + full_error\\n      21.7% → entity span errors ~55.5%\\n  note: Computed from error_propagation breakdown in exp_004\\n- id: c020_capability_stratification_ner\\n  text: SJ ρ=0.547 on SciERC instances with 6+ entities, vs 0.415 for 1-2 entities\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.6plus_sj_rho\\n    value: 0.547\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_ner.by_ent_count.1_2_sj_rho\\n    value: 0.415\\n- id: c021_wnut_boundary\\n  text: 'WNUT-17: SJ ρ=0.089 (p=0.020), 54% zero F1'\\n  sections:\\n  - experiments\\n  - conclusion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_sj\\n    value: 0.089\\n  - exp_id: exp_003_wnut17_eval\\n    metric: sample_f1_pct_zero\\n    value: 53.7\\n  note: 'Corrected 2026-05-16: paper uses ρ=0.089 from exp003_wnut17_eval (gold-filtered\\n    n=689, p=0.020). Old value 0.062 was untraceable — only in deprecated draft.'\\n- id: c022_wnut_logprob_negative\\n  text: WNUT logprob shows strong negative correlation\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_003_ner_wnut17\\n    metric: ner.rho_logprob_full\\n    value: -0.414\\n  - exp_id: exp_003_wnut17_eval\\n    metric: rho_logprob_full\\n    value: -0.409\\n- id: c023_re_sent_length_sj\\n  text: 'RE SJ ρ increases with sentence length: Q1 0.110 → Q4 0.473 (Fisher p=0.004)'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_v2_re_rerun\\n    metric: by_sent_len_quartiles\\n    value:\\n      Q1_sj_rho: 0.11\\n      Q4_sj_rho: 0.473\\n      fisher_z_p: 0.004\\n  note: 'Corrected 2026-05-16: source is exp_009_v2_re_rerun (gold-filtered n=397).\\n    Old registry exp_009 values (Q1=0.447, Q4=0.540) used unfiltered n=551.'\\n- id: c024_high_complexity_re_subset\\n  text: 'High-complexity RE subset (n=81): Voting ρ=0.630, logprob ρ=0.554, SJ ρ=0.502'\\n  sections:\\n  - experiments\\n  tier: 2\\n  evidence:\\n  - exp_id: exp_009_capability_stratification\\n    metric: scierc_re.by_rel_count\\n    value:\\n      6plus_sj_rho: 0.527\\n  note: Registry has 6plus_sj_rho=0.527; paper may use exp_009_v2 data. Voting and\\n    logprob values not in registry summary.\\n- id: c025_temperature_sj_stable\\n  text: SJ NER ρ shifts from 0.388 (T=0.7) to 0.360 (T=1.0), Δ=0.028\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_005\\n    metric: sj_rho_t07_ner\\n    value: 0.388\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  note: T=0.7 data from exp_005; T=1.0 from exp_015\\n- id: c026_n_scaling_sj\\n  text: SJ N=8→N=16 improves ρ from 0.360 to 0.412±0.025 (3-seed, +0.052) on Qwen\\n    SciERC NER\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: ner.sj_rho_full\\n    value: 0.36\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_001_seed123_v2\\n    metric: sj_rho_full\\n    value: 0.424\\n  - exp_id: exp_001_seed456_v2_ner\\n    metric: full.SJ.rho\\n    value: 0.384\\n  note: '3-seed mean: (0.428+0.424+0.384)/3 ≈ 0.412, σ=0.025'\\n- id: c027_llama_conll_3seed\\n  text: 'LLaMA CoNLL N=16 3-seed: SJ ρ=0.463±0.007, logprob ρ=0.310±0.005'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.SJ_rho\\n    value: 0.4698\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.SJ_rho\\n    value: 0.4552\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: full.logprob_rho\\n    value: 0.3161\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    metric: full.logprob_rho\\n    value: 0.3078\\n- id: c028_loo_sj_circularity\\n  text: LOO-SJ Δρ=-0.014, max per-instance Δρ=3.1×10⁻⁴—circularity negligible\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.max_delta_rho\\n    value: 0.000305\\n  - exp_id: exp_015_v2\\n    metric: loo_sj.all_no_circularity\\n    value: true\\n- id: c029_llama_scierc_cross_model\\n  text: 'LLaMA replicates structural-over-surface on SciERC: NER SJ ρ=0.363 > FK ρ=0.327;\\n    conditional RE SJ ρ=0.405 > FK ρ=0.259'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_sj\\n    value: 0.363\\n  - exp_id: exp_007_llama_inference\\n    metric: ner.rho_fk\\n    value: 0.327\\n  - exp_id: exp_007_llama_inference\\n    metric: re.sj_rho_cond\\n    value: 0.405\\n  - exp_id: exp_007_llama_inference\\n    metric: re.fk_rho_cond\\n    value: 0.259\\n- id: c030_em_conditional_dominance\\n  text: 'EM ranks #1 on conditional set across all 4 configurations'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.em_rho_cond\\n    value: 0.3427\\n  - exp_id: exp_015_metrics_expansion\\n    metric: re.em_rho_cond\\n    value: 0.3607\\n  - exp_id: exp_002_conll_n16\\n    metric: conditional.EM_rho\\n    value: 0.4658\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    metric: conditional.EM_rho\\n    value: 0.4732\\n  note: 'Paper cites EM conditional: SciERC NER 0.408, RE 0.485, CoNLL Qwen N=16 0.466,\\n    CoNLL LLaMA 3-seed 0.462. Registry has slightly different values from different\\n    seed/N combinations.'\\n- id: c031_em_conditional_scierc\\n  text: 'EM conditional: NER ρ=0.408, RE ρ=0.485'\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_cond_em_rho\\n    value: 0.414\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: re_cond_em_rho\\n    value: 0.475\\n  note: 'Paper rounds: 0.414→0.408, 0.475→0.485. May use different seed/N baseline.'\\n- id: c032_logprob_re_cond_collapse\\n  text: Logprob conditional RE collapses to ρ=0.011\\n  sections:\\n  - experiments\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    metric: re_cond.logprob.rho\\n    value: 0.0112\\n  note: 'Corrected 2026-05-16: source is exp_012_rerun_1024 (greedy_f1>0 filter, n=238).\\n    Old exp_015 value 0.1457 used wrong filter (any sample F1>0, n=331). Old text\\n    0.002 was stale and untraceable.'\\n- id: c033_sj_n16_cond_re\\n  text: At N=16, SJ maintains ρ=0.308 on conditional RE while logprob drops to -0.026\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_008_re_n16_v2\\n    metric: sj_rho_cond\\n    value: 0.308\\n- id: c034_structural_over_logprob_n16\\n  text: Structural-over-logprob advantage holds across all 4 N=16 settings (Δ=+0.124\\n    to +0.175)\\n  sections:\\n  - experiments\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_voting_conf_rho\\n    value: 0.399\\n  - exp_id: exp_001_ner_n16_scierc\\n    metric: ner_logprob_rho\\n    value: 0.237\\n  - exp_id: exp_002_conll_n16\\n    metric: full.EM_rho\\n    value: 0.4627\\n  - exp_id: exp_002_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3146\\n  - exp_id: exp_007_llama_n16\\n    metric: full.voting_conf_rho\\n    value: 0.4515\\n  - exp_id: exp_007_llama_n16\\n    metric: full.logprob_rho\\n    value: 0.2041\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.logprob_rho\\n    value: 0.3058\\n- id: c035_n_scaling_diminishing\\n  text: 'SJ N-scaling gains are sublinear: +0.052 Qwen SciERC, +0.032 LLaMA CoNLL'\\n  sections:\\n  - discussion\\n  tier: 1\\n  evidence:\\n  - exp_id: exp_001_seed42_v2\\n    metric: sj_rho_full\\n    value: 0.428\\n  - exp_id: exp_015_metrics_expansion\\n    metric: ner.sj_rho_full\\n    value: 0.3565\\n  - exp_id: exp_017_llama_conll_n16\\n    metric: full.SJ_rho\\n    value: 0.4642\\n  - exp_id: exp_017_llama_conll_infer\\n    metric: full.SJ_rho\\n    value: 0.4314\\n  note: 'Qwen SciERC: 0.412 (3-seed mean) - 0.360 = +0.052. LLaMA CoNLL: 0.463 (3-seed)\\n    - 0.431 = +0.032'\\n- id: c036_sj_ece_calibration\\n  text: '[DEPRECATED] SJ achieves lowest calibration error (ECE=0.075-0.102 across\\n    settings)'\\n  sections: []\\n  tier: X\\n  evidence: []\\n  note: DEPRECATED — reversed by c016_ece_miscalibration. Old ECE values (0.075-0.102)\\n    were from exp_015 (max_tokens=512 truncation artifact). Corrected data shows all\\n    signals ECE 0.27-0.77.\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: No signal significantly improves sample selection over greedy decoding despite\\n    13-18pp oracle headroom\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D070\\n  - D071\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: LP scores compressed into effective ties for 60% of instances under constrained\\n    decoding\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Where LP compression is absent, selection recovers +2.9pp (p=0.01)\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Constrained-decoding score compression is the primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP carries useful per-sample quality information; score compression is the\\n    primary bottleneck\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR utility correlates with F1 across instances but not within\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Free-form ablation would test if bottleneck is decoding-regime-specific\\n  type: planned\\n  evidence: []\\n  decisions:\\n  - D071\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Consistency signals effective QE (rho up to 0.38, AUROC up to 0.75) but fail\\n    at selection\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: LP fails due to constrained-decoding score compression\\n  type: empirical\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: RE findings preliminary, single benchmark\\n  type: scope_limitation\\n  evidence:\\n  - exp_012_rerun_1024\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP exhibits 4x higher within-instance variance than full-sequence\\n    LP on SciERC, but selection performs worse (-2.0pp)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_variance_ratio\\n    value: 4.0x\\n  - exp_id: exp_entity_token_lp\\n    metric: scierc_entity_lp_selection_delta\\n    value: -1.68\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: On CoNLL, entity-token LP variance collapses to near-zero (median 2e-10) with\\n    79% tied\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_variance_median\\n    value: 2e-10\\n  - exp_id: exp_entity_token_lp\\n    metric: conll_entity_lp_tied_fraction\\n    value: 0.794\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP rules out format-token dilution as primary cause; points to\\n    intrinsic model overconfidence on entity tokens\\n  type: interpretive\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: sections/limitations\\n    paragraph: 0\\n    sentence: 0\\n  text: Entity-token LP is the only tested remedy; LP×VC and calibration approaches\\n    are unexplored\\n  type: scope\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C1 reframe: instance-level nature is setup, LP compression + MBR within-instance\\n    failure are the findings'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF4: 60% tied replaced with pooled within-instance ρ(LP,F1)=0.248 continuous\\n    characterization'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: 'C2 reframe: entity-token LP added as diagnostic ablation contribution'\\n  type: structural\\n  evidence:\\n  - exp_id: exp_entity_token_lp\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: sections/abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: 'SF3: RE removed from abstract; SF1: ρ=0.38 sourced to SciERC primary, up\\n    to 0.45 on ceiling control; MF2(a): benchmark roles explicit; M2: streamlined\\n    from 9 to 6 sentences'\\n  type: structural\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 21% of SciERC instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 58% of CoNLL instances produce identical F1 across all N samples\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 13% of SciERC instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 49% of CoNLL instances yield constant utility scores\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.524 on SciERC\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: SJ median within-instance rho = 0.994 on CoNLL\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 23% of oracle gap on non-degenerate SciERC instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: MBR closes 41% of oracle gap on non-degenerate CoNLL instances\\n  type: quantitative\\n  evidence: Q1 within-instance analysis\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: sections/discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: Greedy T=0 achieves F1=0.663 on SciERC, surpassing all N=8 selection strategies\\n  type: quantitative\\n  evidence: SF4 greedy data\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: tab:notation\\n  section: method\\n  caption: Notation used throughout the paper\\n  evidence: []\\n  note: Notation table—no experimental data.\\n- id: tab:quality_estimation\\n  section: experiments\\n  caption: Quality estimation across tasks and models (Spearman ρ and AUROC)\\n  evidence:\\n  - exp_id: exp_012_rerun_1024\\n    role: SciERC NER ρ values (N=8, Qwen) — corrected from exp_015 (truncation artifact)\\n  - exp_id: exp_015_metrics_expansion\\n    role: SciERC RE ρ values (N=8, Qwen) — RE values unaffected by truncation fix\\n  - exp_id: exp_015_v2\\n    role: AUROC values across settings\\n  - exp_id: exp_002\\n    role: CoNLL Qwen N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_infer\\n    role: CoNLL LLaMA N=8 ρ and AUROC\\n  - exp_id: exp_017_llama_conll_n16\\n    role: LLaMA CoNLL N=16 3-seed (seed=42)\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: LLaMA CoNLL N=16 3-seed (seed=123)\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: LLaMA CoNLL N=16 3-seed (seed=456)\\n- id: tab:selection\\n  section: experiments\\n  caption: Best-of-N selection F1 on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: All selection F1 values (NER and RE)\\n- id: tab:robustness\\n  section: experiments\\n  caption: Signal robustness across configurations (Spearman ρ)\\n  evidence:\\n  - exp_id: exp_005\\n    role: Temperature block (T=0.7 vs T=1.0, Qwen SciERC)\\n  - exp_id: exp_015_metrics_expansion\\n    role: N=8 baseline values\\n  - exp_id: exp_001_seed42_v2\\n    role: N=16 SJ ρ seed=42\\n  - exp_id: exp_001_seed123_v2\\n    role: N=16 SJ ρ seed=123\\n  - exp_id: exp_001_seed456_v2_ner\\n    role: N=16 SJ ρ seed=456\\n  - exp_id: exp_017_llama_conll_n16\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=42'\\n  - exp_id: exp_017_llama_conll_n16_s123\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=123'\\n  - exp_id: exp_017_llama_conll_n16_s456\\n    role: 'Cross-model block: LLaMA CoNLL N=16 seed=456'\\nfigures:\\n- id: fig:overview\\n  section: introduction\\n  caption: The correlation-selection gap conceptual diagram\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Quality estimation data (ρ, AUROC for left panel)\\n  - exp_id: exp_016_signal_ensemble\\n    role: Selection F1 data (right panel)\\n- id: fig:signal_heatmap\\n  section: experiments\\n  caption: Quality estimation heatmap (Spearman ρ) across five signals and four configurations\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Full set ρ values for SciERC NER/RE (Qwen, N=8)\\n  - exp_id: exp_002\\n    role: CoNLL Qwen full set ρ values\\n  - exp_id: exp_001_ner_n16_scierc\\n    role: Conditional set ρ values\\n- id: fig:selection_gap\\n  section: experiments\\n  caption: The correlation-selection gap on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_016_signal_ensemble\\n    role: Best-of-N selection F1 bars and quality estimation ρ line\\n- id: fig:temperature_robustness\\n  section: experiments\\n  caption: Temperature robustness on SciERC (N=8)\\n  evidence:\\n  - exp_id: exp_005\\n    role: SJ, FK ρ values at T=0.7 and T=1.0\\n- id: fig:reliability\\n  section: experiments\\n  caption: Reliability diagrams on SciERC (N=8, T=1.0)\\n  evidence:\\n  - exp_id: exp_015_metrics_expansion\\n    role: Calibration/ECE data for all signals\\n  - exp_id: exp_002\\n    role: ECE values across signals\\n_completeness:\\n  coverage: 58/68\\n  claims: 63\\n  tables: 4\\n  figures: 5\\n  tier_counts:\\n    tier1: 0\\n    tier2: 58\\n    tier3: 10\\n    tierX: 0\\n  last_checked: '2026-05-16T10:05:35.019798+00:00'\\n\", \"total_chars\": 27187, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d63effa8-6fe4-40af-9fb0-169b79292d2f",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "bb8779c0-b175-4f8f-8ca9-9c82263c6de1",
  "sourceToolAssistantUUID": "d63effa8-6fe4-40af-9fb0-169b79292d2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T12:13:22.351Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015gYWZVoGRT9osNypXg9djB`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb8779c0-b175-4f8f-8ca9-9c82263c6de1",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EAxyWcMtep3iAs9uRb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ceeda2c7-691f-4430-a387-071002be3238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMzZ7L1wXDW3TchdHR1zE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3075,
      "cache_read_input_tokens": 17222,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 381,
          "cache_read_input_tokens": 17222,
          "cache_creation_input_tokens": 3075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3075,
            "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-16T12:13:22.602Z_

<details><summary>↩ Tool result · `toolu_015gYWZVoGRT9osNypXg9djB`</summary>

```text
Error: result (93,945 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b72398d7-e431-4137-b17e-51fc8746e976/tool-results/mcp-agent-ml-research-read_project_file-1778933602599.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b72398d7-e431-4137-b17e-51fc8746e976/tool-results/mcp-agent-ml-research-read_project_file-1778933602599.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/b72398d7-e431-4137-b17e-51fc8746e976/tool-results/mcp-agent-ml-research-read_project_file-1778933602599.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ceeda2c7-691f-4430-a387-071002be3238",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "c67e25a6-e324-4a52-8359-403a46819f0e",
  "sourceToolAssistantUUID": "ceeda2c7-691f-4430-a387-071002be3238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-16T12:13:25.026Z_

Let me read the actual paper sections now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67e25a6-e324-4a52-8359-403a46819f0e",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47ea5651-5fe3-4aa7-a99b-7f4cb2498a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T12:13:25.980Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TcYVVxTLsndP423stBesxt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ea5651-5fe3-4aa7-a99b-7f4cb2498a20",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09048b84-ac63-45dc-ba93-ebd51fe4445e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T12:13:25.998Z_

<details><summary>↩ Tool result · `toolu_01TcYVVxTLsndP423stBesxt`</summary>

```text
1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---for quality estimation and sample selection on three NER benchmarks spanning a difficulty gradient (SciERC, CoNLL, WNUT-17), using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: best-of-$N$ selection approximately matches greedy decoding ($T{=}0$) despite 13--18~pp oracle headroom.
6	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.
7	A five-layer ablation chain and a LoRA-rank ablation (degeneracy 7\% vs.\ 21\%) confirm these mechanisms are intrinsic to capable fine-tuned models: reducing degeneracy is necessary but not sufficient for selection.
8	Closing the gap likely requires learned per-sample scoring.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09048b84-ac63-45dc-ba93-ebd51fe4445e",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "a4fd75b9-5f90-4d1d-8a11-0ce0219643e2",
  "sourceToolAssistantUUID": "09048b84-ac63-45dc-ba93-ebd51fe4445e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T12:13:26.450Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dc3zSGReNij9316Ez5ptwF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4fd75b9-5f90-4d1d-8a11-0ce0219643e2",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55743033-9ef4-4e17-8931-ca298c4c5120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T12:13:26.456Z_

<details><summary>↩ Tool result · `toolu_01Dc3zSGReNij9316Ez5ptwF`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.45, AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to sample selection---the \textbf{correlation-selection gap}: best-of-$N$ selection approximately matches greedy decoding ($T{=}0$) without significant improvement despite 13--18~pp oracle headroom.
13	The gap has two empirical causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---median within-instance range of 0.041 nats (\S\ref{sec:discussion}).
14	
15	\begin{figure*}[t]
16	\centering
17	\includegraphics[width=\textwidth]{fig_overview}
18	\caption{The correlation-selection gap. \textbf{Left}: consistency signals reliably predict instance-level quality ($\rho$ up to 0.45, AUROC up to 0.82). \textbf{Right}: quality estimation does not translate to selection---all methods approximately match greedy decoding ($T{=}0$) despite 13~pp oracle headroom (\S\ref{sec:discussion}).}
19	\label{fig:overview}
20	\end{figure*}
21	
22	We evaluate five signals from three families---structural, surface, and model-internal---on SciERC \cite{luan2018scierc} as a primary medium-difficulty test bed, with CoNLL-2003 \cite{tjongkimsang2003conll} (ceiling-effect control) and WNUT-17 \cite{derczynski2017wnut} (signal-collapse boundary), using two 8B models (Qwen3-8B, LLaMA-3.1-8B) with a 4B ablation (Qwen3-4B).
23	An exploratory extension to relation extraction is reported in Appendix~\ref{app:re_extension}.
24	Our contributions:
25	\begin{enumerate}
26	    \item \textbf{Quality estimation framework.}
27	    Structural agreement signals reliably predict output quality for LLM-based NER: VC achieves $\rho{=}0.38$ on the medium-difficulty primary test bed (SciERC), while EM reaches AUROC${=}0.82$ on CoNLL.
28	    Signal rankings are difficulty-dependent but stable across model families and a 4B scale ablation, supporting practical applications such as selective prediction and error flagging.
29	
30	    \item \textbf{Multi-causal diagnosis of the correlation-selection gap.}
31	    Despite reliable quality estimation, selection fails because two mechanisms jointly eliminate per-sample discriminability.
32	    Instance degeneracy: 21--58\% of instances produce identical F1 across all $N$ samples, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); on non-degenerate instances, consensus-proximity closes 23--41\% of the oracle gap.
33	    LP compression: the only per-sample signal has median within-instance range of 0.041 nats ($\rho(\text{LP}, \text{F1}){=}0.248$).
34	    A LoRA-rank ablation reduces degeneracy from 21\% to 7\% without enabling selection, confirming that low degeneracy is necessary but not sufficient; the non-tied LP subset ($+2.9$~pp, $p{=}0.004$) shows signals carry information that compression prevents from being exploited.
35	
36	    \item \textbf{Diagnostic ablation chain.}
37	    A five-layer ablation (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding or signal design. Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
38	\end{enumerate}
39	
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55743033-9ef4-4e17-8931-ca298c4c5120",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "d3559949-791b-4d76-ab71-5dfe6bbcb856",
  "sourceToolAssistantUUID": "55743033-9ef4-4e17-8931-ca298c4c5120",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T12:13:27.393Z_

<details open><summary>🔧 Tool call — Read · `toolu_011hP8gx6vUQWEcVFQEFks98`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3559949-791b-4d76-ab71-5dfe6bbcb856",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88b67a9b-ab74-4206-9306-8d0d803697a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T12:13:27.398Z_

<details><summary>↩ Tool result · `toolu_011hP8gx6vUQWEcVFQEFks98`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{&lt;j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
27	\begin{equation}\label{eq:fk}
28	\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}
29	\end{equation}
30	where $\bar{P}$ is mean observed and $\bar{P}_e$ expected agreement.
31	Temperature-based sampling introduces mild negative dependence ($-$0.4\% to $-$4.0\%; Appendix~\ref{app:fk_independence}), which does not inflate FK.
32	Unlike structural signals, FK relies on exact string matching.
33	
34	\paragraph{Soft Jaccard (structural, instance-level).}
35	For samples $y_i, y_j$, we group extractions by type, compute max-weight bipartite matching (Hungarian algorithm, token-level IoU), and define:
36	\begin{equation}\label{eq:sj}
37	\text{SJ}(y_i, y_j) = \frac{\sum_{m \in M} \text{sim}(a_m, b_m)}{\sum_{g} \max(|g_i|, |g_j|)}
38	\end{equation}
39	where $M$ is the matched set, $\text{sim}(a_m, b_m)$ is the token-level IoU between matched spans, and $\max(|g_i|, |g_j|)$ penalizes length asymmetry.\footnote{The denominator uses $\max(|g_i|, |g_j|)$ per type group rather than $|A \cup B|$, penalizing cardinality mismatches more heavily than standard Jaccard; robustness to this choice is verified in Table~\ref{tab:sj_normalizer}.}
40	The instance-level signal averages over all pairs:
41	\begin{equation}\label{eq:sj_instance}
42	c_{\text{sj}}(x) = \frac{1}{\binom{N}{2}} \sum_{i&lt;j} \text{SJ}(y_i, y_j)
43	\end{equation}
44	
45	\paragraph{Entity voting confidence (structural, instance-level).}
46	For each entity $e$ in the union $E_\cup$ of all samples, we compute frequency $\text{freq}(e) = |\{i : e \in y_i\}| / N$.
47	The instance-level confidence is the mean frequency:
48	\begin{equation}\label{eq:voting}
49	c_{\text{vote}}(x) = \frac{1}{|E_\cup|} \sum_{e \in E_\cup} \text{freq}(e)
50	\end{equation}
51	When $E_\cup = \emptyset$, we set $c_{\mathrm{vc}}(x) = 0$.\footnote{Equation~\ref{eq:voting} defines the continuous QE signal; for voted-output \textit{selection} (Table~\ref{tab:selection}), we include only entities with frequency ${>}N/2$, following standard majority voting.}
52	
53	\subsection{Evaluation Framework}\label{sec:evaluation}
54	
55	\paragraph{Quality estimation.}
56	Spearman $\rho$ between the signal and instance-level F1, and AUROC classifying instances as above/below median F1.
57	Both quality estimation and selection exclude instances with no gold annotations: $n{=}529$ on SciERC (from 551), $n{=}2{,}756$ on CoNLL (from 3{,}453).\footnote{On CoNLL, full-set ($n{=}3{,}453$) Spearman $\rho$ values are higher than gold-filtered ($n{=}2{,}756$) by $+0.03$--$0.05$ due to the zero/non-zero boundary inflating correlations, paralleling the effect documented for WNUT-17 in Appendix~\ref{app:additional}.}
58	
59	\paragraph{Sample selection.}
60	Best-of-$N$ F1: per-sample signals (LP) directly rank candidates; instance-level signals select the sample closest to consensus.
61	Baselines: \textit{oracle} (highest-F1 sample) and \textit{greedy} ($T{=}0$ argmax decoding).
62	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88b67a9b-ab74-4206-9306-8d0d803697a2",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "e4a1ec85-5ae4-4b67-a61c-7cae4732118f",
  "sourceToolAssistantUUID": "88b67a9b-ab74-4206-9306-8d0d803697a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T12:13:27.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_016qT21kkrHmB1GTZeZa8pbi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4a1ec85-5ae4-4b67-a61c-7cae4732118f",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e6f4aad-0a6f-4f1b-aef5-bd1f290c7a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T12:13:27.868Z_

<details><summary>↩ Tool result · `toolu_016qT21kkrHmB1GTZeZa8pbi`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed stability $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
31	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}
32	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
33	\midrule
34	VC & Structural & \textbf{.379} & \textbf{.663} & .424 & .789 & .426 & .709 \\
35	SJ  & Structural & .360 & .650 & .436 & .801 & \textbf{.431} & .704 \\
36	FK & Surface & .267 & .602 & .400 & .774 & .428 & .703 \\
37	EM  & Surface    & .295 & .614 & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
38	\midrule
39	LP     & Model      & .205 & .578 & .316 & .753 & .307 & \textbf{.761} \\
40	\bottomrule
41	\end{tabular}
42	\end{table*}
43	
44	Table~\ref{tab:quality_estimation} presents $\rho$ and AUROC for five signals across tasks and models.\footnote{$\varepsilon{=}0.05$ applies only to selection (\S\ref{sec:selection_gap}); quality estimation is $\varepsilon$-free. Selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}).}
45	
46	\paragraph{Signal rankings are difficulty-dependent.}
47	On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over surface ($\rho{\leq}0.295$) and LP ($0.205$); bootstrap CIs confirm the SJ--LP gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
48	On CoNLL (ceiling-effect control, single-sample F1${\approx}$0.91), EM leads both $\rho$ and AUROC ($0.816$); the $\rho$--AUROC dissociation across datasets reflects use-case alignment.
49	At the signal-collapse boundary---WNUT-17 (52\% zero F1)---all conditional signals collapse (Table~\ref{tab:wnut}); restricting to non-zero instances reshuffles rankings, with EM strongest ($\rho{=}0.360$; Figure~\ref{fig:signal_heatmap}, Appendix~\ref{app:additional}).
50	
51	%% ============================================================
52	\subsection{The Correlation-Selection Gap}
53	\label{sec:selection_gap}
54	
55	We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from $N$ candidates.
56	
57	\begin{table}[t]
58	\centering
59	\small
60	\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$, $p$ vs.\ greedy baseline from paired sign tests). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Random: uniform random selection from $N$ candidates. Non-tied LP subset analysis in \S\ref{sec:discussion}; RE selection in Appendix~\ref{app:re_extension}.}
61	\label{tab:selection}
62	\begin{tabular}{lcc}
63	\toprule
64	Method & NER F1 & $p$ \\
65	\midrule
66	Oracle & $0.778 \pm 0.003$ & --- \\
67	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
68	\midrule
69	\multicolumn{3}{l}{\textit{Per-sample signal}} \\
70	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
71	\midrule
72	\multicolumn{3}{l}{\textit{Instance-level signals (consensus-proximity selection)}} \\
73	SJ           & $0.646 \pm 0.002$ & .67 \\
74	FK           & $0.646 \pm 0.001$ & .79 \\
75	EM           & $0.637 \pm 0.001$ & --- \\
76	VC           & $0.623 \pm 0.004$ & --- \\
77	\midrule
78	Random           & $0.610 \pm 0.003$ & --- \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	Despite moderate quality estimation, confidence signals yield limited selection gains (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
84	Instance-level signals (SJ, FK, EM, VC) assign identical QE scores to all candidates per input; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}: SJ 0.646, FK 0.646, EM 0.637, VC 0.623), but none improves over the greedy baseline.
85	The key question is whether LP---the only natively per-sample signal---can exploit the oracle headroom.
86	
87	\paragraph{No significant improvement over greedy.}
88	On SciERC NER (2-seed sign tests\footnote{Multi-seed NER experiments confirm seed variation is small ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}).}, $n{=}529$), the oracle (0.778) reveals 13.3~pp of headroom above greedy (0.645), yet LP achieves only 0.647 ($\Delta{=}{+}0.2$~pp, $p{=}0.29$); no signal consistently improves selection ($p{>}0.05$; TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration, Appendix~\ref{app:tost}).
89	The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); RE selection results are consistent (Appendix~\ref{app:re_extension}).
90	CoNLL's near-ceiling single-sample F1 (0.91) with only ${\sim}$4~pp oracle headroom functions primarily as a ceiling-effect control.
91	Under stringent external TOST anchors ($\delta_0{=}1.0$~pp), some configurations (e.g., Qwen CoNLL) show statistically significant degradation, indicating signals can actively harm selection (Appendix~\ref{app:tost}).
92	LP approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, not significant); neither significantly outperforms the other, yet both fall far short of the oracle (0.778, 13.3~pp gap).
93	Instance-level signals predict \textit{which inputs} the model handles reliably, not \textit{which output} is best; closing this gap likely requires trained verifiers \cite{cobbe2021verifiers}.\footnote{For negative results (all $p{>}0.05$), uncorrected tests suffice; the sole positive finding (non-tied LP subset, $+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion}) survives Bonferroni correction over 5 comparisons.}
94	
95	%% ============================================================
96	\subsection{Robustness}
97	\label{sec:robustness_main}
98	
99	Consistency signals are robust across $T{\in}\{0.7, 1.0\}$ with sublinear $N$-scaling gains (Table~\ref{tab:robustness}); LP shows the largest temperature sensitivity ($\Delta\rho{=}{+}0.044$).
100	Signal rankings are stable across seeds (Kendall's $W{=}1.0$ at $N{=}8$; Table~\ref{tab:ranking-stability}).
101	NER calibration is reasonable (ECE 0.069--0.096; Appendix~\ref{app:calibration}).
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{Scale ablation: Qwen3-8B vs.\ 4B NER quality estimation ($\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). 8B values identical to Table~\ref{tab:quality_estimation}; 4B uses matched evaluation protocol. RE scale ablation in Appendix~\ref{app:re_extension}.}
107	\label{tab:scale_ablation}
108	\begin{tabular}{@{}ll cc r@{}}
109	\toprule
110	& & \textbf{8B} & \textbf{4B} & $\Delta$ \\
111	\midrule
112	CoNLL & SJ & .436 & .422 & $-$.014 \\
113	      & FK & .400 & .418 & $+$.018 \\
114	SciERC & SJ & .360 & .422 & $+$.062 \\
115	       & FK & .267 & .326 & $+$.059 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	\paragraph{Scale robustness.}
121	Repeating with Qwen3-4B (Table~\ref{tab:scale_ablation}), quality estimation is comparable or improved (mean $|\Delta\rho|{=}0.042$), yet selection remains below greedy on SciERC ($\Delta$ up to $-3.4$~pp) despite 13.0~pp of oracle headroom, and indistinguishable on CoNLL (${<}0.3$~pp, 1.7~pp headroom). Within the 3B--8B range tested across two model families, task difficulty is a stronger predictor of the gap than model scale.
122	Instance degeneracy also scales with model capability: 8B shows twice the degeneracy of 4B on SciERC (21\% vs.\ 10.4\%) despite comparable within-instance utility correlation (Table~\ref{tab:degeneracy}).
123	
124	\paragraph{LoRA-rank ablation.}
125	To disentangle model capacity from degeneracy, we train Qwen3-8B on SciERC with LoRA rank${=}8$ (vs.\ rank${=}32$ in all other experiments).
126	Reducing rank lowers degeneracy from 21\% to 7.2\% and increases oracle headroom from 13.3~pp to 16.0~pp, confirming that fine-tuning capacity drives output convergence.
127	However, selection still fails: the best signal (LP, 0.635) falls short of greedy (0.640), and all consensus-proximity signals perform worse (SJ 0.631, VC 0.592).
128	Quality estimation remains comparable (VC $\rho{=}0.394$ vs.\ $0.379$; SJ $\rho{=}0.365$ vs.\ $0.360$).
129	Low degeneracy is thus a necessary but not sufficient condition for selection---LP compression persists regardless of LoRA rank, indicating that both mechanisms must be addressed simultaneously.
130	
131	\paragraph{Supervised verifier baseline.}
132	To test whether the information bottleneck lies in the aggregation method or the features themselves, we train a logistic regression verifier on all five signals (3-fold cross-validation on SciERC, $N{=}8$).
133	The supervised selector achieves F1${=}0.648$, closing only 0.8\% of the oracle gap---a negligible improvement over the best unsupervised signal (LP, 0.647; $\Delta{=}{+}0.08$~pp).
134	Its AUROC (0.697) is lower than single-signal VC (0.706), and feature importance is dominated by VC (coefficient 0.65--0.92) with SJ receiving a negative coefficient.
135	The failure of supervised signal combination confirms that the bottleneck is not in how signals are aggregated but in what information they encode: these features lack per-sample discriminative content sufficient for selection.
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e6f4aad-0a6f-4f1b-aef5-bd1f290c7a31",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "c7c260dc-e4ca-4728-b00b-23f2db5bcef6",
  "sourceToolAssistantUUID": "4e6f4aad-0a6f-4f1b-aef5-bd1f290c7a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T12:13:28.398Z_

<details open><summary>🔧 Tool call — Read · `toolu_018rXSWnUgFR3FPjaQHxNCXy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7c260dc-e4ca-4728-b00b-23f2db5bcef6",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59674d57-e1d5-4092-90b6-771df417bf74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T12:13:28.403Z_

<details><summary>↩ Tool result · `toolu_018rXSWnUgFR3FPjaQHxNCXy`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
11	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
12	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
13	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero---the tension between model quality and selection utility is inherent.
14	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
15	Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
16	Meanwhile, LP selection approximately matches greedy decoding ($T{=}0$; $\Delta{=}{+}0.2$~pp, $p{=}0.29$; Table~\ref{tab:selection}), and both fall far short of the oracle (0.778, 13.3~pp gap)---multi-sample selection adds cost without closing the gap.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
22	\label{tab:degeneracy}
23	\begin{tabular}{lccc}
24	\toprule
25	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
26	\midrule
27	Constant F1 & 21\% & 10.4\% & 58\% \\
28	Constant utility & 13\% & 7.0\% & 49\% \\
29	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
30	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	Log-probability, the only per-sample signal, is severely compressed: median LP range is 0.041 nats (IQR [0.024, 0.073]; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ confirming weak but positive signal.
36	Where compression is mitigated ($n{=}210$ instances with above-median LP spread), LP selection outperforms single-sample ($+2.9$~pp, $p{=}0.004$), suggesting compression as a bottleneck; this subset analysis uses $\varepsilon{=}0.05$ tie-breaking, and the effect size is sensitive to subset definition (Appendix~\ref{app:diversity}).
37	Stratifying by voting confidence reveals a complementary pattern: high-consistency instances (Q4) have collapsed headroom (4.78~pp), leaving nothing to select, while low-consistency instances retain headroom but unreliable LP rankings (Appendix~\ref{app:vc_quartile}).
38	Doubling to $N{=}16$ expands oracle headroom by $+4.4$~pp without improving selection (Appendix~\ref{app:n_scaling}).
39	A verbalized confidence baseline confirms that score compression is not LP-specific: the model's self-rated confidence (mean 8.6/10) is even more compressed and yields the weakest selection despite higher $\rho$ than LP (Appendix~\ref{app:verbalized_confidence}; \citealp{bhattacharyya2026beyond}).
40	
41	\paragraph{Signal combinations.}
42	We test three LP${\times}$VC combination strategies: VC-stratified LP selection, LP${\times}$VC product ranking, and LP tiebreaking within VC-equivalent groups.
43	All three fail to improve over greedy (best: $+0.2$~pp, $p{>}0.3$), consistent with VC's collapse on degenerate instances and LP's compression on the remainder.
44	An oracle tiebreaker---selecting the highest-F1 sample among VC-equivalent candidates---recovers $+7.9$~pp, confirming that per-sample signal \textit{exists} within VC-equivalent groups but current signals cannot extract it.
45	
46	\paragraph{Hypotheses for LP compression.}
47	We identify four (non-mutually-exclusive) mechanisms that may explain within-instance LP compression, though we do not isolate their individual contributions.
48	Two are \textit{constraint-imposed}:
49	(b) \textit{schema-dominated tokens}---constrained decoding enforces structural tokens (brackets, type labels) that carry no extraction information yet dominate the sequence, reducing effective variance;
50	(c) \textit{vocabulary restriction}---constrained decoding shrinks the effective vocabulary at each step, concentrating probability mass and reducing log-probability variation.
51	Two are \textit{model-learned}:
52	(a) \textit{token-level averaging}---mean log-probability over long sequences smooths token-level variance, compressing the effective signal;
53	(d) \textit{format-token dilution}---fine-tuned models assign extremely high LP to schema tokens (\texttt{\{"entities": [}~etc.) that carry no extraction information, diluting the signal from entity-name tokens; free-form parse rates of 99.95\% confirm that format tokens dominate the sequence.
54	The constraint-imposed mechanisms (b)--(c) predict that free-form decoding should reduce compression; our NER ablation finds negligible change (std ratio 0.97; Appendix~\ref{app:freeform_ablation}), suggesting the model-learned mechanisms (a) and (d) are the primary drivers for NER.
55	
56	\paragraph{Ablation: free-form decoding.}\label{sec:ablation}
57	Removing grammar constraints (SciERC NER, Qwen3-8B, 4 seeds) yields nearly identical LP distributions (std ratio 0.97) and negligible selection changes (Appendix~\ref{app:freeform_ablation}), ruling out constrained decoding as the cause of NER compression.
58	On RE, free-form decoding consistently reverses LP selection direction ($+1.8{\pm}0.1$~pp, 4 seeds), suggesting regime-dependent behavior (Appendix~\ref{app:re_extension}).
59	VC becomes per-sample in the selection context (each candidate's overlap with the majority-voted output varies), yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias \cite{eikema2022sampling, deguchi2024centroid}.
60	More broadly, all consensus-proximity strategies fail because instance degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Table~\ref{tab:degeneracy}; Appendix~\ref{app:mbr_discussion}).
61	
62	\paragraph{Ablation: entity-token LP.}
63	We directly test hypothesis (d) by isolating entity-mention tokens from the log-probability computation.
64	On SciERC, entity-token LP exhibits $4{\times}$ higher within-instance variance than full-sequence LP, confirming that format tokens do compress the signal.
65	However, entity-token LP selection performs \textit{worse} than full-sequence LP ($-2.0$~pp), and on CoNLL, entity-token LP variance collapses to near-zero (median $2{\times}10^{-10}$) with 79\% of instances tied---consistent with CoNLL's limited entity vocabulary (4 types, high-frequency names) that fine-tuning drives to near-deterministic prediction.
66	This rules out format-token dilution as the primary cause of LP's selection failure and instead points to an intrinsic pattern: fine-tuned models assign near-deterministic probabilities to entity-name tokens themselves, leaving minimal discriminative signal regardless of aggregation scope.
67	
68	\paragraph{Pilot remedy.}
69	Entity-token LP represents a natural pilot remedy: if format-token dilution caused compression, restricting LP to entity tokens should recover selection ability.
70	Its failure---particularly the near-zero entity-token variance on CoNLL---suggests that effective remedies must address the underlying model confidence calibration rather than signal aggregation.
71	
72	\paragraph{Practical considerations.}
73	Multi-sample inference incurs $N{\times}$ compute cost.
74	For quality estimation---where signals are already reliable ($\rho$ up to 0.45, AUROC up to 0.82)---$N{=}8$ samples suffice (Appendix~\ref{app:n_scaling}), making the cost acceptable for selective prediction or error flagging in high-stakes IE.
75	For selection, the cost-benefit is unfavorable: $8{\times}$ inference yields at most $+0.2$~pp over greedy ($p{>}0.05$).
76	Whether the trade-off shifts in low-convergence regimes (e.g., under-parameterized models where degeneracy drops below 10\%) remains an open question.
77	
78	\paragraph{Methodological implications.}
79	The decoupling of $\rho$, AUROC, and selection F1 means single-metric evaluation risks selecting the wrong signal.
80	Even supervised combination of all five signals closes ${<}1\%$ of the oracle gap (\S\ref{sec:robustness_main}), confirming the information bottleneck is in the features themselves, not the aggregation method.
81	Effective selection thus requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers, venktesh2025trust}, not confidence signal aggregation; $N{=}8$ captures most quality estimation benefit (Appendix~\ref{app:n_scaling}).
82	Structural signals are robust to domain shift when the training schema subsumes the target (Appendix~\ref{app:ood}).
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59674d57-e1d5-4092-90b6-771df417bf74",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "7f9d6d6b-8cb1-44ab-ae99-6d1f61112986",
  "sourceToolAssistantUUID": "59674d57-e1d5-4092-90b6-771df417bf74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T12:13:28.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZtBbhEqTRK9aCtb76hpqQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f9d6d6b-8cb1-44ab-ae99-6d1f61112986",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f3e0169-2e31-408b-b9ce-0b8022b37651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T12:13:28.946Z_

<details><summary>↩ Tool result · `toolu_01TZtBbhEqTRK9aCtb76hpqQ`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER.
4	Structural and surface agreement signals reliably predict output quality ($\rho$ up to 0.45, AUROC up to 0.82), supporting selective prediction and error flagging regardless of selection regime.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: selection approximately matches greedy decoding ($T{=}0$) despite 13--18~pp oracle headroom.
6	The gap stems from two jointly operating mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, scaling with model capability) and LP compression (median within-instance range of 0.041 nats).
7	A LoRA-rank ablation reduces degeneracy from 21\% to 7\% without enabling selection, confirming that low degeneracy is necessary but not sufficient; diagnostic ablations confirm both mechanisms are intrinsic to capable fine-tuned models rather than artifacts of constrained decoding.
8	Signal rankings shift with task difficulty and collapse at the capability boundary in the 3B--8B range tested; whether these mechanisms persist at 70B+ scales is an open question.
9	A supervised verifier combining all five signals closes ${<}1\%$ of the oracle gap, confirming the bottleneck is in the features, not the aggregation.
10	Closing the gap requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}, not confidence signal combination; an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) is a promising direction.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f3e0169-2e31-408b-b9ce-0b8022b37651",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "a21f3c12-6c05-4256-9f73-175b04533ace",
  "sourceToolAssistantUUID": "7f3e0169-2e31-408b-b9ce-0b8022b37651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T12:13:29.445Z_

<details open><summary>🔧 Tool call — Read · `toolu_015gKMgQfav7synGxg2EWqyc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a21f3c12-6c05-4256-9f73-175b04533ace",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd9ddedb-dc2a-40ff-8b1b-10e2e24855ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T12:13:29.449Z_

<details><summary>↩ Tool result · `toolu_015gKMgQfav7synGxg2EWqyc`</summary>

```text
1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing within-instance variance on SciERC ($4{\times}$); LP${\times}$VC combinations also fail to recover selection (\S\ref{sec:discussion}); calibration-based approaches remain unexplored.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd9ddedb-dc2a-40ff-8b1b-10e2e24855ec",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "405aab2a-4a1d-4998-bf89-3c0fbef6981c",
  "sourceToolAssistantUUID": "fd9ddedb-dc2a-40ff-8b1b-10e2e24855ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-16T12:13:29.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VzycPTQ7pRxJt1vUjMvib8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "405aab2a-4a1d-4998-bf89-3c0fbef6981c",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBPcqXMNPAjHQBBXYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4f4d5ab-5411-4293-8599-9a8873afba57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtikUWRCp2xMmMcP4DSZy1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14465,
      "cache_read_input_tokens": 20297,
      "output_tokens": 620,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 620,
          "cache_read_input_tokens": 20297,
          "cache_creation_input_tokens": 14465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14465,
            "ephemeral_1h_input_tokens": 0
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

_source line 35 · 2026-05-16T12:13:30.216Z_

<details><summary>↩ Tool result · reported error · `toolu_01VzycPTQ7pRxJt1vUjMvib8`</summary>

```text
File content (26389 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4f4d5ab-5411-4293-8599-9a8873afba57",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "23def058-e505-42bc-b054-f3c21d148ecf",
  "toolUseResult": "Error: File content (26389 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "f4f4d5ab-5411-4293-8599-9a8873afba57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-16T12:13:32.670Z_

The appendix is large. Let me read it in parts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23def058-e505-42bc-b054-f3c21d148ecf",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBxG8LGUBZ3rFS5mTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9579eb76-8a8f-4783-acf0-b9db5ded6cd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rznw8X5qCJJ6v5dYQZfJYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13004,
      "cache_read_input_tokens": 34762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T12:13:34.563Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AE2RZYzotzLRBcDVaTjWuT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9579eb76-8a8f-4783-acf0-b9db5ded6cd3",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBxG8LGUBZ3rFS5mTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36748f33-9fc6-4236-8570-faed1af91076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rznw8X5qCJJ6v5dYQZfJYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13004,
      "cache_read_input_tokens": 34762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T12:13:34.946Z_

<details><summary>↩ Tool result · `toolu_01AE2RZYzotzLRBcDVaTjWuT`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
48	\quad LP & $T{=}0.7$ & 0.249 & --- \\
49	\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\
50	\midrule
51	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
52	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
53	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
54	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
55	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
56	\midrule
57	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
58	\quad SJ &  & $0.474{\pm}0.009$ & --- \\
59	\quad FK &  & $0.467{\pm}0.009$ & --- \\
60	\quad EM &  & $0.473{\pm}0.010$ & --- \\
61	\quad VC &  & $0.470{\pm}0.006$ & --- \\
62	\quad LP &  & $0.311{\pm}0.003$ & --- \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
70	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
71	\label{fig:temperature_robustness}
72	\end{figure}
73	
74	\paragraph{Temperature sensitivity.}
75	SJ NER $\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.
76	FK NER $\rho$ drops by 0.022, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
77	LP exhibits the largest temperature effect on NER ($\rho{=}0.249$ at $T{=}0.7$ vs.\ $0.205$ at $T{=}1.0$, $\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.
78	Across all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).
79	
80	\paragraph{Sample size scaling.}
81	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
82	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
83	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\ref{tab:quality_estimation}).
84	FK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.
85	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
86	SJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, suggesting that structural and binary-agreement signals are the most robust to $N$.
87	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
88	
89	\paragraph{Transfer across model families.}
90	LLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$, $\Delta\rho{=}0.069$; permutation $p{=}0.06$, borderline).
91	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
92	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$),\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.474{\pm}0.009$ vs.\ LP $0.311{\pm}0.003$, $\Delta{=}{+}0.163$).
93	
94	\paragraph{FK independence: instance-level permutation test.}\label{app:fk_independence}
95	
96	To verify that Fleiss' $\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.
97	For each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
103	\label{tab:fk_independence}
104	\begin{tabular}{lrcccc}
105	\toprule
106	Config & $n$ & FK mean & 95\% CI & $t$ & Split-half $r$ \\
107	\midrule
108	SciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\
109	CoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\
110	CoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:fk_independence} reports the results.
116	All configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), confirming that FK captures genuine inter-sample agreement rather than chance label co-occurrence.
117	Split-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), indicating moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.
118	The higher FK means on CoNLL ($0.720$--$0.927$) vs.\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.
119	
120	\section{Calibration Analysis}\label{app:calibration}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{fig_reliability}
125	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
126	\label{fig:reliability}
127	\end{figure*}
128	
129	Reliability diagrams use 10 equal-width bins.
130	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
131	
132	\section{Additional Analyses}\label{app:additional}
133	
134	\begin{figure*}[t]
135	\centering
136	\includegraphics[width=\textwidth]{fig_signal_heatmap}
137	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
138	\label{fig:signal_heatmap}
139	\end{figure*}
140	
141	\paragraph{Per-relation diagnostic.}
142	RE signal degradation is relation-specific.
143	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
144	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
145	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
146	
147	\paragraph{Capability stratification.}
148	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
149	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
150	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
151	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
152	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
153	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
154	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
155	
156	\paragraph{Length vs.\ log-probability.}
157	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
158	
159	\begin{figure}[t]
160	\centering
161	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
162	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
163	\label{fig:length_logprob_scatter}
164	\end{figure}
165	
166	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
167	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
168	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
169	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
170	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
171	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
172	Evaluation circularity is negligible.
173	
174	\paragraph{SJ normalizer robustness.}
175	Equation~\ref{eq:sj} uses $\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \cup g_j|$.
176	Table~\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\Delta\rho|{<}0.01$ in every case, confirming that the choice between max and union normalization does not affect conclusions.
177	
178	\begin{table}[h]
179	\centering
180	\small
181	\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
182	\label{tab:sj_normalizer}
183	\begin{tabular}{@{}ll ccc@{}}
184	\toprule
185	Dataset & Model & $\rho$(max) & $\rho$(union) & $\Delta\rho$ \\
186	\midrule
187	CoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\
188	CoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\
189	CoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\
190	SciERC & Qwen3-8B & .360 & .365 & $-$.005 \\
191	SciERC & Qwen3-4B & .422 & .423 & $-$.001 \\
192	SciERC & LLaMA-8B & .363 & .372 & $-$.009 \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	\paragraph{Conditional filtering details.}
198	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\Delta\rho{=}{-}0.005$, $p{=}0.53$; preliminary).
199	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
217	\toprule
218	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
219	\midrule
220	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
221	FK      & .125 & .001 & .555 & .169 & .002 \\
222	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
223	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
224	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Cross-configuration selection analysis.}
230	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
231	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
232	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
233	
234	\begin{table*}[t]
235	\centering
236	\small
237	\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
238	\label{tab:cross_selection}
239	\begin{tabular}{llccccccc}
240	\toprule
241	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
242	\midrule
243	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
244	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
245	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
246	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
247	\bottomrule
248	\end{tabular}
249	\end{table*}
250	
251	\paragraph{Diminishing returns of $N$-scaling.}
252	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
253	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
254	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
255	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
256	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
257	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
258	
259	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
260	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
261	VC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
262	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
263	This reinforces the primary finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
264	
265	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
266	
267	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
268	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
269	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
270	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
276	\label{tab:bootstrap_signal_ci}
277	\begin{tabular}{lcc}
278	\toprule
279	Signal & $\rho$ & 95\% CI \\
280	\midrule
281	VC & +0.379 & [+0.299, +0.456] \\
282	SJ & +0.360 & [+0.277, +0.437] \\
283	EM & +0.295 & [+0.212, +0.371] \\
284	FK & +0.267 & [+0.176, +0.354] \\
285	LP & +0.205 & [+0.119, +0.291] \\
286	\bottomrule
287	\end{tabular}
288	
289	\vspace{0.5em}
290	
291	\begin{tabular}{lccc}
292	\toprule
293	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
294	\midrule
295	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
296	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
297	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
298	\bottomrule
299	\end{tabular}
300	
301	\smallskip
302	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
303	\end{table}
304	
305	At $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.
306	On SciERC NER ($n{=}529$), SJ--FK ($\Delta\rho{=}0.147$--$0.160$, all $p{\leq}0.002$) and VC--FK ($\Delta\rho{=}0.138$--$0.188$, all $p{\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\Delta\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).
307	On CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\Delta\rho{=}0.071$ ($p{<}0.001$), SJ $\Delta\rho{=}0.056$ ($p{<}0.001$), VC $\Delta\rho{=}0.022$ ($p{=}0.040$).
308	
309	\section{Diversity and Selection Analysis}\label{app:diversity}
310	
311	\begin{figure*}[t]
312	\centering
313	\includegraphics[width=\textwidth]{fig_selection_gap}
314	\caption{The correlation-selection gap on SciERC NER ($N{=}8$, $T{=}1.0$, 2-seed mean). Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.40, no signal significantly outperforms single-sample (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound. RE selection results in Table~\ref{tab:selection}.}
315	\label{fig:selection_gap}
316	\end{figure*}
317	
318	\paragraph{Output diversity quantification.}
319	Table~\ref{tab:diversity} summarizes output diversity across configurations.
320	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
321	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
322	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where single-sample F1 already exceeds 0.90.
323	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
324	
325	\begin{table}[t]
326	\centering
327	\small
328	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
329	\label{tab:diversity}
330	\begin{tabular}{lcc}
331	\toprule
332	Config & Identical & Unique \\
333	\midrule
334	Qwen/SciERC & 11\% & 43\% \\
335	LLaMA/SciERC & 18\% & 39\% \\
336	Qwen/CoNLL & 57\% & --- \\
337	LLaMA/CoNLL & 88\% & --- \\
338	WNUT-17 & 55\% & --- \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	\paragraph{Oracle-improvable fraction.}
344	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding single-sample\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \S\ref{sec:evaluation}); the diversity quantification in Table~\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
345	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
346	
347	\paragraph{Diversity-stratified selection gap.}
348	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
349	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.
350	This rules out insufficient diversity as an explanation for the correlation-selection gap.
351	
352	\paragraph{TOST equivalence testing.}\label{app:tost}
353	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
354	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
355	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
356	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.
357	We address this below with externally anchored equivalence margins.
358	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
359	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
360	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
361	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
362	
363	\begin{table}[t]
364	\centering
365	\small
366	\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
367	\label{tab:tost}
368	\begin{tabular}{l cccc cccc}
369	\toprule
370	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
371	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
372	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
373	\midrule
374	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
375	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
376	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
377	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
378	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
379	\bottomrule
380	\end{tabular}
381	\end{table}
382	
383	\paragraph{External equivalence margins.}
384	The oracle-headroom anchors above introduce circularity, as a reviewer correctly noted: $\delta$ is calibrated against the very quantity it contextualizes.
385	To resolve this, we supplement with three externally grounded margins:
386	(1) $\delta_{\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), representing measurement noise;
387	(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, reflecting the threshold below which NER differences are considered negligible \cite{ratinov2009design};
388	(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
389	
390	Results under these external anchors diverge sharply by configuration.
391	On LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\Delta|{\leq}0.1$~pp) and tight CIs at this sample size.
392	On Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, exceeding even $\delta_{\mathrm{literature}}$.
393	On SciERC NER ($n{=}529$), only SJ passes at $\delta_{\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.
394	These external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.
395	
396	\paragraph{Multiple comparison considerations.}\label{app:multiple_comparisons}
397	Our primary selection analysis involves ${\sim}$20 comparisons (5 signals $\times$ 3--4 configurations).
398	Since all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.
399	The sole positive finding---non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \S\ref{sec:discussion})---survives Bonferroni correction over 5 signal comparisons ($p_{\mathrm{adj}}{=}0.020 < 0.05$), as noted in the main text footnote.
400	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36748f33-9fc6-4236-8570-faed1af91076",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "ac4356de-e0ca-4249-a5f7-ff288d00d922",
  "sourceToolAssistantUUID": "36748f33-9fc6-4236-8570-faed1af91076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T12:13:35.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_014jKDaCTrtzURdGHhcaVxdS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4356de-e0ca-4249-a5f7-ff288d00d922",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBxG8LGUBZ3rFS5mTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65b12870-234b-4d5e-b8db-6cfb664bda24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rznw8X5qCJJ6v5dYQZfJYP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13004,
      "cache_read_input_tokens": 34762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T12:13:35.556Z_

<details><summary>↩ Tool result · `toolu_014jKDaCTrtzURdGHhcaVxdS`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy scales with model capability: CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
13	This creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
15	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar}; recent work highlights hidden costs of constrained generation for log-probability estimation \cite{schall2025hidden} and inference efficiency \cite{yun2025price}.
17	
18	\paragraph{Uncertainty estimation and calibration.}
19	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibration \cite{hobelsberger2025systematic} for LLMs.
20	Semantic uncertainty \cite{kuhn2023semantic} clusters generations by meaning; P(True) \cite{kadavath2022language} queries model confidence directly; \citet{malinin2021uncertainty} study predictive uncertainty for autoregressive structured prediction.
21	Our structural signals instead measure agreement over output \textit{structure}, requiring no model modification.
22	Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid} with structural utility functions.
23	Unlike machine translation where MBR yields consistent gains \cite{freitag2022high}, we find that utility \textit{is} aligned with quality (within-instance SJ--F1 $\rho{=}0.52$) but instance degeneracy eliminates the headroom MBR would otherwise exploit.
24	\citet{eikema2025structured} find that standard MBR utilities degrade on structured outputs due to bag-of-unit mismatches; our diagnosis is complementary---the bottleneck is not utility misalignment but output concentration driven by model capability (\S\ref{sec:discussion}).
25	\citet{xie2024selfevaluation} show self-evaluation improves selective generation for discrete tasks; our results suggest this does not transfer to structured extraction without learned scoring.
26	Our quality estimation results connect to selective prediction \cite{kuleshov2015calibrated}: signals with $\rho$ up to 0.45 and AUROC up to 0.82 can support abstention policies that flag low-quality extractions, providing practical value independent of sample selection.
27	Conformal prediction constructs prediction sets with coverage guarantees \cite{zhang2025conformal}; while complementary, its set-valued output differs from best-of-$N$ selection.
28	
29	\paragraph{Best-of-$N$ with learned verifiers.}
30	\citet{gao2023scaling} establish scaling laws for best-of-$N$ selection with learned reward models, showing that BoN performance scales log-linearly with $N$ but eventually degrades due to reward overoptimization.
31	Our unsupervised signals face a more fundamental limitation: they cannot rank candidates at all (instance-level signals) or rank them too weakly (LP compression), making the overoptimization regime irrelevant.
32	Trained verifiers \cite{cobbe2021verifiers, lightman2024verify} and quality-aware decoding \cite{fernandes2022quality} learn per-sample scoring that may bridge this gap; our LoRA-rank ablation (degeneracy 7\% vs.\ 21\%, selection still fails) suggests that verifier training is necessary beyond merely increasing output diversity.
33	Fine-tuning itself contributes to the problem: \citet{kirk2024understanding} document diversity collapse in RLHF-trained models; our instance degeneracy is an analogous phenomenon in supervised fine-tuning, where stronger models converge to more uniform outputs.
34	Nucleus sampling \cite{holtzman2020curious} improves diversity in open-ended generation, but our constrained structured outputs limit the diversity that temperature scaling alone can recover.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65b12870-234b-4d5e-b8db-6cfb664bda24",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "ac966932-b3fe-4f1d-bb61-381b7bbc3620",
  "sourceToolAssistantUUID": "65b12870-234b-4d5e-b8db-6cfb664bda24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T12:13:35.690Z_

<details open><summary>🔧 Tool call — Read · `toolu_017rWLDg4sGvBwcfiowyJwkc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac966932-b3fe-4f1d-bb61-381b7bbc3620",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EBxG8LGUBZ3rFS5mTj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dcf2949-2def-475d-a7fd-068818451d11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rznw8X5qCJJ6v5dYQZfJYP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13004,
      "cache_read_input_tokens": 34762,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 34762,
          "cache_creation_input_tokens": 13004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13004,
            "ephemeral_1h_input_tokens": 0
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

_source line 42 · 2026-05-16T12:13:35.693Z_

<details><summary>↩ Tool result · `toolu_017rWLDg4sGvBwcfiowyJwkc`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dcf2949-2def-475d-a7fd-068818451d11",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "cf0a1125-c328-4a4e-af77-147a3e07fa9a",
  "sourceToolAssistantUUID": "3dcf2949-2def-475d-a7fd-068818451d11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T12:13:38.783Z_

Now let me read the rest of the appendix to check for numerical consistency and additional claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf0a1125-c328-4a4e-af77-147a3e07fa9a",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ECMy9XsodNcXumDFbG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9718a81-5ada-4577-ab5a-325dd879d6bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXM9dFLcXox7jTL52RN4Kg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14880,
      "cache_read_input_tokens": 47766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14880,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T12:13:40.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H3bF8f4jWRuqjTrj5sYm1f`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 400,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9718a81-5ada-4577-ab5a-325dd879d6bb",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ECMy9XsodNcXumDFbG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dab489d-fffa-4514-909e-c1f53bedd94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXM9dFLcXox7jTL52RN4Kg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14880,
      "cache_read_input_tokens": 47766,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14880
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 47766,
          "cache_creation_input_tokens": 14880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14880,
            "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-16T12:13:40.880Z_

<details><summary>↩ Tool result · `toolu_01H3bF8f4jWRuqjTrj5sYm1f`</summary>

```text
400	For quality estimation signal rankings, differences between the top signals (e.g., VC vs.\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.
401	
402	\section{Multi-Seed Stability}\label{app:multiseed}
403	
404	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
405	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals (rankings are stable across our 3 seeds, though statistical power with $n{=}3$ is limited).
406	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
407	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
408	
409	\begin{table}[t]
410	\centering
411	\small
412	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
413	\label{tab:multiseed}
414	\begin{tabular}{lccccc}
415	\toprule
416	& LP & FK & SJ & VC & EM \\
417	\midrule
418	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
419	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
420	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
421	\midrule
422	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
423	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
424	\midrule
425	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
426	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
427	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	\section{Training Configuration}\label{app:training}
433	
434	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
435	
436	\begin{table}[t]
437	\centering
438	\small
439	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
440	\label{tab:training}
441	\begin{tabular}{ll}
442	\toprule
443	Parameter & Value \\
444	\midrule
445	LoRA rank / $\alpha$ & 32 / 64 \\
446	LoRA target & All linear modules \\
447	LoRA dropout & 0 \\
448	Optimizer & AdamW \\
449	Learning rate & 2e-4, cosine schedule \\
450	Warmup ratio & 0.1 \\
451	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
452	Epochs & 5 \\
453	Max sequence length & 2048 \\
454	Precision & bf16 \\
455	Gradient checkpointing & Enabled \\
456	Max gradient norm & 1.0 \\
457	Training seed & 42 \\
458	Framework & LLaMA Factory \\
459	\midrule
460	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
461	SciERC split & 1861 / 275 / 551 \\
462	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
463	& eval\_steps${=}$200, save\_limit${=}$5 \\
464	\bottomrule
465	\end{tabular}
466	\end{table}
467	
468	\paragraph{Prompt template.}
469	For NER, we use a structured prompt:
470	\begin{quote}
471	\small
472	\texttt{System:} You are an expert in Named Entity Recognition.\\
473	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
474	Text: \texttt{\{input\_text\}}\\
475	Entity types: \texttt{\{schema\_types\}}
476	\end{quote}
477	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
478	
479	\paragraph{Constrained decoding.}
480	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
481	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
482	
483	\section{Thinking Token Impact Analysis}\label{app:thinking_token}
484	
485	Qwen3-8B's SciERC checkpoint was trained with empty \texttt{&lt;think>&lt;/think>} blocks prepended to each response (\S\ref{sec:setup}).
486	We quantify the potential impact on LP scores through three complementary arguments.
487	
488	\paragraph{LP shift magnitude.}
489	Empty thinking tokens (mean 4.5 per sample) constitute 2.1\% of tokens on SciERC.
490	The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
491	Because all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\%$ of instances.
492	
493	\paragraph{Constant prefix cancellation.}
494	All $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.
495	Any LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \textit{rankings} unchanged.
496	
497	\paragraph{CoNLL control group.}
498	CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
499	If thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.
500	Instead, CoNLL shows \textit{higher} tied fractions at both temperatures (86.8\% at $T{=}1.0$, 95.8\% at $T{=}0.7$) than SciERC (60.3\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.
501	
502	\section{Log-Probability Score Compression}\label{app:logprob_ties}
503	
504	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
505	The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
506	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
507	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
508	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
509	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
510	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
511	
512	\begin{figure}[t]
513	\centering
514	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
515	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
516	\label{fig:lp_range_cdf}
517	\end{figure}
518	
519	\begin{table}[t]
520	\centering
521	\small
522	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
523	\label{tab:logprob_ties}
524	\begin{tabular}{lc}
525	\toprule
526	$\varepsilon$ threshold & Tied instances (\%) \\
527	\midrule
528	0.01 & 1.1\% \\
529	0.05 & 60.3\% \\
530	0.1  & ${\sim}$84\% \\
531	0.5  & ${\sim}$99\% \\
532	\bottomrule
533	\end{tabular}
534	\end{table}
535	
536	\paragraph{Non-tied subset.}
537	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
538	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
539	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
540	
541	\paragraph{$\varepsilon$ sensitivity sweep (post-hoc exploratory).}
542	Table~\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.
543	The tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.
544	$\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\varepsilon{\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\leq}36$).
545	
546	\begin{table}[t]
547	\centering
548	\small
549	\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
550	\label{tab:epsilon_sweep}
551	\begin{tabular}{ccccc}
552	\toprule
553	$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
554	\midrule
555	0.01 & 1.1\% & 523 & $+$0.58 & .21 \\
556	0.02 & 13.6\% & 457 & $+$0.83 & .15 \\
557	0.03 & 31.8\% & 361 & $+$1.31 & .079 \\
558	\textbf{0.05} & \textbf{60.3\%} & \textbf{210} & \textbf{$+$2.86} & \textbf{.004} \\
559	0.10 & 83.9\% & 85 & $+$3.69 & .034 \\
560	0.15 & 93.2\% & 36 & $+$4.15 & .11 \\
561	0.20 & 96.4\% & 19 & $+$4.59 & .13 \\
562	\bottomrule
563	\end{tabular}
564	\end{table}
565	
566	\paragraph{$\varepsilon$ robustness of selection F1.}\label{app:epsilon_robustness}
567	The preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\varepsilon$ to define MBR-style proximity in selection.
568	Table~\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\varepsilon \in [0, 0.2]$ for all signals and configurations.
569	At $\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.
570	Spearman $\rho$---the primary quality estimation metric throughout---is a continuous rank correlation that does not depend on any discretization threshold; the $\varepsilon$ parameter affects only the selection analysis.
571	
572	\begin{table}[t]
573	\centering
574	\small
575	\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ governs its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
576	\label{tab:epsilon_robustness}
577	\begin{tabular}{lcccc}
578	\toprule
579	& \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL}} \\
580	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
581	Signal & Qwen & LLaMA & Qwen & LLaMA \\
582	\midrule
583	SJ & 0.92 & 1.45 & 0.99 & 0.18 \\
584	FK & 1.03 & 0.93 & 0.60 & 0.15 \\
585	VC & 2.33 & 0.53 & 0.72 & 0.18 \\
586	EM & 0.00 & 0.00 & 0.00 & 0.00 \\
587	LP & 3.65 & 2.58 & 3.00 & 0.31 \\
588	\bottomrule
589	\end{tabular}
590	\end{table}
591	
592	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
593	
594	Table~\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\Delta$ (gain over single-sample) for LP and SJ.
595	
596	\begin{table}[t]
597	\centering
598	\small
599	\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
600	\label{tab:vc_quartile}
601	\begin{tabular}{lcccc}
602	\toprule
603	Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
604	\midrule
605	\multicolumn{5}{l}{\textit{NER}} \\
606	Q1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\
607	Q2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\
608	Q3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\
609	Q4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\
610	\midrule
611	\multicolumn{5}{l}{\textit{$^\dagger$RE}} \\
612	Q1 (low) & --- & $-$3.56 & --- & --- \\
613	Q4 (high) & --- & $+$4.01 & --- & --- \\
614	\bottomrule
615	\end{tabular}
616	\end{table}
617	
618	The NER pattern reveals two complementary failure modes rather than a monotonic relationship between consistency and selection gain:
619	\begin{itemize}
620	\item \textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp---samples have already converged, leaving little room for any signal to improve selection.
621	\item \textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, yielding inconsistent $\Delta$ signs across quartiles.
622	\end{itemize}
623	
624	On $^\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp, suggesting LP can recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.
625	
626	On CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), yielding $\Delta{=}0$ universally---a ceiling effect even more extreme than SciERC Q4.
627	
628	\section{Exploratory Extension to Relation Extraction}\label{app:re_extension}
629	
630	We extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.
631	RE produces sets of (head, relation, tail) triples with partial overlap; 40\% of RE instances receive zero F1, and entity span errors account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect (\S\ref{app:additional}).
632	All RE results use Qwen3-8B unless noted; single-seed ($\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.
633	
634	\paragraph{Quality estimation.}
635	RE quality estimation is reported in Table~\ref{tab:multiseed} (3-seed means).
636	The signal ranking differs from NER: VC leads ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal reflecting RE's higher sensitivity to per-sample scoring.
637	RE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\ref{fig:reliability}).
638	
639	\paragraph{Selection.}
640	Table~\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.
641	At $N{=}16$ (Qwen3-4B, Table~\ref{tab:re_n16_selection}), LP is the sole positive signal ($\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.
642	
643	\paragraph{Scale ablation.}
644	At 4B scale (Qwen3-4B, $N{=}8$, $\text{seed}{=}42$), RE quality estimation shows FK $\rho{=}0.359$ and LP $\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\ $0.250$).
645	Selection remains below single-sample on RE ($\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.
646	
647	\paragraph{Free-form decoding.}
648	RE LP selection consistently reverses direction under free-form decoding ($+1.8{\pm}0.1$~pp across 4 seeds vs.\ $-0.9$~pp under constrained decoding at 8B; \S\ref{app:freeform_ablation}), suggesting constrained decoding's fixed template obscures LP signal in RE (\S\ref{app:mbr_discussion}).
649	
650	\section{RE Conditional Selection}\label{app:re_conditional_selection}
651	
652	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
653	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
654	All five signals underperform single-sample on both subsets.
655	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
656	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
657	
658	\begin{table}[t]
659	\centering
660	\small
661	\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
662	\label{tab:re_cond_selection}
663	\begin{tabular}{lcc}
664	\toprule
665	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
666	\midrule
667	Oracle & 0.585 & 0.757 \\
668	\midrule
669	LP & 0.395 & 0.600 \\
670	SJ & 0.386 & 0.604 \\
671	EM & 0.372 & 0.583 \\
672	VC & 0.359 & 0.574 \\
673	\midrule
674	Greedy & 0.404 & 0.674 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	\section{RE $N{=}16$ Selection Analysis}\label{app:re_n16_selection}
680	
681	Table~\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.
682	All four consistency signals underperform single-sample, with EM showing the largest deficit ($\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).
683	LP is the only positive signal ($\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).
684	Even the most favorable seed captures only ${\sim}9\%$ of the 17.1~pp oracle headroom.
685	This cross-task consistency---LP as the only viable selection signal on both NER and RE---reinforces the structural limitation of instance-level signals for candidate ranking.
686	
687	\begin{table}[t]
688	\centering
689	\small
690	\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
691	\label{tab:re_n16_selection}
692	\begin{tabular}{lccc}
693	\toprule
694	Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
695	\midrule
696	Oracle & $.463{\pm}.006$ & $+$17.1 & --- \\
697	\midrule
698	LP & $\mathbf{.299}{\pm}.007$ & $+$0.7 & .058 \\
699	VC & $.284{\pm}.002$ & $-$0.8 & .973 \\
700	FK & $.283{\pm}.005$ & $-$0.9 & .985 \\
701	SJ & $.281{\pm}.005$ & $-$1.0 & .993 \\
702	EM & $.277{\pm}.007$ & $-$1.5 & .999 \\
703	\midrule
704	Greedy & $.291{\pm}.000$ & --- & --- \\
705	Random & $.262{\pm}.001$ & $-$2.9 & --- \\
706	\bottomrule
707	\end{tabular}
708	\end{table}
709	
710	\section{MBR Decoding and Task-Specific Interactions}\label{app:mbr_discussion}
711	
712	\paragraph{Connection to MBR decoding.}
713	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
714	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy---the core of the correlation-selection gap.
715	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
716	
717	\paragraph{Task-specific decoding interactions.}
718	The free-form ablation reveals divergent behavior across tasks.
719	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
720	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
721	This interaction does not generalize to NER, where selection remains negligible under both regimes.
722	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
723	The non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
724	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
725	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
726	
727	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
728	
729	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).
730	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
731	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
732	RE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\ $-0.68$~pp constrained.
733	The constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.
734	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
735	
736	\begin{table*}[t]
737	\centering
738	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
739	\label{tab:freeform_ablation}
740	
741	\vspace{2pt}
742	{\small\textsc{Panel A: Logprob Distribution}}
743	\vspace{2pt}
744	
745	\begin{tabular}{lccc}
746	\toprule
747	Metric & Constrained & Free-form & $\Delta$ \\
748	\midrule
749	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
750	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
751	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
752	\bottomrule
753	\end{tabular}
754	
755	\vspace{8pt}
756	
757	{\small\textsc{Panel B: Selection F1}}
758	\vspace{2pt}
759	
760	\begin{tabular}{llccc}
761	\toprule
762	Task & Method & Constrained & Free-form & $\Delta$ \\
763	\midrule
764	\multirow{3}{*}{NER}
765	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
766	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
767	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
768	\midrule
769	\multirow{3}{*}{RE}
770	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
771	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
772	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
773	\bottomrule
774	\end{tabular}
775	
776	\vspace{8pt}
777	
778	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
779	\vspace{2pt}
780	
781	\begin{tabular}{l ccc ccc}
782	\toprule
783	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
784	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
785	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
786	\midrule
787	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
788	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
789	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
790	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
791	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
792	\bottomrule
793	\end{tabular}
794	
795	\vspace{8pt}
796	
797	{\small\textsc{Panel D: Parse Rate (Free-form)}}
798	\vspace{2pt}
799	
800	\begin{tabular}{lc}
801	\toprule
802	Metric & Value \\
803	\midrule
804	Total samples          & 4408 \\
805	Parse rate             & 99.95\% \\
806	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
807	\bottomrule
808	\end{tabular}
809	
810	\end{table*}
811	
812	\paragraph{CoNLL NER free-form results.}
813	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds---higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
814	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
815	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$---comparable to constrained results (Table~\ref{tab:quality_estimation}).
816	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.25~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
817	
818	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
819	
820	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
821	
822	\paragraph{Pairwise overlap.}
823	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
824	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
825	
826	\paragraph{Instance complexity drives failure.}
827	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
828	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
829	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
830	
831	\begin{table}[t]
832	\centering
833	\small
834	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
835	\label{tab:stable_failures}
836	\begin{tabular}{lcccc}
837	\toprule
838	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
839	\midrule
840	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
841	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
842	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
843	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
844	\bottomrule
845	\end{tabular}
846	\end{table}
847	
848	\paragraph{Flip instances.}
849	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
850	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
851	
852	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
853	
854	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
855	
856	\begin{table}[t]
857	\centering
858	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
859	\label{tab:n-scaling}
860	\small
861	\begin{tabular}{l ccc ccc}
862	\toprule
863	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
864	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
865	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
866	\midrule
867	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
868	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
869	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
870	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
871	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
872	\midrule
873	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
874	\bottomrule
875	\end{tabular}
876	\end{table}
877	
878	\begin{table}[t]
879	\centering
880	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
881	\label{tab:ranking-stability}
882	\small
883	\begin{tabular}{ll cc l}
884	\toprule
885	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
886	\midrule
887	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
888	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
889	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
890	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
891	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
892	\bottomrule
893	\end{tabular}
894	\end{table}
895	
896	\begin{table}[t]
897	\centering
898	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
899	\label{tab:sigma-comparison}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dab489d-fffa-4514-909e-c1f53bedd94d",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "d4386bdf-381b-4d1d-88cb-fc36bdf669f2",
  "sourceToolAssistantUUID": "5dab489d-fffa-4514-909e-c1f53bedd94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T12:13:45.210Z_

<details open><summary>🔧 Tool call — Read · `toolu_0186fCcBzYNh6o1fKV7ubaSG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 899,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4386bdf-381b-4d1d-88cb-fc36bdf669f2",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ECjqYQkHnxJKr9Ysqu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cda1aaa-b687-4a9b-b7e2-768129b7a317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DNGwB3BR3aGuTkMmbwbseK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12561,
      "cache_read_input_tokens": 62646,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 62646,
          "cache_creation_input_tokens": 12561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12561,
            "ephemeral_1h_input_tokens": 0
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

_source line 47 · 2026-05-16T12:13:45.217Z_

<details><summary>↩ Tool result · `toolu_0186fCcBzYNh6o1fKV7ubaSG`</summary>

```text
899	\label{tab:sigma-comparison}
900	\small
901	\begin{tabular}{l cc cc}
902	\toprule
903	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
904	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
905	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
906	\midrule
907	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
908	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
909	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
910	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
911	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
912	\midrule
913	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
914	\bottomrule
915	\end{tabular}
916	\end{table}
917	
918	Signal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.
919	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
920	
921	\section{Cross-Dataset OOD Analysis}\label{app:ood}
922	
923	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
924	
925	\begin{table}[t]
926	\centering
927	\small
928	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
929	\label{tab:ood}
930	\begin{tabular}{l ccc ccc}
931	\toprule
932	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
933	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
934	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
935	\midrule
936	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
937	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
938	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
939	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
940	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
941	\bottomrule
942	\end{tabular}
943	\end{table}
944	
945	\paragraph{Wider-to-narrower schema transfer.}
946	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
947	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
948	
949	\paragraph{Narrower-to-wider schema transfer (excluded).}
950	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
951	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).
952	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
953	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
954	
955	\paragraph{Asymmetry interpretation.}
956	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
957	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
958	
959	\section{Verbalized Confidence}\label{app:verbalized_confidence}
960	
961	We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
962	Table~\ref{tab:verbconf} reports quality estimation and selection results.
963	
964	\begin{table}[t]
965	\centering
966	\small
967	\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
968	\label{tab:verbconf}
969	\begin{tabular}{l cc cc}
970	\toprule
971	 & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{CoNLL NER}} \\
972	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
973	Metric & VerbConf & LP & VerbConf & LP \\
974	\midrule
975	$\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\
976	AUROC & 0.681 & 0.578 & 0.747 & 0.753 \\
977	Selection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\
978	$\Delta$ vs.\ greedy & $-$2.45\,pp & $+$0.2\,pp & $-$1.93\,pp & $-$0.77\,pp \\
979	\midrule
980	Mean score & 8.58\,/\,10 & --- & 9.24\,/\,10 & --- \\
981	Parse fail rate & 0.26\% & --- & 0\% & --- \\
982	\bottomrule
983	\end{tabular}
984	\end{table}
985	
986	\paragraph{Severe overconfidence.}
987	VerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.
988	This compression is more severe than LP (which spans a 0.041-nat median range), confirming that score compression is a general property of model self-assessment, not an artifact of log-probability computation.
989	
990	\paragraph{QE--selection decoupling.}
991	VerbConf achieves higher $\rho$ than LP on both datasets (SciERC: 0.297 vs.\ 0.205; CoNLL: 0.337 vs.\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\ 0.578; CoNLL: 0.747 vs.\ 0.753), yet yields the worst selection among all signals ($\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).
992	This dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.
993	The AUROC--$\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\rho$ at 0.337) reflects differing sensitivity to binary vs.\ ordinal discrimination.
994	
995	\section{LLaMA-3.2-3B Scale Ablation}\label{app:llama3b}
996	
997	To extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\ref{tab:llama3b}).
998	
999	\begin{table}[t]
1000	\centering
1001	\small
1002	\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
1003	\label{tab:llama3b}
1004	\begin{tabular}{l cc cc}
1005	\toprule
1006	Signal & $\rho$ & AUROC & Sel.\ F1 & $\Delta$ vs.\ greedy \\
1007	\midrule
1008	VC & \textbf{.460} & .743 & 0.611 & $-$1.54\,pp \\
1009	SJ & .375 & .738 & \textbf{0.633} & $+$0.61\,pp \\
1010	EM & .334 & \textbf{.776} & --- & --- \\
1011	FK & .268 & .671 & 0.630 & $+$0.28\,pp \\
1012	LP & .266 & .633 & 0.628 & $+$0.12\,pp \\
1013	\midrule
1014	Greedy & --- & --- & 0.627 & --- \\
1015	Oracle & --- & --- & 0.763 & --- \\
1016	\bottomrule
1017	\end{tabular}
1018	\end{table}
1019	
1020	The $\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\ref{tab:quality_estimation}), confirming ranking stability across two model families spanning 3B--8B.
1021	AUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), reflecting the $\rho$--AUROC dissociation noted in the main text.
1022	Despite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC---the strongest QE signal---yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.
1023	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cda1aaa-b687-4a9b-b7e2-768129b7a317",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "5180196e-5e30-4a9a-a60e-d563242c0f35",
  "sourceToolAssistantUUID": "1cda1aaa-b687-4a9b-b7e2-768129b7a317",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T12:13:48.907Z_

Now let me check for numerical consistency across the abstract, introduction, and tables. Let me also look at the paper framing and any related project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5180196e-5e30-4a9a-a60e-d563242c0f35",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ED4bQeoAuXHnpTcfMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c56fb17a-5b4c-4cab-8f83-ae80af66fc55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqi4q5fJ5Mi2dvzWPWPeum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 75207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T12:13:49.861Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WVt1j2sXy2bbKnhoXWhom9`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c56fb17a-5b4c-4cab-8f83-ae80af66fc55",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ED4bQeoAuXHnpTcfMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c74c456e-736e-4e14-b1e0-da29a97ddc8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqi4q5fJ5Mi2dvzWPWPeum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 75207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T12:13:49.870Z_

<details><summary>↩ Tool result · `toolu_01WVt1j2sXy2bbKnhoXWhom9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c74c456e-736e-4e14-b1e0-da29a97ddc8c",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "acda5f2f-0296-4a56-8bf4-af0215b9cc56",
  "sourceToolAssistantUUID": "c74c456e-736e-4e14-b1e0-da29a97ddc8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T12:13:50.551Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01C45rHxLTkQTseQGffJgCap`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acda5f2f-0296-4a56-8bf4-af0215b9cc56",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6ED4bQeoAuXHnpTcfMf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7a9aadf-2798-4a0a-95ac-a7b460c71962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqi4q5fJ5Mi2dvzWPWPeum",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3939,
      "cache_read_input_tokens": 75207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3939,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T12:13:50.563Z_

<details><summary>↩ Tool result · `toolu_01C45rHxLTkQTseQGffJgCap`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a9aadf-2798-4a0a-95ac-a7b460c71962",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "a4ea308d-7fa8-4317-9483-881997d14ef2",
  "sourceToolAssistantUUID": "a7a9aadf-2798-4a0a-95ac-a7b460c71962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-16T12:13:53.928Z_

Now let me also check the latest dream review report, which may provide additional context on the paper's state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4ea308d-7fa8-4317-9483-881997d14ef2",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EDTfUbF4FDJhAEUcju",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c848180-aeba-44cc-8df3-363c893174d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SpDhYDykRwBqZVJZaVHjv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 79146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 518,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T12:13:55.906Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SYQ2nHtQ6jbdM2ALNfnvxF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/best/paper.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c848180-aeba-44cc-8df3-363c893174d2",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EDTfUbF4FDJhAEUcju",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4f7cba7-44b3-4900-908d-f76361904b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SpDhYDykRwBqZVJZaVHjv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 79146,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 518
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 79146,
          "cache_creation_input_tokens": 518,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 518,
            "ephemeral_1h_input_tokens": 0
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

_source line 55 · 2026-05-16T12:13:55.913Z_

<details><summary>↩ Tool result · `toolu_01SYQ2nHtQ6jbdM2ALNfnvxF`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{hyperref}
7	\usepackage{natbib}
8	\usepackage{amsmath}
9	\usepackage{amssymb}
10	\usepackage{booktabs}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{subcaption}
14	\usepackage{pgfplots}
15	\pgfplotsset{compat=1.18}
16	
17	\title{Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale Structured Information Extraction}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Test-time scaling via multi-sample generation improves LLM reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear. We present a dual contribution: (1)~a quality estimation (QE) framework showing that five confidence signals across four families reliably predict structured IE output quality (AUROC up to 0.82, Spearman $\rho$ up to 0.44), enabling practical selective prediction; and (2)~a diagnostic analysis revealing why these same signals universally fail at best-of-N selection. We identify a multi-causal failure mechanism: instance degeneracy (21--58\% of instances produce identical outputs across N samples), logprob score compression (within-instance range 0.041 nats), and insufficient signal discriminability even when degeneracy is reduced. A trained verifier (logistic regression on 5 signals) closes 36\% of the oracle gap for NER (+4.8pp over greedy), confirming that signals carry exploitable information but unsupervised aggregation is the bottleneck. Experiments span 3 model configurations (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B), 2 IE tasks (NER, RE), and 3 datasets (SciERC, CoNLL-2003, WNUT-17), establishing that the correlation--selection gap is model-agnostic and task-general.
26	\end{abstract}
27	
28	%=============================================================================
29	\section{Introduction}
30	%=============================================================================
31	
32	Test-time scaling through multi-sample generation and selection has emerged as a powerful paradigm for improving LLM performance on reasoning tasks~\cite{wang2023selfconsistency,brown2024large,snell2024scaling}. Self-consistency---sampling multiple chain-of-thought paths and selecting via majority vote---yields substantial gains for discrete-answer problems. However, structured information extraction (IE) outputs---entity sets, relation triples, event structures---resist naive majority voting due to their combinatorial output space.
33	
34	A natural question arises: can confidence signals derived from multi-sample agreement serve as quality estimators or selectors for structured IE? We decouple these two functions and show they are governed by fundamentally different factors.
35	
36	\paragraph{Contribution A: QE Framework.} We systematically evaluate five confidence signals across four families---structural similarity (set Jaccard, fuzzy match), probabilistic (logprob), voting-based (entity voting confidence), and exact match---for structured IE quality estimation. Signals achieve AUROC up to 0.82 and $\rho$ up to 0.44, demonstrating practical value for selective prediction and error flagging. Signal effectiveness is task-dependent: structural signals dominate for NER while logprob is strongest for RE.
37	
38	\paragraph{Contribution B: Diagnostic Analysis.} We diagnose why reliable quality estimators fail as selectors. The failure is multi-causal: (1)~four of five signals are instance-level aggregates that cannot rank candidates by construction; (2)~instance degeneracy eliminates selection headroom for 21--58\% of instances; (3)~logprob compression (within-instance range 0.041 nats) neutralizes the only per-sample signal; (4)~reducing degeneracy via lower LoRA rank is necessary but not sufficient---signals still cannot exploit increased headroom. A trained verifier closes 36\% of the NER oracle gap, proving the gap is closable with supervision.
39	
40	This dual contribution---positive QE utility paired with mechanistic selection failure diagnosis---provides both practical tools and theoretical understanding for practitioners considering test-time scaling for structured IE.
41	
42	%=============================================================================
43	\section{Related Work}
44	%=============================================================================
45	
46	\paragraph{Self-Consistency and Test-Time Scaling.}
47	Wang et al.~\cite{wang2023selfconsistency} show that sampling diverse reasoning paths and selecting via majority vote improves accuracy on arithmetic and commonsense tasks. Subsequent work extends this to confidence-weighted voting~\cite{cisc2025}, reward-free selection via KL-divergence~\cite{selfcertainty2026}, reliability-aware adaptive consistency~\cite{reasc2026}, and atomic sub-claim consistency for long-form text~\cite{atomicsc2024}. All operate on discrete answers or decomposable claims; none address structured outputs with set-valued semantics.
48	
49	\paragraph{Consistency for Structured IE.}
50	N\'{e}dellec and Xia~\cite{nedellec2026} study consistency--accuracy correlation for hard-prompted LLMs on biomedical NER/RE, finding positive correlation but using surface-level string matching that ``overlooks semantically consistent outputs.'' Our structural Jaccard metric directly addresses this limitation. They do not study best-of-N selection or multi-signal comparison.
51	
52	\paragraph{Uncertainty Quantification for LLMs.}
53	Semantic entropy~\cite{kuhn2023semantic}, SelfCheckGPT~\cite{manakul2023selfcheckgpt}, and conformal prediction~\cite{fisch2021,angelopoulos2021} provide uncertainty estimates for generation. Surveys~\cite{uqsurvey2025,calibsurvey2025} systematize the landscape. Token-level NER uncertainty has been studied via MC-dropout~\cite{shelmanov2021} and ensemble methods~\cite{lakshminarayanan2017}. We complement this line by evaluating sample-level structural consistency signals specifically for structured IE quality estimation.
54	
55	\paragraph{MBR Decoding and Verifiers.}
56	Minimum Bayes Risk decoding~\cite{eikema2022} selects candidates minimizing expected loss under a utility function. CoCoA~\cite{cocoa2025} combines confidence and consistency for MBR-style selection in QA and summarization. Trained verifiers~\cite{cobbe2021,lightman2023} learn to score candidate solutions. Our work differs: we show that for structured IE, utility \emph{is} aligned (within-instance $\rho$=0.524) but headroom is eliminated by degeneracy---a qualitatively distinct failure from utility misalignment.
57	
58	\paragraph{Selective Prediction.}
59	Geifman and El-Yaniv~\cite{geifman2017} formalize selective prediction with guaranteed risk. Kuleshov and Liang~\cite{kuleshov2015} address calibration for structured outputs. Our QE framework provides the confidence scores needed for selective prediction in structured IE, and our diagnostic analysis explains why selection (choosing \emph{which} output to return) fails even when estimation (knowing \emph{how good} an output is) succeeds.
60	
61	%=============================================================================
62	\section{Method}
63	%=============================================================================
64	
65	\subsection{Problem Setup}
66	
67	Given a structured IE model $M$ and input $x$, we generate $N$ samples $\{y_1, \ldots, y_N\}$ at temperature $T{=}1.0$. Each sample $y_i$ is a structured output (entity set or relation set). We evaluate two tasks:
68	\begin{enumerate}
69	    \item \textbf{Quality Estimation (QE)}: Predict the F1 score of each sample or the greedy output without access to ground truth.
70	    \item \textbf{Selection}: Choose the sample $y^* = \arg\max_i s(y_i)$ that maximizes F1, using signal $s$.
71	\end{enumerate}
72	
73	\subsection{Confidence Signals}
74	
75	We evaluate five signals across four families:
76	
77	\paragraph{Set Jaccard (SJ).} For sample $y_i$ with entity set $E_i$, compute pairwise Jaccard similarity against all other samples and average:
78	\begin{equation}
79	\text{SJ}(y_i) = \frac{1}{N{-}1} \sum_{j \neq i} \frac{|E_i \cap E_j|}{|E_i \cup E_j|}
80	\end{equation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4f7cba7-44b3-4900-908d-f76361904b88",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "7e42ae01-3c28-434c-ab60-755dc0f8ddaa",
  "sourceToolAssistantUUID": "b4f7cba7-44b3-4900-908d-f76361904b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-16T12:13:59.821Z_

This is the dream report (synthetic), not the actual paper. I have enough content from the real paper to conduct the review. Let me now perform the numerical consistency check systematically by cross-referencing numbers across sections.

Let me compile the final review based on my thorough reading of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e42ae01-3c28-434c-ab60-755dc0f8ddaa",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EDrTgGkrmRVXJZtKnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "939c18c2-bdc3-4423-a293-9a8572c99406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3FKAuBx9fzF81EXHLGrYM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2405,
      "cache_read_input_tokens": 79664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2405,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T12:14:00.311Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LqoVoPhRKCqTfMZW1onLTM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "939c18c2-bdc3-4423-a293-9a8572c99406",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EDrTgGkrmRVXJZtKnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dad2efa-bdff-40ee-8281-38ea1a6f1c99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3FKAuBx9fzF81EXHLGrYM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2405,
      "cache_read_input_tokens": 79664,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2405
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 79664,
          "cache_creation_input_tokens": 2405,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2405,
            "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-16T12:14:00.313Z_

<details><summary>↩ Tool result · `toolu_01LqoVoPhRKCqTfMZW1onLTM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dad2efa-bdff-40ee-8281-38ea1a6f1c99",
  "isSidechain": true,
  "promptId": "0ce02c20-e485-465c-89da-eea2d8d85351",
  "agentId": "a3cded80d45c60cc1",
  "type": "user",
  "uuid": "ec7f4f3b-0115-4f53-98af-bcb2ecd30023",
  "sourceToolAssistantUUID": "8dad2efa-bdff-40ee-8281-38ea1a6f1c99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-16T12:15:48.733Z_



Now I have thoroughly read the entire paper (abstract, introduction, related work, method, experiments, discussion, conclusion, limitations, and the full appendix). Let me compile the review.

---

## EMNLP 2026 Review — Reviewer 1 (R1: Methods and Experiments)

**Paper**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"

---

### 1. Summary

This paper systematically evaluates five confidence signals for quality estimation (QE) and best-of-N sample selection in LLM-based NER across three datasets and three models. The central finding is the "correlation-selection gap": signals that reliably predict instance-level output quality (rho up to 0.45, AUROC up to 0.82) fail to select better candidates than greedy decoding, despite 13-18pp of oracle headroom. The paper diagnoses two mechanisms---instance degeneracy (21-58% of instances produce identical outputs) and log-probability compression (median within-instance range of 0.041 nats)---and validates these through LoRA-rank, free-form decoding, entity-token LP, scale, and verbalized-confidence ablations.

---

### 2. Strengths

- **Well-defined conceptual contribution.** The decoupling of quality estimation from sample selection is a genuinely useful distinction. The "correlation-selection gap" is clearly defined, well-motivated, and has practical implications for practitioners considering test-time scaling for structured IE.

- **Thorough ablation chain.** The paper presents a commendably comprehensive series of ablations: free-form decoding (ruling out constrained decoding as cause), entity-token LP (ruling out format-token dilution), LoRA-rank ablation (showing degeneracy reduction is necessary but not sufficient), verbalized confidence (showing compression is not LP-specific), scale ablation (4B vs 8B), signal combinations (LP x VC), and the epsilon sensitivity sweep. This is unusually thorough for a negative-result paper.

- **Statistical rigor on the primary claims.** The paper uses paired sign tests, bootstrap CIs, TOST equivalence testing with both oracle-anchored and externally-grounded margins, Cohen's d, Bonferroni correction, and Fisher's z-test. The non-tied LP subset finding (+2.9pp, p=0.004) survives Bonferroni correction and is properly flagged as exploratory. The acknowledgment that TOST conclusions are configuration-dependent (Appendix D) is commendable honesty.

- **Difficulty gradient design.** Using SciERC (medium), CoNLL (ceiling control), and WNUT-17 (signal-collapse boundary) with explicit roles for each dataset is sound experimental design. The paper properly interprets CoNLL as a ceiling-effect control rather than overclaiming from its results.

- **Extensive appendix.** The 20+ page appendix provides FK independence tests, SJ normalizer robustness, LOO-SJ circularity analysis, OOD transfer, LP failure stability, N-scaling, multi-seed tables, and epsilon robustness---far exceeding typical supplementary material.

- **Honest limitations.** The paper is transparent about its scope: single RE benchmark, 4B-8B scale only, no trained verifier, thinking-token confound, and post-hoc epsilon threshold.

---

### 3. Weaknesses

**Major:**

- **W1. AUROC claim inconsistency (Abstract/Introduction vs. Tables).** The abstract (line 4) and introduction (line 11) both claim "AUROC up to 0.82," and Figure 1's caption repeats this. However, Table 1 (tab:quality_estimation) shows the highest AUROC is EM on CoNLL-Qwen at 0.816. While 0.816 rounds to 0.82, this rounding is aggressive for a headline claim. More importantly, the paper_provenance.yaml documents that the original abstract claimed "AUROC up to 0.82" which was supposed to have been corrected to 0.75. The current paper retains 0.82 in abstract/intro while the SciERC primary test bed only reaches 0.749. This creates confusion about which dataset the headline number refers to---the paper should be explicit that 0.82 is from the ceiling-effect control (CoNLL), not the primary test bed.

- **W2. Narrow cross-model validation.** The paper claims findings are "model-agnostic" (abstract line 7: "five-layer ablation chain"), yet both models are 8B decoder-only architectures fine-tuned with identical LoRA recipes (rank=32, alpha=64, 5 epochs, same optimizer, same framework). The LLaMA-3.2-3B ablation (Appendix L) helps but is still a decoder-only model with the same LoRA setup. No encoder-based model (e.g., DeBERTa, BERT-CRF), no 70B+ model, and no closed-source API is tested. The degeneracy phenomenon could plausibly be specific to LoRA fine-tuning of decoder-only models in this parameter range. The paper acknowledges the 70B+ limitation in the conclusion but not the encoder-model gap.

- **W3. Supervised verifier baseline is too weak.** The supervised verifier (logistic regression on 5 signals, 3-fold CV) closes only 0.8% of the oracle gap---but this is not a meaningful test of whether "learned per-sample scoring" can close the gap, because: (a) 4 of 5 input features are instance-level and thus identical across candidates within an instance; (b) LP is the only per-sample feature, making this effectively a univariate LP selector with regularization; (c) LR on highly correlated features (mean inter-signal rho 0.45-0.72 per provenance) is essentially a weighted average. The paper's conclusion that "the bottleneck is in the features, not the aggregation" is valid only for these specific features---it does not support the broader claim that "closing the gap likely requires learned per-sample scoring" because no such scorer was actually tested (e.g., a small MLP on the model's hidden states, or a cross-encoder reranker).

- **W4. Selection table numbers shifted between versions.** Table 2 (tab:selection) reports LP selection F1 = 0.647 with p=0.29, but the abstract and introduction both state "Delta = +0.2pp" while Table 2 shows 0.647 - 0.645 = +0.2pp (consistent). However, the paper_provenance (c011) records "logprob +0.6pp, p=0.39, 3-seed bootstrap" and "CI [-3.0, +4.2]pp, d=0.038." The main text Table 2 reports p=0.29 (2-seed sign test) while the provenance records p=0.39 (3-seed bootstrap). These are different tests on different seed counts, and both appear in the paper without clear reconciliation. The discussion (line 16) states "+0.2pp, p=0.29" while referencing Table 2. Which p-value is definitive? The paper should use consistent statistical tests throughout.

**Minor:**

- **W5. SciERC NER n=529 vs. 551 handling.** The paper correctly notes filtering of 22 empty-gold instances (551 -> 529), but Table 8 (tab:cross_selection) and the RE appendix use n=529 for NER and n=397 for RE (from 551 total). The WNUT table uses n=689 "after filtering gold-empty instances" from 1,287 total---meaning 598 instances (46.5%) have empty gold, which is substantial. The paper does not discuss whether this aggressive filtering biases the WNUT results.

- **W6. Temperature sensitivity under-explored.** Only T=0.7 and T=1.0 are tested. The paper notes LP compression worsens at lower temperatures (CoNLL tied fractions 95.8% at T=0.7) but does not test higher temperatures (T=1.5, T=2.0) which could reduce degeneracy and compression. This is a missed ablation that directly tests the paper's core mechanisms.

- **W7. Selection evaluation uses 2-seed mean.** Table 2 caption states "2-seed mean +/- sigma" for the primary selection result. With only 2 seeds, sigma is unreliable, and the sign test power is limited. The 3-seed multi-seed analysis (Table 7, Appendix E) is used for QE but not systematically for selection across all configurations.

- **W8. Free-form ablation limited scope.** The free-form ablation covers SciERC NER and CoNLL NER with one model (Qwen3-8B). The RE free-form finding (LP selection reverses direction, +1.8pp) is interesting but based on a single benchmark. The ablation does not test LLaMA or the 4B model.

- **W9. Instance degeneracy definition.** "Constant F1" (all N samples receive identical F1) is used as the degeneracy definition, but this conflates two cases: (a) all N outputs are literally identical strings, and (b) outputs differ but happen to achieve the same F1. Table 11 (tab:diversity) distinguishes these ("Identical" = all N identical), showing 11% on Qwen/SciERC vs. 21% "constant F1" in Table 4 (tab:degeneracy). The paper should be clearer that half of the "degenerate" instances actually produce diverse outputs that coincidentally score equally---a distinct phenomenon from output convergence.

---

### 4. Questions for Authors

Q1. The abstract claims "AUROC up to 0.82"---is this from CoNLL (EM, 0.816) or has a rounding/version inconsistency persisted? The paper_provenance documents this was supposed to be corrected to 0.75. Please clarify which value is correct and which dataset it refers to.

Q2. Table 2 reports p=0.29 (2-seed sign test) for LP selection, while provenance records p=0.39 (3-seed bootstrap). Are these different analyses? Which is the definitive test?

Q3. For the LoRA rank=8 ablation, you report greedy F1=0.640 and LP selection=0.635. But in the rank=32 experiments, greedy is 0.645 (Table 2). Does the lower greedy baseline at rank=8 mean the model is weaker, and if so, does this confound the comparison of degeneracy rates?

Q4. What is the actual number of instances where all N=8 outputs are identical strings on SciERC? Table 11 shows 11% "Identical" but Table 4 shows 21% "Constant F1." Are you claiming that the remaining 10% produce different outputs that coincidentally achieve the same F1?

Q5. Have you considered testing with higher temperatures (T=1.5 or T=2.0) to reduce both degeneracy and LP compression? This seems like the most direct test of your mechanisms.

Q6. The trained verifier uses 3-fold CV in the main text but the provenance records 5-fold CV. Which was actually used?

---

### 5. Missing Experiments / Suggestions

1. **Encoder-based baseline.** Even a simple BERT-CRF or DeBERTa NER model with temperature sampling would test whether the degeneracy phenomenon is specific to decoder-only autoregressive models or general to fine-tuned NER.

2. **Higher temperature ablation.** T=1.5 or T=2.0 would directly test the degeneracy mechanism. If degeneracy drops substantially, does selection improve?

3. **70B+ or API model.** Testing with a larger model (even via API) on one dataset would address the scale limitation. Larger models may exhibit different degeneracy profiles.

4. **Stronger verifier.** The LR verifier on 5 correlated features is not a fair test of "learned per-sample scoring." A verifier using the model's hidden states (even a 2-layer MLP on the last hidden state) would meaningfully test whether the oracle gap is closable.

5. **More RE benchmarks.** TACRED or ACE05 would strengthen the RE extension from "exploratory" to a proper secondary finding. The provenance shows exp_tacred_re_benchmark was planned but killed.

6. **Nucleus sampling comparison.** The paper uses temperature sampling throughout. Top-p sampling might produce different diversity profiles and could interact differently with the signals.

---

### 6. Numerical Consistency Check

| Claim location | Value | Source | Status |
|---|---|---|---|
| Abstract: "AUROC up to 0.82" | 0.82 | Table 1: EM CoNLL-Qwen AUROC = 0.816 | BORDERLINE: rounds to 0.82 but misleading as headline since primary test bed (SciERC) is 0.663 |
| Abstract: "rho up to 0.45" | 0.45 | Table 1: EM CoNLL-Qwen rho = 0.451 | CONSISTENT |
| Abstract: "13-18pp oracle headroom" | 13-18 | Table 2: NER oracle 0.778, greedy 0.645 = 13.3pp; RE oracle 0.585, greedy 0.404 = 18.1pp | CONSISTENT |
| Abstract: "21-58% instances" | 21-58 | Table 4: SciERC 8B 21%, CoNLL 8B 58% | CONSISTENT |
| Abstract: "median rho=0.52" | 0.52 | Table 4: SciERC 8B within-inst SJ rho = 0.524 | CONSISTENT |
| Abstract: "0.041 nats" | 0.041 | Appendix H, Table 9 discussion | CONSISTENT |
| Abstract: "degeneracy 7% vs 21%" | 7/21 | Section 4.4: rank=8 yields 7.2%, rank=32 yields 21% | MINOR: abstract says "7%" while text says "7.2%" |
| Intro: "rho=0.38" (contribution 1) | 0.38 | Table 1: VC SciERC rho = 0.379 | CONSISTENT (rounded) |
| Intro: "AUROC=0.82" (contribution 1) | 0.82 | Table 1: EM CoNLL = 0.816 | Same as abstract issue |
| Table 2: LP p=0.29 | 0.29 | Main text Section 4.3: "p=0.29" | CONSISTENT within paper, but provenance records p=0.39 |
| Table 2: Oracle NER 0.778 | 0.778 | Provenance c013: 0.776 | MINOR DISCREPANCY: 0.778 vs 0.776 (may be 2-seed vs 3-seed) |
| Discussion: "+0.2pp, p=0.29" | consistent with Table 2 | CONSISTENT |
| Conclusion: "rho up to 0.45, AUROC up to 0.82" | Same headline numbers | CONSISTENT with abstract |
| Conclusion: "<1% oracle gap" (supervised) | <1% | Section 4.4: 0.8% | CONSISTENT |
| Section 4.4: LR verifier F1=0.648, AUROC=0.697 | - | Provenance records AUROC=0.760, selection F1=0.648, gap closed 3.2% | DISCREPANCY: Main text says "0.8% gap closed" and AUROC=0.697; provenance says 3.2% gap closed and AUROC=0.760. The main text appears to be a different version of the experiment (3-fold vs 5-fold CV). |
| Table 2: Greedy 0.645 +/- 0.001 | - | Provenance c011: greedy 0.644 | MINOR: 0.645 vs 0.644 |

**Summary of numerical issues**: The most concerning are (a) the AUROC=0.82 headline claim sourced from the ceiling-effect control rather than the primary test bed, (b) the supervised verifier numbers differ between the main text (0.8% gap closed, AUROC 0.697) and provenance (3.2% gap closed, AUROC 0.760), and (c) the LP selection p-value appearing as both 0.29 and 0.39 in different places. None of these are fabrication concerns---they appear to reflect version drift across experiment iterations---but they need reconciliation.

---

### 7. Scores

- **Soundness**: 3.5 (between Acceptable and Strong). The core claims are well-supported by the data; statistical methodology is above average. The numerical inconsistencies and the weak supervised verifier baseline are concerns but do not undermine the central finding. The cross-model validation is narrow but present.

- **Excitement**: 3 (Interesting). The correlation-selection gap is a genuine insight with practical value, and the ablation chain is thorough. However, this is ultimately a negative-result paper with limited actionable takeaways beyond "use greedy decoding for NER." The finding that fine-tuned models exhibit instance degeneracy is somewhat expected.

- **Overall Assessment**: 3.0 (Findings). The paper makes a solid empirical contribution documenting a real phenomenon with careful analysis. The ablation chain is a model of thoroughness for negative-result papers. However, the narrow model diversity (all decoder-only, all LoRA, all 3B-8B), the absence of a meaningful verifier baseline, the numerical version-drift issues, and the limited actionable implications place this below the conference threshold. It would be a strong Findings paper. With a stronger verifier experiment, a higher-temperature ablation, and resolution of the numerical inconsistencies, it could reach conference level.

- **Confidence**: 4 (High). I have carefully read the full paper and appendix, cross-checked numerical claims against provenance records, and have relevant expertise in NER evaluation methodology, test-time scaling, and MBR decoding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec7f4f3b-0115-4f53-98af-bcb2ecd30023",
  "isSidechain": true,
  "agentId": "a3cded80d45c60cc1",
  "requestId": "req_011Cb6EEBKzdDbN2UY3NnHpY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "134d2c59-1a25-4ab7-9d68-03ff1c204fe9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "b72398d7-e431-4137-b17e-51fc8746e976",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G1VfupWrZ42oi6MBpuMchY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 730,
      "cache_read_input_tokens": 82069,
      "output_tokens": 4415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4415,
          "cache_read_input_tokens": 82069,
          "cache_creation_input_tokens": 730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 730,
            "ephemeral_1h_input_tokens": 0
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
