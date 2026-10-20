# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad176ae12cbd1995e.jsonl`
- **Structured JSON:** [`bbefe7f3fb56f1fa2911.json`](../../sessions/bb/bbefe7f3fb56f1fa2911.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-17T02:10:53.747Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty/originality** and **Related work positioning**.

## Paper Summary

**Title**: "Phase-Dependent Compound Severity Scales with Eviction Discriminativeness: A Quantitative Analysis of KV Cache Compression Interactions"

**Core claim**: When LLMs use compound sparsity (head pruning + KV cache eviction simultaneously), the resulting super-additive degradation varies across reasoning phases. Key findings:
- All non-trivial eviction strategies produce monotonically increasing compound severity from early to late reasoning phases
- The magnitude scales with "eviction discriminativeness": importance-based yields 1.47-16.6× larger gradients than random
- The ratio is modulated by chain length: shorter chains → higher ratio; longer chains → ratio compresses toward 1.5×

**Framing**: The paper frames this as a "quantitative scaling law" relating eviction discriminativeness, sparsity level, and phase position. It explicitly positions itself as a measurement study, not a method paper.

**Contributions claimed**:
1. Phase-dependent compound severity is universal (all non-trivial eviction strategies)
2. Scaling law: phase gradient magnitude proportional to eviction discriminativeness, modulated by context length
3. Cross-benchmark evidence on GPQA Diamond generalizing to long heterogeneous chains
4. Discrimination collapse mechanism via Gini coefficient and CV analysis

**Related Work section** covers:
- KV Cache Compression: H2O [Zhang et al., 2023], StreamingLLM [Xiao et al., 2023], ThinKV [Xu et al., 2025], R-KV [Luo et al., 2025]
- Compound Compression: SparK [Wang et al., 2024], Lethe [Chen et al., 2026]
- Compression Phase Transitions: Physics of KV Cache Compression [Li et al., 2026], HIES [Zhao et al., 2025]

Total references: 8.

**Method**: Phase segmentation (equal thirds), Interaction Index (super-additive perplexity component), three eviction strategies (importance, random, recency), cross-benchmark comparison.

**Key result**: On GPQA (long chains), random eviction produces nearly as strong phase gradients as importance eviction (ratio 1.47×), while on MATH-500 (medium chains) the ratio is 16.6×. The paper interprets this as: phase-dependent severity is universal, importance-specificity is a function of context length.

**Discussion admits**: Recency is "not a control" (confounded by temporal locality); this is a measurement study with no method contribution; no formal discriminativeness metric.

## Your review task

Provide a detailed review covering:

1. **Novelty Assessment** (2-3 paragraphs):
   - What is genuinely new here? Is "phase-dependent compound severity" a novel concept or an expected consequence of known phenomena?
   - The "scaling law" claim — is it actually a scaling law, or just an empirical observation across 3 data points (3 benchmarks)?
   - Does the paper provide mechanistic insight, or just description?
   - The "discrimination collapse" mechanism is mentioned in contributions but barely developed — is this a real contribution?
   - Could a reviewer trivialize this as "longer reasoning chains are more fragile to any token removal, which is obvious"?

2. **Related Work Assessment** (2-3 paragraphs):
   - Is 8 references sufficient for a top venue? What's missing?
   - Are the cited works real and correctly described?
   - Missing areas: attention head pruning literature (no citations!), CoT reasoning robustness, compression-quality tradeoffs in general, structured pruning literature
   - Does the positioning against SparK/ThinKV/Lethe hold up?
   - "First to systematically analyze the three-dimensional interaction" — is this actually true?

3. **Significance & Impact** (1-2 paragraphs):
   - Who benefits from this work? Practitioners? Researchers?
   - No method proposed = limited practical impact?
   - Would this change how anyone builds compression systems?

4. **Strengths** (bullet list, 3-5 items)

5. **Weaknesses** (bullet list, 5-8 items, with severity: minor/moderate/major)

6. **Questions for Authors** (3-5 questions)

7. **Scores** (with brief justification for each):
   - Novelty (1-6)
   - Significance (1-6)
   - Clarity (1-6)
   - Overall (1-6)
   - Confidence (1-5, where 5=expert)

Be rigorous. For a top venue, novelty must be substantial, related work must be thorough, and the contribution must meaningfully advance the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "c130bc6d-31b3-4b90-8be8-d2ead1f7c2ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T02:10:53.750Z_

```json
{
  "parentUuid": "c130bc6d-31b3-4b90-8be8-d2ead1f7c2ea",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
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
  "uuid": "1940ffc7-fd96-463e-987a-4c2d41e33f55",
  "timestamp": "2026-05-17T02:10:53.750Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T02:10:56.919Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01M4etbajpv8RhjgtpWUVo8E`</summary>

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
  "parentUuid": "1940ffc7-fd96-463e-987a-4c2d41e33f55",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L3cu2SfN7KfUzXQPZr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6707b2b-5907-4a6c-bb93-225e74f61ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018B3E8A11tWhbhN1w39Knc8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8297,
      "cache_read_input_tokens": 8252,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 8297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8297,
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

_source line 4 · 2026-05-17T02:10:56.923Z_

<details><summary>↩ Tool result · `toolu_01M4etbajpv8RhjgtpWUVo8E`</summary>

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
  "parentUuid": "b6707b2b-5907-4a6c-bb93-225e74f61ea3",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "78809ea6-d3d6-45ca-8e7d-adca016af46d",
  "sourceToolAssistantUUID": "b6707b2b-5907-4a6c-bb93-225e74f61ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T02:11:00.212Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0159ycpxeGLportySf5tDctg`</summary>

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
  "parentUuid": "78809ea6-d3d6-45ca-8e7d-adca016af46d",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L3rcXkveweQnrsrxZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e6dd8d8-eca0-4ba1-91da-db32e3ea2d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpUYjXvg6ghn4YsU1PwMfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1270,
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

_source line 6 · 2026-05-17T02:11:00.229Z_

<details><summary>↩ Tool result · `toolu_0159ycpxeGLportySf5tDctg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_random_s020 | Cross-task generalization: random eviction control on GPQA Diamond. DS-R1 random s020 to establish baseline phase gradient (expected NS or weak) for strategy specificity comparison. | — | — | — |\\n| gpqa_ds_importance_s030 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s030 as fourth condition. | — | — | — |\\n| gpqa_ds_importance_s025 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s025 as third condition (after s015 success, s020 running). | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **recency_s025** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.25 condition.\\n  [recency_s025_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s025/report/analysis.md)\\n- **recency_s030** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.30 condition.\\n  [recency_s030_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s030/report/analysis.md)\\n- **recency_s015** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.15 condition.\\n\\n## 趋势\\n成功 70 / 负向 17 / 失败 17 / 共 134\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 3667, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e6dd8d8-eca0-4ba1-91da-db32e3ea2d3a",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "525d39c3-8faf-454e-8630-2806bd667118",
  "sourceToolAssistantUUID": "1e6dd8d8-eca0-4ba1-91da-db32e3ea2d3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T02:11:00.684Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LRPCp1HxRM8B2obGDLDVNP`</summary>

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
  "parentUuid": "525d39c3-8faf-454e-8630-2806bd667118",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L3rcXkveweQnrsrxZ6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48a02ae8-017d-46ab-8994-c455a29cd21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DpUYjXvg6ghn4YsU1PwMfV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16549,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1270
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 16549,
          "cache_creation_input_tokens": 1270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1270,
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

_source line 8 · 2026-05-17T02:11:00.707Z_

<details><summary>↩ Tool result · `toolu_01LRPCp1HxRM8B2obGDLDVNP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression\\\"\\n  authors: Mozaffari et al.\\n  venue: ICML 2025\\n  year: 2025\\n  category: method-component\\n  relevance: 首个正式处理 compound compression error 的框架——用 low-rank adapter 补偿 Q+S 聚合误差，证明误差非加性\\n  key_finding: quantization + sparsity 聚合误差非加性；invertible saliency function 精确计算 low-rank 补偿\\n\\n- paper_id: unicomp-2026\\n  title: \\\"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation\\\"\\n  authors: Wang et al.\\n  venue: arXiv 2602.09130\\n  year: 2026\\n  category: evaluation\\n  relevance: 40+ benchmarks 系统评估 compound compression，发现 compression 有 consistent knowledge bias\\n  key_finding: compression 对 knowledge-intensive tasks 保留好但 reasoning/multilingual 显著退化；quantization 整体 trade-off 最佳\\n\\n- paper_id: compression-ordering-2025\\n  title: \\\"A Systematic Study of Compression Ordering for Large Language Models\\\"\\n  venue: arXiv 2511.19495\\n  year: 2025\\n  category: background\\n  relevance: 证明 compound compression ordering 显著影响结果，early quantization 造成不可逆信息损失\\n  key_finding: P→KD→Q 最优；quantization first 产生不可逆退化；interaction 依赖 ordering\\n\\n- paper_id: phase-transition-compression-2026\\n  title: \\\"Phase Transitions in Large Language Model Compression\\\"\\n  authors: Ma et al.\\n  venue: npj Artificial Intelligence (Nature), 2026\\n  year: 2026\\n  category: background\\n  relevance: 直接支撑 phase-gating 理论动机——不同压缩维度有独立 phase transition point，联合安全区可叠加\\n  key_finding: structured pruning 30-45% 崩溃，unstructured 55-65%；多维度 PTP 正交，联合安全区可实现 10% 压缩\\n\\n- paper_id: graspune-acl2026\\n  title: \\\"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\\\"\\n  authors: Wang et al.\\n  venue: ACL 2026 Main\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 最直接 competitor——联合 pruning FFN channels + KV head groups with learned gate scores under global budget\\n  key_finding: learned gate + projected STE 全局 budget 下联合 prune FFN+heads，高压缩比下显著优于逐层独立 pruning\\n\\n- paper_id: mustafar-neurips2025\\n  title: \\\"MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference\\\"\\n  authors: Joo et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-token magnitude pruning 70% sparsity 无损，与 token eviction 可组合——potential compound baseline\\n  key_finding: unstructured KV sparsity (per-token magnitude) 70% 无损，bitmap 格式 2.23x throughput\\n\\n# ============================================================\\n# 新增 — Non-monotonic / Sign Reversal / Phase Effects\\n# ============================================================\\n\\n- paper_id: decision-repr-transition-2026\\n  title: \\\"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\\\"\\n  venue: arXiv 2605.07271\\n  year: 2026\\n  category: background\\n  relevance: layer pruning 存在 Silent/Decisive Phase 二分——pruning 敏感度 phase-dependent，直接支撑 phase-gated 思想\\n  key_finding: Decision Margin 在 Transition Point 发生符号反转（负→正）；pruning Silent Phase 崩溃，Decisive Phase 可安全 prune\\n\\n- paper_id: doing-more-with-less-2026\\n  title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n  venue: arXiv 2604.25098\\n  year: 2026\\n  category: background\\n  relevance: 符号反转直接证据——unstructured pruning + TTS 可超越未剪枝模型\\n  key_finding: unstructured pruning + test-time scaling 可超越 unpruned baseline（Qwen3-8B）；structured pruning 严重退化\\n\\n- paper_id: sparse-frontier-2025\\n  title: \\\"The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs\\\"\\n  venue: arXiv 2504.17768\\n  year: 2025\\n  category: evaluation\\n  relevance: 最大规模 sparse attention 评估，无通用最优策略，trade-off 依赖 task 和 phase\\n  key_finding: decoding vs prefilling 可承受 sparsity 不同；大模型+高稀疏可优于小模型+密集\\n\\n# ============================================================\\n# 新增 — Adaptive / Learned Controllers\\n# ============================================================\\n\\n- paper_id: obcache-2025\\n  title: \\\"OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference\\\"\\n  venue: arXiv 2510.07651\\n  year: 2025\\n  category: method-component\\n  relevance: OBD 理论推导 joint K-V saliency score，可作为 importance-based masking 的理论参照\\n  key_finding: 二阶 Taylor 近似推导 joint K-V pruning score；key-pruning 比 value-pruning 影响更大\\n\\n- paper_id: pagedeviction-eacl2026\\n  title: \\\"PagedEviction: Structured Block-wise KV Cache Pruning\\\"\\n  venue: EACL 2026 Findings\\n  year: 2026\\n  category: method-component\\n  relevance: prefill/decode 两阶段不同 eviction 策略，呼应 phase-gated 思想\\n  key_finding: block-wise eviction prefill/decode 分阶段执行，优于 token-level baselines\\n\\n- paper_id: adakv-neurips2025\\n  title: \\\"Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: per-head adaptive budget 分配，与 per-phase budget allocation 正交互补\\n  key_finding: 自适应 per-head KV cache budget 优于均匀分配\\n\\n- paper_id: sol-2026\\n  title: \\\"SOL: Self-Optimizing Language Models — Compute Where it Counts\\\"\\n  venue: arXiv 2605.10875\\n  year: 2026\\n  category: method-component\\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\\n\\n# ============================================================\\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\\n# ============================================================\\n\\n- paper_id: twilight-neurips2025\\n  title: \\\"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\\\"\\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\\n  venue: NeurIPS 2025 Spotlight\\n  year: 2025\\n  category: method-component\\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\\n\\n- paper_id: lava-emnlp2025\\n  title: \\\"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\\\"\\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  category: method-component\\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\\n\\n- paper_id: lkv-2026\\n  title: \\\"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\\\"\\n  venue: arXiv 2605.06676\\n  year: 2026\\n  category: method-component\\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\\n\\n- paper_id: defensivekv-iclr2026\\n  title: \\\"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\\\"\\n  venue: ICLR 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\\n\\n- paper_id: retentivekv-2026\\n  title: \\\"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\\\"\\n  venue: arXiv 2605.04075\\n  year: 2026\\n  category: background\\n  relevance: \\\"Deferred Importance\\\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\\n\\n- paper_id: pitfalls-kvcache-2025\\n  title: \\\"The Pitfalls of KV Cache Compression\\\"\\n  venue: arXiv 2510.00231\\n  year: 2025\\n  category: background\\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\\n\\n- paper_id: greedy-bias-kvcache-2026\\n  title: \\\"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\\\"\\n  venue: arXiv 2602.02199\\n  year: 2026\\n  category: background\\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\\n\\n- paper_id: thinking-tokens-mi-neurips2025\\n  title: \\\"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\\n\\n- paper_id: lserve-mlsys2025\\n  title: \\\"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\\\"\\n  venue: MLSys 2025\\n  year: 2025\\n  category: background\\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\\n\\n- paper_id: squeezeattention-iclr2025\\n  title: \\\"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\\\"\\n  venue: ICLR 2025\\n  year: 2025\\n  category: method-component\\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\\n\\n- paper_id: nsa-acl2025\\n  title: \\\"NSA: Native Sparse Attention\\\"\\n  authors: DeepSeek\\n  venue: ACL 2025 Best Paper\\n  year: 2025\\n  category: background\\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\\n\\n- paper_id: evicpress-2025\\n  title: \\\"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\\\"\\n  venue: arXiv 2512.14946\\n  year: 2025\\n  category: method-component\\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\\n\\n- paper_id: phase-transition-pruning-thermo-2026\\n  title: \\\"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\\\"\\n  venue: arXiv 2602.15224\\n  year: 2026\\n  category: background\\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\\n\\n- paper_id: token-budget-aware-acl2025\\n  title: \\\"Token-Budget-Aware LLM Reasoning\\\"\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  category: background\\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget\\n\\n# ============================================================\\n# 新增 — C5b Negative Result 文献联动 (2026-05-14)\\n# ============================================================\\n\\n- paper_id: physics-kvcache-2026\\n  title: \\\"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics\\\"\\n  venue: arXiv 2603.01426\\n  year: 2026\\n  category: background\\n  relevance: 直接解释 C5b negative——representational rigidity 使 budget redistribution 无法修复 routing collapse；90% 附近存在 sharp hallucination cliff (phase transition)\\n  key_finding: head-level consensus 过度导致 representational rigidity，token 存活但 routing flexibility 崩溃；compression 存在 sharp safety cliff 对应 semantic reachability phase transition\\n\\n- paper_id: rkv-neurips2025\\n  title: \\\"R-KV: Redundancy-aware KV Cache Compression for Reasoning Models\\\"\\n  authors: Cai et al.\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: method-component\\n  relevance: reasoning model 专用单轴 KV compression，10% cache 保留 ~100% 性能；但不涉及 compound interaction，与 C5b failure 机制不直接相关\\n  key_finding: importance + non-redundancy 双准则 token ranking，10% KV cache 保留全精度性能；单轴方法无 compound 讨论\\n\", \"total_chars\": 13069, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48a02ae8-017d-46ab-8994-c455a29cd21d",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "a1c22023-721f-4576-ac2c-8ed2b70f0599",
  "sourceToolAssistantUUID": "48a02ae8-017d-46ab-8994-c455a29cd21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T02:11:04.891Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NvqJWX1hNu4fHTkd8phGq6`</summary>

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
  "parentUuid": "a1c22023-721f-4576-ac2c-8ed2b70f0599",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L48nsN6LKKeFRrT2zz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "721e8d6e-40c3-466f-a526-b29afd37d20f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRnETm8kaHLLxNoRKcJtQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7526,
      "cache_read_input_tokens": 17819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7526,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 10 · 2026-05-17T02:11:04.903Z_

<details><summary>↩ Tool result · `toolu_01NvqJWX1hNu4fHTkd8phGq6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "721e8d6e-40c3-466f-a526-b29afd37d20f",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "16363680-9b4a-4b8d-893c-aab511cad473",
  "sourceToolAssistantUUID": "721e8d6e-40c3-466f-a526-b29afd37d20f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T02:11:05.304Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Wj7Hxv4hr3nFp1oyz1gjYs`</summary>

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
  "parentUuid": "16363680-9b4a-4b8d-893c-aab511cad473",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L48nsN6LKKeFRrT2zz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ef9991a-e711-4fa5-8950-87b3597f7804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRnETm8kaHLLxNoRKcJtQV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7526,
      "cache_read_input_tokens": 17819,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 17819,
          "cache_creation_input_tokens": 7526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7526,
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

_source line 12 · 2026-05-17T02:11:05.326Z_

<details><summary>↩ Tool result · `toolu_01Wj7Hxv4hr3nFp1oyz1gjYs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_framing.md\", \"content\": \"# Paper Framing — Phase-Gated Compound Sparsity\\n\\n> 最后更新: 2026-05-17 (D102: C11 confirmed — recency triple NS across s015/s025/s030; s015+s025 primary, s030 supplementary) | 维护者: Director\\n\\n## Core Insight\\n\\nCompound sparsity（attention head pruning + KV cache eviction）的 severity 不是固定常数——它是 eviction strategy 和 reasoning phase 交互的涌现属性。Importance-based eviction 的 compound interaction severity（paired median difference: median(II_low_i − II_high_i)）随 sparsity 单调递增（DeepSeek: 0.39→1.21→3.99→8.48; Qwen: 0.07→0.31→1.07→3.16），而 random masking 在 s015/s020 NS，在 s025 跨模型显著但效应量远小于 importance（DS: 0.257 vs 3.986; QW: 0.393 vs 1.074, 2.7-17×差异），存在 sparsity threshold ~s020-s025（D063; s030 待定）。Cohen's d（per-problem paired, B=10000）从 medium 到 large（DeepSeek: 0.61→1.13; Qwen: 0.37→1.44，registry cohens_d s015→s030）。LLaMA 跨架构验证（D060, c8_llama_n250_fixed, n=250）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29, all monotonic），且 random 在 LLaMA 上所有条件均显著（d_z=0.41-0.46, all p<10^-12），imp/rand Δ ratio 仅 2.0-2.6×（vs DeepSeek 15-17×），strategy×phase 交互强度 architecture-dependent。GSM8K 跨 benchmark 验证（D075）：importance masking 的 phase gradient 在 GSM8K 上同样单调递增（QW: 0.039→0.158→1.100→2.092; DS: 0.241→0.740→1.992→4.682），但 strategy specificity（importance/random gradient ratio）从 MATH-500 的 15-17× 衰减至 GSM8K 的 2.3-3.8×。注意：\\\"反转\\\"仅在原始 II_low 值上（random > importance），phase gradient 层面 importance ≥ random。Strategy specificity 的 task-dependence 机制是开放问题（见 §6 Discussion）。这一发现挑战了 compound degradation 均匀分布的隐含假设。\\n\\n**数字基准**：所有数字基于 bf16 per-problem paired 统计量（B=10000 bootstrap）。median_diff 定义为 median(II_low_i − II_high_i)（逐 problem 配对差的中位数）。fp16 旧数据已弃用。\\n\\n## Narrative Arc\\n\\nCompound sparsity 是高效 LLM 推理的实用部署需求，但 prior work（SparK, Ada-KV, SLiM）将 compound interaction 视为均匀超可加。我们发现 severity 是 strategy × phase 交互的涌现属性：importance eviction 的 compound interaction 在 low-sparsity phase 远大于 high-sparsity phase（paired median difference 单调递增 0.39→8.48），而 random eviction 在低 sparsity (s015/s020) NS，在 s025+ 跨模型显著但效应量远小于 importance (2.7-17×)——存在 sparsity threshold (~s020-s025)，低于阈值 compound effect importance-specific，高于阈值两者均触发但 importance 主导。Cross-model replication 方向一致（Qwen magnitude ~1/4 of DeepSeek，onset threshold s≥0.20）。LLaMA 跨架构验证已完成（c8_llama_n250_fixed, n=250, D060）：within-importance phase gradient 强（d_z=0.81-1.15, all p<10^-29），random 所有条件显著（d_z=0.41-0.46, all p<10^-12），但 imp/rand ratio 仅 2.0-2.6×（远低于 DS 15-17×），strategy×phase 交互强度 architecture-dependent。Recency-based eviction（scoring-independent control, D100/D102）跨三个 sparsity level 均产生 null phase gradient（s015+s025 为 primary evidence，s030 supplementary due to numerical instability at extreme sparsity），确认 phase-dependent severity 是 attention-score-based eviction 的特有交互效应而非 token removal 的 trivial 副产物。我们通过 discrimination collapse 机制解释这一现象：head pruning → importance score 的判别力崩塌（Gini/CV 下降跨模型一致）→ importance eviction 退化为有偏伪随机。Attention entropy redistribution 作为 model-dependent secondary effect 在 DeepSeek 上观察到，但在 Qwen 上不稳健（D044）。\\n\\n**Framing 硬约束（D015）**：\\n- MUST: \\\\\\\"emergent phase-strategy interaction\\\\\\\"\\n- MUST NOT: \\\\\\\"importance metric limitation / importance is broken\\\\\\\"\\n- MUST NOT: claim \\\\\\\"importance masking produces super-additive interaction\\\\\\\" without qualifier — random masking also produces positive II, and at s025+ random is statistically significant (D063). The distinguishing signal is **magnitude gradient** (importance 2.7-17× larger) and **onset threshold** (random NS below ~s020, importance significant from s015+), not the existence of super-additivity itself (D023)\\n\\n## Core Claims\\n\\n| ID | Claim | Status | Key Evidence |\\n|----|-------|--------|-------------|\\n| C1 | Compound sparsity severity is strategy- and task-modulated | confirmed | MATH-500: importance gradient 15-17× random (DeepSeek s025-s030); GSM8K: ratio 衰减至 2.3-3.8× (D075)。Phase gradient 层面 importance ≥ random 跨 benchmark 成立，但 magnitude ratio task-dependent。Threshold ~s020-s025 (D063) |\\n| C2 | Severity is phase-modulated (amplified in low-sparsity phase) | confirmed | bf16 paired median difference 单调递增: 0.39→1.21→3.99→8.48; Bonferroni p<0.005 全 4 水平 (D032)。预注册：n=500 后若 QW s015 CI 仍跨零，叙事改为 'compound effect emerges above threshold sparsity (~s020)' |\\n| C3 | Phase-strategy crossover exists | confirmed | s=0.25: importance high_phase=0.032 < random=0.818, importance low_phase=7.196 > random=1.363 (bf16) |\\n| C4 | Discrimination collapse as primary mechanism; entropy redistribution model-dependent | partially_confirmed | D044: Gini/CV 下降跨模型一致; entropy collapse DeepSeek 一致但 Qwen s025 反转(+0.045) s030≈0。30/30 problems completed. |\\n| C5 | Phase-modulated compound severity generalizes across models | confirmed | DeepSeek + Qwen cross-model replication: 方向一致, Cohen's d ρ=1.0, gradient permutation p=0.043. Qwen magnitude ~1/4 of DeepSeek, onset threshold s≥0.20 (S3→C). |\\n| C5b | Phase-aware mitigation recovers compound degradation | future_work | D056: pilot 完成 gate_failed。Oracle recovery 18% < 30% gate (Wilcoxon p=0.002)，heuristic 32% 但 CI 跨零。方向正确但效应量不足，需更精细 phase boundary estimation → future work |\\n| C6 | Severity gradient is sub-exponential | confirmed | Growth rate decreasing: Δ增长因子 3.8×→4.8×→2.0×（递减） |\\n| C7 | Statistical power at n=500 confirms dose-response | confirmed | c2_n500_deepseek (success) + c2_qw_n500_r3 (success): 两模型 n=500 全 4 sparsity Bonferroni p<0.005, Spearman ρ=1.0 |\\n| C8 | Cross-architecture validation (LLaMA) | confirmed | c8_llama_n250_fixed (n=250, D060): within-importance phase gradient d_z=0.81-1.15 (all p<10^-29, all monotonic) ✓。Random 所有条件显著 (d_z=0.41-0.46, all p<10^-12)，与 DeepSeek/Qwen random 低 sparsity NS 模式定性不同。Imp/rand Δ ratio 2.0-2.6×（远低于 DS 15-17×）。Strategy specificity architecture-dependent。n=250 功效充分。 |\\n| C9 | Differentiation from Lethe/SparK prior work | planned | Related Work §2 引用区分 + SparK gap analysis |\\n| C10 | Phase gradient cross-benchmark robust; strategy specificity task-modulated | confirmed | GSM8K DS gradient 0.241→4.682 单调递增; QW gradient 0.039→2.092; imp/rand ratio 衰减至 2.3-3.8× (D075)。QW random s025+s030 均 success |\\n| C11 | Phase-dependent severity absent under scoring-independent eviction (recency control) | confirmed | D102: 三个 sparsity level 全部 NS。s015+s025 为 primary evidence (n=100 each, both d_z < 0.1, p > 0.5); s030 supplementary (numerical instability at extreme sparsity)。对比 importance: d_z=0.574-1.15, ratio=119.8×。Triple dissociation confirmed: importance 有 gradient, recency + random 均 NS。排除 (a) phase segmentation circularity (b) H2O scoring pathway confound。文献中无先例将 recency eviction 作为 methodological control (experimental design contribution)。 |\\n| S3→C | Onset threshold is model-dependent (DeepSeek s≥0.15, Qwen s≥0.20) | confirmed | D037/D038: Qwen s015 d_z=0.37 CI含0, s020+ 显著 |\\n| S7→C | Dose-response monotonicity (Spearman ρ=1.0) | confirmed | D047: 6-point dose-response, 单调递增 |\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Generalizability — 7B models only, benchmark scope\\n- **预期质疑**: \\\\\\\"Results on two 7B models and MATH-500 only. How do we know this generalizes to larger models or other reasoning tasks?\\\\\\\"\\n- **应对**: 四层泛化证据：(1) Cross-model: DeepSeek-R1-Distill-Qwen-7B + Qwen2.5-7B-Instruct（同架构不同训练，ρ=1.0）(2) Cross-architecture: c8_llama_n250_fixed (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM, n=250)，within-importance phase gradient 强 (d_z=0.81-1.15)，但 strategy specificity 弱于 Qwen2 架构（2.0-2.6× vs 15-17×），strategy×phase 交互强度 architecture-dependent (3) **Cross-benchmark (D075)**: GSM8K（两模型）phase gradient 单调递增复现（DS: 0.241→4.682; QW: 0.039→2.092），但 strategy specificity ratio 从 MATH-500 15-17× 衰减至 2.3-3.8×，表明 phase modulation 跨 benchmark 稳健而 magnitude modulation task-dependent。Limitations 诚实声明：(a) 7B scale only；(b) strategy specificity 强度 task-dependent（GSM8K 衰减，可能因推理链更短）；(c) random phase gradient 行为 architecture-dependent。\\n- **实验支撑**: C5 (cross-model) + C8 (c8_llama_n250_fixed cross-architecture, n=250) + C10 (cross-benchmark GSM8K, D075)\\n\\n### RC2: Methodology — phase segmentation circularity and scoring confound\\n- **预期质疑**: \\\\\\\"Your phase segmentation uses perplexity computed from the same model whose sparsity you're measuring. Isn't this circular? And H2O's attention-score mechanism could itself create the phase gradient artifact.\\\\\\\"\\n- **应对**: Recency-based eviction (scoring-independent control, D102 confirmed) produces null phase gradient across all three sparsity levels (s015+s025 primary, s030 supplementary), confirming the observed severity pattern is specific to attention-score-based methods, not an artifact of (a) phase segmentation itself or (b) the scoring computation pathway. Triple dissociation: importance shows gradient (d_z=0.574+), recency and random both NS. Novel experimental design: repurposing recency eviction as methodological control has no precedent in literature (H2O/StreamingLLM use it only as performance baseline).\\n- **实验支撑**: C11 (recency_s015/s025/s030, D102 confirmed) + c4_entropy (discrimination collapse mechanism, D044)\\n\\n### RC3: Practical impact — 没有 throughput 数据\\n- **预期质疑**: \\\\\\\"No wall-clock or throughput measurements. Is the severity amplification reflected in actual inference speed?\\\\\\\"\\n- **应对**: 本文定位是 empirical finding paper（发现 + 机制解释），不是 method paper。Throughput 不是 claim 的一部分。Discussion 中明确 phase-gated controller 作为 future direction。\\n  - C5b pilot 已完成（D056）：oracle recovery 18%（Wilcoxon p=0.002），heuristic recovery 32%（p=0.024），但两者 95% CI 均跨零。方向正确（Wilcoxon 显著）但效应量不足（未达 30% gate），需更精细的 phase boundary estimation。论文 §6 Discussion 诚实报告 pilot 结果 + future work。\\n  - Heuristic > oracle 悖论值得提及：token position ratio 粗粒度划分可能恰好更适合 mitigation 场景，暗示 phase boundary 的最优粒度是开放问题。\\n- **实验支撑**: c5b_pilot (gate_failed, D056)\\n\\n### RC4: Statistical rigor — bootstrap 是否足够\\n- **预期质疑**: \\\\\\\"Per-problem bootstrap with 50 problems — sufficient sample size?\\\\\\\"\\n- **应对**: bf16 使用 B=10000 per-problem paired bootstrap，有效配对数 n=49 (DeepSeek) / n=46 (Qwen)；n=500 实验进一步验证 (C7 confirmed)。Permutation test 使用 paired median difference 作为 robust statistic（D032），Bonferroni 校正后全 4 水平 p<0.005。Dose-response 主用 Wilcoxon signed-rank p + median_diff（robust to outliers），Cohen's d 作为辅助效应量（DeepSeek 0.61→1.13, Qwen 0.37→1.44, registry cohens_d s015→s030），注释高 sparsity 下 d 受 outlier-driven variance 影响（DS s020→s025: median 3.3× jump 但 d 非单调，因极端 II 值影响分母，D064）。可在 appendix 补充 per-problem 分布图（已生成 fig4_per_problem_dist.pdf）。\\n- **实验支撑**: bf16 permutation test (D032) + Cohen's d per-problem paired (rebootstrap B=10000) + n=500 Wilcoxon (C7 confirmed)\\n\\n### RC5: Novelty — prior work 是否已覆盖 phase-dependent sparsity\\n- **预期质疑**: \\\"ThinKV and phase-aware methods already consider phase. What's new?\\\"\\n- **应对**: Prior work 在单轴上分析 phase（ThinKV: phase-aware eviction）或 compound（SparK: joint compression）。没有工作同时分析 compound × phase × strategy 的三维交互。Crossover 现象（同一 strategy 在不同 phase 方向反转）是全新发现。Related Work 加 Lethe 引用区分 + SparK 对比。具体区分：\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025): 在 KV cache 单轴上做 phase-aware 压缩（按 CoT 阶段差异化 eviction），但不涉及 pruning × eviction 的 compound interaction。我们研究的是双轴（head pruning × KV eviction）compound interaction 如何随 phase 变化，ThinKV 的单轴 phase-aware 策略是我们分析维度的子集。\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026): 揭示了单轴 KV 压缩的 phase transition 和 representational rigidity，是机制层面最接近的工作。关键区分：他们刻画的是单一压缩轴上压缩率的 critical threshold（phase transition），我们刻画的是两种压缩方法的 compound interaction severity 如何被 reasoning phase 调制（phase-dependent gradient）——维度正交。\\n  - **HIES** (arxiv 2510.13832, Oct 2025): 发现 importance score collapse 并提出 entropy 补偿，为我们的 discrimination collapse 机制提供独立 supporting evidence——他们在单轴上观察到的 score collapse 正是我们在 compound setting 中发现的 Gini/CV 下降的单轴对应。\\n  - **R-KV** (arxiv 2505.24133, May 2025): 针对 reasoning task 做 KV compression 优化，属于 task-specific method。我们不是提出新方法，而是 mechanistic 分析 compound interaction 的 phase-dependent 行为，二者目标不同（optimization vs understanding）。\\n- **实验支撑**: C3 (crossover), Related Work §2 的 gap 分析\\n\\n### RC6: Novelty vs Lethe/SparK\\n- **预期质疑**: \\\"How does this differ from Lethe (AAAI 2026) which also does layer-time-adaptive KV pruning, or SparK which studies compound compression?\\\"\\n- **应对**: Lethe 和 SparK 都没有分析 phase × strategy 的交互效应。Lethe 是 method paper（提出 adaptive eviction 方法），我们是 empirical finding paper（发现 phase-dependent severity gradient）。SparK 研究 compound compression 但将 interaction 视为均匀超可加，我们发现 interaction severity 随 phase 和 strategy 变化。新近工作进一步确认我们的独特定位：\\n  - **Physics of KV Cache Compression** (arxiv 2603.01426, Mar 2026) 是最近的相关工作，研究单轴压缩的 phase transition 阈值行为。与我们的核心区别：他们的 phase transition 是压缩率维度上的 critical point，我们的 phase-dependent gradient 是 reasoning phase 维度上 compound interaction 的连续调制——两者刻画的 \\\"phase\\\" 语义不同（compression-rate phase vs reasoning phase）。\\n  - **ThinKV** (arxiv 2510.01290, Oct 2025) 和 **R-KV** (arxiv 2505.24133, May 2025) 都在 KV compression 单轴上引入 phase/reasoning awareness，但均未涉及 compound interaction。我们的贡献在于揭示 pruning × eviction 双轴交互如何被 reasoning phase 调制，这是单轴方法无法观察到的涌现现象。\\n  - **HIES** (arxiv 2510.13832, Oct 2025) 的 importance score collapse 发现为我们的 discrimination collapse 机制提供了独立佐证，但 HIES 聚焦于单轴补偿方法，未研究 collapse 在 compound setting 中的放大效应。\\n  - Related Work §2 明确区分三者定位：Lethe/SparK = method/compound method, ThinKV/R-KV = single-axis phase-aware, Physics of KV = single-axis phase transition, HIES = single-axis collapse。我们 = compound × phase × strategy 三维交互分析。\\n- **实验支撑**: 不需要额外实验，仅需 §2 引用区分\\n\\n## Paper Positioning\\n\\n**类型**: Empirical finding paper（非 method paper）\\n**核心贡献**:\\n1. 发现 compound sparsity severity 的 strategy × phase 交互\\n2. 量化 severity gradient（bf16 paired median difference 0.39→8.48, Cohen's d 0.61→1.13）和 crossover 现象\\n3. 提出 discrimination collapse 机制解释（Gini/CV 跨模型一致；entropy redistribution model-dependent）\\n4. Cross-model + cross-architecture (LLaMA, n=250) replication 验证泛化性（三模型两架构；strategy×phase 交互强度 architecture-dependent, D060）\\n5. Novel use of scoring-independent eviction (recency-based) as methodological control — experimental design contribution 排除 phase segmentation circularity 和 scoring pathway confound (C11, D102 confirmed)\\n\\n**投稿目标**: EMNLP 2026 ARR, deadline 2026-05-25\\n**Rebuttal 准备**: Day 9 (2026-05-23) 预留 rebuttal letter 写作时间\\n**关键时间线**：\\n- Day 9 (2026-05-23): 预留写 rebuttal letter\\n- Day 11 (2026-05-25): EMNLP 2026 ARR 截稿\\n\", \"total_chars\": 14093, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ef9991a-e711-4fa5-8950-87b3597f7804",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "b710aa97-3bb3-4a1b-9c27-3f514aae5d74",
  "sourceToolAssistantUUID": "6ef9991a-e711-4fa5-8950-87b3597f7804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T02:11:13.224Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019KvjuBKULPcMvu7M6GYXPP`</summary>

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
  "parentUuid": "b710aa97-3bb3-4a1b-9c27-3f514aae5d74",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L4VPcL7X1MzJQuAkG4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "591ba6ad-4db1-4944-818c-ae2f5c4986ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XK77s74hKcLARhHc6T8HhA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6658,
      "cache_read_input_tokens": 25345,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 25345,
          "cache_creation_input_tokens": 6658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6658,
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

_source line 14 · 2026-05-17T02:11:13.251Z_

<details><summary>↩ Tool result · `toolu_019KvjuBKULPcMvu7M6GYXPP`</summary>

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
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/abstract.tex
artifacts/dream_reports/dream_20260517T005655/best/paper.tex
artifacts/dream_reports/dream_20260517T005655/median/paper.tex
artifacts/dream_reports/dream_20260517T005655/worst/paper.tex
artifacts/dream_reports/dream_20260517T013445/best/paper.tex
artifacts/dream_reports/dream_20260517T013445/median/paper.tex
artifacts/dream_reports/dream_20260517T013445/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "591ba6ad-4db1-4944-818c-ae2f5c4986ae",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "990be562-6f7a-4a69-956f-9f5b1d566d33",
  "sourceToolAssistantUUID": "591ba6ad-4db1-4944-818c-ae2f5c4986ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T02:11:16.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GNoXQWiV1c6q5boyRULDwn`</summary>

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
  "parentUuid": "990be562-6f7a-4a69-956f-9f5b1d566d33",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L54TwyzPGjwccH3xiF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54c8a820-861b-463a-88ca-46f2eb82d203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MJU34btZLHLV6oak6BEyW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 32003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 16 · 2026-05-17T02:11:16.159Z_

<details><summary>↩ Tool result · `toolu_01GNoXQWiV1c6q5boyRULDwn`</summary>

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
  "parentUuid": "54c8a820-861b-463a-88ca-46f2eb82d203",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "d62ac959-1429-435d-aab3-60ca9ca7cdc9",
  "sourceToolAssistantUUID": "54c8a820-861b-463a-88ca-46f2eb82d203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T02:11:17.109Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192T1Lschg4PZBMLEJNb52V`</summary>

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
  "parentUuid": "d62ac959-1429-435d-aab3-60ca9ca7cdc9",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L54TwyzPGjwccH3xiF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b6292e1-2991-41e2-943f-68fb07f4fda3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MJU34btZLHLV6oak6BEyW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 32003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 18 · 2026-05-17T02:11:17.115Z_

<details><summary>↩ Tool result · `toolu_0192T1Lschg4PZBMLEJNb52V`</summary>

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
  "parentUuid": "9b6292e1-2991-41e2-943f-68fb07f4fda3",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "de094527-5ee4-4b7c-b9f0-d687843cfa99",
  "sourceToolAssistantUUID": "9b6292e1-2991-41e2-943f-68fb07f4fda3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T02:11:17.261Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LGa6dLsp3fusX2p8XoJV8i`</summary>

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
  "parentUuid": "de094527-5ee4-4b7c-b9f0-d687843cfa99",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L54TwyzPGjwccH3xiF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6c88ea8-870d-4e8e-965a-fb81d5c56220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MJU34btZLHLV6oak6BEyW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 32003,
      "output_tokens": 244,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 244,
          "cache_read_input_tokens": 32003,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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

_source line 20 · 2026-05-17T02:11:17.267Z_

<details><summary>↩ Tool result · `toolu_01LGa6dLsp3fusX2p8XoJV8i`</summary>

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
  "parentUuid": "e6c88ea8-870d-4e8e-965a-fb81d5c56220",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "740368fd-7afa-4265-bfb2-6a58f46317c1",
  "sourceToolAssistantUUID": "e6c88ea8-870d-4e8e-965a-fb81d5c56220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T02:11:22.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DRBLm77WU72Mq1d5nfM3Dh`</summary>

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
  "parentUuid": "740368fd-7afa-4265-bfb2-6a58f46317c1",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L5MojKYnGo9zNFzjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c36dad38-e7e8-40f9-ab54-451f9c7e2ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5cJ4AZMYfiCMSUCQqmZCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4677,
      "cache_read_input_tokens": 32613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4677,
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

_source line 22 · 2026-05-17T02:11:22.308Z_

<details><summary>↩ Tool result · `toolu_01DRBLm77WU72Mq1d5nfM3Dh`</summary>

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
  "parentUuid": "c36dad38-e7e8-40f9-ab54-451f9c7e2ede",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "b178a262-7997-4afe-bb15-f773122c1296",
  "sourceToolAssistantUUID": "c36dad38-e7e8-40f9-ab54-451f9c7e2ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T02:11:22.779Z_

<details open><summary>🔧 Tool call — Read · `toolu_012pL6M1sFaFXi1iLhS81224`</summary>

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
  "parentUuid": "b178a262-7997-4afe-bb15-f773122c1296",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L5MojKYnGo9zNFzjaR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8615734c-f288-467c-b93c-229dbdeaa714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5cJ4AZMYfiCMSUCQqmZCB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4677,
      "cache_read_input_tokens": 32613,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 32613,
          "cache_creation_input_tokens": 4677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4677,
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

_source line 24 · 2026-05-17T02:11:22.786Z_

<details><summary>↩ Tool result · `toolu_012pL6M1sFaFXi1iLhS81224`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
7	\paragraph{Reasoning depth scaling and architecture dependence.}
8	Strategy specificity is not a fixed property but varies along at least two axes. First, it scales with reasoning chain depth: MATH-500 ($15$--$17{\times}$) $>$ GSM8K (${\sim}2{\times}$ point-estimate ratio; random non-significant at $n{=}50$), with within-MATH-500 correlational support (Spearman $\rho > 0$, $p < 0.02$ between trace length and specificity). Second, it is architecture-dependent: LlamaForCausalLM exhibits significant random phase gradients ($d_z{=}0.41$--$0.46$), reducing the importance/random ratio to $2.0$--$2.6{\times}$ compared with $15$--$17{\times}$ on DeepSeek (Qwen2-based). This suggests that the degree to which random eviction is phase-insensitive depends on architectural details of the attention implementation. The depth-scaling pattern is consistent with the discrimination collapse mechanism: longer low-sparsity phases provide more tokens over which pruning-degraded importance scores accumulate errors, amplifying the gap between importance-based and random eviction. The practical implication holds regardless of architecture: as models generate longer reasoning chains (a trend driven by test-time compute scaling~\cite{snell-2024-scaling-test-time}), the penalty for naive compound compression grows superlinearly, though the relative advantage of strategy-aware allocation varies by model family.
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
  "parentUuid": "8615734c-f288-467c-b93c-229dbdeaa714",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "79199389-c146-43d5-974f-1d5c5fb79cc1",
  "sourceToolAssistantUUID": "8615734c-f288-467c-b93c-229dbdeaa714",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T02:11:25.992Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rck9sGf8ioVQUU4se7zZCx`</summary>

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
  "parentUuid": "79199389-c146-43d5-974f-1d5c5fb79cc1",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L5mH7XD57YgpVV3Lee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a33529a1-1db7-4b08-8bc6-6c58780df4e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2uJZUaxw18RnqLkaHZexx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 37290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2061,
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

_source line 26 · 2026-05-17T02:11:26.007Z_

<details><summary>↩ Tool result · `toolu_01Rck9sGf8ioVQUU4se7zZCx`</summary>

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
  "parentUuid": "a33529a1-1db7-4b08-8bc6-6c58780df4e0",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "9ded7c47-c559-4bb9-80ff-08650edbba01",
  "sourceToolAssistantUUID": "a33529a1-1db7-4b08-8bc6-6c58780df4e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T02:11:26.134Z_

<details open><summary>🔧 Tool call — Read · `toolu_0113ioRApw8p4HTNxWYFoeCc`</summary>

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
  "parentUuid": "9ded7c47-c559-4bb9-80ff-08650edbba01",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L5mH7XD57YgpVV3Lee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07f1f627-c373-4fcd-8cb1-3b4cc9595c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2uJZUaxw18RnqLkaHZexx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 37290,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2061
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 37290,
          "cache_creation_input_tokens": 2061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2061,
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

_source line 28 · 2026-05-17T02:11:26.138Z_

<details><summary>↩ Tool result · `toolu_0113ioRApw8p4HTNxWYFoeCc`</summary>

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
  "parentUuid": "07f1f627-c373-4fcd-8cb1-3b4cc9595c3f",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "1fbbec95-a08b-454f-bc5f-71f3490aee2d",
  "sourceToolAssistantUUID": "07f1f627-c373-4fcd-8cb1-3b4cc9595c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T02:11:30.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MjSGUduyCZW8y6Xw7AMoHh`</summary>

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
  "parentUuid": "1fbbec95-a08b-454f-bc5f-71f3490aee2d",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L61caQ4STsygTkHzZ8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da761f53-7269-404b-b1da-8f009b696e4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXmCtw7ho89bZSFKUxbkWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10002,
      "cache_read_input_tokens": 39351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10002,
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

_source line 30 · 2026-05-17T02:11:30.559Z_

<details><summary>↩ Tool result · `toolu_01MjSGUduyCZW8y6Xw7AMoHh`</summary>

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
  "parentUuid": "da761f53-7269-404b-b1da-8f009b696e4f",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "afa4b28d-4cde-4c4f-acc9-f1d7e0ae7b08",
  "sourceToolAssistantUUID": "da761f53-7269-404b-b1da-8f009b696e4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T02:11:31.598Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Angn4aj4UfjMKwzKLMgT74`</summary>

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
  "parentUuid": "afa4b28d-4cde-4c4f-acc9-f1d7e0ae7b08",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L61caQ4STsygTkHzZ8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "acb4a764-7031-45c0-888b-932f74a6a8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXmCtw7ho89bZSFKUxbkWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10002,
      "cache_read_input_tokens": 39351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10002,
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

_source line 32 · 2026-05-17T02:11:31.604Z_

<details><summary>↩ Tool result · `toolu_01Angn4aj4UfjMKwzKLMgT74`</summary>

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
  "parentUuid": "acb4a764-7031-45c0-888b-932f74a6a8df",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "6714220e-5c8d-4a61-8397-ebf48104f461",
  "sourceToolAssistantUUID": "acb4a764-7031-45c0-888b-932f74a6a8df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T02:11:31.849Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A5BT9w7ZnPMDdyMNGQT1VX`</summary>

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
  "parentUuid": "6714220e-5c8d-4a61-8397-ebf48104f461",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L61caQ4STsygTkHzZ8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f0700ca-0e99-4114-b441-f4099077f07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NXmCtw7ho89bZSFKUxbkWP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10002,
      "cache_read_input_tokens": 39351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10002,
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

_source line 34 · 2026-05-17T02:11:31.855Z_

<details><summary>↩ Tool result · `toolu_01A5BT9w7ZnPMDdyMNGQT1VX`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) supports that the phase gradient extends beyond the Qwen2 architecture ($n{=}250$, all 8 conditions significant; importance $d_z{=}0.81$--$1.15$), but strategy specificity is substantially weaker ($2.0$--$2.6{\times}$ vs.\ $15$--$17{\times}$ on DeepSeek) because random eviction also exhibits significant phase gradients on LLaMA ($d_z{=}0.41$--$0.46$). This architecture-dependent strategy specificity indicates that the degree of strategy${\times}$phase interaction, not just absolute magnitude, varies across attention implementations. The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form: complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks (code generation, multi-hop QA) produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Eviction strategy scope and H$_2$O confound.}
8	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring~\cite{h2o-neurips2023}, Eq.~\ref{eq:kv-importance}), which creates an inherent confound: head pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report, including importance discrimination collapse and the phase-strategy crossover, may be partly attributable to this circular dependency rather than to compound sparsity \emph{per se}. Other attention-mass-based methods (SnapKV~\cite{snapkv-neurips2024}, PyramidKV~\cite{pyramidkv-colm2025}) share the same scoring basis and would likely exhibit a similar confound. The recency control (\S\ref{sec:scoring-control}) partially addresses this by confirming that the phase gradient requires the attention-score pathway ($d_z{=}0.083$, NS under recency eviction vs.\ $d_z{=}0.574$ under importance at matched $s{=}0.15$). However, recency eviction was tested at a single sparsity level ($n{=}100$ pilot, vs.\ $n{=}500$ for importance); comprehensive evaluation across sparsity levels, and testing of other score-independent strategies (e.g., learned eviction policies), remains an important next step. The qualitative conclusion (gradient absence, CI spanning zero) is robust to sample size: post-hoc power analysis indicates $n{=}100$ provides power $> 0.85$ to detect effects of $d_z \geq 0.30$ at $\alpha{=}0.05$, well below the observed importance effect ($d_z{=}0.57$).
9	
10	\paragraph{Symmetric sparsity assumption.}
11	Our analysis applies symmetric sparsity levels: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) supports that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
12	
13	\paragraph{Phase segmentation validation.}
14	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.88$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
15	
16	\paragraph{Mechanism.}
17	Importance discrimination collapse is a correlational diagnostic observation, not a causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
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
  "parentUuid": "0f0700ca-0e99-4114-b441-f4099077f07f",
  "isSidechain": true,
  "promptId": "1cf267ca-87b9-4a1a-a05d-6c86eb75c132",
  "agentId": "ad176ae12cbd1995e",
  "type": "user",
  "uuid": "f8704721-7563-4c39-9dfb-26f03e5f6d2b",
  "sourceToolAssistantUUID": "0f0700ca-0e99-4114-b441-f4099077f07f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-17T02:13:01.788Z_

