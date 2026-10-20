# Research conversation: You are Reviewer 1 (R1) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aae4905719a5bc744.jsonl`
- **Structured JSON:** [`787d53e46f0829ca5670.json`](../../sessions/78/787d53e46f0829ca5670.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-17T01:19:27.991Z_

You are Reviewer 1 (R1) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **Methods and Experiments**: soundness, reproducibility, statistical rigor, experimental coverage, and whether claims are adequately supported.

## Paper Summary

Title: "Phase-Gated Compound Sparsity: Reasoning Phase Modulates the Severity of Pruning-Eviction Interactions in Large Language Models"

The paper studies compound sparsity (simultaneous attention head pruning + KV cache eviction) and claims that the interaction severity is not uniform but depends on reasoning phase and eviction strategy. Key contributions:

1. Discovery that compound sparsity severity is an emergent property of strategy × phase interaction, with importance-based eviction producing monotonically increasing phase gradients (paired median difference 0.39 to 8.48 on MATH-500, 0.96 to 8.12 on GPQA-Diamond).
2. Introduction of recency-based eviction as a scoring-independent methodological control, establishing a triple dissociation.
3. Proposed "discrimination collapse" mechanism: head pruning reduces importance score discriminability, causing phase-selective degeneration.
4. Validation across 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, DeepSeek-R1-Distill-Llama-8B), 2 architectures (Qwen2, Llama), 3 benchmarks (MATH-500, GSM8K, GPQA-Diamond).

## Methods Details

- Compound sparsity: simultaneous head pruning (fraction s of heads by output norm magnitude) + KV eviction (fraction s of KV pairs by strategy) at s ∈ {0.15, 0.20, 0.25, 0.30}
- Interaction Index II_i = PPL_both - (PPL_prune + PPL_evict - PPL_base) — excess perplexity beyond additive prediction
- Phase segmentation: tokens assigned to low/mid/high phases by tertile of per-token perplexity from uncompressed model
- Three eviction strategies: importance (H2O-style accumulated attention scores), random, recency (oldest tokens first, no attention scores)
- Statistical methodology: paired bootstrap (B=10,000), Wilcoxon signed-rank with Bonferroni, Cohen's d_z

## Key Results

Table 1 (Triple dissociation, MATH-500, DeepSeek-R1-Distill-Qwen-7B, n=100):
- s=0.15: Importance dz=0.57 (sig), Recency dz=0.08 (NS), Random dz=0.12 (NS)
- s=0.25: Importance dz=0.95 (sig), Recency dz=0.11 (NS), Random dz=0.12 (NS)
- s=0.30: Importance dz=1.13 (sig), Recency dz=0.15 (NS), Random dz=0.18 (NS)

Table 2 (Recency at s=0.25): Low-phase II median 0.87, High-phase 0.82, ratio 1.06, dz=0.11, imp/recency ratio 36×
Table 3 (Recency at s=0.30): Low-phase II median 1.52, High-phase 1.38, ratio 1.10, dz=0.15, imp/recency ratio 207×
Table 4 (GPQA dose-response, importance, n=198): s=0.15 IIlow=0.96, s=0.20 IIlow=2.85 dz=0.92, s=0.25 IIlow=8.12 dz=1.08
Table 5 (Strategy specificity): MATH-500 15-17×, GPQA 4.2×, GSM8K 2.3-3.8×

Perplexity analysis: GPQA s=0.25 low-phase PPL=95.6 vs high-phase 4.8 (19.9× ratio)

Discrimination collapse: Gini coefficient and CV decline across models (correlational, not causal).

## Review Context (experiment design file)

The full experiment plan includes:
- Recency controls at s=0.25 and s=0.30 (both present in paper)
- GPQA cross-benchmark at s=0.20 and s=0.25 (both present in paper)
- Imagined reviewer scores avg 3.7

## Your Task

Write a detailed review covering:
1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, focus on methodology and experiments)
3. **Weaknesses** (bullet points, focus on methodology and experiments)
4. **Questions for Authors** (specific, actionable)
5. **Minor Issues**
6. **Scores**: Overall (1-6), Soundness (1-5), Presentation (1-5), Confidence (1-5)

