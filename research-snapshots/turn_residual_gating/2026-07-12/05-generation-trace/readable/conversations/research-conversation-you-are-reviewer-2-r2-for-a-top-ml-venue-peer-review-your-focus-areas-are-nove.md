# Research conversation: You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty/significance** and **related work

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6c604a73d32ffd3d.jsonl`
- **Structured JSON:** [`7cc7668e57720c6f08ec.json`](../../sessions/7c/7cc7668e57720c6f08ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-17T03:53:44.051Z_

You are Reviewer 2 (R2) for a top ML venue peer review. Your focus areas are **novelty/significance** and **related work positioning**. Review standard: top ML venue, ~25% acceptance rate, 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

You must be a **blind reviewer** — evaluate the paper purely on its merits.

## Paper Summary

**Title:** Phase-Dependent Compound Sparsity: Reasoning Complexity Modulates the Severity of Pruning-Eviction Interactions

**Core claim:** Compound sparsity (simultaneous attention head pruning + KV cache eviction) has severity that is NOT uniform across generation but depends on reasoning phase, eviction strategy, and sparsity level. The paper proposes "discrimination collapse" as the mechanism.

**Method:**
- Joint attention head pruning (by activation magnitude) + KV cache eviction (H2O-style importance scoring) during inference
- Phase segmentation: 3 phases by token-level perplexity quantile terciles computed from unpruned model
- Interaction Index (II) = Δ_compound − (Δ_prune-only + Δ_evict-only)
- Paired median difference per problem, Wilcoxon signed-rank with bootstrap CIs + Bonferroni
- Three eviction strategies: importance (H2O), random, recency
- Three benchmarks: GSM8K (~500 tokens), MATH-500 (~2500 tokens), GPQA Diamond (~6000 tokens, n=198)
- Three models: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Llama-8B
- Sparsity: s ∈ {0.15, 0.20, 0.25, 0.30}

**Key Results:**
1. Importance eviction shows strong phase-dependent compound interaction, perfect dose-response monotonicity (ρ=1.0)
2. Triple dissociation: importance shows strong gradient; random shows null/negligible; recency shows null
3. Phase gradient scales with reasoning complexity: GPQA > MATH-500 > GSM8K (r=0.997)
4. Strategy specificity increases with reasoning depth: GSM8K 2.8×, MATH-500 16.6×, GPQA 17.1×
5. Mechanism: "discrimination collapse" — Gini coefficient decline of attention scores under pruning

**Related Work as written:**
- KV Cache Compression: H2O, StreamingLLM cited but with [?] placeholders (missing bibliography)
- Attention Head Pruning: brief, no specific citations
- Compound/Phase-Aware: SparK (no year/citation), ThinKV (2025), R-KV (2025), Physics of KV Cache Compression (2026), HIES (2025), Lethe (AAAI 2026)
- Claims novelty of "three-dimensional interaction" analysis (pruning × eviction × phase × strategy)

**Contributions claimed:**
1. Phase-dependent compound severity with perfect dose-response monotonicity
2. Reasoning-complexity gradient (r=0.997)
3. Triple dissociation (importance/random/recency)
4. Discrimination collapse mechanism via Gini coefficient

**Paper structure:** Abstract, Introduction (2pp), Related Work (1p), Method (1p), Results (2p), Discussion (1p), Conclusion (0.5p). Total 6 pages.

**Limitations acknowledged:** 7B models only, no throughput data, architecture-dependent specificity, saturation in specificity between MATH-500 and GPQA

## YOUR REVIEW TASK

Provide a structured review focusing on:

### 1. Summary (2-3 sentences)

### 2. Novelty Assessment
- How novel is the core finding (phase-dependent compound severity)?
- Is "discrimination collapse" a genuinely new insight or a re-framing of known phenomena?
- How does the triple dissociation design compare to methodological precedent?
- Is the reasoning-complexity gradient a meaningful contribution or a correlation?
- What is the real incremental contribution over SparK, ThinKV, HIES, and Physics of KV Cache Compression?

### 3. Related Work Assessment
- Are there missing citations to critical related work?
- The H2O and StreamingLLM citations show as [?] — broken bibliography
- Is the positioning against SparK, ThinKV, R-KV, HIES, Lethe fair and accurate?
- Are there older works on attention score degradation under pruning that should be cited?
- Is the "no precedent" claim for reasoning-complexity gradient justified?

### 4. Significance Assessment
- Does the paper change how practitioners should think about compound compression?
- Is the practical impact (phase-gated controllers showing only 18–32% recovery) sufficient?
- Is the 7B-only limitation critical for the claims made?
- Does the paper provide actionable insights beyond "be aware that compound sparsity is non-uniform"?

### 5. Strengths (bullet points)

### 6. Weaknesses (bullet points)

### 7. Questions for Authors (numbered)

### 8. Scores
- Novelty: X/6
- Presentation: X/6
- Significance: X/6
- Overall: X/6
- Confidence: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "689c0897-0b8a-4e8e-9a44-609c7e89f06b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T03:53:44.056Z_

```json
{
  "parentUuid": "689c0897-0b8a-4e8e-9a44-609c7e89f06b",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
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
  "uuid": "6d1e9826-fcf1-4b25-9121-8373fb919688",
  "timestamp": "2026-05-17T03:53:44.056Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T03:53:48.136Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KF95BMit7i3PhioJQtKUkw`</summary>

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
  "parentUuid": "6d1e9826-fcf1-4b25-9121-8373fb919688",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TtTfqJsH99MNKhp2Xq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8333fbcb-f2ea-4e16-8752-5b8656b1ea60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018t2MBms5M6r94bxZMpN4dX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8425,
      "cache_read_input_tokens": 8252,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8425
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 88,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8425,
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

_source line 4 · 2026-05-17T03:53:48.140Z_

<details><summary>↩ Tool result · `toolu_01KF95BMit7i3PhioJQtKUkw`</summary>

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
  "parentUuid": "8333fbcb-f2ea-4e16-8752-5b8656b1ea60",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "81720286-a226-4a7c-9e2c-74a77f758cfb",
  "sourceToolAssistantUUID": "8333fbcb-f2ea-4e16-8752-5b8656b1ea60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T03:53:56.239Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YFmgJgF2H43oTUTdKnizfn`</summary>

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
  "parentUuid": "81720286-a226-4a7c-9e2c-74a77f758cfb",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TtmA3rUd2VYhayr5m2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0faf885-724a-4107-892d-2fea3345ecc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFdB27fosdEvktP2eaeBq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 6 · 2026-05-17T03:53:56.254Z_

<details><summary>↩ Tool result · `toolu_01YFmgJgF2H43oTUTdKnizfn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_importance_s020 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s020 as second condition (after s015 success). | ~140/198 | — | — |\\n| gpqa_ds_importance_s025 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s025 as third condition (after s015 success, s020 running). | ~53/198 | — | — |\\n| gpqa_ds_importance_s030 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s030 as fourth condition. | ~23/198 | — | — |\\n| gpqa_ds_random_s020 | Cross-task generalization: random eviction control on GPQA Diamond. DS-R1 random s020 to establish baseline phase gradient (expected NS or weak) for strategy specificity comparison. | ~23/198 | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **recency_s025** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.25 condition.\\n  [recency_s025_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s025/report/analysis.md)\\n- **recency_s030** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.30 condition.\\n  [recency_s030_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s030/report/analysis.md)\\n- **recency_s015** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.15 condition.\\n\\n## 趋势\\n成功 70 / 负向 17 / 失败 17 / 共 134\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 4× RTX 6000 Pro — GPU0 gpqa_ds_importance_s020 (PID 580927, ~70%), GPU1 s025 (PID 599103, ~27%), GPU2 s030 (PID 606507, ~12%), GPU3 random_s020 (PID 606658, ~12%)\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 4113, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0faf885-724a-4107-892d-2fea3345ecc9",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "1ed36340-1714-4df4-8fb7-dcf6391f2b6e",
  "sourceToolAssistantUUID": "d0faf885-724a-4107-892d-2fea3345ecc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T03:53:56.709Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PppwxQPWitVt4grjk3reue`</summary>

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
  "parentUuid": "1ed36340-1714-4df4-8fb7-dcf6391f2b6e",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TtmA3rUd2VYhayr5m2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73c7b130-175c-4c7c-b2bc-04d739784a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AFdB27fosdEvktP2eaeBq6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 16677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1269,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 8 · 2026-05-17T03:53:56.732Z_

<details><summary>↩ Tool result · `toolu_01PppwxQPWitVt4grjk3reue`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\"\\n  authors: Mozaffari et al.\\n  venue: ICML 2025\\n  year: 2025\\n  category: method-component\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\n\\n- paper_id: unicomp-2026\\n  title: \\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\"\\n  authors: Wang et al.\\n  venue: arXiv 2602.09130\\n  year: 2026\\n  category: evaluation\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\n\\n- paper_id: compression-ordering-2025\\n  title: \\\"A Systematic Study of Compression Ordering for Large Language Models\\\"\\n  venue: arXiv 2511.19495\\n  year: 2025\\n  category: background\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\n\\n- paper_id: phase-transition-compression-2026\\n  title: \\\"Phase Transitions in Large Language Model Compression\\\"\\n  authors: Ma et al.\\n  venue: npj Artificial Intelligence (Nature), 2026\\n  year: 2026\\n  category: background\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\n\\n- paper_id: graspune-acl2026\\n  title: \\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\"\\n  authors: Wang et al.\\n  venue: ACL 2026 Main\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\n\\n- paper_id: mustafar-neurips2025\\n  title: \\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\"\\n  authors: Joo et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\n\\n# ============================================================\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\n# ============================================================\\n\\n- paper_id: decision-repr-transition-2026\\n  title: \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\"\\n  venue: arXiv 2605.07271\\n  year: 2026\\n  category: background\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\n\\n- paper_id: doing-more-with-less-2026\\n  title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n  venue: arXiv 2604.25098\\n  year: 2026\\n  category: background\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\n\\n- paper_id: sparse-frontier-2025\\n  title: \\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\"\\n  venue: arXiv 2504.17768\\n  year: 2025\\n  category: evaluation\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\n\\n# ============================================================\\n# 新增 — Adaptive / Learned Controllers\\n# ============================================================\\n\\n- paper_id: obcache-2025\\n  title: \\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\"\\n  venue: arXiv 2510.07651\\n  year: 2025\\n  category: method-component\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\n\\n- paper_id: pagedeviction-eacl2026\\n  title: \\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\"\\n  venue: EACL 2026 Findings\\n  year: 2026\\n  category: method-component\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\n\\n- paper_id: adakv-neurips2025\\n  title: \\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\n\\n- paper_id: sol-2026\\n  title: \\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\"\\n  venue: arXiv 2605.10875\\n  year: 2026\\n  category: method-component\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\n\\n# ============================================================\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\n# ============================================================\\n\\n- paper_id: twilight-neurips2025\\n  title: \\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\"\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\n  venue: NeurIPS 2025 Spotlight\\n  year: 2025\\n  category: method-component\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\n\\n- paper_id: lava-emnlp2025\\n  title: \\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\"\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  category: method-component\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\n\\n- paper_id: lkv-2026\\n  title: \\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\"\\n  venue: arXiv 2605.06676\\n  year: 2026\\n  category: method-component\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\n\\n- paper_id: defensivekv-iclr2026\\n  title: \\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\"\\n  venue: ICLR 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\n\\n- paper_id: retentivekv-2026\\n  title: \\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\"\\n  venue: arXiv 2605.04075\\n  year: 2026\\n  category: background\\n  relevance: \\\"Deferred Importance\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\n\\n- paper_id: pitfalls-kvcache-2025\\n  title: \\\"The Pitfalls of KV Cache Compression\\\"\\n  venue: arXiv 2510.00231\\n  year: 2025\\n  category: background\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\n\\n- paper_id: greedy-bias-kvcache-2026\\n  title: \\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\"\\n  venue: arXiv 2602.02199\\n  year: 2026\\n  category: background\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\n\\n- paper_id: thinking-tokens-mi-neurips2025\\n  title: \\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\n\\n- paper_id: lserve-mlsys2025\\n  title: \\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\"\\n  venue: MLSys 2025\\n  year: 2025\\n  category: background\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\n\\n- paper_id: squeezeattention-iclr2025\\n  title: \\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\"\\n  venue: ICLR 2025\\n  year: 2025\\n  category: method-component\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\n\\n- paper_id: nsa-acl2025\\n  title: \\\"NSA: Native Sparse Attention\\\"\\n  authors: DeepSeek\\n  venue: ACL 2025 Best Paper\\n  year: 2025\\n  category: background\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\n\\n- paper_id: evicpress-2025\\n  title: \\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\"\\n  venue: arXiv 2512.14946\\n  year: 2025\\n  category: method-component\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\n\\n- paper_id: phase-transition-pruning-thermo-2026\\n  title: \\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\"\\n  venue: arXiv 2602.15224\\n  year: 2026\\n  category: background\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\n\\n- paper_id: token-budget-aware-acl2025\\n  title: \\\"Token-Budget-Aware LLM Reasoning\\\"\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  category: background\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\n\\n# ============================================================\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\n# ============================================================\\n\\n- paper_id: physics-kvcache-2026\\n  title: \\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\"\\n  venue: arXiv 2603.01426\\n  year: 2026\\n  category: background\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\n\\n- paper_id: rkv-neurips2025\\n  title: \\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\"\\n  authors: Cai et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\n\", \"total_chars\": 13069, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73c7b130-175c-4c7c-b2bc-04d739784a33",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "5d58938f-7f53-41aa-8c52-6fa0b328b178",
  "sourceToolAssistantUUID": "73c7b130-175c-4c7c-b2bc-04d739784a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T03:54:01.796Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01T3N7i31T9DKcVdVLGcgPbv`</summary>

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
  "parentUuid": "5d58938f-7f53-41aa-8c52-6fa0b328b178",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TuQLSXEAVcC23BXwiS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "498c0197-352e-4d6f-9c32-e562a4484d95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFJCMGWHZQm3AxKCpbUhX1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7696,
      "cache_read_input_tokens": 17946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7696,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 10 · 2026-05-17T03:54:01.823Z_

<details><summary>↩ Tool result · `toolu_01T3N7i31T9DKcVdVLGcgPbv`</summary>

```text
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
artifacts/dream_reports/dream_20260516T150210/best/paper.tex
artifacts/dream_reports/dream_20260516T150210/median/paper.tex
artifacts/dream_reports/dream_20260516T150210/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/dream_reports/dream_20260516T164305/best/paper.tex
artifacts/dream_reports/dream_20260516T164305/median/paper.tex
artifacts/dream_reports/dream_20260516T164305/worst/paper.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/drafts/recency_control_section.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/abstract.tex
artifacts/dream_reports/dream_20260517T005655/best/paper.tex
artifacts/dream_reports/dream_20260517T005655/median/paper.tex
artifacts/dream_reports/dream_20260517T005655/worst/paper.tex
artifacts/dream_reports/dream_20260517T013445/best/paper.tex
artifacts/dream_reports/dream_20260517T013445/median/paper.tex
artifacts/dream_reports/dream_20260517T013445/worst/paper.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/discussion.tex
artifacts/dream_reports/dream_20260517T032843/best/paper.tex
artifacts/dream_reports/dream_20260517T032843/median/paper.tex
artifacts/dream_reports/dream_20260517T032843/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "498c0197-352e-4d6f-9c32-e562a4484d95",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "1515d8c3-78f0-48c6-b834-7253782f3cb1",
  "sourceToolAssistantUUID": "498c0197-352e-4d6f-9c32-e562a4484d95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T03:54:02.304Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HxLNpUoA3LjxEgZeQRi61F`</summary>

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
  "parentUuid": "1515d8c3-78f0-48c6-b834-7253782f3cb1",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TuQLSXEAVcC23BXwiS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53b21fd1-3c7b-4481-af10-c523fdf17650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFJCMGWHZQm3AxKCpbUhX1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7696,
      "cache_read_input_tokens": 17946,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7696
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 17946,
          "cache_creation_input_tokens": 7696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7696,
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

_source line 12 · 2026-05-17T03:54:02.328Z_

<details><summary>↩ Tool result · `toolu_01HxLNpUoA3LjxEgZeQRi61F`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53b21fd1-3c7b-4481-af10-c523fdf17650",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "9b1a84a2-97b8-4457-9f8a-61558f2d4ab0",
  "sourceToolAssistantUUID": "53b21fd1-3c7b-4481-af10-c523fdf17650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T03:54:07.352Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XM1hjkwj8idYZ6v5UDiXZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b1a84a2-97b8-4457-9f8a-61558f2d4ab0",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7Tuot2uXsM6KKXaARVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11125cd6-9c8c-4c78-8281-da71d7997276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh3p8rDVUmWMqrWZ6Qt5rs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 25642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 872,
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

_source line 14 · 2026-05-17T03:54:07.389Z_

<details><summary>↩ Tool result · `toolu_01XM1hjkwj8idYZ6v5UDiXZH`</summary>

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
  "parentUuid": "11125cd6-9c8c-4c78-8281-da71d7997276",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "16a7ffee-637b-4001-8290-3d13e070525e",
  "sourceToolAssistantUUID": "11125cd6-9c8c-4c78-8281-da71d7997276",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T03:54:07.722Z_

<details open><summary>🔧 Tool call — Read · `toolu_015ew8d7MFswkRKJCh9K1Akr`</summary>

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
  "parentUuid": "16a7ffee-637b-4001-8290-3d13e070525e",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7Tuot2uXsM6KKXaARVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31b9e60d-c754-4753-abcc-e11ea480833d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh3p8rDVUmWMqrWZ6Qt5rs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 25642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 872,
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

_source line 16 · 2026-05-17T03:54:07.728Z_

<details><summary>↩ Tool result · `toolu_015ew8d7MFswkRKJCh9K1Akr`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	A scoring-independent control (recency eviction) produces no positive phase gradient: $\Delta$ vanishes at $s \leq 0.25$ and remains non-significant at $s{=}0.30$, confirming that the interaction is attention-score-specific rather than an inherent property of token removal.
7	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K, and generalizes to LlamaForCausalLM ($n{=}250$; $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$).
8	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
9	Prior work characterizes compound degradation as phase-agnostic; we show that phase modulates severity by $15$--$17{\times}$ on DeepSeek and $2.7$--$3.5{\times}$ on Qwen, specifically driven by attention-score-based selection. These findings establish phase-gated analysis as a principled diagnostic framework with direct implications for phase-aware budget allocation.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31b9e60d-c754-4753-abcc-e11ea480833d",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "13c70a66-1fdc-4d65-8f60-2eb14b2ff524",
  "sourceToolAssistantUUID": "31b9e60d-c754-4753-abcc-e11ea480833d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T03:54:08.327Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mi8tcQqYHdzyrsPVf5ym4Y`</summary>

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
  "parentUuid": "13c70a66-1fdc-4d65-8f60-2eb14b2ff524",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7Tuot2uXsM6KKXaARVu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70fdf7c3-44ca-465c-ae6f-5751fa8d287a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hh3p8rDVUmWMqrWZ6Qt5rs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 25642,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 872
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 25642,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 872,
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

_source line 18 · 2026-05-17T03:54:08.345Z_

<details><summary>↩ Tool result · `toolu_01Mi8tcQqYHdzyrsPVf5ym4Y`</summary>

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
15	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with cross-architecture support from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$), where the importance phase gradient replicates with large effect sizes ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$) despite reduced strategy specificity ($2.0$--$2.6{\times}$ vs.\ $15$--$17{\times}$ on Qwen2-family models).
16	Random eviction develops a detectable phase gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \geq 0.25$), supporting that the dominant gradient is strategy-specific.
17	A scoring-independent control (recency eviction, which removes the oldest positions without attention scores) produces no phase gradient ($\Delta{=}-0.003$, CI spans zero), ruling out segmentation artifact and confirming that the interaction is specifically driven by attention-score-based selection (\S\ref{sec:scoring-control}).
18	Cross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\Delta$: $0.24 \to 4.68$; all $p \leq 0.0003$), while Qwen shows directional consistency at $s \geq 0.25$ but is inconclusive due to generation truncation (\S\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.
19	
20	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
21	
22	Beyond individual findings, we contribute a \emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.
23	
24	Our contributions:
25	\begin{enumerate}[nosep,leftmargin=*]
26	    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
27	    \item We replicate the pattern \textbf{across training paradigms and architectures}: within-architecture replication on Qwen2.5-7B-Instruct (same Qwen2 backbone, instruction-tuned; $\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$) and cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM; $n{=}250$; importance phase gradient $d_z{=}0.81$--$1.15$, all $p < 10^{-29}$; strategy specificity reduced to $2.0$--$2.6{\times}$, architecture-dependent; \S\ref{sec:cross-arch}).
28	    \item We provide a \textbf{scoring-independent control}: recency eviction (position-only, no attention scores) under identical compound sparsity produces no phase gradient ($\Delta \approx 0$, CI spans zero), ruling out segmentation artifact and establishing that phase-dependent severity is specifically driven by attention-score-based selection (\S\ref{sec:scoring-control}).
29	    \item We identify \textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\S\ref{sec:analysis}).
30	    \item We validate the phase gradient on \textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\S\ref{sec:cross-benchmark}).
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70fdf7c3-44ca-465c-ae6f-5751fa8d287a",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "7c1298f8-fd25-4f4b-87ca-e3462c0843df",
  "sourceToolAssistantUUID": "70fdf7c3-44ca-465c-ae6f-5751fa8d287a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T03:54:11.394Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U7Pg2E62WokmGBA59NgAzJ`</summary>

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
  "parentUuid": "7c1298f8-fd25-4f4b-87ca-e3462c0843df",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvFj3MLdnWr1VmdZAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0adea4c-434a-48e4-90fa-90e5e4158e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mhEJPvRpRsPngdTDR5nch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3342,
      "cache_read_input_tokens": 26514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3342,
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