Now I have a comprehensive view of the paper. Let me compile my review.

---

## Review: R2 (Novelty/Originality and Related Work Positioning)

---

### 1. Novelty Assessment

**Is "phase-dependent compound severity" genuinely new?** The core observation can be paraphrased as: when you simultaneously prune attention heads and evict KV cache entries, the quality degradation is worse during "exploratory" reasoning phases (where attention is broadly distributed) than during "structured" phases (where attention is concentrated). This is arguably a natural consequence of two well-established facts: (a) importance-based eviction relies on discriminative attention scores, and (b) phases with diffuse attention make those scores less discriminative. The authors themselves acknowledge this through the "importance discrimination collapse" mechanism. The paper essentially documents the expected failure mode of H2O-style scoring under head pruning with phase-level granularity. The finding is not counterintuitive; rather, it quantifies the magnitude of a predictable interaction.

**The "scaling law" claim is overstated.** The paper observes a monotonic dose-response across 4 sparsity levels on 3 models, for 3 eviction strategies. This is an empirical trend, not a scaling law. A scaling law implies a functional form (e.g., power law, log-linear) with predictive utility across regimes not yet tested. The paper provides no parametric fit, no extrapolation beyond tested ranges, and the paper_framing.md itself acknowledges that characterizing "the functional form of G(s)" requires experiments outside the tested range. Calling this a "quantitative scaling law" in the summary is misleading; calling it a "dose-response" throughout the paper is more accurate and the authors deserve credit for using the more cautious terminology in the actual manuscript.