Be rigorous. Consider: Is the interaction index well-defined? Is the phase segmentation circular? Are sample sizes adequate? Is the statistical methodology appropriate? Are there confounds not addressed? Is discrimination collapse adequately supported? Are the claimed contributions matched by the evidence?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "d2776593-88a7-44ec-8f44-6d249dde85a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T01:19:27.996Z_

```json
{
  "parentUuid": "d2776593-88a7-44ec-8f44-6d249dde85a5",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
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
  "uuid": "45d066a6-0bdc-48bf-9ca8-452a0139914a",
  "timestamp": "2026-05-17T01:19:27.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T01:19:31.296Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Wttxp8dMiXaJZihwkUMUQ6`</summary>

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
  "parentUuid": "45d066a6-0bdc-48bf-9ca8-452a0139914a",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8A1gtsmeeLFrdBcvB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d936833-b984-4add-946e-7e504047a3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hy8gqimgg3gW2tZom3ZB4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16658,
      "cache_read_input_tokens": 0,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16658
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16658,
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

_source line 4 · 2026-05-17T01:19:31.302Z_

<details><summary>↩ Tool result · `toolu_01Wttxp8dMiXaJZihwkUMUQ6`</summary>

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
  "parentUuid": "5d936833-b984-4add-946e-7e504047a3c0",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "7f0a1388-ced0-4916-b276-82051f5360c1",
  "sourceToolAssistantUUID": "5d936833-b984-4add-946e-7e504047a3c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T01:19:34.947Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H4YR68qnCRR7rmjAzyecYV`</summary>

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
  "parentUuid": "7f0a1388-ced0-4916-b276-82051f5360c1",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8REj54kdphYuCK7v5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e60d301-d8f2-48bf-86ef-2e34ed9d11a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134BZwvjempiqz88e4B8oMS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1270,
      "cache_read_input_tokens": 16658,
      "output_tokens": 110,
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
          "output_tokens": 110,
          "cache_read_input_tokens": 16658,
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

_source line 6 · 2026-05-17T01:19:34.963Z_

<details><summary>↩ Tool result · `toolu_01H4YR68qnCRR7rmjAzyecYV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_random_s020 | Cross-task generalization: random eviction control on GPQA Diamond. DS-R1 random s020 to establish baseline phase gradient (expected NS or weak) for strategy specificity comparison. | — | — | — |\\n| gpqa_ds_importance_s030 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s030 as fourth condition. | — | — | — |\\n| gpqa_ds_importance_s025 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition. DS-R1 importance s025 as third condition (after s015 success, s020 running). | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **recency_s025** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.25 condition.\\n  [recency_s025_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s025/report/analysis.md)\\n- **recency_s030** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.30 condition.\\n  [recency_s030_analysis](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/recency_s030/report/analysis.md)\\n- **recency_s015** (success): Recency-based (position-only) eviction as scoring-independent control to disentangle phase segmentation circularity and H2O confound from attention-score-specific compound interaction. s=0.15 condition.\\n\\n## 趋势\\n成功 70 / 负向 17 / 失败 17 / 共 134\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 3667, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e60d301-d8f2-48bf-86ef-2e34ed9d11a1",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "06bbf6c2-9c95-403f-aa2f-5e402a19e18d",
  "sourceToolAssistantUUID": "4e60d301-d8f2-48bf-86ef-2e34ed9d11a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T01:19:38.266Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UzLWyjPSt8R5XpPTcgBK7K`</summary>

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
  "parentUuid": "06bbf6c2-9c95-403f-aa2f-5e402a19e18d",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8fxkcraVA7gxqaiH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6b9bc2b-a467-471a-9c1f-a0e1a73006ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V33zZEuvNGEZJ3Jghh2rZN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 17928,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-17T01:19:38.299Z_

<details><summary>↩ Tool result · `toolu_01UzLWyjPSt8R5XpPTcgBK7K`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6b9bc2b-a467-471a-9c1f-a0e1a73006ff",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "15503653-30db-4357-87e3-8c8f7e3fcc20",
  "sourceToolAssistantUUID": "e6b9bc2b-a467-471a-9c1f-a0e1a73006ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T01:19:38.431Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011NHUPwNW3nxkFKp5H3RKB7`</summary>

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
  "parentUuid": "15503653-30db-4357-87e3-8c8f7e3fcc20",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8fxkcraVA7gxqaiH7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d00de0de-0f1e-4f63-820a-3dff63774836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V33zZEuvNGEZJ3Jghh2rZN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 17928,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 17928,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-17T01:19:38.440Z_

