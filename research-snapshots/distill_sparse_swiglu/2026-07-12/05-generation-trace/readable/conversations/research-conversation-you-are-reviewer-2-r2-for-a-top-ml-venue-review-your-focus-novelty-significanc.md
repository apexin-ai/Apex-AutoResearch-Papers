# Research conversation: You are Reviewer 2 (R2) for a top ML venue review. Your focus: **novelty, significance, positioning against related work

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-abd824c7996585d9b.jsonl`
- **Structured JSON:** [`e079c29916702cf1d353.json`](../../sessions/e0/e079c29916702cf1d353.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-15T17:53:32.480Z_

You are Reviewer 2 (R2) for a top ML venue review. Your focus: **novelty, significance, positioning against related work, and writing quality**. Use a 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue acceptance rate ~25%.

## Paper Summary

**Title**: "Training Signal Meets Correction Granularity: A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs"

The paper presents a two-dimensional taxonomy for learned activation sparsity: training signal (BCE decomposed vs. KL coupled) × correction granularity (none, static bias, contextual compensation MLP). Evaluated on Llama 3.1 8B and Mistral-7B-v0.3 across 12 benchmarks.

**Key claims**:
1. BCE+compensation (PPL 9.40±0.19) matches/outperforms KL-only (PPL 9.80±0.87) at 50% sparsity, with 4.6× lower variance
2. SPON+KL corrections are non-additive (additivity ratio = 0.62)
3. KL–BCE gap does not follow s² scaling (R² = 0.66)
4. BCE+comp advantage increases on Mistral-7B (+1.35 PPL gap vs +0.40 on Llama)

**Paper structure** (11 pages):
- §1 Introduction: Frames the problem as a 2D design space (training signal × correction granularity). Prior work explored isolated cells. Natural hypothesis: KL eliminates need for compensation. Paper tests and refutes this.
- §2 Background and Related Work: SwiGLU sparsity, TEAL/R-Sparse/WINA (training-free), FastForward (BCE+comp), SPON (static+KL), KL divergence for sparsity, Gumbel-sigmoid relaxation.
- §3 Method: 2D taxonomy (Table 1), sparsity predictor with Gumbel-sigmoid, BCE/KL loss formulations, compensation MLP definition.
- §4 Experimental Setup: Models, training details, evaluation suite, conditions.
- §5 Results: 12 subsections covering all experiments.
- §6 Discussion: Reframing KL, compensation as universal mechanism, Lagrangian instability, phase transitions vs scaling laws, limitations.
- §7 Conclusion.

**Table 1 (Taxonomy)**:
|                    | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
|--------------------|-------------------|---------------------|---------------|
| Static             | —                 | —                   | SPON          |
| Per-layer          | —                 | ShadowLLM           | —             |
| Per-token contextual | FastForward     | —                   | **Ours**      |

**Related work coverage**: TEAL, R-Sparse, WINA (training-free), FastForward (BCE+contextual comp), SPON (KL+static), ShadowLLM (MSE+per-layer). The paper positions itself as filling cells and providing the first systematic comparison.

**Key experimental results** (abbreviated):
- Core ablation (Table 2): BCE+comp 9.40±0.19 vs KL-only 9.80±0.87
- STE ablation (Table 4): STE+KL ≈ Gumbel+KL, confirming KL loss (not relaxation) drives quality
- Iso-compute (Table 5): Extended BCE (2333 steps) = 24.80, BCE+comp (1500 steps) = 9.40
- SPON+KL (Tables 7-8): Non-additive, additivity ratio 0.62, cos similarity 0.34 in middle layers
- Sparsity sweep (Tables 12-13): Phase transitions rather than s² scaling
- Mistral (Table 14): BCE+comp advantage widens from +0.40 to +1.35
- Full benchmarks (Table 10): BCE+comp outperforms KL-only on 6/7 benchmarks
- Inference profiling (Table 11): KL-only 1.35×/48MB vs BCE+comp 1.19×/304MB
- LongBench (Table 16): KL-only -18.5% vs BCE+comp -14.2%
- MT-Bench (Table 17): KL-only 5.95 vs BCE+comp 6.30
- RULER (Table 18): KL-only 16K drop -31.3% vs BCE+comp -23.5%

**Discussion highlights**: 
- Reframes KL from "eliminates compensation" to "one cell in taxonomy"
- Compensation is the universal mechanism (architecture-robust)
- KL instability traced to Gumbel annealing (not KL objective itself)
- Phase transitions at architecture-specific thresholds rather than smooth s² scaling

**Limitations acknowledged**: 
- Only 7-8B scale
- 512-token training sequences
- Unoptimized compensation MLP architecture
- 304 MB overhead

## Your Review Tasks

Evaluate the following aspects in detail:

1. **Novelty**: Is the taxonomy itself novel? Are the negative findings (KL doesn't eliminate compensation, non-additivity, no s² scaling) sufficiently novel for a top venue? Is the contribution primarily "we ran a lot of experiments" or is there deeper insight?
2. **Significance**: Does this paper change how practitioners think about activation sparsity? Is the practical impact clear?
3. **Related work**: Are all relevant baselines covered? Is the positioning fair and accurate? Are there missing comparisons (e.g., ShadowLLM results, other recent methods)?
4. **Writing quality**: Is the paper well-organized? Is the narrative clear? Are the claims well-calibrated to the evidence?
5. **Framing and positioning**: Is "characterization study" the right frame for a top venue? Does the paper oversell or undersell its contributions?
6. **Presentation**: Tables, figures (described but not visible), overall readability.

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Detailed comments on novelty and positioning
- Score (1-6) and confidence (1-5)
- Overall recommendation

Be rigorous and specific. Cite section/table numbers where applicable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "06206aad-aff3-4df7-a17d-761385ade231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T17:53:32.482Z_

```json
{
  "parentUuid": "06206aad-aff3-4df7-a17d-761385ade231",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
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
  "uuid": "97e18f9f-1e51-4d66-873a-0770698f4fef",
  "timestamp": "2026-05-15T17:53:32.482Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T17:53:36.372Z_



I'll start by reading the paper and related project files to give a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97e18f9f-1e51-4d66-873a-0770698f4fef",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nJyYBjDaAVwigKo8k2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8c2c75e-b3d3-4315-8a3f-ce86411a1bec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWErjedpE4gwLkikMu8VJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7418,
      "cache_read_input_tokens": 8252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7418,
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

_source line 4 · 2026-05-15T17:53:36.942Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0128edf692VJzWNsX9566M3Y`</summary>

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
  "parentUuid": "c8c2c75e-b3d3-4315-8a3f-ce86411a1bec",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nJyYBjDaAVwigKo8k2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46cf508e-068d-4156-8a44-5fb69bc5b24e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWErjedpE4gwLkikMu8VJu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7418,
      "cache_read_input_tokens": 8252,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 8252,
          "cache_creation_input_tokens": 7418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7418,
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

_source line 5 · 2026-05-15T17:53:36.947Z_

<details><summary>↩ Tool result · `toolu_0128edf692VJzWNsX9566M3Y`</summary>

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
  "parentUuid": "46cf508e-068d-4156-8a44-5fb69bc5b24e",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "274707e4-1751-4afc-9d57-5ca41d715621",
  "sourceToolAssistantUUID": "46cf508e-068d-4156-8a44-5fb69bc5b24e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T17:53:40.080Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_013WLLtmCzb928PgDQ2to3Lp`</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "274707e4-1751-4afc-9d57-5ca41d715621",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKK1ToDrcqrjeH8SDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5b62532-2fcc-403b-a72c-636793b53ec6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bQuTa81A5wK45K391TQYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-15T17:53:40.150Z_

<details><summary>↩ Tool result · `toolu_013WLLtmCzb928PgDQ2to3Lp`</summary>

```text
{"result":"# 项目 distill_sparse_swiglu 概况\n\n## 实验状态 (21 个)\n\n- **mvp_kl_norm_v2_s123**: DONE (success) — \n- **mvp_kl_norm_v2_s42**: DONE (success) — \n- **spon_kl_s42**: PREPARING — \n- **kl_only_s1**: RUNNING — \n- **kl_only_s0**: RUNNING — \n- **mvp_kl_norm_s456**: PREPARING (killed) — \n- **kl_norm_v3_quicktest**: PREPARING (success) — \n- **mvp_kl_norm_s123**: DONE (failed) — \n- **mvp_kl_norm_s42**: DONE (failed) — \n- **kl_normalized_quicktest**: DONE (failed) — \n- **mvp_kl_s456**: QUEUED (killed) — \n- **mvp_kl_s123**: QUEUED (killed) — \n- **kl_lagrangian_v2**: PREPARING (killed) — \n- **kl_lagrangian_quicktest**: DONE (negative) — \n- **mvp_kl_s42**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| kl_only_s1 | — | — | — | — |\n| kl_only_s0 | — | — | — | — |\n\n## 待处理\n- spon_training（等待人工审批）\n- bce_comp_staged_s42（等待人工审批）\n- mvp_kl_s456（排队等待 GPU）\n- mvp_kl_s123（排队等待 GPU）\n- spon_kl_s42（准备中）\n- mvp_kl_norm_s456（准备中）\n- kl_norm_v3_quicktest（准备中）\n- kl_lagrangian_v2（准备中）\n\n## 近期结论\n- **mvp_kl_norm_v2_s456** (success): —\n- **mvp_kl_norm_v2_s123** (success): —\n- **mvp_kl_norm_v2_s42** (success): —\n\n## 趋势\n成功 6 / 负向 2 / 失败 3 / 共 11\ncalibration_samples: 32 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-34887: 无 GPU 信息\n\n## 告警\n- kl_normalized_quicktest: 训练失败 — unknown\n- mvp_kl_norm_s42: 训练失败 — unknown\n- mvp_kl_norm_s123: 训练失败 — unknown"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5b62532-2fcc-403b-a72c-636793b53ec6",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "d738e681-08b2-42d1-b82c-6dacde392f59",
  "sourceToolAssistantUUID": "b5b62532-2fcc-403b-a72c-636793b53ec6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T17:53:40.653Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012MTNeerH7nojJetsjwiieG`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d738e681-08b2-42d1-b82c-6dacde392f59",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKK1ToDrcqrjeH8SDk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b16bffc-814a-40a0-9bfa-885a72ee54d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011bQuTa81A5wK45K391TQYo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 9 · 2026-05-15T17:53:40.662Z_

<details><summary>↩ Tool result · `toolu_012MTNeerH7nojJetsjwiieG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| kl_only_s1 | — | — | — | — |\\n| kl_only_s0 | — | — | — | — |\\n\\n## 待处理\\n- spon_training（等待人工审批）\\n- bce_comp_staged_s42（等待人工审批）\\n- mvp_kl_s456（排队等待 GPU）\\n- mvp_kl_s123（排队等待 GPU）\\n- spon_kl_s42（准备中）\\n- mvp_kl_norm_s456（准备中）\\n- kl_norm_v3_quicktest（准备中）\\n- kl_lagrangian_v2（准备中）\\n\\n## 近期结论\\n- **mvp_kl_norm_v2_s456** (success): —\\n- **mvp_kl_norm_v2_s123** (success): —\\n- **mvp_kl_norm_v2_s42** (success): —\\n\\n## 趋势\\n成功 6 / 负向 2 / 失败 3 / 共 11\\ncalibration_samples: 32 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-34887: 无 GPU 信息\\n\\n## 告警\\n- kl_normalized_quicktest: 训练失败 — unknown\\n- mvp_kl_norm_s42: 训练失败 — unknown\\n- mvp_kl_norm_s123: 训练失败 — unknown\\n\", \"total_chars\": 793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b16bffc-814a-40a0-9bfa-885a72ee54d8",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "f56873d5-350d-4768-a565-6d70fa7ed6b1",
  "sourceToolAssistantUUID": "6b16bffc-814a-40a0-9bfa-885a72ee54d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T17:53:43.436Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011DujCDZ61oZoXDwcuM4b5c`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f56873d5-350d-4768-a565-6d70fa7ed6b1",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKafJNavtv225n8Mej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf1253d5-604b-4888-bd1f-72f456773ffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1o1jqoYFPy6Lp2Hg33i5h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 11 · 2026-05-15T17:53:43.445Z_

<details><summary>↩ Tool result · `toolu_011DujCDZ61oZoXDwcuM4b5c`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf1253d5-604b-4888-bd1f-72f456773ffe",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "0bab0683-e67f-426a-8f54-7a0af648cb2d",
  "sourceToolAssistantUUID": "cf1253d5-604b-4888-bd1f-72f456773ffe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T17:53:44.403Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018zvhXkkL2SAdo4B3YAqa4z`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bab0683-e67f-426a-8f54-7a0af648cb2d",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKafJNavtv225n8Mej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a5a293c-f4fc-4de2-af92-1d5ffd6fea99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1o1jqoYFPy6Lp2Hg33i5h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-15T17:53:44.412Z_

<details><summary>↩ Tool result · `toolu_018zvhXkkL2SAdo4B3YAqa4z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md\", \"content\": \"# Memory — distill_sparse_swiglu\\n\\n## 决策记录\\n\\n- [2026-05-15] s0/s1 完成后 GPU 分配：cuda:0 → bce_comp_staged_s42 (plan_001), cuda:1 → spon_training (plan_004)。Director 要求秒级衔接。\\n- [2026-05-15] WINA global 预期会崩（跨层归一化问题），不排查。正式 baseline: TEAL greedy + WINA greedy。WINA global 仅作 \\\"why greedy allocation matters\\\" motivation example。\\n- [2026-05-15] BCE+comp 代码通过 Reviewer：compensation 67.2M params (bottleneck=256)。losses.py / predictor.py / spon.py 全 PASS。\\n- [2026-05-15] SPON 458K params (bias vectors)，dry-run 通过。\\n- [2026-05-15] MVP 结论：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity。KL 非均匀 per-layer 分配 (0.22-0.80)。\\n- [2026-05-15] s456 seed 敏感性：sparse PPL 13.58 vs s42 12.08 / s123 11.91，PPL increase 48.6% vs 31.2%/28.8%。需关注。\\n\", \"total_chars\": 729, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5a293c-f4fc-4de2-af92-1d5ffd6fea99",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "2b52962c-6877-4235-83c2-2f15ff6ca4be",
  "sourceToolAssistantUUID": "7a5a293c-f4fc-4de2-af92-1d5ffd6fea99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T17:53:44.854Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CfY4xDqziByhycM8c5sJB4`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b52962c-6877-4235-83c2-2f15ff6ca4be",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKafJNavtv225n8Mej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0145298c-d1e1-4180-a86a-736e6f6ba2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1o1jqoYFPy6Lp2Hg33i5h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1779,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-15T17:53:44.864Z_

<details><summary>↩ Tool result · `toolu_01CfY4xDqziByhycM8c5sJB4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. (Headline claim)\\n\\n2. **Static and contextual corrections compose additively**: SPON's input-independent bias correction (average-case drift) and KL-trained contextual prediction (per-input variation) provide additive quality recovery. Formalized as modular decomposition c = c_s + c_theta(x) where output-space interaction is negligible.\\n\\n3. **KL advantage grows with sparsity level (testable prediction)**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s — to be validated by 7-level sparsity sweep (plan_008). If empirical scaling deviates from quadratic (linear, log, or phase transition), the actual pattern is itself a finding; abstract/intro will report observed scaling, not assumed quadratic.\\n\\n## Story Spine\\n\\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\\n\\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work tests SPON + contextual composition.\\n\\n- **Our framing / headline question**: \\\"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\\\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\\n\\n- **Headline result template**: \\\"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation subsumes error compensation, enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\\\"\\n\\n## Two-Dimensional Taxonomy (Conceptual Contribution)\\n\\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\\n| Static                   | —                 | —                   | SPON          |\\n| Per-layer                | —                 | ShadowLLM           | —             |\\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\\n\\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. **\\\"Incremental / no new algorithm\\\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\\n\\n2. **\\\"KL wins only because more compute\\\"**: Addressed by iso-compute ablation (plan_003) giving BCE equivalent total FLOPs via extended training.\\n\\n3. **\\\"Gumbel-sigmoid relaxation, not KL, explains gains\\\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\\n\\n4. **\\\"Single model / limited generalization\\\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\\n\\n5. **\\\"Effect size may not hold on downstream tasks\\\"**: Full benchmark suite (PPL + 5 discriminative + LongBench + MT-Bench) covers all axes.\\n\\n6. **\\\"Unfair comparison: BCE+comp close to KL but at higher inference cost\\\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\\n\", \"total_chars\": 5504, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0145298c-d1e1-4180-a86a-736e6f6ba2ed",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "8ca2523e-e8a8-484a-8e23-52c46ceda896",
  "sourceToolAssistantUUID": "0145298c-d1e1-4180-a86a-736e6f6ba2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T17:53:45.460Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019U6J7v2dVoqnHva1RrDiv6`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ca2523e-e8a8-484a-8e23-52c46ceda896",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKafJNavtv225n8Mej",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0f924e8-d15d-4b6b-8ae5-b5dba6a3ce8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1o1jqoYFPy6Lp2Hg33i5h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1779,
      "cache_read_input_tokens": 17117,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1779
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 390,
          "cache_read_input_tokens": 17117,
          "cache_creation_input_tokens": 1779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1779,
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

_source line 17 · 2026-05-15T17:53:45.473Z_

<details><summary>↩ Tool result · `toolu_019U6J7v2dVoqnHva1RrDiv6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/literature_map.yaml\", \"content\": \"# Literature Map: KL Distillation for Sparse SwiGLU Activation Prediction\\n# Last updated: 2026-05-15\\n# Survey scope: 2023-2026, 4 directions\\n\\n# =============================================================================\\n# Direction 1: KL distillation for structured/activation sparsity\\n# Finding: NO prior work uses KL to train an activation sparsity PREDICTOR.\\n# Existing predictors use BCE (DejaVu, ShadowLLM). SPON uses KL but for\\n# learnable bias correction, not predictor training. This is our novelty.\\n# =============================================================================\\n\\n- title: \\\"Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models\\\"\\n  authors: [Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, Tengfei Ma]\\n  venue: ICML 2026\\n  year: 2026\\n  arxiv_id: \\\"2512.12744\\\"\\n  category: direct-competitor\\n  role: \\\"最接近的KL蒸馏用于稀疏性的工作——但SPON训练的是可学习bias项而非predictor\\\"\\n  key_finding: \\\"SPON注入input-independent learnable activation vectors作为sparse computation的anchor，用KL散度(dense vs sparse logits)做distribution matching训练，训练后吸收进bias项，零推理开销\\\"\\n  relevance_to_us: \\\"SPON证明KL divergence比BCE/MSE更适合sparsity场景的distribution matching。但SPON是全局bias correction而非per-token predictor——我们的predictor方案能实现input-dependent的sparsity pattern，比SPON更灵活。SPON在50-60% sparsity下测试，与我们目标一致\\\"\\n\\n- title: \\\"Compact Language Models via Pruning and Knowledge Distillation\\\"\\n  authors: [Saurav Muralidharan, Sharath Turuvekere Sreenivas, Raviraj Joshi, Marcin Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz, Pavlo Molchanov]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv_id: \\\"2407.14679\\\"\\n  category: method-component\\n  role: \\\"KL蒸馏用于结构化剪枝后恢复——验证logit-only KL优于intermediate matching\\\"\\n  key_finding: \\\"Minitron用logit-only forward KL divergence做structured pruning后的distillation recovery，发现仅用KL loss（不用CE或intermediate matching）效果最好，学生模型继承了teacher的inter-token关系和confidence calibration\\\"\\n  relevance_to_us: \\\"支持我们的核心假设：KL divergence保留output distribution比逐元素BCE更优。Minitron的发现（logit-only KL最优）为我们predictor的KL训练目标提供了理论支撑\\\"\\n\\n- title: \\\"Instruction-Following Pruning for Large Language Models\\\"\\n  authors: [Bairu Hou, Qibin Chen, Jianyu Wang, Guoli Yin, Chong Wang, Nan Du, Ruoming Pang, Shiyu Chang, Tao Lei]\\n  venue: ICML 2025\\n  year: 2025\\n  arxiv_id: \\\"2501.02086\\\"\\n  category: method-component\\n  role: \\\"训练sparse mask predictor的范式——input-dependent mask selection\\\"\\n  key_finding: \\\"训练一个sparse mask predictor以instruction为输入动态选择最相关参数子集，联合优化mask predictor和LLM\\\"\\n  relevance_to_us: \\\"架构上与我们类似（训练predictor生成mask），但目标是instruction-aware weight pruning而非activation sparsity。可参考其predictor-LLM联合优化策略\\\"\\n\\n# =============================================================================\\n# Direction 2: Output distribution preservation in pruning/sparsity\\n# =============================================================================\\n\\n- title: \\\"Distilling to Hybrid Attention Models via KL-Guided Layer Selection\\\"\\n  authors: []\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2512.20569\\\"\\n  category: method-component\\n  role: \\\"KL散度引导layer selection——用distribution差异决定哪些层需要保留\\\"\\n  key_finding: \\\"用KL divergence作为指标选择哪些attention层替换为hybrid attention，通过最小化output distribution变化来指导架构决策\\\"\\n  relevance_to_us: \\\"方法论启示：KL divergence不仅可作为训练loss，还可作为layer-wise重要性指标。我们可用per-layer KL分析哪些层的sparsity对output distribution影响最大\\\"\\n\\n# =============================================================================\\n# Direction 3: SPON和类似的learnable bias correction for sparsity\\n# =============================================================================\\n\\n- title: \\\"Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity\\\"\\n  authors: [Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, Narasimha Reddy]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2602.00397\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor + error compensation双组件架构——与SPON的bias correction思路互补\\\"\\n  key_finding: \\\"组合三个组件：(1) lightweight expert predictor选择high-importance neurons，(2) error compensation network修正sparsity误差，(3) layer-wise sparsity scheduler分配计算。50% FFN sparsity下达到1.45x prefill加速\\\"\\n  relevance_to_us: \\\"与我们的方案最可比：都用predictor做activation sparsity。我们的差异在于用KL loss训练predictor而非BCE，且不需要额外的error compensation网络（KL loss本身应该能减少distribution shift）\\\"\\n\\n- title: \\\"Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models\\\"\\n  authors: [Tai An, Ruwu Cai, Yanzhe Zhang, Yang Liu, Hao Chen, Pengcheng Xie, Sheng Chang, Yiwu Yao, Gongyi Wang]\\n  venue: arXiv\\n  year: 2025\\n  arxiv_id: \\\"2508.02128\\\"\\n  category: background\\n  role: \\\"N:M structured activation sparsity——hardware-friendly的sparsity pattern\\\"\\n  key_finding: \\\"Training-free的top-k策略在linear projection层内确定N:M activation masks，在2:4/4:8/8:16多种ratio下有效，可与W8A8量化组合\\\"\\n  relevance_to_us: \\\"如果我们的predictor输出改为N:M structured pattern而非unstructured binary mask，可获得更好的hardware加速。值得作为future work\\\"\\n\\n# =============================================================================\\n# Direction 4: Predictor-based activation sparsity (TEAL, DejaVu, PowerInfer等)\\n# =============================================================================\\n\\n- title: \\\"Training-Free Activation Sparsity in Large Language Models\\\"\\n  authors: [James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, Ben Athiwaratkun]\\n  venue: ICLR 2025 (Spotlight)\\n  year: 2025\\n  arxiv_id: \\\"2408.14690\\\"\\n  category: direct-competitor\\n  role: \\\"TEAL——我们的主要baseline，training-free magnitude pruning\\\"\\n  key_finding: \\\"对所有hidden states施加magnitude-based sparsity（不需训练），在40-50% sparsity下性能降低很小，Llama-2/3和Mistral 7B-70B上验证。50% sparsity下1.8x decoding加速\\\"\\n  relevance_to_us: \\\"TEAL用BCE度量sparsity mask质量（二元对错），我们的核心论点是：BCE只看neuron是否激活的对错，忽略了错误预测对output distribution的差异化影响。KL loss应该能让predictor学到'哪些neuron的错误预测对output影响更大'\\\"\\n\\n- title: \\\"Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time\\\"\\n  authors: [Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali Shrivastava, Ce Zhang, Yuandong Tian, Christopher Re, Beidi Chen]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv_id: \\\"2310.17157\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-based contextual sparsity的开创性工作——我们的直接对比对象\\\"\\n  key_finding: \\\"用两层MLP predictor预测每层的contextual sparsity pattern（哪些attention heads和MLP neurons可跳过），在OPT-175B上实现2x加速。Predictor用BCE训练\\\"\\n  relevance_to_us: \\\"DejaVu是predictor-based sparsity的baseline。其predictor用BCE训练——我们改用KL loss训练类似的predictor。关键差异：DejaVu在per-neuron level用BCE，我们在output distribution level用KL\\\"\\n\\n- title: \\\"ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models\\\"\\n  authors: [Yash Akhauri, Ahmed F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander M Rush, Safeen Huda, Mohamed S Abdelfattah]\\n  venue: EMNLP 2024\\n  year: 2024\\n  arxiv_id: \\\"2406.16635\\\"\\n  category: direct-competitor\\n  role: \\\"DejaVu的改进——更好的predictor架构和sparsity pattern enforcement\\\"\\n  key_finding: \\\"Shadow predictor超越magnitude-based pruning，context-dependent评估attention head和neuron重要性。比DejaVu端到端精度提升15%，速度提升20%\\\"\\n  relevance_to_us: \\\"ShadowLLM改进了predictor架构但仍用BCE-style loss。我们的改进方向正交：不改predictor架构，改训练loss（BCE→KL）。两种改进可能互补\\\"\\n\\n- title: \\\"SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference\\\"\\n  authors: [Jiho Shin, Hoeseok Yang, Youngmin Yi]\\n  venue: DATE 2025\\n  year: 2025\\n  arxiv_id: \\\"2411.12692\\\"\\n  category: background\\n  role: \\\"Training-free sign-bit predictor——极低开销的sparsity预测\\\"\\n  key_finding: \\\"仅比较input和weight的sign bits预测activation sparsity，无需训练。仅适用于ReLU-based LLMs，不适用SwiGLU\\\"\\n  relevance_to_us: \\\"不适用于SwiGLU模型（我们的目标），但其sign-bit方法的简洁性值得参考。SwiGLU缺乏天然sparsity证明trained predictor的必要性\\\"\\n\\n- title: \\\"SVD Contextual Sparsity Predictors for Fast LLM Inference\\\"\\n  authors: [Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, C.C. Korikov]\\n  venue: arXiv\\n  year: 2026\\n  arxiv_id: \\\"2603.14110\\\"\\n  category: direct-competitor\\n  role: \\\"Training-free SVD-based sparsity predictor——用gate projection矩阵的SVD做预测\\\"\\n  key_finding: \\\"对ReGLU FFN的gate projection矩阵做truncation-aware SVD构建sparse pattern predictor，90% FFN sparsity下1.8x decoding加速，benchmark降低<1%\\\"\\n  relevance_to_us: \\\"虽然是training-free competitor，但focus在ReGLU（不是SwiGLU）且需要90%天然稀疏性。我们的方法在SwiGLU的50%目标sparsity下工作，使用场景不同\\\"\\n\\n- title: \\\"CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models\\\"\\n  authors: [Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo Tiwari, Azalia Mirhoseini]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2404.08763\\\"\\n  category: direct-competitor\\n  role: \\\"Contextual thresholding——不训练predictor，用统计threshold做sparsity\\\"\\n  key_finding: \\\"为每个MLP层计算SiLU(x)激活的percentile threshold做sparsification，50% sparsity下性能降低1-2%，无需fine-tuning。Mistral-7B和Llama2-7B上验证\\\"\\n  relevance_to_us: \\\"CATS直接在SwiGLU/SiLU模型上工作，是我们的直接competitor。但CATS是固定threshold不考虑input context，我们的trained predictor是input-dependent的，理论上更优\\\"\\n\\n- title: \\\"R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference\\\"\\n  authors: [Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, Steven Li]\\n  venue: ICLR 2025\\n  year: 2025\\n  arxiv_id: \\\"2504.19449\\\"\\n  category: background\\n  role: \\\"Training-free rank-aware方法——利用input channel sparsity和SVD\\\"\\n  key_finding: \\\"用SVD分解将input channel sparsity映射到output，无需预测active channels。50% model-level sparsity下43%端到端加速\\\"\\n  relevance_to_us: \\\"Training-free baseline。如果R-Sparse在SwiGLU模型上效果很好，我们需要证明trained KL predictor的额外训练成本是值得的\\\"\\n\\n- title: \\\"Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking\\\"\\n  authors: [Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar, Bence Major, Markus Nagel, Paul Whatmough]\\n  venue: MLSys 2025\\n  year: 2024\\n  arxiv_id: \\\"2412.01380\\\"\\n  category: direct-competitor\\n  role: \\\"Predictor-free dynamic pruning for SwiGLU——直接针对SwiGLU的magnitude pruning\\\"\\n  key_finding: \\\"Predictor-free方案动态剪枝SwiGLU MLP层，配合LoRA adapter恢复精度。Phi-3-Medium上46%内存减少+40%吞吐提升\\\"\\n  relevance_to_us: \\\"直接针对SwiGLU的competitor。DIP证明SwiGLU的sparsity pattern难以预测（所以放弃predictor），我们的KL-trained predictor需要证明能克服这个挑战\\\"\\n\\n# =============================================================================\\n# 补充：Activation function替换和sparsity增强\\n# =============================================================================\\n\\n- title: \\\"ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models\\\"\\n  authors: [Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C Del Mundo, Oncel Tuzel, Golnoosh Samei, Mohammad Rastegari, Mehrdad Farajtabar]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv_id: \\\"2310.04564\\\"\\n  category: background\\n  role: \\\"ReLU替换SiLU获得天然sparsity——替代路线\\\"\\n  key_finding: \\\"用ReLU替换SiLU/GELU后continual pretraining，获得天然高稀疏性（>90%），推理计算减少3x\\\"\\n  relevance_to_us: \\\"替代路线：修改activation function vs 训练predictor。我们的定位：不需要修改pretrained模型架构，作为plug-in predictor在现有SwiGLU模型上工作\\\"\\n\\n- title: \\\"Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters\\\"\\n  authors: [Yixin Song, Haotong Xie, Zhengyan Zhang, Bo Wen, Li Ma, Zeyu Mi, Haibo Chen]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2406.05955\\\"\\n  category: background\\n  role: \\\"dReLU获得90%+ sparsity——activation function工程的极致\\\"\\n  key_finding: \\\"提出dReLU使LLM达到近90% sparsity同时保持SOTA性能，2-5x decoding加速\\\"\\n  relevance_to_us: \\\"与ReLU Strikes Back同一思路但更极端。我们不改activation function，这是差异化定位\\\"\\n\\n- title: \\\"ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models\\\"\\n  authors: [Chenyang Song, Xu Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen Chen, Zhiyuan Liu, Guangli Li, Tao Yang, Maosong Sun]\\n  venue: COLING 2025\\n  year: 2025\\n  arxiv_id: \\\"2402.13516\\\"\\n  category: background\\n  role: \\\"Progressive sparsification——渐进式增加sparsity regularization\\\"\\n  key_finding: \\\"三步法：ReLU替换→progressive sparsity regularization（沿sine curve增强）→threshold shifting(FATReLU)。LLaMA2-7B达89.32% sparsity\\\"\\n  relevance_to_us: \\\"ProSparse的progressive training策略可参考：我们的KL predictor训练也可渐进式增加sparsity目标（已在Lagrangian约束中实现）\\\"\\n\\n- title: \\\"Sparsing Law: Towards Large Language Models with Greater Activation Sparsity\\\"\\n  authors: [Yuqi Luo, Chenyang Song, Xu Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun Deng, Jiansheng Wei, Zhiyuan Liu, Maosong Sun]\\n  venue: arXiv\\n  year: 2024\\n  arxiv_id: \\\"2411.02335\\\"\\n  category: background\\n  role: \\\"Activation sparsity的scaling law——理论基础\\\"\\n  key_finding: \\\"SiLU/SwiGLU的activation ratio随训练递增（变密），ReLU递减（变稀）。Sparsity对parameter scale不敏感，与width-depth ratio线性相关\\\"\\n  relevance_to_us: \\\"理论支撑：SiLU/SwiGLU模型天然不够稀疏（随训练变密），因此需要外部predictor/pruning来获得稀疏性——这是我们工作的motivation之一\\\"\\n\\n- title: \\\"A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering\\\"\\n  authors: [Nobel Dhar, Bobin Deng, Md Romyull Islam, Xinyue Zhang, Kazi Fahim Ahmad Nasif, Kun Suo]\\n  venue: Euro-Par 2025\\n  year: 2025\\n  arxiv_id: \\\"2507.14179\\\"\\n  category: background\\n  role: \\\"Clustering-based sparsity prediction——用聚类简化prediction\\\"\\n  key_finding: \\\"将activation patterns聚类为representative clusters，预测cluster assignment而非individual neuron states，减少prediction开销。Mistral-7B上79.34%聚类精度\\\"\\n  relevance_to_us: \\\"降低predictor复杂度的思路。如果我们的per-neuron KL predictor开销太大，可考虑cluster-level prediction\\\"\\n\\n# =============================================================================\\n# 竞争格局总结\\n# =============================================================================\\n#\\n# 我们的独特定位:\\n# 1. 唯一使用KL divergence训练activation sparsity predictor的工作\\n#    - DejaVu/ShadowLLM用BCE训练predictor\\n#    - SPON用KL但训练bias correction而非predictor\\n#    - TEAL/CATS/R-Sparse/SparseInfer/SVD-CSP是training-free\\n# 2. 专注SwiGLU模型的50% sparsity目标\\n#    - ReLU/dReLU方案需要替换activation function\\n#    - 很多training-free方案在SwiGLU上效果不佳(DIP论文证实)\\n# 3. 通过保留output distribution(而非逐neuron匹配)来指导sparsity\\n#    - Minitron/SPON已证明KL loss优于MSE/BCE做distribution matching\\n#    - 我们将此insight应用到predictor训练\\n#\\n# 主要related work定位:\\n# - vs TEAL: trained predictor(input-dependent) vs fixed magnitude threshold\\n# - vs DejaVu/ShadowLLM: KL loss vs BCE loss训练predictor\\n# - vs SPON: predictor vs learnable bias; 都用KL但目标不同\\n# - vs DIP: trained predictor vs predictor-free pruning\\n# - vs ReLU/TurboSparse/ProSparse: 不改activation function\\n# - vs Fast Forward: KL loss vs BCE+error compensation\\n# - vs CATS: input-dependent predictor vs fixed percentile threshold\\n\", \"total_chars\": 13950, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f924e8-d15d-4b6b-8ae5-b5dba6a3ce8c",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "f748035f-cd56-439a-a7ba-9adf13b67697",
  "sourceToolAssistantUUID": "c0f924e8-d15d-4b6b-8ae5-b5dba6a3ce8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T17:53:49.595Z_

Now let me read the actual paper and any writing plan documents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f748035f-cd56-439a-a7ba-9adf13b67697",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKwFYt6AR23wpg5Mzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8d32433-da6c-4abc-9978-295af58cf8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRBkCrVztEhW4LPcVycKsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9169,
      "cache_read_input_tokens": 18896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9169,
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

_source line 19 · 2026-05-15T17:53:50.521Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_015REWBWXstJUSni1dmBdzEo`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8d32433-da6c-4abc-9978-295af58cf8a6",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKwFYt6AR23wpg5Mzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "792078ed-dafd-4a4d-b577-7fbb8ecb282d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRBkCrVztEhW4LPcVycKsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9169,
      "cache_read_input_tokens": 18896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9169,
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

_source line 20 · 2026-05-15T17:53:50.529Z_

<details><summary>↩ Tool result · `toolu_015REWBWXstJUSni1dmBdzEo`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No writing_plan.yaml found for 'distill_sparse_swiglu'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "792078ed-dafd-4a4d-b577-7fbb8ecb282d",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "2b9d8187-043a-4c45-b499-ff1974d25816",
  "sourceToolAssistantUUID": "792078ed-dafd-4a4d-b577-7fbb8ecb282d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T17:53:51.498Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VxBvUFpxdHuinaAJfbDQi5`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b9d8187-043a-4c45-b499-ff1974d25816",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKwFYt6AR23wpg5Mzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d959b87-3b11-417a-a032-9a1d95df5df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRBkCrVztEhW4LPcVycKsy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9169,
      "cache_read_input_tokens": 18896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9169,
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

_source line 22 · 2026-05-15T17:53:51.508Z_

<details><summary>↩ Tool result · `toolu_01VxBvUFpxdHuinaAJfbDQi5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-15 10:07 UTC\\n  summary: 'MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perplexity 对比'\\n  rationale: '核心假设是 KL 训练通过端到端梯度捕获联合神经元交互，优于 BCE 的逐神经元独立目标。MVP 聚焦最基础的 A/B 对比（KL vs\\n    BCE），不涉及 SPON 组合或 compensation network，以最小成本验证核心假设是否成立。Pass criteria: KL ppl <\\n    BCE ppl 差距 ≥ 0.3。评审笔记中的 novelty ceiling 和 effect size 风险恰好需要 MVP 先确认效果量级。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-15 12:08 UTC\\n  summary: 校准数据从 SlimPajama-627B 改为 WikiText-103 train split\\n  rationale: SlimPajama-627B 在 AutoDL 代理环境下 HF datasets API 无法访问（DatasetNotFoundError）。WikiText-103\\n    (~100M tokens) 满足 MVP 1K steps 需求，KL/BCE 用同一数据保证公平性。偏离 IDEA_BRIEF 原始方案，full paper\\n    实验阶段可能需要切回更多样的校准数据。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  - exp_id: mvp_bce_s42\\n    role: affected\\n    result: FAILED due to SlimPajama access\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-15 13:16 UTC\\n  summary: KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_weight\\n  rationale: mvp_kl_s42 的 sparsity 从 0.328 单调降至 0.000。KL loss 天然在 0% sparsity 处最小，固定\\n    reg_weight=0.1 被 KL loss（66 倍量级差）完全压制。Lagrangian multiplier 通过 dual gradient ascent\\n    自动调整约束强度，是约束优化的标准方案。暂停 KL s123/s456 直到修复验证通过。\\n  related_experiments:\\n  - exp_id: mvp_kl_s42\\n    role: evidence\\n    result: sparsity collapsed to 0%, KL=3.3 vs reg=0.05\\n  depends_on:\\n  - D001\\n- id: D004\\n  date: 2026-05-15 13:34 UTC\\n  summary: KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯 KL 端到端训练\\n  rationale: Lagrangian quicktest 确认 lambda 爬升追不上 KL loss 量级（KL~418 vs constraint~1.2）。根因是\\n    KL 用 sum reduction 导致绝对值过大。归一化到 per-token per-dim 后 KL 应降至 ~0.003，与 constraint\\n    可比。选 C 而非 A（BCE warm-start）因为 C 保持原始研究问题（纯 KL 训练），给出最干净的 MVP 信号。\\n  related_experiments:\\n  - exp_id: kl_lagrangian_quicktest\\n    role: evidence\\n    result: sparsity 0.406→0.141, lambda too slow\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-15 14:19 UTC\\n  summary: KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练\\n  rationale: kl_normalized_quicktest 验证 KL/seq_len 归一化 + Lagrangian 配方有效：sparsity\\n    在 200 steps 内收敛到 0.50-0.52，KL loss 与 constraint 同量级。无需再测 KL/(seq_len×vocab_size)\\n    variant。BCE 3-seed 已全部 success，现在用修正配方跑 KL 3-seed (s42/s123/s456) 完成 MVP 对比。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: validation\\n    result: sparsity converged to 0.50-0.52\\n  - exp_id: mvp_kl_s42\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s123\\n    role: next\\n    result: pending\\n  - exp_id: mvp_kl_s456\\n    role: next\\n    result: pending\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-15 14:35 UTC\\n  summary: 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_normalized_quicktest 结论虚假\\n  rationale: Reviewer 独立核实发现 train.py:228 在 KLDistillLoss 已做 ÷seq_len 的基础上又除以 vocab_size(128256)，总归一化\\n    = ÷(seq_len×vocab_size)。实际效果：kl_norm≈0.00007，梯度信号~10^-5，predictor 无法学习神经元重要性。kl_raw\\n    从 1.18 上升至 9.94（而非 Agent 报告的下降）。Agent 的 registry 结论 \\\"seq_len-only 归一化有效\\\" 与代码事实完全矛盾。D005\\n    决策基于虚假数据，作废。修复方案：删除 ÷vocab_size，只保留 ÷seq_len，修复后重新验证。\\n  related_experiments:\\n  - exp_id: kl_normalized_quicktest\\n    role: evidence\\n    result: FALSELY reported as success; actual KL rising, code uses ÷vocab_size not\\n      ÷seq_len\\n  - exp_id: mvp_kl_norm_s42\\n    role: killed\\n    result: Using same buggy code, gradient signal ~10^-5\\n  - exp_id: mvp_kl_norm_s123\\n    role: killed\\n    result: Using same buggy code, just submitted\\n  depends_on:\\n  - D005\\n  - D004\\n- id: D007\\n  date: 2026-05-15 16:49 UTC\\n  summary: 'MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程'\\n  rationale: MVP 结果决定性通过：KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72（差距 31.53 >>\\n    0.3 阈值）。KL 学习非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66），hard-mask PPL 9.20\\n    接近 true dense 6.12。核心假设\\\"KL 通过端到端梯度捕获联合神经元交互优于 BCE\\\"得到强力验证。按 post-mvp-kickoff 流程：写\\n    paper_framing.md + experiment_plan.yaml → dream_simulate → update_roadmap。禁止在\\n    dream 完成前批准新实验。\\n  related_experiments:\\n  - exp_id: mvp_kl_norm_v2_s42\\n    role: evidence\\n    result: success, sparse PPL 12.08\\n  - exp_id: mvp_kl_norm_v2_s123\\n    role: evidence\\n    result: success, sparse PPL 11.91\\n  - exp_id: mvp_kl_norm_v2_s456\\n    role: evidence\\n    result: success, sparse PPL 13.58\\n  - exp_id: mvp_bce_s42\\n    role: evidence\\n    result: success, sparse PPL 44.54\\n  - exp_id: mvp_bce_s123\\n    role: evidence\\n    result: success, sparse PPL 44.59\\n  - exp_id: mvp_bce_s456\\n    role: evidence\\n    result: success, sparse PPL 43.03\\n  depends_on:\\n  - D001\\n  - D004\\n  - D005\\n  - D006\\n\", \"total_chars\": 4509, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d959b87-3b11-417a-a032-9a1d95df5df8",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "d1abf4a6-4779-4db4-953d-79a6165ee1de",
  "sourceToolAssistantUUID": "0d959b87-3b11-417a-a032-9a1d95df5df8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T17:53:54.815Z_

<details open><summary>🔧 Tool call — Glob · `toolu_018BFVrqf5MBPVaaD7GTdiYh`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1abf4a6-4779-4db4-953d-79a6165ee1de",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nKwFYt6AR23wpg5Mzy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf673727-05d9-40d9-a8a8-c30a29f12498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRBkCrVztEhW4LPcVycKsy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9169,
      "cache_read_input_tokens": 18896,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 18896,
          "cache_creation_input_tokens": 9169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9169,
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

_source line 24 · 2026-05-15T17:53:54.825Z_

<details><summary>↩ Tool result · `toolu_018BFVrqf5MBPVaaD7GTdiYh`</summary>

```text
artifacts/dream_reports/dream_20260515T164925/best/paper.tex
artifacts/dream_reports/dream_20260515T164925/median/paper.tex
artifacts/dream_reports/dream_20260515T164925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf673727-05d9-40d9-a8a8-c30a29f12498",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "dc0d84a6-8bb3-400d-b429-8c673dc99cc4",
  "sourceToolAssistantUUID": "cf673727-05d9-40d9-a8a8-c30a29f12498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T17:53:57.342Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MZqvBfYr8iEqbkrzD8fAA7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc0d84a6-8bb3-400d-b429-8c673dc99cc4",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nLdCNjUAj4wikg5NgQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b85e8f3-d363-45d3-a7be-45a506e6835c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRAZdzxnpTmyzfjDPqRTFX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3097,
      "cache_read_input_tokens": 28065,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 28065,
          "cache_creation_input_tokens": 3097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3097,
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

_source line 26 · 2026-05-15T17:53:58.247Z_

<details><summary>↩ Tool result · `toolu_01MZqvBfYr8iEqbkrzD8fAA7`</summary>

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
10	\usepackage{array}
11	\usepackage{xcolor}
12	\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}
13	
14	\title{Output-Distribution Distillation Makes Compensation Networks Obsolete\\for SwiGLU Activation Sparsity}
15	
16	\author{Anonymous}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Activation sparsity in SwiGLU-based large language models enables significant inference speedups by dynamically pruning neurons, but existing learned approaches (e.g., FastForward) train per-neuron binary predictors with BCE loss and require auxiliary compensation networks ($\sim$256\,MB) to recover quality---adding latency and memory overhead.
24	We show that replacing BCE with KL-divergence distillation on the output distribution \emph{eliminates the need for compensation entirely}.
25	On Llama~3.1~8B at 50\% model-level sparsity, a KL-trained contextual predictor without compensation achieves 9.20 perplexity on WikiText-2 (within 50\% of the dense 6.12 baseline), while BCE with compensation reaches only 18.64---a gap of 9.44 PPL points.
26	The advantage stems from KL's gradient structure, which couples all active neurons through the output Jacobian, capturing joint interaction effects that BCE's factorized per-neuron gradient misses.
27	We formalize a modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ combining SPON's static bias correction with KL contextual prediction, achieving 7.98 PPL with only 6.8\% interaction residual.
28	A seven-level sparsity sweep confirms the theoretically predicted quadratic scaling of the KL--BCE quality gap ($R^2 = 0.97$).
29	Cross-architecture validation on Mistral-7B-v0.3, comprehensive downstream benchmarks (MMLU, GSM8K, HumanEval, LongBench, MT-Bench, RULER), and latency profiling demonstrate that KL-only Pareto-dominates BCE+compensation: better quality, lower latency (12.0 vs.\ 13.8\,ms/token), and 10$\times$ fewer additional parameters (24\,MB vs.\ 280\,MB).
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit substantial contextual activation sparsity: at any given input, a large fraction of intermediate neurons contribute negligibly to the output.
36	Exploiting this sparsity at inference time by dynamically skipping inactive neurons can yield wall-clock speedups of $1.3$--$1.5\times$, a practically significant reduction for latency-sensitive deployment.
37	
38	Three tiers of approaches have emerged.
39	\emph{Training-free} methods (TEAL, WINA, R-Sparse) apply static heuristics---magnitude thresholds, weight-informed scores---to select neurons.
40	While requiring no training, these methods incur a 6--9 PPL point gap at 50\% sparsity on Llama~3.1~8B.
41	\emph{Static learned} approaches such as SPON learn input-independent per-layer bias corrections via KL distillation, recovering average-case activation drift but unable to adapt to per-input variation.
42	\emph{Contextual learned} methods, exemplified by FastForward, train a lightweight MLP to predict per-token neuron importance.
43	However, FastForward uses binary cross-entropy (BCE) to train this predictor independently per neuron, then attaches a compensation network to correct the residual error---adding $\sim$256\,MB of parameters and a per-layer GEMV at inference time.
44	
45	We ask: \emph{does the compensation network compensate for a fundamental limitation of the predictor, or for a limitation of the training objective?}
46	The answer hinges on gradient structure.
47	The BCE gradient $\partial\mathcal{L}_{\mathrm{BCE}}/\partial s_j = (\sigma(s_j) - t_j)\sigma'(s_j)$ depends only on neuron $j$'s own target, factorizing across neurons.
48	In contrast, the KL gradient $\partial\mathcal{L}_{\mathrm{KL}}/\partial s_j$ propagates through the full Jacobian $\partial\mathbf{z}/\partial\mathbf{h} \cdot \partial\mathbf{h}/\partial\mathbf{m}$, coupling all active neurons.
49	This coupling captures joint interaction effects that scale as $O(s^2 D^2)$ with sparsity level $s$ and hidden dimension $D$---precisely the effects that compensation networks attempt to correct post hoc.
50	
51	Our contributions:
52	\begin{enumerate}
53	    \item We demonstrate that KL-trained contextual sparsity predictors categorically dominate BCE+compensation: 9.20 vs.\ 18.64 PPL on Llama~3.1~8B at 50\% sparsity, with lower latency and 10$\times$ fewer parameters (\S\ref{sec:ablation}, \S\ref{sec:fullbench}).
54	    \item We formalize a modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ combining static (SPON) and contextual (KL) corrections, achieving 7.98 PPL with near-additive composition (6.8\% interaction residual; \S\ref{sec:composition}).
55	    \item We provide a testable theoretical prediction---the KL--BCE quality gap scales quadratically with sparsity---and confirm it empirically ($R^2 = 0.97$ across seven sparsity levels; \S\ref{sec:scaling}).
56	\end{enumerate}
57	
58	% ============================================================
59	\section{Related Work}
60	
61	\paragraph{Training-free activation sparsity.}
62	TEAL~\cite{liu2024teal} uses magnitude-based thresholding with greedy per-layer budget allocation.
63	WINA~\cite{shen2024wina} incorporates weight magnitudes into the scoring criterion.
64	R-Sparse~\cite{zhang2024rsparse} introduces rank-aware scoring.
65	All three operate without any parameter training but suffer quality gaps of 6--9 PPL points at 50\% sparsity.
66	
67	\paragraph{Learned sparsity prediction.}
68	FastForward~\cite{wang2024fastforward} trains a small MLP per layer to predict binary neuron masks using BCE, then adds a compensation MLP to correct residual errors.
69	SPON~\cite{zhou2024spon} takes a different approach: learning input-independent per-layer bias vectors via KL distillation of the teacher's output distribution.
70	ShadowLLM~\cite{chen2024shadowllm} uses MSE on intermediate representations for per-layer correction.
71	
72	\paragraph{Knowledge distillation for sparsity.}
73	Output-distribution matching via KL divergence is standard in knowledge distillation~\cite{hinton2015distilling} but has not been applied to train \emph{contextual} sparsity predictors.
74	The key distinction is that we distill the \emph{sparsity decision} (which neurons to activate) rather than the model weights, and the KL gradient structure provides a principled advantage over per-neuron objectives.
75	
76	% ============================================================
77	\section{Method}
78	\label{sec:method}
79	
80	\subsection{Problem Setup}
81	
82	Consider a SwiGLU FFN layer with gate projection $\mathbf{g} = \sigma_{\mathrm{SiLU}}(\mathbf{W}_g \mathbf{x})$, up projection $\mathbf{u} = \mathbf{W}_u \mathbf{x}$, and element-wise product $\mathbf{h} = \mathbf{g} \odot \mathbf{u}$.
83	A binary mask $\mathbf{m} \in \{0,1\}^D$ selects a subset of neurons, yielding sparse output $\mathbf{y}_{\mathrm{sparse}} = \mathbf{W}_d (\mathbf{m} \odot \mathbf{h})$.
84	We seek a predictor $f_\theta(\mathbf{x}): \mathbb{R}^{d} \to [0,1]^D$ that produces soft scores, relaxed to masks via Gumbel-sigmoid sampling during training and hard thresholding at inference.
85	
86	\subsection{Gradient Coupling: KL vs.\ BCE}
87	
88	\paragraph{BCE objective.}
89	Given oracle mask $\mathbf{t}$ (e.g., top-$k$ by activation magnitude), the BCE loss is:
90	\begin{equation}
91	\mathcal{L}_{\mathrm{BCE}} = -\sum_{j=1}^{D} \big[ t_j \log \sigma(s_j) + (1-t_j)\log(1-\sigma(s_j)) \big]
92	\end{equation}
93	where $s_j = f_\theta(\mathbf{x})_j$.
94	The gradient $\partial\mathcal{L}_{\mathrm{BCE}}/\partial s_j = \sigma(s_j) - t_j$ depends only on neuron $j$---the loss \emph{factorizes} across neurons.
95	
96	\paragraph{KL objective.}
97	We instead minimize the KL divergence between the dense and sparse model output distributions:
98	\begin{equation}
99	\mathcal{L}_{\mathrm{KL}} = \mathrm{KL}\!\left(p_{\mathrm{dense}}(\cdot|\mathbf{x}) \;\|\; p_{\mathrm{sparse}}(\cdot|\mathbf{x}, \mathbf{m})\right)
100	\end{equation}
101	The gradient with respect to score $s_j$ is:
102	\begin{equation}
103	\frac{\partial\mathcal{L}_{\mathrm{KL}}}{\partial s_j} = \underbrace{\frac{\partial\mathcal{L}_{\mathrm{KL}}}{\partial \mathbf{z}}}_{\text{output error}} \cdot \underbrace{\frac{\partial \mathbf{z}}{\partial \mathbf{h}}}_{\text{down proj}} \cdot \underbrace{\frac{\partial \mathbf{h}}{\partial m_j}}_{\text{neuron }j} \cdot \frac{\partial m_j}{\partial s_j}
104	\end{equation}
105	Critically, $\partial\mathbf{z}/\partial\mathbf{h} = \mathbf{W}_d$ and $\partial\mathcal{L}_{\mathrm{KL}}/\partial\mathbf{z}$ depend on the \emph{full} sparse output, which in turn depends on \emph{all} active neurons.
106	Thus the gradient for neuron $j$ is \emph{coupled} to all other neurons' mask decisions through the shared output space.
107	
108	\paragraph{Quadratic scaling prediction.}
109	When sparsity is $s$, each pruned neuron interacts with $O(sD)$ other pruned neurons.
110	The total pairwise interaction effects scale as $O(s^2 D^2)$.
111	BCE's factorized gradient ignores all such interactions, while KL captures them through the Jacobian.
112	This yields the testable prediction that the KL--BCE quality gap $\Delta(s) \approx a s^2$ for some constant $a$.
113	
114	\subsection{Modular Decomposition}
115	\label{sec:decomposition}
116	
117	We decompose the total correction to the sparse hidden states as:
118	\begin{equation}
119	\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})
120	\end{equation}
121	where $\mathbf{c}_s = \mathbb{E}[\Delta\mathbf{h}]$ is the static, input-independent bias correction (as in SPON), and $\mathbf{c}_\theta(\mathbf{x}) = \Delta\mathbf{h}(\mathbf{x}) - \mathbb{E}[\Delta\mathbf{h}]$ is the per-input residual variation captured by the KL contextual predictor.
122	Since $\mathbf{c}_s$ is constant and $\mathbf{c}_\theta(\mathbf{x})$ is zero-mean by construction, the two corrections are approximately orthogonal.
123	We measure the interaction residual as:
124	\begin{equation}
125	\rho = \frac{\|\mathbf{c} - (\mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x}))\|_2}{\|\mathbf{c}_s\|_2 + \|\mathbf{c}_\theta(\mathbf{x})\|_2}
126	\end{equation}
127	and predict $\rho \ll 1$ when SPON and the KL predictor address different error components.
128	
129	% ============================================================
130	\section{Experiments}
131	\label{sec:experiments}
132	
133	\subsection{Setup}
134	
135	\paragraph{Models.}
136	We evaluate on Llama~3.1~8B (primary) and Mistral-7B-v0.3 (cross-architecture validation).
137	Both use SwiGLU FFN layers with intermediate dimension $D = 14336$ (Llama) and $D = 14336$ (Mistral).
138	
139	\paragraph{Sparsity target.}
140	Unless otherwise noted, we target 50\% model-level sparsity with per-layer budget allocation following TEAL's greedy algorithm.
141	
142	\paragraph{Training.}
143	KL and BCE predictors share identical architecture (2-layer MLP, $\sim$24\,MB per model).
144	Training uses 1000 steps on a 10M-token calibration subset of C4.
145	Gumbel-sigmoid relaxation ($\tau = 1.0 \to 0.1$ cosine anneal) enables gradient flow through discrete masks during training; hard thresholds are used at inference.
146	We report WikiText-2 perplexity as the primary metric.
147	
148	\paragraph{Baselines.}
149	We compare against: (1)~Dense (no sparsity), (2)~TEAL, WINA, R-Sparse (training-free), (3)~SPON (static learned), (4)~BCE-only, BCE+compensation (contextual learned, FastForward-style), and (5)~our KL-only, KL+compensation, and SPON+KL variants.
150	
151	% ------------------------------------------------------------
152	\subsection{Four-Condition Ablation}
153	\label{sec:ablation}
154	
155	Table~\ref{tab:ablation} presents the core ablation at 50\% sparsity on Llama~3.1~8B.
156	
157	\begin{table}[t]
158	\centering
159	\small
160	\caption{Four-condition ablation on WikiText-2 (Llama~3.1~8B, 50\% sparsity). KL-only outperforms BCE+compensation by 9.44 PPL points without any compensation network.}
161	\label{tab:ablation}
162	\begin{tabular}{lcccc}
163	\toprule
164	\textbf{Condition} & \textbf{Seeds} & \textbf{PPL} & \textbf{$\Delta$ Dense} & \textbf{Comp.\ Benefit} \\
165	\midrule
166	Dense & -- & 6.12 & -- & -- \\
167	BCE-only & 3 & 28.16\small{$\pm$0.17} & +360\% & -- \\
168	BCE+comp & 5 & 18.64\small{$\pm$0.33} & +205\% & $-$9.52 \\
169	KL-only & 5 & 9.20\small{$\pm$0.04} & +50\% & -- \\
170	KL+comp & 3 & 9.02\small{$\pm$0.07} & +47\% & $-$0.18 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	KL-only achieves 9.20$\pm$0.04 PPL, surpassing BCE+compensation (18.64$\pm$0.33) by 9.44 points.
176	Adding compensation to KL yields only 0.18 PPL improvement (9.02 vs.\ 9.20), compared to 9.52 for BCE.
177	The extremely low standard deviation across 5 seeds (0.04) confirms high reproducibility.
178	The compensation network is made redundant by KL's gradient coupling---it corrects at training time what compensation would correct at inference time.
179	
180	% ------------------------------------------------------------
181	\subsection{Isolating Loss vs.\ Relaxation (STE Baseline)}
182	\label{sec:ste}
183	
184	A natural concern is whether the advantage comes from the KL loss function or from Gumbel-sigmoid relaxation.
185	We replace Gumbel-sigmoid with Straight-Through Estimation (STE) while keeping KL loss, shown in Table~\ref{tab:ste}.
186	
187	\begin{table}[t]
188	\centering
189	\small
190	\caption{Relaxation method ablation. STE+KL still dominates Gumbel+BCE, confirming the loss function drives $>$97\% of the advantage.}
191	\label{tab:ste}
192	\begin{tabular}{llcc}
193	\toprule
194	\textbf{Condition} & \textbf{Relaxation} & \textbf{Loss} & \textbf{PPL} \\
195	\midrule
196	Gumbel+KL (ours) & Gumbel-sigmoid & KL & 9.20\small{$\pm$0.04} \\
197	STE+KL & Straight-Through & KL & 9.74\small{$\pm$0.09} \\
198	Gumbel+BCE & Gumbel-sigmoid & BCE & 28.16\small{$\pm$0.17} \\
199	\bottomrule
200	\end{tabular}
201	\end{table}
202	
203	STE+KL (9.74) is slightly worse than Gumbel+KL (9.20, $\Delta = 0.54$) but dramatically better than Gumbel+BCE (28.16).
204	The Gumbel relaxation accounts for only 2.8\% of the total KL advantage over BCE (0.54 out of 18.96 PPL points), confirming that the gradient coupling property of KL---not the relaxation method---drives the quality improvement.
205	
206	% ------------------------------------------------------------
207	\subsection{Iso-Compute Comparison}
208	\label{sec:isocompute}
209	
210	KL requires a full forward pass per step to compute logit targets ($\sim$3.2$\times$ BCE per-step FLOPs).
211	To control for this, we train BCE for 3200 steps (equal total FLOPs), shown in Table~\ref{tab:isocompute}.
212	
213	\begin{table}[t]
214	\centering
215	\small
216	\caption{Iso-compute comparison. Extended BCE training (3.2$\times$ steps) barely closes the gap.}
217	\label{tab:isocompute}
218	\begin{tabular}{lccc}
219	\toprule
220	\textbf{Condition} & \textbf{Steps} & \textbf{Total FLOPs} & \textbf{PPL} \\
221	\midrule
222	KL (Gumbel) & 1000 & 3200$\times$ & 9.20\small{$\pm$0.04} \\
223	BCE (standard) & 1000 & 1000$\times$ & 28.16\small{$\pm$0.17} \\
224	BCE (extended) & 3200 & 3200$\times$ & 25.41\small{$\pm$0.31} \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	Extended BCE training reduces PPL from 28.16 to 25.41 ($-$2.75), but the remaining gap to KL is 16.21 points.
230	BCE's information bottleneck is at the loss function level: more compute cannot overcome a factorized gradient that ignores joint neuron interactions.
231	
232	% ------------------------------------------------------------
233	\subsection{Training-Free Baselines and Quality Hierarchy}
234	\label{sec:baselines}
235	
236	Table~\ref{tab:hierarchy} establishes the three-tier quality hierarchy across all method categories.
237	
238	\begin{table}[t]
239	\centering
240	\small
241	\caption{Quality hierarchy at 50\% sparsity (Llama~3.1~8B, WikiText-2).}
242	\label{tab:hierarchy}
243	\begin{tabular}{llcc}
244	\toprule
245	\textbf{Method} & \textbf{Type} & \textbf{PPL} & \textbf{$\Delta$ Dense} \\
246	\midrule
247	Dense & -- & 6.12 & -- \\
248	TEAL & Training-free & 12.48 & +104\% \\
249	R-Sparse & Training-free & 13.62 & +123\% \\
250	WINA & Training-free & 14.76 & +141\% \\
251	SPON & Static learned & 10.82 & +77\% \\
252	KL-only & Contextual learned & 9.20 & +50\% \\
253	\bottomrule
254	\end{tabular}
255	\end{table}
256	
257	The hierarchy is clean: training-free methods (12.5--14.8 PPL) $<$ static learned (10.82) $<$ contextual learned with KL (9.20).
258	Each tier corresponds to increasing information quality: heuristic scoring $\to$ average-case calibration $\to$ per-input output-distribution optimization.
259	TEAL, the best training-free method, is still 3.28 PPL points worse than KL-only, justifying the overhead of learned prediction.
260	
261	% ------------------------------------------------------------
262	\subsection{SPON Validation}
263	\label{sec:spon}
264	
265	We reimplement SPON on Llama~3.1~8B to serve as the static correction component.
266	Table~\ref{tab:spon} validates correctness via QA benchmarks.
267	
268	\begin{table}[t]
269	\centering
270	\small
271	\caption{SPON reimplementation validation (Llama~3.1~8B, 50\% sparsity).}
272	\label{tab:spon}
273	\begin{tabular}{lccc}
274	\toprule
275	\textbf{Benchmark} & \textbf{Dense} & \textbf{SPON} & $\boldsymbol{\Delta}$ \\
276	\midrule
277	ARC-c & 55.2 & 51.2 & $-$4.0 \\
278	ARC-e & 79.4 & 74.5 & $-$4.9 \\
279	BoolQ & 83.1 & 79.3 & $-$3.8 \\
280	PIQA & 81.3 & 78.1 & $-$3.2 \\
281	WinoGrande & 77.8 & 74.8 & $-$3.0 \\
282	\midrule
283	WikiText-2 PPL & 6.12 & 10.82 & +77\% \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	SPON achieves 10.82 PPL with accuracy drops of 3--5 points, consistent with the original paper's reported ranges.
289	As a static correction, SPON recovers the expected activation drift $\mathbb{E}[\Delta\mathbf{h}]$ but cannot adapt to per-input variation.
290	
291	% ------------------------------------------------------------
292	\subsection{SPON + KL Composition}
293	\label{sec:composition}
294	
295	We test the modular decomposition $\mathbf{c} = \mathbf{c}_s + \mathbf{c}_\theta(\mathbf{x})$ by applying SPON bias correction jointly with the KL predictor.
296	Table~\ref{tab:composition} reports the additivity analysis.
297	
298	\begin{table}[t]
299	\centering
300	\small
301	\caption{Composition additivity analysis. SPON and KL corrections compose near-additively (6.8\% interaction residual in logit space).}
302	\label{tab:composition}
303	\begin{tabular}{lcccc}
304	\toprule
305	\textbf{Component} & \textbf{PPL Recovery} & \textbf{Pred.\ Additive} & \textbf{Actual} & \textbf{Residual} \\
306	\midrule
307	SPON only & 1.68 & -- & -- & -- \\
308	KL only & 3.30 & -- & -- & -- \\
309	SPON+KL & -- & 4.98 & 4.52 & 9.2\% \\
310	\bottomrule
311	\end{tabular}
312	\end{table}
313	
314	SPON alone recovers 1.68 PPL points (from the TEAL baseline), KL alone recovers 3.30, and the combination recovers 4.52---close to the predicted additive 4.98 (9.2\% shortfall in PPL-space, 6.8\% in logit $L_2$ norm).
315	The resulting SPON+KL achieves 7.98$\pm$0.10 PPL, only 30.4\% above dense.
316	
317	Per-layer cosine similarity between SPON and KL corrections confirms approximate orthogonality: mean cosine 0.11, median 0.08, with only 4 of 32 layers exceeding 0.20.
318	This validates the decomposition: SPON corrects the constant drift component, and KL corrects the per-input residual, with minimal interference.
319	
320	% ------------------------------------------------------------
321	\subsection{Full Benchmark Suite}
322	\label{sec:fullbench}
323	
324	Table~\ref{tab:fullbench} presents comprehensive results across perplexity and downstream tasks.
325	
326	\begin{table*}[t]
327	\centering
328	\small
329	\caption{Comprehensive benchmark results (Llama~3.1~8B, 50\% sparsity). KL-only averages only 1.3\% accuracy drop from dense across five tasks; SPON+KL achieves 0.7\%.}
330	\label{tab:fullbench}
331	\begin{tabular}{lcccccccc}
332	\toprule
333	\textbf{Method} & \textbf{Wiki$\downarrow$} & \textbf{C4$\downarrow$} & \textbf{ARC-c$\uparrow$} & \textbf{WinoG$\uparrow$} & \textbf{MMLU$\uparrow$} & \textbf{GSM8K$\uparrow$} & \textbf{HumanE$\uparrow$} & \textbf{Avg $\Delta\downarrow$} \\
334	\midrule
335	Dense & 6.12 & 7.85 & 55.2 & 77.8 & 65.8 & 53.8 & 32.9 & --- \\
336	TEAL & 12.48 & 15.12 & 48.1 & 72.4 & 58.2 & 44.2 & 26.2 & $-$7.8 \\
337	WINA & 14.76 & 17.88 & 46.3 & 70.8 & 56.4 & 41.8 & 24.4 & $-$9.9 \\
338	R-Sparse & 13.62 & 16.31 & 47.2 & 71.5 & 57.1 & 43.1 & 25.6 & $-$8.8 \\
339	SPON & 10.82 & 13.24 & 51.2 & 74.8 & 60.3 & 46.5 & 28.1 & $-$5.3 \\
340	BCE+comp & 18.64 & 22.15 & 44.8 & 68.3 & 54.9 & 39.7 & 23.8 & $-$12.8 \\
341	KL-only & 9.20 & 11.38 & 54.3 & 76.9 & 65.0 & 52.8 & 32.3 & $-$1.3 \\
342	SPON+KL & 7.98 & 9.81 & 54.8 & 77.2 & 65.4 & 53.2 & 32.5 & $-$0.7 \\
343	\bottomrule
344	\end{tabular}
345	\end{table*}
346	
347	KL-only's low perplexity (9.20 WikiText-2, 11.38 C4) transfers directly to downstream accuracy: the average drop across five tasks is only 1.3\%, compared to 12.8\% for BCE+compensation.
348	Tasks requiring precise multi-step reasoning (GSM8K, HumanEval) show the largest relative advantage for KL---BCE+compensation drops 26--28\% from dense on these tasks, while KL-only drops less than 2\%.
349	SPON+KL further closes the gap to 0.7\% average drop.
350	
351	\paragraph{Inference efficiency.}
352	Table~\ref{tab:latency} presents the latency--quality Pareto analysis.
353	
354	\begin{table}[t]
355	\centering
356	\small
357	\caption{Inference efficiency comparison. KL-only Pareto-dominates BCE+comp on all axes.}
358	\label{tab:latency}
359	\begin{tabular}{lcccc}
360	\toprule
361	\textbf{Method} & \textbf{ms/tok} & \textbf{Speedup} & \textbf{Extra MB} & \textbf{PPL} \\
362	\midrule
363	Dense & 16.8 & 1.00$\times$ & 0 & 6.12 \\
364	TEAL & 11.2 & 1.50$\times$ & 0 & 12.48 \\
365	SPON & 10.9 & 1.54$\times$ & 1 & 10.82 \\
366	KL-only & 12.0 & 1.40$\times$ & 24 & 9.20 \\
367	BCE+comp & 13.8 & 1.22$\times$ & 280 & 18.64 \\
368	SPON+KL & 12.1 & 1.39$\times$ & 25 & 7.98 \\
369	\bottomrule
370	\end{tabular}
371	\end{table}
372	
373	KL-only strictly Pareto-dominates BCE+compensation: better quality (9.20 vs.\ 18.64 PPL), lower latency (12.0 vs.\ 13.8\,ms/token), and 10$\times$ fewer additional parameters (24 vs.\ 280\,MB).
374	The 1.8\,ms/token savings come from eliminating the per-layer compensation GEMV.
375	SPON+KL adds only 0.1\,ms (bias addition is nearly free) while further improving quality to 7.98 PPL.
376	
377	% ------------------------------------------------------------
378	\subsection{Quadratic Scaling of KL--BCE Gap}
379	\label{sec:scaling}
380	
381	We train KL-only and BCE-only at seven sparsity levels (30--60\%) with single seeds.
382	Table~\ref{tab:sweep} reports the results and fit statistics.
383	
384	\begin{table}[t]
385	\centering
386	\small
387	\caption{Sparsity sweep: KL--BCE quality gap $\Delta$ follows $as^2$ with $R^2 = 0.97$.}
388	\label{tab:sweep}
389	\begin{tabular}{ccccccc}
390	\toprule
391	$s$ & $s^2$ & \textbf{KL} & \textbf{BCE} & $\boldsymbol{\Delta}$ & \textbf{Pred.}\ $as^2$ & \textbf{Taylor \%} \\
392	\midrule
393	0.30 & 0.09 & 7.05 & 14.55 & 7.50 & 7.13 & 96.8 \\
394	0.35 & 0.12 & 7.42 & 17.82 & 10.40 & 9.70 & 95.4 \\
395	0.40 & 0.16 & 7.98 & 19.98 & 12.00 & 12.67 & 94.1 \\
396	0.45 & 0.20 & 8.51 & 24.71 & 16.20 & 16.03 & 92.5 \\
397	0.50 & 0.25 & 9.20 & 28.20 & 19.00 & 19.80 & 89.8 \\
398	0.55 & 0.30 & 10.82 & 33.62 & 22.80 & 23.96 & 85.6 \\
399	0.60 & 0.36 & 13.15 & 42.65 & 29.50 & 28.51 & 80.2 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{Scaling fit statistics for $\Delta_{\mathrm{BCE-KL}}(s)$.}
408	\label{tab:fitstat}
409	\begin{tabular}{lcc}
410	\toprule
411	\textbf{Model} & $\boldsymbol{R^2}$ & \textbf{Parameters} \\
412	\midrule
413	$\Delta = as^2$ & 0.97 & $a = 79.2$ \\
414	$\Delta = as^2 + bs$ & 0.99 & $a = 68.1, b = 5.8$ \\
415	$\Delta = as^2 + bs + c$ & 0.99 & $a = 65.3, b = 7.2, c = -0.4$ \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	The pure quadratic model $\Delta = as^2$ achieves $R^2 = 0.97$, confirming that pairwise neuron interactions dominate the KL--BCE gap.
421	Adding a linear term yields $R^2 = 0.99$, consistent with the theoretical expectation that lower-order corrections (single-neuron boundary effects) provide a minor residual.
422	The Taylor expansion accuracy degrades gracefully from 96.8\% at $s = 0.30$ to 80.2\% at $s = 0.60$, as expected when higher-order ($s^3$) interaction terms become non-negligible at extreme sparsity.
423	
424	This provides a \emph{testable, non-trivial} prediction beyond our data: the KL advantage will accelerate at sparsity levels above 60\%, while new developments in BCE-based training (e.g., auxiliary losses) would need to address the fundamental factorization bottleneck to change the scaling law.
425	
426	% ------------------------------------------------------------
427	\subsection{Cross-Architecture Validation}
428	\label{sec:crossarch}
429	
430	We replicate the KL-only vs.\ BCE+compensation comparison on Mistral-7B-v0.3, which uses GQA with sliding window attention---a different attention architecture from Llama's standard GQA.
431	
432	\begin{table}[t]
433	\centering
434	\small
435	\caption{Cross-architecture validation on Mistral-7B-v0.3 (50\% sparsity).}
436	\label{tab:mistral}
437	\begin{tabular}{lccc}
438	\toprule
439	\textbf{Condition} & \textbf{Wiki PPL$\downarrow$} & \textbf{ARC-c$\uparrow$} & \textbf{MMLU$\uparrow$} \\
440	\midrule
441	Dense & 5.48 & 58.1 & 62.8 \\
442	KL-only & 8.22\small{$\pm$0.10} & 56.4 & 61.3 \\
443	BCE+comp & 12.86\small{$\pm$0.29} & 50.8 & 55.9 \\
444	\midrule
445	Gap (KL vs BCE+comp) & $-$4.64 & +5.6 & +5.4 \\
446	\bottomrule
447	\end{tabular}
448	\end{table}
449	
450	KL dominance replicates cleanly: 8.22 vs.\ 12.86 PPL (36\% gap).
451	The KL PPL increase over dense is 50.0\%, strikingly consistent with Llama's 50.3\%.
452	This consistency across architectures confirms that the advantage is a \emph{universal property of the loss function}, not an architecture-specific artifact.
453	The absolute gap is smaller than on Llama (4.64 vs.\ 9.44 PPL) because Mistral's lower dense baseline (5.48 vs.\ 6.12) and sliding window attention may yield somewhat more localized neuron importance patterns, reducing but not eliminating the interaction effects that BCE misses.
454	
455	% ------------------------------------------------------------
456	\subsection{Long-Context Evaluation (LongBench)}
457	\label{sec:longbench}
458	
459	Table~\ref{tab:longbench} evaluates on LongBench (English subset, 4K--32K tokens) with per-task-type breakdown.
460	
461	\begin{table}[t]
462	\centering
463	\small
464	\caption{LongBench per-task-type results (Llama~3.1~8B, 50\% sparsity).}
465	\label{tab:longbench}
466	\begin{tabular}{lcccccc}
467	\toprule
468	\textbf{Task} & \textbf{Dense} & \textbf{TEAL} & \textbf{SPON} & \textbf{BCE+c} & \textbf{KL} & \textbf{S+KL} \\
469	\midrule
470	Single-doc QA & 46.2 & 38.1 & 42.0 & 35.2 & 44.8 & 45.3 \\
471	Multi-doc QA & 39.5 & 31.2 & 36.1 & 28.4 & 38.2 & 38.8 \\
472	Summarization & 43.8 & 35.8 & 40.2 & 33.8 & 42.5 & 43.1 \\
473	Few-shot & 48.3 & 39.5 & 44.3 & 34.6 & 47.1 & 47.8 \\
474	Code & 39.6 & 32.4 & 36.5 & 28.5 & 38.0 & 38.9 \\
475	\midrule
476	\textbf{Average} & \textbf{43.5} & \textbf{35.4} & \textbf{39.8} & \textbf{32.1} & \textbf{42.1} & \textbf{42.8} \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	KL-only (42.1 average) closely matches dense (43.5, drop 1.4), while BCE+compensation degrades further (32.1, drop 11.4).
482	The KL predictor generalizes well to long contexts despite being trained on short sequences, since it operates on per-token hidden states rather than sequence-level features.
483	Multi-doc QA shows the largest KL drop ($-$3.3), consistent with its requirement for cross-document reasoning---the most challenging setting for any approximation.
484	
485	% ------------------------------------------------------------
486	\subsection{MT-Bench Multi-Turn Evaluation}
487	\label{sec:mtbench}
488	
489	Table~\ref{tab:mtbench} reports GPT-4o-judged MT-Bench scores across 80 multi-turn prompts.
490	
491	\begin{table}[t]
492	\centering
493	\small
494	\caption{MT-Bench results (GPT-4o judge). KL-only is within judge noise of dense.}
495	\label{tab:mtbench}
496	\begin{tabular}{lccccc}
497	\toprule
498	\textbf{Method} & \textbf{Avg} & \textbf{Writing} & \textbf{Reason.} & \textbf{Math} & \textbf{Coding} \\
499	\midrule
500	Dense & 7.21 & 7.50 & 6.85 & 6.80 & 7.10 \\
501	TEAL & 6.18 & 6.45 & 5.60 & 5.40 & 5.80 \\
502	SPON & 6.78 & 7.10 & 6.35 & 6.15 & 6.55 \\
503	BCE+comp & 6.42 & 6.80 & 5.85 & 5.65 & 5.90 \\
504	KL-only & 7.05 & 7.35 & 6.65 & 6.55 & 6.85 \\
505	SPON+KL & 7.12 & 7.40 & 6.75 & 6.65 & 6.95 \\
506	\bottomrule
507	\end{tabular}
508	\end{table}
509	
510	KL-only (7.05) is within 0.16 of dense (7.21)---within the GPT-4o judge's scoring noise floor.
511	BCE+compensation (6.42) shows severe degradation on reasoning ($-$1.00) and math ($-$1.15), tasks most sensitive to output distribution fidelity.
512	SPON+KL (7.12) nearly recovers dense-level performance across all categories.
513	
514	% ------------------------------------------------------------
515	\subsection{RULER Synthetic Diagnostics}
516	\label{sec:ruler}
517	
518	Table~\ref{tab:ruler} provides fine-grained diagnostics on RULER synthetic tasks at 4K and 16K contexts.
519	
520	\begin{table}[t]
521	\centering
522	\small
523	\caption{RULER synthetic evaluation at 4K and 16K context lengths.}
524	\label{tab:ruler}
525	\begin{tabular}{llcccc}
526	\toprule
527	\textbf{Task} & \textbf{Ctx} & \textbf{Dense} & \textbf{KL} & \textbf{BCE+c} & \textbf{S+KL} \\
528	\midrule
529	Needle & 4K & 99.2 & 98.0 & 94.5 & 98.5 \\
530	Needle & 16K & 96.8 & 94.5 & 86.2 & 95.8 \\
531	Multi-key & 4K & 93.5 & 91.2 & 83.8 & 92.4 \\
532	Multi-key & 16K & 84.1 & 82.4 & 72.1 & 83.5 \\
533	Var-track & 4K & 92.8 & 92.1 & 83.9 & 92.5 \\
534	Var-track & 16K & 84.5 & 81.3 & 76.5 & 83.2 \\
535	\midrule
536	\textbf{Average} & \textbf{4K} & \textbf{95.2} & \textbf{93.8} & \textbf{87.4} & \textbf{94.5} \\
537	\textbf{Average} & \textbf{16K} & \textbf{88.5} & \textbf{86.1} & \textbf{78.3} & \textbf{87.2} \\
538	\bottomrule
539	\end{tabular}
540	\end{table}
541	
542	KL-only's context-length degradation pattern (4K$\to$16K: $-$7.7) closely tracks dense ($-$6.7), while BCE+compensation degrades more steeply ($-$9.1).
543	Multi-key retrieval shows the largest differentiation at 16K (KL 82.4 vs.\ BCE+comp 72.1), consistent with this task's sensitivity to joint neuron interactions---simultaneous retrieval of multiple scattered facts requires precise FFN activation patterns.
544	
545	% ============================================================
546	\section{Discussion}
547	
548	\paragraph{Two-dimensional taxonomy.}
549	Our results populate a two-axis taxonomy of sparsity correction methods: \emph{correction granularity} (static $\to$ per-layer $\to$ per-token) $\times$ \emph{training signal coupling} (decomposed/BCE $\to$ intermediate/MSE $\to$ coupled/KL).
550	Prior work fills specific cells---SPON (static, KL), ShadowLLM (per-layer, MSE), FastForward (per-token, BCE)---while our KL-only method fills the (per-token, KL) cell, which proves to be the Pareto-optimal configuration.
551	
552	\paragraph{Practical implications.}
553	Eliminating compensation networks simplifies the inference pipeline: no additional parameters to load, no per-layer GEMV, and a smaller memory footprint.
554	For Llama~3.1~8B, this means 256\,MB fewer parameters and 1.8\,ms/token lower latency, with strictly better quality.
555	The SPON+KL variant adds only 1\,MB (static biases) for a further 1.22 PPL improvement.
556	
557	\paragraph{Limitations.}
558	We evaluate on 7--8B parameter models; scaling behavior at 70B+ remains to be verified.
559	The quadratic scaling prediction is confirmed over $s \in [0.3, 0.6]$ but extrapolation beyond 60\% needs additional data.
560	KL training requires a teacher forward pass per step ($3.2\times$ per-step cost), though the total training time is modest (4.2 hours on a single GPU for 1000 steps).
561	
562	% ============================================================
563	\section{Conclusion}
564	
565	We have shown that output-distribution distillation via KL divergence categorically dominates BCE-based training for contextual activation sparsity prediction in SwiGLU LLMs, eliminating the need for compensation networks.
566	The advantage traces to a fundamental difference in gradient structure: KL's coupled gradients capture joint neuron interactions that BCE's factorized gradients miss, with the quality gap scaling quadratically in sparsity ($R^2 = 0.97$).
567	The resulting method is simultaneously simpler (no compensation network), smaller (24\,MB vs.\ 280\,MB), faster (12.0 vs.\ 13.8\,ms/token), and better (9.20 vs.\ 18.64 PPL) than the BCE+compensation alternative.
568	Combined with SPON's static bias correction, the modular decomposition achieves 7.98 PPL---within 30\% of dense---with near-perfect additivity.
569	
570	% ============================================================
571	\bibliography{custom}
572	
573	\begin{thebibliography}{20}
574	
575	\bibitem[Shazeer, 2020]{shazeer2020glu}
576	Noam Shazeer. 2020.
577	\newblock {GLU} Variants Improve Transformer.
578	\newblock {\em arXiv preprint arXiv:2002.05202}.
579	
580	\bibitem[Liu et~al., 2024]{liu2024teal}
581	Yixin Liu, Haotian Ye, Lei Li, and Hao Peng. 2024.
582	\newblock {TEAL}: Token-wise Efficient Activation sparsity for {LLM}s.
583	\newblock In {\em Proceedings of NeurIPS}.
584	
585	\bibitem[Shen et~al., 2024]{shen2024wina}
586	Zhihang Shen, et~al. 2024.
587	\newblock {WINA}: Weight-Informed Neuron Activation for accelerating large language model inference.
588	\newblock {\em arXiv preprint arXiv:2410.xxxx}.
589	
590	\bibitem[Zhang et~al., 2024]{zhang2024rsparse}
591	Tianyu Zhang, et~al. 2024.
592	\newblock {R-Sparse}: Rank-Aware Activation Sparsity for efficient {LLM} inference.
593	\newblock {\em arXiv preprint arXiv:2410.xxxx}.
594	
595	\bibitem[Wang et~al., 2024]{wang2024fastforward}
596	Tao Wang, et~al. 2024.
597	\newblock {FastForward}: Learned sparsity prediction with compensation for efficient {LLM} inference.
598	\newblock {\em arXiv preprint arXiv:2405.xxxx}.
599	
600	\bibitem[Zhou et~al., 2024]{zhou2024spon}
601	Yongqi Zhou, et~al. 2024.
602	\newblock {SPON}: Static-correction-based sparsity optimization for language models via {KL} distillation.
603	\newblock {\em arXiv preprint arXiv:2406.xxxx}.
604	
605	\bibitem[Chen et~al., 2024]{chen2024shadowllm}
606	Zheng Chen, et~al. 2024.
607	\newblock {ShadowLLM}: Predictor-based contextual sparsity for large language models.
608	\newblock {\em arXiv preprint arXiv:2406.xxxx}.
609	
610	\bibitem[Hinton et~al., 2015]{hinton2015distilling}
611	Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.
612	\newblock Distilling the Knowledge in a Neural Network.
613	\newblock {\em arXiv preprint arXiv:1503.02531}.
614	
615	\end{thebibliography}
616	
617	\end{document}
618	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b85e8f3-d363-45d3-a7be-45a506e6835c",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "b634e36f-e616-4077-9234-741410273498",
  "sourceToolAssistantUUID": "9b85e8f3-d363-45d3-a7be-45a506e6835c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T17:54:01.654Z_

