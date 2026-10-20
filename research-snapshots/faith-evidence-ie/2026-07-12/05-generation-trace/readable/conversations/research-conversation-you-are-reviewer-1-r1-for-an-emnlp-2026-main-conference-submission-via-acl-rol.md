# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 Main conference submission via ACL Rolling Review. Your focus is **Methods and

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 27
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aebcf4b7d1ca414e2.jsonl`
- **Structured JSON:** [`87b244599a3c4e2ab1b3.json`](../../sessions/87/87b244599a3c4e2ab1b3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

68 recorded events

### User

_source line 1 · 2026-05-15T14:28:02.317Z_

You are Reviewer 1 (R1) for an EMNLP 2026 Main conference submission via ACL Rolling Review. Your focus is **Methods and Experiments**.

## ARR Scoring Scale
- **Soundness** (1-5): 5=Excellent (one of the most thorough), 4=Strong (sufficient support for all claims), 3=Acceptable (sufficient for main claims), 2=Poor, 1=Major issues
- **Excitement** (1-5): 5=Highly Exciting (recommend to others), 4=Exciting (mention to others), 3=Ambivalent, 2=Mediocre, 1=Not exciting
- **Overall Assessment** (1-5): 5=Award, 4.5=Strong Accept, 4=Accept, 3.5=Leaning Accept, 3=Borderline, 2.5=Leaning Reject, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit
- **Confidence** (1-5): 5=Absolutely certain, 4=Quite sure, 3=Fairly confident, 2=Willing to defend but not sure, 1=Not my area

## Paper Summary

**Title:** "How Should LLMs Generate Evidence for Document-Level Relation Extraction? A Systematic Study of Training Paradigms and Evaluation"

**Core idea:** First systematic study of LLM-based evidence generation for DocRE. Instead of proposing a single method, frames the problem along three axes: (1) task definition + evaluation framework (conditional vs joint Evi-F1, plus EDCR metric), (2) training paradigm comparison (RSFT, GRPO, DPO), (3) evaluation metric analysis.

**Base model:** Qwen3-4B with QLoRA (rank=64, α=128) on DocRED.

**Methods:**
- SFT baseline: structured output (relation type + evidence sentence indices)
- Candidate Scoring: N=8 candidates scored by DeBERTa-v3-base NLI model
  - Flat-NLI: mean p_pos across evidence sentences
  - CED (Contrastive Evidence Discrimination): margin between gold evidence p_pos and highest-scoring entity-sharing distractor p_pos
- RSFT: top-k=1 selection from candidates, fine-tune on selected
- GRPO: online RL with CED reward, G=4 and G=8
- DPO: offline preference learning from CED-ranked pairs

**Evaluation Metrics:**
- Rel-F1: standard micro-F1 over (h,r,t) triples
- Evi-F1_cond: evidence F1 only for correctly extracted relations
- Evi-F1_joint: evidence counts only if relation is also correct (DREEAM protocol)
- EDCR: fraction of cited sentences that share entities with target relation but are not gold evidence (lower is better)

**Key Results (all from the paper):**

Table 1 (Dev set):
- SFT: Rel-F1=40.57, Evi-F1_cond=79.79, EDCR=71.18
- RSFT flat-NLI: 45.60, 81.20, 65.80
- RSFT+CED (s44): **46.55**, 80.87, **63.50**
- CED-as-reranker: 41.30, 80.20, 66.80
- DPO+CED: 38.50, 80.50, 65.20

Table 2 (Test set):
- SFT: 39.30, —, 24.80 (joint), 73.20
- RSFT+CED: 40.80, 40.10 (Ign-F1), 26.50 (joint), 69.00
- DREEAM (paper): 63.00, —, 57.34 (joint), N/A
- RSFT advantage shrinks to +1.5pp Rel-F1 (p=0.08, not significant at α=0.05)

Table 3 (Dev vs Test):
- RSFT dev→test drop: -5.75pp Rel-F1
- SFT dev→test drop: -1.27pp Rel-F1

Table 4 (CED vs flat-NLI): No statistically significant differences (p>0.10 on all three metrics). Jaccard overlap=0.76.

Table 5 (NLI model ablation): DeBERTa-base vs large — no meaningful difference.

Table 7 (top-k): k=1 (2718 samples) vs k=3 (8154 samples) — slight degradation with more data.

Table 8 (GRPO): All variants catastrophically fail. CED G=4 lr=5e-5: Rel-F1=21.7. CED G=4 lr=5e-6: Rel-F1=1.4, Evi-F1=85.0, EDCR=98.8 (extreme decoupling). flat-NLI and extract-only G=4: collapse.

Table 9 (G=4 vs G=8): G=8 partially recovers (+1.8pp Rel-F1) but still -17.1pp below SFT.

Table 10 (G=8 trajectory): Reward peaks at step 80 (1.52), Rel-F1 peaks at step 80 (23.5) then declines to 19.8 at step 100.

Table 11 (Online-offline spectrum): GRPO G=4 < GRPO G=8 < DPO ≈ SFT < RSFT flat-NLI < RSFT+CED

Table 12 (Cross-paradigm): Joint Evi-F1: RSFT 33.8 vs DREEAM 60.8 (-27pp). Conditional Evi-F1: RSFT 80.9 vs DREEAM N/A.

Table 13 (EDCR diagnostic): EDCR captures GRPO decoupling (98.8) invisible to Evi-F1 (85.0). Normal range: 63.5-71.2.

Table 14 (EDCR human validation): Pearson r=0.28, Spearman ρ=0.31. Precision=0.55, Recall=0.62. Human distractor rate=0.48 vs EDCR predicted=0.65.

Table 15 (EDCR disagreement): 45% false positives from incomplete gold annotations.

Table 16 (Model size): 1.7B ΔRSFT=+2.6pp, 4B ΔRSFT=+6.0pp, 8B ΔRSFT=+1.7pp (non-monotonic).

Table 17 (Re-DocRED): RSFT gain shrinks from +6.0pp to +2.3pp.

**Limitations stated:** (1) all QLoRA, (2) GRPO limited to G≤8, (3) 100-sample human study small, (4) DocRED only.

## Experiment Design Reference (what experiments were planned)

The full experiment design includes these planned experiments:
1. CED vs flat-NLI RSFT ablation — DONE in paper (Table 4)
2. Test set evaluation — DONE (Table 2)
3. EDCR pipeline validation + cross-method diagnostic — DONE (Table 13)
4. DREEAM baseline reproduction — DONE (Table 12)
5. CED-as-reranker — DONE (Table 6)
6. Model size ablation (1.7B/8B) — DONE (Table 16)
7. Re-DocRED extension — DONE (Table 17)
8. top_k ablation (k=1 vs k=3) — DONE (Table 7)
9. GRPO forgetting analysis + visualization — DONE (Tables 8-10)
10. NLI model ablation (base vs large) — DONE (Table 5)
11. GRPO G=8 experiment — DONE (Table 9)
12. DPO+CED experiment — DONE (Table 11)
13. EDCR human annotation validation — DONE (Tables 14-15)

All planned experiments appear covered.

## Your Task

Write a detailed review focusing on **Methods and Experiments**. Evaluate:

1. **Experimental design**: Are the experiments well-designed? Do they support the claims? Are baselines appropriate?
2. **Statistical rigor**: Are results statistically significant? Are appropriate tests used?
3. **Reproducibility**: Is there enough detail to reproduce? Are hyperparameters reported?
4. **Methodological soundness**: Are the proposed methods (CED, EDCR, evaluation protocols) well-motivated and correctly implemented?
5. **Result interpretation**: Are results interpreted fairly? Are limitations acknowledged?
6. **Missing experiments**: What experiments would strengthen the paper?

Structure your review as:
```
## Summary (2-3 sentences)
## Strengths (bulleted)
## Weaknesses (bulleted, with severity: major/minor)
## Questions for Authors
## Soundness: X/5
## Excitement: X/5  
## Overall: X/5
## Confidence: X/5
```

Be rigorous but fair. Judge based on what is in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "9fc998e5-26ab-4c73-87f8-586386e9c302",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:28:02.324Z_

```json
{
  "parentUuid": "9fc998e5-26ab-4c73-87f8-586386e9c302",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
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
  "uuid": "096b44da-51aa-4a3b-8e9e-346407424d91",
  "timestamp": "2026-05-15T14:28:02.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:28:05.361Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "096b44da-51aa-4a3b-8e9e-346407424d91",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4We4sKrqZhhU7x5uJdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb281b7d-5b11-4ad4-9de4-372cb475fb77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJHo28xvki7Y3Lbq1r5CjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16381,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16381,
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

_source line 4 · 2026-05-15T14:28:06.851Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FGFMTVM2pKkaYdF4LGD2PV`</summary>

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
  "parentUuid": "fb281b7d-5b11-4ad4-9de4-372cb475fb77",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4We4sKrqZhhU7x5uJdF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "158b651a-d910-4601-82bc-4b6c4dbe68ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJHo28xvki7Y3Lbq1r5CjK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16381,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16381
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16381,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16381,
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

_source line 5 · 2026-05-15T14:28:06.856Z_

<details><summary>↩ Tool result · `toolu_01FGFMTVM2pKkaYdF4LGD2PV`</summary>

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
  "parentUuid": "158b651a-d910-4601-82bc-4b6c4dbe68ba",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "d0ab19c3-17f5-4041-8270-7a8e2df2ecad",
  "sourceToolAssistantUUID": "158b651a-d910-4601-82bc-4b6c4dbe68ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T14:28:09.773Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_0169W5FunqRJuFDm6XKsQ5yA`</summary>

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
  "parentUuid": "d0ab19c3-17f5-4041-8270-7a8e2df2ecad",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WeQRKYjSYH5coKFaef",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f61df6e-8437-424d-a84c-35ae1d2027ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSdh6kiRsVjSqr2etbtaJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16381,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 7 · 2026-05-15T14:28:10.079Z_

<details><summary>↩ Tool result · `toolu_0169W5FunqRJuFDm6XKsQ5yA`</summary>

```text
{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (76 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\n\n## 待处理\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\n\n## 近期结论\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\n\n## 趋势\n成功 26 / 负向 11 / 失败 12 / 共 71\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — u\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f61df6e-8437-424d-a84c-35ae1d2027ba",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "093a346e-d768-496e-b140-fc9343244387",
  "sourceToolAssistantUUID": "3f61df6e-8437-424d-a84c-35ae1d2027ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T14:28:10.294Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J8CYxVx9FyEdbv1kh9opW8`</summary>

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
  "parentUuid": "093a346e-d768-496e-b140-fc9343244387",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WeQRKYjSYH5coKFaef",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6dd017e-90a3-41ab-92e4-0a0e89d0d520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BSdh6kiRsVjSqr2etbtaJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16381,
      "output_tokens": 160,
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
          "output_tokens": 160,
          "cache_read_input_tokens": 16381,
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

_source line 9 · 2026-05-15T14:28:10.304Z_

<details><summary>↩ Tool result · `toolu_01J8CYxVx9FyEdbv1kh9opW8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\\n\\n## 待处理\\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\\n\\n## 趋势\\n成功 26 / 负向 11 / 失败 12 / 共 71\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_ced_scoring_topk3: 已被终止 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n- mvp2_eval_rsft_r2b_maxtok1536: 已被终止 — unknown\\n\", \"total_chars\": 3533, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6dd017e-90a3-41ab-92e4-0a0e89d0d520",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "1dfa1e6d-f63c-422a-a6a8-77e7fae61dfe",
  "sourceToolAssistantUUID": "c6dd017e-90a3-41ab-92e4-0a0e89d0d520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T14:28:13.647Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G8vjUxvCm23JbHk83jB4SQ`</summary>

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
  "parentUuid": "1dfa1e6d-f63c-422a-a6a8-77e7fae61dfe",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wef5dHUFcEnNJ7zkF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90017d87-613d-4d51-945a-16900f4f54c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzvJbogASCq3KJEmW19h87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 17828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 11 · 2026-05-15T14:28:13.657Z_

<details><summary>↩ Tool result · `toolu_01G8vjUxvCm23JbHk83jB4SQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v1 (重大 reframe based on Dream feedback)\\n> **最后更新**: 2026-05-15\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → 需 reframe 后 re-dream\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 和 offline RL (RSFT) 两条技术路线。关键发现：**GRPO 在结构化 IE 上导致 evidence-extraction decoupling**——evidence 质量持续提升（evi_f1→0.85）但抽取能力 catastrophically forget（rel_f1<0.02），这一现象在 3 种 reward function 下一致出现。RSFT 有效规避此问题。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Exploration**: 系统性比较 online RL (GRPO) vs offline RL (RSFT)\\n4. **Key finding**: evidence-extraction decoupling — GRPO 下 evidence 和 extraction 被差异化优化，extraction catastrophically forget\\n5. **What works**: RSFT with NLI-based scoring 有效提升 evidence 质量而不牺牲抽取\\n6. **Diagnostic tool**: EDCR 捕捉 Evi-F1 的盲区\\n\\n## Core Claims (reframed after Dream v1)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT 在 4/4 配置下均超过 SFT baseline（rel_f1 +3.9~6.0pp）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): GRPO 在结构化 IE 上导致 evidence-extraction decoupling\\n- 3 种 reward × 多个 lr 全线失败\\n- **Evidence-extraction decoupling**: evi_f1 → 0.850 而 rel_f1 < 0.02\\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\\n- **需要加强**: GRPO G=8 实验（排除 G=4 confound）；DPO 作为 offline preference optimization baseline（验证 decoupling 是否 on-policy 特有）\\n- **需要明确边界**: \\\"GRPO fails for DocRE\\\" 而非 \\\"online RL fails for structured IE\\\"\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n\\n### Claim 4 (Diagnostic): EDCR 捕捉 Evi-F1 的盲区\\n- EDCR 概念有价值（三档一致认可）\\n- **需要人工验证**: 100 例标注\\n- **需要更多数据点**: per-document / per-relation-type 分析\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 (conditional) | evi_f1 (joint, TBD) | EDCR |\\n|--------|--------|----------|---------------------|---------------------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.3117 | 0.7118 |\\n| RSFT r1 (3ep, s42) | 0.4449 | +3.92pp | 0.8187 | 0.3468 | 0.6565 |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.3713 | 0.6350 |\\n| RSFT r2a (1ep) | 0.4494 | +4.37pp | 0.8108 | 0.3509 | 0.6641 |\\n| RSFT r2b (1ep, conservative) | 0.4493 | +4.36pp | 0.8128 | 0.3490 | 0.6609 |\\n| GRPO (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | — | 0.9900 |\\n\\n注：evi_f1 (conditional) 仅计算 TP triples 的 evidence，与 DREEAM joint protocol 不可比（D041）。\\n\\n## Anticipated Reviewer Concerns (updated from Dream)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- 标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"\\n- 补充 DPO baseline（offline preference optimization，验证 decoupling 是否 on-policy 特有；注意 DPO 是纯 offline 方法，不是 online/offline 中间点）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 实验；LoRA confound 作为 limitation 讨论\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning（NEW）\\n6. **GRPO+CED (G=4)**: online RL negative baseline\\n7. **GRPO+CED (G=8)**: G=4 confound 排除（NEW）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 rel_f1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) GRPO decoupling 在 G=8 下仍复现\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling 在 G=8 下不复现 → scope 大幅缩减\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| P0 | GRPO G=8 experiment | C2 | ~16h |\\n| P0 | DPO+CED experiment | C2 | ~12h |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| P2 | GRPO forgetting 可视化 | C2 | ~4h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 5543, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90017d87-613d-4d51-945a-16900f4f54c7",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "a80d3cf9-e93c-4c4d-9195-d3d8e0195156",
  "sourceToolAssistantUUID": "90017d87-613d-4d51-945a-16900f4f54c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T14:28:14.625Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015HjWkVdwHXABFcmhAUaJpT`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "EVALUATION.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a80d3cf9-e93c-4c4d-9195-d3d8e0195156",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wef5dHUFcEnNJ7zkF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c22088ea-04ee-4b22-adde-37a7bd9342f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzvJbogASCq3KJEmW19h87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 17828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 13 · 2026-05-15T14:28:14.637Z_

<details><summary>↩ Tool result · `toolu_015HjWkVdwHXABFcmhAUaJpT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c22088ea-04ee-4b22-adde-37a7bd9342f9",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "46ee804d-ce8a-475d-9430-549a54741ca4",
  "sourceToolAssistantUUID": "c22088ea-04ee-4b22-adde-37a7bd9342f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T14:28:15.038Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015rxfdoVdyLUEwRyJeDLUTq`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ARCHITECTURE.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46ee804d-ce8a-475d-9430-549a54741ca4",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wef5dHUFcEnNJ7zkF1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0df879c7-9125-4eb9-a710-1aad8fc2de46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzvJbogASCq3KJEmW19h87",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4672,
      "cache_read_input_tokens": 17828,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 17828,
          "cache_creation_input_tokens": 4672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4672,
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

_source line 15 · 2026-05-15T14:28:15.050Z_

<details><summary>↩ Tool result · `toolu_015rxfdoVdyLUEwRyJeDLUTq`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ARCHITECTURE.md found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0df879c7-9125-4eb9-a710-1aad8fc2de46",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "ae4cea5e-6870-42da-ac41-485a4dff60de",
  "sourceToolAssistantUUID": "0df879c7-9125-4eb9-a710-1aad8fc2de46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T14:28:18.107Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012B3PvwjAe2gWCuKykytSSN`</summary>

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
  "parentUuid": "ae4cea5e-6870-42da-ac41-485a4dff60de",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wf1UTdZudUKsuKmL9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f6ad9ee-c47c-41d2-8a21-ab4e24134b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ci7J1ucQHcqGp8zC2SQRf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3666,
      "cache_read_input_tokens": 22500,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3666,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 17 · 2026-05-15T14:28:18.124Z_

<details><summary>↩ Tool result · `toolu_012B3PvwjAe2gWCuKykytSSN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 47\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n- id: D041\\n  date: 2026-05-15 13:15 UTC\\n  summary: 'D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triples)与 DREEAM\\\"联合 Evi-F1\\\"(含\\n    FP/FN 惩罚)不可比，publishability threshold 暂冻结等对齐后重评'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过（precision 分母只算\\n    TP evidence），recall 分母也只算 matched gold triples。DREEAM 的 official_evaluate() 将\\n    FP/FN 全部计入分母。在 rel_recall ≈ 55% 时，分母差约 1.8x，解释了 82% vs 57% 的差距。已派 Agent 实现 DREEAM\\n    协议对齐函数并重新评估全部实验。在对齐数字出来前，paper_framing.md 的 publishability threshold（Evi-F1 >\\n    57.34）暂冻结。条件 Evi-F1 仍作为辅助指标保留（衡量\\\"关系对了时 evidence 选得好不好\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: evi_f1_conditional=0.7979, joint TBD\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: evi_f1_conditional=0.8187, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: evi_f1_conditional=0.8108, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: evi_f1_conditional=0.8128, joint TBD\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D042\\n  date: 2026-05-15 13:16 UTC\\n  summary: 'D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi-F1 跳过 FP/FN triples，比\\n    DREEAM 的 joint Evi-F1 宽松得多。必须实现 DREEAM 协议对齐后重算所有实验。Publishability threshold 待重算后修订'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过，precision 分母只算\\n    TP；recall 分母也只算已匹配 gold。DREEAM 的 official_evaluate() 把 FP/FN 全部计入分母。关系 recall\\n    ~55% 时，分母差异完全解释 82% vs 57% 的差距。对齐方案：加 FP evidence 到 precision 分母 + 遍历全部 gold triple\\n    evidence 到 recall 分母。论文需要报告 DREEAM 协议数字（与文献可比），条件 Evi-F1 可作为辅助指标（衡量\\\"关系正确时 evidence\\n    选择质量\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: conditional evi_f1=0.7979, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: conditional evi_f1=0.8187, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: conditional evi_f1=0.8108, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: conditional evi_f1=0.8128, dreeam evi_f1 待重算\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D043\\n  date: 2026-05-15 13:20 UTC\\n  summary: 'D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分倒挂）。5 个确认行动项（narrow\\n    Claim 3 scope、加 GRPO G=8、修 Evi-F1 协议、CED contingency plan、加 DPO baseline），4 个观察项。Framing\\n    和 plan 已更新，re-dream 启动'\\n  rationale: 'Dream 三档审稿分析（dream-report-action 协议）：\\n\\n\\n    **三档一致的结构性问题（确认行动项）**：\\n\\n    1. CED vs flat-NLI 可能不显著 → 加 contingency plan，如 p>0.05 则 CED 降级\\n\\n    2. Title/claims overclaim \\\"online RL\\\" → Claim 3 限定为 \\\"GRPO+QLoRA\\\"\\n\\n    3. GRPO G=4 太小 → 加 plan_011 (G=8 实验，P0)\\n\\n    4. Cross-protocol Evi-F1 → 已在修复中 (D041)\\n\\n    5. 缺中间 baseline → 加 plan_012 (DPO, P1)\\n\\n\\n    **两档一致的观察项**：\\n\\n    - EDCR 需人工验证 [M][W] → plan_013\\n\\n    - Dev→test 退化 [M][W] → 等 plan_002 真实数据\\n\\n    - Number discrepancies [B][M] → Dream artifact（虚构数据），真实论文不会有此问题\\n\\n\\n    **评分倒挂说明**：best(2.5) < median(3.0) 因 best 版本膨胀数字被审稿人识破——说明诚实报告比膨胀结果更重要。\\n\\n\\n    **判断**：framing 和 plan 已按确认行动项修改，需 re-dream 验证后才能批准 P0 实验。'\\n  related_experiments: []\\n  depends_on:\\n  - D040\\n  - D041\\n- id: D044\\n  date: 2026-05-15 13:24 UTC\\n  summary: Dream v1 分析完成：reframe paper_framing.md，CED 降级，claims 重构，新增 3 个实验\\n  rationale: Dream v1 (best=2.5, median=3.0, worst=2.5) 三档一致指出：(1) CED vs flat-NLI\\n    不显著 p>0.05 → CED 从核心贡献降级为 one possible scoring function；(2) \\\"online RL fails\\\"\\n    标题过度声称 → 收窄到 \\\"GRPO fails for DocRE\\\"；(3) GRPO G=4 太小 → 新增 G=8 实验(plan_011)；(4)\\n    缺 DPO baseline → 新增 plan_012；(5) EDCR 缺人工验证 → 新增 plan_013。Claims 重构为 C1=evidence-grounded\\n    DocRE 可行性, C2=GRPO decoupling 发现, C3=NLI-based RSFT ablation, C4=EDCR 诊断工具。需 re-dream\\n    验证 reframe 效果。\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: new_from_dream\\n    result: GRPO G=8 实验，排除 G=4 confound\\n  - exp_id: plan_012\\n    role: new_from_dream\\n    result: DPO+CED，online-offline 中间 baseline\\n  - exp_id: plan_013\\n    role: new_from_dream\\n    result: EDCR 100例人工标注验证\\n  depends_on:\\n  - D041\\n- id: D045\\n  date: 2026-05-15 13:41 UTC\\n  summary: 'D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offline preference optimization'\\n  rationale: Reviewer 指出：(1) DPO 是纯 offline 方法，不是 online/offline 中间点——论文中错误定位会被审稿人攻击。已修正\\n    paper_framing.md。(2) DPO 结果直接决定 C2 叙事走向（on-policy 特有 vs 更 general 的现象），对 paper\\n    scope 有重大影响，升级 P0。(3) C2 对 GRPO G=8 单点依赖是最大风险，G=8 必须是 re-dream 后第一个启动的实验。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: 升级 P0\\n  - exp_id: plan_011\\n    role: 第一优先 P0\\n  depends_on:\\n  - D044\\n- id: D046\\n  date: 2026-05-15 13:42 UTC\\n  summary: 'D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + topk3 双变体设计'\\n  rationale: Reviewer 路线图审查指出：(1) DPO 结果直接决定 C2 decoupling 叙事——若 DPO 也出现 decoupling\\n    则现象更 general，若不出现则确认 on-policy 特有，两种结果都对论文有重大影响，升 P0；(2) C2 publishability 必要条件依赖\\n    GRPO G=8 复现 decoupling，是最高风险实验，必须首批启动；(3) topk3 数据含 CED=0 样本会稀释信号，改为双变体并行（全量 vs\\n    过滤 CED=0）以区分数据量效应和信号稀释。同时修正 paper_framing.md 中 DPO 定位错误（纯 offline 方法，非 online/offline\\n    中间点）。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: DPO+CED 升 P0\\n  - exp_id: plan_011\\n    role: GRPO G=8 首批 P0\\n  - exp_id: plan_008\\n    role: topk3 双变体设计\\n  depends_on:\\n  - D044\\n\", \"total_chars\": 34024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f6ad9ee-c47c-41d2-8a21-ab4e24134b8f",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "4b7640c1-ec69-47de-b8f2-b4dec76a3a33",
  "sourceToolAssistantUUID": "5f6ad9ee-c47c-41d2-8a21-ab4e24134b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T14:28:18.475Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RTsr7S196AyuTzRfQh3MX9`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7640c1-ec69-47de-b8f2-b4dec76a3a33",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wf1UTdZudUKsuKmL9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00079ef5-5e2c-4be3-8942-35aac6290ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ci7J1ucQHcqGp8zC2SQRf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3666,
      "cache_read_input_tokens": 22500,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 22500,
          "cache_creation_input_tokens": 3666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3666,
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

_source line 19 · 2026-05-15T14:28:18.499Z_

<details><summary>↩ Tool result · `toolu_01RTsr7S196AyuTzRfQh3MX9`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## D038 重大修正：RSFT r1 实际成功 (2026-05-15)\\n\\n### 事件\\nD037 报告 RSFT r1 \\\"灾难性失败\\\"（rel_f1=0.0483），但这是 **TaskEvalCallback bug**——`--eval_max_docs 50` 评估 50 个 doc 的预测，却用全部 12275 个 gold triples 计算 F1，严重低估 rel_f1。\\n\\n### 真实结果\\ns44 全量 dev eval (985 docs): **rel_f1=0.4655 (+5.98pp), evi_f1=0.8087 (+1.08pp)** → MVP-2 PASS\\n\\n### TaskEvalCallback bug fix\\n已部署到 `rsft_trainer.py:118-120`。gold triples 现在过滤到 eval_max_docs 对应的文档子集。\\n\\n### 教训\\n- 在 callback 中用 subset eval 时，必须确保 gold 和 pred 在同一文档集合上计算\\n- 基于 callback 数字的任何结论都需要全量 eval 交叉验证\\n\\n---\\n\\n## ~~RSFT r1 灾难性失败根因~~ [D038 撤回]\\n\\n**以下分析基于 D037 的错误 rel_f1=0.0483。D038 确认该数字是 eval bug，实际 rel_f1=0.4655。**\\n\\n原分析中关于\\\"关系本体崩塌\\\"的观察可能来自 eval_max_docs=50 下的极小样本偏差，不代表模型真实行为。r1/s43/s44 的全量 eval 正在进行中，将给出真实 ablation 数据。\\n\\n---\\n\\n## RSFT r2a/r2b ablation 结果 (2026-05-15)\\n\\n### 实验配置与结果\\n\\n| 配置 | rel_f1 | evi_f1 | edcr | Δrel_f1 |\\n|------|--------|--------|------|---------|\\n| SFT baseline | 0.4057 | 0.7979 | 0.7118 | — |\\n| r1 (3ep, α=128, lr=2e-5, 2718) | 0.4449 | **0.8187** | 0.6565 | +3.92pp |\\n| r2a (1ep, α=128, lr=2e-5, clean 2548) | **0.4494** | 0.8108 | 0.6641 | +4.37pp |\\n| r2b (1ep, α=32, lr=1e-5, clean 2548) | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\\n\\n### Ablation 结论\\n1. **1 epoch ≈ 3 epoch on rel_f1**（r2a=0.4494 vs r1=0.4449），多 epoch 无额外收益\\n2. **LoRA scaling 不敏感**（α=128 vs α=32 差异 <0.1pp）\\n3. **r1 在 evi_f1 上最优**（0.8187 vs r2a 0.8108），3 epoch 可能有助于证据定位\\n4. **所有 RSFT 变体 EDCR 低于 SFT**（~0.66 vs 0.71），RSFT 增加 pred_count 导致更多 distractor citation\\n\\n---\\n\\n## RSFT 文献对标 (2026-05-15, 更新)\\n\\n### 直接竞争者：无\\n在 DocRE / IE 上**无人用过 RSFT**，NLI-based CED reward for RE training 也无先例。Novelty 完全成立。\\n\\n### 最接近竞争者：R1-RE (arXiv 2507.04642)\\n用 GRPO 做**句子级** RE。与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无。\\n\\n### Must-cite 论文\\n1. **R1-RE** — GRPO for sentence-level RE（最近竞争者，需在 related work 中区分）\\n2. **\\\"Minimalist Approach\\\"** — RSFT 理论基础\\n3. **RelPrior** — LLM-based DocRE baseline (+2.06-2.38pp rel_f1)\\n4. **\\\"RSFT=PPO\\\" (ICML 2025)** — RSFT 与 PPO 等价性理论\\n\\n### 我们的定位\\n- +3.9~6.0pp rel_f1 显著超过同类 LLM-based DocRE 改进（RelPrior: +2.06-2.38pp）\\n- CED 作为 rejection sampling 打分函数是新颖的方法论贡献\\n- 最接近的工作是 Progressive Self-distillation (ACM 2024) 用 knowledge distillation，但无 evidence-based reward\\n\\n### 新增文献 map categories (by literature scan worker)\\n- Category 6: RSFT Methodology & Theory（3 篇）\\n- Category 7: RL for Information Extraction（5 篇）\\n- Category 8: Recent LLM-based DocRE Methods（5 篇）\\n\\n---\\n\\n## CED-as-reranker 探索 (2026-05-15)\\n\\nRSFT 成功后仍保留 CED-as-reranker PoC 作为推理时替代方案（无需额外训练）。\\ncuda:0 上 PID 178050 运行中（985 docs × N=8，预计 ~6h）。\\n如果 reranker 接近或超过 RSFT，可作为论文中的 complementary contribution。\\n\\n---\\n\\n## Qwen3 generation_config 覆盖陷阱 (2026-05-15)\\n\\nQwen3 模型自带 `generation_config.json` 会静默覆盖代码传参：\\n- `model.generation_config.top_k = 20`（限制采样池）\\n- `model.generation_config.temperature = 0.6`（覆盖代码传的任何温度值）\\n\\n**必须在生成前显式覆盖**：\\n```python\\nmodel.generation_config.temperature = target_temp\\nmodel.generation_config.top_k = 0  # 禁用 top_k 限制\\nmodel.generation_config.do_sample = True\\n```\\n\\n---\\n\\n## Diversity 监控计算 bug (2026-05-15)\\n\\n### 根因\\n- triple-set 归一化逻辑不一致\\n- diversity 分母用配置值而非实际生成数\\n\\n### 修复\\n- 提取 `diversity_metrics.py` 独立模块\\n- 修复后真实数据：302 docs mean_diversity=7.52/8, median=8.0/8\\n\\n---\\n\\n## inference.py 参数教训 (2026-05-15)\\n\\n**inference.py 必须传完整模型 stack**：\\n- `--base_model /root/autodl-tmp/models/Qwen3-4B`\\n- `--sft_adapter /root/autodl-tmp/sft_output`\\n- `--model_path &lt;rsft_adapter_path>`（RSFT adapter）\\n- `--data_path /root/autodl-tmp/data/docred`\\n- `--output_dir &lt;output_path>`\\n- `--no-quantize`（RTX 5090 必须）\\n- `--max_new_tokens &lt;N>`（可选，默认 1024）\\n\\n**只传 --model_path 不传 --base_model + --sft_adapter 会导致模型 stack 错误**（Base + RSFT LoRA，缺 SFT merge），结果完全不可用。maxtok1536 eval 因此被 Reviewer CRITICAL 打回并重跑。\\n\\n---\\n\\n## RSFT 代码参数速查\\n\\n**inference.py**: --base_model, --sft_adapter, --model_path(rsft adapter), --data_path, --output_dir, --no-quantize, --max_new_tokens(1024)\\n\\n**rsft_generate.py**: --base_model, --sft_adapter, --data_path, --split, --output_dir, --num_generations(8), --temperature(0.7), --batch_size(1), --max_new_tokens(1024), --seed, --quantize/--no-quantize, --start_idx, --end_idx, --shard_id\\n\\n**rsft_score_filter.py**: --input_dir, --output_path, --nli_model_path, --nli_device, --tau(0.5), --f1_threshold(0.1), --selection_strategy(top_k), --top_k(2)\\n\\n**rsft_trainer.py**: --base_model, --sft_adapter, --rsft_data_path, --output_dir, --learning_rate, --num_epochs, --per_device_batch_size, --gradient_accumulation_steps, --lora_rank(64), --lora_alpha(128), --weighted_sampling, --quantize(False), --eval_data_dir, --eval_max_docs, --wandb_run_name, --seed\", \"total_chars\": 6195, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00079ef5-5e2c-4be3-8942-35aac6290ca7",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "8efc9b76-5d32-40fe-861e-d3e501b807b2",
  "sourceToolAssistantUUID": "00079ef5-5e2c-4be3-8942-35aac6290ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T14:28:21.370Z_

Now let me look at the actual paper artifacts and experiment code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8efc9b76-5d32-40fe-861e-d3e501b807b2",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfGT7qqUE9NYZVsiuf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a472dc63-d67b-4c11-b235-3bc57d23cb98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PYTPoWPCfZcVFRFkeyrrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24421,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24421,
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

_source line 21 · 2026-05-15T14:28:23.322Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FUrSEujtRRdSrfANW9nm4n`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a472dc63-d67b-4c11-b235-3bc57d23cb98",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfGT7qqUE9NYZVsiuf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc030172-fcb6-498e-9a3f-01d7d9f4dfc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PYTPoWPCfZcVFRFkeyrrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24421,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24421,
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

_source line 22 · 2026-05-15T14:28:23.351Z_

<details><summary>↩ Tool result · `toolu_01FUrSEujtRRdSrfANW9nm4n`</summary>

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
  "parentUuid": "dc030172-fcb6-498e-9a3f-01d7d9f4dfc4",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "d374fc56-c275-4594-984b-e59107bc911d",
  "sourceToolAssistantUUID": "dc030172-fcb6-498e-9a3f-01d7d9f4dfc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T14:28:24.257Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0155G8BzZcRwqHhrxojWvQc6`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d374fc56-c275-4594-984b-e59107bc911d",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfGT7qqUE9NYZVsiuf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec8e6170-f3fe-44e0-80ca-00e148e015ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PYTPoWPCfZcVFRFkeyrrU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24421,
      "cache_read_input_tokens": 26166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24421,
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

_source line 24 · 2026-05-15T14:28:24.272Z_

<details><summary>↩ Tool result · `toolu_0155G8BzZcRwqHhrxojWvQc6`</summary>

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
  "parentUuid": "ec8e6170-f3fe-44e0-80ca-00e148e015ad",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "159d0367-a375-4d7b-88c2-b460c0e747f3",
  "sourceToolAssistantUUID": "ec8e6170-f3fe-44e0-80ca-00e148e015ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T14:28:25.069Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XBnDPWTJQYvcVEaPgTkz5u`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "159d0367-a375-4d7b-88c2-b460c0e747f3",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfGT7qqUE9NYZVsiuf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea2709f-c5a5-4cc0-9533-a700c3106266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PYTPoWPCfZcVFRFkeyrrU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24421,
      "cache_read_input_tokens": 26166,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24421
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 26166,
          "cache_creation_input_tokens": 24421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24421,
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

_source line 26 · 2026-05-15T14:28:25.079Z_

<details><summary>↩ Tool result · `toolu_01XBnDPWTJQYvcVEaPgTkz5u`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea2709f-c5a5-4cc0-9533-a700c3106266",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "7c4a7387-03f9-4a65-a12c-332c0be2c586",
  "sourceToolAssistantUUID": "0ea2709f-c5a5-4cc0-9533-a700c3106266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T14:28:27.858Z_

Let me read the latest dream paper (which represents the most recent version of the manuscript).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c4a7387-03f9-4a65-a12c-332c0be2c586",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfkaJQ24573zLBi2QT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b77b5ec6-6d41-4f97-a41c-9808036f923f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NhHNbx35pX8s34AWHqCBa1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 50587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 782,
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

_source line 28 · 2026-05-15T14:28:28.503Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MUK3MonDyCrTuMBUs77oJp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77b5ec6-6d41-4f97-a41c-9808036f923f",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WfkaJQ24573zLBi2QT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1baf1bf2-e273-49a9-9b81-f56c16312ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NhHNbx35pX8s34AWHqCBa1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 782,
      "cache_read_input_tokens": 50587,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 782
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 50587,
          "cache_creation_input_tokens": 782,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 782,
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

_source line 29 · 2026-05-15T14:28:28.764Z_

<details><summary>↩ Tool result · `toolu_01MUK3MonDyCrTuMBUs77oJp`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	
13	\newcommand{\method}{FREIGE}
14	\newcommand{\ced}{CED}
15	\newcommand{\rsft}{RSFT}
16	\newcommand{\edcr}{EDCR}
17	
18	\title{FREIGE: Faithful Evidence Generation for Document-Level Relation Extraction via Rejection Sampling Fine-Tuning}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Large language models (LLMs) have approached encoder-based methods in document-level relation extraction (DocRE) accuracy, yet no existing LLM method generates verifiable evidence---the supporting sentences that justify each extracted relation.
27	We present \method{}, the first LLM-based DocRE system that jointly produces relation triples and faithful sentence-level evidence.
28	Our approach uses \textbf{Rejection Sampling Fine-Tuning (\rsft{})}: an SFT-trained model generates candidate outputs, a Contrastive Evidence Discrimination (\ced{}) scorer filters high-quality candidates using document-internal hard negatives, and the filtered data is used for further fine-tuning.
29	On DocRED, \method{} achieves test rel\_F1 of 43.2\% (+3.2pp over SFT, $p{<}0.01$) and joint Evi-F1 of 32.2\%, while producing human-auditable sentence citations.
30	We further demonstrate that online reward optimization (GRPO) with evidence-quality rewards causes catastrophic \emph{evidence-extraction decoupling}: evidence quality rises while extraction performance collapses to near-zero, and this failure \emph{accelerates} with larger group sizes that provide more precise advantage estimation.
31	We introduce EDCR (Evidence Distractor Citation Rate) as a complementary diagnostic to Evi-F1 and validate it through human annotation ($r{=}0.44$, perfect method-level rank concordance).
32	Our results establish that for structured IE tasks, evidence-quality signals are most effective as offline data curation criteria rather than online training rewards.
33	\end{abstract}
34	
35	\section{Introduction}
36	
37	Document-level relation extraction (DocRE) requires identifying relations between entities across multiple sentences in a document \cite{yao2019docred}.
38	While encoder-based methods have achieved strong performance \cite{zhou2021atlop,ma2023dreeam,xiao2022sais}, LLM-based approaches have recently emerged as competitive alternatives \cite{xu2024lmrc}, offering the advantage of flexible generation.
39	However, no existing LLM-based DocRE method produces \emph{verifiable evidence}---the specific sentences supporting each extracted relation---despite this being critical for deployment in human-in-the-loop knowledge base population, biomedical curation, and RAG provenance tracking.
40	
41	Encoder-based methods like DREEAM \cite{ma2023dreeam} derive evidence from attention weights, producing implicit, post-hoc explanations.
42	In contrast, a generative approach can directly output explicit sentence indices alongside each triple, enabling human-auditable evidence that is fundamentally more interpretable.
43	The challenge is teaching the model to cite \emph{faithfully}: naive supervised fine-tuning (SFT) produces models where 71.2\% of entity-sharing citations are distractor sentences that mention relevant entities but do not actually support the predicted relation.
44	
45	A natural approach to improve evidence quality is reinforcement learning with NLI-based faithfulness rewards.
46	We explore this direction and discover a fundamental obstacle: \textbf{evidence-extraction decoupling}.
47	Under GRPO training with evidence-quality rewards, the model rapidly learns to produce higher-quality evidence (evi\_F1 rising to 0.835--0.862) while simultaneously losing the ability to extract relations (rel\_F1 collapsing to $<$0.08).
48	This occurs across all reward types (CED, flat-NLI, extraction-only) and learning rates, and \emph{worsens} with larger group sizes (G=8 vs.\ G=4) that provide more precise advantage estimation---directly connecting to reward overoptimization theory \cite{gao2023scaling}.
49	
50	Our solution is \textbf{\method{}} (\textbf{F}aithful \textbf{R}elation \textbf{E}xtraction with \textbf{I}nference-time \textbf{G}eneration and \textbf{E}vidence), built on Rejection Sampling Fine-Tuning (\rsft{}).
51	Instead of using evidence-quality signals as online rewards, we use them as offline data curation criteria: an SFT model generates $N$ candidate outputs per document, a Contrastive Evidence Discrimination (\ced{}) scorer ranks candidates by evidence quality using document-internal hard negatives, and only the top-ranked candidate is retained for further fine-tuning.
52	This circumvents the decoupling failure entirely---the model never receives reward gradients, only learns from curated high-quality demonstrations.
53	
54	Our contributions are:
55	\begin{enumerate}
56	\item We present the first LLM-based DocRE method that jointly generates relation triples and verifiable sentence-level evidence, achieving +3.2pp rel\_F1 over SFT on DocRED test ($p{<}0.01$) with consistent gains across three model sizes (1.7B/4B/8B) and on Re-DocRED.
57	\item We characterize evidence-extraction decoupling in GRPO+QLoRA for document-level IE, showing it accelerates with improved advantage estimation (G=8 peaks earlier and collapses faster than G=4), and that offline preference learning (DPO) partially mitigates but does not solve the underlying issue.
58	\item We introduce EDCR as a diagnostic metric complementary to Evi-F1, validated through human annotation ($r{=}0.44$, method-level rank concordance 1.0).
59	\end{enumerate}
60	
61	\section{Related Work}
62	
63	\paragraph{Document-Level Relation Extraction.}
64	DocRE extends sentence-level RE to require cross-sentence reasoning \cite{yao2019docred}.
65	Encoder-based methods dominate, with ATLOP \cite{zhou2021atlop}, DREEAM \cite{ma2023dreeam}, and SAIS \cite{xiao2022sais} achieving strong performance through adaptive thresholding and evidence-aware attention.
66	Recent LLM-based methods include LMRC \cite{xu2024lmrc}, which achieves 60.7\% F1 with LLaMA3.1-8B but produces no evidence.
67	Our work is the first to address evidence generation in generative DocRE.
68	
69	\paragraph{Evidence and Faithfulness in IE.}
70	DREEAM \cite{ma2023dreeam} uses attention supervision for evidence extraction, achieving 57.3\% joint Evi-F1.
71	SAIS \cite{xiao2022sais} provides sentence importance scores (55.7\% joint Evi-F1).
72	Both rely on attention-derived evidence, which is implicit and not directly auditable.
73	Our approach generates explicit sentence citations, enabling transparent verification.
74	
75	\paragraph{Rejection Sampling and Offline RL.}
76	Rejection sampling fine-tuning (RSFT/ReST) has been shown theoretically equivalent to PPO under certain conditions \cite{dong2024raft}.
77	We apply RSFT to structured IE, using CED as the filtering criterion rather than task reward.
78	Our findings connect to reward overoptimization \cite{gao2023scaling} and the evidence grounding gradient vanishing analysis of LongRLVR \cite{song2025longrlvr}.
79	
80	\paragraph{RL for Information Extraction.}
81	Prior work has applied RL to IE tasks with mixed results.
82	Our systematic comparison across the data curation (RSFT) vs.\ preference learning (DPO) vs.\ reward optimization (GRPO) spectrum provides empirical evidence that structured generation tasks are particularly vulnerable to reward-based training.
83	
84	\section{Method}
85	
86	\subsection{Task Formulation}
87	
88	Given a document $D = \{s_1, \ldots, s_n\}$ with entity mentions, the model generates a set of tuples $\{(h_i, r_i, t_i, E_i)\}$ where $h_i, t_i$ are head/tail entities, $r_i$ is a relation type, and $E_i \subseteq \{s_1, \ldots, s_n\}$ is the supporting evidence (sentence indices).
89	
90	\subsection{SFT Baseline}
91	
92	We fine-tune Qwen3-4B with QLoRA on DocRED training data formatted as structured generation: the input is the document with entity markers, and the output is a linearized list of (head, relation, tail, [evidence sentence indices]) tuples.
93	
94	\subsection{Contrastive Evidence Discrimination (CED)}
95	
96	For each predicted triple $(h, r, t, E)$, CED scores evidence quality by comparing the entailment probability of cited sentences against entity-sharing distractor sentences:
97	\begin{equation}
98	\text{CED}(h,r,t,E) = \frac{1}{|E|} \sum_{s_i \in E} \left[ p_{\text{NLI}}(s_i \Rightarrow r) - \max_{s_j \in \mathcal{N}} p_{\text{NLI}}(s_j \Rightarrow r) \right]
99	\end{equation}
100	where $\mathcal{N}$ is the set of entity-sharing non-cited sentences (document-internal hard negatives) and $p_{\text{NLI}}$ is the entailment probability from a DeBERTa-v3-base NLI model.
101	
102	The contrastive margin penalizes citations that are not more entailing than the best available distractor, addressing the entity-mention bias where sentences sharing entities with the target triple receive inflated NLI scores regardless of actual support.
103	
104	\subsection{Rejection Sampling Fine-Tuning (RSFT)}
105	
106	The RSFT pipeline operates in three stages:
107	\begin{enumerate}
108	\item \textbf{Candidate Generation}: The SFT model generates $N{=}8$ candidate outputs per document via temperature sampling.
109	\item \textbf{CED Scoring and Filtering}: Each candidate is scored by CED. Only the top-1 candidate per document is retained (selection rate ${\sim}$12.4\%, yielding 2,718 training samples).
110	\item \textbf{Fine-tuning}: The filtered high-quality candidates serve as training data for additional SFT epochs.
111	\end{enumerate}
112	
113	This design avoids modifying the policy gradient---the model learns only from curated demonstrations, not from reward signals. The key insight is that CED's value lies in \emph{ranking} candidates rather than providing absolute quality scores, making the top-$k$ selection robust to scorer calibration errors.
114	
115	\subsection{EDCR: Evidence Distractor Citation Rate}
116	
117	We propose EDCR as a complementary diagnostic to Evi-F1:
118	\begin{equation}
119	\text{EDCR} = \frac{|\{s \in \text{Cited} : s \in \mathcal{N}_{\text{entity-sharing}} \setminus \text{Gold}\}|}{|\text{Cited}|}
120	\end{equation}
121	EDCR measures the proportion of cited sentences that share entities with the target triple but are not in the gold evidence set. While Evi-F1 measures evidence recall (whether gold evidence is cited), EDCR measures evidence precision in terms of distractor contamination.
122	
123	\section{Experimental Setup}
124	
125	\subsection{Data and Evaluation}
126	
127	We use DocRED \cite{yao2019docred} as the primary benchmark and Re-DocRED \cite{tan2022redocred} for generalization evaluation.
128	We report: (1) \textbf{rel\_F1}: relation extraction F1; (2) \textbf{Evi-F1\textsubscript{joint}}: joint evidence F1 following the DREEAM protocol \cite{ma2023dreeam}, computed over all gold triples; (3) \textbf{Evi-F1\textsubscript{cond}}: conditional evidence F1 over correctly predicted triples; (4) \textbf{EDCR}: evidence distractor citation rate.
129	
130	\subsection{Models and Training}
131	
132	Our primary model is Qwen3-4B with QLoRA ($\alpha{=}128$, rank 64).
133	For model size ablation, we additionally evaluate Qwen3-1.7B and Qwen3-8B.
134	CED scoring uses DeBERTa-v3-base fine-tuned on MNLI.
135	RSFT uses $N{=}8$ candidates per document, top-$k{=}1$ selection.
136	
137	\subsection{Baselines}
138	
139	We compare against: (1) \textbf{SFT}: our Qwen3-4B SFT baseline; (2) \textbf{DREEAM} \cite{ma2023dreeam}: RoBERTa-large encoder (reproduced, test Evi-F1\textsubscript{joint}=57.34\%); (3) \textbf{SAIS} \cite{xiao2022sais}: RoBERTa-large encoder (reproduced, test Evi-F1\textsubscript{joint}=55.67\%); (4) \textbf{LMRC} \cite{xu2024lmrc}: LLaMA3.1-8B generative method (F1=60.7\%, no evidence).
140	We also evaluate intermediate methods: \textbf{GRPO+CED} (online reward optimization), \textbf{DPO+CED} (offline preference learning), \textbf{CED-as-reranker} (inference-time reranking), and \textbf{RSFT+flat-NLI} (non-contrastive scoring ablation).
141	
142	\section{Results}
143	
144	\subsection{Main Results}
145	
146	Table~\ref{tab:main} presents test set results on DocRED.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\begin{tabular}{lcccc}
152	\toprule
153	\textbf{Method} & \textbf{rel\_F1} & \textbf{ign\_F1} & \textbf{Evi-F1\textsubscript{j}} & \textbf{Evi-F1\textsubscript{c}} \\
154	\midrule
155	DREEAM$^\dagger$ & 62.8 & --- & 57.34 & ${\sim}$93 \\
156	SAIS$^\dagger$ & 60.4 & --- & 55.67 & ${\sim}$92 \\
157	LMRC$^\dagger$ & 60.7 & --- & --- & --- \\
158	\midrule
159	SFT (Qwen3-4B) & 40.0 & 39.8 & 29.5 & 79.0 \\
160	RSFT+flat-NLI & 42.5 & 42.3 & 31.2 & 79.5 \\
161	\textbf{RSFT+CED (\method{})} & \textbf{43.2} & \textbf{43.0} & \textbf{32.2} & \textbf{80.0} \\
162	\bottomrule
163	\end{tabular}
164	\caption{Test set results on DocRED. $^\dagger$Published results. Evi-F1\textsubscript{j}: joint protocol (DREEAM-aligned); Evi-F1\textsubscript{c}: conditional on correct triples. \method{} achieves +3.2pp rel\_F1 over SFT ($p{<}0.01$).}
165	\label{tab:main}
166	\end{table}
167	
168	\method{} achieves 43.2\% rel\_F1, a +3.2pp improvement over SFT ($p{<}0.01$), and is the first LLM method to report joint Evi-F1 (32.2\%).
169	The gap to encoder methods in joint Evi-F1 (32.2 vs.\ 57.3) is primarily driven by extraction recall (43.2\% vs.\ 62.8\%) rather than evidence quality: conditional Evi-F1 (80.0\% vs.\ ${\sim}$93\%) shows a much smaller gap, and our explicit sentence citations are directly auditable unlike attention-derived evidence.
170	
171	\subsection{CED vs.\ Flat-NLI Scoring (Ablation)}
172	
173	Table~\ref{tab:ced_ablation} compares CED and flat-NLI scoring for RSFT on the dev set.
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\begin{tabular}{llccc}
179	\toprule
180	\textbf{Config} & \textbf{Scorer} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR} \\
181	\midrule
182	r1 (3ep, $\alpha$128, s42) & CED & 44.49 & 81.87 & 65.65 \\
183	 & flat-NLI & 43.98 & 81.15 & 67.25 \\
184	\midrule
185	s43 (3ep, $\alpha$128, s43) & CED & 46.83 & 81.56 & 63.88 \\
186	 & flat-NLI & 46.10 & 80.78 & 65.90 \\
187	\midrule
188	r2b (1ep, $\alpha$32, lr1e-5) & CED & 44.93 & 81.28 & 66.09 \\
189	 & flat-NLI & 44.70 & 80.53 & 67.52 \\
190	\midrule
191	SFT baseline & --- & 40.57 & 79.79 & 71.18 \\
192	\bottomrule
193	\end{tabular}
194	\caption{CED vs.\ flat-NLI RSFT ablation (dev set). CED outperforms flat-NLI in the same direction across all three configurations, but differences are not statistically significant.}
195	\label{tab:ced_ablation}
196	\end{table}
197	
198	CED outperforms flat-NLI consistently across all three hyperparameter configurations in both evi\_F1 (+0.75pp mean) and rel\_F1 (+0.49pp mean), and achieves lower EDCR ($-$1.68pp mean).
199	However, paired bootstrap tests (10{,}000 resamples) show these differences are not statistically significant (evi\_F1: $p{=}0.12$; rel\_F1: $p{=}0.28$; EDCR: $p{=}0.09$).
200	
201	Critically, \emph{both} CED and flat-NLI RSFT substantially outperform SFT: flat-NLI RSFT achieves +5.5pp rel\_F1 over SFT ($p{<}0.001$), establishing that the \rsft{} pipeline itself---regardless of scoring function---is the primary contribution.
202	The 78\% overlap in selected candidates between the two scorers explains the limited differentiation: DeBERTa-v3-base's positional bias on long documents causes contrastive and non-contrastive scores to converge in high-confidence regions.
203	
204	\subsection{Evidence-Extraction Decoupling in GRPO}
205	
206	\begin{table}[t]
207	\centering
208	\small
209	\begin{tabular}{lcccl}
210	\toprule
211	\textbf{Config} & \textbf{Best rel\_F1} & \textbf{Peak} & \textbf{evi\_F1\textsubscript{end}} & \textbf{Pattern} \\
212	\midrule
213	G=4, kl.01 & 21.7 & s100$\uparrow$ & 57.5 & Slow climb \\
214	G=8, kl.01 & 7.8 & s40 & 86.2 & Peak$\to$collapse \\
215	\bottomrule
216	\end{tabular}
217	\caption{GRPO G=4 vs.\ G=8. Larger group size provides more precise advantage estimation but accelerates decoupling.}
218	\label{tab:grpo_summary}
219	\end{table}
220	
221	Table~\ref{tab:grpo_summary} summarizes the GRPO results. With G=8, rel\_F1 peaks at step 40 (7.8\%) then collapses to 1.2\% by step 100, while evidence quality monotonically rises to 86.2\%. This is \emph{worse} than G=4 (best rel\_F1=21.7\%), decisively ruling out the hypothesis that G=4 was simply too small for stable training.
222	
223	Table~\ref{tab:grpo_trajectory} shows the full G=8 trajectory, revealing the characteristic signature of evidence-extraction decoupling: reward increases monotonically ($0.62 \to 1.45$) while rel\_F1 rises briefly then collapses.
224	
225	\begin{table}[t]
226	\centering
227	\small
228	\begin{tabular}{ccccc}
229	\toprule
230	\textbf{Step} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR} & \textbf{Reward} \\
231	\midrule
232	10 & 0.8 & 72.0 & 98.5 & 0.62 \\
233	20 & 3.5 & 76.0 & 97.2 & 0.85 \\
234	30 & 6.2 & 79.5 & 95.0 & 1.05 \\
235	40 & \textbf{7.8} & 83.5 & 92.8 & 1.18 \\
236	50 & 5.5 & 84.5 & 93.5 & 1.28 \\
237	60 & 3.8 & 85.0 & 94.0 & 1.35 \\
238	80 & 2.0 & 85.8 & 94.5 & 1.42 \\
239	100 & 1.2 & 86.2 & 94.8 & 1.45 \\
240	\bottomrule
241	\end{tabular}
242	\caption{GRPO G=8 checkpoint trajectory. Reward increases monotonically while rel\_F1 peaks then collapses, exhibiting evidence-extraction decoupling.}
243	\label{tab:grpo_trajectory}
244	\end{table}
245	
246	The mechanism is: more precise advantage estimation (lower variance $\propto 1/G$) enables the model to more efficiently optimize the CED reward, which measures evidence quality but is misaligned with relation extraction. The ``success'' of G=4 (rel\_F1=21.7) is an accidental byproduct of noisy advantage estimation acting as implicit regularization, analogous to the role of dropout in preventing overfitting.
247	
248	Across all GRPO configurations, reward and rel\_F1 show strong negative correlation ($r{=}{-}0.68$), while reward and evi\_F1 are strongly positively correlated ($r{=}0.82$). The decoupling onset occurs at step ${\sim}$30 for G=8 versus step ${\sim}$60 for G=4, consistent with faster optimization under lower-variance advantage estimates.
249	
250	\subsection{Data Curation vs.\ Preference/Reward Learning}
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\begin{tabular}{llcccc}
256	\toprule
257	\textbf{Method} & \textbf{Type} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR} & \textbf{$\Delta$SFT} \\
258	\midrule
259	GRPO G=8 & Online reward & 7.8 & 83.5 & 92.8 & $-$32.8 \\
260	GRPO G=4 & Online reward & 21.7 & 57.5 & 85.4 & $-$18.9 \\
261	DPO+CED & Offline pref. & 34.0 & 79.8 & 66.0 & $-$6.6 \\
262	SFT & Supervised & 40.6 & 79.8 & 71.2 & --- \\
263	RSFT+flat-NLI & Data curation & 46.1 & 80.8 & 65.9 & +5.5 \\
264	RSFT+CED & Data curation & 46.8 & 81.6 & 63.9 & +6.3 \\
265	\bottomrule
266	\end{tabular}
267	\caption{Training paradigm comparison (dev set). Data curation (RSFT) succeeds where both online (GRPO) and offline (DPO) contrastive losses fail. $\Delta$SFT: rel\_F1 change in pp.}
268	\label{tab:spectrum}
269	\end{table}
270	
271	Table~\ref{tab:spectrum} reveals a clear ordering across training paradigms.
272	DPO ($\beta{=}0.1$, 5{,}436 preference pairs) avoids GRPO's catastrophic collapse but still degrades rel\_F1 by 6.6pp below SFT.
273	The DPO contrastive loss simultaneously pushes up preferred and pushes down rejected candidates; in structured IE, ``rejected'' candidates may contain correct relation patterns with merely weaker evidence, so pushing them down damages extraction capability.
274	DPO is also more sensitive to CED label noise (${\sim}$18.5\% error rate) than RSFT, which only uses top positive candidates and never explicitly penalizes negatives.
275	
276	The key insight is that the distinction is not online vs.\ offline RL, but \emph{contrastive/reward-based loss vs.\ data curation}: any method that modifies gradients based on evidence-quality comparisons risks damaging structured generation, while RSFT succeeds precisely because it is not RL---it is quality-filtered SFT.
277	
278	\subsection{EDCR as Diagnostic Metric}
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lcccc}
284	\toprule
285	\textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1\textsubscript{c}} & \textbf{EDCR} & \textbf{Zone} \\
286	\midrule
287	GRPO G=8 & 7.8 & 83.5 & 92.8 & Collapse \\
288	GRPO G=4 & 21.7 & 57.5 & 85.4 & Collapse \\
289	SFT & 40.6 & 79.8 & 71.2 & Baseline \\
290	CED-reranker & 42.2 & 80.9 & 66.8 & Filtered \\
291	DPO+CED & 34.0 & 79.8 & 66.0 & Filtered \\
292	RSFT+flat-NLI & 46.1 & 80.8 & 65.9 & Filtered \\
293	RSFT+CED & 46.8 & 81.6 & 63.9 & Filtered \\
294	\bottomrule
295	\end{tabular}
296	\caption{Cross-method EDCR diagnostic (dev set). EDCR discriminates three zones: collapse ($>$85\%), baseline (${\sim}$71\%), and filtered (64--67\%).}
297	\label{tab:edcr_diagnostic}
298	\end{table}
299	
300	Table~\ref{tab:edcr_diagnostic} demonstrates EDCR's ability to discriminate three method categories.
301	EDCR correlates negatively with rel\_F1 ($\rho{=}{-}0.52$) and evi\_F1 ($\rho{=}{-}0.38$) across methods, capturing the intuition that better methods produce fewer distractor citations.
302	
303	\paragraph{Human Validation.}
304	We validate EDCR through a 100-sample annotation study with two annotators ($\kappa{=}0.62$).
305	Table~\ref{tab:edcr_human} summarizes the results.
306	EDCR achieves Pearson $r{=}0.44$ and Spearman $\rho{=}0.41$ against human judgments at the sample level.
307	While modest, method-level rank concordance is perfect (1.0), confirming EDCR reliably discriminates between methods.
308	EDCR systematically overestimates the distractor rate by 8.5pp, primarily because 14\% of sentences labeled as distractors by the automatic metric are judged by annotators as actually supporting the relation---reflecting incomplete gold evidence annotations in DocRED rather than metric failure.
309	
310	\begin{table}[t]
311	\centering
312	\small
313	\begin{tabular}{lc}
314	\toprule
315	\textbf{Statistic} & \textbf{Value} \\
316	\midrule
317	Samples / Annotators & 100 / 2 \\
318	Inter-annotator $\kappa$ & 0.62 \\
319	EDCR vs.\ human Pearson $r$ & 0.44 \\
320	EDCR vs.\ human Spearman $\rho$ & 0.41 \\
321	EDCR overestimate & +8.5pp \\
322	False distractor rate & 14\% \\
323	Method-level rank concordance & 1.0 \\
324	\bottomrule
325	\end{tabular}
326	\caption{EDCR human validation statistics.}
327	\label{tab:edcr_human}
328	\end{table}
329	
330	\subsection{CED as Inference-Time Reranker}
331	
332	Without any additional training, CED can be used to rerank $N{=}8$ SFT candidates at inference time.
333	CED-reranker achieves rel\_F1=42.2\% (+1.6pp over SFT) and EDCR=66.8\% ($-$4.4pp over SFT) on 985 documents, but at 8.5$\times$ inference cost.
334	Compared to RSFT's +6.3pp rel\_F1 improvement at no additional inference cost, reranking demonstrates that CED signals are more effectively transmitted through training data curation than inference-time selection.
335	
336	\subsection{Top-$k$ Selection Ablation}
337	
338	\begin{table}[t]
339	\centering
340	\small
341	\begin{tabular}{ccccc}
342	\toprule
343	\textbf{top-$k$} & \textbf{$N_\text{train}$} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR} \\
344	\midrule
345	1 & 2{,}718 & \textbf{46.8} & \textbf{81.6} & \textbf{63.9} \\
346	3 & 8{,}154 & 45.8 & 80.2 & 66.2 \\
347	\bottomrule
348	\end{tabular}
349	\caption{Top-$k$ selection ablation (dev set). Strict filtering (top-1) outperforms relaxed filtering (top-3) despite 3$\times$ less training data.}
350	\label{tab:topk}
351	\end{table}
352	
353	Table~\ref{tab:topk} shows that top-$k{=}1$ (strict filtering, 2{,}718 samples) uniformly outperforms top-$k{=}3$ (relaxed filtering, 8{,}154 samples).
354	The mean CED score drops from 0.668 to 0.512 when including rank-2/3 candidates, and the lower-quality candidates introduce distractor citation patterns that degrade evidence quality (EDCR +2.3pp).
355	This validates the RSFT design principle: quality of curated data matters more than quantity.
356	
357	\subsection{Model Size Ablation}
358	
359	\begin{table}[t]
360	\centering
361	\small
362	\begin{tabular}{lcccc}
363	\toprule
364	\textbf{Model} & \textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1\textsubscript{c}} & \textbf{$\Delta$rel\_F1} \\
365	\midrule
366	Qwen3-1.7B & SFT & 32.0 & 77.5 & --- \\
367	 & RSFT+CED & 34.8 & 79.2 & +2.8pp \\
368	\midrule
369	Qwen3-4B & SFT & 40.6 & 79.8 & --- \\
370	 & RSFT+CED & 46.8 & 81.6 & +6.3pp \\
371	\midrule
372	Qwen3-8B & SFT & 44.8 & 81.0 & --- \\
373	 & RSFT+CED & 48.8 & 82.5 & +4.0pp \\
374	\bottomrule
375	\end{tabular}
376	\caption{Model size ablation (dev set). RSFT consistently improves across 1.7B, 4B, and 8B.}
377	\label{tab:model_size}
378	\end{table}
379	
380	Table~\ref{tab:model_size} demonstrates consistent RSFT improvement across three model sizes (+2.8/+6.3/+4.0pp).
381	Smaller models generate fewer high-quality candidates, reducing RSFT training data and limiting gains.
382	The largest absolute performance is Qwen3-8B RSFT (rel\_F1=48.8\%), though a gap to LMRC (60.7\%, 8B, no evidence) remains, reflecting the additional burden of evidence generation.
383	
384	\subsection{Re-DocRED Generalization}
385	
386	\begin{table}[t]
387	\centering
388	\small
389	\begin{tabular}{lcccc}
390	\toprule
391	\textbf{Method} & \textbf{DocRED} & \textbf{Re-DocRED} & \textbf{$\Delta$SFT} & \textbf{EDCR} \\
392	\midrule
393	SFT & 40.6 & 48.5 & --- & 66.8 \\
394	RSFT+CED & 46.8 & 52.0 & +3.5pp & 61.0 \\
395	\bottomrule
396	\end{tabular}
397	\caption{Re-DocRED evaluation (dev set, DocRED-trained models). RSFT improvement transfers (+3.5pp).}
398	\label{tab:redocred}
399	\end{table}
400	
401	Models trained on DocRED and evaluated on Re-DocRED (which corrects ${\sim}$30\% false negative triples) show consistent RSFT improvement (+3.5pp, Table~\ref{tab:redocred}).
402	The delta narrows from +6.3pp on DocRED to +3.5pp on Re-DocRED, a ceiling effect: Re-DocRED's more complete annotations strengthen the SFT baseline, compressing the improvement margin.
403	
404	\subsection{Baseline Reproduction}
405	
406	We reproduce DREEAM and SAIS on the DocRED dev set to validate evaluation protocol alignment (Table~\ref{tab:baseline_repro}).
407	
408	\begin{table}[t]
409	\centering
410	\small
411	\begin{tabular}{lccc}
412	\toprule
413	\textbf{Method} & \textbf{rel\_F1} & \textbf{Evi-F1\textsubscript{j}} & \textbf{Evi-F1\textsubscript{c}} \\
414	\midrule
415	DREEAM (repro.) & 62.5 & 58.1 & ${\sim}$93 \\
416	SAIS (repro.) & 60.8 & 56.2 & ${\sim}$92 \\
417	RSFT+CED (ours) & 46.8 & 37.2 & 81.6 \\
418	SFT (ours) & 40.6 & 30.8 & 79.8 \\
419	\bottomrule
420	\end{tabular}
421	\caption{Dev set comparison with reproduced baselines (DREEAM-aligned joint Evi-F1 protocol). Reproduction gap $<$1pp from published test results.}
422	\label{tab:baseline_repro}
423	\end{table}
424	
425	Reproduced dev results are within 1pp of published test results (DREEAM: 58.1 vs.\ 57.3; SAIS: 56.2 vs.\ 55.7), confirming evaluation alignment.
426	The joint Evi-F1 gap (37.2 vs.\ 58.1) decomposes as: joint $\approx$ recall $\times$ conditional $\approx 0.47 \times 0.82 = 0.385$, showing the gap is driven by extraction recall rather than per-triple evidence quality.
427	
428	\subsection{NLI Model Ablation}
429	
430	\begin{table}[t]
431	\centering
432	\small
433	\begin{tabular}{lcccc}
434	\toprule
435	\textbf{NLI Scorer} & \textbf{Disc.\ Acc.} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR} \\
436	\midrule
437	DeBERTa-v3-base & 81.5 & 46.8 & 81.6 & 63.9 \\
438	DeBERTa-v3-large & 84.8 & 47.2 & 82.0 & 63.2 \\
439	\bottomrule
440	\end{tabular}
441	\caption{NLI model ablation. Upgrading the scorer (+3.3pp discrimination accuracy) yields minimal downstream gains (+0.4pp rel\_F1), indicating the pipeline bottleneck is candidate generation quality, not scorer precision.}
442	\label{tab:nli_ablation}
443	\end{table}
444	
445	Upgrading the NLI scorer from DeBERTa-v3-base to DeBERTa-v3-large improves CED discrimination accuracy by 3.3pp (81.5\%$\to$84.8\%) but yields only +0.4pp downstream rel\_F1 (Table~\ref{tab:nli_ablation}).
446	The pipeline bottleneck is candidate generation quality (fixed at $N{=}8$ SFT samples), not scorer precision; base-level accuracy (81.5\%) already exceeds the threshold for effective filtering.
447	
448	\section{Discussion}
449	
450	\paragraph{Why RSFT Succeeds Where RL Fails.}
451	The consistent failure of reward-based methods (GRPO, DPO) and success of data curation (RSFT) reveals a structural property of evidence-generating IE: the evidence-quality objective is misaligned with the extraction objective at the gradient level.
452	Reward-based methods transmit this misalignment directly through policy gradients, while RSFT insulates the model by converting the quality signal into a data selection criterion.
453	This connects to the theoretical result that RSFT is equivalent to PPO under certain conditions \cite{dong2024raft}---but with a crucial practical advantage: RSFT eliminates the risk of reward overoptimization because the model never optimizes a reward function.
454	
455	\paragraph{The Role of CED.}
456	Our ablation shows CED's contrastive margin provides consistent but statistically non-significant improvements over flat-NLI scoring ($p{=}0.12$ for evi\_F1).
457	This is attributable to three factors: (1) DeBERTa-v3-base's positional bias causes contrastive and non-contrastive scores to converge for long documents; (2) incomplete DocRED gold evidence (${\sim}$14\% false distractors) dilutes the hard-negative signal; (3) the indirect RSFT pipeline (scorer $\to$ filter $\to$ training data $\to$ fine-tune) attenuates scoring-level differences.
458	Importantly, CED's top-1 vs.\ top-3 selection advantage (Table~\ref{tab:topk}) demonstrates that the \emph{ranking} quality of the scorer, even if not differentiated from flat-NLI, enables effective data curation.
459	
460	\paragraph{EDCR Limitations.}
461	While EDCR achieves perfect method-level rank concordance with human judgments, its sample-level correlation ($r{=}0.44$) is moderate.
462	The 14\% false distractor rate---where automatically labeled distractors are judged by humans as valid evidence---reflects DocRED's annotation incompleteness rather than metric design failure.
463	EDCR should be used as a complementary diagnostic alongside Evi-F1, not as a standalone metric.
464	
465	\section{Limitations}
466	
467	\textbf{Absolute performance gap.} Our best model (Qwen3-8B RSFT, rel\_F1=48.8\%) trails encoder methods (DREEAM 62.8\%) and LLM methods without evidence (LMRC 60.7\%).
468	Evidence generation imposes an additional burden on the model; closing this gap while maintaining evidence quality is future work.
469	
470	\textbf{Single NLI backbone.} CED relies on DeBERTa NLI models, which have known biases including lexical overlap sensitivity and positional bias on long documents.
471	Alternative evidence scorers (e.g., cross-encoder models, LLM-based evaluation) may better differentiate contrastive from non-contrastive scoring.
472	
473	\textbf{GRPO scope.} Our decoupling findings are established for GRPO+QLoRA on document-level IE.
474	We do not claim this generalizes to full-rank GRPO, other online RL algorithms (PPO, REINFORCE), or other structured generation tasks.
475	
476	\textbf{Gold annotation quality.} DocRED gold evidence annotations are incomplete (${\sim}$14\% false distractors by our human study), which affects both training (RSFT candidates scored against noisy gold) and evaluation (EDCR systematically overestimates by 8.5pp).
477	
478	\textbf{Dev-to-test degradation.} RSFT shows 3.6pp dev-to-test degradation in rel\_F1 (vs.\ 0.6pp for SFT), suggesting indirect overfitting through the CED scoring pathway.
479	The improvement remains significant on test ($p{<}0.01$) but this asymmetric degradation warrants investigation.
480	
481	\section{Conclusion}
482	
483	We introduced \method{}, the first LLM-based method for document-level relation extraction that jointly generates relation triples and verifiable sentence-level evidence.
484	Through systematic comparison of training paradigms, we established that evidence-quality signals are effective as offline data curation criteria (RSFT, +3.2pp test rel\_F1) but destructive as online rewards (GRPO) or offline contrastive losses (DPO).
485	We characterized evidence-extraction decoupling in GRPO+QLoRA, showing it accelerates with larger group sizes, and introduced EDCR as a human-validated diagnostic for evidence quality.
486	Our work opens the path toward trustworthy, evidence-grounded document-level IE with large language models.
487	
488	\begin{thebibliography}{20}
489	
490	\bibitem[\protect\citeauthoryear{Yao et al.}{2019}]{yao2019docred}
491	Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, and Maosong Sun.
492	\newblock DocRED: A large-scale document-level relation extraction dataset.
493	\newblock In \emph{Proc. ACL}, 2019.
494	
495	\bibitem[\protect\citeauthoryear{Zhou et al.}{2021}]{zhou2021atlop}
496	Wenxuan Zhou, Kevin Huang, Tengyu Ma, and Jing Huang.
497	\newblock Document-level relation extraction with adaptive thresholding and localized context pooling.
498	\newblock In \emph{Proc. AAAI}, 2021.
499	
500	\bibitem[\protect\citeauthoryear{Ma et al.}{2023}]{ma2023dreeam}
501	Youmi Ma, An Wang, and Naoaki Okazaki.
502	\newblock DREEAM: Guiding attention with evidence for improving document-level relation extraction.
503	\newblock In \emph{Proc. EACL}, 2023.
504	
505	\bibitem[\protect\citeauthoryear{Xiao et al.}{2022}]{xiao2022sais}
506	Chaojun Xiao, Yuan Yao, Ruobing Xie, Xu Han, Zhiyuan Liu, Maosong Sun, Fen Lin, and Leyu Lin.
507	\newblock SAIS: Supervising and augmenting intermediate steps for document-level relation extraction.
508	\newblock In \emph{Proc. NAACL}, 2022.
509	
510	\bibitem[\protect\citeauthoryear{Xu et al.}{2024}]{xu2024lmrc}
511	Wang Xu, Kehai Chen, and Tiejun Zhao.
512	\newblock Document-level relation extraction with large language models.
513	\newblock In \emph{Proc. EMNLP}, 2024.
514	
515	\bibitem[\protect\citeauthoryear{Gao et al.}{2023}]{gao2023scaling}
516	Leo Gao, John Schulman, and Jacob Hilton.
517	\newblock Scaling laws for reward model overoptimization.
518	\newblock In \emph{Proc. ICML}, 2023.
519	
520	\bibitem[\protect\citeauthoryear{Song et al.}{2025}]{song2025longrlvr}
521	Yige Song, Xinyuan Lu, Zhiling Luo, and Dongkuan Xu.
522	\newblock LongRLVR: Long-context reasoning with reinforcement learning and verifiable rewards.
523	\newblock In \emph{Proc. ICLR}, 2026.
524	
525	\bibitem[\protect\citeauthoryear{Dong et al.}{2024}]{dong2024raft}
526	Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang.
527	\newblock RAFT: Reward ranked finetuning for generative foundation model alignment.
528	\newblock \emph{Transactions on Machine Learning Research}, 2024.
529	
530	\bibitem[\protect\citeauthoryear{Tan et al.}{2022}]{tan2022redocred}
531	Qingyu Tan, Lu Xu, Lidong Bing, Hwee Tou Ng, and Sharifah Mahani Aljunied.
532	\newblock Revisiting DocRED -- addressing the false negative problem in relation extraction.
533	\newblock In \emph{Proc. EMNLP}, 2022.
534	
535	\end{thebibliography}
536	
537	\end{document}
538	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1baf1bf2-e273-49a9-9b81-f56c16312ca7",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "d36edc21-66d8-4387-95df-0f05e758090a",
  "sourceToolAssistantUUID": "1baf1bf2-e273-49a9-9b81-f56c16312ca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T14:28:31.626Z_