<details><summary>↩ Tool result · `toolu_011NHUPwNW3nxkFKp5H3RKB7`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'phase-gated-compound-sparse'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d00de0de-0f1e-4f63-820a-3dff63774836",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "06d8ca1b-b6bf-494e-bceb-1c27a69cf761",
  "sourceToolAssistantUUID": "d00de0de-0f1e-4f63-820a-3dff63774836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T01:19:41.202Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HjsWeeHSRRENjeVfgEyWRq`</summary>

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
  "parentUuid": "06d8ca1b-b6bf-494e-bceb-1c27a69cf761",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8vtBVDwaZLXViyxrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e17a213-046b-4a2e-b885-c9e38a7cfee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cQoe5pv4wAwk62sM3ji5w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 746,
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

_source line 12 · 2026-05-17T01:19:41.218Z_

<details><summary>↩ Tool result · `toolu_01HjsWeeHSRRENjeVfgEyWRq`</summary>

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
  "parentUuid": "4e17a213-046b-4a2e-b885-c9e38a7cfee0",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "e2e0b228-e41f-49dc-a1bb-7c25272d18c8",
  "sourceToolAssistantUUID": "4e17a213-046b-4a2e-b885-c9e38a7cfee0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T01:19:42.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xu5DcQUH5CLXHSVuwUkNQz`</summary>

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
  "parentUuid": "e2e0b228-e41f-49dc-a1bb-7c25272d18c8",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8vtBVDwaZLXViyxrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcf5b06d-c9ba-415d-881e-3d8a121b2ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cQoe5pv4wAwk62sM3ji5w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 746,
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

_source line 14 · 2026-05-17T01:19:42.186Z_

<details><summary>↩ Tool result · `toolu_01Xu5DcQUH5CLXHSVuwUkNQz`</summary>

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
  "parentUuid": "dcf5b06d-c9ba-415d-881e-3d8a121b2ebf",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "3733809f-1acc-43d7-a5c6-a54a48ae1ced",
  "sourceToolAssistantUUID": "dcf5b06d-c9ba-415d-881e-3d8a121b2ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T01:19:42.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_016GiqhgbU1EWf9SA7BeuLk3`</summary>

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
  "parentUuid": "3733809f-1acc-43d7-a5c6-a54a48ae1ced",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G8vtBVDwaZLXViyxrn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a9c80c7-b7be-44f5-8cd1-3bc1630f680d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cQoe5pv4wAwk62sM3ji5w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19841,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 746
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 19841,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 746,
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

_source line 16 · 2026-05-17T01:19:42.354Z_

<details><summary>↩ Tool result · `toolu_016GiqhgbU1EWf9SA7BeuLk3`</summary>

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
  "parentUuid": "0a9c80c7-b7be-44f5-8cd1-3bc1630f680d",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "e8f4ec96-717f-4e1a-a65d-aca6227d50cf",
  "sourceToolAssistantUUID": "0a9c80c7-b7be-44f5-8cd1-3bc1630f680d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T01:19:47.132Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SdyfxWeYcdYWgguD3riKEt`</summary>

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
  "parentUuid": "e8f4ec96-717f-4e1a-a65d-aca6227d50cf",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9DdFoDftdcSqJwRHe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "916976cd-4b0c-46ef-838b-15458eb572c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWYsrazYRe5ujzmtok2mcg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10568,
      "cache_read_input_tokens": 20587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10568,
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

_source line 18 · 2026-05-17T01:19:47.143Z_

