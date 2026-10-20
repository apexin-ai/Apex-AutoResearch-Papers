# Research conversation: You are Reviewer 1 (R1) for a DREAM review session. Your focus: **Methods and Experiments**. ## Venue: EMNLP 2026 Main (

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a40996edda29488d5.jsonl`
- **Structured JSON:** [`e035a5c538e8460eef98.json`](../../sessions/e0/e035a5c538e8460eef98.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

38 recorded events

### User

_source line 1 · 2026-05-15T14:18:46.381Z_

You are Reviewer 1 (R1) for a DREAM review session. Your focus: **Methods and Experiments**.

## Venue: EMNLP 2026 Main (via ACL Rolling Review)

### ARR Review Form Scoring (used by EMNLP 2026):
- **Soundness**: 1-5 (5=Excellent: one of the most thorough; 4=Strong: sufficient support for all claims; 3=Acceptable: sufficient support for main claims; 2=Poor: some claims unsupported; 1=Major issues)
- **Excitement**: 1-5 (5=Highly Exciting; 4=Exciting; 3=Ambivalent; 2=Below threshold; 1=Not exciting)
- **Overall Assessment**: 1-5 with 0.5 increments (5=Award; 4=Accept; 3.5=Leaning Accept; 3=Ambivalent; 2.5=Leaning Reject; 2=Resubmit next cycle; 1.5=Resubmit after next cycle; 1=Do not resubmit)
- **Confidence**: 1-5 (5=Absolutely certain; 4=Quite sure; 3=Fairly confident; 2=Willing to defend but not absolutely certain; 1=Not confident)

### EMNLP acceptance rate: ~22-25%

## Paper Summary

**Title**: FREIGE: Faithful Evidence Generation for Document-Level Relation Extraction via Rejection Sampling Fine-Tuning

**Core idea**: First LLM-based DocRE system that jointly generates relation triples AND sentence-level evidence. Uses Rejection Sampling Fine-Tuning (RSFT): SFT model generates N=8 candidates per doc, a Contrastive Evidence Discrimination (CED) scorer filters top-1, and filtered data used for further SFT. Also discovers "evidence-extraction decoupling" in GRPO and proposes EDCR metric.

**Main contributions**:
1. RSFT pipeline for joint relation+evidence generation: +3.2pp test rel_F1 over SFT (p<0.01), joint Evi-F1 32.2%
2. Evidence-extraction decoupling characterization in GRPO+QLoRA (worsens with G=8 vs G=4)
3. EDCR diagnostic metric (r=0.44 with human, perfect method-level rank concordance)

**Key results (from paper)**:
- Table 1 (test): SFT rel_F1=40.0, RSFT+CED=43.2 (+3.2pp), RSFT+flatNLI=42.5
- Table 2 (dev CED vs flat-NLI ablation): CED consistently better but NOT statistically significant (evi_F1 p=0.12, rel_F1 p=0.28)
- Table 3: GRPO G=8 peaks at step 40 (rel_F1=7.8%) then collapses; G=4 best=21.7%
- Table 4: Full G=8 trajectory showing reward↑ while rel_F1 collapses
- Table 5: Spectrum — GRPO(7.8/21.7) < DPO(34.0) < SFT(40.6) < RSFT(46.1/46.8)
- Table 6: EDCR cross-method diagnostic zones
- Table 7: EDCR human validation (r=0.44, κ=0.62, method-level concordance=1.0)
- Table 8: top-k=1 (2718 samples) > top-k=3 (8154 samples) — quality > quantity
- Table 9: Model size ablation 1.7B/4B/8B all show RSFT gains (+2.8/+6.3/+4.0pp)
- Table 10: Re-DocRED generalization (+3.5pp)
- Table 11: DREEAM/SAIS reproduction within 1pp
- Table 12: NLI model ablation (base→large: +3.3pp disc acc but only +0.4pp downstream)

**Comparison with encoder baselines**: DREEAM 62.8% rel_F1, SAIS 60.4%, LMRC 60.7% — paper's best is 43.2% (test) or 48.8% (8B dev). Large gap.

## Imagined Experiment Coverage Assessment

The review_context.yaml lists 13 experiments (plans 001-013). The paper covers ALL of them:
- plan_001 (CED vs flat-NLI): Table 2 ✓
- plan_002 (test set): Table 1 ✓
- plan_003 (EDCR cross-method): Table 6 ✓
- plan_004 (DREEAM reproduction): Table 11 ✓
- plan_005 (CED-as-reranker): Section 5.6 ✓
- plan_006 (model size ablation): Table 9 ✓
- plan_007 (Re-DocRED): Table 10 ✓
- plan_008 (top-k ablation): Table 8 ✓
- plan_009 (GRPO forgetting analysis): Tables 3-4, Section 5.3 ✓
- plan_010 (NLI model ablation): Table 12 ✓
- plan_011 (GRPO G=8): Tables 3-4 ✓
- plan_012 (DPO+CED): Table 5 ✓
- plan_013 (EDCR human validation): Table 7 ✓

## Your Review Task (R1: Methods + Experiments)

Provide a thorough independent review focusing on:

1. **Methodological soundness**: Is the RSFT pipeline well-designed? Is CED well-motivated? Is the experimental methodology rigorous?
2. **Statistical rigor**: Are significance tests appropriate? How do you evaluate the CED vs flat-NLI non-significance?
3. **Experimental completeness**: Are the ablations sufficient? Missing controls?
4. **Baseline fairness**: Is the comparison to encoder methods (DREEAM, SAIS, LMRC) fair given the different paradigm?
5. **Claims vs evidence alignment**: Does each claim have adequate experimental support?
6. **Reproducibility concerns**
7. **Key weaknesses in method/experiments**

### Specific questions to address:
- The primary claimed contribution (CED scoring) is NOT statistically significantly better than flat-NLI. How severe is this weakness?
- Dev-to-test degradation for RSFT (3.6pp) vs SFT (0.6pp) — does this suggest overfitting through the CED pathway?
- The GRPO decoupling finding is limited to QLoRA — how generalizable is this claim?
- EDCR with r=0.44 human correlation — is this strong enough to validate the metric?
- 43.2% vs 62.8% (DREEAM) gap — how does this affect the paper's impact?

Output format:
```
## R1 Review: Methods and Experiments

### Summary of Contributions (1-2 sentences)

### Strengths
- S1: ...
- S2: ...
...

### Weaknesses
- W1: ...
- W2: ...
...

### Questions for Authors

### Missing Experiments or Analysis

### Claims-Evidence Assessment
| Claim | Evidence | Verdict |
|-------|----------|---------|

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall Assessment: X/5
- Confidence: X/5

### Justification for Overall Assessment (2-3 sentences)
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "347459e0-3fb4-490a-a60e-689effc4def3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:18:46.389Z_

```json
{
  "parentUuid": "347459e0-3fb4-490a-a60e-689effc4def3",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
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
  "uuid": "63ece68e-9c26-4e6d-8c2f-43e68a3b5fd5",
  "timestamp": "2026-05-15T14:18:46.389Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:18:49.277Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ece68e-9c26-4e6d-8c2f-43e68a3b5fd5",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4Vw619h6Bqx25xms7Yt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "640fdab9-a842-4045-a205-5bd4f13a2533",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCA3Yx7ccqvsS617KEUtns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15971,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15971,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 4 · 2026-05-15T14:18:50.665Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FEi6yDTr32KCVMbyB6diqB`</summary>

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
  "parentUuid": "640fdab9-a842-4045-a205-5bd4f13a2533",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4Vw619h6Bqx25xms7Yt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57f03fca-012c-4cb7-8574-b5bff5b103ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCA3Yx7ccqvsS617KEUtns",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15971,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15971
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15971,
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

_source line 5 · 2026-05-15T14:18:50.672Z_

<details><summary>↩ Tool result · `toolu_01FEi6yDTr32KCVMbyB6diqB`</summary>

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
  "parentUuid": "57f03fca-012c-4cb7-8574-b5bff5b103ed",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "2ac5c6fb-21ab-46bf-ac46-4bbf89ac4727",
  "sourceToolAssistantUUID": "57f03fca-012c-4cb7-8574-b5bff5b103ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T14:18:53.602Z_



Let me read the paper and all relevant project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ac5c6fb-21ab-46bf-ac46-4bbf89ac4727",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwQUQHcbEsg2raPGZg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a09d8df3-c499-4991-a3dc-8d4886f0d1ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwrWsHYhbWsFmun5mjCyWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 7 · 2026-05-15T14:18:54.079Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_019uTctNZTiY3ZWQPNT4CgZW`</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09d8df3-c499-4991-a3dc-8d4886f0d1ed",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwQUQHcbEsg2raPGZg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "039c5a35-c57a-41bd-bcb3-b4f015548504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwrWsHYhbWsFmun5mjCyWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-15T14:18:54.430Z_

<details><summary>↩ Tool result · `toolu_019uTctNZTiY3ZWQPNT4CgZW`</summary>

```text
{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (76 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\n\n## 待处理\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\n\n## 近期结论\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\n\n## 趋势\n成功 26 / 负向 11 / 失败 12 / 共 71\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — u\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "039c5a35-c57a-41bd-bcb3-b4f015548504",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "06593fe6-6245-400d-b78e-a93b6287cd25",
  "sourceToolAssistantUUID": "039c5a35-c57a-41bd-bcb3-b4f015548504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:18:55.493Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01JB8gjed19JHxv623LuXC1k`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06593fe6-6245-400d-b78e-a93b6287cd25",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwQUQHcbEsg2raPGZg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ee0e232-4f4d-4c8c-b37b-fa2f4f4831ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwrWsHYhbWsFmun5mjCyWV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-15T14:18:55.516Z_

<details><summary>↩ Tool result · `toolu_01JB8gjed19JHxv623LuXC1k`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
artifacts/dream_reports/dream_20260515T132059/best/paper.tex
artifacts/dream_reports/dream_20260515T132059/median/paper.tex
artifacts/dream_reports/dream_20260515T132059/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ee0e232-4f4d-4c8c-b37b-fa2f4f4831ab",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "a09ec05a-97e9-48a6-bf34-123900f9e843",
  "sourceToolAssistantUUID": "3ee0e232-4f4d-4c8c-b37b-fa2f4f4831ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:18:55.896Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0171jyog4uiesWx66YBanXnY`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a09ec05a-97e9-48a6-bf34-123900f9e843",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwQUQHcbEsg2raPGZg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e09a6da0-f34b-46e9-ae21-bab28952b980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NwrWsHYhbWsFmun5mjCyWV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15971,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 243,
          "cache_read_input_tokens": 15971,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-15T14:18:55.915Z_

<details><summary>↩ Tool result · `toolu_0171jyog4uiesWx66YBanXnY`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.pdf
artifacts/dream_reports/dream_20260515T120227/median/paper.pdf
artifacts/dream_reports/dream_20260515T120227/worst/paper.pdf
artifacts/dream_reports/dream_20260515T132059/best/paper.pdf
artifacts/dream_reports/dream_20260515T132059/median/paper.pdf
artifacts/dream_reports/dream_20260515T132059/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e09a6da0-f34b-46e9-ae21-bab28952b980",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "74c8a160-6de3-4683-a0fa-dfd5bcd7c2e1",
  "sourceToolAssistantUUID": "e09a6da0-f34b-46e9-ae21-bab28952b980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T14:18:59.983Z_

Let me read the paper tex file (the latest best version) and also the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74c8a160-6de3-4683-a0fa-dfd5bcd7c2e1",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwnqocyuvUErU1ywxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ec0a475-e65a-4058-897d-87e0edd4aa4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxE8aAAsNn9xPRxRjAYqRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 17418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 14 · 2026-05-15T14:19:03.746Z_

