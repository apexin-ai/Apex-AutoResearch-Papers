# Research conversation: You are Reviewer R2 for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. Provide a blind, thorough 

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-abe44e0c67a15047b.jsonl`
- **Structured JSON:** [`04704e003b4f088f944e.json`](../../sessions/04/04704e003b4f088f944e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-16T15:50:30.571Z_

You are Reviewer R2 for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. Provide a blind, thorough review.

## Venue: EMNLP 2026 (via ACL Rolling Review)
- Acceptance rate: ~22%
- Scoring: Soundness (1-5), Excitement (1-5), Overall (1-5)
- Soundness: 5=Excellent, 4=Strong, 3=Acceptable, 2=Poor, 1=Major Issues
- Excitement: 5=Highly Exciting, 4=Exciting, 3=Ambivalent, 2=Mediocre, 1=Not Exciting
- Overall: 5=Strong Accept, 4=Accept, 3=Borderline, 2=Reject, 1=Strong Reject

## Paper Summary

**Title**: "Phase-Dependent Compound Sparsity: Quantifying the Interaction Between Head Pruning and KV Cache Eviction Across Reasoning Phases"

**Core claim**: Compound sparsity (simultaneous head pruning + KV cache eviction) produces phase-dependent severity—later reasoning phases suffer more than earlier ones. Three findings:
1. **Phase gradient universality**: dz ≈ 1.0–1.2 across all models/architectures/sparsity levels (Bonferroni p < 10^-30)
2. **Dose-response monotonicity**: Severity increases monotonically with sparsity (Spearman ρ = 1.0)
3. **Strategy modulation with architecture-dependent magnitude**: Importance-based eviction 15-36× stronger than random on MATH-500/Qwen2, attenuates to 2-5× on simpler tasks and LLaMA

**Contributions stated**:
1. First quantitative characterization of phase-dependent compound severity with effect size estimation
2. Demonstration of dose-response monotonicity across 4 sparsity levels and 3 benchmarks
3. Identification of architecture-dependent strategy modulation
4. Discrimination collapse mechanism explaining phase-dependent amplification

**Related work (§2)**:
- **Single-Axis KV Cache**: ThinKV (Feng et al., 2025) — phase-aware but single-axis; R-KV (Li et al., 2025) — reasoning-optimized; Physics of KV Cache Compression (Wang et al., 2026) — phase transitions in compression-rate space
- **Compound Compression**: SparK (Chen et al., 2024) — joint compression treating interaction as uniformly super-additive
- **Importance Score Dynamics**: HIES (Zhang et al., 2025) — importance score collapse, entropy-based compensation
- **Adaptive Pruning**: Lethe (Park et al., 2026) — layer-time-adaptive KV pruning

**Method**: Interaction Index II_i = Δ_compound,i − (Δ_prune,i + Δ_evict,i). Phase segmentation by token position quantiles. Paired phase gradient G_i = II_{i,low} − II_{i,high}. Cohen's dz with Wilcoxon + Bonferroni.

**Models**: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Llama-8B (7-8B scale)

**Benchmarks**: MATH-500, GSM8K, GPQA-Diamond

**Discussion highlights**:
- Phase gradient is a structural property of autoregressive reasoning
- Architecture modulates magnitude (GQA vs MHA)
- Task complexity modulates strategy specificity
- Discrimination collapse: Gini/CV decline in importance scores under compound pruning
- Secondary entropy redistribution is model-dependent (DeepSeek only)

**Limitations**: 7-8B scale only; task-dependent specificity not fully characterized; GQA hypothesis lacks causal evidence; phase segmentation is proxy; no throughput implications

**References**: 7 total references (Chen 2024, Feng 2025, Li 2025, Wang 2026, Zhang 2025, Park 2026, Liu 2024)

## Your Review Focus (Novelty + Related Work)

Please evaluate:

1. **Novelty assessment**: 
   - Is "phase-dependent compound sparsity" genuinely new? The paper claims to be the "first systematic quantification." But ThinKV already does phase-aware KV cache compression. HIES already observes importance score collapse. SparK already studies compound compression. What is the delta?
   - Is the contribution primarily empirical characterization or methodological? The paper proposes no new method—it characterizes an existing phenomenon. Is this sufficient for EMNLP?
   - The "discrimination collapse" mechanism — is it novel or a reframing of HIES's importance score collapse in a compound setting?

2. **Related work coverage**:
   - Only 7 references total. Is this adequate for a venue like EMNLP?
   - Missing areas: (a) structured pruning literature (e.g., lottery ticket, magnitude pruning); (b) other KV cache methods (H2O, StreamingLLM, ScissorHands, PyramidKV, SnapKV); (c) reasoning in LLMs literature; (d) phase-aware or stage-aware inference beyond ThinKV; (e) MoE/sparse architectures that are related to "compound sparsity"
   - The paper cites no pre-2024 foundational work on attention pruning or KV cache compression

3. **Positioning and framing**:
   - The paper frames itself as empirical characterization. Is this the right framing for EMNLP vs. a systems venue or workshop?
   - The "discrimination collapse" framing — does it add mechanistic insight or is it descriptive?
   - Claims like "challenges the implicit assumption of uniform compound degradation" — who actually makes this assumption? Is there a straw man?

4. **Scope and significance**:
   - Only 7-8B models — would findings hold at 70B+?
   - Purely characterization with no proposed solution — is the "so what" clear enough?
   - The practical implication (phase-aware controllers) is mentioned but not explored

5. **Writing quality and clarity**:
   - Paper is 7 pages of content + 1 page references
   - Is the presentation dense enough for EMNLP? Missing: figures, appendix, error analysis

Provide your review in this structure:
- Summary (2-3 sentences)
- Strengths (bullet points)
- Weaknesses (bullet points, numbered W1, W2, ...)
- Questions for Authors (numbered Q1, Q2, ...)
- Novelty Assessment (detailed paragraph)
- Related Work Gaps
- Scores: Soundness (1-5), Excitement (1-5), Overall (1-5) with brief justification
- Confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "c9a0ede8-5115-4b31-a0a6-cdd2d9251adc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T15:50:30.574Z_

```json
{
  "parentUuid": "c9a0ede8-5115-4b31-a0a6-cdd2d9251adc",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
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
  "uuid": "f23a788d-439d-4a2d-9a9a-244e898dc744",
  "timestamp": "2026-05-16T15:50:30.574Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T15:50:33.707Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PxPmjPSXBHa7zRiAqhRs5W`</summary>

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
  "parentUuid": "f23a788d-439d-4a2d-9a9a-244e898dc744",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WjjpXba6d4fmrBEuej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0764bf17-2bcb-48ad-ba67-25f98ba1898d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yiw618zFfXWXdv5GUzc2Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7516,
      "cache_read_input_tokens": 8252,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7516
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7516,
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

_source line 4 · 2026-05-16T15:50:33.711Z_

<details><summary>↩ Tool result · `toolu_01PxPmjPSXBHa7zRiAqhRs5W`</summary>

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
  "parentUuid": "0764bf17-2bcb-48ad-ba67-25f98ba1898d",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "6270d70f-63c3-4e47-bd75-c34a82790337",
  "sourceToolAssistantUUID": "0764bf17-2bcb-48ad-ba67-25f98ba1898d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T15:50:37.050Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0116sNoCnKwt1wFPL4uVcusv`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6270d70f-63c3-4e47-bd75-c34a82790337",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WjyPbbvwGYpQLrGSYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b95b47a-1ec0-4a94-8f91-4907edfe3595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbP2iFk1RcGUgwYP3WoHxm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
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

_source line 6 · 2026-05-16T15:50:37.067Z_

<details><summary>↩ Tool result · `toolu_0116sNoCnKwt1wFPL4uVcusv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_importance_s015 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition (primary method). DS-R1 importance s015 as first condition. | — | — | — |\\n| c8_llama_n250_fixed | — | — | — | — |\\n\\n## 待处理\\n- gpqa_ds_importance_s020（排队等待 GPU）\\n\\n## 近期结论\\n- **c8_llama_gpu0_s025** (success): Pre-emptive run of LLaMA importance s025 on GPU 0 to accelerate c8_llama_n250_fixed (4-round serial → 3-round by pre-completing round 2 condition) ← 基于 c8_llama_n250_fixed\\n- **c10_lang_s020_s025** (success): —\\n- **c4_think_validation_math500** (success): —\\n  [c4_think_validation_math500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c4_think_validation_math500/data/c4_think_validation_math500.txt)\\n\\n## 趋势\\n成功 65 / 负向 17 / 失败 17 / 共 129\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 2761, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b95b47a-1ec0-4a94-8f91-4907edfe3595",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "fc56a203-a2a7-4eab-aa94-5f6aa8614727",
  "sourceToolAssistantUUID": "6b95b47a-1ec0-4a94-8f91-4907edfe3595",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T15:50:37.397Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01EpYwSxba8FKKiCesJEiMtM`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc56a203-a2a7-4eab-aa94-5f6aa8614727",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WjyPbbvwGYpQLrGSYP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8ac6d35-14ae-4d52-97ad-ca63929369e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbP2iFk1RcGUgwYP3WoHxm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 15768,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 15768,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1269,
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

_source line 8 · 2026-05-16T15:50:37.409Z_

<details><summary>↩ Tool result · `toolu_01EpYwSxba8FKKiCesJEiMtM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\"\\n  authors: Mozaffari et al.\\n  venue: ICML 2025\\n  year: 2025\\n  category: method-component\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\n\\n- paper_id: unicomp-2026\\n  title: \\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\"\\n  authors: Wang et al.\\n  venue: arXiv 2602.09130\\n  year: 2026\\n  category: evaluation\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\n\\n- paper_id: compression-ordering-2025\\n  title: \\\"A Systematic Study of Compression Ordering for Large Language Models\\\"\\n  venue: arXiv 2511.19495\\n  year: 2025\\n  category: background\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\n\\n- paper_id: phase-transition-compression-2026\\n  title: \\\"Phase Transitions in Large Language Model Compression\\\"\\n  authors: Ma et al.\\n  venue: npj Artificial Intelligence (Nature), 2026\\n  year: 2026\\n  category: background\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\n\\n- paper_id: graspune-acl2026\\n  title: \\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\"\\n  authors: Wang et al.\\n  venue: ACL 2026 Main\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\n\\n- paper_id: mustafar-neurips2025\\n  title: \\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\"\\n  authors: Joo et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\n\\n# ============================================================\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\n# ============================================================\\n\\n- paper_id: decision-repr-transition-2026\\n  title: \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\"\\n  venue: arXiv 2605.07271\\n  year: 2026\\n  category: background\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\n\\n- paper_id: doing-more-with-less-2026\\n  title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n  venue: arXiv 2604.25098\\n  year: 2026\\n  category: background\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\n\\n- paper_id: sparse-frontier-2025\\n  title: \\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\"\\n  venue: arXiv 2504.17768\\n  year: 2025\\n  category: evaluation\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\n\\n# ============================================================\\n# 新增 — Adaptive / Learned Controllers\\n# ============================================================\\n\\n- paper_id: obcache-2025\\n  title: \\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\"\\n  venue: arXiv 2510.07651\\n  year: 2025\\n  category: method-component\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\n\\n- paper_id: pagedeviction-eacl2026\\n  title: \\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\"\\n  venue: EACL 2026 Findings\\n  year: 2026\\n  category: method-component\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\n\\n- paper_id: adakv-neurips2025\\n  title: \\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\n\\n- paper_id: sol-2026\\n  title: \\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\"\\n  venue: arXiv 2605.10875\\n  year: 2026\\n  category: method-component\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\n\\n# ============================================================\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\n# ============================================================\\n\\n- paper_id: twilight-neurips2025\\n  title: \\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\"\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\n  venue: NeurIPS 2025 Spotlight\\n  year: 2025\\n  category: method-component\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\n\\n- paper_id: lava-emnlp2025\\n  title: \\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\"\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  category: method-component\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\n\\n- paper_id: lkv-2026\\n  title: \\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\"\\n  venue: arXiv 2605.06676\\n  year: 2026\\n  category: method-component\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\n\\n- paper_id: defensivekv-iclr2026\\n  title: \\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\"\\n  venue: ICLR 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\n\\n- paper_id: retentivekv-2026\\n  title: \\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\"\\n  venue: arXiv 2605.04075\\n  year: 2026\\n  category: background\\n  relevance: \\\"Deferred Importance\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\n\\n- paper_id: pitfalls-kvcache-2025\\n  title: \\\"The Pitfalls of KV Cache Compression\\\"\\n  venue: arXiv 2510.00231\\n  year: 2025\\n  category: background\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\n\\n- paper_id: greedy-bias-kvcache-2026\\n  title: \\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\"\\n  venue: arXiv 2602.02199\\n  year: 2026\\n  category: background\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\n\\n- paper_id: thinking-tokens-mi-neurips2025\\n  title: \\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\n\\n- paper_id: lserve-mlsys2025\\n  title: \\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\"\\n  venue: MLSys 2025\\n  year: 2025\\n  category: background\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\n\\n- paper_id: squeezeattention-iclr2025\\n  title: \\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\"\\n  venue: ICLR 2025\\n  year: 2025\\n  category: method-component\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\n\\n- paper_id: nsa-acl2025\\n  title: \\\"NSA: Native Sparse Attention\\\"\\n  authors: DeepSeek\\n  venue: ACL 2025 Best Paper\\n  year: 2025\\n  category: background\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\n\\n- paper_id: evicpress-2025\\n  title: \\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\"\\n  venue: arXiv 2512.14946\\n  year: 2025\\n  category: method-component\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\n\\n- paper_id: phase-transition-pruning-thermo-2026\\n  title: \\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\"\\n  venue: arXiv 2602.15224\\n  year: 2026\\n  category: background\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\n\\n- paper_id: token-budget-aware-acl2025\\n  title: \\\"Token-Budget-Aware LLM Reasoning\\\"\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  category: background\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\n\\n# ============================================================\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\n# ============================================================\\n\\n- paper_id: physics-kvcache-2026\\n  title: \\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\"\\n  venue: arXiv 2603.01426\\n  year: 2026\\n  category: background\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\n\\n- paper_id: rkv-neurips2025\\n  title: \\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\"\\n  authors: Cai et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\n\", \"total_chars\": 13069, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8ac6d35-14ae-4d52-97ad-ca63929369e9",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "97139c15-b30a-4bbd-b880-5314a9ada550",
  "sourceToolAssistantUUID": "d8ac6d35-14ae-4d52-97ad-ca63929369e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T15:50:41.566Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01V2tbn29JFWgHotw7c784zu`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97139c15-b30a-4bbd-b880-5314a9ada550",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WkFSFU74bGX16XJwYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a82a7903-99bd-4ebf-9d8b-3a33ba3b4788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3uRZrKZRwZxJsNYezE3bA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7327,
      "cache_read_input_tokens": 17037,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7327,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 10 · 2026-05-16T15:50:41.587Z_

<details><summary>↩ Tool result · `toolu_01V2tbn29JFWgHotw7c784zu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a82a7903-99bd-4ebf-9d8b-3a33ba3b4788",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "3c083318-a4c3-4010-a949-b8df083b0f3a",
  "sourceToolAssistantUUID": "a82a7903-99bd-4ebf-9d8b-3a33ba3b4788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T15:50:42.037Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019jCr2tyfMgZqzxX7gvZZiU`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c083318-a4c3-4010-a949-b8df083b0f3a",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WkFSFU74bGX16XJwYE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95d56bb0-f312-48d1-881a-c87ba7721e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3uRZrKZRwZxJsNYezE3bA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7327,
      "cache_read_input_tokens": 17037,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7327
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 17037,
          "cache_creation_input_tokens": 7327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7327,
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

_source line 12 · 2026-05-16T15:50:42.050Z_

<details><summary>↩ Tool result · `toolu_019jCr2tyfMgZqzxX7gvZZiU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-16 (数值对齐 n=500 registry: DS median_diff 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16; Cohen's d registry 0.61→1.13/0.37→1.44; C7+C10 status→confirmed; imp/rand 2.7-15×) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-15×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060）qualitative direction consistent（within-importance d_z~1.0），但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 0.19→0.34, 仅 s030 显著），且 random 在 LLaMA 上也显示显著 phase gradient（d_z 0.35→0.44），与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-36× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-15×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c3_llama, D060）：qualitative direction consistent（importance phase gradient d_z≈1.0），但 imp_vs_rand 交互弱（d_z 0.19→0.34, 仅 s030 显著），且 random 也显示非平凡 phase gradient（d_z 0.35→0.44），strategy-dependence 强度 architecture-dependent。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\\\\\\\\\"emergent phase-strategy interaction\\\\\\\\\\\\\\\"\\n- MUST NOT: \\\\\\\\\\\\\\\"importance metric limitation / importance is broken\\\\\\\\\\\\\\\"\\n- MUST NOT: claim \\\\\\\\\\\\\\\"importance masking produces super-additive interaction\\\\\\\\\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-15× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-36× random; GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\\n| C8 | Cross-architecture validation (LLaMA) | partially_confirmed | D060: within-importance phase gradient 强(d_z~1.0) ✓，但 imp_vs_rand 交互弱(d_z 0.19→0.34, 仅 s030 Bonferroni p=0.029 显著)。**关键**：random 在 LLaMA 上也显示显著 phase gradient(d_z 0.35→0.44, CI 排除零)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Qualitative direction consistent, quantitative strategy×phase interaction weaker + architecture-dependent。论文禁用 \\\"confirms\\\"，改用 \\\"suggests\\\"/\\\"provides partial support\\\"。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c3_llama (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM)，qualitative direction consistent，但需加限定——LLaMA 上 random 也显示 phase gradient，strategy × phase 交互弱于 Qwen2 架构（D060）(3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-36× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) LLaMA 跨架构验证 n=50 限制功效；(d) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c3_llama cross-architecture) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Mechanism — entropy-discrimination collapse 缺乏直接测量\\n- **预期质疑**: \\\\\\\"The mechanism is conceptual. Where is the empirical evidence for entropy increase and discrimination collapse?\\\\\\\"\\n- **应对**: c4_entropy 实验已完成（DeepSeek 30/30 + Qwen 30/30）。D044 结论：Gini/CV 下降跨模型一致（discrimination collapse confirmed）；entropy redistribution 在 DeepSeek 上一致但在 Qwen 上 s025 方向反转、s030 近零（model-dependent）。论文以 discrimination collapse 为主线，entropy 作 DeepSeek 特有的强化因素。\\n- **实验支撑**: c4_entropy (DeepSeek DONE) + qwen_c4_entropy (DONE, negative for entropy universality)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 running)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 running)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA) replication 验证泛化性（三模型两架构；LLaMA partially_confirmed，strategy×phase 交互强度 architecture-dependent, D060）\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 12640, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95d56bb0-f312-48d1-881a-c87ba7721e38",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "de02d5c5-ae81-4b0c-8ecd-08bba46e5253",
  "sourceToolAssistantUUID": "95d56bb0-f312-48d1-881a-c87ba7721e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T15:50:49.672Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KpJdT5N6afBZ99ZboEM4V7`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de02d5c5-ae81-4b0c-8ecd-08bba46e5253",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6Wkb4Cg389XWNQ1WScF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f77d57b8-a1fe-41f8-9a27-c1957e798557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NweEHwVh6HVve8xBRenxFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6340,
      "cache_read_input_tokens": 24364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6340,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 32,
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

_source line 14 · 2026-05-16T15:50:49.692Z_

<details><summary>↩ Tool result · `toolu_01KpJdT5N6afBZ99ZboEM4V7`</summary>

```text
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/dream_reports/dream_20260516T150210/best/paper.tex
artifacts/dream_reports/dream_20260516T150210/median/paper.tex
artifacts/dream_reports/dream_20260516T150210/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f77d57b8-a1fe-41f8-9a27-c1957e798557",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "a8dacca3-e2b7-4861-8f48-0f880d2fbdff",
  "sourceToolAssistantUUID": "f77d57b8-a1fe-41f8-9a27-c1957e798557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T15:50:49.811Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01F53ixxdGRADYB89MAtyvHq`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8dacca3-e2b7-4861-8f48-0f880d2fbdff",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6Wkb4Cg389XWNQ1WScF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0e28f5d-b4b5-4d23-b156-3712208bc655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NweEHwVh6HVve8xBRenxFN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6340,
      "cache_read_input_tokens": 24364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6340,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 32,
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

_source line 16 · 2026-05-16T15:50:49.823Z_

<details><summary>↩ Tool result · `toolu_01F53ixxdGRADYB89MAtyvHq`</summary>

```text
artifacts/_project/paper/main_00fdd3.pdf
artifacts/_project/paper/main_5d82e3.pdf
artifacts/_project/paper/main_c93d3b.pdf
artifacts/_project/paper/main_9a05ce.pdf
artifacts/_project/paper/main_a1a036.pdf
artifacts/_project/paper/main_bdfc72.pdf
artifacts/_project/paper/figures/fig3_crossover.pdf
artifacts/_project/paper/figures/fig4_bootstrap.pdf
artifacts/_project/paper/figures/fig5_crossmodel.pdf
artifacts/_project/paper/main_95b922.pdf
artifacts/main.pdf
artifacts/main_r6_revised.pdf
artifacts/main_r7_revised.pdf
artifacts/_project/chart/figure1_n500_69c0c8.pdf
artifacts/_project/chart/figure1_n500.pdf
artifacts/m2_figure1_n500/figure1_n500.pdf
artifacts/_project/paper/figures/fig1_dose_response.pdf
artifacts/_project/chart/fig1_dose_response.pdf
artifacts/_project/paper/fig1_ii_scatter.pdf
artifacts/dream_reports/dream_20260516T073742/best/paper.pdf
artifacts/dream_reports/dream_20260516T073742/median/paper.pdf
artifacts/dream_reports/dream_20260516T073742/worst/paper.pdf
artifacts/_project/paper/main.pdf
artifacts/dream_reports/dream_20260516T150210/best/paper.pdf
artifacts/dream_reports/dream_20260516T150210/median/paper.pdf
artifacts/dream_reports/dream_20260516T150210/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0e28f5d-b4b5-4d23-b156-3712208bc655",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "756a79c2-4c2b-450a-9a88-b7f77b0083d8",
  "sourceToolAssistantUUID": "e0e28f5d-b4b5-4d23-b156-3712208bc655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T15:50:52.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rzv4JKK6nV9D7dfKQYD5Rj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "756a79c2-4c2b-450a-9a88-b7f77b0083d8",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmAXMP4759veAanBYi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de4d3267-c85f-409d-9372-9a8cdfb3c00f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kxg69Se1pU3RCbqxYYQKx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 952,
      "cache_read_input_tokens": 30704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 952,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
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

_source line 18 · 2026-05-16T15:50:52.800Z_

<details><summary>↩ Tool result · `toolu_01Rzv4JKK6nV9D7dfKQYD5Rj`</summary>

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	
22	\title{Phase-Modulated Compound Sparsity Severity\\in 7B-Scale Mathematical Reasoning Models}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	\input{related_work}
34	\input{background}
35	\input{methodology}
36	\input{results}
37	\input{analysis}
38	\input{discussion}
39	\input{conclusion}
40	
41	\bibliography{references}
42	
43	\section*{Limitations}
44	\input{limitations}
45	
46	\section*{Reproducibility}
47	Code and data will be released upon acceptance.
48	
49	\appendix
50	\input{appendix}
51	\input{appendix_moved}
52	\input{appendix_disc_analysis}
53	\input{appendix_robustness}
54	
55	\end{document}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de4d3267-c85f-409d-9372-9a8cdfb3c00f",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "f7fe8dc1-e481-42e6-8753-1a326af9ef2f",
  "sourceToolAssistantUUID": "de4d3267-c85f-409d-9372-9a8cdfb3c00f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T15:50:53.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_018gTJbSvockWVRLYXCL8Wtn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7fe8dc1-e481-42e6-8753-1a326af9ef2f",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmAXMP4759veAanBYi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02b49be1-b45f-4b68-a5b0-d5a6ead930d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kxg69Se1pU3RCbqxYYQKx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 952,
      "cache_read_input_tokens": 30704,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 952
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 30704,
          "cache_creation_input_tokens": 952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 952,
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

_source line 20 · 2026-05-16T15:50:53.384Z_

<details><summary>↩ Tool result · `toolu_018gTJbSvockWVRLYXCL8Wtn`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	PM-KVQ~\cite{pmkvq-iclr2026} shows that progressive quantization---gradually reducing bit-width over the generation process---mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent.
11	
12	\cite{kim2026pqqp} show that compression order (prune-then-quantize vs.\ quantize-then-prune) substantially affects joint quality, and their Progressive Intensity Hypothesis---that weaker perturbations should precede stronger ones---echoes our dose-response finding that interaction severity increases monotonically with sparsity.
13	
14	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
15	
16	\paragraph{KV cache eviction.}
17	StreamingLLM~\cite{streamingllm-iclr2024} establishes attention sinks as a foundational mechanism; DuoAttention~\cite{duoattention-2024} classifies heads into retrieval and streaming types, complementing our analysis of importance discrimination collapse (\S\ref{sec:discrimination-collapse-main}). Subsequent work improves eviction through per-head adaptive budgets \cite{adakv-neurips2025}, observation-window compression \cite{snapkv-neurips2024}, proxy-token strategies \cite{nacl-acl2024}, deferred importance \cite{retentivekv-2026}, and worst-case analysis \cite{defensivekv-iclr2026}; \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias. \cite{hies-2025} independently show that importance discrimination collapses under heavy single-axis pruning; our results extend this to the compound setting, revealing phase-modulated amplification and a strategy crossover (\S\ref{sec:crossover}) absent in single-axis analysis.
18	Recent approaches target reasoning-aware eviction \cite{rlkv-2025, longflow-2026, dong2026foresightkv}, temporal adaptivity \cite{lethe-aaai2026}, channel-level pruning \cite{xu2025think, spark-aaai2026}, and learned budgets \cite{lkv-2026}. Concurrent work~\citep{hold-onto-thought-neurips2025} evaluates single-axis compression on mathematical reasoning; we extend to the compound setting.
19	These methods each optimize a single pruning axis without characterizing compound interactions.
20	
21	\paragraph{Phase-aware inference.}
22	ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
23	\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
24	\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
25	\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.
26	R-KV~\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.
27	These works establish phase-dependent compression tolerance along single axes.
28	Our work bridges this by quantifying how compound severity varies across phases and eviction strategies.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02b49be1-b45f-4b68-a5b0-d5a6ead930d3",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "06d346c2-61ca-4287-9db5-b5c39fa678e8",
  "sourceToolAssistantUUID": "02b49be1-b45f-4b68-a5b0-d5a6ead930d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T15:50:57.387Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KbMmPD2yoSWHPUH9oB3cv7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06d346c2-61ca-4287-9db5-b5c39fa678e8",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmRv4SiR998BTaXnJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "83abe1d9-8a56-4983-8210-c8bf0a55672f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XUzzGQAvHhrhg19hxzLrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1809,
      "cache_read_input_tokens": 31656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 22 · 2026-05-16T15:50:57.392Z_

<details><summary>↩ Tool result · `toolu_01KbMmPD2yoSWHPUH9oB3cv7`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and generalizes to LlamaForCausalLM ($n{=}250$; monotonic gradient confirmed, ${\sim}25{\times}$ smaller magnitude).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	These findings challenge the assumption of uniform compound interaction and establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled framework for diagnosing where and why compound sparsity fails, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83abe1d9-8a56-4983-8210-c8bf0a55672f",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "671291b3-a281-4720-80ac-8f532fbb5fc6",
  "sourceToolAssistantUUID": "83abe1d9-8a56-4983-8210-c8bf0a55672f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T15:50:57.592Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EEFNppS7PeqmgrHSBTENha`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "671291b3-a281-4720-80ac-8f532fbb5fc6",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmRv4SiR998BTaXnJc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63c8b2f9-2828-48b7-92a2-9e02b890c212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XUzzGQAvHhrhg19hxzLrt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1809,
      "cache_read_input_tokens": 31656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1809,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 24 · 2026-05-16T15:50:57.597Z_

<details><summary>↩ Tool result · `toolu_01EEFNppS7PeqmgrHSBTENha`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose chain-of-thought generations \cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \cite{hies-2025}, greedy bias \cite{greedy-bias-kvcache-2026}, and temporal dynamics \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We find that compound sparsity severity is an emergent property of the three-way interaction among eviction strategy, reasoning phase, and sparsity level.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity reasoning phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), the paired median difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
15	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with cross-architecture confirmation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the monotonic phase gradient is validated with ${\sim}25{\times}$ smaller magnitude than Qwen2-architecture models.
16	Random eviction develops a detectable phase gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \geq 0.25$), supporting that the dominant gradient is strategy-specific.
17	Cross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\Delta$: $0.24 \to 4.68$; all $p \leq 0.0003$), while Qwen shows directional consistency at $s \geq 0.25$ but is inconclusive due to generation truncation (\S\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.
18	
19	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
20	
21	Beyond individual findings, we contribute a \emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.
22	
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
26	    \item We replicate the pattern \textbf{across models and architectures}: Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$) and DeepSeek-R1-Distill-Llama-8B ($n{=}250$; monotonic gradient confirmed, ${\sim}25{\times}$ reduced magnitude; \S\ref{sec:cross-arch}).
27	    \item We identify \textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\S\ref{sec:analysis}).
28	    \item We validate the phase gradient on \textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\S\ref{sec:cross-benchmark}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63c8b2f9-2828-48b7-92a2-9e02b890c212",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "4d7fbc69-2a43-4ef4-bf78-633d6a38a245",
  "sourceToolAssistantUUID": "63c8b2f9-2828-48b7-92a2-9e02b890c212",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T15:51:00.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YDsUPHGQsqUxJnYqbKoXf6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7fbc69-2a43-4ef4-bf78-633d6a38a245",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmjxGRJwnftJbdhe4X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edd0daf3-afe4-46a1-a997-b47a1af733ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113t1tvgdadvexZ9P7BtrSx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2464,
      "cache_read_input_tokens": 33465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2464,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 26 · 2026-05-16T15:51:00.695Z_