<details><summary>↩ Tool result · `toolu_01SdyfxWeYcdYWgguD3riKEt`</summary>

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
  "parentUuid": "916976cd-4b0c-46ef-838b-15458eb572c2",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "4023934d-39b2-44fc-9570-e3d4b249e38a",
  "sourceToolAssistantUUID": "916976cd-4b0c-46ef-838b-15458eb572c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T01:19:47.670Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ue6dvaprcqfwQWabKzNDtm`</summary>

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
  "parentUuid": "4023934d-39b2-44fc-9570-e3d4b249e38a",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9DdFoDftdcSqJwRHe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12ec8796-078f-4c64-98a2-48a3be394d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWYsrazYRe5ujzmtok2mcg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10568,
      "cache_read_input_tokens": 20587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10568,
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

_source line 20 · 2026-05-17T01:19:47.676Z_

<details><summary>↩ Tool result · `toolu_01Ue6dvaprcqfwQWabKzNDtm`</summary>

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
  "parentUuid": "12ec8796-078f-4c64-98a2-48a3be394d97",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "81fdbda2-fb33-4e7d-9267-589d2b649dca",
  "sourceToolAssistantUUID": "12ec8796-078f-4c64-98a2-48a3be394d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T01:19:47.949Z_

<details open><summary>🔧 Tool call — Read · `toolu_019heR7EpmS59KMeyoeC8r5S`</summary>

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
  "parentUuid": "81fdbda2-fb33-4e7d-9267-589d2b649dca",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9DdFoDftdcSqJwRHe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32c19f7a-2154-4a43-8fff-a11d66131a8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JWYsrazYRe5ujzmtok2mcg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10568,
      "cache_read_input_tokens": 20587,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10568
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 20587,
          "cache_creation_input_tokens": 10568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10568,
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

_source line 22 · 2026-05-17T01:19:47.954Z_

<details><summary>↩ Tool result · `toolu_019heR7EpmS59KMeyoeC8r5S`</summary>

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
  "parentUuid": "32c19f7a-2154-4a43-8fff-a11d66131a8f",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "2b12d359-628a-4831-893c-0c2d77c1cc7f",
  "sourceToolAssistantUUID": "32c19f7a-2154-4a43-8fff-a11d66131a8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T01:19:50.763Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C7q7t29FEYJhtqLxoo4gwh`</summary>

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
  "parentUuid": "2b12d359-628a-4831-893c-0c2d77c1cc7f",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9dauMGiiqmxFun2FZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d542f1d-23cd-4a98-be29-027aef2b02c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GBiuJzHbxT8Q44wqre9QK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 31155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3654,
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

_source line 24 · 2026-05-17T01:19:50.769Z_

<details><summary>↩ Tool result · `toolu_01C7q7t29FEYJhtqLxoo4gwh`</summary>

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
  "parentUuid": "3d542f1d-23cd-4a98-be29-027aef2b02c2",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "71eb7114-f1cc-4ddf-9274-aa6c9c7eaa59",
  "sourceToolAssistantUUID": "3d542f1d-23cd-4a98-be29-027aef2b02c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T01:19:51.354Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Mq9E5RawbKYKCtBS9rukKc`</summary>

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
  "parentUuid": "71eb7114-f1cc-4ddf-9274-aa6c9c7eaa59",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9dauMGiiqmxFun2FZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f9bff1c7-79e8-4eda-bce1-c3d36e4634bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GBiuJzHbxT8Q44wqre9QK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 31155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3654,
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

_source line 26 · 2026-05-17T01:19:51.360Z_

<details><summary>↩ Tool result · `toolu_01Mq9E5RawbKYKCtBS9rukKc`</summary>

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
  "parentUuid": "f9bff1c7-79e8-4eda-bce1-c3d36e4634bc",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "3d4115ed-b183-4041-ad65-3da3dc33fbfb",
  "sourceToolAssistantUUID": "f9bff1c7-79e8-4eda-bce1-c3d36e4634bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T01:19:51.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_013vSkZDXQbcbu2RaVfWTinM`</summary>

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
  "parentUuid": "3d4115ed-b183-4041-ad65-3da3dc33fbfb",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9dauMGiiqmxFun2FZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4abb0fe6-78f4-41df-8c69-6f4135d776ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GBiuJzHbxT8Q44wqre9QK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3654,
      "cache_read_input_tokens": 31155,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3654
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 31155,
          "cache_creation_input_tokens": 3654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3654,
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

_source line 28 · 2026-05-17T01:19:51.799Z_

