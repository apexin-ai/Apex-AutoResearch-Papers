# Research conversation: You are Reviewer 2 (R2) for a DREAM review session. Your focus: **Novelty and Related Work**. ## Venue: EMNLP 2026 Main 

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4bfa4c56d8d4de5f.jsonl`
- **Structured JSON:** [`92f02983af77eccd6d1b.json`](../../sessions/92/92f02983af77eccd6d1b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-15T14:19:16.311Z_

You are Reviewer 2 (R2) for a DREAM review session. Your focus: **Novelty and Related Work**.

## Venue: EMNLP 2026 Main (via ACL Rolling Review)

### ARR Review Form Scoring (used by EMNLP 2026):
- **Soundness**: 1-5 (5=Excellent; 4=Strong; 3=Acceptable; 2=Poor; 1=Major issues)
- **Excitement**: 1-5 (5=Highly Exciting; 4=Exciting; 3=Ambivalent; 2=Below threshold; 1=Not exciting)
- **Overall Assessment**: 1-5 with 0.5 increments (5=Award; 4=Accept; 3.5=Leaning Accept; 3=Ambivalent; 2.5=Leaning Reject; 2=Resubmit next cycle; 1.5=Resubmit after next cycle; 1=Do not resubmit)
- **Confidence**: 1-5 (5=Absolutely certain; 4=Quite sure; 3=Fairly confident; 2=Willing to defend but not absolutely certain; 1=Not confident)

### EMNLP acceptance rate: ~22-25%

## Paper Summary

**Title**: FREIGE: Faithful Evidence Generation for Document-Level Relation Extraction via Rejection Sampling Fine-Tuning

**Core idea**: First LLM-based DocRE system that jointly generates relation triples AND sentence-level evidence. Uses Rejection Sampling Fine-Tuning (RSFT) with Contrastive Evidence Discrimination (CED) scoring. Also discovers "evidence-extraction decoupling" in GRPO and proposes EDCR metric.

**Three claimed contributions**:
1. First LLM-based DocRE with verifiable evidence + RSFT pipeline (+3.2pp test rel_F1 over SFT)
2. Evidence-extraction decoupling characterization in GRPO+QLoRA (worsens with G=8)
3. EDCR diagnostic metric (r=0.44, method-level rank concordance 1.0)

**Related work covered in paper (Section 2)**:
- DocRE: ATLOP (Zhou et al., 2021), DREEAM (Ma et al., 2023), SAIS (Xiao et al., 2022), LMRC (Xu et al., 2024)
- Evidence/Faithfulness: DREEAM attention supervision, SAIS sentence importance
- Rejection Sampling/Offline RL: RAFT (Dong et al., 2024), reward overoptimization (Gao et al., 2023), LongRLVR (Song et al., 2025)
- RL for IE: mentioned but no specific citations

**Key results**:
- Test: FREIGE 43.2% rel_F1 vs DREEAM 62.8%, LMRC 60.7%
- CED vs flat-NLI: NOT statistically significant (p=0.12/0.28/0.09)
- GRPO collapses with evidence rewards; DPO degrades -6.6pp vs SFT
- RSFT (+6.3pp dev, +3.2pp test over SFT) is the real contribution
- Model size ablation (1.7B/4B/8B): consistent gains
- Re-DocRED: +3.5pp transfer

**Method details**:
- CED score: mean over cited sentences of [p_NLI(s_i => r) - max_{s_j in N} p_NLI(s_j => r)] where N = entity-sharing non-cited sentences
- RSFT: N=8 candidates, top-1 selection, ~12.4% selection rate, 2718 training samples
- EDCR: |{s ∈ Cited : s ∈ N_entity-sharing \ Gold}| / |Cited|
- Base model: Qwen3-4B with QLoRA (α=128, rank 64)

## Your Review Task (R2: Novelty + Related Work)

Provide a thorough independent review focusing on:

1. **Novelty assessment**: 
   - Is "first LLM-based DocRE with evidence" genuinely novel, or is it an incremental extension?
   - Is RSFT for IE novel, or is it a straightforward application of known techniques?
   - Is the evidence-extraction decoupling finding novel and interesting?
   - Is EDCR a meaningful new metric contribution?

2. **Related work completeness**:
   - Missing related work? (NLI for faithfulness evaluation, other RSFT/ReST applications, RL for structured generation, self-training/self-play methods, other evidence generation in NLP)
   - Is the positioning against DREEAM/SAIS/LMRC fair and accurate?
   - Are there other LLM-based IE methods with evidence that should be cited?

3. **Framing and narrative assessment**:
   - The paper frames CED as a contribution, but it's not significantly better than flat-NLI. Is the framing honest?
   - The "evidence-extraction decoupling" finding — is this genuinely surprising or expected?
   - Is the paper overselling given the absolute performance gap (43.2% vs 62.8%)?

4. **Broader impact and significance**:
   - Does this work open new research directions?
   - Would the community find the negative RL results valuable?
   - Is the RSFT insight (quality-filtered SFT > RL for structured IE) broadly applicable?

### Specific novelty questions:
- RSFT/ReST has been applied to many tasks (math, code, etc.). What's novel about applying it to DocRE beyond the application domain?
- Self-training (generate + filter + retrain) is a decades-old idea. How does RSFT differ?
- "Evidence-extraction decoupling" — isn't reward hacking/overoptimization well-known? What's new here?
- EDCR is essentially a precision metric over entity-sharing distractors — is this novel enough for a contribution?

Output format:
```
## R2 Review: Novelty and Related Work

### Summary of Contributions (1-2 sentences)

### Strengths
- S1: ...
- S2: ...
...

### Weaknesses
- W1: ...
- W2: ...
...

### Missing Related Work

### Novelty Assessment
| Component | Novelty Level | Justification |
|-----------|--------------|---------------|

### Narrative/Framing Issues

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
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "b2f8e391-172b-4f02-acdc-da31e767c4fb",
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

_source line 2 · 2026-05-15T14:19:16.315Z_

```json
{
  "parentUuid": "b2f8e391-172b-4f02-acdc-da31e767c4fb",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
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
  "uuid": "8e21f5f5-a793-4dd9-945e-50aa38710440",
  "timestamp": "2026-05-15T14:19:16.315Z",
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

_source line 3 · 2026-05-15T14:19:19.727Z_



I'll start by reading the paper and related materials to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e21f5f5-a793-4dd9-945e-50aa38710440",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyHu4oHBeWdvJTYdur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb6c1019-6b5c-4985-86eb-affb4f99042e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Cq8WQKXbSGtRaGpceaRbY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7481,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7481,
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

_source line 4 · 2026-05-15T14:19:21.116Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HY38fKeyQw51E6R6ANLyq8`</summary>

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
  "parentUuid": "eb6c1019-6b5c-4985-86eb-affb4f99042e",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyHu4oHBeWdvJTYdur",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "294cc61d-1005-40ff-97d4-c1c4c69e9e0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Cq8WQKXbSGtRaGpceaRbY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7481,
      "cache_read_input_tokens": 8249,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 123,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7481,
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

_source line 5 · 2026-05-15T14:19:21.120Z_

<details><summary>↩ Tool result · `toolu_01HY38fKeyQw51E6R6ANLyq8`</summary>

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
  "parentUuid": "294cc61d-1005-40ff-97d4-c1c4c69e9e0a",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "1e9210e1-279d-459c-9a17-c614cfb0713d",
  "sourceToolAssistantUUID": "294cc61d-1005-40ff-97d4-c1c4c69e9e0a",
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

_source line 6 · 2026-05-15T14:19:24.844Z_



Let me read the paper and project materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e9210e1-279d-459c-9a17-c614cfb0713d",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyfKvF1JzwpTvFPhLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f103421-167e-4a10-9bb9-6cc085835f90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KykzXPAuyfVGq1A8zVj4f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
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