**Discrimination collapse is underdeveloped as a contribution.** The authors state clearly that Gini drops are "near-identical" across importance and random eviction, yet severity diverges by 15-17x. This means the proposed mechanism does not actually explain the core finding. The explanation that "importance-based eviction depends on the very scores that pruning degrades" is a one-sentence truism, not a mechanistic contribution. HIES (2025) already reported importance score collapse under single-axis pruning. The extension to "compound setting" adds one extra variable (head pruning as the source of collapse) but the conceptual leap is minimal. The entropy redistribution analysis fails to replicate on Qwen and is explicitly relegated to "model-dependent secondary effect." The mechanism section ultimately concludes with a correlation, not a causal or explanatory contribution.

**Could a reviewer trivialize this?** Yes. The most concise dismissal: "Removing attention heads degrades the attention scores used for eviction; this obviously hurts more during phases that depend on those scores being accurate (broadly-distributed attention phases). The phase gradient is the expected consequence of attention-score degradation, quantified at 4 sparsity levels." The recency control result partially counters this (recency produces no gradient, showing it is not just "any token removal"), but the null result for random eviction at low sparsity is equally expected since random eviction does not depend on scores at all, so score degradation should not affect it. The interesting finding is that random eviction develops a weak gradient at high sparsity, but this is under-analyzed.