<details><summary>↩ Tool result · `toolu_013vSkZDXQbcbu2RaVfWTinM`</summary>

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
  "parentUuid": "4abb0fe6-78f4-41df-8c69-6f4135d776ab",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "b420f7b8-387e-402c-83f5-b22e15dd7f8d",
  "sourceToolAssistantUUID": "4abb0fe6-78f4-41df-8c69-6f4135d776ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T01:19:57.242Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VHAVjxP6PbaUikxPeho2wn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b420f7b8-387e-402c-83f5-b22e15dd7f8d",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7G9v7aWV9Wra6s8YutK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ebfb40b-1988-4f56-a86a-ba0bc4b12d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016tAafqHFKues8uTKvwGzUN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5591,
      "cache_read_input_tokens": 34809,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5591
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 34809,
          "cache_creation_input_tokens": 5591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5591,
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

_source line 30 · 2026-05-17T01:19:57.253Z_

<details><summary>↩ Tool result · `toolu_01VHAVjxP6PbaUikxPeho2wn`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Notably, $\mathrm{II}_{\times} < 0$ across all phases and sparsity levels: the compound interaction is \emph{sub-multiplicative} everywhere---actual compound degradation is less severe than the multiplicative prediction. $G_{\times}$ therefore quantifies the ratio of sub-multiplicative deviations between phases, not super-multiplicative amplification: a value of $G_{\times}{=}30$ means the low-sparsity phase deviates from the multiplicative null by $30{\times}$ more than the high-sparsity phase. Under importance-based eviction, $G_{\times}{=}21.1$--$36.2{\times}$ (DeepSeek) and $43.9$--$64.0{\times}$ (Qwen) across $s \in \{0.15, 0.20, 0.25, 0.30\}$, yielding a combined range of $21$--$64{\times}$. Although compound effects do not exceed the multiplicative prediction in any phase, the low-sparsity phase's deviation from the multiplicative null is $21$--$64{\times}$ larger than the high-sparsity phase's, indicating that the phase-gated severity gradient is preserved under the multiplicative null. These $n{=}500$ exact values are more conservative than the preliminary $n{=}50$ calibrated estimates ($\approx$51--183${\times}$), reflecting reduced variance at full sample size. Values are computed using aggregate per-phase PPL ratios; per-problem exact computation is left for future work. Random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text as the more conservative baseline: it assumes zero interaction (compound loss equals the sum of individual losses), so rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. The qualitative conclusions---phase-modulated severity, strategy asymmetry, and crossover---are preserved under the multiplicative null.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ebfb40b-1988-4f56-a86a-ba0bc4b12d2a",
  "isSidechain": true,
  "promptId": "e094363e-fd4f-4649-8867-0eb6b8a0e169",
  "agentId": "aae4905719a5bc744",
  "type": "user",
  "uuid": "42618708-d5af-45b7-a1b8-5eca37896280",
  "sourceToolAssistantUUID": "0ebfb40b-1988-4f56-a86a-ba0bc4b12d2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T01:21:07.574Z_

Now I have a comprehensive view of the paper. Let me write my review.

---

## Review: "Phase-Gated Compound Sparsity: Reasoning Phase Modulates the Severity of Pruning-Eviction Interactions in Large Language Models"

### 1. Summary

This paper investigates how simultaneously pruning attention heads and evicting KV cache entries (compound sparsity) produces super-additive quality degradation that varies across reasoning phases. The authors define an Interaction Index (II) and segment generated sequences into phases by attention sparsity terciles, finding that importance-based eviction creates a large, monotonically increasing phase-severity gradient absent under recency-based and largely absent under random eviction. The work is primarily a diagnostic characterization study validated across 3 models, 2 architectures, and 3 benchmarks.

### 2. Strengths

- **Well-defined statistical framework.** The paired within-problem design (bootstrapped CIs, Wilcoxon signed-rank, Bonferroni correction, Jonckheere-Terpstra for monotonicity) is appropriate for the data structure. Reporting medians given heavy right-skew is the correct choice, and the paper is transparent about distribution properties.