_source line 20 · 2026-05-17T03:54:11.401Z_

<details><summary>↩ Tool result · `toolu_01U7Pg2E62WokmGBA59NgAzJ`</summary>

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
16	\paragraph{Structured pruning.}
17	Magnitude pruning~\cite{han-neurips2015} and the lottery ticket hypothesis~\cite{frankle-iclr2019} establish that neural networks contain sparse subnetworks preserving full-model performance.
18	Movement pruning~\cite{sanh-neurips2020} extends this to fine-tuning, learning which weights to zero during task adaptation.
19	For attention heads specifically, \cite{voita-acl2019} show most heads are prunable without degradation, and \cite{michel-neurips2019} demonstrate that head importance varies substantially across layers---findings our head pruning axis builds upon. These methods optimize a single pruning axis in isolation; we characterize the interaction when head pruning operates simultaneously with KV cache eviction.
20	
21	\paragraph{KV cache eviction.}
22	StreamingLLM~\cite{streamingllm-iclr2024} establishes attention sinks as a foundational mechanism; DuoAttention~\cite{duoattention-2024} classifies heads into retrieval and streaming types, complementing our analysis of importance discrimination collapse (\S\ref{sec:discrimination-collapse-main}). Subsequent work improves eviction through per-head adaptive budgets \cite{adakv-neurips2025}, observation-window compression \cite{snapkv-neurips2024}, proxy-token strategies \cite{nacl-acl2024}, deferred importance \cite{retentivekv-2026}, and worst-case analysis \cite{defensivekv-iclr2026}; \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias. \cite{hies-2025} independently show that importance discrimination collapses under heavy single-axis pruning; our results extend this to the compound setting, revealing phase-modulated amplification and a strategy crossover (\S\ref{sec:crossover}) absent in single-axis analysis.
23	Recent approaches target reasoning-aware eviction \cite{rlkv-2025, longflow-2026, dong2026foresightkv}, temporal adaptivity \cite{lethe-aaai2026}, channel-level pruning \cite{xu2025think, spark-aaai2026}, and learned budgets \cite{lkv-2026}. Concurrent work~\citep{hold-onto-thought-neurips2025} evaluates single-axis compression on mathematical reasoning; we extend to the compound setting.
24	These methods each optimize a single pruning axis without characterizing compound interactions.
25	
26	\paragraph{Phase-aware inference and reasoning.}
27	ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
28	\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
29	\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
30	\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.
31	R-KV~\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.
32	Test-time compute scaling~\cite{snell-2024-scaling-test-time} shows that allocating more inference-time computation can substitute for model scale; this emphasizes the importance of preserving reasoning-phase fidelity, where our work shows compound sparsity is most destructive.
33	ScissorHands~\cite{scissorhands-2023} leverages the persistence of importance hypothesis---that important tokens remain important across generation steps---a property our Gini analysis shows breaks down under compound stress.
34	These works establish phase-dependent compression tolerance along single axes.
35	
36	\paragraph{Conditional computation.}
37	Mixture-of-Experts architectures~\cite{shazeer-2017-moe, fedus-jmlr2022} achieve dynamic sparsity by routing tokens to a subset of parameters, providing a complementary paradigm to post-hoc pruning.
38	MoE sparsity is \emph{designed} (experts are trained to specialize), whereas compound sparsity is \emph{imposed} (pruning removes capacity without retraining).
39	Our phase-strategy interaction findings suggest that designed sparsity and imposed sparsity may interact differently across reasoning phases---a connection we leave to future work.
40	
41	\paragraph{Positioning.}
42	Our work bridges the compound compression and phase-aware literatures by quantifying how compound severity varies across phases and eviction strategies. Key differentiators: SparK~\cite{spark-aaai2026} characterizes compound interaction magnitude but treats it as phase-invariant; ThinKV~\cite{thinkv-iclr2026} adapts per phase but considers only single-axis KV compression without compound interaction; HIES~\cite{hies-2025} identifies importance score collapse under single-axis pruning but does not quantify its role in compound settings or its phase dependence. Our strategy specificity finding---that random eviction produces near-zero phase gradients while importance-based eviction exhibits $15$--$17{\times}$ amplification---is non-obvious: the \emph{a priori} expectation is that any eviction strategy operating on phase-structured attention should produce some phase gradient, yet random eviction yields effectively none at $s \leq 0.20$. The quantitative dose-response characterization provides target operating points for phase-aware compression controllers.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0adea4c-434a-48e4-90fa-90e5e4158e75",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "ec5ddd7c-e07e-4886-80ab-1b2f5aa1d5d2",
  "sourceToolAssistantUUID": "a0adea4c-434a-48e4-90fa-90e5e4158e75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T03:54:11.736Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ur7bND2n4GCiZKKjr4FvS8`</summary>

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
  "parentUuid": "ec5ddd7c-e07e-4886-80ab-1b2f5aa1d5d2",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvFj3MLdnWr1VmdZAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "388cf0ca-7b56-404d-9228-a05d1a276e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mhEJPvRpRsPngdTDR5nch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3342,
      "cache_read_input_tokens": 26514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3342,
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