Now let me also read the "median" and "worst" scenario papers for comparison, and look at any experiment plans.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b634e36f-e616-4077-9234-741410273498",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nLt5psSXGnRnnFc8g6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18444602-915b-46c0-9d3e-f20fd7249e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aRTKTQmttgnPi9BA8SGcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14069,
      "cache_read_input_tokens": 31162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14069,
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

_source line 28 · 2026-05-15T17:54:04.012Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AZpNyu1xNtztQCYDJaY2h8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18444602-915b-46c0-9d3e-f20fd7249e48",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nLt5psSXGnRnnFc8g6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37d0353d-236a-4db7-9290-ea0f61898a72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aRTKTQmttgnPi9BA8SGcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14069,
      "cache_read_input_tokens": 31162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14069,
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

_source line 29 · 2026-05-15T17:54:04.378Z_

<details><summary>↩ Tool result · `toolu_01AZpNyu1xNtztQCYDJaY2h8`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{hyperref}
11	\usepackage{natbib}
12	\usepackage{array}
13	\usepackage{tabularx}
14	
15	\newcommand{\method}{KL-Sparse}
16	
17	\title{Output-Distribution Distillation Eliminates Compensation Overhead\\for Contextual SwiGLU Sparsity Prediction}
18	
19	\author{
20	  Anonymous Authors
21	}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ===========================================================================
28	\begin{abstract}
29	Activation sparsity in SwiGLU-based large language models enables significant inference speedups through dynamic neuron pruning, but existing approaches face a quality--efficiency trade-off: training-free heuristics leave large quality gaps, while learned BCE-trained predictors require auxiliary compensation networks adding ${\sim}$256\,MB of parameters and per-layer GEMV overhead. We present a systematic study of training signal and correction granularity for contextual sparsity prediction, organized around a two-dimensional taxonomy (loss coupling $\times$ correction granularity). Our key finding is that a KL-divergence-trained contextual predictor achieves \textbf{9.53 perplexity} on WikiText-2 at 50\% model-level sparsity on Llama~3.1~8B---surpassing BCE+compensation (11.56) while eliminating compensation parameters entirely. This result reframes the role of compensation: output-distribution distillation during predictor training preempts the errors that compensation networks correct post-hoc. We further show that static bias correction (SPON) and contextual KL prediction compose with partial additivity (22\% interaction residual), and that the KL advantage over BCE grows super-linearly with sparsity. Across seven benchmarks, two model families, and long-context evaluations, KL-trained prediction achieves 1.49$\times$ batch-32 speedup with only 3.4\% average accuracy drop and 8\,MB overhead.
30	\end{abstract}
31	
32	% ===========================================================================
33	\section{Introduction}
34	
35	SwiGLU feed-forward networks in modern LLMs exhibit substantial contextual activation sparsity: at any given token, 40--60\% of intermediate neurons contribute negligibly to the output. Exploiting this sparsity at inference time promises significant speedups without architectural modification. However, realizing this promise requires solving the \emph{sparsity prediction problem}: determining which neurons to prune for each input.
36	
37	Existing approaches span a spectrum. \textbf{Training-free methods} (TEAL, WINA, R-Sparse) use magnitude-based heuristics with zero training cost, but leave a 6--8 PPL gap at 50\% sparsity. \textbf{Static learned corrections} (SPON) train per-layer bias vectors via KL distillation to compensate average activation drift, achieving zero inference overhead but limited by input-independence. \textbf{Contextual learned predictors} (FastForward) train per-token predictors with BCE loss against binarized activation masks, achieving near-dense quality but requiring auxiliary compensation MLPs (${\sim}$256\,MB) to correct prediction errors---adding parameters and per-layer GEMV operations that partially negate sparsity benefits.
38	
39	A fundamental question remains unexplored: \emph{does the choice of training signal for the contextual predictor determine whether compensation is necessary?} We observe that the gradient structures of BCE and KL losses differ qualitatively. The BCE gradient $\partial \mathcal{L}_{\text{BCE}}/\partial s_j$ depends only on neuron $j$'s activation---a factorized, per-neuron signal. In contrast, the KL gradient $\partial \mathcal{L}_{\text{KL}}/\partial s_j$ couples all active neurons through $\partial \text{logits}/\partial \mathbf{h} \cdot \partial \mathbf{h}/\partial \mathbf{m}$, propagating output-distribution-level supervision to each masking decision. This coupling allows KL-trained predictors to optimize joint neuron selection, capturing interaction effects that BCE structurally misses.
40	
41	We organize prior work and our contributions in a two-dimensional taxonomy crossing \emph{training signal coupling} (decomposed/BCE $\rightarrow$ coupled/KL) with \emph{correction granularity} (static $\rightarrow$ per-token contextual), revealing an unexplored cell: per-token contextual prediction trained with coupled KL supervision.
42	
43	\paragraph{Contributions.}
44	\begin{enumerate}
45	\item \textbf{KL eliminates compensation overhead at quality parity.} At 50\% sparsity, KL-only prediction (PPL 9.53) surpasses BCE+compensation (PPL 11.56) while requiring zero compensation parameters, yielding a simpler and more efficient inference pipeline (1.49$\times$ vs.\ 1.18$\times$ speedup at batch 32, 8\,MB vs.\ 264\,MB overhead).
46	\item \textbf{Empirically observed partial additivity of correction mechanisms.} SPON (static) and KL (contextual) corrections compose to achieve the best overall quality (PPL 8.91), with a 22\% interaction residual honestly characterizing their overlap.
47	\item \textbf{Taxonomy and systematic ablation as methodological contribution.} Our two-dimensional taxonomy, four-condition ablation, iso-compute comparison, and STE baseline provide a rigorous framework for understanding sparsity prediction design choices.
48	\end{enumerate}
49	
50	
51	% ===========================================================================
52	\section{Background and Related Work}
53	
54	\paragraph{Activation sparsity in SwiGLU LLMs.}
55	The SwiGLU activation $\text{SwiGLU}(\mathbf{x}) = (\mathbf{x}\mathbf{W}_1 \odot \sigma(\mathbf{x}\mathbf{W}_g)) \mathbf{W}_2$ produces naturally sparse intermediate representations, as the sigmoid gate $\sigma(\mathbf{x}\mathbf{W}_g)$ drives many neurons toward zero. This contextual sparsity can be exploited by skipping near-zero neurons during inference, reducing FLOPs proportionally.
56	
57	\paragraph{Training-free methods.}
58	TEAL combines activation magnitude with greedy per-layer sparsity allocation. WINA uses weight-informed neuron scoring. R-Sparse incorporates rank-aware redundancy information. These methods require no training but achieve suboptimal quality at high sparsity levels.
59	
60	\paragraph{Static learned corrections.}
61	SPON trains per-layer bias vectors using KL divergence to correct average activation drift from pruning. The bias vectors add negligible parameters (${\sim}$0.5\,MB) and zero inference latency (fused into existing computations), but cannot adapt to per-input neuron importance variations.
62	
63	\paragraph{Contextual learned predictors.}
64	FastForward trains lightweight MLPs to predict per-token neuron importance using BCE loss against binarized activation targets, augmented with compensation networks that correct residual errors in the sparse hidden states. The compensation adds ${\sim}$256\,MB of parameters and per-layer GEMV operations.
65	
66	\paragraph{Two-dimensional taxonomy.}
67	We organize these approaches along two axes (Table~\ref{tab:taxonomy}): \emph{training signal coupling} (how much inter-neuron information the loss gradient carries) and \emph{correction granularity} (whether correction is input-independent or per-token). This taxonomy reveals that no prior work combines per-token contextual prediction with coupled KL training.
68	
69	\begin{table}[t]
70	\centering
71	\caption{Taxonomy of sparsity prediction methods. Our work fills the previously empty per-token contextual + coupled KL cell.}
72	\label{tab:taxonomy}
73	\small
74	\begin{tabular}{lccc}
75	\toprule
76	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
77	\midrule
78	Static & --- & --- & SPON \\
79	Per-layer & --- & ShadowLLM & --- \\
80	Per-token contextual & FastForward & --- & \textbf{Ours} \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	
86	% ===========================================================================
87	\section{Method}
88	
89	\subsection{Problem Formulation}
90	
91	Given a pretrained SwiGLU LLM, we train a lightweight predictor $f_\theta$ that, for each input token, produces a binary mask $\mathbf{m} \in \{0,1\}^D$ selecting which of the $D$ intermediate neurons to activate. The mask is applied element-wise: $\tilde{\mathbf{h}} = \mathbf{m} \odot \mathbf{h}$, where $\mathbf{h}$ is the dense intermediate representation.
92	
93	\subsection{Training Signal: KL Divergence}
94	
95	We train the predictor by minimizing the KL divergence between the output distributions of the dense and sparse models:
96	\begin{equation}
97	\mathcal{L}_{\text{KL}} = \text{KL}\!\left(p_{\text{dense}}(\cdot \mid x) \;\|\; p_{\text{sparse}}(\cdot \mid x; \theta)\right)
98	\end{equation}
99	where $p_{\text{sparse}}$ denotes the model's output distribution when neurons are masked according to $f_\theta(x)$.
100	
101	\paragraph{Gradient coupling.} The key property distinguishing KL from BCE training is gradient structure. For the BCE loss, $\partial \mathcal{L}_{\text{BCE}} / \partial s_j$ depends only on whether neuron $j$'s predicted importance matches its binarized target---a factorized signal. For the KL loss:
102	\begin{equation}
103	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \text{logits}} \cdot \frac{\partial \text{logits}}{\partial \mathbf{h}} \cdot \frac{\partial \mathbf{h}}{\partial m_j} \cdot \frac{\partial m_j}{\partial s_j}
104	\end{equation}
105	The chain through $\partial \text{logits}/\partial \mathbf{h}$ couples all neurons: whether neuron $j$ should be active depends on which \emph{other} neurons are active, because their joint contribution determines the output distribution. This coupling is a mathematical property of the gradient, not an analogy.
106	
107	\subsection{Gumbel-Sigmoid Relaxation}
108	
109	To enable gradient-based optimization of discrete masks, we use Gumbel-sigmoid relaxation during training:
110	\begin{equation}
111	\tilde{m}_j = \sigma\!\left(\frac{s_j + g_1 - g_2}{\tau}\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1)
112	\end{equation}
113	where $s_j = f_\theta(x)_j$ is the predictor's logit for neuron $j$ and $\tau$ is the temperature. At inference, we use hard thresholding: $m_j = \mathbf{1}[s_j > 0]$.
114	
115	\subsection{Composition with Static Correction}
116	
117	We also explore composing the contextual KL predictor with SPON's static bias correction. SPON learns per-layer bias vectors $\mathbf{b}_l$ to correct average activation drift:
118	\begin{equation}
119	\tilde{\mathbf{h}}_l = \mathbf{m}_l \odot \mathbf{h}_l + \mathbf{b}_l
120	\end{equation}
121	The composition applies both the contextual mask (from KL predictor) and the static correction (from SPON), yielding $c = c_s + c_\theta(x)$ where $c_s$ addresses systematic drift and $c_\theta(x)$ adapts to per-input neuron importance.
122	
123	
124	% ===========================================================================
125	\section{Experiments}
126	
127	All experiments use 50\% model-level sparsity unless otherwise noted. Our primary model is Llama~3.1~8B; we validate on Mistral-7B-v0.3. All learned methods are trained on a calibration set of 128 sequences (2048 tokens each) from C4. We report WikiText-2 perplexity as the primary metric, supplemented by downstream benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), long-context evaluations (LongBench, RULER), and instruction-following quality (MT-Bench with GPT-4o judge).
128	
129	% ---------------------------------------------------------------------------
130	\subsection{Training-Free Baselines}
131	\label{sec:baselines}
132	
133	Table~\ref{tab:baselines} establishes the performance of training-free methods, motivating the need for learned predictors.
134	
135	\begin{table}[t]
136	\centering
137	\caption{Training-free baselines at 50\% model-level sparsity (Llama 3.1 8B).}
138	\label{tab:baselines}
139	\small
140	\begin{tabular}{lccr}
141	\toprule
142	Method & WikiText-2 PPL ($\downarrow$) & $\Delta$ vs Dense & Training Cost \\
143	\midrule
144	Dense & 6.12 & --- & --- \\
145	TEAL & 12.50 & +6.38 & 0 \\
146	R-Sparse & 13.50 & +7.38 & 0 \\
147	WINA & 14.20 & +8.08 & 0 \\
148	\midrule
149	KL-only (ref.) & 9.53 & +3.41 & 3.8\,h \\
150	\bottomrule
151	\end{tabular}
152	\end{table}
153	
154	Training-free heuristics leave a 6--8 PPL gap versus the dense model. TEAL is the strongest baseline (12.50) owing to its greedy per-layer allocation, but all three methods substantially underperform learned predictors, establishing a clear hierarchy: training-free (12.5--14.2) $\rightarrow$ static-learned (11.2) $\rightarrow$ contextual-learned (9.5).
155	
156	
157	% ---------------------------------------------------------------------------
158	\subsection{Four-Condition Ablation: Loss $\times$ Compensation}
159	\label{sec:ablation}
160	
161	Our central experiment crosses two factors: training loss (BCE vs.\ KL) and compensation (present vs.\ absent), yielding four conditions (Table~\ref{tab:four_cond}).
162	
163	\begin{table}[t]
164	\centering
165	\caption{Four-condition ablation at 50\% model-level sparsity (Llama 3.1 8B). KL-only achieves better quality than BCE+compensation while requiring zero compensation parameters.}
166	\label{tab:four_cond}
167	\small
168	\begin{tabular}{lcccc}
169	\toprule
170	Condition & WikiText-2 PPL ($\downarrow$) & Seeds & Comp.\ Params & Pipeline \\
171	\midrule
172	Dense (reference) & 6.12 & --- & --- & --- \\
173	BCE-only & 28.16 $\pm$ 0.21 & 3 & 0 & Simple \\
174	BCE + compensation & 11.56 $\pm$ 0.61 & 5 & 256\,MB & Complex \\
175	KL-only & 9.53 $\pm$ 0.41 & 5 & 0 & Simple \\
176	KL + compensation & 9.05 $\pm$ 0.15 & 3 & 256\,MB & Complex \\
177	\bottomrule
178	\end{tabular}
179	\end{table}
180	
181	KL-only (9.53) outperforms BCE+compensation (11.56) by 2.03 PPL while requiring zero compensation overhead. Adding compensation to KL yields only a marginal improvement (9.53 $\rightarrow$ 9.05, $\Delta$ = 0.48), indicating that KL training preemptively addresses the errors compensation is designed to correct. In contrast, compensation is essential for BCE (28.16 $\rightarrow$ 11.56, $\Delta$ = 16.60), confirming that BCE's factorized gradient leaves substantial joint-interaction errors that require post-hoc correction.
182	
183	% ---------------------------------------------------------------------------
184	\subsection{Isolating Loss vs.\ Relaxation: STE Baseline}
185	\label{sec:ste}
186	
187	To disentangle the contributions of the KL loss function and the Gumbel-sigmoid relaxation, we train a predictor with KL loss but using the Straight-Through Estimator (STE) instead of Gumbel-sigmoid (Table~\ref{tab:ste}).
188	
189	\begin{table}[t]
190	\centering
191	\caption{Loss function vs.\ relaxation method ablation. KL contributes 72\% of the total gain over BCE-only; Gumbel-sigmoid contributes 28\%.}
192	\label{tab:ste}
193	\small
194	\begin{tabular}{llccc}
195	\toprule
196	Condition & Loss & Relaxation & WikiText-2 PPL & Gain over BCE-only \\
197	\midrule
198	BCE-only & BCE & STE & 28.16 & --- \\
199	KL + STE & KL & STE & 14.70 $\pm$ 0.60 & 13.46 (72\%) \\
200	KL + Gumbel & KL & Gumbel-$\sigma$ & 9.53 $\pm$ 0.41 & 18.63 (100\%) \\
201	\bottomrule
202	\end{tabular}
203	\end{table}
204	
205	KL + STE (14.70) already substantially outperforms BCE-only (28.16), confirming that the KL loss function---not the relaxation method---is the primary driver of improvement (72\% of total gain). Gumbel-sigmoid contributes a meaningful additional 28\%, as its smooth gradients enable finer-grained mask optimization at decision boundaries. Both components are necessary for optimal performance.
206	
207	% ---------------------------------------------------------------------------
208	\subsection{Iso-Compute Comparison}
209	\label{sec:isocompute}
210	
211	KL training requires a dense forward pass per step (66.0 TFLOPs/step) while BCE uses cached targets (0.8 TFLOPs/step). To ensure KL's advantage is not simply a compute artifact, we extend BCE training to 33{,}000 steps to match KL's total GPU-hours (Table~\ref{tab:isocompute}).
212	
213	\begin{table}[t]
214	\centering
215	\caption{Iso-compute comparison. Even with equivalent total compute, BCE trails KL by ${\sim}$14 PPL.}
216	\label{tab:isocompute}
217	\small
218	\begin{tabular}{lcccr}
219	\toprule
220	Condition & Per-step TFLOPs & Total Steps & GPU-hours & WikiText-2 PPL \\
221	\midrule
222	KL + Gumbel & 66.0 & 1{,}000 & 3.8 & 9.53 $\pm$ 0.41 \\
223	BCE (standard) & 0.8 & 1{,}000 & 0.4 & 28.16 $\pm$ 0.21 \\
224	BCE (iso-compute) & 0.8 & 33{,}000 & 3.8 & 23.50 $\pm$ 0.70 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	Extended BCE training reduces PPL from 28.16 to 23.50---a meaningful but insufficient improvement. The 14 PPL gap versus KL persists, confirming that BCE's information bottleneck lies in the factorized loss structure, not the training budget. Additional BCE steps improve predictor generalization but cannot capture joint neuron interactions that the loss function structurally excludes.
230	
231	% ---------------------------------------------------------------------------
232	\subsection{SPON Reproduction and Composition}
233	\label{sec:composition}
234	
235	\paragraph{SPON reproduction.}
236	We reimplement SPON (learnable per-layer bias vectors + KL training) on Llama~3.1~8B and verify reproduction against published results (Table~\ref{tab:spon_repro}). Our reproduction achieves WikiText-2 PPL of 11.20, within the expected range, with QA benchmark deltas within $\pm$1.2\% of published values.
237	
238	\begin{table}[t]
239	\centering
240	\caption{SPON reproduction on Llama 3.1 8B---QA benchmark comparison at 50\% sparsity.}
241	\label{tab:spon_repro}
242	\small
243	\begin{tabular}{lccr}
244	\toprule
245	Benchmark & Dense & SPON (ours) & $\Delta$ vs.\ published \\
246	\midrule
247	ARC-c & 53.4\% & 49.5\% & +1.2\% \\
248	ARC-e & 81.2\% & 75.8\% & $-$0.5\% \\
249	BoolQ & 83.5\% & 78.2\% & +0.8\% \\
250	PIQA & 81.0\% & 77.5\% & $-$1.0\% \\
251	WinoGrande & 74.2\% & 69.8\% & +0.6\% \\
252	\midrule
253	WikiText-2 PPL & 6.12 & 11.20 & --- \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	\paragraph{Composition analysis.}
259	We combine SPON's static bias correction with our KL contextual predictor (Table~\ref{tab:composition}). The composition achieves 8.91 PPL---the best overall result---but with a 22\% interaction residual relative to a hypothetical fully additive prediction (8.23).
260	
261	\begin{table}[t]
262	\centering
263	\caption{Composition additivity analysis. SPON and KL corrections compose with partial additivity; the 22\% interaction residual reflects overlap in what each mechanism corrects.}
264	\label{tab:composition}
265	\small
266	\begin{tabular}{lcr}
267	\toprule
268	Condition & WikiText-2 PPL & $\Delta$ from TEAL \\
269	\midrule
270	TEAL (no learned correction) & 12.50 & --- \\
271	SPON only & 11.20 & $-$1.30 \\
272	KL-only & 9.53 & $-$2.97 \\
273	SPON + KL (if fully additive) & 8.23 & $-$4.27 \\
274	SPON + KL (actual) & 8.91 $\pm$ 0.14 & $-$3.59 \\
275	\midrule
276	Interaction residual & --- & 0.68 (22\%) \\
277	\bottomrule
278	\end{tabular}
279	\end{table}
280	
281	The interaction arises because KL training partially learns to correct the mean drift that SPON addresses---the KL gradient pushes the predictor to minimize all correctable errors, including systematic bias. Per-layer analysis reveals that early (attention-heavy) layers show near-orthogonal corrections (cosine similarity ${\sim}$0.10), while middle (FFN-heavy) layers show greater overlap (cosine ${\sim}$0.25). We characterize this as \emph{partial additivity}: the composition provides meaningful gains but should not be interpreted as clean decomposition.
282	
283	
284	% ---------------------------------------------------------------------------
285	\subsection{Full Benchmark Evaluation}
286	\label{sec:full_eval}
287	
288	Table~\ref{tab:full_bench} presents results across seven benchmarks. KL-only achieves 3.4\% average accuracy drop versus dense, outperforming BCE+compensation (5.2\%) and TEAL (9.8\%). SPON+KL achieves the best quality at 2.3\% average drop.
289	
290	\begin{table}[t]
291	\centering
292	\caption{Full benchmark comparison (Llama 3.1 8B, 50\% sparsity).}
293	\label{tab:full_bench}
294	\small
295	\setlength{\tabcolsep}{4pt}
296	\begin{tabular}{lcccccccr}
297	\toprule
298	Method & Wiki$\downarrow$ & C4$\downarrow$ & ARC-c$\uparrow$ & WG$\uparrow$ & MMLU$\uparrow$ & GSM8K$\uparrow$ & HE$\uparrow$ & Avg Drop \\
299	\midrule
300	Dense & 6.12 & 8.88 & 53.4 & 74.2 & 65.3 & 48.2 & 33.5 & --- \\
301	TEAL & 12.50 & 17.10 & 47.8 & 67.2 & 58.5 & 40.5 & 27.0 & 9.8\% \\
302	SPON & 11.20 & 15.50 & 49.5 & 69.8 & 60.5 & 43.0 & 28.5 & 7.0\% \\
303	BCE+comp & 11.56 & 15.20 & 50.2 & 70.5 & 61.8 & 44.8 & 30.5 & 5.2\% \\
304	KL-only & 9.53 & 12.80 & 51.5 & 72.0 & 63.0 & 46.2 & 31.5 & 3.4\% \\
305	SPON+KL & 8.91 & 11.90 & 52.1 & 72.8 & 63.8 & 47.0 & 32.0 & 2.3\% \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	\paragraph{Inference efficiency.}
311	Table~\ref{tab:efficiency} reports wall-clock latency on an A100 GPU. At batch size 32 (compute-bound regime), KL-only achieves 1.49$\times$ speedup versus 1.18$\times$ for BCE+compensation---the compensation network's 256\,MB parameters and per-layer GEMV operations consume roughly one-third of the sparsity savings. At batch size 1 (memory-bandwidth-bound), sparsity benefits are smaller across all methods.
312	
313	\begin{table}[t]
314	\centering
315	\caption{Inference efficiency (A100 GPU).}
316	\label{tab:efficiency}
317	\small
318	\begin{tabular}{lccccr}
319	\toprule
320	Method & Lat.\ $b$=1 & Speedup $b$=1 & Lat.\ $b$=32 & Speedup $b$=32 & Extra Params \\
321	\midrule
322	Dense & 18.0\,ms & 1.00$\times$ & 3.20\,ms & 1.00$\times$ & --- \\
323	KL-only & 16.5\,ms & 1.09$\times$ & 2.15\,ms & 1.49$\times$ & 8\,MB \\
324	SPON+KL & 16.5\,ms & 1.09$\times$ & 2.15\,ms & 1.49$\times$ & 8.5\,MB \\
325	BCE+comp & 17.8\,ms & 1.01$\times$ & 2.72\,ms & 1.18$\times$ & 264\,MB \\
326	\bottomrule
327	\end{tabular}
328	\end{table}
329	
330	% ---------------------------------------------------------------------------
331	\subsection{Cross-Model Generalization}
332	\label{sec:mistral}
333	
334	To verify that KL's advantage is not architecture-specific, we evaluate on Mistral-7B-v0.3, which uses grouped-query attention and sliding window attention (Table~\ref{tab:cross_model}).
335	
336	\begin{table}[t]
337	\centering
338	\caption{Cross-model validation at 50\% sparsity. KL advantage direction is consistent; magnitude varies by architecture.}
339	\label{tab:cross_model}
340	\small
341	\begin{tabular}{llcccc}
342	\toprule
343	Model & Condition & Wiki PPL$\downarrow$ & ARC-c$\uparrow$ & MMLU$\uparrow$ & KL--BCE gap \\
344	\midrule
345	Llama 3.1 8B & Dense & 6.12 & 53.4 & 65.3 & --- \\
346	Llama 3.1 8B & KL-only & 9.53 & 51.5 & 63.0 & 2.03 \\
347	Llama 3.1 8B & BCE+comp & 11.56 & 50.2 & 61.8 & --- \\
348	\midrule
349	Mistral 7B v0.3 & Dense & 5.52 & 55.0 & 63.5 & --- \\
350	Mistral 7B v0.3 & KL-only & 9.38 & 52.8 & 61.5 & 1.07 \\
351	Mistral 7B v0.3 & BCE+comp & 10.45 & 51.5 & 60.2 & --- \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	KL-only consistently outperforms BCE+compensation on both architectures. The smaller gap on Mistral (1.07 vs.\ 2.03) is expected: Mistral's GQA produces more concentrated activation patterns where BCE's per-neuron independence assumption is less harmful, and sliding window attention reduces per-token variation in neuron importance. The directional consistency across architectures supports generalizability; the magnitude variation calls for architecture-aware analysis rather than universal effect-size claims.
357	
358	% ---------------------------------------------------------------------------
359	\subsection{Long-Context Evaluation}
360	\label{sec:longcontext}
361	
362	We evaluate on LongBench (English subset, 4K--32K tokens) and RULER (synthetic tasks at 4K and 16K) to test predictor generalization beyond training sequence length (2048 tokens).
363	
364	\begin{table}[t]
365	\centering
366	\caption{LongBench performance (English subset). KL-only maintains lower degradation than BCE+compensation, with SPON+KL achieving the smallest average drop.}
367	\label{tab:longbench}
368	\small
369	\setlength{\tabcolsep}{4pt}
370	\begin{tabular}{lccccccr}
371	\toprule
372	Method & S-QA & M-QA & Summ. & Few-shot & Code & Avg & Drop \\
373	\midrule
374	Dense & 42.5 & 36.0 & 27.2 & 60.0 & 34.0 & 39.9 & --- \\
375	TEAL & 34.0 & 27.5 & 23.0 & 48.5 & 24.5 & 31.5 & 21.1\% \\
376	BCE+comp & 36.5 & 30.0 & 24.2 & 53.5 & 28.5 & 34.5 & 13.5\% \\
377	KL-only & 38.8 & 32.2 & 25.5 & 55.8 & 30.2 & 36.5 & 8.5\% \\
378	SPON+KL & 39.5 & 33.0 & 25.8 & 56.5 & 31.0 & 37.2 & 6.8\% \\
379	\bottomrule
380	\end{tabular}
381	\end{table}
382	
383	\begin{table}[t]
384	\centering
385	\caption{RULER evaluation at 4K and 16K context lengths.}
386	\label{tab:ruler}
387	\small
388	\begin{tabular}{lccr}
389	\toprule
390	Method & 4K Avg & 16K Avg & 4K$\rightarrow$16K $\Delta$ \\
391	\midrule
392	Dense & 92.0 & 85.0 & $-$7.0 \\
393	KL-only & 85.5 & 73.5 & $-$12.0 \\
394	SPON+KL & 87.0 & 75.5 & $-$11.5 \\
395	BCE+comp & 81.0 & 67.0 & $-$14.0 \\
396	\bottomrule
397	\end{tabular}
398	\end{table}
399	
400	KL-trained prediction degrades more gracefully than BCE+compensation on both evaluations. On LongBench, the KL--BCE gap widens at long context (8.5\% vs.\ 13.5\% average drop), suggesting that KL's distributional supervision provides better out-of-distribution robustness. On RULER, KL shows smaller 4K$\rightarrow$16K degradation ($-$12.0 vs.\ $-$14.0), with needle retrieval tasks (78.0 at 16K) degrading less than multi-key or aggregation tasks that require cross-position reasoning.
401	
402	% ---------------------------------------------------------------------------
403	\subsection{Instruction-Following Quality}
404	\label{sec:mtbench}
405	
406	Table~\ref{tab:mtbench} reports MT-Bench scores (80 multi-turn questions, GPT-4o judge).
407	
408	\begin{table}[t]
409	\centering
410	\caption{MT-Bench scores by category (GPT-4o judge).}
411	\label{tab:mtbench}
412	\small
413	\setlength{\tabcolsep}{4pt}
414	\begin{tabular}{lcccc}
415	\toprule
416	Category & Dense & KL-only & BCE+comp & SPON+KL \\
417	\midrule
418	Writing & 7.5 & 7.1 & 6.8 & 7.2 \\
419	Roleplay & 7.3 & 6.9 & 6.5 & 7.0 \\
420	Reasoning & 6.8 & 6.2 & 5.8 & 6.4 \\
421	Math & 6.5 & 5.8 & 5.3 & 6.0 \\
422	Coding & 7.0 & 6.5 & 6.1 & 6.7 \\
423	Extraction & 7.8 & 7.3 & 7.0 & 7.5 \\
424	STEM & 7.2 & 6.8 & 6.4 & 6.9 \\
425	Humanities & 7.9 & 7.2 & 7.2 & 7.3 \\
426	\midrule
427	Average & 7.25 & 6.72 & 6.38 & 6.85 \\
428	\bottomrule
429	\end{tabular}
430	\end{table}
431	
432	KL-only (6.72) outperforms BCE+compensation (6.38) by 0.34 points on average, with SPON+KL reaching 6.85. Math and reasoning categories are most affected by sparsity (KL: 5.8 and 6.2), while writing and extraction are most robust (7.1 and 7.3)---consistent with the intuition that precise computation chains are more sensitive to neuron pruning than pattern-matching tasks.
433	
434	% ---------------------------------------------------------------------------
435	\subsection{Sparsity Scaling Analysis}
436	\label{sec:scaling}
437	
438	We evaluate KL-only and BCE-only across seven sparsity levels (30--60\%) to characterize how the KL advantage scales (Table~\ref{tab:scaling}).
439	
440	\begin{table}[t]
441	\centering
442	\caption{Sparsity sweep: KL vs.\ BCE PPL across sparsity levels (1 seed per level; 50\% reuses 5-seed data).}
443	\label{tab:scaling}
444	\small
445	\begin{tabular}{cccccc}
446	\toprule
447	Sparsity & KL PPL & BCE PPL & $\Delta$(BCE$-$KL) & Quad.\ pred. & Residual \\
448	\midrule
449	30\% & 6.82 & 11.32 & 4.50 & 6.67 & $-$2.17 \\
450	35\% & 7.28 & 14.48 & 7.20 & 9.07 & $-$1.87 \\
451	40\% & 7.95 & 18.95 & 11.00 & 11.90 & $-$0.90 \\
452	45\% & 8.58 & 23.38 & 14.80 & 15.08 & $-$0.28 \\
453	50\% & 9.53 & 28.16 & 18.63 & 18.71 & $-$0.08 \\
454	55\% & 11.20 & 36.70 & 25.50 & 22.79 & +2.71 \\
455	60\% & 14.05 & 49.05 & 35.00 & 27.31 & +7.69 \\
456	\bottomrule
457	\end{tabular}
458	\end{table}
459	
460	The KL--BCE gap grows monotonically with sparsity, consistent with the theoretical expectation that joint neuron interaction effects---captured by KL but missed by BCE---scale with the number of pruned neurons. A quadratic fit ($\Delta \approx 97.2 \cdot s^2$) achieves $R^2 = 0.88$, explaining the majority of variance but with systematic residuals: sub-quadratic at low sparsity (where per-neuron independence is a less harmful approximation) and super-quadratic at high sparsity (where higher-order interaction terms become significant). We report this as a consistent empirical trend rather than a precise quantitative law.
461	
462	
463	% ===========================================================================
464	\section{Discussion}
465	
466	\paragraph{Why does KL eliminate compensation?}
467	Our results suggest a mechanistic explanation. BCE trains the predictor to match per-neuron binary targets independently, producing masks where joint interaction errors accumulate---compensation networks then learn to correct these errors post-hoc. KL training, by propagating output-distribution gradients through the masking operation, allows the predictor to optimize neuron selection \emph{jointly}. The marginal return of compensation on top of KL (0.48 PPL) versus on top of BCE (16.60 PPL) quantifies this: KL preemptively addresses the bulk of errors that compensation would otherwise need to correct.
468	
469	\paragraph{Practical implications.}
470	The elimination of compensation networks simplifies the inference pipeline in two ways: (1)~264\,MB fewer parameters to load and store, enabling deployment on memory-constrained devices; (2)~removal of per-layer GEMV operations that reduce the effective speedup from sparsity. At batch 32, this translates to 1.49$\times$ vs.\ 1.18$\times$ speedup. The training cost increase (3.8 vs.\ 0.4 GPU-hours) is modest and amortized over deployment.
471	
472	\paragraph{Limitations.}
473	Our study has several limitations. (1)~We evaluate on 7B--8B scale models; behavior at larger scales is unknown. (2)~The 22\% interaction residual in SPON+KL composition limits the clean decomposition narrative. (3)~The sparsity scaling analysis ($R^2 = 0.88$) uses single seeds per level and shows systematic deviations from the quadratic model. (4)~Long-context evaluations show increased degradation (8.5--12\% drop), suggesting the predictor's distributional robustness has limits. (5)~KL training requires a dense forward pass per step, making it ${\sim}$80$\times$ more expensive per step than BCE, though total training remains under 4 GPU-hours.
474	
475	
476	% ===========================================================================
477	\section{Conclusion}
478	
479	We present a systematic study of training signals for contextual SwiGLU sparsity prediction, organized around a taxonomy crossing loss coupling with correction granularity. Our central finding is that KL-divergence training eliminates the need for error compensation networks: a KL-trained predictor at 50\% sparsity achieves 9.53 PPL on Llama~3.1~8B---surpassing BCE+compensation (11.56) with zero compensation overhead, enabling a simpler pipeline with 1.49$\times$ batch-32 speedup and only 8\,MB additional parameters. Composition with SPON's static correction achieves the best overall quality (8.91 PPL) with partial additivity. These findings hold across two model families, seven benchmarks, and long-context evaluations, establishing output-distribution distillation as a principled and practical training signal for activation sparsity prediction.
480	
481	
482	% ===========================================================================
483	\appendix
484	\section{Sparsity Scaling: Detailed Fit Analysis}
485	\label{app:scaling}
486	
487	The quadratic model $\Delta(s) = a \cdot s^2$ fitted to the KL--BCE PPL gap yields $a = 97.2$ with $R^2 = 0.88$. The systematic residual pattern (Table~\ref{tab:scaling}) shows sub-quadratic behavior at $s \leq 0.45$ and super-quadratic behavior at $s \geq 0.55$. This suggests that the true relationship involves higher-order terms: at low sparsity, neuron interactions are sparse and well-captured by pairwise effects; at high sparsity, multi-neuron interaction cascades produce super-quadratic divergence. While the $R^2$ of 0.88 supports the general trend that KL advantage grows super-linearly with sparsity, we caution against interpreting the quadratic coefficient as a precise physical constant.
488	
489	\section{SPON Reproduction Details}
490	\label{app:spon}
491	
492	SPON trains per-layer bias vectors (${\sim}$0.5\,MB total, 0.3 GPU-hours) to correct average activation drift via KL divergence. Our reproduction on Llama~3.1~8B achieves WikiText-2 PPL of 11.20, with QA benchmarks within $\pm$1.2\% of published values (Table~\ref{tab:spon_repro}). SPON's PPL (11.20) is comparable to BCE+compensation (11.56) despite using static, input-independent correction---an observation suggesting that KL-quality training signal provides value even in the limited static-correction setting, while BCE requires contextual compensation to reach comparable performance.
493	
494	
495	\bibliographystyle{plainnat}
496	\bibliography{references}
497	
498	\end{document}
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37d0353d-236a-4db7-9290-ea0f61898a72",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "a632f519-53ff-4f96-a676-188e4747b14c",
  "sourceToolAssistantUUID": "37d0353d-236a-4db7-9290-ea0f61898a72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T17:54:04.765Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0112oaJQTaFTUKC4DxsDRByV`</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a632f519-53ff-4f96-a676-188e4747b14c",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nLt5psSXGnRnnFc8g6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f26ab0e-57e6-4ff0-ad39-e69ecc8259d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aRTKTQmttgnPi9BA8SGcP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14069,
      "cache_read_input_tokens": 31162,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 31162,
          "cache_creation_input_tokens": 14069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14069,
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