- **Recency control is methodologically valuable.** Introducing a scoring-independent eviction strategy that removes the attention-score feedback loop is a clean experimental design choice. The triple dissociation (importance: positive gradient; random: weak/absent; recency: absent/negative) provides genuine mechanism discrimination.

- **Sample sizes and effect sizes are strong for the primary claim.** n=496/475 on MATH-500 with Cohen's d_z values of 0.57-1.13 represents solid statistical power. The 15-17x strategy specificity ratio on DeepSeek is large and unlikely artifactual.

- **Honest reporting of limitations.** The paper acknowledges the correlational nature of discrimination collapse, the model-dependence of entropy redistribution, the truncation confound for DeepSeek accuracy, and the reduced strategy specificity on LLaMA. The authors do not overclaim.

- **Dual null verification.** Testing both additive and multiplicative null hypotheses for the Interaction Index, and showing qualitative conclusions hold under both, strengthens the core finding.

- **Robustness checks are thorough.** Segmentation granularity (tercile/quartile/quintile), minimum phase length sensitivity (5/10/20), BH-FDR correction, and the profiling-to-full-sample scaling analysis all address foreseeable objections.

### 3. Weaknesses

- **Circularity in phase segmentation.** Phases are defined by attention sparsity under the *dense* model, and then the paper measures perplexity-based interaction under *compound* sparsity within those boundaries. The implicit assumption is that the dense-model sparsity structure remains meaningful under compression. If head pruning reorganizes attention patterns (which the discrimination collapse mechanism itself suggests), the phase boundaries derived from the uncompressed model may not correspond to functional reasoning phases under compression. The think-token validation (kappa=0.88) is on GSM8K with n=48, a different benchmark than the primary evaluation (MATH-500), and only for DeepSeek. This is acknowledged but not adequately resolved.

- **Recency control has limited scope.** The recency experiment uses n=100 (vs. n=496 for the main results), only on DeepSeek, only on MATH-500. At s=0.30, the condition produces KV perplexity >10^5, rendering it "numerically unreliable." This means the control only clearly works at s=0.15 and s=0.25, exactly 2 clean data points for the primary falsification claim. The paper frames this as a "triple dissociation" but the recency arm is far less comprehensive than the other two.

- **GPQA and 14B scale results are placeholders.** Tables 6 and 7 contain "---" entries with comments like "Results pending." These are claimed contributions in the abstract (GPQA) and the paper body (14B scale), yet the actual data is missing. This is a significant gap between claimed scope and delivered evidence.

- **GSM8K evaluation is underpowered.** n=50 is stated explicitly, with post-hoc power analysis revealing ability to detect only d>=0.40. The random eviction non-significance on GSM8K could simply be a power issue, yet the paper interprets it as "reasoning depth scaling." The Qwen GSM8K data is acknowledged as unreliable due to truncation. This benchmark adds little probative value in its current state.

- **Discrimination collapse mechanism is underspecified.** The paper acknowledges this is correlational, but the core problem is deeper: both importance and random pruning produce similar Gini drops (~10% difference), yet severity diverges by 15-17x. The paper argues "structural specificity" bridges this gap (importance pruning removes low-Gini heads), but this explanation is presented with a single correlational statistic (Mann-Whitney, rank-biserial r=0.62-0.76) rather than a mechanistic model connecting head removal patterns to the observed 15-17x severity ratio. The gap between the correlational evidence and the magnitude of the phenomenon it purports to explain is large.

- **Symmetric sparsity is unrealistic.** The assumption s_head = s_kv is a strong simplification. Real deployment scenarios typically use different budgets for head pruning vs. KV eviction. The paper mentions an asymmetric spot check in the appendix but provides no systematic exploration. The findings may not transfer to the asymmetric case that practitioners actually encounter.

- **No downstream task metrics for the primary claim.** The core contribution is about II (perplexity-based). Accuracy validation is limited to n=100 (Qwen) and n=50 (DeepSeek, confounded). The paper argues that PPL enables per-token phase decomposition while accuracy does not, but this creates a circularity: the contribution is only demonstrable using the metric that the method was designed around. A practitioner cares about whether compound sparsity differentially hurts *correctness* by phase, not just perplexity.