<details open><summary>🔧 Tool call — Read · `toolu_0181D4xgUyQorjcLzKue2NcQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ec0a475-e65a-4058-897d-87e0edd4aa4e",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwnqocyuvUErU1ywxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a5d04f7-7cd5-44cd-aebd-16af4646376b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxE8aAAsNn9xPRxRjAYqRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 17418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 15 · 2026-05-15T14:19:03.762Z_

<details><summary>↩ Tool result · `toolu_0181D4xgUyQorjcLzKue2NcQ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{natbib}
13	\usepackage{tabularx}
14	\usepackage{array}
15	
16	\newcommand{\method}{FREIGE}
17	\newcommand{\ced}{CED}
18	\newcommand{\edcr}{EDCR}
19	\newcommand{\rsft}{RSFT}
20	
21	\title{FREIGE: Faithful Evidence Generation for LLM-Based\\Document-Level Relation Extraction via\\Contrastive Evidence Discrimination}
22	
23	\author{Anonymous Submission to EMNLP 2026}
24	\date{}
25	
26	\begin{document}
27	\maketitle
28	
29	%==============================================================================
30	\begin{abstract}
31	%==============================================================================
32	Large language models (LLMs) are rapidly closing the gap with encoder-based methods on document-level relation extraction (DocRE), yet no existing LLM approach produces verifiable evidence---the supporting sentences that ground each predicted relation triple.
33	We present \method{} (\textbf{F}aithful \textbf{R}elation \textbf{E}xtraction with \textbf{I}ntra-document \textbf{G}rounded \textbf{E}vidence), the first generative LLM framework that jointly outputs relation triples \emph{and} explicit sentence-level evidence citations on DocRED.
34	At the core of \method{} is \ced{} (\textbf{C}ontrastive \textbf{E}vidence \textbf{D}iscrimination), a scoring function that measures evidence quality through intra-document hard-negative contrast: the entailment gap between gold evidence and the best entity-sharing distractor sentence.
35	We show that na\"ive NLI-based scoring is fooled by entity-sharing distractors and that online RL (GRPO+QLoRA) with \ced{} reward leads to catastrophic forgetting---a novel \emph{evidence--extraction decoupling} phenomenon where evidence quality improves (Evi-F1 up to 0.850) while extraction collapses (rel\_F1 $<$ 0.02).
36	Instead, using \ced{} as an offline quality filter for rejection sampling fine-tuning (\rsft{}) yields consistent gains: +5.5pp rel\_F1, +1.7pp Evi-F1 (conditional), and $-$7.1pp \edcr{} on the DocRED test set over SFT.
37	We further propose the \edcr{} (\textbf{E}ntity-sharing \textbf{D}istractor \textbf{C}itation \textbf{R}ate) metric, validated by human annotation (Pearson $r$=0.62), to diagnose plausible-looking but unfaithful evidence that standard Evi-F1 misses.
38	Experiments across three model scales (1.7B--8B) and two DocRED variants confirm the generality of our approach.
39	\end{abstract}
40	
41	%==============================================================================
42	\section{Introduction}
43	\label{sec:intro}
44	%==============================================================================
45	
46	Document-level relation extraction (DocRE) requires identifying relational facts between entity pairs that may span multiple sentences in a document.
47	Recent encoder-based methods achieve strong extraction performance and provide implicit evidence through attention-weight thresholding, but their evidence is not directly interpretable.
48	Meanwhile, LLM-based approaches to DocRE have shown competitive extraction accuracy, yet none produces explicit evidence citations that a human auditor can verify---a critical gap for deployment in knowledge base population, biomedical curation, and RAG provenance tracking.
49	
50	A natural approach is to train LLMs with faithfulness rewards derived from natural language inference (NLI) models.
51	However, we identify a fundamental failure mode: \emph{entity-sharing distractor sentences}---sentences that mention the same entities as the relation but do not actually support it---receive spuriously high NLI entailment scores due to lexical overlap.
52	In our SFT baseline, 71.2\% of cited sentences are such distractors (\edcr{}=0.712), revealing that standard evidence metrics like Evi-F1 are blind to this systematic error pattern.
53	
54	We further discover that applying online RL (GRPO) with evidence-quality rewards causes \emph{catastrophic forgetting with evidence--extraction decoupling}: the model learns to produce high-quality evidence (Evi-F1 up to 0.850) while its extraction capability collapses (rel\_F1 $< 0.02$).
55	This phenomenon persists across multiple reward types, learning rates, and group sizes ($G$=4, 8), pointing to a structural incompatibility between on-policy RL and document-level structured IE under parameter-efficient fine-tuning.
56	
57	To address these challenges, we propose \method{}, comprising three contributions:
58	
59	\begin{enumerate}
60	\item \textbf{\ced{} (Contrastive Evidence Discrimination)}: A scoring function that evaluates evidence quality through the entailment margin between cited evidence and the best intra-document hard negative, effectively serving as an anti-reward-overoptimization mechanism for evidence grounding.
61	
62	\item \textbf{\ced{}-guided \rsft{}}: Rather than using \ced{} as an online reward, we employ it as an offline quality filter---generating $N$ candidates from an SFT model, scoring with \ced{}, and fine-tuning on the top-$k$ highest-quality outputs. This sidesteps the catastrophic forgetting of online RL while retaining the signal strength of \ced{}.
63	
64	\item \textbf{\edcr{} (Entity-sharing Distractor Citation Rate)}: A diagnostic metric that measures the proportion of cited sentences sharing entities with the target relation but absent from gold evidence, capturing a failure mode invisible to standard Evi-F1.
65	\end{enumerate}
66	
67	On the DocRED test set, \method{} achieves rel\_F1=0.455, Evi-F1\textsubscript{joint}=0.376, and \edcr{}=0.648, representing the first LLM-based DocRE system with explicit evidence output.
68	Results generalize across model scales (1.7B--8B), dataset variants (DocRED, Re-DocRED), and are robust to the choice of NLI backbone.
69	
70	%==============================================================================
71	\section{Related Work}
72	\label{sec:related}
73	%==============================================================================
74	
75	\paragraph{Document-Level Relation Extraction.}
76	Encoder-based DocRE methods achieve state-of-the-art extraction performance.
77	DREEAM provides evidence through attention-weight thresholding over a RoBERTa-large encoder, achieving Evi-F1\textsubscript{joint}=0.573 on DocRED.
78	SAIS follows a similar paradigm (Evi-F1\textsubscript{joint}=0.557).
79	Recent LLM-based approaches such as LMRC (LLaMA-3.1-8B, F1=60.69) demonstrate competitive extraction but produce no evidence.
80	\method{} bridges this gap by jointly generating triples and explicit evidence.
81	
82	\paragraph{Reward Hacking and Overoptimization.}
83	Reward overoptimization in RLHF is well-documented: proxy rewards diverge from true objectives as policy optimization progresses.
84	CED connects to this literature by providing a contrastive anti-overoptimization mechanism specifically designed for evidence grounding, where entity-sharing distractors create systematic reward hacking opportunities.
85	
86	\paragraph{Rejection Sampling Fine-Tuning.}
87	RSFT has been shown theoretically equivalent to PPO under certain conditions.
88	Our work applies RSFT to a novel domain---evidence-grounded IE---and demonstrates that for structured document-level tasks, offline quality filtering outperforms both online RL (GRPO) and offline preference learning (DPO).
89	
90	%==============================================================================
91	\section{Method}
92	\label{sec:method}
93	%==============================================================================
94	
95	\subsection{Task Formulation}
96	
97	Given a document $D$ with sentences $\{S_1, \ldots, S_n\}$ and entity mentions, the model must output a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ is the relation type, $t$ is the tail entity, and $E \subseteq \{S_1, \ldots, S_n\}$ is the set of evidence sentences supporting the relation.
98	The model generates these tuples in a structured text format with explicit sentence index citations $[\texttt{S}_i]$.
99	
100	\subsection{Contrastive Evidence Discrimination (\ced{})}
101	
102	Standard NLI-based evidence scoring computes the mean entailment probability over cited sentences:
103	\begin{equation}
104	\text{flat-NLI}(E) = \frac{1}{|E|}\sum_{s \in E} p_{\text{entail}}(s \mid h, r, t)
105	\end{equation}
106	This score is vulnerable to entity-sharing distractors: sentences mentioning $h$ or $t$ that do not support $r$ but achieve high entailment scores due to lexical overlap.
107	
108	\ced{} addresses this by computing a contrastive margin:
109	\begin{equation}
110	\text{\ced{}}(E, D) = \frac{1}{|E|}\sum_{s \in E} \Big[ p_{\text{entail}}(s) - \max_{s' \in \mathcal{N}(h,t,D)} p_{\text{entail}}(s') \Big]
111	\end{equation}
112	where $\mathcal{N}(h,t,D) = \{s' \in D \setminus E_{\text{gold}} : s' \text{ mentions } h \text{ or } t\}$ is the set of intra-document hard negatives---entity-sharing but non-gold sentences.
113	The margin directly penalizes evidence whose entailment score is not substantially higher than the best distractor, serving as an anti-reward-overoptimization mechanism.
114	
115	We implement \ced{} using DeBERTa-v3-base fine-tuned on MNLI (86M parameters), with the relation verbalized as the NLI hypothesis.
116	
117	\subsection{\ced{}-Guided Rejection Sampling Fine-Tuning}
118	
119	Our training pipeline proceeds in three stages:
120	
121	\paragraph{Stage 1: SFT.}
122	We fine-tune a base LLM (Qwen3-4B) with QLoRA on gold DocRED training data, producing a model that can generate (triple, evidence) tuples but with high distractor citation rates.
123	
124	\paragraph{Stage 2: Candidate Generation and \ced{} Filtering.}
125	For each training document, we sample $N=8$ candidate outputs from the SFT model at temperature 0.7.
126	Each candidate is scored by \ced{}, and only the top-$k$ ($k=1$) candidate per document is retained.
127	This yields ${\sim}$2,718 high-quality training samples from 21,952 candidates (12.4\% retention rate).
128	
129	\paragraph{Stage 3: \rsft{}.}
130	The SFT model is further fine-tuned on the \ced{}-filtered candidates with standard supervised loss.
131	The key insight is that \ced{} serves as a \emph{data quality filter} rather than a training reward, completely avoiding the credit-assignment difficulties and catastrophic forgetting of on-policy RL on structured outputs.
132	
133	\subsection{\edcr{}: Entity-Sharing Distractor Citation Rate}
134	\label{sec:edcr}
135	
136	We propose \edcr{} as a diagnostic metric:
137	\begin{equation}
138	\edcr{} = \frac{|\{s \in \hat{E} : s \notin E_{\text{gold}} \wedge s \in \mathcal{N}(h,t,D)\}|}{|\hat{E}|}
139	\end{equation}
140	where $\hat{E}$ is the set of predicted evidence sentences.
141	\edcr{} captures a specific failure mode invisible to standard Evi-F1: citing sentences that \emph{look} like evidence (they mention the right entities) but do not actually support the relation.
142	Lower \edcr{} is better (denoted \edcr{}$\downarrow$ in tables).
143	
144	%==============================================================================
145	\section{Experiments}
146	\label{sec:experiments}
147	%==============================================================================
148	
149	\subsection{Setup}
150	
151	\paragraph{Dataset.}
152	We evaluate on DocRED, the standard benchmark for document-level RE with sentence-level evidence annotations.
153	We additionally report results on Re-DocRED, which corrects ${\sim}$25\% false-negative relations in the original annotations.
154	Test set evaluation uses the official CodaLab submission for rel\_F1 and Ign\_F1.
155	
156	\paragraph{Model and Training.}
157	Our base model is Qwen3-4B with QLoRA (rank=64).
158	SFT uses the full DocRED gold training set (12,151 examples).
159	\rsft{} uses the best SFT checkpoint as the sampling policy, generating $N$=8 candidates per document at temperature 0.7.
160	We report results for the best \rsft{} configuration (3 epochs, $\alpha$=128, seed=43).
161	
162	\paragraph{Metrics.}
163	We report: (1)~rel\_F1 and Ign\_F1 for extraction quality; (2)~Evi-F1\textsubscript{joint} (DREEAM protocol: evidence counts only when the relation is also correct) and Evi-F1\textsubscript{cond} (conditional on correct relation); (3)~\edcr{}$\downarrow$ for distractor citation diagnosis.
164	
165	\paragraph{Baselines.}
166	We compare against: DREEAM (RoBERTa-large, attention-based evidence), SAIS (RoBERTa-large, attention-based), and LMRC (LLaMA-3.1-8B, no evidence).
167	
168	%------------------------------------------------------------------------------
169	\subsection{Main Results}
170	\label{sec:main_results}
171	%------------------------------------------------------------------------------
172	
173	Table~\ref{tab:main_results} presents test set results.
174	\method{} (RSFT+CED) achieves rel\_F1=0.455, a +5.5pp improvement over the SFT baseline (0.400), with consistent gains across all metrics.
175	The Evi-F1\textsubscript{joint} of 0.376 represents the first reported number for any LLM-based method on this metric, as prior generative approaches (LMRC, DocKS-RAG) do not output evidence.
176	
177	\begin{table}[t]
178	\centering
179	\small
180	\caption{Test set results on DocRED. $\dagger$: encoder-based methods with attention-threshold evidence. $\ddagger$: generative LLM methods. Evi-F1\textsubscript{J} = joint (DREEAM protocol); Evi-F1\textsubscript{C} = conditional on correct relation.}
181	\label{tab:main_results}
182	\begin{tabular}{@{}lcccccc@{}}
183	\toprule
184	\textbf{Method} & \textbf{Type} & \textbf{rel\_F1} & \textbf{Ign\_F1} & \textbf{Evi-F1\textsubscript{J}} & \textbf{Evi-F1\textsubscript{C}} & \textbf{\edcr{}$\downarrow$} \\
185	\midrule
186	DREEAM$^\dagger$         & Enc.  & ---   & ---   & 0.573 & 0.834 & ---   \\
187	SAIS$^\dagger$           & Enc.  & ---   & ---   & 0.557 & ---   & ---   \\
188	LMRC$^\ddagger$          & Gen.  & 0.607 & ---   & ---   & ---   & ---   \\
189	\midrule
190	SFT baseline$^\ddagger$  & Gen.  & 0.400 & 0.381 & 0.322 & 0.790 & 0.719 \\
191	RSFT flat-NLI$^\ddagger$ & Gen.  & 0.430 & 0.412 & 0.342 & 0.788 & 0.701 \\
192	\textbf{\method{}}$^\ddagger$ & Gen. & \textbf{0.455} & \textbf{0.437} & \textbf{0.376} & \textbf{0.807} & \textbf{0.648} \\
193	\bottomrule
194	\end{tabular}
195	\end{table}
196	
197	Compared with encoder-based methods, the gap in Evi-F1\textsubscript{joint} (0.376 vs.\ DREEAM's 0.573) is primarily driven by the extraction accuracy gap (rel\_F1 0.455 vs.\ ${\sim}$0.631), not evidence quality: on correctly predicted triples, \method{}'s conditional Evi-F1 (0.807) approaches DREEAM's (0.834).
198	Critically, \method{} outputs \emph{explicit} sentence citations whereas DREEAM's evidence is implicit attention weights---a qualitatively different and more interpretable form.
199	
200	Table~\ref{tab:joint_vs_cond} provides a comprehensive view of joint vs.\ conditional Evi-F1 across methods on the dev set, demonstrating that the decoupling between extraction and evidence quality is most extreme for GRPO (joint Evi-F1 of 0.012 despite conditional Evi-F1 of 0.850).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a5d04f7-7cd5-44cd-aebd-16af4646376b",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "78716e5e-361d-48ff-908b-96aafdab588e",
  "sourceToolAssistantUUID": "8a5d04f7-7cd5-44cd-aebd-16af4646376b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T14:19:03.805Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0137xdRgqrnqizZV3hkasNcN`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78716e5e-361d-48ff-908b-96aafdab588e",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwnqocyuvUErU1ywxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea29283e-b35e-4d27-8d0c-24ea9d98a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxE8aAAsNn9xPRxRjAYqRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 17418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 17 · 2026-05-15T14:19:03.828Z_

<details><summary>↩ Tool result · `toolu_0137xdRgqrnqizZV3hkasNcN`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea29283e-b35e-4d27-8d0c-24ea9d98a894",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "a2981044-f9ec-465a-86f4-1c8bc7e795ef",
  "sourceToolAssistantUUID": "ea29283e-b35e-4d27-8d0c-24ea9d98a894",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T14:19:03.839Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Kbb8XUugbALEwsmTJyf5ce`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2981044-f9ec-465a-86f4-1c8bc7e795ef",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VwnqocyuvUErU1ywxK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9917386-1141-4f21-b294-65356e1c3833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxE8aAAsNn9xPRxRjAYqRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2944,
      "cache_read_input_tokens": 17418,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2944,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 19 · 2026-05-15T14:19:03.850Z_

<details><summary>↩ Tool result · `toolu_01Kbb8XUugbALEwsmTJyf5ce`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\\n\\n## 待处理\\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\\n\\n## 趋势\\n成功 26 / 负向 11 / 失败 12 / 共 71\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_ced_scoring_topk3: 已被终止 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n- mvp2_eval_rsft_r2b_maxtok1536: 已被终止 — unknown\\n\", \"total_chars\": 3533, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9917386-1141-4f21-b294-65356e1c3833",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "072176dd-9e8a-48c2-b9bf-77bf79e53aa8",
  "sourceToolAssistantUUID": "c9917386-1141-4f21-b294-65356e1c3833",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T14:19:09.113Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DSefdXKPud3e8XVdHJiAnH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "072176dd-9e8a-48c2-b9bf-77bf79e53aa8",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VxNnyRMi9Ehrroup2e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e641669-dbdd-40ca-999e-e8f8a2fa9f4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXtb6P6stmLmc77vJ3jmi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7550,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7550,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 21 · 2026-05-15T14:19:09.121Z_

<details><summary>↩ Tool result · `toolu_01DSefdXKPud3e8XVdHJiAnH`</summary>

```text
200	Table~\ref{tab:joint_vs_cond} provides a comprehensive view of joint vs.\ conditional Evi-F1 across methods on the dev set, demonstrating that the decoupling between extraction and evidence quality is most extreme for GRPO (joint Evi-F1 of 0.012 despite conditional Evi-F1 of 0.850).
201	
202	\begin{table}[t]
203	\centering
204	\small
205	\caption{Conditional vs.\ Joint Evi-F1 on DocRED dev set. Joint Evi-F1 penalizes incorrect relation predictions with zero evidence credit.}
206	\label{tab:joint_vs_cond}
207	\begin{tabular}{@{}lcccc@{}}
208	\toprule
209	\textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1\textsubscript{C}} & \textbf{Evi-F1\textsubscript{J}} & \textbf{\edcr{}$\downarrow$} \\
210	\midrule
211	GRPO (lr=5e-6)    & 0.014 & 0.850 & 0.012 & 0.988 \\
212	GRPO (lr=5e-5)    & 0.211 & 0.567 & 0.119 & 0.858 \\
213	SFT baseline      & 0.406 & 0.798 & 0.322 & 0.712 \\
214	RSFT flat-NLI     & 0.441 & 0.797 & 0.350 & 0.689 \\
215	CED-reranker      & 0.415 & 0.821 & 0.341 & 0.598 \\
216	\rsft{} CED       & 0.468 & 0.816 & 0.381 & 0.639 \\
217	\bottomrule
218	\end{tabular}
219	\end{table}
220	
221	%------------------------------------------------------------------------------
222	\subsection{Why Online RL Fails: Evidence--Extraction Decoupling}
223	\label{sec:grpo_failure}
224	%------------------------------------------------------------------------------
225	
226	A central finding is that GRPO+QLoRA with evidence-quality rewards leads to catastrophic forgetting, regardless of reward type, learning rate, or group size.
227	Table~\ref{tab:rl_spectrum} presents the full online--offline RL spectrum.
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\caption{Online--offline RL spectrum on DocRED dev set. GRPO exhibits catastrophic forgetting across configurations. DPO avoids collapse but degrades below SFT. Only \rsft{} improves over SFT.}
233	\label{tab:rl_spectrum}
234	\begin{tabular}{@{}llccccc@{}}
235	\toprule
236	\textbf{Method} & \textbf{RL Type} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} & \textbf{Catastrophic?} \\
237	\midrule
238	GRPO $G$=4    & On-policy   & 0.014 & 0.850 & 0.988 & Yes \\
239	GRPO $G$=8    & On-policy   & 0.031 & 0.816 & 0.981 & Yes \\
240	DPO+CED       & Offline pref. & 0.325 & 0.786 & 0.683 & No (degraded) \\
241	SFT            & No RL       & 0.406 & 0.798 & 0.712 & No \\
242	\textbf{\rsft{}+CED} & Offline filtered & \textbf{0.468} & \textbf{0.816} & \textbf{0.639} & No \\
243	\bottomrule
244	\end{tabular}
245	\end{table}
246	
247	\paragraph{GRPO Catastrophic Forgetting.}
248	All GRPO configurations exhibit the same pattern: the CED reward increases while rel\_F1 collapses to near zero.
249	With $G$=4 (lr=5e-6), rel\_F1 drops to 0.014 while Evi-F1 reaches 0.850---the model learns to cite extensive evidence but can no longer extract relations.
250	Increasing $G$ to 8 marginally delays the onset of forgetting (step ${\sim}$15 vs.\ ${\sim}$10) but does not prevent it: best rel\_F1 remains 0.031, far below SFT's 0.406.
251	This rules out advantage-estimation noise as the root cause and points to a structural incompatibility: QLoRA's rank-limited parameter space, when updated by RL gradients, preferentially optimizes the easier evidence dimension at the expense of structured extraction.
252	
253	\paragraph{DPO as Intermediate Baseline.}
254	DPO+CED (Table~\ref{tab:rl_spectrum}) avoids catastrophic forgetting (rel\_F1=0.325) but \emph{degrades} below SFT (0.406), yielding $-$8.1pp.
255	This demonstrates that the problem is not simply online vs.\ offline RL: DPO's token-level contrastive loss struggles with credit assignment over long structured outputs, and suppressing rejected candidates inadvertently penalizes correct extraction patterns.
256	The full spectrum GRPO (0.014--0.031) $\ll$ DPO (0.325) $<$ SFT (0.406) $<$ \rsft{} (0.468) shows that for document-level IE, \ced{} is most effective as a data filter, not a learning objective.
257	
258	\paragraph{Forgetting Dynamics.}
259	Analysis of 42 checkpoints across 3 GRPO configurations reveals a consistent three-phase pattern: (1)~\emph{Decoupling onset} (steps 5--15): rel\_F1 begins declining while Evi-F1 rises; (2)~\emph{Acceleration} (steps 15--50): rel\_F1 collapses below 0.05, reward saturates; (3)~\emph{Plateau} (steps 50--100): rel\_F1 oscillates near zero, Evi-F1 stabilizes at 0.80--0.85.
260	All configurations converge to a common attractor in the (low-rel\_F1, high-Evi-F1) region, regardless of learning rate or group size.
261	
262	%------------------------------------------------------------------------------
263	\subsection{\ced{} vs.\ Flat-NLI Scoring}
264	\label{sec:ced_vs_flatnli}
265	%------------------------------------------------------------------------------
266	
267	Table~\ref{tab:ced_ablation} presents the core ablation comparing \ced{}-filtered vs.\ flat-NLI-filtered \rsft{}.
268	\ced{} yields statistically significant improvements across all three metrics (paired bootstrap, $p < 0.01$).
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{CED vs.\ flat-NLI as \rsft{} filtering signal (DocRED dev set). Both \rsft{} variants improve over SFT; CED significantly outperforms flat-NLI ($p < 0.01$ for all metrics, paired bootstrap).}
274	\label{tab:ced_ablation}
275	\begin{tabular}{@{}lccccc@{}}
276	\toprule
277	\textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} & \textbf{$n_{\text{train}}$} \\
278	\midrule
279	SFT baseline                    & 0.406 & 0.798 & 0.712 & 12,151 \\
280	\rsft{} flat-NLI (A: 3ep)       & 0.441 & 0.795 & 0.695 & 2,845 \\
281	\rsft{} flat-NLI (B: 1ep)       & 0.438 & 0.797 & 0.689 & 2,845 \\
282	\rsft{} CED (s43: 3ep)          & \textbf{0.468} & \textbf{0.816} & \textbf{0.639} & 2,718 \\
283	\rsft{} CED (r2b: 1ep)          & 0.449 & 0.813 & 0.661 & 2,718 \\
284	\midrule
285	$\Delta$ (CED best $-$ flat-NLI best)  & +2.71pp & +2.08pp & $-$5.64pp & --- \\
286	$p$-value (paired bootstrap)           & 0.007 & 0.004 & 0.002 & --- \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	The advantage of \ced{} is concentrated in distractor-dense documents (distractor density $>$ 0.4), where the Evi-F1 gap expands to ${\sim}$3.5pp, while in low-distractor documents the difference is negligible (${\sim}$0.8pp, not significant).
292	This confirms that the contrastive margin is specifically effective at distinguishing true evidence from entity-sharing distractors---precisely the failure mode that flat-NLI scoring cannot address.
293	
294	Both flat-NLI \rsft{} variants still improve over SFT (+3.2--3.6pp rel\_F1), indicating that \emph{any} quality filtering helps, but \ced{}'s contrastive design provides additional discriminative power where it matters most.
295	
296	%------------------------------------------------------------------------------
297	\subsection{\ced{} Usage Modes: Training vs.\ Inference}
298	\label{sec:ced_usage}
299	%------------------------------------------------------------------------------
300	
301	Table~\ref{tab:ced_modes} compares two usage modes of \ced{}: as a training data filter (\rsft{}) and as an inference-time reranker.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\caption{CED usage modes (DocRED dev set). CED as training signal (\rsft{}) substantially outperforms CED as inference-time reranker.}
307	\label{tab:ced_modes}
308	\begin{tabular}{@{}lcccc@{}}
309	\toprule
310	\textbf{CED Usage} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} & \textbf{Extra Training} \\
311	\midrule
312	SFT (no CED)                & 0.406 & 0.798 & 0.712 & --- \\
313	CED-reranker (inference)     & 0.415 & 0.821 & 0.598 & None \\
314	\rsft{} flat-NLI (training)  & 0.441 & 0.797 & 0.689 & \rsft{} \\
315	\rsft{} CED (training)       & \textbf{0.468} & \textbf{0.816} & 0.639 & \rsft{} \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	CED-reranking achieves the lowest \edcr{} (0.598) by directly selecting the candidate with the highest contrastive margin, but its rel\_F1 gain is modest (+0.95pp over SFT).
321	This is because reranking cannot improve beyond the quality ceiling of the candidate pool---it selects the best existing output but does not shift the model's generation distribution.
322	In contrast, \rsft{} with CED filtering gains +6.26pp rel\_F1 by teaching the model to \emph{generate} higher-quality outputs, confirming that CED is most effective as a training signal rather than a pure inference-time mechanism.
323	
324	%------------------------------------------------------------------------------
325	\subsection{\edcr{} as a Diagnostic Metric}
326	\label{sec:edcr_analysis}
327	%------------------------------------------------------------------------------
328	
329	\paragraph{Cross-Method Diagnostic.}
330	Table~\ref{tab:edcr_diagnostic} presents \edcr{} computed across all evidence-producing methods, revealing a clear gradient that aligns with the training paradigm.
331	
332	\begin{table}[t]
333	\centering
334	\small
335	\caption{Cross-method \edcr{} diagnostic (DocRED dev set). Methods sorted by \edcr{} descending. \edcr{} captures a systematic gradient from catastrophic GRPO to CED-reranker.}
336	\label{tab:edcr_diagnostic}
337	\begin{tabular}{@{}lcccc@{}}
338	\toprule
339	\textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} & \textbf{$n_{\text{distractor}}$} \\
340	\midrule
341	GRPO ckpt-100 (lr=5e-6) & 0.014 & 0.850 & 0.988 & 12,675 \\
342	GRPO ckpt-90 (lr=5e-5)  & 0.211 & 0.567 & 0.858 & 8,431 \\
343	SFT baseline             & 0.406 & 0.798 & 0.712 & 10,113 \\
344	RSFT flat-NLI            & 0.441 & 0.797 & 0.689 & 9,556 \\
345	RSFT CED (r2b)           & 0.449 & 0.813 & 0.661 & 8,950 \\
346	RSFT CED (s43)           & 0.468 & 0.816 & 0.639 & 8,475 \\
347	CED-reranker             & 0.415 & 0.821 & 0.598 & 7,768 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	The \edcr{} gradient (0.988 $\to$ 0.598) is monotonically related to the strength of evidence-quality supervision: GRPO outputs nearly all distractors, SFT has no evidence signal, flat-NLI provides weak filtering, CED provides contrastive filtering, and CED-reranker applies CED directly at inference.
353	Notably, the cross-method Pearson correlation between \edcr{} and Evi-F1 is only $r$=$-$0.42, confirming that \edcr{} captures a dimension of evidence quality \emph{not} measured by standard Evi-F1.
354	
355	\paragraph{Human Validation.}
356	To validate \edcr{} as a meaningful automatic metric, we conduct a human annotation study on 100 samples (25 per method: GRPO, SFT, RSFT flat-NLI, RSFT CED).
357	Three annotators independently judge whether each cited sentence truly supports its corresponding relation (inter-annotator Cohen's $\kappa$=0.72, substantial agreement).
358	Table~\ref{tab:human_edcr} presents the results.
359	
360	\begin{table}[t]
361	\centering
362	\small
363	\caption{Human validation of \edcr{} (100 samples, 3 annotators, $\kappa$=0.72). Auto \edcr{} correlates with human distractor rate at Pearson $r$=0.62.}
364	\label{tab:human_edcr}
365	\begin{tabular}{@{}lcccc@{}}
366	\toprule
367	\textbf{Method} & \textbf{\edcr{}\textsubscript{auto}} & \textbf{Human dist.\ rate} & $\Delta$ & $n$ \\
368	\midrule
369	GRPO ckpt-90     & 0.858 & 0.954 & $-$0.096 & 25 \\
370	SFT              & 0.712 & 0.645 & +0.067 & 25 \\
371	RSFT flat-NLI    & 0.695 & 0.608 & +0.087 & 25 \\
372	RSFT CED         & 0.639 & 0.524 & +0.115 & 25 \\
373	\midrule
374	\multicolumn{2}{@{}l}{Overall Pearson $r$} & \multicolumn{3}{c}{0.62 ($p < 0.001$)} \\
375	\bottomrule
376	\end{tabular}
377	\end{table}
378	
379	The overall Pearson $r$=0.62 confirms that \edcr{} is a meaningful proxy for human-judged evidence quality.
380	The ranking of methods is preserved perfectly between automatic and human evaluation.
381	Auto \edcr{} exhibits a slight positive bias (+6.8pp on average), because the entity-sharing heuristic is somewhat stricter than human judgment---some entity-sharing sentences are deemed partially supportive by human annotators.
382	The CED RSFT method shows the largest auto--human gap (0.115), suggesting that CED-trained models produce citations that are correct by the entity-sharing criterion but occasionally omit contextually relevant (though not gold-annotated) sentences.
383	
384	%------------------------------------------------------------------------------
385	\subsection{Generalization Experiments}
386	\label{sec:generalization}
387	%------------------------------------------------------------------------------
388	
389	\paragraph{Model Size Ablation.}
390	Table~\ref{tab:model_size} verifies that \rsft{}+CED is effective across model scales from 1.7B to 8B parameters.
391	
392	\begin{table}[t]
393	\centering
394	\small
395	\caption{Model size ablation (DocRED dev set). \rsft{}+CED improves consistently across 1.7B--8B.}
396	\label{tab:model_size}
397	\begin{tabular}{@{}llcccr@{}}
398	\toprule
399	\textbf{Model} & \textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} & $\Delta$\textbf{rel\_F1} \\
400	\midrule
401	\multirow{2}{*}{Qwen3-1.7B} & SFT      & 0.341 & 0.753 & 0.746 & --- \\
402	                             & \rsft{}+CED & 0.372 & 0.778 & 0.693 & +3.12pp \\
403	\midrule
404	\multirow{2}{*}{Qwen3-4B}   & SFT      & 0.406 & 0.798 & 0.712 & --- \\
405	                             & \rsft{}+CED & 0.468 & 0.816 & 0.639 & +6.26pp \\
406	\midrule
407	\multirow{2}{*}{Qwen3-8B}   & SFT      & 0.442 & 0.813 & 0.689 & --- \\
408	                             & \rsft{}+CED & 0.491 & 0.837 & 0.619 & +4.89pp \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	The absolute improvement ranges from +3.1pp (1.7B) to +6.3pp (4B) to +4.9pp (8B).
414	The 4B model occupies a sweet spot: large enough to generate diverse high-quality candidates but small enough that SFT alone leaves substantial room for improvement.
415	The 8B model achieves the highest absolute performance (rel\_F1=0.491) but has smaller relative gains because its SFT baseline is already stronger.
416	\edcr{} decreases consistently across all scales ($-$5.2 to $-$7.3pp), confirming the generality of CED-based evidence improvement.
417	
418	\paragraph{Re-DocRED.}
419	Table~\ref{tab:redocred} shows results on Re-DocRED, which corrects ${\sim}$25\% false-negative annotations.
420	
421	\begin{table}[t]
422	\centering
423	\small
424	\caption{DocRED vs.\ Re-DocRED (dev set). \rsft{}+CED gains are preserved on cleaner annotations.}
425	\label{tab:redocred}
426	\begin{tabular}{@{}llcccc@{}}
427	\toprule
428	\textbf{Dataset} & \textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} \\
429	\midrule
430	\multirow{2}{*}{DocRED}    & SFT      & 0.406 & 0.798 & 0.712 \\
431	                           & \rsft{}+CED & 0.468 & 0.816 & 0.639 \\
432	\midrule
433	\multirow{2}{*}{Re-DocRED} & SFT      & 0.453 & 0.811 & 0.689 \\
434	                           & \rsft{}+CED & 0.509 & 0.838 & 0.602 \\
435	\bottomrule
436	\end{tabular}
437	\end{table}
438	
439	The \rsft{}+CED improvement (+5.55pp on Re-DocRED vs.\ +6.26pp on DocRED) is preserved, demonstrating that CED is not exploiting annotation noise.
440	All methods benefit from cleaner annotations, with \edcr{} decreasing on Re-DocRED because some previously labeled distractors are reclassified as gold evidence.
441	
442	\paragraph{top-$k$ Ablation.}
443	Table~\ref{tab:topk} examines the effect of CED filtering strictness.
444	
445	\begin{table}[t]
446	\centering
447	\small
448	\caption{top-$k$ ablation for CED filtering (DocRED dev set). Stricter filtering ($k$=1) yields higher quality despite fewer training samples.}
449	\label{tab:topk}
450	\begin{tabular}{@{}cccccc@{}}
451	\toprule
452	\textbf{top-$k$} & $n_{\text{train}}$ & \textbf{Mean CED} & \textbf{rel\_F1} & \textbf{Evi-F1} & \textbf{\edcr{}$\downarrow$} \\
453	\midrule
454	1 & 2,718 & 0.668 & \textbf{0.468} & \textbf{0.816} & \textbf{0.639} \\
455	3 & 7,856 & 0.523 & 0.452 & 0.803 & 0.671 \\
456	\bottomrule
457	\end{tabular}
458	\end{table}
459	
460	Strict filtering ($k$=1, 2,718 samples) outperforms relaxed filtering ($k$=3, 7,856 samples) across all metrics.
461	The additional samples from $k$=3 have systematically lower CED scores (mean 0.523 vs.\ 0.668), introducing distractor-heavy training examples that dilute the quality signal.
462	This confirms the ``less is more'' principle for \rsft{}: the SFT stage already provides broad coverage, and \rsft{} needs only a small number of high-quality samples to calibrate evidence citation behavior.
463	
464	\paragraph{NLI Model Ablation.}
465	Table~\ref{tab:nli_ablation} shows that replacing DeBERTa-v3-base (86M) with DeBERTa-v3-large (304M) yields marginal improvements (+0.38pp rel\_F1), confirming that \ced{}'s effectiveness stems from the contrastive design rather than the NLI model's capacity.
466	
467	\begin{table}[t]
468	\centering
469	\small
470	\caption{NLI model ablation for CED scoring. Larger NLI model provides marginal gains.}
471	\label{tab:nli_ablation}
472	\begin{tabular}{@{}lcccc@{}}
473	\toprule
474	\textbf{NLI Model} & \textbf{Params} & \textbf{Disc.\ Acc} & \textbf{\rsft{} rel\_F1} & \textbf{\rsft{} Evi-F1} \\
475	\midrule
476	DeBERTa-v3-base  & 86M  & 0.815 & 0.468 & 0.816 \\
477	DeBERTa-v3-large & 304M & 0.847 & 0.472 & 0.819 \\
478	\midrule
479	$\Delta$ & --- & +0.032 & +0.38pp & +0.33pp \\
480	\bottomrule
481	\end{tabular}
482	\end{table}
483	
484	The top-1 candidate selection agrees between base and large models on 89\% of documents; the 11\% disagreements produce only marginal downstream differences, lowering the computational barrier for adopting \method{}.
485	
486	\paragraph{Baseline Comparison with Evidence Methods.}
487	Table~\ref{tab:evidence_comparison} contextualizes \method{} against encoder-based evidence methods.
488	
489	\begin{table}[t]
490	\centering
491	\small
492	\caption{Evidence baseline comparison (dev set). \method{} is the first generative LLM method with explicit evidence; the Evi-F1\textsubscript{J} gap vs.\ encoders is driven by extraction accuracy, not evidence quality.}
493	\label{tab:evidence_comparison}
494	\begin{tabular}{@{}llcccc@{}}
495	\toprule
496	\textbf{Method} & \textbf{Type} & \textbf{rel\_F1} & \textbf{Evi-F1\textsubscript{J}} & \textbf{Evidence Form} \\
497	\midrule
498	DREEAM      & Encoder  & 0.631 & 0.572 & Attention threshold \\
499	SAIS        & Encoder  & 0.610 & 0.554 & Attention threshold \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e641669-dbdd-40ca-999e-e8f8a2fa9f4f",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "a669a1e7-4db3-4d45-989c-d7a085c1968e",
  "sourceToolAssistantUUID": "0e641669-dbdd-40ca-999e-e8f8a2fa9f4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T14:19:09.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_016RxLuDibtyFb1NKt1Z1ZHM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a669a1e7-4db3-4d45-989c-d7a085c1968e",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VxNnyRMi9Ehrroup2e",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "649ac3ab-2cdf-4d9d-9846-e8284a536c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmXtb6P6stmLmc77vJ3jmi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7550,
      "cache_read_input_tokens": 20362,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 20362,
          "cache_creation_input_tokens": 7550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7550,
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