_source line 31 · 2026-05-15T17:54:04.781Z_

<details><summary>↩ Tool result · `toolu_0112oaJQTaFTUKC4DxsDRByV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:53 UTC | 更新原因: Reviewer warning 修正：BCE std 0.72→0.89，Claim 3 降级，SPON 预算提升，并行启动计划\\n\\n## 核心方向\\nKL-divergence 输出分布蒸馏训练 SwiGLU 激活稀疏性预测器，验证是否消除对 error compensation network 的需求，并测试与 SPON 静态校正的组合加性。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-15 通过，D007）\\n- **MVP 结论**: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.89 @ 50% sparsity，差距 31.53 PPL\\n- **关键发现**: KL 非均匀 per-layer 分配（0.22-0.80）vs BCE 均匀（0.43-0.66）；KL hard-mask PPL 9.20 接近 dense 6.12\\n- **Dream**: dream_20260515T164925 运行中（full review），等结果后批准 P0 实验\\n- **Experiment Plan**: 12 experiments（P0×7, P1×3, P2×2），总 196 GPU-hours。详见 experiment_plan.yaml\\n- **Reviewer Warning**: Claim 1 强度取决于 BCE+comp（未测）；Claim 3 降级为 testable prediction；SPON 复现是关键路径\\n\\n## 近期任务\\n- [x] MVP 验证（KL vs BCE @ 50% sparsity, 3 seeds）\\n- [x] 写 paper_framing.md + experiment_plan.yaml\\n- [x] 启动 Dream full review (dream_20260515T164925)\\n- [ ] 等 Dream 结果 → 按行动指令调整\\n- [ ] Dream 通过后并行启动: plan_001 BCE+comp (cuda:0) + plan_004 SPON (cuda:1)\\n- [ ] Agent 完成 vanilla TEAL baseline（队列中）\\n- [ ] 补 KL-only 2 seeds (s0, s1) → 5-seed headline\\n- [ ] 实现 BCE+compensation 训练流程\\n- [ ] 关注 s456 seed 敏感性（13.58 vs 12.08/11.91）\\n\\n## GPU 预算\\n- 本地: westd-34887 cuda:0, cuda:1 — RTX PRO 6000 Blackwell (98GB each)\\n- 可用: 444 GPU-hours remaining (480 - 36 MVP)\\n- 计划: P0 114h + P1 70h + P2 12h = 196h（44% 利用率）\\n- Constraint: C001 — 仅 cuda:0, cuda:1\\n\\n## 目标时间线\\n| 阶段 | 日期 | 内容 |\\n|------|------|------|\\n| Dream review | 05-15 | dream_20260515T164925 |\\n| Phase 1 | 05-15 ~ 05-18 | plan_001 BCE+comp + plan_004 SPON + plan_006 baselines（并行） |\\n| Phase 2 | 05-18 ~ 05-20 | plan_005 composition + plan_002 STE + plan_003 iso-compute |\\n| Phase 3 | 05-20 ~ 05-22 | plan_007 full eval + plan_008 sweep + plan_009 Mistral |\\n| Paper | 05-22 ~ 05-24 | Paper Agent Full Draft + iteration |\\n| Submit | 05-25 | ARR submission |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-15 | MVP PASS: 项目进入 research 阶段，启动 post-MVP kickoff 流程 | mvp_kl_norm_v2_s42, mvp_kl_norm_v2_s123, mvp_kl_norm_v2_s456, mvp_bce_s42, mvp_bce_s123, mvp_bce_s456 |\\n| D006 | 2026-05-15 | 紧急停止 KL 训练：Reviewer 发现 ÷vocab_size 归一化 bug，kl_norm | kl_normalized_quicktest, mvp_kl_norm_s42, mvp_kl_norm_s123 |\\n| D005 | 2026-05-15 | KL 归一化确认 seq_len-only，启动 KL 3-seed 完整训练 | kl_normalized_quicktest, mvp_kl_s42, mvp_kl_s123, mvp_kl_s456 |\\n| D004 | 2026-05-15 | KL 稀疏性坍塌修复：选方案 C（KL loss 归一化 + 激进 Lagrangian），保持纯  | kl_lagrangian_quicktest |\\n| D003 | 2026-05-15 | KL 训练稀疏性坍塌至 0%，改用 Lagrangian multiplier 替代固定 reg_w | mvp_kl_s42 |\\n| D002 | 2026-05-15 | 校准数据从 SlimPajama-627B 改为 WikiText-103 train split | mvp_kl_s42, mvp_bce_s42 |\\n| D001 | 2026-05-15 | MVP 设计: KL vs BCE predictor 在 50% sparsity 下的 perp | — |\\n\\n\\n\\n\", \"total_chars\": 2753, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f26ab0e-57e6-4ff0-ad39-e69ecc8259d5",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "4b81b606-4779-4600-9492-40fbf5e042a9",
  "sourceToolAssistantUUID": "3f26ab0e-57e6-4ff0-ad39-e69ecc8259d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T17:54:08.061Z_

Now let me look at the experiment plan and the dream report to understand what data exists vs. what is projected.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b81b606-4779-4600-9492-40fbf5e042a9",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMMutp8QKhFWXP2CGz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37fcf527-419e-4b2b-a6ae-8a6d4d49e786",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaqKbNBn1vq4haehUhnZMX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13803,
      "cache_read_input_tokens": 45231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13803,
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

_source line 33 · 2026-05-15T17:54:09.020Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EMGNL879WCbrjcCGF8xzGh`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37fcf527-419e-4b2b-a6ae-8a6d4d49e786",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMMutp8QKhFWXP2CGz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "395a688e-9048-44c0-adf4-94778bf02d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaqKbNBn1vq4haehUhnZMX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13803,
      "cache_read_input_tokens": 45231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13803,
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

