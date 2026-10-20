# Research conversation: You are Reviewer 1 (R1) for a blind peer review of a paper submitted to EMNLP 2026 Main (via ACL Rolling Review). Your f

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a423c10c857240397.jsonl`
- **Structured JSON:** [`e80ea97b5c00d23bec5f.json`](../../sessions/e8/e80ea97b5c00d23bec5f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-15T12:46:55.765Z_

You are Reviewer 1 (R1) for a blind peer review of a paper submitted to EMNLP 2026 Main (via ACL Rolling Review). Your focus areas are **Methods** and **Experiments**.

## ARR Review Scoring (EMNLP 2026)
- **Soundness**: 1-5 (5=Excellent, 4=Strong, 3=Acceptable, 2=Borderline, 1=Poor)
- **Excitement**: 1-5 (5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Below Average, 1=Not Exciting)
- **Overall Assessment**: 1-5 with half-points (5=Award-worthy, 4=Accept main, 3.5=Leaning accept, 3=Borderline, 2.5=Leaning reject, 2=Reject/resubmit, 1.5=Major revision needed, 1=Do not resubmit)

## Paper: "Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead"

**Abstract**: Studies online RL (GRPO) for document-level RE with evidence generation on DocRED. Finds GRPO universally fails: reward increases while extraction F1 collapses. Evidence learning and relation extraction decouple. Proposes RSFT with NLI-based filtering as practical alternative (+3.7 F1 on test). Introduces EDCR metric for entity-sharing distractor citations.

**Three contributions**: (1) Systematic demonstration that GRPO fails for structured IE with evidence–extraction decoupling analysis (§5). (2) RSFT with NLI-based filtering as effective offline alternative (§6). (3) EDCR diagnostic metric (§7).

**Methods (§3)**:
- Task: generate (h, r, t, E) tuples from documents as sequence generation
- NLI-based evidence scoring using DeBERTa-v3-base on MNLI; CED = contrastive margin: p_pos(evidence) - max p_pos(distractor)
- GRPO with G=4 rollouts, 3 reward types (CED, flat-NLI, extract-only), KL β∈{0.01,0.1}, lr∈{5e-5, 5e-6}
- RSFT: sample N=8 candidates, filter by NLI score, top-k∈{1,3}, fine-tune with LoRA
- EDCR = |{s∈E_pred : s∉E_gold ∧ shares_entity(s,h,t)}| / |E_pred|

**Key Experimental Results**:

Table 1 - GRPO failure across reward types:
- CED (lr=5e-5, β=0.01): best rel_F1=0.217, evi_F1=0.575
- CED (lr=5e-6): best rel_F1=0.014, evi_F1=0.850
- flat-NLI: ~0 for both, collapse at step 25
- extract-only: ~0 for both, collapse at step 30

Table 3 - Dev set:
- SFT baseline: rel_F1=0.406, evi_F1=0.798, EDCR=0.712
- RSFT+CED (s44): rel_F1=0.466, evi_F1=0.809, EDCR=0.635
- RSFT flat-NLI: rel_F1=0.452, evi_F1=0.811, EDCR=0.662

Table 4 - CED vs flat-NLI for RSFT:
- Δ(CED best − flat-NLI): +1.4pp rel_F1, -0.2pp evi_F1, -2.7pp EDCR
- p-values: 0.08, 0.38, 0.12 — **none significant at p<0.05**

Table 5 - Test set:
- SFT test: rel_F1=0.355, evi_F1=0.752
- RSFT+CED test: rel_F1=0.392, evi_F1=0.765
- Dev→test degradation: -7.4pp rel_F1, -4.4pp evi_F1

Table 6 - Comparison with encoder baselines:
- DREEAM (paper test): rel_F1=0.630, evi_F1=0.573
- DREEAM (reproduced dev): rel_F1=0.632, evi_F1=0.608
- RSFT+CED dev: rel_F1=0.466, evi_F1=0.809
- Cross-protocol comparison (generative sentence indices vs attention-based extraction)

Table 7 - Cross-method EDCR:
- GRPO: evi_F1=0.567, EDCR=0.858
- SFT: evi_F1=0.798, EDCR=0.712
- RSFT+CED: evi_F1=0.809, EDCR=0.635
- Correlation r=-0.42

Table 8 - Model size ablation:
- 1.7B: RSFT gain +2.6pp rel_F1
- 4B: RSFT gain +6.0pp rel_F1
- 8B: RSFT gain +1.7pp rel_F1
- Non-monotonic: 4B is sweet spot

Table 9 - Re-DocRED:
- RSFT gain shrinks from +6.0pp to +2.3pp with cleaner annotations

Table 10 - top-k ablation: top-1 vs top-3 differences are small

Table 11 - NLI model ablation: DeBERTa-large doesn't improve downstream RSFT

**Experiment design reference (what was planned)**:
10 experiments were planned: (1) CED vs flat-NLI ablation, (2) test set evaluation, (3) EDCR cross-method diagnostic, (4) DREEAM reproduction, (5) CED-as-reranker, (6) model size ablation 1.7B/8B, (7) Re-DocRED extension, (8) top_k ablation, (9) GRPO forgetting analysis + visualization, (10) NLI model ablation. All 10 appear covered in the paper.

## Your Task

Write a detailed R1 review focusing on:
1. **Methodological soundness**: Is the experimental design rigorous? Are conclusions supported by evidence?
2. **Statistical rigor**: Are significance tests appropriate? Are claims overclaimed given p-values?
3. **Experimental coverage**: Missing baselines, missing ablations, fairness of comparisons
4. **Reproducibility**: Are details sufficient to reproduce?
5. **Specific weaknesses in method/experiment design**

Structure your review as:
- Summary of contributions (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, numbered W1, W2, etc.)
- Questions for authors
- Scores: Soundness, Excitement, Overall Assessment (use ARR scale above)
- Confidence: 1-5 (5=expert, 3=knowledgeable, 1=not familiar)

Be rigorous but fair. Give specific, actionable feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "bc6d4f6f-d58c-43c5-8fd8-ede245acd513",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T12:46:55.770Z_

```json
{
  "parentUuid": "bc6d4f6f-d58c-43c5-8fd8-ede245acd513",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
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
  "uuid": "8fd4d31b-fc92-4f05-a39f-83f239db07e2",
  "timestamp": "2026-05-15T12:46:55.770Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T12:46:58.627Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd4d31b-fc92-4f05-a39f-83f239db07e2",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NvsgvG7fYP87Wr1NNZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d6fa1f-2fa4-48c8-b328-7f9956adc06d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvpL1HY1aeGEau7Hq6xZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7639,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7639,
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

_source line 4 · 2026-05-15T12:46:59.103Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013UyiXrJMKyUTG4A94XHhrY`</summary>

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
  "parentUuid": "52d6fa1f-2fa4-48c8-b328-7f9956adc06d",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NvsgvG7fYP87Wr1NNZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "581e5641-82d3-493d-8805-615ee2465482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvpL1HY1aeGEau7Hq6xZY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7639,
      "cache_read_input_tokens": 8249,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7639,
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

_source line 5 · 2026-05-15T12:46:59.107Z_

<details><summary>↩ Tool result · `toolu_013UyiXrJMKyUTG4A94XHhrY`</summary>

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
  "parentUuid": "581e5641-82d3-493d-8805-615ee2465482",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "ef446b36-1578-4f83-9246-4b77d375bbd2",
  "sourceToolAssistantUUID": "581e5641-82d3-493d-8805-615ee2465482",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T12:47:02.476Z_



Let me read the paper and all relevant project files thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef446b36-1578-4f83-9246-4b77d375bbd2",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nw8brNDE65d7y89CXQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a1ba6c4-f3f3-446f-a657-00d9d711b816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vxEZEmxR5sHo4SNozp8fF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-15T12:47:02.983Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018xg4EGQLR5K3MY3kvvNS7i`</summary>

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
  "parentUuid": "2a1ba6c4-f3f3-446f-a657-00d9d711b816",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nw8brNDE65d7y89CXQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dfedddb-8144-43b4-9183-ae5f4636dd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vxEZEmxR5sHo4SNozp8fF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 15888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-15T12:47:03.265Z_

<details><summary>↩ Tool result · `toolu_018xg4EGQLR5K3MY3kvvNS7i`</summary>

```text
{"result":"# 项目 faith-evidence-ie 概况\n\n## 实验状态 (74 个)\n\n- **mvp2_sft_eval_r2**: DONE (success) — \n- **mvp2_sft_eval**: DONE (killed) — \n- **mvp2_grpo_flatnli_r2**: DONE (killed) — \n- **mvp2_grpo_extract_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r4**: DONE (killed) — \n- **mvp2_grpo_extract**: DONE (failed) — \n- **mvp2_grpo_flatnli**: DONE (failed) — \n- **mvp2_grpo_ced_r3**: DONE (failed) — \n- **mvp2_grpo_ced_r2**: DONE (killed) — \n- **mvp2_grpo_ced_r1**: DONE (killed) — \n- **mvp2_grpo_ced**: DONE (failed) — \n- **precompute_nli_train**: DONE (success) — \n- **mvp2_sft_warmup**: DONE (success) — \n- **smoke_test_grpo**: DONE (success) — \n- **mvp1_ced_signal**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp2_rsft_ced_scoring_topk3_r2 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). | — | — | — |\n| mvp2_rsft_ced_scoring_topk3 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality? | — | — | — |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\n\n## 待处理\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\n\n## 近期结论\n- **mvp2_rsft_diagnosis** (success): RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\n- **mvp2_eval_ced_kl001_r4_last** (killed): —\n- **mvp2_grpo_ced_kl001_r3** (killed): kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping) ← 基于 mvp2_grpo_ced_kl001\n\n## 趋势\n成功 21 / 负向 11 / 失败 12 / 共 64\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- mvp2_grpo_ced: 训练失败 — unknown\n- mvp2_grpo_flatnli: 训练失败 — unknown\n- mvp2_grpo_extract: 训练失败 — unknown\n- mvp2_sft_eval: 已被终止 — unknown\n- mvp2_grpo_ced_r1: 已被终止 — unknown\n- mvp2_grpo_ced_r2: 已被终止 — unknown\n- mvp2_grpo_ced_r3: 训练失败 — unknown\n- mvp2_grpo_ced_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\n- mvp2_grpo_extract_r4: 已被终止 — unknown\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\n- mvp2_rsft_generate: 训练失败 — unknown\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\n- mvp2_eval_rsft_\n\n## 研究想法\n# Idea Inbox\n\n## 待验证\n\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\n## ACTIVE"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dfedddb-8144-43b4-9183-ae5f4636dd74",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "f4dbb770-3ab4-462f-8e49-eccb9e48c712",
  "sourceToolAssistantUUID": "8dfedddb-8144-43b4-9183-ae5f4636dd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T12:47:06.572Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CjyYLjcX2RjSj66AXjNQTG`</summary>

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
  "parentUuid": "f4dbb770-3ab4-462f-8e49-eccb9e48c712",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NwRkjMZyNbVC2TTyVo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "667edffc-c648-4dc7-877e-bc02d4cde5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYqaZyJQooWttugnJJa1wa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 10 · 2026-05-15T12:47:06.592Z_

<details><summary>↩ Tool result · `toolu_01CjyYLjcX2RjSj66AXjNQTG`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.tex
artifacts/dream_reports/dream_20260515T120227/median/paper.tex
artifacts/dream_reports/dream_20260515T120227/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "667edffc-c648-4dc7-877e-bc02d4cde5d8",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "61a96e46-1887-4cb1-842e-8397624359c4",
  "sourceToolAssistantUUID": "667edffc-c648-4dc7-877e-bc02d4cde5d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T12:47:07.510Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018XSiAmruD49kB5Z5NyZmQC`</summary>

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
  "parentUuid": "61a96e46-1887-4cb1-842e-8397624359c4",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NwRkjMZyNbVC2TTyVo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86eaf72f-9717-45b0-9957-3f99a8f80cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYqaZyJQooWttugnJJa1wa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2442,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 53,
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

_source line 12 · 2026-05-15T12:47:07.524Z_

<details><summary>↩ Tool result · `toolu_018XSiAmruD49kB5Z5NyZmQC`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/paper.pdf
artifacts/dream_reports/dream_20260515T120227/median/paper.pdf
artifacts/dream_reports/dream_20260515T120227/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86eaf72f-9717-45b0-9957-3f99a8f80cb5",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "69c6ff6b-ccb6-4168-bd8d-8d6bc649d8d7",
  "sourceToolAssistantUUID": "86eaf72f-9717-45b0-9957-3f99a8f80cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T12:47:08.021Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AGotrppKSuR7d1f6c9ad9W`</summary>

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
  "parentUuid": "69c6ff6b-ccb6-4168-bd8d-8d6bc649d8d7",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NwRkjMZyNbVC2TTyVo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b246ac01-17d2-4dec-8382-a0fe816066cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYqaZyJQooWttugnJJa1wa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2442,
      "cache_read_input_tokens": 17336,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2442
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 17336,
          "cache_creation_input_tokens": 2442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2442,
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

_source line 14 · 2026-05-15T12:47:08.031Z_

<details><summary>↩ Tool result · `toolu_01AGotrppKSuR7d1f6c9ad9W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp2_rsft_ced_scoring_topk3_r2 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). | — | — | — |\\n| mvp2_rsft_ced_scoring_topk3 | CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality? | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n\\n## 待处理\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_rsft_diagnosis** (success): RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\\n- **mvp2_eval_ced_kl001_r4_last** (killed): —\\n- **mvp2_grpo_ced_kl001_r3** (killed): kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping) ← 基于 mvp2_grpo_ced_kl001\\n\\n## 趋势\\n成功 21 / 负向 11 / 失败 12 / 共 64\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n\", \"total_chars\": 3020, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b246ac01-17d2-4dec-8382-a0fe816066cb",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "3ce5ea07-9e43-44fb-9afb-91f63287e14b",
  "sourceToolAssistantUUID": "b246ac01-17d2-4dec-8382-a0fe816066cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T12:47:11.199Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QDK2VzepUQYLm3Yj5z1bee`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ce5ea07-9e43-44fb-9afb-91f63287e14b",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NwnKV7tbiwzZMUhfjL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a450cbc0-e66b-4f3e-93cc-c950dd8a565c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyT4apt3hicLC1BwSuHdSD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2220,
      "cache_read_input_tokens": 19778,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2220
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 19778,
          "cache_creation_input_tokens": 2220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2220,
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

_source line 16 · 2026-05-15T12:47:11.467Z_

<details><summary>↩ Tool result · `toolu_01QDK2VzepUQYLm3Yj5z1bee`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{hyperref}
12	\usepackage{natbib}
13	\usepackage{caption}
14	\usepackage{subcaption}
15	\usepackage{enumitem}
16	
17	\newcommand{\method}{FREIGE}
18	\newcommand{\ced}{CED}
19	\newcommand{\edcr}{EDCR}
20	\newcommand{\rsft}{RSFT}
21	
22	\title{FREIGE: Faithful Relation Extraction with Evidence via\\Contrastive Evidence Discrimination}
23	
24	\author{Anonymous}
25	\date{}
26	
27	\begin{document}
28	\maketitle
29	
30	% ============================================================
31	% ABSTRACT
32	% ============================================================
33	\begin{abstract}
34	LLM-based document-level relation extraction (DocRE) approaches extraction parity with encoder models but produces no verifiable evidence for predicted relations, limiting deployment in audit-critical domains.
35	We present \method{}, the first LLM-based DocRE system that jointly generates relation triples and supporting evidence sentences.
36	Our key contribution is \emph{Contrastive Evidence Discrimination} (\ced{}), a scoring function that contrasts genuine evidence against entity-sharing distractor sentences within the same document, converting a binary NLI signal into a contrastive margin that is robust to lexical-overlap bias.
37	We show that \ced{} as an online RL reward (GRPO) leads to catastrophic forgetting of extraction ability---reward rises monotonically while relation F1 collapses to near zero---constituting, to our knowledge, the first empirical demonstration of reward overoptimization in structured information extraction.
38	Instead, using \ced{} as an offline quality filter for \emph{Rejection Sampling Fine-Tuning} (\rsft{}) yields consistent gains: on the DocRED test set, \method{} achieves rel-F1 45.4 and Evi-F1 80.2, surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3) under comparable evaluation.
39	We further propose the \emph{Entity-sharing Distractor Citation Rate} (\edcr{}), a complementary metric exposing a blind spot of Evi-F1: high Evi-F1 can coexist with substantial distractor citation.
40	Experiments across three model scales (1.7B/4B/8B) and two datasets (DocRED, Re-DocRED) confirm the generality of the approach.
41	\end{abstract}
42	
43	% ============================================================
44	% 1  INTRODUCTION
45	% ============================================================
46	\section{Introduction}
47	
48	Document-level relation extraction (DocRE) identifies relational facts between entity pairs scattered across multiple sentences. Recent encoder-based methods such as DREEAM and SAIS achieve strong extraction F1 and additionally produce evidence---the sentences supporting each predicted triple. However, these systems derive evidence from attention patterns or auxiliary classifiers, not from the extraction model's own reasoning.
49	
50	Large language models (LLMs) fine-tuned for DocRE have closed the extraction gap with encoder models, yet \emph{no existing LLM-based method produces verifiable evidence}. This is a critical deployment gap: in biomedical knowledge base population, legal document analysis, and RAG-based fact verification, practitioners need to trace each extracted fact back to its textual support.
51	
52	A natural idea is to reward the LLM for producing faithful evidence using an NLI-based faithfulness score. We find, however, that a \emph{flat} NLI reward is easily gamed by \textbf{entity-sharing distractor sentences}---sentences that mention the same entities as the gold evidence but do not actually support the relation. Such sentences receive high entailment scores from NLI models, creating a reward signal that conflates entity co-occurrence with genuine evidential support.
53	
54	We propose \textbf{Contrastive Evidence Discrimination (\ced{})}, which addresses this by computing a contrastive margin: $m = p_\text{pos} - p_\text{neg}$, where $p_\text{pos}$ is the NLI entailment probability for the gold evidence and $p_\text{neg}$ is that for the highest-scoring distractor. This margin is inherently robust to lexical-overlap bias because the bias affects both terms and partially cancels in the difference.
55	
56	A second finding is that \ced{} as an \emph{online} RL reward (via GRPO) catastrophically fails: the model learns to produce NLI-friendly evidence while completely forgetting how to extract relations (rel-F1 drops from 40.6 to $<$2 within 10 training steps, while reward increases monotonically). This is, to our knowledge, the first empirical demonstration of reward overoptimization in structured IE, echoing theoretical predictions from the reward overoptimization literature.
57	
58	Our solution is to use \ced{} \emph{offline}: the SFT model generates $N$ candidate outputs per document, \ced{} scores them, and only the top-$k$ candidates are retained for a second round of supervised fine-tuning (\rsft{}). This sidesteps catastrophic forgetting entirely because no policy gradient update occurs---the model simply sees higher-quality training data.
59	
60	We make four contributions:
61	\begin{enumerate}[nosep,leftmargin=*]
62	\item \textbf{\method{}}: the first LLM-based DocRE method that jointly outputs relation triples and verifiable evidence, achieving rel-F1 45.4 and Evi-F1 80.2 on DocRED test.
63	\item \textbf{\ced{} as offline quality signal}: contrastive NLI scoring for RSFT data filtering significantly outperforms flat-NLI filtering (Evi-F1 +2.6pp, EDCR $-$5.8pp on dev).
64	\item \textbf{Cautionary analysis of online RL for structured IE}: GRPO with three reward types all catastrophically forget, providing empirical grounding for when to prefer offline over online RL.
65	\item \textbf{\edcr{} metric}: a complementary evaluation dimension revealing that high Evi-F1 can coexist with substantial distractor citation (Pearson $r = -0.42$ between Evi-F1 and EDCR).
66	\end{enumerate}
67	
68	% ============================================================
69	% 2  RELATED WORK
70	% ============================================================
71	\section{Related Work}
72	
73	\paragraph{Document-Level Relation Extraction.}
74	DocRE requires reasoning across sentences to extract relations between entity pairs. Encoder-based methods dominate the DocRED leaderboard: ATLOP uses adaptive thresholding, DocuNet introduces a U-shaped network, and DREEAM adds evidence-aware attention training. SAIS improves evidence extraction via a separate evidence module. Recent LLM-based approaches (e.g., LMRC with LLaMA3.1-8B, DocKS-RAG with GNN augmentation) achieve competitive extraction F1 but produce no evidence.
75	
76	\paragraph{Faithfulness and Evidence in IE.}
77	The faithfulness of generated text has been extensively studied in summarization and question answering, typically via NLI-based evaluation. For relation extraction, evidence serves a complementary role: rather than verifying output fidelity, it provides provenance for extracted facts. Evi-F1, the standard metric, measures sentence-level overlap with gold evidence but does not penalize plausible-looking distractor citations.
78	
79	\paragraph{RL for Language Models.}
80	RLHF and its variants (DPO, GRPO, KTO) have shown success in aligning LLMs with human preferences. However, reward overoptimization---where the proxy reward increases while true quality degrades---remains a known failure mode. Our work provides the first empirical evidence of this phenomenon in structured information extraction.
81	
82	\paragraph{Rejection Sampling Fine-Tuning.}
83	RSFT (also called ReST or iterative DPO) generates candidates from the current policy, filters by a quality signal, and fine-tunes on the filtered set. Recent theoretical work shows RSFT is equivalent to PPO under certain conditions. We adopt RSFT with CED as the quality filter.
84	
85	% ============================================================
86	% 3  METHOD
87	% ============================================================
88	\section{Method}
89	
90	\subsection{Problem Formulation}
91	
92	Given a document $D$ with annotated entities, the task is to produce for each entity pair $(h, t)$ a set of relation triples $(h, r, t)$ along with evidence sentences $E \subseteq \{S_1, \ldots, S_{|D|}\}$ that support the relation. We formulate this as sequence generation: the LLM outputs structured text encoding triples and their evidence sentence indices.
93	
94	\subsection{SFT Baseline}
95	
96	We fine-tune Qwen3-4B with LoRA on DocRED training data, where the target sequence encodes each triple as \texttt{(head, relation, tail, [S$_i$, S$_j$, ...])}. The model learns to jointly predict relations and cite evidence sentences.
97	
98	\subsection{Contrastive Evidence Discrimination (\ced{})}
99	\label{sec:ced}
100	
101	For a predicted triple $(h, r, t)$ with cited evidence sentences $E_\text{pred}$, we define:
102	
103	\paragraph{Positive score.} Let the NLI model compute the entailment probability $p_\text{pos} = P(\text{entail} \mid \text{premise}=E_\text{pred},\; \text{hypothesis}=(h, r, t))$.
104	
105	\paragraph{Negative score.} We construct a distractor set: all sentences in $D$ that mention either $h$ or $t$ but are \emph{not} in the gold evidence set. The negative score is $p_\text{neg} = \max_{S_d \in \text{Distractor}} P(\text{entail} \mid S_d, (h, r, t))$.
106	
107	\paragraph{CED margin.} The contrastive margin is:
108	\begin{equation}
109	m_\text{CED} = p_\text{pos} - p_\text{neg}
110	\end{equation}
111	
112	A high margin indicates the cited evidence is genuinely more supportive than the best available distractor. The contrastive design provides two key properties:
113	\begin{enumerate}[nosep,leftmargin=*]
114	\item \textbf{Bias cancellation}: lexical-overlap bias in the NLI model affects both $p_\text{pos}$ and $p_\text{neg}$ similarly (both involve entity-mentioning sentences), so the bias partially cancels in the margin.
115	\item \textbf{Self-correction for annotation noise}: if a ``distractor'' is actually valid evidence missed by annotators, it will have high $p_\text{neg}$, reducing the margin and thus the penalty---the scoring is lenient toward false distractors.
116	\end{enumerate}
117	
118	We use DeBERTa-v3-base fine-tuned on MNLI as the NLI model. The CED scorer achieves discrimination accuracy of 81.5\% (correctly ranking gold evidence above the best distractor) with mean margin 0.48.
119	
120	\subsection{Rejection Sampling Fine-Tuning (\rsft{})}
121	\label{sec:rsft}
122	
123	\begin{enumerate}[nosep,leftmargin=*]
124	\item \textbf{Candidate generation}: For each training document, sample $N=8$ outputs from the SFT model (temperature 0.7).
125	\item \textbf{CED scoring}: Score each candidate's evidence quality using the CED margin.
126	\item \textbf{Filtering}: Retain top-$k$ candidates (default $k=1$) per document, yielding ${\sim}2{,}700$ high-quality training examples from ${\sim}21{,}000$ candidates (selection rate 12.8\%).
127	\item \textbf{Fine-tuning}: Train a second LoRA adapter on the filtered set (1 epoch, $\alpha$=128, lr=$2\times10^{-5}$).
128	\end{enumerate}
129	
130	This pipeline avoids the catastrophic forgetting of online RL: no policy gradient is computed, so the model's extraction ability is preserved while evidence quality improves through data curation.
131	
132	\subsection{Entity-sharing Distractor Citation Rate (\edcr{})}
133	\label{sec:edcr}
134	
135	Standard Evi-F1 measures sentence-level overlap with gold evidence but does not specifically penalize \emph{plausible-looking} distractor citations. We define:
136	
137	\begin{equation}
138	\text{EDCR} = \frac{|\{s \in E_\text{pred} : s \notin E_\text{gold} \wedge s \text{ mentions } h \text{ or } t\}|}{|E_\text{pred}|}
139	\end{equation}
140	
141	EDCR captures the fraction of cited sentences that share entities with the target triple but are not gold evidence---precisely the failure mode that flat NLI rewards encourage. Lower EDCR indicates more precise evidence.
142	
143	\subsection{Why Online RL Fails: GRPO Analysis}
144	
145	We attempted GRPO training with three reward types: (1)~CED margin, (2)~flat-NLI entailment, (3)~extraction-only F1. All three configurations, across multiple learning rates and KL penalties, exhibited the same failure pattern: the reward increases monotonically while relation F1 collapses within the first 10--30 steps. This constitutes reward overoptimization in the structured IE setting: the model discovers degenerate policies (e.g., citing all entity-mentioning sentences) that maximize the reward proxy while destroying extraction capability.
146	
147	% ============================================================
148	% 4  EXPERIMENTAL SETUP
149	% ============================================================
150	\section{Experimental Setup}
151	
152	\paragraph{Datasets.} We evaluate on DocRED (3,053 train / 1,000 dev / 1,000 test documents) and Re-DocRED (a revised version correcting false-negative annotations).
153	
154	\paragraph{Models.} Our primary model is Qwen3-4B with LoRA ($\alpha$=128, $r$=64). We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.
155	
156	\paragraph{Baselines.}
157	(1)~\textbf{SFT}: Qwen3-4B fine-tuned on DocRED gold data.
158	(2)~\textbf{RSFT flat-NLI}: RSFT with flat NLI scoring (non-contrastive).
159	(3)~\textbf{DREEAM}: RoBERTa-large encoder, evidence SOTA (test Evi-F1 57.34).
160	(4)~\textbf{SAIS}: RoBERTa encoder evidence baseline (test Evi-F1 55.67).
161	(5)~\textbf{CED reranker}: inference-time CED reranking of SFT candidates ($N$=8), no additional training.
162	(6)~\textbf{GRPO+CED}: online RL with CED reward (negative baseline).
163	
164	\paragraph{Metrics.} Relation F1 (rel-F1), Ign-F1 (excluding shared training-test triples), Evidence F1 (Evi-F1, sentence-level), and EDCR (Section~\ref{sec:edcr}). Test rel-F1/ign-F1 from CodaLab; Evi-F1 and EDCR computed locally.
165	
166	\paragraph{NLI Model.} DeBERTa-v3-base fine-tuned on MNLI for CED scoring. We additionally ablate DeBERTa-v3-large.
167	
168	% ============================================================
169	% 5  RESULTS
170	% ============================================================
171	\section{Results}
172	
173	\subsection{Main Results on DocRED Test Set}
174	
175	Table~\ref{tab:test} presents the main results. \method{} (RSFT+CED) achieves rel-F1 45.4 and Evi-F1 80.2 on the DocRED test set. While the rel-F1 gap to encoder SOTA (DREEAM, 63.3) reflects the known trade-off of generative approaches, the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable sentence-level evaluation. The dev-to-test decay is small: $-$1.2pp for rel-F1 and $-$0.7pp for Evi-F1, indicating robust generalization.
176	
177	\begin{table}[t]
178	\centering
179	\caption{DocRED test set results. $\dagger$: encoder-based methods; Evi-F1 comparison requires noting the protocol difference (attention-based vs.\ generative evidence).}
180	\label{tab:test}
181	\begin{tabular}{lcccc}
182	\toprule
183	\textbf{Method} & \textbf{rel-F1} & \textbf{ign-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
184	\midrule
185	DREEAM$\dagger$ & 63.3 & --- & 57.3 & --- \\
186	SAIS$\dagger$ & 62.3 & --- & 55.7 & --- \\
187	\midrule
188	SFT baseline & 39.7 & 39.5 & 78.9 & 70.5 \\
189	RSFT flat-NLI & 42.9 & 42.7 & 78.5 & 68.6 \\
190	\textbf{RSFT+CED (ours)} & \textbf{45.4} & \textbf{45.2} & \textbf{80.2} & \textbf{54.8} \\
191	\bottomrule
192	\end{tabular}
193	\end{table}
194	
195	The EDCR of 54.8 on the test set indicates that roughly half of the cited non-gold sentences are entity-sharing distractors---a substantial improvement over SFT (70.5) but indicating remaining room for improvement. Flat-NLI RSFT achieves only marginal EDCR improvement (68.6), confirming that contrastive scoring is essential for distractor filtering.
196	
197	\subsection{CED vs.\ Flat-NLI Ablation}
198	
199	Table~\ref{tab:ced_vs_flatnli} compares CED-scored and flat-NLI-scored RSFT on the dev set. CED RSFT outperforms flat-NLI RSFT across all metrics: +2.8pp rel-F1, +2.6pp Evi-F1, and $-$5.8pp EDCR. The flat-NLI RSFT provides only marginal EDCR improvement over SFT ($-$1.9pp), confirming that non-contrastive NLI scoring has little discriminative power against entity-sharing distractors.
200	
201	\begin{table}[t]
202	\centering
203	\caption{CED vs.\ flat-NLI RSFT ablation on DocRED dev set. All CED configurations outperform flat-NLI.}
204	\label{tab:ced_vs_flatnli}
205	\begin{tabular}{lccccc}
206	\toprule
207	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & $\Delta$\textbf{Evi-F1} & $\Delta$\textbf{EDCR} \\
208	\midrule
209	SFT baseline & 40.6 & 79.8 & 71.2 & --- & --- \\
210	RSFT flat-NLI & 43.8 & 79.3 & 69.3 & $-$0.5 & $-$1.9 \\
211	RSFT CED (r1) & 44.5 & 81.9 & 65.7 & +2.1 & $-$5.5 \\
212	RSFT CED (s44) & 46.6 & 80.9 & 63.5 & +1.1 & $-$7.7 \\
213	RSFT CED (r2b) & 44.9 & 81.3 & 66.1 & +1.5 & $-$5.1 \\
214	\bottomrule
215	\end{tabular}
216	\end{table}
217	
218	The mechanism is clear: flat-NLI scoring assigns high scores to entity-sharing distractors (both genuine evidence and distractors contain the target entities and thus receive high NLI entailment scores). CED's contrastive margin $m = p_\text{pos} - p_\text{neg}$ explicitly penalizes candidates whose evidence is not substantially more supportive than the best distractor, filtering out distractor-heavy training examples.
219	
220	\subsection{EDCR Diagnostic Across Methods}
221	
222	Table~\ref{tab:edcr_diag} presents EDCR computed across all evidence-producing methods, revealing the diagnostic power of EDCR as a complementary metric to Evi-F1.
223	
224	\begin{table}[t]
225	\centering
226	\caption{EDCR diagnostic across all methods (dev set). EDCR and Evi-F1 capture different dimensions (Pearson $r = -0.42$).}
227	\label{tab:edcr_diag}
228	\begin{tabular}{lcccc}
229	\toprule
230	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Evidence pattern} \\
231	\midrule
232	SFT & 40.6 & 79.8 & 71.2 & High distractor \\
233	RSFT flat-NLI & 43.8 & 79.3 & 69.3 & Slightly improved \\
234	RSFT CED (best) & 46.6 & 80.9 & 63.5 & Notably improved \\
235	CED reranker & 39.8 & 80.5 & 49.8 & Most precise \\
236	GRPO CED (ckpt-90) & 21.1 & 56.7 & 85.8 & Catastrophic distractor \\
237	\bottomrule
238	\end{tabular}
239	\end{table}
240	
241	Three observations stand out. First, GRPO's best checkpoint achieves Evi-F1 of 56.7 (seemingly reasonable) but EDCR of 85.8---nearly all citations are distractors. This is a case where Evi-F1 alone would mask a catastrophic failure mode. Second, the CED reranker achieves the lowest EDCR (49.8) among all methods, at the cost of 8$\times$ inference overhead, demonstrating that CED directly filters distractors at inference time. Third, the Pearson correlation between Evi-F1 and EDCR is only $-0.42$, confirming they capture orthogonal evaluation dimensions.
242	
243	\subsection{DREEAM Baseline Reproduction}
244	
245	To ensure evaluation comparability, we reproduce DREEAM (RoBERTa-large) on the DocRED dev set (Table~\ref{tab:dreeam_repro}). The reproduction gap is $<$0.3pp for both rel-F1 and Evi-F1, confirming pipeline consistency.
246	
247	\begin{table}[h]
248	\centering
249	\caption{DREEAM reproduction on DocRED dev set.}
250	\label{tab:dreeam_repro}
251	\begin{tabular}{lccc}
252	\toprule
253	\textbf{Setting} & \textbf{Paper} & \textbf{Reproduced} & \textbf{Gap} \\
254	\midrule
255	Dev rel-F1 & $\sim$62.9 & 62.7 & $-$0.2 \\
256	Dev Evi-F1 & $\sim$57.2 & 57.0 & $-$0.2 \\
257	Test Evi-F1 & 57.3 & (submitted) & --- \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	We note an important protocol difference: DREEAM extracts evidence via attention thresholds (precision 58.1, recall 55.9), while our method generates explicit sentence indices (precision 81.2, recall 79.3). The generative approach naturally has higher recall because the model can cite any number of sentences. Despite this difference, the sentence-level F1 evaluation protocol is identical, making the comparison valid at the metric level.
263	
264	\subsection{CED as Inference-Time Reranker}
265	
266	Table~\ref{tab:reranker} shows results for using CED as a training-free reranker: we sample $N$=8 candidates from SFT and select the one with the highest CED margin.
267	
268	\begin{table}[t]
269	\centering
270	\caption{CED reranker vs.\ baselines (dev set). The reranker achieves the best EDCR without any additional training.}
271	\label{tab:reranker}
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Extra training} \\
275	\midrule
276	SFT baseline & 40.6 & 79.8 & 71.2 & --- \\
277	CED reranker & 39.8 & 80.5 & 49.8 & None \\
278	RSFT+CED & 46.6 & 80.9 & 63.5 & $\sim$2h LoRA \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	The reranker achieves EDCR 49.8 (the best across all methods) with no training cost, at 8$\times$ inference overhead. The rel-F1 drops slightly ($-$0.8pp) because CED selects for evidence quality rather than extraction quality. This provides a complementary pathway: for applications where evidence precision is paramount (e.g., biomedical audit), the reranker is preferable; for balanced performance, RSFT+CED is superior.
284	
285	\subsection{GRPO Catastrophic Forgetting}
286	
287	Table~\ref{tab:grpo} traces the GRPO training trajectory, revealing the reward overoptimization pattern. Within 10 steps, rel-F1 collapses from 40.6 (SFT initialization) to 0.3, while the CED reward increases from 0.45 to 1.195 over 100 steps. Meanwhile, Evi-F1 climbs to 85.0---the model has learned to produce evidence that the NLI model finds entailing, but has completely forgotten how to extract relations.
288	
289	\begin{table}[t]
290	\centering
291	\caption{GRPO trajectory (CED reward, lr=$5\times10^{-6}$). Reward rises while rel-F1 stays near zero---classic reward overoptimization.}
292	\label{tab:grpo}
293	\begin{tabular}{lcccc}
294	\toprule
295	\textbf{Checkpoint} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} & \textbf{Reward} \\
296	\midrule
297	SFT (init) & 40.6 & 79.8 & 71.2 & --- \\
298	step-10 & 0.3 & 72.0 & 99.8 & 0.45 \\
299	step-20 & 0.8 & 62.8 & 99.4 & 0.62 \\
300	step-40 & 0.7 & 75.8 & 99.4 & 0.78 \\
301	step-60 & 0.9 & 81.0 & 99.3 & 0.91 \\
302	step-80 & 1.2 & 82.8 & 99.3 & 1.05 \\
303	step-100 & 1.4 & 85.0 & 98.8 & 1.20 \\
304	\midrule
305	GRPO (KL=0.01, ckpt-90) & 21.1 & 56.7 & 85.8 & --- \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	Adding KL regularization (KL=0.01) partially mitigates the collapse (rel-F1 recovers to 21.1) but remains far below SFT (40.6), and EDCR worsens to 85.8. Flat-NLI and extraction-only rewards collapse even earlier (steps 25--30). This comprehensive failure across reward types and hyperparameters motivates RSFT as the principled alternative: use CED's discriminative signal without the instability of online policy gradient updates.
311	
312	\subsection{Model Size Ablation}
313	
314	Table~\ref{tab:model_size} shows that RSFT+CED yields consistent improvements across three model scales.
315	
316	\begin{table}[t]
317	\centering
318	\caption{Model size ablation on DocRED dev set. RSFT+CED improves consistently across scales.}
319	\label{tab:model_size}
320	\begin{tabular}{lccccc}
321	\toprule
322	\textbf{Model} & \textbf{SFT rel-F1} & \textbf{RSFT rel-F1} & $\Delta$ & \textbf{RSFT Evi-F1} & \textbf{EDCR} \\
323	\midrule
324	Qwen3-1.7B & 34.2 & 37.8 & +3.6 & 77.6 & 68.2 \\
325	Qwen3-4B & 40.6 & 46.6 & +6.0 & 81.9 & 63.5 \\
326	Qwen3-8B & 44.8 & 49.2 & +4.4 & 83.5 & 58.8 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	The improvement ranges from +3.6pp (1.7B) to +6.0pp (4B) in rel-F1 and +1.7--2.1pp in Evi-F1. Larger models benefit more from CED filtering (EDCR improves from 68.2 to 58.8 as scale increases), suggesting they better exploit the higher-quality training data. The 8B model achieves the highest Evi-F1 (83.5), indicating scaling potential for future work with larger models.
332	
333	\subsection{Re-DocRED Extension}
334	
335	Table~\ref{tab:redocred} evaluates on Re-DocRED, which corrects false-negative annotations in DocRED. All methods show higher rel-F1 (because previously correct predictions are no longer penalized as false positives). RSFT+CED maintains its advantage: +4.6pp rel-F1 and +1.9pp Evi-F1 over SFT.
336	
337	\begin{table}[t]
338	\centering
339	\caption{DocRED vs.\ Re-DocRED comparison (dev set).}
340	\label{tab:redocred}
341	\begin{tabular}{llccc}
342	\toprule
343	\textbf{Dataset} & \textbf{Method} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
344	\midrule
345	DocRED & SFT & 40.6 & 79.8 & 71.2 \\
346	DocRED & RSFT+CED & 46.6 & 81.9 & 63.5 \\
347	\midrule
348	Re-DocRED & SFT & 47.2 & 81.2 & 64.8 \\
349	Re-DocRED & RSFT+CED & 51.8 & 83.1 & 57.8 \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	EDCR on Re-DocRED (57.8) is lower than on DocRED (63.5), as expected: with more complete gold annotations, fewer genuinely supportive sentences are misclassified as distractors. The consistent improvement across both datasets addresses the single-dataset generalization concern.
355	
356	\subsection{Top-$k$ Ablation}
357	
358	Table~\ref{tab:topk} compares $k$=1 (strict filtering, ${\sim}2{,}700$ samples, mean CED=0.668) vs.\ $k$=3 (relaxed, ${\sim}8{,}100$ samples, mean CED=0.542).
359	
360	\begin{table}[h]
361	\centering
362	\caption{Top-$k$ ablation for CED-scored RSFT (dev set).}
363	\label{tab:topk}
364	\begin{tabular}{lccccc}
365	\toprule
366	\textbf{top-$k$} & \textbf{Samples} & \textbf{Mean CED} & \textbf{rel-F1} & \textbf{Evi-F1} & \textbf{EDCR} \\
367	\midrule
368	1 & 2,718 & 0.668 & 46.6 & 80.9 & 63.5 \\
369	3 & $\sim$8,100 & 0.542 & 45.8 & 80.4 & 65.2 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	Top-$k$=1 is slightly superior (+0.8pp rel-F1, +0.5pp Evi-F1, $-$1.7pp EDCR), suggesting that data quality outweighs data quantity in this regime. However, both settings substantially outperform SFT, indicating that CED's top-ranked candidates are consistently high-quality.
375	
376	\subsection{NLI Model Ablation}
377	
378	Table~\ref{tab:nli_ablation} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.
379	
380	\begin{table}[h]
381	\centering
382	\caption{NLI model ablation for CED scoring. DeBERTa-base is sufficient.}
383	\label{tab:nli_ablation}
384	\begin{tabular}{lccccc}
385	\toprule
386	\textbf{NLI Model} & \textbf{CED margin} & \textbf{Disc.\ acc} & \textbf{Pearson $r$} & \textbf{Evi-F1} & \textbf{EDCR} \\
387	\midrule
388	DeBERTa-v3-base & 0.480 & 81.5 & 0.34 & 80.9 & 63.5 \\
389	DeBERTa-v3-large & 0.523 & 84.9 & 0.28 & 81.5 & 61.8 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	DeBERTa-large achieves marginally better discrimination accuracy (+3.4pp) and lower lexical-overlap correlation (Pearson $r$ 0.28 vs.\ 0.34), but downstream RSFT improvements are modest (+0.6pp Evi-F1, $-$1.7pp EDCR). The contrastive design of CED inherently reduces sensitivity to NLI model strength: lexical-overlap bias partially cancels in the margin computation. DeBERTa-base is sufficient for practical use, keeping the scoring pipeline lightweight.
395	
396	% ============================================================
397	% 6  DISCUSSION
398	% ============================================================
399	\section{Discussion}
400	
401	\paragraph{Evaluation Protocol Differences.}
402	The Evi-F1 comparison between \method{} (80.2) and DREEAM (57.3) requires careful interpretation. DREEAM extracts evidence via attention thresholds, producing precision-oriented but recall-limited evidence. Our generative approach produces explicit sentence citations with naturally higher recall (79.3 vs.\ 55.9). While the sentence-level F1 computation is identical, the evidence generation mechanism differs fundamentally. We recommend future work develop protocol-normalized metrics for cross-paradigm comparison.
403	
404	\paragraph{EDCR Limitations.}
405	EDCR captures only one type of evidence error (entity-sharing distractors) and may miss other failure modes such as temporally irrelevant evidence or topically adjacent but relationally incorrect citations. Additionally, EDCR depends on the completeness of gold evidence annotations---in Re-DocRED, EDCR is lower partly because annotations are more complete.
406	
407	\paragraph{Why RSFT Over Online RL.}
408	Our GRPO analysis demonstrates a specific failure mode: reward overoptimization in structured IE, where the model exploits the reward proxy (NLI entailment) via degenerate strategies (citing all entity-mentioning sentences) while abandoning the primary task (relation extraction). RSFT sidesteps this by never updating the policy with a reward gradient---it simply curates better training data. This suggests that for complex structured generation tasks where reward design is inherently imperfect, offline approaches may be systematically preferable.
409	
410	\paragraph{Remaining Challenges.}
411	The rel-F1 gap between LLM-based methods (${\sim}$45--49) and encoder SOTA (${\sim}$63) remains substantial. Closing this gap while maintaining evidence generation is an important direction. Additionally, EDCR of 54.8 on test indicates that roughly half of non-gold citations are still distractors, suggesting further improvements in evidence precision are needed.
412	
413	% ============================================================
414	% 7  CONCLUSION
415	% ============================================================
416	\section{Conclusion}
417	
418	We presented \method{}, the first LLM-based document-level relation extraction system that jointly generates relation triples and verifiable evidence. Our approach introduces Contrastive Evidence Discrimination (CED), a scoring function that converts NLI-based faithfulness assessment into a contrastive signal robust to entity-sharing distractor sentences. We demonstrated that CED fails catastrophically as an online RL reward (GRPO) but succeeds as an offline quality filter for rejection sampling fine-tuning (RSFT), providing an empirical cautionary tale for reward design in structured IE.
419	
420	On DocRED, \method{} achieves Evi-F1 80.2, substantially surpassing the encoder evidence SOTA (57.3), while improving extraction F1 by 5.7pp over the SFT baseline. The proposed EDCR metric reveals a blind spot of Evi-F1 where high coverage coexists with substantial distractor citation. Experiments across three model scales and two datasets confirm the generality of the approach. We hope this work encourages the community to treat evidence generation as a first-class output in document-level IE.
421	
422	\bibliographystyle{acl_natbib}
423	
424	\end{document}
425	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a450cbc0-e66b-4f3e-93cc-c950dd8a565c",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "8e22f954-7f47-408c-82e4-b19d59acd000",
  "sourceToolAssistantUUID": "a450cbc0-e66b-4f3e-93cc-c950dd8a565c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T12:47:14.806Z_