---

### 2. Related Work Assessment

**Reference count and coverage.** The actual Related Work section in the paper is substantially more comprehensive than the "8 references" mentioned in the paper summary. The tex file cites approximately 30+ works across five paragraphs. This is adequate for EMNLP. However, there are notable gaps:

- **Attention head pruning literature**: The paper does cite Voita et al. (2019) and Michel et al. (2019) as foundational head-pruning works, and adds movement pruning (Sanh 2020) and magnitude pruning (Han 2015). This is reasonable coverage for a paper that uses head pruning as one axis rather than contributing to the pruning literature itself.
- **CoT reasoning robustness**: Partially covered through the "silent vs. decisive phase" citation and test-time scaling. Missing: work on faithful reasoning, CoT sensitivity to perturbation (only cited in passing via Lanham 2023 in results).
- **Concurrent KV cache work**: Well covered (H2O, StreamingLLM, SnapKV, AdaKV, DuoAttention, DefensiveKV, RetentiveKV, HIES, etc.).

**Are cited works real and correctly described?** Several citations raise concerns. "SparK [AAAI 2026]," "Lethe [AAAI 2026]," "ThinKV [ICLR 2026 Oral]," "GRASPrune [ACL 2026]," "PM-KVQ [ICLR 2026]," and "Physics of KV Cache Compression [2026]" are all cited as 2025-2026 publications. Given the paper is dated May 2026, these could be contemporaneous or forthcoming works. The sheer density of 2026 citations (many at venues that would be publishing around submission time) requires careful verification. The literature_map.yaml provides arXiv IDs for most, which is reassuring, but a reviewer would flag the number of unpublished/simultaneous works cited as if they are established results.

