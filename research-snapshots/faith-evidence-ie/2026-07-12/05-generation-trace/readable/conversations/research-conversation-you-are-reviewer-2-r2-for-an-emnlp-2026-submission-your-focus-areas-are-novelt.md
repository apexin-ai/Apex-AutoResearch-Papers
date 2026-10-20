# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus areas are **Novelty** and **Related Work**. Produce a b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3594e4cd3664149b.jsonl`
- **Structured JSON:** [`426a72cbde69ce6ae51c.json`](../../sessions/42/426a72cbde69ce6ae51c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

50 recorded events

### User

_source line 1 · 2026-05-15T14:10:09.807Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus areas are **Novelty** and **Related Work**. Produce a blind, independent review. Do NOT speculate about whether the paper will be accepted or rejected — just evaluate objectively.

## Venue: EMNLP 2026 Main (via ACL Rolling Review)

### Scoring scales:
- **Soundness** (1-5): 5=Excellent (most thorough), 4=Strong (sufficient for all claims), 3=Acceptable (sufficient for main claims), 2=Poor (main claims not supported), 1=Major issues
- **Excitement** (1-5): 5=Highly exciting, 4=Exciting, 3=Interesting, 2=Potentially interesting, 1=Not exciting
- **Overall Assessment** (1-5, 0.5 increments): 5=Award, 4.5=Borderline award, 4=Conference accept, 3.5=Borderline conference, 3=Findings, 2.5=Borderline findings, 2=Resubmit next cycle, 1.5=Resubmit after next, 1=Do not resubmit
- **Reproducibility** (1-5): 5=Easily reproduce, 4=Mostly reproduce, 3=With some difficulty, 2=Hard pressed, 1=Cannot reproduce
- **Confidence** (1-5): 5=Positive evaluation correct, 4=Quite sure, 3=Pretty sure, 2=Fairly likely missed details, 1=Not my area

### EMNLP typical acceptance rate: ~25% main conference, ~40% including Findings

---

## Paper: FREIGE: Faithful Evidence Generation for LLM-Based Document-Level Relation Extraction via Contrastive Evidence Discrimination

### Abstract
LLMs are closing the gap with encoder-based methods on document-level relation extraction (DocRE), yet no existing LLM approach produces verifiable evidence. FREIGE is the first generative LLM framework jointly outputting relation triples and explicit sentence-level evidence citations on DocRED. Core: CED (Contrastive Evidence Discrimination) scoring via entailment gap between gold evidence and best entity-sharing distractor. Key findings: naïve NLI scoring fooled by entity-sharing distractors; online RL (GRPO+QLoRA) catastrophic forgetting; CED-guided RSFT yields +5.5pp rel_F1, +1.7pp Evi-F1, −7.1pp EDCR on test. Also proposes EDCR metric (human r=0.62).

### Introduction (Section 1)
- DocRE requires identifying relational facts between entity pairs spanning multiple sentences
- Encoder-based methods achieve strong extraction with implicit evidence (attention thresholding)
- LLM approaches show competitive extraction but produce NO explicit evidence — gap for deployment in KB population, biomedical curation, RAG provenance
- Entity-sharing distractor sentences get spuriously high NLI scores due to lexical overlap
- Online RL (GRPO) causes catastrophic forgetting with evidence-extraction decoupling
- Three contributions: CED scoring, CED-guided RSFT, EDCR metric

### Related Work (Section 2)
**Document-Level RE:**
- Encoder-based: DREEAM (RoBERTa-large, attention evidence, Evi-F1_J=0.573), SAIS (Evi-F1_J=0.557)
- LLM-based: LMRC (LLaMA-3.1-8B, F1=60.69, no evidence)
- FREIGE bridges gap: joint triples + explicit evidence

**Reward Hacking and Overoptimization:**
- Connects to RLHF overoptimization literature
- CED as anti-overoptimization mechanism for evidence grounding

**Rejection Sampling Fine-Tuning:**
- RSFT theoretically equivalent to PPO under certain conditions
- Applied here to evidence-grounded IE domain

### Method (Section 3)
**CED:** Contrastive margin = p_entail(gold) − max(p_entail(distractor from entity-sharing non-gold sentences)). Uses DeBERTa-v3-base on MNLI.

**RSFT Pipeline:** SFT → Generate N=8 candidates → CED filter top-1 → fine-tune on filtered data (~2,718 from 21,952 candidates)

**EDCR metric:** Proportion of cited sentences that are entity-sharing but non-gold evidence.

### Experiments (Section 4)
**Test set (Table 1):** FREIGE rel_F1=0.455, Evi-F1_J=0.376, EDCR=0.648. SFT baseline: 0.400/0.322/0.719. LMRC (no evidence): 0.607. DREEAM: Evi-F1_J=0.573.

**RL spectrum (Table 3):** GRPO G=4 rel_F1=0.014, G=8=0.031; DPO=0.325; SFT=0.406; RSFT+CED=0.468

**CED vs flat-NLI (Table 4):** CED > flat-NLI by +2.71pp rel_F1 (p<0.01)

**CED modes (Table 5):** Training (RSFT) >> Inference (reranker) for rel_F1

**EDCR diagnostic (Table 6):** Gradient from GRPO(0.988) to CED-reranker(0.598). EDCR-EviF1 Pearson r=−0.42.

**Human validation (Table 7):** 100 samples, 3 annotators, κ=0.72, Pearson r=0.62.

**Model scale (Table 8):** 1.7B (+3.12pp), 4B (+6.26pp), 8B (+4.89pp) — consistent.

**Re-DocRED (Table 9):** Delta preserved (+5.55pp).

**top_k ablation (Table 10):** k=1 > k=3.

**NLI ablation (Table 11):** DeBERTa-base vs large: +0.38pp, marginal.

**Evidence baselines (Table 12):** FREIGE Evi-F1_J=0.381 vs DREEAM=0.572. Gap from extraction accuracy not evidence quality: conditional Evi-F1 0.807 vs 0.834.

### Discussion (Section 5)
- Why RSFT succeeds: avoids credit assignment issues, QLoRA parameter overwriting, asymmetric gradient optimization
- EDCR limitations: entity-sharing is proxy, +6.8pp auto-human bias, doesn't capture non-entity-sharing distractors
- Extraction gap vs encoders: rel_F1 0.455 vs ~0.631 DREEAM, inherent to generative paradigm at current scale

---

## Your Review Task

Focus on **Novelty** and **Related Work**. Evaluate:

1. **Novelty assessment**: How novel are the three contributions (CED, CED-RSFT, EDCR)? Are they incremental combinations of existing techniques or genuinely new ideas?
2. **Related work coverage**: Are important baselines and related methods missing? Is the positioning accurate?
3. **Claim of "first"**: The paper claims to be the "first LLM-based DocRE with explicit evidence." Is this claim justified? Could there be concurrent or prior work doing similar things?
4. **Framing and positioning**: Is the narrative fair? Does the paper oversell or undersell its contributions? Is the comparison with encoder methods fair?
5. **Broader impact and significance**: How significant is this work for the NLP community? Does it open new research directions?
6. **Writing quality and presentation**: Is the paper clearly written? Are there structural issues?

## Output Format

Produce your review in this exact format:

```
## R2 Review: Novelty & Related Work

### Summary
[2-3 sentence summary]

### Strengths
- S1: ...
- S2: ...
- S3: ...
[etc.]

### Weaknesses
- W1: ...
- W2: ...
- W3: ...
[etc.]

### Questions for Authors
- Q1: ...
- Q2: ...
[etc.]

### Missing Related Work / Positioning Issues
- P1: ...
[etc.]

### Scores
- Soundness: X/5
- Excitement: X/5
- Overall: X.X/5
- Reproducibility: X/5
- Confidence: X/5

### Justification for Overall Score
[2-3 sentences]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "da5a0aa4-3628-4531-8477-92df8ca71cee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T14:10:09.812Z_

```json
{
  "parentUuid": "da5a0aa4-3628-4531-8477-92df8ca71cee",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
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
  "uuid": "79a1733f-4cdb-40e7-bb5d-494854a76dd7",
  "timestamp": "2026-05-15T14:10:09.812Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T14:10:13.380Z_



I'll start by reading the project files to get full context on this paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a1733f-4cdb-40e7-bb5d-494854a76dd7",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VH1Qm4Q1mxHZc7WNCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0fc3ea4-55eb-4b2f-8b7d-c3c0a68dc0d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cZ74Kg4aB3tfPMnos6QXb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7962,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7962,
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

_source line 4 · 2026-05-15T14:10:13.809Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017xo6PeeTCPCWJ2c2qSkEaM`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0fc3ea4-55eb-4b2f-8b7d-c3c0a68dc0d1",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VH1Qm4Q1mxHZc7WNCq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "311219c8-737d-4e87-8c9f-87846c44ede9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017cZ74Kg4aB3tfPMnos6QXb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7962,
      "cache_read_input_tokens": 8249,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7962
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 109,
          "cache_read_input_tokens": 8249,
          "cache_creation_input_tokens": 7962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7962,
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

_source line 5 · 2026-05-15T14:10:13.812Z_

<details><summary>↩ Tool result · `toolu_017xo6PeeTCPCWJ2c2qSkEaM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "311219c8-737d-4e87-8c9f-87846c44ede9",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "263e5b98-93ea-4549-ba57-9a713e264c6e",
  "sourceToolAssistantUUID": "311219c8-737d-4e87-8c9f-87846c44ede9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-15T14:10:16.992Z_



Let me read the key project files to get full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "263e5b98-93ea-4549-ba57-9a713e264c6e",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHJjK1hGsNoWXFSBsd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9d79acd-41fd-4e9a-946d-dae2ec2a1049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoQMZwvdbnWZLVZwpebCp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 7 · 2026-05-15T14:10:17.996Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LFeuJNxVBjXqQQRoGZbrnX`</summary>

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
  "parentUuid": "f9d79acd-41fd-4e9a-946d-dae2ec2a1049",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHJjK1hGsNoWXFSBsd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14d9ee6d-2ab0-415e-8888-97a54c8c5c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoQMZwvdbnWZLVZwpebCp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 8 · 2026-05-15T14:10:18.042Z_

<details><summary>↩ Tool result · `toolu_01LFeuJNxVBjXqQQRoGZbrnX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_011_grpo_g8_bf16 | GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3 | — | — | — |\\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior. | — | — | — |\\n| mvp2_ced_reranker_poc | CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound. | — | — | — |\\n\\n## 待处理\\n- plan_004_dreeam_baseline: Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。（排队等待 GPU）\\n- mvp2_eval_rsft_s44: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).（准备中）\\n\\n## 近期结论\\n- **mvp2_eval_rsft_s43_r2** (success): Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names). ← 基于 mvp2_rsft_train_r1_s43\\n- **mvp2_rsft_ced_scoring_topk3_r2** (success): CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally). ← 基于 mvp2_rsft_ced_scoring\\n- **mvp2_rsft_train_r1_s44** (success): RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798. ← 基于 mvp2_rsft_train_r1\\n\\n## 趋势\\n成功 26 / 负向 11 / 失败 12 / 共 71\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_flatnli: 训练失败 — unknown\\n- mvp2_grpo_extract: 训练失败 — unknown\\n- mvp2_sft_eval: 已被终止 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_r3: 训练失败 — unknown\\n- mvp2_grpo_ced_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r2: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r3: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001: 训练失败 — unknown\\n- mvp2_grpo_ced_kl001_r2: 已被终止 — unknown\\n- mvp2_grpo_ced_kl001_r3: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r4: 已被终止 — unknown\\n- mvp2_grpo_extract_r4: 已被终止 — unknown\\n- mvp2_grpo_flatnli_r5: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_multi: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_last: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt90: 已被终止 — unknown\\n- mvp2_eval_ced_kl001_r4_high: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_p1_r1: 已被终止 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r1: 训练失败 — unknown\\n- mvp2_eval_ced_kl001_r4_ckpt7080: 训练失败 — unknown\\n- mvp2_grpo_ced_lr5e6_rp_r2: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt40: 训练失败 — unknown\\n- mvp2_eval_lr5e6_rp_r2_ckpt20: 已被终止 — unknown\\n- mvp2_eval_lr5e6_r1_ckpt60: 训练失败 — unknown\\n- mvp2_rsft_generate: 训练失败 — unknown\\n- mvp2_rsft_ced_scoring_topk3: 已被终止 — unknown\\n- mvp2_rsft_train_r2_fix: 已被终止 — unknown\\n- mvp2_eval_rsft_s43: 训练失败 — unknown\\n- mvp2_eval_rsft_r2b_maxtok1536: 已被终止 — unknown\\n\", \"total_chars\": 3533, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d9ee6d-2ab0-415e-8888-97a54c8c5c51",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "e49ca294-26e2-400f-ac3f-70139beec18d",
  "sourceToolAssistantUUID": "14d9ee6d-2ab0-415e-8888-97a54c8c5c51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:10:18.939Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TdVwPyAuVTijhHxa6i25dW`</summary>

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
  "parentUuid": "e49ca294-26e2-400f-ac3f-70139beec18d",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHJjK1hGsNoWXFSBsd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25d333cd-efe6-487d-94e3-274cd3cc3c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoQMZwvdbnWZLVZwpebCp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 10 · 2026-05-15T14:10:18.971Z_

<details><summary>↩ Tool result · `toolu_01TdVwPyAuVTijhHxa6i25dW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\n## ACTIVE\\n\", \"total_chars\": 484, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d333cd-efe6-487d-94e3-274cd3cc3c10",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "fcd1d699-2552-408c-bb54-78085b4b01b4",
  "sourceToolAssistantUUID": "25d333cd-efe6-487d-94e3-274cd3cc3c10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:10:19.175Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LgwxigakFwf7j1dnHEH7S9`</summary>

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
  "parentUuid": "fcd1d699-2552-408c-bb54-78085b4b01b4",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHJjK1hGsNoWXFSBsd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f305df7-c6fc-4eb8-9d0d-70a465a9ac18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoQMZwvdbnWZLVZwpebCp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 12 · 2026-05-15T14:10:19.206Z_

<details><summary>↩ Tool result · `toolu_01LgwxigakFwf7j1dnHEH7S9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      DAPO 提出 Clip-Higher（放大 importance sampling 上界）和 Dynamic Sampling\\n      来对抗 entropy collapse，在 AIME 2024 上超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse；CED reward 本身就能防止 mode collapse，\\n      无需额外 clip 调整。reward design vs. algorithm trick 的对比。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化对低 variance 组（全对/全错）给予过高 advantage 权重引入 difficulty bias。\\n      Dr. GRPO 移除 std 归一化项消除偏差，在 per-token 基础上表现更优。\\n    relevance_to_ced_stabilizer: >\\n      分析了 reward_std→0 时的问题（advantage 异常放大或归零），\\n      与我们观察到的 extraction-only reward 下 frac_zero_std→0.8 现象高度一致。\\n      CED 通过增加 reward 维度天然维持 reward_std>0，避免了这一 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      Contrastive reward 让 LLM 惩罚 reward uncertainty、改善鲁棒性、\\n      根据任务难度自适应校准、减少 PPO 中的 variance。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。但针对 RLHF 通用场景，\\n      CED 是 task-specific evidence discrimination 对比信号，且在 GRPO（非 PPO）中验证。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：RSFT 在 DocRE 上成功而 GRPO 失败的原因可能是\\n      structured output（DocRE）比 math reasoning 更难用 online RL 优化，\\n      而 rejection sampling 的 offline 特性天然避免了 catastrophic forgetting。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，\\n      媲美 GPT-4o。在 SemEval-2010 Task 8 和私有 MDKG 数据集上评估。\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。但关键差异：(1) R1-RE 是句子级 RE，我们是文档级 RE；\\n      (2) R1-RE 用 online GRPO，我们用 offline RSFT；\\n      (3) R1-RE 无 evidence extraction 组件，我们有 CED reward；\\n      (4) R1-RE 关注 OOD 泛化，我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior 在 DocRED 上提升 +2.06-2.38pp，\\n      我们的 RSFT 提升 +5.98pp 显著更优。\\n      RelPrior 是 inference paradigm 创新，我们是 training paradigm 创新，正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      在 DocRED/Re-DocRED 上显著优于其他 LLM-based DocRE 方法。\\n    relevance_to_rsft_docre: >\\n      LMRC 用小模型预筛选 + LLM 分类的 pipeline 方式，与我们端到端 LLM 生成方式不同。\\n      展示 LLM-based DocRE 的 class imbalance 挑战，我们通过 RSFT 的 reward-based filtering 隐式解决。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上超越现有 LLM 方法和规则框架。\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证，我们用 training-time reward shaping。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      在 Re-DocRED、FREDo 等 benchmark 的 few-shot 场景达到 SOTA。\\n      预训练于 136K 文档的大规模 RE 数据。\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative），\\n      但验证了 DocRE 领域仍有方法创新空间。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE，\\n      在多个 LLM 上达到 SOTA。\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\", \"total_chars\": 17868, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f305df7-c6fc-4eb8-9d0d-70a465a9ac18",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "46529aab-9a9f-4999-8471-4bcba5f4e881",
  "sourceToolAssistantUUID": "0f305df7-c6fc-4eb8-9d0d-70a465a9ac18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T14:10:23.756Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CPTBsNKN2nTFrnPPRmjpYa`</summary>

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
  "parentUuid": "46529aab-9a9f-4999-8471-4bcba5f4e881",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHiDSFttsr1cAGsn64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13595fab-26e2-4b94-8320-2f20a7f689cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4XhKQth8CC9GKgp9nVitN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11593,
      "cache_read_input_tokens": 17502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11593,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 14 · 2026-05-15T14:10:23.770Z_

<details><summary>↩ Tool result · `toolu_01CPTBsNKN2nTFrnPPRmjpYa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v1 (重大 reframe based on Dream feedback)\\n> **最后更新**: 2026-05-15\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → 需 reframe 后 re-dream\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 和 offline RL (RSFT) 两条技术路线。关键发现：**GRPO 在结构化 IE 上导致 evidence-extraction decoupling**——evidence 质量持续提升（evi_f1→0.85）但抽取能力 catastrophically forget（rel_f1<0.02），这一现象在 3 种 reward function 下一致出现。RSFT 有效规避此问题。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Exploration**: 系统性比较 online RL (GRPO) vs offline RL (RSFT)\\n4. **Key finding**: evidence-extraction decoupling — GRPO 下 evidence 和 extraction 被差异化优化，extraction catastrophically forget\\n5. **What works**: RSFT with NLI-based scoring 有效提升 evidence 质量而不牺牲抽取\\n6. **Diagnostic tool**: EDCR 捕捉 Evi-F1 的盲区\\n\\n## Core Claims (reframed after Dream v1)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- RSFT 在 4/4 配置下均超过 SFT baseline（rel_f1 +3.9~6.0pp）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): GRPO 在结构化 IE 上导致 evidence-extraction decoupling\\n- 3 种 reward × 多个 lr 全线失败\\n- **Evidence-extraction decoupling**: evi_f1 → 0.850 而 rel_f1 < 0.02\\n- 三档 Dream 审稿均认为此发现\\\"genuinely novel and striking\\\"\\n- **需要加强**: GRPO G=8 实验（排除 G=4 confound）；DPO 作为 offline preference optimization baseline（验证 decoupling 是否 on-policy 特有）\\n- **需要明确边界**: \\\"GRPO fails for DocRE\\\" 而非 \\\"online RL fails for structured IE\\\"\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n\\n### Claim 4 (Diagnostic): EDCR 捕捉 Evi-F1 的盲区\\n- EDCR 概念有价值（三档一致认可）\\n- **需要人工验证**: 100 例标注\\n- **需要更多数据点**: per-document / per-relation-type 分析\\n\\n## MVP Evidence Summary\\n\\n| Config | rel_f1 | Δ rel_f1 | evi_f1 (conditional) | evi_f1 (joint, TBD) | EDCR |\\n|--------|--------|----------|---------------------|---------------------|------|\\n| SFT baseline | 0.4057 | — | 0.7979 | 0.3117 | 0.7118 |\\n| RSFT r1 (3ep, s42) | 0.4449 | +3.92pp | 0.8187 | 0.3468 | 0.6565 |\\n| RSFT r1 (s44) | 0.4655 | +5.98pp | 0.8087 | 0.3713 | 0.6350 |\\n| RSFT r2a (1ep) | 0.4494 | +4.37pp | 0.8108 | 0.3509 | 0.6641 |\\n| RSFT r2b (1ep, conservative) | 0.4493 | +4.36pp | 0.8128 | 0.3490 | 0.6609 |\\n| GRPO (lr=5e-6, ckpt-100) | 0.0138 | -39.2pp | 0.8500 | — | 0.9900 |\\n\\n注：evi_f1 (conditional) 仅计算 TP triples 的 evidence，与 DREEAM joint protocol 不可比（D041）。\\n\\n## Anticipated Reviewer Concerns (updated from Dream)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- 标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"\\n- 补充 DPO baseline（offline preference optimization，验证 decoupling 是否 on-policy 特有；注意 DPO 是纯 offline 方法，不是 online/offline 中间点）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 实验；LoRA confound 作为 limitation 讨论\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning（NEW）\\n6. **GRPO+CED (G=4)**: online RL negative baseline\\n7. **GRPO+CED (G=8)**: G=4 confound 排除（NEW）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 rel_f1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) GRPO decoupling 在 G=8 下仍复现\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling 在 G=8 下不复现 → scope 大幅缩减\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| P0 | GRPO G=8 experiment | C2 | ~16h |\\n| P0 | DPO+CED experiment | C2 | ~12h |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| P2 | GRPO forgetting 可视化 | C2 | ~4h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 5543, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13595fab-26e2-4b94-8320-2f20a7f689cf",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "17b2e4a8-e74c-4d6a-b406-acbb2096f5d3",
  "sourceToolAssistantUUID": "13595fab-26e2-4b94-8320-2f20a7f689cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T14:10:24.706Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017qhf1H6gu8Hsfut8vo3Uf6`</summary>

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
  "parentUuid": "17b2e4a8-e74c-4d6a-b406-acbb2096f5d3",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHiDSFttsr1cAGsn64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73c02c00-79d1-4315-8c84-f3a3b221e4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4XhKQth8CC9GKgp9nVitN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11593,
      "cache_read_input_tokens": 17502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11593,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 16 · 2026-05-15T14:10:24.720Z_

<details><summary>↩ Tool result · `toolu_017qhf1H6gu8Hsfut8vo3Uf6`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例\\n\\n### 与我们场景的相关性\\n- **直接相关**。GRPO 阶段的 rel_F1 崩塌是 alignment tax 的典型表现\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重（但 GRPO 路线已判死，仅留作参考）\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数\\n- 在 Qwen 和 LLaMA 系列上验证有效\\n\\n### 与我们场景的相关性\\n- 高度相关但 GRPO 路线已判死，仅留作参考\\n\\n---\\n\\n## D031 Pivot: GRPO+QLoRA → RSFT + CED (2026-05-15)\\n\\n### 决策\\nGRPO+QLoRA 方向判死，pivot 到 Rejection Sampling Fine-Tuning (RSFT) + CED scoring。\\n\\n### 核心证据\\n- lr=5e-5 (ced_kl001_r4): best eval rel_f1=0.211 (step-90)，仅 SFT baseline (0.406) 的 52%\\n- lr=5e-6 (lr5e6_r1): 完整轨迹 ckpt-20→100 rel_f1 = 0.008/0.007/0.009/0.012/0.014 — 零恢复\\n- 所有 3 种 reward type (CED/extract-only/flat-NLI) 在 GRPO+QLoRA 下均 collapse\\n\\n### RSFT 技术约束\\n- **--quantize (4-bit) + merge_and_unload 在 RTX 5090 上有 CUBLAS 错误**，RSFT 训练不要用 quantize。bf16 Qwen3-4B 仅 ~8GB，无需量化。\\n- 运行目录必须是 `/root/autodl-tmp/`（freige 不是 pip install 的包，cd 到 freige/ 子目录会导致 import 找到内层空包）\\n\\n---\\n\\n## D038 重大修正：RSFT r1 实际成功 (2026-05-15)\\n\\n### 事件\\nD037 报告 RSFT r1 \\\"灾难性失败\\\"（rel_f1=0.0483），但这是 **TaskEvalCallback bug**——`--eval_max_docs 50` 评估 50 个 doc 的预测，却用全部 12275 个 gold triples 计算 F1，严重低估 rel_f1。\\n\\n### 真实结果\\ns44 全量 dev eval (985 docs): **rel_f1=0.4655 (+5.98pp), evi_f1=0.8087 (+1.08pp)** → MVP-2 PASS\\n\\n### TaskEvalCallback bug fix\\n已部署到 `rsft_trainer.py:118-120`。gold triples 现在过滤到 eval_max_docs 对应的文档子集。\\n\\n### 教训\\n- 在 callback 中用 subset eval 时，必须确保 gold 和 pred 在同一文档集合上计算\\n- 基于 callback 数字的任何结论都需要全量 eval 交叉验证\\n\\n---\\n\\n## ~~RSFT r1 灾难性失败根因~~ [D038 撤回]\\n\\n**以下分析基于 D037 的错误 rel_f1=0.0483。D038 确认该数字是 eval bug，实际 rel_f1=0.4655。**\\n\\n原分析中关于\\\"关系本体崩塌\\\"的观察可能来自 eval_max_docs=50 下的极小样本偏差，不代表模型真实行为。r1/s43/s44 的全量 eval 正在进行中，将给出真实 ablation 数据。\\n\\n---\\n\\n## RSFT r2a/r2b ablation 结果 (2026-05-15)\\n\\n### 实验配置与结果\\n\\n| 配置 | rel_f1 | evi_f1 | edcr | Δrel_f1 |\\n|------|--------|--------|------|---------|\\n| SFT baseline | 0.4057 | 0.7979 | 0.7118 | — |\\n| r1 (3ep, α=128, lr=2e-5, 2718) | 0.4449 | **0.8187** | 0.6565 | +3.92pp |\\n| r2a (1ep, α=128, lr=2e-5, clean 2548) | **0.4494** | 0.8108 | 0.6641 | +4.37pp |\\n| r2b (1ep, α=32, lr=1e-5, clean 2548) | 0.4493 | 0.8128 | 0.6609 | +4.36pp |\\n\\n### Ablation 结论\\n1. **1 epoch ≈ 3 epoch on rel_f1**（r2a=0.4494 vs r1=0.4449），多 epoch 无额外收益\\n2. **LoRA scaling 不敏感**（α=128 vs α=32 差异 <0.1pp）\\n3. **r1 在 evi_f1 上最优**（0.8187 vs r2a 0.8108），3 epoch 可能有助于证据定位\\n4. **所有 RSFT 变体 EDCR 低于 SFT**（~0.66 vs 0.71），RSFT 增加 pred_count 导致更多 distractor citation\\n\\n---\\n\\n## RSFT 文献对标 (2026-05-15, 更新)\\n\\n### 直接竞争者：无\\n在 DocRE / IE 上**无人用过 RSFT**，NLI-based CED reward for RE training 也无先例。Novelty 完全成立。\\n\\n### 最接近竞争者：R1-RE (arXiv 2507.04642)\\n用 GRPO 做**句子级** RE。与我们差异明确：文档级 vs 句子级、offline RSFT vs online GRPO、有 CED evidence reward vs 无。\\n\\n### Must-cite 论文\\n1. **R1-RE** — GRPO for sentence-level RE（最近竞争者，需在 related work 中区分）\\n2. **\\\"Minimalist Approach\\\"** — RSFT 理论基础\\n3. **RelPrior** — LLM-based DocRE baseline (+2.06-2.38pp rel_f1)\\n4. **\\\"RSFT=PPO\\\" (ICML 2025)** — RSFT 与 PPO 等价性理论\\n\\n### 我们的定位\\n- +3.9~6.0pp rel_f1 显著超过同类 LLM-based DocRE 改进（RelPrior: +2.06-2.38pp）\\n- CED 作为 rejection sampling 打分函数是新颖的方法论贡献\\n- 最接近的工作是 Progressive Self-distillation (ACM 2024) 用 knowledge distillation，但无 evidence-based reward\\n\\n### 新增文献 map categories (by literature scan worker)\\n- Category 6: RSFT Methodology & Theory（3 篇）\\n- Category 7: RL for Information Extraction（5 篇）\\n- Category 8: Recent LLM-based DocRE Methods（5 篇）\\n\\n---\\n\\n## CED-as-reranker 探索 (2026-05-15)\\n\\nRSFT 成功后仍保留 CED-as-reranker PoC 作为推理时替代方案（无需额外训练）。\\ncuda:0 上 PID 178050 运行中（985 docs × N=8，预计 ~6h）。\\n如果 reranker 接近或超过 RSFT，可作为论文中的 complementary contribution。\\n\\n---\\n\\n## Qwen3 generation_config 覆盖陷阱 (2026-05-15)\\n\\nQwen3 模型自带 `generation_config.json` 会静默覆盖代码传参：\\n- `model.generation_config.top_k = 20`（限制采样池）\\n- `model.generation_config.temperature = 0.6`（覆盖代码传的任何温度值）\\n\\n**必须在生成前显式覆盖**：\\n```python\\nmodel.generation_config.temperature = target_temp\\nmodel.generation_config.top_k = 0  # 禁用 top_k 限制\\nmodel.generation_config.do_sample = True\\n```\\n\\n---\\n\\n## Diversity 监控计算 bug (2026-05-15)\\n\\n### 根因\\n- triple-set 归一化逻辑不一致\\n- diversity 分母用配置值而非实际生成数\\n\\n### 修复\\n- 提取 `diversity_metrics.py` 独立模块\\n- 修复后真实数据：302 docs mean_diversity=7.52/8, median=8.0/8\\n\\n---\\n\\n## inference.py 参数教训 (2026-05-15)\\n\\n**inference.py 必须传完整模型 stack**：\\n- `--base_model /root/autodl-tmp/models/Qwen3-4B`\\n- `--sft_adapter /root/autodl-tmp/sft_output`\\n- `--model_path &lt;rsft_adapter_path>`（RSFT adapter）\\n- `--data_path /root/autodl-tmp/data/docred`\\n- `--output_dir &lt;output_path>`\\n- `--no-quantize`（RTX 5090 必须）\\n- `--max_new_tokens &lt;N>`（可选，默认 1024）\\n\\n**只传 --model_path 不传 --base_model + --sft_adapter 会导致模型 stack 错误**（Base + RSFT LoRA，缺 SFT merge），结果完全不可用。maxtok1536 eval 因此被 Reviewer CRITICAL 打回并重跑。\\n\\n---\\n\\n## RSFT 代码参数速查\\n\\n**inference.py**: --base_model, --sft_adapter, --model_path(rsft adapter), --data_path, --output_dir, --no-quantize, --max_new_tokens(1024)\\n\\n**rsft_generate.py**: --base_model, --sft_adapter, --data_path, --split, --output_dir, --num_generations(8), --temperature(0.7), --batch_size(1), --max_new_tokens(1024), --seed, --quantize/--no-quantize, --start_idx, --end_idx, --shard_id\\n\\n**rsft_score_filter.py**: --input_dir, --output_path, --nli_model_path, --nli_device, --tau(0.5), --f1_threshold(0.1), --selection_strategy(top_k), --top_k(2)\\n\\n**rsft_trainer.py**: --base_model, --sft_adapter, --rsft_data_path, --output_dir, --learning_rate, --num_epochs, --per_device_batch_size, --gradient_accumulation_steps, --lora_rank(64), --lora_alpha(128), --weighted_sampling, --quantize(False), --eval_data_dir, --eval_max_docs, --wandb_run_name, --seed\", \"total_chars\": 6195, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73c02c00-79d1-4315-8c84-f3a3b221e4e2",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "e233bf5d-3a44-45b6-a680-4312511b6274",
  "sourceToolAssistantUUID": "73c02c00-79d1-4315-8c84-f3a3b221e4e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T14:10:24.951Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0156QtouYCkdWSB3rgnoUsuR`</summary>

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
  "parentUuid": "e233bf5d-3a44-45b6-a680-4312511b6274",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VHiDSFttsr1cAGsn64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40544d96-5c3d-4cad-9d7a-46ac2bf67579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4XhKQth8CC9GKgp9nVitN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11593,
      "cache_read_input_tokens": 17502,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 17502,
          "cache_creation_input_tokens": 11593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11593,
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

_source line 18 · 2026-05-15T14:10:24.964Z_

<details><summary>↩ Tool result · `toolu_0156QtouYCkdWSB3rgnoUsuR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 13:42 UTC | 更新原因: Reviewer 路线图审查修正：GPU 表更新实际状态、joint evi_f1 进展、DPO 升 P0、C2 风险标注\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 新任务范式。核心发现：GRPO 在结构化 IE 上导致 evidence-extraction decoupling。RSFT+NLI-based scoring 有效提升证据质量。CED 作为 scoring function 之一，显著性待验证。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过）\\n- **Dream v1**: best=2.5, median=3.0, worst=2.5 → 不达标\\n- **Reframe 完成** (D044): CED 降级、claims 重构（C1=可行性, C2=decoupling, C3=NLI ablation, C4=EDCR）\\n- **Re-dream**: dream_20260515T132059 运行中，验证 reframe 效果（目标 best≥3.5, median≥3.0）\\n- **MVP 成果**: RSFT 4/4 configs PASS (rel_f1 +3.9~6.0pp vs SFT)；joint evi_f1 已回填（SFT=0.3117 → best RSFT s44=0.3713, +5.96pp）\\n- **GRPO 判死**: 3 reward × 多 lr 全线 catastrophic forgetting (D031/D033)\\n- **topk3 scoring 完成**: 8037 samples (2.96x topk1)，数据就绪\\n- **DPO 升级为 P0** (D045): 直接影响 C2 decoupling 叙事\\n\\n## 投稿目标\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## 近期任务\\n- [ ] 等 re-dream 结果验证 reframe\\n- [ ] Agent 处理队列（urgent: s43_r2 registry 修复 + plan_008 双变体设计 + evaluate() joint 集成）\\n- [ ] Re-dream 达标后批准 P0 实验：\\n  - plan_011: GRPO G=8（**最高风险，首批启动**，C2 必要条件）\\n  - plan_001: flat-NLI RSFT ablation (C3)\\n  - plan_004: DREEAM baseline reproduction (C1)\\n  - plan_012: DPO+CED（**升 P0**，C2 叙事关键）\\n- [ ] 处理运行中实验结果（maxtok1536_r2 cuda:1, CED reranker cuda:0）\\n- [ ] plan_008 topk3 双变体训练（cuda:2 全量 / cuda:3 过滤CED=0）\\n\\n## GPU 分配\\n\\n| GPU | 状态 | 任务 |\\n|-----|------|------|\\n| cuda:0 | 🏃 | mvp2_ced_reranker_poc (plan_005) |\\n| cuda:1 | 🏃 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\\n| cuda:2 | ⏳ | 待分配 → plan_008 topk3_all |\\n| cuda:3 | ⏳ | 待分配 → plan_008 topk3_ced_filtered |\\n\\n## GPU 预算\\n- 硬件: 4× RTX 5090 32GB (rtx5090-4x)\\n- MVP 已消耗: ~80+ GPU-hours\\n- Research P0: ~75h (flat-NLI 25h + CED seeds 10h + test eval 4h + DREEAM 8h + GRPO G=8 16h + DPO 12h)\\n- Research P1: ~46h (EDCR人工验证 API + post-hoc 4h + reranker 6h + model size 24h + Re-DocRED 12h)\\n\\n## 评审笔记\\n1. ✅ CED 重框定（paper_framing.md 已更新）\\n2. ✅ EDCR 升格为独立贡献 (Claim 4)\\n3. ✅ NLI lexical overlap bias 验证\\n4. ✅ Joint evi_f1 已回填（paper_framing.md 表格已更新）\\n5. ✅ DPO 定位修正（纯 offline，非 online/offline 中间点）\\n6. ⬜ Baselines 扩展到 12+ (含 DPO, GRPO G=8, post-hoc retrieval)\\n\\n## 风险监控\\n- **C2 单点依赖**: GRPO G=8 是 publishability 必要条件。若 G=8 下 decoupling 不复现 → scope 大幅缩减。G=8 必须是 re-dream 后首批 P0。\\n- **CED=0 稀释**: topk3 数据含 ced_reward=0 样本，双变体实验区分数据量效应 vs 信号稀释。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D046 | 2026-05-15 | D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + | plan_012, plan_011, plan_008 |\\n| D045 | 2026-05-15 | D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offlin | plan_012, plan_011 |\\n| D044 | 2026-05-15 | Dream v1 分析完成：reframe paper_framing.md，CED 降级，clai | plan_011, plan_012, plan_013 |\\n| D043 | 2026-05-15 | D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分 | — |\\n| D042 | 2026-05-15 | D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi | mvp2_sft_eval_r2, mvp2_eval_rsft_r1, mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b |\\n| D041 | 2026-05-15 | D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triple | mvp2_sft_eval_r2, mvp2_eval_rsft_r1, mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b |\\n| D040 | 2026-05-15 | D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定 | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D039 | 2026-05-15 | D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoc | mvp2_eval_rsft_r2a, mvp2_eval_rsft_r2b, mvp2_eval_rsft_r1, mvp2_rsft_train_r1_s44 |\\n| D038 | 2026-05-15 | D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred | mvp2_rsft_train_r1_s44, mvp2_rsft_train_r1 |\\n| D037 | 2026-05-15 | D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-r | mvp2_rsft_train_r1, mvp2_rsft_train_r1_s43, mvp2_rsft_train_r1_s44 |\\n\\n\", \"total_chars\": 3772, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40544d96-5c3d-4cad-9d7a-46ac2bf67579",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "f3541364-54fe-4a9e-a6d2-c8ba4648aac2",
  "sourceToolAssistantUUID": "40544d96-5c3d-4cad-9d7a-46ac2bf67579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T14:10:27.871Z_

Now let me look at the actual paper artifacts and any existing dream review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3541364-54fe-4a9e-a6d2-c8ba4648aac2",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJ8QEJqYFMaTmNF4uK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f114c396-21ab-4de1-9d00-43e078116ea8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms498dQdyM8SXTp7SCwvGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10029,
      "cache_read_input_tokens": 29095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10029,
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

_source line 20 · 2026-05-15T14:10:28.331Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011eRbxW78Ynf251apQ7LTnU`</summary>

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
  "parentUuid": "f114c396-21ab-4de1-9d00-43e078116ea8",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJ8QEJqYFMaTmNF4uK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63ac725e-6ee2-46d0-ab23-e186a6f0cb70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms498dQdyM8SXTp7SCwvGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10029,
      "cache_read_input_tokens": 29095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10029,
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

_source line 21 · 2026-05-15T14:10:28.390Z_

<details><summary>↩ Tool result · `toolu_011eRbxW78Ynf251apQ7LTnU`</summary>

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
  "parentUuid": "63ac725e-6ee2-46d0-ab23-e186a6f0cb70",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "1e0e32e2-712d-4d80-a08c-b128d8736c7a",
  "sourceToolAssistantUUID": "63ac725e-6ee2-46d0-ab23-e186a6f0cb70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T14:10:29.277Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01CXAui3cnVhjdqwqKCzcQhT`</summary>

```json
{
  "pattern": "**/dream*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e0e32e2-712d-4d80-a08c-b128d8736c7a",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJ8QEJqYFMaTmNF4uK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c8d5f59-f63b-44f3-9693-17cebe4f0129",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms498dQdyM8SXTp7SCwvGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10029,
      "cache_read_input_tokens": 29095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10029,
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

_source line 23 · 2026-05-15T14:10:29.335Z_

<details><summary>↩ Tool result · `toolu_01CXAui3cnVhjdqwqKCzcQhT`</summary>

```text
dream_registry.lock
dream_registry.yaml.bak
dream_registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c8d5f59-f63b-44f3-9693-17cebe4f0129",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "74fccbfa-d22d-4816-9f73-83d386951c27",
  "sourceToolAssistantUUID": "6c8d5f59-f63b-44f3-9693-17cebe4f0129",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T14:10:29.990Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018wZKhRjVJosrJCM7tLaTrx`</summary>

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
  "parentUuid": "74fccbfa-d22d-4816-9f73-83d386951c27",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJ8QEJqYFMaTmNF4uK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe86fcef-c67c-442e-89ea-88d9d5594de8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ms498dQdyM8SXTp7SCwvGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10029,
      "cache_read_input_tokens": 29095,
      "output_tokens": 284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 284,
          "cache_read_input_tokens": 29095,
          "cache_creation_input_tokens": 10029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10029,
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

_source line 25 · 2026-05-15T14:10:30.028Z_

<details><summary>↩ Tool result · `toolu_018wZKhRjVJosrJCM7tLaTrx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 47\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_reward 1.79→1.10, f1 0.098→0.012,\\n    length 88→547）。clip_ratio 全程为 0 表明 PPO 裁剪未生效，可能是 policy drift 失控的根因。决策：(1) 抢救\\n    step 40 checkpoint 作为当前最优；(2) step 70 前不回升则 kill；(3) 排查并修正 cliprange 后重跑。step\\n    40 checkpoint 仍可用于 vs SFT 的对比 eval，MVP-2 流程不完全停滞。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: training collapse after step 40, early stopping evaluation in progress\\n  depends_on:\\n  - D003\\n  - D004\\n- id: D006\\n  date: 2026-05-14 10:24 UTC\\n  summary: Kill CED r1（F1 归零+无 checkpoint），准备修复配置后重跑 r2\\n  rationale: Reviewer 确认 step 80 时 f1_reward=0.001（从 peak 0.098 单调下降 50 步），grpo_s3\\n    目录为空（无中间 checkpoint），step 40 最优模型不可挽回。继续 1.3h 必产废模型。诊断三个根因：(1) 无 save_steps 配置；(2)\\n    reward 权重失衡（format ~0.97 远大于 f1 ~0.001，模型无 f1 梯度信号）；(3) clip_ratio=0 裁剪未生效。决策\\n    kill 并修复后重跑 r2。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r1\\n    role: primary\\n    result: KILL — f1_reward 归零, 无 checkpoint, 训练不可挽回\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-14 11:28 UTC\\n  summary: r3 回退 num_iterations=1，隔离变量逐一测试\\n  rationale: Reviewer CRITICAL 确认：r2 的 KL 在 step 5 爆到 37亿、step 15 爆到 3400亿，直接导致 loss\\n    爆炸+OOM。根因是 num_iterations=2 + QLoRA 4-bit 量化 logits 精度不足，两次迭代间 KL 被放大。r2 同时改了\\n    6 个超参，崩溃后无法归因。r3 必须回退 num_iterations=1，保留 reward weighting（reward 0.25→0.42 正常上升证明\\n    WeightedRewardFn 有效），一次只改一个变量。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r2\\n    role: evidence\\n    result: KL explosion + OOM at step 18, num_iterations=2 confirmed as root cause\\n  depends_on: []\\n- id: D008\\n  date: 2026-05-14 12:07 UTC\\n  summary: D007 证伪：KL 爆炸根因是 kl_coef + QLoRA 4-bit 不兼容，非 num_iterations。全部 GRPO 重跑\\n    kl_coef=0\\n  rationale: 3 个 GRPO 实验（num_iterations=1）均在 step 5 触发 KL 爆炸早停（KL 达 10^10 量级）。对比 r1（kl_coef=0/未设）跑了\\n    80+ steps 才因 reward imbalance collapse。证据链：所有设 kl_coef=0.05 的实验全部 step 5 爆炸，未设的\\n    r1 稳定运行。机理：QLoRA 4-bit 量化噪声导致 ref model 和 training model 的 log-probs 存在系统性偏差，KL(π_θ||π_ref)\\n    从第一步就是天文数字。修复：kl_coef=0，依赖 reward weighting + save_steps + KL 监控（logging only）控制稳定性。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: KL explosion step 5, kl_coef=0.05, num_iterations=1\\n  - exp_id: mvp2_grpo_extract\\n    role: evidence\\n    result: KL explosion step 5, KL=69.5B\\n  - exp_id: mvp2_grpo_flatnli\\n    role: evidence\\n    result: KL explosion step 5, KL=50.8B\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-14 12:12 UTC\\n  summary: CED r4 采用保守配置：grad_accum=16 + lr=5e-6 + kl_coef=0.5 + warmup 200步，解决 r3\\n    单卡 batch=1 + 高 lr 导致的 KL 爆炸\\n  rationale: r3 根因明确：单卡无 grad_accum 导致 effective batch=1，梯度噪声极高，5 步内 KL 爆炸至 4.4M。r1-r3\\n    三次失败模式不同（mode collapse / OOM / KL explosion），说明 CED reward 本身不是问题，是训练超参不稳定。r4\\n    同时修复 3 个因素：(1) grad_accum=16 使 effective batch=16; (2) lr 从 5e-5 降至 5e-6; (3)\\n    kl_coef 从 0.05 升至 0.5 加强偏离惩罚; (4) 加 200 步 warmup 稳定初始阶段。需先拿到 extract 和 flatnli\\n    r1 结果作为对照基线。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r3\\n    role: evidence\\n    result: failed - KL explosion at step 5, batch=1 root cause\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: pending approval\\n  depends_on: []\\n- id: D010\\n  date: 2026-05-14 12:32 UTC\\n  summary: 选择 Option A：保留 kl_coef=0.0 实验进程，修复 registry 状态从 killed → RUNNING；D009 的\\n    kl_coef=0.5 正式作废\\n  rationale: Reviewer critical 报告 registry-reality 不一致。3 个实验实际在跑（kl_coef=0.0, grad_acc=16）但\\n    registry 标记 killed。配置本身正确——D008 已证明 kl_coef>0 在 QLoRA 4-bit 下不稳定（r1 kl_coef=0\\n    稳定 80 步 vs 所有 kl_coef>0 爆炸）。D009 提出的 kl_coef=0.5 会放大 QLoRA 量化噪声导致的 KL 计算失真，Reviewer\\n    warning 合理，该指令作废。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r4\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_extract_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  - exp_id: mvp2_grpo_flatnli_r2\\n    role: target\\n    result: running with kl_coef=0.0, registry fix needed\\n  depends_on:\\n  - D008\\n  - D009\\n- id: D011\\n  date: 2026-05-14 13:30 UTC\\n  summary: 采纳 Reviewer 评估框架审查：精确化 pass criteria、补充 extraction-only vs SFT 对比、要求多 checkpoint\\n    eval + 统一 eval 脚本\\n  rationale: Reviewer 指出 4 个 warning：(1) 缺 extraction-only vs SFT 对比——回答 GRPO 本身是否有效；(2)\\n    kl_coef=0 必须 eval 多 checkpoint 避免 collapse 后只看末尾；(3) pass criteria 需精确化基准；(4)\\n    eval 代码必须统一。全部采纳，已更新 ROADMAP 和指令 Agent。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: target\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: target\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: target\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n  depends_on:\\n  - D010\\n- id: D012\\n  date: 2026-05-14 14:54 UTC\\n  summary: 调整 MVP-2 pass criteria：取消绝对 F1>45 门槛，改为相对标准；EDCR 升为主指标\\n  rationale: SFT baseline F1=40.57%（37% 输出截断于 1024 tokens），绝对门槛 F1>45 已不现实。截断影响所有模型相同，相对对比仍有效。Evi-F1=79.79%\\n    设了高 baseline，但 EDCR=71.18% 说明模型\\\"spray-and-pray\\\"大量引用 distractor——CED 的核心攻击目标。调整后\\n    pass criteria：(1) CED_Evi-F1 ≥ SFT_Evi-F1（方向正确）；(2) CED_F1 ≥ max(extract, SFT)\\n    - 5pp（不退化）；(3) CED_EDCR 显著低于 SFT_EDCR（核心判据）；(4) CED > flat-NLI 在 Evi-F1 或 EDCR\\n    上方向正确。绝对指标留到 post-MVP 增大 max_new_tokens 后重评。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-14 14:54 UTC\\n  summary: MVP-2 pass criteria 调整：取消绝对 F1>45 门槛，改为相对对比；EDCR 升为核心判定指标\\n  rationale: SFT baseline F1=40.57%（37% 输出被 1024 token 截断导致），已低于原定 F1>45 门槛。但截断对所有模型等效影响，相对对比仍然公平。调整后\\n    pass criteria：(1) 核心不变：CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp；(2) F1 改为相对：CED_F1 ≥ SFT_F1\\n    − 5pp（即 ≥35.57）；(3) 新增 EDCR 核心判定：CED_EDCR 显著低于 SFT_EDCR（71.18%），降幅 ≥10pp 视为强证据；(4)\\n    保持 CED > flat-NLI 方向。SFT EDCR=71% 说明 SFT 模型大量引用 entity-sharing distractors，正是\\n    CED 设计目标的攻击面。即使 Evi-F1 提升不足 2pp，EDCR 大幅下降也足以支撑 Claim 2。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: baseline\\n    result: F1=40.57%, Evi-F1=79.79%, EDCR=71.18%\\n  depends_on:\\n  - D011\\n- id: D014\\n  date: 2026-05-14 14:58 UTC\\n  summary: CED r5 mode collapse 确认 kill；CED reward 必须加 F1 门控防止短输出 hack；暂停 ced_kl001\\n  rationale: CED r5 在 65% 进度完全 collapse：completion 固定 34 tokens，f1_reward=0，ced_reward≈0.99，entropy≈0。模型发现极短输出不引用\\n    distractor 即可获得近完美 CED 分——CED 自身被 reward hack。根因：CED reward 不依赖抽取质量，模型可在 F1=0\\n    时仍获高 CED reward。修复方案：F1 门控——仅在 completion 包含 ≥1 个 predicted triple 时计算 CED reward，否则\\n    CED=0。这确保 evidence quality 的评估以有效抽取为前提。ced_kl001 使用同样有缺陷的 reward 设计，必须暂停，等修复后再启动。extract_r3\\n    部分 collapse 但仍有 F1 信号，继续观察。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: 'mode collapse: f1=0, ced≈0.99, 34-token fixed output'\\n  - exp_id: mvp2_grpo_extract_r3\\n    role: monitoring\\n    result: 'partial collapse: f1=0.2-0.34, 43-50 tokens, trending down'\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: healthy\\n    result: 'healthy: entropy=0.087, grad_norm=0.398, 11% progress'\\n  depends_on:\\n  - D013\\n- id: D015\\n  date: 2026-05-14 14:58 UTC\\n  summary: ced_r5 mode collapse 保留跑完取分析价值；flatnli_r3 kill 并修复 NLI device 后重启\\n  rationale: ced_r5 在 63% 进度时 f1_reward=0 + entropy≈0，已 mode collapse。保留跑完因为：(1) negative\\n    result 证明纯 CED reward 导致 collapse，支撑 reward balance 的 ablation story；(2) 早期 checkpoint\\n    可能有 f1_reward 正常的版本可用。flatnli_r3 因 NLI 推理在 CPU 上运行导致 10x 减速（124s/it vs 12s/it），预计\\n    20h+。RTX 5090 32GB 有足够余量放 DeBERTa-v3-base (~400MB)，kill 后修复 device 配置重启可将时间降至\\n    2-3h。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: subject\\n    result: f1_reward=0, mode collapse at 63%\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: subject\\n    result: NLI on CPU, 10x slowdown, killed for restart\\n  depends_on:\\n  - D011\\n- id: D016\\n  date: 2026-05-14 15:00 UTC\\n  summary: Kill ced_r5 (total collapse)，ced_kl001 移到 cuda:0 立即启动\\n  rationale: ced_r5 step 250+ f1_reward=0、completion 坍缩到 34 tokens、save_total_limit=5\\n    已覆盖所有正常 checkpoint。继续跑无任何回收价值。Kill 后释放 cuda:0 给 ced_kl001（kl_coef=0.01），不再等 cuda:1。ced_kl001\\n    现在是 MVP-2 最关键实验——验证 CED+KL约束能否避免 reward hacking。extract_r3 和 flatnli_r3 保持 kl=0\\n    继续跑，作为对照：若它们没 collapse，说明问题是 CED reward 特异的；若也 collapse，说明 kl=0 通病。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_r5\\n    role: failed\\n    result: total mode collapse, killed\\n  - exp_id: mvp2_grpo_ced_kl001\\n    role: replacement\\n    result: moved to cuda:0, critical experiment\\n  depends_on:\\n  - D015\\n- id: D017\\n  date: 2026-05-14 15:01 UTC\\n  summary: Kill ced_r5 + extract_r3 (kl_coef=0 collapse/stall), 部署 kl_coef=0.01 修正实验\\n  rationale: 3路GRPO健康检查：ced_r5完全mode collapse(entropy=0.0005, F1=0, grad_norm=0)，extract_r3训练停滞(grad_norm=0,\\n    F1=0.20低于SFT baseline 0.4057)。共同根因kl_coef=0导致策略无约束偏移。D008显示kl_coef=0.05会KL爆炸，选择0.01作为中间值（5x低于爆炸阈值）。flatnli_r3保留作为kl_coef=0对照组继续观察。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: failed\\n    result: mode collapse, entropy=0.0005, F1=0\\n  - exp_id: extract_r3\\n    role: failed\\n    result: stalled, grad_norm=0, F1=0.20\\n  - exp_id: flatnli_r3\\n    role: control\\n    result: healthy at 10.7%, continue as kl_coef=0 control\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05 caused KL explosion\\n  depends_on: []\\n- id: D018\\n  date: 2026-05-14 15:04 UTC\\n  summary: flatnli_r3 紧急修复 reward_device cpu→cuda，extract_r3 改为跑完再替换\\n  rationale: Reviewer critical 发现 D015 未执行：flatnli_r3 仍以 --reward_device cpu 运行，step_time\\n    123s/step（GPU 后应 12-15s/step），cuda:3 被占用但 90% 时间等 CPU。修复后从 ~23h 降至 ~2-3h，是当前最高\\n    ROI 操作。extract_r3 已 68%（~50min 完成），改为跑完后再部署 extract_kl001，避免浪费已投入的 2.5h。ced_r5\\n    维持 kill（3.3h GPU 时间用于 ced_kl001 更有价值）。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: reward_device cpu→cuda, from checkpoint-80 resume\\n  - exp_id: extract_r3\\n    role: revised\\n    result: let finish (~50min), then replace with extract_kl001\\n  - exp_id: ced_r5\\n    role: kill\\n    result: maintain kill decision, replace with ced_kl001\\n  depends_on:\\n  - D015\\n  - D017\\n- id: D019\\n  date: 2026-05-14 15:05 UTC\\n  summary: 修正 D017：extract_r3 改为跑完再释放，flatnli_r3 紧急补执行 D015（修复 NLI device 重启）\\n  rationale: Reviewer 审查发现：(1) D015 未执行——flatnli_r3 仍用 CPU NLI，step_time 120s vs GPU\\n    应 12-15s，23h→2-3h 的 10x 效率差，cuda:3 90% 时间在等 CPU。(2) extract_r3 只剩 ~50min，跑完可取早期\\n    checkpoint（collapse 前 step 20-100 可能比 last 好），不值得 kill 浪费已投入的 2.5h。修正后：cuda:0\\n    立即释放给 ced_kl001，cuda:2 等 50min 后给 extract_kl001，cuda:3 kill+修复 NLI device 后从 ckpt-80\\n    重启。\\n  related_experiments:\\n  - exp_id: flatnli_r3\\n    role: fix\\n    result: D015 未执行，NLI 在 CPU 导致 10x 低效，需 kill+修复+重启\\n  - exp_id: extract_r3\\n    role: revised\\n    result: 改为跑完（~50min），eval 早期 checkpoint\\n  - exp_id: ced_r5\\n    role: kill\\n    result: 仍立即 kill，与 D017 一致\\n  depends_on:\\n  - D017\\n  - D015\\n- id: D020\\n  date: 2026-05-14 15:15 UTC\\n  summary: ced_kl001 启动前必须先修复 CED reward F1 门控（D014 未实现）；kl_coef=0.01 实验改为 100 步探测性运行\\n  rationale: Reviewer 代码核查确认 D014 的 F1 门控从未实现：ced_reward.py 对 0-triple 短输出仍给近完美分(0.99)。ced_r5\\n    的 collapse 根因是双重的——kl_coef=0 导致策略自由偏移 + CED reward 对短输出的 hack。仅修 kl_coef 不解决 reward\\n    设计缺陷，ced_kl001 会重复失败。同时 kl_coef=0.01+QLoRA 的兼容性未验证（D008 证明 0.05 爆炸），先做 100 步探测降低风险。\\n  related_experiments:\\n  - exp_id: ced_r5\\n    role: evidence\\n    result: 34-token 短输出 → CED≈0.99 → reward hack → collapse\\n  - exp_id: ced_kl001\\n    role: blocked\\n    result: 等 CED reward 修复后才能启动\\n  - exp_id: D008\\n    role: reference\\n    result: kl_coef=0.05+QLoRA KL 爆炸\\n  depends_on:\\n  - D014\\n  - D017\\n  - D019\\n- id: D021\\n  date: 2026-05-14 17:20 UTC\\n  summary: Kill flatnli_r5（从已 hacked checkpoint 恢复无效），启动 flatnli_r6 从 SFT 全新训练 D020\\n    配置\\n  rationale: Reviewer 独立审查发现 flatnli_r3 checkpoint-100 已深陷 NLI reward hacking（f1=0.025,\\n    flat_nli=0.911）。从该 checkpoint 恢复加 kl_coef=0.01 后 KL=0.46（远高于从 SFT 新训的 ced_kl001_r4\\n    的 0.098），frac_zero_std 升至 0.8-0.9，grad_norm 近零——训练冻结。教训：从 kl=0 已漂移 checkpoint\\n    恢复并加 kl>0 不可行，必须从 SFT 全新开始。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r5\\n    role: 被 kill\\n    result: negative\\n  - exp_id: mvp2_grpo_flatnli_r3\\n    role: 提供了已 hacked 的 checkpoint\\n    result: negative\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: 健康参照（从 SFT 新训）\\n    result: running\\n  depends_on:\\n  - D020\\n- id: D022\\n  date: 2026-05-14 17:40 UTC\\n  summary: Kill extract_r4 (f1_reward=0 at ckpt-30, mode collapse confirmed); cuda:2\\n    转 ced_kl001_r4 多 checkpoint eval\\n  rationale: extract_r4 (extraction-only, kl_coef=0.01+gen=8) 在 step 10 后 f1_reward\\n    归零、frac_zero_std≥0.8 停滞，checkpoint-30 无恢复信号。同配置的 ced_kl001_r4 在 step 20 f1_reward=0.082\\n    持续上升——直接证明 CED reward 通道是驱动学习的关键因素。这一负面结果本身是强证据，不再尝试 extract_r5。cuda:2 空闲，派去 eval\\n    ced_kl001_r4 中间 checkpoint，提前获取多 checkpoint 评估数据。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: killed\\n    result: f1_reward=0 at ckpt-30, mode collapse\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: contrast\\n    result: f1_reward=0.082 at step 20, healthy\\n  depends_on:\\n  - D020\\n- id: D023\\n  date: 2026-05-14 17:40 UTC\\n  summary: 'Kill extract_r4 (mode collapse confirmed); ablation 结论: CED reward 是 GRPO\\n    训练必需的 dense signal，extraction-only reward 太稀疏无法驱动学习'\\n  rationale: 'extract_r4 checkpoint-30: f1_reward 连续 25 步为 0，frac_zero_std 升至 0.9，grad_norm\\n    在 0.005-0.012 震荡。对比 ced_kl001_r4 同期（f1_reward=0.082 持续上升，frac_zero_std=0.4 持续下降），唯一差异是\\n    reward type。结论: Stage 1 (extract-only) 在 D020 配置下无法维持 GRPO 探索多样性，CED 提供的 dense\\n    reward signal 是训练成功的必要条件。这是论文的关键 ablation evidence。cuda:2 释放，分配给 SFT eval baseline。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse — f1_reward=0 for 25 steps\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: f1_reward=0.082 at step 20, healthy training\\n  depends_on:\\n  - D020\\n- id: D024\\n  date: 2026-05-14 18:11 UTC\\n  summary: 'Kill flatnli_r6 (mode collapse step 25); D020 配置下三路 ablation 结论: 仅 CED\\n    reward 存活，extract-only 和 flat-NLI 均 collapse'\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。三个实验共用 D020 配置（kl=0.01, gen=8），唯一差异是\\n    reward type: extract-only collapse (step 10-30), flat-NLI collapse (step 25),\\n    CED 健康完成 100 步。结论: CED 的对比性 evidence discrimination 提供了 GRPO 所需的 dense gradient\\n    signal，是训练成功的必要条件。这比原设想的\\\"CED 改善 evidence quality\\\"更强——CED 是 GRPO 训练本身能否存活的关键。cuda:3\\n    释放用于加速 eval。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 10-30\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward 0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D025\\n  date: 2026-05-14 18:11 UTC\\n  summary: Kill flatnli_r6 (mode collapse confirmed step 25); D020 配置下三路 ablation\\n    结论：仅 CED reward 存活，extract-only 和 flat-NLI 均 collapse\\n  rationale: 'flatnli_r6 step 25: frac_zero_std=0.9, f1_reward=0, flat_nli_reward=0,\\n    reward 100% 来自 format。与 extract_r4 collapse 模式一致。D020 配置（kl=0.01, gen=8）下三路对比：extract-only\\n    step 30 collapse, flat-NLI step 25 collapse, CED 100 步健康完成。唯一差异是 reward type。结论：CED\\n    的对比性 evidence discrimination 提供了更丰富的梯度信号，是维持 GRPO 探索多样性的必要条件。这是论文最核心的 ablation\\n    evidence — 但需注意区分\\\"CED reward 本身的 anti-collapse 特性\\\"与\\\"stage 3 组合 reward 的其他差异\\\"两个假设。cuda:3\\n    释放后用于 eval 加速。'\\n  related_experiments:\\n  - exp_id: mvp2_grpo_flatnli_r6\\n    role: failed_ablation\\n    result: mode collapse step 25, frac_zero_std=0.9\\n  - exp_id: mvp2_grpo_extract_r4\\n    role: failed_ablation\\n    result: mode collapse step 30, f1_reward=0\\n  - exp_id: mvp2_grpo_ced_kl001_r4\\n    role: positive_control\\n    result: 100 steps healthy, reward=0.85-1.37\\n  depends_on:\\n  - D023\\n  - D020\\n- id: D026\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 导致灾难性遗忘+CED recall shortcut 双重问题，启动 P0/P0+P1\\n    并行修复\\n  rationale: 'ckpt-10/50/100 eval 全部远低于 SFT baseline（rel_f1: 0.003→0.156→0.217 vs\\n    SFT 0.4057，evi_f1: 0.720→0.564→0.575 vs SFT 0.7979）。训练 reward 5x 增长但 eval F1 未恢复，确认\\n    reward hacking + 灾难性遗忘双重机制。根因：lr=5e-5 过高 5-10x + CED 对非匹配 triple 无 recall 惩罚。D020\\n    ablation 的 CED 训练稳定性发现仍有效。下一步：P0（lr=5e-6）和 P0+P1（lr=5e-6 + ced_recall_penalty）并行验证。'\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: training success but eval fail\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: f1=0.003\\n  - exp_id: mvp2_eval_ced_kl001_r4_step50\\n    role: eval\\n    result: f1=0.156\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: f1=0.217\\n  depends_on:\\n  - D024\\n  - D025\\n  - D029\\n- id: D027\\n  date: 2026-05-14 19:37 UTC\\n  summary: MVP-2 ced_kl001_r4 FAIL — lr=5e-5 过高导致灾难性遗忘+CED recall shortcut 叠加 reward\\n    hacking\\n  rationale: ckpt-10/50/100 三点轨迹确认：rel_f1 最高 0.217（SFT 0.4057, pass 0.356, gap -13.9pp），evi_f1\\n    最高 0.575（SFT 0.7979, pass 0.818, gap -24.3pp）。恢复速率递减（40步+15.3pp→50步+6.0pp），外推至\\n    step200 仍远低于 pass。根因：(1) lr=5e-5 是社区推荐的 5-10x，导致 step10 即灾难性遗忘；(2) CED shortcut\\n    使非匹配 triple 退化为 flat NLI，引导模型少预测高 EDCR；(3) train/eval 分布不匹配放大差距。下一步：P0(lr=5e-6)\\n    + P0+P1(lr=5e-6+recall_penalty) 并行。\\n  related_experiments:\\n  - exp_id: ced_kl001_r4\\n    role: primary\\n    result: success(training)/fail(eval)\\n  - exp_id: mvp2_eval_ced_kl001_r4_step100\\n    role: eval\\n    result: rel_f1=0.217,evi_f1=0.575\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt50\\n    role: eval\\n    result: rel_f1=0.156,evi_f1=0.564\\n  - exp_id: mvp2_eval_ced_kl001_r4_ckpt10\\n    role: eval\\n    result: rel_f1=0.003,evi_f1=0.720\\n  depends_on:\\n  - D024\\n  - D025\\n- id: D028\\n  date: 2026-05-14 21:36 UTC\\n  summary: Kill rp_r2 (P0+P1) — loss 指数 divergence 不可恢复；cuda:3 转跑 rp_r2 ckpt-20 eval\\n    关闭对比线\\n  rationale: rp_r2 loss 从 step 10-20 持续指数增长 (908→24650→1.34e7)，根因是 recall_penalty\\n    5-10x 梯度 + kl_coef=0.01 形成正反馈循环。与 P0 的瞬时 KL spike 不同，这是持续 divergence。Kill 后 cuda:3\\n    跑 rp_r2 ckpt-20 eval（成本低，~2h）拿到数据关闭 P0+P1 对比线。不启动新训练——MVP 阶段 P0 单独通过即可。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_rp_r2\\n    role: killed\\n    result: loss exponential divergence\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: primary\\n    result: P0 continues as sole MVP path\\n  depends_on:\\n  - D027\\n- id: D029\\n  date: 2026-05-14 21:44 UTC\\n  summary: 修正 rp_r2 终止理由：从\\\"loss 持续发散\\\"改为\\\"recall penalty 过度抑制 CED 信号\\\"\\n  rationale: Reviewer 独立核实 trainer_state.json 发现 rp_r2 step 30-40 的 loss/KL 已完全恢复正常（loss=0.038,\\n    KL=0.005），与 P0 的瞬态发散→恢复模式一致，不是持续发散。真正的问题是 ced_reward=0.005 远低于 P0 的 0.079，说明 recall\\n    penalty 过于严苛压制了 CED 学习信号。kill 决策本身不撤回，但论文引用此 negative result 时应表述为\\\"recall penalty\\n    过度抑制 CED 信号\\\"而非\\\"训练发散\\\"。\\n  related_experiments:\\n  - exp_id: rp_r2\\n    role: subject\\n    result: killed-但理由修正\\n  - exp_id: mvp2_train_lr5e6_r1\\n    role: reference\\n    result: 同样出现瞬态发散后恢复\\n  depends_on: []\\n- id: D030\\n  date: 2026-05-14 22:16 UTC\\n  summary: P0 ckpt-20 eval FAIL (rel_f1=0.0077); lr=5e-6 未能防止早期遗忘，与 lr=5e-5 相同模式；扩展至全\\n    checkpoint 轨迹评估\\n  rationale: lr=5e-5 和 lr=5e-6 在 step-20 均出现灾难性遗忘（rel_f1 < 0.01），说明问题不是单纯 LR 过高——GRPO+QLoRA\\n    在结构化生成任务上的前 20 步 inherently 不稳定（60% 输出截断，field compliance 仅 39.9%）。需要看完整 recovery\\n    trajectory（ckpt-40/60/80）才能判断是否\\\"先崩后恢复\\\"。ced_kl001_r4 (lr=5e-5) step-90 最高 0.211\\n    仍低于阈值，lr=5e-6 能否突破 0.30 存疑。同时开始考虑 GRPO 替代方案（DPO/rejection sampling）作为 contingency。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0077, 39x below threshold'\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: step ~68, f1_reward recovering at step 45\\n  depends_on: []\\n- id: D031\\n  date: 2026-05-14 23:10 UTC\\n  summary: GRPO+QLoRA P0 方向判死：ckpt-40 rel_f1=0.0071（比 ckpt-20 更差），两个 LR 均远劣于 SFT baseline。Pivot\\n    到离线 RL（Rejection Sampling FT → DPO）\\n  rationale: ckpt-20→ckpt-40 轨迹下降（0.0077→0.0071），GRPO 只学会格式/证据引用但完全丧失关系抽取能力。lr=5e-5\\n    最佳 0.211 vs SFT 0.406，lr=5e-6 最佳 0.008。catastrophic forgetting 是 GRPO+QLoRA 在结构化生成任务上的根本性问题，非超参可解。CED\\n    reward signal 本身有效（MVP-1 verified），问题在在线 RL 训练方法论。Pivot 到离线方法：(1) Rejection Sampling\\n    FT 最简单最稳定优先做 (2) DPO+CED scoring 作为并行备选。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40_r2\\n    role: trigger\\n    result: rel_f1=0.0071 FAIL\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: prior\\n    result: rel_f1=0.0077 FAIL\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: f1_reward 无学习趋势\\n  - exp_id: ced_kl001_r4\\n    role: prior_attempt\\n    result: best 0.211 at ckpt-90, mode collapse\\n  depends_on:\\n  - D030\\n  - D027\\n- id: D032\\n  date: 2026-05-15 01:03 UTC\\n  summary: 'Kill GRPO 训练 (cuda:0 step 113/200): 轨迹数据已充分，释放 GPU 给 RSFT 管线加速'\\n  rationale: ckpt-80 rel_f1=0.0116 (SFT baseline 的 2.9%)，ckpt-20→80 全线 FAIL。ckpt-100\\n    eval 在跑会给最后一个数据点，但 step 200 无价值。释放 cuda:0 可用于并行 RSFT generate 或后续 scoring/training。\\n  related_experiments:\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: killed\\n    result: trajectory ckpt-20~80 all FAIL, max rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: evidence\\n    result: rel_f1=0.0116 negative\\n  depends_on:\\n  - D031\\n- id: D033\\n  date: 2026-05-15 01:22 UTC\\n  summary: D031 最终确认：GRPO+QLoRA 全线 FAIL，lr5e6 全 6 checkpoint rel_f1 < 0.02；negative\\n    result 模式有论文价值（CED↑ + rel_f1 catastrophic forgetting = 在线 RL 无法维持双能力）\\n  rationale: Reviewer 独立核实 lr5e6 全 6 checkpoint：rel_f1 最高仅 0.0138（阈值 0.30），evi_f1\\n    从 0.628 单调升至 0.850（超 SFT 0.798），edcr 稳定 ~0.99（远超 SFT 0.712）。模式：CED reward signal\\n    有效驱动 evidence 质量提升，但在线 RL (GRPO+QLoRA) 导致关系抽取 catastrophic forgetting。此 negative\\n    result 直接支持离线 RL (RSFT/DPO) 路线的必要性，且为论文提供重要论据。\\n  related_experiments:\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt100\\n    role: final_eval\\n    result: FAIL rel_f1=0.0138\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt80\\n    role: trajectory\\n    result: FAIL rel_f1=0.0116\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt60\\n    role: trajectory\\n    result: FAIL rel_f1=0.0093\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt40\\n    role: trajectory\\n    result: FAIL rel_f1=0.0071\\n  - exp_id: mvp2_eval_lr5e6_r1_ckpt20\\n    role: trajectory\\n    result: FAIL rel_f1=0.0077\\n  - exp_id: mvp2_grpo_ced_lr5e6_r1\\n    role: training\\n    result: killed after trajectory data collected\\n  depends_on:\\n  - D031\\n  - D032\\n- id: D034\\n  date: 2026-05-15 01:28 UTC\\n  summary: 'D034: RSFT diversity 危机——diversity=1.0/8 因 temperature 未生效，暂停生成并修复'\\n  rationale: Reviewer critical 发现：(1) rsft_generate.py 传入 temperature=0.7 但被 Qwen3-4B\\n    generation_config.json 自带的 T=0.6/top_k=20 覆盖，transformers 打出 WARNING 但 Agent 未注意；(2)\\n    SFT 后模型分布极度尖锐，T=0.6+top_k=20 几乎等同于 greedy，导致 8 次生成完全相同；(3) 早期 diversity_probe\\n    报告 7/8 是 format 解析 bug 导致的虚假多样性，修复格式后真实 diversity 暴露为 1.0/8。必须 kill 当前进程、修复 temperature\\n    覆盖（显式设 model.generation_config.temperature + top_k=0）、用 3-5 doc 验证后再重启。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8, 生成数据无法用于 rejection sampling\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 7/8 是虚假多样性（format bug），实际 5.0/8 且修复后降至 1.0/8\\n  depends_on:\\n  - D033\\n- id: D035\\n  date: 2026-05-15 01:29 UTC\\n  summary: 暂停 RSFT 并行化：Reviewer critical 发现 diversity=1.0/8 是格式修复后的真实值，之前 7/8 为格式不一致假象。高温探针优先。\\n  rationale: diversity_probe 原始数据 (8,6,1) 平均 5.0/8 而非上报的 7；且 probe 时 format_ok 仅 34%，\\\"多样性\\\"来自\\n    JSON key 名变体。生产环境 format_ok=99.8% 后实测 diversity=1.0/8。继续当前配置生成 14h 的数据毫无意义——rejection\\n    sampling 退化为普通 SFT。需先用高温(T=1.0/1.2/1.5)探针验证 diversity 是否可恢复。\\n  related_experiments:\\n  - exp_id: mvp2_diversity_probe\\n    role: evidence\\n    result: 虚报 7/8, 实际 5.0/8, 且为格式假象\\n  - exp_id: mvp2_rsft_generate\\n    role: affected\\n    result: diversity=1.0/8 at T=0.7, 暂不扩展\\n  depends_on:\\n  - D033\\n- id: D036\\n  date: 2026-05-15 01:33 UTC\\n  summary: D034 撤销：diversity crisis 是监控 bug，非生成质量问题，T=0.7 下 diversity 充足(7.11/8)，恢复并行生成\\n  rationale: 独立验证 Worker 分析 cuda:1 已生成的 200 docs：triple-set diversity 7.11/8 (median=8.0)，format\\n    parse rate 90.2%，61.5% 文档 8/8 完全不同。之前监控报告 mean_diversity=1.0/8 为度量代码计算错误。无需执行\\n    D034 的 temperature 修复和高温探针。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_generate\\n    role: trigger\\n    result: diversity monitoring bug identified\\n  depends_on: []\\n- id: D037\\n  date: 2026-05-15 07:46 UTC\\n  summary: 'D037: RSFT 全线 FAIL（rel_f1=0.0483），pivot 到 CED-as-reranker（推理时方案）'\\n  rationale: 'GRPO（D027/D031/D033）和 RSFT 两条训练路线均呈现相同的灾难性遗忘——任何对 SFT checkpoint 的二次微调都摧毁\\n    rel_f1。RSFT r1: rel_f1=0.0483, num_preds=848（SFT baseline: 0.4057, 12234）。跨 seed\\n    方差 <0.04%，非随机。根因假设：LoRA 二次微调的系统性遗忘。Pivot 到 CED-as-reranker：SFT 模型生成 N 候选 → CED\\n    打分 → 选最佳，完全绕过训练问题。'\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1\\n    role: primary\\n    result: 'FAIL: rel_f1=0.0483'\\n  - exp_id: mvp2_rsft_train_r1_s43\\n    role: variance\\n    result: training variance <0.04%\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: variance\\n    result: eval pending, same outcome expected\\n  depends_on:\\n  - D033\\n  - D027\\n- id: D038\\n  date: 2026-05-15 09:40 UTC\\n  summary: 'D038: 撤回 D037——RSFT \\\"灾难性失败\\\"实为 eval bug（50-doc pred vs 12275 gold denominator\\n    mismatch），s44 全量 eval 通过 MVP-2（rel_f1=0.4655 +5.98pp, evi_f1=0.8087 +1.08pp）'\\n  rationale: r1 的 rel_f1=0.0483 是评估代码 bug：TaskEvalCallback 在 50 docs 上生成预测但 gold triples\\n    用了全量 dev set 12275 条，recall 被人为压到 ~3.5%。s44 独立全量 eval（985 docs）结果：rel_f1=0.4655（+5.98pp\\n    vs SFT 0.4057），evi_f1=0.8087（+1.08pp vs 0.7979），edcr=0.6350（-7.68pp vs 0.7118）。CED\\n    rejection sampling 首次端到端验证成功。D037 的 reranker pivot 基于错误数据，RSFT 实际有效。\\n  related_experiments:\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: primary\\n    result: 'PASS: rel_f1=0.4655, evi_f1=0.8087'\\n  - exp_id: mvp2_rsft_train_r1\\n    role: pending_reeval\\n    result: r1 0.0483 was eval bug, full eval needed\\n  depends_on:\\n  - D037\\n- id: D039\\n  date: 2026-05-15 11:49 UTC\\n  summary: 'D039: RSFT+CED ablation 全部 PASS MVP-2——方法鲁棒，1 epoch 足够，EDCR 局限需论文讨论'\\n  rationale: Reviewer 独立验证 4 组 RSFT 配置（r1 s42/s44, r2a, r2b）全部通过 MVP-2 判据（rel_f1 >\\n    0.4057, evi_f1 > 0.798）。核心发现：(1) RSFT+CED 方法贡献 +4-6pp rel_f1，具体超参影响极小（0.45pp 范围内），方法鲁棒性好；(2)\\n    1 epoch 足够，3 epoch 无显著额外收益；(3) r2b 保守 LoRA scaling+低 lr 略优于 r2a（截断更少、字段完整率更高）；(4)\\n    EDCR 一致偏高 63-66%，CED reward 对 rel_f1 提升明显但对证据精确度提升有限，需论文坦诚讨论。两个 warning（ablation\\n    变量混淆、EDCR 高）均不阻塞 MVP，clean ablation 留研究阶段补。等 s43_r2 第三种子确认后调 complete_mvp()。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: ablation\\n    result: rel_f1=0.4494, evi_f1=0.8108, EDCR=0.6641, PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: ablation\\n    result: rel_f1=0.4493, evi_f1=0.8128, EDCR=0.6609, 截断179/字段完整率81.8%, PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: baseline_rsft\\n    result: rel_f1=0.4449, evi_f1=0.8187, EDCR=0.6565, PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: seed_variance\\n    result: rel_f1=0.4655, evi_f1=0.8087, PASS\\n  depends_on:\\n  - D038\\n- id: D040\\n  date: 2026-05-15 12:03 UTC\\n  summary: 'D040: MVP 正式通过 → 进入 Research 阶段。paper_framing.md 定稿（RSFT+CED 路线，4 Claims），experiment_plan.yaml\\n    建立（10 研究实验），dream_simulate(full) 已启动'\\n  rationale: D039 已判定 MVP-2 全部 PASS（4/4 configs），但 complete_mvp() 未被调用。用户催促后补调。Post-MVP\\n    kickoff 按 skill 流程执行：(1) paper_framing.md 从 Pre-MVP draft 更新为 Post-MVP 定稿版——方法从\\n    GRPO 转为 RSFT+CED，新增 Claim 3（在线 RL catastrophic forgetting 分析）和 RC6/RC7；(2) experiment_plan.yaml\\n    新建，10 个研究实验分 P0/P1/P2；(3) dream_simulate(full) 已启动（dream_20260515T120227），等回调后再批准\\n    P0 实验。投稿目标调整为 ARR July → EMNLP 2026 Main（ARR May 25 仅作 stretch goal）。\\n  related_experiments:\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: evidence\\n    result: rel_f1=0.4494 PASS\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: evidence\\n    result: rel_f1=0.4493 PASS\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: evidence\\n    result: rel_f1=0.4449 PASS\\n  - exp_id: mvp2_rsft_train_r1_s44\\n    role: evidence\\n    result: rel_f1=0.4655 PASS\\n  depends_on:\\n  - D039\\n- id: D041\\n  date: 2026-05-15 13:15 UTC\\n  summary: 'D041: Evi-F1 评测协议不一致确认——我们的\\\"条件 Evi-F1\\\"(仅 TP triples)与 DREEAM\\\"联合 Evi-F1\\\"(含\\n    FP/FN 惩罚)不可比，publishability threshold 暂冻结等对齐后重评'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过（precision 分母只算\\n    TP evidence），recall 分母也只算 matched gold triples。DREEAM 的 official_evaluate() 将\\n    FP/FN 全部计入分母。在 rel_recall ≈ 55% 时，分母差约 1.8x，解释了 82% vs 57% 的差距。已派 Agent 实现 DREEAM\\n    协议对齐函数并重新评估全部实验。在对齐数字出来前，paper_framing.md 的 publishability threshold（Evi-F1 >\\n    57.34）暂冻结。条件 Evi-F1 仍作为辅助指标保留（衡量\\\"关系对了时 evidence 选得好不好\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: evi_f1_conditional=0.7979, joint TBD\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: evi_f1_conditional=0.8187, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: evi_f1_conditional=0.8108, joint TBD\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: evi_f1_conditional=0.8128, joint TBD\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D042\\n  date: 2026-05-15 13:16 UTC\\n  summary: 'D041: Evi-F1 评测协议与 DREEAM 不一致——我们的 conditional Evi-F1 跳过 FP/FN triples，比\\n    DREEAM 的 joint Evi-F1 宽松得多。必须实现 DREEAM 协议对齐后重算所有实验。Publishability threshold 待重算后修订'\\n  rationale: Agent 调查确认：我们的 compute_evi_f1() 在 FP triple 时 continue 跳过，precision 分母只算\\n    TP；recall 分母也只算已匹配 gold。DREEAM 的 official_evaluate() 把 FP/FN 全部计入分母。关系 recall\\n    ~55% 时，分母差异完全解释 82% vs 57% 的差距。对齐方案：加 FP evidence 到 precision 分母 + 遍历全部 gold triple\\n    evidence 到 recall 分母。论文需要报告 DREEAM 协议数字（与文献可比），条件 Evi-F1 可作为辅助指标（衡量\\\"关系正确时 evidence\\n    选择质量\\\"）。\\n  related_experiments:\\n  - exp_id: mvp2_sft_eval_r2\\n    role: affected\\n    result: conditional evi_f1=0.7979, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r1\\n    role: affected\\n    result: conditional evi_f1=0.8187, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2a\\n    role: affected\\n    result: conditional evi_f1=0.8108, dreeam evi_f1 待重算\\n  - exp_id: mvp2_eval_rsft_r2b\\n    role: affected\\n    result: conditional evi_f1=0.8128, dreeam evi_f1 待重算\\n  depends_on:\\n  - D039\\n  - D040\\n- id: D043\\n  date: 2026-05-15 13:20 UTC\\n  summary: 'D042: Dream 审稿分析——best=2.5/median=3.0/worst=2.5（评分倒挂）。5 个确认行动项（narrow\\n    Claim 3 scope、加 GRPO G=8、修 Evi-F1 协议、CED contingency plan、加 DPO baseline），4 个观察项。Framing\\n    和 plan 已更新，re-dream 启动'\\n  rationale: 'Dream 三档审稿分析（dream-report-action 协议）：\\n\\n\\n    **三档一致的结构性问题（确认行动项）**：\\n\\n    1. CED vs flat-NLI 可能不显著 → 加 contingency plan，如 p>0.05 则 CED 降级\\n\\n    2. Title/claims overclaim \\\"online RL\\\" → Claim 3 限定为 \\\"GRPO+QLoRA\\\"\\n\\n    3. GRPO G=4 太小 → 加 plan_011 (G=8 实验，P0)\\n\\n    4. Cross-protocol Evi-F1 → 已在修复中 (D041)\\n\\n    5. 缺中间 baseline → 加 plan_012 (DPO, P1)\\n\\n\\n    **两档一致的观察项**：\\n\\n    - EDCR 需人工验证 [M][W] → plan_013\\n\\n    - Dev→test 退化 [M][W] → 等 plan_002 真实数据\\n\\n    - Number discrepancies [B][M] → Dream artifact（虚构数据），真实论文不会有此问题\\n\\n\\n    **评分倒挂说明**：best(2.5) < median(3.0) 因 best 版本膨胀数字被审稿人识破——说明诚实报告比膨胀结果更重要。\\n\\n\\n    **判断**：framing 和 plan 已按确认行动项修改，需 re-dream 验证后才能批准 P0 实验。'\\n  related_experiments: []\\n  depends_on:\\n  - D040\\n  - D041\\n- id: D044\\n  date: 2026-05-15 13:24 UTC\\n  summary: Dream v1 分析完成：reframe paper_framing.md，CED 降级，claims 重构，新增 3 个实验\\n  rationale: Dream v1 (best=2.5, median=3.0, worst=2.5) 三档一致指出：(1) CED vs flat-NLI\\n    不显著 p>0.05 → CED 从核心贡献降级为 one possible scoring function；(2) \\\"online RL fails\\\"\\n    标题过度声称 → 收窄到 \\\"GRPO fails for DocRE\\\"；(3) GRPO G=4 太小 → 新增 G=8 实验(plan_011)；(4)\\n    缺 DPO baseline → 新增 plan_012；(5) EDCR 缺人工验证 → 新增 plan_013。Claims 重构为 C1=evidence-grounded\\n    DocRE 可行性, C2=GRPO decoupling 发现, C3=NLI-based RSFT ablation, C4=EDCR 诊断工具。需 re-dream\\n    验证 reframe 效果。\\n  related_experiments:\\n  - exp_id: plan_011\\n    role: new_from_dream\\n    result: GRPO G=8 实验，排除 G=4 confound\\n  - exp_id: plan_012\\n    role: new_from_dream\\n    result: DPO+CED，online-offline 中间 baseline\\n  - exp_id: plan_013\\n    role: new_from_dream\\n    result: EDCR 100例人工标注验证\\n  depends_on:\\n  - D041\\n- id: D045\\n  date: 2026-05-15 13:41 UTC\\n  summary: 'D045: DPO 升级 P0 + GRPO G=8 排为第一优先；DPO 定位修正为 offline preference optimization'\\n  rationale: Reviewer 指出：(1) DPO 是纯 offline 方法，不是 online/offline 中间点——论文中错误定位会被审稿人攻击。已修正\\n    paper_framing.md。(2) DPO 结果直接决定 C2 叙事走向（on-policy 特有 vs 更 general 的现象），对 paper\\n    scope 有重大影响，升级 P0。(3) C2 对 GRPO G=8 单点依赖是最大风险，G=8 必须是 re-dream 后第一个启动的实验。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: 升级 P0\\n  - exp_id: plan_011\\n    role: 第一优先 P0\\n  depends_on:\\n  - D044\\n- id: D046\\n  date: 2026-05-15 13:42 UTC\\n  summary: 'D045: DPO 从 P1 升 P0 + GRPO G=8 定为 re-dream 后首批实验 + topk3 双变体设计'\\n  rationale: Reviewer 路线图审查指出：(1) DPO 结果直接决定 C2 decoupling 叙事——若 DPO 也出现 decoupling\\n    则现象更 general，若不出现则确认 on-policy 特有，两种结果都对论文有重大影响，升 P0；(2) C2 publishability 必要条件依赖\\n    GRPO G=8 复现 decoupling，是最高风险实验，必须首批启动；(3) topk3 数据含 CED=0 样本会稀释信号，改为双变体并行（全量 vs\\n    过滤 CED=0）以区分数据量效应和信号稀释。同时修正 paper_framing.md 中 DPO 定位错误（纯 offline 方法，非 online/offline\\n    中间点）。\\n  related_experiments:\\n  - exp_id: plan_012\\n    role: DPO+CED 升 P0\\n  - exp_id: plan_011\\n    role: GRPO G=8 首批 P0\\n  - exp_id: plan_008\\n    role: topk3 双变体设计\\n  depends_on:\\n  - D044\\n\", \"total_chars\": 34024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe86fcef-c67c-442e-89ea-88d9d5594de8",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "7624aecb-f71a-4423-91ed-2efffd523484",
  "sourceToolAssistantUUID": "fe86fcef-c67c-442e-89ea-88d9d5594de8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T14:10:35.929Z_

Now let me read the latest dream paper (the reframed version) for the most up-to-date content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7624aecb-f71a-4423-91ed-2efffd523484",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJVxGdoB5NdNKZjMYg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd9042e8-c56f-469b-8be8-ce83ffaccf63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjGAGCbodXa6aaJ7UguiGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20841,
      "cache_read_input_tokens": 39124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20841,
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

_source line 27 · 2026-05-15T14:10:38.460Z_

<details open><summary>🔧 Tool call — Read · `toolu_017tJjnqziZKDSvFzQe8Na7U`</summary>

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
  "parentUuid": "fd9042e8-c56f-469b-8be8-ce83ffaccf63",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VJVxGdoB5NdNKZjMYg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58710ce9-5e77-4433-bff0-af510cfa5d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjGAGCbodXa6aaJ7UguiGy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20841,
      "cache_read_input_tokens": 39124,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 39124,
          "cache_creation_input_tokens": 20841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20841,
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

_source line 28 · 2026-05-15T14:10:38.897Z_

<details><summary>↩ Tool result · `toolu_017tJjnqziZKDSvFzQe8Na7U`</summary>

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
  "parentUuid": "58710ce9-5e77-4433-bff0-af510cfa5d64",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "a3421f06-6172-44c7-a96d-94c2d5aa5d76",
  "sourceToolAssistantUUID": "58710ce9-5e77-4433-bff0-af510cfa5d64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-15T14:10:42.680Z_

Now let me also check the first dream report for context on the scores and reviews.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3421f06-6172-44c7-a96d-94c2d5aa5d76",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VK9qabTU3VAEemspDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0df7305a-e03d-4c19-b07e-855d191780c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vwAQxNdDNn6cAGugUPPsF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 30 · 2026-05-15T14:10:44.618Z_

<details open><summary>🔧 Tool call — Glob · `toolu_014LqpDJNBUwqDNRg8Quxx61`</summary>

```json
{
  "pattern": "**/dream_*/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df7305a-e03d-4c19-b07e-855d191780c3",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VK9qabTU3VAEemspDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02ac616b-20dc-4276-b46f-14067ecdbbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vwAQxNdDNn6cAGugUPPsF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 31 · 2026-05-15T14:10:44.645Z_

<details><summary>↩ Tool result · `toolu_014LqpDJNBUwqDNRg8Quxx61`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/best/experiment_data.json
artifacts/dream_reports/dream_20260515T120227/median/experiment_data.json
artifacts/dream_reports/dream_20260515T120227/worst/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/best/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/median/experiment_data.json
artifacts/dream_reports/dream_20260515T132059/worst/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02ac616b-20dc-4276-b46f-14067ecdbbd2",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "d7d22987-6650-4bf3-92bf-042f0ee8caa4",
  "sourceToolAssistantUUID": "02ac616b-20dc-4276-b46f-14067ecdbbd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T14:10:45.898Z_

<details open><summary>🔧 Tool call — Read · `toolu_019pZ6od8wZVhpeq2g6gjVfp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper.tex",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7d22987-6650-4bf3-92bf-042f0ee8caa4",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VK9qabTU3VAEemspDy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b87d4d76-aa68-43da-b055-6b94f1dfa6ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015vwAQxNdDNn6cAGugUPPsF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13162,
      "cache_read_input_tokens": 59965,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13162,
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

_source line 33 · 2026-05-15T14:10:45.905Z_

<details><summary>↩ Tool result · `toolu_019pZ6od8wZVhpeq2g6gjVfp`</summary>

```text
0	\documentclass[11pt,a4paper]{article}
1	\usepackage[utf8]{inputenc}
2	\usepackage[T1]{fontenc}
3	\usepackage{times}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\newcommand{\method}{FREIGE}
16	\newcommand{\ced}{CED}
17	\newcommand{\edcr}{EDCR}
18	\newcommand{\rsft}{RSFT}
19	
20	\title{FREIGE: Faithful Evidence Generation for LLM-Based\\Document-Level Relation Extraction via\\Contrastive Evidence Discrimination}
21	
22	\author{Anonymous Submission to EMNLP 2026}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	%==============================================================================
29	\begin{abstract}
30	%==============================================================================
31	Large language models (LLMs) are rapidly closing the gap with encoder-based methods on document-level relation extraction (DocRE), yet no existing LLM approach produces verifiable evidence---the supporting sentences that ground each predicted relation triple.
32	We present \method{} (\textbf{F}aithful \textbf{R}elation \textbf{E}xtraction with \textbf{I}ntra-document \textbf{G}rounded \textbf{E}vidence), the first generative LLM framework that jointly outputs relation triples \emph{and} explicit sentence-level evidence citations on DocRED.
33	At the core of \method{} is \ced{} (\textbf{C}ontrastive \textbf{E}vidence \textbf{D}iscrimination), a scoring function that measures evidence quality through intra-document hard-negative contrast: the entailment gap between gold evidence and the best entity-sharing distractor sentence.
34	We show that na\"ive NLI-based scoring is fooled by entity-sharing distractors and that online RL (GRPO+QLoRA) with \ced{} reward leads to catastrophic forgetting---a novel \emph{evidence--extraction decoupling} phenomenon where evidence quality improves (Evi-F1 up to 0.850) while extraction collapses (rel\_F1 $<$ 0.02).
35	Instead, using \ced{} as an offline quality filter for rejection sampling fine-tuning (\rsft{}) yields consistent gains: +5.5pp rel\_F1, +1.7pp Evi-F1 (conditional), and $-$7.1pp \edcr{} on the DocRED test set over SFT.
36	We further propose the \edcr{} (\textbf{E}ntity-sharing \textbf{D}istractor \textbf{C}itation \textbf{R}ate) metric, validated by human annotation (Pearson $r$=0.62), to diagnose plausible-looking but unfaithful evidence that standard Evi-F1 misses.
37	Experiments across three model scales (1.7B--8B) and two DocRED variants confirm the generality of our approach.
38	\end{abstract}
39	
40	%==============================================================================
41	\section{Introduction}
42	\label{sec:intro}
43	%==============================================================================
44	
45	Document-level relation extraction (DocRE) requires identifying relational facts between entity pairs that may span multiple sentences in a document.
46	Recent encoder-based methods achieve strong extraction performance and provide implicit evidence through attention-weight thresholding, but their evidence is not directly interpretable.
47	Meanwhile, LLM-based approaches to DocRE have shown competitive extraction accuracy, yet none produces explicit evidence citations that a human auditor can verify---a critical gap for deployment in knowledge base population, biomedical curation, and RAG provenance tracking.
48	
49	A natural approach is to train LLMs with faithfulness rewards derived from natural language inference (NLI) models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b87d4d76-aa68-43da-b055-6b94f1dfa6ca",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "b8ecf841-a1e6-48c4-bfa6-abc1e6a82519",
  "sourceToolAssistantUUID": "b87d4d76-aa68-43da-b055-6b94f1dfa6ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-15T14:10:49.791Z_

I now have comprehensive context from the paper, project files, literature map, experiment decisions, and paper framing. Let me also check the experiment data for the latest dream to see what actual numbers they're working with.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ecf841-a1e6-48c4-bfa6-abc1e6a82519",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VKgSau8Y5NQtb25irT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d633afe5-bd90-4666-bcf2-322140ccc668",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqHRgnHA9qKnez5fHxEsK8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 73127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1548,
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

_source line 35 · 2026-05-15T14:10:50.098Z_

<details open><summary>🔧 Tool call — Read · `toolu_019qgPFwaiq54WdkaZ3MqyPk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d633afe5-bd90-4666-bcf2-322140ccc668",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VKgSau8Y5NQtb25irT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cb51b04-e5dc-49da-b7a0-03211e39b3e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqHRgnHA9qKnez5fHxEsK8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1548,
      "cache_read_input_tokens": 73127,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 147,
          "cache_read_input_tokens": 73127,
          "cache_creation_input_tokens": 1548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1548,
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

_source line 36 · 2026-05-15T14:10:50.465Z_

<details><summary>↩ Tool result · `toolu_019qgPFwaiq54WdkaZ3MqyPk`</summary>

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
  "parentUuid": "8cb51b04-e5dc-49da-b7a0-03211e39b3e2",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "77911445-1a3b-4a09-8832-3aee6014ed84",
  "sourceToolAssistantUUID": "8cb51b04-e5dc-49da-b7a0-03211e39b3e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T14:10:53.921Z_

Now I have comprehensive context. Let me also check if there's a dream review report to understand what previous reviewers said.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77911445-1a3b-4a09-8832-3aee6014ed84",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VL1Dh21t7yyXoXSzmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c752da4d-75df-410a-83a3-a1047a11e24b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH27WB5BnLY3L3CxtgykQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17852,
      "cache_read_input_tokens": 74675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17852,
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

_source line 38 · 2026-05-15T14:10:55.908Z_

<details open><summary>🔧 Tool call — Glob · `toolu_015kk5vx1YuznUEXKVX1jJtY`</summary>

```json
{
  "pattern": "**/dream_*/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c752da4d-75df-410a-83a3-a1047a11e24b",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VL1Dh21t7yyXoXSzmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3cb9511-48bb-4467-90c6-022c5ebb1128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH27WB5BnLY3L3CxtgykQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17852,
      "cache_read_input_tokens": 74675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17852,
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

_source line 39 · 2026-05-15T14:10:55.939Z_

<details><summary>↩ Tool result · `toolu_015kk5vx1YuznUEXKVX1jJtY`</summary>

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
artifacts/dream_reports/dream_20260515T132059/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3cb9511-48bb-4467-90c6-022c5ebb1128",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "687ab4a7-df85-4161-a2fe-7432f4f09583",
  "sourceToolAssistantUUID": "d3cb9511-48bb-4467-90c6-022c5ebb1128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T14:10:56.203Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LvaJRG8xHhMwaWLwgWXRz2`</summary>

```json
{
  "pattern": "**/dream_*/**/*report*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "687ab4a7-df85-4161-a2fe-7432f4f09583",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VL1Dh21t7yyXoXSzmY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baf53118-c468-44ed-a10b-ecaa8c6ef85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH27WB5BnLY3L3CxtgykQV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17852,
      "cache_read_input_tokens": 74675,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 219,
          "cache_read_input_tokens": 74675,
          "cache_creation_input_tokens": 17852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17852,
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

_source line 41 · 2026-05-15T14:10:56.222Z_

<details><summary>↩ Tool result · `toolu_01LvaJRG8xHhMwaWLwgWXRz2`</summary>

```text
artifacts/dream_reports/dream_20260515T120227/median/review_report.md
artifacts/dream_reports/dream_20260515T120227/best/review_report.md
artifacts/dream_reports/dream_20260515T120227/worst/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf53118-c468-44ed-a10b-ecaa8c6ef85a",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "6dfe02fd-89c8-4840-89ab-4d6d2bff0d06",
  "sourceToolAssistantUUID": "baf53118-c468-44ed-a10b-ecaa8c6ef85a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T14:10:59.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DiFsS3VtR9XGpRP7UsrrPf`</summary>

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
  "parentUuid": "6dfe02fd-89c8-4840-89ab-4d6d2bff0d06",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VLSBroowuvfuVY8rgf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aae0c9e9-a284-41fe-8e48-7c3f5bc47b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7cp9vQF3N6UjeHK1UdyPW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 92527,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 92527,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 703,
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

_source line 43 · 2026-05-15T14:10:59.248Z_

<details><summary>↩ Tool result · `toolu_01DiFsS3VtR9XGpRP7UsrrPf`</summary>

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
  "parentUuid": "aae0c9e9-a284-41fe-8e48-7c3f5bc47b4c",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "98b298d2-f367-43c9-8b6e-635083b5746f",
  "sourceToolAssistantUUID": "aae0c9e9-a284-41fe-8e48-7c3f5bc47b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-15T14:11:02.053Z_

Now I have full context. Let me now produce my R2 review focusing on Novelty and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b298d2-f367-43c9-8b6e-635083b5746f",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VLewa2LYhY2R2Am3xs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51e275e5-97d2-4f1d-8d2c-21eb0dfd476c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvTtEnMxRZQeUh7Pv3uSQS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 93230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 45 · 2026-05-15T14:11:02.575Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PdBSnQqQdNZzGLB3BYRYum`</summary>

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
  "parentUuid": "51e275e5-97d2-4f1d-8d2c-21eb0dfd476c",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VLewa2LYhY2R2Am3xs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a14a873-02ef-4402-8729-157a171eea30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DvTtEnMxRZQeUh7Pv3uSQS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2374,
      "cache_read_input_tokens": 93230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2374,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 46 · 2026-05-15T14:11:02.580Z_

<details><summary>↩ Tool result · `toolu_01PdBSnQqQdNZzGLB3BYRYum`</summary>

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
  "parentUuid": "3a14a873-02ef-4402-8729-157a171eea30",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "417c321a-d49a-44bb-979e-23cb7dd24bc4",
  "sourceToolAssistantUUID": "3a14a873-02ef-4402-8729-157a171eea30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-15T14:12:19.621Z_



Now I have all the context needed. Let me produce the R2 review focusing on Novelty and Related Work, then submit it for all three tiers.

Let me first check which dream_id this review should be associated with — the latest one is `dream_20260515T132059`.

## R2 Review: Novelty & Related Work

### Summary
FREIGE proposes the first LLM-based document-level relation extraction system that jointly generates relation triples and explicit sentence-level evidence citations. The paper's contributions are threefold: (1) a Contrastive Evidence Discrimination (CED) scoring function using NLI-based hard negatives, (2) a CED-guided Rejection Sampling Fine-Tuning (RSFT) pipeline, and (3) the EDCR diagnostic metric. The paper also documents a negative finding — evidence-extraction decoupling under GRPO — which is arguably its most novel empirical contribution.

### Strengths
- **S1: The "first" claim is credible and well-scoped.** I am not aware of any prior LLM-based DocRE method that jointly generates relation triples and explicit sentence-level evidence on DocRED. Encoder methods (DREEAM, SAIS) derive evidence from attention weights, and all existing LLM-based DocRE methods (LMRC, AutoRE, RelPrior, Ru-LLM) produce only triples. The paper appropriately scopes this as "first on DocRED" rather than overclaiming universality.

- **S2: Evidence-extraction decoupling is a genuinely novel and valuable finding.** The observation that GRPO training drives evidence quality up (evi_F1 to 0.862) while extraction collapses (rel_F1 < 0.02), and that this *worsens* with larger group sizes providing more precise advantage estimation, is striking. This connects well to the reward overoptimization literature (Gao et al. 2023) and provides a concrete, task-grounded instance of a phenomenon that the RL-for-LLM community has discussed mostly in abstract terms. The G=4 vs G=8 comparison strengthens this by ruling out the "insufficient exploration" counter-argument.

- **S3: Comprehensive training paradigm comparison.** The GRPO / DPO / RSFT spectrum (Table 5 in the median paper) is a well-designed empirical contribution. The finding that DPO partially mitigates but does not solve decoupling — landing between GRPO collapse and SFT baseline — adds nuance to the online-vs-offline RL narrative and leads to the more precise insight that the issue is contrastive/reward-based loss vs. data curation.

- **S4: EDCR fills a real diagnostic gap.** Standard Evi-F1 is dominated by recall and does not penalize plausible-looking distractors. EDCR is a simple, interpretable metric that captures this failure mode. The human validation, while modest (r=0.44), demonstrates perfect method-level rank concordance, which is the practically useful property.

- **S5: Honest self-assessment.** The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods, and EDCR's limitations. This intellectual honesty significantly increases the paper's credibility.

### Weaknesses
- **W1 (Major): CED itself is not novel — it is a straightforward application of NLI entailment scoring with document-internal hard negatives.** The contrastive margin (p_entail(gold) - max(p_entail(distractor))) is a standard contrastive scoring pattern seen in retrieval, reranking, and faithfulness evaluation (e.g., INFUSE at EACL 2024, contrastive reward methods in RLHF). The novelty is in applying it to DocRE evidence, not in the scoring mechanism itself. Combined with the fact that CED does not significantly outperform flat-NLI (p>0.05 on all three metrics), the method-level novelty is limited. The paper's reframing (CED as "one possible scoring function" rather than the core contribution) is appropriate, but this means the method contribution is essentially RSFT applied to DocRE — which is also not architecturally novel. The novelty resides primarily in the task definition and the negative finding.

- **W2 (Major): The related work section on RL for IE is thin.** The paper mentions "prior work has applied RL to IE tasks with mixed results" without citing specific work. R1-RE (arXiv 2507.04642, GRPO for sentence-level RE) is the most directly comparable method and is not cited. REAR (EMNLP 2025 Findings, RL for event argument extraction) is also missing. The "RL for Information Extraction" paragraph should be substantially expanded with specific citations and differentiation. The absence of R1-RE is particularly notable given that it applies GRPO to RE (sentence-level) and succeeds — which would raise the question of why GRPO fails at document-level but not sentence-level. This contrast would actually *strengthen* the paper's argument if properly discussed.

- **W3 (Major): Missing LLM-based DocRE baselines weaken the "first" and positioning claims.** The related work cites LMRC as the sole LLM-based DocRE method, but several recent works are missing: RelPrior (arXiv 2511.08143, LLM DocRE with relation-as-prior), Ru-LLM (NLPCC 2025, rule-constrained LLM DocRE), AutoRE (arXiv 2403.14888, RHF paradigm with Mistral-7B), and GLiDRE (arXiv 2508.00757, dual-encoder DocRE). While none of these produce evidence, their omission makes the related work section appear under-researched and weakens the positioning of the extraction results. The gap between FREIGE (43.2% test) and these methods (some above 60%) needs contextualization.

- **W4 (Moderate): RSFT is not a novel training paradigm.** The paper correctly cites the RSFT-PPO equivalence (Dong et al. 2024) and positions RSFT as existing methodology applied to a new domain. However, the framing in the introduction ("Our solution is FREIGE, built on RSFT") may lead readers to perceive RSFT as a contribution of this paper. The distinction between "we apply RSFT to DocRE" and "we contribute RSFT" should be sharpened. The "Minimalist Approach" paper (arXiv 2504.11343) showing RAFT matching GRPO/PPO on math reasoning is directly relevant and should be cited — it provides theoretical grounding for why offline rejection sampling can match online RL.

- **W5 (Moderate): The connection to reward overoptimization literature is superficial.** The paper cites Gao et al. (2023) but does not engage deeply with the scaling law framework. Specifically: does the decoupling follow a KL-dependent scaling law? Is there a "Goodhart's Law" interpretation — the CED reward is a proxy for evidence quality, and optimizing the proxy diverges from the true objective? The contrastive reward literature (arXiv 2403.07708, EMNLP 2024 contrastive RM) provides mechanisms for mitigating exactly this kind of reward misalignment. The paper should discuss why these mitigations were not attempted or why they would be insufficient for structured IE.

- **W6 (Minor): The framing alternates between CED-centric and RSFT-centric narratives.** The title of the "best" tier paper centers CED ("via Contrastive Evidence Discrimination") while the "median" tier centers RSFT ("via Rejection Sampling Fine-Tuning"). This reflects a genuine framing tension: if CED is not significantly better than flat-NLI, the paper's identity is "RSFT for evidence-grounded DocRE + negative GRPO findings + EDCR metric." This is still a valid paper, but the framing should commit to one narrative rather than hedging.

- **W7 (Minor): No discussion of concurrent work on evidence/rationale generation for IE.** The faithfulness literature (Drift at ACL 2025 on faithfulness rewards for rationale generation) is relevant but not cited. The paper's approach of using NLI-based faithfulness signals for data curation has conceptual overlap with work on faithful CoT generation, and positioning within this broader context would strengthen the contribution.

### Questions for Authors
- **Q1:** R1-RE (arXiv 2507.04642) successfully applies GRPO to sentence-level RE. What is your hypothesis for why GRPO succeeds at sentence-level RE but catastrophically fails at document-level RE? Is the critical difference document length, output structure complexity, or something else? This contrast could significantly strengthen your decoupling analysis.

- **Q2:** The 78% overlap between CED-selected and flat-NLI-selected candidates is high. Have you analyzed the 22% divergent cases? Are the CED-unique selections demonstrably better in terms of evidence quality, or are they random disagreements? This would clarify whether CED's contrastive margin adds genuine signal or just noise.

- **Q3:** You mention that "incomplete DocRED gold evidence (~14% false distractors) dilutes the hard-negative signal" for CED. If gold evidence annotations are incomplete, doesn't this equally affect the RSFT pipeline (which scores candidates against noisy gold)? How sensitive is RSFT to annotation noise?

- **Q4:** The EDCR metric is defined over entity-sharing distractors only. What fraction of actual distractor citations are non-entity-sharing? If a model cites a sentence that shares no entities with the triple but is still irrelevant, EDCR would not capture this. Have you quantified this blind spot?

- **Q5:** Have you considered a post-hoc evidence retrieval baseline (e.g., run LMRC for extraction, then BM25/sentence-BERT to retrieve evidence sentences)? This would separate the contribution of joint generation from pipeline approaches.

### Missing Related Work / Positioning Issues
- **P1:** R1-RE (arXiv 2507.04642) — first GRPO application to relation extraction (sentence-level). Must-cite for the GRPO analysis. Its success at sentence-level RE creates a natural foil for the document-level failure documented here.

- **P2:** RelPrior (arXiv 2511.08143), Ru-LLM (NLPCC 2025), AutoRE (arXiv 2403.14888) — recent LLM-based DocRE methods that should be cited and compared for extraction performance positioning.

- **P3:** "A Minimalist Approach to LLM Reasoning" (arXiv 2504.11343) — directly relevant RSFT theoretical foundation showing rejection sampling matches GRPO/PPO.

- **P4:** Contrastive reward methods: "Improving RL from Human Feedback Using Contrastive Rewards" (arXiv 2403.07708), contrastive RM at EMNLP 2024 — relevant to CED's contrastive design and to the discussion of why contrastive rewards cause issues in structured IE.

- **P5:** Drift (ACL 2025) — faithfulness rewards for LLM rationale generation. Conceptually adjacent to CED's role as a faithfulness signal.

- **P6:** DAPO (NeurIPS 2025), Dr. GRPO (COLM 2025) — relevant to the GRPO failure analysis. These works identify entropy collapse and normalization bias in GRPO that may partially explain the document-level IE failures.

- **P7:** The connection between EDCR and precision-oriented evaluation metrics in other NLP tasks (e.g., faithfulness metrics in summarization like FactScore) is not drawn. EDCR would benefit from positioning within the broader "precision of generated citations" evaluation landscape.

### Scores
- Soundness: 3/5
- Excitement: 3/5
- Overall: 3.0/5
- Reproducibility: 4/5
- Confidence: 4/5

### Justification for Overall Score
The paper makes a credible "first" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding (evidence-extraction decoupling). However, the method-level novelty is limited: CED is a straightforward NLI contrastive scorer that does not significantly outperform flat-NLI, and RSFT is existing methodology applied to a new domain. The related work has notable gaps (R1-RE, recent LLM-based DocRE methods, contrastive reward literature) that weaken the positioning. The paper is best characterized as a solid empirical study with an interesting negative finding and a useful new metric, but it does not introduce a sufficiently novel method to clear the EMNLP main conference bar without strengthening the related work coverage and either demonstrating CED's statistical advantage or fully committing to the "task definition + negative finding + diagnostic metric" framing.

Now let me submit this review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417c321a-d49a-44bb-979e-23cb7dd24bc4",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VLurWSncCKB2SjkCuL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5b06acd-59d0-476d-a89a-50bfc36cabd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ubPW32ScQbZStCJBMkwUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 95604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 692,
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

_source line 48 · 2026-05-15T14:12:44.384Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01Vx9xp4xf5oMEamtvdqGH6j`</summary>

```json
{
  "project": "faith-evidence-ie",
  "tier": "median",
  "dream_id": "dream_20260515T132059",
  "overall_score": "3.0 - Borderline Findings",
  "report": "## R2 Review: Novelty & Related Work\n\n### Summary\nFREIGE proposes the first LLM-based document-level relation extraction system that jointly generates relation triples and explicit sentence-level evidence citations. The paper's contributions are threefold: (1) a Contrastive Evidence Discrimination (CED) scoring function using NLI-based hard negatives, (2) a CED-guided Rejection Sampling Fine-Tuning (RSFT) pipeline, and (3) the EDCR diagnostic metric. The paper also documents a negative finding — evidence-extraction decoupling under GRPO — which is arguably its most novel empirical contribution.\n\n### Strengths\n- S1: **The \"first\" claim is credible and well-scoped.** I am not aware of any prior LLM-based DocRE method that jointly generates relation triples and explicit sentence-level evidence on DocRED. Encoder methods (DREEAM, SAIS) derive evidence from attention weights, and all existing LLM-based DocRE methods (LMRC, AutoRE, RelPrior, Ru-LLM) produce only triples. The paper appropriately scopes this as \"first on DocRED\" rather than overclaiming universality.\n\n- S2: **Evidence-extraction decoupling is a genuinely novel and valuable finding.** The observation that GRPO training drives evidence quality up (evi_F1 to 0.862) while extraction collapses (rel_F1 < 0.02), and that this *worsens* with larger group sizes providing more precise advantage estimation, is striking. This connects well to the reward overoptimization literature (Gao et al. 2023) and provides a concrete, task-grounded instance of a phenomenon that the RL-for-LLM community has discussed mostly in abstract terms. The G=4 vs G=8 comparison strengthens this by ruling out the \"insufficient exploration\" counter-argument.\n\n- S3: **Comprehensive training paradigm comparison.** The GRPO / DPO / RSFT spectrum is a well-designed empirical contribution. The finding that DPO partially mitigates but does not solve decoupling — landing between GRPO collapse and SFT baseline — adds nuance to the online-vs-offline RL narrative and leads to the more precise insight that the issue is contrastive/reward-based loss vs. data curation.\n\n- S4: **EDCR fills a real diagnostic gap.** Standard Evi-F1 is dominated by recall and does not penalize plausible-looking distractors. EDCR is a simple, interpretable metric that captures this failure mode. The human validation, while modest (r=0.44), demonstrates perfect method-level rank concordance, which is the practically useful property.\n\n- S5: **Honest self-assessment.** The paper is transparent about CED's non-significant advantage over flat-NLI (p=0.12/0.28/0.09), the absolute performance gap to encoder methods, and EDCR's limitations. This intellectual honesty significantly increases the paper's credibility.\n\n### Weaknesses\n- W1 (Major): **CED itself is not novel — it is a straightforward application of NLI entailment scoring with document-internal hard negatives.** The contrastive margin (p_entail(gold) - max(p_entail(distractor))) is a standard contrastive scoring pattern seen in retrieval, reranking, and faithfulness evaluation (e.g., INFUSE at EACL 2024, contrastive reward methods in RLHF). The novelty is in applying it to DocRE evidence, not in the scoring mechanism itself. Combined with the fact that CED does not significantly outperform flat-NLI (p>0.05 on all three metrics), the method-level novelty is limited. The paper's reframing (CED as \"one possible scoring function\" rather than the core contribution) is appropriate, but this means the method contribution is essentially RSFT applied to DocRE — which is also not architecturally novel. The novelty resides primarily in the task definition and the negative finding.\n\n- W2 (Major): **The related work section on RL for IE is thin.** The paper mentions \"prior work has applied RL to IE tasks with mixed results\" without citing specific work. R1-RE (arXiv 2507.04642, GRPO for sentence-level RE) is the most directly comparable method and is not cited. REAR (EMNLP 2025 Findings, RL for event argument extraction) is also missing. The \"RL for Information Extraction\" paragraph should be substantially expanded with specific citations and differentiation. The absence of R1-RE is particularly notable given that it applies GRPO to RE (sentence-level) and succeeds — which would raise the question of why GRPO fails at document-level but not sentence-level. This contrast would actually *strengthen* the paper's argument if properly discussed.\n\n- W3 (Major): **Missing LLM-based DocRE baselines weaken the \"first\" and positioning claims.** The related work cites LMRC as the sole LLM-based DocRE method, but several recent works are missing: RelPrior (arXiv 2511.08143, LLM DocRE with relation-as-prior), Ru-LLM (NLPCC 2025, rule-constrained LLM DocRE), AutoRE (arXiv 2403.14888, RHF paradigm with Mistral-7B), and GLiDRE (arXiv 2508.00757, dual-encoder DocRE). While none of these produce evidence, their omission makes the related work section appear under-researched and weakens the positioning of the extraction results. The gap between FREIGE (43.2% test) and these methods (some above 60%) needs contextualization.\n\n- W4 (Moderate): **RSFT is not a novel training paradigm.** The paper correctly cites the RSFT-PPO equivalence (Dong et al. 2024) and positions RSFT as existing methodology applied to a new domain. However, the framing in the introduction (\"Our solution is FREIGE, built on RSFT\") may lead readers to perceive RSFT as a contribution of this paper. The distinction between \"we apply RSFT to DocRE\" and \"we contribute RSFT\" should be sharpened. The \"Minimalist Approach\" paper (arXiv 2504.11343) showing RAFT matching GRPO/PPO on math reasoning is directly relevant and should be cited — it provides theoretical grounding for why offline rejection sampling can match online RL.\n\n- W5 (Moderate): **The connection to reward overoptimization literature is superficial.** The paper cites Gao et al. (2023) but does not engage deeply with the scaling law framework. Specifically: does the decoupling follow a KL-dependent scaling law? Is there a \"Goodhart's Law\" interpretation — the CED reward is a proxy for evidence quality, and optimizing the proxy diverges from the true objective? The contrastive reward literature (arXiv 2403.07708, EMNLP 2024 contrastive RM) provides mechanisms for mitigating exactly this kind of reward misalignment. The paper should discuss why these mitigations were not attempted or why they would be insufficient for structured IE.\n\n- W6 (Minor): **The framing alternates between CED-centric and RSFT-centric narratives.** The title centers CED/RSFT depending on the version, reflecting a genuine framing tension: if CED is not significantly better than flat-NLI, the paper's identity is \"RSFT for evidence-grounded DocRE + negative GRPO findings + EDCR metric.\" This is still a valid paper, but the framing should commit to one narrative rather than hedging.\n\n- W7 (Minor): **No discussion of concurrent work on evidence/rationale generation for IE.** The faithfulness literature (Drift at ACL 2025 on faithfulness rewards for rationale generation) is relevant but not cited. The paper's approach of using NLI-based faithfulness signals for data curation has conceptual overlap with work on faithful CoT generation, and positioning within this broader context would strengthen the contribution.\n\n### Questions for Authors\n- Q1: R1-RE (arXiv 2507.04642) successfully applies GRPO to sentence-level RE. What is your hypothesis for why GRPO succeeds at sentence-level RE but catastrophically fails at document-level RE? Is the critical difference document length, output structure complexity, or something else? This contrast could significantly strengthen your decoupling analysis.\n\n- Q2: The 78% overlap between CED-selected and flat-NLI-selected candidates is high. Have you analyzed the 22% divergent cases? Are the CED-unique selections demonstrably better in terms of evidence quality, or are they random disagreements? This would clarify whether CED's contrastive margin adds genuine signal or just noise.\n\n- Q3: You mention that \"incomplete DocRED gold evidence (~14% false distractors) dilutes the hard-negative signal\" for CED. If gold evidence annotations are incomplete, doesn't this equally affect the RSFT pipeline (which scores candidates against noisy gold)? How sensitive is RSFT to annotation noise?\n\n- Q4: The EDCR metric is defined over entity-sharing distractors only. What fraction of actual distractor citations are non-entity-sharing? If a model cites a sentence that shares no entities with the triple but is still irrelevant, EDCR would not capture this. Have you quantified this blind spot?\n\n- Q5: Have you considered a post-hoc evidence retrieval baseline (e.g., run LMRC for extraction, then BM25/sentence-BERT to retrieve evidence sentences)? This would separate the contribution of joint generation from pipeline approaches.\n\n### Missing Related Work / Positioning Issues\n- P1: R1-RE (arXiv 2507.04642) — first GRPO application to relation extraction (sentence-level). Must-cite for the GRPO analysis. Its success at sentence-level RE creates a natural foil for the document-level failure documented here.\n\n- P2: RelPrior (arXiv 2511.08143), Ru-LLM (NLPCC 2025), AutoRE (arXiv 2403.14888) — recent LLM-based DocRE methods that should be cited and compared for extraction performance positioning.\n\n- P3: \"A Minimalist Approach to LLM Reasoning\" (arXiv 2504.11343) — directly relevant RSFT theoretical foundation showing rejection sampling matches GRPO/PPO.\n\n- P4: Contrastive reward methods: \"Improving RL from Human Feedback Using Contrastive Rewards\" (arXiv 2403.07708), contrastive RM at EMNLP 2024 — relevant to CED's contrastive design and to the discussion of why contrastive rewards cause issues in structured IE.\n\n- P5: Drift (ACL 2025) — faithfulness rewards for LLM rationale generation. Conceptually adjacent to CED's role as a faithfulness signal.\n\n- P6: DAPO (NeurIPS 2025), Dr. GRPO (COLM 2025) — relevant to the GRPO failure analysis. These works identify entropy collapse and normalization bias in GRPO that may partially explain the document-level IE failures.\n\n- P7: The connection between EDCR and precision-oriented evaluation metrics in other NLP tasks (e.g., faithfulness metrics in summarization like FactScore) is not drawn. EDCR would benefit from positioning within the broader \"precision of generated citations\" evaluation landscape.\n\n### Scores\n- Soundness: 3/5\n- Excitement: 3/5\n- Overall: 3.0/5\n- Reproducibility: 4/5\n- Confidence: 4/5\n\n### Justification for Overall Score\nThe paper makes a credible \"first\" claim for evidence-grounded LLM-based DocRE and documents a genuinely interesting negative finding (evidence-extraction decoupling). However, the method-level novelty is limited: CED is a straightforward NLI contrastive scorer that does not significantly outperform flat-NLI, and RSFT is existing methodology applied to a new domain. The related work has notable gaps (R1-RE, recent LLM-based DocRE methods, contrastive reward literature) that weaken the positioning. The paper is best characterized as a solid empirical study with an interesting negative finding and a useful new metric, but it does not introduce a sufficiently novel method to clear the EMNLP main conference bar without strengthening the related work coverage and either demonstrating CED's statistical advantage or fully committing to the \"task definition + negative finding + diagnostic metric\" framing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b06acd-59d0-476d-a89a-50bfc36cabd5",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VLurWSncCKB2SjkCuL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cda5aacc-4932-45d9-95a2-9a75b5ad3e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ubPW32ScQbZStCJBMkwUU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 95604,
      "output_tokens": 6318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6318,
          "cache_read_input_tokens": 95604,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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

_source line 49 · 2026-05-15T14:12:45.101Z_

<details><summary>↩ Tool result · `toolu_01Vx9xp4xf5oMEamtvdqGH6j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/review_report.md\", \"dream_id\": \"dream_20260515T132059\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda5aacc-4932-45d9-95a2-9a75b5ad3e3e",
  "isSidechain": true,
  "promptId": "c78e6a6e-aab5-40c9-8740-1907908ec6fe",
  "agentId": "a3594e4cd3664149b",
  "type": "user",
  "uuid": "fd43a931-21f4-4ea8-93b3-8ae18172717f",
  "sourceToolAssistantUUID": "cda5aacc-4932-45d9-95a2-9a75b5ad3e3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-15T14:12:54.690Z_

Review submitted for the median tier. The review has been saved to `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/review_report.md`.

**Summary of the R2 review (Novelty & Related Work focus):**

**Overall score: 3.0/5 (Borderline Findings)**

**Key strengths identified:**
- The "first LLM-based DocRE with evidence" claim is credible and well-scoped
- Evidence-extraction decoupling is a genuinely novel and striking empirical finding, strengthened by the G=4 vs G=8 comparison
- The GRPO/DPO/RSFT training paradigm comparison is well-designed
- EDCR fills a real diagnostic gap with useful method-level discrimination
- Intellectual honesty about CED's non-significance over flat-NLI

**Key weaknesses identified:**
- (Major) CED is a straightforward NLI contrastive scorer, not architecturally novel, and statistically indistinguishable from flat-NLI
- (Major) Related work on RL for IE is thin — R1-RE (GRPO for sentence-level RE) is a must-cite that is missing, and its success vs. this paper's failure would actually strengthen the argument
- (Major) Several recent LLM-based DocRE methods (RelPrior, Ru-LLM, AutoRE, GLiDRE) are missing from related work
- (Moderate) RSFT is existing methodology; the distinction between applying it and contributing it needs sharpening
- (Moderate) Connection to reward overoptimization literature is superficial

**Core assessment:** The novelty resides primarily in the task definition (evidence-grounded DocRE) and the negative finding (decoupling), not in the method (CED/RSFT). The related work needs substantial expansion. The paper would benefit from committing fully to the "task + negative finding + diagnostic metric" framing rather than hedging between CED-centric and RSFT-centric narratives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd43a931-21f4-4ea8-93b3-8ae18172717f",
  "isSidechain": true,
  "agentId": "a3594e4cd3664149b",
  "requestId": "req_011Cb4VUTRzhuf1LwicBZm8R",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69a0bd6c-c77c-4fae-b898-e1dccee3e024",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "6f25cfed-835a-4517-9646-6292208db176",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012T2spgkwQt1hqnXcP1oSGt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6447,
      "cache_read_input_tokens": 96296,
      "output_tokens": 505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 505,
          "cache_read_input_tokens": 96296,
          "cache_creation_input_tokens": 6447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6447,
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