_source line 34 · 2026-05-15T17:54:09.040Z_

<details><summary>↩ Tool result · `toolu_01EMGNL879WCbrjcCGF8xzGh`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "395a688e-9048-44c0-adf4-94778bf02d16",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "a3dbbcdd-bea0-4a03-bacc-3d2d3774f856",
  "sourceToolAssistantUUID": "395a688e-9048-44c0-adf4-94778bf02d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T17:54:09.308Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AtthTLmKkzFhs1uX1QDurX`</summary>

```json
{
  "pattern": "**/dream_20260515T164925/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3dbbcdd-bea0-4a03-bacc-3d2d3774f856",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMMutp8QKhFWXP2CGz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e1b6855-edfd-486c-ad8a-b4b3fcf979f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KaqKbNBn1vq4haehUhnZMX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13803,
      "cache_read_input_tokens": 45231,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 45231,
          "cache_creation_input_tokens": 13803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13803,
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

_source line 36 · 2026-05-15T17:54:09.326Z_

<details><summary>↩ Tool result · `toolu_01AtthTLmKkzFhs1uX1QDurX`</summary>

```text
artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/best/review_report.md
artifacts/dream_reports/dream_20260515T164925/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e1b6855-edfd-486c-ad8a-b4b3fcf979f2",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "0d75242f-a341-41c6-90de-1d59904c0031",
  "sourceToolAssistantUUID": "7e1b6855-edfd-486c-ad8a-b4b3fcf979f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T17:54:12.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NFNboMV58m8ezns9CuF3BG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d75242f-a341-41c6-90de-1d59904c0031",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMhDFS9AtZWrG7a12L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e5074ac-5dfd-4128-8fbf-8e2796701645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5DQcYwepChXRMFLX3AWtc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 59034,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 38 · 2026-05-15T17:54:12.182Z_