**Positioning against SparK/ThinKV/Lethe/HIES.** The positioning paragraph does a competent job of articulating the gap: SparK treats compound interaction as phase-invariant, ThinKV is single-axis phase-aware, HIES identifies collapse under single-axis pruning. The claimed novelty of "compound x phase x strategy three-way interaction" is defensible as a specific combination not previously studied, though it is incremental rather than conceptually novel.

**"First to systematically analyze the three-dimensional interaction."** This is likely true in the narrow sense that no one has published this exact combination of measurements. However, the novelty of combining known dimensions into a measurement study is limited. It is the difference between "no one has measured X" and "X is surprising/important enough to warrant measuring."

---

### 3. Significance and Impact

**Who benefits?** The primary audience is researchers studying KV cache compression for reasoning models. Practitioners deploying compound sparsity could use the finding that low-sparsity phases require more conservative budgets, but this is qualitative advice that most practitioners would already intuit ("be careful during important parts of generation"). The pilot mitigation experiment (C5b) failed its pre-registered gate (18% oracle recovery, CI spanning zero), meaning the paper provides no actionable method.

**Practical impact is severely limited.** The paper explicitly positions itself as a measurement study with no method contribution. The "phase-gated analysis framework" is a post-hoc diagnostic, not a deployable system. The Discussion section's engineering utility claims (target operating points, per-phase evaluation metric) are speculative and untested. The authors honestly report the failed mitigation pilot, which is commendable transparency but confirms that the findings have not yet translated to practical benefit.