- **Phase-strategy crossover inconsistency undermines generality.** The crossover (importance lower than random in high-phase, higher in low-phase) appears on DeepSeek but not Qwen. This model-dependence of a key qualitative finding weakens the claim that this is a general property of compound sparsity.

### 4. Questions for Authors

1. **Phase boundary stability under compression:** Have you measured what fraction of tokens change phase assignment when segmentation is re-computed under the compressed (compound sparsity) model rather than the dense model? If the phase boundaries shift substantially under compression, the dense-derived segmentation may not capture the relevant computational states during compressed inference.

2. **Recency at larger n:** Given the methodological centrality of the recency control, why was it not run at n=496 to match the main experiments? At n=100 with only 2 clean sparsity levels, the falsification is suggestive but not conclusive.

3. **Functional form of dose-response:** You report 4 sparsity levels and observe monotonicity. Is the relationship linear, exponential, or sigmoidal in s? With only 4 points, you cannot distinguish these, yet the practical implications differ enormously (exponential growth implies a hard sparsity ceiling; sigmoidal implies eventual saturation).

4. **What explains the 15-17x vs. 2.0-2.6x strategy specificity difference between Qwen2 and LLaMA?** The paper attributes this to "architectural details of the attention implementation" but does not specify which details. Is it GQA vs. MHA? Head count? If GQA, this has direct implications for nearly all modern architectures.

5. **Missing GPQA and 14B data:** Are these experiments still running, or did they fail? The presence of placeholder tables in a submission is unusual and raises concerns about the completeness of the work.

6. **Pilot mitigation failure:** The oracle phase-aware allocation achieved only 18% recovery (CI spanning zero). Does this undermine the practical relevance of the diagnostic framework? If knowing the phases does not help you compress better, what is the engineering utility beyond post-hoc diagnosis?

### 5. Minor Issues

- The title mentions "Reasoning Phase Modulates the Severity" but the abstract and body make clear this is an observational finding, not a demonstrated causal mechanism. The title implies more agency/causality than the evidence supports.
- Table captions marked "Results pending" should not appear in a submitted manuscript.
- The Spearman rho=1.0 with n=4 data points is trivially achievable for any monotone sequence and should not be presented as evidence (the paper acknowledges this in a footnote but still reports it prominently in the abstract).
- The think-token validation sample (n=48, GSM8K) is oddly specific; why not validate on the primary benchmark (MATH-500)?
- The paper references \cite{hies-2025} for discrimination collapse under single-axis pruning but does not discuss how their findings relate quantitatively to the compound setting.

### 6. Scores

| Criterion | Score |
|-----------|-------|
| **Overall** | 4 (Borderline Reject) |
| **Soundness** | 3/5 |
| **Presentation** | 4/5 |
| **Confidence** | 4/5 |

**Justification:** The paper presents a methodologically careful observational study with a well-designed statistical framework and a valuable recency control idea. However, the work has significant gaps: placeholder results for claimed contributions (GPQA, 14B), the recency control is underpowered relative to its centrality, the mechanism (discrimination collapse) is acknowledged as correlational yet still carries substantial narrative weight, and the practical utility is undermined by the failed pilot mitigation. The phase segmentation circularity concern (dense-model boundaries applied to compressed inference) is not fully resolved. The core observation (phase-dependent compound severity under importance eviction) is likely real and reproducible, but the paper as submitted is incomplete (missing tables) and the contribution magnitude is primarily diagnostic/observational rather than providing actionable methods. For a top venue at 25% acceptance, the work needs the missing experiments completed, stronger recency controls, and either a working mitigation strategy or a clearer articulation of why diagnosis alone merits acceptance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42618708-d5af-45b7-a1b8-5eca37896280",
  "isSidechain": true,
  "agentId": "aae4905719a5bc744",
  "requestId": "req_011Cb7GAKH74HkZCEKBCfMi6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd8e502c-befc-4b09-8087-decbb4201416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "133834fc-cdb1-4626-a41f-e256628bff5f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SvcazoP8nfymmx4PfaDq6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1645,
      "cache_read_input_tokens": 40400,
      "output_tokens": 2445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1645
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2445,
          "cache_read_input_tokens": 40400,
          "cache_creation_input_tokens": 1645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1645,
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