_source line 22 · 2026-05-17T03:54:11.755Z_

<details><summary>↩ Tool result · `toolu_01Ur7bND2n4GCiZKKjr4FvS8`</summary>

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
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$: at each level, the head pruning rate $p{=}s$ (fraction of heads removed per layer) equals the KV cache eviction rate $e{=}s$ (fraction of positions evicted). We compute perplexity under four conditions: dense, attention-only ($p{=}s, e{=}0$), KV-only ($p{=}0, e{=}s$), and compound ($p{=}s, e{=}s$). We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
12	
13	\paragraph{Phase segmentation and metrics.}
14	Each sequence is segmented into three phases using the quantile-based method (\S\ref{par:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity and II (Eq.~\ref{eq:ii}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1). The amplification ratio $G$ (Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric}. Robustness to segmentation granularity (quartile, quintile; Appendix~\ref{app:seg-robust}) and minimum phase length ($5$, $10$, $20$ tokens; Appendix~\ref{app:mpl-sensitivity}) is verified.
15	
16	\paragraph{Segmentation validation.}
17	Quantile-based segmentation shows strong agreement with model-intrinsic \texttt{&lt;think>} boundaries on DeepSeek (Cohen's $\kappa{=}0.88$, token-level accuracy $94.2\%$, AUC-ROC${=}0.98$; $n{=}48$, GSM8K): $57.8\%$ of \texttt{&lt;think>} tokens fall in the low-sparsity phase and $62.7\%$ of answer tokens fall in the high-sparsity phase, confirming that attention-sparsity phases recover genuine reasoning structure without requiring explicit delimiters. Boundary proximity is tight (median 1 token; $81.2\%$ within 10 tokens). Appendix~\ref{app:think-validation} provides full details.
18	
19	\paragraph{Statistical analysis.}
20	\label{par:stats}
21	All reported confidence intervals use nonparametric bootstrap ($B{=}10{,}000$, seed$=$42)~\cite{efron-1993}. Significance tests use Wilcoxon signed-rank (paired within-model) or Mann-Whitney $U$ (cross-training-paradigm), with Bonferroni correction at family-wise $k{=}4$ (per model$\times$strategy combination, 4 sparsity levels testing one dose-response hypothesis): each family tests a single directional question (``does $\Delta$ increase with $s$?'') under fixed model and strategy, making $k{=}4$ the natural grouping. Benjamini-Hochberg FDR correction across all 44 tests is reported as a robustness check in Appendix~\ref{app:bh-fdr}; all Bonferroni-significant results remain significant under BH-FDR. Dose-response monotonicity is supported by the Jonckheere-Terpstra test ($z{=}6.2$--$33.7$, all $p < 10^{-9}$), which uses per-problem values (${\sim}496$ per group) rather than aggregated medians.\footnote{Spearman rank correlation on the four aggregate medians ($\rho{=}1.0$, $n{=}4$; interpret with caution given the small number of levels) is consistent; we rely on the JT test as primary evidence.} Scaling from $n{=}50$ (profiling) to $n{=}500$ narrowed bootstrap CI widths by $2.5$--$5.9{\times}$ across all 16 conditions, showing precision gains. The paired median difference $\Delta$ is the primary metric; $G$ (amplification ratio, Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric} as an auxiliary illustrative ratio.\footnote{Experiments on 4$\times$ professional GPUs with 48\,GB memory.}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "388cf0ca-7b56-404d-9228-a05d1a276e43",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "a28030a3-a0b2-4c2c-84ca-10a06d379eb0",
  "sourceToolAssistantUUID": "388cf0ca-7b56-404d-9228-a05d1a276e43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T03:54:12.159Z_

<details open><summary>🔧 Tool call — Read · `toolu_016nSnvTZr5BG6LbkoRueExj`</summary>

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
  "parentUuid": "a28030a3-a0b2-4c2c-84ca-10a06d379eb0",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvFj3MLdnWr1VmdZAW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b51fd328-7546-4fd4-b2f6-78966326cfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mhEJPvRpRsPngdTDR5nch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3342,
      "cache_read_input_tokens": 26514,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3342
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 26514,
          "cache_creation_input_tokens": 3342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3342,
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

_source line 24 · 2026-05-17T03:54:12.170Z_

<details><summary>↩ Tool result · `toolu_016nSnvTZr5BG6LbkoRueExj`</summary>

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
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$3.5{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Cross-Architecture Validation}
91	\label{sec:cross-arch}
92	
93	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}250$, MATH-500) supports the generality of phase-modulated compound interaction beyond the Qwen2 architecture family. Under importance-based eviction, the paired median difference $\Delta$ rises monotonically from $0.050$ ($s{=}0.15$) to $0.695$ ($s{=}0.30$), with large effect sizes throughout ($d_z{=}0.81$--$1.15$; all $p < 10^{-29}$; Table~\ref{tab:llama-cross-arch}).
94	
95	A key architectural difference emerges in strategy specificity. On LLaMA, random eviction also exhibits significant phase gradients ($\Delta{=}0.025$--$0.271$; $d_z{=}0.41$--$0.46$; all $p < 10^{-12}$), unlike DeepSeek and Qwen where random is non-significant at $s \leq 0.20$. The importance/random $\Delta$ ratio is $2.0$--$2.6{\times}$ on LLaMA, substantially weaker than the $15$--$17{\times}$ observed on DeepSeek. Dose-response monotonicity holds for both strategies (all conditions monotonic). This indicates that the phase gradient itself is architecture-general, while the degree of strategy specificity is architecture-dependent, likely reflecting differences between GQA (LLaMA, 32 heads with 8 KV groups) and MHA (Qwen2, 28 heads) in how head pruning differentially disrupts importance scoring.
96	
97	Absolute interaction magnitudes are approximately $7$--$12{\times}$ smaller than Qwen2-family models at matched sparsity, consistent with architecture-specific attention head specialization patterns. Full per-condition breakdowns appear in Appendix~\ref{app:cross-arch}.
98	
99	\subsection{Scoring-Independent Control}
100	\label{sec:scoring-control}
101	
102	To distinguish whether the phase gradient arises from attention-score-based eviction dynamics or from token removal \emph{per se} under compound sparsity, we introduce a scoring-independent control: \emph{recency eviction}, which removes the oldest non-BOS positions regardless of attention scores. This eliminates the feedback loop between head pruning and importance scoring while maintaining identical compression ratios.
103	
104	On DeepSeek ($n{=}100$, MATH-500), recency eviction produces a negative or absent phase gradient across $s \in \{0.15, 0.25\}$: $\Delta{=}-0.013$ (CI spans zero, NS) at $s{=}0.15$ and $\Delta{=}-0.091$ (CI excludes zero, significantly \emph{negative}) at $s{=}0.25$. Both contrast sharply with importance-based eviction at matched sparsity ($\Delta{=}+0.39$ and $+3.99$; all $p < 10^{-69}$). At $s{=}0.30$, KV perplexity saturation (${>}10^5$) under recency eviction renders per-segment II numerically unreliable; the gradient estimate ($+0.112$) is non-significant (CI $[-0.01,\; +0.46]$, spans zero).
105	
106	This triangulation across three eviction strategies provides strong evidence for mechanism discrimination:
107	\begin{itemize}[nosep,leftmargin=*]
108	    \item \textbf{Importance}: super-additive compound interaction ($\mathrm{II} > 0$) with large positive phase gradient ($\Delta$: $+0.39$ to $+8.48$)
109	    \item \textbf{Random}: super-additive interaction ($\mathrm{II} > 0$) with near-zero phase gradient ($\Delta \approx 0$ at $s \leq 0.20$)
110	    \item \textbf{Recency}: sub-additive/zero interaction ($\mathrm{II} \leq 0$) with absent or negative phase gradient ($\Delta \leq 0$ at $s \leq 0.25$; NS at $s{=}0.30$)
111	\end{itemize}
112	The recency control rules out two alternative explanations: (1)~the phase gradient is not a segmentation artifact, since the same phase boundaries produce no positive gradient under recency eviction; (2)~the gradient is not an inherent property of removing tokens under compound sparsity, since recency removes the same fraction of tokens without producing phase-dependent severity. Phase-dependent compound severity is specifically driven by attention-score-based selection, as evidenced by its absence under both position-based and random controls.
113	
114	\subsection{Scale Analysis: Qwen2.5-14B}
115	\label{sec:scale-14b}
116	
117	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
118	
119	\begin{table}[t]
120	\centering
121	\small
122	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
123	\label{tab:scale-14b}
124	\begin{tabular}{@{}lcccc@{}}
125	\toprule
126	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
127	\midrule
128	Importance & --- & --- & --- & --- \\
129	Random     & --- & --- & --- & --- \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
135	%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
136	%% (2) whether strategy specificity ratio is scale-invariant,
137	%% (3) comparison of phase segmentation thresholds at larger scale.
138	
139	\subsection{Cross-Benchmark Validation: GSM8K}
140	\label{sec:cross-benchmark}
141	
142	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero).
143	
144	We interpret this attenuation as \emph{reasoning depth scaling}: strategy specificity scales with reasoning chain depth. MATH-500 (complex multi-step reasoning, strategy ratio $15$--$17{\times}$) produces stronger phase contrast than GSM8K (simpler arithmetic, ratio ${\sim}2{\times}$ from point estimates). Within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), providing continuous correlational support. This scaling relationship is predictive: tasks with deeper reasoning chains should exhibit stronger strategy${\times}$phase interactions, because longer low-sparsity phases provide more opportunity for importance discrimination collapse to accumulate. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
145	
146	\paragraph{GSM8K accuracy under compound sparsity.}
147	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
148	
149	\subsection{Cross-Benchmark Validation: GPQA Diamond}
150	\label{sec:cross-benchmark-gpqa}
151	
152	To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
153	
154	\begin{table}[t]
155	\centering
156	\small
157	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
158	\label{tab:gpqa-results}
159	\begin{tabular}{@{}lcccc@{}}
160	\toprule
161	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
162	\midrule
163	DeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\
164	Qwen2.5-7B-Instruct         & --- & --- & --- & --- \\
165	\bottomrule
166	\end{tabular}
167	\end{table}
168	
169	%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
170	%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
171	%% (2) strategy specificity comparison across task types (math vs. science reasoning),
172	%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
173	
174	\subsection{Statistical Validation}
175	\label{sec:stat-validation}
176	
177	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
178	
179	\begin{table}[t]
180	\centering
181	\small
182	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
183	\label{tab:cohens-d}
184	\begin{tabular}{@{}lcc@{}}
185	\toprule
186	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
187	\midrule
188	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
189	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
190	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
191	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
192	\bottomrule
193	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
194	\end{tabular}
195	\end{table}
196	
197	\subsection{Answer-Region Analysis}
198	\label{sec:answer-region}
199	
200	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
201	
202	\subsection{Downstream Accuracy Validation}
203	\label{sec:accuracy-validation}
204	
205	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
206	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
207	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\%$--$76\%$, should be interpreted as qualitative observations only.
208	
209	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b51fd328-7546-4fd4-b2f6-78966326cfc7",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "12f0ef74-b4bf-49c8-80b1-a1f09214873d",
  "sourceToolAssistantUUID": "b51fd328-7546-4fd4-b2f6-78966326cfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T03:54:17.165Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NxpuhsiKCfaskDjQMnMCZo`</summary>

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
  "parentUuid": "12f0ef74-b4bf-49c8-80b1-a1f09214873d",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvYRPE6hqkPJabiKqa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d2617ad-b23f-47bf-9bc8-d00269129634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQXm2ejPnhDS7LWvMSWvu5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 29856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12005,
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