**Would this change how anyone builds compression systems?** Unlikely in a significant way. The qualitative conclusion ("be more careful about eviction during exploratory reasoning phases") is already implicit in phase-aware systems like ThinKV. The quantitative contribution (the exact magnitudes) may matter for system designers, but 4 sparsity levels on 3 models with a single eviction strategy (H2O-style) is too narrow to be a general design guide.

---

### 4. Strengths

- Rigorous statistical methodology: nonparametric bootstrap (B=10,000), Bonferroni correction, Jonckheere-Terpstra test, paired within-problem design, post-hoc power analysis. The statistical rigor exceeds most empirical ML papers.
- Honest reporting of limitations: failed mitigation pilot is reported transparently, entropy redistribution non-replication is acknowledged, correlational status of mechanism is stated clearly.
- Multi-model replication across two architecture families (Qwen2 and LLaMA) and three models, with n=250-500 per condition.
- The recency-control experiment is a well-designed methodological contribution that cleanly isolates the scoring mechanism as the driver of phase-dependent severity.
- Cross-benchmark evaluation (MATH-500, GSM8K, GPQA Diamond) addresses task-specificity concerns, even though GPQA results are pending.

---

### 5. Weaknesses

- **(Major)** Limited novelty: The core finding (score-based eviction fails worse during phases with diffuse attention) is predictable from first principles. The paper quantifies an expected phenomenon rather than revealing a surprising one.
- **(Major)** No method contribution: The paper positions itself as "empirical finding," but the finding alone does not pass the significance bar for a top venue without being either highly surprising or immediately actionable. It is neither.
- **(Major)** Incomplete results: Tables 5 and 6 (Qwen2.5-14B scale analysis, GPQA Diamond) contain placeholder "---" values. Submitting a paper with placeholder tables is a desk-reject risk.
- **(Moderate)** The "discrimination collapse" mechanism does not explain the observation: identical Gini drops across strategies yet 15-17x severity difference. The actual explanation ("importance eviction depends on the scores") is trivial and does not require the Gini analysis.
- **(Moderate)** Narrow model scale: exclusively 7-8B models (14B pending). Whether findings generalize to 70B+ models (where compound sparsity is most practically relevant for deployment) is unknown.
- **(Moderate)** The "scaling law" framing in the summary misrepresents the actual content. Four discrete sparsity levels do not constitute a scaling law. The relationship between chain length and strategy specificity is tested across only 2 benchmarks (MATH-500 vs. GSM8K).
- **(Moderate)** The paper uses em-dashes throughout the abstract (line 1: "sparsity---simultaneously") despite the CLAUDE.md instructions explicitly forbidding them. While this is a style issue, it signals AI-generated text to reviewers.
- **(Minor)** Symmetric sparsity assumption (p=s for both pruning and eviction) limits ecological validity; real deployments typically use asymmetric budgets.