<details><summary>↩ Tool result · `toolu_01YDsUPHGQsqUxJnYqbKoXf6`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\Delta$ from $0.39$ to $8.48$ (all $p \ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \geq 0.25$ ($\Delta{=}0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$), $15$--$17{\times}$ smaller than importance-based at matched sparsity. Figure~\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\ref{app:g-metric}.
30	Under the multiplicative null ($r_b = r_a \cdot r_k$; Appendix~\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$); we report additive-null values throughout as the more conservative estimates.
31	
32	\begin{table*}[t]
33	\centering
34	\small
35	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta{=}\widetilde{\mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
36	\label{tab:main-results}
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
40	\midrule
41	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
42	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $< 10^{-10}$ \\
43	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & ns \\
44	\addlinespace
45	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $< 10^{-10}$ \\
46	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & ns \\
47	\addlinespace
48	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $< 10^{-10}$ \\
49	0.25 & Random     & 1.113 & 1.514 & 0.26\; $[0.13,\; 0.35]$ & $< 0.006$ \\
50	\addlinespace
51	0.30 & Importance & 0.038 & 8.456 & 8.48\; $[7.75,\; 9.69]$ & $< 10^{-10}$ \\
52	0.30 & Random     & 3.112 & 3.848 & 0.51\; $[0.26,\; 0.89]$ & $< 0.006$ \\
53	\midrule
54	\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
55	0.15 & Importance & $-$0.000$^{\ddagger}$ & 0.044 & 0.07\; $[0.05,\; 0.09]$ & $< 10^{-14}$ \\
56	0.15 & Random     & 0.094 & 0.097 & $-$0.01\; $[-0.04,\; 0.01]$ & ns \\
57	\addlinespace
58	0.20 & Importance & 0.000 & 0.275 & 0.31\; $[0.26,\; 0.36]$ & $< 10^{-14}$ \\
59	0.20 & Random     & 0.291 & 0.356 & 0.02\; $[-0.01,\; 0.07]$ & ns \\
60	\addlinespace
61	0.25 & Importance & 0.004 & 1.053 & 1.07\; $[0.98,\; 1.18]$ & $< 10^{-14}$ \\
62	0.25 & Random     & 1.108 & 1.769 & 0.39\; $[0.24,\; 0.55]$ & $< 10^{-10}$ \\
63	\addlinespace
64	0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $< 10^{-14}$ \\
65	0.30 & Random     & 2.819 & 4.253 & 0.91\; $[0.61,\; 1.26]$ & $< 10^{-13}$ \\
66	\bottomrule
67	\multicolumn{6}{@{}p{0.92\textwidth}}{\footnotesize $^{\ddagger}$ Negative II at this sparsity reflects \texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\mathrm{II}| < 10^{-4}$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
68	\end{tabular}
69	\end{table*}
70	
71	\begin{figure*}[t]
72	\centering
73	\includegraphics[width=\textwidth]{fig1_ii_scatter.pdf}
74	\caption{Paired median difference $\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \geq 0.25$. Error bars show asymmetric bootstrap 95\% CIs. DeepSeek importance effects are ${\sim}2.7{\times}$ larger than Qwen, consistent with the training-paradigm contrast (\S\ref{sec:cross-model}). Significance: {*}{*}{*}\,$p_{\text{Bonf}} < 0.001$; {*}{*}\,$p_{\text{Bonf}} < 0.01$; ns\,$p_{\text{Bonf}} > 0.05$.}
75	\label{fig:hero}
76	\end{figure*}
77	
78	
79	\subsection{Phase-Strategy Crossover}
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) confirms the monotonic phase gradient for importance-based eviction across $s \in \{0.15, 0.20, 0.25\}$ (Table~\ref{tab:llama-cross-arch}), though with substantially reduced magnitude (approximately $25{\times}$ smaller interaction indices than Qwen2-architecture models). At $s{=}0.25$, the paired median difference $\Delta{=}0.38$ $[0.31,\; 0.40]$ ($p_{\text{Bonf}} < 10^{-37}$, $d_z{=}1.12$), indicating a large within-architecture effect despite the reduced absolute magnitude. The monotonic dose-response across $s{=}0.15$--$0.25$ parallels the Qwen2-family pattern, suggesting that phase-modulated severity generalizes across architecture families while quantitative characteristics remain architecture-specific. Random eviction conditions and $s{=}0.30$ are in progress; strategy${\times}$phase interaction analysis is deferred. Full per-sparsity breakdowns appear in Appendix~\ref{app:cross-arch}.
94	
95	\subsection{Scale Analysis: Qwen2.5-14B}
96	\label{sec:scale-14b}
97	
98	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
104	\label{tab:scale-14b}
105	\begin{tabular}{@{}lcccc@{}}
106	\toprule
107	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
108	\midrule
109	Importance & --- & --- & --- & --- \\
110	Random     & --- & --- & --- & --- \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
116	%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
117	%% (2) whether strategy specificity ratio is scale-invariant,
118	%% (3) comparison of phase segmentation thresholds at larger scale.
119	
120	\subsection{Cross-Benchmark Validation: GSM8K}
121	\label{sec:cross-benchmark}
122	
123	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero). We attribute this to \emph{task complexity}: GSM8K's simpler arithmetic is associated with more uniform attention distributions, yielding a flatter sparsity landscape; within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), supporting cognitive load as the modulating variable. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
124	
125	\paragraph{GSM8K accuracy under compound sparsity.}
126	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
127	
128	\subsection{Cross-Benchmark Validation: GPQA Diamond}
129	\label{sec:cross-benchmark-gpqa}
130	
131	To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
137	\label{tab:gpqa-results}
138	\begin{tabular}{@{}lcccc@{}}
139	\toprule
140	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
141	\midrule
142	DeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\
143	Qwen2.5-7B-Instruct         & --- & --- & --- & --- \\
144	\bottomrule
145	\end{tabular}
146	\end{table}
147	
148	%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
149	%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
150	%% (2) strategy specificity comparison across task types (math vs. science reasoning),
151	%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
152	
153	\subsection{Statistical Validation}
154	\label{sec:stat-validation}
155	
156	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
162	\label{tab:cohens-d}
163	\begin{tabular}{@{}lcc@{}}
164	\toprule
165	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
166	\midrule
167	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
168	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
169	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
170	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
171	\bottomrule
172	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
173	\end{tabular}
174	\end{table}
175	
176	\subsection{Answer-Region Analysis}
177	\label{sec:answer-region}
178	
179	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
180	
181	\subsection{Downstream Accuracy Validation}
182	\label{sec:accuracy-validation}
183	
184	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
185	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
186	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\%$--$76\%$, should be interpreted as qualitative observations only.
187	
188	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edd0daf3-afe4-46a1-a997-b47a1af733ca",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "2e47edf3-6353-48bb-a03a-8447680ace6d",
  "sourceToolAssistantUUID": "edd0daf3-afe4-46a1-a997-b47a1af733ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T15:51:00.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_012gD75Nxq7TtxHGx38ojQVJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e47edf3-6353-48bb-a03a-8447680ace6d",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmjxGRJwnftJbdhe4X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8dd7ecf-5633-4bc3-be3d-029270dedd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113t1tvgdadvexZ9P7BtrSx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2464,
      "cache_read_input_tokens": 33465,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2464
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 33465,
          "cache_creation_input_tokens": 2464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2464,
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

_source line 28 · 2026-05-16T15:51:00.937Z_

<details><summary>↩ Tool result · `toolu_012gD75Nxq7TtxHGx38ojQVJ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8dd7ecf-5633-4bc3-be3d-029270dedd4b",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "caaca111-b1e9-4f91-9055-6918fcb6cfae",
  "sourceToolAssistantUUID": "e8dd7ecf-5633-4bc3-be3d-029270dedd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T15:51:05.442Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HFc81m7JtrgBfJxv2vXZX9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caaca111-b1e9-4f91-9055-6918fcb6cfae",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmyiW7Ejd1Ydri8NhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf7f59fb-a02e-43a7-9875-4c0cd5e57a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EphCCr7P1xbv6z2KeUbZnx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7598,
      "cache_read_input_tokens": 35929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7598,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 30 · 2026-05-16T15:51:05.450Z_

<details><summary>↩ Tool result · `toolu_01HFc81m7JtrgBfJxv2vXZX9`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), indicating that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis on Qwen shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level, with monotonically increasing magnitude ($-0.017$ at $s{=}0.15$, $-0.020$ at $s{=}0.20$, $-0.029$ at $s{=}0.25$, $-0.035$ at $s{=}0.30$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	%% TODO: Add per-phase Gini results when available from Agent computation.
17	
18	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
19	\label{sec:entropy-redistribution-main}
20	
21	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf7f59fb-a02e-43a7-9875-4c0cd5e57a88",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "5bc4e5c5-6384-4d37-b983-a51c3cc26525",
  "sourceToolAssistantUUID": "bf7f59fb-a02e-43a7-9875-4c0cd5e57a88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T15:51:06.049Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HuNJGoiKoX9SGjSwm1zDv9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bc4e5c5-6384-4d37-b983-a51c3cc26525",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WmyiW7Ejd1Ydri8NhE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10a8c2b1-ae5e-43ba-968e-55a80c07d822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EphCCr7P1xbv6z2KeUbZnx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7598,
      "cache_read_input_tokens": 35929,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7598
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 35929,
          "cache_creation_input_tokens": 7598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7598,
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

_source line 32 · 2026-05-16T15:51:06.056Z_

<details><summary>↩ Tool result · `toolu_01HuNJGoiKoX9SGjSwm1zDv9`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) confirms that the monotonic phase gradient extends beyond the Qwen2 architecture ($n{=}250$, $d_z{=}1.12$ at $s{=}0.25$; all tested conditions $p_{\text{Bonf}} < 10^{-37}$) but with substantially reduced interaction magnitude (${\sim}25{\times}$ smaller than Qwen2-architecture models). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks---code generation, multi-hop QA---produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Eviction strategy scope and H$_2$O confound.}
8	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring~\cite{h2o-neurips2023}, Eq.~\ref{eq:kv-importance}), which creates an inherent confound: head pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report---including importance discrimination collapse and the phase-strategy crossover---may be partly attributable to this circular dependency rather than to compound sparsity \emph{per se}. Other attention-mass-based methods (SnapKV~\cite{snapkv-neurips2024}, PyramidKV~\cite{pyramidkv-colm2025}) share the same scoring basis and would likely exhibit a similar confound, whereas strategies that do not derive scores from the pruned attention distribution (e.g., learned eviction policies, recency-based heuristics) may exhibit qualitatively different compound interaction dynamics. Disentangling the contribution of score degradation from the intrinsic compound interaction requires testing eviction methods whose scoring is independent of head pruning; this is an important next step.
9	
10	\paragraph{Symmetric sparsity assumption.}
11	Our analysis applies symmetric sparsity levels: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) supports that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
12	
13	\paragraph{Phase segmentation validation.}
14	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.88$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
15	
16	\paragraph{Mechanism.}
17	The importance discrimination collapse mechanism is a correlational marker, not a complete causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
18	
19	\paragraph{Perplexity vs.\ accuracy.}
20	Our primary severity metric is perplexity-based (II), chosen because its per-token granularity enables the phase-level decomposition central to our analysis; accuracy is binary per-problem and cannot be meaningfully decomposed by reasoning phase. Accuracy validation on MATH-500 (\S\ref{sec:accuracy-validation}, Appendix~\ref{app:accuracy-details}) shows gradual decline through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) followed by a sharp cliff at $s{=}0.30$ ($\delta{=}-27$\,pp) for Qwen ($n{=}100$, truncation $\leq 4\%$). DeepSeek accuracy deltas are confounded by rising truncation ($16\%$ to $76\%$); non-truncated analysis reveals a dual-regime structure but is limited by small surviving samples at high sparsity. Comprehensive accuracy evaluation across benchmarks remains an important next step.
21	
22	\paragraph{Sparsity range.}
23	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, sufficient to establish monotonicity at the tested levels (JT test $p \ll 10^{-10}$) but insufficient to characterize the functional form of the auxiliary ratio $G(s)$ or identify potential saturation thresholds. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10a8c2b1-ae5e-43ba-968e-55a80c07d822",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "f9a0e2ae-88aa-4c7e-a11b-19154947a9a4",
  "sourceToolAssistantUUID": "10a8c2b1-ae5e-43ba-968e-55a80c07d822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T15:51:09.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TodVLp1KeYbDXmUv8ubetu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a0e2ae-88aa-4c7e-a11b-19154947a9a4",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WnMae6ihxyswmJsngY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa7eefcf-ef18-4b5a-8441-b50d513711d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dfyshf2i4DZEMuobE127Cf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 43527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3161,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 34 · 2026-05-16T15:51:09.388Z_

<details><summary>↩ Tool result · `toolu_01TodVLp1KeYbDXmUv8ubetu`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ supports robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
12	
13	\paragraph{Phase segmentation and metrics.}
14	Each sequence is segmented into three phases using the quantile-based method (\S\ref{par:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity and II (Eq.~\ref{eq:ii}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1). The amplification ratio $G$ (Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric}. Robustness to segmentation granularity (quartile, quintile; Appendix~\ref{app:seg-robust}) and minimum phase length ($5$, $10$, $20$ tokens; Appendix~\ref{app:mpl-sensitivity}) is verified.
15	
16	\paragraph{Statistical analysis.}
17	\label{par:stats}
18	All reported confidence intervals use nonparametric bootstrap ($B{=}10{,}000$, seed$=$42)~\cite{efron-1993}. Significance tests use Wilcoxon signed-rank (paired within-model) or Mann-Whitney $U$ (cross-training-paradigm), with Bonferroni correction at family-wise $k{=}4$ (per model$\times$strategy combination, 4 sparsity levels testing one dose-response hypothesis): each family tests a single directional question (``does $\Delta$ increase with $s$?'') under fixed model and strategy, making $k{=}4$ the natural grouping. Benjamini-Hochberg FDR correction across all 44 tests is reported as a robustness check in Appendix~\ref{app:bh-fdr}; all Bonferroni-significant results remain significant under BH-FDR. Dose-response monotonicity is supported by the Jonckheere-Terpstra test ($z{=}6.2$--$33.7$, all $p < 10^{-9}$), which uses per-problem values (${\sim}496$ per group) rather than aggregated medians.\footnote{Spearman rank correlation on the four aggregate medians ($\rho{=}1.0$, $n{=}4$; interpret with caution given the small number of levels) is consistent; we rely on the JT test as primary evidence.} Scaling from $n{=}50$ (profiling) to $n{=}500$ narrowed bootstrap CI widths by $2.5$--$5.9{\times}$ across all 16 conditions, showing precision gains. The paired median difference $\Delta$ is the primary metric; $G$ (amplification ratio, Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric} as an auxiliary illustrative ratio.\footnote{Experiments on 4$\times$ professional GPUs with 48\,GB memory.}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa7eefcf-ef18-4b5a-8441-b50d513711d1",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "9434ca69-3522-4069-8a0d-7ac81d93bde4",
  "sourceToolAssistantUUID": "aa7eefcf-ef18-4b5a-8441-b50d513711d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T15:51:09.465Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZkRbGxzhbYBftVEiiaY3W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9434ca69-3522-4069-8a0d-7ac81d93bde4",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WnMae6ihxyswmJsngY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baf545b7-af0b-4553-8ae8-e8d35c43a579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dfyshf2i4DZEMuobE127Cf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 43527,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3161,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 36 · 2026-05-16T15:51:09.471Z_

<details><summary>↩ Tool result · `toolu_01TZkRbGxzhbYBftVEiiaY3W`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}500$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baf545b7-af0b-4553-8ae8-e8d35c43a579",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "a1a17451-1549-4cc3-85a0-fdb9c613d218",
  "sourceToolAssistantUUID": "baf545b7-af0b-4553-8ae8-e8d35c43a579",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T15:51:12.108Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KgCkDi9KGWaDFkdxRpKSs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a17451-1549-4cc3-85a0-fdb9c613d218",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WncMtYfC4F2pYmzNff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a0cbeea-520f-4138-8904-426df2d550e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QT9187nfJNZEEWQCy4ELxE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2069,
      "cache_read_input_tokens": 46688,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 46688,
          "cache_creation_input_tokens": 2069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2069,
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

_source line 38 · 2026-05-16T15:51:12.122Z_

<details><summary>↩ Tool result · `toolu_019KgCkDi9KGWaDFkdxRpKSs`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null as primary: it assumes $r_b = r_a + r_k - 1$ (compound loss equals sum of individual losses), the most conservative independence assumption. Although the two axes are mechanistically linked (\S\ref{sec:analysis}), rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. Appendix~\ref{app:multiplicative-null} reports parallel results under the multiplicative null ($r_b = r_a \cdot r_k$); the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$), supporting null-choice invariance. The II distribution is heavily right-skewed; we report medians throughout.
20	
21	\paragraph{Severity gradient.}
22	To capture phase variation, the per-problem \emph{amplification ratio} is:
23	\begin{equation}
24	    G^{(i)} = \frac{\mathrm{II}^{(i)}_{\,\textit{low}}}{\mathrm{II}^{(i)}_{\,\textit{high}}},
25	    \label{eq:gradient}
26	\end{equation}
27	where $\mathrm{II}^{(i)}_{\,\textit{low/high}}$ is the interaction index in the low/high-sparsity phase for problem $i$. We report $G = \widetilde{G^{(i)}}$, the median across problems, with bootstrap CIs. We use the median of per-problem ratios (not the ratio of medians) to preserve per-problem pairing; see Appendix~\ref{app:profiling-subset} for comparison. $G$ serves as an auxiliary descriptive ratio that illustrates the degree of phase concentration; the primary statistical evidence for the severity gradient rests on $\Delta$ and paired Wilcoxon tests (\S\ref{sec:phase-amplification}).
28	
29	\paragraph{Phase segmentation.}
30	\label{par:phase-segmentation}
31	Inspired by ThinKV's phase-aware perspective on reasoning-time compression~\cite{thinkv-iclr2026}, each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, using a quantile-based segmentation rather than explicit reasoning delimiters (e.g., \texttt{&lt;think>} tokens). Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). We note that this segmentation is an \emph{operationalization choice}: attention sparsity serves as a continuous proxy for reasoning phase rather than a theoretically grounded boundary. We validate robustness to segmentation granularity (tercile/quartile/quintile; Appendix~\ref{app:seg-robust}) and minimum phase length (Appendix~\ref{app:mpl-sensitivity}). Validation against DeepSeek's explicit \texttt{&lt;think>} markers using adaptive per-sequence quantile segmentation yields substantial agreement ($\kappa{=}0.88$, AUC-ROC${=}0.98$; $n{=}48$; Appendix~\ref{app:think-validation}). Details in Appendix~\ref{app:formulation-details}.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a0cbeea-520f-4138-8904-426df2d550e5",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "8e6c2202-3765-4738-84b6-5d0013731b7e",
  "sourceToolAssistantUUID": "1a0cbeea-520f-4138-8904-426df2d550e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-16T15:51:15.210Z_

Now I have a comprehensive understanding of the paper. Let me compile my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6c2202-3765-4738-84b6-5d0013731b7e",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WnoYbTPYPCEc7WTCpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0ac8a48-61f5-4ed7-a683-ae82909f99d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fiVboZQ6vBeqWKoAPGLWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 48757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1509,
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

_source line 40 · 2026-05-16T15:51:16.064Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KzZbdqtJfWZC9fq5WuXxiY`</summary>

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
  "parentUuid": "e0ac8a48-61f5-4ed7-a683-ae82909f99d5",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WnoYbTPYPCEc7WTCpz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29914edc-bafb-4bea-a9e4-6923b6cd2086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fiVboZQ6vBeqWKoAPGLWg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 48757,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 48757,
          "cache_creation_input_tokens": 1509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1509,
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

_source line 41 · 2026-05-16T15:51:16.072Z_

<details><summary>↩ Tool result · `toolu_01KzZbdqtJfWZC9fq5WuXxiY`</summary>

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
  "parentUuid": "29914edc-bafb-4bea-a9e4-6923b6cd2086",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "6a3f60ae-4173-49b4-a4f4-0e3341fc9b2b",
  "sourceToolAssistantUUID": "29914edc-bafb-4bea-a9e4-6923b6cd2086",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T15:51:18.891Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UXShkbTdsQYycfv4iVhTbF`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a3f60ae-4173-49b4-a4f4-0e3341fc9b2b",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6Wo6hiTFrgN1W8KaVuo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5381bdbb-4589-44a4-8078-bf7bc9b5526f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhhqptTsm4KqtEuZHc5cvE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 684,
      "cache_read_input_tokens": 50266,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 50266,
          "cache_creation_input_tokens": 684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 684,
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

_source line 43 · 2026-05-16T15:51:18.894Z_

<details><summary>↩ Tool result · `toolu_01UXShkbTdsQYycfv4iVhTbF`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_post_to_reviewer"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5381bdbb-4589-44a4-8078-bf7bc9b5526f",
  "isSidechain": true,
  "promptId": "9fc20291-e8f1-4e03-bc4b-c7922ed33096",
  "agentId": "abe44e0c67a15047b",
  "type": "user",
  "uuid": "d288a711-673c-492b-9fe5-59398a9d2676",
  "sourceToolAssistantUUID": "5381bdbb-4589-44a4-8078-bf7bc9b5526f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T15:52:35.638Z_


## Review: "Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models"

### Reviewer R2 — Focus: Novelty and Related Work

---

### Summary

This paper empirically characterizes how compound sparsity (simultaneous head pruning + KV cache eviction) produces phase-dependent severity in reasoning models, finding that the interaction is amplified in low-sparsity reasoning phases and monotonically increases with sparsity level. The work identifies "importance discrimination collapse" as a correlational diagnostic mechanism. The contribution is purely empirical characterization — no new method is proposed.

---

### Strengths

- **Well-defined research question**: The three-way interaction (strategy x phase x sparsity) is clearly operationalized via the Interaction Index decomposed by phase, making the claim testable and falsifiable.

- **Thorough statistical methodology**: Per-problem paired bootstrap (B=10,000), Bonferroni correction, Jonckheere-Terpstra tests for monotonicity, and explicit reporting of CIs demonstrate statistical maturity uncommon in empirical ML papers. The scaling from n=50 profiling to n=500 with CI narrowing analysis is commendable.

- **Honest limitations section**: The paper transparently acknowledges the correlational nature of discrimination collapse, the model-dependent entropy results, the H2O confound, and the failed mitigation pilot (C5b). This intellectual honesty strengthens credibility.

- **Multi-axis generalization evidence**: Cross-model (DeepSeek + Qwen), cross-architecture (LLaMA), and cross-benchmark (GSM8K) validation, with appropriate hedging where results are weaker (LLaMA strategy interaction, GSM8K strategy specificity attenuation).

- **Related work section is substantially more thorough than the paper summary suggested**: The actual paper cites approximately 30+ references spanning compound compression, KV cache eviction, and phase-aware inference, not the "7 total" described in the review prompt. This addresses one potential concern significantly.

---

### Weaknesses

**W1: Incremental novelty — the "delta" over existing work is narrow.**
The paper's core finding is that a known phenomenon (super-additive compound degradation, per SparK) varies across a known dimension (reasoning phases, per ThinKV). The Interaction Index is a straightforward algebraic decomposition. The phase segmentation uses attention-sparsity quantiles — a simple operationalization. The novelty is in the *combination* and *quantification*, not in any conceptual or methodological advance. For EMNLP, where empirical findings papers are accepted, this may suffice — but the insight is relatively contained: "compound sparsity hurts more during exploratory reasoning than structured computation." This is intuitively expected (exploratory phases have distributed attention, so evicting tokens is more destructive).

**W2: "Discrimination collapse" reframes HIES without substantial new insight.**
The paper acknowledges that HIES (2025) independently discovered importance score collapse under single-axis pruning. The extension to the compound setting is straightforward (head pruning degrades the scores that importance-based eviction relies on — a circular dependency the paper itself identifies in Limitations). The paper's own analysis admits this is correlational, that both strategies exhibit near-identical Gini drops yet severity diverges by 15-17x, and that "aggregate concentration collapse alone is insufficient." This undermines the mechanistic contribution claim.

**W3: The "uniform compound degradation assumption" is partially a straw man.**
The paper repeatedly claims to "challenge the implicit assumption of uniform compound interaction." But SparK (2024) already shows non-uniform interaction; Physics of KV Cache Compression (2026) characterizes phase transitions; DefensiveKV (2026) shows importance instability. The assumption of uniformity is not widely held in the 2025-2026 literature. The paper's contribution is better framed as *quantifying the phase dimension* of already-known non-uniformity, rather than overturning an assumption.

**W4: No actionable method — the "so what" remains weak.**
The failed mitigation pilot (18% oracle recovery, CI spanning zero) demonstrates that knowing *where* severity concentrates does not straightforwardly translate to improved compression. The paper acknowledges this but frames the finding as "establishing a principled framework." Without evidence that the framework enables better systems, the practical impact is speculative. The "phase-gated analysis framework" amounts to decomposing a metric by quantile — useful but not methodologically novel.

**W5: Placeholder results (14B, GPQA) weaken the submission.**
Tables 3 and 4 contain "---" entries for Qwen2.5-14B and GPQA Diamond experiments. Submitting with placeholder results for claimed experiments is inappropriate. Either complete the experiments or remove the sections entirely.

**W6: The crossover phenomenon is model-specific and underexplained.**
The strategy-ranking reversal (importance < random in high-sparsity phase, importance > random in low-sparsity phase) is presented as a key finding but occurs only on DeepSeek, not Qwen. The paper attributes this to "model-specific attention head specialization patterns" without further analysis. This weakens the generality claim.

**W7: Missing engagement with concurrent and closely related work.**
While the related work is more thorough than initially suggested, several highly relevant threads are underengaged:
- The connection to **MoE/conditional computation** literature (where sparsity is inherent and phase-dependent) is absent.
- **Token-level importance dynamics** work (RetentiveKV's "deferred importance," which is in the literature map but absent from the paper) directly relates to why phase matters.
- The **test-time compute** literature (which intersects with "how much degradation reasoning can tolerate") is not discussed.

---

### Questions for Authors

**Q1**: The Interaction Index assumes an additive null. You show the multiplicative null preserves the gradient. But have you considered that the *expected* interaction under compound sparsity might itself be phase-dependent (e.g., because attention distributions are inherently more fragile in exploratory phases)? If the baseline expectation of interaction is higher in low-sparsity phases, your gradient may simply reflect the baseline rather than an emergent phenomenon.

**Q2**: The 25x magnitude reduction on LLaMA and the lack of strategy x phase crossover on Qwen suggest substantial model dependence. What is the minimum set of models needed to make a generalizable claim? With current evidence, is the phenomenon better characterized as "an effect that occurs on DeepSeek-R1-Distill-Qwen-7B and partially replicates elsewhere"?

**Q3**: Why not test eviction methods whose scoring is independent of the pruned attention (e.g., recency-based, random-with-sink-retention, or learned policies)? This would directly address whether the circular dependency (head pruning degrades scores used for eviction) is the primary driver rather than "compound sparsity per se."

**Q4**: The phase segmentation uses attention-sparsity quantiles, which are computed from the dense model. But under compound sparsity, the attention pattern changes. Are you segmenting based on *where the model would be vulnerable* (dense attention pattern) or *where it actually is vulnerable* (post-pruning pattern)? How sensitive are results to this choice?

**Q5**: Can you clarify why the 14B and GPQA results are placeholders? If these experiments are incomplete, should these sections be removed for submission?

---

### Novelty Assessment

The paper occupies an awkward middle ground between "first to study compound sparsity" (no — SparK, SLiM, UniComp precede it) and "first to propose phase-aware compression" (no — ThinKV, PagedEviction, R-KV precede it). The genuine novelty is in the *intersection*: quantifying how compound interaction severity varies by reasoning phase. This is a valid contribution but a narrow one. The Interaction Index is a simple algebraic decomposition; the phase segmentation is quantile-based; the mechanism (discrimination collapse) is acknowledged as correlational and insufficient. The paper does not propose a new method, algorithm, or framework — the "phase-gated analysis framework" is a description protocol, not a computational contribution.

For EMNLP, empirical findings papers can succeed if the finding is surprising and consequential. The finding here is somewhat intuitive (compound stress hurts more during information-dense reasoning phases) and, critically, does not yet enable better systems (mitigation pilot failed). The dose-response monotonicity and the quantitative characterization are solid empirical work, but the significance for the community is limited without a clear path from characterization to improvement.

Compared to the 2025-2026 literature landscape the authors themselves map (Physics of KV Cache, DefensiveKV, GRASPrune, decision representation transitions), this contribution adds a data point in a rapidly filling space rather than opening a new direction.

---

### Related Work Gaps

1. **H2O (Zhang et al., NeurIPS 2023)** — cited in limitations/discussion but not in Related Work proper, despite being the scoring method used.
2. **StreamingLLM (Xiao et al., ICLR 2024)** — now cited. Good.
3. **Structured pruning foundations** (lottery ticket hypothesis, magnitude pruning, movement pruning) — entirely absent. The head pruning component deserves grounding in this literature.
4. **MoE and conditional computation** — sparsity that is inherently phase/input-dependent. Relevant conceptual parallel absent.
5. **Test-time compute scaling** (e.g., "Doing More With Less" is in lit map but not well-integrated) — directly relevant to whether reasoning models can tolerate sparsity.
6. **RetentiveKV / deferred importance** — in the literature map, directly supports the mechanism, absent from the paper.
7. **Thermodynamic phase transition analysis** (phase-transition-pruning-thermo-2026) — in lit map, would strengthen the theoretical framing, absent from paper.

The related work has improved substantially from an earlier draft (now ~30 citations), but still lacks grounding in foundational pruning work (pre-2024) and does not sufficiently distinguish itself from the rapidly expanding 2025-2026 literature on adaptive/phase-aware compression.

---

### Scores

**Soundness: 4 (Strong)**
The statistical methodology is rigorous, with appropriate paired tests, bootstrap CIs, multiple correction procedures, and honest reporting of null/weak results. The placeholder tables (14B, GPQA) and the correlational-only mechanism are the main deductions.

**Excitement: 2 (Mediocre)**
The finding is incremental and somewhat expected. No new method is proposed. The failed mitigation pilot undermines practical significance. The contribution is a careful quantification of a phenomenon in a space that is rapidly being explored by multiple concurrent works. The paper adds precision but not surprise or direction.

**Overall: 2 (Reject)**
While technically sound, the paper's novelty is too narrow for a top venue. It quantifies a phase-dependent effect that is conceptually expected (compound stress hurts more during information-dense phases), proposes no solution, and the "mechanism" is acknowledged as insufficient. The placeholder tables suggest incomplete work. The contribution would be better suited to a workshop (e.g., Efficient NLP) or as supporting evidence within a methods paper that actually exploits the phase-dependent structure.

---

### Confidence: 4/5

I am familiar with the KV cache compression, structured pruning, and efficient inference literatures. I have read the full paper text and related work. My main uncertainty is whether the EMNLP program committee would weight the statistical rigor and cross-model replication more favorably than I have — some reviewers may view careful empirical characterization as sufficiently valuable even without a method contribution.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d288a711-673c-492b-9fe5-59398a9d2676",
  "isSidechain": true,
  "agentId": "abe44e0c67a15047b",
  "requestId": "req_011Cb6WoJoEjpuvCTdum4x7m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ac65930-fd21-4dc3-8568-ee117f22a1c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "3b278507-b3d6-452e-b8e4-ad54eb721597",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVQtFViLxbXLvhL4xmgqvG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 50950,
      "output_tokens": 2765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2765,
          "cache_read_input_tokens": 50950,
          "cache_creation_input_tokens": 602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 602,
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