_source line 23 · 2026-05-15T14:19:09.726Z_

<details><summary>↩ Tool result · `toolu_016RxLuDibtyFb1NKt1Z1ZHM`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。四个 Claims 全部有强证据支撑： C1（首个同时生成抽取+证据的 LLM DocRE）有
2	  test set 显著优势； C2（CED > flat-NLI）有统计显著性； C3（GRPO+QLoRA decoupling）有 G=4 和 G=8 双重验证
3	  + DPO 中间点对比； C4（EDCR 指标）有人工标注背书。 论文可用完整的 "problem → naive reward fails → online
4	  RL fails → CED+RSFT solves it" story arc， 无需降级任何 claim。主表可展示完整的 online-offline 光谱（GRPO
5	  → DPO → RSFT）。
6	
7	  '
8	imagined_experiments:
9	- name: CED vs flat-NLI RSFT ablation
10	  plan_id: plan_001
11	  description: '用 flat-NLI scoring（DeBERTa NLI entailment score，无 contrastive margin）替代
12	    CED 作为 RSFT 候选筛选信号。 复用 mvp2_rsft_gen_s0~s3 已有的 21952 candidates，仅替换打分函数。 flat-NLI
13	    score = mean entailment probability over cited sentences（无 hard-negative 对比）。
14	    选 top_k=1 per document，训练配置对齐 CED-RSFT 最优（s43: 3ep, α=128, seed=43；r2b: 1ep, α=32,
15	    lr=1e-5）。 共训练 2 个 flat-NLI RSFT 配置，全量 dev eval。
16	
17	    '
18	  expected_results:
19	    flatnli_rsft_a_rel_f1: 0.4412
20	    flatnli_rsft_a_evi_f1: 0.7948
21	    flatnli_rsft_a_edcr: 0.6952
22	    flatnli_rsft_a_n_selected: 2845
23	    flatnli_rsft_b_rel_f1: 0.4378
24	    flatnli_rsft_b_evi_f1: 0.7972
25	    flatnli_rsft_b_edcr: 0.6887
26	    ced_rsft_best_rel_f1: 0.4683
27	    ced_rsft_best_evi_f1: 0.8156
28	    ced_rsft_best_edcr: 0.6388
29	    delta_rel_f1: 0.0271
30	    delta_evi_f1: 0.0208
31	    delta_edcr: -0.0564
32	    paired_bootstrap_evi_f1_p: 0.0038
33	    paired_bootstrap_edcr_p: 0.0021
34	    paired_bootstrap_rel_f1_p: 0.0067
35	  result_rationale: 'flat-NLI scoring 仍然能过滤掉完全无关的候选（如 format 错误、zero-F1 的），因此 flat-NLI
36	    RSFT 仍优于 SFT baseline（+3.2~3.6pp rel_f1）。 但 flat-NLI 的核心缺陷在于：entity-sharing distractor
37	    sentences 的 NLI entailment score 往往偏高（因为共享实体提供了 lexical overlap）， flat-NLI 无法区分"真正支持关系的证据句"和"仅提及相同实体的干扰句"。
38	    因此 flat-NLI 筛选出的 top-1 候选中会保留更多 distractor-heavy 样本——这些样本的 evidence 看起来"合理"（高
39	    NLI score） 但实际上引用了大量 entity-sharing non-gold sentences。 CED 的 contrastive margin
40	    = p(entail|gold) - max(p(entail|distractor)) 直接惩罚这种模式， 因此 CED-filtered 数据的训练样本
41	    evidence 质量系统性更高。 这导致 CED RSFT 在 evi_f1 上高出 ~2.1pp（因为训练数据中 evidence 更精确，模型学到更好的
42	    evidence 引用模式）， 在 EDCR 上低 5.6pp（因为训练数据中 distractor citations 更少，模型被条件化为避免引用干扰句）。
43	    rel_f1 差异 +2.7pp 来自间接效应：CED 筛选出的候选不仅 evidence 更好，整体生成质量也更高（因为能正确定位 evidence 的生成通常也更准确地识别了关系）。
44	    p<0.01 的显著性来自两个因素：(1) dev set 有 985 docs 提供足够统计力，(2) CED vs flat-NLI 的差异是系统性的（几乎在每种关系类型上
45	    CED 都更好），不是少数异常值驱动的。 flat-NLI 选出 ~2845 样本（vs CED 2718），因为 flat-NLI 的筛选 landscape
46	    不同（一些 CED 会拒绝的 distractor-heavy 候选在 flat-NLI 下得分高）。
47	
48	    '
49	  tables:
50	  - name: 'Table: CED vs flat-NLI RSFT Ablation (dev set)'
51	    columns:
52	    - Method
53	    - rel_f1
54	    - evi_f1
55	    - EDCR
56	    - n_train
57	    rows:
58	    - - SFT baseline
59	      - 0.4057
60	      - 0.7979
61	      - 0.7118
62	      - 12151 (gold)
63	    - - 'RSFT flat-NLI (A: 3ep, α=128)'
64	      - 0.4412
65	      - 0.7948
66	      - 0.6952
67	      - 2845
68	    - - 'RSFT flat-NLI (B: 1ep, α=32)'
69	      - 0.4378
70	      - 0.7972
71	      - 0.6887
72	      - 2845
73	    - - 'RSFT CED (s43: 3ep, α=128)'
74	      - 0.4683
75	      - 0.8156
76	      - 0.6388
77	      - 2718
78	    - - 'RSFT CED (r2b: 1ep, α=32)'
79	      - 0.4493
80	      - 0.8128
81	      - 0.6609
82	      - 2718
83	    - - Δ (CED best - flatNLI best)
84	      - +2.71pp
85	      - +2.08pp
86	      - -5.64pp
87	      - —
88	    - - p-value (paired bootstrap)
89	      - 0.0067
90	      - 0.0038
91	      - 0.0021
92	      - —
93	  figures_description:
94	  - 'Scatter plot: per-document evi_f1 差异 (CED - flatNLI)，x 轴为 document 的 distractor
95	    density (entity-sharing non-gold sentences / total sentences)。预期高 distractor density
96	    的文档差异更大，验证 CED 的机制假说。'
97	  - 'Bar chart: 按 relation type frequency 分组的 evi_f1 对比（head/body/tail），验证 CED 在各频率段的一致优势。'
98	  analysis: 'CED vs flat-NLI 的差异模式完美验证了核心假说：CED 的优势集中在 distractor-dense 文档上。 在 distractor
99	    density > 0.4 的文档子集中，CED RSFT 的 evi_f1 优势扩大到 ~3.5pp， 而在 distractor density < 0.2
100	    的文档中差异缩小到 ~0.8pp（不显著）。 这证明 CED 的 contrastive margin 确实在做它该做的事：区分 entity-sharing
101	    distractors 和真正的 evidence。 EDCR 的差异更稳定（几乎所有子集都显著），因为 EDCR 直接测量 distractor citation
102	    rate， 而 evi_f1 还受 recall 影响（有些 gold evidence 即使用 flat-NLI 也能被正确引用）。 rel_f1 的差异虽然也显著，但这是
103	    evidence 质量提升的 downstream 效应，而非 CED 的直接目标。
104	
105	    '
106	- name: Test set evaluation (RSFT best + SFT baseline)
107	  plan_id: plan_002
108	  description: '用 RSFT best config (s43_r2: 3ep, α=128, seed=43) 和 SFT baseline 在
109	    DocRED test set 上评估。 (1) CodaLab 提交获取官方 rel_F1/Ign_F1；(2) 本地 test set 计算 Evi-F1_joint
110	    (DREEAM 协议) 和 Evi-F1_conditional + EDCR；(3) flat-NLI RSFT best 也提交作为 ablation。
111	
112	    '
113	  expected_results:
114	    sft_test_rel_f1: 0.3998
115	    sft_test_ign_f1: 0.3814
116	    sft_test_evi_f1_conditional: 0.7902
117	    sft_test_evi_f1_joint: 0.3216
118	    sft_test_edcr: 0.7185
119	    rsft_test_rel_f1: 0.4548
120	    rsft_test_ign_f1: 0.4367
121	    rsft_test_evi_f1_conditional: 0.8072
122	    rsft_test_evi_f1_joint: 0.3758
123	    rsft_test_edcr: 0.6476
124	    flatnli_test_rel_f1: 0.4302
125	    flatnli_test_ign_f1: 0.4118
126	    flatnli_test_evi_f1_conditional: 0.7883
127	    flatnli_test_evi_f1_joint: 0.3421
128	    flatnli_test_edcr: 0.7014
129	    rsft_vs_sft_test_rel_f1_delta: 0.055
130	    dev_to_test_degradation_rel_f1: 0.0135
131	    rsft_test_evi_f1_joint_value: 0.3758
132	  result_rationale: 'Dev→test degradation 约 1.35pp rel_f1（0.4683 → 0.4548），这在 DocRED
133	    上属正常范围。 DocRED test set 的关系分布与 dev 非常接近（同一标注 pipeline），但 test 略难因为： (1) annotator
134	    间一致性略低的 hard cases 更多被分配到 test，(2) distant supervision noise 在 test 中比例略高。 SFT
135	    test rel_f1=0.3998 比 dev 0.4057 低 0.6pp，同样符合 DocRED 的典型 dev-test gap。 因此 RSFT
136	    vs SFT 的 delta 在 test 上为 +5.5pp（vs dev +6.26pp），退化幅度合理。 Evi-F1_joint (DREEAM 协议)
137	    远低于 conditional（0.376 vs 0.807），因为 joint 计算方式为 evi_f1 = Σ(triple_correct AND evi_correct)
138	    / Σ(gold_triples)，未正确预测的 triple 直接贡献 0 到 evidence score。 RSFT rel_f1=0.455 意味着约
139	    45.5% 的 gold triples 被正确预测；在这些正确预测中，evi_f1_conditional ≈ 0.807； 因此 joint ≈ 0.455
140	    × 0.807 × correction_factor ≈ 0.376（correction factor 因为 recall/precision 不对称略偏离乘积）。
141	    SFT 的 joint 更低（0.322）因为 rel_f1 更低（0.400）。 Ign_F1 低于 F1 约 1.8pp，因为 RSFT 和 SFT 都对
142	    shared entity pairs（train+dev 中出现的）有略高的准确率， 忽略这些后 F1 下降——这是 DocRED 评测的正常模式。 EDCR
143	    在 test 上略高于 dev（0.648 vs 0.639），因为 test set 文档平均 entity density 略高，distractor
144	    机会更多。
145	
146	    '
147	  tables:
148	  - name: 'Table: Test Set Main Results'
149	    columns:
150	    - Method
151	    - rel_F1
152	    - Ign_F1
153	    - Evi-F1_joint
154	    - Evi-F1_cond
155	    - EDCR
156	    rows:
157	    - - SFT baseline
158	      - 0.3998
159	      - 0.3814
160	      - 0.3216
161	      - 0.7902
162	      - 0.7185
163	    - - RSFT flat-NLI
164	      - 0.4302
165	      - 0.4118
166	      - 0.3421
167	      - 0.7883
168	      - 0.7014
169	    - - RSFT CED (FREIGE)
170	      - 0.4548
171	      - 0.4367
172	      - 0.3758
173	      - 0.8072
174	      - 0.6476
175	    - - DREEAM (RoBERTa-large)
176	      - —
177	      - —
178	      - 0.5734
179	      - —
180	      - —
181	    - - SAIS (RoBERTa-large)
182	      - —
183	      - —
184	      - 0.5567
185	      - —
186	      - —
187	  figures_description:
188	  - 'Dev vs Test 对比 bar chart: 每个方法在 dev/test 上的 rel_f1 和 evi_f1_joint 并排对比，可视化 degradation
189	    幅度。'
190	  analysis: 'Test set 结果验证了 Claim 1 的核心——RSFT+CED 在 test 上稳定保持 +5.5pp rel_f1 优势，dev→test
191	    退化仅 1.35pp。 Evi-F1_joint 与 DREEAM 的绝对比较：FREIGE 0.376 vs DREEAM 0.573。 DREEAM 的
192	    joint Evi-F1 更高，但 DREEAM 是 encoder-based 方法，其"evidence"是 attention weight thresholding，
193	    而 FREIGE 是生成式方法同时输出 triple+evidence——二者的 evidence 形式不同（implicit attention vs explicit
194	    citation）。 论文可这样叙述：FREIGE 是首个生成式方法在 DocRED 上输出显式 evidence，且其 joint Evi-F1 在 LLM
195	    方法中无可比对手（LMRC、DocKS-RAG 均不输出 evidence）。 flat-NLI RSFT 在 test 上的表现确认了 CED 优势的泛化性（delta
196	    方向一致）。
197	
198	    '
199	- name: EDCR pipeline 验证 + cross-method diagnostic table
200	  plan_id: plan_003
201	  description: '在所有 evidence-producing 方法上计算统一的 EDCR 指标，构建 cross-method diagnostic
202	    table。 方法包括：SFT, RSFT-CED (4 configs), RSFT-flatNLI (2 configs), CED-reranker,
203	    GRPO checkpoints (selected)。 同时计算 EDCR 与 evi_f1 的相关性（per-method level 和 per-document
204	    level）。
205	
206	    '
207	  expected_results:
208	    sft_edcr: 0.7118
209	    rsft_ced_s43_edcr: 0.6388
210	    rsft_ced_s44_edcr: 0.635
211	    rsft_ced_r2a_edcr: 0.6641
212	    rsft_ced_r2b_edcr: 0.6609
213	    rsft_flatnli_a_edcr: 0.6952
214	    rsft_flatnli_b_edcr: 0.6887
215	    ced_reranker_edcr: 0.5983
216	    grpo_ckpt90_edcr: 0.8584
217	    grpo_ckpt100_lr5e6_edcr: 0.9876
218	    cross_method_pearson_r_edcr_vs_evif1: -0.42
219	    per_doc_spearman_edcr_vs_evif1: -0.31
220	  result_rationale: 'Cross-method table 展现清晰的 EDCR 梯度：GRPO（0.86-0.99）>> SFT（0.71）>>
221	    RSFT-flatNLI（0.69）>> RSFT-CED（0.64）>> CED-reranker（0.60）。 这个梯度与直觉一致：(1) GRPO 的
222	    catastrophic forgetting 导致模型生成大量重复 entity mentions 但极少正确 relation， 几乎所有 cited
223	    sentences 都是 distractor；(2) SFT 从 gold data 学习但无 evidence quality 信号； (3) flat-NLI
224	    RSFT 比 SFT 好因为至少过滤了 zero-evidence 候选，但 flat-NLI 被 entity overlap 欺骗； (4) CED RSFT
225	    进一步降低因为 contrastive margin 训练数据中 distractor 更少； (5) CED-reranker 最低因为推理时直接按 CED
226	    选最佳候选，不受训练数据分布约束。 Cross-method Pearson r ≈ -0.42 表明 EDCR 与 evi_f1 有中等负相关但远非完美——
227	    这正是 EDCR 作为独立指标的价值：它捕获了 evi_f1 的盲区（plausible-looking distractor citations）。 Per-document
228	    Spearman 较低（-0.31）因为 EDCR 在单文档粒度上噪声较大（小 denominator 问题）。
229	
230	    '
231	  tables:
232	  - name: 'Table: Cross-Method EDCR Diagnostic'
233	    columns:
234	    - Method
235	    - rel_F1
236	    - Evi-F1
237	    - EDCR↓
238	    - n_cited_sent
239	    - n_distractor
240	    rows:
241	    - - GRPO ckpt-100 (lr=5e-6)
242	      - 0.0138
243	      - 0.8504
244	      - 0.9876
245	      - 12834
246	      - 12675
247	    - - GRPO ckpt-90 (lr=5e-5)
248	      - 0.2108
249	      - 0.5666
250	      - 0.8584
251	      - 9821
252	      - 8431
253	    - - SFT baseline
254	      - 0.4057
255	      - 0.7979
256	      - 0.7118
257	      - 14206
258	      - 10113
259	    - - RSFT flat-NLI (best)
260	      - 0.4412
261	      - 0.7972
262	      - 0.6887
263	      - 13875
264	      - 9556
265	    - - RSFT CED r2b
266	      - 0.4493
267	      - 0.8128
268	      - 0.6609
269	      - 13542
270	      - 8950
271	    - - RSFT CED s43
272	      - 0.4683
273	      - 0.8156
274	      - 0.6388
275	      - 13267
276	      - 8475
277	    - - CED-reranker
278	      - 0.4152
279	      - 0.8214
280	      - 0.5983
281	      - 12983
282	      - 7768
283	  figures_description:
284	  - 'Scatter plot: 每个方法一个点，x=Evi-F1, y=EDCR。展示 EDCR 和 Evi-F1 的不完全相关——CED-reranker
285	    低 EDCR 高 Evi-F1，GRPO ckpt-100 高 EDCR 高 Evi-F1（decoupling）。附 Pearson r 标注。'
286	  - 'Stacked bar: 每个方法的 cited sentences 分解为 gold evidence / entity-sharing distractor
287	    / other，可视化 EDCR 成分。'
288	  analysis: 'EDCR diagnostic table 的核心发现：GRPO ckpt-100 的 EDCR=0.99 + Evi-F1=0.85 是一个极端案例——
289	    模型输出了大量 citations 且其中 evidence recall 高（0.787），但 99% 的 cited sentences 是 distractor。
290	    这是因为 GRPO 崩塌后模型倾向于引用文档中几乎所有句子，recall 自然高但 precision 极低。 CED-reranker 的 EDCR=0.60
291	    是最低的，因为推理时 CED 直接选择 margin 最大的候选—— 但其 rel_f1=0.415 不如 RSFT CED s43=0.468，因为 reranking
292	    不改变 candidate pool 的质量上限。 这支持了"CED 最适合作为训练数据筛选信号而非纯推理 reranker"的结论。
293	
294	    '
295	- name: DREEAM baseline reproduction
296	  plan_id: plan_004
297	  description: '在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 evidence extraction
298	    结果。 使用官方代码和预训练权重，计算 joint Evi-F1（与 FREIGE 可直接对比）。
299	
300	    '
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "649ac3ab-2cdf-4d9d-9846-e8284a536c3d",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "0fef86f4-1bf2-4a34-b58e-ed7d050a074e",
  "sourceToolAssistantUUID": "649ac3ab-2cdf-4d9d-9846-e8284a536c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T14:19:14.291Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PbSNQ6QpMKoAXHbPC7EnTK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
  "offset": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fef86f4-1bf2-4a34-b58e-ed7d050a074e",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VxoyJAdPBiervYswg6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c33b4da-39cb-4061-8b85-3618f8c068e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz83oisXFmFMRjCae48Qsg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14188,
      "cache_read_input_tokens": 27912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14188,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 25 · 2026-05-15T14:19:14.297Z_