---

### 6. Questions for Authors

1. Can you provide a concrete example where the quantitative findings in this paper would lead to a different system design decision than the qualitative intuition "protect important reasoning phases from aggressive eviction"? What engineering decision requires knowing the exact magnitude of the phase gradient?

2. The Gini coefficient drops identically for importance and random eviction, yet severity diverges by 15-17x. You attribute this to "structural specificity" (importance pruning removes dispersed-attention heads). But if the mechanism is that importance pruning selectively removes certain head types, why does the Gini delta not differ between strategies? Please clarify the causal chain.

3. On LLaMA, random eviction also exhibits significant phase gradients (d_z=0.41-0.46), substantially weakening the "strategy specificity" narrative. Could the DeepSeek/Qwen "random NS at low sparsity" result simply reflect lower statistical power due to smaller effect sizes on those architectures, rather than a fundamental absence of random-strategy phase dependence?

4. The GPQA Diamond and 14B-scale experiments have placeholder results. When will these be available? The paper's generalization claims depend heavily on these pending validations.

5. Given that the mitigation pilot failed its pre-registered gate, what evidence do you have that the phase-dependent severity pattern is addressable? If it cannot be exploited for practical benefit, what is the lasting scientific contribution beyond documenting that "score-based eviction is worse during diffuse-attention phases"?