_source line 26 · 2026-05-17T03:54:17.173Z_

<details><summary>↩ Tool result · `toolu_01NxpuhsiKCfaskDjQMnMCZo`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, providing a correlational diagnostic for the phase-strategy interaction (causal attribution requires future intervention experiments). The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), indicating that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level on both models, with monotonically increasing magnitude (DeepSeek: $-0.016$ at $s{=}0.15$, $-0.021$ at $s{=}0.20$, $-0.031$ at $s{=}0.25$, $-0.037$ at $s{=}0.30$; Qwen: $-0.017$, $-0.020$, $-0.029$, $-0.035$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	
17	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
18	\label{sec:entropy-redistribution-main}
19	
20	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d2617ad-b23f-47bf-9bc8-d00269129634",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "74355fe6-5ba8-44ba-b0a2-60b50afcbeae",
  "sourceToolAssistantUUID": "7d2617ad-b23f-47bf-9bc8-d00269129634",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T03:54:17.674Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U9CdtHtKPa9GSguQ7VEWcn`</summary>

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
  "parentUuid": "74355fe6-5ba8-44ba-b0a2-60b50afcbeae",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvYRPE6hqkPJabiKqa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e85f73e0-de60-4d0e-8ff2-1b7c9a224393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQXm2ejPnhDS7LWvMSWvu5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 29856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12005,
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

_source line 28 · 2026-05-17T03:54:17.680Z_

<details><summary>↩ Tool result · `toolu_01U9CdtHtKPa9GSguQ7VEWcn`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
7	\paragraph{Reasoning depth scaling and architecture dependence.}
8	Strategy specificity is not a fixed property but varies along at least two axes. First, it scales with reasoning chain depth: MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}2{\times}$ point-estimate ratio; random non-significant at $n{=}50$), with within-MATH-500 correlational support (Spearman $\rho > 0$, $p < 0.02$ between trace length and specificity). Second, it is architecture-dependent: LlamaForCausalLM exhibits significant random phase gradients ($d_z{=}0.41$--$0.46$), reducing the importance/random ratio to $2.0$--$2.6{\times}$ compared with $15$--$17{\times}$ on DeepSeek (Qwen2-based). This suggests that the degree to which random eviction is phase-insensitive depends on architectural details of the attention implementation. The depth-scaling pattern is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The practical implication holds regardless of architecture: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly, though the relative advantage of strategy-aware allocation varies by model family. Behavioral evidence supports this scaling concern: under compound sparsity at $s \geq 0.25$, DeepSeek-R1-Distill-Qwen-7B generates degenerate reasoning loops averaging 6{,}344 tokens (76\% exceeding the 8{,}192-token budget), suggesting that compound sparsity not only amplifies phase-internal severity but may also disrupt reasoning termination. This degeneration is consistent with the discrimination collapse observed in exploration phases: once importance scores lose discriminative power, the model fails to consolidate toward an answer, producing unbounded exploratory chains.
9	
10	\paragraph{Diagnostic framework value.}
11	While we do not propose a new compression method, the phase-gated analysis framework has direct engineering utility: (1)~the Interaction Index can serve as a per-phase evaluation metric for assessing the phase robustness of any new compound compression scheme; (2)~the dose-response curves (Figure~\ref{fig:hero}) provide target operating points for phase-aware controllers, e.g., maintaining $s \leq 0.20$ during low-sparsity phases to keep $\Delta < 1.5$; (3)~the strategy specificity finding carries a concrete engineering implication: importance-based eviction under compound sparsity requires phase-aware protection that random eviction does not, because the interaction is structurally coupled to the scoring mechanism rather than to compression magnitude alone.
12	
13	\paragraph{Recency control as methodological contribution.}
14	The use of recency-based eviction as a scoring-independent control (\S\ref{sec:scoring-control}) provides a principled falsification test that, to our knowledge, has no precedent in the KV cache compression literature. Prior work employs recency eviction (StreamingLLM~\cite{streamingllm-iclr2024}) or H$_2$O scoring~\cite{h2o-neurips2023} as performance baselines, but not as controls for isolating the contribution of the scoring mechanism itself. The null result ($d_z{=}0.083$, NS at $s{=}0.15$, $n{=}100$) confirms that the phase gradient is attention-score-specific rather than an artifact of phase segmentation or positional structure, strengthening the causal interpretation of strategy specificity as a property of score-dependent token selection.
15	
16	\paragraph{Evidential status: mechanism discrimination, not causal proof.}
17	The triangulation across importance, random, and recency eviction constitutes \emph{mechanism discrimination}: we identify attention-score-based selection as the specific mediating pathway for phase-dependent severity, by showing the gradient's presence under score-based eviction and absence under score-independent controls. This is discriminative evidence, not intervention-based causal proof. Full causal demonstration would require directly manipulating score quality (e.g., injecting calibrated noise into attention scores before eviction) and observing a corresponding change in gradient magnitude, which we leave to future work. Our contribution is identifying the mediating pathway with sufficient specificity to guide system design: practitioners can use the finding that score-independent eviction eliminates the phase gradient to inform compression strategy selection, regardless of whether the underlying mechanism is fully causally resolved.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e85f73e0-de60-4d0e-8ff2-1b7c9a224393",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "04cb79fa-2231-41c8-bb10-ee885cbfda86",
  "sourceToolAssistantUUID": "e85f73e0-de60-4d0e-8ff2-1b7c9a224393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T03:54:18.024Z_

<details open><summary>🔧 Tool call — Read · `toolu_014RSArCeKuUbShv5qTU34zP`</summary>

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
  "parentUuid": "04cb79fa-2231-41c8-bb10-ee885cbfda86",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TvYRPE6hqkPJabiKqa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0fa9092-d90b-42ad-a632-967fbfcc2017",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQXm2ejPnhDS7LWvMSWvu5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12005,
      "cache_read_input_tokens": 29856,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 29856,
          "cache_creation_input_tokens": 12005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12005,
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

_source line 30 · 2026-05-17T03:54:18.030Z_

<details><summary>↩ Tool result · `toolu_014RSArCeKuUbShv5qTU34zP`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) supports that the phase gradient extends beyond the Qwen2 architecture ($n{=}250$, all 8 conditions significant; importance $d_z{=}0.81$--$1.15$), but strategy specificity is substantially weaker ($2.0$--$2.6{\times}$ vs.\ $15$--$17{\times}$ on DeepSeek) because random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$). This architecture-dependent strategy specificity indicates that the degree of strategy${\times}$phase interaction, not just absolute magnitude, varies across attention implementations. The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form: complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks (code generation, multi-hop QA) produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Recency control architecture scope.}
8	The three-way dissociation (importance/random/recency) was demonstrated on the Qwen2 architecture. On LlamaForCausalLM with grouped-query attention, even random eviction produces statistically significant phase gradients ($d_z{=}0.41$--$0.46$), suggesting that GQA's reduced KV-head count may inherently amplify phase-correlated compound damage regardless of selection criterion. Recency-based validation on GQA architectures remains for future work.
9	
10	\paragraph{Eviction strategy scope and H$_2$O confound.}
11	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring~\cite{h2o-neurips2023}, Eq.~\ref{eq:kv-importance}), which creates an inherent confound: head pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report, including importance discrimination collapse and the phase-strategy crossover, may be partly attributable to this circular dependency rather than to compound sparsity \emph{per se}. Other attention-mass-based methods (SnapKV~\cite{snapkv-neurips2024}, PyramidKV~\cite{pyramidkv-colm2025}) share the same scoring basis and would likely exhibit a similar confound. The recency control (\S\ref{sec:scoring-control}) partially addresses this by confirming that the phase gradient requires the attention-score pathway ($d_z{=}0.083$, NS under recency eviction vs.\ $d_z{=}0.574$ under importance at matched $s{=}0.15$). However, recency eviction was tested at a single sparsity level ($n{=}100$ pilot, vs.\ $n{=}500$ for importance); comprehensive evaluation across sparsity levels, and testing of other score-independent strategies (e.g., learned eviction policies), remains an important next step. The qualitative conclusion (gradient absence, CI spanning zero) is robust to sample size: post-hoc power analysis indicates $n{=}100$ provides power $> 0.85$ to detect effects of $d_z \geq 0.30$ at $\alpha{=}0.05$, well below the observed importance effect ($d_z{=}0.57$).
12	
13	\paragraph{Symmetric sparsity assumption.}
14	Our analysis applies symmetric sparsity levels: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) supports that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
15	
16	\paragraph{Phase segmentation validation.}
17	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.88$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
18	
19	\paragraph{Mechanism.}
20	Importance discrimination collapse is a correlational diagnostic observation, not a causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
21	
22	\paragraph{Perplexity vs.\ accuracy.}
23	Our primary severity metric is perplexity-based (II), chosen because its per-token granularity enables the phase-level decomposition central to our analysis; accuracy is binary per-problem and cannot be meaningfully decomposed by reasoning phase. Accuracy validation on MATH-500 (\S\ref{sec:accuracy-validation}, Appendix~\ref{app:accuracy-details}) shows gradual decline through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) followed by a sharp cliff at $s{=}0.30$ ($\delta{=}-27$\,pp) for Qwen ($n{=}100$, truncation $\leq 4\%$). DeepSeek accuracy deltas are confounded by rising truncation ($16\%$ to $76\%$); non-truncated analysis reveals a dual-regime structure but is limited by small surviving samples at high sparsity. Comprehensive accuracy evaluation across benchmarks remains an important next step.
24	
25	\paragraph{Sparsity range.}
26	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, sufficient to establish monotonicity at the tested levels (JT test $p \ll 10^{-10}$) but insufficient to characterize the functional form of the auxiliary ratio $G(s)$ or identify potential saturation thresholds. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0fa9092-d90b-42ad-a632-967fbfcc2017",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "1484206e-ab7e-4204-a486-48126a59e280",
  "sourceToolAssistantUUID": "e0fa9092-d90b-42ad-a632-967fbfcc2017",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T03:54:22.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BP2G15nfdpfvnfg3nCkRH4`</summary>

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
  "parentUuid": "1484206e-ab7e-4204-a486-48126a59e280",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7Tvy4xt7bXodjxfn9iT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fee46f67-6577-415b-831b-6604145b5c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167gfxmLtYE4DJg3epSozPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5034,
      "cache_read_input_tokens": 41861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5034,
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

_source line 32 · 2026-05-17T03:54:22.212Z_

<details><summary>↩ Tool result · `toolu_01BP2G15nfdpfvnfg3nCkRH4`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity is not phase-invariant but exhibits an emergent phase-strategy interaction. Under importance-based eviction, the paired median difference $\Delta$ increases from $0.39$ to $8.48$ (DeepSeek, $n{=}496$; Spearman $\rho{=}1.0$) and $0.07$ to $3.16$ (Qwen, $n{=}475$), all $p < 10^{-13}$. Random eviction is $2.7$--$17{\times}$ weaker where both strategies are significant ($s \geq 0.25$; DeepSeek $15$--$17{\times}$, Qwen $2.7$--$3.5{\times}$). The importance phase gradient replicates on LlamaForCausalLM ($d_z{=}0.81$--$1.15$, $n{=}250$, all $p < 10^{-29}$), supporting architecture-generality of phase modulation, while strategy specificity is architecture-dependent ($2.0$--$2.6{\times}$ on LLaMA vs.\ $15$--$17{\times}$ on DeepSeek). A model-dependent crossover on DeepSeek demonstrates that no single strategy dominates uniformly. Per-phase Gini analysis reveals importance discrimination collapse as a correlational diagnostic: despite near-identical aggregate Gini drops, severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning.
5	Beyond the empirical findings, the phase-gated analysis framework itself---decomposing compound severity by reasoning phase and eviction strategy---transforms a scalar interaction metric into a structured diagnostic that reveals where compound sparsity fails and why. This framework provides practitioners with a principled basis for phase-aware sparsity allocation: applying aggressive compression during high-sparsity (structured computation) phases while preserving budget during low-sparsity (exploratory reasoning) phases. Future work could explore generalization to other reasoning domains, causal validation of importance discrimination collapse, and systematic characterization of asymmetric compound interactions.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fee46f67-6577-415b-831b-6604145b5c26",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "65ded3de-df30-410c-a34a-cf69d238b40b",
  "sourceToolAssistantUUID": "fee46f67-6577-415b-831b-6604145b5c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T03:54:22.636Z_

<details open><summary>🔧 Tool call — Read · `toolu_016z1UM5yNmcn512eLHHDTkQ`</summary>

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
  "parentUuid": "65ded3de-df30-410c-a34a-cf69d238b40b",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7Tvy4xt7bXodjxfn9iT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0983b144-776c-4d99-b9dd-8525ee2bca9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167gfxmLtYE4DJg3epSozPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5034,
      "cache_read_input_tokens": 41861,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5034
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 41861,
          "cache_creation_input_tokens": 5034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5034,
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

_source line 34 · 2026-05-17T03:54:22.641Z_

<details><summary>↩ Tool result · `toolu_016z1UM5yNmcn512eLHHDTkQ`</summary>

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
31	Inspired by ThinKV's phase-aware perspective on reasoning-time compression~\cite{thinkv-iclr2026}, each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, using a quantile-based segmentation rather than explicit reasoning delimiters (e.g., \texttt{&lt;think>} tokens). Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). We note that this segmentation is an \emph{operationalization choice}: attention sparsity serves as a continuous proxy for reasoning phase rather than a theoretically grounded boundary. We validate robustness to segmentation granularity (tercile/quartile/quintile; Appendix~\ref{app:seg-robust}) and minimum phase length (Appendix~\ref{app:mpl-sensitivity}). Validation against DeepSeek's explicit \texttt{&lt;think>} markers using adaptive per-sequence quantile segmentation yields substantial agreement ($\kappa{=}0.88$, AUC-ROC${=}0.98$; $n{=}48$; Appendix~\ref{app:think-validation}). Importantly, phases reflect genuine computational mode differences even under the dense (uncompressed) baseline: per-phase dense perplexity increases monotonically from high ($1.10$) through mid ($1.17$) to low ($1.18$), confirming that low-sparsity phases correspond to inherently harder computation; the phase gradient in compound severity (\S\ref{sec:results}) thus amplifies a pre-existing computational asymmetry rather than creating one. Details in Appendix~\ref{app:formulation-details}.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0983b144-776c-4d99-b9dd-8525ee2bca9e",
  "isSidechain": true,
  "promptId": "6856a0f8-a83d-4f4c-b659-86cf52d65d21",
  "agentId": "a6c604a73d32ffd3d",
  "type": "user",
  "uuid": "75d37049-b2c2-4707-842f-59caeef9da97",
  "sourceToolAssistantUUID": "0983b144-776c-4d99-b9dd-8525ee2bca9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-17T03:55:49.825Z_

Now I have a comprehensive understanding of the paper. Let me write the review.

---

## Reviewer 2 (R2): Novelty/Significance and Related Work Positioning

### 1. Summary

This paper characterizes compound sparsity (attention head pruning + KV cache eviction) as phase-dependent rather than phase-invariant, demonstrating that severity concentrates in low-sparsity reasoning phases under importance-based eviction but not under random or recency-based eviction. The authors propose "importance discrimination collapse" (Gini coefficient degradation) as a correlational diagnostic and validate the pattern across two architecture families, three benchmarks, and four sparsity levels. The paper is primarily an empirical characterization study that proposes no new compression method but offers a "phase-gated analysis framework."

### 2. Novelty Assessment

**Phase-dependent compound severity:** The core observation---that compound interaction is stronger in some generation phases than others---is reasonably novel but follows naturally from prior work. ThinKV already demonstrates phase-dependent compression tolerance (single-axis). Decision Representation Transitions (2026) already shows pruning sensitivity is phase-dependent. Physics of KV Cache Compression (2026) identifies phase transitions in single-axis compression. The paper's contribution is showing this extends to the *compound* (two-axis) setting, which is incremental but non-trivial.

**Discrimination collapse:** This is largely a re-framing of HIES (2025), which already identifies importance score collapse under pruning. The paper acknowledges this (Section 5.1: "HIES report this collapse under single-axis pruning; we extend it to the compound setting"). The extension to compound settings and the per-phase Gini analysis add modest value, but the authors themselves concede this is correlational and insufficient to explain the 15-17x divergence. The Gini drops are near-identical for importance and random eviction, yet severity diverges dramatically---this undermines "discrimination collapse" as an explanatory mechanism.

**Triple dissociation:** The experimental design (importance vs. random vs. recency) is methodologically sound and represents the paper's strongest novelty. Using recency eviction as a scoring-independent control is well-motivated. However, the claim of "no precedent" is overclaimed: the basic logic of using ablation controls in compression studies is standard practice; what is new is the specific application to isolating score-dependent mechanisms.

**Reasoning-complexity gradient:** The paper claims r=0.997 for a reasoning-complexity gradient (GPQA > MATH-500 > GSM8K), but the GPQA results are listed as "pending" (Table 7 is empty), making this claim currently unsupported by the paper's own data. The correlation is computed over only 3 points, which is insufficient for meaningful inference regardless of the r-value.

**Incremental contribution over prior work:**
- vs. SparK: SparK shows compound interaction is super-additive; this paper shows it varies by phase. Genuine increment.
- vs. ThinKV: ThinKV does phase-aware single-axis compression; this paper characterizes compound interaction across phases. Genuine increment.
- vs. HIES: HIES shows discrimination collapse in single-axis; this paper shows it in compound settings with phase dependence. Small increment.
- vs. Physics of KV Cache Compression: That work identifies phase transitions in single-axis compression; this paper extends to compound settings. Moderate increment.
- vs. DefensiveKV: Independently discovers importance instability; different framing but overlapping insight.

Overall novelty is moderate: the paper combines known components (phase-dependent sensitivity + compound sparsity + importance score degradation) in a previously unexplored combination, but the individual insights are not surprising given existing literature.

### 3. Related Work Assessment

**Strengths of the Related Work section:** Well-organized by theme (compound compression, structured pruning, KV cache eviction, phase-aware inference, conditional computation, positioning). The positioning paragraph explicitly differentiates from SparK, ThinKV, and HIES.

**Missing or problematic citations:**
- H2O [Zhang et al., NeurIPS 2023] is cited in the Limitations section but never properly introduced in Related Work despite being the foundation of the importance scoring mechanism used throughout the paper. This is a significant gap.
- The paper title in the summary mentions "H2O-style importance scoring" but H2O appears only in Limitations and Discussion, not in the Related Work section's KV cache eviction paragraph.
- StreamingLLM is cited but the actual citation format `\cite{streamingllm-iclr2024}` appears to resolve correctly. 
- The [?] placeholders mentioned in the review brief are not visible in the current tex files, suggesting they may have been fixed.

**Positioning fairness:**
- The positioning against SparK is fair: SparK does treat interaction as phase-invariant.
- The positioning against ThinKV is fair: ThinKV does single-axis phase-aware compression without compound interaction analysis.
- The claim about HIES is appropriately hedged.
- DefensiveKV (ICLR 2026) is in the literature map but only briefly mentioned in the Related Work. Given its direct relevance (importance score instability), it deserves more discussion.

**Missing older work:** The paper does not cite DuoAttention's finding about head specialization in the Related Work text (it appears only parenthetically). More importantly, there is limited engagement with the attention head importance literature beyond Voita and Michel (both 2019), missing more recent work on how attention patterns change during generation.

**"No precedent" claims:** The Discussion claims the recency control "to our knowledge, has no precedent in the KV cache compression literature." This is a strong claim. While it may be technically true for KV cache specifically, the experimental logic (using a mechanism-free baseline to isolate mechanism-specific effects) is basic experimental design. The novelty is in the application, not the methodology.

### 4. Significance Assessment

**Does the paper change practitioner thinking?** Partially. The directional message ("compound sparsity is worse during exploratory reasoning phases") is useful but somewhat expected given ThinKV's findings for single-axis compression. The quantification (15-17x amplification) is striking but specific to one model family and one eviction strategy.

**Practical impact:** The paper's own pilot evaluation achieves only 18% oracle recovery (CI spanning zero), falling below the pre-registered 30% gate. This means the authors' own attempt to translate findings into a practical controller failed. The paper explicitly acknowledges this. The practical contribution is thus limited to the diagnostic framework, not to a working solution.

**7B-only limitation:** The Limitations section mentions 14B experiments (Section 5.5, Table 5) but the table is empty ("Results pending"). The Llama-8B validation uses only n=250 (vs. n=496/475 for the primary models). For a characterization paper, the 7B scale is acceptable for establishing the phenomenon, but the generalization claim is substantially weakened. The strategy specificity attenuation on LLaMA (2.0-2.6x vs. 15-17x) already shows the effect is highly model-dependent.

**Actionable insights:** The paper provides:
1. "Maintain s <= 0.20 during low-sparsity phases to keep Delta < 1.5" --- actionable.
2. "Importance-based eviction needs phase-aware protection; random does not" --- actionable.
3. "Use recency eviction as a diagnostic control" --- methodologically useful.

However, these are conservative recommendations (use less compression when it matters), not novel compression methods. A reader could arrive at similar conclusions from ThinKV + SparK without this paper.

**Incomplete results:** Tables 5 and 7 (14B scale analysis and GPQA Diamond) are placeholders with "Results pending." The reasoning-complexity gradient (claimed as contribution in the paper summary's framing) relies on GPQA data that does not exist in the paper. This is a serious issue for review---claims should not be made about data not yet collected.

### 5. Strengths

- Rigorous statistical methodology: paired tests, bootstrap CIs, Bonferroni correction, Jonckheere-Terpstra trend tests, post-hoc power analyses. Among the most statistically careful papers I have reviewed in this area.
- Clean experimental design: the three-way comparison (importance/random/recency) isolates the scoring mechanism convincingly.
- Honest self-assessment: the paper explicitly states discrimination collapse is correlational, the pilot controller failed, and the crossover is model-dependent. Limitations section is thorough and transparent.
- Replication across training paradigms (distillation vs. instruction-tuning) on the same backbone strengthens internal validity.
- Phase segmentation validated against intrinsic model markers (kappa=0.88).
- The Interaction Index formulation and its decomposition by phase is a clean, reusable metric.

### 6. Weaknesses

- **No method proposed:** This is purely a characterization paper. The phase-gated controller pilot *failed* (18% recovery, CI spanning zero). The paper identifies a problem but provides no solution. For a top venue, characterization papers need either a truly surprising finding or immediate actionable impact; this paper achieves neither definitively.
- **Incomplete results:** Two key tables (14B and GPQA) are empty placeholders. The reasoning-complexity gradient claim (r=0.997) appears in the summary framing but is unsupported in the actual paper. This is not acceptable for review.
- **Moderate novelty:** The finding that compound sparsity interacts with generation phase is an expected extension of ThinKV (phase-dependent single-axis) + SparK (compound super-additivity). The combination is new but unsurprising.
- **Proposed mechanism is admittedly insufficient:** Discrimination collapse (Gini drops) is nearly identical for importance and random eviction, yet severity diverges 15-17x. The paper acknowledges this gap but does not resolve it. The "structural specificity" explanation (importance pruning removes low-Gini heads) is post-hoc and correlational.
- **Architecture dependence undermines generality:** The headline finding (15-17x strategy specificity) holds only for DeepSeek/Qwen2. On LLaMA, it drops to 2.0-2.6x. The crossover is DeepSeek-specific. Model-dependence of this magnitude makes it unclear which finding, if any, would generalize to other architectures.
- **Perplexity as primary metric:** The paper's phase decomposition relies on perplexity, not accuracy. The accuracy validation (Section 5.9) shows complex non-linear relationships (truncation confounds in DeepSeek, cliff effects in Qwen) that do not straightforwardly validate the perplexity-based severity gradient as practically meaningful.
- **Small n for key claims:** GSM8K uses n=50; recency control uses n=100. The recency result at s=0.30 is declared unreliable due to saturation.
- **Symmetric sparsity only:** Equal head pruning and KV eviction rates are not realistic deployment configurations. The paper acknowledges this but the limitation significantly reduces practical applicability.

### 7. Questions for Authors

1. The 14B results (Table 5) and GPQA results (Table 7) are listed as "pending." Are these experiments complete? If not, how can the reasoning-complexity gradient claim be supported?

2. Given that the Gini drops are nearly identical for importance and random eviction yet severity diverges 15-17x, what is the actual mechanism? The paper says "structural specificity" but this seems like restating the observation (importance pruning removes specific heads) rather than explaining why this causes 15-17x amplification specifically in low-sparsity phases.

3. The crossover phenomenon (importance better in high-sparsity phase, worse in low-sparsity phase) appears only in DeepSeek and not in Qwen. What architectural or training-related explanation do you have for this?

4. How do the findings change under asymmetric sparsity configurations (e.g., 30% head pruning + 10% KV eviction), which are more realistic for deployment?

5. The phase segmentation uses attention sparsity computed from the *dense* model. In a deployment setting, you would not have access to the dense model's attention patterns. How would a practitioner implement phase-gated compression without the oracle phase assignments?

6. The strategy specificity ratio drops from 15-17x (DeepSeek/Qwen2) to 2.0-2.6x (LLaMA). Under what conditions should a practitioner expect the larger vs. smaller ratio? Is this a GQA vs. MHA distinction?

7. The pilot phase-gated controller achieved only 18% oracle recovery with CI spanning zero. Does this suggest the findings, while statistically significant, may be insufficient in magnitude to be practically exploitable?

### 8. Scores

- **Novelty:** 3/6 --- The combination of phase-dependent analysis with compound sparsity is new but follows naturally from existing work (ThinKV + SparK + HIES). The proposed mechanism is acknowledged as insufficient.
- **Presentation:** 4/6 --- Well-written, statistically rigorous, honest about limitations. Deducted for incomplete tables (14B, GPQA), overly long Limitations section relative to contributions, and some repetition between Results subsections.
- **Significance:** 3/6 --- The diagnostic framework is useful but the paper provides no working method. The pilot controller failed. Architecture dependence of the headline numbers (15-17x vs. 2-2.6x) undermines generalizability. Practical recommendations are largely conservative (compress less when it matters).
- **Overall:** 3/6 (Weak Reject) --- A careful empirical study that identifies a real but expected phenomenon, proposes an insufficient mechanism, fails to demonstrate practical utility (controller pilot failed), and presents incomplete experimental evidence (pending tables). The statistical rigor is commendable, but rigor applied to a moderate question with incomplete data does not meet the bar for a top venue at 25% acceptance.
- **Confidence:** 4/5 --- I am familiar with the KV cache compression, attention pruning, and compound sparsity literatures. My uncertainty is primarily around whether the pending experiments (GPQA, 14B) would meaningfully change the paper's contribution if completed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d37049-b2c2-4707-842f-59caeef9da97",
  "isSidechain": true,
  "agentId": "a6c604a73d32ffd3d",
  "requestId": "req_011Cb7TwKCBGLURFARweH5Rq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22fbdced-5756-4cc9-84ec-35f787a8b6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "e6cd8e41-5873-40ec-aa2c-9e61f1b94abd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Phn4R3ZPacAgCmkbBfhiQB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 46895,
      "output_tokens": 3366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3366,
          "cache_read_input_tokens": 46895,
          "cache_creation_input_tokens": 2270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2270,
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