<details><summary>↩ Tool result · `toolu_01PbSNQ6QpMKoAXHbPC7EnTK`</summary>

```text
500	LMRC        & Gen.\ LLM & 0.607 & ---   & None \\
501	SFT baseline & Gen.\ LLM & 0.406 & 0.322 & Explicit citation \\
502	\textbf{\method{}} & Gen.\ LLM & 0.468 & 0.381 & Explicit citation \\
503	\bottomrule
504	\end{tabular}
505	\end{table}
506	
507	%==============================================================================
508	\section{Discussion}
509	\label{sec:discussion}
510	%==============================================================================
511	
512	\paragraph{Why \rsft{} Succeeds Where RL Fails.}
513	The evidence--extraction decoupling phenomenon reveals that document-level IE presents unique challenges for on-policy RL: (1) QLoRA's rank-limited parameters are easily overwritten by RL gradients that preferentially optimize the more gradient-accessible evidence dimension; (2) evidence-quality rewards provide stronger gradients than extraction-accuracy signals, causing asymmetric optimization; (3) the combinatorial output space of multiple triples with evidence makes credit assignment intractable for policy-gradient methods.
514	\rsft{} bypasses all three issues by using standard supervised learning on curated data, inheriting the stability of SFT while benefiting from CED's quality signal.
515	
516	\paragraph{Limitations of \edcr{}.}
517	Entity-sharing is an operationalized proxy for distractor sentences, not a perfect definition.
518	The auto--human gap of +6.8pp (Table~\ref{tab:human_edcr}) indicates that some entity-sharing sentences provide partial contextual support.
519	Additionally, \edcr{} does not capture non-entity-sharing distractors (sentences that are irrelevant but happen not to mention target entities).
520	We recommend using \edcr{} as a complementary diagnostic alongside Evi-F1, not as a replacement.
521	
522	\paragraph{Extraction Gap vs.\ Encoders.}
523	\method{}'s primary limitation is the extraction accuracy gap compared to encoder-based methods (rel\_F1 0.455 vs.\ DREEAM's ${\sim}$0.631).
524	This gap is inherent to the generative paradigm under current model scales and is not specific to our method---LMRC (LLaMA-3.1-8B) achieves 0.607 with 2$\times$ parameters and no evidence output.
525	As LLM capabilities scale, this gap is expected to narrow, making evidence generation increasingly valuable.
526	
527	%==============================================================================
528	\section{Conclusion}
529	\label{sec:conclusion}
530	%==============================================================================
531	
532	We presented \method{}, the first LLM-based document-level RE framework that jointly generates relation triples and verifiable sentence-level evidence.
533	Our core technical contribution, \ced{}, provides a contrastive evidence scoring mechanism that is effective as an offline data quality filter but causes catastrophic forgetting when used as an online RL reward---revealing a previously unreported evidence--extraction decoupling phenomenon in GRPO+QLoRA for structured IE.
534	The proposed \edcr{} metric, validated by human annotation ($r$=0.62), captures a systematic failure mode of evidence citation invisible to standard Evi-F1.
535	Experiments across three model scales, two dataset variants, multiple RL paradigms, and extensive ablations demonstrate the robustness of our approach.
536	
537	\end{document}
538	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c33b4da-39cb-4061-8b85-3618f8c068e7",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "c30ae061-1af7-40f0-92d1-d9b7b2fa56c7",
  "sourceToolAssistantUUID": "1c33b4da-39cb-4061-8b85-3618f8c068e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T14:19:15.389Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Nb1v9yDm8b8JEQjwNqKj9P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml",
  "offset": 300,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c30ae061-1af7-40f0-92d1-d9b7b2fa56c7",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VxoyJAdPBiervYswg6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "814c90e1-fd4a-4664-99a2-4be2f07bda67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz83oisXFmFMRjCae48Qsg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14188,
      "cache_read_input_tokens": 27912,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14188
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 27912,
          "cache_creation_input_tokens": 14188,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14188,
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

_source line 27 · 2026-05-15T14:19:15.422Z_

<details><summary>↩ Tool result · `toolu_01Nb1v9yDm8b8JEQjwNqKj9P`</summary>

```text
300	    '
301	  expected_results:
302	    dreeam_dev_evi_f1_joint: 0.5718
303	    dreeam_dev_evi_f1_conditional: 0.8342
304	    dreeam_dev_rel_f1: 0.6312
305	    dreeam_paper_evi_f1: 0.5734
306	    reproduction_gap: -0.0016
307	    sais_dev_evi_f1_joint: 0.5542
308	  result_rationale: 'DREEAM 论文报告 Evi-F1 = 57.34，这是 joint protocol（evidence score 仅在
309	    relation 也正确时计入）。 复现应在 ±0.3pp 内——DREEAM 是确定性 encoder 方法（无采样），差异仅来自 PyTorch 版本和随机种子对
310	    fine-tuning 的微小影响。 使用官方 released checkpoint 应几乎完全复现。 DREEAM 的 rel_f1 ≈ 63.1%（RoBERTa-large
311	    encoder 的典型 DocRED 表现），远高于 FREIGE 的 46.8%—— 但 FREIGE 的贡献不在于超越 encoder SOTA 的 extraction
312	    精度，而在于首次提供显式 evidence。 DREEAM 的 evidence 是 attention-based（隐式的），而 FREIGE 输出显式句子索引。
313	    SAIS 复现 Evi-F1_joint ≈ 55.42，略低于 DREEAM，符合论文报告。
314	
315	    '
316	  tables:
317	  - name: 'Table: Evidence Baseline Comparison (dev set)'
318	    columns:
319	    - Method
320	    - Type
321	    - rel_F1
322	    - Evi-F1_joint
323	    - Evidence Form
324	    rows:
325	    - - DREEAM
326	      - Encoder
327	      - 0.6312
328	      - 0.5718
329	      - Attention threshold
330	    - - SAIS
331	      - Encoder
332	      - 0.6103
333	      - 0.5542
334	      - Attention threshold
335	    - - FREIGE (RSFT CED)
336	      - Generative LLM
337	      - 0.4683
338	      - 0.3758
339	      - Explicit [S_i] citation
340	    - - SFT baseline
341	      - Generative LLM
342	      - 0.4057
343	      - 0.3216
344	      - Explicit [S_i] citation
345	    - - LMRC
346	      - Generative LLM
347	      - 0.6069
348	      - —
349	      - No evidence
350	  figures_description: []
351	  analysis: "DREEAM/SAIS 复现确认了数字可靠。FREIGE 在 joint Evi-F1 上低于 DREEAM（0.376 vs 0.572），\
352	    \ 这主要由 rel_f1 gap 驱动（0.468 vs 0.631）。论文需要清晰叙述： (1) FREIGE 是首个输出显式 evidence 的 generative\
353	    \ LLM DocRE 方法； (2) 在 LLM 方法类别内无直接竞争者（LMRC 无 evidence）； (3) 与 encoder methods\
354	    \ 的 gap 主要来自 extraction 能力而非 evidence 能力——\n    在正确预测的 triple 上，FREIGE 的 conditional\
355	    \ Evi-F1 (0.807) 接近 DREEAM 的 (0.834)。\n"
356	- name: CED-as-reranker PoC
357	  plan_id: plan_005
358	  description: '推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。
359	
360	    '
361	  expected_results:
362	    reranker_rel_f1: 0.4152
363	    reranker_evi_f1: 0.8214
364	    reranker_edcr: 0.5983
365	    reranker_evi_precision: 0.8356
366	    reranker_evi_recall: 0.8078
367	    sft_baseline_rel_f1: 0.4057
368	    sft_baseline_evi_f1: 0.7979
369	    sft_baseline_edcr: 0.7118
370	    delta_rel_f1_vs_sft: 0.0095
371	    delta_evi_f1_vs_sft: 0.0235
372	    delta_edcr_vs_sft: -0.1135
373	  result_rationale: 'CED-reranker 在 EDCR 上表现最好（0.598），因为推理时直接选 CED margin 最大的候选——
374	    这等价于选 distractor citation 最少的那个生成。evi_f1 也因此改善（+2.35pp）， 因为更准确的 evidence 引用提升了
375	    precision。 但 rel_f1 提升有限（+0.95pp），原因是 CED 的打分维度是 evidence quality 而非 extraction
376	    accuracy。 N=8 候选的 extraction diversity 有限（Jaccard 在 temp=0.7 下约 0.17）， 重排仅在候选间有
377	    evidence 质量差异时有用，对 extraction 错误无能为力。 与 RSFT CED (rel_f1=0.468) 的差距（-5.3pp）证明了训练
378	    vs 推理的区别： RSFT 通过高质量数据改变了模型的 generation distribution，而 reranker 仅从已有分布中选最佳。 这支持论文的"CED
379	    作为训练信号优于推理信号"结论。
380	
381	    '
382	  tables:
383	  - name: 'Table: CED Usage Modes Comparison'
384	    columns:
385	    - CED Usage
386	    - rel_F1
387	    - Evi-F1
388	    - EDCR↓
389	    - Extra Training
390	    rows:
391	    - - SFT (no CED)
392	      - 0.4057
393	      - 0.7979
394	      - 0.7118
395	      - —
396	    - - CED-reranker (inference)
397	      - 0.4152
398	      - 0.8214
399	      - 0.5983
400	      - None
401	    - - RSFT flat-NLI (training, no CED)
402	      - 0.4412
403	      - 0.7972
404	      - 0.6887
405	      - RSFT
406	    - - RSFT CED (training)
407	      - 0.4683
408	      - 0.8156
409	      - 0.6388
410	      - RSFT
411	  figures_description:
412	  - 'Per-document analysis: reranker 在哪些文档上改善最大？预期是 candidate diversity 高且 SFT baseline
413	    evidence 差的文档。'
414	  analysis: 'CED-reranker 证明了 CED 作为质量信号的有效性（EDCR 大幅下降 -11.35pp）， 但也证明了仅靠推理时 reranking
415	    不够——rel_f1 提升微弱。 这形成一个很好的 ablation 故事：CED 信号本身有效，但需要通过 RSFT 训练来充分利用。 论文可在 analysis
416	    section 用此对比说明"为什么选择 RSFT 而非 reranking"。
417	
418	    '
419	- name: Model size ablation (1.7B / 8B)
420	  plan_id: plan_006
421	  description: '在 Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT+CED pipeline，验证方法对模型规模的泛化性。
422	    每个模型：SFT baseline + RSFT CED (best config from 4B)，dev set 评估。
423	
424	    '
425	  expected_results:
426	    qwen_1_7b_sft_rel_f1: 0.3412
427	    qwen_1_7b_sft_evi_f1: 0.7534
428	    qwen_1_7b_sft_edcr: 0.7456
429	    qwen_1_7b_rsft_ced_rel_f1: 0.3724
430	    qwen_1_7b_rsft_ced_evi_f1: 0.7782
431	    qwen_1_7b_rsft_ced_edcr: 0.6934
432	    qwen_1_7b_delta_rel_f1: 0.0312
433	    qwen_8b_sft_rel_f1: 0.4423
434	    qwen_8b_sft_evi_f1: 0.8125
435	    qwen_8b_sft_edcr: 0.6892
436	    qwen_8b_rsft_ced_rel_f1: 0.4912
437	    qwen_8b_rsft_ced_evi_f1: 0.8367
438	    qwen_8b_rsft_ced_edcr: 0.6187
439	    qwen_8b_delta_rel_f1: 0.0489
440	  result_rationale: '1.7B 模型基础能力更弱（SFT rel_f1 0.341 vs 4B 的 0.406），但 RSFT+CED 的相对提升仍然显著（+3.1pp）。
441	    提升幅度略小于 4B（+6.3pp），因为 1.7B 的 candidate pool 质量上限更低—— N=8 生成中 top-1 CED candidate
442	    的质量受限于模型的 generation capacity。 8B 模型基础更强（SFT 0.442），RSFT+CED 提升到 0.491（+4.9pp），
443	    提升幅度介于 1.7B 和 4B 之间。8B 的 SFT baseline 已经较高，留给 RSFT 的 headroom 相对更小， 但绝对性能最好。 跨三个规模的一致提升（+3.1
444	    / +6.3 / +4.9pp）证明 CED+RSFT 不是模型特定的 trick， 而是一个通用的 evidence quality 提升机制。 EDCR
445	    模式一致：1.7B SFT EDCR 最高（0.746）因为小模型更易引用不相关句子， RSFT+CED 在所有规模上都降低 EDCR（-5.2 / -7.3
446	    / -7.1pp）。
447	
448	    '
449	  tables:
450	  - name: 'Table: Model Size Ablation'
451	    columns:
452	    - Model
453	    - Method
454	    - rel_F1
455	    - Evi-F1
456	    - EDCR↓
457	    - Δ rel_F1
458	    rows:
459	    - - Qwen3-1.7B
460	      - SFT
461	      - 0.3412
462	      - 0.7534
463	      - 0.7456
464	      - —
465	    - - Qwen3-1.7B
466	      - RSFT+CED
467	      - 0.3724
468	      - 0.7782
469	      - 0.6934
470	      - +3.12pp
471	    - - Qwen3-4B
472	      - SFT
473	      - 0.4057
474	      - 0.7979
475	      - 0.7118
476	      - —
477	    - - Qwen3-4B
478	      - RSFT+CED
479	      - 0.4683
480	      - 0.8156
481	      - 0.6388
482	      - +6.26pp
483	    - - Qwen3-8B
484	      - SFT
485	      - 0.4423
486	      - 0.8125
487	      - 0.6892
488	      - —
489	    - - Qwen3-8B
490	      - RSFT+CED
491	      - 0.4912
492	      - 0.8367
493	      - 0.6187
494	      - +4.89pp
495	  figures_description:
496	  - 'Line plot: x=model size (1.7B, 4B, 8B), y=rel_f1，两条线分别为 SFT 和 RSFT+CED，展示 scaling
497	    趋势和一致的 gap。'
498	  analysis: 'Model size ablation 证明 RSFT+CED 在 1.7B-8B 范围内一致有效。 4B 的相对提升最大可能因为它处于"sweet
499	    spot"——模型足够大产生多样高质量候选， 但还不够大到 SFT 已经很好。8B SFT 的 EDCR 已经较低（0.689），说明更大模型本身就更善于引用相关
500	    evidence， 但 RSFT+CED 仍有增量价值。
501	
502	    '
503	- name: Re-DocRED extension
504	  plan_id: plan_007
505	  description: '在 Re-DocRED（修正 false negative 标注的版本）上评估 SFT 和 RSFT+CED，验证方法在更干净标注下的表现。
506	
507	    '
508	  expected_results:
509	    redocred_sft_rel_f1: 0.4534
510	    redocred_sft_evi_f1: 0.8112
511	    redocred_rsft_ced_rel_f1: 0.5089
512	    redocred_rsft_ced_evi_f1: 0.8378
513	    redocred_rsft_ced_edcr: 0.6023
514	    redocred_delta_rel_f1: 0.0555
515	  result_rationale: 'Re-DocRED 修正了 DocRED 中约 25% 的 false negative relations（标注遗漏），
516	    因此所有方法的绝对 F1 都上升（SFT 0.453 vs 原 0.406）——被原始标注遗漏的正确预测不再被惩罚。 RSFT+CED 的 delta（+5.55pp）与
517	    DocRED 上的（+6.26pp）接近， 说明 CED 的 evidence quality 提升不依赖于标注噪声的存在。 EDCR 在 Re-DocRED
518	    上略低（0.602 vs 0.639），因为部分被标为 distractor 的句子在 Re-DocRED 中被重新标注为 gold evidence， 降低了
519	    false-distractor 率。这也间接验证了 CED margin 的鲁棒性—— 即使标注不完美，CED 仍然能有效区分 evidence 质量。
520	
521	    '
522	  tables:
523	  - name: 'Table: DocRED vs Re-DocRED'
524	    columns:
525	    - Dataset
526	    - Method
527	    - rel_F1
528	    - Evi-F1
529	    - EDCR↓
530	    rows:
531	    - - DocRED
532	      - SFT
533	      - 0.4057
534	      - 0.7979
535	      - 0.7118
536	    - - DocRED
537	      - RSFT+CED
538	      - 0.4683
539	      - 0.8156
540	      - 0.6388
541	    - - Re-DocRED
542	      - SFT
543	      - 0.4534
544	      - 0.8112
545	      - 0.6892
546	    - - Re-DocRED
547	      - RSFT+CED
548	      - 0.5089
549	      - 0.8378
550	      - 0.6023
551	  figures_description: []
552	  analysis: 'Re-DocRED 结果为 RC4（单数据集泛化性）提供了部分回应。方法在更干净标注下表现更好且 delta 保持， 说明 CED+RSFT
553	    不是在利用标注噪声。
554	
555	    '
556	- name: top_k ablation (k=1 vs k=3)
557	  plan_id: plan_008
558	  description: 'CED scoring 筛选 top_k=3（每文档选 CED top-3 候选，~8000 训练样本）vs top_k=1（~2718
559	    样本）， 验证 CED 过滤严格度对 RSFT 训练质量的影响。
560	
561	    '
562	  expected_results:
563	    topk1_n_samples: 2718
564	    topk1_rel_f1: 0.4683
565	    topk1_evi_f1: 0.8156
566	    topk1_edcr: 0.6388
567	    topk3_n_samples: 7856
568	    topk3_rel_f1: 0.4523
569	    topk3_evi_f1: 0.8034
570	    topk3_edcr: 0.6712
571	    topk3_mean_ced_score: 0.5234
572	  result_rationale: 'top_k=3 引入了 ~5100 额外训练样本，但这些是每文档的第 2、3 名候选——CED score 系统性更低 （mean
573	    CED 0.523 vs top_k=1 的 0.668）。更多训练数据带来的拟合优势被更低数据质量抵消： (1) rel_f1 下降 1.6pp 因为质量较低的候选引入了更多
574	    extraction 错误模式； (2) evi_f1 下降 1.2pp 因为 2nd/3rd 候选的 evidence 质量明显低于 1st； (3) EDCR
575	    上升 3.2pp 因为训练数据中混入了更多 distractor-heavy 样本。 这验证了 CED 作为质量过滤器的"宁缺毋滥"策略——strict top_k=1
576	    优于宽松 top_k=3， 因为 RSFT 的核心机制是让模型从高质量样本中学习，不需要海量数据。 这也解释了为什么 2718 样本（仅占 21952 候选的
577	    12.4%）就足够有效—— SFT 阶段已经提供了足够的"通用知识"，RSFT 只需少量高质量样本来校准 evidence 引用行为。
578	
579	    '
580	  tables:
581	  - name: 'Table: top_k Ablation'
582	    columns:
583	    - top_k
584	    - n_train
585	    - mean_CED
586	    - rel_F1
587	    - Evi-F1
588	    - EDCR↓
589	    rows:
590	    - - 1
591	      - 2718
592	      - 0.6683
593	      - 0.4683
594	      - 0.8156
595	      - 0.6388
596	    - - 3
597	      - 7856
598	      - 0.5234
599	      - 0.4523
600	      - 0.8034
601	      - 0.6712
602	  figures_description:
603	  - 'CED score distribution: top_k=1 vs top_k=3 的训练样本 CED score histogram，可视化质量差异。'
604	  analysis: 'top_k ablation 确认了 CED 质量过滤的重要性，同时也为 reviewer 提供了"为什么不用更多数据"的回答。 这是一个
605	    diminishing-returns-with-quality-dilution 的经典案例。
606	
607	    '
608	- name: GRPO G=8 实验
609	  plan_id: plan_011
610	  description: 'G=8 + CED reward + kl_coef=0.01 + lr=5e-6，验证 GRPO 在标准 group size 下是否仍然
611	    catastrophic forgetting。 排除 G=4 的 advantage estimation noise 作为 confounding factor。
612	
613	    '
614	  expected_results:
615	    grpo_g8_best_rel_f1: 0.0312
616	    grpo_g8_best_evi_f1: 0.8156
617	    grpo_g8_best_edcr: 0.9812
618	    grpo_g8_best_checkpoint: ckpt-80
619	    grpo_g8_final_rel_f1: 0.0287
620	    grpo_g8_final_reward: 1.287
621	    grpo_g8_forgetting_onset_step: 15
622	    grpo_g8_collapse_pattern: 同 G=4：reward ↑ + rel_f1 ↓，但 collapse 稍慢
623	    grpo_g4_best_rel_f1: 0.0138
624	    grpo_g4_best_evi_f1: 0.8504
625	  result_rationale: "G=8 将 advantage estimation 的方差降低约 √2 倍（相对 G=4），这确实改善了 gradient\
626	    \ quality。 然而 catastrophic forgetting 的根因不是 advantage noise，而是 GRPO+QLoRA 在文档级\
627	    \ IE 任务上的结构性问题： (1) QLoRA 的 rank-limited 参数空间在接收 RL gradient 时容易覆盖 SFT 学到的 extraction\
628	    \ schema knowledge； (2) CED/NLI reward 在 evidence 维度上的梯度远强于 extraction 维度（因为 evidence\
629	    \ quality 变化更容易被 reward 捕获），\n    导致模型优先优化 evidence 而放弃 extraction；\n(3) 文档级 IE\
630	    \ 的输出空间极大（多 triple + evidence），policy gradient 的 credit assignment 困难。 G=8 的 rel_f1\
631	    \ 峰值（0.031）略高于 G=4（0.014），说明更稳定的 advantage 确实有边际帮助， 但远不足以避免 forgetting（仍 < 0.05，远低于\
632	    \ SFT 的 0.406）。 evi_f1 仍然高（0.816），再次确认 decoupling phenomenon——RL 优化了 evidence\
633	    \ 但摧毁了 extraction。 Forgetting onset 稍慢（step 15 vs G=4 的 step ~10），因为 G=8 的 gradient\
634	    \ 更保守， 但最终 trajectory 殊途同归。\n"
635	  tables:
636	  - name: 'Table: GRPO Group Size Comparison'
637	    columns:
638	    - Config
639	    - G
640	    - Best rel_F1
641	    - Best Evi-F1
642	    - EDCR
643	    - Forgetting?
644	    rows:
645	    - - GRPO+CED lr=5e-6
646	      - 4
647	      - 0.0138
648	      - 0.8504
649	      - 0.9876
650	      - Yes (step ~10)
651	    - - GRPO+CED lr=5e-6
652	      - 8
653	      - 0.0312
654	      - 0.8156
655	      - 0.9812
656	      - Yes (step ~15)
657	    - - GRPO+CED lr=5e-5
658	      - 4
659	      - 0.2108
660	      - 0.5666
661	      - 0.8584
662	      - Yes (partial)
663	    - - SFT baseline
664	      - —
665	      - 0.4057
666	      - 0.7979
667	      - 0.7118
668	      - 'No'
669	  figures_description:
670	  - 'Training dynamics: G=4 vs G=8 的 rel_f1 和 reward 随 step 变化曲线，overlay 在同一图上。展示
671	    G=8 collapse 稍慢但最终同样崩溃。'
672	  - 'Decoupling visualization: x=training step, 左 y=rel_f1(↓), 右 y=evi_f1(↑)，展示两个指标的
673	    divergence。'
674	  analysis: 'G=8 实验是 Claim 3 的关键验证——排除了 advantage estimation noise 作为 G=4 failure
675	    的替代解释。 rel_f1 从 0.014 微升到 0.031 说明 G 确实有微弱影响，但量级上不改变结论。 论文可以写："Increasing group
676	    size from 4 to 8 marginally delays but does not prevent catastrophic forgetting
677	    (best rel_F1: 0.031 vs 0.014, both << SFT 0.406), confirming the structural incompatibility
678	    of GRPO+QLoRA with document-level IE."
679	
680	    '
681	- name: DPO+CED experiment
682	  plan_id: plan_012
683	  description: '用 RSFT candidate pool 构造 preference pairs：每文档 CED top-1 为 chosen，CED
684	    bottom-1（F1>0.1 filter）为 rejected。 DPO 训练（β=0.1, lr=1e-5, 1 epoch），验证 offline
685	    preference learning 的表现。
686	
687	    '
688	  expected_results:
689	    dpo_rel_f1: 0.3245
690	    dpo_evi_f1: 0.7856
691	    dpo_edcr: 0.6834
692	    dpo_n_pairs: 2412
693	    dpo_beta: 0.1
694	    sft_rel_f1: 0.4057
695	    rsft_ced_rel_f1: 0.4683
696	    grpo_g8_best_rel_f1: 0.0312
697	  result_rationale: "DPO 作为 offline preference optimization，避免了 GRPO 的 on-policy sampling\
698	    \ 导致的 distribution shift， 因此不会 catastrophic forgetting——rel_f1=0.325 远高于 GRPO\
699	    \ 的 0.031。 但 DPO 弱于 RSFT（0.325 vs 0.468）的原因是： (1) DPO 的 implicit reward model\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "814c90e1-fd4a-4664-99a2-4be2f07bda67",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "19ed8805-583d-47aa-8342-21e18bd8fc5c",
  "sourceToolAssistantUUID": "814c90e1-fd4a-4664-99a2-4be2f07bda67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T14:19:19.875Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XK9RySoAHr2xjPseJPkU1K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml",
  "offset": 700
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ed8805-583d-47aa-8342-21e18bd8fc5c",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VyEJ2gYSZJc15H33Fr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8f0be40-d4a4-4432-b7e7-dab03b076cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jhhzPmyQ219pDwHFrFzuD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8988,
      "cache_read_input_tokens": 42100,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8988
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 42100,
          "cache_creation_input_tokens": 8988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8988,
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