Now let me read the other paper versions and relevant project files for deeper understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e22f954-7f47-408c-82e4-b19d59acd000",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nx2uKwQVV9dHi5F3cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5caf5028-efd4-4e78-aaad-946a130204ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo2h2HyBtnk83aQwpQfZRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10791,
      "cache_read_input_tokens": 21998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10791,
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

_source line 18 · 2026-05-15T12:47:15.827Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01KqGE4FtEwn4MMnR9hGmzeW`</summary>

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
  "parentUuid": "5caf5028-efd4-4e78-aaad-946a130204ba",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nx2uKwQVV9dHi5F3cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9766d04b-10f4-403f-bd18-d31cc286f26a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo2h2HyBtnk83aQwpQfZRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10791,
      "cache_read_input_tokens": 21998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10791,
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

_source line 19 · 2026-05-15T12:47:15.838Z_

<details><summary>↩ Tool result · `toolu_01KqGE4FtEwn4MMnR9hGmzeW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP (MVP-1 + MVP-2 均 PASS，进入 Research 阶段)\\n> **最后更新**: 2026-05-15\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Stretch: ARR May 25 (10 days, 极紧，仅在实验全部顺利时考虑)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。朴素 NLI faithfulness reward 可被 entity-mentioning distractor 句子游戏——共享实体但不支持具体关系的句子仍获正面蕴含分数。\\n\\n**CED (Contrastive Evidence Discrimination)** 通过文档内 hard negative 对比，将 evidence 质量评估从\\\"是否蕴含\\\"升级为\\\"是否比最佳干扰句更蕴含\\\"——本质上是 evidence grounding 场景下的 **anti-reward-overoptimization mechanism**（连接 Gao et al. 2023 reward overoptimization 理论）。\\n\\n**MVP 关键发现**: CED 作为在线 RL (GRPO) reward 导致 catastrophic forgetting（3 种 reward type × 多个 lr 全线失败），但作为离线 RL (RSFT) 的候选筛选信号极其有效——4 组超参配置均稳定超过 SFT baseline。**方法论结论**: 对结构化 IE 任务，CED 应作为离线质量信号而非在线训练奖励。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍（human-in-the-loop KB population、生物医学审计、RAG 溯源）\\n2. **Why naive reward fails**: flat-NLI 被 entity-sharing distractors 欺骗（SFT EDCR=71.2%，大量引用干扰句）\\n3. **Why online RL fails**: GRPO+CED/flat-NLI/extract-only 全部 catastrophic forgetting（reward ↑ + rel_f1 ↓ 至 <0.02）\\n4. **Solution**: CED 作为离线质量信号 + RSFT（rejection sampling fine-tuning）：SFT 模型生成 N 候选 → CED 打分筛选 → 微调，规避在线 RL 的遗忘风险\\n5. **Theoretical grounding**: 连接 LongRLVR (ICLR 2026) evidence grounding 梯度消失分析 + \\\"RSFT=PPO\\\" (ICML 2025) 等价性理论\\n6. **Result**: 首个 LLM-based DocRE 方法同时生成抽取和可验证证据\\n\\n## Core Claims\\n\\n### Claim 1 (Main): CED-scored RSFT 使 LLM 同时生成抽取和忠实证据\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT+CED: rel_f1 +3.9~6.0pp over SFT, evi_f1 +1.1~2.1pp, EDCR -4.8~7.7pp\\n- **MVP-2 已验证**: 4/4 configs PASS\\n- **Research 需要**: test set 评估，DREEAM/SAIS Evi-F1 直接对比\\n\\n### Claim 2 (Ablation): CED scoring 优于 flat-NLI scoring 用于 RSFT\\n- CED-filtered RSFT vs flat-NLI-filtered RSFT 的 evi_f1 和 EDCR 差异\\n- CED 的对比性 margin 过滤掉 distractor-heavy 候选\\n- **Research 需要**: flat-NLI scored RSFT ablation（核心实验）\\n\\n### Claim 3 (Analysis): 在线 RL 在结构化 IE 上 catastrophically forget\\n- GRPO+QLoRA 在 3 种 reward type × 多个 lr 下全线失败\\n- 关键对比: evi_f1 在 GRPO 下提升至 0.850（>SFT 0.798）但 rel_f1 崩至 <0.02——CED 驱动了 evidence 学习但在线 RL 摧毁了抽取能力\\n- RSFT 规避此问题：不修改 policy gradient，只筛选训练数据\\n- **MVP 已有完整证据**: D031/D033 GRPO 判死，D039 RSFT 成功\\n\\n### Claim 4 (Evaluation): EDCR 作为独立评估指标\\n- EDCR = |entity-sharing non-gold cited sentences| / |total cited sentences|\\n- Evi-F1 盲区：不惩罚 plausible-looking distractor citations\\n- SFT EDCR=71.2%, RSFT+CED EDCR=63.5~66.4%（方向正确但差距有限，需坦诚讨论）\\n- **Research 需要**: cross-method diagnostic table, CED vs flat-NLI EDCR 对比\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | 状态 |\\n|--------|--------|----------|--------|------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | ✅ |\\n| RSFT r1 (3ep, α=128, s42) | 0.4449 | +3.92pp | 0.8187 | 0.6565 | ✅ |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.6350 | ✅ |\\n| RSFT r2a (1ep, α=128) | 0.4494 | +4.37pp | 0.8108 | 0.6641 | ✅ |\\n| RSFT r2b (1ep, α=32, lr=1e-5) | 0.4493 | +4.36pp | 0.8128 | 0.6609 | ✅ |\\n| GRPO best (lr=5e-5, ckpt-90) | 0.2110 | -19.5pp | 0.5750 | — | ❌ |\\n| GRPO best (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | 0.9900 | ❌ |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: NLI reward 信号质量（高概率攻击）\\n- **攻击**: \\\"DeBERTa-v3-base 的 NLI 判断有 lexical overlap bias，CED 训练信号有噪声\\\"\\n- **已验证**: MVP-1 Pearson r=0.34（NLI vs lexical overlap），远低于 0.7，证明非捷径\\n- **Research 补充**: DeBERTa-base vs DeBERTa-large 对比\\n\\n### RC2: Gold evidence 标注不完整导致 false distractor\\n- **攻击**: \\\"被标为 distractor 的句子可能是 annotator 遗漏的有效证据\\\"\\n- **应对**: CED margin 的 self-correcting property——如果 false distractor 真正蕴含关系，其 p_neg 高 → margin 小 → 惩罚弱\\n- **Research 补充**: false-distractor 鲁棒性量化分析\\n\\n### RC3: 评测可比性\\n- **攻击**: \\\"生成式 evidence 如何与 DREEAM 的 attention-based evidence 做 apple-to-apple 对比？\\\"\\n- **应对**: 模型输出显式句子索引 [S_i]，直接映射句子级 Evi-F1；辅助指标用 RoBERTa-large-MNLI（非训练用 DeBERTa）避免 circular evaluation\\n\\n### RC4: 单数据集 + 单模型泛化性\\n- **攻击**: \\\"只在 DocRED + Qwen3-4B 上验证\\\"\\n- **Research**: Re-DocRED 扩展 + Qwen3-1.7B/8B model size ablation\\n\\n### RC5: RSFT vs GRPO 是否公平对比\\n- **攻击**: \\\"GRPO 失败可能是超参问题而非方法论问题\\\"\\n- **应对**: 完整 GRPO 轨迹——3 种 reward × 多个 lr × 全 checkpoint eval；D020 控制变量下 CED 是唯一存活的 reward type\\n\\n### RC6: EDCR 63-66% 仍然偏高，CED 对证据精确度提升有限\\n- **攻击**: \\\"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著\\\"\\n- **应对**: (1) CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward；(2) CED-as-reranker 可能更直接降低 EDCR；(3) 需要 flat-NLI RSFT 对比证明 CED 方向正确\\n- **Research**: CED reranker PoC（运行中），top_k ablation\\n\\n### RC7: 方法过于简单\\n- **应对**: 简洁是优点——RSFT 方法论已被证明理论等价于 PPO (ICML 2025)，CED 创新在于打分函数设计而非框架复杂度\\n\\n## Key Baselines (8+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT on DocRED gold — 无 RL\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT — 无 contrastive signal（核心 ablation）\\n3. **RSFT CED (FREIGE)**: CED scored RSFT — 主方法\\n4. **CED-as-reranker**: 推理时 CED 重排 SFT 候选（无训练）— 运行中\\n5. **GRPO+CED**: 在线 RL with CED reward — negative baseline\\n6. **DREEAM**: RoBERTa-large encoder — evidence SOTA (Evi-F1 57.34)\\n7. **SAIS**: RoBERTa encoder — evidence baseline (Evi-F1 55.67)\\n8. **DocKS-RAG**: GNN+RAG — extraction SOTA (F1 63.59, 无 evidence)\\n9. **LMRC**: LLaMA3.1-8B — generative LLM SOTA (F1 60.69, 无 evidence)\\n\\n## Publishability Threshold\\n\\n- **必要条件**: RSFT+CED 在 test set 上 Evi-F1 > DREEAM 57.34 AND rel_f1 显著 > SFT baseline\\n- **充分条件**: 上述 + CED vs flat-NLI RSFT Evi-F1/EDCR 差异显著 + GRPO 分析完整\\n- **Failure pivot**: Evi-F1 < 57.34 on test set → 转为 analysis contribution（在线 vs 离线 RL for structured IE）\\n\\n## Research Phase Priorities\\n\\n| Priority | 实验 | Claim | 预估 GPU-hours |\\n|----------|------|-------|---------------|\\n| P0 | CED vs flat-NLI RSFT ablation | C2 | ~20h |\\n| P0 | Test set evaluation (RSFT best config) | C1 | ~4h |\\n| P0 | EDCR pipeline 验证 + cross-method table | C4 | ~2h |\\n| P0 | DREEAM/SAIS Evi-F1 baseline reproduction | C1 | ~8h |\\n| P1 | CED-as-reranker (running) | C1 bonus | ~6h |\\n| P1 | Model size ablation (1.7B/8B) | RC4 | ~24h |\\n| P1 | Re-DocRED extension | RC4 | ~12h |\\n| P1 | top_k ablation (k=1 vs k=3) | RC6 | ~8h |\\n| P2 | GRPO forgetting 详细分析 + 可视化 | C3 | ~4h |\\n| P2 | DeBERTa-base vs large NLI 对比 | RC1 | ~4h |\\n\", \"total_chars\": 6099, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9766d04b-10f4-403f-bd18-d31cc286f26a",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "aa806ae5-bb6f-4575-b1d3-d2fa08487337",
  "sourceToolAssistantUUID": "9766d04b-10f4-403f-bd18-d31cc286f26a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T12:47:16.774Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HsFAp4XrD4M9CAieXTTi5o`</summary>

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
  "parentUuid": "aa806ae5-bb6f-4575-b1d3-d2fa08487337",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nx2uKwQVV9dHi5F3cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1460dd5e-3c09-4820-93f1-d1a34fa762e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo2h2HyBtnk83aQwpQfZRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10791,
      "cache_read_input_tokens": 21998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10791,
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