---

### 7. Scores

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **Novelty** | 2/6 | The core observation is predictable from known properties of attention-score-based eviction. The quantitative characterization is thorough but the finding itself lacks surprise. "Compound x phase x strategy" combination is new in a bookkeeping sense, not conceptually. |
| **Significance** | 2/6 | No method contribution, failed mitigation pilot, narrow model scale. The diagnostic framework is of limited utility without a corresponding intervention. Practitioners gain qualitative advice that is already implicit in phase-aware systems. |
| **Clarity** | 4/6 | The paper is well-organized with clear statistical reporting. The methodology section is precise. However, placeholder tables, em-dashes (AI-style markers), and the gap between the "scaling law" summary framing and actual content reduce clarity of contribution. |
| **Overall** | 2/6 (Reject) | A well-executed measurement study of a predictable phenomenon, with no method contribution, incomplete experiments (placeholder tables), and limited practical impact. The statistical rigor is commendable but cannot compensate for insufficient novelty and significance at a top venue. |
| **Confidence** | 4/5 | I am familiar with the KV cache compression, structured pruning, and compound sparsity literatures. The main uncertainty is whether the pending GPQA/14B results could substantially strengthen the generalization story, but they cannot address the fundamental novelty concern. |

---

### Summary Recommendation

This paper is a competent empirical study with excellent statistical rigor, but it documents a predictable phenomenon (score-based eviction degrades more during phases where scores are less reliable) without providing either a surprising mechanistic insight or a practical contribution. The "discrimination collapse" mechanism does not actually explain the 15-17x divergence, the mitigation pilot failed, and the paper has incomplete experiments (placeholder tables). For EMNLP, I would recommend rejection in the current form. The work could be strengthened by: (1) a working phase-aware controller that demonstrates practical recovery, (2) a genuine mechanistic explanation (not correlation) for why the magnitude diverges 15-17x despite identical Gini drops, or (3) scaling to models where compound sparsity is deployed in practice (70B+).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8704721-7563-4c39-9dfb-26f03e5f6d2b",
  "isSidechain": true,
  "agentId": "ad176ae12cbd1995e",
  "requestId": "req_011Cb7L6SJswfrz3Uo8G97AM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc815d5f-f668-4f7e-85d8-0c0baaf0ad45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "62fd4d67-76f6-455f-8ddb-c4e96d5fa66d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0171awnVa9J51G7ra8xCGA11",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4030,
      "cache_read_input_tokens": 49353,
      "output_tokens": 3316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4030
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3316,
          "cache_read_input_tokens": 49353,
          "cache_creation_input_tokens": 4030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4030,
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