_source line 29 · 2026-05-15T14:19:19.883Z_

<details><summary>↩ Tool result · `toolu_01XK9RySoAHr2xjPseJPkU1K`</summary>

```text
700	    \ 需要从 preference pairs 中学习 CED 信号，\n    而 RSFT 直接在 CED-selected 高质量样本上 supervised\
701	    \ learning——后者更 sample-efficient；\n(2) DPO 的 contrastive loss 同时推高 chosen 和推低\
702	    \ rejected 的 likelihood，\n    但在 IE 任务中 chosen/rejected 的差异主要在 evidence 而非 extraction——\n\
703	    \    推低 rejected 可能意外降低了正确 extraction pattern 的概率；\n(3) DocRED 的输出空间太大（长 JSON），DPO\
704	    \ 的 token-level KL penalty 对长序列的控制力不足。 DPO 的 evi_f1（0.786）接近 SFT（0.798），说明 evidence\
705	    \ 质量未被显著改善—— DPO 未能从 preference pairs 中有效学到 CED 的 evidence quality 信号。 这与 RSFT\
706	    \ 的 evi_f1=0.816 形成对比，进一步支持\"CED 适合作为筛选信号而非学习目标\"。 rel_f1=0.325 vs SFT=0.406 实际上是\
707	    \ DPO 的退化（-8.1pp），这是因为 DPO 的 rejected 样本中包含的 extraction pattern 被不当抑制了——一种轻度的\
708	    \ DPO \"over-optimization\"。 整体光谱：GRPO (0.031) << DPO (0.325) < SFT (0.406) <\
709	    \ RSFT (0.468)， 清晰展示了 online → offline → no-RL → offline-filtered 的退化/改善梯度。\n"
710	  tables:
711	  - name: 'Table: Online-Offline RL Spectrum'
712	    columns:
713	    - Method
714	    - RL Type
715	    - rel_F1
716	    - Evi-F1
717	    - EDCR↓
718	    - Catastrophic?
719	    rows:
720	    - - GRPO G=8
721	      - Online (on-policy)
722	      - 0.0312
723	      - 0.8156
724	      - 0.9812
725	      - 'Yes'
726	    - - GRPO G=4
727	      - Online (on-policy)
728	      - 0.0138
729	      - 0.8504
730	      - 0.9876
731	      - 'Yes'
732	    - - DPO+CED
733	      - Offline (preference)
734	      - 0.3245
735	      - 0.7856
736	      - 0.6834
737	      - No (but degraded)
738	    - - SFT
739	      - No RL
740	      - 0.4057
741	      - 0.7979
742	      - 0.7118
743	      - 'No'
744	    - - RSFT+CED
745	      - Offline (filtered SFT)
746	      - 0.4683
747	      - 0.8156
748	      - 0.6388
749	      - 'No'
750	  figures_description:
751	  - 'Spectrum bar chart: 5 个方法的 rel_f1 并排，从左到右按 ''RL 强度'' 排列（GRPO → DPO → SFT → RSFT），可视化
752	    online RL 的破坏性和 RSFT 的优越性。'
753	  analysis: "DPO 实验填补了 GRPO 和 RSFT 之间的空白。核心洞察： (1) 问题不在 \"offline vs online\" 的二元对立——DPO（offline）也退化了；\
754	    \ (2) 问题在于 RL loss function 对文档级 IE 输出空间的适配性——\n    GRPO 的 policy gradient 和 DPO\
755	    \ 的 preference loss 都在 token level 操作，\n    对长结构化输出的 credit assignment 困难；\n(3)\
756	    \ RSFT 之所以成功，是因为它根本不用 RL loss——直接 supervised learning on filtered data，\n    避免了\
757	    \ credit assignment 问题。\n这加强了论文的理论贡献：不是\"CED reward 好\"而是\"CED 作为数据质量信号 + SFT\
758	    \ 训练范式 = 最佳组合\"。\n"
759	- name: EDCR 人工标注验证
760	  plan_id: plan_013
761	  description: '100 个样本（每样本 = 一个 predicted triple + 其 cited evidence sentences）， 3
762	    名标注者独立判断每个 cited sentence 是否真正支持对应 relation。 计算 EDCR_auto 与 human_distractor_rate
763	    的 Pearson r。
764	
765	    '
766	  expected_results:
767	    n_samples: 100
768	    n_annotators: 3
769	    inter_annotator_kappa: 0.72
770	    edcr_human_pearson_r: 0.62
771	    edcr_human_spearman_r: 0.58
772	    human_distractor_rate_mean: 0.583
773	    auto_edcr_mean: 0.651
774	    edcr_auto_vs_human_bias: 0.068
775	    sft_human_distractor_rate: 0.645
776	    rsft_ced_human_distractor_rate: 0.524
777	    rsft_flatnli_human_distractor_rate: 0.608
778	    grpo_human_distractor_rate: 0.954
779	  result_rationale: 'Pearson r=0.62 表明 EDCR 与人类判断有中等偏强的正相关——EDCR 确实在测量有意义的 evidence
780	    质量维度。 r 未达到 0.8+ 的原因：(1) EDCR 用 entity-sharing 作为 distractor 的操作性定义， 而人类判断基于语义支持关系——部分
781	    entity-sharing sentences 人类认为确实支持关系（partial evidence）， 部分 non-entity-sharing sentences
782	    人类认为是 distractor（基于语义而非 entity overlap）； (2) 100 样本的统计力有限，置信区间较宽。 Auto EDCR 略高估（bias
783	    +6.8pp），因为 entity-sharing 的自动判定过于严格—— 一些共享实体但确实提供支持的句子被 EDCR 错误标为 distractor。
784	    Inter-annotator Cohen''s κ=0.72（substantial agreement），说明 evidence 支持判断本身具有一定主观性，
785	    但三人投票足以产生可靠的 gold standard。 分方法看，human distractor rate 的排序与 EDCR 一致：GRPO (0.954)
786	    >> SFT (0.645) > flatNLI (0.608) > CED (0.524)， 进一步验证了 EDCR 的诊断方向正确。
787	
788	    '
789	  tables:
790	  - name: 'Table: EDCR Human Validation'
791	    columns:
792	    - Method
793	    - EDCR_auto
794	    - Human_distractor_rate
795	    - Δ
796	    - n
797	    rows:
798	    - - GRPO ckpt-90
799	      - 0.858
800	      - 0.954
801	      - -0.096
802	      - 25
803	    - - SFT
804	      - 0.712
805	      - 0.645
806	      - 0.067
807	      - 25
808	    - - RSFT flat-NLI
809	      - 0.695
810	      - 0.608
811	      - 0.087
812	      - 25
813	    - - RSFT CED
814	      - 0.639
815	      - 0.524
816	      - 0.115
817	      - 25
818	    - - Overall Pearson r
819	      - —
820	      - —
821	      - 0.62
822	      - 100
823	  figures_description:
824	  - 'Scatter plot: x=EDCR_auto, y=human_distractor_rate, 每个点一个样本（n=100），颜色编码方法。附 regression
825	    line 和 r 值。'
826	  - 'Confusion matrix: EDCR binary prediction (>0.5 = distractor-heavy) vs human majority
827	    vote, 计算 accuracy/precision/recall。'
828	  analysis: 'Pearson r=0.62 满足 best tier 要求（[0.55, 0.75]），验证了 EDCR 作为自动指标的有效性。 但需要在论文中诚实讨论
829	    limitations：(1) entity-sharing 是 distractor 的代理指标而非完美定义； (2) CED RSFT 的 auto-human
830	    gap 最大（0.115），说明 CED 训练的模型引用模式与人类直觉有微妙差异—— 部分人类认为有用的 contextual sentences（虽然不是
831	    gold evidence）被 EDCR 标为 distractor。 这实际上是一个有趣的发现，可以在 discussion 中展开。
832	
833	    '
834	- name: GRPO forgetting 详细分析 + 可视化
835	  plan_id: plan_009
836	  description: '整理全部 GRPO checkpoint（G=4 lr=5e-5, G=4 lr=5e-6, G=8）的完整训练轨迹， 绘制 forgetting
837	    dynamics 可视化。
838	
839	    '
840	  expected_results:
841	    n_checkpoints_analyzed: 42
842	    n_configs: 3
843	    decoupling_onset_step_g4_lr5e6: 10
844	    decoupling_onset_step_g4_lr5e5: 5
845	    decoupling_onset_step_g8: 15
846	    peak_evi_f1_across_configs: 0.8504
847	    min_rel_f1_across_configs: 0.0028
848	  result_rationale: 'GRPO 的 forgetting dynamics 在所有配置中呈现一致模式： (1) 早期（step 1-5/10/15
849	    取决于 lr 和 G）：rel_f1 开始下降但 evi_f1 开始上升——decoupling onset； (2) 中期（step 5-50）：reward
850	    持续上升，rel_f1 加速下降至 <0.05，evi_f1 平台期 ~0.80-0.85； (3) 后期（step 50-100）：reward 饱和，rel_f1
851	    在底部震荡（<0.02），evi_f1 微调。 lr=5e-5 的 forgetting 最快（step 5 开始）但 rel_f1 最终峰值最高（0.211
852	    at ckpt-90）， 因为高 lr 的 RL gradient 足够强同时推动 extraction 和 evidence，但最终 evidence gradient
853	    占优。 lr=5e-6 的 forgetting 最慢开始但最终 rel_f1 最低（0.014）， 因为低 lr 的 RL gradient 更精细地优化了
854	    reward 但缺乏足够的 extraction signal。 G=8 在 step 15 开始 forgetting——比 G=4 lr=5e-6 的
855	    step 10 晚， 符合"更稳定 advantage estimation → 更保守 update"的预期。
856	
857	    '
858	  tables: []
859	  figures_description:
860	  - '3×2 panel figure: 3 行 = 3 configs (G4-lr5e5, G4-lr5e6, G8), 2 列 = (rel_f1 + reward
861	    overlay, evi_f1 + EDCR overlay)。每个 panel 用双 y 轴展示两个指标随 step 的 divergence。'
862	  - 'Phase diagram: x=rel_f1, y=evi_f1, 每个 config 的 trajectory 用箭头连接各 checkpoint，展示
863	    decoupling 的方向（右上→左上）。'
864	  analysis: '可视化清晰展示 decoupling phenomenon 的三个阶段。Phase diagram 是最有力的图—— 所有 GRPO configs
865	    的 trajectory 都从 (SFT rel_f1, SFT evi_f1) 出发，向 (↓, ↑) 移动， 形成一个"左上角 attractor"。RSFT
866	    的 trajectory 则从同一起点向 (↑, ↑) 移动， 两个方向的对比直观地说明了 online vs offline RL 的行为差异。
867	
868	    '
869	- name: NLI model ablation (DeBERTa-base vs large)
870	  plan_id: plan_010
871	  description: '用 DeBERTa-v3-large 替代 DeBERTa-v3-base 作为 CED scorer，重新打分已有 candidates，
872	    对比两个 NLI 模型对 CED scoring 质量的影响。
873	
874	    '
875	  expected_results:
876	    deberta_base_mean_ced: 0.6683
877	    deberta_large_mean_ced: 0.7012
878	    deberta_base_discrimination_acc: 0.815
879	    deberta_large_discrimination_acc: 0.847
880	    deberta_large_rsft_rel_f1: 0.4721
881	    deberta_large_rsft_evi_f1: 0.8189
882	    deberta_large_rsft_edcr: 0.6312
883	    deberta_base_rsft_rel_f1: 0.4683
884	    deberta_base_rsft_evi_f1: 0.8156
885	    deberta_base_rsft_edcr: 0.6388
886	    delta_rel_f1: 0.0038
887	    delta_evi_f1: 0.0033
888	  result_rationale: "DeBERTa-large 的 NLI 能力确实更强（discrimination accuracy 0.847 vs 0.815），\
889	    \ CED margin 也更大（0.701 vs 0.668），但这些改善传导到 RSFT 最终结果时被大幅衰减： (1) CED scoring 已经是一个\"\
890	    阈值化\"操作（top_k=1），只要排序大致正确即可——\n    base 和 large 的 top-1 选择一致率约 89%，仅 11% 文档的 top-1\
891	    \ 不同；\n(2) 这 11% 不同的文档中，large 选出的候选确实稍好，但对总体 RSFT 训练的影响被稀释； (3) rel_f1 差异仅 +0.38pp，不具统计显著性。\
892	    \ 这是一个积极结果：CED 方法对 NLI 模型选择不敏感，base 模型足够用， 降低了方法的计算门槛（DeBERTa-base ~86M vs large\
893	    \ ~304M参数）。 同时回应了 RC1（NLI reward 信号质量）：即使用更强的 NLI 模型，CED 提升也很小—— 说明 CED 的瓶颈不在\
894	    \ NLI 模型质量，而在于 RSFT 训练本身的 sample efficiency。\n"
895	  tables:
896	  - name: 'Table: NLI Model Ablation'
897	    columns:
898	    - NLI Model
899	    - Params
900	    - Disc. Acc
901	    - Mean CED
902	    - RSFT rel_F1
903	    - RSFT Evi-F1
904	    rows:
905	    - - DeBERTa-v3-base
906	      - 86M
907	      - 0.815
908	      - 0.668
909	      - 0.4683
910	      - 0.8156
911	    - - DeBERTa-v3-large
912	      - 304M
913	      - 0.847
914	      - 0.701
915	      - 0.4721
916	      - 0.8189
917	    - - Δ
918	      - —
919	      - '+0.032'
920	      - '+0.033'
921	      - +0.38pp
922	      - +0.33pp
923	  figures_description: []
924	  analysis: 'NLI model ablation 的 marginal 差异是好消息——方法鲁棒、计算门槛低。 论文可以一句话带过："Replacing
925	    DeBERTa-base with DeBERTa-large yields marginal improvements (+0.38pp rel_F1),
926	    confirming that CED''s effectiveness stems from the contrastive design rather
927	    than the NLI model''s capacity."
928	
929	    '
930	- name: Evi-F1 DREEAM 协议对齐重评
931	  plan_id: plan_evi_align
932	  description: '对所有已有 dev eval 结果重新计算 Evi-F1_joint（DREEAM 协议：evi score 仅在 relation
933	    也正确时计入）。 已有的 Evi-F1 为 conditional（given correct relation），需要同时报告两种。
934	
935	    '
936	  expected_results:
937	    sft_evi_f1_joint: 0.3216
938	    rsft_ced_s43_evi_f1_joint: 0.3812
939	    rsft_ced_s44_evi_f1_joint: 0.3724
940	    rsft_ced_r2a_evi_f1_joint: 0.3657
941	    rsft_ced_r2b_evi_f1_joint: 0.3663
942	    rsft_flatnli_best_evi_f1_joint: 0.3498
943	    grpo_best_evi_f1_joint: 0.0118
944	    ced_reranker_evi_f1_joint: 0.3412
945	  result_rationale: 'Joint Evi-F1 大幅低于 conditional，因为它对未正确预测的 relation triples 给 0
946	    分。 公式近似为：joint ≈ Σ_{correct triples} evi_f1(triple) / |gold_triples|。 SFT rel_recall=0.407
947	    → 约 40.7% gold triples 被正确预测 → joint ≈ 0.407 × 0.798 × factor ≈ 0.322。 RSFT CED
948	    s43 rel_recall=0.456 → joint ≈ 0.456 × 0.816 × factor ≈ 0.381。 GRPO rel_recall=0.014
949	    → joint ≈ 0.014 × 0.850 × factor ≈ 0.012——catastrophic， 因为即使 evidence quality
950	    高，几乎没有正确 relation 来"兑现"这个高 evi_f1。 这个数字本身就是 decoupling phenomenon 的最直观体现。 Joint
951	    Evi-F1 的 CED vs SFT delta（+5.96pp）比 conditional delta（+1.77pp）大得多， 因为 joint 同时受益于
952	    rel_f1 提升和 evi_f1 提升——RSFT+CED 的双重优势在 joint 指标下被放大。
953	
954	    '
955	  tables:
956	  - name: 'Table: Conditional vs Joint Evi-F1'
957	    columns:
958	    - Method
959	    - rel_F1
960	    - Evi-F1_cond
961	    - Evi-F1_joint
962	    - EDCR
963	    rows:
964	    - - SFT
965	      - 0.4057
966	      - 0.7979
967	      - 0.3216
968	      - 0.7118
969	    - - RSFT flat-NLI best
970	      - 0.4412
971	      - 0.7972
972	      - 0.3498
973	      - 0.6887
974	    - - CED-reranker
975	      - 0.4152
976	      - 0.8214
977	      - 0.3412
978	      - 0.5983
979	    - - RSFT CED s43
980	      - 0.4683
981	      - 0.8156
982	      - 0.3812
983	      - 0.6388
984	    - - GRPO best (lr=5e-5)
985	      - 0.2108
986	      - 0.5666
987	      - 0.1192
988	      - 0.8584
989	    - - GRPO best (lr=5e-6)
990	      - 0.0138
991	      - 0.8504
992	      - 0.0118
993	      - 0.9876
994	  figures_description:
995	  - 'Grouped bar chart: 每个方法的 conditional vs joint Evi-F1 并排，可视化 gap 大小——GRPO 的 gap
996	    最大（0.85 → 0.01），RSFT CED 的 gap 最小。'
997	  analysis: Joint Evi-F1 是论文主指标（与 DREEAM 可比），conditional 作为辅助指标。 Joint 指标下 GRPO 的灾难性表现（0.012）比
998	    conditional（0.850）更直观地展示了 decoupling 的后果—— 模型学会了给好 evidence 但找不到正确 relation，导致
999	    evidence 能力被浪费。 论文 main table 应以 joint 为主列，conditional 放 appendix。
1000	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8f0be40-d4a4-4432-b7e7-dab03b076cdd",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "a911943c-11b1-4088-a5ee-5909f4451802",
  "sourceToolAssistantUUID": "d8f0be40-d4a4-4432-b7e7-dab03b076cdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T14:19:27.136Z_

Now I have a thorough understanding of the paper and the experimental context. Let me also check the decisions/provenance files for additional context on methodology choices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a911943c-11b1-4088-a5ee-5909f4451802",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4Vyku2r1upc48PfN46Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53aa3127-3ba4-45f5-8729-3f2b5ca69e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qjf1x3JXokV34SJR5hGD5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6557,
      "cache_read_input_tokens": 51088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6557,
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

_source line 31 · 2026-05-15T14:19:28.621Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GYqQPyTPpNNBZihjLyAKx6`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53aa3127-3ba4-45f5-8729-3f2b5ca69e37",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4Vyku2r1upc48PfN46Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcce9a65-9030-4a3a-8957-ebe45ca3360d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qjf1x3JXokV34SJR5hGD5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6557,
      "cache_read_input_tokens": 51088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6557,
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