<details><summary>↩ Tool result · `toolu_01NFNboMV58m8ezns9CuF3BG`</summary>

```text
1	---
2	dream_id: dream_20260515T164925
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-15T17:51:48.790433+00:00
6	---
7	
8	
9	# Dream Review Report: Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction
10	
11	**Dream ID**: 20260515T164925 | **Review Mode**: full | **Date**: 2026-05-15
12	
13	---
14	
15	## Panel
16	
17	- **R1** (Methods + Experiments): Score 3/6 (Weak Reject), Confidence 4/5
18	- **R2** (Novelty + Related Work): Score 3/6 (Weak Reject), Confidence 4/5
19	- **Consensus Score: 3/6 (Weak Reject)**
20	
21	---
22	
23	## 1. Paper Summary
24	
25	The paper studies training signals for contextual SwiGLU sparsity prediction, organized around a 2D taxonomy (loss coupling × correction granularity). The central finding is that a KL-divergence-trained contextual predictor (PPL 9.53 at 50% sparsity, Llama 3.1 8B) surpasses BCE+compensation (PPL 11.56) while eliminating 256MB of compensation parameters, yielding a simpler pipeline with 1.49× batch-32 speedup and 8MB overhead. Secondary contributions include SPON+KL composition with 22% interaction residual and a sparsity scaling analysis.
26	
27	---
28	
29	## 2. Strengths (Consensus)
30	
31	- **Large, unambiguous effect size.** KL-only Pareto-dominates BCE+compensation on both quality (9.53 vs 11.56 PPL) and efficiency (1.49× vs 1.18× speedup, 8MB vs 264MB). The practical implication — eliminating compensation networks — is clear and deployment-relevant.
32	
33	- **Above-average ablation design.** The four-condition matrix (loss × compensation), STE isolation experiment (72/28% decomposition), iso-compute comparison, and SPON composition analysis form a methodologically sound set of controls that systematically isolates confounds. This structure exceeds the norm for the subfield.
34	
35	- **Comprehensive evaluation breadth.** 13 tables spanning perplexity, 7 discriminative benchmarks, 2 long-context evaluations (LongBench, RULER), instruction-following (MT-Bench), inference profiling, cross-architecture (Mistral), and sparsity sweep. Coverage of the planned experiment list is complete (12/12 imagined experiments appear in the paper).
36	
37	- **Honest limitation reporting.** The 22% interaction residual is properly characterized as "partial additivity" rather than clean decomposition. The sparsity scaling R²=0.88 is reported as "consistent empirical trend" rather than a precise law. The paper acknowledges scale limitations, training cost, and long-context degradation explicitly.
38	
39	- **Gradient coupling argument is mathematically precise.** The chain-rule distinction between BCE's factorized gradient (∂L_BCE/∂s_j depends only on neuron j) and KL's coupled gradient (flows through ∂logits/∂h Jacobian) is a correct structural observation, not an analogy.
40	
41	- **SPON+KL modular decomposition is the most original contribution.** The orthogonality analysis (per-layer cosine similarity, logit-space linearity test) and quantified interaction residual provide the right kind of evidence for composition claims. This deserves co-headline status.
42	
43	---
44	
45	## 3. Weaknesses
46	
47	### 3.1 Critical (would block acceptance)
48	
49	**(W1) Missing MSE-on-logits baseline — both reviewers flag this as the single most damaging omission.**
50	The gradient coupling property that the paper's theoretical narrative rests on (∂L/∂s_j couples all neurons through ∂logits/∂h) is a property of ANY output-level loss (MSE on logits, JS divergence, reverse KL, etc.), not uniquely KL. Without testing at least MSE on output logits, the paper cannot distinguish "KL is special" from "any coupled output-level loss beats BCE." If MSE-logits matches KL, the framing collapses from "KL divergence eliminates compensation" to the weaker but still valid "output-level training signals eliminate compensation." This is a one-experiment fix that would either strengthen or appropriately reframe the contribution. **Severity: Major.**
51	
52	**(W2) BCE baseline fairness concerns.**
53	BCE-only (28.16 PPL) is 2.25× worse than training-free TEAL (12.50 PPL). A trained predictor performing dramatically worse than a magnitude heuristic is anomalous and raises multiple fairness questions:
54	- Was BCE trained with Gumbel-sigmoid relaxation? Gumbel-sigmoid is designed for continuous losses; applying it to BCE (which naturally pairs with STE) may actively harm BCE training. The STE ablation (Table 4) only tests KL+STE, never BCE+STE.
55	- How are BCE targets generated? If by top-k activation magnitude, target quality is a confound — KL implicitly discovers better masks, so the gap may partly reflect target quality rather than loss function quality.
56	- The KL pipeline uses a Lagrangian multiplier mechanism for sparsity enforcement that required multiple iterations to stabilize. Does the BCE baseline receive comparable engineering effort?
57	Without a BCE+STE control and BCE with KL-optimal targets, the reported gap is confounded. **Severity: Major.**
58	
59	**(W3) Novelty is thin for a top venue.**
60	The core contribution is swapping BCE for KL divergence in an existing predictor pipeline (FastForward-style architecture + Gumbel relaxation). SPON already demonstrated that KL works for sparsity prediction (in the static setting); extending to contextual prediction is the obvious next step in the taxonomy the paper itself constructs. The 2D taxonomy is useful framing but is organizational, not a technical contribution. The gradient coupling insight, while correct, is a standard observation about output-level losses in knowledge distillation — it has been well-understood since at least Hinton et al. (2015) that distillation losses propagate richer gradients than classification losses. The paper does not cite or differentiate from the broader distillation literature. **Severity: Major.**
61	
62	### 3.2 Significant (should be addressed)
63	
64	**(W4) Related work is severely underdeveloped.**
65	The paper references only a handful of methods (TEAL, WINA, R-Sparse, SPON, FastForward, ShadowLLM). Missing citations include:
66	- Deja Vu (foundational contextual sparsity predictor work)
67	- CATS (contextual activation sparsity)
68	- Minitron (structured pruning with distillation)
69	- DIP (dynamic inference pruning)
70	- Knowledge distillation foundations (Hinton et al. 2015 — the gradient coupling insight originates here)
71	- Gumbel-softmax/Gumbel-sigmoid foundations (Jang et al. 2017, Maddison et al. 2017)
72	- L0 regularization (Louizos et al. 2018 — directly relevant to learned binary masks)
73	- MoE routing literature (per-token expert selection is structurally identical to per-token neuron selection)
74	A paper claiming a taxonomic contribution must comprehensively survey the field. **Severity: Moderate.**
75	
76	**(W5) Unequal seed counts and missing statistical tests.**
77	KL-only and BCE+comp use 5 seeds, but BCE-only and KL+comp use only 3. The sparsity sweep uses 1 seed per level. The claim "compensation is redundant for KL" rests on 9.53 vs 9.05 (5 vs 3 seeds) — a 0.48 PPL gap within 1 standard deviation (0.41). No formal significance tests (paired bootstrap, permutation test, Cohen's d) are reported for any comparison. The sparsity scaling curve fit (R²=0.88, 7 single-seed points) cannot distinguish quadratic from alternative functional forms without AIC/BIC comparison. **Severity: Moderate.**
78	
79	**(W6) Reproducibility gaps.**
80	The Lagrangian multiplier mechanism for sparsity enforcement (lambda initialization, exponential update schedule, clamping range) is critical for KL training stability but underspecified in the paper. Project history suggests this mechanism required multiple debugging iterations (sparsity collapse, normalization bugs). Without full specification, first-attempt reproduction is unlikely. Predictor architecture details (rank-128 bottleneck) are stated but not justified — no sensitivity analysis across alternative ranks. **Severity: Moderate.**
81	
82	### 3.3 Minor
83	
84	**(W7) Only 7-8B scale tested.** The "eliminates compensation" claim is validated at a single model scale. The gradient coupling argument predicts stronger KL advantage at larger hidden dimensions, but this is untested. At minimum, a testable prediction about scaling should be stated.
85	
86	**(W8) Calibration data sensitivity unexamined.** Training uses 128 sequences from C4, evaluation is on WikiText-2. No cross-domain sensitivity analysis is provided. Given known OOD fragility of learned sparsity predictors, this is a meaningful gap.
87	
88	**(W9) Long-context degradation (8.5-12% drop) is non-trivial.** The predictor is trained on 2048-token sequences but evaluated at 4K-32K. The increased degradation at longer contexts suggests distributional robustness limits. This is acknowledged in limitations but not analyzed (e.g., training on longer sequences as a control).
89	
90	---
91	
92	## 4. Questions for Authors
93	
94	1. **Evaluation protocol clarity**: Which protocol produces the headline PPL numbers — the predictor's own hard-mask evaluation, or TEAL's greedy allocation applied on top? Please specify unambiguously.
95	
96	2. **BCE relaxation method**: Was BCE trained with Gumbel-sigmoid? If so, was BCE+STE tested? The STE ablation (Table 4) only varies KL's relaxation, creating an asymmetry.
97	
98	3. **BCE target generation**: How are binary targets for BCE constructed? Top-k by activation magnitude? Have you tested BCE with oracle targets derived from KL-optimal masks?
99	
100	4. **Why KL specifically vs. other output-level losses?** The gradient coupling argument applies identically to MSE on logits. What property of KL (asymmetry, information-geometric structure, etc.) makes it preferable? Or is this an untested assumption?
101	
102	5. **Lagrangian mechanism details**: What are lambda_init, the update schedule, and the clamping bounds? How sensitive is training to these hyperparameters?
103	
104	6. **Compensation redundancy claim**: The KL-only vs KL+comp gap (0.48 PPL, 5 vs 3 seeds) is within 1 std. Can you provide a formal significance test for this comparison?
105	
106	---
107	
108	## 5. Missing Experiments / Analysis (Priority-Ordered)
109	
110	1. **MSE-on-logits baseline** — Highest priority. One experiment that either validates KL-specificity or correctly reframes the contribution.
111	2. **BCE + STE baseline** — Ensures the BCE baseline uses its natural relaxation, eliminating a fairness confound.
112	3. **BCE with KL-optimal targets** — Disentangles loss function quality from target quality.
113	4. **Per-layer PPL decomposition** — Which layers show the largest KL-BCE gap? The KL predictor learns highly non-uniform per-layer sparsity (reportedly 0.22-0.80 range) vs BCE's near-uniform allocation. A per-layer analysis would strengthen the joint-interaction narrative.
114	5. **Training dynamics curves** — Loss, sparsity, PPL vs training step for all conditions. The KL training landscape appears more complex than presented.
115	6. **Formal statistical tests** — Paired bootstrap on headline comparisons; AIC/BIC for sparsity scaling functional form.
116	7. **Predictor rank sensitivity** — At least one alternative (r=64 or r=256) to show robustness.
117	
118	---
119	
120	## 6. Experiment Coverage Assessment
121	
122	All 12 imagined experiments from the design document are present in the paper:
123	
124	| # | Experiment | Table | Covered |
125	|---|-----------|-------|---------|
126	| 1 | Four-condition ablation | Table 3 | ✓ |
127	| 2 | STE baseline | Table 4 | ✓ |
128	| 3 | Iso-compute BCE | Table 5 | ✓ |
129	| 4 | SPON reproduction | Table 6 | ✓ |
130	| 5 | SPON+KL composition | Table 7 | ✓ |
131	| 6 | Training-free baselines | Table 2 | ✓ |
132	| 7 | Full benchmarks + profiling | Tables 8-9 | ✓ |
133	| 8 | Sparsity sweep | Table 14 | ✓ |
134	| 9 | Mistral generalization | Table 10 | ✓ |
135	| 10 | LongBench | Table 11 | ✓ |
136	| 11 | MT-Bench | Table 13 | ✓ |
137	| 12 | RULER | Table 12 | ✓ |
138	
139	Coverage is complete. The gap is not in what was planned but in what was NOT planned: the missing MSE-logits and BCE+STE controls.
140	
141	---
142	
143	## 7. Consolidated Assessment
144	
145	### What works well
146	The paper asks a genuinely useful question (can output-distribution distillation replace compensation?) and answers it with a well-structured ablation battery. The effect size is large and practically meaningful. The SPON+KL composition analysis with quantified interaction residual is the most original element. The evaluation breadth (13 tables, 7 benchmarks, long-context, MT-Bench, cross-model) exceeds the subfield norm. Claims are mostly well-calibrated to evidence, with honest limitation reporting.
147	
148	### What prevents acceptance
149	Three issues converge: (1) The missing MSE-on-logits control leaves the paper unable to distinguish its specific claim ("KL is special") from the more general claim ("any output-level loss beats BCE") — this is a one-experiment gap but it undermines the entire theoretical narrative. (2) The BCE baseline may be unfairly handicapped by using Gumbel-sigmoid (designed for continuous losses) rather than STE (its natural pairing), inflating the reported gap. (3) The novelty threshold is marginal — swapping BCE for KL in an existing pipeline, where SPON already proved KL works for sparsity prediction, is an incremental advance. The gradient coupling insight, while correct, is well-known from the knowledge distillation literature.
150	
151	### Path to acceptance
152	- Run MSE-on-logits and BCE+STE controls (two experiments, likely <1 day compute)
153	- If MSE-logits ≈ KL: reframe as "output-level training signals eliminate compensation" (still a valid contribution, different framing)
154	- If MSE-logits ≪ KL: the paper has a stronger, KL-specific story
155	- Expand related work to cover distillation foundations, Deja Vu, CATS, L0 regularization, MoE routing
156	- Add formal significance tests and per-layer analysis
157	- Promote SPON+KL composition to co-headline contribution
158	- Fully specify the Lagrangian mechanism
159	
160	---
161	
162	## 8. Scores Summary
163	
164	| | R1 (Methods) | R2 (Novelty) | Consensus |
165	|---|---|---|---|
166	| Score | 3/6 | 3/6 | **3/6 (Weak Reject)** |
167	| Confidence | 4/5 | 4/5 | 4/5 |
168	
169	**Bottom line**: A well-executed empirical study with a large effect size, held back by a thin novelty margin and two missing critical controls (MSE-logits, BCE+STE) that leave the core theoretical claim untested. The path to acceptance is short (2 experiments + reframing) but essential.
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5074ac-5dfd-4128-8fbf-8e2796701645",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "5c8f1d25-0126-4d0e-8675-4c781ef55f46",
  "sourceToolAssistantUUID": "8e5074ac-5dfd-4128-8fbf-8e2796701645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T17:54:12.561Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HjQR99Cg2RY1emSYMrfPwo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8f1d25-0126-4d0e-8675-4c781ef55f46",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMhDFS9AtZWrG7a12L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da64a3d2-fa5b-4836-8bd6-d4bbb427d5db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5DQcYwepChXRMFLX3AWtc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 59034,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 59034,
          "cache_creation_input_tokens": 404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 404,
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

_source line 40 · 2026-05-15T17:54:12.573Z_

<details><summary>↩ Tool result · `toolu_01HjQR99Cg2RY1emSYMrfPwo`</summary>

```text
1	---
2	dream_id: dream_20260515T164925
3	tier: best
4	overall_score: 3/6 Weak Reject
5	timestamp: 2026-05-15T17:49:35.418147+00:00
6	---
7	
8	# R2 Review — Novelty, Positioning, and Related Work
9	
10	**Paper:** "Output-Distribution Distillation Eliminates Compensation Overhead for Contextual SwiGLU Sparsity Prediction"
11	**Reviewer:** R2 (Novelty & Related Work focus)
12	**Score:** 3/6 (Weak Reject)
13	**Confidence:** 4/5
14	
15	---
16	
17	## Summary
18	
19	The paper proposes replacing BCE with KL-divergence loss when training contextual sparsity predictors for SwiGLU FFN layers, arguing that KL's gradient coupling through the output Jacobian captures joint neuron interactions that BCE's factorized gradient misses. On Llama 3.1 8B at 50% sparsity, the KL-trained predictor achieves 9.20 PPL without compensation, outperforming BCE+compensation (18.64 PPL) while eliminating ~256MB of compensation parameters. A modular decomposition combining SPON static correction with KL contextual prediction yields 7.98 PPL with 6.8% interaction residual.
20	
21	---
22	
23	## Strengths
24	
25	- **Large, unambiguous effect size.** The KL-only vs. BCE+comp gap (9.20 vs. 18.64 PPL) is not a marginal improvement requiring statistical squinting. If the comparison is fair, this is a practically significant finding that would change how practitioners design sparse inference pipelines.
26	
27	- **Well-designed ablation battery.** The four-condition ablation (Table 1), STE baseline (Table 2), and iso-compute comparison (Table 3) constitute an above-average experimental design for this subfield. Each ablation targets a specific alternative explanation, and the authors anticipated the right reviewer concerns (Gumbel vs. KL, compute confound).
28	
29	- **Modular decomposition is the most original contribution.** The formalization c = c_s + c_theta(x) with SPON as static correction and KL as contextual correction, backed by per-layer cosine similarity analysis (mean 0.11) and quantified interaction residual (6.8%), is genuinely novel. This decomposition provides a principled framework for composing different correction strategies and is more interesting than the KL-vs-BCE comparison alone.
30	
31	- **2D taxonomy has organizational value.** The correction granularity x training signal coupling taxonomy clearly identifies the unoccupied design cell and provides a useful mental model for the field. It is not a deep intellectual contribution, but it is a clean way to position the work.
32	
33	- **Comprehensive evaluation breadth.** PPL on two corpora, five discriminative tasks, LongBench, MT-Bench, RULER, latency profiling, and cross-architecture validation on Mistral covers the evaluation space thoroughly. The NLP-specific benchmarks (LongBench, MT-Bench) strengthen EMNLP venue fit.
34	
35	- **Practical Pareto dominance.** KL-only is simultaneously better quality, lower latency, and smaller memory footprint than BCE+comp. This is the strongest form of practical contribution — no tradeoff to navigate.
36	
37	---
38	
39	## Weaknesses
40	
41	### Major
42	
43	1. **The core idea is a loss function swap, not a new method (Major — Novelty).** The entire technical contribution reduces to: replace `loss = BCE(pred, target)` with `loss = KL(dense_logits, sparse_logits)` in the training loop of an existing predictor architecture. SPON already demonstrated that KL divergence is effective for sparsity correction in this exact domain (SwiGLU LLMs). The extension from static bias (SPON) to contextual predictor is the obvious next step that any practitioner aware of SPON would try. The paper does not introduce a new architecture, a new training procedure, or a new theoretical framework — it validates a straightforward design choice. For a ~25% acceptance rate venue, this level of novelty is insufficient without substantially deeper analysis to compensate.
44	
45	2. **The gradient coupling insight is the chain rule, not a novel theoretical result (Major — Novelty).** The paper's theoretical narrative — that KL gradients couple neurons through the Jacobian while BCE factorizes — is mathematically correct but trivially follows from the chain rule applied to any output-level loss. MSE on logits, JS divergence, reverse KL, Wasserstein distance on output distributions, or any other loss computed on the model's final output would exhibit identical gradient coupling through the same Jacobian pathway. The paper never explains why KL is uniquely better than other coupled losses. This is a critical omission: if MSE on logits achieves comparable results, the contribution generalizes to "use any output-level loss instead of BCE" — still useful, but requiring complete reframing.
46	
47	3. **Missing MSE-on-logits baseline is the most conspicuous gap (Major — Related Work / Experimental).** Given that the paper's entire narrative centers on gradient coupling as the mechanism, the most obvious control experiment is MSE on the output logits, which provides identical coupling through the same Jacobian. Its absence is glaring and undermines the claimed specificity of KL. If MSE-logits matches KL, the story changes from "KL is special" to "any output-level loss beats BCE" — a weaker but still valid finding. If KL uniquely dominates MSE, this would substantially strengthen the distributional matching argument. Either outcome is informative, and the omission suggests the authors may not have considered this distinction.
48	
49	4. **BCE baseline appears unreasonably weak, raising fairness concerns (Major — Experimental Design).** BCE-only at 28.16 PPL is dramatically worse than training-free TEAL (12.48 PPL). A trained predictor performing 2.3x worse than a zero-parameter heuristic is anomalous and suggests implementation issues rather than a fundamental loss function limitation. Several possible confounds:
50	   - (a) BCE was trained with Gumbel-sigmoid relaxation, which is designed for continuous-valued losses. For a binary classification objective, STE is the natural relaxation. The STE+BCE condition is never tested.
51	   - (b) The BCE target (top-k by activation magnitude) is itself suboptimal — it ignores downstream output impact. KL implicitly discovers better masks through end-to-end gradients. Much of the gap may be target quality, not loss quality.
52	   - (c) The actual MVP data (bce_mvp_3seed_analysis.md) reports BCE dense PPL of 28.16, which is puzzling — the true dense Llama 3.1 8B PPL should be ~6.12. This suggests the BCE evaluation may use a different protocol or there is a measurement artifact.
53	   - (d) BCE+comp at 18.64 is still worse than TEAL (12.48). In the FastForward paper, BCE+comp reportedly approaches dense quality. The enormous gap here again suggests the BCE pipeline may not be properly implemented or tuned.
54	
55	### Moderate
56	
57	5. **Related work section is severely underdeveloped (Moderate — Related Work).** Only 8 references in the bibliography. For a paper in the activation sparsity space in 2026, this is inadequate. Critical missing citations include:
58	   - **Deja Vu (Liu et al., ICML 2023)**: The foundational work on BCE-trained contextual sparsity predictors. Not citing this is a major gap.
59	   - **CATS (Lee et al., 2024)**: Contextual thresholding for SwiGLU models — a direct competitor.
60	   - **Minitron (Muralidharan et al., NeurIPS 2024)**: KL distillation for structured pruning, directly validates logit-only KL superiority. Listed in the project's own literature map but absent from the paper.
61	   - **DIP (Federici et al., MLSys 2025)**: Predictor-free dynamic pruning for SwiGLU — demonstrates the difficulty of predicting SwiGLU sparsity patterns.
62	   - **Gumbel-Softmax foundations (Jang et al., 2017; Maddison et al., 2017)**: The relaxation technique used is never properly cited.
63	   - **Knowledge distillation foundations**: Only Hinton et al. (2015) is cited. Missing: FitNets, attention transfer, and modern distillation work relevant to the coupling argument.
64	   - **Sparsing Law (Luo et al., 2024)**: Theoretical foundation for why SwiGLU models lack natural sparsity.
65	   - **ReLU Strikes Back, TurboSparse, ProSparse**: Alternative approaches that modify activation functions — needed for complete positioning.
66	   - **L0 regularization (Louizos et al., 2018)**: The Gumbel-sigmoid mechanism for discrete mask learning is closely related.
67	
68	6. **Quadratic scaling claim is post-hoc curve fitting presented as theoretical prediction (Moderate — Claim Calibration).** The O(s^2 D^2) argument conflates the count of neuron pairs with the magnitude of their gradient interaction. The actual KL-BCE gap depends on the spectral properties of the Jacobian W_d, the distribution of neuron activations, and the correlation structure of the mask — not merely the combinatorial count of pairs. Fitting Delta = as^2 to 7 single-seed data points with R^2 = 0.97 is suggestive but not definitive. Many monotonically increasing functions (power law, exponential onset, logistic) would fit 7 points with comparable R^2. No AIC/BIC model comparison is reported. Calling this a "testable theoretical prediction" overstates what is actually an empirical regularity observed on limited data.
69	
70	7. **"Eliminates" in the title overclaims (Moderate — Claim Calibration).** The title claims compensation is "eliminated," but this is demonstrated on exactly two 7-8B models at a single sparsity level (50%). Whether compensation remains unnecessary at 70%+ sparsity, at 70B+ scale, or on non-SwiGLU architectures is unknown. "Reduces the need for" or "subsumes" would be more accurate for the evidence presented.
71	
72	### Minor
73	
74	8. **Unequal seed counts across conditions (3 vs. 5) are unusual and unexplained.** BCE-only has 3 seeds, KL-only has 5, BCE+comp has 5, KL+comp has 3. Standard practice is equal seeds across all conditions for fair comparison.
75	
76	9. **Sparsity enforcement mechanism (Lagrangian multiplier) is underreported.** The decisions.yaml reveals substantial engineering effort to make KL training work at all (sparsity collapse to 0%, multiple failed attempts, normalization bug). The final Lagrangian setup with exponential updates is a non-trivial training recipe that gives KL a more sophisticated optimization landscape than vanilla BCE. This asymmetry in training sophistication should be discussed.
77	
78	10. **Calibration data sensitivity not analyzed.** Training uses WikiText-103 (narrow domain); no analysis of how calibration data choice affects results. The decisions log shows the original plan used SlimPajama-627B but was switched due to access issues — this is a potentially consequential change.
79	
80	---
81	
82	## Questions for Authors
83	
84	1. **What happens with MSE on output logits as the training loss?** This is the most important missing experiment. If MSE-logits achieves comparable results, the gradient coupling argument is confirmed but the KL-specific framing must change.
85	
86	2. **Why is BCE-only (28.16) worse than training-free TEAL (12.48)?** Please explain this anomaly. Was BCE trained with Gumbel-sigmoid? What happens with STE+BCE? Were hyperparameters tuned comparably?
87	
88	3. **The BCE MVP analysis shows "dense PPL" of 28.16 — how is this possible when true dense PPL is 6.12?** This suggests the evaluation protocol differs between conditions. Please clarify.
89	
90	4. **What is the BCE oracle target?** Is it top-k by activation magnitude? If so, how does KL's implicitly learned target differ, and how much of the gap is attributable to target quality vs. loss function quality?
91	
92	5. **How sensitive is the Lagrangian sparsity enforcement to its hyperparameters?** The development history shows sparsity collapse was a major challenge. Is the final recipe robust, or does it require careful tuning per model?
93	
94	6. **At what sparsity level does KL-only start to need compensation?** The paper shows compensation adds only 0.18 PPL at 50% — what about at 60%, 70%?
95	
96	---
97	
98	## Missing Related Work and Positioning Issues
99	
100	The related work section needs substantial expansion. Specific gaps:
101	
102	1. **Deja Vu** is the foundational work for BCE-trained contextual sparsity predictors and must be cited and discussed. The paper references "FastForward-style" approaches but never cites the originating work.
103	
104	2. **The knowledge distillation literature** is engaged superficially. The paper should discuss: (a) why forward KL rather than reverse KL, (b) temperature scaling (standard in KD, absent here), (c) the relationship to feature-based vs. logit-based distillation, which maps onto the intermediate-MSE vs. coupled-KL axis of the taxonomy.
105	
106	3. **MoE routing** literature is entirely absent. Mixture-of-experts models face an analogous problem: routing tokens to expert subsets while preserving output quality. Load balancing losses in MoE (e.g., Switch Transformer's auxiliary loss) are conceptually related to the sparsity enforcement mechanism here. This connection would strengthen the paper's positioning.
107	
108	4. **L0 regularization and the Concrete distribution** (Louizos et al., 2018) — the Gumbel-sigmoid mechanism for learning discrete masks is directly derived from this line of work and should be cited.
109	
110	5. **Structured pruning with distillation** (beyond Minitron): ShearedLLaMA, Wanda, and other recent structured pruning methods that use output-distribution matching should be discussed to properly contextualize the "KL for sparsity" idea.
111	
112	---
113	
114	## Novelty Assessment
115	
116	The paper sits at the intersection of two established techniques: KL distillation (standard since Hinton 2015) and learned sparsity prediction (standard since Deja Vu 2023). SPON already demonstrated KL works for sparsity in SwiGLU LLMs. The step from "KL for static bias correction" to "KL for contextual prediction" is natural and expected. The gradient coupling analysis, while correct, follows trivially from the chain rule and applies to any output-level loss.
117	
118	The most novel contribution is the modular decomposition (SPON + KL composition with orthogonality analysis), but this is positioned as Claim 2 rather than the headline. The quadratic scaling prediction, while interesting, is insufficiently supported theoretically.
119	
120	For a venue with ~25% acceptance rate, the novelty bar requires either (a) a genuinely new technique, or (b) a surprising empirical finding with deep analysis. The paper provides (b) in terms of effect size but not in terms of analytical depth. The missing MSE-logits baseline, the questionable BCE fairness, and the thin theoretical treatment prevent it from clearing the bar.
121	
122	---
123	
124	## Overall Score: 3/6 (Weak Reject)
125	
126	**Confidence: 4/5** — I am confident in the novelty and positioning assessment. The one area of uncertainty is whether the BCE baseline weakness reflects a real phenomenon or an implementation issue, which could shift the score in either direction.
127	
128	**Justification:** The paper identifies a real and practically important phenomenon — KL-trained sparsity predictors dramatically outperform BCE-trained ones. The effect size is large, the ablation design is thoughtful, and the evaluation is comprehensive. However, the core contribution is a loss function swap in an existing pipeline, the gradient coupling theory is trivial (applies to any output-level loss), the most critical baseline (MSE-logits) is missing, the BCE comparison raises fairness concerns, and the related work is severely underdeveloped. The modular decomposition is the strongest original element but is undersold. As written, the paper provides useful empirical knowledge but insufficient novelty or analytical depth for a top venue.
129	
130	**What would change the score:**
131	- MSE-logits baseline showing KL uniquely dominates: +1 (to 4/6)
132	- BCE fairness concerns resolved (STE+BCE tested, target quality confound addressed): +0.5
133	- Adequate related work (20+ well-discussed references): +0.5
134	- Modular decomposition promoted to co-headline with deeper orthogonality theory: +0.5
135	- If MSE-logits matches KL: -0.5 (requires complete reframing)
136	- If BCE implementation found unfair: -1 (to 2/6)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da64a3d2-fa5b-4836-8bd6-d4bbb427d5db",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "efb3f50f-4846-4473-84ce-d99758065033",
  "sourceToolAssistantUUID": "da64a3d2-fa5b-4836-8bd6-d4bbb427d5db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T17:54:18.579Z_

Now let me read the worst-case paper and the paper framing documents for a complete picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efb3f50f-4846-4473-84ce-d99758065033",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMw6BQn3vGVk1F4bi5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12cf8d33-3b8b-4249-ad26-e14c6ca1262a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiV3zyczRRShH8mWVqJKb2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8829,
      "cache_read_input_tokens": 59438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8829,
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

_source line 42 · 2026-05-15T17:54:20.905Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RUvR5CDMQm8aW7LKWVYHcM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12cf8d33-3b8b-4249-ad26-e14c6ca1262a",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMw6BQn3vGVk1F4bi5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f428c565-1be9-424d-ad3a-106ed3e7c23d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiV3zyczRRShH8mWVqJKb2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8829,
      "cache_read_input_tokens": 59438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8829,
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

_source line 43 · 2026-05-15T17:54:20.916Z_

<details><summary>↩ Tool result · `toolu_01RUvR5CDMQm8aW7LKWVYHcM`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{hyperref}
11	\usepackage{natbib}
12	\usepackage{array}
13	\usepackage{makecell}
14	
15	\newcommand{\method}{SwiGLU}
16	\newcommand{\ours}{KL-Sparse}
17	
18	\title{Training Signal Meets Correction Granularity:\\A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs}
19	
20	\author{Anonymous}
21	
22	\date{}
23	
24	\begin{document}
25	
26	\maketitle
27	
28	\begin{abstract}
29	Activation sparsity in SwiGLU-based large language models enables significant inference speedup by pruning inactive neurons, but the landscape of training signals (BCE, KL divergence) and correction mechanisms (none, static bias, contextual compensation) remains fragmented and poorly understood.
30	We present the first systematic characterization study spanning this two-dimensional design space---training signal coupling $\times$ correction granularity---evaluated on Llama~3.1~8B and Mistral-7B-v0.3 across 12~benchmarks including WikiText-2, MMLU, LongBench, MT-Bench, and RULER.
31	Our findings challenge the prevailing assumption that KL-trained predictors eliminate the need for compensation networks.
32	We show that: (1)~BCE with a lightweight compensation MLP (PPL~9.40$\pm$0.19) matches or outperforms KL-only training (PPL~9.80$\pm$0.87) at 50\% sparsity, with substantially lower seed variance; (2)~static (SPON) and contextual corrections are non-additive (additivity ratio = 0.62), targeting overlapping error modes; (3)~the KL--BCE gap does not follow the predicted $s^2$ scaling ($R^2 = 0.66$); and (4)~BCE+compensation advantage \emph{increases} on Mistral-7B (+1.35 PPL gap vs.\ +0.40 on Llama).
33	These results reframe the contribution of KL divergence from ``eliminating compensation'' to ``one cell in a broader taxonomy,'' and reveal that compensation mechanisms provide architecture-robust quality recovery that KL alone cannot guarantee.
34	\end{abstract}
35	
36	\section{Introduction}
37	
38	SwiGLU activation functions, now standard in modern LLMs such as Llama~3 and Mistral, produce naturally sparse intermediate representations.
39	Exploiting this sparsity at inference time---by predicting and pruning near-zero neurons before the expensive up-projection GEMM---can yield 1.3--1.4$\times$ wall-clock speedup with moderate quality loss.
40	
41	The design space for learned sparsity predictors spans two orthogonal axes.
42	The first axis is the \emph{training signal}: decomposed losses like binary cross-entropy (BCE), which supervise each neuron independently, versus coupled losses like KL divergence, which match full output distributions and implicitly capture joint neuron interactions.
43	The second axis is \emph{correction granularity}: whether quality is recovered through no correction, a static input-independent bias (as in SPON), or a contextual per-layer compensation MLP (as in FastForward).
44	
45	Prior work has explored isolated cells in this taxonomy---SPON uses KL training with static correction, FastForward uses BCE with contextual compensation---but no systematic comparison across the full space exists.
46	A natural hypothesis, motivated by the gradient structure of KL divergence ($\partial \mathcal{L}_{\text{KL}} / \partial s_j$ couples all active neurons through the Jacobian), is that KL training should subsume the role of compensation networks: if the predictor already accounts for joint interactions, explicit post-hoc correction becomes redundant.
47	
48	We test this hypothesis through a comprehensive set of experiments and find that it does \emph{not} hold.
49	Our contributions are:
50	
51	\begin{enumerate}
52	\item \textbf{A two-dimensional taxonomy} of training signals $\times$ correction granularity for activation sparsity, positioning prior methods (TEAL, SPON, FastForward) and our configurations in a unified framework.
53	
54	\item \textbf{A four-condition ablation} showing that BCE+compensation (PPL~9.40) outperforms KL-only (PPL~9.80) at 50\% sparsity, with 4.6$\times$ lower seed variance (0.19 vs.\ 0.87), demonstrating that the bottleneck in BCE training is the absence of compensation, not the loss function itself.
55	
56	\item \textbf{Negative results on three prior hypotheses}: (a)~SPON+KL corrections are non-additive (ratio = 0.62), (b)~the KL--BCE gap does not follow $s^2$ scaling ($R^2 = 0.66$, with linear fit equally good at $R^2 = 0.68$), and (c)~KL advantage does not generalize across architectures (direction reversal on Mistral-7B).
57	
58	\item \textbf{Comprehensive evaluation} across 12 benchmarks, two architectures, and two context-length regimes, establishing a quality--efficiency Pareto frontier for the full design space.
59	\end{enumerate}
60	
61	
62	\section{Background and Related Work}
63	
64	\paragraph{Activation sparsity in SwiGLU.}
65	The SwiGLU activation $h = (\text{Silu}(xW_g)) \odot (xW_u)$ produces intermediate representations where a substantial fraction of neurons have near-zero magnitude. Training-free methods exploit this by pruning low-magnitude neurons at inference. TEAL uses activation magnitude with greedy per-layer allocation. R-Sparse employs rank-aware scoring. WINA incorporates weight information. These methods require no additional training but leave a significant quality gap (6+ PPL points at 50\% sparsity).
66	
67	\paragraph{Learned sparsity prediction.}
68	FastForward trains a contextual predictor with BCE loss to predict per-neuron activation masks, paired with a compensation MLP that corrects the output error introduced by pruning. SPON learns a static (input-independent) bias per layer via KL distillation, incurring zero inference overhead but limited by its inability to adapt to per-input variation.
69	
70	\paragraph{KL divergence for sparsity.}
71	KL-based training matches the full output distribution between the sparse and dense models. The gradient $\partial \mathcal{L}_{\text{KL}} / \partial s_j$ couples all neurons through the Jacobian $\partial \text{logits} / \partial h \cdot \partial h / \partial m$, in contrast to BCE where $\partial \mathcal{L}_{\text{BCE}} / \partial s_j$ depends only on neuron $j$. This coupling motivates the hypothesis that KL training captures joint interactions that BCE misses.
72	
73	\paragraph{Gumbel-sigmoid relaxation.}
74	To backpropagate through discrete mask decisions, we use the Gumbel-sigmoid reparameterization with temperature annealing. We also evaluate Straight-Through Estimator (STE) as an alternative gradient pathway to isolate the contribution of the relaxation method from the loss function.
75	
76	
77	\section{Method}
78	
79	\subsection{Two-Dimensional Design Space}
80	
81	We organize the landscape of learned activation sparsity along two axes (Table~\ref{tab:taxonomy}):
82	
83	\begin{table}[h]
84	\centering
85	\caption{Two-dimensional taxonomy of activation sparsity methods. Each cell indicates the method occupying that position. Bold indicates configurations evaluated in this work.}
86	\label{tab:taxonomy}
87	\small
88	\begin{tabular}{l ccc}
89	\toprule
90	& Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
91	\midrule
92	Static & --- & --- & SPON \\
93	Per-layer & --- & ShadowLLM & --- \\
94	Per-token contextual & FastForward & --- & \textbf{Ours} \\
95	\bottomrule
96	\end{tabular}
97	\end{table}
98	
99	\noindent\textbf{Training signal axis} captures how the loss function couples neuron decisions: BCE treats each neuron independently (decomposed), while KL couples all neurons through output-distribution matching (coupled).
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f428c565-1be9-424d-ad3a-106ed3e7c23d",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "b30bfeb8-52d1-4037-948b-527437b333a5",
  "sourceToolAssistantUUID": "f428c565-1be9-424d-ad3a-106ed3e7c23d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T17:54:21.614Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R8QvcEs99NGTUhjfdadror`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b30bfeb8-52d1-4037-948b-527437b333a5",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nMw6BQn3vGVk1F4bi5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe367254-47d9-4487-9fa4-30f4a47663c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BiV3zyczRRShH8mWVqJKb2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8829,
      "cache_read_input_tokens": 59438,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8829
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 59438,
          "cache_creation_input_tokens": 8829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8829,
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

_source line 45 · 2026-05-15T17:54:21.618Z_

<details><summary>↩ Tool result · `toolu_01R8QvcEs99NGTUhjfdadror`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'Four-condition ablation @ 50% model-level sparsity on Llama 3.1 8B:
5	    (a) BCE-only, (b) BCE+compensation, (c) KL-only, (d) KL+compensation. Headline
6	    comparison: KL-only vs BCE+comp (5 seeds each). Secondary comparisons: 3 seeds
7	    each. MVP already completed KL-only 3 seeds (mvp_kl_norm_v2_s42/s123/s456) and
8	    BCE-only 3 seeds (mvp_bce_s42/s123/s456).
9	
10	    '
11	  priority: P0
12	  gpu_budget_hours: 48
13	  deps: []
14	  registry_ids:
15	  - mvp_kl_norm_v2_s42
16	  - mvp_kl_norm_v2_s123
17	  - mvp_kl_norm_v2_s456
18	  - mvp_bce_s42
19	  - mvp_bce_s123
20	  - mvp_bce_s456
21	  remaining_runs:
22	  - KL-only 2 additional seeds (s0, s1) for 5-seed headline
23	  - BCE+comp 5 seeds (s42, s123, s456, s0, s1)
24	  - KL+comp 3 seeds (s42, s123, s456)
25	  registry_id: kl_only_s1
26	- id: plan_002
27	  claim: 1
28	  description: 'STE baseline: KL loss + Straight-Through Estimator (instead of Gumbel-sigmoid).
29	    Isolates whether KL advantage comes from loss function or relaxation method. 3
30	    seeds.
31	
32	    '
33	  priority: P0
34	  gpu_budget_hours: 10
35	  deps:
36	  - plan_001
37	- id: plan_003
38	  claim: 1
39	  description: 'Iso-compute comparison: extend BCE training to match KL total FLOPs
40	    (KL requires full forward pass for output logits, BCE can use cached targets).
41	    Report per-step FLOPs and total training time for both. 3 seeds.
42	
43	    '
44	  priority: P0
45	  gpu_budget_hours: 10
46	  deps:
47	  - plan_001
48	- id: plan_004
49	  claim: 2
50	  description: 'SPON reimplementation on Llama 3.1 8B: learnable bias vectors + KL
51	    training. Validate by reproducing SPON published results on 5 QA benchmarks (ARC-c,
52	    ARC-e, BoolQ, PIQA, WinoGrande) before composition experiment.
53	
54	    '
55	  priority: P0
56	  gpu_budget_hours: 8
57	  deps: []
58	- id: plan_005
59	  claim: 2
60	  description: 'SPON + KL predictor composition experiment. Apply SPON bias correction
61	    AND KL contextual prediction simultaneously. Output-space linearity test: ||Delta_logits(s+c)
62	    - Delta_logits(s) - Delta_logits(c)|| vs individual magnitudes. Per-layer orthogonality
63	    analysis. 3 seeds.
64	
65	    '
66	  priority: P0
67	  gpu_budget_hours: 8
68	  deps:
69	  - plan_001
70	  - plan_004
71	- id: plan_006
72	  claim: 1
73	  description: 'Training-free baselines @ 50% model-level sparsity on Llama 3.1 8B:
74	    TEAL (magnitude pruning + greedy allocation), WINA (weight-informed scoring),
75	    R-Sparse (rank-aware scoring). Establishes three-tier comparison: training-free
76	    < static-learned < contextual-learned.
77	
78	    '
79	  priority: P0
80	  gpu_budget_hours: 6
81	  deps: []
82	- id: plan_007
83	  claim: 1,2,3
84	  description: 'Full benchmark evaluation of all conditions on Llama 3.1 8B: WikiText-2
85	    PPL, C4 PPL, ARC-c, WinoGrande, MMLU, GSM8K, HumanEval. Wall-clock profiling (predictor
86	    overhead, sparse GEMV savings, end-to-end latency). Efficiency-accuracy Pareto
87	    frontier plot.
88	
89	    '
90	  priority: P0
91	  gpu_budget_hours: 24
92	  deps:
93	  - plan_001
94	  - plan_004
95	  - plan_005
96	  - plan_006
97	- id: plan_008
98	  claim: 3
99	  description: '7-level sparsity sweep (30/35/40/45/50/55/60%): KL-only vs BCE-only.
100	    Test quantitative prediction: KL-BCE delta ~ s^2. 1 seed per level (sweep analysis,
101	    not headline). 50% data point reused from plan_001. Taylor expansion accuracy
102	    test at each level.
103	
104	    '
105	  priority: P1
106	  gpu_budget_hours: 30
107	  deps:
108	  - plan_001
109	- id: plan_009
110	  claim: 1
111	  description: 'Mistral-7B-v0.3 generalization validation. KL-only vs BCE+comp @ 50%
112	    model-level sparsity. Core benchmarks only: WikiText-2 PPL, ARC-c, MMLU. 3 seeds
113	    each condition.
114	
115	    '
116	  priority: P1
117	  gpu_budget_hours: 24
118	  deps:
119	  - plan_001
120	- id: plan_010
121	  claim: 1,2
122	  description: 'LongBench English subset evaluation (4K-32K tokens). All conditions
123	    (KL-only, BCE+comp, SPON, SPON+KL, training-free baselines). Per-task-type breakdown:
124	    single-doc QA, multi-doc QA, summarization, few-shot, code. Tests predictor generalization
125	    beyond short training sequences.
126	
127	    '
128	  priority: P1
129	  gpu_budget_hours: 16
130	  deps:
131	  - plan_001
132	  - plan_005
133	- id: plan_011
134	  claim: 1,2
135	  description: 'MT-Bench evaluation with GPT-4o judge. 80 multi-turn questions, 8
136	    categories. All conditions. Tests instruction-following quality under sparsity.
137	
138	    '
139	  priority: P2
140	  gpu_budget_hours: 4
141	  deps:
142	  - plan_001
143	  - plan_005
144	- id: plan_012
145	  claim: 3
146	  description: 'RULER synthetic long-context evaluation (4K, 16K) x 3 representative
147	    task types. Fine-grained capability diagnostics complementing LongBench.
148	
149	    '
150	  priority: P2
151	  gpu_budget_hours: 8
152	  deps:
153	  - plan_010
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe367254-47d9-4487-9fa4-30f4a47663c1",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "59e40683-04c4-4720-9109-90b7e59d5965",
  "sourceToolAssistantUUID": "fe367254-47d9-4487-9fa4-30f4a47663c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-15T17:54:25.627Z_

Now I have a thorough understanding of all three scenario papers, the project state, the literature map, and the experiment plans. Let me now load the submission tool to post my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e40683-04c4-4720-9109-90b7e59d5965",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nNcNaKPkXLJLKXL4p7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04c95fde-6456-4ab2-8253-4cb62f070689",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHfqXE2gMTm8iCvi1X6JRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4603,
      "cache_read_input_tokens": 68267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4603,
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

_source line 47 · 2026-05-15T17:54:26.168Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AtJTcVD6x4Z1sZX3C6SnnK`</summary>

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
  "parentUuid": "04c95fde-6456-4ab2-8253-4cb62f070689",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nNcNaKPkXLJLKXL4p7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5abf9559-e112-4233-8ce8-4ed57943ed01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHfqXE2gMTm8iCvi1X6JRG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4603,
      "cache_read_input_tokens": 68267,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 68267,
          "cache_creation_input_tokens": 4603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4603,
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

_source line 48 · 2026-05-15T17:54:26.175Z_

<details><summary>↩ Tool result · `toolu_01AtJTcVD6x4Z1sZX3C6SnnK`</summary>

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
  "parentUuid": "5abf9559-e112-4233-8ce8-4ed57943ed01",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "18611525-b8f3-4e5d-972b-75f46ebb2fb5",
  "sourceToolAssistantUUID": "5abf9559-e112-4233-8ce8-4ed57943ed01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-15T17:56:38.846Z_



Now I have a comprehensive understanding of the project. Let me note that the user's prompt describes a paper that closely matches the **worst-case scenario** paper (the one with title "Training Signal Meets Correction Granularity: A Systematic Taxonomy..."), where BCE+comp actually outperforms KL-only. The numbers in the user's summary (BCE+comp PPL 9.40±0.19, KL-only 9.80±0.87, additivity ratio 0.62, R²=0.66) match the worst-case paper exactly.

I have also read the best-case and median-case papers, the prior dream reviews (which reviewed the best/median tiers), the literature map, the paper framing, the experiment plan, and the project decisions. I am now ready to produce a thorough R2 review focused on novelty, significance, positioning, and writing quality.

Here is my structured review:

---

## R2 Review -- Novelty, Significance, Positioning, and Writing Quality

**Paper:** "Training Signal Meets Correction Granularity: A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs"

**Reviewer:** R2 (Novelty + Related Work focus)

**Score:** 3/6 (Weak Reject)

**Confidence:** 4/5

---

### 1. Summary

The paper presents a two-dimensional taxonomy (training signal x correction granularity) for learned activation sparsity in SwiGLU LLMs and conducts a systematic empirical study filling the previously unoccupied cell (per-token contextual + KL). Contrary to the natural hypothesis motivated by KL's gradient coupling, the paper finds that BCE+compensation (PPL 9.40 +/- 0.19) matches or slightly outperforms KL-only (PPL 9.80 +/- 0.87) at 50% sparsity on Llama 3.1 8B, while exhibiting 4.6x lower variance. The paper reports three negative results: non-additive SPON+KL composition, failure of s^2 scaling for the KL-BCE gap, and reversal of the KL advantage on Mistral-7B.

---

### 2. Strengths

- **Well-structured characterization study with principled ablation design.** The four-condition matrix (loss x compensation), STE isolation (Table 4), iso-compute comparison (Table 5), and SPON composition analysis form a rigorous experimental scaffolding. Each ablation targets a specific confound. This level of systematic control exceeds the norm for the activation sparsity subfield.

- **Honest reporting of negative results.** The paper set out to show KL eliminates compensation and found the opposite. Publishing this with full transparency (additivity ratio 0.62, R^2 = 0.66, direction reversal on Mistral) is scientifically valuable. The reframing from "KL eliminates compensation" to "compensation is the universal mechanism" is intellectually honest and potentially more useful to practitioners than a positive result would be.

- **Comprehensive evaluation breadth.** 12 benchmarks across perplexity, discriminative tasks, long-context (LongBench, RULER), instruction-following (MT-Bench), inference profiling, and cross-architecture validation. The per-task-type breakdowns (LongBench Table 16, RULER Table 18) are appropriately granular.

- **Variance as a first-class metric.** Reporting that KL-only has 4.6x higher seed variance than BCE+comp (0.87 vs 0.19) is an underappreciated contribution. For deployment, predictability matters as much as mean performance. This finding has immediate practical implications.

- **The taxonomy has genuine organizational value.** Table 1 clearly maps prior work (SPON, ShadowLLM, FastForward) and identifies the empty cell. Even if it is not a deep theoretical contribution, it provides a useful mental model for the field and will likely be cited.

- **Inference cost co-reported with quality.** Table 11 (1.35x/48MB for KL-only vs 1.19x/304MB for BCE+comp) ensures claims are grounded in deployment reality. The observation that BCE+comp's compensation overhead partially negates sparsity gains is practically important.

---

### 3. Weaknesses

#### 3.1 Major

**(W1) The core contribution is a characterization study with no new method, which faces a steep novelty bar at a top venue.**

The paper introduces no new architecture, no new training algorithm, and no new theoretical framework. The taxonomy is organizational; the experiments combine existing components (Gumbel-sigmoid predictor, KL/BCE losses, SPON bias correction, compensation MLP). The most technically involved element -- the Lagrangian sparsity enforcement for KL training -- is underspecified (see W6). For a venue with ~25% acceptance rate, characterization studies must compensate with either (a) deeply surprising findings that overturn community assumptions or (b) analytical depth that explains *why* the observed patterns occur. The paper achieves (a) partially (the negative result on KL is mildly surprising, but not many people held the strong prior that KL eliminates compensation -- SPON is the only prior work in this space, and it addressed static correction, not contextual). It does not achieve (b): the discussion of *why* BCE+comp outperforms KL-only (Section 6) is speculative and does not go beyond restating the empirical observations.

**(W2) The gradient coupling argument is presented but then empirically refuted, creating a narrative tension the paper does not resolve.**

Section 3 motivates KL via gradient coupling: KL's gradient couples all neurons through the Jacobian while BCE factorizes. This is mathematically correct but is a property of ANY output-level loss, not uniquely KL (MSE on logits, JS divergence, reverse KL would all exhibit the same coupling). More importantly, the paper's own results show this coupling does NOT translate to better quality -- BCE+comp beats KL-only. The paper acknowledges this but attributes it to "Lagrangian instability" and "phase transitions" (Section 6) without rigorous evidence. The disconnect between the theoretical motivation (Section 3) and the empirical outcome (Section 5) is the paper's central intellectual weakness. A stronger paper would either (a) provide a theoretical explanation for why coupling in the gradient is necessary but not sufficient, or (b) identify the specific failure mode of KL training that compensation circumvents.

**(W3) Missing MSE-on-logits baseline undermines the gradient coupling narrative.**

The gradient coupling property that Section 3 highlights applies identically to MSE on output logits. Without this baseline, the paper cannot determine whether KL's specific properties (distributional matching, information-geometric structure) matter at all, or whether any output-level loss would perform similarly. Given that the paper frames its contribution around the training signal axis of the taxonomy, this omission is critical. If MSE-logits performs comparably to KL, the taxonomy's "Intermediate (MSE)" column should have a per-token contextual entry, which would change the landscape entirely. This is a single experiment that would substantially strengthen the paper regardless of outcome.

**(W4) BCE baseline fairness is questionable.**

BCE-only achieves 28.16 PPL (Table 2), which is 2.25x worse than training-free TEAL (estimated ~12-13 PPL from the baselines section). A *trained* predictor performing dramatically worse than a zero-parameter magnitude heuristic is anomalous. Several concerns:

- Was BCE trained with Gumbel-sigmoid? Gumbel-sigmoid is designed for continuous losses. For a binary target, STE is the natural relaxation. The STE ablation (Table 4) tests STE+KL but never STE+BCE, creating an asymmetry.
- How are BCE oracle targets generated? If by top-k activation magnitude, the targets themselves are suboptimal. KL implicitly discovers better masks. The gap may partly reflect target quality, not loss quality.
- The project's decision log (D003-D006) reveals that KL training required substantial engineering effort (Lagrangian multiplier, normalization debugging, multiple failed attempts). Did BCE receive comparable engineering attention?
- In the FastForward paper, BCE+comp reportedly approaches dense quality. The fact that BCE+comp here (9.40) is still 3.28 PPL above dense (6.12) at 50% sparsity is plausible but needs explicit comparison with FastForward's reported numbers to establish fairness.

Without a BCE+STE condition and transparency about target generation, the BCE baseline's weakness is a confound that taints the entire study.

#### 3.2 Moderate

**(W5) Related work is severely underdeveloped for a paper claiming a taxonomic contribution.**

A paper whose headline contribution is a taxonomy must comprehensively survey the field. The current related work is too thin. Critical missing citations:

- **Deja Vu (Liu et al., ICML 2023)**: Foundational work on BCE-trained contextual sparsity predictors. The paper references "FastForward-style" approaches but omits the originating work.
- **CATS (Lee et al., 2024)**: Contextual thresholding for SwiGLU -- a direct competitor that should appear in Table 1 or be discussed.
- **Minitron (Muralidharan et al., NeurIPS 2024)**: KL distillation for structured pruning, directly validates logit-only KL superiority. Present in the project's own literature map but absent from the paper.
- **DIP (Federici et al., MLSys 2025)**: Predictor-free dynamic pruning for SwiGLU, demonstrates the difficulty of SwiGLU sparsity prediction.
- **Gumbel-Softmax/Sigmoid foundations (Jang et al., 2017; Maddison et al., 2017)**: The relaxation technique is never properly cited.
- **L0 regularization (Louizos et al., 2018)**: Closely related to learned binary masks via Gumbel-sigmoid.
- **Sparsing Law (Luo et al., 2024)**: Theoretical foundation for why SwiGLU models lack natural sparsity.
- **ReLU Strikes Back, TurboSparse, ProSparse**: Alternative approaches via activation function replacement needed for complete positioning.
- **MoE routing literature**: Per-token expert selection is structurally identical to per-token neuron selection; load-balancing losses are conceptually related to sparsity enforcement.
- **Knowledge distillation foundations beyond Hinton 2015**: FitNets, attention transfer, and modern work on feature vs. logit distillation directly map to the intermediate-MSE vs. coupled-KL axis.

**(W6) Lagrangian sparsity enforcement mechanism is underspecified.**

The project history reveals this was the make-or-break engineering challenge: KL training collapsed to 0% sparsity (D003), required normalization fixes (D004), had a bug that produced false positive results (D006), and took multiple iterations to stabilize. Yet the paper does not fully specify lambda initialization, update schedule, clamping bounds, or sensitivity analysis. This is critical for reproducibility. Moreover, the Lagrangian mechanism gives KL a substantially more sophisticated optimization landscape than vanilla BCE, creating an asymmetry in training infrastructure that the paper does not discuss.

**(W7) Statistical rigor is insufficient for the claims made.**

- Unequal seed counts (3 vs 5) across conditions with no justification.
- The headline comparison (BCE+comp 9.40 +/- 0.19 vs KL-only 9.80 +/- 0.87) has overlapping confidence intervals. No formal significance test (paired bootstrap, permutation test, Welch's t-test) is reported.
- The sparsity sweep uses 1 seed per level. The R^2 = 0.66 for the quadratic fit is reported as evidence *against* s^2 scaling, but with 7 single-seed points, the noise floor is too high to distinguish between functional forms. No AIC/BIC model comparison is provided.
- Additivity ratio = 0.62 is reported without confidence intervals or a statistical test for whether it differs from 1.0.

**(W8) The "phase transitions vs scaling laws" framing (Section 6) is speculative.**

The paper argues that architecture-specific phase transitions explain the failure of s^2 scaling. This is asserted without evidence: no phase transition is demonstrated (e.g., via a sharp discontinuity in a relevant quantity), no theoretical mechanism is proposed, and "phase transition" is used loosely. The discussion reads as post-hoc rationalization of R^2 = 0.66 rather than a genuine scientific claim.

#### 3.3 Minor

**(W9) Only 7-8B scale tested.** The "compensation is universal" claim is validated at a single model scale. The gradient coupling argument predicts scale-dependent behavior (coupling through W_d depends on the spectral properties of the down-projection, which change with scale). A testable prediction about larger scales should at minimum be stated.

**(W10) Calibration data sensitivity unexamined.** Training uses WikiText-103 (as per D002), evaluation is on WikiText-2. No analysis of domain sensitivity. Given known OOD fragility of learned sparsity predictors, and given the forced switch from SlimPajama to WikiText-103, this is a meaningful gap.

**(W11) 512-token training sequences acknowledged as limitation but not analyzed.** The LongBench and RULER evaluations show increased degradation at longer contexts. Training on longer sequences as a control would determine whether this is a fundamental limit or a training artifact.

---

### 4. Questions for Authors

1. **What happens with MSE on output logits as the training loss?** This is the single most informative missing experiment. If MSE-logits matches KL, the gradient coupling narrative is confirmed but is not KL-specific. If MSE-logits is substantially worse, KL's distributional properties are uniquely important. Either outcome strengthens the paper.

2. **Was BCE trained with Gumbel-sigmoid relaxation?** If so, what happens with STE+BCE? The STE ablation (Table 4) only varies KL's relaxation, never BCE's. This asymmetry must be resolved.

3. **How are BCE oracle targets generated?** Top-k by activation magnitude? If so, how do KL's implicitly learned masks differ from these targets, and how much of the gap is target quality vs loss quality?

4. **The headline PPL gap (9.40 vs 9.80) falls within overlapping standard deviations. Can you provide a formal significance test?** With 5 and 5 seeds respectively, a Welch's t-test is straightforward. If p > 0.05, the claim that "BCE+comp outperforms KL-only" must be softened to "matches."

5. **Why is BCE-only (28.16 PPL) worse than training-free TEAL?** This is the most anomalous result in the paper. If this reflects a genuine phenomenon (Gumbel-sigmoid actively harms BCE), it is itself an interesting finding that deserves analysis. If it reflects inadequate tuning, it undermines the entire comparison.

6. **What are the Lagrangian hyperparameters (lambda_init, update schedule, clamping)?** How sensitive is KL training to these settings? The decision log suggests substantial sensitivity.

7. **At what sparsity level does KL-only start to need compensation?** The paper shows KL+comp adds only marginal improvement at 50%. Does this hold at 60%? 70%?

8. **Can you explain the Mistral direction reversal mechanistically?** The paper notes BCE+comp advantage increases on Mistral (+1.35 vs +0.40), but the explanation ("different architecture") is circular. What specific property of GQA + sliding window attention drives this?

---

### 5. Detailed Comments on Novelty and Positioning

**Novelty assessment:** The paper sits at the intersection of two established techniques: KL distillation (standard since Hinton 2015) and learned sparsity prediction (standard since Deja Vu 2023). SPON already demonstrated KL works for sparsity correction in SwiGLU LLMs. Testing KL for contextual (rather than static) prediction is the natural next step that the paper's own taxonomy identifies as the empty cell. The gradient coupling analysis, while correct, follows trivially from the chain rule and applies to any output-level loss.

The most genuinely novel contribution is the negative result: that this natural hypothesis fails, and that compensation is the more robust mechanism. However, the negative result's impact is weakened by: (a) the narrow effect size (9.40 vs 9.80, potentially non-significant), (b) the unresolved BCE fairness concerns, and (c) the lack of a mechanistic explanation for *why* compensation succeeds where KL coupling fails.

**Positioning assessment:** Framing the paper as a "systematic taxonomy" and "characterization study" is the correct strategic choice given the results. The paper does not oversell -- it accurately presents negative findings and acknowledges limitations. However, the characterization is incomplete: the MSE-logits cell in the taxonomy is empty, the related work does not comprehensively map the field, and the discussion does not provide sufficient analytical depth to compensate for the absence of a new method.

**Comparison to related characterization studies at top venues:** Successful characterization/ablation studies at EMNLP/NeurIPS typically have either (a) a much larger scope (e.g., surveying dozens of methods across multiple tasks), (b) a deeply surprising finding that changes community assumptions, or (c) actionable guidelines backed by causal analysis. This paper has moderate scope (4 main conditions, 2 models), a mildly surprising finding (but with caveats about statistical significance and fairness), and limited causal analysis (the discussion is speculative).

---

### 6. Writing Quality

- **Overall organization is clear.** The taxonomy-first structure (Section 3) followed by systematic experiments (Section 5) is logical and easy to follow.
- **Claims are mostly well-calibrated to evidence.** The paper does not make claims beyond what the data supports, with the exception of the "phase transition" speculation in Section 6.
- **The narrative arc is slightly confused.** The introduction motivates KL via gradient coupling, then the results show KL does not win. This creates a bait-and-switch feeling. A cleaner structure would frame the question as genuinely open from the start ("we test whether KL's gradient coupling translates to practical advantage") rather than building up the KL hypothesis only to knock it down.
- **Table density is high.** 18 tables in 11 pages is at the upper limit of readability. Several tables (e.g., Tables 7-8 on SPON+KL non-additivity) could be merged.
- **The discussion section (Section 6) is the weakest part of the writing.** "Phase transitions vs scaling laws" and "Lagrangian instability" are invoked without supporting evidence. This section should either provide rigorous analysis or be substantially shortened.
- **Bibliography is too thin.** 8 references for a survey-style paper is inadequate.

---

### 7. Score and Recommendation

**Score: 3/6 (Weak Reject)**

**Confidence: 4/5** -- I am confident in the novelty and positioning assessment. The area of uncertainty is the BCE baseline fairness: if the anomalous BCE-only result (worse than TEAL) is an implementation artifact, the entire comparison framework is unreliable, which would push toward Reject. If it is a genuine phenomenon, the paper's findings are more interesting than they appear.

**Justification:** The paper asks a good question (does KL training eliminate compensation?) and provides an honest, well-structured empirical answer (no, it does not). The evaluation breadth is commendable, and reporting negative results has scientific value. However, the contribution faces three converging problems: (1) thin novelty (a loss function swap in an existing pipeline, where the taxonomy is organizational rather than technical), (2) unresolved experimental concerns (missing MSE-logits baseline, BCE fairness questions, insufficient statistical rigor for the narrow effect size), and (3) inadequate analytical depth (no mechanistic explanation for why compensation outperforms gradient coupling, speculative discussion section, severely underdeveloped related work). The paper provides useful empirical data points but does not clear the novelty-plus-depth bar for a ~25% acceptance rate venue.

**What would change the score:**
- MSE-logits baseline + BCE+STE control resolving fairness concerns: +0.5 to +1.0
- Mechanistic explanation for compensation's advantage over KL coupling (not speculation): +0.5
- Comprehensive related work (20+ well-discussed references): +0.5
- Formal significance tests showing the 9.40 vs 9.80 gap is robust: +0.5
- If BCE baseline found to be unfairly weak (implementation bug or inappropriate relaxation): -1.0 (to 2/6, Reject)

---

Now let me submit this review formally.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18611525-b8f3-4e5d-972b-75f46ebb2fb5",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nNwEdtCwLqFK5WzPEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76aba766-ace1-4a74-ace4-6ab76222b2d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiYGtSouG1UFnLv4pYZEpn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 72870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 706,
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

_source line 50 · 2026-05-15T17:57:21.672Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01TxvYGW3diBRePuGUbgWYxt`</summary>

```json
{
  "report": "---\ndream_id: dream_20260515T164925\ntier: worst\noverall_score: 3/6 Weak Reject\ntimestamp: 2026-05-15\n---\n\n# R2 Review — Novelty, Significance, Positioning, and Writing Quality\n\n**Paper:** \"Training Signal Meets Correction Granularity: A Systematic Taxonomy of Learned Activation Sparsity for SwiGLU LLMs\"\n**Reviewer:** R2 (Novelty & Related Work focus)\n**Score:** 3/6 (Weak Reject)\n**Confidence:** 4/5\n\n---\n\n## 1. Summary\n\nThe paper presents a two-dimensional taxonomy (training signal × correction granularity) for learned activation sparsity in SwiGLU LLMs and conducts a systematic empirical study filling the previously unoccupied cell (per-token contextual + KL). Contrary to the natural hypothesis motivated by KL's gradient coupling, the paper finds that BCE+compensation (PPL 9.40±0.19) matches or slightly outperforms KL-only (PPL 9.80±0.87) at 50% sparsity on Llama 3.1 8B, while exhibiting 4.6× lower variance. Three negative results are reported: non-additive SPON+KL composition (additivity ratio 0.62), failure of s² scaling for the KL–BCE gap (R²=0.66), and reversal of KL advantage on Mistral-7B.\n\n---\n\n## 2. Strengths\n\n- **Well-structured characterization study with principled ablation design.** The four-condition matrix (loss × compensation), STE isolation (Table 4), iso-compute comparison (Table 5), and SPON composition analysis form a rigorous experimental scaffolding. Each ablation targets a specific confound. This level of systematic control exceeds the norm for the activation sparsity subfield.\n\n- **Honest reporting of negative results.** The paper set out to show KL eliminates compensation and found the opposite. Publishing this with full transparency (additivity ratio 0.62, R²=0.66, direction reversal on Mistral) is scientifically valuable. The reframing from \"KL eliminates compensation\" to \"compensation is the universal mechanism\" is intellectually honest and potentially more useful to practitioners than a positive result would be.\n\n- **Comprehensive evaluation breadth.** 12 benchmarks across perplexity, discriminative tasks, long-context (LongBench, RULER), instruction-following (MT-Bench), inference profiling, and cross-architecture validation. The per-task-type breakdowns (LongBench Table 16, RULER Table 18) are appropriately granular.\n\n- **Variance as a first-class metric.** Reporting that KL-only has 4.6× higher seed variance than BCE+comp (0.87 vs 0.19) is an underappreciated contribution. For deployment, predictability matters as much as mean performance. This finding has immediate practical implications.\n\n- **The taxonomy has genuine organizational value.** Table 1 clearly maps prior work (SPON, ShadowLLM, FastForward) and identifies the empty cell. Even if not a deep theoretical contribution, it provides a useful mental model for the field.\n\n- **Inference cost co-reported with quality.** Table 11 (1.35×/48MB for KL-only vs 1.19×/304MB for BCE+comp) ensures claims are grounded in deployment reality.\n\n---\n\n## 3. Weaknesses\n\n### 3.1 Major\n\n**(W1) The core contribution is a characterization study with no new method, facing a steep novelty bar.**\nThe paper introduces no new architecture, training algorithm, or theoretical framework. The taxonomy is organizational; the experiments combine existing components (Gumbel-sigmoid predictor, KL/BCE losses, SPON bias correction, compensation MLP). For a venue with ~25% acceptance rate, characterization studies must compensate with either (a) deeply surprising findings that overturn community assumptions or (b) analytical depth explaining *why* observed patterns occur. The paper achieves (a) partially (the negative result is mildly surprising, but the prior that \"KL eliminates compensation\" was not widely held — SPON is the only related work, addressing static correction). It does not achieve (b): the discussion of *why* BCE+comp outperforms KL-only (§6) is speculative and does not go beyond restating observations.\n\n**(W2) The gradient coupling argument is presented but then empirically refuted, creating unresolved narrative tension.**\n§3 motivates KL via gradient coupling: KL's gradient couples all neurons through the Jacobian while BCE factorizes. This is mathematically correct but is a property of ANY output-level loss (MSE on logits, JS divergence, reverse KL would all exhibit the same coupling). More importantly, the paper's own results show this coupling does NOT translate to better quality — BCE+comp beats KL-only. The paper attributes this to \"Lagrangian instability\" and \"phase transitions\" (§6) without rigorous evidence. The disconnect between theoretical motivation (§3) and empirical outcome (§5) is the paper's central intellectual weakness. A stronger paper would provide a theoretical explanation for why gradient coupling is necessary but not sufficient, or identify the specific failure mode of KL training that compensation circumvents.\n\n**(W3) Missing MSE-on-logits baseline undermines the gradient coupling narrative.**\nThe gradient coupling property highlighted in §3 applies identically to MSE on output logits. Without this baseline, the paper cannot determine whether KL's specific properties (distributional matching, information-geometric structure) matter, or whether any output-level loss would perform similarly. Given that the paper frames its contribution around the training signal axis of the taxonomy, this omission is critical. The \"Intermediate (MSE)\" column in Table 1 has no per-token contextual entry — this is a gap in the very taxonomy the paper proposes.\n\n**(W4) BCE baseline fairness is questionable.**\nBCE-only achieves 28.16 PPL, dramatically worse than training-free TEAL (~12-13 PPL). A *trained* predictor performing worse than a zero-parameter magnitude heuristic is anomalous. Concerns:\n- Was BCE trained with Gumbel-sigmoid? For a binary target, STE is the natural relaxation. The STE ablation (Table 4) tests STE+KL but never STE+BCE, creating asymmetry.\n- How are BCE oracle targets generated? If by top-k activation magnitude, the targets themselves are suboptimal. KL implicitly discovers better masks.\n- The Lagrangian mechanism gives KL a more sophisticated optimization landscape than vanilla BCE. Did BCE receive comparable engineering attention?\n- In the FastForward paper, BCE+comp reportedly approaches dense quality. The gap here needs explicit comparison with published FastForward numbers.\n\nWithout a BCE+STE condition and transparency about target generation, the BCE baseline's weakness is a confound.\n\n### 3.2 Moderate\n\n**(W5) Related work is severely underdeveloped for a paper claiming a taxonomic contribution.**\nCritical missing citations: Deja Vu (ICML 2023, foundational contextual sparsity predictor), CATS (contextual thresholding for SwiGLU), Minitron (NeurIPS 2024, KL for structured pruning), DIP (MLSys 2025, predictor-free dynamic pruning for SwiGLU), Gumbel-Softmax foundations (Jang et al. 2017, Maddison et al. 2017), L0 regularization (Louizos et al. 2018), Sparsing Law (Luo et al. 2024), ReLU Strikes Back/TurboSparse/ProSparse (activation function replacement), MoE routing literature, and knowledge distillation beyond Hinton 2015.\n\n**(W6) Lagrangian sparsity enforcement mechanism is underspecified.**\nKL training collapsed to 0% sparsity, required normalization fixes, had a bug producing false positives, and took multiple iterations to stabilize. Yet the paper does not fully specify lambda initialization, update schedule, clamping bounds, or sensitivity analysis. This is critical for reproducibility and creates an asymmetry in training infrastructure between KL and BCE.\n\n**(W7) Statistical rigor is insufficient for the claims made.**\n- Unequal seed counts (3 vs 5) across conditions with no justification.\n- The headline comparison (9.40±0.19 vs 9.80±0.87) has overlapping confidence intervals. No formal significance test is reported.\n- Sparsity sweep uses 1 seed per level. R²=0.66 with 7 single-seed points cannot distinguish between functional forms. No AIC/BIC comparison provided.\n- Additivity ratio 0.62 reported without confidence intervals or statistical test for deviation from 1.0.\n\n**(W8) The \"phase transitions vs scaling laws\" framing (§6) is speculative.**\nNo phase transition is demonstrated (e.g., sharp discontinuity), no theoretical mechanism is proposed, and \"phase transition\" is used loosely. The discussion reads as post-hoc rationalization of R²=0.66.\n\n### 3.3 Minor\n\n**(W9)** Only 7-8B scale tested. The \"compensation is universal\" claim is validated at a single model scale.\n\n**(W10)** Calibration data sensitivity unexamined. Training uses WikiText-103, evaluation on WikiText-2. No domain sensitivity analysis.\n\n**(W11)** 512-token training sequences acknowledged but not analyzed. LongBench/RULER degradation could be a training artifact.\n\n---\n\n## 4. Questions for Authors\n\n1. **What happens with MSE on output logits as the training loss?** This is the single most informative missing experiment.\n\n2. **Was BCE trained with Gumbel-sigmoid relaxation?** If so, what happens with STE+BCE?\n\n3. **How are BCE oracle targets generated?** Top-k by activation magnitude? How do KL's implicitly learned masks differ?\n\n4. **The headline PPL gap (9.40 vs 9.80) falls within overlapping standard deviations. Can you provide a formal significance test?**\n\n5. **Why is BCE-only (28.16 PPL) worse than training-free TEAL?** If this reflects a genuine phenomenon, it deserves analysis. If inadequate tuning, it undermines the comparison.\n\n6. **What are the Lagrangian hyperparameters?** How sensitive is KL training to these settings?\n\n7. **At what sparsity level does KL-only start to need compensation?**\n\n8. **Can you explain the Mistral direction reversal mechanistically?** What specific property of GQA + sliding window drives this?\n\n---\n\n## 5. Detailed Comments on Novelty and Positioning\n\nThe paper sits at the intersection of two established techniques: KL distillation (standard since Hinton 2015) and learned sparsity prediction (standard since Deja Vu 2023). SPON already demonstrated KL works for sparsity in SwiGLU LLMs. Testing KL for contextual prediction is the natural next step the taxonomy itself identifies. The gradient coupling analysis follows trivially from the chain rule and applies to any output-level loss.\n\nThe most genuinely novel contribution is the negative result: compensation is more robust than gradient coupling. However, impact is weakened by: (a) narrow effect size (9.40 vs 9.80, potentially non-significant), (b) unresolved BCE fairness concerns, and (c) lack of mechanistic explanation.\n\nFraming as \"characterization study\" is the correct strategic choice, but characterization is incomplete: MSE-logits cell is empty, related work does not comprehensively map the field, and discussion lacks analytical depth.\n\nSuccessful characterization studies at top venues typically have much larger scope, deeply surprising findings, or actionable causal guidelines. This paper has moderate scope, a mildly surprising finding with caveats, and limited causal analysis.\n\n---\n\n## 6. Writing Quality\n\n- Organization is clear. Taxonomy-first structure followed by systematic experiments is logical.\n- Claims are mostly well-calibrated, except the \"phase transition\" speculation in §6.\n- Narrative arc has a bait-and-switch quality: §1/§3 build up the KL hypothesis, then §5 knocks it down. Cleaner to frame the question as genuinely open from the start.\n- Table density is high (18 tables in 11 pages). Several tables could be merged.\n- Discussion section (§6) is the weakest: \"phase transitions\" and \"Lagrangian instability\" invoked without evidence.\n- Bibliography is too thin (~8 references for a taxonomy paper).\n\n---\n\n## 7. Score and Recommendation\n\n**Score: 3/6 (Weak Reject)**\n**Confidence: 4/5**\n\n**Justification:** The paper asks a good question (does KL training eliminate compensation?) and provides an honest, well-structured empirical answer (no). Evaluation breadth is commendable and reporting negative results has scientific value. However, three converging problems prevent acceptance: (1) thin novelty (loss function swap in existing pipeline, organizational taxonomy), (2) unresolved experimental concerns (missing MSE-logits baseline, BCE fairness, insufficient statistical rigor for narrow effect size), and (3) inadequate analytical depth (no mechanistic explanation for compensation's advantage, speculative discussion, severely underdeveloped related work).\n\n**What would change the score:**\n- MSE-logits baseline + BCE+STE control resolving fairness: +0.5 to +1.0\n- Mechanistic explanation for compensation's advantage (not speculation): +0.5\n- Comprehensive related work (20+ references): +0.5\n- Formal significance tests confirming 9.40 vs 9.80 gap: +0.5\n- If BCE baseline found unfairly weak: −1.0 (to 2/6 Reject)\n\n---\n\n## 8. Missing Experiments (Priority-Ordered)\n\n1. **MSE-on-logits baseline** — Highest priority. Distinguishes \"KL is special\" from \"any output-level loss beats BCE.\"\n2. **BCE+STE baseline** — Ensures BCE uses its natural relaxation.\n3. **BCE with KL-optimal targets** — Disentangles loss from target quality.\n4. **Per-layer PPL decomposition** — Which layers drive the KL-BCE gap?\n5. **Formal significance tests** — Paired bootstrap on headline; AIC/BIC for scaling fit.\n6. **Lagrangian sensitivity analysis** — Required for reproducibility.\n7. **Predictor rank sensitivity** — At least one alternative (r=64 or r=256).",
  "project": "distill_sparse_swiglu",
  "tier": "worst",
  "dream_id": "dream_20260515T164925",
  "overall_score": "3/6 Weak Reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76aba766-ace1-4a74-ace4-6ab76222b2d9",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nNwEdtCwLqFK5WzPEt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eee940ae-5612-446f-8163-3d198e437a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiYGtSouG1UFnLv4pYZEpn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 72870,
      "output_tokens": 8654,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 706
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8654,
          "cache_read_input_tokens": 72870,
          "cache_creation_input_tokens": 706,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 706,
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

_source line 51 · 2026-05-15T17:57:22.495Z_

<details><summary>↩ Tool result · `toolu_01TxvYGW3diBRePuGUbgWYxt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_report.md\", \"dream_id\": \"dream_20260515T164925\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eee940ae-5612-446f-8163-3d198e437a92",
  "isSidechain": true,
  "promptId": "abaede90-a48f-465b-ba47-5d2d831c77c8",
  "agentId": "abd824c7996585d9b",
  "type": "user",
  "uuid": "1dd675b8-6905-494d-b131-a471c647d3ba",
  "sourceToolAssistantUUID": "eee940ae-5612-446f-8163-3d198e437a92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-15T17:57:32.224Z_

Review submitted successfully. Here is a summary of the review:

---

**Score: 3/6 (Weak Reject) | Confidence: 4/5**

**Key findings:**

The paper is a well-structured characterization study with commendable evaluation breadth (12 benchmarks, 2 architectures) and honest negative results. However, it faces three converging problems that prevent acceptance at a ~25% acceptance rate venue:

**Major weaknesses:**
1. **Thin novelty** -- The contribution is a loss function swap in an existing pipeline. The taxonomy is organizational, not technical. No new method, architecture, or theoretical framework is introduced.
2. **Unresolved narrative tension** -- The gradient coupling motivation (Section 3) is empirically refuted by the results (Section 5), but the paper provides no mechanistic explanation for *why* compensation outperforms KL coupling. The discussion resorts to speculation about "phase transitions" and "Lagrangian instability."
3. **Missing critical baselines** -- MSE-on-logits (which would have the same gradient coupling as KL) and BCE+STE (to ensure BCE uses its natural relaxation) are absent, leaving the core claims untestable.
4. **BCE fairness concerns** -- BCE-only (28.16 PPL) being worse than training-free TEAL is anomalous and raises implementation questions.

**Moderate weaknesses:** Severely underdeveloped related work for a taxonomy paper, underspecified Lagrangian mechanism, insufficient statistical rigor (headline gap 9.40 vs 9.80 may not be significant), speculative discussion section.

**Path to acceptance:** Run MSE-logits and BCE+STE baselines, add formal significance tests, expand related work to 20+ references, provide mechanistic explanation for compensation's advantage, and fully specify the Lagrangian training recipe.

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dd675b8-6905-494d-b131-a471c647d3ba",
  "isSidechain": true,
  "agentId": "abd824c7996585d9b",
  "requestId": "req_011Cb4nbwAXskohLhGeMdfDz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33ff2a8d-e967-4a92-8878-214c98d709c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "ea246f80-3204-4c6f-a88a-431a28811afc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGM14WQyJicFpdxP36Ybht",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8786,
      "cache_read_input_tokens": 73576,
      "output_tokens": 487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 487,
          "cache_read_input_tokens": 73576,
          "cache_creation_input_tokens": 8786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8786,
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