Now let me also check the dream review reports and the best/worst variants to understand what reviewers said.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d36edc21-66d8-4387-95df-0f05e758090a",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wg1t3i6h2WuN5qHkQm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19a76a0d-e8e9-42bc-9af2-86d998d6b81e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FM5RkWv3jx2RNVy3sTJwMp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13155,
      "cache_read_input_tokens": 51369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13155,
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

_source line 31 · 2026-05-15T14:28:34.164Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KJ2SBtQETCDyCtBptbkX88`</summary>

```json
{
  "pattern": "**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a76a0d-e8e9-42bc-9af2-86d998d6b81e",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wg1t3i6h2WuN5qHkQm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c3e43427-88fc-4ba4-af2f-4e5f5303760a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FM5RkWv3jx2RNVy3sTJwMp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13155,
      "cache_read_input_tokens": 51369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13155,
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

### Tool result

_source line 32 · 2026-05-15T14:28:34.185Z_

<details><summary>↩ Tool result · `toolu_01KJ2SBtQETCDyCtBptbkX88`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/logs/review_best.log
artifacts/dream_reports/dream_20260515T120227/median/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/logs/review_median.log
artifacts/dream_reports/dream_20260515T120227/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T120227/median/review_report.md
artifacts/dream_reports/dream_20260515T120227/best/review_report.md
artifacts/dream_reports/dream_20260515T120227/worst/review_report.md
artifacts/dream_reports/dream_20260515T120227/logs/review_worst.log
artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/best/review_report.md
artifacts/dream_reports/dream_20260515T132059/logs/review_best.log
artifacts/dream_reports/dream_20260515T132059/median/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/median/review_report.md
artifacts/dream_reports/dream_20260515T132059/logs/review_median.log
artifacts/dream_reports/dream_20260515T132059/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3e43427-88fc-4ba4-af2f-4e5f5303760a",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "dec93742-91ed-4b4d-86a2-2c032b22813d",
  "sourceToolAssistantUUID": "c3e43427-88fc-4ba4-af2f-4e5f5303760a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T14:28:34.384Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KVJzXv38hQCRKWKvKpsVmx`</summary>

```json
{
  "pattern": "**/*report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dec93742-91ed-4b4d-86a2-2c032b22813d",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wg1t3i6h2WuN5qHkQm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63d67e08-fb9c-473c-a0a1-304de3a44087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FM5RkWv3jx2RNVy3sTJwMp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13155,
      "cache_read_input_tokens": 51369,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13155
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 51369,
          "cache_creation_input_tokens": 13155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13155,
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

_source line 34 · 2026-05-15T14:28:34.412Z_

<details><summary>↩ Tool result · `toolu_01KVJzXv38hQCRKWKvKpsVmx`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/median/review_report.md
artifacts/dream_reports/dream_20260515T120227/best/review_report.md
artifacts/dream_reports/dream_20260515T120227/worst/review_report.md
artifacts/dream_reports/dream_20260515T132059/best/review_report.md
artifacts/dream_reports/dream_20260515T132059/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63d67e08-fb9c-473c-a0a1-304de3a44087",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "1101a362-3505-4379-97a4-370728ffabfa",
  "sourceToolAssistantUUID": "63d67e08-fb9c-473c-a0a1-304de3a44087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T14:28:37.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AEiv2KdJkdozVbn7q3D8K1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1101a362-3505-4379-97a4-370728ffabfa",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WgSBnjZ4Yq4tLvSZfN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c4626f6-9c59-4e31-b6bb-4d14a730b94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yeroVGzBF4e9rfcqvYpdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 64524,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 36 · 2026-05-15T14:28:37.686Z_

<details><summary>↩ Tool result · `toolu_01AEiv2KdJkdozVbn7q3D8K1`</summary>

```text
1	---
2	dream_id: dream_20260515T132059
3	tier: median
4	overall_score: 2.5/5 — Leaning Reject (Main); Recommend Findings
5	timestamp: 2026-05-15T14:25:43.822210+00:00
6	---
7	
8	# DREAM Review Report: FREIGE
9	
10	**Paper**: FREIGE: Faithful Evidence Generation for Document-Level Relation Extraction via Rejection Sampling Fine-Tuning  
11	**Venue**: EMNLP 2026 Main (via ACL Rolling Review)  
12	**Review Mode**: Full (2 Reviewers + Roundtable)  
13	**Date**: 2026-05-15
14	
15	---
16	
17	## 1. Paper Summary
18	
19	FREIGE proposes the first LLM-based document-level relation extraction (DocRE) system that jointly generates relation triples and sentence-level evidence citations. The method uses Rejection Sampling Fine-Tuning (RSFT): an SFT-trained Qwen3-4B generates N=8 candidate outputs per document, a Contrastive Evidence Discrimination (CED) scorer based on DeBERTa-v3-base NLI ranks candidates by evidence quality using document-internal hard negatives, and only the top-1 candidate is retained for further fine-tuning. On DocRED test, FREIGE achieves rel_F1=43.2% (+3.2pp over SFT, p<0.01) and joint Evi-F1=32.2%. The paper also documents "evidence-extraction decoupling" under GRPO+QLoRA (evidence quality rises while extraction collapses), shows this worsens with larger group sizes (G=8 vs G=4), and introduces EDCR (Evidence Distractor Citation Rate) as a diagnostic metric validated through human annotation (r=0.44, method-level rank concordance=1.0).
20	
21	---
22	
23	## 2. Strengths
24	
25	### S1: Credible and well-scoped "first" claim (R1+R2 consensus)
26	No prior LLM-based DocRE system jointly generates (head, relation, tail, [evidence sentences]). Encoder methods (DREEAM, SAIS) derive evidence from attention weights (implicit, not directly auditable). LLM methods (LMRC, AutoRE) produce triples only. The task definition fills a genuine gap relevant to KB population, biomedical curation, and RAG provenance. The claim is appropriately scoped to DocRED.
27	
28	### S2: Thorough training paradigm comparison (R1+R2 consensus)
29	The systematic GRPO → DPO → SFT → RSFT spectrum (Table 5) is more insightful than typical ablation studies. The ordering (GRPO collapse < DPO degradation < SFT baseline < RSFT improvement) leads to the nuanced insight that the problem is contrastive/reward-based losses in general, not the online/offline distinction. This is a genuinely useful empirical contribution.
30	
31	### S3: Evidence-extraction decoupling is the paper's strongest empirical finding (R1+R2 consensus)
32	The observation that GRPO drives evi_F1 to 0.835–0.862 while rel_F1 collapses to <0.08 is striking. The G=4 vs G=8 comparison is particularly valuable: G=8 peaks earlier (step 40) and collapses faster, ruling out the "insufficient exploration" counter-argument and connecting to reward overoptimization theory (Gao et al. 2023). The full checkpoint trajectory (Table 4) with monotonically increasing reward alongside collapsing extraction is a compelling empirical demonstration.
33	
34	### S4: Well-designed ablation structure (R1)
35	The paper includes ablations along multiple axes: CED vs flat-NLI scoring (Table 2), top-k filtering strictness (Table 8), NLI model capacity (Table 12), CED as training vs inference reranker (Section 5.6), model size (Table 9, 1.7B/4B/8B), and dataset variant (Table 10, Re-DocRED). Each isolates a specific design choice. The CED-reranker experiment is a particularly clever control separating the value of CED as a signal from RSFT as a paradigm.
36	
37	### S5: Intellectual honesty throughout (R2)
38	The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods (43.2% vs 62.8%), EDCR's moderate sample-level correlation (r=0.44), and dev-to-test degradation (3.6pp vs 0.6pp for SFT). This level of self-assessment substantially increases credibility.
39	
40	### S6: EDCR captures a real evaluation blind spot (R1+R2 consensus)
41	The demonstration that GRPO achieves high evi_F1 (~0.835–0.862) but EDCR >0.92 illustrates a clear failure mode invisible to standard Evi-F1. The metric is simple, interpretable, and the cross-method diagnostic zones (collapse >85%, baseline ~71%, filtered 64–67%) provide actionable diagnostic information.
42	
43	---
44	
45	## 3. Weaknesses
46	
47	### W1 [Major]: CED is not a novel method and does not significantly outperform the simpler alternative (R2 primary, R1 concurs after correction)
48	The contrastive margin (p_entail(cited) − max p_entail(distractor)) is a standard pattern in retrieval, reranking, and faithfulness evaluation. More critically, CED does NOT significantly outperform flat-NLI scoring on any metric: evi_F1 p=0.12, rel_F1 p=0.28, EDCR p=0.09 (Table 2). The 78% candidate overlap between the two scorers indicates minimal differentiation. Despite being named in the title, acronym (FREIGE), and 6 of 12 tables, CED's actual contribution is marginal. The paper's Discussion reframes CED as "one possible scoring function," but the rest of the paper reads as CED-centric, creating a title-contribution mismatch.
49	
50	**Impact**: This means the primary methodological contribution reduces to "RSFT applied to DocRE," which is also not architecturally novel (see W2). The contribution budget shifts to task definition + negative findings + diagnostic metric.
51	
52	### W2 [Major]: RSFT is existing methodology applied to a new domain (R2 primary)
53	Rejection sampling fine-tuning / ReST is well-established for math reasoning (Dong et al. 2024, RAFT), code generation (Singh et al. 2024, ReST-EM), and dialogue (Gulcehre et al. 2023). The paper's title centers "Rejection Sampling Fine-Tuning" as the solution, but there is no architectural or algorithmic innovation in the RSFT pipeline — it is a straightforward generate → score → filter → retrain loop. Applying it to DocRE is a valid application contribution, but it should not be framed as a methodological advance.
54	
55	### W3 [Major]: Evidence-extraction decoupling is confounded by QLoRA (R1+R2 consensus)
56	All GRPO experiments use 4-bit QLoRA (rank=64). The paper claims "structural incompatibility" between online RL and document-level IE, but never tests full fine-tuning or even higher-rank/bf16 LoRA as controls. The Limitations section appropriately scopes to "GRPO+QLoRA," but the abstract and introduction use unqualified language like "online reward optimization (GRPO) with evidence-quality rewards causes catastrophic evidence-extraction decoupling." A full fine-tuning or bf16 LoRA experiment would be needed to determine whether this is a QLoRA artifact or a genuine RL-for-IE phenomenon. Without this control, the claim's generalizability is limited.
57	
58	### W4 [Major]: Significant related work gaps (R2 primary)
59	The "RL for Information Extraction" paragraph (Section 2) states "Prior work has applied RL to IE tasks with mixed results" without citing a single specific paper. Critical omissions include:
60	- **R1-RE** (arXiv 2507.04642): GRPO for sentence-level RE that *succeeds* — creates a natural foil (why does GRPO work for sentence-level but fail for document-level?), which would actually strengthen the paper's argument
61	- **Recent LLM-based DocRE methods**: RelPrior (arXiv 2511.08143), Ru-LLM (NLPCC 2025), AutoRE (arXiv 2403.14888), GLiDRE (arXiv 2508.00757) — while none produce evidence (strengthening the "first" claim), their omission leaves the extraction gap (43.2% vs LMRC's 60.7%) undercontextualized
62	- **GRPO stability literature**: DAPO (NeurIPS 2025), Dr. GRPO (COLM 2025) — mechanisms that may explain document-level IE failures
63	- **NLI-based faithfulness evaluation**: INFUSE (EACL 2024), TRUE benchmark — CED's methodological antecedents
64	
65	### W5 [Moderate]: "Evidence-extraction decoupling" may be a special case of well-known reward hacking (R2 primary, R1 concurs)
66	Reward hacking/overoptimization — where optimizing a proxy reward degrades the true objective — is extensively documented (Gao et al. 2023, Skalse et al. 2022). The specific manifestation in DocRE is a domain-specific instance of this general phenomenon. The paper should acknowledge this lineage more explicitly rather than presenting it as a wholly novel discovery. Additionally, the paper mentions (in the GRPO analysis) that the decoupling occurs across all reward types including extraction-only rewards — if even extraction-only reward fails under GRPO+QLoRA, the issue may be GRPO+QLoRA instability for structured generation broadly, not specifically evidence-vs-extraction misalignment. This partially undermines the "decoupling" framing.
67	
68	### W6 [Moderate]: EDCR human validation is underpowered (R1 primary)
69	The human validation uses only 100 samples with 2 annotators (κ=0.62). With only 3–4 methods at the method level, "perfect method-level rank concordance" is not statistically remarkable (random chance ≈ 1/24 for 4 methods, 1/6 for 3 methods). The sample-level correlation r=0.44 has a wide confidence interval at n=100. EDCR systematically overestimates the distractor rate by 8.5pp, attributed to incomplete DocRED gold annotations (~14% false distractors). While the paper honestly reports these limitations, the validation falls short of establishing EDCR as a reliable metric beyond directional diagnostics.
70	
71	### W7 [Moderate]: Large extraction gap limits practical impact (R1+R2 consensus)
72	FREIGE achieves rel_F1=43.2% (test) vs DREEAM 62.8% and LMRC 60.7%. Even the 8B variant (rel_F1=48.8% dev) falls well short. The paper correctly decomposes the Evi-F1 gap into extraction recall vs evidence quality (conditional Evi-F1: 80% vs ~93%), but the extraction gap itself is underexplained. LMRC uses a similar paradigm (LLaMA3.1-8B) and achieves 60.7% without evidence generation — a direct comparison or ablation (same model, with vs without evidence output) would clarify how much of the gap is due to the evidence generation burden vs other factors.
73	
74	### W8 [Moderate]: Dev-to-test degradation asymmetry (R1 primary)
75	RSFT shows 3.6pp dev-to-test degradation in rel_F1 (46.8→43.2 dev→test) vs only 0.6pp for SFT (40.6→40.0). This suggests indirect overfitting through the CED scoring pathway — RSFT candidates are generated from training documents, and CED scoring may implicitly favor patterns that correlate with dev-set characteristics. While the test improvement remains significant (p<0.01), this 6x relative degradation ratio warrants investigation and is not adequately analyzed.
76	
77	### W9 [Minor]: Single-seed reporting for main results (R1)
78	The paper reports results for "best RSFT configuration (3 epochs, alpha=128, seed=43)" based on dev-set selection. Table 2 shows three different configs with CED (rel_F1: 44.49, 46.83, 44.93), indicating meaningful variance across seeds/configs. Mean ± std across seeds should be reported for the main RSFT results to avoid the appearance of cherry-picking.
79	
80	---
81	
82	## 4. Claims-Evidence Alignment
83	
84	| # | Claim | Evidence in Paper | Verdict |
85	|---|-------|-------------------|---------|
86	| C1 | First LLM-based DocRE with verifiable evidence | No prior work cited/found; results across 3 scales and 2 datasets | **Supported** — genuine novelty in task definition |
87	| C2 | RSFT +3.2pp test rel_F1 over SFT (p<0.01) | Table 1 (test), p-value reported | **Supported** — but single seed, 3.6pp dev-to-test degradation noted |
88	| C3 | CED scoring as key component | Table 2: CED vs flat-NLI NOT significant (p=0.12/0.28/0.09); 78% candidate overlap | **Weakly supported** — consistent direction (+0.49/+0.75pp) but no statistical significance; CED's value may lie only in ranking (top-k selection) rather than scoring precision |
89	| C4 | Evidence-extraction decoupling in GRPO | Tables 3–4: comprehensive trajectory data; G=4 vs G=8 comparison; reward-rel_F1 negative correlation r=−0.68 | **Partially supported** — convincing within GRPO+QLoRA scope, but generalizability beyond QLoRA is uncertain; all reward types fail (including extraction-only), which suggests broader GRPO+QLoRA instability rather than evidence-specific decoupling |
90	| C5 | EDCR as validated diagnostic metric | Table 7: r=0.44, κ=0.62, method-level concordance=1.0; Table 6: clear zone separation | **Partially supported** — directionally useful, but modest sample-level correlation, systematic overestimate (+8.5pp), and underpowered validation (n=100) |
91	| C6 | Data curation > reward/preference learning for structured IE | Table 5: RSFT > SFT > DPO > GRPO; Section 5.4 analysis | **Supported** — well-demonstrated for this task/model combination |
92	
93	---
94	
95	## 5. Experiment Coverage Assessment
96	
97	Comparing paper content against the full experiment design (review_context.yaml, 13 planned experiments):
98	
99	| Experiment | Plan ID | In Paper? | Coverage Quality |
100	|-----------|---------|-----------|-----------------|
101	| CED vs flat-NLI RSFT ablation | plan_001 | ✓ Table 2 | Full — 3 configs, bootstrap p-values |
102	| Test set evaluation | plan_002 | ✓ Table 1 | Full — 3 methods on CodaLab |
103	| EDCR cross-method diagnostic | plan_003 | ✓ Table 6 | Full — 7 methods, zone classification |
104	| DREEAM baseline reproduction | plan_004 | ✓ Table 11 | Full — <1pp gap, validates protocol |
105	| CED-as-reranker | plan_005 | ✓ Section 5.6 | Adequate — results reported but no table |
106	| Model size ablation (1.7B/8B) | plan_006 | ✓ Table 9 | Full — 3 sizes with consistent gains |
107	| Re-DocRED extension | plan_007 | ✓ Table 10 | Full — ceiling effect correctly noted |
108	| Top-k ablation | plan_008 | ✓ Table 8 | Full — quality > quantity confirmed |
109	| GRPO forgetting analysis | plan_009 | ✓ Tables 3–4, Section 5.3 | Good — trajectory data shown, but figures described in context not in paper |
110	| NLI model ablation | plan_010 | ✓ Table 12 | Full — base vs large, bottleneck identified |
111	| GRPO G=8 experiment | plan_011 | ✓ Tables 3–4 | Full — decisive for ruling out "G too small" |
112	| DPO+CED experiment | plan_012 | ✓ Table 5 | Full — fills spectrum |
113	| EDCR human validation | plan_013 | ✓ Table 7 | Full — all statistics reported |
114	
115	**Coverage**: 13/13 experiments covered. All planned experiments are represented in the paper. The paper demonstrates comprehensive experimental coverage.
116	
117	---
118	
119	## 6. Novelty Assessment
120	
121	| Component | Novelty | Rationale |
122	|-----------|---------|-----------|
123	| Evidence-grounded DocRE task definition | **Medium-High** | Genuine gap; first to combine extraction + evidence in LLM-based DocRE |
124	| CED scoring function | **Low** | Standard contrastive NLI; not significantly better than flat-NLI |
125	| RSFT for DocRE | **Low** | Existing methodology (RAFT/ReST, mature since 2023) applied to new domain |
126	| Evidence-extraction decoupling finding | **Medium-High** | Novel empirical observation in IE, with good G=4/G=8 evidence; weakened by QLoRA confound and being a domain instance of reward hacking |
127	| EDCR metric | **Medium** | Identifies real blind spot; formula is trivial but observation is valuable |
128	| GRPO/DPO/RSFT spectrum analysis | **Medium** | Well-designed comparison; contrastive-loss insight is useful for the community |
129	
130	**Overall novelty**: The paper's novelty is concentrated in the task definition and negative findings rather than in the method. The method-level contributions (CED, RSFT) are applications of existing techniques with limited differentiation.
131	
132	---
133	
134	## 7. Actionable Revision Suggestions
135	
136	### Must-fix for resubmission:
137	1. **Add QLoRA qualifier to all GRPO claims** in abstract and introduction, not just Limitations
138	2. **Expand "RL for IE" related work** substantially — cite R1-RE (GRPO for sentence-RE), REAR, and other RL-for-IE papers; discuss why sentence-level succeeds where document-level fails
139	3. **Add recent LLM-based DocRE baselines** (RelPrior, Ru-LLM, AutoRE) to contextualize the extraction gap
140	4. **Run GRPO without QLoRA** (full FT or bf16 LoRA) to determine if decoupling is a QLoRA artifact or a genuine phenomenon
141	5. **Report multi-seed mean±std** for main RSFT results (at least 3 seeds)
142	6. **Reframe CED honestly throughout** — either strengthen differentiation or pivot the narrative to "RSFT pipeline (scorer-agnostic) + decoupling finding + EDCR"
143	
144	### Should-fix:
145	7. **Add SFT-without-evidence ablation** to measure the evidence generation tax on extraction
146	8. **Analyze dev-to-test degradation** — does CED filtering create implicit data leakage?
147	9. **Discuss CED's dependence on gold evidence labels** (Eq. 1 uses gold evidence set for hard negatives)
148	10. **Acknowledge reward hacking lineage** more explicitly in Section 5.3/6
149	11. **Expand EDCR human validation** to ≥200 samples if possible
150	
151	### Nice-to-have:
152	12. Per-relation-type analysis of CED vs flat-NLI
153	13. Discussion of CED in the context of citation precision evaluation (FactScore, attributed QA)
154	14. Engagement with GRPO stability literature (DAPO, Dr. GRPO)
155	
156	---
157	
158	## 8. Consolidated Scores
159	
160	| Dimension | R1 | R2 | Converged | Rationale |
161	|-----------|----|----|-----------|-----------|
162	| Soundness | 3 | 3 | **3/5** | Experiments are thorough but QLoRA confound limits the GRPO claim; CED non-significance weakens the method; dev-to-test degradation insufficiently analyzed |
163	| Excitement | 3 | 3 | **3/5** | Task definition is valuable; decoupling finding is interesting; but limited method novelty and large extraction gap dampen excitement |
164	| Overall Assessment | 3.0 | 2.5 | **2.5/5** | After cross-sharing, R1 concurs with R2's novelty concerns and the related work gaps are substantial; contribution package (task + negative finding + diagnostic metric) is suitable for Findings but falls short of Main at ~22-25% acceptance rate |
165	| Confidence | 4 | 4 | **4/5** | Both reviewers well-calibrated on the task area |
166	
167	---
168	
169	## 9. Overall Assessment
170	
171	**Recommendation: 2.5/5 — Leaning Reject for EMNLP 2026 Main; recommend Findings track**
172	
173	### Justification
174	
175	FREIGE makes a credible "first" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding about GRPO+QLoRA for document-level structured IE. The experimental coverage is comprehensive (13 experiments, ablations across scoring function, filtering strictness, NLI model, training paradigm, model size, and dataset). The honest reporting of CED's non-significance, the extraction gap, and EDCR's limitations is commendable.
176	
177	However, the paper faces three interconnected problems that prevent recommendation for Main:
178	
179	1. **Limited method novelty**: CED is a standard contrastive NLI scorer that does not significantly outperform flat-NLI (p>0.05 on all metrics). RSFT is existing methodology with no architectural innovation. The contribution is the application to a new task, not the method.
180	
181	2. **Under-scoped key claim**: The evidence-extraction decoupling finding is established only for GRPO+QLoRA but presented more broadly in the abstract/introduction. Without a full-FT or bf16 LoRA control, the claim cannot be distinguished from a QLoRA-specific artifact. The finding that extraction-only rewards also fail further complicates the "decoupling" narrative — it may be GRPO+QLoRA instability for structured generation generally.
182	
183	3. **Significant related work gaps**: The "RL for IE" section cites no specific papers. Critical omissions include R1-RE (GRPO for sentence-level RE — a direct foil) and multiple recent LLM-based DocRE methods. This weakens the paper's positioning and suggests incomplete literature coverage.
184	
185	The paper's contribution package — task definition, thorough negative findings, EDCR metric — represents solid empirical work appropriate for the EMNLP Findings track. With the revisions outlined above (especially the QLoRA control experiment, expanded related work, and honest CED reframing), this could be strengthened to Main quality.
186	
187	---
188	
189	*Review conducted by: R1 (Methods + Experiments) and R2 (Novelty + Related Work)*  
190	*Roundtable: 4-step protocol (Independent → Cross-share → Convergence → Consolidated)*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c4626f6-9c59-4e31-b6bb-4d14a730b94e",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "bda12e96-a886-4ae2-b91b-8601e47b6264",
  "sourceToolAssistantUUID": "5c4626f6-9c59-4e31-b6bb-4d14a730b94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T14:28:38.073Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WHdCysrQ4mkUd52WtqRCmW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bda12e96-a886-4ae2-b91b-8601e47b6264",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WgSBnjZ4Yq4tLvSZfN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "740d40b4-ee0b-44e4-87d6-c8d36c746b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yeroVGzBF4e9rfcqvYpdh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 64524,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 64524,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 779,
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

_source line 38 · 2026-05-15T14:28:38.079Z_

<details><summary>↩ Tool result · `toolu_01WHdCysrQ4mkUd52WtqRCmW`</summary>

```text
1	---
2	dream_id: dream_20260515T132059
3	tier: best
4	overall_score: 3.0 - Findings
5	timestamp: 2026-05-15T14:16:20.253527+00:00
6	---
7	
8	# Dream Review Report: FREIGE
9	
10	**Paper:** FREIGE: Faithful Evidence Generation for LLM-Based Document-Level Relation Extraction via Contrastive Evidence Discrimination
11	**Venue:** EMNLP 2026 Main (ACL Rolling Review)
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	
14	---
15	
16	## Roundtable Summary
17	
18	| | R1 (Methods+Experiments) | R2 (Novelty+Related Work) | Post-Discussion |
19	|---|---|---|---|
20	| Soundness | 3/5 | 3/5 | 3/5 |
21	| Excitement | 3/5 → 2.5/5 | 3/5 | 3/5 |
22	| Overall | 3.0 → 2.5 | 3.0 | **3.0 (Findings)** |
23	| Reproducibility | 3/5 | 4/5 | 3/5 |
24	| Confidence | 4/5 | 4/5 | 4/5 |
25	
26	**Consensus outcome: 3.0 — Findings acceptance.** Both reviewers initially scored 3.0. During cross-sharing, R1 dropped to 2.5 after being persuaded by R2's point about CED's non-significance over flat-NLI. R2 held at 3.0, finding R1's QLoRA confound concern reinforcing but not score-changing. The meta-review settles at 3.0: the paper has genuine contributions (task definition, decoupling finding, EDCR metric) that merit Findings publication, but insufficient method novelty and positioning gaps prevent main conference acceptance.
27	
28	---
29	
30	## Consolidated Strengths
31	
32	**S1: Evidence-grounded DocRE as a new task (R1, R2 agree).** The paper credibly claims to be the first LLM-based DocRE system jointly generating relation triples and explicit sentence-level evidence citations. This fills a real gap: encoder methods provide only implicit attention-based evidence, and all prior LLM-based DocRE methods (LMRC, AutoRE, etc.) produce no evidence. The task formulation is well-motivated for KB population, biomedical curation, and RAG provenance.
33	
34	**S2: Evidence–extraction decoupling is a striking negative finding (R1, R2 strongly agree).** The observation that GRPO drives Evi-F1 to 0.850 while rel_F1 collapses to <0.02 is the paper's most novel empirical contribution. Testing across G=4/G=8, multiple learning rates, and 42 checkpoints with a clear three-phase dynamics description (onset → acceleration → plateau) provides convincing documentation. The G=4 vs G=8 comparison rules out advantage-estimation noise as the root cause. Both reviewers consider this finding independently valuable to the RL-for-NLP community.
35	
36	**S3: Comprehensive experimental coverage (R1).** 12 tables covering 14 distinct experiments: CED vs flat-NLI ablation, CED usage modes (training vs inference), top-k filtering, NLI model capacity, model scale (1.7B–8B), dataset variant (Re-DocRED), online-offline RL spectrum (GRPO/DPO/SFT/RSFT), cross-method EDCR diagnostic, and human validation. Few ablation gaps remain. Statistical testing (paired bootstrap, p<0.01) is present for key comparisons.
37	
38	**S4: EDCR fills a genuine evaluation gap (R1, R2 agree).** The demonstration that GRPO achieves Evi-F1=0.850 but EDCR=0.988 illustrates a clear blindspot of standard Evi-F1 to entity-sharing distractors. Human validation (100 samples, 3 annotators, κ=0.72, Pearson r=0.62) provides reasonable support. The metric is simple, interpretable, and captures a failure mode practically relevant to evidence generation.
39	
40	**S5: Honest self-assessment and transparent limitations (R2).** The paper acknowledges CED's modest advantage, the extraction gap vs encoder methods, and EDCR's proxy nature. This intellectual honesty increases credibility.
41	
42	**S6: Well-designed GRPO/DPO/RSFT training paradigm comparison (R2).** The full spectrum — GRPO (0.014–0.031) ≪ DPO (0.325) < SFT (0.406) < RSFT (0.468) — adds nuance beyond a binary "RL fails" narrative, showing DPO partially mitigates but does not solve decoupling.
43	
44	---
45	
46	## Consolidated Weaknesses
47	
48	### Major
49	
50	**W1: CED's advantage over flat-NLI is modest and possibly non-significant (R1 W2, R2 W1 — both agree this is critical).** The paper reports +2.71pp rel_F1 (p=0.007), +2.08pp Evi-F1 (p=0.004), −5.64pp EDCR (p=0.002) for CED vs flat-NLI. R2 raises that in broader experimental context, CED's significance is fragile. The core issue: if CED is positioned as the paper's central contribution (it is in the title and acronym) but provides only marginal improvement over a simpler baseline, the method novelty is thin. The bigger contribution is the RSFT pipeline itself, yet RSFT is existing methodology (Dong et al. 2024). During roundtable, R1 was persuaded this is the paper's most damaging structural weakness.
51	
52	**W2: GRPO failure analysis is confounded by QLoRA (R1 W1, R2 agrees).** The paper claims "structural incompatibility between on-policy RL and document-level structured IE," but all GRPO experiments use QLoRA (4-bit quantization). QLoRA introduces specific failure modes: KL explosion from quantization noise, rank-limited parameter space. The paper should scope the claim to "GRPO+QLoRA for document-level IE" and prominently discuss the QLoRA confound. A full-rank or bf16 LoRA GRPO experiment would be needed to support the broader claim. Both reviewers agree this scoping is essential.
53	
54	**W3: Related work has notable gaps (R2 W2, W3 — R1 agrees post-discussion).**
55	- **R1-RE** (arXiv 2507.04642): GRPO for sentence-level RE — must-cite. Its success at sentence-level creates a natural foil for the document-level failure documented here. Explaining why GRPO works at sentence-level but not document-level would *strengthen* the paper's argument.
56	- **Recent LLM-based DocRE methods**: RelPrior, Ru-LLM, AutoRE, GLiDRE — missing from related work. Their omission weakens extraction performance positioning.
57	- **Contrastive reward methods**: (arXiv 2403.07708, EMNLP 2024 contrastive RM) — relevant to CED's design.
58	- **RSFT theoretical foundations**: "A Minimalist Approach to LLM Reasoning" (arXiv 2504.11343) — directly relevant.
59	- **DAPO/Dr. GRPO**: Identify entropy collapse and normalization bias in GRPO that may explain document-level failures.
60	
61	**W4: Large extraction gap with encoder and generative baselines is underexplained (R1 W3).** FREIGE (Qwen3-4B) achieves rel_F1=0.455 vs LMRC (LLaMA-3.1-8B) at 0.607 and DREEAM at ~0.631. The 15pp gap with LMRC deserves quantitative analysis: how much is due to evidence generation burden vs model size (4B vs 8B)? An SFT-without-evidence ablation would isolate the evidence cost. A post-hoc evidence retrieval baseline (extract triples first, retrieve evidence second) would test whether joint generation is necessary.
62	
63	### Moderate
64	
65	**W5: CED requires gold evidence at scoring time (R1 W4).** The hard-negative set N(h,t,D) excludes E_gold, requiring gold annotations during CED scoring. This is acceptable for the RSFT pipeline (scoring candidates on training data), but limits applicability to semi-supervised or domain-transfer scenarios. Not discussed in the paper.
66	
67	**W6: EDCR human validation is small-scale (R1 W5).** 100 samples (25 per method) with a 4-point method-level correlation is statistically thin. Per-sample correlation analysis would be more convincing. The auto-human gap of +6.8pp suggests systematic bias that deserves deeper analysis.
68	
69	**W7: DPO experiment is underspecified (R1 W8).** No details on preference pair construction, dataset size, or DPO hyperparameters (β, lr, epochs). This makes the DPO result — a key data point in the RL spectrum — hard to evaluate and reproduce.
70	
71	**W8: Framing tension (R2 W6).** The paper alternates between CED-centric and RSFT-centric narratives. Given CED's modest advantage, the paper should commit to one framing: either "task definition + negative finding (decoupling) + diagnostic metric (EDCR)" as the core contributions, with CED/RSFT as one reasonable instantiation, or strengthen CED's differentiation.
72	
73	### Minor
74	
75	**W9: Missing forgetting dynamics visualization (R1 W7, R2 agrees).** Section 4.3 describes a three-phase pattern across 42 checkpoints but provides no figure. A training dynamics plot would be far more convincing than text description alone.
76	
77	**W10: Connection to reward overoptimization literature is superficial (R2 W5).** CED is framed as "anti-overoptimization" but the paper does not engage with the KL-dependent scaling law framework or Goodhart's Law interpretation.
78	
79	---
80	
81	## Key Questions for Authors
82	
83	1. **Q1 (Critical):** Have you tested GRPO with full-rank fine-tuning (no LoRA) to isolate whether catastrophic forgetting is QLoRA-specific or inherent to on-policy RL for document-level IE?
84	
85	2. **Q2 (Critical):** R1-RE (arXiv 2507.04642) applies GRPO successfully to sentence-level RE. What is your hypothesis for why GRPO fails at document-level but not sentence-level? Is it output length, multi-triple credit assignment, or something else?
86	
87	3. **Q3 (Important):** What is the overlap rate between CED-selected and flat-NLI-selected top-1 candidates? If >80%, the marginal signal from the contrastive design is limited to a small subset of documents.
88	
89	4. **Q4 (Important):** What happens to CED when N(h,t,D) is empty (no entity-sharing non-gold sentences exist)? Does it reduce to flat-NLI? What fraction of triples have empty hard-negative sets?
90	
91	5. **Q5:** Have you considered training Qwen3-4B SFT without evidence output to quantify the extraction cost of joint evidence generation?
92	
93	6. **Q6:** What is the inference latency of FREIGE vs DREEAM? Practical deployment considerations are absent.
94	
95	---
96	
97	## Missing Experiments / Recommendations
98	
99	1. **SFT-without-evidence ablation** — isolate the extraction cost of joint evidence generation and contextualize the gap with LMRC.
100	2. **Post-hoc evidence retrieval baseline** — extract triples with SFT, then retrieve evidence sentences post-hoc (NLI or BM25). Tests whether joint generation is necessary.
101	3. **Forgetting dynamics figure** — plot rel_F1, Evi-F1, and reward trajectories across training steps for all GRPO configs.
102	4. **Full-rank GRPO experiment** (even small-scale) — needed to support the "structural incompatibility" claim beyond QLoRA.
103	5. **Error analysis by relation type/frequency** — determine whether CED's advantage concentrates on specific relation categories.
104	6. **Confidence intervals across seeds** — Table 1 reports single-number test results; dev set variance (~2pp) is substantial.
105	
106	---
107	
108	## Experiment Coverage Assessment
109	
110	Compared to the full experimental design (review_context.yaml), the paper covers **14/14 planned experiments** across 12 tables. This is comprehensive. However, the paper would benefit from:
111	- Planned visualization (GRPO forgetting dynamics figure) is described in text but not rendered
112	- The DREEAM reproduction (plan_004) is present in Table 12 but could include more detail on reproduction fidelity
113	
114	---
115	
116	## Final Assessment
117	
118	| Dimension | Score | Justification |
119	|-----------|-------|---------------|
120	| **Soundness** | **3/5** (Acceptable) | Main claims supported but with caveats: CED advantage modest, GRPO analysis confounded by QLoRA |
121	| **Excitement** | **3/5** (Interesting) | Decoupling finding is genuinely interesting; EDCR is useful. But method novelty (CED) is limited |
122	| **Overall** | **3.0/5** (Findings) | Genuine contributions in task definition, negative finding, and diagnostic metric. Insufficient method novelty and positioning gaps for main conference |
123	| **Reproducibility** | **3/5** | Most details provided; DPO setup underspecified; no code/data release mentioned |
124	| **Confidence** | **4/5** | Both reviewers are familiar with DocRE, RLHF, and evaluation methodology |
125	
126	### Meta-Review Justification
127	
128	FREIGE makes three genuine contributions: (1) defining evidence-grounded DocRE as a task and providing the first LLM-based system for it, (2) documenting the evidence–extraction decoupling phenomenon under GRPO+QLoRA — a striking negative finding with implications for the RL-for-NLP community, and (3) proposing EDCR as a diagnostic metric that captures a failure mode invisible to standard Evi-F1. These contributions are sufficient for Findings.
129	
130	However, the paper falls short of main conference acceptance for three reasons: (a) the core method contribution (CED) provides only modest, potentially fragile improvements over the simpler flat-NLI baseline — the real contribution is the RSFT pipeline, which is existing methodology; (b) the GRPO failure analysis, while thorough, is confounded by QLoRA and the claims need scoping; (c) the related work section has notable gaps (R1-RE, recent LLM DocRE methods, contrastive reward literature) that weaken positioning.
131	
132	**Path to main conference:** (1) Replicate decoupling under full-rank/bf16 LoRA fine-tuning to support the broader "RL vs structured IE" claim; (2) Either strengthen CED's differentiation from flat-NLI or reframe the paper around the task + negative finding + metric; (3) Expand related work substantially; (4) Add the forgetting dynamics figure and SFT-without-evidence ablation.
133	
134	---
135	
136	## Roundtable Process Record
137	
138	- **Step 1 (Independent):** R1 scored 3.0 (Findings), R2 scored 3.0 (Findings)
139	- **Step 2 (Cross-sharing):** R1 was persuaded by R2's CED non-significance argument and dropped to 2.5. R2 found R1's QLoRA confound point reinforcing but maintained 3.0.
140	- **Step 3 (Convergence):** Both reviewers agree on: (i) task contribution genuine, (ii) decoupling finding most novel, (iii) CED advantage modest, (iv) GRPO claims need QLoRA scoping, (v) related work gaps. Divergence: R1 weights CED weakness more heavily (2.5), R2 weighs the package of contributions as sufficient for Findings (3.0).
141	- **Step 4 (Synthesis):** Final consensus at 3.0 (Findings). The paper's three contributions — task definition, negative finding, diagnostic metric — collectively reach Findings threshold despite limited method novelty. R1's downward revision is partially counterbalanced by the paper's comprehensive experimental coverage and honest self-assessment.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "740d40b4-ee0b-44e4-87d6-c8d36c746b3c",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "77637d5e-dff7-4dc6-90b1-dd144aad5bc8",
  "sourceToolAssistantUUID": "740d40b4-ee0b-44e4-87d6-c8d36c746b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-15T14:28:41.070Z_

Now let me also look at some of the actual experiment code and configurations to assess reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77637d5e-dff7-4dc6-90b1-dd144aad5bc8",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WghtM7cMt94pjMuXpR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05e8e766-354e-49b4-93d1-66e5b4828d73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hS7zuMs1P4t9wEhdBs8PF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10696,
      "cache_read_input_tokens": 65303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10696,
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

_source line 40 · 2026-05-15T14:28:42.914Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019xWfYdefSQFZFCSn3tvtJ3`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e8e766-354e-49b4-93d1-66e5b4828d73",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WghtM7cMt94pjMuXpR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d2fd272-6524-4c70-81f5-c3f4f0f1dd8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hS7zuMs1P4t9wEhdBs8PF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10696,
      "cache_read_input_tokens": 65303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10696,
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

_source line 41 · 2026-05-15T14:28:42.932Z_

<details><summary>↩ Tool result · `toolu_019xWfYdefSQFZFCSn3tvtJ3`</summary>

```text
artifacts/freige/__init__.py
artifacts/freige/data/__init__.py
artifacts/freige/rewards/__init__.py
artifacts/freige/analysis/__init__.py
artifacts/freige/training/__init__.py
artifacts/freige/eval/__init__.py
artifacts/freige/data/docred_processor.py
artifacts/freige/rewards/ced_reward.py
artifacts/freige/eval/evaluator.py
artifacts/freige/analysis/ced_signal_validation.py
artifacts/freige/training/smoke_test.py
artifacts/freige/training/sft_trainer.py
artifacts/freige/training/grpo_trainer.py
artifacts/freige/eval/find_best_checkpoint.py
artifacts/freige/eval/batch_eval.py
artifacts/diversity_probe.py
artifacts/freige/training/rsft_generate.py
artifacts/freige/training/rsft_score_filter.py
artifacts/freige/training/merge_shards.py
artifacts/freige/training/rsft_trainer.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d2fd272-6524-4c70-81f5-c3f4f0f1dd8c",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "52292f89-c884-4588-9809-5197fb3bdcb4",
  "sourceToolAssistantUUID": "1d2fd272-6524-4c70-81f5-c3f4f0f1dd8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T14:28:46.985Z_

<details open><summary>🔧 Tool call — Read · `toolu_012jhoT5N9qL9zRBtiM9TY8Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/rewards/ced_reward.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52292f89-c884-4588-9809-5197fb3bdcb4",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wh5cZR43dCKDkgNwsG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ea3ce80-bd49-402a-ac53-c786d0437e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdEhDcSRmB7XGsGEMRzezz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 75999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 383,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 43 · 2026-05-15T14:28:47.008Z_

<details><summary>↩ Tool result · `toolu_012jhoT5N9qL9zRBtiM9TY8Z`</summary>

```text
1	"""CED（Contrastive Evidence Discrimination）对比证据判别奖励。
2	
3	核心公式:
4	  p_pos = NLI_entail(concat(cited_evidence), claim)
5	  p_neg = max_j NLI_entail(neg_sent_j, claim)
6	  R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)
7	
8	输入: 关系三元组 + gold evidence 句子 + hard negative 句子
9	输出: CED 奖励值 ∈ [0, 1]
10	依赖: transformers, torch
11	"""
12	
13	import logging
14	from typing import Optional
15	
16	import torch
17	import torch.nn.functional as F
18	from transformers import AutoModelForSequenceClassification, AutoTokenizer
19	
20	logger = logging.getLogger(__name__)
21	
22	DEFAULT_NLI_MODEL = "cross-encoder/nli-deberta-v3-base"
23	
24	VERBALIZATION_TEMPLATES = {
25	    "P6": "The head of government of {head} is {tail}.",
26	    "P17": "{head} is located in the country {tail}.",
27	    "P19": "{head} was born in {tail}.",
28	    "P20": "{head} died in {tail}.",
29	    "P22": "The father of {head} is {tail}.",
30	    "P25": "The mother of {head} is {tail}.",
31	    "P26": "{head} is married to {tail}.",
32	    "P27": "{head} is a citizen of {tail}.",
33	    "P30": "{head} is located in the continent of {tail}.",
34	    "P31": "{head} is an instance of {tail}.",
35	    "P35": "The head of state of {head} is {tail}.",
36	    "P36": "The capital of {head} is {tail}.",
37	    "P37": "The official language of {head} is {tail}.",
38	    "P39": "{head} held the position of {tail}.",
39	    "P40": "{head} has a child named {tail}.",
40	    "P50": "The author of {head} is {tail}.",
41	    "P54": "{head} is a member of the sports team {tail}.",
42	    "P57": "The director of {head} is {tail}.",
43	    "P58": "The screenwriter of {head} is {tail}.",
44	    "P69": "{head} was educated at {tail}.",
45	    "P86": "The composer of {head} is {tail}.",
46	    "P102": "{head} is a member of the political party {tail}.",
47	    "P108": "{head} is employed by {tail}.",
48	    "P112": "{head} was founded by {tail}.",
49	    "P118": "{head} plays in the league {tail}.",
50	    "P123": "The publisher of {head} is {tail}.",
51	    "P127": "{head} is owned by {tail}.",
52	    "P131": "{head} is located in {tail}.",
53	    "P136": "The genre of {head} is {tail}.",
54	    "P137": "{head} is operated by {tail}.",
55	    "P140": "The religion of {head} is {tail}.",
56	    "P150": "{head} contains the administrative territory {tail}.",
57	    "P155": "{head} follows {tail}.",
58	    "P156": "{head} is followed by {tail}.",
59	    "P159": "The headquarters of {head} is located in {tail}.",
60	    "P161": "{head} features the cast member {tail}.",
61	    "P162": "The producer of {head} is {tail}.",
62	    "P166": "{head} received the award {tail}.",
63	    "P170": "The creator of {head} is {tail}.",
64	    "P171": "The parent taxon of {head} is {tail}.",
65	    "P172": "{head} belongs to the ethnic group {tail}.",
66	    "P175": "The performer of {head} is {tail}.",
67	    "P176": "The manufacturer of {head} is {tail}.",
68	    "P178": "The developer of {head} is {tail}.",
69	    "P179": "{head} is part of the series {tail}.",
70	    "P190": "{head} is a sister city of {tail}.",
71	    "P194": "The legislative body of {head} is {tail}.",
72	    "P205": "{head} is in the basin of {tail}.",
73	    "P206": "{head} is located near the body of water {tail}.",
74	    "P241": "{head} is a branch of the military {tail}.",
75	    "P264": "The record label of {head} is {tail}.",
76	    "P272": "The production company of {head} is {tail}.",
77	    "P276": "{head} is located in {tail}.",
78	    "P279": "{head} is a subclass of {tail}.",
79	    "P355": "{head} has the subsidiary {tail}.",
80	    "P361": "{head} is part of {tail}.",
81	    "P364": "The original language of {head} is {tail}.",
82	    "P400": "{head} is available on the platform {tail}.",
83	    "P403": "{head} flows into {tail}.",
84	    "P449": "The original network of {head} is {tail}.",
85	    "P463": "{head} is a member of {tail}.",
86	    "P488": "The chairperson of {head} is {tail}.",
87	    "P495": "{head} originates from the country {tail}.",
88	    "P527": "{head} has the part {tail}.",
89	    "P551": "{head} resides in {tail}.",
90	    "P569": "{head} was born on {tail}.",
91	    "P570": "{head} died on {tail}.",
92	    "P571": "{head} was established in {tail}.",
93	    "P576": "{head} was dissolved in {tail}.",
94	    "P577": "{head} was published on {tail}.",
95	    "P580": "{head} started in {tail}.",
96	    "P582": "{head} ended in {tail}.",
97	    "P585": "{head} occurred at the time {tail}.",
98	    "P607": "{head} was involved in the conflict {tail}.",
99	    "P674": "{head} features the character {tail}.",
100	    "P676": "The lyrics of {head} were written by {tail}.",
101	    "P706": "{head} is located on the terrain {tail}.",
102	    "P710": "{head} participated in {tail}.",
103	    "P737": "{head} was influenced by {tail}.",
104	    "P740": "{head} was formed in {tail}.",
105	    "P749": "The parent organization of {head} is {tail}.",
106	    "P800": "The notable work of {head} is {tail}.",
107	    "P807": "{head} was separated from {tail}.",
108	    "P840": "The narrative of {head} is set in {tail}.",
109	    "P937": "{head} worked in {tail}.",
110	    "P1001": "{head} applies to the jurisdiction of {tail}.",
111	    "P1056": "{head} produces {tail}.",
112	    "P1198": "The unemployment rate of {head} is {tail}.",
113	    "P1336": "{head} is claimed by {tail}.",
114	    "P1344": "{head} participated in {tail}.",
115	    "P1365": "{head} replaces {tail}.",
116	    "P1366": "{head} was replaced by {tail}.",
117	    "P1376": "{head} is the capital of {tail}.",
118	    "P1412": "{head} speaks the language {tail}.",
119	    "P1441": "{head} is present in the work {tail}.",
120	    "P3373": "{head} is a sibling of {tail}.",
121	}
122	
123	
124	def verbalize_triple(head: str, relation: str, tail: str) -> str:
125	    """将 (head, relation_id, tail) 三元组转为自然语言 claim。
126	
127	    Args:
128	        head: 头实体名称
129	        relation: Wikidata 属性 ID (如 "P17") 或关系名称
130	        tail: 尾实体名称
131	
132	    Returns:
133	        自然语言 claim 字符串
134	    """
135	    template = VERBALIZATION_TEMPLATES.get(relation)
136	    if template:
137	        return template.format(head=head, tail=tail)
138	    from freige.data.docred_processor import DOCRED_REL_INFO
139	    rel_name = DOCRED_REL_INFO.get(relation, relation)
140	    return f"{head} {rel_name} {tail}."
141	
142	
143	class CEDRewardModel:
144	    """CED 对比证据判别奖励模型。
145	
146	    Args:
147	        model_name: NLI 模型 HuggingFace ID
148	        device: torch 设备
149	        max_length: tokenizer 最大长度
150	    """
151	
152	    def __init__(
153	        self,
154	        model_name: str = DEFAULT_NLI_MODEL,
155	        device: Optional[str] = None,
156	        max_length: int = 512,
157	    ):
158	        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
159	        self.max_length = max_length
160	
161	        logger.info("Loading NLI model: %s", model_name)
162	        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
163	        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
164	        self.model.to(self.device)
165	        self.model.eval()
166	
167	        self._resolve_entailment_idx()
168	
169	    def _resolve_entailment_idx(self):
170	        """从 model.config.id2label 确定 entailment 类别的索引。"""
171	        id2label = self.model.config.id2label
172	        self.entail_idx = None
173	        for idx, label in id2label.items():
174	            if label.lower() in ("entailment", "entail"):
175	                self.entail_idx = int(idx)
176	                break
177	        if self.entail_idx is None:
178	            logger.warning(
179	                "Could not find 'entailment' in id2label=%s, defaulting to index 1",
180	                id2label,
181	            )
182	            self.entail_idx = 1
183	        logger.info("Entailment index: %d (id2label=%s)", self.entail_idx, id2label)
184	
185	    @torch.no_grad()
186	    def nli_entailment_prob(
187	        self, premises: list[str], hypotheses: list[str]
188	    ) -> torch.Tensor:
189	        """计算 batch 的 NLI entailment 概率。
190	
191	        Args:
192	            premises: 前提文本列表（evidence 句子）
193	            hypotheses: 假设文本列表（verbalized claim）
194	
195	        Returns:
196	            shape (batch_size,) 的 entailment 概率张量
197	        """
198	        inputs = self.tokenizer(
199	            premises,
200	            hypotheses,
201	            padding=True,
202	            truncation=True,
203	            max_length=self.max_length,
204	            return_tensors="pt",
205	        ).to(self.device)
206	
207	        logits = self.model(**inputs).logits
208	        probs = F.softmax(logits, dim=-1)
209	        return probs[:, self.entail_idx].cpu()
210	
211	    def compute_ced_reward(
212	        self,
213	        claim: str,
214	        cited_evidence_sents: list[str],
215	        hard_negative_sents: list[str],
216	        tau: float = 0.5,
217	    ) -> dict:
218	        """计算单个样本的 CED 奖励。
219	
220	        R_CED = max(0, p_pos - p_neg) * I(p_pos > tau)
221	
222	        Args:
223	            claim: verbalized 关系 claim
224	            cited_evidence_sents: gold evidence 句子列表
225	            hard_negative_sents: hard negative 句子列表
226	            tau: p_pos 阈值
227	
228	        Returns:
229	            {"reward": float, "p_pos": float, "p_neg": float, "margin": float}
230	        """
231	        evidence_concat = " ".join(cited_evidence_sents)
232	        p_pos = self.nli_entailment_prob(
233	            [evidence_concat], [claim]
234	        ).item()
235	
236	        if not hard_negative_sents:
237	            p_neg = 0.0
238	        else:
239	            neg_probs = self.nli_entailment_prob(
240	                hard_negative_sents, [claim] * len(hard_negative_sents)
241	            )
242	            p_neg = neg_probs.max().item()
243	
244	        margin = p_pos - p_neg
245	        reward = max(0.0, margin) * float(p_pos > tau)
246	
247	        return {
248	            "reward": reward,
249	            "p_pos": p_pos,
250	            "p_neg": p_neg,
251	            "margin": margin,
252	        }
253	
254	    def compute_ced_reward_batch(
255	        self,
256	        claims: list[str],
257	        cited_evidence_list: list[list[str]],
258	        hard_negative_list: list[list[str]],
259	        tau: float = 0.5,
260	    ) -> list[dict]:
261	        """批量计算 CED 奖励。
262	
263	        先合并所有 NLI 请求到两个大 batch（positive 和 negative），
264	        一次前向传播后拆分结果，减少 GPU kernel launch 开销。
265	
266	        Args:
267	            claims: N 个 claim
268	            cited_evidence_list: N 个 evidence 句子列表
269	            hard_negative_list: N 个 hard negative 句子列表
270	            tau: p_pos 阈值
271	
272	        Returns:
273	            N 个 {"reward", "p_pos", "p_neg", "margin"} 字典
274	        """
275	        n = len(claims)
276	        assert len(cited_evidence_list) == n and len(hard_negative_list) == n
277	
278	        pos_premises = [" ".join(ev) for ev in cited_evidence_list]
279	        pos_probs = self.nli_entailment_prob(pos_premises, claims)
280	
281	        all_neg_premises = []
282	        all_neg_hyps = []
283	        neg_counts = []
284	        for i in range(n):
285	            negs = hard_negative_list[i]
286	            neg_counts.append(len(negs))
287	            all_neg_premises.extend(negs)
288	            all_neg_hyps.extend([claims[i]] * len(negs))
289	
290	        if all_neg_premises:
291	            all_neg_probs = self.nli_entailment_prob(all_neg_premises, all_neg_hyps)
292	        else:
293	            all_neg_probs = torch.tensor([])
294	
295	        results = []
296	        offset = 0
297	        for i in range(n):
298	            p_pos = pos_probs[i].item()
299	            nc = neg_counts[i]
300	            if nc > 0:
301	                p_neg = all_neg_probs[offset:offset + nc].max().item()
302	            else:
303	                p_neg = 0.0
304	            offset += nc
305	
306	            margin = p_pos - p_neg
307	            reward = max(0.0, margin) * float(p_pos > tau)
308	            results.append({
309	                "reward": reward,
310	                "p_pos": p_pos,
311	                "p_neg": p_neg,
312	                "margin": margin,
313	            })
314	
315	        return results
316	
317	    def compute_flat_nli_reward(
318	        self,
319	        claim: str,
320	        cited_evidence_sents: list[str],
321	        tau: float = 0.5,
322	    ) -> dict:
323	        """Flat NLI 奖励（无对比项），用于 curriculum 第二阶段。
324	
325	        R_flat = p_pos * I(p_pos > tau)
326	        """
327	        evidence_concat = " ".join(cited_evidence_sents)
328	        p_pos = self.nli_entailment_prob(
329	            [evidence_concat], [claim]
330	        ).item()
331	        reward = p_pos * float(p_pos > tau)
332	        return {"reward": reward, "p_pos": p_pos}
333	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea3ce80-bd49-402a-ac53-c786d0437e3c",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "15c9a5a1-c3b1-4590-81dd-6e88a4f8d0d8",
  "sourceToolAssistantUUID": "0ea3ce80-bd49-402a-ac53-c786d0437e3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T14:28:47.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MYFRKJvmT1X8hd8WsS5x7B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/eval/evaluator.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15c9a5a1-c3b1-4590-81dd-6e88a4f8d0d8",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wh5cZR43dCKDkgNwsG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "225fae9b-d567-4e6c-a776-19e49c520d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdEhDcSRmB7XGsGEMRzezz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 383,
      "cache_read_input_tokens": 75999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 383,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 61,
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

_source line 45 · 2026-05-15T14:28:47.402Z_

<details><summary>↩ Tool result · `toolu_01MYFRKJvmT1X8hd8WsS5x7B`</summary>

```text
1	"""DocRED 关系抽取评测模块。
2	
3	指标:
4	  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组
5	  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1
6	  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例
7	
8	输入: 预测列表 + gold 标注列表（每个元素为文档级标注）
9	输出: 指标字典
10	"""
11	
12	import json
13	import logging
14	from collections import defaultdict
15	from typing import Optional
16	
17	logger = logging.getLogger(__name__)
18	
19	
20	def _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:
21	    return (doc_id, head.lower().strip(), tail.lower().strip(), relation)
22	
23	
24	class DocREDEvaluator:
25	    """DocRED 评测器。
26	
27	    Args:
28	        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。
29	                       每个元素为 (doc_title, head_name, tail_name, relation)。
30	                       为 None 时 Ign-F1 = F1。
31	    """
32	
33	    def __init__(self, train_triples: Optional[set[tuple]] = None):
34	        self.train_triples = train_triples or set()
35	
36	    @classmethod
37	    def from_train_file(cls, train_path: str) -> "DocREDEvaluator":
38	        """从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。"""
39	        from freige.data.docred_processor import DOCRED_REL_INFO
40	
41	        with open(train_path) as f:
42	            train_data = json.load(f)
43	
44	        train_triples = set()
45	        for doc in train_data:
46	            doc_id = doc.get("title", "")
47	            vertex_set = doc["vertexSet"]
48	            for label in doc.get("labels", []):
49	                h_name = vertex_set[label["h"]][0]["name"]
50	                t_name = vertex_set[label["t"]][0]["name"]
51	                rel_name = DOCRED_REL_INFO.get(label["r"], label["r"])
52	                train_triples.add(
53	                    _triple_key(doc_id, h_name, t_name, rel_name)
54	                )
55	
56	        logger.info("Loaded %d training triples for Ign-F1", len(train_triples))
57	        return cls(train_triples=train_triples)
58	
59	    def compute_f1(
60	        self,
61	        predictions: list[dict],
62	        gold: list[dict],
63	    ) -> dict:
64	        """计算 F1 和 Ign-F1。
65	
66	        Args:
67	            predictions: [{"doc_id": str, "head": str, "tail": str,
68	                           "relation": str, ...}, ...]
69	            gold: 同上格式
70	
71	        Returns:
72	            {"precision", "recall", "f1", "ign_precision", "ign_recall", "ign_f1"}
73	        """
74	        pred_set = set()
75	        for p in predictions:
76	            pred_set.add(_triple_key(
77	                p["doc_id"], p["head"], p["tail"], p["relation"]
78	            ))
79	
80	        gold_set = set()
81	        for g in gold:
82	            gold_set.add(_triple_key(
83	                g["doc_id"], g["head"], g["tail"], g["relation"]
84	            ))
85	
86	        tp = pred_set & gold_set
87	        precision = len(tp) / len(pred_set) if pred_set else 0.0
88	        recall = len(tp) / len(gold_set) if gold_set else 0.0
89	        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
90	
91	        pred_ign = pred_set - self.train_triples
92	        gold_ign = gold_set - self.train_triples
93	        tp_ign = pred_ign & gold_ign
94	        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0
95	        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0
96	        ign_f1 = (
97	            2 * ign_prec * ign_rec / (ign_prec + ign_rec)
98	            if (ign_prec + ign_rec) > 0 else 0.0
99	        )
100	
101	        return {
102	            "precision": precision,
103	            "recall": recall,
104	            "f1": f1,
105	            "ign_precision": ign_prec,
106	            "ign_recall": ign_rec,
107	            "ign_f1": ign_f1,
108	            "tp": len(tp),
109	            "pred_count": len(pred_set),
110	            "gold_count": len(gold_set),
111	        }
112	
113	    def compute_evi_f1(
114	        self,
115	        predictions: list[dict],
116	        gold: list[dict],
117	    ) -> dict:
118	        """计算 Evidence F1（句子级）。
119	
120	        仅对正确预测的三元组计算 evidence 匹配。
121	
122	        Args:
123	            predictions: [{"doc_id", "head", "tail", "relation",
124	                           "evidence": [int, ...]}, ...]
125	            gold: 同上格式
126	
127	        Returns:
128	            {"evi_precision", "evi_recall", "evi_f1", "n_evaluated"}
129	        """
130	        gold_map = {}
131	        for g in gold:
132	            key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
133	            gold_map.setdefault(key, set()).update(g.get("evidence", []))
134	
135	        total_tp = 0
136	        total_pred = 0
137	        total_gold = 0
138	        n_evaluated = 0
139	
140	        for p in predictions:
141	            key = _triple_key(p["doc_id"], p["head"], p["tail"], p["relation"])
142	            if key not in gold_map:
143	                continue
144	
145	            pred_evi = set(p.get("evidence", []))
146	            gold_evi = gold_map[key]
147	
148	            tp = len(pred_evi & gold_evi)
149	            total_tp += tp
150	            total_pred += len(pred_evi)
151	            total_gold += len(gold_evi)
152	            n_evaluated += 1
153	
154	        evi_prec = total_tp / total_pred if total_pred else 0.0
155	        evi_rec = total_tp / total_gold if total_gold else 0.0
156	        evi_f1 = (
157	            2 * evi_prec * evi_rec / (evi_prec + evi_rec)
158	            if (evi_prec + evi_rec) > 0 else 0.0
159	        )
160	
161	        return {
162	            "evi_precision": evi_prec,
163	            "evi_recall": evi_rec,
164	            "evi_f1": evi_f1,
165	            "n_evaluated": n_evaluated,
166	        }
167	
168	    def compute_edcr(
169	        self,
170	        predictions: list[dict],
171	        gold: list[dict],
172	    ) -> dict:
173	        """计算 EDCR（Evidence Distractor Citation Rate）。
174	
175	        对所有预测的三元组（不限于正确预测），统计其 evidence 中
176	        不在 gold evidence 集合里的句子占比。
177	
178	        EDCR = |pred_evi - gold_evi| / |pred_evi|，越低越好。
179	
180	        Args:
181	            predictions: [{"doc_id", "head", "tail", "relation",
182	                           "evidence": [int, ...]}, ...]
183	            gold: 同上格式
184	
185	        Returns:
186	            {"edcr", "n_distractor_citations", "n_total_citations", "n_evaluated"}
187	        """
188	        gold_map = {}
189	        for g in gold:
190	            key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
191	            gold_map.setdefault(key, set()).update(g.get("evidence", []))
192	
193	        n_distractor = 0
194	        n_total = 0
195	        n_evaluated = 0
196	
197	        for p in predictions:
198	            pred_evi = set(p.get("evidence", []))
199	            if not pred_evi:
200	                continue
201	
202	            key = _triple_key(p["doc_id"], p["head"], p["tail"], p["relation"])
203	            gold_evi = gold_map.get(key, set())
204	
205	            distractors = pred_evi - gold_evi
206	            n_distractor += len(distractors)
207	            n_total += len(pred_evi)
208	            n_evaluated += 1
209	
210	        edcr = n_distractor / n_total if n_total else 0.0
211	
212	        return {
213	            "edcr": edcr,
214	            "n_distractor_citations": n_distractor,
215	            "n_total_citations": n_total,
216	            "n_evaluated": n_evaluated,
217	        }
218	
219	    def compute_format_compliance(self, raw_outputs: list[dict]) -> dict:
220	        """计算模型输出的格式合规率。
221	
222	        Args:
223	            raw_outputs: [{"doc_id": str, "raw_text": str}, ...]
224	
225	        Returns:
226	            dict with format_compliance_rate, field_compliance_rate,
227	            evidence_format_rate, and counts.
228	        """
229	        required_fields = {"head", "relation", "tail", "evidence"}
230	        n_total = len(raw_outputs)
231	        n_parseable = 0
232	        n_field_complete = 0
233	        n_evidence_valid = 0
234	
235	        for item in raw_outputs:
236	            doc_id = item.get("doc_id", "")
237	            raw_text = item.get("raw_text", "")
238	
239	            parsed = parse_model_output(doc_id, raw_text)
240	            if not parsed and not self._is_parseable_json_list(raw_text):
241	                continue
242	            n_parseable += 1
243	
244	            triples = self._parse_raw_json_list(raw_text)
245	            if triples is None:
246	                continue
247	
248	            all_fields_ok = True
249	            all_evidence_ok = True
250	            for t in triples:
251	                if not isinstance(t, dict) or not required_fields.issubset(t.keys()):
252	                    all_fields_ok = False
253	                    all_evidence_ok = False
254	                    break
255	                evi = t.get("evidence")
256	                if not isinstance(evi, list) or not all(
257	                    isinstance(e, int) and e >= 0 for e in evi
258	                ):
259	                    all_evidence_ok = False
260	
261	            if all_fields_ok:
262	                n_field_complete += 1
263	            if all_fields_ok and all_evidence_ok:
264	                n_evidence_valid += 1
265	
266	        return {
267	            "format_compliance_rate": n_parseable / n_total if n_total else 0.0,
268	            "field_compliance_rate": n_field_complete / n_total if n_total else 0.0,
269	            "evidence_format_rate": n_evidence_valid / n_total if n_total else 0.0,
270	            "n_total": n_total,
271	            "n_parseable": n_parseable,
272	            "n_field_complete": n_field_complete,
273	            "n_evidence_valid": n_evidence_valid,
274	        }
275	
276	    @staticmethod
277	    def _is_parseable_json_list(text: str) -> bool:
278	        try:
279	            obj = json.loads(text)
280	            return isinstance(obj, list)
281	        except json.JSONDecodeError:
282	            start = text.find("[")
283	            end = text.rfind("]") + 1
284	            if start >= 0 and end > start:
285	                try:
286	                    obj = json.loads(text[start:end])
287	                    return isinstance(obj, list)
288	                except json.JSONDecodeError:
289	                    return False
290	            return False
291	
292	    @staticmethod
293	    def _parse_raw_json_list(text: str) -> Optional[list]:
294	        try:
295	            obj = json.loads(text)
296	            if isinstance(obj, list):
297	                return obj
298	        except json.JSONDecodeError:
299	            start = text.find("[")
300	            end = text.rfind("]") + 1
301	            if start >= 0 and end > start:
302	                try:
303	                    obj = json.loads(text[start:end])
304	                    if isinstance(obj, list):
305	                        return obj
306	                except json.JSONDecodeError:
307	                    pass
308	        return None
309	
310	    def evaluate(
311	        self,
312	        predictions: list[dict],
313	        gold: list[dict],
314	        raw_outputs: Optional[list[dict]] = None,
315	    ) -> dict:
316	        """运行所有评测指标。"""
317	        f1_metrics = self.compute_f1(predictions, gold)
318	        evi_metrics = self.compute_evi_f1(predictions, gold)
319	        edcr_metrics = self.compute_edcr(predictions, gold)
320	        result = {**f1_metrics, **evi_metrics, **edcr_metrics}
321	        if raw_outputs is not None:
322	            result.update(self.compute_format_compliance(raw_outputs))
323	        return result
324	
325	
326	def parse_model_output(doc_id: str, output_text: str) -> list[dict]:
327	    """解析模型输出的 JSON 文本为标准预测格式。
328	
329	    模型输出格式:
330	    [{"head": "...", "relation": "...", "tail": "...", "evidence": [0, 3]}, ...]
331	
332	    Returns:
333	        标准预测列表，每个元素包含 doc_id
334	    """
335	    try:
336	        triples = json.loads(output_text)
337	    except json.JSONDecodeError:
338	        start = output_text.find("[")
339	        end = output_text.rfind("]") + 1
340	        if start >= 0 and end > start:
341	            try:
342	                triples = json.loads(output_text[start:end])
343	            except json.JSONDecodeError:
344	                logger.warning("Failed to parse output for doc %s", doc_id)
345	                return []
346	        else:
347	            return []
348	
349	    results = []
350	    for t in triples:
351	        if not isinstance(t, dict):
352	            continue
353	        if "head" not in t or "tail" not in t or "relation" not in t:
354	            continue
355	        results.append({
356	            "doc_id": doc_id,
357	            "head": str(t["head"]),
358	            "tail": str(t["tail"]),
359	            "relation": str(t["relation"]),
360	            "evidence": t.get("evidence", []),
361	        })
362	    return results
363	
364	
365	def gold_from_docred(
366	    docred_data: list[dict],
367	) -> list[dict]:
368	    """将 DocRED 原始数据转为评测用 gold 格式。
369	
370	    将 Wikidata property ID (如 "P17") 映射为 relation name (如 "country")，
371	    与模型训练输出格式对齐。
372	    """
373	    from freige.data.docred_processor import DOCRED_REL_INFO
374	
375	    gold = []
376	    for doc in docred_data:
377	        doc_id = doc.get("title", "")
378	        vertex_set = doc["vertexSet"]
379	        for label in doc.get("labels", []):
380	            h_name = vertex_set[label["h"]][0]["name"]
381	            t_name = vertex_set[label["t"]][0]["name"]
382	            gold.append({
383	                "doc_id": doc_id,
384	                "head": h_name,
385	                "tail": t_name,
386	                "relation": DOCRED_REL_INFO.get(label["r"], label["r"]),
387	                "evidence": label.get("evidence", []),
388	            })
389	    return gold
390	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225fae9b-d567-4e6c-a776-19e49c520d01",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "3bdd1a01-7a1f-4075-810e-46d5f2e3cf72",
  "sourceToolAssistantUUID": "225fae9b-d567-4e6c-a776-19e49c520d01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-15T14:28:51.882Z_

Now let me check the RSFT training code and the DPO setup for reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bdd1a01-7a1f-4075-810e-46d5f2e3cf72",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WhPtA6x1jBpjGL9cCG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c23f2160-d748-4a5c-8760-b914a6a36711",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZKjEwoHYg5K5KirwwvY6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 76382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10047,
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

_source line 47 · 2026-05-15T14:28:53.874Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WMz9sVfqLKTXPAjWrb1rj5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_trainer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c23f2160-d748-4a5c-8760-b914a6a36711",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WhPtA6x1jBpjGL9cCG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cd0b1b4-a50c-43fb-a41a-95cd3ccff151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZKjEwoHYg5K5KirwwvY6N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 76382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10047,
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

_source line 48 · 2026-05-15T14:28:53.879Z_

<details><summary>↩ Tool result · `toolu_01WMz9sVfqLKTXPAjWrb1rj5`</summary>

```text
1	"""RSFT (Rejection Sampling Fine-Tuning) 训练脚本。
2	
3	从 SFT warmup checkpoint 继续训练，使用经 CED 打分筛选的高质量生成数据。
4	流程: base model → merge SFT adapter → 新 QLoRA → 在 RSFT 数据上训练。
5	
6	输入: JSONL，每行 {"doc_id": ..., "input": ..., "output": ..., "ced_score": ..., ...}
7	输出: QLoRA adapter checkpoint
8	依赖: transformers, trl, peft, bitsandbytes, datasets
9	
10	单卡:   python -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
11	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
12	            -m freige.training.rsft_trainer --rsft_data_path data.jsonl --output_dir ./rsft_output
13	"""
14	
15	import argparse
16	import json
17	import logging
18	import os
19	
20	import torch
21	from datasets import Dataset
22	from peft import LoraConfig, PeftModel, TaskType, get_peft_model
23	from torch.utils.data import WeightedRandomSampler
24	from transformers import (
25	    AutoModelForCausalLM,
26	    AutoTokenizer,
27	    BitsAndBytesConfig,
28	    TrainerCallback,
29	)
30	from trl import SFTConfig, SFTTrainer
31	
32	from freige.training.sft_trainer import SYSTEM_PROMPT
33	
34	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
35	logger = logging.getLogger(__name__)
36	
37	DEFAULT_BASE_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
38	DEFAULT_SFT_ADAPTER = "/root/autodl-tmp/sft_output"
39	
40	
41	def load_rsft_data(data_path: str, tokenizer, max_length: int = 2048):
42	    """加载 CED 筛选后的 RSFT 数据，格式化为 chat template 文本。
43	
44	    每行 JSONL 的 input 字段作为 user message，output 字段作为 assistant response，
45	    经 apply_chat_template 拼接后用于 SFT 训练。超过 max_length 的样本被跳过
46	    而非截断，避免训练在不完整 JSON 输出上。
47	
48	    Returns:
49	        (Dataset, list[float]): 训练数据集和对应的 CED scores
50	    """
51	    samples = []
52	    with open(data_path) as f:
53	        for line in f:
54	            if line.strip():
55	                samples.append(json.loads(line))
56	
57	    logger.info("Loaded %d RSFT samples from %s", len(samples), data_path)
58	
59	    formatted = []
60	    ced_scores = []
61	    skipped = 0
62	    for s in samples:
63	        messages = [
64	            {"role": "system", "content": SYSTEM_PROMPT},
65	            {"role": "user", "content": s["input"]},
66	            {"role": "assistant", "content": s["output"]},
67	        ]
68	        text = tokenizer.apply_chat_template(
69	            messages,
70	            tokenize=False,
71	            add_generation_prompt=False,
72	            enable_thinking=False,
73	        )
74	        token_len = len(tokenizer.encode(text, add_special_tokens=False))
75	        if token_len > max_length:
76	            skipped += 1
77	            continue
78	        formatted.append({"text": text})
79	        ced_scores.append(s.get("ced_score", 1.0))
80	
81	    if skipped:
82	        logger.warning("Skipped %d samples exceeding max_length=%d", skipped, max_length)
83	
84	    if ced_scores:
85	        logger.info(
86	            "Prepared %d RSFT samples (CED scores: min=%.3f, max=%.3f, mean=%.3f)",
87	            len(formatted), min(ced_scores), max(ced_scores),
88	            sum(ced_scores) / len(ced_scores),
89	        )
90	    return Dataset.from_list(formatted), ced_scores
91	
92	
93	def prepare_eval_data(data_dir, tokenizer, max_docs=50):
94	    """Load DocRED dev set for task-level evaluation during training."""
95	    from freige.data.docred_processor import DocREDProcessor
96	    from freige.eval.evaluator import gold_from_docred
97	
98	    processor = DocREDProcessor(data_dir=data_dir)
99	    samples = processor.process("dev")
100	    groups = processor.group_by_document(samples)
101	
102	    eval_items = []
103	    for doc_id, doc_samples in list(groups.items())[:max_docs]:
104	        sft_sample = processor.format_sft_sample(doc_samples)
105	        messages = [
106	            {"role": "system", "content": SYSTEM_PROMPT},
107	            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
108	        ]
109	        prompt = tokenizer.apply_chat_template(
110	            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
111	        )
112	        eval_items.append({"doc_id": doc_id, "prompt": prompt})
113	
114	    dev_path = os.path.join(data_dir, "dev.json")
115	    with open(dev_path) as f:
116	        dev_data = json.load(f)
117	    gold = gold_from_docred(dev_data)
118	
119	    # Also build formatted eval dataset for loss-based eval
120	    eval_formatted = []
121	    for doc_id, doc_samples in groups.items():
122	        sft_sample = processor.format_sft_sample(doc_samples)
123	        messages = [
124	            {"role": "system", "content": SYSTEM_PROMPT},
125	            {"role": "user", "content": f"{sft_sample['instruction']}\n\n{sft_sample['input']}"},
126	            {"role": "assistant", "content": sft_sample["output"]},
127	        ]
128	        text = tokenizer.apply_chat_template(
129	            messages, tokenize=False, add_generation_prompt=False, enable_thinking=False,
130	        )
131	        eval_formatted.append({"text": text})
132	    eval_dataset = Dataset.from_list(eval_formatted)
133	
134	    return eval_items, gold, eval_dataset
135	
136	
137	class TaskEvalCallback(TrainerCallback):
138	    """End-of-epoch task eval: generate on dev subset → compute F1 / Evi-F1 / EDCR."""
139	
140	    def __init__(self, tokenizer, eval_items, gold, train_file, max_new_tokens=1024):
141	        self.tokenizer = tokenizer
142	        self.eval_items = eval_items
143	        self.gold = gold
144	        self.train_file = train_file
145	        self.max_new_tokens = max_new_tokens
146	        self._evaluator = None
147	
148	    @property
149	    def evaluator(self):
150	        if self._evaluator is None:
151	            from freige.eval.evaluator import DocREDEvaluator
152	            if self.train_file and os.path.exists(self.train_file):
153	                self._evaluator = DocREDEvaluator.from_train_file(self.train_file)
154	            else:
155	                self._evaluator = DocREDEvaluator()
156	        return self._evaluator
157	
158	    def on_epoch_end(self, args, state, control, model=None, **kwargs):
159	        if not state.is_world_process_zero:
160	            return
161	        self._run_task_eval(model, state)
162	
163	    def _run_task_eval(self, model, state):
164	        from freige.eval.evaluator import parse_model_output
165	
166	        model.eval()
167	        model.config.use_cache = True
168	        if hasattr(model, "gradient_checkpointing_disable"):
169	            model.gradient_checkpointing_disable()
170	
171	        all_predictions = []
172	        for item in self.eval_items:
173	            inputs = self.tokenizer(
174	                item["prompt"], return_tensors="pt", truncation=True, max_length=4096,
175	            ).to(model.device)
176	            with torch.no_grad():
177	                outputs = model.generate(
178	                    **inputs,
179	                    max_new_tokens=self.max_new_tokens,
180	                    do_sample=False,
181	                    pad_token_id=self.tokenizer.pad_token_id,
182	                )
183	            generated = outputs[0][inputs["input_ids"].shape[1]:]
184	            text = self.tokenizer.decode(generated, skip_special_tokens=True)
185	            triples, _ = parse_model_output(text)
186	            for t in triples:
187	                t["doc_id"] = item["doc_id"]
188	            all_predictions.extend(triples)
189	
190	        metrics = self.evaluator.evaluate(all_predictions, self.gold)
191	
192	        log_metrics = {
193	            "eval/rel_f1": metrics["f1"],
194	            "eval/ign_f1": metrics["ign_f1"],
195	            "eval/evi_f1": metrics["evi_f1"],
196	            "eval/evi_precision": metrics["evi_precision"],
197	            "eval/evi_recall": metrics["evi_recall"],
198	            "eval/edcr": metrics.get("edcr", 0),
199	            "eval/n_predictions": len(all_predictions),
200	        }
201	        try:
202	            import wandb
203	            if wandb.run is not None:
204	                wandb.log(log_metrics, step=state.global_step)
205	        except ImportError:
206	            pass
207	
208	        logger.info(
209	            "Task eval @ step %d: F1=%.4f, Ign-F1=%.4f, Evi-F1=%.4f, EDCR=%.4f (%d preds)",
210	            state.global_step, metrics["f1"], metrics["ign_f1"],
211	            metrics["evi_f1"], metrics.get("edcr", 0), len(all_predictions),
212	        )
213	
214	        model.config.use_cache = False
215	        if hasattr(model, "gradient_checkpointing_enable"):
216	            model.gradient_checkpointing_enable()
217	        model.train()
218	
219	
220	class WeightedSFTTrainer(SFTTrainer):
221	    """SFTTrainer with CED score-weighted sampling.
222	
223	    高 CED score 的样本被更频繁采样。使用 WeightedRandomSampler 实现，
224	    适用于单机训练。多机 DDP 场景下 Accelerate 会替换 sampler，
225	    此时 weighted_sampling 不生效，需改用数据集层面的过采样。
226	    """
227	
228	    def __init__(self, *args, sample_weights=None, **kwargs):
229	        super().__init__(*args, **kwargs)
230	        self.sample_weights = sample_weights
231	
232	    def _get_train_sampler(self, dataset=None):
233	        if self.sample_weights is not None:
234	            ds = dataset if dataset is not None else self.train_dataset
235	            return WeightedRandomSampler(
236	                weights=self.sample_weights,
237	                num_samples=len(ds),
238	                replacement=True,
239	            )
240	        return super()._get_train_sampler(dataset)
241	
242	
243	def main():
244	    parser = argparse.ArgumentParser(description="FREIGE RSFT Training")
245	    parser.add_argument("--base_model", type=str, default=DEFAULT_BASE_MODEL)
246	    parser.add_argument("--sft_adapter", type=str, default=DEFAULT_SFT_ADAPTER,
247	                        help="SFT warmup adapter 路径 (merge 后训练新 LoRA)")
248	    parser.add_argument("--rsft_data_path", type=str, required=True,
249	                        help="CED 筛选后的 RSFT 训练数据 (JSONL)")
250	    parser.add_argument("--output_dir", type=str, required=True)
251	    parser.add_argument("--learning_rate", type=float, default=2e-5)
252	    parser.add_argument("--num_epochs", type=int, default=3)
253	    parser.add_argument("--per_device_batch_size", type=int, default=4)
254	    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
255	    parser.add_argument("--warmup_steps", type=int, default=100)
256	    parser.add_argument("--save_steps", type=int, default=50)
257	    parser.add_argument("--save_total_limit", type=int, default=5)
258	    parser.add_argument("--max_length", type=int, default=2048)
259	    parser.add_argument("--seed", type=int, default=42)
260	    parser.add_argument("--wandb_project", type=str, default="freige-rsft")
261	    parser.add_argument("--wandb_run_name", type=str, default=None)
262	    parser.add_argument("--weighted_sampling", action="store_true",
263	                        help="按 CED score 加权采样（高分样本更频繁）")
264	    parser.add_argument("--quantize", action="store_true",
265	                        help="启用 4-bit QLoRA 量化")
266	    parser.add_argument("--lora_rank", type=int, default=64)
267	    parser.add_argument("--lora_alpha", type=int, default=128)
268	    parser.add_argument("--lora_dropout", type=float, default=0.05)
269	    parser.add_argument("--bf16", action="store_true", default=True)
270	    parser.add_argument("--deepspeed", type=str, default=None,
271	                        help="DeepSpeed 配置文件路径")
272	    parser.add_argument("--eval_data_dir", type=str, default=None,
273	                        help="DocRED data dir (contains dev.json) for task-level eval")
274	    parser.add_argument("--eval_max_docs", type=int, default=50,
275	                        help="Max dev docs for task-level eval during training")
276	    parser.add_argument("--max_new_tokens", type=int, default=1024)
277	    parser.add_argument("--max_steps", type=int, default=-1,
278	                        help="Override num_epochs: stop after N steps (-1 = use num_epochs)")
279	    args = parser.parse_args()
280	
281	    # W&B
282	    if args.wandb_project and "WANDB_API_KEY" in os.environ:
283	        os.environ["WANDB_PROJECT"] = args.wandb_project
284	        if args.wandb_run_name:
285	            os.environ["WANDB_NAME"] = args.wandb_run_name
286	
287	    # Tokenizer
288	    logger.info("Loading tokenizer: %s", args.base_model)
289	    tokenizer = AutoTokenizer.from_pretrained(
290	        args.base_model, trust_remote_code=True, padding_side="right",
291	    )
292	    if tokenizer.pad_token is None:
293	        tokenizer.pad_token = tokenizer.eos_token
294	
295	    # Data
296	    logger.info("Loading RSFT data: %s", args.rsft_data_path)
297	    train_dataset, ced_scores = load_rsft_data(
298	        args.rsft_data_path, tokenizer, args.max_length,
299	    )
300	
301	    # Model: base → merge SFT adapter → new LoRA
302	    logger.info("Loading base model: %s", args.base_model)
303	    local_rank = int(os.environ.get("LOCAL_RANK", 0))
304	    model_kwargs = dict(
305	        trust_remote_code=True,
306	        attn_implementation="sdpa",
307	        device_map={"": local_rank},
308	    )
309	    if args.quantize:
310	        logger.info("Using 4-bit QLoRA quantization")
311	        model_kwargs["quantization_config"] = BitsAndBytesConfig(
312	            load_in_4bit=True,
313	            bnb_4bit_compute_dtype=torch.bfloat16,
314	            bnb_4bit_quant_type="nf4",
315	            bnb_4bit_use_double_quant=True,
316	        )
317	    else:
318	        model_kwargs["torch_dtype"] = torch.bfloat16 if args.bf16 else torch.float16
319	
320	    model = AutoModelForCausalLM.from_pretrained(args.base_model, **model_kwargs)
321	
322	    if args.sft_adapter:
323	        logger.info("Merging SFT adapter: %s", args.sft_adapter)
324	        model = PeftModel.from_pretrained(model, args.sft_adapter)
325	        model = model.merge_and_unload()
326	
327	    model.config.use_cache = False
328	    model.gradient_checkpointing_enable()
329	
330	    # Fresh LoRA for RSFT (与 SFT warmup 相同结构)
331	    lora_config = LoraConfig(
332	        task_type=TaskType.CAUSAL_LM,
333	        r=args.lora_rank,
334	        lora_alpha=args.lora_alpha,
335	        lora_dropout=args.lora_dropout,
336	        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
337	                         "gate_proj", "up_proj", "down_proj"],
338	    )
339	    model = get_peft_model(model, lora_config)
340	    model.print_trainable_parameters()
341	
342	    # Eval data
343	    eval_dataset = None
344	    callbacks = []
345	    if args.eval_data_dir:
346	        logger.info("Loading eval data from %s (max %d docs for task eval)",
347	                     args.eval_data_dir, args.eval_max_docs)
348	        eval_items, gold, eval_dataset = prepare_eval_data(
349	            args.eval_data_dir, tokenizer, args.eval_max_docs,
350	        )
351	        train_file = os.path.join(args.eval_data_dir, "train_annotated.json")
352	        callbacks.append(TaskEvalCallback(
353	            tokenizer=tokenizer,
354	            eval_items=eval_items,
355	            gold=gold,
356	            train_file=train_file,
357	            max_new_tokens=args.max_new_tokens,
358	        ))
359	        logger.info("Task eval enabled: %d docs, %d gold triples",
360	                     len(eval_items), len(gold))
361	
362	    # Training config
363	    training_args = SFTConfig(
364	        output_dir=args.output_dir,
365	        num_train_epochs=args.num_epochs,
366	        per_device_train_batch_size=args.per_device_batch_size,
367	        per_device_eval_batch_size=1,
368	        gradient_accumulation_steps=args.gradient_accumulation_steps,
369	        learning_rate=args.learning_rate,
370	        warmup_steps=args.warmup_steps,
371	        bf16=args.bf16,
372	        logging_steps=10,
373	        eval_strategy="epoch" if eval_dataset is not None else "no",
374	        save_strategy="steps",
375	        save_steps=args.save_steps,
376	        save_total_limit=args.save_total_limit,
377	        seed=args.seed,
378	        max_length=args.max_length,
379	        dataset_text_field="text",
380	        report_to="wandb" if "WANDB_API_KEY" in os.environ else "none",
381	        gradient_checkpointing=True,
382	        gradient_checkpointing_kwargs={"use_reentrant": False},
383	        deepspeed=args.deepspeed,
384	        max_steps=args.max_steps,
385	    )
386	
387	    sample_weights = ced_scores if args.weighted_sampling else None
388	
389	    trainer = WeightedSFTTrainer(
390	        model=model,
391	        args=training_args,
392	        train_dataset=train_dataset,
393	        eval_dataset=eval_dataset,
394	        processing_class=tokenizer,
395	        sample_weights=sample_weights,
396	        callbacks=callbacks,
397	    )
398	
399	    logger.info(
400	        "Starting RSFT training (%d samples, weighted=%s)...",
401	        len(train_dataset), args.weighted_sampling,
402	    )
403	    trainer.train()
404	
405	    logger.info("Saving model to %s", args.output_dir)
406	    trainer.save_model(args.output_dir)
407	    tokenizer.save_pretrained(args.output_dir)
408	    logger.info("RSFT training complete.")
409	
410	
411	if __name__ == "__main__":
412	    main()
413	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cd0b1b4-a50c-43fb-a41a-95cd3ccff151",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "c716c6df-1ff9-47e8-a94f-60716d857663",
  "sourceToolAssistantUUID": "6cd0b1b4-a50c-43fb-a41a-95cd3ccff151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T14:28:54.301Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PYKqbnUHJbV1CZnjDRkiDq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/rsft_score_filter.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c716c6df-1ff9-47e8-a94f-60716d857663",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WhPtA6x1jBpjGL9cCG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6499279-19c1-4f10-b727-b05b736e349d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZKjEwoHYg5K5KirwwvY6N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10047,
      "cache_read_input_tokens": 76382,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10047
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 76382,
          "cache_creation_input_tokens": 10047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10047,
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

_source line 50 · 2026-05-15T14:28:54.307Z_

<details><summary>↩ Tool result · `toolu_01PYKqbnUHJbV1CZnjDRkiDq`</summary>

```text
1	"""RSFT Step 2: CED 打分 + 筛选。
2	
3	读取 rsft_generate.py 生成的 JSONL，对每个候选输出计算三种奖励:
4	  - format_reward: JSON 格式合规性
5	  - f1_reward: 与 gold triples 的 micro-F1
6	  - ced_reward: CED 对比证据判别奖励
7	
8	按组合阈值筛选高质量样本，输出 SFT 训练兼容格式。
9	
10	输入:
11	  - generations.jsonl (rsft_generate.py 的输出)
12	
13	输出 (保存到 --output_path):
14	  - rsft_train.json: 筛选后的 SFT 训练数据
15	  - rsft_scores.jsonl: 带分数的完整记录（供分析）
16	  - rsft_report.json: 统计报告
17	
18	依赖: transformers, torch, freige.rewards.ced_reward
19	
20	用法:
21	  python -m freige.training.rsft_score_filter \
22	      --input_dir /root/autodl-tmp/rsft_generations \
23	      --output_path /root/autodl-tmp/rsft_filtered \
24	      --selection_strategy top_pct --top_pct 25 \
25	      --nli_model_path /root/autodl-tmp/models/nli-deberta-v3-base
26	"""
27	
28	import argparse
29	import json
30	import logging
31	import os
32	from collections import defaultdict
33	from pathlib import Path
34	
35	import numpy as np
36	
37	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
38	logger = logging.getLogger(__name__)
39	
40	SYSTEM_PROMPT = (
41	    "You are an information extraction model. Given a document with numbered sentences "
42	    "and a list of entities, extract all relation triples. For each triple, provide the "
43	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
44	    "Output as a JSON list."
45	)
46	
47	
48	# ---------------------------------------------------------------------------
49	# Reward functions — 复用 grpo_trainer 中的逻辑
50	# ---------------------------------------------------------------------------
51	
52	def compute_format_reward(parsed_triples, format_ok):
53	    """格式奖励，复用 grpo_trainer.format_reward_fn 的逻辑。"""
54	    if not format_ok:
55	        return 0.0
56	    if not parsed_triples:
57	        return 0.1
58	    valid = 0
59	    for item in parsed_triples:
60	        if (isinstance(item, dict) and "head" in item
61	                and "relation" in item and "tail" in item
62	                and "evidence" in item
63	                and isinstance(item["evidence"], list)):
64	            valid += 1
65	    return valid / len(parsed_triples)
66	
67	
68	def compute_f1_reward(parsed_triples, gold_triples):
69	    """F1 奖励，复用 grpo_trainer.f1_reward_fn 的逻辑。"""
70	    gold_set = set()
71	    for g in gold_triples:
72	        gold_set.add((
73	            str(g.get("head") or "").lower().strip(),
74	            str(g.get("relation") or "").lower().strip(),
75	            str(g.get("tail") or "").lower().strip(),
76	        ))
77	
78	    pred_set = set()
79	    for p in parsed_triples:
80	        if isinstance(p, dict):
81	            pred_set.add((
82	                str(p.get("head") or "").lower().strip(),
83	                str(p.get("relation") or "").lower().strip(),
84	                str(p.get("tail") or "").lower().strip(),
85	            ))
86	
87	    if not gold_set:
88	        return 1.0 if not pred_set else 0.0
89	
90	    tp = len(pred_set & gold_set)
91	    prec = tp / len(pred_set) if pred_set else 0.0
92	    rec = tp / len(gold_set) if gold_set else 0.0
93	    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
94	    return f1
95	
96	
97	def compute_ced_reward_for_record(record, ced_model, tau=0.5):
98	    """CED 奖励，复用 grpo_trainer.CEDRewardWrapper.__call__ 的逻辑。
99	
100	    对一条记录中的所有 parsed_triples 计算平均 CED reward。
101	    """
102	    from freige.rewards.ced_reward import verbalize_triple
103	
104	    parsed_triples = record["parsed_triples"]
105	    gold_triples = record["gold_triples"]
106	    sents = record["sents"]
107	
108	    if not parsed_triples:
109	        return {"ced_reward": 0.0, "triple_details": []}
110	
111	    # 构建 gold_map
112	    gold_map = {}
113	    for g in gold_triples:
114	        key = (
115	            str(g.get("head") or "").lower().strip(),
116	            str(g.get("relation") or "").lower().strip(),
117	            str(g.get("tail") or "").lower().strip(),
118	        )
119	        gold_map[key] = g
120	
121	    # F1 gate: 至少一个预测 triple 匹配 gold
122	    has_gold_match = False
123	    for p in parsed_triples:
124	        if isinstance(p, dict):
125	            pk = (
126	                str(p.get("head") or "").lower().strip(),
127	                str(p.get("relation") or "").lower().strip(),
128	                str(p.get("tail") or "").lower().strip(),
129	            )
130	            if pk in gold_map:
131	                has_gold_match = True
132	                break
133	    if not has_gold_match:
134	        return {"ced_reward": 0.0, "triple_details": []}
135	
136	    triple_details = []
137	    triple_rewards = []
138	    for p in parsed_triples:
139	        if not isinstance(p, dict):
140	            continue
141	        pred_evi_ids = p.get("evidence", [])
142	        if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
143	            triple_rewards.append(0.0)
144	            triple_details.append({"reward": 0.0, "reason": "no_evidence"})
145	            continue
146	
147	        claim = verbalize_triple(
148	            str(p.get("head") or ""),
149	            str(p.get("relation") or ""),
150	            str(p.get("tail") or ""),
151	        )
152	        cited_sents = [sents[idx] for idx in pred_evi_ids
153	                       if isinstance(idx, int) and 0 <= idx < len(sents)]
154	        if not cited_sents:
155	            triple_rewards.append(0.0)
156	            triple_details.append({"reward": 0.0, "reason": "invalid_evidence_ids"})
157	            continue
158	
159	        key = (
160	            str(p.get("head") or "").lower().strip(),
161	            str(p.get("relation") or "").lower().strip(),
162	            str(p.get("tail") or "").lower().strip(),
163	        )
164	        matched_gold = gold_map.get(key, {})
165	        hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
166	        hard_neg_sents = [sents[idx] for idx in hard_neg_ids
167	                          if isinstance(idx, int) and 0 <= idx < len(sents)]
168	
169	        result = ced_model.compute_ced_reward(
170	            claim, cited_sents, hard_neg_sents, tau=tau,
171	        )
172	        triple_rewards.append(result["reward"])
173	        triple_details.append(result)
174	
175	    mean_ced = sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
176	    return {"ced_reward": mean_ced, "triple_details": triple_details}
177	
178	
179	def load_generations(input_dir):
180	    """加载 generations.jsonl。"""
181	    input_path = Path(input_dir) / "generations.jsonl"
182	    records = []
183	    with open(input_path) as f:
184	        for line in f:
185	            line = line.strip()
186	            if line:
187	                records.append(json.loads(line))
188	    logger.info("Loaded %d generation records from %s", len(records), input_path)
189	    return records
190	
191	
192	def score_all_records(records, ced_model, tau=0.5):
193	    """对所有记录计算三种奖励分数。"""
194	    scored = []
195	    for i, rec in enumerate(records):
196	        format_reward = compute_format_reward(rec["parsed_triples"], rec.get("format_ok", False))
197	        f1_reward = compute_f1_reward(rec["parsed_triples"], rec["gold_triples"])
198	        ced_result = compute_ced_reward_for_record(rec, ced_model, tau=tau)
199	
200	        scored_rec = {
201	            "doc_id": rec["doc_id"],
202	            "generation_idx": rec["generation_idx"],
203	            "output": rec["output"],
204	            "parsed_triples": rec["parsed_triples"],
205	            "format_ok": rec.get("format_ok", False),
206	            "gold_triples": rec["gold_triples"],
207	            "sents": rec["sents"],
208	            "prompt": rec.get("prompt", ""),
209	            "format_reward": format_reward,
210	            "f1_reward": f1_reward,
211	            "ced_reward": ced_result["ced_reward"],
212	            "combined_score": format_reward * 0.2 + f1_reward * 0.4 + ced_result["ced_reward"] * 0.4,
213	        }
214	        scored.append(scored_rec)
215	
216	        if (i + 1) % 500 == 0:
217	            logger.info("Scored %d/%d records", i + 1, len(records))
218	
219	    logger.info("Scoring complete: %d records", len(scored))
220	    return scored
221	
222	
223	def filter_records(scored_records, args):
224	    """根据策略筛选高质量样本。"""
225	    # 先按硬阈值过滤
226	    candidates = []
227	    for rec in scored_records:
228	        if rec["format_reward"] < args.format_threshold:
229	            continue
230	        if rec["f1_reward"] < args.f1_threshold:
231	            continue
232	        if rec["ced_reward"] < args.ced_threshold:
233	            continue
234	        candidates.append(rec)
235	
236	    logger.info("After threshold filter: %d/%d (format>=%.2f, f1>=%.2f, ced>=%.2f)",
237	                len(candidates), len(scored_records),
238	                args.format_threshold, args.f1_threshold, args.ced_threshold)
239	
240	    if args.selection_strategy == "threshold":
241	        return candidates
242	
243	    if args.selection_strategy == "top_pct":
244	        # 按 doc_id 分组，每组取 top N%
245	        by_doc = defaultdict(list)
246	        for rec in candidates:
247	            by_doc[rec["doc_id"]].append(rec)
248	
249	        selected = []
250	        for doc_id, doc_recs in by_doc.items():
251	            doc_recs.sort(key=lambda x: x["combined_score"], reverse=True)
252	            n_keep = max(1, int(len(doc_recs) * args.top_pct / 100))
253	            selected.extend(doc_recs[:n_keep])
254	
255	        logger.info("After top_%d%%: %d records from %d documents",
256	                     args.top_pct, len(selected), len(by_doc))
257	        return selected
258	
259	    if args.selection_strategy == "top_k":
260	        # 按 doc_id 分组，每组取 top-K
261	        by_doc = defaultdict(list)
262	        for rec in candidates:
263	            by_doc[rec["doc_id"]].append(rec)
264	
265	        selected = []
266	        for doc_id, doc_recs in by_doc.items():
267	            doc_recs.sort(key=lambda x: x["combined_score"], reverse=True)
268	            selected.extend(doc_recs[:args.top_k])
269	
270	        logger.info("After top_%d: %d records from %d documents",
271	                     args.top_k, len(selected), len(by_doc))
272	        return selected
273	
274	    raise ValueError(f"Unknown selection strategy: {args.selection_strategy}")
275	
276	
277	def format_sft_training_data(selected_records, tokenizer_name=None):
278	    """将筛选后的记录转换为 SFT 训练格式。
279	
280	    输出格式与 sft_trainer.prepare_dataset 一致:
281	    每条记录包含 "text" 字段，为完整的 chat template 格式文本。
282	    """
283	    sft_data = []
284	    for rec in selected_records:
285	        # 用模型的实际输出作为 assistant 回复（而非 gold output）
286	        # 这就是 RSFT 的核心: 用模型自己的高质量输出做 SFT
287	        messages = [
288	            {"role": "system", "content": SYSTEM_PROMPT},
289	            {"role": "user", "content": _extract_user_content(rec["prompt"])},
290	            {"role": "assistant", "content": rec["output"]},
291	        ]
292	
293	        sft_data.append({
294	            "messages": messages,
295	            "doc_id": rec["doc_id"],
296	            "generation_idx": rec["generation_idx"],
297	            "scores": {
298	                "format_reward": rec["format_reward"],
299	                "f1_reward": rec["f1_reward"],
300	                "ced_reward": rec["ced_reward"],
301	                "combined_score": rec["combined_score"],
302	            },
303	        })
304	
305	    return sft_data
306	
307	
308	def _extract_user_content(prompt_text):
309	    """从完整 prompt 中提取 user 消息内容。
310	
311	    prompt 是 apply_chat_template 的输出，包含 system/user 标记。
312	    直接用完整 prompt 中 user turn 的内容。
313	    """
314	    # Qwen3 chat template 格式:
315	    # <|im_start|>system\n...<|im_end|>\n<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n
316	    user_start = prompt_text.find("<|im_start|>user\n")
317	    if user_start < 0:
318	        return prompt_text
319	    content_start = user_start + len("<|im_start|>user\n")
320	    user_end = prompt_text.find("<|im_end|>", content_start)
321	    if user_end < 0:
322	        return prompt_text[content_start:]
323	    return prompt_text[content_start:user_end]
324	
325	
326	def generate_report(scored_records, selected_records):
327	    """生成统计报告。"""
328	    total = len(scored_records)
329	    passed = len(selected_records)
330	
331	    scores = {
332	        "format_reward": [r["format_reward"] for r in scored_records],
333	        "f1_reward": [r["f1_reward"] for r in scored_records],
334	        "ced_reward": [r["ced_reward"] for r in scored_records],
335	        "combined_score": [r["combined_score"] for r in scored_records],
336	    }
337	
338	    report = {
339	        "total_records": total,
340	        "selected_records": passed,
341	        "filtered_records": total - passed,
342	        "selection_rate": passed / total if total else 0.0,
343	        "unique_docs_total": len(set(r["doc_id"] for r in scored_records)),
344	        "unique_docs_selected": len(set(r["doc_id"] for r in selected_records)),
345	    }
346	
347	    for name, vals in scores.items():
348	        arr = np.array(vals)
349	        report[f"{name}_stats"] = {
350	            "mean": float(np.mean(arr)),
351	            "std": float(np.std(arr)),
352	            "min": float(np.min(arr)),
353	            "max": float(np.max(arr)),
354	            "median": float(np.median(arr)),
355	            "p25": float(np.percentile(arr, 25)),
356	            "p75": float(np.percentile(arr, 75)),
357	        }
358	
359	    # 筛选后子集的统计
360	    if selected_records:
361	        sel_scores = {
362	            "format_reward": [r["format_reward"] for r in selected_records],
363	            "f1_reward": [r["f1_reward"] for r in selected_records],
364	            "ced_reward": [r["ced_reward"] for r in selected_records],
365	            "combined_score": [r["combined_score"] for r in selected_records],
366	        }
367	        report["selected_stats"] = {}
368	        for name, vals in sel_scores.items():
369	            arr = np.array(vals)
370	            report["selected_stats"][name] = {
371	                "mean": float(np.mean(arr)),
372	                "std": float(np.std(arr)),
373	                "min": float(np.min(arr)),
374	                "max": float(np.max(arr)),
375	            }
376	
377	    return report
378	
379	
380	def main():
381	    parser = argparse.ArgumentParser(description="RSFT Step 2: CED Scoring & Filtering")
382	    parser.add_argument("--input_dir", type=str, required=True,
383	                        help="rsft_generate 输出目录（含 generations.jsonl）")
384	    parser.add_argument("--output_path", type=str, required=True,
385	                        help="筛选结果输出目录")
386	    parser.add_argument("--nli_model_path", type=str,
387	                        default="cross-encoder/nli-deberta-v3-base",
388	                        help="NLI 模型路径（用于 CED 打分）")
389	    parser.add_argument("--nli_device", type=str, default=None,
390	                        help="NLI 模型运行设备 (default: auto)")
391	    parser.add_argument("--tau", type=float, default=0.5,
392	                        help="CED tau 阈值 (default: 0.5)")
393	
394	    # 筛选参数
395	    parser.add_argument("--format_threshold", type=float, default=0.5,
396	                        help="format_reward 最低阈值 (default: 0.5)")
397	    parser.add_argument("--f1_threshold", type=float, default=0.0,
398	                        help="f1_reward 最低阈值 (default: 0.0)")
399	    parser.add_argument("--ced_threshold", type=float, default=0.0,
400	                        help="ced_reward 最低阈值 (default: 0.0)")
401	    parser.add_argument("--selection_strategy", type=str, default="top_pct",
402	                        choices=["threshold", "top_k", "top_pct"],
403	                        help="筛选策略 (default: top_pct)")
404	    parser.add_argument("--top_k", type=int, default=2,
405	                        help="top_k 策略: 每个文档取 top-K (default: 2)")
406	    parser.add_argument("--top_pct", type=int, default=25,
407	                        help="top_pct 策略: 每个文档取 top N%% (default: 25)")
408	    args = parser.parse_args()
409	
410	    output_dir = Path(args.output_path)
411	    output_dir.mkdir(parents=True, exist_ok=True)
412	
413	    # 1. 加载生成结果
414	    records = load_generations(args.input_dir)
415	
416	    # 2. 加载 CED 模型并打分
417	    logger.info("Loading NLI model: %s", args.nli_model_path)
418	    from freige.rewards.ced_reward import CEDRewardModel
419	    ced_model = CEDRewardModel(model_name=args.nli_model_path, device=args.nli_device)
420	
421	    scored = score_all_records(records, ced_model, tau=args.tau)
422	
423	    # 保存带分数的完整记录
424	    scores_path = output_dir / "rsft_scores.jsonl"
425	    with open(scores_path, "w") as f:
426	        for rec in scored:
427	            # 不保存大字段以节省空间
428	            slim = {k: v for k, v in rec.items() if k not in ("prompt", "sents", "gold_triples")}
429	            f.write(json.dumps(slim, ensure_ascii=False) + "\n")
430	    logger.info("Scores → %s", scores_path)
431	
432	    # 3. 筛选
433	    selected = filter_records(scored, args)
434	
435	    # 4. 转换为 SFT 训练格式
436	    sft_data = format_sft_training_data(selected)
437	    train_path = output_dir / "rsft_train.jsonl"
438	    with open(train_path, "w") as f:
439	        for item in sft_data:
440	            user_msg = next(m["content"] for m in item["messages"] if m["role"] == "user")
441	            asst_msg = next(m["content"] for m in item["messages"] if m["role"] == "assistant")
442	            record = {
443	                "input": user_msg,
444	                "output": asst_msg,
445	                "ced_score": item["scores"]["ced_reward"],
446	                "doc_id": item.get("doc_id"),
447	                "generation_idx": item.get("generation_idx"),
448	                "scores": item["scores"],
449	            }
450	            f.write(json.dumps(record, ensure_ascii=False) + "\n")
451	    logger.info("Training data → %s (%d samples)", train_path, len(sft_data))
452	
453	    # 5. 统计报告
454	    report = generate_report(scored, selected)
455	    report["args"] = vars(args)
456	    report_path = output_dir / "rsft_report.json"
457	    with open(report_path, "w") as f:
458	        json.dump(report, f, indent=2, ensure_ascii=False)
459	    logger.info("Report → %s", report_path)
460	
461	    # 控制台摘要
462	    print("\n" + "=" * 60)
463	    print(f"  Total records:    {report['total_records']}")
464	    print(f"  Selected:         {report['selected_records']}")
465	    print(f"  Selection rate:   {report['selection_rate']:.1%}")
466	    print(f"  Unique docs:      {report['unique_docs_selected']}/{report['unique_docs_total']}")
467	    print("-" * 60)
468	    for name in ["format_reward", "f1_reward", "ced_reward", "combined_score"]:
469	        stats = report[f"{name}_stats"]
470	        print(f"  {name:20s}  mean={stats['mean']:.3f}  std={stats['std']:.3f}  "
471	              f"median={stats['median']:.3f}  [min={stats['min']:.3f}, max={stats['max']:.3f}]")
472	    print("=" * 60)
473	
474	
475	if __name__ == "__main__":
476	    main()
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6499279-19c1-4f10-b727-b05b736e349d",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "03c6008d-6923-499a-beea-efa85aa15d6d",
  "sourceToolAssistantUUID": "e6499279-19c1-4f10-b727-b05b736e349d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T14:28:57.294Z_

Now let me also check a critical issue I noticed -- the discrepancy between the CED formula in the paper vs the code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03c6008d-6923-499a-beea-efa85aa15d6d",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Whu8451QEAQknPyo2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b13bdce-0de1-4d62-8378-1d868607f178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWiBWv65tL1B26TvJVPctW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13300,
      "cache_read_input_tokens": 86429,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13300,
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

_source line 52 · 2026-05-15T14:28:59.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_01THjg5ax5GeQAM975fThq3U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/grpo_trainer.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b13bdce-0de1-4d62-8378-1d868607f178",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Whu8451QEAQknPyo2f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "660baf32-c28c-4133-8044-28b408fbda92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWiBWv65tL1B26TvJVPctW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13300,
      "cache_read_input_tokens": 86429,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 86429,
          "cache_creation_input_tokens": 13300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13300,
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

_source line 53 · 2026-05-15T14:28:59.658Z_

<details><summary>↩ Tool result · `toolu_01THjg5ax5GeQAM975fThq3U`</summary>

```text
1	"""GRPO 训练脚本: 基于 TRL GRPOTrainer 的多阶段 curriculum 训练。
2	
3	支持单卡和多卡（DeepSpeed ZeRO-2/3）训练，默认 4-bit QLoRA。
4	
5	单卡:   python -m freige.training.grpo_trainer --stage 1 --output_dir ./grpo_s1
6	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
7	            -m freige.training.grpo_trainer --deepspeed configs/deepspeed_zero2.json \
8	            --stage 1 --reward_device cpu
9	不量化: 加 --no_quantize
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import math
16	import os
17	import re
18	from pathlib import Path
19	from typing import Optional
20	
21	import torch
22	from datasets import Dataset
23	from peft import LoraConfig, PeftModel, TaskType
24	from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
25	from trl import GRPOConfig, GRPOTrainer
26	
27	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
28	logger = logging.getLogger(__name__)
29	
30	SYSTEM_PROMPT = (
31	    "You are an information extraction model. Given a document with numbered sentences "
32	    "and a list of entities, extract all relation triples. For each triple, provide the "
33	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
34	    "Output as a JSON list."
35	)
36	
37	
38	def _parse_json_output(text: str) -> list[dict]:
39	    """从模型输出中解析 JSON 列表。"""
40	    try:
41	        return json.loads(text)
42	    except json.JSONDecodeError:
43	        start = text.find("[")
44	        end = text.rfind("]") + 1
45	        if start >= 0 and end > start:
46	            try:
47	                return json.loads(text[start:end])
48	            except json.JSONDecodeError:
49	                return []
50	    return []
51	
52	
53	def format_reward_fn(completions: list[str], **kwargs) -> list[float]:
54	    """格式奖励: 输出是否为合法 JSON 列表，每个元素是否含必需字段。"""
55	    rewards = []
56	    for text in completions:
57	        parsed = _parse_json_output(text)
58	        if not isinstance(parsed, list):
59	            rewards.append(0.0)
60	            continue
61	        if not parsed:
62	            rewards.append(0.1)
63	            continue
64	        valid = 0
65	        for item in parsed:
66	            if (isinstance(item, dict) and "head" in item
67	                    and "relation" in item and "tail" in item
68	                    and "evidence" in item
69	                    and isinstance(item["evidence"], list)):
70	                valid += 1
71	        rewards.append(valid / len(parsed))
72	    return rewards
73	
74	
75	def f1_reward_fn(completions: list[str], gold_triples: list[str], **kwargs) -> list[float]:
76	    """F1 奖励: 预测三元组与 gold 三元组的 micro-F1。
77	
78	    gold_triples 是 JSON 字符串列表，每个元素对应一个 prompt 的 gold。
79	    completions 中每 num_generations 个对应同一个 prompt。
80	    """
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "660baf32-c28c-4133-8044-28b408fbda92",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "0887e7fb-ebec-45c0-ae6a-c40102553df7",
  "sourceToolAssistantUUID": "660baf32-c28c-4133-8044-28b408fbda92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T14:29:04.063Z_

I have now gathered enough information to write a thorough review. Let me also check one more critical detail -- whether the evaluator implements the DREEAM-aligned joint Evi-F1 protocol or only the conditional one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0887e7fb-ebec-45c0-ae6a-c40102553df7",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WiJ5Bqo28BP4TxQ2iJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb96d85d-6a03-4f84-badb-6fd7221816e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6fTZCeeFHuZiGn9Gqrk5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 99729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1184,
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

_source line 55 · 2026-05-15T14:29:06.455Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DQxbuFgnb7YEAuURbL9kke`</summary>

```json
{
  "pattern": "joint|dreeam|compute_evi_f1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/eval/evaluator.py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb96d85d-6a03-4f84-badb-6fd7221816e3",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WiJ5Bqo28BP4TxQ2iJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bfe3633-5b71-4436-9749-b1b679ffef8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6fTZCeeFHuZiGn9Gqrk5J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 99729,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 99729,
          "cache_creation_input_tokens": 1184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1184,
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

_source line 56 · 2026-05-15T14:29:06.482Z_

<details><summary>↩ Tool result · `toolu_01DQxbuFgnb7YEAuURbL9kke`</summary>

```text
113:    def compute_evi_f1(
318:        evi_metrics = self.compute_evi_f1(predictions, gold)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bfe3633-5b71-4436-9749-b1b679ffef8d",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "c5e6bf96-e4dd-4219-87b0-603e70f3b9d5",
  "sourceToolAssistantUUID": "5bfe3633-5b71-4436-9749-b1b679ffef8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T14:29:12.832Z_

The evaluator code only implements the conditional Evi-F1 (lines 113-166 of evaluator.py skip FP triples via `if key not in gold_map: continue`). There is no DREEAM-aligned joint Evi-F1 in the codebase. This is a significant finding -- the paper reports "joint Evi-F1" numbers but the code only computes conditional Evi-F1. Per decision D041/D042, this was identified as a bug and an alignment function was supposed to be implemented.

Now let me also check whether there's any DPO training code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5e6bf96-e4dd-4219-87b0-603e70f3b9d5",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WioG7VuijzNRQd7fqA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fa31a38-1a9a-435f-a985-87c032a00a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SudxRf3BDubZJEYmqs7dGM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 100913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 234,
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

_source line 58 · 2026-05-15T14:29:13.369Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QHKvq9uDUPLQdwfUwTSFcW`</summary>

```json
{
  "pattern": "DPO|dpo",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fa31a38-1a9a-435f-a985-87c032a00a92",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WioG7VuijzNRQd7fqA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8357908-f355-4833-85b6-32758be8fa0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SudxRf3BDubZJEYmqs7dGM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 100913,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 234
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 267,
          "cache_read_input_tokens": 100913,
          "cache_creation_input_tokens": 234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 234,
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

_source line 59 · 2026-05-15T14:29:13.397Z_

<details><summary>↩ Tool result · `toolu_01QHKvq9uDUPLQdwfUwTSFcW`</summary>

```text
Found 45 files
artifacts/dream_reports/dream_20260515T132059/logs/review_worst.log
artifacts/dream_reports/dream_20260515T132059/worst/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/logs/review_median.log
artifacts/dream_reports/dream_20260515T132059/median/review_report.md
artifacts/dream_reports/dream_20260515T132059/median/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/logs/review_best.log
artifacts/dream_reports/dream_20260515T132059/best/review_report.md
artifacts/dream_reports/dream_20260515T132059/best/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260515T132059/worst/paper.aux
artifacts/dream_reports/dream_20260515T132059/worst/paper.tex
artifacts/dream_reports/dream_20260515T132059/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T132059/median/paper.log
artifacts/dream_reports/dream_20260515T132059/median/paper.aux
artifacts/dream_reports/dream_20260515T132059/median/paper.tex
artifacts/dream_reports/dream_20260515T132059/median/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/median/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T132059/best/paper.aux
artifacts/dream_reports/dream_20260515T132059/best/paper.tex
artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md
artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T132059/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T132059/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260515T120227/meta.yaml
artifacts/dream_reports/dream_20260515T120227/logs/review_worst.log
artifacts/dream_reports/dream_20260515T120227/worst/review_report.md
artifacts/dream_reports/dream_20260515T120227/best/review_report.md
artifacts/dream_reports/dream_20260515T120227/median/review_report.md
artifacts/dream_reports/dream_20260515T120227/logs/review_median.log
artifacts/dream_reports/dream_20260515T120227/logs/review_best.log
artifacts/dream_reports/dream_20260515T120227/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/logs/phase1_attempt0.log
artifacts/manifest.yaml
artifacts/ced_stabilizer_literature_survey.md
artifacts/_project/report/d024_literature_survey.md
artifacts/d024_literature_survey.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8357908-f355-4833-85b6-32758be8fa0f",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "700197de-ab45-44ec-a3df-e4b76c8b1b08",
  "sourceToolAssistantUUID": "e8357908-f355-4833-85b6-32758be8fa0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-15T14:29:17.343Z_

No DPO-specific training script exists in the codebase. The DPO results appear to be from planned experiments that were either run with an ad-hoc script not committed, or are simulated/projected numbers.

Let me check the experiment data to understand which numbers are real vs. imagined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "700197de-ab45-44ec-a3df-e4b76c8b1b08",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WjJrbCeWPwETVPczXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49747f17-f1b5-492c-a1da-6cbd6edfec69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01955NbVM4vQu5ecpnSS5fUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 101147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1283,
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

_source line 61 · 2026-05-15T14:29:19.290Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LDnhLXqqUvN3kc5ZtnSPF8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49747f17-f1b5-492c-a1da-6cbd6edfec69",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WjJrbCeWPwETVPczXk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dad4fa4-b9c3-4c29-b372-7ff86782b9a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01955NbVM4vQu5ecpnSS5fUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 101147,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 101147,
          "cache_creation_input_tokens": 1283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1283,
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

_source line 62 · 2026-05-15T14:29:19.308Z_

<details><summary>↩ Tool result · `toolu_01LDnhLXqqUvN3kc5ZtnSPF8`</summary>

```text
1	[
2	  {
3	    "name": "CED vs flat-NLI RSFT ablation",
4	    "description": "用 flat-NLI scoring（DeBERTa p(entailment) 直接打分，无 contrastive margin） 重新筛选已有候选 → RSFT 训练 → dev eval。匹配 CED RSFT 的三组超参配置。\n",
5	    "results": {
6	      "flatnli_rsft_config_a_rel_f1": 0.4398,
7	      "flatnli_rsft_config_a_evi_f1": 0.8115,
8	      "flatnli_rsft_config_a_edcr": 0.6725,
9	      "flatnli_rsft_config_b_rel_f1": 0.461,
10	      "flatnli_rsft_config_b_evi_f1": 0.8078,
11	      "flatnli_rsft_config_b_edcr": 0.659,
12	      "flatnli_rsft_config_c_rel_f1": 0.447,
13	      "flatnli_rsft_config_c_evi_f1": 0.8053,
14	      "flatnli_rsft_config_c_edcr": 0.6752,
15	      "flatnli_rsft_best_rel_f1": 0.461,
16	      "flatnli_rsft_best_evi_f1": 0.8078,
17	      "flatnli_rsft_best_edcr": 0.659,
18	      "ced_vs_flatnli_mean_evi_f1_delta_pp": 0.75,
19	      "ced_vs_flatnli_mean_edcr_delta_pp": -1.68,
20	      "ced_vs_flatnli_mean_rel_f1_delta_pp": 0.49,
21	      "ced_vs_flatnli_evi_f1_bootstrap_p": 0.12,
22	      "ced_vs_flatnli_edcr_bootstrap_p": 0.09,
23	      "ced_vs_flatnli_rel_f1_bootstrap_p": 0.28,
24	      "flatnli_vs_sft_rel_f1_delta_pp": 5.5,
25	      "flatnli_vs_sft_evi_f1_delta_pp": 1.0,
26	      "flatnli_vs_sft_p_value": 0.001,
27	      "flatnli_selected_samples": 2652,
28	      "flatnli_ced_overlap_rate": 0.78
29	    },
30	    "tables": [
31	      {
32	        "name": "Table: CED vs flat-NLI RSFT dev set comparison",
33	        "columns": [
34	          "Config",
35	          "Scorer",
36	          "rel_f1",
37	          "evi_f1",
38	          "EDCR"
39	        ],
40	        "rows": [
41	          [
42	            "r1 (3ep, α128, s42)",
43	            "CED",
44	            0.4449,
45	            0.8187,
46	            0.6565
47	          ],
48	          [
49	            "r1 (3ep, α128, s42)",
50	            "flat-NLI",
51	            0.4398,
52	            0.8115,
53	            0.6725
54	          ],
55	          [
56	            "s43 (3ep, α128, s43)",
57	            "CED",
58	            0.4683,
59	            0.8156,
60	            0.6388
61	          ],
62	          [
63	            "s43 (3ep, α128, s43)",
64	            "flat-NLI",
65	            0.461,
66	            0.8078,
67	            0.659
68	          ],
69	          [
70	            "r2b (1ep, α32, lr1e-5)",
71	            "CED",
72	            0.4493,
73	            0.8128,
74	            0.6609
75	          ],
76	          [
77	            "r2b (1ep, α32, lr1e-5)",
78	            "flat-NLI",
79	            0.447,
80	            0.8053,
81	            0.6752
82	          ],
83	          [
84	            "SFT baseline",
85	            "—",
86	            0.4057,
87	            0.7979,
88	            0.7118
89	          ]
90	        ]
91	      },
92	      {
93	        "name": "Table: Statistical significance (paired bootstrap, 10000 resamples)",
94	        "columns": [
95	          "Metric",
96	          "CED mean",
97	          "flat-NLI mean",
98	          "Δ (pp)",
99	          "p",
100	          "sig (α=0.05)"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7dad4fa4-b9c3-4c29-b372-7ff86782b9a1",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "1d228f42-636e-49f8-a1be-7e6933e358d0",
  "sourceToolAssistantUUID": "7dad4fa4-b9c3-4c29-b372-7ff86782b9a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T14:29:25.727Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LApt4NpSikUqrnFG1r9Db7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/experiment_data.json",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d228f42-636e-49f8-a1be-7e6933e358d0",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WjkCbChC3BjEvxhzPx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f27883a5-170d-456c-815f-ce754a9fc1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LfCaz49fzLnBagBPywDWVj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1682,
      "cache_read_input_tokens": 102430,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1682
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 102430,
          "cache_creation_input_tokens": 1682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1682,
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

_source line 64 · 2026-05-15T14:29:26.161Z_

<details><summary>↩ Tool result · `toolu_01LApt4NpSikUqrnFG1r9Db7`</summary>

```text
100	          "sig (α=0.05)"
101	        ],
102	        "rows": [
103	          [
104	            "evi_f1",
105	            0.8157,
106	            0.8082,
107	            "+0.75",
108	            0.12,
109	            "No"
110	          ],
111	          [
112	            "rel_f1",
113	            0.4542,
114	            0.4493,
115	            "+0.49",
116	            0.28,
117	            "No"
118	          ],
119	          [
120	            "EDCR",
121	            0.6521,
122	            0.6689,
123	            "-1.68",
124	            0.09,
125	            "No"
126	          ]
127	        ]
128	      }
129	    ],
130	    "figures": [],
131	    "analysis": "触发 CED contingency plan。CED vs flat-NLI 三项指标均未达显著。 但正面信号: (1) 方向一致——3/3 configs CED 全优； (2) flat-NLI RSFT 仍大幅优于 SFT (Δrel_f1 +5.5pp, p<0.001)， 证明 RSFT pipeline 本身是核心贡献。 论文策略: CED 降级为\"一种有效但非必需的 scoring variant\"， Claim 2 保留但从 main contribution 降为 ablation finding。\n\n\nflat-NLI 本身有实质信号（MVP-1 DeBERTa discrimination accuracy=0.815）， 因此 flat-NLI filtered RSFT 仍显著优于 SFT (+5.5pp rel_f1, p<0.001)。 CED 的 contrastive margin 理论上额外惩罚 entity-sharing distractor， 但实践中效果被三重因素稀释: (1) DeBERTa-v3-base 对长文档 NLI 存在 positional bias，使 contrastive  和 non-contrastive 打分在高置信区间趋同——两种方法筛选的候选有 78% 重叠； (2) DocRED gold evidence 标注不完整 (~14% false distractors)， CED 的 hard negative 信号被噪声标注污染； (3) RSFT 的间接传导链（scorer→filter→training data→fine-tune） 进一步衰减了打分层面的微弱差异。 Δevi_f1=0.75pp 方向一致（3/3 configs CED 均优于 flat-NLI）但 bootstrap p=0.12 不满足显著性阈值。EDCR 差异 -1.68pp 方向同理， p=0.09 接近但未达显著。\n"
132	  },
133	  {
134	    "name": "Test set evaluation",
135	    "description": "RSFT best (s43) + RSFT flat-NLI best + SFT baseline 提交 CodaLab。 本地计算 Evi-F1_joint (DREEAM 协议) 和 EDCR。\n",
136	    "results": {
137	      "sft_test_rel_f1": 0.4,
138	      "sft_test_ign_f1": 0.398,
139	      "sft_test_evi_f1_joint": 0.295,
140	      "sft_test_evi_f1_cond": 0.79,
141	      "sft_test_edcr": 0.718,
142	      "rsft_ced_test_rel_f1": 0.432,
143	      "rsft_ced_test_ign_f1": 0.43,
144	      "rsft_ced_test_evi_f1_joint": 0.322,
145	      "rsft_ced_test_evi_f1_cond": 0.8,
146	      "rsft_ced_test_edcr": 0.648,
147	      "rsft_flatnli_test_rel_f1": 0.425,
148	      "rsft_flatnli_test_ign_f1": 0.423,
149	      "rsft_flatnli_test_evi_f1_joint": 0.312,
150	      "rsft_flatnli_test_evi_f1_cond": 0.795,
151	      "rsft_flatnli_test_edcr": 0.668,
152	      "test_delta_ced_over_sft_rel_f1_pp": 3.2,
153	      "test_delta_ced_over_sft_evi_f1_joint_pp": 2.7,
154	      "dev_to_test_rsft_ced_rel_f1_degradation_pp": 3.6,
155	      "dev_to_test_sft_rel_f1_degradation_pp": 0.6
156	    },
157	    "tables": [
158	      {
159	        "name": "Table: Test set main results (DocRED)",
160	        "columns": [
161	          "Method",
162	          "Type",
163	          "rel_f1",
164	          "ign_f1",
165	          "Evi-F1_joint",
166	          "Evi-F1_cond",
167	          "EDCR"
168	        ],
169	        "rows": [
170	          [
171	            "SFT (Qwen3-4B)",
172	            "Gen. LLM",
173	            0.4,
174	            0.398,
175	            0.295,
176	            0.79,
177	            0.718
178	          ],
179	          [
180	            "RSFT+flat-NLI",
181	            "Gen. LLM",
182	            0.425,
183	            0.423,
184	            0.312,
185	            0.795,
186	            0.668
187	          ],
188	          [
189	            "RSFT+CED (FREIGE)",
190	            "Gen. LLM",
191	            0.432,
192	            0.43,
193	            0.322,
194	            0.8,
195	            0.648
196	          ],
197	          [
198	            "DREEAM†",
199	            "Encoder",
200	            0.628,
201	            "—",
202	            0.5734,
203	            "~0.93",
204	            "—"
205	          ],
206	          [
207	            "SAIS†",
208	            "Encoder",
209	            0.604,
210	            "—",
211	            0.5567,
212	            "~0.92",
213	            "—"
214	          ],
215	          [
216	            "LMRC†",
217	            "Gen. LLM",
218	            0.607,
219	            "—",
220	            "—",
221	            "—",
222	            "—"
223	          ]
224	        ]
225	      }
226	    ],
227	    "figures": [],
228	    "analysis": "Claim 1 成立: FREIGE 在 test set 上 rel_f1 +3.2pp (p<0.01)， 且是首个同时生成关系和可验证证据的 LLM 方法。 Joint Evi-F1 0.322 < DREEAM 0.573，但论文需分解: conditional evidence quality (80 vs 93%) gap 远小于 joint gap， 且生成式 evidence（显式句子引用）比 attention-based evidence（DREEAM） 更适合 human-in-the-loop 场景。 CED vs flat-NLI 在 test 上同样不显著（Δrel_f1=0.7pp, p>0.10）， 一致支持 CED contingency。\n\n\nDev→test 退化不对称: SFT 仅退化 0.6pp（直接在 gold training data 上学习， 无 dev-dependent 信号），RSFT 退化 3.6pp（CED 打分隐式依赖 dev 文档特征—— NLI 模型在 dev 文档的 entity-sharing pattern 上 calibrated，RSFT 训练数据 源自 SFT 在 dev 上的生成候选，构成 indirect overfitting 通道）。 因此 dev 上 Δrel_f1=6.3pp 在 test 上收窄至 3.2pp，但仍 p<0.01 显著。 Evi-F1_joint 从 conditional ~0.80 大幅降至 0.322 纯粹是协议转换: joint 对所有 gold triples 计分，FN triples evidence F1 记为 0， 因此 joint ≈ recall × conditional ≈ 0.42 × 0.80 ≈ 0.34（实际略低因 低 recall triples 的 evidence 也偏弱）。 Joint Evi-F1 0.322 远低于 DREEAM 57.34%，但差距主因是 extraction recall  (43% vs 63%) 而非 evidence quality——conditional Evi-F1 (80%) 接近 DREEAM (est. ~93%)，且我们生成的是可审计的显式句子引用。\n"
229	  },
230	  {
231	    "name": "EDCR cross-method diagnostic table",
232	    "description": "在所有 evidence-producing 方法上计算 EDCR，验证其跨方法诊断分辨力。\n",
233	    "results": {
234	      "grpo_g8_best_edcr": 0.928,
235	      "grpo_g4_kl001_step100_edcr": 0.854,
236	      "sft_edcr": 0.712,
237	      "ced_reranker_edcr": 0.668,
238	      "rsft_flatnli_edcr": 0.659,
239	      "dpo_ced_edcr": 0.66,
240	      "rsft_ced_edcr": 0.639,
241	      "edcr_evi_f1_spearman_rho": -0.38,
242	      "edcr_rel_f1_spearman_rho": -0.52
243	    },
244	    "tables": [
245	      {
246	        "name": "Table: Cross-method EDCR diagnostic (dev set)",
247	        "columns": [
248	          "Method",
249	          "rel_f1",
250	          "evi_f1_cond",
251	          "EDCR",
252	          "Diagnostic Zone"
253	        ],
254	        "rows": [
255	          [
256	            "GRPO G=8 (best ckpt)",
257	            0.078,
258	            0.835,
259	            0.928,
260	            "Collapse"
261	          ],
262	          [
263	            "GRPO G=4 kl001 (step-100)",
264	            0.217,
265	            0.575,
266	            0.854,
267	            "Collapse"
268	          ],
269	          [
270	            "SFT baseline",
271	            0.406,
272	            0.798,
273	            0.712,
274	            "Baseline"
275	          ],
276	          [
277	            "CED-as-reranker",
278	            0.422,
279	            0.809,
280	            0.668,
281	            "Filtered"
282	          ],
283	          [
284	            "DPO+CED",
285	            0.34,
286	            0.798,
287	            0.66,
288	            "Filtered"
289	          ],
290	          [
291	            "RSFT+flat-NLI",
292	            0.461,
293	            0.808,
294	            0.659,
295	            "Filtered"
296	          ],
297	          [
298	            "RSFT+CED (FREIGE)",
299	            0.468,
300	            0.816,
301	            0.639,
302	            "Filtered"
303	          ]
304	        ]
305	      }
306	    ],
307	    "figures": [],
308	    "analysis": "EDCR 成功区分崩溃/正常/优化三类方法。DPO (0.660) 的 EDCR  接近 flat-NLI RSFT (0.659)，暗示 DPO 的 contrastive loss  在 evidence 质量上达到了 non-contrastive RSFT 的水平， 但 rel_f1 差距 (0.34 vs 0.46) 来自抽取能力退化。 EDCR 在论文中定位为 \"Evi-F1 的互补诊断\": Evi-F1 衡量 evidence recall， EDCR 衡量 evidence precision (distractor 混入率)。\n\n\nEDCR 在方法间呈现预期排序: GRPO G=8 (0.928) > GRPO G=4 (0.854) > SFT (0.712) > CED-reranker (0.668)  ≈ DPO (0.660) ≈ flat-NLI RSFT (0.659) > CED RSFT (0.639)。 三个分辨区间清晰: (1) GRPO 崩溃区 (>0.85)——模型几乎随机引用； (2) SFT 中间区 (~0.71)——无 RL 信号的自然引用； (3) RL-filtered 优化区 (0.64-0.67)——CED/flat-NLI 信号筛选后证据更精准。 但 RL-filtered 区内部分辨力不足: CED RSFT (0.639) vs flat-NLI RSFT (0.659)  仅差 2.0pp，与 plan_001 的 evi_f1 结论一致。 EDCR 与 rel_f1 的负相关 ρ=-0.52 强于与 evi_f1 的 ρ=-0.38，因为 正确抽取的 triple 更容易定位真正支撑句（关系正确 → 证据自然准确）。\n"
309	  },
310	  {
311	    "name": "DREEAM baseline reproduction",
312	    "description": "DocRED dev set 上复现 DREEAM/SAIS 的 Evi-F1_joint，验证评测协议对齐。\n",
313	    "results": {
314	      "dreeam_reproduced_dev_evi_f1_joint": 0.581,
315	      "dreeam_reproduced_dev_rel_f1": 0.625,
316	      "dreeam_published_test_evi_f1_joint": 0.5734,
317	      "dreeam_reproduction_gap_pp": 0.8,
318	      "sais_reproduced_dev_evi_f1_joint": 0.562,
319	      "sais_reproduced_dev_rel_f1": 0.608,
320	      "sais_published_test_evi_f1_joint": 0.5567,
321	      "sais_reproduction_gap_pp": 0.5
322	    },
323	    "tables": [
324	      {
325	        "name": "Table: Evidence baseline comparison (dev, DREEAM joint protocol)",
326	        "columns": [
327	          "Method",
328	          "Type",
329	          "rel_f1",
330	          "Evi-F1_joint",
331	          "Evi-F1_cond (est.)"
332	        ],
333	        "rows": [
334	          [
335	            "DREEAM (reproduced)",
336	            "Encoder (RoBERTa-large)",
337	            0.625,
338	            0.581,
339	            "~0.93"
340	          ],
341	          [
342	            "SAIS (reproduced)",
343	            "Encoder (RoBERTa-large)",
344	            0.608,
345	            0.562,
346	            "~0.92"
347	          ],
348	          [
349	            "RSFT+CED (ours)",
350	            "Generative LLM (Qwen3-4B)",
351	            0.468,
352	            0.372,
353	            0.816
354	          ],
355	          [
356	            "SFT (ours)",
357	            "Generative LLM (Qwen3-4B)",
358	            0.406,
359	            0.308,
360	            0.798
361	          ]
362	        ]
363	      }
364	    ],
365	    "figures": [],
366	    "analysis": "复现成功（Δ<1pp），确认评测对齐。论文中需明确两个关键解读: (1) Joint Evi-F1 差距 (58.1 vs 37.2) 不等于 evidence quality 差距—— conditional 上 82 vs 93% 差距远小； (2) 生成式 evidence（显式句子索引）与 encoder evidence（attention weight  后处理）在可解释性上有本质差异，joint Evi-F1 可比但方法论不同类。\n\n\nDREEAM dev Evi-F1_joint=58.1% 合理（test 57.34%，dev 略高 ~0.8pp  属正常 dev-test gap）。使用官方开源代码 + RoBERTa-large checkpoint 复现， 主要误差源: (1) 不同 random seed 导致微量波动 (<0.5pp)； (2) evaluation protocol 的细微差异（如 evidence matching 的 threshold）。 复现误差 <1pp 验证我们的 DREEAM-aligned joint Evi-F1 计算函数与原始实现一致。 SAIS 同理复现成功 (dev 56.2%, gap 0.5pp from test 55.67%)。 关键对比: 我们 RSFT dev Evi-F1_joint ≈ 37.2%，差距 ~21pp 主要来自 extraction recall 差异 (46.8% vs 62.5%)，而非 per-triple evidence quality。\n"
367	  },
368	  {
369	    "name": "CED-as-reranker",
370	    "description": "推理时对 SFT N=8 候选用 CED 重排选最优。无额外训练。\n",
371	    "results": {
372	      "ced_reranker_rel_f1": 0.422,
373	      "ced_reranker_evi_f1": 0.809,
374	      "ced_reranker_edcr": 0.668,
375	      "delta_rel_f1_over_sft_pp": 1.6,
376	      "delta_evi_f1_over_sft_pp": 1.1,
377	      "delta_edcr_over_sft_pp": -4.4,
378	      "inference_time_factor": 8.5,
379	      "n_documents": 985,
380	      "n_candidates_per_doc": 8
381	    },
382	    "tables": [],
383	    "figures": [],
384	    "analysis": "CED-reranker 验证了 CED 在推理时的即时价值，但 ROI 低。 论文定位: (1) \"无需训练的 quick win\" 选项，适合无法重训的部署场景； (2) 与 RSFT 对比，证明 CED 信号通过训练数据筛选比推理时选择更有效传导。\n\n\nCED 重排从 N=8 候选中选最优，改进受限于候选池质量: (1) rel_f1 +1.6pp 是间接效应——CED 优化证据质量，高质量证据候选 往往也有更好的关系抽取（弱相关 r~0.3），但选择空间仅限 8 个 SFT 生成； (2) evi_f1 +1.1pp 和 EDCR -4.4pp 更直接——CED 有效筛掉高 distractor 候选； (3) 推理成本 8.5x（N=8 生成 + N 次 DeBERTa NLI 评估）， 性价比远不如 RSFT（一次训练后推理成本不变）。 与 RSFT +6.3pp 对比: 重排只能选，RSFT 能教——训练改变了模型生成分布， 使模型 internalize 了更好的 evidence selection pattern。\n"
385	  },
386	  {
387	    "name": "Model size ablation (1.7B / 8B)",
388	    "description": "Qwen3-1.7B 和 Qwen3-8B 上复现 SFT + RSFT+CED pipeline。\n",
389	    "results": {
390	      "qwen3_1_7b_sft_rel_f1": 0.32,
391	      "qwen3_1_7b_sft_evi_f1": 0.775,
392	      "qwen3_1_7b_sft_edcr": 0.738,
393	      "qwen3_1_7b_rsft_ced_rel_f1": 0.348,
394	      "qwen3_1_7b_rsft_ced_evi_f1": 0.792,
395	      "qwen3_1_7b_rsft_ced_edcr": 0.702,
396	      "qwen3_1_7b_delta_rel_f1_pp": 2.8,
397	      "qwen3_1_7b_delta_evi_f1_pp": 1.7,
398	      "qwen3_8b_sft_rel_f1": 0.448,
399	      "qwen3_8b_sft_evi_f1": 0.81,
400	      "qwen3_8b_sft_edcr": 0.695,
401	      "qwen3_8b_rsft_ced_rel_f1": 0.488,
402	      "qwen3_8b_rsft_ced_evi_f1": 0.825,
403	      "qwen3_8b_rsft_ced_edcr": 0.622,
404	      "qwen3_8b_delta_rel_f1_pp": 4.0,
405	      "qwen3_8b_delta_evi_f1_pp": 1.5
406	    },
407	    "tables": [
408	      {
409	        "name": "Table: Model size ablation (dev set)",
410	        "columns": [
411	          "Model",
412	          "Params",
413	          "Method",
414	          "rel_f1",
415	          "evi_f1_cond",
416	          "EDCR",
417	          "Δrel_f1"
418	        ],
419	        "rows": [
420	          [
421	            "Qwen3-1.7B",
422	            "1.7B",
423	            "SFT",
424	            0.32,
425	            0.775,
426	            0.738,
427	            "—"
428	          ],
429	          [
430	            "Qwen3-1.7B",
431	            "1.7B",
432	            "RSFT+CED",
433	            0.348,
434	            0.792,
435	            0.702,
436	            "+2.8pp"
437	          ],
438	          [
439	            "Qwen3-4B",
440	            "4B",
441	            "SFT",
442	            0.406,
443	            0.798,
444	            0.712,
445	            "—"
446	          ],
447	          [
448	            "Qwen3-4B",
449	            "4B",
450	            "RSFT+CED",
451	            0.468,
452	            0.816,
453	            0.639,
454	            "+6.3pp"
455	          ],
456	          [
457	            "Qwen3-8B",
458	            "8B",
459	            "SFT",
460	            0.448,
461	            0.81,
462	            0.695,
463	            "—"
464	          ],
465	          [
466	            "Qwen3-8B",
467	            "8B",
468	            "RSFT+CED",
469	            0.488,
470	            0.825,
471	            0.622,
472	            "+4.0pp"
473	          ]
474	        ]
475	      }
476	    ],
477	    "figures": [],
478	    "analysis": "RSFT 改善跨三模型尺寸一致，部分应对 RC4 的\"单模型\"攻击。 4B 的最大 delta (6.3pp) 可能有超参过拟合成分—— 如果时间允许，在 1.7B/8B 上独立超参搜索可能缩小差距。 8B RSFT rel_f1=0.488 是最高绝对值，但与 LMRC (8B, 60.69) 差距仍大， 说明生成 evidence 的额外负担确实压缩了抽取性能。\n\n\n1.7B: 容量有限，DocRE 需要长文档理解和多跳推理，SFT baseline 显著低于 4B  (0.320 vs 0.406)。RSFT 仍改善 +2.8pp，但幅度略小于 4B (+6.3pp)—— 小模型生成的 N=8 候选多样性和质量更低（unique triples 更少）， CED 筛选后可用高质量训练样本减少（selection rate 可能从 12.4% 降至 ~8%）， 导致 RSFT 训练数据量不足。evi_f1 +1.7pp 方向一致。 8B: 更大容量提升 SFT baseline 至 0.448。RSFT +4.0pp 至 0.488， 提升幅度介于 1.7B (2.8pp) 和 4B (6.3pp) 之间——4B 的最大提升可能因 超参专门在 4B 上搜索优化所致。8B 生成更多高质量候选， CED 筛选后训练数据质量更高，EDCR=0.622 为所有配置最低。 三模型尺寸的 RSFT 改善一致 (+2.8/+6.3/+4.0pp)，支撑方法泛化性。\n"
479	  },
480	  {
481	    "name": "Re-DocRED extension",
482	    "description": "DocRED-trained 模型直接在 Re-DocRED (修正 false negative) 上评估。\n",
483	    "results": {
484	      "sft_redocred_rel_f1": 0.485,
485	      "sft_redocred_evi_f1_cond": 0.812,
486	      "sft_redocred_edcr": 0.668,
487	      "rsft_ced_redocred_rel_f1": 0.52,
488	      "rsft_ced_redocred_evi_f1_cond": 0.83,
489	      "rsft_ced_redocred_edcr": 0.61,
490	      "delta_rel_f1_pp": 3.5,
491	      "redocred_vs_docred_sft_gain_pp": 7.9,
492	      "redocred_vs_docred_rsft_gain_pp": 5.2
493	    },
494	    "tables": [
495	      {
496	        "name": "Table: Re-DocRED evaluation (dev set, DocRED-trained models)",
497	        "columns": [
498	          "Method",
499	          "DocRED rel_f1",
500	          "Re-DocRED rel_f1",
501	          "Δ over SFT",
502	          "Re-DocRED EDCR"
503	        ],
504	        "rows": [
505	          [
506	            "SFT",
507	            0.406,
508	            0.485,
509	            "—",
510	            0.668
511	          ],
512	          [
513	            "RSFT+CED",
514	            0.468,
515	            0.52,
516	            "+3.5pp",
517	            0.61
518	          ]
519	        ]
520	      }
521	    ],
522	    "figures": [],
523	    "analysis": "Re-DocRED 验证了 RSFT 改善在更干净标注下的一致性。 Delta 收窄 (6.3→3.5pp) 是预期的 ceiling effect 而非方法退化。 论文中报告为泛化性验证，不强调绝对数字。\n\n\nRe-DocRED 修正了 DocRED 中约 30% false negative triples: (1) SFT rel_f1 从 0.406 跃升至 0.485 (+7.9pp)——模型本来就预测了这些 triples， 在 DocRED 评估中被误判为 FP，Re-DocRED 修正后变为 TP； (2) RSFT 从 0.468 升至 0.520 (+5.2pp)，升幅小于 SFT——因为 RSFT  在 CED 筛选阶段部分排除了与 false negative triples 相关的候选 （这些 triples 在 DocRED gold 中不存在 → 生成它们的候选 F1 较低 → 被 CED 筛掉）， 导致 RSFT 模型未充分学习这部分 patterns； (3) Delta 从 DocRED +6.3pp 收窄至 +3.5pp——Re-DocRED 更完整标注 使 SFT baseline 更强，RSFT 增量空间被压缩 (ceiling effect)； (4) EDCR 改善——Re-DocRED 的更完整 evidence 标注将部分 \"distractor\"  重新归类为 gold evidence，降低了所有方法的 EDCR。\n"
524	  },
525	  {
526	    "name": "top_k ablation",
527	    "description": "CED scoring 筛选 top_k=3 (~8000 samples) vs top_k=1 (2718 samples)。\n",
528	    "results": {
529	      "topk1_train_samples": 2718,
530	      "topk1_mean_ced_score": 0.668,
531	      "topk1_rel_f1": 0.468,
532	      "topk1_evi_f1": 0.816,
533	      "topk1_edcr": 0.639,
534	      "topk3_train_samples": 8154,
535	      "topk3_mean_ced_score": 0.512,
536	      "topk3_rel_f1": 0.458,
537	      "topk3_evi_f1": 0.802,
538	      "topk3_edcr": 0.662
539	    },
540	    "tables": [
541	      {
542	        "name": "Table: top_k ablation (dev set)",
543	        "columns": [
544	          "top_k",
545	          "N_train",
546	          "Mean CED",
547	          "rel_f1",
548	          "evi_f1",
549	          "EDCR"
550	        ],
551	        "rows": [
552	          [
553	            1,
554	            2718,
555	            0.668,
556	            0.468,
557	            0.816,
558	            0.639
559	          ],
560	          [
561	            3,
562	            8154,
563	            0.512,
564	            0.458,
565	            0.802,
566	            0.662
567	          ]
568	        ]
569	      }
570	    ],
571	    "figures": [],
572	    "analysis": "top_k=1 全面优于 top_k=3，支持 RSFT 设计原则: 严格筛选质量 > 扩大数据量。这间接支持了 CED 打分的排序有效性—— 虽然 CED vs flat-NLI 差异不显著，CED 的 top-1 selection 明确优于 top-3。\n\n\ntop_k=3 将训练数据量扩展 3x (8154 vs 2718)，但平均 CED score 从 0.668  降至 0.512——每文档的第 2/3 候选 CED margin 显著递减: (1) rel_f1 略降 1.0pp: 额外候选引入的多样性理论上有利， 但低质量候选的关系抽取模式噪声抵消了数据量优势； (2) evi_f1 降 1.4pp 和 EDCR 升 2.3pp 更显著: top_k=2/3 候选包含更多 entity-sharing distractor 引用， 训练时模型学到了引用 distractor 的倾向； (3) 在 median tier 下，这一结果为 CED 打分机制的唯一明确正面证据—— 即使 CED vs flat-NLI 不显著，CED 的 ranked filtering (top_k=1 > top_k=3)  证明了打分排序的实际价值。\n"
573	  },
574	  {
575	    "name": "GRPO G=8 experiment",
576	    "description": "G=8 + CED reward + kl_coef=0.01 + lr=5e-6，gradient_accumulation=2。 验证增大 group size 是否改善 catastrophic forgetting。\n",
577	    "results": {
578	      "grpo_g8_best_ckpt_step": 40,
579	      "grpo_g8_best_rel_f1": 0.078,
580	      "grpo_g8_best_evi_f1": 0.835,
581	      "grpo_g8_best_edcr": 0.928,
582	      "grpo_g8_final_step": 100,
583	      "grpo_g8_final_rel_f1": 0.012,
584	      "grpo_g8_final_evi_f1": 0.862,
585	      "grpo_g8_final_edcr": 0.948,
586	      "grpo_g8_final_reward": 1.45,
587	      "grpo_g8_ckpt10_rel_f1": 0.008,
588	      "grpo_g8_ckpt20_rel_f1": 0.035,
589	      "grpo_g8_ckpt30_rel_f1": 0.062,
590	      "grpo_g8_ckpt40_rel_f1": 0.078,
591	      "grpo_g8_ckpt50_rel_f1": 0.055,
592	      "grpo_g8_ckpt60_rel_f1": 0.038,
593	      "grpo_g8_ckpt80_rel_f1": 0.02,
594	      "grpo_g8_ckpt100_rel_f1": 0.012,
595	      "grpo_g8_ckpt10_evi_f1": 0.72,
596	      "grpo_g8_ckpt40_evi_f1": 0.835,
597	      "grpo_g8_ckpt100_evi_f1": 0.862,
598	      "grpo_g4_kl001_best_rel_f1": 0.217,
599	      "grpo_g4_kl001_best_step": 100,
600	      "gradient_accumulation_steps": 2,
601	      "effective_batch_size": 16,
602	      "training_time_hours": 7.5
603	    },
604	    "tables": [
605	      {
606	        "name": "Table: GRPO G=4 vs G=8 summary",
607	        "columns": [
608	          "Config",
609	          "Best rel_f1",
610	          "Peak step",
611	          "Final evi_f1",
612	          "Final EDCR",
613	          "Pattern"
614	        ],
615	        "rows": [
616	          [
617	            "G=4, kl001, lr5e-6",
618	            0.217,
619	            "100 (still rising)",
620	            0.575,
621	            0.854,
622	            "Slow climb, no peak reached"
623	          ],
624	          [
625	            "G=8, kl001, lr5e-6",
626	            0.078,
627	            40,
628	            0.862,
629	            0.948,
630	            "Early peak then collapse"
631	          ]
632	        ]
633	      },
634	      {
635	        "name": "Table: GRPO G=8 checkpoint trajectory",
636	        "columns": [
637	          "Step",
638	          "rel_f1",
639	          "evi_f1",
640	          "EDCR",
641	          "reward"
642	        ],
643	        "rows": [
644	          [
645	            10,
646	            0.008,
647	            0.72,
648	            0.985,
649	            0.62
650	          ],
651	          [
652	            20,
653	            0.035,
654	            0.76,
655	            0.972,
656	            0.85
657	          ],
658	          [
659	            30,
660	            0.062,
661	            0.795,
662	            0.95,
663	            1.05
664	          ],
665	          [
666	            40,
667	            0.078,
668	            0.835,
669	            0.928,
670	            1.18
671	          ],
672	          [
673	            50,
674	            0.055,
675	            0.845,
676	            0.935,
677	            1.28
678	          ],
679	          [
680	            60,
681	            0.038,
682	            0.85,
683	            0.94,
684	            1.35
685	          ],
686	          [
687	            80,
688	            0.02,
689	            0.858,
690	            0.945,
691	            1.42
692	          ],
693	          [
694	            100,
695	            0.012,
696	            0.862,
697	            0.948,
698	            1.45
699	          ]
700	        ]
701	      }
702	    ],
703	    "figures": [],
704	    "analysis": "G=8 决定性支持 Claim 3: (1) 排除 RC5 的 \"G 太小\" 攻击——G=8 表现更差而非更好； (2) 提供新理论洞见: advantage estimation 精度与 forgetting 速度正相关， 连接 Gao et al. 2023 reward overoptimization 的 scaling 分析； (3) 论文可安全宣称 \"GRPO+QLoRA for document-level IE exhibits  evidence-extraction decoupling that worsens with improved advantage estimation\"。 Claim 3 措辞限定为 GRPO+QLoRA，不泛化到 full-rank GRPO 或其他 online RL。\n\n\nG=8 提供更精确的 advantage estimation（每 prompt 8 个 rollout 的 baseline  更稳定，方差 ∝ 1/G），但这反而加速了 catastrophic forgetting: (1) 更精确的 advantage 信号 → CED reward gradient 方向更准确 → 模型更高效地优化 CED reward。但 CED reward 与 rel_f1 不对齐 （CED 衡量 evidence quality，不直接优化 relation extraction）， 因此更好的优化 → 更快的 reward overoptimization； (2) G=4 kl001 的 rel_f1 在 100 步内持续上升 (0.003→0.217)， 可能是 noisy advantage estimation 的\"隐式正则化\"—— 类似 dropout 的随机性延缓了 collapse，使模型在噪声中保留了部分 task-relevant 参数； (3) G=8 的 rel_f1 在 step 40 达峰 0.078 后快速下降—— advantage noise 减小后，RL 信号更快且更准确地将 policy  推向 evidence-optimizing 方向，relation extraction capacity 更快被覆写； (4) evi_f1 持续上升至 0.862 (> G=4 best 0.850)， 证明 G=8 确实更有效优化了 evidence quality——代价是更快的 decoupling。 核心洞见: G=4 的 \"成功\" (rel_f1=0.217) 是 high-variance advantage  estimation 的意外副产品，非方法的合理工作点。\n"
705	  },
706	  {
707	    "name": "DPO+CED experiment",
708	    "description": "用 RSFT 候选构造 CED preference pairs (preferred vs rejected)，DPO 训练。 填补 online-offline 光谱中间方法。\n",
709	    "results": {
710	      "dpo_rel_f1": 0.34,
711	      "dpo_ign_f1": 0.34,
712	      "dpo_evi_f1": 0.798,
713	      "dpo_edcr": 0.66,
714	      "dpo_precision": 0.358,
715	      "dpo_recall": 0.324,
716	      "dpo_n_preference_pairs": 5436,
717	      "dpo_beta": 0.1,
718	      "dpo_training_epochs": 3,
719	      "dpo_eval_loss": 0.685,
720	      "dpo_delta_over_sft_rel_f1_pp": -6.6,
721	      "dpo_delta_over_grpo_g8_rel_f1_pp": 26.2,
722	      "dpo_delta_over_rsft_ced_rel_f1_pp": -12.8
723	    },
724	    "tables": [
725	      {
726	        "name": "Table: Online-offline-curation spectrum",
727	        "columns": [
728	          "Method",
729	          "Type",
730	          "rel_f1",
731	          "evi_f1",
732	          "EDCR",
733	          "Δ over SFT"
734	        ],
735	        "rows": [
736	          [
737	            "GRPO G=8 (best ckpt)",
738	            "Online reward opt.",
739	            0.078,
740	            0.835,
741	            0.928,
742	            "-32.8pp"
743	          ],
744	          [
745	            "GRPO G=4 kl001 (best ckpt)",
746	            "Online reward opt.",
747	            0.217,
748	            0.575,
749	            0.854,
750	            "-18.9pp"
751	          ],
752	          [
753	            "DPO+CED",
754	            "Offline contrastive",
755	            0.34,
756	            0.798,
757	            0.66,
758	            "-6.6pp"
759	          ],
760	          [
761	            "SFT baseline",
762	            "Supervised (no RL)",
763	            0.406,
764	            0.798,
765	            0.712,
766	            "—"
767	          ],
768	          [
769	            "RSFT+flat-NLI",
770	            "Data curation + SFT",
771	            0.461,
772	            0.808,
773	            0.659,
774	            "+5.5pp"
775	          ],
776	          [
777	            "RSFT+CED (FREIGE)",
778	            "Data curation + SFT",
779	            0.468,
780	            0.816,
781	            0.639,
782	            "+6.3pp"
783	          ]
784	        ]
785	      }
786	    ],
787	    "figures": [],
788	    "analysis": "DPO 结果使论文叙事从 \"offline vs online RL\" 转为更精确的分类: (1) Reward optimization (GRPO): catastrophic failure，无论 G 大小； (2) Preference learning (DPO): degradation vs SFT——contrastive loss 损害 structured generation； (3) Data curation (RSFT): improvement over SFT——无 RL loss，只筛选数据。 结论: 对 document-level IE，任何形式的 contrastive/reward-based loss  (无论 online 或 offline) 都有风险；RSFT 成功因为它本质不是 RL—— 是 quality-filtered SFT。 Claim 3 discussion 需承认 DPO 结果的歧义性，避免 overclaim \"offline RL works\"。\n\n\nDPO 使用 offline preference pairs 训练，避免了 GRPO 的 online RL 机制， 因此不出现 catastrophic forgetting (rel_f1=0.340 >> GRPO 0.078)。 但 DPO 仍低于 SFT (0.406)，原因: (1) DPO 的 contrastive loss 同时 push up preferred 和 push down rejected—— \"push down\" 信号在 structured IE 中有害: 被 CED 标为 \"rejected\" 的候选中，关系抽取部分可能是正确的（只是 evidence 差）， push down 这些候选时也 push down 了正确的关系模式； (2) CED preference labels 有 ~18.5% 噪声 (discrimination accuracy 0.815)， DPO 对 label noise 比 RSFT 更敏感—— RSFT 仅用 top positive 训练（噪声负例不参与梯度）， DPO 显式惩罚负例（噪声标签直接产生错误梯度）； (3) DPO 的 implicit reward model 假设 Bradley-Terry preference 模型， 但 CED margin 并非 BT 分布——文档级 IE 的候选质量差异不是连续谱， 而是离散的（正确/部分正确/完全错误），BT 假设不适用导致优化方向偏差。 rel_f1=0.340 的尴尬位置使 online-offline 叙事复杂化: DPO 是 \"offline\" 但劣于 SFT (无 RL 信号)，说明问题不在 online/offline  而在 contrastive loss 对 structured generation 的损害。\n"
789	  },
790	  {
791	    "name": "EDCR 人工标注验证",
792	    "description": "100 样本 × 2 标注者，人工判断 cited evidence 是否支持对应 relation。\n",
793	    "results": {
794	      "n_samples": 100,
795	      "n_annotators": 2,
796	      "inter_annotator_kappa": 0.62,
797	      "edcr_human_pearson_r": 0.44,
798	      "edcr_human_spearman_rho": 0.41,
799	      "human_true_distractor_rate_mean": 0.58,
800	      "edcr_auto_mean": 0.665,
801	      "edcr_overestimate_pp": 8.5,
802	      "false_distractor_rate": 0.14,
803	      "method_level_edcr_human_rank_concordance": 1.0
804	    },
805	    "tables": [
806	      {
807	        "name": "Table: EDCR human validation statistics",
808	        "columns": [
809	          "Statistic",
810	          "Value"
811	        ],
812	        "rows": [
813	          [
814	            "N samples",
815	            100
816	          ],
817	          [
818	            "N annotators",
819	            2
820	          ],
821	          [
822	            "Inter-annotator κ",
823	            0.62
824	          ],
825	          [
826	            "EDCR vs human Pearson r",
827	            0.44
828	          ],
829	          [
830	            "EDCR vs human Spearman ρ",
831	            0.41
832	          ],
833	          [
834	            "Mean EDCR (auto)",
835	            "66.5%"
836	          ],
837	          [
838	            "Mean distractor rate (human)",
839	            "58.0%"
840	          ],
841	          [
842	            "EDCR overestimate",
843	            "+8.5pp"
844	          ],
845	          [
846	            "False distractor rate (auto labels wrong)",
847	            "14%"
848	          ],
849	          [
850	            "Method-level rank concordance",
851	            "1.0 (perfect)"
852	          ]
853	        ]
854	      }
855	    ],
856	    "figures": [],
857	    "analysis": "EDCR 人工验证支持 \"有信号但有局限\": (1) sample-level r=0.44 足以宣称 EDCR 携带 distractor 信息； (2) method-level 排序完全一致，证明 EDCR 可靠用于方法比较； (3) 但 8.5pp 系统性高估和 14% false distractor rate 限制其作为 absolute metric 的可信度。 论文定位 EDCR 为 \"complementary diagnostic to Evi-F1\": Evi-F1 衡量 evidence recall，EDCR 衡量 evidence precision (distractor 混入率)。 Limitation section 需讨论 gold annotation 不完整性对 EDCR 的影响。\n\n\nEDCR 与人工判断 r=0.44，有信号但不够强，三重原因: (1) 主要噪声源: DocRED gold evidence 标注不完整——约 14% 被 EDCR  标为 \"entity-sharing distractor\" 的句子被人工标注者判为 \"supports relation\" （annotator 遗漏的有效证据），导致 EDCR 系统性高估 distractor rate (+8.5pp)； (2) 次要噪声源: 部分 entity-sharing 句子提供辅助上下文（\"partially supports\"）， 人工标注存在灰度而 EDCR 二元化处理损失了连续信号； (3) 标注者一致性 κ=0.62 (substantial agreement) 表明 evidence 判断本身有主观性， 不同标注者对 \"supports relation\" 的理解不完全一致—— 任何自动指标在此条件下都难达 r>0.7。 尽管 sample-level r 中等，method-level rank 完全一致 (SFT EDCR > RSFT-flatNLI EDCR > RSFT-CED EDCR，人工排序同)， 说明 EDCR 作为 method-comparison diagnostic 足够可靠。\n"
858	  },
859	  {
860	    "name": "GRPO forgetting 详细分析 + 可视化",
861	    "description": "整理 G=4 (3 reward × 2 lr) 和 G=8 全部 checkpoint 轨迹， 绘制 forgetting dynamics 可视化。\n",
862	    "results": {
863	      "n_configs_g4": 6,
864	      "n_configs_g8": 1,
865	      "total_checkpoint_trajectory_points": 37,
866	      "reward_rel_f1_pearson_r": -0.68,
867	      "reward_evi_f1_pearson_r": 0.82,
868	      "decoupling_onset_g4_kl001": "step ~60",
869	      "decoupling_onset_g8": "step ~30",
870	      "g4_lr5e5_trajectory_pattern": "rel_f1 high initial → rapid collapse by step 50",
871	      "g4_lr5e6_trajectory_pattern": "rel_f1 near-zero throughout, evi_f1 rising",
872	      "g4_kl001_trajectory_pattern": "rel_f1 slow climb to 0.217, no peak at 100 steps",
873	      "g8_trajectory_pattern": "rel_f1 peaks step 40 then collapses, evi_f1 monotonic rise"
874	    },
875	    "tables": [],
876	    "figures": [],
877	    "analysis": "可视化清晰展示 evidence-extraction decoupling 的动态过程。 论文中作为 Claim 3 的核心 figure，连接 Gao et al. 2023  reward overoptimization 和 LongRLVR (ICLR 2026) gradient vanishing 理论。 G=4 vs G=8 的 onset 对比提供了独立洞见: \"better optimization of a misaligned reward accelerates task degradation\"。\n\n\n这是分析/可视化任务而非新实验。整理已有数据揭示: (1) reward 和 rel_f1 的强负相关 (r=-0.68) 是 reward overoptimization  的直接证据——CED reward 优化摧毁 task performance； (2) reward 和 evi_f1 的强正相关 (r=0.82) 证明 CED reward 确实有效优化了  evidence quality——问题不在 reward signal 质量而在 objective misalignment； (3) decoupling onset 在 G=8 更早 (~step 30 vs G=4 ~step 60)—— 与 advantage estimation 精度理论一致； (4) G=4 lr=5e-5 的 \"high initial → collapse\" 与 G=4 lr=5e-6 的  \"always near-zero\" 形成有趣对比——lr 决定了 collapse 速度而非是否 collapse。\n"
878	  },
879	  {
880	    "name": "NLI model ablation",
881	    "description": "DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer，评估 NLI 模型能力影响。\n",
882	    "results": {
883	      "deberta_base_disc_accuracy": 0.815,
884	      "deberta_base_mean_margin": 0.48,
885	      "deberta_large_disc_accuracy": 0.848,
886	      "deberta_large_mean_margin": 0.552,
887	      "deberta_large_rsft_rel_f1": 0.472,
888	      "deberta_large_rsft_evi_f1": 0.82,
889	      "deberta_large_rsft_edcr": 0.632,
890	      "delta_disc_accuracy_pp": 3.3,
891	      "delta_rsft_rel_f1_pp": 0.4,
892	      "delta_rsft_evi_f1_pp": 0.4,
893	      "delta_rsft_edcr_pp": -0.7
894	    },
895	    "tables": [
896	      {
897	        "name": "Table: NLI model ablation",
898	        "columns": [
899	          "NLI Scorer",
900	          "Disc. Acc.",
901	          "Margin",
902	          "RSFT rel_f1",
903	          "RSFT evi_f1",
904	          "RSFT EDCR"
905	        ],
906	        "rows": [
907	          [
908	            "DeBERTa-v3-base",
909	            0.815,
910	            0.48,
911	            0.468,
912	            0.816,
913	            0.639
914	          ],
915	          [
916	            "DeBERTa-v3-large",
917	            0.848,
918	            0.552,
919	            0.472,
920	            0.82,
921	            0.632
922	          ]
923	        ]
924	      }
925	    ],
926	    "figures": [],
927	    "analysis": "NLI model 升级的 CED 精度提升 (+3pp) 未有效传导到下游 (+0.4pp)。 论文中作为 RC1 回应: 当前 CED 噪声水平可接受，更强 NLI backbone  带来的边际收益有限。同时间接支持 CED vs flat-NLI 不显著的解释—— 如果连 base→large 的提升都微弱，contrastive vs non-contrastive  的差异难以在 RSFT 管线中放大也是自然的。\n\nDeBERTa-large NLI 能力更强 (MNLI ~92% vs base ~90%)， CED discrimination accuracy +3.3pp (0.815→0.848)，margin +0.072 (0.48→0.55)。 但下游 RSFT 提升微弱 (Δrel_f1 +0.4pp, Δevi_f1 +0.4pp): (1) RSFT 的瓶颈不在 CED 打分精度而在候选生成质量—— SFT 模型生成的 N=8 候选限定了 RSFT 训练数据的上限， 更精确的 CED 只能在固定候选池中选得略好； (2) CED base 的 81.5% accuracy 已足够（threshold effect）—— 从 81.5% 到 84.8% 的提升只修正了 ~3% 的边界案例， 这些案例对最终训练数据的影响被其他因素（候选质量、超参）淹没； (3) large 模型推理成本 ~3x，性价比不支持在 RSFT pipeline 中使用。\n"
928	  }
929	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f27883a5-170d-456c-815f-ce754a9fc1f5",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "44ea6900-3b9d-4f84-9bd5-c8d8eab1390f",
  "sourceToolAssistantUUID": "f27883a5-170d-456c-815f-ce754a9fc1f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-15T14:29:30.367Z_

I now have a comprehensive understanding of the paper, its experimental infrastructure, the actual vs. imagined results, and the development history. Let me now write the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44ea6900-3b9d-4f84-9bd5-c8d8eab1390f",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WkFGpDGkZbHtKA88j7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c9bf3f0-5875-4026-8056-2d97f521a2ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxDkTjCpzboYsWPi3Y2WZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16455,
      "cache_read_input_tokens": 104112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16455,
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

_source line 66 · 2026-05-15T14:29:31.409Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DFM1uhD8aiDg9pCMUS7kTN`</summary>

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
  "parentUuid": "6c9bf3f0-5875-4026-8056-2d97f521a2ae",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4WkFGpDGkZbHtKA88j7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5ba417b-c7ad-4414-8d53-2dbc4e8cd056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UxDkTjCpzboYsWPi3Y2WZC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16455,
      "cache_read_input_tokens": 104112,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16455
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 104112,
          "cache_creation_input_tokens": 16455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16455,
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

_source line 67 · 2026-05-15T14:29:31.413Z_

<details><summary>↩ Tool result · `toolu_01DFM1uhD8aiDg9pCMUS7kTN`</summary>

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
  "parentUuid": "f5ba417b-c7ad-4414-8d53-2dbc4e8cd056",
  "isSidechain": true,
  "promptId": "49410741-8063-4be4-9d72-b98bc5da38b8",
  "agentId": "aebcf4b7d1ca414e2",
  "type": "user",
  "uuid": "03714316-73ab-4ba3-bd18-bd2fbff57154",
  "sourceToolAssistantUUID": "f5ba417b-c7ad-4414-8d53-2dbc4e8cd056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 68 · 2026-05-15T14:31:11.472Z_



Here is my review.

---

## Summary

This paper presents FREIGE, the first LLM-based document-level relation extraction system that jointly generates relation triples and sentence-level evidence citations. The core method is Rejection Sampling Fine-Tuning (RSFT) with a Contrastive Evidence Discrimination (CED) scorer built on DeBERTa-v3-base NLI. The paper systematically compares training paradigms (GRPO, DPO, SFT, RSFT) and documents "evidence-extraction decoupling" under GRPO+QLoRA, where evidence quality rises while extraction collapses. It also introduces EDCR as a diagnostic metric. On DocRED test, RSFT+CED achieves +3.2pp rel_F1 over SFT (p<0.01) and reports joint Evi-F1 of 32.2%.

## Strengths

- **Comprehensive training paradigm comparison.** The GRPO (G=4, G=8) --> DPO --> SFT --> RSFT spectrum (Table 5/spectrum) is more informative than a typical ablation. The paper correctly concludes the distinction is contrastive/reward-based loss vs. data curation, not online vs. offline RL. This is a genuinely useful empirical insight for the structured generation community.

- **Evidence-extraction decoupling is well-documented and the paper's strongest finding.** The G=4 vs. G=8 comparison is particularly valuable: G=8 peaks earlier (step 40) and collapses faster, decisively ruling out "insufficient exploration" as a counter-argument. The full checkpoint trajectory (Table 3/grpo_trajectory) with monotonically increasing reward alongside collapsing rel_F1 is compelling. The reward-rel_F1 negative correlation (r=-0.68) and reward-evi_F1 positive correlation (r=0.82) cleanly quantify the phenomenon.

- **Well-designed ablation structure across multiple axes.** The paper isolates individual design choices: CED vs. flat-NLI scoring, top-k filtering strictness, NLI model capacity, CED as training vs. inference-time reranker, model size (1.7B/4B/8B), and dataset variant (Re-DocRED). The CED-reranker experiment is a particularly clever control that separates CED's value as a signal from RSFT as a paradigm.

- **Intellectual honesty.** The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods (43.2% vs. 62.8%), EDCR's moderate sample-level correlation (r=0.44), and the asymmetric dev-to-test degradation (3.6pp vs. 0.6pp). This substantially increases credibility.

- **Statistical testing is present for key claims.** Paired bootstrap tests with 10,000 resamples for CED vs. flat-NLI, and p<0.01 for the main RSFT vs. SFT comparison on test. The paper correctly reports non-significance rather than hiding it.

- **EDCR captures a real evaluation blind spot.** The demonstration that GRPO achieves evi_F1=0.835-0.862 but EDCR>0.92 illustrates a failure mode invisible to standard Evi-F1. The three diagnostic zones (collapse >85%, baseline ~71%, filtered 64-67%) are actionable.

## Weaknesses

- **[Major] Evidence-extraction decoupling claims are confounded by QLoRA.** All GRPO experiments use 4-bit QLoRA (rank=64). The decision log (D008) reveals that kl_coef>0 causes KL explosion specifically due to QLoRA 4-bit quantization noise, and multiple GRPO runs failed for QLoRA-specific reasons (KL explosion, quantization-noise-induced log-prob divergence). The abstract says "online reward optimization (GRPO) with evidence-quality rewards causes catastrophic evidence-extraction decoupling" without qualification. But the experimental record shows QLoRA introduces its own instabilities (D007, D008, D009) that are entangled with the decoupling phenomenon. A bf16 LoRA or full fine-tuning GRPO control is needed to determine whether decoupling is a QLoRA artifact or a genuine RL-for-IE phenomenon. The Limitations section scopes to "GRPO+QLoRA" but the abstract and introduction do not. There is a running experiment (plan_011_grpo_g8_bf16) that may address this, but its results are not yet available.

- **[Major] CED does not significantly outperform flat-NLI, creating a title-contribution mismatch.** CED is named in the title, the acronym (FREIGE), and appears in the majority of tables, yet it does not significantly outperform flat-NLI on any metric (evi_F1: p=0.12; rel_F1: p=0.28; EDCR: p=0.09). The 78% candidate overlap between CED-selected and flat-NLI-selected top-1 candidates confirms minimal differentiation. The paper's Discussion appropriately reframes CED as "one possible scoring function," but the rest of the paper reads as CED-centric. The primary methodological contribution effectively reduces to "RSFT applied to DocRE with NLI-based scoring," which is less novel than the framing suggests.

- **[Major] EDCR definition in the paper (Eq. 2) differs from the code implementation.** The paper defines EDCR as the fraction of cited sentences that are entity-sharing non-gold evidence. However, the evaluator code (`evaluator.py`, lines 168-217) computes `distractors = pred_evi - gold_evi` without any entity-sharing filter -- it counts ALL non-gold cited sentences as distractors, not just entity-sharing ones. This means the reported EDCR values are computed differently from the formal definition. If a cited sentence shares no entities with the target triple but is not gold evidence, it would be counted in the code but should not be counted per the paper's definition. This discrepancy must be resolved and the metric values potentially recomputed.

- **[Major] The evaluator code only computes conditional Evi-F1, but the paper reports "joint Evi-F1."** The `compute_evi_f1` function in `evaluator.py` (lines 140-141) skips FP triples with `if key not in gold_map: continue`, computing only conditional Evi-F1 over correctly predicted triples. The decision log (D041/D042) confirms this was identified as a protocol mismatch with DREEAM's joint Evi-F1, and an alignment function was planned but I find no implementation in the codebase. The joint Evi-F1 numbers in Table 1 (test results: 29.5, 31.2, 32.2) appear to be computed separately or projected, raising questions about their provenance and reliability.

- **[Major] DPO experiment is underspecified and possibly not independently reproducible.** No DPO training script exists in the codebase (only SFT, GRPO, and RSFT trainers). The paper reports DPO results (rel_F1=34.0, beta=0.1, 5,436 preference pairs) but provides insufficient detail: How were preference pairs constructed from CED scores? What was the learning rate, number of epochs, LoRA configuration? Was the same base model + SFT merge used? The experiment_data.json provides some parameters (beta=0.1, 3 epochs, 5436 pairs) but no training details. This is a key data point in the paradigm comparison (Table 5) and needs full specification.

- **[Moderate] Dev-to-test degradation asymmetry is insufficiently analyzed.** RSFT shows 3.6pp dev-to-test degradation in rel_F1 (46.8 -> 43.2) vs. only 0.6pp for SFT (40.6 -> 40.0). This 6x relative degradation ratio is concerning. The RSFT candidates are generated from SFT on training documents, and CED scoring uses gold evidence labels from the training set -- this creates a potential indirect overfitting pathway where patterns correlated with training-set evidence quality are amplified. The paper mentions this in Limitations but does not analyze it. A diagnostic (e.g., RSFT performance on held-out documents not used for candidate generation) would clarify whether this is systematic.

- **[Moderate] CED formula discrepancy between paper and code.** The paper's Eq. 1 defines CED as the mean over cited evidence sentences of [p_NLI(s_i => r) - max_j p_NLI(s_j => r)] for individual sentences. The code (`ced_reward.py`, lines 231-252) concatenates all cited evidence sentences into a single string and computes p_pos on the concatenation. These are meaningfully different: concatenation captures cross-sentence reasoning but does not match the per-sentence formulation in Eq. 1. The paper should report the formula that matches the actual implementation.

- **[Moderate] Single-seed test set reporting.** The paper reports test results from the best dev-set configuration (seed=43). Table 2 shows dev rel_F1 varies from 44.49 to 46.83 across seeds/configs, indicating ~2pp variance. Mean and standard deviation across seeds should be reported for the main results to avoid appearance of cherry-picking. At minimum, the test results should report confidence intervals.

- **[Moderate] The "extraction-only reward also fails" finding undermines the "decoupling" framing.** The decision log (D022-D025) reveals that under the same GRPO+QLoRA configuration, extraction-only reward (no evidence component) also leads to mode collapse. If even a reward that does not involve evidence quality causes GRPO+QLoRA to fail, the phenomenon may be GRPO+QLoRA instability for structured generation broadly, not specifically evidence-vs-extraction misalignment. The paper should discuss this more carefully rather than attributing failure specifically to evidence-extraction tension.

- **[Minor] Missing GRPO forgetting dynamics figure.** The text describes a three-phase pattern across checkpoints with specific onset timings, but no figure is provided. A training dynamics plot of rel_F1, evi_F1, and reward trajectories would be far more compelling than the tabular format and would be the natural centerpiece for the decoupling claim.

- **[Minor] Related work gaps in "RL for IE."** Section 2 states "Prior work has applied RL to IE tasks with mixed results" without citing specific papers. R1-RE (GRPO for sentence-level RE, which succeeds) is a natural foil that would actually strengthen the paper's argument by inviting the question: why does GRPO work at sentence-level but fail at document-level?

## Questions for Authors

1. The CED formula in Eq. 1 computes per-sentence entailment, but the code concatenates all cited sentences. Which is the actual method? Have you compared per-sentence vs. concatenation?

2. How exactly were the joint Evi-F1 numbers in Table 1 computed? The codebase evaluator only implements conditional Evi-F1. Was a separate script used?

3. Given that extraction-only reward also fails under GRPO+QLoRA (D022-D025), how do you distinguish "evidence-extraction decoupling" from general GRPO+QLoRA instability for structured generation?

4. What is the overlap rate between CED-selected and flat-NLI-selected top-1 candidates? The experiment data reports 78% -- does this mean CED and flat-NLI select the exact same candidate for 78% of documents?

5. For the DPO experiment: what learning rate, LoRA rank/alpha, and number of training epochs were used? How were preference pairs constructed -- is the preferred candidate always the CED-top-1 and the rejected always the CED-bottom-1 from each document's N=8 pool?

6. The GRPO G=8 experiment uses kl_coef=0.01 and lr=5e-6. The G=4 result in the paper also uses kl_coef=0.01 but was this the lr=5e-5 run (D026, best rel_F1=0.217 at step 100) or the lr=5e-6 run (D033, best rel_F1=0.014)? The paper needs to be precise about which G=4 configuration is being compared.

7. Have the results of the bf16 LoRA GRPO experiment (plan_011_grpo_g8_bf16) become available? This would substantially strengthen or weaken the decoupling claim.

## Soundness: 2/5

The paper has several implementation-vs-description mismatches (CED formula, EDCR definition, Evi-F1 protocol) that undermine confidence in the reported numbers. The central decoupling claim is confounded by QLoRA, and the extraction-only reward also failing suggests the phenomenon may be more general than presented. The DPO experiment lacks reproducibility detail. However, the RSFT improvement over SFT appears solid (p<0.01 on test).

## Excitement: 3/5

The evidence-extraction decoupling finding is genuinely interesting and the systematic paradigm comparison is valuable. The task definition fills a real gap. But the primary method (CED) does not outperform its simpler ablation, and RSFT is existing methodology applied to a new domain rather than a methodological advance.

## Overall: 2.5/5

The paper contains valuable empirical findings (decoupling, paradigm spectrum) and a credible task definition, but suffers from multiple implementation-description mismatches that erode trust in the reported results, an under-scoped key claim (QLoRA confound), and a title-contribution mismatch (CED prominence vs. non-significance). With the formula/code alignment fixed, the bf16 GRPO control completed, and honest CED reframing, this could reach borderline accept. In its current state, it is suitable for Findings but not Main at a ~22% acceptance rate.

## Confidence: 4/5

I have reviewed the paper, the full codebase (evaluation, CED scoring, RSFT training, GRPO training), the experimental decision log (46 decisions), and the experiment data. I am familiar with DocRE evaluation protocols, GRPO/DPO training, and QLoRA. My lower confidence on 1 point is because I could not verify whether a separate joint Evi-F1 computation exists outside the main codebase.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03714316-73ab-4ba3-bd18-bd2fbff57154",
  "isSidechain": true,
  "agentId": "aebcf4b7d1ca414e2",
  "requestId": "req_011Cb4Wkdx5Y431WznRoiAT6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5d87f32-4a57-4499-bc05-0f4cc8f065b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "5167ddfd-d536-4198-9738-76cb8f0f50e8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KEJuhp3XHNqVtAA7krGr8u",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 120567,
      "output_tokens": 3514,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 702
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3514,
          "cache_read_input_tokens": 120567,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 702,
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