_source line 32 · 2026-05-15T14:19:28.653Z_

<details><summary>↩ Tool result · `toolu_01GYqQPyTPpNNBZihjLyAKx6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 47\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n- id: D041\\n  date: 2026-05-15 13:15 UTC\\n  summary: 'D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triples)与 DREEAM\\\"联合 Evi-F1\\\"(含\\n    FP/FN 惩罚)不可比，publishability threshold 暂冻结等对齐后重评'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过（precision 分母只算\\n    TP evidence），recall 分母也只算 matched gold triples。DREEAM 的 official_evaluate() 将\\n    FP/FN 全部计入分母。在 rel_recall ≈ 55% 时，分母差约 1.8x，解释了 82% vs 57% 的差距。已派 Agent 实现 DREEAM\\n    协议对齐函数并重新评估全部实验。在对齐数字出来前，paper_framing.md 的 publishability threshold（Evi-F1 >\\n    57.34）暂冻结。条件 Evi-F1 仍作为辅助指标保留（衡量\\\"关系对了时 evidence 选得好不好\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: evi_f1_conditional=0.7979, joint TBD\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: evi_f1_conditional=0.8187, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: evi_f1_conditional=0.8108, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: evi_f1_conditional=0.8128, joint TBD\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D042\\n  date: 2026-05-15 13:16 UTC\\n  summary: 'D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi-F1 跳过 FP/FN triples，比\\n    DREEAM 的 joint Evi-F1 宽松得多。必须实现 DREEAM 协议对齐后重算所有实验。Publishability threshold 待重算后修订'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过，precision 分母只算\\n    TP；recall 分母也只算已匹配 gold。DREEAM 的 official_evaluate() 把 FP/FN 全部计入分母。关系 recall\\n    ~55% 时，分母差异完全解释 82% vs 57% 的差距。对齐方案：加 FP evidence 到 precision 分母 + 遍历全部 gold triple\\n    evidence 到 recall 分母。论文需要报告 DREEAM 协议数字（与文献可比），条件 Evi-F1 可作为辅助指标（衡量\\\"关系正确时 evidence\\n    选择质量\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: conditional evi_f1=0.7979, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: conditional evi_f1=0.8187, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: conditional evi_f1=0.8108, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: conditional evi_f1=0.8128, dreeam evi_f1 待重算\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D043\\n  date: 2026-05-15 13:20 UTC\\n  summary: 'D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分倒挂）。5 个确认行动项（narrow\\n    Claim 3 scope、加 GRPO G=8、修 Evi-F1 协议、CED contingency plan、加 DPO baseline），4 个观察项。Framing\\n    和 plan 已更新，re-dream 启动'\\n  rationale: 'Dream 三档审稿分析（dream-report-action 协议）：\\n\\n\\n    **三档一致的结构性问题（确认行动项）**：\\n\\n    1. CED vs flat-NLI 可能不显著 → 加 contingency plan，如 p>0.05 则 CED 降级\\n\\n    2. Title/claims overclaim \\\"online RL\\\" → Claim 3 限定为 \\\"GRPO+QLoRA\\\"\\n\\n    3. GRPO G=4 太小 → 加 plan_011 (G=8 实验，P0)\\n\\n    4. Cross-protocol Evi-F1 → 已在修复中 (D041)\\n\\n    5. 缺中间 baseline → 加 plan_012 (DPO, P1)\\n\\n\\n    **两档一致的观察项**：\\n\\n    - EDCR 需人工验证 [M][W] → plan_013\\n\\n    - Dev→test 退化 [M][W] → 等 plan_002 真实数据\\n\\n    - Number discrepancies [B][M] → Dream artifact（虚构数据），真实论文不会有此问题\\n\\n\\n    **评分倒挂说明**：best(2.5) < median(3.0) 因 best 版本膨胀数字被审稿人识破——说明诚实报告比膨胀结果更重要。\\n\\n\\n    **判断**：framing 和 plan 已按确认行动项修改，需 re-dream 验证后才能批准 P0 实验。'\\n  related_experiments: []\\n  depends_on:\\n  - D040\\n  - D041\\n- id: D044\\n  date: 2026-05-15 13:24 UTC\\n  summary: Dream v1 分析完成：reframe paper_framing.md，CED 降级，claims 重构，新增 3 个实验\\n  rationale: Dream v1 (best=2.5, median=3.0, worst=2.5) 三档一致指出：(1) CED vs flat-NLI\\n    不显著 p>0.05 → CED 从核心贡献降级为 one possible scoring function；(2) \\\"online RL fails\\\"\\n    标题过度声称 → 收窄到 \\\"GRPO fails for DocRE\\\"；(3) GRPO G=4 太小 → 新增 G=8 实验(plan_011)；(4)\\n    缺 DPO baseline → 新增 plan_012；(5) EDCR 缺人工验证 → 新增 plan_013。Claims 重构为 C1=evidence-grounded\\n    DocRE 可行性, C2=GRPO decoupling 发现, C3=NLI-based RSFT ablation, C4=EDCR 诊断工具。需 re-dream\\n    验证 reframe 效果。\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: new_from_dream\\n    result: GRPO G=8 实验，排除 G=4 confound\\n  - exp_id: plan_012\\n    role: new_from_dream\\n    result: DPO+CED，online-offline 中间 baseline\\n  - exp_id: plan_013\\n    role: new_from_dream\\n    result: EDCR 100例人工标注验证\\n  depends_on:\\n  - D041\\n- id: D045\\n  date: 2026-05-15 13:41 UTC\\n  summary: 'D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offline preference optimization'\\n  rationale: Reviewer 指出：(1) DPO 是纯 offline 方法，不是 online/offline 中间点——论文中错误定位会被审稿人攻击。已修正\\n    paper_framing.md。(2) DPO 结果直接决定 C2 叙事走向（on-policy 特有 vs 更 general 的现象），对 paper\\n    scope 有重大影响，升级 P0。(3) C2 对 GRPO G=8 单点依赖是最大风险，G=8 必须是 re-dream 后第一个启动的实验。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: 升级 P0\\n  - exp_id: plan_011\\n    role: 第一优先 P0\\n  depends_on:\\n  - D044\\n- id: D046\\n  date: 2026-05-15 13:42 UTC\\n  summary: 'D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + topk3 双变体设计'\\n  rationale: Reviewer 路线图审查指出：(1) DPO 结果直接决定 C2 decoupling 叙事——若 DPO 也出现 decoupling\\n    则现象更 general，若不出现则确认 on-policy 特有，两种结果都对论文有重大影响，升 P0；(2) C2 publishability 必要条件依赖\\n    GRPO G=8 复现 decoupling，是最高风险实验，必须首批启动；(3) topk3 数据含 CED=0 样本会稀释信号，改为双变体并行（全量 vs\\n    过滤 CED=0）以区分数据量效应和信号稀释。同时修正 paper_framing.md 中 DPO 定位错误（纯 offline 方法，非 online/offline\\n    中间点）。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: DPO+CED 升 P0\\n  - exp_id: plan_011\\n    role: GRPO G=8 首批 P0\\n  - exp_id: plan_008\\n    role: topk3 双变体设计\\n  depends_on:\\n  - D044\\n\", \"total_chars\": 34024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcce9a65-9030-4a3a-8957-ebe45ca3360d",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "ef360fc4-1838-4876-9d19-70cad45a8dd5",
  "sourceToolAssistantUUID": "fcce9a65-9030-4a3a-8957-ebe45ca3360d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:19:29.020Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015XDJo8SZx9PAEp4Yb5WvLj`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef360fc4-1838-4876-9d19-70cad45a8dd5",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4Vyku2r1upc48PfN46Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d49ceba8-287b-4689-a3b4-7541d3c5fd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qjf1x3JXokV34SJR5hGD5U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6557,
      "cache_read_input_tokens": 51088,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 51088,
          "cache_creation_input_tokens": 6557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6557,
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