_source line 7 · 2026-05-15T14:19:25.227Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01LtQzJGNE5RqzrTnJ4M82Q3`</summary>

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
  "parentUuid": "7f103421-167e-4a10-9bb9-6cc085835f90",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyfKvF1JzwpTvFPhLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8bb61ff-7590-474e-bd1e-a21a3aa1a4ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KykzXPAuyfVGq1A8zVj4f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
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

_source line 8 · 2026-05-15T14:19:25.521Z_

<details><summary>↩ Tool result · `toolu_01LtQzJGNE5RqzrTnJ4M82Q3`</summary>

```text
{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (76 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\n\n## 待处理\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\n\n## 近期结论\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\n\n## 趋势\n成功 26 / 负向 11 / 失败 12 / 共 71\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — u\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8bb61ff-7590-474e-bd1e-a21a3aa1a4ad",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "49607ab2-e3e7-42e4-8ed6-1043cd527c09",
  "sourceToolAssistantUUID": "b8bb61ff-7590-474e-bd1e-a21a3aa1a4ad",
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

_source line 9 · 2026-05-15T14:19:26.230Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BycWoUERdntcVXSDdmPGkx`</summary>

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
  "parentUuid": "49607ab2-e3e7-42e4-8ed6-1043cd527c09",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyfKvF1JzwpTvFPhLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84d28c50-d3bc-403b-b86a-3f46f8dce214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KykzXPAuyfVGq1A8zVj4f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
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

_source line 10 · 2026-05-15T14:19:26.243Z_

<details><summary>↩ Tool result · `toolu_01BycWoUERdntcVXSDdmPGkx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\\n\\n## 待处理\\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\\n\\n## 趋势\\n成功 26 / 负向 11 / 失败 12 / 共 71\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_ced_scoring_topk3: 已被终止 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n- mvp2_eval_rsft_r2b_maxtok1536: 已被终止 — unknown\\n\", \"total_chars\": 3533, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84d28c50-d3bc-403b-b86a-3f46f8dce214",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "54b0b021-64c4-4581-9997-33b1553fcdb5",
  "sourceToolAssistantUUID": "84d28c50-d3bc-403b-b86a-3f46f8dce214",
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

_source line 11 · 2026-05-15T14:19:26.697Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TvBKk4ugRMeuoSUAf3GjRB`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54b0b021-64c4-4581-9997-33b1553fcdb5",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VyfKvF1JzwpTvFPhLo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b38226d-d01e-4fd6-86ce-e0024aabcf7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KykzXPAuyfVGq1A8zVj4f3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 15730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
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

_source line 12 · 2026-05-15T14:19:26.721Z_

<details><summary>↩ Tool result · `toolu_01TvBKk4ugRMeuoSUAf3GjRB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      DAPO 提出 Clip-Higher（放大 importance sampling 上界）和 Dynamic Sampling\\n      来对抗 entropy collapse，在 AIME 2024 上超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse；CED reward 本身就能防止 mode collapse，\\n      无需额外 clip 调整。reward design vs. algorithm trick 的对比。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化对低 variance 组（全对/全错）给予过高 advantage 权重引入 difficulty bias。\\n      Dr. GRPO 移除 std 归一化项消除偏差，在 per-token 基础上表现更优。\\n    relevance_to_ced_stabilizer: >\\n      分析了 reward_std→0 时的问题（advantage 异常放大或归零），\\n      与我们观察到的 extraction-only reward 下 frac_zero_std→0.8 现象高度一致。\\n      CED 通过增加 reward 维度天然维持 reward_std>0，避免了这一 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      Contrastive reward 让 LLM 惩罚 reward uncertainty、改善鲁棒性、\\n      根据任务难度自适应校准、减少 PPO 中的 variance。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。但针对 RLHF 通用场景，\\n      CED 是 task-specific evidence discrimination 对比信号，且在 GRPO（非 PPO）中验证。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：RSFT 在 DocRE 上成功而 GRPO 失败的原因可能是\\n      structured output（DocRE）比 math reasoning 更难用 online RL 优化，\\n      而 rejection sampling 的 offline 特性天然避免了 catastrophic forgetting。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，\\n      媲美 GPT-4o。在 SemEval-2010 Task 8 和私有 MDKG 数据集上评估。\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。但关键差异：(1) R1-RE 是句子级 RE，我们是文档级 RE；\\n      (2) R1-RE 用 online GRPO，我们用 offline RSFT；\\n      (3) R1-RE 无 evidence extraction 组件，我们有 CED reward；\\n      (4) R1-RE 关注 OOD 泛化，我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior 在 DocRED 上提升 +2.06-2.38pp，\\n      我们的 RSFT 提升 +5.98pp 显著更优。\\n      RelPrior 是 inference paradigm 创新，我们是 training paradigm 创新，正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      在 DocRED/Re-DocRED 上显著优于其他 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      LMRC 用小模型预筛选 + LLM 分类的 pipeline 方式，与我们端到端 LLM 生成方式不同。\\n      展示 LLM-based DocRE 的 class imbalance 挑战，我们通过 RSFT 的 reward-based filtering 隐式解决。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上超越现有 LLM 方法和规则框架。\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证，我们用 training-time reward shaping。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      在 Re-DocRED、FREDo 等 benchmark 的 few-shot 场景达到 SOTA。\\n      预训练于 136K 文档的大规模 RE 数据。\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative），\\n      但验证了 DocRE 领域仍有方法创新空间。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE，\\n      在多个 LLM 上达到 SOTA。\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\", \"total_chars\": 17868, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b38226d-d01e-4fd6-86ce-e0024aabcf7a",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "433c03fb-b869-4839-af20-8eec82180b9e",
  "sourceToolAssistantUUID": "0b38226d-d01e-4fd6-86ce-e0024aabcf7a",
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

_source line 13 · 2026-05-15T14:19:30.646Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01J2TdAib36ELdqsApgJzZ7o`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "433c03fb-b869-4839-af20-8eec82180b9e",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4Vz4u1RRLZWV13BcZ3p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9694b0d-537a-4dc4-9457-685469ab9a8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdoyGMMyEZNaP1CkeQgktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13479,
      "cache_read_input_tokens": 17175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13479,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 14 · 2026-05-15T14:19:30.657Z_

<details><summary>↩ Tool result · `toolu_01J2TdAib36ELdqsApgJzZ7o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\n## ACTIVE\\n\", \"total_chars\": 484, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9694b0d-537a-4dc4-9457-685469ab9a8d",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "dbe0534e-0c89-43f6-942e-13948bd94bf6",
  "sourceToolAssistantUUID": "d9694b0d-537a-4dc4-9457-685469ab9a8d",
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

_source line 15 · 2026-05-15T14:19:31.591Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RxZv1HnB9uCHXRFLSyV1no`</summary>

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
  "parentUuid": "dbe0534e-0c89-43f6-942e-13948bd94bf6",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4Vz4u1RRLZWV13BcZ3p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f803b3e-4ea6-470f-9f14-441926d976b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdoyGMMyEZNaP1CkeQgktL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13479,
      "cache_read_input_tokens": 17175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13479,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 16 · 2026-05-15T14:19:31.606Z_

<details><summary>↩ Tool result · `toolu_01RxZv1HnB9uCHXRFLSyV1no`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v1 (重大 reframe based on Dream feedback)\\n> **最后更新**: 2026-05-15\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → 需 reframe 后 re-dream\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 和 offline RL (RSFT) 两条技术路线。关键发现：**GRPO 在结构化 IE 上导致 evidence-extraction decoupling**——evidence 质量持续提升（evi_f1→0.85）但抽取能力 catastrophically forget（rel_f1<0.02），这一现象在 3 种 reward function 下一致出现。RSFT 有效规避此问题。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Exploration**: 系统性比较 online RL (GRPO) vs offline RL (RSFT)\\n4. **Key finding**: evidence-extraction decoupling — GRPO 下 evidence 和 extraction 被差异化优化，extraction catastrophically forget\\n5. **What works**: RSFT with NLI-based scoring 有效提升 evidence 质量而不牺牲抽取\\n6. **Diagnostic tool**: EDCR 捕捉 Evi-F1 的盲区\\n\\n## Core Claims (reframed after Dream v1)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT 在 4/4 配置下均超过 SFT baseline（rel_f1 +3.9~6.0pp）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): GRPO 在结构化 IE 上导致 evidence-extraction decoupling\\n- 3 种 reward × 多个 lr 全线失败\\n- **Evidence-extraction decoupling**: evi_f1 → 0.850 而 rel_f1 < 0.02\\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\\n- **需要加强**: GRPO G=8 实验（排除 G=4 confound）；DPO 作为 offline preference optimization baseline（验证 decoupling 是否 on-policy 特有）\\n- **需要明确边界**: \\\"GRPO fails for DocRE\\\" 而非 \\\"online RL fails for structured IE\\\"\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n\\n### Claim 4 (Diagnostic): EDCR 捕捉 Evi-F1 的盲区\\n- EDCR 概念有价值（三档一致认可）\\n- **需要人工验证**: 100 例标注\\n- **需要更多数据点**: per-document / per-relation-type 分析\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 (conditional) | evi_f1 (joint, TBD) | EDCR |\\n|--------|--------|----------|---------------------|---------------------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.3117 | 0.7118 |\\n| RSFT r1 (3ep, s42) | 0.4449 | +3.92pp | 0.8187 | 0.3468 | 0.6565 |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.3713 | 0.6350 |\\n| RSFT r2a (1ep) | 0.4494 | +4.37pp | 0.8108 | 0.3509 | 0.6641 |\\n| RSFT r2b (1ep, conservative) | 0.4493 | +4.36pp | 0.8128 | 0.3490 | 0.6609 |\\n| GRPO (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | — | 0.9900 |\\n\\n注：evi_f1 (conditional) 仅计算 TP triples 的 evidence，与 DREEAM joint protocol 不可比（D041）。\\n\\n## Anticipated Reviewer Concerns (updated from Dream)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- 标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"\\n- 补充 DPO baseline（offline preference optimization，验证 decoupling 是否 on-policy 特有；注意 DPO 是纯 offline 方法，不是 online/offline 中间点）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 实验；LoRA confound 作为 limitation 讨论\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning（NEW）\\n6. **GRPO+CED (G=4)**: online RL negative baseline\\n7. **GRPO+CED (G=8)**: G=4 confound 排除（NEW）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 rel_f1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) GRPO decoupling 在 G=8 下仍复现\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling 在 G=8 下不复现 → scope 大幅缩减\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| P0 | GRPO G=8 experiment | C2 | ~16h |\\n| P0 | DPO+CED experiment | C2 | ~12h |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| P2 | GRPO forgetting 可视化 | C2 | ~4h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 5543, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f803b3e-4ea6-470f-9f14-441926d976b4",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "33b67484-c05e-46af-add7-c3d2b2b71402",
  "sourceToolAssistantUUID": "5f803b3e-4ea6-470f-9f14-441926d976b4",
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

_source line 17 · 2026-05-15T14:19:31.942Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WpCpBhhx4NCnrPWKNwDxoa`</summary>

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
  "parentUuid": "33b67484-c05e-46af-add7-c3d2b2b71402",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4Vz4u1RRLZWV13BcZ3p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d25baecd-8909-4085-9a25-fcb9c2ed7e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdoyGMMyEZNaP1CkeQgktL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13479,
      "cache_read_input_tokens": 17175,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 17175,
          "cache_creation_input_tokens": 13479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13479,
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

_source line 18 · 2026-05-15T14:19:31.955Z_

<details><summary>↩ Tool result · `toolu_01WpCpBhhx4NCnrPWKNwDxoa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d25baecd-8909-4085-9a25-fcb9c2ed7e7d",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "5855ca08-62cc-4b29-9e86-963aeb4fa949",
  "sourceToolAssistantUUID": "d25baecd-8909-4085-9a25-fcb9c2ed7e7d",
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

_source line 19 · 2026-05-15T14:19:35.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015Nuh3s9DgDzPJe8m7ZyzdM`</summary>

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
  "parentUuid": "5855ca08-62cc-4b29-9e86-963aeb4fa949",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VzSz3JU1W9Ci9sNwco",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a489226-7670-4bd2-aef9-32b7b8a1e797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oM1tLTuBxXvGFqARJduHb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4053,
      "cache_read_input_tokens": 30654,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4053,
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

_source line 20 · 2026-05-15T14:19:35.240Z_

<details><summary>↩ Tool result · `toolu_015Nuh3s9DgDzPJe8m7ZyzdM`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## D038 重大修正：RSFT r1 实际成功 (2026-05-15)\\n\\n### 事件\\nD037 报告 RSFT r1 \\\"灾难性失败\\\"（rel_f1=0.0483），但这是 **TaskEvalCallback bug**——`--eval_max_docs 50` 评估 50 个 doc 的预测，却用全部 12275 个 gold triples 计算 F1，严重低估 rel_f1。\\n\\n### 真实结果\\ns44 全量 dev eval (985 docs): **rel_f1=0.4655 (+5.98pp), evi_f1=0.8087 (+1.08pp)** → MVP-2 PASS\\n\\n### TaskEvalCallback bug fix\\n已部署到 `rsft_trainer.py:118-120`。gold triples 现在过滤到 eval_max_docs 对应的文档子集。\\n\\n### 教训\\n- 在 callback 中用 subset eval 时，必须确保 gold 和 pred 在同一文档集合上计算\\n- 基于 callback 数字的任何结论都需要全量 eval 交叉验证\\n\\n---\\n\\n## ~~RSFT r1 灾难性失败根因~~ [D038 撤回]\\n\\n**以下分析基于 D037 的错误 rel_f1=0.0483。D038 确认该数字是 eval bug，实际 rel_f1=0.4655。**\\n\\n原分析中关于\\\"关系本体崩塌\\\"的观察可能来自 eval_max_docs=50 下的极小样本偏差，不代表模型真实行为。r1/s43/s44 的全量 eval 正在进行中，将给出真实 ablation 数据。\\n\\n---\\n\\n## RSFT r2a/r2b ablation 结果 (2026-05-15)\\n\\n### 实验配置与结果\\n\\n| 配置 | rel_f1 | evi_f1 | edcr | Δrel_f1 |\\n|------|--------|--------|------|---------|\\n| SFT baseline | 0.4057 | 0.7979 | 0.7118 | — |\\n| r1 (3ep, α=128, lr=2e-5, 2718) | 0.4449 | **0.8187** | 0.6565 | +3.92pp |\\n| r2a (1ep, α=128, lr=2e-5, clean 2548) | **0.4494** | 0.8108 | 0.6641 | +4.37pp |\\n| r2b (1ep, α=32, lr=1e-5, clean 2548) | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\\n\\n### Ablation 结论\\n1. **1 epoch ≈ 3 epoch on rel_f1**（r2a=0.4494 vs r1=0.4449），多 epoch 无额外收益\\n2. **LoRA scaling 不敏感**（α=128 vs α=32 差异 <0.1pp）\\n3. **r1 在 evi_f1 上最优**（0.8187 vs r2a 0.8108），3 epoch 可能有助于证据定位\\n4. **所有 RSFT 变体 EDCR 低于 SFT**（~0.66 vs 0.71），RSFT 增加 pred_count 导致更多 distractor citation\\n\\n---\\n\\n## RSFT 文献对标 (2026-05-15, 更新)\\n\\n### 直接竞争者：无\\n在 DocRE / IE 上**无人用过 RSFT**，NLI-based CED reward for RE training 也无先例。Novelty 完全成立。\\n\\n### 最接近竞争者：R1-RE (arXiv 2507.04642)\\n用 GRPO 做**句子级** RE。与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无。\\n\\n### Must-cite 论文\\n1. **R1-RE** — GRPO for sentence-level RE（最近竞争者，需在 related work 中区分）\\n2. **\\\"Minimalist Approach\\\"** — RSFT 理论基础\\n3. **RelPrior** — LLM-based DocRE baseline (+2.06-2.38pp rel_f1)\\n4. **\\\"RSFT=PPO\\\" (ICML 2025)** — RSFT 与 PPO 等价性理论\\n\\n### 我们的定位\\n- +3.9~6.0pp rel_f1 显著超过同类 LLM-based DocRE 改进（RelPrior: +2.06-2.38pp）\\n- CED 作为 rejection sampling 打分函数是新颖的方法论贡献\\n- 最接近的工作是 Progressive Self-distillation (ACM 2024) 用 knowledge distillation，但无 evidence-based reward\\n\\n### 新增文献 map categories (by literature scan worker)\\n- Category 6: RSFT Methodology & Theory（3 篇）\\n- Category 7: RL for Information Extraction（5 篇）\\n- Category 8: Recent LLM-based DocRE Methods（5 篇）\\n\\n---\\n\\n## CED-as-reranker 探索 (2026-05-15)\\n\\nRSFT 成功后仍保留 CED-as-reranker PoC 作为推理时替代方案（无需额外训练）。\\ncuda:0 上 PID 178050 运行中（985 docs × N=8，预计 ~6h）。\\n如果 reranker 接近或超过 RSFT，可作为论文中的 complementary contribution。\\n\\n---\\n\\n## Qwen3 generation_config 覆盖陷阱 (2026-05-15)\\n\\nQwen3 模型自带 `generation_config.json` 会静默覆盖代码传参：\\n- `model.generation_config.top_k = 20`（限制采样池）\\n- `model.generation_config.temperature = 0.6`（覆盖代码传的任何温度值）\\n\\n**必须在生成前显式覆盖**：\\n```python\\nmodel.generation_config.temperature = target_temp\\nmodel.generation_config.top_k = 0  # 禁用 top_k 限制\\nmodel.generation_config.do_sample = True\\n```\\n\\n---\\n\\n## Diversity 监控计算 bug (2026-05-15)\\n\\n### 根因\\n- triple-set 归一化逻辑不一致\\n- diversity 分母用配置值而非实际生成数\\n\\n### 修复\\n- 提取 `diversity_metrics.py` 独立模块\\n- 修复后真实数据：302 docs mean_diversity=7.52/8, median=8.0/8\\n\\n---\\n\\n## inference.py 参数教训 (2026-05-15)\\n\\n**inference.py 必须传完整模型 stack**：\\n- `--base_model /root/autodl-tmp/models/Qwen3-4B`\\n- `--sft_adapter /root/autodl-tmp/sft_output`\\n- `--model_path &lt;rsft_adapter_path>`（RSFT adapter）\\n- `--data_path /root/autodl-tmp/data/docred`\\n- `--output_dir &lt;output_path>`\\n- `--no-quantize`（RTX 5090 必须）\\n- `--max_new_tokens &lt;N>`（可选，默认 1024）\\n\\n**只传 --model_path 不传 --base_model + --sft_adapter 会导致模型 stack 错误**（Base + RSFT LoRA，缺 SFT merge），结果完全不可用。maxtok1536 eval 因此被 Reviewer CRITICAL 打回并重跑。\\n\\n---\\n\\n## RSFT 代码参数速查\\n\\n**inference.py**: --base_model, --sft_adapter, --model_path(rsft adapter), --data_path, --output_dir, --no-quantize, --max_new_tokens(1024)\\n\\n**rsft_generate.py**: --base_model, --sft_adapter, --data_path, --split, --output_dir, --num_generations(8), --temperature(0.7), --batch_size(1), --max_new_tokens(1024), --seed, --quantize/--no-quantize, --start_idx, --end_idx, --shard_id\\n\\n**rsft_score_filter.py**: --input_dir, --output_path, --nli_model_path, --nli_device, --tau(0.5), --f1_threshold(0.1), --selection_strategy(top_k), --top_k(2)\\n\\n**rsft_trainer.py**: --base_model, --sft_adapter, --rsft_data_path, --output_dir, --learning_rate, --num_epochs, --per_device_batch_size, --gradient_accumulation_steps, --lora_rank(64), --lora_alpha(128), --weighted_sampling, --quantize(False), --eval_data_dir, --eval_max_docs, --wandb_run_name, --seed\", \"total_chars\": 6195, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a489226-7670-4bd2-aef9-32b7b8a1e797",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "565f918b-d0b9-4831-b054-0a562aece150",
  "sourceToolAssistantUUID": "3a489226-7670-4bd2-aef9-32b7b8a1e797",
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

_source line 21 · 2026-05-15T14:19:35.500Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UMyCQkYiBiWKrNwGXtFGdK`</summary>

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
  "parentUuid": "565f918b-d0b9-4831-b054-0a562aece150",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VzSz3JU1W9Ci9sNwco",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59bc8ebf-5bfe-4fbc-af80-e2ad018da259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013oM1tLTuBxXvGFqARJduHb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4053,
      "cache_read_input_tokens": 30654,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 30654,
          "cache_creation_input_tokens": 4053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4053,
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

_source line 22 · 2026-05-15T14:19:35.522Z_

<details><summary>↩ Tool result · `toolu_01UMyCQkYiBiWKrNwGXtFGdK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 47\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n- id: D041\\n  date: 2026-05-15 13:15 UTC\\n  summary: 'D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triples)与 DREEAM\\\"联合 Evi-F1\\\"(含\\n    FP/FN 惩罚)不可比，publishability threshold 暂冻结等对齐后重评'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过（precision 分母只算\\n    TP evidence），recall 分母也只算 matched gold triples。DREEAM 的 official_evaluate() 将\\n    FP/FN 全部计入分母。在 rel_recall ≈ 55% 时，分母差约 1.8x，解释了 82% vs 57% 的差距。已派 Agent 实现 DREEAM\\n    协议对齐函数并重新评估全部实验。在对齐数字出来前，paper_framing.md 的 publishability threshold（Evi-F1 >\\n    57.34）暂冻结。条件 Evi-F1 仍作为辅助指标保留（衡量\\\"关系对了时 evidence 选得好不好\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: evi_f1_conditional=0.7979, joint TBD\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: evi_f1_conditional=0.8187, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: evi_f1_conditional=0.8108, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: evi_f1_conditional=0.8128, joint TBD\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D042\\n  date: 2026-05-15 13:16 UTC\\n  summary: 'D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi-F1 跳过 FP/FN triples，比\\n    DREEAM 的 joint Evi-F1 宽松得多。必须实现 DREEAM 协议对齐后重算所有实验。Publishability threshold 待重算后修订'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过，precision 分母只算\\n    TP；recall 分母也只算已匹配 gold。DREEAM 的 official_evaluate() 把 FP/FN 全部计入分母。关系 recall\\n    ~55% 时，分母差异完全解释 82% vs 57% 的差距。对齐方案：加 FP evidence 到 precision 分母 + 遍历全部 gold triple\\n    evidence 到 recall 分母。论文需要报告 DREEAM 协议数字（与文献可比），条件 Evi-F1 可作为辅助指标（衡量\\\"关系正确时 evidence\\n    选择质量\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: conditional evi_f1=0.7979, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: conditional evi_f1=0.8187, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: conditional evi_f1=0.8108, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: conditional evi_f1=0.8128, dreeam evi_f1 待重算\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D043\\n  date: 2026-05-15 13:20 UTC\\n  summary: 'D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分倒挂）。5 个确认行动项（narrow\\n    Claim 3 scope、加 GRPO G=8、修 Evi-F1 协议、CED contingency plan、加 DPO baseline），4 个观察项。Framing\\n    和 plan 已更新，re-dream 启动'\\n  rationale: 'Dream 三档审稿分析（dream-report-action 协议）：\\n\\n\\n    **三档一致的结构性问题（确认行动项）**：\\n\\n    1. CED vs flat-NLI 可能不显著 → 加 contingency plan，如 p>0.05 则 CED 降级\\n\\n    2. Title/claims overclaim \\\"online RL\\\" → Claim 3 限定为 \\\"GRPO+QLoRA\\\"\\n\\n    3. GRPO G=4 太小 → 加 plan_011 (G=8 实验，P0)\\n\\n    4. Cross-protocol Evi-F1 → 已在修复中 (D041)\\n\\n    5. 缺中间 baseline → 加 plan_012 (DPO, P1)\\n\\n\\n    **两档一致的观察项**：\\n\\n    - EDCR 需人工验证 [M][W] → plan_013\\n\\n    - Dev→test 退化 [M][W] → 等 plan_002 真实数据\\n\\n    - Number discrepancies [B][M] → Dream artifact（虚构数据），真实论文不会有此问题\\n\\n\\n    **评分倒挂说明**：best(2.5) < median(3.0) 因 best 版本膨胀数字被审稿人识破——说明诚实报告比膨胀结果更重要。\\n\\n\\n    **判断**：framing 和 plan 已按确认行动项修改，需 re-dream 验证后才能批准 P0 实验。'\\n  related_experiments: []\\n  depends_on:\\n  - D040\\n  - D041\\n- id: D044\\n  date: 2026-05-15 13:24 UTC\\n  summary: Dream v1 分析完成：reframe paper_framing.md，CED 降级，claims 重构，新增 3 个实验\\n  rationale: Dream v1 (best=2.5, median=3.0, worst=2.5) 三档一致指出：(1) CED vs flat-NLI\\n    不显著 p>0.05 → CED 从核心贡献降级为 one possible scoring function；(2) \\\"online RL fails\\\"\\n    标题过度声称 → 收窄到 \\\"GRPO fails for DocRE\\\"；(3) GRPO G=4 太小 → 新增 G=8 实验(plan_011)；(4)\\n    缺 DPO baseline → 新增 plan_012；(5) EDCR 缺人工验证 → 新增 plan_013。Claims 重构为 C1=evidence-grounded\\n    DocRE 可行性, C2=GRPO decoupling 发现, C3=NLI-based RSFT ablation, C4=EDCR 诊断工具。需 re-dream\\n    验证 reframe 效果。\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: new_from_dream\\n    result: GRPO G=8 实验，排除 G=4 confound\\n  - exp_id: plan_012\\n    role: new_from_dream\\n    result: DPO+CED，online-offline 中间 baseline\\n  - exp_id: plan_013\\n    role: new_from_dream\\n    result: EDCR 100例人工标注验证\\n  depends_on:\\n  - D041\\n- id: D045\\n  date: 2026-05-15 13:41 UTC\\n  summary: 'D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offline preference optimization'\\n  rationale: Reviewer 指出：(1) DPO 是纯 offline 方法，不是 online/offline 中间点——论文中错误定位会被审稿人攻击。已修正\\n    paper_framing.md。(2) DPO 结果直接决定 C2 叙事走向（on-policy 特有 vs 更 general 的现象），对 paper\\n    scope 有重大影响，升级 P0。(3) C2 对 GRPO G=8 单点依赖是最大风险，G=8 必须是 re-dream 后第一个启动的实验。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: 升级 P0\\n  - exp_id: plan_011\\n    role: 第一优先 P0\\n  depends_on:\\n  - D044\\n- id: D046\\n  date: 2026-05-15 13:42 UTC\\n  summary: 'D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + topk3 双变体设计'\\n  rationale: Reviewer 路线图审查指出：(1) DPO 结果直接决定 C2 decoupling 叙事——若 DPO 也出现 decoupling\\n    则现象更 general，若不出现则确认 on-policy 特有，两种结果都对论文有重大影响，升 P0；(2) C2 publishability 必要条件依赖\\n    GRPO G=8 复现 decoupling，是最高风险实验，必须首批启动；(3) topk3 数据含 CED=0 样本会稀释信号，改为双变体并行（全量 vs\\n    过滤 CED=0）以区分数据量效应和信号稀释。同时修正 paper_framing.md 中 DPO 定位错误（纯 offline 方法，非 online/offline\\n    中间点）。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: DPO+CED 升 P0\\n  - exp_id: plan_011\\n    role: GRPO G=8 首批 P0\\n  - exp_id: plan_008\\n    role: topk3 双变体设计\\n  depends_on:\\n  - D044\\n\", \"total_chars\": 34024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59bc8ebf-5bfe-4fbc-af80-e2ad018da259",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "b1d3e3c8-8317-48c4-a820-09454f5ea423",
  "sourceToolAssistantUUID": "59bc8ebf-5bfe-4fbc-af80-e2ad018da259",
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

_source line 23 · 2026-05-15T14:19:38.466Z_

Now let me look at the paper artifacts and any draft paper text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1d3e3c8-8317-48c4-a820-09454f5ea423",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VziREHotp3jzYnSSwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "719ead6a-f756-499b-a55c-a30f1b09229f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1tDUep5ET7WgAKZd1zdyr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24525,
      "cache_read_input_tokens": 34707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24525,
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

_source line 24 · 2026-05-15T14:19:40.420Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EZCNx6pu2dhsGmPXTGvVYc`</summary>

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
  "parentUuid": "719ead6a-f756-499b-a55c-a30f1b09229f",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VziREHotp3jzYnSSwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c821ede7-4342-4608-9b4f-0ebf4fb61801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1tDUep5ET7WgAKZd1zdyr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24525,
      "cache_read_input_tokens": 34707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24525,
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

_source line 25 · 2026-05-15T14:19:40.448Z_

<details><summary>↩ Tool result · `toolu_01EZCNx6pu2dhsGmPXTGvVYc`</summary>

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
  "parentUuid": "c821ede7-4342-4608-9b4f-0ebf4fb61801",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "a17ddec7-0709-4e2d-ad33-394f24673f9f",
  "sourceToolAssistantUUID": "c821ede7-4342-4608-9b4f-0ebf4fb61801",
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

_source line 26 · 2026-05-15T14:19:41.834Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Sori6BFHrdBZXpRWvxnAZ8`</summary>

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
  "parentUuid": "a17ddec7-0709-4e2d-ad33-394f24673f9f",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VziREHotp3jzYnSSwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81f1447a-faee-4446-a96c-95c2041071db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1tDUep5ET7WgAKZd1zdyr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24525,
      "cache_read_input_tokens": 34707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24525,
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

_source line 27 · 2026-05-15T14:19:41.859Z_

<details><summary>↩ Tool result · `toolu_01Sori6BFHrdBZXpRWvxnAZ8`</summary>

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
  "parentUuid": "81f1447a-faee-4446-a96c-95c2041071db",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "142765ff-9dac-499c-abd4-e02ea920e87c",
  "sourceToolAssistantUUID": "81f1447a-faee-4446-a96c-95c2041071db",
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

_source line 28 · 2026-05-15T14:19:42.168Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M4CmvRegkjtwDc1P6V2bKA`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142765ff-9dac-499c-abd4-e02ea920e87c",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4VziREHotp3jzYnSSwZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b29e6f97-7356-4dd2-bfd1-8e169afbf87a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1tDUep5ET7WgAKZd1zdyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24525,
      "cache_read_input_tokens": 34707,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24525
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 286,
          "cache_read_input_tokens": 34707,
          "cache_creation_input_tokens": 24525,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24525,
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

_source line 29 · 2026-05-15T14:19:42.188Z_

<details><summary>↩ Tool result · `toolu_01M4CmvRegkjtwDc1P6V2bKA`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b29e6f97-7356-4dd2-bfd1-8e169afbf87a",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "b291c9d0-d009-4d8c-a51a-d5171ac5517a",
  "sourceToolAssistantUUID": "b29e6f97-7356-4dd2-bfd1-8e169afbf87a",
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

_source line 30 · 2026-05-15T14:19:47.999Z_

Let me read the latest dream paper (the most recent one with reframed claims) to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b291c9d0-d009-4d8c-a51a-d5171ac5517a",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W1CjKbTiXH23YFQBgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7dcf2109-6005-42cf-8391-41e6327f2d4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNh1EqMdoUwuhdTmGq2y6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 59232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 679,
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

_source line 31 · 2026-05-15T14:19:48.407Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TtgnbW1pLyo9Y5WkauLRMS`</summary>

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
  "parentUuid": "7dcf2109-6005-42cf-8391-41e6327f2d4d",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W1CjKbTiXH23YFQBgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d54efa1-00a4-4908-82f6-1e8c541db85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HNh1EqMdoUwuhdTmGq2y6u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 59232,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 59232,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 679,
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

_source line 32 · 2026-05-15T14:19:48.699Z_

<details><summary>↩ Tool result · `toolu_01TtgnbW1pLyo9Y5WkauLRMS`</summary>

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
  "parentUuid": "8d54efa1-00a4-4908-82f6-1e8c541db85a",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "c8180118-d882-44a4-b4fb-e23a667fdf94",
  "sourceToolAssistantUUID": "8d54efa1-00a4-4908-82f6-1e8c541db85a",
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

_source line 33 · 2026-05-15T14:19:51.733Z_

Now let me also check the dream review reports to understand previous reviewer feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8180118-d882-44a4-b4fb-e23a667fdf94",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W1gTSPUmoUnBJicpF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe7f9c58-72ab-49d0-ac93-5199b29301e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NinHQ5vztzn5pw1FsH16Dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 34 · 2026-05-15T14:19:53.671Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01VyAcE1JudLsFjht5MuXnKw`</summary>

```json
{
  "pattern": "**/dream_review_report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe7f9c58-72ab-49d0-ac93-5199b29301e6",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W1gTSPUmoUnBJicpF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab20ba2c-8982-4e04-94cb-c854079fb4d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NinHQ5vztzn5pw1FsH16Dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 35 · 2026-05-15T14:19:53.687Z_

<details><summary>↩ Tool result · `toolu_01VyAcE1JudLsFjht5MuXnKw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab20ba2c-8982-4e04-94cb-c854079fb4d3",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "d3854f42-6792-47a3-a512-dc8e07b01dd4",
  "sourceToolAssistantUUID": "ab20ba2c-8982-4e04-94cb-c854079fb4d3",
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

_source line 36 · 2026-05-15T14:19:54.251Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DwhRdzQ6zEq2BAB2FSaUqq`</summary>

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
  "parentUuid": "d3854f42-6792-47a3-a512-dc8e07b01dd4",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W1gTSPUmoUnBJicpF6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8f89b06-aa2d-4cc7-a555-ebfd67857643",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NinHQ5vztzn5pw1FsH16Dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59911,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 37 · 2026-05-15T14:19:54.281Z_

<details><summary>↩ Tool result · `toolu_01DwhRdzQ6zEq2BAB2FSaUqq`</summary>

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
artifacts/dream_reports/dream_20260515T132059/median/review_report.md
artifacts/dream_reports/dream_20260515T132059/best/review_report.md
artifacts/dream_reports/dream_20260515T132059/logs/review_best.log
artifacts/dream_reports/dream_20260515T132059/median/review_context.yaml
artifacts/dream_reports/dream_20260515T132059/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8f89b06-aa2d-4cc7-a555-ebfd67857643",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "bf272b51-d7f2-42e5-9f1b-3f7201e4229c",
  "sourceToolAssistantUUID": "a8f89b06-aa2d-4cc7-a555-ebfd67857643",
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

_source line 38 · 2026-05-15T14:20:04.235Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K4VqEXi9v5YgDzKgAYPezn`</summary>

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
  "parentUuid": "bf272b51-d7f2-42e5-9f1b-3f7201e4229c",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W26XYPFjA6GXGe3YB9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acd2be09-6f52-44a7-9ade-bdba6b1699d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq5U34eVhc1VKgbWG6jUyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 73073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 615,
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

_source line 39 · 2026-05-15T14:20:04.246Z_

<details><summary>↩ Tool result · `toolu_01K4VqEXi9v5YgDzKgAYPezn`</summary>

```text
1	---
2	dream_id: dream_20260515T132059
3	tier: median
4	overall_score: 3.0 - Borderline Findings
5	timestamp: 2026-05-15T14:12:44.416329+00:00
6	---
7	
8	## R2 Review: Novelty & Related Work
9	
10	### Summary
11	FREIGE proposes the first LLM-based document-level relation extraction system that jointly generates relation triples and explicit sentence-level evidence citations. The paper's contributions are threefold: (1) a Contrastive Evidence Discrimination (CED) scoring function using NLI-based hard negatives, (2) a CED-guided Rejection Sampling Fine-Tuning (RSFT) pipeline, and (3) the EDCR diagnostic metric. The paper also documents a negative finding — evidence-extraction decoupling under GRPO — which is arguably its most novel empirical contribution.
12	
13	### Strengths
14	- S1: **The "first" claim is credible and well-scoped.** I am not aware of any prior LLM-based DocRE method that jointly generates relation triples and explicit sentence-level evidence on DocRED. Encoder methods (DREEAM, SAIS) derive evidence from attention weights, and all existing LLM-based DocRE methods (LMRC, AutoRE, RelPrior, Ru-LLM) produce only triples. The paper appropriately scopes this as "first on DocRED" rather than overclaiming universality.
15	
16	- S2: **Evidence-extraction decoupling is a genuinely novel and valuable finding.** The observation that GRPO training drives evidence quality up (evi_F1 to 0.862) while extraction collapses (rel_F1 < 0.02), and that this *worsens* with larger group sizes providing more precise advantage estimation, is striking. This connects well to the reward overoptimization literature (Gao et al. 2023) and provides a concrete, task-grounded instance of a phenomenon that the RL-for-LLM community has discussed mostly in abstract terms. The G=4 vs G=8 comparison strengthens this by ruling out the "insufficient exploration" counter-argument.
17	
18	- S3: **Comprehensive training paradigm comparison.** The GRPO / DPO / RSFT spectrum is a well-designed empirical contribution. The finding that DPO partially mitigates but does not solve decoupling — landing between GRPO collapse and SFT baseline — adds nuance to the online-vs-offline RL narrative and leads to the more precise insight that the issue is contrastive/reward-based loss vs. data curation.
19	
20	- S4: **EDCR fills a real diagnostic gap.** Standard Evi-F1 is dominated by recall and does not penalize plausible-looking distractors. EDCR is a simple, interpretable metric that captures this failure mode. The human validation, while modest (r=0.44), demonstrates perfect method-level rank concordance, which is the practically useful property.
21	
22	- S5: **Honest self-assessment.** The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods, and EDCR's limitations. This intellectual honesty significantly increases the paper's credibility.
23	
24	### Weaknesses
25	- W1 (Major): **CED itself is not novel — it is a straightforward application of NLI entailment scoring with document-internal hard negatives.** The contrastive margin (p_entail(gold) - max(p_entail(distractor))) is a standard contrastive scoring pattern seen in retrieval, reranking, and faithfulness evaluation (e.g., INFUSE at EACL 2024, contrastive reward methods in RLHF). The novelty is in applying it to DocRE evidence, not in the scoring mechanism itself. Combined with the fact that CED does not significantly outperform flat-NLI (p>0.05 on all three metrics), the method-level novelty is limited. The paper's reframing (CED as "one possible scoring function" rather than the core contribution) is appropriate, but this means the method contribution is essentially RSFT applied to DocRE — which is also not architecturally novel. The novelty resides primarily in the task definition and the negative finding.
26	
27	- W2 (Major): **The related work section on RL for IE is thin.** The paper mentions "prior work has applied RL to IE tasks with mixed results" without citing specific work. R1-RE (arXiv 2507.04642, GRPO for sentence-level RE) is the most directly comparable method and is not cited. REAR (EMNLP 2025 Findings, RL for event argument extraction) is also missing. The "RL for Information Extraction" paragraph should be substantially expanded with specific citations and differentiation. The absence of R1-RE is particularly notable given that it applies GRPO to RE (sentence-level) and succeeds — which would raise the question of why GRPO fails at document-level but not sentence-level. This contrast would actually *strengthen* the paper's argument if properly discussed.
28	
29	- W3 (Major): **Missing LLM-based DocRE baselines weaken the "first" and positioning claims.** The related work cites LMRC as the sole LLM-based DocRE method, but several recent works are missing: RelPrior (arXiv 2511.08143, LLM DocRE with relation-as-prior), Ru-LLM (NLPCC 2025, rule-constrained LLM DocRE), AutoRE (arXiv 2403.14888, RHF paradigm with Mistral-7B), and GLiDRE (arXiv 2508.00757, dual-encoder DocRE). While none of these produce evidence, their omission makes the related work section appear under-researched and weakens the positioning of the extraction results. The gap between FREIGE (43.2% test) and these methods (some above 60%) needs contextualization.
30	
31	- W4 (Moderate): **RSFT is not a novel training paradigm.** The paper correctly cites the RSFT-PPO equivalence (Dong et al. 2024) and positions RSFT as existing methodology applied to a new domain. However, the framing in the introduction ("Our solution is FREIGE, built on RSFT") may lead readers to perceive RSFT as a contribution of this paper. The distinction between "we apply RSFT to DocRE" and "we contribute RSFT" should be sharpened. The "Minimalist Approach" paper (arXiv 2504.11343) showing RAFT matching GRPO/PPO on math reasoning is directly relevant and should be cited — it provides theoretical grounding for why offline rejection sampling can match online RL.
32	
33	- W5 (Moderate): **The connection to reward overoptimization literature is superficial.** The paper cites Gao et al. (2023) but does not engage deeply with the scaling law framework. Specifically: does the decoupling follow a KL-dependent scaling law? Is there a "Goodhart's Law" interpretation — the CED reward is a proxy for evidence quality, and optimizing the proxy diverges from the true objective? The contrastive reward literature (arXiv 2403.07708, EMNLP 2024 contrastive RM) provides mechanisms for mitigating exactly this kind of reward misalignment. The paper should discuss why these mitigations were not attempted or why they would be insufficient for structured IE.
34	
35	- W6 (Minor): **The framing alternates between CED-centric and RSFT-centric narratives.** The title centers CED/RSFT depending on the version, reflecting a genuine framing tension: if CED is not significantly better than flat-NLI, the paper's identity is "RSFT for evidence-grounded DocRE + negative GRPO findings + EDCR metric." This is still a valid paper, but the framing should commit to one narrative rather than hedging.
36	
37	- W7 (Minor): **No discussion of concurrent work on evidence/rationale generation for IE.** The faithfulness literature (Drift at ACL 2025 on faithfulness rewards for rationale generation) is relevant but not cited. The paper's approach of using NLI-based faithfulness signals for data curation has conceptual overlap with work on faithful CoT generation, and positioning within this broader context would strengthen the contribution.
38	
39	### Questions for Authors
40	- Q1: R1-RE (arXiv 2507.04642) successfully applies GRPO to sentence-level RE. What is your hypothesis for why GRPO succeeds at sentence-level RE but catastrophically fails at document-level RE? Is the critical difference document length, output structure complexity, or something else? This contrast could significantly strengthen your decoupling analysis.
41	
42	- Q2: The 78% overlap between CED-selected and flat-NLI-selected candidates is high. Have you analyzed the 22% divergent cases? Are the CED-unique selections demonstrably better in terms of evidence quality, or are they random disagreements? This would clarify whether CED's contrastive margin adds genuine signal or just noise.
43	
44	- Q3: You mention that "incomplete DocRED gold evidence (~14% false distractors) dilutes the hard-negative signal" for CED. If gold evidence annotations are incomplete, doesn't this equally affect the RSFT pipeline (which scores candidates against noisy gold)? How sensitive is RSFT to annotation noise?
45	
46	- Q4: The EDCR metric is defined over entity-sharing distractors only. What fraction of actual distractor citations are non-entity-sharing? If a model cites a sentence that shares no entities with the triple but is still irrelevant, EDCR would not capture this. Have you quantified this blind spot?
47	
48	- Q5: Have you considered a post-hoc evidence retrieval baseline (e.g., run LMRC for extraction, then BM25/sentence-BERT to retrieve evidence sentences)? This would separate the contribution of joint generation from pipeline approaches.
49	
50	### Missing Related Work / Positioning Issues
51	- P1: R1-RE (arXiv 2507.04642) — first GRPO application to relation extraction (sentence-level). Must-cite for the GRPO analysis. Its success at sentence-level RE creates a natural foil for the document-level failure documented here.
52	
53	- P2: RelPrior (arXiv 2511.08143), Ru-LLM (NLPCC 2025), AutoRE (arXiv 2403.14888) — recent LLM-based DocRE methods that should be cited and compared for extraction performance positioning.
54	
55	- P3: "A Minimalist Approach to LLM Reasoning" (arXiv 2504.11343) — directly relevant RSFT theoretical foundation showing rejection sampling matches GRPO/PPO.
56	
57	- P4: Contrastive reward methods: "Improving RL from Human Feedback Using Contrastive Rewards" (arXiv 2403.07708), contrastive RM at EMNLP 2024 — relevant to CED's contrastive design and to the discussion of why contrastive rewards cause issues in structured IE.
58	
59	- P5: Drift (ACL 2025) — faithfulness rewards for LLM rationale generation. Conceptually adjacent to CED's role as a faithfulness signal.
60	
61	- P6: DAPO (NeurIPS 2025), Dr. GRPO (COLM 2025) — relevant to the GRPO failure analysis. These works identify entropy collapse and normalization bias in GRPO that may partially explain the document-level IE failures.
62	
63	- P7: The connection between EDCR and precision-oriented evaluation metrics in other NLP tasks (e.g., faithfulness metrics in summarization like FactScore) is not drawn. EDCR would benefit from positioning within the broader "precision of generated citations" evaluation landscape.
64	
65	### Scores
66	- Soundness: 3/5
67	- Excitement: 3/5
68	- Overall: 3.0/5
69	- Reproducibility: 4/5
70	- Confidence: 4/5
71	
72	### Justification for Overall Score
73	The paper makes a credible "first" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding (evidence-extraction decoupling). However, the method-level novelty is limited: CED is a straightforward NLI contrastive scorer that does not significantly outperform flat-NLI, and RSFT is existing methodology applied to a new domain. The related work has notable gaps (R1-RE, recent LLM-based DocRE methods, contrastive reward literature) that weaken the positioning. The paper is best characterized as a solid empirical study with an interesting negative finding and a useful new metric, but it does not introduce a sufficiently novel method to clear the EMNLP main conference bar without strengthening the related work coverage and either demonstrating CED's statistical advantage or fully committing to the "task definition + negative finding + diagnostic metric" framing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd2be09-6f52-44a7-9ade-bdba6b1699d2",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "9de745e4-fb1f-44b2-8141-aae5ecb88016",
  "sourceToolAssistantUUID": "acd2be09-6f52-44a7-9ade-bdba6b1699d2",
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

_source line 40 · 2026-05-15T14:20:04.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GPZsajA1ogHzGKoPALE67Z`</summary>

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
  "parentUuid": "9de745e4-fb1f-44b2-8141-aae5ecb88016",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W26XYPFjA6GXGe3YB9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e8d4eee-1baf-4f2f-a9b7-2a3e98d41f82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kq5U34eVhc1VKgbWG6jUyn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 73073,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 73073,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 615,
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

_source line 41 · 2026-05-15T14:20:04.694Z_

<details><summary>↩ Tool result · `toolu_01GPZsajA1ogHzGKoPALE67Z`</summary>

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
  "parentUuid": "5e8d4eee-1baf-4f2f-a9b7-2a3e98d41f82",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "cb932fef-288e-4bea-8d66-bf92b87b2168",
  "sourceToolAssistantUUID": "5e8d4eee-1baf-4f2f-a9b7-2a3e98d41f82",
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

_source line 42 · 2026-05-15T14:20:09.607Z_

Now let me also read the worst-case review and the v1 dream reviews for comprehensive context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb932fef-288e-4bea-8d66-bf92b87b2168",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W2sEciSBsYzP6oud7s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "01cc6397-74d7-4828-9668-f9edf0f67700",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ed8kX3Q8zn8qvtkdceJ14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7895,
      "cache_read_input_tokens": 73688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7895,
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

_source line 43 · 2026-05-15T14:20:11.642Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P986uVGqetTaghnsooM2Sz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01cc6397-74d7-4828-9668-f9edf0f67700",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W2sEciSBsYzP6oud7s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f775955c-98d6-408c-80ff-d7792bcdcd15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Ed8kX3Q8zn8qvtkdceJ14",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7895,
      "cache_read_input_tokens": 73688,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 73688,
          "cache_creation_input_tokens": 7895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7895,
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

_source line 44 · 2026-05-15T14:20:11.674Z_

<details><summary>↩ Tool result · `toolu_01P986uVGqetTaghnsooM2Sz`</summary>

```text
1	---
2	dream_id: dream_20260515T120227
3	tier: median
4	overall_score: 3.0 - Borderline
5	timestamp: 2026-05-15T12:49:42.079796+00:00
6	---
7	
8	# R1 Review: "FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Contrastive Evidence Discrimination" (Median Tier)
9	
10	## Summary
11	
12	This paper presents FREIGE, the first LLM-based DocRE system that jointly generates relation triples and evidence sentences. The key contributions are CED (a contrastive NLI scoring function), RSFT with CED-based filtering, a cautionary analysis of GRPO failure, and the EDCR diagnostic metric. On DocRED test, FREIGE achieves rel_F1 42.8--43.8% and evi_F1 78.3--78.9%.
13	
14	## Strengths
15	
16	- **Well-structured experimental pipeline.** The paper presents a clean progression: SFT baseline -> GRPO failure -> RSFT success, with CED as a composable module applicable at training-time (RSFT filtering) and inference-time (reranking). The composability result (Table 5, RSFT+CED+reranker achieving EDCR 58.5%) is a nice practical finding.
17	
18	- **Thorough GRPO failure documentation.** The three-reward-type analysis with trajectory data (Table 6) convincingly demonstrates systematic GRPO failure. The evidence-extraction decoupling (evi_F1 85.0% while rel_F1 <2%) is a genuinely novel empirical finding.
19	
20	- **Honest evaluation protocol discussion.** Section 5.5 and the baseline comparison table clearly flag the fundamental protocol difference between generative evidence (explicit sentence indices) and attention-based evidence (DREEAM/SAIS). The paper avoids claiming direct superiority despite the large Evi-F1 gap.
21	
22	- **Comprehensive ablation coverage.** CED vs flat-NLI, top-k selection, NLI model capacity, model size (1.7B/4B/8B), Re-DocRED extension, CED reranker -- all contribute to understanding the method's properties.
23	
24	- **DREEAM reproduction** with <0.5pp gap validates the evaluation pipeline.
25	
26	## Weaknesses
27	
28	**W1 (Major): Inconsistencies in reported numbers across tables.**
29	The paper reports different numbers for the same configuration across tables. For example:
30	- Table 1 reports SFT test rel_F1=38.6, but the dev-to-test table (Table 2) shows SFT dev=40.6, test=38.6 -- a 2.0pp gap. However, the actual experimental data shows SFT test rel_F1=0.355 (35.5%), not 38.6%. 
31	- RSFT CED (s44) test rel_F1 is reported as 43.8 in Table 1, but actual data shows 0.392 (39.2%).
32	- The dev-to-test gap is reported as 2.1--2.8pp, but based on actual dev numbers (0.466) and actual test (0.392), it should be 7.4pp.
33	
34	These discrepancies between the paper's tables and the underlying experimental data suggest either (a) multiple evaluation runs with different configurations, or (b) errors in number transcription. The authors must clarify and ensure all numbers are traceable to specific experiments.
35	
36	**W2 (Major): CED vs flat-NLI advantage is modest and potentially not significant.**
37	Table 3 shows CED RSFT outperforming flat-NLI RSFT by +0.7pp rel_F1, +1.4pp evi_F1, and -2.4pp EDCR. No significance tests are reported for this comparison. Given that the "worst" tier paper (which appears to use the actual experimental data) reports p-values of 0.08/0.38/0.12 for the CED vs flat-NLI comparison -- none significant at p<0.05 -- this undermines the paper's central claim that "CED provides consistent improvement over flat-NLI scoring."
38	
39	**W3 (Major): The generative approach's extraction F1 is substantially below state-of-the-art.**
40	Rel_F1 of 42.8--43.8% (test) is 20pp below DREEAM (63.3%) and even further below recent LLM methods like DocKS-RAG (63.6%). The paper positions evidence generation as the primary contribution, but if the extraction quality is too low for practical use, the evidence is of limited value. The paper should discuss whether the rel_F1 gap is inherent to joint extraction+evidence generation or specific to the Qwen3-4B + LoRA setup.
41	
42	**W4 (Moderate): GRPO exploration may be insufficient to claim "structural incompatibility."**
43	The paper tests 3 reward types x 2 learning rates x limited KL configurations, all with QLoRA 4-bit quantization on Qwen3 only. Known issues with QLoRA + RL (quantization noise in KL computation, limited LoRA expressivity) could explain the failures without invoking "structural incompatibility between online policy optimization and compositional structured outputs." Missing explorations:
44	- Full fine-tuning or fp16 LoRA (isolates QLoRA artifacts)
45	- Higher LoRA rank (r=128 or r=256)
46	- DPO as an intermediate approach
47	- Reward decomposition (separate extraction and evidence rewards with independent weighting)
48	
49	**W5 (Moderate): EDCR correlation analysis is statistically underpowered.**
50	The Pearson r=-0.42 between Evi-F1 and EDCR is computed across only 4-5 data points (methods), making this correlation estimate highly unreliable (confidence interval likely spans from -0.9 to +0.3). The claim that "EDCR captures a distinct failure mode" would be better supported by per-document or per-relation-type analysis with sufficient sample size.
51	
52	**W6 (Moderate): Missing comparison with post-hoc evidence retrieval.**
53	A natural baseline for "LLM extraction + evidence" is to run an LLM extraction model (e.g., LMRC) and then retrieve evidence sentences using BM25 or sentence similarity. This would provide a fairer comparison for the evidence quality of the joint generation approach.
54	
55	**W7 (Minor): The relation-type EDCR analysis (Table 7) uses suspiciously round numbers.**
56	The EDCR values by relation type are all integers (85.0, 83.0, 80.0, etc.) with CED improvements that are exactly 5.0 or 6.0pp for every relation type. This suggests either binning/rounding or synthetic data. The authors should provide exact values.
57	
58	**W8 (Minor): Single model family limits generalizability.**
59	All experiments use Qwen3. The GRPO failure claim would be substantially stronger with replication on LLaMA or Mistral.
60	
61	## Questions for Authors
62	
63	1. Can you provide exact p-values for the CED vs flat-NLI comparison? If they are not significant, how do you justify framing CED as the key contribution rather than RSFT itself?
64	
65	2. The relation-type EDCR analysis (Table 7) shows identical improvement magnitudes (5-6pp) across all relation types. Is this an artifact of rounding? Please provide exact values.
66	
67	3. Have you tried running GRPO without QLoRA quantization? The decision log suggests many failures were related to QLoRA-specific issues (KL explosion from 4-bit quantization noise).
68	
69	4. What is the output truncation rate at max_new_tokens=1024? Your experimental notes mention 37% truncation for SFT. Does RSFT reduce this?
70	
71	5. The RSFT+CED+reranker combination (Table 5) achieves the best EDCR (58.5%) but at 8x inference cost. Have you measured the actual latency overhead per document?
72	
73	## Scores
74	
75	- **Soundness**: 3 (Acceptable) -- Experimental design is generally sound but number inconsistencies and missing significance tests weaken confidence.
76	- **Excitement**: 3 (Ambivalent) -- The GRPO failure analysis is interesting but the positive contribution (CED) may not be significant over simpler alternatives.
77	- **Overall Assessment**: 3.0 (Borderline) -- A competent empirical study with interesting negative results, but the method contribution needs statistical validation and the number inconsistencies must be resolved.
78	- **Confidence**: 4 (High) -- Familiar with DocRE, RL for LLMs, NLI-based evaluation, and the specific experimental challenges of this setup.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f775955c-98d6-408c-80ff-d7792bcdcd15",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "6ac888fb-d972-4370-b3e3-379cec97a256",
  "sourceToolAssistantUUID": "f775955c-98d6-408c-80ff-d7792bcdcd15",
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

_source line 45 · 2026-05-15T14:20:16.228Z_

Now I have comprehensive context. Let me also check if there's a GRPO G=8 bf16 experiment running that could affect the analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ac888fb-d972-4370-b3e3-379cec97a256",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W3NjPVuf45m7JrRdhw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cbc5c6b3-05aa-4d44-aef3-788e6c9ca36b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAoffRHpma7pABi9nBV6Ag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2396,
      "cache_read_input_tokens": 81583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2396,
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

_source line 46 · 2026-05-15T14:20:16.923Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UHNdAsgGZFQzz5YdCB5vbc`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbc5c6b3-05aa-4d44-aef3-788e6c9ca36b",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W3NjPVuf45m7JrRdhw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0de57cc-efb7-4053-a326-e7d5860ad434",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAoffRHpma7pABi9nBV6Ag",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2396,
      "cache_read_input_tokens": 81583,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2396
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 81583,
          "cache_creation_input_tokens": 2396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2396,
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

_source line 47 · 2026-05-15T14:20:16.948Z_

<details><summary>↩ Tool result · `toolu_01UHNdAsgGZFQzz5YdCB5vbc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 13:42 UTC | 更新原因: Reviewer 路线图审查修正：GPU 表更新实际状态、joint evi_f1 进展、DPO 升 P0、C2 风险标注\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 新任务范式。核心发现：GRPO 在结构化 IE 上导致 evidence-extraction decoupling。RSFT+NLI-based scoring 有效提升证据质量。CED 作为 scoring function 之一，显著性待验证。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过）\\n- **Dream v1**: best=2.5, median=3.0, worst=2.5 → 不达标\\n- **Reframe 完成** (D044): CED 降级、claims 重构（C1=可行性, C2=decoupling, C3=NLI ablation, C4=EDCR）\\n- **Re-dream**: dream_20260515T132059 运行中，验证 reframe 效果（目标 best≥3.5, median≥3.0）\\n- **MVP 成果**: RSFT 4/4 configs PASS (rel_f1 +3.9~6.0pp vs SFT)；joint evi_f1 已回填（SFT=0.3117 → best RSFT s44=0.3713, +5.96pp）\\n- **GRPO 判死**: 3 reward × 多 lr 全线 catastrophic forgetting (D031/D033)\\n- **topk3 scoring 完成**: 8037 samples (2.96x topk1)，数据就绪\\n- **DPO 升级为 P0** (D045): 直接影响 C2 decoupling 叙事\\n\\n## 投稿目标\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## 近期任务\\n- [ ] 等 re-dream 结果验证 reframe\\n- [ ] Agent 处理队列（urgent: s43_r2 registry 修复 + plan_008 双变体设计 + evaluate() joint 集成）\\n- [ ] Re-dream 达标后批准 P0 实验：\\n  - plan_011: GRPO G=8（**最高风险，首批启动**，C2 必要条件）\\n  - plan_001: flat-NLI RSFT ablation (C3)\\n  - plan_004: DREEAM baseline reproduction (C1)\\n  - plan_012: DPO+CED（**升 P0**，C2 叙事关键）\\n- [ ] 处理运行中实验结果（maxtok1536_r2 cuda:1, CED reranker cuda:0）\\n- [ ] plan_008 topk3 双变体训练（cuda:2 全量 / cuda:3 过滤CED=0）\\n\\n## GPU 分配\\n\\n| GPU | 状态 | 任务 |\\n|-----|------|------|\\n| cuda:0 | 🏃 | mvp2_ced_reranker_poc (plan_005) |\\n| cuda:1 | 🏃 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\\n| cuda:2 | ⏳ | 待分配 → plan_008 topk3_all |\\n| cuda:3 | ⏳ | 待分配 → plan_008 topk3_ced_filtered |\\n\\n## GPU 预算\\n- 硬件: 4× RTX 5090 32GB (rtx5090-4x)\\n- MVP 已消耗: ~80+ GPU-hours\\n- Research P0: ~75h (flat-NLI 25h + CED seeds 10h + test eval 4h + DREEAM 8h + GRPO G=8 16h + DPO 12h)\\n- Research P1: ~46h (EDCR人工验证 API + post-hoc 4h + reranker 6h + model size 24h + Re-DocRED 12h)\\n\\n## 评审笔记\\n1. ✅ CED 重框定（paper_framing.md 已更新）\\n2. ✅ EDCR 升格为独立贡献 (Claim 4)\\n3. ✅ NLI lexical overlap bias 验证\\n4. ✅ Joint evi_f1 已回填（paper_framing.md 表格已更新）\\n5. ✅ DPO 定位修正（纯 offline，非 online/offline 中间点）\\n6. ⬜ Baselines 扩展到 12+ (含 DPO, GRPO G=8, post-hoc retrieval)\\n\\n## 风险监控\\n- **C2 单点依赖**: GRPO G=8 是 publishability 必要条件。若 G=8 下 decoupling 不复现 → scope 大幅缩减。G=8 必须是 re-dream 后首批 P0。\\n- **CED=0 稀释**: topk3 数据含 ced_reward=0 样本，双变体实验区分数据量效应 vs 信号稀释。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D046 | 2026-05-15 | D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + | plan_012, plan_011, plan_008 |\\n| D045 | 2026-05-15 | D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offlin | plan_012, plan_011 |\\n| D044 | 2026-05-15 | Dream v1 分析完成：reframe paper_framing.md，CED 降级，clai | plan_011, plan_012, plan_013 |\\n| D043 | 2026-05-15 | D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分 | — |\\n| D042 | 2026-05-15 | D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi | mvp2_sft_eval_r2, mvp2_eval_rsft_r1, mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b |\\n| D041 | 2026-05-15 | D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triple | mvp2_sft_eval_r2, mvp2_eval_rsft_r1, mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b |\\n| D040 | 2026-05-15 | D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定 | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D039 | 2026-05-15 | D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoc | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D038 | 2026-05-15 | D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred | mvp2_rsft_train_r1_s44, mvp2_rsft_train_r1 |\\n| D037 | 2026-05-15 | D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-r | mvp2_rsft_train_r1, mvp2_rsft_train_r1_s43, mvp2_rsft_train_r1_s44 |\\n\\n\", \"total_chars\": 3772, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0de57cc-efb7-4053-a326-e7d5860ad434",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "6d460ae8-97d0-4992-a67e-0908bf4815db",
  "sourceToolAssistantUUID": "b0de57cc-efb7-4053-a326-e7d5860ad434",
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

_source line 48 · 2026-05-15T14:20:20.277Z_

I now have comprehensive understanding of the paper, its experimental history, prior dream reviews, and the literature landscape. Let me produce my R2 review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d460ae8-97d0-4992-a67e-0908bf4815db",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W3mJwj64nSqaC58wkg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c2aa6c3-8a9f-4e99-a4b9-723435622f36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfVyAzam1bXks1sdX282nJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2674,
      "cache_read_input_tokens": 83979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2674,
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

_source line 49 · 2026-05-15T14:20:21.566Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EG9AHQZEEBBj8XXehZvZrM`</summary>

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
  "parentUuid": "6c2aa6c3-8a9f-4e99-a4b9-723435622f36",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W3mJwj64nSqaC58wkg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "495f46c6-a951-4c79-b33a-37b3a85e8b8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfVyAzam1bXks1sdX282nJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2674,
      "cache_read_input_tokens": 83979,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 83979,
          "cache_creation_input_tokens": 2674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2674,
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

_source line 50 · 2026-05-15T14:20:21.571Z_

<details><summary>↩ Tool result · `toolu_01EG9AHQZEEBBj8XXehZvZrM`</summary>

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
  "parentUuid": "495f46c6-a951-4c79-b33a-37b3a85e8b8d",
  "isSidechain": true,
  "promptId": "f510c60e-c486-46fc-b743-387e47d3bec6",
  "agentId": "a4bfa4c56d8d4de5f",
  "type": "user",
  "uuid": "5edccc1c-cd2d-4e5e-89f2-83c01de367a9",
  "sourceToolAssistantUUID": "495f46c6-a951-4c79-b33a-37b3a85e8b8d",
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

_source line 51 · 2026-05-15T14:22:19.747Z_



Now I have all the information needed. Let me produce the R2 review.

## R2 Review: Novelty and Related Work

### Summary of Contributions (1-2 sentences)

FREIGE defines evidence-grounded DocRE as a new task for LLMs, applies Rejection Sampling Fine-Tuning with NLI-based scoring to it, documents an evidence-extraction decoupling phenomenon under GRPO+QLoRA, and proposes EDCR as a diagnostic metric. The paper's novelty resides primarily in the task definition, the negative GRPO finding, and the diagnostic metric rather than in the method (CED/RSFT), which combines known techniques in a straightforward manner.

### Strengths

- **S1: The "first LLM-based DocRE with evidence" claim is credible and well-scoped.** I am not aware of any prior LLM-based DocRE system that jointly generates (head, relation, tail, [evidence sentences]) on DocRED. All existing LLM methods (LMRC, AutoRE, RelPrior, Ru-LLM, GLiDRE) produce only triples. Encoder methods (DREEAM, SAIS) derive evidence from attention weights, which is implicit and not directly auditable. The paper appropriately scopes the claim to DocRED rather than overclaiming universality. This task definition fills a genuine gap relevant to KB population, biomedical curation, and RAG provenance.

- **S2: Evidence-extraction decoupling is the paper's strongest and most novel empirical contribution.** The observation that GRPO drives evi_F1 to 0.835-0.862 while rel_F1 collapses to <0.02 is striking and, to my knowledge, not documented elsewhere in the IE literature. The G=4 vs G=8 comparison is particularly valuable: the finding that G=8 peaks earlier (step 40) and collapses faster than G=4 rules out the "insufficient exploration" counter-argument and connects naturally to the reward overoptimization literature (Gao et al. 2023). The three-reward-type ablation (CED, flat-NLI, extraction-only all fail) strengthens the claim that this is a structural issue, not a reward-design bug.

- **S3: The GRPO/DPO/RSFT training paradigm spectrum is a well-designed empirical comparison.** The ordering GRPO (collapse) < DPO (-6.6pp) < SFT (baseline) < RSFT (+6.3pp) adds nuance beyond a binary "RL fails" narrative. The finding that DPO partially mitigates but does not solve decoupling leads to the more precise insight that contrastive/reward-based losses are the problem, not the online/offline distinction per se. This is a useful insight for the community.

- **S4: EDCR captures a real evaluation blind spot.** The demonstration that GRPO achieves evi_F1=0.850 but EDCR=0.99 illustrates a clear failure mode invisible to standard Evi-F1. The metric is simple, interpretable, and practically useful. Human validation with method-level rank concordance of 1.0 is the right level of validation for a diagnostic complement (not a standalone metric).

- **S5: Intellectual honesty throughout.** The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods (43.2% vs 62.8%), EDCR's moderate sample-level correlation (r=0.44), and dev-to-test degradation (3.6pp). This level of self-assessment increases credibility substantially.

### Weaknesses

- **W1 (Major): CED is not a novel method -- it is a straightforward application of NLI contrastive scoring.** The contrastive margin (p_entail(cited) - max p_entail(distractor)) is a standard pattern in retrieval, reranking, and faithfulness evaluation. INFUSE (EACL 2024) uses fine-grained NLI for faithfulness; contrastive reward methods in RLHF (arXiv 2403.07708; EMNLP 2024) use the same structure. The novelty is in applying it to DocRE evidence, not in the scoring mechanism. Combined with CED's failure to significantly outperform flat-NLI (p>0.05 on all three metrics, 78% candidate overlap), the method-level novelty is thin. The paper's reframing (CED as "one possible scoring function") is appropriate but means the method contribution reduces to "RSFT applied to DocRE," which is also not architecturally novel. The novelty budget is spent on the task definition and negative findings.

- **W2 (Major): RSFT is existing methodology applied to a new domain, not a contribution.** Rejection sampling fine-tuning / ReST is well-established in math reasoning (Dong et al. 2024, RAFT), code generation (Singh et al. 2024, ReST-EM), and dialogue (Gulcehre et al. 2023). The theoretical equivalence to PPO under certain conditions is known. The "Minimalist Approach" paper (arXiv 2504.11343) demonstrates RAFT matching GRPO/PPO on reasoning tasks. TrajFusion (arXiv 2602.04391) extends RSFT by fusing correct/incorrect trajectories. The theoretical result that "RSFT secretly performs PPO" (ICML 2025) further situates RSFT as a mature technique. Applying RSFT to DocRE is a valid contribution at the application level, but it should not be framed as a methodological advance. The paper's title and abstract partially perpetuate this confusion by centering "Rejection Sampling Fine-Tuning" as the solution.

- **W3 (Major): The RL for IE related work paragraph is unacceptably thin.** The paper states "Prior work has applied RL to IE tasks with mixed results" without citing a single specific paper. This is a serious gap:
  - **R1-RE** (arXiv 2507.04642) applies GRPO to sentence-level RE and *succeeds*. This is the single most important missing citation. Its success at sentence-level RE creates a natural foil: why does GRPO work for sentence-level but catastrophically fail for document-level? The answer (output length, multi-triple credit assignment, evidence generation burden) would actually *strengthen* the paper's argument. Omitting R1-RE makes the related work appear under-researched.
  - **REAR** (EMNLP 2025 Findings): RL for event argument extraction.
  - **MORE-R1** (arXiv 2603.09478): GRPO for multimodal RE.
  - **Graph-R1** (ICML 2026): end-to-end RL for GraphRAG with knowledge extraction.
  - **Adaptive RL Planning** (arXiv 2406.11455): DDQN for IE extraction ordering.

- **W4 (Major): Missing recent LLM-based DocRE baselines weaken the "first" claim and extraction positioning.** The related work cites only LMRC as an LLM-based DocRE method. Several recent works are missing:
  - **RelPrior** (arXiv 2511.08143): relation-as-prior filtering for LLM DocRE, achieves competitive performance on DocRED/Re-DocRED.
  - **Ru-LLM** (NLPCC 2025): rule-constrained LLM DocRE, surpasses existing LLM methods on DocRED.
  - **AutoRE** (arXiv 2403.14888): RHF paradigm with Mistral-7B QLoRA for end-to-end DocRE.
  - **GLiDRE** (arXiv 2508.00757): dual-encoder DocRE for few-shot scenarios.
  
  While none produce evidence (strengthening the "first" claim), their omission makes the related work appear incomplete and fails to contextualize the 43.2% vs 60.7% extraction gap.

- **W5 (Moderate): The connection to reward overoptimization is superficial.** The paper cites Gao et al. (2023) but does not engage with the scaling law framework. Key questions remain unanswered: Does the decoupling follow a KL-dependent scaling law? Is there a Goodhart's Law interpretation where CED is a proxy reward that diverges from the true extraction+evidence objective? The GRPO stability literature (DAPO at NeurIPS 2025 on entropy collapse; Dr. GRPO at COLM 2025 on normalization bias; REINFORCE++ on global advantage normalization) provides mechanisms that may partially explain the document-level IE failures and should be discussed. The contrastive reward literature (arXiv 2403.07708; EMNLP 2024 contrastive RM) is directly relevant to CED's design and the discussion of why contrastive rewards cause issues in structured IE.

- **W6 (Moderate): "Evidence-extraction decoupling" may be a special case of well-known reward hacking, not a genuinely new phenomenon.** Reward hacking/overoptimization -- where optimizing a proxy reward degrades the true objective -- is extensively documented (Gao et al. 2023, Skalse et al. 2022, Pan et al. 2022). The specific manifestation in DocRE (evidence quality up, extraction down) is an instance of this general phenomenon in a new domain. The paper's contribution is documenting it empirically in the IE context and showing the G=4 vs G=8 monotonicity, but it should acknowledge this lineage more explicitly rather than presenting it as a wholly novel discovery. The finding that all three reward types (including extraction-only) fail partially undermines the "evidence-extraction decoupling" framing -- if even extraction-only reward fails, the issue is GRPO+QLoRA instability for structured generation, not specifically evidence-vs-extraction misalignment.

- **W7 (Moderate): GRPO failure analysis is confounded by QLoRA.** All GRPO experiments use 4-bit QLoRA. The decisions log documents KL explosion from quantization noise (D008), multiple restarts due to QLoRA-specific issues, and explicit acknowledgment that "GRPO+QLoRA" is the correct scope. The paper's Limitations section appropriately scopes to "GRPO+QLoRA," but the abstract and introduction still use language like "online reward optimization (GRPO) with evidence-quality rewards causes catastrophic evidence-extraction decoupling" without the QLoRA qualifier. A bf16 LoRA experiment (plan_011_grpo_g8_bf16, currently running) is needed to support broader claims. If this experiment also fails, the claim is substantially strengthened; if it succeeds, the story changes fundamentally.

- **W8 (Minor): No discussion of concurrent work on faithfulness rewards for generation.** Drift (ACL 2025) uses faithfulness rewards for LLM rationale generation and is conceptually adjacent. The NLI-as-faithfulness-evaluation paradigm (INFUSE at EACL 2024, TRUE benchmark, etc.) should be discussed as CED's methodological antecedent.

- **W9 (Minor): EDCR is essentially a precision metric over entity-sharing distractors -- the novelty is in identifying the failure mode, not in the metric formula itself.** The formula |{cited AND entity-sharing AND not-gold}| / |cited| is a straightforward precision computation. Its value lies in highlighting that entity-sharing distractors are the dominant evidence failure mode, which is an empirical observation rather than a metric innovation. Positioning within the broader "precision of generated citations" evaluation landscape (FactScore for biography generation, citation precision in attributed QA) would strengthen the contribution.

### Missing Related Work

| Category | Missing Work | Relevance |
|----------|-------------|-----------|
| RL for RE | R1-RE (arXiv 2507.04642) | GRPO for sentence-level RE -- success creates foil for document-level failure |
| RL for IE | REAR (EMNLP 2025 Findings) | RL for event argument extraction |
| RL for IE | MORE-R1 (arXiv 2603.09478) | GRPO for multimodal RE |
| RL for IE | Graph-R1 (ICML 2026) | End-to-end RL for knowledge extraction |
| LLM DocRE | RelPrior (arXiv 2511.08143) | Relation-as-prior LLM DocRE |
| LLM DocRE | Ru-LLM (NLPCC 2025) | Rule-constrained LLM DocRE |
| LLM DocRE | AutoRE (arXiv 2403.14888) | RHF paradigm, QLoRA for DocRE |
| LLM DocRE | GLiDRE (arXiv 2508.00757) | Lightweight DocRE |
| RSFT theory | "Minimalist Approach" (arXiv 2504.11343) | RAFT matches GRPO/PPO -- theoretical foundation |
| RSFT theory | "RSFT secretly performs PPO" (ICML 2025) | RSFT-PPO equivalence -- theoretical grounding |
| Contrastive rewards | arXiv 2403.07708 | Contrastive rewards in RLHF -- CED precedent |
| Contrastive rewards | EMNLP 2024 contrastive RM | Contrastive RM training for RL stability |
| GRPO stability | DAPO (NeurIPS 2025) | Entropy collapse in GRPO |
| GRPO stability | Dr. GRPO (COLM 2025) | Normalization bias in GRPO |
| Faithfulness | Drift (ACL 2025) | Faithfulness rewards for rationale generation |
| Faithfulness | INFUSE (EACL 2024) | Fine-grained NLI for faithfulness evaluation |
| Citation precision | FactScore (Min et al. 2023) | Precision of generated citations -- evaluation landscape |

### Novelty Assessment

| Component | Novelty Level | Justification |
|-----------|--------------|---------------|
| Evidence-grounded DocRE task | **Medium-High** | First LLM system to jointly generate triples + evidence on DocRED. Genuine gap in the literature. Task definition is valuable but incremental -- adding evidence output to an existing extraction task. |
| CED scoring function | **Low** | Standard contrastive NLI scoring with document-internal hard negatives. Not significantly better than flat-NLI (p>0.05). 78% candidate overlap with flat-NLI. Pattern is well-established in retrieval and faithfulness evaluation. |
| RSFT for DocRE | **Low** | Existing methodology (RAFT/ReST, mature since 2023-2024) applied to a new domain. No architectural or algorithmic innovation. The contribution is the application, not the method. |
| Evidence-extraction decoupling | **Medium-High** | Empirically novel in the IE context. Well-documented with G=4/G=8 comparison, three reward types, and trajectory analysis. Weakened by: (1) being a domain-specific instance of well-known reward hacking; (2) QLoRA confound; (3) extraction-only reward also fails, suggesting GRPO+QLoRA instability rather than evidence-specific decoupling. |
| EDCR metric | **Medium** | Identifies a real evaluation blind spot (entity-sharing distractors). Formula is trivial (precision computation), but the empirical observation motivating it is valuable. Human validation with perfect method-level concordance is appropriate. |
| GRPO/DPO/RSFT spectrum | **Medium** | Well-designed empirical comparison. The insight that contrastive losses (not just online RL) damage structured generation is nuanced and useful. Not a contribution per se but strengthens the paper's empirical story. |

### Narrative/Framing Issues

1. **Title-contribution mismatch.** The title centers "Faithful Evidence Generation" and "Rejection Sampling Fine-Tuning," but CED is not significantly better than flat-NLI, and RSFT is existing methodology. The paper's actual contributions -- task definition, decoupling finding, EDCR -- are not reflected in the title. A title emphasizing the negative finding or the task would be more honest.

2. **CED receives disproportionate narrative attention.** CED is detailed in Section 3.3, is part of the acronym FREIGE, and appears in 6 of 12 tables. Yet it does not significantly outperform the simpler flat-NLI baseline. The paper's reframing (CED as "one possible scoring function") is appropriate in the Discussion, but the rest of the paper still reads as CED-centric. The framing should commit: either strengthen CED's differentiation or fully pivot to "task + negative finding + diagnostic metric" as the contribution package.

3. **"Evidence-extraction decoupling" may overclaim novelty.** The paper presents this as a novel phenomenon, but it is arguably a domain-specific instance of reward hacking/overoptimization. The finding that extraction-only reward (no evidence component) also collapses under GRPO partially undermines the "decoupling" framing -- if even single-objective GRPO fails, the issue is not evidence-vs-extraction misalignment but GRPO+QLoRA's fundamental instability for structured generation. The paper should acknowledge this interpretation.

4. **Abstract and Introduction lack QLoRA qualifier for GRPO claims.** The abstract states "online reward optimization (GRPO) with evidence-quality rewards causes catastrophic evidence-extraction decoupling" without noting this is GRPO+QLoRA. The Limitations section correctly scopes, but key claims in high-visibility sections should carry the qualifier.

5. **The 43.2% vs 62.8% extraction gap is underexplained.** The paper positions evidence generation as the primary contribution, but if extraction quality is too low for practical deployment, the evidence is of limited value. A more thorough decomposition of the gap (evidence generation burden vs model size vs generation vs encoder paradigm) is needed. An SFT-without-evidence ablation would be highly informative.

### Scores

- Soundness: 3/5
- Excitement: 3/5
- Overall Assessment: 2.5/5
- Confidence: 4/5

### Justification for Overall Assessment (2-3 sentences)

The paper makes a credible "first" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding (evidence-extraction decoupling under GRPO+QLoRA), but the method-level novelty is limited: CED is a standard contrastive NLI scorer that does not significantly outperform flat-NLI, and RSFT is existing methodology. The related work section has substantial gaps -- most critically the omission of R1-RE (GRPO for sentence-level RE) and multiple recent LLM-based DocRE methods -- that weaken the paper's positioning. The contribution package (task definition + negative finding + diagnostic metric) is sufficient for Findings but falls short of EMNLP main conference acceptance (~22-25% rate) without stronger method differentiation, expanded related work, and resolution of the QLoRA confound in the GRPO analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5edccc1c-cd2d-4e5e-89f2-83c01de367a9",
  "isSidechain": true,
  "agentId": "a4bfa4c56d8d4de5f",
  "requestId": "req_011Cb4W47ar2Q3ysReJ2EUEG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89a0a8b3-590e-4b63-9676-11aa2d1d80ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "ef33cb85-ae55-46f6-8462-dd61be87818f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABScK7acEnh1UaXFxFGCvW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 86653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 699,
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