_source line 21 · 2026-05-15T12:47:16.786Z_

<details><summary>↩ Tool result · `toolu_01HsFAp4XrD4M9CAieXTTi5o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n\", \"total_chars\": 28970, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1460dd5e-3c09-4820-93f1-d1a34fa762e7",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "d395d350-4c5a-4d6d-89df-0c4e5b3d7b97",
  "sourceToolAssistantUUID": "1460dd5e-3c09-4820-93f1-d1a34fa762e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T12:47:17.211Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Vg19MEp4whVNn1uEB7L6h7`</summary>

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
  "parentUuid": "d395d350-4c5a-4d6d-89df-0c4e5b3d7b97",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nx2uKwQVV9dHi5F3cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4401e9d7-46e7-4c27-b600-4b58127bde7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo2h2HyBtnk83aQwpQfZRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10791,
      "cache_read_input_tokens": 21998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10791,
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

_source line 23 · 2026-05-15T12:47:17.220Z_

<details><summary>↩ Tool result · `toolu_01Vg19MEp4whVNn1uEB7L6h7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4401e9d7-46e7-4c27-b600-4b58127bde7a",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "6cd0649c-7b3a-46bb-95ac-3905d85bf4ea",
  "sourceToolAssistantUUID": "4401e9d7-46e7-4c27-b600-4b58127bde7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T12:47:17.879Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012efGtJ2DTzLC4NVNzonniu`</summary>

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
  "parentUuid": "6cd0649c-7b3a-46bb-95ac-3905d85bf4ea",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nx2uKwQVV9dHi5F3cg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8600c00-0158-4009-8bae-4415d5014170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo2h2HyBtnk83aQwpQfZRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10791,
      "cache_read_input_tokens": 21998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10791,
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

_source line 25 · 2026-05-15T12:47:17.888Z_

<details><summary>↩ Tool result · `toolu_012efGtJ2DTzLC4NVNzonniu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\n## ACTIVE\\n\", \"total_chars\": 484, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8600c00-0158-4009-8bae-4415d5014170",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "dc8d4c29-cb69-4d1a-8168-0a5ca008ed58",
  "sourceToolAssistantUUID": "e8600c00-0158-4009-8bae-4415d5014170",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T12:47:21.211Z_

Now let me read the experiment plan and the memory file for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc8d4c29-cb69-4d1a-8168-0a5ca008ed58",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NxWr6ChfxY9HFxnHhb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c4121dd-da07-4c38-8dbc-9a3c33e20600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhbAacpekc7c6gX8jeZ47S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22071,
      "cache_read_input_tokens": 32789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22071,
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

_source line 27 · 2026-05-15T12:47:22.216Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011MtttV2u6GoPP9ieF9xvA1`</summary>

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
  "parentUuid": "2c4121dd-da07-4c38-8dbc-9a3c33e20600",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NxWr6ChfxY9HFxnHhb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ff8ee9e-7bbe-4495-af02-aa8dd79df346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhbAacpekc7c6gX8jeZ47S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22071,
      "cache_read_input_tokens": 32789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22071,
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

_source line 28 · 2026-05-15T12:47:22.230Z_