_source line 34 · 2026-05-15T14:19:29.034Z_

<details><summary>↩ Tool result · `toolu_015XDJo8SZx9PAEp4Yb5WvLj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v1 (重大 reframe based on Dream feedback)\\n> **最后更新**: 2026-05-15\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → 需 reframe 后 re-dream\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 和 offline RL (RSFT) 两条技术路线。关键发现：**GRPO 在结构化 IE 上导致 evidence-extraction decoupling**——evidence 质量持续提升（evi_f1→0.85）但抽取能力 catastrophically forget（rel_f1<0.02），这一现象在 3 种 reward function 下一致出现。RSFT 有效规避此问题。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Exploration**: 系统性比较 online RL (GRPO) vs offline RL (RSFT)\\n4. **Key finding**: evidence-extraction decoupling — GRPO 下 evidence 和 extraction 被差异化优化，extraction catastrophically forget\\n5. **What works**: RSFT with NLI-based scoring 有效提升 evidence 质量而不牺牲抽取\\n6. **Diagnostic tool**: EDCR 捕捉 Evi-F1 的盲区\\n\\n## Core Claims (reframed after Dream v1)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT 在 4/4 配置下均超过 SFT baseline（rel_f1 +3.9~6.0pp）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): GRPO 在结构化 IE 上导致 evidence-extraction decoupling\\n- 3 种 reward × 多个 lr 全线失败\\n- **Evidence-extraction decoupling**: evi_f1 → 0.850 而 rel_f1 < 0.02\\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\\n- **需要加强**: GRPO G=8 实验（排除 G=4 confound）；DPO 作为 offline preference optimization baseline（验证 decoupling 是否 on-policy 特有）\\n- **需要明确边界**: \\\"GRPO fails for DocRE\\\" 而非 \\\"online RL fails for structured IE\\\"\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n\\n### Claim 4 (Diagnostic): EDCR 捕捉 Evi-F1 的盲区\\n- EDCR 概念有价值（三档一致认可）\\n- **需要人工验证**: 100 例标注\\n- **需要更多数据点**: per-document / per-relation-type 分析\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 (conditional) | evi_f1 (joint, TBD) | EDCR |\\n|--------|--------|----------|---------------------|---------------------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.3117 | 0.7118 |\\n| RSFT r1 (3ep, s42) | 0.4449 | +3.92pp | 0.8187 | 0.3468 | 0.6565 |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.3713 | 0.6350 |\\n| RSFT r2a (1ep) | 0.4494 | +4.37pp | 0.8108 | 0.3509 | 0.6641 |\\n| RSFT r2b (1ep, conservative) | 0.4493 | +4.36pp | 0.8128 | 0.3490 | 0.6609 |\\n| GRPO (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | — | 0.9900 |\\n\\n注：evi_f1 (conditional) 仅计算 TP triples 的 evidence，与 DREEAM joint protocol 不可比（D041）。\\n\\n## Anticipated Reviewer Concerns (updated from Dream)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- 标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"\\n- 补充 DPO baseline（offline preference optimization，验证 decoupling 是否 on-policy 特有；注意 DPO 是纯 offline 方法，不是 online/offline 中间点）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 实验；LoRA confound 作为 limitation 讨论\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning（NEW）\\n6. **GRPO+CED (G=4)**: online RL negative baseline\\n7. **GRPO+CED (G=8)**: G=4 confound 排除（NEW）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 rel_f1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) GRPO decoupling 在 G=8 下仍复现\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling 在 G=8 下不复现 → scope 大幅缩减\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| P0 | GRPO G=8 experiment | C2 | ~16h |\\n| P0 | DPO+CED experiment | C2 | ~12h |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| P2 | GRPO forgetting 可视化 | C2 | ~4h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 5543, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d49ceba8-287b-4689-a3b4-7541d3c5fd67",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "71df57ad-f575-4591-b4c3-dfc4c525f57e",
  "sourceToolAssistantUUID": "d49ceba8-287b-4689-a3b4-7541d3c5fd67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-15T14:19:33.489Z_

Now I have a comprehensive understanding of the paper, the experimental history, and the review context. Let me now produce the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71df57ad-f575-4591-b4c3-dfc4c525f57e",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VzEXSeTTWU7UBUs7FV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b476897-5b1b-4a94-b98a-ece1bc9b5bf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSDKKpbnnVQf23eehJo6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23695,
      "cache_read_input_tokens": 57645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23695,
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

_source line 36 · 2026-05-15T14:19:34.533Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015r7VhhXksGTxKEyAq4VZZf`</summary>

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
  "parentUuid": "8b476897-5b1b-4a94-b98a-ece1bc9b5bf1",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VzEXSeTTWU7UBUs7FV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0becbdb3-5633-4728-92cf-f3ede9b26a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSDKKpbnnVQf23eehJo6DS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23695,
      "cache_read_input_tokens": 57645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23695,
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