<details><summary>↩ Tool result · `toolu_011MtttV2u6GoPP9ieF9xvA1`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## D038 重大修正：RSFT r1 实际成功 (2026-05-15)\\n\\n### 事件\\nD037 报告 RSFT r1 \\\"灾难性失败\\\"（rel_f1=0.0483），但这是 **TaskEvalCallback bug**——`--eval_max_docs 50` 评估 50 个 doc 的预测，却用全部 12275 个 gold triples 计算 F1，严重低估 rel_f1。\\n\\n### 真实结果\\ns44 全量 dev eval (985 docs): **rel_f1=0.4655 (+5.98pp), evi_f1=0.8087 (+1.08pp)** → MVP-2 PASS\\n\\n### TaskEvalCallback bug fix\\n已部署到 `rsft_trainer.py:118-120`。gold triples 现在过滤到 eval_max_docs 对应的文档子集。\\n\\n### 教训\\n- 在 callback 中用 subset eval 时，必须确保 gold 和 pred 在同一文档集合上计算\\n- 基于 callback 数字的任何结论都需要全量 eval 交叉验证\\n\\n---\\n\\n## ~~RSFT r1 灾难性失败根因~~ [D038 撤回]\\n\\n**以下分析基于 D037 的错误 rel_f1=0.0483。D038 确认该数字是 eval bug，实际 rel_f1=0.4655。**\\n\\n原分析中关于\\\"关系本体崩塌\\\"的观察可能来自 eval_max_docs=50 下的极小样本偏差，不代表模型真实行为。r1/s43/s44 的全量 eval 正在进行中，将给出真实 ablation 数据。\\n\\n---\\n\\n## RSFT r2a/r2b ablation 结果 (2026-05-15)\\n\\n### 实验配置与结果\\n\\n| 配置 | rel_f1 | evi_f1 | edcr | Δrel_f1 |\\n|------|--------|--------|------|---------|\\n| SFT baseline | 0.4057 | 0.7979 | 0.7118 | — |\\n| r1 (3ep, α=128, lr=2e-5, 2718) | 0.4449 | **0.8187** | 0.6565 | +3.92pp |\\n| r2a (1ep, α=128, lr=2e-5, clean 2548) | **0.4494** | 0.8108 | 0.6641 | +4.37pp |\\n| r2b (1ep, α=32, lr=1e-5, clean 2548) | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\\n\\n### Ablation 结论\\n1. **1 epoch ≈ 3 epoch on rel_f1**（r2a=0.4494 vs r1=0.4449），多 epoch 无额外收益\\n2. **LoRA scaling 不敏感**（α=128 vs α=32 差异 <0.1pp）\\n3. **r1 在 evi_f1 上最优**（0.8187 vs r2a 0.8108），3 epoch 可能有助于证据定位\\n4. **所有 RSFT 变体 EDCR 低于 SFT**（~0.66 vs 0.71），RSFT 增加 pred_count 导致更多 distractor citation\\n\\n---\\n\\n## RSFT 文献对标 (2026-05-15, 更新)\\n\\n### 直接竞争者：无\\n在 DocRE / IE 上**无人用过 RSFT**，NLI-based CED reward for RE training 也无先例。Novelty 完全成立。\\n\\n### 最接近竞争者：R1-RE (arXiv 2507.04642)\\n用 GRPO 做**句子级** RE。与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无。\\n\\n### Must-cite 论文\\n1. **R1-RE** — GRPO for sentence-level RE（最近竞争者，需在 related work 中区分）\\n2. **\\\"Minimalist Approach\\\"** — RSFT 理论基础\\n3. **RelPrior** — LLM-based DocRE baseline (+2.06-2.38pp rel_f1)\\n4. **\\\"RSFT=PPO\\\" (ICML 2025)** — RSFT 与 PPO 等价性理论\\n\\n### 我们的定位\\n- +3.9~6.0pp rel_f1 显著超过同类 LLM-based DocRE 改进（RelPrior: +2.06-2.38pp）\\n- CED 作为 rejection sampling 打分函数是新颖的方法论贡献\\n- 最接近的工作是 Progressive Self-distillation (ACM 2024) 用 knowledge distillation，但无 evidence-based reward\\n\\n### 新增文献 map categories (by literature scan worker)\\n- Category 6: RSFT Methodology & Theory（3 篇）\\n- Category 7: RL for Information Extraction（5 篇）\\n- Category 8: Recent LLM-based DocRE Methods（5 篇）\\n\\n---\\n\\n## CED-as-reranker 探索 (2026-05-15)\\n\\nRSFT 成功后仍保留 CED-as-reranker PoC 作为推理时替代方案（无需额外训练）。\\ncuda:0 上 PID 178050 运行中（985 docs × N=8，预计 ~6h）。\\n如果 reranker 接近或超过 RSFT，可作为论文中的 complementary contribution。\\n\\n---\\n\\n## Qwen3 generation_config 覆盖陷阱 (2026-05-15)\\n\\nQwen3 模型自带 `generation_config.json` 会静默覆盖代码传参：\\n- `model.generation_config.top_k = 20`（限制采样池）\\n- `model.generation_config.temperature = 0.6`（覆盖代码传的任何温度值）\\n\\n**必须在生成前显式覆盖**：\\n```python\\nmodel.generation_config.temperature = target_temp\\nmodel.generation_config.top_k = 0  # 禁用 top_k 限制\\nmodel.generation_config.do_sample = True\\n```\\n\\n---\\n\\n## Diversity 监控计算 bug (2026-05-15)\\n\\n### 根因\\n- triple-set 归一化逻辑不一致\\n- diversity 分母用配置值而非实际生成数\\n\\n### 修复\\n- 提取 `diversity_metrics.py` 独立模块\\n- 修复后真实数据：302 docs mean_diversity=7.52/8, median=8.0/8\\n\\n---\\n\\n## inference.py 参数教训 (2026-05-15)\\n\\n**inference.py 必须传完整模型 stack**：\\n- `--base_model /root/autodl-tmp/models/Qwen3-4B`\\n- `--sft_adapter /root/autodl-tmp/sft_output`\\n- `--model_path &lt;rsft_adapter_path>`（RSFT adapter）\\n- `--data_path /root/autodl-tmp/data/docred`\\n- `--output_dir &lt;output_path>`\\n- `--no-quantize`（RTX 5090 必须）\\n- `--max_new_tokens &lt;N>`（可选，默认 1024）\\n\\n**只传 --model_path 不传 --base_model + --sft_adapter 会导致模型 stack 错误**（Base + RSFT LoRA，缺 SFT merge），结果完全不可用。maxtok1536 eval 因此被 Reviewer CRITICAL 打回并重跑。\\n\\n---\\n\\n## RSFT 代码参数速查\\n\\n**inference.py**: --base_model, --sft_adapter, --model_path(rsft adapter), --data_path, --output_dir, --no-quantize, --max_new_tokens(1024)\\n\\n**rsft_generate.py**: --base_model, --sft_adapter, --data_path, --split, --output_dir, --num_generations(8), --temperature(0.7), --batch_size(1), --max_new_tokens(1024), --seed, --quantize/--no-quantize, --start_idx, --end_idx, --shard_id\\n\\n**rsft_score_filter.py**: --input_dir, --output_path, --nli_model_path, --nli_device, --tau(0.5), --f1_threshold(0.1), --selection_strategy(top_k), --top_k(2)\\n\\n**rsft_trainer.py**: --base_model, --sft_adapter, --rsft_data_path, --output_dir, --learning_rate, --num_epochs, --per_device_batch_size, --gradient_accumulation_steps, --lora_rank(64), --lora_alpha(128), --weighted_sampling, --quantize(False), --eval_data_dir, --eval_max_docs, --wandb_run_name, --seed\", \"total_chars\": 6195, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ff8ee9e-7bbe-4495-af02-aa8dd79df346",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "c31a2f83-1a2b-46ff-8438-8e3c45f75cfe",
  "sourceToolAssistantUUID": "6ff8ee9e-7bbe-4495-af02-aa8dd79df346",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T12:47:22.577Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VxobfMq65Y8wP49ZuaHgKU`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c31a2f83-1a2b-46ff-8438-8e3c45f75cfe",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NxWr6ChfxY9HFxnHhb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5f5450c-4037-4cf1-af37-9dcd54847145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhbAacpekc7c6gX8jeZ47S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22071,
      "cache_read_input_tokens": 32789,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 32789,
          "cache_creation_input_tokens": 22071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22071,
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

_source line 30 · 2026-05-15T12:47:22.585Z_

<details><summary>↩ Tool result · `toolu_01VxobfMq65Y8wP49ZuaHgKU`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_provenance.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5f5450c-4037-4cf1-af37-9dcd54847145",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "57aaa9a7-c041-451a-9ce3-6052a72289e9",
  "sourceToolAssistantUUID": "a5f5450c-4037-4cf1-af37-9dcd54847145",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-15T12:47:25.934Z_

Now let me also read the median and worst paper versions to understand the range of the dream simulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57aaa9a7-c041-451a-9ce3-6052a72289e9",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NxrZFwFZA9w39VnCnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7950c2a8-b3fc-448b-8117-a13b2244bcac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5doY2FfzTuDeZY4wi5Bwq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 54860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4275,
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

_source line 32 · 2026-05-15T12:47:27.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CAf7psmtHeM4fPqJ7ALCWC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7950c2a8-b3fc-448b-8117-a13b2244bcac",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NxrZFwFZA9w39VnCnH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed90166a-2425-4efa-a83c-560b26f88516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5doY2FfzTuDeZY4wi5Bwq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4275,
      "cache_read_input_tokens": 54860,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 54860,
          "cache_creation_input_tokens": 4275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4275,
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

_source line 33 · 2026-05-15T12:47:27.735Z_

<details><summary>↩ Tool result · `toolu_01CAf7psmtHeM4fPqJ7ALCWC`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{multirow}
9	\usepackage{graphicx}
10	\usepackage{xcolor}
11	\usepackage{soul}
12	\usepackage{hyperref}
13	\usepackage{enumitem}
14	
15	\newcommand{\method}{FREIGE}
16	\newcommand{\ced}{CED}
17	\newcommand{\edcr}{EDCR}
18	
19	\title{FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction\\via Contrastive Evidence Discrimination}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	LLM-based document-level relation extraction (DocRE) approaches extraction performance competitive with encoder models, yet no existing method generates verifiable evidence sentences alongside extracted relations. We present \method{}, the first LLM framework for DocRE that jointly produces relation triples and grounded evidence. Our approach introduces Contrastive Evidence Discrimination (\ced{}), a scoring function that evaluates evidence quality by contrasting gold-supporting sentences against entity-sharing distractors within the same document. We find that \ced{} is effective as an offline quality signal for Rejection Sampling Fine-Tuning (RSFT) but leads to catastrophic forgetting when used as an online RL (GRPO) reward---a finding we systematically document across three reward types and multiple hyperparameter configurations. On DocRED, \method{} achieves an evidence F1 of 78.9\% on the test set, competitive with a relation F1 of 42.8\%, while reducing entity-sharing distractor citations (EDCR) by 5--8 percentage points over the SFT baseline. We further propose the Entity-sharing Distractor Citation Rate (\edcr{}) as a complementary evaluation metric that captures a failure mode invisible to standard evidence F1. Experiments across three model sizes (1.7B--8B) and two datasets (DocRED, Re-DocRED) confirm the consistency of our approach.
28	\end{abstract}
29	
30	\section{Introduction}
31	
32	Document-level relation extraction (DocRE) requires identifying relations between entity pairs that may span multiple sentences in a document \cite{yao2019docred}. While encoder-based methods have achieved strong extraction performance \cite{zhou2021atlop,tan2022dreeam}, and recent LLM-based approaches show competitive results \cite{xu2024lmrc}, none produce verifiable evidence---the specific sentences supporting each extracted relation.
33	
34	Evidence grounding is critical for deploying DocRE in high-stakes domains: human-in-the-loop knowledge base population, biomedical literature curation, and retrieval-augmented generation all require traceability from extracted facts to source text. Without evidence, users cannot verify whether an extraction reflects genuine textual support or a spurious entity co-occurrence.
35	
36	A natural approach to encouraging faithful evidence is to use Natural Language Inference (NLI) as a reward signal during reinforcement learning. However, we identify a fundamental limitation: flat NLI scoring is systematically deceived by \emph{entity-sharing distractors}---sentences that mention the head or tail entity but do not support the specific relation. Such sentences receive high NLI entailment scores because they share key entities with the claim, yet they provide no genuine evidential support.
37	
38	We propose \textbf{Contrastive Evidence Discrimination (\ced{})}, which addresses this limitation by computing a margin between the NLI score for a candidate evidence sentence and the maximum NLI score among entity-sharing distractor sentences from the same document. This contrastive formulation shifts the evaluation from ``does this sentence entail the claim?'' to ``does this sentence entail the claim \emph{better than the best distractor}?''
39	
40	A central finding of our work is that \ced{} is effective as an \emph{offline} quality signal but fails as an \emph{online} RL reward. When used as a GRPO reward, \ced{} drives evidence F1 upward (to 85.0\%) but causes catastrophic forgetting of relation extraction capability (rel\_F1 collapses to $<$2\%). This failure is systematic: we observe it across three reward types (CED, flat-NLI, extraction-only), multiple learning rates, and with KL constraints. In contrast, \ced{} as an offline signal for RSFT---where it filters training candidates rather than directly shaping gradients---yields consistent improvements across all metrics.
41	
42	Our contributions are:
43	\begin{enumerate}
44	    \item \method{}, the first LLM-based DocRE framework that jointly generates relation triples and evidence sentences, achieving competitive extraction and evidence quality on DocRED.
45	    \item Contrastive Evidence Discrimination (\ced{}), a scoring function that provides consistent improvement over flat-NLI scoring for evidence quality, functioning as a composable module applicable at both training and inference time.
46	    \item A systematic analysis of online vs.\ offline RL for structured IE, documenting catastrophic forgetting in GRPO and connecting it to the evidence grounding gradient vanishing phenomenon described in LongRLVR.
47	    \item \edcr{}, a diagnostic metric for entity-sharing distractor citations, with analysis revealing its correlation with relation type characteristics.
48	\end{enumerate}
49	
50	\section{Related Work}
51	
52	\paragraph{Document-Level Relation Extraction.}
53	DocRED \cite{yao2019docred} established the benchmark for document-level RE with evidence annotations. Encoder-based methods achieve strong extraction F1: ATLOP \cite{zhou2021atlop} (63.4\%), DocuNet \cite{zhang2021docunet} (64.6\%). For evidence, DREEAM \cite{tan2022dreeam} uses attention supervision to achieve evidence F1 of 57.34\%, and SAIS \cite{xiao2022sais} reaches 55.67\%. However, these methods treat evidence as attention weights rather than explicit outputs. Recent LLM approaches---LMRC \cite{xu2024lmrc} (60.69\% F1 with LLaMA3.1-8B) and DocKS-RAG \cite{docks2025} (63.59\% with GNN+RAG)---improve extraction but produce no evidence.
54	
55	\paragraph{RL for Language Model Alignment.}
56	RLHF and its variants \cite{ouyang2022training,rafailov2023direct} align LLMs with human preferences. For structured tasks, Group Relative Policy Optimization (GRPO) \cite{shao2024deepseekmath} and Rejection Sampling Fine-Tuning (RSFT) \cite{yuan2024rrhf} offer complementary paradigms. The theoretical equivalence between RSFT and PPO under certain conditions \cite{tang2024rsftppo} motivates using offline approaches when online RL is unstable. LongRLVR \cite{song2026longrlvr} provides theoretical analysis of evidence grounding gradient vanishing in long-context RL.
57	
58	\paragraph{Faithfulness Evaluation.}
59	NLI-based faithfulness metrics \cite{honovich2022true,laban2022summac} assess whether generated text is entailed by source documents. However, document-level IE poses unique challenges: entity-sharing distractors receive high entailment scores despite not supporting the specific relation, a failure mode not addressed by existing metrics.
60	
61	\section{Method}
62	
63	\subsection{Task Formulation}
64	
65	Given a document $D = \{s_1, s_2, \ldots, s_n\}$ consisting of $n$ sentences with annotated entity mentions, the task is to generate a set of relation tuples $\{(h_i, r_i, t_i, E_i)\}$ where $h_i$ is the head entity, $r_i$ is the relation type, $t_i$ is the tail entity, and $E_i \subseteq \{s_1, \ldots, s_n\}$ is the set of evidence sentences supporting the relation.
66	
67	We formulate this as a sequence-to-sequence task where an LLM generates structured output containing relation triples with explicit sentence indices as evidence markers.
68	
69	\subsection{SFT Baseline}
70	
71	We fine-tune Qwen3-4B with LoRA \cite{hu2022lora} on DocRED training data, where each training example maps a document to its gold relation triples with evidence annotations. The output format is:
72	\begin{quote}
73	\texttt{(head; relation; tail; [S$_i$, S$_j$, ...])}
74	\end{quote}
75	where \texttt{S$_i$} denotes the $i$-th sentence in the document.
76	
77	\subsection{Contrastive Evidence Discrimination (CED)}
78	
79	For a candidate output containing a relation triple $(h, r, t)$ with cited evidence sentences $E = \{e_1, \ldots, e_k\}$, we construct the evaluation as follows.
80	
81	\paragraph{Claim Construction.} We form a natural language claim $c = $ ``\texttt{[h] [r\_verbalized] [t]}'' from the relation triple.
82	
83	\paragraph{Positive and Negative Sets.} For each cited sentence $e_i \in E$:
84	\begin{itemize}
85	    \item \textbf{Positive score}: $p_{\text{pos}}(e_i) = \text{NLI}_{\text{entail}}(e_i, c)$, the entailment probability from a pre-trained NLI model (DeBERTa-v3-base fine-tuned on MNLI).
86	    \item \textbf{Negative set}: $N_i = \{s \in D \setminus E \mid s \text{ mentions } h \text{ or } t\}$---all non-cited sentences that share entities with the triple.
87	    \item \textbf{Maximum negative score}: $p_{\text{neg}}^*(e_i) = \max_{s \in N_i} \text{NLI}_{\text{entail}}(s, c)$.
88	\end{itemize}
89	
90	\paragraph{CED Score.} The CED score for a candidate is:
91	\begin{equation}
92	    \text{CED} = \frac{1}{|E|} \sum_{e_i \in E} \left[ p_{\text{pos}}(e_i) - p_{\text{neg}}^*(e_i) \right]
93	\end{equation}
94	
95	A high CED score indicates that cited evidence sentences are more strongly entailing than the best entity-sharing distractors. Unlike flat NLI scoring ($\max_i p_{\text{pos}}(e_i)$), CED explicitly penalizes candidates whose evidence is no more informative than distractor sentences.
96	
97	\subsection{Rejection Sampling Fine-Tuning (RSFT)}
98	
99	We apply CED as an offline quality signal for RSFT:
100	
101	\begin{enumerate}
102	    \item \textbf{Candidate Generation}: The SFT model generates $N=8$ candidate outputs per training document (21,952 candidates total).
103	    \item \textbf{CED Scoring}: Each candidate is scored with CED.
104	    \item \textbf{Selection}: The top-$k$ candidate per document (default $k{=}1$) is selected, yielding 2,718 high-quality training examples.
105	    \item \textbf{Fine-Tuning}: The SFT model is further fine-tuned on the selected examples with LoRA ($\alpha{=}32$, lr$=10^{-5}$, 1 epoch).
106	\end{enumerate}
107	
108	\subsection{CED as Inference-Time Reranker}
109	
110	CED can also be applied at inference time without additional training. Given $N$ candidate outputs from the SFT model, we select the candidate with the highest CED score. This provides a training-free approach to reducing distractor citations at the cost of increased inference time ($\sim$8$\times$).
111	
112	\subsection{Entity-Sharing Distractor Citation Rate (EDCR)}
113	
114	We propose EDCR as a complementary metric to evidence F1:
115	\begin{equation}
116	    \text{EDCR} = \frac{|\{s \in C \setminus G \mid s \text{ mentions } h \text{ or } t\}|}{|C|}
117	\end{equation}
118	where $C$ is the set of all cited sentences and $G$ is the gold evidence set. EDCR measures the proportion of citations that are entity-sharing distractors---sentences that mention relevant entities but do not support the specific relation. Standard evidence F1 treats all false positive citations equally; EDCR specifically quantifies the most deceptive type of error.
119	
120	\section{Experiments}
121	
122	\subsection{Setup}
123	
124	\paragraph{Dataset.} We evaluate on DocRED \cite{yao2019docred} (3,053 train / 1,000 dev / 1,000 test documents, 96 relation types) and Re-DocRED \cite{tan2022redocred}, a revised version with corrected annotations.
125	
126	\paragraph{Models.} Our primary model is Qwen3-4B with LoRA fine-tuning. We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.
127	
128	\paragraph{Baselines.} We compare against: (1)~SFT baseline (Qwen3-4B LoRA, no RL); (2)~RSFT with flat-NLI scoring; (3)~GRPO with CED/flat-NLI/extraction-only rewards; (4)~DREEAM \cite{tan2022dreeam} (encoder, evidence SOTA); (5)~SAIS \cite{xiao2022sais} (encoder, evidence baseline).
129	
130	\paragraph{Metrics.} Relation F1 (rel\_F1), Ign\_F1 (excluding training relational facts), Evidence F1 (evi\_F1), and EDCR (lower is better).
131	
132	\paragraph{CED Configuration.} NLI model: DeBERTa-v3-base fine-tuned on MNLI. Discrimination accuracy on gold vs.\ distractor pairs: 81.5\%.
133	
134	\subsection{Main Results}
135	
136	Table~\ref{tab:main} presents the test set results. \method{} (RSFT+CED) achieves test rel\_F1 of 42.8--43.8\% and evi\_F1 of 78.3--78.9\%, representing a +4.2pp rel\_F1 and +1.4pp evi\_F1 improvement over the SFT baseline.
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\begin{tabular}{lcccc}
142	\toprule
143	\textbf{Method} & \textbf{rel\_F1} & \textbf{ign\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
144	\midrule
145	SFT baseline & 38.6 & 37.8 & 77.5 & 69.5 \\
146	RSFT flat-NLI & 42.0 & --- & 77.6 & 66.8 \\
147	RSFT CED (r2b) & 42.8 & 42.0 & 78.9 & 63.8 \\
148	RSFT CED (s44) & 43.8 & 42.9 & 78.3 & 62.0 \\
149	\midrule
150	DREEAM$^\dagger$ & --- & --- & 57.3 & --- \\
151	SAIS$^\dagger$ & --- & --- & 55.7 & --- \\
152	\bottomrule
153	\end{tabular}
154	\caption{Test set results on DocRED. $^\dagger$Encoder-based methods using attention-based evidence extraction (see \S\ref{sec:protocol} for evaluation protocol discussion). EDCR computed on dev set (test evidence labels unavailable for EDCR computation). Two RSFT+CED configurations are reported: r2b (1 epoch, $\alpha{=}32$) and s44 (3 epochs, $\alpha{=}128$, seed 44).}
155	\label{tab:main}
156	\end{table}
157	
158	The evi\_F1 gap between \method{} and encoder baselines (78.9\% vs.\ 57.3\% for DREEAM) is substantial but requires careful interpretation due to evaluation protocol differences (\S\ref{sec:protocol}). The ign\_F1 values closely track rel\_F1 ($<$1pp difference), indicating that RSFT does not overfit to training-set relation co-occurrences.
159	
160	\paragraph{Dev$\to$Test Generalization.}
161	Table~\ref{tab:devtest} shows the generalization gap. The rel\_F1 drop of 2.1--2.8pp is consistent with the SFT baseline (2.0pp) and within the expected range for DocRED. The s44 configuration (3 epochs) shows slightly larger degradation, suggesting mild dev-set overfitting compared to the 1-epoch r2b configuration.
162	
163	\begin{table}[t]
164	\centering
165	\small
166	\begin{tabular}{lcccc}
167	\toprule
168	\textbf{Config} & \textbf{dev} & \textbf{test} & $\Delta$\textbf{rel\_F1} & $\Delta$\textbf{evi\_F1} \\
169	\midrule
170	SFT & 40.6 / 79.8 & 38.6 / 77.5 & $-$2.0 & $-$2.3 \\
171	r2b & 44.9 / 81.3 & 42.8 / 78.9 & $-$2.1 & $-$2.4 \\
172	s44 & 46.6 / 80.9 & 43.8 / 78.3 & $-$2.8 & $-$2.6 \\
173	\bottomrule
174	\end{tabular}
175	\caption{Dev$\to$test generalization gap (rel\_F1 / evi\_F1).}
176	\label{tab:devtest}
177	\end{table}
178	
179	\subsection{CED vs.\ Flat-NLI Scoring (Claim 2)}
180	\label{sec:ced_vs_nli}
181	
182	Table~\ref{tab:ced_nli} compares CED and flat-NLI as RSFT scoring functions in an apple-to-apple ablation: both use the same candidate pool (21,952 generations), same selection threshold ($k{=}1$), and same RSFT hyperparameters.
183	
184	\begin{table}[t]
185	\centering
186	\small
187	\begin{tabular}{llccccc}
188	\toprule
189	\textbf{Method} & \textbf{Scoring} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
190	\midrule
191	SFT & --- & 40.6 & 79.8 & 71.2 \\
192	RSFT & flat-NLI & 44.2 & 79.9 & 68.5 \\
193	RSFT & CED & 44.9 & 81.3 & 66.1 \\
194	\midrule
195	\multicolumn{2}{l}{$\Delta$ (CED $-$ flat-NLI)} & +0.7 & +1.4 & $-$2.4 \\
196	\bottomrule
197	\end{tabular}
198	\caption{CED vs.\ flat-NLI RSFT ablation (dev set). CED provides consistent improvement across all three metrics.}
199	\label{tab:ced_nli}
200	\end{table}
201	
202	CED scoring improves over flat-NLI on all three dimensions: rel\_F1 (+0.7pp), evi\_F1 (+1.4pp), and EDCR ($-$2.4pp). The critical observation is that flat-NLI RSFT achieves virtually no evi\_F1 improvement over SFT (+0.1pp), while CED RSFT achieves +1.5pp. This reveals that flat-NLI scoring fails to discriminate evidence quality: it filters out candidates with globally low NLI scores but cannot distinguish entity-sharing distractors from genuine evidence, since both receive high entailment scores. CED's contrastive margin directly addresses this blind spot.
203	
204	\subsection{CED as Inference-Time Reranker}
205	
206	Table~\ref{tab:reranker} evaluates CED as a reranker applied at inference time. CED reranking of SFT outputs (no additional training) achieves the largest EDCR reduction ($-$10.7pp), demonstrating CED's direct value as a quality signal. Combining RSFT+CED training with CED reranking further reduces EDCR to 58.5\% while maintaining rel\_F1 and evi\_F1.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\begin{tabular}{lcccc}
212	\toprule
213	\textbf{Method} & \textbf{Train?} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
214	\midrule
215	SFT & SFT only & 40.6 & 79.8 & 71.2 \\
216	CED reranker & No & 41.5 & 80.5 & 60.5 \\
217	RSFT-CED & Yes & 44.9 & 81.3 & 66.1 \\
218	RSFT-CED + reranker & Yes & 45.2 & 81.8 & 58.5 \\
219	\bottomrule
220	\end{tabular}
221	\caption{CED as a composable module (dev set). Reranking uses $N{=}8$ candidates; inference cost is $\sim$8$\times$.}
222	\label{tab:reranker}
223	\end{table}
224	
225	The composability of CED is noteworthy: RSFT improves generation quality (higher rel\_F1 and evi\_F1), while reranking provides additional distractor filtering (lower EDCR). These two applications are complementary because RSFT modifies the model's generation distribution while reranking performs sharp selection among candidates.
226	
227	\subsection{Online RL Fails: GRPO Analysis (Claim 3)}
228	\label{sec:grpo}
229	
230	Table~\ref{tab:grpo} summarizes GRPO experiments across three reward types and multiple configurations. All configurations exhibit the same pattern: reward increases monotonically while rel\_F1 collapses catastrophically within 10--50 steps.
231	
232	\begin{table}[t]
233	\centering
234	\small
235	\begin{tabular}{lcccccc}
236	\toprule
237	\textbf{Reward} & \textbf{LR} & \textbf{KL} & \textbf{Collapse} & \textbf{Peak} & \textbf{Final} & \textbf{Final} \\
238	& & & \textbf{Step} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{Reward} \\
239	\midrule
240	CED & 5e-6 & 0 & $\sim$10 & 1.4 & 85.0 & 1.20 \\
241	CED & 5e-5 & 0.01 & $\sim$50 & 21.1 & 57.5 & 1.20 \\
242	flat-NLI & 5e-6 & 0 & $\sim$25 & $<$1 & $<$1 & 0.29 \\
243	extract & 5e-6 & 0 & $\sim$20 & 1.5 & --- & 0.30 \\
244	\bottomrule
245	\end{tabular}
246	\caption{GRPO trajectory summary. ``Collapse Step'' = step at which rel\_F1 drops below 5\%. All configs start from the same SFT checkpoint (rel\_F1 = 40.6\%).}
247	\label{tab:grpo}
248	\end{table}
249	
250	The CED reward without KL constraint (lr=5e-6) is particularly revealing: evi\_F1 \emph{increases} to 85.0\% (surpassing RSFT's 81.3\%) while rel\_F1 collapses to 1.4\%. The model learns to generate high-quality evidence but ``forgets'' how to extract relations---the policy gradient from CED reward reshapes generation toward evidence-rich outputs at the expense of structured extraction.
251	
252	Adding KL constraints (KL=0.01) delays but does not prevent collapse: rel\_F1 peaks at 21.1\% (step 90) before declining, still far below the SFT baseline. The flat-NLI reward collapses fastest (90\% of groups reach zero-variance outputs by step 25), because its smoother reward surface enables rapid convergence to degenerate optima.
253	
254	This systematic failure across reward types and hyperparameters is consistent with the evidence grounding gradient vanishing analysis in LongRLVR \cite{song2026longrlvr}: in multi-objective structured generation, the evidence grounding signal dominates the policy gradient while the extraction signal vanishes, creating an irreconcilable conflict. RSFT sidesteps this by using CED as a \emph{selection criterion} rather than a gradient signal, preserving the balanced generation capability of the SFT checkpoint.
255	
256	\subsection{EDCR Diagnostic Analysis (Claim 4)}
257	\label{sec:edcr}
258	
259	Table~\ref{tab:edcr_diag} presents cross-method EDCR diagnostics. CED-based methods consistently reduce the mean number of distractor citations per relation instance.
260	
261	\begin{table}[t]
262	\centering
263	\small
264	\begin{tabular}{lccccc}
265	\toprule
266	\textbf{Method} & \textbf{EDCR}$\downarrow$ & \textbf{evi\_F1} & \textbf{\#Distr.} & \textbf{\#Gold} & \textbf{\#Total} \\
267	\midrule
268	SFT & 71.2 & 79.8 & 3.2 & 2.1 & 5.3 \\
269	RSFT flat-NLI & 68.5 & 79.9 & 2.9 & 2.0 & 4.9 \\
270	RSFT CED & 66.1 & 81.3 & 2.6 & 2.1 & 4.7 \\
271	CED reranker & 60.5 & 79.0 & 2.2 & 2.0 & 4.2 \\
272	\bottomrule
273	\end{tabular}
274	\caption{Cross-method EDCR diagnostic (dev set). \#Distr.\ = mean entity-sharing distractor count, \#Gold = mean gold evidence cited, \#Total = mean total citations per instance.}
275	\label{tab:edcr_diag}
276	\end{table}
277	
278	\paragraph{Relation-Type Analysis.}
279	EDCR varies dramatically across relation types (Table~\ref{tab:edcr_rel}). Geographic and nationality relations (P17, P131, P27) exhibit high EDCR ($\geq$0.74 even after RSFT+CED), because documents about locations contain many sentences mentioning country and city names without supporting the specific relation. Creative-domain relations (P50, P86, P175) have lower EDCR ($\leq$0.42), as these relations are typically stated in specific sentences with fewer entity-sharing distractors.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\begin{tabular}{lcccr}
285	\toprule
286	\textbf{Relation} & \textbf{SFT} & \textbf{RSFT-CED} & $\Delta$ & \textbf{\#Inst.} \\
287	\midrule
288	\multicolumn{5}{l}{\emph{High-EDCR relations}} \\
289	P17 (country) & 85.0 & 79.0 & $-$6.0 & 1205 \\
290	P131 (located in) & 83.0 & 78.0 & $-$5.0 & 987 \\
291	P27 (citizenship) & 80.0 & 74.0 & $-$6.0 & 654 \\
292	P30 (continent) & 78.0 & 73.0 & $-$5.0 & 321 \\
293	P150 (contains) & 77.0 & 72.0 & $-$5.0 & 445 \\
294	\midrule
295	\multicolumn{5}{l}{\emph{Low-EDCR relations}} \\
296	P86 (composer) & 48.0 & 42.0 & $-$6.0 & 198 \\
297	P50 (author) & 45.0 & 39.0 & $-$6.0 & 276 \\
298	P175 (performer) & 42.0 & 37.0 & $-$5.0 & 312 \\
299	P40 (child) & 40.0 & 35.0 & $-$5.0 & 187 \\
300	P26 (spouse) & 38.0 & 33.0 & $-$5.0 & 156 \\
301	\bottomrule
302	\end{tabular}
303	\caption{EDCR (\%) by relation type (dev set, top-5 and bottom-5). CED reduces EDCR consistently (5--6pp) but high-EDCR relations remain challenging.}
304	\label{tab:edcr_rel}
305	\end{table}
306	
307	CED provides a uniform 5--6pp EDCR reduction across all relation types, suggesting it captures a general distractor pattern rather than being relation-specific. However, the absolute EDCR values for geographic relations remain high (73--79\%), indicating that entity-sharing distractor confusion in these domains is structural: documents about locations inherently contain many entity-mentioning sentences, and resolving this likely requires relation-type-aware scoring.
308	
309	\paragraph{Limitations.} EDCR of 58.5--66.1\% across our best configurations means that a majority of non-gold citations are still entity-sharing distractors. While this represents meaningful progress over the SFT baseline (71.2\%), we acknowledge that the distractor problem is far from solved. Part of this is attributable to annotation incompleteness in DocRED---our Re-DocRED analysis (\S\ref{sec:redocred}) shows that EDCR drops significantly under more complete annotations.
310	
311	\subsection{Evidence Baseline Comparison}
312	\label{sec:protocol}
313	
314	Table~\ref{tab:baseline} contextualizes our evidence results against encoder baselines. An important caveat: DREEAM and SAIS extract evidence via attention weight thresholding (binary classification per sentence), while \method{} generates explicit sentence indices. These evaluation protocols differ fundamentally---our model ``knows what it is citing'' while attention-based methods derive evidence post-hoc.
315	
316	\begin{table}[t]
317	\centering
318	\small
319	\begin{tabular}{llccc}
320	\toprule
321	\textbf{Method} & \textbf{Type} & \textbf{dev evi\_F1} & \textbf{test evi\_F1} & \textbf{dev rel\_F1} \\
322	\midrule
323	DREEAM (paper) & encoder & --- & 57.3 & 63.5 \\
324	DREEAM (reprod.) & encoder & 56.8 & --- & 62.8 \\
325	SAIS (reprod.) & encoder & 54.8 & 55.7 & 61.8 \\
326	FREIGE (ours) & generative & 81.3 & 78.9$^*$ & 44.9 \\
327	\bottomrule
328	\end{tabular}
329	\caption{Evidence baseline comparison. $^*$Test evi\_F1 computed locally (not from CodaLab). DREEAM reproduction gap: $-$0.5pp from reported test evi\_F1.}
330	\label{tab:baseline}
331	\end{table}
332	
333	\method{}'s evi\_F1 substantially exceeds encoder baselines (78.9\% vs.\ 57.3\%), but we emphasize that this comparison should be treated as a reference point rather than a direct superiority claim. The evaluation protocols produce different error distributions: attention-based methods suffer from threshold sensitivity, while generative methods may over-cite (producing more citations that happen to include gold sentences). \method{}'s rel\_F1 (44.9\%) is lower than encoder methods (62.8\% for DREEAM), reflecting the current gap between generative and encoder approaches for extraction---\method{}'s contribution is evidence grounding, not extraction supremacy.
334	
335	\subsection{Model Size Ablation}
336	
337	Table~\ref{tab:size} evaluates the RSFT+CED pipeline across three model sizes.
338	
339	\begin{table}[t]
340	\centering
341	\small
342	\begin{tabular}{llccccc}
343	\toprule
344	\textbf{Model} & \textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & $\Delta$\textbf{rel} & $\Delta$\textbf{evi} \\
345	\midrule
346	\multirow{2}{*}{1.7B} & SFT & 32.8 & 73.5 & 75.0 & --- & --- \\
347	 & RSFT-CED & 36.5 & 75.8 & 70.5 & +3.7 & +2.3 \\
348	\midrule
349	\multirow{2}{*}{4B} & SFT & 40.6 & 79.8 & 71.2 & --- & --- \\
350	 & RSFT-CED & 44.9 & 81.3 & 66.1 & +4.4 & +1.5 \\
351	\midrule
352	\multirow{2}{*}{8B} & SFT & 44.5 & 81.8 & 69.0 & --- & --- \\
353	 & RSFT-CED & 48.2 & 83.2 & 63.5 & +3.7 & +1.4 \\
354	\bottomrule
355	\end{tabular}
356	\caption{Model size ablation (dev set). RSFT+CED consistently improves over SFT across 1.7B--8B, with relative gains largely independent of model capacity.}
357	\label{tab:size}
358	\end{table}
359	
360	RSFT+CED provides consistent improvements at all scales: $\Delta$rel\_F1 ranges from +3.7 to +4.4pp, and $\Delta$evi\_F1 from +1.4 to +2.3pp. The 1.7B model shows the largest evi\_F1 gain (+2.3pp), likely because smaller models have higher generation diversity, giving CED more room for discrimination. The 8B model achieves the best absolute performance (rel\_F1 48.2\%, evi\_F1 83.2\%) and the largest EDCR improvement ($-$5.5pp). The marginal gain from 4B to 8B is modest (rel\_F1 +3.3pp, evi\_F1 +1.9pp), suggesting diminishing returns at larger scales for this task.
361	
362	\subsection{Re-DocRED Extension}
363	\label{sec:redocred}
364	
365	Table~\ref{tab:redocred} compares results on DocRED and Re-DocRED, which corrects annotation incompleteness in DocRED by supplementing missing relations and evidence labels.
366	
367	\begin{table}[t]
368	\centering
369	\small
370	\begin{tabular}{llccc}
371	\toprule
372	\textbf{Dataset} & \textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
373	\midrule
374	\multirow{2}{*}{DocRED} & SFT & 40.6 & 79.8 & 71.2 \\
375	 & RSFT-CED & 44.9 & 81.3 & 66.1 \\
376	\midrule
377	\multirow{2}{*}{Re-DocRED} & SFT & 43.5 & 81.5 & 58.0 \\
378	 & RSFT-CED & 47.5 & 83.5 & 52.5 \\
379	\bottomrule
380	\end{tabular}
381	\caption{DocRED vs.\ Re-DocRED (dev set). Re-DocRED's more complete annotations reduce EDCR by $\sim$13pp across methods.}
382	\label{tab:redocred}
383	\end{table}
384	
385	Two findings emerge: (1)~EDCR drops substantially on Re-DocRED ($-$13.2pp for SFT, $-$13.6pp for RSFT-CED), confirming that a significant portion of apparent entity-sharing distractors in DocRED are actually valid evidence sentences missed by annotators. (2)~RSFT+CED maintains consistent improvements on Re-DocRED ($\Delta$rel\_F1 +4.0pp, $\Delta$evi\_F1 +2.0pp, $\Delta$EDCR $-$5.5pp), demonstrating robustness to annotation quality. The residual EDCR of 52.5\% on Re-DocRED indicates that the distractor problem persists even with better annotations, though at a reduced level.
386	
387	\subsection{Ablation Studies}
388	
389	\paragraph{Top-$k$ Selection.}
390	Table~\ref{tab:topk} evaluates the quality-quantity trade-off in CED candidate selection.
391	
392	\begin{table}[t]
393	\centering
394	\small
395	\begin{tabular}{ccccccc}
396	\toprule
397	\textbf{$k$} & \textbf{\#Samples} & \textbf{Mean CED} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
398	\midrule
399	1 & 2,718 & 0.668 & 44.9 & 81.3 & 66.1 \\
400	3 & 7,950 & 0.548 & 45.5 & 80.2 & 67.8 \\
401	\bottomrule
402	\end{tabular}
403	\caption{Top-$k$ selection ablation (dev set).}
404	\label{tab:topk}
405	\end{table}
406	
407	$k{=}3$ provides $\sim$3$\times$ more training data with lower mean CED score (0.548 vs.\ 0.668). This yields a slight rel\_F1 improvement (+0.6pp) from greater data diversity, but \emph{degrades} evi\_F1 ($-$1.1pp) and EDCR (+1.7pp). The rank-2 and rank-3 candidates contain more distractor-heavy evidence, diluting the CED signal. We use $k{=}1$ as the default since evidence quality is our primary objective.
408	
409	\paragraph{NLI Model Capacity.}
410	Table~\ref{tab:nli} compares DeBERTa-v3-base and DeBERTa-v3-large as CED scorers.
411	
412	\begin{table}[t]
413	\centering
414	\small
415	\begin{tabular}{lcccc}
416	\toprule
417	\textbf{NLI Model} & \textbf{Disc.\ Acc.} & \textbf{Margin} & \textbf{RSFT evi\_F1} & \textbf{RSFT EDCR}$\downarrow$ \\
418	\midrule
419	DeBERTa-v3-base & 81.5 & 0.48 & 81.3 & 66.1 \\
420	DeBERTa-v3-large & 84.5 & 0.52 & 81.7 & 65.2 \\
421	\bottomrule
422	\end{tabular}
423	\caption{NLI model ablation (dev set). ``Disc.\ Acc.'' = CED discrimination accuracy on gold vs.\ distractor pairs.}
424	\label{tab:nli}
425	\end{table}
426	
427	The larger NLI model improves discrimination accuracy by +3.0pp and mean CED margin by +0.04, but downstream RSFT gains are marginal (evi\_F1 +0.4pp, EDCR $-$0.9pp). This suggests that the current bottleneck is annotation completeness rather than NLI model capability: a stronger NLI model cannot compensate for gold evidence labels that are themselves incomplete.
428	
429	\section{Analysis}
430	
431	\paragraph{Why Flat-NLI Fails at Evidence Discrimination.}
432	The flat-NLI RSFT result (Table~\ref{tab:ced_nli}) reveals that flat-NLI scoring achieves virtually zero evi\_F1 improvement over SFT (+0.1pp), despite meaningfully improving rel\_F1 (+3.6pp). This asymmetry arises because flat-NLI can filter candidates with globally poor NLI scores (improving extraction quality) but cannot distinguish entity-sharing distractors from genuine evidence---both receive high entailment scores because they share key entities. CED's contrastive design directly targets this blind spot: the margin $p_{\text{pos}} - \max(p_{\text{neg}})$ penalizes candidates where distractor sentences also receive high NLI scores.
433	
434	\paragraph{Online vs.\ Offline RL for Structured IE.}
435	Our GRPO analysis (\S\ref{sec:grpo}) provides empirical evidence for a broader methodological insight: online RL is poorly suited for multi-objective structured generation where different objectives (extraction accuracy, evidence faithfulness) create competing gradient signals. The CED GRPO experiment is the clearest illustration---evi\_F1 rises to 85.0\% while rel\_F1 collapses to 1.4\%, because the CED reward gradient overwhelms the extraction objective. RSFT avoids this conflict entirely by treating CED as a data selection criterion rather than a training objective, preserving the SFT model's balanced generation capability.
436	
437	\paragraph{CED as a Composable Module.}
438	CED can be applied at three points in the pipeline: (1)~training data selection for RSFT, (2)~inference-time reranking, and (3)~both combined. Each application provides additive benefits (Table~\ref{tab:reranker}), with the combined approach achieving the best EDCR (58.5\%) while maintaining strong rel\_F1 and evi\_F1. This composability makes CED practical for deployment: teams can start with the training-free reranker and optionally add RSFT when compute allows.
439	
440	\section{Conclusion}
441	
442	We presented \method{}, the first LLM-based framework for document-level relation extraction with evidence grounding. Our Contrastive Evidence Discrimination (\ced{}) scoring function provides consistent improvements over flat-NLI scoring and functions as a composable module for both training and inference. We documented the systematic failure of online RL (GRPO) for structured IE and showed that offline application of \ced{} via RSFT effectively sidesteps catastrophic forgetting.
443	
444	Our results demonstrate that LLMs can generate both relation triples and verifiable evidence for DocRE, with evidence quality competitive across model sizes and datasets. The EDCR metric provides complementary diagnostic value by quantifying entity-sharing distractor citations.
445	
446	\paragraph{Limitations.}
447	\method{}'s rel\_F1 (42.8--43.8\%) remains below encoder SOTA ($\sim$63\%), reflecting the current gap between generative and encoder approaches for extraction. EDCR of 58.5--66.1\% indicates that distractor citations remain a significant issue. The evi\_F1 comparison with encoder baselines is not directly apple-to-apple due to different evidence extraction mechanisms. Our experiments are limited to English DocRE on DocRED/Re-DocRED.
448	
449	\bibliography{custom}
450	
451	\appendix
452	
453	\section{GRPO Full Configuration Grid}
454	\label{app:grpo}
455	
456	We evaluated GRPO across 3 reward types $\times$ 4+ learning rates $\times$ KL constraint configurations. All configurations exhibited the same failure pattern: monotonically increasing reward with catastrophic rel\_F1 collapse within 10--50 gradient steps. The KL-constrained CED variant (lr=5e-5, KL=0.01) achieved the highest peak rel\_F1 (21.1\% at step 90) but still fell far short of the SFT baseline (40.6\%).
457	
458	\section{RSFT Hyperparameter Configurations}
459	\label{app:rsft}
460	
461	\begin{table}[h]
462	\centering
463	\small
464	\begin{tabular}{lcccc}
465	\toprule
466	\textbf{Config} & \textbf{Epochs} & $\alpha$ & \textbf{LR} & \textbf{dev rel\_F1} \\
467	\midrule
468	r1 (s42) & 3 & 128 & 2e-5 & 44.5 \\
469	r1 (s44) & 3 & 128 & 2e-5 & 46.6 \\
470	r2a & 1 & 128 & 2e-5 & 44.9 \\
471	r2b & 1 & 32 & 1e-5 & 44.9 \\
472	\bottomrule
473	\end{tabular}
474	\caption{RSFT hyperparameter configurations. All use LoRA with rank 16.}
475	\end{table}
476	
477	\end{document}
478	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed90166a-2425-4efa-a83c-560b26f88516",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "15a8c6bb-942d-4a35-b252-a427236d5f31",
  "sourceToolAssistantUUID": "ed90166a-2425-4efa-a83c-560b26f88516",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T12:47:31.934Z_

Now let me check the actual experimental numbers more carefully by examining the discrepancies between the "best" and "median" paper versions, and the actual project data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a8c6bb-942d-4a35-b252-a427236d5f31",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NyEMBr4U2GhALvTCeJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ad934a-2527-418c-b39d-0d9f7c8b5e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ky8MrFtQNiJ4QdtrN2EA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12686,
      "cache_read_input_tokens": 59135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12686,
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

_source line 35 · 2026-05-15T12:47:34.443Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VAYThdZURxALU1sSmMk9AX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86ad934a-2527-418c-b39d-0d9f7c8b5e3e",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NyEMBr4U2GhALvTCeJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "361543ee-2eb7-4aa9-9fdb-8a0f87ec568c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ky8MrFtQNiJ4QdtrN2EA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12686,
      "cache_read_input_tokens": 59135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12686,
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

_source line 36 · 2026-05-15T12:47:34.452Z_

<details><summary>↩ Tool result · `toolu_01VAYThdZURxALU1sSmMk9AX`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{multirow}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{natbib}
13	\usepackage{tabularx}
14	\usepackage{caption}
15	
16	\newcommand{\method}{FREIGE}
17	\newcommand{\metric}{EDCR}
18	
19	\title{Why Online RL Catastrophically Fails for Structured Information Extraction, \\and What Works Instead}
20	
21	\author{Anonymous}
22	
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	%======================================================================
29	\begin{abstract}
30	%======================================================================
31	Reinforcement learning from verifier feedback has driven dramatic gains in mathematical reasoning and code generation, yet its effectiveness on \emph{structured} NLP tasks remains poorly understood.
32	We present the first systematic study of online RL (GRPO) for document-level relation extraction with evidence generation on DocRED.
33	Across three reward functions and multiple learning rates, GRPO \emph{universally} fails: reward increases while extraction F1 collapses below 0.02, even as evidence quality can \emph{exceed} the supervised baseline---evidence learning and relation extraction catastrophically decouple under online policy optimization.
34	We connect this finding to recent theoretical work on evidence grounding gradient vanishing in long-context RL.
35	As a practical alternative, we show that \textbf{Rejection Sampling Fine-Tuning (RSFT)} with NLI-based candidate filtering reliably improves both extraction (+3.7 F1 on test) and evidence quality, circumventing the instability of online RL.
36	Additionally, we propose \textbf{Entity-sharing Distractor Citation Rate (EDCR)}, a diagnostic metric that captures a failure mode invisible to standard Evidence F1: models citing entity-sharing distractor sentences that appear relevant but do not actually support the extracted relation.
37	Cross-method EDCR analysis reveals that even the best RSFT model still cites distractors in 63.5\% of evidence sentences, identifying a key bottleneck for future work.
38	Our results suggest that for structured IE tasks with compositional output spaces, offline RL approaches should be preferred over online policy optimization.
39	
40	\end{abstract}
41	
42	%======================================================================
43	\section{Introduction}
44	\label{sec:intro}
45	%======================================================================
46	
47	Document-level relation extraction (DocRE) requires identifying relations between entity pairs scattered across multiple sentences, making it one of the most challenging structured prediction tasks in information extraction \citep{yao2019docred}.
48	Beyond identifying \emph{what} relation holds, deployment scenarios---human-in-the-loop knowledge base population, biomedical literature curation, and RAG-based provenance tracking---increasingly demand \emph{why}: explicit evidence sentences justifying each extracted triple.
49	
50	Recent work has demonstrated that large language models (LLMs) can approach encoder-based SOTA on DocRE extraction metrics \citep{wadhwa2023revisiting}.
51	However, no existing LLM-based method simultaneously generates both extractions and verifiable evidence citations.
52	A natural approach is to train LLMs to output evidence alongside extractions using reinforcement learning with NLI-based faithfulness rewards---an approach that has proven highly effective for reasoning tasks \citep{deepseek2025r1,shao2024deepseekmath}.
53	
54	\textbf{Our central finding is negative}: online RL (specifically GRPO) \emph{catastrophically fails} for this structured IE task, across all reward designs we tested.
55	This is not a hyperparameter issue---we evaluate three fundamentally different reward functions (contrastive NLI, flat NLI, extraction-only) across multiple learning rates, and observe universal failure: reward signals increase monotonically while relation extraction F1 collapses to near zero within 15--30 training steps.
56	
57	More surprisingly, we observe a \emph{decoupling} phenomenon: under slow learning rates, GRPO drives evidence F1 \emph{above} the supervised baseline (0.850 vs.\ 0.798) while relation extraction F1 remains below 0.02.
58	The model learns to generate high-quality evidence for relations it can no longer extract---a failure mode specific to compositional structured outputs where different output components can be independently optimized by the RL objective.
59	
60	We connect this finding to the theoretical analysis in LongRLVR \citep{longrlvr2026}, which identifies evidence grounding gradient vanishing in long-context RL: GRPO's group-relative advantage estimation degenerates when rollouts from the same prompt exhibit high structural variance (different relation types, different entity configurations), causing the advantage signal for structured extraction to be dominated by noise.
61	
62	As a practical alternative, we demonstrate that \textbf{Rejection Sampling Fine-Tuning (RSFT)}---generating multiple candidates from an SFT model, filtering by NLI-based quality scores, and fine-tuning on the filtered set---reliably improves both extraction and evidence quality without the instability of online policy optimization.
63	RSFT improves relation F1 by +3.7 points on the DocRED test set over SFT, while maintaining evidence F1 of 76.5\%.
64	
65	We further introduce \textbf{Entity-sharing Distractor Citation Rate (EDCR)}, a diagnostic metric targeting a blind spot of standard Evidence F1: the citation of sentences that share entities with the target relation but do not actually provide supporting evidence.
66	Cross-method EDCR analysis reveals that this distractor citation problem is pervasive (63--86\% across methods) and only weakly correlated with Evidence F1 ($r = -0.42$), establishing it as an independent evaluation dimension.
67	
68	Our contributions are:
69	\begin{enumerate}
70	    \item A systematic empirical demonstration that online RL (GRPO) catastrophically fails for structured IE, with analysis of the evidence--extraction decoupling phenomenon (\S\ref{sec:grpo_analysis}).
71	    \item RSFT with NLI-based filtering as an effective offline alternative that reliably improves both extraction and evidence quality (\S\ref{sec:rsft_results}).
72	    \item EDCR, a diagnostic metric for entity-sharing distractor citations, revealing a failure mode invisible to standard Evidence F1 (\S\ref{sec:edcr}).
73	\end{enumerate}
74	
75	%======================================================================
76	\section{Related Work}
77	\label{sec:related}
78	%======================================================================
79	
80	\paragraph{Document-Level Relation Extraction.}
81	DocRE has been dominated by encoder-based methods: ATLOP \citep{zhou2021atlop}, DREEAM \citep{ma2023dreeam}, and SAIS \citep{xie2022sais} represent the evidence-providing SOTA, with DREEAM achieving Evi-F1 of 57.34 on DocRED test using attention-guided sentence extraction.
82	Recent generative approaches (LMRC, DocKS-RAG) achieve competitive extraction F1 but do not produce evidence.
83	Our work is the first to address evidence generation in the generative DocRE paradigm.
84	
85	\paragraph{RL for NLP.}
86	RLHF and its variants have driven progress in alignment \citep{ouyang2022training}, mathematical reasoning \citep{deepseek2025r1,shao2024deepseekmath}, and code generation \citep{le2022coderl}.
87	GRPO \citep{shao2024deepseekmath} eliminates the value network by using group-relative advantages.
88	However, applications to structured prediction tasks remain limited.
89	\citet{longrlvr2026} provide theoretical analysis of gradient vanishing in long-context RL, which our empirical findings corroborate for structured IE.
90	
91	\paragraph{Rejection Sampling Fine-Tuning.}
92	RSFT (also called ReST or offline RL) generates candidates from the current policy, filters by a reward signal, and fine-tunes on the filtered set \citep{yuan2023rrhf,dong2023raft,singh2024beyond}.
93	\citet{tajwar2024preference} show theoretical equivalence between RSFT and conservative PPO under certain conditions.
94	We apply RSFT to structured IE with NLI-based filtering, demonstrating its advantage over online RL in this setting.
95	
96	\paragraph{Faithfulness Evaluation.}
97	NLI-based faithfulness metrics are standard for summarization \citep{laban2022summac,honovich2022true}.
98	We extend this paradigm to evidence evaluation in IE, proposing EDCR to capture entity-sharing distractor citations that NLI-based metrics miss.
99	
100	%======================================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "361543ee-2eb7-4aa9-9fdb-8a0f87ec568c",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "1aae6a5e-c8e9-497f-aa54-c6fd53cce9f1",
  "sourceToolAssistantUUID": "361543ee-2eb7-4aa9-9fdb-8a0f87ec568c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T12:47:35.033Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fq8WnnWZG4fU6wrSTNq3PF`</summary>

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
  "parentUuid": "1aae6a5e-c8e9-497f-aa54-c6fd53cce9f1",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NyEMBr4U2GhALvTCeJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd6cc46b-58df-4d8c-855f-7e42cbec678e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126ky8MrFtQNiJ4QdtrN2EA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12686,
      "cache_read_input_tokens": 59135,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12686
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 59135,
          "cache_creation_input_tokens": 12686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12686,
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

_source line 38 · 2026-05-15T12:47:35.042Z_

<details><summary>↩ Tool result · `toolu_01Fq8WnnWZG4fU6wrSTNq3PF`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'faith-evidence-ie'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd6cc46b-58df-4d8c-855f-7e42cbec678e",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "42061c65-62b7-41d5-8473-3101f4aedc5f",
  "sourceToolAssistantUUID": "bd6cc46b-58df-4d8c-855f-7e42cbec678e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T12:47:38.133Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XP1yj5net2n6d9oe6xqXqQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/paper.tex",
  "offset": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42061c65-62b7-41d5-8473-3101f4aedc5f",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NymtjwXvnKnSs9CzTR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95feb95f-22bc-4930-83b5-b18a10ff4463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Gd4y7KLJXd7AFoMDCVgLW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 71821,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 71821,
          "cache_creation_input_tokens": 2666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2666,
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

_source line 40 · 2026-05-15T12:47:38.390Z_

<details><summary>↩ Tool result · `toolu_01XP1yj5net2n6d9oe6xqXqQ`</summary>

```text
100	%======================================================================
101	\section{Method}
102	\label{sec:method}
103	%======================================================================
104	
105	\subsection{Task Formulation}
106	
107	Given a document $D = \{s_1, \ldots, s_n\}$ with entity mentions, the model must output a set of tuples $(h, r, t, E)$ where $h$ is the head entity, $r$ the relation type, $t$ the tail entity, and $E \subseteq \{s_1, \ldots, s_n\}$ the evidence sentences supporting the relation.
108	We format this as a sequence generation task: the model produces structured text containing relation triples annotated with sentence indices $[\texttt{S}_i]$.
109	
110	\subsection{NLI-Based Evidence Scoring}
111	\label{sec:ced}
112	
113	We use a pretrained NLI model (DeBERTa-v3-base fine-tuned on MNLI) to score evidence quality.
114	For a predicted triple $(h, r, t)$ with cited evidence sentence $s_e$, we construct:
115	\begin{itemize}
116	    \item \textbf{Premise}: the evidence sentence $s_e$
117	    \item \textbf{Hypothesis}: ``\textit{h} has the relation \textit{r} with \textit{t}''
118	\end{itemize}
119	and obtain $p_{\text{pos}}(s_e) = P(\text{entailment} \mid s_e, \text{hypothesis})$.
120	
121	\paragraph{Contrastive Evidence Discrimination (CED).}
122	Beyond flat NLI scoring, we compute a contrastive margin.
123	For each triple, we identify the \emph{hardest distractor}: the non-gold sentence $s_d^*$ in the same document that maximizes $p_{\text{pos}}(s_d)$ while sharing at least one entity with the triple.
124	The CED score is:
125	\begin{equation}
126	    \text{CED}(s_e) = p_{\text{pos}}(s_e) - \max_{s_d \in \mathcal{D}} p_{\text{pos}}(s_d)
127	\end{equation}
128	where $\mathcal{D}$ is the set of entity-sharing distractor sentences.
129	
130	\subsection{Online RL: GRPO}
131	\label{sec:grpo_method}
132	
133	We apply Group Relative Policy Optimization (GRPO) to the SFT-initialized model.
134	For each document--query pair, we sample $G$ rollouts and compute advantages relative to the group mean reward.
135	We test three reward functions:
136	\begin{itemize}
137	    \item \textbf{CED reward}: contrastive NLI margin over distractors
138	    \item \textbf{Flat-NLI reward}: $p_{\text{pos}}$ without contrastive comparison
139	    \item \textbf{Extract-only reward}: relation extraction F1 without evidence component
140	\end{itemize}
141	
142	\subsection{Offline RL: Rejection Sampling Fine-Tuning}
143	\label{sec:rsft_method}
144	
145	RSFT proceeds in three stages:
146	\begin{enumerate}
147	    \item \textbf{Candidate Generation}: sample $N=8$ outputs per document from the SFT model with temperature $\tau=0.7$
148	    \item \textbf{Quality Filtering}: score each candidate using the NLI-based scorer (CED or flat-NLI) and retain top-$k$ candidates exceeding a quality threshold
149	    \item \textbf{Fine-Tuning}: train the SFT model on the filtered candidate set using standard supervised loss with LoRA
150	\end{enumerate}
151	
152	This approach circumvents online RL instability by never modifying the policy through gradient-based reward optimization---instead, it \emph{curates} training data using the reward signal.
153	
154	\subsection{Entity-Sharing Distractor Citation Rate (EDCR)}
155	\label{sec:edcr_method}
156	
157	Standard Evidence F1 measures overlap between predicted and gold evidence sentence sets.
158	However, it does not penalize citations of \emph{entity-sharing distractor} sentences: sentences that mention the same entities as the target relation and thus appear superficially relevant, but do not actually support the relation.
159	
160	We define EDCR as:
161	\begin{equation}
162	    \text{EDCR} = \frac{|\{s \in E_{\text{pred}} : s \notin E_{\text{gold}} \wedge \text{shares\_entity}(s, h, t)\}|}{|E_{\text{pred}}|}
163	\end{equation}
164	
165	A lower EDCR indicates fewer distractor citations.
166	EDCR captures a qualitatively different failure mode from Evidence F1: a model can achieve high Evi-F1 (by citing many correct sentences) while simultaneously having high EDCR (by also citing many distractors).
167	
168	%======================================================================
169	\section{Experimental Setup}
170	\label{sec:setup}
171	%======================================================================
172	
173	\paragraph{Dataset.}
174	We use DocRED \citep{yao2019docred} as the primary benchmark, containing 3,053 training, 1,000 development, and 1,000 test documents with relation and evidence annotations.
175	We additionally evaluate on Re-DocRED \citep{tan2022revisiting}, which corrects false negative annotations in DocRED.
176	
177	\paragraph{Base Model.}
178	Our primary model is Qwen3-4B, fine-tuned with LoRA ($\alpha=128$, $r=64$, $\text{lr}=2\times10^{-5}$).
179	We additionally evaluate Qwen3-1.7B and Qwen3-8B for model size ablation.
180	
181	\paragraph{NLI Scorer.}
182	We use DeBERTa-v3-base fine-tuned on MNLI as the default NLI model for CED scoring, with DeBERTa-v3-large evaluated as an ablation.
183	
184	\paragraph{GRPO Configuration.}
185	We train with group size $G=4$, KL coefficient $\beta \in \{0.01, 0.1\}$, and learning rates $\{5 \times 10^{-5}, 5 \times 10^{-6}\}$.
186	All three reward functions (CED, flat-NLI, extract-only) are evaluated.
187	
188	\paragraph{RSFT Configuration.}
189	$N=8$ candidates per document, temperature $\tau=0.7$.
190	Top-$k \in \{1, 3\}$ candidates selected by CED or flat-NLI score.
191	Fine-tuning uses LoRA with the same architecture as SFT.
192	
193	\paragraph{Baselines.}
194	We compare against: (1) SFT-only (Qwen3-4B LoRA on DocRED gold); (2) DREEAM \citep{ma2023dreeam} (RoBERTa-large, evidence SOTA); (3) SAIS \citep{xie2022sais} (RoBERTa, evidence baseline).
195	We reproduce DREEAM and SAIS on the DocRED dev set for controlled comparison.
196	
197	\paragraph{Evaluation Protocol.}
198	We report relation F1 (rel\_F1), Evidence F1 (evi\_F1), and EDCR on the dev set.
199	Test set rel\_F1 and Ign-F1 are obtained from the official CodaLab evaluation; Evi-F1 and EDCR are computed locally.
200	We use paired bootstrap resampling (10,000 iterations) for significance testing.
201	
202	%======================================================================
203	\section{Why Online RL Fails for Structured IE}
204	\label{sec:grpo_analysis}
205	%======================================================================
206	
207	Our central empirical finding is that GRPO \emph{universally fails} for document-level RE with evidence generation.
208	Table~\ref{tab:grpo_summary} summarizes results across all reward types.
209	
210	\begin{table}[t]
211	\centering
212	\caption{GRPO failure across reward types. All configurations fail to maintain extraction capability. Collapse step indicates when output degenerates (frac\_zero\_std $> 0.9$). ``N/A'' indicates slow degradation rather than abrupt collapse.}
213	\label{tab:grpo_summary}
214	\small
215	\begin{tabular}{lcccc}
216	\toprule
217	\textbf{Reward} & \textbf{Best rel\_F1} & \textbf{Best evi\_F1} & \textbf{Best reward} & \textbf{Collapse step} \\
218	\midrule
219	CED (lr=5e-5, $\beta$=0.01) & 0.217 & 0.575 & 1.37 & N/A (slow decay) \\
220	CED (lr=5e-6)               & 0.014 & 0.850 & 1.02 & N/A (never recovers) \\
221	flat-NLI                     & $\sim$0   & $\sim$0   & 0.293 & 25 \\
222	extract-only                 & $\sim$0   & $\sim$0   & $\sim$0   & 30 \\
223	\bottomrule
224	\end{tabular}
225	\end{table}
226	
227	\subsection{The Evidence--Extraction Decoupling Phenomenon}
228	
229	The most striking finding emerges from the GRPO trajectory with lr=$5\times10^{-6}$ (Table~\ref{tab:grpo_trajectory}).
230	This configuration reveals a clean decoupling: the model progressively \emph{improves} evidence quality (evi\_F1 rising from 0.628 at step 20 to 0.850 at step 100, surpassing SFT's 0.798) while relation extraction remains near zero (rel\_F1 $< 0.02$ throughout).
231	The model learns to produce high-quality evidence for relations it cannot extract.
232	
233	\begin{table}[t]
234	\centering
235	\caption{GRPO training trajectories showing reward--extraction divergence. \textbf{Left}: lr=$5\times10^{-5}$, $\beta$=0.01 (fast, partial recovery). \textbf{Right}: lr=$5\times10^{-6}$ (slow, evidence--extraction decoupling).}
236	\label{tab:grpo_trajectory}
237	\small
238	\begin{tabular}{lccc|lccc}
239	\toprule
240	\multicolumn{4}{c|}{\textbf{CED, lr=5e-5, $\beta$=0.01}} & \multicolumn{4}{c}{\textbf{CED, lr=5e-6}} \\
241	\textbf{Step} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{Reward} & \textbf{Step} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{Reward} \\
242	\midrule
243	10  & 0.003 & 0.720 & 0.85 & 20  & 0.008 & 0.628 & 0.60 \\
244	20  & 0.009 & 0.423 & 0.92 & 40  & 0.007 & 0.758 & 0.75 \\
245	30  & 0.034 & 0.589 & 1.05 & 60  & 0.009 & 0.810 & 0.88 \\
246	50  & 0.156 & 0.564 & 1.18 & 80  & 0.012 & 0.828 & 0.95 \\
247	90  & 0.211 & 0.567 & 1.37 & 100 & 0.014 & 0.850 & 1.02 \\
248	\bottomrule
249	\end{tabular}
250	\end{table}
251	
252	\subsection{Theoretical Connection}
253	
254	We connect this failure to the analysis of \citet{longrlvr2026} on evidence grounding gradient vanishing in long-context RL.
255	GRPO estimates advantages by comparing rollouts from the same prompt:
256	\begin{equation}
257	    \hat{A}_i = \frac{r_i - \text{mean}(\{r_j\}_{j=1}^G)}{\text{std}(\{r_j\}_{j=1}^G)}
258	\end{equation}
259	
260	For structured IE, rollouts from the same document exhibit high \emph{structural variance}: different numbers of extracted triples, different entity pairs, different relation types.
261	This structural diversity makes the advantage estimate extremely noisy for the extraction component---the reward difference between two rollouts conflates extraction quality with evidence quality, and the gradient signal for relation extraction is dominated by the evidence reward component.
262	
263	The decoupling in the lr=$5\times10^{-6}$ setting provides direct evidence: the model can isolate and optimize the evidence component (which has a smoother, more learnable reward landscape via NLI scores) while the extraction component's discrete, combinatorial reward signal is overwhelmed by noise.
264	
265	\subsection{Ruling Out Hyperparameter Explanations}
266	
267	A natural objection is that GRPO failure reflects insufficient hyperparameter tuning.
268	We address this with breadth of coverage: three fundamentally different reward functions (CED with contrastive signal, flat-NLI without contrastive signal, extraction-only without evidence component) $\times$ multiple learning rates, spanning qualitatively different optimization regimes.
269	The flat-NLI and extract-only rewards collapse within 25--30 steps, while CED rewards show slower degradation but still fail catastrophically.
270	The universality across reward designs strongly suggests a structural incompatibility between online policy optimization and compositional structured outputs, rather than a tuning issue.
271	
272	%======================================================================
273	\section{RSFT: What Works Instead}
274	\label{sec:rsft_results}
275	%======================================================================
276	
277	In contrast to GRPO's universal failure, RSFT reliably improves both extraction and evidence quality across all tested configurations.
278	
279	\subsection{Development Set Results}
280	
281	Table~\ref{tab:main_dev} shows development set results comparing SFT, RSFT variants, and the CED reranker.
282	
283	\begin{table}[t]
284	\centering
285	\caption{Development set results. RSFT consistently improves over SFT regardless of scoring function. CED reranking provides modest gains without additional training. ``Extra Train'' indicates whether additional fine-tuning beyond SFT is required.}
286	\label{tab:main_dev}
287	\small
288	\begin{tabular}{lcccl}
289	\toprule
290	\textbf{Method} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & \textbf{Extra Train} \\
291	\midrule
292	SFT baseline          & 0.406 & 0.798 & 0.712 & No \\
293	CED-as-reranker (N=8) & 0.415 & 0.801 & 0.665 & No \\
294	RSFT flat-NLI         & 0.452 & 0.811 & 0.662 & Yes \\
295	RSFT+CED (s42)        & 0.445 & 0.819 & 0.657 & Yes \\
296	RSFT+CED (s44)        & \textbf{0.466} & 0.809 & \textbf{0.635} & Yes \\
297	\midrule
298	\multicolumn{5}{l}{\textit{Online RL (for reference)}} \\
299	GRPO+CED best         & 0.217 & 0.575 & 0.858 & Yes \\
300	GRPO+CED (lr=5e-6)    & 0.014 & \textbf{0.850} & --- & Yes \\
301	\bottomrule
302	\end{tabular}
303	\end{table}
304	
305	RSFT+CED (s44) achieves the best rel\_F1 (0.466, +6.0pp over SFT) and the best EDCR (0.635), while RSFT+CED (s42) achieves the best evi\_F1 among RSFT variants (0.819, +2.1pp over SFT).
306	All four RSFT configurations consistently improve over SFT, in stark contrast to GRPO's universal failure.
307	
308	\subsection{CED vs.\ Flat-NLI Scoring for RSFT}
309	\label{sec:ced_vs_flatnli}
310	
311	A critical question is whether CED's contrastive mechanism provides value beyond simple NLI thresholding.
312	Table~\ref{tab:ced_vs_flatnli} presents the head-to-head comparison.
313	
314	\begin{table}[t]
315	\centering
316	\caption{CED vs.\ flat-NLI scoring for RSFT data filtering (dev set). Differences are not statistically significant at $p < 0.05$.}
317	\label{tab:ced_vs_flatnli}
318	\small
319	\begin{tabular}{lcccc}
320	\toprule
321	\textbf{Config} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
322	\midrule
323	SFT baseline           & 0.406 & 0.798 & 0.712 \\
324	RSFT flat-NLI (best)   & 0.452 & 0.811 & 0.662 \\
325	RSFT CED (s42)         & 0.445 & 0.819 & 0.657 \\
326	RSFT CED (s44)         & 0.466 & 0.809 & 0.635 \\
327	\midrule
328	$\Delta$ (CED best $-$ flat-NLI) & +1.4pp & $-$0.2pp & $-$2.7pp \\
329	$p$-value (paired bootstrap) & 0.08 & 0.38 & 0.12 \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	CED scoring shows a directional advantage on rel\_F1 (+1.4pp) and EDCR ($-$2.7pp), but \textbf{neither difference reaches statistical significance} ($p = 0.08$ and $p = 0.12$ respectively).
335	The candidates selected by CED margin filtering and flat-NLI threshold filtering overlap substantially (Jaccard $\sim$0.75), because DocRED's entity-sharing distractors have sufficiently separated NLI score distributions from gold evidence (mean margin = 0.48) that simple $p_{\text{pos}}$ thresholding already filters most distractors.
336	CED's contrastive margin adds discriminative power only for hard negatives ($p_{\text{neg}} > 0.6$), which constitute $<$15\% of distractors.
337	
338	\textbf{Implication}: The benefit of RSFT comes primarily from rejection sampling itself---filtering low-quality candidates regardless of the specific scoring function---rather than from the contrastive signal in CED.
339	
340	\subsection{Test Set Evaluation}
341	\label{sec:test}
342	
343	\begin{table}[t]
344	\centering
345	\caption{Test set results. RSFT+CED improves over SFT but shows larger dev$\to$test degradation than typical encoder methods.}
346	\label{tab:test}
347	\small
348	\begin{tabular}{lcccc}
349	\toprule
350	\textbf{Method} & \textbf{Split} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
351	\midrule
352	SFT baseline    & Test & 0.355 & 0.752 & 0.728 \\
353	RSFT+CED (s44)  & Dev  & 0.466 & 0.809 & 0.635 \\
354	RSFT+CED (s44)  & Test & 0.392 & 0.765 & 0.685 \\
355	$\Delta$ (test $-$ dev) & & $-$7.4pp & $-$4.4pp & +5.0pp \\
356	\bottomrule
357	\end{tabular}
358	\end{table}
359	
360	On the test set (Table~\ref{tab:test}), RSFT+CED achieves rel\_F1 = 0.392 (+3.7pp over SFT's 0.355) and evi\_F1 = 0.765 (+1.3pp over SFT's 0.752).
361	The dev-to-test degradation ($-$7.4pp rel\_F1, $-$4.4pp evi\_F1) exceeds the typical range for encoder methods (DREEAM: $\sim$3.5pp).
362	This suggests partial overfitting to the dev-set distribution, since RSFT candidate generation and CED scoring are performed on the train split which shares distributional characteristics with the dev set.
363	EDCR worsens on the test set (0.685 vs.\ 0.635 on dev), consistent with higher entity co-occurrence density in test documents.
364	
365	\subsection{Comparison with Evidence Baselines}
366	
367	\begin{table}[t]
368	\centering
369	\caption{Comparison with encoder-based evidence methods. Evaluation protocols differ: DREEAM/SAIS use attention-based sentence extraction; our method generates explicit sentence indices. Cross-protocol comparison should be interpreted with caution.}
370	\label{tab:baseline_comparison}
371	\small
372	\begin{tabular}{lccc}
373	\toprule
374	\textbf{Method} & \textbf{Split} & \textbf{rel\_F1} & \textbf{evi\_F1} \\
375	\midrule
376	DREEAM (paper)        & Test & 0.630 & 0.573 \\
377	DREEAM (reproduced)   & Dev  & 0.632 & 0.608 \\
378	SAIS (reproduced)     & Dev  & 0.615 & 0.578 \\
379	\midrule
380	SFT baseline          & Dev  & 0.406 & 0.798 \\
381	RSFT+CED              & Dev  & 0.466 & 0.809 \\
382	RSFT+CED              & Test & 0.392 & 0.765 \\
383	\bottomrule
384	\end{tabular}
385	\end{table}
386	
387	Table~\ref{tab:baseline_comparison} shows that our method achieves substantially higher Evi-F1 than both DREEAM and SAIS, with a $\sim$20pp gap on the dev set.
388	However, this comparison requires careful interpretation: (1) the evaluation protocols differ fundamentally---our model generates explicit sentence indices while DREEAM/SAIS use attention-based extraction; (2) DREEAM's reported test Evi-F1 (57.34) is lower than our reproduced dev Evi-F1 (60.8) by 3.5pp, suggesting possible differences in sentence segmentation or evidence matching; (3) our method's extraction F1 (0.466 dev / 0.392 test) is substantially lower than encoder methods ($\sim$0.63), reflecting the extraction--evidence trade-off inherent in the generative paradigm.
389	
390	%======================================================================
391	\section{EDCR: A Diagnostic Metric for Distractor Citations}
392	\label{sec:edcr}
393	%======================================================================
394	
395	\begin{table}[t]
396	\centering
397	\caption{Cross-method EDCR diagnostic (dev set). EDCR reveals failure modes invisible to Evi-F1: GRPO achieves the highest EDCR (worst distractor behavior) despite having catastrophically low extraction capability. Higher Evi-F1 does not imply lower EDCR ($r = -0.42$).}
398	\label{tab:edcr_diagnostic}
399	\small
400	\begin{tabular}{lccc}
401	\toprule
402	\textbf{Method} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & \textbf{Note} \\
403	\midrule
404	GRPO+CED (ckpt-90)   & 0.567 & 0.858 & catastrophic forgetting \\
405	SFT baseline          & 0.798 & 0.712 & --- \\
406	RSFT flat-NLI         & 0.811 & 0.662 & --- \\
407	CED-as-reranker       & 0.801 & 0.665 & inference-time only \\
408	RSFT+CED (s44)        & 0.809 & 0.635 & best EDCR \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	Table~\ref{tab:edcr_diagnostic} presents EDCR across all evidence-producing methods.
414	The cross-method analysis reveals several insights:
415	
416	\paragraph{EDCR captures a distinct failure mode.}
417	The correlation between Evi-F1 and EDCR is only $r = -0.42$ (weak to moderate), confirming that EDCR measures a qualitatively different dimension of evidence quality.
418	GRPO's ckpt-90 is an extreme case: evi\_F1 = 0.567 with EDCR = 0.858, meaning 85.8\% of its cited evidence consists of entity-sharing distractors.
419	
420	\paragraph{The distractor problem is pervasive.}
421	Even the best method (RSFT+CED) has EDCR = 0.635, meaning 63.5\% of cited sentences are entity-sharing distractors.
422	This establishes distractor citation as a major unsolved problem for generative IE.
423	
424	\paragraph{Training-time vs.\ inference-time intervention.}
425	The CED reranker (EDCR = 0.665) and RSFT (EDCR = 0.635--0.662) both improve over SFT (0.712), but RSFT's advantage is modest.
426	The reranker is constrained by the SFT candidate pool's systematic distractor bias---if all 8 candidates cite similar distractors, reranking cannot help.
427	
428	%======================================================================
429	\section{Ablations and Analysis}
430	\label{sec:ablations}
431	%======================================================================
432	
433	\subsection{Model Size Ablation}
434	\label{sec:model_size}
435	
436	\begin{table}[t]
437	\centering
438	\caption{RSFT+CED across model sizes (dev set). RSFT gain varies non-monotonically with model size; 4B is the sweet spot.}
439	\label{tab:model_size}
440	\small
441	\begin{tabular}{lcccc}
442	\toprule
443	\textbf{Model} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & \textbf{$\Delta$ rel\_F1} \\
444	\midrule
445	Qwen3-1.7B SFT       & 0.312 & 0.735 & 0.720 & --- \\
446	Qwen3-1.7B RSFT+CED  & 0.338 & 0.752 & 0.705 & +2.6pp \\
447	\midrule
448	Qwen3-4B SFT         & 0.406 & 0.798 & 0.712 & --- \\
449	Qwen3-4B RSFT+CED    & 0.466 & 0.809 & 0.635 & +6.0pp \\
450	\midrule
451	Qwen3-8B SFT         & 0.458 & 0.820 & 0.665 & --- \\
452	Qwen3-8B RSFT+CED    & 0.475 & 0.828 & 0.648 & +1.7pp \\
453	\bottomrule
454	\end{tabular}
455	\end{table}
456	
457	Table~\ref{tab:model_size} shows that RSFT gain is non-monotonic with model size.
458	The 1.7B model's weak SFT baseline limits the quality of generated candidates, reducing the pool available for rejection sampling (estimated $\sim$1,200 viable samples vs.\ 2,718 for 4B).
459	The 8B model's strong SFT baseline leaves less room for improvement---its candidates are already relatively good, diminishing the marginal value of filtering.
460	The 4B sweet spot likely reflects an interaction between candidate quality and the filtering headroom, rather than a systematic scaling law.
461	This suggests that the optimal RSFT configuration (including LoRA rank, learning rate, and filtering threshold) should be tuned per model size.
462	
463	\subsection{Re-DocRED Extension}
464	
465	\begin{table}[t]
466	\centering
467	\caption{DocRED vs.\ Re-DocRED (dev set). RSFT gain shrinks with cleaner annotations.}
468	\label{tab:redocred}
469	\small
470	\begin{tabular}{lcccc}
471	\toprule
472	\textbf{Dataset} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ & \textbf{$\Delta$ rel\_F1} \\
473	\midrule
474	DocRED SFT            & 0.406 & 0.798 & 0.712 & --- \\
475	DocRED RSFT+CED       & 0.466 & 0.809 & 0.635 & +6.0pp \\
476	\midrule
477	Re-DocRED SFT         & 0.525 & 0.810 & 0.635 & --- \\
478	Re-DocRED RSFT+CED    & 0.548 & 0.818 & 0.592 & +2.3pp \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	On Re-DocRED (Table~\ref{tab:redocred}), which corrects false negative annotations in DocRED, the SFT baseline is substantially stronger (rel\_F1 0.525 vs.\ 0.406) due to more complete gold labels.
484	RSFT's improvement shrinks from +6.0pp to +2.3pp.
485	This is expected: with cleaner annotations, SFT already captures more of the low-hanging fruit, leaving less room for rejection sampling to add value.
486	EDCR also improves on Re-DocRED (0.592 vs.\ 0.635), because previously mislabeled distractors are now correctly annotated as gold evidence.
487	
488	\subsection{Filtering Threshold: top-$k$ Ablation}
489	
490	\begin{table}[t]
491	\centering
492	\caption{Effect of CED filtering strictness (dev set). Stricter filtering (top-1) yields modest improvements over relaxed filtering (top-3).}
493	\label{tab:topk}
494	\small
495	\begin{tabular}{lccccc}
496	\toprule
497	\textbf{Config} & \textbf{Samples} & \textbf{Mean CED} & \textbf{rel\_F1} & \textbf{evi\_F1} & \textbf{EDCR}$\downarrow$ \\
498	\midrule
499	top-$k$=1 & 2,718  & 0.668 & 0.466 & 0.809 & 0.635 \\
500	top-$k$=3 & 8,154  & 0.512 & 0.458 & 0.805 & 0.672 \\
501	\bottomrule
502	\end{tabular}
503	\end{table}
504	
505	Table~\ref{tab:topk} shows that stricter filtering (top-1, 2,718 samples) modestly outperforms relaxed filtering (top-3, 8,154 samples) on all metrics.
506	The differences are small ($-$0.8pp rel\_F1, $-$0.4pp evi\_F1, +3.7pp EDCR), consistent with our earlier finding that CED scoring precision is not the primary driver of RSFT effectiveness---what matters is that rejection sampling filters out the worst candidates, and both top-1 and top-3 accomplish this.
507	
508	\subsection{NLI Model Capacity}
509	
510	\begin{table}[t]
511	\centering
512	\caption{NLI model ablation for CED scoring. DeBERTa-v3-large provides marginal improvements in discrimination accuracy but does not translate to downstream RSFT gains.}
513	\label{tab:nli_ablation}
514	\small
515	\begin{tabular}{lcccc}
516	\toprule
517	\textbf{NLI Scorer} & \textbf{Mean Margin} & \textbf{Disc.\ Acc.} & \textbf{RSFT evi\_F1} & \textbf{RSFT EDCR}$\downarrow$ \\
518	\midrule
519	DeBERTa-v3-base  & 0.48 & 0.815 & 0.809 & 0.635 \\
520	DeBERTa-v3-large & 0.52 & 0.835 & 0.812 & 0.641 \\
521	\bottomrule
522	\end{tabular}
523	\end{table}
524	
525	Upgrading the NLI scorer from DeBERTa-v3-base to DeBERTa-v3-large increases discrimination accuracy from 81.5\% to 83.5\% and mean CED margin from 0.48 to 0.52, but does \emph{not} improve downstream RSFT quality (Table~\ref{tab:nli_ablation}).
526	Combined with the CED vs.\ flat-NLI result (\S\ref{sec:ced_vs_flatnli}), this confirms that NLI scoring precision is not the bottleneck---a base-sized NLI model with simple threshold filtering is sufficient.
527	
528	\subsection{CED as Inference-Time Reranker}
529	
530	The CED reranker (Table~\ref{tab:main_dev}) provides modest gains over SFT (rel\_F1 +0.9pp, evi\_F1 +0.3pp, EDCR $-$4.7pp) without additional training, but substantially underperforms RSFT.
531	This is expected: reranking is constrained by the SFT candidate pool.
532	If the SFT model systematically cites entity-sharing distractors, all 8 candidates will share this bias, and reranking cannot escape it.
533	RSFT, by contrast, modifies the model's weights to reduce distractor citations at generation time.
534	The 8.5$\times$ inference time overhead of reranking further limits its practical utility.
535	
536	%======================================================================
537	\section{Discussion}
538	\label{sec:discussion}
539	%======================================================================
540	
541	\paragraph{Why does RSFT succeed where GRPO fails?}
542	RSFT and GRPO both use the same reward signal (NLI-based evidence quality), but differ fundamentally in how they use it.
543	GRPO computes policy gradients weighted by reward-based advantages, requiring stable advantage estimation across structurally diverse rollouts.
544	RSFT instead uses the reward purely for \emph{data curation}---filtering candidates and training with standard supervised loss---never propagating reward gradients through the policy.
545	This makes RSFT inherently more stable for compositional outputs where different components (extraction vs.\ evidence) have incommensurable reward landscapes.
546	The theoretical connection to \citet{tajwar2024preference}, who show RSFT's equivalence to conservative PPO, suggests RSFT implicitly constrains the policy update to remain close to the SFT initialization, preventing the catastrophic drift observed in GRPO.
547	
548	\paragraph{The scoring function is not the bottleneck.}
549	Our ablations converge on a surprising conclusion: the specific scoring function (CED vs.\ flat-NLI, DeBERTa-base vs.\ large, top-1 vs.\ top-3) matters far less than the act of rejection sampling itself.
550	This echoes findings in reasoning tasks where simple process rewards outperform elaborate reward models when used for best-of-$N$ selection \citep{lightman2023lets}.
551	For structured IE, the primary signal comes from filtering out degenerate outputs, not from fine-grained quality discrimination.
552	
553	\paragraph{Distractor citations as an open problem.}
554	Even our best model cites entity-sharing distractors in 63.5\% of evidence sentences.
555	This high rate reflects a fundamental challenge: entity-sharing sentences are \emph{topically relevant} to the entity pair and thus difficult to distinguish from genuine evidence without deep relational reasoning.
556	Future work could explore chain-of-thought evidence reasoning, entity-pair-specific contrastive training, or constrained decoding approaches.
557	
558	\paragraph{Limitations.}
559	Our study has several limitations: (1) evaluation is conducted on a single dataset family (DocRED / Re-DocRED); (2) the extraction F1 of our generative approach (0.392 test) substantially trails encoder SOTA ($\sim$0.63), limiting practical applicability; (3) the cross-paradigm Evi-F1 comparison with DREEAM/SAIS involves different evaluation protocols; (4) dev-to-test degradation ($-$7.4pp rel\_F1) suggests overfitting to the training distribution.
560	
561	%======================================================================
562	\section{Conclusion}
563	\label{sec:conclusion}
564	%======================================================================
565	
566	We present the first systematic study of online RL for document-level relation extraction with evidence generation.
567	Our central finding is that GRPO catastrophically fails across all tested reward designs, revealing an evidence--extraction decoupling phenomenon where the model optimizes evidence quality at the expense of extraction capability.
568	This provides empirical support for theoretical predictions about gradient vanishing in long-context RL for structured tasks.
569	
570	As a practical alternative, rejection sampling fine-tuning (RSFT) reliably improves both extraction and evidence quality, with the key insight that the act of filtering low-quality candidates matters more than the sophistication of the scoring function.
571	
572	We additionally introduce EDCR, a diagnostic metric that reveals pervasive entity-sharing distractor citation across all methods---a failure mode invisible to standard Evidence F1.
573	Our analysis establishes distractor citation as a key open problem for evidence-grounded information extraction, with even the best methods citing distractors in over 63\% of evidence sentences.
574	
575	\bibliography{references}
576	\bibliographystyle{plainnat}
577	
578	\end{document}
579	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95feb95f-22bc-4930-83b5-b18a10ff4463",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "f6f96224-6355-40a1-8fef-2a42a875eb30",
  "sourceToolAssistantUUID": "95feb95f-22bc-4930-83b5-b18a10ff4463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T12:47:42.429Z_

Now I have a thorough understanding of the paper, the experimental process, and the three dream paper versions. Let me now also check the actual experiment data to compare against the paper claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f96224-6355-40a1-8fef-2a42a875eb30",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nz1wb2AgB7VF2owDvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7567e6c-e7bc-408c-a595-875d1ae18ff7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LttCq8B86pchFQi2kCeuuC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10687,
      "cache_read_input_tokens": 74487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10687,
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

_source line 42 · 2026-05-15T12:47:43.008Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N6hzKFeae6qXc2KDRBD9DT`</summary>

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
  "parentUuid": "c7567e6c-e7bc-408c-a595-875d1ae18ff7",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4Nz1wb2AgB7VF2owDvN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52d088a2-d352-4efc-bb4b-5d22c70af7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LttCq8B86pchFQi2kCeuuC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10687,
      "cache_read_input_tokens": 74487,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10687
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 74487,
          "cache_creation_input_tokens": 10687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10687,
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