_source line 37 · 2026-05-15T14:19:34.536Z_

<details><summary>↩ Tool result · `toolu_015r7VhhXksGTxKEyAq4VZZf`</summary>

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
  "parentUuid": "0becbdb3-5633-4728-92cf-f3ede9b26a47",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a40996edda29488d5",
  "type": "user",
  "uuid": "c5e5bc87-3612-4589-ac07-08dd2892b8b8",
  "sourceToolAssistantUUID": "0becbdb3-5633-4728-92cf-f3ede9b26a47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-15T14:21:02.827Z_



Now I have all the information needed. Let me produce the R1 review.

## R1 Review: Methods and Experiments

### Summary of Contributions (1-2 sentences)

FREIGE proposes the first LLM-based DocRE system that jointly generates relation triples and sentence-level evidence citations, using CED-guided rejection sampling fine-tuning (RSFT) as the training paradigm after discovering that GRPO+QLoRA causes catastrophic evidence-extraction decoupling. The paper also introduces EDCR, a diagnostic metric for detecting entity-sharing distractor citations invisible to standard Evi-F1.

### Strengths

- **S1: Comprehensive RL spectrum analysis.** The paper systematically explores GRPO (G=4, G=8, multiple LRs), DPO, SFT, and RSFT, creating a clear online-to-offline gradient (GRPO << DPO < SFT < RSFT). This is more thorough than typical ablation studies and provides genuine insight into why different RL paradigms behave differently for structured IE tasks. The 42-checkpoint forgetting dynamics analysis across 3 GRPO configurations is particularly rigorous.

- **S2: Well-designed ablation structure.** The paper includes ablations along multiple axes: CED vs flat-NLI scoring (Table 4), top-k filtering strictness (Table 8), NLI model capacity (Table 10), CED as training signal vs inference reranker (Table 5), model size (1.7B/4B/8B), and dataset variant (DocRED/Re-DocRED). Each ablation isolates a specific design choice. The CED-reranker experiment is a particularly clever control that separates the value of CED as a signal from the value of RSFT as a training paradigm.

- **S3: Statistical rigor on the core CED vs flat-NLI comparison.** The paper reports paired bootstrap p-values for all three metrics (rel_F1 p=0.007, Evi-F1 p=0.004, EDCR p=0.002), all significant at p<0.01. This is a significant improvement over what the initial DREAM review anticipated (p=0.08-0.38 non-significance). The distractor-density stratification analysis strengthens the mechanistic argument.

- **S4: Honest framing of the encoder gap.** The paper does not claim to beat DREEAM/SAIS on absolute numbers. The decomposition into extraction gap vs evidence quality gap (conditional Evi-F1 0.807 vs DREEAM's 0.834) is analytically sound and correctly identifies that the joint Evi-F1 difference is primarily driven by rel_F1, not evidence quality per se.

- **S5: EDCR is a well-motivated diagnostic.** The metric addresses a real blind spot in Evi-F1 (entity-sharing distractors that inflate NLI scores). The cross-method gradient (0.988 to 0.598) and the low correlation with Evi-F1 (r=-0.42) confirm it captures an orthogonal dimension of evidence quality.

### Weaknesses

- **W1 (Major): The evidence-extraction decoupling finding is limited to QLoRA and not adequately controlled.** All GRPO experiments use QLoRA (4-bit quantization, rank=64). The paper claims "structural incompatibility between on-policy RL and document-level structured IE under parameter-efficient fine-tuning" but never tests full fine-tuning or even higher-rank LoRA/bf16 LoRA as controls. The decisions log (D008) reveals that kl_coef>0 caused KL explosion specifically due to QLoRA quantization noise, and D014 shows CED reward was reward-hacked by short outputs --- both are QLoRA-specific pathologies. The claim should be scoped as "GRPO+QLoRA fails for DocRE" rather than implying on-policy RL is fundamentally incompatible with structured IE. The running experiment `plan_011_grpo_g8_bf16` (bf16 LoRA, not QLoRA) would directly address this but results are not yet available.

- **W2 (Major): Dev-to-test degradation asymmetry raises overfitting concerns.** RSFT+CED degrades by 1.3pp (dev 0.468 to test 0.455) while SFT degrades by only 0.6pp (dev 0.406 to test 0.400). The RSFT pipeline generates candidates from training documents and filters by CED score, which could create an implicit data leakage: the CED scorer (DeBERTa MNLI) may score training-set documents differently from unseen test documents due to entity/relation distribution overlap. The 2x relative degradation is not catastrophic but warrants analysis --- e.g., does CED filtering disproportionately select candidates from documents with high entity overlap with the training set?

- **W3 (Moderate): EDCR human validation is underpowered.** The correlation r=0.62 is computed over only 100 samples (25 per method). With 4 data points at the method level, "perfect method-level rank concordance" is trivially achievable (4! = 24 permutations, random chance = 1/24 = 4.2%). The per-sample Pearson r=0.62 is respectable but the confidence interval is wide at n=100. The auto-human gap of +11.5pp for RSFT CED (the paper's own method) is concerning --- it suggests EDCR may systematically overestimate the distractor rate for CED-trained models, which would bias the metric toward favoring exactly the method being proposed.

- **W4 (Moderate): The paper's practical impact is limited by the large extraction gap.** FREIGE achieves rel_F1=0.455 vs DREEAM's ~0.631 and LMRC's 0.607. While the paper frames this as an inherent generative-paradigm limitation, LMRC (same paradigm, LLaMA-3.1-8B) achieves 0.607 with the same 8B scale, suggesting the gap is at least partly model/training-specific. The 8B RSFT result (rel_F1=0.491 dev) still falls well short of LMRC's 0.607, and the paper does not explain this discrepancy (different base model? different prompt format? LMRC doesn't produce evidence so has a simpler output space?). Without addressing this, the claim of being a practical evidence-grounded DocRE system is weakened.

- **W5 (Minor): Training details for reproducibility are incomplete.** The paper reports results for "best RSFT configuration (3 epochs, alpha=128, seed=43)" but the decisions log reveals extensive hyperparameter search (multiple seeds, epochs, LoRA alpha values, learning rates). The selection of seed=43 as the "best" seed for the main result raises concerns about seed cherry-picking. The paper should report mean +/- std across seeds (at least 3 seeds are available: s42, s43, s44 with rel_F1 = 0.4449, 0.4683, 0.4655 respectively).

- **W6 (Minor): CED formulation uses gold evidence labels during scoring.** Equation (2) defines the hard negative set as N(h,t,D) = {s' in D \ E_gold : s' mentions h or t}. This means CED scoring requires access to gold evidence annotations, which limits its applicability to settings where such annotations exist. The paper does not discuss this dependency or propose alternatives for settings without gold evidence labels.

### Questions for Authors

1. Have you tested GRPO with full fine-tuning (no LoRA/QLoRA) even on a smaller subset? This would directly address whether the decoupling is a LoRA artifact or a genuine RL-for-IE phenomenon.

2. The CED formula subtracts max entailment over hard negatives. What happens when N(h,t,D) is empty (the paper mentions 44.4% of triples have no hard negatives in D002)? Does CED degenerate to flat-NLI in those cases? If so, nearly half the training signal is identical between CED and flat-NLI, which would explain why the gap is moderate.

3. Why does FREIGE's 8B model (rel_F1=0.491) still substantially underperform LMRC (0.607) despite using a comparable model scale? Is this because jointly generating evidence makes the task harder, or due to other factors (base model, prompt design, training data)?

4. Table 4 reports CED vs flat-NLI p-values of 0.007/0.004/0.002, but the review_context.yaml lists the expected p-values as 0.0067/0.0038/0.0021 --- identical to 3 significant figures. Were these the actual computed values or the pre-specified expectations from the DREAM simulation?

5. The three-phase forgetting dynamics (onset/acceleration/plateau) --- is this specific to evidence-quality rewards, or would any reward (e.g., pure extraction F1) cause similar forgetting? The decisions log (D022-D24) shows extraction-only reward also caused mode collapse, which weakens the "evidence-extraction decoupling" framing --- it may simply be "GRPO+QLoRA catastrophic forgetting for any complex structured generation task."

### Missing Experiments or Analysis

1. **GRPO with full fine-tuning or bf16 LoRA**: Critical to scope the decoupling claim. Currently running (plan_011_grpo_g8_bf16) but not reported.

2. **Multi-seed statistics for main results**: The paper reports single-seed best results. At minimum, mean +/- std over the 3 available seeds should be reported for RSFT+CED.

3. **LMRC-comparable LLM baseline without evidence**: Run the same Qwen3-4B/8B with standard DocRE prompts (no evidence output) to measure the evidence generation tax --- how much rel_F1 is lost by requiring evidence?

4. **Per-relation-type analysis**: Do certain relation types benefit more from CED vs flat-NLI? The stratification by distractor density is good but relation-type analysis would strengthen the mechanistic story.

5. **Error analysis of EDCR auto-human gap**: The +11.5pp gap for RSFT CED deserves deeper investigation --- are there systematic categories of sentences that EDCR miscategorizes?

### Claims-Evidence Assessment

| Claim | Evidence | Verdict |
|-------|----------|---------|
| C1: First LLM DocRE with explicit evidence | No prior work cited that does this; SFT+RSFT results across scales/datasets | **Supported** --- novel task contribution is clear |
| C2: RSFT+CED yields +5.5pp rel_F1 over SFT on test | Table 1: 0.455 vs 0.400, dev results with p<0.01 | **Supported** --- but single-seed test result; would be stronger with multi-seed |
| C3: CED > flat-NLI as RSFT scoring | Table 4: +2.7pp rel_F1, p=0.007 | **Supported** --- statistically significant with paired bootstrap |
| C4: GRPO causes evidence-extraction decoupling | Tables 3-4, 42 checkpoints, G=4 and G=8 | **Partially supported** --- convincing within QLoRA, but generalizability beyond QLoRA unclear; extraction-only reward also collapses (D022-24), weakening the "decoupling" framing |
| C5: EDCR captures dimension invisible to Evi-F1 | Cross-method r=-0.42 with Evi-F1, human r=0.62 | **Partially supported** --- promising but underpowered human validation (n=100, 4 methods) |
| C6: CED better as training signal than inference reranker | Table 5: RSFT +6.3pp vs reranker +0.95pp | **Supported** --- clean comparison |

### Scores

- **Soundness**: 3/5
- **Excitement**: 3/5
- **Overall Assessment**: 3.0/5
- **Confidence**: 4/5

### Justification for Overall Assessment (2-3 sentences)

The paper introduces a genuinely useful new capability (evidence-grounded LLM DocRE) and provides a thorough experimental exploration of the RL landscape for this task. However, two issues prevent a higher score: (1) the evidence-extraction decoupling claim, which is the paper's most novel finding, is confounded by QLoRA-specific pathologies and the fact that extraction-only rewards also cause collapse, undermining the "decoupling" narrative; and (2) the large performance gap vs both encoder baselines and same-scale generative methods (LMRC) limits practical impact. With the bf16 LoRA GRPO experiment, multi-seed reporting, and a clearer scoping of the decoupling claim, this could become a solid accept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5e5bc87-3612-4589-ac07-08dd2892b8b8",
  "isSidechain": true,
  "agentId": "a40996edda29488d5",
  "requestId": "req_011Cb4VzeMQUQeAaiJ3jUhCj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f8adbd9-dbed-4958-9b75-332f144bf29a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SPunjdKt6hEW1YjFuFatY3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 81340,
      "output_tokens": 3150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3150,
          "cache_read_input_tokens": 81340,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 796,
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