_source line 43 · 2026-05-15T12:47:43.010Z_

<details><summary>↩ Tool result · `toolu_01N6hzKFeae6qXc2KDRBD9DT`</summary>

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
  "parentUuid": "52d088a2-d352-4efc-bb4b-5d22c70af7e3",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "f3e6ed7b-6e4c-4919-a866-502a4ab3f65e",
  "sourceToolAssistantUUID": "52d088a2-d352-4efc-bb4b-5d22c70af7e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-15T12:47:53.124Z_



Now I have thoroughly reviewed all three paper versions (best/median/worst), the full experimental decision log (40 decisions), the paper framing document, the memory file with actual experimental numbers, and the project overview. Let me compile my review.

The key discrepancies and issues I've identified:

1. **The "best" paper fabricates numbers** -- test set results (rel_F1=45.4, evi_F1=80.2) differ dramatically from the actual experimental data (rel_F1=0.392, evi_F1=0.765 per the "worst" paper which uses actual numbers from the project).
2. **The CED vs flat-NLI ablation is not statistically significant** (p=0.08, 0.38, 0.12) -- the "worst" paper honestly reports this, while the "best" paper inflates the differences.
3. **Massive dev-to-test degradation** in the actual data (-7.4pp rel_F1) that the "best" paper minimizes to -1.2pp.
4. **Cross-protocol Evi-F1 comparison** with DREEAM is fundamentally misleading.

Let me submit the review for all three tiers, starting with the most important one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3e6ed7b-6e4c-4919-a866-502a4ab3f65e",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NzMzqnaG7Cejrvn4CD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af3ca34a-e64c-4888-8994-5f1a140d2421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW3HDW9xVBeijc8fp8aPan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 85174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 808,
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

_source line 45 · 2026-05-15T12:48:49.882Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_0123AzZoGWLit2EvgGeBosSV`</summary>

```json
{
  "project": "faith-evidence-ie",
  "tier": "worst",
  "dream_id": "dream_20260515T120227",
  "overall_score": "3.0 - Borderline",
  "report": "# R1 Review: \"Why Online RL Catastrophically Fails for Structured Information Extraction, and What Works Instead\"\n\n## Summary\n\nThis paper studies online RL (GRPO) for document-level relation extraction with evidence generation on DocRED. The central finding is negative: GRPO universally fails, with reward increasing while extraction F1 collapses. The authors propose RSFT with NLI-based filtering as an alternative (+3.7 F1 on test) and introduce the EDCR diagnostic metric. The paper presents a thorough experimental exploration with three reward types, multiple hyperparameter configurations, and several ablations.\n\n## Strengths\n\n- **Thorough negative result documentation.** The GRPO failure analysis is the paper's strongest contribution. The evidence-extraction decoupling phenomenon (evi_F1 rising to 0.850 while rel_F1 collapses to <0.02) is genuinely interesting and well-documented across multiple configurations. Table 2 showing the full trajectory is compelling.\n\n- **Honest statistical reporting.** The paper correctly reports that CED vs flat-NLI differences are not statistically significant (p=0.08, 0.38, 0.12) and draws appropriately hedged conclusions. This is commendable.\n\n- **Comprehensive experimental breadth.** 10 experiments covering GRPO analysis, CED vs flat-NLI ablation, model size ablation (1.7B/4B/8B), Re-DocRED extension, top-k ablation, NLI model ablation, DREEAM reproduction, CED reranker, and test set evaluation. For a systems paper, this is thorough.\n\n- **EDCR metric is a useful contribution.** The observation that Evi-F1 can mask distractor citation (GRPO with evi_F1=0.567 but EDCR=0.858) is a genuinely useful diagnostic insight.\n\n- **Reproducibility details are adequate.** GRPO configurations, RSFT pipeline details (N=8, temperature=0.7, top-k selection), LoRA hyperparameters, and NLI model specifications are provided.\n\n## Weaknesses\n\n**W1 (Major): CED's contribution over flat-NLI is not established.**\nThe paper's central methodological contribution (CED contrastive scoring) shows no statistically significant advantage over flat-NLI scoring for RSFT (p=0.08 for rel_F1, p=0.38 for evi_F1, p=0.12 for EDCR). The paper itself acknowledges that \"the benefit of RSFT comes primarily from rejection sampling itself...rather than from the contrastive signal in CED.\" This fundamentally undermines the paper's method contribution. If CED is not significantly better than flat-NLI, the novelty reduces to \"RSFT works for DocRE\" -- which is a straightforward application of an existing technique.\n\n**W2 (Major): Large dev-to-test degradation raises generalization concerns.**\nThe 7.4pp rel_F1 drop from dev to test (0.466 -> 0.392) is roughly 2x the typical degradation for DocRED methods (DREEAM: ~3.5pp). The EDCR also worsens substantially (0.635 -> 0.685). This suggests the RSFT pipeline may be overfitting to the training distribution, since candidate generation and scoring are performed on training data that shares distributional characteristics with dev. The paper acknowledges this but does not investigate the root cause or propose mitigations.\n\n**W3 (Major): Cross-protocol Evi-F1 comparison with DREEAM is misleading.**\nThe paper compares generative Evi-F1 (0.765 test) against DREEAM's attention-based Evi-F1 (0.573) but these numbers are not comparable. The generative approach produces explicit sentence indices and naturally has higher recall because the model can (and does) cite many sentences. DREEAM uses attention thresholding with precision-oriented behavior. The paper acknowledges the protocol difference but still uses it as a primary selling point. This comparison should be clearly flagged as reference-only, not used to claim \"substantially surpasses encoder evidence SOTA.\"\n\n**W4 (Moderate): Extraction F1 gap is not adequately addressed.**\nThe rel_F1 gap between this method (0.392 test) and encoder SOTA (~0.63) is 24pp -- nearly 40% relative. While the paper positions this as \"the current gap between generative and encoder approaches,\" recent LLM-based methods (LMRC: 0.607, DocKS-RAG: 0.636) achieve much higher extraction F1 without evidence. The paper does not explain why adding evidence generation causes such a large extraction degradation, nor does it compare against these LLM baselines with evidence added post-hoc.\n\n**W5 (Moderate): GRPO hyperparameter exploration is incomplete.**\nThe paper claims GRPO failure is structural, not a hyperparameter issue. However, the exploration is limited: only 2 learning rates (5e-5, 5e-6), one KL coefficient (0.01 vs 0), and G=4 rollouts. Key omissions:\n- No exploration of larger LoRA rank (paper uses r=64, but GRPO+QLoRA instability is known to improve with higher rank)\n- No exploration of reward shaping (e.g., multi-component reward with extraction F1 + evidence quality)\n- No DPO/KTO comparison as intermediate between online RL and offline RSFT\n- The decisions.yaml reveals that many GRPO runs failed due to infrastructure issues (KL explosion from QLoRA 4-bit quantization, reward hacking from missing F1 gating), not fundamental RL limitations\n\n**W6 (Moderate): EDCR metric has significant limitations not fully discussed.**\n- EDCR depends on gold evidence completeness. On Re-DocRED, EDCR drops by ~13pp just from better annotations, meaning a substantial portion of \"distractors\" in DocRED EDCR are actually valid evidence.\n- EDCR only captures one type of evidence error (entity-sharing). Non-entity-sharing false citations are invisible.\n- The Pearson r=-0.42 with Evi-F1 is computed across only 5 data points (methods), making the correlation estimate unreliable.\n\n**W7 (Minor): Missing important baselines.**\n- No comparison with LMRC or DocKS-RAG (LLM-based extraction baselines) augmented with post-hoc evidence retrieval\n- No comparison with DPO, which sits between GRPO and RSFT on the online-offline spectrum\n- No comparison with simple best-of-N sampling at inference time as an RSFT alternative (the CED reranker partially addresses this but uses greedy SFT, not temperature sampling)\n\n**W8 (Minor): Single model family (Qwen3) limits generalizability claims.**\nAll experiments use Qwen3 variants. The GRPO failure could be model-specific (e.g., related to Qwen3's generation_config defaults that caused issues during development, per the memory file). Testing on at least one other model family (LLaMA, Mistral) would strengthen the universality claim.\n\n## Questions for Authors\n\n1. Given that CED vs flat-NLI is not significant, what is the actual methodological contribution? Is the paper better framed as \"RSFT for evidence-grounded DocRE\" rather than \"CED scoring\"?\n\n2. The dev-to-test gap of 7.4pp is concerning. Have you investigated whether this is due to (a) RSFT overfitting, (b) DocRED's known train/dev/test distribution shift, or (c) output truncation at 1024 tokens (which affected 37% of outputs per your experimental notes)?\n\n3. For the GRPO analysis: the decisions.yaml reveals that many runs failed due to QLoRA 4-bit quantization artifacts (KL explosion) and missing reward gating (short outputs getting perfect CED scores). Have you tried GRPO with full fine-tuning or fp16 LoRA to isolate whether the failure is inherent to GRPO or specific to the QLoRA setup?\n\n4. The EDCR correlation of r=-0.42 is computed across 5 methods. Can you compute within-method EDCR-Evi_F1 correlation across documents to get a more reliable estimate?\n\n5. Why does the CED reranker achieve rel_F1=0.415 (barely above SFT 0.406) while RSFT achieves 0.466? If CED is selecting for evidence quality, why does RSFT also improve extraction? Is the extraction improvement from RSFT primarily due to filtering out malformed outputs rather than CED-specific selection?\n\n## Scores\n\n- **Soundness**: 3 (Acceptable) -- The GRPO analysis is solid but the CED contribution is not statistically supported. Cross-protocol comparisons are acknowledged but still misleading.\n- **Excitement**: 3 (Ambivalent) -- The negative GRPO result is interesting but the positive contribution (RSFT+CED) is incremental and CED's advantage is not significant. EDCR is a nice but minor contribution.\n- **Overall Assessment**: 3.0 (Borderline) -- The paper has genuine empirical value in documenting GRPO failure for structured IE, but the claimed method contribution (CED) is not statistically supported over the simpler baseline (flat-NLI RSFT). The honest framing in this version is appreciated, but the positive contribution needs strengthening.\n- **Confidence**: 4 (High) -- I am familiar with DocRE, RL for LLMs, and NLI-based evaluation. I have reviewed the experimental setup in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af3ca34a-e64c-4888-8994-5f1a140d2421",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4NzMzqnaG7Cejrvn4CD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de3bb997-6070-47ea-aa6e-f0cf1bfdb57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW3HDW9xVBeijc8fp8aPan",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 85174,
      "output_tokens": 2767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 808
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2767,
          "cache_read_input_tokens": 85174,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 808,
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

_source line 46 · 2026-05-15T12:48:52.964Z_

<details><summary>↩ Tool result · `toolu_0123AzZoGWLit2EvgGeBosSV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/review_report.md\", \"dream_id\": \"dream_20260515T120227\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de3bb997-6070-47ea-aa6e-f0cf1bfdb57e",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "9ba2a212-129b-4673-97d6-0d3b87b3c987",
  "sourceToolAssistantUUID": "de3bb997-6070-47ea-aa6e-f0cf1bfdb57e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T12:49:42.068Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01JfkHkN1ob8KeJdP2CwiPqZ`</summary>

```json
{
  "project": "faith-evidence-ie",
  "tier": "median",
  "dream_id": "dream_20260515T120227",
  "overall_score": "3.0 - Borderline",
  "report": "# R1 Review: \"FREIGE: Faithful Evidence-Grounded Document-Level Relation Extraction via Contrastive Evidence Discrimination\" (Median Tier)\n\n## Summary\n\nThis paper presents FREIGE, the first LLM-based DocRE system that jointly generates relation triples and evidence sentences. The key contributions are CED (a contrastive NLI scoring function), RSFT with CED-based filtering, a cautionary analysis of GRPO failure, and the EDCR diagnostic metric. On DocRED test, FREIGE achieves rel_F1 42.8--43.8% and evi_F1 78.3--78.9%.\n\n## Strengths\n\n- **Well-structured experimental pipeline.** The paper presents a clean progression: SFT baseline -> GRPO failure -> RSFT success, with CED as a composable module applicable at training-time (RSFT filtering) and inference-time (reranking). The composability result (Table 5, RSFT+CED+reranker achieving EDCR 58.5%) is a nice practical finding.\n\n- **Thorough GRPO failure documentation.** The three-reward-type analysis with trajectory data (Table 6) convincingly demonstrates systematic GRPO failure. The evidence-extraction decoupling (evi_F1 85.0% while rel_F1 <2%) is a genuinely novel empirical finding.\n\n- **Honest evaluation protocol discussion.** Section 5.5 and the baseline comparison table clearly flag the fundamental protocol difference between generative evidence (explicit sentence indices) and attention-based evidence (DREEAM/SAIS). The paper avoids claiming direct superiority despite the large Evi-F1 gap.\n\n- **Comprehensive ablation coverage.** CED vs flat-NLI, top-k selection, NLI model capacity, model size (1.7B/4B/8B), Re-DocRED extension, CED reranker -- all contribute to understanding the method's properties.\n\n- **DREEAM reproduction** with <0.5pp gap validates the evaluation pipeline.\n\n## Weaknesses\n\n**W1 (Major): Inconsistencies in reported numbers across tables.**\nThe paper reports different numbers for the same configuration across tables. For example:\n- Table 1 reports SFT test rel_F1=38.6, but the dev-to-test table (Table 2) shows SFT dev=40.6, test=38.6 -- a 2.0pp gap. However, the actual experimental data shows SFT test rel_F1=0.355 (35.5%), not 38.6%. \n- RSFT CED (s44) test rel_F1 is reported as 43.8 in Table 1, but actual data shows 0.392 (39.2%).\n- The dev-to-test gap is reported as 2.1--2.8pp, but based on actual dev numbers (0.466) and actual test (0.392), it should be 7.4pp.\n\nThese discrepancies between the paper's tables and the underlying experimental data suggest either (a) multiple evaluation runs with different configurations, or (b) errors in number transcription. The authors must clarify and ensure all numbers are traceable to specific experiments.\n\n**W2 (Major): CED vs flat-NLI advantage is modest and potentially not significant.**\nTable 3 shows CED RSFT outperforming flat-NLI RSFT by +0.7pp rel_F1, +1.4pp evi_F1, and -2.4pp EDCR. No significance tests are reported for this comparison. Given that the \"worst\" tier paper (which appears to use the actual experimental data) reports p-values of 0.08/0.38/0.12 for the CED vs flat-NLI comparison -- none significant at p<0.05 -- this undermines the paper's central claim that \"CED provides consistent improvement over flat-NLI scoring.\"\n\n**W3 (Major): The generative approach's extraction F1 is substantially below state-of-the-art.**\nRel_F1 of 42.8--43.8% (test) is 20pp below DREEAM (63.3%) and even further below recent LLM methods like DocKS-RAG (63.6%). The paper positions evidence generation as the primary contribution, but if the extraction quality is too low for practical use, the evidence is of limited value. The paper should discuss whether the rel_F1 gap is inherent to joint extraction+evidence generation or specific to the Qwen3-4B + LoRA setup.\n\n**W4 (Moderate): GRPO exploration may be insufficient to claim \"structural incompatibility.\"**\nThe paper tests 3 reward types x 2 learning rates x limited KL configurations, all with QLoRA 4-bit quantization on Qwen3 only. Known issues with QLoRA + RL (quantization noise in KL computation, limited LoRA expressivity) could explain the failures without invoking \"structural incompatibility between online policy optimization and compositional structured outputs.\" Missing explorations:\n- Full fine-tuning or fp16 LoRA (isolates QLoRA artifacts)\n- Higher LoRA rank (r=128 or r=256)\n- DPO as an intermediate approach\n- Reward decomposition (separate extraction and evidence rewards with independent weighting)\n\n**W5 (Moderate): EDCR correlation analysis is statistically underpowered.**\nThe Pearson r=-0.42 between Evi-F1 and EDCR is computed across only 4-5 data points (methods), making this correlation estimate highly unreliable (confidence interval likely spans from -0.9 to +0.3). The claim that \"EDCR captures a distinct failure mode\" would be better supported by per-document or per-relation-type analysis with sufficient sample size.\n\n**W6 (Moderate): Missing comparison with post-hoc evidence retrieval.**\nA natural baseline for \"LLM extraction + evidence\" is to run an LLM extraction model (e.g., LMRC) and then retrieve evidence sentences using BM25 or sentence similarity. This would provide a fairer comparison for the evidence quality of the joint generation approach.\n\n**W7 (Minor): The relation-type EDCR analysis (Table 7) uses suspiciously round numbers.**\nThe EDCR values by relation type are all integers (85.0, 83.0, 80.0, etc.) with CED improvements that are exactly 5.0 or 6.0pp for every relation type. This suggests either binning/rounding or synthetic data. The authors should provide exact values.\n\n**W8 (Minor): Single model family limits generalizability.**\nAll experiments use Qwen3. The GRPO failure claim would be substantially stronger with replication on LLaMA or Mistral.\n\n## Questions for Authors\n\n1. Can you provide exact p-values for the CED vs flat-NLI comparison? If they are not significant, how do you justify framing CED as the key contribution rather than RSFT itself?\n\n2. The relation-type EDCR analysis (Table 7) shows identical improvement magnitudes (5-6pp) across all relation types. Is this an artifact of rounding? Please provide exact values.\n\n3. Have you tried running GRPO without QLoRA quantization? The decision log suggests many failures were related to QLoRA-specific issues (KL explosion from 4-bit quantization noise).\n\n4. What is the output truncation rate at max_new_tokens=1024? Your experimental notes mention 37% truncation for SFT. Does RSFT reduce this?\n\n5. The RSFT+CED+reranker combination (Table 5) achieves the best EDCR (58.5%) but at 8x inference cost. Have you measured the actual latency overhead per document?\n\n## Scores\n\n- **Soundness**: 3 (Acceptable) -- Experimental design is generally sound but number inconsistencies and missing significance tests weaken confidence.\n- **Excitement**: 3 (Ambivalent) -- The GRPO failure analysis is interesting but the positive contribution (CED) may not be significant over simpler alternatives.\n- **Overall Assessment**: 3.0 (Borderline) -- A competent empirical study with interesting negative results, but the method contribution needs statistical validation and the number inconsistencies must be resolved.\n- **Confidence**: 4 (High) -- Familiar with DocRE, RL for LLMs, NLI-based evaluation, and the specific experimental challenges of this setup."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ba2a212-129b-4673-97d6-0d3b87b3c987",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4P5WnKWrV1JQTViyeqm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42513304-4a15-4ddb-b988-90fc2c734919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X5DrrQkaVE9qy3ukrM7rFc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2896,
      "cache_read_input_tokens": 85982,
      "output_tokens": 2174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2174,
          "cache_read_input_tokens": 85982,
          "cache_creation_input_tokens": 2896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2896,
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

_source line 48 · 2026-05-15T12:49:42.708Z_

<details><summary>↩ Tool result · `toolu_01JfkHkN1ob8KeJdP2CwiPqZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/review_report.md\", \"dream_id\": \"dream_20260515T120227\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42513304-4a15-4ddb-b988-90fc2c734919",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "84040105-3b98-44c4-8937-7528c0417faf",
  "sourceToolAssistantUUID": "42513304-4a15-4ddb-b988-90fc2c734919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T12:50:39.261Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_0163SKYUgfxbmsmWAGtnYiJ4`</summary>

```json
{
  "project": "faith-evidence-ie",
  "tier": "best",
  "dream_id": "dream_20260515T120227",
  "overall_score": "2.5 - Leaning Reject",
  "report": "# R1 Review: \"FREIGE: Faithful Relation Extraction with Evidence via Contrastive Evidence Discrimination\" (Best Tier)\n\n## Summary\n\nThis paper presents FREIGE, which jointly generates relation triples and evidence sentences for document-level RE. It introduces CED (contrastive NLI scoring), shows GRPO catastrophically fails for structured IE, proposes RSFT+CED as an offline alternative, and introduces the EDCR diagnostic metric. The paper claims rel_F1 45.4 and Evi-F1 80.2 on DocRED test, surpassing encoder evidence SOTA.\n\n## Strengths\n\n- **First LLM-based DocRE system with joint evidence generation.** The problem formulation -- generating (h, r, t, E) tuples via sequence generation -- is well-motivated and fills a real gap. No prior LLM-based DocRE method produces verifiable evidence.\n\n- **Strong GRPO failure analysis.** The evidence-extraction decoupling (Table 7: evi_F1 climbing to 85.0% while rel_F1 stays <2%) is a genuinely novel empirical finding. The systematic coverage across 3 reward types provides convincing evidence that this is not a hyperparameter issue.\n\n- **Comprehensive experimental coverage.** 10+ experiments covering model sizes (1.7B/4B/8B), datasets (DocRED, Re-DocRED), scoring functions (CED vs flat-NLI), top-k ablation, NLI model ablation, CED reranker, and DREEAM reproduction. The paper leaves few obvious experimental gaps.\n\n- **EDCR metric is well-motivated.** The observation that GRPO achieves evi_F1=56.7% but EDCR=85.8% demonstrates a genuine blind spot in standard evaluation.\n\n- **CED design has theoretical appeal.** The contrastive margin's bias-cancellation property (lexical overlap affects both positive and negative terms similarly) is a clean insight.\n\n## Weaknesses\n\n**W1 (Critical): Reported numbers appear inflated relative to actual experimental data.**\nCross-referencing the paper's tables with the project's actual experimental records reveals major discrepancies:\n\n| Metric | Paper (Table 5) | Actual Data (decisions/memory) |\n|--------|-----------------|-------------------------------|\n| RSFT+CED test rel_F1 | 45.4 | 39.2 (D038: s44 dev=46.6, test=39.2) |\n| RSFT+CED test evi_F1 | 80.2 | 76.5 |\n| SFT test rel_F1 | 39.7 | 35.5 |\n| Dev-to-test gap | -1.2pp rel_F1 | -7.4pp rel_F1 |\n\nThe paper claims a dev-to-test decay of only -1.2pp for rel_F1, but the actual experimental records show -7.4pp (from 46.6 to 39.2). The test numbers in the paper appear to be projections or estimates rather than actual CodaLab submissions. If these are aspirational numbers from the \"best case\" dream simulation rather than actual results, they cannot be presented as experimental findings. This is the most serious concern with this paper version.\n\n**W2 (Critical): CED vs flat-NLI comparison lacks statistical rigor.**\nTable 2 reports CED RSFT outperforming flat-NLI RSFT by +2.8pp rel_F1, +2.6pp evi_F1, -5.8pp EDCR on dev. However, based on the actual experimental records, the paired bootstrap test yields p-values of 0.08 (rel_F1), 0.38 (evi_F1), and 0.12 (EDCR) -- none significant at p<0.05. The paper presents these differences as established facts (\"CED RSFT outperforms flat-NLI RSFT across all metrics\") without any significance testing. This overclaims the method's contribution.\n\nFurthermore, the paper_framing.md itself notes: \"CED 在 RSFT 中是间接作用（筛选训练数据），非直接 reward\" and lists RC6 concern that \"RSFT+CED 的 EDCR 只比 SFT 低 5-8pp，证据质量提升不够显著.\" The paper should honestly report these limitations.\n\n**W3 (Major): Cross-protocol Evi-F1 comparison is presented misleadingly.**\nThe abstract claims \"surpassing the encoder evidence SOTA (DREEAM, Evi-F1 57.3).\" Section 5.1 states \"the Evi-F1 of 80.2 substantially surpasses DREEAM's 57.3 under comparable evaluation.\" But the evaluation is NOT comparable -- one uses attention-based extraction and the other generates explicit sentence indices. The paper's own Section 6 admits this (\"the evidence generation mechanism differs fundamentally\"), creating an internal contradiction. Generative models that output sentence indices naturally achieve higher Evi-F1 because they can cite many sentences (increasing recall) while attention-based methods threshold attention weights (limiting recall). This is not evidence quality superiority -- it is an artifact of the evaluation protocol.\n\n**W4 (Major): Model size ablation numbers in the paper conflict with actual data.**\nTable 8 reports:\n- 1.7B: RSFT gain +3.6pp (paper) vs +2.6pp (actual data in worst-tier paper)\n- 4B: RSFT gain +6.0pp (consistent across versions)  \n- 8B: RSFT gain +4.4pp (paper) vs +1.7pp (actual data)\n\nThe 8B gain is inflated by 2.7x in this version. If the 8B experiments have not been completed, projected or interpolated numbers should not be presented as results.\n\n**W5 (Major): The extraction F1 gap with SOTA is inadequately addressed.**\nRel_F1 of ~39-45% (depending on which numbers are used) vs encoder SOTA of ~63% is a massive gap. The paper frames this as \"the known trade-off of generative approaches,\" but LMRC achieves 60.7% rel_F1 with LLaMA3.1-8B (also generative, no evidence). The gap is not inherent to the generative paradigm -- it is specific to this system's design choices. The paper should analyze why joint extraction+evidence generation degrades extraction so much and whether architectural modifications (e.g., separate extraction and evidence heads) could help.\n\n**W6 (Moderate): GRPO analysis may be confounded by QLoRA artifacts.**\nThe decision log (D007, D008, D009, D020) reveals that many GRPO failures were caused by QLoRA-specific issues:\n- KL explosion from 4-bit quantization noise (kl_coef > 0 + QLoRA incompatible)\n- Reward hacking from missing F1 gating (short outputs getting perfect CED scores, fixed in D014 but only partially deployed)\n- kl_coef=0 leading to unbounded policy drift\n\nThese are implementation issues, not fundamental RL limitations. The paper's claim of \"structural incompatibility\" between online RL and structured IE would require testing without QLoRA, or at minimum acknowledging that QLoRA-specific artifacts contaminate the analysis.\n\n**W7 (Moderate): Re-DocRED result interpretation is misleading.**\nTable 9 shows RSFT gain on Re-DocRED (+4.6pp rel_F1) comparable to DocRED (+6.0pp). But the actual data (worst-tier paper) shows the gain shrinks from +6.0pp to +2.3pp on Re-DocRED. The paper cherry-picks the version that supports the \"consistent improvement across datasets\" narrative.\n\n**W8 (Minor): Missing important baselines.**\n- No DPO/KTO comparison (intermediate between GRPO and RSFT)\n- No comparison with LLM extraction + post-hoc evidence retrieval  \n- No comparison with other generative LLM DocRE methods (LMRC, DocKS-RAG) augmented with evidence\n- Single model family (Qwen3) limits generalizability of GRPO failure claims\n\n## Questions for Authors\n\n1. The test set numbers in this paper differ substantially from those in the other versions of this manuscript. Which numbers are from actual CodaLab submissions? Please provide submission IDs.\n\n2. Given that CED vs flat-NLI is not significant at p<0.05, would you consider reframing the contribution around RSFT for evidence-grounded DocRE, with CED as one possible scoring function?\n\n3. Have you attempted GRPO with full bf16 fine-tuning (no QLoRA) on even a small subset to verify the failure is not QLoRA-specific?\n\n4. The 8B model ablation shows very different gains across paper versions (1.7pp vs 4.4pp). Are the 8B experiments finalized?\n\n5. What is the inference-time overhead of the full FREIGE pipeline (SFT + RSFT adapter + optional CED reranking) vs a standard encoder model like DREEAM?\n\n## Scores\n\n- **Soundness**: 2 (Borderline) -- Critical number discrepancies between paper versions and experimental records. Missing significance tests for the central method comparison. Cross-protocol comparisons presented as direct comparisons.\n- **Excitement**: 3 (Ambivalent) -- The GRPO failure analysis is interesting, but the positive contribution (CED over flat-NLI) is not statistically validated. EDCR is a useful but minor contribution.\n- **Overall Assessment**: 2.5 (Leaning Reject) -- The \"best case\" framing inflates results beyond what the experimental data supports. The honest version of this paper (worst tier) is borderline acceptable, but this version overclaims. The core issue is that CED's advantage over flat-NLI is not significant, which reduces the novelty to \"RSFT works for evidence-grounded DocRE\" -- an incremental finding. The GRPO analysis is valuable but may be confounded by QLoRA artifacts.\n- **Confidence**: 4 (High) -- I have deep familiarity with DocRE evaluation, RL for LLMs, and NLI-based faithfulness metrics. I have cross-referenced the paper's claims against the full experimental record."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84040105-3b98-44c4-8937-7528c0417faf",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4P9BSbHjDXTRyYiPLqi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4de155b9-fecd-4409-9dad-af03fc3808bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMcui5uQEDSsMomhqyeye9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2300,
      "cache_read_input_tokens": 88878,
      "output_tokens": 2653,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2300
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2653,
          "cache_read_input_tokens": 88878,
          "cache_creation_input_tokens": 2300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2300,
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

_source line 50 · 2026-05-15T12:50:39.926Z_

<details><summary>↩ Tool result · `toolu_0163SKYUgfxbmsmWAGtnYiJ4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/review_report.md\", \"dream_id\": \"dream_20260515T120227\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4de155b9-fecd-4409-9dad-af03fc3808bf",
  "isSidechain": true,
  "promptId": "00a1eb94-0484-4e13-931d-e659507bc0c6",
  "agentId": "a423c10c857240397",
  "type": "user",
  "uuid": "64f0d354-b5dc-48fb-94eb-7bd8d4229c46",
  "sourceToolAssistantUUID": "4de155b9-fecd-4409-9dad-af03fc3808bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T12:50:53.126Z_

All three reviews have been submitted. Here is a summary of the review findings across all three paper tiers:

**Review Summary**

Three versions of the paper were reviewed, each representing a different framing/presentation quality level:

**Worst tier (honest framing):** Score 3.0 (Borderline). This version reports actual experimental numbers (rel_F1=0.392 test, dev-to-test gap of 7.4pp) and honestly discloses that CED vs flat-NLI differences are not statistically significant (p=0.08/0.38/0.12). The GRPO failure analysis is the strongest contribution. Main weaknesses: CED's advantage over flat-NLI is not established, large dev-to-test degradation, and the cross-protocol Evi-F1 comparison with DREEAM remains misleading.

**Median tier (moderate framing):** Score 3.0 (Borderline). Reports intermediate numbers (rel_F1=42.8-43.8% test) with some discrepancies from actual data. Good composability analysis of CED. Main concerns: number inconsistencies across tables, missing significance tests, suspiciously round relation-type EDCR values.

**Best tier (optimistic framing):** Score 2.5 (Leaning Reject). Reports inflated numbers (rel_F1=45.4 test, dev-to-test gap of only 1.2pp) that conflict with actual experimental records (39.2 test, 7.4pp gap). Model size ablation gains are inflated 2.7x for the 8B model. This version overclaims beyond what the data supports.

**Cross-tier critical issues the paper must address:**
1. CED vs flat-NLI is not significant -- reframe contribution around RSFT itself or collect more evidence
2. GRPO failure analysis may be confounded by QLoRA 4-bit artifacts -- needs isolation experiment
3. Cross-protocol Evi-F1 comparison must not be presented as superiority claim
4. 7.4pp dev-to-test degradation needs investigation
5. Missing baselines: DPO, post-hoc evidence retrieval, non-Qwen3 model families

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f0d354-b5dc-48fb-94eb-7bd8d4229c46",
  "isSidechain": true,
  "agentId": "a423c10c857240397",
  "requestId": "req_011Cb4PDQ8wRT1Uu41CuRJRS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5621ea6-ca42-4a50-aa02-21847bf36ff5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596c820e-21ec-4685-b435-a1fe07cb2330",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2WQ8CPGAzF8zMQLM3QAZe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2779,
      "cache_read_input_tokens": 91178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2779,
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
